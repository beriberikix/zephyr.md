---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sip__svc__agilex__mailbox_8h_source.html
original_path: doxygen/html/sip__svc__agilex__mailbox_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc\_agilex\_mailbox.h

[Go to the documentation of this file.](sip__svc__agilex__mailbox_8h.md)

1/\*

2 \* Copyright (c) 2022-2023, Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SIP\_SVC\_AGILEX\_MB\_H\_

8#define ZEPHYR\_INCLUDE\_SIP\_SVC\_AGILEX\_MB\_H\_

9

17

[ 18](sip__svc__agilex__mailbox_8h.md#aa56d732f7a2de4298a5dda992b1405de)#define SIP\_SVP\_MB\_MAX\_WORD\_SIZE 1024

[ 19](sip__svc__agilex__mailbox_8h.md#afccd6d2a8364c2273de2b31a448f5de3)#define SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_OFFSET 24

[ 20](sip__svc__agilex__mailbox_8h.md#a3532db48b21765fb2aa419522a794a94)#define SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_MASK 0xFF

[ 21](sip__svc__agilex__mailbox_8h.md#a6c24e3a782d918ebc001fca12ba8321a)#define SIP\_SVP\_MB\_HEADER\_LENGTH\_OFFSET 12

[ 22](sip__svc__agilex__mailbox_8h.md#a66f47d95a199a02038c3d25f49e46b37)#define SIP\_SVP\_MB\_HEADER\_LENGTH\_MASK 0x7FF

23

[ 24](sip__svc__agilex__mailbox_8h.md#a6a29fa9f750979dce255ee2b56b0a953)#define SIP\_SVC\_MB\_HEADER\_GET\_CLIENT\_ID(header) \

25 ((header) >> SIP\_SVP\_MB\_HEADER\_CLIENT\_ID\_OFFSET & \

26 SIP\_SVP\_MB\_HEADER\_CLIENT\_ID\_MASK)

27

[ 28](sip__svc__agilex__mailbox_8h.md#abb0c7166d5c2ae113ba20315c0eb44ea)#define SIP\_SVC\_MB\_HEADER\_GET\_TRANS\_ID(header) \

29 ((header) >> SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_OFFSET & \

30 SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_MASK)

31

[ 32](sip__svc__agilex__mailbox_8h.md#ad960abd8b2e9acb4d78da132d1481705)#define SIP\_SVC\_MB\_HEADER\_SET\_TRANS\_ID(header, id) \

33 (header) &= ~(SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_MASK << \

34 SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_OFFSET); \

35 (header) |= (((id) & SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_MASK) << \

36 SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_OFFSET);

37

[ 38](sip__svc__agilex__mailbox_8h.md#af6e53a9a4c1e4cad501a541cf0a82e48)#define SIP\_SVC\_MB\_HEADER\_GET\_LENGTH(header) \

39 ((header) >> SIP\_SVP\_MB\_HEADER\_LENGTH\_OFFSET & \

40 SIP\_SVP\_MB\_HEADER\_LENGTH\_MASK)

41

42#endif /\* ZEPHYR\_INCLUDE\_SIP\_SVC\_AGILEX\_MB\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sip\_svc](dir_be59f4c2e7724c8d2ef47362c82e9052.md)
- [sip\_svc\_agilex\_mailbox.h](sip__svc__agilex__mailbox_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
