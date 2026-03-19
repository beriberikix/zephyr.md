---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/virtual__mgmt_8h_source.html
original_path: doxygen/html/virtual__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtual\_mgmt.h

[Go to the documentation of this file.](virtual__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_VIRTUAL\_MGMT\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_VIRTUAL\_MGMT\_H\_

14

15#include <[zephyr/net/virtual.h](virtual_8h.md)>

16#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

30

32

33#define \_NET\_VIRTUAL\_INTERFACE\_LAYER NET\_MGMT\_LAYER\_L2

34#define \_NET\_VIRTUAL\_INTERFACE\_CODE 0x209

35#define \_NET\_VIRTUAL\_INTERFACE\_BASE \

36 (NET\_MGMT\_IFACE\_BIT | \

37 NET\_MGMT\_LAYER(\_NET\_VIRTUAL\_INTERFACE\_LAYER) | \

38 NET\_MGMT\_LAYER\_CODE(\_NET\_VIRTUAL\_INTERFACE\_CODE))

39#define \_NET\_VIRTUAL\_INTERFACE\_EVENT \

40 (\_NET\_VIRTUAL\_INTERFACE\_BASE | NET\_MGMT\_EVENT\_BIT)

41

42struct virtual\_interface\_req\_params {

43 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family;

44 union {

45 struct in\_addr peer4addr;

46 struct in6\_addr peer6addr;

47 int mtu;

48 struct virtual\_interface\_link\_types link\_types;

49 };

50};

51

52enum net\_request\_virtual\_interface\_cmd {

53 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_PEER\_ADDR = 1,

54 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_PEER\_ADDR,

55 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_MTU,

56 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_MTU,

57 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_LINK\_TYPE,

58 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_LINK\_TYPE,

59};

60

61#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_PEER\_ADDRESS \

62 (\_NET\_VIRTUAL\_INTERFACE\_BASE | \

63 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_PEER\_ADDR)

64

65[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_PEER\_ADDRESS);

66

67#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_MTU \

68 (\_NET\_VIRTUAL\_INTERFACE\_BASE | \

69 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_MTU)

70

71[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_MTU);

72

73#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_LINK\_TYPE \

74 (\_NET\_VIRTUAL\_INTERFACE\_BASE | \

75 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_LINK\_TYPE)

76

77[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_LINK\_TYPE);

78

79#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_PEER\_ADDRESS \

80 (\_NET\_VIRTUAL\_INTERFACE\_BASE | \

81 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_PEER\_ADDR)

82

83[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_PEER\_ADDRESS);

84

85#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_MTU \

86 (\_NET\_VIRTUAL\_INTERFACE\_BASE | \

87 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_MTU)

88

89[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_MTU);

90

91#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_LINK\_TYPE \

92 (\_NET\_VIRTUAL\_INTERFACE\_BASE | \

93 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_LINK\_TYPE)

94

95[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_LINK\_TYPE);

96

97struct [net\_if](structnet__if.md);

98

100

104

105#ifdef \_\_cplusplus

106}

107#endif

108

109#endif /\* ZEPHYR\_INCLUDE\_NET\_VIRTUAL\_MGMT\_H\_ \*/

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:168

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:111

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

[virtual.h](virtual_8h.md)

Virtual Network Interface.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [virtual\_mgmt.h](virtual__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
