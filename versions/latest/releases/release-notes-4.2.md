---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/releases/release-notes-4.2.html
original_path: releases/release-notes-4.2.html
---

# Zephyr 4.2.0

We are pleased to announce the release of Zephyr version 4.2.0.

Major enhancements with this release include:

**Initial Support for Renesas RX**
:   The Renesas RX architecture is now supported, including a QEMU-based
    [board target](../boards/qemu/rx/doc/index.md#qemu_rx).

**USB Video Class Driver**
:   The USB device stack now supports USB Video Class (UVC) allowing camera devices and other
    image/video sources to be exposed as standard USB video devices. See [USB Video webcam](../samples/subsys/usb/uvc/README.md#uvc "Send video frames over USB.") to
    get started.

**Twister Power Harness**
:   A [new Twister harness](../develop/test/twister.md#twister-power-harness) enables measurement of the power consumption
    of the device under test and ensures it remains within a given tolerance.

**MQTT 5.0**
:   The networking stack now includes full support for the [MQTT 5.0](../connectivity/networking/api/mqtt.md#mqtt-socket-interface)
    protocol.

**Bluetooth Classic improvements**
:   The Bluetooth Classic stack now includes support for **Hands-Free Profile** (HFP) for both Audio
    Gateway (AG) and Hands-Free (HF) roles.

**Zbus**
:   The [Zbus library](../services/zbus/index.md#zbus) graduates to stable status with the release of API version v1.0.0.

**Expanded Board Support**
:   Support for 96 [new boards](#boards-added-in-zephyr-4-2) and 22
    [new shields](#shields-added-in-zephyr-4-2) has been added in this release.

An overview of the changes required or recommended when migrating your application from Zephyr
v4.1.0 to Zephyr v4.2.0 can be found in the separate [migration guide](migration-guide-4.2.md#migration-4-2).

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

- [**CVE 2025-27809**](https://www.cve.org/CVERecord?id=CVE-2025-27809) [TLS clients may unwittingly skip server authentication](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-03-1/)
- [**CVE 2025-27810**](https://www.cve.org/CVERecord?id=CVE-2025-27810) [Potential authentication bypass in TLS handshake](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-03-2/)
- [**CVE 2025-2962**](https://www.cve.org/CVERecord?id=CVE-2025-2962) [Infinite loop in dns\_copy\_qname](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-2qp5-c2vq-g2ww)
- [**CVE 2025-52496**](https://www.cve.org/CVERecord?id=CVE-2025-52496) [Race condition in AESNI support detection](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-1/)
- [**CVE 2025-52497**](https://www.cve.org/CVERecord?id=CVE-2025-52497) [Heap buffer under-read when parsing PEM-encrypted material](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-2/)
- [**CVE 2025-49600**](https://www.cve.org/CVERecord?id=CVE-2025-49600) [Unchecked return value in LMS verification allows signature bypass](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-3/)
- [**CVE 2025-49601**](https://www.cve.org/CVERecord?id=CVE-2025-49601) [Out-of-bounds read in mbedtls\_lms\_import\_public\_key()](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-4/)
- [**CVE 2025-49087**](https://www.cve.org/CVERecord?id=CVE-2025-49087) [Timing side-channel in block cipher decryption with PKCS#7 padding](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-5/)
- [**CVE 2025-48965**](https://www.cve.org/CVERecord?id=CVE-2025-48965) [NULL pointer dereference after using mbedtls\_asn1\_store\_named\_data()](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-6/)
- [**CVE 2025-47917**](https://www.cve.org/CVERecord?id=CVE-2025-47917) [Misleading memory management in mbedtls\_x509\_string\_to\_names()](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-7/)
- [**CVE 2025-7403**](https://www.cve.org/CVERecord?id=CVE-2025-7403): Under embargo until 2025-09-05

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

## API Changes

### Removed APIs and options

- Removed the deprecated `net_buf_put()` and `net_buf_get()` API functions.
- Removed the deprecated `include/zephyr/net/buf.h` header file.
- Removed the `--disable-unrecognized-section-test` Twister option. Test has been removed and the
  option became the default behavior.
- Removed the deprecated `kscan` subsystem.
- Removed `meas,ms5837` and replaced with [`meas,ms5837-30ba`](../build/dts/api/bindings/sensor/meas,ms5837-30ba.md#std-dtcompatible-meas-ms5837-30ba)
  and [`meas,ms5837-02ba`](../build/dts/api/bindings/sensor/meas,ms5837-02ba.md#std-dtcompatible-meas-ms5837-02ba).
- Removed the `get_ctrl` driver API from [`video_driver_api`](../doxygen/html/structvideo__driver__api.md).
- Removed `CONFIG_I3C_USE_GROUP_ADDR` and support for group addresses for I3C devices.

### Deprecated APIs and options

- The scheduler Kconfig options CONFIG\_SCHED\_DUMB and CONFIG\_WAITQ\_DUMB were
  renamed and deprecated. Use [`CONFIG_SCHED_SIMPLE`](../kconfig.md#CONFIG_SCHED_SIMPLE "CONFIG_SCHED_SIMPLE") and
  [`CONFIG_WAITQ_SIMPLE`](../kconfig.md#CONFIG_WAITQ_SIMPLE "CONFIG_WAITQ_SIMPLE") instead.
- The `CONFIG_LWM2M_ENGINE_MESSAGE_HEADER_SIZE` Kconfig option has been removed.
  The required header size should be included in the message size, configured using
  [`CONFIG_LWM2M_COAP_MAX_MSG_SIZE`](../kconfig.md#CONFIG_LWM2M_COAP_MAX_MSG_SIZE "CONFIG_LWM2M_COAP_MAX_MSG_SIZE"). Special care should be taken to ensure that
  the CoAP block size used ([`CONFIG_LWM2M_COAP_BLOCK_SIZE`](../kconfig.md#CONFIG_LWM2M_COAP_BLOCK_SIZE "CONFIG_LWM2M_COAP_BLOCK_SIZE")) can fit the given
  message size with headers. Previous headroom was 48 bytes.
- TLS credential type `TLS_CREDENTIAL_SERVER_CERTIFICATE` was renamed and
  deprecated, use [`TLS_CREDENTIAL_PUBLIC_CERTIFICATE`](../doxygen/html/group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5acd8b96102765f7f2a83582eab80df3d8) instead.
- `arduino_uno_r4_minima` and `arduino_uno_r4_wifi` board targets have been deprecated in favor
  of a new `arduino_uno_r4` board with revisions (`arduino_uno_r4@minima` and
  `arduino_uno_r4@wifi`).
- `esp32c6_devkitc` board target has been deprecated and renamed to
  `esp32c6_devkitc/esp32c6/hpcore`.
- `xiao_esp32c6` board target has been deprecated and renamed to
  `xiao_esp32c6/esp32c6/hpcore`.
- [`CONFIG_HAWKBIT_DDI_NO_SECURITY`](../kconfig.md#CONFIG_HAWKBIT_DDI_NO_SECURITY "CONFIG_HAWKBIT_DDI_NO_SECURITY") Kconfig option has been
  deprecated, because support for anonymous authentication had been removed from the
  hawkBit server in version 0.8.0.
- The [`CONFIG_BT_CONN_TX_MAX`](../kconfig.md#CONFIG_BT_CONN_TX_MAX "CONFIG_BT_CONN_TX_MAX") Kconfig option has been deprecated. The number of
  pending TX buffers is now aligned with the [`CONFIG_BT_BUF_ACL_TX_COUNT`](../kconfig.md#CONFIG_BT_BUF_ACL_TX_COUNT "CONFIG_BT_BUF_ACL_TX_COUNT") Kconfig
  option.
- The `CONFIG_CRYPTO_TINYCRYPT_SHIM` Kconfig option has been removed. It
  was deprecated since Zephyr 4.0, and users were advised to migrate to alternative
  crypto backends.
- The `CONFIG_BT_MESH_USES_TINYCRYPT` Kconfig option has been removed. It
  was deprecated since Zephyr 4.0. Users were advised to use
  [`CONFIG_BT_MESH_USES_MBEDTLS_PSA`](../kconfig.md#CONFIG_BT_MESH_USES_MBEDTLS_PSA "CONFIG_BT_MESH_USES_MBEDTLS_PSA") or
  [`CONFIG_BT_MESH_USES_TFM_PSA`](../kconfig.md#CONFIG_BT_MESH_USES_TFM_PSA "CONFIG_BT_MESH_USES_TFM_PSA") instead.

### Stable API changes in this release

- The API signature of `net_mgmt` event handler [`net_mgmt_event_handler_t`](../doxygen/html/group__net__mgmt.md#ga2e83a5a769ac52c846f255e23aea84d2)
  and request handler [`net_mgmt_request_handler_t`](../doxygen/html/group__net__mgmt.md#ga78b9302193bd0c5cc35d81d298a5eb6b) has changed. The event value
  type is changed from `uint32_t` to `uint64_t`.

### New APIs and options

- Architectures

  - NIOS2 Architecture was removed from Zephyr.
  - `ARCH_HAS_VECTOR_TABLE_RELOCATION`
  - [`CONFIG_SRAM_VECTOR_TABLE`](../kconfig.md#CONFIG_SRAM_VECTOR_TABLE "CONFIG_SRAM_VECTOR_TABLE") moved from `zephyr/Kconfig.zephyr` to
    `zephyr/arch/Kconfig` and added dependencies to it.
- Bluetooth

  - Audio

    - [`BT_BAP_ADV_PARAM_CONN_QUICK`](../doxygen/html/group__bt__bap.md#gac290c620aa1861ea717dee37e1e83bfe)
    - [`BT_BAP_ADV_PARAM_CONN_REDUCED`](../doxygen/html/group__bt__bap.md#gaf1883b2596f793ef24913ef7f165c5dd)
    - [`BT_BAP_CONN_PARAM_SHORT_7_5`](../doxygen/html/group__bt__bap.md#ga5d90920dfc8d554d0cd345edd0c36c66)
    - [`BT_BAP_CONN_PARAM_SHORT_10`](../doxygen/html/group__bt__bap.md#ga0469f86dc34ab738fbbcdf45cc105194)
    - [`BT_BAP_CONN_PARAM_RELAXED`](../doxygen/html/group__bt__bap.md#gad4a19588129f8cbf085dca166f0bc486)
    - [`BT_BAP_ADV_PARAM_BROADCAST_FAST`](../doxygen/html/group__bt__bap.md#gaf2e44d06b8b7aba57a80b1f04e65d7de)
    - [`BT_BAP_ADV_PARAM_BROADCAST_SLOW`](../doxygen/html/group__bt__bap.md#gaa11e0195a02baa656085f305d911042d)
    - [`BT_BAP_PER_ADV_PARAM_BROADCAST_FAST`](../doxygen/html/group__bt__bap.md#ga0f17a828720504892ff36447a4e3f7c3)
    - [`BT_BAP_PER_ADV_PARAM_BROADCAST_SLOW`](../doxygen/html/group__bt__bap.md#gaf71bf639a2fca0c4d5ab61bfd6354668)
    - [`bt_csip_set_member_set_size_and_rank()`](../doxygen/html/group__bt__csip.md#gaef51ab05dbe9d8a69674f7020e8f837f)
    - [`bt_csip_set_member_get_info()`](../doxygen/html/group__bt__csip.md#gad80917089bc7e629cc3cb9d7fbf6cf45)
    - [`bt_bap_unicast_group_foreach_stream()`](../doxygen/html/group__bt__bap__unicast__client.md#gad608ee07c8a50abf586a3bc31921f032)
    - [`bt_cap_unicast_group_create()`](../doxygen/html/group__bt__cap.md#ga299ee8321aa5059e48244e1ae8080637)
    - [`bt_cap_unicast_group_reconfig()`](../doxygen/html/group__bt__cap.md#ga6c862b49aa1339225aeb05fad32c2f06)
    - [`bt_cap_unicast_group_add_streams()`](../doxygen/html/group__bt__cap.md#ga7b5d30c07e57f4db23f72836a3b12b2b)
    - [`bt_cap_unicast_group_delete()`](../doxygen/html/group__bt__cap.md#ga9af37b30b6c858c24892eb1739b5330a)
    - [`bt_cap_unicast_group_foreach_stream()`](../doxygen/html/group__bt__cap.md#ga6c13996298c3e3aa33eb40f74b7bfe44)
  - Host

    - [`bt_le_get_local_features()`](../doxygen/html/group__bt__gap.md#ga650faa2a86f54499f4bc5a8657a55a87)
    - [`bt_le_bond_exists()`](../doxygen/html/group__bt__gap.md#ga309a67de79cc215db1d33251f267f361)
    - [`bt_br_bond_exists()`](../doxygen/html/group__bt__gap.md#gad88cf1dec20264f9bdde91571efe8dce)
    - [`bt_conn_lookup_addr_br()`](../doxygen/html/group__bt__conn.md#ga11ae1b656683cebe9db6a53e5166ad7a)
    - [`bt_conn_get_dst_br()`](../doxygen/html/group__bt__conn.md#ga1b02a1ce8e48ad483d73d1efd803618c)
    - LE Connection Subrating is no longer experimental.
    - Remove deletion of the classic bonding information from [`bt_unpair()`](../doxygen/html/group__bt__gap.md#gaceabbbe6e844650f791010e53c9df6a4), and add
      [`bt_br_unpair()`](../doxygen/html/group__bt__gap.md#gaccab07100ab64fd805fe1d468bc889ac).
    - Remove query of the classic bonding information from [`bt_foreach_bond()`](../doxygen/html/group__bt__gap.md#gaad380b7f8984f8522c1b79f9bdc04905), and add
      [`bt_br_foreach_bond()`](../doxygen/html/group__bt__gap.md#ga4c82193c50c616d9319c87ebcffabe66).
    - Add a new parameter `limited` to [`bt_br_set_discoverable()`](../doxygen/html/group__bt__gap.md#gae3376fdd364e9b9d6e304ec589ba00f5) to support limited
      discoverable mode for the classic.
    - Enable retransmission and flow control for the classic L2CAP, including
      [`CONFIG_BT_L2CAP_RET`](../kconfig.md#CONFIG_BT_L2CAP_RET "CONFIG_BT_L2CAP_RET"), [`CONFIG_BT_L2CAP_FC`](../kconfig.md#CONFIG_BT_L2CAP_FC "CONFIG_BT_L2CAP_FC"),
      [`CONFIG_BT_L2CAP_ENH_RET`](../kconfig.md#CONFIG_BT_L2CAP_ENH_RET "CONFIG_BT_L2CAP_ENH_RET"), and [`CONFIG_BT_L2CAP_STREAM`](../kconfig.md#CONFIG_BT_L2CAP_STREAM "CONFIG_BT_L2CAP_STREAM").
    - [`bt_avrcp_get_cap()`](../doxygen/html/avrcp_8h.md#adb21554b69948d5994de8344f44c1179)
    - Improve the classic hands-free unit, including
      [`CONFIG_BT_HFP_HF_CODEC_NEG`](../kconfig.md#CONFIG_BT_HFP_HF_CODEC_NEG "CONFIG_BT_HFP_HF_CODEC_NEG"), [`CONFIG_BT_HFP_HF_ECNR`](../kconfig.md#CONFIG_BT_HFP_HF_ECNR "CONFIG_BT_HFP_HF_ECNR"),
      [`CONFIG_BT_HFP_HF_3WAY_CALL`](../kconfig.md#CONFIG_BT_HFP_HF_3WAY_CALL "CONFIG_BT_HFP_HF_3WAY_CALL"), [`CONFIG_BT_HFP_HF_ECS`](../kconfig.md#CONFIG_BT_HFP_HF_ECS "CONFIG_BT_HFP_HF_ECS"),
      [`CONFIG_BT_HFP_HF_ECC`](../kconfig.md#CONFIG_BT_HFP_HF_ECC "CONFIG_BT_HFP_HF_ECC"), [`CONFIG_BT_HFP_HF_VOICE_RECG_TEXT`](../kconfig.md#CONFIG_BT_HFP_HF_VOICE_RECG_TEXT "CONFIG_BT_HFP_HF_VOICE_RECG_TEXT"),
      [`CONFIG_BT_HFP_HF_ENH_VOICE_RECG`](../kconfig.md#CONFIG_BT_HFP_HF_ENH_VOICE_RECG "CONFIG_BT_HFP_HF_ENH_VOICE_RECG"),
      [`CONFIG_BT_HFP_HF_VOICE_RECG`](../kconfig.md#CONFIG_BT_HFP_HF_VOICE_RECG "CONFIG_BT_HFP_HF_VOICE_RECG"),
      [`CONFIG_BT_HFP_HF_HF_INDICATORS`](../kconfig.md#CONFIG_BT_HFP_HF_HF_INDICATORS "CONFIG_BT_HFP_HF_HF_INDICATORS"),
      [`CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY`](../kconfig.md#CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY "CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY"), and
      [`CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY`](../kconfig.md#CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY "CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY").
    - Improve the classic hands-free audio gateway, including
      [`CONFIG_BT_HFP_AG_CODEC_NEG`](../kconfig.md#CONFIG_BT_HFP_AG_CODEC_NEG "CONFIG_BT_HFP_AG_CODEC_NEG"), [`CONFIG_BT_HFP_AG_ECNR`](../kconfig.md#CONFIG_BT_HFP_AG_ECNR "CONFIG_BT_HFP_AG_ECNR"),
      [`CONFIG_BT_HFP_AG_3WAY_CALL`](../kconfig.md#CONFIG_BT_HFP_AG_3WAY_CALL "CONFIG_BT_HFP_AG_3WAY_CALL"), [`CONFIG_BT_HFP_AG_ECS`](../kconfig.md#CONFIG_BT_HFP_AG_ECS "CONFIG_BT_HFP_AG_ECS"),
      [`CONFIG_BT_HFP_AG_ECC`](../kconfig.md#CONFIG_BT_HFP_AG_ECC "CONFIG_BT_HFP_AG_ECC"), [`CONFIG_BT_HFP_AG_VOICE_RECG_TEXT`](../kconfig.md#CONFIG_BT_HFP_AG_VOICE_RECG_TEXT "CONFIG_BT_HFP_AG_VOICE_RECG_TEXT"),
      [`CONFIG_BT_HFP_AG_ENH_VOICE_RECG`](../kconfig.md#CONFIG_BT_HFP_AG_ENH_VOICE_RECG "CONFIG_BT_HFP_AG_ENH_VOICE_RECG"),
      [`CONFIG_BT_HFP_AG_VOICE_TAG`](../kconfig.md#CONFIG_BT_HFP_AG_VOICE_TAG "CONFIG_BT_HFP_AG_VOICE_TAG"),
      [`CONFIG_BT_HFP_AG_HF_INDICATORS`](../kconfig.md#CONFIG_BT_HFP_AG_HF_INDICATORS "CONFIG_BT_HFP_AG_HF_INDICATORS"),
      [`CONFIG_BT_HFP_AG_HF_INDICATOR_ENH_SAFETY`](../kconfig.md#CONFIG_BT_HFP_AG_HF_INDICATOR_ENH_SAFETY "CONFIG_BT_HFP_AG_HF_INDICATOR_ENH_SAFETY"),
      [`CONFIG_BT_HFP_AG_HF_INDICATOR_BATTERY`](../kconfig.md#CONFIG_BT_HFP_AG_HF_INDICATOR_BATTERY "CONFIG_BT_HFP_AG_HF_INDICATOR_BATTERY"), and
      [`CONFIG_BT_HFP_AG_REJECT_CALL`](../kconfig.md#CONFIG_BT_HFP_AG_REJECT_CALL "CONFIG_BT_HFP_AG_REJECT_CALL").
    - Add a callback function `get_ongoing_call()` to [`bt_hfp_ag_cb`](../doxygen/html/structbt__hfp__ag__cb.md).
    - [`bt_hfp_ag_ongoing_calls()`](../doxygen/html/group__bt__hfp__ag.md#ga5614bf3f1de11959a0364f458523e06e)
    - Support the classic L2CAP signaling echo request and response feature, including
      [`bt_l2cap_br_echo_cb`](../doxygen/html/structbt__l2cap__br__echo__cb.md), [`bt_l2cap_br_echo_cb_register()`](../doxygen/html/group__bt__l2cap.md#ga62c0115185f5026c1a842848dc5336ce),
      [`bt_l2cap_br_echo_cb_unregister()`](../doxygen/html/group__bt__l2cap.md#ga00ef7d0a42d8e544b195172af44b88b2), [`bt_l2cap_br_echo_req()`](../doxygen/html/group__bt__l2cap.md#ga3c6ad17ba18f5c00e39a379ed735de21), and
      [`bt_l2cap_br_echo_rsp()`](../doxygen/html/group__bt__l2cap.md#ga8ebf537cc7e4c0a68a320f9c65c94b05).
    - [`bt_a2dp_get_conn()`](../doxygen/html/a2dp_8h.md#a09470ceb08b66661d63c951736f34a5d)
    - [`bt_rfcomm_send_rpn_cmd()`](../doxygen/html/group__bt__rfcomm.md#gab38378db71d7f4631e47742ce4a5c59d)
- Build system

  - Sysbuild

    - Firmware loader image setup/selection support added to sysbuild when using
      `SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER` via
      `SB_CONFIG_FIRMWARE_LOADER` e.g. `SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR`
      for selecting [SMP server](../samples/subsys/mgmt/mcumgr/smp_svr/README.md#smp-svr "Implement a Simple Management Protocol (SMP) server.").
    - Single app RAM load support added to sysbuild using
      `SB_CONFIG_MCUBOOT_MODE_SINGLE_APP_RAM_LOAD`.
- Counter

  - [`counter_reset()`](../doxygen/html/group__counter__interface.md#ga225705f1f6f3bef127de8ef84dcfba4e)
- Debug

  - Core Dump

    - [`CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP`](../kconfig.md#CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP "CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP"), enabled by default for ARM Cortex M when [`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN`](../kconfig.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN "CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN") is selected.
    - [`CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY`](../kconfig.md#CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY "CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY")
    - [`CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY_SIZE`](../kconfig.md#CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY_SIZE "CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY_SIZE")
- Display

  > - Added [`display_clear()`](../doxygen/html/group__display__interface.md#ga62a6cd9e338aa07f789de60e64d3b3c4) API to allow clearing the display content in a standardized way.
  > - Character Frame Buffer (CFB) subsystem now supports drawing circles via [`cfb_draw_circle()`](../doxygen/html/group__monochrome__character__framebuffer.md#ga2a87d5fd58bb7a56081668313f7038f6).
- I2C

  - [`i2c_configure_dt()`](../doxygen/html/group__i2c__interface.md#ga780c4b50a3dc89c01a98c432554c2795).
  - [`I2C_DEVICE_DT_DEINIT_DEFINE`](../doxygen/html/group__i2c__interface.md#ga831cf78c11ebfceb65315995504cb7fb)
  - [`I2C_DEVICE_DT_INST_DEINIT_DEFINE`](../doxygen/html/group__i2c__interface.md#ga9c7a8248802760a2f9509e76377fb38a)
- I3C

  - [`CONFIG_I3C_MODE`](../kconfig.md#CONFIG_I3C_MODE "CONFIG_I3C_MODE")
  - [`CONFIG_I3C_CONTROLLER_ROLE_ONLY`](../kconfig.md#CONFIG_I3C_CONTROLLER_ROLE_ONLY "CONFIG_I3C_CONTROLLER_ROLE_ONLY")
  - [`CONFIG_I3C_TARGET_ROLE_ONLY`](../kconfig.md#CONFIG_I3C_TARGET_ROLE_ONLY "CONFIG_I3C_TARGET_ROLE_ONLY")
  - [`CONFIG_I3C_DUAL_ROLE`](../kconfig.md#CONFIG_I3C_DUAL_ROLE "CONFIG_I3C_DUAL_ROLE")
  - [`i3c_ccc_do_rstdaa()`](../doxygen/html/group__i3c__ccc.md#gac8bdf8d14db5e7fd06846637253cbb76)
- Kernel

> - `K_TIMEOUT_ABS_SEC`
> - [`timespec_add()`](../doxygen/html/group__timeutil__timespec__apis.md#ga81026756e417d086b4f53306d04c8d10)
> - [`timespec_compare()`](../doxygen/html/group__timeutil__timespec__apis.md#gafa281a298f8b2f011875bb00094260fc)
> - [`timespec_equal()`](../doxygen/html/group__timeutil__timespec__apis.md#gaedc15d71f9eee8e243c070a3e07d919f)
> - [`timespec_is_valid()`](../doxygen/html/group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)
> - [`timespec_negate()`](../doxygen/html/group__timeutil__timespec__apis.md#ga38216267ef6ca24e2b05d77104f5837a)
> - [`timespec_normalize()`](../doxygen/html/group__timeutil__timespec__apis.md#ga4a0d4891eb6aef6543b1992566729f6c)
> - [`timespec_from_timeout()`](../doxygen/html/group__timeutil__repr__apis.md#gab9b5ccdfd7abeaf7a05ebf273cb4d022)
> - [`timespec_to_timeout()`](../doxygen/html/group__timeutil__repr__apis.md#gac4262e7e4ebc2af52d21a18744d50169)
> - [`k_heap_array_get()`](../doxygen/html/group__heap__apis.md#ga3aa215396381e1513edf50bd9563dee5)

- LVGL (Light and Versatile Graphics Library)

  > - The LVGL module was synchronized to v9.3, bringing numerous upstream improvements and new features.
  > - LVGL subsystem now supports multiple simultaneous displays, including proper input device-to-display binding.
  > - Added L8/Y8 pixel format support for displays such as SSD1327, SSD1320, SSD1322, and ST75256.
  > - [`CONFIG_LV_Z_COLOR_MONO_HW_INVERSION`](../kconfig.md#CONFIG_LV_Z_COLOR_MONO_HW_INVERSION "CONFIG_LV_Z_COLOR_MONO_HW_INVERSION")
- LoRaWAN
  :   - [`lorawan_request_link_check()`](../doxygen/html/group__lorawan__api.md#gaed19bb9c528f8f21104201fd0816e3a9)
- Management

  - MCUmgr

    - Firmware loader support added to image mgmt group using
      [`CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER`](../kconfig.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER "CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER").
    - Optional boot mode (using retention boot mode) added to OS group reset command using
      [`CONFIG_MCUMGR_GRP_OS_RESET_BOOT_MODE`](../kconfig.md#CONFIG_MCUMGR_GRP_OS_RESET_BOOT_MODE "CONFIG_MCUMGR_GRP_OS_RESET_BOOT_MODE").
- Networking:

  - CoAP

    - [`COAPS_SERVICE_DEFINE`](../doxygen/html/group__coap__service.md#ga1ec49f2bc2c378431c4721080a13d11d)
  - DHCPv4

    - [`CONFIG_NET_DHCPV4_INIT_REBOOT`](../kconfig.md#CONFIG_NET_DHCPV4_INIT_REBOOT "CONFIG_NET_DHCPV4_INIT_REBOOT")
  - DNS

    - [`dns_resolve_service()`](../doxygen/html/group__dns__resolve.md#gaf28f6f8baa97d0b2341e1bdc02b6cb8c)
    - [`dns_resolve_reconfigure_with_interfaces()`](../doxygen/html/group__dns__resolve.md#ga211f9c8a5588186607e9257c4451f64d)
  - HTTP

    - [`CONFIG_HTTP_SERVER_COMPRESSION`](../kconfig.md#CONFIG_HTTP_SERVER_COMPRESSION "CONFIG_HTTP_SERVER_COMPRESSION")
  - IPv4

    - [`CONFIG_NET_IPV4_MTU`](../kconfig.md#CONFIG_NET_IPV4_MTU "CONFIG_NET_IPV4_MTU")
  - LwM2M

    - [`CONFIG_LWM2M_SERVER_BOOTSTRAP_ON_FAIL`](../kconfig.md#CONFIG_LWM2M_SERVER_BOOTSTRAP_ON_FAIL "CONFIG_LWM2M_SERVER_BOOTSTRAP_ON_FAIL")
    - Implemented Greater Than, Less Than and Step observe attributes handling
      (see [`CONFIG_LWM2M_MAX_NOTIFIED_NUMERICAL_RES_TRACKED`](../kconfig.md#CONFIG_LWM2M_MAX_NOTIFIED_NUMERICAL_RES_TRACKED "CONFIG_LWM2M_MAX_NOTIFIED_NUMERICAL_RES_TRACKED")).
  - Misc

    - [`net_if_oper_state_change_time()`](../doxygen/html/group__net__if.md#gabae216ba527bdfcd945ef19fb48e56be)
  - MQTT

    - [`CONFIG_MQTT_VERSION_5_0`](../kconfig.md#CONFIG_MQTT_VERSION_5_0 "CONFIG_MQTT_VERSION_5_0")
    - [`mqtt_transport.if_name`](../doxygen/html/structmqtt__transport.md#a7cfdf50105a275612dbda28e7c02808e)
  - OpenThread

    - Moved OpenThread-related Kconfig options from [subsys/net/l2/openthread/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/openthread/Kconfig)
      to [modules/openthread/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig).
    - Refactored OpenThread networking API, see the OpenThread section of the
      [migration guide](migration-guide-4.2.md#migration-4-2).
    - [`CONFIG_OPENTHREAD_SYS_INIT`](../kconfig.md#CONFIG_OPENTHREAD_SYS_INIT "CONFIG_OPENTHREAD_SYS_INIT")
    - [`CONFIG_OPENTHREAD_SYS_INIT_PRIORITY`](../kconfig.md#CONFIG_OPENTHREAD_SYS_INIT_PRIORITY "CONFIG_OPENTHREAD_SYS_INIT_PRIORITY")
  - SNTP

    - [`sntp_init_async()`](../doxygen/html/group__sntp.md#ga3a45c2b5af5e30b5cbd153368fc7ec3d)
    - [`sntp_send_async()`](../doxygen/html/group__sntp.md#gab6adcd7259bdfa841b57e535c380508d)
    - [`sntp_read_async()`](../doxygen/html/group__sntp.md#gac73db957041a6814abb286fd9143ddb5)
    - [`sntp_close_async()`](../doxygen/html/group__sntp.md#gaeb595e89c56fbb619010e3c8d7b2b5b1)
  - Sockets

    - [`CONFIG_NET_SOCKETS_INET_RAW`](../kconfig.md#CONFIG_NET_SOCKETS_INET_RAW "CONFIG_NET_SOCKETS_INET_RAW")
    - [`socket_offload_dns_enable()`](../doxygen/html/socket__offload_8h.md#a0d0123d234cd292282a272cb2e2eeb3c)
    - Added a new documentation page for [Socket Services](../connectivity/networking/api/socket_service.md#socket-service-interface) library.
    - New socket options:

      - [`IP_MULTICAST_LOOP`](../doxygen/html/group__bsd__sockets.md#ga5481dc4543c45fa31bf769119057a259)
      - [`IPV6_MULTICAST_LOOP`](../doxygen/html/group__bsd__sockets.md#ga2e5d89b45fea8bd9ebc6bb781877adb0)
      - [`TLS_CERT_VERIFY_RESULT`](../doxygen/html/group__secure__sockets__options.md#ga5100c3fe08cbf63e782318dec2bba6ee)
  - Wi-Fi

    - [`CONFIG_WIFI_USAGE_MODE`](../kconfig.md#CONFIG_WIFI_USAGE_MODE "CONFIG_WIFI_USAGE_MODE")
    - Added a new section to the Wi-Fi Management documentation
      (`doc/connectivity/networking/api/wifi.rst`) with step-by-step instructions for generating
      test certificates for Wi-Fi using FreeRADIUS scripts. This helps users reproduce the process
      for their own test environments.
    - Changed the hostap IPC mechanism from socketpair to k\_fifo. Depending on the enabled Wi-Fi configuration options, this can save up to 6-8 kB memory when using native Wi-Fi stack.
  - zperf

    - [`CONFIG_ZPERF_SESSION_PER_THREAD`](../kconfig.md#CONFIG_ZPERF_SESSION_PER_THREAD "CONFIG_ZPERF_SESSION_PER_THREAD")
    - `zperf_upload_params.data_loader`
    - [`CONFIG_NET_ZPERF_SERVER`](../kconfig.md#CONFIG_NET_ZPERF_SERVER "CONFIG_NET_ZPERF_SERVER")
- PCIe

  > - [`CONFIG_NVME_PRP_PAGE_SIZE`](../kconfig.md#CONFIG_NVME_PRP_PAGE_SIZE "CONFIG_NVME_PRP_PAGE_SIZE")
- Power management

  > - [`CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ`](../kconfig.md#CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ "CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ")
  > - [`CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ`](../kconfig.md#CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ "CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ")
  > - `CONFIG_PM_DEVICE_DRIVER_NEEDS_DEDICATED_WQ`
  > - [`CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_STACK_SIZE`](../kconfig.md#CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_STACK_SIZE "CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_STACK_SIZE")
  > - [`CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_PRIO`](../kconfig.md#CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_PRIO "CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_PRIO")
  > - [`CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_INIT_PRIO`](../kconfig.md#CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_INIT_PRIO "CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_INIT_PRIO")
  > - [`CONFIG_PM_DEVICE_RUNTIME_ASYNC`](../kconfig.md#CONFIG_PM_DEVICE_RUNTIME_ASYNC "CONFIG_PM_DEVICE_RUNTIME_ASYNC")
- SPI

  - [`SPI_DEVICE_DT_DEINIT_DEFINE`](../doxygen/html/group__spi__interface.md#gaf98b0cb38cb316b9fe05146bba34126d)
  - [`SPI_DEVICE_DT_INST_DEINIT_DEFINE`](../doxygen/html/group__spi__interface.md#ga50cbb6845d230033f192f1e716fd9f2b)
- Sensor

  - [`sensor_value_to_deci()`](../doxygen/html/group__sensor__interface.md#gabbcb8ad4b9484cba77ae65e2d3ba7457)
  - [`sensor_value_to_centi()`](../doxygen/html/group__sensor__interface.md#gae812fb481bfe3a8053f0fc23f8617434)
- Stepper

  - [`stepper_stop()`](../doxygen/html/group__stepper__interface.md#gaa049d39fe611a86904e7a60fc7005abd)
- Storage

  - [`flash_area_copy()`](../doxygen/html/group__flash__area__api.md#gaa50bb1b455a9004f9c24e4af9fd74cd7)
- Sys

  - [`util_eq()`](../doxygen/html/group__sys-util.md#gaca458acb618a71bd95cb05fe8179d602)
  - [`util_memeq()`](../doxygen/html/group__sys-util.md#gaccffc30e3554212d2cc3803c44cf86f8)
  - [`sys_clock_gettime()`](../doxygen/html/group__clock__apis.md#ga92bad374219a4cd32299569c94907877)
  - [`sys_clock_settime()`](../doxygen/html/group__clock__apis.md#ga297e885a8a95c762ae882e61f7d381b4)
  - [`sys_clock_nanosleep()`](../doxygen/html/group__clock__apis.md#ga01ca6f2ad006ed530ffec06c262ae380)
- USB

  - [`uvc_set_video_dev()`](../doxygen/html/group__usbd__uvc.md#gac4caf401c52d9a3755ace3e8dfa884a3)
- UpdateHub

  - [`updatehub_report_error()`](../doxygen/html/group__updatehub.md#gaa3606855ac680341e7b568421562e165)
- Video

  - [`video_api_ctrl_t`](../doxygen/html/group__video__interface.md#ga522b4027fc6f22bf59f4face3c97e303)
  - [`video_query_ctrl()`](../doxygen/html/group__video__interface.md#ga8813a656a66adc6bfb10fb7f27194898)
  - [`video_print_ctrl()`](../doxygen/html/group__video__interface.md#ga2bff04c6abc344350d6b0036289a701e)
  - [`video_api_selection_t`](../doxygen/html/group__video__interface.md#gab4d2eb34f8ccc95fa6dcda7848f4408a)
  - [`video_set_selection()`](../doxygen/html/group__video__interface.md#ga21f2e7d6b5ec0c50ceeee580c6272613)
  - [`video_get_selection()`](../doxygen/html/group__video__interface.md#ga917889d41696ab12c92475b85caec13f)
  - [video-sw-generator](../snippets/video-sw-generator/README.md#snippet-video-sw-generator)
  - [`video_get_csi_link_freq()`](../doxygen/html/group__video__interface.md#ga41e450607b4dc062fac682728ec7a79d)
  - [`VIDEO_CID_LINK_FREQ`](../doxygen/html/group__video__controls.md#ga2142e2819c445b70d82067a3cfb193c8)
  - [`VIDEO_CID_AUTO_WHITE_BALANCE`](../doxygen/html/group__video__controls.md#ga7e2ce049ed534e1c29ac47d33013e180) and other controls from the BASE control class.
  - [`VIDEO_CID_EXPOSURE_ABSOLUTE`](../doxygen/html/group__video__controls.md#ga036f78623bcae18ea9627d45d1209245) and other controls from the CAMERA control class.
  - [`VIDEO_PIX_FMT_Y10`](../doxygen/html/group__video__pixel__formats.md#ga0506f2c8aa1a82f02fc9383d99b43bc3) and `Y12`, `Y14`, `Y16` variants
  - [`VIDEO_PIX_FMT_SRGGB10P`](../doxygen/html/group__video__pixel__formats.md#ga604d2f3501407546aa924e2fdb37be2f) and `12P`, `14P` variants, for all 4 bayer variants.
  - [`video_buffer.index`](../doxygen/html/structvideo__buffer.md#acb948f9f124f9f2bfe9b19b44af60854) field
  - [`video_ctrl_query.int_menu`](../doxygen/html/structvideo__ctrl__query.md#ad0d74a650e83dece50ca2d46d9e5c750) field
  - [`VIDEO_MIPI_CSI2_DT_NULL`](../doxygen/html/group__video__interface.md#ga59d6f35198b6412a9aa78c094ecfaa19) and other MIPI standard values
- ZBus

  - Zbus has achieved stable status with the release of API version v1.0.0.
  - Runtime observers can work without heap. Now it is possible to choose between static, dynamic,
    and none allocation for the runtime observers nodes.
  - Runtime observers using [`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE`](../kconfig.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE "CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE") must use
    the new function [`zbus_chan_add_obs_with_node()`](../doxygen/html/group__zbus__apis.md#ga6f2b8db3a13546e3d0fd095ff9cd37ba).
  - [`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC`](../kconfig.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC "CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC")
  - [`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC`](../kconfig.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC "CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC")
  - [`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE`](../kconfig.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE "CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE")
  - [`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_POOL_SIZE`](../kconfig.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_POOL_SIZE "CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_POOL_SIZE")

## New Boards

- Adafruit Industries, LLC

  > - [Adafruit Feather ESP32S2](../boards/adafruit/feather_esp32s2/doc/adafruit_feather_esp32s2.md#adafruit_feather_esp32s2) (`adafruit_feather_esp32s2`)
  > - [Adafruit Feather ESP32S2 TFT](../boards/adafruit/feather_esp32s2/doc/adafruit_feather_esp32s2_tft.md#adafruit_feather_esp32s2_tft) (`adafruit_feather_esp32s2_tft`)
  > - [Adafruit Feather ESP32S2 TFT Reverse](../boards/adafruit/feather_esp32s2/doc/adafruit_feather_esp32s2_tft_reverse.md#adafruit_feather_esp32s2_tft_reverse) (`adafruit_feather_esp32s2_tft_reverse`)
  > - [Adafruit Feather ESP32S3](../boards/adafruit/feather_esp32s3/doc/index.md#adafruit_feather_esp32s3) (`adafruit_feather_esp32s3`)
  > - [Adafruit Feather ESP32S3 TFT](../boards/adafruit/feather_esp32s3_tft/doc/index.md#adafruit_feather_esp32s3_tft) (`adafruit_feather_esp32s3_tft`)
  > - [Adafruit ESP32-S3 Reverse TFT Feather](../boards/adafruit/feather_esp32s3_tft_reverse/doc/index.md#adafruit_feather_esp32s3_tft_reverse) (`adafruit_feather_esp32s3_tft_reverse`)
- Advanced Micro Devices (AMD), Inc.

  > - [Versal 2 RPU development board](../boards/amd/versal2_rpu/doc/index.md#versal2_rpu) (`versal2_rpu`)
  > - [Versal NET RPU development board](../boards/amd/versalnet_rpu/doc/index.md#versalnet_rpu) (`versalnet_rpu`)
- Aesc Silicon

  > - [ElemRV-N](../boards/aesc/elemrv/doc/index.md#elemrv) (`elemrv`)
- Ai-Thinker Co., Ltd.

  > - [Ai-Thinker WB2-12F development board](../boards/aithinker/ai_wb2_12f/doc/index.md#ai_wb2_12f) (`ai_wb2_12f`)
- Ambiq Micro, Inc.

  > - [Apollo510 SOC Evaluation Board](../boards/ambiq/apollo510_evb/doc/index.md#apollo510_evb) (`apollo510_evb`)
- Analog Devices, Inc.

  > - [max32657evkit](../boards/adi/max32657evkit/doc/index.md#max32657evkit) (`max32657evkit`)
- Arduino

  > - [Arduino Nano Matter](../boards/arduino/nano_matter/doc/index.md#arduino_nano_matter) (`arduino_nano_matter`)
  > - [Arduino Portenta C33](../boards/arduino/portenta_c33/doc/index.md#arduino_portenta_c33) (`arduino_portenta_c33`)
- ARM Ltd.

  > - [MPS4](../boards/arm/mps4/doc/index.md#mps4) (`mps4`)
- BeagleBoard.org Foundation

  > - [PocketBeagle 2](../boards/beagle/pocketbeagle_2/doc/index.md#pocketbeagle_2) (`pocketbeagle_2`)
- Blues Wireless

  > - [Cygnet](../boards/blues/cygnet/doc/index.md#cygnet) (`cygnet`)
- Bouffalo Lab (Nanjing) Co., Ltd.

  > - [BL604E IOT DVK development board](../boards/bflb/bl60x/bl604e_iot_dvk/doc/index.md#bl604e_iot_dvk) (`bl604e_iot_dvk`)
- Doctors of Intelligence & Technology

  > - [DT-BL10 coexistence Module Development Kit](../boards/doiting/dt_bl10_devkit/doc/index.md#dt_bl10_devkit) (`dt_bl10_devkit`)
- ENE Technology, Inc.

  > - [ENE KB1062\_EVB](../boards/ene/kb1062_evb/doc/index.md#kb1062_evb) (`kb1062_evb`)
- Espressif Systems

  > - [ESP32-DevKitC](../boards/espressif/esp32_devkitc/doc/index.md#esp32_devkitc) (`esp32_devkitc`)
- Ezurio

  > - [BL54L15 DVK](../boards/ezurio/bl54l15_dvk/doc/bl54l15_dvk.md#bl54l15_dvk) (`bl54l15_dvk`)
  > - [BL54L15u DVK](../boards/ezurio/bl54l15u_dvk/doc/bl54l15u_dvk.md#bl54l15u_dvk) (`bl54l15u_dvk`)
- FANKE Technology Co., Ltd.

  > - [FK743M5-XIH6](../boards/fanke/fk743m5_xih6/doc/index.md#fk743m5_xih6) (`fk743m5_xih6`)
- IAR Systems AB

  > - [STM32F429II-ACA](../boards/iar/stm32f429ii_aca/doc/index.md#stm32f429ii_aca) (`stm32f429ii_aca`)
- Infineon Technologies

  > - [XMC7200 Evaluation Kit](../boards/infineon/kit_xmc72_evk/doc/index.md#kit_xmc72_evk) (`kit_xmc72_evk`)
- Intel Corporation

  > - [Bartlett Lake P CRB](../boards/intel/btl/doc/index.md#intel_btl_s_crb) (`intel_btl_s_crb`)
- ITE Tech. Inc.

  > - [IT51XXX series](../boards/ite/it515xx_evb/doc/index.md#it515xx_evb) (`it515xx_evb`)
- KWS Computersysteme Gmbh

  > - [Pico2-SPE](../boards/kws/pico2_spe/doc/index.md#pico2_spe) (`pico2_spe`)
  > - [Pico-SPE](../boards/kws/pico_spe/doc/index.md#pico_spe) (`pico_spe`)
- Lilygo Shenzhen Xinyuan Electronic Technology Co., Ltd

  > - [T-Dongle S3](../boards/lilygo/tdongle_s3/doc/index.md#tdongle_s3) (`tdongle_s3`)
  > - [TTGO TBeam](../boards/lilygo/ttgo_tbeam/doc/index.md#ttgo_tbeam) (`ttgo_tbeam`)
  > - [TTGO T-OI-PLUS](../boards/lilygo/ttgo_toiplus/doc/index.md#ttgo_toiplus) (`ttgo_toiplus`)
  > - [T-Watch S3](../boards/lilygo/twatch_s3/doc/index.md#twatch_s3) (`twatch_s3`)
- M5Stack

  > - [Fire](../boards/m5stack/m5stack_fire/doc/index.md#m5stack_fire) (`m5stack_fire`)
- Microchip Technology Inc.

  > - [MEC17xxEVB ASSY6941](../boards/microchip/mec_assy6941/doc/index.md#mec_assy6941) (`mec_assy6941`)
  > - [SAMA7G54 Evaluation Kit](../boards/microchip/sam/sama7g54_ek/doc/index.md#sama7g54_ek) (`sama7g54_ek`)
- MikroElektronika d.o.o.

  > - [MikroE Quail](../boards/mikroe/quail/doc/mikroe_quail.md#mikroe_quail) (`mikroe_quail`)
- Nordic Semiconductor

  > - [nRF54LM20 DK](../boards/nordic/nrf54lm20dk/doc/index.md#nrf54lm20dk) (`nrf54lm20dk`)
- Nuvoton Technology Corporation

  > - [NPCK3M8K\_EVB](../boards/nuvoton/npck3m8k_evb/doc/index.md#npck3m8k_evb) (`npck3m8k_evb`)
  > - [NUMAKER M55M1](../boards/nuvoton/numaker_m55m1/doc/index.md#numaker_m55m1) (`numaker_m55m1`)
- NXP Semiconductors

  > - [FRDM-MCXA153](../boards/nxp/frdm_mcxa153/doc/index.md#frdm_mcxa153) (`frdm_mcxa153`)
  > - [FRDM-MCXA166](../boards/nxp/frdm_mcxa166/doc/index.md#frdm_mcxa166) (`frdm_mcxa166`)
  > - [FRDM-MCXA276](../boards/nxp/frdm_mcxa276/doc/index.md#frdm_mcxa276) (`frdm_mcxa276`)
  > - [i.MX943 EVK](../boards/nxp/imx943_evk/doc/index.md#imx943_evk) (`imx943_evk`)
  > - [MCX-N9XX-EVK](../boards/nxp/mcx_n9xx_evk/doc/index.md#mcx_n9xx_evk) (`mcx_n9xx_evk`)
  > - [S32K148EVB-Q176](../boards/nxp/s32k148_evb/doc/index.md#s32k148_evb) (`s32k148_evb`)
- Octavo Systems LLC

  > - [OSD32MP1-BRK](../boards/oct/osd32mp1_brk/doc/osd32mp1_brk.md#osd32mp1_brk) (`osd32mp1_brk`)
- OpenHW Group

  > - [cv32a6\_genesys\_2](../boards/openhwgroup/cv32a6_genesys_2/doc/index.md#cv32a6_genesys_2) (`cv32a6_genesys_2`)
  > - [cv64a6\_genesys\_2](../boards/openhwgroup/cv64a6_genesys_2/doc/index.md#cv64a6_genesys_2) (`cv64a6_genesys_2`)
- Pimoroni Ltd.

  > - [Pimoroni Pico Plus2](../boards/pimoroni/pico_plus2/doc/index.md#pico_plus2) (`pico_plus2`)
- QEMU

  > - [QEMU Emulation for Renesas RX](../boards/qemu/rx/doc/index.md#qemu_rx) (`qemu_rx`)
- Raytac Corporation

  > - [AN54L15Q-DB](../boards/raytac/an54l15q_db/doc/index.md#raytac_an54l15q_db) (`raytac_an54l15q_db`)
  > - [AN7002Q-DB-5340](../boards/raytac/an7002q_db/doc/index.md#raytac_an7002q_db) (`raytac_an7002q_db`)
  > - [MDBT50Q-CX-40 Dongle](../boards/raytac/mdbt50q_cx_40_dongle/doc/index.md#raytac_mdbt50q_cx_40_dongle) (`raytac_mdbt50q_cx_40_dongle`)
- Renesas Electronics Corporation

  > - [RA8P1 Evaluation Kit](../boards/renesas/ek_ra8p1/doc/index.md#ek_ra8p1) (`ek_ra8p1`)
  > - [Renesas Starter Kit for RX130](../boards/renesas/rsk_rx130/doc/index.md#rsk_rx130) (`rsk_rx130`)
  > - [RZ/A2M Evaluation Kit](../boards/renesas/rza2m_evk/doc/index.md#rza2m_evk) (`rza2m_evk`)
  > - [RZ/A3UL SMARC Evaluation Board Kit](../boards/renesas/rza3ul_smarc/doc/index.md#rza3ul_smarc) (`rza3ul_smarc`)
  > - [RZ/G2L SMARC Evaluation Board Kit](../boards/renesas/rzg2l_smarc/doc/index.md#rzg2l_smarc) (`rzg2l_smarc`)
  > - [RZ/G2LC SMARC Evaluation Board Kit](../boards/renesas/rzg2lc_smarc/doc/index.md#rzg2lc_smarc) (`rzg2lc_smarc`)
  > - [RZ/G2UL SMARC Evaluation Board Kit](../boards/renesas/rzg2ul_smarc/doc/index.md#rzg2ul_smarc) (`rzg2ul_smarc`)
  > - [Renesas Starter Kit+ for RZ/N2L](../boards/renesas/rzn2l_rsk/doc/index.md#rzn2l_rsk) (`rzn2l_rsk`)
  > - [Renesas Starter Kit+ for RZ/T2L](../boards/renesas/rzt2l_rsk/doc/index.md#rzt2l_rsk) (`rzt2l_rsk`)
  > - [Renesas Starter Kit+ for RZ/T2M](../boards/renesas/rzt2m_rsk/doc/index.md#rzt2m_rsk) (`rzt2m_rsk`)
  > - [RZ/V2H Evaluation Board Kit](../boards/renesas/rzv2h_evk/doc/index.md#rzv2h_evk) (`rzv2h_evk`)
  > - [RZ/V2L SMARC Evaluation Board Kit](../boards/renesas/rzv2l_smarc/doc/index.md#rzv2l_smarc) (`rzv2l_smarc`)
  > - [RZ/V2N Evaluation Board Kit](../boards/renesas/rzv2n_evk/doc/index.md#rzv2n_evk) (`rzv2n_evk`)
- Seeed Technology Co., Ltd

  > - [XIAO MG24](../boards/seeed/xiao_mg24/doc/index.md#xiao_mg24) (`xiao_mg24`)
  > - [XIAO RA4M1](../boards/seeed/xiao_ra4m1/doc/index.md#xiao_ra4m1) (`xiao_ra4m1`)
- sensry.io

  > - [Ganymed Starter Kit (SK)](../boards/sensry/ganymed_sk/doc/index.md#ganymed_sk) (`ganymed_sk`)
- Shanghai Ruiside Electronic Technology Co., Ltd.

  > - [ART-Pi2](../boards/ruiside/art_pi2/doc/index.md#art_pi2) (`art_pi2`)
  > - [RA8D1 Vision Board](../boards/ruiside/ra8d1_vision_board/doc/index.md#ra8d1_vision_board) (`ra8d1_vision_board`)
- Silicon Laboratories

  > - [SiWx917 Wi-Fi 6 and Bluetooth LE 8 MB Flash + 8 MB ext PSRAM Radio Board (SLWRB4342A)](../boards/silabs/radio_boards/siwx917_rb4342a/doc/index.md#siwx917_rb4342a) (`siwx917_rb4342a`)
  > - [EFR32xG21 2.4 GHz 20 dBm (SLWRB4180B)](../boards/silabs/radio_boards/slwrb4180b/doc/index.md#slwrb4180b) (`slwrb4180b`)
- Space Cubics, LLC

  > - [SC-OBC Module A1](../boards/sc/scobc_a1/doc/index.md#scobc_a1) (`scobc_a1`)
- STMicroelectronics

  > - [Nucleo F439ZI](../boards/st/nucleo_f439zi/doc/index.md#nucleo_f439zi) (`nucleo_f439zi`)
  > - [Nucleo U385RG Q](../boards/st/nucleo_u385rg_q/doc/index.md#nucleo_u385rg_q) (`nucleo_u385rg_q`)
  > - [Nucleo WBA65RI](../boards/st/nucleo_wba65ri/doc/nucleo_wba65ri.md#nucleo_wba65ri) (`nucleo_wba65ri`)
  > - [STM32H757I Eval](../boards/st/stm32h757i_eval/doc/index.md#stm32h757i_eval) (`stm32h757i_eval`)
  > - [STM32MP135F-DK Discovery](../boards/st/stm32mp135f_dk/doc/index.md#stm32mp135f_dk) (`stm32mp135f_dk`)
  > - [STM32MP257F-EV1 Evaluation Board](../boards/st/stm32mp257f_ev1/doc/index.md#stm32mp257f_ev1) (`stm32mp257f_ev1`)
  > - [STM32U5G9J Discovery Kit 1](../boards/st/stm32u5g9j_dk1/doc/index.md#stm32u5g9j_dk1) (`stm32u5g9j_dk1`)
  > - [STM32U5G9J Discovery Kit](../boards/st/stm32u5g9j_dk2/doc/index.md#stm32u5g9j_dk2) (`stm32u5g9j_dk2`)
- Texas Instruments

  > - [TI AM243x-EVM](../boards/ti/am243x_evm/doc/index.md#am243x_evm) (`am243x_evm`)
  > - [MSPM0G3507 Launchpad](../boards/ti/lp_mspm0g3507/doc/index.md#lp_mspm0g3507) (`lp_mspm0g3507`)
  > - [SK-AM64](../boards/ti/sk_am64/doc/index.md#sk_am64) (`sk_am64`)
- u-blox

  > - [EVK-IRIS-W106-RW612](../boards/u-blox/ubx_evk_iris_w1/doc/index.md#ubx_evk_iris_w1) (`ubx_evk_iris_w1`)
- Variscite Ltd.

  > - [DART-MX8M-PLUS](../boards/variscite/imx8mp_var_dart/doc/index.md#imx8mp_var_dart) (`imx8mp_var_dart`)
  > - [VAR-SOM-MX8M-PLUS](../boards/variscite/imx8mp_var_som/doc/index.md#imx8mp_var_som) (`imx8mp_var_som`)
  > - [DART-MX93](../boards/variscite/imx93_var_dart/doc/index.md#imx93_var_dart) (`imx93_var_dart`)
  > - [VAR-SOM-MX93](../boards/variscite/imx93_var_som/doc/index.md#imx93_var_som) (`imx93_var_som`)
- Waveshare Electronics

  > - [ESP32-S3-Matrix](../boards/waveshare/esp32s3_matrix/doc/index.md#esp32s3_matrix) (`esp32s3_matrix`)
  > - [RP2040-Plus](../boards/waveshare/rp2040_plus/doc/index.md#rp2040_plus) (`rp2040_plus`)
- WeAct Studio

  > - [BluePill Plus CH32V203](../boards/weact/bluepillplus_ch32v203/doc/index.md#bluepillplus_ch32v203) (`bluepillplus_ch32v203`)
  > - [STM32F446 Core Board V1.1](../boards/weact/stm32f446_core/doc/index.md#weact_stm32f446_core) (`weact_stm32f446_core`)
- WinChipHead

  > - [WCH CH32V003F4P6 Development Board](../boards/wch/ch32v003f4p6_dev_board/doc/index.md#ch32v003f4p6_dev_board) (`ch32v003f4p6_dev_board`)
  > - [WCH CH32V006EVT](../boards/wch/ch32v006evt/doc/index.md#ch32v006evt) (`ch32v006evt`)
  > - [WCH CH32V303VCT6\_EVT](../boards/wch/ch32v303vct6_evt/doc/index.md#ch32v303vct6_evt) (`ch32v303vct6_evt`)
  > - [WCH LinkW](../boards/wch/linkw/doc/index.md#linkw) (`linkw`)
- WIZnet Co., Ltd.

  > - [W5500-EVB-Pico2](../boards/wiznet/w5500_evb_pico2/doc/index.md#w5500_evb_pico2) (`w5500_evb_pico2`)
- Würth Elektronik GmbH.

  > - [Ophelia-IV DK](../boards/we/ophelia4ev/doc/index.md#ophelia4ev) (`ophelia4ev`)

### New shields

- [Arduino Giga Display Shield](../boards/shields/arduino_giga_display_shield/doc/index.md#arduino-giga-display-shield)
- [Arduino Modulino Buttons](../boards/shields/arduino_modulino_buttons/doc/index.md#arduino-modulino-buttons)
- [Arduino Modulino SmartLEDs](../boards/shields/arduino_modulino_smartleds/doc/index.md#arduino-modulino-smartleds)
- [DVP 20-pin OV7670](../boards/shields/dvp_20pin_ov7670/doc/index.md#dvp-20pin-ov7670)
- [EVAL AD4052 ARDZ](../boards/shields/eval_ad4052_ardz/doc/index.md#eval-ad4052-ardz)
- [EVAL ADXL367 ARDZ](../boards/shields/eval_adxl367_ardz/doc/index.md#eval-adxl367-ardz)
- [M5Stack Cardputer](../boards/shields/m5stack_cardputer/doc/index.md#m5stack-cardputer)
- [MikroElektronika LTE IoT10 Click](../boards/shields/mikroe_lte_iot10_click/doc/index.md#mikroe-lte-iot10-click-shield)
- [MikroElektronika Stepper 18 Click](../boards/shields/mikroe_stepper_18_click/doc/index.md#mikroe-stepper-18-click-shield)
- [MikroElektronika Stepper 19 Click](../boards/shields/mikroe_stepper_19_click/doc/index.md#mikroe-stepper-19-click-shield)
- [NPM2100 Evaluation Kit](../boards/shields/npm2100_ek/doc/index.md#npm2100-ek)
- [NXP ADTJA1101](../boards/shields/nxp_adtja1101/doc/index.md#nxp-adtja1101)
- [NXP M2 WiFi BT](../boards/shields/nxp_m2_wifi_bt/doc/index.md#nxp-m2-wifi-bt)
- [OpenThread RCP Arduino](../boards/shields/openthread_rcp_arduino/doc/index.md#openthread-rcp-arduino-shield)
- [RTK7 EKA6M3B00001BU](../boards/shields/rtk7eka6m3b00001bu/doc/index.md#rtk7eka6m3b00001bu)
- [RTKLCDPAR1S00001BE Display](../boards/shields/rtklcdpar1s00001be/doc/index.md#rtklcdpar1s00001be)
- [ST B-CAMS-IMX-MB1854](../boards/shields/st_b_cams_imx_mb1854/doc/index.md#st-b-cams-imx-mb1854)
- [ST MB1897 camera module](../boards/shields/st_mb1897_cam/doc/index.md#st-mb1897-cam)
- [ST STM32F4DIS CAM](../boards/shields/st_stm32f4dis_cam/doc/index.md#st-stm32f4dis-cam)
- [Waveshare Pico LCD 1.14](../boards/shields/waveshare_pico_lcd_1_14/doc/index.md#waveshare-pico-lcd-1-14)
- [Waveshare Pico OLED 1.3](../boards/shields/waveshare_pico_oled_1_3/doc/index.md#waveshare-pico-oled-1-3)
- [X-Nucleo-GFX01M2](../boards/shields/x_nucleo_gfx01m2/doc/index.md#x-nucleo-gfx01m2-shield)

## New Drivers

- ADC

  > - [`adi,ad4050-adc`](../build/dts/api/compatibles/adi,ad4050-adc.md#std-dtcompatible-adi-ad4050-adc)
  > - [`adi,ad4052-adc`](../build/dts/api/bindings/adc/adi,ad4052-adc.md#std-dtcompatible-adi-ad4052-adc)
  > - [`adi,ad4130-adc`](../build/dts/api/bindings/adc/adi,ad4130-adc.md#std-dtcompatible-adi-ad4130-adc)
  > - [`ene,kb106x-adc`](../build/dts/api/bindings/adc/ene,kb106x-adc.md#std-dtcompatible-ene-kb106x-adc)
  > - [`ite,it51xxx-adc`](../build/dts/api/bindings/adc/ite,it51xxx-adc.md#std-dtcompatible-ite-it51xxx-adc)
  > - [`microchip,mcp356xr`](../build/dts/api/bindings/adc/microchip,mcp356xr.md#std-dtcompatible-microchip-mcp356xr)
  > - [`realtek,rts5912-adc`](../build/dts/api/bindings/adc/realtek,rts5912-adc.md#std-dtcompatible-realtek-rts5912-adc)
  > - [`renesas,rz-adc`](../build/dts/api/bindings/adc/renesas,rz-adc.md#std-dtcompatible-renesas-rz-adc)
  > - [`silabs,siwx91x-adc`](../build/dts/api/bindings/adc/silabs,siwx91x-adc.md#std-dtcompatible-silabs-siwx91x-adc)
  > - [`ti,am335x-adc`](../build/dts/api/bindings/adc/ti,am335x-adc.md#std-dtcompatible-ti-am335x-adc)
  > - [`ti,cc23x0-adc`](../build/dts/api/bindings/adc/ti,cc23x0-adc.md#std-dtcompatible-ti-cc23x0-adc)
  > - [`wch,adc`](../build/dts/api/bindings/adc/wch,adc.md#std-dtcompatible-wch-adc)
- Audio

  > - [`ambiq,pdm`](../build/dts/api/bindings/audio/ambiq,pdm.md#std-dtcompatible-ambiq-pdm)
  > - [`maxim,max98091`](../build/dts/api/bindings/audio/maxim,max98091.md#std-dtcompatible-maxim-max98091)
  > - [`ti,pcm1681`](../build/dts/api/compatibles/ti,pcm1681.md#std-dtcompatible-ti-pcm1681)
  > - [`ti,tlv320aic3110`](../build/dts/api/bindings/audio/ti,tlv320aic3110.md#std-dtcompatible-ti-tlv320aic3110)
  > - [`wolfson,wm8962`](../build/dts/api/bindings/audio/wolfson,wm8962.md#std-dtcompatible-wolfson-wm8962)
- Auxiliary Display

  > - [`gpio-7-segment`](../build/dts/api/bindings/auxdisplay/gpio-7-segment.md#std-dtcompatible-gpio-7-segment)
- CAN

  > - [`adi,max32-can`](../build/dts/api/bindings/can/adi,max32-can.md#std-dtcompatible-adi-max32-can)
  > - [`renesas,rz-canfd`](../build/dts/api/bindings/can/renesas,rz-canfd.md#std-dtcompatible-renesas-rz-canfd)
  > - [`renesas,rz-canfd-global`](../build/dts/api/bindings/can/renesas,rz-canfd-global.md#std-dtcompatible-renesas-rz-canfd-global)
- Charger

  > - [`ti,bq25713`](../build/dts/api/bindings/charger/ti,bq25713.md#std-dtcompatible-ti-bq25713)
  > - [`x-powers,axp2101-charger`](../build/dts/api/bindings/charger/x-powers,axp2101-charger.md#std-dtcompatible-x-powers-axp2101-charger)
- Clock control

  > - [`bflb,bclk`](../build/dts/api/bindings/clock/bflb,bclk.md#std-dtcompatible-bflb-bclk)
  > - [`bflb,bl60x-clock-controller`](../build/dts/api/bindings/clock/bflb,bl60x-clock-controller.md#std-dtcompatible-bflb-bl60x-clock-controller)
  > - [`bflb,bl60x-pll`](../build/dts/api/bindings/clock/bflb,bl60x-pll.md#std-dtcompatible-bflb-bl60x-pll)
  > - [`bflb,bl60x-root-clk`](../build/dts/api/bindings/clock/bflb,bl60x-root-clk.md#std-dtcompatible-bflb-bl60x-root-clk)
  > - [`bflb,clock-controller`](../build/dts/api/bindings/clock/bflb,clock-controller.md#std-dtcompatible-bflb-clock-controller)
  > - [`ite,it51xxx-ecpm`](../build/dts/api/bindings/clock/ite,it51xxx-ecpm.md#std-dtcompatible-ite-it51xxx-ecpm)
  > - [`microchip,sam-pmc`](../build/dts/api/bindings/clock/microchip,sam-pmc.md#std-dtcompatible-microchip-sam-pmc)
  > - [`microchip,sama7g5-sckc`](../build/dts/api/bindings/clock/microchip,sama7g5-sckc.md#std-dtcompatible-microchip-sama7g5-sckc)
  > - [`nordic,nrf51-hfxo`](../build/dts/api/bindings/clock/nordic,nrf51-hfxo.md#std-dtcompatible-nordic-nrf51-hfxo)
  > - [`nordic,nrf52-hfxo`](../build/dts/api/bindings/clock/nordic,nrf52-hfxo.md#std-dtcompatible-nordic-nrf52-hfxo)
  > - [`nordic,nrf54l-hfxo`](../build/dts/api/bindings/clock/nordic,nrf54l-hfxo.md#std-dtcompatible-nordic-nrf54l-hfxo)
  > - [`nordic,nrfs-audiopll`](../build/dts/api/bindings/clock/nordic,nrfs-audiopll.md#std-dtcompatible-nordic-nrfs-audiopll)
  > - [`renesas,rx-cgc-pclk`](../build/dts/api/bindings/clock/renesas,rx-cgc-pclk.md#std-dtcompatible-renesas-rx-cgc-pclk)
  > - [`renesas,rx-cgc-pclk-block`](../build/dts/api/bindings/clock/renesas,rx-cgc-pclk-block.md#std-dtcompatible-renesas-rx-cgc-pclk-block)
  > - [`renesas,rx-cgc-pll`](../build/dts/api/bindings/clock/renesas,rx-cgc-pll.md#std-dtcompatible-renesas-rx-cgc-pll)
  > - [`renesas,rx-cgc-root-clock`](../build/dts/api/bindings/clock/renesas,rx-cgc-root-clock.md#std-dtcompatible-renesas-rx-cgc-root-clock)
  > - [`renesas,rza2m-cpg`](../build/dts/api/bindings/clock/renesas,rza2m-cpg.md#std-dtcompatible-renesas-rza2m-cpg)
  > - [`st,stm32mp13-cpu-clock-mux`](../build/dts/api/bindings/clock/st,stm32mp13-cpu-clock-mux.md#std-dtcompatible-st-stm32mp13-cpu-clock-mux)
  > - [`st,stm32mp13-pll-clock`](../build/dts/api/bindings/clock/st,stm32mp13-pll-clock.md#std-dtcompatible-st-stm32mp13-pll-clock)
  > - [`st,stm32mp2-rcc`](../build/dts/api/bindings/clock/st,stm32mp2-rcc.md#std-dtcompatible-st-stm32mp2-rcc)
  > - [`st,stm32u3-msi-clock`](../build/dts/api/bindings/clock/st,stm32u3-msi-clock.md#std-dtcompatible-st-stm32u3-msi-clock)
  > - [`ti,mspm0-clk`](../build/dts/api/bindings/clock/ti,mspm0-clk.md#std-dtcompatible-ti-mspm0-clk)
  > - [`ti,mspm0-osc`](../build/dts/api/bindings/clock/ti,mspm0-osc.md#std-dtcompatible-ti-mspm0-osc)
  > - [`ti,mspm0-pll`](../build/dts/api/bindings/clock/ti,mspm0-pll.md#std-dtcompatible-ti-mspm0-pll)
  > - [`wch,ch32v20x_30x-pll-clock`](../build/dts/api/bindings/clock/wch,ch32v20x_30x-pll-clock.md#std-dtcompatible-wch-ch32v20x_30x-pll-clock)
- Comparator

  > - [`ite,it51xxx-vcmp`](../build/dts/api/bindings/comparator/ite,it51xxx-vcmp.md#std-dtcompatible-ite-it51xxx-vcmp)
  > - [`renesas,ra-acmphs`](../build/dts/api/bindings/comparator/renesas,ra-acmphs.md#std-dtcompatible-renesas-ra-acmphs)
  > - [`renesas,ra-acmphs-global`](../build/dts/api/bindings/comparator/renesas,ra-acmphs-global.md#std-dtcompatible-renesas-ra-acmphs-global)
- Counter

  > - [`adi,max32-wut`](../build/dts/api/bindings/counter/adi,max32-wut.md#std-dtcompatible-adi-max32-wut)
  > - [`espressif,esp32-counter`](../build/dts/api/bindings/counter/espressif,esp32-counter.md#std-dtcompatible-espressif-esp32-counter)
  > - [`ite,it51xxx-counter`](../build/dts/api/bindings/counter/ite,it51xxx-counter.md#std-dtcompatible-ite-it51xxx-counter)
  > - [`ite,it8xxx2-counter`](../build/dts/api/bindings/counter/ite,it8xxx2-counter.md#std-dtcompatible-ite-it8xxx2-counter)
  > - [`neorv32,gptmr`](../build/dts/api/bindings/counter/neorv32,gptmr.md#std-dtcompatible-neorv32-gptmr)
  > - [`realtek,rts5912-timer`](../build/dts/api/bindings/counter/realtek,rts5912-timer.md#std-dtcompatible-realtek-rts5912-timer)
  > - [`ti,cc23x0-lgpt`](../build/dts/api/bindings/counter/ti,cc23x0-lgpt.md#std-dtcompatible-ti-cc23x0-lgpt)
  > - [`ti,cc23x0-rtc`](../build/dts/api/bindings/counter/ti,cc23x0-rtc.md#std-dtcompatible-ti-cc23x0-rtc)
  > - [`ti,mspm0-timer-counter`](../build/dts/api/bindings/counter/ti,mspm0-counter.md#std-dtcompatible-ti-mspm0-timer-counter)
  > - [`wch,gptm`](../build/dts/api/bindings/counter/wch,gptm.md#std-dtcompatible-wch-gptm)
  > - [`zephyr,native-sim-counter`](../build/dts/api/bindings/counter/zephyr,native-sim-counter.md#std-dtcompatible-zephyr-native-sim-counter)
- CPU

  > - [`arm,cortex-r8`](../build/dts/api/bindings/cpu/arm,cortex-r8.md#std-dtcompatible-arm-cortex-r8)
  > - [`intel,bartlett-lake`](../build/dts/api/bindings/cpu/intel,bartlett-lake.md#std-dtcompatible-intel-bartlett-lake)
  > - [`openhwgroup,cva6`](../build/dts/api/bindings/cpu/openhwgroup,cva6.md#std-dtcompatible-openhwgroup-cva6)
  > - [`renesas,rx`](../build/dts/api/bindings/cpu/renesas,rx.md#std-dtcompatible-renesas-rx)
  > - [`wch,qingke-v4b`](../build/dts/api/bindings/cpu/wch,qingke-v4b.md#std-dtcompatible-wch-qingke-v4b)
  > - [`wch,qingke-v4c`](../build/dts/api/bindings/cpu/wch,qingke-v4c.md#std-dtcompatible-wch-qingke-v4c)
  > - [`wch,qingke-v4f`](../build/dts/api/bindings/cpu/wch,qingke-v4f.md#std-dtcompatible-wch-qingke-v4f)
  > - [`zephyr,native-sim-cpu`](../build/dts/api/bindings/cpu/zephyr,native-sim-cpu.md#std-dtcompatible-zephyr-native-sim-cpu)
- Cryptographic accelerator

  > - [`ite,it51xxx-sha`](../build/dts/api/bindings/crypto/ite,it51xxx-sha.md#std-dtcompatible-ite-it51xxx-sha)
  > - [`realtek,rts5912-sha`](../build/dts/api/bindings/crypto/realtek,rts5912-sha.md#std-dtcompatible-realtek-rts5912-sha)
  > - [`ti,cc23x0-aes`](../build/dts/api/bindings/crypto/ti,cc23x0-aes.md#std-dtcompatible-ti-cc23x0-aes)
- DAC

  > - [`nxp,dac12`](../build/dts/api/bindings/dac/nxp,dac12.md#std-dtcompatible-nxp-dac12)
  > - [`ti,dac161s997`](../build/dts/api/bindings/dac/ti,dac161s997.md#std-dtcompatible-ti-dac161s997)
- Debug

  > - [`silabs,pti`](../build/dts/api/bindings/debug/silabs,pti.md#std-dtcompatible-silabs-pti)
- Display

  > - [`sinowealth,sh1122`](../build/dts/api/compatibles/sinowealth,sh1122.md#std-dtcompatible-sinowealth-sh1122)
  > - [`sitronix,st75256`](../build/dts/api/bindings/display/sitronix,st75256.md#std-dtcompatible-sitronix-st75256)
  > - [`sitronix,st7567`](../build/dts/api/compatibles/sitronix,st7567.md#std-dtcompatible-sitronix-st7567)
  > - [`sitronix,st7701`](../build/dts/api/bindings/display/sitronix,st7701.md#std-dtcompatible-sitronix-st7701)
  > - [`solomon,ssd1320`](../build/dts/api/compatibles/solomon,ssd1320.md#std-dtcompatible-solomon-ssd1320)
  > - [`solomon,ssd1327fb`](../build/dts/api/compatibles/solomon,ssd1327fb.md#std-dtcompatible-solomon-ssd1327fb)
  > - [`solomon,ssd1331`](../build/dts/api/bindings/display/solomon,ssd1331.md#std-dtcompatible-solomon-ssd1331)
  > - [`solomon,ssd1351`](../build/dts/api/bindings/display/solomon,ssd1351.md#std-dtcompatible-solomon-ssd1351)
  > - [`solomon,ssd1363`](../build/dts/api/compatibles/solomon,ssd1363.md#std-dtcompatible-solomon-ssd1363)
  > - [`zephyr,displays`](../build/dts/api/bindings/display/zephyr,displays.md#std-dtcompatible-zephyr-displays)
- DMA

  > - [`renesas,rz-dma`](../build/dts/api/bindings/dma/renesas,rz-dma.md#std-dtcompatible-renesas-rz-dma)
  > - [`ti,cc23x0-dma`](../build/dts/api/bindings/dma/ti,cc23x0-dma.md#std-dtcompatible-ti-cc23x0-dma)
  > - [`wch,wch-dma`](../build/dts/api/bindings/dma/wch,wch-dma.md#std-dtcompatible-wch-wch-dma)
- EDAC

  > - [`xlnx,zynqmp-ddrc-2.40a`](../build/dts/api/bindings/edac/xlnx,zynqmp-ddrc-2.40a.md#std-dtcompatible-xlnx-zynqmp-ddrc-2.40a)
- eSPI

  > - [`realtek,rts5912-espi`](../build/dts/api/bindings/espi/realtek,rts5912-espi.md#std-dtcompatible-realtek-rts5912-espi)
- Ethernet

  > - [`ethernet-phy`](../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy)
  > - [`microchip,vsc8541`](../build/dts/api/bindings/ethernet/phy/microchip,vsc8541-phy.md#std-dtcompatible-microchip-vsc8541)
  > - [`nxp,netc-ptp-clock`](../build/dts/api/bindings/ethernet/nxp,netc-ptp-clock.md#std-dtcompatible-nxp-netc-ptp-clock)
  > - [`nxp,tja11xx`](../build/dts/api/bindings/ethernet/nxp,tja11xx.md#std-dtcompatible-nxp-tja11xx)
  > - [`st,stm32-ethernet-controller`](../build/dts/api/bindings/ethernet/st,stm32-ethernet-controller.md#std-dtcompatible-st-stm32-ethernet-controller) has been introduced to ease interoperability
  >   with [`st,stm32-mdio`](../build/dts/api/bindings/mdio/st,stm32-mdio.md#std-dtcompatible-st-stm32-mdio).
  > - [`st,stm32n6-ethernet`](../build/dts/api/bindings/ethernet/st,stm32n6-ethernet.md#std-dtcompatible-st-stm32n6-ethernet)
  > - [`ti,dp83867`](../build/dts/api/bindings/ethernet/phy/ti,dp83867.md#std-dtcompatible-ti-dp83867)
  > - [`xlnx,axi-ethernet-1.00.a`](../build/dts/api/bindings/ethernet/xlnx,axi-ethernet-1.00.a.md#std-dtcompatible-xlnx-axi-ethernet-1.00.a)
- Firmware

  > - [`nxp,scmi-cpu`](../build/dts/api/bindings/firmware/nxp,scmi-cpu.md#std-dtcompatible-nxp-scmi-cpu)
  > - [`ti,k2g-sci`](../build/dts/api/bindings/firmware/ti,k2g-sci.md#std-dtcompatible-ti-k2g-sci)
- Flash controller

  > - [`realtek,rts5912-flash-controller`](../build/dts/api/bindings/flash_controller/realtek,rts5912-flash-controller.md#std-dtcompatible-realtek-rts5912-flash-controller)
  > - [`renesas,ra-ospi-b-nor`](../build/dts/api/bindings/flash_controller/renesas,ra-ospi-b-nor.md#std-dtcompatible-renesas-ra-ospi-b-nor)
  > - [`renesas,rx-flash`](../build/dts/api/bindings/flash_controller/renesas,rx-flash.md#std-dtcompatible-renesas-rx-flash)
  > - [`silabs,series2-flash-controller`](../build/dts/api/bindings/flash_controller/silabs,series2-flash-controller.md#std-dtcompatible-silabs-series2-flash-controller)
  > - [`st,stm32u3-flash-controller`](../build/dts/api/bindings/flash_controller/st,stm32u3-flash-controller.md#std-dtcompatible-st-stm32u3-flash-controller)
- File system

  > - [`zephyr,fstab,fatfs`](../build/dts/api/bindings/fs/zephyr,fstab,fatfs.md#std-dtcompatible-zephyr-fstab-fatfs)
- Fuel gauge

  > - [`onnn,lc709203f`](../build/dts/api/bindings/fuel-gauge/onnn,lc709203f.md#std-dtcompatible-onnn-lc709203f)
  > - [`x-powers,axp2101-fuel-gauge`](../build/dts/api/bindings/fuel-gauge/x-powers,axp2101-fuel-gauge.md#std-dtcompatible-x-powers-axp2101-fuel-gauge)
- GNSS

  > - [`u-blox,f9p`](../build/dts/api/bindings/gnss/u-blox,f9p.md#std-dtcompatible-u-blox-f9p)
- GPIO

  > - [`adi,max14915-gpio`](../build/dts/api/bindings/gpio/adi,max14915-gpio.md#std-dtcompatible-adi-max14915-gpio)
  > - [`adi,max14917-gpio`](../build/dts/api/bindings/gpio/adi,max14917-gpio.md#std-dtcompatible-adi-max14917-gpio)
  > - [`adi,max22199-gpio`](../build/dts/api/bindings/gpio/adi,max22199-gpio.md#std-dtcompatible-adi-max22199-gpio)
  > - [`arducam,dvp-20pin-connector`](../build/dts/api/bindings/gpio/arducam,dvp-20pin-connector.md#std-dtcompatible-arducam-dvp-20pin-connector)
  > - [`bflb,gpio`](../build/dts/api/bindings/gpio/bflb,gpio.md#std-dtcompatible-bflb-gpio)
  > - [`ene,kb106x-gpio`](../build/dts/api/bindings/gpio/ene,kb106x-gpio.md#std-dtcompatible-ene-kb106x-gpio)
  > - [`espressif,esp32-lpgpio`](../build/dts/api/bindings/gpio/espressif,esp32-lpgpio.md#std-dtcompatible-espressif-esp32-lpgpio)
  > - [`ite,it51xxx-gpio`](../build/dts/api/bindings/gpio/ite,it51xxx-gpio.md#std-dtcompatible-ite-it51xxx-gpio)
  > - [`nordic,npm1304-gpio`](../build/dts/api/bindings/gpio/nordic,npm1304-gpio.md#std-dtcompatible-nordic-npm1304-gpio)
  > - [`nxp,lcd-pmod`](../build/dts/api/bindings/gpio/nxp,lcd-pmod.md#std-dtcompatible-nxp-lcd-pmod)
  > - [`raspberrypi,csi-connector`](../build/dts/api/bindings/gpio/raspberrypi,csi-connector.md#std-dtcompatible-raspberrypi-csi-connector)
  > - [`raspberrypi,pico-gpio-port`](../build/dts/api/bindings/gpio/raspberrypi,pico-gpio-port.md#std-dtcompatible-raspberrypi-pico-gpio-port)
  > - [`renesas,ra-parallel-graphics-header`](../build/dts/api/bindings/gpio/renesas,ra-parallel-graphics-header.md#std-dtcompatible-renesas-ra-parallel-graphics-header)
  > - [`renesas,rx-gpio`](../build/dts/api/bindings/gpio/renesas,rx-gpio.md#std-dtcompatible-renesas-rx-gpio)
  > - [`renesas,rza2m-gpio`](../build/dts/api/bindings/gpio/renesas,rza2m-gpio.md#std-dtcompatible-renesas-rza2m-gpio)
  > - [`renesas,rza2m-gpio-int`](../build/dts/api/bindings/gpio/renesas,rza2m-gpio-int.md#std-dtcompatible-renesas-rza2m-gpio-int)
  > - [`st,stm32mp2-gpio`](../build/dts/api/bindings/gpio/st,stm32mp2-gpio.md#std-dtcompatible-st-stm32mp2-gpio)
  > - [`ti,mspm0-gpio`](../build/dts/api/bindings/gpio/ti,mspm0-gpio.md#std-dtcompatible-ti-mspm0-gpio)
- IEEE 802.15.4 HDLC RCP interface

  > - [`spi,hdlc-rcp-if`](../build/dts/api/bindings/hdlc_rcp_if/spi,hdlc-rcp-if.md#std-dtcompatible-spi-hdlc-rcp-if)
- I2C

  > - [`cdns,i2c`](../build/dts/api/bindings/i2c/cdns,i2c.md#std-dtcompatible-cdns-i2c)
  > - [`ite,it51xxx-i2c`](../build/dts/api/bindings/i2c/ite,it51xxx-i2c.md#std-dtcompatible-ite-it51xxx-i2c)
  > - [`litex,litei2c`](../build/dts/api/bindings/i2c/litex,litei2c.md#std-dtcompatible-litex-litei2c)
  > - [`realtek,rts5912-i2c`](../build/dts/api/bindings/i2c/realtek,rts5912-i2c.md#std-dtcompatible-realtek-rts5912-i2c)
  > - [`renesas,ra-i2c-sci-b`](../build/dts/api/bindings/i2c/renesas,ra-i2c-sci-b.md#std-dtcompatible-renesas-ra-i2c-sci-b)
  > - [`renesas,rx-i2c`](../build/dts/api/bindings/i2c/renesas,rx-i2c.md#std-dtcompatible-renesas-rx-i2c)
  > - [`renesas,rz-riic`](../build/dts/api/bindings/i2c/renesas,rz-riic.md#std-dtcompatible-renesas-rz-riic)
  > - [`sensry,sy1xx-i2c`](../build/dts/api/bindings/i2c/sensry,sy1xxx-i2c.md#std-dtcompatible-sensry-sy1xx-i2c)
  > - [`wch,i2c`](../build/dts/api/bindings/i2c/wch,i2c.md#std-dtcompatible-wch-i2c)
- I2S

  > - [`ambiq,i2s`](../build/dts/api/bindings/i2s/ambiq,i2s.md#std-dtcompatible-ambiq-i2s)
  > - [`nordic,nrf-tdm`](../build/dts/api/bindings/i2s/nordic,nrf-tdm.md#std-dtcompatible-nordic-nrf-tdm)
  > - [`renesas,ra-i2s-ssie`](../build/dts/api/bindings/i2s/renesas,ra-i2s-ssie.md#std-dtcompatible-renesas-ra-i2s-ssie)
  > - [`silabs,siwx91x-i2s`](../build/dts/api/bindings/i2s/silabs,siwx91x-i2s.md#std-dtcompatible-silabs-siwx91x-i2s)
  > - [`st,stm32-sai`](../build/dts/api/bindings/i2s/st,stm32-sai.md#std-dtcompatible-st-stm32-sai)
- I3C

  > - [`ite,it51xxx-i3cm`](../build/dts/api/bindings/i3c/ite,it51xxx-i3cm.md#std-dtcompatible-ite-it51xxx-i3cm)
  > - [`ite,it51xxx-i3cs`](../build/dts/api/bindings/i3c/ite,it51xxx-i3cs.md#std-dtcompatible-ite-it51xxx-i3cs)
  > - [`renesas,ra-i3c`](../build/dts/api/bindings/i3c/renesas,ra-i3c.md#std-dtcompatible-renesas-ra-i3c)
- IEEE 802.15.4

  > - [`espressif,esp32-ieee802154`](../build/dts/api/bindings/ieee802154/espressif,esp32-ieee802154.md#std-dtcompatible-espressif-esp32-ieee802154)
- Input

  > - [`arduino,modulino-buttons`](../build/dts/api/bindings/input/arduino,modulino-buttons.md#std-dtcompatible-arduino-modulino-buttons)
  > - [`ite,it51xxx-kbd`](../build/dts/api/bindings/input/ite,it51xxx-kbd.md#std-dtcompatible-ite-it51xxx-kbd)
  > - [`realtek,rts5912-kbd`](../build/dts/api/bindings/input/realtek,rts5912-kbd.md#std-dtcompatible-realtek-rts5912-kbd)
  > - [`st,stm32-tsc`](../build/dts/api/bindings/input/st,stm32-tsc.md#std-dtcompatible-st-stm32-tsc)
  > - [`tsc-keys`](../build/dts/api/bindings/input/tsc-keys.md#std-dtcompatible-tsc-keys)
  > - [`vishay,vs1838b`](../build/dts/api/bindings/input/vishay,vs1838b.md#std-dtcompatible-vishay-vs1838b)
- Interrupt controller

  > - [`ite,it51xxx-intc`](../build/dts/api/bindings/interrupt-controller/ite,it51xxx-intc.md#std-dtcompatible-ite-it51xxx-intc)
  > - [`ite,it51xxx-wuc`](../build/dts/api/bindings/interrupt-controller/ite,it51xxx-wuc.md#std-dtcompatible-ite-it51xxx-wuc)
  > - [`ite,it51xxx-wuc-map`](../build/dts/api/bindings/interrupt-controller/ite,it51xxx-wuc-map.md#std-dtcompatible-ite-it51xxx-wuc-map)
  > - [`renesas,rx-icu`](../build/dts/api/bindings/interrupt-controller/renesas,rx-icu.md#std-dtcompatible-renesas-rx-icu)
  > - [`riscv,clic`](../build/dts/api/bindings/interrupt-controller/riscv,clic.md#std-dtcompatible-riscv-clic)
  > - [`wch,exti`](../build/dts/api/bindings/interrupt-controller/wch,exti.md#std-dtcompatible-wch-exti)
- LED

  > - [`arduino,modulino-buttons-leds`](../build/dts/api/bindings/led/arduino,modulino-buttons-leds.md#std-dtcompatible-arduino-modulino-buttons-leds)
  > - [`dac-leds`](../build/dts/api/bindings/led/dac-leds.md#std-dtcompatible-dac-leds)
  > - [`nordic,npm1304-led`](../build/dts/api/bindings/led/nordic,npm1304-led.md#std-dtcompatible-nordic-npm1304-led)
  > - [`x-powers,axp192-led`](../build/dts/api/bindings/led/x-powers,axp192-led.md#std-dtcompatible-x-powers-axp192-led)
  > - [`x-powers,axp2101-led`](../build/dts/api/bindings/led/x-powers,axp2101-led.md#std-dtcompatible-x-powers-axp2101-led)
- LED strip

  > - [`arduino,modulino-smartleds`](../build/dts/api/bindings/led_strip/arduino,modulino-smartleds.md#std-dtcompatible-arduino-modulino-smartleds)
- Mailbox

  > - [`arm,mhuv3`](../build/dts/api/bindings/mbox/arm,mhuv3.md#std-dtcompatible-arm-mhuv3)
  > - [`renesas,rz-mhu-mbox`](../build/dts/api/bindings/mbox/renesas,rz-mhu-mbox.md#std-dtcompatible-renesas-rz-mhu-mbox)
  > - [`ti,secure-proxy`](../build/dts/api/bindings/mbox/ti,secure-proxy.md#std-dtcompatible-ti-secure-proxy)
- MDIO

  > - [`xlnx,axi-ethernet-1.00.a-mdio`](../build/dts/api/bindings/mdio/xilinx,axi-ethernet-1.00.a-mdio.md#std-dtcompatible-xlnx-axi-ethernet-1.00.a-mdio)
- Memory controller

  > - [`adi,max32-hpb`](../build/dts/api/bindings/memory-controllers/adi,max32-hpb.md#std-dtcompatible-adi-max32-hpb)
  > - [`realtek,rts5912-bbram`](../build/dts/api/bindings/memory-controllers/realtek,rts5912-bbram.md#std-dtcompatible-realtek-rts5912-bbram)
  > - [`silabs,siwx91x-qspi-memory`](../build/dts/api/bindings/memory-controllers/silabs,siwx91x-qspi-memory.md#std-dtcompatible-silabs-siwx91x-qspi-memory)
  > - [`st,stm32-xspi-psram`](../build/dts/api/bindings/memory-controllers/st,stm32-xspi-psram.md#std-dtcompatible-st-stm32-xspi-psram)
- MFD

  > - [`adi,maxq10xx`](../build/dts/api/bindings/mfd/adi,maxq10xx.md#std-dtcompatible-adi-maxq10xx)
  > - [`ambiq,iom`](../build/dts/api/bindings/mfd/ambiq,iom.md#std-dtcompatible-ambiq-iom)
  > - [`microchip,sam-flexcom`](../build/dts/api/bindings/mfd/microchip,sam-flexcom.md#std-dtcompatible-microchip-sam-flexcom)
  > - [`nordic,npm1304`](../build/dts/api/bindings/mfd/nordic,npm1304.md#std-dtcompatible-nordic-npm1304)
  > - [`x-powers,axp2101`](../build/dts/api/bindings/mfd/x-powers,axp2101.md#std-dtcompatible-x-powers-axp2101)
- MIPI DBI

  > - [`nxp,mipi-dbi-dcnano-lcdif`](../build/dts/api/bindings/mipi-dbi/nxp,mipi-dbi-dcnano-lcdif.md#std-dtcompatible-nxp-mipi-dbi-dcnano-lcdif)
- Miscellaneous

  > - [`ene,kb106x-gcfg`](../build/dts/api/bindings/misc/ene,kb106x-gcfg.md#std-dtcompatible-ene-kb106x-gcfg)
  > - [`nordic,ironside-call`](../build/dts/api/bindings/misc/nordic,ironside-call.md#std-dtcompatible-nordic-ironside-call)
  > - [`nordic,nrf-mpc`](../build/dts/api/bindings/misc/nordic,nrf-mpc.md#std-dtcompatible-nordic-nrf-mpc)
  > - [`nxp,rtxxx-dsp-ctrl`](../build/dts/api/bindings/misc/nxp,rtxxx-dsp-ctrl.md#std-dtcompatible-nxp-rtxxx-dsp-ctrl)
  > - [`renesas,ra-elc`](../build/dts/api/bindings/misc/renesas,ra-elc.md#std-dtcompatible-renesas-ra-elc)
  > - [`renesas,ra-ulpt`](../build/dts/api/bindings/misc/renesas,ra-ulpt.md#std-dtcompatible-renesas-ra-ulpt)
  > - [`renesas,rx-external-interrupt`](../build/dts/api/bindings/misc/renesas,rx-external-interrupt.md#std-dtcompatible-renesas-rx-external-interrupt)
  > - [`renesas,rx-mtu`](../build/dts/api/bindings/misc/renesas,rx-mtu.md#std-dtcompatible-renesas-rx-mtu)
  > - [`renesas,rx-sci`](../build/dts/api/bindings/misc/renesas,rx-sci.md#std-dtcompatible-renesas-rx-sci)
  > - [`renesas,rz-sci`](../build/dts/api/bindings/misc/renesas,rz-sci.md#std-dtcompatible-renesas-rz-sci)
  > - [`renesas,rz-sci-b`](../build/dts/api/bindings/misc/renesas,rz-sci-b.md#std-dtcompatible-renesas-rz-sci-b)
  > - [`st,stm32n6-ramcfg`](../build/dts/api/bindings/misc/st,stm32n6-ramcfg.md#std-dtcompatible-st-stm32n6-ramcfg)
- Modem

  > - [`quectel,eg800q`](../build/dts/api/bindings/modem/quectel,eg800q.md#std-dtcompatible-quectel-eg800q)
  > - [`simcom,a76xx`](../build/dts/api/bindings/modem/simcom,a76xx.md#std-dtcompatible-simcom-a76xx)
- Multi-bit SPI

  > - [`nordic,nrf-exmif`](../build/dts/api/bindings/mspi/nordic,nrf-exmif.md#std-dtcompatible-nordic-nrf-exmif)
  > - [`snps,designware-ssi`](../build/dts/api/bindings/mspi/snps,designware-ssi.md#std-dtcompatible-snps-designware-ssi)
- MTD

  > - [`fixed-subpartitions`](../build/dts/api/bindings/mtd/fixed-subpartitions.md#std-dtcompatible-fixed-subpartitions)
  > - [`jedec,mspi-nor`](../build/dts/api/bindings/mtd/jedec,mspi-nor.md#std-dtcompatible-jedec-mspi-nor)
  > - [`mspi-aps-z8`](../build/dts/api/bindings/mtd/mspi-aps-z8.md#std-dtcompatible-mspi-aps-z8)
  > - [`mspi-is25xX0xx`](../build/dts/api/bindings/mtd/mspi-is25xX0xx.md#std-dtcompatible-mspi-is25xX0xx)
  > - [`renesas,ra-nv-code-flash`](../build/dts/api/bindings/mtd/renesas,ra-nv-code-flash.md#std-dtcompatible-renesas-ra-nv-code-flash)
  > - [`renesas,ra-nv-data-flash`](../build/dts/api/bindings/mtd/renesas,ra-nv-data-flash.md#std-dtcompatible-renesas-ra-nv-data-flash)
  > - [`renesas,rx-nv-flash`](../build/dts/api/bindings/mtd/renesas,rx-nv-flash.md#std-dtcompatible-renesas-rx-nv-flash)
  > - [`ti,tmp11x-eeprom`](../build/dts/api/bindings/mtd/ti,tmp11x-eeprom.md#std-dtcompatible-ti-tmp11x-eeprom)
- Networking

  > - [`nordic,nrf-nfct-v2`](../build/dts/api/bindings/net/wireless/nordic,nrf-nfct-v2.md#std-dtcompatible-nordic-nrf-nfct-v2)
  > - [`silabs,siwx91x-nwp`](../build/dts/api/bindings/net/wireless/silabs,siwx91x-nwp.md#std-dtcompatible-silabs-siwx91x-nwp)
- Octal SPI

  > - [`renesas,ra-ospi-b`](../build/dts/api/bindings/ospi/renesas,ra-ospi-b.md#std-dtcompatible-renesas-ra-ospi-b)
- Pin control

  > - [`ambiq,apollo5-pinctrl`](../build/dts/api/bindings/pinctrl/ambiq,apollo5-pinctrl.md#std-dtcompatible-ambiq-apollo5-pinctrl)
  > - [`arm,mps2-pinctrl`](../build/dts/api/bindings/pinctrl/arm,mps2-pinctrl.md#std-dtcompatible-arm-mps2-pinctrl)
  > - [`arm,mps3-pinctrl`](../build/dts/api/bindings/pinctrl/arm,mps3-pinctrl.md#std-dtcompatible-arm-mps3-pinctrl)
  > - [`arm,mps4-pinctrl`](../build/dts/api/bindings/pinctrl/arm,mps4-pinctrl.md#std-dtcompatible-arm-mps4-pinctrl)
  > - [`arm,v2m_beetle-pinctrl`](../build/dts/api/bindings/pinctrl/arm,v2m_beetle-pinctrl.md#std-dtcompatible-arm-v2m_beetle-pinctrl)
  > - [`bflb,pinctrl`](../build/dts/api/bindings/pinctrl/bflb,pinctrl.md#std-dtcompatible-bflb-pinctrl)
  > - [`ene,kb106x-pinctrl`](../build/dts/api/bindings/pinctrl/ene,kb106x-pinctrl.md#std-dtcompatible-ene-kb106x-pinctrl)
  > - [`microchip,sama7g5-pinctrl`](../build/dts/api/bindings/pinctrl/microchip,sama7g5-pinctrl.md#std-dtcompatible-microchip-sama7g5-pinctrl)
  > - [`nuvoton,npcx-pinctrl-npckn`](../build/dts/api/bindings/pinctrl/nuvoton,npcx-pinctrl-npckn.md#std-dtcompatible-nuvoton-npcx-pinctrl-npckn)
  > - [`renesas,rx-pinctrl`](../build/dts/api/bindings/pinctrl/renesas,rx-pinctrl.md#std-dtcompatible-renesas-rx-pinctrl)
  > - [`renesas,rx-pinmux`](../build/dts/api/bindings/pinctrl/renesas,rx-pinmux.md#std-dtcompatible-renesas-rx-pinmux)
  > - [`renesas,rza-pinctrl`](../build/dts/api/bindings/pinctrl/renesas,rza-pinctrl.md#std-dtcompatible-renesas-rza-pinctrl)
  > - [`renesas,rza2m-pinctrl`](../build/dts/api/bindings/pinctrl/renesas,rza2m-pinctrl.md#std-dtcompatible-renesas-rza2m-pinctrl)
  > - [`renesas,rzn-pinctrl`](../build/dts/api/bindings/pinctrl/renesas,rzn-pinctrl.md#std-dtcompatible-renesas-rzn-pinctrl)
  > - [`renesas,rzt-pinctrl`](../build/dts/api/bindings/pinctrl/renesas,rzt-pinctrl.md#std-dtcompatible-renesas-rzt-pinctrl)
  > - [`renesas,rzv-pinctrl`](../build/dts/api/bindings/pinctrl/renesas,rzv-pinctrl.md#std-dtcompatible-renesas-rzv-pinctrl)
  > - [`st,stm32n6-pinctrl`](../build/dts/api/bindings/pinctrl/st,stm32n6-pinctrl.md#std-dtcompatible-st-stm32n6-pinctrl)
  > - [`ti,mspm0-pinctrl`](../build/dts/api/bindings/pinctrl/ti,mspm0-pinctrl.md#std-dtcompatible-ti-mspm0-pinctrl)
  > - [`wch,00x-afio`](../build/dts/api/bindings/pinctrl/wch,00x-afio.md#std-dtcompatible-wch-00x-afio)
  > - [`wch,20x_30x-afio`](../build/dts/api/bindings/pinctrl/wch,20x_30x-afio.md#std-dtcompatible-wch-20x_30x-afio)
- Power management

  > - [`infineon,cat1b-power`](../build/dts/api/bindings/power/infineon,cat1b-power.md#std-dtcompatible-infineon-cat1b-power)
  > - [`realtek,rts5912-ulpm`](../build/dts/api/bindings/power/realtek,rts5912-ulpm.md#std-dtcompatible-realtek-rts5912-ulpm)
- Power domain

  > - [`ti,sci-pm-domain`](../build/dts/api/bindings/power-domain/ti,sci-pm-domain.md#std-dtcompatible-ti-sci-pm-domain)
- PSI5

  > - [`nxp,s32-psi5`](../build/dts/api/bindings/psi5/nxp,s32-psi5.md#std-dtcompatible-nxp-s32-psi5)
- PWM

  > - [`arduino-header-pwm`](../build/dts/api/bindings/pwm/arduino-header-pwm.md#std-dtcompatible-arduino-header-pwm)
  > - [`ene,kb106x-pwm`](../build/dts/api/bindings/pwm/ene,kb106x-pwm.md#std-dtcompatible-ene-kb106x-pwm)
  > - [`ite,it51xxx-pwm`](../build/dts/api/bindings/pwm/ite,it51xxx-pwm.md#std-dtcompatible-ite-it51xxx-pwm)
  > - [`neorv32,pwm`](../build/dts/api/bindings/pwm/neorv32,pwm.md#std-dtcompatible-neorv32-pwm)
  > - [`realtek,rts5912-pwm`](../build/dts/api/bindings/pwm/realtek,rts5912-pwm.md#std-dtcompatible-realtek-rts5912-pwm)
  > - [`renesas,rx-mtu-pwm`](../build/dts/api/bindings/pwm/renesas,rx-mtu-pwm.md#std-dtcompatible-renesas-rx-mtu-pwm)
  > - [`silabs,letimer-pwm`](../build/dts/api/bindings/pwm/silabs,letimer-pwm.md#std-dtcompatible-silabs-letimer-pwm)
  > - [`silabs,siwx91x-pwm`](../build/dts/api/bindings/pwm/silabs,siwx91x-pwm.md#std-dtcompatible-silabs-siwx91x-pwm)
  > - [`silabs,timer-pwm`](../build/dts/api/bindings/pwm/silabs,timer-pwm.md#std-dtcompatible-silabs-timer-pwm)
  > - [`ti,mspm0-timer-pwm`](../build/dts/api/bindings/pwm/ti,mspm0-pwm.md#std-dtcompatible-ti-mspm0-timer-pwm)
  > - [`wch,gptm-pwm`](../build/dts/api/bindings/pwm/wch,gptm-pwm.md#std-dtcompatible-wch-gptm-pwm)
- Regulator

  > - [`nordic,npm1304-regulator`](../build/dts/api/bindings/regulator/nordic,npm1304-regulator.md#std-dtcompatible-nordic-npm1304-regulator)
  > - [`x-powers,axp2101-regulator`](../build/dts/api/bindings/regulator/x-powers,axp2101-regulator.md#std-dtcompatible-x-powers-axp2101-regulator)
- Reset controller

  > - [`microchip,mpfs-reset`](../build/dts/api/bindings/reset/microchip,mpfs-reset.md#std-dtcompatible-microchip-mpfs-reset)
  > - [`reset-mmio`](../build/dts/api/bindings/reset/reset-mmio.md#std-dtcompatible-reset-mmio)
- RNG

  > - [`adi,maxq10xx-trng`](../build/dts/api/bindings/rng/adi,maxq10xx-trng.md#std-dtcompatible-adi-maxq10xx-trng)
  > - [`brcm,iproc-rng200`](../build/dts/api/bindings/rng/brcm,iproc-rng200.md#std-dtcompatible-brcm-iproc-rng200)
  > - [`virtio,device4`](../build/dts/api/bindings/rng/virtio,device4.md#std-dtcompatible-virtio-device4)
  > - [`zephyr,native-sim-rng`](../build/dts/api/bindings/rng/zephyr,native-sim-rng.md#std-dtcompatible-zephyr-native-sim-rng)
- RTC

  > - [`nxp,pcf2123`](../build/dts/api/bindings/rtc/nxp,pcf2123.md#std-dtcompatible-nxp-pcf2123)
  > - [`realtek,rts5912-rtc`](../build/dts/api/bindings/rtc/realtek,rts5912-rtc.md#std-dtcompatible-realtek-rts5912-rtc)
  > - [`silabs,siwx91x-rtc`](../build/dts/api/bindings/rtc/silabs,siwx91x-rtc.md#std-dtcompatible-silabs-siwx91x-rtc)
- SDHC

  > - [`ambiq,sdio`](../build/dts/api/bindings/sdhc/ambiq,sdhc.md#std-dtcompatible-ambiq-sdio)
  > - [`xlnx,versal-8.9a`](../build/dts/api/bindings/sdhc/xlnx,sdhc.md#std-dtcompatible-xlnx-versal-8.9a)
- Sensors

  > - [`adi,ad2s1210`](../build/dts/api/bindings/sensor/adi,ad2s1210.md#std-dtcompatible-adi-ad2s1210)
  > - [`bosch,bmm350`](../build/dts/api/bindings/sensor/bosch,bmm350-i2c.md#std-dtcompatible-bosch-bmm350)
  > - [`brcm,afbr-s50`](../build/dts/api/bindings/sensor/brcm,afbr-s50.md#std-dtcompatible-brcm-afbr-s50)
  > - [`everlight,als-pt19`](../build/dts/api/bindings/sensor/everlight,als-pt19.md#std-dtcompatible-everlight-als-pt19)
  > - [`invensense,icm40627`](../build/dts/api/bindings/sensor/invensense,icm40627-i2c.md#std-dtcompatible-invensense-icm40627)
  > - [`invensense,icm45686`](../build/dts/api/compatibles/invensense,icm45686.md#std-dtcompatible-invensense-icm45686)
  > - [`invensense,icp201xx`](../build/dts/api/compatibles/invensense,icp201xx.md#std-dtcompatible-invensense-icp201xx)
  > - [`liteon,ltr329`](../build/dts/api/bindings/sensor/liteon,ltr329.md#std-dtcompatible-liteon-ltr329)
  > - [`meas,ms5837-02ba`](../build/dts/api/bindings/sensor/meas,ms5837-02ba.md#std-dtcompatible-meas-ms5837-02ba)
  > - [`meas,ms5837-30ba`](../build/dts/api/bindings/sensor/meas,ms5837-30ba.md#std-dtcompatible-meas-ms5837-30ba)
  > - [`nordic,npm1304-charger`](../build/dts/api/bindings/sensor/nordic,npm1304-charger.md#std-dtcompatible-nordic-npm1304-charger)
  > - [`nxp,lpadc-temp40`](../build/dts/api/bindings/sensor/nxp,lpadc-temp40.md#std-dtcompatible-nxp-lpadc-temp40)
  > - [`nxp,tpm-qdec`](../build/dts/api/bindings/sensor/nxp,tpm-qdec.md#std-dtcompatible-nxp-tpm-qdec)
  > - [`peacefair,pzem004t`](../build/dts/api/bindings/sensor/peacefair,pzem004t.md#std-dtcompatible-peacefair-pzem004t)
  > - [`pixart,paa3905`](../build/dts/api/bindings/sensor/pixart,paa3905.md#std-dtcompatible-pixart-paa3905)
  > - [`pixart,paj7620`](../build/dts/api/bindings/sensor/pixart,paj7620.md#std-dtcompatible-pixart-paj7620)
  > - [`pixart,pat9136`](../build/dts/api/bindings/sensor/pixart,pat9136.md#std-dtcompatible-pixart-pat9136)
  > - [`pni,rm3100`](../build/dts/api/bindings/sensor/pni,rm3100.md#std-dtcompatible-pni-rm3100)
  > - [`rohm,bh1730`](../build/dts/api/bindings/sensor/rohm,bh1730.md#std-dtcompatible-rohm-bh1730)
  > - [`rohm,bh1790`](../build/dts/api/bindings/sensor/rohm,bh1790.md#std-dtcompatible-rohm-bh1790)
  > - [`st,lsm6dsv32x`](../build/dts/api/compatibles/st,lsm6dsv32x.md#std-dtcompatible-st-lsm6dsv32x)
  > - [`st,lsm9ds1_mag`](../build/dts/api/bindings/sensor/st,lsm9ds1_mag.md#std-dtcompatible-st-lsm9ds1_mag)
  > - [`ti,tmp11x`](../build/dts/api/bindings/sensor/ti,tmp11x.md#std-dtcompatible-ti-tmp11x)
  > - [`vishay,veml6031`](../build/dts/api/bindings/sensor/vishay,veml6031.md#std-dtcompatible-vishay-veml6031)
  > - [`we,wsen-itds-2533020201601`](../build/dts/api/compatibles/we,wsen-itds-2533020201601.md#std-dtcompatible-we-wsen-itds-2533020201601)
- SENT

  > - [`nxp,s32-sent`](../build/dts/api/bindings/sent/nxp,s32-sent.md#std-dtcompatible-nxp-s32-sent)
- Serial controller

  > - [`aesc,uart`](../build/dts/api/bindings/serial/aesc,uart.md#std-dtcompatible-aesc-uart)
  > - [`ambiq,pl011-uart`](../build/dts/api/bindings/serial/ambiq,pl011-uart.md#std-dtcompatible-ambiq-pl011-uart)
  > - [`bflb,uart`](../build/dts/api/bindings/serial/bflb,uart.md#std-dtcompatible-bflb-uart)
  > - [`ene,kb106x-uart`](../build/dts/api/bindings/serial/ene,kb106x-uart.md#std-dtcompatible-ene-kb106x-uart)
  > - [`espressif,esp32-lpuart`](../build/dts/api/bindings/serial/espressif,esp32-lpuart.md#std-dtcompatible-espressif-esp32-lpuart)
  > - [`ite,it51xxx-uart`](../build/dts/api/bindings/serial/ite,it51xxx-uart.md#std-dtcompatible-ite-it51xxx-uart)
  > - [`nuvoton,npcx-uart-npckn`](../build/dts/api/bindings/serial/nuvoton,npcx-uart-npckn.md#std-dtcompatible-nuvoton-npcx-uart-npckn)
  > - [`renesas,rx-uart-sci`](../build/dts/api/bindings/serial/renesas,rx-uart-sci.md#std-dtcompatible-renesas-rx-uart-sci)
  > - [`renesas,rx-uart-sci-qemu`](../build/dts/api/bindings/serial/renesas,rx-uart-sci-qemu.md#std-dtcompatible-renesas-rx-uart-sci-qemu)
  > - [`renesas,rz-sci-b-uart`](../build/dts/api/bindings/serial/renesas,rz-sci-b-uart.md#std-dtcompatible-renesas-rz-sci-b-uart)
  > - [`renesas,rz-sci-uart`](../build/dts/api/bindings/serial/renesas,rz-sci-uart.md#std-dtcompatible-renesas-rz-sci-uart)
  > - [`renesas,rza2m-scif-uart`](../build/dts/api/bindings/serial/renesas,rza2m-scif-uart.md#std-dtcompatible-renesas-rza2m-scif-uart)
  > - [`ti,mspm0-uart`](../build/dts/api/bindings/serial/ti,mspm0-uart.md#std-dtcompatible-ti-mspm0-uart)
  > - [`zephyr,native-pty-uart`](../build/dts/api/bindings/serial/zephyr,native-pty-uart.md#std-dtcompatible-zephyr-native-pty-uart)
  > - [`zephyr,uart-bridge`](../build/dts/api/bindings/serial/zephyr,uart-bridge.md#std-dtcompatible-zephyr-uart-bridge)
- SPI

  > - [`cdns,spi`](../build/dts/api/bindings/spi/cdns,spi.md#std-dtcompatible-cdns-spi)
  > - [`ite,it51xxx-spi`](../build/dts/api/bindings/spi/ite,it51xxx-spi.md#std-dtcompatible-ite-it51xxx-spi)
  > - [`microchip,mec5-qspi`](../build/dts/api/bindings/spi/microchip,mec5-qspi.md#std-dtcompatible-microchip-mec5-qspi)
  > - [`renesas,rx-rspi`](../build/dts/api/bindings/spi/renesas,rx-rspi.md#std-dtcompatible-renesas-rx-rspi)
  > - [`renesas,rz-rspi`](../build/dts/api/bindings/spi/renesas,rz-rspi.md#std-dtcompatible-renesas-rz-rspi)
  > - [`silabs,gspi`](../build/dts/api/bindings/spi/silabs,gspi.md#std-dtcompatible-silabs-gspi)
  > - [`ti,cc23x0-spi`](../build/dts/api/bindings/spi/ti,cc23x0-spi.md#std-dtcompatible-ti-cc23x0-spi)
  > - [`wch,spi`](../build/dts/api/bindings/spi/wch,spi.md#std-dtcompatible-wch-spi)
- Stepper

  > - [`adi,tmc51xx`](../build/dts/api/compatibles/adi,tmc51xx.md#std-dtcompatible-adi-tmc51xx)
  > - [`allegro,a4979`](../build/dts/api/bindings/stepper/allegro/allegro,a4979.md#std-dtcompatible-allegro-a4979)
- System controller

  > - [`bflb,efuse`](../build/dts/api/bindings/syscon/bflb,efuse.md#std-dtcompatible-bflb-efuse)
- Tachometer

  > - [`ite,it51xxx-tach`](../build/dts/api/bindings/tach/ite,it51xxx-tach.md#std-dtcompatible-ite-it51xxx-tach)
  > - [`realtek,rts5912-tach`](../build/dts/api/bindings/tach/realtek,rts5912-tach.md#std-dtcompatible-realtek-rts5912-tach)
- TCPC

  > - [`onnn,fusb307-tcpc`](../build/dts/api/bindings/tcpc/onnn,fusb307.md#std-dtcompatible-onnn-fusb307-tcpc)
- Timer

  > - [`infineon,cat1-lp-timer`](../build/dts/api/bindings/timer/infineon,cat1-lp-timer.md#std-dtcompatible-infineon-cat1-lp-timer)
  > - [`ite,it51xxx-timer`](../build/dts/api/bindings/timer/ite,it51xxx-timer.md#std-dtcompatible-ite-it51xxx-timer)
  > - [`microchip,sam-pit64b`](../build/dts/api/bindings/timer/microchip,sam-pit64b.md#std-dtcompatible-microchip-sam-pit64b)
  > - [`renesas,ra-ulpt-timer`](../build/dts/api/bindings/timer/renesas,ra-ulpt-timer.md#std-dtcompatible-renesas-ra-ulpt-timer)
  > - [`renesas,rx-timer-cmt`](../build/dts/api/bindings/timer/renesas,rx-timer-cmt.md#std-dtcompatible-renesas-rx-timer-cmt)
  > - [`renesas,rx-timer-cmt-start-control`](../build/dts/api/bindings/timer/renesas,rx-timer-cmt-start-control.md#std-dtcompatible-renesas-rx-timer-cmt-start-control)
  > - [`renesas,rz-gtm-os-timer`](../build/dts/api/bindings/timer/renesas,rz-gtm-os-timer.md#std-dtcompatible-renesas-rz-gtm-os-timer)
  > - [`renesas,rza2m-ostm`](../build/dts/api/bindings/timer/renesas,rza2m-ostm.md#std-dtcompatible-renesas-rza2m-ostm)
  > - [`silabs,series2-letimer`](../build/dts/api/bindings/timer/silabs,series2-letimer.md#std-dtcompatible-silabs-series2-letimer)
  > - [`silabs,series2-timer`](../build/dts/api/bindings/timer/silabs,series2-timer.md#std-dtcompatible-silabs-series2-timer)
  > - [`ti,mspm0-timer`](../build/dts/api/bindings/timer/ti,mspm0-timer.md#std-dtcompatible-ti-mspm0-timer)
- USB

  > - [`adi,max32-usbhs`](../build/dts/api/bindings/usb/adi,max32-usbhs.md#std-dtcompatible-adi-max32-usbhs)
  > - [`nxp,uhc-ehci`](../build/dts/api/bindings/usb/nxp,uhc-ehci.md#std-dtcompatible-nxp-uhc-ehci)
  > - [`nxp,uhc-ip3516hs`](../build/dts/api/bindings/usb/nxp,uhc-ip3516hs.md#std-dtcompatible-nxp-uhc-ip3516hs)
  > - [`nxp,uhc-khci`](../build/dts/api/bindings/usb/nxp,uhc-khci.md#std-dtcompatible-nxp-uhc-khci)
  > - [`nxp,uhc-ohci`](../build/dts/api/bindings/usb/nxp,uhc-ohci.md#std-dtcompatible-nxp-uhc-ohci)
  > - [`st,stm32n6-otghs`](../build/dts/api/bindings/usb/st,stm32n6-otghs.md#std-dtcompatible-st-stm32n6-otghs)
  > - [`zephyr,uvc-device`](../build/dts/api/bindings/usb/zephyr,uvc-device.md#std-dtcompatible-zephyr-uvc-device)
- Video

  > - [`ovti,ov9655`](../build/dts/api/bindings/video/ovti,ov9655.md#std-dtcompatible-ovti-ov9655)
  > - [`sony,imx335`](../build/dts/api/bindings/video/sony,imx335.md#std-dtcompatible-sony-imx335)
  > - [`st,mipid02`](../build/dts/api/bindings/video/st,mipid02.md#std-dtcompatible-st-mipid02)
  > - [`st,stm32-dcmipp`](../build/dts/api/bindings/video/st,stm32-dcmipp.md#std-dtcompatible-st-stm32-dcmipp)
  > - [`zephyr,video-sw-generator`](../build/dts/api/bindings/video/zephyr,video-sw-generator.md#std-dtcompatible-zephyr-video-sw-generator)
- Virtio

  > - [`virtio,mmio`](../build/dts/api/bindings/virtio/virtio,mmio.md#std-dtcompatible-virtio-mmio)
  > - [`virtio,pci`](../build/dts/api/bindings/virtio/virtio,pci.md#std-dtcompatible-virtio-pci)
- Watchdog

  > - [`ene,kb106x-watchdog`](../build/dts/api/bindings/watchdog/ene,kb106x-watchdog.md#std-dtcompatible-ene-kb106x-watchdog)
  > - [`ite,it51xxx-watchdog`](../build/dts/api/bindings/watchdog/ite,it51xxx-watchdog.md#std-dtcompatible-ite-it51xxx-watchdog)
  > - [`nordic,npm1304-wdt`](../build/dts/api/bindings/watchdog/nordic,npm1304-wdt.md#std-dtcompatible-nordic-npm1304-wdt)
  > - [`nxp,ewm`](../build/dts/api/bindings/watchdog/nxp,ewm.md#std-dtcompatible-nxp-ewm)
  > - [`realtek,rts5912-watchdog`](../build/dts/api/bindings/watchdog/realtek,rts5912-watchdog.md#std-dtcompatible-realtek-rts5912-watchdog)
  > - [`renesas,ra-wdt`](../build/dts/api/bindings/watchdog/renesas,ra-wdt.md#std-dtcompatible-renesas-ra-wdt)
  > - [`silabs,siwx91x-wdt`](../build/dts/api/bindings/watchdog/silabs,siwx91x-wdt.md#std-dtcompatible-silabs-siwx91x-wdt)
  > - [`ti,cc23x0-wdt`](../build/dts/api/bindings/watchdog/ti,cc23x0-watchdog.md#std-dtcompatible-ti-cc23x0-wdt)
  > - [`wch,iwdg`](../build/dts/api/bindings/watchdog/wch,iwdg.md#std-dtcompatible-wch-iwdg)
- Wi-Fi

  > - [`espressif,esp-hosted`](../build/dts/api/bindings/wifi/espressif,esp-hosted.md#std-dtcompatible-espressif-esp-hosted)

## New Samples

- [Audio output AMP sample.](../samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/README.md#amp_audio_loopback "AMP system example for NXP i.MX RTxxx platforms - audio loopback.")
- [Audio output AMP sample.](../samples/boards/nxp/adsp/rtxxx/amp_audio_output/README.md#amp_audio_output "AMP system example for NXP i.MX RTxxx platforms - audio output.")
- [Blinky AMP sample](../samples/boards/nxp/adsp/rtxxx/amp_blinky/README.md#amp_blinky "AMP system example for NXP i.MX RTxxx platforms - blinking LED.")
- [mbox API AMP sample](../samples/boards/nxp/adsp/rtxxx/amp_mbox/README.md#amp_mbox "AMP system example for NXP i.MX RTxxx platforms - IPC using the mbox API.")
- [Auxiliary digits display](../samples/drivers/auxdisplay_digits/README.md#auxdisplay_digits "Output increasing numbers to an auxiliary display.")
- [BMG160 3-axis gyroscope](../samples/sensor/bmg160/README.md#bmg160 "Get temperature, and angular velocity data from a BMG160 sensor.")
- [Debug ULP](../samples/boards/espressif/ulp/lp_core/debug_ulp/README.md#debug-ulp "Debug the LP Core in ESP32C6.")
- [Generic distance measurement](../samples/sensor/distance_polling/README.md#distance_polling "Measure distance to an object using a distance sensor")
- [Echo ULP](../samples/boards/espressif/ulp/lp_core/echo_ulp/README.md#echo-ulp "Leverage Zephyr's UART API to use the LP UART on the ESP32-C6's LP core.")
- [Fatfs filesystem fstab](../samples/subsys/fs/fatfs_fstab/README.md#fatfs-fstab "Define fatfs filesystems in the devicetree.")
- [Fuel Gauge](../samples/drivers/fuel_gauge/README.md#fuel_gauge "Use fuel gauge API to access fuel gauge properties and get charge information.")
- [Heart Rate Sensor](../samples/sensor/heart_rate/README.md#heart_rate "Get heart rate data from a sensor (polling mode).")
- [Interrupt ULP](../samples/boards/espressif/ulp/lp_core/interrupt_ulp/README.md#interrupt-ulp "HP Core interrupt LP Core.")
- [Generic Light Sensor Polling](../samples/sensor/light_polling/README.md#light_sensor_polling "Get illuminance data from a light sensor.")
- [LVGL Multi-display](../samples/modules/lvgl/multi_display/README.md#lvgl-multi-display "Run different LVGL demos on multiple displays.")
- [Min-Heap Data Structure](../samples/data_structures/min-heap/README.md#min-heap "Demonstrate usage of a min-heap implementation in a Zephyr application.")
- [Ambiq MSPI timing scan](../samples/drivers/mspi/mspi_timing_scan/README.md#mspi-timing-scan "Find the appropriate timing for a given device on a given board.")
- [Network packet filter](../samples/net/pkt_filter/README.md#net-pkt-filter "Install network packet filter hooks.")
- [Nordic IronSide SE firmware update](../samples/boards/nordic/nrf_ironside/update/README.md#nrf_ironside_update "Update the Nordic IronSide SE firmware.")
- [PAJ7620 Gesture Sensor](../samples/sensor/paj7620_gesture/README.md#paj7620_gesture "Get hand gesture data from PAJ7620 sensor.")
- [Barometric pressure and temperature sensor interrupt example](../samples/sensor/pressure_interrupt/README.md#pressure_interrupt "Manage interrupts from a barometric pressure and temperature sensor.")
- [Barometric pressure and temperature sensor polling example](../samples/sensor/pressure_polling/README.md#pressure_polling "Get barometric pressure and temperature data from a sensor.")
- [PSI5 interface](../samples/drivers/psi5/README.md#psi5 "Use the PSI5 (Peripheral Sensor Interface) driver.")
- [Renesas ELC Sample](../samples/boards/renesas/elc/README.md#renesas-elc "Integrating the Renesas ELC with PWM Functionality")
- [Renesas comparator](../samples/boards/renesas/comparator/README.md#renesas_comparator "Monitor the output of comparator.")
- [OpenAMP Linux Zephyr RPMsg](../samples/boards/renesas/openamp_linux_zephyr/README.md#rz-openamp-linux-zephyr "Enable message exchange between two cores, with the application core running Linux and the real-time core running Zephyr, using the OpenAMP library.")
- [SENT interface](../samples/drivers/sent/README.md#sent "Use the SENT (Single Edge Nibble Transmission) driver.")
- [SPIS wake up](../samples/boards/nordic/spis_wakeup/README.md#spis-wakeup "Reduce current consumption by handling the wake line while using an SPIS.")
- [Stepper](../samples/drivers/stepper/generic/README.md#stepper "Rotate a stepper motor in 4 different modes.")
- [Generic device sample streaming using Data Ready trigger](../samples/sensor/stream_drdy/README.md#stream_drdy "Get accelerometer data frames from a sensor using SENSOR_TRIG_DATA_READY.")
- [UART ASYNC API](../samples/drivers/uart/async_api/README.md#uart_async "Demonstrate the use of the asynchronous API")
- [USB CDC-ACM bridge](../samples/subsys/usb/cdc_acm_bridge/README.md#usb-cdc-acm-bridge "Use USB CDC-ACM driver to implement a serial port bridge.")
- [UUID](../samples/subsys/uuid/README.md#uuid "Manipulate UUID v4 and v5 compliant with IETF RFC 9562.")
- [USB Video webcam](../samples/subsys/usb/uvc/README.md#uvc "Send video frames over USB.")
- [VEML6031 High Accuracy Ambient Light Sensor](../samples/sensor/veml6031/README.md#veml6031 "Get ambient light data from a VEML4040 sensor (polling mode).")

## Other notable changes

- Added support for Armv8.1-M MPU’s PXN (Privileged Execute Never) attribute.
  With this, the MPU attributes for `__ramfunc` and `__ram_text_reloc` were modified such that,
  PXN attribute is set for these regions if compiled with `CONFIG_ARM_MPU_PXN` and `CONFIG_USERSPACE`.
  This results in a change in behavior for code being executed from these regions because,
  if these regions have pxn attribute set in them, they cannot be executed in privileged mode.
- Removed support for Nucleo WBA52CG board (`nucleo_wba52cg`) since it is NRND (Not Recommended
  for New Design) and is no longer supported in the STM32CubeWBA from version 1.1.0 (July 2023).
  The migration to [Nucleo WBA55CG](../boards/st/nucleo_wba55cg/doc/nucleo_wba55cg.md#nucleo_wba55cg) (`nucleo_wba55cg`) is recommended instead.
- Updated Mbed TLS to version 3.6.4 (from 3.6.2). Release notes for 3.6.3 and
  3.6.4 can be found below:

  - 3.6.3: [https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.3](https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.3)
  - 3.6.4: [https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.4](https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.4)
- Updated TF-M to version 2.1.2 (from 2.1.1). The release notes can be found at:
  [https://trustedfirmware-m.readthedocs.io/en/tf-mv2.1.2/releases/2.1.2.html](https://trustedfirmware-m.readthedocs.io/en/tf-mv2.1.2/releases/2.1.2.html)
- Updated all boards with an external I2C connectors (Qwiic, Stemma, Grove…)
  to use the `zephyr_i2c` devicetree label. This allows using the existing
  [Shields](../hardware/porting/shields.md#shields) build system feature (`west build --shield`) to interface
  any connectorized i2c module to any board with a compatible i2c port,
  regardless of the specific i2c connector branding.
- Reverted deprecation of receiver option in Nordic UART driver. Receiver mode which is using
  additional TIMER peripheral to count received bytes was previously deprecated
  (e.g. `CONFIG_CONFIG_UART_0_NRF_HW_ASYNC`). However, it turned out that this
  previously mode is the only one that is capable of reliably receive data without Hardware
  Flow Control so it should stay in the driver.
