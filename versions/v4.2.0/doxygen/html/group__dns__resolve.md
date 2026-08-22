---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__dns__resolve.html
original_path: doxygen/html/group__dns__resolve.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

DNS Resolve Library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

DNS resolving library.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [dns\_addrinfo](structdns__addrinfo.md) |
|  | Address info struct is passed to callback that gets all the results. [More...](structdns__addrinfo.md#details) |
| struct | [dns\_resolve\_context](structdns__resolve__context.md) |
|  | DNS resolve context structure. [More...](structdns__resolve__context.md#details) |

| Macros | |
| --- | --- |
| #define | [DNS\_MAX\_NAME\_SIZE](#gaba564a71c4fb4c44fae69015e880b0db)   20 |
|  | Max size of the resolved name. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [dns\_resolve\_cb\_t](#gafe22d0ef90c581982561ef0c33d1f722)) (enum [dns\_resolve\_status](#ga5baf1fea0482fb3a940b4f5350a3c58e) status, struct [dns\_addrinfo](structdns__addrinfo.md) \*info, void \*user\_data) |
|  | DNS resolve callback. |

| Enumerations | |
| --- | --- |
| enum | [dns\_query\_type](#ga7169c5a920fb1b0d77910a6ab922e3f0) { [DNS\_QUERY\_TYPE\_A](#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134) = 1 , [DNS\_QUERY\_TYPE\_PTR](#gga7169c5a920fb1b0d77910a6ab922e3f0a69676b0e82ee456e5faa935e39c1c3fa) = 12 , [DNS\_QUERY\_TYPE\_AAAA](#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049) = 28 } |
|  | DNS query type enum. [More...](#ga7169c5a920fb1b0d77910a6ab922e3f0) |
| enum | [dns\_server\_source](#gaeda02f82b12e9b7b4dea9fd66be123a7) {     [DNS\_SOURCE\_UNKNOWN](#ggaeda02f82b12e9b7b4dea9fd66be123a7a8e2e0f2cf2997d9519a52dfa9052fdf9) = 0 , [DNS\_SOURCE\_MANUAL](#ggaeda02f82b12e9b7b4dea9fd66be123a7a53fc14584c90542121f4b1cd61658c33) , [DNS\_SOURCE\_DHCPV4](#ggaeda02f82b12e9b7b4dea9fd66be123a7a7eba9f4f6d3bb94c480417e85583463b) , [DNS\_SOURCE\_DHCPV6](#ggaeda02f82b12e9b7b4dea9fd66be123a7ad12f850b810647113633234ae818b84b) ,     [DNS\_SOURCE\_IPV6\_RA](#ggaeda02f82b12e9b7b4dea9fd66be123a7a687bf289d220cfaffbf8c89d9ce5b4c9) , [DNS\_SOURCE\_PPP](#ggaeda02f82b12e9b7b4dea9fd66be123a7aa6df19967b1ac123c79c5812ec62a902)   } |
|  | Entity that added the DNS server. [More...](#gaeda02f82b12e9b7b4dea9fd66be123a7) |
| enum | [dns\_resolve\_status](#ga5baf1fea0482fb3a940b4f5350a3c58e) {     [DNS\_EAI\_NONAME](#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) = -2 , [DNS\_EAI\_AGAIN](#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) = -3 , [DNS\_EAI\_FAIL](#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) = -4 , [DNS\_EAI\_NODATA](#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) = -5 ,     [DNS\_EAI\_ADDRFAMILY](#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d) = -9 , [DNS\_EAI\_MEMORY](#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) = -10 , [DNS\_EAI\_OVERFLOW](#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f) = -12 , [DNS\_EAI\_INPROGRESS](#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3) = -100 ,     [DNS\_EAI\_CANCELED](#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3) = -101 , [DNS\_EAI\_NOTCANCELED](#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f) = -102 , [DNS\_EAI\_ALLDONE](#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836) = -103 , [DNS\_EAI\_IDN\_ENCODE](#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4) = -105   } |
|  | Status values for the callback. [More...](#ga5baf1fea0482fb3a940b4f5350a3c58e) |

| Functions | |
| --- | --- |
| int | [dns\_resolve\_init](#ga74e2be49894100fe5da641331ef083de) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, const char \*dns\_servers\_str[], const struct [sockaddr](structsockaddr.md) \*dns\_servers\_sa[]) |
|  | Init DNS resolving context. |
| int | [dns\_resolve\_init\_default](#ga71eab0f9dd0bc7c02c0d55e7dc6741f3) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx) |
|  | Init DNS resolving context with default Kconfig options. |
| int | [dns\_resolve\_close](#gab04f3b2347e9c59346c10180c6c9ffbc) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx) |
|  | Close DNS resolving context. |
| int | [dns\_resolve\_reconfigure](#ga54dc319f118e6a8e1e78435539c8f039) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, const char \*servers\_str[], const struct [sockaddr](structsockaddr.md) \*servers\_sa[], enum [dns\_server\_source](#gaeda02f82b12e9b7b4dea9fd66be123a7) source) |
|  | Reconfigure DNS resolving context. |
| int | [dns\_resolve\_reconfigure\_with\_interfaces](#ga211f9c8a5588186607e9257c4451f64d) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, const char \*servers\_str[], const struct [sockaddr](structsockaddr.md) \*servers\_sa[], int interfaces[], enum [dns\_server\_source](#gaeda02f82b12e9b7b4dea9fd66be123a7) source) |
|  | Reconfigure DNS resolving context with new server list and allowing servers to be specified to a specific network interface. |
| int | [dns\_resolve\_remove](#ga54c85b9c69c9a44f2e7bb78165cebfcb) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, int if\_index) |
|  | Remove servers from the DNS resolving context. |
| int | [dns\_resolve\_remove\_source](#gae292786587c511c223481f77a4f43017) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, int if\_index, enum [dns\_server\_source](#gaeda02f82b12e9b7b4dea9fd66be123a7) source) |
|  | Remove servers from the DNS resolving context that were added by a specific source. |
| int | [dns\_resolve\_cancel](#ga7701ddd6b6c5923f0d122a2bcf898cbf) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id) |
|  | Cancel a pending DNS query. |
| int | [dns\_resolve\_cancel\_with\_name](#gaf2854ca9b839e7cba073e75202ac7e38) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id, const char \*query\_name, enum [dns\_query\_type](#ga7169c5a920fb1b0d77910a6ab922e3f0) query\_type) |
|  | Cancel a pending DNS query using id, name and type. |
| int | [dns\_resolve\_name](#ga24f9bc24e2021b6b528bb15e4fcca49b) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, const char \*query, enum [dns\_query\_type](#ga7169c5a920fb1b0d77910a6ab922e3f0) type, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dns\_id, [dns\_resolve\_cb\_t](#gafe22d0ef90c581982561ef0c33d1f722) cb, void \*user\_data, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Resolve DNS name. |
| static int | [dns\_resolve\_service](#gaf28f6f8baa97d0b2341e1bdc02b6cb8c) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, const char \*query, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dns\_id, [dns\_resolve\_cb\_t](#gafe22d0ef90c581982561ef0c33d1f722) cb, void \*user\_data, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Resolve DNS service. |
| struct [dns\_resolve\_context](structdns__resolve__context.md) \* | [dns\_resolve\_get\_default](#gae69cd758e99ea93ef8aac28366918b87) (void) |
|  | Get default DNS context. |
| static int | [dns\_get\_addr\_info](#gaf891d7e21bddc8fbd029209b4339c01d) (const char \*query, enum [dns\_query\_type](#ga7169c5a920fb1b0d77910a6ab922e3f0) type, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dns\_id, [dns\_resolve\_cb\_t](#gafe22d0ef90c581982561ef0c33d1f722) cb, void \*user\_data, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Get IP address info from DNS. |
| static int | [dns\_cancel\_addr\_info](#ga54ae7aaf53b36951b27f09e1cc82df55) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id) |
|  | Cancel a pending DNS query. |

## Detailed Description

DNS resolving library.

Since
:   1.8

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#gaba564a71c4fb4c44fae69015e880b0db)DNS\_MAX\_NAME\_SIZE

| #define DNS\_MAX\_NAME\_SIZE   20 |
| --- |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Max size of the resolved name.

## Typedef Documentation

## [◆ ](#gafe22d0ef90c581982561ef0c33d1f722)dns\_resolve\_cb\_t

| typedef void(\* dns\_resolve\_cb\_t) (enum [dns\_resolve\_status](#ga5baf1fea0482fb3a940b4f5350a3c58e) status, struct [dns\_addrinfo](structdns__addrinfo.md) \*info, void \*user\_data) |
| --- |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

DNS resolve callback.

The DNS resolve callback is called after a successful DNS resolving. The resolver can call this callback multiple times, one for each resolved address.

Parameters
:   | status | The status of the query: DNS\_EAI\_INPROGRESS returned for each resolved address DNS\_EAI\_ALLDONE mark end of the resolving, info is set to NULL in this case DNS\_EAI\_CANCELED if the query was canceled manually or timeout happened DNS\_EAI\_FAIL if the name cannot be resolved by the server DNS\_EAI\_NODATA if there is no such name other values means that an error happened. |
    | --- | --- |
    | info | Query results are stored here. |
    | user\_data | The user data given in [dns\_resolve\_name()](#ga24f9bc24e2021b6b528bb15e4fcca49b) call. |

## Enumeration Type Documentation

## [◆ ](#ga7169c5a920fb1b0d77910a6ab922e3f0)dns\_query\_type

| enum [dns\_query\_type](#ga7169c5a920fb1b0d77910a6ab922e3f0) |
| --- |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

DNS query type enum.

| Enumerator | |
| --- | --- |
| DNS\_QUERY\_TYPE\_A | IPv4 query. |
| DNS\_QUERY\_TYPE\_PTR | PTR query. |
| DNS\_QUERY\_TYPE\_AAAA | IPv6 query. |

## [◆ ](#ga5baf1fea0482fb3a940b4f5350a3c58e)dns\_resolve\_status

| enum [dns\_resolve\_status](#ga5baf1fea0482fb3a940b4f5350a3c58e) |
| --- |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Status values for the callback.

| Enumerator | |
| --- | --- |
| DNS\_EAI\_NONAME | Invalid value for `ai\_flags' field \*/ DNS\_EAI\_BADFLAGS = -1, /\*\* NAME or SERVICE is unknown. |
| DNS\_EAI\_AGAIN | Temporary failure in name resolution. |
| DNS\_EAI\_FAIL | Non-recoverable failure in name res. |
| DNS\_EAI\_NODATA | No address associated with NAME. |
| DNS\_EAI\_ADDRFAMILY | ai\_family' not supported \*/ DNS\_EAI\_FAMILY = -6, /\*\* ai\_socktype' not supported \*/ DNS\_EAI\_SOCKTYPE = -7, /\*\* SRV not supported for `ai\_socktype' \*/ DNS\_EAI\_SERVICE = -8, /\*\* Address family for NAME not supported |
| DNS\_EAI\_MEMORY | Memory allocation failure. |
| DNS\_EAI\_OVERFLOW | System error returned in `errno' \*/ DNS\_EAI\_SYSTEM = -11, /\*\* Argument buffer overflow. |
| DNS\_EAI\_INPROGRESS | Processing request in progress. |
| DNS\_EAI\_CANCELED | Request canceled. |
| DNS\_EAI\_NOTCANCELED | Request not canceled. |
| DNS\_EAI\_ALLDONE | All requests done. |
| DNS\_EAI\_IDN\_ENCODE | IDN encoding failed. |

## [◆ ](#gaeda02f82b12e9b7b4dea9fd66be123a7)dns\_server\_source

| enum [dns\_server\_source](#gaeda02f82b12e9b7b4dea9fd66be123a7) |
| --- |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Entity that added the DNS server.

| Enumerator | |
| --- | --- |
| DNS\_SOURCE\_UNKNOWN | Source is unknown. |
| DNS\_SOURCE\_MANUAL | Server information is added manually, for example by an application. |
| DNS\_SOURCE\_DHCPV4 | Server information is from DHCPv4 server. |
| DNS\_SOURCE\_DHCPV6 | Server information is from DHCPv6 server. |
| DNS\_SOURCE\_IPV6\_RA | Server information is from IPv6 SLAAC (router advertisement). |
| DNS\_SOURCE\_PPP | Server information is from PPP. |

## Function Documentation

## [◆ ](#ga54ae7aaf53b36951b27f09e1cc82df55)dns\_cancel\_addr\_info()

| | int dns\_cancel\_addr\_info | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *dns\_id* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Cancel a pending DNS query.

This releases DNS resources used by a pending query.

Parameters
:   | dns\_id | DNS id of the pending query |
    | --- | --- |

Returns
:   0 if ok, <0 if error.

## [◆ ](#gaf891d7e21bddc8fbd029209b4339c01d)dns\_get\_addr\_info()

| | int dns\_get\_addr\_info | ( | const char \* | *query*, | | --- | --- | --- | --- | |  |  | enum [dns\_query\_type](#ga7169c5a920fb1b0d77910a6ab922e3f0) | *type*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *dns\_id*, | |  |  | [dns\_resolve\_cb\_t](#gafe22d0ef90c581982561ef0c33d1f722) | *cb*, | |  |  | void \* | *user\_data*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Get IP address info from DNS.

This function can be used to resolve e.g., IPv4 or IPv6 address. Note that this is asynchronous call, the function will return immediately and system will call the callback after resolving has finished or timeout has occurred. We might send the query to multiple servers (if there are more than one server configured), but we only use the result of the first received response. This variant uses system wide DNS servers.

Parameters
:   | query | What the caller wants to resolve. |
    | --- | --- |
    | type | What kind of data the caller wants to get. |
    | dns\_id | DNS id is returned to the caller. This is needed if one wishes to cancel the query. This can be set to NULL if there is no need to cancel the query. |
    | cb | Callback to call after the resolving has finished or timeout has happened. |
    | user\_data | The user data. |
    | timeout | The timeout value for the connection. Possible values: SYS\_FOREVER\_MS: the query is tried forever, user needs to cancel it manually if it takes too long time to finish >0: start the query and let the system timeout it after specified ms |

Returns
:   0 if resolving was started ok, < 0 otherwise

## [◆ ](#ga7701ddd6b6c5923f0d122a2bcf898cbf)dns\_resolve\_cancel()

| int dns\_resolve\_cancel | ( | struct [dns\_resolve\_context](structdns__resolve__context.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *dns\_id* ) |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Cancel a pending DNS query.

This releases DNS resources used by a pending query.

Parameters
:   | ctx | DNS context |
    | --- | --- |
    | dns\_id | DNS id of the pending query |

Returns
:   0 if ok, <0 if error.

## [◆ ](#gaf2854ca9b839e7cba073e75202ac7e38)dns\_resolve\_cancel\_with\_name()

| int dns\_resolve\_cancel\_with\_name | ( | struct [dns\_resolve\_context](structdns__resolve__context.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *dns\_id*, |
|  |  | const char \* | *query\_name*, |
|  |  | enum [dns\_query\_type](#ga7169c5a920fb1b0d77910a6ab922e3f0) | *query\_type* ) |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Cancel a pending DNS query using id, name and type.

This releases DNS resources used by a pending query.

Parameters
:   | ctx | DNS context |
    | --- | --- |
    | dns\_id | DNS id of the pending query |
    | query\_name | Name of the resource we are trying to query (hostname) |
    | query\_type | Type of the query (A or AAAA) |

Returns
:   0 if ok, <0 if error.

## [◆ ](#gab04f3b2347e9c59346c10180c6c9ffbc)dns\_resolve\_close()

| int dns\_resolve\_close | ( | struct [dns\_resolve\_context](structdns__resolve__context.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Close DNS resolving context.

This releases DNS resolving context and marks the context unusable. Caller must call the [dns\_resolve\_init()](#ga74e2be49894100fe5da641331ef083de) again to make context usable.

Parameters
:   | ctx | DNS context |
    | --- | --- |

Returns
:   0 if ok, <0 if error.

## [◆ ](#gae69cd758e99ea93ef8aac28366918b87)dns\_resolve\_get\_default()

| struct [dns\_resolve\_context](structdns__resolve__context.md) \* dns\_resolve\_get\_default | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Get default DNS context.

The system level DNS context uses DNS servers that are defined in project config file. If no DNS servers are defined by the user, then resolving DNS names using default DNS context will do nothing. The configuration options are described in subsys/net/lib/dns/Kconfig file.

Returns
:   Default DNS context.

## [◆ ](#ga74e2be49894100fe5da641331ef083de)dns\_resolve\_init()

| int dns\_resolve\_init | ( | struct [dns\_resolve\_context](structdns__resolve__context.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *dns\_servers\_str*[], |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *dns\_servers\_sa*[] ) |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Init DNS resolving context.

This function sets the DNS server address and initializes the DNS context that is used by the actual resolver. DNS server addresses can be specified either in textual form, or as struct sockaddr (or both). Note that the recommended way to resolve DNS names is to use the [dns\_get\_addr\_info()](#gaf891d7e21bddc8fbd029209b4339c01d) API. In that case user does not need to call [dns\_resolve\_init()](#ga74e2be49894100fe5da641331ef083de) as the DNS servers are already setup by the system.

Parameters
:   | ctx | DNS context. If the context variable is allocated from the stack, then the variable needs to be valid for the whole duration of the resolving. Caller does not need to fill the variable beforehand or edit the context afterwards. |
    | --- | --- |
    | dns\_servers\_str | DNS server addresses using textual strings. The array is NULL terminated. The port number can be given in the string. Syntax for the server addresses with or without port numbers: IPv4 : 10.0.9.1 IPv4 + port : 10.0.9.1:5353 IPv6 : 2001:db8::22:42 IPv6 + port : [2001:db8::22:42]:5353 |
    | dns\_servers\_sa | DNS server addresses as struct sockaddr. The array is NULL terminated. Port numbers are optional in struct sockaddr, the default will be used if set to 0. |

Returns
:   0 if ok, <0 if error.

## [◆ ](#ga71eab0f9dd0bc7c02c0d55e7dc6741f3)dns\_resolve\_init\_default()

| int dns\_resolve\_init\_default | ( | struct [dns\_resolve\_context](structdns__resolve__context.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Init DNS resolving context with default Kconfig options.

Parameters
:   | ctx | DNS context. |
    | --- | --- |

Returns
:   0 if ok, <0 if error.

## [◆ ](#ga24f9bc24e2021b6b528bb15e4fcca49b)dns\_resolve\_name()

| int dns\_resolve\_name | ( | struct [dns\_resolve\_context](structdns__resolve__context.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *query*, |
|  |  | enum [dns\_query\_type](#ga7169c5a920fb1b0d77910a6ab922e3f0) | *type*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *dns\_id*, |
|  |  | [dns\_resolve\_cb\_t](#gafe22d0ef90c581982561ef0c33d1f722) | *cb*, |
|  |  | void \* | *user\_data*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Resolve DNS name.

This function can be used to resolve e.g., IPv4 or IPv6 address. Note that this is asynchronous call, the function will return immediately and system will call the callback after resolving has finished or timeout has occurred. We might send the query to multiple servers (if there are more than one server configured), but we only use the result of the first received response.

Parameters
:   | ctx | DNS context |
    | --- | --- |
    | query | What the caller wants to resolve. |
    | type | What kind of data the caller wants to get. |
    | dns\_id | DNS id is returned to the caller. This is needed if one wishes to cancel the query. This can be set to NULL if there is no need to cancel the query. |
    | cb | Callback to call after the resolving has finished or timeout has happened. |
    | user\_data | The user data. |
    | timeout | The timeout value for the query. Possible values: SYS\_FOREVER\_MS: the query is tried forever, user needs to cancel it manually if it takes too long time to finish >0: start the query and let the system timeout it after specified ms |

Returns
:   0 if resolving was started ok, < 0 otherwise

## [◆ ](#ga54dc319f118e6a8e1e78435539c8f039)dns\_resolve\_reconfigure()

| int dns\_resolve\_reconfigure | ( | struct [dns\_resolve\_context](structdns__resolve__context.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *servers\_str*[], |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *servers\_sa*[], |
|  |  | enum [dns\_server\_source](#gaeda02f82b12e9b7b4dea9fd66be123a7) | *source* ) |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Reconfigure DNS resolving context.

Reconfigures DNS context with new server list.

Parameters
:   | ctx | DNS context |
    | --- | --- |
    | servers\_str | DNS server addresses using textual strings. The array is NULL terminated. The port number can be given in the string. Syntax for the server addresses with or without port numbers: IPv4 : 10.0.9.1 IPv4 + port : 10.0.9.1:5353 IPv6 : 2001:db8::22:42 IPv6 + port : [2001:db8::22:42]:5353 |
    | servers\_sa | DNS server addresses as struct sockaddr. The array is NULL terminated. Port numbers are optional in struct sockaddr, the default will be used if set to 0. |
    | source | Source of the DNS servers, e.g., manual, DHCPv4/6, etc. |

Returns
:   0 if ok, <0 if error.

## [◆ ](#ga211f9c8a5588186607e9257c4451f64d)dns\_resolve\_reconfigure\_with\_interfaces()

| int dns\_resolve\_reconfigure\_with\_interfaces | ( | struct [dns\_resolve\_context](structdns__resolve__context.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *servers\_str*[], |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *servers\_sa*[], |
|  |  | int | *interfaces*[], |
|  |  | enum [dns\_server\_source](#gaeda02f82b12e9b7b4dea9fd66be123a7) | *source* ) |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Reconfigure DNS resolving context with new server list and allowing servers to be specified to a specific network interface.

Parameters
:   | ctx | DNS context |
    | --- | --- |
    | servers\_str | DNS server addresses using textual strings. The array is NULL terminated. The port number can be given in the string. Syntax for the server addresses with or without port numbers: IPv4 : 10.0.9.1 IPv4 + port : 10.0.9.1:5353 IPv6 : 2001:db8::22:42 IPv6 + port : [2001:db8::22:42]:5353 |
    | servers\_sa | DNS server addresses as struct sockaddr. The array is NULL terminated. Port numbers are optional in struct sockaddr, the default will be used if set to 0. |
    | interfaces | Network interfaces to which the DNS servers are bound. This is an array of network interface indices. The array must be the same length as the servers\_str and servers\_sa arrays. |
    | source | Source of the DNS servers, e.g., manual, DHCPv4/6, etc. |

Returns
:   0 if ok, <0 if error.

## [◆ ](#ga54c85b9c69c9a44f2e7bb78165cebfcb)dns\_resolve\_remove()

| int dns\_resolve\_remove | ( | struct [dns\_resolve\_context](structdns__resolve__context.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | int | *if\_index* ) |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Remove servers from the DNS resolving context.

Parameters
:   | ctx | DNS context |
    | --- | --- |
    | if\_index | Network interface from which the DNS servers are removed. |

Returns
:   0 if ok, <0 if error.

## [◆ ](#gae292786587c511c223481f77a4f43017)dns\_resolve\_remove\_source()

| int dns\_resolve\_remove\_source | ( | struct [dns\_resolve\_context](structdns__resolve__context.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | int | *if\_index*, |
|  |  | enum [dns\_server\_source](#gaeda02f82b12e9b7b4dea9fd66be123a7) | *source* ) |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Remove servers from the DNS resolving context that were added by a specific source.

Parameters
:   | ctx | DNS context |
    | --- | --- |
    | if\_index | Network interface from which the DNS servers are removed. |
    | source | Source of the DNS servers, e.g., manual, DHCPv4/6, etc. |

Returns
:   0 if ok, <0 if error.

## [◆ ](#gaf28f6f8baa97d0b2341e1bdc02b6cb8c)dns\_resolve\_service()

| | int dns\_resolve\_service | ( | struct [dns\_resolve\_context](structdns__resolve__context.md) \* | *ctx*, | | --- | --- | --- | --- | |  |  | const char \* | *query*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *dns\_id*, | |  |  | [dns\_resolve\_cb\_t](#gafe22d0ef90c581982561ef0c33d1f722) | *cb*, | |  |  | void \* | *user\_data*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h.md)>`

Resolve DNS service.

This function can be used to resolve service records needed in DNS-SD service discovery. Note that this is an asynchronous call, the function will return immediately and the system will call the callback after resolving has finished or a timeout has occurred. We might send the query to multiple servers (if there are more than one server configured), but we only use the result of the first received response.

Parameters
:   | ctx | DNS context |
    | --- | --- |
    | query | What the caller wants to resolve. |
    | dns\_id | DNS id is returned to the caller. This is needed if one wishes to cancel the query. This can be set to NULL if there is no need to cancel the query. |
    | cb | Callback to call after the resolving has finished or timeout has happened. |
    | user\_data | The user data. |
    | timeout | The timeout value for the query. Possible values: SYS\_FOREVER\_MS: the query is tried forever, user needs to cancel it manually if it takes too long time to finish >0: start the query and let the system timeout it after specified ms |

Returns
:   0 if resolving was started ok, < 0 otherwise

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
