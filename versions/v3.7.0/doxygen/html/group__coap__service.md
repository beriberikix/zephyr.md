---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__coap__service.html
original_path: doxygen/html/group__coap__service.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

CoAP service API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

CoAP Service API.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [COAP\_RESOURCE\_DEFINE](#gaef40d300170926ad131d06ce62c63d6a)(\_name, \_service, ...) |
|  | Define a static CoAP resource owned by the service named `_service` . |
| #define | [COAP\_SERVICE\_DEFINE](#ga8dc5473755efd48548ec4cb6ac2584ec)(\_name, \_host, \_port, \_flags) |
|  | Define a CoAP service with static resources. |
| #define | [COAP\_SERVICE\_COUNT](#ga1f0c3bf81baa9da11197a74415d3a9ae)(\_dst) |
|  | Count the number of CoAP services. |
| #define | [COAP\_SERVICE\_RESOURCE\_COUNT](#gade9e9a55968a5ad6b3addbb08f2ccb6f)(\_service) |
|  | Count CoAP service static resources. |
| #define | [COAP\_SERVICE\_HAS\_RESOURCE](#gaf01cb4d11b18272eb27be93cb1a7197b)(\_service, \_resource) |
|  | Check if service has the specified resource. |
| #define | [COAP\_SERVICE\_FOREACH](#gab4d154d5b02235a83c7a2c681b1e22e7)(\_it) |
|  | Iterate over all CoAP services. |
| #define | [COAP\_RESOURCE\_FOREACH](#gac3e92107fa12b111771d56987a242b1a)(\_service, \_it) |
|  | Iterate over static CoAP resources associated with a given `_service`. |
| #define | [COAP\_SERVICE\_FOREACH\_RESOURCE](#gaaca92287c495f4afb79e584c47316037)(\_service, \_it) |
|  | Iterate over all static resources associated with `_service` . |

| Functions | |
| --- | --- |
| int | [coap\_service\_start](#gad1e64f8fe2c6ae32730a9a61f8351bab) (const struct coap\_service \*service) |
|  | Start the provided `service` . |
| int | [coap\_service\_stop](#ga58bc31fc4d53ebce9c18ccbc5aab72ce) (const struct coap\_service \*service) |
|  | Stop the provided `service` . |
| int | [coap\_service\_is\_running](#ga08638f2001ca2f807489c12ff426784c) (const struct coap\_service \*service) |
|  | Query the provided `service` running state. |
| int | [coap\_service\_send](#gad4254ddb71400026211fe8a6da05b2be) (const struct coap\_service \*service, const struct [coap\_packet](structcoap__packet.md) \*cpkt, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len, const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params) |
|  | Send a CoAP message from the provided `service` . |
| int | [coap\_resource\_send](#ga67e2cebcfa83f6d11dc335de5dc51a47) (const struct [coap\_resource](structcoap__resource.md) \*resource, const struct [coap\_packet](structcoap__packet.md) \*cpkt, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len, const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params) |
|  | Send a CoAP message from the provided `resource` . |
| int | [coap\_resource\_parse\_observe](#ga098e08b3bc809499b789b890b67cacd5) (struct [coap\_resource](structcoap__resource.md) \*resource, const struct [coap\_packet](structcoap__packet.md) \*request, const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Parse a CoAP observe request for the provided `resource` . |
| int | [coap\_resource\_remove\_observer\_by\_addr](#ga8d9ab0bf6b1ea15408f1c80c45aae16b) (struct [coap\_resource](structcoap__resource.md) \*resource, const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Lookup an observer by address and remove it from the `resource` . |
| int | [coap\_resource\_remove\_observer\_by\_token](#gad575a7209a56874002c540eb3f8c0733) (struct [coap\_resource](structcoap__resource.md) \*resource, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len) |
|  | Lookup an observer by token and remove it from the `resource` . |

| CoAP Service configuration flags | |
| --- | --- |
|  | |
| #define | [COAP\_SERVICE\_AUTOSTART](#gaf5799a7fbf309f8963d22039a6fe2fbb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Start the service on boot. |

## Detailed Description

CoAP Service API.

## Macro Definition Documentation

## [◆ ](#gaef40d300170926ad131d06ce62c63d6a)COAP\_RESOURCE\_DEFINE

| #define COAP\_RESOURCE\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_service*, |
|  |  |  | ... ) |

`#include <[coap_service.h](coap__service_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE\_ALTERNATE](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)(coap\_resource\_##\_service, [coap\_resource](structcoap__resource.md), \_name) \

= \_\_VA\_ARGS\_\_

[STRUCT\_SECTION\_ITERABLE\_ALTERNATE](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)

#define STRUCT\_SECTION\_ITERABLE\_ALTERNATE(secname, struct\_type, varname)

Defines a new element of alternate data type for an iterable section.

**Definition** iterable\_sections.h:188

[coap\_resource](structcoap__resource.md)

Description of CoAP resource.

**Definition** coap.h:263

Define a static CoAP resource owned by the service named `_service` .

Note
:   The handlers registered with the resource can return a CoAP response code to reply with an acknowledge without any payload, nothing is sent if the return value is 0 or negative. As seen in the example.

static const struct [gpio\_dt\_spec](structgpio__dt__spec.md) led = [GPIO\_DT\_SPEC\_GET](group__gpio__interface.md#ga2fa6bb5880f46984f9fc29c70f7d503e)([DT\_ALIAS](group__devicetree-generic-id.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)(led0), gpios);

static int led\_put(struct [coap\_resource](structcoap__resource.md) \*resource, struct [coap\_packet](structcoap__packet.md) \*request,

struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len)

{

const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload;

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) payload\_len;

payload = [coap\_packet\_get\_payload](group__coap.md#ga28ccf00fb1f5f13f747e61c2e3008b5c)(request, &payload\_len);

if (payload\_len != 1) {

return [COAP\_RESPONSE\_CODE\_BAD\_REQUEST](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5);

}

if ([gpio\_pin\_set\_dt](group__gpio__interface.md#ga541064fb9e575c0c559c101754466fa8)(&led, payload[0]) < 0) {

return [COAP\_RESPONSE\_CODE\_INTERNAL\_ERROR](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499);

}

return [COAP\_RESPONSE\_CODE\_CHANGED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3);

}

[COAP\_RESOURCE\_DEFINE](#gaef40d300170926ad131d06ce62c63d6a)(my\_resource, my\_service, {

.put = led\_put,

});

[COAP\_RESOURCE\_DEFINE](#gaef40d300170926ad131d06ce62c63d6a)

#define COAP\_RESOURCE\_DEFINE(\_name, \_service,...)

Define a static CoAP resource owned by the service named \_service .

**Definition** coap\_service.h:111

[coap\_packet\_get\_payload](group__coap.md#ga28ccf00fb1f5f13f747e61c2e3008b5c)

const uint8\_t \* coap\_packet\_get\_payload(const struct coap\_packet \*cpkt, uint16\_t \*len)

Returns the data pointer and length of the CoAP packet.

[COAP\_RESPONSE\_CODE\_INTERNAL\_ERROR](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499)

@ COAP\_RESPONSE\_CODE\_INTERNAL\_ERROR

5.00 - Internal Server Error

**Definition** coap.h:186

[COAP\_RESPONSE\_CODE\_CHANGED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3)

@ COAP\_RESPONSE\_CODE\_CHANGED

2.04 - Changed

**Definition** coap.h:151

[COAP\_RESPONSE\_CODE\_BAD\_REQUEST](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5)

@ COAP\_RESPONSE\_CODE\_BAD\_REQUEST

4.00 - Bad Request

**Definition** coap.h:157

[DT\_ALIAS](group__devicetree-generic-id.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)

#define DT\_ALIAS(alias)

Get a node identifier from /aliases.

**Definition** devicetree.h:240

[GPIO\_DT\_SPEC\_GET](group__gpio__interface.md#ga2fa6bb5880f46984f9fc29c70f7d503e)

#define GPIO\_DT\_SPEC\_GET(node\_id, prop)

Equivalent to GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, 0).

**Definition** gpio.h:368

[gpio\_pin\_set\_dt](group__gpio__interface.md#ga541064fb9e575c0c559c101754466fa8)

static int gpio\_pin\_set\_dt(const struct gpio\_dt\_spec \*spec, int value)

Set logical level of a output pin from a gpio\_dt\_spec.

**Definition** gpio.h:1645

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[coap\_packet](structcoap__packet.md)

Representation of a CoAP Packet.

**Definition** coap.h:295

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:288

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:385

Parameters
:   | \_name | Name of the resource. |
    | --- | --- |
    | \_service | Name of the associated service. |

## [◆ ](#gac3e92107fa12b111771d56987a242b1a)COAP\_RESOURCE\_FOREACH

| #define COAP\_RESOURCE\_FOREACH | ( |  | *\_service*, |
| --- | --- | --- | --- |
|  |  |  | *\_it* ) |

`#include <[coap_service.h](coap__service_8h.md)>`

**Value:**

[STRUCT\_SECTION\_FOREACH\_ALTERNATE](group__iterable__section__apis.md#ga06fb73cfb2dd5036a6e0f7098105ccd4)(coap\_resource\_##\_service, [coap\_resource](structcoap__resource.md), \_it)

[STRUCT\_SECTION\_FOREACH\_ALTERNATE](group__iterable__section__apis.md#ga06fb73cfb2dd5036a6e0f7098105ccd4)

#define STRUCT\_SECTION\_FOREACH\_ALTERNATE(secname, struct\_type, iterator)

Iterate over a specified iterable section (alternate).

**Definition** iterable\_sections.h:257

Iterate over static CoAP resources associated with a given `_service`.

Note
:   This macro requires that `_service` is defined with [COAP\_SERVICE\_DEFINE](#ga8dc5473755efd48548ec4cb6ac2584ec).

Parameters
:   | \_service | Name of CoAP service |
    | --- | --- |
    | \_it | Name of iterator (of type [coap\_resource](structcoap__resource.md "coap_resource")) |

## [◆ ](#gaf5799a7fbf309f8963d22039a6fe2fbb)COAP\_SERVICE\_AUTOSTART

| #define COAP\_SERVICE\_AUTOSTART   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[coap_service.h](coap__service_8h.md)>`

Start the service on boot.

## [◆ ](#ga1f0c3bf81baa9da11197a74415d3a9ae)COAP\_SERVICE\_COUNT

| #define COAP\_SERVICE\_COUNT | ( |  | *\_dst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap_service.h](coap__service_8h.md)>`

**Value:**

[STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)(coap\_service, \_dst)

[STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)

#define STRUCT\_SECTION\_COUNT(struct\_type, dst)

Count elements in a section.

**Definition** iterable\_sections.h:291

Count the number of CoAP services.

Parameters
:   | [out] | \_dst | Pointer to location where result is written. |
    | --- | --- | --- |

## [◆ ](#ga8dc5473755efd48548ec4cb6ac2584ec)COAP\_SERVICE\_DEFINE

| #define COAP\_SERVICE\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_host*, |
|  |  |  | *\_port*, |
|  |  |  | *\_flags* ) |

`#include <[coap_service.h](coap__service_8h.md)>`

**Value:**

extern struct [coap\_resource](structcoap__resource.md) \_CONCAT(\_coap\_resource\_##\_name, \_list\_start)[]; \

extern struct [coap\_resource](structcoap__resource.md) \_CONCAT(\_coap\_resource\_##\_name, \_list\_end)[]; \

\_\_z\_coap\_service\_define(\_name, \_host, \_port, \_flags, \

&\_CONCAT(\_coap\_resource\_##\_name, \_list\_start)[0], \

&\_CONCAT(\_coap\_resource\_##\_name, \_list\_end)[0])

Define a CoAP service with static resources.

Note
:   The `_host` parameter can be NULL. If not, it is used to specify an IP address either in IPv4 or IPv6 format a fully-qualified hostname or a virtual host, otherwise the any address is used.
:   The `_port` parameter must be non-NULL. It points to a location that specifies the port number to use for the service. If the specified port number is zero, then an ephemeral port number will be used and the actual port number assigned will be written back to memory. For ephemeral port numbers, the memory pointed to by `_port` must be writeable.

Parameters
:   |  | \_name | Name of the service. |
    | --- | --- | --- |
    |  | \_host | IP address or hostname associated with the service. |
    | [in,out] | \_port | Pointer to port associated with the service. |
    |  | \_flags | Configuration flags |

See also
:   [COAP\_SERVICE\_FLAGS](#COAP_SERVICE_FLAGS).

## [◆ ](#gab4d154d5b02235a83c7a2c681b1e22e7)COAP\_SERVICE\_FOREACH

| #define COAP\_SERVICE\_FOREACH | ( |  | *\_it* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap_service.h](coap__service_8h.md)>`

**Value:**

[STRUCT\_SECTION\_FOREACH](group__iterable__section__apis.md#gad723296f2650c25dd278e8586bfaf0ab)(coap\_service, \_it)

[STRUCT\_SECTION\_FOREACH](group__iterable__section__apis.md#gad723296f2650c25dd278e8586bfaf0ab)

#define STRUCT\_SECTION\_FOREACH(struct\_type, iterator)

Iterate over a specified iterable section.

**Definition** iterable\_sections.h:270

Iterate over all CoAP services.

Parameters
:   | \_it | Name of iterator (of type [CoAP service API](group__coap__service.md "CoAP service API")) |
    | --- | --- |

## [◆ ](#gaaca92287c495f4afb79e584c47316037)COAP\_SERVICE\_FOREACH\_RESOURCE

| #define COAP\_SERVICE\_FOREACH\_RESOURCE | ( |  | *\_service*, |
| --- | --- | --- | --- |
|  |  |  | *\_it* ) |

`#include <[coap_service.h](coap__service_8h.md)>`

**Value:**

for (struct [coap\_resource](structcoap__resource.md) \*\_it = (\_service)->res\_begin; ({ \

\_\_ASSERT(\_it <= (\_service)->res\_end, "unexpected list end location"); \

\_it < (\_service)->res\_end; \

}); \_it++)

Iterate over all static resources associated with `_service` .

Note
:   This macro is suitable for a `_service` defined with [COAP\_SERVICE\_DEFINE](#ga8dc5473755efd48548ec4cb6ac2584ec).

Parameters
:   | \_service | Pointer to COAP service |
    | --- | --- |
    | \_it | Name of iterator (of type [coap\_resource](structcoap__resource.md "coap_resource")) |

## [◆ ](#gaf01cb4d11b18272eb27be93cb1a7197b)COAP\_SERVICE\_HAS\_RESOURCE

| #define COAP\_SERVICE\_HAS\_RESOURCE | ( |  | *\_service*, |
| --- | --- | --- | --- |
|  |  |  | *\_resource* ) |

`#include <[coap_service.h](coap__service_8h.md)>`

**Value:**

((\_service)->res\_begin <= \_resource && \_resource < (\_service)->res\_end)

Check if service has the specified resource.

Parameters
:   | \_service | Pointer to a service. |
    | --- | --- |
    | \_resource | Pointer to a resource. |

## [◆ ](#gade9e9a55968a5ad6b3addbb08f2ccb6f)COAP\_SERVICE\_RESOURCE\_COUNT

| #define COAP\_SERVICE\_RESOURCE\_COUNT | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap_service.h](coap__service_8h.md)>`

**Value:**

((\_service)->res\_end - (\_service)->res\_begin)

Count CoAP service static resources.

Parameters
:   | \_service | Pointer to a service. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga098e08b3bc809499b789b890b67cacd5)coap\_resource\_parse\_observe()

| int coap\_resource\_parse\_observe | ( | struct [coap\_resource](structcoap__resource.md) \* | *resource*, |
| --- | --- | --- | --- |
|  |  | const struct [coap\_packet](structcoap__packet.md) \* | *request*, |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr* ) |

`#include <[coap_service.h](coap__service_8h.md)>`

Parse a CoAP observe request for the provided `resource` .

Note
:   This function is suitable for a `resource` defined with [COAP\_RESOURCE\_DEFINE](#gaef40d300170926ad131d06ce62c63d6a).

If the observe option value is equal to 0, an observer will be added, if the value is equal to 1, an existing observer will be removed.

Parameters
:   | resource | Pointer to CoAP resource |
    | --- | --- |
    | request | CoAP request to parse |
    | addr | Peer address |

Returns
:   the observe option value in case of success or negative in case of error.

## [◆ ](#ga8d9ab0bf6b1ea15408f1c80c45aae16b)coap\_resource\_remove\_observer\_by\_addr()

| int coap\_resource\_remove\_observer\_by\_addr | ( | struct [coap\_resource](structcoap__resource.md) \* | *resource*, |
| --- | --- | --- | --- |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr* ) |

`#include <[coap_service.h](coap__service_8h.md)>`

Lookup an observer by address and remove it from the `resource` .

Note
:   This function is suitable for a `resource` defined with [COAP\_RESOURCE\_DEFINE](#gaef40d300170926ad131d06ce62c63d6a).

Parameters
:   | resource | Pointer to CoAP resource |
    | --- | --- |
    | addr | Peer address |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#gad575a7209a56874002c540eb3f8c0733)coap\_resource\_remove\_observer\_by\_token()

| int coap\_resource\_remove\_observer\_by\_token | ( | struct [coap\_resource](structcoap__resource.md) \* | *resource*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *token*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *token\_len* ) |

`#include <[coap_service.h](coap__service_8h.md)>`

Lookup an observer by token and remove it from the `resource` .

Note
:   This function is suitable for a `resource` defined with [COAP\_RESOURCE\_DEFINE](#gaef40d300170926ad131d06ce62c63d6a).

Parameters
:   | resource | Pointer to CoAP resource |
    | --- | --- |
    | token | Pointer to the token |
    | token\_len | Length of valid bytes in the token |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga67e2cebcfa83f6d11dc335de5dc51a47)coap\_resource\_send()

| int coap\_resource\_send | ( | const struct [coap\_resource](structcoap__resource.md) \* | *resource*, |
| --- | --- | --- | --- |
|  |  | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addr\_len*, |
|  |  | const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \* | *params* ) |

`#include <[coap_service.h](coap__service_8h.md)>`

Send a CoAP message from the provided `resource` .

Note
:   This function is suitable for a `resource` defined with [COAP\_RESOURCE\_DEFINE](#gaef40d300170926ad131d06ce62c63d6a).

Parameters
:   | resource | Pointer to CoAP resource |
    | --- | --- |
    | cpkt | CoAP Packet to send |
    | addr | Peer address |
    | addr\_len | Peer address length |
    | params | Pointer to transmission parameters structure or NULL to use default values. |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga08638f2001ca2f807489c12ff426784c)coap\_service\_is\_running()

| int coap\_service\_is\_running | ( | const struct coap\_service \* | *service* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap_service.h](coap__service_8h.md)>`

Query the provided `service` running state.

Note
:   This function is suitable for a `service` defined with [COAP\_SERVICE\_DEFINE](#ga8dc5473755efd48548ec4cb6ac2584ec).

Parameters
:   | service | Pointer to CoAP service |
    | --- | --- |

Return values
:   | 1 | if the service is running |
    | --- | --- |
    | 0 | if the service is stopped |
    | negative | in case of an error. |

## [◆ ](#gad4254ddb71400026211fe8a6da05b2be)coap\_service\_send()

| int coap\_service\_send | ( | const struct coap\_service \* | *service*, |
| --- | --- | --- | --- |
|  |  | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addr\_len*, |
|  |  | const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \* | *params* ) |

`#include <[coap_service.h](coap__service_8h.md)>`

Send a CoAP message from the provided `service` .

Note
:   This function is suitable for a `service` defined with [COAP\_SERVICE\_DEFINE](#ga8dc5473755efd48548ec4cb6ac2584ec).

Parameters
:   | service | Pointer to CoAP service |
    | --- | --- |
    | cpkt | CoAP Packet to send |
    | addr | Peer address |
    | addr\_len | Peer address length |
    | params | Pointer to transmission parameters structure or NULL to use default values. |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#gad1e64f8fe2c6ae32730a9a61f8351bab)coap\_service\_start()

| int coap\_service\_start | ( | const struct coap\_service \* | *service* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap_service.h](coap__service_8h.md)>`

Start the provided `service` .

Note
:   This function is suitable for a `service` defined with [COAP\_SERVICE\_DEFINE](#ga8dc5473755efd48548ec4cb6ac2584ec).

Parameters
:   | service | Pointer to CoAP service |
    | --- | --- |

Return values
:   | 0 | in case of success. |
    | --- | --- |
    | -EALREADY | in case of an already running service. |
    | -ENOTSUP | in case the server has no valid host and port configuration. |

## [◆ ](#ga58bc31fc4d53ebce9c18ccbc5aab72ce)coap\_service\_stop()

| int coap\_service\_stop | ( | const struct coap\_service \* | *service* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap_service.h](coap__service_8h.md)>`

Stop the provided `service` .

Note
:   This function is suitable for a `service` defined with [COAP\_SERVICE\_DEFINE](#ga8dc5473755efd48548ec4cb6ac2584ec).

Parameters
:   | service | Pointer to CoAP service |
    | --- | --- |

Return values
:   | 0 | in case of success. |
    | --- | --- |
    | -EALREADY | in case the service isn't running. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
