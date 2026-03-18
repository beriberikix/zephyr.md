---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/icmp_8h.html
original_path: doxygen/html/icmp_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icmp.h File Reference

ICMP sending and receiving.
[More...](#details)

`#include <stddef.h>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/net_pkt.h](net__pkt_8h_source.md)>`

[Go to the source code of this file.](icmp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_icmp\_ctx](structnet__icmp__ctx.md) |
|  | ICMP context structure. [More...](structnet__icmp__ctx.md#details) |
| struct | [net\_icmp\_ip\_hdr](structnet__icmp__ip__hdr.md) |
|  | Struct presents either IPv4 or IPv6 header in ICMP response message. [More...](structnet__icmp__ip__hdr.md#details) |
| struct | [net\_icmp\_ping\_params](structnet__icmp__ping__params.md) |
|  | Struct presents parameters that are needed when sending Echo-Request (ping) messages. [More...](structnet__icmp__ping__params.md#details) |
| struct | [net\_icmp\_offload](structnet__icmp__offload.md) |
|  | ICMP offload context structure. [More...](structnet__icmp__offload.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_ICMPV4\_ECHO\_REQUEST](group__icmp.md#gab09cfc243ae8aea120c2da9e77b3154f)   8 |
|  | ICMPv4 Echo-Request. |
| #define | [NET\_ICMPV4\_ECHO\_REPLY](group__icmp.md#ga34b93cc7084276868f2b635021aad53b)   0 |
|  | ICMPv4 Echo-Reply. |
| #define | [NET\_ICMPV6\_ECHO\_REQUEST](group__icmp.md#ga30ba68bc2372c6253ebce3db452591b3)   128 |
|  | ICMPv6 Echo-Request. |
| #define | [NET\_ICMPV6\_ECHO\_REPLY](group__icmp.md#ga88187908775c5b84ec183f645454ac76)   129 |
|  | ICMPv6 Echo-Reply. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff)) (struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx, struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_icmp\_ip\_hdr](structnet__icmp__ip__hdr.md) \*ip\_hdr, struct net\_icmp\_hdr \*icmp\_hdr, void \*user\_data) |
|  | Handler function that is called when ICMP response is received. |
| typedef int(\* | [net\_icmp\_offload\_ping\_handler\_t](group__icmp.md#ga2923024c2ab217eb6b0fb1371a597dde)) (struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx, struct [net\_if](structnet__if.md) \*iface, struct [sockaddr](structsockaddr.md) \*dst, struct [net\_icmp\_ping\_params](structnet__icmp__ping__params.md) \*params, void \*user\_data) |
|  | Handler function that is called when an Echo-Request is sent to offloaded device. |

| Functions | |
| --- | --- |
| int | [net\_icmp\_init\_ctx](group__icmp.md#gad393c5444b6d949c6329c210dd33110c) (struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code, [net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff) handler) |
|  | Initialize the ICMP context structure. |
| int | [net\_icmp\_cleanup\_ctx](group__icmp.md#gab90fe71303498c127f1f093d78d16ffa) (struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx) |
|  | Cleanup the ICMP context structure. |
| int | [net\_icmp\_send\_echo\_request](group__icmp.md#ga3770c94a08fd6ab112472d138f276b25) (struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx, struct [net\_if](structnet__if.md) \*iface, struct [sockaddr](structsockaddr.md) \*dst, struct [net\_icmp\_ping\_params](structnet__icmp__ping__params.md) \*params, void \*user\_data) |
|  | Send ICMP echo request message. |
| int | [net\_icmp\_register\_offload\_ping](group__icmp.md#ga6cec9e51d91483c33deae86f24e582ae) (struct [net\_icmp\_offload](structnet__icmp__offload.md) \*ctx, struct [net\_if](structnet__if.md) \*iface, [net\_icmp\_offload\_ping\_handler\_t](group__icmp.md#ga2923024c2ab217eb6b0fb1371a597dde) ping\_handler) |
|  | Register a handler function that is called when an Echo-Request is sent to the offloaded device. |
| int | [net\_icmp\_unregister\_offload\_ping](group__icmp.md#ga75f993c1f04d67c63689b5a6e1046d62) (struct [net\_icmp\_offload](structnet__icmp__offload.md) \*ctx) |
|  | Unregister the offload handler. |
| int | [net\_icmp\_get\_offload\_rsp\_handler](group__icmp.md#gad18ca68c320d977abaa3b757c4a1e5b0) (struct [net\_icmp\_offload](structnet__icmp__offload.md) \*ctx, [net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff) \*resp\_handler) |
|  | Get a ICMP response handler function for an offloaded device. |

## Detailed Description

ICMP sending and receiving.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [icmp.h](icmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
