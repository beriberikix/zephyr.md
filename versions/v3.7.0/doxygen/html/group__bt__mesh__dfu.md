---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__mesh__dfu.html
original_path: doxygen/html/group__bt__mesh__dfu.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh Device Firmware Update

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Topics | |
| --- | --- |
|  | [Bluetooth Mesh Device Firmware Update (DFU) metadata](group__bt__mesh__dfu__metadata.md) |
|  | Common types and functions for the Bluetooth Mesh DFU metadata. |
|  | [Firmware Update Server model](group__bt__mesh__dfu__srv.md) |
|  | API for the Bluetooth Mesh Firmware Update Server model. |
|  | [Firmware Uppdate Client model](group__bt__mesh__dfu__cli.md) |
|  | API for the Bluetooth Mesh Firmware Update Client model. |

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) |
|  | DFU image instance. [More...](structbt__mesh__dfu__img.md#details) |
| struct | [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) |
|  | DFU image slot for DFU distribution. [More...](structbt__mesh__dfu__slot.md#details) |

| Macros | |
| --- | --- |
| #define | [CONFIG\_BT\_MESH\_DFU\_FWID\_MAXLEN](#gacd0f7b01837809a0a92d27f248a9fdd3)   0 |
| #define | [CONFIG\_BT\_MESH\_DFU\_METADATA\_MAXLEN](#ga8f2afd35a2215f51cd08debe6e1c8ae4)   0 |
| #define | [CONFIG\_BT\_MESH\_DFU\_URI\_MAXLEN](#gaa0812409217dd069b00d386d8ab17f5c)   0 |
| #define | [CONFIG\_BT\_MESH\_DFU\_SLOT\_CNT](#gab517e917ec3279ba50f1ac92ec62b8cf)   0 |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_dfu\_phase](#ga99919dcee1e41bc74bd59e33bec2ded2) {     [BT\_MESH\_DFU\_PHASE\_IDLE](#gga99919dcee1e41bc74bd59e33bec2ded2a9de660580a58dea6ba6e97ea0d371156) , [BT\_MESH\_DFU\_PHASE\_TRANSFER\_ERR](#gga99919dcee1e41bc74bd59e33bec2ded2ab0e56b13787d57d1db20c04f197b0771) , [BT\_MESH\_DFU\_PHASE\_TRANSFER\_ACTIVE](#gga99919dcee1e41bc74bd59e33bec2ded2a36ff3279f4e7683310015b80710e11ad) , [BT\_MESH\_DFU\_PHASE\_VERIFY](#gga99919dcee1e41bc74bd59e33bec2ded2a98de12815a145378849c71d4a4c3bc65) ,     [BT\_MESH\_DFU\_PHASE\_VERIFY\_OK](#gga99919dcee1e41bc74bd59e33bec2ded2abf0e855c2393a272887df9f45e9475e8) , [BT\_MESH\_DFU\_PHASE\_VERIFY\_FAIL](#gga99919dcee1e41bc74bd59e33bec2ded2ade806d4326588400748caef1a0bb587e) , [BT\_MESH\_DFU\_PHASE\_APPLYING](#gga99919dcee1e41bc74bd59e33bec2ded2ad8fdc7da5216a666999a5918f4632c7f) , [BT\_MESH\_DFU\_PHASE\_TRANSFER\_CANCELED](#gga99919dcee1e41bc74bd59e33bec2ded2af9515160965c55602e623498e01bbc51) ,     [BT\_MESH\_DFU\_PHASE\_APPLY\_SUCCESS](#gga99919dcee1e41bc74bd59e33bec2ded2ab51ff97ee07154b6e94f7886bf99ffca) , [BT\_MESH\_DFU\_PHASE\_APPLY\_FAIL](#gga99919dcee1e41bc74bd59e33bec2ded2ab36713294a0e68d8b1615374d2a65266) , [BT\_MESH\_DFU\_PHASE\_UNKNOWN](#gga99919dcee1e41bc74bd59e33bec2ded2a7be52104081ed2b8880aa4175351d4b7)   } |
|  | DFU transfer phase. [More...](#ga99919dcee1e41bc74bd59e33bec2ded2) |
| enum | [bt\_mesh\_dfu\_status](#ga9e627a3c15de782faa11ef6c4ec5e05d) {     [BT\_MESH\_DFU\_SUCCESS](#gga9e627a3c15de782faa11ef6c4ec5e05da9829bf8e37e6eeec483752ebb73325ad) , [BT\_MESH\_DFU\_ERR\_RESOURCES](#gga9e627a3c15de782faa11ef6c4ec5e05da8021a64fb42385544cb8f8ef7b2bca27) , [BT\_MESH\_DFU\_ERR\_WRONG\_PHASE](#gga9e627a3c15de782faa11ef6c4ec5e05da1f23483a915866abeeefddb0ff126047) , [BT\_MESH\_DFU\_ERR\_INTERNAL](#gga9e627a3c15de782faa11ef6c4ec5e05da3e95581f4bd3981b86c037df8e38f806) ,     [BT\_MESH\_DFU\_ERR\_FW\_IDX](#gga9e627a3c15de782faa11ef6c4ec5e05da2eb1e712cc20311cc303eeed7d94701c) , [BT\_MESH\_DFU\_ERR\_METADATA](#gga9e627a3c15de782faa11ef6c4ec5e05da59c78171ab24cffdd2453dff1f377934) , [BT\_MESH\_DFU\_ERR\_TEMPORARILY\_UNAVAILABLE](#gga9e627a3c15de782faa11ef6c4ec5e05da4b5aeee1bfc7e4d855205c7d623ad33a) , [BT\_MESH\_DFU\_ERR\_BLOB\_XFER\_BUSY](#gga9e627a3c15de782faa11ef6c4ec5e05da8e1990cba0513aa0ad0a95625e949e25)   } |
|  | DFU status. [More...](#ga9e627a3c15de782faa11ef6c4ec5e05d) |
| enum | [bt\_mesh\_dfu\_effect](#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) { [BT\_MESH\_DFU\_EFFECT\_NONE](#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8af8fba9033b663ce141c099b48128b22e) , [BT\_MESH\_DFU\_EFFECT\_COMP\_CHANGE\_NO\_RPR](#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a399d11f493d538d6d11a6aee927015dc) , [BT\_MESH\_DFU\_EFFECT\_COMP\_CHANGE](#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a049447eb32bcc0b1b18d5ae908de30b8) , [BT\_MESH\_DFU\_EFFECT\_UNPROV](#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211) } |
|  | Expected effect of a DFU transfer. [More...](#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) |
| enum | [bt\_mesh\_dfu\_iter](#ga82475cb72f2ea8b60e70d6987eca2ff6) { [BT\_MESH\_DFU\_ITER\_STOP](#gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be) , [BT\_MESH\_DFU\_ITER\_CONTINUE](#gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba) } |
|  | Action for DFU iteration callbacks. [More...](#ga82475cb72f2ea8b60e70d6987eca2ff6) |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gacd0f7b01837809a0a92d27f248a9fdd3)CONFIG\_BT\_MESH\_DFU\_FWID\_MAXLEN

| #define CONFIG\_BT\_MESH\_DFU\_FWID\_MAXLEN   0 |
| --- |

`#include <[dfu.h](dfu_8h.md)>`

## [◆ ](#ga8f2afd35a2215f51cd08debe6e1c8ae4)CONFIG\_BT\_MESH\_DFU\_METADATA\_MAXLEN

| #define CONFIG\_BT\_MESH\_DFU\_METADATA\_MAXLEN   0 |
| --- |

`#include <[dfu.h](dfu_8h.md)>`

## [◆ ](#gab517e917ec3279ba50f1ac92ec62b8cf)CONFIG\_BT\_MESH\_DFU\_SLOT\_CNT

| #define CONFIG\_BT\_MESH\_DFU\_SLOT\_CNT   0 |
| --- |

`#include <[dfu.h](dfu_8h.md)>`

## [◆ ](#gaa0812409217dd069b00d386d8ab17f5c)CONFIG\_BT\_MESH\_DFU\_URI\_MAXLEN

| #define CONFIG\_BT\_MESH\_DFU\_URI\_MAXLEN   0 |
| --- |

`#include <[dfu.h](dfu_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)bt\_mesh\_dfu\_effect

| enum [bt\_mesh\_dfu\_effect](#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) |
| --- |

`#include <[dfu.h](dfu_8h.md)>`

Expected effect of a DFU transfer.

| Enumerator | |
| --- | --- |
| BT\_MESH\_DFU\_EFFECT\_NONE | No changes to node Composition Data. |
| BT\_MESH\_DFU\_EFFECT\_COMP\_CHANGE\_NO\_RPR | Node Composition Data changed and the node does not support remote provisioning. |
| BT\_MESH\_DFU\_EFFECT\_COMP\_CHANGE | Node Composition Data changed, and remote provisioning is supported.  The node supports remote provisioning and Composition Data Page 0x80. Page 0x80 contains different Composition Data than Page 0x0. |
| BT\_MESH\_DFU\_EFFECT\_UNPROV | Node will be unprovisioned after the update. |

## [◆ ](#ga82475cb72f2ea8b60e70d6987eca2ff6)bt\_mesh\_dfu\_iter

| enum [bt\_mesh\_dfu\_iter](#ga82475cb72f2ea8b60e70d6987eca2ff6) |
| --- |

`#include <[dfu.h](dfu_8h.md)>`

Action for DFU iteration callbacks.

| Enumerator | |
| --- | --- |
| BT\_MESH\_DFU\_ITER\_STOP | Stop iterating. |
| BT\_MESH\_DFU\_ITER\_CONTINUE | Continue iterating. |

## [◆ ](#ga99919dcee1e41bc74bd59e33bec2ded2)bt\_mesh\_dfu\_phase

| enum [bt\_mesh\_dfu\_phase](#ga99919dcee1e41bc74bd59e33bec2ded2) |
| --- |

`#include <[dfu.h](dfu_8h.md)>`

DFU transfer phase.

| Enumerator | |
| --- | --- |
| BT\_MESH\_DFU\_PHASE\_IDLE | Ready to start a Receive Firmware procedure. |
| BT\_MESH\_DFU\_PHASE\_TRANSFER\_ERR | The Transfer BLOB procedure failed. |
| BT\_MESH\_DFU\_PHASE\_TRANSFER\_ACTIVE | The Receive Firmware procedure is being executed. |
| BT\_MESH\_DFU\_PHASE\_VERIFY | The Verify Firmware procedure is being executed. |
| BT\_MESH\_DFU\_PHASE\_VERIFY\_OK | The Verify Firmware procedure completed successfully. |
| BT\_MESH\_DFU\_PHASE\_VERIFY\_FAIL | The Verify Firmware procedure failed. |
| BT\_MESH\_DFU\_PHASE\_APPLYING | The Apply New Firmware procedure is being executed. |
| BT\_MESH\_DFU\_PHASE\_TRANSFER\_CANCELED | Firmware transfer has been canceled. |
| BT\_MESH\_DFU\_PHASE\_APPLY\_SUCCESS | Firmware applying succeeded. |
| BT\_MESH\_DFU\_PHASE\_APPLY\_FAIL | Firmware applying failed. |
| BT\_MESH\_DFU\_PHASE\_UNKNOWN | Phase of a node was not yet retrieved. |

## [◆ ](#ga9e627a3c15de782faa11ef6c4ec5e05d)bt\_mesh\_dfu\_status

| enum [bt\_mesh\_dfu\_status](#ga9e627a3c15de782faa11ef6c4ec5e05d) |
| --- |

`#include <[dfu.h](dfu_8h.md)>`

DFU status.

| Enumerator | |
| --- | --- |
| BT\_MESH\_DFU\_SUCCESS | The message was processed successfully. |
| BT\_MESH\_DFU\_ERR\_RESOURCES | Insufficient resources on the node. |
| BT\_MESH\_DFU\_ERR\_WRONG\_PHASE | The operation cannot be performed while the Server is in the current phase. |
| BT\_MESH\_DFU\_ERR\_INTERNAL | An internal error occurred on the node. |
| BT\_MESH\_DFU\_ERR\_FW\_IDX | The message contains a firmware index value that is not expected. |
| BT\_MESH\_DFU\_ERR\_METADATA | The metadata check failed. |
| BT\_MESH\_DFU\_ERR\_TEMPORARILY\_UNAVAILABLE | The Server cannot start a firmware update. |
| BT\_MESH\_DFU\_ERR\_BLOB\_XFER\_BUSY | Another BLOB transfer is in progress. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
