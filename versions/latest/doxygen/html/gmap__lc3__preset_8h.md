---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gmap__lc3__preset_8h.html
original_path: doxygen/html/gmap__lc3__preset_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gmap\_lc3\_preset.h File Reference

Header for Bluetooth GMAP LC3 presets.
[More...](#details)

`#include <[zephyr/bluetooth/audio/bap_lc3_preset.h](bap__lc3__preset_8h_source.md)>`

[Go to the source code of this file.](gmap__lc3__preset_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BT\_GMAP\_LC3\_PRESET\_32\_1\_GR](#a6ec3341f2563494a10ae50bd709a6234)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 32\_1\_gr codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_32\_2\_GR](#a7500c49ffb1d0cbb50faaab296954a9c)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 32\_2\_gr codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_1\_GR](#ac5fbc4c6cd39292baaddfabe0a91547b)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_1\_gr codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_2\_GR](#a43266a8272f9d38ccfc7f845fb872bfa)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_2\_gr codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_3\_GR](#a4b904abf0faf7ffef5e8680c90f861a6)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_3\_gr codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_4\_GR](#a6d5438cd5121dc1853d185ce17278fac)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_4\_gr codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_16\_1\_GS](#a01fd21cc55b4edbef612e704fc26fa0e)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 16\_1\_gs codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_16\_2\_GS](#a900e8e6e308558d1e307c5726b26f00d)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 16\_2\_gs codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_32\_1\_GS](#ad2f2bf8f120332be58c8d3dbfe4e2c48)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 32\_1\_gs codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_32\_2\_GS](#a0261c82920c16db61c2a551b44ea549f)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 32\_2\_gs codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_1\_GS](#a258ac93490e61fbf82e69afa441cbeca)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_1\_gs codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_2\_GS](#a4136fc4f83ebafb9d7574f7c750840aa)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_2\_gs codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_1\_G](#a50562ea208350e7669255613fe4bef14)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_1\_g codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_2\_G](#ad65b1c65aa9943e80934cbf7234646dc)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_2\_g codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_3\_G](#abe6f21e869b54c962633ab3ac6be7a91)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_3\_g codec configuration. |
| #define | [BT\_GMAP\_LC3\_PRESET\_48\_4\_G](#a17d79f07ced6f8605abb88cedad5a4da)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48\_4\_g codec configuration. |

## Detailed Description

Header for Bluetooth GMAP LC3 presets.

Copyright (c) 2023 Nordic Semiconductor ASA

SPDX-License-Identifier: Apache-2.0

## Macro Definition Documentation

## [◆ ](#a01fd21cc55b4edbef612e704fc26fa0e)BT\_GMAP\_LC3\_PRESET\_16\_1\_GS

| #define BT\_GMAP\_LC3\_PRESET\_16\_1\_GS | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1](group__BT__AUDIO__CODEC__LC3.md#gaff29f4ccabab99c7e25fcbf9d10cc789)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#gac5e29e3c02fc24e5bb1208ea12c1f707)(30U, 1U, 15U, 60000U))

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)

#define BT\_BAP\_LC3\_PRESET(\_codec, \_qos)

Helper to declare an LC3 preset structure.

**Definition** bap\_lc3\_preset.h:23

[BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#gac5e29e3c02fc24e5bb1208ea12c1f707)

#define BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(\_sdu, \_rtn, \_latency, \_pd)

Helper to declare LC3 codec QoS for 7.5ms interval unframed input.

**Definition** lc3.h:282

[BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1](group__BT__AUDIO__CODEC__LC3.md#gaff29f4ccabab99c7e25fcbf9d10cc789)

#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1(\_loc, \_stream\_context)

Helper to declare LC3 16.1 codec configuration.

**Definition** lc3.h:153

Helper to declare LC3 16\_1\_gs codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#a900e8e6e308558d1e307c5726b26f00d)BT\_GMAP\_LC3\_PRESET\_16\_2\_GS

| #define BT\_GMAP\_LC3\_PRESET\_16\_2\_GS | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2](group__BT__AUDIO__CODEC__LC3.md#gabf16c8c87682fd9faf180af129bddfd5)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#ga57083d5045a806cc710b899b8de54b7d)(40U, 1U, 20U, 60000U))

[BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#ga57083d5045a806cc710b899b8de54b7d)

#define BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(\_sdu, \_rtn, \_latency, \_pd)

Helper to declare LC3 codec QoS for 10ms interval unframed input.

**Definition** lc3.h:292

[BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2](group__BT__AUDIO__CODEC__LC3.md#gabf16c8c87682fd9faf180af129bddfd5)

#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2(\_loc, \_stream\_context)

Helper to declare LC3 16.2 codec configuration.

**Definition** lc3.h:162

Helper to declare LC3 16\_2\_gs codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#a6ec3341f2563494a10ae50bd709a6234)BT\_GMAP\_LC3\_PRESET\_32\_1\_GR

| #define BT\_GMAP\_LC3\_PRESET\_32\_1\_GR | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1](group__BT__AUDIO__CODEC__LC3.md#ga57a7bf0bbf38e70cfc27e1c267092277)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#gac5e29e3c02fc24e5bb1208ea12c1f707)(60U, 1U, 15U, 10000U))

[BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1](group__BT__AUDIO__CODEC__LC3.md#ga57a7bf0bbf38e70cfc27e1c267092277)

#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1(\_loc, \_stream\_context)

Helper to declare LC3 32.1 codec configuration.

**Definition** lc3.h:190

Helper to declare LC3 32\_1\_gr codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ad2f2bf8f120332be58c8d3dbfe4e2c48)BT\_GMAP\_LC3\_PRESET\_32\_1\_GS

| #define BT\_GMAP\_LC3\_PRESET\_32\_1\_GS | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1](group__BT__AUDIO__CODEC__LC3.md#ga57a7bf0bbf38e70cfc27e1c267092277)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#gac5e29e3c02fc24e5bb1208ea12c1f707)(60U, 1U, 15U, 60000U))

Helper to declare LC3 32\_1\_gs codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#a7500c49ffb1d0cbb50faaab296954a9c)BT\_GMAP\_LC3\_PRESET\_32\_2\_GR

| #define BT\_GMAP\_LC3\_PRESET\_32\_2\_GR | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2](group__BT__AUDIO__CODEC__LC3.md#ga25879311182d38adaca5238cdf016ac4)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#ga57083d5045a806cc710b899b8de54b7d)(80U, 1U, 20U, 10000U))

[BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2](group__BT__AUDIO__CODEC__LC3.md#ga25879311182d38adaca5238cdf016ac4)

#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2(\_loc, \_stream\_context)

Helper to declare LC3 32.2 codec configuration.

**Definition** lc3.h:199

Helper to declare LC3 32\_2\_gr codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#a0261c82920c16db61c2a551b44ea549f)BT\_GMAP\_LC3\_PRESET\_32\_2\_GS

| #define BT\_GMAP\_LC3\_PRESET\_32\_2\_GS | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2](group__BT__AUDIO__CODEC__LC3.md#ga25879311182d38adaca5238cdf016ac4)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#ga57083d5045a806cc710b899b8de54b7d)(80U, 1U, 20U, 60000U))

Helper to declare LC3 32\_2\_gs codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#a50562ea208350e7669255613fe4bef14)BT\_GMAP\_LC3\_PRESET\_48\_1\_G

| #define BT\_GMAP\_LC3\_PRESET\_48\_1\_G | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1](group__BT__AUDIO__CODEC__LC3.md#ga613c2f21212b626f83e37c5614e7129e)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#gac5e29e3c02fc24e5bb1208ea12c1f707)(75U, 1U, 8U, 10000U))

[BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1](group__BT__AUDIO__CODEC__LC3.md#ga613c2f21212b626f83e37c5614e7129e)

#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1(\_loc, \_stream\_context)

Helper to declare LC3 48.1 codec configuration.

**Definition** lc3.h:226

Helper to declare LC3 48\_1\_g codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ac5fbc4c6cd39292baaddfabe0a91547b)BT\_GMAP\_LC3\_PRESET\_48\_1\_GR

| #define BT\_GMAP\_LC3\_PRESET\_48\_1\_GR | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1](group__BT__AUDIO__CODEC__LC3.md#ga613c2f21212b626f83e37c5614e7129e)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#gac5e29e3c02fc24e5bb1208ea12c1f707)(75U, 1U, 15U, 10000U))

Helper to declare LC3 48\_1\_gr codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#a258ac93490e61fbf82e69afa441cbeca)BT\_GMAP\_LC3\_PRESET\_48\_1\_GS

| #define BT\_GMAP\_LC3\_PRESET\_48\_1\_GS | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1](group__BT__AUDIO__CODEC__LC3.md#ga613c2f21212b626f83e37c5614e7129e)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#gac5e29e3c02fc24e5bb1208ea12c1f707)(75U, 1U, 15U, 60000U))

Helper to declare LC3 48\_1\_gs codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ad65b1c65aa9943e80934cbf7234646dc)BT\_GMAP\_LC3\_PRESET\_48\_2\_G

| #define BT\_GMAP\_LC3\_PRESET\_48\_2\_G | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2](group__BT__AUDIO__CODEC__LC3.md#gab5342debdef776007a78576f8d0917dd)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#ga57083d5045a806cc710b899b8de54b7d)(100U, 1U, 10U, 10000U))

[BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2](group__BT__AUDIO__CODEC__LC3.md#gab5342debdef776007a78576f8d0917dd)

#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2(\_loc, \_stream\_context)

Helper to declare LC3 48.2 codec configuration.

**Definition** lc3.h:235

Helper to declare LC3 48\_2\_g codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#a43266a8272f9d38ccfc7f845fb872bfa)BT\_GMAP\_LC3\_PRESET\_48\_2\_GR

| #define BT\_GMAP\_LC3\_PRESET\_48\_2\_GR | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2](group__BT__AUDIO__CODEC__LC3.md#gab5342debdef776007a78576f8d0917dd)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#ga57083d5045a806cc710b899b8de54b7d)(100U, 1U, 20U, 10000U))

Helper to declare LC3 48\_2\_gr codec configuration.

Mandatory to support as both unicast client and server

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#a4136fc4f83ebafb9d7574f7c750840aa)BT\_GMAP\_LC3\_PRESET\_48\_2\_GS

| #define BT\_GMAP\_LC3\_PRESET\_48\_2\_GS | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2](group__BT__AUDIO__CODEC__LC3.md#gab5342debdef776007a78576f8d0917dd)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#ga57083d5045a806cc710b899b8de54b7d)(100U, 1U, 20U, 60000U))

Helper to declare LC3 48\_2\_gs codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#abe6f21e869b54c962633ab3ac6be7a91)BT\_GMAP\_LC3\_PRESET\_48\_3\_G

| #define BT\_GMAP\_LC3\_PRESET\_48\_3\_G | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3](group__BT__AUDIO__CODEC__LC3.md#ga60f65e6c9b9f940a66756f91c82cd64e)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#gac5e29e3c02fc24e5bb1208ea12c1f707)(90U, 1U, 8U, 10000U))

[BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3](group__BT__AUDIO__CODEC__LC3.md#ga60f65e6c9b9f940a66756f91c82cd64e)

#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3(\_loc, \_stream\_context)

Helper to declare LC3 48.3 codec configuration.

**Definition** lc3.h:244

Helper to declare LC3 48\_3\_g codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#a4b904abf0faf7ffef5e8680c90f861a6)BT\_GMAP\_LC3\_PRESET\_48\_3\_GR

| #define BT\_GMAP\_LC3\_PRESET\_48\_3\_GR | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3](group__BT__AUDIO__CODEC__LC3.md#ga60f65e6c9b9f940a66756f91c82cd64e)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#gac5e29e3c02fc24e5bb1208ea12c1f707)(90U, 1U, 15U, 10000U))

Helper to declare LC3 48\_3\_gr codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#a17d79f07ced6f8605abb88cedad5a4da)BT\_GMAP\_LC3\_PRESET\_48\_4\_G

| #define BT\_GMAP\_LC3\_PRESET\_48\_4\_G | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4](group__BT__AUDIO__CODEC__LC3.md#gaefa8bdddf5b56cad4b9096eac1abb49d)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#ga57083d5045a806cc710b899b8de54b7d)(120U, 1U, 10U, 10000U))

[BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4](group__BT__AUDIO__CODEC__LC3.md#gaefa8bdddf5b56cad4b9096eac1abb49d)

#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4(\_loc, \_stream\_context)

Helper to declare LC3 48.4 codec configuration.

**Definition** lc3.h:253

Helper to declare LC3 48\_4\_g codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#a6d5438cd5121dc1853d185ce17278fac)BT\_GMAP\_LC3\_PRESET\_48\_4\_GR

| #define BT\_GMAP\_LC3\_PRESET\_48\_4\_GR | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

**Value:**

[BT\_BAP\_LC3\_PRESET](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)([BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4](group__BT__AUDIO__CODEC__LC3.md#gaefa8bdddf5b56cad4b9096eac1abb49d)(\_loc, \_stream\_context), \

[BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#ga57083d5045a806cc710b899b8de54b7d)(120U, 1U, 20U, 10000U))

Helper to declare LC3 48\_4\_gr codec configuration.

Mandatory to support as unicast server

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [gmap\_lc3\_preset.h](gmap__lc3__preset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
