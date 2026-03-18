---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcan__mcan__config.html
original_path: doxygen/html/structcan__mcan__config.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_mcan\_config Struct Reference

Bosch M\_CAN driver internal configuration structure.
[More...](#details)

`#include <[can_mcan.h](can__mcan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct can\_driver\_config | [common](#a86a6f9a19db54c7368f16f72513db327) |
| const struct [can\_mcan\_ops](structcan__mcan__ops.md) \* | [ops](#aed10f9a4d2ddc0045bc6f37939973039) |
| const struct [can\_mcan\_callbacks](structcan__mcan__callbacks.md) \* | [callbacks](#a0c8500180fb8113e7bc36d446e4c39bb) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mram\_elements](#ab196bf74bf41fba65c0d076ff9070202) [8] |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mram\_offsets](#a412c0bb0b3d8158cd352d4c24a622401) [8] |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [mram\_size](#a10585712cd11d041829dca9c9c5446e1) |
| const void \* | [custom](#a7b2d696b6839a8f958f705fb13a0f63d) |

## Detailed Description

Bosch M\_CAN driver internal configuration structure.

## Field Documentation

## [◆ ](#a0c8500180fb8113e7bc36d446e4c39bb)callbacks

| const struct [can\_mcan\_callbacks](structcan__mcan__callbacks.md)\* can\_mcan\_config::callbacks |
| --- |

## [◆ ](#a86a6f9a19db54c7368f16f72513db327)common

| const struct can\_driver\_config can\_mcan\_config::common |
| --- |

## [◆ ](#a7b2d696b6839a8f958f705fb13a0f63d)custom

| const void\* can\_mcan\_config::custom |
| --- |

## [◆ ](#ab196bf74bf41fba65c0d076ff9070202)mram\_elements

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) can\_mcan\_config::mram\_elements[8] |
| --- |

## [◆ ](#a412c0bb0b3d8158cd352d4c24a622401)mram\_offsets

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) can\_mcan\_config::mram\_offsets[8] |
| --- |

## [◆ ](#a10585712cd11d041829dca9c9c5446e1)mram\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) can\_mcan\_config::mram\_size |
| --- |

## [◆ ](#aed10f9a4d2ddc0045bc6f37939973039)ops

| const struct [can\_mcan\_ops](structcan__mcan__ops.md)\* can\_mcan\_config::ops |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_mcan.h](can__mcan_8h_source.md)

- [can\_mcan\_config](structcan__mcan__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
