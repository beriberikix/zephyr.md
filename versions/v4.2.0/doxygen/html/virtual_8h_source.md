---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/virtual_8h_source.html
original_path: doxygen/html/virtual_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

14#include <[zephyr/kernel.h](kernel_8h.md)>

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16#include <[stdbool.h](stdbool_8h.md)>

17#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

18

19#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

20#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

21

22#include <[zephyr/sys/util.h](sys_2util_8h.md)>

23#include <[zephyr/net/net\_if.h](net__if_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

37

[ 39](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091)enum [virtual\_interface\_caps](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091) {

[ 41](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071) [VIRTUAL\_INTERFACE\_IPIP](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

42

[ 44](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a5d496813292edfe8156484450fc7d83b) [VIRTUAL\_INTERFACE\_VLAN](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a5d496813292edfe8156484450fc7d83b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

45

[ 47](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a1ce35cd2b3312437b51d7440da2efaed) [VIRTUAL\_INTERFACE\_BRIDGE](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a1ce35cd2b3312437b51d7440da2efaed) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

48

[ 50](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a145ffaeae08793e4c93ea7be320efe2b) [VIRTUAL\_INTERFACE\_VPN](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a145ffaeae08793e4c93ea7be320efe2b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

51

53 /\* Marker for capabilities - must be at the end of the enum.

54 \* It is here because the capability list cannot be empty.

55 \*/

56 VIRTUAL\_INTERFACE\_NUM\_CAPS

58};

59

61

62enum virtual\_interface\_config\_type {

63 VIRTUAL\_INTERFACE\_CONFIG\_TYPE\_PEER\_ADDRESS,

64 VIRTUAL\_INTERFACE\_CONFIG\_TYPE\_MTU,

65 VIRTUAL\_INTERFACE\_CONFIG\_TYPE\_LINK\_TYPE,

66 VIRTUAL\_INTERFACE\_CONFIG\_TYPE\_PRIVATE\_KEY,

67 VIRTUAL\_INTERFACE\_CONFIG\_TYPE\_PUBLIC\_KEY,

68};

69

70struct virtual\_interface\_link\_types {

71 int count;

72 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type[[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_NET\_CAPTURE\_COOKED\_MODE,

73 (CONFIG\_NET\_CAPTURE\_COOKED\_MODE\_MAX\_LINK\_TYPES),

74 (1))];

75};

76

77#if !defined(NET\_VIRTUAL\_MAX\_PUBLIC\_KEY\_LEN)

78#define NET\_VIRTUAL\_MAX\_PUBLIC\_KEY\_LEN 32U

79#endif

80

81struct virtual\_interface\_config {

82 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family;

83 union {

84 struct in\_addr peer4addr;

85 struct in6\_addr peer6addr;

86 int mtu;

87 struct virtual\_interface\_link\_types link\_types;

88 struct {

89 size\_t len;

90 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data;

91 } private\_key;

92 struct {

93 size\_t len;

94 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data[NET\_VIRTUAL\_MAX\_PUBLIC\_KEY\_LEN];

95 } public\_key;

96 };

97};

98

99#if defined(CONFIG\_NET\_L2\_VIRTUAL)

100#define VIRTUAL\_MAX\_NAME\_LEN CONFIG\_NET\_L2\_VIRTUAL\_MAX\_NAME\_LEN

101#else

102#define VIRTUAL\_MAX\_NAME\_LEN 0

103#endif

105

[ 107](structvirtual__interface__api.md)struct [virtual\_interface\_api](structvirtual__interface__api.md) {

[ 112](structvirtual__interface__api.md#a827cd13d885b7cc2f80eddd73e438e07) struct net\_if\_api [iface\_api](structvirtual__interface__api.md#aee1250773938536ab28e129113073ae7);

113

115 enum [virtual\_interface\_caps](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091) (\*[get\_capabilities](structvirtual__interface__api.md#a827cd13d885b7cc2f80eddd73e438e07))(struct [net\_if](structnet__if.md) \*iface);

116

[ 118](structvirtual__interface__api.md#af28a6ed36799006d185fab9129c6c120) int (\*[start](structvirtual__interface__api.md#af28a6ed36799006d185fab9129c6c120))(const struct [device](structdevice.md) \*dev);

119

[ 121](structvirtual__interface__api.md#a09a317009d31ac5e9340c3ca7d2191c4) int (\*[stop](structvirtual__interface__api.md#a09a317009d31ac5e9340c3ca7d2191c4))(const struct [device](structdevice.md) \*dev);

122

[ 124](structvirtual__interface__api.md#a6f21e33e39caa00d51cca900a26f7070) int (\*[send](structvirtual__interface__api.md#a6fbfa013374bbafaa610b0a054d3a415))(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

125

132 enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) (\*[recv](structvirtual__interface__api.md#a6f21e33e39caa00d51cca900a26f7070))(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

133

[ 135](structvirtual__interface__api.md#a753258a8929347877997ca5d6a76eb8c) int (\*[attach](structvirtual__interface__api.md#a753258a8929347877997ca5d6a76eb8c))(struct [net\_if](structnet__if.md) \*virtual\_iface, struct [net\_if](structnet__if.md) \*iface);

136

[ 138](structvirtual__interface__api.md#a591f1b7df5313c4a225dceaa04b1eeae) int (\*[set\_config](structvirtual__interface__api.md#a591f1b7df5313c4a225dceaa04b1eeae))(struct [net\_if](structnet__if.md) \*iface,

139 enum virtual\_interface\_config\_type type,

140 const struct virtual\_interface\_config \*config);

141

[ 143](structvirtual__interface__api.md#a4ff5b92897926616778eb6fb696ebb16) int (\*[get\_config](structvirtual__interface__api.md#a4ff5b92897926616778eb6fb696ebb16))(struct [net\_if](structnet__if.md) \*iface,

144 enum virtual\_interface\_config\_type type,

145 struct virtual\_interface\_config \*config);

146};

147

148/\* Make sure that the network interface API is properly setup inside

149 \* Virtual API struct (it is the first one).

150 \*/

151BUILD\_ASSERT(offsetof(struct [virtual\_interface\_api](structvirtual__interface__api.md), iface\_api) == 0);

152

[ 155](structvirtual__interface__context.md)struct [virtual\_interface\_context](structvirtual__interface__context.md) {

157 /\* Keep track of contexts \*/

158 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

159

160 /\* My virtual network interface \*/

161 struct [net\_if](structnet__if.md) \*virtual\_iface;

163

[ 169](structvirtual__interface__context.md#a4a0aada1d7af7a86d2a4b12063f35c71) struct [net\_if](structnet__if.md) \*[iface](structvirtual__interface__context.md#a4a0aada1d7af7a86d2a4b12063f35c71);

170

[ 174](structvirtual__interface__context.md#a493cef75dd5000b19eab5db156015c6e) enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) [virtual\_l2\_flags](structvirtual__interface__context.md#a493cef75dd5000b19eab5db156015c6e);

175

[ 177](structvirtual__interface__context.md#a7e4699c462a1edfdb755833a9ab28d8f) bool [is\_init](structvirtual__interface__context.md#a7e4699c462a1edfdb755833a9ab28d8f);

178

[ 180](structvirtual__interface__context.md#ade8a686b9c002c064e2ae9e1815b6601) struct [net\_linkaddr](structnet__linkaddr.md) [lladdr](structvirtual__interface__context.md#ade8a686b9c002c064e2ae9e1815b6601);

181

[ 183](structvirtual__interface__context.md#a7d53af8860331f23b8ff83ba0bfcaacf) char [name](structvirtual__interface__context.md#a7d53af8860331f23b8ff83ba0bfcaacf)[VIRTUAL\_MAX\_NAME\_LEN];

184};

185

[ 195](group__virtual.md#ga5cba6ff65402b591a0e42d05f258671f)int [net\_virtual\_interface\_attach](group__virtual.md#ga5cba6ff65402b591a0e42d05f258671f)(struct [net\_if](structnet__if.md) \*virtual\_iface,

196 struct [net\_if](structnet__if.md) \*iface);

197

[ 207](group__virtual.md#gabadf14eaa02978cde7030c99ddd3e279)struct [net\_if](structnet__if.md) \*[net\_virtual\_get\_iface](group__virtual.md#gabadf14eaa02978cde7030c99ddd3e279)(struct [net\_if](structnet__if.md) \*iface);

208

[ 218](group__virtual.md#gaa7ff8ebb83fe98a1dfd23f319317a8de)char \*[net\_virtual\_get\_name](group__virtual.md#gaa7ff8ebb83fe98a1dfd23f319317a8de)(struct [net\_if](structnet__if.md) \*iface, char \*buf, size\_t len);

219

[ 226](group__virtual.md#ga2aaba616ed4fecc27138d5aae58a634f)void [net\_virtual\_set\_name](group__virtual.md#ga2aaba616ed4fecc27138d5aae58a634f)(struct [net\_if](structnet__if.md) \*iface, const char \*name);

227

[ 236](group__virtual.md#ga30f92f519a6f204ebeccd6053f17eaf0)enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) [net\_virtual\_set\_flags](group__virtual.md#ga30f92f519a6f204ebeccd6053f17eaf0)(struct [net\_if](structnet__if.md) \*iface,

237 enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

238

[ 248](group__virtual.md#ga6c63773925ef7d96b0ba03d8978fd499)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [net\_virtual\_input](group__virtual.md#ga6c63773925ef7d96b0ba03d8978fd499)(struct [net\_if](structnet__if.md) \*input\_iface,

249 struct net\_addr \*remote\_addr,

250 struct [net\_pkt](structnet__pkt.md) \*pkt);

251

253

260#if defined(CONFIG\_NET\_L2\_VIRTUAL)

261void net\_virtual\_init(struct [net\_if](structnet__if.md) \*iface);

262#else

263static inline void net\_virtual\_init(struct [net\_if](structnet__if.md) \*iface)

264{

265 ARG\_UNUSED(iface);

266}

267#endif

268

275#if defined(CONFIG\_NET\_L2\_VIRTUAL)

276void net\_virtual\_disable(struct [net\_if](structnet__if.md) \*iface);

277#else

278static inline void net\_virtual\_disable(struct [net\_if](structnet__if.md) \*iface)

279{

280 ARG\_UNUSED(iface);

281}

282#endif

283

290#if defined(CONFIG\_NET\_L2\_VIRTUAL)

291void net\_virtual\_enable(struct [net\_if](structnet__if.md) \*iface);

292#else

293static inline void net\_virtual\_enable(struct [net\_if](structnet__if.md) \*iface)

294{

295 ARG\_UNUSED(iface);

296}

297#endif

298

299#define VIRTUAL\_L2\_CTX\_TYPE struct virtual\_interface\_context

300

308static inline enum [virtual\_interface\_caps](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091)

309net\_virtual\_get\_iface\_capabilities(struct [net\_if](structnet__if.md) \*iface)

310{

311 const struct [virtual\_interface\_api](structvirtual__interface__api.md) \*virt =

312 (struct [virtual\_interface\_api](structvirtual__interface__api.md) \*)[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(iface)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

313

314 if (!virt->[get\_capabilities](structvirtual__interface__api.md#a827cd13d885b7cc2f80eddd73e438e07)) {

315 return (enum [virtual\_interface\_caps](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091))0;

316 }

317

318 return virt->[get\_capabilities](structvirtual__interface__api.md#a827cd13d885b7cc2f80eddd73e438e07)(iface);

319}

320

321#define Z\_NET\_VIRTUAL\_INTERFACE\_INIT(node\_id, dev\_id, name, init\_fn, \

322 pm, data, config, prio, api, mtu) \

323 Z\_NET\_DEVICE\_INIT(node\_id, dev\_id, name, init\_fn, pm, data, \

324 config, prio, api, VIRTUAL\_L2, \

325 NET\_L2\_GET\_CTX\_TYPE(VIRTUAL\_L2), mtu)

326

327#define Z\_NET\_VIRTUAL\_INTERFACE\_INIT\_INSTANCE(node\_id, dev\_id, name, \

328 inst, init\_fn, pm, data, \

329 config, prio, api, mtu) \

330 Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, dev\_id, name, inst, \

331 init\_fn, pm, data, \

332 config, prio, api, VIRTUAL\_L2, \

333 NET\_L2\_GET\_CTX\_TYPE(VIRTUAL\_L2), mtu)

335

[ 357](group__virtual.md#ga74a5c258a08397f881a8922516ac5d3a)#define NET\_VIRTUAL\_INTERFACE\_INIT(dev\_id, name, init\_fn, pm, data, \

358 config, prio, api, mtu) \

359 Z\_NET\_VIRTUAL\_INTERFACE\_INIT(DT\_INVALID\_NODE, dev\_id, name, \

360 init\_fn, pm, data, config, prio, \

361 api, mtu)

362

[ 385](group__virtual.md#ga1846d4173bcd4b40a05b70c5fde18f91)#define NET\_VIRTUAL\_INTERFACE\_INIT\_INSTANCE(dev\_id, name, inst, \

386 init\_fn, pm, data, \

387 config, prio, api, mtu) \

388 Z\_NET\_VIRTUAL\_INTERFACE\_INIT\_INSTANCE(DT\_INVALID\_NODE, dev\_id, \

389 name, inst, \

390 init\_fn, pm, data, config, \

391 prio, api, mtu)

392

396

397#ifdef \_\_cplusplus

398}

399#endif

400

401#endif /\* ZEPHYR\_INCLUDE\_NET\_VIRTUAL\_H\_ \*/

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:168

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:103

[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)

static const struct device \* net\_if\_get\_device(struct net\_if \*iface)

Get an network interface's device.

**Definition** net\_if.h:1051

[net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516)

net\_l2\_flags

L2 flags.

**Definition** net\_l2.h:37

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

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

**Definition** virtual.h:39

[net\_virtual\_get\_name](group__virtual.md#gaa7ff8ebb83fe98a1dfd23f319317a8de)

char \* net\_virtual\_get\_name(struct net\_if \*iface, char \*buf, size\_t len)

Return the name of the virtual network interface L2.

[net\_virtual\_get\_iface](group__virtual.md#gabadf14eaa02978cde7030c99ddd3e279)

struct net\_if \* net\_virtual\_get\_iface(struct net\_if \*iface)

Return network interface related to this virtual network interface.

[VIRTUAL\_INTERFACE\_IPIP](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071)

@ VIRTUAL\_INTERFACE\_IPIP

IPIP tunnel.

**Definition** virtual.h:41

[VIRTUAL\_INTERFACE\_VPN](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a145ffaeae08793e4c93ea7be320efe2b)

@ VIRTUAL\_INTERFACE\_VPN

VPN interface.

**Definition** virtual.h:50

[VIRTUAL\_INTERFACE\_BRIDGE](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a1ce35cd2b3312437b51d7440da2efaed)

@ VIRTUAL\_INTERFACE\_BRIDGE

Virtual Ethernet bridge interface.

**Definition** virtual.h:47

[VIRTUAL\_INTERFACE\_VLAN](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a5d496813292edfe8156484450fc7d83b)

@ VIRTUAL\_INTERFACE\_VLAN

Virtual LAN interface (VLAN).

**Definition** virtual.h:44

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[net\_pkt.h](net__pkt_8h.md)

Network packet buffer descriptor API.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[stdbool.h](stdbool_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:726

[net\_linkaddr](structnet__linkaddr.md)

Hardware link address structure.

**Definition** net\_linkaddr.h:70

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

[virtual\_interface\_api](structvirtual__interface__api.md)

Virtual L2 API operations.

**Definition** virtual.h:107

[virtual\_interface\_api::stop](structvirtual__interface__api.md#a09a317009d31ac5e9340c3ca7d2191c4)

int(\* stop)(const struct device \*dev)

Stop the device.

**Definition** virtual.h:121

[virtual\_interface\_api::get\_config](structvirtual__interface__api.md#a4ff5b92897926616778eb6fb696ebb16)

int(\* get\_config)(struct net\_if \*iface, enum virtual\_interface\_config\_type type, struct virtual\_interface\_config \*config)

Get specific L2 configuration.

**Definition** virtual.h:143

[virtual\_interface\_api::set\_config](structvirtual__interface__api.md#a591f1b7df5313c4a225dceaa04b1eeae)

int(\* set\_config)(struct net\_if \*iface, enum virtual\_interface\_config\_type type, const struct virtual\_interface\_config \*config)

Set specific L2 configuration.

**Definition** virtual.h:138

[virtual\_interface\_api::recv](structvirtual__interface__api.md#a6f21e33e39caa00d51cca900a26f7070)

enum net\_verdict(\* recv)(struct net\_if \*iface, struct net\_pkt \*pkt)

Receive a network packet.

**Definition** virtual.h:132

[virtual\_interface\_api::send](structvirtual__interface__api.md#a6fbfa013374bbafaa610b0a054d3a415)

int(\* send)(struct net\_if \*iface, struct net\_pkt \*pkt)

Send a network packet.

**Definition** virtual.h:124

[virtual\_interface\_api::attach](structvirtual__interface__api.md#a753258a8929347877997ca5d6a76eb8c)

int(\* attach)(struct net\_if \*virtual\_iface, struct net\_if \*iface)

Pass the attachment information to virtual interface.

**Definition** virtual.h:135

[virtual\_interface\_api::get\_capabilities](structvirtual__interface__api.md#a827cd13d885b7cc2f80eddd73e438e07)

enum virtual\_interface\_caps(\* get\_capabilities)(struct net\_if \*iface)

Get the virtual interface capabilities.

**Definition** virtual.h:115

[virtual\_interface\_api::iface\_api](structvirtual__interface__api.md#aee1250773938536ab28e129113073ae7)

struct net\_if\_api iface\_api

The net\_if\_api must be placed in first position in this struct so that we are compatible with network...

**Definition** virtual.h:112

[virtual\_interface\_api::start](structvirtual__interface__api.md#af28a6ed36799006d185fab9129c6c120)

int(\* start)(const struct device \*dev)

Start the device.

**Definition** virtual.h:118

[virtual\_interface\_context](structvirtual__interface__context.md)

Virtual L2 context that is needed to binding to the real network interface.

**Definition** virtual.h:155

[virtual\_interface\_context::virtual\_l2\_flags](structvirtual__interface__context.md#a493cef75dd5000b19eab5db156015c6e)

enum net\_l2\_flags virtual\_l2\_flags

This tells what L2 features does virtual support.

**Definition** virtual.h:174

[virtual\_interface\_context::iface](structvirtual__interface__context.md#a4a0aada1d7af7a86d2a4b12063f35c71)

struct net\_if \* iface

Other network interface this virtual network interface is attached to.

**Definition** virtual.h:169

[virtual\_interface\_context::name](structvirtual__interface__context.md#a7d53af8860331f23b8ff83ba0bfcaacf)

char name[VIRTUAL\_MAX\_NAME\_LEN]

User friendly name of this L2 layer.

**Definition** virtual.h:183

[virtual\_interface\_context::is\_init](structvirtual__interface__context.md#a7e4699c462a1edfdb755833a9ab28d8f)

bool is\_init

Is this context already initialized.

**Definition** virtual.h:177

[virtual\_interface\_context::lladdr](structvirtual__interface__context.md#ade8a686b9c002c064e2ae9e1815b6601)

struct net\_linkaddr lladdr

Link address for this network interface.

**Definition** virtual.h:180

[atomic.h](sys_2atomic_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [virtual.h](virtual_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
