---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/mspi.html
original_path: hardware/peripherals/mspi.html
---

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
   The usual device defining macros such as [`DEVICE_DT_INST_DEFINE`](../../doxygen/html/group__device__model.md#gada5ba4aca9e0662ccebb2232c7256419)
   can be used, and the initialization function, config and data provided
   as a parameter to the macro.
2. Initialize the hardware, including but not limited to:

   - Check [`mspi_cfg`](../../doxygen/html/structmspi__cfg.md) against hardware’s own capabilities to prevent
     incorrect usages.
   - Setup default pinmux.
   - Setup the clock for the controller.
   - Power on the hardware.
   - Configure the hardware using [`mspi_cfg`](../../doxygen/html/structmspi__cfg.md) and possibly more
     platform specific settings.
   - Usually, the [`mspi_cfg`](../../doxygen/html/structmspi__cfg.md) is filled from device tree and contains
     static, boot time parameters. However, if needed, one can use [`mspi_config()`](../../doxygen/html/group__mspi__configure__api.md#ga46c2b98e99ecea045c1ecac4bdf3f087)
     to re-initialize the hardware with new parameters during runtime.
   - Release any lock if applicable.
3. Perform device driver initialization. As usually, [`DEVICE_DT_INST_DEFINE`](../../doxygen/html/group__device__model.md#gada5ba4aca9e0662ccebb2232c7256419)
   can be used. Inside device driver initialization function, perform the following
   required steps.

   1. Call [`mspi_dev_config()`](../../doxygen/html/group__mspi__configure__api.md#gaa3c1eae8b3000c9bafcc26f14a8beb8b) with device specific hardware settings obtained
      from device datasheets.

      - The [`mspi_dev_cfg`](../../doxygen/html/structmspi__dev__cfg.md) should be filled by device tree and helper macro
        [`MSPI_DEVICE_CONFIG_DT`](../../doxygen/html/group__mspi__devicetree.md#gaa8e730d85dede3d1e5dc9f69f30098b2) can be used.
      - The controller driver should then validate the members of [`mspi_dev_cfg`](../../doxygen/html/structmspi__dev__cfg.md)
        to prevent incorrect usage.
      - The controller driver should implement a mutex to protect from accidental access.
      - The controller driver may also switch between different devices based on
        [`mspi_dev_id`](../../doxygen/html/structmspi__dev__id.md).
   2. Call API for additional setups if supported by hardware

      - [`mspi_xip_config()`](../../doxygen/html/group__mspi__configure__api.md#gab9d9104636d3c8167b5876b1bc4348ea) for [XIP](../../glossary.md#term-XIP) feature
      - [`mspi_scramble_config()`](../../doxygen/html/group__mspi__configure__api.md#gacf287e08b6ce4898524884e8de22b806) for scrambling feature
      - [`mspi_timing_config()`](../../doxygen/html/group__mspi__configure__api.md#gaff82af1cfc99b9e78cec17ea27f79ab6) for platform specific timing setup.
   3. Register any callback with [`mspi_register_callback()`](../../doxygen/html/group__mspi__callback__api.md#ga967f5fed63f08ac2d5a88625b030cd14) if needed.
   4. Release the controller mutex lock.

### [Transceive](#id3)

The transceive request is of type [`mspi_xfer`](../../doxygen/html/structmspi__xfer.md) which allows dynamic change to
the transfer related settings once the mode of operation is determined and configured
by [`mspi_dev_config()`](../../doxygen/html/group__mspi__configure__api.md#gaa3c1eae8b3000c9bafcc26f14a8beb8b).

The API also supports bulk transfers with different starting addresses and sizes with
[`mspi_xfer_packet`](../../doxygen/html/structmspi__xfer__packet.md). However, it is up to the controller implementation
whether to support scatter IO and callback management. The controller can determine
which user callback to trigger based on [`mspi_bus_event_cb_mask`](../../doxygen/html/group__mspi__interface.md#gab33e9840b0937c944f4e1a2525534cb1) upon completion
of each async/sync transfer if the callback had been registered using
[`mspi_register_callback()`](../../doxygen/html/group__mspi__callback__api.md#ga967f5fed63f08ac2d5a88625b030cd14). Or not to trigger any callback at all with
`MSPI_BUS_NO_CB` even if the callbacks are already registered.
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

With [`mspi_dev_id`](../../doxygen/html/structmspi__dev__id.md) defined as collection of the device index and CE GPIO from
device tree, the API supports multiple devices on the same controller instance.
The controller driver implementation may or may not support device switching,
which can be performed either by software or by hardware. If the switching is handled
by software, it should be performed in [`mspi_dev_config()`](../../doxygen/html/group__mspi__configure__api.md#gaa3c1eae8b3000c9bafcc26f14a8beb8b) call.

The device driver should record the current operating conditions of the device to support
software controlled device switching by saving and updating [`mspi_dev_cfg`](../../doxygen/html/structmspi__dev__cfg.md) and
other relevant mspi struct or private data structures. In particular, [`mspi_dev_id`](../../doxygen/html/structmspi__dev__id.md)
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

[MSPI Driver APIs](../../doxygen/html/group__mspi__interface.md)

Related code samples

- [MSPI asynchronous transfer](../../samples/drivers/mspi/mspi_async/README.md#mspi-async "Use the MSPI API to interact with MSPI memory device asynchronously.")Use the MSPI API to interact with MSPI memory device asynchronously.
