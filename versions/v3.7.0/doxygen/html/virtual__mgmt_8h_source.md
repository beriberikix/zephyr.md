---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/virtual__mgmt_8h_source.html
original_path: doxygen/html/virtual__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

28

30

31#define \_NET\_VIRTUAL\_INTERFACE\_LAYER NET\_MGMT\_LAYER\_L2

32#define \_NET\_VIRTUAL\_INTERFACE\_CODE 0x209

33#define \_NET\_VIRTUAL\_INTERFACE\_BASE \

34 (NET\_MGMT\_IFACE\_BIT | \

35 NET\_MGMT\_LAYER(\_NET\_VIRTUAL\_INTERFACE\_LAYER) | \

36 NET\_MGMT\_LAYER\_CODE(\_NET\_VIRTUAL\_INTERFACE\_CODE))

37#define \_NET\_VIRTUAL\_INTERFACE\_EVENT \

38 (\_NET\_VIRTUAL\_INTERFACE\_BASE | NET\_MGMT\_EVENT\_BIT)

39

40struct virtual\_interface\_req\_params {

41 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family;

42 union {

43 struct in\_addr peer4addr;

44 struct in6\_addr peer6addr;

45 int mtu;

46 struct virtual\_interface\_link\_types link\_types;

47 };

48};

49

50enum net\_request\_virtual\_interface\_cmd {

51 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_PEER\_ADDR = 1,

52 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_PEER\_ADDR,

53 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_MTU,

54 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_MTU,

55 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_LINK\_TYPE,

56 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_LINK\_TYPE,

57};

58

59#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_PEER\_ADDRESS \

60 (\_NET\_VIRTUAL\_INTERFACE\_BASE | \

61 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_PEER\_ADDR)

62

63[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_PEER\_ADDRESS);

64

65#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_MTU \

66 (\_NET\_VIRTUAL\_INTERFACE\_BASE | \

67 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_MTU)

68

69[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_MTU);

70

71#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_LINK\_TYPE \

72 (\_NET\_VIRTUAL\_INTERFACE\_BASE | \

73 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_LINK\_TYPE)

74

75[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_LINK\_TYPE);

76

77#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_PEER\_ADDRESS \

78 (\_NET\_VIRTUAL\_INTERFACE\_BASE | \

79 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_PEER\_ADDR)

80

81[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_PEER\_ADDRESS);

82

83#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_MTU \

84 (\_NET\_VIRTUAL\_INTERFACE\_BASE | \

85 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_MTU)

86

87[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_MTU);

88

89#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_LINK\_TYPE \

90 (\_NET\_VIRTUAL\_INTERFACE\_BASE | \

91 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_LINK\_TYPE)

92

93[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_LINK\_TYPE);

94

95struct [net\_if](structnet__if.md);

96

98

102

103#ifdef \_\_cplusplus

104}

105#endif

106

107#endif /\* ZEPHYR\_INCLUDE\_NET\_VIRTUAL\_MGMT\_H\_ \*/

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:164

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:109

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[virtual.h](virtual_8h.md)

Virtual Network Interface.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [virtual\_mgmt.h](virtual__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
