---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__ip_8h_source.html
original_path: doxygen/html/net__ip_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 68](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a8e42ac7edd78566fb827a482b671ac01) [IPPROTO\_ETH\_P\_ALL](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a8e42ac7edd78566fb827a482b671ac01) = 3,

[ 69](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a49a42f6d628bf65e78478e8eb4874ff2) [IPPROTO\_IPIP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a49a42f6d628bf65e78478e8eb4874ff2) = 4,

[ 70](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4a3c433d15859f62bacc06312791a45e) [IPPROTO\_TCP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4a3c433d15859f62bacc06312791a45e) = 6,

[ 71](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31abd7dfb22e255a4eed332f41de12d7321) [IPPROTO\_UDP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31abd7dfb22e255a4eed332f41de12d7321) = 17,

[ 72](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a892549243e60ed1e04e88a14b44d8185) [IPPROTO\_IPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a892549243e60ed1e04e88a14b44d8185) = 41,

[ 73](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31aeeff57e3cf726718a92b2138e5842926) [IPPROTO\_ICMPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31aeeff57e3cf726718a92b2138e5842926) = 58,

[ 74](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a3f186705d5c21da1b72ecb91cca1f7a4) [IPPROTO\_RAW](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a3f186705d5c21da1b72ecb91cca1f7a4) = 255,

75};

76

[ 78](group__ip__4__6.md#ga721da18d2a3cfd9b3a56e9efc9f6e58b)enum [net\_ip\_protocol\_secure](group__ip__4__6.md#ga721da18d2a3cfd9b3a56e9efc9f6e58b) {

[ 79](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba6d479e64d940cea948c874d36c656fcc) [IPPROTO\_TLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba6d479e64d940cea948c874d36c656fcc) = 256,

[ 80](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba102692f9f57dd0ec6f8c6cb54a235d4c) [IPPROTO\_TLS\_1\_1](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba102692f9f57dd0ec6f8c6cb54a235d4c) = 257,

[ 81](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa5e176fa47ca23a6f25101a5203f8e5a) [IPPROTO\_TLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa5e176fa47ca23a6f25101a5203f8e5a) = 258,

[ 82](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa43bf0393de00897b350b361f97c85ac) [IPPROTO\_TLS\_1\_3](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa43bf0393de00897b350b361f97c85ac) = 259,

[ 83](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba92e94005d7a80aacbffad2f3f10555ef) [IPPROTO\_DTLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba92e94005d7a80aacbffad2f3f10555ef) = 272,

[ 84](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58bad4d2a6ca8756ee52221f19fb06c34a1c) [IPPROTO\_DTLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58bad4d2a6ca8756ee52221f19fb06c34a1c) = 273,

85};

86

[ 88](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c)enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) {

[ 89](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424) [SOCK\_STREAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424) = 1,

[ 90](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc) [SOCK\_DGRAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc),

[ 91](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231) [SOCK\_RAW](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231)

92};

93

[ 100](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)#define ntohs(x) sys\_be16\_to\_cpu(x)

101

[ 108](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)#define ntohl(x) sys\_be32\_to\_cpu(x)

109

