---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__net__pkt.html
original_path: doxygen/html/group__net__pkt.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Packet Library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network packet management library.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_pkt\_cursor](structnet__pkt__cursor.md) |
| struct | [net\_pkt](structnet__pkt.md) |
|  | Network packet. [More...](structnet__pkt.md#details) |
| struct | [net\_pkt\_data\_access](structnet__pkt__data__access.md) |

| Macros | |
| --- | --- |
| #define | [NET\_PKT\_SLAB\_DEFINE](#gafc7e98d5b64d816faabcbaa2ec22a2bb)(name, count) |
|  | Create a [net\_pkt](structnet__pkt.md "Network packet.") slab. |
| #define | [NET\_PKT\_TX\_SLAB\_DEFINE](#gacb3bb7347aa5dccb902531a1d6fbd190)(name, count) |
| #define | [NET\_PKT\_DATA\_POOL\_DEFINE](#ga94ab6300b59d739c4e3c5604d3fbe8a5)(name, count) |
|  | Create a data fragment [net\_buf](structnet__buf.md "Network buffer representation.") pool. |
| #define | [net\_pkt\_print\_frags](#ga2b2d0900ae76674d418918ec955bad48)(pkt) |
|  | Print fragment list and the fragment sizes. |
| #define | [NET\_PKT\_DATA\_ACCESS\_DEFINE](#gafd11f2d4f773bf247296eb08b7006c27)(\_name, \_type) |
| #define | [NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE](#gaa6a48974656755dcc0979683b8431c37)(\_name, \_type) |

| Functions | |
| --- | --- |
| struct [net\_buf](structnet__buf.md) \* | [net\_pkt\_get\_reserve\_rx\_data](#gaf48f4aac4d16a367d46ca76bf038a485) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get RX DATA buffer from pool. |
| struct [net\_buf](structnet__buf.md) \* | [net\_pkt\_get\_reserve\_tx\_data](#gaba26ee929f154978afbd007f7f2b0bc9) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get TX DATA buffer from pool. |
| struct [net\_buf](structnet__buf.md) \* | [net\_pkt\_get\_frag](#gafa7d666bddb182149d5f540880c46b4e) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get a data fragment that might be from user specific buffer pool or from global DATA pool. |
| void | [net\_pkt\_unref](#ga893d1660fd18ad5842224fda78466099) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Place packet back into the available packets slab. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_ref](#ga4e83d4f60b46db8f57798c0e96d6cd7a) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Increase the packet ref count. |
| struct [net\_buf](structnet__buf.md) \* | [net\_pkt\_frag\_ref](#gaea5e1045d188b3abbd85717ff09d563a) (struct [net\_buf](structnet__buf.md) \*frag) |
|  | Increase the packet fragment ref count. |
| void | [net\_pkt\_frag\_unref](#ga5c75ef2149d2ba5ff07525988e0fb7cc) (struct [net\_buf](structnet__buf.md) \*frag) |
|  | Decrease the packet fragment ref count. |
| struct [net\_buf](structnet__buf.md) \* | [net\_pkt\_frag\_del](#ga956c784f5417f0f79976c6e106ad0d76) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*parent, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Delete existing fragment from a packet. |
| void | [net\_pkt\_frag\_add](#ga03a53365cfc2b6c3448763d81f56c2c0) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Add a fragment to a packet at the end of its fragment list. |
| void | [net\_pkt\_frag\_insert](#gabcd375d9dbdca21855abe27d7b5a0a7e) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Insert a fragment to a packet at the beginning of its fragment list. |
| void | [net\_pkt\_compact](#gabf85446fb8000574b180d00c5db65a44) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Compact the fragment list of a packet. |
| void | [net\_pkt\_get\_info](#ga7b02b95838b928febfd4970de5e9c9f9) (struct k\_mem\_slab \*\*rx, struct k\_mem\_slab \*\*tx, struct [net\_buf\_pool](structnet__buf__pool.md) \*\*rx\_data, struct [net\_buf\_pool](structnet__buf__pool.md) \*\*tx\_data) |
|  | Get information about predefined RX, TX and DATA pools. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_alloc](#ga90d97ba913a875b3ee438e0ea8a970fd) ([k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate an initialized [net\_pkt](structnet__pkt.md "Network packet."). |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_alloc\_from\_slab](#gaf1edbaab59576262647089fa1751d9e3) (struct k\_mem\_slab \*slab, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate an initialized [net\_pkt](structnet__pkt.md "Network packet.") from a specific slab. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_rx\_alloc](#ga4cec027a0de4807879fd3bd3aed4f12a) ([k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate an initialized [net\_pkt](structnet__pkt.md "Network packet.") for RX. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_alloc\_on\_iface](#ga770ffe22fc797691b1fc89954d60b2e6) (struct [net\_if](structnet__if.md) \*iface, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a network packet for a specific network interface. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_rx\_alloc\_on\_iface](#gab64f7551b1995c301232ab4cd39b9efc) (struct [net\_if](structnet__if.md) \*iface, [k\_timeout\_t](structk__timeout__t.md) timeout) |
| int | [net\_pkt\_alloc\_buffer](#gae31b4afd510bce346f7d00a9ec5d190d) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate buffer for a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_alloc\_buffer\_raw](#ga53819889ad86bc2c43407f12f113bb94) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate buffer for a [net\_pkt](structnet__pkt.md "Network packet."), of specified size, w/o any additional preconditions. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_alloc\_with\_buffer](#ga57e2f5138acd92ad49864e3d709d9419) (struct [net\_if](structnet__if.md) \*iface, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a network packet and buffer at once. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_rx\_alloc\_with\_buffer](#ga623794964a35e0e24c1f41a75bfba626) (struct [net\_if](structnet__if.md) \*iface, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto, [k\_timeout\_t](structk__timeout__t.md) timeout) |
| void | [net\_pkt\_append\_buffer](#ga2b11492ae3c16368aa6a0ab8f47b67e7) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*buffer) |
|  | Append a buffer in packet. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_pkt\_available\_buffer](#gaeed119d192e3a14ea3eea6e623334519) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Get available buffer space from a pkt. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_pkt\_available\_payload\_buffer](#gaa9f63047b7945a4a155e5d88eac5203b) (struct [net\_pkt](structnet__pkt.md) \*pkt, enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto) |
|  | Get available buffer space for payload from a pkt. |
| void | [net\_pkt\_trim\_buffer](#ga71d1c49f68afab07324cebd835f08a29) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Trim [net\_pkt](structnet__pkt.md "Network packet.") buffer. |
| int | [net\_pkt\_remove\_tail](#gab657c80669733a4afefaf1be6310107e) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Remove *length* bytes from tail of packet. |
| void | [net\_pkt\_cursor\_init](#ga1b7da39f62dfc8b8948d7689e2dd114a) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Initialize [net\_pkt](structnet__pkt.md "Network packet.") cursor. |
| static void | [net\_pkt\_cursor\_backup](#gabd352b66cdeaff2fb45361a0fae62876) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_pkt\_cursor](structnet__pkt__cursor.md) \*backup) |
|  | Backup [net\_pkt](structnet__pkt.md "Network packet.") cursor. |
| static void | [net\_pkt\_cursor\_restore](#gad5ab788f01b4bb3640755e8c4a2c612e) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_pkt\_cursor](structnet__pkt__cursor.md) \*backup) |
|  | Restore [net\_pkt](structnet__pkt.md "Network packet.") cursor from a backup. |
| static void \* | [net\_pkt\_cursor\_get\_pos](#gabc42ba1bcd0801a116651d965e65b9cd) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Returns current position of the cursor. |
| int | [net\_pkt\_skip](#ga223a79baa1e740a53c4ed0f083d62185) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Skip some data from a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_memset](#gabd241a539bf1290f3d45610fd15b2c1f) (struct [net\_pkt](structnet__pkt.md) \*pkt, int byte, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Memset some data in a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_copy](#ga4648828ca353c8c0ecf00ae2648e963a) (struct [net\_pkt](structnet__pkt.md) \*pkt\_dst, struct [net\_pkt](structnet__pkt.md) \*pkt\_src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Copy data from a packet into another one. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_clone](#gaefefe50d0c68fb4997abc7b309740959) (struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Clone pkt and its buffer. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_rx\_clone](#ga66aec729118e4d927c921b872df82dda) (struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Clone pkt and its buffer. |
| struct [net\_pkt](structnet__pkt.md) \* | [net\_pkt\_shallow\_clone](#ga26ae9d1286cb98d255f1bfb65201f1e2) (struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Clone pkt and increase the refcount of its buffer. |
| int | [net\_pkt\_read](#ga914be010ddd225a4fc2d6ab521ee7b64) (struct [net\_pkt](structnet__pkt.md) \*pkt, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Read some data from a [net\_pkt](structnet__pkt.md "Network packet."). |
| static int | [net\_pkt\_read\_u8](#gaf9b2753cb514804a77d9494c9f070089) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
| int | [net\_pkt\_read\_be16](#ga500a318977cfecd4ec7c60cea01db2fc) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data) |
|  | Read [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) big endian data from a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_read\_le16](#gab1735ef4f6a2e538a2692358295dd8d1) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data) |
|  | Read [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) little endian data from a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_read\_be32](#gab38c99947d02982073df65c0d5893d2c) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data) |
|  | Read [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) big endian data from a [net\_pkt](structnet__pkt.md "Network packet."). |
| int | [net\_pkt\_write](#gae99eadd977b7f66ecc91d2ccba34c6fa) (struct [net\_pkt](structnet__pkt.md) \*pkt, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Write data into a [net\_pkt](structnet__pkt.md "Network packet."). |
| static int | [net\_pkt\_write\_u8](#gaa5129f661075c13d9b59627ae9110bd1) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
| static int | [net\_pkt\_write\_be16](#ga8e5083388ccb0333fdcf745bc60ad260) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
| static int | [net\_pkt\_write\_be32](#ga053aff4ff0a501f336132c35b7fb2022) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
| static int | [net\_pkt\_write\_le32](#gaf2388032e4e0b76fe32e4618ef3ea548) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
| static int | [net\_pkt\_write\_le16](#gac8a6ea1b0dc1bcd7b6a3f15869027dd1) (struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_pkt\_remaining\_data](#gadee5307216b6b3b725a2fd7584a224c9) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Get the amount of data which can be read from current cursor position. |
| int | [net\_pkt\_update\_length](#ga2e7a0f9348a623c5160124da188445ee) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Update the overall length of a packet. |
| int | [net\_pkt\_pull](#ga434c347a32600ee113c0e1cc13f70cd4) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Remove data from the packet at current location. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_pkt\_get\_current\_offset](#gadb3b705a0431b3bb98fb2e8193c3b510) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Get the actual offset in the packet from its cursor. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_pkt\_is\_contiguous](#gaf4ee5a8903b495e000a3a4c8a8493160) (struct [net\_pkt](structnet__pkt.md) \*pkt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Check if a data size could fit contiguously. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_pkt\_get\_contiguous\_len](#gafbd6c0ab33139b134f67a8f8c0096445) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Get the contiguous buffer space. |
| void \* | [net\_pkt\_get\_data](#gaa00da4276fd4a01faf80a92796f78e70) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_pkt\_data\_access](structnet__pkt__data__access.md) \*access) |
|  | Get data from a network packet in a contiguous way. |
| int | [net\_pkt\_set\_data](#ga98df84477b35e203b11029fc4ddec1cc) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_pkt\_data\_access](structnet__pkt__data__access.md) \*access) |
|  | Set contiguous data into a network packet. |
| static int | [net\_pkt\_acknowledge\_data](#gac7226cbfa2da28408f9691d375bc8f9f) (struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_pkt\_data\_access](structnet__pkt__data__access.md) \*access) |
|  | Acknowledge previously contiguous data taken from a network packet Packet needs to be set to overwrite mode. |

## Detailed Description

Network packet management library.

## Macro Definition Documentation

## [◆ ](#gaa6a48974656755dcc0979683b8431c37)NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE

| #define NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_type* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

**Value:**

struct [net\_pkt\_data\_access](structnet__pkt__data__access.md) \_name = { \

.data = NULL, \

.size = sizeof(\_type), \

}

[net\_pkt\_data\_access](structnet__pkt__data__access.md)

**Definition** net\_pkt.h:2267

## [◆ ](#gafd11f2d4f773bf247296eb08b7006c27)NET\_PKT\_DATA\_ACCESS\_DEFINE

| #define NET\_PKT\_DATA\_ACCESS\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_type* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

**Value:**

\_type \_hdr\_##\_name; \

struct [net\_pkt\_data\_access](structnet__pkt__data__access.md) \_name = { \

.data = &\_hdr\_##\_name, \

.[size](structnet__pkt__data__access.md#a8638004d4629eff48f85f61900c04034) = sizeof(\_type), \

}

[net\_pkt\_data\_access::size](structnet__pkt__data__access.md#a8638004d4629eff48f85f61900c04034)

const size\_t size

**Definition** net\_pkt.h:2271

## [◆ ](#ga94ab6300b59d739c4e3c5604d3fbe8a5)NET\_PKT\_DATA\_POOL\_DEFINE

| #define NET\_PKT\_DATA\_POOL\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *count* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

**Value:**

[NET\_BUF\_POOL\_DEFINE](group__net__buf.md#ga810aba8ba321fd012edc238ea9fe19dc)(name, count, CONFIG\_NET\_BUF\_DATA\_SIZE, \

0, NULL)

[NET\_BUF\_POOL\_DEFINE](group__net__buf.md#ga810aba8ba321fd012edc238ea9fe19dc)

#define NET\_BUF\_POOL\_DEFINE(\_name, \_count, \_size, \_ud\_size, \_destroy)

Define a new pool for buffers.

**Definition** buf.h:1195

Create a data fragment [net\_buf](structnet__buf.md "Network buffer representation.") pool.

A [net\_buf](structnet__buf.md "Network buffer representation.") pool is used to store actual data for network packets. It must be coupled with a [net\_pkt](structnet__pkt.md "Network packet.") slab ([NET\_PKT\_SLAB\_DEFINE](#gafc7e98d5b64d816faabcbaa2ec22a2bb)) used to store the packet meta-information. The macro can be used by an application to define additional custom per-context TX packet pools (see [net\_context\_setup\_pools()](group__net__context.md#gadde93ce383a4c5b0f450db1eaa0dfd4d "Set custom network buffer pools for context send operations.")).

Parameters
:   | name | Name of the pool. |
    | --- | --- |
    | count | Number of [net\_buf](structnet__buf.md "Network buffer representation.") in this pool. |

## [◆ ](#ga2b2d0900ae76674d418918ec955bad48)net\_pkt\_print\_frags

| #define net\_pkt\_print\_frags | ( |  | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Print fragment list and the fragment sizes.

Only available if debugging is activated.

Parameters
:   | pkt | Network pkt. |
    | --- | --- |

## [◆ ](#gafc7e98d5b64d816faabcbaa2ec22a2bb)NET\_PKT\_SLAB\_DEFINE

| #define NET\_PKT\_SLAB\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *count* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

**Value:**

[K\_MEM\_SLAB\_DEFINE](group__mem__slab__apis.md#ga60bc92eee58fcc5f121b8e4d82eaa69e)(name, sizeof(struct [net\_pkt](structnet__pkt.md)), count, 4)

[K\_MEM\_SLAB\_DEFINE](group__mem__slab__apis.md#ga60bc92eee58fcc5f121b8e4d82eaa69e)

#define K\_MEM\_SLAB\_DEFINE(name, slab\_block\_size, slab\_num\_blocks, slab\_align)

Statically define and initialize a memory slab in a public (non-static) scope.

**Definition** kernel.h:5121

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

Create a [net\_pkt](structnet__pkt.md "Network packet.") slab.

A [net\_pkt](structnet__pkt.md "Network packet.") slab is used to store meta-information about network packets. It must be coupled with a data fragment pool ([NET\_PKT\_DATA\_POOL\_DEFINE](#ga94ab6300b59d739c4e3c5604d3fbe8a5)) used to store the actual packet data. The macro can be used by an application to define additional custom per-context TX packet slabs (see [net\_context\_setup\_pools()](group__net__context.md#gadde93ce383a4c5b0f450db1eaa0dfd4d "Set custom network buffer pools for context send operations.")).

Parameters
:   | name | Name of the slab. |
    | --- | --- |
    | count | Number of [net\_pkt](structnet__pkt.md "Network packet.") in this slab. |

## [◆ ](#gacb3bb7347aa5dccb902531a1d6fbd190)NET\_PKT\_TX\_SLAB\_DEFINE

| #define NET\_PKT\_TX\_SLAB\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *count* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

**Value:**

[NET\_PKT\_SLAB\_DEFINE](#gafc7e98d5b64d816faabcbaa2ec22a2bb)(name, count)

[NET\_PKT\_SLAB\_DEFINE](#gafc7e98d5b64d816faabcbaa2ec22a2bb)

#define NET\_PKT\_SLAB\_DEFINE(name, count)

Create a net\_pkt slab.

**Definition** net\_pkt.h:1373

## Function Documentation

## [◆ ](#gac7226cbfa2da28408f9691d375bc8f9f)net\_pkt\_acknowledge\_data()

| | int net\_pkt\_acknowledge\_data | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, | | --- | --- | --- | --- | |  |  | struct [net\_pkt\_data\_access](structnet__pkt__data__access.md) \* | *access* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Acknowledge previously contiguous data taken from a network packet Packet needs to be set to overwrite mode.

## [◆ ](#ga90d97ba913a875b3ee438e0ea8a970fd)net\_pkt\_alloc()

| struct [net\_pkt](structnet__pkt.md) \* net\_pkt\_alloc | ( | [k\_timeout\_t](structk__timeout__t.md) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Allocate an initialized [net\_pkt](structnet__pkt.md "Network packet.").

for the time being, 2 pools are used. One for TX and one for RX. This allocator has to be used for TX.

Parameters
:   | timeout | Maximum time to wait for an allocation. |
    | --- | --- |

Returns
:   a pointer to a newly allocated [net\_pkt](structnet__pkt.md "Network packet.") on success, NULL otherwise.

## [◆ ](#gae31b4afd510bce346f7d00a9ec5d190d)net\_pkt\_alloc\_buffer()

| int net\_pkt\_alloc\_buffer | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) | *proto*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Allocate buffer for a [net\_pkt](structnet__pkt.md "Network packet.").

: such allocator will take into account space necessary for headers, MTU, and existing buffer (if any). Beware that, due to all these criteria, the allocated size might be smaller/bigger than requested one.

Parameters
:   | pkt | The network packet requiring buffer to be allocated. |
    | --- | --- |
    | size | The size of buffer being requested. |
    | proto | The IP protocol type (can be 0 for none). |
    | timeout | Maximum time to wait for an allocation. |

Returns
:   0 on success, negative errno code otherwise.

## [◆ ](#ga53819889ad86bc2c43407f12f113bb94)net\_pkt\_alloc\_buffer\_raw()

| int net\_pkt\_alloc\_buffer\_raw | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Allocate buffer for a [net\_pkt](structnet__pkt.md "Network packet."), of specified size, w/o any additional preconditions.

: The actual buffer size may be larger than requested one if fixed size buffers are in use.

Parameters
:   | pkt | The network packet requiring buffer to be allocated. |
    | --- | --- |
    | size | The size of buffer being requested. |
    | timeout | Maximum time to wait for an allocation. |

Returns
:   0 on success, negative errno code otherwise.

## [◆ ](#gaf1edbaab59576262647089fa1751d9e3)net\_pkt\_alloc\_from\_slab()

| struct [net\_pkt](structnet__pkt.md) \* net\_pkt\_alloc\_from\_slab | ( | struct k\_mem\_slab \* | *slab*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Allocate an initialized [net\_pkt](structnet__pkt.md "Network packet.") from a specific slab.

unlike [net\_pkt\_alloc()](#ga90d97ba913a875b3ee438e0ea8a970fd) which uses core slabs, this one will use an external slab (see [NET\_PKT\_SLAB\_DEFINE()](#gafc7e98d5b64d816faabcbaa2ec22a2bb)). Do *not* use it unless you know what you are doing. Basically, only [net\_context](structnet__context.md "Note that we do not store the actual source IP address in the context because the address is already ...") should be using this, in order to allocate packet and then buffer on its local slab/pool (if any).

Parameters
:   | slab | The slab to use for allocating the packet |
    | --- | --- |
    | timeout | Maximum time to wait for an allocation. |

Returns
:   a pointer to a newly allocated [net\_pkt](structnet__pkt.md "Network packet.") on success, NULL otherwise.

## [◆ ](#ga770ffe22fc797691b1fc89954d60b2e6)net\_pkt\_alloc\_on\_iface()

| struct [net\_pkt](structnet__pkt.md) \* net\_pkt\_alloc\_on\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Allocate a network packet for a specific network interface.

Parameters
:   | iface | The network interface the packet is supposed to go through. |
    | --- | --- |
    | timeout | Maximum time to wait for an allocation. |

Returns
:   a pointer to a newly allocated [net\_pkt](structnet__pkt.md "Network packet.") on success, NULL otherwise.

## [◆ ](#ga57e2f5138acd92ad49864e3d709d9419)net\_pkt\_alloc\_with\_buffer()

| struct [net\_pkt](structnet__pkt.md) \* net\_pkt\_alloc\_with\_buffer | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, |
|  |  | enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) | *proto*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Allocate a network packet and buffer at once.

Parameters
:   | iface | The network interface the packet is supposed to go through. |
    | --- | --- |
    | size | The size of buffer. |
    | family | The family to which the packet belongs. |
    | proto | The IP protocol type (can be 0 for none). |
    | timeout | Maximum time to wait for an allocation. |

Returns
:   a pointer to a newly allocated [net\_pkt](structnet__pkt.md "Network packet.") on success, NULL otherwise.

## [◆ ](#ga2b11492ae3c16368aa6a0ab8f47b67e7)net\_pkt\_append\_buffer()

| void net\_pkt\_append\_buffer | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buffer* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Append a buffer in packet.

Parameters
:   | pkt | Network packet where to append the buffer |
    | --- | --- |
    | buffer | Buffer to append |

## [◆ ](#gaeed119d192e3a14ea3eea6e623334519)net\_pkt\_available\_buffer()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_pkt\_available\_buffer | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Get available buffer space from a pkt.

Note
:   Reserved bytes (headroom) in any of the fragments are not considered to be available.

Parameters
:   | pkt | The [net\_pkt](structnet__pkt.md "Network packet.") which buffer availability should be evaluated |
    | --- | --- |

Returns
:   the amount of buffer available

## [◆ ](#gaa9f63047b7945a4a155e5d88eac5203b)net\_pkt\_available\_payload\_buffer()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_pkt\_available\_payload\_buffer | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) | *proto* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Get available buffer space for payload from a pkt.

Note
:   Reserved bytes (headroom) in any of the fragments are not considered to be available.

Unlike [net\_pkt\_available\_buffer()](#gaeed119d192e3a14ea3eea6e623334519), this will take into account the headers space.

Parameters
:   | pkt | The [net\_pkt](structnet__pkt.md "Network packet.") which payload buffer availability should be evaluated |
    | --- | --- |
    | proto | The IP protocol type (can be 0 for none). |

Returns
:   the amount of buffer available for payload

## [◆ ](#gaefefe50d0c68fb4997abc7b309740959)net\_pkt\_clone()

| struct [net\_pkt](structnet__pkt.md) \* net\_pkt\_clone | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Clone pkt and its buffer.

The cloned packet will be allocated on the same pool as the original one.

Parameters
:   | pkt | Original pkt to be cloned |
    | --- | --- |
    | timeout | Timeout to wait for free buffer |

Returns
:   NULL if error, cloned packet otherwise.

## [◆ ](#gabf85446fb8000574b180d00c5db65a44)net\_pkt\_compact()

| void net\_pkt\_compact | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Compact the fragment list of a packet.

After this there is no more any free space in individual fragments.

Parameters
:   | pkt | Network packet. |
    | --- | --- |

## [◆ ](#ga4648828ca353c8c0ecf00ae2648e963a)net\_pkt\_copy()

| int net\_pkt\_copy | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt\_dst*, |
| --- | --- | --- | --- |
|  |  | struct [net\_pkt](structnet__pkt.md) \* | *pkt\_src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Copy data from a packet into another one.

Both [net\_pkt](structnet__pkt.md "Network packet.") cursors should be properly initialized and, if needed, positioned using net\_pkt\_skip. The cursors will be updated after the operation.

Parameters
:   | pkt\_dst | Destination network packet. |
    | --- | --- |
    | pkt\_src | Source network packet. |
    | length | Length of data to be copied. |

Returns
:   0 on success, negative errno code otherwise.

## [◆ ](#gabd352b66cdeaff2fb45361a0fae62876)net\_pkt\_cursor\_backup()

| | void net\_pkt\_cursor\_backup | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, | | --- | --- | --- | --- | |  |  | struct [net\_pkt\_cursor](structnet__pkt__cursor.md) \* | *backup* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Backup [net\_pkt](structnet__pkt.md "Network packet.") cursor.

Parameters
:   | pkt | The [net\_pkt](structnet__pkt.md "Network packet.") whose cursor is going to be backed up |
    | --- | --- |
    | backup | The cursor where to backup [net\_pkt](structnet__pkt.md "Network packet.") cursor |

## [◆ ](#gabc42ba1bcd0801a116651d965e65b9cd)net\_pkt\_cursor\_get\_pos()

| | void \* net\_pkt\_cursor\_get\_pos | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Returns current position of the cursor.

Parameters
:   | pkt | The [net\_pkt](structnet__pkt.md "Network packet.") whose cursor position is going to be returned |
    | --- | --- |

Returns
:   cursor's position

## [◆ ](#ga1b7da39f62dfc8b8948d7689e2dd114a)net\_pkt\_cursor\_init()

| void net\_pkt\_cursor\_init | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Initialize [net\_pkt](structnet__pkt.md "Network packet.") cursor.

This will initialize the [net\_pkt](structnet__pkt.md "Network packet.") cursor from its buffer.

Parameters
:   | pkt | The [net\_pkt](structnet__pkt.md "Network packet.") whose cursor is going to be initialized |
    | --- | --- |

## [◆ ](#gad5ab788f01b4bb3640755e8c4a2c612e)net\_pkt\_cursor\_restore()

| | void net\_pkt\_cursor\_restore | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, | | --- | --- | --- | --- | |  |  | struct [net\_pkt\_cursor](structnet__pkt__cursor.md) \* | *backup* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Restore [net\_pkt](structnet__pkt.md "Network packet.") cursor from a backup.

Parameters
:   | pkt | The [net\_pkt](structnet__pkt.md "Network packet.") whose cursor is going to be restored |
    | --- | --- |
    | backup | The cursor from where to restore [net\_pkt](structnet__pkt.md "Network packet.") cursor |

## [◆ ](#ga03a53365cfc2b6c3448763d81f56c2c0)net\_pkt\_frag\_add()

| void net\_pkt\_frag\_add | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *frag* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Add a fragment to a packet at the end of its fragment list.

Parameters
:   | pkt | pkt Network packet where to add the fragment |
    | --- | --- |
    | frag | Fragment to add |

## [◆ ](#ga956c784f5417f0f79976c6e106ad0d76)net\_pkt\_frag\_del()

| struct [net\_buf](structnet__buf.md) \* net\_pkt\_frag\_del | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *parent*, |
|  |  | struct [net\_buf](structnet__buf.md) \* | *frag* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Delete existing fragment from a packet.

Parameters
:   | pkt | Network packet from which frag belongs to. |
    | --- | --- |
    | parent | parent fragment of frag, or NULL if none. |
    | frag | Fragment to delete. |

Returns
:   Pointer to the following fragment, or NULL if it had no further fragments.

## [◆ ](#gabcd375d9dbdca21855abe27d7b5a0a7e)net\_pkt\_frag\_insert()

| void net\_pkt\_frag\_insert | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *frag* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Insert a fragment to a packet at the beginning of its fragment list.

Parameters
:   | pkt | pkt Network packet where to insert the fragment |
    | --- | --- |
    | frag | Fragment to insert |

## [◆ ](#gaea5e1045d188b3abbd85717ff09d563a)net\_pkt\_frag\_ref()

| struct [net\_buf](structnet__buf.md) \* net\_pkt\_frag\_ref | ( | struct [net\_buf](structnet__buf.md) \* | *frag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Increase the packet fragment ref count.

Mark the fragment to be used still.

Parameters
:   | frag | Network fragment to ref. |
    | --- | --- |

Returns
:   a pointer on the referenced Network fragment.

## [◆ ](#ga5c75ef2149d2ba5ff07525988e0fb7cc)net\_pkt\_frag\_unref()

| void net\_pkt\_frag\_unref | ( | struct [net\_buf](structnet__buf.md) \* | *frag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Decrease the packet fragment ref count.

Parameters
:   | frag | Network fragment to unref. |
    | --- | --- |

## [◆ ](#gafbd6c0ab33139b134f67a8f8c0096445)net\_pkt\_get\_contiguous\_len()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_pkt\_get\_contiguous\_len | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Get the contiguous buffer space.

Parameters
:   | pkt | Network packet |
    | --- | --- |

Returns
:   The available contiguous buffer space in bytes starting from the current cursor position. 0 in case of an error.

## [◆ ](#gadb3b705a0431b3bb98fb2e8193c3b510)net\_pkt\_get\_current\_offset()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_get\_current\_offset | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Get the actual offset in the packet from its cursor.

Parameters
:   | pkt | Network packet. |
    | --- | --- |

Returns
:   a valid offset on success, 0 otherwise as there is nothing that can be done to evaluate the offset.

## [◆ ](#gaa00da4276fd4a01faf80a92796f78e70)net\_pkt\_get\_data()

| void \* net\_pkt\_get\_data | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | struct [net\_pkt\_data\_access](structnet__pkt__data__access.md) \* | *access* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Get data from a network packet in a contiguous way.

[net\_pkt](structnet__pkt.md "Network packet.")'s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Unlike other functions, cursor position will not be updated after the operation.

Parameters
:   | pkt | The network packet from where to get the data. |
    | --- | --- |
    | access | A pointer to a valid [net\_pkt\_data\_access](structnet__pkt__data__access.md) describing the data to get in a contiguous way. |

Returns
:   a pointer to the requested contiguous data, NULL otherwise.

## [◆ ](#gafa7d666bddb182149d5f540880c46b4e)net\_pkt\_get\_frag()

| struct [net\_buf](structnet__buf.md) \* net\_pkt\_get\_frag | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *min\_len*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Get a data fragment that might be from user specific buffer pool or from global DATA pool.

Parameters
:   | pkt | Network packet. |
    | --- | --- |
    | min\_len | Minimum length of the requested fragment. |
    | timeout | Affects the action taken should the net buf pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait up to the specified time. |

Returns
:   Network buffer if successful, NULL otherwise.

## [◆ ](#ga7b02b95838b928febfd4970de5e9c9f9)net\_pkt\_get\_info()

| void net\_pkt\_get\_info | ( | struct k\_mem\_slab \*\* | *rx*, |
| --- | --- | --- | --- |
|  |  | struct k\_mem\_slab \*\* | *tx*, |
|  |  | struct [net\_buf\_pool](structnet__buf__pool.md) \*\* | *rx\_data*, |
|  |  | struct [net\_buf\_pool](structnet__buf__pool.md) \*\* | *tx\_data* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Get information about predefined RX, TX and DATA pools.

Parameters
:   | rx | Pointer to RX pool is returned. |
    | --- | --- |
    | tx | Pointer to TX pool is returned. |
    | rx\_data | Pointer to RX DATA pool is returned. |
    | tx\_data | Pointer to TX DATA pool is returned. |

## [◆ ](#gaf48f4aac4d16a367d46ca76bf038a485)net\_pkt\_get\_reserve\_rx\_data()

| struct [net\_buf](structnet__buf.md) \* net\_pkt\_get\_reserve\_rx\_data | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *min\_len*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Get RX DATA buffer from pool.

Normally you should use [net\_pkt\_get\_frag()](#gafa7d666bddb182149d5f540880c46b4e) instead.

Normally this version is not useful for applications but is mainly used by network fragmentation code.

Parameters
:   | min\_len | Minimum length of the requested fragment. |
    | --- | --- |
    | timeout | Affects the action taken should the net buf pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait up to the specified time. |

Returns
:   Network buffer if successful, NULL otherwise.

## [◆ ](#gaba26ee929f154978afbd007f7f2b0bc9)net\_pkt\_get\_reserve\_tx\_data()

| struct [net\_buf](structnet__buf.md) \* net\_pkt\_get\_reserve\_tx\_data | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *min\_len*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Get TX DATA buffer from pool.

Normally you should use [net\_pkt\_get\_frag()](#gafa7d666bddb182149d5f540880c46b4e) instead.

Normally this version is not useful for applications but is mainly used by network fragmentation code.

Parameters
:   | min\_len | Minimum length of the requested fragment. |
    | --- | --- |
    | timeout | Affects the action taken should the net buf pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait up to the specified time. |

Returns
:   Network buffer if successful, NULL otherwise.

## [◆ ](#gaf4ee5a8903b495e000a3a4c8a8493160)net\_pkt\_is\_contiguous()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_pkt\_is\_contiguous | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Check if a data size could fit contiguously.

[net\_pkt](structnet__pkt.md "Network packet.")'s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip.

Parameters
:   | pkt | Network packet. |
    | --- | --- |
    | size | The size to check for contiguity |

Returns
:   true if that is the case, false otherwise.

## [◆ ](#gabd241a539bf1290f3d45610fd15b2c1f)net\_pkt\_memset()

| int net\_pkt\_memset | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | int | *byte*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Memset some data in a [net\_pkt](structnet__pkt.md "Network packet.").

[net\_pkt](structnet__pkt.md "Network packet.")'s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

Parameters
:   | pkt | The [net\_pkt](structnet__pkt.md "Network packet.") whose buffer to fill starting at the current cursor position. |
    | --- | --- |
    | byte | The byte to write in memory |
    | length | Amount of data to memset with given byte |

Returns
:   0 in success, negative errno code otherwise.

## [◆ ](#ga434c347a32600ee113c0e1cc13f70cd4)net\_pkt\_pull()

| int net\_pkt\_pull | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Remove data from the packet at current location.

[net\_pkt](structnet__pkt.md "Network packet.")'s cursor should be properly initialized and, eventually, properly positioned using net\_pkt\_skip/read/write. Note that [net\_pkt](structnet__pkt.md "Network packet.")'s cursor is reset by this function.

Parameters
:   | pkt | Network packet |
    | --- | --- |
    | length | Number of bytes to be removed |

Returns
:   0 on success, negative errno code otherwise.

## [◆ ](#ga914be010ddd225a4fc2d6ab521ee7b64)net\_pkt\_read()

| int net\_pkt\_read | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Read some data from a [net\_pkt](structnet__pkt.md "Network packet.").

[net\_pkt](structnet__pkt.md "Network packet.")'s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

Parameters
:   | pkt | The network packet from where to read some data |
    | --- | --- |
    | data | The destination buffer where to copy the data |
    | length | The amount of data to copy |

Returns
:   0 on success, negative errno code otherwise.

## [◆ ](#ga500a318977cfecd4ec7c60cea01db2fc)net\_pkt\_read\_be16()

| int net\_pkt\_read\_be16 | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *data* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Read [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) big endian data from a [net\_pkt](structnet__pkt.md "Network packet.").

[net\_pkt](structnet__pkt.md "Network packet.")'s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

Parameters
:   | pkt | The network packet from where to read |
    | --- | --- |
    | data | The destination [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) where to copy the data |

Returns
:   0 on success, negative errno code otherwise.

## [◆ ](#gab38c99947d02982073df65c0d5893d2c)net\_pkt\_read\_be32()

| int net\_pkt\_read\_be32 | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *data* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Read [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) big endian data from a [net\_pkt](structnet__pkt.md "Network packet.").

[net\_pkt](structnet__pkt.md "Network packet.")'s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

Parameters
:   | pkt | The network packet from where to read |
    | --- | --- |
    | data | The destination [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) where to copy the data |

Returns
:   0 on success, negative errno code otherwise.

## [◆ ](#gab1735ef4f6a2e538a2692358295dd8d1)net\_pkt\_read\_le16()

| int net\_pkt\_read\_le16 | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *data* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Read [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) little endian data from a [net\_pkt](structnet__pkt.md "Network packet.").

[net\_pkt](structnet__pkt.md "Network packet.")'s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

Parameters
:   | pkt | The network packet from where to read |
    | --- | --- |
    | data | The destination [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) where to copy the data |

Returns
:   0 on success, negative errno code otherwise.

## [◆ ](#gaf9b2753cb514804a77d9494c9f070089)net\_pkt\_read\_u8()

| | int net\_pkt\_read\_u8 | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

## [◆ ](#ga4e83d4f60b46db8f57798c0e96d6cd7a)net\_pkt\_ref()

| struct [net\_pkt](structnet__pkt.md) \* net\_pkt\_ref | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Increase the packet ref count.

Mark the packet to be used still.

Parameters
:   | pkt | Network packet to ref. |
    | --- | --- |

Returns
:   Network packet if successful, NULL otherwise.

## [◆ ](#gadee5307216b6b3b725a2fd7584a224c9)net\_pkt\_remaining\_data()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_pkt\_remaining\_data | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Get the amount of data which can be read from current cursor position.

Parameters
:   | pkt | Network packet |
    | --- | --- |

Returns
:   Amount of data which can be read from current pkt cursor

## [◆ ](#gab657c80669733a4afefaf1be6310107e)net\_pkt\_remove\_tail()

| int net\_pkt\_remove\_tail | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Remove *length* bytes from tail of packet.

This function does not take packet cursor into account. It is a helper to remove unneeded bytes from tail of packet (like appended CRC). It takes care of buffer deallocation if removed bytes span whole buffer(s).

Parameters
:   | pkt | Network packet |
    | --- | --- |
    | length | Number of bytes to be removed |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EINVAL | If packet length is shorter than *length*. |

## [◆ ](#ga4cec027a0de4807879fd3bd3aed4f12a)net\_pkt\_rx\_alloc()

| struct [net\_pkt](structnet__pkt.md) \* net\_pkt\_rx\_alloc | ( | [k\_timeout\_t](structk__timeout__t.md) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Allocate an initialized [net\_pkt](structnet__pkt.md "Network packet.") for RX.

for the time being, 2 pools are used. One for TX and one for RX. This allocator has to be used for RX.

Parameters
:   | timeout | Maximum time to wait for an allocation. |
    | --- | --- |

Returns
:   a pointer to a newly allocated [net\_pkt](structnet__pkt.md "Network packet.") on success, NULL otherwise.

## [◆ ](#gab64f7551b1995c301232ab4cd39b9efc)net\_pkt\_rx\_alloc\_on\_iface()

| struct [net\_pkt](structnet__pkt.md) \* net\_pkt\_rx\_alloc\_on\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

## [◆ ](#ga623794964a35e0e24c1f41a75bfba626)net\_pkt\_rx\_alloc\_with\_buffer()

| struct [net\_pkt](structnet__pkt.md) \* net\_pkt\_rx\_alloc\_with\_buffer | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, |
|  |  | enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) | *proto*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

## [◆ ](#ga66aec729118e4d927c921b872df82dda)net\_pkt\_rx\_clone()

| struct [net\_pkt](structnet__pkt.md) \* net\_pkt\_rx\_clone | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Clone pkt and its buffer.

The cloned packet will be allocated on the RX packet poll.

Parameters
:   | pkt | Original pkt to be cloned |
    | --- | --- |
    | timeout | Timeout to wait for free buffer |

Returns
:   NULL if error, cloned packet otherwise.

## [◆ ](#ga98df84477b35e203b11029fc4ddec1cc)net\_pkt\_set\_data()

| int net\_pkt\_set\_data | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | struct [net\_pkt\_data\_access](structnet__pkt__data__access.md) \* | *access* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Set contiguous data into a network packet.

[net\_pkt](structnet__pkt.md "Network packet.")'s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

Parameters
:   | pkt | The network packet to where the data should be set. |
    | --- | --- |
    | access | A pointer to a valid [net\_pkt\_data\_access](structnet__pkt__data__access.md) describing the data to set. |

Returns
:   0 on success, a negative errno otherwise.

## [◆ ](#ga26ae9d1286cb98d255f1bfb65201f1e2)net\_pkt\_shallow\_clone()

| struct [net\_pkt](structnet__pkt.md) \* net\_pkt\_shallow\_clone | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Clone pkt and increase the refcount of its buffer.

Parameters
:   | pkt | Original pkt to be shallow cloned |
    | --- | --- |
    | timeout | Timeout to wait for free packet |

Returns
:   NULL if error, cloned packet otherwise.

## [◆ ](#ga223a79baa1e740a53c4ed0f083d62185)net\_pkt\_skip()

| int net\_pkt\_skip | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Skip some data from a [net\_pkt](structnet__pkt.md "Network packet.").

[net\_pkt](structnet__pkt.md "Network packet.")'s cursor should be properly initialized Cursor position will be updated after the operation. Depending on the value of pkt->overwrite bit, this function will affect the buffer length or not. If it's true, it will advance the cursor to the requested length. If it's false, it will do the same but if the cursor was already also at the end of existing data, it will increment the buffer length. So in this case, its behavior is just like net\_pkt\_write or net\_pkt\_memset, difference being that it will not affect the buffer content itself (which may be just garbage then).

Parameters
:   | pkt | The [net\_pkt](structnet__pkt.md "Network packet.") whose cursor will be updated to skip given amount of data from the buffer. |
    | --- | --- |
    | length | Amount of data to skip in the buffer |

Returns
:   0 in success, negative errno code otherwise.

## [◆ ](#ga71d1c49f68afab07324cebd835f08a29)net\_pkt\_trim\_buffer()

| void net\_pkt\_trim\_buffer | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Trim [net\_pkt](structnet__pkt.md "Network packet.") buffer.

This will basically check for unused buffers and deallocate them relevantly

Parameters
:   | pkt | The [net\_pkt](structnet__pkt.md "Network packet.") which buffer will be trimmed |
    | --- | --- |

## [◆ ](#ga893d1660fd18ad5842224fda78466099)net\_pkt\_unref()

| void net\_pkt\_unref | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Place packet back into the available packets slab.

Releases the packet to other use. This needs to be called by application after it has finished with the packet.

Parameters
:   | pkt | Network packet to release. |
    | --- | --- |

## [◆ ](#ga2e7a0f9348a623c5160124da188445ee)net\_pkt\_update\_length()

| int net\_pkt\_update\_length | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Update the overall length of a packet.

Unlike [net\_pkt\_pull()](#ga434c347a32600ee113c0e1cc13f70cd4) below, this does not take packet cursor into account. It's mainly a helper dedicated for ipv4 and ipv6 input functions. It shrinks the overall length by given parameter.

Parameters
:   | pkt | Network packet |
    | --- | --- |
    | length | The new length of the packet |

Returns
:   0 on success, negative errno code otherwise.

## [◆ ](#gae99eadd977b7f66ecc91d2ccba34c6fa)net\_pkt\_write()

| int net\_pkt\_write | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, |
| --- | --- | --- | --- |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[net_pkt.h](net__pkt_8h.md)>`

Write data into a [net\_pkt](structnet__pkt.md "Network packet.").

[net\_pkt](structnet__pkt.md "Network packet.")'s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

Parameters
:   | pkt | The network packet where to write |
    | --- | --- |
    | data | Data to be written |
    | length | Length of the data to be written |

Returns
:   0 on success, negative errno code otherwise.

## [◆ ](#ga8e5083388ccb0333fdcf745bc60ad260)net\_pkt\_write\_be16()

| | int net\_pkt\_write\_be16 | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

## [◆ ](#ga053aff4ff0a501f336132c35b7fb2022)net\_pkt\_write\_be32()

| | int net\_pkt\_write\_be32 | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

## [◆ ](#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)net\_pkt\_write\_le16()

| | int net\_pkt\_write\_le16 | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

## [◆ ](#gaf2388032e4e0b76fe32e4618ef3ea548)net\_pkt\_write\_le32()

| | int net\_pkt\_write\_le32 | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

## [◆ ](#gaa5129f661075c13d9b59627ae9110bd1)net\_pkt\_write\_u8()

| | int net\_pkt\_write\_u8 | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_pkt.h](net__pkt_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
