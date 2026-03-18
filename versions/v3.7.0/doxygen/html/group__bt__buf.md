---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__buf.html
original_path: doxygen/html/group__bt__buf.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Data buffers

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Data buffers.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_buf\_data](structbt__buf__data.md) |
|  | This is a base type for bt\_buf user data. [More...](structbt__buf__data.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_BUF\_RESERVE](#ga41f80f3995e79982f704f832394a6bef)   1 |
| #define | [BT\_BUF\_SIZE](#ga9c114a415dc8fc2b84503736b1283468)(size) |
|  | Helper to include reserved HCI data in buffer calculations. |
| #define | [BT\_BUF\_ACL\_SIZE](#ga8f570211d5e391be63bd46c189eac637)(size) |
|  | Helper to calculate needed buffer size for HCI ACL packets. |
| #define | [BT\_BUF\_EVT\_SIZE](#ga098d042ed58592d7c2428967928ee478)(size) |
|  | Helper to calculate needed buffer size for HCI Event packets. |
| #define | [BT\_BUF\_CMD\_SIZE](#ga9dc9de00be5e8bf673ec60921ea6681b)(size) |
|  | Helper to calculate needed buffer size for HCI Command packets. |
| #define | [BT\_BUF\_ISO\_SIZE](#gaa820dee05a7202304e1aaa9a36386ca4)(size) |
|  | Helper to calculate needed buffer size for HCI ISO packets. |
| #define | [BT\_BUF\_ACL\_RX\_SIZE](#ga3ad106326ce13d6eb61d0ac16f592003)   [BT\_BUF\_ACL\_SIZE](#ga8f570211d5e391be63bd46c189eac637)(CONFIG\_BT\_BUF\_ACL\_RX\_SIZE) |
|  | Data size needed for HCI ACL RX buffers. |
| #define | [BT\_BUF\_EVT\_RX\_SIZE](#gac76caf2a7fce82ba652eab094162ec66)   [BT\_BUF\_EVT\_SIZE](#ga098d042ed58592d7c2428967928ee478)(CONFIG\_BT\_BUF\_EVT\_RX\_SIZE) |
|  | Data size needed for HCI Event RX buffers. |
| #define | [BT\_BUF\_ISO\_RX\_SIZE](#gae5db5f9f282f9675fe620842e0c50337)   0 |
| #define | [BT\_BUF\_ISO\_RX\_COUNT](#gac45f7915fff9516d9d156a42794e8221)   0 |
| #define | [BT\_BUF\_RX\_SIZE](#ga3e16a5f4c0c9c4c9117d972b7043d82b) |
|  | Data size needed for HCI ACL, HCI ISO or Event RX buffers. |
| #define | [BT\_BUF\_RX\_COUNT](#gaa3ab0861dfd4ebc5f7485f36c1b0fdf1) |
|  | Buffer count needed for HCI ACL, HCI ISO or Event RX buffers. |
| #define | [BT\_BUF\_CMD\_TX\_SIZE](#ga366c2eee5dcc6056430b203d1c020042)   [BT\_BUF\_CMD\_SIZE](#ga9dc9de00be5e8bf673ec60921ea6681b)(CONFIG\_BT\_BUF\_CMD\_TX\_SIZE) |
|  | Data size needed for HCI Command buffers. |

| Enumerations | |
| --- | --- |
| enum | [bt\_buf\_type](#gafe1539a89ba3389d52d010a071620d7b) {     [BT\_BUF\_CMD](#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1) , [BT\_BUF\_EVT](#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5) , [BT\_BUF\_ACL\_OUT](#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091) , [BT\_BUF\_ACL\_IN](#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13) ,     [BT\_BUF\_ISO\_OUT](#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e) , [BT\_BUF\_ISO\_IN](#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e) , [BT\_BUF\_H4](#ggafe1539a89ba3389d52d010a071620d7baf9a0d91bbd7c45c285615c6e4d9e5b57)   } |
|  | Possible types of buffers passed around the Bluetooth stack. [More...](#gafe1539a89ba3389d52d010a071620d7b) |

| Functions | |
| --- | --- |
| struct [net\_buf](structnet__buf.md) \* | [bt\_buf\_get\_rx](#ga4013cce9637f5aa2742d1f1aaa00e7ee) (enum [bt\_buf\_type](#gafe1539a89ba3389d52d010a071620d7b) type, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a buffer for incoming data. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_buf\_get\_tx](#ga761a31b7fb19f2325b3a9ac6b1fb1700) (enum [bt\_buf\_type](#gafe1539a89ba3389d52d010a071620d7b) type, [k\_timeout\_t](structk__timeout__t.md) timeout, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate a buffer for outgoing data. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_buf\_get\_evt](#ga7b7a19302881dea458fbd2e9e2309b30) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) discardable, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a buffer for an HCI Event. |
| static void | [bt\_buf\_set\_type](#gaec645aec3d6fb845f214c07f2a864fec) (struct [net\_buf](structnet__buf.md) \*buf, enum [bt\_buf\_type](#gafe1539a89ba3389d52d010a071620d7b) type) |
|  | Set the buffer type. |
| static enum [bt\_buf\_type](#gafe1539a89ba3389d52d010a071620d7b) | [bt\_buf\_get\_type](#ga2e35f0593e54d28bad62d6b8933f1599) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Get the buffer type. |

## Detailed Description

Data buffers.

## Macro Definition Documentation

## [◆ ](#ga3ad106326ce13d6eb61d0ac16f592003)BT\_BUF\_ACL\_RX\_SIZE

| #define BT\_BUF\_ACL\_RX\_SIZE   [BT\_BUF\_ACL\_SIZE](#ga8f570211d5e391be63bd46c189eac637)(CONFIG\_BT\_BUF\_ACL\_RX\_SIZE) |
| --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

Data size needed for HCI ACL RX buffers.

## [◆ ](#ga8f570211d5e391be63bd46c189eac637)BT\_BUF\_ACL\_SIZE

| #define BT\_BUF\_ACL\_SIZE | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

**Value:**

[BT\_BUF\_SIZE](#ga9c114a415dc8fc2b84503736b1283468)([BT\_HCI\_ACL\_HDR\_SIZE](hci__types_8h.md#a7418d845532d6b077a9695454fa65bc5) + (size))

[BT\_BUF\_SIZE](#ga9c114a415dc8fc2b84503736b1283468)

#define BT\_BUF\_SIZE(size)

Helper to include reserved HCI data in buffer calculations.

**Definition** buf.h:58

[BT\_HCI\_ACL\_HDR\_SIZE](hci__types_8h.md#a7418d845532d6b077a9695454fa65bc5)

#define BT\_HCI\_ACL\_HDR\_SIZE

**Definition** hci\_types.h:86

Helper to calculate needed buffer size for HCI ACL packets.

## [◆ ](#ga9dc9de00be5e8bf673ec60921ea6681b)BT\_BUF\_CMD\_SIZE

| #define BT\_BUF\_CMD\_SIZE | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

**Value:**

[BT\_BUF\_SIZE](#ga9c114a415dc8fc2b84503736b1283468)([BT\_HCI\_CMD\_HDR\_SIZE](hci__types_8h.md#acdf2b6de1459a7492415a8987ad9a896) + (size))

[BT\_HCI\_CMD\_HDR\_SIZE](hci__types_8h.md#acdf2b6de1459a7492415a8987ad9a896)

#define BT\_HCI\_CMD\_HDR\_SIZE

**Definition** hci\_types.h:135

Helper to calculate needed buffer size for HCI Command packets.

## [◆ ](#ga366c2eee5dcc6056430b203d1c020042)BT\_BUF\_CMD\_TX\_SIZE

| #define BT\_BUF\_CMD\_TX\_SIZE   [BT\_BUF\_CMD\_SIZE](#ga9dc9de00be5e8bf673ec60921ea6681b)(CONFIG\_BT\_BUF\_CMD\_TX\_SIZE) |
| --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

Data size needed for HCI Command buffers.

## [◆ ](#gac76caf2a7fce82ba652eab094162ec66)BT\_BUF\_EVT\_RX\_SIZE

| #define BT\_BUF\_EVT\_RX\_SIZE   [BT\_BUF\_EVT\_SIZE](#ga098d042ed58592d7c2428967928ee478)(CONFIG\_BT\_BUF\_EVT\_RX\_SIZE) |
| --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

Data size needed for HCI Event RX buffers.

## [◆ ](#ga098d042ed58592d7c2428967928ee478)BT\_BUF\_EVT\_SIZE

| #define BT\_BUF\_EVT\_SIZE | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

**Value:**

[BT\_BUF\_SIZE](#ga9c114a415dc8fc2b84503736b1283468)([BT\_HCI\_EVT\_HDR\_SIZE](hci__types_8h.md#a0edb7e700cfa557e7fb8ec44f5eea961) + (size))

[BT\_HCI\_EVT\_HDR\_SIZE](hci__types_8h.md#a0edb7e700cfa557e7fb8ec44f5eea961)

#define BT\_HCI\_EVT\_HDR\_SIZE

**Definition** hci\_types.h:63

Helper to calculate needed buffer size for HCI Event packets.

## [◆ ](#gac45f7915fff9516d9d156a42794e8221)BT\_BUF\_ISO\_RX\_COUNT

| #define BT\_BUF\_ISO\_RX\_COUNT   0 |
| --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

## [◆ ](#gae5db5f9f282f9675fe620842e0c50337)BT\_BUF\_ISO\_RX\_SIZE

| #define BT\_BUF\_ISO\_RX\_SIZE   0 |
| --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

## [◆ ](#gaa820dee05a7202304e1aaa9a36386ca4)BT\_BUF\_ISO\_SIZE

| #define BT\_BUF\_ISO\_SIZE | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

**Value:**

[BT\_BUF\_SIZE](#ga9c114a415dc8fc2b84503736b1283468)([BT\_HCI\_ISO\_HDR\_SIZE](hci__types_8h.md#a75c1f5e8a44b034004ecfebdb75ee4be) + \

[BT\_HCI\_ISO\_SDU\_TS\_HDR\_SIZE](hci__types_8h.md#a22db454317bc89afe092ab9127888441) + \

(size))

[BT\_HCI\_ISO\_SDU\_TS\_HDR\_SIZE](hci__types_8h.md#a22db454317bc89afe092ab9127888441)

#define BT\_HCI\_ISO\_SDU\_TS\_HDR\_SIZE

**Definition** hci\_types.h:121

[BT\_HCI\_ISO\_HDR\_SIZE](hci__types_8h.md#a75c1f5e8a44b034004ecfebdb75ee4be)

#define BT\_HCI\_ISO\_HDR\_SIZE

**Definition** hci\_types.h:128

Helper to calculate needed buffer size for HCI ISO packets.

## [◆ ](#ga41f80f3995e79982f704f832394a6bef)BT\_BUF\_RESERVE

| #define BT\_BUF\_RESERVE   1 |
| --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

## [◆ ](#gaa3ab0861dfd4ebc5f7485f36c1b0fdf1)BT\_BUF\_RX\_COUNT

| #define BT\_BUF\_RX\_COUNT |
| --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

**Value:**

([MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)([MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(CONFIG\_BT\_BUF\_EVT\_RX\_COUNT, \

CONFIG\_BT\_BUF\_ACL\_RX\_COUNT), \

[BT\_BUF\_ISO\_RX\_COUNT](#gac45f7915fff9516d9d156a42794e8221)))

[BT\_BUF\_ISO\_RX\_COUNT](#gac45f7915fff9516d9d156a42794e8221)

#define BT\_BUF\_ISO\_RX\_COUNT

**Definition** buf.h:85

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)

#define MAX(a, b)

Obtain the maximum of two values.

**Definition** util.h:376

Buffer count needed for HCI ACL, HCI ISO or Event RX buffers.

## [◆ ](#ga3e16a5f4c0c9c4c9117d972b7043d82b)BT\_BUF\_RX\_SIZE

| #define BT\_BUF\_RX\_SIZE |
| --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

**Value:**

([MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)([MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)([BT\_BUF\_ACL\_RX\_SIZE](#ga3ad106326ce13d6eb61d0ac16f592003), [BT\_BUF\_EVT\_RX\_SIZE](#gac76caf2a7fce82ba652eab094162ec66)), \

[BT\_BUF\_ISO\_RX\_SIZE](#gae5db5f9f282f9675fe620842e0c50337)))

[BT\_BUF\_ACL\_RX\_SIZE](#ga3ad106326ce13d6eb61d0ac16f592003)

#define BT\_BUF\_ACL\_RX\_SIZE

Data size needed for HCI ACL RX buffers.

**Definition** buf.h:75

[BT\_BUF\_EVT\_RX\_SIZE](#gac76caf2a7fce82ba652eab094162ec66)

#define BT\_BUF\_EVT\_RX\_SIZE

Data size needed for HCI Event RX buffers.

**Definition** buf.h:78

[BT\_BUF\_ISO\_RX\_SIZE](#gae5db5f9f282f9675fe620842e0c50337)

#define BT\_BUF\_ISO\_RX\_SIZE

**Definition** buf.h:84

Data size needed for HCI ACL, HCI ISO or Event RX buffers.

## [◆ ](#ga9c114a415dc8fc2b84503736b1283468)BT\_BUF\_SIZE

| #define BT\_BUF\_SIZE | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

**Value:**

([BT\_BUF\_RESERVE](#ga41f80f3995e79982f704f832394a6bef) + (size))

[BT\_BUF\_RESERVE](#ga41f80f3995e79982f704f832394a6bef)

#define BT\_BUF\_RESERVE

**Definition** buf.h:55

Helper to include reserved HCI data in buffer calculations.

## Enumeration Type Documentation

## [◆ ](#gafe1539a89ba3389d52d010a071620d7b)bt\_buf\_type

| enum [bt\_buf\_type](#gafe1539a89ba3389d52d010a071620d7b) |
| --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

Possible types of buffers passed around the Bluetooth stack.

| Enumerator | |
| --- | --- |
| BT\_BUF\_CMD | HCI command. |
| BT\_BUF\_EVT | HCI event. |
| BT\_BUF\_ACL\_OUT | Outgoing ACL data. |
| BT\_BUF\_ACL\_IN | Incoming ACL data. |
| BT\_BUF\_ISO\_OUT | Outgoing ISO data. |
| BT\_BUF\_ISO\_IN | Incoming ISO data. |
| BT\_BUF\_H4 | H:4 data. |

## Function Documentation

## [◆ ](#ga7b7a19302881dea458fbd2e9e2309b30)bt\_buf\_get\_evt()

| struct [net\_buf](structnet__buf.md) \* bt\_buf\_get\_evt | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *evt*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *discardable*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

Allocate a buffer for an HCI Event.

This will set the buffer type so [bt\_buf\_set\_type()](#gaec645aec3d6fb845f214c07f2a864fec) does not need to be explicitly called.

Parameters
:   | evt | HCI event code |
    | --- | --- |
    | discardable | Whether the driver considers the event discardable. |
    | timeout | Non-negative waiting period to obtain a buffer or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Returns
:   A new buffer.

## [◆ ](#ga4013cce9637f5aa2742d1f1aaa00e7ee)bt\_buf\_get\_rx()

| struct [net\_buf](structnet__buf.md) \* bt\_buf\_get\_rx | ( | enum [bt\_buf\_type](#gafe1539a89ba3389d52d010a071620d7b) | *type*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

Allocate a buffer for incoming data.

This will set the buffer type so [bt\_buf\_set\_type()](#gaec645aec3d6fb845f214c07f2a864fec) does not need to be explicitly called.

Parameters
:   | type | Type of buffer. Only BT\_BUF\_EVT, BT\_BUF\_ACL\_IN and BT\_BUF\_ISO\_IN are allowed. |
    | --- | --- |
    | timeout | Non-negative waiting period to obtain a buffer or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Returns
:   A new buffer.

## [◆ ](#ga761a31b7fb19f2325b3a9ac6b1fb1700)bt\_buf\_get\_tx()

| struct [net\_buf](structnet__buf.md) \* bt\_buf\_get\_tx | ( | enum [bt\_buf\_type](#gafe1539a89ba3389d52d010a071620d7b) | *type*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

Allocate a buffer for outgoing data.

This will set the buffer type so [bt\_buf\_set\_type()](#gaec645aec3d6fb845f214c07f2a864fec) does not need to be explicitly called.

Parameters
:   | type | Type of buffer. Only BT\_BUF\_CMD, BT\_BUF\_ACL\_OUT or BT\_BUF\_H4, when operating on H:4 mode, are allowed. |
    | --- | --- |
    | timeout | Non-negative waiting period to obtain a buffer or one of the special values K\_NO\_WAIT and K\_FOREVER. |
    | data | Initial data to append to buffer. |
    | size | Initial data size. |

Returns
:   A new buffer.

## [◆ ](#ga2e35f0593e54d28bad62d6b8933f1599)bt\_buf\_get\_type()

| | enum [bt\_buf\_type](#gafe1539a89ba3389d52d010a071620d7b) bt\_buf\_get\_type | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

Get the buffer type.

Parameters
:   | buf | Bluetooth buffer |
    | --- | --- |

Returns
:   The BT\_\* type to of the buffer

## [◆ ](#gaec645aec3d6fb845f214c07f2a864fec)bt\_buf\_set\_type()

| | void bt\_buf\_set\_type | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | enum [bt\_buf\_type](#gafe1539a89ba3389d52d010a071620d7b) | *type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](bluetooth_2buf_8h.md)>`

Set the buffer type.

Parameters
:   | buf | Bluetooth buffer |
    | --- | --- |
    | type | The BT\_\* type to set the buffer to |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
