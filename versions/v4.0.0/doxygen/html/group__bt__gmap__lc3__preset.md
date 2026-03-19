---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__gmap__lc3__preset.html
original_path: doxygen/html/group__bt__gmap__lc3__preset.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Gaming Audio Profile (GMAP) LC3 Presets

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Gaming Audio Profile (GMAP) LC3 Presets.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_GMAP\_LC3\_PRESET\_32\_1\_GR](#ga6ec3341f2563494a10ae50bd709a6234)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 32\_1\_gr codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_32\_2\_GR](#ga7500c49ffb1d0cbb50faaab296954a9c)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 32\_2\_gr codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_1\_GR](#gac5fbc4c6cd39292baaddfabe0a91547b)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_1\_gr codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_2\_GR](#ga43266a8272f9d38ccfc7f845fb872bfa)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_2\_gr codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_3\_GR](#ga4b904abf0faf7ffef5e8680c90f861a6)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_3\_gr codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_4\_GR](#ga6d5438cd5121dc1853d185ce17278fac)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_4\_gr codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_16\_1\_GS](#ga01fd21cc55b4edbef612e704fc26fa0e)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 16\_1\_gs codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_16\_2\_GS](#ga900e8e6e308558d1e307c5726b26f00d)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 16\_2\_gs codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_32\_1\_GS](#gad2f2bf8f120332be58c8d3dbfe4e2c48)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 32\_1\_gs codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_32\_2\_GS](#ga0261c82920c16db61c2a551b44ea549f)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 32\_2\_gs codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_1\_GS](#ga258ac93490e61fbf82e69afa441cbeca)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_1\_gs codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_2\_GS](#ga4136fc4f83ebafb9d7574f7c750840aa)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_2\_gs codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_1\_G](#ga50562ea208350e7669255613fe4bef14)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_1\_g codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_2\_G](#gad65b1c65aa9943e80934cbf7234646dc)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_2\_g codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_3\_G](#gabe6f21e869b54c962633ab3ac6be7a91)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_3\_g codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_4\_G](#ga17d79f07ced6f8605abb88cedad5a4da)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_4\_g codec configuration. |

## Detailed Description

Gaming Audio Profile (GMAP) LC3 Presets.

Since
:   3.5

Version
:   0.8.0

These APIs provide presets for codec configuration and QoS based on values supplied by the codec configurations from table 3.16 in the GMAP v1.0 specification

## Macro Definition Documentation

## [◆ ](#ga01fd21cc55b4edbef612e704fc26fa0e)BT\_GMAP\_LC3\_PRESET\_16\_1\_GS

| #define BT\_GMAP\_LC3\_PRESET\_16\_1\_GS | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \_loc, 30U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(7500u, 30U, 1U, 15U, 60000U))

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5

7.5 msec Frame Duration configuration

**Definition** audio.h:292

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ

16 Khz codec sampling frequency

**Definition** audio.h:256

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)

#define BT\_BAP\_LC3\_PRESET(\_codec, \_qos)

Helper to declare an LC3 preset structure.

**Definition** bap\_lc3\_preset.h:46

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)

#define BT\_BAP\_QOS\_CFG\_UNFRAMED(\_interval, \_sdu, \_rtn, \_latency, \_pd)

Helper to declare Input Unframed bt\_bap\_qos\_cfg.

**Definition** bap.h:110

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)

#define BT\_AUDIO\_CODEC\_LC3\_CONFIG(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu, \_stream\_context)

Helper to declare LC3 codec configuration.

**Definition** lc3.h:133

Helper to declare LC3 16\_1\_gs codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga900e8e6e308558d1e307c5726b26f00d)BT\_GMAP\_LC3\_PRESET\_16\_2\_GS

| #define BT\_GMAP\_LC3\_PRESET\_16\_2\_GS | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \_loc, 40U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(10000u, 40U, 1U, 20U, 60000U))

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION\_10

10 msec Frame Duration configuration

**Definition** audio.h:295

Helper to declare LC3 16\_2\_gs codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga6ec3341f2563494a10ae50bd709a6234)BT\_GMAP\_LC3\_PRESET\_32\_1\_GR

| #define BT\_GMAP\_LC3\_PRESET\_32\_1\_GR | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \_loc, 60U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(7500u, 60U, 1U, 15U, 10000U))

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ

32 Khz codec sampling frequency

**Definition** audio.h:265

Helper to declare LC3 32\_1\_gr codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gad2f2bf8f120332be58c8d3dbfe4e2c48)BT\_GMAP\_LC3\_PRESET\_32\_1\_GS

| #define BT\_GMAP\_LC3\_PRESET\_32\_1\_GS | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \_loc, 60U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(7500u, 60U, 1U, 15U, 60000U))

