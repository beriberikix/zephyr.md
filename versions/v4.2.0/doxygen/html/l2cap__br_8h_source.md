---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/l2cap__br_8h_source.html
original_path: doxygen/html/l2cap__br_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

l2cap\_br.h

[Go to the documentation of this file.](l2cap__br_8h.md)

1

4

5/\*

6 \* Copyright 2025 NXP

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_L2CAP\_BR\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_L2CAP\_BR\_H\_

12

19

20#include <stddef.h>

21#include <[stdint.h](stdint_8h.md)>

22

23#include <[zephyr/bluetooth/buf.h](buf_8h.md)>

24#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

25#include <[zephyr/bluetooth/hci.h](hci_8h.md)>

26#include <[zephyr/kernel.h](kernel_8h.md)>

27#include <[zephyr/net\_buf.h](net__buf_8h.md)>

28#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

29#include <[zephyr/sys/slist.h](slist_8h.md)>

30#include <[zephyr/sys/util.h](sys_2util_8h.md)>

31#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

[ 47](structbt__l2cap__br__echo__cb.md)struct [bt\_l2cap\_br\_echo\_cb](structbt__l2cap__br__echo__cb.md) {

[ 58](structbt__l2cap__br__echo__cb.md#abc56aa16213b05fb9d330e4b0147066b) void (\*[req](structbt__l2cap__br__echo__cb.md#abc56aa16213b05fb9d330e4b0147066b))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) identifier, struct [net\_buf](structnet__buf.md) \*buf);

59

[ 68](structbt__l2cap__br__echo__cb.md#aee34c139bbfb03796aa162bf31687d6c) void (\*[rsp](structbt__l2cap__br__echo__cb.md#aee34c139bbfb03796aa162bf31687d6c))(struct bt\_conn \*conn, struct [net\_buf](structnet__buf.md) \*buf);

69

71 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

72};

73

[ 84](group__bt__l2cap.md#ga62c0115185f5026c1a842848dc5336ce)int [bt\_l2cap\_br\_echo\_cb\_register](group__bt__l2cap.md#ga62c0115185f5026c1a842848dc5336ce)(struct [bt\_l2cap\_br\_echo\_cb](structbt__l2cap__br__echo__cb.md) \*cb);

85

[ 97](group__bt__l2cap.md#ga00ef7d0a42d8e544b195172af44b88b2)int [bt\_l2cap\_br\_echo\_cb\_unregister](group__bt__l2cap.md#ga00ef7d0a42d8e544b195172af44b88b2)(struct [bt\_l2cap\_br\_echo\_cb](structbt__l2cap__br__echo__cb.md) \*cb);

98

[ 102](group__bt__l2cap.md#ga12c146741591a55dc50d7d07f0755daa)#define BT\_L2CAP\_BR\_ECHO\_REQ\_RESERVE BT\_L2CAP\_BUF\_SIZE(4)

103

[ 107](group__bt__l2cap.md#ga2961971c1f80aa6168f6cd47b991bf4d)#define BT\_L2CAP\_BR\_ECHO\_RSP\_RESERVE BT\_L2CAP\_BUF\_SIZE(4)

108

[ 120](group__bt__l2cap.md#ga3c6ad17ba18f5c00e39a379ed735de21)int [bt\_l2cap\_br\_echo\_req](group__bt__l2cap.md#ga3c6ad17ba18f5c00e39a379ed735de21)(struct bt\_conn \*conn, struct [net\_buf](structnet__buf.md) \*buf);

121

[ 134](group__bt__l2cap.md#ga8ebf537cc7e4c0a68a320f9c65c94b05)int [bt\_l2cap\_br\_echo\_rsp](group__bt__l2cap.md#ga8ebf537cc7e4c0a68a320f9c65c94b05)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) identifier, struct [net\_buf](structnet__buf.md) \*buf);

135

136#ifdef \_\_cplusplus

137}

138#endif

139

143

144#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_L2CAP\_BR\_H\_ \*/

[buf.h](buf_8h.md)

Bluetooth data buffer API.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_l2cap\_br\_echo\_cb\_unregister](group__bt__l2cap.md#ga00ef7d0a42d8e544b195172af44b88b2)

int bt\_l2cap\_br\_echo\_cb\_unregister(struct bt\_l2cap\_br\_echo\_cb \*cb)

Unregister ECHO callbacks.

[bt\_l2cap\_br\_echo\_req](group__bt__l2cap.md#ga3c6ad17ba18f5c00e39a379ed735de21)

int bt\_l2cap\_br\_echo\_req(struct bt\_conn \*conn, struct net\_buf \*buf)

Send ECHO data through ECHO request.

[bt\_l2cap\_br\_echo\_cb\_register](group__bt__l2cap.md#ga62c0115185f5026c1a842848dc5336ce)

int bt\_l2cap\_br\_echo\_cb\_register(struct bt\_l2cap\_br\_echo\_cb \*cb)

Register ECHO callbacks.

[bt\_l2cap\_br\_echo\_rsp](group__bt__l2cap.md#ga8ebf537cc7e4c0a68a320f9c65c94b05)

int bt\_l2cap\_br\_echo\_rsp(struct bt\_conn \*conn, uint8\_t identifier, struct net\_buf \*buf)

Send ECHO data through ECHO response.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[hci.h](hci_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[net\_buf.h](net__buf_8h.md)

Buffer management.

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_l2cap\_br\_echo\_cb](structbt__l2cap__br__echo__cb.md)

ECHO request/response callback structure.

**Definition** l2cap\_br.h:47

[bt\_l2cap\_br\_echo\_cb::req](structbt__l2cap__br__echo__cb.md#abc56aa16213b05fb9d330e4b0147066b)

void(\* req)(struct bt\_conn \*conn, uint8\_t identifier, struct net\_buf \*buf)

A ECHO request has been received.

**Definition** l2cap\_br.h:58

[bt\_l2cap\_br\_echo\_cb::rsp](structbt__l2cap__br__echo__cb.md#aee34c139bbfb03796aa162bf31687d6c)

void(\* rsp)(struct bt\_conn \*conn, struct net\_buf \*buf)

A ECHO response has been received.

**Definition** l2cap\_br.h:68

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[atomic.h](sys_2atomic_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [l2cap\_br.h](l2cap__br_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
