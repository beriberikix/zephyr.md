---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dfu_8h.html
original_path: doxygen/html/dfu_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dfu.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/blob.h](blob_8h_source.md)>`

[Go to the source code of this file.](dfu_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) |
|  | DFU image instance. [More...](structbt__mesh__dfu__img.md#details) |
| struct | [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) |
|  | DFU image slot for DFU distribution. [More...](structbt__mesh__dfu__slot.md#details) |

| Macros | |
| --- | --- |
| #define | [CONFIG\_BT\_MESH\_DFU\_FWID\_MAXLEN](group__bt__mesh__dfu.md#gacd0f7b01837809a0a92d27f248a9fdd3)   0 |
| #define | [CONFIG\_BT\_MESH\_DFU\_METADATA\_MAXLEN](group__bt__mesh__dfu.md#ga8f2afd35a2215f51cd08debe6e1c8ae4)   0 |
| #define | [CONFIG\_BT\_MESH\_DFU\_URI\_MAXLEN](group__bt__mesh__dfu.md#gaa0812409217dd069b00d386d8ab17f5c)   0 |
| #define | [CONFIG\_BT\_MESH\_DFU\_SLOT\_CNT](group__bt__mesh__dfu.md#gab517e917ec3279ba50f1ac92ec62b8cf)   0 |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_dfu\_phase](group__bt__mesh__dfu.md#ga99919dcee1e41bc74bd59e33bec2ded2) {     [BT\_MESH\_DFU\_PHASE\_IDLE](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a9de660580a58dea6ba6e97ea0d371156) , [BT\_MESH\_DFU\_PHASE\_TRANSFER\_ERR](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ab0e56b13787d57d1db20c04f197b0771) , [BT\_MESH\_DFU\_PHASE\_TRANSFER\_ACTIVE](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a36ff3279f4e7683310015b80710e11ad) , [BT\_MESH\_DFU\_PHASE\_VERIFY](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a98de12815a145378849c71d4a4c3bc65) ,     [BT\_MESH\_DFU\_PHASE\_VERIFY\_OK](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2abf0e855c2393a272887df9f45e9475e8) , [BT\_MESH\_DFU\_PHASE\_VERIFY\_FAIL](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ade806d4326588400748caef1a0bb587e) , [BT\_MESH\_DFU\_PHASE\_APPLYING](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ad8fdc7da5216a666999a5918f4632c7f) , [BT\_MESH\_DFU\_PHASE\_TRANSFER\_CANCELED](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2af9515160965c55602e623498e01bbc51) ,     [BT\_MESH\_DFU\_PHASE\_APPLY\_SUCCESS](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ab51ff97ee07154b6e94f7886bf99ffca) , [BT\_MESH\_DFU\_PHASE\_APPLY\_FAIL](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ab36713294a0e68d8b1615374d2a65266) , [BT\_MESH\_DFU\_PHASE\_UNKNOWN](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a7be52104081ed2b8880aa4175351d4b7)   } |
|  | DFU transfer phase. [More...](group__bt__mesh__dfu.md#ga99919dcee1e41bc74bd59e33bec2ded2) |
| enum | [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d) {     [BT\_MESH\_DFU\_SUCCESS](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da9829bf8e37e6eeec483752ebb73325ad) , [BT\_MESH\_DFU\_ERR\_RESOURCES](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da8021a64fb42385544cb8f8ef7b2bca27) , [BT\_MESH\_DFU\_ERR\_WRONG\_PHASE](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da1f23483a915866abeeefddb0ff126047) , [BT\_MESH\_DFU\_ERR\_INTERNAL](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da3e95581f4bd3981b86c037df8e38f806) ,     [BT\_MESH\_DFU\_ERR\_FW\_IDX](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da2eb1e712cc20311cc303eeed7d94701c) , [BT\_MESH\_DFU\_ERR\_METADATA](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da59c78171ab24cffdd2453dff1f377934) , [BT\_MESH\_DFU\_ERR\_TEMPORARILY\_UNAVAILABLE](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da4b5aeee1bfc7e4d855205c7d623ad33a) , [BT\_MESH\_DFU\_ERR\_BLOB\_XFER\_BUSY](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da8e1990cba0513aa0ad0a95625e949e25)   } |
|  | DFU status. [More...](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d) |
| enum | [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) { [BT\_MESH\_DFU\_EFFECT\_NONE](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8af8fba9033b663ce141c099b48128b22e) , [BT\_MESH\_DFU\_EFFECT\_COMP\_CHANGE\_NO\_RPR](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a399d11f493d538d6d11a6aee927015dc) , [BT\_MESH\_DFU\_EFFECT\_COMP\_CHANGE](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a049447eb32bcc0b1b18d5ae908de30b8) , [BT\_MESH\_DFU\_EFFECT\_UNPROV](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211) } |
|  | Expected effect of a DFU transfer. [More...](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) |
| enum | [bt\_mesh\_dfu\_iter](group__bt__mesh__dfu.md#ga82475cb72f2ea8b60e70d6987eca2ff6) { [BT\_MESH\_DFU\_ITER\_STOP](group__bt__mesh__dfu.md#gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be) , [BT\_MESH\_DFU\_ITER\_CONTINUE](group__bt__mesh__dfu.md#gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba) } |
|  | Action for DFU iteration callbacks. [More...](group__bt__mesh__dfu.md#ga82475cb72f2ea8b60e70d6987eca2ff6) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [dfu.h](dfu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
