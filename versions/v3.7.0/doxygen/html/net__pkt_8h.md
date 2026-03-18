---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__pkt_8h.html
original_path: doxygen/html/net__pkt_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_pkt.h File Reference

Network packet buffer descriptor API.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/net/buf.h](net_2buf_8h_source.md)>`  
`#include <[zephyr/net/net_core.h](net__core_8h_source.md)>`  
`#include <[zephyr/net/net_linkaddr.h](net__linkaddr_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/net_context.h](net__context_8h_source.md)>`  
`#include <[zephyr/net/net_time.h](net__time_8h_source.md)>`  
`#include <[zephyr/net/ethernet_vlan.h](ethernet__vlan_8h_source.md)>`  
`#include <[zephyr/net/ptp_time.h](ptp__time_8h_source.md)>`

[Go to the source code of this file.](net__pkt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_pkt](structnet__pkt.md) |
|  | Network packet. [More...](structnet__pkt.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_PKT\_SLAB\_DEFINE](group__net__pkt.md#gafc7e98d5b64d816faabcbaa2ec22a2bb)(name, count) |
|  | Create a [net\_pkt](structnet__pkt.md "Network packet.") slab. |
| #define | [NET\_PKT\_DATA\_POOL\_DEFINE](group__net__pkt.md#ga94ab6300b59d739c4e3c5604d3fbe8a5)(name, count) |
|  | Create a data fragment [net\_buf](structnet__buf.md "Network buffer representation.") pool. |
| #define | [net\_pkt\_print\_frags](group__net__pkt.md#ga2b2d0900ae76674d418918ec955bad48)(pkt) |
|  | Print fragment list and the fragment sizes. |

| Functions | |
| --- | --- |
| struct [net\_buf](structnet__buf.md) \* | [net\_pkt\_get\_reserve\_data](group__net__pkt.md#ga6f697a97dd09e24663cbddc332ec5f7c) (struct [net\_buf\_pool](structnet__buf__pool.md) \*pool, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get a data buffer from a given pool. |
| struct [net\_buf](structnet__buf.md) \* | [net\_pkt\_get\_reserve\_rx\_data](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get RX DATA buffer from pool. |
| struct [net\_buf](structnet__buf.md) \* | [net\_pkt\_get\_reserve\_tx\_data](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get TX DATA buffer from pool. |
| struct [net\_buf](structnet__buf.md) \* | [net\_pkt\_get\_frag](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get a data fragment that might be from user specific buffer pool or from global DATA pool. |
| void | [net\_pkt\_unref](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Place packet back into the available packets slab. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_ref](group__net__pkt.md#ga4e83d4f60b46db8f57798c0e96d6cd7a) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Increase the packet ref count. |
| struct [net\_buf](structnet__buf.md) \* | [net\_pkt\_frag\_ref](group__net__pkt.md#gaea5e1045d188b3abbd85717ff09d563a) (struct [net\_buf](structnet__buf.md) \*frag) |
|  | Increase the packet fragment ref count. |
| void | [net\_pkt\_frag\_unref](group__net__pkt.md#ga5c75ef2149d2ba5ff07525988e0fb7cc) (struct [net\_buf](structnet__buf.md) \*frag) |
|  | Decrease the packet fragment ref count. |
| struct [net\_buf](structnet__buf.md) \* | [net\_pkt\_frag\_del](group__net__pkt.md#ga956c784f5417f0f79976c6e106ad0d76) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*parent, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Delete existing fragment from a packet. |
| void | [net\_pkt\_frag\_add](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Add a fragment to a packet at the end of its fragment list. |
| void | [net\_pkt\_frag\_insert](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Insert a fragment to a packet at the beginning of its fragment list. |
| void | [net\_pkt\_compact](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Compact the fragment list of a packet. |
| void | [net\_pkt\_get\_info](group__net__pkt.md#ga7b02b95838b928febfd4970de5e9c9f9) (struct k\_mem\_slab \*\*rx, struct k\_mem\_slab \*\*tx, struct [net\_buf\_pool](structnet__buf__pool.md) \*\*rx\_data, struct [net\_buf\_pool](structnet__buf__pool.md) \*\*tx\_data) |
|  | Get information about predefined RX, TX and DATA pools. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_alloc](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd) ([k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate an initialized [net\_pkt](structnet__pkt.md "Network packet."). |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_alloc\_from\_slab](group__net__pkt.md#gaf1edbaab59576262647089fa1751d9e3) (struct k\_mem\_slab \*slab, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate an initialized [net\_pkt](structnet__pkt.md "Network packet.") from a specific slab. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_rx\_alloc](group__net__pkt.md#ga4cec027a0de4807879fd3bd3aed4f12a) ([k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate an initialized [net\_pkt](structnet__pkt.md "Network packet.") for RX. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_alloc\_on\_iface](group__net__pkt.md#ga770ffe22fc797691b1fc89954d60b2e6) (struct [net\_if](structnet__if.md) \*iface, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a network packet for a specific network interface. |
| int | [net\_pkt\_alloc\_buffer](group__net__pkt.md#gae31b4afd510bce346f7d00a9ec5d190d) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate buffer for a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_alloc\_buffer\_raw](group__net__pkt.md#ga53819889ad86bc2c43407f12f113bb94) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate buffer for a [net\_pkt](structnet__pkt.md "Network packet."), of specified size, w/o any additional preconditions. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_alloc\_with\_buffer](group__net__pkt.md#ga57e2f5138acd92ad49864e3d709d9419) (struct [net\_if](structnet__if.md) \*iface, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a network packet and buffer at once. |
| void | [net\_pkt\_append\_buffer](group__net__pkt.md#ga2b11492ae3c16368aa6a0ab8f47b67e7) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*buffer) |
|  | Append a buffer in packet. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_pkt\_available\_buffer](group__net__pkt.md#gaeed119d192e3a14ea3eea6e623334519) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Get available buffer space from a pkt. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_pkt\_available\_payload\_buffer](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b) (struct [net\_pkt](structnet__pkt.md) \*pkt, enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto) |
|  | Get available buffer space for payload from a pkt. |
| void | [net\_pkt\_trim\_buffer](group__net__pkt.md#ga71d1c49f68afab07324cebd835f08a29) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Trim [net\_pkt](structnet__pkt.md "Network packet.") buffer. |
| int | [net\_pkt\_remove\_tail](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Remove *length* bytes from tail of packet. |
| void | [net\_pkt\_cursor\_init](group__net__pkt.md#ga1b7da39f62dfc8b8948d7689e2dd114a) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Initialize [net\_pkt](structnet__pkt.md "Network packet.") cursor. |
| static void | [net\_pkt\_cursor\_backup](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct net\_pkt\_cursor \*backup) |
|  | Backup [net\_pkt](structnet__pkt.md "Network packet.") cursor. |
| static void | [net\_pkt\_cursor\_restore](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct net\_pkt\_cursor \*backup) |
|  | Restore [net\_pkt](structnet__pkt.md "Network packet.") cursor from a backup. |
| static void \* | [net\_pkt\_cursor\_get\_pos](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Returns current position of the cursor. |
| int | [net\_pkt\_skip](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Skip some data from a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_memset](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f) (struct [net\_pkt](structnet__pkt.md) \*pkt, int byte, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Memset some data in a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_copy](group__net__pkt.md#ga4648828ca353c8c0ecf00ae2648e963a) (struct [net\_pkt](structnet__pkt.md) \*pkt\_dst, struct [net\_pkt](structnet__pkt.md) \*pkt\_src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Copy data from a packet into another one. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_clone](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959) (struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Clone pkt and its buffer. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_rx\_clone](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda) (struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Clone pkt and its buffer. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_shallow\_clone](group__net__pkt.md#ga26ae9d1286cb98d255f1bfb65201f1e2) (struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Clone pkt and increase the refcount of its buffer. |
| int | [net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64) (struct [net\_pkt](structnet__pkt.md) \*pkt, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Read some data from a [net\_pkt](structnet__pkt.md "Network packet."). |
| static int | [net\_pkt\_read\_u8](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Read a byte ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)) from a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_read\_be16](group__net__pkt.md#ga500a318977cfecd4ec7c60cea01db2fc) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data) |
|  | Read [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) big endian data from a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_read\_le16](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data) |
|  | Read [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) little endian data from a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_read\_be32](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data) |
|  | Read [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) big endian data from a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa) (struct [net\_pkt](structnet__pkt.md) \*pkt, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Write data into a [net\_pkt](structnet__pkt.md "Network packet."). |
| static int | [net\_pkt\_write\_u8](group__net__pkt.md#gaa5129f661075c13d9b59627ae9110bd1) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
|  | Write a byte ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)) data to a [net\_pkt](structnet__pkt.md "Network packet."). |
| static int | [net\_pkt\_write\_be16](group__net__pkt.md#ga8e5083388ccb0333fdcf745bc60ad260) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write a [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) big endian data to a [net\_pkt](structnet__pkt.md "Network packet."). |
| static int | [net\_pkt\_write\_be32](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write a [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) big endian data to a [net\_pkt](structnet__pkt.md "Network packet."). |
| static int | [net\_pkt\_write\_le32](group__net__pkt.md#gaf2388032e4e0b76fe32e4618ef3ea548) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write a [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) little endian data to a [net\_pkt](structnet__pkt.md "Network packet."). |
| static int | [net\_pkt\_write\_le16](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write a [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) little endian data to a [net\_pkt](structnet__pkt.md "Network packet."). |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_pkt\_remaining\_data](group__net__pkt.md#gadee5307216b6b3b725a2fd7584a224c9) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Get the amount of data which can be read from current cursor position. |
| int | [net\_pkt\_update\_length](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Update the overall length of a packet. |
| int | [net\_pkt\_pull](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Remove data from the packet at current location. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_pkt\_get\_current\_offset](group__net__pkt.md#gadb3b705a0431b3bb98fb2e8193c3b510) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Get the actual offset in the packet from its cursor. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_pkt\_is\_contiguous](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Check if a data size could fit contiguously. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_pkt\_get\_contiguous\_len](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Get the contiguous buffer space. |
| void \* | [net\_pkt\_get\_data](group__net__pkt.md#gaa00da4276fd4a01faf80a92796f78e70) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct net\_pkt\_data\_access \*access) |
|  | Get data from a network packet in a contiguous way. |
| int | [net\_pkt\_set\_data](group__net__pkt.md#ga98df84477b35e203b11029fc4ddec1cc) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct net\_pkt\_data\_access \*access) |
|  | Set contiguous data into a network packet. |
| static int | [net\_pkt\_acknowledge\_data](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct net\_pkt\_data\_access \*access) |
|  | Acknowledge previously contiguous data taken from a network packet Packet needs to be set to overwrite mode. |

## Detailed Description

Network packet buffer descriptor API.

Network data is passed between different parts of the stack via [net\_buf](structnet__buf.md "Network buffer representation.") struct.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_pkt.h](net__pkt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
