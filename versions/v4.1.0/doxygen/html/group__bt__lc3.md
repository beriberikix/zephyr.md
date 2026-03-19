---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__lc3.html
original_path: doxygen/html/group__bt__lc3.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth LC3 codec

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

## Detailed Description

LC3.

Since
:   3.0

Version
:   0.8.0

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

[BT\_AUDIO\_CODEC\_CAP](group__bt__audio.md#ga6b99f589f6cdcd9e48a83f729a7a4698)

#define BT\_AUDIO\_CODEC\_CAP(\_id, \_cid, \_vid, \_data, \_meta)

Helper to declare Codec capability parsing APIs structure.

**Definition** audio.h:571

[BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA](#ga8d679b241585ff5ebff0d97bb22dfda9)

#define BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA(\_freq, \_duration, \_chan\_count, \_len\_min, \_len\_max, \_max\_frames\_per\_sdu)

Helper to declare LC3 codec capability.

**Definition** lc3.h:52

[BT\_AUDIO\_CODEC\_CAP\_LC3\_META](#ga9b5d5e300a7b41060329dbdd2cd073f6)

#define BT\_AUDIO\_CODEC\_CAP\_LC3\_META(\_prefer\_context)

Helper to declare LC3 codec metadata.

**Definition** lc3.h:71

[BT\_HCI\_CODING\_FORMAT\_LC3](hci__types_8h.md#a1fa62d6f28ef56ebe9c18d5ab86fbf8e)

#define BT\_HCI\_CODING\_FORMAT\_LC3

**Definition** hci\_types.h:920

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

**Definition** audio.h:536

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT

Supported audio channel counts.

**Definition** audio.h:74

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION

Supported frame durations.

**Definition** audio.h:71

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT

Supported maximum codec frames per SDU.

**Definition** audio.h:80

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN

Supported octets per codec frame.

**Definition** audio.h:77

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ

Supported sampling frequencies.

**Definition** audio.h:68

[BT\_BYTES\_LIST\_LE16](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)

#define BT\_BYTES\_LIST\_LE16(\_v)

Encode 16-bit value into array values in little-endian format.

**Definition** byteorder.h:36

Helper to declare LC3 codec capability.

`_max_frames_per_sdu` is optional and will be included only if != 1

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20 "COND_CODE_1") is used to omit an LTV entry in case the `_frames_per_sdu` is 1. [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20 "COND_CODE_1") will evaluate to second argument if the flag parameter(first argument) is 1

- removing one layer of paranteses. If the flags argument is != 1 it will evaluate to the third argument which inserts a LTV entry for the max\_frames\_per\_sdu value.

Parameters
:   | \_freq | Supported Sampling Frequencies bitfield (see BT\_AUDIO\_CODEC\_CAP\_FREQ\_\*) |
    | --- | --- |
    | \_duration | Supported Frame Durations bitfield (see BT\_AUDIO\_CODEC\_CAP\_DURATION\_\*) |
    | \_chan\_count | Supported channels (see [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_SUPPORT](group__bt__audio.md#ga8f835266fabd6461216fe13e1b3b3a0f "BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT")) |
    | \_len\_min | Minimum number of octets supported per codec frame |
    | \_len\_max | Maximum number of octets supported per codec frame |
    | \_max\_frames\_per\_sdu | Supported maximum codec frames per SDU |

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

**Definition** audio.h:443

Helper to declare LC3 codec metadata.

Parameters
:   | \_prefer\_context | Preferred contexts ([bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3 "bt_audio_context")) |
    | --- | --- |

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

**Definition** audio.h:232

[BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2)

@ BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN

Octets per codec frame.

**Definition** audio.h:241

[BT\_AUDIO\_CODEC\_CFG\_DURATION](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION

Frame duration.

**Definition** audio.h:235

[BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8)

@ BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU

Codec frame blocks per SDU.

**Definition** audio.h:244

[BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2)

@ BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC

Audio channel allocation.

**Definition** audio.h:238

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

**Definition** audio.h:455

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

[BT\_AUDIO\_CODEC\_CFG](group__bt__audio.md#gaefed7a013e282c63c9b5cbbdcdc67448)

#define BT\_AUDIO\_CODEC\_CFG(\_id, \_cid, \_vid, \_data, \_meta)

Helper to declare Codec config parsing APIs.

**Definition** audio.h:548

[BT\_AUDIO\_CODEC\_CFG\_LC3\_META](#ga2c00f8bd526305d878624c6f1b8030f8)

#define BT\_AUDIO\_CODEC\_CFG\_LC3\_META(\_stream\_context)

Helper to declare LC3 codec metadata configuration.

**Definition** lc3.h:117

[BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA](#ga497ff0aa1d7dcfeea6ec549e5fb155d6)

#define BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu)

Helper to declare LC3 codec data configuration.

**Definition** lc3.h:105

Helper to declare LC3 codec configuration.

Parameters
:   | \_freq | Sampling frequency (BT\_AUDIO\_CODEC\_CFG\_FREQ\_\*) |
    | --- | --- |
    | \_duration | Frame duration (BT\_AUDIO\_CODEC\_CFG\_DURATION\_\*) |
    | \_loc | Audio channel location bitfield ([bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location")) |
    | \_len | Octets per frame (16-bit integer) |
    | \_frames\_per\_sdu | Frames per SDU (8-bit integer) |
    | \_stream\_context | Stream context (BT\_AUDIO\_CONTEXT\_\*) |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
