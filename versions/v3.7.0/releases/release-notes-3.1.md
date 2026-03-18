---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/releases/release-notes-3.1.html
original_path: releases/release-notes-3.1.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Zephyr 3.1.0

The following sections provide detailed lists of changes by component.

## API Changes

### Changes in this release

- All Zephyr public headers have been moved to `include/zephyr`, meaning they
  need to be prefixed with `<zephyr/...>` when included. Because this change
  can potentially break many applications or libraries,
  `CONFIG_LEGACY_INCLUDE_PATH` is provided to allow using the
  old include path. This option is now enabled by default to allow a smooth
  transition. In order to facilitate the migration to the new include prefix, a
  script to automate the process is also provided:
  [scripts/utils/migrate\_includes.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/utils/migrate_includes.py).
- LoRaWAN: The message type parameter in [`lorawan_send()`](../connectivity/lora_lorawan/index.md#c.lorawan_send "lorawan_send") was changed
  from `uint8_t` to `enum lorawan_message_type`. If `0` was passed for
  unconfirmed message, this has to be changed to `LORAWAN_MSG_UNCONFIRMED`.
- Bluetooth: Applications where [`CONFIG_BT_EATT`](../kconfig.md#CONFIG_BT_EATT "CONFIG_BT_EATT") is enabled
  must set the `chan_opt` field on the GATT parameter structs.
  To keep the old behavior use [`BT_ATT_CHAN_OPT_NONE`](../connectivity/bluetooth/api/att.md#c.bt_att_chan_opt.BT_ATT_CHAN_OPT_NONE "BT_ATT_CHAN_OPT_NONE").
- Disk Subsystem: SPI mode SD cards now use the SD subsystem to communicate
  with SD cards. See [the disk access api](../services/storage/disk/access.md#disk-access-api) for an
  example of the new devicetree binding format required.
- Kconfig preprocessor function `dt_nodelabel_has_compat` was redefined, for
  consistency with the `dt_nodelabel_has_prop` function and devicetree macros
  like [`DT_NODE_HAS_COMPAT()`](../build/dts/api/api.md#c.DT_NODE_HAS_COMPAT "DT_NODE_HAS_COMPAT"). Now the function does not take into account
  the status of the checked node. Its former functionality is provided by the
  newly introduced `dt_nodelabel_enabled_with_compat` function.
- CAN

  - Added `const struct device` parameter to the following CAN callback function signatures:

    - `can_tx_callback_t`
    - `can_rx_callback_t`
    - `can_state_change_callback_t`
  - Allow calling the following CAN API functions from userspace:

    - [`can_set_mode()`](../hardware/peripherals/can/controller.md#c.can_set_mode "can_set_mode")
    - [`can_calc_timing()`](../hardware/peripherals/can/controller.md#c.can_calc_timing "can_calc_timing")
    - [`can_calc_timing_data()`](../hardware/peripherals/can/controller.md#c.can_calc_timing_data "can_calc_timing_data")
    - [`can_set_bitrate()`](../hardware/peripherals/can/controller.md#c.can_set_bitrate "can_set_bitrate")
    - [`can_get_max_filters()`](../hardware/peripherals/can/controller.md#c.can_get_max_filters "can_get_max_filters")
  - Changed [`can_set_bitrate()`](../hardware/peripherals/can/controller.md#c.can_set_bitrate "can_set_bitrate") to use a sample point of 75.0% for bitrates over 800 kbit/s,
    80.0% for bitrates over 500 kbit/s, and 87.5% for all other bitrates.
  - Split CAN classic and CAN-FD APIs:

    - [`can_set_timing()`](../hardware/peripherals/can/controller.md#c.can_set_timing "can_set_timing") split into [`can_set_timing()`](../hardware/peripherals/can/controller.md#c.can_set_timing "can_set_timing") and
      [`can_set_timing_data()`](../hardware/peripherals/can/controller.md#c.can_set_timing_data "can_set_timing_data").
    - [`can_set_bitrate()`](../hardware/peripherals/can/controller.md#c.can_set_bitrate "can_set_bitrate") split into [`can_set_bitrate()`](../hardware/peripherals/can/controller.md#c.can_set_bitrate "can_set_bitrate") and
      [`can_set_bitrate_data()`](../hardware/peripherals/can/controller.md#c.can_set_bitrate_data "can_set_bitrate_data").
  - Converted the `enum can_mode` into a `can_mode_t` bitfield and renamed the CAN mode
    definitions:

    - `CAN_NORMAL_MODE` renamed to [`CAN_MODE_NORMAL`](../hardware/peripherals/can/controller.md#c.CAN_MODE_NORMAL "CAN_MODE_NORMAL").
    - `CAN_SILENT_MODE` renamed to [`CAN_MODE_LISTENONLY`](../hardware/peripherals/can/controller.md#c.CAN_MODE_LISTENONLY "CAN_MODE_LISTENONLY").
    - `CAN_LOOPBACK_MODE` renamed to [`CAN_MODE_LOOPBACK`](../hardware/peripherals/can/controller.md#c.CAN_MODE_LOOPBACK "CAN_MODE_LOOPBACK").
    - The previous `CAN_SILENT_LOOPBACK_MODE` can be set using the bitmask `(CAN_MODE_LISTENONLY |
      CAN_MODE_LOOPBACK)`.
  - STM32H7: [`CONFIG_NOCACHE_MEMORY`](../kconfig.md#CONFIG_NOCACHE_MEMORY "CONFIG_NOCACHE_MEMORY") is no longer responsible for disabling
    data cache when defined. Use `CONFIG_DCACHE=n` instead.
  - Converted the STM32F1 pin nodes configuration names to include remap information (in
    cases other than NO\_REMAP/REMAP\_0)
    For instance:

    - `i2c1_scl_pb8` renamed to `i2c1_scl_remap1_pb8`

### Removed APIs in this release

- STM32F1 Serial wire JTAG configuration (SWJ CFG) configuration choice
  was moved from Kconfig to [devicetree](../build/dts/index.md#dt-guide).
  See the [`st,stm32f1-pinctrl`](../build/dts/api/bindings/pinctrl/st%2Cstm32f1-pinctrl.md#std-dtcompatible-st-stm32f1-pinctrl) devicetree binding for more information.
  As a consequence, the following Kconfig symbols were removed:

  - `CONFIG_GPIO_STM32_SWJ_ENABLE`
  - `CONFIG_GPIO_STM32_SWJ_NONJTRST`
  - `CONFIG_GPIO_STM32_SWJ_NOJTAG`
  - `CONFIG_GPIO_STM32_SWJ_DISABLE`
- Removed experimental 6LoCAN protocol support.
- Removed the following deprecated CAN APIs:

  - Custom CAN error codes
  - `can_configure()`
  - `can_attach_workq()`
  - `can_attach_isr()`
  - `can_attach_msgq()`
  - `can_detach()`
  - `can_register_state_change_isr()`
  - `can_write()`

### Deprecated in this release

- `nvs_init()` is deprecated in favor of utilizing [`nvs_mount()`](../services/storage/nvs/nvs.md#c.nvs_mount "nvs_mount").
- `lwm2m_engine_set_res_data()` is deprecated in favor of `lwm2m_engine_set_res_buf()`
- `lwm2m_engine_get_res_data()` is deprecated in favor of `lwm2m_engine_get_res_buf()`
- The TinyCBOR module has been deprecated in favor of the new zcbor CBOR
  library, included with Zephyr in this release.
- GPIO

  - Deprecated the `GPIO_INT_DEBOUNCE` flag and the `GPIO_DS_*` and
    `GPIO_VOLTAGE_*` groups of flags. Controller/SoC specific flags
    should now be used instead.
- SPI

  - Deprecated the `gpio_dev`, `gpio_pin`, and `gpio_dt_flags` members in
    struct [`spi_cs_control`](../hardware/peripherals/spi.md#c.spi_cs_control "spi_cs_control") in favor of a new struct
    [`gpio_dt_spec`](../hardware/peripherals/gpio.md#c.gpio_dt_spec "gpio_dt_spec") member named `gpio`.
- PWM

  - The `pin` prefix has been removed from all PWM API calls. So for example,
    `pwm_pin_set_cycles` is now `pwm_set_cycles`. The old API calls are
    still provided, but are now deprecated.
  - PWM periods are now always set in nanoseconds, so `_nsec` and `_usec`
    set functions such as `pwm_pin_set_nsec()` and `pwm_pin_set_usec()`
    have been deprecated. Other units can be specified using, e.g.
    `PWM_USEC()` macros, which convert other units to nanoseconds.
- Utilities

  - `UTIL_LISTIFY` has been deprecated. Use [`LISTIFY`](../kernel/util/index.md#c.LISTIFY "LISTIFY") instead.
- Mesh

  - The following functions related to the Bluetooth Mesh Health Client model:

    - `bt_mesh_health_fault_get()` replace with [`bt_mesh_health_cli_fault_get()`](../connectivity/bluetooth/api/mesh/health_cli.md#c.bt_mesh_health_cli_fault_get "bt_mesh_health_cli_fault_get")
    - `bt_mesh_health_fault_clear()` replace with [`bt_mesh_health_cli_fault_clear()`](../connectivity/bluetooth/api/mesh/health_cli.md#c.bt_mesh_health_cli_fault_clear "bt_mesh_health_cli_fault_clear")
    - `bt_mesh_health_fault_clear_unack()` replace with [`bt_mesh_health_cli_fault_clear_unack()`](../connectivity/bluetooth/api/mesh/health_cli.md#c.bt_mesh_health_cli_fault_clear_unack "bt_mesh_health_cli_fault_clear_unack")
    - `bt_mesh_health_fault_test()` replace with [`bt_mesh_health_cli_fault_test()`](../connectivity/bluetooth/api/mesh/health_cli.md#c.bt_mesh_health_cli_fault_test "bt_mesh_health_cli_fault_test")
    - `bt_mesh_health_fault_test_unack()` replace with [`bt_mesh_health_cli_fault_test_unack()`](../connectivity/bluetooth/api/mesh/health_cli.md#c.bt_mesh_health_cli_fault_test_unack "bt_mesh_health_cli_fault_test_unack")
    - `bt_mesh_health_period_get()` replace with [`bt_mesh_health_cli_period_get()`](../connectivity/bluetooth/api/mesh/health_cli.md#c.bt_mesh_health_cli_period_get "bt_mesh_health_cli_period_get")
    - `bt_mesh_health_period_set()` replace with [`bt_mesh_health_cli_period_set()`](../connectivity/bluetooth/api/mesh/health_cli.md#c.bt_mesh_health_cli_period_set "bt_mesh_health_cli_period_set")
    - `bt_mesh_health_period_set_unack()` replace with [`bt_mesh_health_cli_period_set_unack()`](../connectivity/bluetooth/api/mesh/health_cli.md#c.bt_mesh_health_cli_period_set_unack "bt_mesh_health_cli_period_set_unack")
    - `bt_mesh_health_attention_get()` replace with [`bt_mesh_health_cli_attention_get()`](../connectivity/bluetooth/api/mesh/health_cli.md#c.bt_mesh_health_cli_attention_get "bt_mesh_health_cli_attention_get")
    - `bt_mesh_health_attention_set()` replace with [`bt_mesh_health_cli_attention_set()`](../connectivity/bluetooth/api/mesh/health_cli.md#c.bt_mesh_health_cli_attention_set "bt_mesh_health_cli_attention_set")
    - `bt_mesh_health_attention_set_unack()` replace with [`bt_mesh_health_cli_attention_set_unack()`](../connectivity/bluetooth/api/mesh/health_cli.md#c.bt_mesh_health_cli_attention_set_unack "bt_mesh_health_cli_attention_set_unack")
  - The following function related to the Bluetooth Mesh Health Server model:

    - `bt_mesh_fault_update()` replace with [`bt_mesh_health_srv_fault_update()`](../connectivity/bluetooth/api/mesh/health_srv.md#c.bt_mesh_health_srv_fault_update "bt_mesh_health_srv_fault_update")

### Stable API changes in this release

### New APIs in this release

- Util

  - Added [`IN_RANGE`](../kernel/util/index.md#c.IN_RANGE "IN_RANGE") for checking if a value is in the range of two
    other values.
- SDHC API

  - Added the [SDHC api](../hardware/peripherals/sdhc.md#sdhc-api), used to interact with SD host controllers.
- MIPI-DSI

  - Added a [MIPI-DSI api](../hardware/peripherals/mipi_dsi.md#mipi-dsi-api). This is an experimental API,
    some of the features/APIs will be implemented later.
- CAN

  - Added support for getting the minimum/maximum supported CAN timing parameters:

    - [`can_get_timing_min()`](../hardware/peripherals/can/controller.md#c.can_get_timing_min "can_get_timing_min")
    - [`can_get_timing_max()`](../hardware/peripherals/can/controller.md#c.can_get_timing_max "can_get_timing_max")
    - [`can_get_timing_data_min()`](../hardware/peripherals/can/controller.md#c.can_get_timing_data_min "can_get_timing_data_min")
    - [`can_get_timing_data_max()`](../hardware/peripherals/can/controller.md#c.can_get_timing_data_max "can_get_timing_data_max")
  - Added support for enabling/disabling CAN-FD mode at runtime using [`CAN_MODE_FD`](../hardware/peripherals/can/controller.md#c.CAN_MODE_FD "CAN_MODE_FD").

## Bluetooth

- Extended and Periodic advertising are no longer experimental
- Direction Finding is no longer experimental
- Added support for disabling Bluetooth, including a new `bt_disable()` API
  call
- Audio

  - Changed the implementation of PACS to indicate instead of notifying
  - Added support for the Broadcast Audio Scan Service (BASS)
  - Added support for the Hearing Access Service (HAS)
  - Added support for the Telephone Bearer Service (TBS)
- Direction Finding

  - Added sampling and switching offset configuration
- Mesh

  - Added support for Proxy Client
  - Added support for Provisioners over PB-GATT
  - Added a new heartbeat publication callback option
- Controller

  - Added support for the full ISO TX data path, including ISOAL
  - Added support for ISO Broadcast Channel Map Update
  - Added support for ISO Synchronized Receiver Channel Map Update
  - The new implementation of LL Control Procedures is now the default whenever
    Direction Finding is enabled
  - Added support for all missing v3 and v4 DTM commands
  - Implemented ISO-AL TX unframed fragmentation
  - Added support for back-to-back receiving of PDUs on nRF5x platforms
  - Increased the maximum number of simultaneous connections to 250
- HCI Driver

  - Added support for a new optional [`bt_hci_driver.close`](../connectivity/bluetooth/api/hci_drivers.md#c.bt_hci_driver.close "bt_hci_driver.close") API which
    closes HCI transport.
  - Implemented [`bt_hci_driver.close`](../connectivity/bluetooth/api/hci_drivers.md#c.bt_hci_driver.close "bt_hci_driver.close") on stm32wb HCI driver.
- Host

  - The [`bt_l2cap_chan_state`](../connectivity/bluetooth/api/l2cap.md#c.bt_l2cap_chan_state "bt_l2cap_chan_state") values `BT_L2CAP_CONNECT` and
    `BT_L2CAP_DISCONNECT` have been renamed to `BT_L2CAP_CONNECTING` and
    `BT_L2CAP_DISCONNECTING` respectively.
  - The callbacks `pairing_complete()`, `pairing_failed()`, and
    `bond_delete()` have been moved from struct `bt_auth_cb` to a
    newly created informational-only callback struct [`bt_conn_auth_info_cb`](../connectivity/bluetooth/api/connection_mgmt.md#c.bt_conn_auth_info_cb "bt_conn_auth_info_cb").
  - [`bt_conn_index()`](../connectivity/bluetooth/api/connection_mgmt.md#c.bt_conn_index "bt_conn_index") now takes a `const struct bt_conn*` argument.
  - The [`bt_gatt_subscribe_params`](../connectivity/bluetooth/api/gatt.md#c.bt_gatt_subscribe_params "bt_gatt_subscribe_params") structure’s `write` callback
    function has been deprecated. Use the new `subscribe` callback
    instead.
  - [`bt_disable()`](../connectivity/bluetooth/api/gap.md#c.bt_disable "bt_disable") was added to enable the caller to disable the Bluetooth stack.
  - Added new Kconfig options to select ISO Central and Peripheral role support
    separately
  - Added a new [`bt_get_appearance()`](../connectivity/bluetooth/api/gap.md#c.bt_get_appearance "bt_get_appearance") API call
  - Implemented support for dynamic appearance, including a new
    [`bt_set_appearance()`](../connectivity/bluetooth/api/gap.md#c.bt_set_appearance "bt_set_appearance") API call
  - Implemented support for L2CAP collision mitigation
  - Changed the scheduling of auto-initiated HCI commands so that they execute
    synchronously
  - Added a new [`bt_is_ready()`](../connectivity/bluetooth/api/gap.md#c.bt_is_ready "bt_is_ready") API call to find out if Bluetooth is
    currently enabled and initialized
  - Added support for automatic MTU exchange right after a connection is
    established
  - Created a new [`bt_conn_auth_info_cb`](../connectivity/bluetooth/api/connection_mgmt.md#c.bt_conn_auth_info_cb "bt_conn_auth_info_cb") to group the
    security-related callbacks under a single struct
  - Optimized the memory usage of the Object Transfer Service
  - Added a new `bt_hci_le_rand()` API call to obtain a random number
    from the LE Controller
  - Added a new public API to connect EATT channels, [`bt_eatt_connect()`](../connectivity/bluetooth/api/att.md#c.bt_eatt_connect "bt_eatt_connect")
  - Optimized L2CAP channels resource usage when not using dynamic channels
  - Added the ability to run the Bluetooth RX context from a workqueue, in order
    to optimize RAM usage. See [`CONFIG_BT_RECV_CONTEXT`](../kconfig.md#CONFIG_BT_RECV_CONTEXT "CONFIG_BT_RECV_CONTEXT").
  - Added support for TX complete callback on EATT channels
  - Corrected the calling of the MTU callback to happen on any reconfiguration

## Kernel

- Aborting an essential thread now causes a kernel panic, as the
  documentation has always promised but the kernel has never
  implemented.
- The k\_timer handler can now correct itself for lost time due to very
  late-arriving interrupts.
- SMP interprocessor interrupts are deferred so that they are sent only at
  schedule points, and not synchronously when the scheduler state
  changes. This prevents IPI “storms” with code that does many
  scheduler operations at once (e.g. waking up a bunch of threads).
- The timeslicing API now allows slice times to be controlled
  independently for each thread, and provides a callback to the app
  when a thread timeslice has expired. The intent is that this will
  allow apps the tools to implement CPU resource control algorithms
  (e.g. fairness or interactivity metrics, budget tracking) that are
  out of scope for Zephyr’s deterministic RTOS scheduler.

## Architectures

- ARC

  - Added ARCv3 32 bit (HS5x) support - both GNU and MWDT toolchains, both UP and SMP
  - Worked around debug\_select interference with MDB debugger
  - Switched to hs6x mcpu usage (GNU toolchain) for HS6x
- ARM

  - AARCH32

    - Added Cortex-R floating point support
  - AARCH64

    - Added support for GICv3 for the ARMv8 Xen Virtual Machine
    - Fixed SMP boot code to take into account multiple cores booting at the same time
    - Added more memory mapping types for device memory
    - Simplified and optimize switching and user mode transition code
    - Added support for CONFIG\_IRQ\_OFFLOAD\_NESTED
    - Fixed booting issue with FVP V8R >= 11.16.16
    - Switched to the IRQ stack during ISR execution
- Xtensa

  - Optimized context switches when KERNEL\_COHERENCE is enabled to
    avoid needless stack invalidations for threads that have not
    migrated between CPUs.
  - Fixed a bug that could return directly into a thread context from a
    nested interrupt instead of properly returning to the preempted
    ISR.
- x64\_64

  - UEFI devices can now use the firmware-initialized system console
    API as a printk/logging backend, simplifying platform bringup on
    devices without known-working serial port configurations.

## Boards & SoC Support

- Added support for these SoC series:

  - STM32H725/STM32H730/STM32H73B SoC variants
- Made these changes in other SoC series:

  - Added Atmel SAM UPLL clock support
  - Raspberry Pi Pico: Added HWINFO support
  - Raspberry Pi Pico: Added I2C support
  - Raspberry Pi Pico: Added reset controller support
  - Raspberry Pi Pico: Added USB support
- Changes for ARC boards:

  - Added nsim\_hs5x and nsim\_hs5x\_smp boards with ARCv3 32bit HS5x CPU
  - Added MWDT toolchain support for nsim\_hs6x and nsim\_hs6x\_smp
  - Overhauled memory layout for nSIM boards. Added a mechanism to switch between
    ICCM/DCCM memory layout and flat memory layout (i.e DDR).
  - Did required platform setup so nsim\_hs5x, nsim\_hs5x\_smp, nsim\_hs6x, nsim\_hs6x\_smp
    can be run on real HW (HAPS FPGA) with minimum additional configuration
  - Enabled MWDT toolchain support for hsdk\_2cores board
  - Adjusted test duration for SMP nSIM boards with timeout\_multiplier
- Added support for these ARM boards:

  - b\_g474e\_dpow1
  - stm32f401\_mini
- Added support for these ARM64 boards:

  - NXP i.MX8MP EVK (i.MX8M Plus LPDDR4 EVK board)
  - NXP i.MX8MM EVK (i.MX8M Mini LPDDR4 EVK board)
- Added support for these RISC-V boards:

  - GigaDevice GD32VF103C-EVAL
- Made these changes in other boards:

  - sam4s\_xplained: Added support for HWINFO
  - sam\_e70\_xlained: Added support for HWINFO and CAN-FD
  - sam\_v71\_xult: Added support for HWINFO and CAN-FD
  - gd32e103v\_eval: Added prescaler to timer
  - longan\_nano: Added support for TF-Card slot
- Added support for these following shields:

  - Keyestudio CAN-BUS Shield (KS0411)
  - MikroElektronika WIFI and BLE Shield
  - X-NUCLEO-53L0A1 ranging and gesture detection sensor expansion board

## Drivers and Sensors

- ADC

  - Atmel SAM0: Fixed adc voltage reference
  - STM32: Added support for [`adc_reference.ADC_REF_INTERNAL`](../hardware/peripherals/adc.md#c.adc_reference.ADC_REF_INTERNAL "adc_reference.ADC_REF_INTERNAL").
  - Added the [`adc_dt_spec`](../hardware/peripherals/adc.md#c.adc_dt_spec "adc_dt_spec") structure and associated helper macros,
    e.g. [`ADC_DT_SPEC_GET`](../hardware/peripherals/adc.md#c.ADC_DT_SPEC_GET "ADC_DT_SPEC_GET"), to facilitate getting configuration of
    ADC channels from devicetree nodes.
- CAN

  - Switched from transmitting CAN frames in FIFO/chronological order to transmitting according to
    CAN-ID priority (NXP FlexCAN, ST STM32 bxCAN, Bosch M\_CAN, Microchip MCP2515).
  - Added support for ST STM32U5 to the ST STM32 FDCAN driver.
  - Renamed the base Bosch M\_CAN devicetree binding compatible from `bosch,m-can-base` to
    `bosch,m_can-base`.
  - Added CAN controller statistics support (NXP FlexCAN, Renesas R-Car, ST STM32 bxCAN).
  - Added CAN transceiver support.
  - Added generic SocketCAN network interface and removed driver-specific implementations.
- Clock\_control

  - STM32: Driver was cleaned up and overhauled for easier maintenance with a deeper integration
    of device tree inputs. Driver now takes into account individual activation of clock sources
    (High/Medium/Low Internal/external speed clocks, PLLs, …)
  - STM32: Additionally to above change it is now possible for clock consumers to select an alternate
    source clock (Eg: LSE) by adding it to its ‘clocks’ property and then configure it using new
    clock\_control\_configure() API.
    See [`st,stm32-rcc`](../build/dts/api/bindings/clock/st%2Cstm32-rcc.md#std-dtcompatible-st-stm32-rcc), [`st,stm32h7-rcc`](../build/dts/api/bindings/clock/st%2Cstm32h7-rcc.md#std-dtcompatible-st-stm32h7-rcc) and [`st,stm32u5-rcc`](../build/dts/api/bindings/clock/st%2Cstm32u5-rcc.md#std-dtcompatible-st-stm32u5-rcc)
    for more information.
- Counter

  - Added driver for NXP QTMR.
- DAC

  - Added support for STM32F1 SoCs to the STM32 DAC driver.
- Disk

  - Added a generic SDMMC disk driver, that uses the SD subsystem to interact with
    disk devices. This disk driver will be used with any disk device declared
    with the `zephyr,sdmmc-disk` compatible string.
- Display

  - STM32: Added basic support for LTDC driver. Currently supported on F4, F7, H7, L4+
    and MP1 series.
- DMA

  - Added a scatter gather test for DMAs that support it
  - Cleanly shared Synopsis DW-DMA driver and Intel cAVS GPDMA driver code.
  - Added support for Synposis DW-DMA transfer lists.
  - Added support for Intel HDA for audio device and host streams.
  - Fixes for NXP eDMA to pass scatter gather tests
- Entropy

  - STM32: Prevented the core from entering stop modes during entropy operations.
- Ethernet

  - eth\_native\_posix: Added support for setting MAC address.
  - eth\_stm32\_hal: Fixed a bug which caused a segfault in case of a failed RX
    buffer allocation.
  - eth\_mcux: Added support for resetting PHY.
  - eth\_liteeth: Refactored driver to use LiteX HAL.
  - eth\_w5500: Fixed possible deadlock due to incorrect IRQ processing.
- Flash

  - Added STM32 OCTOSPI driver. Initial support is provided for L5 and U5
    series. Interrupt driven mode. Supports 1 and 8 lines in Single or Dual
    Transfer Modes.
  - STM32L5: Added support for Single Bank.
  - STM32 QSPI driver was extended with QER (SFDP, DTS), custom quad write opcode
    and 1-1-4 read mode.
  - Added support for STM32U5 series.
- GPIO

  - Refactored GPIO devicetree flags. The upper 8 bits of `gpio_dt_flags_t`
    are now reserved for controller/SoC specific flags. Certain
    hardware-specific flags previously defined as common configuration (IO
    voltage level, drive strength, and debounce filter) were replaced with ones
    defined in this controller/SoC specific space.
  - Added Xilinx PS MIO/EMIO GPIO controller driver.
  - Extended the NXP PCA95XX driver to support also PCAL95XX.
- HWINFO

  - Atmel SAM: Added RSTC support
  - Raspberry Pi Pico: Added Unique ID and reset cause driver
- I2C

  - Added arbitrary I2C clock speed support with [`I2C_SPEED_DT`](../hardware/peripherals/i2c.md#c.I2C_SPEED_DT "I2C_SPEED_DT")
  - NXP flexcomm now supports target (slave) mode
  - Fixed Atmel SAM/SAM0 exclusive bus access
  - Added ITE support
- I2S

  - Ported I2S drivers to pinctrl.
  - Fixed multiple bugs in the NXP I2S (SAI) driver, including problems with
    DMA transmission and FIFO under/overruns.
- MEMC

  - STM32: Extended FMC driver to support NOR/PSRAM. See `st,stm32-fmc-nor-psram.yaml`.
- Pin control

  - Platform support was added for:

    - Atmel SAM/SAM0
    - Espressif ESP32
    - ITE IT8XXX2
    - Microchip XEC
    - Nordic nRF (completed support)
    - Nuvoton NPCX Embedded Controller (EC)
    - NXP iMX
    - NXP Kinetis
    - NXP LPC
    - RV32M1
    - SiFive Freedom
    - Telink B91
    - TI CC13XX/CC26XX
  - STM32: It is now possible to configure plain GPIO pins using the pinctrl API.
    See [`st,stm32-pinctrl`](../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) and [`st,stm32f1-pinctrl`](../build/dts/api/bindings/pinctrl/st%2Cstm32f1-pinctrl.md#std-dtcompatible-st-stm32f1-pinctrl) for
    more information.
- PWM

  - Added [`pwm_dt_spec`](../hardware/peripherals/pwm.md#c.pwm_dt_spec "pwm_dt_spec") and associated helpers, e.g.
    [`PWM_DT_SPEC_GET`](../hardware/peripherals/pwm.md#c.PWM_DT_SPEC_GET "PWM_DT_SPEC_GET") or [`pwm_set_dt()`](../hardware/peripherals/pwm.md#c.pwm_set_dt "pwm_set_dt"). This addition makes it
    easier to use the PWM API when the PWM channel, period and flags are taken
    from a devicetree PWM cell.
  - STM32: Enabled complementary output for timer channel. A PWM consumer can now use
    `PWM_STM32_COMPLEMENTARY` to specify that PWM output should happen on a
    complementary channel pincfg (eg:`tim1_ch2n_pb14`).
  - STM32: Added counter mode support. See [`st,stm32-timers`](../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers).
  - Aligned nRF PWM drivers (pwm\_nrfx and pwm\_nrf5\_sw) with the updated PWM API.
    In particular, this means that the [`pwm_set()`](../hardware/peripherals/pwm.md#c.pwm_set "pwm_set") and
    [`pwm_set_cycles()`](../hardware/peripherals/pwm.md#c.pwm_set_cycles "pwm_set_cycles") functions need to be called with a PWM channel
    as a parameter, not with a pin number like it was for the deprecated
    `pwm_pin_set_*` functions. Also, the `flags` parameter is now supported
    by the drivers, so either the [`PWM_POLARITY_INVERTED`](../hardware/peripherals/pwm.md#c.PWM_POLARITY_INVERTED "PWM_POLARITY_INVERTED") or
    [`PWM_POLARITY_NORMAL`](../hardware/peripherals/pwm.md#c.PWM_POLARITY_NORMAL "PWM_POLARITY_NORMAL") flag must be provided in each call.
- Reset

  - Added reset controller driver API.
  - Raspberry Pi Pico: Added reset controller driver
- Sensor

  - Added NCPX ADC comparator driver.
  - Enhanced the BME680 driver to support SPI.
  - Enhanced the LIS2DW12 driver to support additional filtering and interrupt
    modes.
  - Added ICM42670 6-axis accelerometer driver.
  - Enhanced the VL53L0X driver to support reprogramming its I2C address.
  - Enhanced the Microchip XEC TACH driver to support pin control and MEC172x.
  - Added ITE IT8XXX2 voltage comparator driver.
  - Fixed register definitions in the LSM6DSL driver.
  - Fixed argument passing bug in the ICM42605 driver.
  - Removed redundant DEV\_NAME helpers in various drivers.
  - Enhanced the LIS2DH driver to support device power management.
  - Fixed overflow issue in sensor\_value\_from\_double().
  - Added MAX31875 temperature sensor driver.
- Serial

  - STM32: Added tx/rx pin swap and rx invert / tx invert capabilities.
- SPI

  - Ported all SPI drivers to pinctrl
  - Added support for SPI on the GD32 family
- Timer

  - Ported timer drivers to use pinctrl
  - LiteX: Ported the timer driver to use the HAL
- USB

  - Added RP2040 (Raspberry Pi Pico) USB device controller driver

## Networking

- CoAP:

  - Changed [`coap_pending`](../connectivity/networking/api/coap.md#c.coap_pending "coap_pending") allocation criteria. This now uses a data
    pointer instead of a timestamp, which does not give a 100% guarantee that
    structure is not in use already.
- Ethernet:

  - Added a
    [`CONFIG_NET_ETHERNET_FORWARD_UNRECOGNISED_ETHERTYPE`](../kconfig.md#CONFIG_NET_ETHERNET_FORWARD_UNRECOGNISED_ETHERTYPE "CONFIG_NET_ETHERNET_FORWARD_UNRECOGNISED_ETHERTYPE")
    option, which allows to forward frames with unrecognised EtherType to the
    network stack.
- HTTP:

  - Removed a limitation where the maximum content length was limited up to
    100000 bytes.
  - Fixed `http_client_req()` return value. The function now correctly
    reports the number of bytes sent.
  - Clarified the expected behavior in case of empty response from the server.
  - Made use of `shutdown` to tear down HTTP connection instead of
    closing the socket from a system work queue.
- LwM2M:

  - Various improvements towards LwM2M 1.1 support:

    - Added LwM2M 1.1 Discovery support.
    - Added attribute handling for Resource Instances.
    - Added support for Send, Read-composite, Write-composite, Observe-composite
      operations.
    - Added new content formats: SenML JSON, CBOR, SenML CBOR.
    - Added v1.1 implementation of core LwM2M objects.
  - Added support for dynamic Resource Instance allocation.
  - Added support for LwM2M Portfolio object (Object ID 16).
  - Added LwM2M shell module.
  - Added option to utilize DTLS session cache in queue mode.
  - Added `lwm2m_engine_path_is_observed()` API function.
  - Fixed a bug with hostname verification setting, which prevented DTLS
    connection in certain mbedTLS configurations.
  - Fixed a bug which could cause a socket descriptor leak, in case
    [`lwm2m_rd_client_start()`](../connectivity/networking/api/lwm2m.md#c.lwm2m_rd_client_start "lwm2m_rd_client_start") was called immediately after
    [`lwm2m_rd_client_stop()`](../connectivity/networking/api/lwm2m.md#c.lwm2m_rd_client_stop "lwm2m_rd_client_stop").
  - Added error reporting from [`lwm2m_rd_client_start()`](../connectivity/networking/api/lwm2m.md#c.lwm2m_rd_client_start "lwm2m_rd_client_start") and
    [`lwm2m_rd_client_stop()`](../connectivity/networking/api/lwm2m.md#c.lwm2m_rd_client_stop "lwm2m_rd_client_stop").
- Misc:

  - Added [`net_if_set_default()`](../connectivity/networking/api/net_if.md#c.net_if_set_default "net_if_set_default") function which allows to set a default
    network interface at runtime.
  - Added [`CONFIG_NET_DEFAULT_IF_UP`](../kconfig.md#CONFIG_NET_DEFAULT_IF_UP "CONFIG_NET_DEFAULT_IF_UP") option which allows to make the
    first interface which is up the default choice.
  - Fixed packet leak in network shell TCP receive handler.
  - Added [`net_pkt_rx_clone()`](../connectivity/networking/api/net_pkt.md#c.net_pkt_rx_clone "net_pkt_rx_clone") which allows to allocated packet from
    correct packet pool when cloning. This is used at the loopback interface.
  - Added [`CONFIG_NET_LOOPBACK_SIMULATE_PACKET_DROP`](../kconfig.md#CONFIG_NET_LOOPBACK_SIMULATE_PACKET_DROP "CONFIG_NET_LOOPBACK_SIMULATE_PACKET_DROP") option which
    allows to simulate packet drop at the loopback interface. This is used by
    certain test cases.
- MQTT:

  - Removed custom logging macros from MQTT implementation, in favour of the
    common networking logging.
- OpenThread:

  - Updated OpenThread revision up to commit `130afd9bb6d02f2a07e86b824fb7a79e9fca5fe0`.
  - Implemented `otPlatCryptoRand` platform API for OpenThread.
  - Added support for PSA MAC keys.
  - Multiple minor fixes/improvements to align with upstream OpenThread changes.
- Sockets:

  - Added support for `shutdown()` function.
  - Fixed `sendmsg()` operation when TCP reported full transmission window.
  - Added support for `getpeername()` function.
  - Fixed userspace `accept()` argument validation.
  - Added support for [`SO_SNDBUF`](../connectivity/networking/api/sockets.md#c.SO_SNDBUF "SO_SNDBUF") and [`SO_RCVBUF`](../connectivity/networking/api/sockets.md#c.SO_RCVBUF "SO_RCVBUF") socket
    options.
  - Implemented `POLLOUT` reporting from `poll()` for STREAM
    sockets.
  - Implemented socket dispatcher for offloaded sockets. This module allows to
    use multiple offloaded socket implementations at the same time.
  - Introduced a common socket priority for offloaded sockets
    ([`CONFIG_NET_SOCKETS_OFFLOAD_PRIORITY`](../kconfig.md#CONFIG_NET_SOCKETS_OFFLOAD_PRIORITY "CONFIG_NET_SOCKETS_OFFLOAD_PRIORITY")).
  - Moved socket offloading out of experimental.
- TCP:

  - Implemented receive window handling.
  - Implemented zero-window probe processing and sending.
  - Improved TCP stack throughput over loopback interface.
  - Fixed possible transmission window overflow in case of TCP retransmissions.
    This could led to TX buffer starvation when TCP entered retransmission mode.
  - Updated `FIN_TIMEOUT` delay to correctly reflect time needed for
    all FIN packet retransmissions.
  - Added proper error reporting from TCP to upper layers. This solves the
    problem of connection errors being reported to the application as graceful
    connection shutdown.
  - Added a mechanism which allows upper layers to monitor the TCP transmission
    window availability. This allows to improve throughput greatly in low-buffer
    scenarios.
- TLS:

  - Added [`TLS_SESSION_CACHE`](../connectivity/networking/api/sockets.md#c.TLS_SESSION_CACHE "TLS_SESSION_CACHE") and [`TLS_SESSION_CACHE_PURGE`](../connectivity/networking/api/sockets.md#c.TLS_SESSION_CACHE_PURGE "TLS_SESSION_CACHE_PURGE")
    socket options which allow to control session caching on a socket.
  - Fixed [`TLS_CIPHERSUITE_LIST`](../connectivity/networking/api/sockets.md#c.TLS_CIPHERSUITE_LIST "TLS_CIPHERSUITE_LIST") socket option, which did not set the
    cipher list on a socket correctly.

## USB

- Moved USB device stack code to own directory in preparation for upcoming
  rework of USB support.

## Build System

- The build system’s internals have been completely overhauled for increased
  modularity. This makes it easier to reuse individual components through the
  Zephyr CMake package mechanism.

  With the improved Zephyr CMake package, the following examples are now possible:

  - `find_package(Zephyr)`: load a standard build system, as before
  - `find_package(Zephyr COMPONENTS unittest)`: load a specific unittest
    build component
  - `find_package(Zephyr COMPONENTS dts)`: only load the dts module and its
    direct dependencies
  - `find_package(Zephyr COMPONENTS extensions west zephyr_module)`: load
    multiple specific modules and their dependencies

  Some use cases that this work intends to enable are:

  - The sysbuild proposal: [Zephyr sysbuild / multi image #40555](https://github.com/zephyrproject-rtos/zephyr/pull/40555)
  - Running Zephyr CMake configure stages individually. One example is only
    processing the devicetree steps of the build system, while skipping the
    rest. This is a required feature for extending twister to do test case
    filtering based on the devicetree contents without invoking a complete
    CMake configuration.

  For more details, see [cmake/package\_helper.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/cmake/package_helper.cmake).
- A new Zephyr SDK has been created which now supports macOS and Windows in
  addition to Linux platforms.

  For more information, see: [https://github.com/zephyrproject-rtos/sdk-ng](https://github.com/zephyrproject-rtos/sdk-ng)

## Devicetree

- API

  - New macros for creating tokens in C from strings in the devicetree:
    [`DT_STRING_UPPER_TOKEN_OR`](../build/dts/api/api.md#c.DT_STRING_UPPER_TOKEN_OR "DT_STRING_UPPER_TOKEN_OR"), [`DT_INST_STRING_TOKEN`](../build/dts/api/api.md#c.DT_INST_STRING_TOKEN "DT_INST_STRING_TOKEN"),
    [`DT_INST_STRING_UPPER_TOKEN`](../build/dts/api/api.md#c.DT_INST_STRING_UPPER_TOKEN "DT_INST_STRING_UPPER_TOKEN"),
    [`DT_INST_STRING_UPPER_TOKEN_OR`](../build/dts/api/api.md#c.DT_INST_STRING_UPPER_TOKEN_OR "DT_INST_STRING_UPPER_TOKEN_OR")
  - [CAN](../build/dts/api/api.md#devicetree-can-api): new
- Bindings

  - Several new bindings were created to support [Pin Control](../hardware/pinctrl/index.md#pinctrl-guide) driver API implementations. This also affected many
    peripheral bindings, which now support `pinctrl-0`, `pinctrl-1`, …,
    and `pinctrl-names` properties used to configure peripheral pin
    assignments in different system states, such as active and low-power
    states.

    In some cases, this resulted in the removal of old bindings, or other
    backwards incompatible changes affecting users of the old bindings. These
    changes include:

    - [`atmel,sam-pinctrl`](../build/dts/api/bindings/pinctrl/atmel%2Csam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl) and [`atmel,sam0-pinctrl`](../build/dts/api/bindings/pinctrl/atmel%2Csam0-pinctrl.md#std-dtcompatible-atmel-sam0-pinctrl)
      have been adapted to the new pinctrl bindings interface
    - [`espressif,esp32-pinctrl`](../build/dts/api/bindings/pinctrl/espressif%2Cesp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) has replaced `espressif,esp32-pinmux`
    - [`ite,it8xxx2-pinctrl`](../build/dts/api/bindings/pinctrl/ite%2Cit8xxx2-pinctrl.md#std-dtcompatible-ite-it8xxx2-pinctrl) and
      [`ite,it8xxx2-pinctrl-func`](../build/dts/api/bindings/pinctrl/ite%2Cit8xxx2-pinctrl-func.md#std-dtcompatible-ite-it8xxx2-pinctrl-func) have replaced
      `ite,it8xxx2-pinmux` and `ite,it8xxx2-pinctrl-conf`
    - [`microchip,xec-pinctrl`](../build/dts/api/bindings/pinctrl/microchip%2Cxec-pinctrl.md#std-dtcompatible-microchip-xec-pinctrl): new
    - [`nuvoton,npcx-pinctrl`](../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-pinctrl.md#std-dtcompatible-nuvoton-npcx-pinctrl): new
    - [`nxp,kinetis-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Ckinetis-pinctrl.md#std-dtcompatible-nxp-kinetis-pinctrl) has replaced the `nxp,kinetis-port-pins` property found in the `nxp,kinetis-pinmux` binding.
    - [`nxp,mcux-rt-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Cmcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl),
      [`nxp,mcux-rt11xx-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Cmcux-rt11xx-pinctrl.md#std-dtcompatible-nxp-mcux-rt11xx-pinctrl),
      [`nxp,lpc-iocon-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Clpc-iocon-pinctrl.md#std-dtcompatible-nxp-lpc-iocon-pinctrl), [`nxp,rt-iocon-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Crt-iocon-pinctrl.md#std-dtcompatible-nxp-rt-iocon-pinctrl),
      [`nxp,lpc11u6x-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Clpc11u6x-pinctrl.md#std-dtcompatible-nxp-lpc11u6x-pinctrl), [`nxp,imx7d-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Cimx7d-pinctrl.md#std-dtcompatible-nxp-imx7d-pinctrl),
      [`nxp,imx8m-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Cimx8m-pinctrl.md#std-dtcompatible-nxp-imx8m-pinctrl), [`nxp,imx8mp-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Cimx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) and
      [`nxp,imx-iomuxc`](../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc): new
    - [`openisa,rv32m1-pinctrl`](../build/dts/api/bindings/pinctrl/openisa%2Crv32m1-pinctrl.md#std-dtcompatible-openisa-rv32m1-pinctrl): new
    - [`sifive,pinctrl`](../build/dts/api/bindings/pinctrl/sifive%2Cpinctrl.md#std-dtcompatible-sifive-pinctrl) has replaced `sifive,iof`
    - [`telink,b91-pinctrl`](../build/dts/api/bindings/pinctrl/telink%2Cb91-pinctrl.md#std-dtcompatible-telink-b91-pinctrl) has replaced `telink,b91-pinmux`
    - [`ti,cc13xx-cc26xx-pinctrl`](../build/dts/api/bindings/pinctrl/ti%2Ccc13xx-cc26xx-pinctrl.md#std-dtcompatible-ti-cc13xx-cc26xx-pinctrl) has replaced `ti,cc13xx-cc26xx-pinmux`
  - PWM bindings now generally have `#pwm-cells` set to 3, not 2 as it was in
    previous releases. This was done to follow the Linux convention that each
    PWM specifier should contain a channel, period, and flags cell, in that
    order. See pull request [#44523](https://github.com/zephyrproject-rtos/zephyr/pull/44523) for more
    details on this change and its purpose.
  - Some bindings had their [compatible properties](../build/dts/intro-syntax-structure.md#dt-important-props)
    renamed:

    - [`nxp,imx-elcdif`](../build/dts/api/bindings/display/nxp%2Cimx-elcdif.md#std-dtcompatible-nxp-imx-elcdif) has replaced `fsl,imx6sx-lcdif`
    - [`nxp,imx-gpr`](../build/dts/api/bindings/pinctrl/nxp%2Cimx-gpr.md#std-dtcompatible-nxp-imx-gpr) has replaced `nxp,imx-pinmux`
    - [`nordic,nrf-wdt`](../build/dts/api/bindings/watchdog/nordic%2Cnrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) has replaced `nordic,nrf-watchdog`
    - `bosch,m_can-base` has replaced `bosch,m-can-base`
    - [`nxp,imx-usdhc`](../build/dts/api/bindings/sdhc/nxp%2Cimx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) has replaced `nxp,imx-sdhc`
  - Bindings with `resets` (and optionally `reset-names`) properties were
    added to support the [Reset Controller](../hardware/peripherals/reset.md#reset-api) API. See the list of new bindings
    below for some examples.
  - The `zephyr,memory-region-mpu` property can be set to generate MPU
    regions from devicetree nodes. See commit [b91d21d32c](https://github.com/zephyrproject-rtos/zephyr/commit/b91d21d32ccc312558babe2cc363afbe44ea2de2)
  - The generic [dts/bindings/can/can-controller.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/can/can-controller.yaml) include
    file used for defining CAN controller bindings no longer contains a `bus:
    yaml` statement. This was unused in upstream Zephyr; out of tree bindings
    relying on this will need updates.
  - Bindings for ADC controller nodes can now use a child binding to specify
    the initial configuration of individual channels in devicetree. See pull
    request [43030](https://github.com/zephyrproject-rtos/zephyr/pull/43030)
    for details.
  - New bindings for the following compatible properties were added:

    - [`arduino-nano-header-r3`](../build/dts/api/bindings/gpio/arduino-nano-header-r3.md#std-dtcompatible-arduino-nano-header-r3)
    - [`arm,cortex-r52`](../build/dts/api/bindings/cpu/arm%2Ccortex-r52.md#std-dtcompatible-arm-cortex-r52)
    - [`atmel,sam-rstc`](../build/dts/api/bindings/hwinfo/atmel%2Csam-rstc.md#std-dtcompatible-atmel-sam-rstc)
    - [`can-transceiver-gpio`](../build/dts/api/bindings/phy/can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio) (see also [CAN](../build/dts/api/api.md#devicetree-can-api))
    - [`gd,gd32-spi`](../build/dts/api/bindings/spi/gd%2Cgd32-spi.md#std-dtcompatible-gd-gd32-spi)
    - [`hynitron,cst816s`](../build/dts/api/bindings/input/hynitron%2Ccst816s.md#std-dtcompatible-hynitron-cst816s)
    - `intel,cavs-gpdma`
    - `intel,cavs-hda-host-in` and `intel,cavs-hda-host-out`
    - `intel,cavs-hda-link-in` and `intel,cavs-hda-link-out`
    - [`intel,ssp-dai`](../build/dts/api/bindings/i2s/intel%2Cssp-dai.md#std-dtcompatible-intel-ssp-dai)
    - [`intel,ssp-sspbase`](../build/dts/api/bindings/i2s/intel%2Cssp-sspbase.md#std-dtcompatible-intel-ssp-sspbase)
    - [`invensense,icm42670`](../build/dts/api/bindings/sensor/invensense%2Cicm42670.md#std-dtcompatible-invensense-icm42670)
    - [`ite,enhance-i2c`](../build/dts/api/bindings/i2c/ite%2Cenhance-i2c.md#std-dtcompatible-ite-enhance-i2c)
    - [`ite,it8xxx2-vcmp`](../build/dts/api/bindings/sensor/ite%2Cit8xxx2-vcmp.md#std-dtcompatible-ite-it8xxx2-vcmp)
    - [`ite,it8xxx2-wuc`](../build/dts/api/bindings/interrupt-controller/ite%2Cit8xxx2-wuc.md#std-dtcompatible-ite-it8xxx2-wuc) and [`ite,it8xxx2-wuc-map`](../build/dts/api/bindings/interrupt-controller/ite%2Cit8xxx2-wuc-map.md#std-dtcompatible-ite-it8xxx2-wuc-map)
    - `ite,peci-it8xxx2`
    - [`maxim,max31875`](../build/dts/api/bindings/sensor/maxim%2Cmax31875.md#std-dtcompatible-maxim-max31875)
    - [`microchip,cap1203`](../build/dts/api/bindings/input/microchip%2Ccap1203.md#std-dtcompatible-microchip-cap1203)
    - [`microchip,mcp4728`](../build/dts/api/bindings/dac/microchip%2Cmcp4728.md#std-dtcompatible-microchip-mcp4728)
    - [`microchip,mpfs-qspi`](../build/dts/api/bindings/spi/microchip%2Cmpfs-qspi.md#std-dtcompatible-microchip-mpfs-qspi)
    - [`microchip,xec-bbram`](../build/dts/api/bindings/memory-controllers/microchip%2Cxec-bbram.md#std-dtcompatible-microchip-xec-bbram)
    - [`motorola,mc146818`](../build/dts/api/bindings/rtc/motorola%2Cmc146818.md#std-dtcompatible-motorola-mc146818)
    - [`nordic,nrf-acl`](../build/dts/api/bindings/arm/nordic%2Cnrf-acl.md#std-dtcompatible-nordic-nrf-acl)
    - [`nordic,nrf-bprot`](../build/dts/api/bindings/arm/nordic%2Cnrf-bprot.md#std-dtcompatible-nordic-nrf-bprot)
    - [`nordic,nrf-ccm`](../build/dts/api/bindings/crypto/nordic%2Cnrf-ccm.md#std-dtcompatible-nordic-nrf-ccm)
    - [`nordic,nrf-comp`](../build/dts/api/bindings/sensor/nordic%2Cnrf-comp.md#std-dtcompatible-nordic-nrf-comp)
    - [`nordic,nrf-ctrlapperi`](../build/dts/api/bindings/arm/nordic%2Cnrf-ctrlapperi.md#std-dtcompatible-nordic-nrf-ctrlapperi)
    - [`nordic,nrf-dcnf`](../build/dts/api/bindings/arm/nordic%2Cnrf-dcnf.md#std-dtcompatible-nordic-nrf-dcnf)
    - [`nordic,nrf-gpio-forwarder`](../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio-forwarder.md#std-dtcompatible-nordic-nrf-gpio-forwarder)
    - [`nordic,nrf-lpcomp`](../build/dts/api/bindings/sensor/nordic%2Cnrf-lpcomp.md#std-dtcompatible-nordic-nrf-lpcomp)
    - [`nordic,nrf-mpu`](../build/dts/api/bindings/arm/nordic%2Cnrf-mpu.md#std-dtcompatible-nordic-nrf-mpu)
    - [`nordic,nrf-mutex`](../build/dts/api/bindings/arm/nordic%2Cnrf-mutex.md#std-dtcompatible-nordic-nrf-mutex)
    - [`nordic,nrf-mwu`](../build/dts/api/bindings/arm/nordic%2Cnrf-mwu.md#std-dtcompatible-nordic-nrf-mwu)
    - [`nordic,nrf-nfct`](../build/dts/api/bindings/net/wireless/nordic%2Cnrf-nfct.md#std-dtcompatible-nordic-nrf-nfct)
    - [`nordic,nrf-oscillators`](../build/dts/api/bindings/clock/nordic%2Cnrf-oscillators.md#std-dtcompatible-nordic-nrf-oscillators)
    - [`nordic,nrf-ppi`](../build/dts/api/bindings/misc/nordic%2Cnrf-ppi.md#std-dtcompatible-nordic-nrf-ppi)
    - [`nordic,nrf-reset`](../build/dts/api/bindings/arm/nordic%2Cnrf-reset.md#std-dtcompatible-nordic-nrf-reset)
    - [`nordic,nrf-swi`](../build/dts/api/bindings/arm/nordic%2Cnrf-swi.md#std-dtcompatible-nordic-nrf-swi)
    - [`nordic,nrf-usbreg`](../build/dts/api/bindings/power/nordic%2Cnrf-usbreg.md#std-dtcompatible-nordic-nrf-usbreg)
    - [`nuvoton,adc-cmp`](../build/dts/api/bindings/sensor/nuvoton%2Cadc-cmp.md#std-dtcompatible-nuvoton-adc-cmp)
    - [`nxp,imx-mipi-dsi`](../build/dts/api/bindings/mipi-dsi/nxp%2Cimx-mipi-dsi.md#std-dtcompatible-nxp-imx-mipi-dsi)
    - [`nxp,imx-qtmr`](../build/dts/api/bindings/counter/nxp%2Cimx-qtmr.md#std-dtcompatible-nxp-imx-qtmr)
    - [`nxp,imx-tmr`](../build/dts/api/bindings/counter/nxp%2Cimx-tmr.md#std-dtcompatible-nxp-imx-tmr)
    - [`raspberrypi,pico-reset`](../build/dts/api/bindings/reset/raspberrypi%2Cpico-reset.md#std-dtcompatible-raspberrypi-pico-reset)
    - [`raspberrypi,pico-usbd`](../build/dts/api/bindings/usb/raspberrypi%2Cpico-usbd.md#std-dtcompatible-raspberrypi-pico-usbd)
    - [`raydium,rm68200`](../build/dts/api/bindings/display/raydium%2Crm68200.md#std-dtcompatible-raydium-rm68200)
    - `riscv,sifive-e31`, `riscv,sifive-e51`,
      and `riscv,sifive-s7` CPU bindings
    - [`seeed,grove-lcd-rgb`](../build/dts/api/bindings/misc/seeed%2Cgrove-lcd-rgb.md#std-dtcompatible-seeed-grove-lcd-rgb)
    - [`st,lsm6dso32`](../build/dts/api/compatibles/st%2Clsm6dso32.md#std-dtcompatible-st-lsm6dso32)
    - [`st,stm32-clock-mux`](../build/dts/api/bindings/clock/st%2Cstm32-clock-mux.md#std-dtcompatible-st-stm32-clock-mux)
    - [`st,stm32-fmc-nor-psram`](../build/dts/api/bindings/memory-controllers/st%2Cstm32-fmc-nor-psram.md#std-dtcompatible-st-stm32-fmc-nor-psram)
    - [`st,stm32-lse-clock`](../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock)
    - [`st,stm32-ltdc`](../build/dts/api/bindings/display/st%2Cstm32-ltdc.md#std-dtcompatible-st-stm32-ltdc)
    - [`st,stm32-ospi`](../build/dts/api/bindings/ospi/st%2Cstm32-ospi.md#std-dtcompatible-st-stm32-ospi) and [`st,stm32-ospi-nor`](../build/dts/api/bindings/flash_controller/st%2Cstm32-ospi-nor.md#std-dtcompatible-st-stm32-ospi-nor)
    - [`st,stm32h7-fmc`](../build/dts/api/bindings/memory-controllers/st%2Cstm32h7-fmc.md#std-dtcompatible-st-stm32h7-fmc)
    - TI ADS ADCs: [`ti,ads1013`](../build/dts/api/bindings/adc/ti%2Cads1013.md#std-dtcompatible-ti-ads1013), [`ti,ads1015`](../build/dts/api/bindings/adc/ti%2Cads1015.md#std-dtcompatible-ti-ads1015),
      [`ti,ads1113`](../build/dts/api/bindings/adc/ti%2Cads1113.md#std-dtcompatible-ti-ads1113), [`ti,ads1114`](../build/dts/api/bindings/adc/ti%2Cads1114.md#std-dtcompatible-ti-ads1114),
      [`ti,ads1115`](../build/dts/api/bindings/adc/ti%2Cads1115.md#std-dtcompatible-ti-ads1115), [`ti,ads1014`](../build/dts/api/bindings/adc/ti%2Cads1014.md#std-dtcompatible-ti-ads1014)
    - [`ti,tlc5971`](../build/dts/api/bindings/led_strip/ti%2Ctlc5971.md#std-dtcompatible-ti-tlc5971)
    - [`xlnx,fpga`](../build/dts/api/bindings/fpga/xlnx%2Cfpga.md#std-dtcompatible-xlnx-fpga)
    - [`xlnx,ps-gpio`](../build/dts/api/bindings/gpio/xlnx%2Cps-gpio.md#std-dtcompatible-xlnx-ps-gpio) and [`xlnx,ps-gpio-bank`](../build/dts/api/bindings/gpio/xlnx%2Cps-gpio-bank.md#std-dtcompatible-xlnx-ps-gpio-bank)
    - [`zephyr,bt-hci-entropy`](../build/dts/api/bindings/bluetooth/zephyr%2Cbt-hci-entropy.md#std-dtcompatible-zephyr-bt-hci-entropy)
    - [`zephyr,ipc-icmsg`](../build/dts/api/bindings/ipc/zephyr%2Cipc-icmsg.md#std-dtcompatible-zephyr-ipc-icmsg)
    - [`zephyr,memory-region`](../build/dts/api/bindings/base/zephyr%2Cmemory-region.md#std-dtcompatible-zephyr-memory-region)
    - [`zephyr,sdhc-spi-slot`](../build/dts/api/bindings/sdhc/zephyr%2Csdhc-spi-slot.md#std-dtcompatible-zephyr-sdhc-spi-slot)
  - Bindings for the following compatible properties were removed:

    - `bosch,m-can`
    - `nxp,imx-usdhc`
    - `shared-multi-heap`
    - `snps,creg-gpio-mux-hsdk`
    - `snps,designware-pwm`
    - `zephyr,mmc-spi-slot`
  - Numerous other additional properties were added to bindings throughout the tree.

## Libraries / Subsystems

- C Library

  - Minimal libc

    - Added `[U]INT_{FAST,LEAST}N_{MIN,MAX}` minimum and maximum value
      macros in `stdint.h`.
    - Added `PRIx{FAST,LEAST}N` and `PRIxMAX` format specifier macros in
      `inttypes.h`.
    - Fixed `gmtime()` access fault when userspace is enabled and
      `gmtime()` is called from a user mode thread. This function can be
      safely called from both kernel and user mode threads.
  - Newlib

    - Fixed access fault when calling the newlib math functions from a user
      mode thread. All `libm.a` globals are now placed into the
      `z_libc_partition` when userspace is enabled.
- C++ Subsystem

  - Renamed all C++ source and header files to use the `cpp` and `hpp`
    extensions, respectively. All Zephyr upstream C++ source and header files
    are now required to use these extensions.
- Management

  - MCUMGR has been migrated from using TinyCBOR, for CBOR encoding, to zcbor.
  - MCUMGR `CONFIG_FS_MGMT_UL_CHUNK_SIZE` and
    `CONFIG_IMG_MGMT_UL_CHUNK_SIZE` have been deprecated as,
    with the introduction of zcbor, it is no longer needed to use an intermediate
    buffer to copy data out of CBOR encoded buffer. The file/image chunk size
    is now limited by `CONFIG_MCUMGR_BUF_SIZE` minus all the
    other command required variables.
  - Added support for MCUMGR Parameters command, which can be used to obtain
    MCUMGR parameters; `CONFIG_OS_MGMT_MCUMGR_PARAMS` enables
    the command.
  - Added mcumgr fs handler for getting file status which returns file size;
    controlled with `CONFIG_FS_MGMT_FILE_STATUS`
  - Added mcumgr fs handler for getting file hash/checksum, with support for
    IEEE CRC32 and SHA256, the following Kconfig options have been added to
    control the addition:

    - `CONFIG_FS_MGMT_CHECKSUM_HASH` to enable the command;
    - `CONFIG_FS_MGMT_CHECKSUM_HASH_CHUNK_SIZE` that sets size
      of buffer (stack memory) used for calculation:

      - `CONFIG_FS_MGMT_CHECKSUM_IEEE_CRC32` enables support for
        IEEE CRC32.
      - `CONFIG_FS_MGMT_HASH_SHA256` enables SHA256 hash support.
      - When hash/checksum query to mcumgr does not specify a type, then the order
        of preference (most priority) is CRC32 followed by SHA256.
  - Added mcumgr os hook to allow an application to accept or decline a reset
    request; `CONFIG_OS_MGMT_RESET_HOOK` enables the callback.
  - Added mcumgr fs hook to allow an application to accept or decline a file
    read/write request; `CONFIG_FS_MGMT_FILE_ACCESS_HOOK`
    enables the feature which then needs to be registered by the application.
  - Added supplied image header to mcumgr img upload callback parameter list
    which allows the application to inspect it to determine if it should be
    allowed or declined.
  - Made the `img_mgmt_vercmp()` function public to allow application-
    level comparison of image versions.
  - mcumgr will now only return `MGMT_ERR_ENOMEM` when it fails to allocate
    a memory buffer for request processing, when previously it would wrongly
    report this error when the SMP response failed to fit into a buffer;
    now when encoding of response fails `MGMT_ERR_EMSGSIZE` will be
    reported. This addresses issue [GitHub #44535](https://github.com/zephyrproject-rtos/zephyr/issues/44535).
  - Added `CONFIG_IMG_MGMT_USE_HEAP_FOR_FLASH_IMG_CONTEXT` that
    allows user to select whether the heap will be used for flash image context,
    when heap pool is configured. Previously usage of heap has been implicit,
    with no control from a developer, causing issues reported by [GitHub #44214](https://github.com/zephyrproject-rtos/zephyr/issues/44214).
    The default, implicit, behaviour has not been kept and the above
    Kconfig option needs to be selected to keep previous behaviour.
- SD Subsystem

  - Added the SD subsystem, which is used by the
    [disk access api](../services/storage/disk/access.md#disk-access-api) to interact with connected SD cards.
    This subsystem uses the [SDHC api](../hardware/peripherals/sdhc.md#sdhc-api) to interact with the SD
    host controller the SD device is connected to.
- Power management

  - Added [`CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC`](../kconfig.md#CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC "CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC").
    This option enables support for dynamically bind devices to a Power Domain. The
    memory required to dynamically bind devices is pre-allocated at build time and
    is based on the number of devices set in
    [`CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC_NUM`](../kconfig.md#CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC_NUM "CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC_NUM"). The API introduced
    to use this feature are:

    - [`pm_device_power_domain_add()`](../services/pm/api/index.md#c.pm_device_power_domain_add "pm_device_power_domain_add")
    - [`pm_device_power_domain_remove()`](../services/pm/api/index.md#c.pm_device_power_domain_remove "pm_device_power_domain_remove")
  - The default policy was renamed from `PM_POLICY_RESIDENCY` to
    `PM_POLICY_DEFAULT`, and `PM_POLICY_APP` was renamed to
    `PM_POLICY_CUSTOM`.
  - The following functions were renamed:

    - `pm_power_state_next_get()` is now [`pm_state_next_get()`](../services/pm/api/index.md#c.pm_state_next_get "pm_state_next_get")
    - `pm_power_state_force()` is now [`pm_state_force()`](../services/pm/api/index.md#c.pm_state_force "pm_state_force")
  - Removed the deprecated function `pm_device_state_set()`.
  - The state constraint APIs were moved (and renamed) to the policy
    API and accounts substates.

    - `pm_constraint_get()` is now [`pm_policy_state_lock_is_active()`](../services/pm/api/index.md#c.pm_policy_state_lock_is_active "pm_policy_state_lock_is_active")
    - `pm_constraint_set()` is now [`pm_policy_state_lock_get()`](../services/pm/api/index.md#c.pm_policy_state_lock_get "pm_policy_state_lock_get")
    - `pm_constraint_release()` is now [`pm_policy_state_lock_put()`](../services/pm/api/index.md#c.pm_policy_state_lock_put "pm_policy_state_lock_put")
  - Added a new API to set maximum latency requirements. The `DEFAULT` policy
    will account for latency when computing the next state.

    - [`pm_policy_latency_request_add()`](../services/pm/api/index.md#c.pm_policy_latency_request_add "pm_policy_latency_request_add")
    - [`pm_policy_latency_request_update()`](../services/pm/api/index.md#c.pm_policy_latency_request_update "pm_policy_latency_request_update")
    - [`pm_policy_latency_request_remove()`](../services/pm/api/index.md#c.pm_policy_latency_request_remove "pm_policy_latency_request_remove")
  - The API to set a device initial state was changed to be usable independently of
    [`CONFIG_PM_DEVICE_RUNTIME`](../kconfig.md#CONFIG_PM_DEVICE_RUNTIME "CONFIG_PM_DEVICE_RUNTIME").

    - `pm_device_runtime_init_suspended()` is now [`pm_device_init_suspended()`](../services/pm/api/index.md#c.pm_device_init_suspended "pm_device_init_suspended")
    - `pm_device_runtime_init_off()` is now [`pm_device_init_off()`](../services/pm/api/index.md#c.pm_device_init_off "pm_device_init_off")
- IPC

  - static\_vrings: Fixed work queue (WQ) initialization
  - static\_vrings: Introduced atomic helpers when accessing atomic\_t variables
  - static\_vrings: Moved to one WQ per instance
  - static\_vrings: Added “zephyr,priority” property in the DT to set the WQ priority of the instance
  - static\_vrings: Added configuration parameter to initialize shared memory to zero
  - Extended API with NOCOPY functions
  - static\_vrings: Added support for NOCOPY operations
  - Introduced inter core messaging backend (icmsg) that relies on simple inter core messaging buffer
- Logging

  - Added UART frontend which supports binary dictionary logging.
  - Added support for MIPI SyS-T catalog messages.
  - Added cAVS HDA backend.
- Shell

  - Added API for creating subcommands from multiple files using memory section approach:

    - [`SHELL_SUBCMD_SET_CREATE`](../services/shell/index.md#c.SHELL_SUBCMD_SET_CREATE "SHELL_SUBCMD_SET_CREATE") for creating a subcommand set.
    - [`SHELL_SUBCMD_COND_ADD`](../services/shell/index.md#c.SHELL_SUBCMD_COND_ADD "SHELL_SUBCMD_COND_ADD") and [`SHELL_SUBCMD_ADD`](../services/shell/index.md#c.SHELL_SUBCMD_ADD "SHELL_SUBCMD_ADD") for adding subcommands
      to the set.

## HALs

- Atmel

  - Added devicetree bindings, documentation, and scripts to support
    state-based pin control (`pinctrl`) API.
  - Imported new SoC header files for:

    - SAML21
    - SAMR34
    - SAMR35
- GigaDevice

  - Fixed GD32\_REMAP\_MSK macro
  - Fixed gd32f403z pc3 missing pincodes
- STM32:

  - Updated stm32f4 to new STM32cube version V1.27.0
  - Updated stm32f7 to new STM32cube version V1.16.2
  - Updated stm32g4 to new STM32cube version V1.5.0
  - Updated stm32h7 to new STM32cube version V1.10.0
  - Updated stm32l4 to new STM32cube version V1.17.1
  - Updated stm32u5 to new STM32cube version V1.1.0
  - Updated stm32wb to new STM32cube version V1.13.2 (including hci lib)

## MCUboot

- Added initial support for devices with a write alignment larger than 8B.
- Added an option for entering serial recovery mode with a timeout. See `CONFIG_BOOT_SERIAL_WAIT_FOR_DFU`.
- Used a smaller sha256 implementation.
- Added support for the echo command in serial recovery. See `CONFIG_BOOT_MGMT_ECHO`.
- Fixed image decryption for SoC flash with page sizes larger than 1024 B in single loader mode.
- Fixed a possible output buffer overflow in serial recovery.
- Added a GitHub workflow for verifying integration with Zephyr.
- Removed deprecated `DT_CHOSEN_ZEPHYR_FLASH_CONTROLLER_LABEL`.
- Fixed usage of `CONFIG_LOG_IMMEDIATE`.

## Trusted Firmware-m

- Updated to TF-M 1.6.0

## Documentation

- Reorganised and consolidated documentation for improved readability and
  user experience.
- Replaced the existing statically rendered Kconfig documentation with the new
  Kconfig documentation engine that dynamically renders the Kconfig contents
  for improved search performance.
- Added a ‘Language Support’ sub-category under the ‘Developing with Zephyr’
  category that provides details regarding C and C++ language and standard
  library support status.
- Added a ‘Toolchain’ sub-category under the ‘Developing with Zephyr’ category
  that lists all supported toolchains along with instructions for how to configure
  and use them.

## Tests and Samples

> - A dedicated framework was added to test the STM32 clock\_control driver.

## Issue summary

This section lists security vulnerabilities, other known bugs, and all issues
addressed during the v3.1.0 development period.

### Security Vulnerability Related

The following CVEs are addressed by this release:

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

- CVE-2022-1841: Under embargo until 2022-08-18
- CVE-2022-1042: Under embargo until 2022-06-19
- CVE-2022-1041: Under embargo until 2022-06-19

### Known bugs

- [GitHub #23302](https://github.com/zephyrproject-rtos/zephyr/issues/23302) - Poor TCP performance
- [GitHub #25917](https://github.com/zephyrproject-rtos/zephyr/issues/25917) - Bluetooth: Deadlock with TX of ACL data and HCI commands (command blocked by data)
- [GitHub #30348](https://github.com/zephyrproject-rtos/zephyr/issues/30348) - XIP can’t be enabled with ARC MWDT toolchain
- [GitHub #31298](https://github.com/zephyrproject-rtos/zephyr/issues/31298) - tests/kernel/gen\_isr\_table failed on hsdk and nsim\_hs\_smp sometimes
- [GitHub #33747](https://github.com/zephyrproject-rtos/zephyr/issues/33747) - gptp does not work well on NXP rt series platform
- [GitHub #34226](https://github.com/zephyrproject-rtos/zephyr/issues/34226) - Compile error when building civetweb samples for posix\_native
- [GitHub #34600](https://github.com/zephyrproject-rtos/zephyr/issues/34600) - Bluetooth: L2CAP: Deadlock when there are no free buffers while transmitting on multiple channels
- [GitHub #36358](https://github.com/zephyrproject-rtos/zephyr/issues/36358) - Potential issue with CMAKE\_OBJECT\_PATH\_MAX
- [GitHub #37193](https://github.com/zephyrproject-rtos/zephyr/issues/37193) - mcumgr: Probably incorrect error handling with udp backend
- [GitHub #37704](https://github.com/zephyrproject-rtos/zephyr/issues/37704) - hello world doesn’t work on qemu\_arc\_em when CONFIG\_ISR\_STACK\_SIZE=1048510
- [GitHub #37731](https://github.com/zephyrproject-rtos/zephyr/issues/37731) - Bluetooth: hci samples: Unable to allocate command buffer
- [GitHub #38041](https://github.com/zephyrproject-rtos/zephyr/issues/38041) - Logging-related tests fails on qemu\_arc\_hs6x
- [GitHub #38544](https://github.com/zephyrproject-rtos/zephyr/issues/38544) - drivers: wifi: esWIFI: Regression due to 35815
- [GitHub #38654](https://github.com/zephyrproject-rtos/zephyr/issues/38654) - drivers: modem: bg9x: Has no means to update size of received packet.
- [GitHub #38880](https://github.com/zephyrproject-rtos/zephyr/issues/38880) - ARC: ARCv2: qemu\_arc\_em / qemu\_arc\_hs don’t work with XIP disabled
- [GitHub #38947](https://github.com/zephyrproject-rtos/zephyr/issues/38947) - Issue with SMP commands sent over the UART
- [GitHub #39347](https://github.com/zephyrproject-rtos/zephyr/issues/39347) - Static object constructors do not execute on the NATIVE\_POSIX\_64 target
- [GitHub #39888](https://github.com/zephyrproject-rtos/zephyr/issues/39888) - STM32L4: usb-hid: regression in hal 1.17.0
- [GitHub #40023](https://github.com/zephyrproject-rtos/zephyr/issues/40023) - Build fails for `native_posix` board when using C++ <atomic> header
- [GitHub #41281](https://github.com/zephyrproject-rtos/zephyr/issues/41281) - Style Requirements Seem to Be Inconsistent with Uncrustify Configuration
- [GitHub #41286](https://github.com/zephyrproject-rtos/zephyr/issues/41286) - Bluetooth SDP: When the SDP attribute length is greater than SDP\_MTU, the attribute is discarded
- [GitHub #41606](https://github.com/zephyrproject-rtos/zephyr/issues/41606) - stm32u5: Re-implement VCO input and EPOD configuration
- [GitHub #41622](https://github.com/zephyrproject-rtos/zephyr/issues/41622) - Infinite mutual recursion when SMP and ATOMIC\_OPERATIONS\_C are set
- [GitHub #41822](https://github.com/zephyrproject-rtos/zephyr/issues/41822) - BLE IPSP sample cannot handle large ICMPv6 Echo Request
- [GitHub #42030](https://github.com/zephyrproject-rtos/zephyr/issues/42030) - can: “bosch,m-can-base”: Warning “missing or empty reg/ranges property”
- [GitHub #42134](https://github.com/zephyrproject-rtos/zephyr/issues/42134) - TLS handshake error using DTLS on updatehub
- [GitHub #42574](https://github.com/zephyrproject-rtos/zephyr/issues/42574) - i2c: No support for bus recovery imx.rt and or timeout on bus busy
- [GitHub #42629](https://github.com/zephyrproject-rtos/zephyr/issues/42629) - stm32g0: Device hang/hard fault with AT45 + `CONFIG_PM_DEVICE`
- [GitHub #42842](https://github.com/zephyrproject-rtos/zephyr/issues/42842) - BBRAM API is missing a documentation reference page
- [GitHub #43115](https://github.com/zephyrproject-rtos/zephyr/issues/43115) - Data corruption in STM32 SPI driver in Slave Mode
- [GitHub #43246](https://github.com/zephyrproject-rtos/zephyr/issues/43246) - Bluetooth: Host: Deadlock with Mesh and Ext Adv on native\_posix
- [GitHub #43249](https://github.com/zephyrproject-rtos/zephyr/issues/43249) - MBEDTLS\_ECP\_C not build when MBEDTLS\_USE\_PSA\_CRYPTO
- [GitHub #43308](https://github.com/zephyrproject-rtos/zephyr/issues/43308) - driver: serial: stm32: uart will lost data when use dma mode[async mode]
- [GitHub #43390](https://github.com/zephyrproject-rtos/zephyr/issues/43390) - gPTP broken in Zephyr 3.0
- [GitHub #43515](https://github.com/zephyrproject-rtos/zephyr/issues/43515) - reel\_board: failed to run tests/kernel/workq/work randomly
- [GitHub #43555](https://github.com/zephyrproject-rtos/zephyr/issues/43555) - Variables not properly initialized when using data relocation with SDRAM
- [GitHub #43562](https://github.com/zephyrproject-rtos/zephyr/issues/43562) - Setting and/or documentation of Timer and counter use/requirements for Nordic Bluetooth driver
- [GitHub #43646](https://github.com/zephyrproject-rtos/zephyr/issues/43646) - mgmt/mcumgr/lib: OS taskstat may give shorter list than expected
- [GitHub #43655](https://github.com/zephyrproject-rtos/zephyr/issues/43655) - esp32c3: Connection fail loop
- [GitHub #43811](https://github.com/zephyrproject-rtos/zephyr/issues/43811) - ble: gatt: db\_hash\_work runs for too long and makes serial communication fail
- [GitHub #43828](https://github.com/zephyrproject-rtos/zephyr/issues/43828) - Intel CAVS: multiple tests under tests/boards/intel\_adsp/smoke are failing
- [GitHub #43836](https://github.com/zephyrproject-rtos/zephyr/issues/43836) - stm32: g0b1: RTT doesn’t work properly after stop mode
- [GitHub #43887](https://github.com/zephyrproject-rtos/zephyr/issues/43887) - SystemView tracing with STM32L0x fails to compile
- [GitHub #43910](https://github.com/zephyrproject-rtos/zephyr/issues/43910) - civetweb/http\_server - DEBUG\_OPTIMIZATIONS enabled
- [GitHub #43928](https://github.com/zephyrproject-rtos/zephyr/issues/43928) - pm: going to PM\_STATE\_SOFT\_OFF in pm\_policy\_next\_state causes assert in some cases
- [GitHub #43933](https://github.com/zephyrproject-rtos/zephyr/issues/43933) - llvm: twister: multiple errors with set but unused variables
- [GitHub #44062](https://github.com/zephyrproject-rtos/zephyr/issues/44062) - Need a way to deal with stack size needed when running coverage report.
- [GitHub #44214](https://github.com/zephyrproject-rtos/zephyr/issues/44214) - mgmt/mcumgr/lib: Parasitic use of CONFIG\_HEAP\_MEM\_POOL\_SIZE in image management
- [GitHub #44219](https://github.com/zephyrproject-rtos/zephyr/issues/44219) - mgmt/mcumgr/lib: Incorrect processing of img\_mgmt\_impl\_write\_image\_data leaves mcumgr in broken state in case of error
- [GitHub #44228](https://github.com/zephyrproject-rtos/zephyr/issues/44228) - drivers: modem: bg9x: bug on cmd AT+QICSGP
- [GitHub #44324](https://github.com/zephyrproject-rtos/zephyr/issues/44324) - Compile error in byteorder.h
- [GitHub #44377](https://github.com/zephyrproject-rtos/zephyr/issues/44377) - ISO Broadcast/Receive sample not working with coded PHY
- [GitHub #44403](https://github.com/zephyrproject-rtos/zephyr/issues/44403) - MPU fault and `CONFIG_CMAKE_LINKER_GENERATOR`
- [GitHub #44410](https://github.com/zephyrproject-rtos/zephyr/issues/44410) - drivers: modem: shell: `modem send` doesn’t honor line ending in modem cmd handler
- [GitHub #44579](https://github.com/zephyrproject-rtos/zephyr/issues/44579) - MCC: Discovery cannot complete with success
- [GitHub #44622](https://github.com/zephyrproject-rtos/zephyr/issues/44622) - Microbit v2 board dts file for lsm303agr int line
- [GitHub #44725](https://github.com/zephyrproject-rtos/zephyr/issues/44725) - drivers: can: stm32: can\_add\_rx\_filter() does not respect CONFIG\_CAN\_MAX\_FILTER
- [GitHub #44898](https://github.com/zephyrproject-rtos/zephyr/issues/44898) - mgmt/mcumgr: Fragmentation of responses may cause mcumgr to drop successfully processed response
- [GitHub #44925](https://github.com/zephyrproject-rtos/zephyr/issues/44925) - intel\_adsp\_cavs25: multiple tests failed after running tests/boards/intel\_adsp
- [GitHub #44948](https://github.com/zephyrproject-rtos/zephyr/issues/44948) - cmsis\_dsp: transofrm: error during building cf64.fpu and rf64.fpu for mps2\_an521\_remote
- [GitHub #44996](https://github.com/zephyrproject-rtos/zephyr/issues/44996) - logging: transient strings are no longer duplicated correctly
- [GitHub #44998](https://github.com/zephyrproject-rtos/zephyr/issues/44998) - SMP shell exec command causes BLE stack breakdown if buffer size is too small to hold response
- [GitHub #45105](https://github.com/zephyrproject-rtos/zephyr/issues/45105) - ACRN: failed to run testcase tests/kernel/fifo/fifo\_timeout/
- [GitHub #45117](https://github.com/zephyrproject-rtos/zephyr/issues/45117) - drivers: clock\_control: clock\_control\_nrf
- [GitHub #45157](https://github.com/zephyrproject-rtos/zephyr/issues/45157) - cmake: Use of -ffreestanding disables many useful optimizations and compiler warnings
- [GitHub #45168](https://github.com/zephyrproject-rtos/zephyr/issues/45168) - rcar\_h3ulcb: failed to run test case tests/drivers/can/timing
- [GitHub #45169](https://github.com/zephyrproject-rtos/zephyr/issues/45169) - rcar\_h3ulcb: failed to run test case tests/drivers/can/api
- [GitHub #45218](https://github.com/zephyrproject-rtos/zephyr/issues/45218) - rddrone\_fmuk66: I2C configuration incorrect
- [GitHub #45222](https://github.com/zephyrproject-rtos/zephyr/issues/45222) - drivers: peci: user space handlers not building correctly
- [GitHub #45241](https://github.com/zephyrproject-rtos/zephyr/issues/45241) - (Probably) unnecessary branches in several modules
- [GitHub #45270](https://github.com/zephyrproject-rtos/zephyr/issues/45270) - CMake - TEST\_BIG\_ENDIAN
- [GitHub #45304](https://github.com/zephyrproject-rtos/zephyr/issues/45304) - drivers: can: CAN interfaces are brought up with default bitrate at boot, causing error frames if bus bitrate differs
- [GitHub #45315](https://github.com/zephyrproject-rtos/zephyr/issues/45315) - drivers: timer: nrf\_rtc\_timer: NRF boards take a long time to boot application in CONFIG\_TICKLESS\_KERNEL=n mode after OTA update
- [GitHub #45349](https://github.com/zephyrproject-rtos/zephyr/issues/45349) - ESP32: fails to chain-load sample/board/esp32/wifi\_station from MCUboot
- [GitHub #45374](https://github.com/zephyrproject-rtos/zephyr/issues/45374) - Creating the unicast group before both ISO connections have been configured might cause issue
- [GitHub #45441](https://github.com/zephyrproject-rtos/zephyr/issues/45441) - SPI NOR driver assume all SPI controller HW is implemnted in an identical way
- [GitHub #45509](https://github.com/zephyrproject-rtos/zephyr/issues/45509) - ipc: ipc\_icmsg: Can silently drop buffer if message is too big
- [GitHub #45532](https://github.com/zephyrproject-rtos/zephyr/issues/45532) - uart\_msp432p4xx\_poll\_in() seems to be a blocking function
- [GitHub #45564](https://github.com/zephyrproject-rtos/zephyr/issues/45564) - Zephyr does not boot with CONFIG\_PM=y
- [GitHub #45581](https://github.com/zephyrproject-rtos/zephyr/issues/45581) - samples: usb: mass: Sample.usb.mass\_flash\_fatfs fails on non-secure nrf5340dk
- [GitHub #45596](https://github.com/zephyrproject-rtos/zephyr/issues/45596) - samples: Code relocation nocopy sample has some unusual failure on nrf5340dk
- [GitHub #45647](https://github.com/zephyrproject-rtos/zephyr/issues/45647) - test: drivers: counter: Test passes even when no instances are found
- [GitHub #45666](https://github.com/zephyrproject-rtos/zephyr/issues/45666) - Building samples about BLE audio with nrf5340dk does not work
- [GitHub #45675](https://github.com/zephyrproject-rtos/zephyr/issues/45675) - testing.ztest.customized\_output: mismatch twister results in json/xml file
- [GitHub #45678](https://github.com/zephyrproject-rtos/zephyr/issues/45678) - Lorawan: Devnonce has already been used
- [GitHub #45760](https://github.com/zephyrproject-rtos/zephyr/issues/45760) - Running twister on new board files
- [GitHub #45774](https://github.com/zephyrproject-rtos/zephyr/issues/45774) - drivers: gpio: pca9555: Driver is writing to output port despite all pins having been configured as input
- [GitHub #45802](https://github.com/zephyrproject-rtos/zephyr/issues/45802) - Some tests reported as PASSED (device) but they were only build
- [GitHub #45807](https://github.com/zephyrproject-rtos/zephyr/issues/45807) - CivetWeb doesn’t build for CC3232SF
- [GitHub #45814](https://github.com/zephyrproject-rtos/zephyr/issues/45814) - Armclang build fails due to missing source file
- [GitHub #45842](https://github.com/zephyrproject-rtos/zephyr/issues/45842) - drivers: modem: uart\_mux errors after second call to gsm\_ppp\_start
- [GitHub #45844](https://github.com/zephyrproject-rtos/zephyr/issues/45844) - Not all bytes are downloaded with HTTP request
- [GitHub #45845](https://github.com/zephyrproject-rtos/zephyr/issues/45845) - tests: The failure test case number increase significantly in CMSIS DSP tests on ARM boards.
- [GitHub #45848](https://github.com/zephyrproject-rtos/zephyr/issues/45848) - tests: console harness: inaccuracy testcases report
- [GitHub #45866](https://github.com/zephyrproject-rtos/zephyr/issues/45866) - drivers/entropy: stm32: non-compliant RNG configuration on some MCUs
- [GitHub #45914](https://github.com/zephyrproject-rtos/zephyr/issues/45914) - test: tests/kernel/usage/thread\_runtime\_stats/ test fail
- [GitHub #45929](https://github.com/zephyrproject-rtos/zephyr/issues/45929) - up\_squared：failed to run test case tests/posix/common
- [GitHub #45951](https://github.com/zephyrproject-rtos/zephyr/issues/45951) - modem: ublox-sara-r4: outgoing datagrams are truncated if they do not fit MTU
- [GitHub #45953](https://github.com/zephyrproject-rtos/zephyr/issues/45953) - modem: simcom-sim7080: sendmsg() should result in single outgoing datagram
- [GitHub #46008](https://github.com/zephyrproject-rtos/zephyr/issues/46008) - stm32h7: gptp sample does not work at all
- [GitHub #46049](https://github.com/zephyrproject-rtos/zephyr/issues/46049) - Usage faults on semaphore usage in driver (stm32l1)
- [GitHub #46066](https://github.com/zephyrproject-rtos/zephyr/issues/46066) - TF-M: Unable to trigger NMI interrupt from non-secure
- [GitHub #46072](https://github.com/zephyrproject-rtos/zephyr/issues/46072) - [ESP32] Debug log error in hawkbit example “CONFIG\_LOG\_STRDUP\_MAX\_STRING”
- [GitHub #46073](https://github.com/zephyrproject-rtos/zephyr/issues/46073) - IPSP (IPv6 over BLE) example stop working after a short time
- [GitHub #46121](https://github.com/zephyrproject-rtos/zephyr/issues/46121) - Bluetooth: Controller: hci: Wrong periodic advertising report data status
- [GitHub #46124](https://github.com/zephyrproject-rtos/zephyr/issues/46124) - stm32g071 ADC drivers apply errata during sampling config
- [GitHub #46126](https://github.com/zephyrproject-rtos/zephyr/issues/46126) - pm\_device causes assertion error in sched.c with lis2dh
- [GitHub #46157](https://github.com/zephyrproject-rtos/zephyr/issues/46157) - ACRN: some cases still failed because of the log missing
- [GitHub #46158](https://github.com/zephyrproject-rtos/zephyr/issues/46158) - frdm\_k64f：failed to run test case tests/subsys/modbus/modbus.rtu/server\_setup\_low\_none
- [GitHub #46167](https://github.com/zephyrproject-rtos/zephyr/issues/46167) - esp32: Unable to select GPIO for PWM LED driver channel
- [GitHub #46170](https://github.com/zephyrproject-rtos/zephyr/issues/46170) - ipc\_service: open-amp backend may never leave
- [GitHub #46173](https://github.com/zephyrproject-rtos/zephyr/issues/46173) - nRF UART callback is not passed correct index via evt->data.rx.offset sometimes
- [GitHub #46186](https://github.com/zephyrproject-rtos/zephyr/issues/46186) - ISO Broadcaster fails silently on unsupported RTN/SDU\_Interval combination
- [GitHub #46199](https://github.com/zephyrproject-rtos/zephyr/issues/46199) - LIS2DW12 I2C driver uses invalid write command
- [GitHub #46206](https://github.com/zephyrproject-rtos/zephyr/issues/46206) - it8xxx2\_evb: tests/kernel/fatal/exception/ assertion failed – “thread was not aborted”
- [GitHub #46208](https://github.com/zephyrproject-rtos/zephyr/issues/46208) - it8xxx2\_evb: tests/kernel/sleep failed, elapsed\_ms = 2125
- [GitHub #46234](https://github.com/zephyrproject-rtos/zephyr/issues/46234) - samples: lsm6dso: prints incorrect anglular velocity units
- [GitHub #46235](https://github.com/zephyrproject-rtos/zephyr/issues/46235) - subsystem: Bluetooth LLL: ASSERTION FAIL [!link->next]
- [GitHub #46255](https://github.com/zephyrproject-rtos/zephyr/issues/46255) - imxrt1010 wrong device tree addresses
- [GitHub #46263](https://github.com/zephyrproject-rtos/zephyr/issues/46263) - Regulator Control

### Addressed issues

- [GitHub #46241](https://github.com/zephyrproject-rtos/zephyr/issues/46241) - Bluetooth: Controller: ISO: Setting CONFIG\_BT\_CTLR\_ISO\_TX\_BUFFERS=4 breaks non-ISO data
- [GitHub #46140](https://github.com/zephyrproject-rtos/zephyr/issues/46140) - Custom driver offload socket creation failing
- [GitHub #46138](https://github.com/zephyrproject-rtos/zephyr/issues/46138) - Problem with building zephyr/samples/subsys/mgmt/mcumgr/smp\_svr using atsame70
- [GitHub #46137](https://github.com/zephyrproject-rtos/zephyr/issues/46137) - RFC: Integrate u8g2 monochrome graphcial library as module to Zephyr OS ([https://github.com/olikraus/u8g2](https://github.com/olikraus/u8g2))
- [GitHub #46129](https://github.com/zephyrproject-rtos/zephyr/issues/46129) - net: lwm2m: Object Update Callbacks
- [GitHub #46102](https://github.com/zephyrproject-rtos/zephyr/issues/46102) - samples: net: W5500 implementation
- [GitHub #46097](https://github.com/zephyrproject-rtos/zephyr/issues/46097) - b\_l072z\_lrwan1 usart dma doesn’t work
- [GitHub #46093](https://github.com/zephyrproject-rtos/zephyr/issues/46093) - get a run error “Fatal exception (28): LoadProhibited” while enable CONFIG\_NEWLIB\_LIBC=y
- [GitHub #46091](https://github.com/zephyrproject-rtos/zephyr/issues/46091) - samples: net: cloud: tagoio: Drop pinmux dependency
- [GitHub #46059](https://github.com/zephyrproject-rtos/zephyr/issues/46059) - LwM2M: Software management URI resource not updated properly
- [GitHub #46056](https://github.com/zephyrproject-rtos/zephyr/issues/46056) - `unexpected eof` with twister running `tests/subsys/logging/log_api/logging.log2_api_immediate_printk_cpp` on `qemu_leon3`
- [GitHub #46037](https://github.com/zephyrproject-rtos/zephyr/issues/46037) - ESP32 : fails to build the mcuboot, zephyr v3.1.0 rc2, sdk 0.14.2
- [GitHub #46034](https://github.com/zephyrproject-rtos/zephyr/issues/46034) - subsys settings: should check the return value of function cs->cs\_itf->csi\_load(cs, &arg).
- [GitHub #46033](https://github.com/zephyrproject-rtos/zephyr/issues/46033) - twister: incorrect display of test results
- [GitHub #46027](https://github.com/zephyrproject-rtos/zephyr/issues/46027) - tests: rpi\_pico tests fails on twister with: No rule to make target ‘bootloader/boot\_stage2.S
- [GitHub #46026](https://github.com/zephyrproject-rtos/zephyr/issues/46026) - Bluetooth: Controller: llcp: Wrong effective time calculation if PHY changed
- [GitHub #46023](https://github.com/zephyrproject-rtos/zephyr/issues/46023) - drivers: reset: Use of reserved identifier `assert`
- [GitHub #46020](https://github.com/zephyrproject-rtos/zephyr/issues/46020) - module/mcuboot: doesn’t build with either RSA or ECISE-X25519 image encryption
- [GitHub #46017](https://github.com/zephyrproject-rtos/zephyr/issues/46017) - Apply for contributor
- [GitHub #46002](https://github.com/zephyrproject-rtos/zephyr/issues/46002) - NMP timeout when i am using any mcumgr command
- [GitHub #45996](https://github.com/zephyrproject-rtos/zephyr/issues/45996) - stm32F7: DCache configuration is not correctly implemented
- [GitHub #45948](https://github.com/zephyrproject-rtos/zephyr/issues/45948) - net: socket: dtls: sendmsg() should result in single outgoing datagram
- [GitHub #45946](https://github.com/zephyrproject-rtos/zephyr/issues/45946) - net: context: outgoing datagrams are truncated if not enough memory was allocated
- [GitHub #45942](https://github.com/zephyrproject-rtos/zephyr/issues/45942) - tests: twister: harness: Test harness report pass when there is no console output
- [GitHub #45933](https://github.com/zephyrproject-rtos/zephyr/issues/45933) - webusb sample code linking error for esp32 board
- [GitHub #45932](https://github.com/zephyrproject-rtos/zephyr/issues/45932) - tests: subsys/logging/log\_syst : failed to build on rpi\_pico
- [GitHub #45916](https://github.com/zephyrproject-rtos/zephyr/issues/45916) - USART on STM32: Using same name for different remapping configurations
- [GitHub #45911](https://github.com/zephyrproject-rtos/zephyr/issues/45911) - LVGL sample cannot be built with CONFIG\_LEGACY\_INCLUDE\_PATH=n
- [GitHub #45904](https://github.com/zephyrproject-rtos/zephyr/issues/45904) - All tests require full timeout period to pass after twister overhaul when executed on HW platform
- [GitHub #45894](https://github.com/zephyrproject-rtos/zephyr/issues/45894) - up\_squared：the test shows pass in the twister.log it but does not seem to finish
- [GitHub #45893](https://github.com/zephyrproject-rtos/zephyr/issues/45893) - MCUboot authentication failure with RSA-3072 key on i.MX RT 1160 EVK
- [GitHub #45886](https://github.com/zephyrproject-rtos/zephyr/issues/45886) - ESP32: PWM parameter renaming broke compilation
- [GitHub #45883](https://github.com/zephyrproject-rtos/zephyr/issues/45883) - Bluetooth: Controller: CCM reads data before Radio stores them when DF enabled on PHY 1M
- [GitHub #45882](https://github.com/zephyrproject-rtos/zephyr/issues/45882) - Zephyr minimal C library contains files licensed with BSD-4-Clause-UC
- [GitHub #45878](https://github.com/zephyrproject-rtos/zephyr/issues/45878) - doc: release: Update release notes with CVE
- [GitHub #45876](https://github.com/zephyrproject-rtos/zephyr/issues/45876) - boards: h747/h745: Update dual core flash and debug instructions
- [GitHub #45875](https://github.com/zephyrproject-rtos/zephyr/issues/45875) - bluetooth: hci\_raw: avoid possible memory overflow in bt\_buf\_get\_tx()
- [GitHub #45873](https://github.com/zephyrproject-rtos/zephyr/issues/45873) - soc: esp32: use PYTHON\_EXECUTABLE from build system
- [GitHub #45872](https://github.com/zephyrproject-rtos/zephyr/issues/45872) - ci: make git credentials non-persistent
- [GitHub #45871](https://github.com/zephyrproject-rtos/zephyr/issues/45871) - ci: split Bluetooth workflow
- [GitHub #45870](https://github.com/zephyrproject-rtos/zephyr/issues/45870) - drivers: virt\_ivshmem: Allow multiple instances of ivShMem devices
- [GitHub #45869](https://github.com/zephyrproject-rtos/zephyr/issues/45869) - doc: update requirements
- [GitHub #45865](https://github.com/zephyrproject-rtos/zephyr/issues/45865) - CODEOWNERS has errors
- [GitHub #45862](https://github.com/zephyrproject-rtos/zephyr/issues/45862) - USB ECM/RNDIS Can’t receive broadcast messages
- [GitHub #45856](https://github.com/zephyrproject-rtos/zephyr/issues/45856) - blinky built with asserts on arduino nano
- [GitHub #45855](https://github.com/zephyrproject-rtos/zephyr/issues/45855) - Runtime fault when running with CONFIG\_NO\_OPTIMIZATIONS=y
- [GitHub #45854](https://github.com/zephyrproject-rtos/zephyr/issues/45854) - Bluetooth: Controller: llcp: Assert if LL\_REJECT\_IND PDU received while local and remote control procedure is pending
- [GitHub #45851](https://github.com/zephyrproject-rtos/zephyr/issues/45851) - For native\_posix programs, k\_yield doesn’t yield to k\_msleep threads
- [GitHub #45839](https://github.com/zephyrproject-rtos/zephyr/issues/45839) - Bluetooth: Controller: df: Possible memory overwrite if requested number of CTE is greater than allowed by configuration
- [GitHub #45836](https://github.com/zephyrproject-rtos/zephyr/issues/45836) - samples: Bluetooth: unicast\_audio\_server invalid check for ISO flags
- [GitHub #45834](https://github.com/zephyrproject-rtos/zephyr/issues/45834) - SMP Server Sample needs `-DDTC_OVERLAY_FILE=usb.overlay` for CDC\_ACM
- [GitHub #45828](https://github.com/zephyrproject-rtos/zephyr/issues/45828) - mcumgr: img\_mgmt\_dfu\_stopped is called on a successful erase
- [GitHub #45827](https://github.com/zephyrproject-rtos/zephyr/issues/45827) - bluetooth: bluetooth host: Adding the same device to resolving list
- [GitHub #45826](https://github.com/zephyrproject-rtos/zephyr/issues/45826) - Bluetooth: controller: Assert in lll.c when executing LL/CON/INI/BV-28-C
- [GitHub #45821](https://github.com/zephyrproject-rtos/zephyr/issues/45821) - STM32U5: clock\_control: Issue to get rate of alt clock source
- [GitHub #45820](https://github.com/zephyrproject-rtos/zephyr/issues/45820) - bluetooth: host: Failed to set security right after reconnection with bonded Central
- [GitHub #45800](https://github.com/zephyrproject-rtos/zephyr/issues/45800) - Clock control settings for MCUX Audio Clock are Incorrect
- [GitHub #45799](https://github.com/zephyrproject-rtos/zephyr/issues/45799) - LED strip driver flips colors on stm32h7
- [GitHub #45795](https://github.com/zephyrproject-rtos/zephyr/issues/45795) - driver: pinctrl: npcx: get build error when apply pinctrl mechanism to a DT node without reg prop.
- [GitHub #45791](https://github.com/zephyrproject-rtos/zephyr/issues/45791) - drivers/usb: stm32: Superfluous/misleading Kconfig option
- [GitHub #45790](https://github.com/zephyrproject-rtos/zephyr/issues/45790) - drivers: can: stm32h7: wrong minimum timing values
- [GitHub #45784](https://github.com/zephyrproject-rtos/zephyr/issues/45784) - nominate me as zephyr contributor
- [GitHub #45783](https://github.com/zephyrproject-rtos/zephyr/issues/45783) - drivers/serial: ns16550: message is garbled
- [GitHub #45779](https://github.com/zephyrproject-rtos/zephyr/issues/45779) - Implementing ARCH\_EXCEPT on Xtensa unmasks nested interrupt handling bug
- [GitHub #45778](https://github.com/zephyrproject-rtos/zephyr/issues/45778) - Unable to use thread aware debugging with STM32H743ZI
- [GitHub #45761](https://github.com/zephyrproject-rtos/zephyr/issues/45761) - MCUBoot with multi-image support on Zephyr project for i.MX RT1165 EVK
- [GitHub #45755](https://github.com/zephyrproject-rtos/zephyr/issues/45755) - ESP32 –defsym:1: undefined symbol `printf’ referenced in expression - using CONFIG\_NEWLIB\_LIBC
- [GitHub #45750](https://github.com/zephyrproject-rtos/zephyr/issues/45750) - tests-ci : kernel: timer: tickless test\_sleep\_abs Failed
- [GitHub #45751](https://github.com/zephyrproject-rtos/zephyr/issues/45751) - tests-ci : drivers: counter: basic\_api test\_multiple\_alarms Failed
- [GitHub #45739](https://github.com/zephyrproject-rtos/zephyr/issues/45739) - stm32h7: DCache configuration is not correctly implemented
- [GitHub #45735](https://github.com/zephyrproject-rtos/zephyr/issues/45735) - Ethernet W5500 Driver via SPI is deadlocking
- [GitHub #45725](https://github.com/zephyrproject-rtos/zephyr/issues/45725) - Bluetooth: Controller: df: CTE request not disabled if run in single shot mode
- [GitHub #45714](https://github.com/zephyrproject-rtos/zephyr/issues/45714) - Unable to get TCA9548A to work
- [GitHub #45713](https://github.com/zephyrproject-rtos/zephyr/issues/45713) - twister: map generation fails
- [GitHub #45708](https://github.com/zephyrproject-rtos/zephyr/issues/45708) - Bluetooth: Controller: llcp: CTE request control procedure has missing support for LL\_UNKNOWN\_RSP
- [GitHub #45706](https://github.com/zephyrproject-rtos/zephyr/issues/45706) - tests: error\_hook: mismatch testcases in testplan.json
- [GitHub #45702](https://github.com/zephyrproject-rtos/zephyr/issues/45702) - Reboot instead of halting the system
- [GitHub #45697](https://github.com/zephyrproject-rtos/zephyr/issues/45697) - RING\_BUF\_DECLARE broken for C++
- [GitHub #45691](https://github.com/zephyrproject-rtos/zephyr/issues/45691) - missing testcase tests/drivers/watchdog on nucleo stm32 boards
- [GitHub #45686](https://github.com/zephyrproject-rtos/zephyr/issues/45686) - missing testcase samples/drivers/led\_pwm on nucleo stm32 boards
- [GitHub #45672](https://github.com/zephyrproject-rtos/zephyr/issues/45672) - Bluetooth: Controller: can’t cancel periodic advertising sync create betwee ll\_sync\_create and reception of AUX\_\_ADV\_IND with SyncInfo
- [GitHub #45670](https://github.com/zephyrproject-rtos/zephyr/issues/45670) - Intel CAVS: log missing of tests/lib/p4workq/
- [GitHub #45664](https://github.com/zephyrproject-rtos/zephyr/issues/45664) - mqtt\_publisher does not work in atsame54\_xpro board
- [GitHub #45648](https://github.com/zephyrproject-rtos/zephyr/issues/45648) - pm: device\_runtime: API functions fault when PM not supported
- [GitHub #45632](https://github.com/zephyrproject-rtos/zephyr/issues/45632) - ESP32 get error “undefined reference to `sprintf’ “ while CONFIG\_NEWLIB\_LIBC=y
- [GitHub #45630](https://github.com/zephyrproject-rtos/zephyr/issues/45630) - ipc\_service: Align return codes for available backends.
- [GitHub #45611](https://github.com/zephyrproject-rtos/zephyr/issues/45611) - GD32 build failure: CAN\_MODE\_NORMAL is redefined
- [GitHub #45593](https://github.com/zephyrproject-rtos/zephyr/issues/45593) - tests: newlib: test\_malloc\_thread\_safety fails on nrf9160dk\_nrf9160\_ns
- [GitHub #45583](https://github.com/zephyrproject-rtos/zephyr/issues/45583) - Typo in definition of lsm6ds0.h
- [GitHub #45580](https://github.com/zephyrproject-rtos/zephyr/issues/45580) - ESP32-C3: CONFIG\_ESP32\_PHY\_MAX\_TX\_POWER undeclared error when building with CONFIG\_BT=y
- [GitHub #45578](https://github.com/zephyrproject-rtos/zephyr/issues/45578) - cmake: gcc –print-multi-directory doesn’t print full path and checks fails
- [GitHub #45577](https://github.com/zephyrproject-rtos/zephyr/issues/45577) - STM32L4: USB MSC doesn’t work with SD card
- [GitHub #45568](https://github.com/zephyrproject-rtos/zephyr/issues/45568) - STM32H7xx: Driver for internal flash memory partially uses a fixed flash program word size, which doesn’t fit for all STM32H7xx SOCs (e.g. STM32H7A3, STM32H7B0, STM32H7B3) leading to potential flash data corruption
- [GitHub #45557](https://github.com/zephyrproject-rtos/zephyr/issues/45557) - doc: Some generic yaml bindings don’t show up in dts/api/bindings.html#dt-no-vendor
- [GitHub #45549](https://github.com/zephyrproject-rtos/zephyr/issues/45549) - bt\_gatt\_write\_without\_response\_cb doesn’t use callback
- [GitHub #45545](https://github.com/zephyrproject-rtos/zephyr/issues/45545) - K\_ESSENTIAL option doesn’t have any effect on k\_create\_thread
- [GitHub #45543](https://github.com/zephyrproject-rtos/zephyr/issues/45543) - Build samples/bluetooth/broadcast\_audio\_sink raises an error
- [GitHub #45542](https://github.com/zephyrproject-rtos/zephyr/issues/45542) - Implementing firmware image decompression in img\_mgmt\_upload()
- [GitHub #45533](https://github.com/zephyrproject-rtos/zephyr/issues/45533) - uart\_imx\_poll\_in() seems to be a blocking function
- [GitHub #45529](https://github.com/zephyrproject-rtos/zephyr/issues/45529) - GdbStub get\_mem\_region bug
- [GitHub #45518](https://github.com/zephyrproject-rtos/zephyr/issues/45518) - LPCXpresso55S69 incorrect device name for JLink runner
- [GitHub #45514](https://github.com/zephyrproject-rtos/zephyr/issues/45514) - UDP Packet socket doesn’t do L2 header processing
- [GitHub #45505](https://github.com/zephyrproject-rtos/zephyr/issues/45505) - NXP MIMXRT1050-EVKB: MCUBoot Serial Recover: mcumgr hangs when trying to upload image
- [GitHub #45488](https://github.com/zephyrproject-rtos/zephyr/issues/45488) - Build warnings when no GPIO ports enabled
- [GitHub #45486](https://github.com/zephyrproject-rtos/zephyr/issues/45486) - MCUBootloader can’t building for imxrt1160\_evk\_cm7 core
- [GitHub #45482](https://github.com/zephyrproject-rtos/zephyr/issues/45482) - Adding, building and linking Lua in a project
- [GitHub #45468](https://github.com/zephyrproject-rtos/zephyr/issues/45468) - Is uart\_poll\_in() blocking or not?
- [GitHub #45463](https://github.com/zephyrproject-rtos/zephyr/issues/45463) - null function pointer called when using shell logger backend under heavy load
- [GitHub #45458](https://github.com/zephyrproject-rtos/zephyr/issues/45458) - it8xxx2\_evb: tests/drivers/pwm/pwm\_api assertion fail
- [GitHub #45443](https://github.com/zephyrproject-rtos/zephyr/issues/45443) - SAMD21: Wrong voltage reference set by enum adc\_reference
- [GitHub #45440](https://github.com/zephyrproject-rtos/zephyr/issues/45440) - Intel CAVS: intel\_adsp\_hda testsuite is failing due to time out on intel\_adsp\_cavs15
- [GitHub #45431](https://github.com/zephyrproject-rtos/zephyr/issues/45431) - Bluetooth: Controller: df: Wrong antenna identifier inserted after switch pattern exhausted
- [GitHub #45426](https://github.com/zephyrproject-rtos/zephyr/issues/45426) - Data buffer allocation: TCP stops working
- [GitHub #45421](https://github.com/zephyrproject-rtos/zephyr/issues/45421) - Zephyr build image(sample blinky application) not getting flash through NXP Secure Provisioning Tool V4.0 for i.MX RT 1166EVK
- [GitHub #45407](https://github.com/zephyrproject-rtos/zephyr/issues/45407) - Support for flashing the Zephyr based application on i.MX RT 1160 EVK through SDP Mode(USB-HID/ UART) & PyOCD runner
- [GitHub #45405](https://github.com/zephyrproject-rtos/zephyr/issues/45405) - up\_squared: most of the test case timeout
- [GitHub #45404](https://github.com/zephyrproject-rtos/zephyr/issues/45404) - Bluetooth: Controller: Periodic advertising scheduling is broken, TIFS/TMAFS maintenance corrupted
- [GitHub #45401](https://github.com/zephyrproject-rtos/zephyr/issues/45401) - test-ci: adc: lpcxpresso55s28: adc pinctl init error
- [GitHub #45394](https://github.com/zephyrproject-rtos/zephyr/issues/45394) - Bug when sending a BLE proxy mesh msg of length exactly 2x the MTU size
- [GitHub #45390](https://github.com/zephyrproject-rtos/zephyr/issues/45390) - MinGW-w64: Cannot build Zephyr project
- [GitHub #45395](https://github.com/zephyrproject-rtos/zephyr/issues/45395) - Programming NXP i.MX RT OTP fuse with west
- [GitHub #45372](https://github.com/zephyrproject-rtos/zephyr/issues/45372) - PWM not working
- [GitHub #45371](https://github.com/zephyrproject-rtos/zephyr/issues/45371) - frdm\_k64f: failed to run test case tests/net/socket/offload\_dispatcher
- [GitHub #45367](https://github.com/zephyrproject-rtos/zephyr/issues/45367) - net: tcp: Scheduling dependent throughput
- [GitHub #45365](https://github.com/zephyrproject-rtos/zephyr/issues/45365) - Zephyr IP Stack Leaks in Promiscuous Mode
- [GitHub #45362](https://github.com/zephyrproject-rtos/zephyr/issues/45362) - sample/net/sockets/dumb\_http\_server not working with enc28j60
- [GitHub #45361](https://github.com/zephyrproject-rtos/zephyr/issues/45361) - samples/bluetooth/hci\_usb doesn’t build for nucleo\_wb55rg
- [GitHub #45359](https://github.com/zephyrproject-rtos/zephyr/issues/45359) - USB DFU sample does not work on RT series boards
- [GitHub #45355](https://github.com/zephyrproject-rtos/zephyr/issues/45355) - Twister fails when west is not present
- [GitHub #45345](https://github.com/zephyrproject-rtos/zephyr/issues/45345) - Make FCB work with sectors larger than 16K
- [GitHub #45337](https://github.com/zephyrproject-rtos/zephyr/issues/45337) - timing: missing extern “C” in timing.h
- [GitHub #45336](https://github.com/zephyrproject-rtos/zephyr/issues/45336) - newlib: PRIx8 inttype incorrectly resolves to `hh` with newlib-nano
- [GitHub #45324](https://github.com/zephyrproject-rtos/zephyr/issues/45324) - NET\_TCP\_BACKLOG\_SIZE is unused, it has to be either implemented or deleted
- [GitHub #45322](https://github.com/zephyrproject-rtos/zephyr/issues/45322) - tests: drivers: pwm\_api fails with stm32 devices
- [GitHub #45316](https://github.com/zephyrproject-rtos/zephyr/issues/45316) - drivers: timer: nrf\_rtc\_timer: SYS\_CLOCK\_TICKS\_PER\_SEC too high for when CONFIG\_KERNEL\_TICKLESS=n
- [GitHub #45314](https://github.com/zephyrproject-rtos/zephyr/issues/45314) - subsystem: Bluetooth LLL: ASSERTION FAIL [!link->next] @ ZEPHYR\_BASE/subsys/bluetooth/controller/ll\_sw/ull\_conn.c:1952
- [GitHub #45303](https://github.com/zephyrproject-rtos/zephyr/issues/45303) - drivers: can: CAN classic and CAN-FD APIs are mixed together and CAN-FD is a compile-time option
- [GitHub #45302](https://github.com/zephyrproject-rtos/zephyr/issues/45302) - Bus Fault with Xilinx UART Lite
- [GitHub #45280](https://github.com/zephyrproject-rtos/zephyr/issues/45280) - GPIO Configuration Issue
- [GitHub #45278](https://github.com/zephyrproject-rtos/zephyr/issues/45278) - twister: Run\_id check feature breaks workflows with splitted building and testing.
- [GitHub #45276](https://github.com/zephyrproject-rtos/zephyr/issues/45276) - Add support for multiple zero-latency irq priorities
- [GitHub #45268](https://github.com/zephyrproject-rtos/zephyr/issues/45268) - Error newlibc ESP32
- [GitHub #45267](https://github.com/zephyrproject-rtos/zephyr/issues/45267) - kernel: Recursive spinlock in k\_msgq\_get() in the context of a k\_work\_poll handler
- [GitHub #45266](https://github.com/zephyrproject-rtos/zephyr/issues/45266) - teensy41: pwm sample unable to build
- [GitHub #45261](https://github.com/zephyrproject-rtos/zephyr/issues/45261) - mcumgr: conversion of version to string fails (snprintf format issue)
- [GitHub #45248](https://github.com/zephyrproject-rtos/zephyr/issues/45248) - Avoid redefining 32-bit integer types like \_\_UINT32\_TYPE\_\_
- [GitHub #45237](https://github.com/zephyrproject-rtos/zephyr/issues/45237) - RFC: API Change: Bluetooth - replace callback in bt\_gatt\_subscribe\_param
- [GitHub #45229](https://github.com/zephyrproject-rtos/zephyr/issues/45229) - sample: spi: bitbang: spi\_bitbang sample has improper definition of its test
- [GitHub #45226](https://github.com/zephyrproject-rtos/zephyr/issues/45226) - samples/drivers/led\_pwm: Build failure
- [GitHub #45219](https://github.com/zephyrproject-rtos/zephyr/issues/45219) - drivers: can: transceivers are initialized after controllers
- [GitHub #45209](https://github.com/zephyrproject-rtos/zephyr/issues/45209) - Minimal LIBC missing macros
- [GitHub #45189](https://github.com/zephyrproject-rtos/zephyr/issues/45189) - sam\_e70b\_xplained: failed to run test case tests/benchmarks/cmsis\_dsp/basicmath
- [GitHub #45186](https://github.com/zephyrproject-rtos/zephyr/issues/45186) - Building Zephyr on Ubuntu fails when ZEPHYR\_TOOLCHAIN\_VARIANT is set to llvm
- [GitHub #45185](https://github.com/zephyrproject-rtos/zephyr/issues/45185) - Intel CAVS: tests under tests/ztest/register/ are failing
- [GitHub #45182](https://github.com/zephyrproject-rtos/zephyr/issues/45182) - MCUBoot Usage Fault on RT1060 EVK
- [GitHub #45172](https://github.com/zephyrproject-rtos/zephyr/issues/45172) - Bluetooth: attr->user\_data is NULL when doing discovery with BT\_GATT\_DISCOVER\_ATTRIBUTE
- [GitHub #45155](https://github.com/zephyrproject-rtos/zephyr/issues/45155) - STM32 serial port asynchronous initialization TX DMA channel error
- [GitHub #45152](https://github.com/zephyrproject-rtos/zephyr/issues/45152) - `tests/subsys/logging/log_stack` times out on `qemu_arc_hs6x` with twister
- [GitHub #45129](https://github.com/zephyrproject-rtos/zephyr/issues/45129) - mimxrt1050\_evk: GPIO button pushed only once
- [GitHub #45123](https://github.com/zephyrproject-rtos/zephyr/issues/45123) - driver: can\_stm32fd: STM32U5 series support
- [GitHub #45118](https://github.com/zephyrproject-rtos/zephyr/issues/45118) - Error claiming older doc is the latest
- [GitHub #45112](https://github.com/zephyrproject-rtos/zephyr/issues/45112) - Cannot install watchdog timeout on STM32WB
- [GitHub #45111](https://github.com/zephyrproject-rtos/zephyr/issues/45111) - fvp\_base\_revc\_2xaemv8a: multiple test failures
- [GitHub #45110](https://github.com/zephyrproject-rtos/zephyr/issues/45110) - fvp\_baser\_aemv8r\_smp: multiple test failures
- [GitHub #45108](https://github.com/zephyrproject-rtos/zephyr/issues/45108) - fvp\_baser\_aemv8r: multiple test failures
- [GitHub #45089](https://github.com/zephyrproject-rtos/zephyr/issues/45089) - stm32: usart: rx pin inversion missing
- [GitHub #45073](https://github.com/zephyrproject-rtos/zephyr/issues/45073) - nucleo\_h743zi failing twister builds due to NOCACHE\_MEMORY warning
- [GitHub #45072](https://github.com/zephyrproject-rtos/zephyr/issues/45072) - [Coverity CID: 248346] Copy into fixed size buffer in /subsys/bluetooth/shell/bt.c
- [GitHub #45045](https://github.com/zephyrproject-rtos/zephyr/issues/45045) - mec172xevb\_assy6906: tests/arch/arm/arm\_irq\_vector\_table failed to run
- [GitHub #45012](https://github.com/zephyrproject-rtos/zephyr/issues/45012) - sam\_e70b\_xplained: failed to run test case tests/drivers/can/timing/drivers.can.timing
- [GitHub #45009](https://github.com/zephyrproject-rtos/zephyr/issues/45009) - twister: many tests failed with “mismatch error” after met a SerialException.
- [GitHub #45008](https://github.com/zephyrproject-rtos/zephyr/issues/45008) - esp32: i2c\_read() error was returned successfully at the bus nack
- [GitHub #45006](https://github.com/zephyrproject-rtos/zephyr/issues/45006) - Bluetooth HCI SPI fault
- [GitHub #44997](https://github.com/zephyrproject-rtos/zephyr/issues/44997) - zcbor build error when ZCBOR\_VERBOSE is set
- [GitHub #44985](https://github.com/zephyrproject-rtos/zephyr/issues/44985) - tests: drivers: can: timing: failure to set bitrate of 800kbit/s on nucleo\_g474re
- [GitHub #44977](https://github.com/zephyrproject-rtos/zephyr/issues/44977) - samples: modules: canopennode: failure to initialize settings subsystem on nucleo\_g474re
- [GitHub #44966](https://github.com/zephyrproject-rtos/zephyr/issues/44966) - build fails for nucleo wb55 rg board.
- [GitHub #44956](https://github.com/zephyrproject-rtos/zephyr/issues/44956) - Deprecate the old spi\_cs\_control fields
- [GitHub #44947](https://github.com/zephyrproject-rtos/zephyr/issues/44947) - cmsis\_dsp: matrix: error during building libraries.cmsis\_dsp.matrix.unary\_f64 for qemu\_cortex\_m3
- [GitHub #44940](https://github.com/zephyrproject-rtos/zephyr/issues/44940) - rom\_report creates two identical identifier but for different path in rom.json
- [GitHub #44938](https://github.com/zephyrproject-rtos/zephyr/issues/44938) - Pin assignments SPIS nrf52
- [GitHub #44931](https://github.com/zephyrproject-rtos/zephyr/issues/44931) - Bluetooth: Samples: broadcast\_audio\_source stack overflow
- [GitHub #44927](https://github.com/zephyrproject-rtos/zephyr/issues/44927) - Problems in using STM32 Hal Library
- [GitHub #44926](https://github.com/zephyrproject-rtos/zephyr/issues/44926) - intel\_adsp\_cavs25: can not build multiple tests under tests/posix/ and tests/lib/newlib/
- [GitHub #44921](https://github.com/zephyrproject-rtos/zephyr/issues/44921) - Can’t run hello\_world using mps\_an521\_remote
- [GitHub #44913](https://github.com/zephyrproject-rtos/zephyr/issues/44913) - Enabling BT\_CENTRAL breaks MESH advertising
- [GitHub #44910](https://github.com/zephyrproject-rtos/zephyr/issues/44910) - Issue when installing Python additional dependencies
- [GitHub #44904](https://github.com/zephyrproject-rtos/zephyr/issues/44904) - PR#42879 causes a hang in the shell history
- [GitHub #44902](https://github.com/zephyrproject-rtos/zephyr/issues/44902) - x86: FPU registers are not initialised for userspace (eager FPU sharing)
- [GitHub #44887](https://github.com/zephyrproject-rtos/zephyr/issues/44887) - it8xxx2\_evb: tests/kernel/sched/schedule\_api/ assertion fail
- [GitHub #44886](https://github.com/zephyrproject-rtos/zephyr/issues/44886) - Unable to boot Zephyr on FVP\_BaseR\_AEMv8R
- [GitHub #44882](https://github.com/zephyrproject-rtos/zephyr/issues/44882) - doc: Section/chapter “Supported Boards” missing from pdf documentation
- [GitHub #44874](https://github.com/zephyrproject-rtos/zephyr/issues/44874) - error log for locking a mutex in an ISR
- [GitHub #44872](https://github.com/zephyrproject-rtos/zephyr/issues/44872) - k\_timer callback timing incorrect with multiple lightly loaded cores
- [GitHub #44871](https://github.com/zephyrproject-rtos/zephyr/issues/44871) - mcumgr endless loop in mgmt\_find\_handler
- [GitHub #44864](https://github.com/zephyrproject-rtos/zephyr/issues/44864) - tcp server tls error：server has no certificate
- [GitHub #44856](https://github.com/zephyrproject-rtos/zephyr/issues/44856) - Various kernel timing-related tests fail on hifive1 board
- [GitHub #44837](https://github.com/zephyrproject-rtos/zephyr/issues/44837) - drivers: can: mcp2515: can\_set\_timing() performs a soft-reset of the MCP2515, discarding configured mode
- [GitHub #44834](https://github.com/zephyrproject-rtos/zephyr/issues/44834) - Add support for gpio expandeux NXP PCAL95xx
- [GitHub #44831](https://github.com/zephyrproject-rtos/zephyr/issues/44831) - west flash for nucleo\_u575zi\_q is failing
- [GitHub #44830](https://github.com/zephyrproject-rtos/zephyr/issues/44830) - Unable to set compiler warnings on app exclusively
- [GitHub #44822](https://github.com/zephyrproject-rtos/zephyr/issues/44822) - STM32F103 Custom Board Clock Config Error
- [GitHub #44811](https://github.com/zephyrproject-rtos/zephyr/issues/44811) - STRINGIFY does not work with mcumgr
- [GitHub #44798](https://github.com/zephyrproject-rtos/zephyr/issues/44798) - promote Michael to the Triage permission level
- [GitHub #44797](https://github.com/zephyrproject-rtos/zephyr/issues/44797) - x86: Interrupt handling not working for cores <> core0 - VMs not having core 0 assigned cannot handle IRQ events.
- [GitHub #44778](https://github.com/zephyrproject-rtos/zephyr/issues/44778) - stdint types not recognized in soc\_common.h
- [GitHub #44777](https://github.com/zephyrproject-rtos/zephyr/issues/44777) - disco\_l475\_iot1 default CONFIG\_BOOT\_MAX\_IMG\_SECTORS should be 512 not 256
- [GitHub #44758](https://github.com/zephyrproject-rtos/zephyr/issues/44758) - intel\_adsp: kernel.common tests are failing
- [GitHub #44752](https://github.com/zephyrproject-rtos/zephyr/issues/44752) - Nominate @brgl as contributor
- [GitHub #44750](https://github.com/zephyrproject-rtos/zephyr/issues/44750) - Using STM32 internal ADC with interrupt:
- [GitHub #44737](https://github.com/zephyrproject-rtos/zephyr/issues/44737) - Configurable LSE driving capability on H735
- [GitHub #44734](https://github.com/zephyrproject-rtos/zephyr/issues/44734) - regression in GATT/SR/GAS/BV-06-C qualification test case
- [GitHub #44731](https://github.com/zephyrproject-rtos/zephyr/issues/44731) - mec172xevb\_assy6906: test/drivers/adc/adc\_api test case build fail
- [GitHub #44730](https://github.com/zephyrproject-rtos/zephyr/issues/44730) - zcbor ARRAY\_SIZE conflict with zephyr include
- [GitHub #44728](https://github.com/zephyrproject-rtos/zephyr/issues/44728) - Fresh Build and Flash of Bluetooth Peripheral Sample Produces Error on P-Nucleo-64 Board (STM32WBRG)
- [GitHub #44724](https://github.com/zephyrproject-rtos/zephyr/issues/44724) - can: drivers: mcux: flexcan: correctly handle errata 5461 and 5829
- [GitHub #44722](https://github.com/zephyrproject-rtos/zephyr/issues/44722) - lib: posix: support for pthread\_attr\_setstacksize
- [GitHub #44721](https://github.com/zephyrproject-rtos/zephyr/issues/44721) - drivers: can: mcan: can\_mcan\_add\_rx\_filter() unconditionally adds offset for extended CAN-ID filters
- [GitHub #44706](https://github.com/zephyrproject-rtos/zephyr/issues/44706) - drivers: can: mcp2515: mcp2515\_set\_mode() silently ignores unsupported modes
- [GitHub #44705](https://github.com/zephyrproject-rtos/zephyr/issues/44705) - Windows getting started references wget usage without step for installing wget
- [GitHub #44704](https://github.com/zephyrproject-rtos/zephyr/issues/44704) - Bootloader linking error while building for RPI\_PICO
- [GitHub #44701](https://github.com/zephyrproject-rtos/zephyr/issues/44701) - advertising with multiple advertising sets fails with BT\_HCI\_ERR\_MEM\_CAPACITY\_EXCEEDED
- [GitHub #44691](https://github.com/zephyrproject-rtos/zephyr/issues/44691) - west sign fails to find header size or padding
- [GitHub #44690](https://github.com/zephyrproject-rtos/zephyr/issues/44690) - ST kit b\_u585i\_iot02a and OCTOSPI flash support
- [GitHub #44687](https://github.com/zephyrproject-rtos/zephyr/issues/44687) - drivers: can: missing syscall verifier for can\_get\_max\_filters()
- [GitHub #44680](https://github.com/zephyrproject-rtos/zephyr/issues/44680) - drivers: can: mcux: flexcan: can\_set\_mode() resets IP, discarding installed RX filters
- [GitHub #44678](https://github.com/zephyrproject-rtos/zephyr/issues/44678) - mcumgr: lib: cmd: img\_mgmt: Warning about struct visibility emitted with certain Kconfig options
- [GitHub #44676](https://github.com/zephyrproject-rtos/zephyr/issues/44676) - mimxrt1050\_evk\_qspi crash or freeze when accessing flash
- [GitHub #44670](https://github.com/zephyrproject-rtos/zephyr/issues/44670) - tests-ci : kernel: tickless: concept test Timeout
- [GitHub #44671](https://github.com/zephyrproject-rtos/zephyr/issues/44671) - tests-ci : kernel: scheduler: deadline test failed
- [GitHub #44672](https://github.com/zephyrproject-rtos/zephyr/issues/44672) - tests-ci : drivers: counter: basic\_api test failed
- [GitHub #44659](https://github.com/zephyrproject-rtos/zephyr/issues/44659) - Enhancement to k\_thread\_state\_str()
- [GitHub #44621](https://github.com/zephyrproject-rtos/zephyr/issues/44621) - ASCS: Sink ASE stuck in Releasing state
- [GitHub #44600](https://github.com/zephyrproject-rtos/zephyr/issues/44600) - NMI testcase fails on tests/arch/arm/arm\_interrupt with twister
- [GitHub #44586](https://github.com/zephyrproject-rtos/zephyr/issues/44586) - nrf5340: Random crashes when a lot of interrupts is triggered
- [GitHub #44584](https://github.com/zephyrproject-rtos/zephyr/issues/44584) - SWO log output does not compile for STM32WB55
- [GitHub #44573](https://github.com/zephyrproject-rtos/zephyr/issues/44573) - Do we have complete RNDIS stack available for STM32 controller in zephyr ?
- [GitHub #44558](https://github.com/zephyrproject-rtos/zephyr/issues/44558) - Possible problem with timers
- [GitHub #44557](https://github.com/zephyrproject-rtos/zephyr/issues/44557) - tests: canbus: isotp: implementation: fails on mimxrt1024\_evk
- [GitHub #44553](https://github.com/zephyrproject-rtos/zephyr/issues/44553) - General Question: Compilation Time >15 Minutes?
- [GitHub #44546](https://github.com/zephyrproject-rtos/zephyr/issues/44546) - Bluetooth: ISO: Provide stream established information
- [GitHub #44544](https://github.com/zephyrproject-rtos/zephyr/issues/44544) - shell\_module/sample.shell.shell\_module.usb fails for thingy53\_nrf5340\_cpuapp\_ns
- [GitHub #44539](https://github.com/zephyrproject-rtos/zephyr/issues/44539) - twister fails on several stm32 boards with tests/arch/arm testcases
- [GitHub #44535](https://github.com/zephyrproject-rtos/zephyr/issues/44535) - mgmt/mcumgr/lib: Incorrect use of MGMT\_ERR\_ENOMEM, in most cases where it is used
- [GitHub #44531](https://github.com/zephyrproject-rtos/zephyr/issues/44531) - bl654\_usb without mcuboot maximum image size is not limited
- [GitHub #44530](https://github.com/zephyrproject-rtos/zephyr/issues/44530) - xtensa xcc build usb stack fail (newlib)
- [GitHub #44519](https://github.com/zephyrproject-rtos/zephyr/issues/44519) - Choosing CONFIG\_CHIP Kconfig breaks LwM2M client client example build
- [GitHub #44507](https://github.com/zephyrproject-rtos/zephyr/issues/44507) - net: tcp: No retries of a TCP FIN message
- [GitHub #44504](https://github.com/zephyrproject-rtos/zephyr/issues/44504) - net: tcp: Context still open after timeout on connect
- [GitHub #44497](https://github.com/zephyrproject-rtos/zephyr/issues/44497) - Add guide for disabling MSD on JLink OB devices and link to from smp\_svr page
- [GitHub #44495](https://github.com/zephyrproject-rtos/zephyr/issues/44495) - sys\_slist\_append\_list and sys\_slist\_merge\_slist corrupt target slist if appended or merged list is empty
- [GitHub #44489](https://github.com/zephyrproject-rtos/zephyr/issues/44489) - Docs: missing documentation related to MCUBOOT serial recovery feature
- [GitHub #44488](https://github.com/zephyrproject-rtos/zephyr/issues/44488) - Self sensor library from private git repository
- [GitHub #44486](https://github.com/zephyrproject-rtos/zephyr/issues/44486) - nucleo\_f429zi: multiple networking tests failing
- [GitHub #44484](https://github.com/zephyrproject-rtos/zephyr/issues/44484) - drivers: can: mcp2515: The MCP2515 driver uses wrong timing limits
- [GitHub #44483](https://github.com/zephyrproject-rtos/zephyr/issues/44483) - drivers: can: mcan: data phase prescaler bounds checking uses wrong value
- [GitHub #44482](https://github.com/zephyrproject-rtos/zephyr/issues/44482) - drivers: can: mcan: CAN\_SJW\_NO\_CHANGE not accepted with CONFIG\_ASSERT=y
- [GitHub #44480](https://github.com/zephyrproject-rtos/zephyr/issues/44480) - bt\_le\_adv\_stop null pointer exception
- [GitHub #44478](https://github.com/zephyrproject-rtos/zephyr/issues/44478) - Zephyr on Litex/Vexriscv not booting
- [GitHub #44473](https://github.com/zephyrproject-rtos/zephyr/issues/44473) - net: tcp: Connection does not properly terminate when connection is lost
- [GitHub #44453](https://github.com/zephyrproject-rtos/zephyr/issues/44453) - Linker warnings in watchdog samples and tests built for twr\_ke18f
- [GitHub #44449](https://github.com/zephyrproject-rtos/zephyr/issues/44449) - qemu\_riscv32 DHCP fault
- [GitHub #44439](https://github.com/zephyrproject-rtos/zephyr/issues/44439) - Bluetooth: Controller: Extended and Periodic Advertising HCI Component Conformance Test Coverage
- [GitHub #44427](https://github.com/zephyrproject-rtos/zephyr/issues/44427) - SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC not correct for hifive1\_revb / FE310
- [GitHub #44404](https://github.com/zephyrproject-rtos/zephyr/issues/44404) - Porting stm32h745 for zephyr
- [GitHub #44397](https://github.com/zephyrproject-rtos/zephyr/issues/44397) - twister: test case error number discrepancy in the result
- [GitHub #44391](https://github.com/zephyrproject-rtos/zephyr/issues/44391) - tests-ci : peripheral: gpio: 1pin test Timeout
- [GitHub #44438](https://github.com/zephyrproject-rtos/zephyr/issues/44438) - tests-ci : arch: interrupt: arm.nmi test Unknown
- [GitHub #44386](https://github.com/zephyrproject-rtos/zephyr/issues/44386) - Zephyr SDK 0.14.0 does not contain a sysroots directory
- [GitHub #44374](https://github.com/zephyrproject-rtos/zephyr/issues/44374) - Twister: Non-intact handler.log files when running tests and samples folders
- [GitHub #44361](https://github.com/zephyrproject-rtos/zephyr/issues/44361) - drivers: can: missing syscall verifier for can\_set\_mode()
- [GitHub #44349](https://github.com/zephyrproject-rtos/zephyr/issues/44349) - Nordic BLE fails assertion when logging is enabled
- [GitHub #44348](https://github.com/zephyrproject-rtos/zephyr/issues/44348) - drivers: can: z\_vrfy\_can\_recover() does not compile
- [GitHub #44347](https://github.com/zephyrproject-rtos/zephyr/issues/44347) - ACRN: multiple tests failed due to incomplete log
- [GitHub #44345](https://github.com/zephyrproject-rtos/zephyr/issues/44345) - drivers: can: M\_CAN bus recovery function has the wrong signature
- [GitHub #44344](https://github.com/zephyrproject-rtos/zephyr/issues/44344) - drivers: can: mcp2515 introduces a hard dependency on CONFIG\_CAN\_AUTO\_BUS\_OFF\_RECOVERY
- [GitHub #44338](https://github.com/zephyrproject-rtos/zephyr/issues/44338) - intel\_adsp\_cavs18: multiple tests failed due to non-intact log
- [GitHub #44314](https://github.com/zephyrproject-rtos/zephyr/issues/44314) - rddrone\_fmuk66: fatal error upon running basic samples
- [GitHub #44307](https://github.com/zephyrproject-rtos/zephyr/issues/44307) - LE Audio: unicast stream/ep or ACL disconnect reset should not terminate the CIG
- [GitHub #44296](https://github.com/zephyrproject-rtos/zephyr/issues/44296) - Bluetooth: Controller: DF: IQ sample of CTE signals are not valid if PHY is 1M
- [GitHub #44295](https://github.com/zephyrproject-rtos/zephyr/issues/44295) - Proposal for subsystem for media
- [GitHub #44284](https://github.com/zephyrproject-rtos/zephyr/issues/44284) - LE Audio: Missing recv\_info for BAP recv
- [GitHub #44283](https://github.com/zephyrproject-rtos/zephyr/issues/44283) - Bluetooth: ISO: Add TS flag for ISO receive
- [GitHub #44274](https://github.com/zephyrproject-rtos/zephyr/issues/44274) - direction\_finding\_connectionless\_rx/tx U-Blox Nora B106 EVK
- [GitHub #44271](https://github.com/zephyrproject-rtos/zephyr/issues/44271) - mgmt/mcumgr: BT transport: Possible buffer overflow (and crash) when reciving SMP when CONFIG\_MCUMGR\_BUF\_SIZE < transport MTU
- [GitHub #44262](https://github.com/zephyrproject-rtos/zephyr/issues/44262) - mimxrt1050\_evk: build time too long for this platform
- [GitHub #44261](https://github.com/zephyrproject-rtos/zephyr/issues/44261) - twister: some changes make test cases work abnormally.
- [GitHub #44259](https://github.com/zephyrproject-rtos/zephyr/issues/44259) - intel\_adsp\_cavs18: tests/lib/icmsg failed
- [GitHub #44255](https://github.com/zephyrproject-rtos/zephyr/issues/44255) - kernel: While thread is running [thread\_state] is in \_THREAD\_QUEUED
- [GitHub #44251](https://github.com/zephyrproject-rtos/zephyr/issues/44251) - `CONFIG_USB_DEVICE_REMOTE_WAKEUP` gets default value y if not set
- [GitHub #44250](https://github.com/zephyrproject-rtos/zephyr/issues/44250) - Can’t build WiFi support on esp32, esp32s2, esp32c3
- [GitHub #44247](https://github.com/zephyrproject-rtos/zephyr/issues/44247) - west build -b nrf52dk\_nrf52832 samples/boards/nrf/clock\_skew failed
- [GitHub #44244](https://github.com/zephyrproject-rtos/zephyr/issues/44244) - Bluetooth: Controller: ISO BIS payload counter rollover
- [GitHub #44240](https://github.com/zephyrproject-rtos/zephyr/issues/44240) - tests: drivers: pwm\_api: PWM driver test doesn’t compile for mec172xevb\_assy6906
- [GitHub #44239](https://github.com/zephyrproject-rtos/zephyr/issues/44239) - boards: arm: mec152x/mec172x CONFIG\_PWM=y doesn’t compile PWM driver
- [GitHub #44231](https://github.com/zephyrproject-rtos/zephyr/issues/44231) - Problems trying to configure the environment
- [GitHub #44218](https://github.com/zephyrproject-rtos/zephyr/issues/44218) - libc: minimal: qsort\_r not working as expected
- [GitHub #44216](https://github.com/zephyrproject-rtos/zephyr/issues/44216) - tests: drivers: counter\_basic\_api: Build failing on LPCxpresso55s69\_cpu
- [GitHub #44215](https://github.com/zephyrproject-rtos/zephyr/issues/44215) - tests: subsys: cpp: over half of tests failing on macOS but do not fail on Linux
- [GitHub #44213](https://github.com/zephyrproject-rtos/zephyr/issues/44213) - xtensa arch\_cpu\_idle not correct on cavs18+ platforms
- [GitHub #44199](https://github.com/zephyrproject-rtos/zephyr/issues/44199) - (U)INT{32,64}\_C macro constants do not match the Zephyr stdint types
- [GitHub #44192](https://github.com/zephyrproject-rtos/zephyr/issues/44192) - esp32 flash custom partition table
- [GitHub #44186](https://github.com/zephyrproject-rtos/zephyr/issues/44186) - Possible race condition in TCP connection establishment
- [GitHub #44145](https://github.com/zephyrproject-rtos/zephyr/issues/44145) - Zephyr Panic dump garbled on Intel cAVS platforms
- [GitHub #44134](https://github.com/zephyrproject-rtos/zephyr/issues/44134) - nRF52833 current consumption too high
- [GitHub #44128](https://github.com/zephyrproject-rtos/zephyr/issues/44128) - Deprecate DT\_CHOSEN\_ZEPHYR\_FLASH\_CONTROLLER\_LABEL
- [GitHub #44125](https://github.com/zephyrproject-rtos/zephyr/issues/44125) - drivers/ethernet/eth\_stm32\_hal.c: eth\_stm32\_hal\_set\_config() always returns -ENOTSUP (-134)
- [GitHub #44110](https://github.com/zephyrproject-rtos/zephyr/issues/44110) - Bluetooth: synced callback may have wrong addr type
- [GitHub #44109](https://github.com/zephyrproject-rtos/zephyr/issues/44109) - Device tree error while porting zephyr for a custom board
- [GitHub #44108](https://github.com/zephyrproject-rtos/zephyr/issues/44108) - `CONFIG_ZTEST_NEW_API=y` broken with `CONFIG_TEST_USERSPACE=y`
- [GitHub #44107](https://github.com/zephyrproject-rtos/zephyr/issues/44107) - The SMP nsim boards are started incorrectly when launching on real HW
- [GitHub #44106](https://github.com/zephyrproject-rtos/zephyr/issues/44106) - test of dma drivers fails on dma\_m2m\_loop\_test
- [GitHub #44101](https://github.com/zephyrproject-rtos/zephyr/issues/44101) - a build error when CONFIG\_MULTITHREADING=n
- [GitHub #44092](https://github.com/zephyrproject-rtos/zephyr/issues/44092) - rand32\_ctr\_drbg fails to call the respective initialization routing
- [GitHub #44089](https://github.com/zephyrproject-rtos/zephyr/issues/44089) - logging: shell backend: null-deref when logs are dropped
- [GitHub #44072](https://github.com/zephyrproject-rtos/zephyr/issues/44072) - mcumgr smp source is checking variable without it being set and causing automated test failures
- [GitHub #44070](https://github.com/zephyrproject-rtos/zephyr/issues/44070) - west spdx TypeError: ‘NoneType’ object is not iterable
- [GitHub #44043](https://github.com/zephyrproject-rtos/zephyr/issues/44043) - Usage fault when running flash shell sample on RT1064 EVK
- [GitHub #44029](https://github.com/zephyrproject-rtos/zephyr/issues/44029) - Unexpected behavior of CONFIG\_LOG\_OVERRIDE\_LEVEL
- [GitHub #44018](https://github.com/zephyrproject-rtos/zephyr/issues/44018) - net: tcp: Running out of buffers by packet loss
- [GitHub #44012](https://github.com/zephyrproject-rtos/zephyr/issues/44012) - net: tcp: Cooperative scheduling transfer size limited
- [GitHub #44010](https://github.com/zephyrproject-rtos/zephyr/issues/44010) - frdm\_k64f: failed to run testcase samples/kernel/metairq\_dispatch/
- [GitHub #44006](https://github.com/zephyrproject-rtos/zephyr/issues/44006) - intel\_adsp\_cavs25: tests/drivers/dma/loop\_transfer failed
- [GitHub #44004](https://github.com/zephyrproject-rtos/zephyr/issues/44004) - Bluetooth: ascs: Invalid ASE state transition: Releasing -> QoS Configured
- [GitHub #43993](https://github.com/zephyrproject-rtos/zephyr/issues/43993) - doc: Fix minor display issue for west spdx extension command
- [GitHub #43990](https://github.com/zephyrproject-rtos/zephyr/issues/43990) - How to make civetweb run on a specified network card
- [GitHub #43988](https://github.com/zephyrproject-rtos/zephyr/issues/43988) - Extracting the index of a child node referenced using alias
- [GitHub #43980](https://github.com/zephyrproject-rtos/zephyr/issues/43980) - No PWM signal on Nucleo F103RB using TIM1 CH2 PA9
- [GitHub #43976](https://github.com/zephyrproject-rtos/zephyr/issues/43976) - [lwm2m\_engine / sockets] Possibility to decrease timeout on connect()
- [GitHub #43975](https://github.com/zephyrproject-rtos/zephyr/issues/43975) - tests: kernel: scheduler: Test from kernel.scheduler.slice\_perthread fails on some nrf platforms
- [GitHub #43972](https://github.com/zephyrproject-rtos/zephyr/issues/43972) - UART: uart\_poll\_in() not working in Shell application
- [GitHub #43964](https://github.com/zephyrproject-rtos/zephyr/issues/43964) - k\_timer callback timing gets unreliable with more cores active
- [GitHub #43950](https://github.com/zephyrproject-rtos/zephyr/issues/43950) - code\_relocation: Add NOCOPY feature breaks windows builds
- [GitHub #43949](https://github.com/zephyrproject-rtos/zephyr/issues/43949) - drivers: espi: mec172x: ESPI flash write and erase operations not working
- [GitHub #43948](https://github.com/zephyrproject-rtos/zephyr/issues/43948) - drivers: espi: xec: MEC172x: Driver enables all bus interrupts but doesn’t handle them causing starvation
- [GitHub #43946](https://github.com/zephyrproject-rtos/zephyr/issues/43946) - Bluetooth: Automatic ATT MTU negotiation
- [GitHub #43940](https://github.com/zephyrproject-rtos/zephyr/issues/43940) - Support for CH32V307 devices
- [GitHub #43930](https://github.com/zephyrproject-rtos/zephyr/issues/43930) - nRF52833 High Power Consumption with 32.768kHz RC Oscillator
- [GitHub #43924](https://github.com/zephyrproject-rtos/zephyr/issues/43924) - ipc\_service: Extend API with zero-copy send
- [GitHub #43899](https://github.com/zephyrproject-rtos/zephyr/issues/43899) - can: stm32: Build issue on g4 target
- [GitHub #43898](https://github.com/zephyrproject-rtos/zephyr/issues/43898) - Twister: test case number discrepancy in the result xml.
- [GitHub #43891](https://github.com/zephyrproject-rtos/zephyr/issues/43891) - networking: detect initialisation failures of backing drivers
- [GitHub #43888](https://github.com/zephyrproject-rtos/zephyr/issues/43888) - adc: stm32: compilation broken on G4 targets
- [GitHub #43874](https://github.com/zephyrproject-rtos/zephyr/issues/43874) - mec172xevb\_assy6906: tests/drivers/spi/spi\_loopback test case UART output wrong.
- [GitHub #43873](https://github.com/zephyrproject-rtos/zephyr/issues/43873) - tests:ci:lpcxpresso55s06: portability.posix.common.newlib meet hard fault
- [GitHub #43872](https://github.com/zephyrproject-rtos/zephyr/issues/43872) - tests:ci:lpcxpresso55s06:libraries.cmsis\_dsp.matrix.unary\_f32 test fails
- [GitHub #43870](https://github.com/zephyrproject-rtos/zephyr/issues/43870) - test:ci:lpcxpresso55s06: hwinfo test meet hardfault
- [GitHub #43867](https://github.com/zephyrproject-rtos/zephyr/issues/43867) - mec172xevb\_assy6906: tests/drivers/pwm/pwm\_api test case build fail.
- [GitHub #43865](https://github.com/zephyrproject-rtos/zephyr/issues/43865) - Add APDS-9250 I2C Driver
- [GitHub #43864](https://github.com/zephyrproject-rtos/zephyr/issues/43864) - mec172xevb\_assy6906: tests/drivers/pwm/pwm\_loopback test case failed to build
- [GitHub #43858](https://github.com/zephyrproject-rtos/zephyr/issues/43858) - mcumgr seems to lock up when it receives command for group that does not exist
- [GitHub #43856](https://github.com/zephyrproject-rtos/zephyr/issues/43856) - mec172xevb\_assy6906: tests/drivers/i2c/i2c\_api i2c\_test failed
- [GitHub #43851](https://github.com/zephyrproject-rtos/zephyr/issues/43851) - LE Audio: Make PACS location optional
- [GitHub #43838](https://github.com/zephyrproject-rtos/zephyr/issues/43838) - mec172xevb\_assy6906: tests/drivers/adc/adc\_dma test case build fail
- [GitHub #43842](https://github.com/zephyrproject-rtos/zephyr/issues/43842) - tests-ci : libraries: encoding: jwt test Timeout
- [GitHub #43841](https://github.com/zephyrproject-rtos/zephyr/issues/43841) - tests-ci : net: socket: tls.preempt test Timeout
- [GitHub #43835](https://github.com/zephyrproject-rtos/zephyr/issues/43835) - `zephyr_library_compile_options()` fails to apply if the same setting is set for multiple libraries in a single project
- [GitHub #43834](https://github.com/zephyrproject-rtos/zephyr/issues/43834) - DHCP not work in `Intel@PSE` on `Intel@EHL`
- [GitHub #43830](https://github.com/zephyrproject-rtos/zephyr/issues/43830) - LPC55S69 Not flashing to second core.
- [GitHub #43829](https://github.com/zephyrproject-rtos/zephyr/issues/43829) - http\_client: http\_client\_req() returns incorrect number of bytes sent
- [GitHub #43818](https://github.com/zephyrproject-rtos/zephyr/issues/43818) - lib: os: ring\_buffer: recent changes cause UART shell to fail on qemu\_cortex\_a9
- [GitHub #43816](https://github.com/zephyrproject-rtos/zephyr/issues/43816) - tests: cmsis\_dsp: rf16 and cf16 tests are not executed on Native POSIX
- [GitHub #43807](https://github.com/zephyrproject-rtos/zephyr/issues/43807) - Test “cpp.libcxx.newlib.exception” failed on platforms which use zephyr.bin to run tests.
- [GitHub #43794](https://github.com/zephyrproject-rtos/zephyr/issues/43794) - BMI160 Driver: Waiting time between SPI activation and reading CHIP IP is too low
- [GitHub #43793](https://github.com/zephyrproject-rtos/zephyr/issues/43793) - Alllow callbacks to CDC\_ACM events
- [GitHub #43792](https://github.com/zephyrproject-rtos/zephyr/issues/43792) - mimxrt1050\_evk: failed to run tests/net/socket/tls and tests/subsys/jwt
- [GitHub #43786](https://github.com/zephyrproject-rtos/zephyr/issues/43786) - [Logging] log context redefined with XCC when use zephyr logging api with SOF
- [GitHub #43757](https://github.com/zephyrproject-rtos/zephyr/issues/43757) - it8xxx2\_evb: k\_busy\_wait is not working accurately for ITE RISC-V
- [GitHub #43756](https://github.com/zephyrproject-rtos/zephyr/issues/43756) - drivers: gpio: pca95xx does not compile with CONFIG\_GPIO\_PCA95XX\_INTERRUPT
- [GitHub #43750](https://github.com/zephyrproject-rtos/zephyr/issues/43750) - ADC Driver build is broken for STM32L412
- [GitHub #43745](https://github.com/zephyrproject-rtos/zephyr/issues/43745) - Xtensa XCC Build spi\_nor.c fail
- [GitHub #43742](https://github.com/zephyrproject-rtos/zephyr/issues/43742) - BT510 lis2dh sensor does not disconnect SAO pull-up resistor
- [GitHub #43739](https://github.com/zephyrproject-rtos/zephyr/issues/43739) - tests: dma: random failure on dma loopback suspend and resume case on twr\_ke18f
- [GitHub #43732](https://github.com/zephyrproject-rtos/zephyr/issues/43732) - esp32: MQTT publisher sample stuck for both TLS and non-TLS sample.
- [GitHub #43728](https://github.com/zephyrproject-rtos/zephyr/issues/43728) - esp32 build error while applicaton in T2 topology
- [GitHub #43718](https://github.com/zephyrproject-rtos/zephyr/issues/43718) - Bluetooth: bt\_conn: Unable to allocate buffer within timeout
- [GitHub #43715](https://github.com/zephyrproject-rtos/zephyr/issues/43715) - ESP32 UART devicetree binding design issue
- [GitHub #43713](https://github.com/zephyrproject-rtos/zephyr/issues/43713) - intel\_adsp\_cavs: tests are not running with twister
- [GitHub #43711](https://github.com/zephyrproject-rtos/zephyr/issues/43711) - samples: tfm: psa Some TFM/psa samples fail on nrf platforms
- [GitHub #43702](https://github.com/zephyrproject-rtos/zephyr/issues/43702) - samples/arch/smp/pktqueue not working on ESP32
- [GitHub #43700](https://github.com/zephyrproject-rtos/zephyr/issues/43700) - mgmt/mcumgr: Strange Kconfig names for MCUMGR\_GRP\_ZEPHYR\_BASIC log levels
- [GitHub #43699](https://github.com/zephyrproject-rtos/zephyr/issues/43699) - Bluetooth Mesh working with legacy and extended advertising simultaneously
- [GitHub #43693](https://github.com/zephyrproject-rtos/zephyr/issues/43693) - LE Audio: Rename enum bt\_audio\_pac\_type
- [GitHub #43669](https://github.com/zephyrproject-rtos/zephyr/issues/43669) - LSM6DSL IMU driver - incorrect register definitions
- [GitHub #43663](https://github.com/zephyrproject-rtos/zephyr/issues/43663) - stm32f091 test tests/kernel/context/ test\_kernel\_cpu\_idle fails
- [GitHub #43661](https://github.com/zephyrproject-rtos/zephyr/issues/43661) - Newlib math library not working with user mode threads
- [GitHub #43656](https://github.com/zephyrproject-rtos/zephyr/issues/43656) - samples:bluetoooth:direction\_finding\_connectionless\_rx antenna switching not working with nRF5340
- [GitHub #43654](https://github.com/zephyrproject-rtos/zephyr/issues/43654) - Nominate Mehmet Alperen Sener as Bluetooth Mesh Collaborator
- [GitHub #43649](https://github.com/zephyrproject-rtos/zephyr/issues/43649) - Best practice for “external libraries” and cmake
- [GitHub #43647](https://github.com/zephyrproject-rtos/zephyr/issues/43647) - Bluetooth: LE multirole: connection as central is not totally unreferenced on disconnection
- [GitHub #43640](https://github.com/zephyrproject-rtos/zephyr/issues/43640) - stm32f1: Convert `choice GPIO_STM32_SWJ` to dt
- [GitHub #43636](https://github.com/zephyrproject-rtos/zephyr/issues/43636) - Documentation incorrectly states that C++ new and delete operators are unsupported
- [GitHub #43630](https://github.com/zephyrproject-rtos/zephyr/issues/43630) - Zperf tcp download stalls with window size becoming 0 on Zephyr side
- [GitHub #43618](https://github.com/zephyrproject-rtos/zephyr/issues/43618) - Invalid thread indexes out of userspace generation
- [GitHub #43600](https://github.com/zephyrproject-rtos/zephyr/issues/43600) - tests: mec15xxevb\_assy6853: most of the test cases failed
- [GitHub #43587](https://github.com/zephyrproject-rtos/zephyr/issues/43587) - arm: trustzone: Interrupts using FPU causes usage fault when ARM\_NONSECURE\_PREEMPTIBLE\_SECURE\_CALLS is disabled
- [GitHub #43580](https://github.com/zephyrproject-rtos/zephyr/issues/43580) - hl7800: tcp stack freezes on slow response from modem
- [GitHub #43573](https://github.com/zephyrproject-rtos/zephyr/issues/43573) - return const struct device \* for device\_get\_binding(const char \*name)
- [GitHub #43568](https://github.com/zephyrproject-rtos/zephyr/issues/43568) - ITE eSPI driver expecting OOB header also along with OOB data from app code - espi\_it8xxx2\_send\_oob() & espi\_it8xxx2\_receive\_oob
- [GitHub #43567](https://github.com/zephyrproject-rtos/zephyr/issues/43567) - Bluetooth: Controller: ISO data packet dropped on payload array wraparound
- [GitHub #43553](https://github.com/zephyrproject-rtos/zephyr/issues/43553) - Request to configure SPBTLE-1S of STEVAL-MKSBOX1V1
- [GitHub #43552](https://github.com/zephyrproject-rtos/zephyr/issues/43552) - samples: bluetooth: direction\_finding: Sample fails on nrf5340
- [GitHub #43543](https://github.com/zephyrproject-rtos/zephyr/issues/43543) - RFC: API Change: Bluetooth: struct bt\_auth\_cb field removal
- [GitHub #43525](https://github.com/zephyrproject-rtos/zephyr/issues/43525) - Default network interface selection by up-state
- [GitHub #43518](https://github.com/zephyrproject-rtos/zephyr/issues/43518) - ‘DT\_N\_S\_soc\_S\_timers\_40012c00\_S\_pwm’ undeclared
- [GitHub #43513](https://github.com/zephyrproject-rtos/zephyr/issues/43513) - it8xxx2\_evb: tests/kernel/sleep failed
- [GitHub #43512](https://github.com/zephyrproject-rtos/zephyr/issues/43512) - wifi: esp\_at: sockets not cleaned up on close
- [GitHub #43511](https://github.com/zephyrproject-rtos/zephyr/issues/43511) - lvgl: upgrade to 8.2 build problem
- [GitHub #43505](https://github.com/zephyrproject-rtos/zephyr/issues/43505) - `py` command not found when using nanopb on windows
- [GitHub #43503](https://github.com/zephyrproject-rtos/zephyr/issues/43503) - Build Version detection not working when Zephyr Kernel is a Git Submodule
- [GitHub #43490](https://github.com/zephyrproject-rtos/zephyr/issues/43490) - net: sockets: userspace accept() crashes with NULL addr/addrlen pointer
- [GitHub #43487](https://github.com/zephyrproject-rtos/zephyr/issues/43487) - LE Audio: Broadcast audio sample
- [GitHub #43476](https://github.com/zephyrproject-rtos/zephyr/issues/43476) - tests: nrf: Output of nrf5340dk\_nrf5340\_cpuapp\_ns not available
- [GitHub #43470](https://github.com/zephyrproject-rtos/zephyr/issues/43470) - wifi: esp\_at: race condition on mutex’s leading to deadlock
- [GitHub #43469](https://github.com/zephyrproject-rtos/zephyr/issues/43469) - USBD\_CLASS\_DESCR\_DEFINE section name bug
- [GitHub #43465](https://github.com/zephyrproject-rtos/zephyr/issues/43465) - ‘Malformed data’ on bt\_data\_parse() for every ble adv packet on bbc\_microbit
- [GitHub #43456](https://github.com/zephyrproject-rtos/zephyr/issues/43456) - winc1500 wifi driver fails to build
- [GitHub #43452](https://github.com/zephyrproject-rtos/zephyr/issues/43452) - Missing SPI SCK on STM32F103vctx
- [GitHub #43448](https://github.com/zephyrproject-rtos/zephyr/issues/43448) - Deadlock detection in `bt_att_req_alloc` ineffective when `CONFIG_BT_RECV_IS_RX_THREAD=n`
- [GitHub #43440](https://github.com/zephyrproject-rtos/zephyr/issues/43440) - Bluetooth: L2CAP send le data lack calling net\_buf\_unref() function
- [GitHub #43430](https://github.com/zephyrproject-rtos/zephyr/issues/43430) - Is there any plan to develop zephyr to mircrokenrel architecture?
- [GitHub #43425](https://github.com/zephyrproject-rtos/zephyr/issues/43425) - zephyr+Linux+hypervisor on Raspberry Pi 4
- [GitHub #43419](https://github.com/zephyrproject-rtos/zephyr/issues/43419) - Pull request not updated after force push the original branch
- [GitHub #43411](https://github.com/zephyrproject-rtos/zephyr/issues/43411) - STM32 SPI DMA issue
- [GitHub #43409](https://github.com/zephyrproject-rtos/zephyr/issues/43409) - frdm\_k64f: USB connection gets lost after continuous testing
- [GitHub #43400](https://github.com/zephyrproject-rtos/zephyr/issues/43400) - nrf board system\_off sample application does not work on P1 buttons
- [GitHub #43392](https://github.com/zephyrproject-rtos/zephyr/issues/43392) - Bluetooth: ISO: unallocated memory written during mem\_init
- [GitHub #43389](https://github.com/zephyrproject-rtos/zephyr/issues/43389) - LoRaWAN on Nordic and SX1276 & SX1262 Shield
- [GitHub #43382](https://github.com/zephyrproject-rtos/zephyr/issues/43382) - mgmt/mcumgr/lib: Echo OS command echoes back empty string witn no error when string is too long to handle
- [GitHub #43378](https://github.com/zephyrproject-rtos/zephyr/issues/43378) - TLS availability misdetection when ZEPHYR\_TOOLCHAIN\_VARIANT is not set
- [GitHub #43372](https://github.com/zephyrproject-rtos/zephyr/issues/43372) - pm: lptim: stm32h7: pending irq stops STANDBY
- [GitHub #43369](https://github.com/zephyrproject-rtos/zephyr/issues/43369) - Use Zephyr crc implementation for LittleFS
- [GitHub #43359](https://github.com/zephyrproject-rtos/zephyr/issues/43359) - Bluetooth: ASCS QoS config should not fail for preferred settings
- [GitHub #43348](https://github.com/zephyrproject-rtos/zephyr/issues/43348) - twister:skipped case num issue when use –only-failed.
- [GitHub #43345](https://github.com/zephyrproject-rtos/zephyr/issues/43345) - Bluetooth: Controller: Extended and Periodic Advertising Link Layer Component Test Coverage
- [GitHub #43344](https://github.com/zephyrproject-rtos/zephyr/issues/43344) - intel\_adsp\_cavs25: samples/subsys/logging/syst is failing with a timeout when the sample is enabled to run on intel\_adsp\_cavs25
- [GitHub #43333](https://github.com/zephyrproject-rtos/zephyr/issues/43333) - RFC: Bring zcbor as CBOR decoder/encoder in replacement for TinyCBOR
- [GitHub #43326](https://github.com/zephyrproject-rtos/zephyr/issues/43326) - Unstable SD Card performance on Teensy 4.1
- [GitHub #43319](https://github.com/zephyrproject-rtos/zephyr/issues/43319) - Hardware reset cause api sets reset pin bit every time the api is called
- [GitHub #43316](https://github.com/zephyrproject-rtos/zephyr/issues/43316) - stm32wl55 cannot enable PLL source as MSI
- [GitHub #43314](https://github.com/zephyrproject-rtos/zephyr/issues/43314) - LE Audio: BAP `sent` callback missing
- [GitHub #43310](https://github.com/zephyrproject-rtos/zephyr/issues/43310) - disco\_l475\_iot1: BLE not working
- [GitHub #43306](https://github.com/zephyrproject-rtos/zephyr/issues/43306) - sam\_e70b\_xplained: the platform will be not normal after running test case tests/subsys/usb/desc\_sections/
- [GitHub #43305](https://github.com/zephyrproject-rtos/zephyr/issues/43305) - wifi: esp\_at: shell command “wifi scan” not working well
- [GitHub #43295](https://github.com/zephyrproject-rtos/zephyr/issues/43295) - mimxrt685\_evk\_cm33: Hard fault with `CONFIG_FLASH=y`
- [GitHub #43292](https://github.com/zephyrproject-rtos/zephyr/issues/43292) - NXP RT11xx devicetree missing GPIO7, GPIO8, GPIO12
- [GitHub #43285](https://github.com/zephyrproject-rtos/zephyr/issues/43285) - nRF5x System Off demo fails to put the nRF52840DK into system off
- [GitHub #43284](https://github.com/zephyrproject-rtos/zephyr/issues/43284) - samples: drivers: watchdog failed in mec15xxevb\_assy6853
- [GitHub #43277](https://github.com/zephyrproject-rtos/zephyr/issues/43277) - usb/dfu: upgrade request is not called while used from mcuboot, update doesn’t happen
- [GitHub #43276](https://github.com/zephyrproject-rtos/zephyr/issues/43276) - tests: up\_squared: testsuite tests/kernel/sched/deadline/ failed
- [GitHub #43271](https://github.com/zephyrproject-rtos/zephyr/issues/43271) - tests: acrn\_ehl\_crb: tests/arch/x86/info failed
- [GitHub #43268](https://github.com/zephyrproject-rtos/zephyr/issues/43268) - LE Audio: Add stream ops callbacks for unicast server
- [GitHub #43258](https://github.com/zephyrproject-rtos/zephyr/issues/43258) - HCI core data buffer overflow with ESP32-C3 in Peripheral HR sample
- [GitHub #43248](https://github.com/zephyrproject-rtos/zephyr/issues/43248) - Bluetooth: Mesh: Unable used with ext adv on native\_posix
- [GitHub #43235](https://github.com/zephyrproject-rtos/zephyr/issues/43235) - STM32 platform does not handle large i2c\_write() correctly
- [GitHub #43230](https://github.com/zephyrproject-rtos/zephyr/issues/43230) - Deprecate DT\_CHOSEN\_ZEPHYR\_ENTROPY\_LABEL
- [GitHub #43229](https://github.com/zephyrproject-rtos/zephyr/issues/43229) - nvs: change nvs\_init to accept a device reference
- [GitHub #43218](https://github.com/zephyrproject-rtos/zephyr/issues/43218) - nucleo\_wb55rg: Partition update required to use 0.13.0 BLE firmware
- [GitHub #43205](https://github.com/zephyrproject-rtos/zephyr/issues/43205) - UART console broken since 099850e916ad86e99b3af6821b8c9eb73ba91abf
- [GitHub #43203](https://github.com/zephyrproject-rtos/zephyr/issues/43203) - BLE: With BT\_SETTINGS and BT\_SMP, second connection blocks the system in connection event notification
- [GitHub #43192](https://github.com/zephyrproject-rtos/zephyr/issues/43192) - lvgl: upgrade LVGL to 8.1 build error
- [GitHub #43190](https://github.com/zephyrproject-rtos/zephyr/issues/43190) - Bluetooth: audio: HCI command timeout on LE Setup Isochronous Data Path
- [GitHub #43186](https://github.com/zephyrproject-rtos/zephyr/issues/43186) - Bluetooth: import nrf ble\_db\_discovery library to zephyr
- [GitHub #43172](https://github.com/zephyrproject-rtos/zephyr/issues/43172) - CONFIG\_BT\_MESH\_ADV\_EXT doesn’t build without CONFIG\_BT\_MESH\_RELAY
- [GitHub #43163](https://github.com/zephyrproject-rtos/zephyr/issues/43163) - Applications not pulling LVGL cannot be configured or compiled
- [GitHub #43159](https://github.com/zephyrproject-rtos/zephyr/issues/43159) - hal: stm32: ltdc pins should be very-high-speed
- [GitHub #43142](https://github.com/zephyrproject-rtos/zephyr/issues/43142) - Ethernet and PPP communication conflicts
- [GitHub #43136](https://github.com/zephyrproject-rtos/zephyr/issues/43136) - STM32 Uart log never take effect
- [GitHub #43132](https://github.com/zephyrproject-rtos/zephyr/issues/43132) - Thingy:52 i2c\_nrfx\_twim: Error 0x0BAE0001 occurred for message
- [GitHub #43131](https://github.com/zephyrproject-rtos/zephyr/issues/43131) - LPCXPresso55S69-evk dtsi file incorrect
- [GitHub #43130](https://github.com/zephyrproject-rtos/zephyr/issues/43130) - STM32WL ADC idles / doesn’t work
- [GitHub #43117](https://github.com/zephyrproject-rtos/zephyr/issues/43117) - Not possible to create more than one shield.
- [GitHub #43109](https://github.com/zephyrproject-rtos/zephyr/issues/43109) - drivers:peci:xec: PECI Command ‘Ping’ does not work properly
- [GitHub #43099](https://github.com/zephyrproject-rtos/zephyr/issues/43099) - CMake: ARCH roots issue
- [GitHub #43095](https://github.com/zephyrproject-rtos/zephyr/issues/43095) - Inconsistent logging config result resulted from menuconfig.
- [GitHub #43094](https://github.com/zephyrproject-rtos/zephyr/issues/43094) - CMake stack overflow after changing the build/zephyr/.config, even just timestamp.
- [GitHub #43090](https://github.com/zephyrproject-rtos/zephyr/issues/43090) - mimxrt685\_evk\_cm33: USB examples not working on Zephyr v3.0.0
- [GitHub #43087](https://github.com/zephyrproject-rtos/zephyr/issues/43087) - XCC build failures for all intel\_adsp tests/platforms
- [GitHub #43081](https://github.com/zephyrproject-rtos/zephyr/issues/43081) - [Slack] Slack invite works only on very few mail addresses - this should be changed!
- [GitHub #43066](https://github.com/zephyrproject-rtos/zephyr/issues/43066) - stm32wl55 true RNG falls in seed error
- [GitHub #43058](https://github.com/zephyrproject-rtos/zephyr/issues/43058) - PACS: Fix PAC capabilities to be exposed in PAC Sink/Source characteristic
- [GitHub #43057](https://github.com/zephyrproject-rtos/zephyr/issues/43057) - twister: error while executing twister script on windows machine for sample example code
- [GitHub #43046](https://github.com/zephyrproject-rtos/zephyr/issues/43046) - Wifi sample not working with disco\_l475\_iot1
- [GitHub #43034](https://github.com/zephyrproject-rtos/zephyr/issues/43034) - Documentation for `console_putchar` function is incorrect
- [GitHub #43024](https://github.com/zephyrproject-rtos/zephyr/issues/43024) - samples: tests task wdt fails on some stm32 nucleo target boards
- [GitHub #43020](https://github.com/zephyrproject-rtos/zephyr/issues/43020) - samples/subsys/fs/littlefs does not work with native\_posix board on WSL2
- [GitHub #43016](https://github.com/zephyrproject-rtos/zephyr/issues/43016) - Self inc/dec works incorrectly with logging API.
- [GitHub #42997](https://github.com/zephyrproject-rtos/zephyr/issues/42997) - Bluetooth: Controller: Receiving Periodic Advertising Reports with larger AD Data post v3.0.0-rc2
- [GitHub #42988](https://github.com/zephyrproject-rtos/zephyr/issues/42988) - Specify and standardize undefined behavior on empty response from server for http\_client
- [GitHub #42960](https://github.com/zephyrproject-rtos/zephyr/issues/42960) - Bluetooth: Audio: Codec config parsing and documentation
- [GitHub #42953](https://github.com/zephyrproject-rtos/zephyr/issues/42953) - it8xxx2\_evb: Test in tests/kernel/timer/timer\_api fail.
- [GitHub #42940](https://github.com/zephyrproject-rtos/zephyr/issues/42940) - Please add zsock\_getpeername
- [GitHub #42928](https://github.com/zephyrproject-rtos/zephyr/issues/42928) - CSIS: Invalid usage of bt\_conn\_auth\_cb callbacks
- [GitHub #42888](https://github.com/zephyrproject-rtos/zephyr/issues/42888) - Bluetooth: Controller: Extended Advertising - Advertising Privacy Support
- [GitHub #42881](https://github.com/zephyrproject-rtos/zephyr/issues/42881) - Arduino due missing ‘arduino\_i2c’ alias.
- [GitHub #42877](https://github.com/zephyrproject-rtos/zephyr/issues/42877) - k\_cycle\_get\_32 returns 0 on start-up on native\_posix
- [GitHub #42874](https://github.com/zephyrproject-rtos/zephyr/issues/42874) - ehl\_crb: samples/kernel/metairq\_dispatch fails when it is run multiple times
- [GitHub #42870](https://github.com/zephyrproject-rtos/zephyr/issues/42870) - Build error due to minimal libc qsort callback cast
- [GitHub #42865](https://github.com/zephyrproject-rtos/zephyr/issues/42865) - openocd configurations missing for stm32mp157c\_dk2 board
- [GitHub #42857](https://github.com/zephyrproject-rtos/zephyr/issues/42857) - sam\_e70b\_xplained: failed to run test cases tests/net/npf and tests/net/bridge
- [GitHub #42856](https://github.com/zephyrproject-rtos/zephyr/issues/42856) - Bluetooth: BAP: Unicast client sample cannot connect
- [GitHub #42854](https://github.com/zephyrproject-rtos/zephyr/issues/42854) - k\_busy\_wait() never returns when called - litex vexriscv soc and cpu on xilinx ac701 board
- [GitHub #42851](https://github.com/zephyrproject-rtos/zephyr/issues/42851) - it8xxx2\_evb: Mutlitple tests in tests/kernel/contex fail.
- [GitHub #42850](https://github.com/zephyrproject-rtos/zephyr/issues/42850) - CONFIG items disappeared in zephyr-3.0-rc3
- [GitHub #42848](https://github.com/zephyrproject-rtos/zephyr/issues/42848) - it8xxx2\_evb: Test in /tests/subsys/cpp/libcxx fail.
- [GitHub #42847](https://github.com/zephyrproject-rtos/zephyr/issues/42847) - it8xxx2\_evb: Multiple tests in tests/subsys/portability/cmsis\_rtos\_v2 fail.
- [GitHub #42831](https://github.com/zephyrproject-rtos/zephyr/issues/42831) - Do the atomic\* functions require protection from optimization?
- [GitHub #42829](https://github.com/zephyrproject-rtos/zephyr/issues/42829) - GATT: bt\_gatt\_is\_subscribed does not work as expected when called from bt\_conn\_cb->connected
- [GitHub #42825](https://github.com/zephyrproject-rtos/zephyr/issues/42825) - MQTT client disconnection (EAGAIN) on publish with big payload
- [GitHub #42817](https://github.com/zephyrproject-rtos/zephyr/issues/42817) - ADC on ST Nucleo H743ZI board with DMA
- [GitHub #42800](https://github.com/zephyrproject-rtos/zephyr/issues/42800) - gptp\_mi neighbor\_prop\_delay is not included in sync\_receipt\_time calculation due cast from double to uint64\_t
- [GitHub #42799](https://github.com/zephyrproject-rtos/zephyr/issues/42799) - gptp correction field in sync follow up message does not have correct endianness
- [GitHub #42774](https://github.com/zephyrproject-rtos/zephyr/issues/42774) - pinctrl-0 issue in device tree building
- [GitHub #42723](https://github.com/zephyrproject-rtos/zephyr/issues/42723) - tests: kernel.condvar: child thread is not running
- [GitHub #42702](https://github.com/zephyrproject-rtos/zephyr/issues/42702) - upsquared: drivers.counter.cmos.seconds\_rate is failing with busted maximum bound when run multiple times
- [GitHub #42685](https://github.com/zephyrproject-rtos/zephyr/issues/42685) - Socket echo server sample code not working in Litex Vexriscv cpu (Xilinx AC701 board)
- [GitHub #42680](https://github.com/zephyrproject-rtos/zephyr/issues/42680) - Missing bt\_conn\_(un)ref for LE Audio and tests
- [GitHub #42599](https://github.com/zephyrproject-rtos/zephyr/issues/42599) - tests: kernel: mem\_protect: mem\_protect fails after reset on stm32wb55 nucleo
- [GitHub #42588](https://github.com/zephyrproject-rtos/zephyr/issues/42588) - lsm6dso
- [GitHub #42587](https://github.com/zephyrproject-rtos/zephyr/issues/42587) - LE Audio: BAP Unicast API use array of pointers instead of array of streams
- [GitHub #42559](https://github.com/zephyrproject-rtos/zephyr/issues/42559) - 6LoCAN samples fail due to null pointer dereference
- [GitHub #42548](https://github.com/zephyrproject-rtos/zephyr/issues/42548) - acrn\_ehl\_crb: twister failed to run tests/subsys/logging due to UnicodeEncodeError after switching to log v2
- [GitHub #42544](https://github.com/zephyrproject-rtos/zephyr/issues/42544) - Bluetooth: controller: llcp: handling of remote procedures with and without instant
- [GitHub #42534](https://github.com/zephyrproject-rtos/zephyr/issues/42534) - BLE Testing functions do not work properly
- [GitHub #42530](https://github.com/zephyrproject-rtos/zephyr/issues/42530) - Possibility to define pinmux item for Pin Control as a plain input/output
- [GitHub #42524](https://github.com/zephyrproject-rtos/zephyr/issues/42524) - Wrong implementation of SPI driver
- [GitHub #42520](https://github.com/zephyrproject-rtos/zephyr/issues/42520) - bt\_ots Doxygen documentation does not seem to be included in the Zephyr project documentation.
- [GitHub #42518](https://github.com/zephyrproject-rtos/zephyr/issues/42518) - Bluetooth Ext Adv:Sync: While simultaneous advertiser are working, and skip is non-zero, sync terminates repeatedly
- [GitHub #42508](https://github.com/zephyrproject-rtos/zephyr/issues/42508) - TWIHS hangs
- [GitHub #42496](https://github.com/zephyrproject-rtos/zephyr/issues/42496) - ARM M4 MPU backed userspace livelocks on stack overflow when FPU enabled
- [GitHub #42478](https://github.com/zephyrproject-rtos/zephyr/issues/42478) - Unable to build mcuboot for b\_u585i\_iot02a
- [GitHub #42453](https://github.com/zephyrproject-rtos/zephyr/issues/42453) - Unable to update Firmware using MCUBoot on STM32G0 series
- [GitHub #42436](https://github.com/zephyrproject-rtos/zephyr/issues/42436) - NXP eDMA overrun errors on SAI RX
- [GitHub #42434](https://github.com/zephyrproject-rtos/zephyr/issues/42434) - NXP I2S (SAI) driver bugs
- [GitHub #42432](https://github.com/zephyrproject-rtos/zephyr/issues/42432) - i2c: unable to configure SAMD51 i2c clock frequency for standard (100 KHz) speeds
- [GitHub #42425](https://github.com/zephyrproject-rtos/zephyr/issues/42425) - i2c: sam0 driver does not prevent simultaneous transactions
- [GitHub #42351](https://github.com/zephyrproject-rtos/zephyr/issues/42351) - stm32H743 nucleo board cannot flash after tests/drivers/flash
- [GitHub #42343](https://github.com/zephyrproject-rtos/zephyr/issues/42343) - LE Audio: PACS: Server change location
- [GitHub #42342](https://github.com/zephyrproject-rtos/zephyr/issues/42342) - LE Audio: PACS notify changes to locations
- [GitHub #42333](https://github.com/zephyrproject-rtos/zephyr/issues/42333) - Cannot write to qspi flash in adafruit feather nrf52840, device tree is wrong
- [GitHub #42310](https://github.com/zephyrproject-rtos/zephyr/issues/42310) - Support for TCA6408A gpio expander, which existing driver as a base?
- [GitHub #42306](https://github.com/zephyrproject-rtos/zephyr/issues/42306) - Bluetooth: Host: More than `CONFIG_BT_EATT_MAX` EATT channels may be created
- [GitHub #42290](https://github.com/zephyrproject-rtos/zephyr/issues/42290) - ESP32 - Heltec Wifi - Possibly invalid CONFIG\_ESP32\_XTAL\_FREQ setting (40MHz). Detected 26 MHz
- [GitHub #42235](https://github.com/zephyrproject-rtos/zephyr/issues/42235) - SocketCAN not supported for NUCLEO H743ZI
- [GitHub #42227](https://github.com/zephyrproject-rtos/zephyr/issues/42227) - Teensy41 support SDHC - Storage init Error
- [GitHub #42189](https://github.com/zephyrproject-rtos/zephyr/issues/42189) - Sub 1GHz Support for CC1352
- [GitHub #42181](https://github.com/zephyrproject-rtos/zephyr/issues/42181) - Ethernet PHY imxrt1060 Teensy not working, sample with DHCPv4\_client fails
- [GitHub #42113](https://github.com/zephyrproject-rtos/zephyr/issues/42113) - Modbus RTU allow non-compliant client configuration
- [GitHub #42108](https://github.com/zephyrproject-rtos/zephyr/issues/42108) - upsquared: isr\_dynamic & isr\_regular test is failing
- [GitHub #42102](https://github.com/zephyrproject-rtos/zephyr/issues/42102) - doc: searches for sys\_reboot() are inconsistent
- [GitHub #42096](https://github.com/zephyrproject-rtos/zephyr/issues/42096) - LE Audio: Media: Pass structs by reference and not value
- [GitHub #42090](https://github.com/zephyrproject-rtos/zephyr/issues/42090) - Bluetooth: Audio: MCS BSIM notification length warning
- [GitHub #42083](https://github.com/zephyrproject-rtos/zephyr/issues/42083) - Bluetooth: ISO: Packet Sequence Number should be incremented for each channel
- [GitHub #42081](https://github.com/zephyrproject-rtos/zephyr/issues/42081) - Direction finding code support for nrf52811?
- [GitHub #42072](https://github.com/zephyrproject-rtos/zephyr/issues/42072) - west: spdx: Blank FileChecksum field for missing build file
- [GitHub #42050](https://github.com/zephyrproject-rtos/zephyr/issues/42050) - printk bug: A function called from printk is invoked three times given certain configuration variables
- [GitHub #42015](https://github.com/zephyrproject-rtos/zephyr/issues/42015) - LED api can’t be called from devicetree phandle
- [GitHub #42011](https://github.com/zephyrproject-rtos/zephyr/issues/42011) - Establish guidelines for TSC working groups
- [GitHub #42000](https://github.com/zephyrproject-rtos/zephyr/issues/42000) - BQ274xx driver not working correctly
- [GitHub #41995](https://github.com/zephyrproject-rtos/zephyr/issues/41995) - tracing: riscv: Missing invoking the sys\_trace\_isr\_exit()
- [GitHub #41947](https://github.com/zephyrproject-rtos/zephyr/issues/41947) - lpcxpresso55s16 SPI hardware chip select not working
- [GitHub #41946](https://github.com/zephyrproject-rtos/zephyr/issues/41946) - Bluetooth: ISO: Sending on RX-only CIS doesn’t report error
- [GitHub #41944](https://github.com/zephyrproject-rtos/zephyr/issues/41944) - Assertion triggered when system is going to PM\_STATE\_SOFT\_OFF
- [GitHub #41931](https://github.com/zephyrproject-rtos/zephyr/issues/41931) - drivers: audio: tlv320dac310x: device config used as non-const
- [GitHub #41924](https://github.com/zephyrproject-rtos/zephyr/issues/41924) - drivers: dma/i2c: nios2: config used as non-const
- [GitHub #41921](https://github.com/zephyrproject-rtos/zephyr/issues/41921) - Fast USB DFU workflow
- [GitHub #41899](https://github.com/zephyrproject-rtos/zephyr/issues/41899) - ESP32 Wifi mDNS
- [GitHub #41874](https://github.com/zephyrproject-rtos/zephyr/issues/41874) - Recursive spinlock error on ARM in specific circumstances
- [GitHub #41864](https://github.com/zephyrproject-rtos/zephyr/issues/41864) - ESP32 Wifi AP Mode DHCP Service
- [GitHub #41823](https://github.com/zephyrproject-rtos/zephyr/issues/41823) - Bluetooth: Controller: llcp: Remote request are dropped due to lack of free proc\_ctx
- [GitHub #41788](https://github.com/zephyrproject-rtos/zephyr/issues/41788) - Bluetooth: Controller: llcp: Refectored PHY Update procedure asserts while waiting for free buffers to send notifications
- [GitHub #41787](https://github.com/zephyrproject-rtos/zephyr/issues/41787) - Alignment issue on Cortex M7
- [GitHub #41777](https://github.com/zephyrproject-rtos/zephyr/issues/41777) - periodic\_adv periodic\_sync lost data
- [GitHub #41773](https://github.com/zephyrproject-rtos/zephyr/issues/41773) - LoRaWAN: Unable to correctly join networks of any version on LTS
- [GitHub #41742](https://github.com/zephyrproject-rtos/zephyr/issues/41742) - stm32g0: stm32\_temp: not working
- [GitHub #41710](https://github.com/zephyrproject-rtos/zephyr/issues/41710) - tests: ztest: ztress: Test randomly fails on qemu\_cortex\_a9
- [GitHub #41677](https://github.com/zephyrproject-rtos/zephyr/issues/41677) - undefined reference to `\_\_device\_dts\_ord\_xx’
- [GitHub #41667](https://github.com/zephyrproject-rtos/zephyr/issues/41667) - doc: arm: mec172x: MEC172x EVB documentation points to some inexistent jumpers
- [GitHub #41652](https://github.com/zephyrproject-rtos/zephyr/issues/41652) - Bluetooth: Controller: BIG: Channel map update BIG: Generation of BIG\_CHANNEL\_MAP\_IND (sent 6 times)
- [GitHub #41651](https://github.com/zephyrproject-rtos/zephyr/issues/41651) - Bluetooth: Controller: BIG Sync: Channel map update of BIG
- [GitHub #41650](https://github.com/zephyrproject-rtos/zephyr/issues/41650) - STM32H7 SPI123 incorrect clock source used for prescaler calculation
- [GitHub #41642](https://github.com/zephyrproject-rtos/zephyr/issues/41642) - Deploy generated docs from PRs
- [GitHub #41628](https://github.com/zephyrproject-rtos/zephyr/issues/41628) - Move LVGL glue code to zephyr/modules/
- [GitHub #41613](https://github.com/zephyrproject-rtos/zephyr/issues/41613) - Process: Review and update Milestone Definitions
- [GitHub #41597](https://github.com/zephyrproject-rtos/zephyr/issues/41597) - Unable to build mcuboot for BL654\_DVK
- [GitHub #41596](https://github.com/zephyrproject-rtos/zephyr/issues/41596) - Split connected ISO client and server by Kconfig
- [GitHub #41594](https://github.com/zephyrproject-rtos/zephyr/issues/41594) - LE Audio: Upstream CCP/TBS
- [GitHub #41593](https://github.com/zephyrproject-rtos/zephyr/issues/41593) - LE Audio: Upstream BASS
- [GitHub #41592](https://github.com/zephyrproject-rtos/zephyr/issues/41592) - Object Transfer Service Client made “official”
- [GitHub #41590](https://github.com/zephyrproject-rtos/zephyr/issues/41590) - LE Audio: CAP API - Acceptor
- [GitHub #41517](https://github.com/zephyrproject-rtos/zephyr/issues/41517) - Hard fault if `CONFIG_LOG2_MODE_DEFERRED` is enabled
- [GitHub #41472](https://github.com/zephyrproject-rtos/zephyr/issues/41472) - Unable to mount fat file system on nucleo\_f429zi
- [GitHub #41449](https://github.com/zephyrproject-rtos/zephyr/issues/41449) - PWM capture with STM32
- [GitHub #41408](https://github.com/zephyrproject-rtos/zephyr/issues/41408) - Low power states for STM32 H7
- [GitHub #41388](https://github.com/zephyrproject-rtos/zephyr/issues/41388) - tests: coverage: test code coverage report failed on mps2\_an385
- [GitHub #41382](https://github.com/zephyrproject-rtos/zephyr/issues/41382) - nordic nrf52/nrf53 and missing cpu-power-states (dts) for automatic device PM control
- [GitHub #41375](https://github.com/zephyrproject-rtos/zephyr/issues/41375) - hal\_nordic: update 15.4 driver to newest version
- [GitHub #41297](https://github.com/zephyrproject-rtos/zephyr/issues/41297) - QSPI flash need read, write via 4 lines not 1 line
- [GitHub #41285](https://github.com/zephyrproject-rtos/zephyr/issues/41285) - pthread\_once has incorrect behavior
- [GitHub #41230](https://github.com/zephyrproject-rtos/zephyr/issues/41230) - LE Audio: API Architecture and documentation for GAF
- [GitHub #41228](https://github.com/zephyrproject-rtos/zephyr/issues/41228) - LE Audio: Add a codec to Zephyr
- [GitHub #41220](https://github.com/zephyrproject-rtos/zephyr/issues/41220) - STM32H7: Check for VOSRDY instead of ACTVOSRDY
- [GitHub #41201](https://github.com/zephyrproject-rtos/zephyr/issues/41201) - LE Audio: Improved media\_proxy internal data structure
- [GitHub #41200](https://github.com/zephyrproject-rtos/zephyr/issues/41200) - LE Audio: Other postponed MCS cleanups
- [GitHub #41196](https://github.com/zephyrproject-rtos/zephyr/issues/41196) - LE Audio: Reconfigure Unicast Group after creation
- [GitHub #41194](https://github.com/zephyrproject-rtos/zephyr/issues/41194) - LE Audio: Remove support for bidirectional audio streams
- [GitHub #41192](https://github.com/zephyrproject-rtos/zephyr/issues/41192) - LE Audio: Change PACS from indicate to notify
- [GitHub #41191](https://github.com/zephyrproject-rtos/zephyr/issues/41191) - LE Audio: Update pac\_indicate to actually send data
- [GitHub #41188](https://github.com/zephyrproject-rtos/zephyr/issues/41188) - LE Audio: Remove stream (dis)connected callback from stream ops
- [GitHub #41186](https://github.com/zephyrproject-rtos/zephyr/issues/41186) - LE Audio: CAP API - Initiator
- [GitHub #41169](https://github.com/zephyrproject-rtos/zephyr/issues/41169) - twister: program get stuck when serial in hardware map is empty string
- [GitHub #41151](https://github.com/zephyrproject-rtos/zephyr/issues/41151) - RFC: Provide k\_realloc()
- [GitHub #41093](https://github.com/zephyrproject-rtos/zephyr/issues/41093) - Kconfig.defconfig:11: error: couldn’t parse ‘default $(dt\_node\_int\_prop\_int,/cpus/cpu@0,clock-frequency)’
- [GitHub #40970](https://github.com/zephyrproject-rtos/zephyr/issues/40970) - Upgrade qemu to fix breakage in mps3-an547
- [GitHub #40920](https://github.com/zephyrproject-rtos/zephyr/issues/40920) - Bluetooth audio: client/server naming scheme
- [GitHub #40901](https://github.com/zephyrproject-rtos/zephyr/issues/40901) - RFC: API Change: update LVGL from v7 to v8
- [GitHub #40874](https://github.com/zephyrproject-rtos/zephyr/issues/40874) - mps2\_an521\_ns: fail to handle user\_string\_alloc\_copy() with null parameter
- [GitHub #40856](https://github.com/zephyrproject-rtos/zephyr/issues/40856) - PPP: gsm\_modem: LCP never gets past REQUEST\_SENT phase
- [GitHub #40775](https://github.com/zephyrproject-rtos/zephyr/issues/40775) - stm32: multi-threading broken after #40173
- [GitHub #40679](https://github.com/zephyrproject-rtos/zephyr/issues/40679) - libc/minimal: static variable of gmtime() does not located to z\_libc\_partition at usermode.
- [GitHub #40657](https://github.com/zephyrproject-rtos/zephyr/issues/40657) - Cannot enable secondary pwm out channels on stm32f3
- [GitHub #40635](https://github.com/zephyrproject-rtos/zephyr/issues/40635) - gen\_app\_partitions.py may not include all object files produced by build system
- [GitHub #40620](https://github.com/zephyrproject-rtos/zephyr/issues/40620) - zephyr with cadence xtensa core dsp LX7 ，helloworld program cannot be entered after the program is executed
- [GitHub #40593](https://github.com/zephyrproject-rtos/zephyr/issues/40593) - tests: lib: cmsis\_dsp: Overflows in libraries.cmsis\_dsp.matrix
- [GitHub #40591](https://github.com/zephyrproject-rtos/zephyr/issues/40591) - RFC: Replace TinyCBOR with ZCBOR within Zephyr
- [GitHub #40588](https://github.com/zephyrproject-rtos/zephyr/issues/40588) - mgmg/mcumg/lib: Replace TinyCBOR with zcbor
- [GitHub #40559](https://github.com/zephyrproject-rtos/zephyr/issues/40559) - Move LittlefFS configuration header and CMakeLists.txt from module to zephyr/modules
- [GitHub #40371](https://github.com/zephyrproject-rtos/zephyr/issues/40371) - modem: uart interface does not disable TX interrupt in ISR
- [GitHub #40360](https://github.com/zephyrproject-rtos/zephyr/issues/40360) - Error messages with the sample: Asynchronous Socket Echo Server Using select()
- [GitHub #40306](https://github.com/zephyrproject-rtos/zephyr/issues/40306) - ESP32 BLE transmit error
- [GitHub #40298](https://github.com/zephyrproject-rtos/zephyr/issues/40298) - Bluetooth assertions in lll\_conn.c
- [GitHub #40204](https://github.com/zephyrproject-rtos/zephyr/issues/40204) - Bluetooth: ll\_sync\_create\_cancel fails with BT\_HCI\_ERR\_CMD\_DISALLOWED before BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_ESTABLISHED is generated
- [GitHub #40195](https://github.com/zephyrproject-rtos/zephyr/issues/40195) - CONFIG\_BOARD default value using cmake -DBOARD define value
- [GitHub #39948](https://github.com/zephyrproject-rtos/zephyr/issues/39948) - kernel.common.stack\_sentinel fails on qemu\_cortex\_a9
- [GitHub #39922](https://github.com/zephyrproject-rtos/zephyr/issues/39922) - Instruction fetch fault happens on RISC-V with XIP and userspace enabled
- [GitHub #39834](https://github.com/zephyrproject-rtos/zephyr/issues/39834) - [Coverity CID: 240669] Unrecoverable parse warning in subsys/jwt/jwt.c
- [GitHub #39738](https://github.com/zephyrproject-rtos/zephyr/issues/39738) - twister: tests: samples: Skips on integration\_platforms in CI
- [GitHub #39520](https://github.com/zephyrproject-rtos/zephyr/issues/39520) - Add support for the BlueNRG-LP SoC
- [GitHub #39432](https://github.com/zephyrproject-rtos/zephyr/issues/39432) - Periodic adv. syncing takes longer and bt\_le\_per\_adv\_sync\_delete returns error after commit ecf761b4e9
- [GitHub #39314](https://github.com/zephyrproject-rtos/zephyr/issues/39314) - Invalid CONTROLLER\_ID in usb\_dc\_mcux.c for LPC54114
- [GitHub #39194](https://github.com/zephyrproject-rtos/zephyr/issues/39194) - Process: investigate GitHub code review replacements
- [GitHub #39184](https://github.com/zephyrproject-rtos/zephyr/issues/39184) - HawkBit hash mismatch
- [GitHub #39176](https://github.com/zephyrproject-rtos/zephyr/issues/39176) - overflow in sensor\_value\_from\_double
- [GitHub #39132](https://github.com/zephyrproject-rtos/zephyr/issues/39132) - subsys/net/ip/tcp2: Missing feature to decrease Receive Window size sent in the ACK messge
- [GitHub #38978](https://github.com/zephyrproject-rtos/zephyr/issues/38978) - Esp32 compilation error after enabling CONFIG\_NEWLIB\_LIBC
- [GitHub #38966](https://github.com/zephyrproject-rtos/zephyr/issues/38966) - Please add STM32F412VX
- [GitHub #38747](https://github.com/zephyrproject-rtos/zephyr/issues/38747) - data/json: encoding issues with array in object\_array
- [GitHub #38632](https://github.com/zephyrproject-rtos/zephyr/issues/38632) - Multiple potential dead-locks modem\_socket\_wait\_data
- [GitHub #38570](https://github.com/zephyrproject-rtos/zephyr/issues/38570) - Process: binary blobs in Zephyr
- [GitHub #38567](https://github.com/zephyrproject-rtos/zephyr/issues/38567) - Process: legitimate signed-off-by lines
- [GitHub #38548](https://github.com/zephyrproject-rtos/zephyr/issues/38548) - stm32: QSPI flash driver concurrent access issue
- [GitHub #38305](https://github.com/zephyrproject-rtos/zephyr/issues/38305) - Update to LVGL v8
- [GitHub #38279](https://github.com/zephyrproject-rtos/zephyr/issues/38279) - Bluetooth: Controller: assert LL\_ASSERT(!radio\_is\_ready()) in lll\_conn.c
- [GitHub #38268](https://github.com/zephyrproject-rtos/zephyr/issues/38268) - Multiple defects in “Multi Producer Single Consumer Packet Buffer” library
- [GitHub #38179](https://github.com/zephyrproject-rtos/zephyr/issues/38179) - twister: only report failures in merged junit output
- [GitHub #37798](https://github.com/zephyrproject-rtos/zephyr/issues/37798) - Change nRF5340DK board files to handle CPUNET pin configuration with DTS nodes
- [GitHub #37730](https://github.com/zephyrproject-rtos/zephyr/issues/37730) - http\_client\_req: Timeout likely not working as expected
- [GitHub #37710](https://github.com/zephyrproject-rtos/zephyr/issues/37710) - Bluetooth advert packet size is size of maximum packet not size of actual data
- [GitHub #37683](https://github.com/zephyrproject-rtos/zephyr/issues/37683) - STM32 Eth Tx DMA always uses first descriptor instead of going through circular buffer
- [GitHub #37324](https://github.com/zephyrproject-rtos/zephyr/issues/37324) - subsys/mgmt/hawkbit: Unable to finish download if CPU blocking function (i.e. `flash_img_buffered_write`) is used
- [GitHub #37294](https://github.com/zephyrproject-rtos/zephyr/issues/37294) - RTT logs not found with default west debug invocation on jlink runner
- [GitHub #37191](https://github.com/zephyrproject-rtos/zephyr/issues/37191) - nrf5340: Support +3dBm TX power
- [GitHub #37186](https://github.com/zephyrproject-rtos/zephyr/issues/37186) - entropy: Bluetooth derived entropy device
- [GitHub #36905](https://github.com/zephyrproject-rtos/zephyr/issues/36905) - Improve (k\_)malloc and heap documentation
- [GitHub #36882](https://github.com/zephyrproject-rtos/zephyr/issues/36882) - MCUMGR: fs upload fail for first time file upload
- [GitHub #36645](https://github.com/zephyrproject-rtos/zephyr/issues/36645) - minimal libc: add strtoll and strtoull functions
- [GitHub #36571](https://github.com/zephyrproject-rtos/zephyr/issues/36571) - LoRa support for random DevNonce and NVS stack state storage
- [GitHub #36266](https://github.com/zephyrproject-rtos/zephyr/issues/36266) - kernel timeout\_list NULL pointer access
- [GitHub #35316](https://github.com/zephyrproject-rtos/zephyr/issues/35316) - log\_panic() hangs kernel
- [GitHub #34737](https://github.com/zephyrproject-rtos/zephyr/issues/34737) - Can’t compile CIVETWEB with CONFIG\_NO\_OPTIMIZATIONS or CONFIG\_DEBUG
- [GitHub #34590](https://github.com/zephyrproject-rtos/zephyr/issues/34590) - Functions getopt\_long and getopt\_long\_only from the FreeBSD project
- [GitHub #34256](https://github.com/zephyrproject-rtos/zephyr/issues/34256) - Add support for FVP in CI / SDK
- [GitHub #34218](https://github.com/zephyrproject-rtos/zephyr/issues/34218) - Civetweb server crashing when trying to access invalid resource
- [GitHub #34204](https://github.com/zephyrproject-rtos/zephyr/issues/34204) - nvs\_write: Bad documented return value.
- [GitHub #33876](https://github.com/zephyrproject-rtos/zephyr/issues/33876) - Lora sender sample build error for esp32
- [GitHub #32885](https://github.com/zephyrproject-rtos/zephyr/issues/32885) - Zephyr C++ support documentation conflicts to the code
- [GitHub #31613](https://github.com/zephyrproject-rtos/zephyr/issues/31613) - Undefined reference errors when using External Library with k\_msgq\_\* calls
- [GitHub #30724](https://github.com/zephyrproject-rtos/zephyr/issues/30724) - CAN J1939 Support
- [GitHub #30152](https://github.com/zephyrproject-rtos/zephyr/issues/30152) - Settings nvs subsystem uses a hardcoded flash area label
- [GitHub #29981](https://github.com/zephyrproject-rtos/zephyr/issues/29981) - Improve clock initialization on LPC & MXRT600
- [GitHub #29941](https://github.com/zephyrproject-rtos/zephyr/issues/29941) - Unable to connect Leshan LwM2M server using x86 based LwM2M client
- [GitHub #29199](https://github.com/zephyrproject-rtos/zephyr/issues/29199) - github integration: ensure maintainers are added to PRs that affect them
- [GitHub #29107](https://github.com/zephyrproject-rtos/zephyr/issues/29107) - Bluetooth: hci-usb uses non-standard interfaces
- [GitHub #28009](https://github.com/zephyrproject-rtos/zephyr/issues/28009) - Add connection status to the connection info
- [GitHub #27841](https://github.com/zephyrproject-rtos/zephyr/issues/27841) - samples: disk: unable to access sd card
- [GitHub #27177](https://github.com/zephyrproject-rtos/zephyr/issues/27177) - Unable to build samples/bluetooth/st\_ble\_sensor for steval\_fcu001v1 board
- [GitHub #26731](https://github.com/zephyrproject-rtos/zephyr/issues/26731) - Single channel selection - Bluetooth - Zephyr
- [GitHub #26038](https://github.com/zephyrproject-rtos/zephyr/issues/26038) - build zephyr with llvm fail
- [GitHub #25362](https://github.com/zephyrproject-rtos/zephyr/issues/25362) - better support for posix api read write in socketpair tests
- [GitHub #24733](https://github.com/zephyrproject-rtos/zephyr/issues/24733) - Misconfigured environment
- [GitHub #23347](https://github.com/zephyrproject-rtos/zephyr/issues/23347) - net: ieee802154\_radio: API improvements
- [GitHub #22870](https://github.com/zephyrproject-rtos/zephyr/issues/22870) - Add Cortex-M4 testing platform
- [GitHub #22455](https://github.com/zephyrproject-rtos/zephyr/issues/22455) - How to assign USB endpoint address manually in stm32f4\_disco for CDC ACM class driver
- [GitHub #22247](https://github.com/zephyrproject-rtos/zephyr/issues/22247) - Discussion: Supporting the Arduino ecosystem
- [GitHub #22161](https://github.com/zephyrproject-rtos/zephyr/issues/22161) - add shell command for the settings subsystem
- [GitHub #21994](https://github.com/zephyrproject-rtos/zephyr/issues/21994) - Bluetooth: controller: split: Fix procedure complete event generation
- [GitHub #21409](https://github.com/zephyrproject-rtos/zephyr/issues/21409) - sanitycheck: cmd.exe colorized output
- [GitHub #20269](https://github.com/zephyrproject-rtos/zephyr/issues/20269) - Add support for opamps in MCUs
- [GitHub #19979](https://github.com/zephyrproject-rtos/zephyr/issues/19979) - Implement Cortex-R floating-point support
- [GitHub #19244](https://github.com/zephyrproject-rtos/zephyr/issues/19244) - BLE throughput of DFU by Mcumgr is too slow
- [GitHub #17893](https://github.com/zephyrproject-rtos/zephyr/issues/17893) - dynamic threads don’t work on x86 in some configurations
- [GitHub #17743](https://github.com/zephyrproject-rtos/zephyr/issues/17743) - cross compiling for RISCV32 fails as compiler flags are not supplied by board but must be in target.cmake
- [GitHub #17005](https://github.com/zephyrproject-rtos/zephyr/issues/17005) - Upstreamability of SiLabs RAIL support
- [GitHub #16406](https://github.com/zephyrproject-rtos/zephyr/issues/16406) - west: runners: Add –id and –chiperase options
- [GitHub #16205](https://github.com/zephyrproject-rtos/zephyr/issues/16205) - Add support to west to flash w/o a build, but given a binary
- [GitHub #15820](https://github.com/zephyrproject-rtos/zephyr/issues/15820) - mcumgr: taskstat show name & used size
- [GitHub #14649](https://github.com/zephyrproject-rtos/zephyr/issues/14649) - CI testing must be retry-free
- [GitHub #14591](https://github.com/zephyrproject-rtos/zephyr/issues/14591) - Infineon Tricore architecture support
- [GitHub #13318](https://github.com/zephyrproject-rtos/zephyr/issues/13318) - k\_thread\_foreach api breaks real time semantics
- [GitHub #9578](https://github.com/zephyrproject-rtos/zephyr/issues/9578) - Windows installation of SDK needs ‘just works’ installer
- [GitHub #8536](https://github.com/zephyrproject-rtos/zephyr/issues/8536) - imxrt1050: Replace systick with gpt or other system timer
- [GitHub #8481](https://github.com/zephyrproject-rtos/zephyr/issues/8481) - Remove the Kconfig helper options for nRF ICs once DT can replace them
- [GitHub #8139](https://github.com/zephyrproject-rtos/zephyr/issues/8139) - Driver for BMA400 accelerometer
- [GitHub #6654](https://github.com/zephyrproject-rtos/zephyr/issues/6654) - efm32wg\_stk3800 bluetooth sample do not compile (add support)
- [GitHub #6162](https://github.com/zephyrproject-rtos/zephyr/issues/6162) - LwM2M: Support Queue Mode Operation
- [GitHub #1495](https://github.com/zephyrproject-rtos/zephyr/issues/1495) - esp32: newlibc errors
- [GitHub #1392](https://github.com/zephyrproject-rtos/zephyr/issues/1392) - No module named ‘elftools’
- [GitHub #3192](https://github.com/zephyrproject-rtos/zephyr/issues/3192) - Shutting down BLE support
- [GitHub #3150](https://github.com/zephyrproject-rtos/zephyr/issues/3150) - Si1153 Ambient Light Sensor, Proximity, and Gesture detector support
