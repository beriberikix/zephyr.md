---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structtls__cert__verify__cb.html
original_path: doxygen/html/structtls__cert__verify__cb.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tls\_cert\_verify\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [BSD Sockets compatible API](group__bsd__sockets.md) » [Socket options for TLS](group__secure__sockets__options.md)

Data structure for [TLS\_CERT\_VERIFY\_CALLBACK](group__secure__sockets__options.md#ga6fc0f394602ae713426568c6371c0120 "TLS_CERT_VERIFY_CALLBACK") socket option.
[More...](#details)

`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [cb](#a242e581dda3056658842c233d49dbdb6) |
|  | A pointer to the certificate verification callback function. |
| void \* | [ctx](#aa342fd0888e95e4e1fddde750ee5b183) |
|  | A pointer to an opaque context passed to the callback. |

## Detailed Description

Data structure for [TLS\_CERT\_VERIFY\_CALLBACK](group__secure__sockets__options.md#ga6fc0f394602ae713426568c6371c0120 "TLS_CERT_VERIFY_CALLBACK") socket option.

## Field Documentation

## [◆ ](#a242e581dda3056658842c233d49dbdb6)cb

| void\* tls\_cert\_verify\_cb::cb |
| --- |

A pointer to the certificate verification callback function.

The actual callback function type is defined by mbed TLS, see documentation of mbedtls\_x509\_crt\_verify() function.

## [◆ ](#aa342fd0888e95e4e1fddde750ee5b183)ctx

| void\* tls\_cert\_verify\_cb::ctx |
| --- |

A pointer to an opaque context passed to the callback.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket.h](net_2socket_8h_source.md)

- [tls\_cert\_verify\_cb](structtls__cert__verify__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
