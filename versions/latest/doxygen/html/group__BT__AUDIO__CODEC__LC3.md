---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__BT__AUDIO__CODEC__LC3.html
original_path: doxygen/html/group__BT__AUDIO__CODEC__LC3.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

AUDIO

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

LC3.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA](#ga8d679b241585ff5ebff0d97bb22dfda9)(\_freq, \_duration, \_chan\_count, \_len\_min, \_len\_max, \_max\_frames\_per\_sdu) |
|  | Helper to declare LC3 codec capability. |
| #define | [BT\_AUDIO\_CODEC\_CAP\_LC3\_META](#ga9b5d5e300a7b41060329dbdd2cd073f6)(\_prefer\_context) |
|  | Helper to declare LC3 codec metadata. |
| #define | [BT\_AUDIO\_CODEC\_CAP\_LC3](#gac474746e7314ebf7ed77b8937191cdc1)(\_freq, \_duration, \_chan\_count, \_len\_min, \_len\_max, \_max\_frames\_per\_sdu, \_prefer\_context) |
|  | Helper to declare LC3 codec. |
| #define | [BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA](#ga497ff0aa1d7dcfeea6ec549e5fb155d6)(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu) |
|  | Helper to declare LC3 codec data configuration. |
| #define | [BT\_AUDIO\_CODEC\_CFG\_LC3\_META](#ga2c00f8bd526305d878624c6f1b8030f8)(\_stream\_context) |
|  | Helper to declare LC3 codec metadata configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu, \_stream\_context) |
|  | Helper to declare LC3 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_1](#gaee65a79f2bb704bf5296b778a0e3ad2c)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 8.1 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_2](#gae279ffa1d4eef72d94083bdae968c102)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 8.2 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1](#gaff29f4ccabab99c7e25fcbf9d10cc789)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 16.1 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2](#gabf16c8c87682fd9faf180af129bddfd5)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 16.2 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_1](#ga0655c6ca0c99002493a854cb88969a2b)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 24.1 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_2](#gae8c8a34377b910f52d851dadb9f4216b)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 24.2 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1](#ga57a7bf0bbf38e70cfc27e1c267092277)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 32.1 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2](#ga25879311182d38adaca5238cdf016ac4)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 32.2 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_1](#gad046616ed5367d1e2c674df545def632)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 441.1 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_2](#ga7789d2447105581e5e520c930f19f8ed)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 441.2 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1](#ga613c2f21212b626f83e37c5614e7129e)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48.1 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2](#gab5342debdef776007a78576f8d0917dd)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48.2 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3](#ga60f65e6c9b9f940a66756f91c82cd64e)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48.3 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4](#gaefa8bdddf5b56cad4b9096eac1abb49d)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48.4 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_5](#ga3366230cd60d3e3b05e7cb2a56cfdd26)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48.5 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_6](#ga428a49b8528e62f6f686837dc95ba1b6)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48.6 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5](#ga5bfa82c8858a4fb3fcd7ce26afbd7601)(\_framing, \_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare LC3 codec QoS for 7.5ms interval. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED](#gac5e29e3c02fc24e5bb1208ea12c1f707)(\_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare LC3 codec QoS for 7.5ms interval unframed input. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_QOS\_10](#gad951d0fb06dfe085db73228eef500bbc)(\_framing, \_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare LC3 codec QoS for 10ms frame internal. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED](#ga57083d5045a806cc710b899b8de54b7d)(\_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare LC3 codec QoS for 10ms interval unframed input. |

## Detailed Description

LC3.

## Macro Definition Documentation

## [◆ ](#gac474746e7314ebf7ed77b8937191cdc1)BT\_AUDIO\_CODEC\_CAP\_LC3

| #define BT\_AUDIO\_CODEC\_CAP\_LC3 | ( |  | *\_freq*, |
| --- | --- | --- | --- |
|  |  |  | *\_duration*, |
|  |  |  | *\_chan\_count*, |
|  |  |  | *\_len\_min*, |
|  |  |  | *\_len\_max*, |
|  |  |  | *\_max\_frames\_per\_sdu*, |
|  |  |  | *\_prefer\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_CAP](group__bt__audio.md#ga6b99f589f6cdcd9e48a83f729a7a4698)([BT\_HCI\_CODING\_FORMAT\_LC3](hci__types_8h.md#a1fa62d6f28ef56ebe9c18d5ab86fbf8e), 0x0000, 0x0000, \

[BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA](#ga8d679b241585ff5ebff0d97bb22dfda9)(\_freq, \_duration, \_chan\_count, \_len\_min, \

\_len\_max, \_max\_frames\_per\_sdu), \

[BT\_AUDIO\_CODEC\_CAP\_LC3\_META](#ga9b5d5e300a7b41060329dbdd2cd073f6)(\_prefer\_context))

[BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA](#ga8d679b241585ff5ebff0d97bb22dfda9)

#define BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA(\_freq, \_duration, \_chan\_count, \_len\_min, \_len\_max, \_max\_frames\_per\_sdu)

Helper to declare LC3 codec capability.

**Definition** lc3.h:41

[BT\_AUDIO\_CODEC\_CAP\_LC3\_META](#ga9b5d5e300a7b41060329dbdd2cd073f6)

#define BT\_AUDIO\_CODEC\_CAP\_LC3\_META(\_prefer\_context)

Helper to declare LC3 codec metadata.

**Definition** lc3.h:58

[BT\_AUDIO\_CODEC\_CAP](group__bt__audio.md#ga6b99f589f6cdcd9e48a83f729a7a4698)

#define BT\_AUDIO\_CODEC\_CAP(\_id, \_cid, \_vid, \_data, \_meta)

Helper to declare Codec capability parsing APIs structure.

**Definition** audio.h:467

[BT\_HCI\_CODING\_FORMAT\_LC3](hci__types_8h.md#a1fa62d6f28ef56ebe9c18d5ab86fbf8e)

#define BT\_HCI\_CODING\_FORMAT\_LC3

**Definition** hci\_types.h:785

Helper to declare LC3 codec.

Parameters
:   | \_freq | Supported Sampling Frequencies bitfield (see BT\_AUDIO\_CODEC\_CAP\_FREQ\_\*) |
    | --- | --- |
    | \_duration | Supported Frame Durations bitfield (see BT\_AUDIO\_CODEC\_CAP\_DURATION\_\*) |
    | \_chan\_count | Supported channels (see [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_SUPPORT](group__bt__audio.md#ga8f835266fabd6461216fe13e1b3b3a0f "BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT")) |
    | \_len\_min | Minimum number of octets supported per codec frame |
    | \_len\_max | Maximum number of octets supported per codec frame |
    | \_max\_frames\_per\_sdu | Supported maximum codec frames per SDU |
    | \_prefer\_context | Preferred contexts ([bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3 "bt_audio_context")) |

## [◆ ](#ga8d679b241585ff5ebff0d97bb22dfda9)BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA

| #define BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA | ( |  | *\_freq*, |
| --- | --- | --- | --- |
|  |  |  | *\_duration*, |
|  |  |  | *\_chan\_count*, |
|  |  |  | *\_len\_min*, |
|  |  |  | *\_len\_max*, |
|  |  |  | *\_max\_frames\_per\_sdu* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

{ \

BT\_AUDIO\_CODEC\_DATA([BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b), [BT\_BYTES\_LIST\_LE16](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)(\_freq)), \

BT\_AUDIO\_CODEC\_DATA([BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510), (\_duration)), \

BT\_AUDIO\_CODEC\_DATA([BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191), (\_chan\_count)), \

BT\_AUDIO\_CODEC\_DATA([BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46), \

[BT\_BYTES\_LIST\_LE16](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)(\_len\_min), \

[BT\_BYTES\_LIST\_LE16](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)(\_len\_max)), \

COND\_CODE\_1(\_max\_frames\_per\_sdu, (), \

([BT\_AUDIO\_CODEC\_DATA](group__bt__audio.md#gaddc49e39465798ae4c0cbe345e0b50d7)([BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41), \

(\_max\_frames\_per\_sdu)))) \

}

[BT\_AUDIO\_CODEC\_DATA](group__bt__audio.md#gaddc49e39465798ae4c0cbe345e0b50d7)

#define BT\_AUDIO\_CODEC\_DATA(\_type, \_bytes...)

Helper to declare elements of bt\_audio\_codec\_cap arrays.

**Definition** audio.h:432

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT

Supported audio channel counts.

**Definition** audio.h:58

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION

Supported frame durations.

**Definition** audio.h:55

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT

Supported maximum codec frames per SDU.

**Definition** audio.h:64

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN

Supported octets per codec frame.

**Definition** audio.h:61

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ

Supported sampling frequencies.

**Definition** audio.h:52

[BT\_BYTES\_LIST\_LE16](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)

#define BT\_BYTES\_LIST\_LE16(\_v)

Encode 16-bit value into array values in little-endian format.

**Definition** byteorder.h:36

Helper to declare LC3 codec capability.

\_max\_frames\_per\_sdu value is optional and will be included only if != 1

## [◆ ](#ga9b5d5e300a7b41060329dbdd2cd073f6)BT\_AUDIO\_CODEC\_CAP\_LC3\_META

| #define BT\_AUDIO\_CODEC\_CAP\_LC3\_META | ( |  | *\_prefer\_context* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

{ \

BT\_AUDIO\_CODEC\_DATA([BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a), \

[BT\_BYTES\_LIST\_LE16](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)(\_prefer\_context)) \

}

[BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a)

@ BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT

Preferred audio context.

**Definition** audio.h:360

Helper to declare LC3 codec metadata.

## [◆ ](#ga497ff0aa1d7dcfeea6ec549e5fb155d6)BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA

| #define BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA | ( |  | *\_freq*, |
| --- | --- | --- | --- |
|  |  |  | *\_duration*, |
|  |  |  | *\_loc*, |
|  |  |  | *\_len*, |
|  |  |  | *\_frames\_per\_sdu* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

{ \

BT\_AUDIO\_CODEC\_DATA([BT\_AUDIO\_CODEC\_CFG\_FREQ](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3), (\_freq)), \

BT\_AUDIO\_CODEC\_DATA([BT\_AUDIO\_CODEC\_CFG\_DURATION](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223), (\_duration)), \

BT\_AUDIO\_CODEC\_DATA([BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2), [BT\_BYTES\_LIST\_LE32](group__bt__byteorder.md#ga0bf0275f0eea70eb5ae6002edeb1b812)(\_loc)), \

BT\_AUDIO\_CODEC\_DATA([BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2), [BT\_BYTES\_LIST\_LE16](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)(\_len)), \

COND\_CODE\_1(\_frames\_per\_sdu, (), \

([BT\_AUDIO\_CODEC\_DATA](group__bt__audio.md#gaddc49e39465798ae4c0cbe345e0b50d7)([BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8), \

(\_frames\_per\_sdu)))) \

}

[BT\_AUDIO\_CODEC\_CFG\_FREQ](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ

Sampling frequency.

**Definition** audio.h:214

[BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2)

@ BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN

Octets per codec frame.

**Definition** audio.h:223

[BT\_AUDIO\_CODEC\_CFG\_DURATION](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION

Frame duration.

**Definition** audio.h:217

[BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8)

@ BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU

Codec frame blocks per SDU.

**Definition** audio.h:226

[BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2)

@ BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC

Audio channel allocation.

**Definition** audio.h:220

[BT\_BYTES\_LIST\_LE32](group__bt__byteorder.md#ga0bf0275f0eea70eb5ae6002edeb1b812)

#define BT\_BYTES\_LIST\_LE32(\_v)

Encode 32-bit value into array values in little-endian format.

**Definition** byteorder.h:64

Helper to declare LC3 codec data configuration.

Parameters
:   | \_freq | Sampling frequency (BT\_AUDIO\_CODEC\_CFG\_FREQ\_\*) |
    | --- | --- |
    | \_duration | Frame duration (BT\_AUDIO\_CODEC\_CFG\_DURATION\_\*) |
    | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | \_len | Octets per frame (16-bit integer) |
    | \_frames\_per\_sdu | Frames per SDU (8-bit integer). This value is optional and will be included only if != 1 |

## [◆ ](#ga2c00f8bd526305d878624c6f1b8030f8)BT\_AUDIO\_CODEC\_CFG\_LC3\_META

| #define BT\_AUDIO\_CODEC\_CFG\_LC3\_META | ( |  | *\_stream\_context* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

{ \

BT\_AUDIO\_CODEC\_DATA([BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa), \

[BT\_BYTES\_LIST\_LE16](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)(\_stream\_context)) \

}

[BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa)

@ BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT

Streaming audio context.

**Definition** audio.h:371

Helper to declare LC3 codec metadata configuration.

## [◆ ](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)BT\_AUDIO\_CODEC\_LC3\_CONFIG

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG | ( |  | *\_freq*, |
| --- | --- | --- | --- |
|  |  |  | *\_duration*, |
|  |  |  | *\_loc*, |
|  |  |  | *\_len*, |
|  |  |  | *\_frames\_per\_sdu*, |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_CFG](group__bt__audio.md#gaefed7a013e282c63c9b5cbbdcdc67448)( \

[BT\_HCI\_CODING\_FORMAT\_LC3](hci__types_8h.md#a1fa62d6f28ef56ebe9c18d5ab86fbf8e), 0x0000, 0x0000, \

[BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA](#ga497ff0aa1d7dcfeea6ec549e5fb155d6)(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu), \

[BT\_AUDIO\_CODEC\_CFG\_LC3\_META](#ga2c00f8bd526305d878624c6f1b8030f8)(\_stream\_context))

[BT\_AUDIO\_CODEC\_CFG\_LC3\_META](#ga2c00f8bd526305d878624c6f1b8030f8)

#define BT\_AUDIO\_CODEC\_CFG\_LC3\_META(\_stream\_context)

Helper to declare LC3 codec metadata configuration.

**Definition** lc3.h:107

[BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA](#ga497ff0aa1d7dcfeea6ec549e5fb155d6)

#define BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu)

Helper to declare LC3 codec data configuration.

**Definition** lc3.h:93

[BT\_AUDIO\_CODEC\_CFG](group__bt__audio.md#gaefed7a013e282c63c9b5cbbdcdc67448)

#define BT\_AUDIO\_CODEC\_CFG(\_id, \_cid, \_vid, \_data, \_meta)

Helper to declare Codec config parsing APIs.

**Definition** audio.h:444

Helper to declare LC3 codec configuration.

Parameters
:   | \_freq | Sampling frequency (BT\_AUDIO\_CODEC\_CFG\_FREQ\_\*) |
    | --- | --- |
    | \_duration | Frame duration (BT\_AUDIO\_CODEC\_CFG\_DURATION\_\*) |
    | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | \_len | Octets per frame (16-bit integer) |
    | \_frames\_per\_sdu | Frames per SDU (8-bit integer) |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gaff29f4ccabab99c7e25fcbf9d10cc789)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \

\_loc, 30u, 1, \_stream\_context)

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)

#define BT\_AUDIO\_CODEC\_LC3\_CONFIG(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu, \_stream\_context)

Helper to declare LC3 codec configuration.

**Definition** lc3.h:123

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5

7.5 msec Frame Duration configuration

**Definition** audio.h:272

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ

16 Khz codec sampling frequency

**Definition** audio.h:237

Helper to declare LC3 16.1 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gabf16c8c87682fd9faf180af129bddfd5)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \

\_loc, 40u, 1, \_stream\_context)

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION\_10

10 msec Frame Duration configuration

**Definition** audio.h:275

Helper to declare LC3 16.2 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga0655c6ca0c99002493a854cb88969a2b)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_1

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_1 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \

\_loc, 45u, 1, \_stream\_context)

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ

24 Khz codec sampling frequency

**Definition** audio.h:243

Helper to declare LC3 24.1 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gae8c8a34377b910f52d851dadb9f4216b)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_2

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_2 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \

\_loc, 60u, 1, \_stream\_context)

Helper to declare LC3 24.2 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga57a7bf0bbf38e70cfc27e1c267092277)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \

\_loc, 60u, 1, \_stream\_context)

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ

32 Khz codec sampling frequency

**Definition** audio.h:246

Helper to declare LC3 32.1 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga25879311182d38adaca5238cdf016ac4)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \

\_loc, 80u, 1, \_stream\_context)

Helper to declare LC3 32.2 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gad046616ed5367d1e2c674df545def632)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_1

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_1 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \

\_loc, 98u, 1, \_stream\_context)

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ

44.1 Khz codec sampling frequency

**Definition** audio.h:249

Helper to declare LC3 441.1 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga7789d2447105581e5e520c930f19f8ed)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_2

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_2 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \

\_loc, 130u, 1, \_stream\_context)

Helper to declare LC3 441.2 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga613c2f21212b626f83e37c5614e7129e)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \

\_loc, 75u, 1, \_stream\_context)

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ

48 Khz codec sampling frequency

**Definition** audio.h:252

Helper to declare LC3 48.1 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gab5342debdef776007a78576f8d0917dd)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \

\_loc, 100u, 1, \_stream\_context)

