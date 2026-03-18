---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/a2dp-codec_8h.html
original_path: doxygen/html/a2dp-codec_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

a2dp-codec.h File Reference

Advance Audio Distribution Profile - SBC Codec header.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](a2dp-codec_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md) |
|  | SBC Codec. [More...](structbt__a2dp__codec__sbc__params.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_A2DP\_SBC\_SAMP\_FREQ](#a092b0f76c2af2d41c28b457b87ea8756)(preset) |
|  | Gets the sampling rate from a codec preset. |
| #define | [BT\_A2DP\_SBC\_CHAN\_MODE](#abc9b0f85b8f338d24a62943857858bd4)(preset) |
|  | Gets the channel mode from a codec preset. |
| #define | [BT\_A2DP\_SBC\_BLK\_LEN](#a33d36b781d3ff7eac73be1a29a0c260a)(preset) |
|  | Gets the block length from a codec preset. |
| #define | [BT\_A2DP\_SBC\_SUB\_BAND](#aeacdc6a1857382ff1f4363d7eddce88e)(preset) |
|  | Gets the number subbands from a codec preset. |
| #define | [BT\_A2DP\_SBC\_ALLOC\_MTHD](#a6bed8046031b53111bf0a45057d04565)(preset) |
|  | Gets the bitpool allocation method from a codec preset. |
| Sampling Frequency | |
| #define | [A2DP\_SBC\_SAMP\_FREQ\_16000](#a054dbbaf58ccc3b64142008e3da31ca5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | 16 kHz |
| #define | [A2DP\_SBC\_SAMP\_FREQ\_32000](#a8e4b5399fb5366770a42fd4dfeece220)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | 32 kHz |
| #define | [A2DP\_SBC\_SAMP\_FREQ\_44100](#a57d7b85560b36603651fae6c055c32c6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | 44.1 kHz |
| #define | [A2DP\_SBC\_SAMP\_FREQ\_48000](#a0ebafbef2cddd4b6c7c7990ca77db0f9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | 48 kHz |
| Channel Mode | |
| #define | [A2DP\_SBC\_CH\_MODE\_MONO](#aa9b58737fa1561b684a20980ea0b6feb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Mono. |
| #define | [A2DP\_SBC\_CH\_MODE\_DUAL](#aab5ab0b151f0a150c392be2f4cc82def)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Dual Channel. |
| #define | [A2DP\_SBC\_CH\_MODE\_STREO](#acc5be684b75804f72a28d025fc5cc9bb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Stereo. |
| #define | [A2DP\_SBC\_CH\_MODE\_JOINT](#afcf64fa599e4d820dccdf40990f5ba39)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Joint Stereo. |
| Block Length | |
| #define | [A2DP\_SBC\_BLK\_LEN\_4](#a3abfc1c5202d2659055fc3480c2d3cc2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | 4 blocks |
| #define | [A2DP\_SBC\_BLK\_LEN\_8](#aeb90df4a33ce9ebdfc38d873fd54abab)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | 8 blocks |
| #define | [A2DP\_SBC\_BLK\_LEN\_12](#a9890a0cb8a813e010855c10fc4d22bf8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | 12 blocks |
| #define | [A2DP\_SBC\_BLK\_LEN\_16](#a1cb9425713c325442652fb406557e52a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | 16 blocks |
| Subbands | |
| #define | [A2DP\_SBC\_SUBBAND\_4](#ad5916cf243e40e5a674ceed13477023e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | 4 subbands |
| #define | [A2DP\_SBC\_SUBBAND\_8](#a6b4bd1ef891c14c4f863c9623dcb63f7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | 8 subbands |
| Bit pool Allocation Method | |
| #define | [A2DP\_SBC\_ALLOC\_MTHD\_SNR](#a7e54f1c971e1fd63e52f0322e7f85105)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Allocate based on loudness of the subband signal. |
| #define | [A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS](#a27d905ddf0fdb3dea4d3c12dd3ca33fe)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Allocate based on the signal-to-noise ratio. |

## Detailed Description

Advance Audio Distribution Profile - SBC Codec header.

## Macro Definition Documentation

## [◆ ](#a27d905ddf0fdb3dea4d3c12dd3ca33fe)A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS

| #define A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Allocate based on the signal-to-noise ratio.

## [◆ ](#a7e54f1c971e1fd63e52f0322e7f85105)A2DP\_SBC\_ALLOC\_MTHD\_SNR

| #define A2DP\_SBC\_ALLOC\_MTHD\_SNR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Allocate based on loudness of the subband signal.

## [◆ ](#a9890a0cb8a813e010855c10fc4d22bf8)A2DP\_SBC\_BLK\_LEN\_12

| #define A2DP\_SBC\_BLK\_LEN\_12   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

12 blocks

## [◆ ](#a1cb9425713c325442652fb406557e52a)A2DP\_SBC\_BLK\_LEN\_16

| #define A2DP\_SBC\_BLK\_LEN\_16   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

16 blocks

## [◆ ](#a3abfc1c5202d2659055fc3480c2d3cc2)A2DP\_SBC\_BLK\_LEN\_4

| #define A2DP\_SBC\_BLK\_LEN\_4   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

4 blocks

## [◆ ](#aeb90df4a33ce9ebdfc38d873fd54abab)A2DP\_SBC\_BLK\_LEN\_8

| #define A2DP\_SBC\_BLK\_LEN\_8   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

8 blocks

## [◆ ](#aab5ab0b151f0a150c392be2f4cc82def)A2DP\_SBC\_CH\_MODE\_DUAL

| #define A2DP\_SBC\_CH\_MODE\_DUAL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Dual Channel.

## [◆ ](#afcf64fa599e4d820dccdf40990f5ba39)A2DP\_SBC\_CH\_MODE\_JOINT

| #define A2DP\_SBC\_CH\_MODE\_JOINT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Joint Stereo.

## [◆ ](#aa9b58737fa1561b684a20980ea0b6feb)A2DP\_SBC\_CH\_MODE\_MONO

| #define A2DP\_SBC\_CH\_MODE\_MONO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Mono.

## [◆ ](#acc5be684b75804f72a28d025fc5cc9bb)A2DP\_SBC\_CH\_MODE\_STREO

| #define A2DP\_SBC\_CH\_MODE\_STREO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Stereo.

## [◆ ](#a054dbbaf58ccc3b64142008e3da31ca5)A2DP\_SBC\_SAMP\_FREQ\_16000

| #define A2DP\_SBC\_SAMP\_FREQ\_16000   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

16 kHz

## [◆ ](#a8e4b5399fb5366770a42fd4dfeece220)A2DP\_SBC\_SAMP\_FREQ\_32000

| #define A2DP\_SBC\_SAMP\_FREQ\_32000   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

32 kHz

## [◆ ](#a57d7b85560b36603651fae6c055c32c6)A2DP\_SBC\_SAMP\_FREQ\_44100

| #define A2DP\_SBC\_SAMP\_FREQ\_44100   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

44.1 kHz

## [◆ ](#a0ebafbef2cddd4b6c7c7990ca77db0f9)A2DP\_SBC\_SAMP\_FREQ\_48000

| #define A2DP\_SBC\_SAMP\_FREQ\_48000   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

48 kHz

## [◆ ](#ad5916cf243e40e5a674ceed13477023e)A2DP\_SBC\_SUBBAND\_4

| #define A2DP\_SBC\_SUBBAND\_4   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

4 subbands

## [◆ ](#a6b4bd1ef891c14c4f863c9623dcb63f7)A2DP\_SBC\_SUBBAND\_8

| #define A2DP\_SBC\_SUBBAND\_8   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

8 subbands

## [◆ ](#a6bed8046031b53111bf0a45057d04565)BT\_A2DP\_SBC\_ALLOC\_MTHD

| #define BT\_A2DP\_SBC\_ALLOC\_MTHD | ( |  | *preset* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((preset->config[1]) & 0x03)

Gets the bitpool allocation method from a codec preset.

Parameters
:   | preset | Codec preset |
    | --- | --- |

## [◆ ](#a33d36b781d3ff7eac73be1a29a0c260a)BT\_A2DP\_SBC\_BLK\_LEN

| #define BT\_A2DP\_SBC\_BLK\_LEN | ( |  | *preset* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((preset->config[1] >> 4) & 0x0f)

Gets the block length from a codec preset.

Parameters
:   | preset | Codec preset |
    | --- | --- |

## [◆ ](#abc9b0f85b8f338d24a62943857858bd4)BT\_A2DP\_SBC\_CHAN\_MODE

| #define BT\_A2DP\_SBC\_CHAN\_MODE | ( |  | *preset* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((preset->config[0]) & 0x0f)

Gets the channel mode from a codec preset.

Parameters
:   | preset | Codec preset |
    | --- | --- |

## [◆ ](#a092b0f76c2af2d41c28b457b87ea8756)BT\_A2DP\_SBC\_SAMP\_FREQ

| #define BT\_A2DP\_SBC\_SAMP\_FREQ | ( |  | *preset* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((preset->config[0] >> 4) & 0x0f)

Gets the sampling rate from a codec preset.

Parameters
:   | preset | Codec preset |
    | --- | --- |

## [◆ ](#aeacdc6a1857382ff1f4363d7eddce88e)BT\_A2DP\_SBC\_SUB\_BAND

| #define BT\_A2DP\_SBC\_SUB\_BAND | ( |  | *preset* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((preset->config[1] >> 2) & 0x03)

Gets the number subbands from a codec preset.

Parameters
:   | preset | Codec preset |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [a2dp-codec.h](a2dp-codec_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
