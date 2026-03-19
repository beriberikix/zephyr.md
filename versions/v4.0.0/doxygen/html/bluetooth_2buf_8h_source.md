---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/bluetooth_2buf_8h_source.html
original_path: doxygen/html/bluetooth_2buf_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

buf.h

[Go to the documentation of this file.](bluetooth_2buf_8h.md)

1

4

5/\*

6 \* Copyright (c) 2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_BUF\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_BUF\_H\_

13

20

21#include <[stdint.h](stdint_8h.md)>

22

23#include <[zephyr/net\_buf.h](net__buf_8h.md)>

24#include <[zephyr/bluetooth/hci.h](hci_8h.md)>

25#include <[zephyr/sys/util.h](sys_2util_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 32](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b)enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) {

[ 34](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1) [BT\_BUF\_CMD](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1),

[ 36](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5) [BT\_BUF\_EVT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5),

[ 38](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091) [BT\_BUF\_ACL\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091),

[ 40](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13) [BT\_BUF\_ACL\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13),

[ 42](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e) [BT\_BUF\_ISO\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e),

[ 44](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e) [BT\_BUF\_ISO\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e),

[ 46](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baf9a0d91bbd7c45c285615c6e4d9e5b57) [BT\_BUF\_H4](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baf9a0d91bbd7c45c285615c6e4d9e5b57),

47};

48

