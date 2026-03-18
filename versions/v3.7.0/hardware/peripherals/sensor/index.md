---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/sensor/index.html
original_path: hardware/peripherals/sensor/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Sensors

The sensor driver API provides functionality to uniformly read, configure,
and setup event handling for devices that take real world measurements in
meaningful units.

Sensors range from very simple temperature-reading devices that must be polled
with a fixed scale to complex devices taking in readings from multitudes of
sensors and themselves producing new inferred sensor data such as step counts,
presence detection, orientation, and more.

Supporting this wide breadth of devices is a demanding task and the sensor API
attempts to provide a uniform interface to them.

## Using Sensors

Using sensors from an application there are some APIs and terms that are helpful
to understand. Sensors in Zephyr are composed of [Sensor Channels](channels.md#sensor-channel),
[Sensor Attributes](attributes.md#sensor-attribute), and [Sensor Triggers](triggers.md#sensor-trigger). Attributes and triggers may
be device or channel specific.

Note

Getting samples from sensors using the sensor API today can be done in one of
two ways. A stable and long-lived API [Fetch and Get](fetch_and_get.md#sensor-fetch-and-get), or a newer
but rapidly stabilizing API [Read and Decode](read_and_decode.md#sensor-read-and-decode). It’s expected that
in the near future [Fetch and Get](fetch_and_get.md#sensor-fetch-and-get) will be deprecated in favor of
[Read and Decode](read_and_decode.md#sensor-read-and-decode). Triggers are handled entirely differently for
[Fetch and Get](fetch_and_get.md#sensor-fetch-and-get) or [Read and Decode](read_and_decode.md#sensor-read-and-decode) and the
differences are noted in each of those sections.

## Implementing Sensor Drivers

Note

Implementing the driver side of the sensor API requires an understanding how
the sensor APIs are used. Please read through [Using Sensors](#sensor-using) first!

### Implementing Attributes

- SHOULD implement attribute setting in a blocking manner.
- SHOULD provide the ability to get and set channel scale if supported by the
  device.
- SHOULD provide the ability to get and set channel sampling rate if supported
  by the device.

### Implementing Fetch and Get

- SHOULD implement [`sensor_sample_fetch_t`](#c.sensor_sample_fetch_t) as a blocking call that
  stashes the specified channels (or all sensor channels) as driver instance
  data.
- SHOULD implement [`sensor_channel_get_t`](#c.sensor_channel_get_t) without side effects
  manipulating driver state returning stashed sensor readings.
- SHOULD implement [`sensor_trigger_set_t`](#c.sensor_trigger_set_t) storing the address of the
  [`sensor_trigger`](#c.sensor_trigger) rather than copying the contents. This is so
  [`CONTAINER_OF`](../../../kernel/util/index.md#c.CONTAINER_OF "CONTAINER_OF") may be used for trigger callback context.

### Implementing Read and Decode

- MUST implement [`sensor_submit_t`](#c.sensor_submit_t) as a non-blocking call.
- SHOULD implement [`sensor_submit_t`](#c.sensor_submit_t) using [Real Time I/O (RTIO)](../../../services/rtio/index.md#rtio) to do non-blocking bus transfers if possible.
- MAY implement [`sensor_submit_t`](#c.sensor_submit_t) using a work queue if
  [Real Time I/O (RTIO)](../../../services/rtio/index.md#rtio) is unsupported by the bus.
- SHOULD implement [`sensor_submit_t`](#c.sensor_submit_t) checking the [`rtio_sqe`](../../../services/rtio/index.md#c.rtio_sqe "rtio_sqe")
  is of type `RTIO_SQE_RX` (read request).
- SHOULD implement [`sensor_submit_t`](#c.sensor_submit_t) checking all requested channels
  supported or respond with an error if not.
- SHOULD implement [`sensor_submit_t`](#c.sensor_submit_t) checking the provided buffer
  is large enough for the requested channels.
- SHOULD implement [`sensor_submit_t`](#c.sensor_submit_t) in a way that directly reads into
  the provided buffer avoiding copying of any kind, with few exceptions.
- MUST implement [`sensor_decoder_api`](#c.sensor_decoder_api) with pure stateless functions. All state needed to convert the raw sensor readings into
  fixed point SI united values must be in the provided buffer.
- MUST implement [`sensor_get_decoder_t`](#c.sensor_get_decoder_t) returning the
  [`sensor_decoder_api`](#c.sensor_decoder_api) for that device type.

## API Reference

Related code samples

[LVGL line chart with accelerometer data](../../../samples/modules/lvgl/accelerometer_chart/README.md#lvgl-accelerometer-chart "Display acceleration data on a real-time chart using LVGL.")
:   Display acceleration data on a real-time chart using LVGL.

[Secure MQTT Sensor/Actuator](../../../samples/net/secure_mqtt_sensor_actuator/README.md#secure-mqtt-sensor-actuator "Implement an MQTT-based IoT sensor/actuator device")
:   Implement an MQTT-based IoT sensor/actuator device

[X-NUCLEO-53L0A1 shield](../../../samples/shields/x_nucleo_53l0a1/README.md#x-nucleo-53l0a1 "Interact with the 7-segment display and VL53L0X ranging sensor of an X-NUCLEO-53L0A1 shield.")
:   Interact with the 7-segment display and VL53L0X ranging sensor of an X-NUCLEO-53L0A1 shield.

[X-NUCLEO-IKS01A1 shield](../../../samples/shields/x_nucleo_iks01a1/README.md#x-nucleo-iks01a1 "Interact with all the sensors of an X-NUCLEO-IKS01A1 shield.")
:   Interact with all the sensors of an X-NUCLEO-IKS01A1 shield.

[X-NUCLEO-IKS01A2 shield - SensorHub (Mode 2)](../../../samples/shields/x_nucleo_iks01a2/sensorhub/README.md#x-nucleo-iks01a2-shub "Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Sensor Hub mode.")
:   Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Sensor Hub mode.

[X-NUCLEO-IKS01A2 shield - Standard (Mode 1)](../../../samples/shields/x_nucleo_iks01a2/standard/README.md#x-nucleo-iks01a2-std "Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Standard Mode.")
:   Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Standard Mode.

[X-NUCLEO-IKS01A3 shield - SensorHub (Mode 2)](../../../samples/shields/x_nucleo_iks01a3/sensorhub/README.md#x-nucleo-iks01a3-shub "Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Sensor Hub mode.")
:   Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Sensor Hub mode.

[X-NUCLEO-IKS01A3 shield - Standard (Mode 1)](../../../samples/shields/x_nucleo_iks01a3/standard/README.md#x-nucleo-iks01a3-std "Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Standard mode.")
:   Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Standard mode.

[X-NUCLEO-IKS02A1 shield - SensorHub (Mode 2)](../../../samples/shields/x_nucleo_iks02a1/sensorhub/README.md#x-nucleo-iks02a1-shub "Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Sensor Hub mode.")
:   Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Sensor Hub mode.

[X-NUCLEO-IKS02A1 shield - Standard (Mode 1)](../../../samples/shields/x_nucleo_iks02a1/standard/README.md#x-nucleo-iks02a1-std "Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Standard mode.")
:   Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Standard mode.

*group* Sensor Interface
:   Sensor Interface.

    **Since**
    :   1.2

    **Version**
    :   1.0.0

    Defines

    SENSOR\_DECODE\_CONTEXT\_INIT(decoder\_, buffer\_, channel\_type\_, channel\_index\_)
    :   Initialize a [sensor\_decode\_context](#structsensor__decode__context).

    SENSOR\_STREAM\_TRIGGER\_PREP(\_trigger, \_opt)

    SENSOR\_DT\_READ\_IODEV(name, dt\_node, ...)
    :   Define a reading instance of a sensor.

        Use this macro to generate a [rtio\_iodev](../../../services/rtio/index.md#structrtio__iodev) for reading specific channels. Example:

        ```text
         (.c)
        SENSOR_DT_READ_IODEV(icm42688_accelgyro, DT_NODELABEL(icm42688),
            { SENSOR_CHAN_ACCEL_XYZ, 0 },
            { SENSOR_CHAN_GYRO_XYZ, 0 });

        int main(void) {
          sensor_read_async_mempool(&icm42688_accelgyro, &rtio);
        }
        ```

    SENSOR\_DT\_STREAM\_IODEV(name, dt\_node, ...)
    :   Define a stream instance of a sensor.

        Use this macro to generate a [rtio\_iodev](../../../services/rtio/index.md#structrtio__iodev) for starting a stream that’s triggered by specific interrupts. Example:

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
        :   - **true** – if `chan` is any of [SENSOR\_CHAN\_ACCEL\_XYZ](#group__sensor__interface_1ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9), [SENSOR\_CHAN\_GYRO\_XYZ](#group__sensor__interface_1ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e), or [SENSOR\_CHAN\_MAGN\_XYZ](#group__sensor__interface_1ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32), or [SENSOR\_CHAN\_POS\_DXYZ](#group__sensor__interface_1ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740)
            - **false** – otherwise

    SENSOR\_G
    :   The value of gravitational constant in micro m/s^2.

    SENSOR\_PI
    :   The value of constant PI in micros.

    SENSOR\_INFO\_DEFINE(name, ...)

    SENSOR\_INFO\_DT\_DEFINE(node\_id)

    SENSOR\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, data\_ptr, cfg\_ptr, level, prio, api\_ptr, ...)
    :   Like [DEVICE\_DT\_DEFINE()](../../../kernel/drivers/index.md#group__device__model_1gac49e26fbe91a14307d5ea08d41561dd1) with sensor specifics.

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

    typedef void (\*sensor\_trigger\_handler\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [sensor\_trigger](#c.sensor_trigger) \*trigger)
    :   Callback API upon firing of a trigger.

        Param dev:
        :   Pointer to the sensor device

        Param trigger:
        :   The trigger

    typedef int (\*sensor\_attr\_set\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan, enum [sensor\_attribute](#c.sensor_attribute) attr, const struct [sensor\_value](#c.sensor_value) \*val)
    :   Callback API upon setting a sensor’s attributes.

        See [sensor\_attr\_set()](#group__sensor__interface_1gafbf65226a227e9f8824908bc38e336f5) for argument description

    typedef int (\*sensor\_attr\_get\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan, enum [sensor\_attribute](#c.sensor_attribute) attr, struct [sensor\_value](#c.sensor_value) \*val)
    :   Callback API upon getting a sensor’s attributes.

        See [sensor\_attr\_get()](#group__sensor__interface_1gaedfdfc71dce702dc1fb1c6e60ff0f73a) for argument description

    typedef int (\*sensor\_trigger\_set\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [sensor\_trigger](#c.sensor_trigger) \*trig, [sensor\_trigger\_handler\_t](#c.sensor_trigger_handler_t) handler)
    :   Callback API for setting a sensor’s trigger and handler.

        See [sensor\_trigger\_set()](#group__sensor__interface_1ga7c72aca732e0641612d2f9437c2e41b7) for argument description

    typedef int (\*sensor\_sample\_fetch\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan)
    :   Callback API for fetching data from a sensor.

        See [sensor\_sample\_fetch()](#group__sensor__interface_1gaa75e25d93ee7cac0bf38399f3c006dff) for argument description

    typedef int (\*sensor\_channel\_get\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan, struct [sensor\_value](#c.sensor_value) \*val)
    :   Callback API for getting a reading from a sensor.

        See [sensor\_channel\_get()](#group__sensor__interface_1ga9e0e6c1408d32c52267984bae7cb268d) for argument description

    typedef int (\*sensor\_get\_decoder\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [sensor\_decoder\_api](#c.sensor_decoder_api) \*\*api)
    :   Get the decoder associate with the given device.

        See also

        [sensor\_get\_decoder](#group__sensor__interface_1ga12db6fc43adce48d34c25c16fd2336a3) for more details

    typedef void (\*sensor\_submit\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*sensor, struct [rtio\_iodev\_sqe](../../../services/rtio/index.md#c.rtio_iodev_sqe "rtio_iodev_sqe") \*sqe)

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
        :   **[in]** The optional userdata passed to [sensor\_read\_async\_mempool()](#group__sensor__interface_1gab9eee9440b46b545b1faae224ae5949a)

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

        enumerator SENSOR\_CHAN\_O2
        :   O2 level, in parts per million (ppm).

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

        enumerator SENSOR\_CHAN\_POS\_DXYZ
        :   Position change on the X, Y and Z axis, in points.

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

    static inline bool sensor\_chan\_spec\_eq(struct [sensor\_chan\_spec](#c.sensor_chan_spec) chan\_spec0, struct [sensor\_chan\_spec](#c.sensor_chan_spec) chan\_spec1)
    :   Check if channel specs are equivalent.

        Parameters:
        :   - **chan\_spec0** – First chan spec
            - **chan\_spec1** – Second chan spec

        Return values:
        :   - **true** – If equivalent
            - **false** – If not equivalent

    static inline int sensor\_decode(struct [sensor\_decode\_context](#c.sensor_decode_context) \*ctx, void \*out, uint16\_t max\_count)
    :   Decode N frames using a [sensor\_decode\_context](#structsensor__decode__context).

        Parameters:
        :   - **ctx** – **[inout]** The context to use for decoding
            - **out** – **[out]** The output buffer
            - **max\_count** – **[in]** Maximum number of frames to decode

        Returns:
        :   The decode result from [sensor\_decoder\_api](#structsensor__decoder__api)’s decode function

    int sensor\_natively\_supported\_channel\_size\_info(struct [sensor\_chan\_spec](#c.sensor_chan_spec) channel, size\_t \*base\_size, size\_t \*frame\_size)

    int sensor\_attr\_set(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan, enum [sensor\_attribute](#c.sensor_attribute) attr, const struct [sensor\_value](#c.sensor_value) \*val)
    :   Set an attribute for a sensor.

        Parameters:
        :   - **dev** – Pointer to the sensor device
            - **chan** – The channel the attribute belongs to, if any. Some attributes may only be set for all channels of a device, depending on device capabilities.
            - **attr** – The attribute to set
            - **val** – The value to set the attribute to

        Returns:
        :   0 if successful, negative errno code if failure.

    int sensor\_attr\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan, enum [sensor\_attribute](#c.sensor_attribute) attr, struct [sensor\_value](#c.sensor_value) \*val)
    :   Get an attribute for a sensor.

        Parameters:
        :   - **dev** – Pointer to the sensor device
            - **chan** – The channel the attribute belongs to, if any. Some attributes may only be set for all channels of a device, depending on device capabilities.
            - **attr** – The attribute to get
            - **val** – Pointer to where to store the attribute

        Returns:
        :   0 if successful, negative errno code if failure.

    static inline int sensor\_trigger\_set(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [sensor\_trigger](#c.sensor_trigger) \*trig, [sensor\_trigger\_handler\_t](#c.sensor_trigger_handler_t) handler)
    :   Activate a sensor’s trigger and set the trigger handler.

        The handler will be called from a thread, so I2C or SPI operations are safe. However, the thread’s stack is limited and defined by the driver. It is currently up to the caller to ensure that the handler does not overflow the stack.

        The user-allocated trigger will be stored by the driver as a pointer, rather than a copy, and passed back to the handler. This enables the handler to use CONTAINER\_OF to retrieve a context pointer when the trigger is embedded in a larger struct and requires that the trigger is not allocated on the stack.

        **Function properties (list may not be complete)**
        :   [supervisor](../../../develop/api/terminology.md#api-term-supervisor)

        Parameters:
        :   - **dev** – Pointer to the sensor device
            - **trig** – The trigger to activate
            - **handler** – The function that should be called when the trigger fires

        Returns:
        :   0 if successful, negative errno code if failure.

    int sensor\_sample\_fetch(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Fetch a sample from the sensor and store it in an internal driver buffer.

        Read all of a sensor’s active channels and, if necessary, perform any additional operations necessary to make the values useful. The user may then get individual channel values by calling [sensor\_channel\_get](#group__sensor__interface_1ga9e0e6c1408d32c52267984bae7cb268d).

        The function blocks until the fetch operation is complete.

        Since the function communicates with the sensor device, it is unsafe to call it in an ISR if the device is connected via I2C or SPI.

        Parameters:
        :   - **dev** – Pointer to the sensor device

        Returns:
        :   0 if successful, negative errno code if failure.

    int sensor\_sample\_fetch\_chan(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) type)
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

    int sensor\_channel\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensor\_channel](#c.sensor_channel) chan, struct [sensor\_value](#c.sensor_value) \*val)
    :   Get a reading from a sensor device.

        Return a useful value for a particular channel, from the driver’s internal data. Before calling this function, a sample must be obtained by calling [sensor\_sample\_fetch](#group__sensor__interface_1gaa75e25d93ee7cac0bf38399f3c006dff) or [sensor\_sample\_fetch\_chan](#group__sensor__interface_1gac16192826432438a15274cf28d66e8a6). It is guaranteed that two subsequent calls of this function for the same channels will yield the same value, if [sensor\_sample\_fetch](#group__sensor__interface_1gaa75e25d93ee7cac0bf38399f3c006dff) or [sensor\_sample\_fetch\_chan](#group__sensor__interface_1gac16192826432438a15274cf28d66e8a6) has not been called in the meantime.

        For vectorial data samples you can request all axes in just one call by passing the specific channel with \_XYZ suffix. The sample will be returned at val[0], val[1] and val[2] (X, Y and Z in that order).

        Parameters:
        :   - **dev** – Pointer to the sensor device
            - **chan** – The channel to read
            - **val** – Where to store the value

        Returns:
        :   0 if successful, negative errno code if failure.

    int sensor\_get\_decoder(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [sensor\_decoder\_api](#c.sensor_decoder_api) \*\*decoder)
    :   Get the sensor’s decoder API.

        Parameters:
        :   - **dev** – **[in]** The sensor device
            - **decoder** – **[in]** Pointer to the decoder which will be set upon success

        Returns:
        :   0 on success

        Returns:
        :   < 0 on error

    int sensor\_reconfigure\_read\_iodev(struct [rtio\_iodev](../../../services/rtio/index.md#c.rtio_iodev "rtio_iodev") \*iodev, const struct [device](../../../kernel/drivers/index.md#c.device "device") \*sensor, const struct [sensor\_chan\_spec](#c.sensor_chan_spec) \*channels, size\_t num\_channels)
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

    static inline int sensor\_stream(struct [rtio\_iodev](../../../services/rtio/index.md#c.rtio_iodev "rtio_iodev") \*iodev, struct [rtio](../../../services/rtio/index.md#c.rtio "rtio") \*ctx, void \*userdata, struct [rtio\_sqe](../../../services/rtio/index.md#c.rtio_sqe "rtio_sqe") \*\*handle)

    static inline int sensor\_read(struct [rtio\_iodev](../../../services/rtio/index.md#c.rtio_iodev "rtio_iodev") \*iodev, struct [rtio](../../../services/rtio/index.md#c.rtio "rtio") \*ctx, uint8\_t \*buf, size\_t buf\_len)
    :   Blocking one shot read of samples from a sensor into a buffer.

        Using `cfg`, read data from the device by using the provided RTIO context `ctx`. This call will generate a [rtio\_sqe](../../../services/rtio/index.md#structrtio__sqe) that will be given the provided buffer. The call will wait for the read to complete before returning to the caller.

        Parameters:
        :   - **iodev** – **[in]** The iodev created by [SENSOR\_DT\_READ\_IODEV](#group__sensor__interface_1ga0cc1ee28114557e9e00257071c7dfa9f)
            - **ctx** – **[in]** The RTIO context to service the read
            - **buf** – **[in]** Pointer to memory to read sample data into
            - **buf\_len** – **[in]** Size in bytes of the given memory that are valid to read into

        Returns:
        :   0 on success

        Returns:
        :   < 0 on error

    static inline int sensor\_read\_async\_mempool(struct [rtio\_iodev](../../../services/rtio/index.md#c.rtio_iodev "rtio_iodev") \*iodev, struct [rtio](../../../services/rtio/index.md#c.rtio "rtio") \*ctx, void \*userdata)
    :   One shot non-blocking read with pool allocated buffer.

        Using `cfg`, read one snapshot of data from the device by using the provided RTIO context `ctx`. This call will generate a [rtio\_sqe](../../../services/rtio/index.md#structrtio__sqe) that will leverage the RTIO’s internal mempool when the time comes to service the read.

        Parameters:
        :   - **iodev** – **[in]** The iodev created by [SENSOR\_DT\_READ\_IODEV](#group__sensor__interface_1ga0cc1ee28114557e9e00257071c7dfa9f)
            - **ctx** – **[in]** The RTIO context to service the read
            - **userdata** – **[in]** Optional userdata that will be available when the read is complete

        Returns:
        :   0 on success

        Returns:
        :   < 0 on error

    void sensor\_processing\_with\_callback(struct [rtio](../../../services/rtio/index.md#c.rtio "rtio") \*ctx, [sensor\_processing\_callback\_t](#c.sensor_processing_callback_t) cb)
    :   Helper function for common processing of sensor data.

        This function can be called in a blocking manner after [sensor\_read()](#group__sensor__interface_1ga1e77abad33cfd4b8330484cdc1354976) or in a standalone thread dedicated to processing. It will wait for a cqe from the RTIO context, once received, it will decode the userdata and call the `cb`. Once the `cb` returns, the buffer will be released back into `ctx's` mempool if available.

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

    struct sensor\_chan\_spec
    :   *#include <sensor.h>*

        Sensor Channel Specification.

        A sensor channel specification is a unique identifier per sensor device describing a measurement channel.

        Note

        Typically passed by value as the size of a [sensor\_chan\_spec](#structsensor__chan__spec) is a single word.

        Public Members

        uint16\_t chan\_type
        :   A sensor channel type.

        uint16\_t chan\_idx
        :   A sensor channel index.

    struct sensor\_decoder\_api
    :   *#include <sensor.h>*

        Decodes a single raw data buffer.

        Data buffers are provided on the [RTIO](../../../services/rtio/index.md#group__rtio) context that’s supplied to [sensor\_read](#group__sensor__interface_1ga1e77abad33cfd4b8330484cdc1354976).

        Public Members

        int (\*get\_frame\_count)(const uint8\_t \*buffer, struct [sensor\_chan\_spec](#c.sensor_chan_spec) channel, uint16\_t \*frame\_count)
        :   Get the number of frames in the current buffer.

            Param buffer:
            :   **[in]** The buffer provided on the [RTIO](../../../services/rtio/index.md#group__rtio) context.

            Param channel:
            :   **[in]** The channel to get the count for

            Param frame\_count:
            :   **[out]** The number of frames on the buffer (at least 1)

            Return:
            :   0 on success

            Return:
            :   -ENOTSUP if the channel/channel\_idx aren’t found

        int (\*get\_size\_info)(struct [sensor\_chan\_spec](#c.sensor_chan_spec) channel, size\_t \*base\_size, size\_t \*frame\_size)
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

        int (\*decode)(const uint8\_t \*buffer, struct [sensor\_chan\_spec](#c.sensor_chan_spec) channel, uint32\_t \*fit, uint16\_t max\_count, void \*data\_out)
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
            :   **[in]** The buffer provided on the [RTIO](../../../services/rtio/index.md#group__rtio) context

            Param channel:
            :   **[in]** The channel to decode

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
            :   **[in]** The buffer provided on the [RTIO](../../../services/rtio/index.md#group__rtio) context

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

*group* Sensor emulator backend API
:   Sensor emulator backend API.

    Functions

    static inline bool emul\_sensor\_backend\_is\_supported(const struct [emul](../../emulator/bus_emulators.md#c.emul "emul") \*target)
    :   Check if a given sensor emulator supports the backend API.

        Parameters:
        :   - **target** – Pointer to emulator instance to query

        Returns:
        :   True if supported, false if unsupported or if `target` is NULL.

    static inline int emul\_sensor\_backend\_set\_channel(const struct [emul](../../emulator/bus_emulators.md#c.emul "emul") \*target, struct [sensor\_chan\_spec](#c.sensor_chan_spec) ch, const [q31\_t](../../../services/dsp/index.md#c.q31_t "q31_t") \*value, int8\_t shift)
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

    static inline int emul\_sensor\_backend\_get\_sample\_range(const struct [emul](../../emulator/bus_emulators.md#c.emul "emul") \*target, struct [sensor\_chan\_spec](#c.sensor_chan_spec) ch, [q31\_t](../../../services/dsp/index.md#c.q31_t "q31_t") \*lower, [q31\_t](../../../services/dsp/index.md#c.q31_t "q31_t") \*upper, [q31\_t](../../../services/dsp/index.md#c.q31_t "q31_t") \*epsilon, int8\_t \*shift)
    :   Query an emulator for a channel’s supported sample value range and tolerance.

        Parameters:
        :   - **target** – Pointer to emulator instance to operate on
            - **ch** – The channel to request info for. If `ch` is unsupported, return `-[ENOTSUP](../../../develop/languages/c/minimal_libc.md#group__system__errno_1ga91457bbf35f0f1085619a99423bb1f33)`
            - **lower** – **[out]** Minimum supported sample value in SI units, fixed-point format
            - **upper** – **[out]** Maximum supported sample value in SI units, fixed-point format
            - **epsilon** – **[out]** Tolerance to use comparing expected and actual values to account for rounding and sensor precision issues. This can usually be set to the minimum sample value step size. Uses SI units and fixed-point format.
            - **shift** – **[out]** The shift value (scaling factor) associated with `lower`, `upper`, and `epsilon`.

        Returns:
        :   0 if successful

        Returns:
        :   -ENOTSUP if no backend API or if channel not supported by emul

    static inline int emul\_sensor\_backend\_set\_attribute(const struct [emul](../../emulator/bus_emulators.md#c.emul "emul") \*target, struct [sensor\_chan\_spec](#c.sensor_chan_spec) ch, enum [sensor\_attribute](#c.sensor_attribute) attribute, const void \*value)
    :   Set the emulator’s attribute values.

        Parameters:
        :   - **target** – **[in]** Pointer to emulator instance to operate on
            - **ch** – **[in]** The channel to request info for. If `ch` is unsupported, return `-[ENOTSUP](../../../develop/languages/c/minimal_libc.md#group__system__errno_1ga91457bbf35f0f1085619a99423bb1f33)`
            - **attribute** – **[in]** The attribute to set
            - **value** – **[in]** the value to use (cast according to the channel/attribute pair)

        Returns:
        :   0 is successful

        Returns:
        :   < 0 on error

    static inline int emul\_sensor\_backend\_get\_attribute\_metadata(const struct [emul](../../emulator/bus_emulators.md#c.emul "emul") \*target, struct [sensor\_chan\_spec](#c.sensor_chan_spec) ch, enum [sensor\_attribute](#c.sensor_attribute) attribute, [q31\_t](../../../services/dsp/index.md#c.q31_t "q31_t") \*min, [q31\_t](../../../services/dsp/index.md#c.q31_t "q31_t") \*max, [q31\_t](../../../services/dsp/index.md#c.q31_t "q31_t") \*increment, int8\_t \*shift)
    :   Get metadata about an attribute.

        Information provided by this function includes the minimum/maximum values of the attribute as well as the increment (value per LSB) which can be used as an epsilon when comparing results.

        Parameters:
        :   - **target** – **[in]** Pointer to emulator instance to operate on
            - **ch** – **[in]** The channel to request info for. If `ch` is unsupported, return ‘-ENOTSUP’
            - **attribute** – **[in]** The attribute to request info for. If `attribute` is unsupported, return ‘-ENOTSUP’
            - **min** – **[out]** The minimum value the attribute can be set to
            - **max** – **[out]** The maximum value the attribute can be set to
            - **increment** – **[out]** The value that the attribute increases by for every LSB
            - **shift** – **[out]** The shift for `min`, `max`, and `increment`

        Returns:
        :   0 on SUCCESS

        Returns:
        :   < 0 on error
