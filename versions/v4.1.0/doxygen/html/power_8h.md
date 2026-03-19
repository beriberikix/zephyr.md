---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/power_8h.html
original_path: doxygen/html/power_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

power.h File Reference

SCMI power domain protocol helpers.
[More...](#details)

`#include <[zephyr/drivers/firmware/scmi/protocol.h](protocol_8h_source.md)>`

[Go to the source code of this file.](power_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [scmi\_power\_state\_config](structscmi__power__state__config.md) |
|  | Describes the parameters for the POWER\_STATE\_SET command. [More...](structscmi__power__state__config.md#details) |

| Macros | |
| --- | --- |
| #define | [SCMI\_POWER\_STATE\_SET\_FLAGS\_ASYNC](#a8c95da0a183bcdde6e6fde5b111d9c22)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |

| Enumerations | |
| --- | --- |
| enum | [scmi\_power\_domain\_message](#a669e3ff12b5fc6791440e4adb7596293) {     [SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_VERSION](#a669e3ff12b5fc6791440e4adb7596293a92ac48a13aed6415581beab023ef31b8) = 0x0 , [SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_ATTRIBUTES](#a669e3ff12b5fc6791440e4adb7596293a3457133a86ab6480b10470bb1fe296d3) = 0x1 , [SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES](#a669e3ff12b5fc6791440e4adb7596293a066426afb042922071675b090fd785f3) = 0x2 , [SCMI\_POWER\_DOMAIN\_MSG\_POWER\_DOMAIN\_ATTRIBUTES](#a669e3ff12b5fc6791440e4adb7596293aefdc40ff9bb0939d37cb631eb2aa7daa) = 0x3 ,     [SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_SET](#a669e3ff12b5fc6791440e4adb7596293aab1e51f69264b200fa2df662e7437243) = 0x4 , [SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_GET](#a669e3ff12b5fc6791440e4adb7596293aa524b1298afa78395fa4d11e010f2e47) = 0x5 , [SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_NOTIFY](#a669e3ff12b5fc6791440e4adb7596293aa884e44de1912627adcd7b3df08ee145) = 0x6 , [SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_CHANGE\_REQEUSTED\_NOTIFY](#a669e3ff12b5fc6791440e4adb7596293ac01e7fde59373798fa0ce78d776c58bc) = 0x7 ,     [SCMI\_POWER\_DOMAIN\_MSG\_POWER\_DOMAIN\_NAME\_GET](#a669e3ff12b5fc6791440e4adb7596293a113b5c6493366a21f4874ec25137cd1d) = 0x8 , [SCMI\_POWER\_DOMAIN\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION](#a669e3ff12b5fc6791440e4adb7596293aee289d3ed8b8a0fbdc4befc92f10fa65) = 0x10   } |
|  | Power domain protocol command message IDs. [More...](#a669e3ff12b5fc6791440e4adb7596293) |

| Functions | |
| --- | --- |
| int | [scmi\_power\_state\_set](#a0969968c4d6b94868295172c0408031b) (struct [scmi\_power\_state\_config](structscmi__power__state__config.md) \*cfg) |
|  | Send the POWER\_STATE\_SET command and get its reply. |
| int | [scmi\_power\_state\_get](#adc7a2fbf0c4cab570d3a567ce548c947) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*power\_state) |
|  | Query the power domain state. |

## Detailed Description

SCMI power domain protocol helpers.

## Macro Definition Documentation

## [◆ ](#a8c95da0a183bcdde6e6fde5b111d9c22)SCMI\_POWER\_STATE\_SET\_FLAGS\_ASYNC

| #define SCMI\_POWER\_STATE\_SET\_FLAGS\_ASYNC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## Enumeration Type Documentation

## [◆ ](#a669e3ff12b5fc6791440e4adb7596293)scmi\_power\_domain\_message

| enum [scmi\_power\_domain\_message](#a669e3ff12b5fc6791440e4adb7596293) |
| --- |

Power domain protocol command message IDs.

| Enumerator | |
| --- | --- |
| SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_VERSION |  |
| SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_ATTRIBUTES |  |
| SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES |  |
| SCMI\_POWER\_DOMAIN\_MSG\_POWER\_DOMAIN\_ATTRIBUTES |  |
| SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_SET |  |
| SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_GET |  |
| SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_NOTIFY |  |
| SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_CHANGE\_REQEUSTED\_NOTIFY |  |
| SCMI\_POWER\_DOMAIN\_MSG\_POWER\_DOMAIN\_NAME\_GET |  |
| SCMI\_POWER\_DOMAIN\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION |  |

## Function Documentation

## [◆ ](#adc7a2fbf0c4cab570d3a567ce548c947)scmi\_power\_state\_get()

| int scmi\_power\_state\_get | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *domain\_id*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *power\_state* ) |

Query the power domain state.

Parameters
:   | domain\_id | ID of the power domain for which the query is done |
    | --- | --- |
    | power\_state | pointer to be set via this command |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#a0969968c4d6b94868295172c0408031b)scmi\_power\_state\_set()

| int scmi\_power\_state\_set | ( | struct [scmi\_power\_state\_config](structscmi__power__state__config.md) \* | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

Send the POWER\_STATE\_SET command and get its reply.

Parameters
:   | cfg | pointer to structure containing configuration to be set |
    | --- | --- |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno if failure |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [power.h](power_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
