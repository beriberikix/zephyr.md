---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/virtual__mgmt_8h_source.html
original_path: doxygen/html/virtual__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

33#define NET\_VIRTUAL\_INTERFACE\_LAYER NET\_MGMT\_LAYER\_L2

34#define NET\_VIRTUAL\_INTERFACE\_CODE NET\_MGMT\_LAYER\_CODE\_VIRTUAL

35#define NET\_VIRTUAL\_INTERFACE\_BASE \

36 (NET\_MGMT\_IFACE\_BIT | \

37 NET\_MGMT\_LAYER(NET\_VIRTUAL\_INTERFACE\_LAYER) | \

38 NET\_MGMT\_LAYER\_CODE(NET\_VIRTUAL\_INTERFACE\_CODE))

39#define NET\_VIRTUAL\_INTERFACE\_EVENT \

40 (NET\_VIRTUAL\_INTERFACE\_BASE | NET\_MGMT\_EVENT\_BIT)

41

42struct virtual\_interface\_req\_params {

43 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family;

44 union {

45 struct in\_addr peer4addr;

46 struct in6\_addr peer6addr;

47 int mtu;

48 struct virtual\_interface\_link\_types link\_types;

49 struct {

50 size\_t len;

51 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data;

52 } private\_key;

53 struct {

54 size\_t len;

55 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data[NET\_VIRTUAL\_MAX\_PUBLIC\_KEY\_LEN];

56 } public\_key;

57 };

58};

59

60enum net\_request\_virtual\_interface\_cmd {

61 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_PEER\_ADDR = 1,

62 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_PEER\_ADDR,

63 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_MTU,

64 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_MTU,

65 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_LINK\_TYPE,

66 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_LINK\_TYPE,

67 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_PRIVATE\_KEY,

68 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_PUBLIC\_KEY,

69};

70

71#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_PEER\_ADDRESS \

72 (NET\_VIRTUAL\_INTERFACE\_BASE | \

73 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_PEER\_ADDR)

74

75[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_PEER\_ADDRESS);

76

77#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_MTU \

78 (NET\_VIRTUAL\_INTERFACE\_BASE | \

79 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_MTU)

80

81[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_MTU);

82

83#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_LINK\_TYPE \

84 (NET\_VIRTUAL\_INTERFACE\_BASE | \

85 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_LINK\_TYPE)

86

87[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_LINK\_TYPE);

88

89#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_PEER\_ADDRESS \

90 (NET\_VIRTUAL\_INTERFACE\_BASE | \

91 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_PEER\_ADDR)

92

93[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_PEER\_ADDRESS);

94

95#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_MTU \

96 (NET\_VIRTUAL\_INTERFACE\_BASE | \

97 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_MTU)

98

99[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_MTU);

100

101#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_LINK\_TYPE \

102 (NET\_VIRTUAL\_INTERFACE\_BASE | \

103 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_LINK\_TYPE)

104

105[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_LINK\_TYPE);

106

107#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_PRIVATE\_KEY \

108 (NET\_VIRTUAL\_INTERFACE\_BASE | \

109 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_SET\_PRIVATE\_KEY)

110

111[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_SET\_PRIVATE\_KEY);

112

113#define NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_PUBLIC\_KEY \

114 (NET\_VIRTUAL\_INTERFACE\_BASE | \

115 NET\_REQUEST\_VIRTUAL\_INTERFACE\_CMD\_GET\_PUBLIC\_KEY)

116

117[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_VIRTUAL\_INTERFACE\_GET\_PUBLIC\_KEY);

118

119struct [net\_if](structnet__if.md);

120

122

126

127#ifdef \_\_cplusplus

128}

129#endif

130

131#endif /\* ZEPHYR\_INCLUDE\_NET\_VIRTUAL\_MGMT\_H\_ \*/

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:168

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:129

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:726

[virtual.h](virtual_8h.md)

Virtual Network Interface.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [virtual\_mgmt.h](virtual__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
