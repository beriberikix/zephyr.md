---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hdlc__rcp__if_8h_source.html
original_path: doxygen/html/hdlc__rcp__if_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hdlc\_rcp\_if.h

[Go to the documentation of this file.](hdlc__rcp__if_8h.md)

1/\*

2 \* Copyright (c) 2024, NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#include <[zephyr/sys/util.h](sys_2util_8h.md)>

15#include <[zephyr/net/net\_if.h](net__if_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 26](hdlc__rcp__if_8h.md#a58fa03009f99c7927c930b06fd1dfd0e)typedef void (\*[hdlc\_rx\_callback\_t](hdlc__rcp__if_8h.md#a58fa03009f99c7927c930b06fd1dfd0e))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, void \*param);

27

[ 29](structhdlc__api.md)struct [hdlc\_api](structhdlc__api.md) {

[ 33](structhdlc__api.md#abeb64661526d0a3e241e6515707284de) struct net\_if\_api [iface\_api](structhdlc__api.md#abeb64661526d0a3e241e6515707284de);

34

[ 44](structhdlc__api.md#a2b18e7cd6dc393769b3d3ad2c8bf63ed) int (\*[register\_rx\_cb](structhdlc__api.md#a2b18e7cd6dc393769b3d3ad2c8bf63ed))([hdlc\_rx\_callback\_t](hdlc__rcp__if_8h.md#a58fa03009f99c7927c930b06fd1dfd0e) hdlc\_rx\_callback, void \*param);

45

[ 57](structhdlc__api.md#a5a1958253b254008cd142c2c3ab33d2a) int (\*[send](structhdlc__api.md#a5a1958253b254008cd142c2c3ab33d2a))(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*frame, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

58

[ 67](structhdlc__api.md#a33486d7c73df2958bf89bfe500b27464) int (\*[deinit](structhdlc__api.md#a33486d7c73df2958bf89bfe500b27464))(void);

68};

69

70/\* Make sure that the interface API is properly setup inside

71 \* HDLC interface API struct (it is the first one).

72 \*/

73BUILD\_ASSERT(offsetof(struct [hdlc\_api](structhdlc__api.md), iface\_api) == 0);

74

75#ifdef \_\_cplusplus

76}

77#endif

[hdlc\_rx\_callback\_t](hdlc__rcp__if_8h.md#a58fa03009f99c7927c930b06fd1dfd0e)

void(\* hdlc\_rx\_callback\_t)(uint8\_t \*data, uint16\_t len, void \*param)

OT RCP HDLC RX callback function.

**Definition** hdlc\_rcp\_if.h:26

[net\_if.h](net__if_8h.md)

Public API for network interface.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[hdlc\_api](structhdlc__api.md)

HDLC interface configuration data.

**Definition** hdlc\_rcp\_if.h:29

[hdlc\_api::register\_rx\_cb](structhdlc__api.md#a2b18e7cd6dc393769b3d3ad2c8bf63ed)

int(\* register\_rx\_cb)(hdlc\_rx\_callback\_t hdlc\_rx\_callback, void \*param)

Register the Spinel HDLC RX callback.

**Definition** hdlc\_rcp\_if.h:44

[hdlc\_api::deinit](structhdlc__api.md#a33486d7c73df2958bf89bfe500b27464)

int(\* deinit)(void)

Deinitialize the device.

**Definition** hdlc\_rcp\_if.h:67

[hdlc\_api::send](structhdlc__api.md#a5a1958253b254008cd142c2c3ab33d2a)

int(\* send)(const uint8\_t \*frame, uint16\_t length)

Transmit a HDLC frame.

**Definition** hdlc\_rcp\_if.h:57

[hdlc\_api::iface\_api](structhdlc__api.md#abeb64661526d0a3e241e6515707284de)

struct net\_if\_api iface\_api

HDLC interface API.

**Definition** hdlc\_rcp\_if.h:33

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [hdlc\_rcp\_if](dir_1af8727946a5235b30f274ca84c43895.md)
- [hdlc\_rcp\_if.h](hdlc__rcp__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
