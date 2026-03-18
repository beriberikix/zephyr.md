---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/mspi.html
original_path: hardware/peripherals/mspi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Multi-bit SPI Bus

The MSPI (multi-bit SPI) is provided as a generic API to accommodate
advanced SPI peripherals and devices that typically require command,
address and data phases, and multiple signal lines during these phases.
While the API supports advanced features such as [XIP](../../glossary.md#term-XIP) and scrambling,
it is also compatible with generic SPI.

## [MSPI Controller API](#id2)

Zephyr’s MSPI controller API may be used when a multi-bit SPI controller
is present. E.g. Ambiq MSPI, QSPI, OSPI, Flexspi, etc.
The API supports single to hex SDR/DDR IO with variable latency and advanced
features such as [XIP](../../glossary.md#term-XIP) and scrambling. Applicable devices include but
not limited to high-speed, high density flash/psram memory devices, displays
and sensors.

The MSPI interface contains controller drivers that are SoC platform specific
and implement the MSPI APIs, and device drivers that reference these APIs.
The relationship between the controller and device drivers is many-to-many to
allow for easy switching between platforms.

Here is a list of generic steps for initializing the MSPI controller and the
MSPI bus inside the device driver initialization function:

1. Initialize the data structure of the MSPI controller driver instance.
   The usual device defining macros such as [`DEVICE_DT_INST_DEFINE`](../../kernel/drivers/index.md#c.DEVICE_DT_INST_DEFINE "DEVICE_DT_INST_DEFINE")
   can be used, and the initialization function, config and data provided
   as a parameter to the macro.
2. Initialize the hardware, including but not limited to:

   - Check `mspi_cfg` against hardware’s own capabilities to prevent
     incorrect usages.
   - Setup default pinmux.
   - Setup the clock for the controller.
   - Power on the hardware.
   - Configure the hardware using `mspi_cfg` and possibly more
     platform specific settings.
   - Usually, the `mspi_cfg` is filled from device tree and contains
     static, boot time parameters. However, if needed, one can use `mspi_config()`
     to re-initialize the hardware with new parameters during runtime.
   - Release any lock if applicable.
3. Perform device driver initialization. As usually, [`DEVICE_DT_INST_DEFINE`](../../kernel/drivers/index.md#c.DEVICE_DT_INST_DEFINE "DEVICE_DT_INST_DEFINE")
   can be used. Inside device driver initialization function, perform the following
   required steps.

   1. Call `mspi_dev_config()` with device specific hardware settings obtained
      from device datasheets.

      - The `mspi_dev_cfg` should be filled by device tree and helper macro
        `MSPI_DEVICE_CONFIG_DT` can be used.
      - The controller driver should then validate the members of `mspi_dev_cfg`
        to prevent incorrect usage.
      - The controller driver should implement a mutex to protect from accidental access.
      - The controller driver may also switch between different devices based on
        `mspi_dev_id`.
   2. Call API for additional setups if supported by hardware

      - `mspi_xip_config()` for [XIP](../../glossary.md#term-XIP) feature
      - `mspi_scramble_config()` for scrambling feature
      - `mspi_timing_config()` for platform specific timing setup.
   3. Register any callback with `mspi_register_callback()` if needed.
   4. Release the controller mutex lock.

### [Transceive](#id3)

The transceive request is of type `mspi_xfer` which allows dynamic change to
the transfer related settings once the mode of operation is determined and configured
by `mspi_dev_config()`.

The API also supports bulk transfers with different starting addresses and sizes with
`mspi_xfer_packet`. However, it is up to the controller implementation
whether to support scatter IO and callback management. The controller can determine
which user callback to trigger based on [`mspi_bus_event_cb_mask`](#c.mspi_bus_event_cb_mask) upon completion
of each async/sync transfer if the callback had been registered using
`mspi_register_callback()`. Or not to trigger any callback at all with
[`MSPI_BUS_NO_CB`](#c.mspi_bus_event_cb_mask.MSPI_BUS_NO_CB) even if the callbacks are already registered.
In which case that a controller supports hardware command queue, user could take full
advantage of the hardware performance if scatter IO and callback management are supported
by the driver implementation.

### [Device Tree](#id4)

Here is an example for defining an MSPI controller in device tree:
The mspi controller’s bindings should reference mspi-controller.yaml as one of the base.

```devicetree
mspi0: mspi@400 {
         status = "okay";
         compatible = "zephyr,mspi-emul-controller";

         reg = < 0x400 0x4 >;
         #address-cells = < 0x1 >;
         #size-cells = < 0x0 >;

         clock-frequency = < 0x17d7840 >;
         op-mode = "MSPI_CONTROLLER";
         duplex = "MSPI_HALF_DUPLEX";
         ce-gpios = < &gpio0 0x5 0x1 >, < &gpio0 0x12 0x1 >;
         dqs-support;

         pinctrl-0 = < &pinmux-mspi0 >;
         pinctrl-names = "default";
};
```

Here is an example for defining an MSPI device in device tree:
The mspi device’s bindings should reference mspi-device.yaml as one of the base.

```devicetree
&mspi0 {

         mspi_dev0: mspi_dev0@0 {
                  status = "okay";
                  compatible = "zephyr,mspi-emul-device";

                  reg = < 0x0 >;
                  size = < 0x10000 >;

                  mspi-max-frequency = < 0x2dc6c00 >;
                  mspi-io-mode = "MSPI_IO_MODE_QUAD";
                  mspi-data-rate = "MSPI_DATA_RATE_SINGLE";
                  mspi-hardware-ce-num = < 0x0 >;
                  read-instruction = < 0xb >;
                  write-instruction = < 0x2 >;
                  instruction-length = "INSTR_1_BYTE";
                  address-length = "ADDR_4_BYTE";
                  rx-dummy = < 0x8 >;
                  tx-dummy = < 0x0 >;
                  xip-config = < 0x0 0x0 0x0 0x0 >;
                  ce-break-config = < 0x0 0x0 >;
         };

};
```

User should specify target operating parameters in the DTS such as `mspi-max-frequency`,
`mspi-io-mode` and `mspi-data-rate` even though they may subject to change during runtime.
It should represent the typical configuration of the device during normal operations.

### [Multi Peripheral](#id5)

With `mspi_dev_id` defined as collection of the device index and CE GPIO from
device tree, the API supports multiple devices on the same controller instance.
The controller driver implementation may or may not support device switching,
which can be performed either by software or by hardware. If the switching is handled
by software, it should be performed in `mspi_dev_config()` call.

The device driver should record the current operating conditions of the device to support
software controlled device switching by saving and updating `mspi_dev_cfg` and
other relevant mspi struct or private data structures. In particular, `mspi_dev_id`
which contains the identity of the device needs to be used for every API call.

## [Configuration Options](#id6)

Related configuration options:

- [`CONFIG_MSPI`](../../kconfig.md#CONFIG_MSPI "CONFIG_MSPI")
- [`CONFIG_MSPI_ASYNC`](../../kconfig.md#CONFIG_MSPI_ASYNC "CONFIG_MSPI_ASYNC")
- [`CONFIG_MSPI_PERIPHERAL`](../../kconfig.md#CONFIG_MSPI_PERIPHERAL "CONFIG_MSPI_PERIPHERAL")
- [`CONFIG_MSPI_XIP`](../../kconfig.md#CONFIG_MSPI_XIP "CONFIG_MSPI_XIP")
- [`CONFIG_MSPI_SCRAMBLE`](../../kconfig.md#CONFIG_MSPI_SCRAMBLE "CONFIG_MSPI_SCRAMBLE")
- [`CONFIG_MSPI_TIMING`](../../kconfig.md#CONFIG_MSPI_TIMING "CONFIG_MSPI_TIMING")
- [`CONFIG_MSPI_INIT_PRIORITY`](../../kconfig.md#CONFIG_MSPI_INIT_PRIORITY "CONFIG_MSPI_INIT_PRIORITY")
- [`CONFIG_MSPI_COMPLETION_TIMEOUT_TOLERANCE`](../../kconfig.md#CONFIG_MSPI_COMPLETION_TIMEOUT_TOLERANCE "CONFIG_MSPI_COMPLETION_TIMEOUT_TOLERANCE")

## [API Reference](#id7)

Related code samples

[MSPI asynchronous transfer](../../samples/drivers/mspi/mspi_async/README.md#mspi-async "Use the MSPI API to interact with MSPI memory device asynchronously.")
:   Use the MSPI API to interact with MSPI memory device asynchronously.

*group* MSPI Driver APIs
:   MSPI Driver APIs.

    Typedefs

    typedef int (\*mspi\_api\_config)(const struct mspi\_dt\_spec \*spec)
    :   MSPI driver API definition and system call entry points.

    typedef int (\*mspi\_api\_dev\_config)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*controller, const struct mspi\_dev\_id \*dev\_id, const enum [mspi\_dev\_cfg\_mask](#c.mspi_dev_cfg_mask) param\_mask, const struct mspi\_dev\_cfg \*cfg)

    typedef int (\*mspi\_api\_get\_channel\_status)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*controller, uint8\_t ch)

    typedef int (\*mspi\_api\_transceive)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*controller, const struct mspi\_dev\_id \*dev\_id, const struct mspi\_xfer \*req)

    typedef int (\*mspi\_api\_register\_callback)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*controller, const struct mspi\_dev\_id \*dev\_id, const enum [mspi\_bus\_event](#c.mspi_bus_event) evt\_type, mspi\_callback\_handler\_t cb, struct mspi\_callback\_context \*ctx)

    typedef int (\*mspi\_api\_xip\_config)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*controller, const struct mspi\_dev\_id \*dev\_id, const struct mspi\_xip\_cfg \*xip\_cfg)

    typedef int (\*mspi\_api\_scramble\_config)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*controller, const struct mspi\_dev\_id \*dev\_id, const struct mspi\_scramble\_cfg \*scramble\_cfg)

    typedef int (\*mspi\_api\_timing\_config)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*controller, const struct mspi\_dev\_id \*dev\_id, const uint32\_t param\_mask, void \*timing\_cfg)

    Enums

    enum mspi\_op\_mode
    :   MSPI operational mode.

        *Values:*

        enumerator MSPI\_OP\_MODE\_CONTROLLER = 0

        enumerator MSPI\_OP\_MODE\_PERIPHERAL = 1

    enum mspi\_duplex
    :   MSPI duplex mode.

        *Values:*

        enumerator MSPI\_HALF\_DUPLEX = 0

        enumerator MSPI\_FULL\_DUPLEX = 1

    enum mspi\_io\_mode
    :   MSPI I/O mode capabilities Postfix like 1\_4\_4 stands for the number of lines used for command, address and data phases.

        Mode with no postfix has the same number of lines for all phases.

        *Values:*

        enumerator MSPI\_IO\_MODE\_SINGLE = 0

        enumerator MSPI\_IO\_MODE\_DUAL = 1

        enumerator MSPI\_IO\_MODE\_DUAL\_1\_1\_2 = 2

        enumerator MSPI\_IO\_MODE\_DUAL\_1\_2\_2 = 3

        enumerator MSPI\_IO\_MODE\_QUAD = 4

        enumerator MSPI\_IO\_MODE\_QUAD\_1\_1\_4 = 5

        enumerator MSPI\_IO\_MODE\_QUAD\_1\_4\_4 = 6

        enumerator MSPI\_IO\_MODE\_OCTAL = 7

        enumerator MSPI\_IO\_MODE\_OCTAL\_1\_1\_8 = 8

        enumerator MSPI\_IO\_MODE\_OCTAL\_1\_8\_8 = 9

        enumerator MSPI\_IO\_MODE\_HEX = 10

        enumerator MSPI\_IO\_MODE\_HEX\_8\_8\_16 = 11

        enumerator MSPI\_IO\_MODE\_HEX\_8\_16\_16 = 12

        enumerator MSPI\_IO\_MODE\_MAX

    enum mspi\_data\_rate
    :   MSPI data rate capabilities SINGLE stands for single data rate for all phases.

        DUAL stands for dual data rate for all phases. S\_S\_D stands for single data rate for command and address phases but dual data rate for data phase. S\_D\_D stands for single data rate for command phase but dual data rate for address and data phases.

        *Values:*

        enumerator MSPI\_DATA\_RATE\_SINGLE = 0

        enumerator MSPI\_DATA\_RATE\_S\_S\_D = 1

        enumerator MSPI\_DATA\_RATE\_S\_D\_D = 2

        enumerator MSPI\_DATA\_RATE\_DUAL = 3

        enumerator MSPI\_DATA\_RATE\_MAX

    enum mspi\_cpp\_mode
    :   MSPI Polarity & Phase Modes.

        *Values:*

        enumerator MSPI\_CPP\_MODE\_0 = 0

        enumerator MSPI\_CPP\_MODE\_1 = 1

        enumerator MSPI\_CPP\_MODE\_2 = 2

        enumerator MSPI\_CPP\_MODE\_3 = 3

    enum mspi\_endian
    :   MSPI Endian.

        *Values:*

        enumerator MSPI\_XFER\_LITTLE\_ENDIAN = 0

        enumerator MSPI\_XFER\_BIG\_ENDIAN = 1

    enum mspi\_ce\_polarity
    :   MSPI chip enable polarity.

        *Values:*

        enumerator MSPI\_CE\_ACTIVE\_LOW = 0

        enumerator MSPI\_CE\_ACTIVE\_HIGH = 1

    enum mspi\_bus\_event
    :   MSPI bus event.

        This is a preliminary list of events. I encourage the community to fill it up.

        *Values:*

        enumerator MSPI\_BUS\_RESET = 0

        enumerator MSPI\_BUS\_ERROR = 1

        enumerator MSPI\_BUS\_XFER\_COMPLETE = 2

        enumerator MSPI\_BUS\_EVENT\_MAX

    enum mspi\_bus\_event\_cb\_mask
    :   MSPI bus event callback mask This is a preliminary list same as [mspi\_bus\_event](#group__mspi__interface_1ga4cd05950729893e08ef0d4a12e2242d5).

        I encourage the community to fill it up.

        *Values:*

        enumerator MSPI\_BUS\_NO\_CB = 0

        enumerator MSPI\_BUS\_RESET\_CB = [BIT](../../kernel/util/index.md#c.BIT "BIT")(0)

        enumerator MSPI\_BUS\_ERROR\_CB = [BIT](../../kernel/util/index.md#c.BIT "BIT")(1)

        enumerator MSPI\_BUS\_XFER\_COMPLETE\_CB = [BIT](../../kernel/util/index.md#c.BIT "BIT")(2)

    enum mspi\_xfer\_mode
    :   MSPI transfer modes.

        *Values:*

        enumerator MSPI\_PIO

        enumerator MSPI\_DMA

    enum mspi\_xfer\_direction
    :   MSPI transfer directions.

        *Values:*

        enumerator MSPI\_RX

        enumerator MSPI\_TX

    enum mspi\_dev\_cfg\_mask
    :   MSPI controller device specific configuration mask.

        *Values:*

        enumerator MSPI\_DEVICE\_CONFIG\_NONE = 0

        enumerator MSPI\_DEVICE\_CONFIG\_CE\_NUM = [BIT](../../kernel/util/index.md#c.BIT "BIT")(0)

        enumerator MSPI\_DEVICE\_CONFIG\_FREQUENCY = [BIT](../../kernel/util/index.md#c.BIT "BIT")(1)

        enumerator MSPI\_DEVICE\_CONFIG\_IO\_MODE = [BIT](../../kernel/util/index.md#c.BIT "BIT")(2)

        enumerator MSPI\_DEVICE\_CONFIG\_DATA\_RATE = [BIT](../../kernel/util/index.md#c.BIT "BIT")(3)

        enumerator MSPI\_DEVICE\_CONFIG\_CPP = [BIT](../../kernel/util/index.md#c.BIT "BIT")(4)

        enumerator MSPI\_DEVICE\_CONFIG\_ENDIAN = [BIT](../../kernel/util/index.md#c.BIT "BIT")(5)

        enumerator MSPI\_DEVICE\_CONFIG\_CE\_POL = [BIT](../../kernel/util/index.md#c.BIT "BIT")(6)

        enumerator MSPI\_DEVICE\_CONFIG\_DQS = [BIT](../../kernel/util/index.md#c.BIT "BIT")(7)

        enumerator MSPI\_DEVICE\_CONFIG\_RX\_DUMMY = [BIT](../../kernel/util/index.md#c.BIT "BIT")(8)

        enumerator MSPI\_DEVICE\_CONFIG\_TX\_DUMMY = [BIT](../../kernel/util/index.md#c.BIT "BIT")(9)

        enumerator MSPI\_DEVICE\_CONFIG\_READ\_CMD = [BIT](../../kernel/util/index.md#c.BIT "BIT")(10)

        enumerator MSPI\_DEVICE\_CONFIG\_WRITE\_CMD = [BIT](../../kernel/util/index.md#c.BIT "BIT")(11)

        enumerator MSPI\_DEVICE\_CONFIG\_CMD\_LEN = [BIT](../../kernel/util/index.md#c.BIT "BIT")(12)

        enumerator MSPI\_DEVICE\_CONFIG\_ADDR\_LEN = [BIT](../../kernel/util/index.md#c.BIT "BIT")(13)

        enumerator MSPI\_DEVICE\_CONFIG\_MEM\_BOUND = [BIT](../../kernel/util/index.md#c.BIT "BIT")(14)

        enumerator MSPI\_DEVICE\_CONFIG\_BREAK\_TIME = [BIT](../../kernel/util/index.md#c.BIT "BIT")(15)

        enumerator MSPI\_DEVICE\_CONFIG\_ALL = [BIT\_MASK](../../kernel/util/index.md#c.BIT_MASK "BIT_MASK")(16)

    enum mspi\_xip\_permit
    :   MSPI XIP access permissions.

        *Values:*

        enumerator MSPI\_XIP\_READ\_WRITE = 0

        enumerator MSPI\_XIP\_READ\_ONLY = 1

    struct mspi\_driver\_api
    :   *#include <mspi.h>*
