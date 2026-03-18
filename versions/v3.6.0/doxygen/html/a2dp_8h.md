---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/a2dp_8h.html
original_path: doxygen/html/a2dp_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

a2dp.h File Reference

Advanced Audio Distribution Profile header.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/bluetooth/avdtp.h](avdtp_8h_source.md)>`

[Go to the source code of this file.](a2dp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_a2dp\_stream](structbt__a2dp__stream.md) |
|  | Stream Structure. [More...](structbt__a2dp__stream.md#details) |
| struct | [bt\_a2dp\_preset](structbt__a2dp__preset.md) |
|  | Preset for the endpoint. [More...](structbt__a2dp__preset.md#details) |
| struct | [bt\_a2dp\_endpoint](structbt__a2dp__endpoint.md) |
|  | Stream End Point. [More...](structbt__a2dp__endpoint.md#details) |

| Enumerations | |
| --- | --- |
| enum | [bt\_a2dp\_codec\_id](#ade5dadb0a608a460be3c3fcb59413b49) {     [BT\_A2DP\_SBC](#ade5dadb0a608a460be3c3fcb59413b49abd097d204d4136c5205afe7dfe3dfe00) = 0x00 , [BT\_A2DP\_MPEG1](#ade5dadb0a608a460be3c3fcb59413b49a1f1840d90c1d5ee28b650978bf012497) = 0x01 , [BT\_A2DP\_MPEG2](#ade5dadb0a608a460be3c3fcb59413b49aefe729d388e0a3d8bb7759b986123c88) = 0x02 , [BT\_A2DP\_ATRAC](#ade5dadb0a608a460be3c3fcb59413b49a8b969e35e28d18cf05802e1381995e83) = 0x04 ,     [BT\_A2DP\_VENDOR](#ade5dadb0a608a460be3c3fcb59413b49ad3c292360558ea515a84d570c43c1701) = 0xff   } |
|  | Codec ID. [More...](#ade5dadb0a608a460be3c3fcb59413b49) |
| enum | [MEDIA\_TYPE](#a6244624a5a6adb228209853282d6f7da) { [BT\_A2DP\_AUDIO](#a6244624a5a6adb228209853282d6f7daa66c74e3fc9ff01974bd9afad0ad03ac1) = 0x00 , [BT\_A2DP\_VIDEO](#a6244624a5a6adb228209853282d6f7daacd255bc0a24d060761460859b8a47e28) = 0x01 , [BT\_A2DP\_MULTIMEDIA](#a6244624a5a6adb228209853282d6f7daa4fdde75334bd82a9127d1752b561710a) = 0x02 } |
|  | Stream End Point Media Type. [More...](#a6244624a5a6adb228209853282d6f7da) |
| enum | [ROLE\_TYPE](#aa6f56dccc53ab8d3a1cf6c2bde5306ce) { [BT\_A2DP\_SOURCE](#aa6f56dccc53ab8d3a1cf6c2bde5306cea81c8031ba8926d0471226a8d146abcb8) = 0 , [BT\_A2DP\_SINK](#aa6f56dccc53ab8d3a1cf6c2bde5306ceac9ae751ed0468f82fc606daf3a56f240) = 1 } |
|  | Stream End Point Role. [More...](#aa6f56dccc53ab8d3a1cf6c2bde5306ce) |

| Functions | |
| --- | --- |
| struct bt\_a2dp \* | [bt\_a2dp\_connect](#abc74f6c2a0cf619adbefcf9ffbca1c03) (struct bt\_conn \*conn) |
|  | A2DP Connect. |
| int | [bt\_a2dp\_register\_endpoint](#ad2b12e8d4b509d6a3c360b64225b536e) (struct [bt\_a2dp\_endpoint](structbt__a2dp__endpoint.md) \*endpoint, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) media\_type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) role) |
|  | Endpoint Registration. |

## Detailed Description

Advanced Audio Distribution Profile header.

## Enumeration Type Documentation

## [◆ ](#ade5dadb0a608a460be3c3fcb59413b49)bt\_a2dp\_codec\_id

| enum [bt\_a2dp\_codec\_id](#ade5dadb0a608a460be3c3fcb59413b49) |
| --- |

Codec ID.

| Enumerator | |
| --- | --- |
| BT\_A2DP\_SBC | Codec SBC. |
| BT\_A2DP\_MPEG1 | Codec MPEG-1. |
| BT\_A2DP\_MPEG2 | Codec MPEG-2. |
| BT\_A2DP\_ATRAC | Codec ATRAC. |
| BT\_A2DP\_VENDOR | Codec Non-A2DP. |

## [◆ ](#a6244624a5a6adb228209853282d6f7da)MEDIA\_TYPE

| enum [MEDIA\_TYPE](#a6244624a5a6adb228209853282d6f7da) |
| --- |

Stream End Point Media Type.

| Enumerator | |
| --- | --- |
| BT\_A2DP\_AUDIO | Audio Media Type. |
| BT\_A2DP\_VIDEO | Video Media Type. |
| BT\_A2DP\_MULTIMEDIA | Multimedia Media Type. |

## [◆ ](#aa6f56dccc53ab8d3a1cf6c2bde5306ce)ROLE\_TYPE

| enum [ROLE\_TYPE](#aa6f56dccc53ab8d3a1cf6c2bde5306ce) |
| --- |

Stream End Point Role.

| Enumerator | |
| --- | --- |
| BT\_A2DP\_SOURCE | Source Role. |
| BT\_A2DP\_SINK | Sink Role. |

## Function Documentation

## [◆ ](#abc74f6c2a0cf619adbefcf9ffbca1c03)bt\_a2dp\_connect()

| struct bt\_a2dp \* bt\_a2dp\_connect | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

A2DP Connect.

This function is to be called after the conn parameter is obtained by performing a GAP procedure. The API is to be used to establish A2DP connection between devices.

Parameters
:   | conn | Pointer to bt\_conn structure. |
    | --- | --- |

Returns
:   pointer to struct bt\_a2dp in case of success or NULL in case of error.

## [◆ ](#ad2b12e8d4b509d6a3c360b64225b536e)bt\_a2dp\_register\_endpoint()

| int bt\_a2dp\_register\_endpoint | ( | struct [bt\_a2dp\_endpoint](structbt__a2dp__endpoint.md) \* | *endpoint*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *media\_type*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *role* ) |

Endpoint Registration.

This function is used for registering the stream end points. The user has to take care of allocating the memory, the preset pointer and then pass the required arguments. Also, only one sep can be registered at a time.

Parameters
:   | endpoint | Pointer to [bt\_a2dp\_endpoint](structbt__a2dp__endpoint.md "Stream End Point.") structure. |
    | --- | --- |
    | media\_type | Media type that the Endpoint is. |
    | role | Role of Endpoint. |

Returns
:   0 in case of success and error code in case of error.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [a2dp.h](a2dp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
