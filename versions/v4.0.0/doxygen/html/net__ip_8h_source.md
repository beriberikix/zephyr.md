---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__ip_8h_source.html
original_path: doxygen/html/net__ip_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_ip.h

[Go to the documentation of this file.](net__ip_8h.md)

1

6

7/\*

8 \* Copyright (c) 2016 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_IP\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_NET\_IP\_H\_

15

24

25#include <[string.h](string_8h.md)>

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <[stdbool.h](stdbool_8h.md)>

28#include <[zephyr/sys/util.h](sys_2util_8h.md)>

29#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

30#include <[zephyr/toolchain.h](toolchain_8h.md)>

31

32#include <[zephyr/net/net\_linkaddr.h](net__linkaddr_8h.md)>

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

39/\* Specifying VLAN tag here in order to avoid circular dependencies \*/

40#define NET\_VLAN\_TAG\_UNSPEC 0x0fff

42

43/\* Protocol families. \*/

[ 44](group__ip__4__6.md#ga51dba11ffc8e3b1bf695e721b3144094)#define PF\_UNSPEC 0

[ 45](group__ip__4__6.md#ga3f5da0b5be27fe31ec7cc11bfa8d1a25)#define PF\_INET 1

[ 46](group__ip__4__6.md#ga323f2649198fc7e64b19881869265618)#define PF\_INET6 2

[ 47](group__ip__4__6.md#ga8e297adb5fe2e28b0d9d921a5d56a8e9)#define PF\_PACKET 3

[ 48](group__ip__4__6.md#gaeac0c3db7a1e021f17987bcc76893849)#define PF\_CAN 4

[ 49](group__ip__4__6.md#ga288b09307bcc46aef2acf2af5e3e1006)#define PF\_NET\_MGMT 5

[ 50](group__ip__4__6.md#ga521c315ca2a2a4e6345878e84af4085e)#define PF\_LOCAL 6

[ 51](group__ip__4__6.md#ga0407288f5fb975a03b21d5287c282b2e)#define PF\_UNIX PF\_LOCAL

52

53/\* Address families. \*/

[ 54](group__ip__4__6.md#gae77ae24b14b7b7f294f3e04121173f12)#define AF\_UNSPEC PF\_UNSPEC

[ 55](group__ip__4__6.md#ga9930604d0e32588eae76f43ca38e7826)#define AF\_INET PF\_INET

[ 56](group__ip__4__6.md#gaa03706b2738b9a58d4985dfbe99e1bac)#define AF\_INET6 PF\_INET6

[ 57](group__ip__4__6.md#gaa89aa4cd481fe17260c3f5d493cc23f5)#define AF\_PACKET PF\_PACKET

[ 58](group__ip__4__6.md#ga546620c7e758f003b24b7fdae4f97bd4)#define AF\_CAN PF\_CAN

[ 59](group__ip__4__6.md#ga41d0cbb55cd9550a7f732b1520119c15)#define AF\_NET\_MGMT PF\_NET\_MGMT

[ 60](group__ip__4__6.md#gae24f1f9ea44fcce3affcb2137f593dc1)#define AF\_LOCAL PF\_LOCAL

[ 61](group__ip__4__6.md#ga0fd8739854bc8b48d65f0b669fed3ffe)#define AF\_UNIX PF\_UNIX

62

[ 64](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) {

[ 65](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a334b0a4a5a3e331e7c7864471e9eab08) [IPPROTO\_IP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a334b0a4a5a3e331e7c7864471e9eab08) = 0,

[ 66](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a7ccd735b73f6955ae2f4abf3e7ca6bb4) [IPPROTO\_ICMP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a7ccd735b73f6955ae2f4abf3e7ca6bb4) = 1,

[ 67](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4cbcb48be0cd8eb6fb5b5741f1c7b639) [IPPROTO\_IGMP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4cbcb48be0cd8eb6fb5b5741f1c7b639) = 2,

[ 68](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a49a42f6d628bf65e78478e8eb4874ff2) [IPPROTO\_IPIP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a49a42f6d628bf65e78478e8eb4874ff2) = 4,

[ 69](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4a3c433d15859f62bacc06312791a45e) [IPPROTO\_TCP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4a3c433d15859f62bacc06312791a45e) = 6,

[ 70](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31abd7dfb22e255a4eed332f41de12d7321) [IPPROTO\_UDP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31abd7dfb22e255a4eed332f41de12d7321) = 17,

[ 71](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a892549243e60ed1e04e88a14b44d8185) [IPPROTO\_IPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a892549243e60ed1e04e88a14b44d8185) = 41,

[ 72](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31aeeff57e3cf726718a92b2138e5842926) [IPPROTO\_ICMPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31aeeff57e3cf726718a92b2138e5842926) = 58,

[ 73](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a3f186705d5c21da1b72ecb91cca1f7a4) [IPPROTO\_RAW](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a3f186705d5c21da1b72ecb91cca1f7a4) = 255,

74};

75

[ 77](group__ip__4__6.md#ga721da18d2a3cfd9b3a56e9efc9f6e58b)enum [net\_ip\_protocol\_secure](group__ip__4__6.md#ga721da18d2a3cfd9b3a56e9efc9f6e58b) {

[ 78](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba6d479e64d940cea948c874d36c656fcc) [IPPROTO\_TLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba6d479e64d940cea948c874d36c656fcc) = 256,

[ 79](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba102692f9f57dd0ec6f8c6cb54a235d4c) [IPPROTO\_TLS\_1\_1](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba102692f9f57dd0ec6f8c6cb54a235d4c) = 257,

[ 80](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa5e176fa47ca23a6f25101a5203f8e5a) [IPPROTO\_TLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa5e176fa47ca23a6f25101a5203f8e5a) = 258,

[ 81](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa43bf0393de00897b350b361f97c85ac) [IPPROTO\_TLS\_1\_3](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa43bf0393de00897b350b361f97c85ac) = 259,

[ 82](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba92e94005d7a80aacbffad2f3f10555ef) [IPPROTO\_DTLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba92e94005d7a80aacbffad2f3f10555ef) = 272,

[ 83](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58bad4d2a6ca8756ee52221f19fb06c34a1c) [IPPROTO\_DTLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58bad4d2a6ca8756ee52221f19fb06c34a1c) = 273,

84};

85

[ 87](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c)enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) {

[ 88](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424) [SOCK\_STREAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424) = 1,

[ 89](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc) [SOCK\_DGRAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc),

[ 90](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231) [SOCK\_RAW](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231)

91};

92

[ 99](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)#define ntohs(x) sys\_be16\_to\_cpu(x)

100

[ 107](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)#define ntohl(x) sys\_be32\_to\_cpu(x)

108

[ 115](group__ip__4__6.md#ga3cfcf123d4ead264289232f91f2c9ca5)#define ntohll(x) sys\_be64\_to\_cpu(x)

116

[ 123](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)#define htons(x) sys\_cpu\_to\_be16(x)

124

[ 131](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)#define htonl(x) sys\_cpu\_to\_be32(x)

132

[ 139](group__ip__4__6.md#ga9f4bf0773c45ad9a9753a1b784a13fbb)#define htonll(x) sys\_cpu\_to\_be64(x)

140

[ 142](structin6__addr.md)struct [in6\_addr](structin6__addr.md) {

143 union {

[ 144](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[16];

[ 145](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[8];

[ 146](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[4];

147 };

148};

149

[ 151](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)#define NET\_IPV6\_ADDR\_SIZE 16

152

[ 154](structin__addr.md)struct [in\_addr](structin__addr.md) {

155 union {

[ 156](structin__addr.md#a4fd35e401c510fabab8979eb8416dd9b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [s4\_addr](structin__addr.md#a4fd35e401c510fabab8979eb8416dd9b)[4];

[ 157](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [s4\_addr16](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86)[2];

[ 158](structin__addr.md#ae4e092a27efb643067d7ce10bd454bed) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [s4\_addr32](structin__addr.md#ae4e092a27efb643067d7ce10bd454bed)[1];

[ 159](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5);

160 };

161};

162

[ 164](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)#define NET\_IPV4\_ADDR\_SIZE 4

165

[ 167](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)typedef unsigned short int [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda);

168

170#ifndef \_\_socklen\_t\_defined

[ 171](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)typedef size\_t [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a);

172#define \_\_socklen\_t\_defined

173#endif

174

175/\*

176 \* Note that the sin\_port and sin6\_port are in network byte order

177 \* in various sockaddr\* structs.

178 \*/

179

[ 181](structsockaddr__in6.md)struct [sockaddr\_in6](structsockaddr__in6.md) {

[ 182](structsockaddr__in6.md#aefa41e43be9c615f8cfd6266c0ed1687) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sin6\_family](structsockaddr__in6.md#aefa41e43be9c615f8cfd6266c0ed1687);

[ 183](structsockaddr__in6.md#a4fc2b7a478d258e9e778772701096022) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sin6\_port](structsockaddr__in6.md#a4fc2b7a478d258e9e778772701096022);

[ 184](structsockaddr__in6.md#a219e7f3ecd6d7dcf8fc2465475be490f) struct [in6\_addr](structin6__addr.md) [sin6\_addr](structsockaddr__in6.md#a219e7f3ecd6d7dcf8fc2465475be490f);

[ 185](structsockaddr__in6.md#a1daad78c9848862ab33a48e05fa8cf17) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sin6\_scope\_id](structsockaddr__in6.md#a1daad78c9848862ab33a48e05fa8cf17);

186};

187

[ 189](structsockaddr__in.md)struct [sockaddr\_in](structsockaddr__in.md) {

[ 190](structsockaddr__in.md#a9a7d98bb8e18f4a06a021c32d6cc7117) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sin\_family](structsockaddr__in.md#a9a7d98bb8e18f4a06a021c32d6cc7117);

[ 191](structsockaddr__in.md#a3cf9239fdd8bd32855d66a4b86349fbb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sin\_port](structsockaddr__in.md#a3cf9239fdd8bd32855d66a4b86349fbb);

[ 192](structsockaddr__in.md#a4ea5f2f1138e5c8597097db255a9ec6c) struct [in\_addr](structin__addr.md) [sin\_addr](structsockaddr__in.md#a4ea5f2f1138e5c8597097db255a9ec6c);

193};

194

[ 196](structsockaddr__ll.md)struct [sockaddr\_ll](structsockaddr__ll.md) {

[ 197](structsockaddr__ll.md#a4920e92fb0613ba8594a6b6c226048d9) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sll\_family](structsockaddr__ll.md#a4920e92fb0613ba8594a6b6c226048d9);

[ 198](structsockaddr__ll.md#a661e329c10a8f06a85ad831630273e49) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sll\_protocol](structsockaddr__ll.md#a661e329c10a8f06a85ad831630273e49);

[ 199](structsockaddr__ll.md#a93b4976ed8e9d58cdcc620f5d1987f68) int [sll\_ifindex](structsockaddr__ll.md#a93b4976ed8e9d58cdcc620f5d1987f68);

[ 200](structsockaddr__ll.md#a2df317106a30498dd9f87e1d4eefc8fc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sll\_hatype](structsockaddr__ll.md#a2df317106a30498dd9f87e1d4eefc8fc);

[ 201](structsockaddr__ll.md#a2001fcf2627149283e3460b18f44b313) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sll\_pkttype](structsockaddr__ll.md#a2001fcf2627149283e3460b18f44b313);

[ 202](structsockaddr__ll.md#acb72ab39a239d9e5752b7422dc9a2dc6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sll\_halen](structsockaddr__ll.md#acb72ab39a239d9e5752b7422dc9a2dc6);

[ 203](structsockaddr__ll.md#aee52affe8837ffe1c32c94ce34117d6a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sll\_addr](structsockaddr__ll.md#aee52affe8837ffe1c32c94ce34117d6a)[8];

204};

205

207

209struct sockaddr\_in6\_ptr {

210 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sin6\_family;

211 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sin6\_port;

212 struct [in6\_addr](structin6__addr.md) \*sin6\_addr;

213 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sin6\_scope\_id;

214};

215

217struct sockaddr\_in\_ptr {

218 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sin\_family;

219 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sin\_port;

220 struct in\_addr \*sin\_addr;

221};

222

224struct sockaddr\_ll\_ptr {

225 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sll\_family;

226 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sll\_protocol;

227 int sll\_ifindex;

228 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sll\_hatype;

229 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sll\_pkttype;

230 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sll\_halen;

231 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*sll\_addr;

232};

233

234struct sockaddr\_can\_ptr {

235 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) can\_family;

236 int can\_ifindex;

237};

238

240

241#if !defined(HAVE\_IOVEC)

[ 243](structiovec.md)struct [iovec](structiovec.md) {

[ 244](structiovec.md#a07aeddeccf80f14520fdd7ef0759442b) void \*[iov\_base](structiovec.md#a07aeddeccf80f14520fdd7ef0759442b);

[ 245](structiovec.md#a17b5ac2078fd1adfabb262a95808a07d) size\_t [iov\_len](structiovec.md#a17b5ac2078fd1adfabb262a95808a07d);

246};

247#endif

248

[ 250](structmsghdr.md)struct [msghdr](structmsghdr.md) {

[ 251](structmsghdr.md#a691a8866b21c7083974a2ff1e7987ce1) void \*[msg\_name](structmsghdr.md#a691a8866b21c7083974a2ff1e7987ce1);

[ 252](structmsghdr.md#a47762b69eee1c9ba5736d64516ea0960) [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) [msg\_namelen](structmsghdr.md#a47762b69eee1c9ba5736d64516ea0960);

[ 253](structmsghdr.md#a1b893a6f84c4ba52708c5dcfcc720293) struct [iovec](structiovec.md) \*[msg\_iov](structmsghdr.md#a1b893a6f84c4ba52708c5dcfcc720293);

[ 254](structmsghdr.md#ad4ef1bd6821e599bf42f936850d2c4d7) size\_t [msg\_iovlen](structmsghdr.md#ad4ef1bd6821e599bf42f936850d2c4d7);

[ 255](structmsghdr.md#afba5fc31b0f197e25602d2232ca6d783) void \*[msg\_control](structmsghdr.md#afba5fc31b0f197e25602d2232ca6d783);

[ 256](structmsghdr.md#a9fa41b0e9a02b5dc9a01aa6f18108adb) size\_t [msg\_controllen](structmsghdr.md#a9fa41b0e9a02b5dc9a01aa6f18108adb);

[ 257](structmsghdr.md#a9e8ff97d402c99551cbfd564e9e10a74) int [msg\_flags](structmsghdr.md#a9e8ff97d402c99551cbfd564e9e10a74);

258};

259

[ 261](structcmsghdr.md)struct [cmsghdr](structcmsghdr.md) {

[ 262](structcmsghdr.md#a7cf479e5e162e65ad164616453d61df2) [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) [cmsg\_len](structcmsghdr.md#a7cf479e5e162e65ad164616453d61df2);

[ 263](structcmsghdr.md#ac0ff1400cb63fbc2e0ece19434cb8fef) int [cmsg\_level](structcmsghdr.md#ac0ff1400cb63fbc2e0ece19434cb8fef);

[ 264](structcmsghdr.md#a4c7cabf7899a688ce10bc92773fca9c1) int [cmsg\_type](structcmsghdr.md#a4c7cabf7899a688ce10bc92773fca9c1);

[ 265](structcmsghdr.md#a92c00d02575707f72c04f090b6f8d399) z\_max\_align\_t [cmsg\_data](structcmsghdr.md#a92c00d02575707f72c04f090b6f8d399)[];

266};

267

269

270/\* Alignment for headers and data. These are arch specific but define

271 \* them here atm if not found already.

272 \*/

273#if !defined(ALIGN\_H)

274#define ALIGN\_H(x) ROUND\_UP(x, \_\_alignof\_\_(struct cmsghdr))

275#endif

276#if !defined(ALIGN\_D)

277#define ALIGN\_D(x) ROUND\_UP(x, \_\_alignof\_\_(z\_max\_align\_t))

278#endif

279

281

282#if !defined(CMSG\_FIRSTHDR)

[ 288](group__ip__4__6.md#ga39567a31d167fc53336d2ab4a2cd78a4)#define CMSG\_FIRSTHDR(msghdr) \

289 ((msghdr)->msg\_controllen >= sizeof(struct cmsghdr) ? \

290 (struct cmsghdr \*)((msghdr)->msg\_control) : NULL)

291#endif

292

293#if !defined(CMSG\_NXTHDR)

[ 298](group__ip__4__6.md#ga77c17efca635d597cb6e98b28172bdc0)#define CMSG\_NXTHDR(msghdr, cmsg) \

299 (((cmsg) == NULL) ? CMSG\_FIRSTHDR(msghdr) : \

300 (((uint8\_t \*)(cmsg) + ALIGN\_H((cmsg)->cmsg\_len) + \

301 ALIGN\_D(sizeof(struct cmsghdr)) > \

302 (uint8\_t \*)((msghdr)->msg\_control) + (msghdr)->msg\_controllen) ? \

303 NULL : \

304 (struct cmsghdr \*)((uint8\_t \*)(cmsg) + \

305 ALIGN\_H((cmsg)->cmsg\_len))))

306#endif

307

308#if !defined(CMSG\_DATA)

[ 316](group__ip__4__6.md#ga5ab6d56e410ac0904107e84aeb1484cc)#define CMSG\_DATA(cmsg) ((uint8\_t \*)(cmsg) + ALIGN\_D(sizeof(struct cmsghdr)))

317#endif

318

319#if !defined(CMSG\_SPACE)

[ 324](group__ip__4__6.md#ga8db11d639dd07c723256f3bb5bc89044)#define CMSG\_SPACE(length) (ALIGN\_D(sizeof(struct cmsghdr)) + ALIGN\_H(length))

325#endif

326

327#if !defined(CMSG\_LEN)

[ 333](group__ip__4__6.md#gadb36e4ff4fa9a0c6730321c4bfcf64bc)#define CMSG\_LEN(length) (ALIGN\_D(sizeof(struct cmsghdr)) + length)

334#endif

335

337

338/\* Packet types. \*/

339#define PACKET\_HOST 0 /\* To us \*/

340#define PACKET\_BROADCAST 1 /\* To all \*/

341#define PACKET\_MULTICAST 2 /\* To group \*/

342#define PACKET\_OTHERHOST 3 /\* To someone else \*/

343#define PACKET\_OUTGOING 4 /\* Originated by us \*/

344#define PACKET\_LOOPBACK 5

345#define PACKET\_FASTROUTE 6

346

347/\* ARP protocol HARDWARE identifiers. \*/

348#define ARPHRD\_ETHER 1

349

350/\* Note: These macros are defined in a specific order.

351 \* The largest sockaddr size is the last one.

352 \*/

353#if defined(CONFIG\_NET\_IPV4)

354#undef NET\_SOCKADDR\_MAX\_SIZE

355#undef NET\_SOCKADDR\_PTR\_MAX\_SIZE

356#define NET\_SOCKADDR\_MAX\_SIZE (sizeof(struct sockaddr\_in))

357#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_in\_ptr))

358#endif

359

360#if defined(CONFIG\_NET\_SOCKETS\_PACKET)

361#undef NET\_SOCKADDR\_MAX\_SIZE

362#undef NET\_SOCKADDR\_PTR\_MAX\_SIZE

363#define NET\_SOCKADDR\_MAX\_SIZE (sizeof(struct sockaddr\_ll))

364#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_ll\_ptr))

365#endif

366

367#if defined(CONFIG\_NET\_IPV6)

368#undef NET\_SOCKADDR\_MAX\_SIZE

369#define NET\_SOCKADDR\_MAX\_SIZE (sizeof(struct sockaddr\_in6))

370#if !defined(CONFIG\_NET\_SOCKETS\_PACKET)

371#undef NET\_SOCKADDR\_PTR\_MAX\_SIZE

372#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_in6\_ptr))

373#endif

374#endif

375

376#if !defined(CONFIG\_NET\_IPV4)

377#if !defined(CONFIG\_NET\_IPV6)

378#if !defined(CONFIG\_NET\_SOCKETS\_PACKET)

379#define NET\_SOCKADDR\_MAX\_SIZE (sizeof(struct sockaddr\_in6))

380#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_in6\_ptr))

381#endif

382#endif

383#endif

384

386

[ 388](structsockaddr.md)struct [sockaddr](structsockaddr.md) {

[ 389](structsockaddr.md#ac6ef02e9a2e90a30218132ffd7b5a5c5) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sa\_family](structsockaddr.md#ac6ef02e9a2e90a30218132ffd7b5a5c5);

391 char data[NET\_SOCKADDR\_MAX\_SIZE - sizeof([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda))];

393};

394

396

397struct sockaddr\_ptr {

398 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family;

399 char data[NET\_SOCKADDR\_PTR\_MAX\_SIZE - sizeof([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda))];

400};

401

402/\* Same as sockaddr in our case \*/

403struct sockaddr\_storage {

404 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) ss\_family;

405 char data[NET\_SOCKADDR\_MAX\_SIZE - sizeof([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda))];

406};

407

408/\* Socket address struct for UNIX domain sockets \*/

409struct sockaddr\_un {

410 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sun\_family; /\* AF\_UNIX \*/

411 char sun\_path[NET\_SOCKADDR\_MAX\_SIZE - sizeof([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda))];

412};

413

414struct net\_addr {

415 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family;

416 union {

417 struct in6\_addr in6\_addr;

418 struct in\_addr in\_addr;

419 };

420};

421

423extern const struct [in6\_addr](structin6__addr.md) in6addr\_any;

424

426extern const struct [in6\_addr](structin6__addr.md) in6addr\_loopback;

427

429

[ 431](group__ip__4__6.md#ga1de876a356ee05a2e9427b741f99f49c)#define IN6ADDR\_ANY\_INIT { { { 0, 0, 0, 0, 0, 0, 0, 0, 0, \

432 0, 0, 0, 0, 0, 0, 0 } } }

433

[ 435](group__ip__4__6.md#ga5562c81af19ee5988ddc5a5c6153cf37)#define IN6ADDR\_LOOPBACK\_INIT { { { 0, 0, 0, 0, 0, 0, 0, \

436 0, 0, 0, 0, 0, 0, 0, 0, 1 } } }

437

[ 439](group__ip__4__6.md#ga5d1940045dc2e7de552f3d4ff13a74ab)#define INADDR\_ANY 0

440

[ 442](group__ip__4__6.md#ga915fcf49ce8c1e235e64fc83b57ec5b1)#define INADDR\_ANY\_INIT { { { INADDR\_ANY } } }

443

[ 445](group__ip__4__6.md#ga554163cb2fa86ef4307dd1fff2aad2eb)#define INADDR\_LOOPBACK\_INIT { { { 127, 0, 0, 1 } } }

446

[ 448](group__ip__4__6.md#ga93b37007689284fd9c4bde1a8f4b9199)#define INET\_ADDRSTRLEN 16

[ 452](group__ip__4__6.md#gaf776b22a727aae7c9f4d869d50df47e8)#define INET6\_ADDRSTRLEN 46

453

455

456/\* These are for internal usage of the stack \*/

457#define NET\_IPV6\_ADDR\_LEN sizeof("xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx")

458#define NET\_IPV4\_ADDR\_LEN sizeof("xxx.xxx.xxx.xxx")

459

461

[ 463](group__ip__4__6.md#ga7a207761e4879c140f48f93978cb2f0b)enum [net\_ip\_mtu](group__ip__4__6.md#ga7a207761e4879c140f48f93978cb2f0b) {

467#if defined(CONFIG\_NET\_NATIVE\_IPV6)

468 [NET\_IPV6\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c) = CONFIG\_NET\_IPV6\_MTU,

469#else

[ 470](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c) [NET\_IPV6\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c) = 1280,

471#endif

472

[ 476](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1) [NET\_IPV4\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1) = 576,

477};

478

[ 480](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd)enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) {

[ 481](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b) [NET\_PRIORITY\_BK](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b) = 1,

[ 482](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce) [NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce) = 0,

[ 483](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0) [NET\_PRIORITY\_EE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0) = 2,

[ 484](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354) [NET\_PRIORITY\_CA](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354) = 3,

[ 485](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792) [NET\_PRIORITY\_VI](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792) = 4,

[ 486](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a) [NET\_PRIORITY\_VO](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a) = 5,

[ 487](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05) [NET\_PRIORITY\_IC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05) = 6,

[ 488](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef) [NET\_PRIORITY\_NC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef) = 7

489} \_\_packed;

490

[ 491](group__ip__4__6.md#ga5b32bdfc249437709bb25bd95ec7d6d7)#define NET\_MAX\_PRIORITIES 8

492

[ 494](structnet__tuple.md)struct [net\_tuple](structnet__tuple.md) {

[ 495](structnet__tuple.md#a8f9a1aab3c3aedeead795ca6624d4d6d) struct net\_addr \*[remote\_addr](structnet__tuple.md#a8f9a1aab3c3aedeead795ca6624d4d6d);

[ 496](structnet__tuple.md#af7004f8f8d74d49d6771393825612294) struct net\_addr \*[local\_addr](structnet__tuple.md#af7004f8f8d74d49d6771393825612294);

[ 497](structnet__tuple.md#ab4c31093a23bc60d8dcf5b784e3fb39a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [remote\_port](structnet__tuple.md#ab4c31093a23bc60d8dcf5b784e3fb39a);

[ 498](structnet__tuple.md#a9a1cd0dd55a9e866cb0e910120362b7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [local\_port](structnet__tuple.md#a9a1cd0dd55a9e866cb0e910120362b7e);

[ 499](structnet__tuple.md#aa9eeba2c8e263afbf6368e04353d6014) enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) [ip\_proto](structnet__tuple.md#aa9eeba2c8e263afbf6368e04353d6014);

500};

501

[ 503](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d)enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) {

[ 504](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df) [NET\_ADDR\_ANY\_STATE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df) = -1,

[ 505](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9) [NET\_ADDR\_TENTATIVE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9) = 0,

[ 506](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a) [NET\_ADDR\_PREFERRED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a),

[ 507](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3) [NET\_ADDR\_DEPRECATED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3),

508} \_\_packed;

509

[ 511](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41)enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) {

[ 513](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6) [NET\_ADDR\_ANY](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6) = 0,

[ 515](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006) [NET\_ADDR\_AUTOCONF](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006),

[ 517](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db) [NET\_ADDR\_DHCP](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db),

[ 519](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e) [NET\_ADDR\_MANUAL](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e),

[ 521](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4) [NET\_ADDR\_OVERRIDABLE](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4),

522} \_\_packed;

523

525

526struct net\_ipv6\_hdr {

527 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vtc;

528 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tcflow;

529 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) flow;

530 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len;

531 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nexthdr;

532 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit;

533 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[[NET\_IPV6\_ADDR\_SIZE](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)];

534 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[[NET\_IPV6\_ADDR\_SIZE](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)];

535} \_\_packed;

536

537struct net\_ipv6\_frag\_hdr {

538 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nexthdr;

539 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reserved;

540 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset;

541 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id;

542} \_\_packed;

543

544struct net\_ipv4\_hdr {

545 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vhl;

546 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tos;

547 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len;

548 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id[2];

549 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset[2];

550 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl;

551 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proto;

552 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chksum;

553 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[[NET\_IPV4\_ADDR\_SIZE](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)];

554 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[[NET\_IPV4\_ADDR\_SIZE](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)];

555} \_\_packed;

556

557struct net\_icmp\_hdr {

558 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type;

559 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code;

560 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chksum;

561} \_\_packed;

562

563struct net\_udp\_hdr {

564 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src\_port;

565 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst\_port;

566 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len;

567 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chksum;

568} \_\_packed;

569

570struct net\_tcp\_hdr {

571 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src\_port;

572 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst\_port;

573 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) seq[4];

574 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ack[4];

575 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset;

576 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

577 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wnd[2];

578 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chksum;

579 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) urg[2];

580 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) optdata[0];

581} \_\_packed;

582

583static inline const char \*net\_addr\_type2str(enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) type)

584{

585 switch (type) {

586 case [NET\_ADDR\_AUTOCONF](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006):

587 return "AUTO";

588 case [NET\_ADDR\_DHCP](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db):

589 return "DHCP";

590 case [NET\_ADDR\_MANUAL](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e):

591 return "MANUAL";

592 case [NET\_ADDR\_OVERRIDABLE](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4):

593 return "OVERRIDE";

594 case [NET\_ADDR\_ANY](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6):

595 default:

596 break;

597 }

598

599 return "<unknown>";

600}

601

602/\* IPv6 extension headers types \*/

603#define NET\_IPV6\_NEXTHDR\_HBHO 0

604#define NET\_IPV6\_NEXTHDR\_DESTO 60

605#define NET\_IPV6\_NEXTHDR\_ROUTING 43

606#define NET\_IPV6\_NEXTHDR\_FRAG 44

607#define NET\_IPV6\_NEXTHDR\_NONE 59

608

613union net\_ip\_header {

614 struct net\_ipv4\_hdr \*ipv4;

615 struct net\_ipv6\_hdr \*ipv6;

616};

617

618union net\_proto\_header {

619 struct net\_udp\_hdr \*udp;

620 struct net\_tcp\_hdr \*tcp;

621};

622

623#define NET\_UDPH\_LEN 8 /\* Size of UDP header \*/

624#define NET\_TCPH\_LEN 20 /\* Size of TCP header \*/

625#define NET\_ICMPH\_LEN 4 /\* Size of ICMP header \*/

626

627#define NET\_IPV6H\_LEN 40 /\* Size of IPv6 header \*/

628#define NET\_ICMPV6H\_LEN NET\_ICMPH\_LEN /\* Size of ICMPv6 header \*/

629#define NET\_IPV6UDPH\_LEN (NET\_UDPH\_LEN + NET\_IPV6H\_LEN) /\* IPv6 + UDP \*/

630#define NET\_IPV6TCPH\_LEN (NET\_TCPH\_LEN + NET\_IPV6H\_LEN) /\* IPv6 + TCP \*/

631#define NET\_IPV6ICMPH\_LEN (NET\_IPV6H\_LEN + NET\_ICMPH\_LEN) /\* ICMPv6 + IPv6 \*/

632#define NET\_IPV6\_FRAGH\_LEN 8

633

634#define NET\_IPV4H\_LEN 20 /\* Size of IPv4 header \*/

635#define NET\_ICMPV4H\_LEN NET\_ICMPH\_LEN /\* Size of ICMPv4 header \*/

636#define NET\_IPV4UDPH\_LEN (NET\_UDPH\_LEN + NET\_IPV4H\_LEN) /\* IPv4 + UDP \*/

637#define NET\_IPV4TCPH\_LEN (NET\_TCPH\_LEN + NET\_IPV4H\_LEN) /\* IPv4 + TCP \*/

638#define NET\_IPV4ICMPH\_LEN (NET\_IPV4H\_LEN + NET\_ICMPH\_LEN) /\* ICMPv4 + IPv4 \*/

639

640#define NET\_IPV6H\_LENGTH\_OFFSET 0x04 /\* Offset of the Length field in the IPv6 header \*/

641

642#define NET\_IPV6\_FRAGH\_OFFSET\_MASK 0xfff8 /\* Mask for the 13-bit Fragment Offset field \*/

643#define NET\_IPV4\_FRAGH\_OFFSET\_MASK 0x1fff /\* Mask for the 13-bit Fragment Offset field \*/

644#define NET\_IPV4\_MORE\_FRAG\_MASK 0x2000 /\* Mask for the 1-bit More Fragments field \*/

645#define NET\_IPV4\_DO\_NOT\_FRAG\_MASK 0x4000 /\* Mask for the 1-bit Do Not Fragment field \*/

646

648

[ 656](group__ip__4__6.md#gaa662667005bdc00bf1eb5cf243aad874)static inline bool [net\_ipv6\_is\_addr\_loopback](group__ip__4__6.md#gaa662667005bdc00bf1eb5cf243aad874)(struct [in6\_addr](structin6__addr.md) \*addr)

657{

658 return UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]) == 0 &&

659 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == 0 &&

660 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]) == 0 &&

661 [ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3])) == 1;

662}

663

[ 671](group__ip__4__6.md#ga1a2fb0427eeab1a5dec6d69208ad7f02)static inline bool [net\_ipv6\_is\_addr\_mcast](group__ip__4__6.md#ga1a2fb0427eeab1a5dec6d69208ad7f02)(const struct [in6\_addr](structin6__addr.md) \*addr)

672{

673 return addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xFF;

674}

675

676struct [net\_if](structnet__if.md);

677struct [net\_if\_config](structnet__if__config.md);

678

[ 679](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb)extern struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_lookup](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb)(const struct [in6\_addr](structin6__addr.md) \*addr,

680 struct [net\_if](structnet__if.md) \*\*iface);

681

[ 689](group__ip__4__6.md#ga00853528daf79c947dcdc320035ed538)static inline bool [net\_ipv6\_is\_my\_addr](group__ip__4__6.md#ga00853528daf79c947dcdc320035ed538)(struct [in6\_addr](structin6__addr.md) \*addr)

690{

691 return [net\_if\_ipv6\_addr\_lookup](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb)(addr, NULL) != NULL;

692}

693

[ 694](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975)extern struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv6\_maddr\_lookup](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975)(

695 const struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface);

696

[ 705](group__ip__4__6.md#gaf8c5158de9a65d840faa61bb3dec341c)static inline bool [net\_ipv6\_is\_my\_maddr](group__ip__4__6.md#gaf8c5158de9a65d840faa61bb3dec341c)(struct [in6\_addr](structin6__addr.md) \*maddr)

706{

707 return [net\_if\_ipv6\_maddr\_lookup](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975)(maddr, NULL) != NULL;

708}

709

[ 719](group__ip__4__6.md#ga9654007b0a3c4d033df1ec3d00bd26ee)static inline bool [net\_ipv6\_is\_prefix](group__ip__4__6.md#ga9654007b0a3c4d033df1ec3d00bd26ee)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1,

720 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2,

721 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) length)

722{

723 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bits = 128 - length;

724 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bytes = length / 8U;

725 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) remain = bits % 8;

726 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask;

727

728 if (length > 128) {

729 return false;

730 }

731

732 if ([memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(addr1, addr2, bytes)) {

733 return false;

734 }

735

736 if (!remain) {

737 /\* No remaining bits, the prefixes are the same as first

738 \* bytes are the same.

739 \*/

740 return true;

741 }

742

743 /\* Create a mask that has remaining most significant bits set \*/

744 mask = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))((0xff << (8 - remain)) ^ 0xff) << remain;

745

746 return (addr1[bytes] & mask) == (addr2[bytes] & mask);

747}

748

749

[ 757](group__ip__4__6.md#ga4e91a4298604a916731bf591acc7b326)static inline void [net\_ipv6\_addr\_prefix\_mask](group__ip__4__6.md#ga4e91a4298604a916731bf591acc7b326)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*inaddr,

758 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*outaddr,

759 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prefix\_len)

760{

761 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bits = 128 - prefix\_len;

762 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bytes = prefix\_len / 8U;

763 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) remain = bits % 8;

764 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask;

765

766 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(outaddr, 0, 16U);

767 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(outaddr, inaddr, bytes);

768

769 if (!remain) {

770 /\* No remaining bits, the prefixes are the same as first

771 \* bytes are the same.

772 \*/

773 return;

774 }

775

776 /\* Create a mask that has remaining most significant bits set \*/

777 mask = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))((0xff << (8 - remain)) ^ 0xff) << remain;

778 outaddr[bytes] = inaddr[bytes] & mask;

779}

780

[ 788](group__ip__4__6.md#ga879e4aed725d7ea3fe609fa989f14735)static inline bool [net\_ipv4\_is\_addr\_loopback](group__ip__4__6.md#ga879e4aed725d7ea3fe609fa989f14735)(struct [in\_addr](structin__addr.md) \*addr)

789{

790 return addr->[s4\_addr](structin__addr.md#a4fd35e401c510fabab8979eb8416dd9b)[0] == 127U;

791}

792

[ 800](group__ip__4__6.md#gadc623ecacf024733ab6d477d87cc4b9d)static inline bool [net\_ipv4\_is\_addr\_unspecified](group__ip__4__6.md#gadc623ecacf024733ab6d477d87cc4b9d)(const struct [in\_addr](structin__addr.md) \*addr)

801{

802 return UNALIGNED\_GET(&addr->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5)) == 0;

803}

804

[ 812](group__ip__4__6.md#gae8c3302cf9ca457de32eabcf65975b70)static inline bool [net\_ipv4\_is\_addr\_mcast](group__ip__4__6.md#gae8c3302cf9ca457de32eabcf65975b70)(const struct [in\_addr](structin__addr.md) \*addr)

813{

814 return ([ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5))) & 0xF0000000) == 0xE0000000;

815}

816

[ 824](group__ip__4__6.md#gac000a319de7a6f95d4a63719bca3b865)static inline bool [net\_ipv4\_is\_ll\_addr](group__ip__4__6.md#gac000a319de7a6f95d4a63719bca3b865)(const struct [in\_addr](structin__addr.md) \*addr)

825{

826 return ([ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5))) & 0xFFFF0000) == 0xA9FE0000;

827}

828

[ 838](group__ip__4__6.md#ga6f19cb74de130d70668599c05a5ed66b)static inline bool [net\_ipv4\_is\_private\_addr](group__ip__4__6.md#ga6f19cb74de130d70668599c05a5ed66b)(const struct [in\_addr](structin__addr.md) \*addr)

839{

840 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) masked\_24, masked\_16, masked\_12, masked\_10, masked\_8;

841

842 masked\_24 = [ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5))) & 0xFFFFFF00;

843 masked\_16 = masked\_24 & 0xFFFF0000;

844 masked\_12 = masked\_24 & 0xFFF00000;

845 masked\_10 = masked\_24 & 0xFFC00000;

846 masked\_8 = masked\_24 & 0xFF000000;

847

848 return masked\_8 == 0x0A000000 || /\* 10.0.0.0/8 \*/

849 masked\_10 == 0x64400000 || /\* 100.64.0.0/10 \*/

850 masked\_12 == 0xAC100000 || /\* 172.16.0.0/12 \*/

851 masked\_16 == 0xC0A80000 || /\* 192.168.0.0/16 \*/

852 masked\_24 == 0xC0000200 || /\* 192.0.2.0/24 \*/

853 masked\_24 == 0xC0336400 || /\* 192.51.100.0/24 \*/

854 masked\_24 == 0xCB007100; /\* 203.0.113.0/24 \*/

855}

856

[ 865](group__ip__4__6.md#ga75ffcc08e621c2d47d1ae043fce2acad)#define net\_ipaddr\_copy(dest, src) \

866 UNALIGNED\_PUT(UNALIGNED\_GET(src), dest)

867

[ 874](group__ip__4__6.md#gaf731738fb1761208739976d767736f87)static inline void [net\_ipv4\_addr\_copy\_raw](group__ip__4__6.md#gaf731738fb1761208739976d767736f87)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dest,

875 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src)

876{

877 [net\_ipaddr\_copy](group__ip__4__6.md#ga75ffcc08e621c2d47d1ae043fce2acad)((struct [in\_addr](structin__addr.md) \*)dest, (const struct [in\_addr](structin__addr.md) \*)src);

878}

879

[ 886](group__ip__4__6.md#ga4925e6f3734b8fc1d9cb1ca1a510b5f1)static inline void [net\_ipv6\_addr\_copy\_raw](group__ip__4__6.md#ga4925e6f3734b8fc1d9cb1ca1a510b5f1)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dest,

887 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src)

888{

889 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(dest, src, sizeof(struct [in6\_addr](structin6__addr.md)));

890}

891

[ 900](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)static inline bool [net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)(const struct [in\_addr](structin__addr.md) \*addr1,

901 const struct [in\_addr](structin__addr.md) \*addr2)

902{

903 return UNALIGNED\_GET(&addr1->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5)) == UNALIGNED\_GET(&addr2->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5));

904}

905

[ 914](group__ip__4__6.md#ga32ffb42c62169ac9b34a0faa7c7ffd12)static inline bool [net\_ipv4\_addr\_cmp\_raw](group__ip__4__6.md#ga32ffb42c62169ac9b34a0faa7c7ffd12)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1,

915 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2)

916{

917 return [net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)((const struct [in\_addr](structin__addr.md) \*)addr1,

918 (const struct [in\_addr](structin__addr.md) \*)addr2);

919}

920

[ 929](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)static inline bool [net\_ipv6\_addr\_cmp](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)(const struct [in6\_addr](structin6__addr.md) \*addr1,

930 const struct [in6\_addr](structin6__addr.md) \*addr2)

931{

932 return ![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(addr1, addr2, sizeof(struct [in6\_addr](structin6__addr.md)));

933}

934

[ 943](group__ip__4__6.md#gafbe40461a645cf11fc8b3a07e1d9156e)static inline bool [net\_ipv6\_addr\_cmp\_raw](group__ip__4__6.md#gafbe40461a645cf11fc8b3a07e1d9156e)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1,

944 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2)

945{

946 return [net\_ipv6\_addr\_cmp](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)((const struct [in6\_addr](structin6__addr.md) \*)addr1,

947 (const struct [in6\_addr](structin6__addr.md) \*)addr2);

948}

949

[ 957](group__ip__4__6.md#gacac4279ee8896ddf2a76c612b36edf38)static inline bool [net\_ipv6\_is\_ll\_addr](group__ip__4__6.md#gacac4279ee8896ddf2a76c612b36edf38)(const struct [in6\_addr](structin6__addr.md) \*addr)

958{

959 return UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[0]) == [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(0xFE80);

960}

961

[ 969](group__ip__4__6.md#ga675d016e405e02882fda701aa8617ab7)static inline bool [net\_ipv6\_is\_sl\_addr](group__ip__4__6.md#ga675d016e405e02882fda701aa8617ab7)(const struct [in6\_addr](structin6__addr.md) \*addr)

970{

971 return UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[0]) == [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(0xFEC0);

972}

973

974

[ 982](group__ip__4__6.md#gae10578b8801d213482de7d7d7e7ba230)static inline bool [net\_ipv6\_is\_ula\_addr](group__ip__4__6.md#gae10578b8801d213482de7d7d7e7ba230)(const struct [in6\_addr](structin6__addr.md) \*addr)

983{

984 return addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xFD;

985}

986

[ 994](group__ip__4__6.md#gab2d854e2b24f866839e547c1092ccff6)static inline bool [net\_ipv6\_is\_global\_addr](group__ip__4__6.md#gab2d854e2b24f866839e547c1092ccff6)(const struct [in6\_addr](structin6__addr.md) \*addr)

995{

996 return (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] & 0xE0) == 0x20;

997}

998

[ 1008](group__ip__4__6.md#gad35da6e137d62231052dda63c68b7eff)static inline bool [net\_ipv6\_is\_private\_addr](group__ip__4__6.md#gad35da6e137d62231052dda63c68b7eff)(const struct [in6\_addr](structin6__addr.md) \*addr)

1009{

1010 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) masked\_32, masked\_7;

1011

1012 masked\_32 = [ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]));

1013 masked\_7 = masked\_32 & 0xfc000000;

1014

1015 return masked\_32 == 0x20010db8 || /\* 2001:db8::/32 \*/

1016 masked\_7 == 0xfc000000; /\* fc00::/7 \*/

1017}

1018

[ 1024](group__ip__4__6.md#gab0211c91e113cf01a8a16b1a106e7290)const struct [in6\_addr](structin6__addr.md) \*[net\_ipv6\_unspecified\_address](group__ip__4__6.md#gab0211c91e113cf01a8a16b1a106e7290)(void);

1025

[ 1031](group__ip__4__6.md#gaceb9afdd7f2f78d96e6debd72f63ebf0)const struct [in\_addr](structin__addr.md) \*[net\_ipv4\_unspecified\_address](group__ip__4__6.md#gaceb9afdd7f2f78d96e6debd72f63ebf0)(void);

1032

[ 1038](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113)const struct [in\_addr](structin__addr.md) \*[net\_ipv4\_broadcast\_address](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113)(void);

1039

1040struct [net\_if](structnet__if.md);

[ 1041](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea)extern bool [net\_if\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea)(struct [net\_if](structnet__if.md) \*iface,

1042 const struct [in\_addr](structin__addr.md) \*addr);

1043

[ 1053](group__ip__4__6.md#ga715455ec5e8041c5d7075fa6913674cd)static inline bool [net\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga715455ec5e8041c5d7075fa6913674cd)(struct [net\_if](structnet__if.md) \*iface,

1054 const struct [in\_addr](structin__addr.md) \*addr)

1055{

1056 return [net\_if\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea)(iface, addr);

1057}

1058

[ 1059](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf)extern bool [net\_if\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf)(struct [net\_if](structnet__if.md) \*iface,

1060 const struct [in\_addr](structin__addr.md) \*addr);

1061

1070#if defined(CONFIG\_NET\_NATIVE\_IPV4)

1071static inline bool [net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)(struct [net\_if](structnet__if.md) \*iface,

1072 const struct [in\_addr](structin__addr.md) \*addr)

1073{

1074 if ([net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)(addr, [net\_ipv4\_broadcast\_address](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113)())) {

1075 return true;

1076 }

1077

1078 return [net\_if\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf)(iface, addr);

1079}

1080#else

[ 1081](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)static inline bool [net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)(struct [net\_if](structnet__if.md) \*iface,

1082 const struct [in\_addr](structin__addr.md) \*addr)

1083{

1084 ARG\_UNUSED(iface);

1085 ARG\_UNUSED(addr);

1086

1087 return false;

1088}

1089#endif

1090

[ 1091](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53)extern struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv4\_addr\_lookup](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53)(const struct [in\_addr](structin__addr.md) \*addr,

1092 struct [net\_if](structnet__if.md) \*\*iface);

1093

[ 1103](group__ip__4__6.md#ga3db2a1fca0b525a7202277700b987eb9)static inline bool [net\_ipv4\_is\_my\_addr](group__ip__4__6.md#ga3db2a1fca0b525a7202277700b987eb9)(const struct [in\_addr](structin__addr.md) \*addr)

1104{

1105 bool ret;

1106

1107 ret = [net\_if\_ipv4\_addr\_lookup](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53)(addr, NULL) != NULL;

1108 if (!ret) {

1109 ret = [net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)(NULL, addr);

1110 }

1111

1112 return ret;

1113}

1114

[ 1122](group__ip__4__6.md#gafe2c8dc0bdb677ba9bc872d051aab2a0)static inline bool [net\_ipv6\_is\_addr\_unspecified](group__ip__4__6.md#gafe2c8dc0bdb677ba9bc872d051aab2a0)(const struct [in6\_addr](structin6__addr.md) \*addr)

1123{

1124 return UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]) == 0 &&

1125 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == 0 &&

1126 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]) == 0 &&

1127 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3]) == 0;

1128}

1129

[ 1138](group__ip__4__6.md#ga5a334819f4e4bf87aea5caa7ef28c68a)static inline bool [net\_ipv6\_is\_addr\_solicited\_node](group__ip__4__6.md#ga5a334819f4e4bf87aea5caa7ef28c68a)(const struct [in6\_addr](structin6__addr.md) \*addr)

1139{

1140 return UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]) == [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0xff020000) &&

1141 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == 0x00000000 &&

1142 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]) == [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0x00000001) &&

1143 ((UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3]) & [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0xff000000)) ==

1144 [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0xff000000));

1145}

1146

[ 1157](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)static inline bool [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(const struct [in6\_addr](structin6__addr.md) \*addr,

1158 int scope)

1159{

1160 return (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xff) && ((addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[1] & 0xF) == scope);

1161}

1162

[ 1172](group__ip__4__6.md#ga3f80a84f330a31aaa875fdea64dc18ec)static inline bool [net\_ipv6\_is\_same\_mcast\_scope](group__ip__4__6.md#ga3f80a84f330a31aaa875fdea64dc18ec)(const struct [in6\_addr](structin6__addr.md) \*addr\_1,

1173 const struct [in6\_addr](structin6__addr.md) \*addr\_2)

1174{

1175 return (addr\_1->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xff) && (addr\_2->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xff) &&

1176 (addr\_1->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[1] == addr\_2->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[1]);

1177}

1178

[ 1186](group__ip__4__6.md#ga55d67d4349dd354a7254a2f8e8320693)static inline bool [net\_ipv6\_is\_addr\_mcast\_global](group__ip__4__6.md#ga55d67d4349dd354a7254a2f8e8320693)(const struct [in6\_addr](structin6__addr.md) \*addr)

1187{

1188 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x0e);

1189}

1190

[ 1200](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)static inline bool [net\_ipv6\_is\_addr\_mcast\_iface](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)(const struct [in6\_addr](structin6__addr.md) \*addr)

1201{

1202 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x01);

1203}

1204

[ 1214](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)static inline bool [net\_ipv6\_is\_addr\_mcast\_link](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)(const struct [in6\_addr](structin6__addr.md) \*addr)

1215{

1216 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x02);

1217}

1218

[ 1228](group__ip__4__6.md#ga497a148717c1c1095abeb4482566dda0)static inline bool [net\_ipv6\_is\_addr\_mcast\_mesh](group__ip__4__6.md#ga497a148717c1c1095abeb4482566dda0)(const struct [in6\_addr](structin6__addr.md) \*addr)

1229{

1230 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x03);

1231}

1232

[ 1242](group__ip__4__6.md#ga6704146124a14be9cf2a636947c35a00)static inline bool [net\_ipv6\_is\_addr\_mcast\_site](group__ip__4__6.md#ga6704146124a14be9cf2a636947c35a00)(const struct [in6\_addr](structin6__addr.md) \*addr)

1243{

1244 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x05);

1245}

1246

[ 1256](group__ip__4__6.md#ga141ed5de3043dd7d6b45098aea38a4b1)static inline bool [net\_ipv6\_is\_addr\_mcast\_org](group__ip__4__6.md#ga141ed5de3043dd7d6b45098aea38a4b1)(const struct [in6\_addr](structin6__addr.md) \*addr)

1257{

1258 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x08);

1259}

1260

[ 1271](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0)static inline bool [net\_ipv6\_is\_addr\_mcast\_group](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0)(const struct [in6\_addr](structin6__addr.md) \*addr,

1272 const struct [in6\_addr](structin6__addr.md) \*[group](structgroup.md))

1273{

1274 return UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[1]) == [group](structgroup.md)->s6\_addr16[1] &&

1275 UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[2]) == [group](structgroup.md)->s6\_addr16[2] &&

1276 UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[3]) == [group](structgroup.md)->s6\_addr16[3] &&

1277 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == [group](structgroup.md)->s6\_addr32[1] &&

1278 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]) == [group](structgroup.md)->s6\_addr32[1] &&

1279 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3]) == [group](structgroup.md)->s6\_addr32[3];

1280}

1281

1290static inline bool

[ 1291](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)[net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)(const struct [in6\_addr](structin6__addr.md) \*addr)

1292{

1293 static const struct [in6\_addr](structin6__addr.md) all\_nodes\_mcast\_group = {

1294 { { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,

1295 0x00, 0x00, 0x00, 0x00, 0x00, 0x01 } }

1296 };

1297

1298 return [net\_ipv6\_is\_addr\_mcast\_group](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0)(addr, &all\_nodes\_mcast\_group);

1299}

1300

1310static inline bool

[ 1311](group__ip__4__6.md#ga35bdad7c958f1ea656680000ee3f6bfd)[net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes](group__ip__4__6.md#ga35bdad7c958f1ea656680000ee3f6bfd)(const struct [in6\_addr](structin6__addr.md) \*addr)

1312{

1313 return [net\_ipv6\_is\_addr\_mcast\_iface](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)(addr) &&

1314 [net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)(addr);

1315}

1316

1326static inline bool

[ 1327](group__ip__4__6.md#gaba3e1259f452381ef3e109bb2eb34c09)[net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes](group__ip__4__6.md#gaba3e1259f452381ef3e109bb2eb34c09)(const struct [in6\_addr](structin6__addr.md) \*addr)

1328{

1329 return [net\_ipv6\_is\_addr\_mcast\_link](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)(addr) &&

1330 [net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)(addr);

1331}

1332

1340static inline

[ 1341](group__ip__4__6.md#ga6091a7406c136fcf480517cb969c9d90)void [net\_ipv6\_addr\_create\_solicited\_node](group__ip__4__6.md#ga6091a7406c136fcf480517cb969c9d90)(const struct [in6\_addr](structin6__addr.md) \*src,

1342 struct [in6\_addr](structin6__addr.md) \*dst)

1343{

1344 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] = 0xFF;

1345 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[1] = 0x02;

1346 UNALIGNED\_PUT(0, &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[1]);

1347 UNALIGNED\_PUT(0, &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[2]);

1348 UNALIGNED\_PUT(0, &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[3]);

1349 UNALIGNED\_PUT(0, &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[4]);

1350 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[10] = 0U;

1351 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] = 0x01;

1352 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] = 0xFF;

1353 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13] = src->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13];

1354 UNALIGNED\_PUT(UNALIGNED\_GET(&src->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[7]), &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[7]);

1355}

1356

[ 1369](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)static inline void [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)(struct [in6\_addr](structin6__addr.md) \*addr,

1370 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr0, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr1,

1371 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr2, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr3,

1372 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr4, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr5,

1373 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr6, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr7)

1374{

1375 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr0), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[0]);

1376 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr1), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[1]);

1377 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr2), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[2]);

1378 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr3), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[3]);

1379 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr4), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[4]);

1380 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr5), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[5]);

1381 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr6), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[6]);

1382 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr7), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[7]);

1383}

1384

[ 1390](group__ip__4__6.md#ga58cbba1c522815b1ce201b0377ffe0b2)static inline void [net\_ipv6\_addr\_create\_ll\_allnodes\_mcast](group__ip__4__6.md#ga58cbba1c522815b1ce201b0377ffe0b2)(struct [in6\_addr](structin6__addr.md) \*addr)

1391{

1392 [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)(addr, 0xff02, 0, 0, 0, 0, 0, 0, 0x0001);

1393}

1394

[ 1400](group__ip__4__6.md#ga30821f0a2c08b4b01b71d362e3a25de1)static inline void [net\_ipv6\_addr\_create\_ll\_allrouters\_mcast](group__ip__4__6.md#ga30821f0a2c08b4b01b71d362e3a25de1)(struct [in6\_addr](structin6__addr.md) \*addr)

1401{

1402 [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)(addr, 0xff02, 0, 0, 0, 0, 0, 0, 0x0002);

1403}

1404

[ 1411](group__ip__4__6.md#ga8c6162c6212051037a33477aab9fc55f)static inline void [net\_ipv6\_addr\_create\_v4\_mapped](group__ip__4__6.md#ga8c6162c6212051037a33477aab9fc55f)(const struct [in\_addr](structin__addr.md) \*addr4,

1412 struct [in6\_addr](structin6__addr.md) \*addr6)

1413{

1414 [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)(addr6, 0, 0, 0, 0, 0, 0xffff,

1415 [ntohs](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)(addr4->[s4\_addr16](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86)[0]),

1416 [ntohs](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)(addr4->[s4\_addr16](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86)[1]));

1417}

1418

[ 1427](group__ip__4__6.md#ga53c24abd635fb2bcb137584dbc8a9026)static inline bool [net\_ipv6\_addr\_is\_v4\_mapped](group__ip__4__6.md#ga53c24abd635fb2bcb137584dbc8a9026)(const struct [in6\_addr](structin6__addr.md) \*addr)

1428{

1429 if (UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]) == 0 &&

1430 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == 0 &&

1431 UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[5]) == 0xffff) {

1432 return true;

1433 }

1434

1435 return false;

1436}

1437

[ 1444](group__ip__4__6.md#ga6d41f1de27e2e8fbb8f12925eba852b4)static inline void [net\_ipv6\_addr\_create\_iid](group__ip__4__6.md#ga6d41f1de27e2e8fbb8f12925eba852b4)(struct [in6\_addr](structin6__addr.md) \*addr,

1445 struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr)

1446{

1447 UNALIGNED\_PUT([htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0xfe800000), &addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]);

1448 UNALIGNED\_PUT(0, &addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]);

1449

1450 switch (lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)) {

1451 case 2:

1452 /\* The generated IPv6 shall not toggle the

1453 \* Universal/Local bit. RFC 6282 ch 3.2.2

1454 \*/

1455 if (lladdr->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) == [NET\_LINK\_IEEE802154](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3)) {

1456 UNALIGNED\_PUT(0, &addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]);

1457 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] = 0xff;

1458 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] = 0xfe;

1459 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13] = 0U;

1460 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[14] = lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[0];

1461 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[15] = lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[1];

1462 }

1463

1464 break;

1465 case 6:

1466 /\* We do not toggle the Universal/Local bit

1467 \* in Bluetooth. See RFC 7668 ch 3.2.2

1468 \*/

1469 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8], lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0), 3);

