---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ethernet__vlan_8h_source.html
original_path: doxygen/html/ethernet__vlan_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_vlan.h

[Go to the documentation of this file.](ethernet__vlan_8h.md)

1

6

7/\*

8 \* Copyright (c) 2018 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_ETHERNET\_VLAN\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_ETHERNET\_VLAN\_H\_

15

22

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

[ 30](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70)#define NET\_VLAN\_TAG\_UNSPEC 0x0fff

31

[ 39](group__vlan__api.md#gad12123bb6c9920f21a6faed0e9bf70a6)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_eth\_vlan\_get\_vid](group__vlan__api.md#gad12123bb6c9920f21a6faed0e9bf70a6)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

40{

41 return tci & 0x0fff;

42}

43

[ 51](group__vlan__api.md#ga090648b166db1dc5ee9db71bfba1f97b)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_eth\_vlan\_get\_dei](group__vlan__api.md#ga090648b166db1dc5ee9db71bfba1f97b)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

52{

53 return (tci >> 12) & 0x01;

54}

55

[ 63](group__vlan__api.md#gafc746a075a23e4ad2c1c76328a8d773a)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_eth\_vlan\_get\_pcp](group__vlan__api.md#gafc746a075a23e4ad2c1c76328a8d773a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

64{

65 return (tci >> 13) & 0x07;

66}

67

[ 76](group__vlan__api.md#ga06b2977281f627ebb9529512aecc20dd)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_eth\_vlan\_set\_vid](group__vlan__api.md#ga06b2977281f627ebb9529512aecc20dd)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vid)

77{

78 return (tci & 0xf000) | (vid & 0x0fff);

79}

80

[ 89](group__vlan__api.md#ga6fcea099258c6be9c7cbfbd92fd4e8ab)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_eth\_vlan\_set\_dei](group__vlan__api.md#ga6fcea099258c6be9c7cbfbd92fd4e8ab)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci, bool dei)

90{

91 return (tci & 0xefff) | ((!!dei) << 12);

92}

93

[ 102](group__vlan__api.md#gadee54f9a2af345dd3981f39d73e1bc10)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_eth\_vlan\_set\_pcp](group__vlan__api.md#gadee54f9a2af345dd3981f39d73e1bc10)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pcp)

103{

104 return (tci & 0x1fff) | ((pcp & 0x07) << 13);

105}

106

107#ifdef \_\_cplusplus

108}

109#endif

110

114

115

116#endif /\* ZEPHYR\_INCLUDE\_NET\_ETHERNET\_VLAN\_H\_ \*/

[net\_eth\_vlan\_set\_vid](group__vlan__api.md#ga06b2977281f627ebb9529512aecc20dd)

static uint16\_t net\_eth\_vlan\_set\_vid(uint16\_t tci, uint16\_t vid)

Set VLAN identifier to TCI.

**Definition** ethernet\_vlan.h:76

[net\_eth\_vlan\_get\_dei](group__vlan__api.md#ga090648b166db1dc5ee9db71bfba1f97b)

static uint8\_t net\_eth\_vlan\_get\_dei(uint16\_t tci)

Get Drop Eligible Indicator from TCI.

**Definition** ethernet\_vlan.h:51

[net\_eth\_vlan\_set\_dei](group__vlan__api.md#ga6fcea099258c6be9c7cbfbd92fd4e8ab)

static uint16\_t net\_eth\_vlan\_set\_dei(uint16\_t tci, bool dei)

Set Drop Eligible Indicator to TCI.

**Definition** ethernet\_vlan.h:89

[net\_eth\_vlan\_get\_vid](group__vlan__api.md#gad12123bb6c9920f21a6faed0e9bf70a6)

static uint16\_t net\_eth\_vlan\_get\_vid(uint16\_t tci)

Get VLAN identifier from TCI.

**Definition** ethernet\_vlan.h:39

[net\_eth\_vlan\_set\_pcp](group__vlan__api.md#gadee54f9a2af345dd3981f39d73e1bc10)

static uint16\_t net\_eth\_vlan\_set\_pcp(uint16\_t tci, uint8\_t pcp)

Set Priority Code Point to TCI.

**Definition** ethernet\_vlan.h:102

[net\_eth\_vlan\_get\_pcp](group__vlan__api.md#gafc746a075a23e4ad2c1c76328a8d773a)

static uint8\_t net\_eth\_vlan\_get\_pcp(uint16\_t tci)

Get Priority Code Point from TCI.

**Definition** ethernet\_vlan.h:63

[types.h](include_2zephyr_2types_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet\_vlan.h](ethernet__vlan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
