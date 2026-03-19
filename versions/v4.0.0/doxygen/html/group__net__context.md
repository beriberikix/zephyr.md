---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__net__context.html
original_path: doxygen/html/group__net__context.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Application network context

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Application network context.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_context](structnet__context.md) |
|  | Note that we do not store the actual source IP address in the context because the address is already set in the network interface struct. [More...](structnet__context.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_CONTEXT\_IN\_USE](#ga5e2f5fcc08863a4090bc04040ee88d29)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Is this context used or not. |
| #define | [NET\_CONTEXT\_FAMILY](#gac8f6e3a16d52e8e376c38eec0ed8a940)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5)) |
|  | The address family, connection type and IP protocol are stored into a bit field to save space. |
| #define | [NET\_CONTEXT\_TYPE](#gac9b4cf9beecaac5bf05db3111c803678)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7)) |
|  | Type of the connection (datagram / stream / raw). |
| #define | [NET\_CONTEXT\_REMOTE\_ADDR\_SET](#ga84206421e8f2e1eb114d393f0c81428b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Remote address set. |
| #define | [NET\_CONTEXT\_ACCEPTING\_SOCK](#gae4bfc7d561f99a5c50fa725496dfd69e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Is the socket accepting connections. |
| #define | [NET\_CONTEXT\_CLOSING\_SOCK](#ga90385e51999494c0d530c97b57a01865)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Is the socket closing / closed. |
| #define | [NET\_CONTEXT\_BOUND\_TO\_IFACE](#gaa337bccec2c1df42540f236bb33a70e1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Context is bound to a specific interface. |
| #define | [net\_context\_setup\_pools](#gadde93ce383a4c5b0f450db1eaa0dfd4d)(context, tx\_pool, data\_pool) |
|  | Set custom network buffer pools for context send operations. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [net\_context\_recv\_cb\_t](#gafa485a6fae8237dd7e6856f4567b2317)) (struct [net\_context](structnet__context.md) \*context, struct [net\_pkt](structnet__pkt.md) \*pkt, union net\_ip\_header \*ip\_hdr, union net\_proto\_header \*proto\_hdr, int status, void \*user\_data) |
|  | Network data receive callback. |
| typedef void(\* | [net\_context\_send\_cb\_t](#gab3caccfe9fa1bc7ce0e4654192a5de93)) (struct [net\_context](structnet__context.md) \*context, int status, void \*user\_data) |
|  | Network data send callback. |
| typedef void(\* | [net\_tcp\_accept\_cb\_t](#gabf7bcbd5b7beec6766b22e59a8ca73c8)) (struct [net\_context](structnet__context.md) \*new\_context, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen, int status, void \*user\_data) |
|  | Accept callback. |
| typedef void(\* | [net\_context\_connect\_cb\_t](#ga120ae8d4ff788ab21b19c11ed1738a71)) (struct [net\_context](structnet__context.md) \*context, int status, void \*user\_data) |
|  | Connection callback. |
| typedef struct k\_mem\_slab \*(\* | [net\_pkt\_get\_slab\_func\_t](#ga3bb4bbd522ede36213bafe86f2d1d770)) (void) |
|  | Function that is called to get the slab that is used for [net\_pkt](structnet__pkt.md "Network packet.") allocations. |
| typedef struct [net\_buf\_pool](structnet__buf__pool.md) \*(\* | [net\_pkt\_get\_pool\_func\_t](#gae3082af116955d4175c025a02b296c91)) (void) |
|  | Function that is called to get the pool that is used for [net\_buf](structnet__buf.md "Network buffer representation.") allocations. |
| typedef void(\* | [net\_context\_cb\_t](#gaa82d80fa18693b98dc363c35104075ba)) (struct [net\_context](structnet__context.md) \*context, void \*user\_data) |
|  | Callback used while iterating over network contexts. |

| Enumerations | |
| --- | --- |
| enum | [net\_context\_option](#gab03a354899ff68f6b9d127bc3bb5e17d) {     [NET\_OPT\_PRIORITY](#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c) = 1 , [NET\_OPT\_TXTIME](#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184) = 2 , [NET\_OPT\_SOCKS5](#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c) = 3 , [NET\_OPT\_RCVTIMEO](#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076) = 4 ,     [NET\_OPT\_SNDTIMEO](#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668) = 5 , [NET\_OPT\_RCVBUF](#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1) = 6 , [NET\_OPT\_SNDBUF](#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08) = 7 , [NET\_OPT\_DSCP\_ECN](#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c) = 8 ,     [NET\_OPT\_REUSEADDR](#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561) = 9 , [NET\_OPT\_REUSEPORT](#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4) = 10 , [NET\_OPT\_IPV6\_V6ONLY](#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c) = 11 , [NET\_OPT\_RECV\_PKTINFO](#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a) = 12 ,     [NET\_OPT\_MCAST\_TTL](#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e) = 13 , [NET\_OPT\_MCAST\_HOP\_LIMIT](#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d) = 14 , [NET\_OPT\_UNICAST\_HOP\_LIMIT](#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3) = 15 , [NET\_OPT\_TTL](#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184) = 16 ,     [NET\_OPT\_ADDR\_PREFERENCES](#ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d) = 17 , [NET\_OPT\_TIMESTAMPING](#ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2) = 18   } |
|  | Network context options. [More...](#gab03a354899ff68f6b9d127bc3bb5e17d) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_context\_is\_used](#ga423103d5c386b602737e23ee81f2a961) (struct [net\_context](structnet__context.md) \*context) |
|  | Is this context used or not. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_context\_is\_bound\_to\_iface](#ga2f6d614158c999fa68e518393c0a9c35) (struct [net\_context](structnet__context.md) \*context) |
|  | Is this context bound to a network interface. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_context\_is\_accepting](#ga26aa811e18a6808b6255713ac89c5773) (struct [net\_context](structnet__context.md) \*context) |
|  | Is this context is accepting data now. |
| static void | [net\_context\_set\_accepting](#ga5fac6b26abfff86f29c087f6cddcceed) (struct [net\_context](structnet__context.md) \*context, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) accepting) |
|  | Set this context to accept data now. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_context\_is\_closing](#gac8acf87f9b405df923a258c9f163e38b) (struct [net\_context](structnet__context.md) \*context) |
|  | Is this context closing. |
| static void | [net\_context\_set\_closing](#ga9941aa201206448b6b34789d252f6385) (struct [net\_context](structnet__context.md) \*context, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) closing) |
|  | Set this context to closing. |
| static enum net\_context\_state | [net\_context\_get\_state](#ga53bd5f35a142f1d43f90d3bde99778e0) (struct [net\_context](structnet__context.md) \*context) |
|  | Get state for this network context. |
| static void | [net\_context\_set\_state](#gaac934209341db606a4d563b3c48cce45) (struct [net\_context](structnet__context.md) \*context, enum net\_context\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set state for this network context. |
| static [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | [net\_context\_get\_family](#ga2c55e45a4ff4d4898766d7c391f63f3c) (struct [net\_context](structnet__context.md) \*context) |
|  | Get address family for this network context. |
| static void | [net\_context\_set\_family](#ga6ef48a4b15c086167d44a8ed6a82478f) (struct [net\_context](structnet__context.md) \*context, [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family) |
|  | Set address family for this network context. |
| static enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) | [net\_context\_get\_type](#ga24b4d99dddc4fabf383f5d8079650337) (struct [net\_context](structnet__context.md) \*context) |
|  | Get context type for this network context. |
| static void | [net\_context\_set\_type](#ga01c11c1dfce101df046df9ade00ed277) (struct [net\_context](structnet__context.md) \*context, enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type) |
|  | Set context type for this network context. |
| static void | [net\_context\_set\_can\_filter\_id](#ga581582c0461b36088d21d0fd433cc284) (struct [net\_context](structnet__context.md) \*context, int filter\_id) |
|  | Set CAN filter id for this network context. |
| static int | [net\_context\_get\_can\_filter\_id](#ga7f4d732a99cb9e86fcd5226fbbb727f4) (struct [net\_context](structnet__context.md) \*context) |
|  | Get CAN filter id for this network context. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_context\_get\_proto](#gadf41291ca5be067e830d121000ca3f51) (struct [net\_context](structnet__context.md) \*context) |
|  | Get context IP protocol for this network context. |
| static void | [net\_context\_set\_proto](#gadcd0049229580244ea89fbc98bf23a81) (struct [net\_context](structnet__context.md) \*context, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) proto) |
|  | Set context IP protocol for this network context. |
| static struct [net\_if](structnet__if.md) \* | [net\_context\_get\_iface](#gafe6b8c9af4464cd471285817d6d61087) (struct [net\_context](structnet__context.md) \*context) |
|  | Get network interface for this context. |
| static void | [net\_context\_set\_iface](#ga10399e3f3d159de9325ac7632ce25c51) (struct [net\_context](structnet__context.md) \*context, struct [net\_if](structnet__if.md) \*iface) |
|  | Set network interface for this context. |
| static void | [net\_context\_bind\_iface](#ga2f8fccd2453227706e313ac056f1c6ef) (struct [net\_context](structnet__context.md) \*context, struct [net\_if](structnet__if.md) \*iface) |
|  | Bind network interface to this context. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_context\_get\_ipv4\_ttl](#ga9cdb3e5849a5b2663e0a38ac2a39a427) (struct [net\_context](structnet__context.md) \*context) |
|  | Get IPv4 TTL (time-to-live) value for this context. |
| static void | [net\_context\_set\_ipv4\_ttl](#ga11672ca3ebdae63b0013ad76959304d5) (struct [net\_context](structnet__context.md) \*context, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl) |
|  | Set IPv4 TTL (time-to-live) value for this context. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_context\_get\_ipv4\_mcast\_ttl](#ga3db832f40b6a0b975a282ef354a7bffc) (struct [net\_context](structnet__context.md) \*context) |
|  | Get IPv4 multicast TTL (time-to-live) value for this context. |
| static void | [net\_context\_set\_ipv4\_mcast\_ttl](#gab2a2064fa33613a60ad40597d0971774) (struct [net\_context](structnet__context.md) \*context, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl) |
|  | Set IPv4 multicast TTL (time-to-live) value for this context. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_context\_get\_ipv6\_hop\_limit](#ga977b08a77586e0e4752bff725139427c) (struct [net\_context](structnet__context.md) \*context) |
|  | Get IPv6 hop limit value for this context. |
| static void | [net\_context\_set\_ipv6\_hop\_limit](#ga0cbf8377e7757881033aab3e718b1a61) (struct [net\_context](structnet__context.md) \*context, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit) |
|  | Set IPv6 hop limit value for this context. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_context\_get\_ipv6\_mcast\_hop\_limit](#ga99b5f0ded5d56b735e051ede5651f435) (struct [net\_context](structnet__context.md) \*context) |
|  | Get IPv6 multicast hop limit value for this context. |
| static void | [net\_context\_set\_ipv6\_mcast\_hop\_limit](#gaf29d5ee244c552d78171938a903fbaca) (struct [net\_context](structnet__context.md) \*context, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit) |
|  | Set IPv6 multicast hop limit value for this context. |
| static void | [net\_context\_set\_proxy\_enabled](#ga9bd6b5e9429b6e845d41f6cbf242c092) (struct [net\_context](structnet__context.md) \*context, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable or disable socks proxy support for this context. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_context\_is\_proxy\_enabled](#ga5c3a841ff54ddb53cedcccefde5a7d7a) (struct [net\_context](structnet__context.md) \*context) |
|  | Is socks proxy support enabled or disabled for this context. |
| int | [net\_context\_get](#gae21d27ce120ab72b58b1c20ec1d7ceff) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ip\_proto, struct [net\_context](structnet__context.md) \*\*context) |
|  | Get network context. |
| int | [net\_context\_put](#ga1d6b64e302c546db589c661f4b6bda98) (struct [net\_context](structnet__context.md) \*context) |
|  | Close and unref a network context. |
| int | [net\_context\_ref](#ga4c0ef9540a0d7e800c4529274f5c22f4) (struct [net\_context](structnet__context.md) \*context) |
|  | Take a reference count to a [net\_context](structnet__context.md "Note that we do not store the actual source IP address in the context because the address is already ..."), preventing destruction. |
| int | [net\_context\_unref](#ga0d391690d9d6972ce6f4baedeab64b11) (struct [net\_context](structnet__context.md) \*context) |
|  | Decrement the reference count to a network context. |
| static int | [net\_context\_create\_ipv4\_new](#ga742a09074bf286ac016f17bcbeb4ef68) (struct [net\_context](structnet__context.md) \*context, struct [net\_pkt](structnet__pkt.md) \*pkt, const struct [in\_addr](structin__addr.md) \*src, const struct [in\_addr](structin__addr.md) \*dst) |
|  | Create IPv4 packet in provided [net\_pkt](structnet__pkt.md "Network packet.") from context. |
| static int | [net\_context\_create\_ipv6\_new](#ga71263ea6e2788d67fa2ac77e309aba2a) (struct [net\_context](structnet__context.md) \*context, struct [net\_pkt](structnet__pkt.md) \*pkt, const struct [in6\_addr](structin6__addr.md) \*src, const struct [in6\_addr](structin6__addr.md) \*dst) |
|  | Create IPv6 packet in provided [net\_pkt](structnet__pkt.md "Network packet.") from context. |
| int | [net\_context\_bind](#ga0fb749331a4f21148ca5a7f364f241b9) (struct [net\_context](structnet__context.md) \*context, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
|  | Assign a socket a local address. |
| int | [net\_context\_listen](#ga3803c0d738fbb9d786f401aacc10a4d3) (struct [net\_context](structnet__context.md) \*context, int backlog) |
|  | Mark the context as a listening one. |
| int | [net\_context\_connect](#ga56b2c5fc3f6a97664944cae1c1eb5dad) (struct [net\_context](structnet__context.md) \*context, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen, [net\_context\_connect\_cb\_t](#ga120ae8d4ff788ab21b19c11ed1738a71) cb, [k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Create a network connection. |
| int | [net\_context\_accept](#ga1b056999d9ab8f2d3b3c0f4788f36cdd) (struct [net\_context](structnet__context.md) \*context, [net\_tcp\_accept\_cb\_t](#gabf7bcbd5b7beec6766b22e59a8ca73c8) cb, [k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Accept a network connection attempt. |
| int | [net\_context\_send](#gac793e1def18200416e3f679067c56ab3) (struct [net\_context](structnet__context.md) \*context, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [net\_context\_send\_cb\_t](#gab3caccfe9fa1bc7ce0e4654192a5de93) cb, [k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Send data to a peer. |
| int | [net\_context\_sendto](#gafb0230083b9bdc85c21752d9efb6fb10) (struct [net\_context](structnet__context.md) \*context, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const struct [sockaddr](structsockaddr.md) \*dst\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen, [net\_context\_send\_cb\_t](#gab3caccfe9fa1bc7ce0e4654192a5de93) cb, [k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Send data to a peer specified by address. |
| int | [net\_context\_sendmsg](#ga437f04b1629542d2fcf43a15003dcac0) (struct [net\_context](structnet__context.md) \*context, const struct [msghdr](structmsghdr.md) \*[msghdr](structmsghdr.md), int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [net\_context\_send\_cb\_t](#gab3caccfe9fa1bc7ce0e4654192a5de93) cb, [k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Send data in iovec to a peer specified in msghdr struct. |
| int | [net\_context\_recv](#ga74f919185f8af074c2d90aa04733dd2a) (struct [net\_context](structnet__context.md) \*context, [net\_context\_recv\_cb\_t](#gafa485a6fae8237dd7e6856f4567b2317) cb, [k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Receive network data from a peer specified by context. |
| int | [net\_context\_update\_recv\_wnd](#gab3cc2a13e24f9c263bc40cc87d752a9f) (struct [net\_context](structnet__context.md) \*context, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) delta) |
|  | Update TCP receive window for context. |
| int | [net\_context\_set\_option](#gabd932d5ded649f9a8c8bab40810e9eae) (struct [net\_context](structnet__context.md) \*context, enum [net\_context\_option](#gab03a354899ff68f6b9d127bc3bb5e17d) option, const void \*value, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Set an connection option for this context. |
| int | [net\_context\_get\_option](#gaeec55aee0a2029f8877a953ea137f39c) (struct [net\_context](structnet__context.md) \*context, enum [net\_context\_option](#gab03a354899ff68f6b9d127bc3bb5e17d) option, void \*value, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*len) |
|  | Get connection option value for this context. |
| void | [net\_context\_foreach](#gabb751f7d213d00f8eec72a67f4ce3491) ([net\_context\_cb\_t](#gaa82d80fa18693b98dc363c35104075ba) cb, void \*user\_data) |
|  | Go through all the network connections and call callback for each network context. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_context\_port\_in\_use](#ga64c7442eeaa3ed82e54f50d2b30d67a0) (enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) ip\_proto, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) local\_port, const struct [sockaddr](structsockaddr.md) \*local\_addr) |
|  | Check if a port is in use (bound). |

## Detailed Description

Application network context.

Since
:   1.0

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#gae4bfc7d561f99a5c50fa725496dfd69e)NET\_CONTEXT\_ACCEPTING\_SOCK

| #define NET\_CONTEXT\_ACCEPTING\_SOCK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Is the socket accepting connections.

## [◆ ](#gaa337bccec2c1df42540f236bb33a70e1)NET\_CONTEXT\_BOUND\_TO\_IFACE

| #define NET\_CONTEXT\_BOUND\_TO\_IFACE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Context is bound to a specific interface.

## [◆ ](#ga90385e51999494c0d530c97b57a01865)NET\_CONTEXT\_CLOSING\_SOCK

| #define NET\_CONTEXT\_CLOSING\_SOCK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Is the socket closing / closed.

## [◆ ](#gac8f6e3a16d52e8e376c38eec0ed8a940)NET\_CONTEXT\_FAMILY

| #define NET\_CONTEXT\_FAMILY   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5)) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

The address family, connection type and IP protocol are stored into a bit field to save space.

Protocol family of this connection

## [◆ ](#ga5e2f5fcc08863a4090bc04040ee88d29)NET\_CONTEXT\_IN\_USE

| #define NET\_CONTEXT\_IN\_USE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Is this context used or not.

## [◆ ](#ga84206421e8f2e1eb114d393f0c81428b)NET\_CONTEXT\_REMOTE\_ADDR\_SET

| #define NET\_CONTEXT\_REMOTE\_ADDR\_SET   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Remote address set.

## [◆ ](#gadde93ce383a4c5b0f450db1eaa0dfd4d)net\_context\_setup\_pools

| #define net\_context\_setup\_pools | ( |  | *context*, |
| --- | --- | --- | --- |
|  |  |  | *tx\_pool*, |
|  |  |  | *data\_pool* ) |

`#include <[net_context.h](net__context_8h.md)>`

Set custom network buffer pools for context send operations.

Set custom network buffer pools used by the IP stack to allocate network buffers used by the context when sending data to the network. Using dedicated buffers may help make send operations on a given context more reliable, e.g. not be subject to buffer starvation due to operations on other network contexts. Buffer pools are set per context, but several contexts may share the same buffers. Note that there's no support for per-context custom receive packet pools.

Parameters
:   | context | Context that will use the given [net\_buf](structnet__buf.md "Network buffer representation.") pools. |
    | --- | --- |
    | tx\_pool | Pointer to the function that will return TX pool to the caller. The TX pool is used when sending data to network. There is one TX [net\_pkt](structnet__pkt.md "Network packet.") for each network packet that is sent. |
    | data\_pool | Pointer to the function that will return DATA pool to the caller. The DATA pool is used to store data that is sent to the network. |

## [◆ ](#gac9b4cf9beecaac5bf05db3111c803678)NET\_CONTEXT\_TYPE

| #define NET\_CONTEXT\_TYPE   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7)) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Type of the connection (datagram / stream / raw).

## Typedef Documentation

## [◆ ](#gaa82d80fa18693b98dc363c35104075ba)net\_context\_cb\_t

| typedef void(\* net\_context\_cb\_t) (struct [net\_context](structnet__context.md) \*context, void \*user\_data) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Callback used while iterating over network contexts.

Parameters
:   | context | A valid pointer on current network context |
    | --- | --- |
    | user\_data | A valid pointer on some user data or NULL |

## [◆ ](#ga120ae8d4ff788ab21b19c11ed1738a71)net\_context\_connect\_cb\_t

| typedef void(\* net\_context\_connect\_cb\_t) (struct [net\_context](structnet__context.md) \*context, int status, void \*user\_data) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Connection callback.

The connect callback is called after a connection is being established. For TCP connections, this callback is called by RX thread so its stack and execution context is used here. The callback is called after the TCP connection was established or if the connection failed. Keep processing in the callback minimal to reduce the time spent blocked while handling packets. For UDP connections, this callback is called immediately by [net\_context\_connect()](#ga56b2c5fc3f6a97664944cae1c1eb5dad) function. UDP is a connectionless protocol so the connection can be thought of being established immediately.

Parameters
:   | context | The context to use. |
    | --- | --- |
    | status | Status of the connection establishment. This is 0 if the connection was established successfully, <0 if there was an error. |
    | user\_data | The user data given in [net\_context\_connect()](#ga56b2c5fc3f6a97664944cae1c1eb5dad) call. |

## [◆ ](#gafa485a6fae8237dd7e6856f4567b2317)net\_context\_recv\_cb\_t

| typedef void(\* net\_context\_recv\_cb\_t) (struct [net\_context](structnet__context.md) \*context, struct [net\_pkt](structnet__pkt.md) \*pkt, union net\_ip\_header \*ip\_hdr, union net\_proto\_header \*proto\_hdr, int status, void \*user\_data) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Network data receive callback.

The recv callback is called after a network data packet is received. This callback is called by RX thread so its stack and execution context is used here. Keep processing in the callback minimal to reduce the time spent blocked while handling packets.

Parameters
:   | context | The context to use. |
    | --- | --- |
    | pkt | Network buffer that is received. If the pkt is not NULL, then the callback will own the buffer and it needs to unref the pkt as soon as it has finished working with it. On EOF, pkt will be NULL. |
    | ip\_hdr | a pointer to relevant IP (v4 or v6) header. |
    | proto\_hdr | a pointer to relevant protocol (udp or tcp) header. |
    | status | Value is set to 0 if some data or the connection is at EOF, <0 if there was an error receiving data, in this case the pkt parameter is set to NULL. |
    | user\_data | The user data given in net\_recv() call. |

## [◆ ](#gab3caccfe9fa1bc7ce0e4654192a5de93)net\_context\_send\_cb\_t

| typedef void(\* net\_context\_send\_cb\_t) (struct [net\_context](structnet__context.md) \*context, int status, void \*user\_data) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Network data send callback.

The send callback is called after a network data packet is sent. This callback is called by TX thread so its stack and execution context is used here. Keep processing in the callback minimal to reduce the time spent blocked while handling packets.

Parameters
:   | context | The context to use. |
    | --- | --- |
    | status | Value is set to >= 0: amount of data that was sent, < 0 there was an error sending data. |
    | user\_data | The user data given in net\_send() call. |

## [◆ ](#gae3082af116955d4175c025a02b296c91)net\_pkt\_get\_pool\_func\_t

| typedef struct [net\_buf\_pool](structnet__buf__pool.md) \*(\* net\_pkt\_get\_pool\_func\_t) (void) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Function that is called to get the pool that is used for [net\_buf](structnet__buf.md "Network buffer representation.") allocations.

Returns
:   Pointer to valid struct [net\_buf\_pool](structnet__buf__pool.md "Network buffer pool representation.") instance.

## [◆ ](#ga3bb4bbd522ede36213bafe86f2d1d770)net\_pkt\_get\_slab\_func\_t

| typedef struct k\_mem\_slab \*(\* net\_pkt\_get\_slab\_func\_t) (void) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Function that is called to get the slab that is used for [net\_pkt](structnet__pkt.md "Network packet.") allocations.

Returns
:   Pointer to valid struct k\_mem\_slab instance.

## [◆ ](#gabf7bcbd5b7beec6766b22e59a8ca73c8)net\_tcp\_accept\_cb\_t

| typedef void(\* net\_tcp\_accept\_cb\_t) (struct [net\_context](structnet__context.md) \*new\_context, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen, int status, void \*user\_data) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Accept callback.

The accept callback is called after a successful connection was established or if there was an error while we were waiting for a connection attempt. This callback is called by RX thread so its stack and execution context is used here. Keep processing in the callback minimal to reduce the time spent blocked while handling packets.

Parameters
:   | new\_context | The context to use. |
    | --- | --- |
    | addr | The peer address. |
    | addrlen | Length of the peer address. |
    | status | The status code, 0 on success, < 0 otherwise |
    | user\_data | The user data given in [net\_context\_accept()](#ga1b056999d9ab8f2d3b3c0f4788f36cdd) call. |

## Enumeration Type Documentation

## [◆ ](#gab03a354899ff68f6b9d127bc3bb5e17d)net\_context\_option

| enum [net\_context\_option](#gab03a354899ff68f6b9d127bc3bb5e17d) |
| --- |

`#include <[net_context.h](net__context_8h.md)>`

Network context options.

These map to BSD socket option values.

| Enumerator | |
| --- | --- |
| NET\_OPT\_PRIORITY | Context priority. |
| NET\_OPT\_TXTIME | TX time. |
| NET\_OPT\_SOCKS5 | SOCKS5. |
| NET\_OPT\_RCVTIMEO | Receive timeout. |
| NET\_OPT\_SNDTIMEO | Send timeout. |
| NET\_OPT\_RCVBUF | Receive buffer. |
| NET\_OPT\_SNDBUF | Send buffer. |
| NET\_OPT\_DSCP\_ECN | DSCP ECN. |
| NET\_OPT\_REUSEADDR | Re-use address. |
| NET\_OPT\_REUSEPORT | Re-use port. |
| NET\_OPT\_IPV6\_V6ONLY | Share IPv4 and IPv6 port space. |
| NET\_OPT\_RECV\_PKTINFO | Receive packet information. |
| NET\_OPT\_MCAST\_TTL | IPv4 multicast TTL. |
| NET\_OPT\_MCAST\_HOP\_LIMIT | IPv6 multicast hop limit. |
| NET\_OPT\_UNICAST\_HOP\_LIMIT | IPv6 unicast hop limit. |
| NET\_OPT\_TTL | IPv4 unicast TTL. |
| NET\_OPT\_ADDR\_PREFERENCES | IPv6 address preference. |
| NET\_OPT\_TIMESTAMPING | Packet timestamping. |

## Function Documentation

## [◆ ](#ga1b056999d9ab8f2d3b3c0f4788f36cdd)net\_context\_accept()

| int net\_context\_accept | ( | struct [net\_context](structnet__context.md) \* | *context*, |
| --- | --- | --- | --- |
|  |  | [net\_tcp\_accept\_cb\_t](#gabf7bcbd5b7beec6766b22e59a8ca73c8) | *cb*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
|  |  | void \* | *user\_data* ) |

`#include <[net_context.h](net__context_8h.md)>`

Accept a network connection attempt.

Accept a connection being established. This function will return immediately if the timeout is set to K\_NO\_WAIT. In this case the context will call the supplied callback when ever there is a connection established to this context. This is "a register
handler and forget" type of call (async). If the timeout is set to K\_FOREVER, the function will wait until the connection is established. Timeout value > 0, will wait as many ms. After the connection is established a caller-supplied callback is called. The callback is called even if timeout was set to K\_FOREVER, the callback is called before this function will return in this case. The callback is not called if the timeout expires. This is similar as BSD [accept()](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb "POSIX wrapper for zsock_accept.") function.

Parameters
:   | context | The context to use. |
    | --- | --- |
    | cb | Caller-supplied callback function. |
    | timeout | Timeout for the connection. Possible values are K\_FOREVER, K\_NO\_WAIT, >0. |
    | user\_data | Caller-supplied user data. |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ga0fb749331a4f21148ca5a7f364f241b9)net\_context\_bind()

| int net\_context\_bind | ( | struct [net\_context](structnet__context.md) \* | *context*, |
| --- | --- | --- | --- |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen* ) |

`#include <[net_context.h](net__context_8h.md)>`

Assign a socket a local address.

This is similar as BSD [bind()](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9 "POSIX wrapper for zsock_bind.") function.

Parameters
:   | context | The context to be assigned. |
    | --- | --- |
    | addr | Address to assigned. |
    | addrlen | Length of the address. |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ga2f8fccd2453227706e313ac056f1c6ef)net\_context\_bind\_iface()

| | void net\_context\_bind\_iface | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | struct [net\_if](structnet__if.md) \* | *iface* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Bind network interface to this context.

This function binds network interface to this context.

Parameters
:   | context | Network context. |
    | --- | --- |
    | iface | Network interface. |

## [◆ ](#ga56b2c5fc3f6a97664944cae1c1eb5dad)net\_context\_connect()

| int net\_context\_connect | ( | struct [net\_context](structnet__context.md) \* | *context*, |
| --- | --- | --- | --- |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen*, |
|  |  | [net\_context\_connect\_cb\_t](#ga120ae8d4ff788ab21b19c11ed1738a71) | *cb*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
|  |  | void \* | *user\_data* ) |

`#include <[net_context.h](net__context_8h.md)>`

Create a network connection.

The net\_context\_connect function creates a network connection to the host specified by addr. After the connection is established, the user-supplied callback (cb) is executed. cb is called even if the timeout was set to K\_FOREVER. cb is not called if the timeout expires. For datagram sockets (SOCK\_DGRAM), this function only sets the peer address. This function is similar to the BSD [connect()](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386 "POSIX wrapper for zsock_connect.") function.

Parameters
:   | context | The network context. |
    | --- | --- |
    | addr | The peer address to connect to. |
    | addrlen | Peer address length. |
    | cb | Callback function. Set to NULL if not required. |
    | timeout | The timeout value for the connection. Possible values:  - K\_NO\_WAIT: this function will return immediately, - K\_FOREVER: this function will block until the connection is established, - >0: this function will wait the specified ms. |
    | user\_data | Data passed to the callback function. |

Returns
:   0 on success.
:   -EINVAL if an invalid parameter is passed as an argument.
:   -ENOTSUP if the operation is not supported or implemented.
:   -ETIMEDOUT if the connect operation times out.

## [◆ ](#ga742a09074bf286ac016f17bcbeb4ef68)net\_context\_create\_ipv4\_new()

| | int net\_context\_create\_ipv4\_new | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, | |  |  | const struct [in\_addr](structin__addr.md) \* | *src*, | |  |  | const struct [in\_addr](structin__addr.md) \* | *dst* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Create IPv4 packet in provided [net\_pkt](structnet__pkt.md "Network packet.") from context.

Parameters
:   | context | Network context for a connection |
    | --- | --- |
    | pkt | Network packet |
    | src | Source address, or NULL to choose a default |
    | dst | Destination IPv4 address |

Returns
:   Return 0 on success, negative errno otherwise.

## [◆ ](#ga71263ea6e2788d67fa2ac77e309aba2a)net\_context\_create\_ipv6\_new()

| | int net\_context\_create\_ipv6\_new | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, | |  |  | const struct [in6\_addr](structin6__addr.md) \* | *src*, | |  |  | const struct [in6\_addr](structin6__addr.md) \* | *dst* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Create IPv6 packet in provided [net\_pkt](structnet__pkt.md "Network packet.") from context.

Parameters
:   | context | Network context for a connection |
    | --- | --- |
    | pkt | Network packet |
    | src | Source address, or NULL to choose a default from context |
    | dst | Destination IPv6 address |

Returns
:   Return 0 on success, negative errno otherwise.

## [◆ ](#gabb751f7d213d00f8eec72a67f4ce3491)net\_context\_foreach()

| void net\_context\_foreach | ( | [net\_context\_cb\_t](#gaa82d80fa18693b98dc363c35104075ba) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[net_context.h](net__context_8h.md)>`

Go through all the network connections and call callback for each network context.

Parameters
:   | cb | User-supplied callback function to call. |
    | --- | --- |
    | user\_data | User specified data. |

## [◆ ](#gae21d27ce120ab72b58b1c20ec1d7ceff)net\_context\_get()

| int net\_context\_get | ( | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, |
| --- | --- | --- | --- |
|  |  | enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) | *type*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *ip\_proto*, |
|  |  | struct [net\_context](structnet__context.md) \*\* | *context* ) |

`#include <[net_context.h](net__context_8h.md)>`

Get network context.

Network context is used to define the connection 5-tuple (protocol, remote address, remote port, source address and source port). Random free port number will be assigned to source port when context is created. This is similar as BSD [socket()](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") function. The context will be created with a reference count of 1.

Parameters
:   | family | IP address family (AF\_INET or AF\_INET6) |
    | --- | --- |
    | type | Type of the socket, SOCK\_STREAM or SOCK\_DGRAM |
    | ip\_proto | IP protocol, IPPROTO\_UDP or IPPROTO\_TCP. For raw socket access, the value is the L2 protocol value from IEEE 802.3 (see [ethernet.h](ethernet_8h.md "Ethernet.")) |
    | context | The allocated context is returned to the caller. |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ga7f4d732a99cb9e86fcd5226fbbb727f4)net\_context\_get\_can\_filter\_id()

| | int net\_context\_get\_can\_filter\_id | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Get CAN filter id for this network context.

This function gets the CAN filter id of the context.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   Filter id of this network context

## [◆ ](#ga2c55e45a4ff4d4898766d7c391f63f3c)net\_context\_get\_family()

| | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) net\_context\_get\_family | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Get address family for this network context.

This function returns the address family (IPv4 or IPv6) of the context.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   Network state.

## [◆ ](#gafe6b8c9af4464cd471285817d6d61087)net\_context\_get\_iface()

| | struct [net\_if](structnet__if.md) \* net\_context\_get\_iface | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Get network interface for this context.

This function returns the used network interface.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   Context network interface if context is bind to interface, NULL otherwise.

## [◆ ](#ga3db832f40b6a0b975a282ef354a7bffc)net\_context\_get\_ipv4\_mcast\_ttl()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_context\_get\_ipv4\_mcast\_ttl | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Get IPv4 multicast TTL (time-to-live) value for this context.

This function returns the IPv4 multicast TTL (time-to-live) value that is set to this context.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   IPv4 multicast TTL value

## [◆ ](#ga9cdb3e5849a5b2663e0a38ac2a39a427)net\_context\_get\_ipv4\_ttl()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_context\_get\_ipv4\_ttl | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Get IPv4 TTL (time-to-live) value for this context.

This function returns the IPv4 TTL (time-to-live) value that is set to this context.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   IPv4 TTL value

## [◆ ](#ga977b08a77586e0e4752bff725139427c)net\_context\_get\_ipv6\_hop\_limit()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_context\_get\_ipv6\_hop\_limit | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Get IPv6 hop limit value for this context.

This function returns the IPv6 hop limit value that is set to this context.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   IPv6 hop limit value

## [◆ ](#ga99b5f0ded5d56b735e051ede5651f435)net\_context\_get\_ipv6\_mcast\_hop\_limit()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_context\_get\_ipv6\_mcast\_hop\_limit | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Get IPv6 multicast hop limit value for this context.

This function returns the IPv6 multicast hop limit value that is set to this context.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   IPv6 multicast hop limit value

## [◆ ](#gaeec55aee0a2029f8877a953ea137f39c)net\_context\_get\_option()

| int net\_context\_get\_option | ( | struct [net\_context](structnet__context.md) \* | *context*, |
| --- | --- | --- | --- |
|  |  | enum [net\_context\_option](#gab03a354899ff68f6b9d127bc3bb5e17d) | *option*, |
|  |  | void \* | *value*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *len* ) |

`#include <[net_context.h](net__context_8h.md)>`

Get connection option value for this context.

Parameters
:   | context | The network context to use. |
    | --- | --- |
    | option | Option to set |
    | value | Option value |
    | len | Option length (returned to caller) |

Returns
:   0 if ok, <0 if error

## [◆ ](#gadf41291ca5be067e830d121000ca3f51)net\_context\_get\_proto()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_context\_get\_proto | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Get context IP protocol for this network context.

This function returns the IP protocol (UDP / TCP / IEEE 802.3 protocol value) of the context.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   Network context IP protocol.

## [◆ ](#ga53bd5f35a142f1d43f90d3bde99778e0)net\_context\_get\_state()

| | enum net\_context\_state net\_context\_get\_state | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Get state for this network context.

This function returns the state of the context.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   Network state.

## [◆ ](#ga24b4d99dddc4fabf383f5d8079650337)net\_context\_get\_type()

| | enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) net\_context\_get\_type | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Get context type for this network context.

This function returns the context type (stream, datagram or raw) of the context.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   Network context type.

## [◆ ](#ga26aa811e18a6808b6255713ac89c5773)net\_context\_is\_accepting()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_context\_is\_accepting | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Is this context is accepting data now.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   True if the context is accepting connections, False otherwise.

## [◆ ](#ga2f6d614158c999fa68e518393c0a9c35)net\_context\_is\_bound\_to\_iface()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_context\_is\_bound\_to\_iface | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Is this context bound to a network interface.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   True if the context is bound to network interface, False otherwise.

## [◆ ](#gac8acf87f9b405df923a258c9f163e38b)net\_context\_is\_closing()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_context\_is\_closing | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Is this context closing.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   True if the context is closing, False otherwise.

## [◆ ](#ga5c3a841ff54ddb53cedcccefde5a7d7a)net\_context\_is\_proxy\_enabled()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_context\_is\_proxy\_enabled | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Is socks proxy support enabled or disabled for this context.

This function returns current socks proxy status for this context.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   True if socks proxy is enabled for this context, False otherwise

## [◆ ](#ga423103d5c386b602737e23ee81f2a961)net\_context\_is\_used()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_context\_is\_used | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Is this context used or not.

Parameters
:   | context | Network context. |
    | --- | --- |

Returns
:   True if the context is currently in use, False otherwise.

## [◆ ](#ga3803c0d738fbb9d786f401aacc10a4d3)net\_context\_listen()

| int net\_context\_listen | ( | struct [net\_context](structnet__context.md) \* | *context*, |
| --- | --- | --- | --- |
|  |  | int | *backlog* ) |

`#include <[net_context.h](net__context_8h.md)>`

Mark the context as a listening one.

This is similar as BSD [listen()](group__bsd__sockets.md#ga36f501240a9428fe2ae63a9540c97adb "POSIX wrapper for zsock_listen.") function.

Parameters
:   | context | The context to use. |
    | --- | --- |
    | backlog | The size of the pending connections backlog. |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ga64c7442eeaa3ed82e54f50d2b30d67a0)net\_context\_port\_in\_use()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_context\_port\_in\_use | ( | enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) | *ip\_proto*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *local\_port*, |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *local\_addr* ) |

`#include <[net_context.h](net__context_8h.md)>`

Check if a port is in use (bound).

This function checks if a port is bound with respect to the specified `ip_proto` and `local_addr`.

Parameters
:   | ip\_proto | the IP protocol |
    | --- | --- |
    | local\_port | the port to check |
    | local\_addr | the network address |

Returns
:   true if the port is bound
:   false if the port is not bound

## [◆ ](#ga1d6b64e302c546db589c661f4b6bda98)net\_context\_put()

| int net\_context\_put | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Close and unref a network context.

This releases the context. It is not possible to send or receive data via this context after this call. This is similar as BSD [shutdown()](group__bsd__sockets.md#gafe31a414f8777d15266fe84df7b66cbf "POSIX wrapper for zsock_shutdown.") function. For legacy compatibility, this function will implicitly decrement the reference count and possibly destroy the context either now or when it reaches a final state.

Parameters
:   | context | The context to be closed. |
    | --- | --- |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ga74f919185f8af074c2d90aa04733dd2a)net\_context\_recv()

| int net\_context\_recv | ( | struct [net\_context](structnet__context.md) \* | *context*, |
| --- | --- | --- | --- |
|  |  | [net\_context\_recv\_cb\_t](#gafa485a6fae8237dd7e6856f4567b2317) | *cb*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
|  |  | void \* | *user\_data* ) |

`#include <[net_context.h](net__context_8h.md)>`

Receive network data from a peer specified by context.

This function can be used to register a callback function that is called by the network stack when network data has been received for this context. As this function registers a callback, then there is no need to call this function multiple times if timeout is set to K\_NO\_WAIT. If callback function or user data changes, then the function can be called multiple times to register new values. This function will return immediately if the timeout is set to K\_NO\_WAIT. If the timeout is set to K\_FOREVER, the function will wait until the network buffer is received. Timeout value > 0 will wait as many ms. After the network buffer is received, a caller-supplied callback is called. The callback is called even if timeout was set to K\_FOREVER, the callback is called before this function will return in this case. The callback is not called if the timeout expires. The timeout functionality can be compiled out if synchronous behavior is not needed. The sync call logic requires some memory that can be saved if only async way of call is used. If CONFIG\_NET\_CONTEXT\_SYNC\_RECV is not set, then the timeout parameter value is ignored. This is similar as BSD [recv()](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40 "POSIX wrapper for zsock_recv.") function. Note that [net\_context\_bind()](#ga0fb749331a4f21148ca5a7f364f241b9) should be called before [net\_context\_recv()](#ga74f919185f8af074c2d90aa04733dd2a). Default random port number is assigned to local port. Only [bind()](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9 "POSIX wrapper for zsock_bind.") will update connection information from context. If [recv()](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40 "POSIX wrapper for zsock_recv.") is called before [bind()](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9 "POSIX wrapper for zsock_bind.") call, it may refuse to bind to a context which already has a connection associated.

Parameters
:   | context | The network context to use. |
    | --- | --- |
    | cb | Caller-supplied callback function. |
    | timeout | Caller-supplied timeout. Possible values are K\_FOREVER, K\_NO\_WAIT, >0. |
    | user\_data | Caller-supplied user data. |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ga4c0ef9540a0d7e800c4529274f5c22f4)net\_context\_ref()

| int net\_context\_ref | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Take a reference count to a [net\_context](structnet__context.md "Note that we do not store the actual source IP address in the context because the address is already ..."), preventing destruction.

Network contexts are not recycled until their reference count reaches zero. Note that this does not prevent any "close" behavior that results from errors or net\_context\_put. It simply prevents the context from being recycled for further use.

Parameters
:   | context | The context on which to increment the reference count |
    | --- | --- |

Returns
:   The new reference count

## [◆ ](#gac793e1def18200416e3f679067c56ab3)net\_context\_send()

| int net\_context\_send | ( | struct [net\_context](structnet__context.md) \* | *context*, |
| --- | --- | --- | --- |
|  |  | const void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [net\_context\_send\_cb\_t](#gab3caccfe9fa1bc7ce0e4654192a5de93) | *cb*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
|  |  | void \* | *user\_data* ) |

`#include <[net_context.h](net__context_8h.md)>`

Send data to a peer.

This function can be used to send network data to a peer connection. After the network buffer is sent, a caller-supplied callback is called. Note that the callback might be called after this function has returned. For context of type SOCK\_DGRAM, the destination address must have been set by the call to [net\_context\_connect()](#ga56b2c5fc3f6a97664944cae1c1eb5dad). This is similar as BSD [send()](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d "POSIX wrapper for zsock_send.") function.

Parameters
:   | context | The network context to use. |
    | --- | --- |
    | buf | The data buffer to send |
    | len | Length of the buffer |
    | cb | Caller-supplied callback function. |
    | timeout | Currently this value is not used. |
    | user\_data | Caller-supplied user data. |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ga437f04b1629542d2fcf43a15003dcac0)net\_context\_sendmsg()

| int net\_context\_sendmsg | ( | struct [net\_context](structnet__context.md) \* | *context*, |
| --- | --- | --- | --- |
|  |  | const struct [msghdr](structmsghdr.md) \* | *msghdr*, |
|  |  | int | *flags*, |
|  |  | [net\_context\_send\_cb\_t](#gab3caccfe9fa1bc7ce0e4654192a5de93) | *cb*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
|  |  | void \* | *user\_data* ) |

`#include <[net_context.h](net__context_8h.md)>`

Send data in iovec to a peer specified in msghdr struct.

This function has similar semantics as Posix [sendmsg()](group__bsd__sockets.md#ga1d7ee25c28352b2e7af55f75d721c4b8 "POSIX wrapper for zsock_sendmsg.") call. For unconnected socket, the msg\_name field in msghdr must be set. For connected socket the msg\_name should be set to NULL, and msg\_namelen to 0. After the network buffer is sent, a caller-supplied callback is called. Note that the callback might be called after this function has returned.

Parameters
:   | context | The network context to use. |
    | --- | --- |
    | [msghdr](structmsghdr.md "Message struct.") | The data to send |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags for the sending. |
    | cb | Caller-supplied callback function. |
    | timeout | Currently this value is not used. |
    | user\_data | Caller-supplied user data. |

Returns
:   numbers of bytes sent on success, a negative errno otherwise

## [◆ ](#gafb0230083b9bdc85c21752d9efb6fb10)net\_context\_sendto()

| int net\_context\_sendto | ( | struct [net\_context](structnet__context.md) \* | *context*, |
| --- | --- | --- | --- |
|  |  | const void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *dst\_addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen*, |
|  |  | [net\_context\_send\_cb\_t](#gab3caccfe9fa1bc7ce0e4654192a5de93) | *cb*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
|  |  | void \* | *user\_data* ) |

`#include <[net_context.h](net__context_8h.md)>`

Send data to a peer specified by address.

This function can be used to send network data to a peer specified by address. This variant can only be used for datagram connections of type SOCK\_DGRAM. After the network buffer is sent, a caller-supplied callback is called. Note that the callback might be called after this function has returned. This is similar as BSD [sendto()](group__bsd__sockets.md#gacdc42cdbe2f9480ed58a2bdc2af57035 "POSIX wrapper for zsock_sendto.") function.

Parameters
:   | context | The network context to use. |
    | --- | --- |
    | buf | The data buffer to send |
    | len | Length of the buffer |
    | dst\_addr | Destination address. |
    | addrlen | Length of the address. |
    | cb | Caller-supplied callback function. |
    | timeout | Currently this value is not used. |
    | user\_data | Caller-supplied user data. |

Returns
:   numbers of bytes sent on success, a negative errno otherwise

## [◆ ](#ga5fac6b26abfff86f29c087f6cddcceed)net\_context\_set\_accepting()

| | void net\_context\_set\_accepting | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *accepting* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Set this context to accept data now.

Parameters
:   | context | Network context. |
    | --- | --- |
    | accepting | True if accepting, False if not |

## [◆ ](#ga581582c0461b36088d21d0fd433cc284)net\_context\_set\_can\_filter\_id()

| | void net\_context\_set\_can\_filter\_id | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | int | *filter\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Set CAN filter id for this network context.

This function sets the CAN filter id of the context.

Parameters
:   | context | Network context. |
    | --- | --- |
    | filter\_id | CAN filter id |

## [◆ ](#ga9941aa201206448b6b34789d252f6385)net\_context\_set\_closing()

| | void net\_context\_set\_closing | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *closing* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Set this context to closing.

Parameters
:   | context | Network context. |
    | --- | --- |
    | closing | True if closing, False if not |

## [◆ ](#ga6ef48a4b15c086167d44a8ed6a82478f)net\_context\_set\_family()

| | void net\_context\_set\_family | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | *family* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Set address family for this network context.

This function sets the address family (IPv4, IPv6 or AF\_PACKET) of the context.

Parameters
:   | context | Network context. |
    | --- | --- |
    | family | Address family (AF\_INET, AF\_INET6, AF\_PACKET, AF\_CAN) |

## [◆ ](#ga10399e3f3d159de9325ac7632ce25c51)net\_context\_set\_iface()

| | void net\_context\_set\_iface | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | struct [net\_if](structnet__if.md) \* | *iface* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Set network interface for this context.

This function binds network interface to this context.

Parameters
:   | context | Network context. |
    | --- | --- |
    | iface | Network interface. |

## [◆ ](#gab2a2064fa33613a60ad40597d0971774)net\_context\_set\_ipv4\_mcast\_ttl()

| | void net\_context\_set\_ipv4\_mcast\_ttl | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ttl* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Set IPv4 multicast TTL (time-to-live) value for this context.

This function sets the IPv4 multicast TTL (time-to-live) value for this context.

Parameters
:   | context | Network context. |
    | --- | --- |
    | ttl | IPv4 multicast time-to-live value. |

## [◆ ](#ga11672ca3ebdae63b0013ad76959304d5)net\_context\_set\_ipv4\_ttl()

| | void net\_context\_set\_ipv4\_ttl | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ttl* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Set IPv4 TTL (time-to-live) value for this context.

This function sets the IPv4 TTL (time-to-live) value for this context.

Parameters
:   | context | Network context. |
    | --- | --- |
    | ttl | IPv4 time-to-live value. |

## [◆ ](#ga0cbf8377e7757881033aab3e718b1a61)net\_context\_set\_ipv6\_hop\_limit()

| | void net\_context\_set\_ipv6\_hop\_limit | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *hop\_limit* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Set IPv6 hop limit value for this context.

This function sets the IPv6 hop limit value for this context.

Parameters
:   | context | Network context. |
    | --- | --- |
    | hop\_limit | IPv6 hop limit value. |

## [◆ ](#gaf29d5ee244c552d78171938a903fbaca)net\_context\_set\_ipv6\_mcast\_hop\_limit()

| | void net\_context\_set\_ipv6\_mcast\_hop\_limit | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *hop\_limit* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Set IPv6 multicast hop limit value for this context.

This function sets the IPv6 multicast hop limit value for this context.

Parameters
:   | context | Network context. |
    | --- | --- |
    | hop\_limit | IPv6 multicast hop limit value. |

## [◆ ](#gabd932d5ded649f9a8c8bab40810e9eae)net\_context\_set\_option()

| int net\_context\_set\_option | ( | struct [net\_context](structnet__context.md) \* | *context*, |
| --- | --- | --- | --- |
|  |  | enum [net\_context\_option](#gab03a354899ff68f6b9d127bc3bb5e17d) | *option*, |
|  |  | const void \* | *value*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[net_context.h](net__context_8h.md)>`

Set an connection option for this context.

Parameters
:   | context | The network context to use. |
    | --- | --- |
    | option | Option to set |
    | value | Option value |
    | len | Option length |

Returns
:   0 if ok, <0 if error

## [◆ ](#gadcd0049229580244ea89fbc98bf23a81)net\_context\_set\_proto()

| | void net\_context\_set\_proto | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *proto* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Set context IP protocol for this network context.

This function sets the context IP protocol (UDP / TCP) of the context.

Parameters
:   | context | Network context. |
    | --- | --- |
    | proto | Context IP protocol (IPPROTO\_UDP, IPPROTO\_TCP or IEEE 802.3 protocol value) |

## [◆ ](#ga9bd6b5e9429b6e845d41f6cbf242c092)net\_context\_set\_proxy\_enabled()

| | void net\_context\_set\_proxy\_enabled | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Enable or disable socks proxy support for this context.

This function either enables or disables socks proxy support for this context.

Parameters
:   | context | Network context. |
    | --- | --- |
    | enable | Enable socks proxy or disable it. |

## [◆ ](#gaac934209341db606a4d563b3c48cce45)net\_context\_set\_state()

| | void net\_context\_set\_state | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | enum net\_context\_state | *state* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Set state for this network context.

This function sets the state of the context.

Parameters
:   | context | Network context. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | New network context state. |

## [◆ ](#ga01c11c1dfce101df046df9ade00ed277)net\_context\_set\_type()

| | void net\_context\_set\_type | ( | struct [net\_context](structnet__context.md) \* | *context*, | | --- | --- | --- | --- | |  |  | enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) | *type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Set context type for this network context.

This function sets the context type (stream or datagram) of the context.

Parameters
:   | context | Network context. |
    | --- | --- |
    | type | Context type (SOCK\_STREAM or SOCK\_DGRAM) |

## [◆ ](#ga0d391690d9d6972ce6f4baedeab64b11)net\_context\_unref()

| int net\_context\_unref | ( | struct [net\_context](structnet__context.md) \* | *context* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_context.h](net__context_8h.md)>`

Decrement the reference count to a network context.

Decrements the refcount. If it reaches zero, the context will be recycled. Note that this does not cause any network-visible "close" behavior (i.e. future packets to this connection may see TCP RST or ICMP port unreachable responses). See [net\_context\_put()](#ga1d6b64e302c546db589c661f4b6bda98) for that.

Parameters
:   | context | The context on which to decrement the reference count |
    | --- | --- |

Returns
:   The new reference count, zero if the context was destroyed

## [◆ ](#gab3cc2a13e24f9c263bc40cc87d752a9f)net\_context\_update\_recv\_wnd()

| int net\_context\_update\_recv\_wnd | ( | struct [net\_context](structnet__context.md) \* | *context*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *delta* ) |

`#include <[net_context.h](net__context_8h.md)>`

Update TCP receive window for context.

This function should be used by an application which doesn't fully process incoming data in its receive callback, but for example, queues it. In this case, receive callback should decrease the window (call this function with a negative value) by the size of queued data, and function(s) which dequeue data - with positive value corresponding to the dequeued size. For example, if receive callback gets a packet with the data size of 256 and queues it, it should call this function with delta of -256. If a function extracts 10 bytes of the queued data, it should call it with delta of 10.

Parameters
:   | context | The TCP network context to use. |
    | --- | --- |
    | delta | Size, in bytes, by which to increase TCP receive window (negative value to decrease). |

Returns
:   0 if ok, < 0 if error

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
