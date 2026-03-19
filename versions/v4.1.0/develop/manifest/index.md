---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/develop/manifest/index.html
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
| cmsis | [d1b8b20b6278615b00e136374540eb1c00dcabe7](https://github.com/zephyrproject-rtos/cmsis/commit/d1b8b20b6278615b00e136374540eb1c00dcabe7) |
| cmsis-dsp | [d80a49b2bb186317dc1db4ac88da49c0ab77e6e7](https://github.com/zephyrproject-rtos/cmsis-dsp/commit/d80a49b2bb186317dc1db4ac88da49c0ab77e6e7) |
| cmsis-nn | [e9328d612ea3ea7d0d210d3ac16ea8667c01abdd](https://github.com/zephyrproject-rtos/cmsis-nn/commit/e9328d612ea3ea7d0d210d3ac16ea8667c01abdd) |
| cmsis\_6 | [783317a3072554acbac86cca2ff24928cbf98d30](https://github.com/zephyrproject-rtos/CMSIS_6/commit/783317a3072554acbac86cca2ff24928cbf98d30) |
| edtt | [b9ca3c7030518f07b7937dacf970d37a47865a76](https://github.com/zephyrproject-rtos/edtt/commit/b9ca3c7030518f07b7937dacf970d37a47865a76) |
| fatfs | [16245c7c41d2b79e74984f49b5202551786b8a9b](https://github.com/zephyrproject-rtos/fatfs/commit/16245c7c41d2b79e74984f49b5202551786b8a9b) |
| hal\_adi | [633fcecf3717aaa22079cf6121627a879f24df51](https://github.com/zephyrproject-rtos/hal_adi/commit/633fcecf3717aaa22079cf6121627a879f24df51) |
| hal\_altera | [4fe4df959d4593ce66e676aeba0b57f546dba0fe](https://github.com/zephyrproject-rtos/hal_altera/commit/4fe4df959d4593ce66e676aeba0b57f546dba0fe) |
| hal\_ambiq | [87a188b91aca22ce3ce7deb4a1cbf7780d784673](https://github.com/zephyrproject-rtos/hal_ambiq/commit/87a188b91aca22ce3ce7deb4a1cbf7780d784673) |
| hal\_atmel | [da767444cce3c1d9ccd6b8a35fd7c67dc82d489c](https://github.com/zephyrproject-rtos/hal_atmel/commit/da767444cce3c1d9ccd6b8a35fd7c67dc82d489c) |
| hal\_espressif | [202c59552dc98e5cd02386313e1977ecb17a131f](https://github.com/zephyrproject-rtos/hal_espressif/commit/202c59552dc98e5cd02386313e1977ecb17a131f) |
| hal\_ethos\_u | [50ddffca1cc700112f25ad9bc077915a0355ee5d](https://github.com/zephyrproject-rtos/hal_ethos_u/commit/50ddffca1cc700112f25ad9bc077915a0355ee5d) |
| hal\_gigadevice | [2994b7dde8b0b0fa9b9c0ccb13474b6a486cddc3](https://github.com/zephyrproject-rtos/hal_gigadevice/commit/2994b7dde8b0b0fa9b9c0ccb13474b6a486cddc3) |
| hal\_infineon | [468e955eb49b8a731474ff194ca17b6e6a08c2d9](https://github.com/zephyrproject-rtos/hal_infineon/commit/468e955eb49b8a731474ff194ca17b6e6a08c2d9) |
| hal\_intel | [0355bb816263c54eed23c7781034447af5d8200c](https://github.com/zephyrproject-rtos/hal_intel/commit/0355bb816263c54eed23c7781034447af5d8200c) |
| hal\_microchip | [fa2431a906ffb560160d40739d7cf04169551103](https://github.com/zephyrproject-rtos/hal_microchip/commit/fa2431a906ffb560160d40739d7cf04169551103) |
| hal\_nordic | [37ca068d7b013fb65a2acc9306bffa48a3e72839](https://github.com/zephyrproject-rtos/hal_nordic/commit/37ca068d7b013fb65a2acc9306bffa48a3e72839) |
| hal\_nuvoton | [466c3eed9c98453fb23953bf0e0427fea01924be](https://github.com/zephyrproject-rtos/hal_nuvoton/commit/466c3eed9c98453fb23953bf0e0427fea01924be) |
| hal\_nxp | [9dc7449014a7380355612453b31be479cb3a6833](https://github.com/zephyrproject-rtos/hal_nxp/commit/9dc7449014a7380355612453b31be479cb3a6833) |
| hal\_openisa | [eabd530a64d71de91d907bad257cd61aacf607bc](https://github.com/zephyrproject-rtos/hal_openisa/commit/eabd530a64d71de91d907bad257cd61aacf607bc) |
| hal\_quicklogic | [bad894440fe72c814864798c8e3a76d13edffb6c](https://github.com/zephyrproject-rtos/hal_quicklogic/commit/bad894440fe72c814864798c8e3a76d13edffb6c) |
| hal\_renesas | [3204903bdc5eda6869a40363560a69369c8d0e22](https://github.com/zephyrproject-rtos/hal_renesas/commit/3204903bdc5eda6869a40363560a69369c8d0e22) |
| hal\_rpi\_pico | [7b57b24588797e6e7bf18b6bda168e6b96374264](https://github.com/zephyrproject-rtos/hal_rpi_pico/commit/7b57b24588797e6e7bf18b6bda168e6b96374264) |
| hal\_silabs | [8a173e9e566a396a19d18da4661cb54ce098f268](https://github.com/zephyrproject-rtos/hal_silabs/commit/8a173e9e566a396a19d18da4661cb54ce098f268) |
| hal\_st | [05fd4533730a9aea845261c5d24ed9832a6f0b6e](https://github.com/zephyrproject-rtos/hal_st/commit/05fd4533730a9aea845261c5d24ed9832a6f0b6e) |
| hal\_stm32 | [55043bcc35fffa3b4a8c75a696d932b5020aad09](https://github.com/zephyrproject-rtos/hal_stm32/commit/55043bcc35fffa3b4a8c75a696d932b5020aad09) |
| hal\_tdk | [6727477af1e46fa43878102489b9672a9d24e39f](https://github.com/zephyrproject-rtos/hal_tdk/commit/6727477af1e46fa43878102489b9672a9d24e39f) |
| hal\_telink | [4226c7fc17d5a34e557d026d428fc766191a0800](https://github.com/zephyrproject-rtos/hal_telink/commit/4226c7fc17d5a34e557d026d428fc766191a0800) |
| hal\_ti | [258652a3ac5d7df68ba8df20e4705c3bd98ede38](https://github.com/zephyrproject-rtos/hal_ti/commit/258652a3ac5d7df68ba8df20e4705c3bd98ede38) |
| hal\_wch | [1de9d3e406726702ce7cfc504509a02ecc463554](https://github.com/zephyrproject-rtos/hal_wch/commit/1de9d3e406726702ce7cfc504509a02ecc463554) |
| hal\_wurthelektronik | [e3e2797b224fc48fdef1bc3e5a12a7c73108bba2](https://github.com/zephyrproject-rtos/hal_wurthelektronik/commit/e3e2797b224fc48fdef1bc3e5a12a7c73108bba2) |
| hal\_xtensa | [baa56aa3e119b5aae43d16f9b2d2c8112e052871](https://github.com/zephyrproject-rtos/hal_xtensa/commit/baa56aa3e119b5aae43d16f9b2d2c8112e052871) |
| hostap | [697fd2cf5cbbd0c5375fc34761b6a9d7489a67d2](https://github.com/zephyrproject-rtos/hostap/commit/697fd2cf5cbbd0c5375fc34761b6a9d7489a67d2) |
| liblc3 | [48bbd3eacd36e99a57317a0a4867002e0b09e183](https://github.com/zephyrproject-rtos/liblc3/commit/48bbd3eacd36e99a57317a0a4867002e0b09e183) |
| libmctp | [b97860e78998551af99931ece149eeffc538bdb1](https://github.com/zephyrproject-rtos/libmctp/commit/b97860e78998551af99931ece149eeffc538bdb1) |
| libmetal | [3e8781aae9d7285203118c05bc01d4eb0ca565a7](https://github.com/zephyrproject-rtos/libmetal/commit/3e8781aae9d7285203118c05bc01d4eb0ca565a7) |
| littlefs | [ed0531d59ee37f5fb2762bcf2fc8ba4efaf82656](https://github.com/zephyrproject-rtos/littlefs/commit/ed0531d59ee37f5fb2762bcf2fc8ba4efaf82656) |
| loramac-node | [fb00b383072518c918e2258b0916c996f2d4eebe](https://github.com/zephyrproject-rtos/loramac-node/commit/fb00b383072518c918e2258b0916c996f2d4eebe) |
| lvgl | [1ed1ddd881c3784049a92bb9fe37c38c6c74d998](https://github.com/zephyrproject-rtos/lvgl/commit/1ed1ddd881c3784049a92bb9fe37c38c6c74d998) |
| mbedtls | [4952e1328529ee549d412b498ea71c54f30aa3b1](https://github.com/zephyrproject-rtos/mbedtls/commit/4952e1328529ee549d412b498ea71c54f30aa3b1) |
| mcuboot | [346f7374ff4467e40b5594658f8ac67a5e9813c9](https://github.com/zephyrproject-rtos/mcuboot/commit/346f7374ff4467e40b5594658f8ac67a5e9813c9) |
| mipi-sys-t | [33e5c23cbedda5ba12dbe50c4baefb362a791001](https://github.com/zephyrproject-rtos/mipi-sys-t/commit/33e5c23cbedda5ba12dbe50c4baefb362a791001) |
| net-tools | [93acc8bac4661e74e695eb1aea94c7c5262db2e2](https://github.com/zephyrproject-rtos/net-tools/commit/93acc8bac4661e74e695eb1aea94c7c5262db2e2) |
| nrf\_hw\_models | [73a5d5827a94820be65b7d276d28173ec10bab9f](https://github.com/zephyrproject-rtos/nrf_hw_models/commit/73a5d5827a94820be65b7d276d28173ec10bab9f) |
| nrf\_wifi | [e35f707a782b7c4c0eb83a3b06ca4e6eb693f29f](https://github.com/zephyrproject-rtos/nrf_wifi/commit/e35f707a782b7c4c0eb83a3b06ca4e6eb693f29f) |
| open-amp | [52bb1783521c62c019451cee9b05b8eda9d7425f](https://github.com/zephyrproject-rtos/open-amp/commit/52bb1783521c62c019451cee9b05b8eda9d7425f) |
| openthread | [3ae741f95e7dfb391dec35c48742862049eb62e8](https://github.com/zephyrproject-rtos/openthread/commit/3ae741f95e7dfb391dec35c48742862049eb62e8) |
| percepio | [49e6dc202aa38c2a3edbafcc2dab85dec6aee973](https://github.com/zephyrproject-rtos/percepio/commit/49e6dc202aa38c2a3edbafcc2dab85dec6aee973) |
| picolibc | [82d62ed1ac55b4e34a12d0390aced2dc9af13fc9](https://github.com/zephyrproject-rtos/picolibc/commit/82d62ed1ac55b4e34a12d0390aced2dc9af13fc9) |
| segger | [cf56b1d9c80f81a26e2ac5727c9cf177116a4692](https://github.com/zephyrproject-rtos/segger/commit/cf56b1d9c80f81a26e2ac5727c9cf177116a4692) |
| tinycrypt | [1012a3ebee18c15ede5efc8332ee2fc37817670f](https://github.com/zephyrproject-rtos/tinycrypt/commit/1012a3ebee18c15ede5efc8332ee2fc37817670f) |
| trusted-firmware-a | [713ffbf96c5bcbdeab757423f10f73eb304eff07](https://github.com/zephyrproject-rtos/trusted-firmware-a/commit/713ffbf96c5bcbdeab757423f10f73eb304eff07) |
| trusted-firmware-m | [918f32d9fce5e0ee59fc33844b5317b7626ce37a](https://github.com/zephyrproject-rtos/trusted-firmware-m/commit/918f32d9fce5e0ee59fc33844b5317b7626ce37a) |
| uoscore-uedhoc | [54abc109c9c0adfd53c70077744c14e454f04f4a](https://github.com/zephyrproject-rtos/uoscore-uedhoc/commit/54abc109c9c0adfd53c70077744c14e454f04f4a) |
| zcbor | [9b07780aca6fb21f82a241ba386ad9b379809337](https://github.com/zephyrproject-rtos/zcbor/commit/9b07780aca6fb21f82a241ba386ad9b379809337) |

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
| nanopb | [7307ce399b81ddcb3c3a5dc862c52d4754328d38](https://github.com/zephyrproject-rtos/nanopb/commit/7307ce399b81ddcb3c3a5dc862c52d4754328d38) |
| psa-arch-tests | [2cadb02a72eacda7042505dcbdd492371e8ce024](https://github.com/zephyrproject-rtos/psa-arch-tests/commit/2cadb02a72eacda7042505dcbdd492371e8ce024) |
| sof | [bc08c9c606324cfba0c104f4ffaf5dd456cb11d6](https://github.com/zephyrproject-rtos/sof/commit/bc08c9c606324cfba0c104f4ffaf5dd456cb11d6) |
| tf-m-tests | [502ea90105ee18f20c78f710e2ba2ded0fc0756e](https://github.com/zephyrproject-rtos/tf-m-tests/commit/502ea90105ee18f20c78f710e2ba2ded0fc0756e) |
| tflite-micro | [8d404de73acf7687831e16d88e86e4f73cfddf8e](https://github.com/zephyrproject-rtos/tflite-micro/commit/8d404de73acf7687831e16d88e86e4f73cfddf8e) |
| thrift | [10023645a0e6cb7ce23fcd7fd3dbac9f18df6234](https://github.com/zephyrproject-rtos/thrift/commit/10023645a0e6cb7ce23fcd7fd3dbac9f18df6234) |
| zephyr-lang-rust | [37dc7fac3fb0372bc0e78e022bef87fcce68c48d](https://github.com/zephyrproject-rtos/zephyr-lang-rust/commit/37dc7fac3fb0372bc0e78e022bef87fcce68c48d) |
| zscilib | [ee1b287d9dd07208d2cc52284240ac25bb66eae3](https://github.com/zephyrproject-rtos/zscilib/commit/ee1b287d9dd07208d2cc52284240ac25bb66eae3) |
| babblesim\_base | [153101c61ce7106f6ba8b108b5c6488efdc1151a](https://github.com/BabbleSim/base/commit/153101c61ce7106f6ba8b108b5c6488efdc1151a) |
| babblesim\_ext\_2G4\_channel\_NtNcable | [20a38c997f507b0aa53817aab3d73a462fff7af1](https://github.com/BabbleSim/ext_2G4_channel_NtNcable/commit/20a38c997f507b0aa53817aab3d73a462fff7af1) |
| babblesim\_ext\_2G4\_channel\_multiatt | [bde72a57384dde7a4310bcf3843469401be93074](https://github.com/BabbleSim/ext_2G4_channel_multiatt/commit/bde72a57384dde7a4310bcf3843469401be93074) |
| babblesim\_ext\_2G4\_device\_WLAN\_actmod | [9cb6d8e72695f6b785e57443f0629a18069d6ce4](https://github.com/BabbleSim/ext_2G4_device_WLAN_actmod/commit/9cb6d8e72695f6b785e57443f0629a18069d6ce4) |
| babblesim\_ext\_2G4\_device\_burst\_interferer | [5b5339351d6e6a2368c686c734dc8b2fc65698fc](https://github.com/BabbleSim/ext_2G4_device_burst_interferer/commit/5b5339351d6e6a2368c686c734dc8b2fc65698fc) |
| babblesim\_ext\_2G4\_device\_playback | [abb48cd71ddd4e2a9022f4bf49b2712524c483e8](https://github.com/BabbleSim/ext_2G4_device_playback/commit/abb48cd71ddd4e2a9022f4bf49b2712524c483e8) |
| babblesim\_ext\_2G4\_libPhyComv1 | [15ae0f87fa049e04cbec48a866f3bc37d903f950](https://github.com/BabbleSim/ext_2G4_libPhyComv1/commit/15ae0f87fa049e04cbec48a866f3bc37d903f950) |
| babblesim\_ext\_2G4\_modem\_BLE\_simple | [4d2379de510684cd4b1c3bbbb09bce7b5a20bc1f](https://github.com/BabbleSim/ext_2G4_modem_BLE_simple/commit/4d2379de510684cd4b1c3bbbb09bce7b5a20bc1f) |
| babblesim\_ext\_2G4\_modem\_magic | [edfcda2d3937a74be0a59d6cd47e0f50183453da](https://github.com/BabbleSim/ext_2G4_modem_magic/commit/edfcda2d3937a74be0a59d6cd47e0f50183453da) |
| babblesim\_ext\_2G4\_phy\_v1 | [62e797b2c518e5bb6123a198382ed2b64b8c068e](https://github.com/BabbleSim/ext_2G4_phy_v1/commit/62e797b2c518e5bb6123a198382ed2b64b8c068e) |
| babblesim\_ext\_libCryptov1 | [da246018ebe031e4fe4a8228187fb459e9f3b2fa](https://github.com/BabbleSim/ext_libCryptov1/commit/da246018ebe031e4fe4a8228187fb459e9f3b2fa) |
| bsim | [a88d3353451387ca490a6a7f7c478a90c4ee05b7](https://github.com/zephyrproject-rtos/babblesim-manifest/commit/a88d3353451387ca490a6a7f7c478a90c4ee05b7) |

## External Projects/Modules

The projects listed below are external and are not directly imported into the
default manifest.
To use any of the projects below, you will need to define your own manifest
file which includes them. See [Manifest Imports](../west/manifest.md#west-manifest-import) for information on
recommended ways to do this while still inheriting the mandatory modules from
Zephyr’s `west.yml`.

Use the template `doc/develop/manifest/external/external.rst.tmpl` to add
external modules to the list below:
