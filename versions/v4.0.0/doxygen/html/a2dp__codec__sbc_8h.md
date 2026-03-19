---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/a2dp__codec__sbc_8h.html
original_path: doxygen/html/a2dp__codec__sbc_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

a2dp\_codec\_sbc.h File Reference

Advance Audio Distribution Profile - SBC Codec header.
[More...](#details)

[Go to the source code of this file.](a2dp__codec__sbc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md) |
|  | SBC Codec. [More...](structbt__a2dp__codec__sbc__params.md#details) |

| Macros | |
| --- | --- |
| #define | [A2DP\_SBC\_SAMP\_FREQ\_16000](#a054dbbaf58ccc3b64142008e3da31ca5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [A2DP\_SBC\_SAMP\_FREQ\_32000](#a8e4b5399fb5366770a42fd4dfeece220)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [A2DP\_SBC\_SAMP\_FREQ\_44100](#a57d7b85560b36603651fae6c055c32c6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [A2DP\_SBC\_SAMP\_FREQ\_48000](#a0ebafbef2cddd4b6c7c7990ca77db0f9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [A2DP\_SBC\_CH\_MODE\_MONO](#aa9b58737fa1561b684a20980ea0b6feb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [A2DP\_SBC\_CH\_MODE\_DUAL](#aab5ab0b151f0a150c392be2f4cc82def)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [A2DP\_SBC\_CH\_MODE\_STREO](#acc5be684b75804f72a28d025fc5cc9bb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [A2DP\_SBC\_CH\_MODE\_JOINT](#afcf64fa599e4d820dccdf40990f5ba39)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [A2DP\_SBC\_BLK\_LEN\_4](#a3abfc1c5202d2659055fc3480c2d3cc2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [A2DP\_SBC\_BLK\_LEN\_8](#aeb90df4a33ce9ebdfc38d873fd54abab)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [A2DP\_SBC\_BLK\_LEN\_12](#a9890a0cb8a813e010855c10fc4d22bf8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [A2DP\_SBC\_BLK\_LEN\_16](#a1cb9425713c325442652fb406557e52a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [A2DP\_SBC\_SUBBAND\_4](#ad5916cf243e40e5a674ceed13477023e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [A2DP\_SBC\_SUBBAND\_8](#a6b4bd1ef891c14c4f863c9623dcb63f7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [A2DP\_SBC\_ALLOC\_MTHD\_SNR](#a7e54f1c971e1fd63e52f0322e7f85105)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS](#a27d905ddf0fdb3dea4d3c12dd3ca33fe)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_A2DP\_SBC\_SAMP\_FREQ](#a5b9313959439cc91be71efa214383ef7)(cap) |
| #define | [BT\_A2DP\_SBC\_CHAN\_MODE](#a8d058052eb87cf22314395cc2581ac5d)(cap) |
| #define | [BT\_A2DP\_SBC\_BLK\_LEN](#a1721d8cc832b5a74306943074132369a)(cap) |
| #define | [BT\_A2DP\_SBC\_SUB\_BAND](#aa4eb6816559e80400f1767e230d0efdf)(cap) |
| #define | [BT\_A2DP\_SBC\_ALLOC\_MTHD](#a58878ea86ed87c6c5bfede0fe217ade8)(cap) |
| #define | [BT\_A2DP\_SBC\_MEDIA\_HDR\_NUM\_FRAMES\_GET](#a5d79c5a628c9740a81d5fe9626e14463)(hdr) |
|  | If the F bit is set to 0, this field indicates the number of frames contained in this packet. |
| #define | [BT\_A2DP\_SBC\_MEDIA\_HDR\_L\_GET](#ab84850ce399e236f10ef80f0d2d2acde)(hdr) |
|  | Set to 1 for the last packet of a fragmented SBC frame, otherwise set to 0. |
| #define | [BT\_A2DP\_SBC\_MEDIA\_HDR\_S\_GET](#a164ada24748d1fb21248274a02d11301)(hdr) |
|  | Set to 1 for the starting packet of a fragmented SBC frame, otherwise set to 0. |
| #define | [BT\_A2DP\_SBC\_MEDIA\_HDR\_F\_GET](#aaf18a29764a148b007f10e9a9f1a5437)(hdr) |
|  | Set to 1 if the SBC frame is fragmented, otherwise set to 0. |
| #define | [BT\_A2DP\_SBC\_MEDIA\_HDR\_NUM\_FRAMES\_SET](#af8da63e80785a6fa5a53fd29c6da5b9c)(hdr, val) |
|  | If the F bit is set to 0, this field indicates the number of frames contained in this packet. |
| #define | [BT\_A2DP\_SBC\_MEDIA\_HDR\_L\_SET](#a7f00326a7dcd0839da6ea8557303c45f)(hdr, val) |
|  | Set to 1 for the last packet of a fragmented SBC frame, otherwise set to 0. |
| #define | [BT\_A2DP\_SBC\_MEDIA\_HDR\_S\_SET](#a85bb7d78a1d654a68812517ddcebf76a)(hdr, val) |
|  | Set to 1 for the starting packet of a fragmented SBC frame, otherwise set to 0. |
| #define | [BT\_A2DP\_SBC\_MEDIA\_HDR\_F\_SET](#ab007b2c51612b05f9edc127bd9090536)(hdr, val) |
|  | Set to 1 if the SBC frame is fragmented, otherwise set to 0. |
| #define | [BT\_A2DP\_SBC\_MEDIA\_HDR\_ENCODE](#aa9a0484c4eefe685c0cbde87ce781734)(num\_frames, l, [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), f) |

| Functions | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_a2dp\_sbc\_get\_channel\_num](#a8791ff3f4f02b46ea879df5e20ba5dd6) (struct [bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md) \*sbc\_codec) |
|  | get channel num of a2dp sbc config. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [bt\_a2dp\_sbc\_get\_sampling\_frequency](#a7af2c05d2605d7d21e656222238922c1) (struct [bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md) \*sbc\_codec) |
|  | get sample rate of a2dp sbc config. |

## Detailed Description

Advance Audio Distribution Profile - SBC Codec header.

## Macro Definition Documentation

## [◆ ](#a27d905ddf0fdb3dea4d3c12dd3ca33fe)A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS

| #define A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a7e54f1c971e1fd63e52f0322e7f85105)A2DP\_SBC\_ALLOC\_MTHD\_SNR

| #define A2DP\_SBC\_ALLOC\_MTHD\_SNR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a9890a0cb8a813e010855c10fc4d22bf8)A2DP\_SBC\_BLK\_LEN\_12

| #define A2DP\_SBC\_BLK\_LEN\_12   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a1cb9425713c325442652fb406557e52a)A2DP\_SBC\_BLK\_LEN\_16

| #define A2DP\_SBC\_BLK\_LEN\_16   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a3abfc1c5202d2659055fc3480c2d3cc2)A2DP\_SBC\_BLK\_LEN\_4

| #define A2DP\_SBC\_BLK\_LEN\_4   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#aeb90df4a33ce9ebdfc38d873fd54abab)A2DP\_SBC\_BLK\_LEN\_8

| #define A2DP\_SBC\_BLK\_LEN\_8   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#aab5ab0b151f0a150c392be2f4cc82def)A2DP\_SBC\_CH\_MODE\_DUAL

| #define A2DP\_SBC\_CH\_MODE\_DUAL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#afcf64fa599e4d820dccdf40990f5ba39)A2DP\_SBC\_CH\_MODE\_JOINT

| #define A2DP\_SBC\_CH\_MODE\_JOINT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#aa9b58737fa1561b684a20980ea0b6feb)A2DP\_SBC\_CH\_MODE\_MONO

| #define A2DP\_SBC\_CH\_MODE\_MONO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#acc5be684b75804f72a28d025fc5cc9bb)A2DP\_SBC\_CH\_MODE\_STREO

| #define A2DP\_SBC\_CH\_MODE\_STREO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a054dbbaf58ccc3b64142008e3da31ca5)A2DP\_SBC\_SAMP\_FREQ\_16000

| #define A2DP\_SBC\_SAMP\_FREQ\_16000   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a8e4b5399fb5366770a42fd4dfeece220)A2DP\_SBC\_SAMP\_FREQ\_32000

| #define A2DP\_SBC\_SAMP\_FREQ\_32000   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a57d7b85560b36603651fae6c055c32c6)A2DP\_SBC\_SAMP\_FREQ\_44100

| #define A2DP\_SBC\_SAMP\_FREQ\_44100   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a0ebafbef2cddd4b6c7c7990ca77db0f9)A2DP\_SBC\_SAMP\_FREQ\_48000

| #define A2DP\_SBC\_SAMP\_FREQ\_48000   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#ad5916cf243e40e5a674ceed13477023e)A2DP\_SBC\_SUBBAND\_4

| #define A2DP\_SBC\_SUBBAND\_4   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a6b4bd1ef891c14c4f863c9623dcb63f7)A2DP\_SBC\_SUBBAND\_8

| #define A2DP\_SBC\_SUBBAND\_8   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a58878ea86ed87c6c5bfede0fe217ade8)BT\_A2DP\_SBC\_ALLOC\_MTHD

| #define BT\_A2DP\_SBC\_ALLOC\_MTHD | ( |  | *cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((cap->config[1]) & 0x03)

## [◆ ](#a1721d8cc832b5a74306943074132369a)BT\_A2DP\_SBC\_BLK\_LEN

| #define BT\_A2DP\_SBC\_BLK\_LEN | ( |  | *cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((cap->config[1] >> 4) & 0x0f)

## [◆ ](#a8d058052eb87cf22314395cc2581ac5d)BT\_A2DP\_SBC\_CHAN\_MODE

| #define BT\_A2DP\_SBC\_CHAN\_MODE | ( |  | *cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((cap->config[0]) & 0x0f)

## [◆ ](#aa9a0484c4eefe685c0cbde87ce781734)BT\_A2DP\_SBC\_MEDIA\_HDR\_ENCODE

| #define BT\_A2DP\_SBC\_MEDIA\_HDR\_ENCODE | ( |  | *num\_frames*, |
| --- | --- | --- | --- |
|  |  |  | *l*, |
|  |  |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)*, |
|  |  |  | *f* ) |

**Value:**

[FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0), num\_frames) | [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5), l) |\

