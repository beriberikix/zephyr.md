---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structaudio__codec__cfg.html
original_path: doxygen/html/structaudio__codec__cfg.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

audio\_codec\_cfg Struct Reference

[Audio](group__audio__interface.md) » [Audio Codec Interface](group__audio__codec__interface.md)

Codec configuration parameters.
[More...](#details)

`#include <[codec.h](codec_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mclk\_freq](#a896521cdcacafeb3c5b42a439415c5bb) |
|  | MCLK input frequency in Hz. |
| [audio\_dai\_type\_t](group__audio__codec__interface.md#ga147094be4c7c5d62df695673d293f12d) | [dai\_type](#a121ca221241b0e2e90d9657a2462cd3c) |
|  | Digital interface type. |
| [audio\_dai\_cfg\_t](unionaudio__dai__cfg__t.md) | [dai\_cfg](#aa42aa9a75adec5929c54910abdc5311c) |
|  | DAI configuration info. |

## Detailed Description

Codec configuration parameters.

## Field Documentation

## [◆ ](#aa42aa9a75adec5929c54910abdc5311c)dai\_cfg

| [audio\_dai\_cfg\_t](unionaudio__dai__cfg__t.md) audio\_codec\_cfg::dai\_cfg |
| --- |

DAI configuration info.

## [◆ ](#a121ca221241b0e2e90d9657a2462cd3c)dai\_type

| [audio\_dai\_type\_t](group__audio__codec__interface.md#ga147094be4c7c5d62df695673d293f12d) audio\_codec\_cfg::dai\_type |
| --- |

Digital interface type.

## [◆ ](#a896521cdcacafeb3c5b42a439415c5bb)mclk\_freq

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) audio\_codec\_cfg::mclk\_freq |
| --- |

MCLK input frequency in Hz.

---

The documentation for this struct was generated from the following file:

- zephyr/audio/[codec.h](codec_8h_source.md)

- [audio\_codec\_cfg](structaudio__codec__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
