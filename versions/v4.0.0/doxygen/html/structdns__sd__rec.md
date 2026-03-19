---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structdns__sd__rec.html
original_path: doxygen/html/structdns__sd__rec.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dns\_sd\_rec Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [DNS Service Discovery](group__dns__sd.md)

DNS Service Discovery record.
[More...](#details)

`#include <[dns_sd.h](dns__sd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [instance](#a06a8d777d302f99a7ed8f4ddb7e3af7d) |
|  | "<Instance>" - e.g. |
| const char \* | [service](#ae944cbdafdaced49f7302292d23ea4f8) |
|  | Top half of the "<Service>" such as "\_http". |
| const char \* | [proto](#ad79c74e22f4546826b1de6c41402aa3e) |
|  | Bottom half of the "<Service>" "\_tcp" or "\_udp". |
| const char \* | [domain](#ad282799583cde5b60ae19d5f919c67fc) |
|  | "<Domain>" such as "local" or "zephyrproject.org" |
| const char \* | [text](#ae0585e5a0643a483d6ad12b7ff853323) |
|  | DNS TXT record. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [text\_size](#a852f246f90d3608acd3b660f57a59dfb) |
|  | Size (in bytes) of the DNS TXT record. |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | [port](#a714f196f0d5297d511d97f88c18aa993) |
|  | A pointer to the port number used by the service. |

## Detailed Description

DNS Service Discovery record.

This structure used in the implementation of RFC 6763 and should not need to be accessed directly from application code.

The *port* pointer must be non-NULL. When the value in *port* is non-zero, the service is advertised as being on that particular port. When the value in *port* is zero, then the service is not advertised.

Thus, it is possible for multiple services to advertise on a particular port if they hard-code the port.

See also
:   [RFC 6763](https://tools.ietf.org/html/rfc6763)

## Field Documentation

## [◆ ](#ad282799583cde5b60ae19d5f919c67fc)domain

| const char\* dns\_sd\_rec::domain |
| --- |

"<Domain>" such as "local" or "zephyrproject.org"

## [◆ ](#a06a8d777d302f99a7ed8f4ddb7e3af7d)instance

| const char\* dns\_sd\_rec::instance |
| --- |

"<Instance>" - e.g.

"My HTTP Server"

## [◆ ](#a714f196f0d5297d511d97f88c18aa993)port

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)\* dns\_sd\_rec::port |
| --- |

A pointer to the port number used by the service.

## [◆ ](#ad79c74e22f4546826b1de6c41402aa3e)proto

| const char\* dns\_sd\_rec::proto |
| --- |

Bottom half of the "<Service>" "\_tcp" or "\_udp".

## [◆ ](#ae944cbdafdaced49f7302292d23ea4f8)service

| const char\* dns\_sd\_rec::service |
| --- |

Top half of the "<Service>" such as "\_http".

## [◆ ](#ae0585e5a0643a483d6ad12b7ff853323)text

| const char\* dns\_sd\_rec::text |
| --- |

DNS TXT record.

## [◆ ](#a852f246f90d3608acd3b660f57a59dfb)text\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dns\_sd\_rec::text\_size |
| --- |

Size (in bytes) of the DNS TXT record.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[dns\_sd.h](dns__sd_8h_source.md)

- [dns\_sd\_rec](structdns__sd__rec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
