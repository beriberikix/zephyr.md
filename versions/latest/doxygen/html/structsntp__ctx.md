---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsntp__ctx.html
original_path: doxygen/html/structsntp__ctx.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sntp\_ctx Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [SNTP](group__sntp.md)

SNTP context.
[More...](#details)

`#include <[sntp.h](sntp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| struct [zsock\_pollfd](structzsock__pollfd.md)   [fds](#a6eec3a1aab8430c5edf39f9f386ee51a) [1] |  |
| int   [nfds](#a388a7d7591a6d76df83d975276398a25) |  |
| int   [fd](#a46b36989e639c675caa3a729dffc8f65) |  |
| } | [sock](#a297ca36079700db840de4a5b3d247611) |
| struct [sntp\_time](structsntp__time.md) | [expected\_orig\_ts](#a58bd69ad86d00183e32ed07a9fbebfdc) |
|  | Timestamp when the request was sent from client to server. |

## Detailed Description

SNTP context.

## Field Documentation

## [◆ ](#a58bd69ad86d00183e32ed07a9fbebfdc)expected\_orig\_ts

| struct [sntp\_time](structsntp__time.md) sntp\_ctx::expected\_orig\_ts |
| --- |

Timestamp when the request was sent from client to server.

This is used to check if the originated timestamp in the server reply matches the one in client request.

## [◆ ](#a46b36989e639c675caa3a729dffc8f65)fd

| int sntp\_ctx::fd |
| --- |

## [◆ ](#a6eec3a1aab8430c5edf39f9f386ee51a)fds

| struct [zsock\_pollfd](structzsock__pollfd.md) sntp\_ctx::fds[1] |
| --- |

## [◆ ](#a388a7d7591a6d76df83d975276398a25)nfds

| int sntp\_ctx::nfds |
| --- |

## [◆ ](#a297ca36079700db840de4a5b3d247611)[struct]

| struct { ... } sntp\_ctx::sock |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[sntp.h](sntp_8h_source.md)

- [sntp\_ctx](structsntp__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