Helper to declare LC3 48.2 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga60f65e6c9b9f940a66756f91c82cd64e)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \

\_loc, 90u, 1, \_stream\_context)

Helper to declare LC3 48.3 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gaefa8bdddf5b56cad4b9096eac1abb49d)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \

\_loc, 120u, 1, \_stream\_context)

Helper to declare LC3 48.4 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga3366230cd60d3e3b05e7cb2a56cfdd26)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_5

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_5 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \

\_loc, 117u, 1, \_stream\_context)

Helper to declare LC3 48.5 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#ga428a49b8528e62f6f686837dc95ba1b6)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_6

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_6 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \

\_loc, 155u, 1, \_stream\_context)

Helper to declare LC3 48.6 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gaee65a79f2bb704bf5296b778a0e3ad2c)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_1

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_1 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272), \

\_loc, 26u, 1, \_stream\_context)

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ

8 Khz codec sampling frequency

**Definition** audio.h:231

Helper to declare LC3 8.1 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gae279ffa1d4eef72d94083bdae968c102)BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_2

| #define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_2 | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_stream\_context* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_LC3\_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)([BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a), [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7), \

\_loc, 30u, 1, \_stream\_context)

Helper to declare LC3 8.2 codec configuration.

Parameters
:   | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | --- | --- |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

