---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/a2dp_8h.html
original_path: doxygen/html/a2dp_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

a2dp.h File Reference

Advanced Audio Distribution Profile header.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`  
`#include <[zephyr/bluetooth/l2cap.h](l2cap_8h_source.md)>`  
`#include <[zephyr/bluetooth/classic/avdtp.h](avdtp_8h_source.md)>`

[Go to the source code of this file.](a2dp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) |
|  | codec information elements for the endpoint [More...](structbt__a2dp__codec__ie.md#details) |
| struct | [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) |
|  | The endpoint configuration. [More...](structbt__a2dp__codec__cfg.md#details) |
| struct | [bt\_a2dp\_ep](structbt__a2dp__ep.md) |
|  | Stream End Point. [More...](structbt__a2dp__ep.md#details) |
| struct | [bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md) |
| struct | [bt\_a2dp\_discover\_param](structbt__a2dp__discover__param.md) |
| struct | [bt\_a2dp\_cb](structbt__a2dp__cb.md) |
|  | The connecting callback. [More...](structbt__a2dp__cb.md#details) |
| struct | [bt\_a2dp\_stream](structbt__a2dp__stream.md) |
|  | A2DP Stream. [More...](structbt__a2dp__stream.md#details) |
| struct | [bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md) |
|  | The stream endpoint related operations. [More...](structbt__a2dp__stream__ops.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_A2DP\_STREAM\_BUF\_RESERVE](#a9fce344cfaa8b96ca41a5866f9e3b3d1)   (12u + [BT\_L2CAP\_BUF\_SIZE](group__bt__l2cap.md#gab95b119de4757588074e367a90a7136a)(0)) |
| #define | [BT\_A2DP\_SBC\_IE\_LENGTH](#af83aa927ac312cfc8577056afffeae56)   (4u) |
|  | SBC IE length. |
| #define | [BT\_A2DP\_MPEG\_1\_2\_IE\_LENGTH](#a313fec2276421be6f29c0309e67755eb)   (4u) |
|  | MPEG1,2 IE length. |
| #define | [BT\_A2DP\_MPEG\_2\_4\_IE\_LENGTH](#a73ae4b6e2913b3772b32c520bf84de8c)   (6u) |
|  | MPEG2,4 IE length. |
| #define | [A2DP\_MAX\_IE\_LENGTH](#ab42c7fe29752fb43bb573a752de9c693)   (8U) |
|  | The max IE (Codec Info Element) length. |
| #define | [BT\_A2DP\_EP\_INIT](#afe0cc7b22a941d272de4f8353865d626)(\_role, \_codec, \_capability) |
|  | define the audio endpoint |
| #define | [BT\_A2DP\_SINK\_EP\_INIT](#a892825546a211982b8809dc0f7596ba2)(\_codec, \_capability) |
|  | define the audio sink endpoint |
| #define | [BT\_A2DP\_SOURCE\_EP\_INIT](#a78089fb18ea7a16dff7ba05370bb452c)(\_codec, \_capability) |
|  | define the audio source endpoint |
| #define | [BT\_A2DP\_SBC\_SINK\_EP](#abf08745833eacb9b409627442ac4c8a2)(\_name, \_freq, \_ch\_mode, \_blk\_len, \_subband, \_alloc\_mthd, \_min\_bitpool, \_max\_bitpool) |
|  | define the SBC sink endpoint that can be used as bt\_a2dp\_register\_endpoint's parameter. |
| #define | [BT\_A2DP\_SBC\_SOURCE\_EP](#a9b9d32d04f96f64d7c5f9bf10e03f9a8)(\_name, \_freq, \_ch\_mode, \_blk\_len, \_subband, \_alloc\_mthd, \_min\_bitpool, \_max\_bitpool) |
|  | define the SBC source endpoint that can be used as bt\_a2dp\_register\_endpoint's parameter. |
| #define | [BT\_A2DP\_SBC\_SINK\_EP\_DEFAULT](#a76fb351efe2730311baae1ad6cddbcb1)(\_name) |
|  | define the default SBC sink endpoint that can be used as bt\_a2dp\_register\_endpoint's parameter. |
| #define | [BT\_A2DP\_SBC\_SOURCE\_EP\_DEFAULT](#a6830ae27e85471935ae604b18cf779e2)(\_name) |
|  | define the default SBC source endpoint that can be used as bt\_a2dp\_register\_endpoint's parameter. |
| #define | [BT\_A2DP\_SBC\_EP\_CFG](#ac879cbea5f0bbecfc0ec948d6e46c073)(\_name, \_freq\_cfg, \_ch\_mode\_cfg, \_blk\_len\_cfg, \_subband\_cfg, \_alloc\_mthd\_cfg, \_min\_bitpool\_cfg, \_max\_bitpool\_cfg) |
|  | define the SBC default configuration. |
| #define | [BT\_A2DP\_SBC\_EP\_CFG\_DEFAULT](#abbfd3bc3fa080517ef4395b30fd697f7)(\_name, \_freq\_cfg) |
|  | define the SBC default configuration. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_a2dp\_discover\_ep\_cb](#ae054d7f9fa92e45c7d40ec0e1d8730ed)) (struct bt\_a2dp \*a2dp, struct [bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md) \*info, struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*\*ep) |
|  | Called when a stream endpoint is discovered. |

| Enumerations | |
| --- | --- |
| enum | [bt\_a2dp\_err\_code](#a4162a6db1ead67f52f961d660beabb8c) {     [BT\_A2DP\_INVALID\_CODEC\_TYPE](#a4162a6db1ead67f52f961d660beabb8ca1718e53b8632688eb1aa9253248e7591) = 0xC1 , [BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_TYPE](#a4162a6db1ead67f52f961d660beabb8cabda2c831224e1c994b5c67ea9fe7be7f) = 0xC2 , [BT\_A2DP\_INVALID\_SAMPLING\_FREQUENCY](#a4162a6db1ead67f52f961d660beabb8ca68471cd1037db6687bc1f60cf500681c) = 0xC3 , [BT\_A2DP\_NOT\_SUPPORTED\_SAMPLING\_FREQUENCY](#a4162a6db1ead67f52f961d660beabb8ca499c532b0069432802cbe72bc33e5a76) = 0xC4 ,     [BT\_A2DP\_INVALID\_CHANNEL\_MODE](#a4162a6db1ead67f52f961d660beabb8ca6222f61712e16dbd0b56fda692844396) = 0xC5 , [BT\_A2DP\_NOT\_SUPPORTED\_CHANNEL\_MODE](#a4162a6db1ead67f52f961d660beabb8ca8e62e8df4d9e2a5389ad1620de7af755) = 0xC6 , [BT\_A2DP\_INVALID\_SUBBANDS](#a4162a6db1ead67f52f961d660beabb8ca8e06f678574f38b9538f8c45622cee3f) = 0xC7 , [BT\_A2DP\_NOT\_SUPPORTED\_SUBBANDS](#a4162a6db1ead67f52f961d660beabb8ca2a20d81b47a5b3119988c3702ba1e84d) = 0xC8 ,     [BT\_A2DP\_INVALID\_ALLOCATION\_METHOD](#a4162a6db1ead67f52f961d660beabb8caf13a2a05042cb4ee373017fabd92303a) = 0xC9 , [BT\_A2DP\_NOT\_SUPPORTED\_ALLOCATION\_METHOD](#a4162a6db1ead67f52f961d660beabb8ca81723b89ccf0d40db2a2edacd2cbaca8) = 0xCA , [BT\_A2DP\_INVALID\_MINIMUM\_BITPOOL\_VALUE](#a4162a6db1ead67f52f961d660beabb8cad81217701b215d26e65c220c83ed4a02) = 0xCB , [BT\_A2DP\_NOT\_SUPPORTED\_MINIMUM\_BITPOOL\_VALUE](#a4162a6db1ead67f52f961d660beabb8cacd474a29c941a1b1ad164a63d07763d3) = 0xCC ,     [BT\_A2DP\_INVALID\_MAXIMUM\_BITPOOL\_VALUE](#a4162a6db1ead67f52f961d660beabb8ca71dfaa290af68147e83541e37d59d5cf) = 0xCD , [BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_BITPOOL\_VALUE](#a4162a6db1ead67f52f961d660beabb8ca9fe3d3aea48e5c5122ce058e8918133f) = 0xCE , [BT\_A2DP\_INVALID\_LAYER](#a4162a6db1ead67f52f961d660beabb8caf2bd03a778271c6310fb51d3dccccb41) = 0xCF , [BT\_A2DP\_NOT\_SUPPORTED\_LAYER](#a4162a6db1ead67f52f961d660beabb8ca48b381cca4ddd1ccb26037e84b0bea9e) = 0xD0 ,     [BT\_A2DP\_NOT\_SUPPORTED\_CRC](#a4162a6db1ead67f52f961d660beabb8ca4e204c6ea5acfe20be37da6fca38eaec) = 0xD1 , [BT\_A2DP\_NOT\_SUPPORTED\_MPF](#a4162a6db1ead67f52f961d660beabb8ca95a7b280dbdb757fab3b8b2077120d8f) = 0xD2 , [BT\_A2DP\_NOT\_SUPPORTED\_VBR](#a4162a6db1ead67f52f961d660beabb8ca92d1fb010cc69e27ec988de69c9bbd51) = 0xD3 , [BT\_A2DP\_INVALID\_BIT\_RATE](#a4162a6db1ead67f52f961d660beabb8cadb4d2cc815b2c01e6f7e2666305d4476) = 0xD4 ,     [BT\_A2DP\_NOT\_SUPPORTED\_BIT\_RATE](#a4162a6db1ead67f52f961d660beabb8caf86c457a7e016f440089469c9f442ad1) = 0xD5 , [BT\_A2DP\_INVALID\_OBJECT\_TYPE](#a4162a6db1ead67f52f961d660beabb8ca3896984afb4b5d164503bd53f0d4e429) = 0xD6 , [BT\_A2DP\_NOT\_SUPPORTED\_OBJECT\_TYPE](#a4162a6db1ead67f52f961d660beabb8ca7b5bafd55d8020029e429b142c572615) = 0xD7 , [BT\_A2DP\_INVALID\_CHANNELS](#a4162a6db1ead67f52f961d660beabb8ca182de8e823efe2f6575a900a567b3483) = 0xD8 ,     [BT\_A2DP\_NOT\_SUPPORTED\_CHANNELS](#a4162a6db1ead67f52f961d660beabb8ca3619a0a5c74de24b7dd8bd79b99ca91a) = 0xD9 , [BT\_A2DP\_INVALID\_VERSION](#a4162a6db1ead67f52f961d660beabb8ca47dbe86cbbd2859243995d1d39c46d8d) = 0xDA , [BT\_A2DP\_NOT\_SUPPORTED\_VERSION](#a4162a6db1ead67f52f961d660beabb8ca1d4c42781c74ebda2b084fe609ac284c) = 0xDB , [BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_SUL](#a4162a6db1ead67f52f961d660beabb8cafdf002100cc0d7d1f07cf833ed331f2b) = 0xDC ,     [BT\_A2DP\_INVALID\_BLOCK\_LENGTH](#a4162a6db1ead67f52f961d660beabb8caebf8a58263b517b79947e9cc8a9678c3) = 0xDD , [BT\_A2DP\_INVALID\_CP\_TYPE](#a4162a6db1ead67f52f961d660beabb8caab4c2af80c9588443a297e120f8ee611) = 0xE0 , [BT\_A2DP\_INVALID\_CP\_FORMAT](#a4162a6db1ead67f52f961d660beabb8ca0554b3ef221c98b5cb4580ae049a6e63) = 0xE1 , [BT\_A2DP\_INVALID\_CODEC\_PARAMETER](#a4162a6db1ead67f52f961d660beabb8ca9aa4fc1c6f365b686ab4dc3875b93396) = 0xE2 ,     [BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_PARAMETER](#a4162a6db1ead67f52f961d660beabb8ca3c801158e7ed2623c2d2930ca91b94a9) = 0xE3 , [BT\_A2DP\_INVALID\_DRC](#a4162a6db1ead67f52f961d660beabb8cafd0982a65fc5657b13f35e0761425d96) = 0xE4 , [BT\_A2DP\_NOT\_SUPPORTED\_DRC](#a4162a6db1ead67f52f961d660beabb8ca198bd8a559eca40d9d95f6edf8a703fd) = 0xE5   } |
|  | A2DP error code. [More...](#a4162a6db1ead67f52f961d660beabb8c) |
| enum | [bt\_a2dp\_codec\_type](#afdb0a28b03d1e11f0595dd3f0b3cb4d6) {     [BT\_A2DP\_SBC](#afdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00) = 0x00 , [BT\_A2DP\_MPEG1](#afdb0a28b03d1e11f0595dd3f0b3cb4d6a1f1840d90c1d5ee28b650978bf012497) = 0x01 , [BT\_A2DP\_MPEG2](#afdb0a28b03d1e11f0595dd3f0b3cb4d6aefe729d388e0a3d8bb7759b986123c88) = 0x02 , [BT\_A2DP\_ATRAC](#afdb0a28b03d1e11f0595dd3f0b3cb4d6a8b969e35e28d18cf05802e1381995e83) = 0x04 ,     [BT\_A2DP\_VENDOR](#afdb0a28b03d1e11f0595dd3f0b3cb4d6ad3c292360558ea515a84d570c43c1701) = 0xff   } |
|  | Codec Type. [More...](#afdb0a28b03d1e11f0595dd3f0b3cb4d6) |
| enum | { [BT\_A2DP\_DISCOVER\_EP\_STOP](#a7830b874f18be8fc1c62cb9fc69d3c7eab55d2d864da292240e19ee251de832f2) = 0 , [BT\_A2DP\_DISCOVER\_EP\_CONTINUE](#a7830b874f18be8fc1c62cb9fc69d3c7eae38f6b8bd78c8a975d0f59c74fe9d367) } |
|  | Helper enum to be used as return value of [bt\_a2dp\_discover\_ep\_cb](#ae054d7f9fa92e45c7d40ec0e1d8730ed). [More...](#a7830b874f18be8fc1c62cb9fc69d3c7e) |

| Functions | |
| --- | --- |
| struct bt\_a2dp \* | [bt\_a2dp\_connect](#abc74f6c2a0cf619adbefcf9ffbca1c03) (struct bt\_conn \*conn) |
|  | A2DP Connect. |
| int | [bt\_a2dp\_disconnect](#abbf0d012860a233ecc84ed333e0da051) (struct bt\_a2dp \*a2dp) |
|  | disconnect l2cap a2dp |
| int | [bt\_a2dp\_register\_ep](#adccb916ce9ee1a229f7a9f89ec3adc1b) (struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) media\_type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) role) |
|  | Endpoint Registration. |
| int | [bt\_a2dp\_register\_cb](#a4af29d7c162743c00534868ba945b7ec) (struct [bt\_a2dp\_cb](structbt__a2dp__cb.md) \*cb) |
|  | register callback. |
| int | [bt\_a2dp\_discover](#a931234227bc2b9eaed9cd60471ee54db) (struct bt\_a2dp \*a2dp, struct [bt\_a2dp\_discover\_param](structbt__a2dp__discover__param.md) \*param) |
|  | Discover remote endpoints. |
| void | [bt\_a2dp\_stream\_cb\_register](#ab8459d999437daa7a107b1bdf4c5ea46) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, struct [bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md) \*ops) |
|  | Register Audio callbacks for a stream. |
| int | [bt\_a2dp\_stream\_config](#a3ff3ca4cd016025f95690e89643f0ff5) (struct bt\_a2dp \*a2dp, struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*local\_ep, struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*remote\_ep, struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \*config) |
|  | configure endpoint. |
| int | [bt\_a2dp\_stream\_establish](#af47e0028176494f5353ee00261ffa49a) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
|  | establish a2dp streamer. |
| int | [bt\_a2dp\_stream\_release](#a194e7ec86715cf9007de30f6492e4f58) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
|  | release a2dp streamer. |
| int | [bt\_a2dp\_stream\_start](#a368403c64581b761099631280014d877) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
|  | start a2dp streamer. |
| int | [bt\_a2dp\_stream\_suspend](#af22030f4edd5401b2d5359bcb0590145) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
|  | suspend a2dp streamer. |
| int | [bt\_a2dp\_stream\_reconfig](#a70fc5f43265a4c407a847c4205cd7697) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \*config) |
|  | re-configure a2dp streamer |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [bt\_a2dp\_get\_mtu](#afb67c234c9d5748e54d5e67c7b148353) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
|  | get the stream l2cap mtu |

## Detailed Description

Advanced Audio Distribution Profile header.

## Macro Definition Documentation

## [◆ ](#ab42c7fe29752fb43bb573a752de9c693)A2DP\_MAX\_IE\_LENGTH

| #define A2DP\_MAX\_IE\_LENGTH   (8U) |
| --- |

The max IE (Codec Info Element) length.

## [◆ ](#afe0cc7b22a941d272de4f8353865d626)BT\_A2DP\_EP\_INIT

| #define BT\_A2DP\_EP\_INIT | ( |  | *\_role*, |
| --- | --- | --- | --- |
|  |  |  | *\_codec*, |
|  |  |  | *\_capability* ) |

**Value:**

{\

.codec\_type = \_codec,\

.sep = {.sep\_info = {.media\_type = [BT\_AVDTP\_AUDIO](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58), .tsep = \_role}},\

.codec\_cap = \_capability,\

.stream = NULL,\

}

[BT\_AVDTP\_AUDIO](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58)

@ BT\_AVDTP\_AUDIO

Audio Media Type.

**Definition** avdtp.h:78

define the audio endpoint

Parameters
:   | \_role | BT\_AVDTP\_SOURCE or BT\_AVDTP\_SINK. |
    | --- | --- |
    | \_codec | value of enum bt\_a2dp\_codec\_id. |
    | \_capability | the codec capability. |

## [◆ ](#a313fec2276421be6f29c0309e67755eb)BT\_A2DP\_MPEG\_1\_2\_IE\_LENGTH

| #define BT\_A2DP\_MPEG\_1\_2\_IE\_LENGTH   (4u) |
| --- |

MPEG1,2 IE length.

## [◆ ](#a73ae4b6e2913b3772b32c520bf84de8c)BT\_A2DP\_MPEG\_2\_4\_IE\_LENGTH

| #define BT\_A2DP\_MPEG\_2\_4\_IE\_LENGTH   (6u) |
| --- |

MPEG2,4 IE length.

## [◆ ](#ac879cbea5f0bbecfc0ec948d6e46c073)BT\_A2DP\_SBC\_EP\_CFG

| #define BT\_A2DP\_SBC\_EP\_CFG | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_freq\_cfg*, |
|  |  |  | *\_ch\_mode\_cfg*, |
|  |  |  | *\_blk\_len\_cfg*, |
|  |  |  | *\_subband\_cfg*, |
|  |  |  | *\_alloc\_mthd\_cfg*, |
|  |  |  | *\_min\_bitpool\_cfg*, |
|  |  |  | *\_max\_bitpool\_cfg* ) |

**Value:**

static struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md)##\_name = {\

.len = [BT\_A2DP\_SBC\_IE\_LENGTH](#af83aa927ac312cfc8577056afffeae56), .codec\_ie = {\_freq\_cfg | \_ch\_mode\_cfg,\

\_blk\_len\_cfg | \_subband\_cfg | \_alloc\_mthd\_cfg, \_min\_bitpool\_cfg, \_max\_bitpool\_cfg},};\

struct bt\_a2dp\_codec\_cfg \_name = {.codec\_config = &bt\_a2dp\_codec\_ie##\_name,}

[BT\_A2DP\_SBC\_IE\_LENGTH](#af83aa927ac312cfc8577056afffeae56)

#define BT\_A2DP\_SBC\_IE\_LENGTH

SBC IE length.

**Definition** a2dp.h:27

[bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md)

codec information elements for the endpoint

**Definition** a2dp.h:294

define the SBC default configuration.

Parameters
:   | \_name | unique structure name postfix. |
    | --- | --- |
    | \_freq\_cfg | sbc codec frequency. for example: A2DP\_SBC\_SAMP\_FREQ\_44100 |
    | \_ch\_mode\_cfg | sbc codec channel mode. for example: A2DP\_SBC\_CH\_MODE\_JOINT |
    | \_blk\_len\_cfg | sbc codec block length. for example: A2DP\_SBC\_BLK\_LEN\_16 |
    | \_subband\_cfg | sbc codec subband. for example: A2DP\_SBC\_SUBBAND\_8 |
    | \_alloc\_mthd\_cfg | sbc codec allocate method. for example: A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS |
    | \_min\_bitpool\_cfg | sbc codec min bit pool. for example: 18 |
    | \_max\_bitpool\_cfg | sbc codec max bit pool. for example: 35 |

## [◆ ](#abbfd3bc3fa080517ef4395b30fd697f7)BT\_A2DP\_SBC\_EP\_CFG\_DEFAULT

| #define BT\_A2DP\_SBC\_EP\_CFG\_DEFAULT | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_freq\_cfg* ) |

**Value:**

static struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md)##\_name = {\

.len = [BT\_A2DP\_SBC\_IE\_LENGTH](#af83aa927ac312cfc8577056afffeae56), .codec\_ie = {\_freq\_cfg | [A2DP\_SBC\_CH\_MODE\_JOINT](a2dp__codec__sbc_8h.md#afcf64fa599e4d820dccdf40990f5ba39),\

[A2DP\_SBC\_BLK\_LEN\_16](a2dp__codec__sbc_8h.md#a1cb9425713c325442652fb406557e52a) | [A2DP\_SBC\_SUBBAND\_8](a2dp__codec__sbc_8h.md#a6b4bd1ef891c14c4f863c9623dcb63f7) | [A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS](a2dp__codec__sbc_8h.md#a27d905ddf0fdb3dea4d3c12dd3ca33fe), 18U, 35U},};\

struct bt\_a2dp\_codec\_cfg \_name = {.codec\_config = &bt\_a2dp\_codec\_ie##\_name,}

[A2DP\_SBC\_BLK\_LEN\_16](a2dp__codec__sbc_8h.md#a1cb9425713c325442652fb406557e52a)

#define A2DP\_SBC\_BLK\_LEN\_16

**Definition** a2dp\_codec\_sbc.h:44

[A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS](a2dp__codec__sbc_8h.md#a27d905ddf0fdb3dea4d3c12dd3ca33fe)

#define A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS

**Definition** a2dp\_codec\_sbc.h:52

[A2DP\_SBC\_SUBBAND\_8](a2dp__codec__sbc_8h.md#a6b4bd1ef891c14c4f863c9623dcb63f7)

#define A2DP\_SBC\_SUBBAND\_8

**Definition** a2dp\_codec\_sbc.h:48

[A2DP\_SBC\_CH\_MODE\_JOINT](a2dp__codec__sbc_8h.md#afcf64fa599e4d820dccdf40990f5ba39)

#define A2DP\_SBC\_CH\_MODE\_JOINT

**Definition** a2dp\_codec\_sbc.h:38

define the SBC default configuration.

Parameters
:   | \_name | unique structure name postfix. |
    | --- | --- |
    | \_freq\_cfg | the frequency to configure the remote same codec type endpoint. |

## [◆ ](#af83aa927ac312cfc8577056afffeae56)BT\_A2DP\_SBC\_IE\_LENGTH

| #define BT\_A2DP\_SBC\_IE\_LENGTH   (4u) |
| --- |

SBC IE length.

## [◆ ](#abf08745833eacb9b409627442ac4c8a2)BT\_A2DP\_SBC\_SINK\_EP

| #define BT\_A2DP\_SBC\_SINK\_EP | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_freq*, |
|  |  |  | *\_ch\_mode*, |
|  |  |  | *\_blk\_len*, |
|  |  |  | *\_subband*, |
|  |  |  | *\_alloc\_mthd*, |
|  |  |  | *\_min\_bitpool*, |
|  |  |  | *\_max\_bitpool* ) |

**Value:**

static struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) bt\_a2dp\_ep\_cap\_ie##\_name =\

{.len = [BT\_A2DP\_SBC\_IE\_LENGTH](#af83aa927ac312cfc8577056afffeae56), .codec\_ie = {\_freq | \_ch\_mode,\

\_blk\_len | \_subband | \_alloc\_mthd, \_min\_bitpool, \_max\_bitpool}};\

static struct bt\_a2dp\_ep \_name = [BT\_A2DP\_SINK\_EP\_INIT](#a892825546a211982b8809dc0f7596ba2)([BT\_A2DP\_SBC](#afdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00),\

(&bt\_a2dp\_ep\_cap\_ie##\_name))

[BT\_A2DP\_SINK\_EP\_INIT](#a892825546a211982b8809dc0f7596ba2)

#define BT\_A2DP\_SINK\_EP\_INIT(\_codec, \_capability)

define the audio sink endpoint

**Definition** a2dp.h:52

[BT\_A2DP\_SBC](#afdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00)

@ BT\_A2DP\_SBC

Codec SBC.

**Definition** a2dp.h:276

define the SBC sink endpoint that can be used as bt\_a2dp\_register\_endpoint's parameter.

SBC is mandatory as a2dp specification, BT\_A2DP\_SBC\_SINK\_EP\_DEFAULT is more convenient for user to register SBC endpoint.

Parameters
:   | \_name | unique structure name postfix. |
    | --- | --- |
    | \_freq | sbc codec frequency. for example: A2DP\_SBC\_SAMP\_FREQ\_44100 | A2DP\_SBC\_SAMP\_FREQ\_48000 |
    | \_ch\_mode | sbc codec channel mode. for example: A2DP\_SBC\_CH\_MODE\_MONO | A2DP\_SBC\_CH\_MODE\_STREO |
    | \_blk\_len | sbc codec block length. for example: A2DP\_SBC\_BLK\_LEN\_16 |
    | \_subband | sbc codec subband. for example: A2DP\_SBC\_SUBBAND\_8 |
    | \_alloc\_mthd | sbc codec allocate method. for example: A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS |
    | \_min\_bitpool | sbc codec min bit pool. for example: 18 |
    | \_max\_bitpool | sbc codec max bit pool. for example: 35 @ |

## [◆ ](#a76fb351efe2730311baae1ad6cddbcb1)BT\_A2DP\_SBC\_SINK\_EP\_DEFAULT

| #define BT\_A2DP\_SBC\_SINK\_EP\_DEFAULT | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) bt\_a2dp\_ep\_cap\_ie##\_name =\

{.len = [BT\_A2DP\_SBC\_IE\_LENGTH](#af83aa927ac312cfc8577056afffeae56), .codec\_ie = {[A2DP\_SBC\_SAMP\_FREQ\_44100](a2dp__codec__sbc_8h.md#a57d7b85560b36603651fae6c055c32c6) |\

[A2DP\_SBC\_SAMP\_FREQ\_48000](a2dp__codec__sbc_8h.md#a0ebafbef2cddd4b6c7c7990ca77db0f9) | [A2DP\_SBC\_CH\_MODE\_MONO](a2dp__codec__sbc_8h.md#aa9b58737fa1561b684a20980ea0b6feb) | [A2DP\_SBC\_CH\_MODE\_STREO](a2dp__codec__sbc_8h.md#acc5be684b75804f72a28d025fc5cc9bb) |\

[A2DP\_SBC\_CH\_MODE\_JOINT](a2dp__codec__sbc_8h.md#afcf64fa599e4d820dccdf40990f5ba39), [A2DP\_SBC\_BLK\_LEN\_16](a2dp__codec__sbc_8h.md#a1cb9425713c325442652fb406557e52a) |\

[A2DP\_SBC\_SUBBAND\_8](a2dp__codec__sbc_8h.md#a6b4bd1ef891c14c4f863c9623dcb63f7) | [A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS](a2dp__codec__sbc_8h.md#a27d905ddf0fdb3dea4d3c12dd3ca33fe), 18U, 35U}};\

static struct bt\_a2dp\_ep \_name = [BT\_A2DP\_SINK\_EP\_INIT](#a892825546a211982b8809dc0f7596ba2)([BT\_A2DP\_SBC](#afdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00),\

&bt\_a2dp\_ep\_cap\_ie##\_name)

[A2DP\_SBC\_SAMP\_FREQ\_48000](a2dp__codec__sbc_8h.md#a0ebafbef2cddd4b6c7c7990ca77db0f9)

#define A2DP\_SBC\_SAMP\_FREQ\_48000

**Definition** a2dp\_codec\_sbc.h:32

[A2DP\_SBC\_SAMP\_FREQ\_44100](a2dp__codec__sbc_8h.md#a57d7b85560b36603651fae6c055c32c6)

#define A2DP\_SBC\_SAMP\_FREQ\_44100

**Definition** a2dp\_codec\_sbc.h:31

[A2DP\_SBC\_CH\_MODE\_MONO](a2dp__codec__sbc_8h.md#aa9b58737fa1561b684a20980ea0b6feb)

#define A2DP\_SBC\_CH\_MODE\_MONO

**Definition** a2dp\_codec\_sbc.h:35

[A2DP\_SBC\_CH\_MODE\_STREO](a2dp__codec__sbc_8h.md#acc5be684b75804f72a28d025fc5cc9bb)

#define A2DP\_SBC\_CH\_MODE\_STREO

**Definition** a2dp\_codec\_sbc.h:37

define the default SBC sink endpoint that can be used as bt\_a2dp\_register\_endpoint's parameter.

SBC is mandatory as a2dp specification, BT\_A2DP\_SBC\_SINK\_EP\_DEFAULT is more convenient for user to register SBC endpoint.

Parameters
:   | \_name | the endpoint variable name. |
    | --- | --- |

## [◆ ](#a9b9d32d04f96f64d7c5f9bf10e03f9a8)BT\_A2DP\_SBC\_SOURCE\_EP

| #define BT\_A2DP\_SBC\_SOURCE\_EP | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_freq*, |
|  |  |  | *\_ch\_mode*, |
|  |  |  | *\_blk\_len*, |
|  |  |  | *\_subband*, |
|  |  |  | *\_alloc\_mthd*, |
|  |  |  | *\_min\_bitpool*, |
|  |  |  | *\_max\_bitpool* ) |

**Value:**

static struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) bt\_a2dp\_ep\_cap\_ie##\_name =\

{.len = [BT\_A2DP\_SBC\_IE\_LENGTH](#af83aa927ac312cfc8577056afffeae56), .codec\_ie = {\_freq | \_ch\_mode,\

\_blk\_len | \_subband | \_alloc\_mthd, \_min\_bitpool, \_max\_bitpool}};\

static struct bt\_a2dp\_ep \_name = [BT\_A2DP\_SOURCE\_EP\_INIT](#a78089fb18ea7a16dff7ba05370bb452c)([BT\_A2DP\_SBC](#afdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00),\

&bt\_a2dp\_ep\_cap\_ie##\_name)

[BT\_A2DP\_SOURCE\_EP\_INIT](#a78089fb18ea7a16dff7ba05370bb452c)

#define BT\_A2DP\_SOURCE\_EP\_INIT(\_codec, \_capability)

define the audio source endpoint

**Definition** a2dp.h:59

define the SBC source endpoint that can be used as bt\_a2dp\_register\_endpoint's parameter.

SBC is mandatory as a2dp specification, BT\_A2DP\_SBC\_SOURCE\_EP\_DEFAULT is more convenient for user to register SBC endpoint.

Parameters
:   | \_name | the endpoint variable name. |
    | --- | --- |
    | \_freq | sbc codec frequency. for example: A2DP\_SBC\_SAMP\_FREQ\_44100 | A2DP\_SBC\_SAMP\_FREQ\_48000 |
    | \_ch\_mode | sbc codec channel mode. for example: A2DP\_SBC\_CH\_MODE\_MONO | A2DP\_SBC\_CH\_MODE\_STREO |
    | \_blk\_len | sbc codec block length. for example: A2DP\_SBC\_BLK\_LEN\_16 |
    | \_subband | sbc codec subband. for example: A2DP\_SBC\_SUBBAND\_8 |
    | \_alloc\_mthd | sbc codec allocate method. for example: A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS |
    | \_min\_bitpool | sbc codec min bit pool. for example: 18 |
    | \_max\_bitpool | sbc codec max bit pool. for example: 35 |

## [◆ ](#a6830ae27e85471935ae604b18cf779e2)BT\_A2DP\_SBC\_SOURCE\_EP\_DEFAULT

| #define BT\_A2DP\_SBC\_SOURCE\_EP\_DEFAULT | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) bt\_a2dp\_ep\_cap\_ie##\_name =\

{.len = [BT\_A2DP\_SBC\_IE\_LENGTH](#af83aa927ac312cfc8577056afffeae56), .codec\_ie = {[A2DP\_SBC\_SAMP\_FREQ\_44100](a2dp__codec__sbc_8h.md#a57d7b85560b36603651fae6c055c32c6) | \

[A2DP\_SBC\_SAMP\_FREQ\_48000](a2dp__codec__sbc_8h.md#a0ebafbef2cddd4b6c7c7990ca77db0f9) | [A2DP\_SBC\_CH\_MODE\_MONO](a2dp__codec__sbc_8h.md#aa9b58737fa1561b684a20980ea0b6feb) | [A2DP\_SBC\_CH\_MODE\_STREO](a2dp__codec__sbc_8h.md#acc5be684b75804f72a28d025fc5cc9bb) | \

[A2DP\_SBC\_CH\_MODE\_JOINT](a2dp__codec__sbc_8h.md#afcf64fa599e4d820dccdf40990f5ba39), [A2DP\_SBC\_BLK\_LEN\_16](a2dp__codec__sbc_8h.md#a1cb9425713c325442652fb406557e52a) | [A2DP\_SBC\_SUBBAND\_8](a2dp__codec__sbc_8h.md#a6b4bd1ef891c14c4f863c9623dcb63f7) | [A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS](a2dp__codec__sbc_8h.md#a27d905ddf0fdb3dea4d3c12dd3ca33fe),\

18U, 35U},};\

static struct bt\_a2dp\_ep \_name = [BT\_A2DP\_SOURCE\_EP\_INIT](#a78089fb18ea7a16dff7ba05370bb452c)([BT\_A2DP\_SBC](#afdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00),\

&bt\_a2dp\_ep\_cap\_ie##\_name)

define the default SBC source endpoint that can be used as bt\_a2dp\_register\_endpoint's parameter.

SBC is mandatory as a2dp specification, BT\_A2DP\_SBC\_SOURCE\_EP\_DEFAULT is more convenient for user to register SBC endpoint.

Parameters
:   | \_name | the endpoint variable name. |
    | --- | --- |

## [◆ ](#a892825546a211982b8809dc0f7596ba2)BT\_A2DP\_SINK\_EP\_INIT

| #define BT\_A2DP\_SINK\_EP\_INIT | ( |  | *\_codec*, |
| --- | --- | --- | --- |
|  |  |  | *\_capability* ) |

**Value:**

[BT\_A2DP\_EP\_INIT](#afe0cc7b22a941d272de4f8353865d626)([BT\_AVDTP\_SINK](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757a29ddb8e6ac9f3a5e15dcac7cafa0c8d9), \_codec, \_capability)

[BT\_A2DP\_EP\_INIT](#afe0cc7b22a941d272de4f8353865d626)

#define BT\_A2DP\_EP\_INIT(\_role, \_codec, \_capability)

define the audio endpoint

**Definition** a2dp.h:40

[BT\_AVDTP\_SINK](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757a29ddb8e6ac9f3a5e15dcac7cafa0c8d9)

@ BT\_AVDTP\_SINK

Sink Role.

**Definition** avdtp.h:72

define the audio sink endpoint

Parameters
:   | \_codec | value of enum bt\_a2dp\_codec\_id. |
    | --- | --- |
    | \_capability | the codec capability. |

## [◆ ](#a78089fb18ea7a16dff7ba05370bb452c)BT\_A2DP\_SOURCE\_EP\_INIT

| #define BT\_A2DP\_SOURCE\_EP\_INIT | ( |  | *\_codec*, |
| --- | --- | --- | --- |
|  |  |  | *\_capability* ) |

**Value:**

[BT\_A2DP\_EP\_INIT](#afe0cc7b22a941d272de4f8353865d626)([BT\_AVDTP\_SOURCE](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757a8652b3d997c0daec5b90be2aa046ae0f), \_codec, \_capability)

[BT\_AVDTP\_SOURCE](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757a8652b3d997c0daec5b90be2aa046ae0f)

@ BT\_AVDTP\_SOURCE

Source Role.

**Definition** avdtp.h:70

define the audio source endpoint

Parameters
:   | \_codec | value of enum bt\_a2dp\_codec\_id. |
    | --- | --- |
    | \_capability | the codec capability. |

## [◆ ](#a9fce344cfaa8b96ca41a5866f9e3b3d1)BT\_A2DP\_STREAM\_BUF\_RESERVE

| #define BT\_A2DP\_STREAM\_BUF\_RESERVE   (12u + [BT\_L2CAP\_BUF\_SIZE](group__bt__l2cap.md#gab95b119de4757588074e367a90a7136a)(0)) |
| --- |

## Typedef Documentation

## [◆ ](#ae054d7f9fa92e45c7d40ec0e1d8730ed)bt\_a2dp\_discover\_ep\_cb

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* bt\_a2dp\_discover\_ep\_cb) (struct bt\_a2dp \*a2dp, struct [bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md) \*info, struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*\*ep) |
| --- |

Called when a stream endpoint is discovered.

A function of this type is given by the user to the [bt\_a2dp\_discover\_param](structbt__a2dp__discover__param.md) object. It'll be called on each valid stream endpoint discovery completion. When no more endpoint then NULL is passed to the user. Otherwise user can get valid endpoint information from parameter info, user can set parameter ep to get the endpoint after the callback is return. The returned function value allows the user to control retrieving follow-up endpoints if any. If the user doesn't want to read more endpoints since current found endpoints fulfill its requirements then should return BT\_A2DP\_DISCOVER\_EP\_STOP. Otherwise returned value means more subcall iterations are allowable.

Parameters
:   | a2dp | a2dp connection object identifying a2dp connection to queried remote. |
    | --- | --- |
    | info | Object pointing to the information of the callbacked endpoint. |
    | ep | If the user want to use this found endpoint, user can set value to it to get the endpoint that can be used further in other A2DP APIs. It is NULL if info is NULL (no more endpoint is found). |

Returns
:   BT\_A2DP\_DISCOVER\_EP\_STOP in case of no more need to continue discovery for next endpoint. By returning BT\_A2DP\_DISCOVER\_EP\_STOP user allows this discovery continuation.

## Enumeration Type Documentation

## [◆ ](#a7830b874f18be8fc1c62cb9fc69d3c7e)anonymous enum

| anonymous enum |
| --- |

Helper enum to be used as return value of [bt\_a2dp\_discover\_ep\_cb](#ae054d7f9fa92e45c7d40ec0e1d8730ed).

The value informs the caller to perform further pending actions or stop them.

| Enumerator | |
| --- | --- |
| BT\_A2DP\_DISCOVER\_EP\_STOP |  |
| BT\_A2DP\_DISCOVER\_EP\_CONTINUE |  |

## [◆ ](#afdb0a28b03d1e11f0595dd3f0b3cb4d6)bt\_a2dp\_codec\_type

| enum [bt\_a2dp\_codec\_type](#afdb0a28b03d1e11f0595dd3f0b3cb4d6) |
| --- |

Codec Type.

| Enumerator | |
| --- | --- |
| BT\_A2DP\_SBC | Codec SBC. |
| BT\_A2DP\_MPEG1 | Codec MPEG-1. |
| BT\_A2DP\_MPEG2 | Codec MPEG-2. |
| BT\_A2DP\_ATRAC | Codec ATRAC. |
| BT\_A2DP\_VENDOR | Codec Non-A2DP. |

## [◆ ](#a4162a6db1ead67f52f961d660beabb8c)bt\_a2dp\_err\_code

| enum [bt\_a2dp\_err\_code](#a4162a6db1ead67f52f961d660beabb8c) |
| --- |

A2DP error code.

| Enumerator | |
| --- | --- |
| BT\_A2DP\_INVALID\_CODEC\_TYPE | Media Codec Type is not valid. |
| BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_TYPE | Media Codec Type is not supported. |
| BT\_A2DP\_INVALID\_SAMPLING\_FREQUENCY | Sampling Frequency is not valid or multiple values have been selected. |
| BT\_A2DP\_NOT\_SUPPORTED\_SAMPLING\_FREQUENCY | Sampling Frequency is not supported. |
| BT\_A2DP\_INVALID\_CHANNEL\_MODE | Channel Mode is not valid or multiple values have been selected. |
| BT\_A2DP\_NOT\_SUPPORTED\_CHANNEL\_MODE | Channel Mode is not supported. |
| BT\_A2DP\_INVALID\_SUBBANDS | None or multiple values have been selected for Number of Subbands. |
| BT\_A2DP\_NOT\_SUPPORTED\_SUBBANDS | Number of Subbands is not supported. |
| BT\_A2DP\_INVALID\_ALLOCATION\_METHOD | None or multiple values have been selected for Allocation Method. |
| BT\_A2DP\_NOT\_SUPPORTED\_ALLOCATION\_METHOD | Allocation Method is not supported. |
| BT\_A2DP\_INVALID\_MINIMUM\_BITPOOL\_VALUE | Minimum Bitpool Value is not valid. |
| BT\_A2DP\_NOT\_SUPPORTED\_MINIMUM\_BITPOOL\_VALUE | Minimum Bitpool Value is not supported. |
| BT\_A2DP\_INVALID\_MAXIMUM\_BITPOOL\_VALUE | Maximum Bitpool Value is not valid. |
| BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_BITPOOL\_VALUE | Maximum Bitpool Value is not supported. |
| BT\_A2DP\_INVALID\_LAYER | None or multiple values have been selected for Layer. |
| BT\_A2DP\_NOT\_SUPPORTED\_LAYER | Layer is not supported. |
| BT\_A2DP\_NOT\_SUPPORTED\_CRC | CRC is not supported. |
| BT\_A2DP\_NOT\_SUPPORTED\_MPF | MPF-2 is not supported. |
| BT\_A2DP\_NOT\_SUPPORTED\_VBR | VBR is not supported. |
| BT\_A2DP\_INVALID\_BIT\_RATE | None or multiple values have been selected for Bit Rate. |
| BT\_A2DP\_NOT\_SUPPORTED\_BIT\_RATE | Bit Rate is not supported. |
| BT\_A2DP\_INVALID\_OBJECT\_TYPE | Either 1) Object type is not valid or 2) None or multiple values have been selected for Object Type. |
| BT\_A2DP\_NOT\_SUPPORTED\_OBJECT\_TYPE | Object Type is not supported. |
| BT\_A2DP\_INVALID\_CHANNELS | Either 1) Channels is not valid or 2) None or multiple values have been selected for Channels. |
| BT\_A2DP\_NOT\_SUPPORTED\_CHANNELS | Channels is not supported. |
| BT\_A2DP\_INVALID\_VERSION | Version is not valid. |
| BT\_A2DP\_NOT\_SUPPORTED\_VERSION | Version is not supported. |
| BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_SUL | Maximum SUL is not acceptable for the Decoder in the SNK. |
| BT\_A2DP\_INVALID\_BLOCK\_LENGTH | None or multiple values have been selected for Block Length. |
| BT\_A2DP\_INVALID\_CP\_TYPE | The requested CP Type is not supported. |
| BT\_A2DP\_INVALID\_CP\_FORMAT | The format of Content Protection Service Capability/Content Protection Scheme Dependent Data is not correct. |
| BT\_A2DP\_INVALID\_CODEC\_PARAMETER | The codec parameter is invalid.  Used if a more specific error code does not exist for the codec in use |
| BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_PARAMETER | The codec parameter is not supported.  Used if a more specific error code does not exist for the codec in use |
| BT\_A2DP\_INVALID\_DRC | Combination of Object Type and DRC is invalid. |
| BT\_A2DP\_NOT\_SUPPORTED\_DRC | DRC is not supported. |

## Function Documentation

## [◆ ](#abc74f6c2a0cf619adbefcf9ffbca1c03)bt\_a2dp\_connect()

| struct bt\_a2dp \* bt\_a2dp\_connect | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

A2DP Connect.

This function is to be called after the conn parameter is obtained by performing a GAP procedure. The API is to be used to establish A2DP connection between devices. This function only establish AVDTP L2CAP Signaling connection. After connection success, the callback that is registered by bt\_a2dp\_register\_connect\_callback is called.

Parameters
:   | conn | Pointer to bt\_conn structure. |
    | --- | --- |

Returns
:   pointer to struct bt\_a2dp in case of success or NULL in case of error.

## [◆ ](#abbf0d012860a233ecc84ed333e0da051)bt\_a2dp\_disconnect()

| int bt\_a2dp\_disconnect | ( | struct bt\_a2dp \* | *a2dp* | ) |  |
| --- | --- | --- | --- | --- | --- |

disconnect l2cap a2dp

This function close AVDTP L2CAP Signaling connection. It closes the AVDTP L2CAP Media connection too if it is established.

Parameters
:   | a2dp | The a2dp instance. |
    | --- | --- |

Returns
:   0 in case of success and error code in case of error.

## [◆ ](#a931234227bc2b9eaed9cd60471ee54db)bt\_a2dp\_discover()

| int bt\_a2dp\_discover | ( | struct bt\_a2dp \* | *a2dp*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_a2dp\_discover\_param](structbt__a2dp__discover__param.md) \* | *param* ) |

Discover remote endpoints.

Parameters
:   | a2dp | The a2dp instance. |
    | --- | --- |
    | param | the discover used param. |

Returns
:   0 in case of success and error code in case of error.

## [◆ ](#afb67c234c9d5748e54d5e67c7b148353)bt\_a2dp\_get\_mtu()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_a2dp\_get\_mtu | ( | struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \* | *stream* | ) |  |
| --- | --- | --- | --- | --- | --- |

get the stream l2cap mtu

Parameters
:   | stream | The stream object. |
    | --- | --- |

Returns
:   mtu value

## [◆ ](#a4af29d7c162743c00534868ba945b7ec)bt\_a2dp\_register\_cb()

| int bt\_a2dp\_register\_cb | ( | struct [bt\_a2dp\_cb](structbt__a2dp__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

register callback.

The cb is called when bt\_a2dp\_connect is called or it is operated by remote device.

Parameters
:   | cb | The callback function. |
    | --- | --- |

Returns
:   0 in case of success and error code in case of error.

## [◆ ](#adccb916ce9ee1a229f7a9f89ec3adc1b)bt\_a2dp\_register\_ep()

| int bt\_a2dp\_register\_ep | ( | struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \* | *ep*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *media\_type*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *role* ) |

Endpoint Registration.

Parameters
:   | ep | Pointer to [bt\_a2dp\_ep](structbt__a2dp__ep.md "Stream End Point.") structure. |
    | --- | --- |
    | media\_type | Media type that the Endpoint is. |
    | role | Role of Endpoint. |

Returns
:   0 in case of success and error code in case of error.

## [◆ ](#ab8459d999437daa7a107b1bdf4c5ea46)bt\_a2dp\_stream\_cb\_register()

| void bt\_a2dp\_stream\_cb\_register | ( | struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md) \* | *ops* ) |

Register Audio callbacks for a stream.

Register Audio callbacks for a stream.

Parameters
:   | stream | Stream object. |
    | --- | --- |
    | ops | Stream operations structure. |

## [◆ ](#a3ff3ca4cd016025f95690e89643f0ff5)bt\_a2dp\_stream\_config()

| int bt\_a2dp\_stream\_config | ( | struct bt\_a2dp \* | *a2dp*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \* | *stream*, |
|  |  | struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \* | *local\_ep*, |
|  |  | struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \* | *remote\_ep*, |
|  |  | struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \* | *config* ) |

configure endpoint.

bt\_a2dp\_discover can be used to find remote's endpoints. This function to configure the selected endpoint that is found by bt\_a2dp\_discover. This function sends AVDTP\_SET\_CONFIGURATION.

Parameters
:   | a2dp | The a2dp instance. |
    | --- | --- |
    | stream | Stream object. |
    | local\_ep | The configured endpoint that is registered. |
    | remote\_ep | The remote endpoint. |
    | config | The config to configure the endpoint. |

Returns
:   0 in case of success and error code in case of error.

## [◆ ](#af47e0028176494f5353ee00261ffa49a)bt\_a2dp\_stream\_establish()

| int bt\_a2dp\_stream\_establish | ( | struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \* | *stream* | ) |  |
| --- | --- | --- | --- | --- | --- |

establish a2dp streamer.

This function sends the AVDTP\_OPEN command and create the l2cap channel.

Parameters
:   | stream | The stream object. |
    | --- | --- |

Returns
:   0 in case of success and error code in case of error.

## [◆ ](#a70fc5f43265a4c407a847c4205cd7697)bt\_a2dp\_stream\_reconfig()

| int bt\_a2dp\_stream\_reconfig | ( | struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \* | *config* ) |

re-configure a2dp streamer

This function sends the AVDTP\_RECONFIGURE command.

Parameters
:   | stream | The stream object. |
    | --- | --- |
    | config | The config to configure the stream. |

Returns
:   0 in case of success and error code in case of error.

## [◆ ](#a194e7ec86715cf9007de30f6492e4f58)bt\_a2dp\_stream\_release()

| int bt\_a2dp\_stream\_release | ( | struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \* | *stream* | ) |  |
| --- | --- | --- | --- | --- | --- |

release a2dp streamer.

This function sends the AVDTP\_CLOSE command and release the l2cap channel.

Parameters
:   | stream | The stream object. |
    | --- | --- |

Returns
:   0 in case of success and error code in case of error.

## [◆ ](#a368403c64581b761099631280014d877)bt\_a2dp\_stream\_start()

| int bt\_a2dp\_stream\_start | ( | struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \* | *stream* | ) |  |
| --- | --- | --- | --- | --- | --- |

start a2dp streamer.

This function sends the AVDTP\_START command.

Parameters
:   | stream | The stream object. |
    | --- | --- |

Returns
:   0 in case of success and error code in case of error.

## [◆ ](#af22030f4edd5401b2d5359bcb0590145)bt\_a2dp\_stream\_suspend()

| int bt\_a2dp\_stream\_suspend | ( | struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \* | *stream* | ) |  |
| --- | --- | --- | --- | --- | --- |

suspend a2dp streamer.

This function sends the AVDTP\_SUSPEND command.

Parameters
:   | stream | The stream object. |
    | --- | --- |

Returns
:   0 in case of success and error code in case of error.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [a2dp.h](a2dp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
