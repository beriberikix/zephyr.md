---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/releases/release-notes-3.4.html
original_path: releases/release-notes-3.4.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Zephyr 3.4.0

We are pleased to announce the release of Zephyr version 3.4.0.

Major enhancements with this release include:

- Input subsystem: handles input events from various types of input devices and
  distributes them to other threads in the application.
- Barrier API: added architecture agnostic API for data memory barriers.
- USB Device support:

  - USB device controller API (UDC API) and nRF USBD controller driver.
  - USB device stack implementation using new UDC API.
- Added Power Delivery Source Support to the USB-C Stack.
- Bluetooth: Added support for Periodic Advertising with Responses (PAwR).
- Cache API functions are now fully in-lined by compilers.
- Added an API for real-time clocks (RTC).
- Added Retention subsystem.
- Added initial support for MMU on Xtensa.
- SMBus (System Management Bus) API.
- Various improvements to the testing framework and twister:

  - Introduction of 3 new test harnesses into twister supporting pyTest,
    GoogleTest and Robot Framework.
  - Transitioning to new Ztest API was completed and legacy Ztest was deprecated.
- Added Snippets: Support common configuration settings that can be used across
  platforms.

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

- CVE-2023-1901: Under embargo until 2023-07-04
- CVE-2023-1902: Under embargo until 2023-07-04

## API Changes

### Changes in this release

