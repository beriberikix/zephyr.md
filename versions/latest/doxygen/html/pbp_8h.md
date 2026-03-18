---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pbp_8h.html
original_path: doxygen/html/pbp_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pbp.h File Reference

`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h_source.md)>`

[Go to the source code of this file.](pbp_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BT\_PBP\_MIN\_PBA\_SIZE](group__bt__pbp.md#ga5a334cfc19404a9d9f361b3b2424051a)   ([BT\_UUID\_SIZE\_16](group__bt__uuid.md#ga9d3506fd135b5cd8763446f572c161da) + 1 + 1) |

| Enumerations | |
| --- | --- |
| enum | [bt\_pbp\_announcement\_feature](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47) { [BT\_PBP\_ANNOUNCEMENT\_FEATURE\_ENCRYPTION](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df) = BIT(0) , [BT\_PBP\_ANNOUNCEMENT\_FEATURE\_STANDARD\_QUALITY](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638) = BIT(1) , [BT\_PBP\_ANNOUNCEMENT\_FEATURE\_HIGH\_QUALITY](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e) = BIT(2) } |
|  | Public Broadcast Announcement features. [More...](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47) |

| Functions | |
| --- | --- |
| int | [bt\_pbp\_get\_announcement](group__bt__pbp.md#gaa496ac2a3ec9dd5fc013a1f4a804b11b) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len, enum [bt\_pbp\_announcement\_feature](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47) features, struct [net\_buf\_simple](structnet__buf__simple.md) \*pba\_data\_buf) |
|  | Creates a Public Broadcast Announcement based on the information received in the features parameter. |
| int | [bt\_pbp\_parse\_announcement](group__bt__pbp.md#ga311b1fdb0a2aa24a09e8d3b3566693ff) (struct [bt\_data](structbt__data.md) \*data, enum [bt\_pbp\_announcement\_feature](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47) \*features, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*meta) |
|  | Parses the received advertising data corresponding to a Public Broadcast Announcement. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [pbp.h](pbp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
