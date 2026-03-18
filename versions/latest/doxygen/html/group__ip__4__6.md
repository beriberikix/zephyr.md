---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__ip__4__6.html
original_path: doxygen/html/group__ip__4__6.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

IPv4/IPv6 primitives and helpers

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

IPv4/IPv6 primitives and helpers.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [in6\_addr](structin6__addr.md) |
|  | IPv6 address struct. [More...](structin6__addr.md#details) |
| struct | [in\_addr](structin__addr.md) |
|  | IPv4 address struct. [More...](structin__addr.md#details) |
| struct | [sockaddr\_in6](structsockaddr__in6.md) |
|  | Socket address struct for IPv6. [More...](structsockaddr__in6.md#details) |
| struct | [sockaddr\_in6\_ptr](structsockaddr__in6__ptr.md) |
| struct | [sockaddr\_in](structsockaddr__in.md) |
|  | Socket address struct for IPv4. [More...](structsockaddr__in.md#details) |
| struct | [sockaddr\_in\_ptr](structsockaddr__in__ptr.md) |
| struct | [sockaddr\_ll](structsockaddr__ll.md) |
|  | Socket address struct for packet socket. [More...](structsockaddr__ll.md#details) |
| struct | [sockaddr\_ll\_ptr](structsockaddr__ll__ptr.md) |
| struct | [sockaddr\_can\_ptr](structsockaddr__can__ptr.md) |
| struct | [iovec](structiovec.md) |
| struct | [msghdr](structmsghdr.md) |
| struct | [cmsghdr](structcmsghdr.md) |
| struct | [sockaddr](structsockaddr.md) |
|  | Generic sockaddr struct. [More...](structsockaddr.md#details) |
| struct | [net\_tuple](structnet__tuple.md) |
|  | IPv6/IPv4 network connection tuple. [More...](structnet__tuple.md#details) |

| Macros | |
| --- | --- |
| #define | [PF\_UNSPEC](#ga51dba11ffc8e3b1bf695e721b3144094)   0 |
|  | Unspecified protocol family. |
| #define | [PF\_INET](#ga3f5da0b5be27fe31ec7cc11bfa8d1a25)   1 |
|  | IP protocol family version 4. |
| #define | [PF\_INET6](#ga323f2649198fc7e64b19881869265618)   2 |
|  | IP protocol family version 6. |
| #define | [PF\_PACKET](#ga8e297adb5fe2e28b0d9d921a5d56a8e9)   3 |
|  | Packet family. |
| #define | [PF\_CAN](#gaeac0c3db7a1e021f17987bcc76893849)   4 |
|  | Controller Area Network. |
| #define | [PF\_NET\_MGMT](#ga288b09307bcc46aef2acf2af5e3e1006)   5 |
|  | Network management info. |
| #define | [PF\_LOCAL](#ga521c315ca2a2a4e6345878e84af4085e)   6 |
|  | Inter-process communication. |
| #define | [PF\_UNIX](#ga0407288f5fb975a03b21d5287c282b2e)   [PF\_LOCAL](#ga521c315ca2a2a4e6345878e84af4085e) |
|  | Inter-process communication. |
| #define | [AF\_UNSPEC](#gae77ae24b14b7b7f294f3e04121173f12)   [PF\_UNSPEC](#ga51dba11ffc8e3b1bf695e721b3144094) |
|  | Unspecified address family. |
| #define | [AF\_INET](#ga9930604d0e32588eae76f43ca38e7826)   [PF\_INET](#ga3f5da0b5be27fe31ec7cc11bfa8d1a25) |
|  | IP protocol family version 4. |
| #define | [AF\_INET6](#gaa03706b2738b9a58d4985dfbe99e1bac)   [PF\_INET6](#ga323f2649198fc7e64b19881869265618) |
|  | IP protocol family version 6. |
| #define | [AF\_PACKET](#gaa89aa4cd481fe17260c3f5d493cc23f5)   [PF\_PACKET](#ga8e297adb5fe2e28b0d9d921a5d56a8e9) |
|  | Packet family. |
| #define | [AF\_CAN](#ga546620c7e758f003b24b7fdae4f97bd4)   [PF\_CAN](#gaeac0c3db7a1e021f17987bcc76893849) |
|  | Controller Area Network. |
| #define | [AF\_NET\_MGMT](#ga41d0cbb55cd9550a7f732b1520119c15)   [PF\_NET\_MGMT](#ga288b09307bcc46aef2acf2af5e3e1006) |
|  | Network management info. |
| #define | [AF\_LOCAL](#gae24f1f9ea44fcce3affcb2137f593dc1)   [PF\_LOCAL](#ga521c315ca2a2a4e6345878e84af4085e) |
|  | Inter-process communication. |
| #define | [AF\_UNIX](#ga0fd8739854bc8b48d65f0b669fed3ffe)   [PF\_UNIX](#ga0407288f5fb975a03b21d5287c282b2e) |
|  | Inter-process communication. |
| #define | [ntohs](#gada37feda716b4ba89cf9dba34288141d)(x) |
|  | Convert 16-bit value from network to host byte order. |
| #define | [ntohl](#gac317b3e903719ba02894f1710f7f2439)(x) |
|  | Convert 32-bit value from network to host byte order. |
| #define | [ntohll](#ga3cfcf123d4ead264289232f91f2c9ca5)(x) |
|  | Convert 64-bit value from network to host byte order. |
| #define | [htons](#ga51799f5ebb4c7228ef7e95c247030f42)(x) |
|  | Convert 16-bit value from host to network byte order. |
| #define | [htonl](#gae4027a6ad07f13aa12eab285a1b46019)(x) |
|  | Convert 32-bit value from host to network byte order. |
| #define | [htonll](#ga9f4bf0773c45ad9a9753a1b784a13fbb)(x) |
|  | Convert 64-bit value from host to network byte order. |
| #define | [NET\_IPV6\_ADDR\_SIZE](#ga1eefdabf590090be9f98bdf4a2f43bb4)   16 |
| #define | [NET\_IPV4\_ADDR\_SIZE](#ga10a82ea9ba9ca19f3b773bdd53c978e0)   4 |
| #define | [ALIGN\_H](#ga051015580ee95f46da1d68f6be2b333d)(x) |
| #define | [ALIGN\_D](#gab67ab3f70af998e71325fb26ea0f6a83)(x) |
| #define | [CMSG\_FIRSTHDR](#ga39567a31d167fc53336d2ab4a2cd78a4)([msghdr](structmsghdr.md)) |
| #define | [CMSG\_NXTHDR](#ga77c17efca635d597cb6e98b28172bdc0)([msghdr](structmsghdr.md), cmsg) |
| #define | [CMSG\_DATA](#ga5ab6d56e410ac0904107e84aeb1484cc)(cmsg) |
| #define | [CMSG\_SPACE](#ga8db11d639dd07c723256f3bb5bc89044)(length) |
| #define | [CMSG\_LEN](#gadb36e4ff4fa9a0c6730321c4bfcf64bc)(length) |
| #define | [INET\_ADDRSTRLEN](#ga93b37007689284fd9c4bde1a8f4b9199)   16 |
|  | Max length of the IPv4 address as a string. |
| #define | [INET6\_ADDRSTRLEN](#gaf776b22a727aae7c9f4d869d50df47e8)   46 |
|  | Max length of the IPv6 address as a string. |
| #define | [NET\_MAX\_PRIORITIES](#ga5b32bdfc249437709bb25bd95ec7d6d7)   8 /\* How many priority values there are \*/ |
| #define | [net\_ipaddr\_copy](#ga75ffcc08e621c2d47d1ae043fce2acad)(dest, src) |
|  | Copy an IPv4 or IPv6 address. |

| Typedefs | |
| --- | --- |
| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short int | [sa\_family\_t](#ga2d9e094abb99ebd0874373edf1c45eda) |
|  | Socket address family type. |
| typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [socklen\_t](#gacf0ed818b0a3c85ff6a9206679d6d91a) |
|  | Length of a socket address. |

| Enumerations | |
| --- | --- |
| enum | [net\_ip\_protocol](#gaf06819bf427cc58be1229b27b373ca31) {     [IPPROTO\_IP](#ggaf06819bf427cc58be1229b27b373ca31a334b0a4a5a3e331e7c7864471e9eab08) = 0 , [IPPROTO\_ICMP](#ggaf06819bf427cc58be1229b27b373ca31a7ccd735b73f6955ae2f4abf3e7ca6bb4) = 1 , [IPPROTO\_IGMP](#ggaf06819bf427cc58be1229b27b373ca31a4cbcb48be0cd8eb6fb5b5741f1c7b639) = 2 , [IPPROTO\_IPIP](#ggaf06819bf427cc58be1229b27b373ca31a49a42f6d628bf65e78478e8eb4874ff2) = 4 ,     [IPPROTO\_TCP](#ggaf06819bf427cc58be1229b27b373ca31a4a3c433d15859f62bacc06312791a45e) = 6 , [IPPROTO\_UDP](#ggaf06819bf427cc58be1229b27b373ca31abd7dfb22e255a4eed332f41de12d7321) = 17 , [IPPROTO\_IPV6](#ggaf06819bf427cc58be1229b27b373ca31a892549243e60ed1e04e88a14b44d8185) = 41 , [IPPROTO\_ICMPV6](#ggaf06819bf427cc58be1229b27b373ca31aeeff57e3cf726718a92b2138e5842926) = 58 ,     [IPPROTO\_RAW](#ggaf06819bf427cc58be1229b27b373ca31a3f186705d5c21da1b72ecb91cca1f7a4) = 255   } |
|  | Protocol numbers from IANA/BSD. [More...](#gaf06819bf427cc58be1229b27b373ca31) |
| enum | [net\_ip\_protocol\_secure](#ga721da18d2a3cfd9b3a56e9efc9f6e58b) {     [IPPROTO\_TLS\_1\_0](#gga721da18d2a3cfd9b3a56e9efc9f6e58ba6d479e64d940cea948c874d36c656fcc) = 256 , [IPPROTO\_TLS\_1\_1](#gga721da18d2a3cfd9b3a56e9efc9f6e58ba102692f9f57dd0ec6f8c6cb54a235d4c) = 257 , [IPPROTO\_TLS\_1\_2](#gga721da18d2a3cfd9b3a56e9efc9f6e58baa5e176fa47ca23a6f25101a5203f8e5a) = 258 , [IPPROTO\_DTLS\_1\_0](#gga721da18d2a3cfd9b3a56e9efc9f6e58ba92e94005d7a80aacbffad2f3f10555ef) = 272 ,     [IPPROTO\_DTLS\_1\_2](#gga721da18d2a3cfd9b3a56e9efc9f6e58bad4d2a6ca8756ee52221f19fb06c34a1c) = 273   } |
|  | Protocol numbers for TLS protocols. [More...](#ga721da18d2a3cfd9b3a56e9efc9f6e58b) |
| enum | [net\_sock\_type](#gaaab4268707dbe08348b98fb028e7aa5c) { [SOCK\_STREAM](#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424) = 1 , [SOCK\_DGRAM](#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc) , [SOCK\_RAW](#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231) } |
|  | Socket type. [More...](#gaaab4268707dbe08348b98fb028e7aa5c) |
| enum | [net\_ip\_mtu](#ga7a207761e4879c140f48f93978cb2f0b) { [NET\_IPV6\_MTU](#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c) = 1280 , [NET\_IPV4\_MTU](#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1) = 576 } |
| enum | [net\_priority](#gae87ef466e77ded673ed7e593d3eddffd) {     [NET\_PRIORITY\_BK](#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b) = 1 , [NET\_PRIORITY\_BE](#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce) = 0 , [NET\_PRIORITY\_EE](#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0) = 2 , [NET\_PRIORITY\_CA](#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354) = 3 ,     [NET\_PRIORITY\_VI](#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792) = 4 , [NET\_PRIORITY\_VO](#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a) = 5 , [NET\_PRIORITY\_IC](#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05) = 6 , [NET\_PRIORITY\_NC](#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef) = 7   } |
|  | Network packet priority settings described in IEEE 802.1Q Annex I.1. [More...](#gae87ef466e77ded673ed7e593d3eddffd) |
| enum | [net\_addr\_state](#ga32e58fc83532ef57eeb6ff952f17288d) { [NET\_ADDR\_ANY\_STATE](#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df) = -1 , [NET\_ADDR\_TENTATIVE](#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9) = 0 , [NET\_ADDR\_PREFERRED](#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a) , [NET\_ADDR\_DEPRECATED](#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3) } |
|  | What is the current state of the network address. [More...](#ga32e58fc83532ef57eeb6ff952f17288d) |
| enum | [net\_addr\_type](#gafecee2d4a331dc85ad962b81a6303e41) {     [NET\_ADDR\_ANY](#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6) = 0 , [NET\_ADDR\_AUTOCONF](#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006) , [NET\_ADDR\_DHCP](#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db) , [NET\_ADDR\_MANUAL](#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e) ,     [NET\_ADDR\_OVERRIDABLE](#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4)   } |
|  | How the network address is assigned to network interface. [More...](#gafecee2d4a331dc85ad962b81a6303e41) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_loopback](#gaa662667005bdc00bf1eb5cf243aad874) (struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a loopback address (::1). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast](#ga1a2fb0427eeab1a5dec6d69208ad7f02) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a multicast address. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv6\_addr\_lookup](#ga13b5a26fc672d15697f99e85543184bb) (const struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_my\_addr](#ga00853528daf79c947dcdc320035ed538) (struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if IPv6 address is found in one of the network interfaces. |
| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | [net\_if\_ipv6\_maddr\_lookup](#gadb4031153c4fef86110879befa6b9975) (const struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_my\_maddr](#gaf8c5158de9a65d840faa61bb3dec341c) (struct [in6\_addr](structin6__addr.md) \*maddr) |
|  | Check if IPv6 multicast address is found in one of the network interfaces. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_prefix](#ga9654007b0a3c4d033df1ec3d00bd26ee) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) length) |
|  | Check if two IPv6 addresses are same when compared after prefix mask. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_addr\_loopback](#ga879e4aed725d7ea3fe609fa989f14735) (struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the IPv4 address is a loopback address (127.0.0.0/8). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_addr\_unspecified](#gadc623ecacf024733ab6d477d87cc4b9d) (const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the IPv4 address is unspecified (all bits zero). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_addr\_mcast](#gae8c3302cf9ca457de32eabcf65975b70) (const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the IPv4 address is a multicast address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_ll\_addr](#gac000a319de7a6f95d4a63719bca3b865) (const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the given IPv4 address is a link local address. |
| static void | [net\_ipv4\_addr\_copy\_raw](#gaf731738fb1761208739976d767736f87) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dest, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src) |
|  | Copy an IPv4 address raw buffer. |
| static void | [net\_ipv6\_addr\_copy\_raw](#ga4925e6f3734b8fc1d9cb1ca1a510b5f1) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dest, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src) |
|  | Copy an IPv6 address raw buffer. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_addr\_cmp](#ga0bdcc8dad8eb42c02426e55378ececf8) (const struct [in\_addr](structin__addr.md) \*addr1, const struct [in\_addr](structin__addr.md) \*addr2) |
|  | Compare two IPv4 addresses. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_addr\_cmp\_raw](#ga32ffb42c62169ac9b34a0faa7c7ffd12) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2) |
|  | Compare two raw IPv4 address buffers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_addr\_cmp](#ga3456f90a2ea094d16f05a358645a6eb8) (const struct [in6\_addr](structin6__addr.md) \*addr1, const struct [in6\_addr](structin6__addr.md) \*addr2) |
|  | Compare two IPv6 addresses. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_addr\_cmp\_raw](#gafbe40461a645cf11fc8b3a07e1d9156e) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2) |
|  | Compare two raw IPv6 address buffers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_ll\_addr](#gacac4279ee8896ddf2a76c612b36edf38) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the given IPv6 address is a link local address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_sl\_addr](#ga675d016e405e02882fda701aa8617ab7) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the given IPv6 address is a site local address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_ula\_addr](#gae10578b8801d213482de7d7d7e7ba230) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the given IPv6 address is a unique local address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_global\_addr](#gab2d854e2b24f866839e547c1092ccff6) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the given IPv6 address is a global address. |
| const struct [in6\_addr](structin6__addr.md) \* | [net\_ipv6\_unspecified\_address](#gab0211c91e113cf01a8a16b1a106e7290) (void) |
|  | Return pointer to any (all bits zeros) IPv6 address. |
| const struct [in\_addr](structin__addr.md) \* | [net\_ipv4\_unspecified\_address](#gaceb9afdd7f2f78d96e6debd72f63ebf0) (void) |
|  | Return pointer to any (all bits zeros) IPv4 address. |
| const struct [in\_addr](structin__addr.md) \* | [net\_ipv4\_broadcast\_address](#ga4df601fd1c89f1908df52b2673f9b113) (void) |
|  | Return pointer to broadcast (all bits ones) IPv4 address. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_addr\_mask\_cmp](#ga558b31e556a1a4b8d1e68a78f3f755ea) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_addr\_mask\_cmp](#ga715455ec5e8041c5d7075fa6913674cd) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the given address belongs to same subnet that has been configured for the interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_is\_addr\_bcast](#ga8f93179138c1942bc1a099102a4314cf) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_addr\_bcast](#gac545e2252f221c73c80cea746dffa083) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the given IPv4 address is a broadcast address. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv4\_addr\_lookup](#ga04a8f21d173d51bdcc092b92ed949e53) (const struct [in\_addr](structin__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_my\_addr](#ga3db2a1fca0b525a7202277700b987eb9) (const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the IPv4 address is assigned to any network interface in the system. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_unspecified](#gafe2c8dc0bdb677ba9bc872d051aab2a0) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is unspecified (all bits zero). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_solicited\_node](#ga5a334819f4e4bf87aea5caa7ef28c68a) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is solicited node multicast address FF02:0:0:0:0:1:FFXX:XXXX defined in RFC 3513. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_scope](#gadc75208131d5a4333f31291ac5f8ce94) (const struct [in6\_addr](structin6__addr.md) \*addr, int scope) |
|  | Check if the IPv6 address is a given scope multicast address (FFyx::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_same\_mcast\_scope](#ga3f80a84f330a31aaa875fdea64dc18ec) (const struct [in6\_addr](structin6__addr.md) \*addr\_1, const struct [in6\_addr](structin6__addr.md) \*addr\_2) |
|  | Check if the IPv6 addresses have the same multicast scope (FFyx::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_global](#ga55d67d4349dd354a7254a2f8e8320693) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a global multicast address (FFxE::/16). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_iface](#gae27ca6956f943469cad0faa0ba738fc2) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a interface scope multicast address (FFx1::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_link](#ga6f83a3a8701ec378b47337acba59d5e4) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a link local scope multicast address (FFx2::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_mesh](#ga497a148717c1c1095abeb4482566dda0) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a mesh-local scope multicast address (FFx3::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_site](#ga6704146124a14be9cf2a636947c35a00) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a site scope multicast address (FFx5::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_org](#ga141ed5de3043dd7d6b45098aea38a4b1) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is an organization scope multicast address (FFx8::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_group](#ga611a4adb332715d983375899dcf101d0) (const struct [in6\_addr](structin6__addr.md) \*addr, const struct [in6\_addr](structin6__addr.md) \*group) |
|  | Check if the IPv6 address belongs to certain multicast group. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](#gacf00ae106727f97e2fd35be68418354d) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address belongs to the all nodes multicast group. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes](#ga35bdad7c958f1ea656680000ee3f6bfd) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a interface scope all nodes multicast address (FF01::1). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes](#gaba3e1259f452381ef3e109bb2eb34c09) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a link local scope all nodes multicast address (FF02::1). |
| static void | [net\_ipv6\_addr\_create\_solicited\_node](#ga6091a7406c136fcf480517cb969c9d90) (const struct [in6\_addr](structin6__addr.md) \*src, struct [in6\_addr](structin6__addr.md) \*dst) |
|  | Create solicited node IPv6 multicast address FF02:0:0:0:0:1:FFXX:XXXX defined in RFC 3513. |
| static void | [net\_ipv6\_addr\_create](#ga0a78f83dcb4e341d86d9352506196696) (struct [in6\_addr](structin6__addr.md) \*addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr0, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr1, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr2, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr3, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr4, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr5, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr6, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr7) |
|  | Construct an IPv6 address from eight 16-bit words. |
| static void | [net\_ipv6\_addr\_create\_ll\_allnodes\_mcast](#ga58cbba1c522815b1ce201b0377ffe0b2) (struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Create link local allnodes multicast IPv6 address. |
| static void | [net\_ipv6\_addr\_create\_ll\_allrouters\_mcast](#ga30821f0a2c08b4b01b71d362e3a25de1) (struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Create link local allrouters multicast IPv6 address. |
| static void | [net\_ipv6\_addr\_create\_v4\_mapped](#ga8c6162c6212051037a33477aab9fc55f) (const struct [in\_addr](structin__addr.md) \*addr4, struct [in6\_addr](structin6__addr.md) \*addr6) |
|  | Create IPv4 mapped IPv6 address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_addr\_is\_v4\_mapped](#ga53c24abd635fb2bcb137584dbc8a9026) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Is the IPv6 address an IPv4 mapped one. |
| static void | [net\_ipv6\_addr\_create\_iid](#ga6d41f1de27e2e8fbb8f12925eba852b4) (struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr) |
|  | Create IPv6 address interface identifier. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_addr\_based\_on\_ll](#gaf4b0c30b926748625bd3c4c81d06ffc5) (const struct [in6\_addr](structin6__addr.md) \*addr, const struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr) |
|  | Check if given address is based on link layer address. |
| static struct [sockaddr\_in6](structsockaddr__in6.md) \* | [net\_sin6](#gad97b2c3da722409eada099f9b7e13f03) (const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Get [sockaddr\_in6](structsockaddr__in6.md "Socket address struct for IPv6.") from sockaddr. |
| static struct [sockaddr\_in](structsockaddr__in.md) \* | [net\_sin](#gacccfbac6a03480840fa219e9a1924dc6) (const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Get [sockaddr\_in](structsockaddr__in.md "Socket address struct for IPv4.") from sockaddr. |
| static struct [sockaddr\_in6\_ptr](structsockaddr__in6__ptr.md) \* | [net\_sin6\_ptr](#gae86d2cd402142190e1ea1c120a57939f) (const struct sockaddr\_ptr \*addr) |
|  | Get [sockaddr\_in6\_ptr](structsockaddr__in6__ptr.md) from sockaddr\_ptr. |
| static struct [sockaddr\_in\_ptr](structsockaddr__in__ptr.md) \* | [net\_sin\_ptr](#ga4b948e84590081a8aed2a63496e57ae2) (const struct sockaddr\_ptr \*addr) |
|  | Get [sockaddr\_in\_ptr](structsockaddr__in__ptr.md) from sockaddr\_ptr. |
| static struct [sockaddr\_ll\_ptr](structsockaddr__ll__ptr.md) \* | [net\_sll\_ptr](#gad5cf206e18769a15f9fc917e416db6ee) (const struct sockaddr\_ptr \*addr) |
|  | Get [sockaddr\_ll\_ptr](structsockaddr__ll__ptr.md) from sockaddr\_ptr. |
| static struct [sockaddr\_can\_ptr](structsockaddr__can__ptr.md) \* | [net\_can\_ptr](#gac2fb590a35961c04807dd985f462c5fb) (const struct sockaddr\_ptr \*addr) |
|  | Get [sockaddr\_can\_ptr](structsockaddr__can__ptr.md) from sockaddr\_ptr. |
| int | [net\_addr\_pton](#ga264b3c0a13493eac291ddc85d0b4d43d) ([sa\_family\_t](#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst) |
|  | Convert a string to IP address. |
| char \* | [net\_addr\_ntop](#ga326b6cd455f8b6193f490fa2877c5222) ([sa\_family\_t](#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src, char \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Convert IP address to string form. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipaddr\_parse](#ga9918e156f0039cf45d487a112e0a2ada) (const char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) str\_len, struct [sockaddr](structsockaddr.md) \*addr) |
|  | Parse a string that contains either IPv4 or IPv6 address and optional port, and store the information in user supplied sockaddr struct. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [net\_tcp\_seq\_cmp](#ga1695009388402938dcc2e49b526ebd1f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq2) |
|  | Compare TCP sequence numbers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_tcp\_seq\_greater](#gaa77b299f53e5535ac4c4bea1b6531a34) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq2) |
|  | Check that one TCP sequence number is greater. |
| int | [net\_bytes\_from\_str](#ga8b794f251cf8412c769ab415902a9f32) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, int buf\_len, const char \*src) |
|  | Convert a string of hex values to array of bytes. |
| int | [net\_tx\_priority2tc](#gae74c9ba7ff4addbce7f931bd6fa91fa0) (enum [net\_priority](#gae87ef466e77ded673ed7e593d3eddffd) prio) |
|  | Convert Tx network packet priority to traffic class so we can place the packet into correct Tx queue. |
| int | [net\_rx\_priority2tc](#ga7b3c41ae9b3962090d72c130a9fa61b1) (enum [net\_priority](#gae87ef466e77ded673ed7e593d3eddffd) prio) |
|  | Convert Rx network packet priority to traffic class so we can place the packet into correct Rx queue. |
| static enum [net\_priority](#gae87ef466e77ded673ed7e593d3eddffd) | [net\_vlan2priority](#ga14bc7018e3dd7c3e320b44a077343ce4) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority) |
|  | Convert network packet VLAN priority to network packet priority so we can place the packet into correct queue. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_priority2vlan](#ga8be77d043d4d1d29e0879b3b22274629) (enum [net\_priority](#gae87ef466e77ded673ed7e593d3eddffd) priority) |
|  | Convert network packet priority to network packet VLAN priority. |
| const char \* | [net\_family2str](#gaba4c72e3aa2ceb4ac67d25112fb36523) ([sa\_family\_t](#ga2d9e094abb99ebd0874373edf1c45eda) family) |
|  | Return network address family value as a string. |

## Detailed Description

IPv4/IPv6 primitives and helpers.

## Macro Definition Documentation

## [◆ ](#ga546620c7e758f003b24b7fdae4f97bd4)AF\_CAN

| #define AF\_CAN   [PF\_CAN](#gaeac0c3db7a1e021f17987bcc76893849) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Controller Area Network.

## [◆ ](#ga9930604d0e32588eae76f43ca38e7826)AF\_INET

| #define AF\_INET   [PF\_INET](#ga3f5da0b5be27fe31ec7cc11bfa8d1a25) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

IP protocol family version 4.

## [◆ ](#gaa03706b2738b9a58d4985dfbe99e1bac)AF\_INET6

| #define AF\_INET6   [PF\_INET6](#ga323f2649198fc7e64b19881869265618) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

IP protocol family version 6.

## [◆ ](#gae24f1f9ea44fcce3affcb2137f593dc1)AF\_LOCAL

| #define AF\_LOCAL   [PF\_LOCAL](#ga521c315ca2a2a4e6345878e84af4085e) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Inter-process communication.

## [◆ ](#ga41d0cbb55cd9550a7f732b1520119c15)AF\_NET\_MGMT

| #define AF\_NET\_MGMT   [PF\_NET\_MGMT](#ga288b09307bcc46aef2acf2af5e3e1006) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Network management info.

## [◆ ](#gaa89aa4cd481fe17260c3f5d493cc23f5)AF\_PACKET

| #define AF\_PACKET   [PF\_PACKET](#ga8e297adb5fe2e28b0d9d921a5d56a8e9) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Packet family.

## [◆ ](#ga0fd8739854bc8b48d65f0b669fed3ffe)AF\_UNIX

| #define AF\_UNIX   [PF\_UNIX](#ga0407288f5fb975a03b21d5287c282b2e) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Inter-process communication.

## [◆ ](#gae77ae24b14b7b7f294f3e04121173f12)AF\_UNSPEC

| #define AF\_UNSPEC   [PF\_UNSPEC](#ga51dba11ffc8e3b1bf695e721b3144094) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Unspecified address family.

## [◆ ](#gab67ab3f70af998e71325fb26ea0f6a83)ALIGN\_D

| #define ALIGN\_D | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(x, \_\_alignof\_\_(z\_max\_align\_t))

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:288

## [◆ ](#ga051015580ee95f46da1d68f6be2b333d)ALIGN\_H

| #define ALIGN\_H | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(x, \_\_alignof\_\_(struct [cmsghdr](structcmsghdr.md)))

[cmsghdr](structcmsghdr.md)

**Definition** net\_ip.h:248

## [◆ ](#ga5ab6d56e410ac0904107e84aeb1484cc)CMSG\_DATA

| #define CMSG\_DATA | ( |  | *cmsg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(cmsg) + [ALIGN\_D](#gab67ab3f70af998e71325fb26ea0f6a83)(sizeof(struct [cmsghdr](structcmsghdr.md))))

[ALIGN\_D](#gab67ab3f70af998e71325fb26ea0f6a83)

#define ALIGN\_D(x)

**Definition** net\_ip.h:263

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

## [◆ ](#ga39567a31d167fc53336d2ab4a2cd78a4)CMSG\_FIRSTHDR

| #define CMSG\_FIRSTHDR | ( |  | *[msghdr](structmsghdr.md)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

(([msghdr](structmsghdr.md))->msg\_controllen >= sizeof(struct [cmsghdr](structcmsghdr.md)) ? \

(struct [cmsghdr](structcmsghdr.md) \*)(([msghdr](structmsghdr.md))->msg\_control) : NULL)

[msghdr](structmsghdr.md)

**Definition** net\_ip.h:238

## [◆ ](#gadb36e4ff4fa9a0c6730321c4bfcf64bc)CMSG\_LEN

| #define CMSG\_LEN | ( |  | *length* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

([ALIGN\_D](#gab67ab3f70af998e71325fb26ea0f6a83)(sizeof(struct [cmsghdr](structcmsghdr.md))) + length)

## [◆ ](#ga77c17efca635d597cb6e98b28172bdc0)CMSG\_NXTHDR

| #define CMSG\_NXTHDR | ( |  | *[msghdr](structmsghdr.md)*, |
| --- | --- | --- | --- |
|  |  |  | *cmsg* ) |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

(((cmsg) == NULL) ? [CMSG\_FIRSTHDR](#ga39567a31d167fc53336d2ab4a2cd78a4)([msghdr](structmsghdr.md)) : \

((([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(cmsg) + [ALIGN\_H](#ga051015580ee95f46da1d68f6be2b333d)((cmsg)->cmsg\_len) + \

[ALIGN\_D](#gab67ab3f70af998e71325fb26ea0f6a83)([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [cmsghdr](structcmsghdr.md))) > \

([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(([msghdr](structmsghdr.md))->msg\_control) + ([msghdr](structmsghdr.md))->msg\_controllen) ? \

NULL : \

(struct [cmsghdr](structcmsghdr.md) \*)(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(cmsg) + \

[ALIGN\_H](#ga051015580ee95f46da1d68f6be2b333d)((cmsg)->cmsg\_len))))

[ALIGN\_H](#ga051015580ee95f46da1d68f6be2b333d)

#define ALIGN\_H(x)

**Definition** net\_ip.h:260

[CMSG\_FIRSTHDR](#ga39567a31d167fc53336d2ab4a2cd78a4)

#define CMSG\_FIRSTHDR(msghdr)

**Definition** net\_ip.h:267

[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)

sizeof(size\_t))

## [◆ ](#ga8db11d639dd07c723256f3bb5bc89044)CMSG\_SPACE

| #define CMSG\_SPACE | ( |  | *length* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

([ALIGN\_D](#gab67ab3f70af998e71325fb26ea0f6a83)(sizeof(struct [cmsghdr](structcmsghdr.md))) + [ALIGN\_H](#ga051015580ee95f46da1d68f6be2b333d)(length))

## [◆ ](#gae4027a6ad07f13aa12eab285a1b46019)htonl

| #define htonl | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

[sys\_cpu\_to\_be32](sys_2byteorder_8h.md#a508d3b125adf1d30e8411381827c4f05)(x)

[sys\_cpu\_to\_be32](sys_2byteorder_8h.md#a508d3b125adf1d30e8411381827c4f05)

#define sys\_cpu\_to\_be32(val)

Convert 32-bit integer from host endianness to big-endian.

**Definition** byteorder.h:271

Convert 32-bit value from host to network byte order.

Parameters
:   | x | The host byte order value to convert. |
    | --- | --- |

Returns
:   Network byte order value.

## [◆ ](#ga9f4bf0773c45ad9a9753a1b784a13fbb)htonll

| #define htonll | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

[sys\_cpu\_to\_be64](sys_2byteorder_8h.md#a6ac423744c21c1e40aabd7ecb9b9e8d5)(x)

[sys\_cpu\_to\_be64](sys_2byteorder_8h.md#a6ac423744c21c1e40aabd7ecb9b9e8d5)

#define sys\_cpu\_to\_be64(val)

**Definition** byteorder.h:275

Convert 64-bit value from host to network byte order.

Parameters
:   | x | The host byte order value to convert. |
    | --- | --- |

Returns
:   Network byte order value.

## [◆ ](#ga51799f5ebb4c7228ef7e95c247030f42)htons

| #define htons | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

[sys\_cpu\_to\_be16](sys_2byteorder_8h.md#a9e2c7b19bbba5343ee8c5f9740484a56)(x)

[sys\_cpu\_to\_be16](sys_2byteorder_8h.md#a9e2c7b19bbba5343ee8c5f9740484a56)

#define sys\_cpu\_to\_be16(val)

Convert 16-bit integer from host endianness to big-endian.

**Definition** byteorder.h:267

Convert 16-bit value from host to network byte order.

Parameters
:   | x | The host byte order value to convert. |
    | --- | --- |

Returns
:   Network byte order value.

## [◆ ](#gaf776b22a727aae7c9f4d869d50df47e8)INET6\_ADDRSTRLEN

| #define INET6\_ADDRSTRLEN   46 |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Max length of the IPv6 address as a string.

Takes into account possible mapped IPv4 addresses.

## [◆ ](#ga93b37007689284fd9c4bde1a8f4b9199)INET\_ADDRSTRLEN

| #define INET\_ADDRSTRLEN   16 |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Max length of the IPv4 address as a string.

Defined by POSIX.

## [◆ ](#ga75ffcc08e621c2d47d1ae043fce2acad)net\_ipaddr\_copy

| #define net\_ipaddr\_copy | ( |  | *dest*, |
| --- | --- | --- | --- |
|  |  |  | *src* ) |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

UNALIGNED\_PUT(UNALIGNED\_GET(src), dest)

Copy an IPv4 or IPv6 address.

Parameters
:   | dest | Destination IP address. |
    | --- | --- |
    | src | Source IP address. |

Returns
:   Destination address.

## [◆ ](#ga10a82ea9ba9ca19f3b773bdd53c978e0)NET\_IPV4\_ADDR\_SIZE

| #define NET\_IPV4\_ADDR\_SIZE   4 |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

## [◆ ](#ga1eefdabf590090be9f98bdf4a2f43bb4)NET\_IPV6\_ADDR\_SIZE

| #define NET\_IPV6\_ADDR\_SIZE   16 |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

## [◆ ](#ga5b32bdfc249437709bb25bd95ec7d6d7)NET\_MAX\_PRIORITIES

| #define NET\_MAX\_PRIORITIES   8 /\* How many priority values there are \*/ |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

## [◆ ](#gac317b3e903719ba02894f1710f7f2439)ntohl

| #define ntohl | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

[sys\_be32\_to\_cpu](sys_2byteorder_8h.md#aee4cefae7f089197e77c487faafda269)(x)

[sys\_be32\_to\_cpu](sys_2byteorder_8h.md#aee4cefae7f089197e77c487faafda269)

#define sys\_be32\_to\_cpu(val)

Convert 32-bit integer from big-endian to host endianness.

**Definition** byteorder.h:270

Convert 32-bit value from network to host byte order.

Parameters
:   | x | The network byte order value to convert. |
    | --- | --- |

Returns
:   Host byte order value.

## [◆ ](#ga3cfcf123d4ead264289232f91f2c9ca5)ntohll

| #define ntohll | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

[sys\_be64\_to\_cpu](sys_2byteorder_8h.md#abb4d263f2b9b1cbf1c8fbaec714fc411)(x)

[sys\_be64\_to\_cpu](sys_2byteorder_8h.md#abb4d263f2b9b1cbf1c8fbaec714fc411)

#define sys\_be64\_to\_cpu(val)

**Definition** byteorder.h:274

Convert 64-bit value from network to host byte order.

Parameters
:   | x | The network byte order value to convert. |
    | --- | --- |

Returns
:   Host byte order value.

## [◆ ](#gada37feda716b4ba89cf9dba34288141d)ntohs

| #define ntohs | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

**Value:**

[sys\_be16\_to\_cpu](sys_2byteorder_8h.md#a840037a5fd3d36817dc92a44469df704)(x)

[sys\_be16\_to\_cpu](sys_2byteorder_8h.md#a840037a5fd3d36817dc92a44469df704)

#define sys\_be16\_to\_cpu(val)

Convert 16-bit integer from big-endian to host endianness.

**Definition** byteorder.h:266

Convert 16-bit value from network to host byte order.

Parameters
:   | x | The network byte order value to convert. |
    | --- | --- |

Returns
:   Host byte order value.

## [◆ ](#gaeac0c3db7a1e021f17987bcc76893849)PF\_CAN

| #define PF\_CAN   4 |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Controller Area Network.

## [◆ ](#ga3f5da0b5be27fe31ec7cc11bfa8d1a25)PF\_INET

| #define PF\_INET   1 |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

IP protocol family version 4.

## [◆ ](#ga323f2649198fc7e64b19881869265618)PF\_INET6

| #define PF\_INET6   2 |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

IP protocol family version 6.

## [◆ ](#ga521c315ca2a2a4e6345878e84af4085e)PF\_LOCAL

| #define PF\_LOCAL   6 |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Inter-process communication.

## [◆ ](#ga288b09307bcc46aef2acf2af5e3e1006)PF\_NET\_MGMT

| #define PF\_NET\_MGMT   5 |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Network management info.

## [◆ ](#ga8e297adb5fe2e28b0d9d921a5d56a8e9)PF\_PACKET

| #define PF\_PACKET   3 |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Packet family.

## [◆ ](#ga0407288f5fb975a03b21d5287c282b2e)PF\_UNIX

| #define PF\_UNIX   [PF\_LOCAL](#ga521c315ca2a2a4e6345878e84af4085e) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Inter-process communication.

## [◆ ](#ga51dba11ffc8e3b1bf695e721b3144094)PF\_UNSPEC

| #define PF\_UNSPEC   0 |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Unspecified protocol family.

## Typedef Documentation

## [◆ ](#ga2d9e094abb99ebd0874373edf1c45eda)sa\_family\_t

| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short int [sa\_family\_t](#ga2d9e094abb99ebd0874373edf1c45eda) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Socket address family type.

## [◆ ](#gacf0ed818b0a3c85ff6a9206679d6d91a)socklen\_t

| typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) [socklen\_t](#gacf0ed818b0a3c85ff6a9206679d6d91a) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Length of a socket address.

## Enumeration Type Documentation

## [◆ ](#ga32e58fc83532ef57eeb6ff952f17288d)net\_addr\_state

| enum [net\_addr\_state](#ga32e58fc83532ef57eeb6ff952f17288d) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

What is the current state of the network address.

| Enumerator | |
| --- | --- |
| NET\_ADDR\_ANY\_STATE | Default (invalid) address type. |
| NET\_ADDR\_TENTATIVE | Tentative address. |
| NET\_ADDR\_PREFERRED | Preferred address. |
| NET\_ADDR\_DEPRECATED | Deprecated address. |

## [◆ ](#gafecee2d4a331dc85ad962b81a6303e41)net\_addr\_type

| enum [net\_addr\_type](#gafecee2d4a331dc85ad962b81a6303e41) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

How the network address is assigned to network interface.

| Enumerator | |
| --- | --- |
| NET\_ADDR\_ANY | Default value.  This is not a valid value. |
| NET\_ADDR\_AUTOCONF | Auto configured address. |
| NET\_ADDR\_DHCP | Address is from DHCP. |
| NET\_ADDR\_MANUAL | Manually set address. |
| NET\_ADDR\_OVERRIDABLE | Manually set address which is overridable by DHCP. |

## [◆ ](#ga7a207761e4879c140f48f93978cb2f0b)net\_ip\_mtu

| enum [net\_ip\_mtu](#ga7a207761e4879c140f48f93978cb2f0b) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

| Enumerator | |
| --- | --- |
| NET\_IPV6\_MTU | IPv6 MTU length.  We must be able to receive this size IPv6 packet without fragmentation. |
| NET\_IPV4\_MTU | IPv4 MTU length.  We must be able to receive this size IPv4 packet without fragmentation. |

## [◆ ](#gaf06819bf427cc58be1229b27b373ca31)net\_ip\_protocol

| enum [net\_ip\_protocol](#gaf06819bf427cc58be1229b27b373ca31) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Protocol numbers from IANA/BSD.

| Enumerator | |
| --- | --- |
| IPPROTO\_IP | IP protocol (pseudo-val for [setsockopt()](group__bsd__sockets.md#ga9e476c4da1bb69b721e4aaa384114328 "POSIX wrapper for zsock_setsockopt."). |
| IPPROTO\_ICMP | ICMP protocol. |
| IPPROTO\_IGMP | IGMP protocol. |
| IPPROTO\_IPIP | IPIP tunnels. |
| IPPROTO\_TCP | TCP protocol. |
| IPPROTO\_UDP | UDP protocol. |
| IPPROTO\_IPV6 | IPv6 protocol. |
| IPPROTO\_ICMPV6 | ICMPv6 protocol. |
| IPPROTO\_RAW | RAW IP packets. |

## [◆ ](#ga721da18d2a3cfd9b3a56e9efc9f6e58b)net\_ip\_protocol\_secure

| enum [net\_ip\_protocol\_secure](#ga721da18d2a3cfd9b3a56e9efc9f6e58b) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Protocol numbers for TLS protocols.

| Enumerator | |
| --- | --- |
| IPPROTO\_TLS\_1\_0 | TLS 1.0 protocol. |
| IPPROTO\_TLS\_1\_1 | TLS 1.1 protocol. |
| IPPROTO\_TLS\_1\_2 | TLS 1.2 protocol. |
| IPPROTO\_DTLS\_1\_0 | DTLS 1.0 protocol. |
| IPPROTO\_DTLS\_1\_2 | DTLS 1.2 protocol. |

## [◆ ](#gae87ef466e77ded673ed7e593d3eddffd)net\_priority

| enum [net\_priority](#gae87ef466e77ded673ed7e593d3eddffd) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Network packet priority settings described in IEEE 802.1Q Annex I.1.

| Enumerator | |
| --- | --- |
| NET\_PRIORITY\_BK | Background (lowest). |
| NET\_PRIORITY\_BE | Best effort (default). |
| NET\_PRIORITY\_EE | Excellent effort. |
| NET\_PRIORITY\_CA | Critical applications. |
| NET\_PRIORITY\_VI | Video, < 100 ms latency and jitter. |
| NET\_PRIORITY\_VO | Voice, < 10 ms latency and jitter. |
| NET\_PRIORITY\_IC | Internetwork control. |
| NET\_PRIORITY\_NC | Network control (highest). |

## [◆ ](#gaaab4268707dbe08348b98fb028e7aa5c)net\_sock\_type

| enum [net\_sock\_type](#gaaab4268707dbe08348b98fb028e7aa5c) |
| --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Socket type.

| Enumerator | |
| --- | --- |
| SOCK\_STREAM | Stream socket type. |
| SOCK\_DGRAM | Datagram socket type. |
| SOCK\_RAW | RAW socket type. |

## Function Documentation

## [◆ ](#ga326b6cd455f8b6193f490fa2877c5222)net\_addr\_ntop()

| char \* net\_addr\_ntop | ( | [sa\_family\_t](#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, |
| --- | --- | --- | --- |
|  |  | const void \* | *src*, |
|  |  | char \* | *dst*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[net_ip.h](net__ip_8h.md)>`

Convert IP address to string form.

Parameters
:   | family | IP address family (AF\_INET or AF\_INET6) |
    | --- | --- |
    | src | Pointer to struct [in\_addr](structin__addr.md "IPv4 address struct.") if family is AF\_INET or pointer to struct [in6\_addr](structin6__addr.md "IPv6 address struct.") if family is AF\_INET6 |
    | dst | Buffer for IP address as a null terminated string |
    | size | Number of bytes available in the buffer |

Returns
:   dst pointer if ok, NULL if error

## [◆ ](#ga264b3c0a13493eac291ddc85d0b4d43d)net\_addr\_pton()

| int net\_addr\_pton | ( | [sa\_family\_t](#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, |
| --- | --- | --- | --- |
|  |  | const char \* | *src*, |
|  |  | void \* | *dst* ) |

`#include <[net_ip.h](net__ip_8h.md)>`

Convert a string to IP address.

Parameters
:   | family | IP address family (AF\_INET or AF\_INET6) |
    | --- | --- |
    | src | IP address in a null terminated string |
    | dst | Pointer to struct [in\_addr](structin__addr.md "IPv4 address struct.") if family is AF\_INET or pointer to struct [in6\_addr](structin6__addr.md "IPv6 address struct.") if family is AF\_INET6 |

Note
:   This function doesn't do precise error checking, do not use for untrusted strings.

Returns
:   0 if ok, < 0 if error

## [◆ ](#ga8b794f251cf8412c769ab415902a9f32)net\_bytes\_from\_str()

| int net\_bytes\_from\_str | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | int | *buf\_len*, |
|  |  | const char \* | *src* ) |

`#include <[net_ip.h](net__ip_8h.md)>`

Convert a string of hex values to array of bytes.

The syntax of the string is "ab:02:98:fa:42:01"

Parameters
:   | buf | Pointer to memory where the bytes are written. |
    | --- | --- |
    | buf\_len | Length of the memory area. |
    | src | String of bytes. |

Returns
:   0 if ok, <0 if error

## [◆ ](#gac2fb590a35961c04807dd985f462c5fb)net\_can\_ptr()

| | struct [sockaddr\_can\_ptr](structsockaddr__can__ptr.md) \* net\_can\_ptr | ( | const struct sockaddr\_ptr \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Get [sockaddr\_can\_ptr](structsockaddr__can__ptr.md) from sockaddr\_ptr.

This is a helper so that the code needing this functionality can be made shorter.

Parameters
:   | addr | Socket address |
    | --- | --- |

Returns
:   Pointer to CAN socket address

## [◆ ](#gaba4c72e3aa2ceb4ac67d25112fb36523)net\_family2str()

| const char \* net\_family2str | ( | [sa\_family\_t](#ga2d9e094abb99ebd0874373edf1c45eda) | *family* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Return network address family value as a string.

This is only usable for debugging.

Parameters
:   | family | Network address family code |
    | --- | --- |

Returns
:   Network address family as a string, or NULL if family is unknown.

## [◆ ](#ga04a8f21d173d51bdcc092b92ed949e53)net\_if\_ipv4\_addr\_lookup()

| | struct [net\_if\_addr](structnet__if__addr.md) \* net\_if\_ipv4\_addr\_lookup | ( | const struct [in\_addr](structin__addr.md) \* | *addr*, | | --- | --- | --- | --- | |  |  | struct [net\_if](structnet__if.md) \*\* | *iface* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

## [◆ ](#ga558b31e556a1a4b8d1e68a78f3f755ea)net\_if\_ipv4\_addr\_mask\_cmp()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_addr\_mask\_cmp | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | const struct [in\_addr](structin__addr.md) \* | *addr* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

## [◆ ](#ga8f93179138c1942bc1a099102a4314cf)net\_if\_ipv4\_is\_addr\_bcast()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_is\_addr\_bcast | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | const struct [in\_addr](structin__addr.md) \* | *addr* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

## [◆ ](#ga13b5a26fc672d15697f99e85543184bb)net\_if\_ipv6\_addr\_lookup()

| | struct [net\_if\_addr](structnet__if__addr.md) \* net\_if\_ipv6\_addr\_lookup | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr*, | | --- | --- | --- | --- | |  |  | struct [net\_if](structnet__if.md) \*\* | *iface* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

## [◆ ](#gadb4031153c4fef86110879befa6b9975)net\_if\_ipv6\_maddr\_lookup()

| | struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* net\_if\_ipv6\_maddr\_lookup | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr*, | | --- | --- | --- | --- | |  |  | struct [net\_if](structnet__if.md) \*\* | *iface* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

## [◆ ](#ga9918e156f0039cf45d487a112e0a2ada)net\_ipaddr\_parse()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipaddr\_parse | ( | const char \* | *str*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *str\_len*, |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr* ) |

`#include <[net_ip.h](net__ip_8h.md)>`

Parse a string that contains either IPv4 or IPv6 address and optional port, and store the information in user supplied sockaddr struct.

Syntax of the IP address string: 192.0.2.1:80 192.0.2.42

[2001:db8::2] 2001:db::42 Note that the str\_len parameter is used to restrict the amount of characters that are checked. If the string does not contain port number, then the port number in sockaddr is not modified.

Parameters
:   | str | String that contains the IP address. |
    | --- | --- |
    | str\_len | Length of the string to be parsed. |
    | addr | Pointer to user supplied struct sockaddr. |

Returns
:   True if parsing could be done, false otherwise.

## [◆ ](#ga0bdcc8dad8eb42c02426e55378ececf8)net\_ipv4\_addr\_cmp()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv4\_addr\_cmp | ( | const struct [in\_addr](structin__addr.md) \* | *addr1*, | | --- | --- | --- | --- | |  |  | const struct [in\_addr](structin__addr.md) \* | *addr2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Compare two IPv4 addresses.

Parameters
:   | addr1 | Pointer to IPv4 address. |
    | --- | --- |
    | addr2 | Pointer to IPv4 address. |

Returns
:   True if the addresses are the same, false otherwise.

## [◆ ](#ga32ffb42c62169ac9b34a0faa7c7ffd12)net\_ipv4\_addr\_cmp\_raw()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv4\_addr\_cmp\_raw | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *addr1*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *addr2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Compare two raw IPv4 address buffers.

Parameters
:   | addr1 | Pointer to IPv4 address buffer. |
    | --- | --- |
    | addr2 | Pointer to IPv4 address buffer. |

Returns
:   True if the addresses are the same, false otherwise.

## [◆ ](#gaf731738fb1761208739976d767736f87)net\_ipv4\_addr\_copy\_raw()

| | void net\_ipv4\_addr\_copy\_raw | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *dest*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Copy an IPv4 address raw buffer.

Parameters
:   | dest | Destination IP address. |
    | --- | --- |
    | src | Source IP address. |

## [◆ ](#ga715455ec5e8041c5d7075fa6913674cd)net\_ipv4\_addr\_mask\_cmp()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv4\_addr\_mask\_cmp | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | const struct [in\_addr](structin__addr.md) \* | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the given address belongs to same subnet that has been configured for the interface.

Parameters
:   | iface | A valid pointer on an interface |
    | --- | --- |
    | addr | IPv4 address |

Returns
:   True if address is in same subnet, false otherwise.

## [◆ ](#ga4df601fd1c89f1908df52b2673f9b113)net\_ipv4\_broadcast\_address()

| const struct [in\_addr](structin__addr.md) \* net\_ipv4\_broadcast\_address | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Return pointer to broadcast (all bits ones) IPv4 address.

Returns
:   Broadcast IPv4 address.

## [◆ ](#gac545e2252f221c73c80cea746dffa083)net\_ipv4\_is\_addr\_bcast()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv4\_is\_addr\_bcast | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | const struct [in\_addr](structin__addr.md) \* | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the given IPv4 address is a broadcast address.

Parameters
:   | iface | Interface to use. Must be a valid pointer to an interface. |
    | --- | --- |
    | addr | IPv4 address |

Returns
:   True if address is a broadcast address, false otherwise.

## [◆ ](#ga879e4aed725d7ea3fe609fa989f14735)net\_ipv4\_is\_addr\_loopback()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv4\_is\_addr\_loopback | ( | struct [in\_addr](structin__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv4 address is a loopback address (127.0.0.0/8).

Parameters
:   | addr | IPv4 address |
    | --- | --- |

Returns
:   True if address is a loopback address, False otherwise.

## [◆ ](#gae8c3302cf9ca457de32eabcf65975b70)net\_ipv4\_is\_addr\_mcast()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv4\_is\_addr\_mcast | ( | const struct [in\_addr](structin__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv4 address is a multicast address.

Parameters
:   | addr | IPv4 address |
    | --- | --- |

Returns
:   True if address is multicast address, False otherwise.

## [◆ ](#gadc623ecacf024733ab6d477d87cc4b9d)net\_ipv4\_is\_addr\_unspecified()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv4\_is\_addr\_unspecified | ( | const struct [in\_addr](structin__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv4 address is unspecified (all bits zero).

Parameters
:   | addr | IPv4 address. |
    | --- | --- |

Returns
:   True if the address is unspecified, false otherwise.

## [◆ ](#gac000a319de7a6f95d4a63719bca3b865)net\_ipv4\_is\_ll\_addr()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv4\_is\_ll\_addr | ( | const struct [in\_addr](structin__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the given IPv4 address is a link local address.

Parameters
:   | addr | A valid pointer on an IPv4 address |
    | --- | --- |

Returns
:   True if it is, false otherwise.

## [◆ ](#ga3db2a1fca0b525a7202277700b987eb9)net\_ipv4\_is\_my\_addr()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv4\_is\_my\_addr | ( | const struct [in\_addr](structin__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv4 address is assigned to any network interface in the system.

Parameters
:   | addr | A valid pointer on an IPv4 address |
    | --- | --- |

Returns
:   True if IPv4 address is found in one of the network interfaces, False otherwise.

## [◆ ](#gaceb9afdd7f2f78d96e6debd72f63ebf0)net\_ipv4\_unspecified\_address()

| const struct [in\_addr](structin__addr.md) \* net\_ipv4\_unspecified\_address | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Return pointer to any (all bits zeros) IPv4 address.

Returns
:   Any IPv4 address.

## [◆ ](#gaf4b0c30b926748625bd3c4c81d06ffc5)net\_ipv6\_addr\_based\_on\_ll()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_addr\_based\_on\_ll | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr*, | | --- | --- | --- | --- | |  |  | const struct [net\_linkaddr](structnet__linkaddr.md) \* | *lladdr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if given address is based on link layer address.

Returns
:   True if it is, False otherwise

## [◆ ](#ga3456f90a2ea094d16f05a358645a6eb8)net\_ipv6\_addr\_cmp()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_addr\_cmp | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr1*, | | --- | --- | --- | --- | |  |  | const struct [in6\_addr](structin6__addr.md) \* | *addr2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Compare two IPv6 addresses.

Parameters
:   | addr1 | Pointer to IPv6 address. |
    | --- | --- |
    | addr2 | Pointer to IPv6 address. |

Returns
:   True if the addresses are the same, false otherwise.

## [◆ ](#gafbe40461a645cf11fc8b3a07e1d9156e)net\_ipv6\_addr\_cmp\_raw()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_addr\_cmp\_raw | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *addr1*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *addr2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Compare two raw IPv6 address buffers.

Parameters
:   | addr1 | Pointer to IPv6 address buffer. |
    | --- | --- |
    | addr2 | Pointer to IPv6 address buffer. |

Returns
:   True if the addresses are the same, false otherwise.

## [◆ ](#ga4925e6f3734b8fc1d9cb1ca1a510b5f1)net\_ipv6\_addr\_copy\_raw()

| | void net\_ipv6\_addr\_copy\_raw | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *dest*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Copy an IPv6 address raw buffer.

Parameters
:   | dest | Destination IP address. |
    | --- | --- |
    | src | Source IP address. |

## [◆ ](#ga0a78f83dcb4e341d86d9352506196696)net\_ipv6\_addr\_create()

| | void net\_ipv6\_addr\_create | ( | struct [in6\_addr](structin6__addr.md) \* | *addr*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr0*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr1*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr2*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr3*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr4*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr5*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr6*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr7* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Construct an IPv6 address from eight 16-bit words.

Parameters
:   | addr | IPv6 address |
    | --- | --- |
    | addr0 | 16-bit word which is part of the address |
    | addr1 | 16-bit word which is part of the address |
    | addr2 | 16-bit word which is part of the address |
    | addr3 | 16-bit word which is part of the address |
    | addr4 | 16-bit word which is part of the address |
    | addr5 | 16-bit word which is part of the address |
    | addr6 | 16-bit word which is part of the address |
    | addr7 | 16-bit word which is part of the address |

## [◆ ](#ga6d41f1de27e2e8fbb8f12925eba852b4)net\_ipv6\_addr\_create\_iid()

| | void net\_ipv6\_addr\_create\_iid | ( | struct [in6\_addr](structin6__addr.md) \* | *addr*, | | --- | --- | --- | --- | |  |  | struct [net\_linkaddr](structnet__linkaddr.md) \* | *lladdr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Create IPv6 address interface identifier.

Parameters
:   | addr | IPv6 address |
    | --- | --- |
    | lladdr | Link local address |

## [◆ ](#ga58cbba1c522815b1ce201b0377ffe0b2)net\_ipv6\_addr\_create\_ll\_allnodes\_mcast()

| | void net\_ipv6\_addr\_create\_ll\_allnodes\_mcast | ( | struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Create link local allnodes multicast IPv6 address.

Parameters
:   | addr | IPv6 address |
    | --- | --- |

## [◆ ](#ga30821f0a2c08b4b01b71d362e3a25de1)net\_ipv6\_addr\_create\_ll\_allrouters\_mcast()

| | void net\_ipv6\_addr\_create\_ll\_allrouters\_mcast | ( | struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Create link local allrouters multicast IPv6 address.

Parameters
:   | addr | IPv6 address |
    | --- | --- |

## [◆ ](#ga6091a7406c136fcf480517cb969c9d90)net\_ipv6\_addr\_create\_solicited\_node()

| | void net\_ipv6\_addr\_create\_solicited\_node | ( | const struct [in6\_addr](structin6__addr.md) \* | *src*, | | --- | --- | --- | --- | |  |  | struct [in6\_addr](structin6__addr.md) \* | *dst* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Create solicited node IPv6 multicast address FF02:0:0:0:0:1:FFXX:XXXX defined in RFC 3513.

Parameters
:   | src | IPv6 address. |
    | --- | --- |
    | dst | IPv6 address. |

## [◆ ](#ga8c6162c6212051037a33477aab9fc55f)net\_ipv6\_addr\_create\_v4\_mapped()

| | void net\_ipv6\_addr\_create\_v4\_mapped | ( | const struct [in\_addr](structin__addr.md) \* | *addr4*, | | --- | --- | --- | --- | |  |  | struct [in6\_addr](structin6__addr.md) \* | *addr6* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Create IPv4 mapped IPv6 address.

Parameters
:   | addr4 | IPv4 address |
    | --- | --- |
    | addr6 | IPv6 address to be created |

## [◆ ](#ga53c24abd635fb2bcb137584dbc8a9026)net\_ipv6\_addr\_is\_v4\_mapped()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_addr\_is\_v4\_mapped | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Is the IPv6 address an IPv4 mapped one.

The v4 mapped addresses look like ::ffff:a.b.c.d

Parameters
:   | addr | IPv6 address |
    | --- | --- |

Returns
:   True if IPv6 address is a IPv4 mapped address, False otherwise.

## [◆ ](#gaa662667005bdc00bf1eb5cf243aad874)net\_ipv6\_is\_addr\_loopback()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_loopback | ( | struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is a loopback address (::1).

Parameters
:   | addr | IPv6 address |
    | --- | --- |

Returns
:   True if address is a loopback address, False otherwise.

## [◆ ](#ga1a2fb0427eeab1a5dec6d69208ad7f02)net\_ipv6\_is\_addr\_mcast()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_mcast | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is a multicast address.

Parameters
:   | addr | IPv6 address |
    | --- | --- |

Returns
:   True if address is multicast address, False otherwise.

## [◆ ](#gacf00ae106727f97e2fd35be68418354d)net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address belongs to the all nodes multicast group.

Parameters
:   | addr | IPv6 address |
    | --- | --- |

Returns
:   True if the IPv6 multicast address belongs to the all nodes multicast group, false otherwise

## [◆ ](#ga55d67d4349dd354a7254a2f8e8320693)net\_ipv6\_is\_addr\_mcast\_global()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_mcast\_global | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is a global multicast address (FFxE::/16).

Parameters
:   | addr | IPv6 address. |
    | --- | --- |

Returns
:   True if the address is global multicast address, false otherwise.

## [◆ ](#ga611a4adb332715d983375899dcf101d0)net\_ipv6\_is\_addr\_mcast\_group()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_mcast\_group | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr*, | | --- | --- | --- | --- | |  |  | const struct [in6\_addr](structin6__addr.md) \* | *group* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address belongs to certain multicast group.

Parameters
:   | addr | IPv6 address. |
    | --- | --- |
    | group | Group id IPv6 address, the values must be in network byte order |

Returns
:   True if the IPv6 multicast address belongs to given multicast group, false otherwise.

## [◆ ](#gae27ca6956f943469cad0faa0ba738fc2)net\_ipv6\_is\_addr\_mcast\_iface()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_mcast\_iface | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is a interface scope multicast address (FFx1::).

Parameters
:   | addr | IPv6 address. |
    | --- | --- |

Returns
:   True if the address is a interface scope multicast address, false otherwise.

## [◆ ](#ga35bdad7c958f1ea656680000ee3f6bfd)net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is a interface scope all nodes multicast address (FF01::1).

Parameters
:   | addr | IPv6 address. |
    | --- | --- |

Returns
:   True if the address is a interface scope all nodes multicast address, false otherwise.

## [◆ ](#ga6f83a3a8701ec378b47337acba59d5e4)net\_ipv6\_is\_addr\_mcast\_link()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_mcast\_link | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is a link local scope multicast address (FFx2::).

Parameters
:   | addr | IPv6 address. |
    | --- | --- |

Returns
:   True if the address is a link local scope multicast address, false otherwise.

## [◆ ](#gaba3e1259f452381ef3e109bb2eb34c09)net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is a link local scope all nodes multicast address (FF02::1).

Parameters
:   | addr | IPv6 address. |
    | --- | --- |

Returns
:   True if the address is a link local scope all nodes multicast address, false otherwise.

## [◆ ](#ga497a148717c1c1095abeb4482566dda0)net\_ipv6\_is\_addr\_mcast\_mesh()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_mcast\_mesh | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is a mesh-local scope multicast address (FFx3::).

Parameters
:   | addr | IPv6 address. |
    | --- | --- |

Returns
:   True if the address is a mesh-local scope multicast address, false otherwise.

## [◆ ](#ga141ed5de3043dd7d6b45098aea38a4b1)net\_ipv6\_is\_addr\_mcast\_org()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_mcast\_org | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is an organization scope multicast address (FFx8::).

Parameters
:   | addr | IPv6 address. |
    | --- | --- |

Returns
:   True if the address is an organization scope multicast address, false otherwise.

## [◆ ](#gadc75208131d5a4333f31291ac5f8ce94)net\_ipv6\_is\_addr\_mcast\_scope()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_mcast\_scope | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr*, | | --- | --- | --- | --- | |  |  | int | *scope* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is a given scope multicast address (FFyx::).

Parameters
:   | addr | IPv6 address |
    | --- | --- |
    | scope | Scope to check |

Returns
:   True if the address is in given scope multicast address, false otherwise.

## [◆ ](#ga6704146124a14be9cf2a636947c35a00)net\_ipv6\_is\_addr\_mcast\_site()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_mcast\_site | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is a site scope multicast address (FFx5::).

Parameters
:   | addr | IPv6 address. |
    | --- | --- |

Returns
:   True if the address is a site scope multicast address, false otherwise.

## [◆ ](#ga5a334819f4e4bf87aea5caa7ef28c68a)net\_ipv6\_is\_addr\_solicited\_node()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_solicited\_node | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is solicited node multicast address FF02:0:0:0:0:1:FFXX:XXXX defined in RFC 3513.

Parameters
:   | addr | IPv6 address. |
    | --- | --- |

Returns
:   True if the address is solicited node address, false otherwise.

## [◆ ](#gafe2c8dc0bdb677ba9bc872d051aab2a0)net\_ipv6\_is\_addr\_unspecified()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_addr\_unspecified | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 address is unspecified (all bits zero).

Parameters
:   | addr | IPv6 address. |
    | --- | --- |

Returns
:   True if the address is unspecified, false otherwise.

## [◆ ](#gab2d854e2b24f866839e547c1092ccff6)net\_ipv6\_is\_global\_addr()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_global\_addr | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the given IPv6 address is a global address.

Parameters
:   | addr | A valid pointer on an IPv6 address |
    | --- | --- |

Returns
:   True if it is, false otherwise.

## [◆ ](#gacac4279ee8896ddf2a76c612b36edf38)net\_ipv6\_is\_ll\_addr()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_ll\_addr | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the given IPv6 address is a link local address.

Parameters
:   | addr | A valid pointer on an IPv6 address |
    | --- | --- |

Returns
:   True if it is, false otherwise.

## [◆ ](#ga00853528daf79c947dcdc320035ed538)net\_ipv6\_is\_my\_addr()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_my\_addr | ( | struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if IPv6 address is found in one of the network interfaces.

Parameters
:   | addr | IPv6 address |
    | --- | --- |

Returns
:   True if address was found, False otherwise.

## [◆ ](#gaf8c5158de9a65d840faa61bb3dec341c)net\_ipv6\_is\_my\_maddr()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_my\_maddr | ( | struct [in6\_addr](structin6__addr.md) \* | *maddr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if IPv6 multicast address is found in one of the network interfaces.

Parameters
:   | maddr | Multicast IPv6 address |
    | --- | --- |

Returns
:   True if address was found, False otherwise.

## [◆ ](#ga9654007b0a3c4d033df1ec3d00bd26ee)net\_ipv6\_is\_prefix()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_prefix | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *addr1*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *addr2*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *length* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if two IPv6 addresses are same when compared after prefix mask.

Parameters
:   | addr1 | First IPv6 address. |
    | --- | --- |
    | addr2 | Second IPv6 address. |
    | length | Prefix length (max length is 128). |

Returns
:   True if IPv6 prefixes are the same, False otherwise.

## [◆ ](#ga3f80a84f330a31aaa875fdea64dc18ec)net\_ipv6\_is\_same\_mcast\_scope()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_same\_mcast\_scope | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr\_1*, | | --- | --- | --- | --- | |  |  | const struct [in6\_addr](structin6__addr.md) \* | *addr\_2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the IPv6 addresses have the same multicast scope (FFyx::).

Parameters
:   | addr\_1 | IPv6 address 1 |
    | --- | --- |
    | addr\_2 | IPv6 address 2 |

Returns
:   True if both addresses have same multicast scope, false otherwise.

## [◆ ](#ga675d016e405e02882fda701aa8617ab7)net\_ipv6\_is\_sl\_addr()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_sl\_addr | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the given IPv6 address is a site local address.

Parameters
:   | addr | A valid pointer on an IPv6 address |
    | --- | --- |

Returns
:   True if it is, false otherwise.

## [◆ ](#gae10578b8801d213482de7d7d7e7ba230)net\_ipv6\_is\_ula\_addr()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_ipv6\_is\_ula\_addr | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check if the given IPv6 address is a unique local address.

Parameters
:   | addr | A valid pointer on an IPv6 address |
    | --- | --- |

Returns
:   True if it is, false otherwise.

## [◆ ](#gab0211c91e113cf01a8a16b1a106e7290)net\_ipv6\_unspecified\_address()

| const struct [in6\_addr](structin6__addr.md) \* net\_ipv6\_unspecified\_address | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Return pointer to any (all bits zeros) IPv6 address.

Returns
:   Any IPv6 address.

## [◆ ](#ga8be77d043d4d1d29e0879b3b22274629)net\_priority2vlan()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_priority2vlan | ( | enum [net\_priority](#gae87ef466e77ded673ed7e593d3eddffd) | *priority* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Convert network packet priority to network packet VLAN priority.

Parameters
:   | priority | Packet priority |
    | --- | --- |

Returns
:   VLAN priority (PCP)

## [◆ ](#ga7b3c41ae9b3962090d72c130a9fa61b1)net\_rx\_priority2tc()

| int net\_rx\_priority2tc | ( | enum [net\_priority](#gae87ef466e77ded673ed7e593d3eddffd) | *prio* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Convert Rx network packet priority to traffic class so we can place the packet into correct Rx queue.

Parameters
:   | prio | Network priority |
    | --- | --- |

Returns
:   Rx traffic class that handles that priority network traffic.

## [◆ ](#gacccfbac6a03480840fa219e9a1924dc6)net\_sin()

| | struct [sockaddr\_in](structsockaddr__in.md) \* net\_sin | ( | const struct [sockaddr](structsockaddr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Get [sockaddr\_in](structsockaddr__in.md "Socket address struct for IPv4.") from sockaddr.

This is a helper so that the code calling this function can be made shorter.

Parameters
:   | addr | Socket address |
    | --- | --- |

Returns
:   Pointer to IPv4 socket address

## [◆ ](#gad97b2c3da722409eada099f9b7e13f03)net\_sin6()

| | struct [sockaddr\_in6](structsockaddr__in6.md) \* net\_sin6 | ( | const struct [sockaddr](structsockaddr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Get [sockaddr\_in6](structsockaddr__in6.md "Socket address struct for IPv6.") from sockaddr.

This is a helper so that the code calling this function can be made shorter.

Parameters
:   | addr | Socket address |
    | --- | --- |

Returns
:   Pointer to IPv6 socket address

## [◆ ](#gae86d2cd402142190e1ea1c120a57939f)net\_sin6\_ptr()

| | struct [sockaddr\_in6\_ptr](structsockaddr__in6__ptr.md) \* net\_sin6\_ptr | ( | const struct sockaddr\_ptr \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Get [sockaddr\_in6\_ptr](structsockaddr__in6__ptr.md) from sockaddr\_ptr.

This is a helper so that the code calling this function can be made shorter.

Parameters
:   | addr | Socket address |
    | --- | --- |

Returns
:   Pointer to IPv6 socket address

## [◆ ](#ga4b948e84590081a8aed2a63496e57ae2)net\_sin\_ptr()

| | struct [sockaddr\_in\_ptr](structsockaddr__in__ptr.md) \* net\_sin\_ptr | ( | const struct sockaddr\_ptr \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Get [sockaddr\_in\_ptr](structsockaddr__in__ptr.md) from sockaddr\_ptr.

This is a helper so that the code calling this function can be made shorter.

Parameters
:   | addr | Socket address |
    | --- | --- |

Returns
:   Pointer to IPv4 socket address

## [◆ ](#gad5cf206e18769a15f9fc917e416db6ee)net\_sll\_ptr()

| | struct [sockaddr\_ll\_ptr](structsockaddr__ll__ptr.md) \* net\_sll\_ptr | ( | const struct sockaddr\_ptr \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Get [sockaddr\_ll\_ptr](structsockaddr__ll__ptr.md) from sockaddr\_ptr.

This is a helper so that the code calling this function can be made shorter.

Parameters
:   | addr | Socket address |
    | --- | --- |

Returns
:   Pointer to linklayer socket address

## [◆ ](#ga1695009388402938dcc2e49b526ebd1f)net\_tcp\_seq\_cmp()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) net\_tcp\_seq\_cmp | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *seq1*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *seq2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Compare TCP sequence numbers.

This function compares TCP sequence numbers, accounting for wraparound effects.

Parameters
:   | seq1 | First sequence number |
    | --- | --- |
    | seq2 | Seconds sequence number |

Returns
:   < 0 if seq1 < seq2, 0 if seq1 == seq2, > 0 if seq > seq2

## [◆ ](#gaa77b299f53e5535ac4c4bea1b6531a34)net\_tcp\_seq\_greater()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_tcp\_seq\_greater | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *seq1*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *seq2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Check that one TCP sequence number is greater.

This is convenience function on top of [net\_tcp\_seq\_cmp()](#ga1695009388402938dcc2e49b526ebd1f).

Parameters
:   | seq1 | First sequence number |
    | --- | --- |
    | seq2 | Seconds sequence number |

Returns
:   True if seq > seq2

## [◆ ](#gae74c9ba7ff4addbce7f931bd6fa91fa0)net\_tx\_priority2tc()

| int net\_tx\_priority2tc | ( | enum [net\_priority](#gae87ef466e77ded673ed7e593d3eddffd) | *prio* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Convert Tx network packet priority to traffic class so we can place the packet into correct Tx queue.

Parameters
:   | prio | Network priority |
    | --- | --- |

Returns
:   Tx traffic class that handles that priority network traffic.

## [◆ ](#ga14bc7018e3dd7c3e320b44a077343ce4)net\_vlan2priority()

| | enum [net\_priority](#gae87ef466e77ded673ed7e593d3eddffd) net\_vlan2priority | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *priority* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_ip.h](net__ip_8h.md)>`

Convert network packet VLAN priority to network packet priority so we can place the packet into correct queue.

Parameters
:   | priority | VLAN priority |
    | --- | --- |

Returns
:   Network priority

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
