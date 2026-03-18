---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dai_8h.html
original_path: doxygen/html/dai_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dai.h File Reference

Public APIs for the DAI (Digital Audio Interface) bus drivers.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](dai_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [dai\_properties](structdai__properties.md) |
|  | DAI properties. [More...](structdai__properties.md#details) |
| struct | [dai\_config](structdai__config.md) |
|  | Main DAI config structure. [More...](structdai__config.md#details) |
| struct | [dai\_ts\_cfg](structdai__ts__cfg.md) |
|  | DAI timestamp configuration. [More...](structdai__ts__cfg.md#details) |
| struct | [dai\_ts\_data](structdai__ts__data.md) |
|  | DAI timestamp data. [More...](structdai__ts__data.md#details) |

| Macros | |
| --- | --- |
| #define | [DAI\_FORMAT\_CLOCK\_PROVIDER\_MASK](group__dai__interface.md#ga2a51e43f9a14435a64e428df0b393703)   0xf000 |
|  | Used to extract the clock configuration from the format attribute of struct [dai\_config](structdai__config.md "Main DAI config structure."). |
| #define | [DAI\_FORMAT\_PROTOCOL\_MASK](group__dai__interface.md#gaef86b295b1a13cc91e53f8cdbb4cf008)   0x000f |
|  | Used to extract the protocol from the format attribute of struct [dai\_config](structdai__config.md "Main DAI config structure."). |
| #define | [DAI\_FORMAT\_CLOCK\_INVERSION\_MASK](group__dai__interface.md#ga8891542769e33930342bb5039b57fda8)   0x0f00 |
|  | Used to extract the clock inversion from the format attribute of struct [dai\_config](structdai__config.md "Main DAI config structure."). |

| Enumerations | |
| --- | --- |
| enum | [dai\_clock\_provider](group__dai__interface.md#ga840116b8b56fd0263a17791e7156975d) { [DAI\_CBP\_CFP](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975da347440e41adadd2b6a91076f53abe2e3) = (0 << 12) , [DAI\_CBC\_CFP](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975daf4862a3af6fb46f6ac9ffc0cdbbcf0a1) = (2 << 12) , [DAI\_CBP\_CFC](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975da4baee3a3ab87e540b5f4caf26e8d8c4b) = (3 << 12) , [DAI\_CBC\_CFC](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975da9f8f99d63e607d9603f54d535bd89f84) = (4 << 12) } |
|  | DAI clock configurations. [More...](group__dai__interface.md#ga840116b8b56fd0263a17791e7156975d) |
| enum | [dai\_protocol](group__dai__interface.md#ga3fa4c114ad6a3dd6a6015b6ab3d119a2) {     [DAI\_PROTO\_I2S](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2adf515857c95ea685a32bf18c0ebb9af2) = 1 , [DAI\_PROTO\_RIGHT\_J](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a9ed5273ee9ea0761ccf9cbc7f7295a3f) , [DAI\_PROTO\_LEFT\_J](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a0d0f5db48e33cef8aa6c59a00792866b) , [DAI\_PROTO\_DSP\_A](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a6ffdc334c0f64feeb95297293f747bc3) ,     [DAI\_PROTO\_DSP\_B](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2aea1fd67c47f7d8d7e3ca18b2f2e806a0) , [DAI\_PROTO\_PDM](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a3235bf6888b65c9c6e3a0d2f95fc0758)   } |
|  | DAI protocol. [More...](group__dai__interface.md#ga3fa4c114ad6a3dd6a6015b6ab3d119a2) |
| enum | [dai\_clock\_inversion](group__dai__interface.md#gaf66ca0bbc1f8ba2f2b81caf92bd09b60) { [DAI\_INVERSION\_NB\_NF](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60a35606eb43c6d77204bff029bfab37698) = 0 , [DAI\_INVERSION\_NB\_IF](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ad6622f24986622cf16fdeada99356c43) = (2 << 8) , [DAI\_INVERSION\_IB\_NF](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ae0a56f8334363d4a1aa916ffe5d70e5c) = (3 << 8) , [DAI\_INVERSION\_IB\_IF](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ab35554010caadb69a5414c7f07649ee1) = (4 << 8) } |
|  | DAI clock inversion. [More...](group__dai__interface.md#gaf66ca0bbc1f8ba2f2b81caf92bd09b60) |
| enum | [dai\_type](group__dai__interface.md#gac95242d83a2c2b477fcb9eb3da420797) {     [DAI\_LEGACY\_I2S](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a2560d8f844796f647ed774748c44adfe) = 0 , [DAI\_INTEL\_SSP](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a9301e2ec67fa75aefc0e59df727adcc9) , [DAI\_INTEL\_DMIC](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a366db52bd49557d047f091cdb96b5e36) , [DAI\_INTEL\_HDA](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a1a591d4c0b7a70e175fc967b59929326) ,     [DAI\_INTEL\_ALH](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a19dd111b0d7f7772415bc60c1256d141) , [DAI\_IMX\_SAI](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797aa94ef995d95f9d0ad8b404e26b79faec) , [DAI\_IMX\_ESAI](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a75bfaa3859321a283929ae033fcf22aa) , [DAI\_AMD\_BT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a6c0c4b31c71c9e779a2a9325dc119fd0) ,     [DAI\_AMD\_SP](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797ab675d7b5204a2cbc09f1f60a44f4ff3b) , [DAI\_AMD\_DMIC](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a37f79dfe1804d4abeb89a9767bf37c75) , [DAI\_MEDIATEK\_AFE](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797ac5095e399162d248e638b87a61b59a00) , [DAI\_INTEL\_SSP\_NHLT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a8d75b1d72f5fcff348c15281001f9aaa) ,     [DAI\_INTEL\_DMIC\_NHLT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a3d759f9665a4db0c974913c4aa71e6f2) , [DAI\_INTEL\_HDA\_NHLT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797afd1f617fdd16363c1a10e9f45a67a99b) , [DAI\_INTEL\_ALH\_NHLT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a2a12c2858722c553cb31f24aacd83976)   } |
|  | Types of DAI. [More...](group__dai__interface.md#gac95242d83a2c2b477fcb9eb3da420797) |
| enum | [dai\_dir](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f) { [DAI\_DIR\_TX](group__dai__interface.md#ggafa7b22e4250c6479301fc657fea8a60fadfdf2212e2d86296dbccc60cfd60368c) = 0 , [DAI\_DIR\_RX](group__dai__interface.md#ggafa7b22e4250c6479301fc657fea8a60fa48cc817cda4907b94a03e13e8b9aa69b) , [DAI\_DIR\_BOTH](group__dai__interface.md#ggafa7b22e4250c6479301fc657fea8a60fa58581d875a6a8c28adb0f6351a37f3e1) } |
|  | DAI Direction. [More...](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f) |
| enum | [dai\_state](group__dai__interface.md#ga18f708594ea85d6b893906336047c3a5) {     [DAI\_STATE\_NOT\_READY](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a8486be6ff6f6bf91ee4a8ad632377987) = 0 , [DAI\_STATE\_READY](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a095422b1a71b65e5a5902e0ca5cd3650) , [DAI\_STATE\_RUNNING](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a8692bbb3fce619aec3dfe5ed9697f73f) , [DAI\_STATE\_PRE\_RUNNING](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a234306cd9cc97674455f8a9321834953) ,     [DAI\_STATE\_PAUSED](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5acb4e0c1f9df9eb0b7cf965b710a2ad13) , [DAI\_STATE\_STOPPING](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5aba10f89376d67abdc3dc704c6b283d2b) , [DAI\_STATE\_ERROR](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a5030da046fda46120d9b54a686fb35ef)   } |
|  | Interface state. [More...](group__dai__interface.md#ga18f708594ea85d6b893906336047c3a5) |
| enum | [dai\_trigger\_cmd](group__dai__interface.md#gaee6445967afb3ecf2c0470ca0c104a1a) {     [DAI\_TRIGGER\_START](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aabcbb4f151183d54d51dde07d09b3f222) = 0 , [DAI\_TRIGGER\_PRE\_START](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aac7647bb0111f043abcdaa4b3e703b2ec) , [DAI\_TRIGGER\_STOP](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa23dd7f534a18f92cbf12ad957674ba35) , [DAI\_TRIGGER\_PAUSE](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aadb17f3981cf0e248187c4006f527a3a5) ,     [DAI\_TRIGGER\_POST\_STOP](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aad2fcfa3c229bfc0a82ec7841ab9f88c3) , [DAI\_TRIGGER\_DRAIN](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa1c17da0f6a54c2c25f2dd2349b5c0e02) , [DAI\_TRIGGER\_DROP](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa1f004f7d4dcb67d2c3a89298400b2234) , [DAI\_TRIGGER\_PREPARE](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aad9d4e12f62ee2e106abaeb3bb341ee70) ,     [DAI\_TRIGGER\_RESET](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aafa607dff411961ae22e44f1a972c4711) , [DAI\_TRIGGER\_COPY](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa6720f67f3bc6ab62eacf986316df0a9f)   } |
|  | Trigger command. [More...](group__dai__interface.md#gaee6445967afb3ecf2c0470ca0c104a1a) |

| Functions | |
| --- | --- |
| static int | [dai\_probe](group__dai__interface.md#ga40d5fd2676a9195c07fd7382aa1cea4a) (const struct [device](structdevice.md) \*dev) |
|  | Probe operation of DAI driver. |
| static int | [dai\_remove](group__dai__interface.md#ga91482e349a735a927fa396f4636247e5) (const struct [device](structdevice.md) \*dev) |
|  | Remove operation of DAI driver. |
| static int | [dai\_config\_set](group__dai__interface.md#ga182f79eeaf83ba8936298fcc93ad760a) (const struct [device](structdevice.md) \*dev, const struct [dai\_config](structdai__config.md) \*cfg, const void \*bespoke\_cfg) |
|  | Configure operation of a DAI driver. |
| static int | [dai\_config\_get](group__dai__interface.md#gab093045778b0d0d1eee06e50e8c6481b) (const struct [device](structdevice.md) \*dev, struct [dai\_config](structdai__config.md) \*cfg, enum [dai\_dir](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f) dir) |
|  | Fetch configuration information of a DAI driver. |
| static const struct [dai\_properties](structdai__properties.md) \* | [dai\_get\_properties](group__dai__interface.md#gac732c8b3e737ecca187f38e308d95724) (const struct [device](structdevice.md) \*dev, enum [dai\_dir](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f) dir, int stream\_id) |
|  | Fetch properties of a DAI driver. |
| static int | [dai\_trigger](group__dai__interface.md#gabea217717edd2e986efeb475bbbc2208) (const struct [device](structdevice.md) \*dev, enum [dai\_dir](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f) dir, enum [dai\_trigger\_cmd](group__dai__interface.md#gaee6445967afb3ecf2c0470ca0c104a1a) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Send a trigger command. |
| static int | [dai\_ts\_config](group__dai__interface.md#gac401703e4054d1eeeaf619b295f5d6d8) (const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg) |
|  | Configures timestamping in attached DAI. |
| static int | [dai\_ts\_start](group__dai__interface.md#ga3dd0fd529c091d64dcb92d0c579a34ad) (const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg) |
|  | Starts timestamping. |
| static int | [dai\_ts\_stop](group__dai__interface.md#gaa3f2e59655c13101faf91ab2a6fd2f5e) (const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg) |
|  | Stops timestamping. |
| static int | [dai\_ts\_get](group__dai__interface.md#gaf6a4127a0edb48814aebf2f3fbaa3651) (const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg, struct [dai\_ts\_data](structdai__ts__data.md) \*tsd) |
|  | Gets timestamp. |

## Detailed Description

Public APIs for the DAI (Digital Audio Interface) bus drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dai.h](dai_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
