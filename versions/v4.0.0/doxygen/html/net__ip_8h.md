---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__ip_8h.html
original_path: doxygen/html/net__ip_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_ip.h File Reference

IPv6 and IPv4 definitions.
[More...](#details)

`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/net/net_linkaddr.h](net__linkaddr_8h_source.md)>`  
`#include <zephyr/syscalls/net_ip.h>`

[Go to the source code of this file.](net__ip_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [in6\_addr](structin6__addr.md) |
|  | IPv6 address struct. [More...](structin6__addr.md#details) |
| struct | [in\_addr](structin__addr.md) |
|  | IPv4 address struct. [More...](structin__addr.md#details) |
| struct | [sockaddr\_in6](structsockaddr__in6.md) |
|  | Socket address struct for IPv6. [More...](structsockaddr__in6.md#details) |
| struct | [sockaddr\_in](structsockaddr__in.md) |
|  | Socket address struct for IPv4. [More...](structsockaddr__in.md#details) |
| struct | [sockaddr\_ll](structsockaddr__ll.md) |
|  | Socket address struct for packet socket. [More...](structsockaddr__ll.md#details) |
| struct | [iovec](structiovec.md) |
|  | IO vector array element. [More...](structiovec.md#details) |
| struct | [msghdr](structmsghdr.md) |
|  | Message struct. [More...](structmsghdr.md#details) |
| struct | [cmsghdr](structcmsghdr.md) |
|  | Control message ancillary data. [More...](structcmsghdr.md#details) |
| struct | [sockaddr](structsockaddr.md) |
|  | Generic sockaddr struct. [More...](structsockaddr.md#details) |
| struct | [net\_tuple](structnet__tuple.md) |
|  | IPv6/IPv4 network connection tuple. [More...](structnet__tuple.md#details) |

| Macros | |
| --- | --- |
| #define | [PF\_UNSPEC](group__ip__4__6.md#ga51dba11ffc8e3b1bf695e721b3144094)   0 |
|  | Unspecified protocol family. |
| #define | [PF\_INET](group__ip__4__6.md#ga3f5da0b5be27fe31ec7cc11bfa8d1a25)   1 |
|  | IP protocol family version 4. |
| #define | [PF\_INET6](group__ip__4__6.md#ga323f2649198fc7e64b19881869265618)   2 |
|  | IP protocol family version 6. |
| #define | [PF\_PACKET](group__ip__4__6.md#ga8e297adb5fe2e28b0d9d921a5d56a8e9)   3 |
|  | Packet family. |
| #define | [PF\_CAN](group__ip__4__6.md#gaeac0c3db7a1e021f17987bcc76893849)   4 |
|  | Controller Area Network. |
| #define | [PF\_NET\_MGMT](group__ip__4__6.md#ga288b09307bcc46aef2acf2af5e3e1006)   5 |
|  | Network management info. |
| #define | [PF\_LOCAL](group__ip__4__6.md#ga521c315ca2a2a4e6345878e84af4085e)   6 |
|  | Inter-process communication. |
| #define | [PF\_UNIX](group__ip__4__6.md#ga0407288f5fb975a03b21d5287c282b2e)   [PF\_LOCAL](group__ip__4__6.md#ga521c315ca2a2a4e6345878e84af4085e) |
|  | Inter-process communication. |
| #define | [AF\_UNSPEC](group__ip__4__6.md#gae77ae24b14b7b7f294f3e04121173f12)   [PF\_UNSPEC](group__ip__4__6.md#ga51dba11ffc8e3b1bf695e721b3144094) |
|  | Unspecified address family. |
| #define | [AF\_INET](group__ip__4__6.md#ga9930604d0e32588eae76f43ca38e7826)   [PF\_INET](group__ip__4__6.md#ga3f5da0b5be27fe31ec7cc11bfa8d1a25) |
|  | IP protocol family version 4. |
| #define | [AF\_INET6](group__ip__4__6.md#gaa03706b2738b9a58d4985dfbe99e1bac)   [PF\_INET6](group__ip__4__6.md#ga323f2649198fc7e64b19881869265618) |
|  | IP protocol family version 6. |
| #define | [AF\_PACKET](group__ip__4__6.md#gaa89aa4cd481fe17260c3f5d493cc23f5)   [PF\_PACKET](group__ip__4__6.md#ga8e297adb5fe2e28b0d9d921a5d56a8e9) |
|  | Packet family. |
| #define | [AF\_CAN](group__ip__4__6.md#ga546620c7e758f003b24b7fdae4f97bd4)   [PF\_CAN](group__ip__4__6.md#gaeac0c3db7a1e021f17987bcc76893849) |
|  | Controller Area Network. |
| #define | [AF\_NET\_MGMT](group__ip__4__6.md#ga41d0cbb55cd9550a7f732b1520119c15)   [PF\_NET\_MGMT](group__ip__4__6.md#ga288b09307bcc46aef2acf2af5e3e1006) |
|  | Network management info. |
| #define | [AF\_LOCAL](group__ip__4__6.md#gae24f1f9ea44fcce3affcb2137f593dc1)   [PF\_LOCAL](group__ip__4__6.md#ga521c315ca2a2a4e6345878e84af4085e) |
|  | Inter-process communication. |
| #define | [AF\_UNIX](group__ip__4__6.md#ga0fd8739854bc8b48d65f0b669fed3ffe)   [PF\_UNIX](group__ip__4__6.md#ga0407288f5fb975a03b21d5287c282b2e) |
|  | Inter-process communication. |
| #define | [ntohs](group__ip__4__6.md#gada37feda716b4ba89cf9dba34288141d)(x) |
|  | Convert 16-bit value from network to host byte order. |
| #define | [ntohl](group__ip__4__6.md#gac317b3e903719ba02894f1710f7f2439)(x) |
|  | Convert 32-bit value from network to host byte order. |
| #define | [ntohll](group__ip__4__6.md#ga3cfcf123d4ead264289232f91f2c9ca5)(x) |
|  | Convert 64-bit value from network to host byte order. |
| #define | [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(x) |
|  | Convert 16-bit value from host to network byte order. |
| #define | [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(x) |
|  | Convert 32-bit value from host to network byte order. |
| #define | [htonll](group__ip__4__6.md#ga9f4bf0773c45ad9a9753a1b784a13fbb)(x) |
|  | Convert 64-bit value from host to network byte order. |
| #define | [NET\_IPV6\_ADDR\_SIZE](group__ip__4__6.md#ga1eefdabf590090be9f98bdf4a2f43bb4)   16 |
|  | Binary size of the IPv6 address. |
| #define | [NET\_IPV4\_ADDR\_SIZE](group__ip__4__6.md#ga10a82ea9ba9ca19f3b773bdd53c978e0)   4 |
|  | Binary size of the IPv4 address. |
| #define | [CMSG\_FIRSTHDR](group__ip__4__6.md#ga39567a31d167fc53336d2ab4a2cd78a4)([msghdr](structmsghdr.md)) |
|  | Returns a pointer to the first cmsghdr in the ancillary data buffer associated with the passed msghdr. |
| #define | [CMSG\_NXTHDR](group__ip__4__6.md#ga77c17efca635d597cb6e98b28172bdc0)([msghdr](structmsghdr.md), cmsg) |
|  | Returns the next valid cmsghdr after the passed cmsghdr. |
| #define | [CMSG\_DATA](group__ip__4__6.md#ga5ab6d56e410ac0904107e84aeb1484cc)(cmsg) |
|  | Returns a pointer to the data portion of a cmsghdr. |
| #define | [CMSG\_SPACE](group__ip__4__6.md#ga8db11d639dd07c723256f3bb5bc89044)(length) |
|  | Returns the number of bytes an ancillary element with payload of the passed data length occupies. |
| #define | [CMSG\_LEN](group__ip__4__6.md#gadb36e4ff4fa9a0c6730321c4bfcf64bc)(length) |
|  | Returns the value to store in the cmsg\_len member of the cmsghdr structure, taking into account any necessary alignment. |
| #define | [IN6ADDR\_ANY\_INIT](group__ip__4__6.md#ga1de876a356ee05a2e9427b741f99f49c) |
|  | IPv6 address initializer. |
| #define | [IN6ADDR\_LOOPBACK\_INIT](group__ip__4__6.md#ga5562c81af19ee5988ddc5a5c6153cf37) |
|  | IPv6 loopback address initializer. |
| #define | [INADDR\_ANY](group__ip__4__6.md#ga5d1940045dc2e7de552f3d4ff13a74ab)   0 |
|  | IPv4 any address. |
| #define | [INADDR\_ANY\_INIT](group__ip__4__6.md#ga915fcf49ce8c1e235e64fc83b57ec5b1)   { { { [INADDR\_ANY](group__ip__4__6.md#ga5d1940045dc2e7de552f3d4ff13a74ab) } } } |
|  | IPv4 address initializer. |
| #define | [INADDR\_LOOPBACK\_INIT](group__ip__4__6.md#ga554163cb2fa86ef4307dd1fff2aad2eb)   { { { 127, 0, 0, 1 } } } |
|  | IPv6 loopback address initializer. |
| #define | [INET\_ADDRSTRLEN](group__ip__4__6.md#ga93b37007689284fd9c4bde1a8f4b9199)   16 |
|  | Max length of the IPv4 address as a string. |
| #define | [INET6\_ADDRSTRLEN](group__ip__4__6.md#gaf776b22a727aae7c9f4d869d50df47e8)   46 |
|  | Max length of the IPv6 address as a string. |
| #define | [NET\_MAX\_PRIORITIES](group__ip__4__6.md#ga5b32bdfc249437709bb25bd95ec7d6d7)   8 |
|  | How many priority values there are. |
| #define | [net\_ipaddr\_copy](group__ip__4__6.md#ga75ffcc08e621c2d47d1ae043fce2acad)(dest, src) |
|  | Copy an IPv4 or IPv6 address. |

| Typedefs | |
| --- | --- |
| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short int | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) |
|  | Socket address family type. |
| typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) |
|  | Length of a socket address. |

| Enumerations | |
| --- | --- |
| enum | [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) {     [IPPROTO\_IP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a334b0a4a5a3e331e7c7864471e9eab08) = 0 , [IPPROTO\_ICMP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a7ccd735b73f6955ae2f4abf3e7ca6bb4) = 1 , [IPPROTO\_IGMP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4cbcb48be0cd8eb6fb5b5741f1c7b639) = 2 , [IPPROTO\_IPIP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a49a42f6d628bf65e78478e8eb4874ff2) = 4 ,     [IPPROTO\_TCP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a4a3c433d15859f62bacc06312791a45e) = 6 , [IPPROTO\_UDP](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31abd7dfb22e255a4eed332f41de12d7321) = 17 , [IPPROTO\_IPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a892549243e60ed1e04e88a14b44d8185) = 41 , [IPPROTO\_ICMPV6](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31aeeff57e3cf726718a92b2138e5842926) = 58 ,     [IPPROTO\_RAW](group__ip__4__6.md#ggaf06819bf427cc58be1229b27b373ca31a3f186705d5c21da1b72ecb91cca1f7a4) = 255   } |
|  | Protocol numbers from IANA/BSD. [More...](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) |
| enum | [net\_ip\_protocol\_secure](group__ip__4__6.md#ga721da18d2a3cfd9b3a56e9efc9f6e58b) {     [IPPROTO\_TLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba6d479e64d940cea948c874d36c656fcc) = 256 , [IPPROTO\_TLS\_1\_1](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba102692f9f57dd0ec6f8c6cb54a235d4c) = 257 , [IPPROTO\_TLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa5e176fa47ca23a6f25101a5203f8e5a) = 258 , [IPPROTO\_TLS\_1\_3](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58baa43bf0393de00897b350b361f97c85ac) = 259 ,     [IPPROTO\_DTLS\_1\_0](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58ba92e94005d7a80aacbffad2f3f10555ef) = 272 , [IPPROTO\_DTLS\_1\_2](group__ip__4__6.md#gga721da18d2a3cfd9b3a56e9efc9f6e58bad4d2a6ca8756ee52221f19fb06c34a1c) = 273   } |
|  | Protocol numbers for TLS protocols. [More...](group__ip__4__6.md#ga721da18d2a3cfd9b3a56e9efc9f6e58b) |
| enum | [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) { [SOCK\_STREAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424) = 1 , [SOCK\_DGRAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc) , [SOCK\_RAW](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231) } |
|  | Socket type. [More...](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) |
| enum | [net\_ip\_mtu](group__ip__4__6.md#ga7a207761e4879c140f48f93978cb2f0b) { [NET\_IPV6\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c) = 1280 , [NET\_IPV4\_MTU](group__ip__4__6.md#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1) = 576 } |
|  | IP Maximum Transfer Unit. [More...](group__ip__4__6.md#ga7a207761e4879c140f48f93978cb2f0b) |
| enum | [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) {     [NET\_PRIORITY\_BK](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b) = 1 , [NET\_PRIORITY\_BE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce) = 0 , [NET\_PRIORITY\_EE](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0) = 2 , [NET\_PRIORITY\_CA](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354) = 3 ,     [NET\_PRIORITY\_VI](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792) = 4 , [NET\_PRIORITY\_VO](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a) = 5 , [NET\_PRIORITY\_IC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05) = 6 , [NET\_PRIORITY\_NC](group__ip__4__6.md#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef) = 7   } |
|  | Network packet priority settings described in IEEE 802.1Q Annex I.1. [More...](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) |
| enum | [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) { [NET\_ADDR\_ANY\_STATE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df) = -1 , [NET\_ADDR\_TENTATIVE](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9) = 0 , [NET\_ADDR\_PREFERRED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a) , [NET\_ADDR\_DEPRECATED](group__ip__4__6.md#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3) } |
|  | What is the current state of the network address. [More...](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) |
| enum | [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) {     [NET\_ADDR\_ANY](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6) = 0 , [NET\_ADDR\_AUTOCONF](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006) , [NET\_ADDR\_DHCP](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db) , [NET\_ADDR\_MANUAL](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e) ,     [NET\_ADDR\_OVERRIDABLE](group__ip__4__6.md#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4)   } |
|  | How the network address is assigned to network interface. [More...](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_loopback](group__ip__4__6.md#gaa662667005bdc00bf1eb5cf243aad874) (struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a loopback address (::1). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast](group__ip__4__6.md#ga1a2fb0427eeab1a5dec6d69208ad7f02) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a multicast address. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv6\_addr\_lookup](group__ip__4__6.md#ga13b5a26fc672d15697f99e85543184bb) (const struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_my\_addr](group__ip__4__6.md#ga00853528daf79c947dcdc320035ed538) (struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if IPv6 address is found in one of the network interfaces. |
| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | [net\_if\_ipv6\_maddr\_lookup](group__ip__4__6.md#gadb4031153c4fef86110879befa6b9975) (const struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_my\_maddr](group__ip__4__6.md#gaf8c5158de9a65d840faa61bb3dec341c) (struct [in6\_addr](structin6__addr.md) \*maddr) |
|  | Check if IPv6 multicast address is found in one of the network interfaces. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_prefix](group__ip__4__6.md#ga9654007b0a3c4d033df1ec3d00bd26ee) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) length) |
|  | Check if two IPv6 addresses are same when compared after prefix mask. |
| static void | [net\_ipv6\_addr\_prefix\_mask](group__ip__4__6.md#ga4e91a4298604a916731bf591acc7b326) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*inaddr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*outaddr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prefix\_len) |
|  | Get the IPv6 network address via the unicast address and the prefix mask. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_addr\_loopback](group__ip__4__6.md#ga879e4aed725d7ea3fe609fa989f14735) (struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the IPv4 address is a loopback address (127.0.0.0/8). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_addr\_unspecified](group__ip__4__6.md#gadc623ecacf024733ab6d477d87cc4b9d) (const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the IPv4 address is unspecified (all bits zero). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_addr\_mcast](group__ip__4__6.md#gae8c3302cf9ca457de32eabcf65975b70) (const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the IPv4 address is a multicast address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_ll\_addr](group__ip__4__6.md#gac000a319de7a6f95d4a63719bca3b865) (const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the given IPv4 address is a link local address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_private\_addr](group__ip__4__6.md#ga6f19cb74de130d70668599c05a5ed66b) (const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the given IPv4 address is from a private address range. |
| static void | [net\_ipv4\_addr\_copy\_raw](group__ip__4__6.md#gaf731738fb1761208739976d767736f87) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dest, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src) |
|  | Copy an IPv4 address raw buffer. |
| static void | [net\_ipv6\_addr\_copy\_raw](group__ip__4__6.md#ga4925e6f3734b8fc1d9cb1ca1a510b5f1) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dest, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src) |
|  | Copy an IPv6 address raw buffer. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_addr\_cmp](group__ip__4__6.md#ga0bdcc8dad8eb42c02426e55378ececf8) (const struct [in\_addr](structin__addr.md) \*addr1, const struct [in\_addr](structin__addr.md) \*addr2) |
|  | Compare two IPv4 addresses. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_addr\_cmp\_raw](group__ip__4__6.md#ga32ffb42c62169ac9b34a0faa7c7ffd12) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2) |
|  | Compare two raw IPv4 address buffers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_addr\_cmp](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8) (const struct [in6\_addr](structin6__addr.md) \*addr1, const struct [in6\_addr](structin6__addr.md) \*addr2) |
|  | Compare two IPv6 addresses. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_addr\_cmp\_raw](group__ip__4__6.md#gafbe40461a645cf11fc8b3a07e1d9156e) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr1, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr2) |
|  | Compare two raw IPv6 address buffers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_ll\_addr](group__ip__4__6.md#gacac4279ee8896ddf2a76c612b36edf38) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the given IPv6 address is a link local address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_sl\_addr](group__ip__4__6.md#ga675d016e405e02882fda701aa8617ab7) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the given IPv6 address is a site local address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_ula\_addr](group__ip__4__6.md#gae10578b8801d213482de7d7d7e7ba230) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the given IPv6 address is a unique local address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_global\_addr](group__ip__4__6.md#gab2d854e2b24f866839e547c1092ccff6) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the given IPv6 address is a global address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_private\_addr](group__ip__4__6.md#gad35da6e137d62231052dda63c68b7eff) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the given IPv6 address is from a private/local address range. |
| const struct [in6\_addr](structin6__addr.md) \* | [net\_ipv6\_unspecified\_address](group__ip__4__6.md#gab0211c91e113cf01a8a16b1a106e7290) (void) |
|  | Return pointer to any (all bits zeros) IPv6 address. |
| const struct [in\_addr](structin__addr.md) \* | [net\_ipv4\_unspecified\_address](group__ip__4__6.md#gaceb9afdd7f2f78d96e6debd72f63ebf0) (void) |
|  | Return pointer to any (all bits zeros) IPv4 address. |
| const struct [in\_addr](structin__addr.md) \* | [net\_ipv4\_broadcast\_address](group__ip__4__6.md#ga4df601fd1c89f1908df52b2673f9b113) (void) |
|  | Return pointer to broadcast (all bits ones) IPv4 address. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga558b31e556a1a4b8d1e68a78f3f755ea) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_addr\_mask\_cmp](group__ip__4__6.md#ga715455ec5e8041c5d7075fa6913674cd) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the given address belongs to same subnet that has been configured for the interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#ga8f93179138c1942bc1a099102a4314cf) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_addr\_bcast](group__ip__4__6.md#gac545e2252f221c73c80cea746dffa083) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the given IPv4 address is a broadcast address. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv4\_addr\_lookup](group__ip__4__6.md#ga04a8f21d173d51bdcc092b92ed949e53) (const struct [in\_addr](structin__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv4\_is\_my\_addr](group__ip__4__6.md#ga3db2a1fca0b525a7202277700b987eb9) (const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the IPv4 address is assigned to any network interface in the system. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_unspecified](group__ip__4__6.md#gafe2c8dc0bdb677ba9bc872d051aab2a0) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is unspecified (all bits zero). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_solicited\_node](group__ip__4__6.md#ga5a334819f4e4bf87aea5caa7ef28c68a) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is solicited node multicast address FF02:0:0:0:0:1:FFXX:XXXX defined in RFC 3513. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_scope](group__ip__4__6.md#gadc75208131d5a4333f31291ac5f8ce94) (const struct [in6\_addr](structin6__addr.md) \*addr, int scope) |
|  | Check if the IPv6 address is a given scope multicast address (FFyx::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_same\_mcast\_scope](group__ip__4__6.md#ga3f80a84f330a31aaa875fdea64dc18ec) (const struct [in6\_addr](structin6__addr.md) \*addr\_1, const struct [in6\_addr](structin6__addr.md) \*addr\_2) |
|  | Check if the IPv6 addresses have the same multicast scope (FFyx::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_global](group__ip__4__6.md#ga55d67d4349dd354a7254a2f8e8320693) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a global multicast address (FFxE::/16). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_iface](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a interface scope multicast address (FFx1::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_link](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a link local scope multicast address (FFx2::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_mesh](group__ip__4__6.md#ga497a148717c1c1095abeb4482566dda0) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a mesh-local scope multicast address (FFx3::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_site](group__ip__4__6.md#ga6704146124a14be9cf2a636947c35a00) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a site scope multicast address (FFx5::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_org](group__ip__4__6.md#ga141ed5de3043dd7d6b45098aea38a4b1) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is an organization scope multicast address (FFx8::). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_group](group__ip__4__6.md#ga611a4adb332715d983375899dcf101d0) (const struct [in6\_addr](structin6__addr.md) \*addr, const struct [in6\_addr](structin6__addr.md) \*[group](structgroup.md)) |
|  | Check if the IPv6 address belongs to certain multicast group. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_all\_nodes\_group](group__ip__4__6.md#gacf00ae106727f97e2fd35be68418354d) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address belongs to the all nodes multicast group. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_iface\_all\_nodes](group__ip__4__6.md#ga35bdad7c958f1ea656680000ee3f6bfd) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a interface scope all nodes multicast address (FF01::1). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_is\_addr\_mcast\_link\_all\_nodes](group__ip__4__6.md#gaba3e1259f452381ef3e109bb2eb34c09) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if the IPv6 address is a link local scope all nodes multicast address (FF02::1). |
| static void | [net\_ipv6\_addr\_create\_solicited\_node](group__ip__4__6.md#ga6091a7406c136fcf480517cb969c9d90) (const struct [in6\_addr](structin6__addr.md) \*src, struct [in6\_addr](structin6__addr.md) \*dst) |
|  | Create solicited node IPv6 multicast address FF02:0:0:0:0:1:FFXX:XXXX defined in RFC 3513. |
| static void | [net\_ipv6\_addr\_create](group__ip__4__6.md#ga0a78f83dcb4e341d86d9352506196696) (struct [in6\_addr](structin6__addr.md) \*addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr0, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr1, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr2, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr3, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr4, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr5, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr6, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr7) |
|  | Construct an IPv6 address from eight 16-bit words. |
| static void | [net\_ipv6\_addr\_create\_ll\_allnodes\_mcast](group__ip__4__6.md#ga58cbba1c522815b1ce201b0377ffe0b2) (struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Create link local allnodes multicast IPv6 address. |
| static void | [net\_ipv6\_addr\_create\_ll\_allrouters\_mcast](group__ip__4__6.md#ga30821f0a2c08b4b01b71d362e3a25de1) (struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Create link local allrouters multicast IPv6 address. |
| static void | [net\_ipv6\_addr\_create\_v4\_mapped](group__ip__4__6.md#ga8c6162c6212051037a33477aab9fc55f) (const struct [in\_addr](structin__addr.md) \*addr4, struct [in6\_addr](structin6__addr.md) \*addr6) |
|  | Create IPv4 mapped IPv6 address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_addr\_is\_v4\_mapped](group__ip__4__6.md#ga53c24abd635fb2bcb137584dbc8a9026) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Is the IPv6 address an IPv4 mapped one. |
| static void | [net\_ipv6\_addr\_create\_iid](group__ip__4__6.md#ga6d41f1de27e2e8fbb8f12925eba852b4) (struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr) |
|  | Create IPv6 address interface identifier. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipv6\_addr\_based\_on\_ll](group__ip__4__6.md#gaf4b0c30b926748625bd3c4c81d06ffc5) (const struct [in6\_addr](structin6__addr.md) \*addr, const struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr) |
|  | Check if given address is based on link layer address. |
| static struct [sockaddr\_in6](structsockaddr__in6.md) \* | [net\_sin6](group__ip__4__6.md#gad97b2c3da722409eada099f9b7e13f03) (const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Get [sockaddr\_in6](structsockaddr__in6.md "Socket address struct for IPv6.") from sockaddr. |
| static struct [sockaddr\_in](structsockaddr__in.md) \* | [net\_sin](group__ip__4__6.md#gacccfbac6a03480840fa219e9a1924dc6) (const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Get [sockaddr\_in](structsockaddr__in.md "Socket address struct for IPv4.") from sockaddr. |
| static struct sockaddr\_in6\_ptr \* | [net\_sin6\_ptr](group__ip__4__6.md#gae86d2cd402142190e1ea1c120a57939f) (const struct sockaddr\_ptr \*addr) |
|  | Get sockaddr\_in6\_ptr from sockaddr\_ptr. |
| static struct sockaddr\_in\_ptr \* | [net\_sin\_ptr](group__ip__4__6.md#ga4b948e84590081a8aed2a63496e57ae2) (const struct sockaddr\_ptr \*addr) |
|  | Get sockaddr\_in\_ptr from sockaddr\_ptr. |
| static struct sockaddr\_ll\_ptr \* | [net\_sll\_ptr](group__ip__4__6.md#gad5cf206e18769a15f9fc917e416db6ee) (const struct sockaddr\_ptr \*addr) |
|  | Get sockaddr\_ll\_ptr from sockaddr\_ptr. |
| static struct sockaddr\_can\_ptr \* | [net\_can\_ptr](group__ip__4__6.md#gac2fb590a35961c04807dd985f462c5fb) (const struct sockaddr\_ptr \*addr) |
|  | Get sockaddr\_can\_ptr from sockaddr\_ptr. |
| int | [net\_addr\_pton](group__ip__4__6.md#ga264b3c0a13493eac291ddc85d0b4d43d) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst) |
|  | Convert a string to IP address. |
| char \* | [net\_addr\_ntop](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src, char \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Convert IP address to string form. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_ipaddr\_parse](group__ip__4__6.md#ga9918e156f0039cf45d487a112e0a2ada) (const char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) str\_len, struct [sockaddr](structsockaddr.md) \*addr) |
|  | Parse a string that contains either IPv4 or IPv6 address and optional port, and store the information in user supplied sockaddr struct. |
| int | [net\_port\_set\_default](group__ip__4__6.md#gaa2354e12d310c0647a98c873c7b7e5ad) (struct [sockaddr](structsockaddr.md) \*addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) default\_port) |
|  | Set the default port in the sockaddr structure. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [net\_tcp\_seq\_cmp](group__ip__4__6.md#ga1695009388402938dcc2e49b526ebd1f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq2) |
|  | Compare TCP sequence numbers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_tcp\_seq\_greater](group__ip__4__6.md#gaa77b299f53e5535ac4c4bea1b6531a34) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seq2) |
|  | Check that one TCP sequence number is greater. |
| int | [net\_bytes\_from\_str](group__ip__4__6.md#ga8b794f251cf8412c769ab415902a9f32) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, int buf\_len, const char \*src) |
|  | Convert a string of hex values to array of bytes. |
| int | [net\_tx\_priority2tc](group__ip__4__6.md#gae74c9ba7ff4addbce7f931bd6fa91fa0) (enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) prio) |
|  | Convert Tx network packet priority to traffic class so we can place the packet into correct Tx queue. |
| int | [net\_rx\_priority2tc](group__ip__4__6.md#ga7b3c41ae9b3962090d72c130a9fa61b1) (enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) prio) |
|  | Convert Rx network packet priority to traffic class so we can place the packet into correct Rx queue. |
| static enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) | [net\_vlan2priority](group__ip__4__6.md#ga14bc7018e3dd7c3e320b44a077343ce4) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority) |
|  | Convert network packet VLAN priority to network packet priority so we can place the packet into correct queue. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_priority2vlan](group__ip__4__6.md#ga8be77d043d4d1d29e0879b3b22274629) (enum [net\_priority](group__ip__4__6.md#gae87ef466e77ded673ed7e593d3eddffd) priority) |
|  | Convert network packet priority to network packet VLAN priority. |
| const char \* | [net\_family2str](group__ip__4__6.md#gaba4c72e3aa2ceb4ac67d25112fb36523) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family) |
|  | Return network address family value as a string. |
| static int | [net\_ipv6\_pe\_add\_filter](group__ip__4__6.md#ga14f9607f6c18869e7755ab497ff62147) (struct [in6\_addr](structin6__addr.md) \*addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_denylist) |
|  | Add IPv6 prefix as a privacy extension filter. |
| static int | [net\_ipv6\_pe\_del\_filter](group__ip__4__6.md#ga76e7787a18dbf0b3575d46f81603f65a) (struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Delete IPv6 prefix from privacy extension filter list. |

## Detailed Description

IPv6 and IPv4 definitions.

Generic IPv6 and IPv4 address definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_ip.h](net__ip_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