Helper to declare LC3 32\_1\_gs codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga7500c49ffb1d0cbb50faaab296954a9c)BT\_GMAP\_LC3\_PRESET\_32\_2\_GR

| #define BT\_GMAP\_LC3\_PRESET\_32\_2\_GR | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \_loc, 80U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(10000u, 80U, 1U, 20U, 10000U))

Helper to declare LC3 32\_2\_gr codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga0261c82920c16db61c2a551b44ea549f)BT\_GMAP\_LC3\_PRESET\_32\_2\_GS

| #define BT\_GMAP\_LC3\_PRESET\_32\_2\_GS | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \_loc, 80U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(10000u, 80U, 1U, 20U, 60000U))

Helper to declare LC3 32\_2\_gs codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga50562ea208350e7669255613fe4bef14)BT\_GMAP\_LC3\_PRESET\_48\_1\_G

| #define BT\_GMAP\_LC3\_PRESET\_48\_1\_G | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \_loc, 75U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(7500u, 75U, 1U, 8U, 10000U))

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ

48 Khz codec sampling frequency

**Definition** audio.h:271

Helper to declare LC3 48\_1\_g codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gac5fbc4c6cd39292baaddfabe0a91547b)BT\_GMAP\_LC3\_PRESET\_48\_1\_GR

| #define BT\_GMAP\_LC3\_PRESET\_48\_1\_GR | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \_loc, 75U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(7500u, 75U, 1U, 15U, 10000U))

Helper to declare LC3 48\_1\_gr codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga258ac93490e61fbf82e69afa441cbeca)BT\_GMAP\_LC3\_PRESET\_48\_1\_GS

| #define BT\_GMAP\_LC3\_PRESET\_48\_1\_GS | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \_loc, 75U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(7500u, 75U, 1U, 15U, 60000U))

Helper to declare LC3 48\_1\_gs codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gad65b1c65aa9943e80934cbf7234646dc)BT\_GMAP\_LC3\_PRESET\_48\_2\_G

| #define BT\_GMAP\_LC3\_PRESET\_48\_2\_G | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \_loc, 100U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(10000u, 100U, 1U, 10U, 10000U))

Helper to declare LC3 48\_2\_g codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga43266a8272f9d38ccfc7f845fb872bfa)BT\_GMAP\_LC3\_PRESET\_48\_2\_GR

| #define BT\_GMAP\_LC3\_PRESET\_48\_2\_GR | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \_loc, 100U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(10000u, 100U, 1U, 20U, 10000U))

Helper to declare LC3 48\_2\_gr codec configuration.

Mandatory to support as both unicast client and server

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga4136fc4f83ebafb9d7574f7c750840aa)BT\_GMAP\_LC3\_PRESET\_48\_2\_GS

| #define BT\_GMAP\_LC3\_PRESET\_48\_2\_GS | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \_loc, 100U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(10000u, 100U, 1U, 20U, 60000U))

Helper to declare LC3 48\_2\_gs codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gabe6f21e869b54c962633ab3ac6be7a91)BT\_GMAP\_LC3\_PRESET\_48\_3\_G

| #define BT\_GMAP\_LC3\_PRESET\_48\_3\_G | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \_loc, 90U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(7500u, 90U, 1U, 8U, 10000U))

Helper to declare LC3 48\_3\_g codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga4b904abf0faf7ffef5e8680c90f861a6)BT\_GMAP\_LC3\_PRESET\_48\_3\_GR

| #define BT\_GMAP\_LC3\_PRESET\_48\_3\_GR | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \_loc, 90U, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(7500u, 90U, 1U, 15U, 10000U))

Helper to declare LC3 48\_3\_gr codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga17d79f07ced6f8605abb88cedad5a4da)BT\_GMAP\_LC3\_PRESET\_48\_4\_G

| #define BT\_GMAP\_LC3\_PRESET\_48\_4\_G | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \_loc, 120u, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(10000u, 120U, 1U, 10U, 10000U))

Helper to declare LC3 48\_4\_g codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga6d5438cd5121dc1853d185ce17278fac)BT\_GMAP\_LC3\_PRESET\_48\_4\_GR

| #define BT\_GMAP\_LC3\_PRESET\_48\_4\_GR | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[gmap_lc3_preset.h](gmap__lc3__preset_8h.md)>`

**Value:**

[BT\_BAP\_LC3\_PRESET](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), \

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \_loc, 120u, 1, \

\_stream\_context), \

[BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(10000u, 120U, 1U, 20U, 10000U))

Helper to declare LC3 48\_4\_gr codec configuration.

Mandatory to support as unicast server

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
