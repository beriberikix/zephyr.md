---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsocket__dns__offload.html
original_path: doxygen/html/structsocket__dns__offload.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_dns\_offload Struct Reference

An offloaded Socket DNS API interface.
[More...](#details)

`#include <[socket_offload.h](socket__offload_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [getaddrinfo](#a5241208180bcc8f553d0db6e74e5c115) )(const char \*node, const char \*service, const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints, struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res) |
| void(\* | [freeaddrinfo](#a73640bb24b4838c337ef1a61ffd4949f) )(struct [zsock\_addrinfo](structzsock__addrinfo.md) \*res) |

## Detailed Description

An offloaded Socket DNS API interface.

It is assumed that these offload functions follow the POSIX socket API standard for arguments, return values and setting of errno.

## Field Documentation

## [◆ ](#a73640bb24b4838c337ef1a61ffd4949f)freeaddrinfo

| void(\* socket\_dns\_offload::freeaddrinfo) (struct [zsock\_addrinfo](structzsock__addrinfo.md) \*res) |
| --- |

## [◆ ](#a5241208180bcc8f553d0db6e74e5c115)getaddrinfo

| int(\* socket\_dns\_offload::getaddrinfo) (const char \*node, const char \*service, const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints, struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket\_offload.h](socket__offload_8h_source.md)

- [socket\_dns\_offload](structsocket__dns__offload.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
