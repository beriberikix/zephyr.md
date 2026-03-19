---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcounter__config__info.html
original_path: doxygen/html/structcounter__config__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

counter\_config\_info Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Counter Interface](group__counter__interface.md)

Structure with generic counter features.
[More...](#details)

`#include <[counter.h](drivers_2counter_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_top\_value](#a0465be87680d1a50e1ae7a68c61caaac) |
|  | Maximal (default) top value on which counter is reset (cleared or reloaded). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [freq](#a4cae02b246a92e5d207d5b654d059322) |
|  | Frequency of the source clock if synchronous events are counted. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#ab38d95647388c700de372882db372d6c) |
|  | Flags (see [COUNTER\_FLAGS](group__counter__interface.md#COUNTER_FLAGS "COUNTER_FLAGS")). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channels](#afe2281d1909fa85978077558d6f4b71f) |
|  | Number of channels that can be used for setting alarm. |

## Detailed Description

Structure with generic counter features.

## Field Documentation

## [◆ ](#afe2281d1909fa85978077558d6f4b71f)channels

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) counter\_config\_info::channels |
| --- |

Number of channels that can be used for setting alarm.

See also
:   [counter\_set\_channel\_alarm](group__counter__interface.md#ga00a2857d993a84a56e8e222727f3d85e "Set a single shot alarm on a channel.")

## [◆ ](#ab38d95647388c700de372882db372d6c)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) counter\_config\_info::flags |
| --- |

Flags (see [COUNTER\_FLAGS](group__counter__interface.md#COUNTER_FLAGS "COUNTER_FLAGS")).

## [◆ ](#a4cae02b246a92e5d207d5b654d059322)freq

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) counter\_config\_info::freq |
| --- |

Frequency of the source clock if synchronous events are counted.

## [◆ ](#a0465be87680d1a50e1ae7a68c61caaac)max\_top\_value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) counter\_config\_info::max\_top\_value |
| --- |

Maximal (default) top value on which counter is reset (cleared or reloaded).

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[counter.h](drivers_2counter_8h_source.md)

- [counter\_config\_info](structcounter__config__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