[ 50](structbt__buf__data.md)struct [bt\_buf\_data](structbt__buf__data.md) {

[ 51](structbt__buf__data.md#a4001ab2a10e2970ce19cc7e0d25a0896) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__buf__data.md#a4001ab2a10e2970ce19cc7e0d25a0896);

52};

53

54/\* Headroom reserved in buffers, primarily for HCI transport encoding purposes \*/

[ 55](group__bt__buf.md#ga41f80f3995e79982f704f832394a6bef)#define BT\_BUF\_RESERVE 1

56

[ 58](group__bt__buf.md#ga9c114a415dc8fc2b84503736b1283468)#define BT\_BUF\_SIZE(size) (BT\_BUF\_RESERVE + (size))

59

[ 61](group__bt__buf.md#ga8f570211d5e391be63bd46c189eac637)#define BT\_BUF\_ACL\_SIZE(size) BT\_BUF\_SIZE(BT\_HCI\_ACL\_HDR\_SIZE + (size))

62

[ 64](group__bt__buf.md#ga098d042ed58592d7c2428967928ee478)#define BT\_BUF\_EVT\_SIZE(size) BT\_BUF\_SIZE(BT\_HCI\_EVT\_HDR\_SIZE + (size))

65

[ 67](group__bt__buf.md#ga9dc9de00be5e8bf673ec60921ea6681b)#define BT\_BUF\_CMD\_SIZE(size) BT\_BUF\_SIZE(BT\_HCI\_CMD\_HDR\_SIZE + (size))

68

[ 70](group__bt__buf.md#gaa820dee05a7202304e1aaa9a36386ca4)#define BT\_BUF\_ISO\_SIZE(size) BT\_BUF\_SIZE(BT\_HCI\_ISO\_HDR\_SIZE + \

71 BT\_HCI\_ISO\_SDU\_TS\_HDR\_SIZE + \

72 (size))

73

[ 75](group__bt__buf.md#ga3ad106326ce13d6eb61d0ac16f592003)#define BT\_BUF\_ACL\_RX\_SIZE BT\_BUF\_ACL\_SIZE(CONFIG\_BT\_BUF\_ACL\_RX\_SIZE)

76

[ 78](group__bt__buf.md#gac76caf2a7fce82ba652eab094162ec66)#define BT\_BUF\_EVT\_RX\_SIZE BT\_BUF\_EVT\_SIZE(CONFIG\_BT\_BUF\_EVT\_RX\_SIZE)

79

80#if defined(CONFIG\_BT\_ISO)

81#define BT\_BUF\_ISO\_RX\_SIZE BT\_BUF\_ISO\_SIZE(CONFIG\_BT\_ISO\_RX\_MTU)

82#define BT\_BUF\_ISO\_RX\_COUNT CONFIG\_BT\_ISO\_RX\_BUF\_COUNT

83#else

[ 84](group__bt__buf.md#gae5db5f9f282f9675fe620842e0c50337)#define BT\_BUF\_ISO\_RX\_SIZE 0

[ 85](group__bt__buf.md#gac45f7915fff9516d9d156a42794e8221)#define BT\_BUF\_ISO\_RX\_COUNT 0

86#endif /\* CONFIG\_BT\_ISO \*/

87

[ 89](group__bt__buf.md#ga3e16a5f4c0c9c4c9117d972b7043d82b)#define BT\_BUF\_RX\_SIZE (MAX(MAX(BT\_BUF\_ACL\_RX\_SIZE, BT\_BUF\_EVT\_RX\_SIZE), \

90 BT\_BUF\_ISO\_RX\_SIZE))

91

[ 93](group__bt__buf.md#gaa3ab0861dfd4ebc5f7485f36c1b0fdf1)#define BT\_BUF\_RX\_COUNT (MAX(MAX(CONFIG\_BT\_BUF\_EVT\_RX\_COUNT, \

94 CONFIG\_BT\_BUF\_ACL\_RX\_COUNT), \

95 BT\_BUF\_ISO\_RX\_COUNT))

96

[ 98](group__bt__buf.md#ga366c2eee5dcc6056430b203d1c020042)#define BT\_BUF\_CMD\_TX\_SIZE BT\_BUF\_CMD\_SIZE(CONFIG\_BT\_BUF\_CMD\_TX\_SIZE)

99

[ 111](group__bt__buf.md#ga4013cce9637f5aa2742d1f1aaa00e7ee)struct [net\_buf](structnet__buf.md) \*[bt\_buf\_get\_rx](group__bt__buf.md#ga4013cce9637f5aa2742d1f1aaa00e7ee)(enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) type, [k\_timeout\_t](structk__timeout__t.md) timeout);

112

[ 126](group__bt__buf.md#ga761a31b7fb19f2325b3a9ac6b1fb1700)struct [net\_buf](structnet__buf.md) \*[bt\_buf\_get\_tx](group__bt__buf.md#ga761a31b7fb19f2325b3a9ac6b1fb1700)(enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) type, [k\_timeout\_t](structk__timeout__t.md) timeout,

127 const void \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56), size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527));

128

[ 140](group__bt__buf.md#ga7b7a19302881dea458fbd2e9e2309b30)struct [net\_buf](structnet__buf.md) \*[bt\_buf\_get\_evt](group__bt__buf.md#ga7b7a19302881dea458fbd2e9e2309b30)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evt, bool discardable, [k\_timeout\_t](structk__timeout__t.md) timeout);

141

[ 147](group__bt__buf.md#gaec645aec3d6fb845f214c07f2a864fec)static inline void [bt\_buf\_set\_type](group__bt__buf.md#gaec645aec3d6fb845f214c07f2a864fec)(struct [net\_buf](structnet__buf.md) \*buf, enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) type)

148{

149 ((struct [bt\_buf\_data](structbt__buf__data.md) \*)[net\_buf\_user\_data](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756)(buf))->[type](structbt__buf__data.md#a4001ab2a10e2970ce19cc7e0d25a0896) = [type](structbt__buf__data.md#a4001ab2a10e2970ce19cc7e0d25a0896);

150}

151

[ 158](group__bt__buf.md#ga2e35f0593e54d28bad62d6b8933f1599)static inline enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) [bt\_buf\_get\_type](group__bt__buf.md#ga2e35f0593e54d28bad62d6b8933f1599)(struct [net\_buf](structnet__buf.md) \*buf)

159{

160 return (enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b))((struct [bt\_buf\_data](structbt__buf__data.md) \*)[net\_buf\_user\_data](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756)(buf))

161 ->[type](structbt__buf__data.md#a4001ab2a10e2970ce19cc7e0d25a0896);

162}

163

167

168#ifdef \_\_cplusplus

169}

170#endif

171

172#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_BUF\_H\_ \*/

[bt\_buf\_get\_type](group__bt__buf.md#ga2e35f0593e54d28bad62d6b8933f1599)

static enum bt\_buf\_type bt\_buf\_get\_type(struct net\_buf \*buf)

Get the buffer type.

**Definition** buf.h:158

[bt\_buf\_get\_rx](group__bt__buf.md#ga4013cce9637f5aa2742d1f1aaa00e7ee)

struct net\_buf \* bt\_buf\_get\_rx(enum bt\_buf\_type type, k\_timeout\_t timeout)

Allocate a buffer for incoming data.

[bt\_buf\_get\_tx](group__bt__buf.md#ga761a31b7fb19f2325b3a9ac6b1fb1700)

struct net\_buf \* bt\_buf\_get\_tx(enum bt\_buf\_type type, k\_timeout\_t timeout, const void \*data, size\_t size)

Allocate a buffer for outgoing data.

[bt\_buf\_get\_evt](group__bt__buf.md#ga7b7a19302881dea458fbd2e9e2309b30)

struct net\_buf \* bt\_buf\_get\_evt(uint8\_t evt, bool discardable, k\_timeout\_t timeout)

Allocate a buffer for an HCI Event.

[bt\_buf\_set\_type](group__bt__buf.md#gaec645aec3d6fb845f214c07f2a864fec)

static void bt\_buf\_set\_type(struct net\_buf \*buf, enum bt\_buf\_type type)

Set the buffer type.

**Definition** buf.h:147

[bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b)

bt\_buf\_type

Possible types of buffers passed around the Bluetooth stack.

**Definition** buf.h:32

[BT\_BUF\_EVT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5)

@ BT\_BUF\_EVT

HCI event.

**Definition** buf.h:36

[BT\_BUF\_ISO\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e)

@ BT\_BUF\_ISO\_OUT

Outgoing ISO data.

**Definition** buf.h:42

[BT\_BUF\_ACL\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091)

@ BT\_BUF\_ACL\_OUT

Outgoing ACL data.

**Definition** buf.h:38

[BT\_BUF\_ISO\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e)

@ BT\_BUF\_ISO\_IN

Incoming ISO data.

**Definition** buf.h:44

[BT\_BUF\_CMD](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1)

@ BT\_BUF\_CMD

HCI command.

**Definition** buf.h:34

[BT\_BUF\_H4](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baf9a0d91bbd7c45c285615c6e4d9e5b57)

@ BT\_BUF\_H4

H:4 data.

**Definition** buf.h:46

[BT\_BUF\_ACL\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13)

@ BT\_BUF\_ACL\_IN

Incoming ACL data.

**Definition** buf.h:40

[net\_buf\_user\_data](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756)

static void \* net\_buf\_user\_data(const struct net\_buf \*buf)

Get a pointer to the user data of a buffer.

**Definition** net\_buf.h:1576

[hci.h](hci_8h.md)

[net\_buf.h](net__buf_8h.md)

Buffer management.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_buf\_data](structbt__buf__data.md)

This is a base type for bt\_buf user data.

**Definition** buf.h:50

[bt\_buf\_data::type](structbt__buf__data.md#a4001ab2a10e2970ce19cc7e0d25a0896)

uint8\_t type

**Definition** buf.h:51

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_buf::size](structnet__buf.md#a1522d81a002804223e25300a6961f527)

uint16\_t size

Amount of data that this buffer can store.

**Definition** net\_buf.h:1038

[net\_buf::data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** net\_buf.h:1032

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [buf.h](bluetooth_2buf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