[ 116](group__ip__4__6.md#ga3cfcf123d4ead264289232f91f2c9ca5)#define ntohll(x) sys\_be64\_to\_cpu(x)

117

[ 124](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)#define htons(x) sys\_cpu\_to\_be16(x)

125

[ 132](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)#define htonl(x) sys\_cpu\_to\_be32(x)

133

[ 140](group__ip__4__6.md#ga9f4bf0773c45ad9a9753a1b784a13fbb)#define htonll(x) sys\_cpu\_to\_be64(x)

141

[ 143](structin6__addr.md)struct [in6\_addr](structin6__addr.md) {

144 union {

[ 145](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[16];

[ 146](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[8];

[ 147](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[4];

148 };

149};

150

[ 152](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)#define NET\_IPV6\_ADDR\_SIZE 16

153

[ 155](structin__addr.md)struct [in\_addr](structin__addr.md) {

156 union {

[ 157](structin__addr.md#a4fd35e401c510fabab8979eb8416dd9b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [s4\_addr](structin__addr.md#a4fd35e401c510fabab8979eb8416dd9b)[4];

[ 158](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [s4\_addr16](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86)[2];

[ 159](structin__addr.md#ae4e092a27efb643067d7ce10bd454bed) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [s4\_addr32](structin__addr.md#ae4e092a27efb643067d7ce10bd454bed)[1];

[ 160](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5);

161 };

162};

163

[ 165](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)#define NET\_IPV4\_ADDR\_SIZE 4

166

[ 168](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)typedef unsigned short int [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda);

169

171#ifndef \_\_socklen\_t\_defined

[ 172](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)typedef size\_t [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a);

173#define \_\_socklen\_t\_defined

174#endif

175

176/\*

177 \* Note that the sin\_port and sin6\_port are in network byte order

178 \* in various sockaddr\* structs.

179 \*/

180

[ 182](structsockaddr__in6.md)struct [sockaddr\_in6](structsockaddr__in6.md) {

[ 183](structsockaddr__in6.md#aefa41e43be9c615f8cfd6266c0ed1687) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sin6\_family](structsockaddr__in6.md#aefa41e43be9c615f8cfd6266c0ed1687);

[ 184](structsockaddr__in6.md#a4fc2b7a478d258e9e778772701096022) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sin6\_port](structsockaddr__in6.md#a4fc2b7a478d258e9e778772701096022);

[ 185](structsockaddr__in6.md#a219e7f3ecd6d7dcf8fc2465475be490f) struct [in6\_addr](structin6__addr.md) [sin6\_addr](structsockaddr__in6.md#a219e7f3ecd6d7dcf8fc2465475be490f);

[ 186](structsockaddr__in6.md#a1daad78c9848862ab33a48e05fa8cf17) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sin6\_scope\_id](structsockaddr__in6.md#a1daad78c9848862ab33a48e05fa8cf17);

187};

188

[ 190](structsockaddr__in.md)struct [sockaddr\_in](structsockaddr__in.md) {

[ 191](structsockaddr__in.md#a9a7d98bb8e18f4a06a021c32d6cc7117) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sin\_family](structsockaddr__in.md#a9a7d98bb8e18f4a06a021c32d6cc7117);

[ 192](structsockaddr__in.md#a3cf9239fdd8bd32855d66a4b86349fbb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sin\_port](structsockaddr__in.md#a3cf9239fdd8bd32855d66a4b86349fbb);

[ 193](structsockaddr__in.md#a4ea5f2f1138e5c8597097db255a9ec6c) struct [in\_addr](structin__addr.md) [sin\_addr](structsockaddr__in.md#a4ea5f2f1138e5c8597097db255a9ec6c);

194};

195

[ 197](structsockaddr__ll.md)struct [sockaddr\_ll](structsockaddr__ll.md) {

[ 198](structsockaddr__ll.md#a4920e92fb0613ba8594a6b6c226048d9) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sll\_family](structsockaddr__ll.md#a4920e92fb0613ba8594a6b6c226048d9);

[ 199](structsockaddr__ll.md#a661e329c10a8f06a85ad831630273e49) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sll\_protocol](structsockaddr__ll.md#a661e329c10a8f06a85ad831630273e49);

[ 200](structsockaddr__ll.md#a93b4976ed8e9d58cdcc620f5d1987f68) int [sll\_ifindex](structsockaddr__ll.md#a93b4976ed8e9d58cdcc620f5d1987f68);

[ 201](structsockaddr__ll.md#a2df317106a30498dd9f87e1d4eefc8fc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sll\_hatype](structsockaddr__ll.md#a2df317106a30498dd9f87e1d4eefc8fc);

[ 202](structsockaddr__ll.md#a2001fcf2627149283e3460b18f44b313) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sll\_pkttype](structsockaddr__ll.md#a2001fcf2627149283e3460b18f44b313);

[ 203](structsockaddr__ll.md#acb72ab39a239d9e5752b7422dc9a2dc6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sll\_halen](structsockaddr__ll.md#acb72ab39a239d9e5752b7422dc9a2dc6);

[ 204](structsockaddr__ll.md#aee52affe8837ffe1c32c94ce34117d6a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sll\_addr](structsockaddr__ll.md#aee52affe8837ffe1c32c94ce34117d6a)[8];

205};

206

208

210struct sockaddr\_in6\_ptr {

211 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sin6\_family;

212 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sin6\_port;

213 struct [in6\_addr](structin6__addr.md) \*sin6\_addr;

214 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sin6\_scope\_id;

215};

216

218struct sockaddr\_in\_ptr {

219 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sin\_family;

220 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sin\_port;

221 struct in\_addr \*sin\_addr;

222};

223

225struct sockaddr\_ll\_ptr {

226 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sll\_family;

227 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sll\_protocol;

228 int sll\_ifindex;

229 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sll\_hatype;

230 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sll\_pkttype;

231 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sll\_halen;

232 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*sll\_addr;

233};

234

236struct sockaddr\_un\_ptr {

237 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sun\_family;

238 char \*sun\_path;

239};

240

241struct sockaddr\_can\_ptr {

242 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) can\_family;

243 int can\_ifindex;

244};

245

247

248#if !defined(HAVE\_IOVEC)

[ 250](structiovec.md)struct [iovec](structiovec.md) {

[ 251](structiovec.md#a07aeddeccf80f14520fdd7ef0759442b) void \*[iov\_base](structiovec.md#a07aeddeccf80f14520fdd7ef0759442b);

[ 252](structiovec.md#a17b5ac2078fd1adfabb262a95808a07d) size\_t [iov\_len](structiovec.md#a17b5ac2078fd1adfabb262a95808a07d);

253};

254#endif

255

[ 257](structmsghdr.md)struct [msghdr](structmsghdr.md) {

[ 258](structmsghdr.md#a691a8866b21c7083974a2ff1e7987ce1) void \*[msg\_name](structmsghdr.md#a691a8866b21c7083974a2ff1e7987ce1);

[ 259](structmsghdr.md#a47762b69eee1c9ba5736d64516ea0960) [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) [msg\_namelen](structmsghdr.md#a47762b69eee1c9ba5736d64516ea0960);

[ 260](structmsghdr.md#a1b893a6f84c4ba52708c5dcfcc720293) struct [iovec](structiovec.md) \*[msg\_iov](structmsghdr.md#a1b893a6f84c4ba52708c5dcfcc720293);

[ 261](structmsghdr.md#ad4ef1bd6821e599bf42f936850d2c4d7) size\_t [msg\_iovlen](structmsghdr.md#ad4ef1bd6821e599bf42f936850d2c4d7);

[ 262](structmsghdr.md#afba5fc31b0f197e25602d2232ca6d783) void \*[msg\_control](structmsghdr.md#afba5fc31b0f197e25602d2232ca6d783);

[ 263](structmsghdr.md#a9fa41b0e9a02b5dc9a01aa6f18108adb) size\_t [msg\_controllen](structmsghdr.md#a9fa41b0e9a02b5dc9a01aa6f18108adb);

[ 264](structmsghdr.md#a9e8ff97d402c99551cbfd564e9e10a74) int [msg\_flags](structmsghdr.md#a9e8ff97d402c99551cbfd564e9e10a74);

265};

266

[ 268](structcmsghdr.md)struct [cmsghdr](structcmsghdr.md) {

[ 269](structcmsghdr.md#a7cf479e5e162e65ad164616453d61df2) [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) [cmsg\_len](structcmsghdr.md#a7cf479e5e162e65ad164616453d61df2);

[ 270](structcmsghdr.md#ac0ff1400cb63fbc2e0ece19434cb8fef) int [cmsg\_level](structcmsghdr.md#ac0ff1400cb63fbc2e0ece19434cb8fef);

[ 271](structcmsghdr.md#a4c7cabf7899a688ce10bc92773fca9c1) int [cmsg\_type](structcmsghdr.md#a4c7cabf7899a688ce10bc92773fca9c1);

[ 272](structcmsghdr.md#a92c00d02575707f72c04f090b6f8d399) z\_max\_align\_t [cmsg\_data](structcmsghdr.md#a92c00d02575707f72c04f090b6f8d399)[];

273};

274

276

277/\* Alignment for headers and data. These are arch specific but define

278 \* them here atm if not found already.

279 \*/

280#if !defined(ALIGN\_H)

281#define ALIGN\_H(x) ROUND\_UP(x, \_\_alignof\_\_(struct cmsghdr))

282#endif

283#if !defined(ALIGN\_D)

284#define ALIGN\_D(x) ROUND\_UP(x, \_\_alignof\_\_(z\_max\_align\_t))

285#endif

286

288

289#if !defined(CMSG\_FIRSTHDR)

[ 295](group__ip__4__6.md#ga39567a31d167fc53336d2ab4a2cd78a4)#define CMSG\_FIRSTHDR(msghdr) \

296 ((msghdr)->msg\_controllen >= sizeof(struct cmsghdr) ? \

297 (struct cmsghdr \*)((msghdr)->msg\_control) : NULL)

298#endif

299

300#if !defined(CMSG\_NXTHDR)

[ 305](group__ip__4__6.md#ga77c17efca635d597cb6e98b28172bdc0)#define CMSG\_NXTHDR(msghdr, cmsg) \

306 (((cmsg) == NULL) ? CMSG\_FIRSTHDR(msghdr) : \

307 (((uint8\_t \*)(cmsg) + ALIGN\_H((cmsg)->cmsg\_len) + \

308 ALIGN\_D(sizeof(struct cmsghdr)) > \

309 (uint8\_t \*)((msghdr)->msg\_control) + (msghdr)->msg\_controllen) ? \

310 NULL : \

311 (struct cmsghdr \*)((uint8\_t \*)(cmsg) + \

312 ALIGN\_H((cmsg)->cmsg\_len))))

313#endif

314

315#if !defined(CMSG\_DATA)

[ 323](group__ip__4__6.md#ga5ab6d56e410ac0904107e84aeb1484cc)#define CMSG\_DATA(cmsg) ((uint8\_t \*)(cmsg) + ALIGN\_D(sizeof(struct cmsghdr)))

324#endif

325

326#if !defined(CMSG\_SPACE)

[ 331](group__ip__4__6.md#ga8db11d639dd07c723256f3bb5bc89044)#define CMSG\_SPACE(length) (ALIGN\_D(sizeof(struct cmsghdr)) + ALIGN\_H(length))

332#endif

333

334#if !defined(CMSG\_LEN)

[ 340](group__ip__4__6.md#gadb36e4ff4fa9a0c6730321c4bfcf64bc)#define CMSG\_LEN(length) (ALIGN\_D(sizeof(struct cmsghdr)) + length)

341#endif

342

344

345/\* Packet types. \*/

346#define PACKET\_HOST 0 /\* To us \*/

347#define PACKET\_BROADCAST 1 /\* To all \*/

348#define PACKET\_MULTICAST 2 /\* To group \*/

349#define PACKET\_OTHERHOST 3 /\* To someone else \*/

350#define PACKET\_OUTGOING 4 /\* Originated by us \*/

351#define PACKET\_LOOPBACK 5

352#define PACKET\_FASTROUTE 6

353

354/\* ARP protocol HARDWARE identifiers. \*/

355#define ARPHRD\_ETHER 1

356

357/\* Note: These macros are defined in a specific order.

358 \* The largest sockaddr size is the last one.

359 \*/

360#if defined(CONFIG\_NET\_IPV4)

361#undef NET\_SOCKADDR\_MAX\_SIZE

362#undef NET\_SOCKADDR\_PTR\_MAX\_SIZE

363#define NET\_SOCKADDR\_MAX\_SIZE (sizeof(struct sockaddr\_in))

364#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_in\_ptr))

365#endif

366

367#if defined(CONFIG\_NET\_SOCKETS\_PACKET)

368#undef NET\_SOCKADDR\_MAX\_SIZE

369#undef NET\_SOCKADDR\_PTR\_MAX\_SIZE

370#define NET\_SOCKADDR\_MAX\_SIZE (sizeof(struct sockaddr\_ll))

371#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_ll\_ptr))

372#endif

373

374#if defined(CONFIG\_NET\_IPV6)

375#undef NET\_SOCKADDR\_MAX\_SIZE

376#define NET\_SOCKADDR\_MAX\_SIZE (sizeof(struct sockaddr\_in6))

377#if !defined(CONFIG\_NET\_SOCKETS\_PACKET)

378#undef NET\_SOCKADDR\_PTR\_MAX\_SIZE

379#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_in6\_ptr))

380#endif

381#endif

382

383#if defined(CONFIG\_NET\_NATIVE\_OFFLOADED\_SOCKETS)

384#define UNIX\_PATH\_MAX 108

385#undef NET\_SOCKADDR\_MAX\_SIZE

386/\* Define NET\_SOCKADDR\_MAX\_SIZE to be struct of sa\_family\_t + char[UNIX\_PATH\_MAX] \*/

387#define NET\_SOCKADDR\_MAX\_SIZE (UNIX\_PATH\_MAX+sizeof(sa\_family\_t))

388#if !defined(CONFIG\_NET\_SOCKETS\_PACKET)

389#undef NET\_SOCKADDR\_PTR\_MAX\_SIZE

390#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_un\_ptr))

391#endif

392#endif

393

394#if !defined(CONFIG\_NET\_IPV4)

395#if !defined(CONFIG\_NET\_IPV6)

396#if !defined(CONFIG\_NET\_SOCKETS\_PACKET)

397#if !defined(CONFIG\_NET\_NATIVE\_OFFLOADED\_SOCKETS)

398#define NET\_SOCKADDR\_MAX\_SIZE (sizeof(struct sockaddr\_in6))

399#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_in6\_ptr))

400#endif

401#endif

402#endif

403#endif

404

406

[ 408](structsockaddr.md)struct [sockaddr](structsockaddr.md) {

[ 409](structsockaddr.md#ac6ef02e9a2e90a30218132ffd7b5a5c5) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sa\_family](structsockaddr.md#ac6ef02e9a2e90a30218132ffd7b5a5c5);

411 char data[NET\_SOCKADDR\_MAX\_SIZE - sizeof([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda))];

413};

414

416

417struct sockaddr\_ptr {

418 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family;

419 char data[NET\_SOCKADDR\_PTR\_MAX\_SIZE - sizeof([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda))];

420};

421

422/\* Same as sockaddr in our case \*/

423struct sockaddr\_storage {

424 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) ss\_family;

425 char data[NET\_SOCKADDR\_MAX\_SIZE - sizeof([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda))];

426};

427

428/\* Socket address struct for UNIX domain sockets \*/

429struct sockaddr\_un {

430 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sun\_family; /\* AF\_UNIX \*/

431 char sun\_path[NET\_SOCKADDR\_MAX\_SIZE - sizeof([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda))];

432};

433

434struct net\_addr {

435 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family;

436 union {

437 struct in6\_addr in6\_addr;

438 struct in\_addr in\_addr;

439 };

440};

441

443extern const struct [in6\_addr](structin6__addr.md) in6addr\_any;

444

446extern const struct [in6\_addr](structin6__addr.md) in6addr\_loopback;

447

449

[ 451](group__ip__4__6.md#ga1de876a356ee05a2e9427b741f99f49c)#define IN6ADDR\_ANY\_INIT { { { 0, 0, 0, 0, 0, 0, 0, 0, 0, \

452 0, 0, 0, 0, 0, 0, 0 } } }

453

[ 455](group__ip__4__6.md#ga5562c81af19ee5988ddc5a5c6153cf37)#define IN6ADDR\_LOOPBACK\_INIT { { { 0, 0, 0, 0, 0, 0, 0, \

456 0, 0, 0, 0, 0, 0, 0, 0, 1 } } }

457

[ 459](group__ip__4__6.md#ga5d1940045dc2e7de552f3d4ff13a74ab)#define INADDR\_ANY 0

460

[ 462](group__ip__4__6.md#ga4a725f61ded23ce8a7dff8e82ed51986)#define INADDR\_BROADCAST 0xffffffff

463

[ 465](group__ip__4__6.md#ga915fcf49ce8c1e235e64fc83b57ec5b1)#define INADDR\_ANY\_INIT { { { INADDR\_ANY } } }

466

[ 468](group__ip__4__6.md#ga554163cb2fa86ef4307dd1fff2aad2eb)#define INADDR\_LOOPBACK\_INIT { { { 127, 0, 0, 1 } } }

469

[ 471](group__ip__4__6.md#ga93b37007689284fd9c4bde1a8f4b9199)#define INET\_ADDRSTRLEN 16

[ 475](group__ip__4__6.md#gaf776b22a727aae7c9f4d869d50df47e8)#define INET6\_ADDRSTRLEN 46

476

478

479/\* These are for internal usage of the stack \*/

480#define NET\_IPV6\_ADDR\_LEN sizeof("xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx")

481#define NET\_IPV4\_ADDR\_LEN sizeof("xxx.xxx.xxx.xxx")

482

484

[ 486](group__ip__4__6.md#ga7a207761e4879c140f48f93978cb2f0b)enum [net\_ip\_mtu](group__ip__4__6.md#ga7a207761e4879c140f48f93978cb2f0b) {

490#if defined(CONFIG\_NET\_NATIVE\_IPV6)

491 [NET\_IPV6\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c) = CONFIG\_NET\_IPV6\_MTU,

492#else

[ 493](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c) [NET\_IPV6\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c) = 1280,

494#endif

495

[ 499](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1) [NET\_IPV4\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1) = 576,

500};

501

[ 503](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd)enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) {

[ 504](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b) [NET\_PRIORITY\_BK](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b) = 1,

[ 505](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce) [NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce) = 0,

[ 506](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0) [NET\_PRIORITY\_EE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0) = 2,

[ 507](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354) [NET\_PRIORITY\_CA](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354) = 3,

[ 508](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792) [NET\_PRIORITY\_VI](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792) = 4,

[ 509](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a) [NET\_PRIORITY\_VO](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a) = 5,

[ 510](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05) [NET\_PRIORITY\_IC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05) = 6,

[ 511](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef) [NET\_PRIORITY\_NC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef) = 7

512} \_\_packed;

513

[ 514](group__ip__4__6.md#ga5b32bdfc249437709bb25bd95ec7d6d7)#define NET\_MAX\_PRIORITIES 8

515

[ 517](structnet__tuple.md)struct [net\_tuple](structnet__tuple.md) {

[ 518](structnet__tuple.md#a8f9a1aab3c3aedeead795ca6624d4d6d) struct net\_addr \*[remote\_addr](structnet__tuple.md#a8f9a1aab3c3aedeead795ca6624d4d6d);

[ 519](structnet__tuple.md#af7004f8f8d74d49d6771393825612294) struct net\_addr \*[local\_addr](structnet__tuple.md#af7004f8f8d74d49d6771393825612294);

[ 520](structnet__tuple.md#ab4c31093a23bc60d8dcf5b784e3fb39a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [remote\_port](structnet__tuple.md#ab4c31093a23bc60d8dcf5b784e3fb39a);

[ 521](structnet__tuple.md#a9a1cd0dd55a9e866cb0e910120362b7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [local\_port](structnet__tuple.md#a9a1cd0dd55a9e866cb0e910120362b7e);

[ 522](structnet__tuple.md#aa9eeba2c8e263afbf6368e04353d6014) enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) [ip\_proto](structnet__tuple.md#aa9eeba2c8e263afbf6368e04353d6014);

523};

524

[ 526](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d)enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) {

[ 527](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df) [NET\_ADDR\_ANY\_STATE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df) = -1,

[ 528](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9) [NET\_ADDR\_TENTATIVE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9) = 0,

[ 529](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a) [NET\_ADDR\_PREFERRED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a),

[ 530](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3) [NET\_ADDR\_DEPRECATED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3),

531} \_\_packed;

532

[ 534](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41)enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) {

[ 536](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6) [NET\_ADDR\_ANY](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6) = 0,

[ 538](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006) [NET\_ADDR\_AUTOCONF](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006),

[ 540](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db) [NET\_ADDR\_DHCP](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db),

[ 542](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e) [NET\_ADDR\_MANUAL](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e),

[ 544](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4) [NET\_ADDR\_OVERRIDABLE](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4),

545} \_\_packed;

546

548

549struct net\_ipv6\_hdr {

550 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vtc;

551 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tcflow;

552 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) flow;

553 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len;

554 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nexthdr;

555 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit;

556 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[[NET\_IPV6\_ADDR\_SIZE](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)];

557 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[[NET\_IPV6\_ADDR\_SIZE](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)];

558} \_\_packed;

559

560struct net\_ipv6\_frag\_hdr {

561 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nexthdr;

562 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reserved;

563 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset;

564 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id;

565} \_\_packed;

566

567struct net\_ipv4\_hdr {

568 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vhl;

569 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tos;

570 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len;

571 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id[2];

572 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset[2];

573 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl;

574 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proto;

575 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chksum;

576 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[[NET\_IPV4\_ADDR\_SIZE](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)];

577 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[[NET\_IPV4\_ADDR\_SIZE](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)];

578} \_\_packed;

579

580struct net\_icmp\_hdr {

581 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type;

582 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code;

583 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chksum;

584} \_\_packed;

585

586struct net\_udp\_hdr {

587 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src\_port;

588 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst\_port;

589 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len;

590 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chksum;

591} \_\_packed;

592

593struct net\_tcp\_hdr {

594 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src\_port;

595 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst\_port;

596 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) seq[4];

597 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ack[4];

598 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset;

599 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

600 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wnd[2];

601 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chksum;

602 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) urg[2];

603 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) optdata[0];

604} \_\_packed;

605

606static inline const char \*net\_addr\_type2str(enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) type)

607{

608 switch (type) {

609 case [NET\_ADDR\_AUTOCONF](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006):

610 return "AUTO";

611 case [NET\_ADDR\_DHCP](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db):

612 return "DHCP";

613 case [NET\_ADDR\_MANUAL](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e):

614 return "MANUAL";

615 case [NET\_ADDR\_OVERRIDABLE](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4):

616 return "OVERRIDE";

617 case [NET\_ADDR\_ANY](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6):

618 default:

619 break;

620 }

621

622 return "<unknown>";

623}

624

625/\* IPv6 extension headers types \*/

626#define NET\_IPV6\_NEXTHDR\_HBHO 0

627#define NET\_IPV6\_NEXTHDR\_DESTO 60

628#define NET\_IPV6\_NEXTHDR\_ROUTING 43

629#define NET\_IPV6\_NEXTHDR\_FRAG 44

630#define NET\_IPV6\_NEXTHDR\_NONE 59

631

636union net\_ip\_header {

637 struct net\_ipv4\_hdr \*ipv4;

638 struct net\_ipv6\_hdr \*ipv6;

639};

640

641union net\_proto\_header {

642 struct net\_udp\_hdr \*udp;

643 struct net\_tcp\_hdr \*tcp;

644};

645

646#define NET\_UDPH\_LEN 8 /\* Size of UDP header \*/

647#define NET\_TCPH\_LEN 20 /\* Size of TCP header \*/

648#define NET\_ICMPH\_LEN 4 /\* Size of ICMP header \*/

649

650#define NET\_IPV6H\_LEN 40 /\* Size of IPv6 header \*/

651#define NET\_ICMPV6H\_LEN NET\_ICMPH\_LEN /\* Size of ICMPv6 header \*/

652#define NET\_IPV6UDPH\_LEN (NET\_UDPH\_LEN + NET\_IPV6H\_LEN) /\* IPv6 + UDP \*/

653#define NET\_IPV6TCPH\_LEN (NET\_TCPH\_LEN + NET\_IPV6H\_LEN) /\* IPv6 + TCP \*/

654#define NET\_IPV6ICMPH\_LEN (NET\_IPV6H\_LEN + NET\_ICMPH\_LEN) /\* ICMPv6 + IPv6 \*/

655#define NET\_IPV6\_FRAGH\_LEN 8

656

657#define NET\_IPV4H\_LEN 20 /\* Size of IPv4 header \*/

658#define NET\_ICMPV4H\_LEN NET\_ICMPH\_LEN /\* Size of ICMPv4 header \*/

659#define NET\_IPV4UDPH\_LEN (NET\_UDPH\_LEN + NET\_IPV4H\_LEN) /\* IPv4 + UDP \*/

660#define NET\_IPV4TCPH\_LEN (NET\_TCPH\_LEN + NET\_IPV4H\_LEN) /\* IPv4 + TCP \*/

661#define NET\_IPV4ICMPH\_LEN (NET\_IPV4H\_LEN + NET\_ICMPH\_LEN) /\* ICMPv4 + IPv4 \*/

662

663#define NET\_IPV6H\_LENGTH\_OFFSET 0x04 /\* Offset of the Length field in the IPv6 header \*/

664

665#define NET\_IPV6\_FRAGH\_OFFSET\_MASK 0xfff8 /\* Mask for the 13-bit Fragment Offset field \*/

666#define NET\_IPV4\_FRAGH\_OFFSET\_MASK 0x1fff /\* Mask for the 13-bit Fragment Offset field \*/

667#define NET\_IPV4\_MORE\_FRAG\_MASK 0x2000 /\* Mask for the 1-bit More Fragments field \*/

668#define NET\_IPV4\_DO\_NOT\_FRAG\_MASK 0x4000 /\* Mask for the 1-bit Do Not Fragment field \*/

669

671

[ 679](group__ip__4__6.md#gaa662667005bdc00bf1eb5cf243aad874)static inline bool [net\_ipv6\_is\_addr\_loopback](group__ip__4__6.md#gaa662667005bdc00bf1eb5cf243aad874)(struct [in6\_addr](structin6__addr.md) \*addr)

680{

681 return UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]) == 0 &&

682 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == 0 &&

683 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]) == 0 &&

684 [ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3])) == 1;

685}

686

[ 694](group__ip__4__6.md#ga1a2fb0427eeab1a5dec6d69208ad7f02)static inline bool [net\_ipv6\_is\_addr\_mcast](group__ip__4__6.md#ga1a2fb0427eeab1a5dec6d69208ad7f02)(const struct [in6\_addr](structin6__addr.md) \*addr)

695{

696 return addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xFF;

697}

698

699struct [net\_if](structnet__if.md);

700struct [net\_if\_config](structnet__if__config.md);

701

[ 702](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb)extern struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_lookup](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb)(const struct [in6\_addr](structin6__addr.md) \*addr,

703 struct [net\_if](structnet__if.md) \*\*iface);

704

[ 712](group__ip__4__6.md#ga00853528daf79c947dcdc320035ed538)static inline bool [net\_ipv6\_is\_my\_addr](group__ip__4__6.md#ga00853528daf79c947dcdc320035ed538)(struct [in6\_addr](structin6__addr.md) \*addr)

713{

714 return [net\_if\_ipv6\_addr\_lookup](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb)(addr, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

715}

716

[ 717](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975)extern struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv6\_maddr\_lookup](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975)(

718 const struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface);

719

[ 728](group__ip__4__6.md#gaf8c5158de9a65d840faa61bb3dec341c)static inline bool [net\_ipv6\_is\_my\_maddr](group__ip__4__6.md#gaf8c5158de9a65d840faa61bb3dec341c)(struct [in6\_addr](structin6__addr.md) \*maddr)

729{

730 return [net\_if\_ipv6\_maddr\_lookup](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975)(maddr, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

731}

732

[ 742](group__ip__4__6.md#ga9654007b0a3c4d033df1ec3d00bd26ee)static inline bool [net\_ipv6\_is\_prefix](group__ip__4__6.md#ga9654007b0a3c4d033df1ec3d00bd26ee)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1,

743 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2,

744 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) length)

745{

746 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bits = 128 - length;

747 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bytes = length / 8U;

748 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) remain = bits % 8;

749 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask;

750

751 if (length > 128) {

752 return false;

753 }

754

755 if ([memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(addr1, addr2, bytes)) {

756 return false;

757 }

758

759 if (!remain) {

760 /\* No remaining bits, the prefixes are the same as first

761 \* bytes are the same.

762 \*/

763 return true;

764 }

765

766 /\* Create a mask that has remaining most significant bits set \*/

767 mask = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))((0xff << (8 - remain)) ^ 0xff) << remain;

768

769 return (addr1[bytes] & mask) == (addr2[bytes] & mask);

770}

771

772

[ 780](group__ip__4__6.md#ga4e91a4298604a916731bf591acc7b326)static inline void [net\_ipv6\_addr\_prefix\_mask](group__ip__4__6.md#ga4e91a4298604a916731bf591acc7b326)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*inaddr,

781 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*outaddr,

782 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prefix\_len)

783{

784 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bits = 128 - prefix\_len;

785 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bytes = prefix\_len / 8U;

786 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) remain = bits % 8;

787 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask;

788

789 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(outaddr, 0, 16U);

790 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(outaddr, inaddr, bytes);

791

792 if (!remain) {

793 /\* No remaining bits, the prefixes are the same as first

794 \* bytes are the same.

795 \*/

796 return;

797 }

798

799 /\* Create a mask that has remaining most significant bits set \*/

800 mask = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))((0xff << (8 - remain)) ^ 0xff) << remain;

801 outaddr[bytes] = inaddr[bytes] & mask;

802}

803

[ 811](group__ip__4__6.md#ga879e4aed725d7ea3fe609fa989f14735)static inline bool [net\_ipv4\_is\_addr\_loopback](group__ip__4__6.md#ga879e4aed725d7ea3fe609fa989f14735)(struct [in\_addr](structin__addr.md) \*addr)

812{

813 return addr->[s4\_addr](structin__addr.md#a4fd35e401c510fabab8979eb8416dd9b)[0] == 127U;

814}

815

[ 823](group__ip__4__6.md#gadc623ecacf024733ab6d477d87cc4b9d)static inline bool [net\_ipv4\_is\_addr\_unspecified](group__ip__4__6.md#gadc623ecacf024733ab6d477d87cc4b9d)(const struct [in\_addr](structin__addr.md) \*addr)

824{

825 return UNALIGNED\_GET(&addr->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5)) == 0;

826}

827

[ 835](group__ip__4__6.md#gae8c3302cf9ca457de32eabcf65975b70)static inline bool [net\_ipv4\_is\_addr\_mcast](group__ip__4__6.md#gae8c3302cf9ca457de32eabcf65975b70)(const struct [in\_addr](structin__addr.md) \*addr)

836{

837 return ([ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5))) & 0xF0000000) == 0xE0000000;

838}

839

[ 847](group__ip__4__6.md#gac000a319de7a6f95d4a63719bca3b865)static inline bool [net\_ipv4\_is\_ll\_addr](group__ip__4__6.md#gac000a319de7a6f95d4a63719bca3b865)(const struct [in\_addr](structin__addr.md) \*addr)

848{

849 return ([ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5))) & 0xFFFF0000) == 0xA9FE0000;

850}

851

[ 861](group__ip__4__6.md#ga6f19cb74de130d70668599c05a5ed66b)static inline bool [net\_ipv4\_is\_private\_addr](group__ip__4__6.md#ga6f19cb74de130d70668599c05a5ed66b)(const struct [in\_addr](structin__addr.md) \*addr)

862{

863 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) masked\_24, masked\_16, masked\_12, masked\_10, masked\_8;

864

865 masked\_24 = [ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5))) & 0xFFFFFF00;

866 masked\_16 = masked\_24 & 0xFFFF0000;

867 masked\_12 = masked\_24 & 0xFFF00000;

868 masked\_10 = masked\_24 & 0xFFC00000;

869 masked\_8 = masked\_24 & 0xFF000000;

870

871 return masked\_8 == 0x0A000000 || /\* 10.0.0.0/8 \*/

872 masked\_10 == 0x64400000 || /\* 100.64.0.0/10 \*/

873 masked\_12 == 0xAC100000 || /\* 172.16.0.0/12 \*/

874 masked\_16 == 0xC0A80000 || /\* 192.168.0.0/16 \*/

875 masked\_24 == 0xC0000200 || /\* 192.0.2.0/24 \*/

876 masked\_24 == 0xC0336400 || /\* 192.51.100.0/24 \*/

877 masked\_24 == 0xCB007100; /\* 203.0.113.0/24 \*/

878}

879

[ 888](group__ip__4__6.md#ga75ffcc08e621c2d47d1ae043fce2acad)#define net\_ipaddr\_copy(dest, src) \

889 UNALIGNED\_PUT(UNALIGNED\_GET(src), dest)

890

[ 897](group__ip__4__6.md#gaf731738fb1761208739976d767736f87)static inline void [net\_ipv4\_addr\_copy\_raw](group__ip__4__6.md#gaf731738fb1761208739976d767736f87)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dest,

898 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src)

899{

900 [net\_ipaddr\_copy](group__ip__4__6.md#ga75ffcc08e621c2d47d1ae043fce2acad)((struct [in\_addr](structin__addr.md) \*)dest, (const struct [in\_addr](structin__addr.md) \*)src);

901}

902

[ 909](group__ip__4__6.md#ga4925e6f3734b8fc1d9cb1ca1a510b5f1)static inline void [net\_ipv6\_addr\_copy\_raw](group__ip__4__6.md#ga4925e6f3734b8fc1d9cb1ca1a510b5f1)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dest,

910 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src)

911{

912 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(dest, src, sizeof(struct [in6\_addr](structin6__addr.md)));

913}

914

[ 923](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)static inline bool [net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)(const struct [in\_addr](structin__addr.md) \*addr1,

924 const struct [in\_addr](structin__addr.md) \*addr2)

925{

926 return UNALIGNED\_GET(&addr1->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5)) == UNALIGNED\_GET(&addr2->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5));

927}

928

[ 937](group__ip__4__6.md#ga32ffb42c62169ac9b34a0faa7c7ffd12)static inline bool [net\_ipv4\_addr\_cmp\_raw](group__ip__4__6.md#ga32ffb42c62169ac9b34a0faa7c7ffd12)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1,

938 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2)

939{

940 return [net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)((const struct [in\_addr](structin__addr.md) \*)addr1,

941 (const struct [in\_addr](structin__addr.md) \*)addr2);

942}

943

[ 952](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)static inline bool [net\_ipv6\_addr\_cmp](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)(const struct [in6\_addr](structin6__addr.md) \*addr1,

953 const struct [in6\_addr](structin6__addr.md) \*addr2)

954{

955 return ![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(addr1, addr2, sizeof(struct [in6\_addr](structin6__addr.md)));

956}

957

[ 966](group__ip__4__6.md#gafbe40461a645cf11fc8b3a07e1d9156e)static inline bool [net\_ipv6\_addr\_cmp\_raw](group__ip__4__6.md#gafbe40461a645cf11fc8b3a07e1d9156e)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1,

967 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2)

968{

969 return [net\_ipv6\_addr\_cmp](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)((const struct [in6\_addr](structin6__addr.md) \*)addr1,

970 (const struct [in6\_addr](structin6__addr.md) \*)addr2);

971}

972

[ 980](group__ip__4__6.md#gacac4279ee8896ddf2a76c612b36edf38)static inline bool [net\_ipv6\_is\_ll\_addr](group__ip__4__6.md#gacac4279ee8896ddf2a76c612b36edf38)(const struct [in6\_addr](structin6__addr.md) \*addr)

981{

982 return UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[0]) == [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(0xFE80);

983}

984

[ 992](group__ip__4__6.md#ga675d016e405e02882fda701aa8617ab7)static inline bool [net\_ipv6\_is\_sl\_addr](group__ip__4__6.md#ga675d016e405e02882fda701aa8617ab7)(const struct [in6\_addr](structin6__addr.md) \*addr)

993{

994 return UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[0]) == [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(0xFEC0);

995}

996

997

[ 1005](group__ip__4__6.md#gae10578b8801d213482de7d7d7e7ba230)static inline bool [net\_ipv6\_is\_ula\_addr](group__ip__4__6.md#gae10578b8801d213482de7d7d7e7ba230)(const struct [in6\_addr](structin6__addr.md) \*addr)

1006{

1007 return addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xFD;

1008}

1009

[ 1017](group__ip__4__6.md#gab2d854e2b24f866839e547c1092ccff6)static inline bool [net\_ipv6\_is\_global\_addr](group__ip__4__6.md#gab2d854e2b24f866839e547c1092ccff6)(const struct [in6\_addr](structin6__addr.md) \*addr)

1018{

1019 return (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] & 0xE0) == 0x20;

1020}

1021

[ 1031](group__ip__4__6.md#gad35da6e137d62231052dda63c68b7eff)static inline bool [net\_ipv6\_is\_private\_addr](group__ip__4__6.md#gad35da6e137d62231052dda63c68b7eff)(const struct [in6\_addr](structin6__addr.md) \*addr)

1032{

1033 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) masked\_32, masked\_7;

1034

1035 masked\_32 = [ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]));

1036 masked\_7 = masked\_32 & 0xfc000000;

1037

1038 return masked\_32 == 0x20010db8 || /\* 2001:db8::/32 \*/

1039 masked\_7 == 0xfc000000; /\* fc00::/7 \*/

1040}

1041

[ 1047](group__ip__4__6.md#gab0211c91e113cf01a8a16b1a106e7290)const struct [in6\_addr](structin6__addr.md) \*[net\_ipv6\_unspecified\_address](group__ip__4__6.md#gab0211c91e113cf01a8a16b1a106e7290)(void);

1048

[ 1054](group__ip__4__6.md#gaceb9afdd7f2f78d96e6debd72f63ebf0)const struct [in\_addr](structin__addr.md) \*[net\_ipv4\_unspecified\_address](group__ip__4__6.md#gaceb9afdd7f2f78d96e6debd72f63ebf0)(void);

1055

[ 1061](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113)const struct [in\_addr](structin__addr.md) \*[net\_ipv4\_broadcast\_address](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113)(void);

1062

1063struct [net\_if](structnet__if.md);

[ 1064](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea)extern bool [net\_if\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea)(struct [net\_if](structnet__if.md) \*iface,

1065 const struct [in\_addr](structin__addr.md) \*addr);

1066

[ 1076](group__ip__4__6.md#ga715455ec5e8041c5d7075fa6913674cd)static inline bool [net\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga715455ec5e8041c5d7075fa6913674cd)(struct [net\_if](structnet__if.md) \*iface,

1077 const struct [in\_addr](structin__addr.md) \*addr)

1078{

1079 return [net\_if\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea)(iface, addr);

1080}

1081

[ 1082](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf)extern bool [net\_if\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf)(struct [net\_if](structnet__if.md) \*iface,

1083 const struct [in\_addr](structin__addr.md) \*addr);

1084

1093#if defined(CONFIG\_NET\_NATIVE\_IPV4)

1094static inline bool [net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)(struct [net\_if](structnet__if.md) \*iface,

1095 const struct [in\_addr](structin__addr.md) \*addr)

1096{

1097 if ([net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)(addr, [net\_ipv4\_broadcast\_address](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113)())) {

1098 return true;

1099 }

1100

1101 return [net\_if\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf)(iface, addr);

1102}

1103#else

[ 1104](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)static inline bool [net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)(struct [net\_if](structnet__if.md) \*iface,

1105 const struct [in\_addr](structin__addr.md) \*addr)

1106{

1107 ARG\_UNUSED(iface);

1108 ARG\_UNUSED(addr);

1109

1110 return false;

1111}

1112#endif

1113

[ 1114](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53)extern struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv4\_addr\_lookup](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53)(const struct [in\_addr](structin__addr.md) \*addr,

1115 struct [net\_if](structnet__if.md) \*\*iface);

1116

[ 1126](group__ip__4__6.md#ga3db2a1fca0b525a7202277700b987eb9)static inline bool [net\_ipv4\_is\_my\_addr](group__ip__4__6.md#ga3db2a1fca0b525a7202277700b987eb9)(const struct [in\_addr](structin__addr.md) \*addr)

1127{

1128 bool ret;

1129

1130 ret = [net\_if\_ipv4\_addr\_lookup](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53)(addr, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1131 if (!ret) {

1132 ret = [net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)([NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), addr);

1133 }

1134

1135 return ret;

1136}

1137

[ 1145](group__ip__4__6.md#gafe2c8dc0bdb677ba9bc872d051aab2a0)static inline bool [net\_ipv6\_is\_addr\_unspecified](group__ip__4__6.md#gafe2c8dc0bdb677ba9bc872d051aab2a0)(const struct [in6\_addr](structin6__addr.md) \*addr)

1146{

1147 return UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]) == 0 &&

1148 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == 0 &&

1149 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]) == 0 &&

1150 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3]) == 0;

1151}

1152

[ 1161](group__ip__4__6.md#ga5a334819f4e4bf87aea5caa7ef28c68a)static inline bool [net\_ipv6\_is\_addr\_solicited\_node](group__ip__4__6.md#ga5a334819f4e4bf87aea5caa7ef28c68a)(const struct [in6\_addr](structin6__addr.md) \*addr)

1162{

1163 return UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]) == [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0xff020000) &&

1164 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == 0x00000000 &&

1165 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]) == [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0x00000001) &&

1166 ((UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3]) & [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0xff000000)) ==

1167 [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0xff000000));

1168}

1169

[ 1180](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)static inline bool [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(const struct [in6\_addr](structin6__addr.md) \*addr,

1181 int scope)

1182{

1183 return (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xff) && ((addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[1] & 0xF) == scope);

1184}

1185

[ 1195](group__ip__4__6.md#ga3f80a84f330a31aaa875fdea64dc18ec)static inline bool [net\_ipv6\_is\_same\_mcast\_scope](group__ip__4__6.md#ga3f80a84f330a31aaa875fdea64dc18ec)(const struct [in6\_addr](structin6__addr.md) \*addr\_1,

1196 const struct [in6\_addr](structin6__addr.md) \*addr\_2)

1197{

1198 return (addr\_1->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xff) && (addr\_2->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xff) &&

1199 (addr\_1->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[1] == addr\_2->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[1]);

1200}

1201

[ 1209](group__ip__4__6.md#ga55d67d4349dd354a7254a2f8e8320693)static inline bool [net\_ipv6\_is\_addr\_mcast\_global](group__ip__4__6.md#ga55d67d4349dd354a7254a2f8e8320693)(const struct [in6\_addr](structin6__addr.md) \*addr)

1210{

1211 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x0e);

1212}

1213

[ 1223](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)static inline bool [net\_ipv6\_is\_addr\_mcast\_iface](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)(const struct [in6\_addr](structin6__addr.md) \*addr)

1224{

1225 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x01);

1226}

1227

[ 1237](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)static inline bool [net\_ipv6\_is\_addr\_mcast\_link](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)(const struct [in6\_addr](structin6__addr.md) \*addr)

1238{

1239 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x02);

1240}

1241

[ 1251](group__ip__4__6.md#ga497a148717c1c1095abeb4482566dda0)static inline bool [net\_ipv6\_is\_addr\_mcast\_mesh](group__ip__4__6.md#ga497a148717c1c1095abeb4482566dda0)(const struct [in6\_addr](structin6__addr.md) \*addr)

1252{

1253 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x03);

1254}

1255

[ 1265](group__ip__4__6.md#ga6704146124a14be9cf2a636947c35a00)static inline bool [net\_ipv6\_is\_addr\_mcast\_site](group__ip__4__6.md#ga6704146124a14be9cf2a636947c35a00)(const struct [in6\_addr](structin6__addr.md) \*addr)

1266{

1267 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x05);

1268}

1269

[ 1279](group__ip__4__6.md#ga141ed5de3043dd7d6b45098aea38a4b1)static inline bool [net\_ipv6\_is\_addr\_mcast\_org](group__ip__4__6.md#ga141ed5de3043dd7d6b45098aea38a4b1)(const struct [in6\_addr](structin6__addr.md) \*addr)

1280{

1281 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x08);

1282}

1283

[ 1294](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0)static inline bool [net\_ipv6\_is\_addr\_mcast\_group](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0)(const struct [in6\_addr](structin6__addr.md) \*addr,

1295 const struct [in6\_addr](structin6__addr.md) \*[group](structgroup.md))

1296{

1297 return UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[1]) == [group](structgroup.md)->s6\_addr16[1] &&

1298 UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[2]) == [group](structgroup.md)->s6\_addr16[2] &&

1299 UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[3]) == [group](structgroup.md)->s6\_addr16[3] &&

1300 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == [group](structgroup.md)->s6\_addr32[1] &&

1301 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]) == [group](structgroup.md)->s6\_addr32[1] &&

1302 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3]) == [group](structgroup.md)->s6\_addr32[3];

1303}

1304

1313static inline bool

[ 1314](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)[net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)(const struct [in6\_addr](structin6__addr.md) \*addr)

1315{

1316 static const struct [in6\_addr](structin6__addr.md) all\_nodes\_mcast\_group = {

1317 { { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,

1318 0x00, 0x00, 0x00, 0x00, 0x00, 0x01 } }

1319 };

1320

1321 return [net\_ipv6\_is\_addr\_mcast\_group](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0)(addr, &all\_nodes\_mcast\_group);

1322}

1323

1333static inline bool

[ 1334](group__ip__4__6.md#ga35bdad7c958f1ea656680000ee3f6bfd)[net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes](group__ip__4__6.md#ga35bdad7c958f1ea656680000ee3f6bfd)(const struct [in6\_addr](structin6__addr.md) \*addr)

1335{

1336 return [net\_ipv6\_is\_addr\_mcast\_iface](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)(addr) &&

1337 [net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)(addr);

1338}

1339

1349static inline bool

[ 1350](group__ip__4__6.md#gaba3e1259f452381ef3e109bb2eb34c09)[net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes](group__ip__4__6.md#gaba3e1259f452381ef3e109bb2eb34c09)(const struct [in6\_addr](structin6__addr.md) \*addr)

1351{

1352 return [net\_ipv6\_is\_addr\_mcast\_link](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)(addr) &&

1353 [net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)(addr);

1354}

1355

1363static inline

[ 1364](group__ip__4__6.md#ga6091a7406c136fcf480517cb969c9d90)void [net\_ipv6\_addr\_create\_solicited\_node](group__ip__4__6.md#ga6091a7406c136fcf480517cb969c9d90)(const struct [in6\_addr](structin6__addr.md) \*src,

1365 struct [in6\_addr](structin6__addr.md) \*dst)

1366{

1367 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] = 0xFF;

1368 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[1] = 0x02;

1369 UNALIGNED\_PUT(0, &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[1]);

1370 UNALIGNED\_PUT(0, &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[2]);

1371 UNALIGNED\_PUT(0, &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[3]);

1372 UNALIGNED\_PUT(0, &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[4]);

1373 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[10] = 0U;

1374 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] = 0x01;

1375 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] = 0xFF;

1376 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13] = src->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13];

1377 UNALIGNED\_PUT(UNALIGNED\_GET(&src->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[7]), &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[7]);

1378}

1379

[ 1392](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)static inline void [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)(struct [in6\_addr](structin6__addr.md) \*addr,

1393 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr0, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr1,

1394 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr2, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr3,

1395 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr4, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr5,

1396 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr6, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr7)

1397{

1398 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr0), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[0]);

1399 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr1), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[1]);

1400 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr2), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[2]);

1401 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr3), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[3]);

1402 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr4), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[4]);

1403 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr5), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[5]);

1404 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr6), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[6]);

