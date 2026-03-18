---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/releases/release-notes-3.0.html
original_path: releases/release-notes-3.0.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Zephyr 3.0.0

We are pleased to announce the release of Zephyr RTOS version 3.0.0.

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

- CVE-2021-3835: [Zephyr project bug tracker GHSA-fm6v-8625-99jf](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-fm6v-8625-99jf)
- CVE-2021-3861: [Zephyr project bug tracker GHSA-hvfp-w4h8-gxvj](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-hvfp-w4h8-gxvj)
- CVE-2021-3966: [Zephyr project bug tracker GHSA-hfxq-3w6x-fv2m](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-hfxq-3w6x-fv2m)

## Known issues

You can check all currently known issues by listing them using the GitHub
interface and listing all issues with the [bug label](https://github.com/zephyrproject-rtos/zephyr/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

## API Changes

### Changes in this release

- Following functions in UART Asynchronous API are using microseconds to represent
  timeout instead of milliseconds:
  \* [`uart_tx()`](../hardware/peripherals/uart.md#c.uart_tx "uart_tx")
  \* [`uart_rx_enable()`](../hardware/peripherals/uart.md#c.uart_rx_enable "uart_rx_enable")
- Replaced custom LwM2M `float32_value` type with a native double type.
- Added function for getting status of USB device remote wakeup feature.
- Added `ranges` and `dma-ranges` as invalid property to be used with DT\_PROP\_LEN()
  along `reg` and `interrupts`.
- The existing [`crc16()`](../services/misc.md#c.crc16 "crc16") and [`crc16_ansi()`](../services/misc.md#c.crc16_ansi "crc16_ansi") functions have been
  modified. The former has a new signature. The latter now properly calculates the
  CRC-16-ANSI checksum. A new function, [`crc16_reflect()`](../services/misc.md#c.crc16_reflect "crc16_reflect"), has been
  introduced to calculated reflected CRCs.
- GATT callbacks `bt_gatt_..._func_t` would previously be called with argument
  `conn = NULL` in the event of a disconnect. This was not documented as part
  of the API. This behavior is changed so the `conn` argument is provided as
  normal when a disconnect occurs.

### Removed APIs in this release

- The following Kconfig options related to radio front-end modules (FEMs) were
  removed:

  - `CONFIG_BT_CTLR_GPIO_PA`
  - `CONFIG_BT_CTLR_GPIO_PA_PIN`
  - `CONFIG_BT_CTLR_GPIO_PA_POL_INV`
  - `CONFIG_BT_CTLR_GPIO_PA_OFFSET`
  - `CONFIG_BT_CTLR_GPIO_LNA`
  - `CONFIG_BT_CTLR_GPIO_LNA_PIN`
  - `CONFIG_BT_CTLR_GPIO_LNA_POL_INV`
  - `CONFIG_BT_CTLR_GPIO_LNA_OFFSET`
  - `CONFIG_BT_CTLR_FEM_NRF21540`
  - `CONFIG_BT_CTLR_GPIO_PDN_PIN`
  - `CONFIG_BT_CTLR_GPIO_PDN_POL_INV`
  - `CONFIG_BT_CTLR_GPIO_CSN_PIN`
  - `CONFIG_BT_CTLR_GPIO_CSN_POL_INV`
  - `CONFIG_BT_CTLR_GPIO_PDN_CSN_OFFSET`

  This FEM configuration is hardware description, and was therefore moved to
  [devicetree](../build/dts/index.md#dt-guide). See the [`nordic,nrf-radio`](../build/dts/api/bindings/net/wireless/nordic%2Cnrf-radio.md#std-dtcompatible-nordic-nrf-radio)
  devicetree binding’s `fem` property for information on what to do instead
  on the Nordic open source controller.
- Removed Kconfig option `CONFIG_USB_UART_CONSOLE`.
  Option `CONFIG_USB_UART_CONSOLE` was only relevant for console driver
  when CDC ACM UART is used as backend. Since the behavior of the CDC ACM UART
  is changed so that it more closely mimics the real UART controller,
  option is no longer necessary.
- Removed Kconfig option `CONFIG_OPENOCD_SUPPORT` in favor of
  `CONFIG_DEBUG_THREAD_INFO`.
- Removed `flash_write_protection_set()` along with the flash write protection
  implementation handler.
- Removed `CAN_BUS_UNKNOWN` and changed the signature of
  [`can_get_state()`](../hardware/peripherals/can/controller.md#c.can_get_state "can_get_state") to return an error code instead.
- Removed `DT_CHOSEN_ZEPHYR_CANBUS_LABEL` in favor of utilizing
  [`DEVICE_DT_GET`](../kernel/drivers/index.md#c.DEVICE_DT_GET "DEVICE_DT_GET").
- Removed `CONFIG_LOG_MINIMAL`. Use `CONFIG_LOG_MODE_MINIMAL` instead.
- STM32 clock\_control driver configuration was moved from Kconfig to [devicetree](../build/dts/index.md#dt-guide).
  See the [`st,stm32-rcc`](../build/dts/api/bindings/clock/st%2Cstm32-rcc.md#std-dtcompatible-st-stm32-rcc) devicetree binding for more information.
  As a consequence, following Kconfig symbols were removed:

  - `CONFIG_CLOCK_STM32_SYSCLK_SRC_HSE`
  - `CONFIG_CLOCK_STM32_SYSCLK_SRC_HSI`
  - `CONFIG_CLOCK_STM32_SYSCLK_SRC_MSI`
  - `CONFIG_CLOCK_STM32_SYSCLK_SRC_PLL`
  - `CONFIG_CLOCK_STM32_SYSCLK_SRC_CSI`
  - `CONFIG_CLOCK_STM32_HSE_BYPASS`
  - `CONFIG_CLOCK_STM32_MSI_RANGE`
  - `CONFIG_CLOCK_STM32_PLL_SRC_MSI`
  - `CONFIG_CLOCK_STM32_PLL_SRC_HSI`
  - `CONFIG_CLOCK_STM32_PLL_SRC_HSE`
  - `CONFIG_CLOCK_STM32_PLL_SRC_PLL2`
  - `CONFIG_CLOCK_STM32_PLL_SRC_CSI`
  - `CONFIG_CLOCK_STM32_AHB_PRESCALER`
  - `CONFIG_CLOCK_STM32_APB1_PRESCALER`
  - `CONFIG_CLOCK_STM32_APB2_PRESCALER`
  - `CONFIG_CLOCK_STM32_CPU1_PRESCALER`
  - `CONFIG_CLOCK_STM32_CPU2_PRESCALER`
  - `CONFIG_CLOCK_STM32_AHB3_PRESCALER`
  - `CONFIG_CLOCK_STM32_AHB4_PRESCALER`
  - `CONFIG_CLOCK_STM32_PLL_PREDIV`
  - `CONFIG_CLOCK_STM32_PLL_PREDIV1`
  - `CONFIG_CLOCK_STM32_PLL_MULTIPLIER`
  - `CONFIG_CLOCK_STM32_PLL_XTPRE`
  - `CONFIG_CLOCK_STM32_PLL_M_DIVISOR`
  - `CONFIG_CLOCK_STM32_PLL_N_MULTIPLIER`
  - `CONFIG_CLOCK_STM32_PLL_P_DIVISOR`
  - `CONFIG_CLOCK_STM32_PLL_Q_DIVISOR`
  - `CONFIG_CLOCK_STM32_PLL_R_DIVISOR`
  - `CONFIG_CLOCK_STM32_LSE`
  - `CONFIG_CLOCK_STM32_HSI_DIVISOR`
  - `CONFIG_CLOCK_STM32_D1CPRE`
  - `CONFIG_CLOCK_STM32_HPRE`
  - `CONFIG_CLOCK_STM32_D2PPRE1`
  - `CONFIG_CLOCK_STM32_D2PPRE2`
  - `CONFIG_CLOCK_STM32_D1PPRE`
  - `CONFIG_CLOCK_STM32_D3PPRE`
  - `CONFIG_CLOCK_STM32_PLL3_ENABLE`
  - `CONFIG_CLOCK_STM32_PLL3_M_DIVISOR`
  - `CONFIG_CLOCK_STM32_PLL3_N_MULTIPLIER`
  - `CONFIG_CLOCK_STM32_PLL3_P_ENABLE`
  - `CONFIG_CLOCK_STM32_PLL3_P_DIVISOR`
  - `CONFIG_CLOCK_STM32_PLL3_Q_ENABLE`
  - `CONFIG_CLOCK_STM32_PLL3_Q_DIVISOR`
  - `CONFIG_CLOCK_STM32_PLL3_R_ENABLE`
  - `CONFIG_CLOCK_STM32_PLL3_R_DIVISOR`
  - `CONFIG_CLOCK_STM32_PLL_DIVISOR`
  - `CONFIG_CLOCK_STM32_MSI_PLL_MODE`

### Deprecated in this release

- Removed `<power/reboot.h>` and `<power/power.h>` deprecated headers.
  `<sys/reboot.h>` and `<pm/pm.h>` should be used instead.
- `USBD_CFG_DATA_DEFINE` is deprecated in favor of utilizing
  `USBD_DEFINE_CFG_DATA`
- `SYS_DEVICE_DEFINE` is deprecated in favor of utilizing
  `SYS_INIT`.
- `device_usable_check()` is deprecated in favor of utilizing
  [`device_is_ready()`](../kernel/drivers/index.md#c.device_is_ready "device_is_ready").
- Custom CAN return codes (`CAN_TX_OK`, `CAN_TX_ERR`,
  `CAN_TX_ARB_LOST`, `CAN_TX_BUS_OFF`,
  `CAN_TX_UNKNOWN`, `CAN_TX_EINVAL`,
  `CAN_NO_FREE_FILTER`, and `CAN_TIMEOUT`) are deprecated in
  favor of utilizing standard errno error codes.
- `can_configure()` is deprecated in favor of utilizing
  [`can_set_bitrate()`](../hardware/peripherals/can/controller.md#c.can_set_bitrate "can_set_bitrate") and [`can_set_mode()`](../hardware/peripherals/can/controller.md#c.can_set_mode "can_set_mode").
- `can_attach_workq()` is deprecated in favor of utilizing
  [`can_add_rx_filter_msgq()`](../hardware/peripherals/can/controller.md#c.can_add_rx_filter_msgq "can_add_rx_filter_msgq") and [`k_work_poll_submit()`](../kernel/services/threads/workqueue.md#c.k_work_poll_submit "k_work_poll_submit").
- `can_attach_isr()` is is deprecated and replaced by
  [`can_add_rx_filter()`](../hardware/peripherals/can/controller.md#c.can_add_rx_filter "can_add_rx_filter").
- `CAN_DEFINE_MSGQ` is deprecated and replaced by
  [`CAN_MSGQ_DEFINE`](../hardware/peripherals/can/controller.md#c.CAN_MSGQ_DEFINE "CAN_MSGQ_DEFINE").
- `can_attach_msgq()` is deprecated and replaced by
  [`can_add_rx_filter_msgq()`](../hardware/peripherals/can/controller.md#c.can_add_rx_filter_msgq "can_add_rx_filter_msgq").
- `can_detach()` is deprecated and replaced by
  [`can_remove_rx_filter()`](../hardware/peripherals/can/controller.md#c.can_remove_rx_filter "can_remove_rx_filter").
- `can_register_state_change_isr()` is deprecated and replaced by
  [`can_set_state_change_callback()`](../hardware/peripherals/can/controller.md#c.can_set_state_change_callback "can_set_state_change_callback").
- `can_write()` is deprecated in favor of utilizing [`can_send()`](../hardware/peripherals/can/controller.md#c.can_send "can_send").

### Stable API changes in this release

### New APIs in this release

- Serial

  - Added new APIs to support datum wider than 8-bit.

    - [`CONFIG_UART_WIDE_DATA`](../kconfig.md#CONFIG_UART_WIDE_DATA "CONFIG_UART_WIDE_DATA") is added to enable this new APIs.
    - Following functions, mirroring similar functions for 8-bit datum,
      are added:

      - [`uart_tx_u16()`](../hardware/peripherals/uart.md#c.uart_tx_u16 "uart_tx_u16") to send a given number of datum from buffer.
      - [`uart_rx_enable_u16()`](../hardware/peripherals/uart.md#c.uart_rx_enable_u16 "uart_rx_enable_u16") to start receiving data.
      - [`uart_rx_buf_rsp_u16()`](../hardware/peripherals/uart.md#c.uart_rx_buf_rsp_u16 "uart_rx_buf_rsp_u16") to set buffer for receiving data
        in response to `UART_RX_BUF_REQUEST` event.
      - [`uart_poll_in_u16()`](../hardware/peripherals/uart.md#c.uart_poll_in_u16 "uart_poll_in_u16") to poll for input.
      - [`uart_poll_out_u16()`](../hardware/peripherals/uart.md#c.uart_poll_out_u16 "uart_poll_out_u16") to output datum in polling mode.
      - [`uart_fifo_fill_u16()`](../hardware/peripherals/uart.md#c.uart_fifo_fill_u16 "uart_fifo_fill_u16") to fill FIFO with data.
      - [`uart_fifo_read_u16()`](../hardware/peripherals/uart.md#c.uart_fifo_read_u16 "uart_fifo_read_u16") to read data from FIFO.
- Devicetree

  - Added new Devicetree helpers:

    - [`DT_INST_ENUM_IDX`](../build/dts/api/api.md#c.DT_INST_ENUM_IDX "DT_INST_ENUM_IDX")
    - [`DT_INST_ENUM_IDX_OR`](../build/dts/api/api.md#c.DT_INST_ENUM_IDX_OR "DT_INST_ENUM_IDX_OR")
    - [`DT_INST_PARENT`](../build/dts/api/api.md#c.DT_INST_PARENT "DT_INST_PARENT")
  - New [ranges property](../build/dts/api/api.md#devicetree-ranges-property) APIs
  - Removed: `DT_CHOSEN_ZEPHYR_CANBUS_LABEL`; use
    `DEVICE_DT_GET(DT_CHOSEN(zephyr_canbus))` to get the device instead, and
    read the name from the device structure if needed.
  - Removed deprecated macros:

    - `DT_CLOCKS_LABEL_BY_IDX`
    - `DT_CLOCKS_LABEL`
    - `DT_INST_CLOCKS_LABEL_BY_IDX`
    - `DT_INST_CLOCKS_LABEL_BY_NAME`
    - `DT_INST_CLOCKS_LABEL`
    - `DT_PWMS_LABEL_BY_IDX`
    - `DT_PWMS_LABEL_BY_NAME`
    - `DT_PWMS_LABEL`
    - `DT_INST_PWMS_LABEL_BY_IDX`
    - `DT_INST_PWMS_LABEL_BY_NAME`
    - `DT_INST_PWMS_LABEL`
    - `DT_IO_CHANNELS_LABEL_BY_IDX`
    - `DT_IO_CHANNELS_LABEL_BY_NAME`
    - `DT_IO_CHANNELS_LABEL`
    - `DT_INST_IO_CHANNELS_LABEL_BY_IDX`
    - `DT_INST_IO_CHANNELS_LABEL_BY_NAME`
    - `DT_INST_IO_CHANNELS_LABEL`
    - `DT_DMAS_LABEL_BY_IDX`
    - `DT_INST_DMAS_LABEL_BY_IDX`
    - `DT_DMAS_LABEL_BY_NAME`
    - `DT_INST_DMAS_LABEL_BY_NAME`
    - `DT_ENUM_TOKEN`
    - `DT_ENUM_UPPER_TOKEN`
- CAN

  - Added [`can_get_max_filters()`](../hardware/peripherals/can/controller.md#c.can_get_max_filters "can_get_max_filters") for retrieving the maximum number of RX
    filters support by a CAN controller device.

## Kernel

> - Added support for event objects. Threads may wait on an event object such
>   that any events posted to that event object may wake a waiting thread if the
>   posting satisfies the waiting threads’ event conditions.
> - Extended CPU runtime stats to track current, total, peak and average usage
>   (as bounded by the scheduling of the idle thread). This permits a developer
>   to obtain more system information if desired to tune the system.
> - Added “thread\_usage” API for thread runtime cycle monitoring.
> - Fixed timeout issues when SYSTEM\_CLOCK\_SLOPPY\_IDLE is configured.

## Architectures

- ARM

  - AARCH32

    - Converted inline assembler calls to using CMSIS provided functions for
      `arm_core_mpu_enable()` and `arm_core_mpu_disable()`.
    - Replaced Kconfig CONFIG\_CPU\_CORTEX\_R with CONFIG\_ARMV7\_R to enable
      differentiation between v7 and v8 Cortex-R.
    - Updated the Cortex-R syscall behavior to match that of the Cortex-M.
  - AARCH64

    - Fixed out-of-bounds error when large number of IRQs are enabled and ignore
      special INTDs between 1020 and 1023
    - Added MPU code for ARMv8R
    - Various MMU fixes
    - Added nocache memory segment support
    - Added Xen hypercall interface for ARM64
    - Fixed race condition on SMP scheduling code.
- Xtensa

  - Introduced a mechanism to automatically figure out which scratch registers
    are used for internal code, instead of hard-coding. This is to accommodate
    the configurability of the architecture where some registers may exist in
    one SoC but not on another one.
  - Added coredump support for Xtensa.
  - Added GDB stub support for Xtensa.

## Bluetooth

- Updated all experimental features in Bluetooth to use the new `EXPERIMENTAL`
  selectable Kconfig option
- Bluetooth now uses logging v2 as with the rest of the tree
- Audio

  - Implemented the Content Control ID module (CCID)
  - Added support for the Coordinated Set Identification Service (CSIS)
  - Added a Temporary Object Transfer client implementation
  - Added a Media Control client implementation
  - Added a Media Control Server implementation
  - Implemented the Media Proxy API
  - Implemented CIG reconfiguration and state handling
  - Updated the CSIS API for both server and client
  - Added Basic Audio Profile (BAP) unicast and broadcast server support
- Direction Finding

  - Added support for filtering of Periodic Advertising Sync by CTE type
  - Added additional handling logic for Periodic Advertising Sync Establishemnt
  - Added CTE RX, sampling and IQ report handling in DF connected mode
  - Added support for CTE configuration in connected mode
  - Direction Finding connection mode now uses the newly refactored LLCP
    implementation
- Host

  - The [`CONFIG_BT_SETTINGS_CCC_STORE_ON_WRITE`](../kconfig.md#CONFIG_BT_SETTINGS_CCC_STORE_ON_WRITE "CONFIG_BT_SETTINGS_CCC_STORE_ON_WRITE") is now enabled
    by default. Storing CCC right after it’s written reduces risk of
    inconsistency of CCC values between bonded peers
  - Added support for L2CAP channel reconfiguration.
  - Added support for SMP error code 0xF, where the peer rejects a distributed
    key
  - Added `bt_gatt_service_is_registered()` to verify sevice registration
  - Added create an delete procedures to the Object Transfer Service
    implementation
  - Added support for reassembling extended advertising reports
  - Added support for reassembling periodic advertising reports
  - Added support for setting long periodic advertising data
  - Implemented GATT Long Writes reassembly before forwarding them up to the
    application
  - The GATT Server DB hash calculation logic has been corrected
  - Added storing of the CCC data upon paring complete
- Mesh

  - Split out the Proxy services, which can now be compiled out
  - Added an option to call back on every retransmission
  - Added support for multiple Advertising Sets
  - Refactored he Config Client and Health Client API to allow async use
- Controller

  - Added support for a brand new implementation of LL Control Procedures
    (LLCP), currently disabled by default, can be enabled using the
    `CONFIG_BT_LL_SW_LLCP_IMPL` Kconfig choice
  - Added initial support for Broadcast Isochronous Groups (BIG)
  - Integrated ISO Sync RX datapath
  - Transitioned FEM configurations (PA/LNA) from Kconfig to Devicetree
  - Updated the supported Bluetooth HCI version to 5.3
  - Added support for Periodic Advertiser List
  - Added support for Periodic Advertising Synchronization Receive Enable
  - Added support for filter access list filtering for extended scanning
  - Added support for Advertising Extensions dynamic TX power control
  - Added handling of direct address type in extended adv reports
  - Implemented auxiliary PDU device address matching
  - Implemented fragmentation of extended advertising reports over HCI
  - Implemented Extended Advertising and Scan report back-to-back chaining
  - Implemented Periodic Advertising ADI support,including duplicate filtering
  - Introduced a new preferred central connection spacing feature
- HCI Driver

  - Added support for a new optional `setup()` function for vendor-specific
    setup code required to bring up the controller
  - Fixed DTM mode not being reset correctly with the HCI Reset command
  - Limited the maximum ACL TX buffer size to 251 bytes

## Boards & SoC Support

- Added support for these SoC series:

  - GigaDevice GD32VF103, GD32F3X0, GD32F403 and GD32F450.
  - Raspberry Pi RP2040
  - NXP i.MXRT595, i.MX8MQ, i.MX8MP
- Removed support for these SoC series:
- Made these changes in other SoC series:

  - stm32h7: Added SMPS support
  - stm32u5: Enabled TF-M
- Changes for ARC boards:
- Added support for these ARM boards:

  - GigaDevice GD32F350R-EVAL
  - GigaDevice GD32F403Z-EVAL
  - GigaDevice GD32F450I-EVAL
  - OLIMEX-STM32-H405
  - NXP MIMXRT595-EVK
  - NXP MIMX8MQ-EVK
  - NXP MIMX8MP-EVK
  - Raspberry Pi Pico
  - ST Nucleo G031K8
  - ST Nucleo H7A3ZI Q
  - ST STM32G081B Evaluation
- Added support for these ARM64 boards:

  - Intel SoC FPGA Agilex development kit
- Removed support for these ARM boards:
- Removed support for these X86 boards:
- Added support for these RISC-V boards:

  - GigaDevice GD32VF103V-EVAL
  - Sipeed Longan Nano and Nano Lite
- Made these changes in other boards:

  - sam\_e70\_xplained: Added support for CAN-FD driver
  - mimxrt11xx: Added SOC level power management
  - mimxrt11xx: Added support for GPT timer as OS timer
- Added support for these following shields:

## Drivers and Sensors

- ADC

  - Added support for stm32u5 series
  - stm32: Added shared IRQ support
- CAN

  - Renamed `zephyr,can-primary` chosen property to `zephyr,canbus`.
  - Added [`CAN_STATE_ERROR_WARNING`](../hardware/peripherals/can/controller.md#c.can_state.CAN_STATE_ERROR_WARNING "CAN_STATE_ERROR_WARNING") CAN controller state.
  - Added Atmel SAM Bosch M\_CAN CAN-FD driver.
  - Added NXP LPCXpresso Bosch M\_CAN CAN-FD driver.
  - Added ST STM32H7 Bosch M\_CAN CAN-FD driver.
  - Rework transmission error handling the NXP FlexCAN driver to automatically
    retry transmission in case or arbitration lost or missing acknowledge and
    to fail early in [`can_send()`](../hardware/peripherals/can/controller.md#c.can_send "can_send") if in [`CAN_STATE_BUS_OFF`](../hardware/peripherals/can/controller.md#c.can_state.CAN_STATE_BUS_OFF "CAN_STATE_BUS_OFF").
  - Added support for disabling automatic retransmissions (“one-shot” mode”) to
    the ST STM32 bxCAN driver.
  - Converted the emulated CAN loopback driver to be configured through
    devicetree instead of Kconfig.
- Counter

  - stm32: Added timer based counter driver (stm32f4 only for now).
- DAC

  - Added support for GigaDevice GD32 SoCs
  - Added support for stm32u5 series
- Disk

  - stm32 sdmmc: Converted from polling to IT driven mode and added Hardware
    Flow Control option
- DMA

  - Added support for suspending and resuming transfers
  - Added support for SoCs with DMA between application and embedded
    processors, allows for transfer directions to be identified as such.
  - mimxrt11xx: Added support for DMA
- EEPROM

  - Added support for the EEPROM present in the TMP116 digital temperature
    sensor.
- Entropy

  - Added support for stm32u5 series
- Ethernet

  - Added support for Synopsys DesignWare MAC driver with implementation
    on stm32h7 series.
  - stm32 (hal based): Added promiscuous mode support
  - stm32 (hal based): Added PTP L2 timestamping support
  - mimxrt11xx: Added support for 10/100M ENET
- Flash

  - stm32g0: Added Dual Bank support
  - stm32\_qspi: General enhancement (Generation of the reset pulse for SPI-NOR memory,
    Usage of 4IO for read / write (4READ/4PP), Support for different QSPI banks,
    Support for 4B addressing on spi-nor)
  - ite\_i8xxx2: The driver has been reworked so the write/erase protection
    management has been moved to implementations of the flash\_write()
    and the flash\_erase() calls. The driver was keeping the write protection API
    which was designed to be removed since 2.6 release.
- GPIO

  - Added driver for GigaDevice GD32 SoCs
- I2C

  - Added driver for GigaDevice GD32 SoCs
  - Added stats functionality to all drivers
  - Added I2C driver for Renesas R-Car platform
  - Added support for TCA9548A I2C switch
- I2S

  - mimxrt10xx: Added support for I2S
  - mimxrt11xx: Added support for I2S
- Interrupt Controller

  - Added ECLIC driver for GigaDevice RISC-V GD32 SoCs
  - Added EXTI driver for GigaDevice GD32 SoCs
- MBOX

  - Added MBOX NRFX IPC driver
- MEMC

  - Added support for stm32f7 series
- Pin control

  - Introduced a new state-based pin control (`pinctrl`) API inspired by the
    Linux design principles. The `pinctrl` API will replace the existing
    pinmux API, so all platforms using pinmux are encouraged to migrate. A
    detailed guide with design principles and implementation guidelines can be
    found in [Pin Control](../hardware/pinctrl/index.md#pinctrl-guide).
  - Platforms already supporting the `pinctrl` API:

    - GigaDevice GD32
    - Nordic (preliminary support)
    - Renesas R-Car
    - STM32
- PWM

  - stm32: DT bindings: st,prescaler property was moved from pwm
    to parent timer node.
  - stm32: Implemented PWM capture API
  - Added driver for GigaDevice GD32 SoCs. Only PWM output is supported.
  - mimxrt1021: Added support for PWM
- Sensor

  - Added Invensense MPU9250 9-axis IMU driver.
  - Added ITE IT8XX2 tachometer driver.
  - Added STM L5 die temperature driver.
  - Added STM I3G4250D gyroscope driver.
  - Added TI TMP108 driver.
  - Added Winsen MH-Z19B CO2 driver.
  - Constified device config access in sbs\_gauge and LM75 drivers.
  - Dropped DEV\_DATA/DEV\_CFG usage from various drivers.
  - Moved ODR and range properties from Kconfig to devicetree in various STM
    drivers.
  - Refactored INA230 driver to add support for INA237 variant.
  - Refactored various drivers to use I2C/SPI/GPIO DT APIs.
  - Enabled level triggered interrupts in LIS2DH driver.
  - Fixed TMP112 driver to avoid I2C burst write portability issues.
  - Fixed SENSOR\_DEG2RAD\_DOUBLE macro in LSM6DS0 driver.
  - Fixed gain factor in LSM303DLHC magnetometer driver.
- Serial

  - stm32: Implemented half-duplex option.
  - Added driver for GigaDevice GD32 SoCs. Polling and interrupt driven modes
    are supported.
- SPI

  - stm32: Implemented Frame format option (TI vs Motorola).
  - mimxrt11xx: Added support for Flexspi
- Timer

  - stm32 lptim: Added support for stm32h7
- USB

  - Added support for stm32u5 series (OTG full speed)
- Watchdog

  - Added support for stm32u5 series (Independent and Window)
  - mimxrt1170: Added support for watchdog on CM7

## Networking

- CoAP:

  - Refactored `coap_client`/`coap_server` samples to make better use of
    observe APIs.
  - Added PATCH, iPATCH and FETCH methods.
  - A few fixes for the block transfer handling.
- DNS:

  - Make mdns and llmnr responders join their multicast groups.
  - Added support for mdns/dns\_sd service type enumeration.
- ICMPv6:

  - Added support for Route Information option processing.
- IPv4:

  - Add IPv4 support to multicast monitor.
- LwM2M:

  - Added a parameter to forcefully close the LwM2M session to
    [`lwm2m_rd_client_stop()`](../connectivity/networking/api/lwm2m.md#c.lwm2m_rd_client_stop "lwm2m_rd_client_stop") function.
  - Replaced custom `float32_value_t` type with double.
  - Added `LWM2M_FIRMWARE_PORT_NONSECURE`/
    `LWM2M_FIRMWARE_PORT_SECURE` options, which allow to
    specify a custom port or firmware update.
  - Added [`lwm2m_update_device_service_period()`](../connectivity/networking/api/lwm2m.md#c.lwm2m_update_device_service_period "lwm2m_update_device_service_period") API function.
  - Added observe callback for observe and notification events.
  - Added support for multiple LwM2M Firmware Update object instances.
  - Improved error handling in LwM2M content writers.
  - Added unit tests for LwM2M content writers.
  - Implemented LwM2M Security, Server, Connection Monitor objects in version 1.1.
  - Multiple minor bugfixes in the LwM2M stack.
  - Added support for the following objects:

    - LWM2M Software Management (ID 9)
    - LwM2M Gateway (ID 25)
    - IPSO Current (ID 3317)
    - uCIFI Battery (ID 3411)
    - IPSO Filling level (ID 3435)
- Misc:

  - gptp: clock sync ratio as double, not float
  - Added support for route lifetime and preference.
  - Refactored various packed structures across the networking stack, to avoid
    unaliged access warnings from gcc.
  - Added automatic loopback addresses registration to loopback interface.
  - Fixed source address selection for ARP.
  - Allow to implement a custom IEEE802154 L2 on top of existing drivers.
  - Introduced a network packet filtering framework.
- MQTT:

  - Fixed incomplete [`zsock_sendmsg()`](../connectivity/networking/api/sockets.md#c.zsock_sendmsg "zsock_sendmsg") writes handling.
  - Fixed [`zsock_setsockopt()`](../connectivity/networking/api/sockets.md#c.zsock_setsockopt "zsock_setsockopt") error handling in SOCKS5 transport.
- OpenThread:

  - Updated OpenThread revision up to commit `ce77ab3c1d7ad91b284615112ae38c08527bf73e`.
  - Fixed an overflow bug in the alarm implementation for Zephyr.
  - Added crypto backend based on PSA API.
  - Allow to store OpenThread settings in RAM.
- Socket:

  - Fixed [`zsock_sendmsg()`](../connectivity/networking/api/sockets.md#c.zsock_sendmsg "zsock_sendmsg") when payload size exceeded network MTU.
  - Added socket processing priority.
  - Fixed possible crash in [`zsock_getaddrinfo()`](../connectivity/networking/api/sockets.md#c.zsock_getaddrinfo "zsock_getaddrinfo") when DNS callback is
    delayed.
- Telnet:

  - Fixed handling of multiple commands in a single packet.
  - Enabled command handling by default.
- TCP:

  - Added support for sending our MSS to peer.
  - Fixed packet sending to local addresses.
  - Fixed possible deadlock between TCP and socket layer, when connection close
    is initiated from both sides.
  - Multiple other minor bugfixes and improvements in the TCP implementation.
- TLS:

  - Added support for `TLS_CERT_NOCOPY` socket option, which allows to
    optimise mbed TLS heap usage.
  - Fixed `POLLHUP` detection when underlying TCP connection is closed.
  - Fixed mbedtls session reset on handshake errors.

## USB

## Build and Infrastructure

- Build system

  - New CMake extension functions:

    - `dt_alias()`
    - `target_sources_if_dt_node()`
  - The following CMake extension functions now handle devicetree aliases:

    - `dt_node_exists()`
    - `dt_node_has_status()`
    - `dt_prop()`
    - `dt_num_regs()`
    - `dt_reg_addr()`
    - `dt_reg_size()`
- Devicetree

  - Support for the devicetree compatible `ti,ina23x` has been removed.
    Instead, use [`ti,ina230`](../build/dts/api/bindings/sensor/ti%2Cina230.md#std-dtcompatible-ti-ina230) or [`ti,ina237`](../build/dts/api/bindings/sensor/ti%2Cina237.md#std-dtcompatible-ti-ina237).
- West (extensions)

  - Added support for gd32isp runner

## Libraries / Subsystems

- Management

  - Fixed the mcumgr SMP protocol over serial not adding the length of the CRC16 to packet length.
  - Kconfig option OS\_MGMT\_TASKSTAT is now disabled by default.
- Power management

  - Power management resources are now manually allocated by devices using
    [`PM_DEVICE_DEFINE`](../services/pm/api/index.md#c.PM_DEVICE_DEFINE "PM_DEVICE_DEFINE"), [`PM_DEVICE_DT_DEFINE`](../services/pm/api/index.md#c.PM_DEVICE_DT_DEFINE "PM_DEVICE_DT_DEFINE") or
    [`PM_DEVICE_DT_INST_DEFINE`](../services/pm/api/index.md#c.PM_DEVICE_DT_INST_DEFINE "PM_DEVICE_DT_INST_DEFINE"). Device instantiation macros take now
    a reference to the allocated resources. The reference can be obtained using
    [`PM_DEVICE_GET`](../services/pm/api/index.md#c.PM_DEVICE_GET "PM_DEVICE_GET"), [`PM_DEVICE_DT_GET`](../services/pm/api/index.md#c.PM_DEVICE_DT_GET "PM_DEVICE_DT_GET") or
    [`PM_DEVICE_DT_INST_GET`](../services/pm/api/index.md#c.PM_DEVICE_DT_INST_GET "PM_DEVICE_DT_INST_GET"). Thanks to this change, devices not
    implementing support for device power management will not use unnecessary
    memory.
  - Device runtime power management API error handling has been simplified.
  - [`pm_device_runtime_enable()`](../services/pm/api/index.md#c.pm_device_runtime_enable "pm_device_runtime_enable") suspends the target device if not already
    suspended. This change makes sure device state is always kept in a
    consistent state.
  - Improved PM states Devicetree macros naming
  - Added a new API call [`pm_state_cpu_get_all()`](../services/pm/api/index.md#c.pm_state_cpu_get_all "pm_state_cpu_get_all") to obtain information
    about CPU power states.
  - `pm/device.h` is no longer included by `device.h`, since the device API
    no longer depends on the PM API.
  - Added support for power domains. Power domains are implemented as
    simple devices and use the existent PM API for resume and suspend, devices
    under a power domain are notified when it becomes active or suspended.
  - Added a new action [`PM_DEVICE_ACTION_TURN_ON`](../services/pm/api/index.md#c.pm_device_action.PM_DEVICE_ACTION_TURN_ON "PM_DEVICE_ACTION_TURN_ON"). This action
    is used by power domains to notify devices when it becomes active.
  - Added new API ([`pm_device_state_lock()`](../services/pm/api/index.md#c.pm_device_state_lock "pm_device_state_lock"),
    [`pm_device_state_unlock()`](../services/pm/api/index.md#c.pm_device_state_unlock "pm_device_state_unlock") and
    [`pm_device_state_is_locked()`](../services/pm/api/index.md#c.pm_device_state_is_locked "pm_device_state_is_locked")) to lock a device pm
    state. When the device has its state locked, the kernel will no
    longer suspend and resume devices when the system goes to sleep
    and device runtime power management operations will fail.
  - `pm_device_state_set()` is deprecated in favor of utilizing
    [`pm_device_action_run()`](../services/pm/api/index.md#c.pm_device_action_run "pm_device_action_run").
  - Proper multicore support. Devices are suspended only when the last
    active CPU. A cpu parameter was added to Policy and SoC interfaces.
- Tracing

  - Support all syscalls being traced using the python syscall generator to
    introduce a tracing hook call.
- IPC

  - Added IPC service support and RPMsg with static VRINGs backend

## HALs

- STM32

  - stm32cube/stm32wb and its lib: Upgraded to version V1.12.1
  - stm32cube/stm32mp1: Upgraded to version V1.5.0
  - stm32cube/stm32u5: Upgraded to version V1.0.2
- Added [GigaDevice HAL module](https://github.com/zephyrproject-rtos/hal_gigadevice)

## MCUboot

- Fixed serial recovery skipping on nrf5340.
- Fixed issue which caused that progressive’s erase feature was off although was
  selected by Kconfig (introduced by #42c985cead).
- Added check of reset address in incoming image validation phase, see
  `CONFIG_MCUBOOT_VERIFY_IMG_ADDRESS`.
- Allow image header bigger than 1 KB for encrypted images.
- Support Mbed TLS 3.0.
- stm32: watchdog support.
- many documentation improvements.
- Fixed deadlock on cryptolib selectors in Kconfig.
- Fixed support for single application slot with serial recovery.
- Added various hooks to be able to change how image data is accessed, see
  `CONFIG_BOOT_IMAGE_ACCESS_HOOKS`.
- Added custom commands support in serial recovery (PERUSER\_MGMT\_GROUP): storage
  erase `CONFIG_BOOT_MGMT_CUSTOM_STORAGE_ERASE`, custom image status
  `CONFIG_BOOT_MGMT_CUSTOM_IMG_LIST`.
- Added support for direct image upload, see
  `CONFIG_MCUBOOT_SERIAL_DIRECT_IMAGE_UPLOAD` in serial recovery.

## Trusted Firmware-m

- Updated TF-M to 1.5.0 release, with a handful of additional cherry-picked
  commits.

## Documentation

- A new theme is used by the Doxygen HTML pages. It is based on
  [doxygen-awesome-css](https://github.com/jothepro/doxygen-awesome-css)
  theme.

## Tests and Samples

- Drivers: clock\_control: Added test suite for stm32 (u5, h7).

## Issue Related Items

These GitHub issues were addressed since the previous 2.7.0 tagged
release:

- [GitHub #42973](https://github.com/zephyrproject-rtos/zephyr/issues/42973) - Zephyr-sdkConfig.cmake file not found
- [GitHub #42961](https://github.com/zephyrproject-rtos/zephyr/issues/42961) - Bluetooth: periodic\_sync sample never executes .recv callback
- [GitHub #42942](https://github.com/zephyrproject-rtos/zephyr/issues/42942) - sizeof(struct sockaddr\_storage) is smaller than sizeof(struct sockaddr\_in6)
- [GitHub #42862](https://github.com/zephyrproject-rtos/zephyr/issues/42862) - Bluetooth: L2CAP: Security check on l2cap request is wrong
- [GitHub #42816](https://github.com/zephyrproject-rtos/zephyr/issues/42816) - samples: Bluetooth: df: DF samples build fail
- [GitHub #42794](https://github.com/zephyrproject-rtos/zephyr/issues/42794) - samples: Bluetooth: df: Wrong periodic sync termination handling in direction\_finding\_connectionless\_rx sample
- [GitHub #42793](https://github.com/zephyrproject-rtos/zephyr/issues/42793) - net\_socket: mimxrt1170\_evk\_cm7: build failure
- [GitHub #42778](https://github.com/zephyrproject-rtos/zephyr/issues/42778) - bluetooth: autopts: can’t start on the board
- [GitHub #42759](https://github.com/zephyrproject-rtos/zephyr/issues/42759) - armv8 qemu\_cortex\_a53 bug(gdb) on official sample
- [GitHub #42756](https://github.com/zephyrproject-rtos/zephyr/issues/42756) - mec15xxevb\_assy6853: ringbuffer testsuite failing once due to a timeout randomly when run multiple times.
- [GitHub #42746](https://github.com/zephyrproject-rtos/zephyr/issues/42746) - echo\_server and echo\_client sample code builds fail for native\_posix\_64
- [GitHub #42735](https://github.com/zephyrproject-rtos/zephyr/issues/42735) - Bluetooth: Host: df: Uninitialized variable used to assign length of antenna identifiers
- [GitHub #42693](https://github.com/zephyrproject-rtos/zephyr/issues/42693) - Bluetooth: DF connectionless TX sample fails to build if CONFIG\_BT\_CTLR\_DF\_SCAN\_CTE\_RX is disabled
- [GitHub #42690](https://github.com/zephyrproject-rtos/zephyr/issues/42690) - sample.bootloader.mcuboot.serial\_recovery fails to compile
- [GitHub #42687](https://github.com/zephyrproject-rtos/zephyr/issues/42687) - [v 1.13 ] HID is not connecting to intel 7265 Bluetooth Module
- [GitHub #42665](https://github.com/zephyrproject-rtos/zephyr/issues/42665) - tests: kernel.common.context: test failure on imxrt series platform
- [GitHub #42648](https://github.com/zephyrproject-rtos/zephyr/issues/42648) - Setting long advertising data does not work
- [GitHub #42627](https://github.com/zephyrproject-rtos/zephyr/issues/42627) - Hardfault regression on 90 tests on CM0+ STM32 boards introduced by #39963 Cortex-R mpu fix on 90 tests
- [GitHub #42615](https://github.com/zephyrproject-rtos/zephyr/issues/42615) - [v2.7.2] Bluetooth: Controller: Missing ticks slot offset calculation in Periodic Advertising event scheduling
- [GitHub #42608](https://github.com/zephyrproject-rtos/zephyr/issues/42608) - bsim\_test\_mesh: pb\_adv\_reprovision.sh fails after commit to prevent multiple arguments in logging
- [GitHub #42604](https://github.com/zephyrproject-rtos/zephyr/issues/42604) - doc: broken CONFIG\_GPIO link in [https://docs.zephyrproject.org/latest/reference/peripherals/gpio.html](https://docs.zephyrproject.org/latest/reference/peripherals/gpio.html)
- [GitHub #42602](https://github.com/zephyrproject-rtos/zephyr/issues/42602) - I2C scan writes 0 bytes
- [GitHub #42588](https://github.com/zephyrproject-rtos/zephyr/issues/42588) - lsm6dso
- [GitHub #42586](https://github.com/zephyrproject-rtos/zephyr/issues/42586) - Net buffer macros rely on GCC extension
- [GitHub #42585’ - 3.0.0-rc1: warning: LOG\_STRDUP\_MAX\_STRING was assigned the value ‘100](https://github.com/zephyrproject-rtos/zephyr/issues/42585' - 3.0.0-rc1: warning: LOG_STRDUP_MAX_STRING was assigned the value '100) but got the value ‘’
- [GitHub #42581](https://github.com/zephyrproject-rtos/zephyr/issues/42581) - include: drivers: clock\_control: stm32 incorrect DT\_PROP is used for ‘xtpre’
- [GitHub #42573](https://github.com/zephyrproject-rtos/zephyr/issues/42573) - docs: sphinx-build issue, zephyr conf.py issue or something else?
- [GitHub #42556](https://github.com/zephyrproject-rtos/zephyr/issues/42556) - frdm\_k64f: samples/subsys/modbus are failing with a timeout.
- [GitHub #42555](https://github.com/zephyrproject-rtos/zephyr/issues/42555) - mimxrt1050\_evk: samples/subsys/task\_wdt is failing with control thread getting stuck
- [GitHub #42502](https://github.com/zephyrproject-rtos/zephyr/issues/42502) - Unable to add a specific syscon driver out-of-tree
- [GitHub #42499](https://github.com/zephyrproject-rtos/zephyr/issues/42499) - mec15xxevb\_assy6853: boards.mec15xxevb\_assy6853.i2c.i2c\_pca95xx test failed.
- [GitHub #42477](https://github.com/zephyrproject-rtos/zephyr/issues/42477) - Linker scripts not working properly on xtensa
- [GitHub #42462](https://github.com/zephyrproject-rtos/zephyr/issues/42462) - logging: syst/v2: hang or crash if log contains string arguments
- [GitHub #42435](https://github.com/zephyrproject-rtos/zephyr/issues/42435) - NXP RT1170/1160 base address error for SAI4 in devicetree
- [GitHub #42417](https://github.com/zephyrproject-rtos/zephyr/issues/42417) - tests drivers flash on stm32 qspi controller
- [GitHub #42414](https://github.com/zephyrproject-rtos/zephyr/issues/42414) - twister: testcases skipped by ztest\_test\_skip() have reason “Unknown” in report
- [GitHub #42411](https://github.com/zephyrproject-rtos/zephyr/issues/42411) - CLion CMake error while opening nRF-Connect-SDK project
- [GitHub #42403](https://github.com/zephyrproject-rtos/zephyr/issues/42403) - ‘crc16\_ansi()’ isn’t CRC-16-ANSI
- [GitHub #42397](https://github.com/zephyrproject-rtos/zephyr/issues/42397) - Direction finding nrf5340: uninitialized memory is passed to the callback
- [GitHub #42396](https://github.com/zephyrproject-rtos/zephyr/issues/42396) - ztest: weak test\_main() is promoted over given testsuite’s test\_main() if the testsuite uses own library
- [GitHub #42392](https://github.com/zephyrproject-rtos/zephyr/issues/42392) - Openocd Thread awareness broken on 3.0
- [GitHub #42385](https://github.com/zephyrproject-rtos/zephyr/issues/42385) - STM32: Entropy : health test config & magic never used
- [GitHub #42380](https://github.com/zephyrproject-rtos/zephyr/issues/42380) - USDHC driver encounters usage fault during frequency setting
- [GitHub #42373](https://github.com/zephyrproject-rtos/zephyr/issues/42373) - add k\_spin\_lock() to doxygen prior to v3.0 release
- [GitHub #42367](https://github.com/zephyrproject-rtos/zephyr/issues/42367) - stm32wb: BLE connections not working
- [GitHub #42361](https://github.com/zephyrproject-rtos/zephyr/issues/42361) - OpenOCD flashing not working on cc1352r1\_launchxl/cc26x2r1\_launchxl
- [GitHub #42358](https://github.com/zephyrproject-rtos/zephyr/issues/42358) - net: lwm2m: client context accessed after being invalidated in lwm2m\_rd\_client\_stop()
- [GitHub #42353](https://github.com/zephyrproject-rtos/zephyr/issues/42353) - LwM2M not pass official LightweightM2M-1.1-int-256 and stack enter dead lock
- [GitHub #42323](https://github.com/zephyrproject-rtos/zephyr/issues/42323) - lwm2m\_engine: Error when enabling debug log because of uninitialized variable ‘from\_addr’
- [GitHub #42308](https://github.com/zephyrproject-rtos/zephyr/issues/42308) - pm: Force shutdown has no effect
- [GitHub #42299](https://github.com/zephyrproject-rtos/zephyr/issues/42299) - spi: nRF HAL driver asserts when PM is used
- [GitHub #42292](https://github.com/zephyrproject-rtos/zephyr/issues/42292) - Compilation failed: Driver MPU6050
- [GitHub #42279](https://github.com/zephyrproject-rtos/zephyr/issues/42279) - The pthreads are not working on user space. ARM64 cortex\_a53 but generic requirement.
- [GitHub #42278](https://github.com/zephyrproject-rtos/zephyr/issues/42278) - USB CDC-ACM non-functional after host reboot
- [GitHub #42272](https://github.com/zephyrproject-rtos/zephyr/issues/42272) - doc: “Building on Linux without the Zephyr SDK” does not describe how to actually do it
- [GitHub #42269](https://github.com/zephyrproject-rtos/zephyr/issues/42269) - impossible to run west flash. NoneType error
- [GitHub #42228](https://github.com/zephyrproject-rtos/zephyr/issues/42228) - hal\_stm32: Wrong symbol definition
- [GitHub #42227](https://github.com/zephyrproject-rtos/zephyr/issues/42227) - Teensy41 support SDHC - Storage init Error
- [GitHub #42218](https://github.com/zephyrproject-rtos/zephyr/issues/42218) - stm32wl: Issue when disabling gpio interrupt
- [GitHub #42214](https://github.com/zephyrproject-rtos/zephyr/issues/42214) - drivers: uart\_nrfx\_uarte: Cannot start another reception after reception is complete
- [GitHub #42208](https://github.com/zephyrproject-rtos/zephyr/issues/42208) - tests/subsys/logging/log\_api/ fails qemu\_leon3 if ptr\_in\_rodata() is enabled for SPARC
- [GitHub #42205](https://github.com/zephyrproject-rtos/zephyr/issues/42205) - drivers: i2s\_sam\_ssc: data received via I2S bus are partially corrupted
- [GitHub #42199](https://github.com/zephyrproject-rtos/zephyr/issues/42199) - drivers: qdec\_sam: position measurement unstable if adc\_sam\_afec driver is enabled
- [GitHub #42187](https://github.com/zephyrproject-rtos/zephyr/issues/42187) - Settings tests are not correctly run
- [GitHub #42184](https://github.com/zephyrproject-rtos/zephyr/issues/42184) - Incremental build with config changes can produce an invalid binary when userspace is enabled
- [GitHub #42179](https://github.com/zephyrproject-rtos/zephyr/issues/42179) - driver: i2s: i2s\_mcux\_sai build failure on mixmrt1170\_evk\_cm7
- [GitHub #42177](https://github.com/zephyrproject-rtos/zephyr/issues/42177) - PM\_STATE\_INFO\_DT\_ITEMS\_LIST macro does not fill the pm\_min\_residency array
- [GitHub #42176](https://github.com/zephyrproject-rtos/zephyr/issues/42176) - mec15xxevb\_assy6853: can not be flashed due to “chip not identified”
- [GitHub #42171](https://github.com/zephyrproject-rtos/zephyr/issues/42171) - v3.0.0-rc1: mimxrt685\_evk\_cm33: undefined reference to ‘SystemCoreClock’ for latency\_measure benchmark
- [GitHub #42170](https://github.com/zephyrproject-rtos/zephyr/issues/42170) - v3.0.0-rc1: mimxrt685\_evk\_cm33: dma driver build failure
- [GitHub #42168](https://github.com/zephyrproject-rtos/zephyr/issues/42168) - v3.0.0-rc1: mimxrt685\_evk\_cm33: i2s driver build failure
- [GitHub #42164](https://github.com/zephyrproject-rtos/zephyr/issues/42164) - tests/bluetooth/tester broken after switch to logging v2
- [GitHub #42163](https://github.com/zephyrproject-rtos/zephyr/issues/42163) - BIT\_MASK(32) generate warning on 32 bits processor
- [GitHub #42161](https://github.com/zephyrproject-rtos/zephyr/issues/42161) - samples/compression/l4z: Expected RAM size for correct execution is too low
- [GitHub #42159](https://github.com/zephyrproject-rtos/zephyr/issues/42159) - samples: lora: Miss twister harness
- [GitHub #42157](https://github.com/zephyrproject-rtos/zephyr/issues/42157) - tests/lib/ringbuffer/libraries.ring\_buffer: Miss a timeout
- [GitHub #42151](https://github.com/zephyrproject-rtos/zephyr/issues/42151) - eth\_sam\_gmac: unable to change MAC address
- [GitHub #42149](https://github.com/zephyrproject-rtos/zephyr/issues/42149) - DT\_SPI\_DEV\_CS\_GPIOS\_DT\_SPEC\_GET is a layering violation that shouldn’t exist
- [GitHub #42147](https://github.com/zephyrproject-rtos/zephyr/issues/42147) - hts221 driver fails to build
- [GitHub #42125](https://github.com/zephyrproject-rtos/zephyr/issues/42125) - Bluetooth: controller: llcp: lll\_scan\_aux does not compile with new LLCP
- [GitHub #42120](https://github.com/zephyrproject-rtos/zephyr/issues/42120) - HTS221 missed header hts221\_reg.h
- [GitHub #42118](https://github.com/zephyrproject-rtos/zephyr/issues/42118) - mimxrt685\_evk\_cm33: Build failed on tests/drivers/spi/spi\_loopback/drivers.spi.loopback
- [GitHub #42117](https://github.com/zephyrproject-rtos/zephyr/issues/42117) - efr32mg\_sltb004a: Build issue on ‘tests/drivers/spi/spi\_loopback/drivers.spi.loopback’
- [GitHub #42112](https://github.com/zephyrproject-rtos/zephyr/issues/42112) - OTS: L2CAP: Unable to find channel of LE Credits packet
- [GitHub #42106](https://github.com/zephyrproject-rtos/zephyr/issues/42106) - AARCH64 stack initialisation fails with newlib for qemu\_cortex\_a53
- [GitHub #42098](https://github.com/zephyrproject-rtos/zephyr/issues/42098) - intel\_adsp\_cavs25: west sign command output some unrecognized ASCII char.
- [GitHub #42092](https://github.com/zephyrproject-rtos/zephyr/issues/42092) - stm32l0: Voltage regulator is not restored after leaving STOP mode
- [GitHub #42070](https://github.com/zephyrproject-rtos/zephyr/issues/42070) - west: spdx: Missing field for certain build results
- [GitHub #42065](https://github.com/zephyrproject-rtos/zephyr/issues/42065) - Bluetooth Controller: scan aux setup not checking extended header length of received packet
- [GitHub #42061](https://github.com/zephyrproject-rtos/zephyr/issues/42061) - obj\_tracking hangs system on intel\_adsp\_cavs25
- [GitHub #42031](https://github.com/zephyrproject-rtos/zephyr/issues/42031) - Ringbuffer used in CDC\_ACM seems to corrupt data if completely filled during transfer
- [GitHub #42024](https://github.com/zephyrproject-rtos/zephyr/issues/42024) - unrecognized argument in option ‘-mabi=lp64’
- [GitHub #42010](https://github.com/zephyrproject-rtos/zephyr/issues/42010) - intel\_adsp\_cavs18: Test cases failed on SMP related test cases (when CONFIG\_MP\_NUM\_CPUS > 1)
- [GitHub #41996](https://github.com/zephyrproject-rtos/zephyr/issues/41996) - LWM2M writing too long strings trigger post\_write\_cb with previously written value
- [GitHub #41993](https://github.com/zephyrproject-rtos/zephyr/issues/41993) - Intel\_adsp\_cavs18: test cases can not get complete log
- [GitHub #41992](https://github.com/zephyrproject-rtos/zephyr/issues/41992) - Intel\_adsp\_cavs18: tests/kernel/smp\_boot\_delay: failed to run case
- [GitHub #41991](https://github.com/zephyrproject-rtos/zephyr/issues/41991) - Intel\_adsp\_cavs18: some test cases can not get any log
- [GitHub #41989](https://github.com/zephyrproject-rtos/zephyr/issues/41989) - tests: kernel: tickless: ADSP stalls after firmware downloaded on Up Xtreme
- [GitHub #41982](https://github.com/zephyrproject-rtos/zephyr/issues/41982) - twister: Test not aborted after board was timed out
- [GitHub #41976](https://github.com/zephyrproject-rtos/zephyr/issues/41976) - Extra closing bracket in function lsm6dso\_handle\_interrupt
- [GitHub #41963](https://github.com/zephyrproject-rtos/zephyr/issues/41963) - Kernel usage fault when using semaphore with multi-threading
- [GitHub #41953](https://github.com/zephyrproject-rtos/zephyr/issues/41953) - drivers: counter: mcux\_ctimer: config used as non-const
- [GitHub #41952](https://github.com/zephyrproject-rtos/zephyr/issues/41952) - Log timestamp overflows when using LOGv2
- [GitHub #41951](https://github.com/zephyrproject-rtos/zephyr/issues/41951) - drivers: regulator: pmic: config used as non-const
- [GitHub #41945](https://github.com/zephyrproject-rtos/zephyr/issues/41945) - nxp\_hal module: Seconds GPIO interrupt does never fire
- [GitHub #41943](https://github.com/zephyrproject-rtos/zephyr/issues/41943) - Intel\_adsp\_cavs15: all the test cases run failed when running them by twister
- [GitHub #41942](https://github.com/zephyrproject-rtos/zephyr/issues/41942) - k\_delayable\_work being used as k\_work in work’s handler
- [GitHub #41938](https://github.com/zephyrproject-rtos/zephyr/issues/41938) - esp\_wrover\_kit: hello\_world build failure
- [GitHub #41933](https://github.com/zephyrproject-rtos/zephyr/issues/41933) - updatehub metadata size 0
- [GitHub #41915](https://github.com/zephyrproject-rtos/zephyr/issues/41915) - regression: Build fails after switching logging to V2
- [GitHub #41911](https://github.com/zephyrproject-rtos/zephyr/issues/41911) - pm\_power\_state\_force returns false after first call
- [GitHub #41894](https://github.com/zephyrproject-rtos/zephyr/issues/41894) - ISOAL sink handle value checked incorrectly
- [GitHub #41887](https://github.com/zephyrproject-rtos/zephyr/issues/41887) - Documentation setup page missing packages for arch linux
- [GitHub #41879](https://github.com/zephyrproject-rtos/zephyr/issues/41879) - new ztest api fails when user space is enabled
- [GitHub #41877](https://github.com/zephyrproject-rtos/zephyr/issues/41877) - tests: kernel: fatal: ADSP stalls after firmware downloaded on Up Xtreme
- [GitHub #41873](https://github.com/zephyrproject-rtos/zephyr/issues/41873) - STM32H735 Power Supply Config incorrect
- [GitHub #41862](https://github.com/zephyrproject-rtos/zephyr/issues/41862) - tests: kernel: fail to download firmware to ADSP on Up Xtreme
- [GitHub #41861](https://github.com/zephyrproject-rtos/zephyr/issues/41861) - tests: kernel: There are no log output after flashing image to intel\_adsp\_cavs25
- [GitHub #41860](https://github.com/zephyrproject-rtos/zephyr/issues/41860) - tests: kernel: queue: test case kernel.queue failed on ADSP of Up Xtreme
- [GitHub #41839](https://github.com/zephyrproject-rtos/zephyr/issues/41839) - BLE causes system sleep before main
- [GitHub #41835](https://github.com/zephyrproject-rtos/zephyr/issues/41835) - UP squared and acrn\_ehl\_crb: test cases which have config SMP config failed
- [GitHub #41826](https://github.com/zephyrproject-rtos/zephyr/issues/41826) - MQTT connection failed
- [GitHub #41821](https://github.com/zephyrproject-rtos/zephyr/issues/41821) - ESP32 mcuboot bootloader failed
- [GitHub #41818](https://github.com/zephyrproject-rtos/zephyr/issues/41818) - In uart.h uart\_irq\_rx\_ready() function not working properly for STM32F429 controller
- [GitHub #41816](https://github.com/zephyrproject-rtos/zephyr/issues/41816) - nrf\_802154 radio driver takes random numbers directly from entropy source
- [GitHub #41806](https://github.com/zephyrproject-rtos/zephyr/issues/41806) - tests: driver: clock: nrf: Several failures on nrf52dk\_nrf52832
- [GitHub #41794](https://github.com/zephyrproject-rtos/zephyr/issues/41794) - Bluetooth: ATT calls GATT callbacks with NULL conn pointer during disconnect
- [GitHub #41792](https://github.com/zephyrproject-rtos/zephyr/issues/41792) - CPU load halfed after PR #40784
- [GitHub #41745](https://github.com/zephyrproject-rtos/zephyr/issues/41745) - Power Management blinky example does not work on STM32H735G-DK
- [GitHub #41736](https://github.com/zephyrproject-rtos/zephyr/issues/41736) - Xtensa xt-xc++ Failed to build C++ code
- [GitHub #41734](https://github.com/zephyrproject-rtos/zephyr/issues/41734) - Can’t enable pull-up resistors in ESP32 gpio 25,26,27
- [GitHub #41722](https://github.com/zephyrproject-rtos/zephyr/issues/41722) - mcuboot image not confirmed on nrf5340dk
- [GitHub #41707](https://github.com/zephyrproject-rtos/zephyr/issues/41707) - esp32 newlib
- [GitHub #41698](https://github.com/zephyrproject-rtos/zephyr/issues/41698) - What does one have to do to activate BT\_DBG?
- [GitHub #41694](https://github.com/zephyrproject-rtos/zephyr/issues/41694) - undefined reference to ‘\_open’
- [GitHub #41691](https://github.com/zephyrproject-rtos/zephyr/issues/41691) - Tickless Kernel on STM32H7 fails with Exception
- [GitHub #41686](https://github.com/zephyrproject-rtos/zephyr/issues/41686) - SPI CS signal not used in SSD1306 driver
- [GitHub #41683](https://github.com/zephyrproject-rtos/zephyr/issues/41683) - http\_client: Unreliable rsp->body\_start pointer
- [GitHub #41682](https://github.com/zephyrproject-rtos/zephyr/issues/41682) - ESP32 mcuboot
- [GitHub #41653](https://github.com/zephyrproject-rtos/zephyr/issues/41653) - Bluetooth: Controller: Extended Advertising Scan: Implement Scan Data length maximum
- [GitHub #41637](https://github.com/zephyrproject-rtos/zephyr/issues/41637) - Modbus Gateway: Transaction ID Error!
- [GitHub #41635](https://github.com/zephyrproject-rtos/zephyr/issues/41635) - Samples: iso\_broadcast can not work properly unless some extra configuration flags
- [GitHub #41627](https://github.com/zephyrproject-rtos/zephyr/issues/41627) - PPP\_L2 does not properly terminate the modem state machine when going down.
- [GitHub #41624](https://github.com/zephyrproject-rtos/zephyr/issues/41624) - ESP32 Uart uart\_esp32\_irq\_tx\_ready
- [GitHub #41623](https://github.com/zephyrproject-rtos/zephyr/issues/41623) - esp32: fail to build sample/hello\_world with west
- [GitHub #41608](https://github.com/zephyrproject-rtos/zephyr/issues/41608) - LwM2M: Cannot set pmin/pmax on observable object
- [GitHub #41582](https://github.com/zephyrproject-rtos/zephyr/issues/41582) - stm32h7: CSI as PLL source is broken
- [GitHub #41581](https://github.com/zephyrproject-rtos/zephyr/issues/41581) - STM32 subghzspi fails pinctrl setup
- [GitHub #41557](https://github.com/zephyrproject-rtos/zephyr/issues/41557) - ESP32 Uart 2-bit Stop Register Setting
- [GitHub #41526](https://github.com/zephyrproject-rtos/zephyr/issues/41526) - ESP32 UART driver tx\_complete fires before last byte sent
- [GitHub #41525](https://github.com/zephyrproject-rtos/zephyr/issues/41525) - tests: drivers: : ethernet: fails to link for sam\_v71\_xult and sam\_v71b\_xult
- [GitHub #41524](https://github.com/zephyrproject-rtos/zephyr/issues/41524) - drivers: dma: dma\_mcux\_edma: unused variables cause daily build failures
- [GitHub #41523](https://github.com/zephyrproject-rtos/zephyr/issues/41523) - drivers: i2c: i2c\_mcux: unused variables cause daily build failures
- [GitHub #41509](https://github.com/zephyrproject-rtos/zephyr/issues/41509) - OpenThread’s timer processing enters infinite loop in 49th day of system uptime
- [GitHub #41503](https://github.com/zephyrproject-rtos/zephyr/issues/41503) - including <net/socket.h> fails with redefinition of ‘struct zsock\_timeval’ (sometimes :-) )
- [GitHub #41499](https://github.com/zephyrproject-rtos/zephyr/issues/41499) - drivers: iwdg: stm32: ‘WDT\_OPT\_PAUSE\_HALTED\_BY\_DBG’ might not work
- [GitHub #41488](https://github.com/zephyrproject-rtos/zephyr/issues/41488) - Stall logging on nrf52840
- [GitHub #41486](https://github.com/zephyrproject-rtos/zephyr/issues/41486) - Zephyr project installation
- [GitHub #41482](https://github.com/zephyrproject-rtos/zephyr/issues/41482) - kernel: Dummy thread should not have an uninitialized resource pool
- [GitHub #41471](https://github.com/zephyrproject-rtos/zephyr/issues/41471) - qemu\_cortex\_r5: failed to enable debug
- [GitHub #41465](https://github.com/zephyrproject-rtos/zephyr/issues/41465) - Periodic advertising sync failure, when “DONT\_SYNC\_AOA” or “DONT\_SYNC\_AOD” options is used
- [GitHub #41442](https://github.com/zephyrproject-rtos/zephyr/issues/41442) - power\_init for STM32L4 and STM32G0 in POST\_KERNEL
- [GitHub #41440](https://github.com/zephyrproject-rtos/zephyr/issues/41440) - twister: skip marked as pass
- [GitHub #41426](https://github.com/zephyrproject-rtos/zephyr/issues/41426) - ARMCLANG build fail
- [GitHub #41422](https://github.com/zephyrproject-rtos/zephyr/issues/41422) - The option CONFIG\_SYSTEM\_CLOCK\_SLOPPY\_IDLE blocks k\_sleep when CONFIG\_PM is enabled
- [GitHub #41418](https://github.com/zephyrproject-rtos/zephyr/issues/41418) - tests/lib/devicetree/devices fails to build for thingy52\_nrf52832
- [GitHub #41413](https://github.com/zephyrproject-rtos/zephyr/issues/41413) - NRF52832 - PWM not working after zephyr update
- [GitHub #41404](https://github.com/zephyrproject-rtos/zephyr/issues/41404) - if zsock\_connect() fails, tls\_context does not get released automatically
- [GitHub #41399](https://github.com/zephyrproject-rtos/zephyr/issues/41399) - samples: userspace: syscall\_perf test cannot be run
- [GitHub #41395](https://github.com/zephyrproject-rtos/zephyr/issues/41395) - littlefs(external spi flash) + mcuboot can’t get right mount area
- [GitHub #41392](https://github.com/zephyrproject-rtos/zephyr/issues/41392) - arm ：arm-none-eabi Unable to complete compilation, an error occurred during linking
- [GitHub #41385](https://github.com/zephyrproject-rtos/zephyr/issues/41385) - SHT3xD example does not work on ESP32
- [GitHub #41359](https://github.com/zephyrproject-rtos/zephyr/issues/41359) - Bluetooth: connection times out when trying to connect from certain centrals
- [GitHub #41352](https://github.com/zephyrproject-rtos/zephyr/issues/41352) - uart\_esp32\_poll\_in returns incorrect value
- [GitHub #41347](https://github.com/zephyrproject-rtos/zephyr/issues/41347) - tests: kernel: RT1170 fails test\_kernel\_cpu\_idle
- [GitHub #41339](https://github.com/zephyrproject-rtos/zephyr/issues/41339) - stm32, Unable to read UART while checking from Framing error.
- [GitHub #41331](https://github.com/zephyrproject-rtos/zephyr/issues/41331) - tests: drivers: disk: fail to handle no SD card situation
- [GitHub #41317](https://github.com/zephyrproject-rtos/zephyr/issues/41317) - ADSP: Many kernel test cases which have CONFIG\_MP\_NUM\_CPUS=1 failed in daily testing
- [GitHub #41299](https://github.com/zephyrproject-rtos/zephyr/issues/41299) - IS25LP016D SPI NOR FLASH PROBLEM
- [GitHub #41291](https://github.com/zephyrproject-rtos/zephyr/issues/41291) - LVGL touch event “LV\_EVENT\_LONG\_PRESSED” can not be generated if I press the screen without lift up my finger
- [GitHub #41289](https://github.com/zephyrproject-rtos/zephyr/issues/41289) - shell: infinite error loop upon LOG\_ERR in ISR context
- [GitHub #41284](https://github.com/zephyrproject-rtos/zephyr/issues/41284) - pthread\_cond\_wait return value incorrect
- [GitHub #41272](https://github.com/zephyrproject-rtos/zephyr/issues/41272) - ci: twister: mcuboot: MCUboot tests are no longer executed in the CI
- [GitHub #41268](https://github.com/zephyrproject-rtos/zephyr/issues/41268) - ‘bt\_gatt\_cancel’ type mismatch
- [GitHub #41256](https://github.com/zephyrproject-rtos/zephyr/issues/41256) - Zero Latency Interrupts conflicts
- [GitHub #41255](https://github.com/zephyrproject-rtos/zephyr/issues/41255) - drivers/can/can\_mcan.c: address-of-packed-member warnings
- [GitHub #41251](https://github.com/zephyrproject-rtos/zephyr/issues/41251) - RT1170 EVK Can does not send data
- [GitHub #41244](https://github.com/zephyrproject-rtos/zephyr/issues/41244) - subsys: pm: Low power mode transition broken
- [GitHub #41240](https://github.com/zephyrproject-rtos/zephyr/issues/41240) - logging can get messed up when messages are dropped
- [GitHub #41237](https://github.com/zephyrproject-rtos/zephyr/issues/41237) - [v2.7] drivers: ieee802154\_dw1000: use dedicated workqueue
- [GitHub #41222](https://github.com/zephyrproject-rtos/zephyr/issues/41222) - tests: remove not existing platforms from platform allow or integration\_platform
- [GitHub #41153](https://github.com/zephyrproject-rtos/zephyr/issues/41153) - rt i2s build fail
- [GitHub #41127](https://github.com/zephyrproject-rtos/zephyr/issues/41127) - OpenAMP Sample does not work on LPCXpresso55S69
- [GitHub #41117](https://github.com/zephyrproject-rtos/zephyr/issues/41117) - Incorrect setting of gyro sensitivity in LSM6DSO driver
- [GitHub #41111](https://github.com/zephyrproject-rtos/zephyr/issues/41111) - uint64 overflow in z\_tmcvt() function
- [GitHub #41100](https://github.com/zephyrproject-rtos/zephyr/issues/41100) - Non-standard RISC-V assembly is used
- [GitHub #41097](https://github.com/zephyrproject-rtos/zephyr/issues/41097) - west init issue
- [GitHub #41095](https://github.com/zephyrproject-rtos/zephyr/issues/41095) - libc: newlib: ‘gettimeofday’ causes stack overflow on non-POSIX builds
- [GitHub #41093](https://github.com/zephyrproject-rtos/zephyr/issues/41093) - Kconfig.defconfig:11: error: couldn’t parse ‘default $(dt\_node\_int\_prop\_int,/cpus/cpu@0,clock-frequency)’
- [GitHub #41077](https://github.com/zephyrproject-rtos/zephyr/issues/41077) - console: gsm\_mux: could not send more than 128 bytes of data on dlci
- [GitHub #41074](https://github.com/zephyrproject-rtos/zephyr/issues/41074) - can\_mcan\_send sends corrupted CAN frames with a byte-by-byte memcpy implementation
- [GitHub #41066](https://github.com/zephyrproject-rtos/zephyr/issues/41066) - twister –generate-map is broken
- [GitHub #41062](https://github.com/zephyrproject-rtos/zephyr/issues/41062) - kernel: userspace: Potential misaligned access
- [GitHub #41058](https://github.com/zephyrproject-rtos/zephyr/issues/41058) - stm32h723 : application gets hung during spi\_transceive() operation
- [GitHub #41052](https://github.com/zephyrproject-rtos/zephyr/issues/41052) - tests-ci : portability: posix: fs.tls.newlib test Build failure
- [GitHub #41050](https://github.com/zephyrproject-rtos/zephyr/issues/41050) - MCUMgr Sample Fails to build
- [GitHub #41043](https://github.com/zephyrproject-rtos/zephyr/issues/41043) - Sporadic Bus Fault when using I2C on a nrf52840
- [GitHub #41026](https://github.com/zephyrproject-rtos/zephyr/issues/41026) - LoRa: sx126x: DIO1 interrupt left enabled in sleep mode
- [GitHub #41024](https://github.com/zephyrproject-rtos/zephyr/issues/41024) - SPI Loopback test fails to build on iMX RT EVKs
- [GitHub #41017](https://github.com/zephyrproject-rtos/zephyr/issues/41017) - USB string descriptors can be re-ordered causing corruption and out-of-bounds-write
- [GitHub #41016](https://github.com/zephyrproject-rtos/zephyr/issues/41016) - i2c\_sam0.c i2c\_sam0\_transfer operations do not execute a STOP
- [GitHub #41012](https://github.com/zephyrproject-rtos/zephyr/issues/41012) - irq\_enable() doesn’t support enabling NVIC IRQ number more than 127
- [GitHub #40999](https://github.com/zephyrproject-rtos/zephyr/issues/40999) - Unable to boot smp\_svr sample image as documentation suggests, or sign
- [GitHub #40974](https://github.com/zephyrproject-rtos/zephyr/issues/40974) - Xtensa High priority interrupts cannot be masked during initialization
- [GitHub #40965](https://github.com/zephyrproject-rtos/zephyr/issues/40965) - Halt on receipt of Google Cloud IoT Core MQTT message sized 648+ bytes
- [GitHub #40946](https://github.com/zephyrproject-rtos/zephyr/issues/40946) - Xtensa Interrupt nesting issue
- [GitHub #40942](https://github.com/zephyrproject-rtos/zephyr/issues/40942) - Xtensa debug bug
- [GitHub #40936](https://github.com/zephyrproject-rtos/zephyr/issues/40936) - STM32 ADC gets stuck in Calibration
- [GitHub #40925](https://github.com/zephyrproject-rtos/zephyr/issues/40925) - mesh\_badge not working reel\_board\_v2
- [GitHub #40917](https://github.com/zephyrproject-rtos/zephyr/issues/40917) - twister –export-tests export all cases even this case can not run on given platform
- [GitHub #40916](https://github.com/zephyrproject-rtos/zephyr/issues/40916) - Assertion in nordic’s BLE controller lll.c:352
- [GitHub #40903](https://github.com/zephyrproject-rtos/zephyr/issues/40903) - documentation generation fails on function typedefs
- [GitHub #40889](https://github.com/zephyrproject-rtos/zephyr/issues/40889) - samples: samples/kernel/metairq\_dispatch failed on acrn\_ehl\_crb
- [GitHub #40888](https://github.com/zephyrproject-rtos/zephyr/issues/40888) - samples: samples/subsys/portability/cmsis\_rtos\_v1/philosophers failed on ehl crb
- [GitHub #40887](https://github.com/zephyrproject-rtos/zephyr/issues/40887) - tests: debug: test case subsys/debug/coredump failed on acrn\_ehl\_crb
- [GitHub #40883](https://github.com/zephyrproject-rtos/zephyr/issues/40883) - Limitation on logging module
- [GitHub #40881](https://github.com/zephyrproject-rtos/zephyr/issues/40881) - Bluetooth: shell: fatal error because ctx\_shell is NULL
- [GitHub #40873](https://github.com/zephyrproject-rtos/zephyr/issues/40873) - qemu\_cortex\_r5: fail to handle user\_string\_alloc\_copy() with null parameter
- [GitHub #40870](https://github.com/zephyrproject-rtos/zephyr/issues/40870) - tests: syscall: failed to build on fvp\_baser\_aemv8r\_smp
- [GitHub #40866](https://github.com/zephyrproject-rtos/zephyr/issues/40866) - Undefined behavior in lib/os/cbprintf\_packaged.c: subtraction involving definitely null pointer
- [GitHub #40838](https://github.com/zephyrproject-rtos/zephyr/issues/40838) - Nordic UART driver (UARTE) fail to transfer buffers from read only memory
- [GitHub #40827](https://github.com/zephyrproject-rtos/zephyr/issues/40827) - Tensorflow example not working in zephyr v2.6
- [GitHub #40825](https://github.com/zephyrproject-rtos/zephyr/issues/40825) - STM32WB55RGV6: No output after west flash
- [GitHub #40820](https://github.com/zephyrproject-rtos/zephyr/issues/40820) - coap: blockwise: context current does not match total size after transfer is completed
- [GitHub #40808](https://github.com/zephyrproject-rtos/zephyr/issues/40808) - Invalid CMake warning related to rimage
- [GitHub #40795](https://github.com/zephyrproject-rtos/zephyr/issues/40795) - Timer signal thread execution loop break SMP on ARM64
- [GitHub #40783](https://github.com/zephyrproject-rtos/zephyr/issues/40783) - samples/subsys/usb/dfu should filter on FLASH driver
- [GitHub #40776](https://github.com/zephyrproject-rtos/zephyr/issues/40776) - HCI\_USB with nRF52840 dongle disconnect after 30 s
- [GitHub #40775](https://github.com/zephyrproject-rtos/zephyr/issues/40775) - stm32: multi-threading broken after #40173
- [GitHub #40770](https://github.com/zephyrproject-rtos/zephyr/issues/40770) - tests/subsys/cpp/libcxx/cpp.libcxx.newlib fails on m2gl025\_miv and qemu\_cortex\_m0
- [GitHub #40761](https://github.com/zephyrproject-rtos/zephyr/issues/40761) - Bluetooth: host: Wait for the response callback before clearing Service Changed data
- [GitHub #40759](https://github.com/zephyrproject-rtos/zephyr/issues/40759) - Bluetooth: host: Improper restore of CCC values and handling Service Change indication when bonded peer reconnects
- [GitHub #40758](https://github.com/zephyrproject-rtos/zephyr/issues/40758) - Bluetooth: host: CCC values are not immediately stored on GATT Server by default (risk of inconsistency)
- [GitHub #40744](https://github.com/zephyrproject-rtos/zephyr/issues/40744) - RT600 LittleFS Sample produces build warning in default configuration
- [GitHub #40740](https://github.com/zephyrproject-rtos/zephyr/issues/40740) - tests: logging: test case log\_msg2.logging.log\_msg2\_64b\_timestamp failed on qemu\_cortex\_a9
- [GitHub #40724](https://github.com/zephyrproject-rtos/zephyr/issues/40724) - tests: logging: logging test cases failed in multiple boards
- [GitHub #40717](https://github.com/zephyrproject-rtos/zephyr/issues/40717) - twister: failure in parsing code coverage file
- [GitHub #40714](https://github.com/zephyrproject-rtos/zephyr/issues/40714) - west flash, Invalid DFU suffix signature
- [GitHub #40688](https://github.com/zephyrproject-rtos/zephyr/issues/40688) - in “pinmux\_stm32.c” function “stm32\_dt\_pinctrl\_remap” not work
- [GitHub #40672](https://github.com/zephyrproject-rtos/zephyr/issues/40672) - EDTT: buffer overflow in edtt\_hci\_app
- [GitHub #40668](https://github.com/zephyrproject-rtos/zephyr/issues/40668) - Issue with twister code coverage tests not working with minimal C library (nRF52840)
- [GitHub #40663](https://github.com/zephyrproject-rtos/zephyr/issues/40663) - WWDG not supported on STM32H7 family
- [GitHub #40658](https://github.com/zephyrproject-rtos/zephyr/issues/40658) - shtcx not reporting correct humidity value
- [GitHub #40646](https://github.com/zephyrproject-rtos/zephyr/issues/40646) - Can’t read more than one OUTPUT|INPUT gpio pin in gpio\_emul
- [GitHub #40643](https://github.com/zephyrproject-rtos/zephyr/issues/40643) - intel\_adsp\_cavs15: the zephyr\_pre0.elf is quite large (530MB) on ADSP for some test cases
- [GitHub #40640](https://github.com/zephyrproject-rtos/zephyr/issues/40640) - drivers: usb\_dc\_native\_posix: segfault when using composite USB device
- [GitHub #40638](https://github.com/zephyrproject-rtos/zephyr/issues/40638) - drivers: usb\_dc\_mcux: processing endpoint callbacks in ISR context causes assertion
- [GitHub #40633](https://github.com/zephyrproject-rtos/zephyr/issues/40633) - CI documentation build hangs when there is a broken reference
- [GitHub #40624](https://github.com/zephyrproject-rtos/zephyr/issues/40624) - twister: coverage: Using –coverage flag for on-target test make tests last until time limit
- [GitHub #40622](https://github.com/zephyrproject-rtos/zephyr/issues/40622) - Dark mode readability problem in Unit Test Documentation
- [GitHub #40621](https://github.com/zephyrproject-rtos/zephyr/issues/40621) - npcx uart driver uses device PM callback to block suspension
- [GitHub #40614](https://github.com/zephyrproject-rtos/zephyr/issues/40614) - poll: the code judgment condition is always true
- [GitHub #40590](https://github.com/zephyrproject-rtos/zephyr/issues/40590) - gen\_app\_partitions scans object files unrelated to current image
- [GitHub #40586](https://github.com/zephyrproject-rtos/zephyr/issues/40586) - tests: logging: Logging.add.user scenario fails on all nrf boards
- [GitHub #40578](https://github.com/zephyrproject-rtos/zephyr/issues/40578) - MODBUS RS-485 transceiver support broken on several platforms due to DE race condition
- [GitHub #40569](https://github.com/zephyrproject-rtos/zephyr/issues/40569) - bisected: kernel.common.stack\_protection\_arm\_fpu\_sharing fails on mps3\_an547
- [GitHub #40546](https://github.com/zephyrproject-rtos/zephyr/issues/40546) - Bluetooh:host: GATT notify multiple feature not working properly
- [GitHub #40538](https://github.com/zephyrproject-rtos/zephyr/issues/40538) - mcuboot build fails with nrf52 internal RC oscillator
- [GitHub #40517](https://github.com/zephyrproject-rtos/zephyr/issues/40517) - msgq: NULL handler assertion with data cache enabled
- [GitHub #40483](https://github.com/zephyrproject-rtos/zephyr/issues/40483) - ESP32: display sample over i2c not working
- [GitHub #40464](https://github.com/zephyrproject-rtos/zephyr/issues/40464) - Dereferencing NULL with getsockname() on TI Simplelink Platform
- [GitHub #40456](https://github.com/zephyrproject-rtos/zephyr/issues/40456) - Bluetooth: L2CAP tester application is missing preprocessor flags for ECFC function call
- [GitHub #40453](https://github.com/zephyrproject-rtos/zephyr/issues/40453) - LittleFS fails when block count is greater than block size
- [GitHub #40450](https://github.com/zephyrproject-rtos/zephyr/issues/40450) - Twister map file shows baud in quotes but should not be in quotes
- [GitHub #40449](https://github.com/zephyrproject-rtos/zephyr/issues/40449) - Twister tests fail when running on actual hardware due to deprecated command warning
- [GitHub #40439](https://github.com/zephyrproject-rtos/zephyr/issues/40439) - Undefined escape sequence: ill-formed for the C standard
- [GitHub #40438](https://github.com/zephyrproject-rtos/zephyr/issues/40438) - Ill-formed sources due to external linkage inline functions calling static functions
- [GitHub #40433](https://github.com/zephyrproject-rtos/zephyr/issues/40433) - RTT fails to work in program with large global variable
- [GitHub #40420](https://github.com/zephyrproject-rtos/zephyr/issues/40420) - Lower-case characters in Kconfig symbol names cause obscure errors
- [GitHub #40411](https://github.com/zephyrproject-rtos/zephyr/issues/40411) - Xtensa xcc compile build fails with SOF application on latest Zephyr main
- [GitHub #40376](https://github.com/zephyrproject-rtos/zephyr/issues/40376) - HiFIve1 failed to run tests/kernel/workq/work/
- [GitHub #40374](https://github.com/zephyrproject-rtos/zephyr/issues/40374) - up\_squared: isr\_dynamic test is failing
- [GitHub #40369](https://github.com/zephyrproject-rtos/zephyr/issues/40369) - tests/subsys/logging/log\_core/ and tests/subsys/shell/shell/ hang on qemu\_cortex\_a53 and qemu\_riscv64
- [GitHub #40367](https://github.com/zephyrproject-rtos/zephyr/issues/40367) - sample: cycle\_64 is failing out due to a timeout on 64-bit versions of qemu\_x86 and ehl\_crb
- [GitHub #40348](https://github.com/zephyrproject-rtos/zephyr/issues/40348) - STM32L496 Uart rx interrupt callback fails to work with LVGL
- [GitHub #40329](https://github.com/zephyrproject-rtos/zephyr/issues/40329) - nucleo\_g0b1re: FDCAN message RAM write fails on byte-oriented write
- [GitHub #40317](https://github.com/zephyrproject-rtos/zephyr/issues/40317) - Crash in ull.c when stressing periodic advertising sync (scanner side)
- [GitHub #40316](https://github.com/zephyrproject-rtos/zephyr/issues/40316) - Error undefined reference to ‘\_\_aeabi\_uldivmod’ when build with Zephyr 2.7.0 for STM32
- [GitHub #40298](https://github.com/zephyrproject-rtos/zephyr/issues/40298) - Bluetooth assertions in lll\_conn.c
- [GitHub #40290](https://github.com/zephyrproject-rtos/zephyr/issues/40290) - CAN\_STM32: Build error with CONFIG\_CAN\_AUTO\_BUS\_OFF\_RECOVERY=n
- [GitHub #40256](https://github.com/zephyrproject-rtos/zephyr/issues/40256) - websocket: the size of a websocket payload is limited
- [GitHub #40254](https://github.com/zephyrproject-rtos/zephyr/issues/40254) - TF-M: BL2 signing is broken due to incompatible MCUboot version
- [GitHub #40244](https://github.com/zephyrproject-rtos/zephyr/issues/40244) - [v2.7-branch] hci\_spi sample cannot be built for nrf51dk\_nrf51422 and 96b\_carbon\_nrf51
- [GitHub #40236](https://github.com/zephyrproject-rtos/zephyr/issues/40236) - Unsigned int can’t be used in condition compare with int
- [GitHub #40215](https://github.com/zephyrproject-rtos/zephyr/issues/40215) - RSSI in periodic adv. callbacks always -127 (sync\_recv and cte\_report\_cb)
- [GitHub #40209](https://github.com/zephyrproject-rtos/zephyr/issues/40209) - Bluetooth: First AUX\_SYNC\_IND never received, missing event send to host
- [GitHub #40202](https://github.com/zephyrproject-rtos/zephyr/issues/40202) - Bluetooth: Periodic advertising synchronization not re-established after advertiser reset without scan disable
- [GitHub #40198](https://github.com/zephyrproject-rtos/zephyr/issues/40198) - Shell module doesn’t work on main branch for esp32 board
- [GitHub #40189](https://github.com/zephyrproject-rtos/zephyr/issues/40189) - k\_poll infrastructure can miss “signals” in a heavily contended SMP system
- [GitHub #40169](https://github.com/zephyrproject-rtos/zephyr/issues/40169) - drivers: can: net: compilation broken and no test cases in CI
- [GitHub #40159](https://github.com/zephyrproject-rtos/zephyr/issues/40159) - Bluetooth Mesh branch incorrect return value
- [GitHub #40153](https://github.com/zephyrproject-rtos/zephyr/issues/40153) - mimxrt1050\_evk: failed to run samples/subsys/task\_wdt
- [GitHub #40152](https://github.com/zephyrproject-rtos/zephyr/issues/40152) - task\_wdt can get stuck in a loop where hardware reset is never fired
- [GitHub #40133](https://github.com/zephyrproject-rtos/zephyr/issues/40133) - mimxrt1060-evk flash shell command causes shell deadlock
- [GitHub #40129](https://github.com/zephyrproject-rtos/zephyr/issues/40129) - ‘tests/net/socket/tls/net.socket.tls.preempt’ fails with ‘qemu\_cortex\_a9’
- [GitHub #40124](https://github.com/zephyrproject-rtos/zephyr/issues/40124) - Build fails with ‘CONFIG\_SHELL\_VT100\_COMMANDS=n’
- [GitHub #40119](https://github.com/zephyrproject-rtos/zephyr/issues/40119) - OBJECT\_TRACING for kernel objects
- [GitHub #40115](https://github.com/zephyrproject-rtos/zephyr/issues/40115) - logging: int-uint comparsion causes false assert & epic hang
- [GitHub #40107](https://github.com/zephyrproject-rtos/zephyr/issues/40107) - lwm2m: if network drops during firmware update, lock occurs
- [GitHub #40077](https://github.com/zephyrproject-rtos/zephyr/issues/40077) - driver: wdt: twrke18f: test\_wdt fails
- [GitHub #40076](https://github.com/zephyrproject-rtos/zephyr/issues/40076) - Driver led pca9633 does only use first device in devicetree
- [GitHub #40074](https://github.com/zephyrproject-rtos/zephyr/issues/40074) - sara-r4: socket call fails due to regression
- [GitHub #40070](https://github.com/zephyrproject-rtos/zephyr/issues/40070) - canbus: isotp: Violations of k\_fifo and net\_buf API usage
- [GitHub #40069](https://github.com/zephyrproject-rtos/zephyr/issues/40069) - Bluetooth CCM encryption bug in MIC generation
- [GitHub #40068](https://github.com/zephyrproject-rtos/zephyr/issues/40068) - Test suite subsys.pm.device\_runtime\_api fail on qemu\_x86\_64
- [GitHub #40030](https://github.com/zephyrproject-rtos/zephyr/issues/40030) - STM32 SD hardware flow control gets disabled if disk\_access\_init is used
- [GitHub #40021](https://github.com/zephyrproject-rtos/zephyr/issues/40021) - mimxrt1060\_evk\_hyperflash board definition is broken
- [GitHub #40020](https://github.com/zephyrproject-rtos/zephyr/issues/40020) - tests: kernel: mem\_slab: mslab\_api: undefined reference to z\_impl\_k\_sem\_give and z\_impl\_k\_sem\_take
- [GitHub #40007](https://github.com/zephyrproject-rtos/zephyr/issues/40007) - twister: cannot build samples/tests on Windows
- [GitHub #40003](https://github.com/zephyrproject-rtos/zephyr/issues/40003) - Bluetooth: host: zephyr writes to disconnected device and triggers a bus fault
- [GitHub #40000](https://github.com/zephyrproject-rtos/zephyr/issues/40000) - k\_timer timeout handler is called with interrupts locked
- [GitHub #39989](https://github.com/zephyrproject-rtos/zephyr/issues/39989) - Zephyr does not persist CCC data written before bonding when bonding has completed which leads to loss of subscriptions on device reset
- [GitHub #39985](https://github.com/zephyrproject-rtos/zephyr/issues/39985) - Telnet shell breaks upon sending Ctrl+C character
- [GitHub #39978](https://github.com/zephyrproject-rtos/zephyr/issues/39978) - logging.log2\_api\_deferred and logging.msg2 tests fail on qemu\_cortex\_a9
- [GitHub #39973](https://github.com/zephyrproject-rtos/zephyr/issues/39973) - Bluetooth: hci\_usb example returning “Unknown HCI Command” after reset.
- [GitHub #39969](https://github.com/zephyrproject-rtos/zephyr/issues/39969) - USB not automatically enabled when USB\_UART\_CONSOLE is set
- [GitHub #39968](https://github.com/zephyrproject-rtos/zephyr/issues/39968) - samples: tfm\_integration: tfm\_psa\_test broken on OS X (Windows?)
- [GitHub #39947](https://github.com/zephyrproject-rtos/zephyr/issues/39947) - open-amp problem with dcache
- [GitHub #39942](https://github.com/zephyrproject-rtos/zephyr/issues/39942) - usdhc disk\_usdhc\_access\_write busy fail
- [GitHub #39923](https://github.com/zephyrproject-rtos/zephyr/issues/39923) - qspi\_sfdp\_read fails errata work around
- [GitHub #39919](https://github.com/zephyrproject-rtos/zephyr/issues/39919) - CONFIG\_ISM330DHCX cannot compile due to missing file
- [GitHub #39904](https://github.com/zephyrproject-rtos/zephyr/issues/39904) - bl654\_usb does not work with hci\_usb sample application
- [GitHub #39900](https://github.com/zephyrproject-rtos/zephyr/issues/39900) - usb bug :USB device descriptor could not be obtained on windows10
- [GitHub #39893](https://github.com/zephyrproject-rtos/zephyr/issues/39893) - Bluetooth: hci usb: scan duplicate filter not working
- [GitHub #39883](https://github.com/zephyrproject-rtos/zephyr/issues/39883) - BLE stack overlow due to the default option value when compiling with no optimization
- [GitHub #39874](https://github.com/zephyrproject-rtos/zephyr/issues/39874) - [Coverity CID: 240214] Dereference before null check in drivers/dma/dma\_mcux\_edma.c
- [GitHub #39872](https://github.com/zephyrproject-rtos/zephyr/issues/39872) - [Coverity CID: 240218] Dereference after null check in subsys/bluetooth/controller/ll\_sw/ull\_scan\_aux.c
- [GitHub #39870](https://github.com/zephyrproject-rtos/zephyr/issues/39870) - [Coverity CID: 240220] Argument cannot be negative in tests/net/socket/af\_packet\_ipproto\_raw/src/main.c
- [GitHub #39869](https://github.com/zephyrproject-rtos/zephyr/issues/39869) - [Coverity CID: 240221] Unchecked return value from library in drivers/usb/device/usb\_dc\_native\_posix.c
- [GitHub #39868](https://github.com/zephyrproject-rtos/zephyr/issues/39868) - [Coverity CID: 240222] Dereference before null check in drivers/dma/dma\_mcux\_edma.c
- [GitHub #39857](https://github.com/zephyrproject-rtos/zephyr/issues/39857) - [Coverity CID: 240234] Uninitialized scalar variable in subsys/bluetooth/shell/iso.c
- [GitHub #39856](https://github.com/zephyrproject-rtos/zephyr/issues/39856) - [Coverity CID: 240235] Explicit null dereferenced in subsys/bluetooth/controller/ll\_sw/ull\_scan\_aux.c
- [GitHub #39852](https://github.com/zephyrproject-rtos/zephyr/issues/39852) - [Coverity CID: 240241] Out-of-bounds access in subsys/bluetooth/host/adv.c
- [GitHub #39851](https://github.com/zephyrproject-rtos/zephyr/issues/39851) - [Coverity CID: 240242] Dereference after null check in tests/bluetooth/tester/src/l2cap.c
- [GitHub #39849](https://github.com/zephyrproject-rtos/zephyr/issues/39849) - [Coverity CID: 240244] Untrusted value as argument in drivers/usb/device/usb\_dc\_native\_posix.c
- [GitHub #39844](https://github.com/zephyrproject-rtos/zephyr/issues/39844) - [Coverity CID: 240658] Argument cannot be negative in tests/net/lib/dns\_sd/src/main.c
- [GitHub #39843](https://github.com/zephyrproject-rtos/zephyr/issues/39843) - [Coverity CID: 240659] Out-of-bounds read in /zephyr/include/generated/syscalls/kernel.h (Generated Code)
- [GitHub #39841](https://github.com/zephyrproject-rtos/zephyr/issues/39841) - [Coverity CID: 240661] Unchecked return value in tests/net/net\_pkt/src/main.c
- [GitHub #39840](https://github.com/zephyrproject-rtos/zephyr/issues/39840) - [Coverity CID: 240662] Improper use of negative value in subsys/mgmt/osdp/src/osdp.c
- [GitHub #39839](https://github.com/zephyrproject-rtos/zephyr/issues/39839) - [Coverity CID: 240663] Out-of-bounds access in tests/benchmarks/mbedtls/src/benchmark.c
- [GitHub #39835](https://github.com/zephyrproject-rtos/zephyr/issues/39835) - [Coverity CID: 240667] Improper use of negative value in samples/subsys/usb/cdc\_acm\_composite/src/main.c
- [GitHub #39833](https://github.com/zephyrproject-rtos/zephyr/issues/39833) - [Coverity CID: 240670] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #39832](https://github.com/zephyrproject-rtos/zephyr/issues/39832) - [Coverity CID: 240671] Out-of-bounds access in drivers/flash/flash\_mcux\_flexspi\_hyperflash.c
- [GitHub #39830](https://github.com/zephyrproject-rtos/zephyr/issues/39830) - [Coverity CID: 240673] Out-of-bounds read in /zephyr/include/generated/syscalls/kernel.h (Generated Code)
- [GitHub #39827](https://github.com/zephyrproject-rtos/zephyr/issues/39827) - [Coverity CID: 240676] Out-of-bounds access in drivers/ieee802154/ieee802154\_dw1000.c
- [GitHub #39825](https://github.com/zephyrproject-rtos/zephyr/issues/39825) - [Coverity CID: 240678] Unchecked return value in drivers/ieee802154/ieee802154\_cc1200.c
- [GitHub #39824](https://github.com/zephyrproject-rtos/zephyr/issues/39824) - [Coverity CID: 240679] Out-of-bounds access in samples/subsys/usb/cdc\_acm\_composite/src/main.c
- [GitHub #39823](https://github.com/zephyrproject-rtos/zephyr/issues/39823) - [Coverity CID: 240681] Improper use of negative value in drivers/bluetooth/hci/h4.c
- [GitHub #39817](https://github.com/zephyrproject-rtos/zephyr/issues/39817) - drivers: pwm: nxp: (potentially) Incorrect return value on API function
- [GitHub #39815](https://github.com/zephyrproject-rtos/zephyr/issues/39815) - [Coverity CID: 240688] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #39813](https://github.com/zephyrproject-rtos/zephyr/issues/39813) - [Coverity CID: 240691] Out-of-bounds access in tests/benchmarks/mbedtls/src/benchmark.c
- [GitHub #39812](https://github.com/zephyrproject-rtos/zephyr/issues/39812) - [Coverity CID: 240692] Unintended sign extension in subsys/stats/stats.c
- [GitHub #39810](https://github.com/zephyrproject-rtos/zephyr/issues/39810) - [Coverity CID: 240696] Operands don’t affect result in subsys/net/lib/lwm2m/lwm2m\_util.c
- [GitHub #39809](https://github.com/zephyrproject-rtos/zephyr/issues/39809) - [Coverity CID: 240697] Out-of-bounds access in samples/subsys/usb/cdc\_acm/src/main.c
- [GitHub #39807](https://github.com/zephyrproject-rtos/zephyr/issues/39807) - [Coverity CID: 240699] Out-of-bounds access in tests/bluetooth/tester/src/l2cap.c
- [GitHub #39806](https://github.com/zephyrproject-rtos/zephyr/issues/39806) - [Coverity CID: 240700] Unchecked return value in drivers/ieee802154/ieee802154\_cc2520.c
- [GitHub #39805](https://github.com/zephyrproject-rtos/zephyr/issues/39805) - [Coverity CID: 240703] Improper use of negative value in drivers/bluetooth/hci/h4.c
- [GitHub #39797](https://github.com/zephyrproject-rtos/zephyr/issues/39797) - STM32 G4 series compile error when both ADC1 and ADC2 are opened
- [GitHub #39780](https://github.com/zephyrproject-rtos/zephyr/issues/39780) - On ESP32S2 platform zsock\_getaddrinfo() call causes RTOS to crash
- [GitHub #39774](https://github.com/zephyrproject-rtos/zephyr/issues/39774) - modem: uart mux reading optimization never used
- [GitHub #39758](https://github.com/zephyrproject-rtos/zephyr/issues/39758) - Build is broken if LWM2M\_CANCEL\_OBSERVE\_BY\_PATH config is set
- [GitHub #39756](https://github.com/zephyrproject-rtos/zephyr/issues/39756) - kconfig: choice default is not set if hidden under invisible menu
- [GitHub #39726](https://github.com/zephyrproject-rtos/zephyr/issues/39726) - How to use PWM LED driver for ESP32?
- [GitHub #39721](https://github.com/zephyrproject-rtos/zephyr/issues/39721) - bq274xx sensor - Fails to compile when CONFIG\_PM\_DEVICE enabled
- [GitHub #39720](https://github.com/zephyrproject-rtos/zephyr/issues/39720) - XCC BUILD FAIL :K\_MEM\_SLAB\_DEFINE && K\_HEAP\_DEFINE
- [GitHub #39718](https://github.com/zephyrproject-rtos/zephyr/issues/39718) - STM32L496G\_DISCO uart testing fails on single buffer read
- [GitHub #39712](https://github.com/zephyrproject-rtos/zephyr/issues/39712) - bq274xx sensor - Fails to compile when CONFIG\_PM\_DEVICE enabled
- [GitHub #39707](https://github.com/zephyrproject-rtos/zephyr/issues/39707) - Can’t enable CONFIG\_SHELL\_LOG\_BACKEND Log Shell Menus with pure Telnet Shell Backend
- [GitHub #39705](https://github.com/zephyrproject-rtos/zephyr/issues/39705) - Canot use POSIX\_API and NET\_SOCKETS together
- [GitHub #39704](https://github.com/zephyrproject-rtos/zephyr/issues/39704) - Using OpenThread makes the system unresponsive after 49.7 days
- [GitHub #39703](https://github.com/zephyrproject-rtos/zephyr/issues/39703) - stm32 uart testing fails on test\_read\_abort
- [GitHub #39687](https://github.com/zephyrproject-rtos/zephyr/issues/39687) - sensor: qdec\_nrfx: PM callback has incorrect signature
- [GitHub #39675](https://github.com/zephyrproject-rtos/zephyr/issues/39675) - list\_boards.py script doesn’t properly traverse external board roots
- [GitHub #39672](https://github.com/zephyrproject-rtos/zephyr/issues/39672) - net\_config\_init count calculation appears incorrect.
- [GitHub #39660](https://github.com/zephyrproject-rtos/zephyr/issues/39660) - poll() not notified when a TLS/TCP connection is closed without TLS close\_notify
- [GitHub #39655](https://github.com/zephyrproject-rtos/zephyr/issues/39655) - Linker error with CONFIG\_NET\_TCP=y
- [GitHub #39645](https://github.com/zephyrproject-rtos/zephyr/issues/39645) - STM32L496 Zephyr using LVGL disp\_drv.flush\_cb can not work
- [GitHub #39629](https://github.com/zephyrproject-rtos/zephyr/issues/39629) - Small Compiler warning in subsys/fs/shell.c:381:23 in latest release, need argument change only
- [GitHub #39627](https://github.com/zephyrproject-rtos/zephyr/issues/39627) - samples: http\_get: cannot run on QEMU
- [GitHub #39624](https://github.com/zephyrproject-rtos/zephyr/issues/39624) - Bluetooth: Submitting more GATT writes than available buffers blocks for 30s and then errors out
- [GitHub #39619](https://github.com/zephyrproject-rtos/zephyr/issues/39619) - twister: integration\_platforms getting unnoticeably skipped when –subset is used
- [GitHub #39609](https://github.com/zephyrproject-rtos/zephyr/issues/39609) - spi: slave: division by zero in timeout calculation
- [GitHub #39601](https://github.com/zephyrproject-rtos/zephyr/issues/39601) - On ESP32S2 platform GPIO interrupt causes RTOS to hang when configured to GPIO\_INT\_EDGE\_BOTH
- [GitHub #39594](https://github.com/zephyrproject-rtos/zephyr/issues/39594) - Possible bug or undocumented behaviour of spi\_write
- [GitHub #39588](https://github.com/zephyrproject-rtos/zephyr/issues/39588) - drivers: i2c: nrf: i2c error with burst write
- [GitHub #39575](https://github.com/zephyrproject-rtos/zephyr/issues/39575) - k\_mutex\_lock and k\_sem\_take with K\_FOREVER return -EAGAIN value
- [GitHub #39569](https://github.com/zephyrproject-rtos/zephyr/issues/39569) - [ESP32] crash when trying to set a low cpu clock frequency
- [GitHub #39549](https://github.com/zephyrproject-rtos/zephyr/issues/39549) - Bluetooth: Incomplete Delayed Initialization of acl\_mtu Allows Controller to Crash Host Layer
- [GitHub #39546](https://github.com/zephyrproject-rtos/zephyr/issues/39546) - mcumgr over serial does not add CRC to length of packet len
- [GitHub #39541](https://github.com/zephyrproject-rtos/zephyr/issues/39541) - can: mcux\_flexcan: wrong timing calculation
- [GitHub #39538](https://github.com/zephyrproject-rtos/zephyr/issues/39538) - logging: rtt: Compilation fails when CONFIG\_LOG\_BACKEND\_RTT\_MODE\_OVERWRITE=y and CONFIG\_MULTITHREADING=n
- [GitHub #39523](https://github.com/zephyrproject-rtos/zephyr/issues/39523) - task watchdog crash/asset on NRF52840 - need to reorder task\_wdt\_feed() in task\_wdt\_add()
- [GitHub #39516](https://github.com/zephyrproject-rtos/zephyr/issues/39516) - function net\_eth\_vlan\_enable does not properly validate vlan tag value
- [GitHub #39506](https://github.com/zephyrproject-rtos/zephyr/issues/39506) - Bluetooth: crash in att.c when repeatedly scanning/connecting/disconnecting
- [GitHub #39505](https://github.com/zephyrproject-rtos/zephyr/issues/39505) - question: ethernet: carrier\_on\_off
- [GitHub #39503](https://github.com/zephyrproject-rtos/zephyr/issues/39503) - Zephyr boot banner not updated on rebuild with opdated SHA
- [GitHub #39497](https://github.com/zephyrproject-rtos/zephyr/issues/39497) - doc: kernel: event object static initialization mismatch
- [GitHub #39487](https://github.com/zephyrproject-rtos/zephyr/issues/39487) - esp32 IRQ01 stack utilisation is 100%
- [GitHub #39483](https://github.com/zephyrproject-rtos/zephyr/issues/39483) - LSM6DS0 Gyroscope rad/s Calculation Error
- [GitHub #39463](https://github.com/zephyrproject-rtos/zephyr/issues/39463) - ESP32 GPIO intterupt
- [GitHub #39461](https://github.com/zephyrproject-rtos/zephyr/issues/39461) - Bluetooth: hci acl flow control: bugs of bluetooth hci ACL flow control
- [GitHub #39457](https://github.com/zephyrproject-rtos/zephyr/issues/39457) - mec15xxevb\_assy6853: metairq\_dispatch sample is failing due to timeout while monitoring serial output
- [GitHub #39438](https://github.com/zephyrproject-rtos/zephyr/issues/39438) - Scanning for devices sending periodic advertisements stops working after a while, but keeps reporting none periodic.
- [GitHub #39423](https://github.com/zephyrproject-rtos/zephyr/issues/39423) - mcuboot not upgrade for stm32l1 series
- [GitHub #39418](https://github.com/zephyrproject-rtos/zephyr/issues/39418) - test: run testcase failed on platform mps2\_an521\_ns
- [GitHub #39416](https://github.com/zephyrproject-rtos/zephyr/issues/39416) - west debug throws error
- [GitHub #39405](https://github.com/zephyrproject-rtos/zephyr/issues/39405) - CTE report callback have the wrong pointer to bt\_le\_per\_adv\_sync
- [GitHub #39400](https://github.com/zephyrproject-rtos/zephyr/issues/39400) - stm32f103 example servo\_motor don’t work
- [GitHub #39399](https://github.com/zephyrproject-rtos/zephyr/issues/39399) - linker: Missing align \_\_itcm\_load\_start / \_\_dtcm\_data\_load\_start linker symbols
- [GitHub #39392](https://github.com/zephyrproject-rtos/zephyr/issues/39392) - ARC nsim\_sem fail on tests/crypto/tinycrypt\_hmac\_prng test when use ARCMWDT toolchain
- [GitHub #39340](https://github.com/zephyrproject-rtos/zephyr/issues/39340) - Shell FS sample halts with a usage fault error
- [GitHub #39311](https://github.com/zephyrproject-rtos/zephyr/issues/39311) - SPDX –init fails on windows systems
- [GitHub #39300](https://github.com/zephyrproject-rtos/zephyr/issues/39300) - Library globals in .sdata/.sbss sections doesn’t put into memory partition in userspace
- [GitHub #39293](https://github.com/zephyrproject-rtos/zephyr/issues/39293) - Can not run normally on MIMXRT1061CVL5A SOC
- [GitHub #39269](https://github.com/zephyrproject-rtos/zephyr/issues/39269) - Fail to initialize BLE stack with optimization level zero
- [GitHub #39253](https://github.com/zephyrproject-rtos/zephyr/issues/39253) - modem: hl7800: IPv6 socket not created properly
- [GitHub #39242](https://github.com/zephyrproject-rtos/zephyr/issues/39242) - net: sockets: Zephyr Fatal in dns\_resolve\_cb if dns request was attempted in offline state
- [GitHub #39221](https://github.com/zephyrproject-rtos/zephyr/issues/39221) - Errors when debuging application in Eclipse using STM32L496G-DISCO
- [GitHub #39216](https://github.com/zephyrproject-rtos/zephyr/issues/39216) - Twister: Broken on NRF52840 with pyocd option timeout error
- [GitHub #39179](https://github.com/zephyrproject-rtos/zephyr/issues/39179) - twister: –generate-hardware-map ends up in RuntimeError
- [GitHub #39144](https://github.com/zephyrproject-rtos/zephyr/issues/39144) - gsm\_ppp: stop & starting not working as expected with nullpointer dereference & no full modem init
- [GitHub #39136](https://github.com/zephyrproject-rtos/zephyr/issues/39136) - SD disk access runs into TXUNDERRUN and RXOVERRUN of SDMMC driver
- [GitHub #39131](https://github.com/zephyrproject-rtos/zephyr/issues/39131) - GATT DB hash calculation is wrong on characteristic declarations using 128-bit UUIDs.
- [GitHub #39096](https://github.com/zephyrproject-rtos/zephyr/issues/39096) - DNS responders assume interfaces are up at initialization
- [GitHub #39024](https://github.com/zephyrproject-rtos/zephyr/issues/39024) - drivers: sensors: FXOS8700: Interrupt pin routing configuration must be changed in standby power mode
- [GitHub #38988](https://github.com/zephyrproject-rtos/zephyr/issues/38988) - MCP2515 driver CS gpio active high support issue
- [GitHub #38987](https://github.com/zephyrproject-rtos/zephyr/issues/38987) - Unable to build ESP32 example code using west tool - zephyr
- [GitHub #38954](https://github.com/zephyrproject-rtos/zephyr/issues/38954) - Can’t get FlexPWM working for imxrt1060
- [GitHub #38631](https://github.com/zephyrproject-rtos/zephyr/issues/38631) - printk to console fails for freescale kinetis 8.2.0 (Zephyr 2.6.0) on FRDM-K64F
- [GitHub #38624](https://github.com/zephyrproject-rtos/zephyr/issues/38624) - mcuboot gets the wrong value of DT\_FIXED\_PARTITION\_ID
- [GitHub #38606](https://github.com/zephyrproject-rtos/zephyr/issues/38606) - drivers: adc: stm32h7: Oversampling Ratio set incorrectly
- [GitHub #38598](https://github.com/zephyrproject-rtos/zephyr/issues/38598) - net\_context\_put will not properly close TCP connection (might lead to tcp connection leak)
- [GitHub #38576](https://github.com/zephyrproject-rtos/zephyr/issues/38576) - net shell: self-connecting to TCP might lead to a crash
- [GitHub #38502](https://github.com/zephyrproject-rtos/zephyr/issues/38502) - Update mcumgr library to fix wrong callback state
- [GitHub #38446](https://github.com/zephyrproject-rtos/zephyr/issues/38446) - intel\_adsp\_cavs15: Fail to get testcases output on ADSP
- [GitHub #38376](https://github.com/zephyrproject-rtos/zephyr/issues/38376) - Raw Socket Failure when using 2 Raw Sockets and zsock\_select() statement - improper mapping from sock to handlers
- [GitHub #38303](https://github.com/zephyrproject-rtos/zephyr/issues/38303) - The current BabbleSim tests build system based on bash scripts hides warnings
- [GitHub #38128](https://github.com/zephyrproject-rtos/zephyr/issues/38128) - [Coverity CID: 239574] Out-of-bounds access in subsys/storage/flash\_map/flash\_map.c
- [GitHub #38047](https://github.com/zephyrproject-rtos/zephyr/issues/38047) - twister: The –board-root parameter doesn’t appear to work
- [GitHub #37893](https://github.com/zephyrproject-rtos/zephyr/issues/37893) - mcumgr\_serial\_tx\_pkt with len==91 fails to transmit CRC
- [GitHub #37389](https://github.com/zephyrproject-rtos/zephyr/issues/37389) - nucleo\_g0b1re: Swapping image in mcuboot results in hard fault and softbricks the device
- [GitHub #36986](https://github.com/zephyrproject-rtos/zephyr/issues/36986) - LittleFS mount fails (error -22)
- [GitHub #36962](https://github.com/zephyrproject-rtos/zephyr/issues/36962) - littlefs: Too small heap for file cache (again).
- [GitHub #36852](https://github.com/zephyrproject-rtos/zephyr/issues/36852) - acrn\_ehl\_crb: the test of tests/subsys/cpp/libcxx/ failed
- [GitHub #36808](https://github.com/zephyrproject-rtos/zephyr/issues/36808) - xtensa xcc build Fail , CONFIG\_NO\_OPTIMIZATIONS=y
- [GitHub #36766](https://github.com/zephyrproject-rtos/zephyr/issues/36766) - tests-ci :kernel.tickless.concept.tickless\_slice : test failed
- [GitHub #34732](https://github.com/zephyrproject-rtos/zephyr/issues/34732) - stm32h747i\_disco: Wrong Power supply setting LDO
- [GitHub #34375](https://github.com/zephyrproject-rtos/zephyr/issues/34375) - drivers: can: CAN configure fails when CONFIG\_CAN\_FD\_MODE is enabled
- [GitHub #31748](https://github.com/zephyrproject-rtos/zephyr/issues/31748) - boards:lpcxpresso55s69: Manual toggling of CS required with ETH Click shield
- [GitHub #23052](https://github.com/zephyrproject-rtos/zephyr/issues/23052) - nrf52840\_pca10056: Spurious RTS pulse and incorrect line level with hardware flow control disabled
- [GitHub #16587](https://github.com/zephyrproject-rtos/zephyr/issues/16587) - build failures with gcc 9.x
- [GitHub #8924](https://github.com/zephyrproject-rtos/zephyr/issues/8924) - Get rid of -fno-strict-overflow
