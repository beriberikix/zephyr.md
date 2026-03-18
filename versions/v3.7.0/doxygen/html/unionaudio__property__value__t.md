---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/unionaudio__property__value__t.html
original_path: doxygen/html/unionaudio__property__value__t.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

audio\_property\_value\_t Union Reference

[Audio](group__audio__interface.md) » [Audio Codec Interface](group__audio__codec__interface.md)

Codec property values.
[More...](#details)

`#include <[codec.h](codec_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [vol](#aafcfb98016ab4306b4fd6cb54f0c22e0) |
|  | Volume level in 0.5dB resolution. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [mute](#a23e0d9031006d64dfb31d87e4f061dc8) |
|  | Mute if *true*, unmute if *false*. |

## Detailed Description

Codec property values.

## Field Documentation

## [◆ ](#a23e0d9031006d64dfb31d87e4f061dc8)mute

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) audio\_property\_value\_t::mute |
| --- |

Mute if *true*, unmute if *false*.

## [◆ ](#aafcfb98016ab4306b4fd6cb54f0c22e0)vol

| int audio\_property\_value\_t::vol |
| --- |

Volume level in 0.5dB resolution.

---

The documentation for this union was generated from the following file:

- zephyr/audio/[codec.h](codec_8h_source.md)

- [audio\_property\_value\_t](unionaudio__property__value__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
