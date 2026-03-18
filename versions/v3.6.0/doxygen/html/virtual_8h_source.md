---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/virtual_8h_source.html
original_path: doxygen/html/virtual_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtual.h

[Go to the documentation of this file.](virtual_8h.md)

1

4

5/\*

6 \* Copyright (c) 2021 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_VIRTUAL\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_VIRTUAL\_H\_

13

14#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16#include <[stdbool.h](stdbool_8h.md)>

17#include <[zephyr/sys/atomic.h](atomic_8h.md)>

18

19#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

20#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

21

22#include <[zephyr/sys/util.h](util_8h.md)>

23#include <[zephyr/net/net\_if.h](net__if_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

35

[ 37](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091)enum [virtual\_interface\_caps](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091) {

[ 39](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071) [VIRTUAL\_INTERFACE\_IPIP](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

40

42 /\* Marker for capabilities - must be at the end of the enum.

43 \* It is here because the capability list cannot be empty.

44 \*/

45 VIRTUAL\_INTERFACE\_NUM\_CAPS

47};

48

50

51enum virtual\_interface\_config\_type {

52 VIRTUAL\_INTERFACE\_CONFIG\_TYPE\_PEER\_ADDRESS,

53 VIRTUAL\_INTERFACE\_CONFIG\_TYPE\_MTU,

54};

55

56struct virtual\_interface\_config {

57 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family;

58 union {

59 struct in\_addr peer4addr;

60 struct in6\_addr peer6addr;

61 int mtu;

62 };

63};

64

65#if defined(CONFIG\_NET\_L2\_VIRTUAL)

66#define VIRTUAL\_MAX\_NAME\_LEN CONFIG\_NET\_L2\_VIRTUAL\_MAX\_NAME\_LEN

67#else

68#define VIRTUAL\_MAX\_NAME\_LEN 0

69#endif

71

[ 72](structvirtual__interface__api.md)struct [virtual\_interface\_api](structvirtual__interface__api.md) {

[ 77](structvirtual__interface__api.md#a827cd13d885b7cc2f80eddd73e438e07) struct net\_if\_api [iface\_api](structvirtual__interface__api.md#aee1250773938536ab28e129113073ae7);

78

80 enum [virtual\_interface\_caps](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091) (\*[get\_capabilities](structvirtual__interface__api.md#a827cd13d885b7cc2f80eddd73e438e07))(struct [net\_if](structnet__if.md) \*iface);

81

[ 83](structvirtual__interface__api.md#af28a6ed36799006d185fab9129c6c120) int (\*[start](structvirtual__interface__api.md#af28a6ed36799006d185fab9129c6c120))(const struct [device](structdevice.md) \*dev);

84

[ 86](structvirtual__interface__api.md#a09a317009d31ac5e9340c3ca7d2191c4) int (\*[stop](structvirtual__interface__api.md#a09a317009d31ac5e9340c3ca7d2191c4))(const struct [device](structdevice.md) \*dev);

87

[ 89](structvirtual__interface__api.md#a285f8f872420209107f73b6b268af7b2) int (\*[send](structvirtual__interface__api.md#a6fbfa013374bbafaa610b0a054d3a415))(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

90

92 enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) (\*[recv](structvirtual__interface__api.md#a6f21e33e39caa00d51cca900a26f7070))(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

93

99 enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) (\*[input](structvirtual__interface__api.md#a285f8f872420209107f73b6b268af7b2))(struct [net\_if](structnet__if.md) \*input\_iface,

100 struct [net\_if](structnet__if.md) \*iface,

101 struct net\_addr \*remote\_addr,

102 struct [net\_pkt](structnet__pkt.md) \*pkt);

103

[ 105](structvirtual__interface__api.md#a753258a8929347877997ca5d6a76eb8c) int (\*[attach](structvirtual__interface__api.md#a753258a8929347877997ca5d6a76eb8c))(struct [net\_if](structnet__if.md) \*virtual\_iface, struct [net\_if](structnet__if.md) \*iface);

106

[ 108](structvirtual__interface__api.md#a591f1b7df5313c4a225dceaa04b1eeae) int (\*[set\_config](structvirtual__interface__api.md#a591f1b7df5313c4a225dceaa04b1eeae))(struct [net\_if](structnet__if.md) \*iface,

109 enum virtual\_interface\_config\_type type,

110 const struct virtual\_interface\_config \*config);

111

[ 113](structvirtual__interface__api.md#a4ff5b92897926616778eb6fb696ebb16) int (\*[get\_config](structvirtual__interface__api.md#a4ff5b92897926616778eb6fb696ebb16))(struct [net\_if](structnet__if.md) \*iface,

114 enum virtual\_interface\_config\_type type,

115 struct virtual\_interface\_config \*config);

116};

117

118/\* Make sure that the network interface API is properly setup inside

119 \* Virtual API struct (it is the first one).

120 \*/

121BUILD\_ASSERT(offsetof(struct [virtual\_interface\_api](structvirtual__interface__api.md), iface\_api) == 0);

122

[ 125](structvirtual__interface__context.md)struct [virtual\_interface\_context](structvirtual__interface__context.md) {

127 /\* Keep track of contexts \*/

128 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

129

130 /\* My virtual network interface \*/

131 struct [net\_if](structnet__if.md) \*virtual\_iface;

133

[ 139](structvirtual__interface__context.md#a4a0aada1d7af7a86d2a4b12063f35c71) struct [net\_if](structnet__if.md) \*[iface](structvirtual__interface__context.md#a4a0aada1d7af7a86d2a4b12063f35c71);

140

[ 144](structvirtual__interface__context.md#a493cef75dd5000b19eab5db156015c6e) enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) [virtual\_l2\_flags](structvirtual__interface__context.md#a493cef75dd5000b19eab5db156015c6e);

145

[ 147](structvirtual__interface__context.md#a7e4699c462a1edfdb755833a9ab28d8f) bool [is\_init](structvirtual__interface__context.md#a7e4699c462a1edfdb755833a9ab28d8f);

148

[ 150](structvirtual__interface__context.md#aaf591f82e0448f2b0cbf4ea6fcf05bff) struct [net\_linkaddr\_storage](structnet__linkaddr__storage.md) [lladdr](structvirtual__interface__context.md#aaf591f82e0448f2b0cbf4ea6fcf05bff);

151

[ 153](structvirtual__interface__context.md#a7d53af8860331f23b8ff83ba0bfcaacf) char [name](structvirtual__interface__context.md#a7d53af8860331f23b8ff83ba0bfcaacf)[VIRTUAL\_MAX\_NAME\_LEN];

154};

155

[ 165](group__virtual.md#ga5cba6ff65402b591a0e42d05f258671f)int [net\_virtual\_interface\_attach](group__virtual.md#ga5cba6ff65402b591a0e42d05f258671f)(struct [net\_if](structnet__if.md) \*virtual\_iface,

166 struct [net\_if](structnet__if.md) \*iface);

167

[ 177](group__virtual.md#gabadf14eaa02978cde7030c99ddd3e279)struct [net\_if](structnet__if.md) \*[net\_virtual\_get\_iface](group__virtual.md#gabadf14eaa02978cde7030c99ddd3e279)(struct [net\_if](structnet__if.md) \*iface);

178

[ 188](group__virtual.md#gaa7ff8ebb83fe98a1dfd23f319317a8de)char \*[net\_virtual\_get\_name](group__virtual.md#gaa7ff8ebb83fe98a1dfd23f319317a8de)(struct [net\_if](structnet__if.md) \*iface, char \*buf, size\_t len);

189

[ 196](group__virtual.md#ga2aaba616ed4fecc27138d5aae58a634f)void [net\_virtual\_set\_name](group__virtual.md#ga2aaba616ed4fecc27138d5aae58a634f)(struct [net\_if](structnet__if.md) \*iface, const char \*name);

197

[ 206](group__virtual.md#ga30f92f519a6f204ebeccd6053f17eaf0)enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) [net\_virtual\_set\_flags](group__virtual.md#ga30f92f519a6f204ebeccd6053f17eaf0)(struct [net\_if](structnet__if.md) \*iface,

207 enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

208

[ 218](group__virtual.md#ga6c63773925ef7d96b0ba03d8978fd499)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [net\_virtual\_input](group__virtual.md#ga6c63773925ef7d96b0ba03d8978fd499)(struct [net\_if](structnet__if.md) \*input\_iface,

219 struct net\_addr \*remote\_addr,

220 struct [net\_pkt](structnet__pkt.md) \*pkt);

221

223

230#if defined(CONFIG\_NET\_L2\_VIRTUAL)

231void net\_virtual\_init(struct [net\_if](structnet__if.md) \*iface);

232#else

233static inline void net\_virtual\_init(struct [net\_if](structnet__if.md) \*iface)

234{

235 ARG\_UNUSED(iface);

236}

237#endif

238

245#if defined(CONFIG\_NET\_L2\_VIRTUAL)

246void net\_virtual\_disable(struct [net\_if](structnet__if.md) \*iface);

247#else

248static inline void net\_virtual\_disable(struct [net\_if](structnet__if.md) \*iface)

249{

250 ARG\_UNUSED(iface);

251}

252#endif

253

260#if defined(CONFIG\_NET\_L2\_VIRTUAL)

261void net\_virtual\_enable(struct [net\_if](structnet__if.md) \*iface);

262#else

263static inline void net\_virtual\_enable(struct [net\_if](structnet__if.md) \*iface)

264{

265 ARG\_UNUSED(iface);

266}

267#endif

268

269#define VIRTUAL\_L2\_CTX\_TYPE struct virtual\_interface\_context

270

278static inline enum [virtual\_interface\_caps](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091)

279net\_virtual\_get\_iface\_capabilities(struct [net\_if](structnet__if.md) \*iface)

280{

281 const struct [virtual\_interface\_api](structvirtual__interface__api.md) \*virt =

282 (struct [virtual\_interface\_api](structvirtual__interface__api.md) \*)[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(iface)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

283

284 if (!virt->[get\_capabilities](structvirtual__interface__api.md#a827cd13d885b7cc2f80eddd73e438e07)) {

285 return (enum [virtual\_interface\_caps](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091))0;

286 }

287

288 return virt->[get\_capabilities](structvirtual__interface__api.md#a827cd13d885b7cc2f80eddd73e438e07)(iface);

289}

290

291#define Z\_NET\_VIRTUAL\_INTERFACE\_INIT(node\_id, dev\_id, name, init\_fn, \

292 pm, data, config, prio, api, mtu) \

293 Z\_NET\_DEVICE\_INIT(node\_id, dev\_id, name, init\_fn, pm, data, \

294 config, prio, api, VIRTUAL\_L2, \

295 NET\_L2\_GET\_CTX\_TYPE(VIRTUAL\_L2), mtu)

297

[ 319](group__virtual.md#ga74a5c258a08397f881a8922516ac5d3a)#define NET\_VIRTUAL\_INTERFACE\_INIT(dev\_id, name, init\_fn, pm, data, \

320 config, prio, api, mtu) \

321 Z\_NET\_VIRTUAL\_INTERFACE\_INIT(DT\_INVALID\_NODE, dev\_id, name, \

322 init\_fn, pm, data, config, prio, \

323 api, mtu)

324

328

329#ifdef \_\_cplusplus

330}

331#endif

332

333#endif /\* ZEPHYR\_INCLUDE\_NET\_VIRTUAL\_H\_ \*/

[atomic.h](atomic_8h.md)

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:164

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:98

[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)

static const struct device \* net\_if\_get\_device(struct net\_if \*iface)

Get an network interface's device.

**Definition** net\_if.h:857

[net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516)

net\_l2\_flags

L2 flags.

**Definition** net\_l2.h:34

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[net\_virtual\_set\_name](group__virtual.md#ga2aaba616ed4fecc27138d5aae58a634f)

void net\_virtual\_set\_name(struct net\_if \*iface, const char \*name)

Set the name of the virtual network interface L2.

[net\_virtual\_set\_flags](group__virtual.md#ga30f92f519a6f204ebeccd6053f17eaf0)

enum net\_l2\_flags net\_virtual\_set\_flags(struct net\_if \*iface, enum net\_l2\_flags flags)

Set the L2 flags of the virtual network interface.

[net\_virtual\_interface\_attach](group__virtual.md#ga5cba6ff65402b591a0e42d05f258671f)

int net\_virtual\_interface\_attach(struct net\_if \*virtual\_iface, struct net\_if \*iface)

Attach virtual network interface to the given network interface.

[net\_virtual\_input](group__virtual.md#ga6c63773925ef7d96b0ba03d8978fd499)

enum net\_verdict net\_virtual\_input(struct net\_if \*input\_iface, struct net\_addr \*remote\_addr, struct net\_pkt \*pkt)

Feed the IP pkt to stack if tunneling is enabled.

[virtual\_interface\_caps](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091)

virtual\_interface\_caps

Virtual interface capabilities.

**Definition** virtual.h:37

[net\_virtual\_get\_name](group__virtual.md#gaa7ff8ebb83fe98a1dfd23f319317a8de)

char \* net\_virtual\_get\_name(struct net\_if \*iface, char \*buf, size\_t len)

Return the name of the virtual network interface L2.

[net\_virtual\_get\_iface](group__virtual.md#gabadf14eaa02978cde7030c99ddd3e279)

struct net\_if \* net\_virtual\_get\_iface(struct net\_if \*iface)

Return network interface related to this virtual network interface.

[VIRTUAL\_INTERFACE\_IPIP](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071)

@ VIRTUAL\_INTERFACE\_IPIP

IPIP tunnel.

**Definition** virtual.h:39

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[net\_pkt.h](net__pkt_8h.md)

Network packet buffer descriptor API.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdbool.h](stdbool_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[net\_linkaddr\_storage](structnet__linkaddr__storage.md)

Hardware link address structure.

**Definition** net\_linkaddr.h:88

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

[virtual\_interface\_api](structvirtual__interface__api.md)

**Definition** virtual.h:72

[virtual\_interface\_api::stop](structvirtual__interface__api.md#a09a317009d31ac5e9340c3ca7d2191c4)

int(\* stop)(const struct device \*dev)

Stop the device.

**Definition** virtual.h:86

[virtual\_interface\_api::input](structvirtual__interface__api.md#a285f8f872420209107f73b6b268af7b2)

enum net\_verdict(\* input)(struct net\_if \*input\_iface, struct net\_if \*iface, struct net\_addr \*remote\_addr, struct net\_pkt \*pkt)

Check if this received network packet is for this interface.

**Definition** virtual.h:99

[virtual\_interface\_api::get\_config](structvirtual__interface__api.md#a4ff5b92897926616778eb6fb696ebb16)

int(\* get\_config)(struct net\_if \*iface, enum virtual\_interface\_config\_type type, struct virtual\_interface\_config \*config)

Get specific L2 configuration.

**Definition** virtual.h:113

[virtual\_interface\_api::set\_config](structvirtual__interface__api.md#a591f1b7df5313c4a225dceaa04b1eeae)

int(\* set\_config)(struct net\_if \*iface, enum virtual\_interface\_config\_type type, const struct virtual\_interface\_config \*config)

Set specific L2 configuration.

**Definition** virtual.h:108

[virtual\_interface\_api::recv](structvirtual__interface__api.md#a6f21e33e39caa00d51cca900a26f7070)

enum net\_verdict(\* recv)(struct net\_if \*iface, struct net\_pkt \*pkt)

Receive a network packet.

**Definition** virtual.h:92

[virtual\_interface\_api::send](structvirtual__interface__api.md#a6fbfa013374bbafaa610b0a054d3a415)

int(\* send)(struct net\_if \*iface, struct net\_pkt \*pkt)

Send a network packet.

**Definition** virtual.h:89

[virtual\_interface\_api::attach](structvirtual__interface__api.md#a753258a8929347877997ca5d6a76eb8c)

int(\* attach)(struct net\_if \*virtual\_iface, struct net\_if \*iface)

Pass the attachment information to virtual interface.

**Definition** virtual.h:105

[virtual\_interface\_api::get\_capabilities](structvirtual__interface__api.md#a827cd13d885b7cc2f80eddd73e438e07)

enum virtual\_interface\_caps(\* get\_capabilities)(struct net\_if \*iface)

Get the virtual interface capabilities.

**Definition** virtual.h:80

[virtual\_interface\_api::iface\_api](structvirtual__interface__api.md#aee1250773938536ab28e129113073ae7)

struct net\_if\_api iface\_api

The net\_if\_api must be placed in first position in this struct so that we are compatible with network...

**Definition** virtual.h:77

[virtual\_interface\_api::start](structvirtual__interface__api.md#af28a6ed36799006d185fab9129c6c120)

int(\* start)(const struct device \*dev)

Start the device.

**Definition** virtual.h:83

[virtual\_interface\_context](structvirtual__interface__context.md)

Virtual L2 context that is needed to binding to the real network interface.

**Definition** virtual.h:125

[virtual\_interface\_context::virtual\_l2\_flags](structvirtual__interface__context.md#a493cef75dd5000b19eab5db156015c6e)

enum net\_l2\_flags virtual\_l2\_flags

This tells what L2 features does virtual support.

**Definition** virtual.h:144

[virtual\_interface\_context::iface](structvirtual__interface__context.md#a4a0aada1d7af7a86d2a4b12063f35c71)

struct net\_if \* iface

Other network interface this virtual network interface is attached to.

**Definition** virtual.h:139

[virtual\_interface\_context::name](structvirtual__interface__context.md#a7d53af8860331f23b8ff83ba0bfcaacf)

char name[VIRTUAL\_MAX\_NAME\_LEN]

User friendly name of this L2 layer.

**Definition** virtual.h:153

[virtual\_interface\_context::is\_init](structvirtual__interface__context.md#a7e4699c462a1edfdb755833a9ab28d8f)

bool is\_init

Is this context already initialized.

**Definition** virtual.h:147

[virtual\_interface\_context::lladdr](structvirtual__interface__context.md#aaf591f82e0448f2b0cbf4ea6fcf05bff)

struct net\_linkaddr\_storage lladdr

Link address for this network interface.

**Definition** virtual.h:150

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [virtual.h](virtual_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
