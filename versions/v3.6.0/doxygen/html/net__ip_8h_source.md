---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__ip_8h_source.html
original_path: doxygen/html/net__ip_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

22

23#include <[string.h](string_8h.md)>

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <[stdbool.h](stdbool_8h.md)>

26#include <[zephyr/sys/util.h](util_8h.md)>

27#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

28#include <[zephyr/toolchain.h](toolchain_8h.md)>

29

30#include <[zephyr/net/net\_linkaddr.h](net__linkaddr_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

37/\* Specifying VLAN tag here in order to avoid circular dependencies \*/

38#define NET\_VLAN\_TAG\_UNSPEC 0x0fff

40

41/\* Protocol families. \*/

[ 42](group__ip__4__6.md#ga51dba11ffc8e3b1bf695e721b3144094)#define PF\_UNSPEC 0

[ 43](group__ip__4__6.md#ga3f5da0b5be27fe31ec7cc11bfa8d1a25)#define PF\_INET 1

[ 44](group__ip__4__6.md#ga323f2649198fc7e64b19881869265618)#define PF\_INET6 2

[ 45](group__ip__4__6.md#ga8e297adb5fe2e28b0d9d921a5d56a8e9)#define PF\_PACKET 3

[ 46](group__ip__4__6.md#gaeac0c3db7a1e021f17987bcc76893849)#define PF\_CAN 4

[ 47](group__ip__4__6.md#ga288b09307bcc46aef2acf2af5e3e1006)#define PF\_NET\_MGMT 5

[ 48](group__ip__4__6.md#ga521c315ca2a2a4e6345878e84af4085e)#define PF\_LOCAL 6

[ 49](group__ip__4__6.md#ga0407288f5fb975a03b21d5287c282b2e)#define PF\_UNIX PF\_LOCAL

50

51/\* Address families. \*/

[ 52](group__ip__4__6.md#gae77ae24b14b7b7f294f3e04121173f12)#define AF\_UNSPEC PF\_UNSPEC

[ 53](group__ip__4__6.md#ga9930604d0e32588eae76f43ca38e7826)#define AF\_INET PF\_INET

[ 54](group__ip__4__6.md#gaa03706b2738b9a58d4985dfbe99e1bac)#define AF\_INET6 PF\_INET6

[ 55](group__ip__4__6.md#gaa89aa4cd481fe17260c3f5d493cc23f5)#define AF\_PACKET PF\_PACKET

[ 56](group__ip__4__6.md#ga546620c7e758f003b24b7fdae4f97bd4)#define AF\_CAN PF\_CAN

[ 57](group__ip__4__6.md#ga41d0cbb55cd9550a7f732b1520119c15)#define AF\_NET\_MGMT PF\_NET\_MGMT

[ 58](group__ip__4__6.md#gae24f1f9ea44fcce3affcb2137f593dc1)#define AF\_LOCAL PF\_LOCAL

[ 59](group__ip__4__6.md#ga0fd8739854bc8b48d65f0b669fed3ffe)#define AF\_UNIX PF\_UNIX

60

[ 62](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) {

[ 63](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a334b0a4a5a3e331e7c7864471e9eab08) [IPPROTO\_IP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a334b0a4a5a3e331e7c7864471e9eab08) = 0,

[ 64](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a7ccd735b73f6955ae2f4abf3e7ca6bb4) [IPPROTO\_ICMP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a7ccd735b73f6955ae2f4abf3e7ca6bb4) = 1,

[ 65](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4cbcb48be0cd8eb6fb5b5741f1c7b639) [IPPROTO\_IGMP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4cbcb48be0cd8eb6fb5b5741f1c7b639) = 2,

[ 66](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a49a42f6d628bf65e78478e8eb4874ff2) [IPPROTO\_IPIP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a49a42f6d628bf65e78478e8eb4874ff2) = 4,

[ 67](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4a3c433d15859f62bacc06312791a45e) [IPPROTO\_TCP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4a3c433d15859f62bacc06312791a45e) = 6,

[ 68](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31abd7dfb22e255a4eed332f41de12d7321) [IPPROTO\_UDP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31abd7dfb22e255a4eed332f41de12d7321) = 17,

[ 69](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a892549243e60ed1e04e88a14b44d8185) [IPPROTO\_IPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a892549243e60ed1e04e88a14b44d8185) = 41,

[ 70](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31aeeff57e3cf726718a92b2138e5842926) [IPPROTO\_ICMPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31aeeff57e3cf726718a92b2138e5842926) = 58,

[ 71](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a3f186705d5c21da1b72ecb91cca1f7a4) [IPPROTO\_RAW](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a3f186705d5c21da1b72ecb91cca1f7a4) = 255,

72};

73

[ 75](group__ip__4__6.md#ga721da18d2a3cfd9b3a56e9efc9f6e58b)enum [net\_ip\_protocol\_secure](group__ip__4__6.md#ga721da18d2a3cfd9b3a56e9efc9f6e58b) {

[ 76](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba6d479e64d940cea948c874d36c656fcc) [IPPROTO\_TLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba6d479e64d940cea948c874d36c656fcc) = 256,

[ 77](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba102692f9f57dd0ec6f8c6cb54a235d4c) [IPPROTO\_TLS\_1\_1](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba102692f9f57dd0ec6f8c6cb54a235d4c) = 257,

[ 78](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa5e176fa47ca23a6f25101a5203f8e5a) [IPPROTO\_TLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa5e176fa47ca23a6f25101a5203f8e5a) = 258,

[ 79](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba92e94005d7a80aacbffad2f3f10555ef) [IPPROTO\_DTLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba92e94005d7a80aacbffad2f3f10555ef) = 272,

[ 80](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58bad4d2a6ca8756ee52221f19fb06c34a1c) [IPPROTO\_DTLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58bad4d2a6ca8756ee52221f19fb06c34a1c) = 273,

81};

82

[ 84](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c)enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) {

[ 85](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424) [SOCK\_STREAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424) = 1,

[ 86](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc) [SOCK\_DGRAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc),

[ 87](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231) [SOCK\_RAW](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231)

88};

89

[ 96](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)#define ntohs(x) sys\_be16\_to\_cpu(x)

97

[ 104](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)#define ntohl(x) sys\_be32\_to\_cpu(x)

105

[ 112](group__ip__4__6.md#ga3cfcf123d4ead264289232f91f2c9ca5)#define ntohll(x) sys\_be64\_to\_cpu(x)

113

[ 120](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)#define htons(x) sys\_cpu\_to\_be16(x)

121

[ 128](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)#define htonl(x) sys\_cpu\_to\_be32(x)

129

[ 136](group__ip__4__6.md#ga9f4bf0773c45ad9a9753a1b784a13fbb)#define htonll(x) sys\_cpu\_to\_be64(x)

137

[ 139](structin6__addr.md)struct [in6\_addr](structin6__addr.md) {

140 union {

[ 141](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[16];

[ 142](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[8]; /\* In big endian \*/

[ 143](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[4]; /\* In big endian \*/

144 };

145};

146

147/\* Binary size of the IPv6 address \*/

[ 148](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)#define NET\_IPV6\_ADDR\_SIZE 16

149

[ 151](structin__addr.md)struct [in\_addr](structin__addr.md) {

152 union {

[ 153](structin__addr.md#a4fd35e401c510fabab8979eb8416dd9b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [s4\_addr](structin__addr.md#a4fd35e401c510fabab8979eb8416dd9b)[4];

[ 154](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [s4\_addr16](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86)[2]; /\* In big endian \*/

[ 155](structin__addr.md#ae4e092a27efb643067d7ce10bd454bed) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [s4\_addr32](structin__addr.md#ae4e092a27efb643067d7ce10bd454bed)[1]; /\* In big endian \*/

[ 156](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5); /\* In big endian, for POSIX compatibility. \*/

157 };

158};

159

160/\* Binary size of the IPv4 address \*/

[ 161](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)#define NET\_IPV4\_ADDR\_SIZE 4

162

[ 164](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)typedef unsigned short int [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda);

165

167#ifndef \_\_socklen\_t\_defined

[ 168](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)typedef size\_t [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a);

169#define \_\_socklen\_t\_defined

170#endif

171

172/\*

173 \* Note that the sin\_port and sin6\_port are in network byte order

174 \* in various sockaddr\* structs.

175 \*/

176

[ 178](structsockaddr__in6.md)struct [sockaddr\_in6](structsockaddr__in6.md) {

[ 179](structsockaddr__in6.md#aefa41e43be9c615f8cfd6266c0ed1687) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sin6\_family](structsockaddr__in6.md#aefa41e43be9c615f8cfd6266c0ed1687); /\* AF\_INET6 \*/

[ 180](structsockaddr__in6.md#a4fc2b7a478d258e9e778772701096022) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sin6\_port](structsockaddr__in6.md#a4fc2b7a478d258e9e778772701096022); /\* Port number \*/

[ 181](structsockaddr__in6.md#a219e7f3ecd6d7dcf8fc2465475be490f) struct [in6\_addr](structin6__addr.md) [sin6\_addr](structsockaddr__in6.md#a219e7f3ecd6d7dcf8fc2465475be490f); /\* IPv6 address \*/

[ 182](structsockaddr__in6.md#a1daad78c9848862ab33a48e05fa8cf17) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sin6\_scope\_id](structsockaddr__in6.md#a1daad78c9848862ab33a48e05fa8cf17); /\* interfaces for a scope \*/

183};

184

[ 185](structsockaddr__in6__ptr.md)struct [sockaddr\_in6\_ptr](structsockaddr__in6__ptr.md) {

[ 186](structsockaddr__in6__ptr.md#a5de1da662d5fb57417a593cee8cc82de) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sin6\_family](structsockaddr__in6__ptr.md#a5de1da662d5fb57417a593cee8cc82de); /\* AF\_INET6 \*/

[ 187](structsockaddr__in6__ptr.md#a64be2e93c2453899af630428089086cc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sin6\_port](structsockaddr__in6__ptr.md#a64be2e93c2453899af630428089086cc); /\* Port number \*/

[ 188](structsockaddr__in6__ptr.md#af594f9662b0785a8f527bb9fcb95d92d) struct [in6\_addr](structin6__addr.md) \*[sin6\_addr](structsockaddr__in6__ptr.md#af594f9662b0785a8f527bb9fcb95d92d); /\* IPv6 address \*/

[ 189](structsockaddr__in6__ptr.md#a9fe0b00f5081d4e027e15497304bc55b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sin6\_scope\_id](structsockaddr__in6__ptr.md#a9fe0b00f5081d4e027e15497304bc55b); /\* interfaces for a scope \*/

190};

191

[ 193](structsockaddr__in.md)struct [sockaddr\_in](structsockaddr__in.md) {

[ 194](structsockaddr__in.md#a9a7d98bb8e18f4a06a021c32d6cc7117) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sin\_family](structsockaddr__in.md#a9a7d98bb8e18f4a06a021c32d6cc7117); /\* AF\_INET \*/

[ 195](structsockaddr__in.md#a3cf9239fdd8bd32855d66a4b86349fbb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sin\_port](structsockaddr__in.md#a3cf9239fdd8bd32855d66a4b86349fbb); /\* Port number \*/

[ 196](structsockaddr__in.md#a4ea5f2f1138e5c8597097db255a9ec6c) struct [in\_addr](structin__addr.md) [sin\_addr](structsockaddr__in.md#a4ea5f2f1138e5c8597097db255a9ec6c); /\* IPv4 address \*/

197};

198

[ 199](structsockaddr__in__ptr.md)struct [sockaddr\_in\_ptr](structsockaddr__in__ptr.md) {

[ 200](structsockaddr__in__ptr.md#ae8ca040f7813d6974e0440f877df6744) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sin\_family](structsockaddr__in__ptr.md#ae8ca040f7813d6974e0440f877df6744); /\* AF\_INET \*/

[ 201](structsockaddr__in__ptr.md#aab1491a8d77ca11d8104ef3ef1bace80) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sin\_port](structsockaddr__in__ptr.md#aab1491a8d77ca11d8104ef3ef1bace80); /\* Port number \*/

[ 202](structsockaddr__in__ptr.md#a02d48b07cb42745a729428fc9f4af765) struct [in\_addr](structin__addr.md) \*[sin\_addr](structsockaddr__in__ptr.md#a02d48b07cb42745a729428fc9f4af765); /\* IPv4 address \*/

203};

204

[ 206](structsockaddr__ll.md)struct [sockaddr\_ll](structsockaddr__ll.md) {

[ 207](structsockaddr__ll.md#a4920e92fb0613ba8594a6b6c226048d9) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sll\_family](structsockaddr__ll.md#a4920e92fb0613ba8594a6b6c226048d9); /\* Always AF\_PACKET \*/

[ 208](structsockaddr__ll.md#a661e329c10a8f06a85ad831630273e49) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sll\_protocol](structsockaddr__ll.md#a661e329c10a8f06a85ad831630273e49); /\* Physical-layer protocol \*/

[ 209](structsockaddr__ll.md#a93b4976ed8e9d58cdcc620f5d1987f68) int [sll\_ifindex](structsockaddr__ll.md#a93b4976ed8e9d58cdcc620f5d1987f68); /\* Interface number \*/

[ 210](structsockaddr__ll.md#a2df317106a30498dd9f87e1d4eefc8fc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sll\_hatype](structsockaddr__ll.md#a2df317106a30498dd9f87e1d4eefc8fc); /\* ARP hardware type \*/

[ 211](structsockaddr__ll.md#a2001fcf2627149283e3460b18f44b313) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sll\_pkttype](structsockaddr__ll.md#a2001fcf2627149283e3460b18f44b313); /\* Packet type \*/

[ 212](structsockaddr__ll.md#acb72ab39a239d9e5752b7422dc9a2dc6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sll\_halen](structsockaddr__ll.md#acb72ab39a239d9e5752b7422dc9a2dc6); /\* Length of address \*/

[ 213](structsockaddr__ll.md#aee52affe8837ffe1c32c94ce34117d6a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sll\_addr](structsockaddr__ll.md#aee52affe8837ffe1c32c94ce34117d6a)[8]; /\* Physical-layer address, big endian \*/

214};

215

[ 216](structsockaddr__ll__ptr.md)struct [sockaddr\_ll\_ptr](structsockaddr__ll__ptr.md) {

[ 217](structsockaddr__ll__ptr.md#aab6bfff94bf5880375e7538be72a11c1) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sll\_family](structsockaddr__ll__ptr.md#aab6bfff94bf5880375e7538be72a11c1); /\* Always AF\_PACKET \*/

[ 218](structsockaddr__ll__ptr.md#ad25fe5fef518de3652cf67d25582e50c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sll\_protocol](structsockaddr__ll__ptr.md#ad25fe5fef518de3652cf67d25582e50c); /\* Physical-layer protocol \*/

[ 219](structsockaddr__ll__ptr.md#a47a2543cc247cba79cbaaf82787aa9cf) int [sll\_ifindex](structsockaddr__ll__ptr.md#a47a2543cc247cba79cbaaf82787aa9cf); /\* Interface number \*/

[ 220](structsockaddr__ll__ptr.md#a337cef9822b70d31b50135f158c54b5d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sll\_hatype](structsockaddr__ll__ptr.md#a337cef9822b70d31b50135f158c54b5d); /\* ARP hardware type \*/

[ 221](structsockaddr__ll__ptr.md#a6fa3dcd69fefa59a6da37bde8160104b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sll\_pkttype](structsockaddr__ll__ptr.md#a6fa3dcd69fefa59a6da37bde8160104b); /\* Packet type \*/

[ 222](structsockaddr__ll__ptr.md#ab27a07520cee5183aa62e7a0615f1c5f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sll\_halen](structsockaddr__ll__ptr.md#ab27a07520cee5183aa62e7a0615f1c5f); /\* Length of address \*/

[ 223](structsockaddr__ll__ptr.md#a28579052ff6eda21d5f060e2c8de2421) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[sll\_addr](structsockaddr__ll__ptr.md#a28579052ff6eda21d5f060e2c8de2421); /\* Physical-layer address, big endian \*/

224};

225

[ 226](structsockaddr__can__ptr.md)struct [sockaddr\_can\_ptr](structsockaddr__can__ptr.md) {

[ 227](structsockaddr__can__ptr.md#a37eebdcc4598e3f55eeaa954e77981fb) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [can\_family](structsockaddr__can__ptr.md#a37eebdcc4598e3f55eeaa954e77981fb);

[ 228](structsockaddr__can__ptr.md#a7a181132dfcb2cb7c2bc1cc2deb1814b) int [can\_ifindex](structsockaddr__can__ptr.md#a7a181132dfcb2cb7c2bc1cc2deb1814b);

229};

230

231#if !defined(HAVE\_IOVEC)

[ 232](structiovec.md)struct [iovec](structiovec.md) {

[ 233](structiovec.md#a07aeddeccf80f14520fdd7ef0759442b) void \*[iov\_base](structiovec.md#a07aeddeccf80f14520fdd7ef0759442b);

[ 234](structiovec.md#a17b5ac2078fd1adfabb262a95808a07d) size\_t [iov\_len](structiovec.md#a17b5ac2078fd1adfabb262a95808a07d);

235};

236#endif

237

[ 238](structmsghdr.md)struct [msghdr](structmsghdr.md) {

[ 239](structmsghdr.md#a691a8866b21c7083974a2ff1e7987ce1) void \*[msg\_name](structmsghdr.md#a691a8866b21c7083974a2ff1e7987ce1); /\* optional socket address, big endian \*/

[ 240](structmsghdr.md#a47762b69eee1c9ba5736d64516ea0960) [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) [msg\_namelen](structmsghdr.md#a47762b69eee1c9ba5736d64516ea0960); /\* size of socket address \*/

[ 241](structmsghdr.md#a1b893a6f84c4ba52708c5dcfcc720293) struct [iovec](structiovec.md) \*[msg\_iov](structmsghdr.md#a1b893a6f84c4ba52708c5dcfcc720293); /\* scatter/gather array \*/

[ 242](structmsghdr.md#ad4ef1bd6821e599bf42f936850d2c4d7) size\_t [msg\_iovlen](structmsghdr.md#ad4ef1bd6821e599bf42f936850d2c4d7); /\* number of elements in msg\_iov \*/

[ 243](structmsghdr.md#afba5fc31b0f197e25602d2232ca6d783) void \*[msg\_control](structmsghdr.md#afba5fc31b0f197e25602d2232ca6d783); /\* ancillary data \*/

[ 244](structmsghdr.md#a9fa41b0e9a02b5dc9a01aa6f18108adb) size\_t [msg\_controllen](structmsghdr.md#a9fa41b0e9a02b5dc9a01aa6f18108adb); /\* ancillary data buffer len \*/

[ 245](structmsghdr.md#a9e8ff97d402c99551cbfd564e9e10a74) int [msg\_flags](structmsghdr.md#a9e8ff97d402c99551cbfd564e9e10a74); /\* flags on received message \*/

246};

247

[ 248](structcmsghdr.md)struct [cmsghdr](structcmsghdr.md) {

[ 249](structcmsghdr.md#a7cf479e5e162e65ad164616453d61df2) [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) [cmsg\_len](structcmsghdr.md#a7cf479e5e162e65ad164616453d61df2); /\* Number of bytes, including header \*/

[ 250](structcmsghdr.md#ac0ff1400cb63fbc2e0ece19434cb8fef) int [cmsg\_level](structcmsghdr.md#ac0ff1400cb63fbc2e0ece19434cb8fef); /\* Originating protocol \*/

[ 251](structcmsghdr.md#a4c7cabf7899a688ce10bc92773fca9c1) int [cmsg\_type](structcmsghdr.md#a4c7cabf7899a688ce10bc92773fca9c1); /\* Protocol-specific type \*/

252 /\* Flexible array member to force alignment of cmsghdr \*/

[ 253](structcmsghdr.md#a92c00d02575707f72c04f090b6f8d399) z\_max\_align\_t [cmsg\_data](structcmsghdr.md#a92c00d02575707f72c04f090b6f8d399)[];

254};

255

256/\* Alignment for headers and data. These are arch specific but define

257 \* them here atm if not found alredy.

258 \*/

259#if !defined(ALIGN\_H)

[ 260](group__ip__4__6.md#ga051015580ee95f46da1d68f6be2b333d)#define ALIGN\_H(x) ROUND\_UP(x, \_\_alignof\_\_(struct cmsghdr))

261#endif

262#if !defined(ALIGN\_D)

[ 263](group__ip__4__6.md#gab67ab3f70af998e71325fb26ea0f6a83)#define ALIGN\_D(x) ROUND\_UP(x, \_\_alignof\_\_(z\_max\_align\_t))

264#endif

265

266#if !defined(CMSG\_FIRSTHDR)

[ 267](group__ip__4__6.md#ga39567a31d167fc53336d2ab4a2cd78a4)#define CMSG\_FIRSTHDR(msghdr) \

268 ((msghdr)->msg\_controllen >= sizeof(struct cmsghdr) ? \

269 (struct cmsghdr \*)((msghdr)->msg\_control) : NULL)

270#endif

271

272#if !defined(CMSG\_NXTHDR)

[ 273](group__ip__4__6.md#ga77c17efca635d597cb6e98b28172bdc0)#define CMSG\_NXTHDR(msghdr, cmsg) \

274 (((cmsg) == NULL) ? CMSG\_FIRSTHDR(msghdr) : \

275 (((uint8\_t \*)(cmsg) + ALIGN\_H((cmsg)->cmsg\_len) + \

276 ALIGN\_D(sizeof(struct cmsghdr)) > \

277 (uint8\_t \*)((msghdr)->msg\_control) + (msghdr)->msg\_controllen) ? \

278 NULL : \

279 (struct cmsghdr \*)((uint8\_t \*)(cmsg) + \

280 ALIGN\_H((cmsg)->cmsg\_len))))

281#endif

282

283#if !defined(CMSG\_DATA)

[ 284](group__ip__4__6.md#ga5ab6d56e410ac0904107e84aeb1484cc)#define CMSG\_DATA(cmsg) ((uint8\_t \*)(cmsg) + ALIGN\_D(sizeof(struct cmsghdr)))

285#endif

286

287#if !defined(CMSG\_SPACE)

[ 288](group__ip__4__6.md#ga8db11d639dd07c723256f3bb5bc89044)#define CMSG\_SPACE(length) (ALIGN\_D(sizeof(struct cmsghdr)) + ALIGN\_H(length))

289#endif

290

291#if !defined(CMSG\_LEN)

[ 292](group__ip__4__6.md#gadb36e4ff4fa9a0c6730321c4bfcf64bc)#define CMSG\_LEN(length) (ALIGN\_D(sizeof(struct cmsghdr)) + length)

293#endif

294

296

297/\* Packet types. \*/

298#define PACKET\_HOST 0 /\* To us \*/

299#define PACKET\_BROADCAST 1 /\* To all \*/

300#define PACKET\_MULTICAST 2 /\* To group \*/

301#define PACKET\_OTHERHOST 3 /\* To someone else \*/

302#define PACKET\_OUTGOING 4 /\* Originated by us \*/

303#define PACKET\_LOOPBACK 5

304#define PACKET\_FASTROUTE 6

305

306/\* ARP protocol HARDWARE identifiers. \*/

307#define ARPHRD\_ETHER 1

308

309/\* Note: These macros are defined in a specific order.

310 \* The largest sockaddr size is the last one.

311 \*/

312#if defined(CONFIG\_NET\_IPV4)

313#undef NET\_SOCKADDR\_MAX\_SIZE

314#undef NET\_SOCKADDR\_PTR\_MAX\_SIZE

315#define NET\_SOCKADDR\_MAX\_SIZE (sizeof(struct sockaddr\_in))

316#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_in\_ptr))

317#endif

318

319#if defined(CONFIG\_NET\_SOCKETS\_PACKET)

320#undef NET\_SOCKADDR\_MAX\_SIZE

321#undef NET\_SOCKADDR\_PTR\_MAX\_SIZE

322#define NET\_SOCKADDR\_MAX\_SIZE (sizeof(struct sockaddr\_ll))

323#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_ll\_ptr))

324#endif

325

326#if defined(CONFIG\_NET\_IPV6)

327#undef NET\_SOCKADDR\_MAX\_SIZE

328#define NET\_SOCKADDR\_MAX\_SIZE (sizeof(struct sockaddr\_in6))

329#if !defined(CONFIG\_NET\_SOCKETS\_PACKET)

330#undef NET\_SOCKADDR\_PTR\_MAX\_SIZE

331#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_in6\_ptr))

332#endif

333#endif

334

335#if !defined(CONFIG\_NET\_IPV4)

336#if !defined(CONFIG\_NET\_IPV6)

337#if !defined(CONFIG\_NET\_SOCKETS\_PACKET)

338#define NET\_SOCKADDR\_MAX\_SIZE (sizeof(struct sockaddr\_in6))

339#define NET\_SOCKADDR\_PTR\_MAX\_SIZE (sizeof(struct sockaddr\_in6\_ptr))

340#endif

341#endif

342#endif

343

345

[ 347](structsockaddr.md)struct [sockaddr](structsockaddr.md) {

[ 348](structsockaddr.md#ac6ef02e9a2e90a30218132ffd7b5a5c5) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [sa\_family](structsockaddr.md#ac6ef02e9a2e90a30218132ffd7b5a5c5);

[ 349](structsockaddr.md#a3d44571051f408599343acfc2c95d244) char [data](structsockaddr.md#a3d44571051f408599343acfc2c95d244)[NET\_SOCKADDR\_MAX\_SIZE - sizeof([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda))];

350};

351

353

354struct sockaddr\_ptr {

355 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family;

356 char data[NET\_SOCKADDR\_PTR\_MAX\_SIZE - sizeof([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda))];

357};

358

359/\* Same as sockaddr in our case \*/

360struct sockaddr\_storage {

361 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) ss\_family;

362 char data[NET\_SOCKADDR\_MAX\_SIZE - sizeof([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda))];

363};

364

365/\* Socket address struct for UNIX domain sockets \*/

366struct sockaddr\_un {

367 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sun\_family; /\* AF\_UNIX \*/

368 char sun\_path[NET\_SOCKADDR\_MAX\_SIZE - sizeof([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda))];

369};

370

371struct net\_addr {

372 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family;

373 union {

374 struct in6\_addr in6\_addr;

375 struct in\_addr in\_addr;

376 };

377};

378

379#define IN6ADDR\_ANY\_INIT { { { 0, 0, 0, 0, 0, 0, 0, 0, 0, \

380 0, 0, 0, 0, 0, 0, 0 } } }

381#define IN6ADDR\_LOOPBACK\_INIT { { { 0, 0, 0, 0, 0, 0, 0, \

382 0, 0, 0, 0, 0, 0, 0, 0, 1 } } }

383

384extern const struct [in6\_addr](structin6__addr.md) in6addr\_any;

385extern const struct [in6\_addr](structin6__addr.md) in6addr\_loopback;

386

388

[ 390](group__ip__4__6.md#ga93b37007689284fd9c4bde1a8f4b9199)#define INET\_ADDRSTRLEN 16

[ 394](group__ip__4__6.md#gaf776b22a727aae7c9f4d869d50df47e8)#define INET6\_ADDRSTRLEN 46

395

397

398/\* These are for internal usage of the stack \*/

399#define NET\_IPV6\_ADDR\_LEN sizeof("xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx")

400#define NET\_IPV4\_ADDR\_LEN sizeof("xxx.xxx.xxx.xxx")

401

402#define INADDR\_ANY 0

403#define INADDR\_ANY\_INIT { { { INADDR\_ANY } } }

404

405#define INADDR\_LOOPBACK\_INIT { { { 127, 0, 0, 1 } } }

406

408

[ 409](group__ip__4__6.md#ga7a207761e4879c140f48f93978cb2f0b)enum [net\_ip\_mtu](group__ip__4__6.md#ga7a207761e4879c140f48f93978cb2f0b) {

[ 413](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c) [NET\_IPV6\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c) = 1280,

414

[ 418](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1) [NET\_IPV4\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1) = 576,

419};

420

[ 422](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd)enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) {

[ 423](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b) [NET\_PRIORITY\_BK](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b) = 1,

[ 424](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce) [NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce) = 0,

[ 425](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0) [NET\_PRIORITY\_EE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0) = 2,

[ 426](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354) [NET\_PRIORITY\_CA](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354) = 3,

[ 427](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792) [NET\_PRIORITY\_VI](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792) = 4,

[ 428](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a) [NET\_PRIORITY\_VO](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a) = 5,

[ 429](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05) [NET\_PRIORITY\_IC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05) = 6,

[ 430](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef) [NET\_PRIORITY\_NC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef) = 7

431} \_\_packed;

432

[ 433](group__ip__4__6.md#ga5b32bdfc249437709bb25bd95ec7d6d7)#define NET\_MAX\_PRIORITIES 8 /\* How many priority values there are \*/

434

[ 436](structnet__tuple.md)struct [net\_tuple](structnet__tuple.md) {

[ 437](structnet__tuple.md#a8f9a1aab3c3aedeead795ca6624d4d6d) struct net\_addr \*[remote\_addr](structnet__tuple.md#a8f9a1aab3c3aedeead795ca6624d4d6d);

[ 438](structnet__tuple.md#af7004f8f8d74d49d6771393825612294) struct net\_addr \*[local\_addr](structnet__tuple.md#af7004f8f8d74d49d6771393825612294);

[ 439](structnet__tuple.md#ab4c31093a23bc60d8dcf5b784e3fb39a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [remote\_port](structnet__tuple.md#ab4c31093a23bc60d8dcf5b784e3fb39a);

[ 440](structnet__tuple.md#a9a1cd0dd55a9e866cb0e910120362b7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [local\_port](structnet__tuple.md#a9a1cd0dd55a9e866cb0e910120362b7e);

[ 441](structnet__tuple.md#aa9eeba2c8e263afbf6368e04353d6014) enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) [ip\_proto](structnet__tuple.md#aa9eeba2c8e263afbf6368e04353d6014);

442};

443

[ 445](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d)enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) {

[ 446](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df) [NET\_ADDR\_ANY\_STATE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df) = -1,

[ 447](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9) [NET\_ADDR\_TENTATIVE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9) = 0,

[ 448](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a) [NET\_ADDR\_PREFERRED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a),

[ 449](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3) [NET\_ADDR\_DEPRECATED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3),

450} \_\_packed;

451

[ 453](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41)enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) {

[ 455](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6) [NET\_ADDR\_ANY](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6) = 0,

[ 457](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006) [NET\_ADDR\_AUTOCONF](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006),

[ 459](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db) [NET\_ADDR\_DHCP](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db),

[ 461](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e) [NET\_ADDR\_MANUAL](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e),

[ 463](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4) [NET\_ADDR\_OVERRIDABLE](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4),

464} \_\_packed;

465

467

468struct net\_ipv6\_hdr {

469 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vtc;

470 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tcflow;

471 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) flow;

472 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len;

473 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nexthdr;

474 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit;

475 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[[NET\_IPV6\_ADDR\_SIZE](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)];

476 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[[NET\_IPV6\_ADDR\_SIZE](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)];

477} \_\_packed;

478

479struct net\_ipv6\_frag\_hdr {

480 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nexthdr;

481 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reserved;

482 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset;

483 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id;

484} \_\_packed;

485

486struct net\_ipv4\_hdr {

487 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vhl;

488 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tos;

489 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len;

490 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id[2];

491 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset[2];

492 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl;

493 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proto;

494 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chksum;

495 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[[NET\_IPV4\_ADDR\_SIZE](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)];

496 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[[NET\_IPV4\_ADDR\_SIZE](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)];

497} \_\_packed;

498

499struct net\_icmp\_hdr {

500 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type;

501 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code;

502 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chksum;

503} \_\_packed;

504

505struct net\_udp\_hdr {

506 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src\_port;

507 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst\_port;

508 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len;

509 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chksum;

510} \_\_packed;

511

512struct net\_tcp\_hdr {

513 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src\_port;

514 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst\_port;

515 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) seq[4];

516 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ack[4];

517 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset;

518 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

519 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wnd[2];

520 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chksum;

521 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) urg[2];

522 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) optdata[0];

523} \_\_packed;

524

525static inline const char \*net\_addr\_type2str(enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) type)

526{

527 switch (type) {

528 case [NET\_ADDR\_AUTOCONF](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006):

529 return "AUTO";

530 case [NET\_ADDR\_DHCP](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db):

531 return "DHCP";

532 case [NET\_ADDR\_MANUAL](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e):

533 return "MANUAL";

534 case [NET\_ADDR\_OVERRIDABLE](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4):

535 return "OVERRIDE";

536 case [NET\_ADDR\_ANY](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6):

537 default:

538 break;

539 }

540

541 return "<unknown>";

542}

543

544/\* IPv6 extension headers types \*/

545#define NET\_IPV6\_NEXTHDR\_HBHO 0

546#define NET\_IPV6\_NEXTHDR\_DESTO 60

547#define NET\_IPV6\_NEXTHDR\_ROUTING 43

548#define NET\_IPV6\_NEXTHDR\_FRAG 44

549#define NET\_IPV6\_NEXTHDR\_NONE 59

550

555union net\_ip\_header {

556 struct net\_ipv4\_hdr \*ipv4;

557 struct net\_ipv6\_hdr \*ipv6;

558};

559

560union net\_proto\_header {

561 struct net\_udp\_hdr \*udp;

562 struct net\_tcp\_hdr \*tcp;

563};

564

565#define NET\_UDPH\_LEN 8 /\* Size of UDP header \*/

566#define NET\_TCPH\_LEN 20 /\* Size of TCP header \*/

567#define NET\_ICMPH\_LEN 4 /\* Size of ICMP header \*/

568

569#define NET\_IPV6H\_LEN 40 /\* Size of IPv6 header \*/

570#define NET\_ICMPV6H\_LEN NET\_ICMPH\_LEN /\* Size of ICMPv6 header \*/

571#define NET\_IPV6UDPH\_LEN (NET\_UDPH\_LEN + NET\_IPV6H\_LEN) /\* IPv6 + UDP \*/

572#define NET\_IPV6TCPH\_LEN (NET\_TCPH\_LEN + NET\_IPV6H\_LEN) /\* IPv6 + TCP \*/

573#define NET\_IPV6ICMPH\_LEN (NET\_IPV6H\_LEN + NET\_ICMPH\_LEN) /\* ICMPv6 + IPv6 \*/

574#define NET\_IPV6\_FRAGH\_LEN 8

575

576#define NET\_IPV4H\_LEN 20 /\* Size of IPv4 header \*/

577#define NET\_ICMPV4H\_LEN NET\_ICMPH\_LEN /\* Size of ICMPv4 header \*/

578#define NET\_IPV4UDPH\_LEN (NET\_UDPH\_LEN + NET\_IPV4H\_LEN) /\* IPv4 + UDP \*/

579#define NET\_IPV4TCPH\_LEN (NET\_TCPH\_LEN + NET\_IPV4H\_LEN) /\* IPv4 + TCP \*/

580#define NET\_IPV4ICMPH\_LEN (NET\_IPV4H\_LEN + NET\_ICMPH\_LEN) /\* ICMPv4 + IPv4 \*/

581

582#define NET\_IPV6H\_LENGTH\_OFFSET 0x04 /\* Offset of the Length field in the IPv6 header \*/

583

584#define NET\_IPV6\_FRAGH\_OFFSET\_MASK 0xfff8 /\* Mask for the 13-bit Fragment Offset field \*/

585#define NET\_IPV4\_FRAGH\_OFFSET\_MASK 0x1fff /\* Mask for the 13-bit Fragment Offset field \*/

586#define NET\_IPV4\_MORE\_FRAG\_MASK 0x2000 /\* Mask for the 1-bit More Fragments field \*/

587#define NET\_IPV4\_DO\_NOT\_FRAG\_MASK 0x4000 /\* Mask for the 1-bit Do Not Fragment field \*/

588

590

[ 598](group__ip__4__6.md#gaa662667005bdc00bf1eb5cf243aad874)static inline bool [net\_ipv6\_is\_addr\_loopback](group__ip__4__6.md#gaa662667005bdc00bf1eb5cf243aad874)(struct [in6\_addr](structin6__addr.md) \*addr)

599{

600 return UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]) == 0 &&

601 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == 0 &&

602 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]) == 0 &&

603 [ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3])) == 1;

604}

605

[ 613](group__ip__4__6.md#ga1a2fb0427eeab1a5dec6d69208ad7f02)static inline bool [net\_ipv6\_is\_addr\_mcast](group__ip__4__6.md#ga1a2fb0427eeab1a5dec6d69208ad7f02)(const struct [in6\_addr](structin6__addr.md) \*addr)

614{

615 return addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xFF;

616}

617

618struct [net\_if](structnet__if.md);

619struct [net\_if\_config](structnet__if__config.md);

620

[ 621](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb)extern struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_lookup](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb)(const struct [in6\_addr](structin6__addr.md) \*addr,

622 struct [net\_if](structnet__if.md) \*\*iface);

623

[ 631](group__ip__4__6.md#ga00853528daf79c947dcdc320035ed538)static inline bool [net\_ipv6\_is\_my\_addr](group__ip__4__6.md#ga00853528daf79c947dcdc320035ed538)(struct [in6\_addr](structin6__addr.md) \*addr)

632{

633 return [net\_if\_ipv6\_addr\_lookup](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb)(addr, NULL) != NULL;

634}

635

[ 636](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975)extern struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv6\_maddr\_lookup](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975)(

637 const struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface);

638

[ 647](group__ip__4__6.md#gaf8c5158de9a65d840faa61bb3dec341c)static inline bool [net\_ipv6\_is\_my\_maddr](group__ip__4__6.md#gaf8c5158de9a65d840faa61bb3dec341c)(struct [in6\_addr](structin6__addr.md) \*maddr)

648{

649 return [net\_if\_ipv6\_maddr\_lookup](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975)(maddr, NULL) != NULL;

650}

651

[ 661](group__ip__4__6.md#ga9654007b0a3c4d033df1ec3d00bd26ee)static inline bool [net\_ipv6\_is\_prefix](group__ip__4__6.md#ga9654007b0a3c4d033df1ec3d00bd26ee)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1,

662 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2,

663 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) length)

664{

665 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bits = 128 - length;

666 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bytes = length / 8U;

667 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) remain = bits % 8;

668 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask;

669

670 if (length > 128) {

671 return false;

672 }

673

674 if ([memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(addr1, addr2, bytes)) {

675 return false;

676 }

677

678 if (!remain) {

679 /\* No remaining bits, the prefixes are the same as first

680 \* bytes are the same.

681 \*/

682 return true;

683 }

684

685 /\* Create a mask that has remaining most significant bits set \*/

686 mask = ((0xff << (8 - remain)) ^ 0xff) << remain;

687

688 return (addr1[bytes] & mask) == (addr2[bytes] & mask);

689}

690

[ 698](group__ip__4__6.md#ga879e4aed725d7ea3fe609fa989f14735)static inline bool [net\_ipv4\_is\_addr\_loopback](group__ip__4__6.md#ga879e4aed725d7ea3fe609fa989f14735)(struct [in\_addr](structin__addr.md) \*addr)

699{

700 return addr->[s4\_addr](structin__addr.md#a4fd35e401c510fabab8979eb8416dd9b)[0] == 127U;

701}

702

[ 710](group__ip__4__6.md#gadc623ecacf024733ab6d477d87cc4b9d)static inline bool [net\_ipv4\_is\_addr\_unspecified](group__ip__4__6.md#gadc623ecacf024733ab6d477d87cc4b9d)(const struct [in\_addr](structin__addr.md) \*addr)

711{

712 return UNALIGNED\_GET(&addr->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5)) == 0;

713}

714

[ 722](group__ip__4__6.md#gae8c3302cf9ca457de32eabcf65975b70)static inline bool [net\_ipv4\_is\_addr\_mcast](group__ip__4__6.md#gae8c3302cf9ca457de32eabcf65975b70)(const struct [in\_addr](structin__addr.md) \*addr)

723{

724 return ([ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5))) & 0xF0000000) == 0xE0000000;

725}

726

[ 734](group__ip__4__6.md#gac000a319de7a6f95d4a63719bca3b865)static inline bool [net\_ipv4\_is\_ll\_addr](group__ip__4__6.md#gac000a319de7a6f95d4a63719bca3b865)(const struct [in\_addr](structin__addr.md) \*addr)

735{

736 return ([ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(UNALIGNED\_GET(&addr->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5))) & 0xFFFF0000) == 0xA9FE0000;

737}

738

[ 747](group__ip__4__6.md#ga75ffcc08e621c2d47d1ae043fce2acad)#define net\_ipaddr\_copy(dest, src) \

748 UNALIGNED\_PUT(UNALIGNED\_GET(src), dest)

749

[ 756](group__ip__4__6.md#gaf731738fb1761208739976d767736f87)static inline void [net\_ipv4\_addr\_copy\_raw](group__ip__4__6.md#gaf731738fb1761208739976d767736f87)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dest,

757 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src)

758{

759 [net\_ipaddr\_copy](group__ip__4__6.md#ga75ffcc08e621c2d47d1ae043fce2acad)((struct [in\_addr](structin__addr.md) \*)dest, (const struct [in\_addr](structin__addr.md) \*)src);

760}

761

[ 768](group__ip__4__6.md#ga4925e6f3734b8fc1d9cb1ca1a510b5f1)static inline void [net\_ipv6\_addr\_copy\_raw](group__ip__4__6.md#ga4925e6f3734b8fc1d9cb1ca1a510b5f1)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dest,

769 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src)

770{

771 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(dest, src, sizeof(struct [in6\_addr](structin6__addr.md)));

772}

773

[ 782](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)static inline bool [net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)(const struct [in\_addr](structin__addr.md) \*addr1,

783 const struct [in\_addr](structin__addr.md) \*addr2)

784{

785 return UNALIGNED\_GET(&addr1->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5)) == UNALIGNED\_GET(&addr2->[s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5));

786}

787

[ 796](group__ip__4__6.md#ga32ffb42c62169ac9b34a0faa7c7ffd12)static inline bool [net\_ipv4\_addr\_cmp\_raw](group__ip__4__6.md#ga32ffb42c62169ac9b34a0faa7c7ffd12)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1,

797 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2)

798{

799 return [net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)((const struct [in\_addr](structin__addr.md) \*)addr1,

800 (const struct [in\_addr](structin__addr.md) \*)addr2);

801}

802

[ 811](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)static inline bool [net\_ipv6\_addr\_cmp](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)(const struct [in6\_addr](structin6__addr.md) \*addr1,

812 const struct [in6\_addr](structin6__addr.md) \*addr2)

813{

814 return ![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(addr1, addr2, sizeof(struct [in6\_addr](structin6__addr.md)));

815}

816

[ 825](group__ip__4__6.md#gafbe40461a645cf11fc8b3a07e1d9156e)static inline bool [net\_ipv6\_addr\_cmp\_raw](group__ip__4__6.md#gafbe40461a645cf11fc8b3a07e1d9156e)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1,

826 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2)

827{

828 return [net\_ipv6\_addr\_cmp](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)((const struct [in6\_addr](structin6__addr.md) \*)addr1,

829 (const struct [in6\_addr](structin6__addr.md) \*)addr2);

830}

831

[ 839](group__ip__4__6.md#gacac4279ee8896ddf2a76c612b36edf38)static inline bool [net\_ipv6\_is\_ll\_addr](group__ip__4__6.md#gacac4279ee8896ddf2a76c612b36edf38)(const struct [in6\_addr](structin6__addr.md) \*addr)

840{

841 return UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[0]) == [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(0xFE80);

842}

843

[ 851](group__ip__4__6.md#ga675d016e405e02882fda701aa8617ab7)static inline bool [net\_ipv6\_is\_sl\_addr](group__ip__4__6.md#ga675d016e405e02882fda701aa8617ab7)(const struct [in6\_addr](structin6__addr.md) \*addr)

852{

853 return UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[0]) == [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(0xFEC0);

854}

855

856

[ 864](group__ip__4__6.md#gae10578b8801d213482de7d7d7e7ba230)static inline bool [net\_ipv6\_is\_ula\_addr](group__ip__4__6.md#gae10578b8801d213482de7d7d7e7ba230)(const struct [in6\_addr](structin6__addr.md) \*addr)

865{

866 return addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xFD;

867}

868

[ 876](group__ip__4__6.md#gab2d854e2b24f866839e547c1092ccff6)static inline bool [net\_ipv6\_is\_global\_addr](group__ip__4__6.md#gab2d854e2b24f866839e547c1092ccff6)(const struct [in6\_addr](structin6__addr.md) \*addr)

877{

878 return (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] & 0xE0) == 0x20;

879}

880

[ 886](group__ip__4__6.md#gab0211c91e113cf01a8a16b1a106e7290)const struct [in6\_addr](structin6__addr.md) \*[net\_ipv6\_unspecified\_address](group__ip__4__6.md#gab0211c91e113cf01a8a16b1a106e7290)(void);

887

[ 893](group__ip__4__6.md#gaceb9afdd7f2f78d96e6debd72f63ebf0)const struct [in\_addr](structin__addr.md) \*[net\_ipv4\_unspecified\_address](group__ip__4__6.md#gaceb9afdd7f2f78d96e6debd72f63ebf0)(void);

894

[ 900](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113)const struct [in\_addr](structin__addr.md) \*[net\_ipv4\_broadcast\_address](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113)(void);

901

902struct [net\_if](structnet__if.md);

[ 903](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea)extern bool [net\_if\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea)(struct [net\_if](structnet__if.md) \*iface,

904 const struct [in\_addr](structin__addr.md) \*addr);

905

[ 915](group__ip__4__6.md#ga715455ec5e8041c5d7075fa6913674cd)static inline bool [net\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga715455ec5e8041c5d7075fa6913674cd)(struct [net\_if](structnet__if.md) \*iface,

916 const struct [in\_addr](structin__addr.md) \*addr)

917{

918 return [net\_if\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea)(iface, addr);

919}

920

[ 921](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf)extern bool [net\_if\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf)(struct [net\_if](structnet__if.md) \*iface,

922 const struct [in\_addr](structin__addr.md) \*addr);

923

932#if defined(CONFIG\_NET\_NATIVE\_IPV4)

933static inline bool [net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)(struct [net\_if](structnet__if.md) \*iface,

934 const struct [in\_addr](structin__addr.md) \*addr)

935{

936 if ([net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)(addr, [net\_ipv4\_broadcast\_address](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113)())) {

937 return true;

938 }

939

940 return [net\_if\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf)(iface, addr);

941}

942#else

[ 943](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)static inline bool [net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)(struct [net\_if](structnet__if.md) \*iface,

944 const struct [in\_addr](structin__addr.md) \*addr)

945{

946 ARG\_UNUSED(iface);

947 ARG\_UNUSED(addr);

948

949 return false;

950}

951#endif

952

[ 953](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53)extern struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv4\_addr\_lookup](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53)(const struct [in\_addr](structin__addr.md) \*addr,

954 struct [net\_if](structnet__if.md) \*\*iface);

955

[ 965](group__ip__4__6.md#ga3db2a1fca0b525a7202277700b987eb9)static inline bool [net\_ipv4\_is\_my\_addr](group__ip__4__6.md#ga3db2a1fca0b525a7202277700b987eb9)(const struct [in\_addr](structin__addr.md) \*addr)

966{

967 bool ret;

968

969 ret = [net\_if\_ipv4\_addr\_lookup](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53)(addr, NULL) != NULL;

970 if (!ret) {

971 ret = [net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)(NULL, addr);

972 }

973

974 return ret;

975}

976

[ 984](group__ip__4__6.md#gafe2c8dc0bdb677ba9bc872d051aab2a0)static inline bool [net\_ipv6\_is\_addr\_unspecified](group__ip__4__6.md#gafe2c8dc0bdb677ba9bc872d051aab2a0)(const struct [in6\_addr](structin6__addr.md) \*addr)

985{

986 return UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]) == 0 &&

987 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == 0 &&

988 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]) == 0 &&

989 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3]) == 0;

990}

991

[ 1000](group__ip__4__6.md#ga5a334819f4e4bf87aea5caa7ef28c68a)static inline bool [net\_ipv6\_is\_addr\_solicited\_node](group__ip__4__6.md#ga5a334819f4e4bf87aea5caa7ef28c68a)(const struct [in6\_addr](structin6__addr.md) \*addr)

1001{

1002 return UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]) == [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0xff020000) &&

1003 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == 0x00000000 &&

1004 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]) == [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0x00000001) &&

1005 ((UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3]) & [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0xff000000)) ==

1006 [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0xff000000));

1007}

1008

[ 1019](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)static inline bool [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(const struct [in6\_addr](structin6__addr.md) \*addr,

1020 int scope)

1021{

1022 return (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xff) && (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[1] == scope);

1023}

1024

[ 1034](group__ip__4__6.md#ga3f80a84f330a31aaa875fdea64dc18ec)static inline bool [net\_ipv6\_is\_same\_mcast\_scope](group__ip__4__6.md#ga3f80a84f330a31aaa875fdea64dc18ec)(const struct [in6\_addr](structin6__addr.md) \*addr\_1,

1035 const struct [in6\_addr](structin6__addr.md) \*addr\_2)

1036{

1037 return (addr\_1->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xff) && (addr\_2->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] == 0xff) &&

1038 (addr\_1->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[1] == addr\_2->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[1]);

1039}

1040

[ 1048](group__ip__4__6.md#ga55d67d4349dd354a7254a2f8e8320693)static inline bool [net\_ipv6\_is\_addr\_mcast\_global](group__ip__4__6.md#ga55d67d4349dd354a7254a2f8e8320693)(const struct [in6\_addr](structin6__addr.md) \*addr)

1049{

1050 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x0e);

1051}

1052

[ 1062](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)static inline bool [net\_ipv6\_is\_addr\_mcast\_iface](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)(const struct [in6\_addr](structin6__addr.md) \*addr)

1063{

1064 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x01);

1065}

1066

[ 1076](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)static inline bool [net\_ipv6\_is\_addr\_mcast\_link](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)(const struct [in6\_addr](structin6__addr.md) \*addr)

1077{

1078 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x02);

1079}

1080

[ 1090](group__ip__4__6.md#ga497a148717c1c1095abeb4482566dda0)static inline bool [net\_ipv6\_is\_addr\_mcast\_mesh](group__ip__4__6.md#ga497a148717c1c1095abeb4482566dda0)(const struct [in6\_addr](structin6__addr.md) \*addr)

1091{

1092 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x03);

1093}

1094

[ 1104](group__ip__4__6.md#ga6704146124a14be9cf2a636947c35a00)static inline bool [net\_ipv6\_is\_addr\_mcast\_site](group__ip__4__6.md#ga6704146124a14be9cf2a636947c35a00)(const struct [in6\_addr](structin6__addr.md) \*addr)

1105{

1106 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x05);

1107}

1108

[ 1118](group__ip__4__6.md#ga141ed5de3043dd7d6b45098aea38a4b1)static inline bool [net\_ipv6\_is\_addr\_mcast\_org](group__ip__4__6.md#ga141ed5de3043dd7d6b45098aea38a4b1)(const struct [in6\_addr](structin6__addr.md) \*addr)

1119{

1120 return [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)(addr, 0x08);

1121}

1122

[ 1133](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0)static inline bool [net\_ipv6\_is\_addr\_mcast\_group](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0)(const struct [in6\_addr](structin6__addr.md) \*addr,

1134 const struct [in6\_addr](structin6__addr.md) \*group)

1135{

1136 return UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[1]) == group->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[1] &&

1137 UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[2]) == group->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[2] &&

1138 UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[3]) == group->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[3] &&

1139 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == group->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1] &&

1140 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]) == group->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1] &&

1141 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3]) == group->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[3];

1142}

1143

1152static inline bool

[ 1153](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)[net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)(const struct [in6\_addr](structin6__addr.md) \*addr)

1154{

1155 static const struct [in6\_addr](structin6__addr.md) all\_nodes\_mcast\_group = {

1156 { { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,

1157 0x00, 0x00, 0x00, 0x00, 0x00, 0x01 } }

1158 };

1159

1160 return [net\_ipv6\_is\_addr\_mcast\_group](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0)(addr, &all\_nodes\_mcast\_group);

1161}

1162

1172static inline bool

[ 1173](group__ip__4__6.md#ga35bdad7c958f1ea656680000ee3f6bfd)[net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes](group__ip__4__6.md#ga35bdad7c958f1ea656680000ee3f6bfd)(const struct [in6\_addr](structin6__addr.md) \*addr)

1174{

1175 return [net\_ipv6\_is\_addr\_mcast\_iface](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)(addr) &&

1176 [net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)(addr);

1177}

1178

1188static inline bool

[ 1189](group__ip__4__6.md#gaba3e1259f452381ef3e109bb2eb34c09)[net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes](group__ip__4__6.md#gaba3e1259f452381ef3e109bb2eb34c09)(const struct [in6\_addr](structin6__addr.md) \*addr)

1190{

1191 return [net\_ipv6\_is\_addr\_mcast\_link](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)(addr) &&

1192 [net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)(addr);

1193}

1194

1202static inline

[ 1203](group__ip__4__6.md#ga6091a7406c136fcf480517cb969c9d90)void [net\_ipv6\_addr\_create\_solicited\_node](group__ip__4__6.md#ga6091a7406c136fcf480517cb969c9d90)(const struct [in6\_addr](structin6__addr.md) \*src,

1204 struct [in6\_addr](structin6__addr.md) \*dst)

1205{

1206 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[0] = 0xFF;

1207 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[1] = 0x02;

1208 UNALIGNED\_PUT(0, &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[1]);

1209 UNALIGNED\_PUT(0, &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[2]);

1210 UNALIGNED\_PUT(0, &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[3]);

1211 UNALIGNED\_PUT(0, &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[4]);

1212 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[10] = 0U;

1213 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] = 0x01;

1214 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] = 0xFF;

1215 dst->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13] = src->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13];

1216 UNALIGNED\_PUT(UNALIGNED\_GET(&src->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[7]), &dst->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[7]);

1217}

1218

[ 1231](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)static inline void [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)(struct [in6\_addr](structin6__addr.md) \*addr,

1232 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr0, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr1,

1233 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr2, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr3,

1234 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr4, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr5,

1235 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr6, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr7)

1236{

1237 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr0), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[0]);

1238 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr1), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[1]);

1239 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr2), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[2]);

1240 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr3), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[3]);

1241 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr4), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[4]);

1242 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr5), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[5]);

1243 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr6), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[6]);

1244 UNALIGNED\_PUT([htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(addr7), &addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[7]);

1245}

1246

[ 1252](group__ip__4__6.md#ga58cbba1c522815b1ce201b0377ffe0b2)static inline void [net\_ipv6\_addr\_create\_ll\_allnodes\_mcast](group__ip__4__6.md#ga58cbba1c522815b1ce201b0377ffe0b2)(struct [in6\_addr](structin6__addr.md) \*addr)

1253{

1254 [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)(addr, 0xff02, 0, 0, 0, 0, 0, 0, 0x0001);

1255}

1256

[ 1262](group__ip__4__6.md#ga30821f0a2c08b4b01b71d362e3a25de1)static inline void [net\_ipv6\_addr\_create\_ll\_allrouters\_mcast](group__ip__4__6.md#ga30821f0a2c08b4b01b71d362e3a25de1)(struct [in6\_addr](structin6__addr.md) \*addr)

1263{

1264 [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)(addr, 0xff02, 0, 0, 0, 0, 0, 0, 0x0002);

1265}

1266

[ 1273](group__ip__4__6.md#ga8c6162c6212051037a33477aab9fc55f)static inline void [net\_ipv6\_addr\_create\_v4\_mapped](group__ip__4__6.md#ga8c6162c6212051037a33477aab9fc55f)(const struct [in\_addr](structin__addr.md) \*addr4,

1274 struct [in6\_addr](structin6__addr.md) \*addr6)

1275{

1276 [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)(addr6, 0, 0, 0, 0, 0, 0xffff,

1277 [ntohs](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)(addr4->[s4\_addr16](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86)[0]),

1278 [ntohs](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)(addr4->[s4\_addr16](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86)[1]));

1279}

1280

[ 1289](group__ip__4__6.md#ga53c24abd635fb2bcb137584dbc8a9026)static inline bool [net\_ipv6\_addr\_is\_v4\_mapped](group__ip__4__6.md#ga53c24abd635fb2bcb137584dbc8a9026)(const struct [in6\_addr](structin6__addr.md) \*addr)

1290{

1291 if (UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]) == 0 &&

1292 UNALIGNED\_GET(&addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]) == 0 &&

1293 UNALIGNED\_GET(&addr->[s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)[5]) == 0xffff) {

1294 return true;

1295 }

1296

1297 return false;

1298}

1299

[ 1306](group__ip__4__6.md#ga6d41f1de27e2e8fbb8f12925eba852b4)static inline void [net\_ipv6\_addr\_create\_iid](group__ip__4__6.md#ga6d41f1de27e2e8fbb8f12925eba852b4)(struct [in6\_addr](structin6__addr.md) \*addr,

1307 struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr)

1308{

1309 UNALIGNED\_PUT([htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(0xfe800000), &addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[0]);

1310 UNALIGNED\_PUT(0, &addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[1]);

1311

1312 switch (lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)) {

1313 case 2:

1314 /\* The generated IPv6 shall not toggle the

1315 \* Universal/Local bit. RFC 6282 ch 3.2.2

1316 \*/

1317 if (lladdr->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) == [NET\_LINK\_IEEE802154](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3)) {

1318 UNALIGNED\_PUT(0, &addr->[s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)[2]);

1319 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] = 0xff;

1320 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] = 0xfe;

1321 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13] = 0U;

1322 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[14] = lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[0];

1323 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[15] = lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[1];

1324 }

1325

1326 break;

1327 case 6:

1328 /\* We do not toggle the Universal/Local bit

1329 \* in Bluetooth. See RFC 7668 ch 3.2.2

1330 \*/

1331 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8], lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0), 3);

1332 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] = 0xff;

1333 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] = 0xfe;

1334 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13], lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0) + 3, 3);

1335

1336#if defined(CONFIG\_NET\_L2\_BT\_ZEP1656)

1337 /\* Workaround against older Linux kernel BT IPSP code.

1338 \* This will be removed eventually.

1339 \*/

1340 if (lladdr->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) == [NET\_LINK\_BLUETOOTH](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a)) {

1341 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] ^= 0x02;

1342 }

1343#endif

1344

1345 if (lladdr->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) == [NET\_LINK\_ETHERNET](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)) {

1346 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] ^= 0x02;

1347 }

1348

1349 break;

1350 case 8:

1351 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8], lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0), lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0));

1352 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] ^= 0x02;

1353 break;

1354 }

1355}

1356

[ 1362](group__ip__4__6.md#gaf4b0c30b926748625bd3c4c81d06ffc5)static inline bool [net\_ipv6\_addr\_based\_on\_ll](group__ip__4__6.md#gaf4b0c30b926748625bd3c4c81d06ffc5)(const struct [in6\_addr](structin6__addr.md) \*addr,

1363 const struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr)

1364{

1365 if (!addr || !lladdr) {

1366 return false;

1367 }

1368

1369 switch (lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)) {

1370 case 2:

1371 if (![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[14], lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0), lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)) &&

1372 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] == 0U &&

1373 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[9] == 0U &&

1374 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[10] == 0U &&

1375 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] == 0xff &&

1376 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] == 0xfe) {

1377 return true;

1378 }

1379

1380 break;

1381 case 6:

1382 if (lladdr->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) == [NET\_LINK\_ETHERNET](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)) {

1383 if (![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[9], &lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[1], 2) &&

1384 ![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13], &lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[3], 3) &&

1385 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] == 0xff &&

1386 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] == 0xfe &&

1387 (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] ^ 0x02) == lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[0]) {

1388 return true;

1389 }

1390 } else if (lladdr->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) == [NET\_LINK\_BLUETOOTH](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a)) {

1391 if (![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[9], &lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[1], 2) &&

1392 ![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[13], &lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[3], 3) &&

1393 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[11] == 0xff &&

1394 addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[12] == 0xfe

1395#if defined(CONFIG\_NET\_L2\_BT\_ZEP1656)

1396 /\* Workaround against older Linux kernel BT IPSP

1397 \* code. This will be removed eventually.

1398 \*/

1399 && (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] ^ 0x02) == lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[0]

1400#endif

1401 ) {

1402 return true;

1403 }

1404 }

1405

1406 break;

1407 case 8:

1408 if (![memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(&addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[9], &lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[1],

1409 lladdr->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) - 1) &&

1410 (addr->[s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)[8] ^ 0x02) == lladdr->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)[0]) {

1411 return true;

1412 }

1413

1414 break;

1415 }

1416

1417 return false;

1418}

1419

[ 1428](group__ip__4__6.md#gad97b2c3da722409eada099f9b7e13f03)static inline struct [sockaddr\_in6](structsockaddr__in6.md) \*[net\_sin6](group__ip__4__6.md#gad97b2c3da722409eada099f9b7e13f03)(const struct [sockaddr](structsockaddr.md) \*addr)

1429{

1430 return (struct [sockaddr\_in6](structsockaddr__in6.md) \*)addr;

1431}

1432

[ 1441](group__ip__4__6.md#gacccfbac6a03480840fa219e9a1924dc6)static inline struct [sockaddr\_in](structsockaddr__in.md) \*[net\_sin](group__ip__4__6.md#gacccfbac6a03480840fa219e9a1924dc6)(const struct [sockaddr](structsockaddr.md) \*addr)

1442{

1443 return (struct [sockaddr\_in](structsockaddr__in.md) \*)addr;

1444}

1445

1454static inline

[ 1455](group__ip__4__6.md#gae86d2cd402142190e1ea1c120a57939f)struct [sockaddr\_in6\_ptr](structsockaddr__in6__ptr.md) \*[net\_sin6\_ptr](group__ip__4__6.md#gae86d2cd402142190e1ea1c120a57939f)(const struct sockaddr\_ptr \*addr)

1456{

1457 return (struct [sockaddr\_in6\_ptr](structsockaddr__in6__ptr.md) \*)addr;

1458}

1459

1468static inline

[ 1469](group__ip__4__6.md#ga4b948e84590081a8aed2a63496e57ae2)struct [sockaddr\_in\_ptr](structsockaddr__in__ptr.md) \*[net\_sin\_ptr](group__ip__4__6.md#ga4b948e84590081a8aed2a63496e57ae2)(const struct sockaddr\_ptr \*addr)

1470{

1471 return (struct [sockaddr\_in\_ptr](structsockaddr__in__ptr.md) \*)addr;

1472}

1473

1482static inline

[ 1483](group__ip__4__6.md#gad5cf206e18769a15f9fc917e416db6ee)struct [sockaddr\_ll\_ptr](structsockaddr__ll__ptr.md) \*[net\_sll\_ptr](group__ip__4__6.md#gad5cf206e18769a15f9fc917e416db6ee)(const struct sockaddr\_ptr \*addr)

1484{

1485 return (struct [sockaddr\_ll\_ptr](structsockaddr__ll__ptr.md) \*)addr;

1486}

1487

1496static inline

[ 1497](group__ip__4__6.md#gac2fb590a35961c04807dd985f462c5fb)struct [sockaddr\_can\_ptr](structsockaddr__can__ptr.md) \*[net\_can\_ptr](group__ip__4__6.md#gac2fb590a35961c04807dd985f462c5fb)(const struct sockaddr\_ptr \*addr)

1498{

1499 return (struct [sockaddr\_can\_ptr](structsockaddr__can__ptr.md) \*)addr;

1500}

1501

[ 1515](group__ip__4__6.md#ga264b3c0a13493eac291ddc85d0b4d43d)\_\_syscall int [net\_addr\_pton](group__ip__4__6.md#ga264b3c0a13493eac291ddc85d0b4d43d)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst);

1516

[ 1528](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)\_\_syscall char \*[net\_addr\_ntop](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src,

1529 char \*dst, size\_t size);

1530

[ 1552](group__ip__4__6.md#ga9918e156f0039cf45d487a112e0a2ada)bool [net\_ipaddr\_parse](group__ip__4__6.md#ga9918e156f0039cf45d487a112e0a2ada)(const char \*str, size\_t str\_len,

1553 struct [sockaddr](structsockaddr.md) \*addr);

1554

[ 1566](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [net\_tcp\_seq\_cmp](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq2)

1567{

1568 return ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(seq1 - seq2);

1569}

1570

[ 1581](group__ip__4__6.md#gaa77b299f53e5535ac4c4bea1b6531a34)static inline bool [net\_tcp\_seq\_greater](group__ip__4__6.md#gaa77b299f53e5535ac4c4bea1b6531a34)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq2)

1582{

1583 return [net\_tcp\_seq\_cmp](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f)(seq1, seq2) > 0;

1584}

1585

[ 1597](group__ip__4__6.md#ga8b794f251cf8412c769ab415902a9f32)int [net\_bytes\_from\_str](group__ip__4__6.md#ga8b794f251cf8412c769ab415902a9f32)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, int buf\_len, const char \*src);

1598

[ 1607](group__ip__4__6.md#gae74c9ba7ff4addbce7f931bd6fa91fa0)int [net\_tx\_priority2tc](group__ip__4__6.md#gae74c9ba7ff4addbce7f931bd6fa91fa0)(enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) prio);

1608

[ 1617](group__ip__4__6.md#ga7b3c41ae9b3962090d72c130a9fa61b1)int [net\_rx\_priority2tc](group__ip__4__6.md#ga7b3c41ae9b3962090d72c130a9fa61b1)(enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) prio);

1618

[ 1627](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4)static inline enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) [net\_vlan2priority](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

1628{

1629 /\* Map according to IEEE 802.1Q \*/

1630 static const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vlan2priority[] = {

1631 [NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce),

1632 [NET\_PRIORITY\_BK](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b),

1633 [NET\_PRIORITY\_EE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0),

1634 [NET\_PRIORITY\_CA](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354),

1635 [NET\_PRIORITY\_VI](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792),

1636 [NET\_PRIORITY\_VO](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a),

1637 [NET\_PRIORITY\_IC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05),

1638 [NET\_PRIORITY\_NC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef)

1639 };

1640

1641 if (priority >= [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(vlan2priority)) {

1642 /\* Use Best Effort as the default priority \*/

1643 return [NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce);

1644 }

1645

1646 return (enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd))vlan2priority[priority];

1647}

1648

[ 1656](group__ip__4__6.md#ga8be77d043d4d1d29e0879b3b22274629)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_priority2vlan](group__ip__4__6.md#ga8be77d043d4d1d29e0879b3b22274629)(enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) priority)

1657{

1658 /\* The conversion works both ways \*/

1659 return ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))[net\_vlan2priority](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4)(priority);

1660}

1661

[ 1670](group__ip__4__6.md#gaba4c72e3aa2ceb4ac67d25112fb36523)const char \*[net\_family2str](group__ip__4__6.md#gaba4c72e3aa2ceb4ac67d25112fb36523)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family);

1671

1672#ifdef \_\_cplusplus

1673}

1674#endif

1675

1676#include <syscalls/net\_ip.h>

1677

1681

1682

1683#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_IP\_H\_ \*/

[net\_ipv6\_is\_my\_addr](group__ip__4__6.md#ga00853528daf79c947dcdc320035ed538)

static bool net\_ipv6\_is\_my\_addr(struct in6\_addr \*addr)

Check if IPv6 address is found in one of the network interfaces.

**Definition** net\_ip.h:631

[net\_if\_ipv4\_addr\_lookup](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53)

struct net\_if\_addr \* net\_if\_ipv4\_addr\_lookup(const struct in\_addr \*addr, struct net\_if \*\*iface)

[net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696)

static void net\_ipv6\_addr\_create(struct in6\_addr \*addr, uint16\_t addr0, uint16\_t addr1, uint16\_t addr2, uint16\_t addr3, uint16\_t addr4, uint16\_t addr5, uint16\_t addr6, uint16\_t addr7)

Construct an IPv6 address from eight 16-bit words.

**Definition** net\_ip.h:1231

[net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8)

static bool net\_ipv4\_addr\_cmp(const struct in\_addr \*addr1, const struct in\_addr \*addr2)

Compare two IPv4 addresses.

**Definition** net\_ip.h:782

[NET\_IPV4\_ADDR\_SIZE](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)

#define NET\_IPV4\_ADDR\_SIZE

**Definition** net\_ip.h:161

[net\_if\_ipv6\_addr\_lookup](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb)

struct net\_if\_addr \* net\_if\_ipv6\_addr\_lookup(const struct in6\_addr \*addr, struct net\_if \*\*iface)

[net\_ipv6\_is\_addr\_mcast\_org](group__ip__4__6.md#ga141ed5de3043dd7d6b45098aea38a4b1)

static bool net\_ipv6\_is\_addr\_mcast\_org(const struct in6\_addr \*addr)

Check if the IPv6 address is an organization scope multicast address (FFx8::).

**Definition** net\_ip.h:1118

[net\_vlan2priority](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4)

static enum net\_priority net\_vlan2priority(uint8\_t priority)

Convert network packet VLAN priority to network packet priority so we can place the packet into corre...

**Definition** net\_ip.h:1627

[net\_tcp\_seq\_cmp](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f)

static int32\_t net\_tcp\_seq\_cmp(uint32\_t seq1, uint32\_t seq2)

Compare TCP sequence numbers.

**Definition** net\_ip.h:1566

[net\_ipv6\_is\_addr\_mcast](group__ip__4__6.md#ga1a2fb0427eeab1a5dec6d69208ad7f02)

static bool net\_ipv6\_is\_addr\_mcast(const struct in6\_addr \*addr)

Check if the IPv6 address is a multicast address.

**Definition** net\_ip.h:613

[NET\_IPV6\_ADDR\_SIZE](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)

#define NET\_IPV6\_ADDR\_SIZE

**Definition** net\_ip.h:148

[net\_addr\_pton](group__ip__4__6.md#ga264b3c0a13493eac291ddc85d0b4d43d)

int net\_addr\_pton(sa\_family\_t family, const char \*src, void \*dst)

Convert a string to IP address.

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:164

[net\_ipv6\_addr\_create\_ll\_allrouters\_mcast](group__ip__4__6.md#ga30821f0a2c08b4b01b71d362e3a25de1)

static void net\_ipv6\_addr\_create\_ll\_allrouters\_mcast(struct in6\_addr \*addr)

Create link local allrouters multicast IPv6 address.

**Definition** net\_ip.h:1262

[net\_addr\_ntop](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)

char \* net\_addr\_ntop(sa\_family\_t family, const void \*src, char \*dst, size\_t size)

Convert IP address to string form.

[net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d)

net\_addr\_state

What is the current state of the network address.

**Definition** net\_ip.h:445

[net\_ipv4\_addr\_cmp\_raw](group__ip__4__6.md#ga32ffb42c62169ac9b34a0faa7c7ffd12)

static bool net\_ipv4\_addr\_cmp\_raw(const uint8\_t \*addr1, const uint8\_t \*addr2)

Compare two raw IPv4 address buffers.

**Definition** net\_ip.h:796

[net\_ipv6\_addr\_cmp](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)

static bool net\_ipv6\_addr\_cmp(const struct in6\_addr \*addr1, const struct in6\_addr \*addr2)

Compare two IPv6 addresses.

**Definition** net\_ip.h:811

[net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes](group__ip__4__6.md#ga35bdad7c958f1ea656680000ee3f6bfd)

static bool net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes(const struct in6\_addr \*addr)

Check if the IPv6 address is a interface scope all nodes multicast address (FF01::1).

**Definition** net\_ip.h:1173

[net\_ipv4\_is\_my\_addr](group__ip__4__6.md#ga3db2a1fca0b525a7202277700b987eb9)

static bool net\_ipv4\_is\_my\_addr(const struct in\_addr \*addr)

Check if the IPv4 address is assigned to any network interface in the system.

**Definition** net\_ip.h:965

[net\_ipv6\_is\_same\_mcast\_scope](group__ip__4__6.md#ga3f80a84f330a31aaa875fdea64dc18ec)

static bool net\_ipv6\_is\_same\_mcast\_scope(const struct in6\_addr \*addr\_1, const struct in6\_addr \*addr\_2)

Check if the IPv6 addresses have the same multicast scope (FFyx::).

**Definition** net\_ip.h:1034

[net\_ipv6\_addr\_copy\_raw](group__ip__4__6.md#ga4925e6f3734b8fc1d9cb1ca1a510b5f1)

static void net\_ipv6\_addr\_copy\_raw(uint8\_t \*dest, const uint8\_t \*src)

Copy an IPv6 address raw buffer.

**Definition** net\_ip.h:768

[net\_ipv6\_is\_addr\_mcast\_mesh](group__ip__4__6.md#ga497a148717c1c1095abeb4482566dda0)

static bool net\_ipv6\_is\_addr\_mcast\_mesh(const struct in6\_addr \*addr)

Check if the IPv6 address is a mesh-local scope multicast address (FFx3::).

**Definition** net\_ip.h:1090

[net\_sin\_ptr](group__ip__4__6.md#ga4b948e84590081a8aed2a63496e57ae2)

static struct sockaddr\_in\_ptr \* net\_sin\_ptr(const struct sockaddr\_ptr \*addr)

Get sockaddr\_in\_ptr from sockaddr\_ptr.

**Definition** net\_ip.h:1469

[net\_ipv4\_broadcast\_address](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113)

const struct in\_addr \* net\_ipv4\_broadcast\_address(void)

Return pointer to broadcast (all bits ones) IPv4 address.

[htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)

#define htons(x)

Convert 16-bit value from host to network byte order.

**Definition** net\_ip.h:120

[net\_ipv6\_addr\_is\_v4\_mapped](group__ip__4__6.md#ga53c24abd635fb2bcb137584dbc8a9026)

static bool net\_ipv6\_addr\_is\_v4\_mapped(const struct in6\_addr \*addr)

Is the IPv6 address an IPv4 mapped one.

**Definition** net\_ip.h:1289

[net\_if\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea)

bool net\_if\_ipv4\_addr\_mask\_cmp(struct net\_if \*iface, const struct in\_addr \*addr)

[net\_ipv6\_is\_addr\_mcast\_global](group__ip__4__6.md#ga55d67d4349dd354a7254a2f8e8320693)

static bool net\_ipv6\_is\_addr\_mcast\_global(const struct in6\_addr \*addr)

Check if the IPv6 address is a global multicast address (FFxE::/16).

**Definition** net\_ip.h:1048

[net\_ipv6\_addr\_create\_ll\_allnodes\_mcast](group__ip__4__6.md#ga58cbba1c522815b1ce201b0377ffe0b2)

static void net\_ipv6\_addr\_create\_ll\_allnodes\_mcast(struct in6\_addr \*addr)

Create link local allnodes multicast IPv6 address.

**Definition** net\_ip.h:1252

[net\_ipv6\_is\_addr\_solicited\_node](group__ip__4__6.md#ga5a334819f4e4bf87aea5caa7ef28c68a)

static bool net\_ipv6\_is\_addr\_solicited\_node(const struct in6\_addr \*addr)

Check if the IPv6 address is solicited node multicast address FF02:0:0:0:0:1:FFXX:XXXX defined in RFC...

**Definition** net\_ip.h:1000

[net\_ipv6\_addr\_create\_solicited\_node](group__ip__4__6.md#ga6091a7406c136fcf480517cb969c9d90)

static void net\_ipv6\_addr\_create\_solicited\_node(const struct in6\_addr \*src, struct in6\_addr \*dst)

Create solicited node IPv6 multicast address FF02:0:0:0:0:1:FFXX:XXXX defined in RFC 3513.

**Definition** net\_ip.h:1203

[net\_ipv6\_is\_addr\_mcast\_group](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0)

static bool net\_ipv6\_is\_addr\_mcast\_group(const struct in6\_addr \*addr, const struct in6\_addr \*group)

Check if the IPv6 address belongs to certain multicast group.

**Definition** net\_ip.h:1133

[net\_ipv6\_is\_addr\_mcast\_site](group__ip__4__6.md#ga6704146124a14be9cf2a636947c35a00)

static bool net\_ipv6\_is\_addr\_mcast\_site(const struct in6\_addr \*addr)

Check if the IPv6 address is a site scope multicast address (FFx5::).

**Definition** net\_ip.h:1104

[net\_ipv6\_is\_sl\_addr](group__ip__4__6.md#ga675d016e405e02882fda701aa8617ab7)

static bool net\_ipv6\_is\_sl\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a site local address.

**Definition** net\_ip.h:851

[net\_ipv6\_addr\_create\_iid](group__ip__4__6.md#ga6d41f1de27e2e8fbb8f12925eba852b4)

static void net\_ipv6\_addr\_create\_iid(struct in6\_addr \*addr, struct net\_linkaddr \*lladdr)

Create IPv6 address interface identifier.

**Definition** net\_ip.h:1306

[net\_ipv6\_is\_addr\_mcast\_link](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)

static bool net\_ipv6\_is\_addr\_mcast\_link(const struct in6\_addr \*addr)

Check if the IPv6 address is a link local scope multicast address (FFx2::).

**Definition** net\_ip.h:1076

[net\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga715455ec5e8041c5d7075fa6913674cd)

static bool net\_ipv4\_addr\_mask\_cmp(struct net\_if \*iface, const struct in\_addr \*addr)

Check if the given address belongs to same subnet that has been configured for the interface.

**Definition** net\_ip.h:915

[net\_ip\_protocol\_secure](group__ip__4__6.md#ga721da18d2a3cfd9b3a56e9efc9f6e58b)

net\_ip\_protocol\_secure

Protocol numbers for TLS protocols.

**Definition** net\_ip.h:75

[net\_ipaddr\_copy](group__ip__4__6.md#ga75ffcc08e621c2d47d1ae043fce2acad)

#define net\_ipaddr\_copy(dest, src)

Copy an IPv4 or IPv6 address.

**Definition** net\_ip.h:747

[net\_ip\_mtu](group__ip__4__6.md#ga7a207761e4879c140f48f93978cb2f0b)

net\_ip\_mtu

**Definition** net\_ip.h:409

[net\_rx\_priority2tc](group__ip__4__6.md#ga7b3c41ae9b3962090d72c130a9fa61b1)

int net\_rx\_priority2tc(enum net\_priority prio)

Convert Rx network packet priority to traffic class so we can place the packet into correct Rx queue.

[net\_ipv4\_is\_addr\_loopback](group__ip__4__6.md#ga879e4aed725d7ea3fe609fa989f14735)

static bool net\_ipv4\_is\_addr\_loopback(struct in\_addr \*addr)

Check if the IPv4 address is a loopback address (127.0.0.0/8).

**Definition** net\_ip.h:698

[net\_bytes\_from\_str](group__ip__4__6.md#ga8b794f251cf8412c769ab415902a9f32)

int net\_bytes\_from\_str(uint8\_t \*buf, int buf\_len, const char \*src)

Convert a string of hex values to array of bytes.

[net\_priority2vlan](group__ip__4__6.md#ga8be77d043d4d1d29e0879b3b22274629)

static uint8\_t net\_priority2vlan(enum net\_priority priority)

Convert network packet priority to network packet VLAN priority.

**Definition** net\_ip.h:1656

[net\_ipv6\_addr\_create\_v4\_mapped](group__ip__4__6.md#ga8c6162c6212051037a33477aab9fc55f)

static void net\_ipv6\_addr\_create\_v4\_mapped(const struct in\_addr \*addr4, struct in6\_addr \*addr6)

Create IPv4 mapped IPv6 address.

**Definition** net\_ip.h:1273

[net\_if\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf)

bool net\_if\_ipv4\_is\_addr\_bcast(struct net\_if \*iface, const struct in\_addr \*addr)

[net\_ipv6\_is\_prefix](group__ip__4__6.md#ga9654007b0a3c4d033df1ec3d00bd26ee)

static bool net\_ipv6\_is\_prefix(const uint8\_t \*addr1, const uint8\_t \*addr2, uint8\_t length)

Check if two IPv6 addresses are same when compared after prefix mask.

**Definition** net\_ip.h:661

[net\_ipaddr\_parse](group__ip__4__6.md#ga9918e156f0039cf45d487a112e0a2ada)

bool net\_ipaddr\_parse(const char \*str, size\_t str\_len, struct sockaddr \*addr)

Parse a string that contains either IPv4 or IPv6 address and optional port, and store the information...

[net\_ipv6\_is\_addr\_loopback](group__ip__4__6.md#gaa662667005bdc00bf1eb5cf243aad874)

static bool net\_ipv6\_is\_addr\_loopback(struct in6\_addr \*addr)

Check if the IPv6 address is a loopback address (::1).

**Definition** net\_ip.h:598

[net\_tcp\_seq\_greater](group__ip__4__6.md#gaa77b299f53e5535ac4c4bea1b6531a34)

static bool net\_tcp\_seq\_greater(uint32\_t seq1, uint32\_t seq2)

Check that one TCP sequence number is greater.

**Definition** net\_ip.h:1581

[net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c)

net\_sock\_type

Socket type.

**Definition** net\_ip.h:84

[net\_ipv6\_unspecified\_address](group__ip__4__6.md#gab0211c91e113cf01a8a16b1a106e7290)

const struct in6\_addr \* net\_ipv6\_unspecified\_address(void)

Return pointer to any (all bits zeros) IPv6 address.

[net\_ipv6\_is\_global\_addr](group__ip__4__6.md#gab2d854e2b24f866839e547c1092ccff6)

static bool net\_ipv6\_is\_global\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a global address.

**Definition** net\_ip.h:876

[net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes](group__ip__4__6.md#gaba3e1259f452381ef3e109bb2eb34c09)

static bool net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes(const struct in6\_addr \*addr)

Check if the IPv6 address is a link local scope all nodes multicast address (FF02::1).

**Definition** net\_ip.h:1189

[net\_family2str](group__ip__4__6.md#gaba4c72e3aa2ceb4ac67d25112fb36523)

const char \* net\_family2str(sa\_family\_t family)

Return network address family value as a string.

[net\_ipv4\_is\_ll\_addr](group__ip__4__6.md#gac000a319de7a6f95d4a63719bca3b865)

static bool net\_ipv4\_is\_ll\_addr(const struct in\_addr \*addr)

Check if the given IPv4 address is a link local address.

**Definition** net\_ip.h:734

[net\_can\_ptr](group__ip__4__6.md#gac2fb590a35961c04807dd985f462c5fb)

static struct sockaddr\_can\_ptr \* net\_can\_ptr(const struct sockaddr\_ptr \*addr)

Get sockaddr\_can\_ptr from sockaddr\_ptr.

**Definition** net\_ip.h:1497

[ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)

#define ntohl(x)

Convert 32-bit value from network to host byte order.

**Definition** net\_ip.h:104

[net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083)

static bool net\_ipv4\_is\_addr\_bcast(struct net\_if \*iface, const struct in\_addr \*addr)

Check if the given IPv4 address is a broadcast address.

**Definition** net\_ip.h:943

[net\_ipv6\_is\_ll\_addr](group__ip__4__6.md#gacac4279ee8896ddf2a76c612b36edf38)

static bool net\_ipv6\_is\_ll\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a link local address.

**Definition** net\_ip.h:839

[net\_sin](group__ip__4__6.md#gacccfbac6a03480840fa219e9a1924dc6)

static struct sockaddr\_in \* net\_sin(const struct sockaddr \*addr)

Get sockaddr\_in from sockaddr.

**Definition** net\_ip.h:1441

[net\_ipv4\_unspecified\_address](group__ip__4__6.md#gaceb9afdd7f2f78d96e6debd72f63ebf0)

const struct in\_addr \* net\_ipv4\_unspecified\_address(void)

Return pointer to any (all bits zeros) IPv4 address.

[net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d)

static bool net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group(const struct in6\_addr \*addr)

Check if the IPv6 address belongs to the all nodes multicast group.

**Definition** net\_ip.h:1153

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[net\_sll\_ptr](group__ip__4__6.md#gad5cf206e18769a15f9fc917e416db6ee)

static struct sockaddr\_ll\_ptr \* net\_sll\_ptr(const struct sockaddr\_ptr \*addr)

Get sockaddr\_ll\_ptr from sockaddr\_ptr.

**Definition** net\_ip.h:1483

[net\_sin6](group__ip__4__6.md#gad97b2c3da722409eada099f9b7e13f03)

static struct sockaddr\_in6 \* net\_sin6(const struct sockaddr \*addr)

Get sockaddr\_in6 from sockaddr.

**Definition** net\_ip.h:1428

[ntohs](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)

#define ntohs(x)

Convert 16-bit value from network to host byte order.

**Definition** net\_ip.h:96

[net\_if\_ipv6\_maddr\_lookup](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975)

struct net\_if\_mcast\_addr \* net\_if\_ipv6\_maddr\_lookup(const struct in6\_addr \*addr, struct net\_if \*\*iface)

[net\_ipv4\_is\_addr\_unspecified](group__ip__4__6.md#gadc623ecacf024733ab6d477d87cc4b9d)

static bool net\_ipv4\_is\_addr\_unspecified(const struct in\_addr \*addr)

Check if the IPv4 address is unspecified (all bits zero).

**Definition** net\_ip.h:710

[net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94)

static bool net\_ipv6\_is\_addr\_mcast\_scope(const struct in6\_addr \*addr, int scope)

Check if the IPv6 address is a given scope multicast address (FFyx::).

**Definition** net\_ip.h:1019

[net\_ipv6\_is\_ula\_addr](group__ip__4__6.md#gae10578b8801d213482de7d7d7e7ba230)

static bool net\_ipv6\_is\_ula\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a unique local address.

**Definition** net\_ip.h:864

[net\_ipv6\_is\_addr\_mcast\_iface](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)

static bool net\_ipv6\_is\_addr\_mcast\_iface(const struct in6\_addr \*addr)

Check if the IPv6 address is a interface scope multicast address (FFx1::).

**Definition** net\_ip.h:1062

[htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)

#define htonl(x)

Convert 32-bit value from host to network byte order.

**Definition** net\_ip.h:128

[net\_tx\_priority2tc](group__ip__4__6.md#gae74c9ba7ff4addbce7f931bd6fa91fa0)

int net\_tx\_priority2tc(enum net\_priority prio)

Convert Tx network packet priority to traffic class so we can place the packet into correct Tx queue.

[net\_sin6\_ptr](group__ip__4__6.md#gae86d2cd402142190e1ea1c120a57939f)

static struct sockaddr\_in6\_ptr \* net\_sin6\_ptr(const struct sockaddr\_ptr \*addr)

Get sockaddr\_in6\_ptr from sockaddr\_ptr.

**Definition** net\_ip.h:1455

[net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd)

net\_priority

Network packet priority settings described in IEEE 802.1Q Annex I.1.

**Definition** net\_ip.h:422

[net\_ipv4\_is\_addr\_mcast](group__ip__4__6.md#gae8c3302cf9ca457de32eabcf65975b70)

static bool net\_ipv4\_is\_addr\_mcast(const struct in\_addr \*addr)

Check if the IPv4 address is a multicast address.

**Definition** net\_ip.h:722

[net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)

net\_ip\_protocol

Protocol numbers from IANA/BSD.

**Definition** net\_ip.h:62

[net\_ipv6\_addr\_based\_on\_ll](group__ip__4__6.md#gaf4b0c30b926748625bd3c4c81d06ffc5)

static bool net\_ipv6\_addr\_based\_on\_ll(const struct in6\_addr \*addr, const struct net\_linkaddr \*lladdr)

Check if given address is based on link layer address.

**Definition** net\_ip.h:1362

[net\_ipv4\_addr\_copy\_raw](group__ip__4__6.md#gaf731738fb1761208739976d767736f87)

static void net\_ipv4\_addr\_copy\_raw(uint8\_t \*dest, const uint8\_t \*src)

Copy an IPv4 address raw buffer.

**Definition** net\_ip.h:756

[net\_ipv6\_is\_my\_maddr](group__ip__4__6.md#gaf8c5158de9a65d840faa61bb3dec341c)

static bool net\_ipv6\_is\_my\_maddr(struct in6\_addr \*maddr)

Check if IPv6 multicast address is found in one of the network interfaces.

**Definition** net\_ip.h:647

[net\_ipv6\_addr\_cmp\_raw](group__ip__4__6.md#gafbe40461a645cf11fc8b3a07e1d9156e)

static bool net\_ipv6\_addr\_cmp\_raw(const uint8\_t \*addr1, const uint8\_t \*addr2)

Compare two raw IPv6 address buffers.

**Definition** net\_ip.h:825

[net\_ipv6\_is\_addr\_unspecified](group__ip__4__6.md#gafe2c8dc0bdb677ba9bc872d051aab2a0)

static bool net\_ipv6\_is\_addr\_unspecified(const struct in6\_addr \*addr)

Check if the IPv6 address is unspecified (all bits zero).

**Definition** net\_ip.h:984

[net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41)

net\_addr\_type

How the network address is assigned to network interface.

**Definition** net\_ip.h:453

[NET\_ADDR\_ANY\_STATE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df)

@ NET\_ADDR\_ANY\_STATE

Default (invalid) address type.

**Definition** net\_ip.h:446

[NET\_ADDR\_TENTATIVE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9)

@ NET\_ADDR\_TENTATIVE

Tentative address.

**Definition** net\_ip.h:447

[NET\_ADDR\_DEPRECATED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3)

@ NET\_ADDR\_DEPRECATED

Deprecated address.

**Definition** net\_ip.h:449

[NET\_ADDR\_PREFERRED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a)

@ NET\_ADDR\_PREFERRED

Preferred address.

**Definition** net\_ip.h:448

[IPPROTO\_TLS\_1\_1](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba102692f9f57dd0ec6f8c6cb54a235d4c)

@ IPPROTO\_TLS\_1\_1

TLS 1.1 protocol.

**Definition** net\_ip.h:77

[IPPROTO\_TLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba6d479e64d940cea948c874d36c656fcc)

@ IPPROTO\_TLS\_1\_0

TLS 1.0 protocol.

**Definition** net\_ip.h:76

[IPPROTO\_DTLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba92e94005d7a80aacbffad2f3f10555ef)

@ IPPROTO\_DTLS\_1\_0

DTLS 1.0 protocol.

**Definition** net\_ip.h:79

[IPPROTO\_TLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa5e176fa47ca23a6f25101a5203f8e5a)

@ IPPROTO\_TLS\_1\_2

TLS 1.2 protocol.

**Definition** net\_ip.h:78

[IPPROTO\_DTLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58bad4d2a6ca8756ee52221f19fb06c34a1c)

@ IPPROTO\_DTLS\_1\_2

DTLS 1.2 protocol.

**Definition** net\_ip.h:80

[NET\_IPV4\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1)

@ NET\_IPV4\_MTU

IPv4 MTU length.

**Definition** net\_ip.h:418

[NET\_IPV6\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c)

@ NET\_IPV6\_MTU

IPv6 MTU length.

**Definition** net\_ip.h:413

[SOCK\_DGRAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc)

@ SOCK\_DGRAM

Datagram socket type.

**Definition** net\_ip.h:86

[SOCK\_RAW](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231)

@ SOCK\_RAW

RAW socket type.

**Definition** net\_ip.h:87

[SOCK\_STREAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424)

@ SOCK\_STREAM

Stream socket type.

**Definition** net\_ip.h:85

[NET\_PRIORITY\_NC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef)

@ NET\_PRIORITY\_NC

Network control (highest).

**Definition** net\_ip.h:430

[NET\_PRIORITY\_IC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05)

@ NET\_PRIORITY\_IC

Internetwork control.

**Definition** net\_ip.h:429

[NET\_PRIORITY\_CA](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354)

@ NET\_PRIORITY\_CA

Critical applications.

**Definition** net\_ip.h:426

[NET\_PRIORITY\_VO](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a)

@ NET\_PRIORITY\_VO

Voice, < 10 ms latency and jitter.

**Definition** net\_ip.h:428

[NET\_PRIORITY\_VI](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792)

@ NET\_PRIORITY\_VI

Video, < 100 ms latency and jitter.

**Definition** net\_ip.h:427

[NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce)

@ NET\_PRIORITY\_BE

Best effort (default).

**Definition** net\_ip.h:424

[NET\_PRIORITY\_EE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0)

@ NET\_PRIORITY\_EE

Excellent effort.

**Definition** net\_ip.h:425

[NET\_PRIORITY\_BK](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b)

@ NET\_PRIORITY\_BK

Background (lowest).

**Definition** net\_ip.h:423

[IPPROTO\_IP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a334b0a4a5a3e331e7c7864471e9eab08)

@ IPPROTO\_IP

IP protocol (pseudo-val for setsockopt().

**Definition** net\_ip.h:63

[IPPROTO\_RAW](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a3f186705d5c21da1b72ecb91cca1f7a4)

@ IPPROTO\_RAW

RAW IP packets.

**Definition** net\_ip.h:71

[IPPROTO\_IPIP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a49a42f6d628bf65e78478e8eb4874ff2)

@ IPPROTO\_IPIP

IPIP tunnels.

**Definition** net\_ip.h:66

[IPPROTO\_TCP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4a3c433d15859f62bacc06312791a45e)

@ IPPROTO\_TCP

TCP protocol.

**Definition** net\_ip.h:67

[IPPROTO\_IGMP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4cbcb48be0cd8eb6fb5b5741f1c7b639)

@ IPPROTO\_IGMP

IGMP protocol.

**Definition** net\_ip.h:65

[IPPROTO\_ICMP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a7ccd735b73f6955ae2f4abf3e7ca6bb4)

@ IPPROTO\_ICMP

ICMP protocol.

**Definition** net\_ip.h:64

[IPPROTO\_IPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a892549243e60ed1e04e88a14b44d8185)

@ IPPROTO\_IPV6

IPv6 protocol.

**Definition** net\_ip.h:69

[IPPROTO\_UDP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31abd7dfb22e255a4eed332f41de12d7321)

@ IPPROTO\_UDP

UDP protocol.

**Definition** net\_ip.h:68

[IPPROTO\_ICMPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31aeeff57e3cf726718a92b2138e5842926)

@ IPPROTO\_ICMPV6

ICMPv6 protocol.

**Definition** net\_ip.h:70

[NET\_ADDR\_ANY](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6)

@ NET\_ADDR\_ANY

Default value.

**Definition** net\_ip.h:455

[NET\_ADDR\_OVERRIDABLE](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4)

@ NET\_ADDR\_OVERRIDABLE

Manually set address which is overridable by DHCP.

**Definition** net\_ip.h:463

[NET\_ADDR\_DHCP](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db)

@ NET\_ADDR\_DHCP

Address is from DHCP.

**Definition** net\_ip.h:459

[NET\_ADDR\_MANUAL](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e)

@ NET\_ADDR\_MANUAL

Manually set address.

**Definition** net\_ip.h:461

[NET\_ADDR\_AUTOCONF](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006)

@ NET\_ADDR\_AUTOCONF

Auto configured address.

**Definition** net\_ip.h:457

[NET\_LINK\_IEEE802154](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3)

@ NET\_LINK\_IEEE802154

IEEE 802.15.4 link address.

**Definition** net\_linkaddr.h:51

[NET\_LINK\_ETHERNET](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)

@ NET\_LINK\_ETHERNET

Ethernet link address.

**Definition** net\_linkaddr.h:55

[NET\_LINK\_BLUETOOTH](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a)

@ NET\_LINK\_BLUETOOTH

Bluetooth IPSP link address.

**Definition** net\_linkaddr.h:53

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:124

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

[memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)

int memcmp(const void \*m1, const void \*m2, size\_t n)

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[cmsghdr](structcmsghdr.md)

**Definition** net\_ip.h:248

[cmsghdr::cmsg\_type](structcmsghdr.md#a4c7cabf7899a688ce10bc92773fca9c1)

int cmsg\_type

**Definition** net\_ip.h:251

[cmsghdr::cmsg\_len](structcmsghdr.md#a7cf479e5e162e65ad164616453d61df2)

socklen\_t cmsg\_len

**Definition** net\_ip.h:249

[cmsghdr::cmsg\_data](structcmsghdr.md#a92c00d02575707f72c04f090b6f8d399)

z\_max\_align\_t cmsg\_data[]

**Definition** net\_ip.h:253

[cmsghdr::cmsg\_level](structcmsghdr.md#ac0ff1400cb63fbc2e0ece19434cb8fef)

int cmsg\_level

**Definition** net\_ip.h:250

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:139

[in6\_addr::s6\_addr](structin6__addr.md#aa1d600770ac35faa253a53aecd9b3786)

uint8\_t s6\_addr[16]

**Definition** net\_ip.h:141

[in6\_addr::s6\_addr32](structin6__addr.md#ab436399c6fe320d361b024bf78af4aba)

uint32\_t s6\_addr32[4]

**Definition** net\_ip.h:143

[in6\_addr::s6\_addr16](structin6__addr.md#ac639658b289173e364d9e067ec2ceb69)

uint16\_t s6\_addr16[8]

**Definition** net\_ip.h:142

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:151

[in\_addr::s4\_addr](structin__addr.md#a4fd35e401c510fabab8979eb8416dd9b)

uint8\_t s4\_addr[4]

**Definition** net\_ip.h:153

[in\_addr::s\_addr](structin__addr.md#a5abe94a260a50619a60ce111a59f00b5)

uint32\_t s\_addr

**Definition** net\_ip.h:156

[in\_addr::s4\_addr16](structin__addr.md#ab3122fff9d58baf7dc4f12c6f021fd86)

uint16\_t s4\_addr16[2]

**Definition** net\_ip.h:154

[in\_addr::s4\_addr32](structin__addr.md#ae4e092a27efb643067d7ce10bd454bed)

uint32\_t s4\_addr32[1]

**Definition** net\_ip.h:155

[iovec](structiovec.md)

**Definition** net\_ip.h:232

[iovec::iov\_base](structiovec.md#a07aeddeccf80f14520fdd7ef0759442b)

void \* iov\_base

**Definition** net\_ip.h:233

[iovec::iov\_len](structiovec.md#a17b5ac2078fd1adfabb262a95808a07d)

size\_t iov\_len

**Definition** net\_ip.h:234

[msghdr](structmsghdr.md)

**Definition** net\_ip.h:238

[msghdr::msg\_iov](structmsghdr.md#a1b893a6f84c4ba52708c5dcfcc720293)

struct iovec \* msg\_iov

**Definition** net\_ip.h:241

[msghdr::msg\_namelen](structmsghdr.md#a47762b69eee1c9ba5736d64516ea0960)

socklen\_t msg\_namelen

**Definition** net\_ip.h:240

[msghdr::msg\_name](structmsghdr.md#a691a8866b21c7083974a2ff1e7987ce1)

void \* msg\_name

**Definition** net\_ip.h:239

[msghdr::msg\_flags](structmsghdr.md#a9e8ff97d402c99551cbfd564e9e10a74)

int msg\_flags

**Definition** net\_ip.h:245

[msghdr::msg\_controllen](structmsghdr.md#a9fa41b0e9a02b5dc9a01aa6f18108adb)

size\_t msg\_controllen

**Definition** net\_ip.h:244

[msghdr::msg\_iovlen](structmsghdr.md#ad4ef1bd6821e599bf42f936850d2c4d7)

size\_t msg\_iovlen

**Definition** net\_ip.h:242

[msghdr::msg\_control](structmsghdr.md#afba5fc31b0f197e25602d2232ca6d783)

void \* msg\_control

**Definition** net\_ip.h:243

[net\_if\_addr](structnet__if__addr.md)

Network Interface unicast IP addresses.

**Definition** net\_if.h:52

[net\_if\_config](structnet__if__config.md)

IP and other configuration related data for network interface.

**Definition** net\_if.h:492

[net\_if\_mcast\_addr](structnet__if__mcast__addr.md)

Network Interface multicast IP addresses.

**Definition** net\_if.h:93

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[net\_linkaddr](structnet__linkaddr.md)

Hardware link address structure.

**Definition** net\_linkaddr.h:67

[net\_linkaddr::addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)

uint8\_t \* addr

The array of byte representing the address.

**Definition** net\_linkaddr.h:69

[net\_linkaddr::type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7)

uint8\_t type

What kind of address is this for.

**Definition** net\_linkaddr.h:75

[net\_linkaddr::len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)

uint8\_t len

Length of that address array.

**Definition** net\_linkaddr.h:72

[net\_tuple](structnet__tuple.md)

IPv6/IPv4 network connection tuple.

**Definition** net\_ip.h:436

[net\_tuple::remote\_addr](structnet__tuple.md#a8f9a1aab3c3aedeead795ca6624d4d6d)

struct net\_addr \* remote\_addr

IPv6/IPv4 remote address.

**Definition** net\_ip.h:437

[net\_tuple::local\_port](structnet__tuple.md#a9a1cd0dd55a9e866cb0e910120362b7e)

uint16\_t local\_port

UDP/TCP local port.

**Definition** net\_ip.h:440

[net\_tuple::ip\_proto](structnet__tuple.md#aa9eeba2c8e263afbf6368e04353d6014)

enum net\_ip\_protocol ip\_proto

IP protocol.

**Definition** net\_ip.h:441

[net\_tuple::remote\_port](structnet__tuple.md#ab4c31093a23bc60d8dcf5b784e3fb39a)

uint16\_t remote\_port

UDP/TCP remote port.

**Definition** net\_ip.h:439

[net\_tuple::local\_addr](structnet__tuple.md#af7004f8f8d74d49d6771393825612294)

struct net\_addr \* local\_addr

IPv6/IPv4 local address.

**Definition** net\_ip.h:438

[sockaddr\_can\_ptr](structsockaddr__can__ptr.md)

**Definition** net\_ip.h:226

[sockaddr\_can\_ptr::can\_family](structsockaddr__can__ptr.md#a37eebdcc4598e3f55eeaa954e77981fb)

sa\_family\_t can\_family

**Definition** net\_ip.h:227

[sockaddr\_can\_ptr::can\_ifindex](structsockaddr__can__ptr.md#a7a181132dfcb2cb7c2bc1cc2deb1814b)

int can\_ifindex

**Definition** net\_ip.h:228

[sockaddr\_in6\_ptr](structsockaddr__in6__ptr.md)

**Definition** net\_ip.h:185

[sockaddr\_in6\_ptr::sin6\_family](structsockaddr__in6__ptr.md#a5de1da662d5fb57417a593cee8cc82de)

sa\_family\_t sin6\_family

**Definition** net\_ip.h:186

[sockaddr\_in6\_ptr::sin6\_port](structsockaddr__in6__ptr.md#a64be2e93c2453899af630428089086cc)

uint16\_t sin6\_port

**Definition** net\_ip.h:187

[sockaddr\_in6\_ptr::sin6\_scope\_id](structsockaddr__in6__ptr.md#a9fe0b00f5081d4e027e15497304bc55b)

uint8\_t sin6\_scope\_id

**Definition** net\_ip.h:189

[sockaddr\_in6\_ptr::sin6\_addr](structsockaddr__in6__ptr.md#af594f9662b0785a8f527bb9fcb95d92d)

struct in6\_addr \* sin6\_addr

**Definition** net\_ip.h:188

[sockaddr\_in6](structsockaddr__in6.md)

Socket address struct for IPv6.

**Definition** net\_ip.h:178

[sockaddr\_in6::sin6\_scope\_id](structsockaddr__in6.md#a1daad78c9848862ab33a48e05fa8cf17)

uint8\_t sin6\_scope\_id

**Definition** net\_ip.h:182

[sockaddr\_in6::sin6\_addr](structsockaddr__in6.md#a219e7f3ecd6d7dcf8fc2465475be490f)

struct in6\_addr sin6\_addr

**Definition** net\_ip.h:181

[sockaddr\_in6::sin6\_port](structsockaddr__in6.md#a4fc2b7a478d258e9e778772701096022)

uint16\_t sin6\_port

**Definition** net\_ip.h:180

[sockaddr\_in6::sin6\_family](structsockaddr__in6.md#aefa41e43be9c615f8cfd6266c0ed1687)

sa\_family\_t sin6\_family

**Definition** net\_ip.h:179

[sockaddr\_in\_ptr](structsockaddr__in__ptr.md)

**Definition** net\_ip.h:199

[sockaddr\_in\_ptr::sin\_addr](structsockaddr__in__ptr.md#a02d48b07cb42745a729428fc9f4af765)

struct in\_addr \* sin\_addr

**Definition** net\_ip.h:202

[sockaddr\_in\_ptr::sin\_port](structsockaddr__in__ptr.md#aab1491a8d77ca11d8104ef3ef1bace80)

uint16\_t sin\_port

**Definition** net\_ip.h:201

[sockaddr\_in\_ptr::sin\_family](structsockaddr__in__ptr.md#ae8ca040f7813d6974e0440f877df6744)

sa\_family\_t sin\_family

**Definition** net\_ip.h:200

[sockaddr\_in](structsockaddr__in.md)

Socket address struct for IPv4.

**Definition** net\_ip.h:193

[sockaddr\_in::sin\_port](structsockaddr__in.md#a3cf9239fdd8bd32855d66a4b86349fbb)

uint16\_t sin\_port

**Definition** net\_ip.h:195

[sockaddr\_in::sin\_addr](structsockaddr__in.md#a4ea5f2f1138e5c8597097db255a9ec6c)

struct in\_addr sin\_addr

**Definition** net\_ip.h:196

[sockaddr\_in::sin\_family](structsockaddr__in.md#a9a7d98bb8e18f4a06a021c32d6cc7117)

sa\_family\_t sin\_family

**Definition** net\_ip.h:194

[sockaddr\_ll\_ptr](structsockaddr__ll__ptr.md)

**Definition** net\_ip.h:216

[sockaddr\_ll\_ptr::sll\_addr](structsockaddr__ll__ptr.md#a28579052ff6eda21d5f060e2c8de2421)

uint8\_t \* sll\_addr

**Definition** net\_ip.h:223

[sockaddr\_ll\_ptr::sll\_hatype](structsockaddr__ll__ptr.md#a337cef9822b70d31b50135f158c54b5d)

uint16\_t sll\_hatype

**Definition** net\_ip.h:220

[sockaddr\_ll\_ptr::sll\_ifindex](structsockaddr__ll__ptr.md#a47a2543cc247cba79cbaaf82787aa9cf)

int sll\_ifindex

**Definition** net\_ip.h:219

[sockaddr\_ll\_ptr::sll\_pkttype](structsockaddr__ll__ptr.md#a6fa3dcd69fefa59a6da37bde8160104b)

uint8\_t sll\_pkttype

**Definition** net\_ip.h:221

[sockaddr\_ll\_ptr::sll\_family](structsockaddr__ll__ptr.md#aab6bfff94bf5880375e7538be72a11c1)

sa\_family\_t sll\_family

**Definition** net\_ip.h:217

[sockaddr\_ll\_ptr::sll\_halen](structsockaddr__ll__ptr.md#ab27a07520cee5183aa62e7a0615f1c5f)

uint8\_t sll\_halen

**Definition** net\_ip.h:222

[sockaddr\_ll\_ptr::sll\_protocol](structsockaddr__ll__ptr.md#ad25fe5fef518de3652cf67d25582e50c)

uint16\_t sll\_protocol

**Definition** net\_ip.h:218

[sockaddr\_ll](structsockaddr__ll.md)

Socket address struct for packet socket.

**Definition** net\_ip.h:206

[sockaddr\_ll::sll\_pkttype](structsockaddr__ll.md#a2001fcf2627149283e3460b18f44b313)

uint8\_t sll\_pkttype

**Definition** net\_ip.h:211

[sockaddr\_ll::sll\_hatype](structsockaddr__ll.md#a2df317106a30498dd9f87e1d4eefc8fc)

uint16\_t sll\_hatype

**Definition** net\_ip.h:210

[sockaddr\_ll::sll\_family](structsockaddr__ll.md#a4920e92fb0613ba8594a6b6c226048d9)

sa\_family\_t sll\_family

**Definition** net\_ip.h:207

[sockaddr\_ll::sll\_protocol](structsockaddr__ll.md#a661e329c10a8f06a85ad831630273e49)

uint16\_t sll\_protocol

**Definition** net\_ip.h:208

[sockaddr\_ll::sll\_ifindex](structsockaddr__ll.md#a93b4976ed8e9d58cdcc620f5d1987f68)

int sll\_ifindex

**Definition** net\_ip.h:209

[sockaddr\_ll::sll\_halen](structsockaddr__ll.md#acb72ab39a239d9e5752b7422dc9a2dc6)

uint8\_t sll\_halen

**Definition** net\_ip.h:212

[sockaddr\_ll::sll\_addr](structsockaddr__ll.md#aee52affe8837ffe1c32c94ce34117d6a)

uint8\_t sll\_addr[8]

**Definition** net\_ip.h:213

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:347

[sockaddr::data](structsockaddr.md#a3d44571051f408599343acfc2c95d244)

char data[NET\_SOCKADDR\_MAX\_SIZE - sizeof(sa\_family\_t)]

**Definition** net\_ip.h:349

[sockaddr::sa\_family](structsockaddr.md#ac6ef02e9a2e90a30218132ffd7b5a5c5)

sa\_family\_t sa\_family

**Definition** net\_ip.h:348

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_ip.h](net__ip_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
