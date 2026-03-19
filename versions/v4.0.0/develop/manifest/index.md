---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/develop/manifest/index.html
original_path: develop/manifest/index.html
---

# West Projects index

See [Contributing External Components](../../contribute/external.md#external-contributions) for more information about
this contributing and review process for imported components.

## Active Projects/Modules

The projects below are enabled by default and will be downloaded when you
call **west update**. Many of the projects or modules listed below are
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
| edtt | [b9ca3c7030518f07b7937dacf970d37a47865a76](https://github.com/zephyrproject-rtos/edtt/commit/b9ca3c7030518f07b7937dacf970d37a47865a76) |
| fatfs | [427159bf95ea49b7680facffaa29ad506b42709b](https://github.com/zephyrproject-rtos/fatfs/commit/427159bf95ea49b7680facffaa29ad506b42709b) |
| hal\_adi | [a3eecfde1c76d38312b94fd346c7ba9fe2661992](https://github.com/zephyrproject-rtos/hal_adi/commit/a3eecfde1c76d38312b94fd346c7ba9fe2661992) |
| hal\_altera | [4fe4df959d4593ce66e676aeba0b57f546dba0fe](https://github.com/zephyrproject-rtos/hal_altera/commit/4fe4df959d4593ce66e676aeba0b57f546dba0fe) |
| hal\_ambiq | [d3092f9b82874a1791baa3ac41c3795d108fbbdb](https://github.com/zephyrproject-rtos/hal_ambiq/commit/d3092f9b82874a1791baa3ac41c3795d108fbbdb) |
| hal\_atmel | [56d60ebc909ad065bf6554cee73487969857614b](https://github.com/zephyrproject-rtos/hal_atmel/commit/56d60ebc909ad065bf6554cee73487969857614b) |
| hal\_espressif | [07ff57e8d197765652b7819b297415d859ed7815](https://github.com/zephyrproject-rtos/hal_espressif/commit/07ff57e8d197765652b7819b297415d859ed7815) |
| hal\_ethos\_u | [8e2cf756b474eff9a32a9bdf1775d9620f1eadcf](https://github.com/zephyrproject-rtos/hal_ethos_u/commit/8e2cf756b474eff9a32a9bdf1775d9620f1eadcf) |
| hal\_gigadevice | [2994b7dde8b0b0fa9b9c0ccb13474b6a486cddc3](https://github.com/zephyrproject-rtos/hal_gigadevice/commit/2994b7dde8b0b0fa9b9c0ccb13474b6a486cddc3) |
| hal\_infineon | [88d2529a3c5aee2e81947553bf6cbacb4671088c](https://github.com/zephyrproject-rtos/hal_infineon/commit/88d2529a3c5aee2e81947553bf6cbacb4671088c) |
| hal\_intel | [8876a1815bc59e0464d285459b71e3d69872edfd](https://github.com/zephyrproject-rtos/hal_intel/commit/8876a1815bc59e0464d285459b71e3d69872edfd) |
| hal\_microchip | [71eba057c0cb7fc11b6f33eb40a82f1ebe2c571c](https://github.com/zephyrproject-rtos/hal_microchip/commit/71eba057c0cb7fc11b6f33eb40a82f1ebe2c571c) |
| hal\_nordic | [5c8d109371ebb740fbef1f440a3b59e488a36717](https://github.com/zephyrproject-rtos/hal_nordic/commit/5c8d109371ebb740fbef1f440a3b59e488a36717) |
| hal\_nuvoton | [466c3eed9c98453fb23953bf0e0427fea01924be](https://github.com/zephyrproject-rtos/hal_nuvoton/commit/466c3eed9c98453fb23953bf0e0427fea01924be) |
| hal\_nxp | [3c64cd63125c86870802a561ce79dc33697b005c](https://github.com/zephyrproject-rtos/hal_nxp/commit/3c64cd63125c86870802a561ce79dc33697b005c) |
| hal\_openisa | [eabd530a64d71de91d907bad257cd61aacf607bc](https://github.com/zephyrproject-rtos/hal_openisa/commit/eabd530a64d71de91d907bad257cd61aacf607bc) |
| hal\_quicklogic | [bad894440fe72c814864798c8e3a76d13edffb6c](https://github.com/zephyrproject-rtos/hal_quicklogic/commit/bad894440fe72c814864798c8e3a76d13edffb6c) |
| hal\_renesas | [10326518701e25bf336a2eaeb8b5820110e4e6a3](https://github.com/zephyrproject-rtos/hal_renesas/commit/10326518701e25bf336a2eaeb8b5820110e4e6a3) |
| hal\_rpi\_pico | [79ee0f9e058a6327fc943d2f2a19cf3ade107cec](https://github.com/zephyrproject-rtos/hal_rpi_pico/commit/79ee0f9e058a6327fc943d2f2a19cf3ade107cec) |
| hal\_silabs | [69a5fad41aced94dc59d3103edd6ef370851e623](https://github.com/zephyrproject-rtos/hal_silabs/commit/69a5fad41aced94dc59d3103edd6ef370851e623) |
| hal\_st | [b2f548fe672f24122c7f92027b2c9eeea8a0483a](https://github.com/zephyrproject-rtos/hal_st/commit/b2f548fe672f24122c7f92027b2c9eeea8a0483a) |
| hal\_stm32 | [019d8255333f96bdd47d26b44049bd3e7af8ef55](https://github.com/zephyrproject-rtos/hal_stm32/commit/019d8255333f96bdd47d26b44049bd3e7af8ef55) |
| hal\_telink | [4226c7fc17d5a34e557d026d428fc766191a0800](https://github.com/zephyrproject-rtos/hal_telink/commit/4226c7fc17d5a34e557d026d428fc766191a0800) |
| hal\_ti | [2e7b95ad079e9f636884eedc6853e6ad98b85f65](https://github.com/zephyrproject-rtos/hal_ti/commit/2e7b95ad079e9f636884eedc6853e6ad98b85f65) |
| hal\_wurthelektronik | [e3e2797b224fc48fdef1bc3e5a12a7c73108bba2](https://github.com/zephyrproject-rtos/hal_wurthelektronik/commit/e3e2797b224fc48fdef1bc3e5a12a7c73108bba2) |
| hal\_xtensa | [baa56aa3e119b5aae43d16f9b2d2c8112e052871](https://github.com/zephyrproject-rtos/hal_xtensa/commit/baa56aa3e119b5aae43d16f9b2d2c8112e052871) |
| hostap | [0f7b166487b1ac08e1c6c492383f5c103320b2be](https://github.com/zephyrproject-rtos/hostap/commit/0f7b166487b1ac08e1c6c492383f5c103320b2be) |
| libmetal | [a6851ba6dba8c9e87d00c42f171a822f7a29639b](https://github.com/zephyrproject-rtos/libmetal/commit/a6851ba6dba8c9e87d00c42f171a822f7a29639b) |
| liblc3 | [1a5938ebaca4f13fe79ce074f5dee079783aa29f](https://github.com/zephyrproject-rtos/liblc3/commit/1a5938ebaca4f13fe79ce074f5dee079783aa29f) |
| littlefs | [009bcff0ed4853a53df8256039fa815bda6854dd](https://github.com/zephyrproject-rtos/littlefs/commit/009bcff0ed4853a53df8256039fa815bda6854dd) |
| loramac-node | [fb00b383072518c918e2258b0916c996f2d4eebe](https://github.com/zephyrproject-rtos/loramac-node/commit/fb00b383072518c918e2258b0916c996f2d4eebe) |
| lvgl | [2b498e6f36d6b82ae1da12c8b7742e318624ecf5](https://github.com/zephyrproject-rtos/lvgl/commit/2b498e6f36d6b82ae1da12c8b7742e318624ecf5) |
| mbedtls | [a78176c6ff0733ba08018cba4447bd3f20de7978](https://github.com/zephyrproject-rtos/mbedtls/commit/a78176c6ff0733ba08018cba4447bd3f20de7978) |
| mcuboot | [f74b77cf7808919837c0ed14c2ead3918c546349](https://github.com/zephyrproject-rtos/mcuboot/commit/f74b77cf7808919837c0ed14c2ead3918c546349) |
| mipi-sys-t | [71ace1f5caa03e56c8740a09863e685efb4b2360](https://github.com/zephyrproject-rtos/mipi-sys-t/commit/71ace1f5caa03e56c8740a09863e685efb4b2360) |
| net-tools | [93acc8bac4661e74e695eb1aea94c7c5262db2e2](https://github.com/zephyrproject-rtos/net-tools/commit/93acc8bac4661e74e695eb1aea94c7c5262db2e2) |
| nrf\_hw\_models | [aca798cf7cf0c5dc1fd89c66cf62670051feb8d0](https://github.com/zephyrproject-rtos/nrf_hw_models/commit/aca798cf7cf0c5dc1fd89c66cf62670051feb8d0) |
| open-amp | [b735edbc739ad59156eb55bb8ce2583d74537719](https://github.com/zephyrproject-rtos/open-amp/commit/b735edbc739ad59156eb55bb8ce2583d74537719) |
| openthread | [2aeb8b833ba760ec29d5f340dd1ce7bcb61c5d56](https://github.com/zephyrproject-rtos/openthread/commit/2aeb8b833ba760ec29d5f340dd1ce7bcb61c5d56) |
| percepio | [b68d17993109b9bee6b45dc8c9794e7b7bce236d](https://github.com/zephyrproject-rtos/percepio/commit/b68d17993109b9bee6b45dc8c9794e7b7bce236d) |
| picolibc | [d492d5fa7c96918e37653f303028346bb0dd51a2](https://github.com/zephyrproject-rtos/picolibc/commit/d492d5fa7c96918e37653f303028346bb0dd51a2) |
| segger | [798f95ea9304e5ed8165a661081443051f210733](https://github.com/zephyrproject-rtos/segger/commit/798f95ea9304e5ed8165a661081443051f210733) |
| tinycrypt | [1012a3ebee18c15ede5efc8332ee2fc37817670f](https://github.com/zephyrproject-rtos/tinycrypt/commit/1012a3ebee18c15ede5efc8332ee2fc37817670f) |
| trusted-firmware-m | [8134106ef9cb3df60e8bd22b172532558e936bd2](https://github.com/zephyrproject-rtos/trusted-firmware-m/commit/8134106ef9cb3df60e8bd22b172532558e936bd2) |
| trusted-firmware-a | [713ffbf96c5bcbdeab757423f10f73eb304eff07](https://github.com/zephyrproject-rtos/trusted-firmware-a/commit/713ffbf96c5bcbdeab757423f10f73eb304eff07) |
| uoscore-uedhoc | [84ef879a46d7bfd9a423fbfb502b04289861f9ea](https://github.com/zephyrproject-rtos/uoscore-uedhoc/commit/84ef879a46d7bfd9a423fbfb502b04289861f9ea) |
| zcbor | [47f34dd7f5284e8750b5a715dee7f77c6c5bdc3f](https://github.com/zephyrproject-rtos/zcbor/commit/47f34dd7f5284e8750b5a715dee7f77c6c5bdc3f) |

## Inactive and Optional Projects/Modules

The projects below are optional and will not be downloaded when you
call **west update**. You can add any of the projects or modules listed below
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
| lz4 | [11b8a1e22fa651b524494e55d22b69d3d9cebcfd](https://github.com/zephyrproject-rtos/lz4/commit/11b8a1e22fa651b524494e55d22b69d3d9cebcfd) |
| nanopb | [98bf4db69897b53434f3d0ba72e0a3ab1a902824](https://github.com/zephyrproject-rtos/nanopb/commit/98bf4db69897b53434f3d0ba72e0a3ab1a902824) |
| psa-arch-tests | [2cadb02a72eacda7042505dcbdd492371e8ce024](https://github.com/zephyrproject-rtos/psa-arch-tests/commit/2cadb02a72eacda7042505dcbdd492371e8ce024) |
| zephyr-lang-rust | [7af3db47bf7335ac6a6fe7480df6b41fb46dbe9d](https://github.com/zephyrproject-rtos/zephyr-lang-rust/commit/7af3db47bf7335ac6a6fe7480df6b41fb46dbe9d) |
| sof | [316f414b64dee8e4aefce503af6c2c2e57d266f4](https://github.com/zephyrproject-rtos/sof/commit/316f414b64dee8e4aefce503af6c2c2e57d266f4) |
| tf-m-tests | [502ea90105ee18f20c78f710e2ba2ded0fc0756e](https://github.com/zephyrproject-rtos/tf-m-tests/commit/502ea90105ee18f20c78f710e2ba2ded0fc0756e) |
| tflite-micro | [48613f7ba1ffbda46ad771a77a35408f48f922e9](https://github.com/zephyrproject-rtos/tflite-micro/commit/48613f7ba1ffbda46ad771a77a35408f48f922e9) |
| thrift | [10023645a0e6cb7ce23fcd7fd3dbac9f18df6234](https://github.com/zephyrproject-rtos/thrift/commit/10023645a0e6cb7ce23fcd7fd3dbac9f18df6234) |
| zscilib | [ee1b287d9dd07208d2cc52284240ac25bb66eae3](https://github.com/zephyrproject-rtos/zscilib/commit/ee1b287d9dd07208d2cc52284240ac25bb66eae3) |
| bsim | [1f242f4ed7fc141fdfcfeca8d21c6d9e801179d7](https://github.com/zephyrproject-rtos/babblesim-manifest/commit/1f242f4ed7fc141fdfcfeca8d21c6d9e801179d7) |
| babblesim\_base | [0cc70e78a88c1de9d8ec045a703b38134861e7e7](https://github.com/BabbleSim/base/commit/0cc70e78a88c1de9d8ec045a703b38134861e7e7) |
| babblesim\_ext\_2G4\_libPhyComv1 | [15ae0f87fa049e04cbec48a866f3bc37d903f950](https://github.com/BabbleSim/ext_2G4_libPhyComv1/commit/15ae0f87fa049e04cbec48a866f3bc37d903f950) |
| babblesim\_ext\_2G4\_phy\_v1 | [62e797b2c518e5bb6123a198382ed2b64b8c068e](https://github.com/BabbleSim/ext_2G4_phy_v1/commit/62e797b2c518e5bb6123a198382ed2b64b8c068e) |
| babblesim\_ext\_2G4\_channel\_NtNcable | [20a38c997f507b0aa53817aab3d73a462fff7af1](https://github.com/BabbleSim/ext_2G4_channel_NtNcable/commit/20a38c997f507b0aa53817aab3d73a462fff7af1) |
| babblesim\_ext\_2G4\_channel\_multiatt | [bde72a57384dde7a4310bcf3843469401be93074](https://github.com/BabbleSim/ext_2G4_channel_multiatt/commit/bde72a57384dde7a4310bcf3843469401be93074) |
| babblesim\_ext\_2G4\_modem\_magic | [edfcda2d3937a74be0a59d6cd47e0f50183453da](https://github.com/BabbleSim/ext_2G4_modem_magic/commit/edfcda2d3937a74be0a59d6cd47e0f50183453da) |
| babblesim\_ext\_2G4\_modem\_BLE\_simple | [4d2379de510684cd4b1c3bbbb09bce7b5a20bc1f](https://github.com/BabbleSim/ext_2G4_modem_BLE_simple/commit/4d2379de510684cd4b1c3bbbb09bce7b5a20bc1f) |
| babblesim\_ext\_2G4\_device\_burst\_interferer | [5b5339351d6e6a2368c686c734dc8b2fc65698fc](https://github.com/BabbleSim/ext_2G4_device_burst_interferer/commit/5b5339351d6e6a2368c686c734dc8b2fc65698fc) |
| babblesim\_ext\_2G4\_device\_WLAN\_actmod | [9cb6d8e72695f6b785e57443f0629a18069d6ce4](https://github.com/BabbleSim/ext_2G4_device_WLAN_actmod/commit/9cb6d8e72695f6b785e57443f0629a18069d6ce4) |
| babblesim\_ext\_2G4\_device\_playback | [abb48cd71ddd4e2a9022f4bf49b2712524c483e8](https://github.com/BabbleSim/ext_2G4_device_playback/commit/abb48cd71ddd4e2a9022f4bf49b2712524c483e8) |
| babblesim\_ext\_libCryptov1 | [236309584c90be32ef12848077bd6de54e9f4deb](https://github.com/BabbleSim/ext_libCryptov1/commit/236309584c90be32ef12848077bd6de54e9f4deb) |

## External Projects/Modules

The projects listed below are external and are not directly imported into the
default manifest.
To use any of the projects below, you will need to define your own manifest
file which includes them. See [Manifest Imports](../west/manifest.md#west-manifest-import) for information on
recommended ways to do this while still inheriting the mandatory modules from
Zephyr’s `west.yml`.

Use the template `doc/develop/manifest/external/external.rst.tmpl` to add
external modules to the list below:
