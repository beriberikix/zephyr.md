---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__dai__interface.html
original_path: doxygen/html/group__dai__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

DAI Interface

[Device Driver APIs](group__io__interfaces.md)

DAI Interface.
[More...](#details)

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
| #define | [DAI\_FORMAT\_CLOCK\_PROVIDER\_MASK](#ga2a51e43f9a14435a64e428df0b393703)   0xf000 |
|  | Used to extract the clock configuration from the format attribute of struct [dai\_config](structdai__config.md "Main DAI config structure."). |
| #define | [DAI\_FORMAT\_PROTOCOL\_MASK](#gaef86b295b1a13cc91e53f8cdbb4cf008)   0x000f |
|  | Used to extract the protocol from the format attribute of struct [dai\_config](structdai__config.md "Main DAI config structure."). |
| #define | [DAI\_FORMAT\_CLOCK\_INVERSION\_MASK](#ga8891542769e33930342bb5039b57fda8)   0x0f00 |
|  | Used to extract the clock inversion from the format attribute of struct [dai\_config](structdai__config.md "Main DAI config structure."). |

| Enumerations | |
| --- | --- |
| enum | [dai\_clock\_provider](#ga840116b8b56fd0263a17791e7156975d) { [DAI\_CBP\_CFP](#gga840116b8b56fd0263a17791e7156975da347440e41adadd2b6a91076f53abe2e3) = (0 << 12) , [DAI\_CBC\_CFP](#gga840116b8b56fd0263a17791e7156975daf4862a3af6fb46f6ac9ffc0cdbbcf0a1) = (2 << 12) , [DAI\_CBP\_CFC](#gga840116b8b56fd0263a17791e7156975da4baee3a3ab87e540b5f4caf26e8d8c4b) = (3 << 12) , [DAI\_CBC\_CFC](#gga840116b8b56fd0263a17791e7156975da9f8f99d63e607d9603f54d535bd89f84) = (4 << 12) } |
|  | DAI clock configurations. [More...](#ga840116b8b56fd0263a17791e7156975d) |
| enum | [dai\_protocol](#ga3fa4c114ad6a3dd6a6015b6ab3d119a2) {     [DAI\_PROTO\_I2S](#gga3fa4c114ad6a3dd6a6015b6ab3d119a2adf515857c95ea685a32bf18c0ebb9af2) = 1 , [DAI\_PROTO\_RIGHT\_J](#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a9ed5273ee9ea0761ccf9cbc7f7295a3f) , [DAI\_PROTO\_LEFT\_J](#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a0d0f5db48e33cef8aa6c59a00792866b) , [DAI\_PROTO\_DSP\_A](#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a6ffdc334c0f64feeb95297293f747bc3) ,     [DAI\_PROTO\_DSP\_B](#gga3fa4c114ad6a3dd6a6015b6ab3d119a2aea1fd67c47f7d8d7e3ca18b2f2e806a0) , [DAI\_PROTO\_PDM](#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a3235bf6888b65c9c6e3a0d2f95fc0758)   } |
|  | DAI protocol. [More...](#ga3fa4c114ad6a3dd6a6015b6ab3d119a2) |
| enum | [dai\_clock\_inversion](#gaf66ca0bbc1f8ba2f2b81caf92bd09b60) { [DAI\_INVERSION\_NB\_NF](#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60a35606eb43c6d77204bff029bfab37698) = 0 , [DAI\_INVERSION\_NB\_IF](#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ad6622f24986622cf16fdeada99356c43) = (2 << 8) , [DAI\_INVERSION\_IB\_NF](#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ae0a56f8334363d4a1aa916ffe5d70e5c) = (3 << 8) , [DAI\_INVERSION\_IB\_IF](#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ab35554010caadb69a5414c7f07649ee1) = (4 << 8) } |
|  | DAI clock inversion. [More...](#gaf66ca0bbc1f8ba2f2b81caf92bd09b60) |
| enum | [dai\_type](#gac95242d83a2c2b477fcb9eb3da420797) {     [DAI\_LEGACY\_I2S](#ggac95242d83a2c2b477fcb9eb3da420797a2560d8f844796f647ed774748c44adfe) = 0 , [DAI\_INTEL\_SSP](#ggac95242d83a2c2b477fcb9eb3da420797a9301e2ec67fa75aefc0e59df727adcc9) , [DAI\_INTEL\_DMIC](#ggac95242d83a2c2b477fcb9eb3da420797a366db52bd49557d047f091cdb96b5e36) , [DAI\_INTEL\_HDA](#ggac95242d83a2c2b477fcb9eb3da420797a1a591d4c0b7a70e175fc967b59929326) ,     [DAI\_INTEL\_ALH](#ggac95242d83a2c2b477fcb9eb3da420797a19dd111b0d7f7772415bc60c1256d141) , [DAI\_IMX\_SAI](#ggac95242d83a2c2b477fcb9eb3da420797aa94ef995d95f9d0ad8b404e26b79faec) , [DAI\_IMX\_ESAI](#ggac95242d83a2c2b477fcb9eb3da420797a75bfaa3859321a283929ae033fcf22aa) , [DAI\_AMD\_BT](#ggac95242d83a2c2b477fcb9eb3da420797a6c0c4b31c71c9e779a2a9325dc119fd0) ,     [DAI\_AMD\_SP](#ggac95242d83a2c2b477fcb9eb3da420797ab675d7b5204a2cbc09f1f60a44f4ff3b) , [DAI\_AMD\_DMIC](#ggac95242d83a2c2b477fcb9eb3da420797a37f79dfe1804d4abeb89a9767bf37c75) , [DAI\_MEDIATEK\_AFE](#ggac95242d83a2c2b477fcb9eb3da420797ac5095e399162d248e638b87a61b59a00) , [DAI\_INTEL\_SSP\_NHLT](#ggac95242d83a2c2b477fcb9eb3da420797a8d75b1d72f5fcff348c15281001f9aaa) ,     [DAI\_INTEL\_DMIC\_NHLT](#ggac95242d83a2c2b477fcb9eb3da420797a3d759f9665a4db0c974913c4aa71e6f2) , [DAI\_INTEL\_HDA\_NHLT](#ggac95242d83a2c2b477fcb9eb3da420797afd1f617fdd16363c1a10e9f45a67a99b) , [DAI\_INTEL\_ALH\_NHLT](#ggac95242d83a2c2b477fcb9eb3da420797a2a12c2858722c553cb31f24aacd83976)   } |
|  | Types of DAI. [More...](#gac95242d83a2c2b477fcb9eb3da420797) |
| enum | [dai\_dir](#gafa7b22e4250c6479301fc657fea8a60f) { [DAI\_DIR\_TX](#ggafa7b22e4250c6479301fc657fea8a60fadfdf2212e2d86296dbccc60cfd60368c) = 0 , [DAI\_DIR\_RX](#ggafa7b22e4250c6479301fc657fea8a60fa48cc817cda4907b94a03e13e8b9aa69b) , [DAI\_DIR\_BOTH](#ggafa7b22e4250c6479301fc657fea8a60fa58581d875a6a8c28adb0f6351a37f3e1) } |
|  | DAI Direction. [More...](#gafa7b22e4250c6479301fc657fea8a60f) |
| enum | [dai\_state](#ga18f708594ea85d6b893906336047c3a5) {     [DAI\_STATE\_NOT\_READY](#gga18f708594ea85d6b893906336047c3a5a8486be6ff6f6bf91ee4a8ad632377987) = 0 , [DAI\_STATE\_READY](#gga18f708594ea85d6b893906336047c3a5a095422b1a71b65e5a5902e0ca5cd3650) , [DAI\_STATE\_RUNNING](#gga18f708594ea85d6b893906336047c3a5a8692bbb3fce619aec3dfe5ed9697f73f) , [DAI\_STATE\_PRE\_RUNNING](#gga18f708594ea85d6b893906336047c3a5a234306cd9cc97674455f8a9321834953) ,     [DAI\_STATE\_PAUSED](#gga18f708594ea85d6b893906336047c3a5acb4e0c1f9df9eb0b7cf965b710a2ad13) , [DAI\_STATE\_STOPPING](#gga18f708594ea85d6b893906336047c3a5aba10f89376d67abdc3dc704c6b283d2b) , [DAI\_STATE\_ERROR](#gga18f708594ea85d6b893906336047c3a5a5030da046fda46120d9b54a686fb35ef)   } |
|  | Interface state. [More...](#ga18f708594ea85d6b893906336047c3a5) |
| enum | [dai\_trigger\_cmd](#gaee6445967afb3ecf2c0470ca0c104a1a) {     [DAI\_TRIGGER\_START](#ggaee6445967afb3ecf2c0470ca0c104a1aabcbb4f151183d54d51dde07d09b3f222) = 0 , [DAI\_TRIGGER\_PRE\_START](#ggaee6445967afb3ecf2c0470ca0c104a1aac7647bb0111f043abcdaa4b3e703b2ec) , [DAI\_TRIGGER\_STOP](#ggaee6445967afb3ecf2c0470ca0c104a1aa23dd7f534a18f92cbf12ad957674ba35) , [DAI\_TRIGGER\_PAUSE](#ggaee6445967afb3ecf2c0470ca0c104a1aadb17f3981cf0e248187c4006f527a3a5) ,     [DAI\_TRIGGER\_POST\_STOP](#ggaee6445967afb3ecf2c0470ca0c104a1aad2fcfa3c229bfc0a82ec7841ab9f88c3) , [DAI\_TRIGGER\_DRAIN](#ggaee6445967afb3ecf2c0470ca0c104a1aa1c17da0f6a54c2c25f2dd2349b5c0e02) , [DAI\_TRIGGER\_DROP](#ggaee6445967afb3ecf2c0470ca0c104a1aa1f004f7d4dcb67d2c3a89298400b2234) , [DAI\_TRIGGER\_PREPARE](#ggaee6445967afb3ecf2c0470ca0c104a1aad9d4e12f62ee2e106abaeb3bb341ee70) ,     [DAI\_TRIGGER\_RESET](#ggaee6445967afb3ecf2c0470ca0c104a1aafa607dff411961ae22e44f1a972c4711) , [DAI\_TRIGGER\_COPY](#ggaee6445967afb3ecf2c0470ca0c104a1aa6720f67f3bc6ab62eacf986316df0a9f)   } |
|  | Trigger command. [More...](#gaee6445967afb3ecf2c0470ca0c104a1a) |

| Functions | |
| --- | --- |
| static int | [dai\_probe](#ga40d5fd2676a9195c07fd7382aa1cea4a) (const struct [device](structdevice.md) \*dev) |
|  | Probe operation of DAI driver. |
| static int | [dai\_remove](#ga91482e349a735a927fa396f4636247e5) (const struct [device](structdevice.md) \*dev) |
|  | Remove operation of DAI driver. |
| static int | [dai\_config\_set](#ga182f79eeaf83ba8936298fcc93ad760a) (const struct [device](structdevice.md) \*dev, const struct [dai\_config](structdai__config.md) \*cfg, const void \*bespoke\_cfg) |
|  | Configure operation of a DAI driver. |
| static int | [dai\_config\_get](#gab093045778b0d0d1eee06e50e8c6481b) (const struct [device](structdevice.md) \*dev, struct [dai\_config](structdai__config.md) \*cfg, enum [dai\_dir](#gafa7b22e4250c6479301fc657fea8a60f) dir) |
|  | Fetch configuration information of a DAI driver. |
| static const struct [dai\_properties](structdai__properties.md) \* | [dai\_get\_properties](#gac732c8b3e737ecca187f38e308d95724) (const struct [device](structdevice.md) \*dev, enum [dai\_dir](#gafa7b22e4250c6479301fc657fea8a60f) dir, int stream\_id) |
|  | Fetch properties of a DAI driver. |
| static int | [dai\_trigger](#gabea217717edd2e986efeb475bbbc2208) (const struct [device](structdevice.md) \*dev, enum [dai\_dir](#gafa7b22e4250c6479301fc657fea8a60f) dir, enum [dai\_trigger\_cmd](#gaee6445967afb3ecf2c0470ca0c104a1a) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Send a trigger command. |
| static int | [dai\_ts\_config](#gac401703e4054d1eeeaf619b295f5d6d8) (const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg) |
|  | Configures timestamping in attached DAI. |
| static int | [dai\_ts\_start](#ga3dd0fd529c091d64dcb92d0c579a34ad) (const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg) |
|  | Starts timestamping. |
| static int | [dai\_ts\_stop](#gaa3f2e59655c13101faf91ab2a6fd2f5e) (const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg) |
|  | Stops timestamping. |
| static int | [dai\_ts\_get](#gaf6a4127a0edb48814aebf2f3fbaa3651) (const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg, struct [dai\_ts\_data](structdai__ts__data.md) \*tsd) |
|  | Gets timestamp. |

## Detailed Description

DAI Interface.

The DAI API provides support for the standard I2S (SSP) and its common variants. It supports also DMIC, HDA and SDW backends. The API has a config function with bespoke data argument for device/vendor specific config. There are also optional timestamping functions to get device specific audio clock time.

## Macro Definition Documentation

## [◆ ](#ga8891542769e33930342bb5039b57fda8)DAI\_FORMAT\_CLOCK\_INVERSION\_MASK

| #define DAI\_FORMAT\_CLOCK\_INVERSION\_MASK   0x0f00 |
| --- |

`#include <[dai.h](dai_8h.md)>`

Used to extract the clock inversion from the format attribute of struct [dai\_config](structdai__config.md "Main DAI config structure.").

## [◆ ](#ga2a51e43f9a14435a64e428df0b393703)DAI\_FORMAT\_CLOCK\_PROVIDER\_MASK

| #define DAI\_FORMAT\_CLOCK\_PROVIDER\_MASK   0xf000 |
| --- |

`#include <[dai.h](dai_8h.md)>`

Used to extract the clock configuration from the format attribute of struct [dai\_config](structdai__config.md "Main DAI config structure.").

## [◆ ](#gaef86b295b1a13cc91e53f8cdbb4cf008)DAI\_FORMAT\_PROTOCOL\_MASK

| #define DAI\_FORMAT\_PROTOCOL\_MASK   0x000f |
| --- |

`#include <[dai.h](dai_8h.md)>`

Used to extract the protocol from the format attribute of struct [dai\_config](structdai__config.md "Main DAI config structure.").

## Enumeration Type Documentation

## [◆ ](#gaf66ca0bbc1f8ba2f2b81caf92bd09b60)dai\_clock\_inversion

| enum [dai\_clock\_inversion](#gaf66ca0bbc1f8ba2f2b81caf92bd09b60) |
| --- |

`#include <[dai.h](dai_8h.md)>`

DAI clock inversion.

Some applications may require a different clock polarity (FSYNC/BCLK) compared to the default one chosen based on the protocol.

| Enumerator | |
| --- | --- |
| DAI\_INVERSION\_NB\_NF | no BCLK inversion, no FSYNC inversion  no BCLK inversion, FSYNC inversion |
| DAI\_INVERSION\_NB\_IF | BCLK inversion, no FSYNC inversion. |
| DAI\_INVERSION\_IB\_NF | BCLK inversion, FSYNC inversion. |
| DAI\_INVERSION\_IB\_IF |  |

## [◆ ](#ga840116b8b56fd0263a17791e7156975d)dai\_clock\_provider

| enum [dai\_clock\_provider](#ga840116b8b56fd0263a17791e7156975d) |
| --- |

`#include <[dai.h](dai_8h.md)>`

DAI clock configurations.

This is used to describe all of the possible clock-related configurations w.r.t the DAI and the codec.

| Enumerator | |
| --- | --- |
| DAI\_CBP\_CFP | codec BLCK provider, codec FSYNC provider  codec BCLK consumer, codec FSYNC provider |
| DAI\_CBC\_CFP | codec BCLK provider, codec FSYNC consumer |
| DAI\_CBP\_CFC | codec BCLK consumer, codec FSYNC consumer |
| DAI\_CBC\_CFC |  |

## [◆ ](#gafa7b22e4250c6479301fc657fea8a60f)dai\_dir

| enum [dai\_dir](#gafa7b22e4250c6479301fc657fea8a60f) |
| --- |

`#include <[dai.h](dai_8h.md)>`

DAI Direction.

| Enumerator | |
| --- | --- |
| DAI\_DIR\_TX | Transmit data. |
| DAI\_DIR\_RX | Receive data. |
| DAI\_DIR\_BOTH | Both receive and transmit data. |

## [◆ ](#ga3fa4c114ad6a3dd6a6015b6ab3d119a2)dai\_protocol

| enum [dai\_protocol](#ga3fa4c114ad6a3dd6a6015b6ab3d119a2) |
| --- |

`#include <[dai.h](dai_8h.md)>`

DAI protocol.

The communication between the DAI and the CODEC may use different protocols depending on the scenario.

| Enumerator | |
| --- | --- |
| DAI\_PROTO\_I2S | I2S. |
| DAI\_PROTO\_RIGHT\_J | Right Justified. |
| DAI\_PROTO\_LEFT\_J | Left Justified. |
| DAI\_PROTO\_DSP\_A | TDM, FSYNC asserted 1 BCLK early. |
| DAI\_PROTO\_DSP\_B | TDM, FSYNC asserted at the same time as MSB. |
| DAI\_PROTO\_PDM | Pulse Density Modulation. |

## [◆ ](#ga18f708594ea85d6b893906336047c3a5)dai\_state

| enum [dai\_state](#ga18f708594ea85d6b893906336047c3a5) |
| --- |

`#include <[dai.h](dai_8h.md)>`

Interface state.

| Enumerator | |
| --- | --- |
| DAI\_STATE\_NOT\_READY | The interface is not ready.  The interface was initialized but is not yet ready to receive / transmit data. Call [dai\_config\_set()](#ga182f79eeaf83ba8936298fcc93ad760a) to configure interface and change its state to READY. |
| DAI\_STATE\_READY | The interface is ready to receive / transmit data. |
| DAI\_STATE\_RUNNING | The interface is receiving / transmitting data. |
| DAI\_STATE\_PRE\_RUNNING | The interface is clocking but not receiving / transmitting data. |
| DAI\_STATE\_PAUSED | The interface paused. |
| DAI\_STATE\_STOPPING | The interface is draining its transmit queue. |
| DAI\_STATE\_ERROR | TX buffer underrun or RX buffer overrun has occurred. |

## [◆ ](#gaee6445967afb3ecf2c0470ca0c104a1a)dai\_trigger\_cmd

| enum [dai\_trigger\_cmd](#gaee6445967afb3ecf2c0470ca0c104a1a) |
| --- |

`#include <[dai.h](dai_8h.md)>`

Trigger command.

| Enumerator | |
| --- | --- |
| DAI\_TRIGGER\_START | Start the transmission / reception of data.  If DAI\_DIR\_TX is set some data has to be queued for transmission by the dai\_write() function. This trigger can be used in READY state only and changes the interface state to RUNNING. |
| DAI\_TRIGGER\_PRE\_START | Optional - Pre Start the transmission / reception of data.  Allows the DAI and downstream codecs to prepare for audio Tx/Rx by starting any required clocks for downstream PLL/FLL locking. |
| DAI\_TRIGGER\_STOP | Stop the transmission / reception of data.  Stop the transmission / reception of data at the end of the current memory block. This trigger can be used in RUNNING state only and at first changes the interface state to STOPPING. When the current TX / RX block is transmitted / received the state is changed to READY. Subsequent START trigger will resume transmission / reception where it stopped. |
| DAI\_TRIGGER\_PAUSE | Pause the transmission / reception of data.  Pause the transmission / reception of data at the end of the current memory block. Behavior is implementation specific but usually this state doesn't completely stop the clocks or transmission. The DAI could be transmitting 0's (silence), but it is not consuming data from outside. |
| DAI\_TRIGGER\_POST\_STOP | Optional - Post Stop the transmission / reception of data.  Allows the DAI and downstream codecs to shutdown cleanly after audio Tx/Rx by stopping any required clocks for downstream audio completion. |
| DAI\_TRIGGER\_DRAIN | Empty the transmit queue.  Send all data in the transmit queue and stop the transmission. If the trigger is applied to the RX queue it has the same effect as DAI\_TRIGGER\_STOP. This trigger can be used in RUNNING state only and at first changes the interface state to STOPPING. When all TX blocks are transmitted the state is changed to READY. |
| DAI\_TRIGGER\_DROP | Discard the transmit / receive queue.  Stop the transmission / reception immediately and discard the contents of the respective queue. This trigger can be used in any state other than NOT\_READY and changes the interface state to READY. |
| DAI\_TRIGGER\_PREPARE | Prepare the queues after underrun/overrun error has occurred.  This trigger can be used in ERROR state only and changes the interface state to READY. |
| DAI\_TRIGGER\_RESET | Reset.  This trigger frees resources and moves the driver back to initial state. |
| DAI\_TRIGGER\_COPY | Copy.  This trigger prepares for data copying. |

## [◆ ](#gac95242d83a2c2b477fcb9eb3da420797)dai\_type

| enum [dai\_type](#gac95242d83a2c2b477fcb9eb3da420797) |
| --- |

`#include <[dai.h](dai_8h.md)>`

Types of DAI.

The type of the DAI. This ID type is used to configure bespoke DAI HW settings.

DAIs have a lot of physical link feature variability and therefore need different configuration data to cater for different use cases. We usually need to pass extra bespoke configuration prior to DAI start.

| Enumerator | |
| --- | --- |
| DAI\_LEGACY\_I2S | Legacy I2S compatible with [i2s.h](i2s_8h.md "Public APIs for the I2S (Inter-IC Sound) bus drivers."). |
| DAI\_INTEL\_SSP | Intel SSP. |
| DAI\_INTEL\_DMIC | Intel DMIC. |
| DAI\_INTEL\_HDA | Intel HD/A. |
| DAI\_INTEL\_ALH | Intel ALH. |
| DAI\_IMX\_SAI | i.MX SAI |
| DAI\_IMX\_ESAI | i.MX ESAI |
| DAI\_AMD\_BT | Amd BT. |
| DAI\_AMD\_SP | Amd SP. |
| DAI\_AMD\_DMIC | Amd DMIC. |
| DAI\_MEDIATEK\_AFE | Mtk AFE. |
| DAI\_INTEL\_SSP\_NHLT | nhlt ssp |
| DAI\_INTEL\_DMIC\_NHLT | nhlt ssp |
| DAI\_INTEL\_HDA\_NHLT | nhlt Intel HD/A |
| DAI\_INTEL\_ALH\_NHLT | nhlt Intel ALH |

## Function Documentation

## [◆ ](#gab093045778b0d0d1eee06e50e8c6481b)dai\_config\_get()

| | int dai\_config\_get | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [dai\_config](structdai__config.md) \* | *cfg*, | |  |  | enum [dai\_dir](#gafa7b22e4250c6479301fc657fea8a60f) | *dir* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dai.h](dai_8h.md)>`

Fetch configuration information of a DAI driver.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | cfg | Pointer to the config structure to be filled by the instance |
    | dir | Stream direction: RX or TX as defined by DAI\_DIR\_\* |

Return values
:   | 0 | if success, negative if invalid parameters or DAI un-configured |
    | --- | --- |

## [◆ ](#ga182f79eeaf83ba8936298fcc93ad760a)dai\_config\_set()

| | int dai\_config\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [dai\_config](structdai__config.md) \* | *cfg*, | |  |  | const void \* | *bespoke\_cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dai.h](dai_8h.md)>`

Configure operation of a DAI driver.

The dir parameter specifies if Transmit (TX) or Receive (RX) direction will be configured by data provided via cfg parameter.

The function can be called in NOT\_READY or READY state only. If executed successfully the function will change the interface state to READY.

If the function is called with the parameter cfg->frame\_clk\_freq set to 0 the interface state will be changed to NOT\_READY.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | cfg | Pointer to the structure containing configuration parameters. |
    | bespoke\_cfg | Pointer to the structure containing bespoke config. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | Invalid argument. |
    | -ENOSYS | DAI\_DIR\_BOTH value is not supported. |

## [◆ ](#gac732c8b3e737ecca187f38e308d95724)dai\_get\_properties()

| | const struct [dai\_properties](structdai__properties.md) \* dai\_get\_properties | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [dai\_dir](#gafa7b22e4250c6479301fc657fea8a60f) | *dir*, | |  |  | int | *stream\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dai.h](dai_8h.md)>`

Fetch properties of a DAI driver.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | dir | Stream direction: RX or TX as defined by DAI\_DIR\_\* |
    | stream\_id | Stream id: some drivers may have stream specific properties, this id specifies the stream. |

Return values
:   | Pointer | to the structure containing properties, or NULL if error or no properties |
    | --- | --- |

## [◆ ](#ga40d5fd2676a9195c07fd7382aa1cea4a)dai\_probe()

| | int dai\_probe | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dai.h](dai_8h.md)>`

Probe operation of DAI driver.

The function will be called to power up the device and update for example possible reference count of the users. It can be used also to initialize internal variables and memory allocation.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |

## [◆ ](#ga91482e349a735a927fa396f4636247e5)dai\_remove()

| | int dai\_remove | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dai.h](dai_8h.md)>`

Remove operation of DAI driver.

The function will be called to unregister/unbind the device, for example to power down the device or decrease the usage reference count.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |

## [◆ ](#gabea217717edd2e986efeb475bbbc2208)dai\_trigger()

| | int dai\_trigger | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [dai\_dir](#gafa7b22e4250c6479301fc657fea8a60f) | *dir*, | |  |  | enum [dai\_trigger\_cmd](#gaee6445967afb3ecf2c0470ca0c104a1a) | *cmd* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dai.h](dai_8h.md)>`

Send a trigger command.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | dir | Stream direction: RX, TX, or both, as defined by DAI\_DIR\_\*. The DAI\_DIR\_BOTH value may not be supported by some drivers. For those, triggering need to be done separately for the RX and TX streams. |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Trigger command. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | Invalid argument. |
    | -EIO | The trigger cannot be executed in the current state or a DMA channel cannot be allocated. |
    | -ENOMEM | RX/TX memory block not available. |
    | -ENOSYS | DAI\_DIR\_BOTH value is not supported. |

## [◆ ](#gac401703e4054d1eeeaf619b295f5d6d8)dai\_ts\_config()

| | int dai\_ts\_config | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [dai\_ts\_cfg](structdai__ts__cfg.md) \* | *cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dai.h](dai_8h.md)>`

Configures timestamping in attached DAI.

Parameters
:   | dev | Component device. |
    | --- | --- |
    | cfg | Timestamp config. |

Optional method.

Return values
:   | 0 | If successful. |
    | --- | --- |

## [◆ ](#gaf6a4127a0edb48814aebf2f3fbaa3651)dai\_ts\_get()

| | int dai\_ts\_get | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [dai\_ts\_cfg](structdai__ts__cfg.md) \* | *cfg*, | |  |  | struct [dai\_ts\_data](structdai__ts__data.md) \* | *tsd* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dai.h](dai_8h.md)>`

Gets timestamp.

Parameters
:   | dev | Component device. |
    | --- | --- |
    | cfg | Timestamp config. |
    | tsd | Receives timestamp data. |

Optional method.

Return values
:   | 0 | If successful. |
    | --- | --- |

## [◆ ](#ga3dd0fd529c091d64dcb92d0c579a34ad)dai\_ts\_start()

| | int dai\_ts\_start | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [dai\_ts\_cfg](structdai__ts__cfg.md) \* | *cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dai.h](dai_8h.md)>`

Starts timestamping.

Parameters
:   | dev | Component device. |
    | --- | --- |
    | cfg | Timestamp config. |

Optional method

Return values
:   | 0 | If successful. |
    | --- | --- |

## [◆ ](#gaa3f2e59655c13101faf91ab2a6fd2f5e)dai\_ts\_stop()

| | int dai\_ts\_stop | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [dai\_ts\_cfg](structdai__ts__cfg.md) \* | *cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dai.h](dai_8h.md)>`

Stops timestamping.

Parameters
:   | dev | Component device. |
    | --- | --- |
    | cfg | Timestamp config. |

Optional method.

Return values
:   | 0 | If successful. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
