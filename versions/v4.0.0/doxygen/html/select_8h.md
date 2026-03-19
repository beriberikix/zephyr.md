---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/select_8h.html
original_path: doxygen/html/select_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

select.h File Reference

`#include <[zephyr/posix/posix_types.h](posix__types_8h_source.md)>`  
`#include <[zephyr/sys/fdtable.h](fdtable_8h_source.md)>`

[Go to the source code of this file.](select_8h_source.md)

| Macros | |
| --- | --- |
| #define | [FD\_SETSIZE](#a86c5dbf5a99358e288f573d6a1e0873f)   [ZVFS\_FD\_SETSIZE](fdtable_8h.md#ae8d10dc8bd02e619f8c384c493f53709) |

| Typedefs | |
| --- | --- |
| typedef struct [zvfs\_fd\_set](structzvfs__fd__set.md) | [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) |

| Functions | |
| --- | --- |
| int | [pselect](#a2aed0a9b18a0ac6a3b8bb3ea9c3a34ab) (int nfds, [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \*readfds, [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \*writefds, [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \*exceptfds, const struct [timespec](structtimespec.md) \*timeout, const void \*sigmask) |
| int | [select](#a7ffa34f8c9a12e7fd43f5ef65bf889fa) (int nfds, [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \*readfds, [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \*writefds, [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \*errorfds, struct [timeval](structtimeval.md) \*timeout) |
| void | [FD\_CLR](#a0835759308c63ca23a1760980eea21d7) (int fd, [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \*fdset) |
| int | [FD\_ISSET](#ac38fe1ff5db5e46e778f13ad5accdf98) (int fd, [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \*fdset) |
| void | [FD\_SET](#a8c14b5b455292781fbcc2e34a47923d6) (int fd, [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \*fdset) |
| void | [FD\_ZERO](#a3f88268fa19b2068723de10d848e8a42) ([fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \*fdset) |

## Macro Definition Documentation

## [◆ ](#a86c5dbf5a99358e288f573d6a1e0873f)FD\_SETSIZE

| #define FD\_SETSIZE   [ZVFS\_FD\_SETSIZE](fdtable_8h.md#ae8d10dc8bd02e619f8c384c493f53709) |
| --- |

## Typedef Documentation

## [◆ ](#ae96e561afd32b1445d8a7370f23762a2)fd\_set

| typedef struct [zvfs\_fd\_set](structzvfs__fd__set.md) [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) |
| --- |

## Function Documentation

## [◆ ](#a0835759308c63ca23a1760980eea21d7)FD\_CLR()

| void FD\_CLR | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \* | *fdset* ) |

## [◆ ](#ac38fe1ff5db5e46e778f13ad5accdf98)FD\_ISSET()

| int FD\_ISSET | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \* | *fdset* ) |

## [◆ ](#a8c14b5b455292781fbcc2e34a47923d6)FD\_SET()

| void FD\_SET | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \* | *fdset* ) |

## [◆ ](#a3f88268fa19b2068723de10d848e8a42)FD\_ZERO()

| void FD\_ZERO | ( | [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \* | *fdset* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a2aed0a9b18a0ac6a3b8bb3ea9c3a34ab)pselect()

| int pselect | ( | int | *nfds*, |
| --- | --- | --- | --- |
|  |  | [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \* | *readfds*, |
|  |  | [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \* | *writefds*, |
|  |  | [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \* | *exceptfds*, |
|  |  | const struct [timespec](structtimespec.md) \* | *timeout*, |
|  |  | const void \* | *sigmask* ) |

## [◆ ](#a7ffa34f8c9a12e7fd43f5ef65bf889fa)select()

| int select | ( | int | *nfds*, |
| --- | --- | --- | --- |
|  |  | [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \* | *readfds*, |
|  |  | [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \* | *writefds*, |
|  |  | [fd\_set](#ae96e561afd32b1445d8a7370f23762a2) \* | *errorfds*, |
|  |  | struct [timeval](structtimeval.md) \* | *timeout* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [select.h](select_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
