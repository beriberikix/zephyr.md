---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/releases/migration-guide-3.6.html
original_path: releases/migration-guide-3.6.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Migration guide to Zephyr v3.6.0

This document describes the changes required when migrating your application from Zephyr v3.5.0 to
Zephyr v3.6.0.

Any other changes (not directly related to migrating applications) can be found in
the [release notes](release-notes-3.6.md#zephyr-3-6).

## [Build System](#id1)

- The deprecated `prj_<board>.conf` Kconfig file support has been removed, projects that use
  this should switch to using board Kconfig fragments instead (`boards/<board>.conf`).
- Until now `_POSIX_C_SOURCE`, `_XOPEN_SOURCE`, and `_XOPEN_SOURCE_EXTENDED` were defined
  globally when building for the native (`ARCH_POSIX`) targets, and `_POSIX_C_SOURCE` when
  building with PicolibC. Since this release, these are set only for the files that need them.
  If your library or application needed this, you may start getting an “implicit declaration”
  warning for functions whose prototypes are only exposed if one of these is defined.
  If so, you can fix it by defining the corresponding macro in your C source file before any
  include, or by adding the equivalent of
  `target_compile_definitions(app PRIVATE _POSIX_C_SOURCE=200809L)` to your application
  or `zephyr_library_compile_definitions(_POSIX_C_SOURCE=200809L)` to your library.
- Build type by setting `CONF_FILE` to `prj_<build>.conf` is now deprecated, users should
  instead use the new `-DFILE_SUFFIX` feature [File Suffixes](../develop/application/index.md#application-file-suffixes).

## [Kernel](#id2)

- The system heap size and its availability is now determined by a `K_HEAP_MEM_POOL_SIZE`
  define instead of the [`CONFIG_HEAP_MEM_POOL_SIZE`](../kconfig.md#CONFIG_HEAP_MEM_POOL_SIZE "CONFIG_HEAP_MEM_POOL_SIZE") Kconfig option. Subsystems
  can specify their own custom system heap size requirements by specifying Kconfig options with
  the prefix `CONFIG_HEAP_MEM_POOL_ADD_SIZE_`. The old Kconfig option still exists, but will be
  overridden if the custom requirements are larger. To force the old Kconfig option to be used,
  even when its value is less than the indicated custom requirements, a new
  [`CONFIG_HEAP_MEM_POOL_IGNORE_MIN`](../kconfig.md#CONFIG_HEAP_MEM_POOL_IGNORE_MIN "CONFIG_HEAP_MEM_POOL_IGNORE_MIN") option has been introduced (which defaults
  being disabled).

## [Boards](#id3)

- The deprecated Nordic SoC Kconfig option `NRF_STORE_REBOOT_TYPE_GPREGRET` has been removed,
  applications that use this should switch to using the [Boot mode](../services/retention/index.md#boot-mode-api) instead.
- NXP: Enabled [linkserver](../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) to be the default runner on the
  following NXP boards: `mimxrt685_evk_cm33`, `frdm_k64f`, `mimxrt1050_evk`, `frdm_kl25z`,
  `mimxrt1020_evk`, `mimxrt1015_evk`

## [Modules](#id4)

### [Optional Modules](#id5)

The following modules have been made optional and are not downloaded with west update by default
anymore:

- `canopennode` ([GitHub #64139](https://github.com/zephyrproject-rtos/zephyr/issues/64139))

To enable them again use the `west config manifest.project-filter -- +<module
name>` command, or `west config manifest.group-filter -- +optional` to
enable all optional modules, and then run `west update` again.

### [MCUboot](#id6)

- MCUboot’s deprecated `CONFIG_ZEPHYR_TRY_MASS_ERASE` Kconfig option has been removed. If an
  erase is needed when flashing MCUboot, this should now be provided directly to the `west`
  command e.g. `west flash --erase`. ([GitHub #64703](https://github.com/zephyrproject-rtos/zephyr/issues/64703))

### [zcbor](#id7)

- If you have zcbor-generated code that relies on the zcbor libraries through Zephyr, you must
  regenerate the files using zcbor 0.8.1. Note that the names of generated types and members has
  been overhauled, so the code using the generated code must likely be changed.
  For example:

  - Leading single underscores and all double underscores are largely gone,
  - Names sometimes gain suffixes like `_m` or `_l` for disambiguation.
  - All enum (choice) names have now gained a `_c` suffix, so the enum name no longer matches
    the corresponding member name exactly (because this broke C++ namespace rules).
- The function `zcbor_new_state()`, `zcbor_new_decode_state()` and the macro
  `ZCBOR_STATE_D` have gained new parameters related to decoding of unordered maps.
  Unless you are using that new functionality, these can all be set to NULL or 0.
- The functions `zcbor_bstr_put_term()` and `zcbor_tstr_put_term()` have gained a new
  parameter `maxlen`, referring to the maximum length of the parameter `str`.
  This parameter is passed directly to `strnlen()` under the hood.
- The function `zcbor_tag_encode()` has been renamed to `zcbor_tag_put()`.
- Printing has been changed significantly, e.g. `zcbor_print()` is now called
  `zcbor_log()`, and `zcbor_trace()` with no parameters is gone, and in its place are
  `zcbor_trace_file()` and `zcbor_trace()`, both of which take a `state` parameter.

## [Device Drivers and Devicetree](#id8)

### [Devicetree Labels](#id9)

- Various deprecated macros related to the deprecated devicetree label property
  were removed. These are listed in the following table. The table also
  provides replacements.

  However, if you are still using code like
  `device_get_binding(DT_LABEL(node_id))`, consider replacing it with
  something like `DEVICE_DT_GET(node_id)` instead. The `DEVICE_DT_GET()`
  macro avoids run-time string comparisons, and is also safer because it will
  fail the build if the device does not exist.

  | Removed macro | Replacement |
  | --- | --- |
  | `DT_GPIO_LABEL(node_id, gpio_pha)` | `DT_PROP(DT_GPIO_CTLR(node_id, gpio_pha), label)` |
  | `DT_GPIO_LABEL_BY_IDX(node_id, gpio_pha, idx)` | `DT_PROP(DT_GPIO_CTLR_BY_IDX(node_id, gpio_pha, idx), label)` |
  | `DT_INST_GPIO_LABEL(inst, gpio_pha)` | `DT_PROP(DT_GPIO_CTLR(DT_DRV_INST(inst), gpio_pha), label)` |
  | `DT_INST_GPIO_LABEL_BY_IDX(inst, gpio_pha, idx)` | `DT_PROP(DT_GPIO_CTLR_BY_IDX(DT_DRV_INST(inst), gpio_pha, idx), label)` |
  | `DT_SPI_DEV_CS_GPIOS_LABEL(spi_dev)` | `DT_PROP(DT_SPI_DEV_CS_GPIOS_CTLR(spi_dev), label)` |
  | `DT_INST_SPI_DEV_CS_GPIOS_LABEL(inst)` | `DT_PROP(DT_SPI_DEV_CS_GPIOS_CTLR(DT_DRV_INST(inst)), label)` |
  | `DT_LABEL(node_id)` | `DT_PROP(node_id, label)` |
  | `DT_BUS_LABEL(node_id)` | `DT_PROP(DT_BUS(node_id), label)` |
  | `DT_INST_LABEL(inst)` | `DT_INST_PROP(inst, label)` |
  | `DT_INST_BUS_LABEL(inst)` | `DT_PROP(DT_BUS(DT_DRV_INST(inst)), label)` |

### [Multi-level Interrupts](#id10)

- For platforms that enabled [`CONFIG_MULTI_LEVEL_INTERRUPTS`](../kconfig.md#CONFIG_MULTI_LEVEL_INTERRUPTS "CONFIG_MULTI_LEVEL_INTERRUPTS"), the `IRQ` variant
  of the Devicetree macros now return the as-seen value in the devicetree instead of the Zephyr
  multilevel-encoded IRQ number. To get the IRQ number in Zephyr multilevel-encoded format, use
  `IRQN` variant instead. For example, consider the following devicetree:

  ```devicetree
  plic: interrupt-controller@c000000 {
          riscv,max-priority = <7>;
          riscv,ndev = <1024>;
          reg = <0x0c000000 0x04000000>;
          interrupts-extended = <&hlic0 11>;
          interrupt-controller;
          compatible = "sifive,plic-1.0.0";
          #address-cells = <0x0>;
          #interrupt-cells = <0x2>;
  };

  uart0: uart@10000000 {
          interrupts = <10 1>;
          interrupt-parent = <&plic>;
          clock-frequency = <0x384000>;
          reg = <0x10000000 0x100>;
          compatible = "ns16550";
          reg-shift = <0>;
  };
  ```

  `plic` is a second level interrupt aggregator and `uart0` is a child of `plic`.
  `DT_IRQ_BY_IDX(DT_NODELABEL(uart0), 0, irq)` will return `10`
  (as-seen value in the devicetree), while `DT_IRQN_BY_IDX(DT_NODELABEL(uart0), 0)` will return
  `(((10 + 1) << CONFIG_1ST_LEVEL_INTERRUPT_BITS) | 11)`.

  Drivers and applications that are supposed to work in multilevel-interrupt configurations should
  be updated to use the `IRQN` variant, i.e.:

  - `DT_IRQ(node_id, irq)` -> `DT_IRQN(node_id)`
  - `DT_IRQ_BY_IDX(node_id, idx, irq)` -> `DT_IRQN_BY_IDX(node_id, idx)`
  - `DT_IRQ_BY_NAME(node_id, name, irq)` -> `DT_IRQN_BY_NAME(node_id, name)`
  - `DT_INST_IRQ(inst, irq)` -> `DT_INST_IRQN(inst)`
  - `DT_INST_IRQ_BY_IDX(inst, idx, irq)` -> `DT_INST_IRQN_BY_IDX(inst, idx)`
  - `DT_INST_IRQ_BY_NAME(inst, name, irq)` -> `DT_INST_IRQN_BY_NAME(inst, name)`

### [Analog-to-Digital Converter (ADC)](#id11)

- The io-channel cells of the following devicetree bindings were reduced from 2 (`positive` and
  `negative`) to the common `input`, making it possible to use the various ADC DT macros with TI
  LMP90xxx ADC devices:

  - [`ti,lmp90077`](../build/dts/api/bindings/adc/ti%2Clmp90077.md#std-dtcompatible-ti-lmp90077)
  - [`ti,lmp90078`](../build/dts/api/bindings/adc/ti%2Clmp90078.md#std-dtcompatible-ti-lmp90078)
  - [`ti,lmp90079`](../build/dts/api/bindings/adc/ti%2Clmp90079.md#std-dtcompatible-ti-lmp90079)
  - [`ti,lmp90080`](../build/dts/api/bindings/adc/ti%2Clmp90080.md#std-dtcompatible-ti-lmp90080)
  - [`ti,lmp90097`](../build/dts/api/bindings/adc/ti%2Clmp90097.md#std-dtcompatible-ti-lmp90097)
  - [`ti,lmp90098`](../build/dts/api/bindings/adc/ti%2Clmp90098.md#std-dtcompatible-ti-lmp90098)
  - [`ti,lmp90099`](../build/dts/api/bindings/adc/ti%2Clmp90099.md#std-dtcompatible-ti-lmp90099)
  - [`ti,lmp90100`](../build/dts/api/bindings/adc/ti%2Clmp90100.md#std-dtcompatible-ti-lmp90100)
- The io-channel cells of the [`microchip,mcp3204`](../build/dts/api/bindings/adc/microchip%2Cmcp3204.md#std-dtcompatible-microchip-mcp3204) and
  [`microchip,mcp3208`](../build/dts/api/bindings/adc/microchip%2Cmcp3208.md#std-dtcompatible-microchip-mcp3208) devicetree bindings were renamed from `channel` to the common
  `input`, making it possible to use the various ADC DT macros with Microchip MCP320x ADC devices.

### [Bluetooth HCI](#id12)

- The optional `setup()` function in the Bluetooth HCI driver API (enabled through
  [`CONFIG_BT_HCI_SETUP`](../kconfig.md#CONFIG_BT_HCI_SETUP "CONFIG_BT_HCI_SETUP")) has gained a function parameter of type
  [`bt_hci_setup_params`](../connectivity/bluetooth/api/hci_drivers.md#c.bt_hci_setup_params "bt_hci_setup_params"). By default, the struct is empty, but drivers can opt-in to
  [`CONFIG_BT_HCI_SET_PUBLIC_ADDR`](../kconfig.md#CONFIG_BT_HCI_SET_PUBLIC_ADDR "CONFIG_BT_HCI_SET_PUBLIC_ADDR") if they support setting the controller’s public
  identity address, which will then be passed in the `public_addr` field.

  ([GitHub #62994](https://github.com/zephyrproject-rtos/zephyr/issues/62994))
- The [`st,hci-spi-v1`](../build/dts/api/bindings/bluetooth/st%2Chci-spi-v1.md#std-dtcompatible-st-hci-spi-v1) should be used instead of [`zephyr,bt-hci-spi`](../build/dts/api/bindings/bluetooth/zephyr%2Cbt-hci-spi.md#std-dtcompatible-zephyr-bt-hci-spi)
  for the boards which are based on ST BlueNRG-MS.

### [Controller Area Network (CAN)](#id13)

- The native Linux SocketCAN driver, which can now be used in both [native\_posix](../boards/posix/native_posix/doc/index.md#native-posix)
  and [native\_sim](../boards/posix/native_sim/doc/index.md#native-sim) with or without an embedded C-library, has been renamed to
  reflect this:

  - The devicetree compatible was renamed from `zephyr,native-posix-linux-can` to
    [`zephyr,native-linux-can`](../build/dts/api/bindings/can/zephyr%2Cnative-linux-can.md#std-dtcompatible-zephyr-native-linux-can).
  - The main Kconfig option was renamed from `CONFIG_CAN_NATIVE_POSIX_LINUX` to
    [`CONFIG_CAN_NATIVE_LINUX`](../kconfig.md#CONFIG_CAN_NATIVE_LINUX "CONFIG_CAN_NATIVE_LINUX").
- Two new structures for holding common CAN controller driver configuration (`struct
  can_driver_config`) and data (`struct can_driver_data`) fields were introduced. Out-of-tree CAN
  controller drivers need to be updated to use these new, common configuration and data structures
  along with their initializer macros.
- The optional `can_get_max_bitrate_t` CAN controller driver callback was removed in favor of a
  common accessor function. Out-of-tree CAN controller drivers need to be updated to no longer
  supply this callback.
- The CAN transceiver API function [`can_transceiver_enable()`](../hardware/peripherals/can/transceiver.md#c.can_transceiver_enable "can_transceiver_enable") now takes a [`can_mode_t`](../hardware/peripherals/can/controller.md#c.can_mode_t "can_mode_t")
  argument for propagating the CAN controller operational mode to the CAN transceiver. Out-of-tree
  CAN controller and CAN transceiver drivers need to be updated to match this new API function
  signature.
- The `CAN_FILTER_FDF` flag for filtering classic CAN/CAN FD frames was removed since no known CAN
  controllers implement support for this. Applications can still filter on classic CAN/CAN FD frames
  in their receive callback functions as needed.
- The `CAN_FILTER_DATA` and `CAN_FILTER_RTR` flags for filtering between Data and Remote
  Transmission Request (RTR) frames were removed since not all CAN controllers implement support for
  individual RX filtering based on the RTR bit. Applications can now use
  [`CONFIG_CAN_ACCEPT_RTR`](../kconfig.md#CONFIG_CAN_ACCEPT_RTR "CONFIG_CAN_ACCEPT_RTR") to either accept incoming RTR frames matching CAN filters
  or reject all incoming CAN RTR frames (the default). When [`CONFIG_CAN_ACCEPT_RTR`](../kconfig.md#CONFIG_CAN_ACCEPT_RTR "CONFIG_CAN_ACCEPT_RTR")
  is enabled, applications can still filter between Data and RTR frames in their receive callback
  functions as needed.
- The [`st,stm32h7-fdcan`](../build/dts/api/bindings/can/st%2Cstm32h7-fdcan.md#std-dtcompatible-st-stm32h7-fdcan) CAN controller driver now supports configuring the
  domain/kernel clock via devicetree. Previously, the driver only supported using the PLL1\_Q clock
  for kernel clock, but now it defaults to the HSE clock, which is the chip default. Boards that
  use the PLL1\_Q clock for FDCAN will need to override the `clocks` property as follows:

  ```devicetree
  &fdcan1 {
          clocks = <&rcc STM32_CLOCK_BUS_APB1_2 0x00000100>,
                   <&rcc STM32_SRC_PLL1_Q FDCAN_SEL(1)>;
  };
  ```

### [Display](#id14)

- ILI9XXX based displays now use the MIPI DBI driver class. These displays
  must now be declared within a MIPI DBI driver wrapper device, which will
  manage interfacing with the display. Note that the cmd-data-gpios pin has
  changed polarity with this update, to align better with the new
  dc-gpios name. For an example, see below:

  ```devicetree
  /* Legacy ILI9XXX display definition */
  &spi2 {
      ili9340: ili9340@0 {
          compatible = "ilitek,ili9340";
          reg = <0>;
          spi-max-frequency = <32000000>;
          reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
          cmd-data-gpios = <&gpio0 12 GPIO_ACTIVE_LOW>;
          rotation = <270>;
          width = <320>;
          height = <240>;
      };
  };

  /* New display definition with MIPI DBI device */

  mipi_dbi {
      compatible = "zephyr,mipi-dbi-spi";
      reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
      dc-gpios = <&gpio0 12 GPIO_ACTIVE_HIGH>;
      spi-dev = <&spi2>;
      #address-cells = <1>;
      #size-cells = <0>;

      ili9340: ili9340@0 {
          compatible = "ilitek,ili9340";
          reg = <0>;
          mipi-max-frequency = <32000000>;
          rotation = <270>;
          width = <320>;
          height = <240>;
      };
  };
  ```

### [Flash](#id15)

- The [`st,stm32-ospi-nor`](../build/dts/api/bindings/flash_controller/st%2Cstm32-ospi-nor.md#std-dtcompatible-st-stm32-ospi-nor) and [`st,stm32-qspi-nor`](../build/dts/api/bindings/flash_controller/st%2Cstm32-qspi-nor.md#std-dtcompatible-st-stm32-qspi-nor) give the nor flash
  base address and size (in Bytes) with the **reg** property as follows.
  The <size> property is not used anymore.

  ```devicetree
  mx25lm51245: ospi-nor-flash@70000000 {
          compatible = "st,stm32-ospi-nor";
          reg = <0x70000000 DT_SIZE_M(64)>; /* 512 Mbits*/
  };
  ```

### [General Purpose I/O (GPIO)](#id16)

- The `nxp,pcf8574` driver has been renamed to
  [`nxp,pcf857x`](../build/dts/api/bindings/gpio/nxp%2Cpcf857x.md#std-dtcompatible-nxp-pcf857x). ([GitHub #67054](https://github.com/zephyrproject-rtos/zephyr/issues/67054)) to support pcf8574 and pcf8575.
  The Kconfig option has been renamed from `CONFIG_GPIO_PCF8574` to
  [`CONFIG_GPIO_PCF857X`](../kconfig.md#CONFIG_GPIO_PCF857X "CONFIG_GPIO_PCF857X").
  The Device Tree can be configured as follows:

  ```devicetree
  &i2c {
    status = "okay";
    pcf8574: pcf857x@20 {
        compatible = "nxp,pcf857x";
        status = "okay";
        reg = <0x20>;
        gpio-controller;
        #gpio-cells = <2>;
        ngpios = <8>;
    };

    pcf8575: pcf857x@21 {
        compatible = "nxp,pcf857x";
        status = "okay";
        reg = <0x21>;
        gpio-controller;
        #gpio-cells = <2>;
        ngpios = <16>;
    };
  };
  ```

### [Input](#id17)

- Touchscreen drivers [`focaltech,ft5336`](../build/dts/api/bindings/input/focaltech%2Cft5336.md#std-dtcompatible-focaltech-ft5336) and
  [`goodix,gt911`](../build/dts/api/bindings/input/goodix%2Cgt911.md#std-dtcompatible-goodix-gt911) were using the incorrect polarity for the
  respective `reset-gpios`. This has been fixed so those signals now have to
  be flagged as [`GPIO_ACTIVE_LOW`](../hardware/peripherals/gpio.md#c.GPIO_ACTIVE_LOW "GPIO_ACTIVE_LOW") in the devicetree. ([GitHub #64800](https://github.com/zephyrproject-rtos/zephyr/issues/64800))

### [Interrupt Controller](#id18)

- The function signature of the `isr_t` callback function passed to the `shared_irq`
  interrupt controller driver API via `shared_irq_isr_register()` has changed.
  The callback now takes an additional irq\_number parameter. Out-of-tree users of
  this API will need to be updated.

  ([GitHub #66427](https://github.com/zephyrproject-rtos/zephyr/issues/66427))

### [Renesas RA Series Drivers](#id19)

- Several Renesas RA series drivers Kconfig options have been renamed:

  - `CONFIG_CLOCK_CONTROL_RA` -> [`CONFIG_CLOCK_CONTROL_RENESAS_RA`](../kconfig.md#CONFIG_CLOCK_CONTROL_RENESAS_RA "CONFIG_CLOCK_CONTROL_RENESAS_RA")
  - `CONFIG_GPIO_RA` -> [`CONFIG_GPIO_RENESAS_RA`](../kconfig.md#CONFIG_GPIO_RENESAS_RA "CONFIG_GPIO_RENESAS_RA")
  - `CONFIG_PINCTRL_RA` -> [`CONFIG_PINCTRL_RENESAS_RA`](../kconfig.md#CONFIG_PINCTRL_RENESAS_RA "CONFIG_PINCTRL_RENESAS_RA")
  - `CONFIG_UART_RA` -> [`CONFIG_UART_RENESAS_RA`](../kconfig.md#CONFIG_UART_RENESAS_RA "CONFIG_UART_RENESAS_RA")

### [Sensors](#id20)

- The [`st,lsm6dsv16x`](../build/dts/api/compatibles/st%2Clsm6dsv16x.md#std-dtcompatible-st-lsm6dsv16x) sensor driver has been changed to support
  configuration of both int1 and int2 pins. The DT attribute `irq-gpios` has been
  removed and substituted by two new attributes, `int1-gpios` and `int2-gpios`.
  These attributes must be configured in the Device Tree similarly to the following
  example:

  ```devicetree
  / {
      lsm6dsv16x@0 {
          compatible = "st,lsm6dsv16x";

          int1-gpios = <&gpioa 4 GPIO_ACTIVE_HIGH>;
          int2-gpios = <&gpiod 11 GPIO_ACTIVE_HIGH>;
          drdy-pin = <2>;
      };
  };
  ```

### [Serial](#id21)

- Runtime configuration is now disabled by default for Nordic UART drivers. The motivation for the
  change is that this feature is rarely used and disabling it significantly reduces the memory
  footprint.

### [Timer](#id22)

- The [`st,stm32-lptim`](../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) lptim which is selected for counting ticks during
  low power modes is identified by **stm32\_lp\_tick\_source** in the device tree as follows.
  The stm32\_lptim\_timer driver has been changed to support this.

  ```devicetree
  stm32_lp_tick_source: &lptim1 {
          status = "okay";
  };
  ```

## [Bluetooth](#id23)

- ATT now has its own TX buffer pool.
  If extra ATT buffers were configured using [`CONFIG_BT_L2CAP_TX_BUF_COUNT`](../kconfig.md#CONFIG_BT_L2CAP_TX_BUF_COUNT "CONFIG_BT_L2CAP_TX_BUF_COUNT"),
  they now instead should be configured through [`CONFIG_BT_ATT_TX_COUNT`](../kconfig.md#CONFIG_BT_ATT_TX_COUNT "CONFIG_BT_ATT_TX_COUNT").
- The HCI implementation for both the Host and the Controller sides has been
  renamed for the IPC transport. The `CONFIG_BT_RPMSG` Kconfig option is now
  [`CONFIG_BT_HCI_IPC`](../kconfig.md#CONFIG_BT_HCI_IPC "CONFIG_BT_HCI_IPC"), and the `zephyr,bt-hci-rpmsg-ipc`
  Devicetree chosen is now `zephyr,bt-hci-ipc`. The existing sample has also
  been renamed, from `samples/bluetooth/hci_rpmsg` to
  `samples/bluetooth/hci_ipc`. ([GitHub #64391](https://github.com/zephyrproject-rtos/zephyr/issues/64391))
- The BT GATT callback list, appended to by [`bt_gatt_cb_register()`](../connectivity/bluetooth/api/gatt.md#c.bt_gatt_cb_register "bt_gatt_cb_register"), is no longer
  cleared on [`bt_enable()`](../connectivity/bluetooth/api/gap.md#c.bt_enable "bt_enable"). Callbacks can now be registered before the initial
  call to [`bt_enable()`](../connectivity/bluetooth/api/gap.md#c.bt_enable "bt_enable"), and should no longer be re-registered after a [`bt_disable()`](../connectivity/bluetooth/api/gap.md#c.bt_disable "bt_disable")
  [`bt_enable()`](../connectivity/bluetooth/api/gap.md#c.bt_enable "bt_enable") cycle. ([GitHub #63693](https://github.com/zephyrproject-rtos/zephyr/issues/63693))
- The Bluetooth UUID has been modified to rodata in `BT_UUID_DECLARE_16`, `BT_UUID_DECLARE_32`
  and `BT_UUID_DECLARE_128` as the return value has been changed to `const`.
  Any pointer to a UUID must be prefixed with `const`, otherwise there will be a compilation
  warning. For example change `struct bt_uuid *uuid = BT_UUID_DECLARE_16(xx)` to
  `const struct bt_uuid *uuid = BT_UUID_DECLARE_16(xx)`. ([GitHub #66136](https://github.com/zephyrproject-rtos/zephyr/issues/66136))
- The [`bt_l2cap_chan_send()`](../connectivity/bluetooth/api/l2cap.md#c.bt_l2cap_chan_send "bt_l2cap_chan_send") API no longer allocates buffers from the same pool as its buf
  parameter when segmenting SDUs into PDUs. In order to reproduce the previous behavior, the
  application should register the alloc\_seg channel callback and allocate from the same pool as
  buf.
- The [`bt_l2cap_chan_send()`](../connectivity/bluetooth/api/l2cap.md#c.bt_l2cap_chan_send "bt_l2cap_chan_send") API now requires the application to reserve
  enough bytes for the L2CAP headers. Call `net_buf_reserve(buf,
  BT_L2CAP_SDU_CHAN_SEND_RESERVE);` at buffer allocation time to do so.
- BT\_ISO\_TIMESTAMP\_NONE has been removed and the ts parameter of `bt_iso_chan_send()` has
  as well. `bt_iso_chan_send()` now always sends without timestamp. To send with a timestamp,
  `bt_iso_chan_send_ts()` can be used.

### [Bluetooth Mesh](#id24)

> - The Bluetooth Mesh `model` declaration has been changed to add prefix `const`.
>   The `model->user_data`, `model->elem_idx` and `model->mod_idx` field has been changed to
>   the new runtime structure, replaced by `model->rt->user_data`, `model->rt->elem_idx` and
>   `model->rt->mod_idx` separately. ([GitHub #65152](https://github.com/zephyrproject-rtos/zephyr/issues/65152))
> - The Bluetooth Mesh `element` declaration has been changed to add prefix `const`.
>   The `elem->addr` field has been changed to the new runtime structure, replaced by
>   `elem->rt->addr`. ([GitHub #65388](https://github.com/zephyrproject-rtos/zephyr/issues/65388))
> - Deprecated [`CONFIG_BT_MESH_PROV_DEVICE`](../kconfig.md#CONFIG_BT_MESH_PROV_DEVICE "CONFIG_BT_MESH_PROV_DEVICE"). This option is
>   replaced by new option [`CONFIG_BT_MESH_PROVISIONEE`](../kconfig.md#CONFIG_BT_MESH_PROVISIONEE "CONFIG_BT_MESH_PROVISIONEE") to
>   be aligned with Mesh Protocol Specification v1.1, section 5.4. ([GitHub #64252](https://github.com/zephyrproject-rtos/zephyr/issues/64252))
> - Removed the `CONFIG_BT_MESH_V1d1` Kconfig option.
> - Removed the `CONFIG_BT_MESH_TX_SEG_RETRANS_COUNT`,
>   `CONFIG_BT_MESH_TX_SEG_RETRANS_TIMEOUT_UNICAST`,
>   `CONFIG_BT_MESH_TX_SEG_RETRANS_TIMEOUT_GROUP`, `CONFIG_BT_MESH_SEG_ACK_BASE_TIMEOUT`,
>   `CONFIG_BT_MESH_SEG_ACK_PER_HOP_TIMEOUT`, `BT_MESH_SEG_ACK_PER_SEGMENT_TIMEOUT`
>   Kconfig options. They are superseded by the
>   [`CONFIG_BT_MESH_SAR_TX_SEG_INT_STEP`](../kconfig.md#CONFIG_BT_MESH_SAR_TX_SEG_INT_STEP "CONFIG_BT_MESH_SAR_TX_SEG_INT_STEP"),
>   [`CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_COUNT`](../kconfig.md#CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_COUNT "CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_COUNT"),
>   [`CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_WITHOUT_PROG_COUNT`](../kconfig.md#CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_WITHOUT_PROG_COUNT "CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_WITHOUT_PROG_COUNT"),
>   [`CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_STEP`](../kconfig.md#CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_STEP "CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_STEP"),
>   [`CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_INC`](../kconfig.md#CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_INC "CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_INC"),
>   [`CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_COUNT`](../kconfig.md#CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_COUNT "CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_COUNT"),
>   [`CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_INT`](../kconfig.md#CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_INT "CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_INT"),
>   [`CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD`](../kconfig.md#CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD "CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD"),
>   [`CONFIG_BT_MESH_SAR_RX_ACK_DELAY_INC`](../kconfig.md#CONFIG_BT_MESH_SAR_RX_ACK_DELAY_INC "CONFIG_BT_MESH_SAR_RX_ACK_DELAY_INC"),
>   [`CONFIG_BT_MESH_SAR_RX_SEG_INT_STEP`](../kconfig.md#CONFIG_BT_MESH_SAR_RX_SEG_INT_STEP "CONFIG_BT_MESH_SAR_RX_SEG_INT_STEP"),
>   [`CONFIG_BT_MESH_SAR_RX_DISCARD_TIMEOUT`](../kconfig.md#CONFIG_BT_MESH_SAR_RX_DISCARD_TIMEOUT "CONFIG_BT_MESH_SAR_RX_DISCARD_TIMEOUT"),
>   [`CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT`](../kconfig.md#CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT "CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT") Kconfig options.

### [Bluetooth Audio](#id25)

> - The `BT_AUDIO_CODEC_LC3_*` values from `<zephyr/bluetooth/audio/lc3.h>` have moved to
>   `<zephyr/bluetooth/audio/audio.h>` and have the `LC3` part of their names replaced by a
>   more semantically correct name: e.g.
>   `BT_AUDIO_CODEC_LC3_CHAN_COUNT` is now `BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT`,
>   `BT_AUDIO_CODEC_LC3_FREQ` is now `BT_AUDIO_CODEC_CAP_TYPE_FREQ`, and
>   `BT_AUDIO_CODEC_CONFIG_LC3_FREQ` is now `BT_AUDIO_CODEC_CFG_FREQ`, etc.
>   Similarly the enumerations have also been renamed.
>   E.g. `bt_audio_codec_config_freq` is now `bt_audio_codec_cfg_freq`,
>   `bt_audio_codec_capability_type` is now `bt_audio_codec_cap_type`,
>   `bt_audio_codec_config_type` is now `bt_audio_codec_cfg_type`, etc. ([GitHub #67024](https://github.com/zephyrproject-rtos/zephyr/issues/67024))
> - The ts parameter of [`bt_bap_stream_send()`](../connectivity/bluetooth/api/bap.md#c.bt_bap_stream_send "bt_bap_stream_send") has been removed.
>   [`bt_bap_stream_send()`](../connectivity/bluetooth/api/bap.md#c.bt_bap_stream_send "bt_bap_stream_send") now always sends without timestamp.
>   To send with a timestamp, [`bt_bap_stream_send_ts()`](../connectivity/bluetooth/api/bap.md#c.bt_bap_stream_send_ts "bt_bap_stream_send_ts") can be used.
> - The ts parameter of [`bt_cap_stream_send()`](../connectivity/bluetooth/api/cap.md#c.bt_cap_stream_send "bt_cap_stream_send") has been removed.
>   [`bt_cap_stream_send()`](../connectivity/bluetooth/api/cap.md#c.bt_cap_stream_send "bt_cap_stream_send") now always sends without timestamp.
>   To send with a timestamp, [`bt_cap_stream_send_ts()`](../connectivity/bluetooth/api/cap.md#c.bt_cap_stream_send_ts "bt_cap_stream_send_ts") can be used.

## [Networking](#id26)

- The CoAP public API has some minor changes to take into account. The
  [`coap_remove_observer()`](../connectivity/networking/api/coap.md#c.coap_remove_observer "coap_remove_observer") now returns a result if the observer was removed. This
  change is used by the newly introduced [CoAP server](../connectivity/networking/api/coap_server.md#coap-server-interface) subsystem. Also, the
  `request` argument for [`coap_well_known_core_get()`](../connectivity/networking/api/coap.md#c.coap_well_known_core_get "coap_well_known_core_get") is made `const`.
  ([GitHub #64265](https://github.com/zephyrproject-rtos/zephyr/issues/64265))
- CoAP observer events have moved from a callback function in a CoAP resource to the Network Events
  subsystem. The `CONFIG_COAP_OBSERVER_EVENTS` configuration option has been removed.
  ([GitHub #65936](https://github.com/zephyrproject-rtos/zephyr/issues/65936))
- The CoAP public API function [`coap_pending_init()`](../connectivity/networking/api/coap.md#c.coap_pending_init "coap_pending_init") has changed. The parameter
  `retries` is replaced with a pointer to [`coap_transmission_parameters`](../connectivity/networking/api/coap.md#c.coap_transmission_parameters "coap_transmission_parameters"). This allows to
  specify retransmission parameters of the confirmable message. It is safe to pass a NULL pointer to
  use default values.
  ([GitHub #66482](https://github.com/zephyrproject-rtos/zephyr/issues/66482))
- The CoAP public API functions [`coap_service_send()`](../connectivity/networking/api/coap_server.md#c.coap_service_send "coap_service_send") and [`coap_resource_send()`](../connectivity/networking/api/coap_server.md#c.coap_resource_send "coap_resource_send") have
  changed. An additional parameter pointer to [`coap_transmission_parameters`](../connectivity/networking/api/coap.md#c.coap_transmission_parameters "coap_transmission_parameters") has been
  added. It is safe to pass a NULL pointer to use default values. ([GitHub #66540](https://github.com/zephyrproject-rtos/zephyr/issues/66540))
- The IGMP multicast library now supports IGMPv3. This results in a minor change to the existing
  api. The `net_ipv4_igmp_join()` now takes an additional argument of the type
  `const struct igmp_param *param`. This allows IGMPv3 to exclude/include certain groups of
  addresses. If this functionality is not used or available (when using IGMPv2), you can safely pass
  a NULL pointer. IGMPv3 can be enabled using the Kconfig `CONFIG_NET_IPV4_IGMPV3`.
  ([GitHub #65293](https://github.com/zephyrproject-rtos/zephyr/issues/65293))
- The network stack now uses a separate IPv4 TTL (time-to-live) value for multicast packets.
  Before, the same TTL value was used for unicast and multicast packets.
  The IPv6 hop limit value is also changed so that unicast and multicast packets can have a
  different one. ([GitHub #65886](https://github.com/zephyrproject-rtos/zephyr/issues/65886))
- The Ethernet phy APIs defined in `<zephyr/net/phy.h>` are removed from syscall list.
  The APIs were marked as callable from usermode but in practice this does not work as the device
  cannot be accessed from usermode thread. This means that the API calls will need to made
  from supervisor mode thread.
- The zperf ratio between mbps and kbps, kbps and bps is changed to 1000, instead of 1024,
  to align with iperf ratios.
- For network buffer pools maximum allocation size was added to a common structure
  `struct net_buf_data_alloc` as a new field `max_alloc_size`. Similar member `data_size` of
  `struct net_buf_pool_fixed` that was specific only for buffer pools with a fixed size was
  removed.

## [Other Subsystems](#id27)

### [LoRaWAN](#id28)

- The API to register a callback to provide battery level information to the LoRaWAN stack has been
  renamed from `lorawan_set_battery_level_callback` to
  [`lorawan_register_battery_level_callback()`](../connectivity/lora_lorawan/index.md#c.lorawan_register_battery_level_callback "lorawan_register_battery_level_callback") and the return type is now `void`. This
  is more consistent with similar functions for downlink and data rate changed callbacks.
  ([GitHub #65103](https://github.com/zephyrproject-rtos/zephyr/issues/65103))

### [MCUmgr](#id29)

- MCUmgr applications that make use of serial transports (shell or UART) must now select
  [`CONFIG_CRC`](../kconfig.md#CONFIG_CRC "CONFIG_CRC"), this was previously erroneously selected if MCUmgr was enabled,
  when for non-serial transports it was not needed. ([GitHub #64078](https://github.com/zephyrproject-rtos/zephyr/issues/64078))

### [Shell](#id30)

- The following subsystem and driver shell modules are now disabled by default. Each required shell
  module must now be explicitly enabled via Kconfig ([GitHub #65307](https://github.com/zephyrproject-rtos/zephyr/issues/65307)):

  - [`CONFIG_ACPI_SHELL`](../kconfig.md#CONFIG_ACPI_SHELL "CONFIG_ACPI_SHELL")
  - [`CONFIG_ADC_SHELL`](../kconfig.md#CONFIG_ADC_SHELL "CONFIG_ADC_SHELL")
  - [`CONFIG_AUDIO_CODEC_SHELL`](../kconfig.md#CONFIG_AUDIO_CODEC_SHELL "CONFIG_AUDIO_CODEC_SHELL")
  - [`CONFIG_CAN_SHELL`](../kconfig.md#CONFIG_CAN_SHELL "CONFIG_CAN_SHELL")
  - [`CONFIG_CLOCK_CONTROL_NRF_SHELL`](../kconfig.md#CONFIG_CLOCK_CONTROL_NRF_SHELL "CONFIG_CLOCK_CONTROL_NRF_SHELL")
  - [`CONFIG_DAC_SHELL`](../kconfig.md#CONFIG_DAC_SHELL "CONFIG_DAC_SHELL")
  - [`CONFIG_DEBUG_COREDUMP_SHELL`](../kconfig.md#CONFIG_DEBUG_COREDUMP_SHELL "CONFIG_DEBUG_COREDUMP_SHELL")
  - [`CONFIG_EDAC_SHELL`](../kconfig.md#CONFIG_EDAC_SHELL "CONFIG_EDAC_SHELL")
  - [`CONFIG_EEPROM_SHELL`](../kconfig.md#CONFIG_EEPROM_SHELL "CONFIG_EEPROM_SHELL")
  - [`CONFIG_FLASH_SHELL`](../kconfig.md#CONFIG_FLASH_SHELL "CONFIG_FLASH_SHELL")
  - [`CONFIG_HWINFO_SHELL`](../kconfig.md#CONFIG_HWINFO_SHELL "CONFIG_HWINFO_SHELL")
  - [`CONFIG_I2C_SHELL`](../kconfig.md#CONFIG_I2C_SHELL "CONFIG_I2C_SHELL")
  - [`CONFIG_LOG_CMDS`](../kconfig.md#CONFIG_LOG_CMDS "CONFIG_LOG_CMDS")
  - [`CONFIG_LORA_SHELL`](../kconfig.md#CONFIG_LORA_SHELL "CONFIG_LORA_SHELL")
  - [`CONFIG_MCUBOOT_SHELL`](../kconfig.md#CONFIG_MCUBOOT_SHELL "CONFIG_MCUBOOT_SHELL")
  - [`CONFIG_MDIO_SHELL`](../kconfig.md#CONFIG_MDIO_SHELL "CONFIG_MDIO_SHELL")
  - [`CONFIG_OPENTHREAD_SHELL`](../kconfig.md#CONFIG_OPENTHREAD_SHELL "CONFIG_OPENTHREAD_SHELL")
  - [`CONFIG_PCIE_SHELL`](../kconfig.md#CONFIG_PCIE_SHELL "CONFIG_PCIE_SHELL")
  - [`CONFIG_PSCI_SHELL`](../kconfig.md#CONFIG_PSCI_SHELL "CONFIG_PSCI_SHELL")
  - [`CONFIG_PWM_SHELL`](../kconfig.md#CONFIG_PWM_SHELL "CONFIG_PWM_SHELL")
  - [`CONFIG_REGULATOR_SHELL`](../kconfig.md#CONFIG_REGULATOR_SHELL "CONFIG_REGULATOR_SHELL")
  - [`CONFIG_SENSOR_SHELL`](../kconfig.md#CONFIG_SENSOR_SHELL "CONFIG_SENSOR_SHELL")
  - [`CONFIG_SMBUS_SHELL`](../kconfig.md#CONFIG_SMBUS_SHELL "CONFIG_SMBUS_SHELL")
  - [`CONFIG_STATS_SHELL`](../kconfig.md#CONFIG_STATS_SHELL "CONFIG_STATS_SHELL")
  - [`CONFIG_USBD_SHELL`](../kconfig.md#CONFIG_USBD_SHELL "CONFIG_USBD_SHELL")
  - [`CONFIG_USBH_SHELL`](../kconfig.md#CONFIG_USBH_SHELL "CONFIG_USBH_SHELL")
  - [`CONFIG_W1_SHELL`](../kconfig.md#CONFIG_W1_SHELL "CONFIG_W1_SHELL")
  - [`CONFIG_WDT_SHELL`](../kconfig.md#CONFIG_WDT_SHELL "CONFIG_WDT_SHELL")
- The `SHELL_UART_DEFINE` macro now only requires a `_name` argument. In the meantime, the
  macro accepts additional arguments (ring buffer TX & RX size arguments) for compatibility with
  previous Zephyr version, but they are ignored, and will be removed in future release.
- [`CONFIG_SHELL_BACKEND_SERIAL_API`](../kconfig.md#CONFIG_SHELL_BACKEND_SERIAL_API "CONFIG_SHELL_BACKEND_SERIAL_API") now does not automatically default to
  [`CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC`](../kconfig.md#CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC "CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC") when
  [`CONFIG_UART_ASYNC_API`](../kconfig.md#CONFIG_UART_ASYNC_API "CONFIG_UART_ASYNC_API") is enabled, [`CONFIG_SHELL_ASYNC_API`](../kconfig.md#CONFIG_SHELL_ASYNC_API "CONFIG_SHELL_ASYNC_API")
  also has to be enabled in order to use the asynchronous serial shell (:github: 68475).

### [ZBus](#id31)

- The `CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_DYNAMIC` and
  `CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_STATIC` zbus options are renamed. Instead, the new
  [`CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC`](../kconfig.md#CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC "CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC") and
  [`CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC`](../kconfig.md#CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC "CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC") options should be used.
  ([GitHub #65632](https://github.com/zephyrproject-rtos/zephyr/issues/65632))
- To enable the zbus HLP priority boost, the developer must call the
  [`zbus_obs_attach_to_thread()`](../services/zbus/index.md#c.zbus_obs_attach_to_thread "zbus_obs_attach_to_thread") inside the attaching thread. The observer will then assume the
  attached thread priority which will be used by zbus to calculate HLP priority. ([GitHub #63183](https://github.com/zephyrproject-rtos/zephyr/issues/63183))

## [Userspace](#id32)

- A number of userspace related functions have been moved out of the `z_` namespace
  and into the kernel namespace.

  - `Z_OOPS` to `K_OOPS`
  - `Z_SYSCALL_MEMORY` to `K_SYSCALL_MEMORY`
  - `Z_SYSCALL_MEMORY_READ` to `K_SYSCALL_MEMORY_READ`
  - `Z_SYSCALL_MEMORY_WRITE` to `K_SYSCALL_MEMORY_WRITE`
  - `Z_SYSCALL_DRIVER_OP` to `K_SYSCALL_DRIVER_OP`
  - `Z_SYSCALL_SPECIFIC_DRIVER` to `K_SYSCALL_SPECIFIC_DRIVER`
  - `Z_SYSCALL_OBJ` to `K_SYSCALL_OBJ`
  - `Z_SYSCALL_OBJ_INIT` to `K_SYSCALL_OBJ_INIT`
  - `Z_SYSCALL_OBJ_NEVER_INIT` to `K_SYSCALL_OBJ_NEVER_INIT`
  - `z_user_from_copy` to `k_usermode_from_copy()`
  - `z_user_to_copy` to `k_usermode_to_copy()`
  - `z_user_string_copy` to `k_usermode_string_copy()`
  - `z_user_string_alloc_copy` to `k_usermode_string_alloc_copy()`
  - `z_user_alloc_from_copy` to `k_usermode_alloc_from_copy()`
  - `z_user_string_nlen` to `k_usermode_string_nlen()`
  - `z_dump_object_error` to `k_object_dump_error()`
  - `z_object_validate` to `k_object_validate()`
  - `z_object_find` to `k_object_find()`
  - `z_object_wordlist_foreach` to `k_object_wordlist_foreach()`
  - `z_thread_perms_inherit` to `k_thread_perms_inherit()`
  - `z_thread_perms_set` to `k_thread_perms_set()`
  - `z_thread_perms_clear` to `k_thread_perms_clear()`
  - `z_thread_perms_all_clear` to `k_thread_perms_all_clear()`
  - `z_object_uninit` to `k_object_uninit()`
  - `z_object_recycle` to `k_object_recycle()`
  - `z_obj_validation_check` to `k_object_validation_check()`
  - `Z_SYSCALL_VERIFY_MSG` to `K_SYSCALL_VERIFY_MSG`
  - `z_object` to `k_object`
  - `z_object_init` to `k_object_init()`
  - `z_dynamic_object_aligned_create` to `k_object_create_dynamic_aligned()`

## [Architectures](#id33)

### [Xtensa](#id34)

- [`CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC`](../kconfig.md#CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC "CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC") no longer has a default in
  the architecture layer. Instead, SoCs or boards will need to define it.
- Scratch registers `ZSR_ALLOCA` has been renamed to `ZSR_A0SAVE`.
- Renamed files with hyhphens to underscores:

  - `xtensa-asm2-context.h` to `xtensa_asm2_context.h`
  - `xtensa-asm2-s.h` to `xtensa_asm2_s.h`
- `xtensa_asm2.h` has been removed. Use `xtensa_asm2_context.h` instead for
  stack frame structs.
- Renamed functions out of `z_` namespace into `xtensa_` namespace.

  - `z_xtensa_irq_enable` to `xtensa_irq_enable()`
  - `z_xtensa_irq_disable` to `xtensa_irq_disable()`
  - `z_xtensa_irq_is_enabled` to `xtensa_irq_is_enabled()`
