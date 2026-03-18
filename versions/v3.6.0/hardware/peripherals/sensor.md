---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/sensor.html
original_path: hardware/peripherals/sensor.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Sensors

The sensor subsystem exposes an API to uniformly access sensor devices.
Common operations are: reading data and executing code when specific
conditions are met.

## Basic Operation

### Channels

Fundamentally, a channel is a quantity that a sensor device can measure.

Sensors can have multiple channels, either to represent different axes of
the same physical property (e.g. acceleration); or because they can measure
different properties altogether (ambient temperature, pressure and
humidity). Complex sensors cover both cases, so a single device can expose
three acceleration channels and a temperature one.

It is imperative that all sensors that support a given channel express
results in the same unit of measurement. Consult the
[API Reference](#sensor-api-reference) for all supported channels, along with their
description and units of measurement:

### Values

Sensor stable APIs return results as [`sensor_value`](#c.sensor_value). This
representation avoids use of floating point values as they may not be
supported on certain setups.

A newer experimental (may change) API that can interpret raw sensor data is
available in parallel. This new API exposes raw encoded sensor data to the
application and provides a separate decoder to convert the data to a Q31 format
which is compatible with the Zephyr [Digital Signal Processing (DSP)](../../services/dsp/index.md#zdsp-api). The values represented are
in the range of (-1.0, 1.0) and require a shift operation in order to scale
them to their SI unit values. See [Async Read](#async-read) for more information.

### Fetching Values

Getting a reading from a sensor requires two operations. First, an
application instructs the driver to fetch a sample of all its channels.
Then, individual channels may be read. In the case of channels with
multiple axes, they can be read in a single operation by supplying
the corresponding `_XYZ` channel type and a buffer of 3
[`sensor_value`](#c.sensor_value) objects. This approach ensures consistency
of channels between reads and efficiency of communication by issuing a
single transaction on the underlying bus.

Below is an example illustrating the usage of the BME280 sensor, which
measures ambient temperature and atmospheric pressure. Note that
[`sensor_sample_fetch()`](#c.sensor_sample_fetch) is only called once, as it reads and
compensates data for both channels.

```c
 1
 2/*
 3 * Get a device structure from a devicetree node with compatible
 4 * "bosch,bme280". (If there are multiple, just pick one.)
 5 */
 6static const struct device *get_bme280_device(void)
 7{
 8	const struct device *const dev = DEVICE_DT_GET_ANY(bosch_bme280);
 9
10	if (dev == NULL) {
11		/* No such node, or the node does not have status "okay". */
12		printk("\nError: no device found.\n");
13		return NULL;
14	}
15
16	if (!device_is_ready(dev)) {
17		printk("\nError: Device \"%s\" is not ready; "
18		       "check the driver initialization logs for errors.\n",
19		       dev->name);
20		return NULL;
21	}
22
23	printk("Found device \"%s\", getting sensor data\n", dev->name);
24	return dev;
25}
26
27int main(void)
28{
29	const struct device *dev = get_bme280_device();
30
31	if (dev == NULL) {
32		return 0;
33	}
34
35	while (1) {
36		struct sensor_value temp, press, humidity;
37
38		sensor_sample_fetch(dev);
39		sensor_channel_get(dev, SENSOR_CHAN_AMBIENT_TEMP, &temp);
40		sensor_channel_get(dev, SENSOR_CHAN_PRESS, &press);
41		sensor_channel_get(dev, SENSOR_CHAN_HUMIDITY, &humidity);
42
43		printk("temp: %d.%06d; press: %d.%06d; humidity: %d.%06d\n",
44		      temp.val1, temp.val2, press.val1, press.val2,
45		      humidity.val1, humidity.val2);
46
47		k_sleep(K_MSEC(1000));
48	}
49	return 0;
50}
```

### Async Read

To enable the async APIs, use [`CONFIG_SENSOR_ASYNC_API`](../../kconfig.md#CONFIG_SENSOR_ASYNC_API "CONFIG_SENSOR_ASYNC_API").

Reading the sensors leverages the [Real Time I/O (RTIO)](../../services/rtio/index.md#rtio-api) subsystem. Applications
gain control of the data processing thread and even memory management. In order
to get started with reading the sensors, an IODev must be created via the
[`SENSOR_DT_READ_IODEV`](#c.SENSOR_DT_READ_IODEV). Next, an RTIO context must be created. It is
strongly suggested that this context is created with a memory pool via
[`RTIO_DEFINE_WITH_MEMPOOL`](../../services/rtio/index.md#c.RTIO_DEFINE_WITH_MEMPOOL "RTIO_DEFINE_WITH_MEMPOOL").

```c
#include <zephyr/device.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/rtio/rtio.h>

static const struct device *lid_accel = DEVICE_DT_GET(DT_ALIAS(lid_accel));
SENSOR_DT_READ_IODEV(lid_accel_iodev, DT_ALIAS(lid_accel), SENSOR_CHAN_ACCEL_XYZ);

RTIO_DEFINE_WITH_MEMPOOL(sensors_rtio,
                         4,  /* submission queue size */
                         4,  /* completion queue size */
                         16, /* number of memory blocks */
                         32, /* size of each memory block */
                         4   /* memory alignment */
                         );
```

To trigger a read, the application simply needs to call [`sensor_read()`](#c.sensor_read)
and pass the relevant IODev and RTIO context. Getting the result is done like
any other RTIO operation, by waiting on a completion queue event (CQE). In
order to help reduce some boilerplate code, the helper function
[`sensor_processing_with_callback()`](#c.sensor_processing_with_callback) is provided. When called, the
function will block until a CQE becomes available from the provided RTIO
context. The appropriate buffers are extracted and the callback is called.
Once the callback is done, the memory is reclaimed by the memorypool. This
looks like:

```c
static void sensor_processing_callback(int result, uint8_t *buf,
                                       uint32_t buf_len, void *userdata) {
  // Process the data...
}

static void sensor_processing_thread(void *, void *, void *) {
  while (true) {
    sensor_processing_with_callback(&sensors_rtio, sensor_processing_callback);
  }
}
K_THREAD_DEFINE(sensor_processing_tid, 1024, sensor_processing_thread,
                NULL, NULL, NULL, 0, 0, 0);
```

Note

Helper functions to create custom length IODev nodes and ones that don’t
have static bindings will be added soon.

### Processing the Data

Once data collection completes and the processing callback was called,
processing the data is done via the [`sensor_decoder_api`](#c.sensor_decoder_api). The API
provides a means for applications to control *when* to process the data and how
many resources to dedicate to the processing. The API is entirely self
contained and requires no system calls (even when
[`CONFIG_USERSPACE`](../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") is enabled).

```c
static struct sensor_decoder_api *lid_accel_decoder = SENSOR_DECODER_DT_GET(DT_ALIAS(lid_accel));

static void sensor_processing_callback(int result, uint8_t *buf,
                                       uint32_t buf_len, void *userdata) {
  uint64_t timestamp;
  sensor_frame_iterator_t fit = {0};
  sensor_channel_iterator_t cit = {0};
  enum sensor_channel channels[3];
  q31_t values[3];
  int8_t shift[3];

  lid_accel_decoder->get_timestamp(buf, &timestamp);
  lid_accel_decoder->decode(buf, &fit, &cit, channels, values, 3);

  /* Values are now in q31_t format, we're going to convert them to micro-units */

  /* First, we need to know by how much to shift the values */
  lid_accel_decoder->get_shift(buf, channels[0], &shift[0]);
  lid_accel_decoder->get_shift(buf, channels[1], &shift[1]);
  lid_accel_decoder->get_shift(buf, channels[2], &shift[2]);

  /* Shift the values to get the SI units */
  int64_t scaled_values[] = {
    (int64_t)values[0] << shift[0],
    (int64_t)values[1] << shift[1],
    (int64_t)values[2] << shift[2],
  };

  /*
   * FIELD_GET(GENMASK64(63, 31), scaled_values[]) - will give the integer value
   * FIELD_GET(GENMASK64(30, 0), scaled_values[]) / INT32_MAX - is the decimal value
   */
}
```

## Configuration and Attributes

Setting the communication bus and address is considered the most basic
configuration for sensor devices. This setting is done at compile time, via
the configuration menu. If the sensor supports interrupts, the interrupt
lines and triggering parameters described below are also configured at
compile time.

Alongside these communication parameters, sensor chips typically expose
multiple parameters that control the accuracy and frequency of measurement.
In compliance with Zephyr’s design goals, most of these values are
statically configured at compile time.

However, certain parameters could require runtime configuration, for
example, threshold values for interrupts. These values are configured via
attributes. The example in the following section showcases a sensor with an
interrupt line that is triggered when the temperature crosses a threshold.
The threshold is configured at runtime using an attribute.

## Triggers

*Triggers* in Zephyr refer to the interrupt lines of the sensor chips.
Many sensor chips support one or more triggers. Some examples of triggers
include: new data is ready for reading, a channel value has crossed a
threshold, or the device has sensed motion.

To configure a trigger, an application needs to supply a
[`sensor_trigger`](#c.sensor_trigger) and a handler function. The structure contains the
trigger type and the channel on which the trigger must be configured.

Because most sensors are connected via SPI or I2C buses, it is not possible
to communicate with them from the interrupt execution context. The
execution of the trigger handler is deferred to a thread, so that data
fetching operations are possible. A driver can spawn its own thread to fetch
data, thus ensuring minimum latency. Alternatively, multiple sensor drivers
can share a system-wide thread. The shared thread approach increases the
latency of handling interrupts but uses less memory. You can configure which
approach to follow for each driver. Most drivers can entirely disable
triggers resulting in a smaller footprint.

The following example contains a trigger fired whenever temperature crosses
the 26 degree Celsius threshold. It also samples the temperature every
second. A real application would ideally disable periodic sampling in the
interest of saving power. Since the application has direct access to the
kernel config symbols, no trigger is registered when triggering was disabled
by the driver’s configuration.

```c
  1
  2#define UCEL_PER_CEL 1000000
  3#define UCEL_PER_MCEL 1000
  4#define TEMP_INITIAL_CEL 25
  5#define TEMP_WINDOW_HALF_UCEL 500000
  6
  7static const char *now_str(void)
  8{
  9	static char buf[16]; /* ...HH:MM:SS.MMM */
 10	uint32_t now = k_uptime_get_32();
 11	unsigned int ms = now % MSEC_PER_SEC;
 12	unsigned int s;
 13	unsigned int min;
 14	unsigned int h;
 15
 16	now /= MSEC_PER_SEC;
 17	s = now % 60U;
 18	now /= 60U;
 19	min = now % 60U;
 20	now /= 60U;
 21	h = now;
 22
 23	snprintf(buf, sizeof(buf), "%u:%02u:%02u.%03u",
 24		 h, min, s, ms);
 25	return buf;
 26}
 27
 28#ifdef CONFIG_MCP9808_TRIGGER
 29
 30static struct sensor_trigger sensor_trig;
 31
 32static int set_window(const struct device *dev,
 33		      const struct sensor_value *temp)
 34{
 35	const int temp_ucel = temp->val1 * UCEL_PER_CEL + temp->val2;
 36	const int low_ucel = temp_ucel - TEMP_WINDOW_HALF_UCEL;
 37	const int high_ucel = temp_ucel + TEMP_WINDOW_HALF_UCEL;
 38	struct sensor_value val = {
 39		.val1 = low_ucel / UCEL_PER_CEL,
 40		.val2 = low_ucel % UCEL_PER_CEL,
 41	};
 42	int rc = sensor_attr_set(dev, SENSOR_CHAN_AMBIENT_TEMP,
 43				 SENSOR_ATTR_LOWER_THRESH, &val);
 44	if (rc == 0) {
 45		val.val1 = high_ucel / UCEL_PER_CEL,
 46		val.val2 = high_ucel % UCEL_PER_CEL,
 47		rc = sensor_attr_set(dev, SENSOR_CHAN_AMBIENT_TEMP,
 48				     SENSOR_ATTR_UPPER_THRESH, &val);
 49	}
 50
 51	if (rc == 0) {
 52		printf("Alert on temp outside [%d, %d] milli-Celsius\n",
 53		       low_ucel / UCEL_PER_MCEL,
 54		       high_ucel / UCEL_PER_MCEL);
 55	}
 56
 57	return rc;
 58}
 59
 60static inline int set_window_ucel(const struct device *dev,
 61				  int temp_ucel)
 62{
 63	struct sensor_value val = {
 64		.val1 = temp_ucel / UCEL_PER_CEL,
 65		.val2 = temp_ucel % UCEL_PER_CEL,
 66	};
 67
 68	return set_window(dev, &val);
 69}
 70
 71static void trigger_handler(const struct device *dev,
 72			    const struct sensor_trigger *trig)
 73{
 74	struct sensor_value temp;
 75	static size_t cnt;
 76	int rc;
 77
 78	++cnt;
 79	rc = sensor_sample_fetch(dev);
 80	if (rc != 0) {
 81		printf("sensor_sample_fetch error: %d\n", rc);
 82		return;
 83	}
 84	rc = sensor_channel_get(dev, SENSOR_CHAN_AMBIENT_TEMP, &temp);
 85	if (rc != 0) {
 86		printf("sensor_channel_get error: %d\n", rc);
 87		return;
 88	}
 89
 90	printf("trigger fired %u, temp %g deg C\n", cnt,
 91	       sensor_value_to_double(&temp));
 92	set_window(dev, &temp);
 93}
 94#endif
 95
 96int main(void)
 97{
 98	const struct device *const dev = DEVICE_DT_GET_ANY(microchip_mcp9808);
 99	int rc;
100
101	if (dev == NULL) {
102		printf("Device not found.\n");
103		return 0;
104	}
105	if (!device_is_ready(dev)) {
106		printf("Device %s is not ready.\n", dev->name);
107		return 0;
108	}
109
110#ifdef CONFIG_MCP9808_TRIGGER
111	rc = set_window_ucel(dev, TEMP_INITIAL_CEL * UCEL_PER_CEL);
112	if (rc == 0) {
113		sensor_trig.type = SENSOR_TRIG_THRESHOLD;
114		sensor_trig.chan = SENSOR_CHAN_AMBIENT_TEMP;
115		rc = sensor_trigger_set(dev, &sensor_trig, trigger_handler);
116	}
117
118	if (rc != 0) {
119		printf("Trigger set failed: %d\n", rc);
120		return 0;
121	}
122	printk("Trigger set got %d\n", rc);
123#endif
124
125	while (1) {
126		struct sensor_value temp;
127
128		rc = sensor_sample_fetch(dev);
129		if (rc != 0) {
130			printf("sensor_sample_fetch error: %d\n", rc);
131			break;
132		}
133
134		rc = sensor_channel_get(dev, SENSOR_CHAN_AMBIENT_TEMP, &temp);
135		if (rc != 0) {
136			printf("sensor_channel_get error: %d\n", rc);
137			break;
138		}
139
140		printf("%s: %g C\n", now_str(),
141		       sensor_value_to_double(&temp));
142
143		k_sleep(K_SECONDS(2));
144	}
145	return 0;
146}
```

## API Reference

Related code samples

[LVGL line chart with accelerometer data](../../samples/modules/lvgl/accelerometer_chart/README.md#lvgl-accelerometer-chart "Display acceleration data on a real-time chart using LVGL.")
:   Display acceleration data on a real-time chart using LVGL.

[X-NUCLEO-53L0A1 shield](../../samples/shields/x_nucleo_53l0a1/README.md#x-nucleo-53l0a1 "Interact with the 7-segment display and VL53L0X ranging sensor of an X-NUCLEO-53L0A1 shield.")
:   Interact with the 7-segment display and VL53L0X ranging sensor of an X-NUCLEO-53L0A1 shield.

[X-NUCLEO-IKS01A1 shield](../../samples/shields/x_nucleo_iks01a1/README.md#x-nucleo-iks01a1 "Interact with all the sensors of an X-NUCLEO-IKS01A1 shield.")
:   Interact with all the sensors of an X-NUCLEO-IKS01A1 shield.

[X-NUCLEO-IKS01A2 shield - SensorHub (Mode 2)](../../samples/shields/x_nucleo_iks01a2/sensorhub/README.md#x-nucleo-iks01a2-shub "Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Sensor Hub mode.")
:   Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Sensor Hub mode.

[X-NUCLEO-IKS01A2 shield - Standard (Mode 1)](../../samples/shields/x_nucleo_iks01a2/standard/README.md#x-nucleo-iks01a2-std "Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Standard Mode.")
:   Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Standard Mode.

[X-NUCLEO-IKS01A3 shield - SensorHub (Mode 2)](../../samples/shields/x_nucleo_iks01a3/sensorhub/README.md#x-nucleo-iks01a3-shub "Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Sensor Hub mode.")
:   Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Sensor Hub mode.

[X-NUCLEO-IKS01A3 shield - Standard (Mode 1)](../../samples/shields/x_nucleo_iks01a3/standard/README.md#x-nucleo-iks01a3-std "Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Standard mode.")
:   Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Standard mode.

[X-NUCLEO-IKS02A1 shield - SensorHub (Mode 2)](../../samples/shields/x_nucleo_iks02a1/sensorhub/README.md#x-nucleo-iks02a1-shub "Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Sensor Hub mode.")
:   Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Sensor Hub mode.

[X-NUCLEO-IKS02A1 shield - Standard (Mode 1)](../../samples/shields/x_nucleo_iks02a1/standard/README.md#x-nucleo-iks02a1-std "Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Standard mode.")
:   Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Standard mode.

*group* sensor\_interface
:   Sensor Interface.

    Defines

    SENSOR\_DECODE\_CONTEXT\_INIT(decoder\_, buffer\_, channel\_, channel\_index\_)
    :   Initialize a [sensor\_decode\_context](#structsensor__decode__context).

    SENSOR\_STREAM\_TRIGGER\_PREP(\_trigger, \_opt)

    SENSOR\_DT\_READ\_IODEV(name, dt\_node, ...)
    :   Define a reading instance of a sensor.

        Use this macro to generate a [rtio\_iodev](../../services/rtio/index.md#structrtio__iodev) for reading specific channels. Example:

        ```text
         (.c)
        SENSOR_DT_READ_IODEV(icm42688_accelgyro, DT_NODELABEL(icm42688),
            SENSOR_CHAN_ACCEL_XYZ, SENSOR_CHAN_GYRO_XYZ);

        int main(void) {
          sensor_read(&icm42688_accelgyro, &rtio);
        }
        ```

    SENSOR\_DT\_STREAM\_IODEV(name, dt\_node, ...)
    :   Define a stream instance of a sensor.

        Use this macro to generate a [rtio\_iodev](../../services/rtio/index.md#structrtio__iodev) for starting a stream that’s triggered by specific interrupts. Example:

        ```text
         (.c)
        SENSOR_DT_STREAM_IODEV(imu_stream, DT_ALIAS(imu),
            {SENSOR_TRIG_FIFO_WATERMARK, SENSOR_STREAM_DATA_INCLUDE},
            {SENSOR_TRIG_FIFO_FULL, SENSOR_STREAM_DATA_NOP});

        int main(void) {
          struct rtio_sqe *handle;
          sensor_stream(&imu_stream, &rtio, NULL, &handle);
          k_msleep(1000);
          rtio_sqe_cancel(handle);
        }
        ```

    SENSOR\_CHANNEL\_3\_AXIS(chan)
    :   checks if a given channel is a 3-axis channel

        Parameters:
        :   - **chan** – **[in]** The channel to check

        Return values:
        :   - **true** – if `chan` is any of [SENSOR\_CHAN\_ACCEL\_XYZ](#group__sensor__interface_1ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9), [SENSOR\_CHAN\_GYRO\_XYZ](#group__sensor__interface_1ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e), or [SENSOR\_CHAN\_MAGN\_XYZ](#group__sensor__interface_1ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32)
            - **false** – otherwise

    SENSOR\_G
    :   The value of gravitational constant in micro m/s^2.

    SENSOR\_PI
    :   The value of constant PI in micros.

    SENSOR\_INFO\_DEFINE(name, ...)

    SENSOR\_INFO\_DT\_DEFINE(node\_id)

    SENSOR\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, data\_ptr, cfg\_ptr, level, prio, api\_ptr, ...)
    :   Like [DEVICE\_DT\_DEFINE()](../../kernel/drivers/index.md#group__device__model_1gac49e26fbe91a14307d5ea08d41561dd1) with sensor specifics.

        Defines a device which implements the sensor API. May define an element in the sensor info iterable section used to enumerate all sensor devices.

        Parameters:
        :   - **node\_id** – The devicetree node identifier.
            - **init\_fn** – Name of the init function of the driver.
            - **pm\_device** – PM device resources reference (NULL if device does not use PM).
            - **data\_ptr** – Pointer to the device’s private data.
            - **cfg\_ptr** – The address to the structure containing the configuration information for this instance of the driver.
            - **level** – The initialization level. See SYS\_INIT() for details.
            - **prio** – Priority within the selected initialization level. See SYS\_INIT() for details.
            - **api\_ptr** – Provides an initial pointer to the API function struct used by the driver. Can be NULL.

    SENSOR\_DEVICE\_DT\_INST\_DEFINE(inst, ...)
    :   Like [SENSOR\_DEVICE\_DT\_DEFINE()](#group__sensor__interface_1gaa67ca630e3931a0c3821ba438c86690c) for an instance of a DT\_DRV\_COMPAT compatible.

        Parameters:
        :   - **inst** – instance number. This is replaced by `DT_DRV_COMPAT(inst)` in the call to [SENSOR\_DEVICE\_DT\_DEFINE()](#group__sensor__interface_1gaa67ca630e3931a0c3821ba438c86690c).
            - **...** – other parameters as expected by [SENSOR\_DEVICE\_DT\_DEFINE()](#group__sensor__interface_1gaa67ca630e3931a0c3821ba438c86690c).

    Typedefs

    typedef void (\*sensor\_trigger\_handler\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [sensor\_trigger](#c.sensor_trigger) \*trigger)
    :   Callback API upon firing of a trigger.

        Param dev:
        :   Pointer to the sensor device

        Param trigger:
        :   The trigger

    typedef int (\*sensor\_attr\_set\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan, enum [sensor\_attribute](#c.sensor_attribute) attr, const struct [sensor\_value](#c.sensor_value) \*val)
    :   Callback API upon setting a sensor’s attributes.

        See [sensor\_attr\_set()](#group__sensor__interface_1gafbf65226a227e9f8824908bc38e336f5) for argument description

    typedef int (\*sensor\_attr\_get\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan, enum [sensor\_attribute](#c.sensor_attribute) attr, struct [sensor\_value](#c.sensor_value) \*val)
    :   Callback API upon getting a sensor’s attributes.

        See [sensor\_attr\_get()](#group__sensor__interface_1gaedfdfc71dce702dc1fb1c6e60ff0f73a) for argument description

    typedef int (\*sensor\_trigger\_set\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [sensor\_trigger](#c.sensor_trigger) \*trig, [sensor\_trigger\_handler\_t](#c.sensor_trigger_handler_t) handler)
    :   Callback API for setting a sensor’s trigger and handler.

        See [sensor\_trigger\_set()](#group__sensor__interface_1ga7c72aca732e0641612d2f9437c2e41b7) for argument description

    typedef int (\*sensor\_sample\_fetch\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan)
    :   Callback API for fetching data from a sensor.

        See [sensor\_sample\_fetch()](#group__sensor__interface_1gaa75e25d93ee7cac0bf38399f3c006dff) for argument description

    typedef int (\*sensor\_channel\_get\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan, struct [sensor\_value](#c.sensor_value) \*val)
    :   Callback API for getting a reading from a sensor.

        See [sensor\_channel\_get()](#group__sensor__interface_1ga9e0e6c1408d32c52267984bae7cb268d) for argument description

    typedef int (\*sensor\_get\_decoder\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [sensor\_decoder\_api](#c.sensor_decoder_api) \*\*api)
    :   Get the decoder associate with the given device.

        See also

        [sensor\_get\_decoder](#group__sensor__interface_1ga12db6fc43adce48d34c25c16fd2336a3) for more details

    typedef int (\*sensor\_submit\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*sensor, struct [rtio\_iodev\_sqe](../../services/rtio/index.md#c.rtio_iodev_sqe "rtio_iodev_sqe") \*sqe)

    typedef void (\*sensor\_processing\_callback\_t)(int result, uint8\_t \*buf, uint32\_t buf\_len, void \*userdata)
    :   Callback function used with the helper processing function.

        See also

        [sensor\_processing\_with\_callback](#group__sensor__interface_1gabb076531445e1b128d515b28c7cc9dc8)

        Param result:
        :   **[in]** The result code of the read (0 being success)

        Param buf:
        :   **[in]** The data buffer holding the sensor data

        Param buf\_len:
        :   **[in]** The length (in bytes) of the `buf`

        Param userdata:
        :   **[in]** The optional userdata passed to [sensor\_read()](#group__sensor__interface_1ga385feca2a8b65cb6a24443a5d903ca8b)

    Enums

    enum sensor\_channel
    :   Sensor channels.

        *Values:*

        enumerator SENSOR\_CHAN\_ACCEL\_X
        :   Acceleration on the X axis, in m/s^2.

        enumerator SENSOR\_CHAN\_ACCEL\_Y
        :   Acceleration on the Y axis, in m/s^2.

        enumerator SENSOR\_CHAN\_ACCEL\_Z
        :   Acceleration on the Z axis, in m/s^2.

        enumerator SENSOR\_CHAN\_ACCEL\_XYZ
        :   Acceleration on the X, Y and Z axes.

        enumerator SENSOR\_CHAN\_GYRO\_X
        :   Angular velocity around the X axis, in radians/s.

        enumerator SENSOR\_CHAN\_GYRO\_Y
        :   Angular velocity around the Y axis, in radians/s.

        enumerator SENSOR\_CHAN\_GYRO\_Z
        :   Angular velocity around the Z axis, in radians/s.

        enumerator SENSOR\_CHAN\_GYRO\_XYZ
        :   Angular velocity around the X, Y and Z axes.

        enumerator SENSOR\_CHAN\_MAGN\_X
        :   Magnetic field on the X axis, in Gauss.

        enumerator SENSOR\_CHAN\_MAGN\_Y
        :   Magnetic field on the Y axis, in Gauss.

        enumerator SENSOR\_CHAN\_MAGN\_Z
        :   Magnetic field on the Z axis, in Gauss.

        enumerator SENSOR\_CHAN\_MAGN\_XYZ
        :   Magnetic field on the X, Y and Z axes.

        enumerator SENSOR\_CHAN\_DIE\_TEMP
        :   Device die temperature in degrees Celsius.

        enumerator SENSOR\_CHAN\_AMBIENT\_TEMP
        :   Ambient temperature in degrees Celsius.

        enumerator SENSOR\_CHAN\_PRESS
        :   Pressure in kilopascal.

        enumerator SENSOR\_CHAN\_PROX
        :   Proximity.

            Adimensional. A value of 1 indicates that an object is close.

        enumerator SENSOR\_CHAN\_HUMIDITY
        :   Humidity, in percent.

        enumerator SENSOR\_CHAN\_LIGHT
        :   Illuminance in visible spectrum, in lux.

        enumerator SENSOR\_CHAN\_IR
        :   Illuminance in infra-red spectrum, in lux.

        enumerator SENSOR\_CHAN\_RED
        :   Illuminance in red spectrum, in lux.

        enumerator SENSOR\_CHAN\_GREEN
        :   Illuminance in green spectrum, in lux.

        enumerator SENSOR\_CHAN\_BLUE
        :   Illuminance in blue spectrum, in lux.

        enumerator SENSOR\_CHAN\_ALTITUDE
        :   Altitude, in meters.

        enumerator SENSOR\_CHAN\_PM\_1\_0
        :   1.0 micro-meters Particulate Matter, in ug/m^3

        enumerator SENSOR\_CHAN\_PM\_2\_5
        :   2.5 micro-meters Particulate Matter, in ug/m^3

        enumerator SENSOR\_CHAN\_PM\_10
        :   10 micro-meters Particulate Matter, in ug/m^3

        enumerator SENSOR\_CHAN\_DISTANCE
        :   Distance.

            From sensor to target, in meters

        enumerator SENSOR\_CHAN\_CO2
        :   CO2 level, in parts per million (ppm).

        enumerator SENSOR\_CHAN\_VOC
        :   VOC level, in parts per billion (ppb).

        enumerator SENSOR\_CHAN\_GAS\_RES
        :   Gas sensor resistance in ohms.

        enumerator SENSOR\_CHAN\_VOLTAGE
        :   Voltage, in volts.

        enumerator SENSOR\_CHAN\_VSHUNT
        :   Current Shunt Voltage in milli-volts.

        enumerator SENSOR\_CHAN\_CURRENT
        :   Current, in amps.

        enumerator SENSOR\_CHAN\_POWER
        :   Power in watts.

        enumerator SENSOR\_CHAN\_RESISTANCE
        :   Resistance , in Ohm.

        enumerator SENSOR\_CHAN\_ROTATION
        :   Angular rotation, in degrees.

        enumerator SENSOR\_CHAN\_POS\_DX
        :   Position change on the X axis, in points.

        enumerator SENSOR\_CHAN\_POS\_DY
        :   Position change on the Y axis, in points.

        enumerator SENSOR\_CHAN\_POS\_DZ
        :   Position change on the Z axis, in points.

        enumerator SENSOR\_CHAN\_RPM
        :   Revolutions per minute, in RPM.

        enumerator SENSOR\_CHAN\_GAUGE\_VOLTAGE
        :   Voltage, in volts.

        enumerator SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT
        :   Average current, in amps.

        enumerator SENSOR\_CHAN\_GAUGE\_STDBY\_CURRENT
        :   Standby current, in amps.

        enumerator SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT
        :   Max load current, in amps.

        enumerator SENSOR\_CHAN\_GAUGE\_TEMP
        :   Gauge temperature.

        enumerator SENSOR\_CHAN\_GAUGE\_STATE\_OF\_CHARGE
        :   State of charge measurement in %.

        enumerator SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY
        :   Full Charge Capacity in mAh.

        enumerator SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY
        :   Remaining Charge Capacity in mAh.

        enumerator SENSOR\_CHAN\_GAUGE\_NOM\_AVAIL\_CAPACITY
        :   Nominal Available Capacity in mAh.

        enumerator SENSOR\_CHAN\_GAUGE\_FULL\_AVAIL\_CAPACITY
        :   Full Available Capacity in mAh.

        enumerator SENSOR\_CHAN\_GAUGE\_AVG\_POWER
        :   Average power in mW.

        enumerator SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH
        :   State of health measurement in %.

        enumerator SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY
        :   Time to empty in minutes.

        enumerator SENSOR\_CHAN\_GAUGE\_TIME\_TO\_FULL
        :   Time to full in minutes.

        enumerator SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT
        :   Cycle count (total number of charge/discharge cycles).

        enumerator SENSOR\_CHAN\_GAUGE\_DESIGN\_VOLTAGE
        :   Design voltage of cell in V (max voltage).

        enumerator SENSOR\_CHAN\_GAUGE\_DESIRED\_VOLTAGE
        :   Desired voltage of cell in V (nominal voltage).

        enumerator SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT
        :   Desired charging current in mA.

        enumerator SENSOR\_CHAN\_ALL
        :   All channels.

        enumerator SENSOR\_CHAN\_COMMON\_COUNT
        :   Number of all common sensor channels.

        enumerator SENSOR\_CHAN\_PRIV\_START = [SENSOR\_CHAN\_COMMON\_COUNT](#c.sensor_channel.SENSOR_CHAN_COMMON_COUNT)
        :   This and higher values are sensor specific.

            Refer to the sensor header file.

        enumerator SENSOR\_CHAN\_MAX = INT16\_MAX
        :   Maximum value describing a sensor channel type.

    enum sensor\_trigger\_type
    :   Sensor trigger types.

        *Values:*

        enumerator SENSOR\_TRIG\_TIMER
        :   Timer-based trigger, useful when the sensor does not have an interrupt line.

        enumerator SENSOR\_TRIG\_DATA\_READY
        :   Trigger fires whenever new data is ready.

        enumerator SENSOR\_TRIG\_DELTA
        :   Trigger fires when the selected channel varies significantly.

            This includes any-motion detection when the channel is acceleration or gyro. If detection is based on slope between successive channel readings, the slope threshold is configured via the [SENSOR\_ATTR\_SLOPE\_TH](#group__sensor__interface_1gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302) and [SENSOR\_ATTR\_SLOPE\_DUR](#group__sensor__interface_1gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1) attributes.

        enumerator SENSOR\_TRIG\_NEAR\_FAR
        :   Trigger fires when a near/far event is detected.

        enumerator SENSOR\_TRIG\_THRESHOLD
        :   Trigger fires when channel reading transitions configured thresholds.

            The thresholds are configured via the [SENSOR\_ATTR\_LOWER\_THRESH](#group__sensor__interface_1gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa), [SENSOR\_ATTR\_UPPER\_THRESH](#group__sensor__interface_1gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b), and [SENSOR\_ATTR\_HYSTERESIS](#group__sensor__interface_1gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94) attributes.

        enumerator SENSOR\_TRIG\_TAP
        :   Trigger fires when a single tap is detected.

        enumerator SENSOR\_TRIG\_DOUBLE\_TAP
        :   Trigger fires when a double tap is detected.

        enumerator SENSOR\_TRIG\_FREEFALL
        :   Trigger fires when a free fall is detected.

        enumerator SENSOR\_TRIG\_MOTION
        :   Trigger fires when motion is detected.

        enumerator SENSOR\_TRIG\_STATIONARY
        :   Trigger fires when no motion has been detected for a while.

        enumerator SENSOR\_TRIG\_FIFO\_WATERMARK
        :   Trigger fires when the FIFO watermark has been reached.

        enumerator SENSOR\_TRIG\_FIFO\_FULL
        :   Trigger fires when the FIFO becomes full.

        enumerator SENSOR\_TRIG\_COMMON\_COUNT
        :   Number of all common sensor triggers.

        enumerator SENSOR\_TRIG\_PRIV\_START = [SENSOR\_TRIG\_COMMON\_COUNT](#c.sensor_trigger_type.SENSOR_TRIG_COMMON_COUNT)
        :   This and higher values are sensor specific.

            Refer to the sensor header file.

        enumerator SENSOR\_TRIG\_MAX = INT16\_MAX
        :   Maximum value describing a sensor trigger type.

    enum sensor\_attribute
    :   Sensor attribute types.

        *Values:*

        enumerator SENSOR\_ATTR\_SAMPLING\_FREQUENCY
        :   Sensor sampling frequency, i.e.

            how many times a second the sensor takes a measurement.

        enumerator SENSOR\_ATTR\_LOWER\_THRESH
        :   Lower threshold for trigger.

        enumerator SENSOR\_ATTR\_UPPER\_THRESH
        :   Upper threshold for trigger.

        enumerator SENSOR\_ATTR\_SLOPE\_TH
        :   Threshold for any-motion (slope) trigger.

        enumerator SENSOR\_ATTR\_SLOPE\_DUR
        :   Duration for which the slope values needs to be outside the threshold for the trigger to fire.

        enumerator SENSOR\_ATTR\_HYSTERESIS

        enumerator SENSOR\_ATTR\_OVERSAMPLING
        :   Oversampling factor.

        enumerator SENSOR\_ATTR\_FULL\_SCALE
        :   Sensor range, in SI units.

        enumerator SENSOR\_ATTR\_OFFSET
        :   The sensor value returned will be altered by the amount indicated by offset: final\_value = [sensor\_value](#structsensor__value) + offset.

        enumerator SENSOR\_ATTR\_CALIB\_TARGET
        :   Calibration target.

            This will be used by the internal chip’s algorithms to calibrate itself on a certain axis, or all of them.

        enumerator SENSOR\_ATTR\_CONFIGURATION
        :   Configure the operating modes of a sensor.

        enumerator SENSOR\_ATTR\_CALIBRATION
        :   Set a calibration value needed by a sensor.

        enumerator SENSOR\_ATTR\_FEATURE\_MASK
        :   Enable/disable sensor features.

        enumerator SENSOR\_ATTR\_ALERT
        :   Alert threshold or alert enable/disable.

        enumerator SENSOR\_ATTR\_FF\_DUR
        :   Free-fall duration represented in milliseconds.

            If the sampling frequency is changed during runtime, this attribute should be set to adjust freefall duration to the new sampling frequency.

        enumerator SENSOR\_ATTR\_BATCH\_DURATION
        :   Hardware batch duration in ticks.

        enumerator SENSOR\_ATTR\_COMMON\_COUNT
        :   Number of all common sensor attributes.

        enumerator SENSOR\_ATTR\_PRIV\_START = [SENSOR\_ATTR\_COMMON\_COUNT](#c.sensor_attribute.SENSOR_ATTR_COMMON_COUNT)
        :   This and higher values are sensor specific.

            Refer to the sensor header file.

        enumerator SENSOR\_ATTR\_MAX = INT16\_MAX
        :   Maximum value describing a sensor attribute type.

    enum sensor\_stream\_data\_opt
    :   Options for what to do with the associated data when a trigger is consumed.

        *Values:*

        enumerator SENSOR\_STREAM\_DATA\_INCLUDE = 0
        :   Include whatever data is associated with the trigger.

        enumerator SENSOR\_STREAM\_DATA\_NOP = 1
        :   Do nothing with the associated trigger data, it may be consumed later.

        enumerator SENSOR\_STREAM\_DATA\_DROP = 2
        :   Flush/clear whatever data is associated with the trigger.

    Functions

    static inline int sensor\_decode(struct [sensor\_decode\_context](#c.sensor_decode_context) \*ctx, void \*out, uint16\_t max\_count)
    :   Decode N frames using a [sensor\_decode\_context](#structsensor__decode__context).

        Parameters:
        :   - **ctx** – **[inout]** The context to use for decoding
            - **out** – **[out]** The output buffer
            - **max\_count** – **[in]** Maximum number of frames to decode

        Returns:
        :   The decode result from [sensor\_decoder\_api](#structsensor__decoder__api)’s decode function

    int sensor\_natively\_supported\_channel\_size\_info(enum [sensor\_channel](#c.sensor_channel) channel, size\_t \*base\_size, size\_t \*frame\_size)

    int sensor\_attr\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan, enum [sensor\_attribute](#c.sensor_attribute) attr, const struct [sensor\_value](#c.sensor_value) \*val)
    :   Set an attribute for a sensor.

        Parameters:
        :   - **dev** – Pointer to the sensor device
            - **chan** – The channel the attribute belongs to, if any. Some attributes may only be set for all channels of a device, depending on device capabilities.
            - **attr** – The attribute to set
            - **val** – The value to set the attribute to

        Returns:
        :   0 if successful, negative errno code if failure.

    int sensor\_attr\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan, enum [sensor\_attribute](#c.sensor_attribute) attr, struct [sensor\_value](#c.sensor_value) \*val)
    :   Get an attribute for a sensor.

        Parameters:
        :   - **dev** – Pointer to the sensor device
            - **chan** – The channel the attribute belongs to, if any. Some attributes may only be set for all channels of a device, depending on device capabilities.
            - **attr** – The attribute to get
            - **val** – Pointer to where to store the attribute

        Returns:
        :   0 if successful, negative errno code if failure.

    static inline int sensor\_trigger\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [sensor\_trigger](#c.sensor_trigger) \*trig, [sensor\_trigger\_handler\_t](#c.sensor_trigger_handler_t) handler)
    :   Activate a sensor’s trigger and set the trigger handler.

        The handler will be called from a thread, so I2C or SPI operations are safe. However, the thread’s stack is limited and defined by the driver. It is currently up to the caller to ensure that the handler does not overflow the stack.

        The user-allocated trigger will be stored by the driver as a pointer, rather than a copy, and passed back to the handler. This enables the handler to use CONTAINER\_OF to retrieve a context pointer when the trigger is embedded in a larger struct and requires that the trigger is not allocated on the stack.

        **Function properties (list may not be complete)**
        :   [supervisor](../../develop/api/terminology.md#api-term-supervisor)

        Parameters:
        :   - **dev** – Pointer to the sensor device
            - **trig** – The trigger to activate
            - **handler** – The function that should be called when the trigger fires

        Returns:
        :   0 if successful, negative errno code if failure.

    int sensor\_sample\_fetch(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Fetch a sample from the sensor and store it in an internal driver buffer.

        Read all of a sensor’s active channels and, if necessary, perform any additional operations necessary to make the values useful. The user may then get individual channel values by calling [sensor\_channel\_get](#group__sensor__interface_1ga9e0e6c1408d32c52267984bae7cb268d).

        The function blocks until the fetch operation is complete.

        Since the function communicates with the sensor device, it is unsafe to call it in an ISR if the device is connected via I2C or SPI.

        Parameters:
        :   - **dev** – Pointer to the sensor device

        Returns:
        :   0 if successful, negative errno code if failure.

    int sensor\_sample\_fetch\_chan(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) type)
    :   Fetch a sample from the sensor and store it in an internal driver buffer.

        Read and compute compensation for one type of sensor data (magnetometer, accelerometer, etc). The user may then get individual channel values by calling [sensor\_channel\_get](#group__sensor__interface_1ga9e0e6c1408d32c52267984bae7cb268d).

        This is mostly implemented by multi function devices enabling reading at different sampling rates.

        The function blocks until the fetch operation is complete.

        Since the function communicates with the sensor device, it is unsafe to call it in an ISR if the device is connected via I2C or SPI.

        Parameters:
        :   - **dev** – Pointer to the sensor device
            - **type** – The channel that needs updated

        Returns:
        :   0 if successful, negative errno code if failure.

    int sensor\_channel\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan, struct [sensor\_value](#c.sensor_value) \*val)
    :   Get a reading from a sensor device.

        Return a useful value for a particular channel, from the driver’s internal data. Before calling this function, a sample must be obtained by calling [sensor\_sample\_fetch](#group__sensor__interface_1gaa75e25d93ee7cac0bf38399f3c006dff) or [sensor\_sample\_fetch\_chan](#group__sensor__interface_1gac16192826432438a15274cf28d66e8a6). It is guaranteed that two subsequent calls of this function for the same channels will yield the same value, if [sensor\_sample\_fetch](#group__sensor__interface_1gaa75e25d93ee7cac0bf38399f3c006dff) or [sensor\_sample\_fetch\_chan](#group__sensor__interface_1gac16192826432438a15274cf28d66e8a6) has not been called in the meantime.

        For vectorial data samples you can request all axes in just one call by passing the specific channel with \_XYZ suffix. The sample will be returned at val[0], val[1] and val[2] (X, Y and Z in that order).

        Parameters:
        :   - **dev** – Pointer to the sensor device
            - **chan** – The channel to read
            - **val** – Where to store the value

        Returns:
        :   0 if successful, negative errno code if failure.

    int sensor\_get\_decoder(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [sensor\_decoder\_api](#c.sensor_decoder_api) \*\*decoder)
    :   Get the sensor’s decoder API.

        Parameters:
        :   - **dev** – **[in]** The sensor device
            - **decoder** – **[in]** Pointer to the decoder which will be set upon success

        Returns:
        :   0 on success

        Returns:
        :   < 0 on error

    int sensor\_reconfigure\_read\_iodev(struct [rtio\_iodev](../../services/rtio/index.md#c.rtio_iodev "rtio_iodev") \*iodev, const struct [device](../../kernel/drivers/index.md#c.device "device") \*sensor, const enum [sensor\_channel](#c.sensor_channel) \*channels, size\_t num\_channels)
    :   Reconfigure a reading iodev.

        Allows a reconfiguration of the iodev associated with reading a sample from a sensor.

        **Important**: If the iodev is currently servicing a read operation, the data will likely be invalid. Please be sure the flush or wait for all pending operations to complete before using the data after a configuration change.

        It is also important that the `data` field of the iodev is a [sensor\_read\_config](#structsensor__read__config).

        Parameters:
        :   - **iodev** – **[in]** The iodev to reconfigure
            - **sensor** – **[in]** The sensor to read from
            - **channels** – **[in]** One or more channels to read
            - **num\_channels** – **[in]** The number of channels in `channels`

        Returns:
        :   0 on success

        Returns:
        :   < 0 on error

    static inline int sensor\_stream(struct [rtio\_iodev](../../services/rtio/index.md#c.rtio_iodev "rtio_iodev") \*iodev, struct [rtio](../../services/rtio/index.md#c.rtio "rtio") \*ctx, void \*userdata, struct [rtio\_sqe](../../services/rtio/index.md#c.rtio_sqe "rtio_sqe") \*\*handle)

    static inline int sensor\_read(struct [rtio\_iodev](../../services/rtio/index.md#c.rtio_iodev "rtio_iodev") \*iodev, struct [rtio](../../services/rtio/index.md#c.rtio "rtio") \*ctx, void \*userdata)
    :   Read data from a sensor.

        Using `cfg`, read one snapshot of data from the device by using the provided RTIO context `ctx`. This call will generate a [rtio\_sqe](../../services/rtio/index.md#structrtio__sqe) that will leverage the RTIO’s internal mempool when the time comes to service the read.

        Parameters:
        :   - **iodev** – **[in]** The iodev created by [SENSOR\_DT\_READ\_IODEV](#group__sensor__interface_1ga0cc1ee28114557e9e00257071c7dfa9f)
            - **ctx** – **[in]** The RTIO context to service the read
            - **userdata** – **[in]** Optional userdata that will be available when the read is complete

        Returns:
        :   0 on success

        Returns:
        :   < 0 on error

    void sensor\_processing\_with\_callback(struct [rtio](../../services/rtio/index.md#c.rtio "rtio") \*ctx, [sensor\_processing\_callback\_t](#c.sensor_processing_callback_t) cb)
    :   Helper function for common processing of sensor data.

        This function can be called in a blocking manner after [sensor\_read()](#group__sensor__interface_1ga385feca2a8b65cb6a24443a5d903ca8b) or in a standalone thread dedicated to processing. It will wait for a cqe from the RTIO context, once received, it will decode the userdata and call the `cb`. Once the `cb` returns, the buffer will be released back into `ctx's` mempool if available.

        Parameters:
        :   - **ctx** – **[in]** The RTIO context to wait on
            - **cb** – **[in]** Callback to call when data is ready for processing

    static inline int32\_t sensor\_ms2\_to\_g(const struct [sensor\_value](#c.sensor_value) \*ms2)
    :   Helper function to convert acceleration from m/s^2 to Gs.

        Parameters:
        :   - **ms2** – A pointer to a [sensor\_value](#structsensor__value) struct holding the acceleration, in m/s^2.

        Returns:
        :   The converted value, in Gs.

    static inline void sensor\_g\_to\_ms2(int32\_t g, struct [sensor\_value](#c.sensor_value) \*ms2)
    :   Helper function to convert acceleration from Gs to m/s^2.

        Parameters:
        :   - **g** – The G value to be converted.
            - **ms2** – A pointer to a [sensor\_value](#structsensor__value) struct, where the result is stored.

    static inline int32\_t sensor\_ms2\_to\_ug(const struct [sensor\_value](#c.sensor_value) \*ms2)
    :   Helper function to convert acceleration from m/s^2 to micro Gs.

        Parameters:
        :   - **ms2** – A pointer to a [sensor\_value](#structsensor__value) struct holding the acceleration, in m/s^2.

        Returns:
        :   The converted value, in micro Gs.

    static inline void sensor\_ug\_to\_ms2(int32\_t ug, struct [sensor\_value](#c.sensor_value) \*ms2)
    :   Helper function to convert acceleration from micro Gs to m/s^2.

        Parameters:
        :   - **ug** – The micro G value to be converted.
            - **ms2** – A pointer to a [sensor\_value](#structsensor__value) struct, where the result is stored.

    static inline int32\_t sensor\_rad\_to\_degrees(const struct [sensor\_value](#c.sensor_value) \*rad)
    :   Helper function for converting radians to degrees.

        Parameters:
        :   - **rad** – A pointer to a [sensor\_value](#structsensor__value) struct, holding the value in radians.

        Returns:
        :   The converted value, in degrees.

    static inline void sensor\_degrees\_to\_rad(int32\_t d, struct [sensor\_value](#c.sensor_value) \*rad)
    :   Helper function for converting degrees to radians.

        Parameters:
        :   - **d** – The value (in degrees) to be converted.
            - **rad** – A pointer to a [sensor\_value](#structsensor__value) struct, where the result is stored.

    static inline int32\_t sensor\_rad\_to\_10udegrees(const struct [sensor\_value](#c.sensor_value) \*rad)
    :   Helper function for converting radians to 10 micro degrees.

        When the unit is 1 micro degree, the range that the int32\_t can represent is +/-2147.483 degrees. In order to increase this range, here we use 10 micro degrees as the unit.

        Parameters:
        :   - **rad** – A pointer to a [sensor\_value](#structsensor__value) struct, holding the value in radians.

        Returns:
        :   The converted value, in 10 micro degrees.

    static inline void sensor\_10udegrees\_to\_rad(int32\_t d, struct [sensor\_value](#c.sensor_value) \*rad)
    :   Helper function for converting 10 micro degrees to radians.

        Parameters:
        :   - **d** – The value (in 10 micro degrees) to be converted.
            - **rad** – A pointer to a [sensor\_value](#structsensor__value) struct, where the result is stored.

    static inline double sensor\_value\_to\_double(const struct [sensor\_value](#c.sensor_value) \*val)
    :   Helper function for converting struct [sensor\_value](#structsensor__value) to double.

        Parameters:
        :   - **val** – A pointer to a [sensor\_value](#structsensor__value) struct.

        Returns:
        :   The converted value.

    static inline float sensor\_value\_to\_float(const struct [sensor\_value](#c.sensor_value) \*val)
    :   Helper function for converting struct [sensor\_value](#structsensor__value) to float.

        Parameters:
        :   - **val** – A pointer to a [sensor\_value](#structsensor__value) struct.

        Returns:
        :   The converted value.

    static inline int sensor\_value\_from\_double(struct [sensor\_value](#c.sensor_value) \*val, double inp)
    :   Helper function for converting double to struct [sensor\_value](#structsensor__value).

        Parameters:
        :   - **val** – A pointer to a [sensor\_value](#structsensor__value) struct.
            - **inp** – The converted value.

        Returns:
        :   0 if successful, negative errno code if failure.

    static inline int sensor\_value\_from\_float(struct [sensor\_value](#c.sensor_value) \*val, float inp)
    :   Helper function for converting float to struct [sensor\_value](#structsensor__value).

        Parameters:
        :   - **val** – A pointer to a [sensor\_value](#structsensor__value) struct.
            - **inp** – The converted value.

        Returns:
        :   0 if successful, negative errno code if failure.

    static inline int64\_t sensor\_value\_to\_milli(const struct [sensor\_value](#c.sensor_value) \*val)
    :   Helper function for converting struct [sensor\_value](#structsensor__value) to integer milli units.

        Parameters:
        :   - **val** – A pointer to a [sensor\_value](#structsensor__value) struct.

        Returns:
        :   The converted value.

    static inline int64\_t sensor\_value\_to\_micro(const struct [sensor\_value](#c.sensor_value) \*val)
    :   Helper function for converting struct [sensor\_value](#structsensor__value) to integer micro units.

        Parameters:
        :   - **val** – A pointer to a [sensor\_value](#structsensor__value) struct.

        Returns:
        :   The converted value.

    static inline int sensor\_value\_from\_milli(struct [sensor\_value](#c.sensor_value) \*val, int64\_t milli)
    :   Helper function for converting integer milli units to struct [sensor\_value](#structsensor__value).

        Parameters:
        :   - **val** – A pointer to a [sensor\_value](#structsensor__value) struct.
            - **milli** – The converted value.

        Returns:
        :   0 if successful, negative errno code if failure.

    static inline int sensor\_value\_from\_micro(struct [sensor\_value](#c.sensor_value) \*val, int64\_t micro)
    :   Helper function for converting integer micro units to struct [sensor\_value](#structsensor__value).

        Parameters:
        :   - **val** – A pointer to a [sensor\_value](#structsensor__value) struct.
            - **micro** – The converted value.

        Returns:
        :   0 if successful, negative errno code if failure.

    struct sensor\_value
    :   *#include <sensor.h>*

        Representation of a sensor readout value.

        The value is represented as having an integer and a fractional part, and can be obtained using the formula val1 + val2 \* 10^(-6). Negative values also adhere to the above formula, but may need special attention. Here are some examples of the value representation:

        ```text
         0.5: val1 =  0, val2 =  500000
        -0.5: val1 =  0, val2 = -500000
        -1.0: val1 = -1, val2 =  0
        -1.5: val1 = -1, val2 = -500000
        ```

        Public Members

        int32\_t val1
        :   Integer part of the value.

        int32\_t val2
        :   Fractional part of the value (in one-millionth parts).

    struct sensor\_trigger
    :   *#include <sensor.h>*

        Sensor trigger spec.

        Public Members

        enum [sensor\_trigger\_type](#c.sensor_trigger_type) type
        :   Trigger type.

        enum [sensor\_channel](#c.sensor_channel) chan
        :   Channel the trigger is set on.

    struct sensor\_decoder\_api
    :   *#include <sensor.h>*

        Decodes a single raw data buffer.

        Data buffers are provided on the [RTIO](../../services/rtio/index.md#group__rtio) context that’s supplied to [sensor\_read](#group__sensor__interface_1ga385feca2a8b65cb6a24443a5d903ca8b).

        Public Members

        int (\*get\_frame\_count)(const uint8\_t \*buffer, enum [sensor\_channel](#c.sensor_channel) channel, size\_t channel\_idx, uint16\_t \*frame\_count)
        :   Get the number of frames in the current buffer.

            Param buffer:
            :   **[in]** The buffer provided on the [RTIO](../../services/rtio/index.md#group__rtio) context.

            Param channel:
            :   **[in]** The channel to get the count for

            Param channel\_idx:
            :   **[in]** The index of the channel

            Param frame\_count:
            :   **[out]** The number of frames on the buffer (at least 1)

            Return:
            :   0 on success

            Return:
            :   -ENOTSUP if the channel/channel\_idx aren’t found

        int (\*get\_size\_info)(enum [sensor\_channel](#c.sensor_channel) channel, size\_t \*base\_size, size\_t \*frame\_size)
        :   Get the size required to decode a given channel.

            When decoding a single frame, use `base_size`. For every additional frame, add another `frame_size`. As an example, to decode 3 frames use: ‘base\_size + 2 \* frame\_size’.

            Param channel:
            :   **[in]** The channel to query

            Param base\_size:
            :   **[out]** The size of decoding the first frame

            Param frame\_size:
            :   **[out]** The additional size of every additional frame

            Return:
            :   0 on success

            Return:
            :   -ENOTSUP if the channel is not supported

        int (\*decode)(const uint8\_t \*buffer, enum [sensor\_channel](#c.sensor_channel) channel, size\_t channel\_idx, uint32\_t \*fit, uint16\_t max\_count, void \*data\_out)
        :   Decode up to `max_count` samples from the buffer.

            Decode samples of channel [sensor\_channel](#group__sensor__interface_1gaaa1b502bc029b10d7b23b0a25ef4e934) across multiple frames. If there exist multiple instances of the same channel, `channel_index` is used to differentiate them. As an example, assume a sensor provides 2 distance measurements:

            ```c
            // Decode the first channel instance of 'distance'
            decoder->decode(buffer, SENSOR_CHAN_DISTANCE, 0, &fit, 5, out);
            ...

            // Decode the second channel instance of 'distance'
            decoder->decode(buffer, SENSOR_CHAN_DISTANCE, 1, &fit, 5, out);
            ```

            Param buffer:
            :   **[in]** The buffer provided on the [RTIO](../../services/rtio/index.md#group__rtio) context

            Param channel:
            :   **[in]** The channel to decode

            Param channel\_idx:
            :   **[in]** The index of the channel

            Param fit:
            :   **[inout]** The current frame iterator

            Param max\_count:
            :   **[in]** The maximum number of channels to decode.

            Param data\_out:
            :   **[out]** The decoded data

            Return:
            :   0 no more samples to decode

            Return:
            :   >0 the number of decoded frames

            Return:
            :   <0 on error

        bool (\*has\_trigger)(const uint8\_t \*buffer, enum [sensor\_trigger\_type](#c.sensor_trigger_type) trigger)
        :   Check if the given trigger type is present.

            Param buffer:
            :   **[in]** The buffer provided on the [RTIO](../../services/rtio/index.md#group__rtio) context

            Param trigger:
            :   **[in]** The trigger type in question

            Return:
            :   Whether the trigger is present in the buffer

    struct sensor\_decode\_context
    :   *#include <sensor.h>*

        Used for iterating over the data frames via the [sensor\_decoder\_api](#structsensor__decoder__api).

        Example usage:

        ```text
        (.c)
           struct sensor_decode_context ctx = SENSOR_DECODE_CONTEXT_INIT(
               decoder, buffer, SENSOR_CHAN_ACCEL_XYZ, 0);

           while (true) {
             struct sensor_three_axis_data accel_out_data;

             num_decoded_channels = sensor_decode(ctx, &accel_out_data, 1);

             if (num_decoded_channels <= 0) {
               printk("Done decoding buffer\n");
               break;
             }

             printk("Decoded (%" PRId32 ", %" PRId32 ", %" PRId32 ")\n", accel_out_data.readings[0].x,
                 accel_out_data.readings[0].y, accel_out_data.readings[0].z);
           }
        ```

    struct sensor\_stream\_trigger
    :   *#include <sensor.h>*

    struct sensor\_read\_config
    :   *#include <sensor.h>*

    struct sensor\_driver\_api
    :   *#include <sensor.h>*

    struct sensor\_data\_generic\_header
    :   *#include <sensor.h>*

*group* sensor\_emulator\_backend
:   Sensor emulator backend API.

    Functions

    static inline bool emul\_sensor\_backend\_is\_supported(const struct [emul](../emulator/bus_emulators.md#c.emul "emul") \*target)
    :   Check if a given sensor emulator supports the backend API.

        Parameters:
        :   - **target** – Pointer to emulator instance to query

        Returns:
        :   True if supported, false if unsupported or if `target` is NULL.

    static inline int emul\_sensor\_backend\_set\_channel(const struct [emul](../emulator/bus_emulators.md#c.emul "emul") \*target, enum [sensor\_channel](#c.sensor_channel) ch, const [q31\_t](../../services/dsp/index.md#c.q31_t "q31_t") \*value, int8\_t shift)
    :   Set an expected value for a given channel on a given sensor emulator.

        Parameters:
        :   - **target** – Pointer to emulator instance to operate on
            - **ch** – Sensor channel to set expected value for
            - **value** – Expected value in fixed-point format using standard SI unit for sensor type
            - **shift** – Shift value (scaling factor) applied to `value`

        Returns:
        :   0 if successful

        Returns:
        :   -ENOTSUP if no backend API or if channel not supported by emul

        Returns:
        :   -ERANGE if provided value is not in the sensor’s supported range

    static inline int emul\_sensor\_backend\_get\_sample\_range(const struct [emul](../emulator/bus_emulators.md#c.emul "emul") \*target, enum [sensor\_channel](#c.sensor_channel) ch, [q31\_t](../../services/dsp/index.md#c.q31_t "q31_t") \*lower, [q31\_t](../../services/dsp/index.md#c.q31_t "q31_t") \*upper, [q31\_t](../../services/dsp/index.md#c.q31_t "q31_t") \*epsilon, int8\_t \*shift)
    :   Query an emulator for a channel’s supported sample value range and tolerance.

        Parameters:
        :   - **target** – Pointer to emulator instance to operate on
            - **ch** – The channel to request info for. If `ch` is unsupported, return `-[ENOTSUP](../../develop/languages/c/minimal_libc.md#group__system__errno_1ga91457bbf35f0f1085619a99423bb1f33)`
            - **lower** – **[out]** Minimum supported sample value in SI units, fixed-point format
            - **upper** – **[out]** Maximum supported sample value in SI units, fixed-point format
            - **epsilon** – **[out]** Tolerance to use comparing expected and actual values to account for rounding and sensor precision issues. This can usually be set to the minimum sample value step size. Uses SI units and fixed-point format.
            - **shift** – **[out]** The shift value (scaling factor) associated with `lower`, `upper`, and `epsilon`.

        Returns:
        :   0 if successful

        Returns:
        :   -ENOTSUP if no backend API or if channel not supported by emul

    static inline int emul\_sensor\_backend\_set\_attribute(const struct [emul](../emulator/bus_emulators.md#c.emul "emul") \*target, enum [sensor\_channel](#c.sensor_channel) ch, enum [sensor\_attribute](#c.sensor_attribute) attribute, const void \*value)
    :   Set the emulator’s attribute values.

        Parameters:
        :   - **target** – **[in]** Pointer to emulator instance to operate on
            - **ch** – **[in]** The channel to request info for. If `ch` is unsupported, return `-[ENOTSUP](../../develop/languages/c/minimal_libc.md#group__system__errno_1ga91457bbf35f0f1085619a99423bb1f33)`
            - **attribute** – **[in]** The attribute to set
            - **value** – **[in]** the value to use (cast according to the channel/attribute pair)

        Returns:
        :   0 is successful

        Returns:
        :   < 0 on error

    static inline int emul\_sensor\_backend\_get\_attribute\_metadata(const struct [emul](../emulator/bus_emulators.md#c.emul "emul") \*target, enum [sensor\_channel](#c.sensor_channel) ch, enum [sensor\_attribute](#c.sensor_attribute) attribute, [q31\_t](../../services/dsp/index.md#c.q31_t "q31_t") \*min, [q31\_t](../../services/dsp/index.md#c.q31_t "q31_t") \*max, [q31\_t](../../services/dsp/index.md#c.q31_t "q31_t") \*increment, int8\_t \*shift)
    :   Get metadata about an attribute.

        Information provided by this function includes the minimum/maximum values of the attribute as well as the increment (value per LSB) which can be used as an epsilon when comparing results.

        Parameters:
        :   - **target** – **[in]** Pointer to emulator instance to operate on
            - **ch** – **[in]** The channel to request info for. If `ch` is unsupported, return ‘-ENOTSUP’
            - **attribute** – **[in]** The attribute to request info for. If `attribute` is unsupported, return ‘-ENOTSUP’
            - **min** – **[out]** The minimum value the attribute can be set to
            - **max** – **[out]** The maximum value the attribute can be set to
            - **increment** – **[out]** The value that the attribute increses by for every LSB
            - **shift** – **[out]** The shift for `min`, `max`, and `increment`

        Returns:
        :   0 on SUCCESS

        Returns:
        :   < 0 on error