## [◆ ](#gad951d0fb06dfe085db73228eef500bbc)BT\_AUDIO\_CODEC\_LC3\_QOS\_10

| #define BT\_AUDIO\_CODEC\_LC3\_QOS\_10 | ( |  | *\_framing*, |
| --- | --- | --- | --- |
|  |  |  | *\_sdu*, |
|  |  |  | *\_rtn*, |
|  |  |  | *\_latency*, |
|  |  |  | *\_pd* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_QOS](group__bt__audio.md#ga13e5148d62cb364602f01c75a88b615b)(10000u, \_framing, [BT\_AUDIO\_CODEC\_QOS\_2M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ac81306188ed29b8fa17aa2afa878f297), \_sdu, \_rtn, \_latency, \_pd)

[BT\_AUDIO\_CODEC\_QOS](group__bt__audio.md#ga13e5148d62cb364602f01c75a88b615b)

#define BT\_AUDIO\_CODEC\_QOS(\_interval, \_framing, \_phy, \_sdu, \_rtn, \_latency, \_pd)

Helper to declare elements of bt\_audio\_codec\_qos.

**Definition** audio.h:651

[BT\_AUDIO\_CODEC\_QOS\_2M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ac81306188ed29b8fa17aa2afa878f297)

@ BT\_AUDIO\_CODEC\_QOS\_2M

**Definition** audio.h:671

Helper to declare LC3 codec QoS for 10ms frame internal.

## [◆ ](#ga57083d5045a806cc710b899b8de54b7d)BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED

| #define BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED | ( |  | *\_sdu*, |
| --- | --- | --- | --- |
|  |  |  | *\_rtn*, |
|  |  |  | *\_latency*, |
|  |  |  | *\_pd* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_QOS\_UNFRAMED](group__bt__audio.md#gadfc744b32a0b40da9377bb3668004bc2)(10000u, \_sdu, \_rtn, \_latency, \_pd)

[BT\_AUDIO\_CODEC\_QOS\_UNFRAMED](group__bt__audio.md#gadfc744b32a0b40da9377bb3668004bc2)

#define BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(\_interval, \_sdu, \_rtn, \_latency, \_pd)

Helper to declare Input Unframed bt\_audio\_codec\_qos.

**Definition** audio.h:684

Helper to declare LC3 codec QoS for 10ms interval unframed input.

## [◆ ](#ga5bfa82c8858a4fb3fcd7ce26afbd7601)BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5

| #define BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5 | ( |  | *\_framing*, |
| --- | --- | --- | --- |
|  |  |  | *\_sdu*, |
|  |  |  | *\_rtn*, |
|  |  |  | *\_latency*, |
|  |  |  | *\_pd* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_QOS](group__bt__audio.md#ga13e5148d62cb364602f01c75a88b615b)(7500u, \_framing, [BT\_AUDIO\_CODEC\_QOS\_2M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ac81306188ed29b8fa17aa2afa878f297), \_sdu, \_rtn, \_latency, \_pd)

Helper to declare LC3 codec QoS for 7.5ms interval.

## [◆ ](#gac5e29e3c02fc24e5bb1208ea12c1f707)BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED

| #define BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED | ( |  | *\_sdu*, |
| --- | --- | --- | --- |
|  |  |  | *\_rtn*, |
|  |  |  | *\_latency*, |
|  |  |  | *\_pd* ) |

`#include <[lc3.h](lc3_8h.md)>`

**Value:**

[BT\_AUDIO\_CODEC\_QOS\_UNFRAMED](group__bt__audio.md#gadfc744b32a0b40da9377bb3668004bc2)(7500u, \_sdu, \_rtn, \_latency, \_pd)

Helper to declare LC3 codec QoS for 7.5ms interval unframed input.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