FIELD\_PREP([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) | [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7), f)

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)

#define GENMASK(h, l)

Create a contiguous bitmask starting at bit position l and ending at position h.

**Definition** util.h:79

[FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)

#define FIELD\_PREP(mask, value)

Prepare a bitfield element using value with mask representing its field position and width.

**Definition** util\_macro.h:110

## [◆ ](#aaf18a29764a148b007f10e9a9f1a5437)BT\_A2DP\_SBC\_MEDIA\_HDR\_F\_GET

| #define BT\_A2DP\_SBC\_MEDIA\_HDR\_F\_GET | ( |  | *hdr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[FIELD\_GET](group__sys-util.md#gaa49a456f06f7bdbedfcf3517e461947e)([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7), (hdr))

[FIELD\_GET](group__sys-util.md#gaa49a456f06f7bdbedfcf3517e461947e)

#define FIELD\_GET(mask, value)

Extract a bitfield element from value corresponding to the field mask mask.

**Definition** util\_macro.h:103

Set to 1 if the SBC frame is fragmented, otherwise set to 0.

## [◆ ](#ab007b2c51612b05f9edc127bd9090536)BT\_A2DP\_SBC\_MEDIA\_HDR\_F\_SET

| #define BT\_A2DP\_SBC\_MEDIA\_HDR\_F\_SET | ( |  | *hdr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

**Value:**

hdr = ((hdr) & [~BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7)) | [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7), (val))

