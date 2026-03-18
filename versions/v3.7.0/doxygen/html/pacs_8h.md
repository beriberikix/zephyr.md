---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/pacs_8h.html
original_path: doxygen/html/pacs_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pacs.h File Reference

Bluetooth Published Audio Capabilities Service (PACS) APIs.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](pacs_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_pacs\_cap](structbt__pacs__cap.md) |
|  | Published Audio Capability structure. [More...](structbt__pacs__cap.md#details) |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_pacs\_cap\_foreach\_func\_t](group__bt__gatt__csip.md#ga452591f80b6be5d79609b25ade2154a9)) (const struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap, void \*user\_data) |
|  | Published Audio Capability iterator callback. |

| Functions | |
| --- | --- |
| void | [bt\_pacs\_cap\_foreach](group__bt__gatt__csip.md#ga31e2c7e9a4b5b6a291b96832c1218a49) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, [bt\_pacs\_cap\_foreach\_func\_t](group__bt__gatt__csip.md#ga452591f80b6be5d79609b25ade2154a9) func, void \*user\_data) |
|  | Published Audio Capability iterator. |
| int | [bt\_pacs\_cap\_register](group__bt__gatt__csip.md#ga251b36d4f5775eea1f69873709f847cc) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap) |
|  | Register Published Audio Capability. |
| int | [bt\_pacs\_cap\_unregister](group__bt__gatt__csip.md#ga4f6015eba63ffc7a9377afe54a290da1) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap) |
|  | Unregister Published Audio Capability. |
| int | [bt\_pacs\_set\_location](group__bt__gatt__csip.md#gaff290fd59bb05012abcf405dbdc72884) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) location) |
|  | Set the location for an endpoint type. |
| int | [bt\_pacs\_set\_available\_contexts](group__bt__gatt__csip.md#ga29a1ec26c1e5e82e02eac39e1088332c) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) contexts) |
|  | Set the available contexts for an endpoint type. |
| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | [bt\_pacs\_get\_available\_contexts](group__bt__gatt__csip.md#ga437d824d0a944b6c30db492dbe28514f) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir) |
|  | Get the available contexts for an endpoint type. |
| int | [bt\_pacs\_conn\_set\_available\_contexts\_for\_conn](group__bt__gatt__csip.md#ga12f283d2daf72302a01cefb4a4a8fc70) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) \*contexts) |
|  | Set the available contexts for a given connection. |
| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | [bt\_pacs\_get\_available\_contexts\_for\_conn](group__bt__gatt__csip.md#ga7b28aa42525344445b20bb90a19441aa) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir) |
|  | Get the available contexts for a given connection. |
| int | [bt\_pacs\_set\_supported\_contexts](group__bt__gatt__csip.md#gabae9cf025f32ce80b660ebd7f95241b2) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) contexts) |
|  | Set the supported contexts for an endpoint type. |

## Detailed Description

Bluetooth Published Audio Capabilities Service (PACS) APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [pacs.h](pacs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
