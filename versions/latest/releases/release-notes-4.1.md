---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/releases/release-notes-4.1.html
original_path: releases/release-notes-4.1.html
---

# Zephyr 4.1.0

We are pleased to announce the release of Zephyr version 4.1.0.
Major enhancements with this release include:

**Performance improvements**
:   Multiple performance improvements of core Zephyr kernel functions have been implemented,
    benefiting all supported hardware architectures.

    An official port of the [thread\_metric ](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric) RTOS
    benchmark has also been added to make it easier for developers to measure the performance of
    Zephyr on their hardware and compare it to other RTOSes.

**Experimental support for IAR compiler**
:   [IAR Arm Toolchain](../develop/toolchains/iar_arm_toolchain.md#toolchain-iar-arm) can now be used to build Zephyr applications. This is an experimental
    feature that is expected to be improved in future releases.

**Initial support for Rust on Zephyr**
:   It is now possible to write Zephyr applications in Rust. [Rust Language Support](../develop/languages/rust/index.md#language-rust) is available through
    an optional Zephyr module, and several code samples are available as a starting point.

**USB MIDI Class Driver**
:   Introduction of a new [USB MIDI 2.0](../connectivity/usb/device_next/api/usbd_midi2.md#usbd-midi2) device driver, allowing Zephyr devices to
    communicate with MIDI controllers and instruments over USB.

**Expanded Board Support**
:   Support for 70 [new boards](#boards-added-in-zephyr-4-1) and 11
    [new shields](#shields-added-in-zephyr-4-1) has been added in this release.

    This includes highly popular boards such as [Raspberry Pi Pico 2](../boards/raspberrypi/rpi_pico2/doc/index.md#rpi_pico2) and
    [WCH CH32V003EVT](../boards/wch/ch32v003evt/doc/index.md#ch32v003evt), several boards with CAN+USB capabilities making them good candidates
    for running the Zephyr-based open source [CANnectivity](https://cannectivity.org/) firmware, and dozens of other boards
    across all supported architectures.

An overview of the changes required or recommended when migrating your application from Zephyr
v4.0.0 to Zephyr v4.1.0 can be found in the separate [migration guide](migration-guide-4.1.md#migration-4-1).

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

- [**CVE 2025-1673**](https://www.cve.org/CVERecord?id=CVE-2025-1673) [Zephyr project bug tracker GHSA-jjhx-rrh4-j8mx](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-jjhx-rrh4-j8mx)
- [**CVE 2025-1674**](https://www.cve.org/CVERecord?id=CVE-2025-1674) [Zephyr project bug tracker GHSA-x975-8pgf-qh66](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-x975-8pgf-qh66)
- [**CVE 2025-1675**](https://www.cve.org/CVERecord?id=CVE-2025-1675) [Zephyr project bug tracker GHSA-2m84-5hfw-m8v4](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-2m84-5hfw-m8v4)

## API Changes

### Removed APIs and options

- The legacy Bluetooth HCI driver API has been removed. It has been replaced
  by a [Bluetooth HCI APIs](../doxygen/html/group__bt__hci__api.md) that follows the normal Zephyr driver
  model.
- The `CAN_MAX_STD_ID` (replaced by [`CAN_STD_ID_MASK`](../doxygen/html/group__can__interface.md#ga4cd8ce34887b90baeeaa6a4aa048b398)) and
  `CAN_MAX_EXT_ID` (replaced by [`CAN_EXT_ID_MASK`](../doxygen/html/group__can__interface.md#ga15ee71e8abcf51008925585049125986)) CAN API macros
  have been removed.
- The `can_get_min_bitrate()` (replaced by [`can_get_bitrate_min()`](../doxygen/html/group__can__interface.md#ga343456749eec6144a91bacae0d94b114))
  and `can_get_max_bitrate()` (replaced by [`can_get_bitrate_max()`](../doxygen/html/group__can__interface.md#ga1e6dc8026e4d922bce4d398d9f32a457))
  CAN API functions have been removed.
- The `can_calc_prescaler()` CAN API function has been removed.
- The `CONFIG_NET_SOCKETS_POSIX_NAMES` option has been
  removed. It was a legacy option and was used to allow user to call BSD
  socket API while not enabling POSIX API. This removal means that in order
  to use POSIX API socket calls, one needs to enable the
  [`CONFIG_POSIX_API`](../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API") option. If the application does not want
  or is not able to enable that option, then the socket API calls need to be
  prefixed by a `zsock_` string.
- Removed `video_pix_fmt_bpp()` function that was returning a *byte* count
  and only supported 8-bit depth to [`video_bits_per_pixel()`](../doxygen/html/group__video__pixel__formats.md#gabdbd1b0f40af6663d81402deefdd387f) returning
  the *bit* count and supporting any color depth.
- The `video_stream_start()` and `video_stream_stop()` driver APIs have been
  replaced by `video_set_stream()`.
- `CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO`
- The `CONFIG_PM_DEVICE_RUNTIME_EXCLUSIVE` option has been removed
  after being deprecated in favor of [`CONFIG_PM_DEVICE_SYSTEM_MANAGED`](../kconfig.md#CONFIG_PM_DEVICE_SYSTEM_MANAGED "CONFIG_PM_DEVICE_SYSTEM_MANAGED").
- The `z_pm_save_idle_exit()` PM API function has been removed.
- Struct `z_arch_esf_t` has been removed. Use `struct arch_esf` instead.
- The following networking options have been removed:

  > - `CONFIG_NET_PKT_BUF_DATA_POOL_SIZE`
  > - `CONFIG_NET_TCP_ACK_TIMEOUT`

### Deprecated APIs and options

- the [`bt_le_set_auto_conn()`](../doxygen/html/group__bt__conn.md#ga8eea2211705d0691acc6ee4e0c37a47a) API function. Application developers can achieve
  the same functionality in their application code by reconnecting to the peer when the
  [`bt_conn_cb.disconnected`](../doxygen/html/structbt__conn__cb.md#a8b8983b5b5b05c9e2dae242485b6c914) callback is invoked.
- [`CONFIG_NATIVE_APPLICATION`](../kconfig.md#CONFIG_NATIVE_APPLICATION "CONFIG_NATIVE_APPLICATION") has been deprecated.
- Deprecated the [`stream_flash_erase_page()`](../doxygen/html/group__stream__flash.md#ga75711b22789724c2d8629e1202dcb48d) from Stream Flash API. The same functionality
  can be achieved using [`flash_area_erase()`](../doxygen/html/group__flash__area__api.md#gacc5cbff19d23773115f3334f862814d2) or [`flash_erase()`](../doxygen/html/group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95). Nevertheless
  erasing of a device, while stream flash is supposed to do so, as configured, will result in
  data lost from stream flash. There are only two situations where device should be erased
  directly:

  1. when Stream Flash is not configured to do erase on its own
  2. when erase is used for removal of a data prior or after Stream Flash uses the designated area.
- The pipe API has been reworked.
  The new API is enabled by default when `CONFIG_MULTITHREADING` is set.

  - Deprecates the `CONFIG_PIPES` Kconfig option.
  - Introduces the `k_pipe_close(..)` function.
  - `k_pipe_put(..)` translates to `k_pipe_write(..)`.
  - `k_pipe_get(..)` translates to `k_pipe_read(..)`.
  - `k_pipe_flush(..)` & `k_pipe_buffer_flush()` can be translated to `k_pipe_reset(..)`.
  - Dynamic allocation of pipes is no longer supported.

    - `k_pipe_alloc_init(..)` API has been removed.
    - `k_pipe_cleanup(..)` API has been removed.
  - Querying the number of bytes in the pipe is no longer supported.

    - `k_pipe_read_avail(..)` API has been removed.
    - `k_pipe_write_avail(..)` API has been removed.
- For the native\_sim target `CONFIG_NATIVE_SIM_NATIVE_POSIX_COMPAT` has been
  switched to `n` by default, and this option has been deprecated.
- [`CONFIG_BT_BUF_ACL_RX_COUNT`](../kconfig.md#CONFIG_BT_BUF_ACL_RX_COUNT "CONFIG_BT_BUF_ACL_RX_COUNT")
- All HWMv1 board name aliases which were added as deprecated in v3.7 are now removed
  ([GitHub #82247](https://github.com/zephyrproject-rtos/zephyr/issues/82247)).
- The TinyCrypt library has been deprecated as the upstream version is no longer maintained.
  PSA Crypto API is now the recommended cryptographic library for Zephyr.
- The [`CONFIG_BT_DIS_MODEL`](../kconfig.md#CONFIG_BT_DIS_MODEL "CONFIG_BT_DIS_MODEL") and [`CONFIG_BT_DIS_MANUF`](../kconfig.md#CONFIG_BT_DIS_MANUF "CONFIG_BT_DIS_MANUF") have been
  deprecated. Application developers can achieve the same configuration by using the new
  [`CONFIG_BT_DIS_MODEL_NUMBER_STR`](../kconfig.md#CONFIG_BT_DIS_MODEL_NUMBER_STR "CONFIG_BT_DIS_MODEL_NUMBER_STR") and
  [`CONFIG_BT_DIS_MANUF_NAME_STR`](../kconfig.md#CONFIG_BT_DIS_MANUF_NAME_STR "CONFIG_BT_DIS_MANUF_NAME_STR") Kconfig options.

### New APIs and options

- Architectures

  - [`CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL`](../kconfig.md#CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL "CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL")
  - [`CONFIG_RISCV_CURRENT_VIA_GP`](../kconfig.md#CONFIG_RISCV_CURRENT_VIA_GP "CONFIG_RISCV_CURRENT_VIA_GP")
- Bluetooth

  - Audio

    - [`bt_bap_broadcast_source_register_cb()`](../doxygen/html/group__bt__bap__broadcast__source.md#gac75ad00b8f9a1cd7048677a33b17acda)
    - [`bt_bap_broadcast_source_unregister_cb()`](../doxygen/html/group__bt__bap__broadcast__source.md#gacc8d26c42c6b4ae6dc11af84ec4af616)
    - [`bt_cap_commander_distribute_broadcast_code()`](../doxygen/html/group__bt__cap.md#gaf86582ad529b6ee801d1154db7e33827)
    - `bt_ccp` API (in progress)
    - [`bt_pacs_register()`](../doxygen/html/group__bt__pacs.md#gac77a3dd5015058145b51db5fef2c9485)
    - [`bt_pacs_unregister()`](../doxygen/html/group__bt__pacs.md#gac23d3c4e850394194871e8daaa44545b)
  - Host

    - [`bt_conn_is_type()`](../doxygen/html/group__bt__conn.md#gaf3d55f1f8efc630b495389ced3ee3fa5)
  - Mesh

    - [`bt_mesh_health_cli::update`](../doxygen/html/structbt__mesh__health__cli.md#ae1b396cb99a32a96762d4435629b1ba5) callback can be used to periodically update the message
      published by the Health Client.
  - Services

    - The [`CONFIG_BT_DIS_MODEL_NUMBER`](../kconfig.md#CONFIG_BT_DIS_MODEL_NUMBER "CONFIG_BT_DIS_MODEL_NUMBER") and
      [`CONFIG_BT_DIS_MANUF_NAME`](../kconfig.md#CONFIG_BT_DIS_MANUF_NAME "CONFIG_BT_DIS_MANUF_NAME") Kconfig options can be used to control the
      presence of the Model Number String and Manufacturer Name String characteristics inside
      the Device Information Service (DIS). The [`CONFIG_BT_DIS_MODEL_NUMBER_STR`](../kconfig.md#CONFIG_BT_DIS_MODEL_NUMBER_STR "CONFIG_BT_DIS_MODEL_NUMBER_STR")
      and [`CONFIG_BT_DIS_MANUF_NAME_STR`](../kconfig.md#CONFIG_BT_DIS_MANUF_NAME_STR "CONFIG_BT_DIS_MANUF_NAME_STR") Kconfig options are now used to set the
      string values in these characteristics. They replace the functionality of the deprecated
      [`CONFIG_BT_DIS_MODEL`](../kconfig.md#CONFIG_BT_DIS_MODEL "CONFIG_BT_DIS_MODEL") and [`CONFIG_BT_DIS_MANUF`](../kconfig.md#CONFIG_BT_DIS_MANUF "CONFIG_BT_DIS_MANUF") Kconfigs.
- Build system

  - Sysbuild

    - The newly introduced MCUboot swap using offset mode can be selected from sysbuild by using
      `SB_CONFIG_MCUBOOT_MODE_SWAP_USING_OFFSET`, this mode is experimental.
- Crypto

  - [`CONFIG_MBEDTLS_PSA_STATIC_KEY_SLOTS`](../kconfig.md#CONFIG_MBEDTLS_PSA_STATIC_KEY_SLOTS "CONFIG_MBEDTLS_PSA_STATIC_KEY_SLOTS")
  - [`CONFIG_MBEDTLS_PSA_KEY_SLOT_COUNT`](../kconfig.md#CONFIG_MBEDTLS_PSA_KEY_SLOT_COUNT "CONFIG_MBEDTLS_PSA_KEY_SLOT_COUNT")
- I3C

  - [`CONFIG_I3C_TARGET_BUFFER_MODE`](../kconfig.md#CONFIG_I3C_TARGET_BUFFER_MODE "CONFIG_I3C_TARGET_BUFFER_MODE")
  - [`CONFIG_I3C_RTIO`](../kconfig.md#CONFIG_I3C_RTIO "CONFIG_I3C_RTIO")
  - [`i3c_ibi_hj_response()`](../doxygen/html/group__i3c__ibi.md#gac8c77e43fc7c06701437e799739507ee)
  - [`i3c_ccc_do_getacccr()`](../doxygen/html/group__i3c__ccc.md#ga87c42055b8b03871558df6be56dc1bd6)
  - [`i3c_device_controller_handoff()`](../doxygen/html/group__i3c__interface.md#ga22857e3c19dbd5d93f3aed120fa32c84)
- Management

  - hawkBit

    - The hawkBit subsystem now uses the State Machine Framework internally.
    - [`CONFIG_HAWKBIT_TENANT`](../kconfig.md#CONFIG_HAWKBIT_TENANT "CONFIG_HAWKBIT_TENANT")
    - [`CONFIG_HAWKBIT_EVENT_CALLBACKS`](../kconfig.md#CONFIG_HAWKBIT_EVENT_CALLBACKS "CONFIG_HAWKBIT_EVENT_CALLBACKS")
    - [`CONFIG_HAWKBIT_SAVE_PROGRESS`](../kconfig.md#CONFIG_HAWKBIT_SAVE_PROGRESS "CONFIG_HAWKBIT_SAVE_PROGRESS")
  - MCUmgr

    - Image management `MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED` now has image data field
      [`img_mgmt_image_confirmed`](../doxygen/html/structimg__mgmt__image__confirmed.md).
- MCUboot

  - Signed hex files where an encryption key Kconfig is set now have the encrypted flag set in
    the image header.
- Networking:

  - CoAP

    - [`coap_client_cancel_request()`](../doxygen/html/group__coap__client.md#ga71abc48834df15e7550f7f9c75918117)
  - DHCP

    - [`CONFIG_NET_DHCPV4_SERVER_OPTION_ROUTER`](../kconfig.md#CONFIG_NET_DHCPV4_SERVER_OPTION_ROUTER "CONFIG_NET_DHCPV4_SERVER_OPTION_ROUTER")
    - [`CONFIG_NET_DHCPV4_OPTION_DNS_ADDRESS`](../kconfig.md#CONFIG_NET_DHCPV4_OPTION_DNS_ADDRESS "CONFIG_NET_DHCPV4_OPTION_DNS_ADDRESS")
    - [`CONFIG_NET_DHCPV6_OPTION_DNS_ADDRESS`](../kconfig.md#CONFIG_NET_DHCPV6_OPTION_DNS_ADDRESS "CONFIG_NET_DHCPV6_OPTION_DNS_ADDRESS")
  - DNS

    - [`CONFIG_MDNS_RESPONDER_PROBE`](../kconfig.md#CONFIG_MDNS_RESPONDER_PROBE "CONFIG_MDNS_RESPONDER_PROBE")
  - Ethernet

    - Allow user to specify protocol extensions when receiving data from Ethernet network.
      This makes it possible to register a handler for Ethernet protocol type without changing
      core Zephyr network code. `NET_L3_REGISTER`
    - [`CONFIG_NET_L2_ETHERNET_RESERVE_HEADER`](../kconfig.md#CONFIG_NET_L2_ETHERNET_RESERVE_HEADER "CONFIG_NET_L2_ETHERNET_RESERVE_HEADER")
  - HTTP

    - Extended [`HTTP_SERVICE_DEFINE`](../doxygen/html/group__http__service.md#ga1aa8efe3622b5c9421a6257140c5d2c5) to allow to specify a default
      fallback resource handler.
    - [`CONFIG_HTTP_SERVER_REPORT_FAILURE_REASON`](../kconfig.md#CONFIG_HTTP_SERVER_REPORT_FAILURE_REASON "CONFIG_HTTP_SERVER_REPORT_FAILURE_REASON")
    - [`CONFIG_HTTP_SERVER_TLS_USE_ALPN`](../kconfig.md#CONFIG_HTTP_SERVER_TLS_USE_ALPN "CONFIG_HTTP_SERVER_TLS_USE_ALPN")
  - IPv4

    - [`CONFIG_NET_IPV4_PMTU`](../kconfig.md#CONFIG_NET_IPV4_PMTU "CONFIG_NET_IPV4_PMTU")
  - IPv6

    - [`CONFIG_NET_IPV6_PMTU`](../kconfig.md#CONFIG_NET_IPV6_PMTU "CONFIG_NET_IPV6_PMTU")
  - LwM2M

    - [`lwm2m_pull_context_set_sockopt_callback()`](../doxygen/html/group__lwm2m__api.md#ga647018abc15cd65c894d9acb6c866486)
  - MQTT-SN

    - Added Gateway Advertisement and Discovery support:

      - [`mqtt_sn_add_gw()`](../doxygen/html/group__mqtt__sn__socket.md#gadd38840ebc78217a692748afb704b42b)
      - [`mqtt_sn_search()`](../doxygen/html/group__mqtt__sn__socket.md#gafdf80b1de5d1b069b2f75b2bd688416f)
  - OpenThread

    - [`CONFIG_OPENTHREAD_WAKEUP_COORDINATOR`](../kconfig.md#CONFIG_OPENTHREAD_WAKEUP_COORDINATOR "CONFIG_OPENTHREAD_WAKEUP_COORDINATOR")
    - [`CONFIG_OPENTHREAD_WAKEUP_END_DEVICE`](../kconfig.md#CONFIG_OPENTHREAD_WAKEUP_END_DEVICE "CONFIG_OPENTHREAD_WAKEUP_END_DEVICE")
    - [`CONFIG_OPENTHREAD_PLATFORM_MESSAGE_MANAGEMENT`](../kconfig.md#CONFIG_OPENTHREAD_PLATFORM_MESSAGE_MANAGEMENT "CONFIG_OPENTHREAD_PLATFORM_MESSAGE_MANAGEMENT")
    - [`CONFIG_OPENTHREAD_TCAT_MULTIRADIO_CAPABILITIES`](../kconfig.md#CONFIG_OPENTHREAD_TCAT_MULTIRADIO_CAPABILITIES "CONFIG_OPENTHREAD_TCAT_MULTIRADIO_CAPABILITIES")
  - Sockets

    - Added support for new socket options:

      - [`IP_LOCAL_PORT_RANGE`](../doxygen/html/group__bsd__sockets.md#gafca1e9e3b4ffeac402cb6e5bcca02dc9)
      - [`IP_MULTICAST_IF`](../doxygen/html/group__bsd__sockets.md#ga95ac9ecdbd7845274e20667d3b42cd00)
      - [`IPV6_MULTICAST_IF`](../doxygen/html/group__bsd__sockets.md#gafcc32c29ac8987b2ad69411d0384a0e5)
      - [`IP_MTU`](../doxygen/html/group__bsd__sockets.md#gaabb76515b6fbcb20c1220b35592ad642)
      - [`IPV6_MTU`](../doxygen/html/group__bsd__sockets.md#gab121a483673073b8f7cfa6ce80b57b03)
  - Other

    - [`CONFIG_NET_STATISTICS_VIA_PROMETHEUS`](../kconfig.md#CONFIG_NET_STATISTICS_VIA_PROMETHEUS "CONFIG_NET_STATISTICS_VIA_PROMETHEUS")
- Video

  - `video_set_stream()` driver API has replaced [`video_stream_start()`](../doxygen/html/group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0) and
    [`video_stream_stop()`](../doxygen/html/group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48) driver APIs.
- Other

  - [`CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA`](../kconfig.md#CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA "CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA")
  - [`DT_ANY_INST_HAS_BOOL_STATUS_OKAY`](../doxygen/html/group__devicetree-inst.md#gab3d2f48ad95c4e2af76eed5e34735b18)
  - [`led_dt_spec`](../doxygen/html/structled__dt__spec.md)
  - [`CONFIG_STEP_DIR_STEPPER`](../kconfig.md#CONFIG_STEP_DIR_STEPPER "CONFIG_STEP_DIR_STEPPER")

## New Boards

- Adafruit Industries, LLC

  > - [Feather M4 Express](../boards/adafruit/feather_m4_express/doc/index.md#adafruit_feather_m4_express) (`adafruit_feather_m4_express`)
  > - [Adafruit MacroPad RP2040](../boards/adafruit/macropad_rp2040/doc/index.md#adafruit_macropad_rp2040) (`adafruit_macropad_rp2040`)
  > - [QT Py ESP32-S3](../boards/adafruit/qt_py_esp32s3/doc/index.md#adafruit_qt_py_esp32s3) (`adafruit_qt_py_esp32s3`)
- Advanced Micro Devices (AMD), Inc.

  > - [ACP 6.0 Xtensa Audio DSP](../boards/amd/acp_6_0_adsp/doc/index.md#acp_6_0_adsp) (`acp_6_0_adsp`)
- Analog Devices, Inc.

  > - [AD-SWIOT1L-SL](../boards/adi/ad_swiot1l_sl/doc/index.md#ad_swiot1l_sl) (`ad_swiot1l_sl`)
  > - [MAX32650EVKIT](../boards/adi/max32650evkit/doc/index.md#max32650evkit) (`max32650evkit`)
  > - [MAX32650FTHR](../boards/adi/max32650fthr/doc/index.md#max32650fthr) (`max32650fthr`)
  > - [MAX32660EVSYS](../boards/adi/max32660evsys/doc/index.md#max32660evsys) (`max32660evsys`)
  > - [MAX78000EVKIT](../boards/adi/max78000evkit/doc/index.md#max78000evkit) (`max78000evkit`)
  > - [MAX78000FTHR](../boards/adi/max78000fthr/doc/index.md#max78000fthr) (`max78000fthr`)
  > - [MAX78002EVKIT](../boards/adi/max78002evkit/doc/index.md#max78002evkit) (`max78002evkit`)
- Antmicro

  > - [Myra SiP Baseboard](../boards/antmicro/myra_sip_baseboard/doc/index.md#myra_sip_baseboard) (`myra_sip_baseboard`)
- BeagleBoard.org Foundation

  > - [BeagleY-AI](../boards/beagle/beagley_ai/doc/index.md#beagley_ai) (`beagley_ai`)
- FANKE Technology Co., Ltd.

  > - [FK750M1-VBT6](../boards/fanke/fk750m1_vbt6/doc/index.md#fk750m1_vbt6) (`fk750m1_vbt6`)
- Google, Inc.

  > - [Icetower Development Board](../boards/google/icetower/doc/index.md#google_icetower) (`google_icetower`)
  > - [Quincy](../boards/google/quincy/doc/index.md#google_quincy) (`google_quincy`)
- Infineon Technologies

  > - [PSOC 6 AI Evaluation Kit](../boards/infineon/cy8ckit_062s2_ai/doc/index.md#cy8ckit_062s2_ai) (`cy8ckit_062s2_ai`)
- Khadas

  > - [Edge2](../boards/khadas/edge2/doc/index.md#khadas_edge2) (`khadas_edge2`)
- Lilygo Shenzhen Xinyuan Electronic Technology Co., Ltd

  > - [TTGO T7 Mini32 V1.5](../boards/lilygo/ttgo_t7v1_5/doc/index.md#ttgo_t7v1_5) (`ttgo_t7v1_5`)
  > - [TTGO T8-S3](../boards/lilygo/ttgo_t8s3/doc/index.md#ttgo_t8s3) (`ttgo_t8s3`)
- M5Stack

  > - [CoreS3](../boards/m5stack/m5stack_cores3/doc/index.md#m5stack_cores3) (`m5stack_cores3`)
- Makerbase Co., Ltd.

  > - [MKS CANable V2.0](../boards/makerbase/mks_canable_v20/doc/index.md#mks_canable_v20) (`mks_canable_v20`)
- MediaTek Inc.

  > - MT8186 (`mt8186`)
  > - MT8188 (`mt8188`)
  > - MT8196 (`mt8196`)
- NXP Semiconductors

  > - [FRDM-MCXW72](../boards/nxp/frdm_mcxw72/doc/index.md#frdm_mcxw72) (`frdm_mcxw72`)
  > - [i.MX91 EVK](../boards/nxp/imx91_evk/doc/index.md#imx91_evk) (`imx91_evk`)
  > - [MCXW72-EVK](../boards/nxp/mcxw72_evk/doc/index.md#mcxw72_evk) (`mcxw72_evk`)
  > - [MIMXRT700-EVK](../boards/nxp/mimxrt700_evk/doc/index.md#mimxrt700_evk) (`mimxrt700_evk`)
- Nordic Semiconductor

  > - [nRF54L09 PDK](../boards/nordic/nrf54l09pdk/doc/index.md#nrf54l09pdk) (`nrf54l09pdk`)
- Norik Systems

  > - [Octopus IO-Board](../boards/norik/octopus_io_board/doc/index.md#octopus_io_board) (`octopus_io_board`)
  > - [Octopus SoM](../boards/norik/octopus_som/doc/index.md#octopus_som) (`octopus_som`)
- Panasonic Corporation

  > - [PAN B511 Evaluation Board](../boards/panasonic/panb511evb/doc/index.md#panb511evb) (`panb511evb`)
- Peregrine Consultoria e Servicos

  > - [SAM4L WM-400 Cape Board](../boards/peregrine/sam4l_wm400_cape/doc/index.md#sam4l_wm400_cape) (`sam4l_wm400_cape`)
- Qorvo, Inc.

  > - [Decawave DWM3001CDK](../boards/qorvo/decawave_dwm3001cdk/doc/index.md#decawave_dwm3001cdk) (`decawave_dwm3001cdk`)
- RAKwireless Technology Limited

  > - [RAK3172](../boards/rakwireless/rak3172/doc/index.md#rak3172) (`rak3172`)
- Raspberry Pi Foundation

  > - [Raspberry Pi Pico 2](../boards/raspberrypi/rpi_pico2/doc/index.md#rpi_pico2) (`rpi_pico2`)
- Realtek Semiconductor Corp.

  > - [RTS5912 Evaluation Board](../boards/realtek/rts5912_evb/doc/index.md#rts5912_evb) (`rts5912_evb`)
- Renesas Electronics Corporation

  > - [ek\_ra2l1](../boards/renesas/ek_ra2l1/doc/index.md#ek_ra2l1) (`ek_ra2l1`)
  > - [RA4L1 Evaluation Kit](../boards/renesas/ek_ra4l1/doc/index.md#ek_ra4l1) (`ek_ra4l1`)
  > - [RA4M1 Evaluation Kit](../boards/renesas/ek_ra4m1/doc/index.md#ek_ra4m1) (`ek_ra4m1`)
  > - [RA4E1 Fast Prototyping Board](../boards/renesas/fpb_ra4e1/doc/index.md#fpb_ra4e1) (`fpb_ra4e1`)
  > - [RZ/G3S SMARC Evaluation Board Kit](../boards/renesas/rzg3s_smarc/doc/index.md#rzg3s_smarc) (`rzg3s_smarc`)
  > - [RA4E1 Voice User Reference Kit](../boards/renesas/voice_ra4e1/doc/index.md#voice_ra4e1) (`voice_ra4e1`)
- STMicroelectronics

  > - [Nucleo C071RB](../boards/st/nucleo_c071rb/doc/index.md#nucleo_c071rb) (`nucleo_c071rb`)
  > - [Nucleo F072RB](../boards/st/nucleo_f072rb/doc/index.md#nucleo_f072rb) (`nucleo_f072rb`)
  > - [Nucleo H7S3L8](../boards/st/nucleo_h7s3l8/doc/index.md#nucleo_h7s3l8) (`nucleo_h7s3l8`)
  > - [Nucleo N657X0-Q](../boards/st/nucleo_n657x0_q/doc/index.md#nucleo_n657x0_q) (`nucleo_n657x0_q`)
  > - [Nucleo WB07CC](../boards/st/nucleo_wb07cc/doc/index.md#nucleo_wb07cc) (`nucleo_wb07cc`)
  > - [STM32F413H Discovery](../boards/st/stm32f413h_disco/doc/index.md#stm32f413h_disco) (`stm32f413h_disco`)
  > - [STM32N6570-DK](../boards/st/stm32n6570_dk/doc/index.md#stm32n6570_dk) (`stm32n6570_dk`)
- Seeed Technology Co., Ltd

  > - [XIAO ESP32C6](../boards/seeed/xiao_esp32c6/doc/index.md#xiao_esp32c6) (`xiao_esp32c6`)
- Shenzhen Fuyuansheng Electronic Technology Co., Ltd.

  > - [UCAN](../boards/fysetc/ucan/doc/index.md#ucan) (`ucan`)
- Silicon Laboratories

  > - [SiWx917 Wi-Fi 6 and Bluetooth LE SoC 8 MB Flash Radio Board (SLWRB4338A)](../boards/silabs/radio_boards/siwx917_rb4338a/doc/index.md#siwx917_rb4338a) (`siwx917_rb4338a`)
  > - [EFR32xG23 868-915 MHz 20 dBm (xG23-RB4210A)](../boards/silabs/radio_boards/xg23_rb4210a/doc/index.md#xg23_rb4210a) (`xg23_rb4210a`)
  > - [EFR32xG24 Explorer Kit (xG24-EK2703A)](../boards/silabs/dev_kits/xg24_ek2703a/doc/index.md#xg24_ek2703a) (`xg24_ek2703a`)
  > - [EFR32xG29 2.4 GHz 8 dBm Buck (xG29-RB4412A)](../boards/silabs/radio_boards/xg29_rb4412a/doc/index.md#xg29_rb4412a) (`xg29_rb4412a`)
- Texas Instruments

  > - [CC2340R5 LaunchPad](../boards/ti/lp_em_cc2340r5/doc/index.md#lp_em_cc2340r5) (`lp_em_cc2340r5`)
- Toradex AG

  > - [Verdin iMX8M Mini](../boards/toradex/verdin_imx8mm/doc/index.md#verdin_imx8mm) (`verdin_imx8mm`)
- Waveshare Electronics

  > - [RP2040-Zero](../boards/waveshare/rp2040_zero/doc/index.md#rp2040_zero) (`rp2040_zero`)
- WeAct Studio

  > - [MiniSTM32H7B0 Core Board](../boards/weact/mini_stm32h7b0/doc/index.md#mini_stm32h7b0) (`mini_stm32h7b0`)
  > - [STM32H5 Core Board](../boards/weact/stm32h5_core/doc/index.md#weact_stm32h5_core) (`weact_stm32h5_core`)
- WinChipHead

  > - [WCH CH32V003EVT](../boards/wch/ch32v003evt/doc/index.md#ch32v003evt) (`ch32v003evt`)
- Würth Elektronik GmbH.

  > - [Oceanus-I EV](../boards/we/oceanus1ev/doc/index.md#we_oceanus1ev) (`we_oceanus1ev`)
  > - [Orthosie-I-EV](../boards/we/orthosie1ev/doc/index.md#we_orthosie1ev) (`we_orthosie1ev`)
- Others

  > - [CANbardo](../boards/others/canbardo/doc/index.md#canbardo) (`canbardo`)
  > - [candleLight](../boards/others/candlelight/doc/index.md#candlelight) (`candlelight`)
  > - [candleLightFD](../boards/others/candlelightfd/doc/index.md#candlelightfd) (`candlelightfd`)
  > - [ESP32-C3-SUPERMINI](../boards/others/esp32c3_supermini/doc/index.md#esp32c3_supermini) (`esp32c3_supermini`)
  > - [Pro Micro nRF52840](../boards/others/promicro_nrf52840/doc/index.md#promicro_nrf52840) (`promicro_nrf52840`)

### New shields

> - [Abrobot ESP32 C3 OLED Shield](../boards/shields/abrobot_esp32c3_oled/doc/index.md#abrobot-esp32c3oled-shield)
> - [Adafruit Adalogger Featherwing Shield](../boards/shields/adafruit_adalogger_featherwing/doc/index.md#adafruit-adalogger-featherwing-shield)
> - [Adafruit AW9523 GPIO Expander and LED Driver](../boards/shields/adafruit_aw9523/doc/index.md#adafruit-aw9523)
> - [MikroElektronika ETH 3 Click](../boards/shields/mikroe_eth3_click/doc/index.md#mikroe-eth3-click)
> - [P3T1755DP Arduino® Shield Evaluation Board](../boards/shields/p3t1755dp_ard_i2c/doc/index.md#p3t1755dp-ard-i2c-shield)
> - [P3T1755DP Arduino® Shield Evaluation Board](../boards/shields/p3t1755dp_ard_i3c/doc/index.md#p3t1755dp-ard-i3c-shield)
> - [Digilent Pmod SD](../boards/shields/pmod_sd/doc/index.md#pmod-sd)
> - [Renesas DA14531 Pmod Board](../boards/shields/renesas_us159_da14531evz/doc/index.md#renesas-us159-da14531evz-shield)
> - [RTKMIPILCDB00000BE MIPI Display](../boards/shields/rtkmipilcdb00000be/doc/index.md#rtkmipilcdb00000be)
> - [Seeed W5500 Ethernet Shield](../boards/shields/seeed_w5500/doc/index.md#seeed-w5500)
> - [ST B-CAMS-OMV-MB1683](../boards/shields/st_b_cams_omv_mb1683/doc/index.md#st-b-cams-omv-mb1683)

## New Drivers

- ADC

  > - [`adi,ad4114-adc`](../build/dts/api/bindings/adc/adi%2Cad4114-adc.md#std-dtcompatible-adi-ad4114-adc)
  > - [`adi,ad7124-adc`](../build/dts/api/bindings/adc/adi%2Cad7124-adc.md#std-dtcompatible-adi-ad7124-adc)
  > - [`st,stm32n6-adc`](../build/dts/api/bindings/adc/st%2Cstm32n6-adc.md#std-dtcompatible-st-stm32n6-adc)
  > - [`ti,ads114s06`](../build/dts/api/bindings/adc/ti%2Cads114s06.md#std-dtcompatible-ti-ads114s06)
  > - [`ti,ads124s06`](../build/dts/api/bindings/adc/ti%2Cads124s06.md#std-dtcompatible-ti-ads124s06)
  > - [`ti,ads124s08`](../build/dts/api/bindings/adc/ti%2Cads124s08.md#std-dtcompatible-ti-ads124s08)
  > - [`ti,ads131m02`](../build/dts/api/bindings/adc/ti%2Cads131m02.md#std-dtcompatible-ti-ads131m02)
  > - [`ti,tla2022`](../build/dts/api/bindings/adc/ti%2Ctla2022.md#std-dtcompatible-ti-tla2022)
  > - [`ti,tla2024`](../build/dts/api/bindings/adc/ti%2Ctla2024.md#std-dtcompatible-ti-tla2024)
- ARM architecture

  > - [`nxp,nbu`](../build/dts/api/bindings/arm/nxp%2Cnbu.md#std-dtcompatible-nxp-nbu)
- Audio

  > - [`cirrus,cs43l22`](../build/dts/api/bindings/audio/cirrus%2Cc43l22.md#std-dtcompatible-cirrus-cs43l22)
  > - [`intel,adsp-mic-privacy`](../build/dts/api/bindings/audio/intel%2Cmic-privacy.md#std-dtcompatible-intel-adsp-mic-privacy)
- Bluetooth

  > - [`renesas,bt-hci-da1453x`](../build/dts/api/bindings/bluetooth/renesas%2Cbt-hci-da1453x.md#std-dtcompatible-renesas-bt-hci-da1453x)
  > - [`silabs,siwx91x-bt-hci`](../build/dts/api/bindings/bluetooth/silabs%2Csiwx91x-bt-hci.md#std-dtcompatible-silabs-siwx91x-bt-hci)
  > - [`st,hci-stm32wb0`](../build/dts/api/bindings/bluetooth/st%2Chci-stm32wb0.md#std-dtcompatible-st-hci-stm32wb0)
- Charger

  > - [`nxp,pf1550-charger`](../build/dts/api/bindings/charger/nxp%2Cpf1550-charger.md#std-dtcompatible-nxp-pf1550-charger)
- Clock control

  > - [`atmel,sam0-gclk`](../build/dts/api/bindings/clock/atmel%2Csam0-gclk.md#std-dtcompatible-atmel-sam0-gclk)
  > - [`atmel,sam0-mclk`](../build/dts/api/bindings/clock/atmel%2Csam0-mclk.md#std-dtcompatible-atmel-sam0-mclk)
  > - [`atmel,sam0-osc32kctrl`](../build/dts/api/bindings/clock/atmel%2Csam0-osc32kctrl.md#std-dtcompatible-atmel-sam0-osc32kctrl)
  > - [`nordic,nrf-hsfll-global`](../build/dts/api/bindings/clock/nordic%2Cnrf-hsfll-global.md#std-dtcompatible-nordic-nrf-hsfll-global)
  > - [`nuvoton,npcm-pcc`](../build/dts/api/bindings/clock/nuvoton%2Cnpcm-pcc.md#std-dtcompatible-nuvoton-npcm-pcc)
  > - [`realtek,rts5912-sccon`](../build/dts/api/bindings/clock/realtek%2Crts5912-sccon.md#std-dtcompatible-realtek-rts5912-sccon)
  > - [`renesas,rz-cpg`](../build/dts/api/bindings/clock/renesas%2Crz-cpg.md#std-dtcompatible-renesas-rz-cpg)
  > - [`st,stm32n6-cpu-clock-mux`](../build/dts/api/bindings/clock/st%2Cstm32n6-cpu-clock-mux.md#std-dtcompatible-st-stm32n6-cpu-clock-mux)
  > - [`st,stm32n6-hse-clock`](../build/dts/api/bindings/clock/st%2Cstm32n6-hse-clock.md#std-dtcompatible-st-stm32n6-hse-clock)
  > - [`st,stm32n6-ic-clock-mux`](../build/dts/api/bindings/clock/st%2Cstm32n6-ic-clock-mux.md#std-dtcompatible-st-stm32n6-ic-clock-mux)
  > - [`st,stm32n6-pll-clock`](../build/dts/api/bindings/clock/st%2Cstm32n6-pll-clock.md#std-dtcompatible-st-stm32n6-pll-clock)
  > - [`st,stm32n6-rcc`](../build/dts/api/bindings/clock/st%2Cstm32n6-rcc.md#std-dtcompatible-st-stm32n6-rcc)
  > - [`wch,ch32v00x-hse-clock`](../build/dts/api/bindings/clock/wch%2Cch32v00x-hse-clock.md#std-dtcompatible-wch-ch32v00x-hse-clock)
  > - [`wch,ch32v00x-hsi-clock`](../build/dts/api/bindings/clock/wch%2Cch32v00x-hsi-clock.md#std-dtcompatible-wch-ch32v00x-hsi-clock)
  > - [`wch,ch32v00x-pll-clock`](../build/dts/api/bindings/clock/wch%2Cch32v00x-pll-clock.md#std-dtcompatible-wch-ch32v00x-pll-clock)
  > - [`wch,rcc`](../build/dts/api/bindings/clock/wch%2Crcc.md#std-dtcompatible-wch-rcc)
- Comparator

  > - [`silabs,acmp`](../build/dts/api/bindings/comparator/silabs%2Cacmp.md#std-dtcompatible-silabs-acmp)
- Counter

  > - [`adi,max32-rtc-counter`](../build/dts/api/bindings/counter/adi%2Cmax32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter)
  > - [`renesas,rz-gtm-counter`](../build/dts/api/bindings/counter/renesas%2Crz-gtm-counter.md#std-dtcompatible-renesas-rz-gtm-counter)
- CPU

  > - [`wch,qingke-v2`](../build/dts/api/bindings/cpu/wch%2Cqingke-v2.md#std-dtcompatible-wch-qingke-v2)
- DAC

  > - [`adi,max22017-dac`](../build/dts/api/bindings/dac/adi%2Cmax22017-dac.md#std-dtcompatible-adi-max22017-dac)
  > - [`renesas,ra-dac`](../build/dts/api/bindings/dac/renesas%2Cra-dac.md#std-dtcompatible-renesas-ra-dac)
  > - [`renesas,ra-dac-global`](../build/dts/api/bindings/dac/renesas%2Cra-dac-global.md#std-dtcompatible-renesas-ra-dac-global)
- DAI

  > - [`mediatek,afe`](../build/dts/api/bindings/dai/mediatek%2Cafe.md#std-dtcompatible-mediatek-afe)
  > - [`nxp,dai-micfil`](../build/dts/api/bindings/dai/nxp%2Cdai-micfil.md#std-dtcompatible-nxp-dai-micfil)
- Display

  > - [`ilitek,ili9806e-dsi`](../build/dts/api/bindings/display/ilitek%2Cili9806e.md#std-dtcompatible-ilitek-ili9806e-dsi)
  > - [`renesas,ra-glcdc`](../build/dts/api/bindings/display/renesas%2Cra-glcdc.md#std-dtcompatible-renesas-ra-glcdc)
  > - [`solomon,ssd1309fb`](../build/dts/api/compatibles/solomon%2Cssd1309fb.md#std-dtcompatible-solomon-ssd1309fb)
- DMA

  > - [`infineon,cat1-dma`](../build/dts/api/bindings/dma/infineon%2Ccat1-dma.md#std-dtcompatible-infineon-cat1-dma)
  > - [`nxp,sdma`](../build/dts/api/bindings/dma/nxp%2Csdma.md#std-dtcompatible-nxp-sdma)
  > - [`silabs,ldma`](../build/dts/api/bindings/dma/silabs%2Cldma.md#std-dtcompatible-silabs-ldma)
  > - [`silabs,siwx91x-dma`](../build/dts/api/bindings/dma/silabs%2Csiwx91x-dma.md#std-dtcompatible-silabs-siwx91x-dma)
  > - [`xlnx,axi-dma-1.00.a`](../build/dts/api/bindings/dma/xilinx%2Caxi-dma.md#std-dtcompatible-xlnx-axi-dma-1.00.a)
  > - [`xlnx,eth-dma`](../build/dts/api/bindings/dma/xilinx%2Ceth-dma.md#std-dtcompatible-xlnx-eth-dma)
- DSA

  > - [`nxp,netc-switch`](../build/dts/api/bindings/dsa/nxp%2Cnetc-switch.md#std-dtcompatible-nxp-netc-switch)
- EEPROM

  - [`fujitsu,mb85rsxx`](../build/dts/api/bindings/mtd/fujitsu%2Cmb85rsxx.md#std-dtcompatible-fujitsu-mb85rsxx)
- Ethernet

  > - [`davicom,dm8806-phy`](../build/dts/api/bindings/ethernet/davicom%2Cdm8806-phy.md#std-dtcompatible-davicom-dm8806-phy)
  > - [`microchip,lan9250`](../build/dts/api/bindings/ethernet/microchip%2Clan9250.md#std-dtcompatible-microchip-lan9250)
  > - [`microchip,t1s-phy`](../build/dts/api/bindings/ethernet/microchip%2Ct1s-phy.md#std-dtcompatible-microchip-t1s-phy)
  > - [`microchip,vsc8541`](../build/dts/api/bindings/ethernet/microchip%2Cvsc8541-phy.md#std-dtcompatible-microchip-vsc8541)
  > - [`renesas,ra-ethernet`](../build/dts/api/bindings/ethernet/renesas%2Cra-ethernet.md#std-dtcompatible-renesas-ra-ethernet)
  > - [`sensry,sy1xx-mac`](../build/dts/api/bindings/ethernet/sensry%2Csy1xx-mac.md#std-dtcompatible-sensry-sy1xx-mac)
- Firmware

  > - [`arm,scmi-power`](../build/dts/api/bindings/firmware/arm%2Cscmi-power.md#std-dtcompatible-arm-scmi-power)
- Flash controller

  > - [`silabs,siwx91x-flash-controller`](../build/dts/api/bindings/flash_controller/silabs%2Csiwx91x-flash-controller.md#std-dtcompatible-silabs-siwx91x-flash-controller)
  > - [`ti,cc23x0-flash-controller`](../build/dts/api/bindings/flash_controller/ti%2Ccc23x0-flash-controller.md#std-dtcompatible-ti-cc23x0-flash-controller)
- FPGA

  > - [`lattice,ice40-fpga-base`](../build/dts/api/bindings/fpga/lattice%2Cice40-fpga-base.md#std-dtcompatible-lattice-ice40-fpga-base)
  > - [`lattice,ice40-fpga-bitbang`](../build/dts/api/bindings/fpga/lattice%2Cice40-fpga-bitbang.md#std-dtcompatible-lattice-ice40-fpga-bitbang)
- GPIO

  > - [`adi,max22017-gpio`](../build/dts/api/bindings/gpio/adi%2Cmax22017-gpio.md#std-dtcompatible-adi-max22017-gpio)
  > - [`adi,max22190-gpio`](../build/dts/api/bindings/gpio/adi%2Cmax22190-gpio.md#std-dtcompatible-adi-max22190-gpio)
  > - [`awinic,aw9523b-gpio`](../build/dts/api/bindings/gpio/awinic%2Caw9523b-gpio.md#std-dtcompatible-awinic-aw9523b-gpio)
  > - [`ite,it8801-gpio`](../build/dts/api/bindings/gpio/ite%2Cit8801-gpio.md#std-dtcompatible-ite-it8801-gpio)
  > - [`microchip,mec5-gpio`](../build/dts/api/bindings/gpio/microchip%2Cmec5-gpio.md#std-dtcompatible-microchip-mec5-gpio)
  > - [`nordic,npm2100-gpio`](../build/dts/api/bindings/gpio/nordic%2Cnpm2100-gpio.md#std-dtcompatible-nordic-npm2100-gpio)
  > - [`nxp,pca6416`](../build/dts/api/bindings/gpio/nxp%2Cpca6416.md#std-dtcompatible-nxp-pca6416)
  > - [`raspberrypi,rp1-gpio`](../build/dts/api/bindings/gpio/raspberrypi%2Crp1-gpio.md#std-dtcompatible-raspberrypi-rp1-gpio)
  > - [`realtek,rts5912-gpio`](../build/dts/api/bindings/gpio/realtek%2Crts5912-gpio.md#std-dtcompatible-realtek-rts5912-gpio)
  > - [`renesas,ra-gpio-mipi-header`](../build/dts/api/bindings/gpio/renesas%2Cmipi-header.md#std-dtcompatible-renesas-ra-gpio-mipi-header)
  > - [`renesas,rz-gpio`](../build/dts/api/bindings/gpio/renesas%2Crz-gpio.md#std-dtcompatible-renesas-rz-gpio)
  > - [`renesas,rz-gpio-int`](../build/dts/api/bindings/gpio/renesas%2Crz-gpio-int.md#std-dtcompatible-renesas-rz-gpio-int)
  > - [`sensry,sy1xx-gpio`](../build/dts/api/bindings/gpio/sensry%2Csy1xx-gpio.md#std-dtcompatible-sensry-sy1xx-gpio)
  > - [`silabs,siwx91x-gpio`](../build/dts/api/bindings/gpio/silabs%2Csiwx91x-gpio.md#std-dtcompatible-silabs-siwx91x-gpio)
  > - [`silabs,siwx91x-gpio-port`](../build/dts/api/bindings/gpio/silabs%2Csiwx91x-gpio-port.md#std-dtcompatible-silabs-siwx91x-gpio-port)
  > - [`silabs,siwx91x-gpio-uulp`](../build/dts/api/bindings/gpio/silabs%2Csiwx91x-gpio-uulp.md#std-dtcompatible-silabs-siwx91x-gpio-uulp)
  > - [`st,dcmi-camera-fpu-330zh`](../build/dts/api/bindings/gpio/st%2Cdcmi-camera-fpu-330zh.md#std-dtcompatible-st-dcmi-camera-fpu-330zh)
  > - [`st,mfxstm32l152`](../build/dts/api/bindings/gpio/st%2Cmfxstm32l152.md#std-dtcompatible-st-mfxstm32l152)
  > - [`stemma-qt-connector`](../build/dts/api/bindings/gpio/stemma-qt-connector.md#std-dtcompatible-stemma-qt-connector)
  > - [`ti,cc23x0-gpio`](../build/dts/api/bindings/gpio/ti%2Ccc23x0-gpio.md#std-dtcompatible-ti-cc23x0-gpio)
  > - [`wch,gpio`](../build/dts/api/bindings/gpio/wch%2Cgpio.md#std-dtcompatible-wch-gpio)
- IEEE 802.15.4 HDLC RCP interface

  > - [`nxp,hdlc-rcp-if`](../build/dts/api/bindings/hdlc_rcp_if/nxp%2Chdlc-rcp-if.md#std-dtcompatible-nxp-hdlc-rcp-if)
  > - [`uart,hdlc-rcp-if`](../build/dts/api/bindings/hdlc_rcp_if/uart%2Chdlc-rcp-if.md#std-dtcompatible-uart-hdlc-rcp-if)
- I2C

  > - [`nordic,nrf-twis`](../build/dts/api/bindings/i2c/nordic%2Cnrf-twis.md#std-dtcompatible-nordic-nrf-twis)
  > - [`nxp,ii2c`](../build/dts/api/bindings/i2c/nxp%2Cii2c.md#std-dtcompatible-nxp-ii2c)
  > - [`ti,omap-i2c`](../build/dts/api/bindings/i2c/ti%2Comap-i2c.md#std-dtcompatible-ti-omap-i2c)
  > - [`ti,tca9544a`](../build/dts/api/bindings/i2c/ti%2Ctca9544a.md#std-dtcompatible-ti-tca9544a)
- I3C

  > - [`snps,designware-i3c`](../build/dts/api/bindings/i3c/snps%2Cdesignware-i3c.md#std-dtcompatible-snps-designware-i3c)
  > - [`st,stm32-i3c`](../build/dts/api/bindings/i3c/st%2Cstm32-i3c.md#std-dtcompatible-st-stm32-i3c)
- IEEE 802.15.4

  > - [`nxp,mcxw-ieee802154`](../build/dts/api/bindings/ieee802154/nxp%2Cmcxw-ieee802154.md#std-dtcompatible-nxp-mcxw-ieee802154)
- Input

  > - [`cypress,cy8cmbr3xxx`](../build/dts/api/bindings/input/cypress%2Ccy8cmbr3xxx.md#std-dtcompatible-cypress-cy8cmbr3xxx)
  > - [`ite,it8801-kbd`](../build/dts/api/bindings/input/ite%2Cit8801-kbd.md#std-dtcompatible-ite-it8801-kbd)
  > - [`microchip,cap12xx`](../build/dts/api/bindings/input/microchip%2Ccap12xx.md#std-dtcompatible-microchip-cap12xx)
  > - [`nintendo,nunchuk`](../build/dts/api/bindings/input/nintendo%2Cnunchuk.md#std-dtcompatible-nintendo-nunchuk)
- Interrupt controller

  > - [`renesas,rz-ext-irq`](../build/dts/api/bindings/interrupt-controller/renesas%2Crz-ext-irq.md#std-dtcompatible-renesas-rz-ext-irq)
  > - [`wch,pfic`](../build/dts/api/bindings/interrupt-controller/wch%2Cpfic.md#std-dtcompatible-wch-pfic)
- Mailbox

  > - [`linaro,ivshmem-mbox`](../build/dts/api/bindings/mbox/linaro%2Civshmem-mbox.md#std-dtcompatible-linaro-ivshmem-mbox)
  > - [`ti,omap-mailbox`](../build/dts/api/bindings/mbox/ti%2Comap-mailbox.md#std-dtcompatible-ti-omap-mailbox)
- MDIO

  > - [`microchip,lan865x-mdio`](../build/dts/api/bindings/mdio/microchip%2Clan865x-mdio.md#std-dtcompatible-microchip-lan865x-mdio)
  > - [`renesas,ra-mdio`](../build/dts/api/bindings/mdio/renesas%2Cra-mdio.md#std-dtcompatible-renesas-ra-mdio)
  > - [`sensry,sy1xx-mdio`](../build/dts/api/bindings/mdio/sensry%2Csy1xx-mdio.md#std-dtcompatible-sensry-sy1xx-mdio)
- Memory controller

  > - [`renesas,ra-sdram`](../build/dts/api/bindings/memory-controllers/renesas%2Cra-sdram.md#std-dtcompatible-renesas-ra-sdram)
- MFD

  > - [`adi,max22017`](../build/dts/api/bindings/mfd/adi%2Cmax22017.md#std-dtcompatible-adi-max22017)
  > - [`awinic,aw9523b`](../build/dts/api/bindings/mfd/awinic%2Caw9523b.md#std-dtcompatible-awinic-aw9523b)
  > - [`ite,it8801-altctrl`](../build/dts/api/bindings/mfd/ite%2Cit8801-altctrl.md#std-dtcompatible-ite-it8801-altctrl)
  > - [`ite,it8801-mfd`](../build/dts/api/bindings/mfd/ite%2Cit8801-mfd.md#std-dtcompatible-ite-it8801-mfd)
  > - [`ite,it8801-mfd-map`](../build/dts/api/bindings/mfd/ite%2Cit8801-mfd-map.md#std-dtcompatible-ite-it8801-mfd-map)
  > - [`maxim,ds3231-mfd`](../build/dts/api/bindings/mfd/maxim%2Cds3231-mfd.md#std-dtcompatible-maxim-ds3231-mfd)
  > - [`nordic,npm2100`](../build/dts/api/bindings/mfd/nordic%2Cnpm2100.md#std-dtcompatible-nordic-npm2100)
  > - [`nxp,pf1550`](../build/dts/api/bindings/mfd/nxp%2Cpf1550.md#std-dtcompatible-nxp-pf1550)
- MIPI DSI

  > - [`renesas,ra-mipi-dsi`](../build/dts/api/bindings/mipi-dsi/renesas%2Cra-mipi-dsi.md#std-dtcompatible-renesas-ra-mipi-dsi)
- Miscellaneous

  > - [`nordic,nrf-bicr`](../build/dts/api/bindings/misc/nordic%2Cnrf-bicr.md#std-dtcompatible-nordic-nrf-bicr)
  > - [`nordic,nrf-ppib`](../build/dts/api/bindings/misc/nordic%2Cnrf-ppib.md#std-dtcompatible-nordic-nrf-ppib)
  > - [`renesas,ra-external-interrupt`](../build/dts/api/bindings/misc/renesas%2Cra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt)
- MMU / MPU

  > - [`nxp,sysmpu`](../build/dts/api/bindings/mmu_mpu/nxp%2Csysmpu.md#std-dtcompatible-nxp-sysmpu)
- MTD

  > - [`nxp,s32-qspi-hyperflash`](../build/dts/api/bindings/mtd/nxp%2Cs32-qspi-hyperflash.md#std-dtcompatible-nxp-s32-qspi-hyperflash)
  > - [`nxp,xspi-mx25um51345g`](../build/dts/api/bindings/mtd/nxp%2Cxspi-mx25um51345g.md#std-dtcompatible-nxp-xspi-mx25um51345g)
  > - [`ti,cc23x0-ccfg-flash`](../build/dts/api/bindings/mtd/ti%2Ccc23x0-ccfg-flash.md#std-dtcompatible-ti-cc23x0-ccfg-flash)
- Networking

  > - [`silabs,series2-radio`](../build/dts/api/bindings/net/wireless/silabs%2Cseries2-radio.md#std-dtcompatible-silabs-series2-radio)
- PCIe

  > - [`brcm,brcmstb-pcie`](../build/dts/api/bindings/pcie/controller/brcm%2Cbrcmstb-pcie.md#std-dtcompatible-brcm-brcmstb-pcie)
- PHY

  > - [`renesas,ra-usbphyc`](../build/dts/api/bindings/phy/renesas%2Cra-usbphyc.md#std-dtcompatible-renesas-ra-usbphyc)
  > - [`st,stm32u5-otghs-phy`](../build/dts/api/bindings/phy/st%2Cstm32u5-otghs-phy.md#std-dtcompatible-st-stm32u5-otghs-phy)
- Pin control

  > - [`realtek,rts5912-pinctrl`](../build/dts/api/bindings/pinctrl/realtek%2Crts5912-pinctrl.md#std-dtcompatible-realtek-rts5912-pinctrl)
  > - [`renesas,rzg-pinctrl`](../build/dts/api/bindings/pinctrl/renesas%2Crzg-pinctrl.md#std-dtcompatible-renesas-rzg-pinctrl)
  > - [`sensry,sy1xx-pinctrl`](../build/dts/api/bindings/pinctrl/sensry%2Csy1xx-pinctrl.md#std-dtcompatible-sensry-sy1xx-pinctrl)
  > - [`silabs,dbus-pinctrl`](../build/dts/api/bindings/pinctrl/silabs%2Cdbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl)
  > - [`silabs,siwx91x-pinctrl`](../build/dts/api/bindings/pinctrl/silabs%2Csiwx91x-pinctrl.md#std-dtcompatible-silabs-siwx91x-pinctrl)
  > - [`ti,cc23x0-pinctrl`](../build/dts/api/bindings/pinctrl/ti%2Ccc23x0-pinctrl.md#std-dtcompatible-ti-cc23x0-pinctrl)
  > - [`wch,afio`](../build/dts/api/bindings/pinctrl/wch%2Cafio.md#std-dtcompatible-wch-afio)
- PWM

  > - [`atmel,sam0-tc-pwm`](../build/dts/api/bindings/pwm/atmel%2Csam0-tc-pwm.md#std-dtcompatible-atmel-sam0-tc-pwm)
  > - [`ite,it8801-pwm`](../build/dts/api/bindings/pwm/ite%2Cit8801-pwm.md#std-dtcompatible-ite-it8801-pwm)
  > - [`renesas,rz-gpt-pwm`](../build/dts/api/bindings/pwm/renesas%2Crz-gpt-pwm.md#std-dtcompatible-renesas-rz-gpt-pwm)
  > - [`zephyr,fake-pwm`](../build/dts/api/bindings/pwm/zephyr%2Cfake-pwm.md#std-dtcompatible-zephyr-fake-pwm)
- Quad SPI

  > - [`nxp,s32-qspi-sfp-frad`](../build/dts/api/bindings/qspi/nxp%2Cs32-qspi-sfp-frad.md#std-dtcompatible-nxp-s32-qspi-sfp-frad)
  > - [`nxp,s32-qspi-sfp-mdad`](../build/dts/api/bindings/qspi/nxp%2Cs32-qspi-sfp-mdad.md#std-dtcompatible-nxp-s32-qspi-sfp-mdad)
- Regulator

  > - [`nordic,npm2100-regulator`](../build/dts/api/bindings/regulator/nordic%2Cnpm2100-regulator.md#std-dtcompatible-nordic-npm2100-regulator)
  > - [`nxp,pf1550-regulator`](../build/dts/api/bindings/regulator/nxp%2Cpf1550-regulator.md#std-dtcompatible-nxp-pf1550-regulator)
- RNG

  > - [`nordic,nrf-cracen-ctrdrbg`](../build/dts/api/bindings/rng/nordic%2Cnrf-cracen-ctrdrbg.md#std-dtcompatible-nordic-nrf-cracen-ctrdrbg)
  > - [`nxp,ele-trng`](../build/dts/api/bindings/rng/nxp%2Cele-trng.md#std-dtcompatible-nxp-ele-trng)
  > - [`renesas,ra-sce5-rng`](../build/dts/api/bindings/rng/renesas%2Cra-sce5-rng.md#std-dtcompatible-renesas-ra-sce5-rng)
  > - [`renesas,ra-sce7-rng`](../build/dts/api/bindings/rng/renesas%2Cra-sce7-rng.md#std-dtcompatible-renesas-ra-sce7-rng)
  > - [`renesas,ra-sce9-rng`](../build/dts/api/bindings/rng/renesas%2Cra-sce9-rng.md#std-dtcompatible-renesas-ra-sce9-rng)
  > - [`renesas,ra-trng`](../build/dts/api/bindings/rng/renesas%2Cra-trng.md#std-dtcompatible-renesas-ra-trng)
  > - [`sensry,sy1xx-trng`](../build/dts/api/bindings/rng/sensry%2Csy1xx-trng.md#std-dtcompatible-sensry-sy1xx-trng)
  > - [`silabs,siwx91x-rng`](../build/dts/api/bindings/rng/silabs%2Csiwx91x-rng.md#std-dtcompatible-silabs-siwx91x-rng)
  > - [`st,stm32-rng-noirq`](../build/dts/api/bindings/rng/st%2Cstm32-rng-noirq.md#std-dtcompatible-st-stm32-rng-noirq)
- RTC

  > - [`epson,rx8130ce-rtc`](../build/dts/api/bindings/rtc/epson%2Crx8130ce.md#std-dtcompatible-epson-rx8130ce-rtc)
  > - [`maxim,ds1337`](../build/dts/api/bindings/rtc/maxim%2Cds1337.md#std-dtcompatible-maxim-ds1337)
  > - [`maxim,ds3231-rtc`](../build/dts/api/bindings/rtc/maxim%2Cds3231-rtc.md#std-dtcompatible-maxim-ds3231-rtc)
  > - [`microcrystal,rv8803`](../build/dts/api/bindings/rtc/microcrystal%2Crv8803.md#std-dtcompatible-microcrystal-rv8803)
  > - [`ti,bq32002`](../build/dts/api/bindings/rtc/ti%2Cbq32002.md#std-dtcompatible-ti-bq32002)
- SDHC

  > - [`renesas,ra-sdhc`](../build/dts/api/bindings/sdhc/renesas%2Cra-sdhc.md#std-dtcompatible-renesas-ra-sdhc)
- Sensors

  > - [`adi,adxl366`](../build/dts/api/compatibles/adi%2Cadxl366.md#std-dtcompatible-adi-adxl366)
  > - [`hc-sr04`](../build/dts/api/bindings/sensor/hc-sr04.md#std-dtcompatible-hc-sr04)
  > - [`invensense,icm42370p`](../build/dts/api/compatibles/invensense%2Cicm42370p.md#std-dtcompatible-invensense-icm42370p)
  > - [`invensense,icm42670s`](../build/dts/api/compatibles/invensense%2Cicm42670s.md#std-dtcompatible-invensense-icm42670s)
  > - [`invensense,icp101xx`](../build/dts/api/bindings/sensor/invensense%2Cicp101xx.md#std-dtcompatible-invensense-icp101xx)
  > - [`maxim,ds3231-sensor`](../build/dts/api/bindings/sensor/maxim%2Cds3231-sensor.md#std-dtcompatible-maxim-ds3231-sensor)
  > - [`melexis,mlx90394`](../build/dts/api/bindings/sensor/melexis%2Cmlx90394.md#std-dtcompatible-melexis-mlx90394)
  > - [`nordic,npm2100-vbat`](../build/dts/api/bindings/sensor/nordic%2Cnpm2100-vbat.md#std-dtcompatible-nordic-npm2100-vbat)
  > - [`phosense,xbr818`](../build/dts/api/bindings/sensor/phosense%2Cxbr818.md#std-dtcompatible-phosense-xbr818)
  > - [`renesas,hs400x`](../build/dts/api/bindings/sensor/renesas%2Chs400x.md#std-dtcompatible-renesas-hs400x)
  > - [`sensirion,scd40`](../build/dts/api/bindings/sensor/sensirion%2Cscd40.md#std-dtcompatible-sensirion-scd40)
  > - [`sensirion,scd41`](../build/dts/api/bindings/sensor/sensirion%2Cscd41.md#std-dtcompatible-sensirion-scd41)
  > - [`sensirion,sts4x`](../build/dts/api/bindings/sensor/sensirion%2Csts4x.md#std-dtcompatible-sensirion-sts4x)
  > - [`st,lis2duxs12`](../build/dts/api/compatibles/st%2Clis2duxs12.md#std-dtcompatible-st-lis2duxs12)
  > - [`st,lsm6dsv16x`](../build/dts/api/compatibles/st%2Clsm6dsv16x.md#std-dtcompatible-st-lsm6dsv16x)
  > - [`ti,tmag3001`](../build/dts/api/bindings/sensor/ti%2Ctmag3001.md#std-dtcompatible-ti-tmag3001)
  > - [`ti,tmp435`](../build/dts/api/bindings/sensor/ti%2Ctmp435.md#std-dtcompatible-ti-tmp435)
  > - [`we,wsen-pads-2511020213301`](../build/dts/api/compatibles/we%2Cwsen-pads-2511020213301.md#std-dtcompatible-we-wsen-pads-2511020213301)
  > - [`we,wsen-pdus-25131308XXXXX`](../build/dts/api/bindings/sensor/we%2Cwsen-pdus-25131308XXXXX.md#std-dtcompatible-we-wsen-pdus-25131308XXXXX)
  > - [`we,wsen-tids-2521020222501`](../build/dts/api/bindings/sensor/we%2Cwsen-tids-2521020222501.md#std-dtcompatible-we-wsen-tids-2521020222501)
- Serial controller

  > - [`microchip,mec5-uart`](../build/dts/api/bindings/serial/microchip%2Cmec5-uart.md#std-dtcompatible-microchip-mec5-uart)
  > - [`realtek,rts5912-uart`](../build/dts/api/bindings/serial/realtek%2Crts5912-uart.md#std-dtcompatible-realtek-rts5912-uart)
  > - [`renesas,rz-scif-uart`](../build/dts/api/bindings/serial/renesas%2Crz-scif-uart.md#std-dtcompatible-renesas-rz-scif-uart)
  > - [`silabs,eusart-uart`](../build/dts/api/bindings/serial/silabs%2Ceusart-uart.md#std-dtcompatible-silabs-eusart-uart)
  > - [`silabs,usart-uart`](../build/dts/api/bindings/serial/silabs%2Cusart-uart.md#std-dtcompatible-silabs-usart-uart)
  > - [`ti,cc23x0-uart`](../build/dts/api/bindings/serial/ti%2Ccc23x0-uart.md#std-dtcompatible-ti-cc23x0-uart)
  > - [`wch,usart`](../build/dts/api/bindings/serial/wch%2Cusart.md#std-dtcompatible-wch-usart)
- SPI

  > - [`ite,it8xxx2-spi`](../build/dts/api/bindings/spi/ite%2Cit8xxx2-spi.md#std-dtcompatible-ite-it8xxx2-spi)
  > - [`nxp,lpspi`](../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi)
  > - [`nxp,xspi`](../build/dts/api/bindings/spi/nxp%2Cxspi.md#std-dtcompatible-nxp-xspi)
  > - [`renesas,ra-spi`](../build/dts/api/bindings/spi/renesas%2Cra-spi.md#std-dtcompatible-renesas-ra-spi)
- Stepper

  > - [`adi,tmc2209`](../build/dts/api/bindings/stepper/adi/adi%2Ctmc2209.md#std-dtcompatible-adi-tmc2209)
  > - [`ti,drv8424`](../build/dts/api/bindings/stepper/ti/ti%2Cdrv8424.md#std-dtcompatible-ti-drv8424)
- TCPC

  > - [`richtek,rt1715`](../build/dts/api/bindings/tcpc/richtek%2Crt1715.md#std-dtcompatible-richtek-rt1715)
- Timer

  > - [`mediatek,ostimer64`](../build/dts/api/bindings/timer/mediatek%2Costimer64.md#std-dtcompatible-mediatek-ostimer64)
  > - [`realtek,rts5912-rtmr`](../build/dts/api/bindings/timer/realtek%2Crts5912-rtmr.md#std-dtcompatible-realtek-rts5912-rtmr)
  > - [`realtek,rts5912-slwtimer`](../build/dts/api/bindings/timer/realtek%2Crts5912-slwtimer.md#std-dtcompatible-realtek-rts5912-slwtimer)
  > - [`renesas,rz-gpt`](../build/dts/api/bindings/timer/renesas%2Crz-gpt.md#std-dtcompatible-renesas-rz-gpt)
  > - [`renesas,rz-gtm`](../build/dts/api/bindings/timer/renesas%2Crz-gtm.md#std-dtcompatible-renesas-rz-gtm)
  > - [`riscv,machine-timer`](../build/dts/api/bindings/timer/riscv%2Cmachine-timer.md#std-dtcompatible-riscv-machine-timer)
  > - [`ti,cc23x0-systim-timer`](../build/dts/api/bindings/timer/ti%2Ccc23x0-timer.md#std-dtcompatible-ti-cc23x0-systim-timer)
  > - [`wch,systick`](../build/dts/api/bindings/timer/wch%2Csystick.md#std-dtcompatible-wch-systick)
- USB

  > - [`ambiq,usb`](../build/dts/api/bindings/usb/ambiq%2Cusb.md#std-dtcompatible-ambiq-usb)
  > - [`renesas,ra-udc`](../build/dts/api/bindings/usb/renesas/renesas%2Cra-udc.md#std-dtcompatible-renesas-ra-udc)
  > - [`renesas,ra-usbfs`](../build/dts/api/bindings/usb/renesas/renesas%2Cra-usbfs.md#std-dtcompatible-renesas-ra-usbfs)
  > - [`renesas,ra-usbhs`](../build/dts/api/bindings/usb/renesas/renesas%2Cra-usbhs.md#std-dtcompatible-renesas-ra-usbhs)
  > - [`zephyr,midi2-device`](../build/dts/api/bindings/usb/zephyr%2Cmidi2-device.md#std-dtcompatible-zephyr-midi2-device)
- Video

  > - [`zephyr,video-emul-imager`](../build/dts/api/bindings/video/zephyr%2Cvideo-emul-imager.md#std-dtcompatible-zephyr-video-emul-imager)
  > - [`zephyr,video-emul-rx`](../build/dts/api/bindings/video/zephyr%2Cvideo-emul-rx.md#std-dtcompatible-zephyr-video-emul-rx)
- Watchdog

  > - [`atmel,sam4l-watchdog`](../build/dts/api/bindings/watchdog/atmel%2Csam4l-watchdog.md#std-dtcompatible-atmel-sam4l-watchdog)
  > - [`nordic,npm2100-wdt`](../build/dts/api/bindings/watchdog/nordic%2Cnpm2100-wdt.md#std-dtcompatible-nordic-npm2100-wdt)
  > - [`nxp,rtwdog`](../build/dts/api/bindings/watchdog/nxp%2Crtwdog.md#std-dtcompatible-nxp-rtwdog)
- Wi-Fi

  > - [`infineon,airoc-wifi`](../build/dts/api/compatibles/infineon%2Cairoc-wifi.md#std-dtcompatible-infineon-airoc-wifi)
  > - [`silabs,siwx91x-wifi`](../build/dts/api/bindings/wifi/silabs%2Csiwx91x-wifi.md#std-dtcompatible-silabs-siwx91x-wifi)

## New Samples

- [Generic 6DOF Motion Dataready](../samples/sensor/6dof_motion_drdy/README.md#6dof_motion_drdy "Get 6-Axis accelerometer and gyroscope data from a sensor (data ready interrupt mode).")
- [Channel Sounding](../samples/bluetooth/channel_sounding/README.md#ble_cs "Use Channel Sounding functionality.")
- [Call Control Profile (CCP) Call Control Server](../samples/bluetooth/ccp_call_control_client/README.md#bluetooth_ccp_call_control_client "CCP Call Control Server sample that registers one or more TBS bearers and advertises the TBS UUID(s).")
- [Call Control Profile (CCP) Call Control Server](../samples/bluetooth/ccp_call_control_server/README.md#bluetooth_ccp_call_control_server "CCP Call Control Server sample that registers one or more TBS bearers and advertises the TBS UUID(s).")
- [Coresight STM benchmark](../samples/boards/nordic/coresight_stm/README.md#coresight_stm_sample)
- [USB DFU](../samples/subsys/usb/dfu-next/README.md#dfu-next "Implement a basic USB DFU device")
- [I2C RTIO loopback](../samples/drivers/i2c/rtio_loopback/README.md#i2c-rtio-loopback "Perform I2C transfers between I2C controller and custom I2C target using RTIO.")
- [LVGL screen transparency](../samples/modules/lvgl/screen_transparency/README.md#lvgl-screen-transparency "Rendering to screens with transparency support using LVGL.")
- [MCTP Endpoint Sample](../samples/modules/mctp/mctp_endpoint/README.md#mctp_endpoint_sample "Create an MCTP endpoint over UART.")
- [MCTP Host Sample](../samples/modules/mctp/mctp_host/README.md#mctp_host_sample "Create an MCTP host over UART.")
- [OpenThread shell](../samples/net/openthread/shell/README.md#openthread-shell "Test Thread and IEEE 802.15.4 using the OpenThread shell.")
- [OpenThread CoAP client and server application](../samples/net/openthread/coap/README.md#ot-coap "Build a Full Thread Device (FTD) CoAP server and client.")
- [Real-Time Clock (RTC)](../samples/drivers/rtc/README.md#rtc "Set and read the date/time from a Real-Time Clock.")
- [Sensor batch processing](../samples/subsys/rtio/sensor_batch_processing/README.md#sensor_batch_processing "Implement a sensor device using RTIO for asynchronous data processing.")
- [Sensor Clock](../samples/sensor/clock/README.md#sensor_clock "Test and debug Sensor Clock functionality.")
- [Generic device FIFO streaming](../samples/sensor/stream_fifo/README.md#stream_fifo "Get accelerometer/gyroscope/temperature FIFO data frames from a sensor using SENSOR_TRIG_FIFO_WATERMARK as a trigger.")
- [TDK Advanced Pedometer and Event Detection (APEX)](../samples/sensor/tdk_apex/README.md#tdk_apex "Get TDK APEX event detection (trigger mode).")
- [TMC50XX stepper](../samples/drivers/stepper/tmc50xx/README.md#tmc50xx "Rotate a TMC50XX stepper motor and change velocity at runtime.")
- [UART echo](../samples/drivers/uart/echo_bot/README.md#uart "Read data from the console and echo it back.")
- [USB MIDI2 device](../samples/subsys/usb/midi/README.md#usb-midi2-device "Implements a simple USB MIDI loopback and keyboard device.")
- [Console over USB CDC ACM](../samples/subsys/usb/console-next/README.md#usbd-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.")
- [WebUSB-next](../samples/subsys/usb/webusb-next/README.md#webusb-next "Receive and echo data from a web page using WebUSB API.")

## Other notable changes

- A header file has been introduced to allocate ID ranges for persistent keys in the PSA Crypto API.
  It defines the ID ranges allocated to different users of the API (application, subsystems…).
  Users of the API must now use this header file to construct persistent key IDs.
  See [include/zephyr/psa/key\_ids.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/psa/key_ids.h) for more information. ([GitHub #85581](https://github.com/zephyrproject-rtos/zephyr/issues/85581))
- Space-separated lists support has been removed from Twister configuration
  files. This feature was deprecated a long time ago. Projects that do still use
  them can use the [scripts/utils/twister\_to\_list.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/utils/twister_to_list.py) script to
  automatically migrate Twister configuration files.
- Test case names for Ztest now include the Ztest suite name, meaning the resulting identifier has
  three sections and looks like: `<test_scenario_name>.<ztest_suite_name>.<ztest_name>`.
  These extended identifiers are used in log output, twister.json and testplan.json,
  as well as for `--sub-test` command line parameters.
- The `--no-detailed-test-id` command line option can be used to shorten the test case name
  by excluding the test scenario name prefix which is the same as the parent test suite id.
- Added support for HTTP PUT/PATCH/DELETE methods for HTTP server dynamic resources.
- Driver API structures are now available through iterable sections and a new
  [`DEVICE_API_IS`](../doxygen/html/device_8h.md#a48c6030c2e7d1d05ace7c708dda11949) macro has been introduced to allow to check if a device supports a
  given API. Many shell commands now use this to provide “smarter” auto-completion and only list
  compatible devices when they expect a device argument.
- Zephyr’s [interactive board catalog](../boards/index.md#boards) has been extended to allow searching for boards
  based on supported hardware features. A new [`zephyr:board-supported-hw`](../contribute/documentation/guidelines.md#directive-zephyr-board-supported-hw "zephyr:board-supported-hw directive") Sphinx directive
  can now be used in boards’ documentation pages to automatically include a list of the hardware
  features supported by a board, and many boards have already adopted this new feature in their
  documentation.
