---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsd__csd.html
original_path: doxygen/html/structsd__csd.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sd\_csd Struct Reference

SD card specific data register.
[More...](#details)

`#include <[sd_spec.h](sd__spec_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [csd\_structure](#a37b15b70967c9317183b3e5e7837b228) |
|  | CSD structure [127:126]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [read\_time1](#a583c715045b5934ad94ab9cf61b25b06) |
|  | Data read access-time-1 [119:112]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [read\_time2](#a96bc4672222dece77d29ffc9287c59ac) |
|  | Data read access-time-2 in clock cycles (NSAC\*100) [111:104]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [xfer\_rate](#ae39272173a5253d0d11ef04a2e129db6) |
|  | Maximum data transfer rate [103:96]. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cmd\_class](#a8bfd2c42066d85058d01076fcaa7a32d) |
|  | Card command classes [95:84]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [read\_blk\_len](#a06f6aef4f4745a78bcf769df5415daa6) |
|  | Maximum read data block length [83:80]. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#ae10b32787aeedd4789d657eb1ef492eb) |
|  | Flags in \_sd\_csd\_flag. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [device\_size](#ad35b07abba80e9929c5eed40e37d25b3) |
|  | Device size [73:62]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [read\_current\_min](#aa868cfc1db75eb2913d21bffeaf29fd9) |
|  | Maximum read current at VDD min [61:59]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [read\_current\_max](#ad2f31731d7ec0b101d911fe20b5d94db) |
|  | Maximum read current at VDD max [58:56]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [write\_current\_min](#a0d1efea12c467eacd0d0f98a0bb0ac91) |
|  | Maximum write current at VDD min [55:53]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [write\_current\_max](#a53b364ce0db06b9217259afeb625da44) |
|  | Maximum write current at VDD max [52:50]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dev\_size\_mul](#a9d5a952bc6c2a6967e9a88cd93f19e89) |
|  | Device size multiplier [49:47]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [erase\_size](#ab8d5ae38b19f7ea83b0856ad093c65cb) |
|  | Erase sector size [45:39]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [write\_prtect\_size](#a029a893cdcd3765864c70476eb6dd64e) |
|  | Write protect group size [38:32]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [write\_speed\_factor](#a9c362eff38daf7d00776416ed064de24) |
|  | Write speed factor [28:26]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [write\_blk\_len](#adff7d405662589ec44f4d0a6b3548760) |
|  | Maximum write data block length [25:22]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [file\_fmt](#af93239157610a6eeea420c29432d5412) |
|  | File format [11:10]. |

## Detailed Description

SD card specific data register.

Card specific data register. contains additional data about SD card.

## Field Documentation

## [◆ ](#a8bfd2c42066d85058d01076fcaa7a32d)cmd\_class

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sd\_csd::cmd\_class |
| --- |

Card command classes [95:84].

## [◆ ](#a37b15b70967c9317183b3e5e7837b228)csd\_structure

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::csd\_structure |
| --- |

CSD structure [127:126].

## [◆ ](#a9d5a952bc6c2a6967e9a88cd93f19e89)dev\_size\_mul

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::dev\_size\_mul |
| --- |

Device size multiplier [49:47].

## [◆ ](#ad35b07abba80e9929c5eed40e37d25b3)device\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sd\_csd::device\_size |
| --- |

Device size [73:62].

## [◆ ](#ab8d5ae38b19f7ea83b0856ad093c65cb)erase\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::erase\_size |
| --- |

Erase sector size [45:39].

## [◆ ](#af93239157610a6eeea420c29432d5412)file\_fmt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::file\_fmt |
| --- |

File format [11:10].

## [◆ ](#ae10b32787aeedd4789d657eb1ef492eb)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sd\_csd::flags |
| --- |

Flags in \_sd\_csd\_flag.

## [◆ ](#a06f6aef4f4745a78bcf769df5415daa6)read\_blk\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::read\_blk\_len |
| --- |

Maximum read data block length [83:80].

## [◆ ](#ad2f31731d7ec0b101d911fe20b5d94db)read\_current\_max

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::read\_current\_max |
| --- |

Maximum read current at VDD max [58:56].

## [◆ ](#aa868cfc1db75eb2913d21bffeaf29fd9)read\_current\_min

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::read\_current\_min |
| --- |

Maximum read current at VDD min [61:59].

## [◆ ](#a583c715045b5934ad94ab9cf61b25b06)read\_time1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::read\_time1 |
| --- |

Data read access-time-1 [119:112].

## [◆ ](#a96bc4672222dece77d29ffc9287c59ac)read\_time2

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::read\_time2 |
| --- |

Data read access-time-2 in clock cycles (NSAC\*100) [111:104].

## [◆ ](#adff7d405662589ec44f4d0a6b3548760)write\_blk\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::write\_blk\_len |
| --- |

Maximum write data block length [25:22].

## [◆ ](#a53b364ce0db06b9217259afeb625da44)write\_current\_max

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::write\_current\_max |
| --- |

Maximum write current at VDD max [52:50].

## [◆ ](#a0d1efea12c467eacd0d0f98a0bb0ac91)write\_current\_min

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::write\_current\_min |
| --- |

Maximum write current at VDD min [55:53].

## [◆ ](#a029a893cdcd3765864c70476eb6dd64e)write\_prtect\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::write\_prtect\_size |
| --- |

Write protect group size [38:32].

## [◆ ](#a9c362eff38daf7d00776416ed064de24)write\_speed\_factor

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::write\_speed\_factor |
| --- |

Write speed factor [28:26].

## [◆ ](#ae39272173a5253d0d11ef04a2e129db6)xfer\_rate

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_csd::xfer\_rate |
| --- |

Maximum data transfer rate [103:96].

---

The documentation for this struct was generated from the following file:

- zephyr/sd/[sd\_spec.h](sd__spec_8h_source.md)

- [sd\_csd](structsd__csd.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