1405 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr7), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[7]);

1406}

1407

[ 1413](group__ip__4__6.md#ga58cbba1c522815b1ce201b0377ffe0b2)static inline void [net\_ipv6\_addr\_create\_ll\_allnodes\_mcast](group__ip__4__6.md#ga58cbba1c522815b1ce201b0377ffe0b2)(struct [in6\_addr](structin6__addr.md) \*addr)

1414{

1415 [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)(addr, 0xff02, 0, 0, 0, 0, 0, 0, 0x0001);

1416}

1417

[ 1423](group__ip__4__6.md#ga30821f0a2c08b4b01b71d362e3a25de1)static inline void [net\_ipv6\_addr\_create\_ll\_allrouters\_mcast](group__ip__4__6.md#ga30821f0a2c08b4b01b71d362e3a25de1)(struct [in6\_addr](structin6__addr.md) \*addr)

1424{

1425 [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)(addr, 0xff02, 0, 0, 0, 0, 0, 0, 0x0002);

1426}

1427

[ 1434](group__ip__4__6.md#ga8c6162c6212051037a33477aab9fc55f)static inline void [net\_ipv6\_addr\_create\_v4\_mapped](group__ip__4__6.md#ga8c6162c6212051037a33477aab9fc55f)(const struct [in\_addr](structin__addr.md) \*addr4,

1435 struct [in6\_addr](structin6__addr.md) \*addr6)

1436{

1437 [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)(addr6, 0, 0, 0, 0, 0, 0xffff,

1438 [ntohs](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)(addr4->[s4\_addr16](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86)[0]),

1439 [ntohs](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)(addr4->[s4\_addr16](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86)[1]));

1440}

1441

[ 1450](group__ip__4__6.md#ga53c24abd635fb2bcb137584dbc8a9026)static inline bool [net\_ipv6\_addr\_is\_v4\_mapped](group__ip__4__6.md#ga53c24abd635fb2bcb137584dbc8a9026)(const struct [in6\_addr](structin6__addr.md) \*addr)

1451{

1452 if (UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]) == 0 &&

1453 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == 0 &&

1454 UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[5]) == 0xffff) {

1455 return true;

1456 }

1457

1458 return false;

1459}

