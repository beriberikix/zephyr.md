---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structi2s__config.html
original_path: doxygen/html/structi2s__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2s\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I2S Interface](group__i2s__interface.md)

Interface configuration options.
[More...](#details)

`#include <[i2s.h](i2s_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [word\_size](#a5a38a75f0b4a3356ed85495fb45d0cd2) |
|  | Number of bits representing one data word. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channels](#acd9ff8b9a0e79e95a8deb19df145478d) |
|  | Number of words per frame. |
| [i2s\_fmt\_t](group__i2s__interface.md#ga0939a3ba04a233d9d637fba8a42b0bbb) | [format](#a9ab2e8fa330473be99ce0713aec60daf) |
|  | Data stream format as defined by I2S\_FMT\_\* constants. |
| [i2s\_opt\_t](group__i2s__interface.md#gad0ca475f9bf5edeecc7de65b4f56c119) | [options](#a56a9caaf8133ced8e47e3699e322fdab) |
|  | Configuration options as defined by I2S\_OPT\_\* constants. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [frame\_clk\_freq](#ab5b0556fcd113c6c645e265af4846b45) |
|  | Frame clock (WS) frequency, this is sampling rate. |
| struct k\_mem\_slab \* | [mem\_slab](#a11991601fa180ead06a23b90a58136ff) |
|  | Memory slab to store RX/TX data. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [block\_size](#a62f504e954fc42c343d142513bbaf4ef) |
|  | Size of one RX/TX memory block (buffer) in bytes. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [timeout](#a9bf6c6cb96cc9c3acd8efc3fad0cbca9) |
|  | Read/Write timeout. |

## Detailed Description

Interface configuration options.

Memory slab pointed to by the mem\_slab field has to be defined and initialized by the user. For I2S driver to function correctly number of memory blocks in a slab has to be at least 2 per queue. Size of the memory block should be multiple of frame\_size where frame\_size = (channels \* word\_size\_bytes). As an example 16 bit word will occupy 2 bytes, 24 or 32 bit word will occupy 4 bytes.

Please check Zephyr Kernel Primer for more information on memory slabs.

Remarks
:   When I2S data format is selected parameter channels is ignored, number of words in a frame is always 2.

## Field Documentation

## [◆ ](#a62f504e954fc42c343d142513bbaf4ef)block\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) i2s\_config::block\_size |
| --- |

Size of one RX/TX memory block (buffer) in bytes.

## [◆ ](#acd9ff8b9a0e79e95a8deb19df145478d)channels

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i2s\_config::channels |
| --- |

Number of words per frame.

## [◆ ](#a9ab2e8fa330473be99ce0713aec60daf)format

| [i2s\_fmt\_t](group__i2s__interface.md#ga0939a3ba04a233d9d637fba8a42b0bbb) i2s\_config::format |
| --- |

Data stream format as defined by I2S\_FMT\_\* constants.

## [◆ ](#ab5b0556fcd113c6c645e265af4846b45)frame\_clk\_freq

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i2s\_config::frame\_clk\_freq |
| --- |

Frame clock (WS) frequency, this is sampling rate.

## [◆ ](#a11991601fa180ead06a23b90a58136ff)mem\_slab

| struct k\_mem\_slab\* i2s\_config::mem\_slab |
| --- |

Memory slab to store RX/TX data.

## [◆ ](#a56a9caaf8133ced8e47e3699e322fdab)options

| [i2s\_opt\_t](group__i2s__interface.md#gad0ca475f9bf5edeecc7de65b4f56c119) i2s\_config::options |
| --- |

Configuration options as defined by I2S\_OPT\_\* constants.

## [◆ ](#a9bf6c6cb96cc9c3acd8efc3fad0cbca9)timeout

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) i2s\_config::timeout |
| --- |

Read/Write timeout.

Number of milliseconds to wait in case TX queue is full or RX queue is empty, or 0, or SYS\_FOREVER\_MS.

## [◆ ](#a5a38a75f0b4a3356ed85495fb45d0cd2)word\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i2s\_config::word\_size |
| --- |

Number of bits representing one data word.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i2s.h](i2s_8h_source.md)

- [i2s\_config](structi2s__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
