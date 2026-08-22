---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/develop/manifest/index.html
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
| cmsis | [512cc7e895e8491696b61f7ba8066b4a182569b8](https://github.com/zephyrproject-rtos/cmsis/commit/512cc7e895e8491696b61f7ba8066b4a182569b8) |
| cmsis-dsp | [d80a49b2bb186317dc1db4ac88da49c0ab77e6e7](https://github.com/zephyrproject-rtos/cmsis-dsp/commit/d80a49b2bb186317dc1db4ac88da49c0ab77e6e7) |
| cmsis-nn | [e9328d612ea3ea7d0d210d3ac16ea8667c01abdd](https://github.com/zephyrproject-rtos/cmsis-nn/commit/e9328d612ea3ea7d0d210d3ac16ea8667c01abdd) |
| cmsis\_6 | [06d952b6713a2ca41c9224a62075e4059402a151](https://github.com/zephyrproject-rtos/CMSIS_6/commit/06d952b6713a2ca41c9224a62075e4059402a151) |
| edtt | [b9ca3c7030518f07b7937dacf970d37a47865a76](https://github.com/zephyrproject-rtos/edtt/commit/b9ca3c7030518f07b7937dacf970d37a47865a76) |
| fatfs | [16245c7c41d2b79e74984f49b5202551786b8a9b](https://github.com/zephyrproject-rtos/fatfs/commit/16245c7c41d2b79e74984f49b5202551786b8a9b) |
| hal\_adi | [16829b77264678f31a2d077a870af7bdca2d39bd](https://github.com/zephyrproject-rtos/hal_adi/commit/16829b77264678f31a2d077a870af7bdca2d39bd) |
| hal\_afbr | [4e1eea7ea283db9d9ce529b0e9f89c0b5c2660e3](https://github.com/zephyrproject-rtos/hal_afbr/commit/4e1eea7ea283db9d9ce529b0e9f89c0b5c2660e3) |
| hal\_ambiq | [84ccbfc0b6041ba9f5688337c78bad99da5448ce](https://github.com/zephyrproject-rtos/hal_ambiq/commit/84ccbfc0b6041ba9f5688337c78bad99da5448ce) |
| hal\_atmel | [ca7e4c6920f44b9d677ed5995ffa169f18a54cdf](https://github.com/zephyrproject-rtos/hal_atmel/commit/ca7e4c6920f44b9d677ed5995ffa169f18a54cdf) |
| hal\_bouffalolab | [5811738e2be348f30dc97d78280f2735d5d14084](https://github.com/zephyrproject-rtos/hal_bouffalolab/commit/5811738e2be348f30dc97d78280f2735d5d14084) |
| hal\_espressif | [f3453bdeced28642424692aae32cce4eec3f2d7f](https://github.com/zephyrproject-rtos/hal_espressif/commit/f3453bdeced28642424692aae32cce4eec3f2d7f) |
| hal\_ethos\_u | [50ddffca1cc700112f25ad9bc077915a0355ee5d](https://github.com/zephyrproject-rtos/hal_ethos_u/commit/50ddffca1cc700112f25ad9bc077915a0355ee5d) |
| hal\_gigadevice | [2994b7dde8b0b0fa9b9c0ccb13474b6a486cddc3](https://github.com/zephyrproject-rtos/hal_gigadevice/commit/2994b7dde8b0b0fa9b9c0ccb13474b6a486cddc3) |
| hal\_infineon | [1030915af885cffc8cedc49a62291dd279a9e81e](https://github.com/zephyrproject-rtos/hal_infineon/commit/1030915af885cffc8cedc49a62291dd279a9e81e) |
| hal\_intel | [0447cd22e74d7ca243653f21cfd6e38c016630c6](https://github.com/zephyrproject-rtos/hal_intel/commit/0447cd22e74d7ca243653f21cfd6e38c016630c6) |
| hal\_microchip | [32a79d481c056b2204a5701d5a5799f9e5130dd7](https://github.com/zephyrproject-rtos/hal_microchip/commit/32a79d481c056b2204a5701d5a5799f9e5130dd7) |
| hal\_nordic | [9587b1dcb83d24ab74e89837843a5f7d573f7059](https://github.com/zephyrproject-rtos/hal_nordic/commit/9587b1dcb83d24ab74e89837843a5f7d573f7059) |
| hal\_nuvoton | [be1042dc8a96ebe9ea4c5d714f07c617539106d6](https://github.com/zephyrproject-rtos/hal_nuvoton/commit/be1042dc8a96ebe9ea4c5d714f07c617539106d6) |
| hal\_nxp | [7a52cbb7cb56db3a276cbd617db3ea7cc3435d12](https://github.com/zephyrproject-rtos/hal_nxp/commit/7a52cbb7cb56db3a276cbd617db3ea7cc3435d12) |
| hal\_openisa | [eabd530a64d71de91d907bad257cd61aacf607bc](https://github.com/zephyrproject-rtos/hal_openisa/commit/eabd530a64d71de91d907bad257cd61aacf607bc) |
| hal\_quicklogic | [bad894440fe72c814864798c8e3a76d13edffb6c](https://github.com/zephyrproject-rtos/hal_quicklogic/commit/bad894440fe72c814864798c8e3a76d13edffb6c) |
| hal\_renesas | [0769fe1520f6c14e6301188588da758a609f181d](https://github.com/zephyrproject-rtos/hal_renesas/commit/0769fe1520f6c14e6301188588da758a609f181d) |
| hal\_rpi\_pico | [7b57b24588797e6e7bf18b6bda168e6b96374264](https://github.com/zephyrproject-rtos/hal_rpi_pico/commit/7b57b24588797e6e7bf18b6bda168e6b96374264) |
| hal\_silabs | [190a144a16bed9a938a94543ed5bbc70c0552e0f](https://github.com/zephyrproject-rtos/hal_silabs/commit/190a144a16bed9a938a94543ed5bbc70c0552e0f) |
| hal\_st | [9f81b4427e955885398805b7bca0da3a8cd9109c](https://github.com/zephyrproject-rtos/hal_st/commit/9f81b4427e955885398805b7bca0da3a8cd9109c) |
| hal\_stm32 | [1e753266ddfb4b07a8a0b1ec566e9637ea45d5ef](https://github.com/zephyrproject-rtos/hal_stm32/commit/1e753266ddfb4b07a8a0b1ec566e9637ea45d5ef) |
| hal\_tdk | [6727477af1e46fa43878102489b9672a9d24e39f](https://github.com/zephyrproject-rtos/hal_tdk/commit/6727477af1e46fa43878102489b9672a9d24e39f) |
| hal\_telink | [4226c7fc17d5a34e557d026d428fc766191a0800](https://github.com/zephyrproject-rtos/hal_telink/commit/4226c7fc17d5a34e557d026d428fc766191a0800) |
| hal\_ti | [bc8e7b99bb668cc51a3aa384448a48c48a33f8e2](https://github.com/zephyrproject-rtos/hal_ti/commit/bc8e7b99bb668cc51a3aa384448a48c48a33f8e2) |
| hal\_wch | [6dd313768b5f4cc69baeac4ce6e59f2038eb8ce5](https://github.com/zephyrproject-rtos/hal_wch/commit/6dd313768b5f4cc69baeac4ce6e59f2038eb8ce5) |
| hal\_wurthelektronik | [e3e2797b224fc48fdef1bc3e5a12a7c73108bba2](https://github.com/zephyrproject-rtos/hal_wurthelektronik/commit/e3e2797b224fc48fdef1bc3e5a12a7c73108bba2) |
| hal\_xtensa | [b38620c7cc61e349e192ed86a54940a5cd0636b7](https://github.com/zephyrproject-rtos/hal_xtensa/commit/b38620c7cc61e349e192ed86a54940a5cd0636b7) |
| hostap | [e942f86e865d5b24bbbe8b0c333f030cbbe62bfb](https://github.com/zephyrproject-rtos/hostap/commit/e942f86e865d5b24bbbe8b0c333f030cbbe62bfb) |
| liblc3 | [48bbd3eacd36e99a57317a0a4867002e0b09e183](https://github.com/zephyrproject-rtos/liblc3/commit/48bbd3eacd36e99a57317a0a4867002e0b09e183) |
| libmctp | [b97860e78998551af99931ece149eeffc538bdb1](https://github.com/zephyrproject-rtos/libmctp/commit/b97860e78998551af99931ece149eeffc538bdb1) |
| libmetal | [91d38634d1882f0a2151966f8c5c230ce1c0de7b](https://github.com/zephyrproject-rtos/libmetal/commit/91d38634d1882f0a2151966f8c5c230ce1c0de7b) |
| littlefs | [8f5ca347843363882619d8f96c00d8dbd88a8e79](https://github.com/zephyrproject-rtos/littlefs/commit/8f5ca347843363882619d8f96c00d8dbd88a8e79) |
| loramac-node | [fb00b383072518c918e2258b0916c996f2d4eebe](https://github.com/zephyrproject-rtos/loramac-node/commit/fb00b383072518c918e2258b0916c996f2d4eebe) |
| lvgl | [b03edc8e6282a963cd312cd0b409eb5ce263ea75](https://github.com/zephyrproject-rtos/lvgl/commit/b03edc8e6282a963cd312cd0b409eb5ce263ea75) |
| mbedtls | [85440ef5fffa95d0e9971e9163719189cf34d979](https://github.com/zephyrproject-rtos/mbedtls/commit/85440ef5fffa95d0e9971e9163719189cf34d979) |
| mcuboot | [4eba8087fa606db801455f14d185255bc8c49467](https://github.com/zephyrproject-rtos/mcuboot/commit/4eba8087fa606db801455f14d185255bc8c49467) |
| mipi-sys-t | [33e5c23cbedda5ba12dbe50c4baefb362a791001](https://github.com/zephyrproject-rtos/mipi-sys-t/commit/33e5c23cbedda5ba12dbe50c4baefb362a791001) |
| net-tools | [986bfeb040df3d9029366de8aea4ce1f84e93780](https://github.com/zephyrproject-rtos/net-tools/commit/986bfeb040df3d9029366de8aea4ce1f84e93780) |
| nrf\_hw\_models | [6e5961223f81aa2707c555db138819a5c1b7942c](https://github.com/zephyrproject-rtos/nrf_hw_models/commit/6e5961223f81aa2707c555db138819a5c1b7942c) |
| nrf\_wifi | [5f59c2336c69f28ae83f93812a1d726f9fceabfe](https://github.com/zephyrproject-rtos/nrf_wifi/commit/5f59c2336c69f28ae83f93812a1d726f9fceabfe) |
| open-amp | [c30a6d8b92fcebdb797fc1a7698e8729e250f637](https://github.com/zephyrproject-rtos/open-amp/commit/c30a6d8b92fcebdb797fc1a7698e8729e250f637) |
| openthread | [3ae741f95e7dfb391dec35c48742862049eb62e8](https://github.com/zephyrproject-rtos/openthread/commit/3ae741f95e7dfb391dec35c48742862049eb62e8) |
| percepio | [49e6dc202aa38c2a3edbafcc2dab85dec6aee973](https://github.com/zephyrproject-rtos/percepio/commit/49e6dc202aa38c2a3edbafcc2dab85dec6aee973) |
| picolibc | [560946f26db075c296beea5b39d99e6de43c9010](https://github.com/zephyrproject-rtos/picolibc/commit/560946f26db075c296beea5b39d99e6de43c9010) |
| segger | [cf56b1d9c80f81a26e2ac5727c9cf177116a4692](https://github.com/zephyrproject-rtos/segger/commit/cf56b1d9c80f81a26e2ac5727c9cf177116a4692) |
| tinycrypt | [1012a3ebee18c15ede5efc8332ee2fc37817670f](https://github.com/zephyrproject-rtos/tinycrypt/commit/1012a3ebee18c15ede5efc8332ee2fc37817670f) |
| trusted-firmware-a | [713ffbf96c5bcbdeab757423f10f73eb304eff07](https://github.com/zephyrproject-rtos/trusted-firmware-a/commit/713ffbf96c5bcbdeab757423f10f73eb304eff07) |
| trusted-firmware-m | [021e2bbd50c215e41710a72e05abce3224f074a7](https://github.com/zephyrproject-rtos/trusted-firmware-m/commit/021e2bbd50c215e41710a72e05abce3224f074a7) |
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
| tf-m-tests | [a286347e6a5dd37a9a5e960450ffc0260d63fb27](https://github.com/zephyrproject-rtos/tf-m-tests/commit/a286347e6a5dd37a9a5e960450ffc0260d63fb27) |
| tflite-micro | [8d404de73acf7687831e16d88e86e4f73cfddf8e](https://github.com/zephyrproject-rtos/tflite-micro/commit/8d404de73acf7687831e16d88e86e4f73cfddf8e) |
| thrift | [10023645a0e6cb7ce23fcd7fd3dbac9f18df6234](https://github.com/zephyrproject-rtos/thrift/commit/10023645a0e6cb7ce23fcd7fd3dbac9f18df6234) |
| zephyr-lang-rust | [dd73abc242e995784da62352fe8c70d9a6c7ac2e](https://github.com/zephyrproject-rtos/zephyr-lang-rust/commit/dd73abc242e995784da62352fe8c70d9a6c7ac2e) |
| zscilib | [ee3c0c405087e331aad16d167b6e4ec1c3452ba9](https://github.com/zephyrproject-rtos/zscilib/commit/ee3c0c405087e331aad16d167b6e4ec1c3452ba9) |
| babblesim\_base | [2cfac3dca2071452ae481d115d8541880568753d](https://github.com/BabbleSim/base/commit/2cfac3dca2071452ae481d115d8541880568753d) |
| babblesim\_ext\_2G4\_channel\_NtNcable | [20a38c997f507b0aa53817aab3d73a462fff7af1](https://github.com/BabbleSim/ext_2G4_channel_NtNcable/commit/20a38c997f507b0aa53817aab3d73a462fff7af1) |
| babblesim\_ext\_2G4\_channel\_multiatt | [bde72a57384dde7a4310bcf3843469401be93074](https://github.com/BabbleSim/ext_2G4_channel_multiatt/commit/bde72a57384dde7a4310bcf3843469401be93074) |
| babblesim\_ext\_2G4\_device\_WLAN\_actmod | [9cb6d8e72695f6b785e57443f0629a18069d6ce4](https://github.com/BabbleSim/ext_2G4_device_WLAN_actmod/commit/9cb6d8e72695f6b785e57443f0629a18069d6ce4) |
| babblesim\_ext\_2G4\_device\_burst\_interferer | [5b5339351d6e6a2368c686c734dc8b2fc65698fc](https://github.com/BabbleSim/ext_2G4_device_burst_interferer/commit/5b5339351d6e6a2368c686c734dc8b2fc65698fc) |
| babblesim\_ext\_2G4\_device\_playback | [abb48cd71ddd4e2a9022f4bf49b2712524c483e8](https://github.com/BabbleSim/ext_2G4_device_playback/commit/abb48cd71ddd4e2a9022f4bf49b2712524c483e8) |
| babblesim\_ext\_2G4\_libPhyComv1 | [e18e41e8e3fa9f996559ed98b9238a5702dcdd36](https://github.com/BabbleSim/ext_2G4_libPhyComv1/commit/e18e41e8e3fa9f996559ed98b9238a5702dcdd36) |
| babblesim\_ext\_2G4\_modem\_BLE\_simple | [4d2379de510684cd4b1c3bbbb09bce7b5a20bc1f](https://github.com/BabbleSim/ext_2G4_modem_BLE_simple/commit/4d2379de510684cd4b1c3bbbb09bce7b5a20bc1f) |
| babblesim\_ext\_2G4\_modem\_magic | [edfcda2d3937a74be0a59d6cd47e0f50183453da](https://github.com/BabbleSim/ext_2G4_modem_magic/commit/edfcda2d3937a74be0a59d6cd47e0f50183453da) |
| babblesim\_ext\_2G4\_phy\_v1 | [8964ed1eb94606c2ea555340907bdc5171793e65](https://github.com/BabbleSim/ext_2G4_phy_v1/commit/8964ed1eb94606c2ea555340907bdc5171793e65) |
| babblesim\_ext\_libCryptov1 | [da246018ebe031e4fe4a8228187fb459e9f3b2fa](https://github.com/BabbleSim/ext_libCryptov1/commit/da246018ebe031e4fe4a8228187fb459e9f3b2fa) |
| bsim | [2ba22a0608ad9f46da1b96ee5121af357053c791](https://github.com/zephyrproject-rtos/babblesim-manifest/commit/2ba22a0608ad9f46da1b96ee5121af357053c791) |

## External Projects/Modules

The projects listed below are external and are not directly imported into the
default manifest.
To use any of the projects below, you will need to define your own manifest
file which includes them. See [Manifest Imports](../west/manifest.md#west-manifest-import) for information on
recommended ways to do this while still inheriting the mandatory modules from
Zephyr’s `west.yml`.

Use the template `doc/develop/manifest/external/external.rst.tmpl` to add
external modules to the list below:
