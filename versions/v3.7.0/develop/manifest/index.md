---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/develop/manifest/index.html
original_path: develop/manifest/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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
| acpica | [8d24867bc9c9d81c81eeac59391cda59333affd4](https://github.com/zephyrproject-rtos/acpica/commit/8d24867bc9c9d81c81eeac59391cda59333affd4) |
| cmsis | [4b96cbb174678dcd3ca86e11e1f24bc5f8726da0](https://github.com/zephyrproject-rtos/cmsis/commit/4b96cbb174678dcd3ca86e11e1f24bc5f8726da0) |
| cmsis-dsp | [6489e771e9c405f1763b52d64a3f17a1ec488ace](https://github.com/zephyrproject-rtos/cmsis-dsp/commit/6489e771e9c405f1763b52d64a3f17a1ec488ace) |
| cmsis-nn | [ea987c1ca661be723de83bd159aed815d6cbd430](https://github.com/zephyrproject-rtos/cmsis-nn/commit/ea987c1ca661be723de83bd159aed815d6cbd430) |
| edtt | [8d7b543d4d2f2be0f78481e4e1d8d73a88024803](https://github.com/zephyrproject-rtos/edtt/commit/8d7b543d4d2f2be0f78481e4e1d8d73a88024803) |
| fatfs | [427159bf95ea49b7680facffaa29ad506b42709b](https://github.com/zephyrproject-rtos/fatfs/commit/427159bf95ea49b7680facffaa29ad506b42709b) |
| hal\_adi | [dee9a7b1eff13a9da0560daf8842d61657f9d61e](https://github.com/zephyrproject-rtos/hal_adi/commit/dee9a7b1eff13a9da0560daf8842d61657f9d61e) |
| hal\_altera | [4fe4df959d4593ce66e676aeba0b57f546dba0fe](https://github.com/zephyrproject-rtos/hal_altera/commit/4fe4df959d4593ce66e676aeba0b57f546dba0fe) |
| hal\_ambiq | [e25327f026df1ee08f1bf01a4bbfeb5e5f4026f1](https://github.com/zephyrproject-rtos/hal_ambiq/commit/e25327f026df1ee08f1bf01a4bbfeb5e5f4026f1) |
| hal\_atmel | [56d60ebc909ad065bf6554cee73487969857614b](https://github.com/zephyrproject-rtos/hal_atmel/commit/56d60ebc909ad065bf6554cee73487969857614b) |
| hal\_espressif | [87e7902d7184a8280b4d13bce79801a723f4ddd8](https://github.com/zephyrproject-rtos/hal_espressif/commit/87e7902d7184a8280b4d13bce79801a723f4ddd8) |
| hal\_ethos\_u | [8e2cf756b474eff9a32a9bdf1775d9620f1eadcf](https://github.com/zephyrproject-rtos/hal_ethos_u/commit/8e2cf756b474eff9a32a9bdf1775d9620f1eadcf) |
| hal\_gigadevice | [2994b7dde8b0b0fa9b9c0ccb13474b6a486cddc3](https://github.com/zephyrproject-rtos/hal_gigadevice/commit/2994b7dde8b0b0fa9b9c0ccb13474b6a486cddc3) |
| hal\_infineon | [f25734a72c585f6675e8254a382e80e78a3cd03a](https://github.com/zephyrproject-rtos/hal_infineon/commit/f25734a72c585f6675e8254a382e80e78a3cd03a) |
| hal\_intel | [0905a528623de56b1bedf817536321bcdbc0efae](https://github.com/zephyrproject-rtos/hal_intel/commit/0905a528623de56b1bedf817536321bcdbc0efae) |
| hal\_microchip | [71eba057c0cb7fc11b6f33eb40a82f1ebe2c571c](https://github.com/zephyrproject-rtos/hal_microchip/commit/71eba057c0cb7fc11b6f33eb40a82f1ebe2c571c) |
| hal\_nordic | [ab5cb2e2faeb1edfad7a25286dcb513929ae55da](https://github.com/zephyrproject-rtos/hal_nordic/commit/ab5cb2e2faeb1edfad7a25286dcb513929ae55da) |
| hal\_nuvoton | [466c3eed9c98453fb23953bf0e0427fea01924be](https://github.com/zephyrproject-rtos/hal_nuvoton/commit/466c3eed9c98453fb23953bf0e0427fea01924be) |
| hal\_nxp | [862e001504bd6e0a4feade6a718e9f973116849c](https://github.com/zephyrproject-rtos/hal_nxp/commit/862e001504bd6e0a4feade6a718e9f973116849c) |
| hal\_openisa | [eabd530a64d71de91d907bad257cd61aacf607bc](https://github.com/zephyrproject-rtos/hal_openisa/commit/eabd530a64d71de91d907bad257cd61aacf607bc) |
| hal\_quicklogic | [bad894440fe72c814864798c8e3a76d13edffb6c](https://github.com/zephyrproject-rtos/hal_quicklogic/commit/bad894440fe72c814864798c8e3a76d13edffb6c) |
| hal\_renesas | [af77d7cdfeeff290593e7e99f54f0c1e2a3f91e6](https://github.com/zephyrproject-rtos/hal_renesas/commit/af77d7cdfeeff290593e7e99f54f0c1e2a3f91e6) |
| hal\_rpi\_pico | [fba7162cc7bee06d0149622bbcaac4e41062d368](https://github.com/zephyrproject-rtos/hal_rpi_pico/commit/fba7162cc7bee06d0149622bbcaac4e41062d368) |
| hal\_silabs | [a09dd1b82b24aa3060e162c0dfa40026c0dba450](https://github.com/zephyrproject-rtos/hal_silabs/commit/a09dd1b82b24aa3060e162c0dfa40026c0dba450) |
| hal\_st | [b77157f6bc4395e398d90ab02a7d2cbc01ab2ce7](https://github.com/zephyrproject-rtos/hal_st/commit/b77157f6bc4395e398d90ab02a7d2cbc01ab2ce7) |
| hal\_stm32 | [f1317150eac951fdd8259337a47cbbc4c2e6d335](https://github.com/zephyrproject-rtos/hal_stm32/commit/f1317150eac951fdd8259337a47cbbc4c2e6d335) |
| hal\_telink | [4226c7fc17d5a34e557d026d428fc766191a0800](https://github.com/zephyrproject-rtos/hal_telink/commit/4226c7fc17d5a34e557d026d428fc766191a0800) |
| hal\_ti | [b85f86e51fc4d47c4c383d320d64d52d4d371ae4](https://github.com/zephyrproject-rtos/hal_ti/commit/b85f86e51fc4d47c4c383d320d64d52d4d371ae4) |
| hal\_wurthelektronik | [e5bcb2eac1bb9639ce13b4dafc78eb254e014342](https://github.com/zephyrproject-rtos/hal_wurthelektronik/commit/e5bcb2eac1bb9639ce13b4dafc78eb254e014342) |
| hal\_xtensa | [a2d658525b16c57bea8dd565f5bd5167e4b9f1ee](https://github.com/zephyrproject-rtos/hal_xtensa/commit/a2d658525b16c57bea8dd565f5bd5167e4b9f1ee) |
| hostap | [a90df86d7c596a5367ff70c2b50c7f599e6636f3](https://github.com/zephyrproject-rtos/hostap/commit/a90df86d7c596a5367ff70c2b50c7f599e6636f3) |
| libmetal | [a6851ba6dba8c9e87d00c42f171a822f7a29639b](https://github.com/zephyrproject-rtos/libmetal/commit/a6851ba6dba8c9e87d00c42f171a822f7a29639b) |
| liblc3 | [1a5938ebaca4f13fe79ce074f5dee079783aa29f](https://github.com/zephyrproject-rtos/liblc3/commit/1a5938ebaca4f13fe79ce074f5dee079783aa29f) |
| littlefs | [408c16a909dd6cf128874a76f21c793798c9e423](https://github.com/zephyrproject-rtos/littlefs/commit/408c16a909dd6cf128874a76f21c793798c9e423) |
| loramac-node | [fb00b383072518c918e2258b0916c996f2d4eebe](https://github.com/zephyrproject-rtos/loramac-node/commit/fb00b383072518c918e2258b0916c996f2d4eebe) |
| lvgl | [2b498e6f36d6b82ae1da12c8b7742e318624ecf5](https://github.com/zephyrproject-rtos/lvgl/commit/2b498e6f36d6b82ae1da12c8b7742e318624ecf5) |
| mbedtls | [2f24831ee13d399ce019c4632b0bcd440a713f7c](https://github.com/zephyrproject-rtos/mbedtls/commit/2f24831ee13d399ce019c4632b0bcd440a713f7c) |
| mcuboot | [fb2cf0ec3da3687b93f28e556ab682bdd4b85223](https://github.com/zephyrproject-rtos/mcuboot/commit/fb2cf0ec3da3687b93f28e556ab682bdd4b85223) |
| mipi-sys-t | [71ace1f5caa03e56c8740a09863e685efb4b2360](https://github.com/zephyrproject-rtos/mipi-sys-t/commit/71ace1f5caa03e56c8740a09863e685efb4b2360) |
| net-tools | [7c7a856814d7f27509c8511fef14cec21f7d0c30](https://github.com/zephyrproject-rtos/net-tools/commit/7c7a856814d7f27509c8511fef14cec21f7d0c30) |
| nrf\_hw\_models | [6c389b9b5fa0a079cd4502e69d375da4c0c289b7](https://github.com/zephyrproject-rtos/nrf_hw_models/commit/6c389b9b5fa0a079cd4502e69d375da4c0c289b7) |
| open-amp | [76d2168bcdfcd23a9a7dce8c21f2083b90a1e60a](https://github.com/zephyrproject-rtos/open-amp/commit/76d2168bcdfcd23a9a7dce8c21f2083b90a1e60a) |
| openthread | [3873c6fcd5a8a9dd01b71e8efe32ef5dc7923bb1](https://github.com/zephyrproject-rtos/openthread/commit/3873c6fcd5a8a9dd01b71e8efe32ef5dc7923bb1) |
| percepio | [a49e5f3947faad0dd654eddd5a750127fb81e50d](https://github.com/zephyrproject-rtos/percepio/commit/a49e5f3947faad0dd654eddd5a750127fb81e50d) |
| picolibc | [764ef4e401a8f4c6a86ab723533841f072885a5b](https://github.com/zephyrproject-rtos/picolibc/commit/764ef4e401a8f4c6a86ab723533841f072885a5b) |
| segger | [b011c45b585e097d95d9cf93edf4f2e01588d3cd](https://github.com/zephyrproject-rtos/segger/commit/b011c45b585e097d95d9cf93edf4f2e01588d3cd) |
| tinycrypt | [1012a3ebee18c15ede5efc8332ee2fc37817670f](https://github.com/zephyrproject-rtos/tinycrypt/commit/1012a3ebee18c15ede5efc8332ee2fc37817670f) |
| trusted-firmware-m | [069455be098383bf96eab73e3ff8e0c66c60fa5a](https://github.com/zephyrproject-rtos/trusted-firmware-m/commit/069455be098383bf96eab73e3ff8e0c66c60fa5a) |
| trusted-firmware-a | [713ffbf96c5bcbdeab757423f10f73eb304eff07](https://github.com/zephyrproject-rtos/trusted-firmware-a/commit/713ffbf96c5bcbdeab757423f10f73eb304eff07) |
| uoscore-uedhoc | [84ef879a46d7bfd9a423fbfb502b04289861f9ea](https://github.com/zephyrproject-rtos/uoscore-uedhoc/commit/84ef879a46d7bfd9a423fbfb502b04289861f9ea) |
| zcbor | [75d088037eb237b18e7ec1f47c9ce494b9b95aab](https://github.com/zephyrproject-rtos/zcbor/commit/75d088037eb237b18e7ec1f47c9ce494b9b95aab) |

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
| nanopb | [4474bd35bd39de067f0532a1b19ce3aed9ed9807](https://github.com/zephyrproject-rtos/nanopb/commit/4474bd35bd39de067f0532a1b19ce3aed9ed9807) |
| psa-arch-tests | [2cadb02a72eacda7042505dcbdd492371e8ce024](https://github.com/zephyrproject-rtos/psa-arch-tests/commit/2cadb02a72eacda7042505dcbdd492371e8ce024) |
| sof | [3f1716b0da7a48358bc265586b90b2252745c14c](https://github.com/zephyrproject-rtos/sof/commit/3f1716b0da7a48358bc265586b90b2252745c14c) |
| tf-m-tests | [d552e4f18b92032bd335d5e3aa312f6acd82a83b](https://github.com/zephyrproject-rtos/tf-m-tests/commit/d552e4f18b92032bd335d5e3aa312f6acd82a83b) |
| tflite-micro | [48613f7ba1ffbda46ad771a77a35408f48f922e9](https://github.com/zephyrproject-rtos/tflite-micro/commit/48613f7ba1ffbda46ad771a77a35408f48f922e9) |
| thrift | [10023645a0e6cb7ce23fcd7fd3dbac9f18df6234](https://github.com/zephyrproject-rtos/thrift/commit/10023645a0e6cb7ce23fcd7fd3dbac9f18df6234) |
| zscilib | [ee1b287d9dd07208d2cc52284240ac25bb66eae3](https://github.com/zephyrproject-rtos/zscilib/commit/ee1b287d9dd07208d2cc52284240ac25bb66eae3) |
| bsim | [9351ae1ad44864a49c351f9704f65f43046abeb0](https://github.com/zephyrproject-rtos/babblesim-manifest/commit/9351ae1ad44864a49c351f9704f65f43046abeb0) |
| babblesim\_base | [4bd907be0b2abec3b31a23fd8ca98db2a07209d2](https://github.com/BabbleSim/base/commit/4bd907be0b2abec3b31a23fd8ca98db2a07209d2) |
| babblesim\_ext\_2G4\_libPhyComv1 | [93f5eba512c438b0c9ebc1b1a947517c865b3643](https://github.com/BabbleSim/ext_2G4_libPhyComv1/commit/93f5eba512c438b0c9ebc1b1a947517c865b3643) |
| babblesim\_ext\_2G4\_phy\_v1 | [04eeb3c3794444122fbeeb3715f4233b0b50cfbb](https://github.com/BabbleSim/ext_2G4_phy_v1/commit/04eeb3c3794444122fbeeb3715f4233b0b50cfbb) |
| babblesim\_ext\_2G4\_channel\_NtNcable | [20a38c997f507b0aa53817aab3d73a462fff7af1](https://github.com/BabbleSim/ext_2G4_channel_NtNcable/commit/20a38c997f507b0aa53817aab3d73a462fff7af1) |
| babblesim\_ext\_2G4\_channel\_multiatt | [bde72a57384dde7a4310bcf3843469401be93074](https://github.com/BabbleSim/ext_2G4_channel_multiatt/commit/bde72a57384dde7a4310bcf3843469401be93074) |
| babblesim\_ext\_2G4\_modem\_magic | [edfcda2d3937a74be0a59d6cd47e0f50183453da](https://github.com/BabbleSim/ext_2G4_modem_magic/commit/edfcda2d3937a74be0a59d6cd47e0f50183453da) |
| babblesim\_ext\_2G4\_modem\_BLE\_simple | [a38d2d24b04a6f970a225d1316047256ebf5a539](https://github.com/BabbleSim/ext_2G4_modem_BLE_simple/commit/a38d2d24b04a6f970a225d1316047256ebf5a539) |
| babblesim\_ext\_2G4\_device\_burst\_interferer | [5b5339351d6e6a2368c686c734dc8b2fc65698fc](https://github.com/BabbleSim/ext_2G4_device_burst_interferer/commit/5b5339351d6e6a2368c686c734dc8b2fc65698fc) |
| babblesim\_ext\_2G4\_device\_WLAN\_actmod | [9cb6d8e72695f6b785e57443f0629a18069d6ce4](https://github.com/BabbleSim/ext_2G4_device_WLAN_actmod/commit/9cb6d8e72695f6b785e57443f0629a18069d6ce4) |
| babblesim\_ext\_2G4\_device\_playback | [abb48cd71ddd4e2a9022f4bf49b2712524c483e8](https://github.com/BabbleSim/ext_2G4_device_playback/commit/abb48cd71ddd4e2a9022f4bf49b2712524c483e8) |
| babblesim\_ext\_libCryptov1 | [eed6d7038e839153e340bd333bc43541cb90ba64](https://github.com/BabbleSim/ext_libCryptov1/commit/eed6d7038e839153e340bd333bc43541cb90ba64) |

## External Projects/Modules

The projects listed below are external and are not directly imported into the
default manifest.
To use any of the projects below, you will need to define your own manifest
file which includes them. See [Manifest Imports](../west/manifest.md#west-manifest-import) for information on
recommended ways to do this while still inheriting the mandatory modules from
Zephyr’s `west.yml`.

Use the template `doc/develop/manifest/external/external.rst.tmpl` to add
external modules to the list below:
