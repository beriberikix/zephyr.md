---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/bluetooth_2buf_8h.html
original_path: doxygen/html/bluetooth_2buf_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

buf.h File Reference

Bluetooth data buffer API.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/hci.h](hci_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](bluetooth_2buf_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_buf\_data](structbt__buf__data.md) |
|  | This is a base type for bt\_buf user data. [More...](structbt__buf__data.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_BUF\_RESERVE](group__bt__buf.md#ga41f80f3995e79982f704f832394a6bef)   1 |
| #define | [BT\_BUF\_SIZE](group__bt__buf.md#ga9c114a415dc8fc2b84503736b1283468)(size) |
|  | Helper to include reserved HCI data in buffer calculations. |
| #define | [BT\_BUF\_ACL\_SIZE](group__bt__buf.md#ga8f570211d5e391be63bd46c189eac637)(size) |
|  | Helper to calculate needed buffer size for HCI ACL packets. |
| #define | [BT\_BUF\_EVT\_SIZE](group__bt__buf.md#ga098d042ed58592d7c2428967928ee478)(size) |
|  | Helper to calculate needed buffer size for HCI Event packets. |
| #define | [BT\_BUF\_CMD\_SIZE](group__bt__buf.md#ga9dc9de00be5e8bf673ec60921ea6681b)(size) |
|  | Helper to calculate needed buffer size for HCI Command packets. |
| #define | [BT\_BUF\_ISO\_SIZE](group__bt__buf.md#gaa820dee05a7202304e1aaa9a36386ca4)(size) |
|  | Helper to calculate needed buffer size for HCI ISO packets. |
| #define | [BT\_BUF\_ACL\_RX\_SIZE](group__bt__buf.md#ga3ad106326ce13d6eb61d0ac16f592003)   [BT\_BUF\_ACL\_SIZE](group__bt__buf.md#ga8f570211d5e391be63bd46c189eac637)(CONFIG\_BT\_BUF\_ACL\_RX\_SIZE) |
|  | Data size needed for HCI ACL RX buffers. |
| #define | [BT\_BUF\_EVT\_RX\_SIZE](group__bt__buf.md#gac76caf2a7fce82ba652eab094162ec66)   [BT\_BUF\_EVT\_SIZE](group__bt__buf.md#ga098d042ed58592d7c2428967928ee478)(CONFIG\_BT\_BUF\_EVT\_RX\_SIZE) |
|  | Data size needed for HCI Event RX buffers. |
| #define | [BT\_BUF\_ISO\_RX\_SIZE](group__bt__buf.md#gae5db5f9f282f9675fe620842e0c50337)   0 |
| #define | [BT\_BUF\_ISO\_RX\_COUNT](group__bt__buf.md#gac45f7915fff9516d9d156a42794e8221)   0 |
| #define | [BT\_BUF\_ACL\_RX\_COUNT\_MAX](group__bt__buf.md#ga9a196035ab78158867ce301c698c08e1)   65535 |
| #define | [BT\_BUF\_ACL\_RX\_COUNT\_EXTRA](group__bt__buf.md#ga2a43657d82801ab838928fd544d93f1f)   0 |
| #define | [BT\_BUF\_ACL\_RX\_COUNT](group__bt__buf.md#ga1f2226f2fb0a4ea2b215e1c5572ecbf6)   0 |
| #define | [BT\_BUF\_RX\_SIZE](group__bt__buf.md#ga3e16a5f4c0c9c4c9117d972b7043d82b) |
|  | Data size needed for HCI ACL, HCI ISO or Event RX buffers. |
| #define | [BT\_BUF\_RX\_COUNT](group__bt__buf.md#gaa3ab0861dfd4ebc5f7485f36c1b0fdf1) |
|  | Buffer count needed for HCI ACL or HCI ISO plus Event RX buffers. |
| #define | [BT\_BUF\_CMD\_TX\_SIZE](group__bt__buf.md#ga366c2eee5dcc6056430b203d1c020042)   [BT\_BUF\_CMD\_SIZE](group__bt__buf.md#ga9dc9de00be5e8bf673ec60921ea6681b)(CONFIG\_BT\_BUF\_CMD\_TX\_SIZE) |
|  | Data size needed for HCI Command buffers. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_buf\_rx\_freed\_cb\_t](group__bt__buf.md#gaf5c7be1db66cc51c588938fe0b332040)) (enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) type\_mask) |
|  | A callback to notify about freed buffer in the incoming data pool. |

| Enumerations | |
| --- | --- |
| enum | [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) {     [BT\_BUF\_CMD](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1) = BIT(0) , [BT\_BUF\_EVT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5) = BIT(1) , [BT\_BUF\_ACL\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091) = BIT(2) , [BT\_BUF\_ACL\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13) = BIT(3) ,     [BT\_BUF\_ISO\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e) = BIT(4) , [BT\_BUF\_ISO\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e) = BIT(5) , [BT\_BUF\_H4](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baf9a0d91bbd7c45c285615c6e4d9e5b57) = BIT(6)   } |
|  | Possible types of buffers passed around the Bluetooth stack in a form of bitmask. [More...](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) |

| Functions | |
| --- | --- |
| struct [net\_buf](structnet__buf.md) \* | [bt\_buf\_get\_rx](group__bt__buf.md#ga4013cce9637f5aa2742d1f1aaa00e7ee) (enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) type, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a buffer for incoming data. |
| void | [bt\_buf\_rx\_freed\_cb\_set](group__bt__buf.md#gaf946b1bf3706fe74c6d0c9faaaf478f5) ([bt\_buf\_rx\_freed\_cb\_t](group__bt__buf.md#gaf5c7be1db66cc51c588938fe0b332040) cb) |
|  | Set the callback to notify about freed buffer in the incoming data pool. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_buf\_get\_tx](group__bt__buf.md#ga761a31b7fb19f2325b3a9ac6b1fb1700) (enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) type, [k\_timeout\_t](structk__timeout__t.md) timeout, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate a buffer for outgoing data. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_buf\_get\_evt](group__bt__buf.md#ga7b7a19302881dea458fbd2e9e2309b30) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) discardable, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a buffer for an HCI Event. |
| static void | [bt\_buf\_set\_type](group__bt__buf.md#gaec645aec3d6fb845f214c07f2a864fec) (struct [net\_buf](structnet__buf.md) \*buf, enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) type) |
|  | Set the buffer type. |
| static enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) | [bt\_buf\_get\_type](group__bt__buf.md#ga2e35f0593e54d28bad62d6b8933f1599) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Get the buffer type. |

## Detailed Description

Bluetooth data buffer API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [buf.h](bluetooth_2buf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
