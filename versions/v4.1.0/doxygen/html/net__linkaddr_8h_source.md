---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__linkaddr_8h_source.html
original_path: doxygen/html/net__linkaddr_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_linkaddr.h

[Go to the documentation of this file.](net__linkaddr_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_LINKADDR\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_NET\_LINKADDR\_H\_

14

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16#include <[stdbool.h](stdbool_8h.md)>

17#include <[errno.h](errno_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

31

33#ifdef CONFIG\_NET\_L2\_IEEE802154

34#define NET\_LINK\_ADDR\_MAX\_LENGTH 8

35#else

36#ifdef CONFIG\_NET\_L2\_PPP

37#define NET\_LINK\_ADDR\_MAX\_LENGTH 8

38#else

[ 39](group__net__linkaddr.md#ga5680cf2ac9302bbee824148f36193b2b)#define NET\_LINK\_ADDR\_MAX\_LENGTH 6

40#endif

41#endif

42

[ 49](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24)enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) {

[ 51](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34) [NET\_LINK\_UNKNOWN](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34) = 0,

[ 53](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3) [NET\_LINK\_IEEE802154](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3),

[ 55](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a) [NET\_LINK\_BLUETOOTH](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a),

[ 57](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b) [NET\_LINK\_ETHERNET](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b),

[ 59](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8) [NET\_LINK\_DUMMY](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8),

[ 61](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a) [NET\_LINK\_CANBUS\_RAW](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a),

62} \_\_packed;

63

[ 69](structnet__linkaddr.md)struct [net\_linkaddr](structnet__linkaddr.md) {

[ 71](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0); /\* in big endian \*/

72

[ 74](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0);

75

[ 77](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

78};

79

[ 90](structnet__linkaddr__storage.md)struct [net\_linkaddr\_storage](structnet__linkaddr__storage.md) {

[ 92](structnet__linkaddr__storage.md#a00ae00d99b6022663e0f5a3894704ca8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structnet__linkaddr__storage.md#a00ae00d99b6022663e0f5a3894704ca8);

93

[ 95](structnet__linkaddr__storage.md#ab1d9024ef8574f6e7daaa19ee5266a11) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__linkaddr__storage.md#ab1d9024ef8574f6e7daaa19ee5266a11);

96

[ 98](structnet__linkaddr__storage.md#ae37b0b74f3d2b7ec09e2c2022e86c0bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structnet__linkaddr__storage.md#ae37b0b74f3d2b7ec09e2c2022e86c0bb)[[NET\_LINK\_ADDR\_MAX\_LENGTH](group__net__linkaddr.md#ga5680cf2ac9302bbee824148f36193b2b)]; /\* in big endian \*/

99};

100

[ 109](group__net__linkaddr.md#ga36387353825a70fbe54dd16d076a9e26)static inline bool [net\_linkaddr\_cmp](group__net__linkaddr.md#ga36387353825a70fbe54dd16d076a9e26)(struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr1,

110 struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr2)

111{

112 if (!lladdr1 || !lladdr2) {

113 return false;

114 }

115

116 if (lladdr1->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) != lladdr2->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)) {

117 return false;

118 }

119

120 return ![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(lladdr1->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0), lladdr2->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0), lladdr1->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0));

121}

122

[ 132](group__net__linkaddr.md#gaa20d6cb50b240f9306ea88b1dc4c1de4)static inline int [net\_linkaddr\_set](group__net__linkaddr.md#gaa20d6cb50b240f9306ea88b1dc4c1de4)(struct [net\_linkaddr\_storage](structnet__linkaddr__storage.md) \*lladdr\_store,

133 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*new\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_len)

134{

135 if (!lladdr\_store || !new\_addr) {

136 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

137 }

138

139 if (new\_len > [NET\_LINK\_ADDR\_MAX\_LENGTH](group__net__linkaddr.md#ga5680cf2ac9302bbee824148f36193b2b)) {

140 return -[EMSGSIZE](group__system__errno.md#gae37becfaa095a9df5c5c788bce5aa06f);

141 }

142

143 lladdr\_store->[len](structnet__linkaddr__storage.md#ab1d9024ef8574f6e7daaa19ee5266a11) = new\_len;

144 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(lladdr\_store->[addr](structnet__linkaddr__storage.md#ae37b0b74f3d2b7ec09e2c2022e86c0bb), new\_addr, new\_len);

145

146 return 0;

147}

148

152

153#ifdef \_\_cplusplus

154}

155#endif

156

157#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_LINKADDR\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24)

net\_link\_type

Type of the link address.

**Definition** net\_linkaddr.h:49

[net\_linkaddr\_cmp](group__net__linkaddr.md#ga36387353825a70fbe54dd16d076a9e26)

static bool net\_linkaddr\_cmp(struct net\_linkaddr \*lladdr1, struct net\_linkaddr \*lladdr2)

Compare two link layer addresses.

**Definition** net\_linkaddr.h:109

[NET\_LINK\_ADDR\_MAX\_LENGTH](group__net__linkaddr.md#ga5680cf2ac9302bbee824148f36193b2b)

#define NET\_LINK\_ADDR\_MAX\_LENGTH

Maximum length of the link address.

**Definition** net\_linkaddr.h:39

[net\_linkaddr\_set](group__net__linkaddr.md#gaa20d6cb50b240f9306ea88b1dc4c1de4)

static int net\_linkaddr\_set(struct net\_linkaddr\_storage \*lladdr\_store, uint8\_t \*new\_addr, uint8\_t new\_len)

Set the member data of a link layer address storage structure.

**Definition** net\_linkaddr.h:132

[NET\_LINK\_UNKNOWN](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34)

@ NET\_LINK\_UNKNOWN

Unknown link address type.

**Definition** net\_linkaddr.h:51

[NET\_LINK\_IEEE802154](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3)

@ NET\_LINK\_IEEE802154

IEEE 802.15.4 link address.

**Definition** net\_linkaddr.h:53

[NET\_LINK\_DUMMY](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8)

@ NET\_LINK\_DUMMY

Dummy link address.

**Definition** net\_linkaddr.h:59

[NET\_LINK\_ETHERNET](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)

@ NET\_LINK\_ETHERNET

Ethernet link address.

**Definition** net\_linkaddr.h:57

[NET\_LINK\_CANBUS\_RAW](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a)

@ NET\_LINK\_CANBUS\_RAW

CANBUS link address.

**Definition** net\_linkaddr.h:61

[NET\_LINK\_BLUETOOTH](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a)

@ NET\_LINK\_BLUETOOTH

Bluetooth IPSP link address.

**Definition** net\_linkaddr.h:55

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[EMSGSIZE](group__system__errno.md#gae37becfaa095a9df5c5c788bce5aa06f)

#define EMSGSIZE

Message size.

**Definition** errno.h:106

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)

int memcmp(const void \*m1, const void \*m2, size\_t n)

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[net\_linkaddr\_storage](structnet__linkaddr__storage.md)

Hardware link address structure.

**Definition** net\_linkaddr.h:90

[net\_linkaddr\_storage::type](structnet__linkaddr__storage.md#a00ae00d99b6022663e0f5a3894704ca8)

uint8\_t type

What kind of address is this for.

**Definition** net\_linkaddr.h:92

[net\_linkaddr\_storage::len](structnet__linkaddr__storage.md#ab1d9024ef8574f6e7daaa19ee5266a11)

uint8\_t len

The real length of the ll address.

**Definition** net\_linkaddr.h:95

[net\_linkaddr\_storage::addr](structnet__linkaddr__storage.md#ae37b0b74f3d2b7ec09e2c2022e86c0bb)

uint8\_t addr[6]

The array of bytes representing the address.

**Definition** net\_linkaddr.h:98

[net\_linkaddr](structnet__linkaddr.md)

Hardware link address structure.

**Definition** net\_linkaddr.h:69

[net\_linkaddr::addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)

uint8\_t \* addr

The array of byte representing the address.

**Definition** net\_linkaddr.h:71

[net\_linkaddr::type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7)

uint8\_t type

What kind of address is this for.

**Definition** net\_linkaddr.h:77

[net\_linkaddr::len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)

uint8\_t len

Length of that address array.

**Definition** net\_linkaddr.h:74

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_linkaddr.h](net__linkaddr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
