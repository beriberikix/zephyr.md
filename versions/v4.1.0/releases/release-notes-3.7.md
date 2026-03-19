---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/releases/release-notes-3.7.html
original_path: releases/release-notes-3.7.html
---

# Zephyr 3.7.0

We are pleased to announce the release of Zephyr version 3.7.0.

This release is the last non-maintenance 3.x release and, as such, will be the next
[Long Term Support (LTS) release](../project/release_process.md#release-process-lts).

Major enhancements with this release include:

- A new, completely [overhauled hardware model](../hardware/porting/board_porting.md#hw-model-v2) has been introduced.
  It changes the way both SoCs and boards are named, defined and constructed in Zephyr.
  Additional information can be found in the [Board Porting Guide](../hardware/porting/board_porting.md#board-porting-guide).
- A long-awaited [HTTP Server](../connectivity/networking/api/http_server.md#http-server-interface) library, and associated service API,
  allow to easily implement HTTP/1.1 and HTTP/2 servers in Zephyr. Resources can be registered
  statically or dynamically, and WebSocket support is included.
- [POSIX support](../services/portability/posix/index.md#posix-support) has been extended, with most Options of the IEEE 1003-2017
  [System Interfaces](../services/portability/posix/conformance/index.md#posix-system-interfaces-required) receiving support, as well as most
  Options and Option groups required for [PSE51](../services/portability/posix/aep/index.md#posix-aep-pse51),
  [PSE52](../services/portability/posix/aep/index.md#posix-aep-pse52), and [PSE53](../services/portability/posix/aep/index.md#posix-aep-pse53).
- Bluetooth Host has been extended with support for the Nordic UART Service (NUS), Hands-free Audio
  Gateway (AG), Advanced Audio Distribution Profile (A2DP), and Audio/Video Distribution Transport
  Protocol (AVDTP).
- Sensor abstraction model has been overhauled to adopt a
  [read-then-decode approach](../hardware/peripherals/sensor/read_and_decode.md#sensor-read-and-decode) that enables more types of sensors and
  data flows than the previous fetch/get APIs.
- A new [LLEXT Extension Developer Kit (EDK)](../services/llext/build.md#llext-build-edk) makes it easier to develop and
  integrate custom extensions into Zephyr, including outside of the Zephyr tree.
- [Native simulator](../boards/native/native_sim/doc/index.md#native-sim) now supports leveraging the native host networking stack
  without having to rely on a complex setup of the host environment.
- Trusted Firmware-M (TF-M) 2.1.0 and Mbed TLS 3.6.0 have been integrated into Zephyr.
  Both of these versions are LTS releases. What’s more, [PSA Crypto](../services/crypto/psa_crypto.md#psa-crypto) has been adopted as a replacement
  for TinyCrypt and provides enhanced security and performance.
- A new experimental implementation of the [Precision Time Protocol](../connectivity/networking/api/ptp.md#ptp-interface) (PTP, IEEE
  1588) allows to synchronize time across devices with sub-microsecond accuracy.
- New documentation pages have been introduced to help developers setup their local development
  environment for [Visual Studio Code](../develop/tools/vscode.md#vscode-ide) and [CLion](../develop/tools/clion.md#clion-ide).

An overview of the changes required or recommended when migrating your application from Zephyr
v3.6.0 to Zephyr v3.7.0 can be found in the separate [migration guide](migration-guide-3.7.md#migration-3-7).

While you may refer to release notes from previous 3.x releases for a full change log, other major
enhancements and changes since previous LTS release, Zephyr 2.7.0, include:

- Added support for Picolibc as the new default C library.
- Added support for the following types of hardware peripherals:

  - 1-Wire
  - Battery Charger
  - Cellular Modem
  - Fuel Gauge
  - GNSS
  - Hardware Spinlock
  - I3C
  - RTC (Real Time Clock)
  - SMBus
- Added support for snippets. Snippets are common configuration settings that can be used across
  platforms.
- Added support for Linkable Loadable Extensions (LLEXT).
- Summary of breaking changes (refer to release notes and migration guides from previous release
  notes for more details):

  - All Zephyr public headers have been moved to `include/zephyr`, meaning they need to be
    prefixed with `<zephyr/...>` when included.
  - Pinmux API has been removed. Pin control needs to be used as its replacement, refer to
    [Pin Control](../hardware/pinctrl/index.md#pinctrl-guide) for more details.
  - The following deprecated or experimental features have been removed:

    - 6LoCAN
    - civetweb module. See Zephyr 3.7’s new [HTTP Server](../connectivity/networking/api/http_server.md#http-server-interface) as a replacement.
    - tinycbor module. You may use zcbor as a replacement.

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

- CVE-2024-3077 [Zephyr project bug tracker GHSA-gmfv-4vfh-2mh8](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-gmfv-4vfh-2mh8)
- CVE-2024-3332 [Zephyr project bug tracker GHSA-jmr9-xw2v-5vf4](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-jmr9-xw2v-5vf4)
- CVE-2024-4785: Under embargo until 2024-08-07
- CVE-2024-5754: Under embargo until 2024-09-04
- CVE-2024-5931: Under embargo until 2024-09-10
- CVE-2024-6135: Under embargo until 2024-09-11
- CVE-2024-6137: Under embargo until 2024-09-11
- CVE-2024-6258: Under embargo until 2024-09-05
- CVE-2024-6259: Under embargo until 2024-09-12
- CVE-2024-6442: Under embargo until 2024-09-22
- CVE-2024-6443: Under embargo until 2024-09-22
- CVE-2024-6444: Under embargo until 2024-09-22

## API Changes

### Removed APIs in this release

> - The Bluetooth subsystem specific debug symbols are removed. They have been replaced with the
>   Zephyr logging ones.
> - Removed deprecated `pcie_probe` and `pcie_bdf_lookup` functions from the PCIe APIs.
> - Removed deprecated `CONFIG_EMUL_EEPROM_AT2X` Kconfig option.
> - Removed `pm_device_state_lock`, `pm_device_state_is_locked` and `pm_device_state_unlock`
>   functions from the Device PM APIs.
> - Removed deprecated MCUmgr transport API functions: `zephyr_smp_rx_req`,
>   `zephyr_smp_alloc_rsp` and `zephyr_smp_free_buf`.

### Deprecated in this release

> - Bluetooth advertiser options `BT_LE_ADV_OPT_USE_NAME` and
>   `BT_LE_ADV_OPT_FORCE_NAME_IN_AD` are now deprecated. That means the following macro are
>   deprecated:
>
>   > - [`BT_LE_ADV_CONN_NAME`](../doxygen/html/group__bt__gap.md#ga7b29dba3d892186897c5b4ca5adfd2e3)
>   > - [`BT_LE_ADV_CONN_NAME_AD`](../doxygen/html/group__bt__gap.md#ga213307090f1debdc783c54faf4a36740)
>   > - [`BT_LE_ADV_NCONN_NAME`](../doxygen/html/group__bt__gap.md#gac1c3c47e3136ce813bb50b00a9387cb4)
>   > - [`BT_LE_EXT_ADV_CONN_NAME`](../doxygen/html/group__bt__gap.md#gac4880197cbe21aad78c4edf10cde95da)
>   > - [`BT_LE_EXT_ADV_SCAN_NAME`](../doxygen/html/group__bt__gap.md#ga3e4abd3691e2c6d95acd21b9ca566edd)
>   > - [`BT_LE_EXT_ADV_NCONN_NAME`](../doxygen/html/group__bt__gap.md#ga5c79af6787ccda890f485a45c931cdc8)
>   > - [`BT_LE_EXT_ADV_CODED_NCONN_NAME`](../doxygen/html/group__bt__gap.md#ga8c6027f7c0888c577f9b61a65104be05)
>
>   Application developers will now need to set the advertised name themselves by updating the
>   advertising data or the scan response data.

- CAN

  - Deprecated the `can_calc_prescaler()` API function, as it allows for bitrate
    errors. Bitrate errors between nodes on the same network leads to them drifting apart after the
    start-of-frame (SOF) synchronization has taken place, leading to bus errors.
  - Deprecated the `can_get_min_bitrate()` and `can_get_max_bitrate()` API functions in
    favor of [`can_get_bitrate_min()`](../doxygen/html/group__can__interface.md#ga343456749eec6144a91bacae0d94b114) and [`can_get_bitrate_max()`](../doxygen/html/group__can__interface.md#ga1e6dc8026e4d922bce4d398d9f32a457).
  - Deprecated the `CAN_MAX_STD_ID` and `CAN_MAX_EXT_ID` macros in favor of
    [`CAN_STD_ID_MASK`](../doxygen/html/group__can__interface.md#ga4cd8ce34887b90baeeaa6a4aa048b398) and [`CAN_EXT_ID_MASK`](../doxygen/html/group__can__interface.md#ga15ee71e8abcf51008925585049125986).
- PM

  - Deprecated `CONFIG_PM_DEVICE_RUNTIME_EXCLUSIVE`. Similar behavior can be achieved
    using [`CONFIG_PM_DEVICE_SYSTEM_MANAGED`](../kconfig.md#CONFIG_PM_DEVICE_SYSTEM_MANAGED "CONFIG_PM_DEVICE_SYSTEM_MANAGED").

- POSIX API

  - Deprecated `PTHREAD_BARRIER_DEFINE` has been removed.
  - Deprecated `EFD_IN_USE` and `EFD_FLAGS_SET` have been removed.
  - In efforts to use Kconfig options that map directly to the Options and Option Groups in
    IEEE 1003.1-2017, the following Kconfig options have been deprecated (replaced by):

    - [`CONFIG_EVENTFD_MAX`](../kconfig.md#CONFIG_EVENTFD_MAX "CONFIG_EVENTFD_MAX") ([`CONFIG_ZVFS_EVENTFD_MAX`](../kconfig.md#CONFIG_ZVFS_EVENTFD_MAX "CONFIG_ZVFS_EVENTFD_MAX"))
    - [`CONFIG_FNMATCH`](../kconfig.md#CONFIG_FNMATCH "CONFIG_FNMATCH") ([`CONFIG_POSIX_C_LIB_EXT`](../kconfig.md#CONFIG_POSIX_C_LIB_EXT "CONFIG_POSIX_C_LIB_EXT"))
    - [`CONFIG_GETOPT`](../kconfig.md#CONFIG_GETOPT "CONFIG_GETOPT") ([`CONFIG_POSIX_C_LIB_EXT`](../kconfig.md#CONFIG_POSIX_C_LIB_EXT "CONFIG_POSIX_C_LIB_EXT"))
    - [`CONFIG_MAX_PTHREAD_COUNT`](../kconfig.md#CONFIG_MAX_PTHREAD_COUNT "CONFIG_MAX_PTHREAD_COUNT") ([`CONFIG_POSIX_THREAD_THREADS_MAX`](../kconfig.md#CONFIG_POSIX_THREAD_THREADS_MAX "CONFIG_POSIX_THREAD_THREADS_MAX"))
    - [`CONFIG_MAX_PTHREAD_KEY_COUNT`](../kconfig.md#CONFIG_MAX_PTHREAD_KEY_COUNT "CONFIG_MAX_PTHREAD_KEY_COUNT") ([`CONFIG_POSIX_THREAD_KEYS_MAX`](../kconfig.md#CONFIG_POSIX_THREAD_KEYS_MAX "CONFIG_POSIX_THREAD_KEYS_MAX"))
    - [`CONFIG_MAX_TIMER_COUNT`](../kconfig.md#CONFIG_MAX_TIMER_COUNT "CONFIG_MAX_TIMER_COUNT") ([`CONFIG_POSIX_TIMER_MAX`](../kconfig.md#CONFIG_POSIX_TIMER_MAX "CONFIG_POSIX_TIMER_MAX"))
    - [`CONFIG_POSIX_LIMITS_RTSIG_MAX`](../kconfig.md#CONFIG_POSIX_LIMITS_RTSIG_MAX "CONFIG_POSIX_LIMITS_RTSIG_MAX") ([`CONFIG_POSIX_RTSIG_MAX`](../kconfig.md#CONFIG_POSIX_RTSIG_MAX "CONFIG_POSIX_RTSIG_MAX"))
    - [`CONFIG_POSIX_CLOCK`](../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") ([`CONFIG_POSIX_CLOCK_SELECTION`](../kconfig.md#CONFIG_POSIX_CLOCK_SELECTION "CONFIG_POSIX_CLOCK_SELECTION"),
      [`CONFIG_POSIX_CPUTIME`](../kconfig.md#CONFIG_POSIX_CPUTIME "CONFIG_POSIX_CPUTIME"), [`CONFIG_POSIX_MONOTONIC_CLOCK`](../kconfig.md#CONFIG_POSIX_MONOTONIC_CLOCK "CONFIG_POSIX_MONOTONIC_CLOCK"),
      [`CONFIG_POSIX_TIMERS`](../kconfig.md#CONFIG_POSIX_TIMERS "CONFIG_POSIX_TIMERS"), and [`CONFIG_POSIX_TIMEOUTS`](../kconfig.md#CONFIG_POSIX_TIMEOUTS "CONFIG_POSIX_TIMEOUTS"))
    - [`CONFIG_POSIX_FS`](../kconfig.md#CONFIG_POSIX_FS "CONFIG_POSIX_FS") ([`CONFIG_POSIX_FILE_SYSTEM`](../kconfig.md#CONFIG_POSIX_FILE_SYSTEM "CONFIG_POSIX_FILE_SYSTEM"))
    - [`CONFIG_POSIX_MAX_FDS`](../kconfig.md#CONFIG_POSIX_MAX_FDS "CONFIG_POSIX_MAX_FDS") ([`CONFIG_POSIX_OPEN_MAX`](../kconfig.md#CONFIG_POSIX_OPEN_MAX "CONFIG_POSIX_OPEN_MAX") and
      [`CONFIG_ZVFS_OPEN_MAX`](../kconfig.md#CONFIG_ZVFS_OPEN_MAX "CONFIG_ZVFS_OPEN_MAX"))
    - [`CONFIG_POSIX_MAX_OPEN_FILES`](../kconfig.md#CONFIG_POSIX_MAX_OPEN_FILES "CONFIG_POSIX_MAX_OPEN_FILES") ([`CONFIG_POSIX_OPEN_MAX`](../kconfig.md#CONFIG_POSIX_OPEN_MAX "CONFIG_POSIX_OPEN_MAX") and
      [`CONFIG_ZVFS_OPEN_MAX`](../kconfig.md#CONFIG_ZVFS_OPEN_MAX "CONFIG_ZVFS_OPEN_MAX"))
    - [`CONFIG_POSIX_MQUEUE`](../kconfig.md#CONFIG_POSIX_MQUEUE "CONFIG_POSIX_MQUEUE") ([`CONFIG_POSIX_MESSAGE_PASSING`](../kconfig.md#CONFIG_POSIX_MESSAGE_PASSING "CONFIG_POSIX_MESSAGE_PASSING"))
    - [`CONFIG_POSIX_PUTMSG`](../kconfig.md#CONFIG_POSIX_PUTMSG "CONFIG_POSIX_PUTMSG") ([`CONFIG_XOPEN_STREAMS`](../kconfig.md#CONFIG_XOPEN_STREAMS "CONFIG_XOPEN_STREAMS"))
    - [`CONFIG_POSIX_SIGNAL`](../kconfig.md#CONFIG_POSIX_SIGNAL "CONFIG_POSIX_SIGNAL") ([`CONFIG_POSIX_SIGNALS`](../kconfig.md#CONFIG_POSIX_SIGNALS "CONFIG_POSIX_SIGNALS"))
    - [`CONFIG_POSIX_SYSCONF`](../kconfig.md#CONFIG_POSIX_SYSCONF "CONFIG_POSIX_SYSCONF") ([`CONFIG_POSIX_SINGLE_PROCESS`](../kconfig.md#CONFIG_POSIX_SINGLE_PROCESS "CONFIG_POSIX_SINGLE_PROCESS"))
    - [`CONFIG_POSIX_UNAME`](../kconfig.md#CONFIG_POSIX_UNAME "CONFIG_POSIX_UNAME") ([`CONFIG_POSIX_SINGLE_PROCESS`](../kconfig.md#CONFIG_POSIX_SINGLE_PROCESS "CONFIG_POSIX_SINGLE_PROCESS"))
    - [`CONFIG_PTHREAD`](../kconfig.md#CONFIG_PTHREAD "CONFIG_PTHREAD") ([`CONFIG_POSIX_THREADS`](../kconfig.md#CONFIG_POSIX_THREADS "CONFIG_POSIX_THREADS"))
    - [`CONFIG_PTHREAD_BARRIER`](../kconfig.md#CONFIG_PTHREAD_BARRIER "CONFIG_PTHREAD_BARRIER") ([`CONFIG_POSIX_BARRIERS`](../kconfig.md#CONFIG_POSIX_BARRIERS "CONFIG_POSIX_BARRIERS"))
    - [`CONFIG_PTHREAD_COND`](../kconfig.md#CONFIG_PTHREAD_COND "CONFIG_PTHREAD_COND") ([`CONFIG_POSIX_THREADS`](../kconfig.md#CONFIG_POSIX_THREADS "CONFIG_POSIX_THREADS"))
    - [`CONFIG_PTHREAD_IPC`](../kconfig.md#CONFIG_PTHREAD_IPC "CONFIG_PTHREAD_IPC") ([`CONFIG_POSIX_THREADS`](../kconfig.md#CONFIG_POSIX_THREADS "CONFIG_POSIX_THREADS"))
    - [`CONFIG_PTHREAD_KEY`](../kconfig.md#CONFIG_PTHREAD_KEY "CONFIG_PTHREAD_KEY") ([`CONFIG_POSIX_THREADS`](../kconfig.md#CONFIG_POSIX_THREADS "CONFIG_POSIX_THREADS"))
    - [`CONFIG_PTHREAD_MUTEX`](../kconfig.md#CONFIG_PTHREAD_MUTEX "CONFIG_PTHREAD_MUTEX") ([`CONFIG_POSIX_THREADS`](../kconfig.md#CONFIG_POSIX_THREADS "CONFIG_POSIX_THREADS"))
    - [`CONFIG_PTHREAD_RWLOCK`](../kconfig.md#CONFIG_PTHREAD_RWLOCK "CONFIG_PTHREAD_RWLOCK") ([`CONFIG_POSIX_READER_WRITER_LOCKS`](../kconfig.md#CONFIG_POSIX_READER_WRITER_LOCKS "CONFIG_POSIX_READER_WRITER_LOCKS"))
    - [`CONFIG_PTHREAD_SPINLOCK`](../kconfig.md#CONFIG_PTHREAD_SPINLOCK "CONFIG_PTHREAD_SPINLOCK") ([`CONFIG_POSIX_SPIN_LOCKS`](../kconfig.md#CONFIG_POSIX_SPIN_LOCKS "CONFIG_POSIX_SPIN_LOCKS"))
    - [`CONFIG_SEM_NAMELEN_MAX`](../kconfig.md#CONFIG_SEM_NAMELEN_MAX "CONFIG_SEM_NAMELEN_MAX") ([`CONFIG_POSIX_SEM_NAMELEN_MAX`](../kconfig.md#CONFIG_POSIX_SEM_NAMELEN_MAX "CONFIG_POSIX_SEM_NAMELEN_MAX"))
    - [`CONFIG_SEM_VALUE_MAX`](../kconfig.md#CONFIG_SEM_VALUE_MAX "CONFIG_SEM_VALUE_MAX") ([`CONFIG_POSIX_SEM_VALUE_MAX`](../kconfig.md#CONFIG_POSIX_SEM_VALUE_MAX "CONFIG_POSIX_SEM_VALUE_MAX"))
    - [`CONFIG_TIMER`](../kconfig.md#CONFIG_TIMER "CONFIG_TIMER") ([`CONFIG_POSIX_TIMERS`](../kconfig.md#CONFIG_POSIX_TIMERS "CONFIG_POSIX_TIMERS"))
    - [`CONFIG_TIMER_DELAYTIMER_MAX`](../kconfig.md#CONFIG_TIMER_DELAYTIMER_MAX "CONFIG_TIMER_DELAYTIMER_MAX") ([`CONFIG_POSIX_DELAYTIMER_MAX`](../kconfig.md#CONFIG_POSIX_DELAYTIMER_MAX "CONFIG_POSIX_DELAYTIMER_MAX"))

    Please see the [POSIX API migration guide](migration-guide-3.7.md#zephyr-3-7-posix-api-migration).

> - SPI
>
> > - Deprecated `spi_is_ready()` API function has been removed.
> > - Deprecated `spi_transceive_async()` API function has been removed.
> > - Deprecated `spi_read_async()` API function has been removed.
> > - Deprecated `spi_write_async()` API function has been removed.

## Architectures

- ARC

  - Added ARC MWDT toolchain support for ARC-V targets
  - Added HW memory barrier API support for multicore targets
  - Enabled TLS by default if C++ is used in case of ARC MWDT toolchain
  - Fixed the issue when mbedtls failed to build with ARC MWDT toolchain & minimal LibC due to
    incorrect define which mark support of bounds-checking interfaces C library extension
  - Fixed device deferred initialization in case of ARC MWDT toolchain
- ARM

  - Added initial support for Cortex-M85 Core
- ARM64

  - Implemented symbol names in the backtraces, enable by selecting [`CONFIG_SYMTAB`](../kconfig.md#CONFIG_SYMTAB "CONFIG_SYMTAB")
  - Add compiler tuning for Cortex-R82
- RISC-V

  - The fatal error message triggered from a fault now contains the callee-saved-registers states.
  - Implemented stack unwinding

    - Frame-pointer can be selected to enable precise stack traces at the expense of slightly
      increased size and decreased speed.
    - Symbol names can be enabled by selecting `CONFIG_EXCEPTION_STACK_TRACE_SYMTAB`
- Xtensa

  - Added support to save/restore HiFi AudioEngine registers.
  - Added support to utilize MPU.
  - Added support to automatically generate interrupt handlers.
  - Added support to generate vector table at build time to be included in the linker script.
  - Added kconfig [`CONFIG_XTENSA_BREAK_ON_UNRECOVERABLE_EXCEPTIONS`](../kconfig.md#CONFIG_XTENSA_BREAK_ON_UNRECOVERABLE_EXCEPTIONS "CONFIG_XTENSA_BREAK_ON_UNRECOVERABLE_EXCEPTIONS") to guard
    using break instruction for unrecoverable exceptions. Enabling the break instruction via
    this kconfig may result in an infinite interrupt storm which may hinder debugging efforts.
  - Fixed an issue where passing the 7th argument via syscall was handled incorrectly.
  - Fixed an issue where [`arch_user_string_nlen()`](../doxygen/html/group__arch-userspace.md#ga174c4f356fe315c523cefbf513858c9c) accessing unmapped memory resulted
    in an unrecoverable exception.

## Kernel

> - Added [`k_uptime_seconds()`](../doxygen/html/group__clock__apis.md#gae082928ea608a8b180b4cb3a79d21a24) function to simplify `k_uptime_get() / 1000` usage.
> - Added [`k_realloc()`](../doxygen/html/group__heap__apis.md#ga852a7a60dce5853b6925897b24a54e02), that uses kernel heap to implement traditional [`realloc()`](../doxygen/html/stdlib_8h.md#ad28fed1039f35d754710633141b4edf0)
>   semantics.
> - Devices can now store devicetree metadata such as nodelabels by turning on
>   [`CONFIG_DEVICE_DT_METADATA`](../kconfig.md#CONFIG_DEVICE_DT_METADATA "CONFIG_DEVICE_DT_METADATA"). This option may be useful in
>   e.g. shells as devices can be obtained using human-friendly names thanks to
>   APIs like `device_get_by_dt_nodelabel()`.
> - Any device initialization can be deferred if its associated devicetree node
>   has the special `zephyr,deferred-init` property set. The device can be
>   initialized later in time by using [`device_init()`](../doxygen/html/group__device__model.md#gaeea4f9c9f14ab12d224378ab90231c09).
> - The declaration of statically allocated thread stacks has been updated to utilize
>   [`K_THREAD_STACK_LEN`](../doxygen/html/group__thread__stack__api.md#ga72fa31a9d8e28ccabd6e5e908a24ec00) for both single thread stack declaration and array thread
>   stack declarations. This ensures correct alignment for all thread stacks. For user
>   threads, this may increase the size of the statically allocated stack objects depending
>   on architecture alignment requirements.
> - Fix an edge case deadlock in [`k_thread_abort()`](../doxygen/html/group__thread__apis.md#ga1f44bb0307bea7a97227764ecd7bf963) (and join)
>   where racing ISRs on SMP systems could become stuck spinning to
>   signal each other’s interrupted threads.
> - Fix a bug where [`CONFIG_SCHED_SCALABLE`](../kconfig.md#CONFIG_SCHED_SCALABLE "CONFIG_SCHED_SCALABLE") and
>   [`CONFIG_SCHED_DEADLINE`](../kconfig.md#CONFIG_SCHED_DEADLINE "CONFIG_SCHED_DEADLINE") would corrupt the
>   scheduling queue when used together.

## Bluetooth

- Audio

  - Removed `err` from `bt_bap_broadcast_assistant_cb.recv_state_removed` as it was
    redundant.
  - The broadcast\_audio\_assistant sample has been renamed to bap\_broadcast\_assistant.
    The broadcast\_audio\_sink sample has been renamed to bap\_broadcast\_sink.
    The broadcast\_audio\_source sample has been renamed to bap\_broadcast\_source.
    The unicast\_audio\_client sample has been renamed to bap\_unicast\_client.
    The unicast\_audio\_server sample has been renamed to bap\_unicast\_server.
    The public\_broadcast\_sink sample has been renamed to pbp\_public\_broadcast\_sink.
    The public\_broadcast\_source sample has been renamed to pbp\_public\_broadcast\_source.
  - The CAP Commander and CAP Initiator now no longer require CAS to be discovered for
    `BT_CAP_SET_TYPE_AD_HOC` sets. This allows applications to use these APIs on e.g.
    BAP Unicast Servers that do not implement the CAP Acceptor role.
- Host

  - Added Nordic UART Service (NUS), enabled by the [`CONFIG_BT_ZEPHYR_NUS`](../kconfig.md#CONFIG_BT_ZEPHYR_NUS "CONFIG_BT_ZEPHYR_NUS").
    This Service exposes the ability to declare multiple instances of the GATT service,
    allowing multiple serial endpoints to be used for different purposes.
  - Implemented Hands-free Audio Gateway (AG), enabled by the [`CONFIG_BT_HFP_AG`](../kconfig.md#CONFIG_BT_HFP_AG "CONFIG_BT_HFP_AG").
    It works as a device that is the gateway of the audio. The typical device acting as Audio
    Gateway is a cellular phone. It controls the device (Hands-free Unit), that is the remote
    audio input and output mechanism.
  - Implemented Advanced Audio Distribution Profile (A2DP) and Audio/Video Distribution Transport
    Protocol (AVDTP), A2DP is enabled by [`CONFIG_BT_A2DP`](../kconfig.md#CONFIG_BT_A2DP "CONFIG_BT_A2DP"), AVDTP is enabled
    by [`CONFIG_BT_AVDTP`](../kconfig.md#CONFIG_BT_AVDTP "CONFIG_BT_AVDTP"). They implement the protocols and procedures that
    realize distribution of audio content of high quality in mono, stereo, or multi-channel modes.
    A typical use case is the streaming of music content from a stereo music player to headphones
    or speakers. The audio data is compressed in a proper format for efficient use of the limited
    bandwidth.
  - Reworked the transmission path for data and commands. The “BT TX” thread has been removed, along
    with the buffer pools for HCI fragments and L2CAP segments. All communication with the
    Controller is now exclusively done in the system workqueue context.
  - [`CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER`](../kconfig.md#CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER "CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER") and
    [`CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER`](../kconfig.md#CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER "CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER") now depend on
    `CONFIG_BT_CONN` as they do not work without connections.
  - Improve [`bt_foreach_bond()`](../doxygen/html/group__bt__gap.md#gaad380b7f8984f8522c1b79f9bdc04905) to support Bluetooth Classic key traversal.
- HCI Drivers

  - Completely redesigned HCI driver interface. See the Bluetooth HCI section in
    [Migration guide to Zephyr v3.7.0](migration-guide-3.7.md#migration-3-7) for more information.
  - Added support for Ambiq Apollo3 Blue series.
  - Added support for NXP RW61x.
  - Added support for Infineon CYW208XX.
  - Added support for Renesas SmartBond DA1469x.
  - Removed unmaintained B91 driver.
  - Added support for NXP IW612 on boards mimxrt1170\_evkb and mimxrt1040\_evk.
    It can be enabled by [`CONFIG_BT_NXP_NW612`](../kconfig.md#CONFIG_BT_NXP_NW612 "CONFIG_BT_NXP_NW612").

## Boards & SoC Support

- Added support for these SoC series:

  - Added support for Ambiq Apollo3 Blue and Apollo3 Blue Plus SoC series.
  - Added support for Synopsys ARC-V RMX1xx simulation platform.
  - Added support for STM32H7R/S SoC series.
  - Added support for NXP mke15z7, mke17z7, mke17z9, MCXNx4x, RW61x
  - Added support for Analog Devices MAX32 SoC series.
  - Added support for Infineon Technologies AIROC™ CYW20829 Bluetooth LE SoC series.
  - Added support for MediaTek MT8195 Audio DSPs
  - Added support for Nuvoton Numaker M2L31X SoC series.
  - Added support for the Microchip PolarFire ICICLE Kit SMP variant.
  - Added support for Renesas RA8 series SoC.
- Made these changes in other SoC series:

  - Intel ACE Audio DSP: Use dedicated registers to report boot status instead of arbitrary memory.
  - ITE: Rename the Kconfig symbol for all ITE SoC variants.
  - STM32: Enabled ART Accelerator, I-cache, D-cache and prefetch on compatible series.
  - STM32H5: Added support for Stop mode and [`CONFIG_PM`](../kconfig.md#CONFIG_PM "CONFIG_PM").
  - STM32WL: Decreased Sub-GHz SPI frequency from 12 to 8MHz.
  - STM32C0: Added support for [`CONFIG_POWEROFF`](../kconfig.md#CONFIG_POWEROFF "CONFIG_POWEROFF").
  - STM32U5: Added support for Stop3 mode.
  - Synopsys:

    - nsim: split nsim platform for arc\_classic (ARCv2 and ARCv3 ISA based) and arc\_v (RISC-V ISA based)
    - nsim/nsim\_hs5x/smp: align sys clock frequency with other SMP nSIM configs
  - NXP IMX8M: added resource domain controller support
  - NXP s32k146: set RTC clock source to internal oscillator
  - GD32F4XX: Fixed an incorrect uart4 irq number.
  - Nordic nRF54L: Added support for the FLPR (fast lightweight processor) RISC-V CPU.
  - Espressif: Removed idf-bootloader dependency from all ESP32 SoC variants.
  - Espressif: Added Simple boot support for ESP32 SoC variants, which allows loading application
    using a single binary image without a 2nd stage bootloader.
  - Espressif: Re-worked and optimized all SoCs memory map.
  - LiteX:

    - Added support for `sys_arch_reboot()`.
    - [`CONFIG_RISCV_ISA_EXT_A`](../kconfig.md#CONFIG_RISCV_ISA_EXT_A "CONFIG_RISCV_ISA_EXT_A") is no longer erroneously y-selected.
  - rp2040: The proprietary UART driver has been discontinued and replaced with PL011.
  - Renesas RZ/T2M: Added default values for System Clock Control register.
- Added support for these boards:

  - Added support for [Ambiq Apollo3 Blue board](../boards/ambiq/apollo3_evb/doc/index.md#apollo3_evb): `apollo3_evb`.
  - Added support for [Ambiq Apollo3 Blue Plus board](../boards/ambiq/apollo3p_evb/doc/index.md#apollo3p_evb): `apollo3p_evb`.
  - Added support for [Raspberry Pi 5 board](../boards/raspberrypi/rpi_5/doc/index.md#rpi_5): `rpi_5`.
  - Added support for [Seeed Studio XIAO RP2040 board](../boards/seeed/xiao_rp2040/doc/index.md#xiao_rp2040): `xiao_rp2040`.
  - Added support for [Mikroe RA4M1 Clicker board](../boards/mikroe/clicker_ra4m1/doc/index.md#mikroe_clicker_ra4m1): `mikroe_clicker_ra4m1`.
  - Added support for [Arduino UNO R4 WiFi board](../boards/arduino/uno_r4/doc/index.md#arduino-uno-r4): `arduino_uno_r4_wifi`.
  - Added support for [Renesas EK-RA8M1 board](../boards/renesas/ek_ra8m1/doc/index.md#ek_ra8m1): `ek_ra8m1`.
  - Added support for [ST Nucleo H533RE](../boards/st/nucleo_h533re/doc/index.md#nucleo_h533re): `nucleo_h533re`.
  - Added support for [ST STM32C0116-DK Discovery Kit](../boards/st/stm32c0116_dk/doc/index.md#stm32c0116_dk): `stm32c0116_dk`.
  - Added support for [ST STM32H745I Discovery](../boards/st/stm32h745i_disco/doc/index.md#stm32h745i_disco): `stm32h745i_disco`.
  - Added support for [ST STM32H7S78-DK Discovery](../boards/st/stm32h7s78_dk/doc/index.md#stm32h7s78_dk): `stm32h7s78_dk`.
  - Added support for [ST STM32L152CDISCOVERY board](../boards/st/stm32l1_disco/doc/index.md#stm32l1_disco): `stm32l152c_disco`.
  - Added support for [ST STEVAL STWINBX1 Development kit](../boards/st/steval_stwinbx1/doc/index.md#steval_stwinbx1): `steval_stwinbx1`.
  - Added support for NXP boards: `frdm_mcxn947`, `ke17z512`, `rd_rw612_bga`, `frdm_rw612`, `frdm_ke15z`, `frdm_ke17z`
  - Added support for [Synopsys ARC-V RMX1xx nSIM-based simulation platform](../boards/snps/nsim/arc_v/doc/index.md#nsim_arc_v): `nsim_arc_v/rmx100`.
  - Added support for [Analog Devices MAX32690EVKIT](../boards/adi/max32690evkit/doc/index.md#max32690evkit): `max32690evkit`.
  - Added support for [Analog Devices MAX32680EVKIT](../boards/adi/max32680evkit/doc/index.md#max32680evkit): `max32680evkit`.
  - Added support for [Analog Devices MAX32672EVKIT](../boards/adi/max32672evkit/doc/index.md#max32672evkit): `max32672evkit`.
  - Added support for [Analog Devices MAX32672FTHR](../boards/adi/max32672fthr/doc/index.md#max32672fthr): `max32672fthr`.
  - Added support for [Analog Devices MAX32670EVKIT](../boards/adi/max32670evkit/doc/index.md#max32670evkit): `max32670evkit`.
  - Added support for [Analog Devices MAX32655EVKIT](../boards/adi/max32655evkit/doc/index.md#max32655evkit): `max32655evkit`.
  - Added support for [Analog Devices MAX32655FTHR](../boards/adi/max32655fthr/doc/index.md#max32655fthr): `max32655fthr`.
  - Added support for [Analog Devices AD-APARD32690-SL](../boards/adi/apard32690/doc/index.md#apard32690): `ad_apard32690_sl`.
  - Added support for [Infineon Technologies CYW920829M2EVK-02](../boards/infineon/cyw920829m2evk_02/doc/index.md#cyw920829m2evk_02): `cyw920829m2evk_02`.
  - Added support for [Nuvoton Numaker M2L31KI board](../boards/nuvoton/numaker_m2l31ki/doc/index.md#numaker_m2l31ki): `numaker_m2l31ki`.
  - Added support for [Espressif ESP32-S2 DevKit-C](../boards/espressif/esp32s2_devkitc/doc/index.md#esp32s2_devkitc): `esp32s2_devkitc`.
  - Added support for [Espressif ESP32-S3 DevKit-C](../boards/espressif/esp32s3_devkitc/doc/index.md#esp32s3_devkitc): `esp32s3_devkitc`.
  - Added support for [Espressif ESP32-C6 DevKit-C](../boards/espressif/esp32c6_devkitc/doc/index.md#esp32c6_devkitc): `esp32c6_devkitc`.
  - Added support for [Waveshare ESP32-S3-Touch-LCD-1.28](../boards/waveshare/esp32s3_touch_lcd_1_28/doc/index.md#esp32s3_touch_lcd_1_28): `esp32s3_touch_lcd_1_28`.
  - Added support for [M5Stack ATOM Lite](../boards/m5stack/m5stack_atom_lite/doc/index.md#m5stack_atom_lite): `m5stack_atom_lite`.
  - Added support for [CTHINGS.CO Connectivity Card nRF52840](../boards/ct/ctcc/doc/index.md#ctcc): `ctcc`.
- Made these board changes:

  - On [ST STM32H7B3I Discovery Kit](../boards/st/stm32h7b3i_dk/doc/index.md#stm32h7b3i_dk): `stm32h7b3i_dk`,
    enabled full cache management, Chrom-ART, double frame buffer and full refresh for
    optimal LVGL performance.
  - On ST STM32 boards, stm32cubeprogrammer runner can now be used to program external
    flash using `--extload` option.
  - Add HEX file support for Linkserver to all NXP boards
  - Updated the Linkserver west runner to reflect changes to the CLI of LinkServer v1.5.xx
  - Add LinkServer support to NXP `mimxrt1010_evk`, `mimxrt1160_evk`, `frdm_rw612`, `rd_rw612_bga`, `frdm_mcxn947`
  - Introduced the simulated [nrf54l15bsim](../boards/native/nrf_bsim/doc/nrf54l15bsim.md#nrf54l15bsim) target.
  - The nrf5x bsim targets now support BT LE Coded PHY.
  - LLVM fuzzing support has been refactored while adding support for it in native\_sim.
  - nRF54H20 PDK (pre-release) converted to [nRF54H20 DK](../boards/nordic/nrf54h20dk/doc/index.md#nrf54h20dk-nrf54h20)
  - PPR core target in [nRF54H20 DK](../boards/nordic/nrf54h20dk/doc/index.md#nrf54h20dk-nrf54h20) runs from RAM by default. A
    new `xip` variant has been introduced which runs from MRAM (XIP).
  - Refactored [BeagleConnect Freedom](../boards/beagle/beagleconnect_freedom/doc/index.md#beagleconnect_freedom) external antenna switch handling.
  - Added Arduino dts node labels for the nRF5340 Audio DK.
  - Changed the default revision of the nRF54L15 PDK from 0.2.1 to 0.3.0.
  - In boards based on the nRF5340 SoC, replaced direct accesses to the register
    that controls the network core Force-OFF signal with a module that uses an
    on-off manager to keep track of the network core use and exposes its API
    in `<nrf53_cpunet_mgmt.h>`.
  - Laird Connectivity boards are rebranded to Ezurio.
- Added support for the following shields:

  - [Adafruit 2.8” TFT Touch Shield v2](../boards/shields/adafruit_2_8_tft_touch_v2/doc/index.md#adafruit-2-8-tft-touch-v2) (`adafruit_2_8_tft_touch_v2`)
  - [Adafruit 5x5 NeoPixel Grid BFF](../boards/shields/adafruit_neopixel_grid_bff/doc/index.md#adafruit-neopixel-grid-bff) (`adafruit_neopixel_grid_bff`)
  - [Arduino UNO click shield](../boards/shields/arduino_uno_click/doc/index.md#arduino-uno-click) (`arduino_uno_click`)
  - [DVP FPC-24 MT9M114 Camera Module](../boards/shields/dvp_fpc24_mt9m114/doc/index.md#dvp-fpc24-mt9m114) (`dvp_fpc24_mt9m114`)
  - [NXP LCD\_PAR\_S035 TFT LCD Module](../boards/shields/lcd_par_s035/doc/index.md#lcd-par-s035) (`lcd_par_s035`)
  - [MikroElektronika Weather Click](../boards/shields/mikroe_weather_click/doc/index.md#mikroe-weather-click) (`mikroe_weather_click`)
  - [NXP BTB-44 OV5640 Camera Module](../boards/shields/nxp_btb44_ov5640/doc/index.md#nxp-btb44-ov5640) (`nxp_btb44_ov5640`)
  - [Reyax LoRa RYLR896 and RYLR915 Modules](../boards/shields/reyax_lora/doc/index.md#reyax-lora) (`reyax_lora`)
  - [NXP RK043FN02H-CT Parallel Display](../boards/shields/rk043fn02h_ct/doc/index.md#rk043fn02h-ct) (`rk043fn02h_ct`)
  - [NXP RK043FN66HS-CTG Parallel Display](../boards/shields/rk043fn66hs_ctg/doc/index.md#rk043fn66hs-ctg) (`rk043fn66hs_ctg`)
  - [RaspberryPi Pico to UNO FlexyPin Adapter](../boards/shields/rpi_pico_uno_flexypin/doc/index.md#rpi-pico-uno-flexypin) (`rpi_pico_uno_flexypin`)
  - [Seeed Studio XIAO Expansion Board](../boards/shields/seeed_xiao_expansion_board/doc/index.md#seeed-xiao-expansion-board) (`seeed_xiao_expansion_board`)
  - [Seeed Studio XIAO Round Display](../boards/shields/seeed_xiao_round_display/doc/index.md#seeed-xiao-round-display) (`seeed_xiao_round_display`)
  - [Sparkfun SparkFun MicroMod Asset Tracker Shield](../boards/shields/sparkfun_carrier_asset_tracker/doc/index.md#sparkfun-carrier-asset-tracker) (`sparkfun_carrier_asset_tracker`)
  - [ST B-LCD40-DSI1](../boards/shields/st_b_lcd40_dsi1_mb1166/doc/index.md#st-b-lcd40-dsi1-mb1166) (`st_b_lcd40_dsi1_mb1166`)
  - [WAVESHARE e-Paper Raw Panel Shield](../boards/shields/waveshare_epaper/doc/index.md#waveshare-epaper) (`waveshare_epaper`)
  - [X-NUCLEO-BNRG2A1: BLE expansion board](../boards/shields/x_nucleo_bnrg2a1/doc/index.md#x-nucleo-bnrg2a1) (`x_nucleo_bnrg2a1`)

## Build system and Infrastructure

> - CI-enabled blackbox tests were added to verify the correctness of most Twister flags.
> - A `socs` folder for applications has been introduced that allows for Kconfig fragments and
>   devicetree overlays that should apply to any board target using a particular SoC and board
>   qualifier ([GitHub #70418](https://github.com/zephyrproject-rtos/zephyr/issues/70418)). Support has also been added to sysbuild ([GitHub #71320](https://github.com/zephyrproject-rtos/zephyr/issues/71320)).
> - [Board/SoC flashing configuration](../build/flashing/configuration.md#flashing-soc-board-config) settings have been added
>   ([GitHub #69748](https://github.com/zephyrproject-rtos/zephyr/issues/69748)).
> - Deprecated the global CSTD cmake property in favor of the [`CONFIG_STD_C`](../kconfig.md#CONFIG_STD_C "CONFIG_STD_C")
>   choice to select the C Standard version. Additionally, subsystems can select a minimum
>   required C Standard version, with, for example, [`CONFIG_REQUIRES_STD_C11`](../kconfig.md#CONFIG_REQUIRES_STD_C11 "CONFIG_REQUIRES_STD_C11").
> - Fixed issue with passing UTF-8 configs to applications using sysbuild ([GitHub #74152](https://github.com/zephyrproject-rtos/zephyr/issues/74152)).
> - Fixed issue whereby domain file in sysbuild projects would be loaded and used with outdated
>   information if sysbuild configuration was changed, and `west flash` was ran directly after
>   ([GitHub #73864](https://github.com/zephyrproject-rtos/zephyr/issues/73864)).
> - Fixed issue with Zephyr modules not being listed in sysbuild if they did not have a Kconfig
>   file set ([GitHub #72070](https://github.com/zephyrproject-rtos/zephyr/issues/72070)).
> - Added sysbuild `SB_CONFIG_COMPILER_WARNINGS_AS_ERRORS` Kconfig option to turn on
>   “warning as error” toolchain flags for all images, if set ([GitHub #70217](https://github.com/zephyrproject-rtos/zephyr/issues/70217)).
> - Fixed issue whereby files used in a project (e.g. devicetree overlays or Kconfig fragments)
>   were not correctly watched and CMake would not reconfigure if they were changed
>   ([GitHub #74655](https://github.com/zephyrproject-rtos/zephyr/issues/74655)).
> - Added flash support for Intel Hex files for the LinkServer runner.
> - Added sysbuild `sysbuild/CMakeLists.txt` entry point and added support for
>   `APPLICATION_CONFIG_DIR` which allows for adjusting how sysbuild functions ([GitHub #72923](https://github.com/zephyrproject-rtos/zephyr/issues/72923)).
> - Fixed issue with armfvp find path if it contained a colon-separated list ([GitHub #74868](https://github.com/zephyrproject-rtos/zephyr/issues/74868)).
> - Fixed issue with version.cmake field sizes not being enforced ([GitHub #74357](https://github.com/zephyrproject-rtos/zephyr/issues/74357)).
> - Fixed issue with sysbuild not clearing `EXTRA_CONF_FILE` before processing images which
>   prevented this option being passed on to the image ([GitHub #74082](https://github.com/zephyrproject-rtos/zephyr/issues/74082)).
> - Added sysbuild root support which works similarly to the existing root module, adjusting paths
>   relative to `APP_DIR` ([GitHub #73390](https://github.com/zephyrproject-rtos/zephyr/issues/73390)).
> - Added warning/error message for blobs that are missing ([GitHub #73051](https://github.com/zephyrproject-rtos/zephyr/issues/73051)).
> - Fixed issue with correct python executable detection on some systems ([GitHub #72232](https://github.com/zephyrproject-rtos/zephyr/issues/72232)).
> - Added support for enabling LTO for whole application ([GitHub #69519](https://github.com/zephyrproject-rtos/zephyr/issues/69519)).
> - Fixed `FILE_SUFFIX` issues relating to double application of suffixes, non-application in
>   sysbuild and variable name clashes in CMake functions ([GitHub #70124](https://github.com/zephyrproject-rtos/zephyr/issues/70124), [GitHub #71280](https://github.com/zephyrproject-rtos/zephyr/issues/71280)).
> - Added support for new aggressive size optimisation flag (for GCC and Clang) using
>   [`CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE`](../kconfig.md#CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE "CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE") ([GitHub #70511](https://github.com/zephyrproject-rtos/zephyr/issues/70511)).
> - Fixed issue with printing out `BUILD_VERSION` if it was empty ([GitHub #70970](https://github.com/zephyrproject-rtos/zephyr/issues/70970)).
> - Fixed sysbuild issue of `sysbuild_cache_set()` cmake function wrongly detecting partial
>   matches for de-duplication ([GitHub #71381](https://github.com/zephyrproject-rtos/zephyr/issues/71381)).
> - Fixed issue with detecting wrong `VERSION` file ([GitHub #71385](https://github.com/zephyrproject-rtos/zephyr/issues/71385)).
> - Added support for disabling output disassembly having the source code in using
>   [`CONFIG_OUTPUT_DISASSEMBLY_WITH_SOURCE`](../kconfig.md#CONFIG_OUTPUT_DISASSEMBLY_WITH_SOURCE "CONFIG_OUTPUT_DISASSEMBLY_WITH_SOURCE") ([GitHub #71535](https://github.com/zephyrproject-rtos/zephyr/issues/71535)).
> - Twister now supports `--flash-before` parameter that allows flashing DUT before
>   opening serial port ([GitHub #47037](https://github.com/zephyrproject-rtos/zephyr/issues/47037)).

## Drivers and Sensors

- ADC

  - Added `ADC_DT_SPEC_*BY_NAME()` macros to get ADC IO-channel information from DT by name.
  - Added support for voltage biasing:

    - Added a `CONFIG_ADC_CONFIGURABLE_VBIAS_PIN` selected by drivers that support
      voltage biasing.
    - Added a `zephyr,vbias-pins` property to the adc-controller base binding to describe voltage
      bias pins.
    - Implemented for the TI ADC114s08 ADC driver.
  - Sample changes

    - Renamed existing ADC sample to adc\_dt.
    - Added a new sample called adc\_sequence that shows more of the runtime
      [`adc_sequence`](../doxygen/html/structadc__sequence.md) features.
  - New ADC Drivers

    - Added driver for the ENE KB1200.
    - Added driver for the NXP GAU ADC.
  - ADI AD559x changes

    - Added support for ADI’s ad5593.
    - Added I2C bus support for ADI ad559x.
    - Added configuration of internal reference voltage value to ad559x to support
      calls of [`adc_raw_to_millivolts()`](../doxygen/html/group__adc__interface.md#gaef98dabea3e0dc1cef8add298171a950).
    - Fixed issue with driver initialization causing improper operation in the ad559x driver
      regarding the availability of [`CONFIG_THREAD_NAME`](../kconfig.md#CONFIG_THREAD_NAME "CONFIG_THREAD_NAME").
    - Improved the ADC read efficiency and validation in ad559x driver.
  - ESP32 changes

    - Updated ESP32 ADC driver to work with version 5.1 of hal\_espressif.
    - Added support for DMA mode operation for ESP32S3 and ESP32C3.
  - nRF changes

    - Added support for nRF54L15 and nRF54H20 in the nrfx\_saadc driver.
    - Improved the nRF SAADC driver by disabling burst mode on unused channels, avoiding freezes.
    - Fixed issue which allowed negative ADC readings in single-ended mode using the
      `adc_nrfx_saadc.c` device driver.
      Note that this fix prevents the nRF54H and nRF54L series from performing
      8-bit resolution single-ended readings due to hardware limitations.
  - NXP LPADC changes

    - Enabled acquisition time feature in the NXP LPADC driver.
    - Added support for regulator output as reference to NXP LPADC.
    - Changed phandle type DT property `nxp,reference-supply` to phandle-array type DT property
      `nxp,references` in `nxp,lpc-lpadc` binding. The NXP LPADC driver now supports passing
      the reference voltage value by using `nxp,references`.
  - Smartbond changes

    - Added support for power management to the Smartbond SDADC and GPADC drivers.
    - Fixed support for [`CONFIG_PM_DEVICE_RUNTIME`](../kconfig.md#CONFIG_PM_DEVICE_RUNTIME "CONFIG_PM_DEVICE_RUNTIME") in the Smartbond ADC driver.
  - STM32 changes

    - Fixed various issues with DMA support in the STM32 ADC driver.
    - Added support for STM32H7R/S series.
  - Other driver changes

    - Added support for Nuvoton m2l31x in the numaker ADC driver.
    - Fixed issue with configuration register access in the ads1119 driver.
    - Fixed uninitialized value in kb1200 driver found in static analysis.
    - Fixed issue with [`adc_raw_to_millivolts()`](../doxygen/html/group__adc__interface.md#gaef98dabea3e0dc1cef8add298171a950) returning half the actual voltage with
      the tla2021 driver by correcting the reference voltage value.
  - Added support for Nuvoton Numaker M2L31X series.
- Battery

  - Added `re-charge-voltage-microvolt` property to the `battery` binding. This allows to set
    limit to automatically start charging again.
- Battery backed up RAM

  - Added support for STM32G0 and STM32H5 series.
- CAN

  - Extended support for automatic sample point location to also cover [`can_calc_timing()`](../doxygen/html/group__can__interface.md#gac27fe64142603f0d32d422594356b2d7) and
    [`can_calc_timing_data()`](../doxygen/html/group__can__interface.md#ga358cd73ed59c2099f4b2c6ceb397ca11).
  - Added optional `min-bitrate` devicetree property for CAN transceivers.
  - Added devicetree macros [`DT_CAN_TRANSCEIVER_MIN_BITRATE`](../doxygen/html/group__devicetree-can.md#ga60cb3dc5c2feb517dddcb5a57cce8a9b) and
    [`DT_INST_CAN_TRANSCEIVER_MIN_BITRATE`](../doxygen/html/group__devicetree-can.md#ga5c0b8011b5ec85dd8772f33572ae2b71) for getting the minimum supported bitrate of a CAN
    transceiver.
  - Added support for specifying the minimum bitrate supported by a CAN controller in the internal
    `CAN_DT_DRIVER_CONFIG_GET` and `CAN_DT_DRIVER_CONFIG_INST_GET` macros.
  - Added [`can_get_bitrate_min()`](../doxygen/html/group__can__interface.md#ga343456749eec6144a91bacae0d94b114) and [`can_get_bitrate_max()`](../doxygen/html/group__can__interface.md#ga1e6dc8026e4d922bce4d398d9f32a457) for retrieving the minimum
    and maximum supported bitrate for a given CAN controller/CAN transceiver combination, reflecting
    that retrieving the bitrate limits can no longer fail. Deprecated the existing
    `can_get_max_bitrate()` API function.
  - Updated the CAN timing functions to take the minimum supported bitrate into consideration when
    validating the bitrate.
  - Made the `sample-point` and `sample-point-data` devicetree properties optional.
  - Renamed the `bus_speed` and `bus_speed_data` fields of `can_driver_config` to
    `bitrate` and `bitrate_data`.
  - Added driver for [`nordic,nrf-can`](../build/dts/api/bindings/can/nordic%2Cnrf-can.md#std-dtcompatible-nordic-nrf-can).
  - Added driver support for Numaker M2L31X to the [`nuvoton,numaker-canfd`](../build/dts/api/bindings/can/nuvoton%2Cnumaker-canfd.md#std-dtcompatible-nuvoton-numaker-canfd) driver.
  - Added host communication test suite.
- Charger

  - Added `chgin-to-sys-current-limit-microamp` property to `maxim,max20335-charger`.
  - Added `system-voltage-min-threshold-microvolt` property to `maxim,max20335-charger`.
  - Added `re-charge-threshold-microvolt` property to `maxim,max20335-charger`.
  - Added `thermistor-monitoring-mode` property to `maxim,max20335-charger`.
- Clock control

  - Added support for Microcontroller Clock Output (MCO) on STM32H5 series.
  - Added support for MSI clock on STM32WL series.
  - Added driver for Analog Devices MAX32 SoC series.
  - Added support for Nuvoton Numaker M2L31X series.
  - Refactored ESP32 clock control driver to support ESP32-C6.
  - In LiteX (`drivers/clock_control/clock_control_litex.c`) added return code checking for
    `litex_clk_get_duty_cycle()` and `litex_clk_get_clkout_divider()`.
- Counter

  - Added support for Ambiq Apollo3 series.
  - Added support for STM32H7R/S series.
  - Added driver for LPTMR to NXP MCXN947
  - Added the `resolution` property in `nxp,lptmr` binding to represent the maximum width
    in bits the LPTMR peripheral uses for its counter.
- DAC

  - Added support for NXP RW SOC series DAC ([`nxp,gau-dac`](../build/dts/api/bindings/dac/nxp%2Cgau-dac.md#std-dtcompatible-nxp-gau-dac)).
  - Added support for Analog Devices AD5691 / AD5692 / AD5693 DACs
    ([`adi,ad5691`](../build/dts/api/bindings/dac/adi%2Cad5691.md#std-dtcompatible-adi-ad5691), [`adi,ad5692`](../build/dts/api/bindings/dac/adi%2Cad5692.md#std-dtcompatible-adi-ad5692) and [`adi,ad5693`](../build/dts/api/bindings/dac/adi%2Cad5693.md#std-dtcompatible-adi-ad5693)).
  - Added support for Texas Instruments DACx0501 series DACs ([`ti,dacx0501`](../build/dts/api/bindings/dac/ti%2Cdacx0501.md#std-dtcompatible-ti-dacx0501)).
- Disk

  - Support for eMMC devices was added to the STM32 SD driver. This can
    be enabled with [`CONFIG_SDMMC_STM32_EMMC`](../kconfig.md#CONFIG_SDMMC_STM32_EMMC "CONFIG_SDMMC_STM32_EMMC").
  - Added a loopback disk driver, to expose a disk device backed by a file.
    A file can be registered with the loopback disk driver using
    [`loopback_disk_access_register()`](../doxygen/html/loopback__disk_8h.md#a17a5f2ad1706fd7c3a8dcdbda2753b9c)
  - Added support for [`DISK_IOCTL_CTRL_INIT`](../doxygen/html/group__disk__driver__interface.md#ga9def34b23915a3ce6c9a8a746d3d1372) and
    [`DISK_IOCTL_CTRL_DEINIT`](../doxygen/html/group__disk__driver__interface.md#gaf13b377592baace863070fee450bd5be) macros, which allow for initializing
    and de-initializing a disk at runtime. This allows hotpluggable
    disk devices (like SD cards) to be removed and reinserted at runtime.
  - Added SDMMC support for STM32H5 series.
- Display

  - All in tree displays capable of supporting the [MIPI Display Bus Interface (DBI)](../hardware/peripherals/mipi_dbi.md#mipi-dbi-api) have
    been converted to use it. GC9X01X, UC81XX, SSD16XX, ST7789V, ST7735R based
    displays have been converted to this API. Boards using these displays will
    need their devicetree updated, see the display section of
    [Migration guide to Zephyr v3.7.0](migration-guide-3.7.md#migration-3-7) for examples of this process.
  - Added driver for ST7796S display controller ([`sitronix,st7796s`](../build/dts/api/bindings/display/sitronix%2Cst7796s.md#std-dtcompatible-sitronix-st7796s))
  - Added support for [`display_read()`](../doxygen/html/group__display__interface.md#ga3f497776520b0eac16b8aea80ccbbcfc) API to ILI9XXX display driver,
    which can be enabled with [`CONFIG_ILI9XXX_READ`](../kconfig.md#CONFIG_ILI9XXX_READ "CONFIG_ILI9XXX_READ")
  - Added support for [`display_set_orientation()`](../doxygen/html/group__display__interface.md#ga4e0a4dc2e434144874af014b8e7c4394) API to SSD16XXX
    display driver
  - Added driver for NT35510 MIPI-DSI display controller
    ([`frida,nt35510`](../build/dts/api/bindings/display/frida%2Cnt35510.md#std-dtcompatible-frida-nt35510))
  - Added driver to abstract LED strip devices as displays
    ([`led-strip-matrix`](../build/dts/api/bindings/display/led-strip-matrix.md#std-dtcompatible-led-strip-matrix))
  - Added support for [`display_set_pixel_format()`](../doxygen/html/group__display__interface.md#ga7ede828663090760c2558a231d9f2150) API to NXP eLCDIF
    driver. ARGB8888, RGB888, and BGR565 formats are supported.
  - Added support for inverting color at runtime to the SSD1306 driver, via
    the [`display_set_pixel_format()`](../doxygen/html/group__display__interface.md#ga7ede828663090760c2558a231d9f2150) API.
  - Inversion mode can now be disabled in the ST7789V driver
    ([`sitronix,st7789v`](../build/dts/api/bindings/display/sitronix%2Cst7789v.md#std-dtcompatible-sitronix-st7789v)) using the `inversion-off` property.
  - Added support for NXP MCXNx4x
- DMA

  - Error callback configuration renamed to better signal enable/disable status
  - Add support to NXP MCXN947
- DMIC

  - Added support for NXP `rd_rw612_bga`
- Entropy

  - Added support for STM32H7R/S series.
- EEPROM

  - Added property for specifying `address-width` to [`zephyr,i2c-target-eeprom`](../build/dts/api/bindings/mtd/zephyr%2Ci2c-target-eeprom.md#std-dtcompatible-zephyr-i2c-target-eeprom).
- eSPI

  - Renamed eSPI virtual wire direction macros, enum values and Kconfig to match the new
    terminology in eSPI 1.5 specification.
- Ethernet

  - Introduced [`CONFIG_ETH_DRIVER_RAW_MODE`](../kconfig.md#CONFIG_ETH_DRIVER_RAW_MODE "CONFIG_ETH_DRIVER_RAW_MODE"). This option allows building
    ethernet drivers without the zephyr L2 ethernet layer.
  - Removed the ethernet-fixed-link DT binding.
  - Removed VLAN handling from ethernet drivers since it is now handled by the
    generic ethernet L2 code.
  - Implemented/reworked HW MAC Address filtering in the eth\_mcux, eth\_nxp\_enet,
    and eth\_nxp\_s32\_gmac, eth\_stm32, and eth\_nxp\_s32\_netc drivers.
  - New Drivers

    - Added new eth\_nxp\_enet\_qos driver for the ethernet controller present on NXP MCXN SOCs.
    - Added support for adin1100 phy.
    - Added support for the Realtek RTL8211F phy.
  - NXP ENET driver changes

    - eth\_nxp\_enet driver is no longer experimental.
    - Deprecated eth\_mcux driver.
    - All boards and SOCs with [`nxp,kinetis-ethernet`](../build/dts/api/bindings/ethernet/nxp%2Ckinetis-ethernet.md#std-dtcompatible-nxp-kinetis-ethernet) compatible nodes
      reworked to use the new [`nxp,enet`](../build/dts/api/bindings/ethernet/nxp%2Cenet.md#std-dtcompatible-nxp-enet) binding.
    - Added support for network device power management with nxp\_enet driver on Kinetis platforms.
    - Converted eth\_nxp\_enet driver to use a dedicated workqueue for RX
      managed by the kernel rather than a manual infinite loop.
    - Disabled hardware checksum acceleration when IPV6 is enabled with eth\_nxp\_enet, since
      the hardware does not support accelerating ICMPv6 checksums.
    - Added support for [`nxp,enet1g`](../build/dts/api/bindings/ethernet/nxp%2Cenet1g.md#std-dtcompatible-nxp-enet1g).
    - Added support to use a fused MAC address for nxp\_enet MAC on some platforms.
    - Fixed issue with LAA bit not being set and a confusing description of the nxp,unique-mac
      property used with the nxp\_enet driver.
    - Fixed cache maintain being enabled when using a noncache DMA buffer in nxp\_enet driver.
    - Added MMIO mappings to nxp\_enet driver.
    - Clarified DSA supported with eth\_nxp\_enet.
  - NXP S32 ethernet changes

    - The eth\_nxp\_s32\_gmac driver now implies [`CONFIG_MDIO`](../kconfig.md#CONFIG_MDIO "CONFIG_MDIO").
    - eth\_nxp\_s32\_netc driver updated to use new MBOX API.
  - Adin2111 driver changes

    - Corrected the bitfield position of IAMSK1 TX\_READY\_MASK in adin2111 driver.
    - Changed adin2111 driver to always append crc32 to the end of the frame.
    - Adjusted eth\_adin2111 driver to have the appropriate multicaster filter mask.
    - Fixed the “generic SPI without crc8” mode of adin2111 driver.
    - Added Open Alliance SPI protocol support to the adin2111 driver.
    - Added custom driver extension APIs for adin2111 driver.
    - Enabled support for promiscuous mode in the adin2111 driver.
    - Moved OA buffers out of device data of the adin2111 driver to save ~32KB of space
      when using the generic SPI protocol.
    - Fixed a build warning in eth\_adin2111 driver on 64-bit platforms.
    - Various small changes to adin2111 driver.
  - STM32 ethernet driver changes

    - Added support for PTP on compatible STM32 series (STM32F7, STM32H5 and STM32H7).
    - Changed eth\_stm32 to use phy APIs to access the phy to avoid collisions when multitasking.
    - Removed legacy STM32Cube HAL API support for STM32 F4, F7, and H7 series.
    - Added support for RX/TX timestamping to eth\_stm32\_hal driver.
  - ESP32 ethernet driver changes

    - Added support to esp32 ethernet driver to set the MAC address during runtime.
    - Updated esp32 ethernet driver to work with version 5.1 of hal\_espressif.
    - Fixed build of esp32 ethernet driver when [`CONFIG_NET_STATISTICS`](../kconfig.md#CONFIG_NET_STATISTICS "CONFIG_NET_STATISTICS") is enabled.
    - Fixed ESP32 ethernet driver not clocking external PHY correctly over GPIO.
  - Other ethernet driver changes

    - Added link status detection to the w5500 ethernet driver, configurable via Kconfig.
    - Added ability to set MAC address at runtime with eth\_liteeth driver.
    - Fixed issue in the eth\_stellaris driver where it was previously not taken into account
      that the number of interrupts received by the driver may be less than the number of
      data packets received by the ethernet controller.
    - Added a devicetree property for the enc28j60 to set the RX filter.
    - Fixed ESTAT TXABRT bit not being cleared on error in the enc28j60 driver.
    - Added conditions to enable ptp\_clock driver implementation for the native\_posix
      ethernet driver when PTP subsystem is enabled.
    - Fixed DSA driver for KSZ8xxx to correctly initialize LAN devices.
    - Fixed the wrong register address being used for tail tag enable in ksz8863.
  - Phy driver changes

    - Fixed various control issues with the KSZ8081 phy driver regarding
      resets, autonegotiation, link detection, and missing/spamming logging messages.
    - Changed property names of the reset and interrupt gpios in the KSZ8081 DT binding.
    - Fixed bus fault in phy\_mii driver when using fixed-link mode.
- Flash

  - Added support for Ambiq Apollo3 series.
  - Added support for multiple instances of the SPI NOR driver (spi\_nor.c).
  - Added preliminary support for non-erase devices with introduction of
    device capabilities to [`flash_parameters`](../doxygen/html/structflash__parameters.md) and the utility function
    [`flash_params_get_erase_cap()`](../doxygen/html/group__flash__interface.md#gabc73e8888dcb8f4f79cd80b8d02a6a2c) that allows to obtain the erase type
    provided by a device; added [`FLASH_ERASE_C_EXPLICIT`](../doxygen/html/group__flash__interface.md#ga760f7d79cb9f23bc0326abfea85808aa), which is
    currently the only supported erase type and is set by all flash devices.
  - Added the [`flash_flatten()`](../doxygen/html/group__flash__interface.md#ga11eda0cdc7be12636a90d2e8c7264e4a) function that can be used on devices,
    with or without erase requirement, when erase has been used not for preparing
    a device for a random data write, but rather to remove/scramble data from
    that device.
  - Added the [`flash_fill()`](../doxygen/html/group__flash__interface.md#ga022838332e905b0111d5136dd963889b) utility function which allows to write
    a single value across a provided range in a selected device.
  - Added support for RRAM on nrf54l15 devices.
  - Added support of non busy wait polling in STM32 OSPI driver.
  - Added support for STM32 XSPI external NOR flash driver ([`st,stm32-xspi-nor`](../build/dts/api/bindings/flash_controller/st%2Cstm32-xspi-nor.md#std-dtcompatible-st-stm32-xspi-nor)).
  - Added support for XIP on external NOR flash in STM32 OSPI, QSPI and XSPI driver.
  - STM32 OSPI driver: clk, dqs, ncs ports can now be configured by device tree
    configurable (see [`st,stm32-ospi`](../build/dts/api/bindings/ospi/st%2Cstm32-ospi.md#std-dtcompatible-st-stm32-ospi)).
  - Added FlexSPI support to NXP MCXN947
  - Added support for Nuvoton Numaker M2L31X series.
- Fuel Gauge

  - max17048: Corrected voltage units from mV to uV.
- GNSS

  - Added GNSS device driver API test suite.
  - Added support for the u-blox UBX protocol.
  - Added device driver for the u-blox M8 GNSS modem ([`u-blox,m8`](../build/dts/api/bindings/gnss/u-blox%2Cm8.md#std-dtcompatible-u-blox-m8)).
  - Added device driver for the Luatos Air530z GNSS modem ([`luatos,air530z`](../build/dts/api/bindings/gnss/luatos%2Cair530z.md#std-dtcompatible-luatos-air530z)).
- GPIO

  - Added support for Ambiq Apollo3 series.
  - Added Broadcom Set-top box(brcmstb) SoC GPIO driver.
  - Added [`STM32_GPIO_WKUP`](../doxygen/html/group__gpio__interface.md#ga9a05f736e9ee915f591a65a7f6d382d3) flag which allows to configure specific pins as wakeup source
    from Power Off state on STM32 L4, U5, WB, & WL SoC series.
  - Added driver for Analog Devices MAX32 SoC series.
  - Added support for Nuvoton Numaker M2L31X series.
  - Added interrupt support to the Renesas RZ/T2M GPIO driver ([`renesas,rzt2m-gpio`](../build/dts/api/bindings/gpio/renesas%2Crzt2m-gpio.md#std-dtcompatible-renesas-rzt2m-gpio)).
- Hardware info

  - Added device EUI64 ID support and implementation for STM32WB, STM32WBA and STM32WL series.
- I2C

  - Added support for Ambiq Apollo3 series.
  - In STM32 V2 driver, added support for a new [`CONFIG_I2C_STM32_V2_TIMING`](../kconfig.md#CONFIG_I2C_STM32_V2_TIMING "CONFIG_I2C_STM32_V2_TIMING")
    which automatically computes bus timings which should be used to configure the hardware
    block depending on the clock configuration in use. To avoid embedding this heavy algorithm
    in a production application, a dedicated sample [I2C V2 timings](../samples/boards/st/i2c_timing/README.md#stm32_i2c_v2_timings "Retrieve I2C V2 timings at runtime.") is provided
    to get the output of the algorithm. Once bus timings configuration is available,
    [`CONFIG_I2C_STM32_V2_TIMING`](../kconfig.md#CONFIG_I2C_STM32_V2_TIMING "CONFIG_I2C_STM32_V2_TIMING") could be disabled, bus timings configured
    using device tree.
  - Added support for STM32H5 series.
  - Added support to NXP MCXN947
  - Added driver for Analog Devices MAX32 SoC series.
  - Added support for Nuvoton Numaker M2L31X series.
  - LiteX I2C driver (`drivers/i2c/i2c_litex.c`):

    - Added support for bitrate setting from the devicetree.
    - Added `i2c_litex_recover_bus()` and `i2c_litex_get_config()` API
      implementations.
- I2S

  - Added support for STM32H5 series.
  - Extended the MCUX Flexcomm driver to support additional channels and formats.
  - Added support for Nordic nRF54L Series.
  - Fixed divider calculations in the nRF I2S driver.
- I3C

  - Added shell support for querying bus and CCC commands.
  - Added driver to support the I3C controller on NPCX.
  - Improvements and bug fixes on [`nxp,mcux-i3c`](../build/dts/api/bindings/i3c/nxp%2Cmcux-i3c.md#std-dtcompatible-nxp-mcux-i3c), including handling the bus
    being busy more gracefully instead of simply returning errors.
- Input

  - New drivers: [`adc-keys`](../build/dts/api/bindings/input/adc-keys.md#std-dtcompatible-adc-keys), [`chipsemi,chsc6x`](../build/dts/api/bindings/input/chipsemi%2Cchsc6x.md#std-dtcompatible-chipsemi-chsc6x),
    [`cirque,pinnacle`](../build/dts/api/compatibles/cirque%2Cpinnacle.md#std-dtcompatible-cirque-pinnacle), [`futaba,sbus`](../build/dts/api/bindings/input/futaba%2Csbus.md#std-dtcompatible-futaba-sbus),
    [`pixart,pat912x`](../build/dts/api/bindings/input/pixart%2Cpat912x.md#std-dtcompatible-pixart-pat912x), [`pixart,paw32xx`](../build/dts/api/bindings/input/pixart%2Cpaw32xx.md#std-dtcompatible-pixart-paw32xx),
    [`pixart,pmw3610`](../build/dts/api/bindings/input/pixart%2Cpmw3610.md#std-dtcompatible-pixart-pmw3610) and [`sitronix,cf1133`](../build/dts/api/bindings/input/sitronix%2Ccf1133.md#std-dtcompatible-sitronix-cf1133).
  - Migrated [`holtek,ht16k33`](../build/dts/api/bindings/led/holtek%2Cht16k33.md#std-dtcompatible-holtek-ht16k33) and
    [`microchip,xec-kbd`](../build/dts/api/bindings/input/microchip%2Cxec-kbd.md#std-dtcompatible-microchip-xec-kbd) from kscan to input subsystem.
- LED

  - Added device completion to LED shell commands and made the `get_info` command display
    colors as strings.
  - Added driver for Lumissil Microsystems (a division of ISSI) IS31FL3194 controller
    ([`issi,is31fl3194`](../build/dts/api/bindings/led/issi%2Cis31fl3194.md#std-dtcompatible-issi-is31fl3194)).
- LED Strip

  - The `chain-length` and `color-mapping` properties have been added to all LED strip
    bindings.
  - The length of a strip is now checked before updating it, an error is returned if the provided
    data is too long.
  - A length function has been added which returns the length of the LED strip
    ([`led_strip_length()`](../doxygen/html/group__led__strip__interface.md#ga7f94eab0b357a81cccb5f0ea1575714a)).
  - The update channels function is now optional and can be left unimplemented.
  - The `in-gpios` and `output-pin` properties of the respective
    [`worldsemi,ws2812-gpio`](../build/dts/api/bindings/led_strip/worldsemi%2Cws2812-gpio.md#std-dtcompatible-worldsemi-ws2812-gpio) and [`worldsemi,ws2812-rpi_pico-pio`](../build/dts/api/bindings/led_strip/worldsemi%2Cws2812-rpi_pico-pio.md#std-dtcompatible-worldsemi-ws2812-rpi_pico-pio)
    devicetree bindings have been renamed to `gpios`.
  - Removed `CONFIG_WS2812_STRIP` and `CONFIG_WS2812_STRIP_DRIVER` Kconfig options. They became
    useless after refactoring.
  - Added driver for Texas Instruments TLC59731 RGB controller.
- LoRa

  - Added driver for Reyax LoRa module
- Mailbox

  - Added support for HSEM based STM32 driver.
- MDIO

  - Made the `bus_enable` and `bus_disable` functions optional for drivers to
    implement, and removed empty implementation from many drivers.
  - Added NXP ENET QOS MDIO controller driver.
  - Fixed but with NXP ENET MDIO driver blocking the system workqueue.
  - [`CONFIG_MDIO_NXP_ENET_TIMEOUT`](../kconfig.md#CONFIG_MDIO_NXP_ENET_TIMEOUT "CONFIG_MDIO_NXP_ENET_TIMEOUT") units change to microseconds.
  - Added support for STM32 MDIO controller driver.
- MFD

  - New driver [`nxp,lp-flexcomm`](../build/dts/api/bindings/mfd/nxp%2Clp-flexcomm.md#std-dtcompatible-nxp-lp-flexcomm).
  - New driver [`rohm,bd8lb600fs`](../build/dts/api/bindings/mfd/rohm%2Cbd8lb600fs.md#std-dtcompatible-rohm-bd8lb600fs).
  - New driver [`maxim,max31790`](../build/dts/api/bindings/mfd/maxim%2Cmax31790.md#std-dtcompatible-maxim-max31790).
  - New driver [`infineon,tle9104`](../build/dts/api/bindings/mfd/infineon%2Ctle9104.md#std-dtcompatible-infineon-tle9104)
  - New driver [`adi,ad559x`](../build/dts/api/compatibles/adi%2Cad559x.md#std-dtcompatible-adi-ad559x)
  - Added option to disable N\_VBUSEN for [`x-powers,axp192`](../build/dts/api/bindings/mfd/x-powers%2Caxp192.md#std-dtcompatible-x-powers-axp192).
  - Added GPIO input edge events for [`nordic,npm1300`](../build/dts/api/bindings/mfd/nordic%2Cnpm1300.md#std-dtcompatible-nordic-npm1300).
  - Added long press reset configuration for [`nordic,npm1300`](../build/dts/api/bindings/mfd/nordic%2Cnpm1300.md#std-dtcompatible-nordic-npm1300).
  - Fixed initialisation of hysteretic mode for [`nordic,npm6001`](../build/dts/api/bindings/mfd/nordic%2Cnpm6001.md#std-dtcompatible-nordic-npm6001).
- Modem

  - Removed deprecated `GSM_PPP` driver along with its dts compatible `zephyr,gsm-ppp`.
  - Removed deprecated `UART_MUX` and `GSM_MUX` previously used by `GSM_PPP`.
  - Removed support for dts compatible `zephyr,gsm-ppp` from `MODEM_CELLULAR` driver.
  - Removed integration with `UART_MUX` from `MODEM_IFACE_UART_INTERRUPT` module.
  - Removed integration with `UART_MUX` from `MODEM_SHELL` module.
  - Implemented modem pipelinks in `MODEM_CELLULAR` driver for additional DLCI channels
    available by the different modems. This includes generic AT mode DLCI channels, named
    `user_pipe_<index>` and DLCI channels reserved for GNSS tunneling named
    `gnss_pipe`.
  - Added new set of shell commands for sending AT commands directly to a modem using the
    newly implemented modem pipelinks. The implementation of the new shell commands is
    both functional and together with the `MODEM_CELLULAR` driver will provide an
    example of how to implement and use the modem pipelink module.
- PCIE

  - `pcie_bdf_lookup` and `pcie_probe` have been removed since they have been
    deprecated since v3.3.0.
- MIPI-DBI

  - Added release API
  - Added support for mode selection via the device tree
- MSPI

  - Add the new experimental [MSPI(Multi-bit SPI)](../hardware/peripherals/mspi.md#mspi-api) API, enabling support for
    advanced SPI controllers and peripherals that typically require command, address and data
    phases as well as variable latency for a transfer. The API now supports from single wire
    SDR up to hex wires DDR communication in sync/async ways.
  - Added MSPI bus emulator under bus emulators to showcase the implementation of the MSPI API.
  - Added MSPI flash device emulator to showcase the use of the MSPI API and interfacing with
    MSPI bus controllers.
  - Added APS6404L QPI pSRAM device driver.
  - Added ATXP032 OPI NOR flash device driver.
  - Added Ambiq Apollo3p MSPI controller driver.
  - Added [MSPI asynchronous transfer](../samples/drivers/mspi/mspi_async/README.md#mspi-async "Use the MSPI API to interact with MSPI memory device asynchronously.") and [JEDEC MSPI-NOR flash](../samples/drivers/mspi/mspi_flash/README.md#mspi-flash "Use the flash API to interact with a MSPI NOR serial flash memory device.") samples to
    showcase the use of MSPI device drivers.
  - Added mspi/api and mspi/flash testcase for developers to check their implementations.
- Pin control

  - Added driver for Renesas RA8 series
  - Added driver for Infineon PSoC6 (legacy)
  - Added driver for Analog Devices MAX32 SoC series.
  - Added driver for Ambiq Apollo3
  - Added driver for ENE KB1200
  - Added driver for NXP RW
  - Espressif driver now supports ESP32C6
  - STM32 driver now supports remap functionality for STM32C0
  - Added support for Nuvoton Numaker M2L31X series.
- PWM

  - Added support for STM32H7R/S series.
  - Added a Add QTMR PWM driver for NXP imxrt11xx
  - Made the NXP MCUX PWM driver thread safe
  - Fix [PWM Blinky](../samples/basic/blinky_pwm/README.md#pwm-blinky "Blink an LED using the PWM API.") code sample to demonstrate PWM support for
    [BeagleConnect Freedom](../boards/beagle/beagleconnect_freedom/doc/index.md#beagleconnect_freedom).
  - Added driver for ENE KB1200.
  - Added support for Nordic nRF54H and nRF54L Series SoCs.
  - Added support for Nuvoton Numaker M2L31X series.
- Regulators

  - New driver [`cirrus,cp9314`](../build/dts/api/bindings/regulator/cirrus%2Ccp9314.md#std-dtcompatible-cirrus-cp9314).
  - Added `regulator-boot-off` property to common regulator driver.
    Updated [`adi,adp5360-regulator`](../build/dts/api/bindings/regulator/adi%2Cadp5360-regulator.md#std-dtcompatible-adi-adp5360-regulator), [`nordic,npm1300-regulator`](../build/dts/api/bindings/regulator/nordic%2Cnpm1300-regulator.md#std-dtcompatible-nordic-npm1300-regulator),
    [`nordic,npm6001-regulator`](../build/dts/api/bindings/regulator/nordic%2Cnpm6001-regulator.md#std-dtcompatible-nordic-npm6001-regulator) and [`x-powers,axp192-regulator`](../build/dts/api/bindings/regulator/x-powers%2Caxp192-regulator.md#std-dtcompatible-x-powers-axp192-regulator)
    to use this new property.
  - Added power management for [`renesas,smartbond-regulator`](../build/dts/api/bindings/regulator/renesas%2Cda1469x-regulator.md#std-dtcompatible-renesas-smartbond-regulator).
  - Added `is_enabled` shell command.
  - Removed use of busy wait for single threaded systems.
  - Fixed control of DCDC2 output for [`x-powers,axp192-regulator`](../build/dts/api/bindings/regulator/x-powers%2Caxp192-regulator.md#std-dtcompatible-x-powers-axp192-regulator).
  - Fixed current and voltage get functions for [`renesas,smartbond-regulator`](../build/dts/api/bindings/regulator/renesas%2Cda1469x-regulator.md#std-dtcompatible-renesas-smartbond-regulator).
  - Fixed NXP VREF Kconfig leakage.
  - Fixed display of micro values in shell.
  - Fixed strcmp usage bug in `adset` shell command.
- Reset

  - Added driver for reset controller on Nuvoton NPCX chips.
  - Added reset controller driver for NXP SYSCON.
  - Added reset controller driver for NXP RSTCTL.
  - Added support for Nuvoton Numaker M2L31X series.
- RTC

  - Added Raspberry Pi Pico RTC driver.
  - Added support for [`CONFIG_RTC_ALARM`](../kconfig.md#CONFIG_RTC_ALARM "CONFIG_RTC_ALARM") on all STM32 MCU series (except STM32F1).
  - Added support for Nuvoton Numaker M2L31X series.
- RTIO

  - Move lock-free queues out of RTIO into lib, dropping the `rtio_` prefix to SPSC and MPSC queues.
  - Added tests and fixed bugs related to chained callback requests.
  - Wrapper around p4wq (rtio workq) created to go from blocking to non-blocking behavior in cases
    where native asynchronous RTIO functionality is unavailable.
- SDHC

  - Added ESP32 SDHC driver ([`espressif,esp32-sdhc`](../build/dts/api/bindings/sdhc/espressif%2Cesp32-sdhc.md#std-dtcompatible-espressif-esp32-sdhc)).
  - Added SDHC driver for Renesas MMC controller ([`renesas,rcar-mmc`](../build/dts/api/bindings/mmc/renesas%2Crcar-emmc.md#std-dtcompatible-renesas-rcar-mmc)).
- Sensors

  - General

    - Added a channel specifier to the new read/decoder API.
    - Added a blocking sensor read call [`sensor_read()`](../doxygen/html/group__sensor__interface.md#ga1e77abad33cfd4b8330484cdc1354976).
    - Decoupled RTIO requests using RTIO workqueues service to turn
      `sensor_submit_callback()` into an asynchronous request.
    - Moved most drivers to vendor subdirectories.
  - AMS

    - Added TSL2591 light sensor driver ([`ams,tsl2591`](../build/dts/api/bindings/sensor/ams%2Ctsl2591.md#std-dtcompatible-ams-tsl2591)).
  - Aosong

    - Added DHT20 digital-output humidity and temperature sensor driver
      ([`aosong,dht20`](../build/dts/api/bindings/sensor/aosong%2Cdht20.md#std-dtcompatible-aosong-dht20)).
    - Added [`CONFIG_DHT_LOCK_IRQS`](../kconfig.md#CONFIG_DHT_LOCK_IRQS "CONFIG_DHT_LOCK_IRQS") for the dht11 driver which allows for locking
      interrupts during sensor reading to prevent issues with reading the sensor.
  - Bosch

    - Updated BME280 to the new async API.
  - Infineon

    - Added TLE9104 power train switch diagnostics sensor driver
      ([`infineon,tle9104-diagnostics`](../build/dts/api/bindings/sensor/infineon%2Ctle9104-diagnostics.md#std-dtcompatible-infineon-tle9104-diagnostics)).
  - Maxim

    - Added DS18S20 1-Wire temperature sensor driver ([`maxim,ds18s20`](../build/dts/api/bindings/sensor/maxim%2Cds18s20.md#std-dtcompatible-maxim-ds18s20)).
    - Added MAX31790 fan speed and fan fault sensor
      ([`maxim,max31790-fan-fault`](../build/dts/api/bindings/sensor/maxim%2Cmax31790-fan-fault.md#std-dtcompatible-maxim-max31790-fan-fault) and [`maxim,max31790-fan-speed`](../build/dts/api/bindings/sensor/maxim%2Cmax31790-fan-speed.md#std-dtcompatible-maxim-max31790-fan-speed)).
  - NXP

    - Added low power comparator driver ([`nxp,lpcmp`](../build/dts/api/bindings/sensor/nxp%2Clpcmp.md#std-dtcompatible-nxp-lpcmp)).
  - Rohm

    - Added BD8LB600FS diagnostics sensor driver ([`rohm,bd8lb600fs-diagnostics`](../build/dts/api/bindings/sensor/rohm%2Cbd8lb600fs-diagnostics.md#std-dtcompatible-rohm-bd8lb600fs-diagnostics)).
  - Silabs

    - Made various fixes and enhancements to the SI7006 humidity/temperature sensor driver.
  - ST

    - QDEC driver now supports encoder mode configuration (see [`st,stm32-qdec`](../build/dts/api/bindings/sensor/st%2Cstm32-qdec.md#std-dtcompatible-st-stm32-qdec)).
    - Added support for STM32 Digital Temperature Sensor ([`st,stm32-digi-temp`](../build/dts/api/bindings/sensor/st%2Cstm32-digi-temp.md#std-dtcompatible-st-stm32-digi-temp)).
    - Added IIS328DQ I2C/SPI accelerometer sensor driver ([`st,iis328dq`](../build/dts/api/compatibles/st%2Ciis328dq.md#std-dtcompatible-st-iis328dq)).
  - TDK

    - Added support for the MPU6500 3-axis accelerometer and 3-axis gyroscope sensor to the
      MPU6050 driver.
  - TI

    - Added TMP114 driver ([`ti,tmp114`](../build/dts/api/bindings/sensor/ti%2Ctmp114.md#std-dtcompatible-ti-tmp114)).
    - Added INA226 bidirectional current and power monitor driver ([`ti,ina226`](../build/dts/api/bindings/sensor/ti%2Cina226.md#std-dtcompatible-ti-ina226)).
    - Added LM95234 quad remote diode and local temperature sensor driver
      ([`national,lm95234`](../build/dts/api/bindings/sensor/national%2Clm95234.md#std-dtcompatible-national-lm95234)).
  - Other vendors

    - Added Angst+Pfister FCX-MLDX5 O2 sensor driver ([`ap,fcx-mldx5`](../build/dts/api/bindings/sensor/ap%2Cfcx-mldx5.md#std-dtcompatible-ap-fcx-mldx5)).
    - Added ENE KB1200 tachometer sensor driver ([`ene,kb1200-tach`](../build/dts/api/bindings/tach/ene%2Ckb1200-tach.md#std-dtcompatible-ene-kb1200-tach)).
    - Added Festo VEAA-X-3 series proportional pressure regulator driver
      ([`festo,veaa-x-3`](../build/dts/api/bindings/sensor/festo%2Cveaa-x-3.md#std-dtcompatible-festo-veaa-x-3)).
    - Added Innovative Sensor Technology TSic xx6 temperature sensor driver
      ([`ist,tsic-xx6`](../build/dts/api/bindings/sensor/ist%2Ctsic-xx6.md#std-dtcompatible-ist-tsic-xx6)).
    - Added ON Semiconductor NCT75 temperature sensor driver ([`onnn,nct75`](../build/dts/api/bindings/sensor/onnn%2Cnct75.md#std-dtcompatible-onnn-nct75)).
    - Added ScioSense ENS160 digital metal oxide multi-gas sensor driver
      ([`sciosense,ens160`](../build/dts/api/compatibles/sciosense%2Cens160.md#std-dtcompatible-sciosense-ens160)).
    - Made various fixes and enhancements to the GROW\_R502A fingerprint sensor driver.
- Serial

  - Added driver to support UART over Bluetooth LE using NUS (Nordic UART Service). This driver
    enables using Bluetooth as a transport to all the subsystems that are currently supported by
    UART (e.g: Console, Shell, Logging).
  - Added [`CONFIG_NOCACHE_MEMORY`](../kconfig.md#CONFIG_NOCACHE_MEMORY "CONFIG_NOCACHE_MEMORY") support in async DMA mode in STM32 driver.
    It is now possible to use UART in DMA mode with [`CONFIG_DCACHE`](../kconfig.md#CONFIG_DCACHE "CONFIG_DCACHE") enabled
    on STM32 F7 & H7 SoC series, as long as DMA buffers are placed in an uncached memory section.
  - Added support for STM32H7R/S series.
  - Added support for HSCIF (High Speed Serial Communication Interface with FIFO) in the UART
    driver for Renesas RCar platforms.
  - Added driver for ENE KB1200 UART.
  - Added driver for UART on Analog Devices MAX32 series microcontrollers.
  - Added driver for UART on Renesas RA8 devices.
  - `uart_emul` ([`zephyr,uart-emul`](../build/dts/api/bindings/serial/zephyr%2Cuart-emul.md#std-dtcompatible-zephyr-uart-emul)):

    - Added support for asynchronous API for the emulated UART driver.
  - `uart_esp32` ([`espressif,esp32-uart`](../build/dts/api/bindings/serial/espressif%2Cesp32-uart.md#std-dtcompatible-espressif-esp32-uart)):

    - Added support to invert TX and RX pin signals.
    - Added support for ESP32C6 SoC.
  - `uart_native_tty` ([`zephyr,native-tty-uart`](../build/dts/api/bindings/serial/zephyr%2Cnative-tty-uart.md#std-dtcompatible-zephyr-native-tty-uart)):

    - Added support to emulate interrupt driven UART.
  - `uart_mcux_lpuart` (`nxp,kinetis-lpuart`):

    - Added support for single wire half-duplex communication.
    - Added support to invert TX and RX pin signals.
  - `uart_npcx` ([`nuvoton,npcx-uart`](../build/dts/api/bindings/serial/nuvoton%2Cnpcx-uart.md#std-dtcompatible-nuvoton-npcx-uart)):

    - Added support for asynchronous API.
    - Added support for baud rate of 3MHz.
  - `uart_nrfx_uarte` ([`nordic,nrf-uarte`](../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte)):

    - Added support to put TX and RX pins into low power mode when UART is not active.
  - `uart_nrfx_uarte2` ([`nordic,nrf-uarte`](../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte)):

    - Prevents UART from transmitting when device is suspended.
    - Fixed some events not being triggered.
  - `uart_pl011` ([`arm,pl011`](../build/dts/api/bindings/serial/arm%2Cpl011.md#std-dtcompatible-arm-pl011)):

    - Added support for runtime configuration.
    - Added support for reset device.
    - Added support to use clock control to determine frequency.
    - Added support for hardware flow control.
    - Added support for UART on Ambiq Apollo3 SoC.
  - `uart_smartbond` ([`renesas,smartbond-uart`](../build/dts/api/bindings/serial/renesas%2Csmartbond-uart.md#std-dtcompatible-renesas-smartbond-uart)):

    - Added support for power management.
    - Added support to wake up via DTR and RX lines.
  - `uart_stm32` ([`st,stm32-uart`](../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart)):

    - Added support to identify if DMA buffers are in data cache or non-cacheable memory.
  - Added support for Nuvoton Numaker M2L31X series.
- SPI

  - Added support to NXP MCXN947
  - Added support for Ambiq Apollo3 series general IOM based SPI.
  - Added support for Ambiq Apollo3 BLEIF based SPI, which is specific for internal HCI.
  - Added support for [`CONFIG_PM`](../kconfig.md#CONFIG_PM "CONFIG_PM") and [`CONFIG_PM_DEVICE_RUNTIME`](../kconfig.md#CONFIG_PM_DEVICE_RUNTIME "CONFIG_PM_DEVICE_RUNTIME") on STM32 SPI driver.
  - Added support for [`CONFIG_NOCACHE_MEMORY`](../kconfig.md#CONFIG_NOCACHE_MEMORY "CONFIG_NOCACHE_MEMORY") in DMA SPI mode for STM32F7x SoC series.
  - Added support for STM32H7R/S series.
  - Added driver for Analog Devices MAX32 SoC series.
  - Fixed an incorrect register assignment in gd32 spi.
- USB

  - Added UDC shim driver for NXP EHCI and IP3511 USB controller.
  - Various fixes and improvements in IT82xx2, DWC2, STM32, RP2040, Smartbond
    USB controller drivers.
- Video

  - Added support for STM32 Digital camera interface (DCMI) driver ([`st,stm32-dcmi`](../build/dts/api/bindings/video/st%2Cstm32-dcmi.md#std-dtcompatible-st-stm32-dcmi)).
  - Enabled NXP USB Device controllers
  - Added support for the ov7670 camera
  - Added support for the ov5640 camera
  - Added CSI-2 MIPI driver for NXP MCUX
  - Added support for DVP FPC 24-pins mt9m114 camera module shield
- Watchdog

  - Added [`CONFIG_WDT_NPCX_WARNING_LEADING_TIME_MS`](../kconfig.md#CONFIG_WDT_NPCX_WARNING_LEADING_TIME_MS "CONFIG_WDT_NPCX_WARNING_LEADING_TIME_MS") to set the leading warning time
    in milliseconds. Removed no longer used `CONFIG_WDT_NPCX_DELAY_CYCLES`.
  - Added support for Ambiq Apollo3 series.
  - Added support for STM32H7R/S series.
  - Added support for Nuvoton Numaker M2L31X series.
  - Added watchdog for external 32kHz crystal in ESP32 SoC variants.
- Wi-Fi

  - Fixed message parsing for esp-at.
  - Fixed esp-at connect failures.
  - Implement [`bind()`](../doxygen/html/posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8) and [`recvfrom()`](../doxygen/html/posix_2sys_2socket_8h.md#a1c41b0d557d19b5031e668b1997dc73a) for UDP sockets for esp-at.
  - Added option for setting maximum data size for eswifi.
  - Fixed ESP32 Wi-Fi driver memory leak.

## Networking

- ARP:

  - Added support for gratuitous ARP transmission.
  - Fixed a possible deadlock between TX and RX threads within ARP module.
  - Fixed a possible ARP entry leak.
  - Improved ARP debug logs.
- CoAP:

  - Fixed CoAP observe age overflows.
  - Increased upper limit for CoAP retransmissions ([`CONFIG_COAP_MAX_RETRANSMIT`](../kconfig.md#CONFIG_COAP_MAX_RETRANSMIT "CONFIG_COAP_MAX_RETRANSMIT")).
  - Fixed CoAP observations in CoAP client library.
  - Added new CoAP client [`coap_client_cancel_requests()`](../doxygen/html/group__coap__client.md#ga3f511d4df22bece05c1ac97ff4d09a80) API which allows
    to cancel active observations.
  - Fixed CoAP ID generation for responses in CoAP Server sample.
- Connection manager:

  - Added support for new net\_mgmt events, which allow to track IPv4 and IPv6
    connectivity independently:

    - [`NET_EVENT_L4_IPV4_CONNECTED`](../doxygen/html/group__net__mgmt.md#ga532fdc2f199e047a5d17e325cee12cf1)
    - [`NET_EVENT_L4_IPV4_DISCONNECTED`](../doxygen/html/group__net__mgmt.md#gaa92cc806d93446d548a05edb8e0074c2)
    - [`NET_EVENT_L4_IPV6_CONNECTED`](../doxygen/html/group__net__mgmt.md#gaf6bb88ed90df5aacb40e42fcc5bfbcf5)
    - [`NET_EVENT_L4_IPV6_DISCONNECTED`](../doxygen/html/group__net__mgmt.md#gac81abeab44fbf2b6f29d4e11a1e1bd17)
- DHCPv4:

  - Added support for encapsulated vendor specific options. By enabling
    [`CONFIG_NET_DHCPV4_OPTION_CALLBACKS_VENDOR_SPECIFIC`](../kconfig.md#CONFIG_NET_DHCPV4_OPTION_CALLBACKS_VENDOR_SPECIFIC "CONFIG_NET_DHCPV4_OPTION_CALLBACKS_VENDOR_SPECIFIC") callbacks can be
    registered with [`net_dhcpv4_add_option_vendor_callback()`](../doxygen/html/group__dhcpv4.md#gabf3d97139fc4f7122c1bdee52cb003cb) to handle these options after
    being initialised with [`net_dhcpv4_init_option_vendor_callback()`](../doxygen/html/group__dhcpv4.md#gaec0f1c87f5093767a4bb1c43b8e18e72).
  - Added support for the “Vendor class identifier” option. Use the
    [`CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER`](../kconfig.md#CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER "CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER") to enable it and
    [`CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER_STRING`](../kconfig.md#CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER_STRING "CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER_STRING") to set it.
  - The NTP server from the DHCPv4 option can now be used to set the system time. This is done by
    default, if [`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`](../kconfig.md#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT "CONFIG_NET_CONFIG_CLOCK_SNTP_INIT") is enabled.
  - The syslog server address can now be set with DHCPv4 option. This is done by
    default, if [`CONFIG_LOG_BACKEND_NET_USE_DHCPV4_OPTION`](../kconfig.md#CONFIG_LOG_BACKEND_NET_USE_DHCPV4_OPTION "CONFIG_LOG_BACKEND_NET_USE_DHCPV4_OPTION") is enabled.
  - Fixed a bug, where options with registered callbacks were not requested from
    the server.
  - Fixed a bug, where netmask received from the server was not applied correctly.
  - Reimplemented DHCPv4 client RENEW/REBIND logic to be compliant with RFC2131.
  - Improved declined addresses management in DHCPv4 server, which now can be
    reused after configured time.
  - Fixed including the client ID option in the DHCPv4 server response, according to RFC6842.
  - Added [`CONFIG_NET_DHCPV4_SERVER_NAK_UNRECOGNIZED_REQUESTS`](../kconfig.md#CONFIG_NET_DHCPV4_SERVER_NAK_UNRECOGNIZED_REQUESTS "CONFIG_NET_DHCPV4_SERVER_NAK_UNRECOGNIZED_REQUESTS") which
    allows to override RFC-defined behavior, and NAK requests from unrecognized
    clients.
  - Fixed client ID generation in DHCPv4 server.
  - Other minor fixes in DHCPv4 client and server implementations.
- DHCPv6:

  - Fixed incorrect DHCPv6 events code base for net\_mgmt events.
  - Added [`CONFIG_NET_DHCPV6_DUID_MAX_LEN`](../kconfig.md#CONFIG_NET_DHCPV6_DUID_MAX_LEN "CONFIG_NET_DHCPV6_DUID_MAX_LEN") which allows to configure
    maximum supported DUID length.
  - Added documentation page for DHCPv6.
- DNS/mDNS/LLMNR:

  - Fixed an issue where the mDNS Responder did not work when the mDNS Resolver was also enabled.
    The mDNS Resolver and mDNS Responder can now be used simultaneously.
  - Reworked LLMNR and mDNS responders, and DNS resolver to use sockets and socket services API.
  - Added ANY query resource type.
  - Added support for mDNS to provide records in runtime.
  - Added support for caching DNS records.
  - Fixed error codes returned when socket creation fails, and when all results have been returned.
  - Fixed DNS retransmission timeout calculation.
- gPTP/PTP:

  - Added support for IEEE 1588-2019 PTP.
  - Added support for SO\_TIMESTAMPING socket option to get timestamping information in socket
    ancillary data.
  - Fixed race condition on timestamp callback.
  - Fixed clock master sync send SM if we are not the GM clock.
- HTTP:

  - Added HTTP/2 server library and sample application with support for static,
    dynamic and Websocket resource types.
  - Added HTTP shell component.
  - Improved HTTP client error reporting.
  - Moved HTTP client library out of experimental.
  - Added POLLOUT monitoring when sending response in HTTP client.
- IPSP:

  - Removed IPSP support. `CONFIG_NET_L2_BT` does not exist anymore.
- IPv4:

  - Implemented IPv4 Address Conflict Detection, according to RFC 5227.
  - Added [`net_ipv4_is_private_addr()`](../doxygen/html/group__ip__4__6.md#ga6f19cb74de130d70668599c05a5ed66b) API function.
  - IPv4 netmask is now set individually for each address instead of being set
    for the whole interface.
  - Other minor fixes and improvements.
- IPv6:

  - Implemented IPv6 Privacy Extensions according to RFC 8981.
  - Added [`net_ipv6_is_private_addr()`](../doxygen/html/group__ip__4__6.md#gad35da6e137d62231052dda63c68b7eff) API function.
  - Implemented reachability hint for IPv6. Upper layers can use
    [`net_if_nbr_reachability_hint()`](../doxygen/html/group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5) to report Neighbor reachability and
    avoid unnecessary Neighbor Discovery solicitations.
  - Added [`CONFIG_NET_IPV6_MTU`](../kconfig.md#CONFIG_NET_IPV6_MTU "CONFIG_NET_IPV6_MTU") allowing to set custom IPv6 MTU.
  - Added [`CONFIG_NET_MCAST_ROUTE_MAX_IFACES`](../kconfig.md#CONFIG_NET_MCAST_ROUTE_MAX_IFACES "CONFIG_NET_MCAST_ROUTE_MAX_IFACES") which allows to set
    multiple interfaces for multicast forwarding entries.
  - Added [`CONFIG_NET_MCAST_ROUTE_MLD_REPORTS`](../kconfig.md#CONFIG_NET_MCAST_ROUTE_MLD_REPORTS "CONFIG_NET_MCAST_ROUTE_MLD_REPORTS") which allows to
    report multicast routes in MLDv2 reports.
  - Fixed IPv6 hop limit handling for multicast packets.
  - Improved IPv6 Neighbor Discovery test coverage.
  - Fixed a bug, where Neighbor Advertisement packets reporting Duplicate address
    detection conflicts were dropped.
  - Other minor fixes and improvements.
- LwM2M:

  - Added new API functions:

    - [`lwm2m_set_bulk()`](../doxygen/html/group__lwm2m__api.md#ga41b673986e11748b2ded8e1f8f05e0a7)
    - `lwm2m_rd_client_set_ctx()`
  - Added new `offset` parameter to [`lwm2m_engine_set_data_cb_t`](../doxygen/html/group__lwm2m__api.md#ga3afac013b0cf731f9c86dc3791131585) callback type.
    This affects post write and validate callbacks as well as some firmware callbacks.
  - Fixed block context not being reset upon receiving block number 0 in block transfer.
  - Fixed block size negotiation with the server in block transfer.
  - Added [`CONFIG_LWM2M_ENGINE_ALWAYS_REPORT_OBJ_VERSION`](../kconfig.md#CONFIG_LWM2M_ENGINE_ALWAYS_REPORT_OBJ_VERSION "CONFIG_LWM2M_ENGINE_ALWAYS_REPORT_OBJ_VERSION") which
    allows to force the client to always report object version.
  - Block transfer is now possible with resource w/o registered callback.
  - Fixed a bug, where an empty ACK sent from the registered callback would not
    be sent immediately.
  - Removed deprecated API functions and definitions.
  - Other minor fixes and improvements.
- Misc:

  - Improved overall networking API Doxygen documentation.
  - Converted TFTP library to use `zsock_*` API.
  - Added SNTP [`sntp_simple_addr()`](../doxygen/html/group__sntp.md#ga75aaee9a8f8490c0cc826a0e9298cd88) API function to perform SNTP query
    when the server IP address is already known.
  - Added [`CONFIG_NET_TC_THREAD_PRIO_CUSTOM`](../kconfig.md#CONFIG_NET_TC_THREAD_PRIO_CUSTOM "CONFIG_NET_TC_THREAD_PRIO_CUSTOM") allowing to override
    default traffic class threads priority.
  - Fixed the IPv6 event handler initialization order in net config library.
  - Reworked telnet shell backend to use sockets and socket services API.
  - Fixed double dereference of IGMP packets.
  - Moved from `native_posix` to `native_sim` support in various tests and
    samples.
  - Added support for copying user data in network buffers.
  - Fixed cloning of zero sized network buffers.
  - Added net\_buf APIs to handle 40 bit data format.
  - Added receive callback for dummy L2, applicable in certain use cases
    (for example, packet capture).
  - Implemented pseudo interface, a.k.a “any” interface for packet capture use
    case.
  - Added cooked mode capture support. This allows non-IP based network data capture.
  - Generate network events when starting or stopping packet capture.
  - Removed obsolete and unused `tcp_first_msg` [`net_pkt`](../doxygen/html/structnet__pkt.md) flag.
  - Added new [Secure MQTT Sensor/Actuator](../samples/net/secure_mqtt_sensor_actuator/README.md#secure-mqtt-sensor-actuator "Implement an MQTT-based IoT sensor/actuator device") sample.
  - Added support for partial L3 and L4 checksum offloading.
  - Updated [Microsoft Azure IoT Hub MQTT](../samples/net/cloud/mqtt_azure/README.md#mqtt-azure "Connect to Azure IoT Hub and publish messages using MQTT.") with new CA certificates, the current
    on expires soon.
  - Added new driver for Native Simulator offloaded sockets.
  - Overhauled VLAN support to use Virtual network interfaces.
  - Added statistics collection for Virtual network interfaces.
  - Fixed system workqueue block in `mgmt_event_work_handler()`
    when [`CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE`](../kconfig.md#CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE "CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE") is enabled.
- MQTT:

  - Added ALPN support for MQTT TLS backend.
  - Added user data field in [`mqtt_client`](../doxygen/html/structmqtt__client.md) context structure.
  - Fixed a potential socket leak in MQTT Websockets transport.
- Network Interface:

  - Added new API functions:

    - [`net_if_ipv4_maddr_foreach()`](../doxygen/html/group__net__if.md#gae82f53c670f602e9c37b65abb6dfaec7)
    - [`net_if_ipv6_maddr_foreach()`](../doxygen/html/group__net__if.md#gab677496fb2e27be2df299a346e9c7132)
  - Improved debug logging in the network interface code.
  - Added reference counter to the [`net_if_addr`](../doxygen/html/structnet__if__addr.md) structure.
  - Fixed IPv6 DAD and MLDv2 operation when interface goes up.
  - Added unique default name for OpenThread interfaces.
  - Other minor fixes.
- OpenThread

  - Removed deprecated `openthread_set_state_changed_cb()` function.
  - Added implementation of BLE TCAT advertisement API.
- PPP

  - Removed deprecated `gsm_modem` driver and sample.
  - Optimized memory allocation in PPP driver.
  - Misc improvements in the [Cellular modem](../samples/net/cellular_modem/README.md#cellular-modem "Use a cellular modem to communicate with a UDP server.") sample
  - Added PPP low level packet capture support.
- Shell:

  - Added `net ipv4 gateway` command to set IPv4 gateway address.
  - Added argument validation in network shell macros.
  - Fixed net\_mgmt sockets information printout.
  - Reworked VLAN information printout.
  - Added option to set random MAC address with `net iface set_mac` command.
  - Added multicast join status when printing multicast address information.
- Sockets:

  - Implemented new networking POSIX APIs:

    - [`if_nameindex()`](../doxygen/html/if_8h.md#aadc0427486b1b97fa250760e8ccd4f7f)
    - [`inet_ntoa()`](../doxygen/html/inet_8h.md#ab1d195e3682f88d1cea726e8c1de08d2)
    - [`inet_addr()`](../doxygen/html/inet_8h.md#a3e3b8f43e05dc3b87977b6a7a2ed09ca)
  - Added support for tracing socket API calls.
  - TLS sockets are no longer experimental API.
  - Fixed the protocol field endianness for `AF_PACKET` type sockets.
  - Fixed [`getsockname()`](../doxygen/html/posix_2sys_2socket_8h.md#abef44fb98f476ef2adba92bbdb362a1b) for TCP.
  - Improve [`sendmsg()`](../doxygen/html/posix_2sys_2socket_8h.md#a8a2ad4261d3978ba299926f45d56ed74) support when using DTLS sockets.
  - Fixed [`net_socket_service_register()`](../doxygen/html/group__bsd__socket__service.md#gaa72bb82aa413b711e61eda092504b091) function stall in case socket
    services thread stopped.
  - Fixed potential socket services thread stoppage when deregistering service.
  - Removed support for asynchronous timeouts in socket services library.
  - Fixed potential busy looping when using [`zsock_accept()`](../doxygen/html/group__bsd__sockets.md#ga25c993772f26b872e7ed16c4ae2349fb) in case of
    file descriptors shortage.
- Syslog:

  - Added new API functions:

    - [`log_backend_net_set_ip()`](../doxygen/html/log__backend__net_8h.md#aae909fb9ee8e4dbd773f44a2666dfa3a) to initialize syslog net backend with IP
      address directly.
    - [`log_backend_net_start()`](../doxygen/html/log__backend__net_8h.md#aab57f963e8a9e88b1e9483872e737466) to facilitate syslog net backend activation.
  - Added structured logging support to syslog net backend.
  - Added TCP support to syslog net backend.
- TCP:

  - Fixed possible deadlock when accepting new TCP connection.
  - Fixed ACK number verification during connection teardown.
  - Fixed a bug, where data bytes included in FIN packet were ignored.
  - Fixed a possible TCP context leak in case initial SYN packet transmission failed.
  - Deprecated `CONFIG_NET_TCP_ACK_TIMEOUT` as it was redundant with other configs.
  - Improved debug logs, so that they’re easier to follow under heavy load.
  - ISN generation now uses SHA-256 instead of MD5. Moreover, it now relies on PSA APIs
    instead of legacy Mbed TLS functions for hash computation.
  - Improved ACK reply logic in case no PSH flag is present to reduce redundant ACKs.
- Websocket:

  - Added new Websocket APIs:

    - [`websocket_register()`](../doxygen/html/group__websocket.md#gabc2556e62f001f8109bf6ae9f50f3952)
    - [`websocket_unregister()`](../doxygen/html/group__websocket.md#gaa3131d2599c8c69ab95c55c2e38e28e0)
  - Converted Websocket library to use `zsock_*` API.
  - Added Object Core support to Websocket sockets.
  - Added POLLOUT monitoring when sending.
- Wi-Fi:

  - Reduce memory usage of 5 GHz channel list.
  - Added channel validity check in AP mode.
  - Added support for BSSID configuration in connect call.
  - Wifi shell help text fixes. Option parsing fixes.
  - Support WPA auto personal security mode.
  - Collect unicast received/sent network packet statistics.
  - Added support for configuring RTS threshold. With this, users can set the RTS threshold
    value or disable the RTS mechanism.
  - Added support for configuring AP parameters. With this, users can set AP parameters at
    build and run time.
  - Added support to configure `max_inactivity` BSS parameter. Users can set this both
    build and runtime duration to control the maximum time duration after which AP may
    disconnect a STA due to inactivity from STA.
  - Added support to configure `inactivity_poll` BSS parameter. Users can set build
    only AP parameter to control whether AP may poll the STA before throwing away STA
    due to inactivity.
  - Added support to configure `max_num_sta` BSS parameter. Users can set this both
    build and run time parameter to control the maximum number of STA entries.
- zperf:

  - Fixed `IP_TOS` and `IPV6_TCLASS` options handling in zperf.
  - Fixed throughput calculation during long zperf sessions.
  - Fixed error on TCP upload session end in case multicast IP address was used.
  - Fixed a bug, where IPv6 socket was bound with IPv4 address, giving error.
  - Added an option to specify the network interface to use during zperf sessions.
  - Added a new `ZPERF_SESSION_PERIODIC_RESULT` event for periodic updates
    during TCP upload sessions.
  - Fixed possible socket leak in case of errors during zperf session.
  - Improved performance in the default configuration for the zperf sample.

## USB

- New USB device stack:

  - Added support for HID devices
  - Introduced speed-specific configurations and made high-speed support
    compliant with the USB2.0 specification
  - Added notification support and initial BOS support

## Devicetree

- Added [`DT_INST_NODE_HAS_COMPAT`](../doxygen/html/group__devicetree-inst.md#gaf88c7dc0e935ad7097e317e54c362ba0) to check if a node has a compatible.
  This is useful for nodes that have multiple compatibles.
- Added [`DT_CHILD_NUM`](../doxygen/html/group__devicetree-generic-id.md#ga37cf660c2a7a844f70191d21b6543dc1) and variants to count the number of children of a node.
- Added [`DT_FOREACH_NODELABEL`](../doxygen/html/group__devicetree-generic-foreach.md#gad5585436896efc4c5154a93b5980d3b0) and variants, which can be used to iterate over the
  node labels of a devicetree node.
- Added [`DT_NODELABEL_STRING_ARRAY`](../doxygen/html/group__devicetree-generic-id.md#ga0114cbfa3a2075558769d4632b7bb1e9) and [`DT_NUM_NODELABELS`](../doxygen/html/group__devicetree-interrupts-prop.md#ga7b63eb05db40d7b95ccb62a9fd1f4404) and their variants.
- Added [`DT_REG_HAS_NAME`](../doxygen/html/group__devicetree-reg-prop.md#ga2c68672c60d95725b69371c3ab306d24) and variants.
- Reworked [`DT_ANY_INST_HAS_PROP_STATUS_OKAY`](../doxygen/html/group__devicetree-inst.md#gaf2a45df474090b0403dffe1b7b82b735) so that the result can
  be used with macros like [`IS_ENABLED`](../doxygen/html/group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a), IF\_ENABLED, or COND\_CODE\_x.
- Reworked [`DT_NODE_HAS_COMPAT_STATUS`](../doxygen/html/group__devicetree-generic-exist.md#ga9bf6258fbeb0c5cd1fd15b9c9be9228a) so that it can be evaluated at preprocessor time.
- Updated PyYaml version used in dts scripts to 6.0 to remove supply chain vulnerabilities.

## Kconfig

- Added a `substring` Kconfig preprocessor function.
- Added a `dt_node_ph_prop_path` Kconfig preprocessor function.
- Added a `dt_compat_any_has_prop` Kconfig preprocessor function.

## Libraries / Subsystems

- Debug

  - symtab
  > - By enabling [`CONFIG_SYMTAB`](../kconfig.md#CONFIG_SYMTAB "CONFIG_SYMTAB"), the symbol table will be
  >   generated with Zephyr link stage executable on supported architectures.
- Demand Paging

  - NRU (Not Recently Used) eviction algorithm has updated its selection logic to avoid
    picking the same page to evict constantly. The updated login now searches for a new
    candidate linearly after the last evicted page.
  - Added LRU (Least Recently Used) eviction algorithm.
- Formatted output

  - Fix warning when compiling cbprintf with ARCMWDT.
- Management

  - hawkBit

    - The hawkBit subsystem has been reworked to use the settings subsystem to store the hawkBit
      configuration.
    - By enabling [`CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME`](../kconfig.md#CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME "CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME"), the hawkBit settings can
      be configured at runtime. Use the [`hawkbit_set_config()`](../doxygen/html/group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6) function to set the hawkBit
      configuration. It can also be set via the hawkBit shell, by using the `hawkbit set`
      command.
    - When using the hawkBit autohandler and an update is installed, the device will now
      automatically reboot after the installation is complete.
    - By enabling [`CONFIG_HAWKBIT_CUSTOM_DEVICE_ID`](../kconfig.md#CONFIG_HAWKBIT_CUSTOM_DEVICE_ID "CONFIG_HAWKBIT_CUSTOM_DEVICE_ID"), a callback function can be
      registered to set the device ID. Use the [`hawkbit_set_device_identity_cb()`](../doxygen/html/group__hawkbit.md#ga4ce085b8f2bb46af2c2e9f3f2879d633) function to
      register the callback.
    - By enabling [`CONFIG_HAWKBIT_CUSTOM_ATTRIBUTES`](../kconfig.md#CONFIG_HAWKBIT_CUSTOM_ATTRIBUTES "CONFIG_HAWKBIT_CUSTOM_ATTRIBUTES"), a callback function can be
      registered to set the device attributes that are sent to the hawkBit server. Use the
      [`hawkbit_set_custom_data_cb()`](../doxygen/html/group__hawkbit.md#gad8e83255a969eb61244b1edfd0b95e5d) function to register the callback.
  - MCUmgr

    - Instructions for the deprecated mcumgr go tool have been removed, a list of alternative,
      supported clients can be found on [Tools/libraries](../services/device_mgmt/mcumgr.md#mcumgr-tools-libraries).
    - Fixed an issue with the SMP structure not being packed which would cause a fault on devices
      that do not support unaligned memory accesses.
    - Added [`CONFIG_MCUMGR_TRANSPORT_BT_DYNAMIC_SVC_REGISTRATION`](../kconfig.md#CONFIG_MCUMGR_TRANSPORT_BT_DYNAMIC_SVC_REGISTRATION "CONFIG_MCUMGR_TRANSPORT_BT_DYNAMIC_SVC_REGISTRATION") that allows users
      to select whether MCUmgr BT service is statically registered at compile time or
      dynamically at run time.
    - In FS group, TinyCrypt has been replaced with PSA calls for SHA calculation.
- Logging

  - By enabling [`CONFIG_LOG_BACKEND_NET_USE_DHCPV4_OPTION`](../kconfig.md#CONFIG_LOG_BACKEND_NET_USE_DHCPV4_OPTION "CONFIG_LOG_BACKEND_NET_USE_DHCPV4_OPTION"), the IP address of the
    syslog server for the networking backend is set by the DHCPv4 Log Server Option (7).
  - Use real time clock as timestamp on POSIX.
  - Add support for syslog (POSIX).
  - Add [`LOG_WRN_ONCE`](../doxygen/html/group__log__api.md#gaa9b22a7d4659030d9a3273f1f1e6786c) for logging warning message where only the first occurrence is
    logged.
  - Add [`log_thread_trigger()`](../doxygen/html/group__log__ctrl.md#ga173eff0a07bbd1fc2978a1a705cae1fb) for triggering processing of the log messages.
  - Fix case when deferred logging not compiling when [`CONFIG_MULTITHREADING`](../kconfig.md#CONFIG_MULTITHREADING "CONFIG_MULTITHREADING") was
    disabled.
  - Fix case when logging strings could be stripped from the binary when dictionary based logging
    was mixed with non-dictionary.
  - Fix dictionary database not being generated in certain situations.
  - Fix dictionary logging parser not handling long long arguments correctly.
  - Fix support for [`CONFIG_LOG_MSG_APPEND_RO_STRING_LOC`](../kconfig.md#CONFIG_LOG_MSG_APPEND_RO_STRING_LOC "CONFIG_LOG_MSG_APPEND_RO_STRING_LOC").
- Modem modules

  - Added modem pipelink module which shares modem pipes globally, allowing device drivers to
    create and set up pipes for the application to use.
  - Simplified the modem pipe module’s synchronization mechanism to only protect the callback
    and user data. This matches the actual in-tree usage of the modem pipes.
  - Added `modem_stats` module which tracks the usage of buffers throughout the modem
    subsystem.
- Power management

  - Devices can now declare which system power states cause power loss.
    This information can be used to set and release power state
    constraints when it is needed by the device. This feature is enabled with
    [`CONFIG_PM_POLICY_DEVICE_CONSTRAINTS`](../kconfig.md#CONFIG_PM_POLICY_DEVICE_CONSTRAINTS "CONFIG_PM_POLICY_DEVICE_CONSTRAINTS"). Use functions
    [`pm_policy_device_power_lock_get()`](../doxygen/html/group__subsys__pm__sys__policy.md#ga708b7d2f8cb5f09738e3c6e5937c475e) and [`pm_policy_device_power_lock_put()`](../doxygen/html/group__subsys__pm__sys__policy.md#gafb90036c42bce2cc44466427b2907a81)
    to lock and unlock all power states that cause power loss in a device.
  - Added shell support for device power management.
  - Device power management was de-coupled from system power management. The new
    [`CONFIG_PM_DEVICE_SYSTEM_MANAGED`](../kconfig.md#CONFIG_PM_DEVICE_SYSTEM_MANAGED "CONFIG_PM_DEVICE_SYSTEM_MANAGED") option is used to enable
    whether devices must be suspended when the system sleeps.
  - Make it possible to disable system device power management individually per
    power state using `zephyr,pm-device-disabled`. This allows targets tuning which
    states should (and which should not) trigger device power management.
- Crypto

  - TinyCrypt remains available but is now being phased out in favor
    of PSA Crypto for enhanced security and performance.
  - Mbed TLS was updated to 3.6.0. Release notes can be found at:
    [https://github.com/Mbed-TLS/mbedtls/releases/tag/v3.6.0](https://github.com/Mbed-TLS/mbedtls/releases/tag/v3.6.0)
  - When any PSA crypto provider is available in the system
    (`CONFIG_MBEDTLS_PSA_CRYPTO_CLIENT` is enabled), desired PSA features
    must now be explicitly selected through `CONFIG_PSA_WANT_xxx` symbols.
  - Choice symbols [`CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG`](../kconfig.md#CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG "CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG") and
    [`CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG`](../kconfig.md#CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG "CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG") were added in order
    to allow the user to specify how Mbed TLS PSA crypto core should generate random numbers.
    The former option, which is the default, relies on legacy entropy and CTR\_DRBG/HMAC\_DRBG
    modules, while the latter relies on CSPRNG drivers.
  - [`CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED`](../kconfig.md#CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED "CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED") enables support
    for the Mbed TLS’s p256-m driver PSA crypto library. This is a Cortex-M SW
    optimized implementation of secp256r1 curve.
- CMSIS-NN

  - CMSIS-NN was updated to v6.0.0 from v4.1.0:
    [https://arm-software.github.io/CMSIS-NN/latest/rev\_hist.html](https://arm-software.github.io/CMSIS-NN/latest/rev_hist.html)
- FPGA

  - Improve handling of drivers missing `reset`, `load`, `get_status`, and `get_info`
    methods.
  - Add support for Agilex and Agilex 5.
- Random

  - Besides the existing [`sys_rand32_get()`](../doxygen/html/group__random__api.md#ga62cb24a6049b7aa9d03d66786e4a4db6) function, [`sys_rand8_get()`](../doxygen/html/group__random__api.md#ga810eaca8c5f71c9417d87f05c8fa4ebb),
    [`sys_rand16_get()`](../doxygen/html/group__random__api.md#ga27581a2b65faa6f1f3978ad6794300ba) and [`sys_rand64_get()`](../doxygen/html/group__random__api.md#ga26da47b7d5a76475b2fc528f5d6eced6) are now also available.
    These functions are all implemented on top of [`sys_rand_get()`](../doxygen/html/group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7).
- SD

  - SDMMC and SDIO frequency and timing selection logic have been reworked,
    to resolve an issue where a timing mode would not be selected if the
    SDHC device in use did not report support for the maximum frequency
    possible in that mode. Now, if the host controller and card both report
    support for a given timing mode but not the highest frequency that
    mode supports, the timing mode will be selected and configured at
    the reduced frequency ([GitHub #72705](https://github.com/zephyrproject-rtos/zephyr/issues/72705)).
- State Machine Framework

  - The [`SMF_CREATE_STATE`](../doxygen/html/group__smf.md#ga5760b98a36ed1ac55eba700cf44c7e1e) macro now always takes 5 arguments.
  - Transition sources that are parents of the state that was run now choose the correct Least
    Common Ancestor for executing Exit and Entry Actions.
  - Passing `NULL` to [`smf_set_state()`](../doxygen/html/group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb) is now not allowed.
- Storage

  - FAT FS: It is now possible to expose file system formatting functionality for FAT without also
    enabling automatic formatting on mount failure by setting the
    [`CONFIG_FS_FATFS_MKFS`](../kconfig.md#CONFIG_FS_FATFS_MKFS "CONFIG_FS_FATFS_MKFS") Kconfig option. This option is enabled by default if
    [`CONFIG_FILE_SYSTEM_MKFS`](../kconfig.md#CONFIG_FILE_SYSTEM_MKFS "CONFIG_FILE_SYSTEM_MKFS") is set.
  - FS: It is now possible to truncate a file while opening using [`fs_open()`](../doxygen/html/group__file__system__api.md#ga9c90031ba3e5a10da8e00e81d53ef63b)
    and by passing `FS_O_TRUNC` flag.
  - Flash Map: TinyCrypt has been replaced with PSA Crypto in Flash Area integrity check.
  - Flash Map: [`flash_area_flatten()`](../doxygen/html/group__flash__area__api.md#gafd097d05f5bfe91695bc7793e82cabcd) has been added to be used where an erase
    operation has been previously used for removing/scrambling data rather than
    to prepare a device for a random data write.
  - Flash Map: [`FIXED_PARTITION_NODE_OFFSET`](../doxygen/html/group__flash__area__api.md#gaf26b80f089d25283c01ed54b5a27988c), [`FIXED_PARTITION_NODE_SIZE`](../doxygen/html/group__flash__area__api.md#ga526459438c6de09abb727585d22b7004)
    and [`FIXED_PARTITION_NODE_DEVICE`](../doxygen/html/group__flash__area__api.md#gad64fb220f82870acce62661bfa94991a) have been added to allow obtaining
    fixed partition information from a devicetree node rather than a label.
  - Added [`CONFIG_NVS_DATA_CRC`](../kconfig.md#CONFIG_NVS_DATA_CRC "CONFIG_NVS_DATA_CRC"), to add CRC protection for data.
    Note that enabling this option makes NVS incompatible with existing storage
    that have not been previously using CRC on data.
  - Fixed NVS issue where [`nvs_calc_free_space()`](../doxygen/html/group__nvs__high__level__api.md#ga37e5a55f0b9209c7c0c95db9e1e84715) would return larger
    size than available, because space for reserved ate was not subtracted.
  - Fixed ext2 incorrectly calculating free space when attempting to format
    partition.
  - Fixed FAT driver leaving disk in initialized state after unmount.
- Task Watchdog

  - Added shell (mainly for testing purposes during development).
- POSIX API

  - Improved Kconfig options to reflect standard POSIX Options and Option Groups.
  - Added support for the following Option Groups

    - [POSIX\_MAPPED\_FILES](../services/portability/posix/option_groups/index.md#posix-option-group-mapped-files)
    - [POSIX\_MEMORY\_PROTECTION](../services/portability/posix/option_groups/index.md#posix-option-group-memory-protection)
    - [POSIX\_NETWORKING](../services/portability/posix/option_groups/index.md#posix-option-group-networking)
    - [POSIX\_SINGLE\_PROCESS](../services/portability/posix/option_groups/index.md#posix-option-group-single-process)
    - [POSIX\_TIMERS](../services/portability/posix/option_groups/index.md#posix-option-group-timers)
    - [XSI\_SYSTEM\_LOGGING](../services/portability/posix/option_groups/index.md#posix-option-group-xsi-system-logging)
  - Added support for the following Options

    - [\_POSIX\_ASYNCHRONOUS\_IO](../services/portability/posix/option_groups/index.md#posix-option-asynchronous-io)
    - [\_POSIX\_CPUTIME](../services/portability/posix/option_groups/index.md#posix-option-cputime)
    - [\_POSIX\_FSYNC](../services/portability/posix/option_groups/index.md#posix-option-fsync)
    - [\_POSIX\_MEMLOCK](../services/portability/posix/option_groups/index.md#posix-option-memlock)
    - [\_POSIX\_MEMLOCK\_RANGE](../services/portability/posix/option_groups/index.md#posix-option-memlock-range)
    - [\_POSIX\_READER\_WRITER\_LOCKS](../services/portability/posix/option_groups/index.md#posix-option-reader-writer-locks)
    - [\_POSIX\_SHARED\_MEMORY\_OBJECTS](../services/portability/posix/option_groups/index.md#posix-shared-memory-objects)
    - [\_POSIX\_THREAD\_CPUTIME](../services/portability/posix/option_groups/index.md#posix-option-thread-cputime)
    - [\_POSIX\_THREAD\_PRIO\_PROTECT](../services/portability/posix/option_groups/index.md#posix-option-thread-prio-protect)
    - [\_POSIX\_THREAD\_PRIORITY\_SCHEDULING](../services/portability/posix/option_groups/index.md#posix-option-thread-priority-scheduling)
    - [\_XOPEN\_STREAMS](../services/portability/posix/option_groups/index.md#posix-option-xopen-streams)
  - Fixed eventfd `F_SETFL` handling to avoid overwriting internal flags.
  - Fixed thread stack address printed in debug message.
  - Fixed macro parameter usage in signal code.
- LoRa/LoRaWAN

  - Added the Fragmented Data Block Transport service, which can be enabled via
    [`CONFIG_LORAWAN_FRAG_TRANSPORT`](../kconfig.md#CONFIG_LORAWAN_FRAG_TRANSPORT "CONFIG_LORAWAN_FRAG_TRANSPORT"). In addition to the default fragment decoder
    implementation from Semtech, an in-tree implementation with reduced memory footprint is
    available.
  - Added a sample to demonstrate LoRaWAN firmware-upgrade over the air (FUOTA).
- ZBus

  - Improved the VDED process by optimizing the channel reference copying for the clones delivered
    during the message subscriber delivery notification.
  - Improved the initialization phase by statically initiating the semaphores and runtime observer
    list. That decreased the duration of the zbus initialization.
  - Added a way of isolating a channel message subscribers pool. Some channels can now share an
    isolated pool to avoid delivery failures and shorten communication latency. It is only necessary
    to enable the [`CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION`](../kconfig.md#CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION "CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION") and use the
    function [`zbus_chan_set_msg_sub_pool()`](../doxygen/html/group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357) to change the msg pool used by the channel.
    Channels can share the same message pool.

## HALs

- Nordic

  - Updated nrfx to version 3.5.0.
  - Added nRF Services (nrfs) library.
- STM32

  - Updated STM32F0 to cube version V1.11.5.
  - Updated STM32F3 to cube version V1.11.5.
  - Updated STM32F4 to cube version V1.28.0.
  - Updated STM32F7 to cube version V1.17.2.
  - Updated STM32G0 to cube version V1.6.2.
  - Updated STM32G4 to cube version V1.5.2.
  - Updated STM32H5 to cube version V1.2.0.
  - Updated STM32H7 to cube version V1.11.2.
  - Updated STM32L5 to cube version V1.5.1.
  - Updated STM32U5 to cube version V1.5.0.
  - Updated STM32WB to cube version V1.19.1.
  - Updated STM32WBA to cube version V1.3.1.
  - Added STM32H7R/S with cube version V1.0.0.
- ADI

  - Introduced the `hal_adi` module, which is a subset of the Maxim Software
    Development Kit (MSDK) that contains device header files and bare metal
    peripheral drivers ([GitHub #72391](https://github.com/zephyrproject-rtos/zephyr/issues/72391)).
- Espressif

  - Updated HAL to version v5.1, which has new SoCs low-level files.

## MCUboot

> - Fixed memory leak in bootutil HKDF implementation
> - Fixed enforcing TLV entries to be protected
> - Fixed disabling instruction/data caches
> - Fixed estimated image overhead size calculation
> - Fixed issue with swap-move algorithm failing to validate multiple-images
> - Fixed align script error in imgtool
> - Fixed img verify for hex file format in imgtool
> - Fixed issue with reading the flash image reset vector
> - Fixed too-early `check_config.h` include in mbedtls
> - Refactored image dependency functions to reduce code size
> - Added MCUboot support for `ESP32-C6`
> - Added optional MCUboot boot banner
> - Added TLV querying for protected region
> - Added using builtin keys for verification in bootutil
> - Added builtin ECDSA key support for PSA Crypto backend
> - Added `OVERWRITE_ONLY_KEEP_BACKUP` option for secondary images
> - Added defines for `SOC_FLASH_0_ID` and `SPI_FLASH_0_ID`
> - Fixed ASN.1 support for mbedtls version >= 3.1
> - Fixed bootutil signed/unsigned comparison in `boot_read_enc_key`
> - Updated imgtool version.py to take command line arguments
> - Added imgtool improvements to dumpinfo
> - Fixed various imgtool dumpinfo issues
> - Fixed imgtool verify command for edcsa-p384 signed images
> - Added support for NXP MCXN947
> - The MCUboot version in this release is version `2.1.0+0-dev`.

## OSDP

- Fixed issue in CP secure channel handshake where R-MAC can be reverted to an
  old one by a rogue PD sending an out-of-order secure channel response resulting
  in a replay attack.

## Trusted Firmware-M

- TF-M was updated to 2.1.0. Release notes can be found at:
  [https://tf-m-user-guide.trustedfirmware.org/releases/2.1.0.html](https://tf-m-user-guide.trustedfirmware.org/releases/2.1.0.html)
- Support for MCUboot signature types other than RSA-3072 has been added.
  The type can be chosen with the [`CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE`](../kconfig.md#CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE "CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE") Kconfig option.
  Using EC-P256, the new default, reduces flash usage by several KBs compared to RSA.

## LVGL

LVGL was updated to 8.4.0. Release notes can be found at:
[https://docs.lvgl.io/8.4/CHANGELOG.html#v8-4-0-19-march-2024](https://docs.lvgl.io/8.4/CHANGELOG.html#v8-4-0-19-march-2024)

Additionally, the following changes in Zephyr were done:

> - Added support to place memory pool buffers in `.lvgl_heap` section by enabling
>   [`CONFIG_LV_Z_MEMORY_POOL_CUSTOM_SECTION`](../kconfig.md#CONFIG_LV_Z_MEMORY_POOL_CUSTOM_SECTION "CONFIG_LV_Z_MEMORY_POOL_CUSTOM_SECTION")
> - Removed kscan-based pointer input wrapper code.
> - Corrected encoder button behavior to emit `LV_KEY_ENTER` events correctly.
> - Improved handling for `invert-x,y` and `swap-xy` configurations.
> - Added `LV_MEM_CUSTOM_FREE` call on file closure.
> - Added missing Kconfig stubs for DMA2D symbols.
> - Integrated support for LVGL rounder callback function.

## Tests and Samples

> - Added snippet for easily enabling UART over Bluetooth LE by passing `-S nus-console` during
>   `west build`. This snippet sets the [`CONFIG_BT_ZEPHYR_NUS_AUTO_START_BLUETOOTH`](../kconfig.md#CONFIG_BT_ZEPHYR_NUS_AUTO_START_BLUETOOTH "CONFIG_BT_ZEPHYR_NUS_AUTO_START_BLUETOOTH")
>   which allows non-Bluetooth samples that use the UART APIs to run without modifications
>   (e.g.: Console and Logging examples).
> - Removed `GSM_PPP` specific configuration overlays from samples `net/cloud/tagoio` and
>   `net/mgmt/updatehub`. The `GSM_PPP` device driver has been deprecated and removed. The new
>   `MODEM_CELLULAR` device driver which replaces it uses the native networking stack and `PM`
>   subsystem, which like ethernet, requires no application specific actions to set up networking.
> - Removed `net/gsm_modem` sample as the `GSM_PPP` device driver it depended on has been
>   deprecated and removed. The sample has been replaced by the sample `net/cellular_modem`
>   based on the `MODEM_CELLULAR` device driver.
> - BT LE Coded PHY is now runtime tested in CI with the nrf5x bsim targets.
> - External ethernet network interfaces have been disabled in the `tests/net` tests, since these
>   tests are meant to use simulated network interfaces.

## Issue Related Items

### Known Issues

- [GitHub #74345](https://github.com/zephyrproject-rtos/zephyr/issues/74345) - Bluetooth: Non functional on nRF51 with fault
