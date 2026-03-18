---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/poll_8h.html
original_path: doxygen/html/poll_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

poll.h File Reference

`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`

[Go to the source code of this file.](poll_8h_source.md)

| Macros | |
| --- | --- |
| #define | [pollfd](#af78a57e8ee17b7ecfe4510253d858afd)   [zsock\_pollfd](structzsock__pollfd.md) |
| #define | [POLLIN](#a52ac479a805051f59643588b096024ff)   [ZSOCK\_POLLIN](group__bsd__sockets.md#ga6ade0deb4952e1ea23b368d9eceee9ed) |
| #define | [POLLOUT](#a91b3c67129ac7675062f316b840a0d58)   [ZSOCK\_POLLOUT](group__bsd__sockets.md#ga9ca302c64dfb676798ce03100894ca3e) |
| #define | [POLLERR](#ab1c532446408c98559d4aaaeeeb99820)   [ZSOCK\_POLLERR](group__bsd__sockets.md#gad44368a112fbf91436a2439e7b767641) |
| #define | [POLLHUP](#a262754fe6bdf27c2cd3da43284ec8536)   [ZSOCK\_POLLHUP](group__bsd__sockets.md#gadd341cd5c1f6d7deeaedc5c58dc56fe7) |
| #define | [POLLNVAL](#ae8bffe35c61e12fb7b408b89721896df)   [ZSOCK\_POLLNVAL](group__bsd__sockets.md#ga45c5b0efca6e09e4f7db78d1d007bf67) |

| Functions | |
| --- | --- |
| int | [poll](#afa7e83ddea0ab5b08fcf614b89ac48ba) (struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int nfds, int timeout) |

## Macro Definition Documentation

## [◆ ](#ab1c532446408c98559d4aaaeeeb99820)POLLERR

| #define POLLERR   [ZSOCK\_POLLERR](group__bsd__sockets.md#gad44368a112fbf91436a2439e7b767641) |
| --- |

## [◆ ](#af78a57e8ee17b7ecfe4510253d858afd)pollfd

| #define pollfd   [zsock\_pollfd](structzsock__pollfd.md) |
| --- |

## [◆ ](#a262754fe6bdf27c2cd3da43284ec8536)POLLHUP

| #define POLLHUP   [ZSOCK\_POLLHUP](group__bsd__sockets.md#gadd341cd5c1f6d7deeaedc5c58dc56fe7) |
| --- |

## [◆ ](#a52ac479a805051f59643588b096024ff)POLLIN

| #define POLLIN   [ZSOCK\_POLLIN](group__bsd__sockets.md#ga6ade0deb4952e1ea23b368d9eceee9ed) |
| --- |

## [◆ ](#ae8bffe35c61e12fb7b408b89721896df)POLLNVAL

| #define POLLNVAL   [ZSOCK\_POLLNVAL](group__bsd__sockets.md#ga45c5b0efca6e09e4f7db78d1d007bf67) |
| --- |

## [◆ ](#a91b3c67129ac7675062f316b840a0d58)POLLOUT

| #define POLLOUT   [ZSOCK\_POLLOUT](group__bsd__sockets.md#ga9ca302c64dfb676798ce03100894ca3e) |
| --- |

## Function Documentation

## [◆ ](#afa7e83ddea0ab5b08fcf614b89ac48ba)poll()

| int poll | ( | struct [zsock\_pollfd](structzsock__pollfd.md) \* | *fds*, |
| --- | --- | --- | --- |
|  |  | int | *nfds*, |
|  |  | int | *timeout* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [poll.h](poll_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