1460

[ 1479](group__ip__4__6.md#ga876301e06196f2e543bf2ef8d41449be)int [net\_ipv6\_addr\_generate\_iid](group__ip__4__6.md#ga876301e06196f2e543bf2ef8d41449be)(struct [net\_if](structnet__if.md) \*iface,

1480 const struct [in6\_addr](structin6__addr.md) \*prefix,

1481 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*network\_id, size\_t network\_id\_len,

1482 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dad\_counter,

1483 struct [in6\_addr](structin6__addr.md) \*addr,

1484 struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr);

1485

[ 1492](group__ip__4__6.md#ga6d41f1de27e2e8fbb8f12925eba852b4)static inline void [net\_ipv6\_addr\_create\_iid](group__ip__4__6.md#ga6d41f1de27e2e8fbb8f12925eba852b4)(struct [in6\_addr](structin6__addr.md) \*addr,

1493 struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr)

1494{

1495 (void)[net\_ipv6\_addr\_generate\_iid](group__ip__4__6.md#ga876301e06196f2e543bf2ef8d41449be)([NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), 0, 0, addr, lladdr);

1496}

1497

[ 1503](group__ip__4__6.md#gaf4b0c30b926748625bd3c4c81d06ffc5)static inline bool [net\_ipv6\_addr\_based\_on\_ll](group__ip__4__6.md#gaf4b0c30b926748625bd3c4c81d06ffc5)(const struct [in6\_addr](structin6__addr.md) \*addr,

1504 const struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr)

1505{

1506 if (!addr || !lladdr) {

1507 return false;

1508 }

1509

1510 switch (lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)) {

1511 case 2:

1512 if (![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[14], lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0), lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)) &&

1513 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] == 0U &&

