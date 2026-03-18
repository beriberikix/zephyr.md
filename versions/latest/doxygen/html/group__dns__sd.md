---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__dns__sd.html
original_path: doxygen/html/group__dns__sd.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

DNS Service Discovery

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

DNS Service Discovery.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [DNS\_SD\_INSTANCE\_MIN\_SIZE](#ga4d1f5462555d6051bdeaa21b02e7aa6e)   1 |
|  | RFC 1034 Section 3.1. |
| #define | [DNS\_SD\_INSTANCE\_MAX\_SIZE](#ga5c0993b8bc21d47fa15f56acb313ac31)   63 |
|  | RFC 1034 Section 3.1, RFC 6763 Section 7.2. |
| #define | [DNS\_SD\_SERVICE\_MIN\_SIZE](#gacc652552aa567206ab7a4d7d070d1fbc)   2 |
|  | RFC 6763 Section 7.2 - inclusive of underscore. |
| #define | [DNS\_SD\_SERVICE\_MAX\_SIZE](#gab4d208eac1491c45cb47e87c90a78c26)   16 |
|  | RFC 6763 Section 7.2 - inclusive of underscore. |
| #define | [DNS\_SD\_SERVICE\_PREFIX](#ga81cac0a52e58142e492bad244ff97490)   '\_' |
|  | RFC 6763 Section 4.1.2. |
| #define | [DNS\_SD\_PROTO\_SIZE](#gafb686ae445f5bd640176f59d62df2bdc)   4 |
|  | RFC 6763 Section 4.1.2 - either \_tcp or \_udp (case insensitive). |
| #define | [DNS\_SD\_DOMAIN\_MIN\_SIZE](#ga19d655c1778143e2aed5d2d69a757422)   2 |
|  | ICANN Rules for TLD naming. |
| #define | [DNS\_SD\_DOMAIN\_MAX\_SIZE](#gaa93b197f2b9a3b13c7ed8f3c455f11cb)   63 |
|  | RFC 1034 Section 3.1, RFC 6763 Section 7.2. |
| #define | [DNS\_SD\_MIN\_LABELS](#gaeec792bc3111e1961eb2e21cd8bea80a)   3 |
|  | Minimum number of segments in a fully-qualified name. |
| #define | [DNS\_SD\_MAX\_LABELS](#ga269e2f3bbf15a5ccd81a444749faa384)   4 |
|  | Maximum number of segments in a fully-qualified name. |
| #define | [DNS\_SD\_REGISTER\_SERVICE](#ga0c0060a680d5c4fe56f2815c920c3627)(\_id, \_instance, \_service, \_proto, \_domain, \_text, \_port) |
|  | Register a service for DNS Service Discovery. |
| #define | [DNS\_SD\_REGISTER\_TCP\_SERVICE](#ga96abc525d755c138304f07cdd2d9e1c2)(id, instance, service, domain, text, port) |
|  | Register a TCP service for DNS Service Discovery. |
| #define | [DNS\_SD\_REGISTER\_UDP\_SERVICE](#gaf8abe0968552213d46b49be16c1f21d6)(id, instance, service, domain, text, port) |
|  | Register a UDP service for DNS Service Discovery. |
| #define | [DNS\_SD\_EMPTY\_TXT](#ga221216c5ffd142aa4c6cade4064d580f)   dns\_sd\_empty\_txt |
|  | Empty DNS-SD TXT specifier. |

| Functions | |
| --- | --- |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [dns\_sd\_txt\_size](#ga6d68e785607089df42d534c2f876c6d5) (const struct dns\_sd\_rec \*rec) |
|  | Obtain the size of DNS-SD TXT data. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [dns\_sd\_is\_service\_type\_enumeration](#gaeba098fa6d159067c70588cb60056277) (const struct dns\_sd\_rec \*rec) |
|  | Check if *rec* is a DNS-SD Service Type Enumeration. |
| void | [dns\_sd\_create\_wildcard\_filter](#ga328d71e26411460b1b329db8f1ebd37b) (struct dns\_sd\_rec \*filter) |
|  | Create a wildcard filter for DNS-SD records. |

## Detailed Description

DNS Service Discovery.

This API enables services to be advertised via DNS. To advertise a service, system or application code should use [DNS\_SD\_REGISTER\_TCP\_SERVICE](#ga96abc525d755c138304f07cdd2d9e1c2) or [DNS\_SD\_REGISTER\_UDP\_SERVICE](#gaf8abe0968552213d46b49be16c1f21d6).

See also
:   [RFC 6763](https://tools.ietf.org/html/rfc6763)

## Macro Definition Documentation

## [◆ ](#gaa93b197f2b9a3b13c7ed8f3c455f11cb)DNS\_SD\_DOMAIN\_MAX\_SIZE

| #define DNS\_SD\_DOMAIN\_MAX\_SIZE   63 |
| --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

RFC 1034 Section 3.1, RFC 6763 Section 7.2.

## [◆ ](#ga19d655c1778143e2aed5d2d69a757422)DNS\_SD\_DOMAIN\_MIN\_SIZE

| #define DNS\_SD\_DOMAIN\_MIN\_SIZE   2 |
| --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

ICANN Rules for TLD naming.

## [◆ ](#ga221216c5ffd142aa4c6cade4064d580f)DNS\_SD\_EMPTY\_TXT

| #define DNS\_SD\_EMPTY\_TXT   dns\_sd\_empty\_txt |
| --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

Empty DNS-SD TXT specifier.

## [◆ ](#ga5c0993b8bc21d47fa15f56acb313ac31)DNS\_SD\_INSTANCE\_MAX\_SIZE

| #define DNS\_SD\_INSTANCE\_MAX\_SIZE   63 |
| --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

RFC 1034 Section 3.1, RFC 6763 Section 7.2.

## [◆ ](#ga4d1f5462555d6051bdeaa21b02e7aa6e)DNS\_SD\_INSTANCE\_MIN\_SIZE

| #define DNS\_SD\_INSTANCE\_MIN\_SIZE   1 |
| --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

RFC 1034 Section 3.1.

## [◆ ](#ga269e2f3bbf15a5ccd81a444749faa384)DNS\_SD\_MAX\_LABELS

| #define DNS\_SD\_MAX\_LABELS   4 |
| --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

Maximum number of segments in a fully-qualified name.

This represents FQN's of the form below

<instance>.<sn>.\_tcp.<domain>.

Currently sub-types and service domains are unsupported and only the "local" domain is supported. Specifically, that excludes the following:

<sub>.\_sub.<sn>.\_tcp.<servicedomain>.<parentdomain>.

See also
:   [RFC 6763](https://datatracker.ietf.org/doc/html/rfc6763), Section 7.2.

## [◆ ](#gaeec792bc3111e1961eb2e21cd8bea80a)DNS\_SD\_MIN\_LABELS

| #define DNS\_SD\_MIN\_LABELS   3 |
| --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

Minimum number of segments in a fully-qualified name.

This represents FQN's of the form below

<sn>.\_tcp.<domain>.

Currently sub-types and service domains are unsupported and only the "local" domain is supported. Specifically, that excludes the following:

<sub>.\_sub.<sn>.\_tcp.<servicedomain>.<parentdomain>.

See also
:   [RFC 6763](https://datatracker.ietf.org/doc/html/rfc6763), Section 7.2.

## [◆ ](#gafb686ae445f5bd640176f59d62df2bdc)DNS\_SD\_PROTO\_SIZE

| #define DNS\_SD\_PROTO\_SIZE   4 |
| --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

RFC 6763 Section 4.1.2 - either \_tcp or \_udp (case insensitive).

## [◆ ](#ga0c0060a680d5c4fe56f2815c920c3627)DNS\_SD\_REGISTER\_SERVICE

| #define DNS\_SD\_REGISTER\_SERVICE | ( |  | *\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_instance*, |
|  |  |  | *\_service*, |
|  |  |  | *\_proto*, |
|  |  |  | *\_domain*, |
|  |  |  | *\_text*, |
|  |  |  | *\_port* ) |

`#include <[dns_sd.h](dns__sd_8h.md)>`

**Value:**

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(dns\_sd\_rec, \_id) = { \

.instance = \_instance, \

.service = \_service, \

.proto = \_proto, \

.domain = \_domain, \

.text = (const char \*)\_text, \

.text\_size = sizeof(\_text) - 1, \

.port = \_port, \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

Register a service for DNS Service Discovery.

This macro should be used for advanced use cases. Two simple use cases are when a custom `_domain` or a custom (non-standard) `_proto` is required.

Another use case is when the port number is not preassigned. That could be for a number of reasons, but the most common use case would be for ephemeral port usage - i.e. when the service is bound using port number 0. In that case, Zephyr (like other OS's) will simply choose an unused port. When using ephemeral ports, it can be helpful to assign `_port` to the [sockaddr\_in::sin\_port](structsockaddr__in.md#a3cf9239fdd8bd32855d66a4b86349fbb "sockaddr_in::sin_port") field of an IPv4 [sockaddr\_in](structsockaddr__in.md "sockaddr_in"), or to the [sockaddr\_in6::sin6\_port](structsockaddr__in6.md#a4fc2b7a478d258e9e778772701096022 "sockaddr_in6::sin6_port") field of an IPv6 [sockaddr\_in6](structsockaddr__in6.md "sockaddr_in6").

The service can be referenced using the `_id` variable.

Parameters
:   | \_id | variable name for the DNS-SD service record |
    | --- | --- |
    | \_instance | name of the service instance such as "My HTTP Server" |
    | \_service | name of the service, such as "\_http" |
    | \_proto | protocol used by the service - either "\_tcp" or "\_udp" |
    | \_domain | the domain of the service, such as "local" |
    | \_text | information for the DNS TXT record |
    | \_port | a pointer to the port number that this service will use |

## [◆ ](#ga96abc525d755c138304f07cdd2d9e1c2)DNS\_SD\_REGISTER\_TCP\_SERVICE

| #define DNS\_SD\_REGISTER\_TCP\_SERVICE | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *instance*, |
|  |  |  | *service*, |
|  |  |  | *domain*, |
|  |  |  | *text*, |
|  |  |  | *port* ) |

`#include <[dns_sd.h](dns__sd_8h.md)>`

**Value:**

static const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id ## \_port = [sys\_cpu\_to\_be16](sys_2byteorder_8h.md#a9e2c7b19bbba5343ee8c5f9740484a56)(port); \

DNS\_SD\_REGISTER\_SERVICE(id, instance, service, "\_tcp", domain, \

text, &id ## \_port)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[sys\_cpu\_to\_be16](sys_2byteorder_8h.md#a9e2c7b19bbba5343ee8c5f9740484a56)

#define sys\_cpu\_to\_be16(val)

Convert 16-bit integer from host endianness to big-endian.

**Definition** byteorder.h:267

Register a TCP service for DNS Service Discovery.

This macro can be used for service advertisement using DNS-SD.

The service can be referenced using the `id` variable.

Example (with TXT):

#include <[zephyr/net/dns\_sd.h](dns__sd_8h.md)>

static const bar\_txt[] = {

"\x06" "path=/"

"\x0f" "this=is the way"

"\x0e" "foo or=foo not"

"\x17" "this=has\0embedded\0nulls"

"\x04" "true"

};

// Possibly use an ephemeral port

// Possibly only assign bar\_port when the service is running

static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bar\_port;

[DNS\_SD\_REGISTER\_TCP\_SERVICE](#ga96abc525d755c138304f07cdd2d9e1c2)(bar, CONFIG\_NET\_HOSTNAME,

"\_bar", "local", bar\_txt, &bar\_port);

[dns\_sd.h](dns__sd_8h.md)

DNS Service Discovery.

[DNS\_SD\_REGISTER\_TCP\_SERVICE](#ga96abc525d755c138304f07cdd2d9e1c2)

#define DNS\_SD\_REGISTER\_TCP\_SERVICE(id, instance, service, domain, text, port)

Register a TCP service for DNS Service Discovery.

**Definition** dns\_sd.h:161

{c}

TXT records begin with a single length byte (hex-encoded) and contain key=value pairs. Thus, the length of the key-value pair must not exceed 255 bytes. Care must be taken to ensure that the encoded length value is correct.

For additional rules on TXT encoding, see RFC 6763, Section 6.

Parameters
:   | id | variable name for the DNS-SD service record |
    | --- | --- |
    | instance | name of the service instance such as "My HTTP Server" |
    | service | name of the service, such as "\_http" |
    | domain | the domain of the service, such as "local" |
    | text | information for the DNS TXT record |
    | port | the port number that this service will use |

See also
:   [RFC 6763](https://tools.ietf.org/html/rfc6763)

## [◆ ](#gaf8abe0968552213d46b49be16c1f21d6)DNS\_SD\_REGISTER\_UDP\_SERVICE

| #define DNS\_SD\_REGISTER\_UDP\_SERVICE | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *instance*, |
|  |  |  | *service*, |
|  |  |  | *domain*, |
|  |  |  | *text*, |
|  |  |  | *port* ) |

`#include <[dns_sd.h](dns__sd_8h.md)>`

**Value:**

static const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id ## \_port = [sys\_cpu\_to\_be16](sys_2byteorder_8h.md#a9e2c7b19bbba5343ee8c5f9740484a56)(port); \

DNS\_SD\_REGISTER\_SERVICE(id, instance, service, "\_udp", domain, \

text, &id ## \_port)

Register a UDP service for DNS Service Discovery.

This macro can be used for service advertisement using DNS-SD.

The service can be referenced using the `id` variable.

Example (no TXT):

#include <[zephyr/net/dns\_sd.h](dns__sd_8h.md)>

#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

static const foo\_port = [sys\_cpu\_to\_be16](sys_2byteorder_8h.md#a9e2c7b19bbba5343ee8c5f9740484a56)(4242);

[DNS\_SD\_REGISTER\_UDP\_SERVICE](#gaf8abe0968552213d46b49be16c1f21d6)(foo, CONFIG\_NET\_HOSTNAME,

"\_foo", [DNS\_SD\_EMPTY\_TXT](#ga221216c5ffd142aa4c6cade4064d580f), &foo\_port);

[DNS\_SD\_EMPTY\_TXT](#ga221216c5ffd142aa4c6cade4064d580f)

#define DNS\_SD\_EMPTY\_TXT

Empty DNS-SD TXT specifier.

**Definition** dns\_sd.h:199

[DNS\_SD\_REGISTER\_UDP\_SERVICE](#gaf8abe0968552213d46b49be16c1f21d6)

#define DNS\_SD\_REGISTER\_UDP\_SERVICE(id, instance, service, domain, text, port)

Register a UDP service for DNS Service Discovery.

**Definition** dns\_sd.h:192

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

{c}

Parameters
:   | id | variable name for the DNS-SD service record |
    | --- | --- |
    | instance | name of the service instance such as "My TFTP Server" |
    | service | name of the service, such as "\_tftp" |
    | domain | the domain of the service, such as "local" or "zephyrproject.org" |
    | text | information for the DNS TXT record |
    | port | a pointer to the port number that this service will use |

See also
:   [RFC 6763](https://tools.ietf.org/html/rfc6763)

## [◆ ](#gab4d208eac1491c45cb47e87c90a78c26)DNS\_SD\_SERVICE\_MAX\_SIZE

| #define DNS\_SD\_SERVICE\_MAX\_SIZE   16 |
| --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

RFC 6763 Section 7.2 - inclusive of underscore.

## [◆ ](#gacc652552aa567206ab7a4d7d070d1fbc)DNS\_SD\_SERVICE\_MIN\_SIZE

| #define DNS\_SD\_SERVICE\_MIN\_SIZE   2 |
| --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

RFC 6763 Section 7.2 - inclusive of underscore.

## [◆ ](#ga81cac0a52e58142e492bad244ff97490)DNS\_SD\_SERVICE\_PREFIX

| #define DNS\_SD\_SERVICE\_PREFIX   '\_' |
| --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

RFC 6763 Section 4.1.2.

## Function Documentation

## [◆ ](#ga328d71e26411460b1b329db8f1ebd37b)dns\_sd\_create\_wildcard\_filter()

| void dns\_sd\_create\_wildcard\_filter | ( | struct dns\_sd\_rec \* | *filter* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

Create a wildcard filter for DNS-SD records.

Parameters
:   | filter | a pointer to the filter to use |
    | --- | --- |

## [◆ ](#gaeba098fa6d159067c70588cb60056277)dns\_sd\_is\_service\_type\_enumeration()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dns\_sd\_is\_service\_type\_enumeration | ( | const struct dns\_sd\_rec \* | *rec* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

Check if *rec* is a DNS-SD Service Type Enumeration.

DNS-SD Service Type Enumeration is used by network tooling to acquire a list of all mDNS-advertised services belonging to a particular host on a particular domain.

For example, for the domain '.local', the equivalent query would be '\_services.\_dns-sd.\_udp.local'.

Currently, only the '.local' domain is supported.

See also
:   [Service Type Enumeration, RFC 6763](https://datatracker.ietf.org/doc/html/rfc6763#section-9).

Parameters
:   | rec | the record to in question |
    | --- | --- |

Returns
:   true if *rec* is a DNS-SD Service Type Enumeration

## [◆ ](#ga6d68e785607089df42d534c2f876c6d5)dns\_sd\_txt\_size()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dns\_sd\_txt\_size | ( | const struct dns\_sd\_rec \* | *rec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dns_sd.h](dns__sd_8h.md)>`

Obtain the size of DNS-SD TXT data.

Parameters
:   | rec | the record to in question |
    | --- | --- |

Returns
:   the size of the text field

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
