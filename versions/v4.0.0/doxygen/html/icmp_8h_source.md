---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/icmp_8h_source.html
original_path: doxygen/html/icmp_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icmp.h

[Go to the documentation of this file.](icmp_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

17

18#ifndef ZEPHYR\_INCLUDE\_NET\_ICMP\_H\_

19#define ZEPHYR\_INCLUDE\_NET\_ICMP\_H\_

20

21#include <stddef.h>

22

23#include <[zephyr/kernel.h](kernel_8h.md)>

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

26#include <[zephyr/net/net\_if.h](net__if_8h.md)>

27#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 33](group__icmp.md#gab09cfc243ae8aea120c2da9e77b3154f)#define NET\_ICMPV4\_ECHO\_REQUEST 8

[ 34](group__icmp.md#ga34b93cc7084276868f2b635021aad53b)#define NET\_ICMPV4\_ECHO\_REPLY 0

[ 35](group__icmp.md#ga30ba68bc2372c6253ebce3db452591b3)#define NET\_ICMPV6\_ECHO\_REQUEST 128

[ 36](group__icmp.md#ga88187908775c5b84ec183f645454ac76)#define NET\_ICMPV6\_ECHO\_REPLY 129

37

38struct [net\_icmp\_ctx](structnet__icmp__ctx.md);

39struct [net\_icmp\_ip\_hdr](structnet__icmp__ip__hdr.md);

40struct [net\_icmp\_ping\_params](structnet__icmp__ping__params.md);

41

[ 52](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff)typedef int (\*[net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff))(struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx,

53 struct [net\_pkt](structnet__pkt.md) \*pkt,

54 struct [net\_icmp\_ip\_hdr](structnet__icmp__ip__hdr.md) \*ip\_hdr,

55 struct net\_icmp\_hdr \*icmp\_hdr,

56 void \*user\_data);

57

[ 74](group__icmp.md#ga2923024c2ab217eb6b0fb1371a597dde)typedef int (\*[net\_icmp\_offload\_ping\_handler\_t](group__icmp.md#ga2923024c2ab217eb6b0fb1371a597dde))(struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx,

75 struct [net\_if](structnet__if.md) \*iface,

76 struct [sockaddr](structsockaddr.md) \*dst,

77 struct [net\_icmp\_ping\_params](structnet__icmp__ping__params.md) \*params,

78 void \*user\_data);

79

[ 83](structnet__icmp__ctx.md)struct [net\_icmp\_ctx](structnet__icmp__ctx.md) {

[ 85](structnet__icmp__ctx.md#a792d11b7dc74b0c064e5471f385028e5) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__icmp__ctx.md#a792d11b7dc74b0c064e5471f385028e5);

86

[ 88](structnet__icmp__ctx.md#a9da78845a12a69a359087607e11f7e72) [net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff) [handler](structnet__icmp__ctx.md#a9da78845a12a69a359087607e11f7e72);

89

[ 91](structnet__icmp__ctx.md#a88e1f3dc6118366f37ff5a110fff4b08) struct [net\_if](structnet__if.md) \*[iface](structnet__icmp__ctx.md#a88e1f3dc6118366f37ff5a110fff4b08);

92

[ 94](structnet__icmp__ctx.md#a2a718521d0b8c6de45c39fc8b45e47cf) void \*[user\_data](structnet__icmp__ctx.md#a2a718521d0b8c6de45c39fc8b45e47cf);

95

[ 97](structnet__icmp__ctx.md#ae7ccf9c7bbcc89d656d20e9486cf7df5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structnet__icmp__ctx.md#ae7ccf9c7bbcc89d656d20e9486cf7df5);

98

[ 100](structnet__icmp__ctx.md#a8eaa061d7ade479523cfdbcb465f76b2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [code](structnet__icmp__ctx.md#a8eaa061d7ade479523cfdbcb465f76b2);

101};

102

[ 106](structnet__icmp__ip__hdr.md)struct [net\_icmp\_ip\_hdr](structnet__icmp__ip__hdr.md) {

107 union {

[ 109](structnet__icmp__ip__hdr.md#a3d0d8b7442611c74a71a72ab1d1c7a90) struct net\_ipv4\_hdr \*[ipv4](structnet__icmp__ip__hdr.md#a3d0d8b7442611c74a71a72ab1d1c7a90);

110

[ 112](structnet__icmp__ip__hdr.md#ac993b71afdd637dba048ba5038d489c8) struct net\_ipv6\_hdr \*[ipv6](structnet__icmp__ip__hdr.md#ac993b71afdd637dba048ba5038d489c8);

113 };

114

[ 116](structnet__icmp__ip__hdr.md#a4e0f7c9694ed1c7bfafc0d73d7447b26) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [family](structnet__icmp__ip__hdr.md#a4e0f7c9694ed1c7bfafc0d73d7447b26);

117};

118

[ 123](structnet__icmp__ping__params.md)struct [net\_icmp\_ping\_params](structnet__icmp__ping__params.md) {

[ 127](structnet__icmp__ping__params.md#a138d6de6072ebbf3ae454eb3ee28b138) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [identifier](structnet__icmp__ping__params.md#a138d6de6072ebbf3ae454eb3ee28b138);

128

[ 132](structnet__icmp__ping__params.md#a3756461b95ce1b7fde9d59819de10d85) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sequence](structnet__icmp__ping__params.md#a3756461b95ce1b7fde9d59819de10d85);

133

[ 137](structnet__icmp__ping__params.md#aaf5a9493b5d98f72bb27758fd24c64ec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tc\_tos](structnet__icmp__ping__params.md#aaf5a9493b5d98f72bb27758fd24c64ec);

138

[ 140](structnet__icmp__ping__params.md#a3a9abdb27bfb94ca6515e280bf6bee3c) int [priority](structnet__icmp__ping__params.md#a3a9abdb27bfb94ca6515e280bf6bee3c);

141

[ 145](structnet__icmp__ping__params.md#ac2247bc63eea000200429f0f441031bf) const void \*[data](structnet__icmp__ping__params.md#ac2247bc63eea000200429f0f441031bf);

146

[ 151](structnet__icmp__ping__params.md#a342b75123a32e35f91bda3e11601598b) size\_t [data\_size](structnet__icmp__ping__params.md#a342b75123a32e35f91bda3e11601598b);

152};

153

[ 164](group__icmp.md#gad393c5444b6d949c6329c210dd33110c)int [net\_icmp\_init\_ctx](group__icmp.md#gad393c5444b6d949c6329c210dd33110c)(struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code,

165 [net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff) handler);

166

[ 173](group__icmp.md#gab90fe71303498c127f1f093d78d16ffa)int [net\_icmp\_cleanup\_ctx](group__icmp.md#gab90fe71303498c127f1f093d78d16ffa)(struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx);

174

[ 188](group__icmp.md#ga3770c94a08fd6ab112472d138f276b25)int [net\_icmp\_send\_echo\_request](group__icmp.md#ga3770c94a08fd6ab112472d138f276b25)(struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx,

189 struct [net\_if](structnet__if.md) \*iface,

190 struct [sockaddr](structsockaddr.md) \*dst,

191 struct [net\_icmp\_ping\_params](structnet__icmp__ping__params.md) \*params,

192 void \*user\_data);

193

[ 197](structnet__icmp__offload.md)struct [net\_icmp\_offload](structnet__icmp__offload.md) {

[ 199](structnet__icmp__offload.md#ae31036c45fac89b321fe2c62c06be0b3) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__icmp__offload.md#ae31036c45fac89b321fe2c62c06be0b3);

200

[ 206](structnet__icmp__offload.md#aad5c9913e8bf68a7453bc773c5784772) [net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff) [handler](structnet__icmp__offload.md#aad5c9913e8bf68a7453bc773c5784772);

207

[ 209](structnet__icmp__offload.md#ae28f8f6a0e15271b1f00b10abecdfc3e) [net\_icmp\_offload\_ping\_handler\_t](group__icmp.md#ga2923024c2ab217eb6b0fb1371a597dde) [ping\_handler](structnet__icmp__offload.md#ae28f8f6a0e15271b1f00b10abecdfc3e);

210

[ 212](structnet__icmp__offload.md#aeffe11b4701e58532e44b4cff37be680) struct [net\_if](structnet__if.md) \*[iface](structnet__icmp__offload.md#aeffe11b4701e58532e44b4cff37be680);

213};

214

[ 227](group__icmp.md#ga6cec9e51d91483c33deae86f24e582ae)int [net\_icmp\_register\_offload\_ping](group__icmp.md#ga6cec9e51d91483c33deae86f24e582ae)(struct [net\_icmp\_offload](structnet__icmp__offload.md) \*ctx,

228 struct [net\_if](structnet__if.md) \*iface,

229 [net\_icmp\_offload\_ping\_handler\_t](group__icmp.md#ga2923024c2ab217eb6b0fb1371a597dde) ping\_handler);

230

[ 238](group__icmp.md#ga75f993c1f04d67c63689b5a6e1046d62)int [net\_icmp\_unregister\_offload\_ping](group__icmp.md#ga75f993c1f04d67c63689b5a6e1046d62)(struct [net\_icmp\_offload](structnet__icmp__offload.md) \*ctx);

239

[ 253](group__icmp.md#gad18ca68c320d977abaa3b757c4a1e5b0)int [net\_icmp\_get\_offload\_rsp\_handler](group__icmp.md#gad18ca68c320d977abaa3b757c4a1e5b0)(struct [net\_icmp\_offload](structnet__icmp__offload.md) \*ctx,

254 [net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff) \*resp\_handler);

255

256#ifdef \_\_cplusplus

257}

258#endif

259

260#endif /\* ZEPHYR\_INCLUDE\_NET\_ICMP\_H \*/

261

[net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff)

int(\* net\_icmp\_handler\_t)(struct net\_icmp\_ctx \*ctx, struct net\_pkt \*pkt, struct net\_icmp\_ip\_hdr \*ip\_hdr, struct net\_icmp\_hdr \*icmp\_hdr, void \*user\_data)

Handler function that is called when ICMP response is received.

**Definition** icmp.h:52

[net\_icmp\_offload\_ping\_handler\_t](group__icmp.md#ga2923024c2ab217eb6b0fb1371a597dde)

int(\* net\_icmp\_offload\_ping\_handler\_t)(struct net\_icmp\_ctx \*ctx, struct net\_if \*iface, struct sockaddr \*dst, struct net\_icmp\_ping\_params \*params, void \*user\_data)

Handler function that is called when an Echo-Request is sent to offloaded device.

**Definition** icmp.h:74

[net\_icmp\_send\_echo\_request](group__icmp.md#ga3770c94a08fd6ab112472d138f276b25)

int net\_icmp\_send\_echo\_request(struct net\_icmp\_ctx \*ctx, struct net\_if \*iface, struct sockaddr \*dst, struct net\_icmp\_ping\_params \*params, void \*user\_data)

Send ICMP echo request message.

[net\_icmp\_register\_offload\_ping](group__icmp.md#ga6cec9e51d91483c33deae86f24e582ae)

int net\_icmp\_register\_offload\_ping(struct net\_icmp\_offload \*ctx, struct net\_if \*iface, net\_icmp\_offload\_ping\_handler\_t ping\_handler)

Register a handler function that is called when an Echo-Request is sent to the offloaded device.

[net\_icmp\_unregister\_offload\_ping](group__icmp.md#ga75f993c1f04d67c63689b5a6e1046d62)

int net\_icmp\_unregister\_offload\_ping(struct net\_icmp\_offload \*ctx)

Unregister the offload handler.

[net\_icmp\_cleanup\_ctx](group__icmp.md#gab90fe71303498c127f1f093d78d16ffa)

int net\_icmp\_cleanup\_ctx(struct net\_icmp\_ctx \*ctx)

Cleanup the ICMP context structure.

[net\_icmp\_get\_offload\_rsp\_handler](group__icmp.md#gad18ca68c320d977abaa3b757c4a1e5b0)

int net\_icmp\_get\_offload\_rsp\_handler(struct net\_icmp\_offload \*ctx, net\_icmp\_handler\_t \*resp\_handler)

Get a ICMP response handler function for an offloaded device.

[net\_icmp\_init\_ctx](group__icmp.md#gad393c5444b6d949c6329c210dd33110c)

int net\_icmp\_init\_ctx(struct net\_icmp\_ctx \*ctx, uint8\_t type, uint8\_t code, net\_icmp\_handler\_t handler)

Initialize the ICMP context structure.

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:167

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[net\_pkt.h](net__pkt_8h.md)

Network packet buffer descriptor API.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[net\_icmp\_ctx](structnet__icmp__ctx.md)

ICMP context structure.

**Definition** icmp.h:83

[net\_icmp\_ctx::user\_data](structnet__icmp__ctx.md#a2a718521d0b8c6de45c39fc8b45e47cf)

void \* user\_data

Opaque user supplied data.

**Definition** icmp.h:94

[net\_icmp\_ctx::node](structnet__icmp__ctx.md#a792d11b7dc74b0c064e5471f385028e5)

sys\_snode\_t node

List node.

**Definition** icmp.h:85

[net\_icmp\_ctx::iface](structnet__icmp__ctx.md#a88e1f3dc6118366f37ff5a110fff4b08)

struct net\_if \* iface

Network interface where the ICMP request was sent.

**Definition** icmp.h:91

[net\_icmp\_ctx::code](structnet__icmp__ctx.md#a8eaa061d7ade479523cfdbcb465f76b2)

uint8\_t code

ICMP code of the response type we are waiting.

**Definition** icmp.h:100

[net\_icmp\_ctx::handler](structnet__icmp__ctx.md#a9da78845a12a69a359087607e11f7e72)

net\_icmp\_handler\_t handler

ICMP response handler.

**Definition** icmp.h:88

[net\_icmp\_ctx::type](structnet__icmp__ctx.md#ae7ccf9c7bbcc89d656d20e9486cf7df5)

uint8\_t type

ICMP type of the response we are waiting.

**Definition** icmp.h:97

[net\_icmp\_ip\_hdr](structnet__icmp__ip__hdr.md)

Struct presents either IPv4 or IPv6 header in ICMP response message.

**Definition** icmp.h:106

[net\_icmp\_ip\_hdr::ipv4](structnet__icmp__ip__hdr.md#a3d0d8b7442611c74a71a72ab1d1c7a90)

struct net\_ipv4\_hdr \* ipv4

IPv4 header in response message.

**Definition** icmp.h:109

[net\_icmp\_ip\_hdr::family](structnet__icmp__ip__hdr.md#a4e0f7c9694ed1c7bfafc0d73d7447b26)

sa\_family\_t family

Is the header IPv4 or IPv6 one.

**Definition** icmp.h:116

[net\_icmp\_ip\_hdr::ipv6](structnet__icmp__ip__hdr.md#ac993b71afdd637dba048ba5038d489c8)

struct net\_ipv6\_hdr \* ipv6

IPv6 header in response message.

**Definition** icmp.h:112

[net\_icmp\_offload](structnet__icmp__offload.md)

ICMP offload context structure.

**Definition** icmp.h:197

[net\_icmp\_offload::handler](structnet__icmp__offload.md#aad5c9913e8bf68a7453bc773c5784772)

net\_icmp\_handler\_t handler

ICMP response handler.

**Definition** icmp.h:206

[net\_icmp\_offload::ping\_handler](structnet__icmp__offload.md#ae28f8f6a0e15271b1f00b10abecdfc3e)

net\_icmp\_offload\_ping\_handler\_t ping\_handler

ICMP offloaded ping handler.

**Definition** icmp.h:209

[net\_icmp\_offload::node](structnet__icmp__offload.md#ae31036c45fac89b321fe2c62c06be0b3)

sys\_snode\_t node

List node.

**Definition** icmp.h:199

[net\_icmp\_offload::iface](structnet__icmp__offload.md#aeffe11b4701e58532e44b4cff37be680)

struct net\_if \* iface

Offloaded network interface.

**Definition** icmp.h:212

[net\_icmp\_ping\_params](structnet__icmp__ping__params.md)

Struct presents parameters that are needed when sending Echo-Request (ping) messages.

**Definition** icmp.h:123

[net\_icmp\_ping\_params::identifier](structnet__icmp__ping__params.md#a138d6de6072ebbf3ae454eb3ee28b138)

uint16\_t identifier

An identifier to aid in matching Echo Replies to this Echo Request.

**Definition** icmp.h:127

[net\_icmp\_ping\_params::data\_size](structnet__icmp__ping__params.md#a342b75123a32e35f91bda3e11601598b)

size\_t data\_size

Size of the Payload Data in bytes.

**Definition** icmp.h:151

[net\_icmp\_ping\_params::sequence](structnet__icmp__ping__params.md#a3756461b95ce1b7fde9d59819de10d85)

uint16\_t sequence

A sequence number to aid in matching Echo Replies to this Echo Request.

**Definition** icmp.h:132

[net\_icmp\_ping\_params::priority](structnet__icmp__ping__params.md#a3a9abdb27bfb94ca6515e280bf6bee3c)

int priority

Network packet priority.

**Definition** icmp.h:140

[net\_icmp\_ping\_params::tc\_tos](structnet__icmp__ping__params.md#aaf5a9493b5d98f72bb27758fd24c64ec)

uint8\_t tc\_tos

Can be either IPv4 Type-of-service field value, or IPv6 Traffic Class field value.

**Definition** icmp.h:137

[net\_icmp\_ping\_params::data](structnet__icmp__ping__params.md#ac2247bc63eea000200429f0f441031bf)

const void \* data

Arbitrary payload data that will be included in the Echo Reply verbatim.

**Definition** icmp.h:145

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:388

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [icmp.h](icmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
