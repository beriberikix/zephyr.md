---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/net__linkaddr_8h_source.html
original_path: doxygen/html/net__linkaddr_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

33#if defined(CONFIG\_NET\_L2\_PHY\_IEEE802154) || defined(CONFIG\_NET\_L2\_PPP)

34#define NET\_LINK\_ADDR\_MAX\_LENGTH 8

35#else

[ 36](group__net__linkaddr.md#ga5680cf2ac9302bbee824148f36193b2b)#define NET\_LINK\_ADDR\_MAX\_LENGTH 6

37#endif

38

[ 45](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24)enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) {

[ 47](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34) [NET\_LINK\_UNKNOWN](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34) = 0,

[ 49](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3) [NET\_LINK\_IEEE802154](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3),

[ 51](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a) [NET\_LINK\_BLUETOOTH](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a),

[ 53](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b) [NET\_LINK\_ETHERNET](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b),

[ 55](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8) [NET\_LINK\_DUMMY](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8),

[ 57](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a) [NET\_LINK\_CANBUS\_RAW](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a),

58} \_\_packed;

59

[ 70](structnet__linkaddr.md)struct [net\_linkaddr](structnet__linkaddr.md) {

[ 72](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

73

[ 75](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0);

76

[ 78](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881)[[NET\_LINK\_ADDR\_MAX\_LENGTH](group__net__linkaddr.md#ga5680cf2ac9302bbee824148f36193b2b)]; /\* in big endian \*/

79};

80

[ 89](group__net__linkaddr.md#ga36387353825a70fbe54dd16d076a9e26)static inline bool [net\_linkaddr\_cmp](group__net__linkaddr.md#ga36387353825a70fbe54dd16d076a9e26)(struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr1,

90 struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr2)

91{

92 if (!lladdr1 || !lladdr2) {

93 return false;

94 }

95

96 if (lladdr1->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) != lladdr2->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)) {

97 return false;

98 }

99

100 return ![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(lladdr1->[addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881), lladdr2->[addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881), lladdr1->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0));

101}

102

[ 113](group__net__linkaddr.md#gab0c451240b31d61749b724eaa6d61d45)static inline int [net\_linkaddr\_set](group__net__linkaddr.md#gab0c451240b31d61749b724eaa6d61d45)(struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr,

114 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*new\_addr,

115 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_len)

116{

117 if (lladdr == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || new\_addr == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

118 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

119 }

120

121 if (new\_len > [NET\_LINK\_ADDR\_MAX\_LENGTH](group__net__linkaddr.md#ga5680cf2ac9302bbee824148f36193b2b)) {

122 return -[EMSGSIZE](group__system__errno.md#gae37becfaa095a9df5c5c788bce5aa06f);

123 }

124

125 lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) = new\_len;

126 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(lladdr->[addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881), new\_addr, new\_len);

127

128 return 0;

129}

130

[ 138](group__net__linkaddr.md#ga1230eb353dd8f6671bf8ed31c464b712)static inline int [net\_linkaddr\_copy](group__net__linkaddr.md#ga1230eb353dd8f6671bf8ed31c464b712)(struct [net\_linkaddr](structnet__linkaddr.md) \*dst,

139 const struct [net\_linkaddr](structnet__linkaddr.md) \*src)

140{

141 if (dst == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || src == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

142 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

143 }

144

145 if (src->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) > [NET\_LINK\_ADDR\_MAX\_LENGTH](group__net__linkaddr.md#ga5680cf2ac9302bbee824148f36193b2b)) {

146 return -[EMSGSIZE](group__system__errno.md#gae37becfaa095a9df5c5c788bce5aa06f);

147 }

148

149 dst->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) = src->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

150 dst->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) = src->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0);

151 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(dst->[addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881), src->[addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881), src->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0));

152

153 return 0;

154}

155

[ 166](group__net__linkaddr.md#gae8a73ee528b82ae36357bd066dc8128b)static inline int [net\_linkaddr\_create](group__net__linkaddr.md#gae8a73ee528b82ae36357bd066dc8128b)(struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr,

167 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

168 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type)

