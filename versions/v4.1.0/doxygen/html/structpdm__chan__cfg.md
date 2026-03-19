---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structpdm__chan__cfg.html
original_path: doxygen/html/structpdm__chan__cfg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pdm\_chan\_cfg Struct Reference

[Audio](group__audio__interface.md) » [Digital Microphone Interface](group__audio__dmic__interface.md)

Mapping/ordering of the PDM channels to logical PCM output channel.
[More...](#details)

`#include <[dmic.h](dmic_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [req\_num\_chan](#aa2518c6f577c3fd92ec009fa134a6185) |
|  | Requested number of channels. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [act\_num\_chan](#a3268169aaee14827cb15778fbc44ceb1) |
|  | Actual number of channels that the driver could configure. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [req\_num\_streams](#ae1398759382606cc60cf8944a1b9e5f6) |
|  | Requested number of streams for each channel. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [act\_num\_streams](#a7614fefd7976ba7b195afb4e81f7100e) |
|  | Actual number of streams that the driver could configure. |
| Requested channel map | |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [req\_chan\_map\_lo](#a028c8cd3dfcf0bfce618ef8937a7b211) |
|  | Channels 0 to 7. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [req\_chan\_map\_hi](#a11a258f6b21126e1d50c5a3f46b2cad7) |
|  | Channels 8 to 15. |
| Actual channel map that the driver could configure | |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [act\_chan\_map\_lo](#a34d2e2d03df48e26245835d4df88b60b) |
|  | Channels 0 to 7. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [act\_chan\_map\_hi](#a9a91e9341f4c033243effbebd5ffa194) |
|  | Channels 8 to 15. |

## Detailed Description

Mapping/ordering of the PDM channels to logical PCM output channel.

Since each controller can have 2 audio channels (stereo), there can be a total of 8x2=16 channels. The actual number of channels shall be described in [act\_num\_chan](#a3268169aaee14827cb15778fbc44ceb1).

If 2 streams are enabled, the channel order will be the same for both streams.

Each channel is described as a 4-bit number, the least significant bit indicates LEFT/RIGHT selection of the PDM controller.

The most significant 3 bits indicate the PDM controller number:

- bits 0-3 are for channel 0, bit 0 indicates LEFT or RIGHT
- bits 4-7 are for channel 1, bit 4 indicates LEFT or RIGHT and so on.

CONSTRAINT: The LEFT and RIGHT channels of EACH PDM controller needs to be adjacent to each other.

## Field Documentation

## [◆ ](#a9a91e9341f4c033243effbebd5ffa194)act\_chan\_map\_hi

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pdm\_chan\_cfg::act\_chan\_map\_hi |
| --- |

Channels 8 to 15.

## [◆ ](#a34d2e2d03df48e26245835d4df88b60b)act\_chan\_map\_lo

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pdm\_chan\_cfg::act\_chan\_map\_lo |
| --- |

Channels 0 to 7.

## [◆ ](#a3268169aaee14827cb15778fbc44ceb1)act\_num\_chan

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm\_chan\_cfg::act\_num\_chan |
| --- |

Actual number of channels that the driver could configure.

## [◆ ](#a7614fefd7976ba7b195afb4e81f7100e)act\_num\_streams

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm\_chan\_cfg::act\_num\_streams |
| --- |

Actual number of streams that the driver could configure.

## [◆ ](#a11a258f6b21126e1d50c5a3f46b2cad7)req\_chan\_map\_hi

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pdm\_chan\_cfg::req\_chan\_map\_hi |
| --- |

Channels 8 to 15.

## [◆ ](#a028c8cd3dfcf0bfce618ef8937a7b211)req\_chan\_map\_lo

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pdm\_chan\_cfg::req\_chan\_map\_lo |
| --- |

Channels 0 to 7.

## [◆ ](#aa2518c6f577c3fd92ec009fa134a6185)req\_num\_chan

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm\_chan\_cfg::req\_num\_chan |
| --- |

Requested number of channels.

## [◆ ](#ae1398759382606cc60cf8944a1b9e5f6)req\_num\_streams

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm\_chan\_cfg::req\_num\_streams |
| --- |

Requested number of streams for each channel.

---

The documentation for this struct was generated from the following file:

- zephyr/audio/[dmic.h](dmic_8h_source.md)

- [pdm\_chan\_cfg](structpdm__chan__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
