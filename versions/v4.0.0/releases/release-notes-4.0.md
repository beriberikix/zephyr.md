---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/releases/release-notes-4.0.html
original_path: releases/release-notes-4.0.html
---

# Zephyr 4.0.0

We are pleased to announce the release of Zephyr version 4.0.0.

Major enhancements with this release include:

- **Secure Storage Subsystem**:
  A newly introduced [secure storage](../services/secure_storage.md#secure-storage) subsystem allows the use of the
  PSA Secure Storage API and of persistent keys in the PSA Crypto API on *all* board targets. It
  is now the standard way to provide device-specific protection to data at rest. ([GitHub #76222](https://github.com/zephyrproject-rtos/zephyr/issues/76222))
- **ZMS (Zephyr Memory Storage) Subsystem**:
  [ZMS](../services/storage/zms/zms.md#zms-api) is a new key-value storage subsystem compatible with all non-volatile storage
  types, including traditional NOR flash and advanced technologies like RRAM and MRAM that support
  write without erasure.
- **Analog Comparators**:
  A new [comparator](../hardware/peripherals/comparator.md#comparator-api) device driver subsystem for analog comparators has been
  added, complete with shell support. It supports initial configuration through Devicetree and
  runtime configuration through vendor specific APIs. Initially the [`nordic,nrf-comp`](../build/dts/api/bindings/comparator/nordic%2Cnrf-comp.md#std-dtcompatible-nordic-nrf-comp),
  [`nordic,nrf-lpcomp`](../build/dts/api/bindings/comparator/nordic%2Cnrf-lpcomp.md#std-dtcompatible-nordic-nrf-lpcomp) and [`nxp,kinetis-acmp`](../build/dts/api/bindings/comparator/nxp%2Ckinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp) are supported.
- **Stepper Motors**:
  It is now possible to interact with stepper motors using a standard API thanks to the new
  [stepper](../hardware/peripherals/stepper.md#stepper-api) device driver subsystem, which also comes with shell support.
  Initially implemented drivers include a simple [`zephyr,gpio-steppers`](../build/dts/api/bindings/stepper/zephyr%2Cgpio-stepper.md#std-dtcompatible-zephyr-gpio-steppers) and a complex
  sensor-less stall-detection capable with integrated ramp-controller [`adi,tmc5041`](../build/dts/api/bindings/stepper/adi/adi%2Ctmc5041.md#std-dtcompatible-adi-tmc5041).
- **Haptics**:
  A new [Haptics](../hardware/peripherals/haptics.md#haptics-api) device driver subsystem allows unified access to haptic controllers,
  enabling users to add haptic feedback to their applications.
- **Multimedia Capabilities**
  Zephyr’s audio and video capabilities have been expanded with support for new image sensors, video
  interfaces, audio interfaces, and codecs being supported.
- **Prometheus Library**:
  A [Prometheus](https://prometheus.io/) metrics library has been added to the networking stack. It provides a way to
  expose metrics to Prometheus clients over HTTP, facilitating the consolidated remote monitoring of
  Zephyr devices alongside other systems typically monitored using Prometheus.
- **Documentation Improvements**:
  Several enhancements were made to the online documentation to improve content discovery and
  navigation. These include a new [interactive board catalog](../boards/index.md#boards) and an interactive
  directory for [code samples](../samples/index.md#samples).
- **Expanded Board Support**:
  Over 60 [new boards](#boards-added-in-zephyr-4-0) and
  [shields](#shields-added-in-zephyr-4-0) are supported in Zephyr 4.0.

An overview of the changes required or recommended when migrating your application from Zephyr
v3.7.0 to Zephyr v4.0.0 can be found in the separate [migration guide](migration-guide-4.0.md#migration-4-0).

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

- [**CVE 2024-8798**](https://www.cve.org/CVERecord?id=CVE-2024-8798): Under embargo until 2024-11-22
- [**CVE 2024-10395**](https://www.cve.org/CVERecord?id=CVE-2024-10395): Under embargo until 2025-01-23
- [**CVE 2024-11263**](https://www.cve.org/CVERecord?id=CVE-2024-11263) [Zephyr project bug tracker GHSA-jjf3-7x72-pqm9](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-jjf3-7x72-pqm9)

## API Changes

### Removed APIs in this release

- Macro `K_THREAD_STACK_MEMBER`, deprecated since v3.5.0, has been removed.
  Use [`K_KERNEL_STACK_MEMBER`](../doxygen/html/group__thread__stack__api.md#ga600162959def399e70310b944834711f) instead.
- `CBPRINTF_PACKAGE_COPY_*` macros, deprecated since Zephyr 3.5.0, have been removed.
- `_ENUM_TOKEN` and `_ENUM_UPPER_TOKEN` macros, deprecated since Zephyr 2.7.0,
  are no longer generated.
- Removed deprecated arch-level CMSIS header files
  `include/zephyr/arch/arm/cortex_a_r/cmsis.h` and
  `include/zephyr/arch/arm/cortex_m/cmsis.h`. `cmsis_core.h` needs to be
  included now.
- Removed deprecated `ceiling_fraction` macro. [`DIV_ROUND_UP`](../doxygen/html/group__sys-util.md#gae664e7492e37d324831caf2321ddda37) needs
  to be used now.
- Removed deprecated header file
  `include/zephyr/random/rand32.h`. `random.h` needs to be included now.
- Deprecated `EARLY`, `APPLICATION` and `SMP` init levels can no longer be
  used for devices.
- Removed deprecated net\_pkt functions.

### Deprecated in this release

- Deprecated the [`net_buf_put()`](../doxygen/html/group__net__buf.md#ga7e1bcc520b7bffcbd9c1d3d308100047) and [`net_buf_get()`](../doxygen/html/group__net__buf.md#ga014a0e87afc143d06a7eaf6c2f04c742) API functions in favor of
  [`k_fifo_put()`](../doxygen/html/group__fifo__apis.md#ga3addb10f86f19e245c23362433d5c913) and [`k_fifo_get()`](../doxygen/html/group__fifo__apis.md#ga1e2c480e2124116af97e94e7b4435de6).
- The [Keyboard Scan](../hardware/peripherals/kscan.md#kscan-api) subsystem has been marked as deprecated.
- Deprecated the TinyCrypt shim driver `CONFIG_CRYPTO_TINYCRYPT_SHIM`.
- [native\_posix](../boards/native/native_posix/doc/index.md#native-posix) has been deprecated in favour of
  [native\_sim](../boards/native/native_sim/doc/index.md#native-sim).
- `include/zephyr/net/buf.h` is deprecated in favor of
  `include/zephyr/net_buf.h>`. The old header will be removed in future releases
  and its usage should be avoided.
- Deprecated the [`net_buf_put()`](../doxygen/html/group__net__buf.md#ga7e1bcc520b7bffcbd9c1d3d308100047) and [`net_buf_get()`](../doxygen/html/group__net__buf.md#ga014a0e87afc143d06a7eaf6c2f04c742) API functions.

## Architectures

- ARC
- ARM

  - Added support of device memory attributes on Cortex-M (arm\_mpu\_v8)
- ARM64

  - Added initial support for [`arch_stack_walk()`](../doxygen/html/group__arch-stackwalk.md#ga7129c254277cfa162cd9c5778a7662c2) that supports unwinding via esf only
  - Added sys\_arch\_reboot() support to ARM64
  - Added support for demand paging.
  - Added support for Linkable Loadable Extensions (LLEXT).
- RISC-V

  - The stack traces upon fatal exception now prints the address of stack pointer (sp) or frame
    pointer (fp) depending on the build configuration.
  - When [`CONFIG_EXTRA_EXCEPTION_INFO`](../kconfig.md#CONFIG_EXTRA_EXCEPTION_INFO "CONFIG_EXTRA_EXCEPTION_INFO") is enabled, the exception stack frame (arch\_esf)
    has an additional field `csf` that points to the callee-saved-registers upon an fatal error,
    which can be accessed in [`k_sys_fatal_error_handler()`](../doxygen/html/group__fatal__apis.md#ga255cc816d227f0a5c0e80e61bfba11fa) by `esf->csf`.

    - For SoCs that select `RISCV_SOC_HAS_ISR_STACKING`, the `SOC_ISR_STACKING_ESF_DECLARE` has to
      include the `csf` member, otherwise the build would fail.
- Xtensa
- x86

  - Added initial support for [`arch_stack_walk()`](../doxygen/html/group__arch-stackwalk.md#ga7129c254277cfa162cd9c5778a7662c2) that supports unwinding via esf only

## Kernel

- Devicetree devices are now exported to [Linkable Loadable Extensions (LLEXT)](../services/llext/index.md#llext).

## Bluetooth

- Audio

  - [`bt_tbs_client_register_cb()`](../doxygen/html/group__bt__tbs.md#gabe2251d4ea88306793dc68ae683886bb) now supports multiple listeners and may now return an error.
  - Added APIs for getting and setting the assisted listening stream values in codec capabilities
    and codec configuration:

    - [`bt_audio_codec_cfg_meta_get_assisted_listening_stream()`](../doxygen/html/group__bt__audio__codec__cfg.md#ga22ae14fce65b757e31f391c4bdcae328)
    - [`bt_audio_codec_cfg_meta_set_assisted_listening_stream()`](../doxygen/html/group__bt__audio__codec__cfg.md#ga67d83559cbe6cfab235f2e588cbc398c)
    - [`bt_audio_codec_cap_meta_get_assisted_listening_stream()`](../doxygen/html/group__bt__audio__codec__cap.md#ga4f1ea56f2c1c21420f078d35081ceee5)
    - [`bt_audio_codec_cap_meta_set_assisted_listening_stream()`](../doxygen/html/group__bt__audio__codec__cap.md#ga3346db1f59cb35b9b9e5255424adb6e4)
  - Added APIs for getting and setting the broadcast name in codec capabilities
    and codec configuration:

    - [`bt_audio_codec_cfg_meta_get_broadcast_name()`](../doxygen/html/group__bt__audio__codec__cfg.md#ga5d80babcd6f381014e1fae98a755e1d3)
    - [`bt_audio_codec_cfg_meta_set_broadcast_name()`](../doxygen/html/group__bt__audio__codec__cfg.md#ga4f5cbacebedc8d7df02d1c47b140bf3c)
    - [`bt_audio_codec_cap_meta_get_broadcast_name()`](../doxygen/html/group__bt__audio__codec__cap.md#ga3c8df3fe79f0bb96c4e15e7c2502bf89)
    - [`bt_audio_codec_cap_meta_set_broadcast_name()`](../doxygen/html/group__bt__audio__codec__cap.md#ga461add2808a1eca8993222d2b31d5a5f)
- Host

  - Added API [`bt_gatt_get_uatt_mtu()`](../doxygen/html/group__bt__gatt__server.md#ga6653de5e245cae6dc12cd0b45acbe028) to get current Unenhanced ATT MTU of a given
    connection (experimental).
  - Added [`CONFIG_BT_CONN_TX_NOTIFY_WQ`](../kconfig.md#CONFIG_BT_CONN_TX_NOTIFY_WQ "CONFIG_BT_CONN_TX_NOTIFY_WQ").
    The option allows using a separate workqueue for connection TX notify processing
    (`bt_conn_tx_notify()`) to make Bluetooth stack more independent from the system workqueue.
  - The host now disconnects from the peer upon ATT timeout.
  - Added a warning to [`bt_conn_le_create()`](../doxygen/html/group__bt__conn.md#ga8d66f3e0262a51279e9fa8b3139252e6) and [`bt_conn_le_create_synced()`](../doxygen/html/group__bt__conn.md#ga98f99c893e444d1ad1ecd9139803c0b1) if
    the connection pointer passed as an argument is not NULL.
  - Added Kconfig option [`CONFIG_BT_CONN_CHECK_NULL_BEFORE_CREATE`](../kconfig.md#CONFIG_BT_CONN_CHECK_NULL_BEFORE_CREATE "CONFIG_BT_CONN_CHECK_NULL_BEFORE_CREATE") to enforce
    [`bt_conn_le_create()`](../doxygen/html/group__bt__conn.md#ga8d66f3e0262a51279e9fa8b3139252e6) and [`bt_conn_le_create_synced()`](../doxygen/html/group__bt__conn.md#ga98f99c893e444d1ad1ecd9139803c0b1) return an error if the
    connection pointer passed as an argument is not NULL.
  - Fixed an ltk derive issue in L2CAP
  - Added listener callback for discovery (BR)
  - Corrected BR bonding type (SSP)
  - Added support for non-bondable mode (SSP)
  - Changed SSP so that no MITM if required level is less than L3
  - Added checking the receiving buffer length before pulling data (AVDTP)
  - Added support of security level 4 to SSP
  - Fixed LE LTK cannot be derived
  - Added support for Multi-Command Packet (l2cap)
  - Improved the L2CAP code to Set flags in CFG RSP
  - Improved the L2CAP code to handle all configuration options
  - Improved the SSP code to clear pairing flag if ssp pairing completed area
  - Improved the SMP code to check if remote supports CID 0x0007
  - Added support for SMP CT2 flag
  - Improved the SSP code so the proper callback is called when pairing fails
- Controller

  - Added Periodic Advertising Sync Transfer (PAST) support with support for both sending and receiving roles.
    The option can be enabled by [`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER`](../kconfig.md#CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER "CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER") and
    [`CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER`](../kconfig.md#CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER "CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER").
- HCI Drivers
- Mesh

  - Introduced a mesh-specific workqueue to increase reliability of the mesh messages
    transmission. To get the old behavior enable [`CONFIG_BT_MESH_WORKQ_SYS`](../kconfig.md#CONFIG_BT_MESH_WORKQ_SYS "CONFIG_BT_MESH_WORKQ_SYS").

## Boards & SoC Support

- Added support for these SoC series:

  - Added ESP32-C2 and ESP8684 SoC support.
  - Added STM32U0 series with GPIO, Serial, I2C, DAC, ADC, flash, PWM and counter driver support.
  - Added STM32WB0 series with GPIO, Serial, I2C, SPI, ADC, DMA and flash driver support.
  - Added STM32U545xx SoC variant.
  - Added NXP i.MX93’s Cortex-M33 core
  - Added NXP MCXW71, MCXC242, MCXA156, MCXN236, MCXC444, RT1180
- Made these changes in other SoC series:

  - NXP S32Z270: Added support for the new silicon cut version 2.0. Note that the previous
    versions (1.0 and 1.1) are no longer supported.
  - NXP s32k3: fixed RAM retention issue
  - NXP s32k1: obtain system clock frequency from Devicetree
    versions (1.0 and 1.1) are no longer supported.
  - Added ESP32 WROVER-E-N16R4 variant.
  - STM32H5: Added support for OpenOCD through STMicroelectronics OpenOCD fork.
  - MAX32: Enabled Segger RTT and SystemView support.
  - Silabs Series 2: Use oscillator, clock and DCDC configuration from device tree during init.
  - Silabs Series 2: Added initialization for SMU (Security Management Unit).
  - Silabs Series 2: Use sleeptimer as the default OS timer instead of systick.
  - NXP i.MX8MP: Enable the IRQ\_STEER interrupt controller.
  - NXP RWxxx:

    > - added additional support to Wakeup from low power modes
    > - RW61x: increased main stack size to avoid stack overflows when running BLE
    > - RW612: enabled SCTIMER
  - NXP IMXRT: Fixed flexspi boot issue caused by an erroneous relocation of the Flash Configuration Block
    of Kconfig defaults being sourced
  - NXP RT11xx: enabled FlexIO
  - NXP IMXRT116x: Fixed bus clocking to align with the settings of the MCUXpresso SDK
  - NXP mimxrt685: fixed clocks to enable DMIC
  - NXP MCX N Series: Fixed NXP LPSPI native chip select when using synchronous API with DMA bug
  - Nordic nRF54H: Added support for the FLPR (Fast Lightweight Processor) RISC-V CPU.

- Added support for these boards:

  > - [01space ESP32C3 0.42 OLED](../boards/01space/esp32c3_042_oled/doc/index.md#esp32c3_042_oled) (`esp32c3_042_oled`)
  > - [ADI MAX32662EVKIT](../boards/adi/max32662evkit/doc/index.md#max32662evkit) (`max32662evkit`)
  > - [ADI MAX32666EVKIT](../boards/adi/max32666evkit/doc/index.md#max32666evkit) (`max32666evkit`)
  > - [ADI MAX32666FTHR](../boards/adi/max32666fthr/doc/index.md#max32666fthr) (`max32666fthr`)
  > - [ADI MAX32675EVKIT](../boards/adi/max32675evkit/doc/index.md#max32675evkit) (`max32675evkit`)
  > - [ADI MAX32690FTHR](../boards/adi/max32690fthr/doc/index.md#max32690fthr) (`max32690fthr`)
  > - [Arduino Nicla Vision](../boards/arduino/nicla_vision/doc/index.md#arduino-nicla-vision-board) (`arduino_nicla_vision`)
  > - [BeagleBone AI-64](../boards/beagle/beaglebone_ai64/doc/index.md#beaglebone_ai64) (`beaglebone_ai64`)
  > - [BeaglePlay (CC1352)](../boards/beagle/beagleplay/doc/beagleplay_cc1352p7.md#beagleplay) (`beagleplay`)
  > - [DPTechnics Walter](../boards/dptechnics/walter/doc/index.md#walter) (`walter`)
  > - [Espressif ESP32-C3-DevKitC](../boards/espressif/esp32c3_devkitc/doc/index.md#esp32c3_devkitc) (`esp32c3_devkitc`)
  > - [Espressif ESP32-C3-DevKit-RUST](../boards/espressif/esp32c3_rust/doc/index.md#esp32c3_rust) (`esp32c3_rust`)
  > - [Espressif ESP32-S3-EYE](../boards/espressif/esp32s3_eye/doc/index.md#esp32s3_eye) (`esp32s3_eye`)
  > - [Espressif ESP8684-DevKitM](../boards/espressif/esp8684_devkitm/doc/index.md#esp8684_devkitm) (`esp8684_devkitm`)
  > - [Gardena Smart Garden Radio Module](../boards/gardena/sgrm/doc/index.md#sgrm) (`sgrm`)
  > - [mikroe STM32 M4 Clicker](../boards/mikroe/stm32_m4_clicker/doc/index.md#mikroe_stm32_m4_clicker) (`mikroe_stm32_m4_clicker`)
  > - [Nordic Semiconductor nRF54L15 DK](../boards/nordic/nrf54l15dk/doc/index.md#nrf54l15dk-nrf54l15) (`nrf54l15dk`)
  > - [Nordic Semiconductor nRF54L20 PDK](../boards/nordic/nrf54l20pdk/doc/index.md#nrf54l20pdk-nrf54l20) (`nrf54l20pdk`)
  > - [Nordic Semiconductor nRF7002 DK](../boards/nordic/nrf7002dk/doc/index.md#nrf7002dk-nrf5340) (`nrf7002dk`)
  > - [Nuvoton NPCM400\_EVB](../boards/nuvoton/npcm400_evb/doc/index.md#npcm400_evb) (`npcm400_evb`)
  > - [NXP FRDM-MCXA156](../boards/nxp/frdm_mcxa156/doc/index.md#frdm_mcxa156) (`frdm_mcxa156`)
  > - [NXP FRDM-MCXC242](../boards/nxp/frdm_mcxc242/doc/index.md#frdm_mcxc242) (`frdm_mcxc242`)
  > - [NXP FRDM-MCXC444](../boards/nxp/frdm_mcxc444/doc/index.md#frdm_mcxc444) (`frdm_mcxc444`)
  > - [NXP FRDM-MCXN236](../boards/nxp/frdm_mcxn236/doc/index.md#frdm_mcxn236) (`frdm_mcxn236`)
  > - [NXP FRDM-MCXW71](../boards/nxp/frdm_mcxw71/doc/index.md#frdm_mcxw71) (`frdm_mcxw71`)
  > - [NXP i.MX95 EVK](../boards/nxp/imx95_evk/doc/index.md#imx95_evk) (`imx95_evk`)
  > - [NXP MIMXRT1180-EVK](../boards/nxp/mimxrt1180_evk/doc/index.md#mimxrt1180_evk) (`mimxrt1180_evk`)
  > - [PHYTEC phyBOARD-Nash i.MX93](../boards/phytec/phyboard_nash/doc/index.md#phyboard-nash) (`phyboard_nash`)
  > - [Renesas RA2A1 Evaluation Kit](../boards/renesas/ek_ra2a1/doc/index.md#ek-ra2a1) (`ek_ra2a1`)
  > - [Renesas RA4E2 Evaluation Kit](../boards/renesas/ek_ra4e2/doc/index.md#ek-ra4e2) (`ek_ra4e2`)
  > - [Renesas RA4M2 Evaluation Kit](../boards/renesas/ek_ra4m2/doc/index.md#ek-ra4m2) (`ek_ra4m2`)
  > - [Renesas RA4M3 Evaluation Kit](../boards/renesas/ek_ra4m3/doc/index.md#ek-ra4m3) (`ek_ra4m3`)
  > - [Renesas RA4W1 Evaluation Kit](../boards/renesas/ek_ra4w1/doc/index.md#ek-ra4w1) (`ek_ra4w1`)
  > - [Renesas RA6E2 Evaluation Kit](../boards/renesas/ek_ra6e2/doc/index.md#ek-ra6e2) (`ek_ra6e2`)
  > - [Renesas RA6M1 Evaluation Kit](../boards/renesas/ek_ra6m1/doc/index.md#ek-ra6m1) (`ek_ra6m1`)
  > - [Renesas RA6M2 Evaluation Kit](../boards/renesas/ek_ra6m2/doc/index.md#ek-ra6m2) (`ek_ra6m2`)
  > - [Renesas RA6M3 Evaluation Kit](../boards/renesas/ek_ra6m3/doc/index.md#ek-ra6m3) (`ek_ra6m3`)
  > - [Renesas RA6M4 Evaluation Kit](../boards/renesas/ek_ra6m4/doc/index.md#ek-ra6m4) (`ek_ra6m4`)
  > - [Renesas RA6M5 Evaluation Kit](../boards/renesas/ek_ra6m5/doc/index.md#ek-ra6m5) (`ek_ra6m5`)
  > - [Renesas RA8D1 Evaluation Kit](../boards/renesas/ek_ra8d1/doc/index.md#ek-ra8d1) (`ek_ra8d1`)
  > - [Renesas RA6E1 Fast Prototyping Board](../boards/renesas/fpb_ra6e1/doc/index.md#fpb-ra6e1) (`fpb_ra6e1`)
  > - [Renesas RA6E2 Fast Prototyping Board](../boards/renesas/fpb_ra6e2/doc/index.md#fpb-ra6e2) (`fpb_ra6e2`)
  > - [Renesas RA8T1 Evaluation Kit](../boards/renesas/mck_ra8t1/doc/index.md#mcb-ra8t1) (`mck_ra8t1`)
  > - [Renode Cortex-R8 Virtual](../boards/renode/cortex_r8_virtual/doc/index.md#cortex_r8_virtual) (`cortex_r8_virtual`)
  > - [Seeed XIAO ESP32-S3 Sense Variant](../boards/seeed/xiao_esp32s3/doc/index.md#xiao_esp32s3): `xiao_esp32s3`.
  > - [sensry.io Ganymed Break-Out-Board (BOB)](../boards/sensry/ganymed_bob/doc/index.md#ganymed-bob) (`ganymed_bob`)
  > - [SiLabs SiM3U1xx 32-bit MCU USB Development Kit](../boards/silabs/dev_kits/sim3u1xx_dk/doc/index.md#sim3u1xx_dk) (`sim3u1xx_dk`)
  > - [SparkFun Thing Plus Matter](../boards/sparkfun/thing_plus_matter_mgm240p/doc/index.md#sparkfun-thing-plus-mgm240p) (`sparkfun_thing_plus_matter_mgm240p`)
  > - [ST Nucleo G431KB](../boards/st/nucleo_g431kb/doc/index.md#nucleo_g431kb) (`nucleo_g431kb`)
  > - [ST Nucleo H503RB](../boards/st/nucleo_h503rb/doc/index.md#nucleo_h503rb) (`nucleo_h503rb`)
  > - [ST Nucleo H755ZI-Q](../boards/st/nucleo_h755zi_q/doc/index.md#nucleo_h755zi_q) (`nucleo_h755zi_q`)
  > - [ST Nucleo U031R8](../boards/st/nucleo_u031r8/doc/index.md#nucleo_u031r8) (`nucleo_u031r8`)
  > - [ST Nucleo U083RC](../boards/st/nucleo_u083rc/doc/index.md#nucleo_u083rc) (`nucleo_u083rc`)
  > - [ST Nucleo WB05KZ](../boards/st/nucleo_wb05kz/doc/index.md#nucleo_wb05kz) (`nucleo_wb05kz`)
  > - [ST Nucleo WB09KE](../boards/st/nucleo_wb09ke/doc/index.md#nucleo_wb09ke) (`nucleo_wb09ke`)
  > - [ST STM32U083C-DK](../boards/st/stm32u083c_dk/doc/index.md#stm32u083c_dk) (`stm32u083c_dk`)
  > - [TI CC1352P7 LaunchPad](../boards/ti/cc1352p7_launchpad/doc/index.md#cc1352p7_lp) (`cc1352p7_lp`)
  > - [vcc-gnd YD-STM32H750VB](../boards/vcc-gnd/yd_stm32h750vb/doc/index.md#yd_stm32h750vb) (`yd_stm32h750vb`)
  > - [WeAct Studio STM32F405 Core Board V1.0](../boards/weact/stm32f405_core/doc/index.md#weact_stm32f405_core) (`weact_stm32f405_core`)
  > - [WeAct Studio USB2CANFDV1](../boards/weact/usb2canfdv1/doc/index.md#usb2canfdv1) (`usb2canfdv1`)
  > - [Witte Technology Linum Board](../boards/witte/linum/doc/index.md#linum) (`linum`)
- Made these board changes:

  - The nrf54l15bsim target now includes models of the AAR, CCM and ECB peripherals, and many
    other improvements.
  - Support for Google Kukui EC board (`google_kukui`) has been dropped.
  - STM32: Deprecated MCO configuration via Kconfig in favour of setting it through Devicetree.
    See `samples/boards/st/mco` sample.
  - STM32: STM32CubeProgrammer is now the default runner on all STMicroelectronics STM32 boards.
  - Removed the `nrf54l15pdk` board, use [nRF54L15 DK](../boards/nordic/nrf54l15dk/doc/index.md#nrf54l15dk-nrf54l15) instead.
  - PHYTEC: `mimx8mp_phyboard_pollux` has been renamed to [phyboard\_pollux](../boards/phytec/phyboard_pollux/doc/index.md#phyboard-pollux),
    with the old name marked as deprecated.
  - PHYTEC: `mimx8mm_phyboard_polis` has been renamed to [phyboard\_polis](../boards/phytec/phyboard_polis/doc/index.md#phyboard-polis),
    with the old name marked as deprecated.
  - The board qualifier for MPS3/AN547 is changed from:

    - `mps3/an547` to `mps3/corstone300/an547` for secure and
    - `mps3/an547/ns` to `mps3/corstone300/an547/ns` for non-secure.
  - Added Thingy53 forwarding of network core pins to network core for SPI peripheral (disabled
    by default) including pin mappings.
  - Added uart, flexio pwm, flexio spi, watchdog, flash, rtc, i2c, lpspi, edma, gpio, acmp, adc and lptmr support
    to NXP `frdm_ke17z` and `frdm_ke17z512`
  - Enabled support for MCUmgr on NXP boards
  - Enabled MCUboot, FlexCAN, LPI2C, VREF, LPADC and timers (TPM, LPTMR, counter, watchdog) on NXP `frdm_mcxw71`
  - Enabled I2C, PWM on NXP `imx95_evk`
  - Enabled FLEXCAN, LPI2C on NXP `s32z2xxdc2`
  - Enabled DSPI and EDMA3 on NXP `s32z270dc2`
  - Enabled ENET ethernet on NXP `imx8mm` and `imx8mn`
  - Added support for the NXP `imx8qm` and `imx8qxp` DSP core to enable the openAMP sample

- Added support for the following shields:

  - [ADI EVAL-ADXL362-ARDZ](../boards/shields/eval_adxl362_ardz/doc/index.md#eval-adxl362-ardz)
  - [ADI EVAL-ADXL372-ARDZ](../boards/shields/eval_adxl372_ardz/doc/index.md#eval-adxl372-ardz)
  - [Digilent Pmod ACL](../boards/shields/pmod_acl/doc/index.md#pmod-acl)
  - [MikroElektronika BLE TINY Click](../boards/shields/mikroe_ble_tiny_click/doc/index.md#mikroe-ble-tiny-click-shield)
  - [Nordic SemiConductor nRF7002 EB](../boards/shields/nrf7002eb/doc/index.md#nrf7002eb)
  - [Nordic SemiConductor nRF7002 EK](../boards/shields/nrf7002ek/doc/index.md#nrf7002ek)
  - [ST X-NUCLEO-WB05KN1: BLE expansion board](../boards/shields/x_nucleo_wb05kn1/doc/index.md#x-nucleo-wb05kn1)
  - [WeAct Studio MiniSTM32H7xx OV2640 Camera Sensor](../boards/shields/weact_ov2640_cam_module/doc/index.md#weact-ov2640-cam-module)

## Build system and Infrastructure

- Added support for .elf files to the west flash command for jlink, pyocd and linkserver runners.
- Extracted pickled EDT generation from gen\_defines.py into gen\_edt.py. This moved the following
  parameters from the cmake variable `EXTRA_GEN_DEFINES_ARGS` to `EXTRA_GEN_EDT_ARGS`:

  > - `--dts`
  > - `--dtc-flags`
  > - `--bindings-dirs`
  > - `--dts-out`
  > - `--edt-pickle-out`
  > - `--vendor-prefixes`
  > - `--edtlib-Werror`
- Switched to using imgtool directly from the build system when signing images instead of calling
  `west sign`.
- Added support for selecting MCUboot operating mode in sysbuild using `SB_CONFIG_MCUBOOT_MODE`.
- Added support for RAM-load MCUboot operating mode in build system, including sysbuild support.
- Added a script parameter to Twister to enable HW specific arguments, such as a system specific
  timeout

## Documentation

- Added a new [interactive board catalog](../boards/index.md#boards) enabling users to search boards by criteria
  such as name, architecture, vendor, or SoC.
- Added a new [interactive code sample catalog](../samples/index.md#samples) for quickly
  finding code samples based on name and description.
- Added [`zephyr:board`](../contribute/documentation/guidelines.md#directive-zephyr-board "zephyr:board directive") directive and [`zephyr:board`](../contribute/documentation/guidelines.md#role-zephyr-board "zephyr:board role") role to mark Sphinx pages as
  board documentation and reference them from other pages. Most existing board documentation pages
  have been updated to use this directive, with full migration planned for the next release.
- Added [`zephyr:code-sample-category`](../contribute/documentation/guidelines.md#directive-zephyr-code-sample-category "zephyr:code-sample-category directive") directive to describe and group code samples in the
  documentation.
- Added a link to the source code of the driver matching a binding’s compatible string (when one can
  be found in the Zephyr tree) to the [Devicetree bindings](../build/dts/api/bindings.md#devicetree-binding-index) documentation.
- Added a button to all code sample README pages allowing to directly browse the sample’s source
  code on GitHub.
- Moved Zephyr C API documentation out of main documentation. API references now feature a rich
  tooltip and link to the dedicated Doxygen site.
- Added two new build commands, `make html-live` and `make html-live-fast`, that automatically
  locally host the generated documentation. They also automatically rebuild and rehost the
  documentation when changes to the input `.rst` files are detected on the filesystem.

## Drivers and Sensors

- ADC

  - Added proper ADC2 calibration entries in ESP32.
  - Fixed calibration scheme in ESP32-S3.
  - STM32H7: Added support for higher sampling frequencies thanks to boost mode implementation.
  - Added initial support for Renesas RA8 ADC driver ([`renesas,ra-adc`](../build/dts/api/bindings/adc/renesas%2Cra-adc.md#std-dtcompatible-renesas-ra-adc))
  - Added driver for Analog Devices MAX32 SoC series ([`adi,max32-adc`](../build/dts/api/bindings/adc/adi%2Cmax32-adc.md#std-dtcompatible-adi-max32-adc)).
  - Added support for NXP S32 SAR\_ADC ([`nxp,s32-adc-sar`](../build/dts/api/bindings/adc/nxp%2Cs32-adc-sar.md#std-dtcompatible-nxp-s32-adc-sar))
  - Added support for Ambiq Apollo3 series ([`ambiq,adc`](../build/dts/api/bindings/adc/ambiq%2Cadc.md#std-dtcompatible-ambiq-adc)).
- CAN

  - Added initial support for Renesas RA CANFD ([`renesas,ra-canfd-global`](../build/dts/api/bindings/can/renesas%2Cra-canfd-global.md#std-dtcompatible-renesas-ra-canfd-global),
    [`renesas,ra-canfd`](../build/dts/api/bindings/can/renesas%2Cra-canfd.md#std-dtcompatible-renesas-ra-canfd))
  - Added Flexcan support for S32Z27x ([`nxp,flexcan`](../build/dts/api/bindings/can/nxp%2Cflexcan.md#std-dtcompatible-nxp-flexcan), [`nxp,flexcan-fd`](../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd))
  - Improved NXP S32 CANXL error reporting ([`nxp,s32-canxl`](../build/dts/api/bindings/can/nxp%2Cs32-canxl.md#std-dtcompatible-nxp-s32-canxl))
- Clock control

  - STM32 MCO (Microcontroller Clock Output) is now available on STM32U5 series.
  - STM32 MCO can and should now be configured with device tree.
  - STM32: [`CONFIG_CLOCK_CONTROL`](../kconfig.md#CONFIG_CLOCK_CONTROL "CONFIG_CLOCK_CONTROL") is now enabled by default at family level and doesn’t need
    to be enabled at board level anymore.
  - STM32H7: PLL FRACN can now be configured (see [`st,stm32h7-pll-clock`](../build/dts/api/bindings/clock/st%2Cstm32h7-pll-clock.md#std-dtcompatible-st-stm32h7-pll-clock))
  - Added initial support for Renesas RA clock control driver ([`renesas,ra-cgc-pclk`](../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk),
    [`renesas,ra-cgc-pclk-block`](../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block), [`renesas,ra-cgc-pll`](../build/dts/api/bindings/clock/renesas%2Cra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll),
    [`renesas,ra-cgc-external-clock`](../build/dts/api/bindings/clock/renesas%2Cra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock), [`renesas,ra-cgc-subclk`](../build/dts/api/bindings/clock/renesas%2Cra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk),
    [`renesas,ra-cgc-pll-out`](../build/dts/api/bindings/clock/renesas%2Cra-cgc-pll-out.md#std-dtcompatible-renesas-ra-cgc-pll-out))
  - Silabs: Added support for Series 2+ Clock Management Unit (see [`silabs,series-clock`](../build/dts/api/bindings/clock/silabs%2Cseries-clock.md#std-dtcompatible-silabs-series-clock))
  - Added initial support for Nordic nRF54H Series clock controllers.
- Codec (Audio)

  - Added a driver for the Wolfson WM8904 audio codec ([`wolfson,wm8904`](../build/dts/api/bindings/audio/wolfson%2Cwm8904.md#std-dtcompatible-wolfson-wm8904))
- Comparator

  - Introduced comparator device driver subsystem selected with [`CONFIG_COMPARATOR`](../kconfig.md#CONFIG_COMPARATOR "CONFIG_COMPARATOR")
  - Introduced comparator shell commands selected with [`CONFIG_COMPARATOR_SHELL`](../kconfig.md#CONFIG_COMPARATOR_SHELL "CONFIG_COMPARATOR_SHELL")
  - Added support for Nordic nRF COMP ([`nordic,nrf-comp`](../build/dts/api/bindings/comparator/nordic%2Cnrf-comp.md#std-dtcompatible-nordic-nrf-comp))
  - Added support for Nordic nRF LPCOMP ([`nordic,nrf-lpcomp`](../build/dts/api/bindings/comparator/nordic%2Cnrf-lpcomp.md#std-dtcompatible-nordic-nrf-lpcomp))
  - Added support for NXP Kinetis ACMP ([`nxp,kinetis-acmp`](../build/dts/api/bindings/comparator/nxp%2Ckinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp))
- Counter

  - Added initial support for Renesas RA8 AGT counter driver ([`renesas,ra-agt`](../build/dts/api/bindings/misc/renesas%2Cra-agt.md#std-dtcompatible-renesas-ra-agt))
  - Added driver for Analog Devices MAX32 SoC series ([`adi,max32-counter`](../build/dts/api/bindings/counter/adi%2Cmax32-counter.md#std-dtcompatible-adi-max32-counter)).
  - Updated the NXP counter\_mcux\_lptmr driver to support multiple instances of the lptmr
    peripheral.
  - Converted the NXP S32 System Timer Module driver to native Zephyr code
  - Added support for late and short relative alarms area to NXP nxp\_sys\_timer ([`nxp,s32-sys-timer`](../build/dts/api/bindings/timer/nxp%2Cs32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer))
- Crypto

  - Added support for STM32L4 AES.
- DAC

  - DAC API now supports specifying channel path as internal. Support has been added in STM32 drivers.
- Disk

  - STM32F7 SDMMC driver now supports usage of DMA.
  - STM32 mem controller driver now supports FMC for STM32H5.
  - SDMMC subsystem driver will now power down the SD card when the disk is
    deinitialized
- Display

  - NXP ELCDIF driver now supports flipping the image along the horizontal
    or vertical axis using the PXP. Use
    [`CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION`](../kconfig.md#CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION "CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION") to set the desired
    flip.
  - ST7789V driver now supports BGR565, enabled with
    [`CONFIG_ST7789V_BGR565`](../kconfig.md#CONFIG_ST7789V_BGR565 "CONFIG_ST7789V_BGR565").
  - Added driver for SSD1327 OLED display controller ([`solomon,ssd1327fb`](../build/dts/api/bindings/display/solomon%2Cssd1327fb.md#std-dtcompatible-solomon-ssd1327fb)).
  - Added driver for SSD1322 OLED display controller ([`solomon,ssd1322`](../build/dts/api/bindings/display/solomon%2Cssd1322.md#std-dtcompatible-solomon-ssd1322)).
  - Added driver for IST3931 monochrome display controller ([`istech,ist3931`](../build/dts/api/bindings/display/istech%2Cist3931.md#std-dtcompatible-istech-ist3931)).
- DMA

  - Added driver for Analog Devices MAX32 SoC series ([`adi,max32-dma`](../build/dts/api/bindings/dma/adi%2Cmax32-dma.md#std-dtcompatible-adi-max32-dma)).
  - Added flip feature to the NXP dma\_mcux\_pxp driver ([`nxp,pxp`](../build/dts/api/bindings/dma/nxp%2Cpxp.md#std-dtcompatible-nxp-pxp))
  - Added support for eDMAv5 and cyclic mode ([GitHub #80584](https://github.com/zephyrproject-rtos/zephyr/issues/80584)) to the NXP EMDA driver ([`nxp,edma`](../build/dts/api/bindings/dma/nxp%2Cedma.md#std-dtcompatible-nxp-edma))
- EEPROM

  - Added support for using the EEPROM simulator with embedded C standard libraries
    ([`zephyr,sim-eeprom`](../build/dts/api/bindings/mtd/zephyr%2Csim-eeprom.md#std-dtcompatible-zephyr-sim-eeprom)).
- Entropy

  - Added initial support for Renesas RA8 Entropy driver ([`renesas,ra-rsip-e51a-trng`](../build/dts/api/bindings/rng/renesas%2Cra-rsip-e51a-trng.md#std-dtcompatible-renesas-ra-rsip-e51a-trng))
  - Added driver for Analog Devices MAX32 SoC series ([`adi,max32-trng`](../build/dts/api/bindings/rng/adi%2Cmax32-trng.md#std-dtcompatible-adi-max32-trng)).
- Ethernet

  - Added a `get_phy()` function to the ethernet driver api, which returns the phy device
    associated to a network interface.
  - Added 2.5G and 5G link speeds to the ethernet hardware capabilities api.
  - Added check for null api pointer in [`net_eth_get_hw_capabilities()`](../doxygen/html/group__ethernet.md#gab0a3b4584bb6ce1d27b98b063fd3fcbd), fixing netusb crash.
  - Added synopsis dwc\_xgmac ethernet driver.
  - Added NXP iMX NETC driver.
  - Adin2111

    - Fixed bug that resulted in double RX buffer read when generic spi protocol is used.
    - Fixed essential thread termination on OA read failure.
    - Skip checks for port 2 on the adin1110 since it doesn’t apply, as there is no port 2.
  - ENC28J60

    - Added support for the `zephyr,random-mac-address` property.
    - Fixed race condition between interrupt service and L2 init affecting carrier status in init.
  - ENC424j600: Added ability to change mac address at runtime with net management api.
  - ESP32: Added configuration of interrupts from DT.
  - Lan865x

    - Enable all multicast MAC address for IPv6. All multicast mac address can now be
      received and allows for correct handling of the IPv6 neighbor discovery protocol.
    - Fixed transmission stopping when setting mac address or promiscuous mode.
  - LiteX

    - Renamed the `compatible` from `litex,eth0` to [`litex,liteeth`](../build/dts/api/bindings/ethernet/litex%2Cliteeth.md#std-dtcompatible-litex-liteeth).
    - Added support for multiple instances of the liteX ethernet driver.
    - Added support for VLAN to the liteX ethernet driver.
    - Added phy support.
  - Native\_posix

    - Implemented getting the interface name from the command line.
    - Now prints error number in error message when creating an interface.
  - NXP ENET\_QOS: Fixed check for `zephyr,random-mac-address` property.
  - NXP ENET:

    - Fixed fused MAC address initialization code.
    - Fixed code path for handling tx errors with timestamped frames.
    - Fixed network carrier status race condition during init.
  - NXP S32: Added configs to enable VLAN promiscuous and untagged, and enable SI message interrupt.
  - STM32

    - Driver can now be configured to use a preemptive RX thread priority, which could be useful
      in case of high network traffic load (reduces jitter).
    - Added support for DT-defined mdio.
    - Fixed bus error after network disconnection that happened in some cases.
  - TC6: Combine read chunks into continuous net buffer. This fixes IPv6 neighbor discovery protocol
    because 64 bytes was not enough for all headers.
  - PHY driver changes

    - Added Qualcomm AR8031 phy driver.
    - Added DP83825 phy driver.
    - PHY\_MII

      - Fixed generic phy\_mii driver not using the value of the `no-reset` property from Devicetree.
      - Removed excess newlines from log output of phy\_mii driver.
    - KSZ8081

      - Fixed reset times during init that were unnecessarily long.
      - Removed unnecessary reset on every link configuration that blocked system workqueue
      - Fixed issue relating to strap-in override bits.
- Flash

  - Fixed SPI NOR driver issue where wp, hold and reset pins were incorrectly initialized from
    device tee when SFDP at run-time has been enabled ([GitHub #80383](https://github.com/zephyrproject-rtos/zephyr/issues/80383))
  - Updated all Espressif’s SoC driver initialization to allow new chipsets and octal flash support.
  - Added [`CONFIG_SPI_NOR_ACTIVE_DWELL_MS`](../kconfig.md#CONFIG_SPI_NOR_ACTIVE_DWELL_MS "CONFIG_SPI_NOR_ACTIVE_DWELL_MS"), to the SPI NOR driver configuration,
    which allows setting the time during which the driver will wait before triggering Deep Power Down (DPD).
    This option replaces `CONFIG_SPI_NOR_IDLE_IN_DPD`, aiming at reducing unnecessary power
    state changes and SPI transfers between other operations, specifically when burst type
    access to an SPI NOR device occurs.
  - Added [`CONFIG_SPI_NOR_INIT_PRIORITY`](../kconfig.md#CONFIG_SPI_NOR_INIT_PRIORITY "CONFIG_SPI_NOR_INIT_PRIORITY") to allow selecting the SPI NOR driver initialization priority.
  - The flash API has been extended with the [`flash_copy()`](../doxygen/html/group__flash__interface.md#ga847407358a20d3d5918d8ef11657ce2b) utility function which allows performing
    direct data copies between two Flash API devices.
  - Fixed a Flash Simulator issue where offsets were assumed to be absolute instead of relative
    to the device base address ([GitHub #79082](https://github.com/zephyrproject-rtos/zephyr/issues/79082)).
  - Extended STM32 OSPI drivers to support QUAL, DUAL and SPI modes. Additionally, added support
    for custom write and SFDP:BFP opcodes.
  - Added possibility to run STM32H7 flash driver from Cortex-M4 core.
  - Implemented readout protection handling (RDP levels) for STM32F7 SoCs.
  - Added initial support for Renesas RA8 Flash controller driver ([`renesas,ra-flash-hp-controller`](../build/dts/api/bindings/flash_controller/renesas%2Cra-flash-hp-controller.md#std-dtcompatible-renesas-ra-flash-hp-controller))
  - Added driver for Analog Devices MAX32 SoC series ([`adi,max32-flash-controller`](../build/dts/api/bindings/flash_controller/adi%2Cmax32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller)).
  - Added support for W25Q512JV and W25Q512NW-IQ/IN to NXP’s MCUX Flexspi driver
  - Renamed the binding `nxp,iap-msf1` to [`nxp,msf1`](../build/dts/api/bindings/flash_controller/nxp%2Cmsf1.md#std-dtcompatible-nxp-msf1) for accuracy
- GPIO

  - tle9104: Add support for the parallel output mode via setting the properties `parallel-out12` and
    `parallel-out34`.
  - Converted the NXP S32 SIUL2 drivers to native Zephyr code
  - Converted the NXP wake-up drivers to native Zephyr code
- Haptics

  - Introduced a haptics device driver subsystem selected with [`CONFIG_HAPTICS`](../kconfig.md#CONFIG_HAPTICS "CONFIG_HAPTICS")
  - Added support for TI DRV2605 haptic driver IC ([`ti,drv2605`](../build/dts/api/bindings/haptics/ti%2Cdrv2605.md#std-dtcompatible-ti-drv2605))
  - Added a sample for the DRV2605 haptic driver to trigger ROM events ([DRV2605 Haptic Driver](../samples/drivers/haptics/drv2605/README.md#drv2605 "Drive an LRA using the DRV2605 haptic driver chip."))
- I2C

  - Added initial support for Renesas RA8 I2C driver ([`renesas,ra-iic`](../build/dts/api/bindings/i2c/renesas%2Cra-iic.md#std-dtcompatible-renesas-ra-iic))
- I2S

  - Added ESP32-S3 and ESP32-C3 driver support.
- I3C

  - Added support for SETAASA optimization during initialization. Added a
    `supports-setaasa` property to `i3c-devices.yaml`.
  - Added sending DEFTGTS if any devices that support functioning as a secondary
    controller on the bus.
  - Added retrieving GETMXDS within [`i3c_device_basic_info_get()`](../doxygen/html/group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8) if BCR mxds
    bit is set.
  - Added helper functions for sending CCCs for ENTTM, VENDOR, DEFTGTS, SETAASA,
    GETMXDS, SETBUSCON, RSTACT DC, ENTAS0, ENTAS1, ENTAS2, and ENTAS3.
  - Added shell commands for sending CCCs for ENTTM, VENDOR, DEFTGTS, SETAASA,
    GETMXDS, SETBUSCON, RSTACT DC, ENTAS0, ENTAS1, ENTAS2, and ENTAS3.
  - Added shell commands for setting the I3C speed, sending HDR-DDR, raising IBIs,
    enabling IBIs, disabling IBIs, and scanning I2C addresses.
  - [`i3c_ccc_do_setdasa()`](../doxygen/html/group__i3c__ccc.md#gaf4836548527c1a7fe54767c2a7e2ebb9) has been modified to now require specifying the assigned
    dynamic address rather than having the dynamic address be determined within the function.
  - `i3c_determine_default_addr()` has been removed
  - `attach_i3c_device` now no longer requires the attached address as an argument. It is now
    up to the driver to determine the attached address from the `i3c_device_desc`.
- Input

  - New feature: [`zephyr,input-double-tap`](../build/dts/api/bindings/input/zephyr%2Cinput-double-tap.md#std-dtcompatible-zephyr-input-double-tap).
  - New driver: [`ilitek,ili2132a`](../build/dts/api/bindings/input/ilitek%2Cili2132a.md#std-dtcompatible-ilitek-ili2132a).
  - Added power management support to all keyboard matrix drivers, added a
    `no-disconnect` property to [`gpio-keys`](../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) so it can be used
    with power management on GPIO drivers that do not support pin
    disconnection.
  - Added a new framework for touchscreen common properties and features
    (screen size, inversion, xy swap).
  - Fixed broken ESP32 input touch sensor driver.
  - gt911:
    \* Fixed the INT pin to be always set during probe to allow for proper initialization
    \* Fixed OOB buffer write to touch points array
    \* Add support for multitouch events
- Interrupt

  - Updated ESP32 family interrupt allocator with proper IRQ flags and priorities.
  - Implemented a function to set pending interrupts for Arm GIC
  - Added a safe configuration option so multiple OS’es can share the same GIC and avoid reconfiguring
    the distributor
- LED

  - lp5562: added `enable-gpios` property to describe the EN/VCC GPIO of the lp5562.
  - lp5569: added `charge-pump-mode` property to configure the charge pump of the lp5569.
  - lp5569: added `enable-gpios` property to describe the EN/PWM GPIO of the lp5569.
  - LED code samples have been consolidated under the [samples/drivers/led](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/led) directory.
- LED Strip

  - Updated ws2812 GPIO driver to support dynamic bus timings
- Mailbox

  - Added driver support for ESP32 and ESP32-S3 SoCs.
- MDIO

  - Added litex MDIO driver.
  - Added support for mdio shell to stm32 mdio.
  - Added mdio driver for dwc\_xgmac synopsis ethernet.
  - Added NXP IMX NETC mdio driver.
  - NXP ENET MDIO: Fixed inconsistent behavior by keeping the mdio interrupt enabled all the time.
- MEMC

  - Add driver for APS6404L PSRAM using NXP FLEXSPI
- MFD
- Modem

  - Added support for the U-Blox LARA-R6 modem.
  - Added support for setting the modem’s UART baudrate during init.
- MIPI-DBI

  - Added bitbang MIPI-DBI driver, supporting 8080 and 6800 mode
    ([`zephyr,mipi-dbi-bitbang`](../build/dts/api/bindings/mipi-dbi/zephyr%2Cmipi-dbi-bitbang.md#std-dtcompatible-zephyr-mipi-dbi-bitbang)).
  - Added support for STM32 FMC memory controller ([`st,stm32-fmc-mipi-dbi`](../build/dts/api/bindings/mipi-dbi/st%2Cmipi-dbi-fmc.md#std-dtcompatible-st-stm32-fmc-mipi-dbi)).
  - Added support for 8080 mode to NXP LCDIC controller ([`nxp,lcdic`](../build/dts/api/bindings/mipi-dbi/nxp%2Clcdic.md#std-dtcompatible-nxp-lcdic)).
  - Fixed the calculation of the reset delay for NXP’s LCD controller ([`nxp,lcdic`](../build/dts/api/bindings/mipi-dbi/nxp%2Clcdic.md#std-dtcompatible-nxp-lcdic))
- MIPI-CSI

  - Improve NXP CSI and MIPI\_CSI2Rx drivers to support varibale frame rates
- Pin control

  - Added support for Microchip MEC5
  - Added SCMI-based driver for NXP i.MX
  - Added support for i.MX93 M33 core
  - Added support for ESP32C2
  - STM32: [`CONFIG_PINCTRL`](../kconfig.md#CONFIG_PINCTRL "CONFIG_PINCTRL") is now selected by drivers requiring it and
    shouldn’t be enabled at board level anymore.
- PWM

  - rpi\_pico: The driver now configures the divide ratio adaptively.
  - Added initial support for Renesas RA8 PWM driver ([`renesas,ra8-pwm`](../build/dts/api/bindings/pwm/renesas%2Cra8-pwm.md#std-dtcompatible-renesas-ra8-pwm))
  - Added driver for Analog Devices MAX32 SoC series ([`adi,max32-pwm`](../build/dts/api/bindings/pwm/adi%2Cmax32-pwm.md#std-dtcompatible-adi-max32-pwm)).
  - Fixed a build issue of the NXP TPM driver for variants without the capability to combine channels
- Regulators

  - Upgraded CP9314 driver to B1 silicon revision
  - Added basic driver for MPS MPM54304
- RTC

  - STM32: HSE can now be used as domain clock.
  - Added the NXP IRTC Driver.
- RTIO
- SAI

  - Improved NXP’s SAI driver to use a default clock if none is provided in the DT
  - Fixed a bug in the NXP SAI driver that caused a crash on a FIFO under- and overrun
  - Fixed a bug that reset the NXP ESAI during initialization (unnecessary)
  - Added support for PM operations in NXP’s SAI driver
- SDHC

  - Added ESP32-S3 driver support.
  - SPI SDHC driver now handles SPI devices with runtime PM support correctly
  - Improved NXP’s imx SDHC driver to assume card is present if no detection method is provided
- Sensors

  - General

    - The existing driver for the Microchip MCP9808 temperature sensor transformed and renamed to
      support all JEDEC JC 42.4 compatible temperature sensors. It now uses the
      [`jedec,jc-42.4-temp`](../build/dts/api/bindings/sensor/jedec%2Cjc-42.4-temp.md#std-dtcompatible-jedec-jc-42.4-temp) compatible string instead to the `microchip,mcp9808`
      string.
    - Added support for VDD based ADC reference to the NTC thermistor driver.
    - Added Avago APDS9253 ([`avago,apds9253`](../build/dts/api/bindings/sensor/avago%2Capds9253.md#std-dtcompatible-avago-apds9253)) and APDS9306
      ([`avago,apds9306`](../build/dts/api/bindings/sensor/avago%2Capds9306.md#std-dtcompatible-avago-apds9306)) ambient light sensor drivers.
    - Added gain and resolution attributes (`SENSOR_ATTR_GAIN` and
      `SENSOR_ATTR_RESOLUTION`).
  - ADI

    - Add RTIO streaming support to ADXL345, ADXL362, and ADXL372 accelerometer drivers.
  - Bosch

    - Merged BMP390 into BMP388.
    - Added support for power domains to BMM150 and BME680 drivers.
    - Added BMP180 pressure sensor driver ([`bosch,bmp180`](../build/dts/api/bindings/sensor/bosch%2Cbmp180.md#std-dtcompatible-bosch-bmp180)).
  - Memsic

    - Added MMC56X3 magnetometer and temperature sensor driver ([`memsic,mmc56x3`](../build/dts/api/bindings/sensor/memsic%2Cmmc56x3.md#std-dtcompatible-memsic-mmc56x3)).
  - NXP

    - Added P3T1755 digital temperature sensor driver ([`nxp,p3t1755`](../build/dts/api/compatibles/nxp%2Cp3t1755.md#std-dtcompatible-nxp-p3t1755)).
    - Added FXLS8974 accelerometer driver ([`nxp,fxls8974`](../build/dts/api/compatibles/nxp%2Cfxls8974.md#std-dtcompatible-nxp-fxls8974)).
  - ST

    - Aligned drivers to stmemsc HAL i/f v2.6.
    - Added LSM9DS1 accelerometer/gyroscope/magnetometer sensor driver ([`st,lsm9ds1`](../build/dts/api/bindings/sensor/st%2Clsm9ds1.md#std-dtcompatible-st-lsm9ds1)).
  - TDK

    - Added I2C bus support to ICM42670.
  - TI

    - Added support for INA236 to the existing INA230 driver.
    - Added support for TMAG3001 to the existing TMAG5273 driver.
    - Added TMP1075 temperature sensor driver ([`ti,tmp1075`](../build/dts/api/bindings/sensor/ti%2Ctmp1075.md#std-dtcompatible-ti-tmp1075)).
  - Vishay

    - Added trigger capability to VCNL36825T driver.
  - WE

    - Added Würth Elektronik HIDS-2525020210002
      [`we,wsen-hids-2525020210002`](../build/dts/api/bindings/sensor/we%2Cwsen-hids-2525020210002.md#std-dtcompatible-we-wsen-hids-2525020210002) humidity sensor driver.
    - Added general samples for triggers
- Serial

  - LiteX: Renamed the `compatible` from `litex,uart0` to [`litex,uart`](../build/dts/api/bindings/serial/litex%2Cuart.md#std-dtcompatible-litex-uart).
  - Nordic: Removed `CONFIG_UART_n_GPIO_MANAGEMENT` Kconfig options (where n is an instance
    index) which had no use after pinctrl driver was introduced.
  - NS16550: Added support for Synopsys Designware 8250 UART.
  - Renesas: Added support for SCI UART.
  - Sensry: Added UART support for Ganymed SY1XX.
- SPI

  - Added initial support for Renesas RA8 SPI driver ([`renesas,ra8-spi-b`](../build/dts/api/bindings/spi/renesas%2Cra8-spi-b.md#std-dtcompatible-renesas-ra8-spi-b))
  - Added RTIO support to the Analog Devices MAX32 driver.
  - Silabs: Added support for EUSART ([`silabs,gecko-spi-eusart`](../build/dts/api/bindings/spi/silabs%2Cgecko-spi-eusart.md#std-dtcompatible-silabs-gecko-spi-eusart))
- Steppers

  - Introduced stepper controller device driver subsystem selected with
    [`CONFIG_STEPPER`](../kconfig.md#CONFIG_STEPPER "CONFIG_STEPPER")
  - Introduced stepper shell commands for controlling and configuring
    stepper motors with [`CONFIG_STEPPER_SHELL`](../kconfig.md#CONFIG_STEPPER_SHELL "CONFIG_STEPPER_SHELL")
  - Added support for ADI TMC5041 ([`adi,tmc5041`](../build/dts/api/bindings/stepper/adi/adi%2Ctmc5041.md#std-dtcompatible-adi-tmc5041))
  - Added support for gpio-stepper-controller ([`zephyr,gpio-steppers`](../build/dts/api/bindings/stepper/zephyr%2Cgpio-stepper.md#std-dtcompatible-zephyr-gpio-steppers))
  - Added stepper api test-suite
  - Added stepper shell test-suite
- Timer

  - Silabs: Added support for Sleeptimer ([`silabs,gecko-stimer`](../build/dts/api/bindings/rtc/silabs%2Cgecko-stimer.md#std-dtcompatible-silabs-gecko-stimer))
- USB

  - Added support for USB HS on STM32U59x/STM32U5Ax SoC variants.
  - Enhanced DWC2 UDC driver
  - Added UDC drivers for Smartbond, NuMaker USBD and RP2040 device controllers
  - Enabled SoF in NXP USB drivers (UDC)
  - Enabled cache maintenance in the NXP EHCI USB driver
- Video

  - Introduced API to control frame rate
  - Introduced API for partial frames transfer with the video buffer field `line_offset`
  - Introduced API for [multi-heap](../kernel/memory_management/shared_multi_heap.md#memory-management-shared-multi-heap) video buffer allocation with
    [`CONFIG_VIDEO_BUFFER_USE_SHARED_MULTI_HEAP`](../kconfig.md#CONFIG_VIDEO_BUFFER_USE_SHARED_MULTI_HEAP "CONFIG_VIDEO_BUFFER_USE_SHARED_MULTI_HEAP")
  - Introduced bindings for common video link properties in `video-interfaces.yaml`. Migration to the
    new bindings is tracked in [GitHub #80514](https://github.com/zephyrproject-rtos/zephyr/issues/80514)
  - Introduced missing `CONFIG_VIDEO_LOG_LEVEL`
  - Added a sample for capturing video and displaying it with LVGL
    ([Video capture to LVGL](../samples/drivers/video/capture_to_lvgl/README.md#video-capture-to-lvgl "Capture video frames and display them on an LCD using LVGL."))
  - Added an automatic test to check colorbar pattern correctness
  - Added support for GalaxyCore GC2145 image sensor ([`galaxycore,gc2145`](../build/dts/api/bindings/video/galaxycore%2Cgc2145.md#std-dtcompatible-galaxycore-gc2145))
  - Added support for ESP32-S3 LCD-CAM interface ([`espressif,esp32-lcd-cam`](../build/dts/api/bindings/video/espressif%2Cesp32-cam.md#std-dtcompatible-espressif-esp32-lcd-cam))
  - Added support for NXP MCUX SMARTDMA interface ([`nxp,smartdma`](../build/dts/api/bindings/dma/nxp%2Csmartdma.md#std-dtcompatible-nxp-smartdma))
  - Added support for more OmniVision OV2640 controls ([`ovti,ov2640`](../build/dts/api/bindings/video/ovti%2Cov2640.md#std-dtcompatible-ovti-ov2640))
  - Added support for more OmniVision OV5640 controls ([`ovti,ov5640`](../build/dts/api/bindings/video/ovti%2Cov5640.md#std-dtcompatible-ovti-ov5640))
  - STM32: Implemented [`video_get_ctrl()`](../doxygen/html/group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd) and [`video_set_ctrl()`](../doxygen/html/group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e) APIs.
  - Removed an init order circular dependency for the camera pipeline on NXP RT10xx platforms
    ([GitHub #80304](https://github.com/zephyrproject-rtos/zephyr/issues/80304))
  - Added an NXP’s smartdma based video driver ([`nxp,video-smartdma`](../build/dts/api/bindings/video/nxp%2Cvideo-smartdma.md#std-dtcompatible-nxp-video-smartdma))
  - Added frame interval APIs to support variable frame rates (video\_sw\_generator.c)
  - Added image controls to the OV5640 driver
- W1

  - Added 1-Wire master driver for Analog Devices MAX32 SoC series ([`adi,max32-w1`](../build/dts/api/bindings/w1/adi%2Cmax32-w1.md#std-dtcompatible-adi-max32-w1))
- Watchdog

  - Added driver for Analog Devices MAX32 SoC series ([`adi,max32-watchdog`](../build/dts/api/bindings/watchdog/adi%2Cmax32-watchdog.md#std-dtcompatible-adi-max32-watchdog)).
  - Converted NXP S32 Software Watchdog Timer driver to native Zephyr code
- Wi-Fi

  - Add Wi-Fi Easy Connect (DPP) support.
  - Add support for Wi-Fi credentials library.
  - Add enterprise support for station.
  - Add Wi-Fi snippet support for networking samples.
  - Add build testing for various Wi-Fi config combinations.
  - Add regulatory domain support to Wi-Fi shell.
  - Add WPS support to Wi-Fi shell.
  - Add 802.11r connect command usage in Wi-Fi shell.
  - Add current PHY rate to hostap status message.
  - Allow user to reset Wi-Fi statistics in Wi-Fi shell.
  - Display RTS threshold in Wi-Fi shell.
  - Fix SSID array length size in scanning results.
  - Fix the “wifi ap config” command using the STA interface instead of SAP interface.
  - Fix memory leak in hostap when doing a disconnect.
  - Fix setting of frequency band both in AP and STA mode in Wi-Fi shell.
  - Fix correct channel scan range in Wi-Fi 6GHz.
  - Fix scan results printing in Wi-Fi shell.
  - Increase main and shell stack sizes for Wi-Fi shell sample.
  - Increase the maximum count of connected STA to 8 in Wi-Fi shell.
  - Relocate AP and STA Wi-Fi sample to samples/net/wifi directory.
  - Run Wi-Fi tests together with network tests.
  - Updated ESP32 Wi-Fi driver to reflect actual negotiated PHY mode.
  - Add ESP32-C2 Wi-Fi support.
  - Add ESP32 driver APSTA support.
  - Add NXP RW612 driver support.
  - Added nRF70 Wi-Fi driver.

## Networking

- 802.15.4:

  - Implemented support for beacons without association bit.
  - Implemented support for beacons payload.
  - Fixed a bug where LL address endianness was swapped twice when deciphering a frame.
  - Fixed missing context lock release when checking destination address.
  - Improved error logging in 6LoWPAN fragmentation.
  - Improved error logging in 802.15.4 management commands.
- ARP:

  - Fixed ARP probe verification during IPv4 address conflict detection.
- CoAP:

  - Added new API [`coap_rst_init()`](../doxygen/html/group__coap.md#ga9626781d73d18c1305f654ef4723e5db) to simplify creating RST replies.
  - Implemented replying with CoAP RST response for unknown queries in CoAP client.
  - Added support for runtime configuration of ACK random factor parameter.
  - Added support for No Response CoAP option.
  - Added a new sample demonstrating downloading a resource with GET request.
  - Fixed handling of received CoAP RST reply in CoAP client.
  - Fixed socket error reporting to the application in CoAP client.
  - Fixed handling of response retransmissions in CoAP client.
  - Fixed a bug where CoAP block numbers were limited to `uint8_t`.
  - Various fixes in the block transfer support in CoAP client.
  - Improved handling of truncated datagrams in CoAP client.
  - Improved thread safety of CoAP client.
  - Fixed missing `static` keyword in some internal functions.
  - Various other minor fixes in CoAP client.
- DHCPv4:

  - Added support for parsing multiple DNS servers received from DHCP server.
  - Added support for DNS Server option in DHCPv4 server.
  - Added support for Router option in DHCPv4 server.
  - Added support for application callback which allows to assign custom addresses
    in DHCPv4 server.
  - Fixed DNS server list allocation in DHCPv4 client.
  - Fixed a bug where system workqueue could be blocked indefinitely by DHCPv4 client.
- DHCPv6:

  - Fixed a bug where system workqueue could be blocked indefinitely by DHCPv6 client.
- DNS/mDNS/LLMNR:

  - Added support for collecting DNS statistics.
  - Added support for more error codes in [`zsock_gai_strerror()`](../doxygen/html/group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b).
  - Fixed handling of DNS responses encoded with capital letters.
  - Fixed DNS dispatcher operation on multiple network interfaces.
  - Fixed error being reported for mDNS queries with query count equal to 0.
  - Various other minor fixes in DNS/mDNS implementations.
- Ethernet:
- gPTP/PTP:

  - Fixed handling of second overflow/underflow.
  - Fixed PTP clock adjusting with offset.
- HTTP:

  - Added support for specifying response headers and response code by the application.
  - Added support for netusb in the HTTP server sample.
  - Added support for accessing HTTP request headers from the application callback.
  - Added support for handling IPv4 connections over IPv6 socket in HTTP server.
  - Added support for creating HTTP server instances without specifying local host.
  - Added overlays to support HTTP over IEEE 802.15.4 for HTTP client and server
    samples.
  - Added support for static filesystem resources in HTTP server.
  - Fixed assertion in HTTP server sample when resource upload was aborted.
  - Refactored dynamic resource callback format for easier handling of short
    requests/replies.
  - Fixed possible busy-looping in case of errors in the HTTP server sample.
  - Fixed possible incorrect HTTP headers matching in HTTP server.
  - Refactored HTTP server sample to better demonstrate server use cases.
  - Fixed processing of multiple HTTP/1 requests over the same connection.
  - Improved HTTP server test coverage.
  - Various other minor fixes in HTTP server.
- IPv4:

  - Improved IGMP test coverage.
  - Fixed IGMPv2 queries processing when IGMPv3 is enabled.
  - Fixed `CONFIG_NET_NATIVE_IPV4` dependency for native IPv4 options.
  - Fix net\_pkt leak in `send_ipv4_fragment()`.`
  - Fixed tx\_pkts slab leak in send\_ipv4\_fragment
- IPv6:

  - Added a public header for Multicast Listener Discovery APIs.
  - Added new [`net_ipv6_addr_prefix_mask()`](../doxygen/html/group__ip__4__6.md#ga4e91a4298604a916731bf591acc7b326) API function.
  - Made IPv6 Router Solicitation timeout configurable.
  - Fixed endless IPv6 packet looping with both routing and VLAN support enabled.
  - Fixed unneeded error logging in case of dropped NS packets.
  - Fixed accepting of incoming DAD NS messages.
  - Various fixes improving IPv6 routing.
  - Added onlink and forwarding check to IPv6-prepare
- LwM2M:

  - Location object: optional resources altitude, radius, and speed can now be
    used optionally as per the location object’s specification. Users of these
    resources will now need to provide a read buffer.
  - Added TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CCM\_8 to DTLS cipher list.
  - Added LwM2M shell command for listing resources.
  - Added LwM2M shell command to list observations.
  - Added support for accepting SenML-CBOR floats decoded as integers.
  - Added support for X509 hostname verification if using certificates, when
    URI contains valid name.
  - Regenerated generated code files using zcbor 0.9.0 for lwm2m\_senml\_cbor.
  - Improved thread safety of the LwM2M engine.
  - Fixed block transfer issues for composite operations.
  - Fixed enabler version reporting during bootstrap discovery.
  - Removed unneeded Security object instance from the LwM2M client sample.
  - Fixed buffer size check for U16 resource.
  - Removed deprecated APIs and configs.
  - Optional Location object resources altitude, radius, and speed can now be
    used optionally as per the location object’s specification. Users of these
    resources will now need to provide a read buffer.
  - Fixed the retry counter not being reset on successful Registration update.
  - Fixed REGISTRATION\_TIMEOUT event not always being emitted on registration
    errors.
  - Fixed c++ support in LwM2M public header.
  - Fixed a bug where DISCONNECTED event was not always emitted when needed.
- Misc:

  - Added support for network packet allocation statistics.
  - Added a new library implementing Prometheus monitoring support.
  - Added USB CDC NCM support for Echo Server sample.
  - Added packet drop statistics for capture interfaces.
  - Added new [`net_hostname_set_postfix_str()`](../doxygen/html/group__net__hostname.md#ga2b9d6f604afcde27b6d1543495e2ba8b) API function to set hostname
    postfix in non-hexadecimal format.
  - Added API version information to public networking headers.
  - Implemented optional periodic SNTP time resynchronization.
  - Improved error reporting when starting/stopping virtual interfaces.
  - Fixed build error of packet capture library when variable sized buffers are used.
  - Fixed build error of packet capture library when either IPv4 or IPv6 is disabled.
  - Fixed CMake complaint about missing sources in net library in certain
    configurations.
  - Fixed compilation issues with networking and SystemView Tracing enabled.
  - Removed redundant DHCPv4 code from telnet sample.
  - Fixed build warnings in Echo Client sample with IPv6 disabled.
  - Extended network tracing support and added documentation page
    ([Network Tracing](../connectivity/networking/network_tracing.md#network-tracing)).
  - Moved network buffers implementation out of net subsystem into lib directory
  - Removed `wpansub` sample.
- MQTT:

  - Updated information in the mqtt\_publisher sample about Mosquitto broker
    configuration.
  - Updated MQTT tests to be self-contained, no longer requiring external broker.
  - Optimized buffer handling in MQTT encoder/decoder.
- Network contexts:

  - Fixed IPv4 destination address setting when using [`sendmsg()`](../doxygen/html/group__bsd__sockets.md#ga1d7ee25c28352b2e7af55f75d721c4b8) with
    [`CONFIG_NET_IPV4_MAPPING_TO_IPV6`](../kconfig.md#CONFIG_NET_IPV4_MAPPING_TO_IPV6 "CONFIG_NET_IPV4_MAPPING_TO_IPV6") option enabled.
  - Fixed possible unaligned memory access when in [`net_context_bind()`](../doxygen/html/group__net__context.md#ga0fb749331a4f21148ca5a7f364f241b9).
  - Fixed missing NULL pointer check for V6ONLY option read.
- Network Interface:

  - Added new [`net_if_ipv4_get_gw()`](../doxygen/html/group__net__if.md#gae42f6f9620e40e2d2b36d30e81bb82d9) API function.
  - Fixed checksum offloading checks for VLAN interfaces.
  - Fixed native IP support being required to register IP addresses on an
    interface.
  - Fixed missing mutex locks in a few net\_if functions.
  - Fixed rejoining of IPv6 multicast groups.
  - Fixed [`net_if_send_data()`](../doxygen/html/group__net__if.md#gada0398d757eab28d16a129692c309f4d) operation for offloaded interfaces.
  - Fixed needless IPv6 multicast groups joining if IPv6 is disabled.
  - Fixed compiler warnings when building with `-Wtype-limits`.
- OpenThread:

  - Added support for [`CONFIG_IEEE802154_SELECTIVE_TXCHANNEL`](../kconfig.md#CONFIG_IEEE802154_SELECTIVE_TXCHANNEL "CONFIG_IEEE802154_SELECTIVE_TXCHANNEL")
    option in OpenThread radio platform.
  - Added NAT64 send and receive callbacks.
  - Added new Kconfig options:

    - [`CONFIG_OPENTHREAD_NAT64_CIDR`](../kconfig.md#CONFIG_OPENTHREAD_NAT64_CIDR "CONFIG_OPENTHREAD_NAT64_CIDR")
    - [`CONFIG_OPENTHREAD_STORE_FRAME_COUNTER_AHEAD`](../kconfig.md#CONFIG_OPENTHREAD_STORE_FRAME_COUNTER_AHEAD "CONFIG_OPENTHREAD_STORE_FRAME_COUNTER_AHEAD")
    - [`CONFIG_OPENTHREAD_DEFAULT_RX_SENSITIVITY`](../kconfig.md#CONFIG_OPENTHREAD_DEFAULT_RX_SENSITIVITY "CONFIG_OPENTHREAD_DEFAULT_RX_SENSITIVITY")
    - [`CONFIG_OPENTHREAD_CSL_REQUEST_TIME_AHEAD`](../kconfig.md#CONFIG_OPENTHREAD_CSL_REQUEST_TIME_AHEAD "CONFIG_OPENTHREAD_CSL_REQUEST_TIME_AHEAD")
  - Fixed deprecated/preferred IPv6 address state transitions.
  - Fixed handling of deprecated IPv6 addresses.
  - Other various minor fixes in Zephyr’s OpenThread port.
- Shell:

  - Added support for enabling/disabling individual network shell commands with
    Kconfig.
  - Added new `net dhcpv4/6 client` commands for DHCPv4/6 client management.
  - Added new `net virtual` commands for virtual interface management.
  - `net ipv4/6` commands are now available even if native IP stack is disabled.
  - Added new `net cm` commands exposing Connection Manager functionality.
  - Fixed possible assertion if telnet shell backend connection is terminated.
  - Event monitor thread stack size is now configurable with Kconfig.
  - Relocated `bridge` command under `net` command, i. e. `net bridge`.
  - Multiple minor improvements in various command outputs.
- Sockets:

  - Added dedicated `net_socket_service_handler_t` callback function type for
    socket services.
  - Added TLS 1.3 support for TLS sockets.
  - Fixed socket leak when closing NSOS socket.
  - Moved socket service library out of experimental.
  - Deprecated `CONFIG_NET_SOCKETS_POLL_MAX`.
  - Moved `zsock_poll()` and `zsock_select` implementations into `zvfs`
    library.
  - Removed `work_q` parameter from socket service macros as it was no longer
    used.
  - Separated native INET sockets implementation from socket syscalls so that
    it doesn’t have to be built when offloaded sockets are used.
  - Fixed possible infinite block inside TLS socket [`zsock_connect()`](../doxygen/html/group__bsd__sockets.md#ga1a70b1d3616341a86977835cc853d81d) when
    peer goes down silently.
  - Fixed `msg_controllen` not being set correctly in [`zsock_recvmsg()`](../doxygen/html/group__bsd__sockets.md#gac8d659bad72d651265c8cd0b69e678c0).
  - Fixed possible busy-looping when polling TLS socket for POLLOUT event.
- TCP:

  - Fixed propagating connection errors to the socket layer.
  - Improved ACK reply logic when peer does not send PSH flag with data.
- Websocket:

  - Added support for Websocket console in the Echo Server sample.
  - Fixed undefined reference to `MSG_DONTWAIT` while building websockets
    without POSIX.
- Wi-Fi:

  - Add a 80211R fast BSS transition argument usage to the wifi shell’s connect command.
  - Fixed the shell’s ap config command using the sta interface area
  - Added AP configuration cmd support to the NXP Wifi drivers
  - Fixed the dormant state in the NXP WiFi driver to be set to off once a connection to an AP is achieved
- zperf:

  - Added support for USB CDC NCM in the zperf sample.
  - Fixed DHCPv4 client not being started in the zperf sample in certain
    configurations.

## USB

- New USB device stack:

  - Added USB CDC Network Control Model implementation
  - Enhanced USB Audio class 2 implementation
  - Made USB device stack high-bandwidth aware
  - Enhanced CDC ACM and HID class implementations

## Devicetree

- Added support for string-array and array type properties to be enums.
  Many new macros added for this, for example [`DT_ENUM_IDX_BY_IDX`](../doxygen/html/group__devicetree-generic-prop.md#gae2e5f62d8f0c1eefcbb60ec7a5e84be2).
- Added [`DT_ANY_COMPAT_HAS_PROP_STATUS_OKAY`](../doxygen/html/group__devicetree-inst.md#ga052727464d4f04768eaa71b7522c9a61).
- Added [`DT_NODE_HAS_STATUS_OKAY`](../doxygen/html/group__devicetree-generic-exist.md#gaed773a8782fe00db90e8599ff673e8ed).
- Added [`DT_INST_NUM_IRQS`](../doxygen/html/group__devicetree-inst.md#ga446d4b9c267e7c9da73dfb8a07701f2a).
- Added macros [`DT_NODE_FULL_NAME_UNQUOTED`](../doxygen/html/group__devicetree-generic-id.md#ga8832fb6fa0e0555884621d210440fdcd), [`DT_NODE_FULL_NAME_TOKEN`](../doxygen/html/group__devicetree-generic-id.md#gad24b51e728175e7d347407f2131a3850),
  and [`DT_NODE_FULL_NAME_UPPER_TOKEN`](../doxygen/html/group__devicetree-generic-id.md#gab966ae50efe46cc3a54f086f508edb3b).
- `DT_*_REG_ADDR` now returns an explicit unsigned value with C’s `U` suffix.
- Fixed escaping of double quotes, backslashes, and new line characters from DTS
  so that they can be used in string properties.
- Renamed `power-domain` base property to `power-domains`,
  and introduced `power-domain-names` property. `#power-domain-cells` is now required as well.
- Moved the NXP Remote Domain Controller property to its own schema file

## Kconfig

## Libraries / Subsystems

- Debug

  > - Added west runner for probe-rs, a Rust-based embedded toolkit.
- Demand Paging

  - Added LRU (Least Recently Used) eviction algorithm.
  - Added on-demand memory mapping support ([`CONFIG_DEMAND_MAPPING`](../kconfig.md#CONFIG_DEMAND_MAPPING "CONFIG_DEMAND_MAPPING")).
  - Made demand paging SMP compatible.
- Management

  - MCUmgr

    - Added support for [Enumeration Management Group](../services/device_mgmt/smp_groups/smp_group_10.md#mcumgr-smp-group-10), which allows for listing information on
      supported groups.
    - Fixed formatting of milliseconds in `OS_MGMT_ID_DATETIME_STR` by adding
      leading zeros.
    - Added support for custom os mgmt bootloader info responses using notification hooks, this
      can be enabled with [`CONFIG_MCUMGR_GRP_OS_BOOTLOADER_INFO_HOOK`](../kconfig.md#CONFIG_MCUMGR_GRP_OS_BOOTLOADER_INFO_HOOK "CONFIG_MCUMGR_GRP_OS_BOOTLOADER_INFO_HOOK"), the data
      structure is [`os_mgmt_bootloader_info_data`](../doxygen/html/structos__mgmt__bootloader__info__data.md).
    - Added support for img mgmt slot info command, which allows for listing information on
      images and slots on the device.
    - Added support for LoRaWAN MCUmgr transport, which can be enabled with
      [`CONFIG_MCUMGR_TRANSPORT_LORAWAN`](../kconfig.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN "CONFIG_MCUMGR_TRANSPORT_LORAWAN").
  - hawkBit

    - [`hawkbit_autohandler()`](../doxygen/html/group__hawkbit__autohandler.md#ga41865255aa3020a34816c23ae7977f20) now takes one argument. If the argument is set to true, the
      autohandler will reshedule itself after running. If the argument is set to false, the
      autohandler will not reshedule itself. Both variants are scheduled independent of each other.
      The autohandler always runs in the system workqueue.
    - Use the [`hawkbit_autohandler_wait()`](../doxygen/html/group__hawkbit__autohandler.md#ga6d13b3d7b9a61d06a6eaa346189a08c6) function to wait for the autohandler to finish.
    - Running hawkBit from the shell is now executed in the system workqueue.
    - Use the [`hawkbit_autohandler_cancel()`](../doxygen/html/group__hawkbit__autohandler.md#gabc27308bb974d6e0b9650476243e5e9a) function to cancel the autohandler.
    - Use the [`hawkbit_autohandler_set_delay()`](../doxygen/html/group__hawkbit__autohandler.md#ga47fe3e9cd227fd4da332e9eeff81f991) function to delay the next run of the
      autohandler.
    - The hawkBit header file was separated into multiple header files. The main header file is now
      `<zephyr/mgmt/hawkbit/hawkbit.h>`, the autohandler header file is now
      `<zephyr/mgmt/hawkbit/autohandler.h>` and the configuration header file is now
      `<zephyr/mgmt/hawkbit/config.h>`.
- Power management

  - Added initial ESP32-C6 power management interface to allow light and deep-sleep features.
- Crypto

  - Mbed TLS was updated to version 3.6.2 (from 3.6.0). The release notes can be found at:

    - [https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.1](https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.1)
    - [https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.2](https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.2)
  - The Kconfig symbol [`CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG_ALLOW_NON_CSPRNG`](../kconfig.md#CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG_ALLOW_NON_CSPRNG "CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG_ALLOW_NON_CSPRNG")
    was added to allow `psa_get_random()` to make use of non-cryptographically
    secure random sources when [`CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG`](../kconfig.md#CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG "CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG")
    is also enabled. This is only meant to be used for test purposes, not in production.
    ([GitHub #76408](https://github.com/zephyrproject-rtos/zephyr/issues/76408))
  - The Kconfig symbol [`CONFIG_MBEDTLS_TLS_VERSION_1_3`](../kconfig.md#CONFIG_MBEDTLS_TLS_VERSION_1_3 "CONFIG_MBEDTLS_TLS_VERSION_1_3") was added to
    enable TLS 1.3 support from Mbed TLS. When this is enabled the following
    new Kconfig symbols can also be enabled:

    - [`CONFIG_MBEDTLS_TLS_SESSION_TICKETS`](../kconfig.md#CONFIG_MBEDTLS_TLS_SESSION_TICKETS "CONFIG_MBEDTLS_TLS_SESSION_TICKETS") to enable session tickets
      (RFC 5077);
    - [`CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_ENABLED`](../kconfig.md#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_ENABLED "CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_ENABLED")
      for TLS 1.3 PSK key exchange mode;
    - [`CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED`](../kconfig.md#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED "CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED")
      for TLS 1.3 ephemeral key exchange mode;
    - [`CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_EPHEMERAL_ENABLED`](../kconfig.md#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_EPHEMERAL_ENABLED "CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_EPHEMERAL_ENABLED")
      for TLS 1.3 PSK ephemeral key exchange mode.
- SD

  - No significant changes in this release
- Settings

  - Settings has been extended to allow prioritizing the commit handlers using
    `SETTINGS_STATIC_HANDLER_DEFINE_WITH_CPRIO(...)` for static\_handlers and
    `settings_register_with_cprio(...)` for dynamic\_handlers.
- Shell:

  - Reorganized the `kernel threads` and `kernel stacks` shell command under the
    L1 `kernel thread` shell command as `kernel thread list` & `kernel thread stacks`
  - Added multiple shell command to configure the CPU mask affinity / pinning a thread in
    runtime, do `kernel thread -h` for more info.
  - `kernel reboot` shell command without any additional arguments will now do a cold reboot
    instead of requiring you to type `kernel reboot cold`.
- Storage

  - LittleFS: The module has been updated with changes committed upstream
    from version 2.8.1, the last module update, up to and including
    the released version 2.9.3.
  - Fixed static analysis error caused by mismatched variable assignment in NVS
  - LittleFS: Fixed an issue where the DTS option for configuring block cycles for LittleFS instances
    was ignored ([GitHub #79072](https://github.com/zephyrproject-rtos/zephyr/issues/79072)).
  - LittleFS: Fixed issue with lookahead buffer size mismatch to actual allocated buffer size
    ([GitHub #77917](https://github.com/zephyrproject-rtos/zephyr/issues/77917)).
  - FAT FS: Added [`CONFIG_FILE_SYSTEM_LIB_LINK`](../kconfig.md#CONFIG_FILE_SYSTEM_LIB_LINK "CONFIG_FILE_SYSTEM_LIB_LINK") to allow linking file system
    support libraries without enabling the File System subsystem. This option can be used
    when a user wants to directly use file system libraries, bypassing the File System
    subsystem.
  - FAT FS: Added [`CONFIG_FS_FATFS_LBA64`](../kconfig.md#CONFIG_FS_FATFS_LBA64 "CONFIG_FS_FATFS_LBA64") to enable support for the 64-bit LBA
    and GPT in FAT file system driver.
  - FAT FS: Added [`CONFIG_FS_FATFS_MULTI_PARTITION`](../kconfig.md#CONFIG_FS_FATFS_MULTI_PARTITION "CONFIG_FS_FATFS_MULTI_PARTITION") that enables support for
    devices partitioned with GPT or MBR.
  - FAT FS: Added [`CONFIG_FS_FATFS_HAS_RTC`](../kconfig.md#CONFIG_FS_FATFS_HAS_RTC "CONFIG_FS_FATFS_HAS_RTC") that enables RTC usage for time-stamping
    files on FAT file systems.
  - FAT FS: Added [`CONFIG_FS_FATFS_EXTRA_NATIVE_API`](../kconfig.md#CONFIG_FS_FATFS_EXTRA_NATIVE_API "CONFIG_FS_FATFS_EXTRA_NATIVE_API") that enables additional FAT
    file system driver functions, which are not exposed via Zephyr File System subsystem,
    for users that intend to directly call them in their code.
  - Stream Flash: Fixed an issue where [`stream_flash_erase_page()`](../doxygen/html/group__stream__flash.md#ga75711b22789724c2d8629e1202dcb48d) did not properly check
    the requested erase range and possibly allowed erasing any page on a device ([GitHub #79800](https://github.com/zephyrproject-rtos/zephyr/issues/79800)).
  - Shell: Fixed an issue were a failed file system mount attempt using the shell would make it
    impossible to ever succeed in mounting that file system again until the device was reset ([GitHub #80024](https://github.com/zephyrproject-rtos/zephyr/issues/80024)).
  - [ZMS](../services/storage/zms/zms.md#zms-api): Introduction of a new storage system that is designed to work with all types of
    non-volatile storage technologies. It supports classical on-chip NOR flash as well as
    new technologies like RRAM and MRAM that do not require a separate erase operation at all.
- Task Watchdog
- Tracing

  - Added support for a “user event” trace, with the purpose to allow driver or
    application developers to quickly add tracing for events for debug purposes
- POSIX API

  - Added support for the following Option Groups:

    - [POSIX\_DEVICE\_IO](../services/portability/posix/option_groups/index.md#posix-option-group-device-io)
    - [POSIX\_SIGNALS](../services/portability/posix/option_groups/index.md#posix-option-group-signals)
  - Added support for the following Options:

    - [\_POSIX\_SYNCHRONIZED\_IO](../services/portability/posix/option_groups/index.md#posix-option-synchronized-io)
    - [\_POSIX\_THREAD\_PRIO\_PROTECT](../services/portability/posix/option_groups/index.md#posix-option-thread-prio-protect)
  - [POSIX\_FILE\_SYSTEM](../services/portability/posix/option_groups/index.md#posix-option-group-file-system) improvements:

    - Support for [`O_TRUNC`](../doxygen/html/fcntl_8h.md#ad1d67e453fb3031f40f8cd3403773813) flag in [`open()`](../doxygen/html/fcntl_8h.md#ac843f2e35e60c3bbf1da47d84306f29b).
    - Support for `rmdir()` and [`remove()`](../doxygen/html/stdio_8h.md#a32e4cef9beb0262cea4bdafb5b998276).
  - [\_POSIX\_THREAD\_SAFE\_FUNCTIONS](../services/portability/posix/option_groups/index.md#posix-option-thread-safe-functions) improvements:

    - Support for [`asctime_r()`](../doxygen/html/lib_2libc_2minimal_2include_2time_8h.md#a86ed062bf74f495209b11b650631e2f2), [`ctime_r()`](../doxygen/html/lib_2libc_2minimal_2include_2time_8h.md#abb5334ac0f38a87278861e6edab616db), and [`localtime_r()`](../doxygen/html/lib_2libc_2minimal_2include_2time_8h.md#a3d8015c8bf5fadc92389635bd977e880).
  - [POSIX\_THREADS\_BASE](../services/portability/posix/option_groups/index.md#posix-option-group-threads-base) improvements:

    - Use the [user mode semaphore API](../kernel/services/synchronization/semaphores.md#semaphores-v2) instead of the
      [spinlock API](../kernel/services/smp/smp.md#smp-arch) for pool synchronization.
- LoRa/LoRaWAN
- ZBus
- JWT (JSON Web Token)

  - The following new symbols were added to allow specifying both the signature
    algorithm and crypto library:

    - [`CONFIG_JWT_SIGN_RSA_PSA`](../kconfig.md#CONFIG_JWT_SIGN_RSA_PSA "CONFIG_JWT_SIGN_RSA_PSA") (default) RSA signature using the PSA Crypto API;
    - [`CONFIG_JWT_SIGN_RSA_LEGACY`](../kconfig.md#CONFIG_JWT_SIGN_RSA_LEGACY "CONFIG_JWT_SIGN_RSA_LEGACY") RSA signature using Mbed TLS;
    - [`CONFIG_JWT_SIGN_ECDSA_PSA`](../kconfig.md#CONFIG_JWT_SIGN_ECDSA_PSA "CONFIG_JWT_SIGN_ECDSA_PSA") ECDSA signature using the PSA Crypto API.

    ([GitHub #79653](https://github.com/zephyrproject-rtos/zephyr/issues/79653))
- Firmware

  - Introduced basic support for ARM’s System Control and Management Interface, which includes:

    - Subset of clock management protocol commands
    - Subset of pin control protocol commands
    - Shared memory and mailbox-based transport

## HALs

- Nordic

  - Updated nrfx to version 3.7.0.
  - Added OS agnostic parts of the nRF70 Wi-Fi driver.
- STM32

  - Updated STM32C0 to cube version V1.2.0.
  - Updated STM32F1 to cube version V1.8.6.
  - Updated STM32F2 to cube version V1.9.5.
  - Updated STM32F4 to cube version V1.28.1.
  - Updated STM32G4 to cube version V1.6.0.
  - Updated STM32H5 to cube version V1.3.0.
  - Updated STM32H7 to cube version V1.11.2.
  - Updated STM32H7RS to cube version V1.1.0.
  - Added STM32U0 Cube package (1.1.0)
  - Updated STM32U5 to cube version V1.6.0.
  - Updated STM32WB to cube version V1.20.0.
  - Added STM32WB0 Cube package (1.0.0)
  - Updated STM32WBA to cube version V1.4.1.
- ADI
- Espressif

  - Synced HAL to version v5.1.4 to update SoCs low level files, RF libraries and
    overall driver support.
- NXP

  > - Updated the MCUX HAL to the SDK version 2.16.000
  > - Updated the NXP S32ZE HAL drivers to version 2.0.0
- Silabs

  - Updated Series 2 to Simplicity SDK 2024.6, while Series 0/1 continue to use Gecko SDK 4.4.

## MCUboot

> - Removed broken target config header feature.
> - Removed `image_index` from `boot_encrypt`.
> - Renamed boot\_enc\_decrypt to boot\_decrypt\_key.
> - Updated to use `EXTRA_CONF_FILE` instead of the deprecated `OVERLAY_CONFIG` argument.
> - Updated `boot_encrypt()` to instead be `boot_enc_encrypt()` and `boot_enc_decrypt()`.
> - Updated `boot_enc_valid` to take slot instead of image index.
> - Updated `boot_enc_load()` to take slot number instead of image.
> - Updated logging to debug level in boot\_serial.
> - Updated Kconfig to allow disabling NRFX\_WDT on nRF devices.
> - Updated CMake ERROR statements into FATAL\_ERROR.
> - Added application version that is being booted output prior to booting it.
> - Added sysbuild support to the hello-world sample.
> - Added SIG\_PURE TLV to bootutil.
> - Added write block size checking to bootutil.
> - Added check for unexpected flash sector size.
> - Added SHA512 support to MCUboot code and support for calculating SHA512 hash in imgtool.
> - Added fallback to USB DFU option.
> - Added better mode selection checks to bootutil.
> - Added bootutil protected TLV size to image size check.
> - Added functionality to remove images with conflicting flags or where features are required
>   that are not supported.
> - Added compressed image flags and TLVs to MCUboot, Kconfig options and support for generating
>   compressed LZMA2 images with ARM thumb filter to imgtool.
> - Added image header verification before checking image.
> - Added state to `boot_is_header_valid()` function.
> - Added `CONFIG_MCUBOOT_ENC_BUILTIN_KEY` Kconfig option.
> - Added non-bootable flag to imgtool.
> - Added zephyr prefix to generated header path.
> - Added optional img mgmt slot info feature.
> - Added bootutil support for maximum image size details for additional images.
> - Added support for automatically calculating max sectors.
> - Added missing `boot_enc_init()` function.
> - Added support for keeping image encrypted in scratch area in bootutil.
> - Fixed serial recovery for NXP IMX.RT, LPC55x and MCXNx platforms
> - Fixed issue with public RSA signing in imgtool.
> - Fixed issue with `boot_serial_enter()` being defined but not used warning.
> - Fixed issue with `main()` in sample returning wrong type warning.
> - Fixed issue with using pointers in bootutil.
> - Fixed wrong usage of slot numbers in boot\_serial.
> - Fixed slot info for directXIP/RAM load in bootutil.
> - Fixed bootutil issue with not zeroing AES and SHA-256 contexts with mbedTLS.
> - Fixed boot\_serial `format` and `incompatible-pointer-types` warnings.
> - Fixed bootutil wrong definition of `find_swap_count`.
> - Fixed bootutil swap move max app size calculation.
> - Fixed imgtool issue where getpub failed for ed25519 key.
> - Fixed issue with sysbuild if something else is named mcuboot.
> - Fixed RAM load chain load address.
> - Fixed issue with properly retrieving image headers after interrupted swap-scratch in bootutil.
> - The MCUboot version in this release is version `2.1.0+0-dev`.
> - Add the following nxp boards as test targets area: `frdm_ke17z`, `frdm_ke17z512`,
>   `rddrone_fmuk66`, `twr_ke18f`, `frdm_mcxn947/mcxn947/cpu0`

## OSDP

## Trusted Firmware-M (TF-M)

- TF-M was updated to version 2.1.1 (from 2.1.0).
  The release notes can be found at: [https://trustedfirmware-m.readthedocs.io/en/tf-mv2.1.1/releases/2.1.1.html](https://trustedfirmware-m.readthedocs.io/en/tf-mv2.1.1/releases/2.1.1.html)

## Nanopb

- Updated the nanopb module to version 0.4.9.
  Full release notes at [https://github.com/nanopb/nanopb/blob/0.4.9/CHANGELOG.txt](https://github.com/nanopb/nanopb/blob/0.4.9/CHANGELOG.txt)

## LVGL

- Added definition of `LV_ATTRIBUTE_MEM_ALIGN` so library internal data structures can be aligned
  to a specific boundary.
- Provided alignment definition to accommodate the alignment requirement of some GPU’s

## zcbor

- Updated the zcbor library to version 0.9.0.
  Full release notes at [https://github.com/NordicSemiconductor/zcbor/blob/0.9.0/RELEASE\_NOTES.md](https://github.com/NordicSemiconductor/zcbor/blob/0.9.0/RELEASE_NOTES.md)
  Migration guide at [https://github.com/NordicSemiconductor/zcbor/blob/0.9.0/MIGRATION\_GUIDE.md](https://github.com/NordicSemiconductor/zcbor/blob/0.9.0/MIGRATION_GUIDE.md)
  Highlights:

  > - Many code generation bugfixes
  > - You can now decide at run-time whether the decoder should enforce canonical encoding.
  > - Allow –file-header to accept a path to a file with header contents

## Tests and Samples

- Together with the deprecation of [native\_posix](../boards/native/native_posix/doc/index.md#native-posix), many tests which were
  explicitly run in native\_posix now run in [native\_sim](../boards/native/native_sim/doc/index.md#native-sim) instead.
  native\_posix as a platform remains tested though.
- Extended the tests of counter\_basic\_api with a testcase for counters without alarms
- Added support for testing SDMMC devices to the fatfs API test
- Extended net/vlan to add IPv6 prefix config to each vlan-iface
- Enhanced the camera fixture test by adding a color bar to enable automation
- Added a number crunching (maths such as FFT, echo cancellation) sample using an optimized
  library for the NXP ADSP board
- Tailored the SPI\_LOOPBACK test to the limitations of NXP Kinetis MCU’s
- Enabled the video sample to run video capture (samples/drivers/video)
- Added [SMF Calculator](../samples/subsys/smf/smf_calculator/README.md#smf_calculator "Create a simple desk calculator using the State Machine Framework.") sample demonstrating the usage of the State Machine framework
  in combination with LVGL to create a simple calculator application.
- Consolidated display sample where possible to use a single testcase for all shields

## Issue Related Items

### Known Issues

- [GitHub #71042](https://github.com/zephyrproject-rtos/zephyr/issues/71042) stream\_flash: stream\_flash\_init() size parameter allows to ignore partition layout
- [GitHub #67407](https://github.com/zephyrproject-rtos/zephyr/issues/67407) stream\_flash: stream\_flash\_erase\_page allows to accidentally erase stream
- [GitHub #80875](https://github.com/zephyrproject-rtos/zephyr/issues/80875) stepper\_api: incorrect c-prototype stepper.h and absence of NULL check stepper\_shell.c
