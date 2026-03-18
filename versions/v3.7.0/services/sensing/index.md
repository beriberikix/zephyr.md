---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/sensing/index.html
original_path: services/sensing/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Sensing Subsystem

## [Overview](#id1)

Sensing Subsystem is a high level sensor framework inside the OS user
space service layer. It is a framework focused on sensor fusion, client
arbitration, sampling, timing, scheduling and sensor based power management.

Key concepts in Sensing Subsystem include physical sensor and virtual sensor objects,
and a scheduling framework over sensor object relationships.
Physical sensors do not depend on any other sensor objects for input, and
will directly interact with existing zephyr sensor device drivers.
Virtual sensors rely on other sensor objects (physical or virtual) as
report inputs.

The sensing subsystem relies on Zephyr sensor device APIs (existing version or update in future)
to leverage Zephyr’s large library of sensor device drivers (100+).

Use of the sensing subsystem is optional. Applications that only need to access simple sensors
devices can use the Zephyr [Sensors](../../hardware/peripherals/sensor/index.md#sensor) API directly.

Since the sensing subsystem is separated from device driver layer or
kernel space and could support various customizations and sensor
algorithms in user space with virtual sensor concepts. The existing
sensor device driver can focus on low layer device side works, can keep
simple as much as possible, just provide device HW abstraction and
operations etc. This is very good for system stability.

The sensing subsystem is decoupled with any sensor expose/transfer
protocols, the target is to support various up-layer frameworks and
Applications with different sensor expose/transfer protocols,
such as [CHRE](https://github.com/zephyrproject-rtos/chre), HID sensors Applications,
MQTT sensor Applications according different products requirements. Or even support multiple
Applications with different up-layer sensor protocols at the same time
with it’s multiple clients support design.

Sensing subsystem can help build a unified Zephyr sensing architecture for
cross host OSes support and as well as IoT sensor solutions.

The diagram below illustrates how the Sensing Subsystem integrates with up-layer frameworks.

![Unified Zephyr sensing architecture.](../../_images/sensing_solution.png)

## [Configurability](#id2)

- Reusable and configurable standalone subsystem.
- Based on Zephyr existing low-level Sensor API (reuse 100+ existing sensor device drivers)
- Provide Zephyr high-level Sensing Subsystem API for Applications.
- Separate option CHRE Sensor PAL Implementation module to support CHRE.
- Decoupled with any host link protocols, it’s Zephyr Application’s role to handle different
  protocols (MQTT, HID or Private, all configurable)

## [Main Features](#id3)

- Scope
  :   - Focus on framework for sensor fusion, multiple clients, arbitration, data sampling, timing
        management and scheduling.
- Sensor Abstraction
  :   - `Physical sensor`: interacts with Zephyr sensor device drivers, focus on data collecting.
      - `Virtual sensor`: relies on other sensor(s), `physical` or `virtual`, focus on
        data fusion.
- Data Driven Model
  :   - `Polling mode`: periodical sampling rate
      - `Interrupt mode`: data ready, threshold interrupt etc.
- Scheduling
  :   - single thread main loop for all sensor objects sampling and process.
- Buffer Mode for Batching
- Configurable Via Device Tree

Below diagram shows the API position and scope:

![Sensing subsystem API organization.](../../_images/sensing_api_org.png)

`Sensing Subsystem API` is for Applications.
`Sensing Sensor API` is for development `sensors`.

## [Major Flows](#id4)

- Sensor Configuration Flow

![Sensor Configuration Flow (App set report interval to hinge angel sensor example).](../../_images/sensor_config_flow.png)

- Sensor Data Flow

![Sensor Data Flow (App receive hinge angel data through data event callback example).](../../_images/sensor_data_flow.png)

## [Sensor Types And Instance](#id5)

The `Sensing Subsystem` supports multiple instances of the same sensor type,
there’re two methods for Applications to identify and open an unique sensor instance:

- Enumerate all sensor instances

  [`sensing_get_sensors()`](#c.sensing_get_sensors) returns all current board configuration supported sensor instances’
  information in a [`sensing_sensor_info`](#c.sensing_sensor_info) pointer array .

  Then Applications can use [`sensing_open_sensor()`](#c.sensing_open_sensor) to
  open specific sensor instance for future accessing, configuration and receive sensor data etc.

  This method is suitable for supporting some up-layer frameworks like `CHRE`, `HID` which need
  to dynamically enumerate the underlying platform’s sensor instances.
- Open the sensor instance by devicetree node directly

  Applications can use [`sensing_open_sensor_by_dt()`](#c.sensing_open_sensor_by_dt) to open a sensor instance directly with
  sensor devicetree node identifier.

  For example:

```c
sensing_open_sensor_by_dt(DEVICE_DT_GET(DT_NODELABEL(base_accel)), cb_list, handle);
sensing_open_sensor_by_dt(DEVICE_DT_GET(DT_CHOSEN(zephyr_sensing_base_accel)), cb_list, handle);
```

This method is useful and easy use for some simple Application which just want to access specific
sensor(s).

`Sensor type` follows the
[HID standard sensor types definition](https://usb.org/sites/default/files/hutrr39b_0.pdf).

See [include/zephyr/sensing/sensing\_sensor\_types.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sensing/sensing_sensor_types.h)

## [Sensor Instance Handler](#id6)

Clients using a [`sensing_sensor_handle_t`](#c.sensing_sensor_handle_t) type handler to handle a opened sensor
instance, and all subsequent operations on this sensor instance need use this handler,
such as set configurations, read sensor sample data, etc.

For a sensor instance, could have two kinds of clients:
`Application clients` and `Sensor clients`.

`Application clients` can use [`sensing_open_sensor()`](#c.sensing_open_sensor) to open a sensor instance
and get it’s handler.

For `Sensor clients`, there is no open API for opening a reporter, because the client-report
relationship is built at the sensor’s registration stage with devicetree.

The `Sensing Subsystem` will auto open and create `handlers` for client sensor
to it’s reporter sensors.
`Sensor clients` can get it’s reporters’ handlers via [`sensing_sensor_get_reporters()`](#c.sensing_sensor_get_reporters).

![Sensor Reporting Topology.](../../_images/sensor_top.png)

Note

Sensors inside the Sensing Subsystem, the reporting relationship between them are all auto
generated by Sensing Subsystem according devicetree definitions, handlers between client sensor
and reporter sensors are auto created.
Application(s) need to call [`sensing_open_sensor()`](#c.sensing_open_sensor) to explicitly open the sensor instance.

## [Sensor Sample Value](#id7)

- Data Structure

  Each sensor sample value defines as a common `header` + `readings[]` data structure, like
  [`sensing_sensor_value_3d_q31`](#c.sensing_sensor_value_3d_q31), [`sensing_sensor_value_q31`](#c.sensing_sensor_value_q31), and
  [`sensing_sensor_value_uint32`](#c.sensing_sensor_value_uint32).

  The `header` definition [`sensing_sensor_value_header()`](#c.sensing_sensor_value_header).
- Time Stamp

  Time stamp unit in sensing subsystem is `micro seconds`.

  The `header` defines a **base\_timestamp**, and
  each element in the **readings[]** array defines **timestamp\_delta**.

  The **timestamp\_delta** is in relation to the previous **readings** (or the **base\_timestamp**)

  For example:

  - timestamp of `readings[0]` is `header.base_timestamp` + `readings[0].timestamp_delta`.
  - timestamp of `readings[1]` is `timestamp of readings[0]` + `readings[1].timestamp_delta`.

  Since timestamp unit is micro seconds,
  the max **timestamp\_delta** (`uint32_t`) is `4295` seconds.

  If a sensor has batched data where two consecutive readings differ by more than `4295` seconds,
  the sensing subsystem runtime will split them across multiple instances of the readings structure,
  and send multiple events.

  This concept is referred from [CHRE Sensor API](https://github.com/zephyrproject-rtos/chre/blob/zephyr/chre_api/include/chre_api/chre/sensor_types.h).
- Data Format

  `Sensing Subsystem` uses per sensor type defined data format structure,
  and support `Q Format` defined in [include/zephyr/dsp/types.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dsp/types.h)
  for `zdsp` lib support.

  For example [`sensing_sensor_value_3d_q31`](#c.sensing_sensor_value_3d_q31) can be used by 3D IMU sensors like
  [`SENSING_SENSOR_TYPE_MOTION_ACCELEROMETER_3D`](#c.SENSING_SENSOR_TYPE_MOTION_ACCELEROMETER_3D),
  [`SENSING_SENSOR_TYPE_MOTION_UNCALIB_ACCELEROMETER_3D`](#c.SENSING_SENSOR_TYPE_MOTION_UNCALIB_ACCELEROMETER_3D),
  and [`SENSING_SENSOR_TYPE_MOTION_GYROMETER_3D`](#c.SENSING_SENSOR_TYPE_MOTION_GYROMETER_3D).

  [`sensing_sensor_value_uint32`](#c.sensing_sensor_value_uint32) can be used by
  [`SENSING_SENSOR_TYPE_LIGHT_AMBIENTLIGHT`](#c.SENSING_SENSOR_TYPE_LIGHT_AMBIENTLIGHT) sensor,

  and [`sensing_sensor_value_q31`](#c.sensing_sensor_value_q31) can be used by
  [`SENSING_SENSOR_TYPE_MOTION_HINGE_ANGLE`](#c.SENSING_SENSOR_TYPE_MOTION_HINGE_ANGLE) sensor

  See [include/zephyr/sensing/sensing\_datatypes.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sensing/sensing_datatypes.h)

## [Device Tree Configuration](#id8)

Sensing subsystem using device tree to configuration all sensor instances and their properties,
reporting relationships.

See the example [samples/subsys/sensing/simple/boards/native\_sim.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/sensing/simple/boards/native_sim.overlay)

## [API Reference](#id9)

*group* Sensor Types
:   Sensor Types Definition.

    Sensor types definition followed HID standard. [https://usb.org/sites/default/files/hutrr39b\_0.pdf](https://usb.org/sites/default/files/hutrr39b_0.pdf)

    TODO: will add more types

    Defines

    SENSING\_SENSOR\_TYPE\_LIGHT\_AMBIENTLIGHT
    :   sensor category light

    SENSING\_SENSOR\_TYPE\_MOTION\_ACCELEROMETER\_3D
    :   sensor category motion

    SENSING\_SENSOR\_TYPE\_MOTION\_GYROMETER\_3D

    SENSING\_SENSOR\_TYPE\_MOTION\_MOTION\_DETECTOR

    SENSING\_SENSOR\_TYPE\_OTHER\_CUSTOM
    :   sensor category other

    SENSING\_SENSOR\_TYPE\_MOTION\_UNCALIB\_ACCELEROMETER\_3D

    SENSING\_SENSOR\_TYPE\_MOTION\_HINGE\_ANGLE

    SENSING\_SENSOR\_TYPE\_ALL
    :   Sensor type for all sensors.

        This macro defines the sensor type for all sensors.

*group* Data Types
:   Data Types .

    struct sensing\_sensor\_value\_header
    :   *#include <sensing\_datatypes.h>*

        sensor value header

        Each sensor value data structure should have this header

        Here use ‘base\_timestamp’ (uint64\_t) and ‘timestamp\_delta’ (uint32\_t) to save memory usage in batching mode.

        The ‘base\_timestamp’ is for readings[0], the ‘timestamp\_delta’ is relation to the previous ‘readings’. So, timestamp of readings[0] is header.base\_timestamp + readings[0].timestamp\_delta. timestamp of readings[1] is timestamp of readings[0] + readings[1].timestamp\_delta.

        Since timestamp unit is micro seconds, the max ‘timestamp\_delta’ (uint32\_t) is 4295 seconds.

        If a sensor has batched data where two consecutive readings differ by more than 4295 seconds, the sensor subsystem core will split them across multiple instances of the readings structure, and send multiple events.

        This concept is borrowed from CHRE: [https://cs.android.com/android/platform/superproject/+/master:](https://cs.android.com/android/platform/superproject/+/master:)\ system/chre/chre\_api/include/chre\_api/chre/sensor\_types.h

        Public Members

        uint64\_t base\_timestamp
        :   Base timestamp of this data readings, unit is micro seconds.

        uint16\_t reading\_count
        :   Count of this data readings.

    struct sensing\_sensor\_value\_3d\_q31
    :   *#include <sensing\_datatypes.h>*

        Sensor value data structure types based on common data types.

        Suitable for common sensors, such as IMU, Light sensors and orientation sensors.

        Sensor value data structure for 3-axis sensors. struct [sensing\_sensor\_value\_3d\_q31](#structsensing__sensor__value__3d__q31) can be used by 3D IMU sensors like: SENSING\_SENSOR\_TYPE\_MOTION\_ACCELEROMETER\_3D, SENSING\_SENSOR\_TYPE\_MOTION\_UNCALIB\_ACCELEROMETER\_3D, SENSING\_SENSOR\_TYPE\_MOTION\_GYROMETER\_3D, q31 version

        Public Members

        struct [sensing\_sensor\_value\_header](#c.sensing_sensor_value_header) header
        :   Header of the sensor value data structure.

        int8\_t shift
        :   The shift value for the [q31\_t](../dsp/index.md#group__math__dsp_1gadc89a3547f5324b7b3b95adec3806bc0) v[3] reading.

        uint32\_t timestamp\_delta
        :   Timestamp delta of the reading.

            Unit is micro seconds.

        [q31\_t](../dsp/index.md#c.q31_t "q31_t") v[3]
        :   3D vector of the reading represented as an array.

            For SENSING\_SENSOR\_TYPE\_MOTION\_ACCELEROMETER\_3D and SENSING\_SENSOR\_TYPE\_MOTION\_UNCALIB\_ACCELEROMETER\_3D, the unit is Gs (gravitational force). For SENSING\_SENSOR\_TYPE\_MOTION\_GYROMETER\_3D, the unit is degrees.

        [q31\_t](../dsp/index.md#c.q31_t "q31_t") x
        :   X value of the 3D vector.

        [q31\_t](../dsp/index.md#c.q31_t "q31_t") y
        :   Y value of the 3D vector.

        [q31\_t](../dsp/index.md#c.q31_t "q31_t") z
        :   Z value of the 3D vector.

        struct [sensing\_sensor\_value\_3d\_q31](#c.sensing_sensor_value_3d_q31).[anonymous] readings[1]
        :   Array of readings.

    struct sensing\_sensor\_value\_uint32
    :   *#include <sensing\_datatypes.h>*

        Sensor value data structure for single 1-axis value.

        struct [sensing\_sensor\_value\_uint32](#structsensing__sensor__value__uint32) can be used by SENSING\_SENSOR\_TYPE\_LIGHT\_AMBIENTLIGHT sensor uint32\_t version

        Public Members

        struct [sensing\_sensor\_value\_header](#c.sensing_sensor_value_header) header
        :   Header of the sensor value data structure.

        uint32\_t timestamp\_delta
        :   Timestamp delta of the reading.

            Unit is micro seconds.

        uint32\_t v
        :   Value of the reading.

            For SENSING\_SENSOR\_TYPE\_LIGHT\_AMBIENTLIGHT, the unit is luxs.

        struct [sensing\_sensor\_value\_uint32](#c.sensing_sensor_value_uint32).[anonymous] readings[1]
        :   Array of readings.

    struct sensing\_sensor\_value\_q31
    :   *#include <sensing\_datatypes.h>*

        Sensor value data structure for single 1-axis value.

        struct [sensing\_sensor\_value\_q31](#structsensing__sensor__value__q31) can be used by SENSING\_SENSOR\_TYPE\_MOTION\_HINGE\_ANGLE sensor q31 version

        Public Members

        struct [sensing\_sensor\_value\_header](#c.sensing_sensor_value_header) header
        :   Header of the sensor value data structure.

        int8\_t shift
        :   The shift value for the [q31\_t](../dsp/index.md#group__math__dsp_1gadc89a3547f5324b7b3b95adec3806bc0) v reading.

        uint32\_t timestamp\_delta
        :   Timestamp delta of the reading.

            Unit is micro seconds.

        [q31\_t](../dsp/index.md#c.q31_t "q31_t") v
        :   Value of the reading.

            For SENSING\_SENSOR\_TYPE\_MOTION\_HINGE\_ANGLE, the unit is degrees.

        struct [sensing\_sensor\_value\_q31](#c.sensing_sensor_value_q31).[anonymous] readings[1]
        :   Array of readings.

Related code samples

[Sensing subsystem](../../samples/subsys/sensing/simple/README.md#sensing "Get high-level sensor data in defined intervals.")
:   Get high-level sensor data in defined intervals.

*group* Sensing Subsystem API
:   Sensing Subsystem API .

    Defines

    SENSING\_SENSOR\_VERSION(\_major, \_minor, \_hotfix, \_build)
    :   Macro to create a sensor version value.

    SENSING\_SENSOR\_FLAG\_REPORT\_ON\_EVENT
    :   Sensor flag indicating if this sensor is on event reporting data.

        Reporting sensor data when the sensor event occurs, such as a motion detect sensor reporting a motion or motionless detected event.

    SENSING\_SENSOR\_FLAG\_REPORT\_ON\_CHANGE
    :   Sensor flag indicating if this sensor is on change reporting data.

        Reporting sensor data when the sensor data changes.

        Exclusive with [SENSING\_SENSOR\_FLAG\_REPORT\_ON\_EVENT](#group__sensing__api_1ga498dcf4dbd0eb42d8ca399df4acc2e5e)

    SENSING\_SENSITIVITY\_INDEX\_ALL
    :   SENSING\_SENSITIVITY\_INDEX\_ALL indicating sensitivity of each data field should be set.

    Typedefs

    typedef void \*sensing\_sensor\_handle\_t
    :   Define Sensing subsystem sensor handle.

    typedef void (\*sensing\_data\_event\_t)([sensing\_sensor\_handle\_t](#c.sensing_sensor_handle_t) handle, const void \*buf, void \*context)
    :   Sensor data event receive callback.

        Param handle:
        :   The sensor instance handle.

        Param buf:
        :   The data buffer with sensor data.

        Param context:
        :   User provided context pointer.

    Enums

    enum sensing\_sensor\_state
    :   Sensing subsystem sensor state.

        *Values:*

        enumerator SENSING\_SENSOR\_STATE\_READY = 0
        :   The sensor is ready.

        enumerator SENSING\_SENSOR\_STATE\_OFFLINE = 1
        :   The sensor is offline.

    enum sensing\_sensor\_attribute
    :   Sensing subsystem sensor config attribute.

        *Values:*

        enumerator SENSING\_SENSOR\_ATTRIBUTE\_INTERVAL = 0
        :   The interval attribute of a sensor configuration.

        enumerator SENSING\_SENSOR\_ATTRIBUTE\_SENSITIVITY = 1
        :   The sensitivity attribute of a sensor configuration.

        enumerator SENSING\_SENSOR\_ATTRIBUTE\_LATENCY = 2
        :   The latency attribute of a sensor configuration.

        enumerator SENSING\_SENSOR\_ATTRIBUTE\_MAX
        :   The maximum number of attributes that a sensor configuration can have.

    Functions

    int sensing\_get\_sensors(int \*num\_sensors, const struct [sensing\_sensor\_info](#c.sensing_sensor_info) \*\*info)
    :   Get all supported sensor instances’ information.

        This API just returns read only information of sensor instances, pointer info will directly point to internal buffer, no need for caller to allocate buffer, no side effect to sensor instances.

        Parameters:
        :   - **num\_sensors** – Get number of sensor instances.
            - **info** – For receiving sensor instances’ information array pointer.

        Returns:
        :   0 on success or negative error value on failure.

    int sensing\_open\_sensor(const struct [sensing\_sensor\_info](#c.sensing_sensor_info) \*info, struct [sensing\_callback\_list](#c.sensing_callback_list) \*cb\_list, [sensing\_sensor\_handle\_t](#c.sensing_sensor_handle_t) \*handle)
    :   Open sensor instance by sensing sensor info.

        Application clients use it to open a sensor instance and get its handle. Support multiple Application clients for open same sensor instance, in this case, the returned handle will different for different clients. meanwhile, also register sensing callback list

        Parameters:
        :   - **info** – The sensor info got from [sensing\_get\_sensors](#group__sensing__api_1gaf3b6c66c2db12115f3ebec0cdba32e86)
            - **cb\_list** – callback list to be registered to sensing, must have a static lifetime.
            - **handle** – The opened instance handle, if failed will be set to NULL.

        Returns:
        :   0 on success or negative error value on failure.

    int sensing\_open\_sensor\_by\_dt(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [sensing\_callback\_list](#c.sensing_callback_list) \*cb\_list, [sensing\_sensor\_handle\_t](#c.sensing_sensor_handle_t) \*handle)
    :   Open sensor instance by device.

        Application clients use it to open a sensor instance and get its handle. Support multiple Application clients for open same sensor instance, in this case, the returned handle will different for different clients. meanwhile, also register sensing callback list.

        Parameters:
        :   - **dev** – pointer device get from device tree.
            - **cb\_list** – callback list to be registered to sensing, must have a static lifetime.
            - **handle** – The opened instance handle, if failed will be set to NULL.

        Returns:
        :   0 on success or negative error value on failure.

    int sensing\_close\_sensor([sensing\_sensor\_handle\_t](#c.sensing_sensor_handle_t) \*handle)
    :   Close sensor instance.

        Parameters:
        :   - **handle** – The sensor instance handle need to close.

        Returns:
        :   0 on success or negative error value on failure.

    int sensing\_set\_config([sensing\_sensor\_handle\_t](#c.sensing_sensor_handle_t) handle, struct [sensing\_sensor\_config](#c.sensing_sensor_config) \*configs, int count)
    :   Set current config items to Sensing subsystem.

        Parameters:
        :   - **handle** – The sensor instance handle.
            - **configs** – The configs to be set according to config attribute.
            - **count** – count of configs.

        Returns:
        :   0 on success or negative error value on failure, not support etc.

    int sensing\_get\_config([sensing\_sensor\_handle\_t](#c.sensing_sensor_handle_t) handle, struct [sensing\_sensor\_config](#c.sensing_sensor_config) \*configs, int count)
    :   Get current config items from Sensing subsystem.

        Parameters:
        :   - **handle** – The sensor instance handle.
            - **configs** – The configs to be get according to config attribute.
            - **count** – count of configs.

        Returns:
        :   0 on success or negative error value on failure, not support etc.

    const struct [sensing\_sensor\_info](#c.sensing_sensor_info) \*sensing\_get\_sensor\_info([sensing\_sensor\_handle\_t](#c.sensing_sensor_handle_t) handle)
    :   Get sensor information from sensor instance handle.

        Parameters:
        :   - **handle** – The sensor instance handle.

        Returns:
        :   a const pointer to [sensing\_sensor\_info](#structsensing__sensor__info) on success or NULL on failure.

    struct sensing\_sensor\_version
    :   *#include <sensing.h>*

        Sensor Version.

        Public Members

        uint32\_t value
        :   The version represented as a 32-bit value.

        uint8\_t major
        :   The major version number.

        uint8\_t minor
        :   The minor version number.

        uint8\_t hotfix
        :   The hotfix version number.

        uint8\_t build
        :   The build version number.

    struct sensing\_sensor\_info
    :   *#include <sensing.h>*

        Sensor basic constant information.

        Public Members

        const char \*name
        :   Name of the sensor instance.

        const char \*friendly\_name
        :   Friendly name of the sensor instance.

        const char \*vendor
        :   Vendor name of the sensor instance.

        const char \*model
        :   Model name of the sensor instance.

        const int32\_t type
        :   Sensor type.

        const uint32\_t minimal\_interval
        :   Minimal report interval in micro seconds.

    struct sensing\_callback\_list
    :   *#include <sensing.h>*

        Sensing subsystem event callback list.

        Public Members

        [sensing\_data\_event\_t](#c.sensing_data_event_t) on\_data\_event
        :   Callback function for a sensor data event.

        void \*context
        :   Associated context with on\_data\_event.

    struct sensing\_sensor\_config
    :   *#include <sensing.h>*

        Sensing subsystem sensor configure, including interval, sensitivity, latency.

        Public Members

        enum [sensing\_sensor\_attribute](#c.sensing_sensor_attribute) attri
        :   Attribute of the sensor configuration.

        int8\_t data\_field
        :   [SENSING\_SENSITIVITY\_INDEX\_ALL](#group__sensing__api_1ga16ac7bd397836280f7e8b4aa82f8eb4c)

            Data field of the sensor configuration.

        uint32\_t interval
        :   Interval between two sensor samples in microseconds (us).

        uint32\_t sensitivity
        :   Sensitivity threshold for reporting new data.

            A new sensor sample is reported only if the difference between it and the previous sample exceeds this sensitivity value.

        uint64\_t latency
        :   Maximum duration for batching sensor samples before reporting in microseconds (us).

            This defines how long sensor samples can be accumulated before they must be reported.

*group* Sensing Sensor API
:   Sensing Sensor API .

    Defines

    SENSING\_SENSORS\_DT\_DEFINE(node, reg\_ptr, cb\_list\_ptr, init\_fn, pm\_device, data\_ptr, cfg\_ptr, level, prio, api\_ptr, ...)
    :   Like [SENSOR\_DEVICE\_DT\_DEFINE()](../../hardware/peripherals/sensor/index.md#group__sensor__interface_1gaa67ca630e3931a0c3821ba438c86690c) with sensing specifics.

        Defines a sensor which implements the sensor API. May define an element in the sensing sensor iterable section used to enumerate all sensing sensors.

        Parameters:
        :   - **node** – The devicetree node identifier.
            - **reg\_ptr** – Pointer to the device’s [sensing\_sensor\_register\_info](#structsensing__sensor__register__info).
            - **cb\_list\_ptr** – Pointer to sensing callback list.
            - **init\_fn** – Name of the init function of the driver.
            - **pm\_device** – PM device resources reference (NULL if device does not use PM).
            - **data\_ptr** – Pointer to the device’s private data.
            - **cfg\_ptr** – The address to the structure containing the configuration information for this instance of the driver.
            - **level** – The initialization level. See SYS\_INIT() for details.
            - **prio** – Priority within the selected initialization level. See SYS\_INIT() for details.
            - **api\_ptr** – Provides an initial pointer to the API function struct used by the driver. Can be NULL.

    SENSING\_SENSORS\_DT\_INST\_DEFINE(inst, ...)
    :   Like [SENSING\_SENSORS\_DT\_DEFINE()](#group__sensing__sensor_1gad5a9ccb04d96efc57078e880ca28b654) for an instance of a DT\_DRV\_COMPAT compatible.

        Parameters:
        :   - **inst** – instance number. This is replaced by `DT_DRV_COMPAT(inst)` in the call to [SENSING\_SENSORS\_DT\_DEFINE()](#group__sensing__sensor_1gad5a9ccb04d96efc57078e880ca28b654).
            - **...** – other parameters as expected by [SENSING\_SENSORS\_DT\_DEFINE()](#group__sensing__sensor_1gad5a9ccb04d96efc57078e880ca28b654).

    Functions

    int sensing\_sensor\_get\_reporters(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int type, [sensing\_sensor\_handle\_t](#c.sensing_sensor_handle_t) \*reporter\_handles, int max\_handles)
    :   Get reporter handles of a given sensor instance by sensor type.

        Parameters:
        :   - **dev** – The sensor instance device structure.
            - **type** – The given type, [SENSING\_SENSOR\_TYPE\_ALL](#group__sensing__sensor__types_1ga9f6bc03e84167bf0b1ae8ea4fe016223) to get reporters with all types.
            - **max\_handles** – The max count of the `reporter_handles` array input. Can get real count number via [sensing\_sensor\_get\_reporters\_count](#group__sensing__sensor_1ga2c5cfb298b2dfde967edfdd987115021)
            - **reporter\_handles** – Input handles array for receiving found reporter sensor instances

        Returns:
        :   number of reporters found, 0 returned if not found.

    int sensing\_sensor\_get\_reporters\_count(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int type)
    :   Get reporters count of a given sensor instance by sensor type.

        Parameters:
        :   - **dev** – The sensor instance device structure.
            - **type** – The sensor type for checking, [SENSING\_SENSOR\_TYPE\_ALL](#group__sensing__sensor__types_1ga9f6bc03e84167bf0b1ae8ea4fe016223)

        Returns:
        :   Count of reporters by `type`, 0 returned if no reporters by `type`.

    int sensing\_sensor\_get\_state(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [sensing\_sensor\_state](#c.sensing_sensor_state) \*state)
    :   Get this sensor’s state.

        Parameters:
        :   - **dev** – The sensor instance device structure.
            - **state** – Returned sensor state value

        Returns:
        :   0 on success or negative error value on failure.

    struct sensing\_sensor\_register\_info
    :   *#include <sensing\_sensor.h>*

        Sensor registration information.

        Public Members

        uint16\_t flags
        :   Sensor flags.

        uint16\_t sample\_size
        :   Sample size in bytes for a single sample of the registered sensor.

            sensing runtime need this information for internal buffer allocation.

        uint8\_t sensitivity\_count
        :   The number of sensor sensitivities.

        struct [sensing\_sensor\_version](#c.sensing_sensor_version) version
        :   Sensor version.

            Version can be used to identify different versions of sensor implementation.
