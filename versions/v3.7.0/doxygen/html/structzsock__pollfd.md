---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structzsock__pollfd.html
original_path: doxygen/html/structzsock__pollfd.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zsock\_pollfd Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [BSD Sockets compatible API](group__bsd__sockets.md)

Definition of the monitored socket/file descriptor.
[More...](#details)

`#include <[socket_poll.h](socket__poll_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [fd](#a58fcd3f9af542bb15a936319aaf9c32e) |
|  | Socket descriptor. |
| short | [events](#a31929c24c64b58c6f7e443645352f67d) |
|  | Requested events. |
| short | [revents](#a98838f19b29e759a4b53db9b15349917) |
|  | Returned events. |

## Detailed Description

Definition of the monitored socket/file descriptor.

An array of these descriptors is passed as an argument to [poll()](group__bsd__sockets.md#gae2d9b8390c125624595e2b400a08ea29 "POSIX wrapper for zsock_poll.").

## Field Documentation

## [◆ ](#a31929c24c64b58c6f7e443645352f67d)events

| short zsock\_pollfd::events |
| --- |

Requested events.

## [◆ ](#a58fcd3f9af542bb15a936319aaf9c32e)fd

| int zsock\_pollfd::fd |
| --- |

Socket descriptor.

## [◆ ](#a98838f19b29e759a4b53db9b15349917)revents

| short zsock\_pollfd::revents |
| --- |

Returned events.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket\_poll.h](socket__poll_8h_source.md)

- [zsock\_pollfd](structzsock__pollfd.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