Set to 1 if the SBC frame is fragmented, otherwise set to 0.

## [◆ ](#ab84850ce399e236f10ef80f0d2d2acde)BT\_A2DP\_SBC\_MEDIA\_HDR\_L\_GET

| #define BT\_A2DP\_SBC\_MEDIA\_HDR\_L\_GET | ( |  | *hdr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[FIELD\_GET](group__sys-util.md#gaa49a456f06f7bdbedfcf3517e461947e)([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5), (hdr))

Set to 1 for the last packet of a fragmented SBC frame, otherwise set to 0.

## [◆ ](#a7f00326a7dcd0839da6ea8557303c45f)BT\_A2DP\_SBC\_MEDIA\_HDR\_L\_SET

| #define BT\_A2DP\_SBC\_MEDIA\_HDR\_L\_SET | ( |  | *hdr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

**Value:**

hdr = ((hdr) & [~BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5)) | [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5), (val))

Set to 1 for the last packet of a fragmented SBC frame, otherwise set to 0.

## [◆ ](#a5d79c5a628c9740a81d5fe9626e14463)BT\_A2DP\_SBC\_MEDIA\_HDR\_NUM\_FRAMES\_GET

| #define BT\_A2DP\_SBC\_MEDIA\_HDR\_NUM\_FRAMES\_GET | ( |  | *hdr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[FIELD\_GET](group__sys-util.md#gaa49a456f06f7bdbedfcf3517e461947e)([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0), (hdr))

