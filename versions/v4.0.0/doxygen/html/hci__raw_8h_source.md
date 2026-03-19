---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hci__raw_8h_source.html
original_path: doxygen/html/hci__raw_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci\_raw.h

[Go to the documentation of this file.](hci__raw_8h.md)

1

4

5/\*

6 \* Copyright (c) 2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_RAW\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_RAW\_H\_

12

19

20#include <[stdint.h](stdint_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 35](group__hci__raw.md#ga8de934e01eb9a16a3c9d096151e58313)int [bt\_send](group__hci__raw.md#ga8de934e01eb9a16a3c9d096151e58313)(struct [net\_buf](structnet__buf.md) \*buf);

36

37enum {

[ 43](group__hci__raw.md#gga86bca5821000418c323335e250754a84aef221882801448593d4e2771305e5c12) [BT\_HCI\_RAW\_MODE\_PASSTHROUGH](group__hci__raw.md#gga86bca5821000418c323335e250754a84aef221882801448593d4e2771305e5c12) = 0x00,

44

[ 51](group__hci__raw.md#gga86bca5821000418c323335e250754a84a3b9f471e60e3e295c2e687811fb2a0b2) [BT\_HCI\_RAW\_MODE\_H4](group__hci__raw.md#gga86bca5821000418c323335e250754a84a3b9f471e60e3e295c2e687811fb2a0b2) = 0x01,

52};

53

[ 62](group__hci__raw.md#gaeac8c91975e3385b56c5e4b957a5c0db)int [bt\_hci\_raw\_set\_mode](group__hci__raw.md#gaeac8c91975e3385b56c5e4b957a5c0db)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode);

63

[ 70](group__hci__raw.md#gaa6bdef963d4d62dab1df6975453eb761)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_hci\_raw\_get\_mode](group__hci__raw.md#gaa6bdef963d4d62dab1df6975453eb761)(void);

71

[ 72](group__hci__raw.md#ga3362c6f543530ee2e84033289cc338dc)#define BT\_HCI\_ERR\_EXT\_HANDLED 0xff

73

[ 80](group__hci__raw.md#gafba7e7bb992c0e58f692e7548fd70d7a)#define BT\_HCI\_RAW\_CMD\_EXT(\_op, \_min\_len, \_func) \

81 { \

82 .op = \_op, \

83 .min\_len = \_min\_len, \

84 .func = \_func, \

85 }

86

[ 87](structbt__hci__raw__cmd__ext.md)struct [bt\_hci\_raw\_cmd\_ext](structbt__hci__raw__cmd__ext.md) {

[ 89](structbt__hci__raw__cmd__ext.md#a3b6fb18d5fabcc5f10265d9de3e46c48) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [op](structbt__hci__raw__cmd__ext.md#a3b6fb18d5fabcc5f10265d9de3e46c48);

90

[ 92](structbt__hci__raw__cmd__ext.md#a04041d07145923ffb7116136e3c70ffa) size\_t [min\_len](structbt__hci__raw__cmd__ext.md#a04041d07145923ffb7116136e3c70ffa);

93

[ 105](structbt__hci__raw__cmd__ext.md#a364aa7239debd06655d7e51f2eb28ee5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[func](structbt__hci__raw__cmd__ext.md#a364aa7239debd06655d7e51f2eb28ee5))(struct [net\_buf](structnet__buf.md) \*buf);

106};

107

[ 116](group__hci__raw.md#ga9ebd7ac0d9779b52dc971f43158eacdd)void [bt\_hci\_raw\_cmd\_ext\_register](group__hci__raw.md#ga9ebd7ac0d9779b52dc971f43158eacdd)(struct [bt\_hci\_raw\_cmd\_ext](structbt__hci__raw__cmd__ext.md) \*cmds, size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527));

117

[ 128](group__hci__raw.md#gaae30308fe69b1b2fd2972dbcd5a34d9f)int [bt\_enable\_raw](group__hci__raw.md#gaae30308fe69b1b2fd2972dbcd5a34d9f)(struct [k\_fifo](structk__fifo.md) \*rx\_queue);

129

130#ifdef \_\_cplusplus

131}

132#endif

136

137#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_RAW\_H\_ \*/

[bt\_send](group__hci__raw.md#ga8de934e01eb9a16a3c9d096151e58313)

int bt\_send(struct net\_buf \*buf)

Send packet to the Bluetooth controller.

[bt\_hci\_raw\_cmd\_ext\_register](group__hci__raw.md#ga9ebd7ac0d9779b52dc971f43158eacdd)

void bt\_hci\_raw\_cmd\_ext\_register(struct bt\_hci\_raw\_cmd\_ext \*cmds, size\_t size)

Register Bluetooth RAW command extension table.

[bt\_hci\_raw\_get\_mode](group__hci__raw.md#gaa6bdef963d4d62dab1df6975453eb761)

uint8\_t bt\_hci\_raw\_get\_mode(void)

Get Bluetooth RAW channel mode.

[bt\_enable\_raw](group__hci__raw.md#gaae30308fe69b1b2fd2972dbcd5a34d9f)

int bt\_enable\_raw(struct k\_fifo \*rx\_queue)

Enable Bluetooth RAW channel:

[bt\_hci\_raw\_set\_mode](group__hci__raw.md#gaeac8c91975e3385b56c5e4b957a5c0db)

int bt\_hci\_raw\_set\_mode(uint8\_t mode)

Set Bluetooth RAW channel mode.

[BT\_HCI\_RAW\_MODE\_H4](group__hci__raw.md#gga86bca5821000418c323335e250754a84a3b9f471e60e3e295c2e687811fb2a0b2)

@ BT\_HCI\_RAW\_MODE\_H4

H:4 mode.

**Definition** hci\_raw.h:51

[BT\_HCI\_RAW\_MODE\_PASSTHROUGH](group__hci__raw.md#gga86bca5821000418c323335e250754a84aef221882801448593d4e2771305e5c12)

@ BT\_HCI\_RAW\_MODE\_PASSTHROUGH

Passthrough mode.

**Definition** hci\_raw.h:43

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_hci\_raw\_cmd\_ext](structbt__hci__raw__cmd__ext.md)

**Definition** hci\_raw.h:87

[bt\_hci\_raw\_cmd\_ext::min\_len](structbt__hci__raw__cmd__ext.md#a04041d07145923ffb7116136e3c70ffa)

size\_t min\_len

Minimal length of the command.

**Definition** hci\_raw.h:92

[bt\_hci\_raw\_cmd\_ext::func](structbt__hci__raw__cmd__ext.md#a364aa7239debd06655d7e51f2eb28ee5)

uint8\_t(\* func)(struct net\_buf \*buf)

Handler function.

**Definition** hci\_raw.h:105

[bt\_hci\_raw\_cmd\_ext::op](structbt__hci__raw__cmd__ext.md#a3b6fb18d5fabcc5f10265d9de3e46c48)

uint16\_t op

Opcode of the command.

**Definition** hci\_raw.h:89

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2468

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_buf::size](structnet__buf.md#a1522d81a002804223e25300a6961f527)

uint16\_t size

Amount of data that this buffer can store.

**Definition** net\_buf.h:1038

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [hci\_raw.h](hci__raw_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
