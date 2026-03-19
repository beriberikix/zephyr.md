---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__icmp.html
original_path: doxygen/html/group__icmp.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Send and receive IPv4 or IPv6 ICMP Echo Request messages.

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

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
| #define | [NET\_ICMPV4\_ECHO\_REQUEST](#gab09cfc243ae8aea120c2da9e77b3154f)   8 |
|  | ICMPv4 Echo-Request. |
| #define | [NET\_ICMPV4\_ECHO\_REPLY](#ga34b93cc7084276868f2b635021aad53b)   0 |
|  | ICMPv4 Echo-Reply. |
| #define | [NET\_ICMPV6\_ECHO\_REQUEST](#ga30ba68bc2372c6253ebce3db452591b3)   128 |
|  | ICMPv6 Echo-Request. |
| #define | [NET\_ICMPV6\_ECHO\_REPLY](#ga88187908775c5b84ec183f645454ac76)   129 |
|  | ICMPv6 Echo-Reply. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [net\_icmp\_handler\_t](#ga0c3bd8147e4664ca0557ef0f118117ff)) (struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx, struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_icmp\_ip\_hdr](structnet__icmp__ip__hdr.md) \*ip\_hdr, struct net\_icmp\_hdr \*icmp\_hdr, void \*user\_data) |
|  | Handler function that is called when ICMP response is received. |
| typedef int(\* | [net\_icmp\_offload\_ping\_handler\_t](#ga2923024c2ab217eb6b0fb1371a597dde)) (struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx, struct [net\_if](structnet__if.md) \*iface, struct [sockaddr](structsockaddr.md) \*dst, struct [net\_icmp\_ping\_params](structnet__icmp__ping__params.md) \*params, void \*user\_data) |
|  | Handler function that is called when an Echo-Request is sent to offloaded device. |

| Functions | |
| --- | --- |
| int | [net\_icmp\_init\_ctx](#gad393c5444b6d949c6329c210dd33110c) (struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code, [net\_icmp\_handler\_t](#ga0c3bd8147e4664ca0557ef0f118117ff) handler) |
|  | Initialize the ICMP context structure. |
| int | [net\_icmp\_cleanup\_ctx](#gab90fe71303498c127f1f093d78d16ffa) (struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx) |
|  | Cleanup the ICMP context structure. |
| int | [net\_icmp\_send\_echo\_request](#ga3770c94a08fd6ab112472d138f276b25) (struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx, struct [net\_if](structnet__if.md) \*iface, struct [sockaddr](structsockaddr.md) \*dst, struct [net\_icmp\_ping\_params](structnet__icmp__ping__params.md) \*params, void \*user\_data) |
|  | Send ICMP echo request message. |
| int | [net\_icmp\_register\_offload\_ping](#ga6cec9e51d91483c33deae86f24e582ae) (struct [net\_icmp\_offload](structnet__icmp__offload.md) \*ctx, struct [net\_if](structnet__if.md) \*iface, [net\_icmp\_offload\_ping\_handler\_t](#ga2923024c2ab217eb6b0fb1371a597dde) ping\_handler) |
|  | Register a handler function that is called when an Echo-Request is sent to the offloaded device. |
| int | [net\_icmp\_unregister\_offload\_ping](#ga75f993c1f04d67c63689b5a6e1046d62) (struct [net\_icmp\_offload](structnet__icmp__offload.md) \*ctx) |
|  | Unregister the offload handler. |
| int | [net\_icmp\_get\_offload\_rsp\_handler](#gad18ca68c320d977abaa3b757c4a1e5b0) (struct [net\_icmp\_offload](structnet__icmp__offload.md) \*ctx, [net\_icmp\_handler\_t](#ga0c3bd8147e4664ca0557ef0f118117ff) \*resp\_handler) |
|  | Get a ICMP response handler function for an offloaded device. |

## Detailed Description

Since
:   3.5

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#ga34b93cc7084276868f2b635021aad53b)NET\_ICMPV4\_ECHO\_REPLY

| #define NET\_ICMPV4\_ECHO\_REPLY   0 |
| --- |

`#include <[icmp.h](icmp_8h.md)>`

ICMPv4 Echo-Reply.

## [◆ ](#gab09cfc243ae8aea120c2da9e77b3154f)NET\_ICMPV4\_ECHO\_REQUEST

| #define NET\_ICMPV4\_ECHO\_REQUEST   8 |
| --- |

`#include <[icmp.h](icmp_8h.md)>`

ICMPv4 Echo-Request.

## [◆ ](#ga88187908775c5b84ec183f645454ac76)NET\_ICMPV6\_ECHO\_REPLY

| #define NET\_ICMPV6\_ECHO\_REPLY   129 |
| --- |

`#include <[icmp.h](icmp_8h.md)>`

ICMPv6 Echo-Reply.

## [◆ ](#ga30ba68bc2372c6253ebce3db452591b3)NET\_ICMPV6\_ECHO\_REQUEST

| #define NET\_ICMPV6\_ECHO\_REQUEST   128 |
| --- |

`#include <[icmp.h](icmp_8h.md)>`

ICMPv6 Echo-Request.

## Typedef Documentation

## [◆ ](#ga0c3bd8147e4664ca0557ef0f118117ff)net\_icmp\_handler\_t

| typedef int(\* net\_icmp\_handler\_t) (struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx, struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_icmp\_ip\_hdr](structnet__icmp__ip__hdr.md) \*ip\_hdr, struct net\_icmp\_hdr \*icmp\_hdr, void \*user\_data) |
| --- |

`#include <[icmp.h](icmp_8h.md)>`

Handler function that is called when ICMP response is received.

Parameters
:   | ctx | ICMP context to use. |
    | --- | --- |
    | pkt | Received ICMP response network packet. |
    | ip\_hdr | IP header of the packet. |
    | icmp\_hdr | ICMP header of the packet. |
    | user\_data | A valid pointer to user data or NULL |

## [◆ ](#ga2923024c2ab217eb6b0fb1371a597dde)net\_icmp\_offload\_ping\_handler\_t

| typedef int(\* net\_icmp\_offload\_ping\_handler\_t) (struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \*ctx, struct [net\_if](structnet__if.md) \*iface, struct [sockaddr](structsockaddr.md) \*dst, struct [net\_icmp\_ping\_params](structnet__icmp__ping__params.md) \*params, void \*user\_data) |
| --- |

`#include <[icmp.h](icmp_8h.md)>`

Handler function that is called when an Echo-Request is sent to offloaded device.

This handler is typically setup by the device driver so that it can catch the ping request and send it to the offloaded device.

Parameters
:   | ctx | ICMP context used in this request. |
    | --- | --- |
    | iface | Network interface, can be set to NULL in which case the interface is selected according to destination address. |
    | dst | IP address of the target host. |
    | params | Echo-Request specific parameters. May be NULL in which case suitable default parameters are used. |
    | user\_data | User supplied opaque data passed to the handler. May be NULL. |

## Function Documentation

## [◆ ](#gab90fe71303498c127f1f093d78d16ffa)net\_icmp\_cleanup\_ctx()

| int net\_icmp\_cleanup\_ctx | ( | struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[icmp.h](icmp_8h.md)>`

Cleanup the ICMP context structure.

This will unregister the ICMP handler from the system.

Parameters
:   | ctx | ICMP context used in this request. |
    | --- | --- |

## [◆ ](#gad18ca68c320d977abaa3b757c4a1e5b0)net\_icmp\_get\_offload\_rsp\_handler()

| int net\_icmp\_get\_offload\_rsp\_handler | ( | struct [net\_icmp\_offload](structnet__icmp__offload.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [net\_icmp\_handler\_t](#ga0c3bd8147e4664ca0557ef0f118117ff) \* | *resp\_handler* ) |

`#include <[icmp.h](icmp_8h.md)>`

Get a ICMP response handler function for an offloaded device.

When a ping response is received by the driver, it should call the handler function with proper parameters so that the ICMP response is received by the net stack.

Parameters
:   | ctx | ICMP offload context used in this request. |
    | --- | --- |
    | resp\_handler | Function to be called when offloaded ping response is received by the offloaded driver. The ICMP response handler function is returned and the caller should call it when appropriate. |

Returns
:   Return 0 if the call succeed, <0 otherwise.

## [◆ ](#gad393c5444b6d949c6329c210dd33110c)net\_icmp\_init\_ctx()

| int net\_icmp\_init\_ctx | ( | struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *type*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *code*, |
|  |  | [net\_icmp\_handler\_t](#ga0c3bd8147e4664ca0557ef0f118117ff) | *handler* ) |

`#include <[icmp.h](icmp_8h.md)>`

Initialize the ICMP context structure.

Must be called before ICMP messages can be sent. This will register handler to the system.

Parameters
:   | ctx | ICMP context used in this request. |
    | --- | --- |
    | type | Type of ICMP message we are handling. |
    | code | Code of ICMP message we are handling. |
    | handler | Callback function that is called when a response is received. |

## [◆ ](#ga6cec9e51d91483c33deae86f24e582ae)net\_icmp\_register\_offload\_ping()

| int net\_icmp\_register\_offload\_ping | ( | struct [net\_icmp\_offload](structnet__icmp__offload.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \* | *iface*, |
|  |  | [net\_icmp\_offload\_ping\_handler\_t](#ga2923024c2ab217eb6b0fb1371a597dde) | *ping\_handler* ) |

`#include <[icmp.h](icmp_8h.md)>`

Register a handler function that is called when an Echo-Request is sent to the offloaded device.

This function is typically called by a device driver so that it can do the actual offloaded ping call.

Parameters
:   | ctx | ICMP offload context used for this interface. |
    | --- | --- |
    | iface | Network interface of the offloaded device. |
    | ping\_handler | Function to be called when offloaded ping request is done. |

Returns
:   Return 0 if the register succeed, <0 otherwise.

## [◆ ](#ga3770c94a08fd6ab112472d138f276b25)net\_icmp\_send\_echo\_request()

| int net\_icmp\_send\_echo\_request | ( | struct [net\_icmp\_ctx](structnet__icmp__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \* | *iface*, |
|  |  | struct [sockaddr](structsockaddr.md) \* | *dst*, |
|  |  | struct [net\_icmp\_ping\_params](structnet__icmp__ping__params.md) \* | *params*, |
|  |  | void \* | *user\_data* ) |

`#include <[icmp.h](icmp_8h.md)>`

Send ICMP echo request message.

Parameters
:   | ctx | ICMP context used in this request. |
    | --- | --- |
    | iface | Network interface, can be set to NULL in which case the interface is selected according to destination address. |
    | dst | IP address of the target host. |
    | params | Echo-Request specific parameters. May be NULL in which case suitable default parameters are used. |
    | user\_data | User supplied opaque data passed to the handler. May be NULL. |

Returns
:   Return 0 if the sending succeed, <0 otherwise.

## [◆ ](#ga75f993c1f04d67c63689b5a6e1046d62)net\_icmp\_unregister\_offload\_ping()

| int net\_icmp\_unregister\_offload\_ping | ( | struct [net\_icmp\_offload](structnet__icmp__offload.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[icmp.h](icmp_8h.md)>`

Unregister the offload handler.

Parameters
:   | ctx | ICMP offload context used for this interface. |
    | --- | --- |

Returns
:   Return 0 if the call succeed, <0 otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
