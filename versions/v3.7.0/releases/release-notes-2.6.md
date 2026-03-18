---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/releases/release-notes-2.6.html
original_path: releases/release-notes-2.6.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Zephyr 2.6.0

We are pleased to announce the release of Zephyr RTOS version 2.6.0.

Major enhancements with this release include:

- Logging subsystem overhauled
- Added support for 64-bit ARCv3
- Split ARM32 and ARM64, ARM64 is now a top-level architecture
- Added initial support for Arm v8.1-m and Cortex-M55
- Removed legacy TCP stack support which was deprecated in 2.4
- Tracing subsystem overhaul including expansion for tracing points and
  added support for Percepio Tracealyzer
- Device runtime power management (PM), former IDLE runtime, was
  completely overhauled.
- Added an example standalone Zephyr application in its own Git repository:
  [https://github.com/zephyrproject-rtos/example-application](https://github.com/zephyrproject-rtos/example-application)

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

- CVE-2021-3581: Under embargo until 2021-09-04

## Known issues

You can check all currently known issues by listing them using the GitHub
interface and listing all issues with the [bug label](https://github.com/zephyrproject-rtos/zephyr/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

## API Changes

- Driver APIs now return `-ENOSYS` if optional functions are not implemented.
  If the feature is not supported by the hardware `-ENOTSUP` will be returned.
  Formerly `-ENOTSUP` was returned for both failure modes, meaning this change
  may require existing code that tests only for that value to be changed.
- The `wait_for_usb_dfu()` function now accepts a `k_timeout_t` argument instead of
  using the `CONFIG_USB_DFU_WAIT_DELAY_MS` macro.
- Added disconnect reason to the `disconnected()` callback of `bt_iso_chan_ops`.
- Align error handling of :c:func:bt\_l2cap\_chan\_send and
  `bt_iso_chan_send()` so when an error occur the buffer is not unref.
- Added `lwm2m_engine_delete_obj_inst()` function to the LwM2M library API.

Deprecated in this release

- `DT_CLOCKS_LABEL_BY_IDX`, `DT_CLOCKS_LABEL_BY_NAME`,
  `DT_CLOCKS_LABEL`, `DT_INST_CLOCKS_LABEL_BY_IDX`,
  `DT_INST_CLOCKS_LABEL_BY_NAME`, and
  `DT_INST_CLOCKS_LABEL` was deprecated in favor of utilizing
  [`DT_CLOCKS_CTLR`](../build/dts/api/api.md#c.DT_CLOCKS_CTLR "DT_CLOCKS_CTLR") and variants.
- `DT_PWMS_LABEL_BY_IDX`, `DT_PWMS_LABEL_BY_NAME`,
  `DT_PWMS_LABEL`, `DT_INST_PWMS_LABEL_BY_IDX`,
  `DT_INST_PWMS_LABEL_BY_NAME`, and
  `DT_INST_PWMS_LABEL` was deprecated in favor of utilizing
  [`DT_PWMS_CTLR`](../build/dts/api/api.md#c.DT_PWMS_CTLR "DT_PWMS_CTLR") and variants.
- `DT_IO_CHANNELS_LABEL_BY_IDX`,
  `DT_IO_CHANNELS_LABEL_BY_NAME`,
  `DT_IO_CHANNELS_LABEL`,
  `DT_INST_IO_CHANNELS_LABEL_BY_IDX`,
  `DT_INST_IO_CHANNELS_LABEL_BY_NAME`, and
  `DT_INST_IO_CHANNELS_LABEL` were deprecated in favor of utilizing
  [`DT_IO_CHANNELS_CTLR`](../build/dts/api/api.md#c.DT_IO_CHANNELS_CTLR "DT_IO_CHANNELS_CTLR") and variants.
- `DT_DMAS_LABEL_BY_IDX`,
  `DT_DMAS_LABEL_BY_NAME`,
  `DT_INST_DMAS_LABEL_BY_IDX`, and
  `DT_INST_DMAS_LABEL_BY_NAME` were deprecated in favor of utilizing
  [`DT_DMAS_CTLR`](../build/dts/api/api.md#c.DT_DMAS_CTLR "DT_DMAS_CTLR") and variants.
- USB HID specific macros in `<include/usb/class/usb_hid.h>` are deprecated
  in favor of new common HID macros defined in `<include/usb/class/hid.h>`.
- USB HID Kconfig option USB\_HID\_PROTOCOL\_CODE is deprecated.
  USB\_HID\_PROTOCOL\_CODE does not allow to set boot protocol code for specific
  HID device. USB HID API function usb\_hid\_set\_proto\_code() can be used instead.
- USB HID class API is changed by removing get\_protocol/set\_protocol and
  get\_idle/set\_idle callbacks. These callbacks are redundant or do not provide
  any additional value and have led to incorrect usage of HID class API.
- The `CONFIG_OPENOCD_SUPPORT` Kconfig option has been deprecated in favor
  of `CONFIG_DEBUG_THREAD_INFO`.
- Disk API header `<include/disk/disk_access.h>` is deprecated in favor of
  `<include/storage/disk_access.h>`.
- `flash_write_protection_set()`.
- The `CONFIG_NET_CONTEXT_TIMESTAMP` is removed as it was only able to work
  with transmitted data. The same functionality can be achieved by setting
  `CONFIG_NET_PKT_RXTIME_STATS` and `CONFIG_NET_PKT_TXTIME_STATS` options.
  These options are also able to calculate the RX & TX times more accurately.
  This means that support for the SO\_TIMESTAMPING socket option is also removed
  as it was used by the removed config option.
- The device power management (PM) APIs and data structures have been renamed
  from `device_pm_*` to `pm_device_*` since they are not device APIs but PM
  subsystem APIs. The same applies to enumerations and definitions, they now
  follow the `PM_DEVICE_*` convention. Some other API calls such as
  `device_set_power_state` and `device_get_power_state` have been renamed to
  `pm_device_state_set` and `pm_device_state_get` in order to align with
  the naming of other device PM APIs.
- The runtime device power management (PM) APIs is now synchronous by default
  and the asynchronous API has the **\_async** sufix. This change aligns the API
  with the convention used in Zephyr. The affected APIs are
  `pm_device_put` and `pm_device_get`.
- The following functions, macros, and structures related to the kernel
  work queue API:

  - `k_work_pending()` replace with [`k_work_is_pending()`](../kernel/services/threads/workqueue.md#c.k_work_is_pending "k_work_is_pending")
  - `k_work_q_start()` replace with [`k_work_queue_start()`](../kernel/services/threads/workqueue.md#c.k_work_queue_start "k_work_queue_start")
  - `k_delayed_work` replace with [`k_work_delayable`](../kernel/services/threads/workqueue.md#c.k_work_delayable "k_work_delayable")
  - `k_delayed_work_init()` replace with
    [`k_work_init_delayable()`](../kernel/services/threads/workqueue.md#c.k_work_init_delayable "k_work_init_delayable")
  - `k_delayed_work_submit_to_queue()` replace with
    [`k_work_schedule_for_queue()`](../kernel/services/threads/workqueue.md#c.k_work_schedule_for_queue "k_work_schedule_for_queue") or
    [`k_work_reschedule_for_queue()`](../kernel/services/threads/workqueue.md#c.k_work_reschedule_for_queue "k_work_reschedule_for_queue")
  - `k_delayed_work_submit()` replace with [`k_work_schedule()`](../kernel/services/threads/workqueue.md#c.k_work_schedule "k_work_schedule")
    or [`k_work_reschedule()`](../kernel/services/threads/workqueue.md#c.k_work_reschedule "k_work_reschedule")
  - `k_delayed_work_pending()` replace with
    [`k_work_delayable_is_pending()`](../kernel/services/threads/workqueue.md#c.k_work_delayable_is_pending "k_work_delayable_is_pending")
  - `k_delayed_work_cancel()` replace with
    [`k_work_cancel_delayable()`](../kernel/services/threads/workqueue.md#c.k_work_cancel_delayable "k_work_cancel_delayable")
  - `k_delayed_work_remaining_get()` replace with
    [`k_work_delayable_remaining_get()`](../kernel/services/threads/workqueue.md#c.k_work_delayable_remaining_get "k_work_delayable_remaining_get")
  - `k_delayed_work_expires_ticks()` replace with
    [`k_work_delayable_expires_get()`](../kernel/services/threads/workqueue.md#c.k_work_delayable_expires_get "k_work_delayable_expires_get")
  - `k_delayed_work_remaining_ticks()` replace with
    [`k_work_delayable_remaining_get()`](../kernel/services/threads/workqueue.md#c.k_work_delayable_remaining_get "k_work_delayable_remaining_get")
  - `K_DELAYED_WORK_DEFINE` replace with
    [`K_WORK_DELAYABLE_DEFINE`](../kernel/services/threads/workqueue.md#c.K_WORK_DELAYABLE_DEFINE "K_WORK_DELAYABLE_DEFINE")

---

Removed APIs in this release

- Removed support for the old zephyr integer typedefs (u8\_t, u16\_t, etc…).
- Removed support for k\_mem\_domain\_destroy and k\_mem\_domain\_remove\_thread
- Removed support for counter\_read and counter\_get\_max\_relative\_alarm
- Removed support for device\_list\_get

---

### Stable API changes in this release

## Kernel

- Added [`k_mem_unmap()`](../kernel/memory_management/virtual_memory.md#c.k_mem_unmap "k_mem_unmap") so anonymous memory mapped via [`k_mem_map()`](../kernel/memory_management/virtual_memory.md#c.k_mem_map "k_mem_map")
  can be unmapped and virtual address reclaimed.
- Added the ability to gather more statistics for demand paging, including execution
  time histograms for eviction algorithms and backing stores.

## Architectures

- ARC

  - Added new ARCv3 64bit ISA support and corresponding HS6x processor support
  - Hardened SMP support
  - Various minor fixes/improvements for ARC MWDT toolchain infrastructure
  - Refactor of ARC Kconfig
- ARM

  - AARCH32

    - Added support for null pointer dereferencing detection in Cortex-M.
    - Added initial support for Arm v8.1-m and Cortex-M55.
    - Added support for preempting threads while they are performing secure calls in Cortex-M.
    - Added support for memory region generation by the linker based on device tree node information in Cortex-M.
    - Cleaned up definitions of SoC-specific memory regions in the common Cortex-M linker script.
    - Added support for clearing NXP MPU region configuration during Zephyr early boot stage.
    - Disallowed fpu hard ABI when building Non-Secure applications with TF-M on Cortex-M33.
    - Enhanced register information dump in fault exceptions in Cortex-R.
    - Fixed spurious interrupt handling in Cortex-R.
  - AARCH64

    - SMP support
    - MMU dynamic mappings with page table sharing.
    - Userspace (unprivileged) thread support.
    - Standalone SMCCC support.
    - XIP support.
    - ARM64 is now a top-level standalone architecture.
    - Support for Cortex-R82 and Armv8-R AArch64 MPU.
    - Cache management support.
    - Revamped boot code.
    - Full FPU context switching.
- x86

  - Added SoC configuration for Lakemont SoC.
  - Removed kconfig `CONFIG_CPU_MINUTEIA` as there is no user of this option.
  - Renamed kconfig `CONFIG_SSE*` to `CONFIG_X86_SSE*`.
  - Extended the pagetable generation script to allow specifying additional
    memory mapping during build.
  - x86-32

    - Added support for kernel image to reside in virtual address space, allowing
      code execution and data manipulation via virtual addresses.

## Bluetooth

- Audio

  - Split up ISO handling from audio handling, and moved the latter to its
    own directory.
  - Added the Volume Offset Control Service and client.
  - Added the Audio Input Control Service and client.
  - Added the Volume Control Service and client.
- Host

  - Added basic support for Direction Finding.
  - Added support for CTE connectionless transimission and reception over
    periodic advertising.
  - Refactored the HCI and ECC handling implementations.
  - Stopped auto updating the device name in the adv data.
  - Added support for logging security keys to be used by an air sniffer.
  - Fixed a bonding issue where the local bond data was not being updated after
    the remote device had removed it when the peer was not using the IRK stored
    in the bonding information.
  - Implemented the directory listing object to OTS.
  - Added a function to access the `bt_conn_iso` object.
  - Added a new configuration option for writeable device name.
  - Added a new configuration option for minimum encryption key size.
  - Added support for keypress notifications as an SMP responder.
  - Added a new option, `BT_LE_ADV_OPT_FORCE_NAME_IN_AD`, which forces the
    device name to appear in the adv packet instead of the scan response.
  - Added a security level check when sending a notification or indication.
  - Added the ability to send HCI monitor traces over RTT.
  - Refactored the Bluetooth buffer configuration for simplicity. See the
    commit message of 6483e12a8ac4f495b28279a6b84014f633b0d374 for more info.
    Note however that the aforementioned commit message has two typos;

    - `BT_CTLR_TX_BUFFER` should be `BT_CTLR_TX_BUFFERS`
    - `BT_CTLR_TX_BUFFERS_SIZE` should be `BT_CTLR_TX_BUFFER_SIZE`
  - Added support for concurrent advertising with multiple identities.
  - Changed the logic to disable scanning before setting the random address.
  - Fixed a crash where an ATT timeout occurred on a disconnected ATT channel.
  - Changed the pairing procedure to fail pairing when both sides have the same
    public key.
  - Fixed an issue where GATT requests could deadlock the RX thread.
  - Fixed an issue where a fixed passkey that was previously set could not be
    cleared.
  - Fixed an issue where callbacks for “security changed” and “pairing failed”
    were not always called.
  - Changed the pairing procedure to fail early if the remote device could not
    reach the required security level.
  - Fixed an issue where GATT notifications and Writes Without Response could
    be sent out of order.
  - Changed buffer ownership of `bt_l2cap_chan_send`.
    The application must now release the buffer for all returned errors.
- Mesh

  - Added CDB handle key refresh phase.
  - Added the ability to perform replay checks on SeqAuth.
  - Added the sending of a Link Close message when closing a link.
  - Added a Proxy callback structure for Node ID enabling and disabling.
  - Added a check for the response address in the Configuration Client.
  - Introduced a new acknowledged messages API.
  - Reworked the periodic publication timer and poll timeout scheduling logic.
  - Added reporting configured `LPNTimeout` in `cfg_srv`.
  - Ensured that provisioning output count number is at least 1.
  - Ensured to encrypt initial friend poll with friend credentials.
  - Stopped resetting the PB ADV reliable timer on retransmission.
- Bluetooth LE split software Controller

  - Removed support for the nRF5340 PDK. Use the nRF5340 DK instead.
  - Added basic support for Direction Finding.
  - Added support for CTE connectionless transimission and reception over
    periodic advertising.
  - Added support for antenna switching in the context of Direction Finding.
  - Added an invalid ACL data length check.
  - Added basic support for the ISO Adaptation Layer.
  - Added experimental support for Broadcast Isochronous Groups and Streams.
  - Added partial experimental support for Connected Isochronous Groups and
    Streams.
  - Implemented extended connection creation and cancellation.
  - Changed the policy to ignore connection requests from an already-connected
    peer.
  - Added a control procedure locking system.
  - Added GPIO PA/LNA support for the Nordic nRF53x SoC series.
  - Added FEM support for the nRF21540 IC.
  - Added a new radio API to configure the CTE RX path.
- HCI Driver

  - Added support for the Espressif ESP32 platform.

## Boards & SoC Support

- Added support for these SoC series:

  - STM32F205xx
  - STM32G03yxx, STM32G05yxx, STM32G070xx and STM32G0byxx
  - STM32G4x1, STM32G4x3 and STM32G484xE
  - STM32WL55xx
  - Nuvoton npcx7m6fc, and npcx7m6fc
  - Renesas R-Car Gen3
  - Silicon Labs EFR32FG13P
  - ARM MPS3-AN547
  - ARM FVP-AEMv8A
  - ARM FVP-AEMv8R
  - NXP LS1046A
  - X86 Lakemont
- Removed support for these SoC series:

  > - ARM Musca-A
- Made these changes in other SoC series:

  - Added Cypress PSoC-6 pinctrl support.
  - STM32 L4/L5/WB series were updated for better power management support (CONFIG\_PM=y).
  - Backup SRAM added on a selection of STM32 series (F2/F4/F7/H7)
  - Set TRACE\_MODE to asynchronous and enable trace output pin on STM32 SoCs
- Changes for ARC boards:

  - Added nSIM and QEMU simulation boards (nsim\_hs6x and qemu\_arc\_hs6x)
    with ARCv3 64bit HS6x processors
  - Enabled MPU on qemu\_arc\_hs and qemu\_arc\_em boards
  - Added cy8c95xx GPIO expander support to HSDK board
- Added support for these ARM boards:

  > - Actinius Icarus
  > - Actinius Icarus SoM
  > - Laird Connectivity BL654 Sensor Board
  > - Laird Connectivity Sentrius BT6x0 Sensor
  > - EFR32 Radio BRD4255A Board
  > - MPS3-AN547
  > - RAK4631
  > - Renesas R-Car H3ULCB
  > - Ronoth LoDev (based on AcSIP S76S / STM32L073)
  > - nRF9160 Thing Plus
  > - ST Nucleo F030R8
  > - ST Nucleo G0B1RE
  > - ST Nucleo H753ZI
  > - ST Nucleo L412RP-P
  > - ST Nucleo WL55JC
  > - ST STM32G071B Discovery
  > - Thingy:53
  > - u-blox EVK-BMD-30/35: BMD-300-EVAL, BMD-301-EVAL, and BMD-350-EVAL
  > - u-blox EVK-BMD-330: BMD-330-EVAL
  > - u-blox EVK-BMD-34/38: BMD-340-EVAL and BMD-341-EVAL
  > - u-blox EVK-BMD-34/38: BMD-345-EVAL
  > - u-blox EVK-BMD-360: BMD-360-EVAL
  > - u-blox EVK-BMD-34/48: BMD-380-EVAL
  > - u-blox EVK-ANNA-B11x
  > - u-blox EVK NINA-B11x
  > - u-blox EVK-NINA-B3
  > - u-blox EVK NINA-B40x
- Added support for these ARM64 boards:

  > - fvp\_base\_revc\_2xaemv8a
  > - fvp\_baser\_aemv8r
  > - nxp\_ls1046ardb
- Removed support for these ARM boards:

  > - ARM V2M Musca-A
  > - Nordic nRF5340 PDK
- Removed support for these X86 boards:

  > - up\_squared\_32
  > - qemu\_x86\_coverage
  > - minnowboard
- Made these changes in other boards:

  - cy8ckit\_062\_ble: Refactored to configure by pinctrl.
  - cy8ckit\_062\_ble: Added support to SCB[uart] with interrupt.
  - cy8ckit\_062\_ble: Added support to SCB[spi].
  - cy8ckit\_062\_ble: Added board revision schema.
  - cy8ckit\_062\_wifi\_bt: Refactored to configure by pinctrl.
  - cy8ckit\_062\_wifi\_bt: Added support to SCB[uart] with interrupt.
  - lpcxpresso55s16: Board renamed from lpcxpresso55s16\_ns to
    lpcxpresso55s16 since the board does not have Trusted Firmware M
    (TF-M) support.
  - lpcxpresso55s28: Removed lpcxpresso55s28\_ns config since the board
    does not have Trusted Firmware M (TF-M) support.
  - mimxrt685\_evk: Added support for octal SPI flash storage, LittleFS, I2S, OS
    timer, and power management.
  - mimxrt1060\_evk: Added support for QSPI flash storage, LittleFS, and
    mcuboot.
  - mimxrt1064\_evk: Added support for mcuboot.
- Added support for these following shields:

  - FTDI VM800C Embedded Video Engine Board
  - Generic ST7735R Display Shield
  - NXP FRDM-STBC-AGM01
  - Semtech SX1272MB2DAS LoRa Shield

## Drivers and Sensors

- ADC

  - Added support on TI CC32xx.
  - Added support on ITE IT8xxx2.
  - Added support for DMA and HW triggers in the MCUX ADC16 driver.
  - Added ADC emulator.
  - Moved definitions of ADC acquisition time macros so that those macros can be used in dts files.
- Bluetooth

  - The Kconfig option `CONFIG_BT_CTLR_TO_HOST_UART_DEV_NAME` was removed.
    Use the [zephyr,bt-c2h-uart chosen node](../build/dts/api/api.md#devicetree-chosen-nodes)
    directly instead.
- CAN

  - A driver for CAN-FD based on the Bosch M\_CAN IP was added. The driver
    currently supports STM32G4 series MCUs. Additional support for Microchip
    SAM and NXP chips is in progress.
  - The CAN ISO-TP subsystem was enhanced to allow padding and fixed
    addressing.
- Clock Control

  - On STM32 series, system clock configuration has been moved from Kconfig to DTS.
    Usage of existing Kconfig dedicated symbols (CONFIG\_CLOCK\_STM32\_FOO) is now
    deprecated.
  - Added clock control driver for Renesas R-Car platform
- Console

  - Added `UART_CONSOLE_INPUT_EXPIRED` and `UART_CONSOLE_INPUT_EXPIRED_TIMEOUT`
    Kconfig options to notify the power management module that UART console is
    in use now and forbid it to enter low-power states.
- Counter

  > - Added support for ESP32 Counter
- DAC

  > - Added support for Microchip MCP4725
- Disk

  - Added SDMMC support on STM32L4+
- Display

  - Added support for ST7735R
- Disk

  - Moved disk drivers (`disk_access_*.c`) to `drivers/disk` and renamed
    according to their function.
  - Fixed CMD6 support in USDHC driver.
  - Fixed clock frequency switching after initialization in `sdmmc_spi.c` driver.
- DMA

  - Added support on STM32G0 and STM32H7
- EEPROM

  - Added support for EEPROM emulated in flash.
- ESPI

  - Added support for Microchip eSPI SAF
- Ethernet

  - Added simulated PTP clock to e1000 Ethernet controller. This allows simple PTP
    clock testing with Qemu.
  - Separated PTP clock from gPTP support in mcux and gmac drivers. This allows
    application to use PTP clock without enabling gPTP support.
  - Converted clock control to use DEVICE\_DT\_GET in mcux driver.
  - Changed to allow changing MAC address in gmac driver.
  - Driver for STM32H7 is now using specific memory layout to fit DMA constraints
    for RAM accesses.
- Flash

  - flash\_write\_protection\_set() has been deprecated and will be removed in
    Zephyr 2.8. Responsibility for write/erase protection management has been
    moved to the driver-specific implementation of the flash\_write() and
    flash\_erase() API calls. All in-tree flash drivers have been updated,
    and the protect implementation removed from their API tables.
    During the deprecation period user code invoking
    flash\_write\_protection\_set() will have no effect, but the flash\_write() and
    flash\_erase() driver shims will wrap their calls with calls to the protect
    implementation if it is present in the API table.
    Out-of-tree drivers must be updated before the wrapping in the shims is
    removed when the deprecation period ends.
  - Added QSPI support on STM32F7.
- GPIO

  - [`gpio_dt_spec`](../hardware/peripherals/gpio.md#c.gpio_dt_spec "gpio_dt_spec"): a new structure which makes it more convenient to
    access GPIO configuration in the [devicetree](../build/dts/index.md#dt-guide).
  - New macros for initializing `gpio_dt_spec` values:
    [`GPIO_DT_SPEC_GET_BY_IDX`](../hardware/peripherals/gpio.md#c.GPIO_DT_SPEC_GET_BY_IDX "GPIO_DT_SPEC_GET_BY_IDX"), [`GPIO_DT_SPEC_GET_BY_IDX_OR`](../hardware/peripherals/gpio.md#c.GPIO_DT_SPEC_GET_BY_IDX_OR "GPIO_DT_SPEC_GET_BY_IDX_OR"),
    [`GPIO_DT_SPEC_GET`](../hardware/peripherals/gpio.md#c.GPIO_DT_SPEC_GET "GPIO_DT_SPEC_GET"), [`GPIO_DT_SPEC_GET_OR`](../hardware/peripherals/gpio.md#c.GPIO_DT_SPEC_GET_OR "GPIO_DT_SPEC_GET_OR"),
    [`GPIO_DT_SPEC_INST_GET_BY_IDX`](../hardware/peripherals/gpio.md#c.GPIO_DT_SPEC_INST_GET_BY_IDX "GPIO_DT_SPEC_INST_GET_BY_IDX"),
    [`GPIO_DT_SPEC_INST_GET_BY_IDX_OR`](../hardware/peripherals/gpio.md#c.GPIO_DT_SPEC_INST_GET_BY_IDX_OR "GPIO_DT_SPEC_INST_GET_BY_IDX_OR"),
    [`GPIO_DT_SPEC_INST_GET`](../hardware/peripherals/gpio.md#c.GPIO_DT_SPEC_INST_GET "GPIO_DT_SPEC_INST_GET"), and [`GPIO_DT_SPEC_INST_GET_OR`](../hardware/peripherals/gpio.md#c.GPIO_DT_SPEC_INST_GET_OR "GPIO_DT_SPEC_INST_GET_OR")
  - New helper functions for using `gpio_dt_spec` values:
    [`gpio_pin_configure_dt()`](../hardware/peripherals/gpio.md#c.gpio_pin_configure_dt "gpio_pin_configure_dt"), [`gpio_pin_interrupt_configure_dt()`](../hardware/peripherals/gpio.md#c.gpio_pin_interrupt_configure_dt "gpio_pin_interrupt_configure_dt")
  - Remove support for `GPIO_INT_*` flags in [`gpio_pin_configure()`](../hardware/peripherals/gpio.md#c.gpio_pin_configure "gpio_pin_configure").
    The feature has been deprecated in the Zephyr 2.2 release. The interrupt
    flags are now accepted by [`gpio_pin_interrupt_configure()`](../hardware/peripherals/gpio.md#c.gpio_pin_interrupt_configure "gpio_pin_interrupt_configure")
    function only.
  - STM32 GPIO driver now supports clock gating using PM\_DEVICE and PM\_DEVICE\_RUNTIME
  - Added GPIO driver for Renesas R-Car platform
- Hardware Info

  - Added support on Silicon Labs Gecko SoCs
- I2C

  - Added support on STM32F2
- I2S

  - Added support for NXP LPC devices
- IEEE 802.15.4

  - Fixed various issues in IEEE 802.15.4 L2 driver.
  - nrf5:

    - Made HW Radio Capabilities runtime.
    - Enabled CSMA-CA on serialized host.
    - Changed driver to load EUI64 from UICR.
  - rf2xx:

    - Added support for tx mode direct.
    - Added support for tx mode CCA.
    - Added support to enable promiscuous mode.
    - Added support to enable pan coordinator mode.
- Interrupt Controller

  - Moved shared interrupt controller configuration to be based
    on devicetree.
- LED

  - Add support for LED GPIO
  - Added power management support for LED PWM
- LoRa

  - Added support for SX1272
- Modem

  - Converted wncm14a2a, quectel-bg9x, hl7800 and ublox-sara-r4 drivers to use
    new DT device macros.
  - Changed GSM modem to optionally do a factory reset when booting.
  - Added autostarting support to GSM modem.
  - Added wait for RDY instead of polling AT in BG9X.
  - Fixed PDP context management for BG9X.
  - Added TLS offload support to ublox-sara-r4.
  - Made reset pin optional in ublox-sara-r4.
  - Fixed potential buffer overrun in hl7800.
  - Fixed build errors on 64-bit platforms.
  - Added support for dialup modem in PPP driver.
- PWM

  - Added support on STM32F2 and STM32L1.
  - Added support on Silicon Labs Gecko SoCs.
- Sensor

  - Added support for STM32 internal (CPU) temperature sensor.
  - Refactored multiple ST sensor drivers to use gpio\_dt\_spec macros and common
    stmemc routines, support multiple instances, and configure ODR/range
    properties in device tree.
  - Added SBS 1.1 compliant fuel gauge driver.
  - Added MAX17262 fuel gauge driver.
  - Added BMP388 pressure sensor driver.
  - Added Atmel SAM QDEC driver.
  - Added TI FDC2X1X driver.
  - Added support for MPU9250 to existing MPU6050 6-axis motion tracking driver.
  - Refactored BME280 temperature/pressure sensor driver.
  - Added BMI270 IMU driver.
  - Added Nuvoton tachometer sensor driver.
  - Added MAX6675 cold-junction-compensated K-thermocouple to digital
    converter.
- Serial

  - Extended Cypress PSoC-6 SCB[uart] driver to support interrupts.
  - Added UART driver for Renesas R-Car platform
- SPI

  - Added Cypress PSoC-6 SCB[spi] driver.
  - Default SPI\_SCK configuration is now pull-down for all STM32 to minimize power
    consumption in stop mode.
- Timer

  - Added x86 APIC TSC\_DEADLINE driver.
  - Added support for NXP MCUX OS Timer.
  - Added support for Nuvoton NPCX system timer.
  - Added CMT driver for Renesas R-Car platform.
- USB

  - Added support on STM32H7
  - Added attached event delay to usb\_dc\_nrfx driver
- Watchdog

  - Added support for TI CC32xx watchdog.
- WiFi

  - Converted eswifi and esp drivers to new DT device macros
  - esp:

    - Fixed hostname configuration.
    - Removed POSIX API dependency.
    - Renamed offloading driver from esp to esp\_at.
    - Added esp32 wifi driver support.

## Networking

- CoAP:

  - Fixed coap\_find\_options() to return 0 when options are empty.
- DHCPv4:

  - Fixed DHCPv4 dependency to network event management options.
- DNS:

  - Added locking to DNS library prevent concurrent access.
  - Added 10ms delay when rescheduling query timeout handler in DNS. This allows
    applications to run and handle the timeout gracefully.
  - Added support for reconfiguring DNS resolver when DNS servers are changed.
    This is supported by DHCPv4 and PPP.
- HTTP:

  - Added support for storing numeric HTTP error code in client API.
- IPv4:

  - Added IGMPv2 support to IPv4.
  - Removed IPv4 multicast address check when selecting source address during TX.
- LwM2M:

  - Fixed query buffer size so that it is large enough to encode all query strings.
  - Added data validation callback.
  - Fixed Register/Update to use link\_format writer.
  - Added application/link-format content writer.
  - Removed .well-known/core handling.
  - Introduced attribute handling helper functions.
  - Removed obsolete LWM2M\_IPSO\_TIMESTAMP\_EXTENSIONS option.
  - Added IPSO Buzzer, Push Button, On/Off Switch, Accelerometer, Pressure Sensor,
    Humidity, Generic Sensor and Temperature object implementation to support
    object model in version 1.1
  - Unified reusable resources creation.
  - Added support for object versioning.
  - Changed to allow cancel-observe to match path.
  - Made pmin and pmax attributes optional.
  - Added API function to delete object instance.
  - Fixed Registration Update send on object creation.
  - Changed to only parse TLV from the first block.
  - Changed to trigger registration update only when registered.
- Misc:

  - Added UDP packet sending support to net-shell.
  - Fixed source network interface setting when sending and when there are
    multiple network interfaces.
  - Changed connection managed to ignore not used network interfaces.
  - Added locking to network interface API function calls.
  - Changed to allow application to disable IPv4 or IPv6 support for a network interface.
  - Added support for virtual network interfaces.
  - Added support for IPv4/v6 tunneling network interface.
  - Added net events notification for PPP dead and running states.
  - Added PPP LCP MRU option support.
  - Added PPP IPCP IP and DNS address peer options support.
  - Added support for network packet capturing and sending data to external system
    for analysis.
  - Enabled running without TX or RX threads. By default, one RX thread and
    no TX thread is created. If userspace support is enabled, then one RX and one
    TX thread are created. This improves the network transmit latency when a
    packet is sent from application.
  - Changed to push highest priority net\_pkt directly to driver when sending and if
    there is at least one TX thread.
  - Changed to use k\_fifo instead of k\_work in RX and TX processing. This prevents
    k\_work from accessing already freed net\_pkt struct. This also improves the latency
    of network packets when the data is passed between different network threads.
  - Changed to check network interface status when sending and return ENETDOWN to the
    application if data cannot be sent.
  - Fixed echo-server sample application and set netmask properly when VLAN is
    enabled.
- OpenThread:

  - Added microseconds timer API support.
  - Changed to switch radio off when stopping diagnostics.
  - Enabled CSL delayed transmissions.
  - Added CSL transmitter and receiver API support.
  - Changed to init NCP after USB communication is established.
  - Aligned with the new NCP API.
  - Aligned with the new CLI API.
  - Introduced new OpenThread options.
  - Added Link Metrics API support.
  - Selected ECDSA when SRP is enabled.
  - Made child related options only visible on FTD.
  - Changed OT shell not to execute OT commands when shell is not ready.
- Socket:

  - Added SO\_PROTOCOL and SO\_TYPE get socket option.
  - Added MSG\_WAITALL receive socket option flag.
  - Added MSG\_TRUNC socket option flag.
  - Added support for close method for packet sockets.
  - Added locking to socket API function calls.
  - Added support for SO\_BINDTODEVICE socket option.
  - Added support for SO\_SNDTIMEO socket option.
  - Made NET\_SOCKETS\_POSIX\_NAMES be on by default. This allows application to use
    normal BSD socket API calls without adding the zsock prefix.
  - Added sample application to use SO\_TXTIME socket option.
- TCP:

  - Implemented ISN calculation according to RFC6528 in TCP. This is optional and
    enabled by default, and can be disabled if needed.
  - Removed legacy TCP stack support.
  - Changed TCP to use private work queue in order not to block system work queue.
- TLS:

  - Fixed userspace access to TLS socket.
  - Added socket option support for setting and getting DTLS handshake timeout.

## USB

- Reworked USB classes configuration. Various minor fixes in USB DFU class.
- USB HID class

  - Removed get\_protocol/set\_protocol from USB HID class API.
  - Allowed boot interface Protocol Code to be set per device.
  - Rework idle report implementation.
- Samples

  - Allowed to build USB Audio sampe for different platforms.
  - Added SD card support to USB MSC sample.
  - Reworked USB HID sample.

## Build and Infrastructure

- Improved support for additional toolchains:
  \* Support for the Intel oneApi toolchain.
- Devicetree

  - [`DT_COMPAT_GET_ANY_STATUS_OKAY`](../build/dts/api/api.md#c.DT_COMPAT_GET_ANY_STATUS_OKAY "DT_COMPAT_GET_ANY_STATUS_OKAY"): new macro
  - the `96b-lscon-3v3` and `96b-lscon-1v8` [compatible properties](../build/dts/intro-syntax-structure.md#dt-important-props) now have `linaro,` vendor prefixes, i.e. they are
    now respectively [`linaro,96b-lscon-3v3`](../build/dts/api/bindings/gpio/linaro%2C96b-lscon-3v3.md#std-dtcompatible-linaro-96b-lscon-3v3) and
    [`linaro,96b-lscon-1v8`](../build/dts/api/bindings/gpio/linaro%2C96b-lscon-1v8.md#std-dtcompatible-linaro-96b-lscon-1v8).

    This change was made to bring Zephyr’s devicetrees into compliance with an
    upstream Linux regular expression used to validate compatible properties.
    This regular expression requires a letter as the first character.
- West (extensions)

  - This section only covers west [Extensions](../develop/west/extensions.md#west-extensions) maintained in the
    zephyr repository. For release notes on west’s built-in features, see
    [West Release Notes](../develop/west/release-notes.md#west-release-notes).
  - Changes to the runners backends used for [flashing and debugging
    commands](../develop/west/build-flash-debug.md#west-build-flash-debug):

    - bossac runner: added legacy mode option into extended SAM-BA
      bootloader selection. This extends compatibility between Zephyr and
      some Arduino IDE bootloaders.
    - jlink runner: Zephyr thread awareness is now available in GDB by default
      for application builds with [`CONFIG_DEBUG_THREAD_INFO`](../kconfig.md#CONFIG_DEBUG_THREAD_INFO "CONFIG_DEBUG_THREAD_INFO") set to `y`
      in [Configuration System (Kconfig)](../build/kconfig/index.md#kconfig). This applies to `west debug`, `west debugserver`,
      and `west attach`. JLink version 7.11b or later must be installed on the
      host system, with JLink 7.20 or later strongly recommended.
    - jlink runner: default `west flash` output is less verbose. The old
      behavior is still available when run as `west --verbose flash`.
    - jlink runner: when flashing, this runner now prefers a `.hex` file
      generated by the build system to a `.bin`. Unlike `.bin`, the HEX
      format includes information on the image’s address range in flash, so
      this works better when flashing Zephyr images linked for locations other
      than the target’s boot address, e.g. images meant to be run by
      bootloaders. The `.bin` file is still used as a fallback if a HEX File
      is not present.
    - openocd runner: support for `west debug` and `west attach` has been
      fixed. Previously with this runner, `west debug` behaved like `west
      attach` should, and `west attach` behaved like `west debugserver`
      should.
    - pyocd runner: board-specific pyOCD configuration files in YAML can now be
      placed in `support/pyocd.yaml` inside the board directory. See
      [boards/arm/reel\_board/support/pyocd.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/reel_board/support/pyocd.yaml) for an example,
      and the pyOCD documentation for details on its configuration format.
  - `west spdx`: new command which can be used to generate SPDX software
    bills of materials for a Zephyr application build. See [Software bill of materials: west spdx](../develop/west/zephyr-cmds.md#west-spdx).

## Libraries / Subsystems

- Disk

  - Disk drivers (`disk_access_*.c`) are moved to `drivers/disk` and renamed
    according to their function. Driver’s Kconfig options are revised and renamed.
    SDMMC host controller drivers are selected when the corresponding node
    in devicetree is enabled. Following application relevant Kconfig options
    are renamed: `CONFIG_DISK_ACCESS_RAM` -> CONFIG\_DISK\_DRIVER\_RAM,
    `CONFIG_DISK_ACCESS_FLASH` -> CONFIG\_DISK\_DRIVER\_FLASH,
    `CONFIG_DISK_ACCESS_SDHC` -> CONFIG\_DISK\_DRIVER\_SDMMC.
- Management

  - MCUmgr

    - Fixed an issue with the file system management failing to
      open files due to missing initializations of [`fs_file_t`](../services/file_system/index.md#c.fs_file_t "fs_file_t")
      structures.
    - Fixed an issue where multiple SMP commands sent one after the other would
      corrupt CBOR payload.
    - Fixed problem where mcumgr over shell would stall and wait for
      retransmissions of frames.
- CMSIS subsystem

  - Moved CMSIS portability layer headers to include/portability/cmsis\_os.h
    and include/portability/cmsis\_os2.h
- Power management

  - `device_pm_control_nop` has been removed in favor of `NULL` when device
    PM is not supported by a device. In order to make transition easier for
    out-of-tree users a macro with the same name is provided as an alias to
    `NULL`. The macro is flagged as deprecated to make users aware of the
    change.
  - Devices set as busy are no longer suspended by the system power management.
  - The time necessary to exit a sleep state and return to the active state was
    added in `zephyr,power-state` binding and accounted when the system
    changes to a power state.
  - Device runtime power management (PM), former IDLE runtime, was
    completely overhauled.

    - Multiple threads can wait an operation (`pm_device_get_async` and
      `pm_device_put_async`) to finish.
    - A new API `pm_device_wait` was added so that drivers can easily
      wait for an async request to finish.
    - The API can be used in [pre-kernel](../develop/api/terminology.md#api-term-pre-kernel-ok) stages.
    - Several concurrence issues related with atomics access and the usage
      of the polling API have been fixed. Condition variables are now used to
      handle notification.
- Logging

  - Introduced logging v2 which allows logging any variable types (including
    floating point variables). New version does not require transient string
    duplication (`log_strdup()`). Legacy mode remains and is still the default
    but user API is not changed and modes are interchangeable.
    `CONFIG_LOG2_MODE_DEFERRED` or `CONFIG_LOG2_MODE_IMMEDIATE` enable
    logging v2. Logging backend API is extended to support v2 and the most
    popular backends (UART, shell) are updated.
- Shell

  - Added `CONFIG_SHELL_BACKEND_DUMMY_BUF_SIZE` option that allows to set
    size of the dummy backend buffer; changing this parameter allows to work
    around issue, where output from command, shell that is gathered by the dummy
    backend, gets cut to the size of buffer.
- Storage

  - Added persistent write progress to stream\_flash.
- Task Watchdog

  - This new subsystem was added with this release and allows supervision of
    individual threads. It is based on a regularly updated kernel timer,
    whose ISR is never actually called in regular system operation.

    An existing hardware watchdog can be used as an optional fallback if the
    task watchdog itself gets stuck.
- Tracing

  - `CONFIG_TRACING_CPU_STATS` was removed in favor of
    `CONFIG_THREAD_RUNTIME_STATS` which provides per thread statistics. The
    same functionality is also available when Thread analyzer is enabled with
    the runtime statistics enabled.
  - Expanded and overhauled tracing hooks with more coverage and support for
    tracing all kernel objects and basic power management operations.
  - Added support for Percepio Tracealyzer, a commercial tracing tool which now
    has built-in support for Zephyr. We now have the Percepio tracerecorder
    integrated as a module.
  - Expanded support for the new hooks in SEGGER Systemview and enhanced the
    description file with support for all APIs.
- Debug
  \* SEGGER Systemview and RTT SDK updated to version v3.30
- OS

  - Reboot functionality has been moved to `subsys/os` from `subsys/power`.
    A consequence of this movement is that the `<power/reboot.h>` header has
    been moved to `<sys/reboot.h>`. `<power/reboot.h>` is still provided
    for compatibility, but it will produce a warning to inform users of the
    relocation.

## HALs

- HALs are now moved out of the main tree as external modules and reside in
  their own standalone repositories.

## Trusted Firmware-m

- Synchronized Trusted-Firmware-M module to the upstream v1.3.0 release.
- Configured QEMU to run Zephyr samples and tests in CI on mps2\_an521\_nonsecure
  (Cortex-M33 Non-Secure) with TF-M as the secure firmware component.
- Added Kconfig options for selecting the desired TF-M profile and build type
- Added Kconfig options for enabling the desired TF-M secure partitions
- Added a new sample to run the PSA tests with Zephyr
- Added a new sample to run the TF-M regression tests using the Zephyr build system
- Added support for new platforms

  > - BL5340 DVK
  > - STM32L562E DK
- NOTE: Trusted-Firmware-M can not currently be used with mbedtls 2.26.0 when
  PSA APIs are enabled in mbedtls (`MBEDTLS_USE_PSA_CRYPTO` and
  `MBEDTLS_PSA_CRYPTO_C`). If both TF-M and mbedtls are required, mbedtls
  must be used without the PSA APIs. This will be resolved in a future
  update to mbedtls.

## Documentation

- Documentation look and feel has been improved by using a new stylesheet.
- Doxygen is now run by Sphinx using the `doxyrunner` custom extension. The
  new extension centralizes multiple scattered workarounds that existed before
  in a single place.
- Doxygen now runs with `WARN_AS_ERROR` enabled.
- Documentation known warnings are now filtered using a custom Sphinx extension:
  `warnings_filter`. This extension removes the need of post-processing
  the Sphinx output and allows to use the `-W` option (treat warnings as
  errors) which has been enabled by default.
- External content, e.g. samples and boards documentation is now handled by
  the `external_content` extension.
- Sphinx is now run in parallel mode by default (`-j auto`).
- The documentation helper `Makefile` has been moved from the repository root
  to the `doc` folder.

## Tests and Samples

- Twister’s `dt_compat_enabled_with_alias()` test case filter was deprecated
  in favor of a new `dt_enabled_alias_with_parent_compat()` filter. The old
  filter is still supported, but it may be removed in a future release.

  To update, replace uses like this:

  ```yaml
  filter: dt_compat_enabled_with_alias("gpio-leds", "led0")
  ```

  with:

  ```yaml
  filter: dt_enabled_alias_with_parent_compat("led0", "gpio-leds")
  ```
- Add a feature which handles pytest script in twister and provide an example.
- Provide test execution time per ztest testcase.
- Added and refined some testcases, most of them are negative testcases, to
  improve the test code coverage:

  > - Testcases of x86’s regular/direct interrupts and offload job from ISR.
  > - Testcases of SMP, and enabled SMP for existed testing of semaphore, condvar, etc.
  > - Testcases of memory protection, userspace and memory heap.
  > - Testcases of data structure include stack, queue, ringbuffer and rbtree.
  > - Testcases of IPC include pipe, poll, mailbox, message queue.
  > - Testcases of synchronization include mutex, semaphore, atomic operations.
  > - Testcases of scheduling and thread.
  > - Testcases of testing for arch\_nop() and errno.
  > - Testcases of libc and posix API.
  > - Testcases of log and sensor subsystem.

## Issue Related Items

These GitHub issues were addressed since the previous 2.5.0 tagged
release:

- [GitHub #35962](https://github.com/zephyrproject-rtos/zephyr/issues/35962) - drivers using deprecated Kconfigs
- [GitHub #35955](https://github.com/zephyrproject-rtos/zephyr/issues/35955) - Bluetooth: Controller: Regression in connection setup
- [GitHub #35949](https://github.com/zephyrproject-rtos/zephyr/issues/35949) - can: mcan: sjw-data devicetree configuration is not written correctly
- [GitHub #35941](https://github.com/zephyrproject-rtos/zephyr/issues/35941) - subsys: tracing: sysview: No SEGGER\_SYSVIEW.h in path
- [GitHub #35926](https://github.com/zephyrproject-rtos/zephyr/issues/35926) - Shell tab-completion with more than two levels of nested dynamic commands fails
- [GitHub #35924](https://github.com/zephyrproject-rtos/zephyr/issues/35924) - Help with Configuring Custom GPIO Pins
- [GitHub #35916](https://github.com/zephyrproject-rtos/zephyr/issues/35916) - drivers: TI cc13xx\_cc26xx: build error when PM is enabled (serial, entropy, spi, i2c modules)
- [GitHub #35911](https://github.com/zephyrproject-rtos/zephyr/issues/35911) - shield sample sensorhub does not produce and meaningful data
- [GitHub #35910](https://github.com/zephyrproject-rtos/zephyr/issues/35910) - LIS2MDL reporting wrong temperature
- [GitHub #35896](https://github.com/zephyrproject-rtos/zephyr/issues/35896) - frdm\_k64f: build failure missing dt-bindings/clock/kinetis\_sim.h: No such file or directory
- [GitHub #35890](https://github.com/zephyrproject-rtos/zephyr/issues/35890) - Build system ignores explicit ZephyrBuildConfiguration\_ROOT variable
- [GitHub #35882](https://github.com/zephyrproject-rtos/zephyr/issues/35882) - Fixed width documentation makes DT bindings docs unreadable
- [GitHub #35876](https://github.com/zephyrproject-rtos/zephyr/issues/35876) - Bluetooth: host: CCC store not correctly handled for multiple connections
- [GitHub #35871](https://github.com/zephyrproject-rtos/zephyr/issues/35871) - LPS22HH sensor reporting wrong pressure data
- [GitHub #35840](https://github.com/zephyrproject-rtos/zephyr/issues/35840) - Bluetooth: host: L2CAP enhanced connection request conformance test issues
- [GitHub #35838](https://github.com/zephyrproject-rtos/zephyr/issues/35838) - Bluetooth: ISO: BIG termination doesn’t fully unref the connection
- [GitHub #35826](https://github.com/zephyrproject-rtos/zephyr/issues/35826) - LORAWAN Compatibility with nrf52832 and sx1262
- [GitHub #35813](https://github.com/zephyrproject-rtos/zephyr/issues/35813) - Zephyr Native Posix Build Uses Linux Build Machine Headers out of Sandbox
- [GitHub #35812](https://github.com/zephyrproject-rtos/zephyr/issues/35812) - ESP32 Factory app partition is not bootable
- [GitHub #35781](https://github.com/zephyrproject-rtos/zephyr/issues/35781) - Missing response parameter for HCI\_LE\_Set\_Connectionless\_IQ\_Sampling\_Enable HCI command
- [GitHub #35772](https://github.com/zephyrproject-rtos/zephyr/issues/35772) - Support C++ exceptions on NIOS2
- [GitHub #35764](https://github.com/zephyrproject-rtos/zephyr/issues/35764) - tests: kernel: threads: no multithreading: fails with CONFIG\_STACK\_SENTINEL=y
- [GitHub #35762](https://github.com/zephyrproject-rtos/zephyr/issues/35762) - SAMPLES: shell\_module gives no console output on qemu\_leon3
- [GitHub #35756](https://github.com/zephyrproject-rtos/zephyr/issues/35756) - ESP32 Ethernet Support
- [GitHub #35737](https://github.com/zephyrproject-rtos/zephyr/issues/35737) - drivers: can: mcan: sjw not initialized when CAN\_FD\_MODE is enabled
- [GitHub #35714](https://github.com/zephyrproject-rtos/zephyr/issues/35714) - samples: subsys: testusb: I want to know how to test in window10.
- [GitHub #35713](https://github.com/zephyrproject-rtos/zephyr/issues/35713) - tests: kernel.scheduler.multiq: test\_k\_thread\_suspend\_init\_null failure
- [GitHub #35694](https://github.com/zephyrproject-rtos/zephyr/issues/35694) - No console output from NIOS2 Max10
- [GitHub #35693](https://github.com/zephyrproject-rtos/zephyr/issues/35693) - gpio\_mcux\_lpc.c uses devicetree instance numbers incorrectly
- [GitHub #35686](https://github.com/zephyrproject-rtos/zephyr/issues/35686) - Bluetooth: Crash in bt\_gatt\_dm\_attr\_chrc\_val when BLE device is disconnected during discovery process
- [GitHub #35681](https://github.com/zephyrproject-rtos/zephyr/issues/35681) - Unable to get ouput for samples/subsys/logging/logger and samples/philosophers
- [GitHub #35677](https://github.com/zephyrproject-rtos/zephyr/issues/35677) - samples/subsys/console/getchar and samples/subsys/console/getline build breaks for arduino\_nano\_33\_ble
- [GitHub #35655](https://github.com/zephyrproject-rtos/zephyr/issues/35655) - Arm64: Assertion failed when CONFIG\_MP\_CPUS >= 3.
- [GitHub #35653](https://github.com/zephyrproject-rtos/zephyr/issues/35653) - ARC MWDT toolchain put \_\_start and \_\_reset at different address
- [GitHub #35633](https://github.com/zephyrproject-rtos/zephyr/issues/35633) - Out of bound read: Multiple Coverity sightings in generated code
- [GitHub #35631](https://github.com/zephyrproject-rtos/zephyr/issues/35631) - [Coverity CID: 205610] Out-of-bounds read in /zephyr/include/generated/syscalls/kernel.h (Generated Code)
- [GitHub #35630](https://github.com/zephyrproject-rtos/zephyr/issues/35630) - [Coverity CID: 205657] Out-of-bounds read in /zephyr/include/generated/syscalls/sample\_driver.h (Generated Code)
- [GitHub #35629](https://github.com/zephyrproject-rtos/zephyr/issues/35629) - [Coverity CID: 207968] Out-of-bounds read in /zephyr/include/generated/syscalls/counter.h (Generated Code)
- [GitHub #35628](https://github.com/zephyrproject-rtos/zephyr/issues/35628) - [Coverity CID: 207976] Out-of-bounds read in /zephyr/include/generated/syscalls/counter.h (Generated Code)
- [GitHub #35627](https://github.com/zephyrproject-rtos/zephyr/issues/35627) - [Coverity CID: 208195] Out-of-bounds read in /zephyr/include/generated/syscalls/gpio.h (Generated Code)
- [GitHub #35626](https://github.com/zephyrproject-rtos/zephyr/issues/35626) - [Coverity CID: 210588] Out-of-bounds read in /zephyr/include/generated/syscalls/dac.h (Generated Code)
- [GitHub #35625](https://github.com/zephyrproject-rtos/zephyr/issues/35625) - [Coverity CID: 211042] Out-of-bounds read in /zephyr/include/generated/syscalls/socket.h (Generated Code)
- [GitHub #35624](https://github.com/zephyrproject-rtos/zephyr/issues/35624) - [Coverity CID: 214226] Out-of-bounds read in /zephyr/include/generated/syscalls/uart.h (Generated Code)
- [GitHub #35623](https://github.com/zephyrproject-rtos/zephyr/issues/35623) - [Coverity CID: 215223] Out-of-bounds read in /zephyr/include/generated/syscalls/net\_ip.h (Generated Code)
- [GitHub #35622](https://github.com/zephyrproject-rtos/zephyr/issues/35622) - [Coverity CID: 215238] Out-of-bounds read in /zephyr/include/generated/syscalls/net\_ip.h (Generated Code)
- [GitHub #35621](https://github.com/zephyrproject-rtos/zephyr/issues/35621) - [Coverity CID: 219477] Out-of-bounds read in /zephyr/include/generated/syscalls/pwm.h (Generated Code)
- [GitHub #35620](https://github.com/zephyrproject-rtos/zephyr/issues/35620) - [Coverity CID: 219482] Out-of-bounds read in /zephyr/include/generated/syscalls/pwm.h (Generated Code)
- [GitHub #35619](https://github.com/zephyrproject-rtos/zephyr/issues/35619) - [Coverity CID: 219496] Out-of-bounds read in /zephyr/include/generated/syscalls/ztest\_error\_hook.h (Generated Code)
- [GitHub #35618](https://github.com/zephyrproject-rtos/zephyr/issues/35618) - [Coverity CID: 219506] Out-of-bounds read in /zephyr/include/generated/syscalls/log\_ctrl.h (Generated Code)
- [GitHub #35617](https://github.com/zephyrproject-rtos/zephyr/issues/35617) - [Coverity CID: 219568] Out-of-bounds read in /zephyr/include/generated/syscalls/net\_if.h (Generated Code)
- [GitHub #35616](https://github.com/zephyrproject-rtos/zephyr/issues/35616) - [Coverity CID: 219586] Out-of-bounds read in /zephyr/include/generated/syscalls/net\_if.h (Generated Code)
- [GitHub #35615](https://github.com/zephyrproject-rtos/zephyr/issues/35615) - [Coverity CID: 219648] Uninitialized scalar variable in /zephyr/include/generated/syscalls/test\_syscalls.h (Generated Code)
- [GitHub #35614](https://github.com/zephyrproject-rtos/zephyr/issues/35614) - [Coverity CID: 219725] Out-of-bounds read in /zephyr/include/generated/syscalls/kernel.h (Generated Code)
- [GitHub #35613](https://github.com/zephyrproject-rtos/zephyr/issues/35613) - [Coverity CID: 225900] Out-of-bounds access in tests/net/lib/dns\_addremove/src/main.c
- [GitHub #35612](https://github.com/zephyrproject-rtos/zephyr/issues/35612) - [Coverity CID: 229325] Out-of-bounds read in /zephyr/include/generated/syscalls/log\_msg2.h (Generated Code)
- [GitHub #35611](https://github.com/zephyrproject-rtos/zephyr/issues/35611) - [Coverity CID: 230223] Out-of-bounds read in /zephyr/include/generated/syscalls/log\_msg2.h (Generated Code)
- [GitHub #35610](https://github.com/zephyrproject-rtos/zephyr/issues/35610) - [Coverity CID: 232755] Out-of-bounds read in /zephyr/include/generated/syscalls/log\_ctrl.h (Generated Code)
- [GitHub #35609](https://github.com/zephyrproject-rtos/zephyr/issues/35609) - [Coverity CID: 235917] Out-of-bounds read in /zephyr/include/generated/syscalls/log\_msg2.h (Generated Code)
- [GitHub #35608](https://github.com/zephyrproject-rtos/zephyr/issues/35608) - [Coverity CID: 235923] Out-of-bounds read in /zephyr/include/generated/syscalls/log\_msg2.h (Generated Code)
- [GitHub #35607](https://github.com/zephyrproject-rtos/zephyr/issues/35607) - [Coverity CID: 235933] Out-of-bounds read in /zephyr/include/generated/syscalls/gpio.h (Generated Code)
- [GitHub #35606](https://github.com/zephyrproject-rtos/zephyr/issues/35606) - [Coverity CID: 235951] Out-of-bounds read in /zephyr/include/generated/syscalls/log\_ctrl.h (Generated Code)
- [GitHub #35605](https://github.com/zephyrproject-rtos/zephyr/issues/35605) - [Coverity CID: 236005] Out-of-bounds read in /zephyr/include/generated/syscalls/log\_ctrl.h (Generated Code)
- [GitHub #35604](https://github.com/zephyrproject-rtos/zephyr/issues/35604) - [Coverity CID: 236129] Unused value in drivers/adc/adc\_lmp90xxx.c
- [GitHub #35603](https://github.com/zephyrproject-rtos/zephyr/issues/35603) - [Coverity CID: 236130] Wrong sizeof argument in drivers/adc/adc\_lmp90xxx.c
- [GitHub #35596](https://github.com/zephyrproject-rtos/zephyr/issues/35596) - Bluetooth: Cannot connect if extended advertising is enabled in `prj.conf`
- [GitHub #35586](https://github.com/zephyrproject-rtos/zephyr/issues/35586) - Timer based example on docu using nrf52-dk compile error.
- [GitHub #35580](https://github.com/zephyrproject-rtos/zephyr/issues/35580) - Fault when logging
- [GitHub #35569](https://github.com/zephyrproject-rtos/zephyr/issues/35569) - tests/lib/mem\_alloc failed with arcmwdt toolchain
- [GitHub #35567](https://github.com/zephyrproject-rtos/zephyr/issues/35567) - some mwdt compiler options can’t be recognized by zephyr\_cc\_option
- [GitHub #35561](https://github.com/zephyrproject-rtos/zephyr/issues/35561) - Issue with fat\_fs example on nucleo\_f767zi
- [GitHub #35553](https://github.com/zephyrproject-rtos/zephyr/issues/35553) - all menuconfig interfaces contain sound open firmware/SOF text
- [GitHub #35543](https://github.com/zephyrproject-rtos/zephyr/issues/35543) - samples: subsys: display: lvgl: is run on nucleo\_f429zi and nucleo\_f746zg but should be skipped
- [GitHub #35541](https://github.com/zephyrproject-rtos/zephyr/issues/35541) - sockets\_tls: when using dtls with sara-r4 modem, handshake hangs if no reply
- [GitHub #35540](https://github.com/zephyrproject-rtos/zephyr/issues/35540) - tests: ztest: error\_hook: fails on nucleo\_g071rb and nucleo\_l073rz
- [GitHub #35539](https://github.com/zephyrproject-rtos/zephyr/issues/35539) - tests: drivers: spi: spi\_loopback: test failed since #34731 is merged
- [GitHub #35524](https://github.com/zephyrproject-rtos/zephyr/issues/35524) - tests: samples: led: LED PWM sample fails on nrf platforms
- [GitHub #35522](https://github.com/zephyrproject-rtos/zephyr/issues/35522) - doc: Current section is not shown in the side pane nor the page top cookie
- [GitHub #35512](https://github.com/zephyrproject-rtos/zephyr/issues/35512) - OpenThread can’t find TRNG driver on nRF5340
- [GitHub #35509](https://github.com/zephyrproject-rtos/zephyr/issues/35509) - tests: timer: Unstable tests using timer at nrf platforms
- [GitHub #35489](https://github.com/zephyrproject-rtos/zephyr/issues/35489) - samples: net: gsm\_modem: build fails if CONFIG\_GSM\_MUX=y
- [GitHub #35480](https://github.com/zephyrproject-rtos/zephyr/issues/35480) - pm: device\_runtime: `pm_device_request` can block forever
- [GitHub #35479](https://github.com/zephyrproject-rtos/zephyr/issues/35479) - address is not a known kernel object exception with arcmwdt toolchain
- [GitHub #35476](https://github.com/zephyrproject-rtos/zephyr/issues/35476) - bluetooth: controller assertion when scanning with multiple active connections
- [GitHub #35474](https://github.com/zephyrproject-rtos/zephyr/issues/35474) - The dma-stm32 driver don’t build for STM32F0 MCUs
- [GitHub #35444](https://github.com/zephyrproject-rtos/zephyr/issues/35444) - drivers: sensor: sbs-gauge: The sbs-gauge cannot be read from sensor shell
- [GitHub #35401](https://github.com/zephyrproject-rtos/zephyr/issues/35401) - Enabling POSIX\_API leads to SSL handshake error
- [GitHub #35395](https://github.com/zephyrproject-rtos/zephyr/issues/35395) - STM32F4: Infinite reboot loop due to Ethernet initialization
- [GitHub #35390](https://github.com/zephyrproject-rtos/zephyr/issues/35390) - net.socket.tls.tls\_ext: frdm\_k64f test failure
- [GitHub #35383](https://github.com/zephyrproject-rtos/zephyr/issues/35383) - Can’t setup ISO Broadcast Demo on nrf53dk
- [GitHub #35380](https://github.com/zephyrproject-rtos/zephyr/issues/35380) - sys: timeutil: inconsistent types for local times
- [GitHub #35363](https://github.com/zephyrproject-rtos/zephyr/issues/35363) - bt\_gatt\_discover() retunrs incorrect handle (offset by -1)
- [GitHub #35360](https://github.com/zephyrproject-rtos/zephyr/issues/35360) - Power consumption nRF52
- [GitHub #35352](https://github.com/zephyrproject-rtos/zephyr/issues/35352) - [Coverity CID: 215376] Out-of-bounds access in drivers/sensor/lis2dh/lis2dh\_trigger.c
- [GitHub #35351](https://github.com/zephyrproject-rtos/zephyr/issues/35351) - [Coverity CID: 219472] Unrecoverable parse warning in tests/kernel/mem\_protect/mem\_protect/src/mem\_domain.c
- [GitHub #35350](https://github.com/zephyrproject-rtos/zephyr/issues/35350) - [Coverity CID: 236055] Out-of-bounds access in subsys/modbus/modbus\_core.c
- [GitHub #35349](https://github.com/zephyrproject-rtos/zephyr/issues/35349) - [Coverity CID: 236057] Unrecoverable parse warning in tests/kernel/mem\_protect/mem\_protect/src/mem\_domain.c
- [GitHub #35348](https://github.com/zephyrproject-rtos/zephyr/issues/35348) - [Coverity CID: 236060] Out-of-bounds access in subsys/net/l2/ppp/ppp\_l2.c
- [GitHub #35347](https://github.com/zephyrproject-rtos/zephyr/issues/35347) - [Coverity CID: 236064] Dereference null return value in subsys/bluetooth/controller/ll\_sw/ull.c
- [GitHub #35346](https://github.com/zephyrproject-rtos/zephyr/issues/35346) - [Coverity CID: 236069] Out-of-bounds access in tests/lib/c\_lib/src/main.c
- [GitHub #35345](https://github.com/zephyrproject-rtos/zephyr/issues/35345) - [Coverity CID: 236074] Out-of-bounds access in tests/lib/c\_lib/src/main.c
- [GitHub #35344](https://github.com/zephyrproject-rtos/zephyr/issues/35344) - [Coverity CID: 236075] Out-of-bounds access in subsys/bluetooth/controller/hci/hci.c
- [GitHub #35343](https://github.com/zephyrproject-rtos/zephyr/issues/35343) - [Coverity CID: 236079] Untrusted divisor in subsys/bluetooth/controller/hci/hci.c
- [GitHub #35342](https://github.com/zephyrproject-rtos/zephyr/issues/35342) - [Coverity CID: 236085] Dereference after null check in samples/userspace/prod\_consumer/src/app\_a.c
- [GitHub #35341](https://github.com/zephyrproject-rtos/zephyr/issues/35341) - twister: Hardware map creation is buggy (+ inaccurate docs)
- [GitHub #35338](https://github.com/zephyrproject-rtos/zephyr/issues/35338) - USB: ethernet CDC ECM/EEM support is broken
- [GitHub #35336](https://github.com/zephyrproject-rtos/zephyr/issues/35336) - tests: samples: power: samples/subsys/pm/device\_pm/sample.power.ospm.dev\_idle\_pm fails on nrf52 platforms
- [GitHub #35329](https://github.com/zephyrproject-rtos/zephyr/issues/35329) - samples: gsm\_modem: Compilation failed, likely related to logging changes
- [GitHub #35327](https://github.com/zephyrproject-rtos/zephyr/issues/35327) - Sensor Code for CC3220sf
- [GitHub #35325](https://github.com/zephyrproject-rtos/zephyr/issues/35325) - Shell: Kernel: Reboot: echo is abruptly terminated
- [GitHub #35321](https://github.com/zephyrproject-rtos/zephyr/issues/35321) - Improve STM32: Serial Driver,Handle uart mode per instance
- [GitHub #35307](https://github.com/zephyrproject-rtos/zephyr/issues/35307) - ARM64 system calls are entered with interrupts masked
- [GitHub #35305](https://github.com/zephyrproject-rtos/zephyr/issues/35305) - Linking order when using both TF-M and Mbed TLS
- [GitHub #35299](https://github.com/zephyrproject-rtos/zephyr/issues/35299) - PM suspend IPC message sporadically not being delivered
- [GitHub #35297](https://github.com/zephyrproject-rtos/zephyr/issues/35297) - STM32 SPI - wrong behavior after PR 34731
- [GitHub #35286](https://github.com/zephyrproject-rtos/zephyr/issues/35286) - New logging breaks eclipse
- [GitHub #35278](https://github.com/zephyrproject-rtos/zephyr/issues/35278) - LittleFs Sample will not build for qemu\_riscv64 sample target
- [GitHub #35263](https://github.com/zephyrproject-rtos/zephyr/issues/35263) - device\_pm\_control\_nop is used in dac\_mcp4725.c
- [GitHub #35242](https://github.com/zephyrproject-rtos/zephyr/issues/35242) - intel\_adsp\_cavs15: run kernel common testcases failed on ADSP
- [GitHub #35241](https://github.com/zephyrproject-rtos/zephyr/issues/35241) - intel\_adsp\_cavs15: run interrupt testcases failed on ADSP
- [GitHub #35236](https://github.com/zephyrproject-rtos/zephyr/issues/35236) - tests: doc: Document generation process FAILS with valid module `samples:`
- [GitHub #35223](https://github.com/zephyrproject-rtos/zephyr/issues/35223) - Coverity [CID 221772]: Wrong operator used in logging subsystem, multiple violations
- [GitHub #35220](https://github.com/zephyrproject-rtos/zephyr/issues/35220) - tests: dma: memory-to-memory transfer fails on stm32f746zg nucleo board
- [GitHub #35219](https://github.com/zephyrproject-rtos/zephyr/issues/35219) - tests: driver: dma test case loop\_transfer fails on stm32 with dmamux
- [GitHub #35215](https://github.com/zephyrproject-rtos/zephyr/issues/35215) - tests/kernel/msgq/msgq\_usage failed on hsdk board
- [GitHub #35209](https://github.com/zephyrproject-rtos/zephyr/issues/35209) - tests/kernel/mem\_heap/mheap\_api\_concept failed on hsdk board
- [GitHub #35204](https://github.com/zephyrproject-rtos/zephyr/issues/35204) - PPI channel assignment for Bluetooth controller is incorrect for nRF52805
- [GitHub #35202](https://github.com/zephyrproject-rtos/zephyr/issues/35202) - smp atomic\_t global\_lock will never be cleared when a thread oops with global\_lock is set
- [GitHub #35200](https://github.com/zephyrproject-rtos/zephyr/issues/35200) - tests/kernel/smp failed on hsdk board
- [GitHub #35199](https://github.com/zephyrproject-rtos/zephyr/issues/35199) - Queues: there is no documentation about queue’s implementation.
- [GitHub #35198](https://github.com/zephyrproject-rtos/zephyr/issues/35198) - subsys.pm.device\_pm: frdm\_k64f leave idel fails
- [GitHub #35197](https://github.com/zephyrproject-rtos/zephyr/issues/35197) - Zephyr Project Development with 2 Ethernet Interfaces Supported (eth0, and eth1)
- [GitHub #35195](https://github.com/zephyrproject-rtos/zephyr/issues/35195) - doc, coding guidelines: broken CERT-C links
- [GitHub #35191](https://github.com/zephyrproject-rtos/zephyr/issues/35191) - GIT Checkout of Master Branch is 2.6.0rc1 versus west update as 2.5.99
- [GitHub #35189](https://github.com/zephyrproject-rtos/zephyr/issues/35189) - Coding Guidelines: Resolve the issues under Rule 21.2
- [GitHub #35187](https://github.com/zephyrproject-rtos/zephyr/issues/35187) - Version selection not working
- [GitHub #35176](https://github.com/zephyrproject-rtos/zephyr/issues/35176) - strtol crashes
- [GitHub #35175](https://github.com/zephyrproject-rtos/zephyr/issues/35175) - quectel-bg9x crashes in modem\_rssi\_query\_work
- [GitHub #35169](https://github.com/zephyrproject-rtos/zephyr/issues/35169) - esp32: uart\_poll\_in never ready for UART2 only
- [GitHub #35163](https://github.com/zephyrproject-rtos/zephyr/issues/35163) - [Coverity CID: 236009] Wrong sizeof argument in tests/lib/cbprintf\_package/src/test.inc
- [GitHub #35162](https://github.com/zephyrproject-rtos/zephyr/issues/35162) - [Coverity CID: 235972] Wrong sizeof argument in tests/lib/cbprintf\_package/src/test.inc
- [GitHub #35161](https://github.com/zephyrproject-rtos/zephyr/issues/35161) - [Coverity CID: 235962] Unused value in tests/kernel/mem\_protect/mem\_map/src/main.c
- [GitHub #35160](https://github.com/zephyrproject-rtos/zephyr/issues/35160) - [Coverity CID: 235930] Unused value in kernel/mmu.c
- [GitHub #35159](https://github.com/zephyrproject-rtos/zephyr/issues/35159) - [Coverity CID: 232698] Uninitialized scalar variable in samples/net/sockets/txtime/src/main.c
- [GitHub #35158](https://github.com/zephyrproject-rtos/zephyr/issues/35158) - [Coverity CID: 224630] Uninitialized scalar variable in subsys/net/ip/igmp.c
- [GitHub #35157](https://github.com/zephyrproject-rtos/zephyr/issues/35157) - [Coverity CID: 221380] Uninitialized scalar variable in subsys/bluetooth/controller/ll\_sw/ull\_iso.c
- [GitHub #35156](https://github.com/zephyrproject-rtos/zephyr/issues/35156) - [Coverity CID: 235979] Unchecked return value in drivers/sensor/iis2mdc/iis2mdc\_trigger.c
- [GitHub #35155](https://github.com/zephyrproject-rtos/zephyr/issues/35155) - [Coverity CID: 235677] Unchecked return value in drivers/gpio/gpio\_cy8c95xx.c
- [GitHub #35154](https://github.com/zephyrproject-rtos/zephyr/issues/35154) - [Coverity CID: 233524] Unchecked return value in include/drivers/dma.h
- [GitHub #35153](https://github.com/zephyrproject-rtos/zephyr/issues/35153) - [Coverity CID: 236006] Structurally dead code in tests/subsys/logging/log\_api/src/test.inc
- [GitHub #35152](https://github.com/zephyrproject-rtos/zephyr/issues/35152) - [Coverity CID: 235986] Structurally dead code in tests/subsys/logging/log\_api/src/test.inc
- [GitHub #35151](https://github.com/zephyrproject-rtos/zephyr/issues/35151) - [Coverity CID: 235943] Reliance on integer endianness in include/sys/cbprintf\_cxx.h
- [GitHub #35150](https://github.com/zephyrproject-rtos/zephyr/issues/35150) - [Coverity CID: 225136] Out-of-bounds write in tests/kernel/sched/deadline/src/main.c
- [GitHub #35149](https://github.com/zephyrproject-rtos/zephyr/issues/35149) - [Coverity CID: 234410] Out-of-bounds read in tests/kernel/sched/preempt/src/main.c
- [GitHub #35148](https://github.com/zephyrproject-rtos/zephyr/issues/35148) - [Coverity CID: 236015] Out-of-bounds access in tests/subsys/logging/log\_api/src/mock\_backend.c
- [GitHub #35147](https://github.com/zephyrproject-rtos/zephyr/issues/35147) - [Coverity CID: 236012] Out-of-bounds access in subsys/bluetooth/audio/vcs\_client.c
- [GitHub #35146](https://github.com/zephyrproject-rtos/zephyr/issues/35146) - [Coverity CID: 235994] Out-of-bounds access in tests/kernel/interrupt/src/interrupt\_offload.c
- [GitHub #35145](https://github.com/zephyrproject-rtos/zephyr/issues/35145) - [Coverity CID: 235984] Out-of-bounds access in include/sys/cbprintf\_cxx.h
- [GitHub #35144](https://github.com/zephyrproject-rtos/zephyr/issues/35144) - [Coverity CID: 235944] Out-of-bounds access in subsys/bluetooth/audio/vcs\_client.c
- [GitHub #35143](https://github.com/zephyrproject-rtos/zephyr/issues/35143) - [Coverity CID: 235921] Out-of-bounds access in include/sys/cbprintf\_cxx.h
- [GitHub #35142](https://github.com/zephyrproject-rtos/zephyr/issues/35142) - [Coverity CID: 235914] Out-of-bounds access in subsys/bluetooth/audio/vcs.c
- [GitHub #35141](https://github.com/zephyrproject-rtos/zephyr/issues/35141) - [Coverity CID: 235913] Out-of-bounds access in subsys/bluetooth/audio/vcs.c
- [GitHub #35140](https://github.com/zephyrproject-rtos/zephyr/issues/35140) - [Coverity CID: 231072] Out-of-bounds access in tests/kernel/sched/preempt/src/main.c
- [GitHub #35139](https://github.com/zephyrproject-rtos/zephyr/issues/35139) - [Coverity CID: 229646] Out-of-bounds access in subsys/bluetooth/audio/vocs.c
- [GitHub #35138](https://github.com/zephyrproject-rtos/zephyr/issues/35138) - [Coverity CID: 229545] Out-of-bounds access in tests/subsys/canbus/isotp/conformance/src/main.c
- [GitHub #35137](https://github.com/zephyrproject-rtos/zephyr/issues/35137) - [Coverity CID: 225993] Out-of-bounds access in tests/subsys/canbus/isotp/conformance/src/main.c
- [GitHub #35136](https://github.com/zephyrproject-rtos/zephyr/issues/35136) - [Coverity CID: 235916] Operands don’t affect result in drivers/adc/adc\_stm32.c
- [GitHub #35135](https://github.com/zephyrproject-rtos/zephyr/issues/35135) - [Coverity CID: 235911] Negative array index write in tests/subsys/logging/log\_api/src/mock\_backend.c
- [GitHub #35134](https://github.com/zephyrproject-rtos/zephyr/issues/35134) - [Coverity CID: 222151] Negative array index write in tests/subsys/logging/log\_msg2/src/main.c
- [GitHub #35133](https://github.com/zephyrproject-rtos/zephyr/issues/35133) - [Coverity CID: 232501] Missing varargs init or cleanup in subsys/logging/log\_msg2.c
- [GitHub #35132](https://github.com/zephyrproject-rtos/zephyr/issues/35132) - [Coverity CID: 236003] Logically dead code in subsys/bluetooth/audio/vcs.c
- [GitHub #35131](https://github.com/zephyrproject-rtos/zephyr/issues/35131) - [Coverity CID: 235998] Logically dead code in subsys/bluetooth/audio/vcs.c
- [GitHub #35130](https://github.com/zephyrproject-rtos/zephyr/issues/35130) - [Coverity CID: 235997] Logically dead code in drivers/adc/adc\_stm32.c
- [GitHub #35129](https://github.com/zephyrproject-rtos/zephyr/issues/35129) - [Coverity CID: 235990] Logically dead code in subsys/bluetooth/audio/vcs.c
- [GitHub #35128](https://github.com/zephyrproject-rtos/zephyr/issues/35128) - [Coverity CID: 235970] Logically dead code in subsys/bluetooth/audio/vcs.c
- [GitHub #35127](https://github.com/zephyrproject-rtos/zephyr/issues/35127) - [Coverity CID: 235965] Logically dead code in tests/subsys/logging/log\_api/src/test.inc
- [GitHub #35126](https://github.com/zephyrproject-rtos/zephyr/issues/35126) - [Coverity CID: 235961] Logically dead code in tests/subsys/logging/log\_api/src/test.inc
- [GitHub #35125](https://github.com/zephyrproject-rtos/zephyr/issues/35125) - [Coverity CID: 235956] Logically dead code in subsys/bluetooth/audio/vcs.c
- [GitHub #35124](https://github.com/zephyrproject-rtos/zephyr/issues/35124) - [Coverity CID: 235955] Logically dead code in subsys/bluetooth/audio/vcs.c
- [GitHub #35123](https://github.com/zephyrproject-rtos/zephyr/issues/35123) - [Coverity CID: 235954] Logically dead code in subsys/bluetooth/audio/vcs.c
- [GitHub #35122](https://github.com/zephyrproject-rtos/zephyr/issues/35122) - [Coverity CID: 235952] Logically dead code in subsys/bluetooth/audio/vcs.c
- [GitHub #35121](https://github.com/zephyrproject-rtos/zephyr/issues/35121) - [Coverity CID: 235950] Logically dead code in subsys/bluetooth/audio/vcs.c
- [GitHub #35120](https://github.com/zephyrproject-rtos/zephyr/issues/35120) - [Coverity CID: 235934] Logically dead code in subsys/bluetooth/audio/vcs.c
- [GitHub #35119](https://github.com/zephyrproject-rtos/zephyr/issues/35119) - [Coverity CID: 235932] Logically dead code in samples/sensor/adxl372/src/main.c
- [GitHub #35118](https://github.com/zephyrproject-rtos/zephyr/issues/35118) - [Coverity CID: 235919] Logically dead code in samples/sensor/bmg160/src/main.c
- [GitHub #35117](https://github.com/zephyrproject-rtos/zephyr/issues/35117) - [Coverity CID: 235945] Incorrect sizeof expression in include/sys/cbprintf\_cxx.h
- [GitHub #35116](https://github.com/zephyrproject-rtos/zephyr/issues/35116) - [Coverity CID: 235987] Incompatible cast in include/sys/cbprintf\_cxx.h
- [GitHub #35115](https://github.com/zephyrproject-rtos/zephyr/issues/35115) - [Coverity CID: 236000] Improper use of negative value in tests/lib/cbprintf\_package/src/test.inc
- [GitHub #35114](https://github.com/zephyrproject-rtos/zephyr/issues/35114) - [Coverity CID: 221976] Division or modulo by zero in tests/drivers/can/timing/src/main.c
- [GitHub #35113](https://github.com/zephyrproject-rtos/zephyr/issues/35113) - [Coverity CID: 235985] Dereference before null check in subsys/bluetooth/audio/vcs\_client.c
- [GitHub #35112](https://github.com/zephyrproject-rtos/zephyr/issues/35112) - [Coverity CID: 235983] Dereference after null check in samples/sensor/max17262/src/main.c
- [GitHub #35111](https://github.com/zephyrproject-rtos/zephyr/issues/35111) - [Coverity CID: 234630] Dereference after null check in tests/net/dhcpv4/src/main.c
- [GitHub #35110](https://github.com/zephyrproject-rtos/zephyr/issues/35110) - [Coverity CID: 220616] Arguments in wrong order in tests/subsys/canbus/isotp/conformance/src/main.c
- [GitHub #35108](https://github.com/zephyrproject-rtos/zephyr/issues/35108) - tests: drivers: pwm: pwm\_api: failed on nucleo\_f207zg
- [GitHub #35107](https://github.com/zephyrproject-rtos/zephyr/issues/35107) - Atmel SAM E70 / Cortex-M7 fails to boot if CONFIG\_NOCACHE\_MEMORY=y
- [GitHub #35104](https://github.com/zephyrproject-rtos/zephyr/issues/35104) - arch.interrupt.gen\_isr\_table.arm\_mainline: fails on lpcxpresso55s16\_ns
- [GitHub #35102](https://github.com/zephyrproject-rtos/zephyr/issues/35102) - testing.ztest.error\_hook: fails on lpcxpresso55s16\_ns
- [GitHub #35100](https://github.com/zephyrproject-rtos/zephyr/issues/35100) - libraries.libc.sprintf\_new: fails on lpcxpresso55s16\_ns and lpcxpresso55s69\_ns
- [GitHub #35099](https://github.com/zephyrproject-rtos/zephyr/issues/35099) - benchmark.kernel.application.fp.arm: Illegal load of EXC\_RETURN into PC on lpcxpresso55s16\_ns and lpcxpresso55s69\_ns
- [GitHub #35097](https://github.com/zephyrproject-rtos/zephyr/issues/35097) - arch.interrupt: fails on NXP Cortex-M0+ platforms
- [GitHub #35091](https://github.com/zephyrproject-rtos/zephyr/issues/35091) - enc424j600 does not work
- [GitHub #35089](https://github.com/zephyrproject-rtos/zephyr/issues/35089) - stm32h7: systematic crash at each second boot with NETWORKING=y
- [GitHub #35083](https://github.com/zephyrproject-rtos/zephyr/issues/35083) - dts: stm32mp1: SPI2 mixup with SAI2, SPI3 mixup with SAI3
- [GitHub #35082](https://github.com/zephyrproject-rtos/zephyr/issues/35082) - intel\_adsp\_cavs15: All the testcases run failed on ADSP
- [GitHub #35079](https://github.com/zephyrproject-rtos/zephyr/issues/35079) - acrn\_ehl\_crb: build warnings for old APIC\_TIMER configs
- [GitHub #35076](https://github.com/zephyrproject-rtos/zephyr/issues/35076) - acrn\_ehl\_crb does not work with CPUs >1
- [GitHub #35075](https://github.com/zephyrproject-rtos/zephyr/issues/35075) - .west/config west.yml and zephyr versioning during project development
- [GitHub #35073](https://github.com/zephyrproject-rtos/zephyr/issues/35073) - timer: cortex\_m\_systick: uptime drifting in tickless mode
- [GitHub #35060](https://github.com/zephyrproject-rtos/zephyr/issues/35060) - tests/kernel/common: test\_nop failed on ARMV7\_M\_ARMV8\_M\_MAINLINE
- [GitHub #35058](https://github.com/zephyrproject-rtos/zephyr/issues/35058) - Bluetooth: deadlock when canceling db\_hash.work from settings commit handler
- [GitHub #35051](https://github.com/zephyrproject-rtos/zephyr/issues/35051) - CONFIG\_LOG2 fails for floating point output with warning and bad output
- [GitHub #35048](https://github.com/zephyrproject-rtos/zephyr/issues/35048) - mcuboot with enabled serial recovery does not compile
- [GitHub #35046](https://github.com/zephyrproject-rtos/zephyr/issues/35046) - Tracing shows k\_busy\_wait() being executed very often on nRF platforms
- [GitHub #35043](https://github.com/zephyrproject-rtos/zephyr/issues/35043) - NXP: Build error : ModuleNotFoundError: No module named ‘elftools’
- [GitHub #35041](https://github.com/zephyrproject-rtos/zephyr/issues/35041) - Crash in net-shell when invoking “net dns” command
- [GitHub #35036](https://github.com/zephyrproject-rtos/zephyr/issues/35036) - STM32: Wrong uart\_event\_tx len calculation
- [GitHub #35033](https://github.com/zephyrproject-rtos/zephyr/issues/35033) - samples/boards: stm32 pm blinky fails when run with twister
- [GitHub #35028](https://github.com/zephyrproject-rtos/zephyr/issues/35028) - frdm\_k64f: failed to run tests/subsys/pm/power\_mgmt/
- [GitHub #35027](https://github.com/zephyrproject-rtos/zephyr/issues/35027) - frdm\_k64f: failed to run testcase tests/drivers/adc/adc\_emul/
- [GitHub #35026](https://github.com/zephyrproject-rtos/zephyr/issues/35026) - sam\_e70b\_xplained: failed to run testcases tests/drivers/adc/adc\_emul/
- [GitHub #35013](https://github.com/zephyrproject-rtos/zephyr/issues/35013) - Bluetooth: Controller: Out-of-Bound ULL context access during connection completion
- [GitHub #34999](https://github.com/zephyrproject-rtos/zephyr/issues/34999) - Using BT\_ISO bluetooth hci\_usb sample, and enable, but still shows no command supported
- [GitHub #34989](https://github.com/zephyrproject-rtos/zephyr/issues/34989) - Implement arch\_page\_phys\_get() for ARM64
- [GitHub #34979](https://github.com/zephyrproject-rtos/zephyr/issues/34979) - MIMRT685-EVK board page has broken links
- [GitHub #34978](https://github.com/zephyrproject-rtos/zephyr/issues/34978) - misleading root folder size in footprint reports
- [GitHub #34969](https://github.com/zephyrproject-rtos/zephyr/issues/34969) - Documentation still mentions deprecated macro DT\_INST\_FOREACH\_STATUS\_OKAY
- [GitHub #34964](https://github.com/zephyrproject-rtos/zephyr/issues/34964) - net regression: Connection to Zephyr server non-deterministically leads to client timeout, ENOTCONN on server side
- [GitHub #34962](https://github.com/zephyrproject-rtos/zephyr/issues/34962) - tfm: cmake: Toolchain not being passed into psa-arch-tests
- [GitHub #34950](https://github.com/zephyrproject-rtos/zephyr/issues/34950) - xtensa arch ：The source code version is too old
- [GitHub #34948](https://github.com/zephyrproject-rtos/zephyr/issues/34948) - SoF module is not pointing at Zehpyr repo
- [GitHub #34935](https://github.com/zephyrproject-rtos/zephyr/issues/34935) - LwM2M: Block transfer with TLV format does not work
- [GitHub #34932](https://github.com/zephyrproject-rtos/zephyr/issues/34932) - drvers/flash/nrf\_qspi\_nor: high power consumption on nrf52840
- [GitHub #34931](https://github.com/zephyrproject-rtos/zephyr/issues/34931) - dns resolve timeout leads to CPU memory access violation error
- [GitHub #34925](https://github.com/zephyrproject-rtos/zephyr/issues/34925) - tests/lib/cbprintf\_package fails to build
- [GitHub #34923](https://github.com/zephyrproject-rtos/zephyr/issues/34923) - net.socket.get\_addr\_info: frdm\_k64f test fails
- [GitHub #34917](https://github.com/zephyrproject-rtos/zephyr/issues/34917) - arch.interrupt.arm| arch.interrupt.extra\_exception\_info: lpcxpresso55s28 series: test failure
- [GitHub #34915](https://github.com/zephyrproject-rtos/zephyr/issues/34915) - arch.interrupt.gen\_isr\_table.arm\_mainline:lpcxpresso55s16\_ns/lpcxpresso55s28: interrupt 57 does not work
- [GitHub #34911](https://github.com/zephyrproject-rtos/zephyr/issues/34911) - tests/kernel/mem\_protect/mem\_protect: frdm\_k82f/frdm\_k64f unexpected fatal error
- [GitHub #34909](https://github.com/zephyrproject-rtos/zephyr/issues/34909) - dma\_loopback:lpcxpresso55s28\_ns driver test failure
- [GitHub #34904](https://github.com/zephyrproject-rtos/zephyr/issues/34904) - uart\_mcux\_lpuart: Enable driver to work with `CONFIG_MULTITHREADING=n`
- [GitHub #34903](https://github.com/zephyrproject-rtos/zephyr/issues/34903) - doc: Target name is wrong for rcar\_h3ulcb board
- [GitHub #34891](https://github.com/zephyrproject-rtos/zephyr/issues/34891) - mcumgr timeout due to smp\_shell\_process stalling
- [GitHub #34880](https://github.com/zephyrproject-rtos/zephyr/issues/34880) - Convert SoF Module to new kwork API
- [GitHub #34865](https://github.com/zephyrproject-rtos/zephyr/issues/34865) - CONFIG\_NET\_SOCKETS\_PACKET interferes with other network traffic (gptp, IP)
- [GitHub #34862](https://github.com/zephyrproject-rtos/zephyr/issues/34862) - CAN ISO-TP implementation not using local work queue
- [GitHub #34852](https://github.com/zephyrproject-rtos/zephyr/issues/34852) - Some bluetooth advertising packages never get transmitted over-air (Bluetooth Mesh application)
- [GitHub #34844](https://github.com/zephyrproject-rtos/zephyr/issues/34844) - qemu\_cortex\_a53\_smp: tests/ztest/error\_hook failed after enabling the FPU context switching support
- [GitHub #34840](https://github.com/zephyrproject-rtos/zephyr/issues/34840) - CONFIG\_MULTITHREADING=n is not tested on hardware platforms
- [GitHub #34838](https://github.com/zephyrproject-rtos/zephyr/issues/34838) - tests/subsys/logging/log\_msg2 failes on qemu\_cortex\_a53
- [GitHub #34837](https://github.com/zephyrproject-rtos/zephyr/issues/34837) - Unstable multi connections between NRF52840
- [GitHub #34827](https://github.com/zephyrproject-rtos/zephyr/issues/34827) - tests: power management: test\_power\_state\_trans fails on nrf boards
- [GitHub #34796](https://github.com/zephyrproject-rtos/zephyr/issues/34796) - x86 jlink runner fails on M1 macs
- [GitHub #34794](https://github.com/zephyrproject-rtos/zephyr/issues/34794) - LIS2DH Hard Fault when INT2 is not defined
- [GitHub #34788](https://github.com/zephyrproject-rtos/zephyr/issues/34788) - APIC timer does not support SMP
- [GitHub #34777](https://github.com/zephyrproject-rtos/zephyr/issues/34777) - semaphore and condvar\_api tests fails after ARM64 FPU context switch commit on qemu\_cortex\_a53\_smp
- [GitHub #34772](https://github.com/zephyrproject-rtos/zephyr/issues/34772) - Mixed usage of signed/unsigned integer by the logging subsystem
- [GitHub #34757](https://github.com/zephyrproject-rtos/zephyr/issues/34757) - west update: Default behavior should fetch only –depth 1
- [GitHub #34753](https://github.com/zephyrproject-rtos/zephyr/issues/34753) - Building and Debugging Zephyr for Native Platform on Linux using VSCode and/or QtCreator
- [GitHub #34748](https://github.com/zephyrproject-rtos/zephyr/issues/34748) - Native posix: Segmentation fault in case of allocations without explicit heap assignment
- [GitHub #34739](https://github.com/zephyrproject-rtos/zephyr/issues/34739) - tests/arch/arm/arm\_no\_multithreading/arch.arm.no\_multithreading fails to build on a number of platforms
- [GitHub #34734](https://github.com/zephyrproject-rtos/zephyr/issues/34734) - Can handler doesn’t compile with CONFIG\_USERSPACE
- [GitHub #34722](https://github.com/zephyrproject-rtos/zephyr/issues/34722) - nvs: possibility of losing data
- [GitHub #34716](https://github.com/zephyrproject-rtos/zephyr/issues/34716) - flash: spi\_nor: build fails when CONFIG\_SPI\_NOR\_SFDP\_RUNTIME is enabled
- [GitHub #34696](https://github.com/zephyrproject-rtos/zephyr/issues/34696) - Unable to select LOG\_DICTIONARY\_SUPPORT when TEST\_LOGGING\_DEFAULTS=y
- [GitHub #34690](https://github.com/zephyrproject-rtos/zephyr/issues/34690) - net: process\_rx\_packet() work handler violates requirements of Workqueue Threads implementation
- [GitHub #34687](https://github.com/zephyrproject-rtos/zephyr/issues/34687) - intel\_adsp\_cavs15: run tests/kernel/semaphore/semaphore/ failed on ADSP
- [GitHub #34683](https://github.com/zephyrproject-rtos/zephyr/issues/34683) - MCUboot not confirm image when using ‘west flash’
- [GitHub #34672](https://github.com/zephyrproject-rtos/zephyr/issues/34672) - stm32h7: issue with CONFIG\_UART\_ASYNC\_API=y
- [GitHub #34670](https://github.com/zephyrproject-rtos/zephyr/issues/34670) - smp\_svr sample configured for serial port with shell management enabled does not work
- [GitHub #34669](https://github.com/zephyrproject-rtos/zephyr/issues/34669) - uart\_read\_fifo() reads only 2 chars on nucleo STM32L43KC and nRF52840-DK
- [GitHub #34668](https://github.com/zephyrproject-rtos/zephyr/issues/34668) - i2c\_ite\_it8xxx2.c fails to build - possibly related to device\_pm\_control\_nop changes
- [GitHub #34667](https://github.com/zephyrproject-rtos/zephyr/issues/34667) - posix\_apis:mimxrt685\_evk\_cm33 timeout in test\_posix\_realtime
- [GitHub #34662](https://github.com/zephyrproject-rtos/zephyr/issues/34662) - many udp networking cases fail on nxp platforms
- [GitHub #34658](https://github.com/zephyrproject-rtos/zephyr/issues/34658) - TF-M integration samples do not work with GNU ARM Embedded having GCC v10.x.x
- [GitHub #34656](https://github.com/zephyrproject-rtos/zephyr/issues/34656) - STM32 ADC - read of multiple channels in a sequence
- [GitHub #34644](https://github.com/zephyrproject-rtos/zephyr/issues/34644) - CAN - Bus Driver Sample
- [GitHub #34635](https://github.com/zephyrproject-rtos/zephyr/issues/34635) - BME280 build error
- [GitHub #34633](https://github.com/zephyrproject-rtos/zephyr/issues/34633) - STM32: Mass conversion of boards to dts based clock control configuration
- [GitHub #34624](https://github.com/zephyrproject-rtos/zephyr/issues/34624) - Coding guidelines 15.7 PR causes tests failures
- [GitHub #34605](https://github.com/zephyrproject-rtos/zephyr/issues/34605) - flash\_stm32h7x.c fails to build
- [GitHub #34601](https://github.com/zephyrproject-rtos/zephyr/issues/34601) - sample: bluetooth: beacon: USAGE FAULT after few seconds on board b\_l4s5i\_iot01a
- [GitHub #34597](https://github.com/zephyrproject-rtos/zephyr/issues/34597) - Mismatch between `ot ping` and `net ping`
- [GitHub #34593](https://github.com/zephyrproject-rtos/zephyr/issues/34593) - Using hci\_usb with Bluez 5.55 or 5.58
- [GitHub #34585](https://github.com/zephyrproject-rtos/zephyr/issues/34585) - mec15xxevb\_assy6853: test\_timeout\_order in tests/kernel/common assertion failed
- [GitHub #34584](https://github.com/zephyrproject-rtos/zephyr/issues/34584) - kernel: workqueue thread is occasionally not invoked when kernel is run in cooperative mode only
- [GitHub #34583](https://github.com/zephyrproject-rtos/zephyr/issues/34583) - twister failing: fails platform native\_posix, test lib/cmsis\_dsp/filtering
- [GitHub #34581](https://github.com/zephyrproject-rtos/zephyr/issues/34581) - Unable to work with SX1276 Lora module.
- [GitHub #34570](https://github.com/zephyrproject-rtos/zephyr/issues/34570) - IPC samples running secure but configured nonsecure (AN521)
- [GitHub #34568](https://github.com/zephyrproject-rtos/zephyr/issues/34568) - Compilation error with zephyr 2.3.0
- [GitHub #34563](https://github.com/zephyrproject-rtos/zephyr/issues/34563) - net: lib: sockets: Unable to select() file descriptors with number >= 32
- [GitHub #34558](https://github.com/zephyrproject-rtos/zephyr/issues/34558) - Compilation error with Log v2 and CONFIG\_LOG\_PRINTK
- [GitHub #34541](https://github.com/zephyrproject-rtos/zephyr/issues/34541) - per-adv-sync-create doesn’t work on nRF52840, ./tests/bluetooth/shell/
- [GitHub #34538](https://github.com/zephyrproject-rtos/zephyr/issues/34538) - STM32 temperature sensor
- [GitHub #34534](https://github.com/zephyrproject-rtos/zephyr/issues/34534) - west sign regression when HEX file not exists
- [GitHub #34527](https://github.com/zephyrproject-rtos/zephyr/issues/34527) - Cpp compiling error: expected primary-expression before ‘char’. \_Generic macros problem
- [GitHub #34526](https://github.com/zephyrproject-rtos/zephyr/issues/34526) - logging tests fails to build on a number of platforms
- [GitHub #34515](https://github.com/zephyrproject-rtos/zephyr/issues/34515) - samples: net: syslog\_net: hard fault when running on frdm\_k64f
- [GitHub #34505](https://github.com/zephyrproject-rtos/zephyr/issues/34505) - mimxrt1050\_evk:failed to run testcases tests/net
- [GitHub #34503](https://github.com/zephyrproject-rtos/zephyr/issues/34503) - up\_squared and ehl\_crb: test fails from timeout in application\_development.cpp.libcxx.exceptions
- [GitHub #34500](https://github.com/zephyrproject-rtos/zephyr/issues/34500) - thingy52 lis2dh12 sensor values too large
- [GitHub #34495](https://github.com/zephyrproject-rtos/zephyr/issues/34495) - logger: Logger API cannot be compiled with C++
- [GitHub #34492](https://github.com/zephyrproject-rtos/zephyr/issues/34492) - Logging still broken with SOF
- [GitHub #34482](https://github.com/zephyrproject-rtos/zephyr/issues/34482) - net\_tunnel\_virtual:frdm\_k64f: build failure
- [GitHub #34474](https://github.com/zephyrproject-rtos/zephyr/issues/34474) - MPS2-AN385 SRAM does not match what the documentation page says
- [GitHub #34473](https://github.com/zephyrproject-rtos/zephyr/issues/34473) - Add Requirements repository with infrastructure and placeholder requirements
- [GitHub #34469](https://github.com/zephyrproject-rtos/zephyr/issues/34469) - nrf53: nrf5340dk\_nrf5340\_cpunet not executing.
- [GitHub #34463](https://github.com/zephyrproject-rtos/zephyr/issues/34463) - LwM2M bootstrap DELETE operation not working
- [GitHub #34462](https://github.com/zephyrproject-rtos/zephyr/issues/34462) - samples: net: sockets: packet: reception stops working after a while
- [GitHub #34461](https://github.com/zephyrproject-rtos/zephyr/issues/34461) - Unable to use PWM pins with STM Nucleo H743ZI
- [GitHub #34443](https://github.com/zephyrproject-rtos/zephyr/issues/34443) - Document font display is incomplete
- [GitHub #34439](https://github.com/zephyrproject-rtos/zephyr/issues/34439) - Logging subsystem causes build to fail with LLVM
- [GitHub #34434](https://github.com/zephyrproject-rtos/zephyr/issues/34434) - subsys: testsuite: ztest framework breaks if run in cooperative mode only
- [GitHub #34426](https://github.com/zephyrproject-rtos/zephyr/issues/34426) - RFC: API Change: USB HID remove get\_protocol/set\_protocol/get\_idle/set\_idle callbacks
- [GitHub #34423](https://github.com/zephyrproject-rtos/zephyr/issues/34423) - twister build issue with arm64
- [GitHub #34419](https://github.com/zephyrproject-rtos/zephyr/issues/34419) - significant build time increase with new logging subsystem
- [GitHub #34416](https://github.com/zephyrproject-rtos/zephyr/issues/34416) - Configuration HAS\_DTS has no function, preventing compile for vendors without device tree
- [GitHub #34409](https://github.com/zephyrproject-rtos/zephyr/issues/34409) - mDNS response on link local when using DHCPv4 and AutoIP/Static IP
- [GitHub #34403](https://github.com/zephyrproject-rtos/zephyr/issues/34403) - Logging disable function causes Zephyr hard lockup
- [GitHub #34402](https://github.com/zephyrproject-rtos/zephyr/issues/34402) - spi: spi\_nrfx\_spim: wrong clock frequency selected
- [GitHub #34397](https://github.com/zephyrproject-rtos/zephyr/issues/34397) - Update getting started docs to reflect gdb python requirements
- [GitHub #34387](https://github.com/zephyrproject-rtos/zephyr/issues/34387) - Error message in include/linker/kobject-text.ld is unclear
- [GitHub #34382](https://github.com/zephyrproject-rtos/zephyr/issues/34382) - fs/nvs: if closing ATE has to high offset NVS iterates up to the end of flash.
- [GitHub #34372](https://github.com/zephyrproject-rtos/zephyr/issues/34372) - CPU Lockups when using own Log Backend
- [GitHub #34369](https://github.com/zephyrproject-rtos/zephyr/issues/34369) - Driver esp for wifi got a dead lock.
- [GitHub #34368](https://github.com/zephyrproject-rtos/zephyr/issues/34368) - Cmake’s Python path breaks after using west build –pristine
- [GitHub #34363](https://github.com/zephyrproject-rtos/zephyr/issues/34363) - k\_work: incorrect return values for synchronous cancel
- [GitHub #34355](https://github.com/zephyrproject-rtos/zephyr/issues/34355) - LittleFS sample code catch an “undefined symbol ‘ITCM\_ADDR’ referenced in expression” in linker step
- [GitHub #34345](https://github.com/zephyrproject-rtos/zephyr/issues/34345) - samples/net/civetweb/websocket\_server fails to build
- [GitHub #34342](https://github.com/zephyrproject-rtos/zephyr/issues/34342) - No output on SWO pin (STM32L4)
- [GitHub #34341](https://github.com/zephyrproject-rtos/zephyr/issues/34341) - SWO logging and DWT timing collision
- [GitHub #34329](https://github.com/zephyrproject-rtos/zephyr/issues/34329) - lwm2m: pmin and pmax attributes should be optional
- [GitHub #34325](https://github.com/zephyrproject-rtos/zephyr/issues/34325) - hal: microchip: Missing Wake bit definitions
- [GitHub #34309](https://github.com/zephyrproject-rtos/zephyr/issues/34309) - unable to connect to azure iot hub via mqtt protocol
- [GitHub #34308](https://github.com/zephyrproject-rtos/zephyr/issues/34308) - SPI transceive function only transmitting first tx\_buffer on Sifive’s MCU
- [GitHub #34304](https://github.com/zephyrproject-rtos/zephyr/issues/34304) - intel\_adsp\_cavs15: run tests/kernel/queue/ failed on ADSP
- [GitHub #34295](https://github.com/zephyrproject-rtos/zephyr/issues/34295) - TensorFlow Lite Micro Module
- [GitHub #34280](https://github.com/zephyrproject-rtos/zephyr/issues/34280) - Add USB to LPCXpresso55S69 board
- [GitHub #34275](https://github.com/zephyrproject-rtos/zephyr/issues/34275) - drivers: led\_pwm: Improper label assignment
- [GitHub #34272](https://github.com/zephyrproject-rtos/zephyr/issues/34272) - twister: Add memory footprint info to json report
- [GitHub #34270](https://github.com/zephyrproject-rtos/zephyr/issues/34270) - NVS read after consecutive restarts.
- [GitHub #34265](https://github.com/zephyrproject-rtos/zephyr/issues/34265) - BME280 Pressure calculation
- [GitHub #34264](https://github.com/zephyrproject-rtos/zephyr/issues/34264) - CI: twister: Add merged report from all sub-builds to buildkite build artifacts
- [GitHub #34262](https://github.com/zephyrproject-rtos/zephyr/issues/34262) - Unable to find detailed documentation on pinmux driver development
- [GitHub #34249](https://github.com/zephyrproject-rtos/zephyr/issues/34249) - Unable to initialize on STM32F103RE + Quectel EC21 using BG9x driver
- [GitHub #34246](https://github.com/zephyrproject-rtos/zephyr/issues/34246) - LoRa driver sending opcode of commands without parameters
- [GitHub #34234](https://github.com/zephyrproject-rtos/zephyr/issues/34234) - UART NS16550 Underflow Issue During Clearing Port
- [GitHub #34233](https://github.com/zephyrproject-rtos/zephyr/issues/34233) - OpenThread build issues
- [GitHub #34231](https://github.com/zephyrproject-rtos/zephyr/issues/34231) - uzlib (decompression library)
- [GitHub #34229](https://github.com/zephyrproject-rtos/zephyr/issues/34229) - C++ Exception Support in qemu\_riscv32 emulation
- [GitHub #34225](https://github.com/zephyrproject-rtos/zephyr/issues/34225) - BBC micro:bit v1.5 LSM303AGR-ACCEL
- [GitHub #34216](https://github.com/zephyrproject-rtos/zephyr/issues/34216) - Using nrfx\_gpiote library with spi(nrf52840)
- [GitHub #34214](https://github.com/zephyrproject-rtos/zephyr/issues/34214) - codes reference weak variable are optimized out
- [GitHub #34209](https://github.com/zephyrproject-rtos/zephyr/issues/34209) - BLE Mesh Provisioning generates value 0 outside of Specification for Blink, Beep, or Vibrate
- [GitHub #34206](https://github.com/zephyrproject-rtos/zephyr/issues/34206) - Question: Is zephyrproject actively maintaining the windows-curses sub-project?
- [GitHub #34202](https://github.com/zephyrproject-rtos/zephyr/issues/34202) - MPU Fault when running central coded bluetooth and ENC28J60 dhcpv4\_client
- [GitHub #34201](https://github.com/zephyrproject-rtos/zephyr/issues/34201) - Fatal error when perform “bt phy-update” if there is not any connections at ./tests/bluetooth/shell
- [GitHub #34197](https://github.com/zephyrproject-rtos/zephyr/issues/34197) - samples: telnet: Tab completion not working in telnet shell
- [GitHub #34196](https://github.com/zephyrproject-rtos/zephyr/issues/34196) - st\_lis2mdl: LSM303AGR-MAGN not detected
- [GitHub #34190](https://github.com/zephyrproject-rtos/zephyr/issues/34190) - Newbie: Simple C++ List App Builds for QEMU but not Native Posix Emulation
- [GitHub #34184](https://github.com/zephyrproject-rtos/zephyr/issues/34184) - video samples fail to build
- [GitHub #34178](https://github.com/zephyrproject-rtos/zephyr/issues/34178) - apds9960 sensor sample does not build on STM32
- [GitHub #34165](https://github.com/zephyrproject-rtos/zephyr/issues/34165) - SNTP fails to close the used socket
- [GitHub #34154](https://github.com/zephyrproject-rtos/zephyr/issues/34154) - AArch64 PR reviews and merges are lagging behind
- [GitHub #34152](https://github.com/zephyrproject-rtos/zephyr/issues/34152) - intel\_adsp\_cavs15: run tests/kernel/smp/ failed on ADSP
- [GitHub #34149](https://github.com/zephyrproject-rtos/zephyr/issues/34149) - Invalid link in Zephyr document to ACRN page
- [GitHub #34145](https://github.com/zephyrproject-rtos/zephyr/issues/34145) - Convert NXP kinetis boards to have pindata in devicetree
- [GitHub #34134](https://github.com/zephyrproject-rtos/zephyr/issues/34134) - USB do not works if bootloader badly use the device before
- [GitHub #34117](https://github.com/zephyrproject-rtos/zephyr/issues/34117) - ehl\_crb: tests/kernel/context tests failed
- [GitHub #34116](https://github.com/zephyrproject-rtos/zephyr/issues/34116) - mec15xxevb\_assy6853: tests/kernel/mutex/sys\_mutex/
- [GitHub #34107](https://github.com/zephyrproject-rtos/zephyr/issues/34107) - Convert tests/benchmarks/mbedtls/src/benchmark.c to new kwork API
- [GitHub #34106](https://github.com/zephyrproject-rtos/zephyr/issues/34106) - Convert tests/kernel/pending/src/main.c to new kwork API
- [GitHub #34104](https://github.com/zephyrproject-rtos/zephyr/issues/34104) - Convert tests/benchmarks/footprints/src/workq.c to new kwork API
- [GitHub #34103](https://github.com/zephyrproject-rtos/zephyr/issues/34103) - Convert drivers/console/uart\_mux.c to new kwork API
- [GitHub #34102](https://github.com/zephyrproject-rtos/zephyr/issues/34102) - Convert drivers/serial/uart\_sam0.c to new kwork API
- [GitHub #34101](https://github.com/zephyrproject-rtos/zephyr/issues/34101) - Convert subsys/mgmt to new kwork API
- [GitHub #34100](https://github.com/zephyrproject-rtos/zephyr/issues/34100) - Convert subsys/shell/shell\_telnet to new kwork API
- [GitHub #34099](https://github.com/zephyrproject-rtos/zephyr/issues/34099) - Convert subsys/tracing/cpu\_stats.c to new kwork API
- [GitHub #34098](https://github.com/zephyrproject-rtos/zephyr/issues/34098) - Convert samples/drivers/led\_sx1509b\_intensity to new kwork API
- [GitHub #34097](https://github.com/zephyrproject-rtos/zephyr/issues/34097) - Convert samples/boards/reel\_board/mesh\_badge to new kwork API
- [GitHub #34096](https://github.com/zephyrproject-rtos/zephyr/issues/34096) - Convert samples nrf clock\_skew to new kwork API
- [GitHub #34095](https://github.com/zephyrproject-rtos/zephyr/issues/34095) - Convert CAN to new kwork API
- [GitHub #34094](https://github.com/zephyrproject-rtos/zephyr/issues/34094) - Convert ubsys/ipc/rpmsg\_service/rpmsg\_backend.c to new kwork API
- [GitHub #34093](https://github.com/zephyrproject-rtos/zephyr/issues/34093) - Convert bluetooth to new kwork API
- [GitHub #34092](https://github.com/zephyrproject-rtos/zephyr/issues/34092) - Convert usb to new kwork API
- [GitHub #34091](https://github.com/zephyrproject-rtos/zephyr/issues/34091) - Convert uart\_stm32.c to new kwork API
- [GitHub #34090](https://github.com/zephyrproject-rtos/zephyr/issues/34090) - Convert video\_sw\_generator.c to new kwork API
- [GitHub #34082](https://github.com/zephyrproject-rtos/zephyr/issues/34082) - Bullets are broken in documentation
- [GitHub #34076](https://github.com/zephyrproject-rtos/zephyr/issues/34076) - Unrecognized characters generated during document construction
- [GitHub #34068](https://github.com/zephyrproject-rtos/zephyr/issues/34068) - DOC BUILD FAIL
- [GitHub #34046](https://github.com/zephyrproject-rtos/zephyr/issues/34046) - Failed to build arm64 architecture related board
- [GitHub #34045](https://github.com/zephyrproject-rtos/zephyr/issues/34045) - samples: subsys: mgmt: smp\_srv: UDP sample does not boot on frdm\_k64f
- [GitHub #34026](https://github.com/zephyrproject-rtos/zephyr/issues/34026) - RISCV32 QEMU illegal instruction exception / floating point support
- [GitHub #34023](https://github.com/zephyrproject-rtos/zephyr/issues/34023) - test\_prevent\_interruption has wrong data type for key
- [GitHub #34014](https://github.com/zephyrproject-rtos/zephyr/issues/34014) - Toolchain Compile Error of RISC-V(rv32m1-vega board)
- [GitHub #34011](https://github.com/zephyrproject-rtos/zephyr/issues/34011) - NRF52840 DTS questions
- [GitHub #34010](https://github.com/zephyrproject-rtos/zephyr/issues/34010) - [Coverity CID: 220531] Copy into fixed size buffer in tests/net/socket/misc/src/main.c
- [GitHub #34009](https://github.com/zephyrproject-rtos/zephyr/issues/34009) - [Coverity CID: 220532] Unrecoverable parse warning in subsys/bluetooth/controller/ll\_sw/ull\_peripheral\_iso.c
- [GitHub #34008](https://github.com/zephyrproject-rtos/zephyr/issues/34008) - [Coverity CID: 220533] Improper use of negative value in tests/net/socket/misc/src/main.c
- [GitHub #34007](https://github.com/zephyrproject-rtos/zephyr/issues/34007) - [Coverity CID: 220534] Out-of-bounds access in tests/arch/arm/arm\_no\_multithreading/src/main.c
- [GitHub #34006](https://github.com/zephyrproject-rtos/zephyr/issues/34006) - [Coverity CID: 220535] Dereference before null check in subsys/net/l2/virtual/virtual.c
- [GitHub #34005](https://github.com/zephyrproject-rtos/zephyr/issues/34005) - [Coverity CID: 220536] Pointer to local outside scope in subsys/net/lib/lwm2m/lwm2m\_engine.c
- [GitHub #34004](https://github.com/zephyrproject-rtos/zephyr/issues/34004) - [Coverity CID: 220537] Uninitialized pointer read in tests/net/virtual/src/main.c
- [GitHub #34003](https://github.com/zephyrproject-rtos/zephyr/issues/34003) - [Coverity CID: 220538] Logically dead code in subsys/net/l2/virtual/virtual.c
- [GitHub #34002](https://github.com/zephyrproject-rtos/zephyr/issues/34002) - [Coverity CID: 220539] Improper use of negative value in tests/net/socket/misc/src/main.c
- [GitHub #34001](https://github.com/zephyrproject-rtos/zephyr/issues/34001) - [Coverity CID: 220540] Uninitialized scalar variable in samples/drivers/flash\_shell/src/main.c
- [GitHub #34000](https://github.com/zephyrproject-rtos/zephyr/issues/34000) - [Coverity CID: 220541] Dereference before null check in subsys/net/lib/capture/capture.c
- [GitHub #33986](https://github.com/zephyrproject-rtos/zephyr/issues/33986) - TCP stack doesn’t handle data received in FIN\_WAIT\_1
- [GitHub #33983](https://github.com/zephyrproject-rtos/zephyr/issues/33983) - example-application module: add trivial driver
- [GitHub #33981](https://github.com/zephyrproject-rtos/zephyr/issues/33981) - example-application module: add board zxa\_board\_stub
- [GitHub #33978](https://github.com/zephyrproject-rtos/zephyr/issues/33978) - MCP2515 wrong BRP value
- [GitHub #33977](https://github.com/zephyrproject-rtos/zephyr/issues/33977) - Question: How best to contribute drivers upstream?
- [GitHub #33974](https://github.com/zephyrproject-rtos/zephyr/issues/33974) - The stm32wb55rc MCU does not operate on zephyr
- [GitHub #33969](https://github.com/zephyrproject-rtos/zephyr/issues/33969) - Hardfault error caused by ARM Cortex m0 non-4-byte alignment
- [GitHub #33968](https://github.com/zephyrproject-rtos/zephyr/issues/33968) - ESP32 Porting GSM Module Compile Error
- [GitHub #33967](https://github.com/zephyrproject-rtos/zephyr/issues/33967) - The printed total size differs from calculated from .json
- [GitHub #33966](https://github.com/zephyrproject-rtos/zephyr/issues/33966) - STM32: I-cache & D-cache
- [GitHub #33965](https://github.com/zephyrproject-rtos/zephyr/issues/33965) - example-application module: add trivial project
- [GitHub #33956](https://github.com/zephyrproject-rtos/zephyr/issues/33956) - tests: kernel: fpu: Several tests related to fpu fail on nrf5340dk\_nrf5340\_cpuappns
- [GitHub #33954](https://github.com/zephyrproject-rtos/zephyr/issues/33954) - I2C scan in UART shell is not detecting any I2C devices on ESP32
- [GitHub #33951](https://github.com/zephyrproject-rtos/zephyr/issues/33951) - periodic\_adv not working with nRF5340 DK
- [GitHub #33950](https://github.com/zephyrproject-rtos/zephyr/issues/33950) - periodic\_adv not working with nRF5340 DK
- [GitHub #33929](https://github.com/zephyrproject-rtos/zephyr/issues/33929) - subsys: logging: Sample app doesn’t build if using Werror and logging with latest SDK
- [GitHub #33925](https://github.com/zephyrproject-rtos/zephyr/issues/33925) - Rework hl7800 driver to use new work queue APIs
- [GitHub #33923](https://github.com/zephyrproject-rtos/zephyr/issues/33923) - GSM modem automatic operation selection mode problems
- [GitHub #33911](https://github.com/zephyrproject-rtos/zephyr/issues/33911) - test:twr\_ke18f: tests/kernel/sched/schedule\_api - kernel\_threads\_sched\_userspace cases meet out our space
- [GitHub #33904](https://github.com/zephyrproject-rtos/zephyr/issues/33904) - having issue compile a shell program and it is bug likely
- [GitHub #33898](https://github.com/zephyrproject-rtos/zephyr/issues/33898) - intel\_adsp\_cavs15: running testcases failed tests/kernel/workq/work on adsp
- [GitHub #33897](https://github.com/zephyrproject-rtos/zephyr/issues/33897) - Bluetooth: extended advertising can’t restart after connection
- [GitHub #33896](https://github.com/zephyrproject-rtos/zephyr/issues/33896) - Device tree: STM32L4 defines can1 node for chips which do not support CAN peripheral
- [GitHub #33895](https://github.com/zephyrproject-rtos/zephyr/issues/33895) - Device tree: STM32L412 and STM32L422 are missing nodes
- [GitHub #33890](https://github.com/zephyrproject-rtos/zephyr/issues/33890) - Continuous Integration check patch false warnings
- [GitHub #33884](https://github.com/zephyrproject-rtos/zephyr/issues/33884) - CORTEX\_M\_DEBUG\_NULL\_POINTER\_EXCEPTION\_DETECTION\_NONE is way too long
- [GitHub #33874](https://github.com/zephyrproject-rtos/zephyr/issues/33874) - twister: Add skip as error feature
- [GitHub #33868](https://github.com/zephyrproject-rtos/zephyr/issues/33868) - Bluetooth: controller: connectable advertisement disable race condition
- [GitHub #33866](https://github.com/zephyrproject-rtos/zephyr/issues/33866) - uart: TX\_DONE occurs before transmission is complete.
- [GitHub #33860](https://github.com/zephyrproject-rtos/zephyr/issues/33860) - DEPRECATED, a replacement suggestion should be found somewhere
- [GitHub #33858](https://github.com/zephyrproject-rtos/zephyr/issues/33858) - tests: ztest: test trigger\_fault\_access from tests/ztest/error\_hook fails on em\_starterkit\_em7d\_v22
- [GitHub #33857](https://github.com/zephyrproject-rtos/zephyr/issues/33857) - atomic xtensa build fail
- [GitHub #33843](https://github.com/zephyrproject-rtos/zephyr/issues/33843) - ESP32 example does not connect to WiFi
- [GitHub #33840](https://github.com/zephyrproject-rtos/zephyr/issues/33840) - [Coverity CID: 220301] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33839](https://github.com/zephyrproject-rtos/zephyr/issues/33839) - [Coverity CID: 220302] Uninitialized scalar variable in subsys/net/lib/lwm2m/lwm2m\_rw\_link\_format.c
- [GitHub #33838](https://github.com/zephyrproject-rtos/zephyr/issues/33838) - [Coverity CID: 220304] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33837](https://github.com/zephyrproject-rtos/zephyr/issues/33837) - [Coverity CID: 220305] Logically dead code in drivers/gpio/gpio\_nrfx.c
- [GitHub #33836](https://github.com/zephyrproject-rtos/zephyr/issues/33836) - [Coverity CID: 220306] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33835](https://github.com/zephyrproject-rtos/zephyr/issues/33835) - [Coverity CID: 220309] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33834](https://github.com/zephyrproject-rtos/zephyr/issues/33834) - [Coverity CID: 220310] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33833](https://github.com/zephyrproject-rtos/zephyr/issues/33833) - [Coverity CID: 220311] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33832](https://github.com/zephyrproject-rtos/zephyr/issues/33832) - [Coverity CID: 220312] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33831](https://github.com/zephyrproject-rtos/zephyr/issues/33831) - [Coverity CID: 220313] Logically dead code in subsys/bluetooth/services/ots/ots\_obj\_manager.c
- [GitHub #33830](https://github.com/zephyrproject-rtos/zephyr/issues/33830) - [Coverity CID: 220314] Untrusted value as argument in subsys/bluetooth/services/ots/ots\_dir\_list.c
- [GitHub #33829](https://github.com/zephyrproject-rtos/zephyr/issues/33829) - [Coverity CID: 220315] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33828](https://github.com/zephyrproject-rtos/zephyr/issues/33828) - [Coverity CID: 220316] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33827](https://github.com/zephyrproject-rtos/zephyr/issues/33827) - [Coverity CID: 220317] Unchecked return value in tests/kernel/pipe/pipe\_api/src/test\_pipe\_contexts.c
- [GitHub #33826](https://github.com/zephyrproject-rtos/zephyr/issues/33826) - [Coverity CID: 220318] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33825](https://github.com/zephyrproject-rtos/zephyr/issues/33825) - [Coverity CID: 220319] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33824](https://github.com/zephyrproject-rtos/zephyr/issues/33824) - [Coverity CID: 220320] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33823](https://github.com/zephyrproject-rtos/zephyr/issues/33823) - [Coverity CID: 220321] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33822](https://github.com/zephyrproject-rtos/zephyr/issues/33822) - [Coverity CID: 220413] Explicit null dereferenced in tests/lib/sprintf/src/main.c
- [GitHub #33821](https://github.com/zephyrproject-rtos/zephyr/issues/33821) - [Coverity CID: 220414] Unused value in tests/subsys/logging/log\_backend\_fs/src/log\_fs\_test.c
- [GitHub #33820](https://github.com/zephyrproject-rtos/zephyr/issues/33820) - [Coverity CID: 220415] Uninitialized scalar variable in tests/posix/common/src/pthread.c
- [GitHub #33819](https://github.com/zephyrproject-rtos/zephyr/issues/33819) - [Coverity CID: 220417] Out-of-bounds access in subsys/modbus/modbus\_core.c
- [GitHub #33818](https://github.com/zephyrproject-rtos/zephyr/issues/33818) - [Coverity CID: 220418] Destination buffer too small in subsys/modbus/modbus\_raw.c
- [GitHub #33817](https://github.com/zephyrproject-rtos/zephyr/issues/33817) - [Coverity CID: 220419] Unchecked return value in subsys/bluetooth/host/gatt.c
- [GitHub #33816](https://github.com/zephyrproject-rtos/zephyr/issues/33816) - [Coverity CID: 220420] Out-of-bounds access in tests/subsys/modbus/src/test\_modbus\_raw.c
- [GitHub #33815](https://github.com/zephyrproject-rtos/zephyr/issues/33815) - [Coverity CID: 220421] Incorrect sizeof expression in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33814](https://github.com/zephyrproject-rtos/zephyr/issues/33814) - [Coverity CID: 220422] Extra argument to printf format specifier in tests/lib/sprintf/src/main.c
- [GitHub #33813](https://github.com/zephyrproject-rtos/zephyr/issues/33813) - [Coverity CID: 220423] Out-of-bounds access in subsys/net/l2/ppp/ppp\_l2.c
- [GitHub #33812](https://github.com/zephyrproject-rtos/zephyr/issues/33812) - [Coverity CID: 220424] Out-of-bounds access in drivers/watchdog/wdt\_mcux\_imx\_wdog.c
- [GitHub #33811](https://github.com/zephyrproject-rtos/zephyr/issues/33811) - [Coverity CID: 220425] Destination buffer too small in tests/subsys/modbus/src/test\_modbus\_raw.c
- [GitHub #33810](https://github.com/zephyrproject-rtos/zephyr/issues/33810) - [Coverity CID: 220426] Out-of-bounds access in tests/lib/c\_lib/src/main.c
- [GitHub #33809](https://github.com/zephyrproject-rtos/zephyr/issues/33809) - [Coverity CID: 220427] Unchecked return value in tests/posix/common/src/pthread.c
- [GitHub #33808](https://github.com/zephyrproject-rtos/zephyr/issues/33808) - [Coverity CID: 220428] Out-of-bounds access in subsys/bluetooth/audio/vocs.c
- [GitHub #33807](https://github.com/zephyrproject-rtos/zephyr/issues/33807) - [Coverity CID: 220429] Out-of-bounds access in subsys/net/l2/ppp/ppp\_l2.c
- [GitHub #33806](https://github.com/zephyrproject-rtos/zephyr/issues/33806) - [Coverity CID: 220430] Operands don’t affect result in tests/lib/c\_lib/src/main.c
- [GitHub #33805](https://github.com/zephyrproject-rtos/zephyr/issues/33805) - [Coverity CID: 220431] Extra argument to printf format specifier in tests/lib/sprintf/src/main.c
- [GitHub #33804](https://github.com/zephyrproject-rtos/zephyr/issues/33804) - [Coverity CID: 220432] Out-of-bounds access in subsys/net/l2/ethernet/ethernet.c
- [GitHub #33803](https://github.com/zephyrproject-rtos/zephyr/issues/33803) - [Coverity CID: 220433] Printf arg count mismatch in tests/lib/sprintf/src/main.c
- [GitHub #33802](https://github.com/zephyrproject-rtos/zephyr/issues/33802) - [Coverity CID: 220434] Resource leak in tests/lib/mem\_alloc/src/main.c
- [GitHub #33801](https://github.com/zephyrproject-rtos/zephyr/issues/33801) - [Coverity CID: 220435] Extra argument to printf format specifier in tests/lib/sprintf/src/main.c
- [GitHub #33800](https://github.com/zephyrproject-rtos/zephyr/issues/33800) - [Coverity CID: 220436] Explicit null dereferenced in tests/lib/sprintf/src/main.c
- [GitHub #33799](https://github.com/zephyrproject-rtos/zephyr/issues/33799) - [Coverity CID: 220437] Wrong size argument in tests/lib/mem\_alloc/src/main.c
- [GitHub #33798](https://github.com/zephyrproject-rtos/zephyr/issues/33798) - [Coverity CID: 220438] Out-of-bounds access in subsys/bluetooth/audio/vocs\_client.c
- [GitHub #33797](https://github.com/zephyrproject-rtos/zephyr/issues/33797) - [Coverity CID: 220439] Destination buffer too small in tests/subsys/modbus/src/test\_modbus\_raw.c
- [GitHub #33796](https://github.com/zephyrproject-rtos/zephyr/issues/33796) - [Coverity CID: 220440] Out-of-bounds access in tests/subsys/modbus/src/test\_modbus\_raw.c
- [GitHub #33795](https://github.com/zephyrproject-rtos/zephyr/issues/33795) - [Coverity CID: 220441] Untrusted loop bound in subsys/modbus/modbus\_client.c
- [GitHub #33794](https://github.com/zephyrproject-rtos/zephyr/issues/33794) - [Coverity CID: 220442] Pointless string comparison in tests/lib/c\_lib/src/main.c
- [GitHub #33793](https://github.com/zephyrproject-rtos/zephyr/issues/33793) - [Coverity CID: 220443] Out-of-bounds access in tests/subsys/modbus/src/test\_modbus\_raw.c
- [GitHub #33792](https://github.com/zephyrproject-rtos/zephyr/issues/33792) - [Coverity CID: 220444] Out-of-bounds access in subsys/modbus/modbus\_raw.c
- [GitHub #33791](https://github.com/zephyrproject-rtos/zephyr/issues/33791) - [Coverity CID: 220445] Unchecked return value in subsys/logging/log\_backend\_fs.c
- [GitHub #33790](https://github.com/zephyrproject-rtos/zephyr/issues/33790) - [Coverity CID: 220446] Printf arg count mismatch in tests/lib/sprintf/src/main.c
- [GitHub #33789](https://github.com/zephyrproject-rtos/zephyr/issues/33789) - [Coverity CID: 220447] Out-of-bounds access in subsys/modbus/modbus\_raw.c
- [GitHub #33788](https://github.com/zephyrproject-rtos/zephyr/issues/33788) - [Coverity CID: 220448] Out-of-bounds access in tests/subsys/modbus/src/test\_modbus\_raw.c
- [GitHub #33787](https://github.com/zephyrproject-rtos/zephyr/issues/33787) - [Coverity CID: 220449] Unused value in tests/subsys/logging/log\_backend\_fs/src/log\_fs\_test.c
- [GitHub #33786](https://github.com/zephyrproject-rtos/zephyr/issues/33786) - [Coverity CID: 220450] Untrusted loop bound in subsys/modbus/modbus\_client.c
- [GitHub #33785](https://github.com/zephyrproject-rtos/zephyr/issues/33785) - [Coverity CID: 220451] Resource leak in tests/lib/mem\_alloc/src/main.c
- [GitHub #33784](https://github.com/zephyrproject-rtos/zephyr/issues/33784) - [Coverity CID: 220452] Out-of-bounds access in subsys/net/l2/ethernet/ethernet.c
- [GitHub #33783](https://github.com/zephyrproject-rtos/zephyr/issues/33783) - [Coverity CID: 220453] Extra argument to printf format specifier in tests/lib/sprintf/src/main.c
- [GitHub #33768](https://github.com/zephyrproject-rtos/zephyr/issues/33768) - Rpmsg initialisation on nRF53 may fail
- [GitHub #33765](https://github.com/zephyrproject-rtos/zephyr/issues/33765) - Regular loss of a few connection intervals
- [GitHub #33761](https://github.com/zephyrproject-rtos/zephyr/issues/33761) - Documentation: K\_WORK\_DEFINE usage is not shown in workqueue doc
- [GitHub #33754](https://github.com/zephyrproject-rtos/zephyr/issues/33754) - xtensa sys timer Interrupt bug？
- [GitHub #33745](https://github.com/zephyrproject-rtos/zephyr/issues/33745) - `west attach` silently downgrades to `debugserver` for openocd runner
- [GitHub #33729](https://github.com/zephyrproject-rtos/zephyr/issues/33729) - flash\_write() in STM32L0 MCU throws hard fault
- [GitHub #33727](https://github.com/zephyrproject-rtos/zephyr/issues/33727) - mec15xxevb\_assy6853: multiple tests failed due to assertion failure at kernel/sched.c:841
- [GitHub #33726](https://github.com/zephyrproject-rtos/zephyr/issues/33726) - test:mimxrt1010\_evk: tests/kernel/sched/schedule\_api - kernel\_threads\_sched\_userspace cases meet out our space
- [GitHub #33721](https://github.com/zephyrproject-rtos/zephyr/issues/33721) - STM32 serial driver configure api doesn’t set correct datalength when even or odd parity is used.
- [GitHub #33712](https://github.com/zephyrproject-rtos/zephyr/issues/33712) - kernel/poll: no error happened when mutil-threads poll a same event at a same time.
- [GitHub #33702](https://github.com/zephyrproject-rtos/zephyr/issues/33702) - cfb sample build error for esp32 when SSD1306 is enabled
- [GitHub #33697](https://github.com/zephyrproject-rtos/zephyr/issues/33697) - dts:dt-bindings No OCTOSPIM dt-bindings available for stm32h723
- [GitHub #33693](https://github.com/zephyrproject-rtos/zephyr/issues/33693) - cmake -E env: unknown option ‘-Wno-unique\_unit\_address\_if\_enabled’
- [GitHub #33667](https://github.com/zephyrproject-rtos/zephyr/issues/33667) - tests: kernel: timer: Test timeout\_abs from tests/kernel/timer/timer\_api hangs causing test scenarios to fail
- [GitHub #33665](https://github.com/zephyrproject-rtos/zephyr/issues/33665) - tests: kernel: timer\_api fails with hard fault in CONFIG\_TICKLESS\_KERNEL
- [GitHub #33662](https://github.com/zephyrproject-rtos/zephyr/issues/33662) - Make twister dig deeper in directory structure to find additional .yaml files
- [GitHub #33658](https://github.com/zephyrproject-rtos/zephyr/issues/33658) - Question: How is NUM\_IRQS determined for example for STM32F401xC
- [GitHub #33655](https://github.com/zephyrproject-rtos/zephyr/issues/33655) - Add support for board: Nucleo-L412RB-P
- [GitHub #33646](https://github.com/zephyrproject-rtos/zephyr/issues/33646) - Expose net\_ipv4\_create, net\_ipv6\_create, and net\_udp\_create in standard header
- [GitHub #33645](https://github.com/zephyrproject-rtos/zephyr/issues/33645) - Random MAC after RESET - NRF52832
- [GitHub #33641](https://github.com/zephyrproject-rtos/zephyr/issues/33641) - API Meeting Minutes
- [GitHub #33635](https://github.com/zephyrproject-rtos/zephyr/issues/33635) - subsys/ipc/openamp sample on QEMU not working when debugging
- [GitHub #33633](https://github.com/zephyrproject-rtos/zephyr/issues/33633) - NXP imx rt1064 evk: Application does not boot when flash/flexSPI driver is enabled
- [GitHub #33629](https://github.com/zephyrproject-rtos/zephyr/issues/33629) - tests: subsys: logging: Tests from /tests/subsys/logging/log\_backend\_fs fail on nrf52840dk
- [GitHub #33625](https://github.com/zephyrproject-rtos/zephyr/issues/33625) - NVS: replace dev\_name parameter by device reference in nvs\_init()
- [GitHub #33612](https://github.com/zephyrproject-rtos/zephyr/issues/33612) - Add support to get adv address of a per\_adv\_sync object and lookup per\_adv\_sync object from adv address
- [GitHub #33610](https://github.com/zephyrproject-rtos/zephyr/issues/33610) - ARC: add ARCv3 HS6x support
- [GitHub #33609](https://github.com/zephyrproject-rtos/zephyr/issues/33609) - Question about memory usage of the binary zephyr.exe
- [GitHub #33600](https://github.com/zephyrproject-rtos/zephyr/issues/33600) - Master is broken at build-time when SRAM is mapped at an high address
- [GitHub #33593](https://github.com/zephyrproject-rtos/zephyr/issues/33593) - acrn\_ehl\_crb: general tests and samples execution slowdown
- [GitHub #33591](https://github.com/zephyrproject-rtos/zephyr/issues/33591) - wordlist (kobject hash) is not generated correctly when using high addresses for SRAM on 64-bit platforms
- [GitHub #33590](https://github.com/zephyrproject-rtos/zephyr/issues/33590) - nrf: Debugging any test fails when CORTEX\_M\_DEBUG\_NULL\_POINTER\_EXCEPTION\_DETECTION\_DWT is enabled
- [GitHub #33589](https://github.com/zephyrproject-rtos/zephyr/issues/33589) - SSD1306 driver no longer works for I2C displays
- [GitHub #33583](https://github.com/zephyrproject-rtos/zephyr/issues/33583) - nRF SPI CS control: CS set / release delay is longer than configured
- [GitHub #33572](https://github.com/zephyrproject-rtos/zephyr/issues/33572) - <err> esp\_event: SYSTEM\_EVENT\_STA\_DISCONNECTED for wifi sample for esp32 board
- [GitHub #33568](https://github.com/zephyrproject-rtos/zephyr/issues/33568) - Test tests/arch/x86/info fails for ehl\_crb
- [GitHub #33567](https://github.com/zephyrproject-rtos/zephyr/issues/33567) - sof: framework is redefnining MAX, MIN to version with limited capabilities
- [GitHub #33559](https://github.com/zephyrproject-rtos/zephyr/issues/33559) - pin setting error on frdm\_kl25z boards
- [GitHub #33558](https://github.com/zephyrproject-rtos/zephyr/issues/33558) - qemu\_cortex\_a53\_smp and qemu\_x86\_64 failed in tests/kernel/condvar/condvar while enabling for SMP
- [GitHub #33557](https://github.com/zephyrproject-rtos/zephyr/issues/33557) - there is no network interface to work with for wifi sample for esp32 board
- [GitHub #33551](https://github.com/zephyrproject-rtos/zephyr/issues/33551) - tests: SMP: Two threads synchronize failed using mutex or semaphore while both doing irq\_lock()
- [GitHub #33549](https://github.com/zephyrproject-rtos/zephyr/issues/33549) - xt-xcc unknown field ‘obj’ specified in initializer
- [GitHub #33548](https://github.com/zephyrproject-rtos/zephyr/issues/33548) - xt-xcc does not support deprecated attribute
- [GitHub #33545](https://github.com/zephyrproject-rtos/zephyr/issues/33545) - ehl\_crb: tests/arch/x86/info failed.
- [GitHub #33544](https://github.com/zephyrproject-rtos/zephyr/issues/33544) - ehl\_crb: portability.posix.common.posix\_realtime failed.
- [GitHub #33543](https://github.com/zephyrproject-rtos/zephyr/issues/33543) - ehl\_crb: tests/subsys/edac/ibecc failed.
- [GitHub #33542](https://github.com/zephyrproject-rtos/zephyr/issues/33542) - reel\_board: samples/subsys/usb/hid/ timeout failure
- [GitHub #33539](https://github.com/zephyrproject-rtos/zephyr/issues/33539) - ehl\_crb: tests/kernel/mem\_heap/mheap\_api\_concept failed.
- [GitHub #33529](https://github.com/zephyrproject-rtos/zephyr/issues/33529) - adafruit\_feather\_nrf52840 dts not setting I2C controller compat (was: SSD1306 DTS properties not being generated in devicetree\_unfixed.h)
- [GitHub #33526](https://github.com/zephyrproject-rtos/zephyr/issues/33526) - boards: Optimal way to have customized dts for my project.
- [GitHub #33525](https://github.com/zephyrproject-rtos/zephyr/issues/33525) - ST Nucleo G071RB board support issue
- [GitHub #33524](https://github.com/zephyrproject-rtos/zephyr/issues/33524) - minor: kswap.h is included twice in kernel/init.c
- [GitHub #33523](https://github.com/zephyrproject-rtos/zephyr/issues/33523) - Bossac runner flashes at an incorrect offset
- [GitHub #33516](https://github.com/zephyrproject-rtos/zephyr/issues/33516) - socket: tcp application crashes when there are no more net buffers in case of reception
- [GitHub #33515](https://github.com/zephyrproject-rtos/zephyr/issues/33515) - arm64/mmu: Are you sure it’s OK to use atomic\_cas before the MMU is initialized?
- [GitHub #33512](https://github.com/zephyrproject-rtos/zephyr/issues/33512) - build: build target is always out-of-date
- [GitHub #33509](https://github.com/zephyrproject-rtos/zephyr/issues/33509) - samples: tests: watchdog: samples/subsys/task\_wdt breaks nrf platforms performace
- [GitHub #33505](https://github.com/zephyrproject-rtos/zephyr/issues/33505) - WS2812 SPI LED driver with DMA on nrf52 bad SPI data
- [GitHub #33498](https://github.com/zephyrproject-rtos/zephyr/issues/33498) - west: Question on `west flash --hex-file` behavior with build.dir-fmt
- [GitHub #33491](https://github.com/zephyrproject-rtos/zephyr/issues/33491) - fwrite() function will cause the program to crash when wrong parameters passed
- [GitHub #33488](https://github.com/zephyrproject-rtos/zephyr/issues/33488) - Ring buffer makes it hard to discard items
- [GitHub #33479](https://github.com/zephyrproject-rtos/zephyr/issues/33479) - disk\_access\_spi\_sdhc: Missing stop/end bit
- [GitHub #33475](https://github.com/zephyrproject-rtos/zephyr/issues/33475) - Need to add device node for UART10 in dts/arm/st/h7/stm32h723.dtsi
- [GitHub #33464](https://github.com/zephyrproject-rtos/zephyr/issues/33464) - SYS\_INIT initialize priority “2-9” ordering error
- [GitHub #33459](https://github.com/zephyrproject-rtos/zephyr/issues/33459) - Divide zero exception is not enabled in ARC
- [GitHub #33457](https://github.com/zephyrproject-rtos/zephyr/issues/33457) - Fail to build ARC zephyr with MetaWare toolchain
- [GitHub #33456](https://github.com/zephyrproject-rtos/zephyr/issues/33456) - lorawan: unconfirmed messages leave stack in busy state
- [GitHub #33426](https://github.com/zephyrproject-rtos/zephyr/issues/33426) - a few failures with CONFIG\_HCI\_ACL\_DATA\_SIZE in nightly builds
- [GitHub #33424](https://github.com/zephyrproject-rtos/zephyr/issues/33424) - tests: ztest: Test from tests/ztest/error\_hook fails on nrf5340dk\_nrf5340\_cpuappns
- [GitHub #33423](https://github.com/zephyrproject-rtos/zephyr/issues/33423) - tests: portability: tests/portability/cmsis\_rtos\_v2 fails on nrf5340dk\_nrf5340\_cpuappns
- [GitHub #33422](https://github.com/zephyrproject-rtos/zephyr/issues/33422) - samples/subsys/usb/dfu/sample.usb.dfu fails on multiple platforms in daily build
- [GitHub #33421](https://github.com/zephyrproject-rtos/zephyr/issues/33421) - Add BT\_LE\_FEAT\_BIT\_PER\_ADV checks for periodic advertising commands
- [GitHub #33403](https://github.com/zephyrproject-rtos/zephyr/issues/33403) - trigger\_fault\_divide\_zero test case didn’t run divide instruction
- [GitHub #33381](https://github.com/zephyrproject-rtos/zephyr/issues/33381) - West debug does not work with Bluetooth shell and nRF52840 DK
- [GitHub #33378](https://github.com/zephyrproject-rtos/zephyr/issues/33378) - Extended advertising switch on / switch off loop impossible
- [GitHub #33374](https://github.com/zephyrproject-rtos/zephyr/issues/33374) - Network interface routines are not thread safe
- [GitHub #33371](https://github.com/zephyrproject-rtos/zephyr/issues/33371) - mec15xxevb\_assy6853: tests/drivers/gpio/gpio\_basic\_api/ failed
- [GitHub #33365](https://github.com/zephyrproject-rtos/zephyr/issues/33365) - Add STM32H7 Series USB Device Support
- [GitHub #33363](https://github.com/zephyrproject-rtos/zephyr/issues/33363) - Properly indicate ISR number in SystemView
- [GitHub #33356](https://github.com/zephyrproject-rtos/zephyr/issues/33356) - Using AT HOST fails build
- [GitHub #33353](https://github.com/zephyrproject-rtos/zephyr/issues/33353) - work: k\_work\_schedule from running work item does not schedule
- [GitHub #33352](https://github.com/zephyrproject-rtos/zephyr/issues/33352) - Arduino Nano 33 BLE sense constantly resetting.
- [GitHub #33351](https://github.com/zephyrproject-rtos/zephyr/issues/33351) - uart peripheral outputs 7 bits when configured in 8 bits + parity on stm32
- [GitHub #33348](https://github.com/zephyrproject-rtos/zephyr/issues/33348) - ip/dhcpv4 is not thread-safe in SMP/preemptive thread configurations
- [GitHub #33342](https://github.com/zephyrproject-rtos/zephyr/issues/33342) - disco\_l475\_iot1: Multiple definitions of z\_timer\_cycle\_get\_32, etc.
- [GitHub #33339](https://github.com/zephyrproject-rtos/zephyr/issues/33339) - API/functions to get remaining free heap size
- [GitHub #33330](https://github.com/zephyrproject-rtos/zephyr/issues/33330) - Poll on DTLS socket returns -EAGAIN if bind & receive any data.
- [GitHub #33326](https://github.com/zephyrproject-rtos/zephyr/issues/33326) - The gpio-map for adafruit\_feather\_stm32f405 looks like it contains conflicts
- [GitHub #33324](https://github.com/zephyrproject-rtos/zephyr/issues/33324) - Using bluetooth hci\_usb sample, and set periodic adv enable, but bluez still shows no command supported
- [GitHub #33322](https://github.com/zephyrproject-rtos/zephyr/issues/33322) - Questions on ztest : 1) Can twister/ztests run on windows? 2) Project structure
- [GitHub #33319](https://github.com/zephyrproject-rtos/zephyr/issues/33319) - Kernel doesn’t validate lock state on swap
- [GitHub #33318](https://github.com/zephyrproject-rtos/zephyr/issues/33318) - [Coverity CID: 219722] Resource leak in tests/lib/mem\_alloc/src/main.c
- [GitHub #33317](https://github.com/zephyrproject-rtos/zephyr/issues/33317) - [Coverity CID: 219727] Improper use of negative value in tests/lib/cbprintf\_package/src/main.c
- [GitHub #33316](https://github.com/zephyrproject-rtos/zephyr/issues/33316) - [Coverity CID: 219724] Side effect in assertion in tests/kernel/queue/src/test\_queue\_contexts.c
- [GitHub #33315](https://github.com/zephyrproject-rtos/zephyr/issues/33315) - [Coverity CID: 219723] Side effect in assertion in tests/kernel/queue/src/test\_queue\_contexts.c
- [GitHub #33314](https://github.com/zephyrproject-rtos/zephyr/issues/33314) - [Coverity CID: 219726] Side effect in assertion in tests/kernel/lifo/lifo\_usage/src/main.c
- [GitHub #33313](https://github.com/zephyrproject-rtos/zephyr/issues/33313) - [Coverity CID: 219728] Untrusted array index read in subsys/bluetooth/host/iso.c
- [GitHub #33312](https://github.com/zephyrproject-rtos/zephyr/issues/33312) - [Coverity CID: 219721] Untrusted array index read in subsys/bluetooth/host/iso.c
- [GitHub #33311](https://github.com/zephyrproject-rtos/zephyr/issues/33311) - [Coverity CID: 219729] Logically dead code in lib/os/cbprintf\_packaged.c
- [GitHub #33303](https://github.com/zephyrproject-rtos/zephyr/issues/33303) - \_\_ASSERT does not display message or register info in v2.5.0
- [GitHub #33291](https://github.com/zephyrproject-rtos/zephyr/issues/33291) - Using both NET\_SOCKETS\_SOCKOPT\_TLS and POSIX\_API fails build
- [GitHub #33280](https://github.com/zephyrproject-rtos/zephyr/issues/33280) - drivers: serial: nrf uarte: The application receives one more byte that was received over UART
- [GitHub #33273](https://github.com/zephyrproject-rtos/zephyr/issues/33273) - The z\_smp\_reacquire\_global\_lock() internal API is not used any where inside zephyr code base
- [GitHub #33269](https://github.com/zephyrproject-rtos/zephyr/issues/33269) - ILI9341 (ILI9XXX) set orientation function fails to update the display area correctly
- [GitHub #33265](https://github.com/zephyrproject-rtos/zephyr/issues/33265) - Power Management Overhaul
- [GitHub #33261](https://github.com/zephyrproject-rtos/zephyr/issues/33261) - gatt\_notify too slow on Broadcast
- [GitHub #33253](https://github.com/zephyrproject-rtos/zephyr/issues/33253) - STM32G4 with USB-C PD: Some pins cannot be used as input by default
- [GitHub #33239](https://github.com/zephyrproject-rtos/zephyr/issues/33239) - lib/rbtree: Remove dead case in rb\_remove()
- [GitHub #33238](https://github.com/zephyrproject-rtos/zephyr/issues/33238) - tests: drivers: pwm api fails on many boards
- [GitHub #33233](https://github.com/zephyrproject-rtos/zephyr/issues/33233) - uart9 missing from <st/h7/stm32h7.dtsi>
- [GitHub #33218](https://github.com/zephyrproject-rtos/zephyr/issues/33218) - Incorrect documentation CONFIG\_LOG\_STRDUP\_MAX\_STRING
- [GitHub #33213](https://github.com/zephyrproject-rtos/zephyr/issues/33213) - Configuring a project with a sub-project (e.g. nRF5340) and an overlay causes an infinite configuring loop
- [GitHub #33212](https://github.com/zephyrproject-rtos/zephyr/issues/33212) - GUI configuration system (ninja menuconfig) exists with an error when the windows key is pressed
- [GitHub #33208](https://github.com/zephyrproject-rtos/zephyr/issues/33208) - cbprintf: Package size calculation is using best case alignment
- [GitHub #33207](https://github.com/zephyrproject-rtos/zephyr/issues/33207) - twister: Add option to load list with quarantined tests
- [GitHub #33203](https://github.com/zephyrproject-rtos/zephyr/issues/33203) - Bluetooth: host: ISO: Missing terminate reason in ISO disconnected callback
- [GitHub #33200](https://github.com/zephyrproject-rtos/zephyr/issues/33200) - USB CDC ACM sample application fails to compile
- [GitHub #33196](https://github.com/zephyrproject-rtos/zephyr/issues/33196) - I2C doesn’t work on STM32F103RE
- [GitHub #33185](https://github.com/zephyrproject-rtos/zephyr/issues/33185) - TCP traffic with IPSP sample not working on 96Boards Nitrogen
- [GitHub #33176](https://github.com/zephyrproject-rtos/zephyr/issues/33176) - tests: kernel: Multiple test cases from tests/kernel/workq/work\_queue are failing
- [GitHub #33173](https://github.com/zephyrproject-rtos/zephyr/issues/33173) - tests/kernel/workq/work\_queue fails on sam\_e70\_xplained
- [GitHub #33171](https://github.com/zephyrproject-rtos/zephyr/issues/33171) - Create Renesas HAL
- [GitHub #33169](https://github.com/zephyrproject-rtos/zephyr/issues/33169) - STM32 SPI Driver - Transmit (MOSI) Only - Infinite Loop on Tranceive
- [GitHub #33168](https://github.com/zephyrproject-rtos/zephyr/issues/33168) - CONFIG\_HEAP\_MEM\_POOL\_SIZE=64 doesn’t work
- [GitHub #33164](https://github.com/zephyrproject-rtos/zephyr/issues/33164) - Newlib has no synchronization
- [GitHub #33153](https://github.com/zephyrproject-rtos/zephyr/issues/33153) - west flash cannot find OpenOCD
- [GitHub #33149](https://github.com/zephyrproject-rtos/zephyr/issues/33149) - subsys: canbus: canopen EDSEditor / libedssharp version that works with Zephyr’s CANopenNode
- [GitHub #33147](https://github.com/zephyrproject-rtos/zephyr/issues/33147) - Not able to build blinky or set toolchain to zephyr
- [GitHub #33142](https://github.com/zephyrproject-rtos/zephyr/issues/33142) - fs\_mount for FAT FS does not distingush between no file system and other errors
- [GitHub #33140](https://github.com/zephyrproject-rtos/zephyr/issues/33140) - STM32H7: Bus fault when reading corrupt flash sectors
- [GitHub #33138](https://github.com/zephyrproject-rtos/zephyr/issues/33138) - invalid west cmake diagnostics when using board alias
- [GitHub #33137](https://github.com/zephyrproject-rtos/zephyr/issues/33137) - Enabling DHCP without NET\_MGMT shouldn’t be allowed
- [GitHub #33127](https://github.com/zephyrproject-rtos/zephyr/issues/33127) - Improve documentation user experience
- [GitHub #33122](https://github.com/zephyrproject-rtos/zephyr/issues/33122) - Device-level Cache API
- [GitHub #33120](https://github.com/zephyrproject-rtos/zephyr/issues/33120) - iotdk: running testcase tests/kernel/mbox/mbox\_api/ failed
- [GitHub #33114](https://github.com/zephyrproject-rtos/zephyr/issues/33114) - tests: mbox\_api: testcase test\_mbox\_data\_get\_null has some bugs.
- [GitHub #33104](https://github.com/zephyrproject-rtos/zephyr/issues/33104) - Updating Zephyr to fix Work Queue Problems
- [GitHub #33101](https://github.com/zephyrproject-rtos/zephyr/issues/33101) - DNS resolver misbehaves if receiving response too late
- [GitHub #33100](https://github.com/zephyrproject-rtos/zephyr/issues/33100) - tcp2 not working with ppp
- [GitHub #33097](https://github.com/zephyrproject-rtos/zephyr/issues/33097) - Coverity ID links in associated GitHub issues are broken
- [GitHub #33096](https://github.com/zephyrproject-rtos/zephyr/issues/33096) - [Coverity CID :215373] Unchecked return value in subsys/net/lib/lwm2m/lwm2m\_rd\_client.c
- [GitHub #33095](https://github.com/zephyrproject-rtos/zephyr/issues/33095) - [Coverity CID :215379] Out-of-bounds write in subsys/mgmt/osdp/src/osdp\_cp.c
- [GitHub #33094](https://github.com/zephyrproject-rtos/zephyr/issues/33094) - [Coverity CID :215381] Resource leak in samples/net/mdns\_responder/src/service.c
- [GitHub #33093](https://github.com/zephyrproject-rtos/zephyr/issues/33093) - [Coverity CID :215391] Unchecked return value from library in samples/net/mdns\_responder/src/service.c
- [GitHub #33092](https://github.com/zephyrproject-rtos/zephyr/issues/33092) - [Coverity CID :215392] Logically dead code in subsys/mgmt/osdp/src/osdp\_cp.c
- [GitHub #33091](https://github.com/zephyrproject-rtos/zephyr/issues/33091) - [Coverity CID :219474] Logically dead code in subsys/bluetooth/controller/ll\_sw/ull\_scan.c
- [GitHub #33090](https://github.com/zephyrproject-rtos/zephyr/issues/33090) - [Coverity CID :219476] Dereference after null check in subsys/bluetooth/controller/ll\_sw/ull\_conn.c
- [GitHub #33089](https://github.com/zephyrproject-rtos/zephyr/issues/33089) - [Coverity CID :219556] Self assignment in drivers/espi/host\_subs\_npcx.c
- [GitHub #33088](https://github.com/zephyrproject-rtos/zephyr/issues/33088) - [Coverity CID :219558] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33087](https://github.com/zephyrproject-rtos/zephyr/issues/33087) - [Coverity CID :219559] Out-of-bounds access in tests/arch/arm/arm\_interrupt/src/arm\_interrupt.c
- [GitHub #33086](https://github.com/zephyrproject-rtos/zephyr/issues/33086) - [Coverity CID :219561] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33085](https://github.com/zephyrproject-rtos/zephyr/issues/33085) - [Coverity CID :219562] Out-of-bounds access in tests/bluetooth/tester/src/gatt.c
- [GitHub #33084](https://github.com/zephyrproject-rtos/zephyr/issues/33084) - [Coverity CID :219563] Dereference after null check in arch/x86/core/multiboot.c
- [GitHub #33083](https://github.com/zephyrproject-rtos/zephyr/issues/33083) - [Coverity CID :219564] Untrusted value as argument in subsys/net/lib/lwm2m/lwm2m\_engine.c
- [GitHub #33082](https://github.com/zephyrproject-rtos/zephyr/issues/33082) - [Coverity CID :219566] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33081](https://github.com/zephyrproject-rtos/zephyr/issues/33081) - [Coverity CID :219572] Untrusted value as argument in tests/net/lib/coap/src/main.c
- [GitHub #33080](https://github.com/zephyrproject-rtos/zephyr/issues/33080) - [Coverity CID :219573] Untrusted value as argument in samples/net/sockets/coap\_client/src/coap-client.c
- [GitHub #33079](https://github.com/zephyrproject-rtos/zephyr/issues/33079) - [Coverity CID :219574] Side effect in assertion in tests/subsys/edac/ibecc/src/ibecc.c
- [GitHub #33078](https://github.com/zephyrproject-rtos/zephyr/issues/33078) - [Coverity CID :219576] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33077](https://github.com/zephyrproject-rtos/zephyr/issues/33077) - [Coverity CID :219579] Out-of-bounds read in drivers/ipm/ipm\_nrfx\_ipc.c
- [GitHub #33076](https://github.com/zephyrproject-rtos/zephyr/issues/33076) - [Coverity CID :219583] Operands don’t affect result in drivers/clock\_control/clock\_control\_npcx.c
- [GitHub #33075](https://github.com/zephyrproject-rtos/zephyr/issues/33075) - [Coverity CID :219588] Out-of-bounds access in tests/bluetooth/tester/src/gatt.c
- [GitHub #33074](https://github.com/zephyrproject-rtos/zephyr/issues/33074) - [Coverity CID :219590] Unchecked return value in subsys/bluetooth/mesh/proxy.c
- [GitHub #33073](https://github.com/zephyrproject-rtos/zephyr/issues/33073) - [Coverity CID :219591] Untrusted divisor in drivers/sensor/bme680/bme680.c
- [GitHub #33072](https://github.com/zephyrproject-rtos/zephyr/issues/33072) - [Coverity CID :219593] Logically dead code in tests/arch/x86/pagetables/src/main.c
- [GitHub #33071](https://github.com/zephyrproject-rtos/zephyr/issues/33071) - [Coverity CID :219595] Dereference before null check in subsys/net/ip/net\_context.c
- [GitHub #33070](https://github.com/zephyrproject-rtos/zephyr/issues/33070) - [Coverity CID :219596] Out-of-bounds read in tests/kernel/interrupt/src/dynamic\_isr.c
- [GitHub #33069](https://github.com/zephyrproject-rtos/zephyr/issues/33069) - [Coverity CID :219597] Untrusted value as argument in tests/net/lib/coap/src/main.c
- [GitHub #33068](https://github.com/zephyrproject-rtos/zephyr/issues/33068) - [Coverity CID :219598] Out-of-bounds access in tests/bluetooth/tester/src/gatt.c
- [GitHub #33067](https://github.com/zephyrproject-rtos/zephyr/issues/33067) - [Coverity CID :219600] Unchecked return value in drivers/watchdog/wdt\_wwdg\_stm32.c
- [GitHub #33066](https://github.com/zephyrproject-rtos/zephyr/issues/33066) - [Coverity CID :219601] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33065](https://github.com/zephyrproject-rtos/zephyr/issues/33065) - [Coverity CID :219603] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33064](https://github.com/zephyrproject-rtos/zephyr/issues/33064) - [Coverity CID :219608] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33063](https://github.com/zephyrproject-rtos/zephyr/issues/33063) - [Coverity CID :219609] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33062](https://github.com/zephyrproject-rtos/zephyr/issues/33062) - [Coverity CID :219610] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33061](https://github.com/zephyrproject-rtos/zephyr/issues/33061) - [Coverity CID :219611] Dereference after null check in subsys/net/ip/tcp2.c
- [GitHub #33060](https://github.com/zephyrproject-rtos/zephyr/issues/33060) - [Coverity CID :219613] Uninitialized scalar variable in lib/cmsis\_rtos\_v1/cmsis\_signal.c
- [GitHub #33059](https://github.com/zephyrproject-rtos/zephyr/issues/33059) - [Coverity CID :219615] Out-of-bounds access in tests/arch/arm/arm\_irq\_advanced\_features/src/arm\_zero\_latency\_irqs.c
- [GitHub #33058](https://github.com/zephyrproject-rtos/zephyr/issues/33058) - [Coverity CID :219616] Untrusted value as argument in subsys/net/lib/coap/coap\_link\_format.c
- [GitHub #33057](https://github.com/zephyrproject-rtos/zephyr/issues/33057) - [Coverity CID :219619] Untrusted divisor in subsys/bluetooth/controller/hci/hci.c
- [GitHub #33056](https://github.com/zephyrproject-rtos/zephyr/issues/33056) - [Coverity CID :219620] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33055](https://github.com/zephyrproject-rtos/zephyr/issues/33055) - [Coverity CID :219621] Uninitialized scalar variable in tests/net/socket/getaddrinfo/src/main.c
- [GitHub #33054](https://github.com/zephyrproject-rtos/zephyr/issues/33054) - [Coverity CID :219622] Untrusted value as argument in subsys/net/lib/coap/coap.c
- [GitHub #33053](https://github.com/zephyrproject-rtos/zephyr/issues/33053) - [Coverity CID :219623] Out-of-bounds read in drivers/ipm/ipm\_nrfx\_ipc.c
- [GitHub #33051](https://github.com/zephyrproject-rtos/zephyr/issues/33051) - [Coverity CID :219625] Unchecked return value in subsys/bluetooth/mesh/proxy.c
- [GitHub #33050](https://github.com/zephyrproject-rtos/zephyr/issues/33050) - [Coverity CID :219628] Untrusted value as argument in subsys/net/lib/lwm2m/lwm2m\_engine.c
- [GitHub #33049](https://github.com/zephyrproject-rtos/zephyr/issues/33049) - [Coverity CID :219629] Operands don’t affect result in drivers/clock\_control/clock\_control\_npcx.c
- [GitHub #33048](https://github.com/zephyrproject-rtos/zephyr/issues/33048) - [Coverity CID :219631] Out-of-bounds read in drivers/espi/espi\_npcx.c
- [GitHub #33047](https://github.com/zephyrproject-rtos/zephyr/issues/33047) - [Coverity CID :219634] Out-of-bounds access in tests/net/lib/dns\_addremove/src/main.c
- [GitHub #33046](https://github.com/zephyrproject-rtos/zephyr/issues/33046) - [Coverity CID :219636] Untrusted value as argument in subsys/net/lib/lwm2m/lwm2m\_engine.c
- [GitHub #33045](https://github.com/zephyrproject-rtos/zephyr/issues/33045) - [Coverity CID :219637] Untrusted value as argument in tests/net/lib/coap/src/main.c
- [GitHub #33044](https://github.com/zephyrproject-rtos/zephyr/issues/33044) - [Coverity CID :219638] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33043](https://github.com/zephyrproject-rtos/zephyr/issues/33043) - [Coverity CID :219641] Out-of-bounds access in tests/bluetooth/tester/src/gatt.c
- [GitHub #33042](https://github.com/zephyrproject-rtos/zephyr/issues/33042) - [Coverity CID :219644] Side effect in assertion in tests/subsys/edac/ibecc/src/ibecc.c
- [GitHub #33040](https://github.com/zephyrproject-rtos/zephyr/issues/33040) - [Coverity CID :219646] Untrusted value as argument in subsys/net/lib/coap/coap.c
- [GitHub #33039](https://github.com/zephyrproject-rtos/zephyr/issues/33039) - [Coverity CID :219647] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33038](https://github.com/zephyrproject-rtos/zephyr/issues/33038) - [Coverity CID :219649] Operands don’t affect result in kernel/sem.c
- [GitHub #33037](https://github.com/zephyrproject-rtos/zephyr/issues/33037) - [Coverity CID :219650] Out-of-bounds access in samples/bluetooth/central\_ht/src/main.c
- [GitHub #33036](https://github.com/zephyrproject-rtos/zephyr/issues/33036) - [Coverity CID :219651] Logically dead code in subsys/bluetooth/mesh/net.c
- [GitHub #33035](https://github.com/zephyrproject-rtos/zephyr/issues/33035) - [Coverity CID :219652] Unchecked return value in drivers/gpio/gpio\_stm32.c
- [GitHub #33034](https://github.com/zephyrproject-rtos/zephyr/issues/33034) - [Coverity CID :219653] Unchecked return value in drivers/modem/hl7800.c
- [GitHub #33033](https://github.com/zephyrproject-rtos/zephyr/issues/33033) - [Coverity CID :219654] Out-of-bounds access in tests/net/lib/dns\_addremove/src/main.c
- [GitHub #33032](https://github.com/zephyrproject-rtos/zephyr/issues/33032) - [Coverity CID :219656] Uninitialized scalar variable in tests/kernel/threads/thread\_stack/src/main.c
- [GitHub #33031](https://github.com/zephyrproject-rtos/zephyr/issues/33031) - [Coverity CID :219658] Untrusted value as argument in samples/net/sockets/coap\_client/src/coap-client.c
- [GitHub #33030](https://github.com/zephyrproject-rtos/zephyr/issues/33030) - [Coverity CID :219659] Side effect in assertion in tests/subsys/edac/ibecc/src/ibecc.c
- [GitHub #33029](https://github.com/zephyrproject-rtos/zephyr/issues/33029) - [Coverity CID :219660] Untrusted divisor in drivers/sensor/bme680/bme680.c
- [GitHub #33028](https://github.com/zephyrproject-rtos/zephyr/issues/33028) - [Coverity CID :219661] Unchecked return value in subsys/bluetooth/host/gatt.c
- [GitHub #33027](https://github.com/zephyrproject-rtos/zephyr/issues/33027) - [Coverity CID :219662] Inequality comparison against NULL in lib/os/cbprintf\_packaged.c
- [GitHub #33026](https://github.com/zephyrproject-rtos/zephyr/issues/33026) - [Coverity CID :219666] Out-of-bounds access in tests/bluetooth/tester/src/gatt.c
- [GitHub #33025](https://github.com/zephyrproject-rtos/zephyr/issues/33025) - [Coverity CID :219667] Untrusted value as argument in tests/net/lib/coap/src/main.c
- [GitHub #33024](https://github.com/zephyrproject-rtos/zephyr/issues/33024) - [Coverity CID :219668] Dereference after null check in drivers/espi/host\_subs\_npcx.c
- [GitHub #33023](https://github.com/zephyrproject-rtos/zephyr/issues/33023) - [Coverity CID :219669] Untrusted value as argument in subsys/mgmt/updatehub/updatehub.c
- [GitHub #33022](https://github.com/zephyrproject-rtos/zephyr/issues/33022) - [Coverity CID :219672] Untrusted value as argument in samples/net/sockets/coap\_server/src/coap-server.c
- [GitHub #33021](https://github.com/zephyrproject-rtos/zephyr/issues/33021) - [Coverity CID :219673] Untrusted value as argument in samples/net/sockets/coap\_client/src/coap-client.c
- [GitHub #33020](https://github.com/zephyrproject-rtos/zephyr/issues/33020) - [Coverity CID :219675] Macro compares unsigned to 0 in kernel/include/mmu.h
- [GitHub #33019](https://github.com/zephyrproject-rtos/zephyr/issues/33019) - [Coverity CID :219676] Unchecked return value in drivers/modem/wncm14a2a.c
- [GitHub #33018](https://github.com/zephyrproject-rtos/zephyr/issues/33018) - [Coverity CID :219677] Logically dead code in drivers/timer/npcx\_itim\_timer.c
- [GitHub #33009](https://github.com/zephyrproject-rtos/zephyr/issues/33009) - kernel: k\_heap failures on small heaps
- [GitHub #33001](https://github.com/zephyrproject-rtos/zephyr/issues/33001) - stm32: window watchdog (wwdg): setup of prescaler not valid for newer series
- [GitHub #33000](https://github.com/zephyrproject-rtos/zephyr/issues/33000) - stm32: window watchdog (wwdg): invalid interrupts priority for CM0 Series Socs
- [GitHub #32996](https://github.com/zephyrproject-rtos/zephyr/issues/32996) - SPI speed when using SDHC via SPI in Zephyr
- [GitHub #32994](https://github.com/zephyrproject-rtos/zephyr/issues/32994) - Question: Possible simplification in mutex.h?
- [GitHub #32975](https://github.com/zephyrproject-rtos/zephyr/issues/32975) - Where should a few include/ headers live
- [GitHub #32969](https://github.com/zephyrproject-rtos/zephyr/issues/32969) - Wrong board target in microbit v2 documentation
- [GitHub #32966](https://github.com/zephyrproject-rtos/zephyr/issues/32966) - frdm\_k64f: Run some testcases timeout failed by using twister
- [GitHub #32963](https://github.com/zephyrproject-rtos/zephyr/issues/32963) - USB device is not supported by qemu\_x86 platform
- [GitHub #32961](https://github.com/zephyrproject-rtos/zephyr/issues/32961) - [Coverity CID :219478] Unchecked return value in subsys/bluetooth/controller/ll\_sw/ull\_filter.c
- [GitHub #32960](https://github.com/zephyrproject-rtos/zephyr/issues/32960) - [Coverity CID :219479] Out-of-bounds access in subsys/net/l2/bluetooth/bluetooth.c
- [GitHub #32959](https://github.com/zephyrproject-rtos/zephyr/issues/32959) - [Coverity CID :219480] Out-of-bounds read in lib/os/cbprintf\_nano.c
- [GitHub #32958](https://github.com/zephyrproject-rtos/zephyr/issues/32958) - [Coverity CID :219481] Out-of-bounds access in subsys/bluetooth/controller/ll\_sw/nordic/lll/lll\_adv\_aux.c
- [GitHub #32957](https://github.com/zephyrproject-rtos/zephyr/issues/32957) - [Coverity CID :219483] Improper use of negative value in tests/drivers/timer/nrf\_rtc\_timer/src/main.c
- [GitHub #32956](https://github.com/zephyrproject-rtos/zephyr/issues/32956) - [Coverity CID :219484] Out-of-bounds access in tests/drivers/timer/nrf\_rtc\_timer/src/main.c
- [GitHub #32955](https://github.com/zephyrproject-rtos/zephyr/issues/32955) - [Coverity CID :219485] Logically dead code in subsys/bluetooth/controller/ll\_sw/ull.c
- [GitHub #32954](https://github.com/zephyrproject-rtos/zephyr/issues/32954) - [Coverity CID :219486] Unrecoverable parse warning in tests/kernel/mem\_protect/mem\_protect/src/mem\_domain.c
- [GitHub #32953](https://github.com/zephyrproject-rtos/zephyr/issues/32953) - [Coverity CID :219487] Resource leak in tests/net/socket/getaddrinfo/src/main.c
- [GitHub #32952](https://github.com/zephyrproject-rtos/zephyr/issues/32952) - [Coverity CID :219488] Unrecoverable parse warning in tests/kernel/mem\_protect/mem\_protect/src/mem\_domain.c
- [GitHub #32951](https://github.com/zephyrproject-rtos/zephyr/issues/32951) - [Coverity CID :219489] Structurally dead code in tests/drivers/dma/loop\_transfer/src/test\_dma\_loop.c
- [GitHub #32950](https://github.com/zephyrproject-rtos/zephyr/issues/32950) - [Coverity CID :219490] Unsigned compared against 0 in drivers/wifi/esp/esp.c
- [GitHub #32949](https://github.com/zephyrproject-rtos/zephyr/issues/32949) - [Coverity CID :219491] Resource leak in tests/net/socket/af\_packet/src/main.c
- [GitHub #32948](https://github.com/zephyrproject-rtos/zephyr/issues/32948) - [Coverity CID :219492] Out-of-bounds access in tests/drivers/timer/nrf\_rtc\_timer/src/main.c
- [GitHub #32947](https://github.com/zephyrproject-rtos/zephyr/issues/32947) - [Coverity CID :219493] Unchecked return value in tests/kernel/workq/work/src/main.c
- [GitHub #32946](https://github.com/zephyrproject-rtos/zephyr/issues/32946) - [Coverity CID :219494] Logically dead code in boards/xtensa/intel\_s1000\_crb/pinmux.c
- [GitHub #32945](https://github.com/zephyrproject-rtos/zephyr/issues/32945) - [Coverity CID :219495] Pointless string comparison in tests/lib/devicetree/api/src/main.c
- [GitHub #32944](https://github.com/zephyrproject-rtos/zephyr/issues/32944) - [Coverity CID :219497] Logically dead code in subsys/bluetooth/host/gatt.c
- [GitHub #32943](https://github.com/zephyrproject-rtos/zephyr/issues/32943) - [Coverity CID :219498] Out-of-bounds access in tests/drivers/timer/nrf\_rtc\_timer/src/main.c
- [GitHub #32942](https://github.com/zephyrproject-rtos/zephyr/issues/32942) - [Coverity CID :219499] Argument cannot be negative in tests/net/socket/af\_packet/src/main.c
- [GitHub #32941](https://github.com/zephyrproject-rtos/zephyr/issues/32941) - [Coverity CID :219501] Unchecked return value in subsys/net/l2/bluetooth/bluetooth.c
- [GitHub #32940](https://github.com/zephyrproject-rtos/zephyr/issues/32940) - [Coverity CID :219502] Improper use of negative value in tests/net/socket/af\_packet/src/main.c
- [GitHub #32939](https://github.com/zephyrproject-rtos/zephyr/issues/32939) - [Coverity CID :219504] Logically dead code in subsys/net/lib/lwm2m/lwm2m\_engine.c
- [GitHub #32938](https://github.com/zephyrproject-rtos/zephyr/issues/32938) - [Coverity CID :219508] Unchecked return value in lib/libc/minimal/source/stdlib/malloc.c
- [GitHub #32937](https://github.com/zephyrproject-rtos/zephyr/issues/32937) - [Coverity CID :219508] Unchecked return value in lib/libc/minimal/source/stdlib/malloc.c
- [GitHub #32936](https://github.com/zephyrproject-rtos/zephyr/issues/32936) - [Coverity CID :219509] Side effect in assertion in tests/net/socket/tcp/src/main.c
- [GitHub #32935](https://github.com/zephyrproject-rtos/zephyr/issues/32935) - [Coverity CID :219510] Improper use of negative value in tests/drivers/timer/nrf\_rtc\_timer/src/main.c
- [GitHub #32934](https://github.com/zephyrproject-rtos/zephyr/issues/32934) - [Coverity CID :219511] Uninitialized scalar variable in tests/kernel/mbox/mbox\_api/src/test\_mbox\_api.c
- [GitHub #32933](https://github.com/zephyrproject-rtos/zephyr/issues/32933) - [Coverity CID :219512] Unrecoverable parse warning in tests/kernel/mem\_protect/mem\_protect/src/mem\_domain.c
- [GitHub #32932](https://github.com/zephyrproject-rtos/zephyr/issues/32932) - [Coverity CID :219513] Logically dead code in drivers/wifi/esp/esp.c
- [GitHub #32931](https://github.com/zephyrproject-rtos/zephyr/issues/32931) - [Coverity CID :219514] Out-of-bounds access in tests/drivers/timer/nrf\_rtc\_timer/src/main.c
- [GitHub #32930](https://github.com/zephyrproject-rtos/zephyr/issues/32930) - [Coverity CID :219515] Side effect in assertion in subsys/bluetooth/controller/ll\_sw/ull\_sched.c
- [GitHub #32929](https://github.com/zephyrproject-rtos/zephyr/issues/32929) - [Coverity CID :219516] Improper use of negative value in tests/drivers/timer/nrf\_rtc\_timer/src/main.c
- [GitHub #32928](https://github.com/zephyrproject-rtos/zephyr/issues/32928) - [Coverity CID :219518] Macro compares unsigned to 0 in subsys/bluetooth/mesh/transport.c
- [GitHub #32927](https://github.com/zephyrproject-rtos/zephyr/issues/32927) - [Coverity CID :219519] Unchecked return value in drivers/ethernet/eth\_sam\_gmac.c
- [GitHub #32926](https://github.com/zephyrproject-rtos/zephyr/issues/32926) - [Coverity CID :219520] Unsigned compared against 0 in drivers/wifi/esp/esp.c
- [GitHub #32925](https://github.com/zephyrproject-rtos/zephyr/issues/32925) - [Coverity CID :219521] Unchecked return value in tests/kernel/workq/work/src/main.c
- [GitHub #32924](https://github.com/zephyrproject-rtos/zephyr/issues/32924) - [Coverity CID :219522] Unchecked return value in tests/subsys/dfu/mcuboot/src/main.c
- [GitHub #32923](https://github.com/zephyrproject-rtos/zephyr/issues/32923) - [Coverity CID :219523] Side effect in assertion in subsys/bluetooth/controller/ll\_sw/ull\_adv\_sync.c
- [GitHub #32922](https://github.com/zephyrproject-rtos/zephyr/issues/32922) - [Coverity CID :219524] Logically dead code in drivers/wifi/esp/esp.c
- [GitHub #32921](https://github.com/zephyrproject-rtos/zephyr/issues/32921) - [Coverity CID :219525] Unchecked return value in tests/subsys/settings/functional/src/settings\_basic\_test.c
- [GitHub #32920](https://github.com/zephyrproject-rtos/zephyr/issues/32920) - [Coverity CID :219526] Operands don’t affect result in tests/boards/mec15xxevb\_assy6853/qspi/src/main.c
- [GitHub #32919](https://github.com/zephyrproject-rtos/zephyr/issues/32919) - [Coverity CID :219527] Resource leak in tests/net/socket/getaddrinfo/src/main.c
- [GitHub #32918](https://github.com/zephyrproject-rtos/zephyr/issues/32918) - [Coverity CID :219528] Arguments in wrong order in tests/drivers/pwm/pwm\_loopback/src/main.c
- [GitHub #32917](https://github.com/zephyrproject-rtos/zephyr/issues/32917) - [Coverity CID :219529] Unchecked return value in subsys/bluetooth/controller/ll\_sw/ull\_filter.c
- [GitHub #32916](https://github.com/zephyrproject-rtos/zephyr/issues/32916) - [Coverity CID :219530] Dereference before null check in drivers/modem/ublox-sara-r4.c
- [GitHub #32915](https://github.com/zephyrproject-rtos/zephyr/issues/32915) - [Coverity CID :219531] Improper use of negative value in tests/drivers/timer/nrf\_rtc\_timer/src/main.c
- [GitHub #32914](https://github.com/zephyrproject-rtos/zephyr/issues/32914) - [Coverity CID :219532] Out-of-bounds access in tests/drivers/timer/nrf\_rtc\_timer/src/main.c
- [GitHub #32913](https://github.com/zephyrproject-rtos/zephyr/issues/32913) - [Coverity CID :219535] Dereference after null check in drivers/sensor/icm42605/icm42605.c
- [GitHub #32912](https://github.com/zephyrproject-rtos/zephyr/issues/32912) - [Coverity CID :219536] Dereference before null check in drivers/ieee802154/ieee802154\_nrf5.c
- [GitHub #32911](https://github.com/zephyrproject-rtos/zephyr/issues/32911) - [Coverity CID :219537] Out-of-bounds access in samples/boards/nrf/system\_off/src/retained.c
- [GitHub #32910](https://github.com/zephyrproject-rtos/zephyr/issues/32910) - [Coverity CID :219538] Illegal address computation in subsys/bluetooth/controller/ll\_sw/nordic/lll/lll\_adv\_aux.c
- [GitHub #32909](https://github.com/zephyrproject-rtos/zephyr/issues/32909) - [Coverity CID :219540] Side effect in assertion in subsys/bluetooth/controller/ll\_sw/ull\_sched.c
- [GitHub #32908](https://github.com/zephyrproject-rtos/zephyr/issues/32908) - [Coverity CID :219541] Unused value in subsys/bluetooth/controller/ticker/ticker.c
- [GitHub #32907](https://github.com/zephyrproject-rtos/zephyr/issues/32907) - [Coverity CID :219542] Dereference null return value in subsys/bluetooth/mesh/heartbeat.c
- [GitHub #32906](https://github.com/zephyrproject-rtos/zephyr/issues/32906) - [Coverity CID :219543] Out-of-bounds access in samples/boards/nrf/mesh/onoff\_level\_lighting\_vnd\_app/src/smp\_svr.c
- [GitHub #32905](https://github.com/zephyrproject-rtos/zephyr/issues/32905) - [Coverity CID :219544] Logically dead code in drivers/wifi/esp/esp.c
- [GitHub #32904](https://github.com/zephyrproject-rtos/zephyr/issues/32904) - [Coverity CID :219545] Side effect in assertion in subsys/bluetooth/controller/ll\_sw/ull\_adv\_aux.c
- [GitHub #32903](https://github.com/zephyrproject-rtos/zephyr/issues/32903) - [Coverity CID :219546] Unchecked return value in tests/kernel/workq/work/src/main.c
- [GitHub #32902](https://github.com/zephyrproject-rtos/zephyr/issues/32902) - [Coverity CID :219547] Improper use of negative value in tests/drivers/timer/nrf\_rtc\_timer/src/main.c
- [GitHub #32898](https://github.com/zephyrproject-rtos/zephyr/issues/32898) - Bluetooth: controller: Control PDU buffer leak into Data PDU buffer pool
- [GitHub #32877](https://github.com/zephyrproject-rtos/zephyr/issues/32877) - acrn: test case of kernel.timer and kernel.timer.tickless failed
- [GitHub #32875](https://github.com/zephyrproject-rtos/zephyr/issues/32875) - Benchmarking Zephyr vs. RIOT-OS
- [GitHub #32867](https://github.com/zephyrproject-rtos/zephyr/issues/32867) - tests/kernel/sched/schedule\_api does not start with stm32wb55 on nucleo
- [GitHub #32866](https://github.com/zephyrproject-rtos/zephyr/issues/32866) - bt\_le\_ext\_adv\_create returns -5 with 0x2036 opcode status 1
- [GitHub #32862](https://github.com/zephyrproject-rtos/zephyr/issues/32862) - MCUboot, use default UART\_0 value for RECOVERY\_UART\_DEV\_NAME
- [GitHub #32860](https://github.com/zephyrproject-rtos/zephyr/issues/32860) - Periodic advertising/synchronization on nRF52810
- [GitHub #32853](https://github.com/zephyrproject-rtos/zephyr/issues/32853) - lwm2m: uninitialized variable in this function
- [GitHub #32839](https://github.com/zephyrproject-rtos/zephyr/issues/32839) - tests/kernel/timer/timer\_api/test\_timeout\_abs still fails on multiple platforms
- [GitHub #32835](https://github.com/zephyrproject-rtos/zephyr/issues/32835) - twister: integration\_platforms stopped working as it should
- [GitHub #32828](https://github.com/zephyrproject-rtos/zephyr/issues/32828) - tests: posix: Test case portability.posix.common.tls.newlib.posix\_realtime fails on nrf9160dk\_nrf9160
- [GitHub #32827](https://github.com/zephyrproject-rtos/zephyr/issues/32827) - question: Specify size of malloc arena
- [GitHub #32818](https://github.com/zephyrproject-rtos/zephyr/issues/32818) - Function z\_swap\_next\_thread() missing coverage in sched.c
- [GitHub #32817](https://github.com/zephyrproject-rtos/zephyr/issues/32817) - Supporting fedora in the getting started docs
- [GitHub #32816](https://github.com/zephyrproject-rtos/zephyr/issues/32816) - ehl\_crb: tests/kernel/timer/timer\_api/timer\_api/test\_sleep\_abs (kernel.timer.tickless) failed.
- [GitHub #32809](https://github.com/zephyrproject-rtos/zephyr/issues/32809) - Fail to build ARC zephyr with MetaWare toolchain
- [GitHub #32800](https://github.com/zephyrproject-rtos/zephyr/issues/32800) - Race conditions with setting thread attributes after `z_ready_thread`?
- [GitHub #32798](https://github.com/zephyrproject-rtos/zephyr/issues/32798) - west flash fails for reel board
- [GitHub #32778](https://github.com/zephyrproject-rtos/zephyr/issues/32778) - Cannot support both HID boot report keyboard and mouse on a USB HID device
- [GitHub #32774](https://github.com/zephyrproject-rtos/zephyr/issues/32774) - Sensor BMI160: set of undersampling mode is not working
- [GitHub #32771](https://github.com/zephyrproject-rtos/zephyr/issues/32771) - STM32 with Ethernet crashes when receiving packets early
- [GitHub #32757](https://github.com/zephyrproject-rtos/zephyr/issues/32757) - Need openthread merge
- [GitHub #32755](https://github.com/zephyrproject-rtos/zephyr/issues/32755) - mcumgr: shell output gets truncated
- [GitHub #32745](https://github.com/zephyrproject-rtos/zephyr/issues/32745) - Bluetooth PAST shell command
- [GitHub #32742](https://github.com/zephyrproject-rtos/zephyr/issues/32742) - Bluetooth: GAP: LE connection complete event handling priority
- [GitHub #32741](https://github.com/zephyrproject-rtos/zephyr/issues/32741) - ARM32 / ARM64 separation
- [GitHub #32735](https://github.com/zephyrproject-rtos/zephyr/issues/32735) - Subsys: Logging: Functions purely to avoid compiling error affects test coverage
- [GitHub #32724](https://github.com/zephyrproject-rtos/zephyr/issues/32724) - qemu timer change introducing new CI failures
- [GitHub #32723](https://github.com/zephyrproject-rtos/zephyr/issues/32723) - kernel/sched: Only send IPI to abort a thread if the hardware supports it
- [GitHub #32721](https://github.com/zephyrproject-rtos/zephyr/issues/32721) - samples/bluetooth/periodic\_adv/, print random address after every reset
- [GitHub #32720](https://github.com/zephyrproject-rtos/zephyr/issues/32720) - ./samples/microbit/central\_eatt builds failed at v2.5.0 release
- [GitHub #32718](https://github.com/zephyrproject-rtos/zephyr/issues/32718) - NUCLEO-F446RE: Enable CAN Module
- [GitHub #32715](https://github.com/zephyrproject-rtos/zephyr/issues/32715) - async uart api not working on stm32 with dmamux
- [GitHub #32705](https://github.com/zephyrproject-rtos/zephyr/issues/32705) - KERNEL\_COHERENCE on xtensa doesn’t quite work yet
- [GitHub #32702](https://github.com/zephyrproject-rtos/zephyr/issues/32702) - RAM overflow with bbc:microbit for samples/bluetooth/peripheral…
- [GitHub #32699](https://github.com/zephyrproject-rtos/zephyr/issues/32699) - Setting custom BOARD\_ROOT raises FileNotFoundError
- [GitHub #32697](https://github.com/zephyrproject-rtos/zephyr/issues/32697) - sam\_e70b\_xplained: running tests/kernel/timer/timer\_api failed
- [GitHub #32696](https://github.com/zephyrproject-rtos/zephyr/issues/32696) - intel\_adsp\_cavs15: run testcases failed of tests/kernel/common
- [GitHub #32695](https://github.com/zephyrproject-rtos/zephyr/issues/32695) - intel\_adsp\_cavs15: cannot get output of some testcases
- [GitHub #32691](https://github.com/zephyrproject-rtos/zephyr/issues/32691) - Function z\_find\_first\_thread\_to\_unpend() missing coverage in sched.c
- [GitHub #32688](https://github.com/zephyrproject-rtos/zephyr/issues/32688) - up\_squared: tests/kernel/timer/timer\_api failed.
- [GitHub #32679](https://github.com/zephyrproject-rtos/zephyr/issues/32679) - twister with –device-testing sometimes overlaps tests
- [GitHub #32677](https://github.com/zephyrproject-rtos/zephyr/issues/32677) - z\_user\_string\_nlen() might lead to non-recoverable errors, despite suggesting the opposite
- [GitHub #32657](https://github.com/zephyrproject-rtos/zephyr/issues/32657) - canopen sample wont respond on pdo mapping with CO\_ODs from objdict.eds
- [GitHub #32656](https://github.com/zephyrproject-rtos/zephyr/issues/32656) - reel\_board: tests/lib/devicetree/devices/ build failure
- [GitHub #32655](https://github.com/zephyrproject-rtos/zephyr/issues/32655) - reel\_board: tests/kernel/timer/timer\_api/ failure
- [GitHub #32644](https://github.com/zephyrproject-rtos/zephyr/issues/32644) - Cannot build any project with system-wide DTC
- [GitHub #32619](https://github.com/zephyrproject-rtos/zephyr/issues/32619) - samples: usb: audio: Samples for usb audio fail building
- [GitHub #32599](https://github.com/zephyrproject-rtos/zephyr/issues/32599) - bbc\_microbit build failure is blocking CI
- [GitHub #32589](https://github.com/zephyrproject-rtos/zephyr/issues/32589) - ehl\_crb: tests/kernel/context fails sporadically
- [GitHub #32581](https://github.com/zephyrproject-rtos/zephyr/issues/32581) - shell/usb cdc\_acm: shell does not work on CDC\_ACM
- [GitHub #32579](https://github.com/zephyrproject-rtos/zephyr/issues/32579) - Corrupt CBOR payloads in MCUMGR when sending multiple commands together
- [GitHub #32572](https://github.com/zephyrproject-rtos/zephyr/issues/32572) - tests/kernel/timer/timer\_api/test\_timeout\_abs fails on stm32 boards
- [GitHub #32566](https://github.com/zephyrproject-rtos/zephyr/issues/32566) - lwm2m: Long endpoint names are truncated due to short buffer
- [GitHub #32537](https://github.com/zephyrproject-rtos/zephyr/issues/32537) - Fatal error syscall\_list.h
- [GitHub #32536](https://github.com/zephyrproject-rtos/zephyr/issues/32536) - Codec phy connection ASSERTION FAIL [event.curr.abort\_cb]
- [GitHub #32515](https://github.com/zephyrproject-rtos/zephyr/issues/32515) - zephyr/kernel/thread.c:382 failed
- [GitHub #32514](https://github.com/zephyrproject-rtos/zephyr/issues/32514) - frdm\_k64f:running testcase tests/subsys/debug/coredump/ and tests/subsys/debug/coredump\_backends/ failed
- [GitHub #32513](https://github.com/zephyrproject-rtos/zephyr/issues/32513) - intel\_adsp\_cavs15: run testcases of fifo failed
- [GitHub #32512](https://github.com/zephyrproject-rtos/zephyr/issues/32512) - intel\_adsp\_cavs15: run testcases of queue failed
- [GitHub #32511](https://github.com/zephyrproject-rtos/zephyr/issues/32511) - Zephyr build fail with LLVM on Ubuntu for target ARC
- [GitHub #32509](https://github.com/zephyrproject-rtos/zephyr/issues/32509) - west build -p auto -b nrf52840dk\_nrf52840 samples/bluetooth/hci\_uart FAILED with zephyr-v2.5.0
- [GitHub #32506](https://github.com/zephyrproject-rtos/zephyr/issues/32506) - k\_sleep: Invalid return value when using absolute timeout.
- [GitHub #32499](https://github.com/zephyrproject-rtos/zephyr/issues/32499) - k\_sleep duration is off by 1 tick
- [GitHub #32497](https://github.com/zephyrproject-rtos/zephyr/issues/32497) - No checks of buffer size in l2cap\_chan\_le\_recv
- [GitHub #32492](https://github.com/zephyrproject-rtos/zephyr/issues/32492) - AArch64: Rework secure states (NS vs S) discussion
- [GitHub #32485](https://github.com/zephyrproject-rtos/zephyr/issues/32485) - CONFIG\_NFCT\_PINS\_AS\_GPIOS not in Kconfig.soc for nRF53
- [GitHub #32478](https://github.com/zephyrproject-rtos/zephyr/issues/32478) - twister: Twister cannot properly handle runners errors (flashing)
- [GitHub #32475](https://github.com/zephyrproject-rtos/zephyr/issues/32475) - twister error building mcux acmp driver
- [GitHub #32474](https://github.com/zephyrproject-rtos/zephyr/issues/32474) - pm: review post sleep wake up application notification scheduling
- [GitHub #32469](https://github.com/zephyrproject-rtos/zephyr/issues/32469) - Twister: potential race conditions.
- [GitHub #32468](https://github.com/zephyrproject-rtos/zephyr/issues/32468) - up\_squared: tests/kernel/smp failed.
- [GitHub #32467](https://github.com/zephyrproject-rtos/zephyr/issues/32467) - x86\_64: page fault with access violation error complaining supervisor thread not allowed to rwx
- [GitHub #32459](https://github.com/zephyrproject-rtos/zephyr/issues/32459) - the cbprintf unit tests don’t actually test all variations
- [GitHub #32457](https://github.com/zephyrproject-rtos/zephyr/issues/32457) - samples: drivers: espi: Need to handle failures in temperature retrieval
- [GitHub #32448](https://github.com/zephyrproject-rtos/zephyr/issues/32448) - C++ exceptions do not work on multiple platforms
- [GitHub #32445](https://github.com/zephyrproject-rtos/zephyr/issues/32445) - 2021 GSoC Project Idea: Transplantation for embarc\_mli
- [GitHub #32444](https://github.com/zephyrproject-rtos/zephyr/issues/32444) - z\_cstart bug
- [GitHub #32433](https://github.com/zephyrproject-rtos/zephyr/issues/32433) - pwm\_stm32: warning: non-portable use of “defined”
- [GitHub #32431](https://github.com/zephyrproject-rtos/zephyr/issues/32431) - RTC driver support on STM32F1 series
- [GitHub #32429](https://github.com/zephyrproject-rtos/zephyr/issues/32429) - Only one PWM Channel supported in STM32L4 ?
- [GitHub #32420](https://github.com/zephyrproject-rtos/zephyr/issues/32420) - bbc\_microbit\_v2 build error for lis2dh
- [GitHub #32414](https://github.com/zephyrproject-rtos/zephyr/issues/32414) - [Coverity CID :218733] Explicit null dereferenced in tests/ztest/error\_hook/src/main.c
- [GitHub #32413](https://github.com/zephyrproject-rtos/zephyr/issues/32413) - [Coverity CID :216799] Out-of-bounds access in tests/net/lib/dns\_addremove/src/main.c
- [GitHub #32412](https://github.com/zephyrproject-rtos/zephyr/issues/32412) - [Coverity CID :216797] Dereference null return value in tests/net/6lo/src/main.c
- [GitHub #32411](https://github.com/zephyrproject-rtos/zephyr/issues/32411) - [Coverity CID :218744] Out-of-bounds access in subsys/bluetooth/host/gatt.c
- [GitHub #32410](https://github.com/zephyrproject-rtos/zephyr/issues/32410) - [Coverity CID :218743] Out-of-bounds access in subsys/bluetooth/host/gatt.c
- [GitHub #32409](https://github.com/zephyrproject-rtos/zephyr/issues/32409) - [Coverity CID :218742] Out-of-bounds access in subsys/bluetooth/host/gatt.c
- [GitHub #32408](https://github.com/zephyrproject-rtos/zephyr/issues/32408) - [Coverity CID :218741] Out-of-bounds access in subsys/bluetooth/host/att.c
- [GitHub #32407](https://github.com/zephyrproject-rtos/zephyr/issues/32407) - [Coverity CID :218740] Out-of-bounds access in subsys/bluetooth/host/gatt.c
- [GitHub #32406](https://github.com/zephyrproject-rtos/zephyr/issues/32406) - [Coverity CID :218737] Out-of-bounds write in subsys/bluetooth/host/gatt.c
- [GitHub #32405](https://github.com/zephyrproject-rtos/zephyr/issues/32405) - [Coverity CID :218735] Out-of-bounds access in subsys/bluetooth/host/att.c
- [GitHub #32404](https://github.com/zephyrproject-rtos/zephyr/issues/32404) - [Coverity CID :218734] Out-of-bounds access in subsys/bluetooth/host/smp.c
- [GitHub #32403](https://github.com/zephyrproject-rtos/zephyr/issues/32403) - [Coverity CID :218732] Out-of-bounds access in subsys/bluetooth/host/att.c
- [GitHub #32402](https://github.com/zephyrproject-rtos/zephyr/issues/32402) - [Coverity CID :218731] Out-of-bounds access in subsys/bluetooth/shell/gatt.c
- [GitHub #32401](https://github.com/zephyrproject-rtos/zephyr/issues/32401) - [Coverity CID :218730] Operands don’t affect result in subsys/bluetooth/host/conn.c
- [GitHub #32400](https://github.com/zephyrproject-rtos/zephyr/issues/32400) - [Coverity CID :218729] Out-of-bounds access in subsys/bluetooth/host/gatt.c
- [GitHub #32399](https://github.com/zephyrproject-rtos/zephyr/issues/32399) - [Coverity CID :218728] Out-of-bounds access in subsys/bluetooth/host/gatt.c
- [GitHub #32398](https://github.com/zephyrproject-rtos/zephyr/issues/32398) - [Coverity CID :218727] Out-of-bounds access in subsys/bluetooth/host/gatt.c
- [GitHub #32397](https://github.com/zephyrproject-rtos/zephyr/issues/32397) - [Coverity CID :218726] Out-of-bounds access in subsys/bluetooth/host/att.c
- [GitHub #32385](https://github.com/zephyrproject-rtos/zephyr/issues/32385) - clock\_control: int is returned on enum return value
- [GitHub #32382](https://github.com/zephyrproject-rtos/zephyr/issues/32382) - Clock issues for STM32F103RE custom board
- [GitHub #32376](https://github.com/zephyrproject-rtos/zephyr/issues/32376) - samples: driver: watchdog: Sample fails on disco\_l475\_iot1
- [GitHub #32375](https://github.com/zephyrproject-rtos/zephyr/issues/32375) - Networking stack crashes when run in cooperative scheduling mode only
- [GitHub #32365](https://github.com/zephyrproject-rtos/zephyr/issues/32365) - samples: hci\_rpmsg build fail for nrf5340
- [GitHub #32344](https://github.com/zephyrproject-rtos/zephyr/issues/32344) - sporadic failure in tests/kernel/mem\_protect/userspace/kernel.memory\_protection.userspace
- [GitHub #32343](https://github.com/zephyrproject-rtos/zephyr/issues/32343) - openthread manual joiner hangs
- [GitHub #32342](https://github.com/zephyrproject-rtos/zephyr/issues/32342) - review use of cpsid in aarch32 / CONFIG\_PM
- [GitHub #32331](https://github.com/zephyrproject-rtos/zephyr/issues/32331) - Use of unitialized variables in can\_set\_bitrate()
- [GitHub #32321](https://github.com/zephyrproject-rtos/zephyr/issues/32321) - /tmp/ccTlcyeD.s:242: Error: Unrecognized Symbol type “ “
- [GitHub #32320](https://github.com/zephyrproject-rtos/zephyr/issues/32320) - drivers: flash: stm32: Flush ART Flash cache after erase operation
- [GitHub #32314](https://github.com/zephyrproject-rtos/zephyr/issues/32314) - 2021 GSoC Project Idea: Enable Interactive Zephyr Test Suite
- [GitHub #32291](https://github.com/zephyrproject-rtos/zephyr/issues/32291) - Zephyr don’t build sample hello world for Particle Xenon
- [GitHub #32289](https://github.com/zephyrproject-rtos/zephyr/issues/32289) - USDHC: Fails after reset
- [GitHub #32279](https://github.com/zephyrproject-rtos/zephyr/issues/32279) - Question about flasing Adafruit Feather Sense with Zephyr
- [GitHub #32270](https://github.com/zephyrproject-rtos/zephyr/issues/32270) - TCP connection stalls
- [GitHub #32269](https://github.com/zephyrproject-rtos/zephyr/issues/32269) - shield: cmake: Shield conf is not loaded during build
- [GitHub #32265](https://github.com/zephyrproject-rtos/zephyr/issues/32265) - STM32F4 stuck handling I2C interrupt
- [GitHub #32261](https://github.com/zephyrproject-rtos/zephyr/issues/32261) - problem with CONFIG\_STACK\_SENTINEL
- [GitHub #32260](https://github.com/zephyrproject-rtos/zephyr/issues/32260) - STM32 counter driver error in estimating alarm time
- [GitHub #32258](https://github.com/zephyrproject-rtos/zephyr/issues/32258) - power mgmt: pm\_devices: Get rid of z\_pm\_core\_devices array
- [GitHub #32257](https://github.com/zephyrproject-rtos/zephyr/issues/32257) - Common DFU partition enumeration API
- [GitHub #32256](https://github.com/zephyrproject-rtos/zephyr/issues/32256) - Bluetooth mesh : Long friendship establishment after reset
- [GitHub #32252](https://github.com/zephyrproject-rtos/zephyr/issues/32252) - Building anything for nrf5340pdk\_nrf5340\_cpuappns/mps2\_an521\_ns(any non-secure platforms) pulls external git trees
- [GitHub #32237](https://github.com/zephyrproject-rtos/zephyr/issues/32237) - twister failing locally - fails to link native\_posix w/lld
- [GitHub #32234](https://github.com/zephyrproject-rtos/zephyr/issues/32234) - Documentation: How to update Zephyr itself (with west)
- [GitHub #32233](https://github.com/zephyrproject-rtos/zephyr/issues/32233) - Often disconnect timeouts when running the BLE peripheral HR sample on Nitrogen96
- [GitHub #32224](https://github.com/zephyrproject-rtos/zephyr/issues/32224) - Treat devicetree binding deprecation usage as build error when running w/twister
- [GitHub #32212](https://github.com/zephyrproject-rtos/zephyr/issues/32212) - Tx power levels are not similar on ADV and CONN modes when set manually (nRF52)
- [GitHub #32206](https://github.com/zephyrproject-rtos/zephyr/issues/32206) - CMSIS-DSP support seems broken on link
- [GitHub #32205](https://github.com/zephyrproject-rtos/zephyr/issues/32205) - [misc] AArch64 improvements and fixes
- [GitHub #32203](https://github.com/zephyrproject-rtos/zephyr/issues/32203) - Cannot set static address when using hci\_usb or hci\_uart on nRF5340 attached to Linux Host
- [GitHub #32201](https://github.com/zephyrproject-rtos/zephyr/issues/32201) - arch\_switch() on ARM64 isn’t quite right
- [GitHub #32197](https://github.com/zephyrproject-rtos/zephyr/issues/32197) - arch\_switch() on SPARC isn’t quite right
- [GitHub #32195](https://github.com/zephyrproject-rtos/zephyr/issues/32195) - ARMv8-nofp support
- [GitHub #32193](https://github.com/zephyrproject-rtos/zephyr/issues/32193) - Plan to support raspberry pi Pico?
- [GitHub #32158](https://github.com/zephyrproject-rtos/zephyr/issues/32158) - twister: inconsistent total testcases number with same configuration
- [GitHub #32145](https://github.com/zephyrproject-rtos/zephyr/issues/32145) - `kernel threads` and `kernel stacks` deadlock in many scenarios
- [GitHub #32137](https://github.com/zephyrproject-rtos/zephyr/issues/32137) - Provide test execution times per ztest testcase
- [GitHub #32118](https://github.com/zephyrproject-rtos/zephyr/issues/32118) - drivers/flash/soc\_flash\_nrf: nRF anomaly 242 workaround is not implemented
- [GitHub #32098](https://github.com/zephyrproject-rtos/zephyr/issues/32098) - Implement a driver for the Microphone / audio sensor (MP23ABS1) in Sensotile.Box
- [GitHub #32084](https://github.com/zephyrproject-rtos/zephyr/issues/32084) - Custom Log Backend breaks performance
- [GitHub #32075](https://github.com/zephyrproject-rtos/zephyr/issues/32075) - net: lwm2m: Testing Strategy for LWM2M Engine
- [GitHub #32072](https://github.com/zephyrproject-rtos/zephyr/issues/32072) - tests/kernel/common seems to fail on nrf52833dk\_nrf52833
- [GitHub #32071](https://github.com/zephyrproject-rtos/zephyr/issues/32071) - devicetree: `bus:` does not work in `child-binding`
- [GitHub #32052](https://github.com/zephyrproject-rtos/zephyr/issues/32052) - p4wq has a race with work item re-use
- [GitHub #32023](https://github.com/zephyrproject-rtos/zephyr/issues/32023) - samples: bluetooth: peripheral\_hids: Unable to communicate with paired device after board reset
- [GitHub #32000](https://github.com/zephyrproject-rtos/zephyr/issues/32000) - 2021 GSoC Call for Project Ideas - deadline Feb.19, 2021 12:00PM PST
- [GitHub #31985](https://github.com/zephyrproject-rtos/zephyr/issues/31985) - riscv: Long execution time when TICKLESS\_KERNEL=y
- [GitHub #31982](https://github.com/zephyrproject-rtos/zephyr/issues/31982) - tests: kernel: queue: regression introduced by FPU sharing PR #31772
- [GitHub #31980](https://github.com/zephyrproject-rtos/zephyr/issues/31980) - Communicating with BMI160 chip over SPI
- [GitHub #31969](https://github.com/zephyrproject-rtos/zephyr/issues/31969) - test\_tcp\_fn:net2 mximxrt1060/1064/1050 fails on test\_client\_invalid\_rst with semaphore timed out
- [GitHub #31964](https://github.com/zephyrproject-rtos/zephyr/issues/31964) - up\_squared: tests/kernel/timer/timer\_api failed.
- [GitHub #31922](https://github.com/zephyrproject-rtos/zephyr/issues/31922) - hci\_usb: HCI ACL packet with size divisible by 64 not sent
- [GitHub #31856](https://github.com/zephyrproject-rtos/zephyr/issues/31856) - power: `device_pm_get_sync` not thread-safe
- [GitHub #31854](https://github.com/zephyrproject-rtos/zephyr/issues/31854) - undefined reference to `sys_arch_reboot`
- [GitHub #31829](https://github.com/zephyrproject-rtos/zephyr/issues/31829) - net: lwm2m: Update IPSO objects to version 1.1
- [GitHub #31799](https://github.com/zephyrproject-rtos/zephyr/issues/31799) - uart\_configure does not return -ENOTSUP for stm32 uart with 9 bit data length.
- [GitHub #31774](https://github.com/zephyrproject-rtos/zephyr/issues/31774) - Add an application power management sample (PM\_POLICY\_APP)
- [GitHub #31762](https://github.com/zephyrproject-rtos/zephyr/issues/31762) - ivshmem application in acrn
- [GitHub #31761](https://github.com/zephyrproject-rtos/zephyr/issues/31761) - logging:buffer\_write with len=0 causes kernel panic
- [GitHub #31757](https://github.com/zephyrproject-rtos/zephyr/issues/31757) - GCC compiler option should include ‘-mcpu=hs38’ for HSDK
- [GitHub #31742](https://github.com/zephyrproject-rtos/zephyr/issues/31742) - Bluetooth: BLE 5 data throughput to Linux host
- [GitHub #31721](https://github.com/zephyrproject-rtos/zephyr/issues/31721) - tests: nrf: posix: portability.posix.common.tls.newlib fails on nrf9160dk\_nrf9160
- [GitHub #31711](https://github.com/zephyrproject-rtos/zephyr/issues/31711) - UART failure with CONFIG\_UART\_ASYNC\_API
- [GitHub #31613](https://github.com/zephyrproject-rtos/zephyr/issues/31613) - Undefined reference errors when using External Library with k\_msgq\_\* calls
- [GitHub #31588](https://github.com/zephyrproject-rtos/zephyr/issues/31588) - Bluetooth: Support for multiple connectable advertising sets with different identities.
- [GitHub #31585](https://github.com/zephyrproject-rtos/zephyr/issues/31585) - BMD345: Extended BLE range with PA/LNA
- [GitHub #31503](https://github.com/zephyrproject-rtos/zephyr/issues/31503) - drivers: i2c: i2c\_nrfx\_twim Power Consumption rises after I2C data transfer
- [GitHub #31416](https://github.com/zephyrproject-rtos/zephyr/issues/31416) - ARC MPU version number misuse ver3, should be ver4
- [GitHub #31348](https://github.com/zephyrproject-rtos/zephyr/issues/31348) - twister: CI: Run twister daily builds with “–overflow-as-errors”
- [GitHub #31323](https://github.com/zephyrproject-rtos/zephyr/issues/31323) - Compilation warning regards the SNTP subsys
- [GitHub #31299](https://github.com/zephyrproject-rtos/zephyr/issues/31299) - tests/kernel/mbox/mbox\_usage failed on hsdk board
- [GitHub #31284](https://github.com/zephyrproject-rtos/zephyr/issues/31284) - [stm32] PM restore console after sleep mode
- [GitHub #31280](https://github.com/zephyrproject-rtos/zephyr/issues/31280) - devicetree: Add a macro to easily get optionnal devicetree GPIO properties
- [GitHub #31254](https://github.com/zephyrproject-rtos/zephyr/issues/31254) - Bluetooth: Extended advertising with one advertising set fails after the first time
- [GitHub #31248](https://github.com/zephyrproject-rtos/zephyr/issues/31248) - i2c shell functions non-functional on nRF53
- [GitHub #31217](https://github.com/zephyrproject-rtos/zephyr/issues/31217) - Multi-threading flash access is not supported by flash\_write\_protection\_set()
- [GitHub #31191](https://github.com/zephyrproject-rtos/zephyr/issues/31191) - Samples: TF-M: Enable NS test app(s)
- [GitHub #31179](https://github.com/zephyrproject-rtos/zephyr/issues/31179) - `iso bind` for slave not working as intended
- [GitHub #31169](https://github.com/zephyrproject-rtos/zephyr/issues/31169) - kconfig configuration (prj.conf) based on zephyr version
- [GitHub #31164](https://github.com/zephyrproject-rtos/zephyr/issues/31164) - Problem to build lorawan from samples
- [GitHub #31150](https://github.com/zephyrproject-rtos/zephyr/issues/31150) - tests/subsys/canbus/isotp/conformance: failing on nucleo\_f746zg
- [GitHub #31149](https://github.com/zephyrproject-rtos/zephyr/issues/31149) - tests/subsys/canbus/isotp/implementation: failing on nucleo\_f746zg
- [GitHub #31103](https://github.com/zephyrproject-rtos/zephyr/issues/31103) - CMSIS RTOS v2 API implementation bugs in osEventFlagsWait
- [GitHub #31058](https://github.com/zephyrproject-rtos/zephyr/issues/31058) - SWO log backend clock frequency is off on some CPUs
- [GitHub #31036](https://github.com/zephyrproject-rtos/zephyr/issues/31036) - BMI 160 i2c version not working. I modified to i2c in kconfig to make it use i2c.
- [GitHub #31031](https://github.com/zephyrproject-rtos/zephyr/issues/31031) - samples/bluetooth/mesh is not helpful
- [GitHub #30991](https://github.com/zephyrproject-rtos/zephyr/issues/30991) - Unable to add new i2c sensor to nrf/samples
- [GitHub #30943](https://github.com/zephyrproject-rtos/zephyr/issues/30943) - MPU fault with STM32L452
- [GitHub #30936](https://github.com/zephyrproject-rtos/zephyr/issues/30936) - tests: sockets: tcp: add a tls test
- [GitHub #30929](https://github.com/zephyrproject-rtos/zephyr/issues/30929) - PDM Driver for nrf52840dk
- [GitHub #30841](https://github.com/zephyrproject-rtos/zephyr/issues/30841) - How to disable reception of socket CAN frames
- [GitHub #30771](https://github.com/zephyrproject-rtos/zephyr/issues/30771) - Logging: Fault instruction address in the logging thread
- [GitHub #30770](https://github.com/zephyrproject-rtos/zephyr/issues/30770) - mps2\_an521: no input to shell from Windows qemu host
- [GitHub #30618](https://github.com/zephyrproject-rtos/zephyr/issues/30618) - Add arduino header/spi support for HSDK board
- [GitHub #30544](https://github.com/zephyrproject-rtos/zephyr/issues/30544) - nrf5340 pwm “Unsupported board: pwm-led0 devicetree alias is not defined”
- [GitHub #30540](https://github.com/zephyrproject-rtos/zephyr/issues/30540) - CONFIG\_TRACING not working after updating from v2.1.0 to 2.2.0
- [GitHub #30520](https://github.com/zephyrproject-rtos/zephyr/issues/30520) - recv() call to Ublox Sara R4 cant return 0
- [GitHub #30465](https://github.com/zephyrproject-rtos/zephyr/issues/30465) - Spurious interrupts not handled in ARMv7-R code with GICv2.
- [GitHub #30441](https://github.com/zephyrproject-rtos/zephyr/issues/30441) - hci\_uart uses wrong BT\_BUF\_ACL\_SIZE on dual chip solutions + multicore
- [GitHub #30429](https://github.com/zephyrproject-rtos/zephyr/issues/30429) - Thread Border Router with NRC/RCP sample and nrf52840dk not starting
- [GitHub #30416](https://github.com/zephyrproject-rtos/zephyr/issues/30416) - No restore possible with mesh shell app from /tests using qemu\_x86 on RaspberryPi3
- [GitHub #30395](https://github.com/zephyrproject-rtos/zephyr/issues/30395) - Add possibility to use alternative list of platforms default for CI runs.
- [GitHub #30355](https://github.com/zephyrproject-rtos/zephyr/issues/30355) - Multiple vlan interfaces on same interface not working
- [GitHub #30353](https://github.com/zephyrproject-rtos/zephyr/issues/30353) - RFC: Logging subsystem overhaul
- [GitHub #30325](https://github.com/zephyrproject-rtos/zephyr/issues/30325) - Stack overflow with http post when using civetweb
- [GitHub #30204](https://github.com/zephyrproject-rtos/zephyr/issues/30204) - Support for Teensy 4.0 and 4.1
- [GitHub #30195](https://github.com/zephyrproject-rtos/zephyr/issues/30195) - Missing error check of device\_get\_binding() and flash\_area\_open()
- [GitHub #30192](https://github.com/zephyrproject-rtos/zephyr/issues/30192) - mec15xxevb\_assy6853: running tests/subsys/power/power\_mgmt\_soc failed
- [GitHub #30162](https://github.com/zephyrproject-rtos/zephyr/issues/30162) - Build zephyr with Metaware toolchain for HSDK fails
- [GitHub #30121](https://github.com/zephyrproject-rtos/zephyr/issues/30121) - Make log subsystem power aware
- [GitHub #30101](https://github.com/zephyrproject-rtos/zephyr/issues/30101) - tests should not be silently skipped due to insufficient RAM
- [GitHub #30074](https://github.com/zephyrproject-rtos/zephyr/issues/30074) - Occasional Spinlocks on zephyr 2.4.0 (ASSERTION FAIL [z\_spin\_lock\_valid(l)] @ WEST\_TOPDIR/zephyr/include/spinlock.h:92)
- [GitHub #30055](https://github.com/zephyrproject-rtos/zephyr/issues/30055) - Memory corruption for newlib-nano with float printf and disabled heap
- [GitHub #29946](https://github.com/zephyrproject-rtos/zephyr/issues/29946) - SD card initialization is wrong
- [GitHub #29915](https://github.com/zephyrproject-rtos/zephyr/issues/29915) - eth: stm32h747i\_disco: sem timeout and hang on debug build
- [GitHub #29798](https://github.com/zephyrproject-rtos/zephyr/issues/29798) - test spi loopback with dma fails on nucleo\_f746zg
- [GitHub #29733](https://github.com/zephyrproject-rtos/zephyr/issues/29733) - SAM0 will wake up with interrupted execution after deep sleep
- [GitHub #29722](https://github.com/zephyrproject-rtos/zephyr/issues/29722) - West flash is not able to flash with openocd
- [GitHub #29689](https://github.com/zephyrproject-rtos/zephyr/issues/29689) - tests: drivers: gpio: gpio\_basic\_api: correct dts binding
- [GitHub #29610](https://github.com/zephyrproject-rtos/zephyr/issues/29610) - documentation says giving a semaphore can release IRQ lock
- [GitHub #29599](https://github.com/zephyrproject-rtos/zephyr/issues/29599) - gPTP: frdm\_k64f : can not converge time
- [GitHub #29581](https://github.com/zephyrproject-rtos/zephyr/issues/29581) - LoRaWAN sample for 96b\_wistrio - Tx timeout
- [GitHub #29545](https://github.com/zephyrproject-rtos/zephyr/issues/29545) - samples: tfm\_integration: tfm\_ipc: No module named ‘cryptography.hazmat.primitives.asymmetric.ed25519’
- [GitHub #29526](https://github.com/zephyrproject-rtos/zephyr/issues/29526) - generic page pool for MMU-based systems
- [GitHub #29476](https://github.com/zephyrproject-rtos/zephyr/issues/29476) - Samples: TF-M: Add PSA FF API Sample
- [GitHub #29349](https://github.com/zephyrproject-rtos/zephyr/issues/29349) - Using float when driver init in RISC-V arch might cause system to get stuck.
- [GitHub #29224](https://github.com/zephyrproject-rtos/zephyr/issues/29224) - PTS: Test framework: Bluetooth: GATT/SR/GAC/BI-01-C - FAIL
- [GitHub #29107](https://github.com/zephyrproject-rtos/zephyr/issues/29107) - Bluetooth: hci-usb uses non-standard interfaces
- [GitHub #29038](https://github.com/zephyrproject-rtos/zephyr/issues/29038) - drivers/usb/device/usb\_dc\_native\_posix\_adapt.c sees weird commands and aborts
- [GitHub #28901](https://github.com/zephyrproject-rtos/zephyr/issues/28901) - implement searchable bitfields
- [GitHub #28900](https://github.com/zephyrproject-rtos/zephyr/issues/28900) - add support for memory un-mapping
- [GitHub #28873](https://github.com/zephyrproject-rtos/zephyr/issues/28873) - z\_device\_ready() lies
- [GitHub #28803](https://github.com/zephyrproject-rtos/zephyr/issues/28803) - Use generic config option for early platfrom init (AKA “warm boot”)
- [GitHub #28722](https://github.com/zephyrproject-rtos/zephyr/issues/28722) - Bluetooth: provide `struct bt_conn` to ccc\_changed callback
- [GitHub #28597](https://github.com/zephyrproject-rtos/zephyr/issues/28597) - Bluetooth: controller: Redesign the implementation/use of NODE\_RX\_TYPE\_DC\_PDU\_RELEASE
- [GitHub #28551](https://github.com/zephyrproject-rtos/zephyr/issues/28551) - up\_squared: samples/boards/up\_squared/gpio\_counter failed.
- [GitHub #28535](https://github.com/zephyrproject-rtos/zephyr/issues/28535) - RFC: Add lz4 Data Compresssion library Support
- [GitHub #28438](https://github.com/zephyrproject-rtos/zephyr/issues/28438) - Example downstream manifest+module repo in zephyrproject-rtos
- [GitHub #28249](https://github.com/zephyrproject-rtos/zephyr/issues/28249) - driver: espi: mchp: eSPI OOB driver does not support callbacks for incoming OOB messages from eSPI master.
- [GitHub #28105](https://github.com/zephyrproject-rtos/zephyr/issues/28105) - sporadic “Attempt to resume un-suspended thread object” faults on x86-64
- [GitHub #28096](https://github.com/zephyrproject-rtos/zephyr/issues/28096) - fatfs update to latest upstream version
- [GitHub #27855](https://github.com/zephyrproject-rtos/zephyr/issues/27855) - i2c bitbanging on nrf52840
- [GitHub #27697](https://github.com/zephyrproject-rtos/zephyr/issues/27697) - Add support for passing -nogui 1 to J-Link Commander on MS Windows
- [GitHub #27692](https://github.com/zephyrproject-rtos/zephyr/issues/27692) - Allow to select between advertising packet/scan response for BT LE device name
- [GitHub #27525](https://github.com/zephyrproject-rtos/zephyr/issues/27525) - Including STM32Cube’s USB PD support to Zephyr
- [GitHub #27484](https://github.com/zephyrproject-rtos/zephyr/issues/27484) - sanitycheck: Ease error interception from calling script
- [GitHub #27415](https://github.com/zephyrproject-rtos/zephyr/issues/27415) - Decide if we keep a single thread support (CONFIG\_MULTITHREADING=n) in Zephyr
- [GitHub #27356](https://github.com/zephyrproject-rtos/zephyr/issues/27356) - deep review and redesign of API for work queue functionality
- [GitHub #27203](https://github.com/zephyrproject-rtos/zephyr/issues/27203) - tests/subsys/storage/flash\_map failure on twr\_ke18f
- [GitHub #27048](https://github.com/zephyrproject-rtos/zephyr/issues/27048) - Improve out-of-tree driver experience
- [GitHub #27033](https://github.com/zephyrproject-rtos/zephyr/issues/27033) - Update terminology related to I2C
- [GitHub #27032](https://github.com/zephyrproject-rtos/zephyr/issues/27032) - zephyr network stack socket APIs are not thread safe
- [GitHub #27000](https://github.com/zephyrproject-rtos/zephyr/issues/27000) - Avoid oppressive language in code base
- [GitHub #26952](https://github.com/zephyrproject-rtos/zephyr/issues/26952) - SMP support on ARM64 platform
- [GitHub #26889](https://github.com/zephyrproject-rtos/zephyr/issues/26889) - subsys: power: Need syscall that allows to force sleep state
- [GitHub #26760](https://github.com/zephyrproject-rtos/zephyr/issues/26760) - Improve caching configuration and move it to be cross architecture
- [GitHub #26728](https://github.com/zephyrproject-rtos/zephyr/issues/26728) - Allow k\_poll for multiple message queues
- [GitHub #26495](https://github.com/zephyrproject-rtos/zephyr/issues/26495) - Make k\_poll work with KERNEL\_COHERENCE
- [GitHub #26491](https://github.com/zephyrproject-rtos/zephyr/issues/26491) - PCIe: add API to get BAR region size
- [GitHub #26363](https://github.com/zephyrproject-rtos/zephyr/issues/26363) - samples: subsys: canbus: canopen: objdict: CO\_OD.h is not normally made.
- [GitHub #26246](https://github.com/zephyrproject-rtos/zephyr/issues/26246) - Printing 64-bit values in LOG\_DBG
- [GitHub #26172](https://github.com/zephyrproject-rtos/zephyr/issues/26172) - Zephyr Master/Slave not conforming with Core Spec. 5.2 connection policies
- [GitHub #26170](https://github.com/zephyrproject-rtos/zephyr/issues/26170) - HEXDUMP log gives warning when logging function name.
- [GitHub #26118](https://github.com/zephyrproject-rtos/zephyr/issues/26118) - Bluetooth: controller: nRF5x: refactor radio\_nrf5\_ppi.h
- [GitHub #25956](https://github.com/zephyrproject-rtos/zephyr/issues/25956) - Including header files from modules into app
- [GitHub #25865](https://github.com/zephyrproject-rtos/zephyr/issues/25865) - Device Tree Memory Layout
- [GitHub #25775](https://github.com/zephyrproject-rtos/zephyr/issues/25775) - [Coverity CID :210075] Negative array index write in samples/net/cloud/mqtt\_azure/src/main.c
- [GitHub #25719](https://github.com/zephyrproject-rtos/zephyr/issues/25719) - sanitycheck log mixing between tests
- [GitHub #25601](https://github.com/zephyrproject-rtos/zephyr/issues/25601) - UART input does not work on mps2\_an{385,521}
- [GitHub #25440](https://github.com/zephyrproject-rtos/zephyr/issues/25440) - Bluetooth: controller: ensure deferred PDU populations complete on time
- [GitHub #25389](https://github.com/zephyrproject-rtos/zephyr/issues/25389) - driver MMIO address range management
- [GitHub #25313](https://github.com/zephyrproject-rtos/zephyr/issues/25313) - samples:mimxrt1010\_evk:samples/subsys/usb/audio: build error no usbd found
- [GitHub #25187](https://github.com/zephyrproject-rtos/zephyr/issues/25187) - Generic ethernet packet filtering based on link (MAC) address
- [GitHub #24986](https://github.com/zephyrproject-rtos/zephyr/issues/24986) - Convert dma\_nios2\_msgdma to DTS
- [GitHub #24731](https://github.com/zephyrproject-rtos/zephyr/issues/24731) - Bluetooth: controller: Network privacy not respected when address resolution is disabled
- [GitHub #24625](https://github.com/zephyrproject-rtos/zephyr/issues/24625) - lib: drivers: clock: rtc: rtc api to maintain calendar time through reboot
- [GitHub #24228](https://github.com/zephyrproject-rtos/zephyr/issues/24228) - system power states
- [GitHub #24142](https://github.com/zephyrproject-rtos/zephyr/issues/24142) - NRF5340 PA/LNA support
- [GitHub #24119](https://github.com/zephyrproject-rtos/zephyr/issues/24119) - STM32: SPI: Extend power saving SPI pin config to all stm32 series
- [GitHub #24113](https://github.com/zephyrproject-rtos/zephyr/issues/24113) - STM32 Flash: Device tree updates
- [GitHub #23727](https://github.com/zephyrproject-rtos/zephyr/issues/23727) - RFC: clarification and standardization of ENOTSUP/ENOSYS error returns
- [GitHub #23520](https://github.com/zephyrproject-rtos/zephyr/issues/23520) - JLink Thread-Aware Debugging (RTOS Plugin)
- [GitHub #23465](https://github.com/zephyrproject-rtos/zephyr/issues/23465) - Zephyr Authentication - ZAUTH
- [GitHub #23449](https://github.com/zephyrproject-rtos/zephyr/issues/23449) - “make clean” doesn’t clean a lot of generated files
- [GitHub #23225](https://github.com/zephyrproject-rtos/zephyr/issues/23225) - Bluetooth: Quality of service: Adaptive channel map
- [GitHub #23165](https://github.com/zephyrproject-rtos/zephyr/issues/23165) - macOS setup fails to build for lack of “elftools” Python package
- [GitHub #22965](https://github.com/zephyrproject-rtos/zephyr/issues/22965) - 4 byte addressing in spi\_nor driver for memory larger than 128Mb.
- [GitHub #22956](https://github.com/zephyrproject-rtos/zephyr/issues/22956) - nios2: k\_busy\_wait() never returns if called with interrupts locked
- [GitHub #22731](https://github.com/zephyrproject-rtos/zephyr/issues/22731) - Improve docker CI documentation
- [GitHub #22620](https://github.com/zephyrproject-rtos/zephyr/issues/22620) - adapt cpu stats tracing to tracing infrastructure
- [GitHub #22078](https://github.com/zephyrproject-rtos/zephyr/issues/22078) - stm32: Shell module sample doesn’t work on nucleo\_l152re
- [GitHub #22061](https://github.com/zephyrproject-rtos/zephyr/issues/22061) - Ethernet switch support
- [GitHub #22060](https://github.com/zephyrproject-rtos/zephyr/issues/22060) - Build fails with gcc-arm-none-eabi-9-2019-q4-major
- [GitHub #22027](https://github.com/zephyrproject-rtos/zephyr/issues/22027) - i2c\_scanner does not work on olimexino\_stm32
- [GitHub #21993](https://github.com/zephyrproject-rtos/zephyr/issues/21993) - Bluetooth: controller: split: Move the LLL event prepare/resume queue handling into LLL
- [GitHub #21840](https://github.com/zephyrproject-rtos/zephyr/issues/21840) - need test case for CONFIG\_MULTIBOOT on x86
- [GitHub #21811](https://github.com/zephyrproject-rtos/zephyr/issues/21811) - Investigate using Doxygen-generated API docs vs. Sphinx/Breath API docs
- [GitHub #21809](https://github.com/zephyrproject-rtos/zephyr/issues/21809) - Update document generating tools to newer versions
- [GitHub #21783](https://github.com/zephyrproject-rtos/zephyr/issues/21783) - rename zassert functions
- [GitHub #21489](https://github.com/zephyrproject-rtos/zephyr/issues/21489) - Allow to read any types during discovery
- [GitHub #21484](https://github.com/zephyrproject-rtos/zephyr/issues/21484) - Option for safe k\_thread\_abort
- [GitHub #21342](https://github.com/zephyrproject-rtos/zephyr/issues/21342) - z\_arch\_cpu\_halt() should enter deep power-down where supported
- [GitHub #21293](https://github.com/zephyrproject-rtos/zephyr/issues/21293) - adding timeout the I2C read/write functions for the stm32 port
- [GitHub #21136](https://github.com/zephyrproject-rtos/zephyr/issues/21136) - ARC: Add support for reduced register file
- [GitHub #21061](https://github.com/zephyrproject-rtos/zephyr/issues/21061) - Document where APIs can be called from using doxygen
- [GitHub #21033](https://github.com/zephyrproject-rtos/zephyr/issues/21033) - Read out heap space used and unallocated
- [GitHub #20707](https://github.com/zephyrproject-rtos/zephyr/issues/20707) - Define GATT service at run-time
- [GitHub #20576](https://github.com/zephyrproject-rtos/zephyr/issues/20576) - DTS overlay files must include full path name
- [GitHub #20366](https://github.com/zephyrproject-rtos/zephyr/issues/20366) - Make babbelsim testing more easily available outside of CI
- [GitHub #19655](https://github.com/zephyrproject-rtos/zephyr/issues/19655) - Milestones toward generalized representation of timeouts
- [GitHub #19582](https://github.com/zephyrproject-rtos/zephyr/issues/19582) - zephyr\_library: missing ‘kernel-mode’ vs ‘app-mode’ documentation
- [GitHub #19340](https://github.com/zephyrproject-rtos/zephyr/issues/19340) - ARM: Cortex-M: Stack Overflows when building with NO\_OPTIMIZATIONS
- [GitHub #19244](https://github.com/zephyrproject-rtos/zephyr/issues/19244) - BLE throughput of DFU by Mcumgr is too slow
- [GitHub #19224](https://github.com/zephyrproject-rtos/zephyr/issues/19224) - deprecate spi\_flash\_w25qxxdv
- [GitHub #18934](https://github.com/zephyrproject-rtos/zephyr/issues/18934) - Update Documentation To Reflect No Concurrent Multi-Protocol
- [GitHub #18554](https://github.com/zephyrproject-rtos/zephyr/issues/18554) - Tracking Issue for C++ Support as of release 2.1
- [GitHub #18509](https://github.com/zephyrproject-rtos/zephyr/issues/18509) - Bluetooth:Mesh:Memory allocation is too large
- [GitHub #18351](https://github.com/zephyrproject-rtos/zephyr/issues/18351) - logging: 32 bit float values don’t work.
- [GitHub #17991](https://github.com/zephyrproject-rtos/zephyr/issues/17991) - Cannot generate coverage reports on qemu\_x86\_64
- [GitHub #17748](https://github.com/zephyrproject-rtos/zephyr/issues/17748) - stm32: clock-control: Remove usage of SystemCoreClock
- [GitHub #17745](https://github.com/zephyrproject-rtos/zephyr/issues/17745) - stm32: Move clock configuration to device tree
- [GitHub #17571](https://github.com/zephyrproject-rtos/zephyr/issues/17571) - mempool is expensive for cyclic use
- [GitHub #17486](https://github.com/zephyrproject-rtos/zephyr/issues/17486) - nRF52: SPIM: Errata work-around status?
- [GitHub #17375](https://github.com/zephyrproject-rtos/zephyr/issues/17375) - Add VREF, TEMPSENSOR, VBAT internal channels to the stm32 adc driver
- [GitHub #17353](https://github.com/zephyrproject-rtos/zephyr/issues/17353) - Configuring with POSIX\_API disables NET\_SOCKETS\_POSIX\_NAMES
- [GitHub #17314](https://github.com/zephyrproject-rtos/zephyr/issues/17314) - doc: add tutorial for using mbed TLS
- [GitHub #16539](https://github.com/zephyrproject-rtos/zephyr/issues/16539) - include/ directory and header cleanup
- [GitHub #16150](https://github.com/zephyrproject-rtos/zephyr/issues/16150) - Make more LWM2M parameters configurable at runtime
- [GitHub #15855](https://github.com/zephyrproject-rtos/zephyr/issues/15855) - Create a reliable footprint tracking benchmark
- [GitHub #15854](https://github.com/zephyrproject-rtos/zephyr/issues/15854) - Footprint Enhancements
- [GitHub #15738](https://github.com/zephyrproject-rtos/zephyr/issues/15738) - Networking with QEMU for mac
- [GitHub #15497](https://github.com/zephyrproject-rtos/zephyr/issues/15497) - USB DFU: STM32: usb dfu mode doesn’t work
- [GitHub #15134](https://github.com/zephyrproject-rtos/zephyr/issues/15134) - samples/boards/reel\_board/mesh\_badge/README.rst : No compilation or flash instructions
- [GitHub #14996](https://github.com/zephyrproject-rtos/zephyr/issues/14996) - enhance mutex tests
- [GitHub #14973](https://github.com/zephyrproject-rtos/zephyr/issues/14973) - samples: Specify the board target required for the sample
- [GitHub #14806](https://github.com/zephyrproject-rtos/zephyr/issues/14806) - Assorted pylint warnings in Python scripts
- [GitHub #14591](https://github.com/zephyrproject-rtos/zephyr/issues/14591) - Infineon Tricore architecture support
- [GitHub #14581](https://github.com/zephyrproject-rtos/zephyr/issues/14581) - Network interfaces should be able to declare if they work with IPv4 and IPv6 dynamically
- [GitHub #14442](https://github.com/zephyrproject-rtos/zephyr/issues/14442) - x86 SOC/CPU definitions need clean up.
- [GitHub #14309](https://github.com/zephyrproject-rtos/zephyr/issues/14309) - Automatic device dependency tracking
- [GitHub #19760](https://github.com/zephyrproject-rtos/zephyr/issues/19760) - Provide command to check board supported features
- [GitHub #13553](https://github.com/zephyrproject-rtos/zephyr/issues/13553) - Ways to reduce Bluetooth Mesh message loss
- [GitHub #13469](https://github.com/zephyrproject-rtos/zephyr/issues/13469) - Shell does not show ISR stack usage
- [GitHub #13436](https://github.com/zephyrproject-rtos/zephyr/issues/13436) - Enabling cooperative scheduling via menuconfig may result in an invalid configuration
- [GitHub #13091](https://github.com/zephyrproject-rtos/zephyr/issues/13091) - sockets: Implement MSG\_WAITALL flag
- [GitHub #12718](https://github.com/zephyrproject-rtos/zephyr/issues/12718) - Generic MbedTLS setup doesn’t use MBEDTLS\_ENTROPY\_C
- [GitHub #12098](https://github.com/zephyrproject-rtos/zephyr/issues/12098) - Not possible to print 64 bit decimal values with minimal libc
- [GitHub #12028](https://github.com/zephyrproject-rtos/zephyr/issues/12028) - Enable 16550 UART driver on x86\_64
- [GitHub #11820](https://github.com/zephyrproject-rtos/zephyr/issues/11820) - sockets: Implement (POSIX-compatible) timeout support
- [GitHub #11529](https://github.com/zephyrproject-rtos/zephyr/issues/11529) - Get configuration of a running kernel in console
- [GitHub #11449](https://github.com/zephyrproject-rtos/zephyr/issues/11449) - checkpatch warns on .dtsi files about line length
- [GitHub #11207](https://github.com/zephyrproject-rtos/zephyr/issues/11207) - ENOSYS has ambiguous meaning.
- [GitHub #10621](https://github.com/zephyrproject-rtos/zephyr/issues/10621) - RFC: Enable device by using dts, not Kconfig
- [GitHub #10499](https://github.com/zephyrproject-rtos/zephyr/issues/10499) - docs: References to “user threads” are confusing
- [GitHub #10494](https://github.com/zephyrproject-rtos/zephyr/issues/10494) - sockets: Implement MSG\_TRUNC flag for recv()
- [GitHub #10436](https://github.com/zephyrproject-rtos/zephyr/issues/10436) - Mess with ssize\_t, off\_t definitions
- [GitHub #10268](https://github.com/zephyrproject-rtos/zephyr/issues/10268) - Clean up remaining SPI\_DW defines in soc.h
- [GitHub #10042](https://github.com/zephyrproject-rtos/zephyr/issues/10042) - MISRA C - Do not cast an arithimetic type to void pointer
- [GitHub #10041](https://github.com/zephyrproject-rtos/zephyr/issues/10041) - MISRA C - types that indicate size and signedness should be used instead of basic numerical types
- [GitHub #10030](https://github.com/zephyrproject-rtos/zephyr/issues/10030) - MISRA C - Document Zephyr’s code guideline based on MISRA C 2012
- [GitHub #9954](https://github.com/zephyrproject-rtos/zephyr/issues/9954) - samples/hello\_world build failed on Windows/MSYS
- [GitHub #9895](https://github.com/zephyrproject-rtos/zephyr/issues/9895) - MISRA C Add ‘u’ or ‘U’ suffix for all unsigned integer constants
- [GitHub #9894](https://github.com/zephyrproject-rtos/zephyr/issues/9894) - MISRA C Make external identifiers distinct according with C99
- [GitHub #9889](https://github.com/zephyrproject-rtos/zephyr/issues/9889) - MISRA C Avoid implicit conversion between integers and boolean expressions
- [GitHub #9886](https://github.com/zephyrproject-rtos/zephyr/issues/9886) - MISRA C Do not mix signed and unsigned types
- [GitHub #9885](https://github.com/zephyrproject-rtos/zephyr/issues/9885) - MISRA C Do not have dead code
- [GitHub #9884](https://github.com/zephyrproject-rtos/zephyr/issues/9884) - MISRA-C Check return value of a non-void function
- [GitHub #9882](https://github.com/zephyrproject-rtos/zephyr/issues/9882) - MISRA-C - Do not use reserved names
- [GitHub #9778](https://github.com/zephyrproject-rtos/zephyr/issues/9778) - Implement zephyr specific SEGGER\_RTT\_LOCK and SEGGER\_RTT\_UNLOCK macros
- [GitHub #9626](https://github.com/zephyrproject-rtos/zephyr/issues/9626) - Add support for the FRDM-KL28Z board
- [GitHub #9507](https://github.com/zephyrproject-rtos/zephyr/issues/9507) - pwm: No clear semantics to stop a PWM leads to diverse implementations
- [GitHub #9284](https://github.com/zephyrproject-rtos/zephyr/issues/9284) - Issues/experience trying to use TI ARM code gen tools in Zephyr
- [GitHub #8958](https://github.com/zephyrproject-rtos/zephyr/issues/8958) - Bluetooth: Proprietary vendor specific opcode discovery
- [GitHub #8400](https://github.com/zephyrproject-rtos/zephyr/issues/8400) - test kernel XIP case seems not well defined
- [GitHub #8393](https://github.com/zephyrproject-rtos/zephyr/issues/8393) - `CONFIG_MULTITHREADING=n` builds call `main()` with interrupts locked
- [GitHub #7317](https://github.com/zephyrproject-rtos/zephyr/issues/7317) - Add generation of SPDX TagValue documents to each build
- [GitHub #7297](https://github.com/zephyrproject-rtos/zephyr/issues/7297) - STM32: Drivers: Document series support for each driver
- [GitHub #7246](https://github.com/zephyrproject-rtos/zephyr/issues/7246) - esp32 fails to build with xtensa-esp32-elf-gcc: error: unrecognized command line option ‘-no-pie’
- [GitHub #7216](https://github.com/zephyrproject-rtos/zephyr/issues/7216) - Stop using gcc’s “-include” flag
- [GitHub #7214](https://github.com/zephyrproject-rtos/zephyr/issues/7214) - Defines from DTS and Kconfig should be available simultaneously
- [GitHub #7151](https://github.com/zephyrproject-rtos/zephyr/issues/7151) - boards: Move existing boards to “default configuration guidelines”
- [GitHub #6925](https://github.com/zephyrproject-rtos/zephyr/issues/6925) - Provide Reviewer Guidelines as part of the documentation
- [GitHub #6291](https://github.com/zephyrproject-rtos/zephyr/issues/6291) - userspace: support MMU-based memory virtualization
- [GitHub #6066](https://github.com/zephyrproject-rtos/zephyr/issues/6066) - LwM2M: support object versioning in register / discover operations
- [GitHub #5517](https://github.com/zephyrproject-rtos/zephyr/issues/5517) - Expand toolchain/SDK support
- [GitHub #5325](https://github.com/zephyrproject-rtos/zephyr/issues/5325) - Support interaction with console in twister
- [GitHub #5116](https://github.com/zephyrproject-rtos/zephyr/issues/5116) - [Coverity CID: 179986] Null pointer dereferences in /subsys/bluetooth/host/mesh/access.c
- [GitHub #4911](https://github.com/zephyrproject-rtos/zephyr/issues/4911) - Filesystem support for qemu
- [GitHub #4569](https://github.com/zephyrproject-rtos/zephyr/issues/4569) - LoRa: support LoRa
- [GitHub #1418](https://github.com/zephyrproject-rtos/zephyr/issues/1418) - kconfig options need some cleanup and reorganisation
- [GitHub #1415](https://github.com/zephyrproject-rtos/zephyr/issues/1415) - Problem with forcing new line in generated documentation.
- [GitHub #1392](https://github.com/zephyrproject-rtos/zephyr/issues/1392) - No module named ‘elftools’
- [GitHub #3933](https://github.com/zephyrproject-rtos/zephyr/issues/3933) - LWM2M: Create application/link-format writer object to handle discovery formatting
- [GitHub #3931](https://github.com/zephyrproject-rtos/zephyr/issues/3931) - LWM2M: Data Validation Callback
- [GitHub #3723](https://github.com/zephyrproject-rtos/zephyr/issues/3723) - WiFi support for ESP32
- [GitHub #3675](https://github.com/zephyrproject-rtos/zephyr/issues/3675) - LE Adv. Ext.: Extended Scan with PHY selection for non-conn non-scan un-directed without aux packets
- [GitHub #3674](https://github.com/zephyrproject-rtos/zephyr/issues/3674) - LE Adv. Ext.: Non-Connectable and Non-Scannable Undirected without auxiliary packet
- [GitHub #3634](https://github.com/zephyrproject-rtos/zephyr/issues/3634) - ARM: implement NULL pointer protection
- [GitHub #3514](https://github.com/zephyrproject-rtos/zephyr/issues/3514) - Bluetooth: controller: LE Advertising Extensions
- [GitHub #3487](https://github.com/zephyrproject-rtos/zephyr/issues/3487) - Keep Zephyr Device tree Linux compatible
- [GitHub #3420](https://github.com/zephyrproject-rtos/zephyr/issues/3420) - Percepio Tracealyzer Support
- [GitHub #3280](https://github.com/zephyrproject-rtos/zephyr/issues/3280) - Paging Support
- [GitHub #2854](https://github.com/zephyrproject-rtos/zephyr/issues/2854) - Modbus RTU Support
- [GitHub #2542](https://github.com/zephyrproject-rtos/zephyr/issues/2542) - battery: Add standard APIs for Battery Charging and Fuel Gauge Handling (Energy Management)
- [GitHub #2470](https://github.com/zephyrproject-rtos/zephyr/issues/2470) - Supervisory and Monitoring Task
- [GitHub #2381](https://github.com/zephyrproject-rtos/zephyr/issues/2381) - SQL Database
- [GitHub #2336](https://github.com/zephyrproject-rtos/zephyr/issues/2336) - IPv4 - Multicast Join/Leave Support
