---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__context_8h.html
original_path: doxygen/html/net__context_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_context.h File Reference

Network context definitions.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/net_stats.h](net__stats_8h_source.md)>`

[Go to the source code of this file.](net__context_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_context](structnet__context.md) |
|  | Note that we do not store the actual source IP address in the context because the address is already set in the network interface struct. [More...](structnet__context.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_CONTEXT\_IN\_USE](group__net__context.md#ga5e2f5fcc08863a4090bc04040ee88d29)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Is this context used or not. |
| #define | [NET\_CONTEXT\_FAMILY](group__net__context.md#gac8f6e3a16d52e8e376c38eec0ed8a940)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5)) |
|  | The address family, connection type and IP protocol are stored into a bit field to save space. |
| #define | [NET\_CONTEXT\_TYPE](group__net__context.md#gac9b4cf9beecaac5bf05db3111c803678)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7)) |
|  | Type of the connection (datagram / stream / raw). |
| #define | [NET\_CONTEXT\_REMOTE\_ADDR\_SET](group__net__context.md#ga84206421e8f2e1eb114d393f0c81428b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Remote address set. |
| #define | [NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Is the socket accepting connections. |
| #define | [NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Is the socket closing / closed. |
| #define | [NET\_CONTEXT\_BOUND\_TO\_IFACE](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Context is bound to a specific interface. |
| #define | [net\_context\_setup\_pools](group__net__context.md#gadde93ce383a4c5b0f450db1eaa0dfd4d)(context, tx\_pool, data\_pool) |
|  | Set custom network buffer pools for context send operations. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317)) (struct [net\_context](structnet__context.md) \*context, struct [net\_pkt](structnet__pkt.md) \*pkt, union net\_ip\_header \*ip\_hdr, union net\_proto\_header \*proto\_hdr, int status, void \*user\_data) |
|  | Network data receive callback. |
| typedef void(\* | [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93)) (struct [net\_context](structnet__context.md) \*context, int status, void \*user\_data) |
|  | Network data send callback. |
| typedef void(\* | [net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8)) (struct [net\_context](structnet__context.md) \*new\_context, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen, int status, void \*user\_data) |
|  | Accept callback. |
| typedef void(\* | [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71)) (struct [net\_context](structnet__context.md) \*context, int status, void \*user\_data) |
|  | Connection callback. |
| typedef struct k\_mem\_slab \*(\* | [net\_pkt\_get\_slab\_func\_t](group__net__context.md#ga3bb4bbd522ede36213bafe86f2d1d770)) (void) |
|  | Function that is called to get the slab that is used for [net\_pkt](structnet__pkt.md "Network packet.") allocations. |
| typedef struct [net\_buf\_pool](structnet__buf__pool.md) \*(\* | [net\_pkt\_get\_pool\_func\_t](group__net__context.md#gae3082af116955d4175c025a02b296c91)) (void) |
|  | Function that is called to get the pool that is used for [net\_buf](structnet__buf.md "Network buffer representation.") allocations. |
| typedef void(\* | [net\_context\_cb\_t](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba)) (struct [net\_context](structnet__context.md) \*context, void \*user\_data) |
|  | Callback used while iterating over network contexts. |

| Enumerations | |
| --- | --- |
| enum | [net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) {     [NET\_OPT\_PRIORITY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c) = 1 , [NET\_OPT\_TXTIME](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184) = 2 , [NET\_OPT\_SOCKS5](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c) = 3 , [NET\_OPT\_RCVTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076) = 4 ,     [NET\_OPT\_SNDTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668) = 5 , [NET\_OPT\_RCVBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1) = 6 , [NET\_OPT\_SNDBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08) = 7 , [NET\_OPT\_DSCP\_ECN](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c) = 8 ,     [NET\_OPT\_REUSEADDR](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561) = 9 , [NET\_OPT\_REUSEPORT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4) = 10 , [NET\_OPT\_IPV6\_V6ONLY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c) = 11 , [NET\_OPT\_RECV\_PKTINFO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a) = 12 ,     [NET\_OPT\_MCAST\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e) = 13 , [NET\_OPT\_MCAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d) = 14 , [NET\_OPT\_UNICAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3) = 15 , [NET\_OPT\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184) = 16 ,     [NET\_OPT\_ADDR\_PREFERENCES](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d) = 17 , [NET\_OPT\_TIMESTAMPING](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2) = 18 , [NET\_OPT\_MCAST\_IFINDEX](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da98136d42db895cf6f3e35ee418e0b7eb) = 19 , [NET\_OPT\_MTU](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dad6b8627398a90dd622f433e8b3fee3a3) = 20 ,     [NET\_OPT\_LOCAL\_PORT\_RANGE](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da469d1d21e088eba6f96ec0a679636ba7) = 21   } |
|  | Network context options. [More...](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_context\_is\_used](group__net__context.md#ga423103d5c386b602737e23ee81f2a961) (struct [net\_context](structnet__context.md) \*context) |
|  | Is this context used or not. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_context\_is\_bound\_to\_iface](group__net__context.md#ga2f6d614158c999fa68e518393c0a9c35) (struct [net\_context](structnet__context.md) \*context) |
|  | Is this context bound to a network interface. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_context\_is\_accepting](group__net__context.md#ga26aa811e18a6808b6255713ac89c5773) (struct [net\_context](structnet__context.md) \*context) |
|  | Is this context is accepting data now. |
| static void | [net\_context\_set\_accepting](group__net__context.md#ga5fac6b26abfff86f29c087f6cddcceed) (struct [net\_context](structnet__context.md) \*context, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) accepting) |
|  | Set this context to accept data now. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_context\_is\_closing](group__net__context.md#gac8acf87f9b405df923a258c9f163e38b) (struct [net\_context](structnet__context.md) \*context) |
|  | Is this context closing. |
| static void | [net\_context\_set\_closing](group__net__context.md#ga9941aa201206448b6b34789d252f6385) (struct [net\_context](structnet__context.md) \*context, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) closing) |
|  | Set this context to closing. |
| static enum net\_context\_state | [net\_context\_get\_state](group__net__context.md#ga53bd5f35a142f1d43f90d3bde99778e0) (struct [net\_context](structnet__context.md) \*context) |
|  | Get state for this network context. |
| static void | [net\_context\_set\_state](group__net__context.md#gaac934209341db606a4d563b3c48cce45) (struct [net\_context](structnet__context.md) \*context, enum net\_context\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set state for this network context. |
| static [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | [net\_context\_get\_family](group__net__context.md#ga2c55e45a4ff4d4898766d7c391f63f3c) (struct [net\_context](structnet__context.md) \*context) |
|  | Get address family for this network context. |
| static void | [net\_context\_set\_family](group__net__context.md#ga6ef48a4b15c086167d44a8ed6a82478f) (struct [net\_context](structnet__context.md) \*context, [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family) |
|  | Set address family for this network context. |
| static enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) | [net\_context\_get\_type](group__net__context.md#ga24b4d99dddc4fabf383f5d8079650337) (struct [net\_context](structnet__context.md) \*context) |
|  | Get context type for this network context. |
| static void | [net\_context\_set\_type](group__net__context.md#ga01c11c1dfce101df046df9ade00ed277) (struct [net\_context](structnet__context.md) \*context, enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type) |
|  | Set context type for this network context. |
| static void | [net\_context\_set\_can\_filter\_id](group__net__context.md#ga581582c0461b36088d21d0fd433cc284) (struct [net\_context](structnet__context.md) \*context, int filter\_id) |
|  | Set CAN filter id for this network context. |
| static int | [net\_context\_get\_can\_filter\_id](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4) (struct [net\_context](structnet__context.md) \*context) |
|  | Get CAN filter id for this network context. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_context\_get\_proto](group__net__context.md#gadf41291ca5be067e830d121000ca3f51) (struct [net\_context](structnet__context.md) \*context) |
|  | Get context IP protocol for this network context. |
| static void | [net\_context\_set\_proto](group__net__context.md#gadcd0049229580244ea89fbc98bf23a81) (struct [net\_context](structnet__context.md) \*context, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) proto) |
|  | Set context IP protocol for this network context. |
| static struct [net\_if](structnet__if.md) \* | [net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087) (struct [net\_context](structnet__context.md) \*context) |
|  | Get network interface for this context. |
| static void | [net\_context\_set\_iface](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51) (struct [net\_context](structnet__context.md) \*context, struct [net\_if](structnet__if.md) \*iface) |
|  | Set network interface for this context. |
| static void | [net\_context\_bind\_iface](group__net__context.md#ga2f8fccd2453227706e313ac056f1c6ef) (struct [net\_context](structnet__context.md) \*context, struct [net\_if](structnet__if.md) \*iface) |
|  | Bind network interface to this context. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_context\_get\_ipv4\_ttl](group__net__context.md#ga9cdb3e5849a5b2663e0a38ac2a39a427) (struct [net\_context](structnet__context.md) \*context) |
|  | Get IPv4 TTL (time-to-live) value for this context. |
| static void | [net\_context\_set\_ipv4\_ttl](group__net__context.md#ga11672ca3ebdae63b0013ad76959304d5) (struct [net\_context](structnet__context.md) \*context, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl) |
|  | Set IPv4 TTL (time-to-live) value for this context. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_context\_get\_ipv4\_mcast\_ttl](group__net__context.md#ga3db832f40b6a0b975a282ef354a7bffc) (struct [net\_context](structnet__context.md) \*context) |
|  | Get IPv4 multicast TTL (time-to-live) value for this context. |
| static void | [net\_context\_set\_ipv4\_mcast\_ttl](group__net__context.md#gab2a2064fa33613a60ad40597d0971774) (struct [net\_context](structnet__context.md) \*context, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl) |
|  | Set IPv4 multicast TTL (time-to-live) value for this context. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_context\_get\_ipv6\_hop\_limit](group__net__context.md#ga977b08a77586e0e4752bff725139427c) (struct [net\_context](structnet__context.md) \*context) |
|  | Get IPv6 hop limit value for this context. |
| static void | [net\_context\_set\_ipv6\_hop\_limit](group__net__context.md#ga0cbf8377e7757881033aab3e718b1a61) (struct [net\_context](structnet__context.md) \*context, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit) |
|  | Set IPv6 hop limit value for this context. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_context\_get\_ipv6\_mcast\_hop\_limit](group__net__context.md#ga99b5f0ded5d56b735e051ede5651f435) (struct [net\_context](structnet__context.md) \*context) |
|  | Get IPv6 multicast hop limit value for this context. |
| static void | [net\_context\_set\_ipv6\_mcast\_hop\_limit](group__net__context.md#gaf29d5ee244c552d78171938a903fbaca) (struct [net\_context](structnet__context.md) \*context, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit) |
|  | Set IPv6 multicast hop limit value for this context. |
| static void | [net\_context\_set\_proxy\_enabled](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092) (struct [net\_context](structnet__context.md) \*context, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable or disable socks proxy support for this context. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_context\_is\_proxy\_enabled](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a) (struct [net\_context](structnet__context.md) \*context) |
|  | Is socks proxy support enabled or disabled for this context. |
| int | [net\_context\_get](group__net__context.md#gae21d27ce120ab72b58b1c20ec1d7ceff) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ip\_proto, struct [net\_context](structnet__context.md) \*\*context) |
|  | Get network context. |
| int | [net\_context\_put](group__net__context.md#ga1d6b64e302c546db589c661f4b6bda98) (struct [net\_context](structnet__context.md) \*context) |
|  | Close and unref a network context. |
| int | [net\_context\_ref](group__net__context.md#ga4c0ef9540a0d7e800c4529274f5c22f4) (struct [net\_context](structnet__context.md) \*context) |
|  | Take a reference count to a [net\_context](structnet__context.md "Note that we do not store the actual source IP address in the context because the address is already ..."), preventing destruction. |
| int | [net\_context\_unref](group__net__context.md#ga0d391690d9d6972ce6f4baedeab64b11) (struct [net\_context](structnet__context.md) \*context) |
|  | Decrement the reference count to a network context. |
| static int | [net\_context\_create\_ipv4\_new](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68) (struct [net\_context](structnet__context.md) \*context, struct [net\_pkt](structnet__pkt.md) \*pkt, const struct [in\_addr](structin__addr.md) \*src, const struct [in\_addr](structin__addr.md) \*dst) |
|  | Create IPv4 packet in provided [net\_pkt](structnet__pkt.md "Network packet.") from context. |
| static int | [net\_context\_create\_ipv6\_new](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a) (struct [net\_context](structnet__context.md) \*context, struct [net\_pkt](structnet__pkt.md) \*pkt, const struct [in6\_addr](structin6__addr.md) \*src, const struct [in6\_addr](structin6__addr.md) \*dst) |
|  | Create IPv6 packet in provided [net\_pkt](structnet__pkt.md "Network packet.") from context. |
| int | [net\_context\_bind](group__net__context.md#ga0fb749331a4f21148ca5a7f364f241b9) (struct [net\_context](structnet__context.md) \*context, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
|  | Assign a socket a local address. |
| int | [net\_context\_listen](group__net__context.md#ga3803c0d738fbb9d786f401aacc10a4d3) (struct [net\_context](structnet__context.md) \*context, int backlog) |
|  | Mark the context as a listening one. |
| int | [net\_context\_connect](group__net__context.md#ga56b2c5fc3f6a97664944cae1c1eb5dad) (struct [net\_context](structnet__context.md) \*context, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen, [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) cb, [k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Create a network connection. |
| int | [net\_context\_accept](group__net__context.md#ga1b056999d9ab8f2d3b3c0f4788f36cdd) (struct [net\_context](structnet__context.md) \*context, [net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8) cb, [k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Accept a network connection attempt. |
| int | [net\_context\_send](group__net__context.md#gac793e1def18200416e3f679067c56ab3) (struct [net\_context](structnet__context.md) \*context, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb, [k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Send data to a peer. |
| int | [net\_context\_sendto](group__net__context.md#gafb0230083b9bdc85c21752d9efb6fb10) (struct [net\_context](structnet__context.md) \*context, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const struct [sockaddr](structsockaddr.md) \*dst\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen, [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb, [k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Send data to a peer specified by address. |
| int | [net\_context\_sendmsg](group__net__context.md#ga437f04b1629542d2fcf43a15003dcac0) (struct [net\_context](structnet__context.md) \*context, const struct [msghdr](structmsghdr.md) \*[msghdr](structmsghdr.md), int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb, [k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Send data in iovec to a peer specified in msghdr struct. |
| int | [net\_context\_recv](group__net__context.md#ga74f919185f8af074c2d90aa04733dd2a) (struct [net\_context](structnet__context.md) \*context, [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) cb, [k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Receive network data from a peer specified by context. |
| int | [net\_context\_update\_recv\_wnd](group__net__context.md#gab3cc2a13e24f9c263bc40cc87d752a9f) (struct [net\_context](structnet__context.md) \*context, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) delta) |
|  | Update TCP receive window for context. |
| int | [net\_context\_set\_option](group__net__context.md#gabd932d5ded649f9a8c8bab40810e9eae) (struct [net\_context](structnet__context.md) \*context, enum [net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) option, const void \*value, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Set an connection option for this context. |
| int | [net\_context\_get\_option](group__net__context.md#gaeec55aee0a2029f8877a953ea137f39c) (struct [net\_context](structnet__context.md) \*context, enum [net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) option, void \*value, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*len) |
|  | Get connection option value for this context. |
| void | [net\_context\_foreach](group__net__context.md#gabb751f7d213d00f8eec72a67f4ce3491) ([net\_context\_cb\_t](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba) cb, void \*user\_data) |
|  | Go through all the network connections and call callback for each network context. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_context\_port\_in\_use](group__net__context.md#ga64c7442eeaa3ed82e54f50d2b30d67a0) (enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) ip\_proto, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) local\_port, const struct [sockaddr](structsockaddr.md) \*local\_addr) |
|  | Check if a port is in use (bound). |

## Detailed Description

Network context definitions.

An API for applications to define a network connection.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_context.h](net__context_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
