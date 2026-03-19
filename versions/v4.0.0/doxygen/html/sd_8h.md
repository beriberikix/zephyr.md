---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sd_8h.html
original_path: doxygen/html/sd_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sd.h File Reference

Public API for SD subsystem.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/sdhc.h](sdhc_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](sd_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sdio\_func](structsdio__func.md) |
|  | SDIO function definition. [More...](structsdio__func.md#details) |
| struct | [sd\_card](structsd__card.md) |
|  | SD card structure. [More...](structsd__card.md#details) |

| Enumerations | |
| --- | --- |
| enum | [card\_status](#a52167aac735d93085a5eebc6f50e1bba) { [CARD\_UNINITIALIZED](#a52167aac735d93085a5eebc6f50e1bbaaa059e919850b36b85ebe33a07050e453) = 0 , [CARD\_ERROR](#a52167aac735d93085a5eebc6f50e1bbaa5458e6fab05f8c1afbe7d191eb489e5e) = 1 , [CARD\_INITIALIZED](#a52167aac735d93085a5eebc6f50e1bbaa839d17bb0bee41a125a617683bce17c9) = 2 } |
|  | card status. [More...](#a52167aac735d93085a5eebc6f50e1bba) |
| enum | [card\_type](#aee707e2ff5691dbdefd9341a18de7b14) { [CARD\_SDMMC](#aee707e2ff5691dbdefd9341a18de7b14a8b26749346e26d9257cd53c48a68eda4) = 0 , [CARD\_SDIO](#aee707e2ff5691dbdefd9341a18de7b14a5afc0338b5a0541bb34f1a5b67139b6b) = 1 , [CARD\_COMBO](#aee707e2ff5691dbdefd9341a18de7b14ad527710e81e76e0938689015c2013090) = 2 , [CARD\_MMC](#aee707e2ff5691dbdefd9341a18de7b14a868625c31f4384780de3992d78b93345) = 3 } |
|  | card type. [More...](#aee707e2ff5691dbdefd9341a18de7b14) |

| Functions | |
| --- | --- |
| int | [sd\_init](#ac02b6fe46112b8b891e9713ef24bd131) (const struct [device](structdevice.md) \*sdhc\_dev, struct [sd\_card](structsd__card.md) \*card) |
|  | Initialize an SD device. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sd\_is\_card\_present](#aed46c9c492c5c6434a6ae4d6151ac7d3) (const struct [device](structdevice.md) \*sdhc\_dev) |
|  | checks to see if card is present in the SD slot |

## Detailed Description

Public API for SD subsystem.

## Enumeration Type Documentation

## [◆ ](#a52167aac735d93085a5eebc6f50e1bba)card\_status

| enum [card\_status](#a52167aac735d93085a5eebc6f50e1bba) |
| --- |

card status.

Used internally by subsystem.

| Enumerator | |
| --- | --- |
| CARD\_UNINITIALIZED | card has not been initialized |
| CARD\_ERROR | card state is error |
| CARD\_INITIALIZED | card is in valid state |

## [◆ ](#aee707e2ff5691dbdefd9341a18de7b14)card\_type

| enum [card\_type](#aee707e2ff5691dbdefd9341a18de7b14) |
| --- |

card type.

Used internally by subsystem.

| Enumerator | |
| --- | --- |
| CARD\_SDMMC | SD memory card. |
| CARD\_SDIO | SD I/O card. |
| CARD\_COMBO | SD memory and I/O card. |
| CARD\_MMC | MMC memory card. |

## Function Documentation

## [◆ ](#ac02b6fe46112b8b891e9713ef24bd131)sd\_init()

| int sd\_init | ( | const struct [device](structdevice.md) \* | *sdhc\_dev*, |
| --- | --- | --- | --- |
|  |  | struct [sd\_card](structsd__card.md) \* | *card* ) |

Initialize an SD device.

Initializes an SD device to use with the subsystem. After this call, only the SD card structure is required to access the card.

Parameters
:   | sdhc\_dev | SD host controller device for this card |
    | --- | --- |
    | card | SD card structure for this card |

Return values
:   | 0 | card was initialized |
    | --- | --- |
    | -ETIMEDOUT | card initialization timed out |
    | -EBUSY | card is busy |
    | -EIO | IO error while starting card |

## [◆ ](#aed46c9c492c5c6434a6ae4d6151ac7d3)sd\_is\_card\_present()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sd\_is\_card\_present | ( | const struct [device](structdevice.md) \* | *sdhc\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

checks to see if card is present in the SD slot

Parameters
:   | sdhc\_dev | SD host controller to check for card presence on |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | card is present |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | card is not present |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sd](dir_ff091b3f4b9505cc58dad89321d1c232.md)
- [sd.h](sd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
