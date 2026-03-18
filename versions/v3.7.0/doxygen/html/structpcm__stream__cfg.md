---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structpcm__stream__cfg.html
original_path: doxygen/html/structpcm__stream__cfg.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pcm\_stream\_cfg Struct Reference

[Audio](group__audio__interface.md) » [Digital Microphone Interface](group__audio__dmic__interface.md)

Configuration of the PCM streams to be output by the PDM hardware.
[More...](#details)

`#include <[dmic.h](dmic_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcm\_rate](#ae6e3790576f910943b0383f4731a5545) |
|  | PCM sample rate of stream. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pcm\_width](#a7d9fd0039bc25de292f35f60c99c6615) |
|  | PCM sample width of stream. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [block\_size](#a3c224ba6f6c6fa7a128a739b6f1c36bf) |
|  | PCM sample block size per transfer. |
| struct k\_mem\_slab \* | [mem\_slab](#ade324dcfe8604fcb94400544ddb4517e) |
|  | SLAB for DMIC driver to allocate buffers for stream. |

## Detailed Description

Configuration of the PCM streams to be output by the PDM hardware.

Note
:   if either [pcm\_rate](#ae6e3790576f910943b0383f4731a5545) or [pcm\_width](#a7d9fd0039bc25de292f35f60c99c6615) is set to 0 for a stream, the stream would be disabled

## Field Documentation

## [◆ ](#a3c224ba6f6c6fa7a128a739b6f1c36bf)block\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pcm\_stream\_cfg::block\_size |
| --- |

PCM sample block size per transfer.

## [◆ ](#ade324dcfe8604fcb94400544ddb4517e)mem\_slab

| struct k\_mem\_slab\* pcm\_stream\_cfg::mem\_slab |
| --- |

SLAB for DMIC driver to allocate buffers for stream.

## [◆ ](#ae6e3790576f910943b0383f4731a5545)pcm\_rate

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pcm\_stream\_cfg::pcm\_rate |
| --- |

PCM sample rate of stream.

## [◆ ](#a7d9fd0039bc25de292f35f60c99c6615)pcm\_width

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pcm\_stream\_cfg::pcm\_width |
| --- |

PCM sample width of stream.

---

The documentation for this struct was generated from the following file:

- zephyr/audio/[dmic.h](dmic_8h_source.md)

- [pcm\_stream\_cfg](structpcm__stream__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