169{

170 if (lladdr == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

171 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

172 }

173

174 if (len > [NET\_LINK\_ADDR\_MAX\_LENGTH](group__net__linkaddr.md#ga5680cf2ac9302bbee824148f36193b2b)) {

175 return -[EMSGSIZE](group__system__errno.md#gae37becfaa095a9df5c5c788bce5aa06f);

176 }

177

178 if (addr == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

179 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(lladdr->[addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881), 0, [NET\_LINK\_ADDR\_MAX\_LENGTH](group__net__linkaddr.md#ga5680cf2ac9302bbee824148f36193b2b));

180 } else {

181 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(lladdr->[addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881), addr, len);

182 }

183

184 lladdr->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) = type;

185 lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) = len;

186

187 return 0;

188}

189

[ 196](group__net__linkaddr.md#ga4061ecaf3b1c4c06968ef6a744de0185)static inline int [net\_linkaddr\_clear](group__net__linkaddr.md#ga4061ecaf3b1c4c06968ef6a744de0185)(struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr)

197{

198 return [net\_linkaddr\_create](group__net__linkaddr.md#gae8a73ee528b82ae36357bd066dc8128b)(lladdr, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), 0, [NET\_LINK\_UNKNOWN](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34));

199}

200

204

205#ifdef \_\_cplusplus

206}

207#endif

208

209#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_LINKADDR\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[net\_linkaddr\_copy](group__net__linkaddr.md#ga1230eb353dd8f6671bf8ed31c464b712)

static int net\_linkaddr\_copy(struct net\_linkaddr \*dst, const struct net\_linkaddr \*src)

Copy link address from one variable to another.

**Definition** net\_linkaddr.h:138

[net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24)

net\_link\_type

Type of the link address.

**Definition** net\_linkaddr.h:45

[net\_linkaddr\_cmp](group__net__linkaddr.md#ga36387353825a70fbe54dd16d076a9e26)

static bool net\_linkaddr\_cmp(struct net\_linkaddr \*lladdr1, struct net\_linkaddr \*lladdr2)

Compare two link layer addresses.

**Definition** net\_linkaddr.h:89

[net\_linkaddr\_clear](group__net__linkaddr.md#ga4061ecaf3b1c4c06968ef6a744de0185)

static int net\_linkaddr\_clear(struct net\_linkaddr \*lladdr)

Clear link address.

**Definition** net\_linkaddr.h:196

[NET\_LINK\_ADDR\_MAX\_LENGTH](group__net__linkaddr.md#ga5680cf2ac9302bbee824148f36193b2b)

#define NET\_LINK\_ADDR\_MAX\_LENGTH

Maximum length of the link address.

**Definition** net\_linkaddr.h:36

[net\_linkaddr\_set](group__net__linkaddr.md#gab0c451240b31d61749b724eaa6d61d45)

static int net\_linkaddr\_set(struct net\_linkaddr \*lladdr, const uint8\_t \*new\_addr, uint8\_t new\_len)

Set the member data of a link layer address storage structure.

**Definition** net\_linkaddr.h:113

[net\_linkaddr\_create](group__net__linkaddr.md#gae8a73ee528b82ae36357bd066dc8128b)

static int net\_linkaddr\_create(struct net\_linkaddr \*lladdr, const uint8\_t \*addr, uint8\_t len, enum net\_link\_type type)

Create a link address structure.

**Definition** net\_linkaddr.h:166

[NET\_LINK\_UNKNOWN](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34)

@ NET\_LINK\_UNKNOWN

Unknown link address type.

**Definition** net\_linkaddr.h:47

[NET\_LINK\_IEEE802154](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3)

@ NET\_LINK\_IEEE802154

IEEE 802.15.4 link address.

**Definition** net\_linkaddr.h:49

[NET\_LINK\_DUMMY](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8)

@ NET\_LINK\_DUMMY

Dummy link address.

**Definition** net\_linkaddr.h:55

[NET\_LINK\_ETHERNET](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)

@ NET\_LINK\_ETHERNET

Ethernet link address.

**Definition** net\_linkaddr.h:53

[NET\_LINK\_CANBUS\_RAW](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a)

@ NET\_LINK\_CANBUS\_RAW

CANBUS link address.

**Definition** net\_linkaddr.h:57

[NET\_LINK\_BLUETOOTH](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a)

@ NET\_LINK\_BLUETOOTH

Bluetooth IPSP link address.

**Definition** net\_linkaddr.h:51

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[EMSGSIZE](group__system__errno.md#gae37becfaa095a9df5c5c788bce5aa06f)

#define EMSGSIZE

Message size.

**Definition** errno.h:106

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)

void \* memset(void \*buf, int c, size\_t n)

[memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)

int memcmp(const void \*m1, const void \*m2, size\_t n)

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[net\_linkaddr](structnet__linkaddr.md)

Hardware link address structure.

**Definition** net\_linkaddr.h:70

[net\_linkaddr::addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881)

uint8\_t addr[6]

The array of bytes representing the address.

**Definition** net\_linkaddr.h:78

[net\_linkaddr::type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7)

uint8\_t type

What kind of address is this for.

**Definition** net\_linkaddr.h:72

[net\_linkaddr::len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)

uint8\_t len

The real length of the ll address.

**Definition** net\_linkaddr.h:75

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_linkaddr.h](net__linkaddr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