1470 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] = 0xff;

1471 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] = 0xfe;

1472 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13], lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0) + 3, 3);

1473

1474 if (lladdr->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) == [NET\_LINK\_ETHERNET](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)) {

1475 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] ^= 0x02;

1476 }

1477

1478 break;

1479 case 8:

1480 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8], lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0), lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0));

1481 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] ^= 0x02;

1482 break;

1483 }

1484}

1485

[ 1491](group__ip__4__6.md#gaf4b0c30b926748625bd3c4c81d06ffc5)static inline bool [net\_ipv6\_addr\_based\_on\_ll](group__ip__4__6.md#gaf4b0c30b926748625bd3c4c81d06ffc5)(const struct [in6\_addr](structin6__addr.md) \*addr,

1492 const struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr)

1493{

1494 if (!addr || !lladdr) {

1495 return false;

1496 }

1497

1498 switch (lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)) {

1499 case 2:

1500 if (![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[14], lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0), lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)) &&

1501 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] == 0U &&

1502 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[9] == 0U &&

1503 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[10] == 0U &&

1504 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] == 0xff &&

1505 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] == 0xfe) {

1506 return true;

1507 }

1508

1509 break;

1510 case 6:

1511 if (lladdr->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) == [NET\_LINK\_ETHERNET](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)) {

1512 if (![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[9], &lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[1], 2) &&

1513 ![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13], &lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[3], 3) &&

1514 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] == 0xff &&

