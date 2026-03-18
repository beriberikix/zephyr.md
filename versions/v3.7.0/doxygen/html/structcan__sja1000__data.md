---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcan__sja1000__data.html
original_path: doxygen/html/structcan__sja1000__data.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_sja1000\_data Struct Reference

SJA1000 driver internal data structure.
[More...](#details)

`#include <[can_sja1000.h](can__sja1000_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct can\_driver\_data | [common](#aa31ac266b0f4f976bc346fb87e62c1dc) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [rx\_allocs](#afde535cdca9611a264e3feefe3f4c180) [[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)(CONFIG\_CAN\_MAX\_FILTER)] |
| struct [can\_sja1000\_rx\_filter](structcan__sja1000__rx__filter.md) | [filters](#ab4510fe2232bcea825e68777640d182d) [CONFIG\_CAN\_MAX\_FILTER] |
| struct [k\_mutex](structk__mutex.md) | [mod\_lock](#adc707a2852492ff0859e08976986e191) |
| enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) | [state](#ab2e365eb95f4440db7c42f6f6c9999a0) |
| struct k\_sem | [tx\_idle](#a8152989a4408268abdb35688bfcfd02b) |
| [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) | [tx\_callback](#a3ee972b9dfd1aa226159ad3c5cf41210) |
| void \* | [tx\_user\_data](#ab61c31be1a91696bceb65bab188356a1) |
| void \* | [custom](#a2c6e39433b4d07423635cb73dd7a37e6) |

## Detailed Description

SJA1000 driver internal data structure.

## Field Documentation

## [◆ ](#aa31ac266b0f4f976bc346fb87e62c1dc)common

| struct can\_driver\_data can\_sja1000\_data::common |
| --- |

## [◆ ](#a2c6e39433b4d07423635cb73dd7a37e6)custom

| void\* can\_sja1000\_data::custom |
| --- |

## [◆ ](#ab4510fe2232bcea825e68777640d182d)filters

| struct [can\_sja1000\_rx\_filter](structcan__sja1000__rx__filter.md) can\_sja1000\_data::filters[CONFIG\_CAN\_MAX\_FILTER] |
| --- |

## [◆ ](#adc707a2852492ff0859e08976986e191)mod\_lock

| struct [k\_mutex](structk__mutex.md) can\_sja1000\_data::mod\_lock |
| --- |

## [◆ ](#afde535cdca9611a264e3feefe3f4c180)rx\_allocs

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) can\_sja1000\_data::rx\_allocs[[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)(CONFIG\_CAN\_MAX\_FILTER)] |
| --- |

## [◆ ](#ab2e365eb95f4440db7c42f6f6c9999a0)state

| enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) can\_sja1000\_data::state |
| --- |

## [◆ ](#a3ee972b9dfd1aa226159ad3c5cf41210)tx\_callback

| [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) can\_sja1000\_data::tx\_callback |
| --- |

## [◆ ](#a8152989a4408268abdb35688bfcfd02b)tx\_idle

| struct k\_sem can\_sja1000\_data::tx\_idle |
| --- |

## [◆ ](#ab61c31be1a91696bceb65bab188356a1)tx\_user\_data

| void\* can\_sja1000\_data::tx\_user\_data |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_sja1000.h](can__sja1000_8h_source.md)

- [can\_sja1000\_data](structcan__sja1000__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
