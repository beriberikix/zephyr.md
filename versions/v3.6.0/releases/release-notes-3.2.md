---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/releases/release-notes-3.2.html
original_path: releases/release-notes-3.2.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Zephyr 3.2.0

We are pleased to announce the release of Zephyr version 3.2.0.

Major enhancements with this release include:

- Introduced [Sysbuild (System build)](../build/sysbuild/index.md#sysbuild).
- Added support for [Binary Blobs](../contribute/bin_blobs.md#bin-blobs) (also see [Working with binary blobs: west blobs](../develop/west/zephyr-cmds.md#west-blobs)).
- Added support for Picolibc (see [`CONFIG_PICOLIBC`](../kconfig.md#CONFIG_PICOLIBC "CONFIG_PICOLIBC")).
- Converted all supported boards from `pinmux` to [Pin Control](../hardware/pinctrl/index.md#pinctrl-guide).
- Initial support for [Improved Inter-Integrated Circuit (I3C) Bus](../hardware/peripherals/i3c.md#i3c-api) controllers.
- Support for [W1 api](../hardware/peripherals/w1.md#w1-api).
- Improved access to Devicetree compatibles from Kconfig (new generated
  `DTS_HAS_..._ENABLED` configs).

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

- CVE-2022-2993: Under embargo until 2022-11-03
- CVE-2022-2741: Under embargo until 2022-10-14

## API Changes

### Changes in this release

- Zephyr now requires Python 3.8 or higher
- Changed [`spi_cs_control`](../hardware/peripherals/spi.md#c.spi_cs_control "spi_cs_control") to remove anonymous struct.
  This causes possible breakage for static initialization of the
  struct. Updated `SPI_CS_CONTROL_PTR_DT` to reflect
  this change.
- The `CONFIG_LEGACY_INCLUDE_PATH` option has been disabled by
  default, all upstream code and modules have been converted to use
  `<zephyr/...>` header paths. The option is still available to facilitate
  the migration of external applications, but will be removed with the 3.4
  release. The [scripts/utils/migrate\_includes.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/utils/migrate_includes.py) script is
  provided to automate the migration.
- [include/zephyr/zephyr.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/zephyr.h) no longer defines `__ZEPHYR__`.
  This definition can be used by third-party code to compile code conditional
  to Zephyr. The definition is already injected by the Zephyr build system.
  Therefore, any third-party code integrated using the Zephyr build system will
  require no changes. External build systems will need to inject the definition
  by themselves, if they did not already.
- [include/zephyr/zephyr.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/zephyr.h) has been deprecated in favor of
  [include/zephyr/kernel.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/kernel.h), since it only included that header. No
  changes are required by applications other than replacing `#include
  <zephyr/zephyr.h>` with `#include <zephyr/kernel.h>`.
- Bluetooth: Applications where [`CONFIG_BT_EATT`](../kconfig.md#CONFIG_BT_EATT "CONFIG_BT_EATT") is enabled
  must set the `chan_opt` field on the GATT parameter structs.
  To keep the old behavior use [`BT_ATT_CHAN_OPT_NONE`](../connectivity/bluetooth/api/att.md#c.bt_att_chan_opt.BT_ATT_CHAN_OPT_NONE "BT_ATT_CHAN_OPT_NONE").
- CAN

  - The Zephyr SocketCAN definitions have been moved from [include/zephyr/drivers/can.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/can.h)
    to [include/zephyr/net/socketcan.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/socketcan.h), the SocketCAN `struct can_frame` has been
    renamed to `socketcan_frame`, and the SocketCAN `struct can_filter` has been renamed
    to `socketcan_filter`. The SocketCAN utility functions are now available in
    [include/zephyr/net/socketcan\_utils.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/socketcan_utils.h).
  - The CAN controller `struct zcan_frame` has been renamed to [`can_frame`](../hardware/peripherals/can/controller.md#c.can_frame "can_frame"), and `struct
    zcan_filter` has been renamed to [`can_filter`](../hardware/peripherals/can/controller.md#c.can_filter "can_filter").
  - The [`can_state`](../hardware/peripherals/can/controller.md#c.can_state "can_state") enumerations have been renamed to contain the word STATE in order to make
    their context more clear:

    - `CAN_ERROR_ACTIVE` renamed to [`CAN_STATE_ERROR_ACTIVE`](../hardware/peripherals/can/controller.md#c.can_state.CAN_STATE_ERROR_ACTIVE "CAN_STATE_ERROR_ACTIVE").
    - `CAN_ERROR_WARNING` renamed to [`CAN_STATE_ERROR_WARNING`](../hardware/peripherals/can/controller.md#c.can_state.CAN_STATE_ERROR_WARNING "CAN_STATE_ERROR_WARNING").
    - `CAN_ERROR_PASSIVE` renamed to [`CAN_STATE_ERROR_PASSIVE`](../hardware/peripherals/can/controller.md#c.can_state.CAN_STATE_ERROR_PASSIVE "CAN_STATE_ERROR_PASSIVE").
    - `CAN_BUS_OFF` renamed to [`CAN_STATE_BUS_OFF`](../hardware/peripherals/can/controller.md#c.can_state.CAN_STATE_BUS_OFF "CAN_STATE_BUS_OFF").
  - The error code for [`can_send()`](../hardware/peripherals/can/controller.md#c.can_send "can_send") when the CAN controller is in bus off state has been
    changed from `-ENETDOWN` to `-ENETUNREACH`. A return value of `-ENETDOWN` now indicates
    that the CAN controller is in [`CAN_STATE_STOPPED`](../hardware/peripherals/can/controller.md#c.can_state.CAN_STATE_STOPPED "CAN_STATE_STOPPED").
  - The list of valid return values for the CAN timing calculation functions have been expanded to
    allow distinguishing between an out of range bitrate/sample point, an unsupported bitrate, and a
    resulting sample point outside the guard limit.
- Memory Management Drivers

  - Added `sys_mm_drv_update_page_flags()` and
    `sys_mm_drv_update_region_flags()` to update flags associated
    with memory pages and regions.

### Removed APIs in this release

- The following functions, macros, and structures related to the
  deprecated kernel work queue API have been removed:

  - `k_work_pending()`
  - `k_work_q_start()`
  - `k_delayed_work`
  - `k_delayed_work_init()`
  - `k_delayed_work_submit_to_queue()`
  - `k_delayed_work_submit()`
  - `k_delayed_work_pending()`
  - `k_delayed_work_cancel()`
  - `k_delayed_work_remaining_get()`
  - `k_delayed_work_expires_ticks()`
  - `k_delayed_work_remaining_ticks()`
  - `K_DELAYED_WORK_DEFINE`
- Removed support for enabling passthrough mode on MPU9150 to
  AK8975 sensor.
- Removed deprecated SPI [`spi_cs_control`](../hardware/peripherals/spi.md#c.spi_cs_control "spi_cs_control") fields for GPIO management
  that have been replaced with [`gpio_dt_spec`](../hardware/peripherals/gpio.md#c.gpio_dt_spec "gpio_dt_spec").
- Removed support for configuring the CAN-FD maximum DLC value via Kconfig
  `CONFIG_CANFD_MAX_DLC`.
- Removed deprecated civetweb module and the associated support code and samples.

### Deprecated in this release

- `DT_SPI_DEV_CS_GPIOS_LABEL` and
  `DT_INST_SPI_DEV_CS_GPIOS_LABEL` are deprecated in favor of
  utilizing [`DT_SPI_DEV_CS_GPIOS_CTLR`](../build/dts/api/api.md#c.DT_SPI_DEV_CS_GPIOS_CTLR "DT_SPI_DEV_CS_GPIOS_CTLR") and variants.
- `DT_GPIO_LABEL`, `DT_INST_GPIO_LABEL`,
  `DT_GPIO_LABEL_BY_IDX`, and `DT_INST_GPIO_LABEL_BY_IDX`,
  are deprecated in favor of utilizing [`DT_GPIO_CTLR`](../build/dts/api/api.md#c.DT_GPIO_CTLR "DT_GPIO_CTLR") and variants.
- `DT_LABEL`, and `DT_INST_LABEL`, are deprecated
  in favor of utilizing [`DT_PROP`](../build/dts/api/api.md#c.DT_PROP "DT_PROP") and variants.
- `DT_BUS_LABEL`, and `DT_INST_BUS_LABEL`, are deprecated
  in favor of utilizing [`DT_BUS`](../build/dts/api/api.md#c.DT_BUS "DT_BUS") and variants.
- STM32 LPTIM domain clock should now be configured using devicetree.
  Related Kconfig [`CONFIG_STM32_LPTIM_CLOCK`](../kconfig.md#CONFIG_STM32_LPTIM_CLOCK "CONFIG_STM32_LPTIM_CLOCK") option is now
  deprecated.
- `label` property from devicetree as a base property. The property is still
  valid for specific bindings to specify like [`gpio-leds`](../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) and
  [`fixed-partitions`](../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions).
- Bluetooth mesh Configuration Client API prefixed with `bt_mesh_cfg_`
  is deprecated in favor of a new API with prefix `bt_mesh_cfg_cli_`.
- Pinmux API is now officially deprecated in favor of the pin control API.
  Its removal is scheduled for the 3.4 release. Refer to [Pin Control](../hardware/pinctrl/index.md#pinctrl-guide)
  for more details on pin control.
- Flash Map API macros `FLASH_MAP_`, which have been using DTS node label
  property to reference partitions, have been deprecated and replaced with
  `FIXED_PARTITION_` which use DTS node label instead.
  Replacement list:

  | Deprecated, takes label property | Replacement, takes DTS node label |
  | --- | --- |
  | `FLASH_AREA_ID` | [`FIXED_PARTITION_ID`](../services/storage/flash_map/flash_map.md#c.FIXED_PARTITION_ID "FIXED_PARTITION_ID") |
  | `FLASH_AREA_OFFSET` | [`FIXED_PARTITION_OFFSET`](../services/storage/flash_map/flash_map.md#c.FIXED_PARTITION_OFFSET "FIXED_PARTITION_OFFSET") |
  | `FLASH_AREA_SIZE` | [`FIXED_PARTITION_SIZE`](../services/storage/flash_map/flash_map.md#c.FIXED_PARTITION_SIZE "FIXED_PARTITION_SIZE") |
  | `FLASH_AREA_LABEL_EXISTS` | [`FIXED_PARTITION_EXISTS`](../services/storage/flash_map/flash_map.md#c.FIXED_PARTITION_EXISTS "FIXED_PARTITION_EXISTS") |
  | [`FLASH_AREA_DEVICE`](../services/storage/flash_map/flash_map.md#c.FLASH_AREA_DEVICE "FLASH_AREA_DEVICE") | [`FIXED_PARTITION_DEVICE`](../services/storage/flash_map/flash_map.md#c.FIXED_PARTITION_DEVICE "FIXED_PARTITION_DEVICE") |

  `FLASH_AREA_LABEL_STR` is deprecated with no replacement as its sole
  purpose was to obtain the DTS node property label.

### Stable API changes in this release

### New APIs in this release

- CAN

  - Added [`can_start()`](../hardware/peripherals/can/controller.md#c.can_start "can_start") and [`can_stop()`](../hardware/peripherals/can/controller.md#c.can_stop "can_stop") API functions for starting and stopping a CAN
    controller. Applications will need to call [`can_start()`](../hardware/peripherals/can/controller.md#c.can_start "can_start") to bring the CAN controller out
    of [`CAN_STATE_STOPPED`](../hardware/peripherals/can/controller.md#c.can_state.CAN_STATE_STOPPED "CAN_STATE_STOPPED") before being able to transmit and receive CAN frames.
  - Added [`can_get_capabilities()`](../hardware/peripherals/can/controller.md#c.can_get_capabilities "can_get_capabilities") for retrieving a bitmask of the capabilities supported by a
    CAN controller.
  - Added [`CAN_MODE_ONE_SHOT`](../hardware/peripherals/can/controller.md#c.CAN_MODE_ONE_SHOT "CAN_MODE_ONE_SHOT") for enabling CAN controller one-shot transmission mode.
  - Added [`CAN_MODE_3_SAMPLES`](../hardware/peripherals/can/controller.md#c.CAN_MODE_3_SAMPLES "CAN_MODE_3_SAMPLES") for enabling CAN controller triple-sampling receive
    mode.
- I3C

  - Added a set of new API for I3C controllers.
- W1

  - Introduced the [W1 api](../hardware/peripherals/w1.md#w1-api), used to interact with 1-Wire masters.

## Kernel

- Source files using multiple `SYS_INIT` macros with the
  same initialisation function must now use `SYS_INIT_NAMED`
  with unique names per instance.

## Architectures

- ARC

  - Added support of non-multithreading mode for all UP ARC targets.
  - Added extra compile-time checks of [`CONFIG_ISR_STACK_SIZE`](../kconfig.md#CONFIG_ISR_STACK_SIZE "CONFIG_ISR_STACK_SIZE")
    and [`CONFIG_ARC_EXCEPTION_STACK_SIZE`](../kconfig.md#CONFIG_ARC_EXCEPTION_STACK_SIZE "CONFIG_ARC_EXCEPTION_STACK_SIZE") value.
  - Added support of generation symbol file for ARC MWDT toolchain variant.
  - Added ARC MWDT toolchain version check.
  - Added support for GCC mcpu option tuning for ARC targets on SoC level.
  - Switched ARCv3 64bit targets for usage of new linker output format value.
  - Added ARCv3 64bit accumulator reg save / restore, cleanup it for ARCv3
    32bit targets.
  - Fixed SMP race in ASM ARC interrupt handling code.
- ARM

  - Improved HardFault handling on Cortex-M.
  - Enabled automatic placement of the IRQ vector table.
  - Enabled S2RAM for Cortex-M, hooking up the provided API functions.
  - Added icache and dcache maintenance functions, and switched to the new
    Kconfig symbols ([`CONFIG_CPU_HAS_DCACHE`](../kconfig.md#CONFIG_CPU_HAS_DCACHE "CONFIG_CPU_HAS_DCACHE") and
    [`CONFIG_CPU_HAS_ICACHE`](../kconfig.md#CONFIG_CPU_HAS_ICACHE "CONFIG_CPU_HAS_ICACHE")).
  - Added data/instr. sync barriers after writing to `SCTLR` to disable MPU.
  - Use `spsr_cxsf` instead of unpredictable `spsr_hyp` on Cortex-R52.
  - Removes `-Wstringop-overread` warning with GCC 12.
  - Fixed handling of system off failure.
  - Fixed issue with incorrect `ssf` under bad syscall.
  - Fixed region check issue with mmu.
- ARM64

  - [`arch_mem_map()`](../hardware/porting/arch.md#c.arch_mem_map "arch_mem_map") now supports [`K_MEM_PERM_USER`](../kernel/memory_management/virtual_memory.md#c.K_MEM_PERM_USER "K_MEM_PERM_USER").
  - Added [`CONFIG_WAIT_AT_RESET_VECTOR`](../kconfig.md#CONFIG_WAIT_AT_RESET_VECTOR "CONFIG_WAIT_AT_RESET_VECTOR") to spin at reset vector
    allowing a debugger to be attached.
  - Implemented erratum 822227 “Using unsupported 16K translation granules
    might cause Cortex-A57 to incorrectly trigger a domain fault”.
  - Enabled single-threaded support for some platforms.
  - IRQ stack is now initialized when [`CONFIG_INIT_STACKS`](../kconfig.md#CONFIG_INIT_STACKS "CONFIG_INIT_STACKS") is set.
  - Fixed issue when cache API are used from userspace.
  - Fixed issue about the way IPI are delivered.
  - TF-A (TrustedFirmware-A) is now shipped as module.
- RISC-V

  - Introduced support for RV32E.
  - Reduced callee-saved registers for RV32E.
  - Introduced Zicsr, Zifencei and BitManip as separate extensions.
  - Introduced [`CONFIG_RISCV_ALWAYS_SWITCH_THROUGH_ECALL`](../kconfig.md#CONFIG_RISCV_ALWAYS_SWITCH_THROUGH_ECALL "CONFIG_RISCV_ALWAYS_SWITCH_THROUGH_ECALL") for
    platforms that require every `mret` to be balanced by `ecall`.
  - IRQ vector table is now used for vectored mode.
  - Disabled [`CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_CODE`](../kconfig.md#CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_CODE "CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_CODE") for CLIC.
  - `STRINGIFY` macro is now used for CSR helpers.
  - [`CONFIG_CODE_DATA_RELOCATION`](../kconfig.md#CONFIG_CODE_DATA_RELOCATION "CONFIG_CODE_DATA_RELOCATION") is now supported.
  - PLIC and CLIC are now decoupled.
  - `jedec,spi-nor` is no longer required to be `okay` by the RISC-V arch
    linker script.
  - Removed usage of `SOC_ERET`.
  - Removed usage of `ulong_t`.
  - Added new TLS-based [`arch_is_user_context()`](../hardware/porting/arch.md#c.arch_is_user_context "arch_is_user_context") implementation.
  - Fixed PMP for builds with SMP enabled.
  - Fixed the per-thread m-mode/u-mode entry array.
  - [`semihost_exec()`](../hardware/arch/semihost.md#c.semihost_exec "semihost_exec") function is now aligned at 16-byte boundary.
- Xtensa

  - Macros `RSR` and `WSR` have been renamed to `XTENSA_RSR`
    and `XTENSA_WSR` to give them proper namespace.
  - Fixed a rounding error in timing function when converting from cycles
    to nanoseconds.
  - Fixed the calculation of average “cycles to nanoseconds” to actually
    return nanoseconds instead of cycles.

## Bluetooth

- Audio

  - Implemented central security establishment when required.
  - Added additional security level options to the connection call.
  - Switched the unicast client and server to bidirectional CIS if available.
  - Added a new RSI advertising callback for CSIS.
  - Added multiple improvements to context handling, including public functions
    to get contexts.
  - Added ordered access procedure for the CSIS client, as well as storing
    active members by rank.
  - Added support for Write Preset Name in HAS.
  - Added support for using PACS for the broadcast sink role.
  - Cleaned up the MICP implementation, including renaming several structures
    and functions.
  - Implemented the CAP Acceptor role.
  - Added ASCS Metadata verification support.
  - Started exposing broadcast sink advertising data to the application.
  - Added support for unicast server start, reconfigure, release, disable and
    metadata.
  - Added support for multi-CIS.
  - Implemented HAS client support for preset switching.
  - Added support for setting vendor-specific non-HCI data paths for audio
    streams.
- Direction Finding

  - Added support for selectable IQ samples conversion to 8-bit.
  - Added support for VS IQ sample reports in `int16_t` format.
- Host

  - Added support for LE Secure Connections permission checking.
  - Added support for Multiple Variable Length Read procedure without EATT.
  - Added a new callback `rpa_expired()` in the struct
    [`bt_le_ext_adv_cb`](../connectivity/bluetooth/api/gap.md#c.bt_le_ext_adv_cb "bt_le_ext_adv_cb") to enable synchronization of the advertising
    payload updates with the Resolvable Private Address (RPA) rotations when
    the [`CONFIG_BT_PRIVACY`](../kconfig.md#CONFIG_BT_PRIVACY "CONFIG_BT_PRIVACY") is enabled.
  - Added a new [`bt_le_set_rpa_timeout()`](../connectivity/bluetooth/api/gap.md#c.bt_le_set_rpa_timeout "bt_le_set_rpa_timeout") API call to dynamically change
    the Resolvable Private Address (RPA) timeout when the
    [`CONFIG_BT_RPA_TIMEOUT_DYNAMIC`](../kconfig.md#CONFIG_BT_RPA_TIMEOUT_DYNAMIC "CONFIG_BT_RPA_TIMEOUT_DYNAMIC") is enabled.
  - Added [`bt_conn_auth_cb_overlay()`](../connectivity/bluetooth/api/connection_mgmt.md#c.bt_conn_auth_cb_overlay "bt_conn_auth_cb_overlay") to overlay authentication callbacks
    for a Bluetooth LE connection.
  - Removed `CONFIG_BT_HCI_ECC_STACK_SIZE`. A new Bluetooth long workqueue
    ([`CONFIG_BT_LONG_WQ`](../kconfig.md#CONFIG_BT_LONG_WQ "CONFIG_BT_LONG_WQ")) is used for processing ECC commands
    instead of the former dedicated thread.
  - [`bt_conn_get_security()`](../connectivity/bluetooth/api/connection_mgmt.md#c.bt_conn_get_security "bt_conn_get_security") and [`bt_conn_enc_key_size()`](../connectivity/bluetooth/api/connection_mgmt.md#c.bt_conn_enc_key_size "bt_conn_enc_key_size") now take
    a `const struct bt_conn*` argument.
  - The handling of GATT multiple notifications has been rewritten, and is now
    only to be used as a low-level API.
  - Added support for GATT CCCs in arbitrary locations as a client.
  - Extended the [`bt_conn_info`](../connectivity/bluetooth/api/connection_mgmt.md#c.bt_conn_info "bt_conn_info") structure with security information.
  - Added a new [`CONFIG_BT_PRIVACY_RANDOMIZE_IR`](../kconfig.md#CONFIG_BT_PRIVACY_RANDOMIZE_IR "CONFIG_BT_PRIVACY_RANDOMIZE_IR") that prevents
    the Host from using Controller-provided identity roots.
  - Added support for GATT over EATT.
  - Implemented the Immediate Alert Client.
- Mesh

  - Added support for selectable RPL backends.
  - Changed the way segmented messages are sent, avoiding bulk transmission.
  - Added an async config client API.
  - Added model publish support to the Health Client.
  - Moved relayed messages to a separate buffer pool.
  - Reduced delay of sending segment acknowledge message. Set
    `CONFIG_BT_MESH_SEG_ACK_PER_SEGMENT_TIMEOUT` to 100 to get
    the previous timing.
  - Restructured shell commands.
- Controller

  - Made the new LLCP implementation the default one. Enable
    `CONFIG_BT_LL_SW_LLCP_LEGACY` to revert back to the legacy
    implementation. `CONFIG_BT_LL_SW_LLCP_LEGACY` is marked
    deprecated in favor of the new `CONFIG_BT_LL_SW_LLCP`, which
    is the default now.
  - Marked Extended Advertising as stable, no longer experimental.
  - Added deinit() infrastructure in order to properly support disabling
    Bluetooth support, including the controller.
  - Implemented the Peripheral CIS Create procedure.
  - Implemented the CIS Terminate procedure.
  - Added support for Periodic Advertising ADI.
  - Implemented support for Extended Scan Response Data fragment operations.
  - Enable back-to-back PDU chaining for AD data.
  - Added a new [`CONFIG_BT_CTLR_SYNC_PERIODIC_SKIP_ON_SCAN_AUX`](../kconfig.md#CONFIG_BT_CTLR_SYNC_PERIODIC_SKIP_ON_SCAN_AUX "CONFIG_BT_CTLR_SYNC_PERIODIC_SKIP_ON_SCAN_AUX")
    for allowing periodic sync event skipping.
  - Added a new [`CONFIG_BT_CTLR_SCAN_AUX_SYNC_RESERVE_MIN`](../kconfig.md#CONFIG_BT_CTLR_SCAN_AUX_SYNC_RESERVE_MIN "CONFIG_BT_CTLR_SCAN_AUX_SYNC_RESERVE_MIN") for
    minimal time reservation.
  - Implemented ISO Test Mode HCI commands.
  - Added support for multiple BIS sync selection within a BIG.
  - Implement flushing pending ISO TX PDUs when a BIG event is terminated.
  - Added a new [`CONFIG_BT_CTLR_ADV_DATA_CHAIN`](../kconfig.md#CONFIG_BT_CTLR_ADV_DATA_CHAIN "CONFIG_BT_CTLR_ADV_DATA_CHAIN") to enable
    experimental Advertising Data chaining support.
- HCI Driver

  - Added a new Telink B91 HCI driver.

## Boards & SoC Support

- Added support for these SoC series:

  - Atmel SAML21, SAMR34, SAMR35
  - GigaDevice GD32E50X
  - GigaDevice GD32F470
  - NXP i.MX8MN, LPC55S36, LPC51U68
  - renesas\_smartbond da1469x SoC series
- Made these changes in other SoC series:

  - gigadevice: Enable SEGGER RTT
  - Raspberry Pi Pico: Added ADC support
  - Raspberry Pi Pico: Added PWM support
  - Raspberry Pi Pico: Added SPI support
  - Raspberry Pi Pico: Added watchdog support
- Changes for ARC boards:

  - Added support for qemu\_arc\_hs5x board (ARCv3, 32bit, UP, HS5x)
  - Simplified multi-runner setup for SMP nSIM ARC platforms
  - Fixed mdb execution folder for mdb-based west runners (mdb-nsim and mdb-hw)
- Added support for these ARM boards:

  - Arduino MKR Zero
  - Atmel atsaml21\_xpro
  - Atmel atsamr34\_xpro
  - Blues Wireless Swan
  - Digilent Zybo
  - EBYTE E73-TBB
  - GigaDevice GD32E507V-START
  - GigaDevice GD32E507Z-EVAL
  - GigaDevice GD32F407V-START
  - GigaDevice GD32F450V-START
  - GigaDevice GD32F450Z-EVAL
  - GigaDevice GD32F470I-EVAL
  - NXP lpcxpresso51u68, RT1060 EVKB
  - NXP lpcxpresso55s36
  - Olimex LoRa STM32WL DevKit
  - PAN1770 Evaluation Board
  - PAN1780 Evaluation Board
  - PAN1781 Evaluation Board
  - PAN1782 Evaluation Board
  - ST STM32F7508-DK Discovery Kit
  - TDK RoboKit 1
  - WeAct Studio Black Pill V1.2
  - WeAct Studio Black Pill V3.0
  - XIAO BLE
  - da1469x\_dk\_pro
- Added support for these ARM64 boards:

  - i.MX8M Nano LPDDR4 EVK board series
- Added support for these RISC-V boards:

  - ICE-V Wireless
  - RISCV32E Emulation (QEMU)
- Added support for these Xtensa boards:

  - ESP32-NET
  - intel\_adsp\_ace15\_mtpm
- Removed support for these Xtensa boards:

  - Intel S1000
- Made these changes in other boards:

  - sam\_e70\_xplained: Uses EEPROM devicetree bindings for Ethernet MAC
  - sam\_v71\_xult: Uses EEPROM devicetree bindings for Ethernet MAC
  - rpi\_pico: Added west runner configurations for Picoprobe, Jlink and Blackmagicprobe
- Added support for these following shields:

  - ARCELI W5500 ETH
  - MAX7219 LED display driver shield
  - Panasonic Grid-EYE (AMG88xx)

## Build system and infrastructure

- Introduced sysbuild, a new higher-level build system layer that enables
  combining multiple build systems together. It can be used to generate multiple
  images from a single build system invocation while maintaining a link between
  those different applications/images via a shared Kconfig layer.
- Introduced support for binary blobs in west, via a new `west blobs` command
  that allows users to list, fetch and delete binary blobs from their
  filesystem. Vendors can thus now integrate binary blobs, be it images or
  libraries, with upstream Zephyr.
- Removed deprecated `GCCARMEMB_TOOLCHAIN_PATH` setting.

## Drivers and Sensors

- ADC

  - STM32: Now supports Vbat monitoring channel and STM32U5 series.
  - Added driver for GigaDevice GD32 SoCs.
  - Raspberry Pi Pico: Added ADC support for the Pico series.
  - Added [`adc_dt_spec`](../hardware/peripherals/adc.md#c.adc_dt_spec "adc_dt_spec") related helpers for sequence initialization,
    setting up channels, and converting raw values to millivolts.
  - Fixed [`ADC_DT_SPEC_GET`](../hardware/peripherals/adc.md#c.ADC_DT_SPEC_GET "ADC_DT_SPEC_GET") and related macros to properly handle
    channel identifiers >= 10.
- CAN

  - A driver for bridging from [Native POSIX execution (native\_posix)](../boards/posix/native_posix/doc/index.md#native-posix) to Linux SocketCAN has been added.
  - A driver for the Espressif ESP32 TWAI has been added. See the
    [`espressif,esp32-twai`](../build/dts/api/bindings/can/espressif%2Cesp32-twai.md#std-dtcompatible-espressif-esp32-twai) devicetree binding for more information.
  - The STM32 CAN-FD CAN driver clock configuration has been moved from Kconfig to [devicetree](../build/dts/index.md#dt-guide). See the [`st,stm32-fdcan`](../build/dts/api/bindings/can/st%2Cstm32-fdcan.md#std-dtcompatible-st-stm32-fdcan) devicetree binding for more information.
  - The filter handling of STM32 bxCAN driver has been simplified and made more reliable.
  - The STM32 bxCAN driver now supports dual instances.
  - The CAN loopback driver now supports CAN-FD.
  - The CAN shell module has been rewritten to properly support the additions and changes to the CAN
    controller API.
  - The Zephyr network CAN bus driver, which provides raw L2 access to the CAN bus via a CAN
    controller driver, has been moved to [drivers/net/canbus.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/canbus.c) and can now be enabled
    using [`CONFIG_NET_CANBUS`](../kconfig.md#CONFIG_NET_CANBUS "CONFIG_NET_CANBUS").
  - Added CAN support for NXP LPC55S36.
- Clock control

  - STM32: PLL\_P, PLL\_Q, PLL\_R outputs can now be used as domain clock.
  - Added driver for GigaDevice GD32 SoCs (peripheral clocks configuration only).
  - Documented behavior when clock is not on.
- Counter

  - Added [`counter_get_value_64()`](../hardware/peripherals/counter.md#c.counter_get_value_64 "counter_get_value_64") function.
  - STM32: RTC : Now supports STM32U5 and STM32F1 series.
  - STM32: Timer : Now supports STM32L4 series.
  - Added counter support using CTimer for NXP MIMXRT595.
  - ESP32: Added support to Pulse Counter Mode (PCNT) and RTC.
- Crypto

  - Added Intel ADSP sha driver.
  - stm32: Check if clock device is ready before accessing clock control
    devices.
  - ataes132a: Convert to devicetree.
- DFU

  - Fixed fetch of the flash write block size from incorrect device by
    `flash_img`.
  - Fixed possible build failure in the image manager for mcuboot on
    redefinitions of `BOOT_MAX_ALIGN` and `BOOT_MAGIC_SZ`.
- Display

  - Renamed EPD controller driver GD7965 to UC81xx.
  - Improved support for different controllers in ssd16xx and uc81xx drivers.
  - Added basic read support for ssd16xx compatible EPD controllers.
  - Revised intel\_multibootfb driver.
  - Added MAX7219 display controller driver.
- Disk

  - Added support for DMA transfers when using STM32 SD host controller.
  - Added support for SD host controller present on STM32L5X family.
- DMA

  - STM32: Now supports stm32u5 series.
  - cAVS drivers renamed with the broader Intel ADSP naming.
  - Kconfig depends on improvements with device tree statuses.
  - Added driver for GigaDevice GD32 SoCs.
  - Added DMA support for NXP MIMXRT595.
- EEPROM

  - Added Microchip XEC (MEC172x) on-chip EEPROM driver. See the
    [`microchip,xec-eeprom`](../build/dts/api/bindings/mtd/microchip%2Cxec-eeprom.md#std-dtcompatible-microchip-xec-eeprom) devicetree binding for more information.
- Entropy

  - Update drivers to use devicetree Kconfig symbol.
  - gecko: Add driver using Secure Element module of EFR3.
  - Added entropy driver for MCUX CAAM.
  - stm32: Check if clock device is ready before accessing.
- ESPI

  - eSPI emulator initialization improvements.
  - Nuvoton: Enabled platform specific Virtual Wire GPIO.
  - Microchip: Added XEC (MEC152x) overcurrent platform-specific virtual wires.
  - Nuvoton: Added driver flash channel operations support.
- Ethernet

  - Atmel gmac: Add EEPROM devicetree bindings for MAC address.
  - Performance improvements on the NXP MCUX Ethernet Driver.
- Flash

  - Atmel eefc: Fix support for Cortex-M4 variants.
  - Added flash driver for Renesas Smartbond platform
  - Added support for STM32H7 and STM32U5 in the STM32 OSPI driver.
  - Added DMA transfer support in the STM32 OSPI driver.
  - Added driver for GigaDevice GD32 SoCs
  - Added Flash support for NXP LPCXpresso55S36.
  - Added Flash support for NXP MIMXRT595 EVK.
  - Added on-chip flash driver for TI CC13xx/CC26xx.
  - Fixed flash to flash write for Telink B91.
  - Fixed DMA priority configuration in the stm32 QSPI driver.
  - Drivers are enabled by default based on their devicetree hardware declarations.
  - Fixed write from unaligned source for STM32G0x.
  - Added Flash support for Renesas Smartbond platform.
  - Added Flash support for Cadence QSPI NOR FLASH.
  - Fixed usage fault on nRF driver (along with BLE) due to possible incorrect handling of the ticker stop operation.
- GPIO

  - Added GPIO driver for Renesas Smartbond platform.
- I2C

  - Terminology updated to latest i2c specification removing master/slave
    terminology and replacing with controller/target terminology.
  - Asynchronous APIs added for requesting i2c transactions without
    waiting for the completion of them.
  - Added NXP LPI2C driver asynchronous i2c implementation with sample
    showing usage with a FRDM-K64F board.
  - STM32: support for second target address was added.
  - Kconfig depends on improvements with device tree statuses.
  - Improved ITE I2C support with FIFO and command queue mode.
  - Improve gd32 driver stability (remove repeated START, use STOP + START conditions instead).
  - Fixed gd32 driver incorrect Fast-mode config.
  - Add bus recovery support to the NXP MCUX LPI2C driver.
  - Enable I2C support on NXP MIMXRT595 EVK.
- I2S

  - Removed the Intel S1000 I2S driver.
- I3C

  - Added a driver to support the NXP MCUX I3C hardware acting as the primary controller
    on the bus (tested using RT685).
- IEEE 802.15.4

  - All IEEE 802.15.4 drivers have been converted to Devicetree-based drivers.
  - Atmel AT86RF2xx: Add Power Table on devicetree.
  - Atmel AT86RF2xx: Add support to RF212/212B Sub-Giga devices.
- Interrupt Controller

  - Added support for ACE V1X.
  - Fixed an addressing issue on GICv3 controllers.
  - Removed support for `intel_s1000_crb`.
- IPM

  - Kconfig is split into smaller, vendor oriented files.
  - Support for Intel S1000 in cAVS IDC driver has been removed as the board
    `intel_s1000_crb` has been removed.
- KSCAN

  - Enabled the touch panel on the NXP MIMXRT1170 EVK.
- LED

  - Added support for using multiple instances of LP5562 LED module.
  - Devicetree usage cleanups.
  - i2c\_dt\_spec migration.
  - Updated LED PWM support for ESP32 boards.
- LoRa

  - Added support for setting the sync-word and iq-inverted modes in LoRa modems.
  - Removed `REQUIRES_FULL_LIBC` library dependency from LoRa drivers. This
    results in considerable flash memory savings.
  - Devicetree usage cleanups.
- MEMC

  - Added support for Atmel SAM SMC/EBI.
- PCIE

  - Added a `dump` subcommand to the `pcie` shell command to print out
    the first 16 configuration space registers.
  - Added a `ls` subcommand to the `pcie` shell command to list
    devices.
- PECI

  - Added PECI driver for Nuvoton NPCX family.
  - Devicetree binding for ITE it8xxx2 PECI driver has changed from
    `ite,peci-it8xxx2` to [`ite,it8xxx2-peci`](../build/dts/api/bindings/peci/ite%2Cit8xxx2-peci.md#std-dtcompatible-ite-it8xxx2-peci) so that this aligns
    with other ITE devices.
- Pin control

  - Added driver for Infineon XMC4XXX.
  - Added driver for Renesas Smartbond platform.
  - Added driver for Xilinx Zynq-7000.
  - Added support for PSL pads in NPCX driver.
  - MEC15XX driver now supports both MEC15XX and MEC17XX.
  - nRF driver now supports disconnecting a pin by using `NRF_PSEL_DISCONNECT`.
  - nRF driver will use S0D1 drive mode for TWI/TWIM pins by default.
- PWM

  - Added PWM driver for Renesas R-Car platform.
  - Added PWM driver for Raspberry Pi Pico series.
  - Added PWM support for NXP LPC55S36.
  - Added MCPWM support for ESP32 boards.
  - Fixed the nRF PWM driver to properly handle cases where PWM generation is
    used for some channels while some others are set to a constant level (active
    or inactive), e.g. when the LED driver API is used to turn off a PWM driven
    LED while another one (within the same PWM instance) is blinking.
- Power Domain

  - Enabled access to the PMIC on NXP MXRT595 EVK.
  - Added soft off mode to the RT10xx Power Management.
  - Added support for power gating for Intel ADSP devices.
- Reset

  - Added driver for GigaDevice GD32 SoCs.
- SDHC

  - Added SDHC driver for NXP LPCXpresso platform.
  - Added support for card busy signal in SDHC SPI driver, to support
    the [File System API](../services/file_system/index.md#file-system-api).
- Sensor

  - Converted drivers to use Kconfig ‘select’ instead of ‘depends on’ for I2C,
    SPI, and GPIO dependencies.
  - Converted drivers to use I2C, SPI, and GPIO dt\_spec helpers.
  - Added multi-instance support to various drivers.
  - Added DS18B20 1-wire temperature sensor driver.
  - Added Würth Elektronik WSEN-HIDS driver.
  - Fixed unit conversion in the ADXL345 driver.
  - Fixed TTE and TTF time units in the MAX17055 driver.
  - Removed MPU9150 passthrough support from the AK8975 driver.
  - Changed the FXOS8700 driver default mode from accel-only to hybrid.
  - Enhanced the ADXL345 driver to support SPI.
  - Enhanced the BQ274XX driver to support the data ready interrupt trigger.
  - Enhanced the INA237 driver to support triggered mode.
  - Enhanced the LPS22HH driver to support being on an I3C bus.
  - Enhanced the MAX17055 driver to support VFOCV.
- Serial

  - Added serial driver for Renesas Smartbond platform.
  - The STM32 driver now allows to use serial device as stop mode wake up source.
  - Added check for clock control device readiness during configuration
    for various drivers.
  - Various fixes on `lpuart`.
  - Added a workaround on bytes dropping on `nrfx_uarte`.
  - Fixed compilation error on `uart_pl011` when interrupt is disabled.
  - Added power management support on `stm32`.
  - `xlnx_ps` has moved to using `DEVICE_MMIO` API.
  - `gd32` now supports using reset API to reset hardware and clock
    control API to enable UART clock.
- SPI

  - Add interrupt-driven mode support for gd32 driver.
  - Enable SPI support on NXP MIMXRT595 EVK.
  - PL022: Added SPI driver for the PL022 peripheral.
- Timer

  - STM32 LPTIM based timer should now be configured using device tree.
- USB

  - Restructured the NXP MCUX USB driver.
  - Added USB support for NXP MXRT595.
  - Fixed detach behavior in nRF USBD and Atmel SAM drivers.
- W1

  - Added Zephyr-Serial 1-Wire master driver.
  - Added DS2484 1-Wire master driver. See the [`maxim,ds2484`](../build/dts/api/bindings/w1/maxim%2Cds2484.md#std-dtcompatible-maxim-ds2484)
    devicetree binding for more information.
  - Added DS2485 1-Wire master driver. See the [`maxim,ds2485`](../build/dts/api/bindings/w1/maxim%2Cds2485.md#std-dtcompatible-maxim-ds2485)
    devicetree binding for more information.
  - Introduced a shell module for 1-Wire.
- Watchdog

  - Added support for Raspberry Pi Pico watchdog.
  - Added watchdog support on NXP MIMXRT595 EVK.
- WiFi

  - Added ESP32 WiFi integration to Wi-Fi API management.

## Networking

- CoAP:

  - Replaced constant CoAP retransmission count and acknowledgment random factor
    with configurable [`CONFIG_COAP_ACK_RANDOM_PERCENT`](../kconfig.md#CONFIG_COAP_ACK_RANDOM_PERCENT "CONFIG_COAP_ACK_RANDOM_PERCENT") and
    [`CONFIG_COAP_MAX_RETRANSMIT`](../kconfig.md#CONFIG_COAP_MAX_RETRANSMIT "CONFIG_COAP_MAX_RETRANSMIT").
  - Updated [`coap_packet_parse()`](../connectivity/networking/api/coap.md#c.coap_packet_parse "coap_packet_parse") and [`coap_handle_request()`](../connectivity/networking/api/coap.md#c.coap_handle_request "coap_handle_request") to
    return different error code based on the reason of parsing error.
- Ethernet:

  - Added EAPoL and IEEE802154 Ethernet protocol types.
- HTTP:

  - Improved API documentation.
- LwM2M:

  - Moved LwM2M 1.1 support out of experimental.
  - Refactored SenML-JSON and JSON encoder/decoder to use Zephyr’s JSON library
    internally.
  - Extended LwM2M shell module with the following commands: `exec`, `read`,
    `write`, `start`, `stop`, `update`, `pause`, `resume`.
  - Refactored LwM2M engine module into smaller sub-modules: LwM2M registry,
    LwM2M observation, LwM2M message handling.
  - Added an implementation of the LwM2M Access Control object (object ID 2).
  - Added support for LwM2M engine pause/resume.
  - Improved API documentation of the LwM2M engine.
  - Improved thread safety of the LwM2M library.
  - Added [`lwm2m_registry_lock()`](../connectivity/networking/api/lwm2m.md#c.lwm2m_registry_lock "lwm2m_registry_lock") and [`lwm2m_registry_unlock()`](../connectivity/networking/api/lwm2m.md#c.lwm2m_registry_unlock "lwm2m_registry_unlock")
    functions, which allow to update multiple resources w/o sending a
    notification for every update.
  - Multiple minor fixes/improvements.
- Misc:

  - `CONFIG_NET_CONFIG_IEEE802154_DEV_NAME` has been removed in favor of
    using a Devicetree choice given by `zephyr,ieee802154`.
  - Fixed net\_pkt leak with shallow clone.
  - Fixed websocket build with [`CONFIG_POSIX_API`](../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API").
  - Extracted zperf shell commands into a library.
  - Added support for building and using IEEE 802.15.4 L2 without IP support.
  - General clean up of inbound packet handling.
  - Added support for restarting DHCP w/o randomized delay.
  - Fixed a bug, where only one packet could be queued on a pending ARP
    request.
- OpenThread:

  - Moved OpenThread glue code into `modules` directory.
  - Fixed OpenThread build with [`CONFIG_NET_MGMT_EVENT_INFO`](../kconfig.md#CONFIG_NET_MGMT_EVENT_INFO "CONFIG_NET_MGMT_EVENT_INFO")
    disabled.
  - Fixed mbed TLS configuration for Service Registration Protocol (SRP)
    OpenThread feature.
  - Added Kconfig option to enable Thread 1.3 support
    ([`CONFIG_OPENTHREAD_THREAD_VERSION_1_3`](../kconfig.md#CONFIG_OPENTHREAD_THREAD_VERSION_1_3 "CONFIG_OPENTHREAD_THREAD_VERSION_1_3")).
  - Updated `otPlatSettingsSet()` according to new API documentation.
  - Added new Kconfig options:

    - [`CONFIG_OPENTHREAD_MESSAGE_BUFFER_SIZE`](../kconfig.md#CONFIG_OPENTHREAD_MESSAGE_BUFFER_SIZE "CONFIG_OPENTHREAD_MESSAGE_BUFFER_SIZE")
    - [`CONFIG_OPENTHREAD_MAC_STAY_AWAKE_BETWEEN_FRAGMENTS`](../kconfig.md#CONFIG_OPENTHREAD_MAC_STAY_AWAKE_BETWEEN_FRAGMENTS "CONFIG_OPENTHREAD_MAC_STAY_AWAKE_BETWEEN_FRAGMENTS")
- Sockets:

  - Fixed filling of the address structure provided in [`recvfrom()`](../connectivity/networking/api/sockets.md#c.recvfrom "recvfrom") for
    packet socket.
  - Fixed a potential deadlock in TCP [`send()`](../connectivity/networking/api/sockets.md#c.send "send") call.
  - Added support for raw 802.15.4 packet socket.
- TCP:

  - Added support for Nagle’s algorithm.
  - Added “Silly Window Syndrome” avoidance.
  - Fixed MSS calculation.
  - Avoid unnecessary packet cloning on the RX path.
  - Implemented randomized retransmission timeouts and exponential backoff.
  - Fixed out-of-order data processing.
  - Implemented fast retransmit algorithm.
  - Multiple minor fixes/improvements.
- Wi-Fi

  - Added support for using offloaded wifi\_mgmt API with native network stack.
  - Extended Wi-Fi headers with additional Wi-Fi parameters (security, bands,
    modes).
  - Added new Wi-Fi management APIs for retrieving status and statistics.

## USB

> - Minor bug fixes and improvements in class implementations CDC ACM, DFU, and MSC.
>   Otherwise no significant changes.

## Devicetree

- Use of the devicetree *label property* has been deprecated, and the property
  has been made optional in almost all bindings throughout the tree.

  In previous versions of zephyr, label properties like this commonly appeared
  in devicetree files:

  ```dts
  foo {
          label = "FOO";
          /* ... */
  };
  ```

  You could then use something like the following to retrieve a device
  structure for use in the [Device Driver Model](../kernel/drivers/index.md#device-model-api):

  ```c
  const struct device *my_dev = device_get_binding("FOO");
  if (my_dev == NULL) {
          /* either device initialization failed, or no such device */
  } else {
          /* device is ready for use */
  }
  ```

  This approach has multiple problems.

  First, it incurs a runtime string comparison over all devices in the system
  to look up each device, which is inefficient since devices are statically
  allocated and known at build time. Second, missing devices due to
  misconfigured device drivers could not easily be distinguished from device
  initialization failures, since both produced `NULL` return values from
  `device_get_binding()`. This led to frequent confusion. Third, the
  distinction between the label property and devicetree *node labels* – which
  are different despite the similar terms – was a frequent source of user
  confusion, especially since either one can be used to retrieve device
  structures.

  Instead of using label properties, you should now generally be using node
  labels to retrieve devices instead. Node labels look like the `lbl` token
  in the following devicetree:

  ```dts
  lbl: foo {
          /* ... */
  };
  ```

  and you can retrieve the device structure pointer like this:

  ```c
  /* If the next line causes a build error, then there
   * is no such device. Either fix your devicetree or make sure your
   * device driver is allocating a device. */
  const struct device *my_dev = DEVICE_DT_GET(DT_NODELABEL(lbl));

  if (!device_is_ready(my_dev)) {
          /* device exists, but it failed to initialize */
  } else {
          /* device is ready for use */
  }
  ```

  As shown in the above snippet, [`DEVICE_DT_GET`](../kernel/drivers/index.md#c.DEVICE_DT_GET "DEVICE_DT_GET") should generally be
  used instead of `device_get_binding()` when getting device structures from
  devicetree nodes. Note that you can pass `DEVICE_DT_GET` any devicetree
  [node identifier](../build/dts/api-usage.md#dt-node-identifiers) – you don’t have to use
  [`DT_NODELABEL`](../build/dts/api/api.md#c.DT_NODELABEL "DT_NODELABEL"), though it is usually convenient to do so.
- Support for devicetree “fixups” was removed. For more details, see [commit
  b2520b09a7](https://github.com/zephyrproject-rtos/zephyr/commit/b2520b09a78b86b982a659805e0c65b34e3112a5)
- [Devicetree API](../build/dts/api/api.md#devicetree-api)

  - All devicetree macros now recursively expand their arguments. This means
    that in the following example, `INDEX` is always replaced with the number
    `3` for any hypothetical devicetree macro `DT_FOO()`:

    ```c
    #define INDEX 3
    int foo = DT_FOO(..., INDEX)
    ```

    Previously, devicetree macro arguments were expanded or not on a
    case-by-case basis. The current behavior ensures you can always rely on
    macro expansion when using devicetree APIs.
  - New API macros:

    > - [`DT_FIXED_PARTITION_EXISTS`](../build/dts/api/api.md#c.DT_FIXED_PARTITION_EXISTS "DT_FIXED_PARTITION_EXISTS")
    > - [`DT_FOREACH_CHILD_SEP_VARGS`](../build/dts/api/api.md#c.DT_FOREACH_CHILD_SEP_VARGS "DT_FOREACH_CHILD_SEP_VARGS")
    > - [`DT_FOREACH_CHILD_SEP`](../build/dts/api/api.md#c.DT_FOREACH_CHILD_SEP "DT_FOREACH_CHILD_SEP")
    > - [`DT_FOREACH_CHILD_STATUS_OKAY_SEP_VARGS`](../build/dts/api/api.md#c.DT_FOREACH_CHILD_STATUS_OKAY_SEP_VARGS "DT_FOREACH_CHILD_STATUS_OKAY_SEP_VARGS")
    > - [`DT_FOREACH_CHILD_STATUS_OKAY_SEP`](../build/dts/api/api.md#c.DT_FOREACH_CHILD_STATUS_OKAY_SEP "DT_FOREACH_CHILD_STATUS_OKAY_SEP")
    > - [`DT_FOREACH_NODE`](../build/dts/api/api.md#c.DT_FOREACH_NODE "DT_FOREACH_NODE")
    > - [`DT_FOREACH_STATUS_OKAY_NODE`](../build/dts/api/api.md#c.DT_FOREACH_STATUS_OKAY_NODE "DT_FOREACH_STATUS_OKAY_NODE")
    > - [`DT_INST_CHILD`](../build/dts/api/api.md#c.DT_INST_CHILD "DT_INST_CHILD")
    > - [`DT_INST_FOREACH_CHILD_SEP_VARGS`](../build/dts/api/api.md#c.DT_INST_FOREACH_CHILD_SEP_VARGS "DT_INST_FOREACH_CHILD_SEP_VARGS")
    > - [`DT_INST_FOREACH_CHILD_SEP`](../build/dts/api/api.md#c.DT_INST_FOREACH_CHILD_SEP "DT_INST_FOREACH_CHILD_SEP")
    > - [`DT_INST_FOREACH_CHILD_STATUS_OKAY_SEP_VARGS`](../build/dts/api/api.md#c.DT_INST_FOREACH_CHILD_STATUS_OKAY_SEP_VARGS "DT_INST_FOREACH_CHILD_STATUS_OKAY_SEP_VARGS")
    > - [`DT_INST_FOREACH_CHILD_STATUS_OKAY_SEP`](../build/dts/api/api.md#c.DT_INST_FOREACH_CHILD_STATUS_OKAY_SEP "DT_INST_FOREACH_CHILD_STATUS_OKAY_SEP")
    > - [`DT_INST_FOREACH_CHILD_STATUS_OKAY_VARGS`](../build/dts/api/api.md#c.DT_INST_FOREACH_CHILD_STATUS_OKAY_VARGS "DT_INST_FOREACH_CHILD_STATUS_OKAY_VARGS")
    > - [`DT_INST_FOREACH_CHILD_STATUS_OKAY`](../build/dts/api/api.md#c.DT_INST_FOREACH_CHILD_STATUS_OKAY "DT_INST_FOREACH_CHILD_STATUS_OKAY")
    > - [`DT_INST_STRING_TOKEN_BY_IDX`](../build/dts/api/api.md#c.DT_INST_STRING_TOKEN_BY_IDX "DT_INST_STRING_TOKEN_BY_IDX")
    > - [`DT_INST_STRING_TOKEN`](../build/dts/api/api.md#c.DT_INST_STRING_TOKEN "DT_INST_STRING_TOKEN")
    > - [`DT_INST_STRING_UPPER_TOKEN_BY_IDX`](../build/dts/api/api.md#c.DT_INST_STRING_UPPER_TOKEN_BY_IDX "DT_INST_STRING_UPPER_TOKEN_BY_IDX")
    > - [`DT_INST_STRING_UPPER_TOKEN_OR`](../build/dts/api/api.md#c.DT_INST_STRING_UPPER_TOKEN_OR "DT_INST_STRING_UPPER_TOKEN_OR")
    > - [`DT_INST_STRING_UPPER_TOKEN`](../build/dts/api/api.md#c.DT_INST_STRING_UPPER_TOKEN "DT_INST_STRING_UPPER_TOKEN")
    > - `DT_NODE_VENDOR_BY_IDX_OR`
    > - `DT_NODE_VENDOR_BY_IDX`
    > - `DT_NODE_VENDOR_HAS_IDX`
    > - `DT_NODE_VENDOR_OR`
    > - [`DT_STRING_TOKEN_BY_IDX`](../build/dts/api/api.md#c.DT_STRING_TOKEN_BY_IDX "DT_STRING_TOKEN_BY_IDX")
    > - [`DT_STRING_UPPER_TOKEN_BY_IDX`](../build/dts/api/api.md#c.DT_STRING_UPPER_TOKEN_BY_IDX "DT_STRING_UPPER_TOKEN_BY_IDX")
    > - [`DT_STRING_UPPER_TOKEN_OR`](../build/dts/api/api.md#c.DT_STRING_UPPER_TOKEN_OR "DT_STRING_UPPER_TOKEN_OR")
  - Deprecated macros:

    > - `DT_LABEL(node_id)`: use `DT_PROP(node_id, label)` instead. This is
    >   part of the general deprecation of the label property described at the
    >   top of this section.
    > - `DT_INST_LABEL(inst)`: use `DT_INST_PROP(inst, label)` instead.
    > - `DT_BUS_LABEL(node_id)`: use `DT_PROP(DT_BUS(node_id), label))` instead.
    > - `DT_INST_BUS_LABEL(node_id)`: use `` `DT_PROP(DT_INST_BUS(inst),
    >   label) `` instead. Similar advice applies for the rest of the following
    >   deprecated macros: if you need to access a devicetree node’s label
    >   property, do so explicitly using another property access API macro.
    > - `DT_GPIO_LABEL_BY_IDX()`
    > - `DT_GPIO_LABEL()`
    > - `DT_INST_GPIO_LABEL_BY_IDX()`
    > - `DT_INST_GPIO_LABEL()`
    > - `DT_SPI_DEV_CS_GPIOS_LABEL()`
    > - `DT_INST_SPI_DEV_CS_GPIOS_LABEL()`
    > - `DT_CHOSEN_ZEPHYR_FLASH_CONTROLLER_LABEL`
- Bindings

  - The [bus](../build/dts/bindings-syntax.md#dt-bindings-bus) key in a bindings file can now be a list
    of strings as well as a string. This allows a single node to declare that
    it represents hardware which can communicate over multiple bus protocols.
    The primary use case is simultaneous support for I3C and I2C buses in the
    same nodes, with the base bus definition provided in
    [dts/bindings/i3c/i3c-controller.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/i3c/i3c-controller.yaml).
  - New:

    - [`adi,adxl345`](../build/dts/api/compatibles/adi%2Cadxl345.md#std-dtcompatible-adi-adxl345)
    - [`altr,nios2-qspi-nor`](../build/dts/api/bindings/flash_controller/altr%2Cnios2-qspi-nor.md#std-dtcompatible-altr-nios2-qspi-nor)
    - [`altr,nios2-qspi`](../build/dts/api/bindings/qspi/altr%2Cnios2-qspi.md#std-dtcompatible-altr-nios2-qspi)
    - [`andestech,atciic100`](../build/dts/api/bindings/i2c/andestech%2Catciic100.md#std-dtcompatible-andestech-atciic100)
    - [`andestech,atcpit100`](../build/dts/api/bindings/timer/andestech%2Catcpit100.md#std-dtcompatible-andestech-atcpit100)
    - [`andestech,machine-timer`](../build/dts/api/bindings/timer/andestech%2Cmachine-timer.md#std-dtcompatible-andestech-machine-timer)
    - [`andestech,atcspi200`](../build/dts/api/bindings/spi/andestech.atcspi200.md#std-dtcompatible-andestech-atcspi200)
    - [`arduino-mkr-header`](../build/dts/api/bindings/gpio/arduino-mkr-header.md#std-dtcompatible-arduino-mkr-header)
    - [`arm,armv6m-systick`](../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick)
    - [`arm,armv7m-itm`](../build/dts/api/bindings/debug/arm%2Carmv7m-itm.md#std-dtcompatible-arm-armv7m-itm)
    - [`arm,armv7m-systick`](../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick)
    - [`arm,armv8.1m-systick`](../build/dts/api/bindings/timer/arm%2Carmv8.1m-systick.md#std-dtcompatible-arm-armv8.1m-systick)
    - [`arm,armv8m-itm`](../build/dts/api/bindings/debug/arm%2Carmv8m-itm.md#std-dtcompatible-arm-armv8m-itm)
    - [`arm,armv8m-systick`](../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick)
    - [`arm,beetle-syscon`](../build/dts/api/bindings/arm/arm%2Cbeetle-syscon.md#std-dtcompatible-arm-beetle-syscon)
    - [`arm,pl022`](../build/dts/api/bindings/spi/arm%2Cpl022.md#std-dtcompatible-arm-pl022)
    - [`aspeed,ast10x0-clock`](../build/dts/api/bindings/clock/aspeed%2Cast10x0-clock.md#std-dtcompatible-aspeed-ast10x0-clock)
    - [`atmel,at24mac402`](../build/dts/api/bindings/mtd/atmel%2C24mac402.md#std-dtcompatible-atmel-at24mac402)
    - [`atmel,ataes132a`](../build/dts/api/bindings/crypto/atmel%2Cataes132a.md#std-dtcompatible-atmel-ataes132a)
    - [`atmel,sam-smc`](../build/dts/api/bindings/memory-controllers/atmel%2Csam-smc.md#std-dtcompatible-atmel-sam-smc)
    - [`atmel,sam4l-flashcalw-controller`](../build/dts/api/bindings/flash_controller/atmel%2Csam4l-flashcalw-controller.md#std-dtcompatible-atmel-sam4l-flashcalw-controller)
    - [`atmel,saml2x-gclk`](../build/dts/api/bindings/clock/atmel%2Csaml2x-gclk.md#std-dtcompatible-atmel-saml2x-gclk)
    - [`atmel,saml2x-mclk`](../build/dts/api/bindings/clock/atmel%2Csaml2x-mclk.md#std-dtcompatible-atmel-saml2x-mclk)
    - [`cdns,qspi-nor`](../build/dts/api/bindings/flash_controller/cdns%2Cqspi-nor.md#std-dtcompatible-cdns-qspi-nor)
    - [`espressif,esp32-ipm`](../build/dts/api/bindings/ipm/espressif%2Cesp32-ipm.md#std-dtcompatible-espressif-esp32-ipm)
    - [`espressif,esp32-mcpwm`](../build/dts/api/bindings/pwm/espressif%2Cesp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm)
    - [`espressif,esp32-pcnt`](../build/dts/api/bindings/sensor/espressif%2Cesp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt)
    - [`espressif,esp32-rtc-timer`](../build/dts/api/bindings/counter/espressif%2Cesp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer)
    - [`espressif,esp32-timer`](../build/dts/api/bindings/counter/espressif%2Cesp32-timer.md#std-dtcompatible-espressif-esp32-timer)
    - [`espressif,esp32-twai`](../build/dts/api/bindings/can/espressif%2Cesp32-twai.md#std-dtcompatible-espressif-esp32-twai)
    - [`espressif,esp32-usb-serial`](../build/dts/api/bindings/serial/espressif%2Cesp32-usb-serial.md#std-dtcompatible-espressif-esp32-usb-serial)
    - [`espressif,esp32-wifi`](../build/dts/api/bindings/wifi/espressif%2Cesp32-wifi.md#std-dtcompatible-espressif-esp32-wifi)
    - [`gd,gd32-adc`](../build/dts/api/bindings/adc/gd%2Cgd32-adc.md#std-dtcompatible-gd-gd32-adc)
    - [`gd,gd32-cctl`](../build/dts/api/bindings/clock/gd%2Cgd32-cctl.md#std-dtcompatible-gd-gd32-cctl)
    - [`gd,gd32-dma`](../build/dts/api/bindings/dma/gd%2Cgd32-dma.md#std-dtcompatible-gd-gd32-dma)
    - [`gd,gd32-flash-controller`](../build/dts/api/bindings/flash_controller/gd%2Cgd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller)
    - [`gd,gd32-rcu`](../build/dts/api/bindings/mfd/gd%2Cgd32-rcu.md#std-dtcompatible-gd-gd32-rcu)
    - [`goodix,gt911`](../build/dts/api/bindings/input/goodix%2Cgt911.md#std-dtcompatible-goodix-gt911)
    - [`infineon,xmc4xxx-gpio`](../build/dts/api/bindings/gpio/infineon%2Cxmc4xxx-gpio.md#std-dtcompatible-infineon-xmc4xxx-gpio)
    - [`infineon,xmc4xxx-pinctrl`](../build/dts/api/bindings/pinctrl/infineon%2Cxmc4xxx-pinctrl.md#std-dtcompatible-infineon-xmc4xxx-pinctrl)
    - [`intel,ace-art-counter`](../build/dts/api/bindings/counter/intel%2Cace-art-counter.md#std-dtcompatible-intel-ace-art-counter)
    - [`intel,ace-intc`](../build/dts/api/bindings/interrupt-controller/intel%2Cace-intc.md#std-dtcompatible-intel-ace-intc)
    - [`intel,ace-rtc-counter`](../build/dts/api/bindings/counter/intel%2Cace-rtc-counter.md#std-dtcompatible-intel-ace-rtc-counter)
    - [`intel,ace-timestamp`](../build/dts/api/bindings/timestamp/intel%2Cace-timestamp.md#std-dtcompatible-intel-ace-timestamp)
    - [`intel,adsp-gpdma`](../build/dts/api/bindings/dma/intel%2Cadsp-gpdma.md#std-dtcompatible-intel-adsp-gpdma) (formerly `intel,cavs-gpdma`)
    - [`intel,adsp-hda-host-in`](../build/dts/api/bindings/dma/intel%2Cadsp-hda-host-in.md#std-dtcompatible-intel-adsp-hda-host-in) (formerly `intel,cavs-hda-host-in`)
    - [`intel,adsp-hda-host-out`](../build/dts/api/bindings/dma/intel%2Cadsp-hda-host-out.md#std-dtcompatible-intel-adsp-hda-host-out) (formerly `intel,cavs-hda-host-out`)
    - [`intel,adsp-hda-link-in`](../build/dts/api/bindings/dma/intel%2Cadsp-hda-link-in.md#std-dtcompatible-intel-adsp-hda-link-in) (formerly `intel,cavs-hda-link-in`)
    - [`intel,adsp-hda-link-out`](../build/dts/api/bindings/dma/intel%2Cadsp-hda-link-out.md#std-dtcompatible-intel-adsp-hda-link-out) (formerly `intel,cavs-hda-link-out`)
    - [`intel,adsp-host-ipc`](../build/dts/api/bindings/ipc/intel%2Cadsp-host-ipc.md#std-dtcompatible-intel-adsp-host-ipc)
    - [`intel,adsp-idc`](../build/dts/api/bindings/ipc/intel%2Cadsp-idc.md#std-dtcompatible-intel-adsp-idc) (formerly `intel,cavs-idc`)
    - [`intel,adsp-imr`](../build/dts/api/bindings/mm/intel%2Cadsp-imr.md#std-dtcompatible-intel-adsp-imr)
    - `intel,adsp-lps`
    - [`intel,adsp-mtl-tlb`](../build/dts/api/bindings/mm/intel%2Cadsp-mtl-tlb.md#std-dtcompatible-intel-adsp-mtl-tlb)
    - [`intel,adsp-power-domain`](../build/dts/api/bindings/power-domain/intel%2Cadsp-power-domain.md#std-dtcompatible-intel-adsp-power-domain)
    - [`intel,adsp-shim-clkctl`](../build/dts/api/bindings/clock/intel%2Cadsp-shim-clkctl.md#std-dtcompatible-intel-adsp-shim-clkctl)
    - [`intel,agilex-clock`](../build/dts/api/bindings/clock/intel%2Cagilex-clock.md#std-dtcompatible-intel-agilex-clock)
    - [`intel,alh-dai`](../build/dts/api/bindings/alh/intel%2Calh-dai.md#std-dtcompatible-intel-alh-dai)
    - [`intel,multiboot-framebuffer`](../build/dts/api/bindings/display/intel%2Cmultiboot-framebuffer.md#std-dtcompatible-intel-multiboot-framebuffer)
    - [`ite,it8xxx2-peci`](../build/dts/api/bindings/peci/ite%2Cit8xxx2-peci.md#std-dtcompatible-ite-it8xxx2-peci) (formerly `ite,peci-it8xxx2`)
    - [`maxim,ds18b20`](../build/dts/api/bindings/sensor/maxim%2Cds18b20.md#std-dtcompatible-maxim-ds18b20)
    - [`maxim,ds2484`](../build/dts/api/bindings/w1/maxim%2Cds2484.md#std-dtcompatible-maxim-ds2484)
    - [`maxim,ds2485`](../build/dts/api/bindings/w1/maxim%2Cds2485.md#std-dtcompatible-maxim-ds2485)
    - [`maxim,max7219`](../build/dts/api/bindings/display/maxim%2Cmax7219.md#std-dtcompatible-maxim-max7219)
    - [`microchip,mpfs-gpio`](../build/dts/api/bindings/gpio/microchip%2Cmpfs-gpio.md#std-dtcompatible-microchip-mpfs-gpio)
    - [`microchip,xec-eeprom`](../build/dts/api/bindings/mtd/microchip%2Cxec-eeprom.md#std-dtcompatible-microchip-xec-eeprom)
    - [`microchip,xec-espi`](../build/dts/api/bindings/espi/microchip%2Cxec-espi.md#std-dtcompatible-microchip-xec-espi)
    - [`microchip,xec-i2c`](../build/dts/api/bindings/i2c/microchip%2Cxec-i2c.md#std-dtcompatible-microchip-xec-i2c)
    - [`microchip,xec-qmspi`](../build/dts/api/bindings/spi/microchip%2Cxec-qmspi.md#std-dtcompatible-microchip-xec-qmspi)
    - [`neorv32-machine-timer`](../build/dts/api/bindings/timer/neorv32-machine-timer.md#std-dtcompatible-neorv32-machine-timer)
    - [`nordic,nrf-ieee802154`](../build/dts/api/bindings/ieee802154/nordic%2Cnrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154)
    - [`nuclei,systimer`](../build/dts/api/bindings/timer/nuclei%2Csystimer.md#std-dtcompatible-nuclei-systimer)
    - [`nuvoton,npcx-leakage-io`](../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-leakage-io.md#std-dtcompatible-nuvoton-npcx-leakage-io)
    - [`nuvoton,npcx-peci`](../build/dts/api/bindings/peci/nuvoton%2Cnpcx-peci.md#std-dtcompatible-nuvoton-npcx-peci)
    - [`nuvoton,npcx-power-psl`](../build/dts/api/bindings/power/nuvoton%2Cnpcx-power-psl.md#std-dtcompatible-nuvoton-npcx-power-psl)
    - [`nxp,gpt-hw-timer`](../build/dts/api/bindings/timer/nxp%2Cgpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer)
    - [`nxp,iap-fmc11`](../build/dts/api/bindings/flash_controller/nxp%2Ciap-fmc11.md#std-dtcompatible-nxp-iap-fmc11)
    - [`nxp,imx-caam`](../build/dts/api/bindings/rng/nxp%2Cimx-caam.md#std-dtcompatible-nxp-imx-caam)
    - [`nxp,kw41z-ieee802154`](../build/dts/api/bindings/ieee802154/nxp%2Ckw41z-ieee802154.md#std-dtcompatible-nxp-kw41z-ieee802154)
    - [`nxp,lpc-rtc`](../build/dts/api/bindings/rtc/nxp%2Clpc-rtc.md#std-dtcompatible-nxp-lpc-rtc)
    - [`nxp,lpc-sdif`](../build/dts/api/bindings/sdhc/nxp%2Clpc-sdif.md#std-dtcompatible-nxp-lpc-sdif)
    - [`nxp,mcux-i3c`](../build/dts/api/bindings/i3c/nxp%2Cmcux-i3c.md#std-dtcompatible-nxp-mcux-i3c)
    - [`nxp,os-timer`](../build/dts/api/bindings/timer/nxp%2Cos-timer.md#std-dtcompatible-nxp-os-timer)
    - [`panasonic,reduced-arduino-header`](../build/dts/api/bindings/gpio/panasonic%2Creduced-arduino-header.md#std-dtcompatible-panasonic-reduced-arduino-header)
    - [`raspberrypi,pico-adc`](../build/dts/api/bindings/adc/raspberrypi%2Cpico-adc.md#std-dtcompatible-raspberrypi-pico-adc)
    - [`raspberrypi,pico-pwm`](../build/dts/api/bindings/pwm/raspberrypi%2Cpico-pwm.md#std-dtcompatible-raspberrypi-pico-pwm)
    - [`raspberrypi,pico-spi`](../build/dts/api/bindings/spi/raspberrypi%2Cpico-spi.md#std-dtcompatible-raspberrypi-pico-spi)
    - [`raspberrypi,pico-watchdog`](../build/dts/api/bindings/watchdog/raspberrypi%2Cpico-watchdog.md#std-dtcompatible-raspberrypi-pico-watchdog)
    - [`renesas,pwm-rcar`](../build/dts/api/bindings/pwm/renesas%2Cpwm-rcar.md#std-dtcompatible-renesas-pwm-rcar)
    - [`renesas,r8a7795-cpg-mssr`](../build/dts/api/bindings/clock/renesas%2Cr8a7795-cpg-mssr.md#std-dtcompatible-renesas-r8a7795-cpg-mssr) (formerly `renesas,rcar-cpg-mssr`)
    - [`renesas,smartbond-flash-controller`](../build/dts/api/bindings/flash_controller/renesas%2Csmartbond-flash-controller.md#std-dtcompatible-renesas-smartbond-flash-controller)
    - [`renesas,smartbond-gpio`](../build/dts/api/bindings/gpio/renesas%2Csmartbond-gpio.md#std-dtcompatible-renesas-smartbond-gpio)
    - [`renesas,smartbond-pinctrl`](../build/dts/api/bindings/pinctrl/renesas%2Csmartbond-pinctrl.md#std-dtcompatible-renesas-smartbond-pinctrl)
    - [`renesas,smartbond-uart`](../build/dts/api/bindings/serial/renesas%2Csmartbond-uart.md#std-dtcompatible-renesas-smartbond-uart)
    - [`sifive,clint0`](../build/dts/api/bindings/timer/sifive%2Cclint0.md#std-dtcompatible-sifive-clint0)
    - [`sifive,e24`](../build/dts/api/bindings/cpu/sifive%2Ce24.md#std-dtcompatible-sifive-e24) (formerly `riscv,sifive-e24`)
    - [`sifive,e31`](../build/dts/api/bindings/cpu/sifive%2Ce31.md#std-dtcompatible-sifive-e31) (formerly `riscv,sifive-e31`)
    - [`sifive,e51`](../build/dts/api/bindings/cpu/sifive%2Ce51.md#std-dtcompatible-sifive-e51) (formerly `riscv,sifive-e51`)
    - [`sifive,s7`](../build/dts/api/bindings/cpu/sifive%2Cs7.md#std-dtcompatible-sifive-s7) (formerly `riscv,sifive-s7`)
    - [`silabs,gecko-semailbox`](../build/dts/api/bindings/crypto/silabs%2Cgecko-semailbox.md#std-dtcompatible-silabs-gecko-semailbox)
    - [`snps,arc-iot-sysconf`](../build/dts/api/bindings/misc/snps%2Carc-iot-sysconf.md#std-dtcompatible-snps-arc-iot-sysconf)
    - [`snps,arc-timer`](../build/dts/api/bindings/timer/snps%2Carc-timer.md#std-dtcompatible-snps-arc-timer)
    - [`snps,archs-ici`](../build/dts/api/bindings/misc/snps%2Carchs-ici.md#std-dtcompatible-snps-archs-ici)
    - [`st,stm32-vbat`](../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat)
    - [`st,stm32g0-hsi-clock`](../build/dts/api/bindings/clock/st%2Cstm32g0-hsi-clock.md#std-dtcompatible-st-stm32g0-hsi-clock)
    - [`st,stm32h7-spi`](../build/dts/api/bindings/spi/st%2Cstm32h7-spi.md#std-dtcompatible-st-stm32h7-spi)
    - [`st,stm32u5-dma`](../build/dts/api/bindings/dma/st%2Cstm32u5-dma.md#std-dtcompatible-st-stm32u5-dma)
    - [`starfive,jh7100-clint`](../build/dts/api/bindings/timer/starfive%2Cjh7100-clint.md#std-dtcompatible-starfive-jh7100-clint)
    - [`telink,b91-adc`](../build/dts/api/bindings/adc/telink%2Cb91-adc.md#std-dtcompatible-telink-b91-adc)
    - [`telink,machine-timer`](../build/dts/api/bindings/timer/telink%2Cmachine-timer.md#std-dtcompatible-telink-machine-timer)
    - [`ti,ads1119`](../build/dts/api/bindings/adc/ti%2Cads1119.md#std-dtcompatible-ti-ads1119)
    - [`ti,cc13xx-cc26xx-flash-controller`](../build/dts/api/bindings/flash_controller/ti%2Ccc13xx-cc26xx-flash-controller.md#std-dtcompatible-ti-cc13xx-cc26xx-flash-controller)
    - [`ti,cc13xx-cc26xx-ieee802154-subghz`](../build/dts/api/bindings/ieee802154/ti%2Ccc13xx-cc26xx-ieee802154-subghz.md#std-dtcompatible-ti-cc13xx-cc26xx-ieee802154-subghz)
    - [`ti,cc13xx-cc26xx-ieee802154`](../build/dts/api/bindings/ieee802154/ti%2Ccc13xx-cc26xx-ieee802154.md#std-dtcompatible-ti-cc13xx-cc26xx-ieee802154)
    - [`ti,sn74hc595`](../build/dts/api/bindings/gpio/ti%2Csn74hc595.md#std-dtcompatible-ti-sn74hc595)
    - [`ultrachip,uc8176`](../build/dts/api/bindings/display/ultrachip%2Cuc8176.md#std-dtcompatible-ultrachip-uc8176)
    - [`ultrachip,uc8179`](../build/dts/api/bindings/display/ultrachip%2Cuc8179.md#std-dtcompatible-ultrachip-uc8179)
    - [`xen,hvc-uart`](../build/dts/api/bindings/serial/xen%2Chvc-uart.md#std-dtcompatible-xen-hvc-uart)
    - `xen,xen-4.15`
    - [`xlnx,pinctrl-zynq`](../build/dts/api/bindings/pinctrl/xlnx%2Cpinctrl-zynq.md#std-dtcompatible-xlnx-pinctrl-zynq)
    - [`zephyr,coredump`](../build/dts/api/bindings/coredump/zephyr%2Ccoredump.md#std-dtcompatible-zephyr-coredump)
    - [`zephyr,ieee802154-uart-pipe`](../build/dts/api/bindings/ieee802154/zephyr%2Cieee802154-uart-pipe.md#std-dtcompatible-zephyr-ieee802154-uart-pipe)
    - [`zephyr,native-posix-counter`](../build/dts/api/bindings/counter/zephyr%2Cnative-posix-counter.md#std-dtcompatible-zephyr-native-posix-counter)
    - `zephyr,native-posix-linux-can`
    - `zephyr,sdl-kscan`
    - [`zephyr,sdmmc-disk`](../build/dts/api/bindings/sd/zephyr%2Csdmmc-disk.md#std-dtcompatible-zephyr-sdmmc-disk)
    - [`zephyr,w1-serial`](../build/dts/api/bindings/w1/zephyr%2Cw1-serial.md#std-dtcompatible-zephyr-w1-serial)
  - [Pin Control](../hardware/pinctrl/index.md#pinctrl-guide) support added via new `pinctrl-0`, etc. properties:

    - [`microchip,xec-qmspi`](../build/dts/api/bindings/spi/microchip%2Cxec-qmspi.md#std-dtcompatible-microchip-xec-qmspi)
    - [`infineon,xmc4xxx-uart`](../build/dts/api/bindings/serial/infineon%2Cxmc4xxx-uart.md#std-dtcompatible-infineon-xmc4xxx-uart)
    - [`nxp,lpc-mcan`](../build/dts/api/bindings/can/nxp%2Clpc-mcan.md#std-dtcompatible-nxp-lpc-mcan)
    - [`xlnx,xuartps`](../build/dts/api/bindings/serial/xlnx%2Cxuartps.md#std-dtcompatible-xlnx-xuartps)
  - Other changes:

    - Analog Devices parts:

      - [`adi,adxl372`](../build/dts/api/compatibles/adi%2Cadxl372.md#std-dtcompatible-adi-adxl372): new properties as part of a general conversion
        of the associated upstream driver to support multiple instances.
      - [`adi,adxl362`](../build/dts/api/bindings/sensor/adi%2Cadxl362.md#std-dtcompatible-adi-adxl362): new `wakeup-mode`, `autosleep` properties.
    - Atmel SoCs:

      - [`atmel,rf2xx`](../build/dts/api/bindings/ieee802154/atmel%2Crf2xx.md#std-dtcompatible-atmel-rf2xx): new `channel-page`, `tx-pwr-table`,
        `tx-pwr-min`, `tx-pwr-max` properties.
      - GMAC: new `mac-eeprom` property.
    - Espressif SoCs:

      - [`espressif,esp32-i2c`](../build/dts/api/bindings/i2c/espressif%2Cesp32-i2c.md#std-dtcompatible-espressif-esp32-i2c): the `sda-pin` and `scl-pin`
        properties are now `scl-gpios` and `sda-gpios`.
      - [`espressif,esp32-ledc`](../build/dts/api/bindings/pwm/espressif%2Cesp32-ledc.md#std-dtcompatible-espressif-esp32-ledc): device configuration moved to
        devicetree via a new child binding.
      - [`espressif,esp32-pinctrl`](../build/dts/api/bindings/pinctrl/espressif%2Cesp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl): this now uses pin groups.
      - [`espressif,esp32-spi`](../build/dts/api/bindings/spi/espressif%2Cesp32-spi.md#std-dtcompatible-espressif-esp32-spi): new `use-iomux` property.
      - [`espressif,esp32-usb-serial`](../build/dts/api/bindings/serial/espressif%2Cesp32-usb-serial.md#std-dtcompatible-espressif-esp32-usb-serial): removed `peripheral`
        property.
    - GigaDevice SoCs:

      - Various peripheral bindings have had their SoC-specific
        `rcu-periph-clock` properties replaced with the standard `clocks`
        property as part of driver changes associated with the new
        [`gd,gd32-cctl`](../build/dts/api/bindings/clock/gd%2Cgd32-cctl.md#std-dtcompatible-gd-gd32-cctl) clock controller binding:

        - [`gd,gd32-afio`](../build/dts/api/bindings/pinctrl/gd%2Cgd32-afio.md#std-dtcompatible-gd-gd32-afio)
        - [`gd,gd32-dac`](../build/dts/api/bindings/dac/gd%2Cgd32-dac.md#std-dtcompatible-gd-gd32-dac)
        - [`gd,gd32-gpio`](../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio)
        - [`gd,gd32-i2c`](../build/dts/api/bindings/i2c/gd%2Cgd32-i2c.md#std-dtcompatible-gd-gd32-i2c)
        - [`gd,gd32-pwm`](../build/dts/api/bindings/pwm/gd%2Cgd32-pwm.md#std-dtcompatible-gd-gd32-pwm)
        - [`gd,gd32-spi`](../build/dts/api/bindings/spi/gd%2Cgd32-spi.md#std-dtcompatible-gd-gd32-spi)
        - [`gd,gd32-syscfg`](../build/dts/api/bindings/misc/gd%2Cgd32-syscfg.md#std-dtcompatible-gd-gd32-syscfg)
        - [`gd,gd32-timer`](../build/dts/api/bindings/timer/gd%2Cgd32-timer.md#std-dtcompatible-gd-gd32-timer)
        - [`gd,gd32-usart`](../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart)
      - Similarly, various GigaDevice peripherals now support the standard
        `resets` property as part of related driver changes to support
        resetting the peripheral state before initialization via the
        [`gd,gd32-rcu`](../build/dts/api/bindings/mfd/gd%2Cgd32-rcu.md#std-dtcompatible-gd-gd32-rcu) binding:

        - [`gd,gd32-dac`](../build/dts/api/bindings/dac/gd%2Cgd32-dac.md#std-dtcompatible-gd-gd32-dac)
        - [`gd,gd32-gpio`](../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio)
        - [`gd,gd32-i2c`](../build/dts/api/bindings/i2c/gd%2Cgd32-i2c.md#std-dtcompatible-gd-gd32-i2c)
        - [`gd,gd32-pwm`](../build/dts/api/bindings/pwm/gd%2Cgd32-pwm.md#std-dtcompatible-gd-gd32-pwm)
        - [`gd,gd32-spi`](../build/dts/api/bindings/spi/gd%2Cgd32-spi.md#std-dtcompatible-gd-gd32-spi)
        - [`gd,gd32-usart`](../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart)
    - Intel SoCs:

      - [`intel,adsp-tlb`](../build/dts/api/bindings/mm/intel%2Cadsp-tlb.md#std-dtcompatible-intel-adsp-tlb):
        new `paddr-size`, `exec-bit-idx`, `write-bit-idx` properties.
      - [`intel,adsp-shim-clkctl`](../build/dts/api/bindings/clock/intel%2Cadsp-shim-clkctl.md#std-dtcompatible-intel-adsp-shim-clkctl): new `wovcro-supported` property.
      - Removed `intel,dmic` binding.
      - Removed `intel,s1000-pinmux` binding.
    - Nordic SoCs:

      - [`nordic,nrf-pinctrl`](../build/dts/api/bindings/pinctrl/nordic%2Cnrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl): `NRF_PSEL_DISCONNECTED` can be used
        to disconnect a pin.
      - [`nordic,nrf-spim`](../build/dts/api/bindings/spi/nordic%2Cnrf-spim.md#std-dtcompatible-nordic-nrf-spim): new `rx-delay-supported`,
        `rx-delay` properties.
      - [`nordic,nrf-spim`](../build/dts/api/bindings/spi/nordic%2Cnrf-spim.md#std-dtcompatible-nordic-nrf-spim), [`nordic,nrf-spi`](../build/dts/api/bindings/spi/nordic%2Cnrf-spi.md#std-dtcompatible-nordic-nrf-spi): new
        :   `overrun-character`, `max-frequency`, `memory-region`,
            `memory-region-names` properties.
      - [`nordic,nrf-uarte`](../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte): new `memory-region`,
        `memory-region-names` properties.
      - Various bindings have had `foo-pin` properties deprecated. For
        example, [`nordic,nrf-qspi`](../build/dts/api/bindings/flash_controller/nordic%2Cnrf-qspi.md#std-dtcompatible-nordic-nrf-qspi) has a deprecated `sck-pin`
        property. Uses of such properties should be replaced with pinctrl
        equivalents; see `nordic,nrfpinctrl`.
    - Nuvoton SoCs:

      - [`nuvoton,npcx-leakage-io`](../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-leakage-io.md#std-dtcompatible-nuvoton-npcx-leakage-io): new `lvol-maps` property.
      - [`nuvoton,npcx-scfg`](../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-scfg.md#std-dtcompatible-nuvoton-npcx-scfg): removed `io_port`, `io_bit`
        cells in `lvol_cells` specifiers.
      - Removed: `nuvoton,npcx-lvolctrl-def`, `nuvoton,npcx-psl-out`,
        `nuvoton,npcx-pslctrl-conf`, `nuvoton,npcx-pslctrl-def`.
      - Added pinctrl support for PSL (Power Switch Logic) pads.
    - NXP SoCs:

      - [`nxp,imx-pwm`](../build/dts/api/bindings/pwm/nxp%2Cimx-pwm.md#std-dtcompatible-nxp-imx-pwm): new `run-in-wait`, `run-in-debug` properties.
      - [`nxp,lpc-spi`](../build/dts/api/bindings/spi/nxp%2Clpc-spi.md#std-dtcompatible-nxp-lpc-spi): new `def-char` property.
      - [`nxp,lpc-iocon-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Clpc-iocon-pinctrl.md#std-dtcompatible-nxp-lpc-iocon-pinctrl): new `nxp,analog-alt-mode` property.
      - removed deprecated `nxp,lpc-iap` binding.
      - [`nxp,imx-csi`](../build/dts/api/bindings/video/nxp%2Cimx-csi.md#std-dtcompatible-nxp-imx-csi): new `sensor` property replacing the
        `sensor-label` property.
      - [`nxp,imx-lpi2c`](../build/dts/api/bindings/i2c/nxp%2Cimx-lpi2c.md#std-dtcompatible-nxp-imx-lpi2c): new `scl-gpios`, `sda-gpios` properties.
    - STM32 SoCs:

      - [`st,stm32-adc`](../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc): new `has-vbat-channel` property.
      - `st,stm32-can`: removed `one-shot` property.
      - [`st,stm32-fdcan`](../build/dts/api/bindings/can/st%2Cstm32-fdcan.md#std-dtcompatible-st-stm32-fdcan): new `clocks`, `clk-divider` properties.
      - [`st,stm32-ospi`](../build/dts/api/bindings/ospi/st%2Cstm32-ospi.md#std-dtcompatible-st-stm32-ospi): new `dmas`, `dma-names` properties.
      - [`st,stm32-ospi-nor`](../build/dts/api/bindings/flash_controller/st%2Cstm32-ospi-nor.md#std-dtcompatible-st-stm32-ospi-nor): new `four-byte-opcodes`,
        `writeoc` properties; new enum values `2` and `4` in
        `spi-bus-width` property.
      - [`st,stm32-pwm`](../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm): removed deprecated `st,prescaler` property.
      - [`st,stm32-rng`](../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng): new `nist-config` property.
      - [`st,stm32-sdmmc`](../build/dts/api/bindings/mmc/st%2Cstm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc): new `dmas`, `dma-names`,
        `bus-width` properties.
      - [`st,stm32-temp-cal`](../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal): new `ts-cal-resolution` property;
        removed `ts-cal-offset` property.
      - [`st,stm32u5-pll-clock`](../build/dts/api/bindings/clock/st%2Cstm32u5-pll-clock.md#std-dtcompatible-st-stm32u5-pll-clock): new `div-p` property.
      - temperature sensor bindings no longer have a `ts-voltage-mv` property.
      - UART bindings: new `wakeup-line` properties.
    - Texas Instruments parts:

      - [`ti,ina237`](../build/dts/api/bindings/sensor/ti%2Cina237.md#std-dtcompatible-ti-ina237): new `alert-config`, `irq-gpios` properties.
      - [`ti,bq274xx`](../build/dts/api/bindings/sensor/ti%2Cbq274xx.md#std-dtcompatible-ti-bq274xx): new `zephyr,lazy-load` property.
    - Ultrachip UC81xx displays:

      - The `gooddisplay,gd7965` binding was removed in favor of new
        UltraChip device-specific bindings (see list of new `ultrachip,...`
        bindings above). Various required properties in the removed binding are
        now optional in the new bindings.
      - New `pll`, `vdcs`, `lutc`, `lutww`, `lutkw`, `lutwk`,
        `lutkk`, `lutbd`, `softstart` properties. Full and partial
        refresh profile support. The `pwr` property is now part of the child
        binding.
    - Zephyr-specific bindings:

      - [`zephyr,bt-hci-spi`](../build/dts/api/bindings/bluetooth/zephyr%2Cbt-hci-spi.md#std-dtcompatible-zephyr-bt-hci-spi): new `reset-assert-duration-ms` property.
      - removed `zephyr,ipm-console` binding.
      - [`zephyr,ipc-openamp-static-vrings`](../build/dts/api/bindings/ipc/zephyr%2Cipc-openamp-static-vrings.md#std-dtcompatible-zephyr-ipc-openamp-static-vrings): new
        `zephyr,buffer-size` property.
      - [`zephyr,memory-region`](../build/dts/api/bindings/base/zephyr%2Cmemory-region.md#std-dtcompatible-zephyr-memory-region): new `PPB` and `IO` region support.
    - [`infineon,xmc4xxx-uart`](../build/dts/api/bindings/serial/infineon%2Cxmc4xxx-uart.md#std-dtcompatible-infineon-xmc4xxx-uart): new `input-src` property.
    - WSEN-HIDS sensors: new `drdy-gpios`, `odr` properties.
    - [`sitronix,st7789v`](../build/dts/api/bindings/display/sitronix%2Cst7789v.md#std-dtcompatible-sitronix-st7789v): `cmd-data-gpios` is now optional.
    - `solomon,ssd16xxfb`: new `dummy-line`,
      `gate-line-width` properties. The `gdv`, `sdv`, `vcom`, and
      `border-waveform` properties are now optional.
    - `riscv,clint0` removed; all in-tree users were converted to
      `sifive,clint0` or derived bindings.
    - [`worldsemi,ws2812-spi`](../build/dts/api/bindings/led_strip/worldsemi%2Cws2812-spi.md#std-dtcompatible-worldsemi-ws2812-spi): SPI bindings have new `spi-cpol`,
      `spi-cpha` properties.
    - [`ns16550`](../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550): `reg-shift` is now required.
    - Removed `reserved-memory` binding.
- Implementation details

  - The generated devicetree header file placed in the build directory was
    renamed from `devicetree_unfixed.h` to `devicetree_generated.h`.
  - The generated `device_extern.h` has been replaced using
    `DT_FOREACH_STATUS_OKAY_NODE`. See [commit
    0224f2c508df154ffc9c1ecffaf0b06608d6b623](https://github.com/zephyrproject-rtos/zephyr/commit/0224f2c508df154ffc9c1ecffaf0b06608d6b623)

## Libraries / Subsystems

- C Library

  - Added Picolibc as a Zephyr module. Picolibc module is a footprint-optimized
    full C standard library implementation that is configurable at the build
    time.
  - C library heap initialization call has been moved from the `APPLICATION`
    phase to the `POST_KERNEL` phase to allow calling the libc dynamic memory
    management functions (e.g. `malloc()`) during the application
    initialization phase.
  - Added `strerror()` and `strerror_r()` functions to the minimal libc.
  - Removed architecture-specific `off_t` type definition in the minimal
    libc. `off_t` is now defined as `intptr_t` regardless of the selected
    architecture.
- C++ Subsystem

  - Added `std::ptrdiff_t`, `std::size_t`, `std::max_align_t` and
    `std::nullptr_t` type definitions to the C++ subsystem `cstddef`
    header.
  - Renamed global constructor list symbols to prevent the native POSIX host
    runtime from executing the constructors before Zephyr loads.
- Cbprintf

  - Updated cbprintf static packaging to interpret `unsigned char *` as a pointer
    to a string. See [Limitations and recommendations](../services/formatted_output.md#cbprintf-packaging-limitations) for more details about
    how to efficienty use strings. Change mainly applies to the `logging` subsystem
    since it uses this feature.
- Emul

  - Added [`EMUL_DT_DEFINE`](../hardware/emulator/bus_emulators.md#c.EMUL_DT_DEFINE "EMUL_DT_DEFINE") and [`EMUL_DT_INST_DEFINE`](../hardware/emulator/bus_emulators.md#c.EMUL_DT_INST_DEFINE "EMUL_DT_INST_DEFINE") to mirror
    [`DEVICE_DT_DEFINE`](../kernel/drivers/index.md#c.DEVICE_DT_DEFINE "DEVICE_DT_DEFINE") and [`DEVICE_DT_INST_DEFINE`](../kernel/drivers/index.md#c.DEVICE_DT_INST_DEFINE "DEVICE_DT_INST_DEFINE") respectively.
  - Added [`EMUL_DT_GET`](../hardware/emulator/bus_emulators.md#c.EMUL_DT_GET "EMUL_DT_GET") to mirror [`DEVICE_DT_GET`](../kernel/drivers/index.md#c.DEVICE_DT_GET "DEVICE_DT_GET").
  - Removed the need to manually register emulators in their init function (automatically done).
- Filesystem

  - Added cash used to reduce the NVS data lookup time, see
    [`CONFIG_NVS_LOOKUP_CACHE`](../kconfig.md#CONFIG_NVS_LOOKUP_CACHE "CONFIG_NVS_LOOKUP_CACHE") option.
  - Changing mkfs options to create FAT32 on larger storage when FAT16 fails.
  - Added [`CONFIG_FS_FATFS_MIN_SS`](../kconfig.md#CONFIG_FS_FATFS_MIN_SS "CONFIG_FS_FATFS_MIN_SS") that allows to set
    minimal expected sector size to be supported.
- Management

  - MCUMGR race condition when using the task status function whereby if a
    thread state changed it could give a falsely short process list has been
    fixed.
  - MCUMGR shell (group 9) CBOR structure has changed, the `rc`
    response is now only used for mcumgr errors, shell command
    execution result codes are instead returned in the `ret`
    variable instead, see [Shell management](../services/device_mgmt/smp_groups/smp_group_9.md#mcumgr-smp-group-9) for updated
    information. Legacy behaviour can be restored by enabling
    `CONFIG_MCUMGR_CMD_SHELL_MGMT_LEGACY_RC_RETURN_CODE`.
  - MCUMGR img\_mgmt erase command now accepts an optional slot number
    to select which image will be erased, using the `slot` input
    (will default to slot 1 if not provided).
  - MCUMGR `CONFIG_OS_MGMT_TASKSTAT_SIGNED_PRIORITY` is now
    enabled by default, this makes thread priorities in the taskstat command
    signed, which matches the signed priority of tasks in Zephyr, to revert
    to previous behaviour of using unsigned values, disable this Kconfig.
  - MCUMGR taskstat runtime field support has been added, if
    `CONFIG_OS_MGMT_TASKSTAT` is enabled, which will report the
    number of CPU cycles have been spent executing the thread.
  - MCUMGR transport API drops `zst` parameter, of `zephyr_smp_transport`
    type, from `zephyr_smp_transport_out_fn()` type callback as it has
    not been used, and the `nb` parameter, of [`net_buf`](../connectivity/networking/api/net_buf.md#c.net_buf "net_buf") type,
    can carry additional transport information when needed.
  - A dummy SMP transport has been added which allows for testing MCUMGR
    functionality and commands/responses.
  - An issue with the UART/shell transports whereby large packets would wrongly
    be split up with multiple start-of-frame headers instead of only one has been
    fixed.
  - SMP now runs in its own dedicated work queue which prevents issues running in
    the system workqueue with some transports, e.g. Bluetooth, which previously
    caused a deadlock if buffers could not be allocated.
  - Bluetooth transport will now reduce the size of packets that are sent if they
    are too large for the remote device instead of failing to send them, if the
    remote device cannot accept a notification of 20 bytes then the attempt is
    aborted.
  - Unaligned memory access problems for CPUs that do not support it in MCUMGR
    headers has been fixed.
  - Groups in MCUMGR now use kernel slist entries rather than the custom MCUMGR
    structs for storage.
  - Levels of function redirection which were previously used to support multiple
    OS’s have been reduced to simplify code and reduce output size.
  - Bluetooth SMP debug output format specifier has been fixed to avoid a build
    warning on native\_posix platforms.
  - Issue with `img_mgmt_dfu_stopped()` being wrongly called on success
    has been fixed.
  - Issue with MCUMGR img\_mgmt image erase wrongly returning success during an
    error condition has been fixed.
  - Unused MCUMGR header files such as mcumgr\_util.h have been removed.
  - Verbose error response reporting has been fixed and is now present when
    enabled.
  - Internal SMP functions have been removed from the public smp.h header file
    and moved to smp\_internal.h
  - Kconfig files have been split up and moved to directories containing the
    systems they influence.
  - MCUMGR img\_mgmt image upload over-riding/hiding of result codes has been
    fixed.
- Logging

  - Removed legacy (v1) implementation and removed any references to the logging
    v2.
  - Added [`LOG_RAW`](../services/logging/index.md#c.LOG_RAW "LOG_RAW") for logging strings without additional formatting.
    It is similar to [`LOG_PRINTK`](../services/logging/index.md#c.LOG_PRINTK "LOG_PRINTK") but do not append `<cr>` when new line is found.
  - Improvements in the ADSP backend.
  - File system backend: Only delete old files if necessary.
- IPC

  - Introduced a ‘zephyr,buffer-size’ DT property to set the sizes for TX and
    RX buffers per created instance.
  - Set WQ priority back to `PRIO_PREEMPT` to fix an issue that was starving
    the scheduler.
  - `icmsg_buf` library was renamed to `spsc_pbuf`.
  - Added cache handling support to `spsc_pbuf`.
  - Fixed an issue where the TX virtqueue was misaligned by 2 bytes due to the
    way the virtqueue start address is calculated
  - Added [`ipc_service_deregister_endpoint()`](../services/ipc/ipc_service/ipc_service.md#c.ipc_service_deregister_endpoint "ipc_service_deregister_endpoint") function to deregister endpoints.
- LoRaWAN

  - Added Class-C support.
  - Upgraded the loramac-node repository to v4.6.0.
  - Moved the `REQUIRES_FULL_LIBC` library dependency from LoRa to LoRaWAN.
  - Fixed the async reception in SX127x modems.
- Modbus

  - Added user data entry for ADU callback.
- Power management

  - Allow multiple subscribers to latency changes in the policy manager.
  - Added new API to implement suspend-to-RAM (S2RAM). Select
    [`CONFIG_PM_S2RAM`](../kconfig.md#CONFIG_PM_S2RAM "CONFIG_PM_S2RAM") to enable this feature.
  - Added [`pm_device_is_powered()`](../services/pm/api/index.md#c.pm_device_is_powered "pm_device_is_powered") to query a device power state.
- POSIX

  - Made `tz` non-const in `gettimeofday()` for conformance to spec.
  - Fixed pthread descriptor resource leak. Previously only pthreads with state
    `PTHREAD_TERMINATED` could be reused. However, `pthread_join()` sets
    the state to `PTHREAD_EXITED`. Consider both states as candidates in
    `pthread_create()`.
  - Added `perror()` implementation.
  - Used consistent timebase in `sem_timedwait()`.
- RTIO

  - Initial version of an asynchronous task and executor API for I/O similar inspired
    by Linux’s very successful io\_uring.
  - Provided a simple linear and limited concurrency executor, simple task queuing,
    and the ability to poll for task completions.
- SD Subsystem

  - SDMMC STM32: Now compatible with STM32L5 series. Added DMA support for DMA-V1
    compatible devices.
  - Added support for handling the [`DISK_IOCTL_CTRL_SYNC`](../services/storage/disk/access.md#c.DISK_IOCTL_CTRL_SYNC "DISK_IOCTL_CTRL_SYNC") ioctl call.
    this enables the filesystem api [`fs_sync()`](../services/file_system/index.md#c.fs_sync "fs_sync").
- Settings

  - Added API function `settings_storage_get()` which allows to get
    the storage instance used by the settings backed to store its records.
- Shell

  - Added new API function checking shell readiness: [`shell_ready()`](../services/shell/index.md#c.shell_ready "shell_ready").
  - Added option to control formatting of the logging timestamp.
  - Added missing asserts to the shell api functions.
  - MQTT backend: bug fix to handle negative return value of the wait function.
  - A new `backends` command that lists the name and number of active shell backends.
  - Fixed handling mandatory args with optional raw arg.
- Storage

  - [`flash_area_open()`](../services/storage/flash_map/flash_map.md#c.flash_area_open "flash_area_open") returns error if area’s flash device is unreachable.
  - `flash_area` components were reworked so build-time reference to the flash
    device is used instead of its name with runtime driver buinding.
  - Added `FIXED_PARTITION_` macros that move flash\_map to use DTS node labels.
- Testsuite

  - Added Kconfig support to `unit_testing` platform.
  - Migrated tests to use `CONFIG_ZTEST_NEW_API`.
  - Added ztest options for shuffling tests/suites via:

    - [`CONFIG_ZTEST_SHUFFLE`](../kconfig.md#CONFIG_ZTEST_SHUFFLE "CONFIG_ZTEST_SHUFFLE")
    - [`CONFIG_ZTEST_SHUFFLE_SUITE_REPEAT_COUNT`](../kconfig.md#CONFIG_ZTEST_SHUFFLE_SUITE_REPEAT_COUNT "CONFIG_ZTEST_SHUFFLE_SUITE_REPEAT_COUNT")
    - [`CONFIG_ZTEST_SHUFFLE_TEST_REPEAT_COUNT`](../kconfig.md#CONFIG_ZTEST_SHUFFLE_TEST_REPEAT_COUNT "CONFIG_ZTEST_SHUFFLE_TEST_REPEAT_COUNT")
  - Added ztest native\_posix command line arguments for running specific tests/suites using
    `--test suite_name:*` or `--test suite_name::test_name` command line arguments.
- Storage

  - Flash Map API deprecates usage of `FLASH_AREA_` macros and replaces
    them with `FIXED_PARTITION_` macros. This follows removal of `label`
    property from DTS nodes.

## HALs

- Atmel

  - sam: Fixed incorrect CIDR values for revision b silicon of SAMV71 devices.
- Espressif

  - Updated Espressif HAL with esp-idf 4.4.1 updates.
  - Added support to binary blobs implementation.
  - Fixed ESP32-C3 wifi issues.
- GigaDevice

  - Added support for gd32e50x.
  - gd32e10x: upgraded to v1.3.0.
  - gd32f4xx: upgraded to v3.0.0.
- NXP

  - Updated the NXP MCUX SDK to version 2.12.
  - Updated the USB middleware to version 2.12.
  - Removed all binary Blobs for power management libraries.
  - Removed all binary archive files.
- Nordic

  - Updated nrfx to version 2.9.0.
- RPi Pico

  - Renamed `adc_read` to `pico_adc_read`, to avoid name collision with Zephyr’s API.
- STM32

  - stm32cube: update stm32f7 to cube version V1.17.0.
  - stm32cube: update stm32g0 to cube version V1.6.1.
  - stm32cube: update stm32g4 to cube version V1.5.1.
  - stm32cube: update stm32l4 to cube version V1.17.2.
  - stm32cube: update stm32u5 to cube version V1.1.1.
  - stm32cube: update stm32wb to cube version V1.14.0.
  - pinctrl: some pin definitions did not contain the “\_c” suffix, used by pins
    with analog switch on certain H7 devices.
- TI

  - simplelink: cc13x2\_cc26x2: include ADC driverlib sources.
  - simplelink: cc13x2\_cc26x2: include flash driverlib sources.
  - cc13x2: kconfig conditions for P variant support & custom RF hwattrs.
  - cc13x2\_cc26x2: update to TI SimpleLink SDK 4.40.04.04.

## MCUboot

- Added initial support for leveraging the RAM-LOAD mode with the zephyr-rtos port.
- Added the MCUboot status callback support.
  See `CONFIG_MCUBOOT_ACTION_HOOKS`.
- Edited includes to have the `zephyr/` prefix.
- Edited the DFU detection’s GPIO-pin configuration to be done through DTS using the `mcuboot-button0` pin alias.
- Edited the LED usage to prefer DTS’ `mcuboot-led0` alias over the `bootloader-led0` alias.
- Removed [`device_get_binding()`](../kernel/drivers/index.md#c.device_get_binding "device_get_binding") usage in favor of [`DEVICE_DT_GET()`](../kernel/drivers/index.md#c.DEVICE_DT_GET "DEVICE_DT_GET").
- Added support for generic watchdog0 alias.
- Enabled watchdog feed by default.
- Dropped the `CONFIG_BOOT_IMAGE_ACCESS_HOOKS_FILE` option.
  The inclusion of the Hooks implementation file is now up to the project’s customization.
- Switched zephyr port from using `FLASH_AREA_` macros to `FIXED_PARTITION_` macros.
- Made flash\_map\_backend.h compatible with a C++ compiler.
- Allowed to get the flash write alignment based on the `zephyr,flash` DT chosen node property.
- boot\_serial:

  - Upgraded from cddl-gen v0.1.0 to zcbor v0.4.0.
  - Refactored and optimized the code, mainly in what affects the progressive erase implementation.
  - Fixed a compilation issue with the echo command code.
- imgtool:

  - Added support for providing a signature through a third party.

## Trusted Firmware-M

- Allowed enabling FPU in the application when TF-M is enabled.
- Added option to exclude non-secure TF-M application from build.
- Relocated `mergehex.py` to `scripts/build`.
- Added option for custom reset handlers.

## Documentation

## Tests and Samples

- A large number of tests have been reworked to use the new ztest API, see
  [Test Framework](../develop/test/ztest.md#test-framework) for more details. This should be used for newly
  introduce tests as well.
- smp\_svr Bluetooth overlay (overlay-bt) has been reworked to increase
  throughput and enable packet reassembly.
- Added test for the new shell API function: [`shell_ready()`](../services/shell/index.md#c.shell_ready "shell_ready").

## Issue Related Items

### Known Issues

- [GitHub #22049](https://github.com/zephyrproject-rtos/zephyr/issues/22049) - Bluetooth: IRK handling issue when using multiple local identities
- [GitHub #25917](https://github.com/zephyrproject-rtos/zephyr/issues/25917) - Bluetooth: Deadlock with TX of ACL data and HCI commands (command blocked by data)
- [GitHub #30348](https://github.com/zephyrproject-rtos/zephyr/issues/30348) - XIP can’t be enabled with ARC MWDT toolchain
- [GitHub #31298](https://github.com/zephyrproject-rtos/zephyr/issues/31298) - tests/kernel/gen\_isr\_table failed on hsdk and nsim\_hs\_smp sometimes
- [GitHub #33747](https://github.com/zephyrproject-rtos/zephyr/issues/33747) - gptp does not work well on NXP rt series platform
- [GitHub #34269](https://github.com/zephyrproject-rtos/zephyr/issues/34269) - LOG\_MODE\_MINIMAL BUILD error
- [GitHub #37193](https://github.com/zephyrproject-rtos/zephyr/issues/37193) - mcumgr: Probably incorrect error handling with udp backend
- [GitHub #37731](https://github.com/zephyrproject-rtos/zephyr/issues/37731) - Bluetooth: hci samples: Unable to allocate command buffer
- [GitHub #38041](https://github.com/zephyrproject-rtos/zephyr/issues/38041) - Logging-related tests fails on qemu\_arc\_hs6x
- [GitHub #38880](https://github.com/zephyrproject-rtos/zephyr/issues/38880) - ARC: ARCv2: qemu\_arc\_em / qemu\_arc\_hs don’t work with XIP disabled
- [GitHub #38947](https://github.com/zephyrproject-rtos/zephyr/issues/38947) - Issue with SMP commands sent over the UART
- [GitHub #39598](https://github.com/zephyrproject-rtos/zephyr/issues/39598) - use of \_\_noinit with ecc memory hangs system
- [GitHub #40023](https://github.com/zephyrproject-rtos/zephyr/issues/40023) - Build fails for `native_posix` board when using C++ <atomic> header
- [GitHub #41606](https://github.com/zephyrproject-rtos/zephyr/issues/41606) - stm32u5: Re-implement VCO input and EPOD configuration
- [GitHub #41622](https://github.com/zephyrproject-rtos/zephyr/issues/41622) - Infinite mutual recursion when SMP and ATOMIC\_OPERATIONS\_C are set
- [GitHub #41822](https://github.com/zephyrproject-rtos/zephyr/issues/41822) - BLE IPSP sample cannot handle large ICMPv6 Echo Request
- [GitHub #41823](https://github.com/zephyrproject-rtos/zephyr/issues/41823) - Bluetooth: Controller: llcp: Remote request are dropped due to lack of free proc\_ctx
- [GitHub #42030](https://github.com/zephyrproject-rtos/zephyr/issues/42030) - can: “bosch,m-can-base”: Warning “missing or empty reg/ranges property”
- [GitHub #43099](https://github.com/zephyrproject-rtos/zephyr/issues/43099) - CMake: ARCH roots issue
- [GitHub #43249](https://github.com/zephyrproject-rtos/zephyr/issues/43249) - MBEDTLS\_ECP\_C not build when MBEDTLS\_USE\_PSA\_CRYPTO
- [GitHub #43308](https://github.com/zephyrproject-rtos/zephyr/issues/43308) - driver: serial: stm32: uart will lost data when use dma mode[async mode]
- [GitHub #43555](https://github.com/zephyrproject-rtos/zephyr/issues/43555) - Variables not properly initialized when using data relocation with SDRAM
- [GitHub #43562](https://github.com/zephyrproject-rtos/zephyr/issues/43562) - Setting and/or documentation of Timer and counter use/requirements for Nordic Bluetooth driver
- [GitHub #43836](https://github.com/zephyrproject-rtos/zephyr/issues/43836) - stm32: g0b1: RTT doesn’t work properly after stop mode
- [GitHub #44339](https://github.com/zephyrproject-rtos/zephyr/issues/44339) - Bluetooth:controller: Implement support for Advanced Scheduling in refactored LLCP
- [GitHub #44377](https://github.com/zephyrproject-rtos/zephyr/issues/44377) - ISO Broadcast/Receive sample not working with coded PHY
- [GitHub #44410](https://github.com/zephyrproject-rtos/zephyr/issues/44410) - drivers: modem: shell: `modem send` doesn’t honor line ending in modem cmd handler
- [GitHub #44948](https://github.com/zephyrproject-rtos/zephyr/issues/44948) - cmsis\_dsp: transofrm: error during building cf64.fpu and rf64.fpu for mps2\_an521\_remote
- [GitHub #45218](https://github.com/zephyrproject-rtos/zephyr/issues/45218) - rddrone\_fmuk66: I2C configuration incorrect
- [GitHub #45241](https://github.com/zephyrproject-rtos/zephyr/issues/45241) - (Probably) unnecessary branches in several modules
- [GitHub #45323](https://github.com/zephyrproject-rtos/zephyr/issues/45323) - Bluetooth: controller: llcp: Implement handling of delayed notifications in refactored LLCP
- [GitHub #45427](https://github.com/zephyrproject-rtos/zephyr/issues/45427) - Bluetooth: Controller: LLCP: Data structure for communication between the ISR and the thread
- [GitHub #45814](https://github.com/zephyrproject-rtos/zephyr/issues/45814) - Armclang build fails due to missing source file
- [GitHub #46073](https://github.com/zephyrproject-rtos/zephyr/issues/46073) - IPSP (IPv6 over BLE) example stop working after a short time
- [GitHub #46121](https://github.com/zephyrproject-rtos/zephyr/issues/46121) - Bluetooth: Controller: hci: Wrong periodic advertising report data status
- [GitHub #46126](https://github.com/zephyrproject-rtos/zephyr/issues/46126) - pm\_device causes assertion error in sched.c with lis2dh
- [GitHub #46401](https://github.com/zephyrproject-rtos/zephyr/issues/46401) - ARM64: Relax 4K MMU mapping alignment
- [GitHub #46596](https://github.com/zephyrproject-rtos/zephyr/issues/46596) - STM32F74X RMII interface does not work
- [GitHub #46598](https://github.com/zephyrproject-rtos/zephyr/issues/46598) - Logging with RTT backend on STM32WB strange behavier
- [GitHub #46844](https://github.com/zephyrproject-rtos/zephyr/issues/46844) - Timer drivers likely have off-by-one in rapidly-presented timeouts
- [GitHub #46846](https://github.com/zephyrproject-rtos/zephyr/issues/46846) - lib: libc: newlib: strerror\_r non-functional
- [GitHub #46986](https://github.com/zephyrproject-rtos/zephyr/issues/46986) - Logging (deferred v2) with a lot of output causes MPU fault
- [GitHub #47014](https://github.com/zephyrproject-rtos/zephyr/issues/47014) - can: iso-tp: implementation test failed with twister on nucleo\_g474re
- [GitHub #47092](https://github.com/zephyrproject-rtos/zephyr/issues/47092) - driver: nrf: uarte: new dirver breaks our implementation for uart.
- [GitHub #47120](https://github.com/zephyrproject-rtos/zephyr/issues/47120) - shell uart: busy wait for DTR in ISR
- [GitHub #47477](https://github.com/zephyrproject-rtos/zephyr/issues/47477) - qemu\_leon3: tests/kernel/fpu\_sharing/generic/ failed when migrating to new ztest API
- [GitHub #47500](https://github.com/zephyrproject-rtos/zephyr/issues/47500) - twister: cmake: Failure of “–build-only -M” combined with “–test-only” for –device-testing
- [GitHub #47607](https://github.com/zephyrproject-rtos/zephyr/issues/47607) - Settings with FCB backend does not pass test on stm32h743
- [GitHub #47732](https://github.com/zephyrproject-rtos/zephyr/issues/47732) - Flash map does not fare well with MCU who do bank swaps
- [GitHub #47817](https://github.com/zephyrproject-rtos/zephyr/issues/47817) - samples/modules/nanopb/sample.modules.nanopb fails with protobuf > 3.19.0
- [GitHub #47908](https://github.com/zephyrproject-rtos/zephyr/issues/47908) - tests/kernel/mem\_protect/stack\_random works unreliably and sporadically fails
- [GitHub #47988](https://github.com/zephyrproject-rtos/zephyr/issues/47988) - JSON parser not consistent on extra data
- [GitHub #48018](https://github.com/zephyrproject-rtos/zephyr/issues/48018) - ztest: static threads are not re-launched for repeated test suite execution.
- [GitHub #48037](https://github.com/zephyrproject-rtos/zephyr/issues/48037) - Grove LCD Sample Not Working
- [GitHub #48094](https://github.com/zephyrproject-rtos/zephyr/issues/48094) - pre-commit scripts fail when there is a space in zephyr\_base
- [GitHub #48102](https://github.com/zephyrproject-rtos/zephyr/issues/48102) - JSON parses uses recursion (breaks rule 17.2)
- [GitHub #48147](https://github.com/zephyrproject-rtos/zephyr/issues/48147) - ztest: before/after functions may run on different threads, which may cause potential issues.
- [GitHub #48287](https://github.com/zephyrproject-rtos/zephyr/issues/48287) - malloc\_prepare ASSERT happens when enabling newlib libc with demand paging
- [GitHub #48299](https://github.com/zephyrproject-rtos/zephyr/issues/48299) - SHT3XD\_CMD\_WRITE\_TH\_LOW\_SET should be SHT3XD\_CMD\_WRITE\_TH\_LOW\_CLEAR
- [GitHub #48304](https://github.com/zephyrproject-rtos/zephyr/issues/48304) - bt\_disable() does not work properly on nRF52
- [GitHub #48390](https://github.com/zephyrproject-rtos/zephyr/issues/48390) - [Intel Cavs] Boot failures on low optimization levels
- [GitHub #48394](https://github.com/zephyrproject-rtos/zephyr/issues/48394) - vsnprintfcb writes to `*str` if it is NULL
- [GitHub #48468](https://github.com/zephyrproject-rtos/zephyr/issues/48468) - GSM Mux does not transmit all queued data when uart\_fifo\_fill is called
- [GitHub #48473](https://github.com/zephyrproject-rtos/zephyr/issues/48473) - Setting CONFIG\_GSM\_MUX\_INITIATOR=n results in a compile error
- [GitHub #48505](https://github.com/zephyrproject-rtos/zephyr/issues/48505) - BLE stack can get stuck in connected state despite connection failure
- [GitHub #48520](https://github.com/zephyrproject-rtos/zephyr/issues/48520) - clang-format: #include reorder due to default: SortIncludesOptions != SI\_Never
- [GitHub #48603](https://github.com/zephyrproject-rtos/zephyr/issues/48603) - LoRa driver asynchronous receive callback clears data before the callback.
- [GitHub #48608](https://github.com/zephyrproject-rtos/zephyr/issues/48608) - boards: mps2\_an385: Unstable system timer
- [GitHub #48625](https://github.com/zephyrproject-rtos/zephyr/issues/48625) - GSM\_PPP api keeps sending commands to muxed AT channel
- [GitHub #48726](https://github.com/zephyrproject-rtos/zephyr/issues/48726) - net: tests/net/ieee802154/l2/net.ieee802154.l2 failed on reel board
- [GitHub #48841](https://github.com/zephyrproject-rtos/zephyr/issues/48841) - Bluetooth: df: Assert in lower link layer when requesting CTE from peer periodically with 7.5ms connection interval
- [GitHub #48850](https://github.com/zephyrproject-rtos/zephyr/issues/48850) - Bluetooth: LLCP: possible access to released control procedure context
- [GitHub #48857](https://github.com/zephyrproject-rtos/zephyr/issues/48857) - samples: Bluetooth: Buffer size mismatch in samples/bluetooth/hci\_usb for nRF5340
- [GitHub #48953](https://github.com/zephyrproject-rtos/zephyr/issues/48953) - ‘intel,sha’ is missing binding and usage
- [GitHub #48954](https://github.com/zephyrproject-rtos/zephyr/issues/48954) - several NXP devicetree bindings are missing
- [GitHub #48992](https://github.com/zephyrproject-rtos/zephyr/issues/48992) - qemu\_leon3: tests/posix/common/portability.posix.common fails
- [GitHub #49021](https://github.com/zephyrproject-rtos/zephyr/issues/49021) - uart async api does not provide all received data
- [GitHub #49032](https://github.com/zephyrproject-rtos/zephyr/issues/49032) - espi saf testing disabled
- [GitHub #49069](https://github.com/zephyrproject-rtos/zephyr/issues/49069) - log: cdc\_acm: hard fault message does not output
- [GitHub #49148](https://github.com/zephyrproject-rtos/zephyr/issues/49148) - Asynchronous UART API triggers Zephyr assertion on STM32WB55
- [GitHub #49210](https://github.com/zephyrproject-rtos/zephyr/issues/49210) - BL5340 board cannot build bluetooth applications
- [GitHub #49213](https://github.com/zephyrproject-rtos/zephyr/issues/49213) - logging.add.log\_user test fails when compiled with GCC 12
- [GitHub #49266](https://github.com/zephyrproject-rtos/zephyr/issues/49266) - Bluetooth: Host doesn’t seem to handle INCOMPLETE per adv reports
- [GitHub #49313](https://github.com/zephyrproject-rtos/zephyr/issues/49313) - nRF51822 sometimes hard fault on connect
- [GitHub #49338](https://github.com/zephyrproject-rtos/zephyr/issues/49338) - Antenna switching for Bluetooth direction finding with the nRF5340
- [GitHub #49373](https://github.com/zephyrproject-rtos/zephyr/issues/49373) - BLE scanning - BT RX thread hangs on.
- [GitHub #49390](https://github.com/zephyrproject-rtos/zephyr/issues/49390) - shell\_rtt thread can starve other threads of the same priority
- [GitHub #49484](https://github.com/zephyrproject-rtos/zephyr/issues/49484) - CONFIG\_BOOTLOADER\_SRAM\_SIZE should not be defined by default
- [GitHub #49492](https://github.com/zephyrproject-rtos/zephyr/issues/49492) - kernel.poll test fails on qemu\_arc\_hs6x when compiled with GCC 12
- [GitHub #49494](https://github.com/zephyrproject-rtos/zephyr/issues/49494) - testing.ztest.ztress test fails on qemu\_cortex\_r5 when compiled with GCC 12
- [GitHub #49584](https://github.com/zephyrproject-rtos/zephyr/issues/49584) - STM32WB55 Failed read remote feature, remote version and LE set PHY
- [GitHub #49588](https://github.com/zephyrproject-rtos/zephyr/issues/49588) - Json parser is incorrect with undefined parameter
- [GitHub #49611](https://github.com/zephyrproject-rtos/zephyr/issues/49611) - ehl\_crb: Failed to run timer testcases
- [GitHub #49614](https://github.com/zephyrproject-rtos/zephyr/issues/49614) - acrn\_ehl\_crb: The testcase tests/kernel/sched/schedule\_api failed to run.
- [GitHub #49656](https://github.com/zephyrproject-rtos/zephyr/issues/49656) - acrn\_ehl\_crb: testcases tests/kernel/smp failed to run on v2.7-branch
- [GitHub #49746](https://github.com/zephyrproject-rtos/zephyr/issues/49746) - twister: extra test results
- [GitHub #49811](https://github.com/zephyrproject-rtos/zephyr/issues/49811) - DHCP cannot obtain IP, when CONFIG\_NET\_VLAN is enabled
- [GitHub #49816](https://github.com/zephyrproject-rtos/zephyr/issues/49816) - ISOTP receive fails for multiple binds with same CAN ID but different extended ID
- [GitHub #49889](https://github.com/zephyrproject-rtos/zephyr/issues/49889) - ctf trace: unknown event id when parsing samples/tracing result on reel board
- [GitHub #49917](https://github.com/zephyrproject-rtos/zephyr/issues/49917) - http\_client\_req() sometimes hangs when peer disconnects
- [GitHub #49963](https://github.com/zephyrproject-rtos/zephyr/issues/49963) - Random crash on the L475 due to work->handler set to NULL
- [GitHub #49996](https://github.com/zephyrproject-rtos/zephyr/issues/49996) - tests: drivers: clock\_control: nrf\_lf\_clock\_start and nrf\_onoff\_and\_bt fails
- [GitHub #50028](https://github.com/zephyrproject-rtos/zephyr/issues/50028) - flash\_stm32\_ospi Write enable failed when building with TF-M
- [GitHub #50084](https://github.com/zephyrproject-rtos/zephyr/issues/50084) - drivers: nrf\_802154: nrf\_802154\_trx.c - assertion fault when enabling Segger SystemView tracing
- [GitHub #50095](https://github.com/zephyrproject-rtos/zephyr/issues/50095) - ARC revision Kconfigs wrongly mixed with board name
- [GitHub #50149](https://github.com/zephyrproject-rtos/zephyr/issues/50149) - tests: drivers: flash fails on nucleo\_l152re because of wrong erase flash size
- [GitHub #50196](https://github.com/zephyrproject-rtos/zephyr/issues/50196) - LSM6DSO interrupt handler not being called
- [GitHub #50256](https://github.com/zephyrproject-rtos/zephyr/issues/50256) - I2C on SAMC21 sends out stop condition incorrectly
- [GitHub #50306](https://github.com/zephyrproject-rtos/zephyr/issues/50306) - Not able to flash stm32h735g\_disco - TARGET: stm32h7x.cpu0 - Not halted
- [GitHub #50345](https://github.com/zephyrproject-rtos/zephyr/issues/50345) - Network traffic occurs before Bluetooth NET L2 (IPSP) link setup complete
- [GitHub #50354](https://github.com/zephyrproject-rtos/zephyr/issues/50354) - ztest\_new: \_zassert\_base : return without post processing
- [GitHub #50404](https://github.com/zephyrproject-rtos/zephyr/issues/50404) - Intel CAVS: tests/subsys/logging/log\_immediate failed.
- [GitHub #50427](https://github.com/zephyrproject-rtos/zephyr/issues/50427) - Bluetooth: host: central connection context leak
- [GitHub #50446](https://github.com/zephyrproject-rtos/zephyr/issues/50446) - MCUX CAAM is disabled temporarily
- [GitHub #50452](https://github.com/zephyrproject-rtos/zephyr/issues/50452) - mec172xevb\_assy6906: The testcase tests/lib/cmsis\_dsp/matrix failed to run.
- [GitHub #50501](https://github.com/zephyrproject-rtos/zephyr/issues/50501) - STM32 SPI does not work properly with async + interrupts
- [GitHub #50506](https://github.com/zephyrproject-rtos/zephyr/issues/50506) - nxp,mcux-usbd devicetree binding issues
- [GitHub #50515](https://github.com/zephyrproject-rtos/zephyr/issues/50515) - Non-existing test cases reported as “Skipped” with reason “No results captured, testsuite misconfiguration?” in test report
- [GitHub #50546](https://github.com/zephyrproject-rtos/zephyr/issues/50546) - drivers: can: rcar: likely inconsistent behavior when calling can\_stop() with pending transmissions
- [GitHub #50554](https://github.com/zephyrproject-rtos/zephyr/issues/50554) - Test uart async failed on Nucleo F429ZI
- [GitHub #50565](https://github.com/zephyrproject-rtos/zephyr/issues/50565) - Fatal error after `west flash` for nucleo\_l053r8
- [GitHub #50567](https://github.com/zephyrproject-rtos/zephyr/issues/50567) - Passed test cases are reported as “Skipped” because of incomplete test log
- [GitHub #50570](https://github.com/zephyrproject-rtos/zephyr/issues/50570) - samples/drivers/can/counter fails in twister for native\_posix
- [GitHub #50587](https://github.com/zephyrproject-rtos/zephyr/issues/50587) - Regression in Link Layer Control Procedure (LLCP)
- [GitHub #50590](https://github.com/zephyrproject-rtos/zephyr/issues/50590) - openocd: Can’t flash on various STM32 boards
- [GitHub #50598](https://github.com/zephyrproject-rtos/zephyr/issues/50598) - UDP over IPSP not working on nRF52840
- [GitHub #50614](https://github.com/zephyrproject-rtos/zephyr/issues/50614) - Zephyr if got the ip is “10.xxx.xxx.xxx” when join in the switchboard, then the device may can not visit the outer net, also unable to Ping.
- [GitHub #50620](https://github.com/zephyrproject-rtos/zephyr/issues/50620) - fifo test fails with CONFIG\_CMAKE\_LINKER\_GENERATOR enabled on qemu\_cortex\_a9
- [GitHub #50652](https://github.com/zephyrproject-rtos/zephyr/issues/50652) - RAM Loading on i.MXRT1160\_evk
- [GitHub #50655](https://github.com/zephyrproject-rtos/zephyr/issues/50655) - STM32WB55 Bus Fault when connecting then disconnecting then connecting then disconnecting then connecting
- [GitHub #50658](https://github.com/zephyrproject-rtos/zephyr/issues/50658) - BLE stack notifications blocks host side for too long
- [GitHub #50709](https://github.com/zephyrproject-rtos/zephyr/issues/50709) - tests: arch: arm: arm\_thread\_swap fails on stm32g0 or stm32l0
- [GitHub #50732](https://github.com/zephyrproject-rtos/zephyr/issues/50732) - net: tests/net/ieee802154/l2/net.ieee802154.l2 failed on reel\_board due to build failure
- [GitHub #50735](https://github.com/zephyrproject-rtos/zephyr/issues/50735) - Intel CAVS18: tests/boards/intel\_adsp/hda\_log/boards.intel\_adsp.hda\_log.printk failed
- [GitHub #50746](https://github.com/zephyrproject-rtos/zephyr/issues/50746) - Stale kernel memory pool API references
- [GitHub #50766](https://github.com/zephyrproject-rtos/zephyr/issues/50766) - Zephyr build system doesn’t setup CMake host environment correctly
- [GitHub #50776](https://github.com/zephyrproject-rtos/zephyr/issues/50776) - CAN Drivers allow sending FD frames without device being set to FD mode
- [GitHub #50777](https://github.com/zephyrproject-rtos/zephyr/issues/50777) - LE Audio: Receiver start ready command shall only be sent by the receiver
- [GitHub #50778](https://github.com/zephyrproject-rtos/zephyr/issues/50778) - LE Audio: Audio shell: Unicast server cannot execute commands for the default\_stream
- [GitHub #50780](https://github.com/zephyrproject-rtos/zephyr/issues/50780) - LE Audio: Bidirectional handling of 2 audio streams as the unicast server when streams are configured separately not working as intended
- [GitHub #50781](https://github.com/zephyrproject-rtos/zephyr/issues/50781) - LE Audio: mpl init causes warnings when adding objects
- [GitHub #50783](https://github.com/zephyrproject-rtos/zephyr/issues/50783) - LE Audio: Reject ISO data if the stream is not in the streaming state
- [GitHub #50789](https://github.com/zephyrproject-rtos/zephyr/issues/50789) - west: runners: blackmagicprobe: Doesn’t work on windows due to wrong path separator
- [GitHub #50801](https://github.com/zephyrproject-rtos/zephyr/issues/50801) - JSON parser fails on multidimensional arrays
- [GitHub #50812](https://github.com/zephyrproject-rtos/zephyr/issues/50812) - MCUmgr udp sample fails with shell - BUS FAULT
- [GitHub #50841](https://github.com/zephyrproject-rtos/zephyr/issues/50841) - high SRAM usage with picolibc on nRF platforms

### Addressed issues

- [GitHub #50861](https://github.com/zephyrproject-rtos/zephyr/issues/50861) - Intel ADSP HDA and GPDMA Bugs
- [GitHub #50843](https://github.com/zephyrproject-rtos/zephyr/issues/50843) - tests: kernel: timer: timer\_behavior: kernel.timer.timer - SRAM overflow on nrf5340dk\_nrf5340\_cpunet and nrf52dk\_nrf52832
- [GitHub #50841](https://github.com/zephyrproject-rtos/zephyr/issues/50841) - high SRAM usage with picolibc on some userspace platforms
- [GitHub #50774](https://github.com/zephyrproject-rtos/zephyr/issues/50774) - ESP32 GPIO34 IRQ not working
- [GitHub #50771](https://github.com/zephyrproject-rtos/zephyr/issues/50771) - mcan driver has tx and rx error counts swapped
- [GitHub #50754](https://github.com/zephyrproject-rtos/zephyr/issues/50754) - MCUboot update breaks compilation for boards without CONFIG\_WATCHDOG=y
- [GitHub #50737](https://github.com/zephyrproject-rtos/zephyr/issues/50737) - tfm\_ram\_report does not work with sdk-ng 0.15.0
- [GitHub #50728](https://github.com/zephyrproject-rtos/zephyr/issues/50728) - missing SMP fixes for RISC-V
- [GitHub #50691](https://github.com/zephyrproject-rtos/zephyr/issues/50691) - Bluetooth: Host: CONFIG\_BT\_LOG\_SNIFFER\_INFO doesn’t work as intended without bonding
- [GitHub #50689](https://github.com/zephyrproject-rtos/zephyr/issues/50689) - Suspected unaligned access in Bluetooth controller connection handling
- [GitHub #50681](https://github.com/zephyrproject-rtos/zephyr/issues/50681) - gpio: ite: gpio\_ite\_configure() neither supporting nor throwing error when gpio is configured with GPIO\_DISCONNECTED flag
- [GitHub #50656](https://github.com/zephyrproject-rtos/zephyr/issues/50656) - Wrong definition of bank size for intel memory management driver.
- [GitHub #50654](https://github.com/zephyrproject-rtos/zephyr/issues/50654) - Some files are being ALWAYS built, without them being used
- [GitHub #50635](https://github.com/zephyrproject-rtos/zephyr/issues/50635) - hal: stm32: valid pins were removed in the last version
- [GitHub #50631](https://github.com/zephyrproject-rtos/zephyr/issues/50631) - Please Add \_\_heapstats() to stdlib.h
- [GitHub #50621](https://github.com/zephyrproject-rtos/zephyr/issues/50621) - The history of the multi API / MFD discussions 2022 July - Sep
- [GitHub #50619](https://github.com/zephyrproject-rtos/zephyr/issues/50619) - tests/kernel/timer/starve fails to run on devices
- [GitHub #50618](https://github.com/zephyrproject-rtos/zephyr/issues/50618) - STM32 Ethernet
- [GitHub #50615](https://github.com/zephyrproject-rtos/zephyr/issues/50615) - ESP32 GPIO driver
- [GitHub #50611](https://github.com/zephyrproject-rtos/zephyr/issues/50611) - k\_heap\_aligned\_alloc does not handle a timeout of K\_FOREVER correctly
- [GitHub #50603](https://github.com/zephyrproject-rtos/zephyr/issues/50603) - Upgrade to loramac-node 4.7.0 when it is released to fix async LoRa reception on SX1276
- [GitHub #50579](https://github.com/zephyrproject-rtos/zephyr/issues/50579) - arch: arm: Using ISR\_DIRECT\_PM with zero-latency-interrupt violation
- [GitHub #50549](https://github.com/zephyrproject-rtos/zephyr/issues/50549) - USB: samhs: Device does not work after detach-attach sequence
- [GitHub #50545](https://github.com/zephyrproject-rtos/zephyr/issues/50545) - drivers: can: inconsistent behavior when calling can\_stop() with pending transmissions
- [GitHub #50538](https://github.com/zephyrproject-rtos/zephyr/issues/50538) - lpcxpresso55s69\_cpu0 samples/subsys/usb/dfu/sample.usb.dfu build failure
- [GitHub #50525](https://github.com/zephyrproject-rtos/zephyr/issues/50525) - Passed test cases reported as “Skipped” because test log lost
- [GitHub #50522](https://github.com/zephyrproject-rtos/zephyr/issues/50522) - mgmt: mcumgr: img\_mgmt: Failure of erase returns nothing
- [GitHub #50520](https://github.com/zephyrproject-rtos/zephyr/issues/50520) - Bluetooth: bsim eatt\_notif test fails with assertion in some environments
- [GitHub #50502](https://github.com/zephyrproject-rtos/zephyr/issues/50502) - iMX 7D GPIO Pinmux Array Has Incorrect Ordering
- [GitHub #50482](https://github.com/zephyrproject-rtos/zephyr/issues/50482) - mcumgr: img\_mgmt: zephyr\_img\_mgmt\_flash\_area\_id has wrong slot3 ID
- [GitHub #50468](https://github.com/zephyrproject-rtos/zephyr/issues/50468) - Incorrect Z\_THREAD\_STACK\_BUFFER in arch\_start\_cpu for Xtensa
- [GitHub #50467](https://github.com/zephyrproject-rtos/zephyr/issues/50467) - Possible memory corruption on ARC when userspace is enabled
- [GitHub #50465](https://github.com/zephyrproject-rtos/zephyr/issues/50465) - Possible memory corruption on RISCV when userspace is enabled
- [GitHub #50464](https://github.com/zephyrproject-rtos/zephyr/issues/50464) - Boot banner can cut through output of shell prompt
- [GitHub #50455](https://github.com/zephyrproject-rtos/zephyr/issues/50455) - Intel CAVS15/25: tests/subsys/shell/shell failed with no console output
- [GitHub #50438](https://github.com/zephyrproject-rtos/zephyr/issues/50438) - Bluetooth: Conn: Bluetooth stack becomes unusable when communicating with both centrals and peripherals
- [GitHub #50432](https://github.com/zephyrproject-rtos/zephyr/issues/50432) - Bluetooth: Controller: Restarting BLE scanning not always working and sometimes crashes together with periodic. adv.
- [GitHub #50421](https://github.com/zephyrproject-rtos/zephyr/issues/50421) - Sysbuild-configured project using `west flash --recover` will wrongly recover (and reset) the MCU each time it flashes an image
- [GitHub #50414](https://github.com/zephyrproject-rtos/zephyr/issues/50414) - smp\_dummy.h file is outside of zephyr include folder
- [GitHub #50394](https://github.com/zephyrproject-rtos/zephyr/issues/50394) - RT685 flash chip size is incorrect
- [GitHub #50386](https://github.com/zephyrproject-rtos/zephyr/issues/50386) - Twister “FLASH overflow” does not account for imgtool trailer.
- [GitHub #50374](https://github.com/zephyrproject-rtos/zephyr/issues/50374) - CI failure in v3.1.0-rc2 full run
- [GitHub #50368](https://github.com/zephyrproject-rtos/zephyr/issues/50368) - esp32: counter driver not working with absolute value
- [GitHub #50344](https://github.com/zephyrproject-rtos/zephyr/issues/50344) - bl5340\_dvk\_cpuapp: undefined reference to `__device_dts_ord_14`
- [GitHub #50343](https://github.com/zephyrproject-rtos/zephyr/issues/50343) - uninitialized variable in kernel.workqueue test
- [GitHub #50342](https://github.com/zephyrproject-rtos/zephyr/issues/50342) - mcuboot: BOOT\_MAX\_ALIGN is redefined
- [GitHub #50341](https://github.com/zephyrproject-rtos/zephyr/issues/50341) - undefined reference to `log_output_flush` in sample.logger.syst.catalog
- [GitHub #50331](https://github.com/zephyrproject-rtos/zephyr/issues/50331) - net mem shell output indents TX DATA line
- [GitHub #50330](https://github.com/zephyrproject-rtos/zephyr/issues/50330) - Fail to find GICv3 Redistributor base address for Cortex-R52 running in a cluster different than 0
- [GitHub #50327](https://github.com/zephyrproject-rtos/zephyr/issues/50327) - JLink needs flashloader for MIMXRT1060-EVK
- [GitHub #50317](https://github.com/zephyrproject-rtos/zephyr/issues/50317) - boards/arm/thingy53\_nrf5340: lack of mcuboot’s gpio aliases
- [GitHub #50306](https://github.com/zephyrproject-rtos/zephyr/issues/50306) - Not able to flash stm32h735g\_disco - TARGET: stm32h7x.cpu0 - Not halted
- [GitHub #50299](https://github.com/zephyrproject-rtos/zephyr/issues/50299) - CI fails building stm32u5 tests/subsys/pm/device\_runtime\_api
- [GitHub #50297](https://github.com/zephyrproject-rtos/zephyr/issues/50297) - mcumgr: fs\_mgmt: hash/checksum: Build warnings on native\_posix\_64
- [GitHub #50294](https://github.com/zephyrproject-rtos/zephyr/issues/50294) - test-ci: timer\_behavior: mimxrt1170\_evk\_cm7/1160: test failure
- [GitHub #50284](https://github.com/zephyrproject-rtos/zephyr/issues/50284) - Generated linker scripts break when ZEPHYR\_BASE and ZEPHYR\_MODULES share structure that contains symlinks
- [GitHub #50282](https://github.com/zephyrproject-rtos/zephyr/issues/50282) - samples: drivers: can: babbling: can controller not started.
- [GitHub #50266](https://github.com/zephyrproject-rtos/zephyr/issues/50266) - drivers: can: native\_posix\_linux: should not receive frames while stopped
- [GitHub #50263](https://github.com/zephyrproject-rtos/zephyr/issues/50263) - drivers: can: mcan: transceiver is enabled at driver initialization
- [GitHub #50257](https://github.com/zephyrproject-rtos/zephyr/issues/50257) - twister: –coverage option does not work for qemu\_x86\_64 and other boards
- [GitHub #50255](https://github.com/zephyrproject-rtos/zephyr/issues/50255) - Test process crash when run twister with –coverage
- [GitHub #50244](https://github.com/zephyrproject-rtos/zephyr/issues/50244) - GPIO manipulation from a “counter” (ie HW timer) when Bluetooth (BLE) is enabled.
- [GitHub #50238](https://github.com/zephyrproject-rtos/zephyr/issues/50238) - ESP32: rtcio\_ll\_pullup\_disable crash regression
- [GitHub #50235](https://github.com/zephyrproject-rtos/zephyr/issues/50235) - UDP: Memory leak when allocated packet is smaller than requested
- [GitHub #50232](https://github.com/zephyrproject-rtos/zephyr/issues/50232) - gpio\_shell: Not functional anymore following DT label cleanup and deprecation
- [GitHub #50226](https://github.com/zephyrproject-rtos/zephyr/issues/50226) - MPU FAULT: Stacking error with lvgl on lv\_timer\_handler()
- [GitHub #50224](https://github.com/zephyrproject-rtos/zephyr/issues/50224) - tests/kernel/tickless/tickless\_concept: Failed on STM32
- [GitHub #50219](https://github.com/zephyrproject-rtos/zephyr/issues/50219) - Kernel tests failing on qemu\_riscv32\_smp
- [GitHub #50218](https://github.com/zephyrproject-rtos/zephyr/issues/50218) - rcar\_h3ulcb: can: failed to run RTR test cases
- [GitHub #50214](https://github.com/zephyrproject-rtos/zephyr/issues/50214) - Missing human readable names in names file od deive structure
- [GitHub #50202](https://github.com/zephyrproject-rtos/zephyr/issues/50202) - Configuring `GPIO25` crashes ESP32
- [GitHub #50192](https://github.com/zephyrproject-rtos/zephyr/issues/50192) - nrf\_qspi\_nor driver might crash if power management is enabled
- [GitHub #50191](https://github.com/zephyrproject-rtos/zephyr/issues/50191) - nrf\_qspi\_nor-driver leaves CS pin to undefined state when pinctrl is enabled
- [GitHub #50172](https://github.com/zephyrproject-rtos/zephyr/issues/50172) - QSPI NAND Flash driver question
- [GitHub #50165](https://github.com/zephyrproject-rtos/zephyr/issues/50165) - boards: riscv: ite: No flash and RAM stats are shown whenever building ITE board
- [GitHub #50158](https://github.com/zephyrproject-rtos/zephyr/issues/50158) - Drivers: gpio: stm32u5 portG not working
- [GitHub #50152](https://github.com/zephyrproject-rtos/zephyr/issues/50152) - SMT32: incorrect internal temperature value
- [GitHub #50150](https://github.com/zephyrproject-rtos/zephyr/issues/50150) - tests: drivers: flash: building error with b\_u585i\_iot02a\_ns board
- [GitHub #50146](https://github.com/zephyrproject-rtos/zephyr/issues/50146) - tests: kernel: mem\_protect fails on ARMv6-M and ARMv8-M Baseline
- [GitHub #50142](https://github.com/zephyrproject-rtos/zephyr/issues/50142) - NXP i.MX RT1024 CPU GPIO access bug.
- [GitHub #50140](https://github.com/zephyrproject-rtos/zephyr/issues/50140) - ARP handling causes dropped packets when multiple outgoing packets are queued
- [GitHub #50135](https://github.com/zephyrproject-rtos/zephyr/issues/50135) - cannot boot up on custom board
- [GitHub #50119](https://github.com/zephyrproject-rtos/zephyr/issues/50119) - non-IPI path of SMP is broken
- [GitHub #50118](https://github.com/zephyrproject-rtos/zephyr/issues/50118) - Twister: `--coverage-formats` Does not work despite `--coverage` added
- [GitHub #50108](https://github.com/zephyrproject-rtos/zephyr/issues/50108) - drivers: console: rtt\_console: undefined reference to `__printk_hook_install`
- [GitHub #50107](https://github.com/zephyrproject-rtos/zephyr/issues/50107) - subsys: pm: device\_runtime.c: compile error
- [GitHub #50106](https://github.com/zephyrproject-rtos/zephyr/issues/50106) - ram\_report stopped working with zephyr-sdk 0.15
- [GitHub #50099](https://github.com/zephyrproject-rtos/zephyr/issues/50099) - boards: pinnacle\_100\_dvk should enable QSPI and modem by default
- [GitHub #50096](https://github.com/zephyrproject-rtos/zephyr/issues/50096) - tests: drivers: the gpio\_basic\_api test cannot be build successfully on bl5340\_dvk\_cpuapp board
- [GitHub #50073](https://github.com/zephyrproject-rtos/zephyr/issues/50073) - mcumgr: Bluetooth backend does not restart advertising after disconnect
- [GitHub #50070](https://github.com/zephyrproject-rtos/zephyr/issues/50070) - LoRa: Support on RFM95 LoRa module combined with a nRF52 board
- [GitHub #50066](https://github.com/zephyrproject-rtos/zephyr/issues/50066) - tests: tests/drivers/can/shell failed in daily test on many platforms
- [GitHub #50065](https://github.com/zephyrproject-rtos/zephyr/issues/50065) - tests: tests/subsys/shell/shell test case fail in daily test on many platforms
- [GitHub #50061](https://github.com/zephyrproject-rtos/zephyr/issues/50061) - Bluetooth: Samples: bluetooth\_audio\_source does not send multiple streams
- [GitHub #50044](https://github.com/zephyrproject-rtos/zephyr/issues/50044) - reel\_board: pyocd.yaml causes flashing error on reel board
- [GitHub #50033](https://github.com/zephyrproject-rtos/zephyr/issues/50033) - tests: subsys: fs: littlefs: filesystem.littlefs.custom fails to build
- [GitHub #50032](https://github.com/zephyrproject-rtos/zephyr/issues/50032) - tests: subsys: shell: shell.core and drivers.can.shell fails at shell\_setup
- [GitHub #50029](https://github.com/zephyrproject-rtos/zephyr/issues/50029) - Unable to use functions from gsm\_ppp driver
- [GitHub #50023](https://github.com/zephyrproject-rtos/zephyr/issues/50023) - tests: some driver tests of frdm\_k64f build failed in twister (shows devicetree error)
- [GitHub #50016](https://github.com/zephyrproject-rtos/zephyr/issues/50016) - jlinkarm.so files renamed in latest J-Link drivers
- [GitHub #49988](https://github.com/zephyrproject-rtos/zephyr/issues/49988) - boards: pinnacle\_100\_dvk: UART1 flow control is not turned on
- [GitHub #49987](https://github.com/zephyrproject-rtos/zephyr/issues/49987) - Unable to compile on windows
- [GitHub #49985](https://github.com/zephyrproject-rtos/zephyr/issues/49985) - STM32:NUCLEO\_WL55JC No serial RX in STOP mode
- [GitHub #49982](https://github.com/zephyrproject-rtos/zephyr/issues/49982) - SD: f\_sync will always fail using the sdhc\_spi driver
- [GitHub #49970](https://github.com/zephyrproject-rtos/zephyr/issues/49970) - strange behavior in the spi\_flash example
- [GitHub #49960](https://github.com/zephyrproject-rtos/zephyr/issues/49960) - LoRaWAN Code won’t linking when config with CN470 region
- [GitHub #49956](https://github.com/zephyrproject-rtos/zephyr/issues/49956) - `NRF_DRIVE_S0D1` option is not always overridden in the `nordic,nrf-twi` and `nordic,nrf-twim` nodes
- [GitHub #49953](https://github.com/zephyrproject-rtos/zephyr/issues/49953) - stm32 gpio\_basic\_api test fail with CONFIG\_ZTEST\_NEW\_API
- [GitHub #49939](https://github.com/zephyrproject-rtos/zephyr/issues/49939) - stm32 adc driver\_api test fails on stm32wb55 and stm32l5
- [GitHub #49938](https://github.com/zephyrproject-rtos/zephyr/issues/49938) - drivers/modem/gsm\_ppp.c: unnecessary modem\_cmd\_handler\_tx\_lock when CONFIG\_GSM\_MUX disabled
- [GitHub #49924](https://github.com/zephyrproject-rtos/zephyr/issues/49924) - tests: drivers: pwm\_api and pwm\_loopback tests failed on frdm\_k64f boards
- [GitHub #49923](https://github.com/zephyrproject-rtos/zephyr/issues/49923) - ASSERTION FAIL [!arch\_is\_in\_isr()] @ WEST\_TOPDIR/zephyr/kernel/sched.c:1449
- [GitHub #49916](https://github.com/zephyrproject-rtos/zephyr/issues/49916) - renesas smartbond family Kconfig visible to non-renesas devices
- [GitHub #49915](https://github.com/zephyrproject-rtos/zephyr/issues/49915) - Bluetooth: Controller: Syncing with devices with per. adv. int. < ~10ms eventually causes events from BT controller stop arriving
- [GitHub #49903](https://github.com/zephyrproject-rtos/zephyr/issues/49903) - riscv: Enabling IRQ vector table makes Zephyr unbootable
- [GitHub #49897](https://github.com/zephyrproject-rtos/zephyr/issues/49897) - STM32: NUCLEO\_WL55JC internal (die) temperature incorrect
- [GitHub #49890](https://github.com/zephyrproject-rtos/zephyr/issues/49890) - drivers/can: stm32\_fd: CONFIG\_CAN\_STM32FD\_CLOCK\_DIVISOR not applied in driver setup
- [GitHub #49876](https://github.com/zephyrproject-rtos/zephyr/issues/49876) - drivers: can: twai: driver fails initialization
- [GitHub #49874](https://github.com/zephyrproject-rtos/zephyr/issues/49874) - STM32G0 HW\_STACK\_PROTECTION Warning
- [GitHub #49852](https://github.com/zephyrproject-rtos/zephyr/issues/49852) - uart: extra XOFF byte in the read buffer
- [GitHub #49851](https://github.com/zephyrproject-rtos/zephyr/issues/49851) - Bluetooth Controller with Extended Advertising
- [GitHub #49846](https://github.com/zephyrproject-rtos/zephyr/issues/49846) - mimxrt1160\_evk network samples stopped working
- [GitHub #49825](https://github.com/zephyrproject-rtos/zephyr/issues/49825) - net: ip: tcp: use zu format specifier for size\_t
- [GitHub #49823](https://github.com/zephyrproject-rtos/zephyr/issues/49823) - Example Application: Use of undocumented zephyr/module.yml in application folder
- [GitHub #49814](https://github.com/zephyrproject-rtos/zephyr/issues/49814) - Cortex-A9 fails to build cmsis due to missing core\_ca.h
- [GitHub #49805](https://github.com/zephyrproject-rtos/zephyr/issues/49805) - stm32f1: can2 & eth pin remap not working
- [GitHub #49803](https://github.com/zephyrproject-rtos/zephyr/issues/49803) - I/O APIC Driver in Zephyr makes incorrect register access.
- [GitHub #49792](https://github.com/zephyrproject-rtos/zephyr/issues/49792) - test-ci: adc-dma : frdm-k64f: dma dest addess assert
- [GitHub #49790](https://github.com/zephyrproject-rtos/zephyr/issues/49790) - Intel CAVS25: Failure in tests/boards/intel\_adsp/smoke sporadically
- [GitHub #49789](https://github.com/zephyrproject-rtos/zephyr/issues/49789) - it8xxx2\_evb: tests/crypto/tinycrypt/ test takes longer on sdk 0.15.0
- [GitHub #49786](https://github.com/zephyrproject-rtos/zephyr/issues/49786) - nsim\_em: tests: fail to run tests/kernel/timer/timer\_behavior
- [GitHub #49769](https://github.com/zephyrproject-rtos/zephyr/issues/49769) - STM32F1 CAN2 does not enable master can gating clock
- [GitHub #49766](https://github.com/zephyrproject-rtos/zephyr/issues/49766) - Document downstream module configuration recommendations
- [GitHub #49763](https://github.com/zephyrproject-rtos/zephyr/issues/49763) - nucleo\_f767zi: sample.net.gptp build fails
- [GitHub #49762](https://github.com/zephyrproject-rtos/zephyr/issues/49762) - esp32: testing.ztest.error\_hook.no\_userspace build fails due to array-bounds warnings
- [GitHub #49760](https://github.com/zephyrproject-rtos/zephyr/issues/49760) - frdm\_kl25z: sample.usb.dfu Kconfig issue causing build failure
- [GitHub #49747](https://github.com/zephyrproject-rtos/zephyr/issues/49747) - CAN2 interface on STM32F105 not working
- [GitHub #49738](https://github.com/zephyrproject-rtos/zephyr/issues/49738) - Bluetooth: Controller: Restarting periodic advertising causes crash when ADV\_SYNC\_PDU\_BACK2BACK=y
- [GitHub #49733](https://github.com/zephyrproject-rtos/zephyr/issues/49733) - Error log “Could not lookup stream by iso 0xXXXXXXXX” from unicast server if client release the stream
- [GitHub #49717](https://github.com/zephyrproject-rtos/zephyr/issues/49717) - mcumgr: Bluetooth transport fix prevents passing GATT notify status back to SMP
- [GitHub #49716](https://github.com/zephyrproject-rtos/zephyr/issues/49716) - Intel CAVS15/18: Failure in tests/arch/common/timing
- [GitHub #49715](https://github.com/zephyrproject-rtos/zephyr/issues/49715) - The function ospi\_read\_sfdp in drivers/flash/flash\_stm32\_ospi.c can corrupt the stack
- [GitHub #49714](https://github.com/zephyrproject-rtos/zephyr/issues/49714) - tests: tests/drivers/gpio/gpio\_api\_1pin failed on mec172xevb\_assy6906 in daily test
- [GitHub #49713](https://github.com/zephyrproject-rtos/zephyr/issues/49713) - frdm\_k64f: tests: failed to run tests/drivers/adc/adc\_dma/drivers.adc-dma
- [GitHub #49711](https://github.com/zephyrproject-rtos/zephyr/issues/49711) - tests/arch/common/timing/arch.common.timing.smp fails for CAVS15, 18
- [GitHub #49703](https://github.com/zephyrproject-rtos/zephyr/issues/49703) - eSPI: Add platform specific Slave to Master Virtual Wires
- [GitHub #49696](https://github.com/zephyrproject-rtos/zephyr/issues/49696) - twister: testplan: toolchain\_exclude filter is overridden by integration\_platforms
- [GitHub #49687](https://github.com/zephyrproject-rtos/zephyr/issues/49687) - West: Allow having .west folder and west.yml in the same folder
- [GitHub #49678](https://github.com/zephyrproject-rtos/zephyr/issues/49678) - Zephyr 3.2 module updates overview
- [GitHub #49677](https://github.com/zephyrproject-rtos/zephyr/issues/49677) - STM32U5 consumes more current using power management
- [GitHub #49663](https://github.com/zephyrproject-rtos/zephyr/issues/49663) - Bluetooth seems to not work randomly on target device
- [GitHub #49662](https://github.com/zephyrproject-rtos/zephyr/issues/49662) - hello world+ mcuboot is not working
- [GitHub #49661](https://github.com/zephyrproject-rtos/zephyr/issues/49661) - mcumgr: bt transport runs in system workqueue thread and can cause resource deadlock
- [GitHub #49659](https://github.com/zephyrproject-rtos/zephyr/issues/49659) - logging: LOG\_\* appends 0x0D to 0x0A
- [GitHub #49648](https://github.com/zephyrproject-rtos/zephyr/issues/49648) - tests/subsys/logging/log\_switch\_format, log\_syst build failures on CAVS
- [GitHub #49637](https://github.com/zephyrproject-rtos/zephyr/issues/49637) - CMSIS-DSP tests broken with SDK 0.15.0
- [GitHub #49631](https://github.com/zephyrproject-rtos/zephyr/issues/49631) - arch: arm: FP stack warning with GCC 12 and `CONFIG_FPU=y`
- [GitHub #49629](https://github.com/zephyrproject-rtos/zephyr/issues/49629) - Bluetooth: ISO Broadcast sample fails to send data on nRF5340
- [GitHub #49628](https://github.com/zephyrproject-rtos/zephyr/issues/49628) - Compilation fails when ASAN is used with gcc
- [GitHub #49618](https://github.com/zephyrproject-rtos/zephyr/issues/49618) - &usart2\_rx\_pd6 no more available for STM32L073RZ
- [GitHub #49616](https://github.com/zephyrproject-rtos/zephyr/issues/49616) - acrn\_ehl\_crb: The testcase tests/kernel/common failed to run.
- [GitHub #49609](https://github.com/zephyrproject-rtos/zephyr/issues/49609) - sdk: failed to run tests/subsys/logging/log\_core\_additional
- [GitHub #49607](https://github.com/zephyrproject-rtos/zephyr/issues/49607) - ADC reading on E73-2G4M04S1B and nrf52dk
- [GitHub #49606](https://github.com/zephyrproject-rtos/zephyr/issues/49606) - BeagleBone Black / AM335x Support
- [GitHub #49605](https://github.com/zephyrproject-rtos/zephyr/issues/49605) - it8xxx2\_evb: tests/kernel/timer/timer\_api test failed after commit cb041d06
- [GitHub #49602](https://github.com/zephyrproject-rtos/zephyr/issues/49602) - Bluetooth: Audio: Build error when enable CONFIG\_LIBLC3
- [GitHub #49601](https://github.com/zephyrproject-rtos/zephyr/issues/49601) - mec15xxevb\_assy6853: tests/drivers/adc/adc\_api asynchronous test failed
- [GitHub #49599](https://github.com/zephyrproject-rtos/zephyr/issues/49599) - Bluetooth: Host: Unable to pair zephyr bluetooth peripheral with Secure connection and static passkey
- [GitHub #49590](https://github.com/zephyrproject-rtos/zephyr/issues/49590) - devicetree parsing does not error out on duplicate node names
- [GitHub #49587](https://github.com/zephyrproject-rtos/zephyr/issues/49587) - cross-compile toolchain variant doesn’t working properly with multilib toolchain
- [GitHub #49586](https://github.com/zephyrproject-rtos/zephyr/issues/49586) - Json parser is incorrect with undefined parameter
- [GitHub #49578](https://github.com/zephyrproject-rtos/zephyr/issues/49578) - [RFC] Deprecate <zephyr/zephyr.h>
- [GitHub #49576](https://github.com/zephyrproject-rtos/zephyr/issues/49576) - tests: kernel: timer: timer\_behavior: kernel.timer.timer fails
- [GitHub #49572](https://github.com/zephyrproject-rtos/zephyr/issues/49572) - Reproducable builds with MCUboot signing
- [GitHub #49542](https://github.com/zephyrproject-rtos/zephyr/issues/49542) - sdk: it8xxx2\_evb cannot build the hello\_world sample after zephyr SDK upgrade to 0.15.0
- [GitHub #49540](https://github.com/zephyrproject-rtos/zephyr/issues/49540) - Bluetooth: Host: sync termination callback parameters not populated correctly when using per. adv. list feature.
- [GitHub #49531](https://github.com/zephyrproject-rtos/zephyr/issues/49531) - LE Audio: Broadcast Sink not supporting general and specific BIS codec configurations in the BASE
- [GitHub #49523](https://github.com/zephyrproject-rtos/zephyr/issues/49523) - k\_sleep in native\_posix always sleeps one tick too much
- [GitHub #49498](https://github.com/zephyrproject-rtos/zephyr/issues/49498) - net: lib: coap: update method\_from\_code() to report success/failure
- [GitHub #49493](https://github.com/zephyrproject-rtos/zephyr/issues/49493) - Bluetooth: ISO: samples/bluetooth/broadcast\_audio\_source error -122
- [GitHub #49491](https://github.com/zephyrproject-rtos/zephyr/issues/49491) - arch.interrupt test fails on ARM64 QEMU targets when compiled with GCC 12
- [GitHub #49482](https://github.com/zephyrproject-rtos/zephyr/issues/49482) - stm32g0 interrupts for usart3,4,5,6 all set to 29
- [GitHub #49471](https://github.com/zephyrproject-rtos/zephyr/issues/49471) - stm32: dietemp node generates warning
- [GitHub #49465](https://github.com/zephyrproject-rtos/zephyr/issues/49465) - Bluetooth: Controller: Periodic adv. sync. degraded performance on latest main branch
- [GitHub #49463](https://github.com/zephyrproject-rtos/zephyr/issues/49463) - STM32G0B0 errors out on stm32g0\_disable\_dead\_battery function in soc.c
- [GitHub #49462](https://github.com/zephyrproject-rtos/zephyr/issues/49462) - tests: tests/kernel/fatal/exception/ test case fail
- [GitHub #49444](https://github.com/zephyrproject-rtos/zephyr/issues/49444) - mcumgr: Outgoing packets that are larger than the transport MTU are wrongly split into different individual messages
- [GitHub #49442](https://github.com/zephyrproject-rtos/zephyr/issues/49442) - Intel CAVS25: Failure in tests/kernel/smp
- [GitHub #49440](https://github.com/zephyrproject-rtos/zephyr/issues/49440) - test-ci: mimxrt11xx: testing.ztest.base.verbose\_x and crypto.tinycryp : run failure no console output
- [GitHub #49439](https://github.com/zephyrproject-rtos/zephyr/issues/49439) - test-ci: lpcxpresso54114\_m4: libraries.devicetree.devices.requires test failure
- [GitHub #49410](https://github.com/zephyrproject-rtos/zephyr/issues/49410) - Bluetooth: Scan responses with info about periodic adv. sometimes stops being reported
- [GitHub #49406](https://github.com/zephyrproject-rtos/zephyr/issues/49406) - flash\_stm32\_ospi: OSPI wr in OPI/STR mode is for 32bit address only
- [GitHub #49360](https://github.com/zephyrproject-rtos/zephyr/issues/49360) - west boards doesn’t print boards from modules
- [GitHub #49359](https://github.com/zephyrproject-rtos/zephyr/issues/49359) - nrf5\*: crash when Bluetooth advertisements and flash write/erase are used simultaneously
- [GitHub #49350](https://github.com/zephyrproject-rtos/zephyr/issues/49350) - RFC: Add arch aligned memory Kconfig option
- [GitHub #49342](https://github.com/zephyrproject-rtos/zephyr/issues/49342) - Zephyr hci\_usb sample cannot use LE coded phy
- [GitHub #49331](https://github.com/zephyrproject-rtos/zephyr/issues/49331) - device if got the ip is “10.4.239.xxx” when join in the switchboard, then the device can not visit the outer net.
- [GitHub #49329](https://github.com/zephyrproject-rtos/zephyr/issues/49329) - twister: frdm\_k64f: test string mismatch
- [GitHub #49315](https://github.com/zephyrproject-rtos/zephyr/issues/49315) - loopback socket send from shell hangs
- [GitHub #49305](https://github.com/zephyrproject-rtos/zephyr/issues/49305) - Can’t read and write to the Nor Flash at address 0x402a8000 on RT1060
- [GitHub #49268](https://github.com/zephyrproject-rtos/zephyr/issues/49268) - tests: samples/boards/stm32/power\_mgmt/serial\_wakeup failed on mec15xxevb\_assy6853 (and several stm32 boards)
- [GitHub #49263](https://github.com/zephyrproject-rtos/zephyr/issues/49263) - ztest: tracing backend works incorrectly when new ZTEST enabled.
- [GitHub #49258](https://github.com/zephyrproject-rtos/zephyr/issues/49258) - MCUboot not loading properly due to missing ALIGN
- [GitHub #49251](https://github.com/zephyrproject-rtos/zephyr/issues/49251) - STM32 HW TIMER + DMA + DAC
- [GitHub #49203](https://github.com/zephyrproject-rtos/zephyr/issues/49203) - Intel CAVS15: Failure in tests/boards/intel\_adsp/hda,hda\_log
- [GitHub #49200](https://github.com/zephyrproject-rtos/zephyr/issues/49200) - Intel CAVS: Failure in tests/kernel/interrupt
- [GitHub #49195](https://github.com/zephyrproject-rtos/zephyr/issues/49195) - Integrate Zephyr SDK 0.15.0 to the Zephyr main CI
- [GitHub #49184](https://github.com/zephyrproject-rtos/zephyr/issues/49184) - DHCP client is not `carrier` aware
- [GitHub #49183](https://github.com/zephyrproject-rtos/zephyr/issues/49183) - Missing handling of UNKNOWN\_RSP in peripheral PHY UPDATE procedure
- [GitHub #49178](https://github.com/zephyrproject-rtos/zephyr/issues/49178) - subsys: pm: stats: typo causes build failure
- [GitHub #49177](https://github.com/zephyrproject-rtos/zephyr/issues/49177) - usb: sam0: device driver is leaking memory when interface is reset
- [GitHub #49173](https://github.com/zephyrproject-rtos/zephyr/issues/49173) - Bluetooth: empty notification received by peer after unsubscribe
- [GitHub #49169](https://github.com/zephyrproject-rtos/zephyr/issues/49169) - v2m\_musca\_s1\_ns fails to build several tfm related samples
- [GitHub #49166](https://github.com/zephyrproject-rtos/zephyr/issues/49166) - samples/drivers/flash\_shell/sample.drivers.flash.shell fails to build on a few nxp platforms
- [GitHub #49164](https://github.com/zephyrproject-rtos/zephyr/issues/49164) - samples/arch/smp/pi/sample.smp.pi fails on a number esp32 platforms
- [GitHub #49162](https://github.com/zephyrproject-rtos/zephyr/issues/49162) - Calling cache maintenance APIs from user mode threads result in a bad syscall error.
- [GitHub #49154](https://github.com/zephyrproject-rtos/zephyr/issues/49154) - SDMMC driver with STM32 U575
- [GitHub #49145](https://github.com/zephyrproject-rtos/zephyr/issues/49145) - tests: kernel: fifo: fifo\_timeout: kernel.fifo.timeout fails on nrf5340dk\_nrf5340\_cpuapp
- [GitHub #49142](https://github.com/zephyrproject-rtos/zephyr/issues/49142) - Bluetooth: Audio: MCC subscribe failure
- [GitHub #49136](https://github.com/zephyrproject-rtos/zephyr/issues/49136) - L2CAP ecred test cases failed.
- [GitHub #49134](https://github.com/zephyrproject-rtos/zephyr/issues/49134) - STM32G070RBT6 can not build with zephyr 3.1.99
- [GitHub #49119](https://github.com/zephyrproject-rtos/zephyr/issues/49119) - ARC: west: mdb runner: fix folder where MDB is run
- [GitHub #49116](https://github.com/zephyrproject-rtos/zephyr/issues/49116) - cmake cached BOARD\_DIR variable does not get overwritten
- [GitHub #49106](https://github.com/zephyrproject-rtos/zephyr/issues/49106) - Add cherryusb as a module
- [GitHub #49105](https://github.com/zephyrproject-rtos/zephyr/issues/49105) - hda\_host and hda\_link registers block size are not equal
- [GitHub #49102](https://github.com/zephyrproject-rtos/zephyr/issues/49102) - hawkbit - dns name randomly not resolved
- [GitHub #49100](https://github.com/zephyrproject-rtos/zephyr/issues/49100) - STM b\_u585i\_iot02a NOR flash and OSPI\_SPI\_MODE, erase failed
- [GitHub #49086](https://github.com/zephyrproject-rtos/zephyr/issues/49086) - twister: frdm\_k64f: twister process blocks after the flash error occurs
- [GitHub #49074](https://github.com/zephyrproject-rtos/zephyr/issues/49074) - GD32: Use clocks instead rcu-periph-clock property
- [GitHub #49073](https://github.com/zephyrproject-rtos/zephyr/issues/49073) - SOC\_FLASH\_LPC vs SOC\_FLASH\_MCUX
- [GitHub #49066](https://github.com/zephyrproject-rtos/zephyr/issues/49066) - Mcumgr img\_mgmt\_impl\_upload\_inspect() can cause unaligned memory access hard fault.
- [GitHub #49057](https://github.com/zephyrproject-rtos/zephyr/issues/49057) - USB Mass Storage Sample crashes due to overflow of Mass Storage Stack
- [GitHub #49056](https://github.com/zephyrproject-rtos/zephyr/issues/49056) - STM b\_u585i\_iot02a MCUboot crash
- [GitHub #49054](https://github.com/zephyrproject-rtos/zephyr/issues/49054) - STM32H7 apps are broken in C++ mode due to HAL include craziness
- [GitHub #49051](https://github.com/zephyrproject-rtos/zephyr/issues/49051) - Nrf52832 ADC SAMPLE cannot compile
- [GitHub #49047](https://github.com/zephyrproject-rtos/zephyr/issues/49047) - LORAWAN Devicetree sx1262 setup on rak4631\_nrf52840 board
- [GitHub #49046](https://github.com/zephyrproject-rtos/zephyr/issues/49046) - Cannot use devices behind I2C mux (TCA9548A)
- [GitHub #49044](https://github.com/zephyrproject-rtos/zephyr/issues/49044) - doc: boards: litex\_vexrisc: update with common environment variables and arty-a7-100t support
- [GitHub #49036](https://github.com/zephyrproject-rtos/zephyr/issues/49036) - soc: telink\_b91: ROM region section overlap
- [GitHub #49027](https://github.com/zephyrproject-rtos/zephyr/issues/49027) - Regulator support for gpio-leds
- [GitHub #49019](https://github.com/zephyrproject-rtos/zephyr/issues/49019) - Fix multiple issues with adxl372 driver
- [GitHub #49016](https://github.com/zephyrproject-rtos/zephyr/issues/49016) - intel\_adsp smoke test fails with CONFIG\_LOG\_MIPI\_SYST\_USE\_CATALOG=y
- [GitHub #49014](https://github.com/zephyrproject-rtos/zephyr/issues/49014) - Advertising address not updated after RPA Timeout with Extended Advertising enabled
- [GitHub #49012](https://github.com/zephyrproject-rtos/zephyr/issues/49012) - pm breaks intel dai ssp in cavs25
- [GitHub #49008](https://github.com/zephyrproject-rtos/zephyr/issues/49008) - ESP32: net\_buf\_get() FAILED
- [GitHub #49006](https://github.com/zephyrproject-rtos/zephyr/issues/49006) - tests: subsys: portability: cmsis\_rtos\_v2: portability.cmsis\_rtos\_v2 - test\_timer - does not end within 60 sec
- [GitHub #49005](https://github.com/zephyrproject-rtos/zephyr/issues/49005) - samples: tfm\_integration: tfm\_regression\_test: sample.tfm.regression\_ipc\_lvl2 no console output within 210 sec - timeout
- [GitHub #49004](https://github.com/zephyrproject-rtos/zephyr/issues/49004) - unexpected eof in qemu\_cortex and mps2
- [GitHub #49002](https://github.com/zephyrproject-rtos/zephyr/issues/49002) - tests: subsys: settings: functional: fcb: system.settings.functional.fcb fails
- [GitHub #49000](https://github.com/zephyrproject-rtos/zephyr/issues/49000) - tests: arch: arm: arm\_thread\_swap: arch.arm.swap.common.no\_optimizations USAGE FAULT
- [GitHub #48999](https://github.com/zephyrproject-rtos/zephyr/issues/48999) - tests: arch: arm: arm\_interrupt: arch.interrupt.no\_optimizations Wrong crash type got 2 expected 0
- [GitHub #48997](https://github.com/zephyrproject-rtos/zephyr/issues/48997) - tests: kernel: workq: work\_queue: kernel.workqueue fails
- [GitHub #48991](https://github.com/zephyrproject-rtos/zephyr/issues/48991) - Receiving message from pc over PCAN-USB FD
- [GitHub #48977](https://github.com/zephyrproject-rtos/zephyr/issues/48977) - kernel: mem\_protect: mimxrt11xx series build failure
- [GitHub #48967](https://github.com/zephyrproject-rtos/zephyr/issues/48967) - modem: hl7800 runtime log control API is broken
- [GitHub #48960](https://github.com/zephyrproject-rtos/zephyr/issues/48960) - coap\_packet\_parse() should return different values based on error type
- [GitHub #48951](https://github.com/zephyrproject-rtos/zephyr/issues/48951) - stm32wb55 BLE unable to connect / pair
- [GitHub #48950](https://github.com/zephyrproject-rtos/zephyr/issues/48950) - cmake: string quotes are removed from extra\_kconfig\_options.conf
- [GitHub #48937](https://github.com/zephyrproject-rtos/zephyr/issues/48937) - Compilation error when adding lwm2m client on CHIP/matter sample
- [GitHub #48921](https://github.com/zephyrproject-rtos/zephyr/issues/48921) - build system/west: Add a warning if any project repo does not match the manifest
- [GitHub #48918](https://github.com/zephyrproject-rtos/zephyr/issues/48918) - ztest: tests: add CONFIG\_ZTEST\_SHUFFLE=y to tests/subsys/logging/log\_benchmark/prj.conf cause build failure
- [GitHub #48913](https://github.com/zephyrproject-rtos/zephyr/issues/48913) - net: Add pointer member to net\_mgmt\_event\_callback struct to pass user data to the event handler.
- [GitHub #48912](https://github.com/zephyrproject-rtos/zephyr/issues/48912) - sample.drivers.flash.shell: Failed on NXP targets
- [GitHub #48911](https://github.com/zephyrproject-rtos/zephyr/issues/48911) - sample.drivers.flash.shell: Failed on atmel targets
- [GitHub #48907](https://github.com/zephyrproject-rtos/zephyr/issues/48907) - Does esp32 support BLE Mesh
- [GitHub #48897](https://github.com/zephyrproject-rtos/zephyr/issues/48897) - twister –sub-test never works
- [GitHub #48880](https://github.com/zephyrproject-rtos/zephyr/issues/48880) - BLE notifications on custom service not working anymore: <wrn> bt\_gatt: Device is not subscribed to characteristic
- [GitHub #48877](https://github.com/zephyrproject-rtos/zephyr/issues/48877) - tests: kernel: mem\_slab: mslab: kernel.memory\_slabs fails
- [GitHub #48875](https://github.com/zephyrproject-rtos/zephyr/issues/48875) - tests: kernel: context: kernel.context fails at test\_busy\_wait and Kernel panic at test\_k\_sleep
- [GitHub #48863](https://github.com/zephyrproject-rtos/zephyr/issues/48863) - hawkbit subsystem - prints garbage if debug enabled and no update pending
- [GitHub #48829](https://github.com/zephyrproject-rtos/zephyr/issues/48829) - cbprintf is broken on multiple platforms with GCC 12
- [GitHub #48828](https://github.com/zephyrproject-rtos/zephyr/issues/48828) - Clicking a link leads to “Sorry, Page Not Found”, where they ask to notify this GitHub
- [GitHub #48823](https://github.com/zephyrproject-rtos/zephyr/issues/48823) - Bluetooth: controller: llcp: limited nr. of simultaneous connections
- [GitHub #48813](https://github.com/zephyrproject-rtos/zephyr/issues/48813) - Bluetooth: bt\_conn\_disconnect randomly gives error “bt\_conn: not connected!”
- [GitHub #48812](https://github.com/zephyrproject-rtos/zephyr/issues/48812) - Bluetooth controller extended advertisement crashes in lll layer
- [GitHub #48808](https://github.com/zephyrproject-rtos/zephyr/issues/48808) - Pinctl api breaks NXP imx6sx
- [GitHub #48806](https://github.com/zephyrproject-rtos/zephyr/issues/48806) - Bluetooth: controller: conformance test instability
- [GitHub #48804](https://github.com/zephyrproject-rtos/zephyr/issues/48804) - LE Audio: Add HAP sample to Zephyr footprint tracking
- [GitHub #48801](https://github.com/zephyrproject-rtos/zephyr/issues/48801) - test: driver: wdt: wdt cases fails in LPC platform randonly
- [GitHub #48799](https://github.com/zephyrproject-rtos/zephyr/issues/48799) - Why is the command input incomplete?
- [GitHub #48780](https://github.com/zephyrproject-rtos/zephyr/issues/48780) - boards: bus devices label names should include address on bus
- [GitHub #48779](https://github.com/zephyrproject-rtos/zephyr/issues/48779) - net.socket.select: failed (qemu/mps2\_an385)
- [GitHub #48757](https://github.com/zephyrproject-rtos/zephyr/issues/48757) - Windows10 Installation: Failed to run `west update`
- [GitHub #48742](https://github.com/zephyrproject-rtos/zephyr/issues/48742) - Linking fails during build when referencing functions in `zephyr/bluetooth/crypto.h`
- [GitHub #48739](https://github.com/zephyrproject-rtos/zephyr/issues/48739) - net: tcp: Implicit MSS value is not correct
- [GitHub #48738](https://github.com/zephyrproject-rtos/zephyr/issues/48738) - dts: label: label defined in soc does not take effects in final zephyr.dts
- [GitHub #48731](https://github.com/zephyrproject-rtos/zephyr/issues/48731) - gen\_handles script fails with pwmleds handle
- [GitHub #48725](https://github.com/zephyrproject-rtos/zephyr/issues/48725) - arm\_thread\_swap: tests/arch/arm/arm\_thread\_swap/ failed on reel\_board
- [GitHub #48724](https://github.com/zephyrproject-rtos/zephyr/issues/48724) - mpu9250 driver init function register setup using the same config parameter twice.
- [GitHub #48722](https://github.com/zephyrproject-rtos/zephyr/issues/48722) - flash\_map: pointer dereferencing causes build to fail
- [GitHub #48718](https://github.com/zephyrproject-rtos/zephyr/issues/48718) - Completely disabling IP support leads to a build error when enabling IEEE 802.15.4 L2 support
- [GitHub #48715](https://github.com/zephyrproject-rtos/zephyr/issues/48715) - Enabling NET\_L2\_IEEE802154 and IEEE802154\_RAW\_MODE together breaks the build
- [GitHub #48699](https://github.com/zephyrproject-rtos/zephyr/issues/48699) - Is there a way to port the Bluetooth host stack to linux?
- [GitHub #48682](https://github.com/zephyrproject-rtos/zephyr/issues/48682) - ADC Support for STM32U575
- [GitHub #48671](https://github.com/zephyrproject-rtos/zephyr/issues/48671) - SAM V71B Initial USB Transfer Drops Data Bytes
- [GitHub #48665](https://github.com/zephyrproject-rtos/zephyr/issues/48665) - tests/usb/device: Add zassert to match zassume usage.
- [GitHub #48642](https://github.com/zephyrproject-rtos/zephyr/issues/48642) - nucleo\_l011k4 does not build
- [GitHub #48630](https://github.com/zephyrproject-rtos/zephyr/issues/48630) - Process: maintainer involvement in triaging issues
- [GitHub #48626](https://github.com/zephyrproject-rtos/zephyr/issues/48626) - jlink flasher not working with recent versions of pylink dependency
- [GitHub #48620](https://github.com/zephyrproject-rtos/zephyr/issues/48620) - LC3 External Source Code
- [GitHub #48591](https://github.com/zephyrproject-rtos/zephyr/issues/48591) - Can’t run zephyr application from SDRAM on RT1060-EVKB
- [GitHub #48585](https://github.com/zephyrproject-rtos/zephyr/issues/48585) - net: l2: ieee802154: decouple l2/l3 layers
- [GitHub #48584](https://github.com/zephyrproject-rtos/zephyr/issues/48584) - Remove netifaces Python package dependency
- [GitHub #48578](https://github.com/zephyrproject-rtos/zephyr/issues/48578) - NRF GPIO Toggle introduces race condition when multithreaded
- [GitHub #48567](https://github.com/zephyrproject-rtos/zephyr/issues/48567) - MIMXRT1060 custom board support for NXP HAL modules
- [GitHub #48547](https://github.com/zephyrproject-rtos/zephyr/issues/48547) - ztest: Incorrect display of test duration value.
- [GitHub #48541](https://github.com/zephyrproject-rtos/zephyr/issues/48541) - subsys/net/l2/ppp/fsm.c: BUS FAULT
- [GitHub #48537](https://github.com/zephyrproject-rtos/zephyr/issues/48537) - Can gpio output configuration flags be expressed in the devicetree?
- [GitHub #48534](https://github.com/zephyrproject-rtos/zephyr/issues/48534) - SMF missing events
- [GitHub #48531](https://github.com/zephyrproject-rtos/zephyr/issues/48531) - RFC: Changing the sys\_clock interface to fix race conditions.
- [GitHub #48523](https://github.com/zephyrproject-rtos/zephyr/issues/48523) - Mathematical operations in Kconfig
- [GitHub #48518](https://github.com/zephyrproject-rtos/zephyr/issues/48518) - `samples/sensor/*`: Build issue when board expose sensors defined on both I2C and SPI buses
- [GitHub #48516](https://github.com/zephyrproject-rtos/zephyr/issues/48516) - flash: sam: Build error for sam4s\_xplained
- [GitHub #48514](https://github.com/zephyrproject-rtos/zephyr/issues/48514) - bsim mesh establish\_multi.sh doesn’t send data for one of devices
- [GitHub #48512](https://github.com/zephyrproject-rtos/zephyr/issues/48512) - frdm\_k64f : failed to run tests/drivers/dma/scatter\_gather
- [GitHub #48507](https://github.com/zephyrproject-rtos/zephyr/issues/48507) - error on console usb app.overlay
- [GitHub #48501](https://github.com/zephyrproject-rtos/zephyr/issues/48501) - Usage Fault : Illegal use of EPSR , NRFSDK 2.0.0 and BLE DFU NRF52840 DK
- [GitHub #48492](https://github.com/zephyrproject-rtos/zephyr/issues/48492) - gdbstub for arc core
- [GitHub #48480](https://github.com/zephyrproject-rtos/zephyr/issues/48480) - ZTEST: duplicate symbol linker error
- [GitHub #48471](https://github.com/zephyrproject-rtos/zephyr/issues/48471) - net: tcp: Persistent timer for window probing does not implement exponential backoff
- [GitHub #48470](https://github.com/zephyrproject-rtos/zephyr/issues/48470) - Inconsistent return value of uart\_mux\_fifo\_fill when called inside/outside of an ISR
- [GitHub #48469](https://github.com/zephyrproject-rtos/zephyr/issues/48469) - [bisected] 5a850a5d06e1 is breaking some tests on ARM64
- [GitHub #48465](https://github.com/zephyrproject-rtos/zephyr/issues/48465) - net: tcp: SYN flag received after connection is established should result in connection reset
- [GitHub #48463](https://github.com/zephyrproject-rtos/zephyr/issues/48463) - Grant Triage permission level to @aurel32
- [GitHub #48460](https://github.com/zephyrproject-rtos/zephyr/issues/48460) - Provide duration of each testsuite and testcase in ztest test summary.
- [GitHub #48459](https://github.com/zephyrproject-rtos/zephyr/issues/48459) - bluetooth: host: Dangling pointer in le\_adv\_recv
- [GitHub #48447](https://github.com/zephyrproject-rtos/zephyr/issues/48447) - `hwinfo devid` does not work correctly for NXP devices using `nxp,lpc-uid` device binding
- [GitHub #48444](https://github.com/zephyrproject-rtos/zephyr/issues/48444) - Problem upgrading ncs 1.5.1 upgrade to ncs 1.9.1 failed
- [GitHub #48424](https://github.com/zephyrproject-rtos/zephyr/issues/48424) - ZTEST Framework fails when ztest\_run\_all is called multiple times
- [GitHub #48416](https://github.com/zephyrproject-rtos/zephyr/issues/48416) - samples: samples/subsys/tracing is broken for UART tracing
- [GitHub #48392](https://github.com/zephyrproject-rtos/zephyr/issues/48392) - Compiling failure watchdog sample with nucleo\_u575zi\_q
- [GitHub #48386](https://github.com/zephyrproject-rtos/zephyr/issues/48386) - twister cannot take `board@revision` as platform filter
- [GitHub #48385](https://github.com/zephyrproject-rtos/zephyr/issues/48385) - Compilation failures on Cavs 18/20/25 GCC
- [GitHub #48380](https://github.com/zephyrproject-rtos/zephyr/issues/48380) - shell: Mixing mandatory arguments w/ SHELL\_OPT\_ARG\_RAW causes crash
- [GitHub #48367](https://github.com/zephyrproject-rtos/zephyr/issues/48367) - Wrong clock assigned
- [GitHub #48343](https://github.com/zephyrproject-rtos/zephyr/issues/48343) - NVS nvs\_recover\_last\_ate() does not align data length
- [GitHub #48328](https://github.com/zephyrproject-rtos/zephyr/issues/48328) - Add API to get the nvs\_fs struct from the settings backend
- [GitHub #48321](https://github.com/zephyrproject-rtos/zephyr/issues/48321) - twister: bug in platform names verification
- [GitHub #48306](https://github.com/zephyrproject-rtos/zephyr/issues/48306) - Lwm2m\_client sample broken on native\_posix target
- [GitHub #48302](https://github.com/zephyrproject-rtos/zephyr/issues/48302) - West search for “compatible” device tree property does not expand C preprocessor macros
- [GitHub #48290](https://github.com/zephyrproject-rtos/zephyr/issues/48290) - ESP32 ble no work while enable CONFIG\_SETTINGS
- [GitHub #48282](https://github.com/zephyrproject-rtos/zephyr/issues/48282) - BT\_H4 overriding BT\_SPI=y causing build to fail - HCI Host only build SPI bus
- [GitHub #48281](https://github.com/zephyrproject-rtos/zephyr/issues/48281) - Fix github permissions for user “alevkoy”
- [GitHub #48267](https://github.com/zephyrproject-rtos/zephyr/issues/48267) - No model in devicetree\_unfixed.h :
- [GitHub #48253](https://github.com/zephyrproject-rtos/zephyr/issues/48253) - Only the first failing test is aborted and marked failed
- [GitHub #48223](https://github.com/zephyrproject-rtos/zephyr/issues/48223) - base64.c encode returns wrong count of output bytes
- [GitHub #48220](https://github.com/zephyrproject-rtos/zephyr/issues/48220) - adxl345: sensor value calculation should be wrong
- [GitHub #48216](https://github.com/zephyrproject-rtos/zephyr/issues/48216) - Running gPTP sample application on SAMe54 Xplained pro(Supports IEEE 802.1 AS gPTP clock) , PDelay Response Receipt Timeout
- [GitHub #48215](https://github.com/zephyrproject-rtos/zephyr/issues/48215) - docs: build the documentation failed due to “Could NOT find LATEX”
- [GitHub #48198](https://github.com/zephyrproject-rtos/zephyr/issues/48198) - NPCX Tachometer driver compiled despite status = “disabled”
- [GitHub #48194](https://github.com/zephyrproject-rtos/zephyr/issues/48194) - Support J-Link debugger for RaspberryPi Pico
- [GitHub #48185](https://github.com/zephyrproject-rtos/zephyr/issues/48185) - LV\_Z\_DISPLAY\_DEV\_NAME symbol has not got “parent” symbol with a type
- [GitHub #48175](https://github.com/zephyrproject-rtos/zephyr/issues/48175) - stm32 octospi flash driver
- [GitHub #48149](https://github.com/zephyrproject-rtos/zephyr/issues/48149) - Sensor Subsystem: client facing API: finding sensors
- [GitHub #48115](https://github.com/zephyrproject-rtos/zephyr/issues/48115) - tests: subsys: dfu: mcuboot\_multi: dfu.mcuboot.multiimage hangs at first test case - test\_request\_upgrade\_multi
- [GitHub #48113](https://github.com/zephyrproject-rtos/zephyr/issues/48113) - Zephyr support for STM32U5 series MCU
- [GitHub #48111](https://github.com/zephyrproject-rtos/zephyr/issues/48111) - LVGL: License agreement not found for the font arial.ttf
- [GitHub #48104](https://github.com/zephyrproject-rtos/zephyr/issues/48104) - [v 1.13 ] HID is not connecting to Linux based Master device
- [GitHub #48098](https://github.com/zephyrproject-rtos/zephyr/issues/48098) - Build error for samples/bluetooth/unicast\_audio\_server of nrf52dk-nrf52832 board
- [GitHub #48089](https://github.com/zephyrproject-rtos/zephyr/issues/48089) - AF\_PACKET sockets not filling L2 header details in `sockaddr_ll`
- [GitHub #48081](https://github.com/zephyrproject-rtos/zephyr/issues/48081) - tests/drivers/clock\_control/stm32\_clock\_configuration/stm32u5\_core not working with msis 48
- [GitHub #48071](https://github.com/zephyrproject-rtos/zephyr/issues/48071) - mec15xxevb\_assy6853: test\_i2c\_pca95xx failed
- [GitHub #48060](https://github.com/zephyrproject-rtos/zephyr/issues/48060) - Have modbus RTU Client and modbus TCP Master on the same microcontroller
- [GitHub #48058](https://github.com/zephyrproject-rtos/zephyr/issues/48058) - Reading out a GPIO pin configured as output returns invalid value.
- [GitHub #48056](https://github.com/zephyrproject-rtos/zephyr/issues/48056) - Possible null pointer dereference after k\_mutex\_lock times out
- [GitHub #48055](https://github.com/zephyrproject-rtos/zephyr/issues/48055) - samples: subsys: usb: audio: headphones\_microphone and headset - Can not get USB Device
- [GitHub #48051](https://github.com/zephyrproject-rtos/zephyr/issues/48051) - samples: logger: samples/subsys/logging/logger/sample.logger.basic failed on acrn\_ehl\_crb board
- [GitHub #48047](https://github.com/zephyrproject-rtos/zephyr/issues/48047) - Reference to obsolete files in cmake package docs
- [GitHub #48007](https://github.com/zephyrproject-rtos/zephyr/issues/48007) - tests: gpio driver fails in pin\_get\_config
- [GitHub #47991](https://github.com/zephyrproject-rtos/zephyr/issues/47991) - BLE functionality for STM32WB55 is limited with full version of BLE stack
- [GitHub #47987](https://github.com/zephyrproject-rtos/zephyr/issues/47987) - test: samples/boards/mec15xxevb\_assy6853/power\_management failed after commit 5f60164a0fc
- [GitHub #47986](https://github.com/zephyrproject-rtos/zephyr/issues/47986) - Rework of STM32 bxCAN driver filter handling required
- [GitHub #47985](https://github.com/zephyrproject-rtos/zephyr/issues/47985) - ARC wrong .debug\_frame
- [GitHub #47970](https://github.com/zephyrproject-rtos/zephyr/issues/47970) - Flash: SFDP parameter address is not correct
- [GitHub #47966](https://github.com/zephyrproject-rtos/zephyr/issues/47966) - TCP: Zero window probe packet incorrect
- [GitHub #47948](https://github.com/zephyrproject-rtos/zephyr/issues/47948) - \_kernel.threads’ always points to NULL(0x0000’0000)
- [GitHub #47942](https://github.com/zephyrproject-rtos/zephyr/issues/47942) - Mutex priority inheritance when thread holds multiple mutexes
- [GitHub #47933](https://github.com/zephyrproject-rtos/zephyr/issues/47933) - tests: subsys: logging: log\_switch\_format: logging.log\_switch\_format - test\_log\_switch\_format\_success\_case - Assertion failed
- [GitHub #47930](https://github.com/zephyrproject-rtos/zephyr/issues/47930) - tests: arch: arm: arm\_interrupt: arch.interrupt.no\_optimizations - Data Access Violation - MPU Fault
- [GitHub #47929](https://github.com/zephyrproject-rtos/zephyr/issues/47929) - tests: arch: arm: arm\_thread\_swap: arch.arm.swap.common.no\_optimizations - Data Access Violation - MPU Fault
- [GitHub #47925](https://github.com/zephyrproject-rtos/zephyr/issues/47925) - Asynchronous UART API (DMA) not working like expected on nrf52840
- [GitHub #47921](https://github.com/zephyrproject-rtos/zephyr/issues/47921) - tests: pin\_get\_config failed on it8xxx2\_evb
- [GitHub #47904](https://github.com/zephyrproject-rtos/zephyr/issues/47904) - drivers: can: loopback driver only compares loopback frames against CAN IDs in installed filters
- [GitHub #47902](https://github.com/zephyrproject-rtos/zephyr/issues/47902) - drivers: can: mcux: flexcan: failure to handle RTR frames correctly
- [GitHub #47895](https://github.com/zephyrproject-rtos/zephyr/issues/47895) - samples: smp\_svr missing CONFIG\_MULTITHREADING=y dependency
- [GitHub #47860](https://github.com/zephyrproject-rtos/zephyr/issues/47860) - Bluetooth: shell: bt init sync enables Bluetooth asynchronously
- [GitHub #47857](https://github.com/zephyrproject-rtos/zephyr/issues/47857) - Zephyr USB-RNDIS
- [GitHub #47855](https://github.com/zephyrproject-rtos/zephyr/issues/47855) - tests: arch: arm: fpu: arch.arm.swap.common.fpu\_sharing.no\_optimizations - Data Access Violation - MPU Fault
- [GitHub #47854](https://github.com/zephyrproject-rtos/zephyr/issues/47854) - Multiple blinking LED’s cannot be turned off
- [GitHub #47852](https://github.com/zephyrproject-rtos/zephyr/issues/47852) - samples: boards: nrf: s2ram No valid output on console
- [GitHub #47847](https://github.com/zephyrproject-rtos/zephyr/issues/47847) - How to PM change pm\_state
- [GitHub #47833](https://github.com/zephyrproject-rtos/zephyr/issues/47833) - Intel CAVS: cavstool.py fails to extract complete log from winstream buffer when logging is frequent
- [GitHub #47830](https://github.com/zephyrproject-rtos/zephyr/issues/47830) - Intel CAVS: Build failure due to #47713 PR
- [GitHub #47825](https://github.com/zephyrproject-rtos/zephyr/issues/47825) - qemu\_cortex\_a53\_smp: tests/kernel/profiling/profiling\_api failed
- [GitHub #47822](https://github.com/zephyrproject-rtos/zephyr/issues/47822) - Stack Overflow when calling spi at an interrupt on STM32l4
- [GitHub #47783](https://github.com/zephyrproject-rtos/zephyr/issues/47783) - warning: attempt to assign the value ‘y’ to the undefined symbol UART\_0\_NRF\_FLOW\_CONTROL
- [GitHub #47781](https://github.com/zephyrproject-rtos/zephyr/issues/47781) - MCUbootloader with b\_u585i\_iot02a (stm32u585) boot error
- [GitHub #47780](https://github.com/zephyrproject-rtos/zephyr/issues/47780) - WS2812 driver not work on nRF52833DK
- [GitHub #47762](https://github.com/zephyrproject-rtos/zephyr/issues/47762) - Some github users in the MAINTAINERS file are missing permissions
- [GitHub #47751](https://github.com/zephyrproject-rtos/zephyr/issues/47751) - soc/arm/common/cortex\_m doesn’t work for out-of-tree socs
- [GitHub #47742](https://github.com/zephyrproject-rtos/zephyr/issues/47742) - NXP LPC MCAN driver front-end lacks pinctrl support
- [GitHub #47734](https://github.com/zephyrproject-rtos/zephyr/issues/47734) - tests/posix/eventfd/ : failed on both nucleo\_f103rb and nucleo\_l073rz with 20K RAM only
- [GitHub #47731](https://github.com/zephyrproject-rtos/zephyr/issues/47731) - JESD216 fails to read SFDP on STM32 targets
- [GitHub #47725](https://github.com/zephyrproject-rtos/zephyr/issues/47725) - qemu\_arc: tests/kernel/context/ failed when migrating to new ztest API
- [GitHub #47719](https://github.com/zephyrproject-rtos/zephyr/issues/47719) - Configure-time library dependency problem
- [GitHub #47714](https://github.com/zephyrproject-rtos/zephyr/issues/47714) - test: tests/lib/sprintf/ build fail
- [GitHub #47702](https://github.com/zephyrproject-rtos/zephyr/issues/47702) - twister: regression : Failures are counted as errors
- [GitHub #47696](https://github.com/zephyrproject-rtos/zephyr/issues/47696) - tests: arch: arm: arm\_thread\_swap: regression since use of new ztest API
- [GitHub #47682](https://github.com/zephyrproject-rtos/zephyr/issues/47682) - bt\_gatt\_unsubscribe creates write request to CCC and then cancels it
- [GitHub #47676](https://github.com/zephyrproject-rtos/zephyr/issues/47676) - bt\_data\_parse is destructive without warning
- [GitHub #47652](https://github.com/zephyrproject-rtos/zephyr/issues/47652) - The client-server based cavstool.py might be stuck when the ROM is not start
- [GitHub #47649](https://github.com/zephyrproject-rtos/zephyr/issues/47649) - ATT Notification buffer not released after reconnection
- [GitHub #47641](https://github.com/zephyrproject-rtos/zephyr/issues/47641) - Poor Ethernet Performance using NXP Enet MCUX Driver
- [GitHub #47640](https://github.com/zephyrproject-rtos/zephyr/issues/47640) - Zephyr and caches: a difficult love story.
- [GitHub #47613](https://github.com/zephyrproject-rtos/zephyr/issues/47613) - Samples / Tests without a testcase.yaml or sample.yaml
- [GitHub #47683](https://github.com/zephyrproject-rtos/zephyr/issues/47683) - TCP Connected Change the window size to 1/3/ff fail
- [GitHub #47609](https://github.com/zephyrproject-rtos/zephyr/issues/47609) - posix: pthread: descriptor leak with pthread\_join
- [GitHub #47606](https://github.com/zephyrproject-rtos/zephyr/issues/47606) - nvs\_read return value is not correct
- [GitHub #47592](https://github.com/zephyrproject-rtos/zephyr/issues/47592) - test: tests/drivers/gpio/gpio\_basic\_api failed after commit 2a8e3fe
- [GitHub #47588](https://github.com/zephyrproject-rtos/zephyr/issues/47588) - tests: sprintf: zero-length gnu\_printf format string
- [GitHub #47580](https://github.com/zephyrproject-rtos/zephyr/issues/47580) - https connect failing with all the samples (qemu\_x86 & mbedtls)
- [GitHub #47576](https://github.com/zephyrproject-rtos/zephyr/issues/47576) - undefined reference to `__device_dts_ord_20` When building with board hifive\_unmatched on flash\_shell samples
- [GitHub #47568](https://github.com/zephyrproject-rtos/zephyr/issues/47568) - uart\_mcux\_lpuart driver activates the noise error interrupt but does not clear the noise error flag
- [GitHub #47556](https://github.com/zephyrproject-rtos/zephyr/issues/47556) - sample: logging: Builds failing for samples/subsys/logging/syst
- [GitHub #47551](https://github.com/zephyrproject-rtos/zephyr/issues/47551) - Enabling CONFIG\_OPENTHREAD\_SRP\_CLIENT on NRF52840 dongle board leads to MBED compilation errors.
- [GitHub #47546](https://github.com/zephyrproject-rtos/zephyr/issues/47546) - Revert [https://github.com/zephyrproject-rtos/zephyr/pull/47511](https://github.com/zephyrproject-rtos/zephyr/pull/47511)
- [GitHub #47520](https://github.com/zephyrproject-rtos/zephyr/issues/47520) - Support for sub-ghz channels in at86rf2xx radio driver
- [GitHub #47512](https://github.com/zephyrproject-rtos/zephyr/issues/47512) - up\_squared: issues of EFI console feature
- [GitHub #47508](https://github.com/zephyrproject-rtos/zephyr/issues/47508) - tests: arch: the xtensa\_asm2 test is broken
- [GitHub #47483](https://github.com/zephyrproject-rtos/zephyr/issues/47483) - PPP + GSM MUX doesn’t work with Thales PLS83-W modem
- [GitHub #47476](https://github.com/zephyrproject-rtos/zephyr/issues/47476) - SX127x LoRaWAN - Failing on Boot - Missing Read/Write functions?
- [GitHub #47461](https://github.com/zephyrproject-rtos/zephyr/issues/47461) - Unable to build the flash\_shell samples with board cc1352r1\_launchxl
- [GitHub #47458](https://github.com/zephyrproject-rtos/zephyr/issues/47458) - BQ274XX Sensors Driver - Fails with CONFIG\_BQ274XX\_LAZY\_CONFIGURE
- [GitHub #47445](https://github.com/zephyrproject-rtos/zephyr/issues/47445) - USB OTG FS controller support on STM32F413 broken
- [GitHub #47428](https://github.com/zephyrproject-rtos/zephyr/issues/47428) - SRAM increase in Bluetooth [samples: bbc\_microbit: pong fails to build]
- [GitHub #47426](https://github.com/zephyrproject-rtos/zephyr/issues/47426) - ZTEST\_USER tests being skipped on systems without userspace support
- [GitHub #47420](https://github.com/zephyrproject-rtos/zephyr/issues/47420) - Tests: unittest with new ZTEST API
- [GitHub #47409](https://github.com/zephyrproject-rtos/zephyr/issues/47409) - LE Audio: Read PACS available contexts as unicast client
- [GitHub #47407](https://github.com/zephyrproject-rtos/zephyr/issues/47407) - stm32l5: tfm: Build error on tests/arch/arm/arm\_thread\_swap\_tz
- [GitHub #47379](https://github.com/zephyrproject-rtos/zephyr/issues/47379) - Crypto sample fail to build with cryp node in .dts for STM32u5 (error: unknown type name ‘CRYP\_HandleTypeDef’ etc.)
- [GitHub #47356](https://github.com/zephyrproject-rtos/zephyr/issues/47356) - cpp: global static object initialisation may fail for MMU and MPU platforms
- [GitHub #47330](https://github.com/zephyrproject-rtos/zephyr/issues/47330) - ARM Cortex-R52 doesn’t have SPSR\_hyp
- [GitHub #47326](https://github.com/zephyrproject-rtos/zephyr/issues/47326) - drivers: WINC1500: issues with buffer allocation when using sockets
- [GitHub #47323](https://github.com/zephyrproject-rtos/zephyr/issues/47323) - STM32WL LoRa SoC stuck at initialization due to SPI transmit buffer not emptying
- [GitHub #47307](https://github.com/zephyrproject-rtos/zephyr/issues/47307) - tests: kernel: fatal: exception: build failure on multiple platforms
- [GitHub #47301](https://github.com/zephyrproject-rtos/zephyr/issues/47301) - Module request: Lua
- [GitHub #47300](https://github.com/zephyrproject-rtos/zephyr/issues/47300) - Intel CAVS: Failure in tests/lib/spsc\_pbuf
- [GitHub #47292](https://github.com/zephyrproject-rtos/zephyr/issues/47292) - it8xxx2\_evb: many test cases failed probably due to the west update
- [GitHub #47288](https://github.com/zephyrproject-rtos/zephyr/issues/47288) - tests: posix: increase coverage for picolibc
- [GitHub #47275](https://github.com/zephyrproject-rtos/zephyr/issues/47275) - builds are broken with gnuarmemb toolchain, due to picolibc tests/configuration
- [GitHub #47273](https://github.com/zephyrproject-rtos/zephyr/issues/47273) - linker script: Vector table regression due to change in definition of \_vector\_end
- [GitHub #47272](https://github.com/zephyrproject-rtos/zephyr/issues/47272) - nrf51\_ble400: onboard chip should be updated to nRF51822\_QFAC in dts
- [GitHub #47248](https://github.com/zephyrproject-rtos/zephyr/issues/47248) - LE Audio: Crash on originating call.
- [GitHub #47240](https://github.com/zephyrproject-rtos/zephyr/issues/47240) - net: tcp: Correctly handle overlapped TCP retransmits
- [GitHub #47238](https://github.com/zephyrproject-rtos/zephyr/issues/47238) - SD Card init issue when CONFIG\_SPEED\_OPTIMIZATIONS=y
- [GitHub #47232](https://github.com/zephyrproject-rtos/zephyr/issues/47232) - Please add STM32F412RX
- [GitHub #47222](https://github.com/zephyrproject-rtos/zephyr/issues/47222) - zephyr doc: Unable to open pdf document version 3.1.0
- [GitHub #47220](https://github.com/zephyrproject-rtos/zephyr/issues/47220) - Twister: Skipping `*.cpp` files
- [GitHub #47204](https://github.com/zephyrproject-rtos/zephyr/issues/47204) - CAN filter with RTR mask causes infinite loop in MCAN driver on filtered message arrival
- [GitHub #47197](https://github.com/zephyrproject-rtos/zephyr/issues/47197) - BLE latency decreasing and increasing over time (possibly GPIO issue)
- [GitHub #47146](https://github.com/zephyrproject-rtos/zephyr/issues/47146) - STM32F103: USB clock prescaler isn’t set during USB initialisation
- [GitHub #47127](https://github.com/zephyrproject-rtos/zephyr/issues/47127) - twister : frdm\_k64f ：Non-existent tests appear and fail on tests/lib/cmsis\_dsp/transform
- [GitHub #47126](https://github.com/zephyrproject-rtos/zephyr/issues/47126) - New ztest API: build failure on qemu\_cortex\_m3 when CONFIG\_CMAKE\_LINKER\_GENERATOR=y
- [GitHub #47119](https://github.com/zephyrproject-rtos/zephyr/issues/47119) - ADC\_DT\_SPEC\_GET not working for channels >= 10
- [GitHub #47114](https://github.com/zephyrproject-rtos/zephyr/issues/47114) - `check_compliance.py` crash on Ubuntu 22.04
- [GitHub #47105](https://github.com/zephyrproject-rtos/zephyr/issues/47105) - drivers: clock\_control: stm32 common: wrong PLLCLK rate returned
- [GitHub #47104](https://github.com/zephyrproject-rtos/zephyr/issues/47104) - Bluetooth: Controller: Errors in implementation of tx buffer queue mechanism
- [GitHub #47101](https://github.com/zephyrproject-rtos/zephyr/issues/47101) - drivers: clock\_control: stm32 common: PLL\_Q divider not converted to reg val
- [GitHub #47095](https://github.com/zephyrproject-rtos/zephyr/issues/47095) - ppp network interface - MQTT/TCP communication
- [GitHub #47082](https://github.com/zephyrproject-rtos/zephyr/issues/47082) - drivers: modem: AT commands sent before OK from previous is received
- [GitHub #47081](https://github.com/zephyrproject-rtos/zephyr/issues/47081) - on x86, k\_is\_in\_isr() returns false in execption context
- [GitHub #47077](https://github.com/zephyrproject-rtos/zephyr/issues/47077) - Intel CAVS: tests/subsys/logging/log\_switch\_format/ are skipped as no result captured
- [GitHub #47072](https://github.com/zephyrproject-rtos/zephyr/issues/47072) - ZTEST Docs Page
- [GitHub #47062](https://github.com/zephyrproject-rtos/zephyr/issues/47062) - dt-bindings: clock: STM32G4 device clk sources selection helper macros don’t match the SOCs CCIPR register
- [GitHub #47061](https://github.com/zephyrproject-rtos/zephyr/issues/47061) - pipes: Usage between task and ISR results in corrupted pipe state
- [GitHub #47054](https://github.com/zephyrproject-rtos/zephyr/issues/47054) - it8xxx2\_evb: flash fail in daily test
- [GitHub #47051](https://github.com/zephyrproject-rtos/zephyr/issues/47051) - drivers: usb: stm32: usb\_write size on bulk transfer problematic
- [GitHub #47046](https://github.com/zephyrproject-rtos/zephyr/issues/47046) - samples/net/sockets/packet: Bus fault
- [GitHub #47030](https://github.com/zephyrproject-rtos/zephyr/issues/47030) - drivers: gpio: nrfx: return -ENOTSUP rather than -EIO for misconfigurations
- [GitHub #47025](https://github.com/zephyrproject-rtos/zephyr/issues/47025) - mimxrt1050\_evk: reset cause
- [GitHub #47021](https://github.com/zephyrproject-rtos/zephyr/issues/47021) - Integrate Würth Elektronik Sensors SDK code for use in sensor drivers
- [GitHub #47010](https://github.com/zephyrproject-rtos/zephyr/issues/47010) - ACRN: failed to run the test case tests/drivers/coredump/coredump\_api
- [GitHub #46988](https://github.com/zephyrproject-rtos/zephyr/issues/46988) - samples: net: openthread: coprocessor: RCP is missing required capabilities: tx-security tx-timing
- [GitHub #46985](https://github.com/zephyrproject-rtos/zephyr/issues/46985) - uOSCORE/uEDHOC integration as a Zephyr module
- [GitHub #46962](https://github.com/zephyrproject-rtos/zephyr/issues/46962) - Regression in apds9960 driver
- [GitHub #46954](https://github.com/zephyrproject-rtos/zephyr/issues/46954) - Binaries found in hal\_nxp without conspicuous license information
- [GitHub #46935](https://github.com/zephyrproject-rtos/zephyr/issues/46935) - Not printk/log output working
- [GitHub #46931](https://github.com/zephyrproject-rtos/zephyr/issues/46931) - flash\_stm32\_ospi.c: Unable to erase flash partition using flash\_map API
- [GitHub #46928](https://github.com/zephyrproject-rtos/zephyr/issues/46928) - drivers: modem: gsm\_ppp: support hardware flow control
- [GitHub #46925](https://github.com/zephyrproject-rtos/zephyr/issues/46925) - Intel CAVS: tests/lib/mem\_block/ failed, caused by too frequent log output.
- [GitHub #46917](https://github.com/zephyrproject-rtos/zephyr/issues/46917) - frdm\_k64f : failed to run tests/drivers/gpio/gpio\_get\_direction
- [GitHub #46901](https://github.com/zephyrproject-rtos/zephyr/issues/46901) - RFC: I3C I2C API
- [GitHub #46887](https://github.com/zephyrproject-rtos/zephyr/issues/46887) - Automatically organize BLE EIR/AD data into a struct instead of providing it in a simple\_network\_buffer.
- [GitHub #46865](https://github.com/zephyrproject-rtos/zephyr/issues/46865) - Intel CAVS: Support for different ports for client / server
- [GitHub #46864](https://github.com/zephyrproject-rtos/zephyr/issues/46864) - Intel CAVS: cavstool\_client.py sporadically fails
- [GitHub #46847](https://github.com/zephyrproject-rtos/zephyr/issues/46847) - STOP2 Mode on Nucleo-WL55JC1 not accessed
- [GitHub #46829](https://github.com/zephyrproject-rtos/zephyr/issues/46829) - LE Audio: Avoid multiple calls to `bt_iso_chan_connect` in parallel
- [GitHub #46822](https://github.com/zephyrproject-rtos/zephyr/issues/46822) - L2CAP disconnected packet timing in ecred reconf function
- [GitHub #46807](https://github.com/zephyrproject-rtos/zephyr/issues/46807) - lib: posix: semaphore: use consistent timebase in sem\_timedwait
- [GitHub #46801](https://github.com/zephyrproject-rtos/zephyr/issues/46801) - Revisit modules and inclusion in the default manifest
- [GitHub #46799](https://github.com/zephyrproject-rtos/zephyr/issues/46799) - IRQ vector table: how to support different formats
- [GitHub #46798](https://github.com/zephyrproject-rtos/zephyr/issues/46798) - Zephyr does not store a new IRK when another device re-bonds with a Zephyr device
- [GitHub #46797](https://github.com/zephyrproject-rtos/zephyr/issues/46797) - UART Asynchronous API continuous data receiving weird behaviour
- [GitHub #46796](https://github.com/zephyrproject-rtos/zephyr/issues/46796) - IRQ vector table
- [GitHub #46793](https://github.com/zephyrproject-rtos/zephyr/issues/46793) - tests: posix: use new ztest api
- [GitHub #46765](https://github.com/zephyrproject-rtos/zephyr/issues/46765) - test-ci: kernel.timer: test\_timer\_remaining asserts
- [GitHub #46763](https://github.com/zephyrproject-rtos/zephyr/issues/46763) - LE Audio: Unicast Audio read PAC location
- [GitHub #46761](https://github.com/zephyrproject-rtos/zephyr/issues/46761) - logging: tagged arguments feature does not work with char arrays in C++
- [GitHub #46757](https://github.com/zephyrproject-rtos/zephyr/issues/46757) - Bluetooth: Controller: Missing validation of unsupported PHY when performing PHY update
- [GitHub #46749](https://github.com/zephyrproject-rtos/zephyr/issues/46749) - mbox: wrong syscall check
- [GitHub #46743](https://github.com/zephyrproject-rtos/zephyr/issues/46743) - samples: net: civetweb: websocket\_server
- [GitHub #46740](https://github.com/zephyrproject-rtos/zephyr/issues/46740) - stm32 flash ospi fails on stm32l5 and stm32u5 disco
- [GitHub #46734](https://github.com/zephyrproject-rtos/zephyr/issues/46734) - drivers/disk: sdmmc: Doesn’t compile for STM32F4
- [GitHub #46733](https://github.com/zephyrproject-rtos/zephyr/issues/46733) - ipc\_rpmsg\_static\_vrings creates unaligned TX virtqueues
- [GitHub #46728](https://github.com/zephyrproject-rtos/zephyr/issues/46728) - mcumgr: rt1060: upload an image over the shell does not work
- [GitHub #46725](https://github.com/zephyrproject-rtos/zephyr/issues/46725) - stm32: QSPI flash driver have a broken priority configuration
- [GitHub #46721](https://github.com/zephyrproject-rtos/zephyr/issues/46721) - HAL module request: hal\_renesas
- [GitHub #46706](https://github.com/zephyrproject-rtos/zephyr/issues/46706) - add missing checks for segment number
- [GitHub #46705](https://github.com/zephyrproject-rtos/zephyr/issues/46705) - Check buffer size in rx
- [GitHub #46698](https://github.com/zephyrproject-rtos/zephyr/issues/46698) - sm351 driver faults when using global thread
- [GitHub #46697](https://github.com/zephyrproject-rtos/zephyr/issues/46697) - Missed interrupts in NXP RT685 GPIO driver
- [GitHub #46694](https://github.com/zephyrproject-rtos/zephyr/issues/46694) - Bluetooth: controller: LLCP: missing release of tx nodes on disconnect when tx data paused
- [GitHub #46692](https://github.com/zephyrproject-rtos/zephyr/issues/46692) - Bluetooth: controller: LLCP: reduced throughput
- [GitHub #46689](https://github.com/zephyrproject-rtos/zephyr/issues/46689) - Missing handling of DISK\_IOCTL\_CTRL\_SYNC in sdmmc\_ioctl
- [GitHub #46684](https://github.com/zephyrproject-rtos/zephyr/issues/46684) - ethernet: w5500: driver will be stack overflowed when reading the invalid(corrupt) packet length
- [GitHub #46656](https://github.com/zephyrproject-rtos/zephyr/issues/46656) - Scheduling timing issue
- [GitHub #46650](https://github.com/zephyrproject-rtos/zephyr/issues/46650) - qemu\_x86: shell does not work with tip of main
- [GitHub #46645](https://github.com/zephyrproject-rtos/zephyr/issues/46645) - NRFX samples use deprecated API
- [GitHub #46641](https://github.com/zephyrproject-rtos/zephyr/issues/46641) - tests : kernel: context test\_kernel\_cpu\_idle fails on nucleo\_f091 board
- [GitHub #46635](https://github.com/zephyrproject-rtos/zephyr/issues/46635) - tests: subsys: modbus: testcase hang up when running by twister
- [GitHub #46632](https://github.com/zephyrproject-rtos/zephyr/issues/46632) - Intel CAVS: Assertion failures in tests/boards/intel\_adsp/hda
- [GitHub #46626](https://github.com/zephyrproject-rtos/zephyr/issues/46626) - USB CDC ACM Sample Application build fail with stm32\_mini\_dev\_blue board
- [GitHub #46623](https://github.com/zephyrproject-rtos/zephyr/issues/46623) - Promote user “tari” to traige permission level
- [GitHub #46621](https://github.com/zephyrproject-rtos/zephyr/issues/46621) - drivers: i2c: Infinite recursion in driver unregister function
- [GitHub #46602](https://github.com/zephyrproject-rtos/zephyr/issues/46602) - BLE paring/connection issue on Windows (Zephyr 3.1.0)
- [GitHub #46594](https://github.com/zephyrproject-rtos/zephyr/issues/46594) - openthread net\_mgmt\_event\_callback expects event info.
- [GitHub #46582](https://github.com/zephyrproject-rtos/zephyr/issues/46582) - LE Audio: PACS notify warns about failure when not connected
- [GitHub #46580](https://github.com/zephyrproject-rtos/zephyr/issues/46580) - Suggestion for additional configuration of `twister --coverage` gcovr formats
- [GitHub #46573](https://github.com/zephyrproject-rtos/zephyr/issues/46573) - raspberry pi pico always in mass storage mode
- [GitHub #46570](https://github.com/zephyrproject-rtos/zephyr/issues/46570) - Compiler warning when enabling userspace, sockets and speed optimization
- [GitHub #46558](https://github.com/zephyrproject-rtos/zephyr/issues/46558) - Bluetooth: Controller: Crash on bt\_le\_adv\_start() when using CONFIG\_BT\_CTLR\_ADVANCED\_FEATURES
- [GitHub #46556](https://github.com/zephyrproject-rtos/zephyr/issues/46556) - Kconfig search webpage no longer shows all flags
- [GitHub #46555](https://github.com/zephyrproject-rtos/zephyr/issues/46555) - test: samples/drivers/adc twister result wrong
- [GitHub #46541](https://github.com/zephyrproject-rtos/zephyr/issues/46541) - Duplicate IDs used for different Systemview trace events
- [GitHub #46525](https://github.com/zephyrproject-rtos/zephyr/issues/46525) - PWM of it8xxx2
- [GitHub #46521](https://github.com/zephyrproject-rtos/zephyr/issues/46521) - ‘\_\_device\_dts\_ord\_\_\_BUS\_ORD’ undeclared here (not in a function); did you mean ‘\_\_device\_dts\_ord\_94’?
- [GitHub #46519](https://github.com/zephyrproject-rtos/zephyr/issues/46519) - STM32F4 CAN2 peripheral not working
- [GitHub #46510](https://github.com/zephyrproject-rtos/zephyr/issues/46510) - bluetooth: controller: llcp: set refactored LLCP as default
- [GitHub #46500](https://github.com/zephyrproject-rtos/zephyr/issues/46500) - Removal of logging v1
- [GitHub #46497](https://github.com/zephyrproject-rtos/zephyr/issues/46497) - Modbus: Add support for FC03 without floating-point extension as client
- [GitHub #46493](https://github.com/zephyrproject-rtos/zephyr/issues/46493) - Ethernet W5500 driver fails initialization with latest change - revert needed
- [GitHub #46483](https://github.com/zephyrproject-rtos/zephyr/issues/46483) - Update RISC-V ISA configs
- [GitHub #46478](https://github.com/zephyrproject-rtos/zephyr/issues/46478) - mimxrt1050\_evk\_qspi freeze when erasing flash
- [GitHub #46474](https://github.com/zephyrproject-rtos/zephyr/issues/46474) - LE Audio: Add seq\_num and TS to bt\_audio\_send
- [GitHub #46470](https://github.com/zephyrproject-rtos/zephyr/issues/46470) - twister : retry failed parameter is not valid
- [GitHub #46464](https://github.com/zephyrproject-rtos/zephyr/issues/46464) - frdm\_k64f : sudden failure to flash program
- [GitHub #46459](https://github.com/zephyrproject-rtos/zephyr/issues/46459) - Test framework incorrectly uses c++ keyword `this`
- [GitHub #46453](https://github.com/zephyrproject-rtos/zephyr/issues/46453) - nRF52840 PWM with pinctrl - Unable to build samples/basic/blinky\_pwm
- [GitHub #46446](https://github.com/zephyrproject-rtos/zephyr/issues/46446) - lvgl: Using sw\_rotate with SSD1306 shield causes memory fault
- [GitHub #46444](https://github.com/zephyrproject-rtos/zephyr/issues/46444) - Proposal to integrate Cadence QSPI driver from Trusted Firmware-A
- [GitHub #46434](https://github.com/zephyrproject-rtos/zephyr/issues/46434) - ESP32-C3 UART1 broken since introduction of pinctrl
- [GitHub #46426](https://github.com/zephyrproject-rtos/zephyr/issues/46426) - Intel CAVS: Assertion failures on tests/boards/intel\_adsp/smoke
- [GitHub #46422](https://github.com/zephyrproject-rtos/zephyr/issues/46422) - SDK version 14.2 increases image size significantly
- [GitHub #46414](https://github.com/zephyrproject-rtos/zephyr/issues/46414) - mcuboot: rt1060: confirmed image causes usage fault
- [GitHub #46413](https://github.com/zephyrproject-rtos/zephyr/issues/46413) - No multicast reception on IMX1064
- [GitHub #46410](https://github.com/zephyrproject-rtos/zephyr/issues/46410) - Add devicetree binding for `zephyr,sdmmc-disk`
- [GitHub #46400](https://github.com/zephyrproject-rtos/zephyr/issues/46400) - STM32WB BLE HCI interface problem.
- [GitHub #46398](https://github.com/zephyrproject-rtos/zephyr/issues/46398) - `mem_protect/mem_map` is failing on `qemu_x86_tiny` when userspace is enabled
- [GitHub #46383](https://github.com/zephyrproject-rtos/zephyr/issues/46383) - fatal error: sys/cbprintf\_enums.h: No such file or directory
- [GitHub #46382](https://github.com/zephyrproject-rtos/zephyr/issues/46382) - twister -x / –extra-args escaping quotes issue with CONFIG\_COMPILER\_OPTIONS
- [GitHub #46378](https://github.com/zephyrproject-rtos/zephyr/issues/46378) - CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC affects app code speed with tickless kernel
- [GitHub #46372](https://github.com/zephyrproject-rtos/zephyr/issues/46372) - Intel-ADSP: sporadic core boot
- [GitHub #46369](https://github.com/zephyrproject-rtos/zephyr/issues/46369) - LE Audio: Bidirectional stream is not created
- [GitHub #46368](https://github.com/zephyrproject-rtos/zephyr/issues/46368) - twister : frdm\_k64f ：the test case tests/subsys/logging/log\_switch\_format/logger.syst.v2.immediate/ blocks
- [GitHub #46366](https://github.com/zephyrproject-rtos/zephyr/issues/46366) - test\_thread\_stats\_usage fail on arm64 fvp
- [GitHub #46363](https://github.com/zephyrproject-rtos/zephyr/issues/46363) - Initial Setup: Ubuntu 20.04: ensurepip is not available
- [GitHub #46355](https://github.com/zephyrproject-rtos/zephyr/issues/46355) - Sample wifi\_station not building for esp32: No SOURCES given to Zephyr library: drivers\_\_ethernet
- [GitHub #46350](https://github.com/zephyrproject-rtos/zephyr/issues/46350) - net: tcp: When the first FIN message is lost, the connection does not properly close
- [GitHub #46347](https://github.com/zephyrproject-rtos/zephyr/issues/46347) - MCUMGR\_SMP\_BT: system workqueue blocked during execution of shell commands
- [GitHub #46346](https://github.com/zephyrproject-rtos/zephyr/issues/46346) - LE Audio: Fatal crash when sending Audio data
- [GitHub #46345](https://github.com/zephyrproject-rtos/zephyr/issues/46345) - get\_maintainer.py incorrectly invoked by Github?
- [GitHub #46341](https://github.com/zephyrproject-rtos/zephyr/issues/46341) - Zephyr scheduler lock: add selective locking up to a given priority ceiling
- [GitHub #46335](https://github.com/zephyrproject-rtos/zephyr/issues/46335) - For ESP32, initialization of static object during declaration with derived class type doesn’t work.
- [GitHub #46326](https://github.com/zephyrproject-rtos/zephyr/issues/46326) - Async UART for STM32 U5 support
- [GitHub #46325](https://github.com/zephyrproject-rtos/zephyr/issues/46325) - ESP32 strcmp error while enable MCUBOOT and NEWLIB\_LIBC
- [GitHub #46324](https://github.com/zephyrproject-rtos/zephyr/issues/46324) - it8xxx2\_evb: tests/kernel/sched/schedule\_api fail due to k\_sleep(K\_MSEC(100)) not correct
- [GitHub #46322](https://github.com/zephyrproject-rtos/zephyr/issues/46322) - Time units in shtcx sensor
- [GitHub #46312](https://github.com/zephyrproject-rtos/zephyr/issues/46312) - sample: bluetooth: ipsp - TCP not running over IPSP
- [GitHub #46286](https://github.com/zephyrproject-rtos/zephyr/issues/46286) - python-devicetree tox run fails
- [GitHub #46285](https://github.com/zephyrproject-rtos/zephyr/issues/46285) - nrf\_qspi\_nor: Inconsistent state of HOLD and WP for QSPI command execution causes hang on startup for some flash chips
- [GitHub #46284](https://github.com/zephyrproject-rtos/zephyr/issues/46284) - ring buffer in item mode crashes
- [GitHub #46277](https://github.com/zephyrproject-rtos/zephyr/issues/46277) - IMX8MM: Running fail a zephyr sample in the imx8mm
- [GitHub #46269](https://github.com/zephyrproject-rtos/zephyr/issues/46269) - docs: include/zephyr/net/socket.h is not documented anywhere
- [GitHub #46267](https://github.com/zephyrproject-rtos/zephyr/issues/46267) - docs: include/zephyr/net/http\_client.h is not documented anywhere
- [GitHub #46266](https://github.com/zephyrproject-rtos/zephyr/issues/46266) - zephyr,sdmmc-disk compatible lacks a binding
- [GitHub #46263](https://github.com/zephyrproject-rtos/zephyr/issues/46263) - Regulator Control
- [GitHub #46255](https://github.com/zephyrproject-rtos/zephyr/issues/46255) - imxrt1010 wrong device tree addresses
- [GitHub #46235](https://github.com/zephyrproject-rtos/zephyr/issues/46235) - subsystem: Bluetooth LLL: ASSERTION FAIL [!link->next]
- [GitHub #46234](https://github.com/zephyrproject-rtos/zephyr/issues/46234) - samples: lsm6dso: prints incorrect anglular velocity units
- [GitHub #46208](https://github.com/zephyrproject-rtos/zephyr/issues/46208) - it8xxx2\_evb: tests/kernel/sleep failed, elapsed\_ms = 2125
- [GitHub #46206](https://github.com/zephyrproject-rtos/zephyr/issues/46206) - it8xxx2\_evb: tests/kernel/fatal/exception/ assertion failed – “thread was not aborted”
- [GitHub #46199](https://github.com/zephyrproject-rtos/zephyr/issues/46199) - LIS2DW12 I2C driver uses invalid write command
- [GitHub #46186](https://github.com/zephyrproject-rtos/zephyr/issues/46186) - ISO Broadcaster fails silently on unsupported RTN/SDU\_Interval combination
- [GitHub #46183](https://github.com/zephyrproject-rtos/zephyr/issues/46183) - LE Audio: Broadcast sink stop sending syncable once synced
- [GitHub #46180](https://github.com/zephyrproject-rtos/zephyr/issues/46180) - Add GitHub app for Googler notifications
- [GitHub #46173](https://github.com/zephyrproject-rtos/zephyr/issues/46173) - nRF UART callback is not passed correct index via evt->data.rx.offset sometimes
- [GitHub #46170](https://github.com/zephyrproject-rtos/zephyr/issues/46170) - ipc\_service: open-amp backend may never leave
- [GitHub #46167](https://github.com/zephyrproject-rtos/zephyr/issues/46167) - esp32: Unable to select GPIO for PWM LED driver channel
- [GitHub #46164](https://github.com/zephyrproject-rtos/zephyr/issues/46164) - scripts: release: ci checks for issues associated with backport prs
- [GitHub #46158](https://github.com/zephyrproject-rtos/zephyr/issues/46158) - frdm\_k64f：failed to run test case tests/subsys/modbus/modbus.rtu/server\_setup\_low\_none
- [GitHub #46157](https://github.com/zephyrproject-rtos/zephyr/issues/46157) - ACRN: some cases still failed because of the log missing
- [GitHub #46124](https://github.com/zephyrproject-rtos/zephyr/issues/46124) - stm32g071 ADC drivers apply errata during sampling config
- [GitHub #46117](https://github.com/zephyrproject-rtos/zephyr/issues/46117) - Kernel events can’t be manipulated without race conditions
- [GitHub #46100](https://github.com/zephyrproject-rtos/zephyr/issues/46100) - lib: posix: support for perror()
- [GitHub #46099](https://github.com/zephyrproject-rtos/zephyr/issues/46099) - libc: minimal: add strerror() function
- [GitHub #46075](https://github.com/zephyrproject-rtos/zephyr/issues/46075) - BT HCI Raw on STM32WB55RG
- [GitHub #46072](https://github.com/zephyrproject-rtos/zephyr/issues/46072) - subsys/hawkBit: Debug log error in hawkbit example “CONFIG\_LOG\_STRDUP\_MAX\_STRING”
- [GitHub #46066](https://github.com/zephyrproject-rtos/zephyr/issues/46066) - TF-M: Unable to trigger NMI interrupt from non-secure
- [GitHub #46065](https://github.com/zephyrproject-rtos/zephyr/issues/46065) - Bluetooth: controller: llcp: verify that refactored LLCP is used in EDTT
- [GitHub #46049](https://github.com/zephyrproject-rtos/zephyr/issues/46049) - Usage faults on semaphore usage in driver (stm32l1)
- [GitHub #46048](https://github.com/zephyrproject-rtos/zephyr/issues/46048) - Use dts memory-region property to retrieve memory region used by driver
- [GitHub #46008](https://github.com/zephyrproject-rtos/zephyr/issues/46008) - stm32h7: gptp sample does not work at all
- [GitHub #45993](https://github.com/zephyrproject-rtos/zephyr/issues/45993) - Matter(CHIP) support
- [GitHub #45955](https://github.com/zephyrproject-rtos/zephyr/issues/45955) - stm32h7 i2s support
- [GitHub #45953](https://github.com/zephyrproject-rtos/zephyr/issues/45953) - modem: simcom-sim7080: sendmsg() should result in single outgoing datagram
- [GitHub #45951](https://github.com/zephyrproject-rtos/zephyr/issues/45951) - modem: ublox-sara-r4: outgoing datagrams are truncated if they do not fit MTU
- [GitHub #45938](https://github.com/zephyrproject-rtos/zephyr/issues/45938) - Unable to combine USB CDC-ACM and Modbus Serial due to dependecy on uart\_configure().
- [GitHub #45934](https://github.com/zephyrproject-rtos/zephyr/issues/45934) - ipc\_service: nocopy tx buffer allocation works unexpectedly with RPMSG backend
- [GitHub #45933](https://github.com/zephyrproject-rtos/zephyr/issues/45933) - webusb sample code linking error for esp32 board
- [GitHub #45929](https://github.com/zephyrproject-rtos/zephyr/issues/45929) - up\_squared：failed to run test case tests/posix/common
- [GitHub #45914](https://github.com/zephyrproject-rtos/zephyr/issues/45914) - test: tests/kernel/usage/thread\_runtime\_stats/ test fail
- [GitHub #45866](https://github.com/zephyrproject-rtos/zephyr/issues/45866) - drivers/entropy: stm32: non-compliant RNG configuration on some MCUs
- [GitHub #45848](https://github.com/zephyrproject-rtos/zephyr/issues/45848) - tests: console harness: inaccuracy testcases report
- [GitHub #45846](https://github.com/zephyrproject-rtos/zephyr/issues/45846) - New ZTEST API for noisily skipping a test based dependency failures
- [GitHub #45845](https://github.com/zephyrproject-rtos/zephyr/issues/45845) - tests: The failure test case number increase significantly in CMSIS DSP tests on ARM boards.
- [GitHub #45844](https://github.com/zephyrproject-rtos/zephyr/issues/45844) - Not all bytes are downloaded with HTTP request
- [GitHub #45842](https://github.com/zephyrproject-rtos/zephyr/issues/45842) - drivers: modem: uart\_mux errors after second call to gsm\_ppp\_start
- [GitHub #45827](https://github.com/zephyrproject-rtos/zephyr/issues/45827) - bluetooth: bluetooth host: Adding the same device to resolving list
- [GitHub #45807](https://github.com/zephyrproject-rtos/zephyr/issues/45807) - CivetWeb doesn’t build for CC3232SF
- [GitHub #45802](https://github.com/zephyrproject-rtos/zephyr/issues/45802) - Some tests reported as PASSED (device) but they were only build
- [GitHub #45774](https://github.com/zephyrproject-rtos/zephyr/issues/45774) - drivers: gpio: pca9555: Driver is writing to output port despite all pins been configured as input
- [GitHub #45760](https://github.com/zephyrproject-rtos/zephyr/issues/45760) - Running twister on new board files
- [GitHub #45741](https://github.com/zephyrproject-rtos/zephyr/issues/45741) - LE Audio: Allow unique `bt_codec_qos` for each unicast stream
- [GitHub #45678](https://github.com/zephyrproject-rtos/zephyr/issues/45678) - Lorawan: Devnonce has already been used
- [GitHub #45675](https://github.com/zephyrproject-rtos/zephyr/issues/45675) - testing.ztest.customized\_output: mismatch twister results in json/xml file
- [GitHub #45666](https://github.com/zephyrproject-rtos/zephyr/issues/45666) - Building samples about BLE audio with nrf5340dk does not work
- [GitHub #45658](https://github.com/zephyrproject-rtos/zephyr/issues/45658) - Build failure: civetweb/http\_server with target blackpill\_f411ce and CONFIG\_DEBUG=y
- [GitHub #45647](https://github.com/zephyrproject-rtos/zephyr/issues/45647) - test: drivers: counter: Test passes even when no instances are found
- [GitHub #45613](https://github.com/zephyrproject-rtos/zephyr/issues/45613) - LE Audio: Setting ISO chan path and CC from BAP
- [GitHub #45611](https://github.com/zephyrproject-rtos/zephyr/issues/45611) - GD32 build failure: CAN\_MODE\_NORMAL is redefined
- [GitHub #45596](https://github.com/zephyrproject-rtos/zephyr/issues/45596) - samples: Code relocation nocopy sample has some unusual failure on nrf5340dk
- [GitHub #45581](https://github.com/zephyrproject-rtos/zephyr/issues/45581) - samples: usb: mass: Sample.usb.mass\_flash\_fatfs fails on non-secure nrf5340dk
- [GitHub #45564](https://github.com/zephyrproject-rtos/zephyr/issues/45564) - Zephyr does not boot with CONFIG\_PM=y
- [GitHub #45558](https://github.com/zephyrproject-rtos/zephyr/issues/45558) - LE Audio: Update MICP API with new naming scheme
- [GitHub #45532](https://github.com/zephyrproject-rtos/zephyr/issues/45532) - uart\_msp432p4xx\_poll\_in() seems to be a blocking function
- [GitHub #45509](https://github.com/zephyrproject-rtos/zephyr/issues/45509) - ipc: ipc\_icmsg: Can silently drop buffer if message is too big
- [GitHub #45441](https://github.com/zephyrproject-rtos/zephyr/issues/45441) - SPI NOR driver assume all SPI controller HW is implemnted in an identical way
- [GitHub #45374](https://github.com/zephyrproject-rtos/zephyr/issues/45374) - Creating the unicast group before both ISO connections have been configured might cause issue
- [GitHub #45349](https://github.com/zephyrproject-rtos/zephyr/issues/45349) - ESP32: fails to chain-load sample/board/esp32/wifi\_station from MCUboot
- [GitHub #45315](https://github.com/zephyrproject-rtos/zephyr/issues/45315) - drivers: timer: nrf\_rtc\_timer: NRF boards take a long time to boot application in CONFIG\_TICKLESS\_KERNEL=n mode after OTA update
- [GitHub #45304](https://github.com/zephyrproject-rtos/zephyr/issues/45304) - drivers: can: CAN interfaces are brought up with default bitrate at boot, causing error frames if bus bitrate differs
- [GitHub #45270](https://github.com/zephyrproject-rtos/zephyr/issues/45270) - CMake - TEST\_BIG\_ENDIAN
- [GitHub #45234](https://github.com/zephyrproject-rtos/zephyr/issues/45234) - stm32: Allow multiple GPIOs to trigger an interrupt
- [GitHub #45222](https://github.com/zephyrproject-rtos/zephyr/issues/45222) - drivers: peci: user space handlers not building correctly
- [GitHub #45169](https://github.com/zephyrproject-rtos/zephyr/issues/45169) - rcar\_h3ulcb: failed to run test case tests/drivers/can/api
- [GitHub #45168](https://github.com/zephyrproject-rtos/zephyr/issues/45168) - rcar\_h3ulcb: failed to run test case tests/drivers/can/timing
- [GitHub #45157](https://github.com/zephyrproject-rtos/zephyr/issues/45157) - cmake: Use of -ffreestanding disables many useful optimizations and compiler warnings
- [GitHub #45130](https://github.com/zephyrproject-rtos/zephyr/issues/45130) - LE Audio: Allow CSIS set sizes of 1
- [GitHub #45117](https://github.com/zephyrproject-rtos/zephyr/issues/45117) - drivers: clock\_control: clock\_control\_nrf
- [GitHub #45114](https://github.com/zephyrproject-rtos/zephyr/issues/45114) - Sample net/sockets/echo not working with disco\_l475\_iot1
- [GitHub #45105](https://github.com/zephyrproject-rtos/zephyr/issues/45105) - ACRN: failed to run testcase tests/kernel/fifo/fifo\_timeout/
- [GitHub #45039](https://github.com/zephyrproject-rtos/zephyr/issues/45039) - Bluetooth: Controller: Broadcast multiple BIS (broadcast ISO streams)
- [GitHub #45021](https://github.com/zephyrproject-rtos/zephyr/issues/45021) - Configurable SDMMC bus width for STM32
- [GitHub #45012](https://github.com/zephyrproject-rtos/zephyr/issues/45012) - sam\_e70b\_xplained: failed to run test case tests/drivers/can/timing/drivers.can.timing
- [GitHub #45009](https://github.com/zephyrproject-rtos/zephyr/issues/45009) - twister: many tests failed with “mismatch error” after met a SerialException.
- [GitHub #45008](https://github.com/zephyrproject-rtos/zephyr/issues/45008) - esp32: i2c\_read() error was returned successfully at the bus nack
- [GitHub #44998](https://github.com/zephyrproject-rtos/zephyr/issues/44998) - SMP shell exec command causes BLE stack breakdown if buffer size is too small to hold response
- [GitHub #44996](https://github.com/zephyrproject-rtos/zephyr/issues/44996) - logging: transient strings are no longer duplicated correctly
- [GitHub #44980](https://github.com/zephyrproject-rtos/zephyr/issues/44980) - ws2812\_spi allow setting CPHA in overlay
- [GitHub #44944](https://github.com/zephyrproject-rtos/zephyr/issues/44944) - LE Audio: Add ISO part to broadcast audio bsim tests
- [GitHub #44925](https://github.com/zephyrproject-rtos/zephyr/issues/44925) - intel\_adsp\_cavs25: multiple tests failed after running tests/boards/intel\_adsp
- [GitHub #44898](https://github.com/zephyrproject-rtos/zephyr/issues/44898) - mgmt/mcumgr: Fragmentation of responses may cause mcumgr to drop successfully processed response
- [GitHub #44861](https://github.com/zephyrproject-rtos/zephyr/issues/44861) - WiFi support for STM32 boards
- [GitHub #44830](https://github.com/zephyrproject-rtos/zephyr/issues/44830) - Unable to set compiler warnings on app exclusively
- [GitHub #44824](https://github.com/zephyrproject-rtos/zephyr/issues/44824) - mgmt/mcumgr/lib: Use slist in group registration to unify with Zephyr code
- [GitHub #44725](https://github.com/zephyrproject-rtos/zephyr/issues/44725) - drivers: can: stm32: can\_add\_rx\_filter() does not respect CONFIG\_CAN\_MAX\_FILTER
- [GitHub #44622](https://github.com/zephyrproject-rtos/zephyr/issues/44622) - Microbit v2 board dts file for lsm303agr int line
- [GitHub #44579](https://github.com/zephyrproject-rtos/zephyr/issues/44579) - MCC: Discovery cannot complete with success
- [GitHub #44573](https://github.com/zephyrproject-rtos/zephyr/issues/44573) - Do we have complete RNDIS stack available for STM32 controller in zephyr ?
- [GitHub #44466](https://github.com/zephyrproject-rtos/zephyr/issues/44466) - Zephyr misses strict aliasing disabling
- [GitHub #44455](https://github.com/zephyrproject-rtos/zephyr/issues/44455) - LE Audio: Remove `struct bt_codec *codec` parameter from `bt_audio_broadcast_sink_sync`
- [GitHub #44403](https://github.com/zephyrproject-rtos/zephyr/issues/44403) - MPU fault and `CONFIG_CMAKE_LINKER_GENERATOR`
- [GitHub #44400](https://github.com/zephyrproject-rtos/zephyr/issues/44400) - LE Audio: Unicast server stream control
- [GitHub #44340](https://github.com/zephyrproject-rtos/zephyr/issues/44340) - Bluetooth: controller: Handle parallel (across connections) CU/CPRs in refactored LLCP
- [GitHub #44338](https://github.com/zephyrproject-rtos/zephyr/issues/44338) - Intel CAVS: tests/subsys/logging/log\_immediate/ failed due to non-intact log
- [GitHub #44324](https://github.com/zephyrproject-rtos/zephyr/issues/44324) - Compile error in byteorder.h
- [GitHub #44228](https://github.com/zephyrproject-rtos/zephyr/issues/44228) - drivers: modem: bg9x: bug on cmd AT+QICSGP
- [GitHub #44219](https://github.com/zephyrproject-rtos/zephyr/issues/44219) - mgmt/mcumgr/lib: Incorrect processing of img\_mgmt\_impl\_write\_image\_data leaves mcumgr in broken state in case of error
- [GitHub #44214](https://github.com/zephyrproject-rtos/zephyr/issues/44214) - mgmt/mcumgr/lib: Parasitic use of CONFIG\_HEAP\_MEM\_POOL\_SIZE in image management
- [GitHub #44143](https://github.com/zephyrproject-rtos/zephyr/issues/44143) - Adding picolibc as a module
- [GitHub #44071](https://github.com/zephyrproject-rtos/zephyr/issues/44071) - LE Audio: Upstream remaining parts of topic branch
- [GitHub #44070](https://github.com/zephyrproject-rtos/zephyr/issues/44070) - west spdx TypeError: ‘NoneType’ object is not iterable
- [GitHub #44059](https://github.com/zephyrproject-rtos/zephyr/issues/44059) - Hearing Aid Role
- [GitHub #44058](https://github.com/zephyrproject-rtos/zephyr/issues/44058) - Hearing Access Service API
- [GitHub #44005](https://github.com/zephyrproject-rtos/zephyr/issues/44005) - add strtoll and strtoull to libc minimal
- [GitHub #43940](https://github.com/zephyrproject-rtos/zephyr/issues/43940) - Support for CH32V307 devices
- [GitHub #43933](https://github.com/zephyrproject-rtos/zephyr/issues/43933) - llvm: twister: multiple errors with set but unused variables
- [GitHub #43928](https://github.com/zephyrproject-rtos/zephyr/issues/43928) - pm: going to PM\_STATE\_SOFT\_OFF in pm\_policy\_next\_state causes assert in some cases
- [GitHub #43913](https://github.com/zephyrproject-rtos/zephyr/issues/43913) - LE Audio: Callbacks as singletons or lists?
- [GitHub #43910](https://github.com/zephyrproject-rtos/zephyr/issues/43910) - civetweb/http\_server - DEBUG\_OPTIMIZATIONS enabled
- [GitHub #43887](https://github.com/zephyrproject-rtos/zephyr/issues/43887) - SystemView tracing with STM32L0x fails to compile
- [GitHub #43859](https://github.com/zephyrproject-rtos/zephyr/issues/43859) - Bluetooth: ISO: Add sequence number and timestamp to bt\_iso\_chan\_send
- [GitHub #43828](https://github.com/zephyrproject-rtos/zephyr/issues/43828) - Intel CAVS: multiple tests under tests/boards/intel\_adsp/smoke are failing
- [GitHub #43811](https://github.com/zephyrproject-rtos/zephyr/issues/43811) - ble: gatt: db\_hash\_work runs for too long and makes serial communication fail
- [GitHub #43788](https://github.com/zephyrproject-rtos/zephyr/issues/43788) - LE Audio: Broadcast Sink shall instantiate PACS
- [GitHub #43767](https://github.com/zephyrproject-rtos/zephyr/issues/43767) - LE Audio: Broadcast sink/source use list of streams instead of array
- [GitHub #43718](https://github.com/zephyrproject-rtos/zephyr/issues/43718) - Bluetooth: bt\_conn: Unable to allocate buffer within timeout
- [GitHub #43655](https://github.com/zephyrproject-rtos/zephyr/issues/43655) - esp32c3: Connection fail loop
- [GitHub #43646](https://github.com/zephyrproject-rtos/zephyr/issues/43646) - mgmt/mcumgr/lib: OS taskstat may give shorter list than expected
- [GitHub #43515](https://github.com/zephyrproject-rtos/zephyr/issues/43515) - reel\_board: failed to run tests/kernel/workq/work randomly
- [GitHub #43450](https://github.com/zephyrproject-rtos/zephyr/issues/43450) - twister: platform names from quarantine file are not verified
- [GitHub #43435](https://github.com/zephyrproject-rtos/zephyr/issues/43435) - Bluetooth: controller: llcp: failing EBQ and Harmony tests
- [GitHub #43335](https://github.com/zephyrproject-rtos/zephyr/issues/43335) - Automatic Automated Backports?
- [GitHub #43246](https://github.com/zephyrproject-rtos/zephyr/issues/43246) - Bluetooth: Host: Deadlock with Mesh and Ext Adv on native\_posix
- [GitHub #43245](https://github.com/zephyrproject-rtos/zephyr/issues/43245) - GitHub settings: Update topics
- [GitHub #43202](https://github.com/zephyrproject-rtos/zephyr/issues/43202) - LE Audio: Avoid hardcoding context type for LC3 macros
- [GitHub #43135](https://github.com/zephyrproject-rtos/zephyr/issues/43135) - stm32: uart: Support for wakeup from stop
- [GitHub #43130](https://github.com/zephyrproject-rtos/zephyr/issues/43130) - STM32WL ADC idles / doesn’t work
- [GitHub #43124](https://github.com/zephyrproject-rtos/zephyr/issues/43124) - twister: Create pytest-based PoC for twister v2
- [GitHub #43115](https://github.com/zephyrproject-rtos/zephyr/issues/43115) - Data corruption in STM32 SPI driver in Slave Mode
- [GitHub #43103](https://github.com/zephyrproject-rtos/zephyr/issues/43103) - LwM2M library should use JSON library for parsing
- [GitHub #42890](https://github.com/zephyrproject-rtos/zephyr/issues/42890) - Bluetooth: Controller: Periodic Advertising: AD data fragmentation
- [GitHub #42889](https://github.com/zephyrproject-rtos/zephyr/issues/42889) - Bluetooth: Controller: Extended Advertising: AD data fragmentation
- [GitHub #42885](https://github.com/zephyrproject-rtos/zephyr/issues/42885) - Bluetooth: Controller: Group auxiliary PDU transmissions
- [GitHub #42842](https://github.com/zephyrproject-rtos/zephyr/issues/42842) - BBRAM API is missing a documentation reference page
- [GitHub #42700](https://github.com/zephyrproject-rtos/zephyr/issues/42700) - Support module.yml in zephyr repo
- [GitHub #42684](https://github.com/zephyrproject-rtos/zephyr/issues/42684) - New LLCP handling of Preferred PHY (default tx/rx phy) needs a review
- [GitHub #42649](https://github.com/zephyrproject-rtos/zephyr/issues/42649) - bt\_ots\_client\_unregister()
- [GitHub #42629](https://github.com/zephyrproject-rtos/zephyr/issues/42629) - stm32g0: Device hang/hard fault with AT45 + `CONFIG_PM_DEVICE`
- [GitHub #42574](https://github.com/zephyrproject-rtos/zephyr/issues/42574) - i2c: No support for bus recovery imx.rt and or timeout on bus busy
- [GitHub #42522](https://github.com/zephyrproject-rtos/zephyr/issues/42522) - LE Audio: Immediate alert service
- [GitHub #42472](https://github.com/zephyrproject-rtos/zephyr/issues/42472) - ztest: add support for assumptions
- [GitHub #42450](https://github.com/zephyrproject-rtos/zephyr/issues/42450) - cmake: dts.cmake: Add Board overlays before shields
- [GitHub #42420](https://github.com/zephyrproject-rtos/zephyr/issues/42420) - mgmt/mcumgr/lib: Async image erase command with status check
- [GitHub #42356](https://github.com/zephyrproject-rtos/zephyr/issues/42356) - Repo size - board documentation - large PNGs
- [GitHub #42341](https://github.com/zephyrproject-rtos/zephyr/issues/42341) - LE Audio: CSIS Ordered Access procedure use rank
- [GitHub #42324](https://github.com/zephyrproject-rtos/zephyr/issues/42324) - mgmt/mcumgr/lib: Move to direct use of net\_buf
- [GitHub #42277](https://github.com/zephyrproject-rtos/zephyr/issues/42277) - Zephyr Docs on West need to be updated to include SBOM generation
- [GitHub #42208](https://github.com/zephyrproject-rtos/zephyr/issues/42208) - tests/subsys/logging/log\_api/ fails qemu\_leon3 if ptr\_in\_rodata() is enabled for SPARC
- [GitHub #42197](https://github.com/zephyrproject-rtos/zephyr/issues/42197) - Bluetooth: Controller: llcp: No disconnect if remote does not response for initiated control procedure
- [GitHub #42134](https://github.com/zephyrproject-rtos/zephyr/issues/42134) - TLS handshake error using DTLS on updatehub
- [GitHub #42102](https://github.com/zephyrproject-rtos/zephyr/issues/42102) - doc: searches for sys\_reboot() are inconsistent
- [GitHub #41954](https://github.com/zephyrproject-rtos/zephyr/issues/41954) - Bluetooth: Controller: BIS: Event timing calculations
- [GitHub #41922](https://github.com/zephyrproject-rtos/zephyr/issues/41922) - Bluetooth: Controller: ISOAL: TX: Implement SDU Fragmentation into Unframed PDUs
- [GitHub #41880](https://github.com/zephyrproject-rtos/zephyr/issues/41880) - Strict test ordering in new ztest API
- [GitHub #41776](https://github.com/zephyrproject-rtos/zephyr/issues/41776) - LLVM: support -fuse-ld=lld linker on qemu\_x86.
- [GitHub #41772](https://github.com/zephyrproject-rtos/zephyr/issues/41772) - stm32: G0: adc: Add support for VBAT internal channel
- [GitHub #41711](https://github.com/zephyrproject-rtos/zephyr/issues/41711) - LE Audio: CAP Acceptor Implementation
- [GitHub #41355](https://github.com/zephyrproject-rtos/zephyr/issues/41355) - Bluetooth: API to determine if notification over EATT is possible
- [GitHub #41286](https://github.com/zephyrproject-rtos/zephyr/issues/41286) - Bluetooth SDP: When the SDP attribute length is greater than SDP\_MTU, the attribute is discarded
- [GitHub #41281](https://github.com/zephyrproject-rtos/zephyr/issues/41281) - Style Requirements Seem to Be Inconsistent with Uncrustify Configuration
- [GitHub #41224](https://github.com/zephyrproject-rtos/zephyr/issues/41224) - LE Audio: Telephony and Media Audio Profile (TMAP)
- [GitHub #41217](https://github.com/zephyrproject-rtos/zephyr/issues/41217) - LE Audio: Support for a minimum CCP client
- [GitHub #41214](https://github.com/zephyrproject-rtos/zephyr/issues/41214) - LE Audio: Add public API to CCP/TBS
- [GitHub #41211](https://github.com/zephyrproject-rtos/zephyr/issues/41211) - LE Audio: BASS support for multiple connection
- [GitHub #41208](https://github.com/zephyrproject-rtos/zephyr/issues/41208) - LE Audio: BASS use multi-characteristic macro for receive states
- [GitHub #41205](https://github.com/zephyrproject-rtos/zephyr/issues/41205) - OTS: Debug metadata output
- [GitHub #41204](https://github.com/zephyrproject-rtos/zephyr/issues/41204) - LE Audio: BASS read long
- [GitHub #41203](https://github.com/zephyrproject-rtos/zephyr/issues/41203) - LE Audio: BASS write long
- [GitHub #41199](https://github.com/zephyrproject-rtos/zephyr/issues/41199) - LE Audio: Media API with one call per command, rather than sending opcodes
- [GitHub #41197](https://github.com/zephyrproject-rtos/zephyr/issues/41197) - LE Audio: Use BT\_MEDIA\_PROXY values instead of BT\_MCS
- [GitHub #41193](https://github.com/zephyrproject-rtos/zephyr/issues/41193) - LE Audio: Couple IN audio stream with an OUT audio stream
- [GitHub #40933](https://github.com/zephyrproject-rtos/zephyr/issues/40933) - mgmt/mcumgr/lib: Divide the lib Kconfig into sub-Kconfigs dedicated to specific mgmt cmd group
- [GitHub #40893](https://github.com/zephyrproject-rtos/zephyr/issues/40893) - mgmt/mcumg/lib: Encode shell command execution result in additional field of response
- [GitHub #40855](https://github.com/zephyrproject-rtos/zephyr/issues/40855) - mgmt/mcumgr/lib: Add optional image/slot parameter to “image erase” mcumgr request command
- [GitHub #40854](https://github.com/zephyrproject-rtos/zephyr/issues/40854) - mgmt/mcumgr/lib: Extend taskstat response with “runtime” statistics
- [GitHub #40827](https://github.com/zephyrproject-rtos/zephyr/issues/40827) - Tensorflow example not working in zephyr v2.6
- [GitHub #40664](https://github.com/zephyrproject-rtos/zephyr/issues/40664) - Bluetooth: GATT: EATT: Multiple notify feature not utilize new PDU fully
- [GitHub #40444](https://github.com/zephyrproject-rtos/zephyr/issues/40444) - Late C++ constructor initialization on native posix boards
- [GitHub #40389](https://github.com/zephyrproject-rtos/zephyr/issues/40389) - Inconsistent use of CMake / environment variables
- [GitHub #40309](https://github.com/zephyrproject-rtos/zephyr/issues/40309) - Multi-image support for MCUboot
- [GitHub #40146](https://github.com/zephyrproject-rtos/zephyr/issues/40146) - On the status of DT-defined regions and MPU
- [GitHub #39888](https://github.com/zephyrproject-rtos/zephyr/issues/39888) - STM32L4: usb-hid: regression in hal 1.17.0
- [GitHub #39491](https://github.com/zephyrproject-rtos/zephyr/issues/39491) - Add a hal module for Nuclei RISC-V core (NMSIS)
- [GitHub #39486](https://github.com/zephyrproject-rtos/zephyr/issues/39486) - Improve emulator APIs for testing
- [GitHub #39347](https://github.com/zephyrproject-rtos/zephyr/issues/39347) - Static object constructors do not execute on the NATIVE\_POSIX\_64 target
- [GitHub #39153](https://github.com/zephyrproject-rtos/zephyr/issues/39153) - Improve ztest test suites (setup/teardown/before/after + OOD)
- [GitHub #39037](https://github.com/zephyrproject-rtos/zephyr/issues/39037) - CivetWeb samples fail to build with CONFIG\_NEWLIB\_LIBC
- [GitHub #38727](https://github.com/zephyrproject-rtos/zephyr/issues/38727) - [RFC] Add hal\_gigadevice to support GigaDevice SoC Vendor
- [GitHub #38654](https://github.com/zephyrproject-rtos/zephyr/issues/38654) - drivers: modem: bg9x: Has no means to update size of received packet.
- [GitHub #38613](https://github.com/zephyrproject-rtos/zephyr/issues/38613) - BLE connection parameters updated with inconsistent values
- [GitHub #38544](https://github.com/zephyrproject-rtos/zephyr/issues/38544) - drivers: wifi: esWIFI: Regression due to 35815
- [GitHub #38494](https://github.com/zephyrproject-rtos/zephyr/issues/38494) - Flooded logs when using CDC\_ACM as back-end
- [GitHub #38336](https://github.com/zephyrproject-rtos/zephyr/issues/38336) - Bluetooth: Host: separate authentication callbacks for each identity
- [GitHub #37883](https://github.com/zephyrproject-rtos/zephyr/issues/37883) - Mesh Bluetooth Sample not working with P-NUCLEO-WB55RG
- [GitHub #37704](https://github.com/zephyrproject-rtos/zephyr/issues/37704) - hello world doesn’t work on qemu\_arc\_em when CONFIG\_ISR\_STACK\_SIZE=1048510
- [GitHub #37212](https://github.com/zephyrproject-rtos/zephyr/issues/37212) - improve docs with diagram for boot flow of ACRN on x86 ehl\_crb
- [GitHub #36819](https://github.com/zephyrproject-rtos/zephyr/issues/36819) - qemu\_leon3 samples/subsys/portability/cmsis\_rtos\_v2 samples failing
- [GitHub #36644](https://github.com/zephyrproject-rtos/zephyr/issues/36644) - Toolchain C++ headers can be included when libstdc++ is not selected
- [GitHub #36476](https://github.com/zephyrproject-rtos/zephyr/issues/36476) - Add intel HAL support
- [GitHub #36084](https://github.com/zephyrproject-rtos/zephyr/issues/36084) - Arduino Nano 33 BLE: USB gets disconnected after flashing
- [GitHub #36026](https://github.com/zephyrproject-rtos/zephyr/issues/36026) - wolfssl / wolfcrypt
- [GitHub #35931](https://github.com/zephyrproject-rtos/zephyr/issues/35931) - Bluetooth: controller: Assertion in ull\_master.c
- [GitHub #35816](https://github.com/zephyrproject-rtos/zephyr/issues/35816) - timer: STM32: using hw timer for counting and interrupt callback
- [GitHub #35778](https://github.com/zephyrproject-rtos/zephyr/issues/35778) - pwm : STM32: Timer handling interrupt callback handling
- [GitHub #35762](https://github.com/zephyrproject-rtos/zephyr/issues/35762) - SAMPLES: shell\_module gives no console output on qemu\_leon3
- [GitHub #35719](https://github.com/zephyrproject-rtos/zephyr/issues/35719) - WiFi Management expects networking to be offloaded
- [GitHub #35512](https://github.com/zephyrproject-rtos/zephyr/issues/35512) - OpenThread can’t find TRNG driver on nRF5340
- [GitHub #34927](https://github.com/zephyrproject-rtos/zephyr/issues/34927) - Add error check to twister if set of platforms between platform\_allow and integration\_platforms is empty
- [GitHub #34600](https://github.com/zephyrproject-rtos/zephyr/issues/34600) - Bluetooth: L2CAP: Deadlock when there are no free buffers while transmitting on multiple channels
- [GitHub #34571](https://github.com/zephyrproject-rtos/zephyr/issues/34571) - Twister mark successfully passed tests as failed
- [GitHub #34438](https://github.com/zephyrproject-rtos/zephyr/issues/34438) - CivetWeb sample only supports HTTP, Zephyr lacks TLS support
- [GitHub #34413](https://github.com/zephyrproject-rtos/zephyr/issues/34413) - Improve \_\_used attribute to actually keep requested function/variable
- [GitHub #34227](https://github.com/zephyrproject-rtos/zephyr/issues/34227) - Use compile time resolved device bindings in flash map, when possible
- [GitHub #34226](https://github.com/zephyrproject-rtos/zephyr/issues/34226) - Compile error when building civetweb samples for posix\_native
- [GitHub #34190](https://github.com/zephyrproject-rtos/zephyr/issues/34190) - Newbie: Simple C++ List App Builds for QEMU but not Native Posix Emulation
- [GitHub #33876](https://github.com/zephyrproject-rtos/zephyr/issues/33876) - Lora sender sample build error for esp32
- [GitHub #33865](https://github.com/zephyrproject-rtos/zephyr/issues/33865) - Bluetooth: iso\_server security is not applied
- [GitHub #33725](https://github.com/zephyrproject-rtos/zephyr/issues/33725) - Modularisation and Restructuring of Documentation
- [GitHub #33627](https://github.com/zephyrproject-rtos/zephyr/issues/33627) - Provide alternative nvs\_init that will take const struct `*device` instead of device name
- [GitHub #33520](https://github.com/zephyrproject-rtos/zephyr/issues/33520) - Update module civetweb (bug fixes and increased stack size requirement)
- [GitHub #33339](https://github.com/zephyrproject-rtos/zephyr/issues/33339) - API/functions to get remaining free heap size
- [GitHub #33185](https://github.com/zephyrproject-rtos/zephyr/issues/33185) - TCP traffic with IPSP sample not working on 96Boards Nitrogen
- [GitHub #33015](https://github.com/zephyrproject-rtos/zephyr/issues/33015) - spi\_nor driver: SPI\_NOR\_IDLE\_IN\_DPD breaks SPI\_NOR\_SFDP\_RUNTIME
- [GitHub #32665](https://github.com/zephyrproject-rtos/zephyr/issues/32665) - Bluetooth: controller: inclusion of vendor data type and function overrides provided by vendor LLL
- [GitHub #32608](https://github.com/zephyrproject-rtos/zephyr/issues/32608) - Revert practice of removing devicetree labels
- [GitHub #32516](https://github.com/zephyrproject-rtos/zephyr/issues/32516) - RFC: 1-Wire driver
- [GitHub #32197](https://github.com/zephyrproject-rtos/zephyr/issues/32197) - arch\_switch() on SPARC isn’t quite right
- [GitHub #31290](https://github.com/zephyrproject-rtos/zephyr/issues/31290) - dts: arm: st: standardize pwm default property st,prescaler to 0
- [GitHub #31208](https://github.com/zephyrproject-rtos/zephyr/issues/31208) - Bluetooth Mesh CCM Hardware Acceleration
- [GitHub #31175](https://github.com/zephyrproject-rtos/zephyr/issues/31175) - STM32F1 RTC
- [GitHub #30694](https://github.com/zephyrproject-rtos/zephyr/issues/30694) - Some boards enable non-minimal peripherals by default
- [GitHub #30505](https://github.com/zephyrproject-rtos/zephyr/issues/30505) - Rework pipe\_api test for coverage
- [GitHub #30365](https://github.com/zephyrproject-rtos/zephyr/issues/30365) - TCP2 does not implement Nagle algorithm
- [GitHub #29866](https://github.com/zephyrproject-rtos/zephyr/issues/29866) - Drivers/PCIE: read/write 8/16/32 bit word to an endpoint’s configuration space
- [GitHub #28145](https://github.com/zephyrproject-rtos/zephyr/issues/28145) - nRF52840 Dongle cannot scan LE Coded PHY devices
- [GitHub #27997](https://github.com/zephyrproject-rtos/zephyr/issues/27997) - Errors in copy paste lengthy script into Shell Console
- [GitHub #27975](https://github.com/zephyrproject-rtos/zephyr/issues/27975) - [Thingy52\_nrf52832 board] - Working with other led than led0
- [GitHub #27735](https://github.com/zephyrproject-rtos/zephyr/issues/27735) - Enable DT-based sanity-check test filtering
- [GitHub #27585](https://github.com/zephyrproject-rtos/zephyr/issues/27585) - investigate using the interrupt stack for the idle thread
- [GitHub #27511](https://github.com/zephyrproject-rtos/zephyr/issues/27511) - coverage: qemu platforms: sanitycheck generates many `unexpected eof` failures when enable coverage
- [GitHub #27033](https://github.com/zephyrproject-rtos/zephyr/issues/27033) - Update terminology related to I2C
- [GitHub #26938](https://github.com/zephyrproject-rtos/zephyr/issues/26938) - gpio: api to query pin configuration
- [GitHub #26179](https://github.com/zephyrproject-rtos/zephyr/issues/26179) - devicetree: Missing support of unquoted strings
- [GitHub #25442](https://github.com/zephyrproject-rtos/zephyr/issues/25442) - Does Zephyr support USB host mode ?
- [GitHub #25382](https://github.com/zephyrproject-rtos/zephyr/issues/25382) - devicetree: Add ranges property support for PCIe node
- [GitHub #24457](https://github.com/zephyrproject-rtos/zephyr/issues/24457) - Common Trace Format - Failed to produce correct trace output
- [GitHub #24373](https://github.com/zephyrproject-rtos/zephyr/issues/24373) - NULL-pointer dereferencing in GATT when master connection fails
- [GitHub #23893](https://github.com/zephyrproject-rtos/zephyr/issues/23893) - server to client ble coms: two characteristics with notifications failing to notify the right characteristics at the client
- [GitHub #23302](https://github.com/zephyrproject-rtos/zephyr/issues/23302) - Poor TCP performance
- [GitHub #23165](https://github.com/zephyrproject-rtos/zephyr/issues/23165) - macOS setup fails to build for lack of “elftools” Python package
- [GitHub #23111](https://github.com/zephyrproject-rtos/zephyr/issues/23111) - drivers:usb:device:sam0: Descriptor tables are filled with zeros in attach()
- [GitHub #23032](https://github.com/zephyrproject-rtos/zephyr/issues/23032) - Need help to enable Sub-GHz for ieee802154\_cc13xx\_cc26xx
- [GitHub #22208](https://github.com/zephyrproject-rtos/zephyr/issues/22208) - gpio: clean up debounce configuration
- [GitHub #22079](https://github.com/zephyrproject-rtos/zephyr/issues/22079) - Add reception channel information to advertise\_report
- [GitHub #21980](https://github.com/zephyrproject-rtos/zephyr/issues/21980) - Doesn’t Install on Raspberry Pi
- [GitHub #21234](https://github.com/zephyrproject-rtos/zephyr/issues/21234) - drivers: usb\_dc\_sam0: usb detach and reattach does not work
- [GitHub #19979](https://github.com/zephyrproject-rtos/zephyr/issues/19979) - Implement Cortex-R floating-point support
- [GitHub #19244](https://github.com/zephyrproject-rtos/zephyr/issues/19244) - BLE throughput of DFU by Mcumgr is too slow
- [GitHub #18551](https://github.com/zephyrproject-rtos/zephyr/issues/18551) - address-of-temporary idiom not allowed in C++
- [GitHub #16683](https://github.com/zephyrproject-rtos/zephyr/issues/16683) - [RFC] Missing parts of libc required for CivetWeb
- [GitHub #16674](https://github.com/zephyrproject-rtos/zephyr/issues/16674) - Checkpatch generates incorrect warning for \_\_DEPRECATED\_MACRO
- [GitHub #15591](https://github.com/zephyrproject-rtos/zephyr/issues/15591) - Add STM32 LCD-TFT Display Controller (LTDC) Driver
- [GitHub #15429](https://github.com/zephyrproject-rtos/zephyr/issues/15429) - shields: improve cmake to define/extract pinmux and defconfig info
- [GitHub #15256](https://github.com/zephyrproject-rtos/zephyr/issues/15256) - Link Layer Control Procedure overhaul
- [GitHub #15214](https://github.com/zephyrproject-rtos/zephyr/issues/15214) - Enforce correct compilers in boilerplate.cmake
- [GitHub #14527](https://github.com/zephyrproject-rtos/zephyr/issues/14527) - [wip] Generic support for out-of-tree drivers
- [GitHub #14068](https://github.com/zephyrproject-rtos/zephyr/issues/14068) - Allow better control on SPI pin settings
- [GitHub #13662](https://github.com/zephyrproject-rtos/zephyr/issues/13662) - samples/subsys/usb/cdc\_acm: Stuck at “Wait for DTR”
- [GitHub #13639](https://github.com/zephyrproject-rtos/zephyr/issues/13639) - Use dirsync for doxygen directory syncing
- [GitHub #13519](https://github.com/zephyrproject-rtos/zephyr/issues/13519) - BLE Split Link Layer Improvements
- [GitHub #13196](https://github.com/zephyrproject-rtos/zephyr/issues/13196) - LwM2M: support Access Control objects (object id 2)
- [GitHub #12272](https://github.com/zephyrproject-rtos/zephyr/issues/12272) - SD/MMC interface support
- [GitHub #12191](https://github.com/zephyrproject-rtos/zephyr/issues/12191) - Nested interrupt test has very poor coverage
- [GitHub #11975](https://github.com/zephyrproject-rtos/zephyr/issues/11975) - Logging subsystem doesn’t work with prink char\_out functions
- [GitHub #11918](https://github.com/zephyrproject-rtos/zephyr/issues/11918) - Runtime pin configuration
- [GitHub #11636](https://github.com/zephyrproject-rtos/zephyr/issues/11636) - Generic GPIO reset driver
- [GitHub #10938](https://github.com/zephyrproject-rtos/zephyr/issues/10938) - Standardize labels (string device names) used for device binding
- [GitHub #10516](https://github.com/zephyrproject-rtos/zephyr/issues/10516) - Migrate drivers to Devicetree
- [GitHub #10512](https://github.com/zephyrproject-rtos/zephyr/issues/10512) - Console, logger, shell architecure
- [GitHub #8945](https://github.com/zephyrproject-rtos/zephyr/issues/8945) - Explore baselibc as a replacement for minimal libc
- [GitHub #8497](https://github.com/zephyrproject-rtos/zephyr/issues/8497) - Need a “monitor” spin-for-ISR API
- [GitHub #8496](https://github.com/zephyrproject-rtos/zephyr/issues/8496) - Need a “lock” wrapper around k\_sem
- [GitHub #8139](https://github.com/zephyrproject-rtos/zephyr/issues/8139) - Driver for BMA400 accelerometer
- [GitHub #7876](https://github.com/zephyrproject-rtos/zephyr/issues/7876) - net: tcp: Zero Window Probes are not supported/handled properly
- [GitHub #7516](https://github.com/zephyrproject-rtos/zephyr/issues/7516) - Support binary blobs / libraries and glue code in vanilla upstream Zephyr
- [GitHub #6498](https://github.com/zephyrproject-rtos/zephyr/issues/6498) - Kernel high-resolution timer support
- [GitHub #5408](https://github.com/zephyrproject-rtos/zephyr/issues/5408) - Improve docs & samples on device tree overlay
- [GitHub #1392](https://github.com/zephyrproject-rtos/zephyr/issues/1392) - No module named ‘elftools’
- [GitHub #2170](https://github.com/zephyrproject-rtos/zephyr/issues/2170) - I2C fail to read GY2561 sensor when GY2561 & GY271 sensor are attached to I2C bus.