If the F bit is set to 0, this field indicates the number of frames contained in this packet.

If the F bit is set to 1, this field indicates the number of remaining fragments, including the current fragment. Therefore, the last counter value shall be one.

## [◆ ](#af8da63e80785a6fa5a53fd29c6da5b9c)BT\_A2DP\_SBC\_MEDIA\_HDR\_NUM\_FRAMES\_SET

| #define BT\_A2DP\_SBC\_MEDIA\_HDR\_NUM\_FRAMES\_SET | ( |  | *hdr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

**Value:**

hdr = ((hdr) & [~GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0)) | [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0), (val))

If the F bit is set to 0, this field indicates the number of frames contained in this packet.

If the F bit is set to 1, this field indicates the number of remaining fragments, including the current fragment. Therefore, the last counter value shall be one.

## [◆ ](#a164ada24748d1fb21248274a02d11301)BT\_A2DP\_SBC\_MEDIA\_HDR\_S\_GET

| #define BT\_A2DP\_SBC\_MEDIA\_HDR\_S\_GET | ( |  | *hdr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[FIELD\_GET](group__sys-util.md#gaa49a456f06f7bdbedfcf3517e461947e)([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6), (hdr))

Set to 1 for the starting packet of a fragmented SBC frame, otherwise set to 0.

## [◆ ](#a85bb7d78a1d654a68812517ddcebf76a)BT\_A2DP\_SBC\_MEDIA\_HDR\_S\_SET

| #define BT\_A2DP\_SBC\_MEDIA\_HDR\_S\_SET | ( |  | *hdr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

**Value:**

hdr = ((hdr) & [~BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6)) | [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6), (val))

Set to 1 for the starting packet of a fragmented SBC frame, otherwise set to 0.

## [◆ ](#a5b9313959439cc91be71efa214383ef7)BT\_A2DP\_SBC\_SAMP\_FREQ

| #define BT\_A2DP\_SBC\_SAMP\_FREQ | ( |  | *cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((cap->config[0] >> 4) & 0x0f)

## [◆ ](#aa4eb6816559e80400f1767e230d0efdf)BT\_A2DP\_SBC\_SUB\_BAND

| #define BT\_A2DP\_SBC\_SUB\_BAND | ( |  | *cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((cap->config[1] >> 2) & 0x03)

## Function Documentation

## [◆ ](#a8791ff3f4f02b46ea879df5e20ba5dd6)bt\_a2dp\_sbc\_get\_channel\_num()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_a2dp\_sbc\_get\_channel\_num | ( | struct [bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md) \* | *sbc\_codec* | ) |  |
| --- | --- | --- | --- | --- | --- |

get channel num of a2dp sbc config.

Parameters
:   | sbc\_codec | The a2dp sbc parameter. |
    | --- | --- |

Returns
:   the channel num.

## [◆ ](#a7af2c05d2605d7d21e656222238922c1)bt\_a2dp\_sbc\_get\_sampling\_frequency()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_a2dp\_sbc\_get\_sampling\_frequency | ( | struct [bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md) \* | *sbc\_codec* | ) |  |
| --- | --- | --- | --- | --- | --- |

get sample rate of a2dp sbc config.

Parameters
:   | sbc\_codec | The a2dp sbc parameter. |
    | --- | --- |

Returns
:   the sample rate.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [a2dp\_codec\_sbc.h](a2dp__codec__sbc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
