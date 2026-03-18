---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/avdtp_8h_source.html
original_path: doxygen/html/avdtp_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

avdtp.h

[Go to the documentation of this file.](avdtp_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AVDTP\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AVDTP\_H\_

12

13#include <[zephyr/bluetooth/l2cap.h](l2cap_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 20](structbt__avdtp__seid__info.md)struct [bt\_avdtp\_seid\_info](structbt__avdtp__seid__info.md) {

[ 22](structbt__avdtp__seid__info.md#a56f008e3e3fddcab2a67a21c10116a3f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__avdtp__seid__info.md#a56f008e3e3fddcab2a67a21c10116a3f):6;

[ 24](structbt__avdtp__seid__info.md#acb3914f52ee4decef0649fb8eb859487) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [inuse](structbt__avdtp__seid__info.md#acb3914f52ee4decef0649fb8eb859487):1;

[ 26](structbt__avdtp__seid__info.md#afb8ec9e677ffcb0a6354b82bf3d473c9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rfa0](structbt__avdtp__seid__info.md#afb8ec9e677ffcb0a6354b82bf3d473c9):1;

[ 28](structbt__avdtp__seid__info.md#a5f8e4fa4000cc21032b2f5996c07dc57) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [media\_type](structbt__avdtp__seid__info.md#a5f8e4fa4000cc21032b2f5996c07dc57):4;

[ 30](structbt__avdtp__seid__info.md#a0241167057783c20110fc23c002f4b4d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tsep](structbt__avdtp__seid__info.md#a0241167057783c20110fc23c002f4b4d):1;

[ 32](structbt__avdtp__seid__info.md#a9a29e533600151e233b49342874bb8fa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rfa1](structbt__avdtp__seid__info.md#a9a29e533600151e233b49342874bb8fa):3;

33} \_\_packed;

34

[ 36](structbt__avdtp__seid__lsep.md)struct [bt\_avdtp\_seid\_lsep](structbt__avdtp__seid__lsep.md) {

[ 38](structbt__avdtp__seid__lsep.md#abad1ec2065348ec2eda669bc6729945b) struct [bt\_avdtp\_seid\_info](structbt__avdtp__seid__info.md) [sep](structbt__avdtp__seid__lsep.md#abad1ec2065348ec2eda669bc6729945b);

[ 40](structbt__avdtp__seid__lsep.md#a62b122dafb5304bcdd2770c73aefd512) struct [bt\_avdtp\_seid\_lsep](structbt__avdtp__seid__lsep.md) \*[next](structbt__avdtp__seid__lsep.md#a62b122dafb5304bcdd2770c73aefd512);

41};

42

[ 44](structbt__avdtp__stream.md)struct [bt\_avdtp\_stream](structbt__avdtp__stream.md) {

[ 45](structbt__avdtp__stream.md#a1d29697103ce0c7841c8e9f0b7119d46) struct [bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md) [chan](structbt__avdtp__stream.md#a1d29697103ce0c7841c8e9f0b7119d46); /\* Transport Channel\*/

[ 46](structbt__avdtp__stream.md#ad9fb733cae9f63854ee7e425ab4ee3f0) struct [bt\_avdtp\_seid\_info](structbt__avdtp__seid__info.md) [lsep](structbt__avdtp__stream.md#ad9fb733cae9f63854ee7e425ab4ee3f0); /\* Configured Local SEP \*/

[ 47](structbt__avdtp__stream.md#a81b7ac4fcfe5d6bdc02548616cbd8a6e) struct [bt\_avdtp\_seid\_info](structbt__avdtp__seid__info.md) [rsep](structbt__avdtp__stream.md#a81b7ac4fcfe5d6bdc02548616cbd8a6e); /\* Configured Remote SEP\*/

[ 48](structbt__avdtp__stream.md#a0ad0e0aa07f3d70ebec105db6356f722) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](structbt__avdtp__stream.md#a0ad0e0aa07f3d70ebec105db6356f722); /\* current state of the stream \*/

[ 49](structbt__avdtp__stream.md#a9ab341af107de917b20545ae5ac34274) struct [bt\_avdtp\_stream](structbt__avdtp__stream.md) \*[next](structbt__avdtp__stream.md#a9ab341af107de917b20545ae5ac34274);

50};

51

52#ifdef \_\_cplusplus

53}

54#endif

55

56#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AVDTP\_H\_ \*/

[l2cap.h](l2cap_8h.md)

Bluetooth L2CAP handling.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_avdtp\_seid\_info](structbt__avdtp__seid__info.md)

AVDTP SEID Information.

**Definition** avdtp.h:20

[bt\_avdtp\_seid\_info::tsep](structbt__avdtp__seid__info.md#a0241167057783c20110fc23c002f4b4d)

uint8\_t tsep

TSEP of the End Point.

**Definition** avdtp.h:30

[bt\_avdtp\_seid\_info::id](structbt__avdtp__seid__info.md#a56f008e3e3fddcab2a67a21c10116a3f)

uint8\_t id

Stream End Point ID.

**Definition** avdtp.h:22

[bt\_avdtp\_seid\_info::media\_type](structbt__avdtp__seid__info.md#a5f8e4fa4000cc21032b2f5996c07dc57)

uint8\_t media\_type

Media-type of the End Point.

**Definition** avdtp.h:28

[bt\_avdtp\_seid\_info::rfa1](structbt__avdtp__seid__info.md#a9a29e533600151e233b49342874bb8fa)

uint8\_t rfa1

Reserved.

**Definition** avdtp.h:32

[bt\_avdtp\_seid\_info::inuse](structbt__avdtp__seid__info.md#acb3914f52ee4decef0649fb8eb859487)

uint8\_t inuse

End Point usage status.

**Definition** avdtp.h:24

[bt\_avdtp\_seid\_info::rfa0](structbt__avdtp__seid__info.md#afb8ec9e677ffcb0a6354b82bf3d473c9)

uint8\_t rfa0

Reserved.

**Definition** avdtp.h:26

[bt\_avdtp\_seid\_lsep](structbt__avdtp__seid__lsep.md)

AVDTP Local SEP.

**Definition** avdtp.h:36

[bt\_avdtp\_seid\_lsep::next](structbt__avdtp__seid__lsep.md#a62b122dafb5304bcdd2770c73aefd512)

struct bt\_avdtp\_seid\_lsep \* next

Pointer to next local Stream End Point structure.

**Definition** avdtp.h:40

[bt\_avdtp\_seid\_lsep::sep](structbt__avdtp__seid__lsep.md#abad1ec2065348ec2eda669bc6729945b)

struct bt\_avdtp\_seid\_info sep

Stream End Point information.

**Definition** avdtp.h:38

[bt\_avdtp\_stream](structbt__avdtp__stream.md)

AVDTP Stream.

**Definition** avdtp.h:44

[bt\_avdtp\_stream::state](structbt__avdtp__stream.md#a0ad0e0aa07f3d70ebec105db6356f722)

uint8\_t state

**Definition** avdtp.h:48

[bt\_avdtp\_stream::chan](structbt__avdtp__stream.md#a1d29697103ce0c7841c8e9f0b7119d46)

struct bt\_l2cap\_br\_chan chan

**Definition** avdtp.h:45

[bt\_avdtp\_stream::rsep](structbt__avdtp__stream.md#a81b7ac4fcfe5d6bdc02548616cbd8a6e)

struct bt\_avdtp\_seid\_info rsep

**Definition** avdtp.h:47

[bt\_avdtp\_stream::next](structbt__avdtp__stream.md#a9ab341af107de917b20545ae5ac34274)

struct bt\_avdtp\_stream \* next

**Definition** avdtp.h:49

[bt\_avdtp\_stream::lsep](structbt__avdtp__stream.md#ad9fb733cae9f63854ee7e425ab4ee3f0)

struct bt\_avdtp\_seid\_info lsep

**Definition** avdtp.h:46

[bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md)

BREDR L2CAP Channel structure.

**Definition** l2cap.h:245

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [avdtp.h](avdtp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