1514 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[9] == 0U &&

1515 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[10] == 0U &&

1516 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] == 0xff &&

1517 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] == 0xfe) {

1518 return true;

1519 }

1520

1521 break;

1522 case 6:

1523 if (lladdr->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) == [NET\_LINK\_ETHERNET](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)) {

1524 if (![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[9], &lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[1], 2) &&

1525 ![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13], &lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[3], 3) &&

1526 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] == 0xff &&

1527 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] == 0xfe &&

1528 (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] ^ 0x02) == lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[0]) {

1529 return true;

1530 }

1531 }

1532

1533 break;

1534 case 8:

1535 if (![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[9], &lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[1],

1536 lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) - 1) &&

1537 (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] ^ 0x02) == lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[0]) {

1538 return true;

1539 }

1540

1541 break;

1542 }

1543

1544 return false;

1545}

1546

[ 1555](group__ip__4__6.md#gad97b2c3da722409eada099f9b7e13f03)static inline struct [sockaddr\_in6](structsockaddr__in6.md) \*[net\_sin6](group__ip__4__6.md#gad97b2c3da722409eada099f9b7e13f03)(const struct [sockaddr](structsockaddr.md) \*addr)

1556{

1557 return (struct [sockaddr\_in6](structsockaddr__in6.md) \*)addr;

1558}

1559

[ 1568](group__ip__4__6.md#gacccfbac6a03480840fa219e9a1924dc6)static inline struct [sockaddr\_in](structsockaddr__in.md) \*[net\_sin](group__ip__4__6.md#gacccfbac6a03480840fa219e9a1924dc6)(const struct [sockaddr](structsockaddr.md) \*addr)

1569{

1570 return (struct [sockaddr\_in](structsockaddr__in.md) \*)addr;

1571}

1572

1581static inline

[ 1582](group__ip__4__6.md#gae86d2cd402142190e1ea1c120a57939f)struct sockaddr\_in6\_ptr \*[net\_sin6\_ptr](group__ip__4__6.md#gae86d2cd402142190e1ea1c120a57939f)(const struct sockaddr\_ptr \*addr)

1583{

1584 return (struct sockaddr\_in6\_ptr \*)addr;

1585}

1586

1595static inline

[ 1596](group__ip__4__6.md#ga4b948e84590081a8aed2a63496e57ae2)struct sockaddr\_in\_ptr \*[net\_sin\_ptr](group__ip__4__6.md#ga4b948e84590081a8aed2a63496e57ae2)(const struct sockaddr\_ptr \*addr)

1597{

1598 return (struct sockaddr\_in\_ptr \*)addr;

1599}

1600

1609static inline

[ 1610](group__ip__4__6.md#gad5cf206e18769a15f9fc917e416db6ee)struct sockaddr\_ll\_ptr \*[net\_sll\_ptr](group__ip__4__6.md#gad5cf206e18769a15f9fc917e416db6ee)(const struct sockaddr\_ptr \*addr)

1611{

1612 return (struct sockaddr\_ll\_ptr \*)addr;

1613}

1614

1623static inline

[ 1624](group__ip__4__6.md#gac2fb590a35961c04807dd985f462c5fb)struct sockaddr\_can\_ptr \*[net\_can\_ptr](group__ip__4__6.md#gac2fb590a35961c04807dd985f462c5fb)(const struct sockaddr\_ptr \*addr)

1625{

1626 return (struct sockaddr\_can\_ptr \*)addr;

1627}

1628

[ 1642](group__ip__4__6.md#ga264b3c0a13493eac291ddc85d0b4d43d)\_\_syscall int [net\_addr\_pton](group__ip__4__6.md#ga264b3c0a13493eac291ddc85d0b4d43d)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst);

1643

[ 1655](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)\_\_syscall char \*[net\_addr\_ntop](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src,

1656 char \*dst, size\_t size);

1657

[ 1679](group__ip__4__6.md#ga9918e156f0039cf45d487a112e0a2ada)bool [net\_ipaddr\_parse](group__ip__4__6.md#ga9918e156f0039cf45d487a112e0a2ada)(const char \*str, size\_t str\_len,

1680 struct [sockaddr](structsockaddr.md) \*addr);

1681

[ 1691](group__ip__4__6.md#gaa2354e12d310c0647a98c873c7b7e5ad)int [net\_port\_set\_default](group__ip__4__6.md#gaa2354e12d310c0647a98c873c7b7e5ad)(struct [sockaddr](structsockaddr.md) \*addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) default\_port);

1692

[ 1704](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [net\_tcp\_seq\_cmp](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq2)

1705{

1706 return ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(seq1 - seq2);

1707}

1708

[ 1719](group__ip__4__6.md#gaa77b299f53e5535ac4c4bea1b6531a34)static inline bool [net\_tcp\_seq\_greater](group__ip__4__6.md#gaa77b299f53e5535ac4c4bea1b6531a34)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq2)

1720{

1721 return [net\_tcp\_seq\_cmp](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f)(seq1, seq2) > 0;

1722}

1723

[ 1735](group__ip__4__6.md#ga8b794f251cf8412c769ab415902a9f32)int [net\_bytes\_from\_str](group__ip__4__6.md#ga8b794f251cf8412c769ab415902a9f32)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, int buf\_len, const char \*src);

1736

[ 1745](group__ip__4__6.md#gae74c9ba7ff4addbce7f931bd6fa91fa0)int [net\_tx\_priority2tc](group__ip__4__6.md#gae74c9ba7ff4addbce7f931bd6fa91fa0)(enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) prio);

1746

[ 1755](group__ip__4__6.md#ga7b3c41ae9b3962090d72c130a9fa61b1)int [net\_rx\_priority2tc](group__ip__4__6.md#ga7b3c41ae9b3962090d72c130a9fa61b1)(enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) prio);

1756

[ 1765](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4)static inline enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) [net\_vlan2priority](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

1766{

1767 /\* Map according to IEEE 802.1Q \*/

1768 static const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vlan2priority[] = {

1769 [NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce),

1770 [NET\_PRIORITY\_BK](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b),

1771 [NET\_PRIORITY\_EE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0),

1772 [NET\_PRIORITY\_CA](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354),

1773 [NET\_PRIORITY\_VI](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792),

1774 [NET\_PRIORITY\_VO](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a),

1775 [NET\_PRIORITY\_IC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05),

1776 [NET\_PRIORITY\_NC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef)

1777 };

1778

1779 if (priority >= [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(vlan2priority)) {

1780 /\* Use Best Effort as the default priority \*/

1781 return [NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce);

1782 }

1783

1784 return (enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd))vlan2priority[priority];

1785}

1786

[ 1794](group__ip__4__6.md#ga8be77d043d4d1d29e0879b3b22274629)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_priority2vlan](group__ip__4__6.md#ga8be77d043d4d1d29e0879b3b22274629)(enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) priority)

1795{

1796 /\* The conversion works both ways \*/

1797 return ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))[net\_vlan2priority](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4)(priority);

1798}

1799

[ 1808](group__ip__4__6.md#gaba4c72e3aa2ceb4ac67d25112fb36523)const char \*[net\_family2str](group__ip__4__6.md#gaba4c72e3aa2ceb4ac67d25112fb36523)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family);

1809

1820#if defined(CONFIG\_NET\_IPV6\_PE)

1821int [net\_ipv6\_pe\_add\_filter](group__ip__4__6.md#ga14f9607f6c18869e7755ab497ff62147)(struct [in6\_addr](structin6__addr.md) \*addr, bool is\_denylist);

1822#else

[ 1823](group__ip__4__6.md#ga14f9607f6c18869e7755ab497ff62147)static inline int [net\_ipv6\_pe\_add\_filter](group__ip__4__6.md#ga14f9607f6c18869e7755ab497ff62147)(struct [in6\_addr](structin6__addr.md) \*addr,

1824 bool is\_denylist)

1825{

1826 ARG\_UNUSED(addr);

1827 ARG\_UNUSED(is\_denylist);

1828

1829 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1830}

1831#endif /\* CONFIG\_NET\_IPV6\_PE \*/

1832

1840#if defined(CONFIG\_NET\_IPV6\_PE)

1841int [net\_ipv6\_pe\_del\_filter](group__ip__4__6.md#ga76e7787a18dbf0b3575d46f81603f65a)(struct [in6\_addr](structin6__addr.md) \*addr);

1842#else

[ 1843](group__ip__4__6.md#ga76e7787a18dbf0b3575d46f81603f65a)static inline int [net\_ipv6\_pe\_del\_filter](group__ip__4__6.md#ga76e7787a18dbf0b3575d46f81603f65a)(struct [in6\_addr](structin6__addr.md) \*addr)

1844{

1845 ARG\_UNUSED(addr);

1846

1847 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1848}

1849#endif /\* CONFIG\_NET\_IPV6\_PE \*/

1850

1851#ifdef \_\_cplusplus

1852}

1853#endif

1854

1855#include <zephyr/syscalls/net\_ip.h>

1856

1860

1861

1862#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_IP\_H\_ \*/

[net\_ipv6\_is\_my\_addr](group__ip__4__6.md#ga00853528daf79c947dcdc320035ed538)

static bool net\_ipv6\_is\_my\_addr(struct in6\_addr \*addr)

Check if IPv6 address is found in one of the network interfaces.

**Definition** net\_ip.h:712

[net\_if\_ipv4\_addr\_lookup](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53)

struct net\_if\_addr \* net\_if\_ipv4\_addr\_lookup(const struct in\_addr \*addr, struct net\_if \*\*iface)

[net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)

static void net\_ipv6\_addr\_create(struct in6\_addr \*addr, uint16\_t addr0, uint16\_t addr1, uint16\_t addr2, uint16\_t addr3, uint16\_t addr4, uint16\_t addr5, uint16\_t addr6, uint16\_t addr7)

Construct an IPv6 address from eight 16-bit words.

**Definition** net\_ip.h:1392

[net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)

static bool net\_ipv4\_addr\_cmp(const struct in\_addr \*addr1, const struct in\_addr \*addr2)

Compare two IPv4 addresses.

**Definition** net\_ip.h:923

[NET\_IPV4\_ADDR\_SIZE](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)

#define NET\_IPV4\_ADDR\_SIZE

Binary size of the IPv4 address.

**Definition** net\_ip.h:165

[net\_if\_ipv6\_addr\_lookup](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb)

struct net\_if\_addr \* net\_if\_ipv6\_addr\_lookup(const struct in6\_addr \*addr, struct net\_if \*\*iface)

[net\_ipv6\_is\_addr\_mcast\_org](group__ip__4__6.md#ga141ed5de3043dd7d6b45098aea38a4b1)

static bool net\_ipv6\_is\_addr\_mcast\_org(const struct in6\_addr \*addr)

Check if the IPv6 address is an organization scope multicast address (FFx8::).

**Definition** net\_ip.h:1279

[net\_vlan2priority](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4)

static enum net\_priority net\_vlan2priority(uint8\_t priority)

Convert network packet VLAN priority to network packet priority so we can place the packet into corre...

**Definition** net\_ip.h:1765

[net\_ipv6\_pe\_add\_filter](group__ip__4__6.md#ga14f9607f6c18869e7755ab497ff62147)

static int net\_ipv6\_pe\_add\_filter(struct in6\_addr \*addr, bool is\_denylist)

Add IPv6 prefix as a privacy extension filter.

**Definition** net\_ip.h:1823

[net\_tcp\_seq\_cmp](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f)

static int32\_t net\_tcp\_seq\_cmp(uint32\_t seq1, uint32\_t seq2)

Compare TCP sequence numbers.

**Definition** net\_ip.h:1704

[net\_ipv6\_is\_addr\_mcast](group__ip__4__6.md#ga1a2fb0427eeab1a5dec6d69208ad7f02)

static bool net\_ipv6\_is\_addr\_mcast(const struct in6\_addr \*addr)

Check if the IPv6 address is a multicast address.

**Definition** net\_ip.h:694

[NET\_IPV6\_ADDR\_SIZE](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)

#define NET\_IPV6\_ADDR\_SIZE

Binary size of the IPv6 address.

**Definition** net\_ip.h:152

[net\_addr\_pton](group__ip__4__6.md#ga264b3c0a13493eac291ddc85d0b4d43d)

int net\_addr\_pton(sa\_family\_t family, const char \*src, void \*dst)

Convert a string to IP address.

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:168

[net\_ipv6\_addr\_create\_ll\_allrouters\_mcast](group__ip__4__6.md#ga30821f0a2c08b4b01b71d362e3a25de1)

static void net\_ipv6\_addr\_create\_ll\_allrouters\_mcast(struct in6\_addr \*addr)

Create link local allrouters multicast IPv6 address.

**Definition** net\_ip.h:1423

[net\_addr\_ntop](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)

char \* net\_addr\_ntop(sa\_family\_t family, const void \*src, char \*dst, size\_t size)

Convert IP address to string form.

[net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d)

net\_addr\_state

What is the current state of the network address.

**Definition** net\_ip.h:526

[net\_ipv4\_addr\_cmp\_raw](group__ip__4__6.md#ga32ffb42c62169ac9b34a0faa7c7ffd12)

static bool net\_ipv4\_addr\_cmp\_raw(const uint8\_t \*addr1, const uint8\_t \*addr2)

Compare two raw IPv4 address buffers.

**Definition** net\_ip.h:937

[net\_ipv6\_addr\_cmp](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)

static bool net\_ipv6\_addr\_cmp(const struct in6\_addr \*addr1, const struct in6\_addr \*addr2)

Compare two IPv6 addresses.

**Definition** net\_ip.h:952

[net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes](group__ip__4__6.md#ga35bdad7c958f1ea656680000ee3f6bfd)

static bool net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes(const struct in6\_addr \*addr)

Check if the IPv6 address is a interface scope all nodes multicast address (FF01::1).

**Definition** net\_ip.h:1334

[net\_ipv4\_is\_my\_addr](group__ip__4__6.md#ga3db2a1fca0b525a7202277700b987eb9)

static bool net\_ipv4\_is\_my\_addr(const struct in\_addr \*addr)

Check if the IPv4 address is assigned to any network interface in the system.

**Definition** net\_ip.h:1126

[net\_ipv6\_is\_same\_mcast\_scope](group__ip__4__6.md#ga3f80a84f330a31aaa875fdea64dc18ec)

static bool net\_ipv6\_is\_same\_mcast\_scope(const struct in6\_addr \*addr\_1, const struct in6\_addr \*addr\_2)

Check if the IPv6 addresses have the same multicast scope (FFyx::).

**Definition** net\_ip.h:1195

[net\_ipv6\_addr\_copy\_raw](group__ip__4__6.md#ga4925e6f3734b8fc1d9cb1ca1a510b5f1)

static void net\_ipv6\_addr\_copy\_raw(uint8\_t \*dest, const uint8\_t \*src)

Copy an IPv6 address raw buffer.

**Definition** net\_ip.h:909

[net\_ipv6\_is\_addr\_mcast\_mesh](group__ip__4__6.md#ga497a148717c1c1095abeb4482566dda0)

static bool net\_ipv6\_is\_addr\_mcast\_mesh(const struct in6\_addr \*addr)

Check if the IPv6 address is a mesh-local scope multicast address (FFx3::).

**Definition** net\_ip.h:1251

[net\_sin\_ptr](group__ip__4__6.md#ga4b948e84590081a8aed2a63496e57ae2)

static struct sockaddr\_in\_ptr \* net\_sin\_ptr(const struct sockaddr\_ptr \*addr)

Get sockaddr\_in\_ptr from sockaddr\_ptr.

**Definition** net\_ip.h:1596

[net\_ipv4\_broadcast\_address](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113)

const struct in\_addr \* net\_ipv4\_broadcast\_address(void)

Return pointer to broadcast (all bits ones) IPv4 address.

[net\_ipv6\_addr\_prefix\_mask](group__ip__4__6.md#ga4e91a4298604a916731bf591acc7b326)

static void net\_ipv6\_addr\_prefix\_mask(const uint8\_t \*inaddr, uint8\_t \*outaddr, uint8\_t prefix\_len)

Get the IPv6 network address via the unicast address and the prefix mask.

**Definition** net\_ip.h:780

[htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)

#define htons(x)

Convert 16-bit value from host to network byte order.

**Definition** net\_ip.h:124

[net\_ipv6\_addr\_is\_v4\_mapped](group__ip__4__6.md#ga53c24abd635fb2bcb137584dbc8a9026)

static bool net\_ipv6\_addr\_is\_v4\_mapped(const struct in6\_addr \*addr)

Is the IPv6 address an IPv4 mapped one.

**Definition** net\_ip.h:1450

[net\_if\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea)

bool net\_if\_ipv4\_addr\_mask\_cmp(struct net\_if \*iface, const struct in\_addr \*addr)

[net\_ipv6\_is\_addr\_mcast\_global](group__ip__4__6.md#ga55d67d4349dd354a7254a2f8e8320693)

static bool net\_ipv6\_is\_addr\_mcast\_global(const struct in6\_addr \*addr)

Check if the IPv6 address is a global multicast address (FFxE::/16).

**Definition** net\_ip.h:1209

[net\_ipv6\_addr\_create\_ll\_allnodes\_mcast](group__ip__4__6.md#ga58cbba1c522815b1ce201b0377ffe0b2)

static void net\_ipv6\_addr\_create\_ll\_allnodes\_mcast(struct in6\_addr \*addr)

Create link local allnodes multicast IPv6 address.

**Definition** net\_ip.h:1413

[net\_ipv6\_is\_addr\_solicited\_node](group__ip__4__6.md#ga5a334819f4e4bf87aea5caa7ef28c68a)

static bool net\_ipv6\_is\_addr\_solicited\_node(const struct in6\_addr \*addr)

Check if the IPv6 address is solicited node multicast address FF02:0:0:0:0:1:FFXX:XXXX defined in RFC...

**Definition** net\_ip.h:1161

[net\_ipv6\_addr\_create\_solicited\_node](group__ip__4__6.md#ga6091a7406c136fcf480517cb969c9d90)

static void net\_ipv6\_addr\_create\_solicited\_node(const struct in6\_addr \*src, struct in6\_addr \*dst)

Create solicited node IPv6 multicast address FF02:0:0:0:0:1:FFXX:XXXX defined in RFC 3513.

**Definition** net\_ip.h:1364

[net\_ipv6\_is\_addr\_mcast\_group](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0)

static bool net\_ipv6\_is\_addr\_mcast\_group(const struct in6\_addr \*addr, const struct in6\_addr \*group)

Check if the IPv6 address belongs to certain multicast group.

**Definition** net\_ip.h:1294

[net\_ipv6\_is\_addr\_mcast\_site](group__ip__4__6.md#ga6704146124a14be9cf2a636947c35a00)

static bool net\_ipv6\_is\_addr\_mcast\_site(const struct in6\_addr \*addr)

Check if the IPv6 address is a site scope multicast address (FFx5::).

**Definition** net\_ip.h:1265

[net\_ipv6\_is\_sl\_addr](group__ip__4__6.md#ga675d016e405e02882fda701aa8617ab7)

static bool net\_ipv6\_is\_sl\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a site local address.

**Definition** net\_ip.h:992

[net\_ipv6\_addr\_create\_iid](group__ip__4__6.md#ga6d41f1de27e2e8fbb8f12925eba852b4)

static void net\_ipv6\_addr\_create\_iid(struct in6\_addr \*addr, struct net\_linkaddr \*lladdr)

Create IPv6 address interface identifier.

**Definition** net\_ip.h:1492

[net\_ipv4\_is\_private\_addr](group__ip__4__6.md#ga6f19cb74de130d70668599c05a5ed66b)

static bool net\_ipv4\_is\_private\_addr(const struct in\_addr \*addr)

Check if the given IPv4 address is from a private address range.

**Definition** net\_ip.h:861

[net\_ipv6\_is\_addr\_mcast\_link](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)

static bool net\_ipv6\_is\_addr\_mcast\_link(const struct in6\_addr \*addr)

Check if the IPv6 address is a link local scope multicast address (FFx2::).

**Definition** net\_ip.h:1237

[net\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga715455ec5e8041c5d7075fa6913674cd)

static bool net\_ipv4\_addr\_mask\_cmp(struct net\_if \*iface, const struct in\_addr \*addr)

Check if the given address belongs to same subnet that has been configured for the interface.

**Definition** net\_ip.h:1076

[net\_ip\_protocol\_secure](group__ip__4__6.md#ga721da18d2a3cfd9b3a56e9efc9f6e58b)

net\_ip\_protocol\_secure

Protocol numbers for TLS protocols.

**Definition** net\_ip.h:78

[net\_ipaddr\_copy](group__ip__4__6.md#ga75ffcc08e621c2d47d1ae043fce2acad)

#define net\_ipaddr\_copy(dest, src)

Copy an IPv4 or IPv6 address.

**Definition** net\_ip.h:888

[net\_ipv6\_pe\_del\_filter](group__ip__4__6.md#ga76e7787a18dbf0b3575d46f81603f65a)

static int net\_ipv6\_pe\_del\_filter(struct in6\_addr \*addr)

Delete IPv6 prefix from privacy extension filter list.

**Definition** net\_ip.h:1843

[net\_ip\_mtu](group__ip__4__6.md#ga7a207761e4879c140f48f93978cb2f0b)

net\_ip\_mtu

IP Maximum Transfer Unit.

**Definition** net\_ip.h:486

[net\_rx\_priority2tc](group__ip__4__6.md#ga7b3c41ae9b3962090d72c130a9fa61b1)

int net\_rx\_priority2tc(enum net\_priority prio)

Convert Rx network packet priority to traffic class so we can place the packet into correct Rx queue.

[net\_ipv6\_addr\_generate\_iid](group__ip__4__6.md#ga876301e06196f2e543bf2ef8d41449be)

int net\_ipv6\_addr\_generate\_iid(struct net\_if \*iface, const struct in6\_addr \*prefix, uint8\_t \*network\_id, size\_t network\_id\_len, uint8\_t dad\_counter, struct in6\_addr \*addr, struct net\_linkaddr \*lladdr)

Generate IPv6 address using a prefix and interface identifier.

[net\_ipv4\_is\_addr\_loopback](group__ip__4__6.md#ga879e4aed725d7ea3fe609fa989f14735)

static bool net\_ipv4\_is\_addr\_loopback(struct in\_addr \*addr)

Check if the IPv4 address is a loopback address (127.0.0.0/8).

**Definition** net\_ip.h:811

[net\_bytes\_from\_str](group__ip__4__6.md#ga8b794f251cf8412c769ab415902a9f32)

int net\_bytes\_from\_str(uint8\_t \*buf, int buf\_len, const char \*src)

Convert a string of hex values to array of bytes.

[net\_priority2vlan](group__ip__4__6.md#ga8be77d043d4d1d29e0879b3b22274629)

static uint8\_t net\_priority2vlan(enum net\_priority priority)

Convert network packet priority to network packet VLAN priority.

**Definition** net\_ip.h:1794

[net\_ipv6\_addr\_create\_v4\_mapped](group__ip__4__6.md#ga8c6162c6212051037a33477aab9fc55f)

static void net\_ipv6\_addr\_create\_v4\_mapped(const struct in\_addr \*addr4, struct in6\_addr \*addr6)

Create IPv4 mapped IPv6 address.

**Definition** net\_ip.h:1434

[net\_if\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf)

bool net\_if\_ipv4\_is\_addr\_bcast(struct net\_if \*iface, const struct in\_addr \*addr)

[net\_ipv6\_is\_prefix](group__ip__4__6.md#ga9654007b0a3c4d033df1ec3d00bd26ee)

static bool net\_ipv6\_is\_prefix(const uint8\_t \*addr1, const uint8\_t \*addr2, uint8\_t length)

Check if two IPv6 addresses are same when compared after prefix mask.

**Definition** net\_ip.h:742

[net\_ipaddr\_parse](group__ip__4__6.md#ga9918e156f0039cf45d487a112e0a2ada)

bool net\_ipaddr\_parse(const char \*str, size\_t str\_len, struct sockaddr \*addr)

Parse a string that contains either IPv4 or IPv6 address and optional port, and store the information...

[net\_port\_set\_default](group__ip__4__6.md#gaa2354e12d310c0647a98c873c7b7e5ad)

int net\_port\_set\_default(struct sockaddr \*addr, uint16\_t default\_port)

Set the default port in the sockaddr structure.

[net\_ipv6\_is\_addr\_loopback](group__ip__4__6.md#gaa662667005bdc00bf1eb5cf243aad874)

static bool net\_ipv6\_is\_addr\_loopback(struct in6\_addr \*addr)

Check if the IPv6 address is a loopback address (::1).

**Definition** net\_ip.h:679

[net\_tcp\_seq\_greater](group__ip__4__6.md#gaa77b299f53e5535ac4c4bea1b6531a34)

static bool net\_tcp\_seq\_greater(uint32\_t seq1, uint32\_t seq2)

Check that one TCP sequence number is greater.

**Definition** net\_ip.h:1719

[net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c)

net\_sock\_type

Socket type.

**Definition** net\_ip.h:88

[net\_ipv6\_unspecified\_address](group__ip__4__6.md#gab0211c91e113cf01a8a16b1a106e7290)

const struct in6\_addr \* net\_ipv6\_unspecified\_address(void)

Return pointer to any (all bits zeros) IPv6 address.

[net\_ipv6\_is\_global\_addr](group__ip__4__6.md#gab2d854e2b24f866839e547c1092ccff6)

static bool net\_ipv6\_is\_global\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a global address.

**Definition** net\_ip.h:1017

[net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes](group__ip__4__6.md#gaba3e1259f452381ef3e109bb2eb34c09)

static bool net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes(const struct in6\_addr \*addr)

Check if the IPv6 address is a link local scope all nodes multicast address (FF02::1).

**Definition** net\_ip.h:1350

[net\_family2str](group__ip__4__6.md#gaba4c72e3aa2ceb4ac67d25112fb36523)

const char \* net\_family2str(sa\_family\_t family)

Return network address family value as a string.

[net\_ipv4\_is\_ll\_addr](group__ip__4__6.md#gac000a319de7a6f95d4a63719bca3b865)

static bool net\_ipv4\_is\_ll\_addr(const struct in\_addr \*addr)

Check if the given IPv4 address is a link local address.

**Definition** net\_ip.h:847

[net\_can\_ptr](group__ip__4__6.md#gac2fb590a35961c04807dd985f462c5fb)

static struct sockaddr\_can\_ptr \* net\_can\_ptr(const struct sockaddr\_ptr \*addr)

Get sockaddr\_can\_ptr from sockaddr\_ptr.

**Definition** net\_ip.h:1624

[ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)

#define ntohl(x)

Convert 32-bit value from network to host byte order.

**Definition** net\_ip.h:108

[net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)

static bool net\_ipv4\_is\_addr\_bcast(struct net\_if \*iface, const struct in\_addr \*addr)

Check if the given IPv4 address is a broadcast address.

**Definition** net\_ip.h:1104

[net\_ipv6\_is\_ll\_addr](group__ip__4__6.md#gacac4279ee8896ddf2a76c612b36edf38)

static bool net\_ipv6\_is\_ll\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a link local address.

**Definition** net\_ip.h:980

[net\_sin](group__ip__4__6.md#gacccfbac6a03480840fa219e9a1924dc6)

static struct sockaddr\_in \* net\_sin(const struct sockaddr \*addr)

Get sockaddr\_in from sockaddr.

**Definition** net\_ip.h:1568

[net\_ipv4\_unspecified\_address](group__ip__4__6.md#gaceb9afdd7f2f78d96e6debd72f63ebf0)

const struct in\_addr \* net\_ipv4\_unspecified\_address(void)

Return pointer to any (all bits zeros) IPv4 address.

[net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)

static bool net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group(const struct in6\_addr \*addr)

Check if the IPv6 address belongs to the all nodes multicast group.

**Definition** net\_ip.h:1314

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:172

[net\_ipv6\_is\_private\_addr](group__ip__4__6.md#gad35da6e137d62231052dda63c68b7eff)

static bool net\_ipv6\_is\_private\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is from a private/local address range.

**Definition** net\_ip.h:1031

[net\_sll\_ptr](group__ip__4__6.md#gad5cf206e18769a15f9fc917e416db6ee)

static struct sockaddr\_ll\_ptr \* net\_sll\_ptr(const struct sockaddr\_ptr \*addr)

Get sockaddr\_ll\_ptr from sockaddr\_ptr.

**Definition** net\_ip.h:1610

[net\_sin6](group__ip__4__6.md#gad97b2c3da722409eada099f9b7e13f03)

static struct sockaddr\_in6 \* net\_sin6(const struct sockaddr \*addr)

Get sockaddr\_in6 from sockaddr.

**Definition** net\_ip.h:1555

[ntohs](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)

#define ntohs(x)

Convert 16-bit value from network to host byte order.

**Definition** net\_ip.h:100

[net\_if\_ipv6\_maddr\_lookup](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975)

struct net\_if\_mcast\_addr \* net\_if\_ipv6\_maddr\_lookup(const struct in6\_addr \*addr, struct net\_if \*\*iface)

[net\_ipv4\_is\_addr\_unspecified](group__ip__4__6.md#gadc623ecacf024733ab6d477d87cc4b9d)

static bool net\_ipv4\_is\_addr\_unspecified(const struct in\_addr \*addr)

Check if the IPv4 address is unspecified (all bits zero).

**Definition** net\_ip.h:823

[net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)

static bool net\_ipv6\_is\_addr\_mcast\_scope(const struct in6\_addr \*addr, int scope)

Check if the IPv6 address is a given scope multicast address (FFyx::).

**Definition** net\_ip.h:1180

[net\_ipv6\_is\_ula\_addr](group__ip__4__6.md#gae10578b8801d213482de7d7d7e7ba230)

static bool net\_ipv6\_is\_ula\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a unique local address.

**Definition** net\_ip.h:1005

[net\_ipv6\_is\_addr\_mcast\_iface](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)

static bool net\_ipv6\_is\_addr\_mcast\_iface(const struct in6\_addr \*addr)

Check if the IPv6 address is a interface scope multicast address (FFx1::).

**Definition** net\_ip.h:1223

[htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)

#define htonl(x)

Convert 32-bit value from host to network byte order.

**Definition** net\_ip.h:132

[net\_tx\_priority2tc](group__ip__4__6.md#gae74c9ba7ff4addbce7f931bd6fa91fa0)

int net\_tx\_priority2tc(enum net\_priority prio)

Convert Tx network packet priority to traffic class so we can place the packet into correct Tx queue.

[net\_sin6\_ptr](group__ip__4__6.md#gae86d2cd402142190e1ea1c120a57939f)

static struct sockaddr\_in6\_ptr \* net\_sin6\_ptr(const struct sockaddr\_ptr \*addr)

Get sockaddr\_in6\_ptr from sockaddr\_ptr.

**Definition** net\_ip.h:1582

[net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd)

net\_priority

Network packet priority settings described in IEEE 802.1Q Annex I.1.

**Definition** net\_ip.h:503

[net\_ipv4\_is\_addr\_mcast](group__ip__4__6.md#gae8c3302cf9ca457de32eabcf65975b70)

static bool net\_ipv4\_is\_addr\_mcast(const struct in\_addr \*addr)

Check if the IPv4 address is a multicast address.

**Definition** net\_ip.h:835

[net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)

net\_ip\_protocol

Protocol numbers from IANA/BSD.

**Definition** net\_ip.h:64

[net\_ipv6\_addr\_based\_on\_ll](group__ip__4__6.md#gaf4b0c30b926748625bd3c4c81d06ffc5)

static bool net\_ipv6\_addr\_based\_on\_ll(const struct in6\_addr \*addr, const struct net\_linkaddr \*lladdr)

Check if given address is based on link layer address.

**Definition** net\_ip.h:1503

[net\_ipv4\_addr\_copy\_raw](group__ip__4__6.md#gaf731738fb1761208739976d767736f87)

static void net\_ipv4\_addr\_copy\_raw(uint8\_t \*dest, const uint8\_t \*src)

Copy an IPv4 address raw buffer.

**Definition** net\_ip.h:897

[net\_ipv6\_is\_my\_maddr](group__ip__4__6.md#gaf8c5158de9a65d840faa61bb3dec341c)

static bool net\_ipv6\_is\_my\_maddr(struct in6\_addr \*maddr)

Check if IPv6 multicast address is found in one of the network interfaces.

**Definition** net\_ip.h:728

[net\_ipv6\_addr\_cmp\_raw](group__ip__4__6.md#gafbe40461a645cf11fc8b3a07e1d9156e)

static bool net\_ipv6\_addr\_cmp\_raw(const uint8\_t \*addr1, const uint8\_t \*addr2)

Compare two raw IPv6 address buffers.

**Definition** net\_ip.h:966

[net\_ipv6\_is\_addr\_unspecified](group__ip__4__6.md#gafe2c8dc0bdb677ba9bc872d051aab2a0)

static bool net\_ipv6\_is\_addr\_unspecified(const struct in6\_addr \*addr)

Check if the IPv6 address is unspecified (all bits zero).

**Definition** net\_ip.h:1145

[net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41)

net\_addr\_type

How the network address is assigned to network interface.

**Definition** net\_ip.h:534

[NET\_ADDR\_ANY\_STATE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df)

@ NET\_ADDR\_ANY\_STATE

Default (invalid) address type.

**Definition** net\_ip.h:527

[NET\_ADDR\_TENTATIVE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9)

@ NET\_ADDR\_TENTATIVE

Tentative address.

**Definition** net\_ip.h:528

[NET\_ADDR\_DEPRECATED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3)

@ NET\_ADDR\_DEPRECATED

Deprecated address.

**Definition** net\_ip.h:530

[NET\_ADDR\_PREFERRED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a)

@ NET\_ADDR\_PREFERRED

Preferred address.

**Definition** net\_ip.h:529

[IPPROTO\_TLS\_1\_1](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba102692f9f57dd0ec6f8c6cb54a235d4c)

@ IPPROTO\_TLS\_1\_1

TLS 1.1 protocol.

**Definition** net\_ip.h:80

[IPPROTO\_TLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba6d479e64d940cea948c874d36c656fcc)

@ IPPROTO\_TLS\_1\_0

TLS 1.0 protocol.

**Definition** net\_ip.h:79

[IPPROTO\_DTLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba92e94005d7a80aacbffad2f3f10555ef)

@ IPPROTO\_DTLS\_1\_0

DTLS 1.0 protocol.

**Definition** net\_ip.h:83

[IPPROTO\_TLS\_1\_3](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa43bf0393de00897b350b361f97c85ac)

@ IPPROTO\_TLS\_1\_3

TLS 1.3 protocol.

**Definition** net\_ip.h:82

[IPPROTO\_TLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa5e176fa47ca23a6f25101a5203f8e5a)

@ IPPROTO\_TLS\_1\_2

TLS 1.2 protocol.

**Definition** net\_ip.h:81

[IPPROTO\_DTLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58bad4d2a6ca8756ee52221f19fb06c34a1c)

@ IPPROTO\_DTLS\_1\_2

DTLS 1.2 protocol.

**Definition** net\_ip.h:84

[NET\_IPV4\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1)

@ NET\_IPV4\_MTU

IPv4 MTU length.

**Definition** net\_ip.h:499

[NET\_IPV6\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c)

@ NET\_IPV6\_MTU

IPv6 MTU length.

**Definition** net\_ip.h:493

[SOCK\_DGRAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc)

@ SOCK\_DGRAM

Datagram socket type.

**Definition** net\_ip.h:90

[SOCK\_RAW](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231)

@ SOCK\_RAW

RAW socket type.

**Definition** net\_ip.h:91

[SOCK\_STREAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424)

@ SOCK\_STREAM

Stream socket type.

**Definition** net\_ip.h:89

[NET\_PRIORITY\_NC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef)

@ NET\_PRIORITY\_NC

Network control (highest).

**Definition** net\_ip.h:511

[NET\_PRIORITY\_IC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05)

@ NET\_PRIORITY\_IC

Internetwork control.

**Definition** net\_ip.h:510

[NET\_PRIORITY\_CA](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354)

@ NET\_PRIORITY\_CA

Critical applications.

**Definition** net\_ip.h:507

[NET\_PRIORITY\_VO](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a)

@ NET\_PRIORITY\_VO

Voice, < 10 ms latency and jitter.

**Definition** net\_ip.h:509

[NET\_PRIORITY\_VI](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792)

@ NET\_PRIORITY\_VI

Video, < 100 ms latency and jitter.

**Definition** net\_ip.h:508

[NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce)

@ NET\_PRIORITY\_BE

Best effort (default).

**Definition** net\_ip.h:505

[NET\_PRIORITY\_EE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0)

@ NET\_PRIORITY\_EE

Excellent effort.

**Definition** net\_ip.h:506

[NET\_PRIORITY\_BK](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b)

@ NET\_PRIORITY\_BK

Background (lowest).

**Definition** net\_ip.h:504

[IPPROTO\_IP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a334b0a4a5a3e331e7c7864471e9eab08)

@ IPPROTO\_IP

IP protocol (pseudo-val for setsockopt().

**Definition** net\_ip.h:65

[IPPROTO\_RAW](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a3f186705d5c21da1b72ecb91cca1f7a4)

@ IPPROTO\_RAW

RAW IP packets.

**Definition** net\_ip.h:74

[IPPROTO\_IPIP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a49a42f6d628bf65e78478e8eb4874ff2)

@ IPPROTO\_IPIP

IPIP tunnels.

**Definition** net\_ip.h:69

[IPPROTO\_TCP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4a3c433d15859f62bacc06312791a45e)

@ IPPROTO\_TCP

TCP protocol.

**Definition** net\_ip.h:70

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

**Definition** net\_ip.h:72

[IPPROTO\_ETH\_P\_ALL](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a8e42ac7edd78566fb827a482b671ac01)

@ IPPROTO\_ETH\_P\_ALL

Every packet.

**Definition** net\_ip.h:68

[IPPROTO\_UDP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31abd7dfb22e255a4eed332f41de12d7321)

@ IPPROTO\_UDP

UDP protocol.

**Definition** net\_ip.h:71

[IPPROTO\_ICMPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31aeeff57e3cf726718a92b2138e5842926)

@ IPPROTO\_ICMPV6

ICMPv6 protocol.

**Definition** net\_ip.h:73

[NET\_ADDR\_ANY](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6)

@ NET\_ADDR\_ANY

Default value.

**Definition** net\_ip.h:536

[NET\_ADDR\_OVERRIDABLE](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4)

@ NET\_ADDR\_OVERRIDABLE

Manually set address which is overridable by DHCP.

**Definition** net\_ip.h:544

[NET\_ADDR\_DHCP](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db)

@ NET\_ADDR\_DHCP

Address is from DHCP.

**Definition** net\_ip.h:540

[NET\_ADDR\_MANUAL](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e)

@ NET\_ADDR\_MANUAL

Manually set address.

**Definition** net\_ip.h:542

[NET\_ADDR\_AUTOCONF](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006)

@ NET\_ADDR\_AUTOCONF

Auto configured address.

**Definition** net\_ip.h:538

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

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[net\_linkaddr.h](net__linkaddr_8h.md)

Public API for network link address.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

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

**Definition** net\_ip.h:268

[cmsghdr::cmsg\_type](structcmsghdr.md#a4c7cabf7899a688ce10bc92773fca9c1)

int cmsg\_type

Protocol-specific type.

**Definition** net\_ip.h:271

[cmsghdr::cmsg\_len](structcmsghdr.md#a7cf479e5e162e65ad164616453d61df2)

socklen\_t cmsg\_len

Number of bytes, including header.

**Definition** net\_ip.h:269

[cmsghdr::cmsg\_data](structcmsghdr.md#a92c00d02575707f72c04f090b6f8d399)

z\_max\_align\_t cmsg\_data[]

Flexible array member to force alignment of cmsghdr.

**Definition** net\_ip.h:272

[cmsghdr::cmsg\_level](structcmsghdr.md#ac0ff1400cb63fbc2e0ece19434cb8fef)

int cmsg\_level

Originating protocol.

**Definition** net\_ip.h:270

[group](structgroup.md)

Group structure.

**Definition** grp.h:18

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:143

[in6\_addr::s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)

uint8\_t s6\_addr[16]

IPv6 address buffer.

**Definition** net\_ip.h:145

[in6\_addr::s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)

uint32\_t s6\_addr32[4]

In big endian.

**Definition** net\_ip.h:147

[in6\_addr::s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)

uint16\_t s6\_addr16[8]

In big endian.

**Definition** net\_ip.h:146

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:155

[in\_addr::s4\_addr](structin__addr.md#a4fd35e401c510fabab8979eb8416dd9b)

uint8\_t s4\_addr[4]

IPv4 address buffer.

**Definition** net\_ip.h:157

[in\_addr::s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5)

uint32\_t s\_addr

In big endian, for POSIX compatibility.

**Definition** net\_ip.h:160

[in\_addr::s4\_addr16](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86)

uint16\_t s4\_addr16[2]

In big endian.

**Definition** net\_ip.h:158

[in\_addr::s4\_addr32](structin__addr.md#ae4e092a27efb643067d7ce10bd454bed)

uint32\_t s4\_addr32[1]

In big endian.

**Definition** net\_ip.h:159

[iovec](structiovec.md)

IO vector array element.

**Definition** net\_ip.h:250

[iovec::iov\_base](structiovec.md#a07aeddeccf80f14520fdd7ef0759442b)

void \* iov\_base

Pointer to data.

**Definition** net\_ip.h:251

[iovec::iov\_len](structiovec.md#a17b5ac2078fd1adfabb262a95808a07d)

size\_t iov\_len

Length of the data.

**Definition** net\_ip.h:252

[msghdr](structmsghdr.md)

Message struct.

**Definition** net\_ip.h:257

[msghdr::msg\_iov](structmsghdr.md#a1b893a6f84c4ba52708c5dcfcc720293)

struct iovec \* msg\_iov

Scatter/gather array.

**Definition** net\_ip.h:260

[msghdr::msg\_namelen](structmsghdr.md#a47762b69eee1c9ba5736d64516ea0960)

socklen\_t msg\_namelen

Size of socket address.

**Definition** net\_ip.h:259

[msghdr::msg\_name](structmsghdr.md#a691a8866b21c7083974a2ff1e7987ce1)

void \* msg\_name

Optional socket address, big endian.

**Definition** net\_ip.h:258

[msghdr::msg\_flags](structmsghdr.md#a9e8ff97d402c99551cbfd564e9e10a74)

int msg\_flags

Flags on received message.

**Definition** net\_ip.h:264

[msghdr::msg\_controllen](structmsghdr.md#a9fa41b0e9a02b5dc9a01aa6f18108adb)

size\_t msg\_controllen

Ancillary data buffer len.

**Definition** net\_ip.h:263

[msghdr::msg\_iovlen](structmsghdr.md#ad4ef1bd6821e599bf42f936850d2c4d7)

size\_t msg\_iovlen

Number of elements in msg\_iov.

**Definition** net\_ip.h:261

[msghdr::msg\_control](structmsghdr.md#afba5fc31b0f197e25602d2232ca6d783)

void \* msg\_control

Ancillary data.

**Definition** net\_ip.h:262

[net\_if\_addr](structnet__if__addr.md)

Network Interface unicast IP addresses.

**Definition** net\_if.h:56

[net\_if\_config](structnet__if__config.md)

IP and other configuration related data for network interface.

**Definition** net\_if.h:585

[net\_if\_mcast\_addr](structnet__if__mcast__addr.md)

Network Interface multicast IP addresses.

**Definition** net\_if.h:160

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

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

**Definition** net\_ip.h:517

[net\_tuple::remote\_addr](structnet__tuple.md#a8f9a1aab3c3aedeead795ca6624d4d6d)

struct net\_addr \* remote\_addr

IPv6/IPv4 remote address.

**Definition** net\_ip.h:518

[net\_tuple::local\_port](structnet__tuple.md#a9a1cd0dd55a9e866cb0e910120362b7e)

uint16\_t local\_port

UDP/TCP local port.

**Definition** net\_ip.h:521

[net\_tuple::ip\_proto](structnet__tuple.md#aa9eeba2c8e263afbf6368e04353d6014)

enum net\_ip\_protocol ip\_proto

IP protocol.

**Definition** net\_ip.h:522

[net\_tuple::remote\_port](structnet__tuple.md#ab4c31093a23bc60d8dcf5b784e3fb39a)

uint16\_t remote\_port

UDP/TCP remote port.

**Definition** net\_ip.h:520

[net\_tuple::local\_addr](structnet__tuple.md#af7004f8f8d74d49d6771393825612294)

struct net\_addr \* local\_addr

IPv6/IPv4 local address.

**Definition** net\_ip.h:519

[sockaddr\_in6](structsockaddr__in6.md)

Socket address struct for IPv6.

**Definition** net\_ip.h:182

[sockaddr\_in6::sin6\_scope\_id](structsockaddr__in6.md#a1daad78c9848862ab33a48e05fa8cf17)

uint8\_t sin6\_scope\_id

Interfaces for a scope.

**Definition** net\_ip.h:186

[sockaddr\_in6::sin6\_addr](structsockaddr__in6.md#a219e7f3ecd6d7dcf8fc2465475be490f)

struct in6\_addr sin6\_addr

IPv6 address.

**Definition** net\_ip.h:185

[sockaddr\_in6::sin6\_port](structsockaddr__in6.md#a4fc2b7a478d258e9e778772701096022)

uint16\_t sin6\_port

Port number.

**Definition** net\_ip.h:184

[sockaddr\_in6::sin6\_family](structsockaddr__in6.md#aefa41e43be9c615f8cfd6266c0ed1687)

sa\_family\_t sin6\_family

AF\_INET6.

**Definition** net\_ip.h:183

[sockaddr\_in](structsockaddr__in.md)

Socket address struct for IPv4.

**Definition** net\_ip.h:190

[sockaddr\_in::sin\_port](structsockaddr__in.md#a3cf9239fdd8bd32855d66a4b86349fbb)

uint16\_t sin\_port

Port number.

**Definition** net\_ip.h:192

[sockaddr\_in::sin\_addr](structsockaddr__in.md#a4ea5f2f1138e5c8597097db255a9ec6c)

struct in\_addr sin\_addr

IPv4 address.

**Definition** net\_ip.h:193

[sockaddr\_in::sin\_family](structsockaddr__in.md#a9a7d98bb8e18f4a06a021c32d6cc7117)

sa\_family\_t sin\_family

AF\_INET.

**Definition** net\_ip.h:191

[sockaddr\_ll](structsockaddr__ll.md)

Socket address struct for packet socket.

**Definition** net\_ip.h:197

[sockaddr\_ll::sll\_pkttype](structsockaddr__ll.md#a2001fcf2627149283e3460b18f44b313)

uint8\_t sll\_pkttype

Packet type.

**Definition** net\_ip.h:202

[sockaddr\_ll::sll\_hatype](structsockaddr__ll.md#a2df317106a30498dd9f87e1d4eefc8fc)

uint16\_t sll\_hatype

ARP hardware type.

**Definition** net\_ip.h:201

[sockaddr\_ll::sll\_family](structsockaddr__ll.md#a4920e92fb0613ba8594a6b6c226048d9)

sa\_family\_t sll\_family

Always AF\_PACKET.

**Definition** net\_ip.h:198

[sockaddr\_ll::sll\_protocol](structsockaddr__ll.md#a661e329c10a8f06a85ad831630273e49)

uint16\_t sll\_protocol

Physical-layer protocol.

**Definition** net\_ip.h:199

[sockaddr\_ll::sll\_ifindex](structsockaddr__ll.md#a93b4976ed8e9d58cdcc620f5d1987f68)

int sll\_ifindex

Interface number.

**Definition** net\_ip.h:200

[sockaddr\_ll::sll\_halen](structsockaddr__ll.md#acb72ab39a239d9e5752b7422dc9a2dc6)

uint8\_t sll\_halen

Length of address.

**Definition** net\_ip.h:203

[sockaddr\_ll::sll\_addr](structsockaddr__ll.md#aee52affe8837ffe1c32c94ce34117d6a)

uint8\_t sll\_addr[8]

Physical-layer address, big endian.

**Definition** net\_ip.h:204

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:408

[sockaddr::sa\_family](structsockaddr.md#ac6ef02e9a2e90a30218132ffd7b5a5c5)

sa\_family\_t sa\_family

Address family.

**Definition** net\_ip.h:409

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
