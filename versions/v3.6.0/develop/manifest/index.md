---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/manifest/index.html
original_path: develop/manifest/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# West Projects index

See [Contributing External Components](../../contribute/external.md#external-contributions) for more information about
this contributing and review process for imported components.

## Active Projects/Modules

The projects below are enabled by default and will be downloaded when you
call west update. Many of the projects or modules listed below are
essential for building generic Zephyr application and include among others
hardware support for many of the platforms available in Zephyr.

To disable any of the active modules, for example a specific HAL, use the
following commands:

```text
west config manifest.project-filter -- -hal_FOO
west update
```

| Project | Revision |
| --- | --- |
| acpica | [da5f2721e1c7f188fe04aa50af76f4b94f3c3ea3](https://github.com/zephyrproject-rtos/acpica/commit/da5f2721e1c7f188fe04aa50af76f4b94f3c3ea3) |
| cmsis | [4b96cbb174678dcd3ca86e11e1f24bc5f8726da0](https://github.com/zephyrproject-rtos/cmsis/commit/4b96cbb174678dcd3ca86e11e1f24bc5f8726da0) |
| cmsis-dsp | [6489e771e9c405f1763b52d64a3f17a1ec488ace](https://github.com/zephyrproject-rtos/cmsis-dsp/commit/6489e771e9c405f1763b52d64a3f17a1ec488ace) |
| cmsis-nn | [0c8669d81381ccf3b1a01d699f3b68b50134a99f](https://github.com/zephyrproject-rtos/cmsis-nn/commit/0c8669d81381ccf3b1a01d699f3b68b50134a99f) |
| edtt | [64e5105ad82390164fb73fc654be3f73a608209a](https://github.com/zephyrproject-rtos/edtt/commit/64e5105ad82390164fb73fc654be3f73a608209a) |
| fatfs | [427159bf95ea49b7680facffaa29ad506b42709b](https://github.com/zephyrproject-rtos/fatfs/commit/427159bf95ea49b7680facffaa29ad506b42709b) |
| hal\_altera | [0d225ddd314379b32355a00fb669eacf911e750d](https://github.com/zephyrproject-rtos/hal_altera/commit/0d225ddd314379b32355a00fb669eacf911e750d) |
| hal\_ambiq | [ff4ca358d730536addf336c40c3faa4ebf1df00a](https://github.com/zephyrproject-rtos/hal_ambiq/commit/ff4ca358d730536addf336c40c3faa4ebf1df00a) |
| hal\_atmel | [aad79bf530b69b72712d18873df4120ad052d921](https://github.com/zephyrproject-rtos/hal_atmel/commit/aad79bf530b69b72712d18873df4120ad052d921) |
| hal\_espressif | [67fa60bdffca7ba8ed199aecfaa26f485f24878b](https://github.com/zephyrproject-rtos/hal_espressif/commit/67fa60bdffca7ba8ed199aecfaa26f485f24878b) |
| hal\_ethos\_u | [90ada2ea5681b2a2722a10d2898eac34c2510791](https://github.com/zephyrproject-rtos/hal_ethos_u/commit/90ada2ea5681b2a2722a10d2898eac34c2510791) |
| hal\_gigadevice | [2994b7dde8b0b0fa9b9c0ccb13474b6a486cddc3](https://github.com/zephyrproject-rtos/hal_gigadevice/commit/2994b7dde8b0b0fa9b9c0ccb13474b6a486cddc3) |
| hal\_infineon | [69c883d3bd9fac8a18dd8384624b8c472a68d06f](https://github.com/zephyrproject-rtos/hal_infineon/commit/69c883d3bd9fac8a18dd8384624b8c472a68d06f) |
| hal\_intel | [7b4c25669f1513b0d6d6ee78ee42340d91958884](https://github.com/zephyrproject-rtos/hal_intel/commit/7b4c25669f1513b0d6d6ee78ee42340d91958884) |
| hal\_microchip | [5d079f1683a00b801373bbbbf5d181d4e33b30d5](https://github.com/zephyrproject-rtos/hal_microchip/commit/5d079f1683a00b801373bbbbf5d181d4e33b30d5) |
| hal\_nordic | [dce8519f7da37b0a745237679fd3f88250b495ff](https://github.com/zephyrproject-rtos/hal_nordic/commit/dce8519f7da37b0a745237679fd3f88250b495ff) |
| hal\_nuvoton | [68a91bb343ff47e40dbd9189a7d6e3ee801a7135](https://github.com/zephyrproject-rtos/hal_nuvoton/commit/68a91bb343ff47e40dbd9189a7d6e3ee801a7135) |
| hal\_nxp | [d45b14c198d778658b7853b48378d2e132a6c4be](https://github.com/zephyrproject-rtos/hal_nxp/commit/d45b14c198d778658b7853b48378d2e132a6c4be) |
| hal\_openisa | [eabd530a64d71de91d907bad257cd61aacf607bc](https://github.com/zephyrproject-rtos/hal_openisa/commit/eabd530a64d71de91d907bad257cd61aacf607bc) |
| hal\_quicklogic | [b3a66fe6d04d87fd1533a5c8de51d0599fcd08d0](https://github.com/zephyrproject-rtos/hal_quicklogic/commit/b3a66fe6d04d87fd1533a5c8de51d0599fcd08d0) |
| hal\_renesas | [0b1f2fdb99d6386f125a8dba72083e3c56aecc2b](https://github.com/zephyrproject-rtos/hal_renesas/commit/0b1f2fdb99d6386f125a8dba72083e3c56aecc2b) |
| hal\_rpi\_pico | [fba7162cc7bee06d0149622bbcaac4e41062d368](https://github.com/zephyrproject-rtos/hal_rpi_pico/commit/fba7162cc7bee06d0149622bbcaac4e41062d368) |
| hal\_silabs | [b11b29167f3f9a0fd0c34a8eeeb36b0c1d218917](https://github.com/zephyrproject-rtos/hal_silabs/commit/b11b29167f3f9a0fd0c34a8eeeb36b0c1d218917) |
| hal\_st | [0643d20ae85b32c658ad11036f7c964a860ddefe](https://github.com/zephyrproject-rtos/hal_st/commit/0643d20ae85b32c658ad11036f7c964a860ddefe) |
| hal\_stm32 | [60c9634f61c697e1c310ec648d33529712806069](https://github.com/zephyrproject-rtos/hal_stm32/commit/60c9634f61c697e1c310ec648d33529712806069) |
| hal\_telink | [38573af589173259801ae6c2b34b7d4c9e626746](https://github.com/zephyrproject-rtos/hal_telink/commit/38573af589173259801ae6c2b34b7d4c9e626746) |
| hal\_ti | [b85f86e51fc4d47c4c383d320d64d52d4d371ae4](https://github.com/zephyrproject-rtos/hal_ti/commit/b85f86e51fc4d47c4c383d320d64d52d4d371ae4) |
| hal\_wurthelektronik | [e5bcb2eac1bb9639ce13b4dafc78eb254e014342](https://github.com/zephyrproject-rtos/hal_wurthelektronik/commit/e5bcb2eac1bb9639ce13b4dafc78eb254e014342) |
| hal\_xtensa | [08325d6fb7190a105f5382d35e64ed2812c57cf4](https://github.com/zephyrproject-rtos/hal_xtensa/commit/08325d6fb7190a105f5382d35e64ed2812c57cf4) |
| hostap | [dee924caf7218d0ee2c2698c217559b1292a46d0](https://github.com/zephyrproject-rtos/hostap/commit/dee924caf7218d0ee2c2698c217559b1292a46d0) |
| libmetal | [243eed541b9c211a2ce8841c788e62ddce84425e](https://github.com/zephyrproject-rtos/libmetal/commit/243eed541b9c211a2ce8841c788e62ddce84425e) |
| liblc3 | [1a5938ebaca4f13fe79ce074f5dee079783aa29f](https://github.com/zephyrproject-rtos/liblc3/commit/1a5938ebaca4f13fe79ce074f5dee079783aa29f) |
| littlefs | [408c16a909dd6cf128874a76f21c793798c9e423](https://github.com/zephyrproject-rtos/littlefs/commit/408c16a909dd6cf128874a76f21c793798c9e423) |
| loramac-node | [842413c5fb98707eb5f26e619e8e792453877897](https://github.com/zephyrproject-rtos/loramac-node/commit/842413c5fb98707eb5f26e619e8e792453877897) |
| lvgl | [2b76c641749725ac90c6ac7959ca7718804cf356](https://github.com/zephyrproject-rtos/lvgl/commit/2b76c641749725ac90c6ac7959ca7718804cf356) |
| mbedtls | [6ec4abdcda78dfc47315af568f93e5ad4398dea0](https://github.com/zephyrproject-rtos/mbedtls/commit/6ec4abdcda78dfc47315af568f93e5ad4398dea0) |
| mcuboot | [a4eda30f5b0cfd0cf15512be9dcd559239dbfc91](https://github.com/zephyrproject-rtos/mcuboot/commit/a4eda30f5b0cfd0cf15512be9dcd559239dbfc91) |
| mipi-sys-t | [a819419603a2dfcb47f7f39092e1bc112e45d1ef](https://github.com/zephyrproject-rtos/mipi-sys-t/commit/a819419603a2dfcb47f7f39092e1bc112e45d1ef) |
| net-tools | [3a677d355cc7f73e444801a6280d0ccec80a1957](https://github.com/zephyrproject-rtos/net-tools/commit/3a677d355cc7f73e444801a6280d0ccec80a1957) |
| nrf\_hw\_models | [52d0b4b7b7431d8da6222cc3b17a8afdcb099baf](https://github.com/zephyrproject-rtos/nrf_hw_models/commit/52d0b4b7b7431d8da6222cc3b17a8afdcb099baf) |
| open-amp | [da78aea63159771956fe0c9263f2e6985b66e9d5](https://github.com/zephyrproject-rtos/open-amp/commit/da78aea63159771956fe0c9263f2e6985b66e9d5) |
| openthread | [7761b81d23b10b3d5ee21b8504c67535cde10896](https://github.com/zephyrproject-rtos/openthread/commit/7761b81d23b10b3d5ee21b8504c67535cde10896) |
| percepio | [0fbc5b72aeab8a6434523a3a7bc8111c17f0bc73](https://github.com/zephyrproject-rtos/percepio/commit/0fbc5b72aeab8a6434523a3a7bc8111c17f0bc73) |
| picolibc | [764ef4e401a8f4c6a86ab723533841f072885a5b](https://github.com/zephyrproject-rtos/picolibc/commit/764ef4e401a8f4c6a86ab723533841f072885a5b) |
| segger | [9d0191285956cef43daf411edc2f1a7788346def](https://github.com/zephyrproject-rtos/segger/commit/9d0191285956cef43daf411edc2f1a7788346def) |
| tinycrypt | [3e9a49d2672ec01435ffbf0d788db6d95ef28de0](https://github.com/zephyrproject-rtos/tinycrypt/commit/3e9a49d2672ec01435ffbf0d788db6d95ef28de0) |
| trusted-firmware-m | [0b898c9b72171b0a260c0bb64a92ea4713f9e931](https://github.com/zephyrproject-rtos/trusted-firmware-m/commit/0b898c9b72171b0a260c0bb64a92ea4713f9e931) |
| trusted-firmware-a | [421dc050278287839f5c70019bd6aec617f2bbdb](https://github.com/zephyrproject-rtos/trusted-firmware-a/commit/421dc050278287839f5c70019bd6aec617f2bbdb) |
| uoscore-uedhoc | [150f4eb2955eaf36ac0f9519d4f4f58d5ade5740](https://github.com/zephyrproject-rtos/uoscore-uedhoc/commit/150f4eb2955eaf36ac0f9519d4f4f58d5ade5740) |
| zcbor | [d3093b5684f62268c7f27f8a5079f166772619de](https://github.com/zephyrproject-rtos/zcbor/commit/d3093b5684f62268c7f27f8a5079f166772619de) |

## Inactive and Optional Projects/Modules

The projects below are optional and will not be downloaded when you
call west update. You can add any of the projects or modules listed below
and use them to write application code and extend your workspace with the added
functionality.

To enable any of the modules below, use the following commands:

```text
west config manifest.project-filter -- +nanopb
west update
```

| Project | Revision |
| --- | --- |
| canopennode | [dec12fa3f0d790cafa8414a4c2930ea71ab72ffd](https://github.com/zephyrproject-rtos/canopennode/commit/dec12fa3f0d790cafa8414a4c2930ea71ab72ffd) |
| chre | [3b32c76efee705af146124fb4190f71be5a4e36e](https://github.com/zephyrproject-rtos/chre/commit/3b32c76efee705af146124fb4190f71be5a4e36e) |
| lz4 | [8e303c264fc21c2116dc612658003a22e933124d](https://github.com/zephyrproject-rtos/lz4/commit/8e303c264fc21c2116dc612658003a22e933124d) |
| nanopb | [42fa8b211e946b90b9d968523fce7b1cfe27617e](https://github.com/zephyrproject-rtos/nanopb/commit/42fa8b211e946b90b9d968523fce7b1cfe27617e) |
| psa-arch-tests | [2cadb02a72eacda7042505dcbdd492371e8ce024](https://github.com/zephyrproject-rtos/psa-arch-tests/commit/2cadb02a72eacda7042505dcbdd492371e8ce024) |
| sof | [0606152d4aafc1f7ed43df1b1813252bfc74e154](https://github.com/zephyrproject-rtos/sof/commit/0606152d4aafc1f7ed43df1b1813252bfc74e154) |
| tf-m-tests | [08a3158f0623a4205608a52d880b17ae394e31d2](https://github.com/zephyrproject-rtos/tf-m-tests/commit/08a3158f0623a4205608a52d880b17ae394e31d2) |
| tflite-micro | [1a34dcab41e7e0e667db72d6a40999c1ec9c510c](https://github.com/zephyrproject-rtos/tflite-micro/commit/1a34dcab41e7e0e667db72d6a40999c1ec9c510c) |
| thrift | [10023645a0e6cb7ce23fcd7fd3dbac9f18df6234](https://github.com/zephyrproject-rtos/thrift/commit/10023645a0e6cb7ce23fcd7fd3dbac9f18df6234) |
| zscilib | [a4bb6cfd6800e14373261904825f7f34a3a7f2e5](https://github.com/zephyrproject-rtos/zscilib/commit/a4bb6cfd6800e14373261904825f7f34a3a7f2e5) |
| bsim | [384a091445c57b44ac8cbd18ebd245b47c71db94](https://github.com/zephyrproject-rtos/babblesim-manifest/commit/384a091445c57b44ac8cbd18ebd245b47c71db94) |
| babblesim\_base | [19d62424c0802c6c9fc15528febe666e40f372a1](https://github.com/BabbleSim/base.git/commit/19d62424c0802c6c9fc15528febe666e40f372a1) |
| babblesim\_ext\_2G4\_libPhyComv1 | [9018113a362fa6c9e8f4b9cab9e5a8f12cc46b94](https://github.com/BabbleSim/ext_2G4_libPhyComv1.git/commit/9018113a362fa6c9e8f4b9cab9e5a8f12cc46b94) |
| babblesim\_ext\_2G4\_phy\_v1 | [d47c6dd90035b41b14f6921785ccb7b8484868e2](https://github.com/BabbleSim/ext_2G4_phy_v1.git/commit/d47c6dd90035b41b14f6921785ccb7b8484868e2) |
| babblesim\_ext\_2G4\_channel\_NtNcable | [20a38c997f507b0aa53817aab3d73a462fff7af1](https://github.com/BabbleSim/ext_2G4_channel_NtNcable.git/commit/20a38c997f507b0aa53817aab3d73a462fff7af1) |
| babblesim\_ext\_2G4\_channel\_multiatt | [bde72a57384dde7a4310bcf3843469401be93074](https://github.com/BabbleSim/ext_2G4_channel_multiatt.git/commit/bde72a57384dde7a4310bcf3843469401be93074) |
| babblesim\_ext\_2G4\_modem\_magic | [cb70771794f0bf6f262aa474848611c68ae8f1ed](https://github.com/BabbleSim/ext_2G4_modem_magic.git/commit/cb70771794f0bf6f262aa474848611c68ae8f1ed) |
| babblesim\_ext\_2G4\_modem\_BLE\_simple | [809ab073159c9ab6686c2fea5749b0702e0909f7](https://github.com/BabbleSim/ext_2G4_modem_BLE_simple.git/commit/809ab073159c9ab6686c2fea5749b0702e0909f7) |
| babblesim\_ext\_2G4\_device\_burst\_interferer | [5b5339351d6e6a2368c686c734dc8b2fc65698fc](https://github.com/BabbleSim/ext_2G4_device_burst_interferer.git/commit/5b5339351d6e6a2368c686c734dc8b2fc65698fc) |
| babblesim\_ext\_2G4\_device\_WLAN\_actmod | [9cb6d8e72695f6b785e57443f0629a18069d6ce4](https://github.com/BabbleSim/ext_2G4_device_WLAN_actmod.git/commit/9cb6d8e72695f6b785e57443f0629a18069d6ce4) |
| babblesim\_ext\_2G4\_device\_playback | [85c645929cf1ce995d8537107d9dcbd12ed64036](https://github.com/BabbleSim/ext_2G4_device_playback.git/commit/85c645929cf1ce995d8537107d9dcbd12ed64036) |
| babblesim\_ext\_libCryptov1 | [eed6d7038e839153e340bd333bc43541cb90ba64](https://github.com/BabbleSim/ext_libCryptov1.git/commit/eed6d7038e839153e340bd333bc43541cb90ba64) |

## External Projects/Modules

The projects listed below are external and are not directly imported into the
default manifest.
To use any of the projects below, you will need to define your own manifest
file which includes them. See [Manifest Imports](../west/manifest.md#west-manifest-import) for information on
recommended ways to do this while still inheriting the mandatory modules from
Zephyr’s `west.yml`.

Use the template `doc/develop/manifest/external/external.rst.tmpl` to add
external modules to the list below:
