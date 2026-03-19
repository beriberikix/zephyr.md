---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/releases/release-notes-3.3.html
original_path: releases/release-notes-3.3.html
---

# Zephyr 3.3.0

We are pleased to announce the release of Zephyr version 3.3.0.

Major enhancements with this release include:

- Introduced [Fuel Gauge](../hardware/peripherals/fuel_gauge.md#fuel-gauge-api) subsystem for battery level
  monitoring.
- Introduced [USB-C](../connectivity/usb/pd/ucds.md#usbc-api) device stack with PD (power delivery)
  support.
- Introduced [DSP (digital signal processing)](../services/dsp/index.md#zdsp-api) subsystem with
  CMSIS-DSP as the default backend.
- Added Picolibc support for all architectures when using Zephyr SDK.

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

- CVE-2023-0359: Under embargo until 2023-04-20
- CVE-2023-0779: Under embargo until 2023-04-22

## API Changes

- Emulator creation APIs have changed to better match
  [`DEVICE_DT_DEFINE`](../doxygen/html/group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1). It also includes a new backend API pointer to
  allow sensors to share common APIs for more generic tests.

### Changes in this release

- Newlib nano variant is no longer selected by default when
  [`CONFIG_NEWLIB_LIBC`](../kconfig.md#CONFIG_NEWLIB_LIBC "CONFIG_NEWLIB_LIBC") is selected.
  [`CONFIG_NEWLIB_LIBC_NANO`](../kconfig.md#CONFIG_NEWLIB_LIBC_NANO "CONFIG_NEWLIB_LIBC_NANO") must now be explicitly selected in
  order to use the nano variant.
- Bluetooth: Added extra options to bt\_le\_per\_adv\_sync\_transfer\_subscribe to
  allow disabling sync reports, and enable sync report filtering. these two
  options are mutually exclusive.
- Bluetooth: [`CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER`](../kconfig.md#CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER "CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER")
  and [`CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER`](../kconfig.md#CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER "CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER") have been
  added to enable the PAST implementation rather than
  `CONFIG_BT_CONN`.
- Flashdisk: `CONFIG_DISK_FLASH_VOLUME_NAME`,
  `CONFIG_DISK_FLASH_DEV_NAME`,
  `CONFIG_DISK_FLASH_START`,
  `CONFIG_DISK_FLASH_MAX_RW_SIZE`,
  `CONFIG_DISK_ERASE_BLOCK_SIZE`,
  `CONFIG_DISK_FLASH_ERASE_ALIGNMENT`,
  `CONFIG_DISK_VOLUME_SIZE` and
  `CONFIG_DISK_FLASH_SECTOR_SIZE` Kconfig options have been
  removed in favor of new [`zephyr,flash-disk`](../build/dts/api/bindings/misc/zephyr%2Cflash-disk.md#std-dtcompatible-zephyr-flash-disk) devicetree binding.
- Regulator APIs previously located in `<zephyr/drivers/regulator/consumer.h>`
  are now part of `<zephyr/drivers/regulator.h>`.
- Starting from this release `zephyr-` prefixed tags won’t be created
  anymore. The project will continue using `v` tags, for example `v3.3.0`.
- Bluetooth: Deprecated the Bluetooth logging subsystem in favor of the Zephyr
  standard logging system. To enable debugging for a particular module in the
  Bluetooth subsystem, enable CONFIG\_BT\_(module name)\_LOG\_LEVEL\_DBG instead of
  CONFIG\_BT\_DEBUG\_(module name).
- MCUmgr img\_mgmt now requires that a full sha256 hash to be used when
  uploading an image to keep track of the progress, where the sha256 hash
  is of the whole file being uploaded (different to the hash used when getting
  image states). Use of a truncated hash or non-sha256 hash will still work
  but will cause issues and failures in client software with future updates
  to Zephyr/MCUmgr such as image verification.
- MCUmgr handlers no longer need to be registered by the application code,
  handlers just need to use a define which will then call the supplied
  registration function at boot-up. If applications register this then
  those registrations should be removed to prevent registering the same
  handler multiple times.
- MCUmgr Bluetooth and UDP transports no longer need to be registered by the
  application code, these will now automatically be registered at boot-up (this
  feature can be disabled for the UDP transport by setting
  [`CONFIG_MCUMGR_TRANSPORT_UDP_AUTOMATIC_INIT`](../kconfig.md#CONFIG_MCUMGR_TRANSPORT_UDP_AUTOMATIC_INIT "CONFIG_MCUMGR_TRANSPORT_UDP_AUTOMATIC_INIT")). If
  applications register transports then those registrations should be removed
  to prevent registering the same transport multiple times.
- MCUmgr transport Kconfigs have changed from `select` to `depends on`
  which means that for applications using the Bluetooth transport,
  applications will now need to enable the following:

  - [`CONFIG_BT`](../kconfig.md#CONFIG_BT "CONFIG_BT")
  - [`CONFIG_BT_PERIPHERAL`](../kconfig.md#CONFIG_BT_PERIPHERAL "CONFIG_BT_PERIPHERAL")

  For CDC or serial transports:

  - [`CONFIG_CONSOLE`](../kconfig.md#CONFIG_CONSOLE "CONFIG_CONSOLE")

  For shell transport:

  - [`CONFIG_SHELL`](../kconfig.md#CONFIG_SHELL "CONFIG_SHELL")
  - [`CONFIG_SHELL_BACKEND_SERIAL`](../kconfig.md#CONFIG_SHELL_BACKEND_SERIAL "CONFIG_SHELL_BACKEND_SERIAL")

  For UDP transport:

  - [`CONFIG_NETWORKING`](../kconfig.md#CONFIG_NETWORKING "CONFIG_NETWORKING")
  - [`CONFIG_NET_UDP`](../kconfig.md#CONFIG_NET_UDP "CONFIG_NET_UDP")
- MCUmgr fs\_mgmt hash/checksum function, type and variable names have been
  changed to be prefixed with `fs_mgmt_` to retain alignment with other
  zephyr and MCUmgr APIs.
- Python’s argparse argument parser usage in Zephyr scripts has been updated
  to disable abbreviations, any future python scripts or python code updates
  must also disable allowing abbreviations by using `allow_abbrev=False`
  when setting up `ArgumentParser()`.

  This may cause out-of-tree scripts or commands to fail if they have relied
  upon their behaviour previously, these will need to be updated in order for
  building to work. As an example, if a script argument had `--reset-type`
  and an out-of-tree script used this by passing `--reset` then it will need
  to be updated to use the full argument name, `--reset-type`.
- Rewrote the CAN API to utilize flag bitfields instead discrete of struct
  members for indicating standard/extended CAN ID, Remote Transmission Request
  (RTR), and added support for filtering of CAN-FD format frames.
- New [Zephyr message bus (Zbus)](../services/zbus/index.md#zbus) subsystem added; a message-oriented
  bus that enables one-to-one, one-to-many and many-to-many communication
  between threads.
- zTest now supports controlling test summary printouts via the
  [`CONFIG_ZTEST_SUMMARY`](../kconfig.md#CONFIG_ZTEST_SUMMARY "CONFIG_ZTEST_SUMMARY"). This Kconfig can be set to `n` for
  less verbose test output.
- Emulators now support a backend API pointer which allows a single class of
  devices to provide similar emulated functionality. This can be used to write
  a single test for the class of devices and testing various boards using
  different chips.

### Removed APIs in this release

- Removed `CONFIG_COUNTER_RTC_STM32_LSE_DRIVE*`
  This should now be configured using the `driving_capability` property of
  LSE clock
- Removed `CONFIG_COUNTER_RTC_STM32_LSE_BYPASS`
  This should now be configured using the new `lse_bypass` property of
  LSE clock
- Removed `CONFIG_COUNTER_RTC_STM32_BACKUP_DOMAIN_RESET`. Its purpose
  was to control the reset of the counter value at board reset. It is removed since
  it has too wide scope (full Backup RAM reset). Replaced by
  [`CONFIG_COUNTER_RTC_STM32_SAVE_VALUE_BETWEEN_RESETS`](../kconfig.md#CONFIG_COUNTER_RTC_STM32_SAVE_VALUE_BETWEEN_RESETS "CONFIG_COUNTER_RTC_STM32_SAVE_VALUE_BETWEEN_RESETS") which also
  allows to control the reset of counter value, with an opposite logic.
- Removed deprecated tinycbor module, code that uses this module should be
  updated to use zcbor as a replacement.
- Removed deprecated GPIO flags used for setting debounce, drive strength and
  voltage level. All drivers now use vendor-specific flags as needed.
- Removed deprecated `UTIL_LISTIFY` helper macro.
- Removed deprecated `pwm_pin*` family of functions from the PWM API.
- Removed deprecated `nvs_init` function from the NVS filesystem API.
- Removed deprecated `DT_CHOSEN_*_LABEL` helper macros.
- Removed deprecated property `enable-pin-remap` from :dtcompatible: st,stm32-usb:.
  `remap-pa11-pa12` from :dtcompatible: st-stm32-pinctrl: should now be used.

### Deprecated in this release

- `xtools` toolchain variant is now deprecated. When using a
  custom toolchain built with Crosstool-NG, the
  [cross-compile toolchain variant](../develop/toolchains/other_x_compilers.md#other-x-compilers) should be used instead.
- C++ library Kconfig options have been renamed to improve consistency. See
  below for the list of deprecated Kconfig options and their replacements:

  | Deprecated | Replacement |
  | --- | --- |
  | `CONFIG_CPLUSPLUS` | [`CONFIG_CPP`](../kconfig.md#CONFIG_CPP "CONFIG_CPP") |
  | `CONFIG_EXCEPTIONS` | [`CONFIG_CPP_EXCEPTIONS`](../kconfig.md#CONFIG_CPP_EXCEPTIONS "CONFIG_CPP_EXCEPTIONS") |
  | `CONFIG_RTTI` | [`CONFIG_CPP_RTTI`](../kconfig.md#CONFIG_CPP_RTTI "CONFIG_CPP_RTTI") |
  | `CONFIG_LIB_CPLUSPLUS` | [`CONFIG_LIBCPP_IMPLEMENTATION`](../kconfig.md#CONFIG_LIBCPP_IMPLEMENTATION "CONFIG_LIBCPP_IMPLEMENTATION") |
- MCUmgr subsystem, specifically the SMP transport API, is dropping zephyr\_
  prefix, deprecating prefixed functions and callback type definitions with the
  prefix and replacing them with prefix-less variants.
  The `zephyr_smp_transport` type, representing transport object,
  is now replaced with [`smp_transport`](../doxygen/html/structsmp__transport.md), and the later one is used,
  instead of the former one, by all prefix-less functions.

  Deprecated functions and their replacements:

  | Deprecated | Drop in replacement |
  | --- | --- |
  | `zephyr_smp_transport_init()` | [`smp_transport_init()`](../doxygen/html/group__mcumgr__transport__smp.md#gaf275034765327b52b900046d71c411ee) |
  | `zephyr_smp_rx_req()` | `smp_rx_req()` |
  | `zephyr_smp_alloc_rsp()` | `smp_alloc_rsp()` |
  | `zephyr_smp_free_buf()` | `smp_free_buf()` |

  Deprecated callback types and their replacements:

  | Deprecated | Drop in replacement |
  | --- | --- |
  | `zephyr_smp_transport_out_fn()` | `smp_transport_out_fn()` |
  | `zephyr_smp_transport_get_mtu_fn()` | `smp_transport_get_mtu_fn()` |
  | `zephyr_smp_transport_ud_copy_fn()` | `smp_transport_ud_copy_fn()` |
  | `zephyr_smp_transport_ud_free_fn()` | `smp_transport_ud_free_fn()` |

  NOTE: Only functions are marked as `__deprecated`, type definitions are not.
- STM32 Ethernet Mac address Kconfig related symbols (`CONFIG_ETH_STM32_HAL_RANDOM_MAC`,
  `CONFIG_ETH_STM32_HAL_MAC4`, …) have been deprecated in favor
  of the use of zephyr generic device tree `local-mac-address` and `zephyr,random-mac-address`
  properties.
- STM32 RTC source clock should now be configured using devicetree.
  Related Kconfig `CONFIG_COUNTER_RTC_STM32_CLOCK_LSI` and
  `CONFIG_COUNTER_RTC_STM32_CLOCK_LSE` options are now
  deprecated.
- STM32 Interrupt controller Kconfig symbols such as `CONFIG_EXTI_STM32_EXTI0_IRQ_PRI`
  are removed. Related IRQ priorities should now be configured in device tree.
- PWM\_STM32\_COMPLEMENTARY deprecated in favor of STM32\_PWM\_COMPLEMENTARY.
- File backend for settings APIs and Kconfig options were deprecated:

  `settings_mount_fs_backend()` in favor of `settings_mount_file_backend()`

  `CONFIG_SETTINGS_FS` in favor of [`CONFIG_SETTINGS_FILE`](../kconfig.md#CONFIG_SETTINGS_FILE "CONFIG_SETTINGS_FILE")

  `CONFIG_SETTINGS_FS_DIR` in favor of creating all parent
  directories from [`CONFIG_SETTINGS_FILE_PATH`](../kconfig.md#CONFIG_SETTINGS_FILE_PATH "CONFIG_SETTINGS_FILE_PATH")

  `CONFIG_SETTINGS_FS_FILE` in favor of [`CONFIG_SETTINGS_FILE_PATH`](../kconfig.md#CONFIG_SETTINGS_FILE_PATH "CONFIG_SETTINGS_FILE_PATH")

  `CONFIG_SETTINGS_FS_MAX_LINES` in favor of [`CONFIG_SETTINGS_FILE_MAX_LINES`](../kconfig.md#CONFIG_SETTINGS_FILE_MAX_LINES "CONFIG_SETTINGS_FILE_MAX_LINES")
- PCIe APIs `pcie_probe()` and `pcie_bdf_lookup()` have been
  deprecated in favor of a centralized scan of available PCIe devices.
- POSIX API

  > - Deprecated `PTHREAD_COND_DEFINE`, `PTHREAD_MUTEX_DEFINE` in favour of the
  >   standard [`PTHREAD_COND_INITIALIZER`](../doxygen/html/pthread_8h.md#aa7b867fe46f3660283fcb356c4fcbbf0) and [`PTHREAD_MUTEX_INITIALIZER`](../doxygen/html/pthread_8h.md#a84e55100366a6a8338a2af3b3f279686).
  > - Deprecated `<fcntl.h>`, `<sys/stat.h>` header files in the minimal libc in favour of
  >   `<zephyr/posix/fcntl.h>` and `<zephyr/posix/sys/stat.h>`.
- SPI DT `spi_is_ready()` function has been deprecated in favor of [`spi_is_ready_dt()`](../doxygen/html/group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403).
- LwM2M APIs using string references as LwM2M paths has been deprecated in favor of functions
  using `lwm2m_path_obj` instead.

### Stable API changes in this release

- MCUmgr events have been reworked to use a single, unified callback system.
  This allows better customisation of the callbacks with a lower flash size.
  Applications using the existing callback system will need to be upgraded to
  use the new API by following the [migration guide](../services/device_mgmt/mcumgr_callbacks.md#mcumgr-cb-migration)
- [`net_pkt_get_frag()`](../doxygen/html/group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e), [`net_pkt_get_reserve_tx_data()`](../doxygen/html/group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9) and
  [`net_pkt_get_reserve_rx_data()`](../doxygen/html/group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485) functions are now requiring to specify
  the minimum fragment length to allocate, so that they work correctly also in
  case [`CONFIG_NET_BUF_VARIABLE_DATA_SIZE`](../kconfig.md#CONFIG_NET_BUF_VARIABLE_DATA_SIZE "CONFIG_NET_BUF_VARIABLE_DATA_SIZE") is enabled.
  Applications using this APIs will need to be updated to provide the expected
  fragment length.
- Marked the Controller Area Network (CAN) controller driver API as stable.

### New APIs in this release

## Kernel

- Added an “EARLY” init level that runs immediately on entry to z\_cstart()
- Refactored the internal CPU count API to allow for runtime changes
- Added support for defining application main() in C++ code
- Fixed a race condition on SMP when pending threads where a second CPU
  could attempt to run a thread before the pending thread had finished
  the context switch.

## Architectures

- ARC

  - Fixed & reworked interrupt management (enabling / disabling) for the SMP systems
  - Added TLS (thread-local storage) for ARC MWDT toolchain
  - Fixed & rework irq\_offload implementation
  - Fixed multiple logging & cbprintf issues for ARCv3 64bit
  - Added XIP support with MWDT toolchain
  - Improved DSP support, add DSP and AGU context save / restore
  - Added XY memory support for ARC DSP targets
  - Added architectures-specific DSP tests
  - Added additional compile-time checks for unsupported configuration: ARC\_FIRQ + ARC\_HAS\_SECURE
  - Added support for using `__auto_type` type for ARC MWDT toolchain
  - Added support for using `_Generic` and `__fallthrough` keywords for ARC MWDT toolchain
  - Bumped minimal required ARC MWDT version to 2022.09
  - Fixed & reworked inclusion of C/C++ headers for ARC MWDT toolchain which cased build issue with
    C++
- ARM

  - More precise ‘reason’ codes are now returned in the fault handler.
  - Cache functions now use proper `sys_*` functions.
  - Renamed default RAM region from `SRAM` to `RAM`.
- ARM64

  - Implemented ASID support for ARM64 MMU
- RISC-V

  - Converted `CONFIG_MP_NUM_CPUS` to
    [`CONFIG_MP_MAX_NUM_CPUS`](../kconfig.md#CONFIG_MP_MAX_NUM_CPUS "CONFIG_MP_MAX_NUM_CPUS").
  - Added support for hardware register stacking/unstacking during ISRs and
    exceptions.
  - Added support for overriding [`arch_irq_lock()`](../doxygen/html/group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38),
    [`arch_irq_unlock()`](../doxygen/html/group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05) and [`arch_irq_unlocked()`](../doxygen/html/group__arch-irq.md#ga1b827afafc622d412962f568b78726dc).
  - Zephyr CPU number is now decoupled from the hart ID.
  - Secondary boot code is no longer included when
    [`CONFIG_MP_MAX_NUM_CPUS`](../kconfig.md#CONFIG_MP_MAX_NUM_CPUS "CONFIG_MP_MAX_NUM_CPUS") equals `1`.
  - IPIs are no longer hardcoded to `z_sched_ipi()`.
  - Implemented an on-demand context switching algorithm for thread FPU
    accesses.
  - Enabled booting from non-zero indexed RISC-V harts with
    [`CONFIG_RV_BOOT_HART`](../kconfig.md#CONFIG_RV_BOOT_HART "CONFIG_RV_BOOT_HART").
  - Hart IDs are now mapped to Zephyr CPUs with the devicetree.
  - Added a workaround for `MTVAL` not updating properly on QEMU-based
    platforms.

## Bluetooth

- Audio

  - Refactored the handling of extended and periodic advertising in the BAP
    broadcast source.
  - Implemented the Common Audio Profile initiator role.
  - Added support for Broadcast source subgroup and BIS codec configuration.
  - Renamed the CSI and VCP functionality to use the “P” postfix for profile
    instead of “S” for service.
  - Added a broadcast source metadata update function.
  - Added (un)binding of audio ISO structs to Audio Streams.
  - Added support for encrypted broadcast.
  - Added the ability to change the supported contexts in PACS.
  - Improved stream coupling for CIS as the unicast client
  - Added broadcast source metadata update function
  - Added packing to unicast group create
  - Added packing field to broadcast source
  - Renamed BASS and BASS client to BAP Scan Delegator and BPA Broadcast Assistant
  - Added support for multiple subgroups for BAP broadcast sink
  - Replaced capabilities API with PACS
- Host

  - Added a new `BT_CONN_INTERVAL_TO_US` utility macro.
  - Made the HCI fragmentation logic asynchronous, thus fixing a long-standing
    potential deadlock between data and control procedures.
  - Added the local advertising address to [`bt_le_ext_adv_get_info()`](../doxygen/html/group__bt__gap.md#gac06c9f55cf1da46e0d64b4d9af984ecb).
  - Improved the implementation of [`bt_disable()`](../doxygen/html/group__bt__gap.md#ga0a58e5a050170e84a80f8d5bb3516ec7) to handle additional
    edge cases.
  - Removed all Bluetooth-specific logging macros and functionality, switching
    instead to the OS-wide ones.
  - Added a new [`bt_le_per_adv_sync_lookup_index()`](../doxygen/html/group__bt__gap.md#ga59532b37412b1b93f81cf5cc1bab0534) function.
  - Fixed missing calls to bt\_le\_per\_adv\_sync\_cb.term when deleting a periodic
    advertising sync object.
  - Added local advertising address to bt\_le\_ext\_adv\_info.
  - Added the printing of function names by default when logging.
  - Changed the policy for advertising restart after disconnection, which is now
    done only for connections in the peripheral role.
  - Added a guard to prevent bonding to the same device more than once.
  - Refactored crypto functionality from SMP into its own folder, and added the
    h8 crypto function.
  - Changed the behavior when receiving an L2CAP K-frame larger than the MPS,
    disconnecting instead of truncating it.
  - Added a new `BT_ID_ALLOW_UNAUTH_OVERWRITE` that allows
    unauthorized bond overrides with multiple identities.
  - Added support for the object calculate checksum feature in OTS.
  - Changed back the semantics of `BT_PRIVACY` to refer to local
    RPA address generation.
  - Modified the SMP behavior when outside a pairing procedure. The stack no
    longer sends unnecessary Pairing Failed PDUs in that state.
  - ISO: Changed ISO seq\_num to 16-bit
- Mesh

  - Changed the default advertiser to be extended advertiser.
  - Made the provisioning feature set dynamic.
  - Made the maximum number of simultaneous Bluetooth connections that the mesh
    stack can use configurable via `BT_MESH_MAX_CONN`.
  - Changed the advertising duration calculation to avoid imprecise estimations.
  - Added the `BT_MESH_FRIEND_ADV_LATENCY` Kconfig option.
- Controller

  - Implemented the Read/Write Connection Accept Timeout HCI commands.
  - Implemented the Sleep Clock Accuracy Update procedure.
  - Implemented additional ISO-related HCI commands.
  - Implemented ISO-AL SDU buffering and PDU release timeout.
  - Added support for handling fragmented AD without chaining PDUs.
  - Added support for multiple memory pools for advertising PDUs
  - Added support for retrying the automatic peripheral connection parameter
    update.
  - Added support for deferring anchor points moves using an external hook.
  - Added a new `LL_ASSERT_MSG` macro for verbose assertions.
  - Added long control PDU support.
  - Added support for Broadcast ISO encryption.
  - Added support for central CIS/CIG, including ULL and Nordic LLL.
  - Added support for peripheral CIS/CIG in the Nordic LLL.
  - Added the `BT_CTLR_SLOT_RESERVATION_UPDATE` Kconfig option.
  - Integrated ISOAL for ISO broadcast.

## Boards & SoC Support

- Added support for these SoC series:

  - Atmel SAMC20, SAMC21
  - Atmel SAME70Q19
  - GigaDevice GD32L23X
  - GigaDevice GD32A50X
  - NXP S32Z2/E2
- Made these changes in other SoC series:

  - STM32F1: USB Prescaler configuration is now expected to be done using
    :dtcompatible: st,stm32f1-pll-clock: `usbpre`
    or :dtcompatible: st,stm32f105-pll-clock: `otgfspre` properties.
  - STM32F7/L4: Now supports configuring MCO.
  - STM32G0: Now supports FDCAN
  - STM32G4: Now supports power management (STOP0 and STOP1 low power modes).
  - STM32H7: Now supports PLL2, USB OTG HS and ULPI PHY.
  - STM32L5: Now supports RTC based [Counter](../hardware/peripherals/counter.md#counter-api).
  - STM32U5: Now supports [Crypto APIs](../services/crypto/api/index.md#crypto-api) through AES device.
  - STM32F7/L4: Now supports configuring MCO.
- Changes for ARC boards:

  - Multiple fixes to `mdb-hw` and `mdb-nsim` west runners to improve usability
  - Added `nsim_em11d` board with DSP features (XY DSP with AGU and XY memory)
  - Fixed cy8c95xx I2C GPIO port init on HSDK board
  - Added SPI flash support on EM starter kit board
  - Multiple fixes for nSIM platform - configuration: adding of missing HW features or
    configurations sync
  - Improved creg\_gpio platform driver - add pin\_configure API
  - Added separate QEMU config `qemu_arc_hs_xip` for XIP testing
  - Added `nsim_hs_sram`, `nsim_hs_flash_xip` nSIM platforms to verify various memory models
  - nSIM board documentation overhaul
- Added support for these ARM boards:

  - Adafruit ItsyBitsy nRF52840 Express
  - Adafruit KB2040
  - Atmel atsamc21n\_xpro
  - GigaDevice GD32L233R-EVAL
  - GigaDevice GD32A503V-EVAL
  - nRF5340 Audio DK
  - Sparkfun pro micro RP2040
  - Arduino Portenta H7
  - SECO JUNO SBC-D23 (STM32F302)
  - ST Nucleo G070RB
  - ST Nucleo L4A6ZG
  - NXP X-S32Z27X-DC (DC2)
- Added support for these ARM64 boards:

  - i.MX93 (Cortex-A) EVK board
  - Khadas Edge-V board
  - QEMU Virt KVM
- Added support for these X86 boards:

  - Intel Raptor Lake CRB
- Added support for these RISC-V boards:

  - Added LCD support for `longan_nano` board.
- Made these changes in ARM boards:

  - sam4s\_xplained: Enabled PWM
  - sam\_e70\_xplained: Added DMA devicetree entries for SPI
  - sam\_v71\_xult: Added DMA devicetree entries for SPI
  - tdk\_robokit1: Added DMA devicetree entries for SPI
  - The scratch partition has been removed for the following Nordic boards and
    flash used by this area re-assigned to other partitions to free up space
    and rely upon the swap-using-move algorithm in MCUboot (which does not
    suffer from the same faults or stuck image issues as swap-using-scratch
    does):
    `nrf21540dk_nrf52840`
    `nrf51dk_nrf51422`
    `nrf51dongle_nrf51422`
    `nrf52833dk_nrf52833`
    `nrf52840dk_nrf52811`
    `nrf52840dk_nrf52840`
    `nrf52840dongle_nrf52840`
    `nrf52dk_nrf52805`
    `nrf52dk_nrf52810`
    `nrf52dk_nrf52832`
    `nrf5340dk_nrf5340`
    `nrf9160dk_nrf52840`
    `nrf9160dk_nrf9160`

    Note that MCUboot and MCUboot image updates from pre-Zephyr 3.3 might be
    incompatible with Zephyr 3.3 onwards and vice versa.
  - The default console for the `nrf52840dongle_nrf52840` board has been
    changed from physical UART (which is not connected to anything on the
    board) to use USB CDC instead.
  - Forced configuration of FPU was removed from following boards:
    `stm32373c_eval`
    `stm32f3_disco`
  - On STM32 boards, configuration of USB, SDMMC and entropy devices that generally
    expect a 48MHz clock is now done using device tree. When available, HSI48 is enabled
    and configured as domain clock for these devices, otherwise PLL\_Q output or MSI is used.
    On some boards, previous PLL SAI configuration has been changed to above options,
    since PLL SAI cannot yet be configured using device tree.
- Made these changes in other boards:

  - The nrf52\_bsim (natively simulated nRF52 device with BabbleSim) now models
    a nRF52833 instead of a nRF52832 device
- Added support for these following shields:

  - Adafruit PCA9685
  - nPM6001 EK
  - nPM1100 EK
  - Semtech SX1262MB2DAS
  - Sparkfun MAX3421E

## Build system and infrastructure

- Code relocation

  - `zephyr_code_relocate` API has changed to accept a list of files to
    relocate and a location to place the files.
- Sysbuild

  - Issue with duplicate sysbuild image name causing an infinite cmake loop
    has been fixed.
  - Issue with board revision not being passed to sysbuild images has been
    fixed.
  - Application specific configurations of sysbuild controlled images.
- Userspace

  - Userspace option to disable using the `relax` linker option has been
    added.
- Tools

  - Static code analyser (SCA) tool support has been added.

## Drivers and Sensors

- ADC

  - STM32: Now Supports sequencing multiple channels into a single read.
  - Fixed a problem in [`ADC_CHANNEL_CFG_DT`](../doxygen/html/group__adc__interface.md#ga8d1f7d55c94fed3247c830a4569ab05e) that forced users to add
    artificial `input-positive` property in nodes related to ADC drivers that
    do not use configurable analog inputs when such drivers were used together
    with an ADC driver that uses such input configuration.
  - Added driver for TI CC13xx/CC26xx family.
  - Added driver for Infineon XMC4xxx family.
  - Added driver for ESP32 SoCs.
- Battery-backed RAM

  - STM32: Added driver to enable support for backup registers from RTC.
- CAN

  - Added RX overflow counter statistics support (STM32 bxCAN, Renesas R-Car,
    and NXP FlexCAN).
  - Added support for TWAI on ESP32-C3.
  - Added support for multiple MCP2515 driver instances.
  - Added Kvaser PCIcan driver and support for using it under QEMU.
  - Made the fake CAN test driver generally available.
  - Added support for compiling the Native Posix Linux CAN driver against Linux
    kernel headers prior to v5.14.
  - Removed the CONFIG\_CAN\_HAS\_RX\_TIMESTAMP and CONFIG\_CAN\_HAS\_CANFD Kconfig
    helper symbols.
- Clock control

  - STM32: HSI48 can now be configured using device tree.
- Counter

  - STM32 RTC based counter domain clock (LSE/SLI) should now be configured using device tree.
  - Added Timer based driver for GigaDevice GD32 SoCs.
  - Added NXP S32 System Timer Module driver.
- DAC

  - Added support for GigaDevice GD32 SoCs.
  - Added support for Espressif ESP32 SoCs.
- DFU

  - Removed `BOOT_TRAILER_IMG_STATUS_OFFS` in favor a two new functions;
    [`boot_get_area_trailer_status_offset()`](../doxygen/html/group__mcuboot__api.md#ga6fa12d4058bbb78b7d8f35b436f0009c) and [`boot_get_trailer_status_offset()`](../doxygen/html/group__mcuboot__api.md#ga7b4443f339f2935895f01dfb80c6b460)
- Disk

  - STM32 SD host controller clocks are now configured via devicetree.
  - Zephyr flash disks are now configured using the [`zephyr,flash-disk`](../build/dts/api/bindings/misc/zephyr%2Cflash-disk.md#std-dtcompatible-zephyr-flash-disk)
    devicetree binding
  - Flash disks can be marked as read only by setting the `read-only` property
    on the linked flash device partition.
- DMA

  - Adjusted incorrect dma1 clock source for GD32 gd32vf103 SoC.
  - Atmel SAM: Added support to select fixed or increment address mode when using
    peripherals to memory or memory to peripheral transfers.
  - STM32 DMA variable scope cleanups
  - Intel GPDMA linked list transfer descriptors appropriately aligned to 64 byte addresses
  - Intel GPDMA fixed bug in transfer configuration to initialize cfg\_hi and cfg\_lo
  - STM32 DMA Support for the STM32MP1 series
  - SAM XDMAC fixes to enable usage with SPI DMA transfers
  - Intel GPDMA fixed to return errors on dma stop
  - Intel GPDMA disabled interrupts when unneeded
  - Intel GPDMA fixed for register/ip ownership
  - STM32U5 GPDMA bug fix for busy flag
  - STM32U5 Suspend and resume features added
  - Intel GPDMA Report total bytes read/written (linear link position) in dma status
  - DMA API get attribute function added, added attributes for scatter/gather blocks available
    to Intel HDA and Intel GPDMA drivers.
  - Intel GPDMA Power management functionality added
  - Intel HDA Power management functionality added
  - GD32 Slot used for peripheral selection
  - GD32 memory to memory support added
  - ESP32C3 GDMA driver added
  - Intel HDA underrun/overrun (xrun) handling and reporting added
  - Intel GPDMA underrun/overrun (xrun) handling nad reporting added
  - DMA API start/stop are defined to be repeatable callable with test cases added.
    STM32 DMA, Intel HDA, and Intel GPDMA all comply with the contract after patches.
  - NXP EDMA Unused mutex removed
- EEPROM

  - Added fake EEPROM driver for testing purposes.
- Ethernet

  - STM32: Default Mac address configuration is now uid based. Optionally, user can
    configure it to be random or provide its own address using device tree.
  - STM32: Added support for STM32Cube HAL Ethernet API V2 on F4/F7/H7. By default disabled,
    it can be enabled with [`CONFIG_ETH_STM32_HAL_API_V2`](../kconfig.md#CONFIG_ETH_STM32_HAL_API_V2 "CONFIG_ETH_STM32_HAL_API_V2").
  - STM32: Added ethernet support on STM32F107 devices.
  - STM32: Now supports multicast hash filtering in the MAC. It can be enabled using
    [`CONFIG_ETH_STM32_MULTICAST_FILTER`](../kconfig.md#CONFIG_ETH_STM32_MULTICAST_FILTER "CONFIG_ETH_STM32_MULTICAST_FILTER").
  - STM32: Now supports statistics logging through [`CONFIG_NET_STATISTICS_ETHERNET`](../kconfig.md#CONFIG_NET_STATISTICS_ETHERNET "CONFIG_NET_STATISTICS_ETHERNET").
    Requires use of HAL Ethernet API V2.
- Flash

  - Flash: Moved CONFIG\_FLASH\_FLEXSPI\_XIP into the SOC level due to the flexspi clock initialization occurring in the SOC level.
  - NRF: Added CONFIG\_SOC\_FLASH\_NRF\_TIMEOUT\_MULTIPLIER to allow tweaking the timeout of flash operations.
  - spi\_nor: Added property mxicy,mx25r-power-mode to jedec,spi-nor binding for controlling low power/high performance mode on Macronix MX25R\* Ultra Low Power flash devices.
  - spi\_nor: Added check if the flash is busy during init. This used to cause
    the flash device to be unavailable until the system was restarted. The fix
    waits for the flash to become ready before continuing. In cases where a
    full flash erase was started before a restart, this might result in several
    minutes of waiting time (depending on flash size and erase speed).
  - rpi\_pico: Added a flash driver for the Raspberry Pi Pico platform.
  - STM32 OSPI: sfdp-bfp table and jedec-id can now be read from device tree and override
    the flash content if required.
  - STM32 OSPI: Now supports DMA transfer on STM32U5.
  - STM32: Flash driver was revisited to simplify reuse of driver for new series, taking
    advantage of device tree compatibles.
- FPGA

  - Added preliminary support for the Lattice iCE40.
  - Added Qomu board sample.
- GPIO

  - Atmel SAM: Added support to configure Open-Drain pins
  - Added driver for nPM6001 PMIC GPIOs
  - Added NXP S32 GPIO (SIUL2) driver
- hwinfo

  - Added hwinfo\_get\_device\_id for ESP32-C3
  - Added reset cause for iwdg and wwdg for STM32H7 and MP1
- I2C

  - SAM0 Fixed spurious trailing data by moving stop condition from thread into ISR
  - I2C Shell command adds ability to configure bus speed through i2c speed
  - ITE usage of instruction local memory support
  - NPCX bus recovery on transaction timeout
  - ITE log status of registers on transfer failure
  - ESP32 enabled configuring a hardware timeout to account for longer durations of clock stretching
  - ITE fixed bug where an operation was done outside of the driver mutex
  - NRFX TWIM Made transfer timeout configurable
  - DW Bug fix for clearing FIFO on initialization
  - NPCX simplified smb bank register usage
  - NXP LPI2C enabled target mode
  - NXP FlexComm Added semaphore for shared usage of bus
  - I2C Added support for dumping messages in the log for all transactions, reads and writes
  - STM32: Slave configuration now supports 10-bit addressing.
  - STM32: Now support power management. 3 modes supported: [`CONFIG_PM`](../kconfig.md#CONFIG_PM "CONFIG_PM"),
    [`CONFIG_PM_DEVICE`](../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE"), [`CONFIG_PM_DEVICE_RUNTIME`](../kconfig.md#CONFIG_PM_DEVICE_RUNTIME "CONFIG_PM_DEVICE_RUNTIME").
  - STM32: Domain clock can now be configured using device tree
- I3C

  - Added a new target device API [`i3c_target_tx_write()`](../doxygen/html/group__i3c__target__device.md#gafb5ebdfd5536ee265a3719beb8ae81dc) to
    explicit write to TX FIFO.
  - GETMRL and GETMWL are both optional in [`i3c_device_basic_info_get()`](../doxygen/html/group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8) as
    MRL and MWL are optional according to I3C specification.
  - Added a new driver to support Cadence I3C controller.
- Interrupt Controller

  - STM32: Driver configuration and initialization is now based on device tree
  - Added NXP S32 External Interrupt Controller (SIUL2) driver.
- IPM

  - ipm\_stm32\_ipcc: fixed an issue where interrupt mask is not cleaned correctly,
    resulting in infinite TXF interrupts.
- MBOX

  - Added NXP S32 Message Receive Unit (MRU) driver.
- PCIE

  - Support for accessing I/O BARs, which was previously removed, is back.
  - Added new API [`pcie_scan()`](../doxygen/html/group__pcie__host__interface.md#ga9a7b3c202f91d37fe8445d5016f4c6ab) to scan for devices.

    - This iterates through the buses and devices which are expected to
      exist. The old method was to try all possible combination of buses
      and devices to determine if there is a device there.
      `pci_init()` and `pcie_bdf_lookup()` have been updated to
      use this new API.
    - [`pcie_scan()`](../doxygen/html/group__pcie__host__interface.md#ga9a7b3c202f91d37fe8445d5016f4c6ab) also introduces a callback mechanism for when
      a new device has been discovered.
- Pin control

  - Common pin control properties are now defined at root level in a single
    file: [dts/bindings/pinctrl/pincfg-node.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/pinctrl/pincfg-node.yaml). Pin control
    bindings are expected to include it at the level they need. For example,
    drivers using the grouping representation approach need to include it at
    grandchild level, while drivers using the node approach need to include it
    at the child level. This change will only impact out-of-tree pin control
    drivers, since all in-tree drivers have been updated.
  - Added NXP S32 SIUL2 driver
  - Added Nuvoton NuMicro driver
  - Added Silabs Gecko driver
  - Added support for i.MX93 in the i.MX driver
  - Added support for GD32L23x/GD32A50x in the Gigadevice driver
- PWM

  - Atmel SAM: Added support to select pin polarity
  - Added driver for NXP PCA9685 LED controller
- Regulators

  - Completed an API overhaul so that devices like PMICs can be supported. The
    API now offers a clear and concise API that allows to perform the following
    operations:

    > - Enable/disable regulator output (reference counted)
    > - List supported voltages
    > - Get/set operating voltage
    > - Get/set maximum current
    > - Get/set operating mode
    > - Obtain errors, e.g. overcurrent.

    The devicetree part maintains compatibility with Linux bindings, for example,
    the following properties are well supported:

    > - `regulator-boot-on`
    > - `regulator-always-on`
    > - `regulator-min-microvolt`
    > - `regulator-max-microvolt`
    > - `regulator-min-microamp`
    > - `regulator-max-microamp`
    > - `regulator-allowed-modes`
    > - `regulator-initial-mode`

    A common driver class layer takes care of the common functionality so that
    driver implementations are kept simple. For example, allowed voltage ranges
    are verified before calling into the driver.

    An experimental parent API to configure DVS (Dynamic Voltage Scaling) has
    also been introduced.
  - Refactored NXP PCA9420 driver to align with the new API.
  - Added support for nPM6001 PMIC (LDO and BUCK converters).
  - Added support for nPM1100 PMIC (allows to dynamically change its mode).
  - Added a new test that allows to verify regulator output voltage using the
    ADC API.
  - Added a new test that checks API behavior provided we have a well-behaved
    driver.
- Reset

  - STM32: STM32 reset driver is now available. Devices reset line configuration should
    be done using device tree.
- SDHC

  - i.MX RT USDHC:

    - Support HS400 and HS200 mode. This mode is used with eMMC devices,
      and will enable high speed operation for those cards.
    - Support DMA operation on SOCs that do not support non-cacheable memory,
      such as the RT595. DMA will enable higher performance SD modes,
      such as HS400 and SDR104, to reliably transfer data using the
      SD host controller
- Sensor

  - Refactored all drivers to use [`SENSOR_DEVICE_DT_INST_DEFINE`](../doxygen/html/group__sensor__interface.md#ga284dc3b9018f14161dc0a2b6bed9a37e) to
    enable a new sensor info iterable section and shell command. See
    [`CONFIG_SENSOR_INFO`](../kconfig.md#CONFIG_SENSOR_INFO "CONFIG_SENSOR_INFO").
  - Refactored all sensor devicetree bindings to inherit new base sensor device
    properties in [dts/bindings/sensor/sensor-device.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/sensor/sensor-device.yaml).
  - Added sensor attribute support to the shell.
  - Added ESP32 and RaspberryPi Pico die temperature sensor drivers.
  - Added TDK InvenSense ICM42688 six axis IMU driver.
  - Added TDK InvenSense ICP10125 pressure and temperature sensor driver.
  - Added AMS AS5600 magnetic angle sensor driver.
  - Added AMS AS621x temperature sensor driver.
  - Added HZ-Grow R502A fingerprint sensor driver.
  - Enhanced FXOS8700, FXAS21002, and BMI270 drivers to support SPI in addition
    to I2C.
  - Enhanced ST LIS2DW12 driver to support free fall detection.
  - rpi\_pico: Added die temperature sensor driver.
  - STM32 family Quadrature Decoder driver was added. Only enabled on STM32F4 for now.
- Serial

  - Atmel SAM: UART/USART: Added support to configure driver at runtime
  - STM32: DMA now supported on STM32U5 series.
  - uart\_altera\_jtag: added support for Nios-V UART.
  - uart\_esp32: added support asynchronous operation.
  - uart\_gecko: added support for pinctrl.
  - uart\_mchp\_xec: now supports UART on MEC15xx SoC.
  - uart\_mcux\_flexcomm: added support for runtime configuration.
  - uart\_mcux\_lpuart: added support for RS-485.
  - uart\_numicro: uses pinctrl to configure UART pins.
  - uart\_pl011: added support for pinctrl.
  - uart\_rpi\_pico: added support for runtime configuration.
  - uart\_xmc4xxx: added support for interrupt so it can now be interrupt driven.
    Also added support for FIFO.
  - New UART drivers are added:

    - Cadence IP6528 UART.
    - NXP S32 LINFlexD UART.
    - OpenTitan UART.
    - QuickLogic USBserialport\_S3B.
- SPI

  - Added dma support for GD32 driver.
  - Atmel SAM:

    - Added support to transfers using DMA.
    - Added support to loopback mode for testing purposes.
  - Added NXP S32 SPI driver.
- Timer

  - Corrected CPU numbering on SMP RISC-V systems using the mtime device
  - Added support for OpenTitan’s privileged timer device to riscv\_machine\_timer
  - Refactored SYS\_CLOCK\_EXISTS such that it always matches the
    existence of a timer device in kconfig
  - Significant rework to nrf\_rtc\_timer with multiple fixes
  - Fixed prescaler correction in stm32\_lptim driver and fix race with auto-reload
- USB

  - STM32F1: Clock bus configuration is not done automatically by driver anymore.
    It is user’s responsibility to configure the proper bus prescaler using clock\_control
    device tree node to achieve a 48MHz bus clock. Note that, in most cases, core clock
    is 72MHz and default prescaler configuration is set to achieve 48MHz USB bus clock.
    Prescaler only needs to be configured manually when core clock is already 48MHz.
  - STM32 (non F1): Clock bus configuration is now expected to be done in device tree
    using `clocks` node property. When a dedicated HSI 48MHz clock is available on target,
    is it configured by default as the USB bus clock, but user has the ability to select
    another 48MHz clock source. When no HSI48 is available, a specific 48MHz bus clock
    source should be configured by user.
  - STM32: Now supports [`usb_dc_detach()`](../doxygen/html/group____usb__device__controller__api.md#ga062b4c8b618f2e964984786baf635a93) and [`usb_dc_wakeup_request()`](../doxygen/html/group____usb__device__controller__api.md#ga459110125c2a52da95b5b2c3c6fff096).
  - STM32: Vbus sensing is now supported and determined based on the presence of the
    hardware detection pin(s) in the device tree. E.g: pinctrl-0 = <&usb\_otg\_fs\_vbus\_pa9 …>;
  - RPi Pico: fixed buffer status handling, fixed infinite unhandled irq retriggers,
    fixed DATA PID toggle and control transfer handling.
  - NXP: Enabled high speed support, fixed endpoint buffer write operation.
  - nRF USBD: Removed HAL driver uninit on detach, fixed endpoints disable on
    USB stack disable.
  - Added new experimental USB device controller (UDC) API and implementation
    for nRF USBD, Kinetis USBFSOTG, and virtual controllers.
  - Added new experimental USB host controller (UDC) API and implementation
    for MAX3421E and virtual controllers.
- Watchdog

  - Added driver for nPM6001 PMIC Watchdog.
  - Added free watchdog driver for GigaDevice GD32 SoCs.
  - Added window watchdog driver for GigaDevice GD32 SoCs.
  - Added NXP S32 Software Watchdog Timer driver.

## Networking

- CoAP:

  - Implemented insertion of a CoAP option at arbitrary position.
- Ethernet:

  - Fixed AF\_PACKET/SOCK\_RAW/IPPROTO\_RAW sockets on top of Ethernet L2.
  - Added support for setting Ethernet MAC address with net shell.
  - Added check for return values of the driver start/stop routines when
    bringing Ethernet interface up.
  - Added `unknown_protocol` statistic for packets with unrecognized protocol
    field, instead of using `error` for this purpose.
  - Added NXP S32 NETC Ethernet driver.
- HTTP:

  - Reworked HTTP headers: moved methods to a separate header, added status
    response codes header and grouped HTTP headers in a subdirectory.
  - Used [`zsock_poll()`](../doxygen/html/group__bsd__sockets.md#ga518361903c9fac3766164d38243872e3) for HTTP timeout instead of a delayed work.
- ICMPv4:

  - Added support to autogenerate Echo Request payload.
- ICMPv6:

  - Added support to autogenerate Echo Request payload.
  - Fixed stats counting for ND packets.
- IEEE802154:

  - Improved short address support.
  - Improved IEEE802154 context thread safety.
  - Decoupled IEEE802154 parameters from [`net_pkt`](../doxygen/html/structnet__pkt.md) into
    `net_pkt_cb_ieee802154`.
  - Multiple other minor fixes/improvements.
- IPv4:

  - IPv4 packet fragmentation support has been added, this allows large packets
    to be split up before sending or reassembled during receive for packets that
    are larger than the network device MTU. This is disabled by default but can
    be enabled with [`CONFIG_NET_IPV4_FRAGMENT`](../kconfig.md#CONFIG_NET_IPV4_FRAGMENT "CONFIG_NET_IPV4_FRAGMENT").
  - Added support for setting/reading DSCP/ECN fields.
  - Fixed packet leak in IPv4 address auto-configuration procedure.
  - Added support for configuring IPv4 addresses with `net ipv4` shell
    command.
  - Zephyr now adds IGMP all systems 224.0.0.1 address to all IPv4 network
    interfaces by default.
- IPv6:

  - Made it possible to add route to router’s link local address.
  - Added support for setting/reading DSCP/ECN fields.
  - Improved test coverage for IPv6 fragmentation.
  - Added support for configuring IPv6 addresses with `net ipv6` shell
    command.
  - Added support for configuring IPv6 routes with `net route` shell
    command.
- LwM2M:

  - Renamed `LWM2M_RD_CLIENT_EVENT_REG_UPDATE_FAILURE` to
    `LWM2M_RD_CLIENT_EVENT_REG_TIMEOUT`. This event is now used in case
    of registration timeout.
  - Added new LwM2M APIs for historical data storage for LwM2M resource.
  - Updated LwM2M APIs to use `const` pointers when possible.
  - Added shell command to lock/unlock LwM2M registry.
  - Added shell command to enable historical data cache for a resource.
  - Switched to use `zsock_*` functions internally.
  - Added uCIFI LPWAN (ID 3412) object implementation.
  - Added BinaryAppDataContainer (ID 19) object implementation.
  - Deprecated `CONFIG_LWM2M_RD_CLIENT_SUPPORT`, as it’s now
    considered as an integral part of the LwM2M library.
  - Added support for SenML Object Link data type.
  - Fixed a bug causing incorrect ordering of the observation paths.
  - Deprecated string based LwM2M APIs. LwM2M APIs now use
    [`lwm2m_obj_path`](../doxygen/html/structlwm2m__obj__path.md) to represent object/resource paths.
  - Refactored `lwm2m_client` sample by splitting specific functionalities
    into separate modules.
  - Multiple other minor fixes within the LwM2M library.
- Misc:

  - Updated various networking test suites to use the new ztest API.
  - Added redirect support for `big_http_download` sample and updated the
    server URL for TLS variant.
  - Fixed memory leak in `net udp` shell command.
  - Fixed cloning of LL address for [`net_pkt`](../doxygen/html/structnet__pkt.md).
  - Added support for QoS and payload size setting in `net ping` shell
    command.
  - Added support for aborting `net ping` shell command.
  - Introduced carrier and dormant management on network interfaces. Separated
    interface administrative state from operational state.
  - Improved DHCPv4 behavior with multiple DHCPv4 servers in the network.
  - Fixed net\_mgmt event size calculation.
  - Added [`CONFIG_NET_LOOPBACK_MTU`](../kconfig.md#CONFIG_NET_LOOPBACK_MTU "CONFIG_NET_LOOPBACK_MTU") option to configure loopback
    interface MTU.
  - Reimplemented the IP/UDP/TCP checksum calculation to speed up the
    processing.
  - Removed [`CONFIG_NET_CONFIG_SETTINGS`](../kconfig.md#CONFIG_NET_CONFIG_SETTINGS "CONFIG_NET_CONFIG_SETTINGS") use from test cases to
    improve test execution on real platforms.
  - Added MQTT-SN library and sample.
  - Fixed variable buffer length configuration
    ([`CONFIG_NET_BUF_VARIABLE_DATA_SIZE`](../kconfig.md#CONFIG_NET_BUF_VARIABLE_DATA_SIZE "CONFIG_NET_BUF_VARIABLE_DATA_SIZE")).
  - Fixed IGMPv2 membership report destination address.
  - Added mutex protection for the connection list handling.
  - Separated user data pointer from FIFO reserved space in
    [`net_context`](../doxygen/html/structnet__context.md).
  - Added input validation for `net pkt` shell command.
- OpenThread:

  - Implemented PSA support for ECDSA API.
  - Fixed `otPlatRadioSetMacKey()` when asserts are disabled.
  - Deprecated `openthread_set_state_changed_cb()` in favour of more
    generic [`openthread_state_changed_cb_register()`](../doxygen/html/group__openthread.md#ga46471bc0ccdf1f953b81dd9720883327).
  - Implemented diagnostic GPIO commands.
- SNTP:

  - Switched to use `zsock_*` functions internally.
  - Fixed the library operation with IPv4 disabled.
- Sockets:

  - Fixed a possible memory leak on failed TLS socket creation.
- TCP:

  - Extended the default TCP out-of-order receive queue timeout to 2 seconds.
  - Reimplemented TCP ref counting, to prevent situation, where TCP connection
    context could be released prematurely.
- Websockets:

  - Reimplemented websocket receive routine to fix several issues.
  - Implemented proper websocket close procedure.
  - Fixed a bug where websocket would overwrite the mutex used by underlying TCP
    socket.
- Wi-Fi:

  - Added support for power save configuration.
  - Added support for regulatory domain configuration.
  - Added support for power save timeout configuration.
- zperf

  - Added option to set QoS for zperf.
  - Fixed out of order/lost packets statistics.
  - Defined a public API for the library to allow throughput measurement without shell enabled.
  - Added an option for asynchronous upload.

## USB

- New experimental USB support:

  - Added new USB device stack (device\_next), class implementation for CDC ACM and
    BT HCI USB transport layer.
  - Added initial support for USB host
- USB device stack (device):

  - Removed transfer cancellation on bus suspend.
  - Reworked disabling all endpoints on stack disable to allow re-enabling USB
    device stack.
  - Revised endpoint enable/disable on alternate setting.
  - Improved USB DFU support with WinUSB on Windows.
  - Added check to prevent recursive logging loop and allowed to send more than
    one byte using poll out in CDC ACM class implementation.
  - Corrected IAD and interface descriptors, removed unnecessary CDC descriptors,
    and fixed packet reception in RNDIS ethernet implementation.
  - Implemented cache synchronization after write operations in USB MSC class.

## Devicetree

### API

New general-purpose macros:

- [`DT_FOREACH_PROP_ELEM_SEP_VARGS`](../doxygen/html/group__devicetree-generic-foreach.md#ga29120ee8718b889273dc2649ab25438f)
- [`DT_FOREACH_PROP_ELEM_SEP`](../doxygen/html/group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)
- [`DT_INST_FOREACH_PROP_ELEM_SEP_VARGS`](../doxygen/html/group__devicetree-inst.md#ga41b9dfd3519809bfc3c1c500780d6a2d)
- [`DT_INST_FOREACH_PROP_ELEM_SEP`](../doxygen/html/group__devicetree-inst.md#ga08de2f0ba1a6ec395f198e06c5f52373)
- [`DT_INST_GPARENT`](../doxygen/html/group__devicetree-inst.md#ga5c68d697534682988a51a343abed05c9)
- [`DT_NODE_MODEL_BY_IDX_OR`](../doxygen/html/group__devicetree-generic-vendor.md#ga98a2ff981359088e2e995017791176b1)
- [`DT_NODE_MODEL_BY_IDX`](../doxygen/html/group__devicetree-generic-vendor.md#gae4bbd66726d930d878588f9bb9f4d500)
- [`DT_NODE_MODEL_HAS_IDX`](../doxygen/html/group__devicetree-generic-vendor.md#ga2ff3c91b22fae081d00d96964f465aa2)
- [`DT_NODE_MODEL_OR`](../doxygen/html/group__devicetree-generic-vendor.md#ga239f5fc9f6f33cf83e6c7ebfeef15d0f)

New special-purpose macros introduced for the GPIO hogs feature (see
[drivers/gpio/gpio\_hogs.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/gpio_hogs.c)):

- [`DT_GPIO_HOG_FLAGS_BY_IDX`](../doxygen/html/group__devicetree-gpio.md#gaed024e6acac49f591fe50cd43e8af14f)
- [`DT_GPIO_HOG_PIN_BY_IDX`](../doxygen/html/group__devicetree-gpio.md#gaf4ecdebbd433473f654f4b6859542af9)
- [`DT_NUM_GPIO_HOGS`](../doxygen/html/group__devicetree-gpio.md#ga0a4575c3750db76692fd0f817a169b50)

The following deprecated macros were removed:

- `DT_CHOSEN_ZEPHYR_ENTROPY_LABEL`
- `DT_CHOSEN_ZEPHYR_FLASH_CONTROLLER_LABEL`

### Bindings

New bindings:

> - Generic or vendor-independent:
>
>   - [`usb-c-connector`](../build/dts/api/bindings/usb-c/usb-c-connector.md#std-dtcompatible-usb-c-connector)
>   - [`usb-ulpi-phy`](../build/dts/api/bindings/phy/usb-ulpi-phy.md#std-dtcompatible-usb-ulpi-phy)
> - AMS AG (ams):
>
>   - [`ams,as5600`](../build/dts/api/bindings/sensor/ams%2Cas5600.md#std-dtcompatible-ams-as5600)
>   - [`ams,as6212`](../build/dts/api/bindings/sensor/ams%2Cas6212.md#std-dtcompatible-ams-as6212)
> - Synopsys, Inc. (formerly ARC International PLC) (arc):
>
>   - [`arc,xccm`](../build/dts/api/bindings/arc/arc%2Cxccm.md#std-dtcompatible-arc-xccm)
>   - [`arc,yccm`](../build/dts/api/bindings/arc/arc%2Cyccm.md#std-dtcompatible-arc-yccm)
> - ARM Ltd. (arm):
>
>   - [`arm,cortex-a55`](../build/dts/api/bindings/cpu/arm%2Ccortex-a55.md#std-dtcompatible-arm-cortex-a55)
>   - [`arm,ethos-u`](../build/dts/api/bindings/arm/arm%2Cethos-u.md#std-dtcompatible-arm-ethos-u)
> - ASPEED Technology Inc. (aspeed):
>
>   - [`aspeed,ast10x0-reset`](../build/dts/api/bindings/reset/aspeed%2Cast10x0-reset.md#std-dtcompatible-aspeed-ast10x0-reset)
> - Atmel Corporation (atmel):
>
>   - `atmel,samc2x-gclk`
>   - `atmel,samc2x-mclk`
> - Bosch Sensortec GmbH (bosch):
>
>   - [`bosch,bmi270`](../build/dts/api/compatibles/bosch%2Cbmi270.md#std-dtcompatible-bosch-bmi270)
>   - [`bosch,bmi270`](../build/dts/api/compatibles/bosch%2Cbmi270.md#std-dtcompatible-bosch-bmi270)
> - Cadence Design Systems Inc. (cdns):
>
>   - [`cdns,i3c`](../build/dts/api/bindings/i3c/cdns%2Ci3c.md#std-dtcompatible-cdns-i3c)
>   - [`cdns,uart`](../build/dts/api/bindings/serial/cdns%2Cuart.md#std-dtcompatible-cdns-uart)
> - Espressif Systems (espressif):
>
>   - [`espressif,esp32-adc`](../build/dts/api/bindings/adc/espressif%2Cesp32-adc.md#std-dtcompatible-espressif-esp32-adc)
>   - [`espressif,esp32-dac`](../build/dts/api/bindings/dac/espressif%2Cesp32-dac.md#std-dtcompatible-espressif-esp32-dac)
>   - [`espressif,esp32-eth`](../build/dts/api/bindings/ethernet/espressif%2Cesp32-eth.md#std-dtcompatible-espressif-esp32-eth)
>   - [`espressif,esp32-gdma`](../build/dts/api/bindings/dma/espressif%2Cesp32-gdma.md#std-dtcompatible-espressif-esp32-gdma)
>   - [`espressif,esp32-mdio`](../build/dts/api/bindings/mdio/espressif%2Cesp32-mdio.md#std-dtcompatible-espressif-esp32-mdio)
>   - [`espressif,esp32-temp`](../build/dts/api/bindings/sensor/espressif%2Cesp32-temp.md#std-dtcompatible-espressif-esp32-temp)
> - GigaDevice Semiconductor (gd):
>
>   - `gd,gd322-dma` has new helper macros to easily setup the `dma-cells` property.
>   - [`gd,gd32-dma-v1`](../build/dts/api/bindings/dma/gd%2Cgd32-dma-v1.md#std-dtcompatible-gd-gd32-dma-v1)
>   - [`gd,gd32-fwdgt`](../build/dts/api/bindings/watchdog/gd%2Cgd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt)
>   - [`gd,gd32-wwdgt`](../build/dts/api/bindings/watchdog/gd%2Cgd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt)
> - Hangzhou Grow Technology Co., Ltd. (hzgrow):
>
>   - [`hzgrow,r502a`](../build/dts/api/bindings/sensor/hzgrow%2Cr502a.md#std-dtcompatible-hzgrow-r502a)
> - Infineon Technologies (infineon):
>
>   - [`infineon,xmc4xxx-adc`](../build/dts/api/bindings/adc/infineon%2Cxmc4xxx-adc.md#std-dtcompatible-infineon-xmc4xxx-adc)
>   - [`infineon,xmc4xxx-flash-controller`](../build/dts/api/bindings/flash_controller/infineon%2Cxmc4xxx-flash-controller.md#std-dtcompatible-infineon-xmc4xxx-flash-controller)
>   - [`infineon,xmc4xxx-intc`](../build/dts/api/bindings/interrupt-controller/infineon%2Cxmc4xxx-intc.md#std-dtcompatible-infineon-xmc4xxx-intc)
>   - [`infineon,xmc4xxx-nv-flash`](../build/dts/api/bindings/mtd/infineon%2Cxmc4xxx-nv-flash.md#std-dtcompatible-infineon-xmc4xxx-nv-flash)
> - Intel Corporation (intel):
>
>   - [`intel,adsp-communication-widget`](../build/dts/api/bindings/misc/intel%2Cadsp-communication-widget.md#std-dtcompatible-intel-adsp-communication-widget)
>   - [`intel,adsp-dfpmcch`](../build/dts/api/bindings/dfpmcch/intel%2Cadsp-dfpmcch.md#std-dtcompatible-intel-adsp-dfpmcch)
>   - [`intel,adsp-dfpmccu`](../build/dts/api/bindings/dfpmccu/intel%2Cadsp-dfpmccu.md#std-dtcompatible-intel-adsp-dfpmccu)
>   - [`intel,adsp-mem-window`](../build/dts/api/bindings/memory-window/intel%2Cadsp-mem-window.md#std-dtcompatible-intel-adsp-mem-window)
>   - [`intel,adsp-sha`](../build/dts/api/bindings/crypto/intel%2Cadsp-sha.md#std-dtcompatible-intel-adsp-sha)
>   - [`intel,adsp-timer`](../build/dts/api/bindings/timer/intel%2Cadsp-timer.md#std-dtcompatible-intel-adsp-timer)
>   - [`intel,hda-dai`](../build/dts/api/bindings/hda/intel%2Chda-dai.md#std-dtcompatible-intel-hda-dai)
>   - [`intel,raptor-lake`](../build/dts/api/bindings/cpu/intel%2Craptor-lake.md#std-dtcompatible-intel-raptor-lake)
> - InvenSense Inc. (invensense):
>
>   - [`invensense,icm42688`](../build/dts/api/bindings/sensor/invensense%2Cicm42688.md#std-dtcompatible-invensense-icm42688)
>   - `invensense,icp10125`
> - ITE Tech. Inc. (ite):
>
>   - [`ite,it8xxx2-espi`](../build/dts/api/bindings/espi/ite%2Cit8xxx2-espi.md#std-dtcompatible-ite-it8xxx2-espi)
>   - [`ite,it8xxx2-gpiokscan`](../build/dts/api/bindings/gpio/ite%2Cit8xxx2-gpiokscan.md#std-dtcompatible-ite-it8xxx2-gpiokscan)
>   - [`ite,it8xxx2-ilm`](../build/dts/api/bindings/memory-controllers/ite%2Cit8xxx2-ilm.md#std-dtcompatible-ite-it8xxx2-ilm)
>   - [`ite,it8xxx2-shi`](../build/dts/api/bindings/shi/ite%2Cit8xxx2-shi.md#std-dtcompatible-ite-it8xxx2-shi)
>   - [`ite,it8xxx2-usbpd`](../build/dts/api/bindings/usb-c/ite%2Cit8xxx2-usbpd.md#std-dtcompatible-ite-it8xxx2-usbpd)
> - Kvaser (kvaser):
>
>   - [`kvaser,pcican`](../build/dts/api/bindings/can/kvaser%2Cpcican.md#std-dtcompatible-kvaser-pcican)
> - Lattice Semiconductor (lattice):
>
>   - [`lattice,ice40-fpga`](../build/dts/api/bindings/fpga/lattice%2Cice40-fpga.md#std-dtcompatible-lattice-ice40-fpga)
> - lowRISC Community Interest Company (lowrisc):
>
>   - `lowrisc,machine-timer`
>   - [`lowrisc,opentitan-uart`](../build/dts/api/bindings/serial/lowrisc%2Copentitan-uart.md#std-dtcompatible-lowrisc-opentitan-uart)
> - Maxim Integrated Products (maxim):
>
>   - [`maxim,max3421e_spi`](../build/dts/api/bindings/usb/maxim%2Cmax3421e_spi.md#std-dtcompatible-maxim-max3421e_spi)
> - Microchip Technology Inc. (microchip):
>
>   - [`microchip,xec-bbled`](../build/dts/api/bindings/led/microchip%2Cxec-bbled.md#std-dtcompatible-microchip-xec-bbled)
>   - [`microchip,xec-ecs`](../build/dts/api/bindings/hwinfo/microchip%2Cxec-ecs.md#std-dtcompatible-microchip-xec-ecs)
>   - [`microchip,xec-espi-saf-v2`](../build/dts/api/bindings/espi/microchip%2Cxec-espi-saf-v2.md#std-dtcompatible-microchip-xec-espi-saf-v2)
>   - `microchip,xec-qmspi-full-duplex`
> - Nordic Semiconductor (nordic):
>
>   - [`nordic,npm1100`](../build/dts/api/bindings/regulator/nordic%2Cnpm1100.md#std-dtcompatible-nordic-npm1100)
>   - [`nordic,npm6001`](../build/dts/api/bindings/mfd/nordic%2Cnpm6001.md#std-dtcompatible-nordic-npm6001)
>   - [`nordic,npm6001-gpio`](../build/dts/api/bindings/gpio/nordic%2Cnpm6001-gpio.md#std-dtcompatible-nordic-npm6001-gpio)
>   - [`nordic,npm6001-regulator`](../build/dts/api/bindings/regulator/nordic%2Cnpm6001-regulator.md#std-dtcompatible-nordic-npm6001-regulator)
>   - [`nordic,npm6001-wdt`](../build/dts/api/bindings/watchdog/nordic%2Cnpm6001-wdt.md#std-dtcompatible-nordic-npm6001-wdt)
> - Nuvoton Technology Corporation (nuvoton):
>
>   - `nuvoton,npcx-kscan`
>   - [`nuvoton,npcx-sha`](../build/dts/api/bindings/crypto/nuvoton%2Cnpcx-sha.md#std-dtcompatible-nuvoton-npcx-sha)
>   - [`nuvoton,npcx-shi`](../build/dts/api/bindings/shi/nuvoton%2Cnpcx-shi.md#std-dtcompatible-nuvoton-npcx-shi)
>   - [`nuvoton,numicro-gpio`](../build/dts/api/bindings/gpio/nuvoton%2Cnumicro-gpio.md#std-dtcompatible-nuvoton-numicro-gpio)
>   - [`nuvoton,numicro-pinctrl`](../build/dts/api/bindings/pinctrl/nuvoton%2Cnumicro-pinctrl.md#std-dtcompatible-nuvoton-numicro-pinctrl)
> - NXP Semiconductors (nxp):
>
>   - `nxp,css-v2`
>   - [`nxp,fxas21002`](../build/dts/api/compatibles/nxp%2Cfxas21002.md#std-dtcompatible-nxp-fxas21002)
>   - [`nxp,fxos8700`](../build/dts/api/compatibles/nxp%2Cfxos8700.md#std-dtcompatible-nxp-fxos8700)
>   - [`nxp,imx-flexspi-aps6408l`](../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-aps6408l.md#std-dtcompatible-nxp-imx-flexspi-aps6408l)
>   - [`nxp,imx-flexspi-s27ks0641`](../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-s27ks0641.md#std-dtcompatible-nxp-imx-flexspi-s27ks0641)
>   - `nxp,imx-mu-rev2`
>   - [`nxp,imx93-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Cimx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl)
>   - [`nxp,mcux-qdec`](../build/dts/api/bindings/sensor/nxp%2Cmcux-qdec.md#std-dtcompatible-nxp-mcux-qdec)
>   - [`nxp,mcux-xbar`](../build/dts/api/bindings/arm/nxp%2Cmcux-xbar.md#std-dtcompatible-nxp-mcux-xbar)
>   - [`nxp,pca9420`](../build/dts/api/bindings/regulator/nxp%2Cpca9420.md#std-dtcompatible-nxp-pca9420)
>   - [`nxp,pca9685-pwm`](../build/dts/api/bindings/pwm/nxp%2Cpca9685.md#std-dtcompatible-nxp-pca9685-pwm)
>   - `nxp,pcf8574`
>   - [`nxp,pdcfg-power`](../build/dts/api/bindings/power/nxp%2Cpdcfg-power.md#std-dtcompatible-nxp-pdcfg-power)
>   - [`nxp,s32-gpio`](../build/dts/api/bindings/gpio/nxp%2Cs32-gpio.md#std-dtcompatible-nxp-s32-gpio)
>   - [`nxp,s32-linflexd`](../build/dts/api/bindings/serial/nxp%2Cs32-linflexd.md#std-dtcompatible-nxp-s32-linflexd)
>   - [`nxp,s32-mru`](../build/dts/api/bindings/mbox/nxp%2Cs32-mru.md#std-dtcompatible-nxp-s32-mru)
>   - [`nxp,s32-netc-emdio`](../build/dts/api/bindings/mdio/nxp%2Cs32-netc-emdio.md#std-dtcompatible-nxp-s32-netc-emdio)
>   - [`nxp,s32-netc-psi`](../build/dts/api/bindings/ethernet/nxp%2Cs32-netc-psi.md#std-dtcompatible-nxp-s32-netc-psi)
>   - [`nxp,s32-netc-vsi`](../build/dts/api/bindings/ethernet/nxp%2Cs32-netc-vsi.md#std-dtcompatible-nxp-s32-netc-vsi)
>   - [`nxp,s32-siul2-eirq`](../build/dts/api/bindings/interrupt-controller/nxp%2Cs32-siul2-eirq.md#std-dtcompatible-nxp-s32-siul2-eirq)
>   - [`nxp,s32-spi`](../build/dts/api/bindings/spi/nxp%2Cs32-spi.md#std-dtcompatible-nxp-s32-spi)
>   - [`nxp,s32-swt`](../build/dts/api/bindings/watchdog/nxp%2Cs32-swt.md#std-dtcompatible-nxp-s32-swt)
>   - [`nxp,s32-sys-timer`](../build/dts/api/bindings/counter/nxp%2Cs32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer)
>   - [`nxp,s32ze-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Cs32ze-pinctrl.md#std-dtcompatible-nxp-s32ze-pinctrl)
> - OpenThread (openthread):
>
>   - [`openthread,config`](../build/dts/api/bindings/options/openthread%2Cconfig.md#std-dtcompatible-openthread-config)
> - QuickLogic Corp. (quicklogic):
>
>   - [`quicklogic,usbserialport-s3b`](../build/dts/api/bindings/serial/quicklogic%2Cusbserialport-s3b.md#std-dtcompatible-quicklogic-usbserialport-s3b)
> - Raspberry Pi Foundation (raspberrypi):
>
>   - [`raspberrypi,pico-flash-controller`](../build/dts/api/bindings/flash_controller/raspberrypi%2Cpico-flash-controller.md#std-dtcompatible-raspberrypi-pico-flash-controller)
>   - [`raspberrypi,pico-temp`](../build/dts/api/bindings/sensor/raspberrrypi%2Cpico-temp.md#std-dtcompatible-raspberrypi-pico-temp)
> - Richtek Technology Corporation (richtek):
>
>   - [`richtek,rt1718s`](../build/dts/api/bindings/gpio/richtek%2Crt1718s.md#std-dtcompatible-richtek-rt1718s)
>   - [`richtek,rt1718s-gpio-port`](../build/dts/api/bindings/gpio/richtek%2Crt1718s-gpio-port.md#std-dtcompatible-richtek-rt1718s-gpio-port)
> - Smart Battery System (sbs):
>
>   - [`sbs,sbs-gauge-new-api`](../build/dts/api/bindings/fuel-gauge/sbs%2Csbs-gauge-new-api.md#std-dtcompatible-sbs-sbs-gauge-new-api)
> - Silicon Laboratories (silabs):
>
>   - [`silabs,gecko-pinctrl`](../build/dts/api/bindings/pinctrl/silabs%2Cgecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl)
>   - [`silabs,gecko-stimer`](../build/dts/api/bindings/rtc/silabs%2Cgecko-stimer.md#std-dtcompatible-silabs-gecko-stimer)
> - Synopsys, Inc. (snps):
>
>   - [`snps,ethernet-cyclonev`](../build/dts/api/bindings/ethernet/snps%2Cethernet-cyclonev.md#std-dtcompatible-snps-ethernet-cyclonev)
> - SparkFun Electronics (sparkfun):
>
>   - [`sparkfun,pro-micro-gpio`](../build/dts/api/bindings/gpio/sparkfun-pro-micro-header.md#std-dtcompatible-sparkfun-pro-micro-gpio)
> - STMicroelectronics (st):
>
>   - [`st,stm32-bbram`](../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram)
>   - [`st,stm32-qdec`](../build/dts/api/bindings/sensor/st%2Cstm32-qdec.md#std-dtcompatible-st-stm32-qdec)
>   - [`st,stm32-rcc-rctl`](../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl)
>   - [`st,stm32wb-rf`](../build/dts/api/bindings/bluetooth/st%2Cstm32wb-ble-rf.md#std-dtcompatible-st-stm32wb-rf)
> - Texas Instruments (ti):
>
>   - [`ti,cc13xx-cc26xx-adc`](../build/dts/api/bindings/adc/ti%2Ccc13xx-cc26xx-adc.md#std-dtcompatible-ti-cc13xx-cc26xx-adc)
>   - [`ti,cc13xx-cc26xx-watchdog`](../build/dts/api/bindings/watchdog/ti%2Ccc13xx-cc26xx-watchdog.md#std-dtcompatible-ti-cc13xx-cc26xx-watchdog)
>   - [`ti,tca6424a`](../build/dts/api/bindings/gpio/ti%2Ctca6424a.md#std-dtcompatible-ti-tca6424a)
> - A stand-in for a real vendor which can be used in examples and tests (vnd):
>
>   - `vnd,emul-tester`
> - Zephyr-specific binding (zephyr):
>
>   - `zephyr,ec-host-cmd-periph-espi`
>   - [`zephyr,fake-can`](../build/dts/api/bindings/can/zephyr%2Cfake-can.md#std-dtcompatible-zephyr-fake-can)
>   - [`zephyr,fake-eeprom`](../build/dts/api/bindings/mtd/zephyr%2Cfake-eeprom.md#std-dtcompatible-zephyr-fake-eeprom)
>   - [`zephyr,fake-regulator`](../build/dts/api/bindings/regulator/zephyr%2Cfake-regulator.md#std-dtcompatible-zephyr-fake-regulator)
>   - [`zephyr,flash-disk`](../build/dts/api/bindings/misc/zephyr%2Cflash-disk.md#std-dtcompatible-zephyr-flash-disk)
>   - [`zephyr,gpio-emul-sdl`](../build/dts/api/bindings/gpio/zephyr%2Cgpio-emul-sdl.md#std-dtcompatible-zephyr-gpio-emul-sdl)
>   - `zephyr,gpio-keys`
>   - [`zephyr,ipc-icmsg-me-follower`](../build/dts/api/bindings/ipc/zephyr%2Cipc-icmsg-me-follower.md#std-dtcompatible-zephyr-ipc-icmsg-me-follower)
>   - [`zephyr,ipc-icmsg-me-initiator`](../build/dts/api/bindings/ipc/zephyr%2Cipc-icmsg-me-initiator.md#std-dtcompatible-zephyr-ipc-icmsg-me-initiator)
>   - [`zephyr,mmc-disk`](../build/dts/api/bindings/sd/zephyr%2Cmmc-disk.md#std-dtcompatible-zephyr-mmc-disk)
>   - [`zephyr,psa-crypto-rng`](../build/dts/api/bindings/rng/zephyr%2Cpsa-crypto-rng.md#std-dtcompatible-zephyr-psa-crypto-rng)
>   - [`zephyr,udc-virtual`](../build/dts/api/bindings/usb/zephyr%2Cudc-virtual.md#std-dtcompatible-zephyr-udc-virtual)
>   - [`zephyr,uhc-virtual`](../build/dts/api/bindings/usb/zephyr%2Cuhc-virtual.md#std-dtcompatible-zephyr-uhc-virtual)
>   - [`zephyr,usb-c-vbus-adc`](../build/dts/api/bindings/usb-c/zephyr%2Cusb-c-vbus-adc.md#std-dtcompatible-zephyr-usb-c-vbus-adc)

Removed bindings:

> - Generic or vendor-independent:
>
>   - `regulator-pmic`
> - Intel Corporation (intel):
>
>   - `intel,adsp-lps`
> - NXP Semiconductors (nxp):
>
>   - `nxp,imx-flexspi-hyperram`
> - STMicroelectronics (st):
>
>   - `st,stm32f0-flash-controller`
>   - `st,stm32f3-flash-controller`
>   - `st,stm32l0-flash-controller`
>   - `st,stm32l1-flash-controller`
>   - `st,stm32u5-flash-controller`

Modified bindings:

> - Generic or vendor-independent:
>
>   - All sensor devices now have a `friendly-name` property,
>     which is a human-readable string describing the sensor.
>     See [dts/bindings/sensor/sensor-device.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/sensor/sensor-device.yaml)
>     for more information.
>   - All DMA controller devices have had their `dma-buf-alignment`
>     properties renamed to `dma-buf-addr-alignment`.
>
>     Additionally, all DMA controller devices have new
>     `dma-buf-size-alignment` and `dma-copy-alignment` properties.
>
>     See [dts/bindings/dma/dma-controller.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/dma/dma-controller.yaml) for
>     more information.
>   - [`ns16550`](../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550):
>
>     > - new property: `vendor-id`
>     > - new property: `device-id`
>     > - property `reg` is no longer required
>   - [`pci-host-ecam-generic`](../build/dts/api/bindings/pcie/host/pci-host-ecam-generic.md#std-dtcompatible-pci-host-ecam-generic):
>
>     > - new property: `interrupt-map-mask`
>     > - new property: `interrupt-map`
>     > - new property: `bus-range`
>   - [`regulator-fixed`](../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed):
>
>     > - removed property: `supply-gpios`
>     > - removed property: `vin-supply`
>   - [`gpio-keys`](../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys):
>
>     > - new property: `debounce-interval-ms`
> - Altera Corp. (altr):
>
>   - [`altr,jtag-uart`](../build/dts/api/bindings/serial/altr%2Cjtag-uart.md#std-dtcompatible-altr-jtag-uart):
>
>     > - new property: `write-fifo-depth`
> - ARM Ltd. (arm):
>
>   - [`arm,pl011`](../build/dts/api/bindings/serial/arm%2Cpl011.md#std-dtcompatible-arm-pl011):
>
>     > - new property: `pinctrl-0`
>     > - new property: `pinctrl-1`
>     > - new property: `pinctrl-2`
>     > - new property: `pinctrl-3`
>     > - new property: `pinctrl-4`
>     > - new property: `pinctrl-names`
> - Atmel Corporation (atmel):
>
>   - [`atmel,sam-pwm`](../build/dts/api/bindings/pwm/atmel%2Csam-pwm.md#std-dtcompatible-atmel-sam-pwm):
>
>     > - specifier cells for space “pwm” are now named: [‘channel’, ‘period’, ‘flags’] (old value: [‘channel’, ‘period’])
>     > - property `#pwm-cells` const value changed from 2 to 3
>   - [`atmel,sam-spi`](../build/dts/api/bindings/spi/atmel%2Csam-spi.md#std-dtcompatible-atmel-sam-spi):
>
>     > - new property: `loopback`
> - Espressif Systems (espressif):
>
>   - [`espressif,esp32-twai`](../build/dts/api/bindings/can/espressif%2Cesp32-twai.md#std-dtcompatible-espressif-esp32-twai):
>
>     > - property `clkout-divider` enum value changed from [1, 2, 4, 6, 8, 10, 12, 14] to None
>   - [`espressif,esp32-i2c`](../build/dts/api/bindings/i2c/espressif%2Cesp32-i2c.md#std-dtcompatible-espressif-esp32-i2c):
>
>     > - new property: `scl-timeout-us`
>   - [`espressif,esp32-spi`](../build/dts/api/bindings/spi/espressif%2Cesp32-spi.md#std-dtcompatible-espressif-esp32-spi):
>
>     > - new property: `dma-enabled`
>     > - new property: `dma-clk`
>     > - new property: `dma-host`
>     > - removed property: `dma`
> - GigaDevice Semiconductor (gd):
>
>   - [`gd,gd32-dma`](../build/dts/api/bindings/dma/gd%2Cgd32-dma.md#std-dtcompatible-gd-gd32-dma):
>
>     > - specifier cells for space “dma” are now named: [‘channel’, ‘config’] (old value: [‘channel’])
>     > - new property: `gd,mem2mem`
>     > - removed property: `resets`
>     > - removed property: `reset-names`
>     > - property `#dma-cells` const value changed from 1 to 2
> - ILI Technology Corporation (ILITEK) (ilitek):
>
>   - [`ilitek,ili9341`](../build/dts/api/bindings/display/ilitek%2Cili9341.md#std-dtcompatible-ilitek-ili9341) (on spi bus):
>
>     > - property `disctrl` default value changed from [10, 130, 39] to [10, 130, 39, 4]
> - Infineon Technologies (infineon):
>
>   - [`infineon,xmc4xxx-uart`](../build/dts/api/bindings/serial/infineon%2Cxmc4xxx-uart.md#std-dtcompatible-infineon-xmc4xxx-uart):
>
>     > - new property: `fifo-start-offset`
>     > - new property: `fifo-tx-size`
>     > - new property: `fifo-rx-size`
> - Intel Corporation (intel):
>
>   - [`intel,adsp-power-domain`](../build/dts/api/bindings/power-domain/intel%2Cadsp-power-domain.md#std-dtcompatible-intel-adsp-power-domain):
>
>     > - removed property: `lps`
>   - [`intel,e1000`](../build/dts/api/bindings/ethernet/intel%2Ce1000.md#std-dtcompatible-intel-e1000):
>
>     > - new property: `vendor-id`
>     > - new property: `device-id`
>     > - property `reg` is no longer required
>   - [`intel,dai-dmic`](../build/dts/api/bindings/dai/intel%2Cdai-dmic.md#std-dtcompatible-intel-dai-dmic):
>
>     > - new property: `fifo`
>     > - property `shim` type changed from array to int
> - ITE Tech. Inc. (ite):
>
>   - [`ite,it8xxx2-pinctrl-func`](../build/dts/api/bindings/pinctrl/ite%2Cit8xxx2-pinctrl-func.md#std-dtcompatible-ite-it8xxx2-pinctrl-func):
>
>     > - new property: `pp-od-mask`
>     > - new property: `pullup-mask`
>     > - new property: `gpio-group`
>     > - property `volt-sel-mask` is no longer required
>     > - property `func4-gcr` is no longer required
>     > - property `func3-en-mask` is no longer required
>     > - property `func3-gcr` is no longer required
>     > - property `func4-en-mask` is no longer required
>     > - property `volt-sel` is no longer required
> - JEDEC Solid State Technology Association (jedec):
>
>   - [`jedec,spi-nor`](../build/dts/api/bindings/mtd/jedec%2Cspi-nor.md#std-dtcompatible-jedec-spi-nor) (on spi bus):
>
>     > - new property: `mxicy,mx25r-power-mode`
> - Microchip Technology Inc. (microchip):
>
>   - [`microchip,xec-uart`](../build/dts/api/bindings/serial/microchip%2Cxec-uart.md#std-dtcompatible-microchip-xec-uart):
>
>     > - new property: `wakerx-gpios`
>   - [`microchip,xec-pcr`](../build/dts/api/bindings/clock/microchip%2Cxec-pcr.md#std-dtcompatible-microchip-xec-pcr):
>
>     > - new property: `clk32kmon-period-min`
>     > - new property: `clk32kmon-period-max`
>     > - new property: `clk32kmon-duty-cycle-var-max`
>     > - new property: `clk32kmon-valid-min`
>     > - new property: `xtal-enable-delay-ms`
>     > - new property: `pll-lock-timeout-ms`
>     > - new property: `clkmon-bypass`
>     > - new property: `internal-osc-disable`
>     > - new property: `pinctrl-0`
>     > - new property: `pinctrl-names`
>     > - new property: `pinctrl-1`
>     > - new property: `pinctrl-2`
>     > - new property: `pinctrl-3`
>     > - new property: `pinctrl-4`
>     > - property `interrupts` is no longer required
>   - [`microchip,xec-qmspi-ldma`](../build/dts/api/bindings/spi/microchip%2Cxec-qmspi-ldma.md#std-dtcompatible-microchip-xec-qmspi-ldma):
>
>     > - new property: `port-sel`
>     > - new property: `chip-select`
>     > - removed property: `port_sel`
>     > - removed property: `chip_select`
>     > - property `lines` enum value changed from None to [1, 2, 4]
> - Nordic Semiconductor (nordic):
>
>   - [`nordic,nrf21540-fem`](../build/dts/api/bindings/net/wireless/nordic%2Cnrf21540-fem.md#std-dtcompatible-nordic-nrf21540-fem):
>
>     > - new property: `supply-voltage-mv`
>   - [`nordic,qspi-nor`](../build/dts/api/bindings/mtd/nordic%2Cqspi-nor.md#std-dtcompatible-nordic-qspi-nor) (on qspi bus):
>
>     > - new property: `mxicy,mx25r-power-mode`
> - Nuvoton Technology Corporation (nuvoton):
>
>   - [`nuvoton,numicro-uart`](../build/dts/api/bindings/serial/nuvoton%2Cnumicro-uart.md#std-dtcompatible-nuvoton-numicro-uart):
>
>     > - new property: `pinctrl-0`
>     > - new property: `pinctrl-1`
>     > - new property: `pinctrl-2`
>     > - new property: `pinctrl-3`
>     > - new property: `pinctrl-4`
>     > - new property: `pinctrl-names`
>   - [`nuvoton,adc-cmp`](../build/dts/api/bindings/sensor/nuvoton%2Cadc-cmp.md#std-dtcompatible-nuvoton-adc-cmp):
>
>     > - new property: `status`
>     > - new property: `compatible`
>     > - new property: `reg`
>     > - new property: `reg-names`
>     > - new property: `interrupts`
>     > - new property: `interrupts-extended`
>     > - new property: `interrupt-names`
>     > - new property: `interrupt-parent`
>     > - new property: `label`
>     > - new property: `clocks`
>     > - new property: `clock-names`
>     > - new property: `#address-cells`
>     > - new property: `#size-cells`
>     > - new property: `dmas`
>     > - new property: `dma-names`
>     > - new property: `io-channel-names`
>     > - new property: `mboxes`
>     > - new property: `mbox-names`
>     > - new property: `wakeup-source`
>     > - new property: `power-domain`
> - NXP Semiconductors (nxp):
>
>   - `nxp,kinetis-lpuart`:
>
>     > - new property: `nxp,rs485-mode`
>     > - new property: `nxp,rs485-de-active-low`
>   - [`nxp,fxas21002`](../build/dts/api/compatibles/nxp%2Cfxas21002.md#std-dtcompatible-nxp-fxas21002) (on i2c bus):
>
>     > - new property: `reset-gpios`
>   - [`nxp,imx-pwm`](../build/dts/api/bindings/pwm/nxp%2Cimx-pwm.md#std-dtcompatible-nxp-imx-pwm):
>
>     > - specifier cells for space “pwm” are now named: [‘channel’, ‘period’, ‘flags’] (old value: [‘channel’, ‘period’])
>     > - new property: `nxp,prescaler`
>     > - new property: `nxp,reload`
>     > - property `#pwm-cells` const value changed from 2 to 3
>   - [`nxp,imx-usdhc`](../build/dts/api/bindings/sdhc/nxp%2Cimx-usdhc.md#std-dtcompatible-nxp-imx-usdhc):
>
>     > - new property: `mmc-hs200-1_8v`
>     > - new property: `mmc-hs400-1_8v`
>   - [`nxp,lpc-sdif`](../build/dts/api/bindings/sdhc/nxp%2Clpc-sdif.md#std-dtcompatible-nxp-lpc-sdif):
>
>     > - new property: `mmc-hs200-1_8v`
>     > - new property: `mmc-hs400-1_8v`
> - QEMU, a generic and open source machine emulator and virtualizer (qemu):
>
>   - [`qemu,ivshmem`](../build/dts/api/bindings/virtualization/qemu%2Civshmem.md#std-dtcompatible-qemu-ivshmem):
>
>     > - new property: `vendor-id`
>     > - new property: `device-id`
> - Renesas Electronics Corporation (renesas):
>
>   - [`renesas,smartbond-uart`](../build/dts/api/bindings/serial/renesas%2Csmartbond-uart.md#std-dtcompatible-renesas-smartbond-uart):
>
>     > - property `current-speed` enum value changed from [1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200, 230400, 460800, 921600, 1000000] to [4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200, 230400, 500000, 921600, 1000000, 2000000]
> - Silicon Laboratories (silabs):
>
>   - [`silabs,gecko-usart`](../build/dts/api/bindings/serial/silabs%2Cgecko-usart.md#std-dtcompatible-silabs-gecko-usart):
>
>     > - new property: `pinctrl-0`
>     > - new property: `pinctrl-1`
>     > - new property: `pinctrl-2`
>     > - new property: `pinctrl-3`
>     > - new property: `pinctrl-4`
>     > - new property: `pinctrl-names`
>     > - property `location-rx` is no longer required
>     > - property `location-tx` is no longer required
>     > - property `peripheral-id` is no longer required
>   - [`silabs,gecko-gpio-port`](../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port):
>
>     > - property `peripheral-id` is no longer required
>   - `silabs,gecko-spi-usart`:
>
>     > - new property: `pinctrl-0`
>     > - new property: `pinctrl-1`
>     > - new property: `pinctrl-2`
>     > - new property: `pinctrl-3`
>     > - new property: `pinctrl-4`
>     > - new property: `pinctrl-names`
>     > - property `location-clk` is no longer required
>     > - property `location-rx` is no longer required
>     > - property `location-tx` is no longer required
>     > - property `peripheral-id` is no longer required
> - Sitronix Technology Corporation (sitronix):
>
>   - [`sitronix,st7735r`](../build/dts/api/bindings/display/sitronix%2Cst7735r.md#std-dtcompatible-sitronix-st7735r) (on spi bus):
>
>     > - new property: `rgb-is-inverted`
> - Synopsys, Inc. (snps):
>
>   - [`snps,designware-i2c`](../build/dts/api/bindings/i2c/snps%2Cdesignware-i2c.md#std-dtcompatible-snps-designware-i2c):
>
>     > - new property: `vendor-id`
>     > - new property: `device-id`
>     > - property `reg` is no longer required
> - STMicroelectronics (st):
>
>   - [`st,stm32-adc`](../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc):
>
>     > - the `has-temp-channel`, `has-vref-channel` and
>     >   `has-vbat-channel` properties were respectively replaced by
>     >   `temp-channel`, `vref-channel` and `vbat-channel`
>   - [`st,stm32-ethernet`](../build/dts/api/bindings/ethernet/st%2Cstm32-ethernet.md#std-dtcompatible-st-stm32-ethernet):
>
>     > - the built-in driver for this compatible now supports the
>     >   `local-mac-address` and `zephyr,random-mac-address` properties
>     >   for setting MAC addresses, and the associated Kconfig options
>     >   (`CONFIG_ETH_STM32_HAL_RANDOM_MAC`,
>     >   `CONFIG_ETH_STM32_HAL_USER_STATIC_MAC`) are now deprecated
>   - [`st,stm32-qspi-nor`](../build/dts/api/bindings/flash_controller/st%2Cstm32-qspi-nor.md#std-dtcompatible-st-stm32-qspi-nor) (on qspi bus):
>
>     > - new property: `reset-cmd`
>     > - new property: `reset-cmd-wait`
>   - [`st,stm32-uart`](../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart):
>
>     > - new property: `resets`
>     > - new property: `tx-rx-swap`
>     > - new property: `reset-names`
>   - [`st,stm32-usart`](../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart):
>
>     > - new property: `resets`
>     > - new property: `tx-rx-swap`
>     > - new property: `reset-names`
>   - [`st,stm32-lpuart`](../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart):
>
>     > - new property: `resets`
>     > - new property: `tx-rx-swap`
>     > - new property: `reset-names`
>   - [`st,stm32-exti`](../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti):
>
>     > - new property: `num-lines`
>     > - new property: `line-ranges`
>     > - new property: `interrupt-controller`
>     > - new property: `#interrupt-cells`
>     > - property `interrupts` is now required
>     > - property `interrupt-names` is now required
>   - [`st,stm32-ospi`](../build/dts/api/bindings/ospi/st%2Cstm32-ospi.md#std-dtcompatible-st-stm32-ospi):
>
>     > - property `clock-names` is now required
>   - [`st,stm32f105-pll2-clock`](../build/dts/api/bindings/clock/st%2Cstm32f105-pll2-clock.md#std-dtcompatible-st-stm32f105-pll2-clock):
>
>     > - new property: `otgfspre`
>   - [`st,stm32f105-pll-clock`](../build/dts/api/bindings/clock/st%2Cstm32f105-pll-clock.md#std-dtcompatible-st-stm32f105-pll-clock):
>
>     > - new property: `otgfspre`
>   - [`st,stm32f100-pll-clock`](../build/dts/api/bindings/clock/st%2Cstm32f100-pll-clock.md#std-dtcompatible-st-stm32f100-pll-clock):
>
>     > - new property: `otgfspre`
>   - [`st,stm32f1-pll-clock`](../build/dts/api/bindings/clock/st%2Cstm32f1-pll-clock.md#std-dtcompatible-st-stm32f1-pll-clock):
>
>     > - property `usbpre` type changed from int to boolean
>   - [`st,stm32-lse-clock`](../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock):
>
>     > - new property: `lse-bypass`
>   - [`st,lis2dh12`](../build/dts/api/bindings/sensor/st%2Clis2dh12-i2c.md#std-dtcompatible-st-lis2dh12) (on i2c bus):
>
>     > - new property: `anym-no-latch`
>     > - new property: `anym-mode`
>   - [`st,lsm6dso`](../build/dts/api/compatibles/st%2Clsm6dso.md#std-dtcompatible-st-lsm6dso) (on i2c bus):
>
>     > - new property: `drdy-pulsed`
>   - [`st,lis2dh`](../build/dts/api/compatibles/st%2Clis2dh.md#std-dtcompatible-st-lis2dh) (on i2c bus):
>
>     > - new property: `anym-no-latch`
>     > - new property: `anym-mode`
>   - [`st,lsm303agr-accel`](../build/dts/api/compatibles/st%2Clsm303agr-accel.md#std-dtcompatible-st-lsm303agr-accel) (on spi bus):
>
>     > - new property: `anym-no-latch`
>     > - new property: `anym-mode`
>   - [`st,lis3dh`](../build/dts/api/bindings/sensor/st%2Clis3dh-i2c.md#std-dtcompatible-st-lis3dh) (on i2c bus):
>
>     > - new property: `anym-no-latch`
>     > - new property: `anym-mode`
>   - [`st,lsm6dso`](../build/dts/api/compatibles/st%2Clsm6dso.md#std-dtcompatible-st-lsm6dso) (on spi bus):
>
>     > - new property: `drdy-pulsed`
>   - [`st,lis2dw12`](../build/dts/api/compatibles/st%2Clis2dw12.md#std-dtcompatible-st-lis2dw12) (on spi bus):
>
>     > - new property: `odr`
>     > - new property: `ff-duration`
>     > - new property: `ff-threshold`
>   - [`st,lsm6dso32`](../build/dts/api/compatibles/st%2Clsm6dso32.md#std-dtcompatible-st-lsm6dso32) (on spi bus):
>
>     > - new property: `drdy-pulsed`
>   - [`st,lsm303dlhc-accel`](../build/dts/api/bindings/sensor/st%2Clsm303dlhc-accel.md#std-dtcompatible-st-lsm303dlhc-accel) (on i2c bus):
>
>     > - new property: `anym-no-latch`
>     > - new property: `anym-mode`
>   - [`st,lis2dh`](../build/dts/api/compatibles/st%2Clis2dh.md#std-dtcompatible-st-lis2dh) (on spi bus):
>
>     > - new property: `anym-no-latch`
>     > - new property: `anym-mode`
>   - [`st,lis2dw12`](../build/dts/api/compatibles/st%2Clis2dw12.md#std-dtcompatible-st-lis2dw12) (on i2c bus):
>
>     > - new property: `odr`
>     > - new property: `ff-duration`
>     > - new property: `ff-threshold`
>   - [`st,lsm303agr-accel`](../build/dts/api/compatibles/st%2Clsm303agr-accel.md#std-dtcompatible-st-lsm303agr-accel) (on i2c bus):
>
>     > - new property: `anym-no-latch`
>     > - new property: `anym-mode`
>   - [`st,lsm6dso32`](../build/dts/api/compatibles/st%2Clsm6dso32.md#std-dtcompatible-st-lsm6dso32) (on i2c bus):
>
>     > - new property: `drdy-pulsed`
>   - [`st,stm32-sdmmc`](../build/dts/api/bindings/mmc/st%2Cstm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc):
>
>     > - new property: `resets`
>     > - new property: `reset-names`
>   - [`st,stm32-ucpd`](../build/dts/api/bindings/tcpc/st%2Cstm32-ucpd.md#std-dtcompatible-st-stm32-ucpd):
>
>     > - new property: `dead-battery`
>     > - new property: `pinctrl-0`
>     > - new property: `pinctrl-names`
>     > - new property: `pinctrl-1`
>     > - new property: `pinctrl-2`
>     > - new property: `pinctrl-3`
>     > - new property: `pinctrl-4`
>   - [`st,stm32-timers`](../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers):
>
>     > - new property: `resets`
>     > - new property: `reset-names`
>   - [`st,stm32-lptim`](../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim):
>
>     > - new property: `st,static-prescaler`
>     > - new property: `reset-names`
>   - [`st,stm32-usb`](../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb):
>
>     > - removed property: `enable-pin-remap`
> - Texas Instruments (ti):
>
>   - [`ti,ina230`](../build/dts/api/bindings/sensor/ti%2Cina230.md#std-dtcompatible-ti-ina230) (on i2c bus):
>
>     > - new property: `current-lsb-microamps`
>     > - new property: `rshunt-milliohms`
>     > - new property: `alert-gpios`
>     > - removed property: `irq-gpios`
>     > - removed property: `current-lsb`
>     > - removed property: `rshunt`
>   - [`ti,ina237`](../build/dts/api/bindings/sensor/ti%2Cina237.md#std-dtcompatible-ti-ina237) (on i2c bus):
>
>     > - new property: `current-lsb-microamps`
>     > - new property: `rshunt-milliohms`
>     > - new property: `alert-gpios`
>     > - removed property: `irq-gpios`
>     > - removed property: `current-lsb`
>     > - removed property: `rshunt`
> - A stand-in for a real vendor which can be used in examples and tests (vnd):
>
>   - `vnd,pinctrl`:
>
>     > - new property: `bias-disable`
>     > - new property: `bias-high-impedance`
>     > - new property: `bias-bus-hold`
>     > - new property: `bias-pull-up`
>     > - new property: `bias-pull-down`
>     > - new property: `bias-pull-pin-default`
>     > - new property: `drive-push-pull`
>     > - new property: `drive-open-drain`
>     > - new property: `drive-open-source`
>     > - new property: `drive-strength`
>     > - new property: `drive-strength-microamp`
>     > - new property: `input-enable`
>     > - new property: `input-disable`
>     > - new property: `input-schmitt-enable`
>     > - new property: `input-schmitt-disable`
>     > - new property: `input-debounce`
>     > - new property: `power-source`
>     > - new property: `low-power-enable`
>     > - new property: `low-power-disable`
>     > - new property: `output-disable`
>     > - new property: `output-enable`
>     > - new property: `output-low`
>     > - new property: `output-high`
>     > - new property: `sleep-hardware-state`
>     > - new property: `slew-rate`
>     > - new property: `skew-delay`
> - Zephyr-specific binding (zephyr):
>
>   - [`zephyr,cdc-acm-uart`](../build/dts/api/bindings/serial/zephyr%2Ccdc-acm-uart.md#std-dtcompatible-zephyr-cdc-acm-uart) (on usb bus):
>
>     > - new property: `tx-fifo-size`
>     > - new property: `rx-fifo-size`
>   - [`zephyr,sdhc-spi-slot`](../build/dts/api/bindings/sdhc/zephyr%2Csdhc-spi-slot.md#std-dtcompatible-zephyr-sdhc-spi-slot) (on spi bus):
>
>     > - bus list changed from [] to [‘sd’]

### Other

Shields

> - In order to avoid name conflicts with devices that may be defined at
>   board level, it is advised, specifically for shields devicetree descriptions,
>   to provide a device nodelabel in the form `<device>_<shield>`. In-tree shields
>   have been updated to follow this recommendation.

- Others

  - STM32F1 SoCs

    - Added new pinctrl definitions for STM32F1xx PWM input. In PWM capture mode
      STM32F1xx pins have to be configured as input and not as alternate.
      The new names takes the form tim1\_ch1\_pwm\_in\_pa8 for example.
    - Renamed pinctrl definitions for STM32F1xx PWM output to differentiate them
      from newly created inputs. The new names takes the form tim1\_ch1\_pwm\_out\_pa8
      instead of tim1\_ch1\_pwm\_pa8.

## Libraries / Subsystems

- C Library

  - Newlib nano variant is no longer selected by default when
    [`CONFIG_NEWLIB_LIBC`](../kconfig.md#CONFIG_NEWLIB_LIBC "CONFIG_NEWLIB_LIBC") is selected.
    [`CONFIG_NEWLIB_LIBC_NANO`](../kconfig.md#CONFIG_NEWLIB_LIBC_NANO "CONFIG_NEWLIB_LIBC_NANO") must now be explicitly selected
    in order to use the nano variant.
  - Picolibc now supports all architectures supported by Zephyr.
  - Added C11 `aligned_alloc` support to the minimal libc.
- C++ Library

  - C++ support in Zephyr is no longer considered a “subsystem” because it
    mainly consists of the C++ ABI runtime library and the C++ standard
    library, which are “libraries” that are dissimilar to the existing Zephyr
    subsystems. C++ support components are now located in `lib/cpp` as
    “C++ library.”
  - C++ ABI runtime library components such as global constructor/destructor
    and initialiser handlers, that were previously located under
    `subsys/cpp`, have been moved to `lib/cpp/abi` in order to provide a
    clear separation between the C++ ABI runtime library and the C++ standard
    library.
  - C++ minimal library components have been moved to `lib/cpp/minimal`.
  - C++ tests have been moved to `tests/lib/cpp`.
  - C++ samples have been moved to `samples/cpp`.
  - `CONFIG_CPLUSPLUS` has been renamed to
    [`CONFIG_CPP`](../kconfig.md#CONFIG_CPP "CONFIG_CPP").
  - `CONFIG_EXCEPTIONS` has been renamed to
    [`CONFIG_CPP_EXCEPTIONS`](../kconfig.md#CONFIG_CPP_EXCEPTIONS "CONFIG_CPP_EXCEPTIONS").
  - `CONFIG_RTTI` has been renamed to
    [`CONFIG_CPP_RTTI`](../kconfig.md#CONFIG_CPP_RTTI "CONFIG_CPP_RTTI").
  - `CONFIG_LIB_CPLUSPLUS` is deprecated. A toolchain-specific
    C++ standard library Kconfig option from
    [`CONFIG_LIBCPP_IMPLEMENTATION`](../kconfig.md#CONFIG_LIBCPP_IMPLEMENTATION "CONFIG_LIBCPP_IMPLEMENTATION") should be selected instead.
  - Zephyr subsystems and modules that require the features from the full C++
    standard library (e.g. Standard Template Library) can now select
    [`CONFIG_REQUIRES_FULL_LIBC`](../kconfig.md#CONFIG_REQUIRES_FULL_LIBC "CONFIG_REQUIRES_FULL_LIBC"), which automatically selects
    a compatible C++ standard library.
  - Introduced `CONFIG_CPP_MAIN` to support defining `main()`
    function in a C++ source file. Enabling this option makes the Zephyr kernel
    invoke `int main(void)`, which is required by the ISO C++ standards, as
    opposed to the Zephyr default `void main(void)`.
  - Added no-throwing implementation of new operator to the C++ minimal
    library.
  - Added support for new operator with alignment request (C++17) to the C++
    minimal library.
  - Added GNU C++ standard library support with Picolibc when using a suitably
    configured toolchain (e.g. the upcoming Zephyr SDK 0.16.0 release).
- Cache

  - Introduced new Cache API
  - `CONFIG_HAS_ARCH_CACHE` has been renamed to
    [`CONFIG_ARCH_CACHE`](../kconfig.md#CONFIG_ARCH_CACHE "CONFIG_ARCH_CACHE")
  - `CONFIG_HAS_EXTERNAL_CACHE` has been renamed to
    [`CONFIG_EXTERNAL_CACHE`](../kconfig.md#CONFIG_EXTERNAL_CACHE "CONFIG_EXTERNAL_CACHE")
- DSP

  - Introduced DSP (digital signal processing) subsystem with CMSIS-DSP as the
    default backend.
  - CMSIS-DSP now supports all architectures supported by Zephyr.
- File systems

  - Added new API call fs\_mkfs.
  - Added new sample samples/subsys/fs/format.
  - FAT FS driver has been updated to version 0.15 w/patch1.
  - Added the option to disable CRC checking in [Flash Circular Buffer (FCB)](../services/storage/fcb/fcb.md#fcb-api) by enabling the
    Kconfig option [`CONFIG_FCB_ALLOW_FIXED_ENDMARKER`](../kconfig.md#CONFIG_FCB_ALLOW_FIXED_ENDMARKER "CONFIG_FCB_ALLOW_FIXED_ENDMARKER")
    and setting the FCB\_FLAGS\_CRC\_DISABLED flag in the [`fcb`](../doxygen/html/structfcb.md) struct.
- IPC

  - Added [`ipc_rpmsg_deinit()`](../doxygen/html/group__ipc__service__rpmsg__api.md#gaef3a7306082f88deb394f85a4bb5758b), [`ipc_service_close_instance()`](../doxygen/html/group__ipc__service__api.md#ga78c837d30cfd8989efe63e0a397148a7) and
    [`ipc_static_vrings_deinit()`](../doxygen/html/group__ipc__service__static__vrings__api.md#ga90680ce6a8cc4dae9cabba8fad6e939a) functions
  - Added deregister API support for icmsg backend
  - Added a multi-endpoint feature to icmsg backend
  - Added no-copy features to icmsg backend
- ISO-TP

  - Rewrote the ISO-TP API to not reuse definitions from the CAN controller API.
- Logging

  - Added support for logging on multiple domains.
  - [`CONFIG_LOG_PRINTK`](../kconfig.md#CONFIG_LOG_PRINTK "CONFIG_LOG_PRINTK") is now by default enabled which means that
    when logging is enabled then printk is by directed to the logging subsystem.
  - Added option to use custom logging header.
- Management

  - MCUmgr functionality deprecated in 3.1 has been removed:
    CONFIG\_FS\_MGMT\_UL\_CHUNK\_SIZE, CONFIG\_IMG\_MGMT\_UL\_CHUNK\_SIZE,
    CONFIG\_OS\_MGMT\_ECHO\_LENGTH
  - MCUmgr fs\_mgmt issue with erasing a file prior to writing the first block
    of data has been worked around by only truncating/deleting the file data
    if the file exists. This can help work around an issue whereby logging is
    enabled and the command is sent on the same UART as the logging system, in
    which a filesystem error was emitted.
  - A MCUmgr bug when using the smp\_svr sample with Bluetooth transport that
    could have caused a stack overflow has been fixed.
  - A MCUmgr issue with Bluetooth transport that could cause a deadlock of the
    mcumgr thread if the remote device disconnected before the output message
    was sent has been fixed.
  - A MCUmgr img\_mgmt bug whereby the state of an image upload could persist
    when it was no longer valid (e.g. after an image erase command) has been
    fixed.
  - MCUmgr fs\_mgmt command has been added that allows querying/listing the
    supported hash/checksum types.
  - MCUmgr Bluetooth transport will now clear unprocessed commands sent if a
    remote device disconnects instead of processing them.
  - A new MCUmgr transport function pointer has been added which needs
    registering in `smp_transport_init` for removing invalid packets for
    connection-orientated transports. If this is unimplemented, the function
    pointer can be set to NULL.
  - MCUmgr command handler definitions have changed, the `mgmt_ctxt` struct
    has been replaced with the `smp_streamer` struct, the zcbor objects need
    to replace `cnbe` object access with `writer` and `cnbd` object
    access with `reader` to successfully build.
  - MCUmgr callback system has been reworked with a unified singular interface
    which supports status passing to the handler ([MCUmgr Callbacks](../services/device_mgmt/mcumgr_callbacks.md#mcumgr-callbacks)).
  - MCUmgr subsystem directory structure has been flattened and contents of the
    lib subdirectory has been redistributed into following directories:

    | Subdirectory | MCUmgr area |
    | --- | --- |
    | mgmt | MCUmgr management functions, group registration, and so on; |
    | smp | Simple Management Protocol processing; |
    | transport | Transport support and transport API; |
    | grp | Command groups, formerly lib/cmd; each group, which has Zephyr built in support has its own directory here; |
    | util | Utilities used by various subareas of MCUmgr. |

    Public API interfaces for above areas are now exported through zephyr\_interface,
    and headers for them reside in `zephyr/mgmt/mcumgr/<mcumgr_subarea>/`.
    For example to access mgmt API include `<zephyr/mgmt/mcumgr/mgmt/mgmt.h>`.

    Private headers for above areas can be accessed, when required, using paths:
    `mgmt/mcumgr/mgmt/<mcumgr_subarea>/`.
  - MCUmgr os\_mgmt info command has been added that allows querying details on
    the kernel and application, allowing application-level extensibility
    see [OS/Application Info](../services/device_mgmt/smp_groups/smp_group_0.md#mcumgr-os-application-info) for details.
  - MCUMgr `CONFIG_APP_LINK_WITH_MCUMGR` has been removed as
    it has not been doing anything.
  - MCUmgr Kconfig option names have been standardised. Script
    [scripts/utils/migrate\_mcumgr\_kconfigs.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/utils/migrate_mcumgr_kconfigs.py) has been provided
    to make transition to new Kconfig options easier.
    Below table provides information on old names and new equivalents:

    | Old Kconfig option name | New Kconfig option name |
    | --- | --- |
    | MCUMGR\_SMP\_WORKQUEUE\_STACK\_SIZE | MCUMGR\_TRANSPORT\_WORKQUEUE\_STACK\_SIZE |
    | MCUMGR\_SMP\_WORKQUEUE\_THREAD\_PRIO | MCUMGR\_TRANSPORT\_WORKQUEUE\_THREAD\_PRIO |
    | MGMT\_MAX\_MAIN\_MAP\_ENTRIES | MCUMGR\_SMP\_CBOR\_MAX\_MAIN\_MAP\_ENTRIES |
    | MGMT\_MIN\_DECODING\_LEVELS | MCUMGR\_SMP\_CBOR\_MIN\_DECODING\_LEVELS |
    | MGMT\_MIN\_DECODING\_LEVEL\_1 | MCUMGR\_SMP\_CBOR\_MIN\_DECODING\_LEVEL\_1 |
    | MGMT\_MIN\_DECODING\_LEVEL\_2 | MCUMGR\_SMP\_CBOR\_MIN\_DECODING\_LEVEL\_2 |
    | MGMT\_MIN\_DECODING\_LEVEL\_3 | MCUMGR\_SMP\_CBOR\_MIN\_DECODING\_LEVEL\_3 |
    | MGMT\_MIN\_DECODING\_LEVEL\_4 | MCUMGR\_SMP\_CBOR\_MIN\_DECODING\_LEVEL\_4 |
    | MGMT\_MIN\_DECODING\_LEVEL\_5 | MCUMGR\_SMP\_CBOR\_MIN\_DECODING\_LEVEL\_5 |
    | MGMT\_MAX\_DECODING\_LEVELS | MCUMGR\_SMP\_CBOR\_MAX\_DECODING\_LEVELS |
    | MCUMGR\_CMD\_FS\_MGMT | MCUMGR\_GRP\_FS |
    | FS\_MGMT\_MAX\_FILE\_SIZE\_64KB | MCUMGR\_GRP\_FS\_MAX\_FILE\_SIZE\_64KB |
    | FS\_MGMT\_MAX\_FILE\_SIZE\_4GB | MCUMGR\_GRP\_FS\_MAX\_FILE\_SIZE\_4GB |
    | FS\_MGMT\_MAX\_OFFSET\_LEN | MCUMGR\_GRP\_FS\_MAX\_OFFSET\_LEN |
    | FS\_MGMT\_DL\_CHUNK\_SIZE\_LIMIT | MCUMGR\_GRP\_FS\_DL\_CHUNK\_SIZE\_LIMIT |
    | FS\_MGMT\_DL\_CHUNK\_SIZE | MCUMGR\_GRP\_FS\_DL\_CHUNK\_SIZE |
    | FS\_MGMT\_FILE\_STATUS | MCUMGR\_GRP\_FS\_FILE\_STATUS |
    | FS\_MGMT\_CHECKSUM\_HASH | MCUMGR\_GRP\_FS\_CHECKSUM\_HASH |
    | FS\_MGMT\_CHECKSUM\_HASH\_CHUNK\_SIZE | MCUMGR\_GRP\_FS\_CHECKSUM\_HASH\_CHUNK\_SIZE |
    | FS\_MGMT\_CHECKSUM\_IEEE\_CRC32 | MCUMGR\_GRP\_FS\_CHECKSUM\_IEEE\_CRC32 |
    | FS\_MGMT\_HASH\_SHA256 | MCUMGR\_GRP\_FS\_HASH\_SHA256 |
    | FS\_MGMT\_FILE\_ACCESS\_HOOK | MCUMGR\_GRP\_FS\_FILE\_ACCESS\_HOOK |
    | FS\_MGMT\_PATH\_SIZE | MCUMGR\_GRP\_FS\_PATH\_LEN |
    | MCUMGR\_CMD\_IMG\_MGMT | MCUMGR\_GRP\_IMG |
    | IMG\_MGMT\_USE\_HEAP\_FOR\_FLASH\_IMG\_CONTEXT | MCUMGR\_GRP\_IMG\_USE\_HEAP\_FOR\_FLASH\_IMG\_CONTEXT |
    | IMG\_MGMT\_UPDATABLE\_IMAGE\_NUMBER | MCUMGR\_GRP\_IMG\_UPDATABLE\_IMAGE\_NUMBER |
    | IMG\_MGMT\_VERBOSE\_ERR | MCUMGR\_GRP\_IMG\_VERBOSE\_ERR |
    | IMG\_MGMT\_DUMMY\_HDR | MCUMGR\_GRP\_IMG\_DUMMY\_HDR |
    | IMG\_MGMT\_DIRECT\_IMAGE\_UPLOAD | MCUMGR\_GRP\_IMG\_DIRECT\_UPLOAD |
    | IMG\_MGMT\_REJECT\_DIRECT\_XIP\_MISMATCHED\_SLOT | MCUMGR\_GRP\_IMG\_REJECT\_DIRECT\_XIP\_MISMATCHED\_SLOT |
    | IMG\_MGMT\_FRUGAL\_LIST | MCUMGR\_GRP\_IMG\_FRUGAL\_LIST |
    | MCUMGR\_CMD\_OS\_MGMT | MCUMGR\_GRP\_OS |
    | MCUMGR\_GRP\_OS\_OS\_RESET\_HOOK | MCUMGR\_GRP\_OS\_RESET\_HOOK |
    | OS\_MGMT\_RESET\_MS | MCUMGR\_GRP\_OS\_RESET\_MS |
    | OS\_MGMT\_TASKSTAT | MCUMGR\_GRP\_OS\_TASKSTAT |
    | OS\_MGMT\_TASKSTAT\_ONLY\_SUPPORTED\_STATS | MCUMGR\_GRP\_OS\_TASKSTAT\_ONLY\_SUPPORTED\_STATS |
    | OS\_MGMT\_TASKSTAT\_MAX\_NUM\_THREADS | MCUMGR\_GRP\_OS\_TASKSTAT\_MAX\_NUM\_THREADS |
    | OS\_MGMT\_TASKSTAT\_THREAD\_NAME\_LEN | MCUMGR\_GRP\_OS\_TASKSTAT\_THREAD\_NAME\_LEN |
    | OS\_MGMT\_TASKSTAT\_SIGNED\_PRIORITY | MCUMGR\_GRP\_OS\_TASKSTAT\_SIGNED\_PRIORITY |
    | OS\_MGMT\_TASKSTAT\_STACK\_INFO | MCUMGR\_GRP\_OS\_TASKSTAT\_STACK\_INFO |
    | OS\_MGMT\_ECHO | MCUMGR\_GRP\_OS\_ECHO |
    | OS\_MGMT\_MCUMGR\_PARAMS | MCUMGR\_GRP\_OS\_MCUMGR\_PARAMS |
    | MCUMGR\_CMD\_SHELL\_MGMT | MCUMGR\_GRP\_SHELL |
    | MCUMGR\_CMD\_SHELL\_MGMT\_LEGACY\_RC\_RETURN\_CODE | MCUMGR\_GRP\_SHELL\_LEGACY\_RC\_RETURN\_CODE |
    | MCUMGR\_CMD\_STAT\_MGMT | MCUMGR\_GRP\_STAT |
    | STAT\_MGMT\_MAX\_NAME\_LEN | MCUMGR\_GRP\_STAT\_MAX\_NAME\_LEN |
    | MCUMGR\_GRP\_ZEPHYR\_BASIC | MCUMGR\_GRP\_ZBASIC |
    | MCUMGR\_GRP\_BASIC\_CMD\_STORAGE\_ERASE | MCUMGR\_GRP\_ZBASIC\_STORAGE\_ERASE |
    | MGMT\_VERBOSE\_ERR\_RESPONSE | MCUMGR\_SMP\_VERBOSE\_ERR\_RESPONSE |
    | MCUMGR\_SMP\_REASSEMBLY | MCUMGR\_TRANSPORT\_REASSEMBLY |
    | MCUMGR\_BUF\_COUNT | MCUMGR\_TRANSPORT\_NETBUF\_COUNT |
    | MCUMGR\_BUF\_SIZE | MCUMGR\_TRANSPORT\_NETBUF\_SIZE |
    | MCUMGR\_BUF\_USER\_DATA\_SIZE | MCUMGR\_TRANSPORT\_NETBUF\_USER\_DATA\_SIZE |
    | MCUMGR\_SMP\_BT | MCUMGR\_TRANSPORT\_BT |
    | MCUMGR\_SMP\_REASSEMBLY\_BT | MCUMGR\_TRANSPORT\_BT\_REASSEMBLY |
    | MCUMGR\_SMP\_REASSEMBLY\_UNIT\_TESTS | MCUMGR\_TRANSPORT\_REASSEMBLY\_UNIT\_TESTS |
    | MCUMGR\_SMP\_BT\_AUTHEN | MCUMGR\_TRANSPORT\_BT\_AUTHEN |
    | MCUMGR\_SMP\_BT\_CONN\_PARAM\_CONTROL | MCUMGR\_TRANSPORT\_BT\_CONN\_PARAM\_CONTROL |
    | MCUMGR\_SMP\_BT\_CONN\_PARAM\_CONTROL\_MIN\_INT | MCUMGR\_TRANSPORT\_BT\_CONN\_PARAM\_CONTROL\_MIN\_INT |
    | MCUMGR\_SMP\_BT\_CONN\_PARAM\_CONTROL\_MAX\_INT | MCUMGR\_TRANSPORT\_BT\_CONN\_PARAM\_CONTROL\_MAX\_INT |
    | MCUMGR\_SMP\_BT\_CONN\_PARAM\_CONTROL\_LATENCY | MCUMGR\_TRANSPORT\_BT\_CONN\_PARAM\_CONTROL\_LATENCY |
    | MCUMGR\_SMP\_BT\_CONN\_PARAM\_CONTROL\_TIMEOUT | MCUMGR\_TRANSPORT\_BT\_CONN\_PARAM\_CONTROL\_TIMEOUT |
    | MCUMGR\_SMP\_BT\_CONN\_PARAM\_CONTROL\_RESTORE\_TIME | MCUMGR\_TRANSPORT\_BT\_CONN\_PARAM\_CONTROL\_RESTORE\_TIME |
    | MCUMGR\_SMP\_BT\_CONN\_PARAM\_CONTROL\_RETRY\_TIME | MCUMGR\_TRANSPORT\_BT\_CONN\_PARAM\_CONTROL\_RETRY\_TIME |
    | MCUMGR\_SMP\_DUMMY | MCUMGR\_TRANSPORT\_DUMMY |
    | MCUMGR\_SMP\_DUMMY\_RX\_BUF\_SIZE | MCUMGR\_TRANSPORT\_DUMMY\_RX\_BUF\_SIZE |
    | MCUMGR\_SMP\_SHELL | MCUMGR\_TRANSPORT\_SHELL |
    | MCUMGR\_SMP\_SHELL\_MTU | MCUMGR\_TRANSPORT\_SHELL\_MTU |
    | MCUMGR\_SMP\_SHELL\_RX\_BUF\_COUNT | MCUMGR\_TRANSPORT\_SHELL\_RX\_BUF\_COUNT |
    | MCUMGR\_SMP\_UART | MCUMGR\_TRANSPORT\_UART |
    | MCUMGR\_SMP\_UART\_ASYNC | MCUMGR\_TRANSPORT\_UART\_ASYNC |
    | MCUMGR\_SMP\_UART\_ASYNC\_BUFS | MCUMGR\_TRANSPORT\_UART\_ASYNC\_BUFS |
    | MCUMGR\_SMP\_UART\_ASYNC\_BUF\_SIZE | MCUMGR\_TRANSPORT\_UART\_ASYNC\_BUF\_SIZE |
    | MCUMGR\_SMP\_UART\_MTU | MCUMGR\_TRANSPORT\_UART\_MTU |
    | MCUMGR\_SMP\_UDP | MCUMGR\_TRANSPORT\_UDP |
    | MCUMGR\_SMP\_UDP\_IPV4 | MCUMGR\_TRANSPORT\_UDP\_IPV4 |
    | MCUMGR\_SMP\_UDP\_IPV6 | MCUMGR\_TRANSPORT\_UDP\_IPV6 |
    | MCUMGR\_SMP\_UDP\_PORT | MCUMGR\_TRANSPORT\_UDP\_PORT |
    | MCUMGR\_SMP\_UDP\_STACK\_SIZE | MCUMGR\_TRANSPORT\_UDP\_STACK\_SIZE |
    | MCUMGR\_SMP\_UDP\_THREAD\_PRIO | MCUMGR\_TRANSPORT\_UDP\_THREAD\_PRIO |
    | MCUMGR\_SMP\_UDP\_MTU | MCUMGR\_TRANSPORT\_UDP\_MTU |
  - MCUmgr responses where `rc` (result code) is 0 (no error) will no longer
    be present in responses and in cases where there is only an `rc` result,
    the resultant response will now be an empty CBOR map. The old behaviour can
    be restored by enabling
    [`CONFIG_MCUMGR_SMP_LEGACY_RC_BEHAVIOUR`](../kconfig.md#CONFIG_MCUMGR_SMP_LEGACY_RC_BEHAVIOUR "CONFIG_MCUMGR_SMP_LEGACY_RC_BEHAVIOUR").
  - MCUmgr now has log outputting on most errors from the included fs, img,
    os, shell, stat and zephyr\_basic group commands. The level of logging can be
    controlled by adjusting: `CONFIG_MCUMGR_GRP_FS_LOG_LEVEL`,
    `CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL`,
    `CONFIG_MCUMGR_GRP_OS_LOG_LEVEL`,
    `CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL`,
    `CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL` and
    `CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL`.
  - MCUmgr img\_mgmt has a new field which is sent in the final packet (if
    [`CONFIG_IMG_ENABLE_IMAGE_CHECK`](../kconfig.md#CONFIG_IMG_ENABLE_IMAGE_CHECK "CONFIG_IMG_ENABLE_IMAGE_CHECK") is enabled) named `match`
    which is a boolean and is true if the uploaded data matches the supplied
    hash, or false otherwise.
  - MCUmgr img\_mgmt will now skip receiving data if the provided hash already
    matches the hash of the data present (if
    [`CONFIG_IMG_ENABLE_IMAGE_CHECK`](../kconfig.md#CONFIG_IMG_ENABLE_IMAGE_CHECK "CONFIG_IMG_ENABLE_IMAGE_CHECK") is enabled) and finish the
    upload operation request instantly.
  - MCUmgr img\_mgmt structs are now packed, which fixes a fault issue on
    processors that do not support unaligned memory access.
  - If MCUmgr is used with the shell transport and `printk()` functionality
    is used, there can be an issue whereby the `printk()` calls output during
    a MCUmgr frame receive, this has been fixed by default in zephyr by routing
    `printk()` calls to the logging system, For user applications,
    [`CONFIG_LOG_PRINTK`](../kconfig.md#CONFIG_LOG_PRINTK "CONFIG_LOG_PRINTK") should be enabled to include this fix.
  - A bug when MCUmgr shell transport is used (issue was observed over USB CDC
    but could also occur with UART) whereby the default shell receive ring
    buffer is insufficient has been fixed by making the default size 256 bytes
    instead of 64 when the shell MCUmgr transport is selected.
  - UpdateHub:

    - The integrity check was reworked to allow use by other libraries. Since
      then UpdateHub uses mbedTLS library as default crypto library.
    - Added a new Storage Abstraction to isolate both flash operations and
      MCUboot internals.
    - The UpdateHub User API was moved as a Zephyr public API and the userspace
      now is available. This added [`updatehub_confirm()`](../doxygen/html/group__updatehub.md#gad1a3f6b1d91a7c9969a3411e0fd74f72) and
      [`updatehub_reboot()`](../doxygen/html/group__updatehub.md#gac433e995a18418771cac9fe4559ce84b) functions.
- LwM2M

  - The `lwm2m_senml_cbor_*` files have been regenerated using zcbor 0.6.0.
- POSIX API

  - Harmonized posix type definitions across the minimal libc, newlib and picolibc.

    - Abstract `pthread_t`, `pthread_key_t`, `pthread_cond_t`,
      `pthread_mutex_t`, as `uint32_t`.
    - Defined `PTHREAD_KEY_INITIALIZER`, [`PTHREAD_COND_INITIALIZER`](../doxygen/html/pthread_8h.md#aa7b867fe46f3660283fcb356c4fcbbf0),
      [`PTHREAD_MUTEX_INITIALIZER`](../doxygen/html/pthread_8h.md#a84e55100366a6a8338a2af3b3f279686) to align with POSIX 1003.1.
  - Allowed non-prefixed standard include paths with [`CONFIG_POSIX_API`](../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API").

    - I.e. `#include <unistd.h>` instead of `#include <zephyr/posix/unistd.h>`.
    - Primarily to ease integration with external libraries.
    - Internal Zephyr code should continue to use prefixed header paths.
  - Enabled `eventfd()`, `getopt()` by default with [`CONFIG_POSIX_API`](../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API").
  - Moved / renamed header files to align with POSIX specifications.

    - E.g. move `fcntl.h`, `sys/stat.h` from the minimal libc into the
      `include/zephyr/posix` directory. Rename `posix_sched.h` to `sched.h`.
    - Move [`O_ACCMODE`](../doxygen/html/fcntl_8h.md#a4dc4d45e07d2abc899bcaf04b2846a87), [`O_RDONLY`](../doxygen/html/fcntl_8h.md#a7a68c9ffaac7dbcd652225dd7c06a54b), [`O_WRONLY`](../doxygen/html/fcntl_8h.md#a11b644a8526139c4cc1850dac1271ced),
      [`O_WRONLY`](../doxygen/html/fcntl_8h.md#a11b644a8526139c4cc1850dac1271ced), to `fcntl.h`.
  - Added [`CONFIG_TIMER_CREATE_WAIT`](../kconfig.md#CONFIG_TIMER_CREATE_WAIT "CONFIG_TIMER_CREATE_WAIT"), [`CONFIG_MAX_PTHREAD_KEY_COUNT`](../kconfig.md#CONFIG_MAX_PTHREAD_KEY_COUNT "CONFIG_MAX_PTHREAD_KEY_COUNT"),
    [`CONFIG_MAX_PTHREAD_COND_COUNT`](../kconfig.md#CONFIG_MAX_PTHREAD_COND_COUNT "CONFIG_MAX_PTHREAD_COND_COUNT"), [`CONFIG_MAX_PTHREAD_MUTEX_COUNT`](../kconfig.md#CONFIG_MAX_PTHREAD_MUTEX_COUNT "CONFIG_MAX_PTHREAD_MUTEX_COUNT").
  - Defined [`SEEK_SET`](../doxygen/html/stdio_8h.md#a0d112bae8fd35be772185b6ec6bcbe64), [`SEEK_CUR`](../doxygen/html/stdio_8h.md#a4c8d0b76b470ba65a43ca46a88320f39), [`SEEK_END`](../doxygen/html/stdio_8h.md#ad2a2e6c114780c3071efd24f16c7f7d8).
- SD Subsystem

  - Added support for eMMC protocol in Zephyr.

    - Speed modes up to HS400 are supported using 1.8v operation.
    - Additional protocol tests have been added to verify eMMC functionality.
    - Disk subsystem tests have been updated to function with eMMC.
  - Card and host combinations that cannot utilize UHS (ultra high speed) mode
    will now use 4 bit bus width when possible. This will greatly improve
    performance for these systems.
- Settings

  - Replaced all [`k_panic()`](../doxygen/html/kernel_8h.md#aedd541f707b1463aaac15c7798340329) invocations within settings backend
    initialization with returning / propagating error codes.
- Shell

  - New features:

    - SHELL\_AUTOSTART configuration option. When SHELL\_AUTOSTART is set to n, the shell is not
      started after boot but can be enabled later from the application code.
    - Added support for setting the help description for each entry in a dictionary.
  - Bugfix:

    - Updated to clear command buffer when leaving bypass mode to prevent undefined behaviour
      on consecutive shell operations.
    - Set RX size default to 256 if shell MCUmgr is enabled.
    - Fixed log message queue size for all backends.
  - Documentation:

    - Added information explaining commands execution.
- Utilities

  - Added the linear range API to map values in a linear range to a range index
    [include/zephyr/sys/linear\_range.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/linear_range.h).
- Zbus

  - Added the [Zephyr bus (zbus)](../services/zbus/index.md#zbus) to Zephyr.

    - Channel-centric multi-paradigm (message-passing and publish-subscribe) communication message bus.
    - Virtual Distributed Event Dispatcher.
    - Observers can be listeners (synchronous) and subscribers (asynchronous).
    - One-to-one, one-to-many, and many-to-many communications.
    - Persistent messages distributed by shared-memory approach.
    - Delivery guarantee only for listeners.
    - Uses mutex to control channels access.
    - Added the following samples:

      - [zbus Hello World](../samples/subsys/zbus/hello_world/README.md#zbus-hello-world "Make three threads talk to each other using zbus.")
      - [Work queue](../samples/subsys/zbus/work_queue/README.md#zbus-work-queue "Use a work queue to process zbus messages in various ways.")
      - [Dynamic channel](../samples/subsys/zbus/dyn_channel/README.md#zbus-dyn-channel "Use zbus channels with dynamically allocated messages.")
      - [UART bridge](../samples/subsys/zbus/uart_bridge/README.md#zbus-uart-bridge "Redirect channel events to the host over UART.")
      - [Remote mock sample](../samples/subsys/zbus/remote_mock/README.md#zbus-remote-mock "Publish to a zbus instance using UART as a bridge.")
      - [Runtime observer registration](../samples/subsys/zbus/runtime_obs_registration/README.md#zbus-runtime-obs-registration "Use zbus' runtime observer registration to filter data generated by a producer.")
      - [Benchmarking](../samples/subsys/zbus/benchmark/README.md#zbus-benchmark "Measure the time for sending 256KB from a producer to N consumers.")
    - Added zbus channels APIs:

      - [`zbus_chan_pub()`](../doxygen/html/group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)
      - [`zbus_chan_read()`](../doxygen/html/group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e)
      - [`zbus_chan_notify()`](../doxygen/html/group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)
      - [`zbus_chan_claim()`](../doxygen/html/group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)
      - [`zbus_chan_finish()`](../doxygen/html/group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59)
      - [`zbus_chan_name()`](../doxygen/html/group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)
      - [`zbus_chan_msg()`](../doxygen/html/group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)
      - [`zbus_chan_const_msg()`](../doxygen/html/group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)
      - [`zbus_chan_msg_size()`](../doxygen/html/group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)
      - [`zbus_chan_user_data()`](../doxygen/html/group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)
      - [`zbus_chan_add_obs()`](../doxygen/html/group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)
      - [`zbus_chan_rm_obs()`](../doxygen/html/group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)
      - `zbus_runtime_obs_pool()`
      - [`zbus_obs_set_enable()`](../doxygen/html/group__zbus__apis.md#ga96767314e040e42609867a36684a6349)
      - [`zbus_obs_name()`](../doxygen/html/group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)
      - [`zbus_sub_wait()`](../doxygen/html/group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b)
      - [`zbus_iterate_over_channels()`](../doxygen/html/group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)
      - [`zbus_iterate_over_observers()`](../doxygen/html/group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)
    - Added the related configuration options:

      - [`CONFIG_ZBUS_CHANNEL_NAME`](../kconfig.md#CONFIG_ZBUS_CHANNEL_NAME "CONFIG_ZBUS_CHANNEL_NAME")
      - [`CONFIG_ZBUS_OBSERVER_NAME`](../kconfig.md#CONFIG_ZBUS_OBSERVER_NAME "CONFIG_ZBUS_OBSERVER_NAME")
      - `CONFIG_ZBUS_STRUCTS_ITERABLE_ACCESS`
      - `CONFIG_ZBUS_RUNTIME_OBSERVERS_POOL_SIZE`

## HALs

- Atmel

  - sam0: Added support for SAMC20/21.
  - sam4l: Added `US_MR_CHRL_{n}_BIT` Register Aliases for USART Driver.
- GigaDevice

  - Added support for gd32l23x.
  - Added support for gd32a50x.
- Nordic

  - Updated nrfx to version 2.10.0.
- STM32

  - stm32cube: updated stm32h7 to cube version V1.11.0.
  - stm32cube: updated stm32l5 to cube version V1.5.0.
  - stm32cube: updated stm32wl to cube version V1.3.0.
- Espressif

  - Added Ethernet driver support
  - Added light-sleep and deep-sleep support over PM interface
  - Added ADC and DAC driver support
  - Added GDMA driver support

## Storage

- Flash Map API drops `fa_device_id` from [`flash_area`](../doxygen/html/structflash__area.md), as it
  is no longer needed by MCUboot, and has not been populated for a long
  time now.

## Trusted Firmware-M

- Updated to TF-M 1.7.0 (and MbedTLS 3.2.1).
- Initial attestation service has been disabled by default due to license
  issues with the QCBOR dependency. To enable it, set the path for QCBOR via
  `CONFIG_TFM_QCBOR_PATH` or set the path to `DOWNLOAD`.
- Firmware update sample removed pending update to 1.0 FWU service.
- psa\_crypto sample removed pending resolution of PSA API conflicts w/MbedTLS.

## zcbor

Upgraded zcbor to 0.6.0. Among other things, this brings in a few convenient
changes for Zephyr:

- In the zcbor codebase, the `ARRAY_SIZE` macro has been renamed to
  `ZCBOR_ARRAY_SIZE` to not collide with Zephyr’s [`ARRAY_SIZE`](../doxygen/html/group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a) macro.
- The zcbor codebase now better supports being used in C++ code.

The entire release notes can be found at
[https://github.com/zephyrproject-rtos/zcbor/blob/0.6.0/RELEASE\_NOTES.md](https://github.com/zephyrproject-rtos/zcbor/blob/0.6.0/RELEASE_NOTES.md)

## Documentation

- Upgraded to Doxygen 1.9.6.
- It is now possible to link to Kconfig search results.

## Issue Related Items

### Known Issues

- [GitHub #33747](https://github.com/zephyrproject-rtos/zephyr/issues/33747) - gptp does not work well on NXP rt series platform
- [GitHub #37193](https://github.com/zephyrproject-rtos/zephyr/issues/37193) - mcumgr: Probably incorrect error handling with udp backend
- [GitHub #37731](https://github.com/zephyrproject-rtos/zephyr/issues/37731) - Bluetooth: hci samples: Unable to allocate command buffer
- [GitHub #40023](https://github.com/zephyrproject-rtos/zephyr/issues/40023) - Build fails for `native_posix` board when using C++ <atomic> header
- [GitHub #42030](https://github.com/zephyrproject-rtos/zephyr/issues/42030) - can: “bosch,m-can-base”: Warning “missing or empty reg/ranges property”
- [GitHub #43099](https://github.com/zephyrproject-rtos/zephyr/issues/43099) - CMake: ARCH roots issue
- [GitHub #43249](https://github.com/zephyrproject-rtos/zephyr/issues/43249) - MBEDTLS\_ECP\_C not build when MBEDTLS\_USE\_PSA\_CRYPTO
- [GitHub #43555](https://github.com/zephyrproject-rtos/zephyr/issues/43555) - Variables not properly initialized when using data relocation with SDRAM
- [GitHub #43562](https://github.com/zephyrproject-rtos/zephyr/issues/43562) - Setting and/or documentation of Timer and counter use/requirements for Nordic Bluetooth driver
- [GitHub #44339](https://github.com/zephyrproject-rtos/zephyr/issues/44339) - Bluetooth:controller: Implement support for Advanced Scheduling in refactored LLCP
- [GitHub #44948](https://github.com/zephyrproject-rtos/zephyr/issues/44948) - cmsis\_dsp: transform: error during building cf64.fpu and rf64.fpu for mps2\_an521\_remote
- [GitHub #45241](https://github.com/zephyrproject-rtos/zephyr/issues/45241) - (Probably) unnecessary branches in several modules
- [GitHub #45323](https://github.com/zephyrproject-rtos/zephyr/issues/45323) - Bluetooth: controller: llcp: Implement handling of delayed notifications in refactored LLCP
- [GitHub #45814](https://github.com/zephyrproject-rtos/zephyr/issues/45814) - Armclang build fails due to missing source file
- [GitHub #46121](https://github.com/zephyrproject-rtos/zephyr/issues/46121) - Bluetooth: Controller: hci: Wrong periodic advertising report data status
- [GitHub #46401](https://github.com/zephyrproject-rtos/zephyr/issues/46401) - ARM64: Relax 4K MMU mapping alignment
- [GitHub #46846](https://github.com/zephyrproject-rtos/zephyr/issues/46846) - lib: libc: newlib: strerror\_r non-functional
- [GitHub #47120](https://github.com/zephyrproject-rtos/zephyr/issues/47120) - shell uart: busy wait for DTR in ISR
- [GitHub #47732](https://github.com/zephyrproject-rtos/zephyr/issues/47732) - Flash map does not fare well with MCU who do bank swaps
- [GitHub #47908](https://github.com/zephyrproject-rtos/zephyr/issues/47908) - tests/kernel/mem\_protect/stack\_random works unreliably and sporadically fails
- [GitHub #48094](https://github.com/zephyrproject-rtos/zephyr/issues/48094) - pre-commit scripts fail when there is a space in zephyr\_base
- [GitHub #48102](https://github.com/zephyrproject-rtos/zephyr/issues/48102) - JSON parses uses recursion (breaks rule 17.2)
- [GitHub #48287](https://github.com/zephyrproject-rtos/zephyr/issues/48287) - malloc\_prepare ASSERT happens when enabling newlib libc with demand paging
- [GitHub #48608](https://github.com/zephyrproject-rtos/zephyr/issues/48608) - boards: mps2\_an385: Unstable system timer
- [GitHub #48841](https://github.com/zephyrproject-rtos/zephyr/issues/48841) - Bluetooth: df: Assert in lower link layer when requesting CTE from peer periodically with 7.5ms connection interval
- [GitHub #48992](https://github.com/zephyrproject-rtos/zephyr/issues/48992) - qemu\_leon3: tests/posix/common/portability.posix.common fails
- [GitHub #49213](https://github.com/zephyrproject-rtos/zephyr/issues/49213) - logging.add.log\_user test fails when compiled with GCC 12
- [GitHub #49390](https://github.com/zephyrproject-rtos/zephyr/issues/49390) - shell\_rtt thread can starve other threads of the same priority
- [GitHub #49484](https://github.com/zephyrproject-rtos/zephyr/issues/49484) - CONFIG\_BOOTLOADER\_SRAM\_SIZE should not be defined by default
- [GitHub #49492](https://github.com/zephyrproject-rtos/zephyr/issues/49492) - kernel.poll test fails on qemu\_arc\_hs6x when compiled with GCC 12
- [GitHub #49494](https://github.com/zephyrproject-rtos/zephyr/issues/49494) - testing.ztest.ztress test fails on qemu\_cortex\_r5 when compiled with GCC 12
- [GitHub #49614](https://github.com/zephyrproject-rtos/zephyr/issues/49614) - acrn\_ehl\_crb: The testcase tests/kernel/sched/schedule\_api failed to run.
- [GitHub #49816](https://github.com/zephyrproject-rtos/zephyr/issues/49816) - ISOTP receive fails for multiple binds with same CAN ID but different extended ID
- [GitHub #49889](https://github.com/zephyrproject-rtos/zephyr/issues/49889) - ctf trace: unknown event id when parsing samples/tracing result on reel board
- [GitHub #50084](https://github.com/zephyrproject-rtos/zephyr/issues/50084) - drivers: nrf\_802154: nrf\_802154\_trx.c - assertion fault when enabling Segger SystemView tracing
- [GitHub #50095](https://github.com/zephyrproject-rtos/zephyr/issues/50095) - ARC revision Kconfigs wrongly mixed with board name
- [GitHub #50196](https://github.com/zephyrproject-rtos/zephyr/issues/50196) - LSM6DSO interrupt handler not being called
- [GitHub #50501](https://github.com/zephyrproject-rtos/zephyr/issues/50501) - STM32 SPI does not work properly with async + interrupts
- [GitHub #50506](https://github.com/zephyrproject-rtos/zephyr/issues/50506) - nxp,mcux-usbd devicetree binding issues
- [GitHub #50546](https://github.com/zephyrproject-rtos/zephyr/issues/50546) - drivers: can: rcar: likely inconsistent behavior when calling can\_stop() with pending transmissions
- [GitHub #50598](https://github.com/zephyrproject-rtos/zephyr/issues/50598) - UDP over IPSP not working on nRF52840
- [GitHub #50652](https://github.com/zephyrproject-rtos/zephyr/issues/50652) - RAM Loading on i.MXRT1160\_evk
- [GitHub #50766](https://github.com/zephyrproject-rtos/zephyr/issues/50766) - Disable cross-compiling when using host toolchain
- [GitHub #50777](https://github.com/zephyrproject-rtos/zephyr/issues/50777) - LE Audio: Receiver start ready command shall only be sent by the receiver
- [GitHub #50875](https://github.com/zephyrproject-rtos/zephyr/issues/50875) - net: ip: race in access to writable net\_if attributes
- [GitHub #50941](https://github.com/zephyrproject-rtos/zephyr/issues/50941) - sample.logger.syst.catalog.deferred\_cpp fails on qemu\_cortex\_m0
- [GitHub #51024](https://github.com/zephyrproject-rtos/zephyr/issues/51024) - aarch32 excn vector not pinned in mmu causing newlib heap overlap
- [GitHub #51127](https://github.com/zephyrproject-rtos/zephyr/issues/51127) - UART HW DMA ( UART Communication based on HW DMA ) - Buffer Overflow test in STM32H743 Controller
- [GitHub #51133](https://github.com/zephyrproject-rtos/zephyr/issues/51133) - Bluetooth: audio: Sink ASE does not go to IDLE state
- [GitHub #51250](https://github.com/zephyrproject-rtos/zephyr/issues/51250) - ESP32-C3 pin glitches during start-up
- [GitHub #51317](https://github.com/zephyrproject-rtos/zephyr/issues/51317) - Confusing license references in nios2f-zephyr
- [GitHub #51342](https://github.com/zephyrproject-rtos/zephyr/issues/51342) - Bluetooth ISO extra `stream_sent` callback after `seq_num` 16-bit rollover
- [GitHub #51420](https://github.com/zephyrproject-rtos/zephyr/issues/51420) - tests: subsys: logging: log\_links: logging.log\_links fails
- [GitHub #51422](https://github.com/zephyrproject-rtos/zephyr/issues/51422) - nsim\_em: tests/subsys/logging/log\_link\_order run failed on nsim\_em
- [GitHub #51449](https://github.com/zephyrproject-rtos/zephyr/issues/51449) - device: device\_get\_binding is broken for nodes with the same name
- [GitHub #51604](https://github.com/zephyrproject-rtos/zephyr/issues/51604) - doc: is the documentation GDPR compliant since it uses Google Analytics without prompting the user about tracking?
- [GitHub #51637](https://github.com/zephyrproject-rtos/zephyr/issues/51637) - shell: bypass shell\_fprintf ASSERT fail
- [GitHub #51728](https://github.com/zephyrproject-rtos/zephyr/issues/51728) - soc: xtensa: esp32\_net: Remove binary blobs from source tree
- [GitHub #51774](https://github.com/zephyrproject-rtos/zephyr/issues/51774) - thread safety of adv\_new in Bluetooth subsys
- [GitHub #51814](https://github.com/zephyrproject-rtos/zephyr/issues/51814) - ARC irq\_offload doesn’t honor thread switches
- [GitHub #51820](https://github.com/zephyrproject-rtos/zephyr/issues/51820) - Longer strings aren’t logged
- [GitHub #51825](https://github.com/zephyrproject-rtos/zephyr/issues/51825) - west: runners: jlink: JLink.exe name collision
- [GitHub #51977](https://github.com/zephyrproject-rtos/zephyr/issues/51977) - newlib integration: \_unlink isn’t mapped to unlink
- [GitHub #52055](https://github.com/zephyrproject-rtos/zephyr/issues/52055) - Bluetooth: Controller: Broadcast scheduling issues
- [GitHub #52269](https://github.com/zephyrproject-rtos/zephyr/issues/52269) - UART documentation for uart\_irq\_tx\_enable/disable incomplete
- [GitHub #52271](https://github.com/zephyrproject-rtos/zephyr/issues/52271) - west sign: imgtool: zephyr.signed.hex and zephyr.signed.bin do not have the same contents
- [GitHub #52362](https://github.com/zephyrproject-rtos/zephyr/issues/52362) - nrf\_qspi\_nor driver crash if power management is enabled
- [GitHub #52395](https://github.com/zephyrproject-rtos/zephyr/issues/52395) - Cannot build applications with dts having (unused) external flash partition and disabling those drivers
- [GitHub #52491](https://github.com/zephyrproject-rtos/zephyr/issues/52491) - Value of EVENT\_OVERHEAD\_START\_US is set to low
- [GitHub #52494](https://github.com/zephyrproject-rtos/zephyr/issues/52494) - SPI NOR DPD comment is misleading/wrong
- [GitHub #52510](https://github.com/zephyrproject-rtos/zephyr/issues/52510) - twister: truncated handler.log reports test as “failed”
- [GitHub #52513](https://github.com/zephyrproject-rtos/zephyr/issues/52513) - sample.modules.chre fails on qemu\_leon3
- [GitHub #52575](https://github.com/zephyrproject-rtos/zephyr/issues/52575) - Kconfig: excessive `select` usage
- [GitHub #52585](https://github.com/zephyrproject-rtos/zephyr/issues/52585) - PDM event handler shouldn’t stop driver on allocation failure
- [GitHub #52589](https://github.com/zephyrproject-rtos/zephyr/issues/52589) - Add support for different SDHC high-speed modes (currently defaults to SDR25)
- [GitHub #52605](https://github.com/zephyrproject-rtos/zephyr/issues/52605) - esp32-usb-serial tx-complete interrupt not working in interrupt mode on esp32c3
- [GitHub #52623](https://github.com/zephyrproject-rtos/zephyr/issues/52623) - qemu\_x86: thousands of timer interrupts per second
- [GitHub #52667](https://github.com/zephyrproject-rtos/zephyr/issues/52667) - nrf\_rtc\_timer: Booting application with zephyr < 3.0.0 from mcuboot with zephyr >= 3.0.0
- [GitHub #52700](https://github.com/zephyrproject-rtos/zephyr/issues/52700) - posix: getopt: implement standards-compliant reset
- [GitHub #52702](https://github.com/zephyrproject-rtos/zephyr/issues/52702) - drivers: wifi: esp\_at: Some issues on Passive Receive mode
- [GitHub #52705](https://github.com/zephyrproject-rtos/zephyr/issues/52705) - RNDIS fails to enumerate on Raspberry Pi Pico
- [GitHub #52741](https://github.com/zephyrproject-rtos/zephyr/issues/52741) - bl5340\_dvk\_cpuapp has wrong button for mcuboot button
- [GitHub #52764](https://github.com/zephyrproject-rtos/zephyr/issues/52764) - boards: esp32c3\_devkitm: unable to read memory-mapped flash memory
- [GitHub #52792](https://github.com/zephyrproject-rtos/zephyr/issues/52792) - ATWINC1500 : (wifi\_winc1500\_nm\_bsp.c : nm\_bsp\_reset) The reset function is not logical and more
- [GitHub #52825](https://github.com/zephyrproject-rtos/zephyr/issues/52825) - Overflow in settime posix function
- [GitHub #52830](https://github.com/zephyrproject-rtos/zephyr/issues/52830) - Annoying Slirp Message console output from qemu\_x86 board target
- [GitHub #52868](https://github.com/zephyrproject-rtos/zephyr/issues/52868) - ESP32 Wifi driver returns EIO (-5) if connecting without a sleep sometime before calling
- [GitHub #52869](https://github.com/zephyrproject-rtos/zephyr/issues/52869) - ESP32 Counter overflow, with no API to reset it
- [GitHub #52885](https://github.com/zephyrproject-rtos/zephyr/issues/52885) - modem: gsm\_ppp: CONFIG\_GSM\_MUX: Unable to reactivate modem after executing gsm\_ppp\_stop()
- [GitHub #52886](https://github.com/zephyrproject-rtos/zephyr/issues/52886) - tests: subsys: fs: littlefs: filesystem.littlefs.default and filesystem.littlefs.custom fails
- [GitHub #52887](https://github.com/zephyrproject-rtos/zephyr/issues/52887) - Bluetooth: LL assert with chained adv packets
- [GitHub #52924](https://github.com/zephyrproject-rtos/zephyr/issues/52924) - ESP32 get the build message “IRAM0 segment data does not fit.”
- [GitHub #52941](https://github.com/zephyrproject-rtos/zephyr/issues/52941) - Zephyr assumes ARM M7 core has a cache
- [GitHub #52954](https://github.com/zephyrproject-rtos/zephyr/issues/52954) - check\_zephyr\_package() only checks the first zephyr package rather than all the considered ones.
- [GitHub #52998](https://github.com/zephyrproject-rtos/zephyr/issues/52998) - tests: drivers: can: Build failure with sysroot path not quoted on Windows
- [GitHub #53000](https://github.com/zephyrproject-rtos/zephyr/issues/53000) - Delaying logging via CONFIG\_LOG\_PROCESS\_THREAD\_STARTUP\_DELAY\_MS doesn’t work if another backend is disabled
- [GitHub #53006](https://github.com/zephyrproject-rtos/zephyr/issues/53006) - Hawbkit with b\_l4s5i\_iot01a - wifi\_eswifi: Cannot allocate rx packet
- [GitHub #53008](https://github.com/zephyrproject-rtos/zephyr/issues/53008) - Invalid ISO interval configuration
- [GitHub #53088](https://github.com/zephyrproject-rtos/zephyr/issues/53088) - Unable to chage initialization priority of logging subsys
- [GitHub #53123](https://github.com/zephyrproject-rtos/zephyr/issues/53123) - Cannot run a unit test on Mac OSX with M1 Chip
- [GitHub #53124](https://github.com/zephyrproject-rtos/zephyr/issues/53124) - cmake: incorrect argument passing and dereference in zephyr\_check\_compiler\_flag() and zephyr\_check\_compiler\_flag\_hardcoded()
- [GitHub #53137](https://github.com/zephyrproject-rtos/zephyr/issues/53137) - Bluetooth: Controller: HCI 0x45 error after 3rd AD fragment with data > 248 bytes
- [GitHub #53148](https://github.com/zephyrproject-rtos/zephyr/issues/53148) - Bluetooth: Controller: BT\_HCI\_OP\_LE\_BIG\_TERMINATE\_SYNC on syncing BIG sync returns invalid BIG handle
- [GitHub #53172](https://github.com/zephyrproject-rtos/zephyr/issues/53172) - SHTCx driver wrong negative temperature values
- [GitHub #53173](https://github.com/zephyrproject-rtos/zephyr/issues/53173) - HCI-UART: unable to preform a DFU - GATT CONN timeout
- [GitHub #53198](https://github.com/zephyrproject-rtos/zephyr/issues/53198) - Bluetooth: Restoring security level fails and missing some notifications
- [GitHub #53265](https://github.com/zephyrproject-rtos/zephyr/issues/53265) - Bluetooth: Controller: ISO interleaved broadcast not working
- [GitHub #53319](https://github.com/zephyrproject-rtos/zephyr/issues/53319) - USB CDC ACM UART driver’s interrupt-driven API hangs when no host is connected
- [GitHub #53334](https://github.com/zephyrproject-rtos/zephyr/issues/53334) - Bluetooth: Peripheral disconnected with BT\_HCI\_ERR\_LL\_RESP\_TIMEOUT reason and SMP timeout
- [GitHub #53343](https://github.com/zephyrproject-rtos/zephyr/issues/53343) - subsys: logging: use of timestamping during early boot may crash MMU-based systems
- [GitHub #53348](https://github.com/zephyrproject-rtos/zephyr/issues/53348) - Bluetooth: Restoring connection to peripheral issue
- [GitHub #53375](https://github.com/zephyrproject-rtos/zephyr/issues/53375) - net: lwm2m: write method when floating point
- [GitHub #53475](https://github.com/zephyrproject-rtos/zephyr/issues/53475) - The ATT\_MTU value for EATT should be set as the minimum MTU of ATT Client and ATT Server
- [GitHub #53505](https://github.com/zephyrproject-rtos/zephyr/issues/53505) - Some device tree integers may be signed or unsigned depending on their value
- [GitHub #53522](https://github.com/zephyrproject-rtos/zephyr/issues/53522) - k\_busy\_wait function hangs on when CONFIG\_SYSTEM\_CLOCK\_SLOPPY\_IDLE is set with CONFIG\_PM.
- [GitHub #53537](https://github.com/zephyrproject-rtos/zephyr/issues/53537) - TFM-M doesn’t generate tfm\_ns\_signed.bin image for FOTA firmware upgrade
- [GitHub #53544](https://github.com/zephyrproject-rtos/zephyr/issues/53544) - Cannot see both bootloader and application RTT output
- [GitHub #53546](https://github.com/zephyrproject-rtos/zephyr/issues/53546) - zephyr kernel Kconfig USE\_STDC\_LSM6DS3TR and hal\_st CMakeLists.txt lsm6ds3tr-c variable name mismatched (hyphen sign special case)
- [GitHub #53552](https://github.com/zephyrproject-rtos/zephyr/issues/53552) - LE Audio: Device executes receiver start ready before the CIS is connected
- [GitHub #53555](https://github.com/zephyrproject-rtos/zephyr/issues/53555) - ESP32-C3 Is RV32IMA, Not RV32IMC?
- [GitHub #53570](https://github.com/zephyrproject-rtos/zephyr/issues/53570) - SDHC SPI driver should issue CMD12 after receiving data error token
- [GitHub #53587](https://github.com/zephyrproject-rtos/zephyr/issues/53587) - Issue with Auto-IP and Multicast/socket connection
- [GitHub #53605](https://github.com/zephyrproject-rtos/zephyr/issues/53605) - tests: posix: common: portability.posix.common fails - posix\_apis.test\_clock\_gettime\_rollover
- [GitHub #53613](https://github.com/zephyrproject-rtos/zephyr/issues/53613) - tests: drivers: uart: uart\_mix\_fifo\_poll: tests `drivers.uart.uart_mix_poll_async_api_*` fail
- [GitHub #53643](https://github.com/zephyrproject-rtos/zephyr/issues/53643) - Invalid warning when BLE advertising times out
- [GitHub #53674](https://github.com/zephyrproject-rtos/zephyr/issues/53674) - net: lwm2m: senml cbor formatter relying on implementation detail / inconsistency of lwm2m\_path\_to\_string
- [GitHub #53680](https://github.com/zephyrproject-rtos/zephyr/issues/53680) - HawkBit Metadata Error
- [GitHub #53728](https://github.com/zephyrproject-rtos/zephyr/issues/53728) - Sensor API documentation: no mention of blocking behaviour
- [GitHub #53729](https://github.com/zephyrproject-rtos/zephyr/issues/53729) - Can not build for ESP32 sample program - Zephyr using CMake build
- [GitHub #53767](https://github.com/zephyrproject-rtos/zephyr/issues/53767) - @kconfig is not allowed in headline
- [GitHub #53780](https://github.com/zephyrproject-rtos/zephyr/issues/53780) - sysbuild with custom board compilation failed to find the board
- [GitHub #53790](https://github.com/zephyrproject-rtos/zephyr/issues/53790) - Flash Init fails when CONFIG\_SPI\_NOR\_IDLE\_IN\_DPD=y
- [GitHub #53800](https://github.com/zephyrproject-rtos/zephyr/issues/53800) - Raspberry Pi Pico - ssd1306 display attempts to initialize before i2c bus is ready for communication
- [GitHub #53801](https://github.com/zephyrproject-rtos/zephyr/issues/53801) - k\_busy\_wait adds 1us delay unnecessarily
- [GitHub #53823](https://github.com/zephyrproject-rtos/zephyr/issues/53823) - Bluetooth init failed on nrf5340\_audio\_dk\_nrf5340\_cpuapp
- [GitHub #53855](https://github.com/zephyrproject-rtos/zephyr/issues/53855) - mimxrt1050\_evk invalid writes to flash
- [GitHub #53858](https://github.com/zephyrproject-rtos/zephyr/issues/53858) - Response on the shell missing with fast queries
- [GitHub #53867](https://github.com/zephyrproject-rtos/zephyr/issues/53867) - kconfig: Linked code into external SEMC-controlled memory without boot header
- [GitHub #53871](https://github.com/zephyrproject-rtos/zephyr/issues/53871) - Bluetooth: IPSP Sample Crash on nrf52840dk\_nrf52840
- [GitHub #53873](https://github.com/zephyrproject-rtos/zephyr/issues/53873) - Syscall parser creates syscall macro for commented/ifdefed out syscall prototype
- [GitHub #53917](https://github.com/zephyrproject-rtos/zephyr/issues/53917) - clang-format key incompatible with IntelliJ IDEs
- [GitHub #53933](https://github.com/zephyrproject-rtos/zephyr/issues/53933) - tests: lib: spsc\_pbuf: lib.spsc\_pbuf… hangs
- [GitHub #53937](https://github.com/zephyrproject-rtos/zephyr/issues/53937) - usb: stm32g0: sometimes get write error during CDC ACM enumeration when using USB hub
- [GitHub #53939](https://github.com/zephyrproject-rtos/zephyr/issues/53939) - USB C PD stack no callback for MSG\_NOT\_SUPPORTED\_RECEIVED policy notify
- [GitHub #53964](https://github.com/zephyrproject-rtos/zephyr/issues/53964) - gpio\_emul: `gpio_*` functions not callable within an ISR
- [GitHub #53980](https://github.com/zephyrproject-rtos/zephyr/issues/53980) - Bluetooth: hci: spi: race condition leading to deadlock
- [GitHub #53993](https://github.com/zephyrproject-rtos/zephyr/issues/53993) - platform: Raspberry Pi Pico area: USB Default config should be bus powered device for the Raspberry Pi Pico
- [GitHub #53996](https://github.com/zephyrproject-rtos/zephyr/issues/53996) - bt\_conn\_foreach() includes invalid connection while advertising
- [GitHub #54014](https://github.com/zephyrproject-rtos/zephyr/issues/54014) - usb: using Bluetooth HCI class in composite device leads to conflicts
- [GitHub #54037](https://github.com/zephyrproject-rtos/zephyr/issues/54037) - Unciast\_audio\_client sample application cannot work with servers with only sinks.
- [GitHub #54047](https://github.com/zephyrproject-rtos/zephyr/issues/54047) - Bluetooth: Host: Invalid handling of Service Changed indication if GATT Service is registered after Bluetooth initialization and before settings load
- [GitHub #54064](https://github.com/zephyrproject-rtos/zephyr/issues/54064) - doc: mgmt: mcumgr: img\_mgmt: Documentation specifies that hash in state of images is a required field
- [GitHub #54076](https://github.com/zephyrproject-rtos/zephyr/issues/54076) - logging fails to build with LOG\_ALWAYS\_RUNTIME=y
- [GitHub #54085](https://github.com/zephyrproject-rtos/zephyr/issues/54085) - USB MSC Sample does not work for native\_posix over USBIP
- [GitHub #54092](https://github.com/zephyrproject-rtos/zephyr/issues/54092) - ZCBOR code generator generates names not compatible with C++
- [GitHub #54101](https://github.com/zephyrproject-rtos/zephyr/issues/54101) - bluetooth: shell: Lots of checks of type (unsigned < 0) which is bogus
- [GitHub #54121](https://github.com/zephyrproject-rtos/zephyr/issues/54121) - Intel CAVS: tests/subsys/zbus/user\_data fails
- [GitHub #54122](https://github.com/zephyrproject-rtos/zephyr/issues/54122) - Intel CAVS: tests/subsys/dsp/basicmath fails (timeout)
- [GitHub #54162](https://github.com/zephyrproject-rtos/zephyr/issues/54162) - Mass-Storage-Sample - USB HS support for the stm32f723e\_disco board
- [GitHub #54179](https://github.com/zephyrproject-rtos/zephyr/issues/54179) - DeviceTree compile failures do not stop build
- [GitHub #54198](https://github.com/zephyrproject-rtos/zephyr/issues/54198) - reel board: Mesh badge demo fails to send BT Mesh message
- [GitHub #54199](https://github.com/zephyrproject-rtos/zephyr/issues/54199) - ENC28J60: dns resolve fails after few minutes uptime
- [GitHub #54200](https://github.com/zephyrproject-rtos/zephyr/issues/54200) - bq274xx incorrect conversions
- [GitHub #54211](https://github.com/zephyrproject-rtos/zephyr/issues/54211) - tests: kernel: timer: timer\_behavior: kernel.timer.timer fails
- [GitHub #54226](https://github.com/zephyrproject-rtos/zephyr/issues/54226) - Code coverage collection is broken
- [GitHub #54240](https://github.com/zephyrproject-rtos/zephyr/issues/54240) - twister: –runtime-artifact-cleanup has no effect
- [GitHub #54273](https://github.com/zephyrproject-rtos/zephyr/issues/54273) - ci: Scan code workflow does not report a violation for unknown LicenseRef
- [GitHub #54275](https://github.com/zephyrproject-rtos/zephyr/issues/54275) - net: socket: tls: cannot send when using blocking socket
- [GitHub #54288](https://github.com/zephyrproject-rtos/zephyr/issues/54288) - modem: hl7800: power off draws excessive current
- [GitHub #54289](https://github.com/zephyrproject-rtos/zephyr/issues/54289) - Twister jobserver support eliminates parallel build for me
- [GitHub #54301](https://github.com/zephyrproject-rtos/zephyr/issues/54301) - esp32: Console doesn’t work with power management enabled
- [GitHub #54317](https://github.com/zephyrproject-rtos/zephyr/issues/54317) - kernel: events: SMP race condition and one enhancement
- [GitHub #54330](https://github.com/zephyrproject-rtos/zephyr/issues/54330) - West build command execution takes more time or fails sometimes
- [GitHub #54336](https://github.com/zephyrproject-rtos/zephyr/issues/54336) - picolibc is incompatible with xcc / xcc-clang toolchains
- [GitHub #54364](https://github.com/zephyrproject-rtos/zephyr/issues/54364) - CANopen SYNC message is not received
- [GitHub #54373](https://github.com/zephyrproject-rtos/zephyr/issues/54373) - Mcuboot swap type is `test` when update fails
- [GitHub #54377](https://github.com/zephyrproject-rtos/zephyr/issues/54377) - mec172xevb: benchmark.kernel.core (and adc\_api/drivers.adc) failing
- [GitHub #54407](https://github.com/zephyrproject-rtos/zephyr/issues/54407) - Bluetooth: Controller: ISO Central with continuous scanning asserts
- [GitHub #54411](https://github.com/zephyrproject-rtos/zephyr/issues/54411) - mgmt: mcumgr: Shell transport can lock shell up until device is rebooted
- [GitHub #54435](https://github.com/zephyrproject-rtos/zephyr/issues/54435) - mec172xevb: sample.drivers.sample.drivers.peci failing
- [GitHub #54439](https://github.com/zephyrproject-rtos/zephyr/issues/54439) - Missing documentation of lwm2m\_rd\_client\_resume and lwm2m\_rd\_client\_pause
- [GitHub #54444](https://github.com/zephyrproject-rtos/zephyr/issues/54444) - samples/modules/chre/sample.modules.chre should not attempt to build on toolchains w/o newlib
- [GitHub #54459](https://github.com/zephyrproject-rtos/zephyr/issues/54459) - hawkbit: wrong header size used while reading the version of the app
- [GitHub #54460](https://github.com/zephyrproject-rtos/zephyr/issues/54460) - Build system should skip `zephyr/drivers/ethernet` module if TAP & SLIP already provides a network driver in `zephyr/drivers/net/slip.c`
- [GitHub #54498](https://github.com/zephyrproject-rtos/zephyr/issues/54498) - net: openthread: echo server do not work in userspace
- [GitHub #54500](https://github.com/zephyrproject-rtos/zephyr/issues/54500) - jwt: memory allocation problem after multiple jwt\_sign calls
- [GitHub #54504](https://github.com/zephyrproject-rtos/zephyr/issues/54504) - LwM2M: Connection resume does not work after network error
- [GitHub #54506](https://github.com/zephyrproject-rtos/zephyr/issues/54506) - net: ieee802154\_6lo: wrong fragmentation of packets with specific payload sizes
- [GitHub #54531](https://github.com/zephyrproject-rtos/zephyr/issues/54531) - Bluetooth: Controller: le\_ext\_create\_connection fails with initiating\_PHYs == 0x03
- [GitHub #54532](https://github.com/zephyrproject-rtos/zephyr/issues/54532) - Tests: Bluetooth: tester: BTP communication is not fully reliable on NRF52 board using UART
- [GitHub #54538](https://github.com/zephyrproject-rtos/zephyr/issues/54538) - LE Audio: BAP Unicast Client Idle/CIS disconnect race condition
- [GitHub #54539](https://github.com/zephyrproject-rtos/zephyr/issues/54539) - LE Audio: Unicast client should only disconnect CIS if both ASEs are not in streaming state
- [GitHub #54542](https://github.com/zephyrproject-rtos/zephyr/issues/54542) - Bluetooth pending tx packets assert on disable
- [GitHub #54554](https://github.com/zephyrproject-rtos/zephyr/issues/54554) - arch.arm.swap.tz fails to build for v2m\_musca\_b1\_ns
- [GitHub #54576](https://github.com/zephyrproject-rtos/zephyr/issues/54576) - Errors during IPv4 defragmenting
- [GitHub #54577](https://github.com/zephyrproject-rtos/zephyr/issues/54577) - IPv6 defragmenting fails when segments do not overlap
- [GitHub #54581](https://github.com/zephyrproject-rtos/zephyr/issues/54581) - STM32H7 adc sequence init function unstable logic return
- [GitHub #54599](https://github.com/zephyrproject-rtos/zephyr/issues/54599) - net stats: many received TCP packets count as “dropped”
- [GitHub #54609](https://github.com/zephyrproject-rtos/zephyr/issues/54609) - driver: led: kconfig symbols mix up
- [GitHub #54610](https://github.com/zephyrproject-rtos/zephyr/issues/54610) - samples: kernel: metairq\_dispatch: sample.kernel.metairq\_dispatch hangs
- [GitHub #54630](https://github.com/zephyrproject-rtos/zephyr/issues/54630) - memcpy crashes with NEW\_LIBC on stm32 cortex m7 with debugger attached
- [GitHub #54668](https://github.com/zephyrproject-rtos/zephyr/issues/54668) - shell: “log backend” command causes shell to lock up
- [GitHub #54670](https://github.com/zephyrproject-rtos/zephyr/issues/54670) - stm32: memcpy crashes with NEWLIBC
- [GitHub #54674](https://github.com/zephyrproject-rtos/zephyr/issues/54674) - modem: hl7800: DNS resolver does not start for IPv6 only
- [GitHub #54683](https://github.com/zephyrproject-rtos/zephyr/issues/54683) - Missing input validation in gen\_driver\_kconfig\_dts.py
- [GitHub #54695](https://github.com/zephyrproject-rtos/zephyr/issues/54695) - usb mass storage on mimxrt595\_evk\_cm33 mount very slow
- [GitHub #54705](https://github.com/zephyrproject-rtos/zephyr/issues/54705) - CDC USB shell receives garbage when application starts
- [GitHub #54713](https://github.com/zephyrproject-rtos/zephyr/issues/54713) - LVGL Module File System Memory Leaks
- [GitHub #54717](https://github.com/zephyrproject-rtos/zephyr/issues/54717) - –generate-hardware-map produces TypeError: expected string or bytes-like object on Windows
- [GitHub #54719](https://github.com/zephyrproject-rtos/zephyr/issues/54719) - STM32 clock frequency calculation error
- [GitHub #54720](https://github.com/zephyrproject-rtos/zephyr/issues/54720) - QEMU bug with branch delay slots on ARC
- [GitHub #54726](https://github.com/zephyrproject-rtos/zephyr/issues/54726) - LittleFS test only works for specific device parameters
- [GitHub #54731](https://github.com/zephyrproject-rtos/zephyr/issues/54731) - USB DFU sample does not reliably upload image on RT1050
- [GitHub #54737](https://github.com/zephyrproject-rtos/zephyr/issues/54737) - Wrong order of member initialization for macro Z\_DEVICE\_INIT
- [GitHub #54739](https://github.com/zephyrproject-rtos/zephyr/issues/54739) - C++ Compatibility for DEVICE\_DT\_INST\_DEFINE
- [GitHub #54746](https://github.com/zephyrproject-rtos/zephyr/issues/54746) - ESP32 SPI word size is not respected
- [GitHub #54754](https://github.com/zephyrproject-rtos/zephyr/issues/54754) - outdated version of rpi\_pico hal configures USB PLL incorrectly
- [GitHub #54755](https://github.com/zephyrproject-rtos/zephyr/issues/54755) - small timer periods take twice as much time as they should
- [GitHub #54768](https://github.com/zephyrproject-rtos/zephyr/issues/54768) - nrf9160dk\_nrf52840: flow control pins crossed
- [GitHub #54769](https://github.com/zephyrproject-rtos/zephyr/issues/54769) - Error when flashing to LPCXpresso55S06 EVK.
- [GitHub #54770](https://github.com/zephyrproject-rtos/zephyr/issues/54770) - Bluetooth: GATT: CCC and CF values written by privacy-disabled peer before bonding may be lost
- [GitHub #54773](https://github.com/zephyrproject-rtos/zephyr/issues/54773) - Bluetooth: GATT: Possible race conditions related to GATT database hash calculation after settings load
- [GitHub #54779](https://github.com/zephyrproject-rtos/zephyr/issues/54779) - file write gives -5 after file size reaches cache size
- [GitHub #54783](https://github.com/zephyrproject-rtos/zephyr/issues/54783) - stm32: NULL dereference in net\_eth\_carrier\_on
- [GitHub #54785](https://github.com/zephyrproject-rtos/zephyr/issues/54785) - .data and .bss relocation to DTCM & CCM is broken with SDK 0.15+
- [GitHub #54798](https://github.com/zephyrproject-rtos/zephyr/issues/54798) - net: ipv4: IP packets get dropped in Zephyr when an application is receiving high rate data
- [GitHub #54805](https://github.com/zephyrproject-rtos/zephyr/issues/54805) - when invoke dma\_stm32\_disable\_stream failed in interrupt callback, it will endless loop
- [GitHub #54813](https://github.com/zephyrproject-rtos/zephyr/issues/54813) - Bluetooth: host: Implicit sc\_indicate declaration when Service Changed is disabled
- [GitHub #54824](https://github.com/zephyrproject-rtos/zephyr/issues/54824) - BT: Mesh: Utilizes some not initialized variables
- [GitHub #54826](https://github.com/zephyrproject-rtos/zephyr/issues/54826) - Clang/llvm build is broken: Error: initializer element is not a compile-time constant
- [GitHub #54833](https://github.com/zephyrproject-rtos/zephyr/issues/54833) - ESPXX failing in gpio tests
- [GitHub #54841](https://github.com/zephyrproject-rtos/zephyr/issues/54841) - Drivers: I2S: STM32: Mishandling of Master Clock output (MCK)
- [GitHub #54844](https://github.com/zephyrproject-rtos/zephyr/issues/54844) - RAK5010 board has wrong LIS3DH INT pin configured
- [GitHub #54846](https://github.com/zephyrproject-rtos/zephyr/issues/54846) - ESP32C3 SPI DMA host ID
- [GitHub #54855](https://github.com/zephyrproject-rtos/zephyr/issues/54855) - ESP32: Compilation errors after migrating to zephyr 3.2.0
- [GitHub #54856](https://github.com/zephyrproject-rtos/zephyr/issues/54856) - nRF52840 nRF52833 Bluetooth: Timeout in `net_config_init_by_iface` but interface is up
- [GitHub #54859](https://github.com/zephyrproject-rtos/zephyr/issues/54859) - LE Audio: BT\_AUDIO\_UNICAST\_CLIENT\_GROUP\_STREAM\_COUNT invalid descsi
- [GitHub #54861](https://github.com/zephyrproject-rtos/zephyr/issues/54861) - up\_squared: CHRE sample output mangling fails regex verification

### Addressed issues

- [GitHub #54873](https://github.com/zephyrproject-rtos/zephyr/issues/54873) - doc: Remove Google Analytics tracking code from generated documentation.
- [GitHub #54858](https://github.com/zephyrproject-rtos/zephyr/issues/54858) - espressif blobs does not follow zephyr requirements
- [GitHub #54872](https://github.com/zephyrproject-rtos/zephyr/issues/54872) - west flash –elf-file is not flashing using .elf file, but using zephyr.hex to flash
- [GitHub #54813](https://github.com/zephyrproject-rtos/zephyr/issues/54813) - Bluetooth: host: Implicit sc\_indicate declaration when Service Changed is disabled
- [GitHub #54804](https://github.com/zephyrproject-rtos/zephyr/issues/54804) - Warning (simple\_bus\_reg): /soc/can: missing or empty reg/ranges property
- [GitHub #54786](https://github.com/zephyrproject-rtos/zephyr/issues/54786) - doc: Version selector should link to latest LTS version instead of 2.7.0
- [GitHub #54782](https://github.com/zephyrproject-rtos/zephyr/issues/54782) - nrf\_rtc\_timer may not properly handle a timeout that is set in specific conditions
- [GitHub #54770](https://github.com/zephyrproject-rtos/zephyr/issues/54770) - Bluetooth: GATT: CCC and CF values written by privacy-disabled peer before bonding may be lost
- [GitHub #54763](https://github.com/zephyrproject-rtos/zephyr/issues/54763) - doc: Copyright notice should be updated to 2015-2023
- [GitHub #54760](https://github.com/zephyrproject-rtos/zephyr/issues/54760) - net\_lwm2m\_engine: fcntl(F\_GETFL) failed (-22) on es-wifi
- [GitHub #54730](https://github.com/zephyrproject-rtos/zephyr/issues/54730) - intel\_adsp\_ace15\_mtpm: cpp.main.minimal test failing
- [GitHub #54718](https://github.com/zephyrproject-rtos/zephyr/issues/54718) - The rf2xx driver uses a wrong bit mask on TRAC\_STATUS
- [GitHub #54710](https://github.com/zephyrproject-rtos/zephyr/issues/54710) - Sending NODE\_RX\_TYPE\_CIS\_ESTABLISHED messes up LLCP
- [GitHub #54703](https://github.com/zephyrproject-rtos/zephyr/issues/54703) - boards: thingy53: Inconsistent method of setting USB related log level
- [GitHub #54702](https://github.com/zephyrproject-rtos/zephyr/issues/54702) - boards: thingy53: USB remote wakeup is not correctly disabled
- [GitHub #54686](https://github.com/zephyrproject-rtos/zephyr/issues/54686) - RP2040: Cleanup incorrect comment and condition from the USB driver
- [GitHub #54685](https://github.com/zephyrproject-rtos/zephyr/issues/54685) - drivers: serial: rp2040: fix rpi pico address mapping
- [GitHub #54671](https://github.com/zephyrproject-rtos/zephyr/issues/54671) - Bluetooth: spurious error when using hci\_rpmsg
- [GitHub #54666](https://github.com/zephyrproject-rtos/zephyr/issues/54666) - LE Audio: EALREADY error of ase\_stream\_qos() not mapped
- [GitHub #54659](https://github.com/zephyrproject-rtos/zephyr/issues/54659) - boards: arm: nrf52840dongle\_nrf52840: Defaults to UART which is not connected (and mcuboot build fails)
- [GitHub #54654](https://github.com/zephyrproject-rtos/zephyr/issues/54654) - LE Audio: Kconfig typo in `pacs.c`
- [GitHub #54642](https://github.com/zephyrproject-rtos/zephyr/issues/54642) - Bluetooth: Controller: Assertion on disconnecting CIS and assertion on synchronizing to first encrypted BIS
- [GitHub #54614](https://github.com/zephyrproject-rtos/zephyr/issues/54614) - Cannot flash b\_l4s5i\_iot01a samples/hello\_world
- [GitHub #54613](https://github.com/zephyrproject-rtos/zephyr/issues/54613) - Bluetooth: Unable to enable PAST as advertiser without periodic sync support
- [GitHub #54605](https://github.com/zephyrproject-rtos/zephyr/issues/54605) - native\_posix\_64 platform broken in Twister
- [GitHub #54597](https://github.com/zephyrproject-rtos/zephyr/issues/54597) - SRAM2 wrong on certain stm32h7 SOC (system crashes during startup)
- [GitHub #54580](https://github.com/zephyrproject-rtos/zephyr/issues/54580) - samples/subsys/task\_wdt fails with timeout on s32z270dc2\_r52 boards
- [GitHub #54575](https://github.com/zephyrproject-rtos/zephyr/issues/54575) - Automatic termination with return code from a native\_posix main function
- [GitHub #54574](https://github.com/zephyrproject-rtos/zephyr/issues/54574) - USB RNDIS Reception and Descriptor Issue(s)
- [GitHub #54573](https://github.com/zephyrproject-rtos/zephyr/issues/54573) - gpio\_hogs test uses an incorrect GPIO spec handle
- [GitHub #54572](https://github.com/zephyrproject-rtos/zephyr/issues/54572) - QEMU networking breakage (Updating nrf-sdk 2.1->2.2 , implies zephyr 3.1 -> 3.2)
- [GitHub #54569](https://github.com/zephyrproject-rtos/zephyr/issues/54569) - MMC subsys shares sdmmc kconfigs
- [GitHub #54567](https://github.com/zephyrproject-rtos/zephyr/issues/54567) - Assertion in z\_add\_timeout() fails in drivers.uart.uart\_mix\_poll\_async\_api test
- [GitHub #54563](https://github.com/zephyrproject-rtos/zephyr/issues/54563) - Variable uninitialised in flash\_stm32\_page\_layout
- [GitHub #54558](https://github.com/zephyrproject-rtos/zephyr/issues/54558) - LPTIM Kconfig-related build failures for nucleo\_g431rb
- [GitHub #54557](https://github.com/zephyrproject-rtos/zephyr/issues/54557) - sample.drivers.flash.shell fails to build for adafruit\_kb2040
- [GitHub #54556](https://github.com/zephyrproject-rtos/zephyr/issues/54556) - sample.display.lvgl.gui fails to build for stm32f429i\_disc1
- [GitHub #54545](https://github.com/zephyrproject-rtos/zephyr/issues/54545) - boards: rpi\_pico: Bad MPU settings
- [GitHub #54544](https://github.com/zephyrproject-rtos/zephyr/issues/54544) - Bluetooth: controller: HCI/CCO/BI-45-C setHostFeatureBit failing
- [GitHub #54540](https://github.com/zephyrproject-rtos/zephyr/issues/54540) - psa\_crypto variants of drivers/entropy/api and crypto/rand32 tests fail to build for nrf9160dk\_nrf9160\_ns and nrf5340dk\_nrf5340\_cpuapp\_ns
- [GitHub #54537](https://github.com/zephyrproject-rtos/zephyr/issues/54537) - logging.add.async build fails on mtpm with xcc-clang
- [GitHub #54534](https://github.com/zephyrproject-rtos/zephyr/issues/54534) - PSoC6/Cat1 add binary blob for Cortex-M0+ core
- [GitHub #54533](https://github.com/zephyrproject-rtos/zephyr/issues/54533) - tests/drivers/can/timing fails on nucleo\_f746zg
- [GitHub #54529](https://github.com/zephyrproject-rtos/zephyr/issues/54529) - Bluetooth: shell: Missing help messages and parameters
- [GitHub #54528](https://github.com/zephyrproject-rtos/zephyr/issues/54528) - log switch\_format, mipi\_syst tests failing on intel\_adsp\_ace15\_mtpm
- [GitHub #54522](https://github.com/zephyrproject-rtos/zephyr/issues/54522) - Can we embrace GNU Build IDs?
- [GitHub #54516](https://github.com/zephyrproject-rtos/zephyr/issues/54516) - twister: Quarantine verify works incorrectly with integration mode
- [GitHub #54509](https://github.com/zephyrproject-rtos/zephyr/issues/54509) - Zephyr does not configure TF-M correctly for Hard-Float
- [GitHub #54507](https://github.com/zephyrproject-rtos/zephyr/issues/54507) - CONFIG\_PM=y results to hard fault system for STM32L083
- [GitHub #54499](https://github.com/zephyrproject-rtos/zephyr/issues/54499) - stm32u5 lptimer driver init must wait after interrupt reg
- [GitHub #54493](https://github.com/zephyrproject-rtos/zephyr/issues/54493) - samples/drivers/counter/alarm/ fails on nucleo\_f746zg
- [GitHub #54492](https://github.com/zephyrproject-rtos/zephyr/issues/54492) - west: twister return code ignored by west
- [GitHub #54484](https://github.com/zephyrproject-rtos/zephyr/issues/54484) - Intel CAVS25: tests/boards/intel\_adsp/ssp/ fails
- [GitHub #54472](https://github.com/zephyrproject-rtos/zephyr/issues/54472) - How to enable a node in main.
- [GitHub #54469](https://github.com/zephyrproject-rtos/zephyr/issues/54469) - nsim\_sem and nsim\_em7d\_v22 failed in zdsp.basicmath test
- [GitHub #54462](https://github.com/zephyrproject-rtos/zephyr/issues/54462) - usb\_dc\_rpi\_pico driver enables some interrupts it doesn’t handle
- [GitHub #54461](https://github.com/zephyrproject-rtos/zephyr/issues/54461) - SAM spi bus inoperable when interrupted on fast path
- [GitHub #54457](https://github.com/zephyrproject-rtos/zephyr/issues/54457) - DHCPv4 starts even when interface is not operationally up
- [GitHub #54455](https://github.com/zephyrproject-rtos/zephyr/issues/54455) - Many tests have wrong component and are wrongly categorized
- [GitHub #54454](https://github.com/zephyrproject-rtos/zephyr/issues/54454) - Twister summary in some cases provides an irrelevant example
- [GitHub #54450](https://github.com/zephyrproject-rtos/zephyr/issues/54450) - nuvoton\_pfm\_m487 failed to build due to missing M48x-pinctrl.h
- [GitHub #54440](https://github.com/zephyrproject-rtos/zephyr/issues/54440) - tests/net/lib/lwm2m/lwm2m\_registry/subsys.net.lib.lwm2m.lwm2m\_registry fails to build w/toolchains that don’t support newlib
- [GitHub #54438](https://github.com/zephyrproject-rtos/zephyr/issues/54438) - question: why lwm2m\_rd\_client\_stop might block
- [GitHub #54431](https://github.com/zephyrproject-rtos/zephyr/issues/54431) - adafruit kb2040 board configuration is invalid and lack flash controller
- [GitHub #54428](https://github.com/zephyrproject-rtos/zephyr/issues/54428) - esp32 invalid flash dependencies
- [GitHub #54427](https://github.com/zephyrproject-rtos/zephyr/issues/54427) - stm32 uart driver `LOG_` msg crashes when entering sleep mode
- [GitHub #54422](https://github.com/zephyrproject-rtos/zephyr/issues/54422) - modules: openthread: multiple definition in openthread config
- [GitHub #54417](https://github.com/zephyrproject-rtos/zephyr/issues/54417) - Intel CAVS18: tests/subsys/dsp/basicmath fails
- [GitHub #54414](https://github.com/zephyrproject-rtos/zephyr/issues/54414) - stm32u5 dma driver does not support repeated start-stop
- [GitHub #54412](https://github.com/zephyrproject-rtos/zephyr/issues/54412) - [hci\_uart] nrf52840 & BlueZ 5.55 - start / stop scanning breaks
- [GitHub #54410](https://github.com/zephyrproject-rtos/zephyr/issues/54410) - [BUG] TLB driver fails to unmap L2 HPSRAM region when assertions are enabled
- [GitHub #54409](https://github.com/zephyrproject-rtos/zephyr/issues/54409) - ETH MAC config for STM32H7X and STM32\_HAL\_API\_V2 too late and fails
- [GitHub #54405](https://github.com/zephyrproject-rtos/zephyr/issues/54405) - Nominate @Vge0rge as contributor
- [GitHub #54401](https://github.com/zephyrproject-rtos/zephyr/issues/54401) - Uninitialized has\_param struct sometimes causes BSIM “has.sh” test to fail
- [GitHub #54399](https://github.com/zephyrproject-rtos/zephyr/issues/54399) - Intel CAVS18: tests/subsys/zbus/user\_data/user\_data.channel\_user\_data FAILED
- [GitHub #54397](https://github.com/zephyrproject-rtos/zephyr/issues/54397) - Test posix\_header fails on some STM32 Nucleo boards
- [GitHub #54395](https://github.com/zephyrproject-rtos/zephyr/issues/54395) - mgmt: mcumgr: img\_grp: Upload inspect fails when using swap using scratch
- [GitHub #54393](https://github.com/zephyrproject-rtos/zephyr/issues/54393) - Bluetooth: Controller: Starting a second BIG causes them to overlap and have twice the interval
- [GitHub #54387](https://github.com/zephyrproject-rtos/zephyr/issues/54387) - soc: arm: st\_stm32: Incorrect SRAM devicetree definition for the STM32L471xx
- [GitHub #54384](https://github.com/zephyrproject-rtos/zephyr/issues/54384) - Removal of old runner options caused downstream breakage
- [GitHub #54378](https://github.com/zephyrproject-rtos/zephyr/issues/54378) - Net pkt PPP dependency bug
- [GitHub #54374](https://github.com/zephyrproject-rtos/zephyr/issues/54374) - ARC: west runner: mdb: incorrect handling of unsupported jtag adapters
- [GitHub #54372](https://github.com/zephyrproject-rtos/zephyr/issues/54372) - ARC: west runner: mdb: unexpected empty argument pass to MDB executable
- [GitHub #54366](https://github.com/zephyrproject-rtos/zephyr/issues/54366) - tests: pin\_get\_config failed on it8xxx2\_evb, again
- [GitHub #54361](https://github.com/zephyrproject-rtos/zephyr/issues/54361) - Incorrect network stats for Neighbour Discovery packets
- [GitHub #54360](https://github.com/zephyrproject-rtos/zephyr/issues/54360) - enable HTTPS server on Zephyr RTOS
- [GitHub #54356](https://github.com/zephyrproject-rtos/zephyr/issues/54356) - Bluetooth: Scanner consumption while scanning
- [GitHub #54351](https://github.com/zephyrproject-rtos/zephyr/issues/54351) - Tests: bluetooth: failing unittests
- [GitHub #54347](https://github.com/zephyrproject-rtos/zephyr/issues/54347) - zephyr/posix/fcntl.h header works differently on native\_posix platform
- [GitHub #54344](https://github.com/zephyrproject-rtos/zephyr/issues/54344) - Bluetooth: Controller: Central ACL connections overlap Broadcast ISO BIG event
- [GitHub #54342](https://github.com/zephyrproject-rtos/zephyr/issues/54342) - Bluetooth: Controller: Connected ISO Central causes Peripheral to drop ISO data PDUs
- [GitHub #54341](https://github.com/zephyrproject-rtos/zephyr/issues/54341) - Bluetooth: Controller: Direction finding samples do not reconnect after disconnection
- [GitHub #54335](https://github.com/zephyrproject-rtos/zephyr/issues/54335) - tests/kernel/fatal/no-multithreading/kernel.no-mt.cpu\_exception failing on qemu\_cortex\_m3
- [GitHub #54334](https://github.com/zephyrproject-rtos/zephyr/issues/54334) - Need support to define partitions for usage with mcuboot
- [GitHub #54332](https://github.com/zephyrproject-rtos/zephyr/issues/54332) - LwM2M engine is does not go into non-block mode anymore in native\_posix target
- [GitHub #54327](https://github.com/zephyrproject-rtos/zephyr/issues/54327) - intel\_adsp: ace: various multicore bugs, timeouts
- [GitHub #54321](https://github.com/zephyrproject-rtos/zephyr/issues/54321) - ARC: unusable console after west flash or west debug with mdb runners
- [GitHub #54318](https://github.com/zephyrproject-rtos/zephyr/issues/54318) - boards: nucleo\_g474re: openocd runner is not stable enough for intensive testing
- [GitHub #54316](https://github.com/zephyrproject-rtos/zephyr/issues/54316) - RTT is not working correctly on STM32U5 series
- [GitHub #54315](https://github.com/zephyrproject-rtos/zephyr/issues/54315) - Problem seen with touch screen on RT1170 when running the LVGL sample
- [GitHub #54310](https://github.com/zephyrproject-rtos/zephyr/issues/54310) - Using NOCOPY code relocation generates a warning flag
- [GitHub #54287](https://github.com/zephyrproject-rtos/zephyr/issues/54287) - modem: hl7800: PSM hibernate draws excessive current
- [GitHub #54274](https://github.com/zephyrproject-rtos/zephyr/issues/54274) - newlib: Document CONFIG\_NEWLIB\_LIBC\_NANO default change
- [GitHub #54258](https://github.com/zephyrproject-rtos/zephyr/issues/54258) - boards: arm: twr\_ke18f: LPTMR always enabled, resulting in low system timer resolution
- [GitHub #54254](https://github.com/zephyrproject-rtos/zephyr/issues/54254) - tests: canbus: isotp: conformance: test fails with CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC=100
- [GitHub #54253](https://github.com/zephyrproject-rtos/zephyr/issues/54253) - v3.3.0-rc1: stm32: IPv6 neighbour solicitation packets are not received without CONFIG\_ETH\_STM32\_MULTICAST\_FILTER
- [GitHub #54247](https://github.com/zephyrproject-rtos/zephyr/issues/54247) - tests: net: tcp: net.tcp.simple fails
- [GitHub #54246](https://github.com/zephyrproject-rtos/zephyr/issues/54246) - Sample:subsys/ipc/rpmsg\_server:The two cores cannot communicate in nRF5340
- [GitHub #54241](https://github.com/zephyrproject-rtos/zephyr/issues/54241) - The cy8c95xx I2C GPIO expander support was broken in #47841
- [GitHub #54236](https://github.com/zephyrproject-rtos/zephyr/issues/54236) - b\_u585i\_iot02a\_ns: Can’t build TFM enabled samples (TF-M 1.7.0)
- [GitHub #54230](https://github.com/zephyrproject-rtos/zephyr/issues/54230) - STM32H7: Kernel crash with BCM4=0
- [GitHub #54225](https://github.com/zephyrproject-rtos/zephyr/issues/54225) - Intel CAVS: tests/lib/c\_lib/ fails
- [GitHub #54224](https://github.com/zephyrproject-rtos/zephyr/issues/54224) - Issues with picolibc on xtensa platforms
- [GitHub #54223](https://github.com/zephyrproject-rtos/zephyr/issues/54223) - Intel CAVS: tests/kernel/common/kernel.common.picolibc fails
- [GitHub #54214](https://github.com/zephyrproject-rtos/zephyr/issues/54214) - Display framebuffer allocation
- [GitHub #54210](https://github.com/zephyrproject-rtos/zephyr/issues/54210) - tests: drivers: udc drivers.udc fails
- [GitHub #54209](https://github.com/zephyrproject-rtos/zephyr/issues/54209) - USB C PD dead battery support
- [GitHub #54208](https://github.com/zephyrproject-rtos/zephyr/issues/54208) - Various RISC-V FPU context switching issues
- [GitHub #54205](https://github.com/zephyrproject-rtos/zephyr/issues/54205) - Regression: RiscV FPU regs not saved in multithreaded applications
- [GitHub #54202](https://github.com/zephyrproject-rtos/zephyr/issues/54202) - decawave\_dwm1001\_dev: i2c broken due to pinctrl\_nrf fix
- [GitHub #54190](https://github.com/zephyrproject-rtos/zephyr/issues/54190) - RP2040 cannot be compiled with C11 enabled
- [GitHub #54173](https://github.com/zephyrproject-rtos/zephyr/issues/54173) - Bluetooth: GATT: Change awareness of bonded GATT Client is not maintained on reconnection after reboot
- [GitHub #54172](https://github.com/zephyrproject-rtos/zephyr/issues/54172) - Bluetooth: GATT: Written value of gatt\_cf\_cfg data may be dropped on power down
- [GitHub #54148](https://github.com/zephyrproject-rtos/zephyr/issues/54148) - qemu\_x86\_tiny places picolibc text outside of pinned.text
- [GitHub #54140](https://github.com/zephyrproject-rtos/zephyr/issues/54140) - BUS FAULT when running nmap towards echo\_async sample
- [GitHub #54139](https://github.com/zephyrproject-rtos/zephyr/issues/54139) - Bluetooth: Audio: race hazard bt\_audio\_discover() callback vs unicast\_client\_ase\_cp\_discover()
- [GitHub #54138](https://github.com/zephyrproject-rtos/zephyr/issues/54138) - Buetooth: shell: bt adv-data isn’t working properly
- [GitHub #54136](https://github.com/zephyrproject-rtos/zephyr/issues/54136) - Socket error after deregistration causes RD client state machine to re-register
- [GitHub #54123](https://github.com/zephyrproject-rtos/zephyr/issues/54123) - Intel CAVS 25: tests/boards/intel\_adsp/ssp fails
- [GitHub #54117](https://github.com/zephyrproject-rtos/zephyr/issues/54117) - West flash fails on upload to Nucleo F303K8
- [GitHub #54104](https://github.com/zephyrproject-rtos/zephyr/issues/54104) - Bluetooth: Host: Bonding information distribution in the non-bondable mode
- [GitHub #54087](https://github.com/zephyrproject-rtos/zephyr/issues/54087) - tests:igmp:frdm\_k64f: igmp test fails
- [GitHub #54086](https://github.com/zephyrproject-rtos/zephyr/issues/54086) - test:rio:frdm\_k64f: rio user\_space test fails with zephyr-v3.2.0-3842-g7ffc20082023
- [GitHub #54078](https://github.com/zephyrproject-rtos/zephyr/issues/54078) - No activity on can\_tx when running the ISO-TP sample
- [GitHub #54072](https://github.com/zephyrproject-rtos/zephyr/issues/54072) - Bluetooth: Host: Periodic scanner does not differentiate between partial and incomplete data
- [GitHub #54065](https://github.com/zephyrproject-rtos/zephyr/issues/54065) - How To Change C++ Version Compilation Option For Freestanding Application?
- [GitHub #54053](https://github.com/zephyrproject-rtos/zephyr/issues/54053) - CI:frdm\_k64f: kernel.common.stack\_protection test failure
- [GitHub #54034](https://github.com/zephyrproject-rtos/zephyr/issues/54034) - QSPI: Unable to build the project when introduced DMA into external flash interfacing
- [GitHub #54017](https://github.com/zephyrproject-rtos/zephyr/issues/54017) - Modules: TF-M: Resolve QCBOR issues with TF-M 1.7.0
- [GitHub #54005](https://github.com/zephyrproject-rtos/zephyr/issues/54005) - esp32 Severe crash using modules with embedded PSRAM (eg esp32-wroom-32E-n8r2)
- [GitHub #54002](https://github.com/zephyrproject-rtos/zephyr/issues/54002) - mgmt: mcumgr: bluetooth transport: Inability to use refactored transport as a library in some circumstances
- [GitHub #53995](https://github.com/zephyrproject-rtos/zephyr/issues/53995) - drivers: ethernet: stm32: Enable ethernet statistics in the driver
- [GitHub #53994](https://github.com/zephyrproject-rtos/zephyr/issues/53994) - net: ethernet: Multicast receive packets statistics are not getting updated
- [GitHub #53991](https://github.com/zephyrproject-rtos/zephyr/issues/53991) - LE Audio: samples/bluetooth/broadcast\_audio\_sink configure error
- [GitHub #53989](https://github.com/zephyrproject-rtos/zephyr/issues/53989) - STM32 usb networking stack threading issue
- [GitHub #53967](https://github.com/zephyrproject-rtos/zephyr/issues/53967) - net: http client: HTTP timeout can lead to deadlock of global system queue
- [GitHub #53954](https://github.com/zephyrproject-rtos/zephyr/issues/53954) - tests: lib: ringbuffer: libraries.ring\_buffer hangs
- [GitHub #53952](https://github.com/zephyrproject-rtos/zephyr/issues/53952) - USB C PD sink sample stops working when connected to a non-PD source
- [GitHub #53942](https://github.com/zephyrproject-rtos/zephyr/issues/53942) - Websocket: No close message on websocket close
- [GitHub #53936](https://github.com/zephyrproject-rtos/zephyr/issues/53936) - Enabling CONFIG\_TRACING and CONFIG\_EVENTS causes undefined reference error
- [GitHub #53935](https://github.com/zephyrproject-rtos/zephyr/issues/53935) - stm32 iwdt wdt\_install\_timeout not working properly
- [GitHub #53926](https://github.com/zephyrproject-rtos/zephyr/issues/53926) - Bluetooth Mesh stack question
- [GitHub #53916](https://github.com/zephyrproject-rtos/zephyr/issues/53916) - Multichannel PWM for STM32U575
- [GitHub #53913](https://github.com/zephyrproject-rtos/zephyr/issues/53913) - net: ip: igmp: IGMP doesn’t get initialised because the iface->config.ip.ipv4 pointer is not initialised
- [GitHub #53911](https://github.com/zephyrproject-rtos/zephyr/issues/53911) - Info request: SMP Hash
- [GitHub #53900](https://github.com/zephyrproject-rtos/zephyr/issues/53900) - led\_set\_brightness() is not setting brightness after led\_blink() for STM32U575
- [GitHub #53885](https://github.com/zephyrproject-rtos/zephyr/issues/53885) - Ethernet TCP Client Issue description with iperf/zperf
- [GitHub #53876](https://github.com/zephyrproject-rtos/zephyr/issues/53876) - The handle of att indication violates the spec
- [GitHub #53862](https://github.com/zephyrproject-rtos/zephyr/issues/53862) - Switching from USB to UART
- [GitHub #53859](https://github.com/zephyrproject-rtos/zephyr/issues/53859) - RFC: Board porting guide: Do not assume OS or default ports for board files
- [GitHub #53808](https://github.com/zephyrproject-rtos/zephyr/issues/53808) - Improve PLLI2S VCO precision
- [GitHub #53805](https://github.com/zephyrproject-rtos/zephyr/issues/53805) - peripheral\_dis compilation reports RAM overflow for BBC microbit
- [GitHub #53799](https://github.com/zephyrproject-rtos/zephyr/issues/53799) - Info request: SMP hash definition
- [GitHub #53786](https://github.com/zephyrproject-rtos/zephyr/issues/53786) - BLE:DF: slot\_plus\_us is not set properly
- [GitHub #53782](https://github.com/zephyrproject-rtos/zephyr/issues/53782) - nrf5340dk: missing i2c bias pull up
- [GitHub #53781](https://github.com/zephyrproject-rtos/zephyr/issues/53781) - Allow resetting STM32 peripherals through RCC peripheral reset register
- [GitHub #53777](https://github.com/zephyrproject-rtos/zephyr/issues/53777) - mgmt: mcumgr: Change transport selects to depends on
- [GitHub #53773](https://github.com/zephyrproject-rtos/zephyr/issues/53773) - drivers: ethernet: stm32: Completion of enabling the multicast hash filter
- [GitHub #53756](https://github.com/zephyrproject-rtos/zephyr/issues/53756) - esp32 - Wrong value for the default cpu freq -> crash on assert
- [GitHub #53753](https://github.com/zephyrproject-rtos/zephyr/issues/53753) - [DOC] Mismatch of driver sample overview
- [GitHub #53744](https://github.com/zephyrproject-rtos/zephyr/issues/53744) - ztest: assert() functions does not always retuns
- [GitHub #53723](https://github.com/zephyrproject-rtos/zephyr/issues/53723) - device tree macro: GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR does not work
- [GitHub #53720](https://github.com/zephyrproject-rtos/zephyr/issues/53720) - Bluetooth: Controller: Incorrect address type for PA sync established
- [GitHub #53715](https://github.com/zephyrproject-rtos/zephyr/issues/53715) - mec15xxevb\_assy6853: broken UART console output
- [GitHub #53707](https://github.com/zephyrproject-rtos/zephyr/issues/53707) - fs: fcb: Add option to disable CRC for FCB entries
- [GitHub #53697](https://github.com/zephyrproject-rtos/zephyr/issues/53697) - Can not run the usb mass storage demo on NXP mimxrt595\_evk\_cm33
- [GitHub #53696](https://github.com/zephyrproject-rtos/zephyr/issues/53696) - sysbuild should not parse the board revision conf
- [GitHub #53689](https://github.com/zephyrproject-rtos/zephyr/issues/53689) - boards: nrf52840dongle\_nrf52840 is missing storage partition definition
- [GitHub #53676](https://github.com/zephyrproject-rtos/zephyr/issues/53676) - net: lwm2m: inconsistent path string handling throughout the codebase
- [GitHub #53673](https://github.com/zephyrproject-rtos/zephyr/issues/53673) - samples: posix: gettimeofday does not build on native\_posix
- [GitHub #53663](https://github.com/zephyrproject-rtos/zephyr/issues/53663) - Error while trying to flash nucleo\_f446re: TARGET: stm32f4x.cpu - Not halted
- [GitHub #53656](https://github.com/zephyrproject-rtos/zephyr/issues/53656) - twister: samples: Bogus yaml for code\_relocation sample
- [GitHub #53654](https://github.com/zephyrproject-rtos/zephyr/issues/53654) - SPI2 not working on STM32L412
- [GitHub #53652](https://github.com/zephyrproject-rtos/zephyr/issues/53652) - samples: mgmt: mcumgr: fs overlay does not work
- [GitHub #53642](https://github.com/zephyrproject-rtos/zephyr/issues/53642) - Display driver sample seems to mix up RGB565 and BGR565
- [GitHub #53636](https://github.com/zephyrproject-rtos/zephyr/issues/53636) - cdc\_acm fails on lpcxpresso55s69 board
- [GitHub #53630](https://github.com/zephyrproject-rtos/zephyr/issues/53630) - net: ieee802154\_6lo: REGRESSION: L2 MAC byte swapping results in wrong IPHC decompression
- [GitHub #53617](https://github.com/zephyrproject-rtos/zephyr/issues/53617) - unicast\_audio\_client and unicast\_audio\_server example assert
- [GitHub #53612](https://github.com/zephyrproject-rtos/zephyr/issues/53612) - file system (LFS?): failure to expand file with truncate
- [GitHub #53610](https://github.com/zephyrproject-rtos/zephyr/issues/53610) - k\_malloc and settings
- [GitHub #53604](https://github.com/zephyrproject-rtos/zephyr/issues/53604) - testsuite: Broken Kconfig prevents building tests for nrf52840dk\_nrf52840 platform
- [GitHub #53584](https://github.com/zephyrproject-rtos/zephyr/issues/53584) - STM32F1 PWM Input Capture Issue
- [GitHub #53579](https://github.com/zephyrproject-rtos/zephyr/issues/53579) - add\_compile\_definitions does not “propagate upwards” as supposed to when using west
- [GitHub #53568](https://github.com/zephyrproject-rtos/zephyr/issues/53568) - Kconfig search has white on white text
- [GitHub #53566](https://github.com/zephyrproject-rtos/zephyr/issues/53566) - Use fixup commits during code review
- [GitHub #53559](https://github.com/zephyrproject-rtos/zephyr/issues/53559) - mgmt: mcumgr: explore why UART interface is so slow (possible go application fault)
- [GitHub #53556](https://github.com/zephyrproject-rtos/zephyr/issues/53556) - Cannot add multiple out-of-the-tree secure partitions
- [GitHub #53549](https://github.com/zephyrproject-rtos/zephyr/issues/53549) - mgmt: mcumgr: callbacks: Callbacks events for a single group should be able to be combined
- [GitHub #53548](https://github.com/zephyrproject-rtos/zephyr/issues/53548) - net: ip: igmp: Mechanism to add MAC address for IGMP all systems multicast address to an ethernet multicast hash filter
- [GitHub #53535](https://github.com/zephyrproject-rtos/zephyr/issues/53535) - define a recommended process in zephyr for a CI framework integration
- [GitHub #53520](https://github.com/zephyrproject-rtos/zephyr/issues/53520) - tests: drivers: gpio: gpio\_api\_1pin: peripheral.gpio.1pin fails
- [GitHub #53513](https://github.com/zephyrproject-rtos/zephyr/issues/53513) - STM32 PWM Input Capture Issue
- [GitHub #53500](https://github.com/zephyrproject-rtos/zephyr/issues/53500) - `net_tcp: context->tcp == NULL` error messages during TCP connection
- [GitHub #53495](https://github.com/zephyrproject-rtos/zephyr/issues/53495) - RFC: treewide: python: argparse default configuration allows shortened command arguments
- [GitHub #53490](https://github.com/zephyrproject-rtos/zephyr/issues/53490) - Peridic current spike using tickless Zephyr
- [GitHub #53488](https://github.com/zephyrproject-rtos/zephyr/issues/53488) - Missing UUID for PBA and TMAS
- [GitHub #53487](https://github.com/zephyrproject-rtos/zephyr/issues/53487) - west: flash: stm32cubeprogrammer: Reset command line argument is wrong
- [GitHub #53474](https://github.com/zephyrproject-rtos/zephyr/issues/53474) - Sysbuild cmake enters infinite loop if 2 images are added to a build with the same name
- [GitHub #53470](https://github.com/zephyrproject-rtos/zephyr/issues/53470) - Unable to build using Arduino Zero
- [GitHub #53468](https://github.com/zephyrproject-rtos/zephyr/issues/53468) - STM32 single-wire UART not working when poll-out more than 1 char
- [GitHub #53466](https://github.com/zephyrproject-rtos/zephyr/issues/53466) - Nucleo F413ZH CAN bus support
- [GitHub #53458](https://github.com/zephyrproject-rtos/zephyr/issues/53458) - IPv4 address autoconfiguration leaks TX packets/buffers
- [GitHub #53455](https://github.com/zephyrproject-rtos/zephyr/issues/53455) - GATT: Deadlock while sending GATT notification from system workqueue thread
- [GitHub #53451](https://github.com/zephyrproject-rtos/zephyr/issues/53451) - USB: Suspending CDC ACM can lead to endpoint/transfer state mismatch
- [GitHub #53446](https://github.com/zephyrproject-rtos/zephyr/issues/53446) - Bluetooth: Controller: ll\_setup\_iso\_path not working if both CIS and BIS supported
- [GitHub #53438](https://github.com/zephyrproject-rtos/zephyr/issues/53438) - unable to wakeup from Stop2 mode
- [GitHub #53437](https://github.com/zephyrproject-rtos/zephyr/issues/53437) - WaveShare xnucleo\_f411re: Error: `** Unable to reset target **`
- [GitHub #53433](https://github.com/zephyrproject-rtos/zephyr/issues/53433) - flash content erase in bootloader region at run time
- [GitHub #53430](https://github.com/zephyrproject-rtos/zephyr/issues/53430) - drivers: display: otm8009a: import 3rd-party source
- [GitHub #53425](https://github.com/zephyrproject-rtos/zephyr/issues/53425) - Do we have support for rtc subsecond calculation in zephyr.
- [GitHub #53424](https://github.com/zephyrproject-rtos/zephyr/issues/53424) - Reopen issue #49390
- [GitHub #53423](https://github.com/zephyrproject-rtos/zephyr/issues/53423) - [bisected] logging.log\_msg\_no\_overflow is failing on qemu\_riscv64
- [GitHub #53421](https://github.com/zephyrproject-rtos/zephyr/issues/53421) - cpp: defined popcount macro prevents use of std::popcount
- [GitHub #53419](https://github.com/zephyrproject-rtos/zephyr/issues/53419) - net: stats: DHCP packets are not counted as part of UDP counters
- [GitHub #53417](https://github.com/zephyrproject-rtos/zephyr/issues/53417) - CAN-FD / MCAN driver: Possible variable overflow for some MCUs
- [GitHub #53407](https://github.com/zephyrproject-rtos/zephyr/issues/53407) - Support of regex
- [GitHub #53385](https://github.com/zephyrproject-rtos/zephyr/issues/53385) - SWD not working on STM32F405
- [GitHub #53366](https://github.com/zephyrproject-rtos/zephyr/issues/53366) - net: ethernet: provide a way to get ethernet config
- [GitHub #53361](https://github.com/zephyrproject-rtos/zephyr/issues/53361) - Adding I2C devices SX1509B to Devicetree with the same address on different busses generates FATAL ERROR.
- [GitHub #53360](https://github.com/zephyrproject-rtos/zephyr/issues/53360) - kernel: k\_msgq: add peek\_more function
- [GitHub #53347](https://github.com/zephyrproject-rtos/zephyr/issues/53347) - WINC1500 socket recv fail
- [GitHub #53340](https://github.com/zephyrproject-rtos/zephyr/issues/53340) - net: lwm2m: add BinaryAppDataContainer object (19)
- [GitHub #53335](https://github.com/zephyrproject-rtos/zephyr/issues/53335) - Undeclared constants in devicetree\_generated.h
- [GitHub #53326](https://github.com/zephyrproject-rtos/zephyr/issues/53326) - usb: device: usb\_dfu: k\_mutex is being called from isr
- [GitHub #53315](https://github.com/zephyrproject-rtos/zephyr/issues/53315) - Fix possible underflow in tcp flags parse.
- [GitHub #53306](https://github.com/zephyrproject-rtos/zephyr/issues/53306) - scripts: utils: migrate\_mcumgr\_kconfigs.py: Missing options
- [GitHub #53301](https://github.com/zephyrproject-rtos/zephyr/issues/53301) - Bluetooth: Controller: Cannot recreate CIG
- [GitHub #53294](https://github.com/zephyrproject-rtos/zephyr/issues/53294) - samples: mgmt: mcumgr: smp\_svr: UDP file can be removed
- [GitHub #53293](https://github.com/zephyrproject-rtos/zephyr/issues/53293) - mgmt: mcumgr: CONFIG\_MCUMGR\_GRP\_IMG\_REJECT\_DIRECT\_XIP\_MISMATCHED\_SLOT causes a build failure
- [GitHub #53285](https://github.com/zephyrproject-rtos/zephyr/issues/53285) - SNTP & DATE\_TIME & SERVER ADDRESS configuration and behavior
- [GitHub #53280](https://github.com/zephyrproject-rtos/zephyr/issues/53280) - Bluetooth: security level failure with multiple links
- [GitHub #53276](https://github.com/zephyrproject-rtos/zephyr/issues/53276) - doc: mgmt: mcumgr: fix “some unspecified” error
- [GitHub #53271](https://github.com/zephyrproject-rtos/zephyr/issues/53271) - modules: segger: KConfigs are broken
- [GitHub #53259](https://github.com/zephyrproject-rtos/zephyr/issues/53259) - RFC: API Change: dma: callback status
- [GitHub #53254](https://github.com/zephyrproject-rtos/zephyr/issues/53254) - Bluetooth: bt\_conn\_foreach() reports unstable conn ref before the connection is completed
- [GitHub #53247](https://github.com/zephyrproject-rtos/zephyr/issues/53247) - ATT timeout followed by a segmentation fault
- [GitHub #53242](https://github.com/zephyrproject-rtos/zephyr/issues/53242) - Controller in HCI UART RAW mode responds to Stop Discovery mgmt command with 0x0b status code
- [GitHub #53240](https://github.com/zephyrproject-rtos/zephyr/issues/53240) - Task Watchdog Fallback Timeout Before Installing Timeout - STM32
- [GitHub #53236](https://github.com/zephyrproject-rtos/zephyr/issues/53236) - Make USB VBUS sensing configurable for STM32 devices
- [GitHub #53231](https://github.com/zephyrproject-rtos/zephyr/issues/53231) - drivers/flash/flash\_stm32l5\_u5.c : unable to use full 2MB flash with TF-M activated
- [GitHub #53227](https://github.com/zephyrproject-rtos/zephyr/issues/53227) - mgmt: mcumgr: Possible instability with USB CDC data transfer
- [GitHub #53223](https://github.com/zephyrproject-rtos/zephyr/issues/53223) - LE Audio: Add interleaved packing for LE audio
- [GitHub #53221](https://github.com/zephyrproject-rtos/zephyr/issues/53221) - Systemview trace id overlap
- [GitHub #53209](https://github.com/zephyrproject-rtos/zephyr/issues/53209) - LwM2M: Replace pathstrings from the APIs
- [GitHub #53194](https://github.com/zephyrproject-rtos/zephyr/issues/53194) - tests: kernel: timer: starve: DTS failure stm32f3\_seco\_d23
- [GitHub #53189](https://github.com/zephyrproject-rtos/zephyr/issues/53189) - Mesh CI failure with BT\_MESH\_LPN\_RECV\_DELAY
- [GitHub #53175](https://github.com/zephyrproject-rtos/zephyr/issues/53175) - Select pin properties from shield overlay
- [GitHub #53164](https://github.com/zephyrproject-rtos/zephyr/issues/53164) - mgmt: mcumgr: NMP Timeout with smp\_svr example
- [GitHub #53158](https://github.com/zephyrproject-rtos/zephyr/issues/53158) - SPIM transaction timeout leads to crash
- [GitHub #53151](https://github.com/zephyrproject-rtos/zephyr/issues/53151) - fs: FAT\_FS\_API MKFS test uses driver specific calls
- [GitHub #53147](https://github.com/zephyrproject-rtos/zephyr/issues/53147) - usb: cdc\_acm: log related warning promoted to error
- [GitHub #53141](https://github.com/zephyrproject-rtos/zephyr/issues/53141) - For pinctrl on STM32 pin cannot be defined as push-pull with low level
- [GitHub #53129](https://github.com/zephyrproject-rtos/zephyr/issues/53129) - Build fails on ESP32 when enabling websocket client API
- [GitHub #53103](https://github.com/zephyrproject-rtos/zephyr/issues/53103) - Zephyr shell on litex : number higher than 10 are printed as repeated hex
- [GitHub #53101](https://github.com/zephyrproject-rtos/zephyr/issues/53101) - esp32: The startup code hangs after reboot via sys\_reboot(…)
- [GitHub #53094](https://github.com/zephyrproject-rtos/zephyr/issues/53094) - Extend Zperf command
- [GitHub #53093](https://github.com/zephyrproject-rtos/zephyr/issues/53093) - ARM: Ability to query CFSR on exception
- [GitHub #53059](https://github.com/zephyrproject-rtos/zephyr/issues/53059) - Bluetooth: peripheral GATT notification call takes a lot of time
- [GitHub #53049](https://github.com/zephyrproject-rtos/zephyr/issues/53049) - Bluetooth: LL assertion fail with peripherals connect/disconnect rounds
- [GitHub #53048](https://github.com/zephyrproject-rtos/zephyr/issues/53048) - Bluetooth: legacy advertising doesn’t resume if CONFIG\_BT\_EXT\_ADV=y
- [GitHub #53046](https://github.com/zephyrproject-rtos/zephyr/issues/53046) - Bluetooth: Failed to set security level for the second connection
- [GitHub #53043](https://github.com/zephyrproject-rtos/zephyr/issues/53043) - Bluetooth: Peripheral misses notifications from Central after setting security level
- [GitHub #53033](https://github.com/zephyrproject-rtos/zephyr/issues/53033) - tests-ci : libraries: encoding: jwt test Failed
- [GitHub #53034](https://github.com/zephyrproject-rtos/zephyr/issues/53034) - tests-ci : os: mgmt: info\_net test No Console Output(Timeout)
- [GitHub #53035](https://github.com/zephyrproject-rtos/zephyr/issues/53035) - tests-ci : crypto: rand32: random\_ctr\_drbg test No Console Output(Timeout)
- [GitHub #53036](https://github.com/zephyrproject-rtos/zephyr/issues/53036) - tests-ci : testing: ztest: base.verbose\_1 test No Console Output(Timeout)
- [GitHub #53037](https://github.com/zephyrproject-rtos/zephyr/issues/53037) - tests-ci : net: mqtt\_sn: client test No Console Output(Timeout)
- [GitHub #53038](https://github.com/zephyrproject-rtos/zephyr/issues/53038) - tests-ci : net: socket: mgmt test No Console Output(Timeout)
- [GitHub #53039](https://github.com/zephyrproject-rtos/zephyr/issues/53039) - tests-ci : net: socket: af\_packet.ipproto\_raw test No Console Output(Timeout)
- [GitHub #53040](https://github.com/zephyrproject-rtos/zephyr/issues/53040) - tests-ci : net: ipv4: fragment test No Console Output(Timeout)
- [GitHub #53019](https://github.com/zephyrproject-rtos/zephyr/issues/53019) - random: Zephyr enables TEST\_RANDOM\_GENERATOR when it should not
- [GitHub #53012](https://github.com/zephyrproject-rtos/zephyr/issues/53012) - stm32u5: timer api: lptim: k\_msleep is twice long as expected
- [GitHub #53010](https://github.com/zephyrproject-rtos/zephyr/issues/53010) - timers: large drift if hardware timer has a low resolution
- [GitHub #53007](https://github.com/zephyrproject-rtos/zephyr/issues/53007) - Bluetooth: Notification callback is called with incorrect connection reference
- [GitHub #53002](https://github.com/zephyrproject-rtos/zephyr/issues/53002) - Incorrect hardware reset cause sets for watchdog reset on stm32h743zi
- [GitHub #52996](https://github.com/zephyrproject-rtos/zephyr/issues/52996) - kconfig: Use of multiple fragment files with OVERLAY\_CONFIG not taking effect
- [GitHub #52995](https://github.com/zephyrproject-rtos/zephyr/issues/52995) - Add triage permissions for dianazig
- [GitHub #52983](https://github.com/zephyrproject-rtos/zephyr/issues/52983) - Bluetooth: Audio: BT\_CODEC\_LC3\_CONFIG\_DATA fails to compile with \_frame\_blocks\_per\_sdu > 1
- [GitHub #52981](https://github.com/zephyrproject-rtos/zephyr/issues/52981) - LOG\_MODE\_MINIMAL do not work with USB\_CDC for nRF52840
- [GitHub #52975](https://github.com/zephyrproject-rtos/zephyr/issues/52975) - posix: clock: current method of capturing elapsed time leads to loss in seconds
- [GitHub #52970](https://github.com/zephyrproject-rtos/zephyr/issues/52970) - samples/net/wifi example does not work with ESP32
- [GitHub #52962](https://github.com/zephyrproject-rtos/zephyr/issues/52962) - Bluetooth non-functional on nRF5340 target
- [GitHub #52935](https://github.com/zephyrproject-rtos/zephyr/issues/52935) - Missing Libraries
- [GitHub #52931](https://github.com/zephyrproject-rtos/zephyr/issues/52931) - Filesystem Write Fails with Some SD-Cards
- [GitHub #52925](https://github.com/zephyrproject-rtos/zephyr/issues/52925) - Using #define LOG\_LEVEL 0 does not filter out logs
- [GitHub #52920](https://github.com/zephyrproject-rtos/zephyr/issues/52920) - qemu\_cortex\_r5: tests/ztest/base
- [GitHub #52918](https://github.com/zephyrproject-rtos/zephyr/issues/52918) - qemu\_cortex\_r5` CI fails
- [GitHub #52914](https://github.com/zephyrproject-rtos/zephyr/issues/52914) - drivers: adc: ADC\_CONFIGURABLE\_INPUTS confict between 2 ADCs
- [GitHub #52913](https://github.com/zephyrproject-rtos/zephyr/issues/52913) - twister build fails but returns exit code of 0
- [GitHub #52909](https://github.com/zephyrproject-rtos/zephyr/issues/52909) - usb: usb don’t work after switch from Zephyr 2.7.3 to 3.2.99 on i.MX RT1020
- [GitHub #52898](https://github.com/zephyrproject-rtos/zephyr/issues/52898) - mgmt: mcumgr: replace cmake functions without zephyr prefix to have zephyr prefix
- [GitHub #52882](https://github.com/zephyrproject-rtos/zephyr/issues/52882) - Sample applications that enable USB and error if it fails are incompatible with boards like thingy53 with auto-USB init (i.e. USB CDC for logging)
- [GitHub #52878](https://github.com/zephyrproject-rtos/zephyr/issues/52878) - Bluetooth: Unable use native\_posix with shell demo
- [GitHub #52872](https://github.com/zephyrproject-rtos/zephyr/issues/52872) - Logging to USB CDC ACM limited to very low rate
- [GitHub #52870](https://github.com/zephyrproject-rtos/zephyr/issues/52870) - ESP32-C3 System clock resolution improvements
- [GitHub #52857](https://github.com/zephyrproject-rtos/zephyr/issues/52857) - Adafruit WINC1500 Wifi Shield doesn’t work on nRF528XX
- [GitHub #52855](https://github.com/zephyrproject-rtos/zephyr/issues/52855) - Improve artifact generation for split build/test operation of twister
- [GitHub #52854](https://github.com/zephyrproject-rtos/zephyr/issues/52854) - twister build fails but returns exit code of 0
- [GitHub #52838](https://github.com/zephyrproject-rtos/zephyr/issues/52838) - Bluetooth: audio：invalid ase state transition
- [GitHub #52833](https://github.com/zephyrproject-rtos/zephyr/issues/52833) - Bluetooth Controller assertion on sys\_reboot() with active connections (lll\_preempt\_calc: Actual EVENT\_OVERHEAD\_START\_US)
- [GitHub #52829](https://github.com/zephyrproject-rtos/zephyr/issues/52829) - kernel/sched: Fix SMP race on pend
- [GitHub #52818](https://github.com/zephyrproject-rtos/zephyr/issues/52818) - samples: subsys: usb: shell: sample.usbd.shell fails - no output from console
- [GitHub #52817](https://github.com/zephyrproject-rtos/zephyr/issues/52817) - tests: drivers: udc: dirvers.udc fails
- [GitHub #52813](https://github.com/zephyrproject-rtos/zephyr/issues/52813) - stm32h7: dsi: ltdc: clock: PLL3: clock not set up correctly or side effect
- [GitHub #52812](https://github.com/zephyrproject-rtos/zephyr/issues/52812) - Various problems with pipes (Not unblocking, Data Access Violation, unblocking wrong thread…)
- [GitHub #52805](https://github.com/zephyrproject-rtos/zephyr/issues/52805) - Code crashing due to ADC Sync operation (STM32F4)
- [GitHub #52803](https://github.com/zephyrproject-rtos/zephyr/issues/52803) - Kconfig: STM32F4 UF2 family ID
- [GitHub #52795](https://github.com/zephyrproject-rtos/zephyr/issues/52795) - Remove deprecated tinycbor module
- [GitHub #52794](https://github.com/zephyrproject-rtos/zephyr/issues/52794) - Possible regression for printk() output of i2c sensor data on amg88xx sample
- [GitHub #52788](https://github.com/zephyrproject-rtos/zephyr/issues/52788) - Re-enable LVGL support for M0 processors.
- [GitHub #52784](https://github.com/zephyrproject-rtos/zephyr/issues/52784) - NRF\_DRIVE\_S0D1 option is not always set in the nordic,nrf-twi and nordic,nrf-twim nodes, when using shield?
- [GitHub #52779](https://github.com/zephyrproject-rtos/zephyr/issues/52779) - Error While adding the mcuboot folder in repo.
- [GitHub #52776](https://github.com/zephyrproject-rtos/zephyr/issues/52776) - ite: eSPI driver: espi\_it8xxx2\_send\_vwire() is not setting valid flag along with respective virtual wire when invoked from app code.
- [GitHub #52754](https://github.com/zephyrproject-rtos/zephyr/issues/52754) - tests/drivers/bbram: Refactor to use a common prj.conf
- [GitHub #52749](https://github.com/zephyrproject-rtos/zephyr/issues/52749) - posix: getopt: cannot use getopt() in a standard way
- [GitHub #52739](https://github.com/zephyrproject-rtos/zephyr/issues/52739) - Newlib defines POSIX primitives when -std=gnu
- [GitHub #52721](https://github.com/zephyrproject-rtos/zephyr/issues/52721) - Minimal logging does not work if printk and boot banner are disabled
- [GitHub #52718](https://github.com/zephyrproject-rtos/zephyr/issues/52718) - Simplify handling of fragments in `net_buf`
- [GitHub #52709](https://github.com/zephyrproject-rtos/zephyr/issues/52709) - samples: subsys: nvs: sample.nvs.basic does not complete within twister default timeout
- [GitHub #52708](https://github.com/zephyrproject-rtos/zephyr/issues/52708) - samples: drivers: watchdog: sample.drivers.watchdog loops endlessly
- [GitHub #52707](https://github.com/zephyrproject-rtos/zephyr/issues/52707) - samples: subsys: task\_wdt: sample.subsys.task\_wdt loops endlessly
- [GitHub #52703](https://github.com/zephyrproject-rtos/zephyr/issues/52703) - tests: subsys: usb: device: usb.device USAGE FAULT exception
- [GitHub #52691](https://github.com/zephyrproject-rtos/zephyr/issues/52691) - cannot read octospi flash when partition size exceeds 4mb
- [GitHub #52690](https://github.com/zephyrproject-rtos/zephyr/issues/52690) - coredump: stm32l5: I-cache error on coredump backend in flash
- [GitHub #52675](https://github.com/zephyrproject-rtos/zephyr/issues/52675) - I2C: STM32F0 can’t switch to HSI clock by default and change timing
- [GitHub #52673](https://github.com/zephyrproject-rtos/zephyr/issues/52673) - mcux: flexcan: forever waiting semaphore in can\_send()
- [GitHub #52670](https://github.com/zephyrproject-rtos/zephyr/issues/52670) - tests: subsys: usb: device: usb.device hangs
- [GitHub #52652](https://github.com/zephyrproject-rtos/zephyr/issues/52652) - drivers: sensors: bmi08x config file
- [GitHub #52641](https://github.com/zephyrproject-rtos/zephyr/issues/52641) - armv7: mpu: RASR size field incorrectly initialized
- [GitHub #52632](https://github.com/zephyrproject-rtos/zephyr/issues/52632) - MQTT over WebSockets: After hours of running time receiving published messages is strongly delayed
- [GitHub #52628](https://github.com/zephyrproject-rtos/zephyr/issues/52628) - spi: NXP MCUX LPSPI driver does not correctly change baud rate once configured
- [GitHub #52626](https://github.com/zephyrproject-rtos/zephyr/issues/52626) - Improve LLCP unit tests
- [GitHub #52625](https://github.com/zephyrproject-rtos/zephyr/issues/52625) - USB device: mimxrt685\_evk\_cm33: premature ZLP during control IN transfer
- [GitHub #52614](https://github.com/zephyrproject-rtos/zephyr/issues/52614) - Empty “west build –test-item” doesn’t report warnings/errors
- [GitHub #52602](https://github.com/zephyrproject-rtos/zephyr/issues/52602) - tests: subsys: settings: file\_littlefs: system.settings.file\_littlefs.raw fails
- [GitHub #52598](https://github.com/zephyrproject-rtos/zephyr/issues/52598) - esp32c3 Unable to do any timing faster than 1ms
- [GitHub #52595](https://github.com/zephyrproject-rtos/zephyr/issues/52595) - Twister: unable to run tests on real hardware
- [GitHub #52588](https://github.com/zephyrproject-rtos/zephyr/issues/52588) - ESP32c3 SPI driver DMA mode limited to 64 byte chunks
- [GitHub #52566](https://github.com/zephyrproject-rtos/zephyr/issues/52566) - Error while build esp32 samples/hello\_world
- [GitHub #52563](https://github.com/zephyrproject-rtos/zephyr/issues/52563) - spi\_transceive with DMA for STM32 does not work for devices with 16 bit words.
- [GitHub #52561](https://github.com/zephyrproject-rtos/zephyr/issues/52561) - fsl\_flexcan missing flags
- [GitHub #52559](https://github.com/zephyrproject-rtos/zephyr/issues/52559) - Compiler cannot include C++ headers when both PICOLIBC and LIB\_CPLUSPLUS options are set
- [GitHub #52556](https://github.com/zephyrproject-rtos/zephyr/issues/52556) - adc driver sample was failing with STM32 nucleo\_f429zi board
- [GitHub #52548](https://github.com/zephyrproject-rtos/zephyr/issues/52548) - Late device driver initialization
- [GitHub #52539](https://github.com/zephyrproject-rtos/zephyr/issues/52539) - Broken linker script for the esp32 platform
- [GitHub #52534](https://github.com/zephyrproject-rtos/zephyr/issues/52534) - Missing include to src/core/lv\_theme.h in src/themes/mono/lv\_theme\_mono.h
- [GitHub #52528](https://github.com/zephyrproject-rtos/zephyr/issues/52528) - Zephyr support for Nordic devices Thingy with TFLM
- [GitHub #52527](https://github.com/zephyrproject-rtos/zephyr/issues/52527) - net: lwm2m: wrong SenML CBOR object link encoding
- [GitHub #52526](https://github.com/zephyrproject-rtos/zephyr/issues/52526) - Simplify lvgl.h file by creating more header files inside module’s sub-filoders (src/widgets and src/layouts)
- [GitHub #52518](https://github.com/zephyrproject-rtos/zephyr/issues/52518) - lib: posix: usleep() does not follow the POSIX spec
- [GitHub #52517](https://github.com/zephyrproject-rtos/zephyr/issues/52517) - lib: posix: sleep() does not return the number of seconds left if interrupted
- [GitHub #52506](https://github.com/zephyrproject-rtos/zephyr/issues/52506) - GPIO multiple gaps cause incorrect pinout check
- [GitHub #52493](https://github.com/zephyrproject-rtos/zephyr/issues/52493) - net: lwm2m: add 32 bits floating point support
- [GitHub #52486](https://github.com/zephyrproject-rtos/zephyr/issues/52486) - Losing connection with JLink on STM32H743IIK6 with Zephyr 2.7.2
- [GitHub #52479](https://github.com/zephyrproject-rtos/zephyr/issues/52479) - incorrect canopennode SDO CRC
- [GitHub #52472](https://github.com/zephyrproject-rtos/zephyr/issues/52472) - Set compiler options only for a custom/external module
- [GitHub #52464](https://github.com/zephyrproject-rtos/zephyr/issues/52464) - LE Audio: Unicast Client failing to create the CIG
- [GitHub #52462](https://github.com/zephyrproject-rtos/zephyr/issues/52462) - uart: stm32: UART clock source not initialized
- [GitHub #52457](https://github.com/zephyrproject-rtos/zephyr/issues/52457) - compilation error with “west build -b lpcxpresso54114\_m4 samples/subsys/ipc/openamp/ “
- [GitHub #52455](https://github.com/zephyrproject-rtos/zephyr/issues/52455) - ARC: MWDT: minimal libc includes
- [GitHub #52452](https://github.com/zephyrproject-rtos/zephyr/issues/52452) - drivers: pwm: loopback test fails on frdm\_k64f
- [GitHub #52449](https://github.com/zephyrproject-rtos/zephyr/issues/52449) - net: ip: igmp: IGMP v2 membership reports are sent to 224.0.0.2 instead of the group being reported
- [GitHub #52448](https://github.com/zephyrproject-rtos/zephyr/issues/52448) - esp32: subsys: settings: not working properly on esp\_wrover\_kit
- [GitHub #52443](https://github.com/zephyrproject-rtos/zephyr/issues/52443) - Concerns with maintaining separate kernel device drivers for fuel-gauge and charger ICs
- [GitHub #52415](https://github.com/zephyrproject-rtos/zephyr/issues/52415) - tests: kernel: timer: timer\_behavior: kernel.timer.timer fails
- [GitHub #52412](https://github.com/zephyrproject-rtos/zephyr/issues/52412) - doc: mgmt: mcumgr: Clarify that hash in img\_mgmt is a full sha256 hash and required
- [GitHub #52409](https://github.com/zephyrproject-rtos/zephyr/issues/52409) - STM32H7: ethernet: Device fails to receive any IP packets over ethernet after receiving UDP/IP multicast at a constant rate for some time
- [GitHub #52407](https://github.com/zephyrproject-rtos/zephyr/issues/52407) - tests: subsys: mgmt: mcumgr: Test needed that enables all features/Kconfigs
- [GitHub #52404](https://github.com/zephyrproject-rtos/zephyr/issues/52404) - mgmt: mcumgr: Callback include file has file name typo
- [GitHub #52401](https://github.com/zephyrproject-rtos/zephyr/issues/52401) - mgmt: mcumgr: Leftover files after directory update
- [GitHub #52399](https://github.com/zephyrproject-rtos/zephyr/issues/52399) - cmake error
- [GitHub #52393](https://github.com/zephyrproject-rtos/zephyr/issues/52393) - Controller: ACL packets NACKed after Data Length Update
- [GitHub #52376](https://github.com/zephyrproject-rtos/zephyr/issues/52376) - Cannot build apps with main in a .cpp file
- [GitHub #52366](https://github.com/zephyrproject-rtos/zephyr/issues/52366) - LE Audio: Missing released callback for streams on ACL disconnect
- [GitHub #52360](https://github.com/zephyrproject-rtos/zephyr/issues/52360) - samples/net/sockets/socketpair does not run as expected
- [GitHub #52353](https://github.com/zephyrproject-rtos/zephyr/issues/52353) - bug: sysbuild lost board reversion here
- [GitHub #52352](https://github.com/zephyrproject-rtos/zephyr/issues/52352) - Questions about newlib library
- [GitHub #52351](https://github.com/zephyrproject-rtos/zephyr/issues/52351) - Bluetooth: Controller: ISOAL ASSERT failure
- [GitHub #52344](https://github.com/zephyrproject-rtos/zephyr/issues/52344) - Software-based Debounced GPIO
- [GitHub #52339](https://github.com/zephyrproject-rtos/zephyr/issues/52339) - usb: USB device re-enabling does not work on Nordic devices (regression)
- [GitHub #52327](https://github.com/zephyrproject-rtos/zephyr/issues/52327) - websocket: websocket\_recv\_msg breaks when there is no data after header
- [GitHub #52324](https://github.com/zephyrproject-rtos/zephyr/issues/52324) - Bluetooth Mesh example seems broken on v3.2.99 - worked ok with v3.1.99
- [GitHub #52317](https://github.com/zephyrproject-rtos/zephyr/issues/52317) - drivers: wifi: eswifi: Offload sockets accessing invalid net\_context, resulting in errors in FLASH\_SR and blocking flash use
- [GitHub #52309](https://github.com/zephyrproject-rtos/zephyr/issues/52309) - SAM0 flash driver with page emulated enabled will not write data at 0 block
- [GitHub #52308](https://github.com/zephyrproject-rtos/zephyr/issues/52308) - pip3 is unable to build wheel for cmsis-pack-manager as part of the requirements.txt on Fedora 37.
- [GitHub #52307](https://github.com/zephyrproject-rtos/zephyr/issues/52307) - Linker Error using CONSOLE\_GETCHAR and CONSOLE\_GETLINE
- [GitHub #52301](https://github.com/zephyrproject-rtos/zephyr/issues/52301) - Zephyr-Hello World is not working
- [GitHub #52298](https://github.com/zephyrproject-rtos/zephyr/issues/52298) - CI fail multiple times due to download package from [http://azure.archive.ubuntu.com/ubuntu](http://azure.archive.ubuntu.com/ubuntu) failed.
- [GitHub #52296](https://github.com/zephyrproject-rtos/zephyr/issues/52296) - Regulator shell does not build due to missing atoi define
- [GitHub #52291](https://github.com/zephyrproject-rtos/zephyr/issues/52291) - boards: thingy53: Enable USB-CDC by default
- [GitHub #52284](https://github.com/zephyrproject-rtos/zephyr/issues/52284) - unable to malloc during tests/lib/cmsis\_dsp/transform.cf64
- [GitHub #52280](https://github.com/zephyrproject-rtos/zephyr/issues/52280) - boards: thingy53 non-secure (thingy53\_nrf5340\_cpuapp\_ns) does not build
- [GitHub #52276](https://github.com/zephyrproject-rtos/zephyr/issues/52276) - stm32: ST Kit B-L4S5I-IOT01A Octospi flash support
- [GitHub #52267](https://github.com/zephyrproject-rtos/zephyr/issues/52267) - http client includes chunking data in response body when making a non-chunked request and server responds with chunked data
- [GitHub #52262](https://github.com/zephyrproject-rtos/zephyr/issues/52262) - west flash –file
- [GitHub #52242](https://github.com/zephyrproject-rtos/zephyr/issues/52242) - Fatal exception LoadProhibited from mcuboot when enabling newlib in wifi sample (esp32)
- [GitHub #52235](https://github.com/zephyrproject-rtos/zephyr/issues/52235) - counter\_basic\_api test fails to build on STM32 platforms
- [GitHub #52228](https://github.com/zephyrproject-rtos/zephyr/issues/52228) - Bluetooth: L2CAP: receive a K-frame with payload longer than MPS if Enhanced ATT enabled
- [GitHub #52219](https://github.com/zephyrproject-rtos/zephyr/issues/52219) - jlink runner doesn’t flash bin file if a hex file is present
- [GitHub #52218](https://github.com/zephyrproject-rtos/zephyr/issues/52218) - ADC read locked forever with CONFIG\_DEBUG\_OPTIMISATION=y on STM32U5
- [GitHub #52216](https://github.com/zephyrproject-rtos/zephyr/issues/52216) - spi\_transceive with DMA on a STM32 slave returns value incorrect
- [GitHub #52211](https://github.com/zephyrproject-rtos/zephyr/issues/52211) - MCUX based QDEC driver
- [GitHub #52196](https://github.com/zephyrproject-rtos/zephyr/issues/52196) - Calling `bt_le_ext_adv_stop()` can causes failures in connections when support for multiple connections are enabled
- [GitHub #52195](https://github.com/zephyrproject-rtos/zephyr/issues/52195) - Bluetooth: GATT: add\_subscriptions not respecting encryption
- [GitHub #52190](https://github.com/zephyrproject-rtos/zephyr/issues/52190) - [lpcxpresso55s28] flash range starts from Secure address which is not compatible with latest Jlink(v7.82a)
- [GitHub #52189](https://github.com/zephyrproject-rtos/zephyr/issues/52189) - Flash file system not working on stm32h735g\_disco
- [GitHub #52181](https://github.com/zephyrproject-rtos/zephyr/issues/52181) - ADC Channel SCAN mode for STM32U5
- [GitHub #52171](https://github.com/zephyrproject-rtos/zephyr/issues/52171) - Bluetooth: BR/EDR: Inappropriate l2cap channel state set/get
- [GitHub #52169](https://github.com/zephyrproject-rtos/zephyr/issues/52169) - Mesh provisioning static OOB incorrect zero padding
- [GitHub #52167](https://github.com/zephyrproject-rtos/zephyr/issues/52167) - twister: Mechanism to pass CLI args through to ztest executable
- [GitHub #52154](https://github.com/zephyrproject-rtos/zephyr/issues/52154) - mgmt: mcumgr: Add Kconfig to automatically register handlers and mcumgr functionality
- [GitHub #52139](https://github.com/zephyrproject-rtos/zephyr/issues/52139) - ppp modem doesn’t send NET\_EVENT\_L4\_CONNECTED event
- [GitHub #52131](https://github.com/zephyrproject-rtos/zephyr/issues/52131) - tests-ci : kernel: timer: starve test No Console Output(Timeout)
- [GitHub #52125](https://github.com/zephyrproject-rtos/zephyr/issues/52125) - Timer accuracy issue with STM32U5 board
- [GitHub #52114](https://github.com/zephyrproject-rtos/zephyr/issues/52114) - Can’t make JerryScript Work with Zephyr
- [GitHub #52113](https://github.com/zephyrproject-rtos/zephyr/issues/52113) - Binary blobs in `hal_telink` submodules
- [GitHub #52111](https://github.com/zephyrproject-rtos/zephyr/issues/52111) - Incompatible LTO version of liblt\_9518\_zephyr.a
- [GitHub #52103](https://github.com/zephyrproject-rtos/zephyr/issues/52103) - STM32u5 dual bank flash issue
- [GitHub #52101](https://github.com/zephyrproject-rtos/zephyr/issues/52101) - `bt_gatt_notify` function does not notify data larger than 20 bytes
- [GitHub #52099](https://github.com/zephyrproject-rtos/zephyr/issues/52099) - mgmt: mcumgr: Rename fs\_mgmt hash/checksum functions
- [GitHub #52095](https://github.com/zephyrproject-rtos/zephyr/issues/52095) - dfu/mcuboot: dfu/mcuboot.h used BOOT\_MAX\_ALIGN and BOOT\_MAGIC\_SZ but does not include `bootutil/bootutil_public.h`
- [GitHub #52094](https://github.com/zephyrproject-rtos/zephyr/issues/52094) - STM32MP157 Debugging method use wrong GDB port when execute command `west debug`
- [GitHub #52085](https://github.com/zephyrproject-rtos/zephyr/issues/52085) - can: SAM M\_CAN regression
- [GitHub #52079](https://github.com/zephyrproject-rtos/zephyr/issues/52079) - TLS handshake failure (after client-hello) with big\_http\_download sample
- [GitHub #52073](https://github.com/zephyrproject-rtos/zephyr/issues/52073) - ESP32-C3 UART1 not available after zephyr update to v3.2.99
- [GitHub #52065](https://github.com/zephyrproject-rtos/zephyr/issues/52065) - west: debugserver command does not work
- [GitHub #52059](https://github.com/zephyrproject-rtos/zephyr/issues/52059) - Bluetooth: conn: in multi role configuration incorrect address is set after advertising resume
- [GitHub #52057](https://github.com/zephyrproject-rtos/zephyr/issues/52057) - tests: kernel: timer: starve: kernel.timer.starve hangs
- [GitHub #52056](https://github.com/zephyrproject-rtos/zephyr/issues/52056) - Bluetooth: Missing LL data length update callback on Central and Peripheral sides
- [GitHub #52055](https://github.com/zephyrproject-rtos/zephyr/issues/52055) - Bluetooth: Controller: Broadcast scheduling issues
- [GitHub #52049](https://github.com/zephyrproject-rtos/zephyr/issues/52049) - Update mps2\_an521\_remote for compatibility with mps2\_an521\_ns
- [GitHub #52022](https://github.com/zephyrproject-rtos/zephyr/issues/52022) - RFC: API Change: mgmt: mcumgr: transport: Add query valid check function
- [GitHub #52021](https://github.com/zephyrproject-rtos/zephyr/issues/52021) - RFC: API Change: mgmt: mcumgr: Replace mgmt\_ctxt struct with smp\_streamer
- [GitHub #52009](https://github.com/zephyrproject-rtos/zephyr/issues/52009) - tests: kernel: fifo: fifo\_timeout: kernel.fifo.timeout fails on nrf5340dk\_nrf5340\_cpuapp
- [GitHub #51998](https://github.com/zephyrproject-rtos/zephyr/issues/51998) - Nominate Attie Grande as zephyr Collaborator
- [GitHub #51997](https://github.com/zephyrproject-rtos/zephyr/issues/51997) - microTVM or zephyr bugs, No SOURCES given to Zephyr library
- [GitHub #51989](https://github.com/zephyrproject-rtos/zephyr/issues/51989) - stm32f303v(b-c)tx-pinctrl.dtsi, No such file or directory
- [GitHub #51984](https://github.com/zephyrproject-rtos/zephyr/issues/51984) - Bluetooth: Central rejects connection parameters update request from a connected peripheral
- [GitHub #51973](https://github.com/zephyrproject-rtos/zephyr/issues/51973) - Coding style problem, clang-format formatted code cannot pass CI.
- [GitHub #51951](https://github.com/zephyrproject-rtos/zephyr/issues/51951) - Zephyr Getting Started steps fail with Python v3.11
- [GitHub #51944](https://github.com/zephyrproject-rtos/zephyr/issues/51944) - lsm6dso sensnsor driver: to enable drdy in pulsed mode call `lsm6dso_data_ready_mode_set()`
- [GitHub #51939](https://github.com/zephyrproject-rtos/zephyr/issues/51939) - mgmt: mcumgr: SMP is broken
- [GitHub #51931](https://github.com/zephyrproject-rtos/zephyr/issues/51931) - Failing unit test re. missing PERIPHERAL\_ISO\_SUPPORT KConfig selection
- [GitHub #51893](https://github.com/zephyrproject-rtos/zephyr/issues/51893) - LSM303dlhc sensor example not compiling for nRF52840
- [GitHub #51874](https://github.com/zephyrproject-rtos/zephyr/issues/51874) - Zephyr 3.1 bosch,bme280 device is in the final DTS and accessible, but DT\_HAS\_BOSCH\_BME280\_ENABLED=n
- [GitHub #51873](https://github.com/zephyrproject-rtos/zephyr/issues/51873) - sensor: bmp388: missing if check around i2c device ready function
- [GitHub #51872](https://github.com/zephyrproject-rtos/zephyr/issues/51872) - Race condition in workqueue can lead to work items being lost
- [GitHub #51870](https://github.com/zephyrproject-rtos/zephyr/issues/51870) - Nucleo\_h743zi fails to format storage flash partition
- [GitHub #51855](https://github.com/zephyrproject-rtos/zephyr/issues/51855) - openocd: targeting wrong serial port / device
- [GitHub #51829](https://github.com/zephyrproject-rtos/zephyr/issues/51829) - qemu\_x86: upgrading to q35 breaks networking samples.
- [GitHub #51827](https://github.com/zephyrproject-rtos/zephyr/issues/51827) - picolibc heap lock recursion mismatch
- [GitHub #51821](https://github.com/zephyrproject-rtos/zephyr/issues/51821) - native\_posix: Cmake must be run at least twice to find ${CMAKE\_STRIP}
- [GitHub #51815](https://github.com/zephyrproject-rtos/zephyr/issues/51815) - Bluetooth: bt\_disable in loop with babblesim gatt test causes Zephyr link layer assert
- [GitHub #51798](https://github.com/zephyrproject-rtos/zephyr/issues/51798) - mgmt: mcumgr: image upload, then image erase, then image upload does not restart upload from start
- [GitHub #51797](https://github.com/zephyrproject-rtos/zephyr/issues/51797) - West espressif install not working
- [GitHub #51796](https://github.com/zephyrproject-rtos/zephyr/issues/51796) - LE Audio: Improve stream coupling for CIS as the unicast client
- [GitHub #51788](https://github.com/zephyrproject-rtos/zephyr/issues/51788) - Questionable test code in ipv6\_fragment test
- [GitHub #51785](https://github.com/zephyrproject-rtos/zephyr/issues/51785) - drivers/clock\_control: stm32: Can support configure stm32\_h7 PLL2 ?
- [GitHub #51780](https://github.com/zephyrproject-rtos/zephyr/issues/51780) - windows-curses Python package in requirements.txt can’t install if using Python 3.11
- [GitHub #51778](https://github.com/zephyrproject-rtos/zephyr/issues/51778) - stm32l562e-dk: Broken TF-M psa-crypto sample
- [GitHub #51776](https://github.com/zephyrproject-rtos/zephyr/issues/51776) - POSIX API is not portable across arches
- [GitHub #51761](https://github.com/zephyrproject-rtos/zephyr/issues/51761) - Bluetooth : HardFault in hci\_driver on sample/bluetooth/periodic\_sync using nRF52833DK
- [GitHub #51752](https://github.com/zephyrproject-rtos/zephyr/issues/51752) - CAN documentation points to old sample locations
- [GitHub #51731](https://github.com/zephyrproject-rtos/zephyr/issues/51731) - Twister has a hard dependency on `west.log`
- [GitHub #51728](https://github.com/zephyrproject-rtos/zephyr/issues/51728) - soc: xtensa: esp32\_net: Remove binary blobs from source tree
- [GitHub #51720](https://github.com/zephyrproject-rtos/zephyr/issues/51720) - USB mass sample not working for FAT FS
- [GitHub #51714](https://github.com/zephyrproject-rtos/zephyr/issues/51714) - Bluetooth: Application with buffer that cannot unref it in disconnect handler leads to advertising issues
- [GitHub #51713](https://github.com/zephyrproject-rtos/zephyr/issues/51713) - drivers: flash: spi\_nor: init fails when flash is busy
- [GitHub #51711](https://github.com/zephyrproject-rtos/zephyr/issues/51711) - Esp32-WROVER Unable to include the header file `esp32-pinctrl.h`
- [GitHub #51693](https://github.com/zephyrproject-rtos/zephyr/issues/51693) - Bluetooth: Controller: Transmits packets longer than configured max len
- [GitHub #51687](https://github.com/zephyrproject-rtos/zephyr/issues/51687) - tests-ci : net: socket: tcp.preempt test Failed
- [GitHub #51688](https://github.com/zephyrproject-rtos/zephyr/issues/51688) - tests-ci : net: socket: tcp test Failed
- [GitHub #51689](https://github.com/zephyrproject-rtos/zephyr/issues/51689) - tests-ci : net: socket: poll test Failed
- [GitHub #51690](https://github.com/zephyrproject-rtos/zephyr/issues/51690) - tests-ci : net: socket: select test Failed
- [GitHub #51691](https://github.com/zephyrproject-rtos/zephyr/issues/51691) - tests-ci : net: socket: tls.preempt test Failed
- [GitHub #51692](https://github.com/zephyrproject-rtos/zephyr/issues/51692) - tests-ci : net: socket: tls test Failed
- [GitHub #51676](https://github.com/zephyrproject-rtos/zephyr/issues/51676) - stm32\_hal – undefined reference to “SystemCoreClock”
- [GitHub #51653](https://github.com/zephyrproject-rtos/zephyr/issues/51653) - mgmt: mcumgr: bt: issue with queued packets when device is busy
- [GitHub #51650](https://github.com/zephyrproject-rtos/zephyr/issues/51650) - Bluetooth: Extended adv reports with legacy data should also be discardable
- [GitHub #51631](https://github.com/zephyrproject-rtos/zephyr/issues/51631) - bluetooth: shell: linker error
- [GitHub #51629](https://github.com/zephyrproject-rtos/zephyr/issues/51629) - BLE stack execution fails with CONFIG\_NO\_OPTIMIZATIONS=y
- [GitHub #51622](https://github.com/zephyrproject-rtos/zephyr/issues/51622) - ESP32 mcuboot not support chip revision 1
- [GitHub #51621](https://github.com/zephyrproject-rtos/zephyr/issues/51621) - APPLICATION\_CONFIG\_DIR, CONF\_FILE do not always pick up local `boards/*.conf`
- [GitHub #51620](https://github.com/zephyrproject-rtos/zephyr/issues/51620) - Add Apache Thrift Module (from GSoC 2022 Project)
- [GitHub #51617](https://github.com/zephyrproject-rtos/zephyr/issues/51617) - RFC: Add Apache Thrift Upstream Module (from GSoC 2022 Project)
- [GitHub #51611](https://github.com/zephyrproject-rtos/zephyr/issues/51611) - check\_compliance.py generates file checkpath.txt which isn’t in .gitingore
- [GitHub #51607](https://github.com/zephyrproject-rtos/zephyr/issues/51607) - DT\_NODE\_HAS\_COMPAT does not consider parents/path
- [GitHub #51604](https://github.com/zephyrproject-rtos/zephyr/issues/51604) - doc: is the documentation GDPR compliant since it uses Google Analytics without prompting the user about tracking?
- [GitHub #51602](https://github.com/zephyrproject-rtos/zephyr/issues/51602) - Stack overflow when using mcumgr fs\_mgmt
- [GitHub #51600](https://github.com/zephyrproject-rtos/zephyr/issues/51600) - Bluetooth assert on flash erase using mcumgr
- [GitHub #51594](https://github.com/zephyrproject-rtos/zephyr/issues/51594) - mgmt: mcumgr: bt: thread freezes if device disconnects
- [GitHub #51588](https://github.com/zephyrproject-rtos/zephyr/issues/51588) - Doc: Broken link in the “Electronut Labs Papyr” documentation page
- [GitHub #51566](https://github.com/zephyrproject-rtos/zephyr/issues/51566) - broken network once lwM2M is resumed after pause
- [GitHub #51559](https://github.com/zephyrproject-rtos/zephyr/issues/51559) - lwm2m tests are failing
- [GitHub #51549](https://github.com/zephyrproject-rtos/zephyr/issues/51549) - Memory report generation breaks if app and Zephyr is located on different Windows drives
- [GitHub #51546](https://github.com/zephyrproject-rtos/zephyr/issues/51546) - The blinky\_pwm sample does not work on raspberry pi pico
- [GitHub #51544](https://github.com/zephyrproject-rtos/zephyr/issues/51544) - drivers/pwm/pwm\_sam.c - update period and duty cycle issue (workaround + suggestions for fix)
- [GitHub #51529](https://github.com/zephyrproject-rtos/zephyr/issues/51529) - frdm\_k64f: tests/net/socket/tls run failed on frdm\_k64f
- [GitHub #51528](https://github.com/zephyrproject-rtos/zephyr/issues/51528) - spurious warnings when EXTRA\_CFLAGS=-save-temps=obj is passed
- [GitHub #51521](https://github.com/zephyrproject-rtos/zephyr/issues/51521) - subsys: bluetooth: shell: gatt.c build fails with CONFIG\_DEBUG\_OPTIMIZATIONS and CONFIG\_BT\_SHELL=y
- [GitHub #51520](https://github.com/zephyrproject-rtos/zephyr/issues/51520) - samples: compression lz4 fails on small-ram stm32 platforms
- [GitHub #51508](https://github.com/zephyrproject-rtos/zephyr/issues/51508) - openocd: can’t flash STM32H7 board using STLink V3
- [GitHub #51506](https://github.com/zephyrproject-rtos/zephyr/issues/51506) - it8xxx2\_evb: Test suite after watchdog test will display fail in the daily test
- [GitHub #51505](https://github.com/zephyrproject-rtos/zephyr/issues/51505) - drivers: modem: gsm: gsm\_ppp\_stop() does not change gsm->state
- [GitHub #51488](https://github.com/zephyrproject-rtos/zephyr/issues/51488) - lis2dw12 function latch is misunderstood with drdy latch
- [GitHub #51480](https://github.com/zephyrproject-rtos/zephyr/issues/51480) - tests-ci : drivers: watchdog test Build failure of mimxrt1064\_evk
- [GitHub #51476](https://github.com/zephyrproject-rtos/zephyr/issues/51476) - Please add documentation or sample how to use TLS\_SESSION\_CACHE socket option
- [GitHub #51475](https://github.com/zephyrproject-rtos/zephyr/issues/51475) - Twister: Mistake timeout as skipped
- [GitHub #51474](https://github.com/zephyrproject-rtos/zephyr/issues/51474) - driver: stm32: usb: add detach function support
- [GitHub #51471](https://github.com/zephyrproject-rtos/zephyr/issues/51471) - Network protocol MQTT: When qos=1, there is a bug in the subscription and publication
- [GitHub #51470](https://github.com/zephyrproject-rtos/zephyr/issues/51470) - tests-ci : drivers: mipi\_dsi: api test Build failure
- [GitHub #51469](https://github.com/zephyrproject-rtos/zephyr/issues/51469) - Intel CAVS: Failed in tests/kernel/spinlock
- [GitHub #51468](https://github.com/zephyrproject-rtos/zephyr/issues/51468) - mps3\_an547:tests/lib/cmsis\_dsp/filtering bus fault
- [GitHub #51464](https://github.com/zephyrproject-rtos/zephyr/issues/51464) - samples: drivers: peci: Code doesn’t build for npcx7m6fb\_evb board
- [GitHub #51458](https://github.com/zephyrproject-rtos/zephyr/issues/51458) - Only one instance of mcp2515
- [GitHub #51454](https://github.com/zephyrproject-rtos/zephyr/issues/51454) - Cmake error for Zephyr Sample Code in Visual Studio
- [GitHub #51446](https://github.com/zephyrproject-rtos/zephyr/issues/51446) - The PR #50334 breaks twister execution on various HW boards
- [GitHub #51437](https://github.com/zephyrproject-rtos/zephyr/issues/51437) - LoRaWan problem with uplink messages sent as a response to class C downlink
- [GitHub #51438](https://github.com/zephyrproject-rtos/zephyr/issues/51438) - tests-ci : net: http: test Build failure
- [GitHub #51436](https://github.com/zephyrproject-rtos/zephyr/issues/51436) - tests-ci : drivers: drivers.watchdog: nxp-imxrt11xx series : watchdog build failure
- [GitHub #51435](https://github.com/zephyrproject-rtos/zephyr/issues/51435) - tests-ci : drivers: hwinfo: api test Failed
- [GitHub #51432](https://github.com/zephyrproject-rtos/zephyr/issues/51432) - Bluetooth: ISO: Remove checks for and change seq\_num to uint16\_t
- [GitHub #51424](https://github.com/zephyrproject-rtos/zephyr/issues/51424) - tests: net: socket: tls: v4 dtls sendmsg test is testing v6
- [GitHub #51421](https://github.com/zephyrproject-rtos/zephyr/issues/51421) - tests: net: socket: tls: net.socket.tls region `FLASH` overflowed
- [GitHub #51418](https://github.com/zephyrproject-rtos/zephyr/issues/51418) - Intel CAVS: Assertion failed in tests/subsys/logging/log\_links
- [GitHub #51406](https://github.com/zephyrproject-rtos/zephyr/issues/51406) - Blinky not executing on Windows
- [GitHub #51376](https://github.com/zephyrproject-rtos/zephyr/issues/51376) - Silabs WFX200 Binary Blob
- [GitHub #51375](https://github.com/zephyrproject-rtos/zephyr/issues/51375) - tests/lib/devicetree/devices/libraries.devicetree.devices: build failure (bl5340\_dvk\_cpuapp)
- [GitHub #51371](https://github.com/zephyrproject-rtos/zephyr/issues/51371) - hal: nxp: ARRAY\_SIZE collision
- [GitHub #51370](https://github.com/zephyrproject-rtos/zephyr/issues/51370) - Driver error precision LPS22HH
- [GitHub #51368](https://github.com/zephyrproject-rtos/zephyr/issues/51368) - tests: tests/subsys/cpp/cxx/cpp.main.picolibc: build failure
- [GitHub #51364](https://github.com/zephyrproject-rtos/zephyr/issues/51364) - ESP32 WIFI: when allocating system\_heap to PSRAM(extern ram), wifi station can’t connet to ap(indicate that ap not found)
- [GitHub #51360](https://github.com/zephyrproject-rtos/zephyr/issues/51360) - I2C master read failure when 10-bit addressing is used with i2c\_ll\_stm32\_v1
- [GitHub #51351](https://github.com/zephyrproject-rtos/zephyr/issues/51351) - I2C: ESP32 driver does not support longer clock stretching
- [GitHub #51349](https://github.com/zephyrproject-rtos/zephyr/issues/51349) - Turn power domains on/off directly
- [GitHub #51343](https://github.com/zephyrproject-rtos/zephyr/issues/51343) - qemu\_x86\_tiny doesn’t place libc-hooks data in z\_libc\_partition
- [GitHub #51331](https://github.com/zephyrproject-rtos/zephyr/issues/51331) - lvgl: LV\_FONT\_CUSTOM\_DECLARE does not work as string
- [GitHub #51323](https://github.com/zephyrproject-rtos/zephyr/issues/51323) - kernel: tests: Evaluate “platform\_allow” usage in kernel tests.
- [GitHub #51322](https://github.com/zephyrproject-rtos/zephyr/issues/51322) - tests: kernel: timer: timer\_behavior: kernel.timer.timer fails
- [GitHub #51318](https://github.com/zephyrproject-rtos/zephyr/issues/51318) - x86\_64: Thread Local Storage pointer not setup before first thread started
- [GitHub #51301](https://github.com/zephyrproject-rtos/zephyr/issues/51301) - CI: mps3\_an547: test failures
- [GitHub #51297](https://github.com/zephyrproject-rtos/zephyr/issues/51297) - Bluetooth: Implement H8 function from cryptographic toolbox
- [GitHub #51294](https://github.com/zephyrproject-rtos/zephyr/issues/51294) - ztest: Broken tests in main branch due to API-breaking change `ZTEST_FAIL_ON_ASSUME`
- [GitHub #51290](https://github.com/zephyrproject-rtos/zephyr/issues/51290) - samples: application\_development: external\_lib: does not work on windows
- [GitHub #51276](https://github.com/zephyrproject-rtos/zephyr/issues/51276) - CAN driver for ESP32 (TWAI) does not enable the transceiver
- [GitHub #51265](https://github.com/zephyrproject-rtos/zephyr/issues/51265) - net: ip: cloning of net\_pkt produces dangling ll address pointers and may flip overwrite flag
- [GitHub #51264](https://github.com/zephyrproject-rtos/zephyr/issues/51264) - drivers: ieee802154: nrf: wrapped pkt attribute access
- [GitHub #51263](https://github.com/zephyrproject-rtos/zephyr/issues/51263) - drivers: ieee802154: IEEE 802.15.4 L2 does not announce (but uses) promisc mode
- [GitHub #51261](https://github.com/zephyrproject-rtos/zephyr/issues/51261) - drivers: ieee802154: Drivers allocate RX packets from the TX pool
- [GitHub #51247](https://github.com/zephyrproject-rtos/zephyr/issues/51247) - Bluetooth: RPA expired callback inconsistently called
- [GitHub #51235](https://github.com/zephyrproject-rtos/zephyr/issues/51235) - nominate me as zephyr contributor
- [GitHub #51234](https://github.com/zephyrproject-rtos/zephyr/issues/51234) - it8xxx2\_evb: The testcase tests/kernel/sleep/failed to run.
- [GitHub #51233](https://github.com/zephyrproject-rtos/zephyr/issues/51233) - up\_squared: samples/boards/up\_squared/gpio\_counter run failed
- [GitHub #51228](https://github.com/zephyrproject-rtos/zephyr/issues/51228) - Bluetooth: Privacy in scan roles not updating RPA on timeout
- [GitHub #51223](https://github.com/zephyrproject-rtos/zephyr/issues/51223) - Problem when using fatfs example in a out\_of\_tree\_driver with the file ff.h
- [GitHub #51214](https://github.com/zephyrproject-rtos/zephyr/issues/51214) - enc28j60 appears to be unable to correctly determine network state
- [GitHub #51208](https://github.com/zephyrproject-rtos/zephyr/issues/51208) - Bluetooth: Host: `bt_le_oob_get_local` gives incorrect address
- [GitHub #51202](https://github.com/zephyrproject-rtos/zephyr/issues/51202) - twister: Integration errors not reported nor counted in the console output but present in the reports.
- [GitHub #51194](https://github.com/zephyrproject-rtos/zephyr/issues/51194) - samples/subsys/lorawan building failed
- [GitHub #51185](https://github.com/zephyrproject-rtos/zephyr/issues/51185) - tests/drivers/counter/counter\_basic\_api fails to build on mimxrt685\_evk\_cm33
- [GitHub #51177](https://github.com/zephyrproject-rtos/zephyr/issues/51177) - Change SPI configuration (bitrate) with MCUXpresso SPI driver fails
- [GitHub #51174](https://github.com/zephyrproject-rtos/zephyr/issues/51174) - Bluetooth: l2cap needs check rx.mps when le\_recv
- [GitHub #51168](https://github.com/zephyrproject-rtos/zephyr/issues/51168) - ITERABLE\_SECTION\_ROM stores data in RAM instead of ROM
- [GitHub #51165](https://github.com/zephyrproject-rtos/zephyr/issues/51165) - tools/fiptool/fiptool: Permission denied
- [GitHub #51156](https://github.com/zephyrproject-rtos/zephyr/issues/51156) - esp32 wifi: how to use ap mode and ap+station mode?
- [GitHub #51153](https://github.com/zephyrproject-rtos/zephyr/issues/51153) - modem: ppp: extract access technology when MODEM\_CELL\_INFO is enabled
- [GitHub #51149](https://github.com/zephyrproject-rtos/zephyr/issues/51149) - Esp32 wifi compilation error
- [GitHub #51146](https://github.com/zephyrproject-rtos/zephyr/issues/51146) - Running test: drivers: disk: disk\_access with RAM disk fails
- [GitHub #51144](https://github.com/zephyrproject-rtos/zephyr/issues/51144) - PR #51017 Broke GPIO builds for LPC11u6x platforms
- [GitHub #51142](https://github.com/zephyrproject-rtos/zephyr/issues/51142) - TestPlan generation not picking up tests missing `test_` prefix
- [GitHub #51138](https://github.com/zephyrproject-rtos/zephyr/issues/51138) - Testing tests/lib/cmsis\_dsp/ fails on some stm32 boards
- [GitHub #51126](https://github.com/zephyrproject-rtos/zephyr/issues/51126) - Bluetooh: host: df: wrong size of a HCI command for connectionless CTE enable in AoD mode
- [GitHub #51117](https://github.com/zephyrproject-rtos/zephyr/issues/51117) - tests: kernel: workq: work: kernel.work.api fails test\_1cpu\_drain\_wait
- [GitHub #51108](https://github.com/zephyrproject-rtos/zephyr/issues/51108) - Ethernet: Error frames are displayed when DHCP is suspended for a long time: <inf> net\_dhcpv4: Received: 192.168.1.119
- [GitHub #51107](https://github.com/zephyrproject-rtos/zephyr/issues/51107) - Ethernet: Error frames are often displayed: <err> eth\_mcux: ENET\_GetRxFrameSize return: 4001
- [GitHub #51105](https://github.com/zephyrproject-rtos/zephyr/issues/51105) - esp32 wifi: http transmit rate is too slow
- [GitHub #51102](https://github.com/zephyrproject-rtos/zephyr/issues/51102) - issue installing zepyhr when i am using west cmd
- [GitHub #51076](https://github.com/zephyrproject-rtos/zephyr/issues/51076) - ADC channels 8-12 not working on LPC55s6X
- [GitHub #51074](https://github.com/zephyrproject-rtos/zephyr/issues/51074) - logging: syst: sample failure
- [GitHub #51070](https://github.com/zephyrproject-rtos/zephyr/issues/51070) - ModuleNotFoundError: No module named ‘elftools’
- [GitHub #51068](https://github.com/zephyrproject-rtos/zephyr/issues/51068) - ModuleNotFoundError: No module named ‘elftools’
- [GitHub #51065](https://github.com/zephyrproject-rtos/zephyr/issues/51065) - building tests/subsys/jwt failed on disco\_l475\_iot1 with twister
- [GitHub #51062](https://github.com/zephyrproject-rtos/zephyr/issues/51062) - lora\_recv\_async receives empty buffer after multiple receptions on sx12xx
- [GitHub #51060](https://github.com/zephyrproject-rtos/zephyr/issues/51060) - 10-bit addressing not supported by I2C slave driver for STM32 target
- [GitHub #51057](https://github.com/zephyrproject-rtos/zephyr/issues/51057) - Retrieve gpios used by a device (pinctrl)
- [GitHub #51048](https://github.com/zephyrproject-rtos/zephyr/issues/51048) - Firmware Upgrade Issue with Mcumgr On STM32H743 controller
- [GitHub #51025](https://github.com/zephyrproject-rtos/zephyr/issues/51025) - mbedtls: build warnings
- [GitHub #51021](https://github.com/zephyrproject-rtos/zephyr/issues/51021) - openthread: build warnings
- [GitHub #51019](https://github.com/zephyrproject-rtos/zephyr/issues/51019) - NVS should allow overwriting existing index even if there’s no room to keep the old value
- [GitHub #51016](https://github.com/zephyrproject-rtos/zephyr/issues/51016) - mgmt: mcumgr: Add dummy shell buffer size Kconfig entry to shell mgmt
- [GitHub #51015](https://github.com/zephyrproject-rtos/zephyr/issues/51015) - Build Error for ST Nucleo F103RB
- [GitHub #51010](https://github.com/zephyrproject-rtos/zephyr/issues/51010) - Unable to communicate with LIS2DS12 on 52840DK or custom board
- [GitHub #51007](https://github.com/zephyrproject-rtos/zephyr/issues/51007) - Improve process around feature freeze exceptions
- [GitHub #51003](https://github.com/zephyrproject-rtos/zephyr/issues/51003) - Crash when using flexcomm5 as i2c on LPC5526
- [GitHub #50989](https://github.com/zephyrproject-rtos/zephyr/issues/50989) - Invalid ASE State Machine Transition
- [GitHub #50983](https://github.com/zephyrproject-rtos/zephyr/issues/50983) - RPI Pico usb hangs up in interrupt handler for composite devices
- [GitHub #50976](https://github.com/zephyrproject-rtos/zephyr/issues/50976) - JSON array encoding fails on array of objects
- [GitHub #50974](https://github.com/zephyrproject-rtos/zephyr/issues/50974) - DHCP (IPv4) NAK not respected when in renewing state
- [GitHub #50973](https://github.com/zephyrproject-rtos/zephyr/issues/50973) - DHCP (IPv4) seemingly dies by trying to assign an IP of 0.0.0.0
- [GitHub #50970](https://github.com/zephyrproject-rtos/zephyr/issues/50970) - SAME54\_xpro network driver not attached
- [GitHub #50953](https://github.com/zephyrproject-rtos/zephyr/issues/50953) - LE Audio: Add support for setting ISO data path for broadcast sink
- [GitHub #50948](https://github.com/zephyrproject-rtos/zephyr/issues/50948) - SSD1306+lvgl sample fails to display
- [GitHub #50947](https://github.com/zephyrproject-rtos/zephyr/issues/50947) - stm32 static IPv4 networking in smp\_svr sample application does not seem to work until a ping is received
- [GitHub #50940](https://github.com/zephyrproject-rtos/zephyr/issues/50940) - logging.log\_output\_ts64 fails on qemu\_arc\_hs5x
- [GitHub #50937](https://github.com/zephyrproject-rtos/zephyr/issues/50937) - Error when building for esp32c3\_devkitm
- [GitHub #50923](https://github.com/zephyrproject-rtos/zephyr/issues/50923) - RFC: Stable API change: Rework and improve mcumgr callback system
- [GitHub #50895](https://github.com/zephyrproject-rtos/zephyr/issues/50895) - ADC Voltage Reference issue with STM32U5 MCU
- [GitHub #50874](https://github.com/zephyrproject-rtos/zephyr/issues/50874) - Cant disable bluetooth for BLE peripheral after connection with Central
- [GitHub #50872](https://github.com/zephyrproject-rtos/zephyr/issues/50872) - Error while installing python dependecies
- [GitHub #50868](https://github.com/zephyrproject-rtos/zephyr/issues/50868) - DHCP never binds if a NAK is received during the requesting state
- [GitHub #50853](https://github.com/zephyrproject-rtos/zephyr/issues/50853) - STM32F7 series can’t run at frequencies higher than 180MHz
- [GitHub #50844](https://github.com/zephyrproject-rtos/zephyr/issues/50844) - zcbor module apis which are used for mcu boot functionality are not building in cpp file against v3.1.0
- [GitHub #50812](https://github.com/zephyrproject-rtos/zephyr/issues/50812) - MCUmgr udp sample fails with shell - BUS FAULT
- [GitHub #50801](https://github.com/zephyrproject-rtos/zephyr/issues/50801) - JSON parser fails on multidimensional arrays
- [GitHub #50789](https://github.com/zephyrproject-rtos/zephyr/issues/50789) - west: runners: blackmagicprobe: Doesn’t work on windows due to wrong path separator
- [GitHub #50786](https://github.com/zephyrproject-rtos/zephyr/issues/50786) - Bluetooth: Host: Extended advertising reports may block the host
- [GitHub #50784](https://github.com/zephyrproject-rtos/zephyr/issues/50784) - LE Audio: Missing Media Proxy checks for callbacks
- [GitHub #50783](https://github.com/zephyrproject-rtos/zephyr/issues/50783) - LE Audio: Reject ISO data if the stream is not in the streaming state
- [GitHub #50782](https://github.com/zephyrproject-rtos/zephyr/issues/50782) - LE Audio: The MPL shell module should not use opcodes
- [GitHub #50781](https://github.com/zephyrproject-rtos/zephyr/issues/50781) - LE Audio: `mpl init` causes warnings when adding objects
- [GitHub #50780](https://github.com/zephyrproject-rtos/zephyr/issues/50780) - LE Audio: Bidirectional handling of 2 audio streams as the unicast server when streams are configured separately not working as intended
- [GitHub #50778](https://github.com/zephyrproject-rtos/zephyr/issues/50778) - LE Audio: Audio shell: Unicast server cannot execute commands for the default\_stream
- [GitHub #50776](https://github.com/zephyrproject-rtos/zephyr/issues/50776) - CAN Drivers allow sending FD frames without device being set to FD mode
- [GitHub #50768](https://github.com/zephyrproject-rtos/zephyr/issues/50768) - storage: DT `fixed-partition` with `status = "okay"` requires flash driver
- [GitHub #50746](https://github.com/zephyrproject-rtos/zephyr/issues/50746) - Stale kernel memory pool API references
- [GitHub #50744](https://github.com/zephyrproject-rtos/zephyr/issues/50744) - net: ipv6: Allow on creating incomplete neighbor entries and routes in case of receiving Router Advertisement
- [GitHub #50735](https://github.com/zephyrproject-rtos/zephyr/issues/50735) - intel\_adsp\_cavs18: tests/boards/intel\_adsp/hda\_log/boards.intel\_adsp.hda\_log.printk failed
- [GitHub #50732](https://github.com/zephyrproject-rtos/zephyr/issues/50732) - net: tests/net/ieee802154/l2/net.ieee802154.l2 failed on reel\_board due to build failure
- [GitHub #50709](https://github.com/zephyrproject-rtos/zephyr/issues/50709) - tests: arch: arm: arm\_thread\_swap fails on stm32g0 or stm32l0
- [GitHub #50684](https://github.com/zephyrproject-rtos/zephyr/issues/50684) - After enabling CONFIG\_SPI\_STM32\_DMA in project config file for STM32MP157-dk2 Zephyr throwing error
- [GitHub #50665](https://github.com/zephyrproject-rtos/zephyr/issues/50665) - MEC15xx/MEC1501: UART and special purpose pins missing pinctrl configuration
- [GitHub #50658](https://github.com/zephyrproject-rtos/zephyr/issues/50658) - Bluetooth: BLE stack notifications blocks host side for too long (`drivers/bluetooth/hci/spi.c` and `hci_spi`)
- [GitHub #50656](https://github.com/zephyrproject-rtos/zephyr/issues/50656) - Wrong definition of bank size for intel memory management driver.
- [GitHub #50655](https://github.com/zephyrproject-rtos/zephyr/issues/50655) - STM32WB55 Bus Fault when connecting then disconnecting then connecting then disconnecting then connecting
- [GitHub #50620](https://github.com/zephyrproject-rtos/zephyr/issues/50620) - fifo test fails with CONFIG\_CMAKE\_LINKER\_GENERATOR enabled on qemu\_cortex\_a9
- [GitHub #50614](https://github.com/zephyrproject-rtos/zephyr/issues/50614) - Zephyr if got the ip is “10.xxx.xxx.xxx” when join in the switchboard, then the device may can not visit the outer net, also unable to Ping.
- [GitHub #50603](https://github.com/zephyrproject-rtos/zephyr/issues/50603) - Upgrade to loramac-node 4.7.0 when it is released to fix async LoRa reception on SX1276
- [GitHub #50596](https://github.com/zephyrproject-rtos/zephyr/issues/50596) - Documentation: Broken links in the previous release documentation
- [GitHub #50592](https://github.com/zephyrproject-rtos/zephyr/issues/50592) - mgmt: mcumgr: Remove code/functions deprecated in zephyr 3.1 release
- [GitHub #50590](https://github.com/zephyrproject-rtos/zephyr/issues/50590) - openocd: Can’t flash on various STM32 boards
- [GitHub #50587](https://github.com/zephyrproject-rtos/zephyr/issues/50587) - Regression in Link Layer Control Procedure (LLCP)
- [GitHub #50570](https://github.com/zephyrproject-rtos/zephyr/issues/50570) - samples/drivers/can/counter fails in twister for native\_posix
- [GitHub #50567](https://github.com/zephyrproject-rtos/zephyr/issues/50567) - Passed test cases are reported as “Skipped” because of incomplete test log
- [GitHub #50565](https://github.com/zephyrproject-rtos/zephyr/issues/50565) - Fatal error after `west flash` for nucleo\_l053r8
- [GitHub #50554](https://github.com/zephyrproject-rtos/zephyr/issues/50554) - Test uart async failed on Nucleo F429ZI
- [GitHub #50525](https://github.com/zephyrproject-rtos/zephyr/issues/50525) - Passed test cases reported as “Skipped” because test log lost
- [GitHub #50515](https://github.com/zephyrproject-rtos/zephyr/issues/50515) - Non-existing test cases reported as “Skipped” with reason “No results captured, testsuite misconfiguration?” in test report
- [GitHub #50461](https://github.com/zephyrproject-rtos/zephyr/issues/50461) - Bluetooth: controller: LLCP: use of legacy ctrl Tx buffers
- [GitHub #50452](https://github.com/zephyrproject-rtos/zephyr/issues/50452) - mec172xevb\_assy6906: The testcase tests/lib/cmsis\_dsp/matrix failed to run.
- [GitHub #50446](https://github.com/zephyrproject-rtos/zephyr/issues/50446) - MCUX CAAM is disabled temporarily
- [GitHub #50438](https://github.com/zephyrproject-rtos/zephyr/issues/50438) - Bluetooth: Conn: Bluetooth stack becomes unusable when communicating with both centrals and peripherals
- [GitHub #50427](https://github.com/zephyrproject-rtos/zephyr/issues/50427) - Bluetooth: host: central connection context leak
- [GitHub #50426](https://github.com/zephyrproject-rtos/zephyr/issues/50426) - STM32: using SPI after STOP2 sleep causes application to hang
- [GitHub #50404](https://github.com/zephyrproject-rtos/zephyr/issues/50404) - Intel CAVS: tests/subsys/logging/log\_immediate failed.
- [GitHub #50389](https://github.com/zephyrproject-rtos/zephyr/issues/50389) - Allow twister to be called directly from west
- [GitHub #50381](https://github.com/zephyrproject-rtos/zephyr/issues/50381) - BLE: Connection slows down massively when connecting to a second device
- [GitHub #50354](https://github.com/zephyrproject-rtos/zephyr/issues/50354) - ztest\_new: \_zassert\_base : return without post processing
- [GitHub #50345](https://github.com/zephyrproject-rtos/zephyr/issues/50345) - Network traffic occurs before Bluetooth NET L2 (IPSP) link setup complete
- [GitHub #50284](https://github.com/zephyrproject-rtos/zephyr/issues/50284) - Generated linker scripts break when ZEPHYR\_BASE and ZEPHYR\_MODULES share structure that contains symlinks
- [GitHub #50256](https://github.com/zephyrproject-rtos/zephyr/issues/50256) - I2C on SAMC21 sends out stop condition incorrectly
- [GitHub #50193](https://github.com/zephyrproject-rtos/zephyr/issues/50193) - Impossible to connect with a peripheral with BLE and zephyr 2.7.99, BT\_HCI\_ERR\_UNKNOWN\_CONN\_ID error
- [GitHub #50192](https://github.com/zephyrproject-rtos/zephyr/issues/50192) - nrf\_qspi\_nor driver might crash if power management is enabled
- [GitHub #50188](https://github.com/zephyrproject-rtos/zephyr/issues/50188) - Avoid using extra net buffer for L2 header
- [GitHub #50149](https://github.com/zephyrproject-rtos/zephyr/issues/50149) - tests: drivers: flash fails on nucleo\_l152re because of wrong erase flash size
- [GitHub #50139](https://github.com/zephyrproject-rtos/zephyr/issues/50139) - net: ipv4: Add DSCP/ToS based QoS support
- [GitHub #50070](https://github.com/zephyrproject-rtos/zephyr/issues/50070) - LoRa: Support on RFM95 LoRa module combined with a nRF52 board
- [GitHub #50040](https://github.com/zephyrproject-rtos/zephyr/issues/50040) - shields: Settle on nodelabels naming scheme
- [GitHub #50028](https://github.com/zephyrproject-rtos/zephyr/issues/50028) - flash\_stm32\_ospi Write enable failed when building with TF-M
- [GitHub #49996](https://github.com/zephyrproject-rtos/zephyr/issues/49996) - tests: drivers: clock\_control: nrf\_lf\_clock\_start and nrf\_onoff\_and\_bt fails
- [GitHub #49963](https://github.com/zephyrproject-rtos/zephyr/issues/49963) - Random crash on the L475 due to work->handler set to NULL
- [GitHub #49962](https://github.com/zephyrproject-rtos/zephyr/issues/49962) - RFC: Stable API Change: SMP (Simple Management Protocol) transport API within MCUMgr drops `zephyr_` prefix in functions and type definitions and drop zst parameter from zephyr\_smp\_transport\_out\_fn
- [GitHub #49917](https://github.com/zephyrproject-rtos/zephyr/issues/49917) - http\_client\_req() sometimes hangs when peer disconnects
- [GitHub #49871](https://github.com/zephyrproject-rtos/zephyr/issues/49871) - zperf: Add support to stop/start download
- [GitHub #49870](https://github.com/zephyrproject-rtos/zephyr/issues/49870) - stm32 enables HSI48 clock with device tree
- [GitHub #49844](https://github.com/zephyrproject-rtos/zephyr/issues/49844) - shell: Add abort support
- [GitHub #49843](https://github.com/zephyrproject-rtos/zephyr/issues/49843) - net: shell: Extend ping command
- [GitHub #49821](https://github.com/zephyrproject-rtos/zephyr/issues/49821) - USB DFU implementation does not work with WinUSB because of missing device reset API
- [GitHub #49811](https://github.com/zephyrproject-rtos/zephyr/issues/49811) - DHCP cannot obtain IP, when CONFIG\_NET\_VLAN is enabled
- [GitHub #49783](https://github.com/zephyrproject-rtos/zephyr/issues/49783) - net: ipv4: packet fragmentation support
- [GitHub #49746](https://github.com/zephyrproject-rtos/zephyr/issues/49746) - twister: extra test results
- [GitHub #49740](https://github.com/zephyrproject-rtos/zephyr/issues/49740) - LE Audio: Support for application-controlled advertisement for BAP broadcast source
- [GitHub #49711](https://github.com/zephyrproject-rtos/zephyr/issues/49711) - tests/arch/common/timing/arch.common.timing.smp fails for CAVS15, 18
- [GitHub #49648](https://github.com/zephyrproject-rtos/zephyr/issues/49648) - tests/subsys/logging/log\_switch\_format, log\_syst build failures on CAVS
- [GitHub #49624](https://github.com/zephyrproject-rtos/zephyr/issues/49624) - Bluetooth: Controller: Recent RAM usage increase for hci\_rpmsg build
- [GitHub #49621](https://github.com/zephyrproject-rtos/zephyr/issues/49621) - STM32WB55 BLE Extended Advertising support
- [GitHub #49620](https://github.com/zephyrproject-rtos/zephyr/issues/49620) - Add picolibc documentation
- [GitHub #49614](https://github.com/zephyrproject-rtos/zephyr/issues/49614) - acrn\_ehl\_crb: The testcase tests/kernel/sched/schedule\_api failed to run.
- [GitHub #49611](https://github.com/zephyrproject-rtos/zephyr/issues/49611) - ehl\_crb: Failed to run timer testcases
- [GitHub #49588](https://github.com/zephyrproject-rtos/zephyr/issues/49588) - Json parser is incorrect with undefined parameter
- [GitHub #49584](https://github.com/zephyrproject-rtos/zephyr/issues/49584) - STM32WB55 Failed read remote feature, remote version and LE set PHY
- [GitHub #49530](https://github.com/zephyrproject-rtos/zephyr/issues/49530) - Bluetooth: Audio: Invalid behavior testing
- [GitHub #49451](https://github.com/zephyrproject-rtos/zephyr/issues/49451) - Treat carrier UP/DOWN independently to interface UP/DOWN
- [GitHub #49413](https://github.com/zephyrproject-rtos/zephyr/issues/49413) - TI-AM62x: Add Zephyr Support for M4 and R5 cores
- [GitHub #49373](https://github.com/zephyrproject-rtos/zephyr/issues/49373) - BLE scanning - BT RX thread hangs on.
- [GitHub #49338](https://github.com/zephyrproject-rtos/zephyr/issues/49338) - Antenna switching for Bluetooth direction finding with the nRF5340
- [GitHub #49313](https://github.com/zephyrproject-rtos/zephyr/issues/49313) - nRF51822 sometimes hard fault on connect
- [GitHub #49298](https://github.com/zephyrproject-rtos/zephyr/issues/49298) - cc3220sf: add a launchpad\_connector.dtsi
- [GitHub #49266](https://github.com/zephyrproject-rtos/zephyr/issues/49266) - Bluetooth: Host doesn’t seem to handle INCOMPLETE per adv reports
- [GitHub #49234](https://github.com/zephyrproject-rtos/zephyr/issues/49234) - option to configure coverage data heap size
- [GitHub #49228](https://github.com/zephyrproject-rtos/zephyr/issues/49228) - ti: cc13xx\_cc26xx: ADC support
- [GitHub #49210](https://github.com/zephyrproject-rtos/zephyr/issues/49210) - BL5340 board cannot build bluetooth applications
- [GitHub #49208](https://github.com/zephyrproject-rtos/zephyr/issues/49208) - drivers: modem: bg9x: not supporting UDP
- [GitHub #49148](https://github.com/zephyrproject-rtos/zephyr/issues/49148) - Asynchronous UART API triggers Zephyr assertion on STM32WB55
- [GitHub #49112](https://github.com/zephyrproject-rtos/zephyr/issues/49112) - lack of support for lpsram cache
- [GitHub #49069](https://github.com/zephyrproject-rtos/zephyr/issues/49069) - log: cdc\_acm: hard fault message does not output
- [GitHub #49066](https://github.com/zephyrproject-rtos/zephyr/issues/49066) - Mcumgr img\_mgmt\_impl\_upload\_inspect() can cause unaligned memory access hard fault.
- [GitHub #49054](https://github.com/zephyrproject-rtos/zephyr/issues/49054) - STM32H7 apps are broken in C++ mode due to HAL include craziness
- [GitHub #49032](https://github.com/zephyrproject-rtos/zephyr/issues/49032) - espi saf testing disabled
- [GitHub #49026](https://github.com/zephyrproject-rtos/zephyr/issues/49026) - Add a CI check on image file sizes (specifically around boards)
- [GitHub #49021](https://github.com/zephyrproject-rtos/zephyr/issues/49021) - uart async api does not provide all received data
- [GitHub #48954](https://github.com/zephyrproject-rtos/zephyr/issues/48954) - several NXP devicetree bindings are missing
- [GitHub #48953](https://github.com/zephyrproject-rtos/zephyr/issues/48953) - ‘intel,sha’ is missing binding and usage
- [GitHub #48886](https://github.com/zephyrproject-rtos/zephyr/issues/48886) - Documenting the process for treewide changes
- [GitHub #48857](https://github.com/zephyrproject-rtos/zephyr/issues/48857) - samples: Bluetooth: Buffer size mismatch in samples/bluetooth/hci\_usb for nRF5340
- [GitHub #48850](https://github.com/zephyrproject-rtos/zephyr/issues/48850) - Bluetooth: LLCP: possible access to released control procedure context
- [GitHub #48726](https://github.com/zephyrproject-rtos/zephyr/issues/48726) - net: tests/net/ieee802154/l2/net.ieee802154.l2 failed on reel board
- [GitHub #48625](https://github.com/zephyrproject-rtos/zephyr/issues/48625) - GSM\_PPP api keeps sending commands to muxed AT channel
- [GitHub #48616](https://github.com/zephyrproject-rtos/zephyr/issues/48616) - RFC: Change to clang-format coding style rules re binary operators
- [GitHub #48609](https://github.com/zephyrproject-rtos/zephyr/issues/48609) - drivers: gpio: expose gpio\_utils.h to external GPIO drivers
- [GitHub #48603](https://github.com/zephyrproject-rtos/zephyr/issues/48603) - LoRa driver asynchronous receive callback clears data before the callback.
- [GitHub #48520](https://github.com/zephyrproject-rtos/zephyr/issues/48520) - clang-format: #include reorder due to default: SortIncludesOptions != SI\_Never
- [GitHub #48505](https://github.com/zephyrproject-rtos/zephyr/issues/48505) - BLE stack can get stuck in connected state despite connection failure
- [GitHub #48473](https://github.com/zephyrproject-rtos/zephyr/issues/48473) - Setting CONFIG\_GSM\_MUX\_INITIATOR=n results in a compile error
- [GitHub #48468](https://github.com/zephyrproject-rtos/zephyr/issues/48468) - GSM Mux does not transmit all queued data when uart\_fifo\_fill is called
- [GitHub #48394](https://github.com/zephyrproject-rtos/zephyr/issues/48394) - vsnprintfcb writes to `*str` if it is NULL
- [GitHub #48390](https://github.com/zephyrproject-rtos/zephyr/issues/48390) - [Intel Cavs] Boot failures on low optimization levels
- [GitHub #48317](https://github.com/zephyrproject-rtos/zephyr/issues/48317) - drivers: fpga: include driver for Lattice iCE40 parts
- [GitHub #48304](https://github.com/zephyrproject-rtos/zephyr/issues/48304) - bt\_disable() does not work properly on nRF52
- [GitHub #48299](https://github.com/zephyrproject-rtos/zephyr/issues/48299) - SHT3XD\_CMD\_WRITE\_TH\_LOW\_SET should be SHT3XD\_CMD\_WRITE\_TH\_LOW\_CLEAR
- [GitHub #48150](https://github.com/zephyrproject-rtos/zephyr/issues/48150) - Sensor Subsystem: data types
- [GitHub #48148](https://github.com/zephyrproject-rtos/zephyr/issues/48148) - Sensor Subsystem: Base sensor DTS bindings
- [GitHub #48147](https://github.com/zephyrproject-rtos/zephyr/issues/48147) - ztest: before/after functions may run on different threads, which may cause potential issues.
- [GitHub #48037](https://github.com/zephyrproject-rtos/zephyr/issues/48037) - Grove LCD Sample Not Working
- [GitHub #48018](https://github.com/zephyrproject-rtos/zephyr/issues/48018) - ztest: static threads are not re-launched for repeated test suite execution.
- [GitHub #47988](https://github.com/zephyrproject-rtos/zephyr/issues/47988) - JSON parser not consistent on extra data
- [GitHub #47877](https://github.com/zephyrproject-rtos/zephyr/issues/47877) - ECSPI support for NXP i.MX devices
- [GitHub #47872](https://github.com/zephyrproject-rtos/zephyr/issues/47872) - Differentiating Samples, Tests & Demos
- [GitHub #47833](https://github.com/zephyrproject-rtos/zephyr/issues/47833) - Intel CAVS: cavstool.py fails to extract complete log from winstream buffer when logging is frequent
- [GitHub #47830](https://github.com/zephyrproject-rtos/zephyr/issues/47830) - Intel CAVS: Build failure due to #47713 PR
- [GitHub #47817](https://github.com/zephyrproject-rtos/zephyr/issues/47817) - samples/modules/nanopb/sample.modules.nanopb fails with protobuf > 3.19.0
- [GitHub #47611](https://github.com/zephyrproject-rtos/zephyr/issues/47611) - ci: workflows: compliance: Add commit title to an error msg
- [GitHub #47607](https://github.com/zephyrproject-rtos/zephyr/issues/47607) - Settings with FCB backend does not pass test on stm32h743
- [GitHub #47576](https://github.com/zephyrproject-rtos/zephyr/issues/47576) - undefined reference to `__device_dts_ord_20` When building with board hifive\_unmatched on flash\_shell samples
- [GitHub #47500](https://github.com/zephyrproject-rtos/zephyr/issues/47500) - twister: cmake: Failure of “–build-only -M” combined with “–test-only” for –device-testing
- [GitHub #47477](https://github.com/zephyrproject-rtos/zephyr/issues/47477) - qemu\_leon3: tests/kernel/fpu\_sharing/generic/ failed when migrating to new ztest API
- [GitHub #47329](https://github.com/zephyrproject-rtos/zephyr/issues/47329) - Newlib nano variant footprint reduction
- [GitHub #47326](https://github.com/zephyrproject-rtos/zephyr/issues/47326) - drivers: WINC1500: issues with buffer allocation when using sockets
- [GitHub #47324](https://github.com/zephyrproject-rtos/zephyr/issues/47324) - drivers: modem: gsm\_ppp: support common gpios
- [GitHub #47315](https://github.com/zephyrproject-rtos/zephyr/issues/47315) - LE Audio: CAP Initiator skeleton Implementation
- [GitHub #47299](https://github.com/zephyrproject-rtos/zephyr/issues/47299) - LE Audio: Advertising (service) data for one or more services/roles
- [GitHub #47296](https://github.com/zephyrproject-rtos/zephyr/issues/47296) - LE Audio: Move board files for nRF5340 Audio development kit upstream
- [GitHub #47274](https://github.com/zephyrproject-rtos/zephyr/issues/47274) - mgmt/mcumgr/lib: Rework of event callback framework
- [GitHub #47243](https://github.com/zephyrproject-rtos/zephyr/issues/47243) - LE Audio: Add support for stream specific codec configurations for broadcast source
- [GitHub #47242](https://github.com/zephyrproject-rtos/zephyr/issues/47242) - LE Audio: Add subgroup support for broadcast source
- [GitHub #47092](https://github.com/zephyrproject-rtos/zephyr/issues/47092) - driver: nrf: uarte: new dirver breaks our implementation for uart.
- [GitHub #47040](https://github.com/zephyrproject-rtos/zephyr/issues/47040) - tests: drivers: gpio\_basic\_api and gpio\_api\_1pin: convert to new ztest API
- [GitHub #47014](https://github.com/zephyrproject-rtos/zephyr/issues/47014) - can: iso-tp: implementation test failed with twister on nucleo\_g474re
- [GitHub #46988](https://github.com/zephyrproject-rtos/zephyr/issues/46988) - samples: net: openthread: coprocessor: RCP is missing required capabilities: tx-security tx-timing
- [GitHub #46986](https://github.com/zephyrproject-rtos/zephyr/issues/46986) - Logging (deferred v2) with a lot of output causes MPU fault
- [GitHub #46897](https://github.com/zephyrproject-rtos/zephyr/issues/46897) - tests: posix: fs: improve tests to take better advantage of new ztest features
- [GitHub #46844](https://github.com/zephyrproject-rtos/zephyr/issues/46844) - Timer drivers likely have off-by-one in rapidly-presented timeouts
- [GitHub #46824](https://github.com/zephyrproject-rtos/zephyr/issues/46824) - Prevent new uses of old ztest API
- [GitHub #46598](https://github.com/zephyrproject-rtos/zephyr/issues/46598) - Logging with RTT backend on STM32WB strange behavier
- [GitHub #46596](https://github.com/zephyrproject-rtos/zephyr/issues/46596) - STM32F74X RMII interface does not work
- [GitHub #46491](https://github.com/zephyrproject-rtos/zephyr/issues/46491) - Zephyr SDK 0.15.0 Checklist
- [GitHub #46446](https://github.com/zephyrproject-rtos/zephyr/issues/46446) - lvgl: Using sw\_rotate with SSD1306 shield causes memory fault
- [GitHub #46351](https://github.com/zephyrproject-rtos/zephyr/issues/46351) - net: tcp: Implement fast-retransmit
- [GitHub #46326](https://github.com/zephyrproject-rtos/zephyr/issues/46326) - Async UART for STM32 U5 support
- [GitHub #46287](https://github.com/zephyrproject-rtos/zephyr/issues/46287) - Zephyr 3.2 release checklist
- [GitHub #46268](https://github.com/zephyrproject-rtos/zephyr/issues/46268) - Update RNDIS USB class codes for automatic driver loading by Windows
- [GitHub #46126](https://github.com/zephyrproject-rtos/zephyr/issues/46126) - pm\_device causes assertion error in sched.c with lis2dh
- [GitHub #46105](https://github.com/zephyrproject-rtos/zephyr/issues/46105) - RFC: Proposal of Integrating Trusted Firmware-A
- [GitHub #46073](https://github.com/zephyrproject-rtos/zephyr/issues/46073) - IPSP (IPv6 over BLE) example stop working after a short time
- [GitHub #45921](https://github.com/zephyrproject-rtos/zephyr/issues/45921) - Runtime memory usage
- [GitHub #45910](https://github.com/zephyrproject-rtos/zephyr/issues/45910) - [RFC] Zbus: a message bus system
- [GitHub #45891](https://github.com/zephyrproject-rtos/zephyr/issues/45891) - mgmt/mcumgr/lib: Refactoring of callback subsystem in image management (DFU)
- [GitHub #45814](https://github.com/zephyrproject-rtos/zephyr/issues/45814) - Armclang build fails due to missing source file
- [GitHub #45756](https://github.com/zephyrproject-rtos/zephyr/issues/45756) - Add overlay-bt-minimal.conf for smp\_svr sample application
- [GitHub #45697](https://github.com/zephyrproject-rtos/zephyr/issues/45697) - RING\_BUF\_DECLARE broken for C++
- [GitHub #45625](https://github.com/zephyrproject-rtos/zephyr/issues/45625) - LE Audio: Update CSIP API with new naming scheme
- [GitHub #45621](https://github.com/zephyrproject-rtos/zephyr/issues/45621) - LE Audio: Update VCP API with new naming scheme
- [GitHub #45427](https://github.com/zephyrproject-rtos/zephyr/issues/45427) - Bluetooth: Controller: LLCP: Data structure for communication between the ISR and the thread
- [GitHub #45222](https://github.com/zephyrproject-rtos/zephyr/issues/45222) - drivers: peci: user space handlers not building correctly
- [GitHub #45218](https://github.com/zephyrproject-rtos/zephyr/issues/45218) - rddrone\_fmuk66: I2C configuration incorrect
- [GitHub #45094](https://github.com/zephyrproject-rtos/zephyr/issues/45094) - stm32: Add USB HS device support to STM32H747
- [GitHub #44908](https://github.com/zephyrproject-rtos/zephyr/issues/44908) - Support ESP32 ADC
- [GitHub #44861](https://github.com/zephyrproject-rtos/zephyr/issues/44861) - WiFi support for STM32 boards
- [GitHub #44410](https://github.com/zephyrproject-rtos/zephyr/issues/44410) - drivers: modem: shell: `modem send` doesn’t honor line ending in modem cmd handler
- [GitHub #44399](https://github.com/zephyrproject-rtos/zephyr/issues/44399) - Zephyr RTOS support for Litex SoC with 64 bit rocket cpu.
- [GitHub #44377](https://github.com/zephyrproject-rtos/zephyr/issues/44377) - ISO Broadcast/Receive sample not working with coded PHY
- [GitHub #44324](https://github.com/zephyrproject-rtos/zephyr/issues/44324) - Compile error in byteorder.h
- [GitHub #44318](https://github.com/zephyrproject-rtos/zephyr/issues/44318) - boards: arm: rpi\_pico: Enable CONFIG\_ARM\_MPU=y for raspberry pi pico board
- [GitHub #44281](https://github.com/zephyrproject-rtos/zephyr/issues/44281) - Bluetooth: Use hardware encryption for encryption
- [GitHub #44164](https://github.com/zephyrproject-rtos/zephyr/issues/44164) - Implement the equivalent of PR #44102 in LLCP
- [GitHub #44055](https://github.com/zephyrproject-rtos/zephyr/issues/44055) - Immediate alert client
- [GitHub #43998](https://github.com/zephyrproject-rtos/zephyr/issues/43998) - posix: add include/posix to search path based on Kconfig
- [GitHub #43986](https://github.com/zephyrproject-rtos/zephyr/issues/43986) - interrupt feature for gpio\_mcp23xxx
- [GitHub #43836](https://github.com/zephyrproject-rtos/zephyr/issues/43836) - stm32: g0b1: RTT doesn’t work properly after stop mode
- [GitHub #43737](https://github.com/zephyrproject-rtos/zephyr/issues/43737) - Support compiling `` `native_posix `` targets on Windows using the MinGW
- [GitHub #43696](https://github.com/zephyrproject-rtos/zephyr/issues/43696) - mgmt/mcumgr: RFC: Standardize Kconfig option names for MCUMGR
- [GitHub #43655](https://github.com/zephyrproject-rtos/zephyr/issues/43655) - esp32c3: Connection fail loop
- [GitHub #43647](https://github.com/zephyrproject-rtos/zephyr/issues/43647) - Bluetooth: LE multirole: connection as central is not totally unreferenced on disconnection
- [GitHub #43604](https://github.com/zephyrproject-rtos/zephyr/issues/43604) - Checkpatch: Support in-code ignore tags
- [GitHub #43411](https://github.com/zephyrproject-rtos/zephyr/issues/43411) - STM32 SPI DMA issue
- [GitHub #43330](https://github.com/zephyrproject-rtos/zephyr/issues/43330) - usb\_dc\_nrfx.c starts usbd\_work\_queue with no name
- [GitHub #43308](https://github.com/zephyrproject-rtos/zephyr/issues/43308) - driver: serial: stm32: uart will lost data when use dma mode[async mode]
- [GitHub #43294](https://github.com/zephyrproject-rtos/zephyr/issues/43294) - LoRaWAN stack & user ChannelsMask
- [GitHub #43286](https://github.com/zephyrproject-rtos/zephyr/issues/43286) - Zephyr 3.1 Release Checklist
- [GitHub #42998](https://github.com/zephyrproject-rtos/zephyr/issues/42998) - Should board.dts enable peripherals by default?
- [GitHub #42910](https://github.com/zephyrproject-rtos/zephyr/issues/42910) - Bluetooth: Controller: CIS Data path setup: HCI ISO Data
- [GitHub #42908](https://github.com/zephyrproject-rtos/zephyr/issues/42908) - Bluetooth: Controller: CIG: LE Remove CIG
- [GitHub #42907](https://github.com/zephyrproject-rtos/zephyr/issues/42907) - Bluetooth: Controller: CIG: Disconnect: ACL disconnection leading to CIS Disconnection complete
- [GitHub #42906](https://github.com/zephyrproject-rtos/zephyr/issues/42906) - Bluetooth: Controller: CIG: Disconnect: Using HCI Disconnect: Generate LL\_CIS\_TERMINATE\_IND
- [GitHub #42905](https://github.com/zephyrproject-rtos/zephyr/issues/42905) - Bluetooth: Controller: CIG: LL Rejects: Remote request being rejected
- [GitHub #42902](https://github.com/zephyrproject-rtos/zephyr/issues/42902) - Bluetooth: Controller: CIG: Host reject: LE Reject CIS Request
- [GitHub #42900](https://github.com/zephyrproject-rtos/zephyr/issues/42900) - Bluetooth: Controller: CIG: LE Setup ISO Data Path
- [GitHub #42899](https://github.com/zephyrproject-rtos/zephyr/issues/42899) - Bluetooth: Controller: CIG: LE CIS Established Event
- [GitHub #42898](https://github.com/zephyrproject-rtos/zephyr/issues/42898) - Bluetooth: Controller: CIG: LE Accept CIS
- [GitHub #42897](https://github.com/zephyrproject-rtos/zephyr/issues/42897) - Bluetooth: Controller: CIG: LE CIS Request Event
- [GitHub #42896](https://github.com/zephyrproject-rtos/zephyr/issues/42896) - Bluetooth: Controller: CIG: LE Create CIS: NULL PDU scheduling
- [GitHub #42895](https://github.com/zephyrproject-rtos/zephyr/issues/42895) - Bluetooth: Controller: CIG: LE Create CIS: Control procedure with LL\_CIS\_REQ/RSP/IND PDU
- [GitHub #42894](https://github.com/zephyrproject-rtos/zephyr/issues/42894) - Bluetooth: Controller: CIG: LE Set CIG Parameters
- [GitHub #42700](https://github.com/zephyrproject-rtos/zephyr/issues/42700) - Support module.yml in zephyr repo
- [GitHub #42590](https://github.com/zephyrproject-rtos/zephyr/issues/42590) - mgmt/mcumgr/lib: RFC: Allow leaving out “rc” in successful respones and use “rc” only for SMP processing errors.
- [GitHub #42432](https://github.com/zephyrproject-rtos/zephyr/issues/42432) - i2c: unable to configure SAMD51 i2c clock frequency for standard (100 KHz) speeds
- [GitHub #42420](https://github.com/zephyrproject-rtos/zephyr/issues/42420) - mgmt/mcumgr/lib: Async image erase command with status check
- [GitHub #42374](https://github.com/zephyrproject-rtos/zephyr/issues/42374) - STM32L5: Entropy : Power Management not working due to entropy driver & stop mode
- [GitHub #42361](https://github.com/zephyrproject-rtos/zephyr/issues/42361) - OpenOCD flashing not working on cc1352r1\_launchxl/cc26x2r1\_launchxl
- [GitHub #41956](https://github.com/zephyrproject-rtos/zephyr/issues/41956) - Bluetooth: Controller: BIG: Synchronized receiver encryption support
- [GitHub #41955](https://github.com/zephyrproject-rtos/zephyr/issues/41955) - Bluetooth: Controller: BIG: Broadcaster encryption support
- [GitHub #41830](https://github.com/zephyrproject-rtos/zephyr/issues/41830) - CONF\_FILE, OVERLAY\_CONFIG parsing expands `${ZEPHYR_<whatever>_MODULE_DIR}`
- [GitHub #41823](https://github.com/zephyrproject-rtos/zephyr/issues/41823) - Bluetooth: Controller: llcp: Remote request are dropped due to lack of free proc\_ctx
- [GitHub #41822](https://github.com/zephyrproject-rtos/zephyr/issues/41822) - BLE IPSP sample cannot handle large ICMPv6 Echo Request
- [GitHub #41784](https://github.com/zephyrproject-rtos/zephyr/issues/41784) - virtio device driver
- [GitHub #41771](https://github.com/zephyrproject-rtos/zephyr/issues/41771) - tests: drivers: adc: Test doesn’t build for mec172xevb\_assy6906
- [GitHub #41765](https://github.com/zephyrproject-rtos/zephyr/issues/41765) - assert.h should not include non libc headers
- [GitHub #41694](https://github.com/zephyrproject-rtos/zephyr/issues/41694) - undefined reference to `_open`
- [GitHub #41622](https://github.com/zephyrproject-rtos/zephyr/issues/41622) - Infinite mutual recursion when SMP and ATOMIC\_OPERATIONS\_C are set
- [GitHub #41606](https://github.com/zephyrproject-rtos/zephyr/issues/41606) - stm32u5: Re-implement VCO input and EPOD configuration
- [GitHub #41581](https://github.com/zephyrproject-rtos/zephyr/issues/41581) - STM32 subghzspi fails pinctrl setup
- [GitHub #41380](https://github.com/zephyrproject-rtos/zephyr/issues/41380) - stm32h7: Ethernet: Migrate driver to the new eth HAL api
- [GitHub #41213](https://github.com/zephyrproject-rtos/zephyr/issues/41213) - LE Audio: Update GA services to use the multi-instance macro
- [GitHub #41212](https://github.com/zephyrproject-rtos/zephyr/issues/41212) - LE Audio: Store of bonded data
- [GitHub #41209](https://github.com/zephyrproject-rtos/zephyr/issues/41209) - LE Audio: MCS support for multiple instances
- [GitHub #41073](https://github.com/zephyrproject-rtos/zephyr/issues/41073) - twister: no way to specify arguments for the binary zephyr.exe
- [GitHub #40982](https://github.com/zephyrproject-rtos/zephyr/issues/40982) - Build system: West: Add a warning when used repository does not match manifest
- [GitHub #40972](https://github.com/zephyrproject-rtos/zephyr/issues/40972) - Power management support for MEC172x
- [GitHub #40944](https://github.com/zephyrproject-rtos/zephyr/issues/40944) - BUILTIN\_STACK\_CHECKER and MPU\_STACK\_GUARD with a thread using the FPU will fault the bulltin stack checker
- [GitHub #40928](https://github.com/zephyrproject-rtos/zephyr/issues/40928) - mgmt/mcumgr/lib: Check image consistency after writing last chunk
- [GitHub #40924](https://github.com/zephyrproject-rtos/zephyr/issues/40924) - mgmt/mcumgr/lib: Do not re-upload image, by default, to the secondary slot
- [GitHub #40868](https://github.com/zephyrproject-rtos/zephyr/issues/40868) - Add a pre and post initialization among CONFIG\_APPLICATION\_INIT\_PRIORITY
- [GitHub #40850](https://github.com/zephyrproject-rtos/zephyr/issues/40850) - Add Zephyr logging support to mgmt/mcumgr/lib
- [GitHub #40833](https://github.com/zephyrproject-rtos/zephyr/issues/40833) - driver: i2c: TCA9546a: Have compilation fails when driver init priority missmatch
- [GitHub #40642](https://github.com/zephyrproject-rtos/zephyr/issues/40642) - Why does CMake wrongly believe the rimage target is changing?
- [GitHub #40582](https://github.com/zephyrproject-rtos/zephyr/issues/40582) - how the zephyr supportting with running cadence hifi4 lx7,reset\_vectorXEA2.s ?
- [GitHub #40561](https://github.com/zephyrproject-rtos/zephyr/issues/40561) - BLE notification and indication callback data are difficult to pass to other threads…
- [GitHub #40560](https://github.com/zephyrproject-rtos/zephyr/issues/40560) - Callbacks lack context information…
- [GitHub #39740](https://github.com/zephyrproject-rtos/zephyr/issues/39740) - Road from pinmux to pinctrl
- [GitHub #39712](https://github.com/zephyrproject-rtos/zephyr/issues/39712) - bq274xx sensor - Fails to compile when CONFIG\_PM\_DEVICE enabled
- [GitHub #39598](https://github.com/zephyrproject-rtos/zephyr/issues/39598) - use of \_\_noinit with ecc memory hangs system
- [GitHub #39520](https://github.com/zephyrproject-rtos/zephyr/issues/39520) - Add support for the BlueNRG-LP SoC
- [GitHub #39431](https://github.com/zephyrproject-rtos/zephyr/issues/39431) - arduino\_nano\_33\_ble\_sense: Add More Devices to the Device Tree
- [GitHub #39331](https://github.com/zephyrproject-rtos/zephyr/issues/39331) - ti: cc13xx\_cc26xx: watchdog timer driver
- [GitHub #39234](https://github.com/zephyrproject-rtos/zephyr/issues/39234) - Add support for the Sensririon SCD30 CO2 sensor
- [GitHub #39194](https://github.com/zephyrproject-rtos/zephyr/issues/39194) - Process: investigate GitHub code review replacements
- [GitHub #39037](https://github.com/zephyrproject-rtos/zephyr/issues/39037) - CivetWeb samples fail to build with CONFIG\_NEWLIB\_LIBC
- [GitHub #39025](https://github.com/zephyrproject-rtos/zephyr/issues/39025) - Bluetooth: Periodic Advertising, Filter Accept List, Resolving list related variable name abbreviations
- [GitHub #38947](https://github.com/zephyrproject-rtos/zephyr/issues/38947) - Issue with SMP commands sent over the UART
- [GitHub #38880](https://github.com/zephyrproject-rtos/zephyr/issues/38880) - ARC: ARCv2: qemu\_arc\_em / qemu\_arc\_hs don’t work with XIP disabled
- [GitHub #38668](https://github.com/zephyrproject-rtos/zephyr/issues/38668) - ESP32S I2S
- [GitHub #38570](https://github.com/zephyrproject-rtos/zephyr/issues/38570) - Process: binary blobs in Zephyr
- [GitHub #38450](https://github.com/zephyrproject-rtos/zephyr/issues/38450) - Python script for checking PR errors
- [GitHub #38346](https://github.com/zephyrproject-rtos/zephyr/issues/38346) - twister command line parameter clean up and optimizate twister documents
- [GitHub #38291](https://github.com/zephyrproject-rtos/zephyr/issues/38291) - Make Zephyr modules compatible with PlatformIO libdeps
- [GitHub #38251](https://github.com/zephyrproject-rtos/zephyr/issues/38251) - cmake: DTC\_OVERLAY\_FILE flags cancel board <board>.overlay files
- [GitHub #38041](https://github.com/zephyrproject-rtos/zephyr/issues/38041) - Logging-related tests fails on qemu\_arc\_hs6x
- [GitHub #37855](https://github.com/zephyrproject-rtos/zephyr/issues/37855) - STM32 - kconfigs to determine if peripheral is available
- [GitHub #37346](https://github.com/zephyrproject-rtos/zephyr/issues/37346) - STM32WL LoRa increased the current in “suspend\_to\_idle” state
- [GitHub #37056](https://github.com/zephyrproject-rtos/zephyr/issues/37056) - Clarify device power states
- [GitHub #36953](https://github.com/zephyrproject-rtos/zephyr/issues/36953) - <err> lorawan: MlmeConfirm failed : Tx timeout
- [GitHub #36951](https://github.com/zephyrproject-rtos/zephyr/issues/36951) - twister: report information about tests instability
- [GitHub #36882](https://github.com/zephyrproject-rtos/zephyr/issues/36882) - MCUMGR: fs upload fail for first time file upload
- [GitHub #36724](https://github.com/zephyrproject-rtos/zephyr/issues/36724) - The road to a stable Controller Area Network driver API
- [GitHub #36601](https://github.com/zephyrproject-rtos/zephyr/issues/36601) - Add input support to audio\_codec
- [GitHub #36553](https://github.com/zephyrproject-rtos/zephyr/issues/36553) - LoRaWAN Sample: `join accept` but “Join failed”
- [GitHub #36544](https://github.com/zephyrproject-rtos/zephyr/issues/36544) - RFC: API Change: Bluetooth: Read Multiple
- [GitHub #36343](https://github.com/zephyrproject-rtos/zephyr/issues/36343) - Bluetooth: Mesh: Modularizing the proxy feature
- [GitHub #36301](https://github.com/zephyrproject-rtos/zephyr/issues/36301) - soc: cypress: Port Zephyr to Cypress CYW43907
- [GitHub #36297](https://github.com/zephyrproject-rtos/zephyr/issues/36297) - Move BSS section to the end of image
- [GitHub #35986](https://github.com/zephyrproject-rtos/zephyr/issues/35986) - POSIX: multiple definition of posix\_types
- [GitHub #35812](https://github.com/zephyrproject-rtos/zephyr/issues/35812) - ESP32 Factory app partition is not bootable
- [GitHub #35316](https://github.com/zephyrproject-rtos/zephyr/issues/35316) - log\_panic() hangs kernel
- [GitHub #35238](https://github.com/zephyrproject-rtos/zephyr/issues/35238) - ieee802.15.4 support for stm32wb55
- [GitHub #35237](https://github.com/zephyrproject-rtos/zephyr/issues/35237) - build: Enhance twister to follow all module.yml in module list
- [GitHub #35177](https://github.com/zephyrproject-rtos/zephyr/issues/35177) - example-application: Add example library & tests
- [GitHub #34949](https://github.com/zephyrproject-rtos/zephyr/issues/34949) - console Bluetooth LE backend
- [GitHub #34597](https://github.com/zephyrproject-rtos/zephyr/issues/34597) - Mismatch between `ot ping` and `net ping`
- [GitHub #34536](https://github.com/zephyrproject-rtos/zephyr/issues/34536) - Simple event-driven framework
- [GitHub #34324](https://github.com/zephyrproject-rtos/zephyr/issues/34324) - RTT is not working on STM32
- [GitHub #34269](https://github.com/zephyrproject-rtos/zephyr/issues/34269) - LOG\_MODE\_MINIMAL BUILD error
- [GitHub #34049](https://github.com/zephyrproject-rtos/zephyr/issues/34049) - Nordic nrf9160 switching between drivers and peripherals
- [GitHub #33876](https://github.com/zephyrproject-rtos/zephyr/issues/33876) - Lora sender sample build error for esp32
- [GitHub #33704](https://github.com/zephyrproject-rtos/zephyr/issues/33704) - BLE Shell Scan application filters
- [GitHub #32875](https://github.com/zephyrproject-rtos/zephyr/issues/32875) - Benchmarking Zephyr vs. RIOT-OS
- [GitHub #32756](https://github.com/zephyrproject-rtos/zephyr/issues/32756) - Enable mcumgr shell management to send responses to UART other than assigned to shell
- [GitHub #32733](https://github.com/zephyrproject-rtos/zephyr/issues/32733) - RS-485 support
- [GitHub #32339](https://github.com/zephyrproject-rtos/zephyr/issues/32339) - reimplement tests/kernel/timer/timer\_api
- [GitHub #32288](https://github.com/zephyrproject-rtos/zephyr/issues/32288) - Enhance the ADC functionality on the STM32 devices to all available ADC channels
- [GitHub #32213](https://github.com/zephyrproject-rtos/zephyr/issues/32213) - Universal error code type
- [GitHub #31959](https://github.com/zephyrproject-rtos/zephyr/issues/31959) - BLE firmware update STM32WB stuck in loop waiting for CPU2
- [GitHub #31298](https://github.com/zephyrproject-rtos/zephyr/issues/31298) - tests/kernel/gen\_isr\_table failed on hsdk and nsim\_hs\_smp sometimes
- [GitHub #30391](https://github.com/zephyrproject-rtos/zephyr/issues/30391) - Unit Testing in Zephyr
- [GitHub #30348](https://github.com/zephyrproject-rtos/zephyr/issues/30348) - XIP can’t be enabled with ARC MWDT toolchain
- [GitHub #30212](https://github.com/zephyrproject-rtos/zephyr/issues/30212) - Disk rewrites same flash page multiple times.
- [GitHub #30159](https://github.com/zephyrproject-rtos/zephyr/issues/30159) - Clean code related to dts fixup files
- [GitHub #30042](https://github.com/zephyrproject-rtos/zephyr/issues/30042) - usbd: support more than one configuration descriptors
- [GitHub #30023](https://github.com/zephyrproject-rtos/zephyr/issues/30023) - Device model: add debug helpers for when device\_get\_binding() fails
- [GitHub #29986](https://github.com/zephyrproject-rtos/zephyr/issues/29986) - Add support for a single node having multiple bus types
- [GitHub #29832](https://github.com/zephyrproject-rtos/zephyr/issues/29832) - Redundant error check of function uart\_irq\_update() in `tests/drivers/uart/uart_basic_api/src/test_uart_fifo.c`
- [GitHub #29495](https://github.com/zephyrproject-rtos/zephyr/issues/29495) - SD card slow write SPI/Fatfs/stm32
- [GitHub #29160](https://github.com/zephyrproject-rtos/zephyr/issues/29160) - arm: Always include arch/arm/include
- [GitHub #29136](https://github.com/zephyrproject-rtos/zephyr/issues/29136) - usb: add USB device stack shell support
- [GitHub #29135](https://github.com/zephyrproject-rtos/zephyr/issues/29135) - usb: allow the instances of a USB class to be enabled and disabled at runtime
- [GitHub #29134](https://github.com/zephyrproject-rtos/zephyr/issues/29134) - usb: allow more extensive settings of the device descriptor
- [GitHub #29133](https://github.com/zephyrproject-rtos/zephyr/issues/29133) - usb: USB device stack should store and validate the device state
- [GitHub #29132](https://github.com/zephyrproject-rtos/zephyr/issues/29132) - usb: USB device stack should track and check the state of control transfers
- [GitHub #29087](https://github.com/zephyrproject-rtos/zephyr/issues/29087) - Moving (some) boards to their own repo/module
- [GitHub #28998](https://github.com/zephyrproject-rtos/zephyr/issues/28998) - net: if: extend list of admin/operational states of network interface
- [GitHub #28872](https://github.com/zephyrproject-rtos/zephyr/issues/28872) - Support ESP32 as Bluetooth controller
- [GitHub #28864](https://github.com/zephyrproject-rtos/zephyr/issues/28864) - sanitycheck: Make sanitycheck test specifiacation compatible
- [GitHub #28617](https://github.com/zephyrproject-rtos/zephyr/issues/28617) - enable CONFIG\_TEST for all samples
- [GitHub #27819](https://github.com/zephyrproject-rtos/zephyr/issues/27819) - Memory Management for MMU-based devices for LTS2
- [GitHub #27258](https://github.com/zephyrproject-rtos/zephyr/issues/27258) - Ring buffer does not allow to partially put/get data
- [GitHub #26796](https://github.com/zephyrproject-rtos/zephyr/issues/26796) - Interrupts on Cortex-M do not work with CONFIG\_MULTITHREADING=n
- [GitHub #26392](https://github.com/zephyrproject-rtos/zephyr/issues/26392) - e1000 ethernet driver needs to be converted to DTS
- [GitHub #26109](https://github.com/zephyrproject-rtos/zephyr/issues/26109) - devicetree: overloaded DT\_REG\_ADDR() and DT\_REG\_SIZE() for PCI devices
- [GitHub #25917](https://github.com/zephyrproject-rtos/zephyr/issues/25917) - Bluetooth: Deadlock with TX of ACL data and HCI commands (command blocked by data)
- [GitHub #25417](https://github.com/zephyrproject-rtos/zephyr/issues/25417) - net: socket: socketpair: check for ISR context
- [GitHub #25407](https://github.com/zephyrproject-rtos/zephyr/issues/25407) - No tests/samples covering socket read()/write() calls
- [GitHub #25055](https://github.com/zephyrproject-rtos/zephyr/issues/25055) - Redundant flash shell commands
- [GitHub #24653](https://github.com/zephyrproject-rtos/zephyr/issues/24653) - device\_pm: clarify and document usage
- [GitHub #23887](https://github.com/zephyrproject-rtos/zephyr/issues/23887) - drivers: modem: question: Should modem stack include headers to put into zephyr/include?
- [GitHub #23165](https://github.com/zephyrproject-rtos/zephyr/issues/23165) - macOS setup fails to build for lack of “elftools” Python package
- [GitHub #23161](https://github.com/zephyrproject-rtos/zephyr/issues/23161) - I2C and sensor deinitialization
- [GitHub #23072](https://github.com/zephyrproject-rtos/zephyr/issues/23072) - #ifdef \_\_cplusplus missing in tracking\_cpu\_stats.h
- [GitHub #22049](https://github.com/zephyrproject-rtos/zephyr/issues/22049) - Bluetooth: IRK handling issue when using multiple local identities
- [GitHub #21995](https://github.com/zephyrproject-rtos/zephyr/issues/21995) - Bluetooth: controller: split: Porting of connection event length
- [GitHub #21724](https://github.com/zephyrproject-rtos/zephyr/issues/21724) - dts: edtlib: handle child-binding or child-child-binding as ‘normal’ binding with compatible
- [GitHub #21446](https://github.com/zephyrproject-rtos/zephyr/issues/21446) - samples: add SPI slave
- [GitHub #21239](https://github.com/zephyrproject-rtos/zephyr/issues/21239) - devicetree: Generation of the child-bindigs items as a common static initializer
- [GitHub #20707](https://github.com/zephyrproject-rtos/zephyr/issues/20707) - Define GATT service at run-time
- [GitHub #20262](https://github.com/zephyrproject-rtos/zephyr/issues/20262) - dt-binding for timers
- [GitHub #19713](https://github.com/zephyrproject-rtos/zephyr/issues/19713) - usb: investigate if Network Buffer can be used in USB device stack and USB drivers
- [GitHub #19496](https://github.com/zephyrproject-rtos/zephyr/issues/19496) - insufficient test case coverage for log subsystem
- [GitHub #19356](https://github.com/zephyrproject-rtos/zephyr/issues/19356) - LwM2M sample reorganization: split out LwM2M source into object-based .c files
- [GitHub #19259](https://github.com/zephyrproject-rtos/zephyr/issues/19259) - doc: two-column tricks for HTML breaks PDF
- [GitHub #19243](https://github.com/zephyrproject-rtos/zephyr/issues/19243) - Support SDHC & samples/subsys/fs on FRDM-K64F
- [GitHub #19152](https://github.com/zephyrproject-rtos/zephyr/issues/19152) - MK22F51212 MPU defines missing
- [GitHub #18892](https://github.com/zephyrproject-rtos/zephyr/issues/18892) - POSIX subsys: transition to #include\_next for header consistency
- [GitHub #17171](https://github.com/zephyrproject-rtos/zephyr/issues/17171) - Insufficient code coverage for lib/os/fdtable.c
- [GitHub #16961](https://github.com/zephyrproject-rtos/zephyr/issues/16961) - Modules: add a SHA1 check to avoid updating module in the past
- [GitHub #16942](https://github.com/zephyrproject-rtos/zephyr/issues/16942) - Missing test case coverage for include/misc/byteorder.h functions
- [GitHub #16851](https://github.com/zephyrproject-rtos/zephyr/issues/16851) - west flash error on zephyr v1.14.99
- [GitHub #16444](https://github.com/zephyrproject-rtos/zephyr/issues/16444) - drivers/flash/flash\_simulator: Support for required read alignment
- [GitHub #16088](https://github.com/zephyrproject-rtos/zephyr/issues/16088) - Verify POSIX PSE51 API requirements
- [GitHub #15453](https://github.com/zephyrproject-rtos/zephyr/issues/15453) - Kconfig should enforce that at most one Console driver is enabled at a time
- [GitHub #15181](https://github.com/zephyrproject-rtos/zephyr/issues/15181) - ztest issues
- [GitHub #14753](https://github.com/zephyrproject-rtos/zephyr/issues/14753) - nrf52840\_pca10056: Leading spurious 0x00 byte in UART output
- [GitHub #14577](https://github.com/zephyrproject-rtos/zephyr/issues/14577) - Address latency/performance in nRF51 timer ISR
- [GitHub #13170](https://github.com/zephyrproject-rtos/zephyr/issues/13170) - Porting guide for advanced board (multi CPU SoC)
- [GitHub #12504](https://github.com/zephyrproject-rtos/zephyr/issues/12504) - STM32: add USB\_OTG\_HS example
- [GitHub #12401](https://github.com/zephyrproject-rtos/zephyr/issues/12401) - Target Capabilities / Board Directory Layout Capabilities
- [GitHub #12367](https://github.com/zephyrproject-rtos/zephyr/issues/12367) - Power management strategy of Zephyr can’t work well on nRF52 boards.
- [GitHub #11594](https://github.com/zephyrproject-rtos/zephyr/issues/11594) - Cleanup GNUisms to make the code standards compliant
- [GitHub #9045](https://github.com/zephyrproject-rtos/zephyr/issues/9045) - A resource-saving programming model
- [GitHub #6198](https://github.com/zephyrproject-rtos/zephyr/issues/6198) - unit test: Add unit test example which appends source files to SOURCES list
- [GitHub #5697](https://github.com/zephyrproject-rtos/zephyr/issues/5697) - Driver API review/cleanup/rework
- [GitHub #3849](https://github.com/zephyrproject-rtos/zephyr/issues/3849) - Reduce the overall memory usage of the LwM2M library
- [GitHub #2837](https://github.com/zephyrproject-rtos/zephyr/issues/2837) - Ability to use hardware-based block ciphers
- [GitHub #2647](https://github.com/zephyrproject-rtos/zephyr/issues/2647) - Better cache APIs needed.
