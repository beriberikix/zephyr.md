---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dns__resolve_8h.html
original_path: doxygen/html/dns__resolve_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dns\_resolve.h File Reference

DNS resolving library.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/socket_poll.h](socket__poll_8h_source.md)>`  
`#include <[zephyr/net/net_core.h](net__core_8h_source.md)>`

[Go to the source code of this file.](dns__resolve_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [dns\_addrinfo](structdns__addrinfo.md) |
|  | Address info struct is passed to callback that gets all the results. [More...](structdns__addrinfo.md#details) |
| struct | [dns\_resolve\_context](structdns__resolve__context.md) |
|  | DNS resolve context structure. [More...](structdns__resolve__context.md#details) |
| struct | [dns\_resolve\_context::dns\_server](structdns__resolve__context_1_1dns__server.md) |
|  | List of configured DNS servers. [More...](structdns__resolve__context_1_1dns__server.md#details) |
| struct | [dns\_resolve\_context::dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md) |
|  | Result callbacks. [More...](structdns__resolve__context_1_1dns__pending__query.md#details) |

| Macros | |
| --- | --- |
| #define | [DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db)   20 |
|  | Max size of the resolved name. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722)) (enum [dns\_resolve\_status](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e) status, struct [dns\_addrinfo](structdns__addrinfo.md) \*info, void \*user\_data) |
|  | DNS resolve callback. |

| Enumerations | |
| --- | --- |
| enum | [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) { [DNS\_QUERY\_TYPE\_A](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134) = 1 , [DNS\_QUERY\_TYPE\_AAAA](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049) = 28 } |
|  | DNS query type enum. [More...](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) |
| enum | [dns\_resolve\_status](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e) {     [DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) = -2 , [DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) = -3 , [DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) = -4 , [DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) = -5 ,     [DNS\_EAI\_ADDRFAMILY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d) = -9 , [DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) = -10 , [DNS\_EAI\_OVERFLOW](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f) = -12 , [DNS\_EAI\_INPROGRESS](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3) = -100 ,     [DNS\_EAI\_CANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3) = -101 , [DNS\_EAI\_NOTCANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f) = -102 , [DNS\_EAI\_ALLDONE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836) = -103 , [DNS\_EAI\_IDN\_ENCODE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4) = -105   } |
|  | Status values for the callback. [More...](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e) |

| Functions | |
| --- | --- |
| int | [dns\_resolve\_init](group__dns__resolve.md#ga74e2be49894100fe5da641331ef083de) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, const char \*dns\_servers\_str[], const struct [sockaddr](structsockaddr.md) \*dns\_servers\_sa[]) |
|  | Init DNS resolving context. |
| int | [dns\_resolve\_init\_default](group__dns__resolve.md#ga71eab0f9dd0bc7c02c0d55e7dc6741f3) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx) |
|  | Init DNS resolving context with default Kconfig options. |
| int | [dns\_resolve\_close](group__dns__resolve.md#gab04f3b2347e9c59346c10180c6c9ffbc) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx) |
|  | Close DNS resolving context. |
| int | [dns\_resolve\_reconfigure](group__dns__resolve.md#ga9da2d7299cfafcdea7d6bfe0e4a2223c) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, const char \*servers\_str[], const struct [sockaddr](structsockaddr.md) \*servers\_sa[]) |
|  | Reconfigure DNS resolving context. |
| int | [dns\_resolve\_cancel](group__dns__resolve.md#ga7701ddd6b6c5923f0d122a2bcf898cbf) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id) |
|  | Cancel a pending DNS query. |
| int | [dns\_resolve\_cancel\_with\_name](group__dns__resolve.md#gaf2854ca9b839e7cba073e75202ac7e38) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id, const char \*query\_name, enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) query\_type) |
|  | Cancel a pending DNS query using id, name and type. |
| int | [dns\_resolve\_name](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b) (struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, const char \*query, enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) type, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dns\_id, [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) cb, void \*user\_data, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Resolve DNS name. |
| struct [dns\_resolve\_context](structdns__resolve__context.md) \* | [dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87) (void) |
|  | Get default DNS context. |
| static int | [dns\_get\_addr\_info](group__dns__resolve.md#gaf891d7e21bddc8fbd029209b4339c01d) (const char \*query, enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) type, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dns\_id, [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) cb, void \*user\_data, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Get IP address info from DNS. |
| static int | [dns\_cancel\_addr\_info](group__dns__resolve.md#ga54ae7aaf53b36951b27f09e1cc82df55) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id) |
|  | Cancel a pending DNS query. |

## Detailed Description

DNS resolving library.

An API for applications to resolve a DNS name.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dns\_resolve.h](dns__resolve_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