1515 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] == 0xfe &&

1516 (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] ^ 0x02) == lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[0]) {

1517 return true;

1518 }

1519 }

1520

1521 break;

1522 case 8:

1523 if (![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[9], &lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[1],

1524 lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) - 1) &&

1525 (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] ^ 0x02) == lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[0]) {

1526 return true;

1527 }

1528

1529 break;

1530 }

1531

1532 return false;

1533}

1534

[ 1543](group__ip__4__6.md#gad97b2c3da722409eada099f9b7e13f03)static inline struct [sockaddr\_in6](structsockaddr__in6.md) \*[net\_sin6](group__ip__4__6.md#gad97b2c3da722409eada099f9b7e13f03)(const struct [sockaddr](structsockaddr.md) \*addr)

1544{

1545 return (struct [sockaddr\_in6](structsockaddr__in6.md) \*)addr;

1546}

1547

[ 1556](group__ip__4__6.md#gacccfbac6a03480840fa219e9a1924dc6)static inline struct [sockaddr\_in](structsockaddr__in.md) \*[net\_sin](group__ip__4__6.md#gacccfbac6a03480840fa219e9a1924dc6)(const struct [sockaddr](structsockaddr.md) \*addr)

1557{

1558 return (struct [sockaddr\_in](structsockaddr__in.md) \*)addr;

1559}

1560

1569static inline

[ 1570](group__ip__4__6.md#gae86d2cd402142190e1ea1c120a57939f)struct sockaddr\_in6\_ptr \*[net\_sin6\_ptr](group__ip__4__6.md#gae86d2cd402142190e1ea1c120a57939f)(const struct sockaddr\_ptr \*addr)

1571{

1572 return (struct sockaddr\_in6\_ptr \*)addr;

1573}

1574

1583static inline

[ 1584](group__ip__4__6.md#ga4b948e84590081a8aed2a63496e57ae2)struct sockaddr\_in\_ptr \*[net\_sin\_ptr](group__ip__4__6.md#ga4b948e84590081a8aed2a63496e57ae2)(const struct sockaddr\_ptr \*addr)

1585{

1586 return (struct sockaddr\_in\_ptr \*)addr;

1587}

1588

1597static inline

[ 1598](group__ip__4__6.md#gad5cf206e18769a15f9fc917e416db6ee)struct sockaddr\_ll\_ptr \*[net\_sll\_ptr](group__ip__4__6.md#gad5cf206e18769a15f9fc917e416db6ee)(const struct sockaddr\_ptr \*addr)

1599{

1600 return (struct sockaddr\_ll\_ptr \*)addr;

1601}

1602

1611static inline

[ 1612](group__ip__4__6.md#gac2fb590a35961c04807dd985f462c5fb)struct sockaddr\_can\_ptr \*[net\_can\_ptr](group__ip__4__6.md#gac2fb590a35961c04807dd985f462c5fb)(const struct sockaddr\_ptr \*addr)

1613{

1614 return (struct sockaddr\_can\_ptr \*)addr;

1615}

1616

[ 1630](group__ip__4__6.md#ga264b3c0a13493eac291ddc85d0b4d43d)\_\_syscall int [net\_addr\_pton](group__ip__4__6.md#ga264b3c0a13493eac291ddc85d0b4d43d)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst);

1631

[ 1643](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)\_\_syscall char \*[net\_addr\_ntop](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src,

1644 char \*dst, size\_t size);

1645

[ 1667](group__ip__4__6.md#ga9918e156f0039cf45d487a112e0a2ada)bool [net\_ipaddr\_parse](group__ip__4__6.md#ga9918e156f0039cf45d487a112e0a2ada)(const char \*str, size\_t str\_len,

1668 struct [sockaddr](structsockaddr.md) \*addr);

1669

[ 1679](group__ip__4__6.md#gaa2354e12d310c0647a98c873c7b7e5ad)int [net\_port\_set\_default](group__ip__4__6.md#gaa2354e12d310c0647a98c873c7b7e5ad)(struct [sockaddr](structsockaddr.md) \*addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) default\_port);

1680

[ 1692](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [net\_tcp\_seq\_cmp](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq2)

1693{

1694 return ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(seq1 - seq2);

1695}

1696

[ 1707](group__ip__4__6.md#gaa77b299f53e5535ac4c4bea1b6531a34)static inline bool [net\_tcp\_seq\_greater](group__ip__4__6.md#gaa77b299f53e5535ac4c4bea1b6531a34)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq2)

1708{

1709 return [net\_tcp\_seq\_cmp](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f)(seq1, seq2) > 0;

1710}

1711

[ 1723](group__ip__4__6.md#ga8b794f251cf8412c769ab415902a9f32)int [net\_bytes\_from\_str](group__ip__4__6.md#ga8b794f251cf8412c769ab415902a9f32)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, int buf\_len, const char \*src);

1724

[ 1733](group__ip__4__6.md#gae74c9ba7ff4addbce7f931bd6fa91fa0)int [net\_tx\_priority2tc](group__ip__4__6.md#gae74c9ba7ff4addbce7f931bd6fa91fa0)(enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) prio);

1734

[ 1743](group__ip__4__6.md#ga7b3c41ae9b3962090d72c130a9fa61b1)int [net\_rx\_priority2tc](group__ip__4__6.md#ga7b3c41ae9b3962090d72c130a9fa61b1)(enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) prio);

1744

[ 1753](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4)static inline enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) [net\_vlan2priority](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

1754{

1755 /\* Map according to IEEE 802.1Q \*/

1756 static const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vlan2priority[] = {

1757 [NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce),

1758 [NET\_PRIORITY\_BK](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b),

1759 [NET\_PRIORITY\_EE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0),

1760 [NET\_PRIORITY\_CA](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354),

1761 [NET\_PRIORITY\_VI](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792),

1762 [NET\_PRIORITY\_VO](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a),

1763 [NET\_PRIORITY\_IC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05),

1764 [NET\_PRIORITY\_NC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef)

1765 };

1766

1767 if (priority >= [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(vlan2priority)) {

1768 /\* Use Best Effort as the default priority \*/

1769 return [NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce);

1770 }

1771

1772 return (enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd))vlan2priority[priority];

1773}

1774

[ 1782](group__ip__4__6.md#ga8be77d043d4d1d29e0879b3b22274629)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_priority2vlan](group__ip__4__6.md#ga8be77d043d4d1d29e0879b3b22274629)(enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) priority)

1783{

1784 /\* The conversion works both ways \*/

1785 return ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))[net\_vlan2priority](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4)(priority);

1786}

1787

[ 1796](group__ip__4__6.md#gaba4c72e3aa2ceb4ac67d25112fb36523)const char \*[net\_family2str](group__ip__4__6.md#gaba4c72e3aa2ceb4ac67d25112fb36523)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family);

1797

1808#if defined(CONFIG\_NET\_IPV6\_PE)

1809int [net\_ipv6\_pe\_add\_filter](group__ip__4__6.md#ga14f9607f6c18869e7755ab497ff62147)(struct [in6\_addr](structin6__addr.md) \*addr, bool is\_denylist);

1810#else

[ 1811](group__ip__4__6.md#ga14f9607f6c18869e7755ab497ff62147)static inline int [net\_ipv6\_pe\_add\_filter](group__ip__4__6.md#ga14f9607f6c18869e7755ab497ff62147)(struct [in6\_addr](structin6__addr.md) \*addr,

1812 bool is\_denylist)

1813{

1814 ARG\_UNUSED(addr);

1815 ARG\_UNUSED(is\_denylist);

1816

1817 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1818}

1819#endif /\* CONFIG\_NET\_IPV6\_PE \*/

1820

1828#if defined(CONFIG\_NET\_IPV6\_PE)

1829int [net\_ipv6\_pe\_del\_filter](group__ip__4__6.md#ga76e7787a18dbf0b3575d46f81603f65a)(struct [in6\_addr](structin6__addr.md) \*addr);

1830#else

[ 1831](group__ip__4__6.md#ga76e7787a18dbf0b3575d46f81603f65a)static inline int [net\_ipv6\_pe\_del\_filter](group__ip__4__6.md#ga76e7787a18dbf0b3575d46f81603f65a)(struct [in6\_addr](structin6__addr.md) \*addr)

1832{

1833 ARG\_UNUSED(addr);

1834

1835 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1836}

1837#endif /\* CONFIG\_NET\_IPV6\_PE \*/

1838

1839#ifdef \_\_cplusplus

1840}

1841#endif

1842

1843#include <zephyr/syscalls/net\_ip.h>

1844

1848

1849

1850#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_IP\_H\_ \*/

[net\_ipv6\_is\_my\_addr](group__ip__4__6.md#ga00853528daf79c947dcdc320035ed538)

static bool net\_ipv6\_is\_my\_addr(struct in6\_addr \*addr)

Check if IPv6 address is found in one of the network interfaces.

**Definition** net\_ip.h:689

[net\_if\_ipv4\_addr\_lookup](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53)

struct net\_if\_addr \* net\_if\_ipv4\_addr\_lookup(const struct in\_addr \*addr, struct net\_if \*\*iface)

[net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)

static void net\_ipv6\_addr\_create(struct in6\_addr \*addr, uint16\_t addr0, uint16\_t addr1, uint16\_t addr2, uint16\_t addr3, uint16\_t addr4, uint16\_t addr5, uint16\_t addr6, uint16\_t addr7)

Construct an IPv6 address from eight 16-bit words.

**Definition** net\_ip.h:1369

[net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)

static bool net\_ipv4\_addr\_cmp(const struct in\_addr \*addr1, const struct in\_addr \*addr2)

Compare two IPv4 addresses.

**Definition** net\_ip.h:900

[NET\_IPV4\_ADDR\_SIZE](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)

#define NET\_IPV4\_ADDR\_SIZE

Binary size of the IPv4 address.

**Definition** net\_ip.h:164

[net\_if\_ipv6\_addr\_lookup](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb)

struct net\_if\_addr \* net\_if\_ipv6\_addr\_lookup(const struct in6\_addr \*addr, struct net\_if \*\*iface)

[net\_ipv6\_is\_addr\_mcast\_org](group__ip__4__6.md#ga141ed5de3043dd7d6b45098aea38a4b1)

static bool net\_ipv6\_is\_addr\_mcast\_org(const struct in6\_addr \*addr)

Check if the IPv6 address is an organization scope multicast address (FFx8::).

**Definition** net\_ip.h:1256

[net\_vlan2priority](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4)

static enum net\_priority net\_vlan2priority(uint8\_t priority)

Convert network packet VLAN priority to network packet priority so we can place the packet into corre...

**Definition** net\_ip.h:1753

[net\_ipv6\_pe\_add\_filter](group__ip__4__6.md#ga14f9607f6c18869e7755ab497ff62147)

static int net\_ipv6\_pe\_add\_filter(struct in6\_addr \*addr, bool is\_denylist)

Add IPv6 prefix as a privacy extension filter.

**Definition** net\_ip.h:1811

[net\_tcp\_seq\_cmp](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f)

static int32\_t net\_tcp\_seq\_cmp(uint32\_t seq1, uint32\_t seq2)

Compare TCP sequence numbers.

**Definition** net\_ip.h:1692

[net\_ipv6\_is\_addr\_mcast](group__ip__4__6.md#ga1a2fb0427eeab1a5dec6d69208ad7f02)

static bool net\_ipv6\_is\_addr\_mcast(const struct in6\_addr \*addr)

Check if the IPv6 address is a multicast address.

**Definition** net\_ip.h:671

[NET\_IPV6\_ADDR\_SIZE](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)

#define NET\_IPV6\_ADDR\_SIZE

Binary size of the IPv6 address.

**Definition** net\_ip.h:151

[net\_addr\_pton](group__ip__4__6.md#ga264b3c0a13493eac291ddc85d0b4d43d)

int net\_addr\_pton(sa\_family\_t family, const char \*src, void \*dst)

Convert a string to IP address.

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:167

[net\_ipv6\_addr\_create\_ll\_allrouters\_mcast](group__ip__4__6.md#ga30821f0a2c08b4b01b71d362e3a25de1)

static void net\_ipv6\_addr\_create\_ll\_allrouters\_mcast(struct in6\_addr \*addr)

Create link local allrouters multicast IPv6 address.

**Definition** net\_ip.h:1400

[net\_addr\_ntop](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)

char \* net\_addr\_ntop(sa\_family\_t family, const void \*src, char \*dst, size\_t size)

Convert IP address to string form.

[net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d)

net\_addr\_state

What is the current state of the network address.

**Definition** net\_ip.h:503

[net\_ipv4\_addr\_cmp\_raw](group__ip__4__6.md#ga32ffb42c62169ac9b34a0faa7c7ffd12)

static bool net\_ipv4\_addr\_cmp\_raw(const uint8\_t \*addr1, const uint8\_t \*addr2)

Compare two raw IPv4 address buffers.

**Definition** net\_ip.h:914

[net\_ipv6\_addr\_cmp](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)

static bool net\_ipv6\_addr\_cmp(const struct in6\_addr \*addr1, const struct in6\_addr \*addr2)

Compare two IPv6 addresses.

**Definition** net\_ip.h:929

[net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes](group__ip__4__6.md#ga35bdad7c958f1ea656680000ee3f6bfd)

static bool net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes(const struct in6\_addr \*addr)

Check if the IPv6 address is a interface scope all nodes multicast address (FF01::1).

**Definition** net\_ip.h:1311

[net\_ipv4\_is\_my\_addr](group__ip__4__6.md#ga3db2a1fca0b525a7202277700b987eb9)

static bool net\_ipv4\_is\_my\_addr(const struct in\_addr \*addr)

Check if the IPv4 address is assigned to any network interface in the system.

**Definition** net\_ip.h:1103

[net\_ipv6\_is\_same\_mcast\_scope](group__ip__4__6.md#ga3f80a84f330a31aaa875fdea64dc18ec)

static bool net\_ipv6\_is\_same\_mcast\_scope(const struct in6\_addr \*addr\_1, const struct in6\_addr \*addr\_2)

Check if the IPv6 addresses have the same multicast scope (FFyx::).

**Definition** net\_ip.h:1172

[net\_ipv6\_addr\_copy\_raw](group__ip__4__6.md#ga4925e6f3734b8fc1d9cb1ca1a510b5f1)

static void net\_ipv6\_addr\_copy\_raw(uint8\_t \*dest, const uint8\_t \*src)

Copy an IPv6 address raw buffer.

**Definition** net\_ip.h:886

[net\_ipv6\_is\_addr\_mcast\_mesh](group__ip__4__6.md#ga497a148717c1c1095abeb4482566dda0)

static bool net\_ipv6\_is\_addr\_mcast\_mesh(const struct in6\_addr \*addr)

Check if the IPv6 address is a mesh-local scope multicast address (FFx3::).

**Definition** net\_ip.h:1228

[net\_sin\_ptr](group__ip__4__6.md#ga4b948e84590081a8aed2a63496e57ae2)

static struct sockaddr\_in\_ptr \* net\_sin\_ptr(const struct sockaddr\_ptr \*addr)

Get sockaddr\_in\_ptr from sockaddr\_ptr.

**Definition** net\_ip.h:1584

[net\_ipv4\_broadcast\_address](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113)

const struct in\_addr \* net\_ipv4\_broadcast\_address(void)

Return pointer to broadcast (all bits ones) IPv4 address.

[net\_ipv6\_addr\_prefix\_mask](group__ip__4__6.md#ga4e91a4298604a916731bf591acc7b326)

static void net\_ipv6\_addr\_prefix\_mask(const uint8\_t \*inaddr, uint8\_t \*outaddr, uint8\_t prefix\_len)

Get the IPv6 network address via the unicast address and the prefix mask.

**Definition** net\_ip.h:757

[htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)

#define htons(x)

Convert 16-bit value from host to network byte order.

**Definition** net\_ip.h:123

[net\_ipv6\_addr\_is\_v4\_mapped](group__ip__4__6.md#ga53c24abd635fb2bcb137584dbc8a9026)

static bool net\_ipv6\_addr\_is\_v4\_mapped(const struct in6\_addr \*addr)

Is the IPv6 address an IPv4 mapped one.

**Definition** net\_ip.h:1427

[net\_if\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea)

bool net\_if\_ipv4\_addr\_mask\_cmp(struct net\_if \*iface, const struct in\_addr \*addr)

[net\_ipv6\_is\_addr\_mcast\_global](group__ip__4__6.md#ga55d67d4349dd354a7254a2f8e8320693)

static bool net\_ipv6\_is\_addr\_mcast\_global(const struct in6\_addr \*addr)

Check if the IPv6 address is a global multicast address (FFxE::/16).

**Definition** net\_ip.h:1186

[net\_ipv6\_addr\_create\_ll\_allnodes\_mcast](group__ip__4__6.md#ga58cbba1c522815b1ce201b0377ffe0b2)

static void net\_ipv6\_addr\_create\_ll\_allnodes\_mcast(struct in6\_addr \*addr)

Create link local allnodes multicast IPv6 address.

**Definition** net\_ip.h:1390

[net\_ipv6\_is\_addr\_solicited\_node](group__ip__4__6.md#ga5a334819f4e4bf87aea5caa7ef28c68a)

static bool net\_ipv6\_is\_addr\_solicited\_node(const struct in6\_addr \*addr)

Check if the IPv6 address is solicited node multicast address FF02:0:0:0:0:1:FFXX:XXXX defined in RFC...

**Definition** net\_ip.h:1138

[net\_ipv6\_addr\_create\_solicited\_node](group__ip__4__6.md#ga6091a7406c136fcf480517cb969c9d90)

static void net\_ipv6\_addr\_create\_solicited\_node(const struct in6\_addr \*src, struct in6\_addr \*dst)

Create solicited node IPv6 multicast address FF02:0:0:0:0:1:FFXX:XXXX defined in RFC 3513.

**Definition** net\_ip.h:1341

[net\_ipv6\_is\_addr\_mcast\_group](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0)

static bool net\_ipv6\_is\_addr\_mcast\_group(const struct in6\_addr \*addr, const struct in6\_addr \*group)

Check if the IPv6 address belongs to certain multicast group.

**Definition** net\_ip.h:1271

[net\_ipv6\_is\_addr\_mcast\_site](group__ip__4__6.md#ga6704146124a14be9cf2a636947c35a00)

static bool net\_ipv6\_is\_addr\_mcast\_site(const struct in6\_addr \*addr)

Check if the IPv6 address is a site scope multicast address (FFx5::).

**Definition** net\_ip.h:1242

[net\_ipv6\_is\_sl\_addr](group__ip__4__6.md#ga675d016e405e02882fda701aa8617ab7)

static bool net\_ipv6\_is\_sl\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a site local address.

**Definition** net\_ip.h:969

[net\_ipv6\_addr\_create\_iid](group__ip__4__6.md#ga6d41f1de27e2e8fbb8f12925eba852b4)

static void net\_ipv6\_addr\_create\_iid(struct in6\_addr \*addr, struct net\_linkaddr \*lladdr)

Create IPv6 address interface identifier.

**Definition** net\_ip.h:1444

[net\_ipv4\_is\_private\_addr](group__ip__4__6.md#ga6f19cb74de130d70668599c05a5ed66b)

static bool net\_ipv4\_is\_private\_addr(const struct in\_addr \*addr)

Check if the given IPv4 address is from a private address range.

**Definition** net\_ip.h:838

[net\_ipv6\_is\_addr\_mcast\_link](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)

static bool net\_ipv6\_is\_addr\_mcast\_link(const struct in6\_addr \*addr)

Check if the IPv6 address is a link local scope multicast address (FFx2::).

**Definition** net\_ip.h:1214

[net\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga715455ec5e8041c5d7075fa6913674cd)

static bool net\_ipv4\_addr\_mask\_cmp(struct net\_if \*iface, const struct in\_addr \*addr)

Check if the given address belongs to same subnet that has been configured for the interface.

**Definition** net\_ip.h:1053

[net\_ip\_protocol\_secure](group__ip__4__6.md#ga721da18d2a3cfd9b3a56e9efc9f6e58b)

net\_ip\_protocol\_secure

Protocol numbers for TLS protocols.

**Definition** net\_ip.h:77

[net\_ipaddr\_copy](group__ip__4__6.md#ga75ffcc08e621c2d47d1ae043fce2acad)

#define net\_ipaddr\_copy(dest, src)

Copy an IPv4 or IPv6 address.

**Definition** net\_ip.h:865

[net\_ipv6\_pe\_del\_filter](group__ip__4__6.md#ga76e7787a18dbf0b3575d46f81603f65a)

static int net\_ipv6\_pe\_del\_filter(struct in6\_addr \*addr)

Delete IPv6 prefix from privacy extension filter list.

**Definition** net\_ip.h:1831

[net\_ip\_mtu](group__ip__4__6.md#ga7a207761e4879c140f48f93978cb2f0b)

net\_ip\_mtu

IP Maximum Transfer Unit.

**Definition** net\_ip.h:463

[net\_rx\_priority2tc](group__ip__4__6.md#ga7b3c41ae9b3962090d72c130a9fa61b1)

int net\_rx\_priority2tc(enum net\_priority prio)

Convert Rx network packet priority to traffic class so we can place the packet into correct Rx queue.

[net\_ipv4\_is\_addr\_loopback](group__ip__4__6.md#ga879e4aed725d7ea3fe609fa989f14735)

static bool net\_ipv4\_is\_addr\_loopback(struct in\_addr \*addr)

Check if the IPv4 address is a loopback address (127.0.0.0/8).

**Definition** net\_ip.h:788

[net\_bytes\_from\_str](group__ip__4__6.md#ga8b794f251cf8412c769ab415902a9f32)

int net\_bytes\_from\_str(uint8\_t \*buf, int buf\_len, const char \*src)

Convert a string of hex values to array of bytes.

[net\_priority2vlan](group__ip__4__6.md#ga8be77d043d4d1d29e0879b3b22274629)

static uint8\_t net\_priority2vlan(enum net\_priority priority)

Convert network packet priority to network packet VLAN priority.

**Definition** net\_ip.h:1782

[net\_ipv6\_addr\_create\_v4\_mapped](group__ip__4__6.md#ga8c6162c6212051037a33477aab9fc55f)

static void net\_ipv6\_addr\_create\_v4\_mapped(const struct in\_addr \*addr4, struct in6\_addr \*addr6)

Create IPv4 mapped IPv6 address.

**Definition** net\_ip.h:1411

[net\_if\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf)

bool net\_if\_ipv4\_is\_addr\_bcast(struct net\_if \*iface, const struct in\_addr \*addr)

[net\_ipv6\_is\_prefix](group__ip__4__6.md#ga9654007b0a3c4d033df1ec3d00bd26ee)

static bool net\_ipv6\_is\_prefix(const uint8\_t \*addr1, const uint8\_t \*addr2, uint8\_t length)

Check if two IPv6 addresses are same when compared after prefix mask.

**Definition** net\_ip.h:719

[net\_ipaddr\_parse](group__ip__4__6.md#ga9918e156f0039cf45d487a112e0a2ada)

bool net\_ipaddr\_parse(const char \*str, size\_t str\_len, struct sockaddr \*addr)

Parse a string that contains either IPv4 or IPv6 address and optional port, and store the information...

[net\_port\_set\_default](group__ip__4__6.md#gaa2354e12d310c0647a98c873c7b7e5ad)

int net\_port\_set\_default(struct sockaddr \*addr, uint16\_t default\_port)

Set the default port in the sockaddr structure.

[net\_ipv6\_is\_addr\_loopback](group__ip__4__6.md#gaa662667005bdc00bf1eb5cf243aad874)

static bool net\_ipv6\_is\_addr\_loopback(struct in6\_addr \*addr)

Check if the IPv6 address is a loopback address (::1).

**Definition** net\_ip.h:656

[net\_tcp\_seq\_greater](group__ip__4__6.md#gaa77b299f53e5535ac4c4bea1b6531a34)

static bool net\_tcp\_seq\_greater(uint32\_t seq1, uint32\_t seq2)

Check that one TCP sequence number is greater.

**Definition** net\_ip.h:1707

[net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c)

net\_sock\_type

Socket type.

**Definition** net\_ip.h:87

[net\_ipv6\_unspecified\_address](group__ip__4__6.md#gab0211c91e113cf01a8a16b1a106e7290)

const struct in6\_addr \* net\_ipv6\_unspecified\_address(void)

Return pointer to any (all bits zeros) IPv6 address.

[net\_ipv6\_is\_global\_addr](group__ip__4__6.md#gab2d854e2b24f866839e547c1092ccff6)

static bool net\_ipv6\_is\_global\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a global address.

**Definition** net\_ip.h:994

[net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes](group__ip__4__6.md#gaba3e1259f452381ef3e109bb2eb34c09)

static bool net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes(const struct in6\_addr \*addr)

Check if the IPv6 address is a link local scope all nodes multicast address (FF02::1).

**Definition** net\_ip.h:1327

[net\_family2str](group__ip__4__6.md#gaba4c72e3aa2ceb4ac67d25112fb36523)

const char \* net\_family2str(sa\_family\_t family)

Return network address family value as a string.

[net\_ipv4\_is\_ll\_addr](group__ip__4__6.md#gac000a319de7a6f95d4a63719bca3b865)

static bool net\_ipv4\_is\_ll\_addr(const struct in\_addr \*addr)

Check if the given IPv4 address is a link local address.

**Definition** net\_ip.h:824

[net\_can\_ptr](group__ip__4__6.md#gac2fb590a35961c04807dd985f462c5fb)

static struct sockaddr\_can\_ptr \* net\_can\_ptr(const struct sockaddr\_ptr \*addr)

Get sockaddr\_can\_ptr from sockaddr\_ptr.

**Definition** net\_ip.h:1612

[ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)

#define ntohl(x)

Convert 32-bit value from network to host byte order.

**Definition** net\_ip.h:107

[net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)

static bool net\_ipv4\_is\_addr\_bcast(struct net\_if \*iface, const struct in\_addr \*addr)

Check if the given IPv4 address is a broadcast address.

**Definition** net\_ip.h:1081

[net\_ipv6\_is\_ll\_addr](group__ip__4__6.md#gacac4279ee8896ddf2a76c612b36edf38)

static bool net\_ipv6\_is\_ll\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a link local address.

**Definition** net\_ip.h:957

[net\_sin](group__ip__4__6.md#gacccfbac6a03480840fa219e9a1924dc6)

static struct sockaddr\_in \* net\_sin(const struct sockaddr \*addr)

Get sockaddr\_in from sockaddr.

**Definition** net\_ip.h:1556

[net\_ipv4\_unspecified\_address](group__ip__4__6.md#gaceb9afdd7f2f78d96e6debd72f63ebf0)

const struct in\_addr \* net\_ipv4\_unspecified\_address(void)

Return pointer to any (all bits zeros) IPv4 address.

[net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)

static bool net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group(const struct in6\_addr \*addr)

Check if the IPv6 address belongs to the all nodes multicast group.

**Definition** net\_ip.h:1291

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:171

[net\_ipv6\_is\_private\_addr](group__ip__4__6.md#gad35da6e137d62231052dda63c68b7eff)

static bool net\_ipv6\_is\_private\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is from a private/local address range.

**Definition** net\_ip.h:1008

[net\_sll\_ptr](group__ip__4__6.md#gad5cf206e18769a15f9fc917e416db6ee)

static struct sockaddr\_ll\_ptr \* net\_sll\_ptr(const struct sockaddr\_ptr \*addr)

Get sockaddr\_ll\_ptr from sockaddr\_ptr.

**Definition** net\_ip.h:1598

[net\_sin6](group__ip__4__6.md#gad97b2c3da722409eada099f9b7e13f03)

static struct sockaddr\_in6 \* net\_sin6(const struct sockaddr \*addr)

Get sockaddr\_in6 from sockaddr.

**Definition** net\_ip.h:1543

[ntohs](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)

#define ntohs(x)

Convert 16-bit value from network to host byte order.

**Definition** net\_ip.h:99

[net\_if\_ipv6\_maddr\_lookup](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975)

struct net\_if\_mcast\_addr \* net\_if\_ipv6\_maddr\_lookup(const struct in6\_addr \*addr, struct net\_if \*\*iface)

[net\_ipv4\_is\_addr\_unspecified](group__ip__4__6.md#gadc623ecacf024733ab6d477d87cc4b9d)

static bool net\_ipv4\_is\_addr\_unspecified(const struct in\_addr \*addr)

Check if the IPv4 address is unspecified (all bits zero).

**Definition** net\_ip.h:800

[net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)

static bool net\_ipv6\_is\_addr\_mcast\_scope(const struct in6\_addr \*addr, int scope)

Check if the IPv6 address is a given scope multicast address (FFyx::).

**Definition** net\_ip.h:1157

[net\_ipv6\_is\_ula\_addr](group__ip__4__6.md#gae10578b8801d213482de7d7d7e7ba230)

static bool net\_ipv6\_is\_ula\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a unique local address.

**Definition** net\_ip.h:982

[net\_ipv6\_is\_addr\_mcast\_iface](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)

static bool net\_ipv6\_is\_addr\_mcast\_iface(const struct in6\_addr \*addr)

Check if the IPv6 address is a interface scope multicast address (FFx1::).

**Definition** net\_ip.h:1200

[htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)

#define htonl(x)

Convert 32-bit value from host to network byte order.

**Definition** net\_ip.h:131

[net\_tx\_priority2tc](group__ip__4__6.md#gae74c9ba7ff4addbce7f931bd6fa91fa0)

int net\_tx\_priority2tc(enum net\_priority prio)

Convert Tx network packet priority to traffic class so we can place the packet into correct Tx queue.

[net\_sin6\_ptr](group__ip__4__6.md#gae86d2cd402142190e1ea1c120a57939f)

static struct sockaddr\_in6\_ptr \* net\_sin6\_ptr(const struct sockaddr\_ptr \*addr)

Get sockaddr\_in6\_ptr from sockaddr\_ptr.

**Definition** net\_ip.h:1570

[net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd)

net\_priority

Network packet priority settings described in IEEE 802.1Q Annex I.1.

**Definition** net\_ip.h:480

[net\_ipv4\_is\_addr\_mcast](group__ip__4__6.md#gae8c3302cf9ca457de32eabcf65975b70)

static bool net\_ipv4\_is\_addr\_mcast(const struct in\_addr \*addr)

Check if the IPv4 address is a multicast address.

**Definition** net\_ip.h:812

[net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)

net\_ip\_protocol

Protocol numbers from IANA/BSD.

**Definition** net\_ip.h:64

[net\_ipv6\_addr\_based\_on\_ll](group__ip__4__6.md#gaf4b0c30b926748625bd3c4c81d06ffc5)

static bool net\_ipv6\_addr\_based\_on\_ll(const struct in6\_addr \*addr, const struct net\_linkaddr \*lladdr)

Check if given address is based on link layer address.

**Definition** net\_ip.h:1491

[net\_ipv4\_addr\_copy\_raw](group__ip__4__6.md#gaf731738fb1761208739976d767736f87)

static void net\_ipv4\_addr\_copy\_raw(uint8\_t \*dest, const uint8\_t \*src)

Copy an IPv4 address raw buffer.

**Definition** net\_ip.h:874

[net\_ipv6\_is\_my\_maddr](group__ip__4__6.md#gaf8c5158de9a65d840faa61bb3dec341c)

static bool net\_ipv6\_is\_my\_maddr(struct in6\_addr \*maddr)

Check if IPv6 multicast address is found in one of the network interfaces.

**Definition** net\_ip.h:705

[net\_ipv6\_addr\_cmp\_raw](group__ip__4__6.md#gafbe40461a645cf11fc8b3a07e1d9156e)

static bool net\_ipv6\_addr\_cmp\_raw(const uint8\_t \*addr1, const uint8\_t \*addr2)

Compare two raw IPv6 address buffers.

**Definition** net\_ip.h:943

[net\_ipv6\_is\_addr\_unspecified](group__ip__4__6.md#gafe2c8dc0bdb677ba9bc872d051aab2a0)

static bool net\_ipv6\_is\_addr\_unspecified(const struct in6\_addr \*addr)

Check if the IPv6 address is unspecified (all bits zero).

**Definition** net\_ip.h:1122

[net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41)

net\_addr\_type

How the network address is assigned to network interface.

**Definition** net\_ip.h:511

[NET\_ADDR\_ANY\_STATE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df)

@ NET\_ADDR\_ANY\_STATE

Default (invalid) address type.

**Definition** net\_ip.h:504

[NET\_ADDR\_TENTATIVE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9)

@ NET\_ADDR\_TENTATIVE

Tentative address.

**Definition** net\_ip.h:505

[NET\_ADDR\_DEPRECATED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3)

@ NET\_ADDR\_DEPRECATED

Deprecated address.

**Definition** net\_ip.h:507

[NET\_ADDR\_PREFERRED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a)

@ NET\_ADDR\_PREFERRED

Preferred address.

**Definition** net\_ip.h:506

[IPPROTO\_TLS\_1\_1](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba102692f9f57dd0ec6f8c6cb54a235d4c)

@ IPPROTO\_TLS\_1\_1

TLS 1.1 protocol.

**Definition** net\_ip.h:79

[IPPROTO\_TLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba6d479e64d940cea948c874d36c656fcc)

@ IPPROTO\_TLS\_1\_0

TLS 1.0 protocol.

**Definition** net\_ip.h:78

[IPPROTO\_DTLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba92e94005d7a80aacbffad2f3f10555ef)

@ IPPROTO\_DTLS\_1\_0

DTLS 1.0 protocol.

**Definition** net\_ip.h:82

[IPPROTO\_TLS\_1\_3](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa43bf0393de00897b350b361f97c85ac)

@ IPPROTO\_TLS\_1\_3

TLS 1.3 protocol.

**Definition** net\_ip.h:81

[IPPROTO\_TLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa5e176fa47ca23a6f25101a5203f8e5a)

@ IPPROTO\_TLS\_1\_2

TLS 1.2 protocol.

**Definition** net\_ip.h:80

[IPPROTO\_DTLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58bad4d2a6ca8756ee52221f19fb06c34a1c)

@ IPPROTO\_DTLS\_1\_2

DTLS 1.2 protocol.

**Definition** net\_ip.h:83

[NET\_IPV4\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1)

@ NET\_IPV4\_MTU

IPv4 MTU length.

**Definition** net\_ip.h:476

[NET\_IPV6\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c)

@ NET\_IPV6\_MTU

IPv6 MTU length.

**Definition** net\_ip.h:470

[SOCK\_DGRAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc)

@ SOCK\_DGRAM

Datagram socket type.

**Definition** net\_ip.h:89

[SOCK\_RAW](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231)

@ SOCK\_RAW

RAW socket type.

**Definition** net\_ip.h:90

[SOCK\_STREAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424)

@ SOCK\_STREAM

Stream socket type.

**Definition** net\_ip.h:88

[NET\_PRIORITY\_NC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef)

@ NET\_PRIORITY\_NC

Network control (highest).

**Definition** net\_ip.h:488

[NET\_PRIORITY\_IC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05)

@ NET\_PRIORITY\_IC

Internetwork control.

**Definition** net\_ip.h:487

[NET\_PRIORITY\_CA](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354)

@ NET\_PRIORITY\_CA

Critical applications.

**Definition** net\_ip.h:484

[NET\_PRIORITY\_VO](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a)

@ NET\_PRIORITY\_VO

Voice, < 10 ms latency and jitter.

**Definition** net\_ip.h:486

[NET\_PRIORITY\_VI](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792)

@ NET\_PRIORITY\_VI

Video, < 100 ms latency and jitter.

**Definition** net\_ip.h:485

[NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce)

@ NET\_PRIORITY\_BE

Best effort (default).

**Definition** net\_ip.h:482

[NET\_PRIORITY\_EE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0)

@ NET\_PRIORITY\_EE

Excellent effort.

**Definition** net\_ip.h:483

[NET\_PRIORITY\_BK](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b)

@ NET\_PRIORITY\_BK

Background (lowest).

**Definition** net\_ip.h:481

[IPPROTO\_IP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a334b0a4a5a3e331e7c7864471e9eab08)

@ IPPROTO\_IP

IP protocol (pseudo-val for setsockopt().

**Definition** net\_ip.h:65

[IPPROTO\_RAW](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a3f186705d5c21da1b72ecb91cca1f7a4)

@ IPPROTO\_RAW

RAW IP packets.

**Definition** net\_ip.h:73

[IPPROTO\_IPIP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a49a42f6d628bf65e78478e8eb4874ff2)

@ IPPROTO\_IPIP

IPIP tunnels.

**Definition** net\_ip.h:68

[IPPROTO\_TCP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4a3c433d15859f62bacc06312791a45e)

@ IPPROTO\_TCP

TCP protocol.

**Definition** net\_ip.h:69

[IPPROTO\_IGMP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4cbcb48be0cd8eb6fb5b5741f1c7b639)

@ IPPROTO\_IGMP

IGMP protocol.

**Definition** net\_ip.h:67

[IPPROTO\_ICMP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a7ccd735b73f6955ae2f4abf3e7ca6bb4)

@ IPPROTO\_ICMP

ICMP protocol.

**Definition** net\_ip.h:66

[IPPROTO\_IPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a892549243e60ed1e04e88a14b44d8185)

@ IPPROTO\_IPV6

IPv6 protocol.

**Definition** net\_ip.h:71

[IPPROTO\_UDP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31abd7dfb22e255a4eed332f41de12d7321)

@ IPPROTO\_UDP

UDP protocol.

**Definition** net\_ip.h:70

[IPPROTO\_ICMPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31aeeff57e3cf726718a92b2138e5842926)

@ IPPROTO\_ICMPV6

ICMPv6 protocol.

**Definition** net\_ip.h:72

[NET\_ADDR\_ANY](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6)

@ NET\_ADDR\_ANY

Default value.

**Definition** net\_ip.h:513

[NET\_ADDR\_OVERRIDABLE](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4)

@ NET\_ADDR\_OVERRIDABLE

Manually set address which is overridable by DHCP.

**Definition** net\_ip.h:521

[NET\_ADDR\_DHCP](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db)

@ NET\_ADDR\_DHCP

Address is from DHCP.

**Definition** net\_ip.h:517

[NET\_ADDR\_MANUAL](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e)

@ NET\_ADDR\_MANUAL

Manually set address.

**Definition** net\_ip.h:519

[NET\_ADDR\_AUTOCONF](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006)

@ NET\_ADDR\_AUTOCONF

Auto configured address.

**Definition** net\_ip.h:515

[NET\_LINK\_IEEE802154](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3)

@ NET\_LINK\_IEEE802154

IEEE 802.15.4 link address.

**Definition** net\_linkaddr.h:53

[NET\_LINK\_ETHERNET](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)

@ NET\_LINK\_ETHERNET

Ethernet link address.

**Definition** net\_linkaddr.h:57

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:120

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[types.h](include_2zephyr_2types_8h.md)

[net\_linkaddr.h](net__linkaddr_8h.md)

Public API for network link address.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[string.h](string_8h.md)

[memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)

void \* memset(void \*buf, int c, size\_t n)

[memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)

int memcmp(const void \*m1, const void \*m2, size\_t n)

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[cmsghdr](structcmsghdr.md)

Control message ancillary data.

**Definition** net\_ip.h:261

[cmsghdr::cmsg\_type](structcmsghdr.md#a4c7cabf7899a688ce10bc92773fca9c1)

int cmsg\_type

Protocol-specific type.

**Definition** net\_ip.h:264

[cmsghdr::cmsg\_len](structcmsghdr.md#a7cf479e5e162e65ad164616453d61df2)

socklen\_t cmsg\_len

Number of bytes, including header.

**Definition** net\_ip.h:262

[cmsghdr::cmsg\_data](structcmsghdr.md#a92c00d02575707f72c04f090b6f8d399)

z\_max\_align\_t cmsg\_data[]

Flexible array member to force alignment of cmsghdr.

**Definition** net\_ip.h:265

[cmsghdr::cmsg\_level](structcmsghdr.md#ac0ff1400cb63fbc2e0ece19434cb8fef)

int cmsg\_level

Originating protocol.

**Definition** net\_ip.h:263

[group](structgroup.md)

Group structure.

**Definition** grp.h:18

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:142

[in6\_addr::s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)

uint8\_t s6\_addr[16]

IPv6 address buffer.

**Definition** net\_ip.h:144

[in6\_addr::s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)

uint32\_t s6\_addr32[4]

In big endian.

**Definition** net\_ip.h:146

[in6\_addr::s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)

uint16\_t s6\_addr16[8]

In big endian.

**Definition** net\_ip.h:145

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:154

[in\_addr::s4\_addr](structin__addr.md#a4fd35e401c510fabab8979eb8416dd9b)

uint8\_t s4\_addr[4]

IPv4 address buffer.

**Definition** net\_ip.h:156

[in\_addr::s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5)

uint32\_t s\_addr

In big endian, for POSIX compatibility.

**Definition** net\_ip.h:159

[in\_addr::s4\_addr16](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86)

uint16\_t s4\_addr16[2]

In big endian.

**Definition** net\_ip.h:157

[in\_addr::s4\_addr32](structin__addr.md#ae4e092a27efb643067d7ce10bd454bed)

uint32\_t s4\_addr32[1]

In big endian.

**Definition** net\_ip.h:158

[iovec](structiovec.md)

IO vector array element.

**Definition** net\_ip.h:243

[iovec::iov\_base](structiovec.md#a07aeddeccf80f14520fdd7ef0759442b)

void \* iov\_base

Pointer to data.

**Definition** net\_ip.h:244

[iovec::iov\_len](structiovec.md#a17b5ac2078fd1adfabb262a95808a07d)

size\_t iov\_len

Length of the data.

**Definition** net\_ip.h:245

[msghdr](structmsghdr.md)

Message struct.

**Definition** net\_ip.h:250

[msghdr::msg\_iov](structmsghdr.md#a1b893a6f84c4ba52708c5dcfcc720293)

struct iovec \* msg\_iov

Scatter/gather array.

**Definition** net\_ip.h:253

[msghdr::msg\_namelen](structmsghdr.md#a47762b69eee1c9ba5736d64516ea0960)

socklen\_t msg\_namelen

Size of socket address.

**Definition** net\_ip.h:252

[msghdr::msg\_name](structmsghdr.md#a691a8866b21c7083974a2ff1e7987ce1)

void \* msg\_name

Optional socket address, big endian.

**Definition** net\_ip.h:251

[msghdr::msg\_flags](structmsghdr.md#a9e8ff97d402c99551cbfd564e9e10a74)

int msg\_flags

Flags on received message.

**Definition** net\_ip.h:257

[msghdr::msg\_controllen](structmsghdr.md#a9fa41b0e9a02b5dc9a01aa6f18108adb)

size\_t msg\_controllen

Ancillary data buffer len.

**Definition** net\_ip.h:256

[msghdr::msg\_iovlen](structmsghdr.md#ad4ef1bd6821e599bf42f936850d2c4d7)

size\_t msg\_iovlen

Number of elements in msg\_iov.

**Definition** net\_ip.h:254

[msghdr::msg\_control](structmsghdr.md#afba5fc31b0f197e25602d2232ca6d783)

void \* msg\_control

Ancillary data.

**Definition** net\_ip.h:255

[net\_if\_addr](structnet__if__addr.md)

Network Interface unicast IP addresses.

**Definition** net\_if.h:54

[net\_if\_config](structnet__if__config.md)

IP and other configuration related data for network interface.

**Definition** net\_if.h:557

[net\_if\_mcast\_addr](structnet__if__mcast__addr.md)

Network Interface multicast IP addresses.

**Definition** net\_if.h:145

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

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

[net\_tuple](structnet__tuple.md)

IPv6/IPv4 network connection tuple.

**Definition** net\_ip.h:494

[net\_tuple::remote\_addr](structnet__tuple.md#a8f9a1aab3c3aedeead795ca6624d4d6d)

struct net\_addr \* remote\_addr

IPv6/IPv4 remote address.

**Definition** net\_ip.h:495

[net\_tuple::local\_port](structnet__tuple.md#a9a1cd0dd55a9e866cb0e910120362b7e)

uint16\_t local\_port

UDP/TCP local port.

**Definition** net\_ip.h:498

[net\_tuple::ip\_proto](structnet__tuple.md#aa9eeba2c8e263afbf6368e04353d6014)

enum net\_ip\_protocol ip\_proto

IP protocol.

**Definition** net\_ip.h:499

[net\_tuple::remote\_port](structnet__tuple.md#ab4c31093a23bc60d8dcf5b784e3fb39a)

uint16\_t remote\_port

UDP/TCP remote port.

**Definition** net\_ip.h:497

[net\_tuple::local\_addr](structnet__tuple.md#af7004f8f8d74d49d6771393825612294)

struct net\_addr \* local\_addr

IPv6/IPv4 local address.

**Definition** net\_ip.h:496

[sockaddr\_in6](structsockaddr__in6.md)

Socket address struct for IPv6.

**Definition** net\_ip.h:181

[sockaddr\_in6::sin6\_scope\_id](structsockaddr__in6.md#a1daad78c9848862ab33a48e05fa8cf17)

uint8\_t sin6\_scope\_id

Interfaces for a scope.

**Definition** net\_ip.h:185

[sockaddr\_in6::sin6\_addr](structsockaddr__in6.md#a219e7f3ecd6d7dcf8fc2465475be490f)

struct in6\_addr sin6\_addr

IPv6 address.

**Definition** net\_ip.h:184

[sockaddr\_in6::sin6\_port](structsockaddr__in6.md#a4fc2b7a478d258e9e778772701096022)

uint16\_t sin6\_port

Port number.

**Definition** net\_ip.h:183

[sockaddr\_in6::sin6\_family](structsockaddr__in6.md#aefa41e43be9c615f8cfd6266c0ed1687)

sa\_family\_t sin6\_family

AF\_INET6.

**Definition** net\_ip.h:182

[sockaddr\_in](structsockaddr__in.md)

Socket address struct for IPv4.

**Definition** net\_ip.h:189

[sockaddr\_in::sin\_port](structsockaddr__in.md#a3cf9239fdd8bd32855d66a4b86349fbb)

uint16\_t sin\_port

Port number.

**Definition** net\_ip.h:191

[sockaddr\_in::sin\_addr](structsockaddr__in.md#a4ea5f2f1138e5c8597097db255a9ec6c)

struct in\_addr sin\_addr

IPv4 address.

**Definition** net\_ip.h:192

[sockaddr\_in::sin\_family](structsockaddr__in.md#a9a7d98bb8e18f4a06a021c32d6cc7117)

sa\_family\_t sin\_family

AF\_INET.

**Definition** net\_ip.h:190

[sockaddr\_ll](structsockaddr__ll.md)

Socket address struct for packet socket.

**Definition** net\_ip.h:196

[sockaddr\_ll::sll\_pkttype](structsockaddr__ll.md#a2001fcf2627149283e3460b18f44b313)

uint8\_t sll\_pkttype

Packet type.

**Definition** net\_ip.h:201

[sockaddr\_ll::sll\_hatype](structsockaddr__ll.md#a2df317106a30498dd9f87e1d4eefc8fc)

uint16\_t sll\_hatype

ARP hardware type.

**Definition** net\_ip.h:200

[sockaddr\_ll::sll\_family](structsockaddr__ll.md#a4920e92fb0613ba8594a6b6c226048d9)

sa\_family\_t sll\_family

Always AF\_PACKET.

**Definition** net\_ip.h:197

[sockaddr\_ll::sll\_protocol](structsockaddr__ll.md#a661e329c10a8f06a85ad831630273e49)

uint16\_t sll\_protocol

Physical-layer protocol.

**Definition** net\_ip.h:198

[sockaddr\_ll::sll\_ifindex](structsockaddr__ll.md#a93b4976ed8e9d58cdcc620f5d1987f68)

int sll\_ifindex

Interface number.

**Definition** net\_ip.h:199

[sockaddr\_ll::sll\_halen](structsockaddr__ll.md#acb72ab39a239d9e5752b7422dc9a2dc6)

uint8\_t sll\_halen

Length of address.

**Definition** net\_ip.h:202

[sockaddr\_ll::sll\_addr](structsockaddr__ll.md#aee52affe8837ffe1c32c94ce34117d6a)

uint8\_t sll\_addr[8]

Physical-layer address, big endian.

**Definition** net\_ip.h:203

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:388

[sockaddr::sa\_family](structsockaddr.md#ac6ef02e9a2e90a30218132ffd7b5a5c5)

sa\_family\_t sa\_family

Address family.

**Definition** net\_ip.h:389

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_ip.h](net__ip_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