- Any applications using the mcuboot image manager
  ([`CONFIG_MCUBOOT_IMG_MANAGER`](../kconfig.md#CONFIG_MCUBOOT_IMG_MANAGER "CONFIG_MCUBOOT_IMG_MANAGER")) will now need to also select
  [`CONFIG_FLASH_MAP`](../kconfig.md#CONFIG_FLASH_MAP "CONFIG_FLASH_MAP") and [`CONFIG_STREAM_FLASH`](../kconfig.md#CONFIG_STREAM_FLASH "CONFIG_STREAM_FLASH"),
  this prevents a cmake dependency loop if the image manager Kconfig is enabled
  manually without also manually enabling the other options.
- Including hawkbit in an application now requires additional Kconfig options
  to be selected, previously these options would have been selected
  automatically but have changed from `select` options in Kconfig files to
  `depends on`:

  > | [`CONFIG_NVS`](../kconfig.md#CONFIG_NVS "CONFIG_NVS") |
  > | --- |
  > | [`CONFIG_FLASH`](../kconfig.md#CONFIG_FLASH "CONFIG_FLASH") |
  > | [`CONFIG_FLASH_MAP`](../kconfig.md#CONFIG_FLASH_MAP "CONFIG_FLASH_MAP") |
  > | [`CONFIG_STREAM_FLASH`](../kconfig.md#CONFIG_STREAM_FLASH "CONFIG_STREAM_FLASH") |
  > | [`CONFIG_REBOOT`](../kconfig.md#CONFIG_REBOOT "CONFIG_REBOOT") |
  > | [`CONFIG_HWINFO`](../kconfig.md#CONFIG_HWINFO "CONFIG_HWINFO") |
  > | [`CONFIG_NET_TCP`](../kconfig.md#CONFIG_NET_TCP "CONFIG_NET_TCP") |
  > | [`CONFIG_NET_SOCKETS`](../kconfig.md#CONFIG_NET_SOCKETS "CONFIG_NET_SOCKETS") |
  > | [`CONFIG_IMG_MANAGER`](../kconfig.md#CONFIG_IMG_MANAGER "CONFIG_IMG_MANAGER") |
  > | [`CONFIG_NETWORKING`](../kconfig.md#CONFIG_NETWORKING "CONFIG_NETWORKING") |
  > | [`CONFIG_HTTP_CLIENT`](../kconfig.md#CONFIG_HTTP_CLIENT "CONFIG_HTTP_CLIENT") |
  > | [`CONFIG_DNS_RESOLVER`](../kconfig.md#CONFIG_DNS_RESOLVER "CONFIG_DNS_RESOLVER") |
  > | [`CONFIG_JSON_LIBRARY`](../kconfig.md#CONFIG_JSON_LIBRARY "CONFIG_JSON_LIBRARY") |
  > | [`CONFIG_NET_SOCKETS_POSIX_NAMES`](../kconfig.md#CONFIG_NET_SOCKETS_POSIX_NAMES "CONFIG_NET_SOCKETS_POSIX_NAMES") |
  > | [`CONFIG_BOOTLOADER_MCUBOOT`](../kconfig.md#CONFIG_BOOTLOADER_MCUBOOT "CONFIG_BOOTLOADER_MCUBOOT") |
- Including updatehub in an application now requires additional Kconfig options
  to be selected, previously these options would have been selected
  automatically but have changed from `select` options in Kconfig files to
  `depends on`:

  > | [`CONFIG_FLASH`](../kconfig.md#CONFIG_FLASH "CONFIG_FLASH") |
  > | --- |
  > | [`CONFIG_STREAM_FLASH`](../kconfig.md#CONFIG_STREAM_FLASH "CONFIG_STREAM_FLASH") |
  > | [`CONFIG_FLASH_MAP`](../kconfig.md#CONFIG_FLASH_MAP "CONFIG_FLASH_MAP") |
  > | [`CONFIG_REBOOT`](../kconfig.md#CONFIG_REBOOT "CONFIG_REBOOT") |
  > | [`CONFIG_MCUBOOT_IMG_MANAGER`](../kconfig.md#CONFIG_MCUBOOT_IMG_MANAGER "CONFIG_MCUBOOT_IMG_MANAGER") |
  > | [`CONFIG_IMG_MANAGER`](../kconfig.md#CONFIG_IMG_MANAGER "CONFIG_IMG_MANAGER") |
  > | [`CONFIG_IMG_ENABLE_IMAGE_CHECK`](../kconfig.md#CONFIG_IMG_ENABLE_IMAGE_CHECK "CONFIG_IMG_ENABLE_IMAGE_CHECK") |
  > | [`CONFIG_BOOTLOADER_MCUBOOT`](../kconfig.md#CONFIG_BOOTLOADER_MCUBOOT "CONFIG_BOOTLOADER_MCUBOOT") |
  > | [`CONFIG_MPU_ALLOW_FLASH_WRITE`](../kconfig.md#CONFIG_MPU_ALLOW_FLASH_WRITE "CONFIG_MPU_ALLOW_FLASH_WRITE") |
  > | [`CONFIG_NETWORKING`](../kconfig.md#CONFIG_NETWORKING "CONFIG_NETWORKING") |
  > | [`CONFIG_NET_UDP`](../kconfig.md#CONFIG_NET_UDP "CONFIG_NET_UDP") |
  > | [`CONFIG_NET_SOCKETS`](../kconfig.md#CONFIG_NET_SOCKETS "CONFIG_NET_SOCKETS") |
  > | [`CONFIG_NET_SOCKETS_POSIX_NAMES`](../kconfig.md#CONFIG_NET_SOCKETS_POSIX_NAMES "CONFIG_NET_SOCKETS_POSIX_NAMES") |
  > | [`CONFIG_COAP`](../kconfig.md#CONFIG_COAP "CONFIG_COAP") |
  > | [`CONFIG_DNS_RESOLVER`](../kconfig.md#CONFIG_DNS_RESOLVER "CONFIG_DNS_RESOLVER") |
  > | [`CONFIG_JSON_LIBRARY`](../kconfig.md#CONFIG_JSON_LIBRARY "CONFIG_JSON_LIBRARY") |
  > | [`CONFIG_HWINFO`](../kconfig.md#CONFIG_HWINFO "CONFIG_HWINFO") |
- The sensor driver API clarified [`sensor_trigger_set()`](../hardware/peripherals/sensor.md#c.sensor_trigger_set "sensor_trigger_set") to state that
  the user-allocated sensor trigger will be stored by the driver as a pointer,
  rather than a copy, and passed back to the handler. This enables the handler
  to use [`CONTAINER_OF`](../kernel/util/index.md#c.CONTAINER_OF "CONTAINER_OF") to retrieve a context pointer when the trigger
  is embedded in a larger struct and requires that the trigger is not allocated
  on the stack. Applications that allocate a sensor trigger on the stack need
  to be updated.
- Converted few drivers to the [Input](../services/input/index.md#input) subsystem.

  - `gpio_keys`: moved out of `gpio`, replaced the custom API to use input
    events instead, the `zephyr,gpio-keys` binding is unchanged
    but now requires `zephyr,code` to be set.
  - `ft5336`: moved from [Keyboard Scan](../hardware/peripherals/kscan.md#kscan-api) to [Input](../services/input/index.md#input), renamed the Kconfig
    options from `CONFIG_KSCAN_FT5336`, `CONFIG_KSCAN_FT5336_PERIOD` and
    `KSCAN_FT5336_INTERRUPT` to [`CONFIG_INPUT_FT5336`](../kconfig.md#CONFIG_INPUT_FT5336 "CONFIG_INPUT_FT5336"),
    [`CONFIG_INPUT_FT5336_PERIOD`](../kconfig.md#CONFIG_INPUT_FT5336_PERIOD "CONFIG_INPUT_FT5336_PERIOD") and
    [`CONFIG_INPUT_FT5336_INTERRUPT`](../kconfig.md#CONFIG_INPUT_FT5336_INTERRUPT "CONFIG_INPUT_FT5336_INTERRUPT").
  - `kscan_sdl`: moved from [Keyboard Scan](../hardware/peripherals/kscan.md#kscan-api) to [Input](../services/input/index.md#input), renamed the Kconfig
    option from `KSCAN_SDL` to [`CONFIG_INPUT_SDL_TOUCH`](../kconfig.md#CONFIG_INPUT_SDL_TOUCH "CONFIG_INPUT_SDL_TOUCH") and the
    compatible from `zephyr,sdl-kscan` to
    [`zephyr,input-sdl-touch`](../build/dts/api/bindings/input/zephyr%2Cinput-sdl-touch.md#std-dtcompatible-zephyr-input-sdl-touch).
  - `nuvoton,npcx-kscan` moved to [Input](../services/input/index.md#input), renamed the Kconfig option
    names from `KSCAN_NPCX_...` to `INPUT_NPCX_KBD...` and the compatible
    from `nuvoton,npcx-kscan` to [`nuvoton,npcx-kbd`](../build/dts/api/bindings/input/nuvoton%2Cnpcx-kbd.md#std-dtcompatible-nuvoton-npcx-kbd).
  - Touchscreen drivers converted to use the input APIs can use the
    [`zephyr,kscan-input`](../build/dts/api/bindings/kscan/zephyr%2Ckscan-input.md#std-dtcompatible-zephyr-kscan-input) driver to maintain Kscan compatibility.
- The declaration of `main()` has been changed from `void
  main(void)` to `int main(void)`. The main function is required to
  return the value zero. All other return values are reserved. This aligns
  Zephyr with the C and C++ language specification requirements for
  “hosted” environments, avoiding compiler warnings and errors. These
  compiler messages are generated when applications are built in “hosted”
  mode (which means without the `-ffreestanding` compiler flag). As the
  `-ffreestanding` flag is currently enabled unless the application is
  using picolibc, only applications using picolibc will be affected by this
  change at this time.
- The following network interface APIs now take additional,
  `struct net_if * iface` parameter:

  - [`net_if_ipv4_maddr_join()`](../connectivity/networking/api/net_if.md#c.net_if_ipv4_maddr_join "net_if_ipv4_maddr_join")
  - [`net_if_ipv4_maddr_leave()`](../connectivity/networking/api/net_if.md#c.net_if_ipv4_maddr_leave "net_if_ipv4_maddr_leave")
  - [`net_if_ipv6_maddr_join()`](../connectivity/networking/api/net_if.md#c.net_if_ipv6_maddr_join "net_if_ipv6_maddr_join")
  - [`net_if_ipv6_maddr_leave()`](../connectivity/networking/api/net_if.md#c.net_if_ipv6_maddr_leave "net_if_ipv6_maddr_leave")
- MCUmgr transports now need to set up the struct before registering it by
  setting the function pointers to the function handlers, these have been
  moved to a `functions` struct object of type
  [`smp_transport_api_t`](../services/device_mgmt/smp_transport.md#c.smp_transport_api_t "smp_transport_api_t"). Because of these changes, the legacy
  transport registration function and object are no longer available. The
  registration function now returns a value which is 0 for success or a
  negative error code if an error occurred.
- Added a new flag [`dac_channel_cfg`](../hardware/peripherals/dac.md#c.dac_channel_cfg "dac_channel_cfg") `buffered` for DAC channels in
  [`dac_channel_cfg`](../hardware/peripherals/dac.md#c.dac_channel_cfg "dac_channel_cfg") to allow the configuration of the output buffer.
  The actual interpretation of this depends on the hardware and is so far only
  implemented for the STM32 DAC driver. Implicitly for this driver this changes
  the default from being buffered to unbuffered.
- MCUmgr fs\_mgmt group’s file access hook is now called for all fs\_mgmt group
  functions (adding support for file status and file hash/checksum). In
  addition, if the file access state is not lost, it will now only be called
  once for the file access instead of each time a command is received.
  Note that the structure for the notification has changed, the `upload` bool
  has been replaced with an enum to indicate what function is used, see
  [`fs_mgmt_file_access`](../services/device_mgmt/mcumgr_callbacks.md#c.fs_mgmt_file_access "fs_mgmt_file_access") for the new structure definition.
- Iterable sections API is now available at
  [include/zephyr/sys/iterable\_sections.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/iterable_sections.h). LD linker snippets are
  available at [include/zephyr/linker/iterable\_sections.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/linker/iterable_sections.h).
- Cache API functions are now fully inlined by compilers.
- The Bluetooth HCI headers have been reworked, with `hci.h` now containing
  only the function prototypes and the new `hci_types.h` defining all
  HCI-related macros and structs. The previous `hci_err.h` has been merged
  into `hci_types.h`.

### Removed APIs in this release

- Pinmux API has been removed. Pin control needs to be used as its replacement,
  refer to [Pin Control](../hardware/pinctrl/index.md#pinctrl-guide) for more details.

### Deprecated in this release

- Configuring applications with `prj_<board>.conf` files has been deprecated,
  this should be replaced by using a prj.conf with the common configuration and
  board-specific configuration in board Kconfig fragments in the `boards`
  folder of the application.
- On nRF51 and nRF52-based boards, the behavior of the reset reason being
  provided to `sys_reboot()` and being set in the GPREGRET register has
  been dropped. This function will now just reboot the device without changing
  the register contents. The new method for setting this register uses the boot
  mode feature of the retention subsystem, see the
  [boot mode API](../services/retention/index.md#boot-mode-api) for details. To restore the deprecated
  functionality, enable
  `CONFIG_NRF_STORE_REBOOT_TYPE_GPREGRET`.
- Deprecated `PTHREAD_BARRIER_DEFINE` in favor of the standardized
  `pthread_barrier_init()`
- On all STM32 targets except STM32F2 series, Ethernet drivers implementation
  based on STM32Cube Ethernet API V1 ([`CONFIG_ETH_STM32_HAL_API_V1`](../kconfig.md#CONFIG_ETH_STM32_HAL_API_V1 "CONFIG_ETH_STM32_HAL_API_V1"))
  is now deprecated in favor of implementation based on more reliable and performant
  STM32Cube Ethernet API V2.
- Legacy Ztest API was deprecated. All new tests shall use the new Ztest API.

### Stable API changes in this release

- Removed bt\_set\_oob\_data\_flag and replaced it with two new API calls:
  \* [`bt_le_oob_set_sc_flag()`](../connectivity/bluetooth/api/connection_mgmt.md#c.bt_le_oob_set_sc_flag "bt_le_oob_set_sc_flag") for setting/clearing OOB flag in SC pairing
  \* [`bt_le_oob_set_legacy_flag()`](../connectivity/bluetooth/api/connection_mgmt.md#c.bt_le_oob_set_legacy_flag "bt_le_oob_set_legacy_flag") for setting/clearing OOB flag in legacy paring
- `SYS_INIT` callback no longer requires a [`device`](../kernel/drivers/index.md#c.device "device") argument.
  The new callback signature is `int f(void)`. A utility script to
  automatically migrate existing projects can be found in
  [scripts/utils/migrate\_sys\_init.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/utils/migrate_sys_init.py).
- Changed [`spi_config`](../hardware/peripherals/spi.md#c.spi_config "spi_config") `cs` ([`spi_cs_control`](../hardware/peripherals/spi.md#c.spi_cs_control "spi_cs_control")) from
  pointer to struct member. This allows using the existing SPI dt-spec macros in
  C++. SPI controller drivers doing `NULL` checks on the `cs` field to check
  if CS is GPIO-based or not, must now use [`spi_cs_is_gpio()`](../hardware/peripherals/spi.md#c.spi_cs_is_gpio "spi_cs_is_gpio") or
  [`spi_cs_is_gpio_dt()`](../hardware/peripherals/spi.md#c.spi_cs_is_gpio_dt "spi_cs_is_gpio_dt") calls.

### New APIs in this release

- Introduced [`flash_ex_op()`](../hardware/peripherals/flash.md#c.flash_ex_op "flash_ex_op") function. This allows to perform extra
  operations on flash devices, defined by Zephyr Flash API or by vendor specific
  header files. Support for extra operations is enabled by
  [`CONFIG_FLASH_EX_OP_ENABLED`](../kconfig.md#CONFIG_FLASH_EX_OP_ENABLED "CONFIG_FLASH_EX_OP_ENABLED") which depends on
  [`CONFIG_FLASH_HAS_EX_OP`](../kconfig.md#CONFIG_FLASH_HAS_EX_OP "CONFIG_FLASH_HAS_EX_OP") selected by driver.
- Introduced [Real-Time Clock (RTC)](../hardware/peripherals/rtc.md#rtc-api) API which adds experimental support for real-time clock
  devices. These devices previously used the [Counter](../hardware/peripherals/counter.md#counter-api) API combined with
  conversion between unix-time and broken-down time. The new API adds the mandatory
  functions [`rtc_set_time()`](../hardware/peripherals/rtc.md#c.rtc_set_time "rtc_set_time") and [`rtc_get_time()`](../hardware/peripherals/rtc.md#c.rtc_get_time "rtc_get_time"), the optional functions
  [`rtc_alarm_get_supported_fields()`](../hardware/peripherals/rtc.md#c.rtc_alarm_get_supported_fields "rtc_alarm_get_supported_fields"), [`rtc_alarm_set_time()`](../hardware/peripherals/rtc.md#c.rtc_alarm_set_time "rtc_alarm_set_time"),
  [`rtc_alarm_get_time()`](../hardware/peripherals/rtc.md#c.rtc_alarm_get_time "rtc_alarm_get_time"), [`rtc_alarm_is_pending()`](../hardware/peripherals/rtc.md#c.rtc_alarm_is_pending "rtc_alarm_is_pending") and
  [`rtc_alarm_set_callback()`](../hardware/peripherals/rtc.md#c.rtc_alarm_set_callback "rtc_alarm_set_callback") are enabled with
  [`CONFIG_RTC_ALARM`](../kconfig.md#CONFIG_RTC_ALARM "CONFIG_RTC_ALARM"), the optional function
  [`rtc_update_set_callback()`](../hardware/peripherals/rtc.md#c.rtc_update_set_callback "rtc_update_set_callback") is enabled with
  [`CONFIG_RTC_UPDATE`](../kconfig.md#CONFIG_RTC_UPDATE "CONFIG_RTC_UPDATE"), and lastly, the optional functions
  [`rtc_set_calibration()`](../hardware/peripherals/rtc.md#c.rtc_set_calibration "rtc_set_calibration") and [`rtc_get_calibration()`](../hardware/peripherals/rtc.md#c.rtc_get_calibration "rtc_get_calibration") are enabled with
  [`CONFIG_RTC_CALIBRATION`](../kconfig.md#CONFIG_RTC_CALIBRATION "CONFIG_RTC_CALIBRATION").
- Introduced [Auxiliary Display (auxdisplay)](../hardware/peripherals/auxdisplay.md#auxdisplay-api) for auxiliary (alphanumeric-based) displays.
- Introduced [Barriers API](../hardware/barriers/index.md#barriers-api) for barrier operations.
- Added [`CAN_FRAME_ESI`](../hardware/peripherals/can/controller.md#c.CAN_FRAME_ESI "CAN_FRAME_ESI") CAN-FD Error State Indicator flag.

## Kernel

- Removed absolute symbols `___cpu_t_SIZEOF`,
  `_STRUCT_KERNEL_SIZE`, `K_THREAD_SIZEOF` and
  `_DEVICE_STRUCT_SIZEOF`

## Architectures

- ARC

  - Added MPUv8 support
  - Add support of virtual UART over ARC hostlink channel
  - Improved ARCv2 HS4x processors handling - added proper Kconfig options, provided default mcpu
  - Improved ARCMWDT toolchain handling:

    - added rollback to check METAWARE\_ROOT if ARCMWDT\_TOOLCHAIN\_PATH missing
    - reworked extra warnings options handling in twister so it can be used with ARCMWDT
    - used 64bit MDB binary by default
  - Fixed excessive ROM memory consumption if MPU is enabled and ROM & RAM are located in different
    memory regions
  - Fixed DSP registers handling in case of ARCMWDT
  - Improved SMP handling:

    - Fixed potential livelock in thread abort due to exception
    - Fixed IDU mask setup
  - Removed absolute symbols `___callee_saved_t_SIZEOF` and
    `_K_THREAD_NO_FLOAT_SIZEOF`
- ARM

  - Removed absolute symbols `___basic_sf_t_SIZEOF`,
    `_K_THREAD_NO_FLOAT_SIZEOF`, `___cpu_context_t_SIZEOF`
    and `___thread_stack_info_t_SIZEOF`
  - Enabled fp16 for Cortex-M55
  - Fixed a compilation issue with arm-clang and TrustZone
  - Implemented a new cache-management API
  - Added support for generating zImage headers
  - Introduced a new `z_arm_on_enter_cpu_idle()` hook on CPU idle
- ARM64

  - Removed absolute symbol `___callee_saved_t_SIZEOF`
  - Enabled FPU and FPU\_SHARING for v8r aarch64
  - Fixed the STACK\_INIT logic during the reset
  - Introduced and enabled safe exception stack
  - Fixed possible deadlock on SMP with FPU sharing
  - Added ISBs after SCTLR Modifications
- NIOS2

  - Removed absolute symbol `_K_THREAD_NO_FLOAT_SIZEOF`
- POSIX:

  - Added `Z_SPIN_DELAY` to allow to conditionally compile a k\_busy\_wait() for this arch
    in tests and samples.
- RISC-V

  - Added [`CONFIG_PMP_NO_TOR`](../kconfig.md#CONFIG_PMP_NO_TOR "CONFIG_PMP_NO_TOR"), [`CONFIG_PMP_NO_NA4`](../kconfig.md#CONFIG_PMP_NO_NA4 "CONFIG_PMP_NO_NA4"), and
    [`CONFIG_PMP_NO_NAPOT`](../kconfig.md#CONFIG_PMP_NO_NAPOT "CONFIG_PMP_NO_NAPOT") to allow disabling unsupported PMP range modes.
  - Removed unused symbols: `_thread_offset_to_tp`,
    `_thread_offset_to_priv_stack_start`, `_thread_offset_to_user_sp`.
  - Added support for setting PMP granularity with [`CONFIG_PMP_GRANULARITY`](../kconfig.md#CONFIG_PMP_GRANULARITY "CONFIG_PMP_GRANULARITY").
  - Switched from accessing CSRs from inline assembly to using the `csr_read()` helper
    function.
  - Enabled single-threading support.
- SPARC

  - Removed absolute symbol `_K_THREAD_NO_FLOAT_SIZEOF`
- Xtensa

  - Fixed the cross stack call mechanism during nested interrupts where stack would be
    corrupted under certain conditions.
  - Added initial support for MMU on Xtensa.
  - Now supports building with [`CONFIG_MULTITHREADING`](../kconfig.md#CONFIG_MULTITHREADING "CONFIG_MULTITHREADING") disabled so
    target can run in single thread only operations.
  - Added C structs to represent interrupt frames to help with debugging.

## Bluetooth

- General

  - Moved all logging symbols together in a new `Kconfig.logging` file.
  - Deprecated the `BT_DEBUG_LOG` option. Instead `BT_LOG` should be used.
  - Made the `BT_LOG` and `BT_LOG_LEGACY` options hidden.
  - Removed `BT_DEBUG` entirely.
- Audio

  - Implemented the CAP initiator broadcast audio start, stop and metadata
    update procedures.
  - Implemented the CAP unicast audio start, stop and metadata update procedures.
  - Implemented the Telephony and Media Audio Service (TMAS).
  - Added additional validation for MCC and MCS, including opcodes, values, etc.
  - Refactored and extended the scan delegator implementation, including
    integration with broadcast sink.
  - Added support for creating a broadcast sink from a PA sink.
  - Added support for optional characteristics in CSIP.
  - Implemented discovery by UUID instead of reading by UUID for multiple
    characteristics.
  - Added support for long reads and writes for multiple profiles.
  - Added support for long BAP ASE notifications and optimized long notify
    reads.
  - Offloaded MCS notifications to the system workqueue.
  - Added the CAP initiator cancel procedure.
- Direction Finding
- Host

  - Updated the Host to the v5.4 specification.
  - The GATT DB Hash is now recalculated upon loading settings.
  - Added experimental support for SMP keypress notifications.
  - Downgraded the severity of select log messages to avoid log flooding.
  - Separated the handling of LE SC OOB pairing from the legacy OOB logic.
  - Implemented the Encrypted Advertising Data feature.
  - Added support for the new Periodic Advertising with Responses (PAwR), both
    as an advertiser and as a scanner.
  - Added support for initiating connections from PAwR, as well as receiving
    connections while synced.
  - Clarified the behavior that is enabled by the `BT_PRIVACY` Kconfig option.
  - Introduced a new `seg_recv` L2CAP API for an application to receive
    segments directly and manage credits explicitly.
- Mesh

  - Added experimental support for Mesh Protocol d1.1r18 specification, gated
    by a new configuration option. This includes:

    - Enhanced Provisioning Authentication support.
    - Mesh Remote Provisioning support including:

      - Remote Provisioning Server and Client models.
      - Composition Data Page 128 and Models Metadata Page 128 support.
    - Large Composition Data support including:

      - Large Composition Data Server and Client models.
      - Models Metadata Page 0 support.
    - New Transport Segmentation and Reassembly (SAR) implementation including:

      - SAR Configuration Server and Client models.
    - Mesh Private Beacons support including:

      - Mesh Private Beacon Server and Client models.
    - Opcodes Aggregator support including:

      - Opcodes Aggregator Server and Client models.
    - Proxy Solicitation support including:

      - Solicitation PDU RPL Configuration Server and Client models.
      - On-Demand Private Proxy Server and Client models.
    - Composition Data Page 1 support.
    - Other Mesh Profile Enhancements.
  - Added experimental support for Mesh Binary Large Object Transfer Model d1.0r04\_PRr00 specification.
  - Added experimental support for Mesh Device Firmware Update Model d1.0r04\_PRr00 specification.
  - Fixed multiple profile errata.
  - Added experimental support for the PSA crypto APIs.
  - Added a new work queue to store mesh settings, including a new API for
    storing user data.
  - Disabled the models initialization macros for C++ as they use the compound
    literal feature from C99.
  - Deprecated Health Client and Configuration Client API have been removed.
- Controller

  - Implemented support for the central with multiple CIS usecase.
  - Implemented support for multiple peripheral CIS establishment.
  - Updated the Controller to the v5.4 specification.
  - Added support for coexistence with other transceivers.
  - Added support for multiple CIS/CIG setup/connect and teardown procedures in
    sequence.
  - Extended the ticker API to return expiration info.
  - Re-implemented Extended and Periodic Advertising, as well as and Broadcast
    ISO, using the new ticket expiration info feature.
  - Modified the ticker implementation to reschedule unreserved tickers that use
    `ticks_slot_window`. Implement continuous scanning with it.
  - Added support for considering the SDU interval, along with the packet
    sequence number and time stamps, in SDU fragmentation.
  - Added a new `BT_CTRL_TX_PWR_DBM` option to set the TX power directly in
    dBm.
  - Optimized the RX path with support for piggy-backing notifications on
    already-allocated RX nodes.
- HCI Driver

## Boards & SoC Support

- Added support for these SoC series:

  - STM32C0 series are now supported (with introduction of STM32C031 SoC).
  - STM32H5 series are now supported (with introduction of STM32H503 and STM32H573 SoCs).
  - Added support for STM32U599 SoC variants
  - Nordic Semiconductor nRF9161
- Removed support for these SoC series:
- Made these changes in other SoC series:
- Added support for these ARC boards:

  - DesignWare ARC HS4x/HS4xD Development Kit (HSDK4xD) - ARCv2 HS47D, SMP 4 cores
  - nsim\_hs3x\_hostlink - simulation (nSIM-based) platform with hostlink UART
- Added support for these ARM boards:

  - Aconno ACN52832
  - Alientek STM32L475 Pandora
  - Arduino GIGA R1 Wi-Fi
  - BeagleConnect Freedom
  - Infineon PSoC™ 6 BLE Prototyping Kit (CY8CPROTO-063-BLE)
  - Infineon PSoC™ 6 Wi-Fi BT Prototyping Kit (CY8CPROTO-062-4343W)
  - Infineon XMC4700 Relax Kit
  - MXChip AZ3166 IoT DevKit
  - Nordic Semiconductor nRF9161 DK
  - NXP MIMXRT1040-EVK
  - NXP MIMXRT1062 FMURT6
  - PHYTEC PhyBOARD Polis (NXP i.MX8M Mini)
  - PHYTEC PhyBOARD Pollux (NXP i.MX8M Plus)
  - Raspberry Pi Pico W
  - Raytac MDBT50Q-DB-33
  - Raytac MDBT50Q-DB-40
  - Seeed Studio Wio Terminal
  - Seeed Studio XIAO BLE Sense
  - Silicon Labs BRD2601B
  - Silicon Labs BRD4187C
  - Silicon Labs EFR32 Thunderboard-style boards
  - ST Nucleo C031C6
  - ST Nucleo F042K6
  - ST Nucleo H563ZI
  - ST STM32H573I-DK Discovery
  - Xilinx KV260 (Cortex-R5)
- Added support for these ARM64 boards:

  - PHYTEC phyCORE-AM62x A53
  - NXP i.MX93 EVK A55 (SOF variant)
- Added support for these RISC-V boards:

  - Intel FPGA Nios® V/m
  - ITE IT82XX2 EV-Board
- Added support for these X86 boards:
- Added support for these Xtensa boards:

  - ESP32S3-DevKitM
- Made these changes for ARC boards:

  - Added ARC MWDT toolchain support for qemu\_arc\_hs
  - Improved emsdp platform support:

    - Added DFSS driver support
    - Added pinctrl support
- Made these changes for ARM boards:

  - `atsamc21n_xpro`: Enable support to CAN.
  - `atsame54_xpro`: Read Ethernet MAC from I2C.
  - Changed the default board revision to 0.14.0 for the Nordic boards
    `nrf9160dk_nrf9160` and `nrf9160dk_nrf52840`. To build for an
    older revision of the nRF9160 DK without external flash, specify that
    older board revision when building.
  - `nrf9160dk_nrf52840`: Enabled external\_flash\_pins\_routing switch by default.
  - `nrf9160dk_nrf9160`: Changed the order of buttons and switches on the GPIO
    expander to match the order when using GPIO directly on the nRF9160 SoC.
  - `STM32H747i_disco`: Enabled support for ST B-LCD40-DSI1 display extension
  - `qemu_cortex_m0`: Fixed prescaler of the system timer so that its frequency
    is actually 1 MHz, not 2 MHz.
- Made these changes for ARM64 boards:

  - FVP revc\_2xaemv8a / aemv8r: Added ethernet, PHY and MDIO nodes
- Made these changes to POSIX boards:

  > - nrf52\_bsim now includes support and models for:
  >
  >   - 802.15.4 in the RADIO.
  >   - EGU.
  >   - FLASH (NVMC & UICR).
  >   - TEMP.
  >   - UART connected to a host ptty.
  >   - Many more minor CMSIS API and nRF APIs and drivers.
- Made these changes for RISC-V boards:

  - `gd32vf103`: No longer requires special OpenOCD version.
- Made these changes for X86 boards:
- Made these changes for Xtensa boards:
- Removed support for these ARC boards:
- Removed support for these ARM boards:
- Removed support for these RISC-V boards:

  - BeagleV Starlight JH7100
- Removed support for these X86 boards:
- Removed support for these Xtensa boards:
- Made these changes in other boards:
- Added support for these following shields:

  - Adafruit Data Logger Shield
  - nPM1300 EK (Power Management Integrated Circuit (PMIC))
  - Panasonic Grid-EYE Shields
  - ST B\_LCD40\_DSI1\_MB1166

## Build system and infrastructure

- Fixed an issue whereby older versions of the Zephyr SDK toolchain were used
  instead of the latest compatible version.
- Fixed an issue whereby building an application with sysbuild and specifying
  mcuboot’s verification to be checksum only did not build a bootable image.
- Fixed an issue whereby if no prj.conf file was present then board
  configuration files would not be included by emitting a fatal error. As a
  result, prj.conf files are now mandatory in projects.
- Introduced support for extending/replacing the signing mechanism in zephyr,
  see [West extending signing](../develop/west/sign.md#west-extending-signing) for further
  details.
- Fixed an issue whereby when using `*_ROOT` variables with Sysbuild, these
  were lost for images.
- Enhanced `zephyr_get` CMake helper function to optionally support merging
  of scoped variables into a list.
- Added a new CMake helper function for setting/updating sysbuild CMake cache
  variables: `sysbuild_cache_set`.
- Enhanced `zephyr_get` CMake helper function to lookup multiple variables
  and return the result in a variable of different name.
- Introduced `EXTRA_CONF_FILE`, `EXTRA_DTC_OVERLAY_FILE`, and
  `EXTRA_ZEPHYR_MODULES` for better naming consistency and uniform behavior
  for applying extra build settings in addition to Zephyr automatic build
  setting lookup.
  `EXTRA_CONF_FILE` replaces `OVERLAY_CONFIG`.
  `EXTRA_ZEPHYR_MODULES` replaces `ZEPHYR_EXTRA_MODULES`.
  `EXTRA_DTC_OVERLAY_FILE` is new, see
  [Set devicetree overlays](../build/dts/howtos.md#set-devicetree-overlays) for further details.
- Twister now supports `gtest` harness for running tests written in gTest.
- Added an option to validate device initialization priorities at build time.
  To use it, enable [`CONFIG_CHECK_INIT_PRIORITIES`](../kconfig.md#CONFIG_CHECK_INIT_PRIORITIES "CONFIG_CHECK_INIT_PRIORITIES"), see
  [scripts/build/check\_init\_priorities.py](../build/cmake/index.md#check-init-priorities-py) for more details.
- Added a new option to disable tracking of macro expansion when compiling,
  [`CONFIG_COMPILER_TRACK_MACRO_EXPANSION`](../kconfig.md#CONFIG_COMPILER_TRACK_MACRO_EXPANSION "CONFIG_COMPILER_TRACK_MACRO_EXPANSION"). This option may be
  disabled to reduce compiler verbosity when errors occur during macro
  expansions, e.g. in device definition macros.
- Twister now supports loading test configurations from alternative root
  folder/s by using `--alt-config-root`. When a test is found, Twister will
  check if a test configuration file exist in any of the alternative test
  configuration root folders. For example, given
  `$test_root/tests/foo/testcase.yaml`, Twister will use
  `$alt_config_root/tests/foo/testcase.yaml` if it exists.
- Twister now uses native YAML lists for fields that were previously defined
  using space-separated strings. For example:

  ```yaml
  platform_allow: foo bar
  ```

  can now be written as:

  ```yaml
  platform_allow:
    - foo
    - bar
  ```

  This applies to the following properties:

  > - `arch_exclude`
  > - `arch_allow`
  > - `depends_on`
  > - `extra_args`
  > - `extra_sections`
  > - `platform_exclude`
  > - `platform_allow`
  > - `tags`
  > - `toolchain_exclude`
  > - `toolchain_allow`

  Note that the old behavior is kept as deprecated. The
  [scripts/utils/twister\_to\_list.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/utils/twister_to_list.py) script can be used to
  automatically migrate Twister configuration files.
- When MCUboot image signing is enabled, a warning will now be emitted by cmake
  if no signing key is set in the project, this warning can be safely ignored
  if signing is performed manually or outside of zephyr. This warning informs
  the user that the generated image will not be bootable by MCUboot as-is.
- Babblesim is now included in the west manifest. Users can fetch it by enabling
  the `babblesim` group with west config.
- west sign now uses DT labels, of “fixed-partition” compatible nodes, to identify
  application image slots, instead of previously used DT node label properties.
  If you have been using custom partition layout for MCUboot, you will have to label
  your MCUboot slot partitions with proper DT node labels; for example partition
  with “image-0” label property will have to be given slot0\_partition DT node label.
  Label property does not have to be removed from partition node, but will not be used.

  DT node labels used are listed below

  | Partition with label property | Required DT node label |
  | --- | --- |
  | “image-0” | slot0\_partition |
  | “image-1” | slot1\_partition |
- Fixed an issue whereby relative paths supplied for the `BOARD_ROOT` value
  might wrongly emit a warning about a `boards` directory not being found.
- Fixed an issue whereby relative paths did not work for sysbuild images.

## Drivers and Sensors

- Device model

  - Devices that do not require an initialization routine can now pass `NULL`
    to the `DEVICE_*_DEFINE()` macros.
- Auxiliary display

  - New auxiliary display (auxdisplay) peripheral has been added, this allows
    for interfacing with simple alphanumeric displays that do not feature
    graphic capabilities. This peripheral is marked as unstable.
  - HD44780 driver added.
  - Noritake Itron driver added.
  - Grove LCD driver added (ported from existing sample).
- ADC

  - MCUX LPADC driver now uses the channel parameter to select a software channel
    configuration buffer. Use `zephyr,input-positive` and
    `zephyr,input-negative` devicetree properties to select the hardware
    channel(s) to link a software channel configuration to.
  - MCUX LPADC driver `voltage-ref` and `power-level` devicetree properties
    were shifted to match the hardware as described in reference manual instead
    of matching the NXP SDK enum identifiers.
  - Added support for STM32C0 and STM32H5.
  - Added DMA support for STM32H7.
  - STM32: Resolutions are now listed in the device tree for each ADC instance
  - STM32: Sampling times are now listed in the device tree for each ADC instance
  - Added driver for Atmel SAM family ADC.
  - Added driver for Gecko Incremental ADC.
  - Added driver for Infineon CAT1 ADC.
  - Added driver for TI ADS7052.
  - Added driver for TI ADS114S0x family.
  - Added drivers for Renesas SmartBond GPADC and SDADC.
- Battery-backed RAM

  - Added MCP7940N battery-backed RTC SRAM driver.
- CAN

  - The CAN statistics are now reset when calling [`can_start()`](../hardware/peripherals/can/controller.md#c.can_start "can_start").
  - Renamed the NXP FlexCAN devicetree binding compatible from `nxp,kinetis-flexcan` to
    [`nxp,flexcan`](../build/dts/api/bindings/can/nxp%2Cflexcan.md#std-dtcompatible-nxp-flexcan).
  - Added support for the CAN-FD variant of the NXP FlexCAN controller using devicetree binding
    [`nxp,flexcan-fd`](../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd).
  - Added support for the NXP NXP S32 CANEXCEL controller using devicetree binding
    [`nxp,s32-canxl`](../build/dts/api/bindings/can/nxp%2Cs32-canxl.md#std-dtcompatible-nxp-s32-canxl).
  - Added support for the Atmel SAM0 CAN controller using devicetree binding
    [`atmel,sam0-can`](../build/dts/api/bindings/can/atmel%2Csam0-can.md#std-dtcompatible-atmel-sam0-can).
  - Refactored the Bosch M\_CAN controller driver backend to allow for per-instance configuration via
    devicetree.
  - Now supports STM32H5 series.
- Clock control

  - Atmel SAM/SAM0: Introduced peripheral clock control.
  - Atmel SAM0: Improved `samd20`/`samd21`/`samr21` clocking mechanism.
  - STM32F4: Added support for PLL I2S
- Console:

  - The native\_posix and bsim console drivers have been merged into one generic
    driver usable by all POSIX arch based boards.
- Counter

  - Added support on timer based counter on STM32H7 and STM32H5
  - Added support on RTC based counter on STM32C0 and STM32H5
- Crypto

  - Added support for STM32H5 AES
- DAC

  - Added support on STM32H5 series.
- Disk

  - SDMMC STM32L4+: Now compatible with internal DMA
  - NVME disks are now supported using FATFS, with a single I/O queue enabled
- Display

  - Improved MCUX ELCDIF and SSD16XX display controller drivers
  - Added support for ILI9342C display controller
  - Added support for OTM8009A panel
- DMA

  - STM32C0: Added support for DMA
  - STM32H5: Added support for GPDMA
  - STM32H7: Added support for BDMA
  - Added DMA support for the RP2040 SoC
- EEPROM

  - Switched from [`atmel,at24`](../build/dts/api/bindings/mtd/atmel%2Cat24.md#std-dtcompatible-atmel-at24) to dedicated [`zephyr,i2c-target-eeprom`](../build/dts/api/bindings/mtd/zephyr%2Ci2c-target-eeprom.md#std-dtcompatible-zephyr-i2c-target-eeprom) for I2C EEPROM target driver.
- Entropy

  - Added support for STM32H5 series.
- Flash

  - Introduced new flash API call [`flash_ex_op()`](../hardware/peripherals/flash.md#c.flash_ex_op "flash_ex_op") which calls
    `ec_op()` callback provided by a flash driver. This allows to perform
    extra operations on flash devices, defined by Zephyr Flash API or by vendor
    specific header files. [`CONFIG_FLASH_HAS_EX_OP`](../kconfig.md#CONFIG_FLASH_HAS_EX_OP "CONFIG_FLASH_HAS_EX_OP") should be
    selected by the driver to indicate that extra operations are supported.
    To enable extra operations user should select
    [`CONFIG_FLASH_EX_OP_ENABLED`](../kconfig.md#CONFIG_FLASH_EX_OP_ENABLED "CONFIG_FLASH_EX_OP_ENABLED").
  - STM32F4: Now supports write protection and readout protection through
    new flash API call [`flash_ex_op()`](../hardware/peripherals/flash.md#c.flash_ex_op "flash_ex_op").
  - nrf\_qspi\_nor: Replaced custom API function `nrf_qspi_nor_base_clock_div_force`
    with `nrf_qspi_nor_xip_enable` which apart from forcing the clock divider
    prevents the driver from deactivating the QSPI peripheral so that the XIP
    operation is actually possible.
  - flash\_simulator:

    - A memory region can now be used as the storage area for the
      flash simulator. Using the memory region allows the flash simulator to keep
      its contents over a device reboot.
    - When building in native\_posix, command line options have been added to select
      if the flash should be cleared at boot, the flash content kept in RAM,
      or the flash content file be deleted on exit.
  - spi\_flash\_at45: Fixed erase procedure to properly handle chips that have
    their initial sector split into two parts (usually marked as 0a and 0b).
  - STM32H5 now supports OSPI
- GPIO

  - Converted the `gpio_keys` driver to the input subsystem.
  - Added single-ended IO support for the RP2040 SoC
  - STM32: Supports newly introduced experimental API to enable/disable interrupts
    without re-config
- I2C

  - Added support for STM32C0 and STM32H5 series
- I2S

  - STM32: Domain clock should now be configured by device tree.
- Input

  - Introduced the [Input](../services/input/index.md#input) subsystem.
- KSCAN

  - Added a [`zephyr,kscan-input`](../build/dts/api/bindings/kscan/zephyr%2Ckscan-input.md#std-dtcompatible-zephyr-kscan-input) input to kscan compatibility driver.
  - Converted the `ft5336` and `kscan_sdl` drivers to the input subsystem.
- MIPI-DSI

  - Added support on STM32H7
- Misc

  > - Added PIO support for the RP2040 SoC
- PCIE

  - Enable filtering PCIe devices by class/revision.
- PECI
- Retained memory

  - Retained memory (retained\_mem) driver has been added with backends for
    Nordic nRF GPREGRET, and uninitialised RAM.
- Pin control

  - Added support for Infineon CAT1
  - Added support for TI K3
  - Added support for ARC emdsp
- PWM

  - Added support for STM32C0.
  - STM32: Now supports 6-PWM channels
  - Added PWM driver for Microchip XEC BBLED.
- Power domain
- Regulators

  - The regulator API can now be built without thread-safe reference counting
    by using [`CONFIG_REGULATOR_THREAD_SAFE_REFCNT`](../kconfig.md#CONFIG_REGULATOR_THREAD_SAFE_REFCNT "CONFIG_REGULATOR_THREAD_SAFE_REFCNT"). This
    feature can be useful in applications that do not enable
    [`CONFIG_MULTITHREADING`](../kconfig.md#CONFIG_MULTITHREADING "CONFIG_MULTITHREADING").
  - Added support for ADP5360 PMIC
  - Added support for nPM1300 PMIC
  - Added support for Raspberry Pi Pico core supply regulator
- SDHC

  - Support was added for using CPOL/CPHA SPI clock modes with SD cards, as
    some cards require the SPI clock switch to low when not active
- Sensor

  - Added generic voltage measurement sample
  - Removed STM32 Vbat measurement sample (replaced by a generic one)
  - Added STM32 Vref sensor driver
  - Added STM32 Vref/Vbat measurement through the new generic voltage measurement sample
  - Added temperature measurement driver for STM32C0 and STM32F0x0
  - Removed STM32 temperature measurement sample (replaced by a generic one)
  - Added STM32 temperature measurement through the generic temperature measurement sample
- Serial

  - Added UART3 and UART4 configuration for `gd32vf103` SoCs.
  - uart\_altera: added new driver for Altera Avalon UART.
  - uart\_emul: added new driver for emulated UART.
  - uart\_esp32:
    \* Added support for ESP32S3 SoC.
    \* Added support for RS-485 half duplex mode.
  - uart\_hostlink: added new driver for virtual UART via Synopsys ARC hostlink channels.
  - uart\_ifx\_cat1: added new driver for Infineon CAT1 UART.
  - uart\_mcux: added power management support.
  - uart\_mcux\_flexcomm: added support for asynchronous operations.
  - uart\_mcux\_lpuart: added support for parity.
  - uart\_ns16550: now supports per instance hardware access mode instead of
    one access mode for all instances.
  - uart\_pl011: fixed interrupt support.
  - uart\_rpi\_pico\_pio: added new driver to support UART via
    Programmable Input/Output (PIO) on Raspberry Pi Pico.
  - uart\_xmc4xxx: added support for asynchronous operations.
  - uart\_stm32: Now support driver enable mode
  - Added hardware flow control support for the RP2040 SoC
- SPI

  - Added support on STM32H5 series.
- Timer

  - Support added for stopping Nordic nRF RTC system timer, which fixes an
    issue when booting applications built in prior version of Zephyr.
  - STM32: Now supports a prescaler at the input of clock (default not divided).
    Prescaler allows to achieve higher LPTIM timeout (up to 256s when lptim clocked by LSE)
    and consequently higher core sleep durations but impacts the tick precision.
    To be used with caution.
- USB

  > - Added remote wakeup support for the RP2040 SoC
  > - Added Battery Charging (BC12) API and PI3USB9201 driver implementation.
  > - Added new USB device controller drivers (using usb\_dc API) for ITE IT82xx2
  >   and smartbond platforms.
  > - Added USB device controller driver skeleton for UDC API.
  > - Reworked DWC2 driver and added support for STM32F4 SoC family
- W1

  - Added DS2482-800 1-Wire master driver. See the [`maxim,ds2482-800`](../build/dts/api/bindings/w1/maxim%2Cds2482-800.md#std-dtcompatible-maxim-ds2482-800)
    devicetree binding for more information.
  - Added [`CONFIG_W1_NET_FORCE_MULTIDROP_ADDRESSING`](../kconfig.md#CONFIG_W1_NET_FORCE_MULTIDROP_ADDRESSING "CONFIG_W1_NET_FORCE_MULTIDROP_ADDRESSING") which can be
    enabled force the 1-Wire network layer to use multidrop addressing.
- Watchdog

  - Added support for STM32C0 and STM32H5 series

## Networking

- CoAP:

  - Added [`coap_append_descriptive_block_option()`](../connectivity/networking/api/coap.md#c.coap_append_descriptive_block_option "coap_append_descriptive_block_option") and
    [`coap_get_block1_option()`](../connectivity/networking/api/coap.md#c.coap_get_block1_option "coap_get_block1_option") APIs to facilitate block transfer handling.
  - Added a [CoAP client](../connectivity/networking/api/coap_client.md#coap-client-interface) helper library, based on the existing CoAP APIs.
  - Fixed missing token length validation in [`coap_header_get_token()`](../connectivity/networking/api/coap.md#c.coap_header_get_token "coap_header_get_token").
  - Fixed missing response check in [`coap_response_received()`](../connectivity/networking/api/coap.md#c.coap_response_received "coap_response_received").
- Connection Manager:

  - Extended the library with a generic L2 connectivity API.
  - Refactored library internals significantly.
  - Improved thread safety in the library.
  - Reworked how Connection Manager events are notified - they are no longer
    raised for each interface individually, but instead:

    - `NET_EVENT_L4_CONNECTED` is called only once after the first
      interface gains connectivity.
    - `NET_EVENT_L4_DISCONNECTED` is called only after connectivity is
      lost on all interfaces.
  - Improved Connection Manager test coverage.
- DHCPv4:

  - Fixed a potential packet leak in DHCPv4 input handler.
  - Fixed a potential NULL pointer dereference in `dhcpv4_create_message()`.
  - Added a mechanism to register a callback for handling DHCPv4 options.
  - Modified `dhcpv4_client` sample to trigger DHCP on all network interfaces
    in the system.
- DNS:

  - Fixed a possible crash on NULL pointer as a query callback.
  - Added a check on existing DNS servers before reconfigure.
  - Improved debug logging in DNS SD.
  - Fixed IPv4/IPv6 address handling in mDNS responder, if both are IPv4 and IPv6 are enabled.
  - Removed dead code in DNS SD query parsing.
- Ethernet:

  - Fixed double packet dereference in case of ARP request transmission errors.
  - Fixed a possible slist corruption in case Ethernet interface went up before
    LLDP initialization.
- HTTP:

  - Added HTTP service and resource iterable sections.
- ICMPv6:

  - Implemented IPv6 RA Recursive DNS Server option handling.
- IEEE802154:

  - Fixed a corner case with 6LoWPAN IP Header Compression and fragmentation, where
    for a short range of packet sizes, fragmentation did not work correctly after IPHC.
  - Added new radio API function to start continuous carrier wave transmission.
  - Several improvements/fixes in IEEE802154 L2 security.
  - Fixed a packet leak when handling beacon/command frames.
  - Deprecated [`CONFIG_IEEE802154_2015`](../kconfig.md#CONFIG_IEEE802154_2015 "CONFIG_IEEE802154_2015") Kconfig option.
  - Added simple Babblesim echo test over IEEE802154 L2.
  - Improved IEEE802154 L2 test coverage.
  - Multiple other minor IEEE802154 L2 and documentation improvements/fixes.
- IPv4:

  - Implemented a fallback to IPv4 Link Local address if no other address is available.
  - Fixed [`net_ipv4_is_ll_addr()`](../connectivity/networking/api/ip_4_6.md#c.net_ipv4_is_ll_addr "net_ipv4_is_ll_addr") helper function to correctly identify LL address.
  - Fixed possible NULL pointer dereference in IPv4 fragmentation.
- LwM2M:

  - Added new [`LWM2M_RD_CLIENT_EVENT_REG_UPDATE`](../connectivity/networking/api/lwm2m.md#c.lwm2m_rd_client_event.LWM2M_RD_CLIENT_EVENT_REG_UPDATE "LWM2M_RD_CLIENT_EVENT_REG_UPDATE") event.
  - Added missing `const` qualifier in the APIs, where applicable.
  - Fixed socket error handling on packet transmission.
  - Improved LwM2M context cleanup when falling back to regular Registration.
  - Added possibility to register a callback function for FW update cancel action.
  - Added possibility to register a callback function for LwM2M send operation.
  - Added ISPO voltage sensor object support.
  - Fixed stopping of the LwM2M client when it’s suspended.
  - Fixed a minor CoAP RFC incompatibility, where it should not be assumed that
    consecutive data blocks in block transfer will carry the same token.
  - Added block transfer support on TX.
  - Fixed a possible out-of-bounds memory access when creating FW update object.
  - Added possibility to override default socket option configuration with a
    dedicated callback function (`set_socketoptions`).
  - Improved LwM2M test coverage.
  - Several other minor improvements and cleanups.
- Misc:

  - Added generic `OFFLOADED_NETDEV_L2` for offloaded devices to allow
    offloaded implementations to detect when interface is brought up/down.
  - Factored out `net_buf_simple` routines to a separate source file.
  - Fixed possible NULL pointer dereference in `net_pkt_cursor_operate()`.
  - Reimplemented `net_mgmt` to use message queue internally. This also fixed
    a possible event loss with the old implementation.
  - Fixed error handling in `net ping` shell command to avoid shell freeze.
  - Improved Ethernet error statistics logging in `net stats` shell command.
  - Moved SLIP TAP implementation into a separate file, to prevent build warnings
    about missing sources for Ethernet drivers.
  - Fixed crashes in `echo_server` and `echo_client` samples, when
    userspace is enabled.
  - Fixed IPv6 support in `mqtt_sn_publisher` sample.
  - Fixed build issues with arm-clang in the networking stack.
  - Added new `NET_IF_IPV6_NO_ND` and `NET_IF_IPV6_NO_MLD` interface flags,
    which allow to disable ND/MLD respectively on an interface.
  - Reworked network interface mutex protection, to use individual mutex for
    each interface, instead of a global one.
  - Added new [AWS IoT Core MQTT](../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.").
  - Added a few missing NULL pointer checks in network interface functions.
- OpenThread:

  - Implemented the following OpenThread platform APIs:

    - `otPlatRadioSetMacFrameCounterIfLarger()`,
    - `otPlatCryptoEcdsaGenerateAndImportKey()`,
    - `otPlatCryptoEcdsaExportPublicKey()`,
    - `otPlatCryptoEcdsaVerifyUsingKeyRef()`,
    - `otPlatCryptoEcdsaSignUsingKeyRef()`.
  - Added [`CONFIG_OPENTHREAD_CSL_TIMEOUT`](../kconfig.md#CONFIG_OPENTHREAD_CSL_TIMEOUT "CONFIG_OPENTHREAD_CSL_TIMEOUT") option.
  - Removed no longer needed `CONFIG_OPENTHREAD_EXCLUDE_TCPLP_LIB`.
  - Added simple Babblesim echo test over OpenThread.
- SNTP:

  - Switched to use `zsock_*` functions internally.
- Sockets:

  - Fixed `SO_RCVBUF` and `SO_SNDBUF` socket options handling, so that they
    configure TCP window sizes correctly.
  - Fixed `SO_SNDTIMEO` socket option handling - the timeout value was ignored
    and socket behaved as in non-blocking mode when used.
  - Reworked TLS sockets implementation, to allow parallel TX/RX from
    different threads.
  - Implemented TLS handshake timeout.
  - Added support for asynchronous connect for TCP sockets.
  - Fixed blocking [`recv()`](../connectivity/networking/api/sockets.md#c.recv "recv") not being interrupted on socket close.
  - Fixed blocking [`accept()`](../connectivity/networking/api/sockets.md#c.accept "accept") not being interrupted on socket close.
  - Improved sockets test coverage.
- TCP:

  - Fixed incorrect TCP stats by improving packet processing result reporting.
  - Added [`CONFIG_NET_TCP_PKT_ALLOC_TIMEOUT`](../kconfig.md#CONFIG_NET_TCP_PKT_ALLOC_TIMEOUT "CONFIG_NET_TCP_PKT_ALLOC_TIMEOUT") to allow to configure
    packet allocation timeout.
  - Improved TCP test coverage.
  - Fixed TCP MSS calculation for IPv6.
  - Fixed possible double acknowledgment of retransmitted data.
  - Fixed local address setting for incoming connections.
  - Fixed double TCP context dereferencing in certain corner cases.
- TFTP:

  - Added `tftp_put()` API to support TFTP write request.
  - Introduced `tftp_callback_t` callback to allow to read large files.
  - Reworked `struct tftpc` client context structure, to allow for parallel
    communication from several contexts.
- UDP:

  - [`CONFIG_NET_UDP_MISSING_CHECKSUM`](../kconfig.md#CONFIG_NET_UDP_MISSING_CHECKSUM "CONFIG_NET_UDP_MISSING_CHECKSUM") is now enabled by default.
- Websockets:

  - Implemented proper timeout handling in [`websocket_recv_msg()`](../connectivity/networking/api/websocket.md#c.websocket_recv_msg "websocket_recv_msg").
  - Fixed implicit type conversion when parsing length field, which could lead
    to data loss.
- Wi-Fi:

  - Display TWT (Target Wake Time) configuration response status in Wi-Fi shell.
  - Added more detailed TWT response parameters printout in Wi-Fi shell.
  - Added new `NET_EVENT_WIFI_TWT_SLEEP_STATE` event to notify TWT sleep status.
  - Fixed an issue where not all security modes were displayed correctly on scan.
  - Added connection status and AP capabilities verification before initiating
    TWT operation.
  - TWT intervals are changed from milliseconds to microseconds, interval
    variables are also renamed.
  - Extended Power Saving configuration parameters with listening interval and
    wake up mode.
  - Added [`CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS`](../kconfig.md#CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS "CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS") option, which
    enables providing of RAW (unprocessed) scan results to the application with
    `NET_EVENT_WIFI_CMD_RAW_SCAN_RESULT` event.
  - Several other minor fixes/cleanups in the Wi-Fi management/shell modules.
- zperf

  - Added an extra parameter to disable Nagle’s algorithm with TCP benchmarks.
  - Added support for handling multiple incoming TCP sessions.
  - Made zperf thread priority and stack size configurable.
  - Several minor cleanups in the module.

## USB

- USB device support

  - Fixed control endpoint handling with MPS of 8 bytes.
- New experimental USB support

  - Various improvements for new device support, better string descriptor support,
    implemented usbd\_class\_shutdown API.
  - Added USB Mass Storage class and CDC ECM class implementations for the new
    device support.

## Libraries / Subsystems

- File systems

  - Added [`CONFIG_FS_FATFS_REENTRANT`](../kconfig.md#CONFIG_FS_FATFS_REENTRANT "CONFIG_FS_FATFS_REENTRANT") to enable the FAT FS reentrant option.
  - With LittleFS as backend, [`fs_mount()`](../services/file_system/index.md#c.fs_mount "fs_mount") return code was corrected to `EFAULT` when
    called with `FS_MOUNT_FLAG_NO_FORMAT` and the designated LittleFS area could not be
    mounted because it has not yet been mounted or it required reformatting.
  - The FAT FS initialization order has been updated to match LittleFS, fixing an issue where
    attempting to mount the disk in a global function caused FAT FS to fail due to not being registered beforehand.
    FAT FS is now initialized in POST\_KERNEL.
  - Added [`CONFIG_FS_LITTLEFS_FMP_DEV`](../kconfig.md#CONFIG_FS_LITTLEFS_FMP_DEV "CONFIG_FS_LITTLEFS_FMP_DEV") to enable possibility of using LittleFS
    for block devices only, e.g. without Flash support. The option is set to ‘y’ by default in
    order to keep previous behaviour.
- IPC

  - [`ipc_service_close_instance()`](../services/ipc/ipc_service/ipc_service.md#c.ipc_service_close_instance "ipc_service_close_instance") now only acts on bounded endpoints.
  - ICMSG: removed race condition during bonding.
  - ICMSG: removed internal API for clearing shared memory.
  - ICMSG: added mutual exclusion access to SHMEM.
  - Fixed CONFIG\_OPENAMP\_WITH\_DCACHE.
- Management

  - Added optional input expiration to shell MCUmgr transport, this allows
    returning the shell to normal operation if a complete MCUmgr packet is not
    received in a specific duration. Can be enabled with
    [`CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT`](../kconfig.md#CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT "CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT") and timeout
    set with
    [`CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT_TIME`](../kconfig.md#CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT_TIME "CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT_TIME").
  - MCUmgr fs\_mgmt upload and download now caches the file handle to improve
    throughput when transferring data, the file is no longer opened and closed
    for each part of a transfer. In addition, new functionality has been added
    that will allow closing file handles of uploaded/downloaded files if they
    are idle for a period of time, the timeout is set with
    `MCUMGR_GRP_FS_FILE_AUTOMATIC_IDLE_CLOSE_TIME`. There is a
    new command that can be used to close open file handles which can be used
    after a file upload is complete to ensure that the file handle is closed
    correctly, allowing other transports or other parts of the application
    code to use it.
  - A new version of the SMP protocol used by MCUmgr has been introduced in the
    header, which is used to indicate the version of the protocol being used.
    This updated protocol allows returning much more detailed error responses
    per group, see the
    [MCUmgr SMP protocol specification](../services/device_mgmt/smp_protocol.md#mcumgr-smp-protocol-specification)
    for details.
  - MCUmgr has now been marked as a stable Zephyr API.
  - The MCUmgr UDP transport has been refactored to resolve some concurrency
    issues and fixes a potential issue whereby an application might call the
    open transport function whilst it is already open, causing an endless log
    output loop.
  - The MCUmgr fs\_mgmt group Kconfig `Insecure` text has been replaced with
    a CMake warning which triggers if fs\_mgmt hooks are not enabled, as these
    hooks can be used to ensure security of file access allowed by MCUmgr
    clients.
  - Fixed an issue with MCUmgr fs\_mgmt file download not checking if the
    offset parameter was provided.
  - Fixed an issue with MCUmgr fs\_mgmt file upload notification hook not
    setting upload to true.
  - Fixed an issue with MCUmgr img\_mgmt image upload `upgrade` field wrongly
    checking if the new image was the same version of the application and
    allowing it to be uploaded if it was.
  - MCUmgr img\_mgmt group will only verify the SHA256 hash provided by the
    client against the uploaded image (if support is enabled) if a full SHA256
    hash was provided.
  - MCUmgr Kconfig options have changed from `select` to `depends on` which
    means that some additional Kconfig options may now need to be selected by
    applications. [`CONFIG_NET_BUF`](../kconfig.md#CONFIG_NET_BUF "CONFIG_NET_BUF"),
    [`CONFIG_ZCBOR`](../kconfig.md#CONFIG_ZCBOR "CONFIG_ZCBOR") and [`CONFIG_CRC`](../kconfig.md#CONFIG_CRC "CONFIG_CRC") are needed
    to enable MCUmgr support, [`CONFIG_BASE64`](../kconfig.md#CONFIG_BASE64 "CONFIG_BASE64") is needed to
    enable shell/UART/dummy MCUmgr transports,
    [`CONFIG_NET_SOCKETS`](../kconfig.md#CONFIG_NET_SOCKETS "CONFIG_NET_SOCKETS") is needed to enable the UDP MCUmgr
    transport, [`CONFIG_FLASH`](../kconfig.md#CONFIG_FLASH "CONFIG_FLASH") is needed to enable MCUmgr
    fs\_mgmt, [`CONFIG_FLASH`](../kconfig.md#CONFIG_FLASH "CONFIG_FLASH") and
    [`CONFIG_IMG_MANAGER`](../kconfig.md#CONFIG_IMG_MANAGER "CONFIG_IMG_MANAGER") are needed to enable MCUmgr img\_mgmt.
  - MCUmgr img\_mgmt group now uses unsigned integer values for image and slot
    numbers, these numbers would never have been negative and should have been
    unsigned.
- POSIX API

  - Improved the locking strategy for `eventfd_read()` and
    `eventfd_write()`. This eliminated a deadlock scenario that was
    present since the initial contribution and increased performance by a
    factor of 10x.
  - Reimplemented [POSIX](../services/portability/posix/index.md#posix-support) threads, mutexes, condition
    variables, and barriers using native Zephyr counterparts. POSIX
    synchronization primitives in Zephyr were originally implemented
    separately and received less maintenance as a result. Unfortunately, this
    opened POSIX up to unique bugs and race conditions. Going forward, POSIX
    will benefit from all improvements to Zephyr’s synchronization and
    threading API and race conditions have been mitigated.
- Retention

  - Retention subsystem has been added which adds enhanced features over
    retained memory drivers allowing for partitioning, magic headers and
    checksum validation. See [retention API](../services/retention/index.md#retention-api) for details.
    Support for the retention subsystem is experimental.
  - Boot mode retention module has been added which allows for setting/checking
    the boot mode of an application, initial support has also been added to
    MCUboot to allow for applications to use this as an entrance method for
    MCUboot serial recovery mode. See [boot mode API](../services/retention/index.md#boot-mode-api) for
    details.
- RTIO

  - Added policy that every `sqe` will generate a `cqe` (previously an RTIO\_SQE\_TRANSACTION
    entry would only trigger a `cqe` on the last `sqe` in the transaction.
- Power management

  - Added a new policy event API that can be used to register expected events
    that will wake the system up in the future. This can be used to influence
    the system on which low power states can be used.
  - Added a new device tree property `zephyr,pm-device-runtime-auto` to
    automatically enable device runtime power management on a device after its
    initialization.

## HALs

- Nordic

  - Updated nrfx to version 3.0.0.
- STM32

  - stm32cube: updated STM32F0 to cube version V1.11.4.
  - stm32cube: updated STM32F3 to cube version V1.11.4
  - stm32cube: updated STM32L0 to cube version V1.12.2
  - stm32cube: updated STM32U5 to cube version V1.2.0
  - stm32cube: updated STM32WB to cube version V1.16.0
- Raspberry Pi Pico

  - Updated hal\_rpi\_pico to version 1.5.0

## MCUboot

- Relocated the MCUboot Kconfig options from the main `Kconfig.zephyr` file to
  a new `modules/Kconfig.mcuboot` module-specific file. This means that, for
  interactive Kconfig interfaces, the MCUboot options will now be located under
  `Modules` instead of under `Boot Options`.
- Added [`CONFIG_MCUBOOT_CMAKE_WEST_SIGN_PARAMS`](../kconfig.md#CONFIG_MCUBOOT_CMAKE_WEST_SIGN_PARAMS "CONFIG_MCUBOOT_CMAKE_WEST_SIGN_PARAMS") that allows to pass arguments to
  west sign when invoked from cmake.

## Storage

- Added [`CONFIG_FLASH_MAP_LABELS`](../kconfig.md#CONFIG_FLASH_MAP_LABELS "CONFIG_FLASH_MAP_LABELS"), which will enable runtime access to the labels
  property of fixed partitions. This option is implied if kconfig:option:CONFIG\_FLASH\_MAP\_SHELL
  is enabled. These labels will be displayed in a separate column when using the `flash_map list`
  shell command.

## Trusted Firmware-M

- Enable routing of PSA Crypto API calls from NS to S, thanks to separating MbedTLS into three
  distinct libraries at build time (crypto, TLS, X.509). This also resolves header conflicts with
  earlier integrations of TF-M and MbedTLS.
- Added psa\_crypto sample back.

## zcbor

Updated from 0.6.0 to 0.7.0.
Among other things, this update brings:

- C++ improvements
- float16 support
- Improved docs
- -Wall and -Wconversion compliance

## Tests and Samples

- Two Babblesim based networking (802.15.4) tests have been added, which are run in Zephyr’s CI
  system. One of them including the OpenThread stack.
- For native\_posix and the nrf52\_bsim: Many tests have been fixed and enabled.
- LittleFS sample has been given SPI example configuration for nrf52840dk\_nrf52840.
- Migrated all tests to new Ztest API and deprecated legacy Ztest.
