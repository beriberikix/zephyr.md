---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/socketutils_8h.html
original_path: doxygen/html/socketutils_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socketutils.h File Reference

`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`

[Go to the source code of this file.](socketutils_8h_source.md)

| Functions | |
| --- | --- |
| const char \* | [net\_addr\_str\_find\_port](#aae0889a4a96fd9763e3f5337b4703205) (const char \*addr\_str) |
|  | Find port in addr:port string. |
| int | [net\_getaddrinfo\_addr\_str](#ab60f526101571078d9b24055f130b1a0) (const char \*addr\_str, const char \*def\_port, const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints, struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res) |
|  | Call [getaddrinfo()](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c "POSIX wrapper for zsock_getaddrinfo.") on addr:port string. |

## Function Documentation

## [◆ ](#aae0889a4a96fd9763e3f5337b4703205)net\_addr\_str\_find\_port()

| const char \* net\_addr\_str\_find\_port | ( | const char \* | *addr\_str* | ) |  |
| --- | --- | --- | --- | --- | --- |

Find port in addr:port string.

Parameters
:   | addr\_str | String of addr[:port] format |
    | --- | --- |

Returns
:   Pointer to "port" part, or NULL is none.

## [◆ ](#ab60f526101571078d9b24055f130b1a0)net\_getaddrinfo\_addr\_str()

| int net\_getaddrinfo\_addr\_str | ( | const char \* | *addr\_str*, |
| --- | --- | --- | --- |
|  |  | const char \* | *def\_port*, |
|  |  | const struct [zsock\_addrinfo](structzsock__addrinfo.md) \* | *hints*, |
|  |  | struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\* | *res* ) |

Call [getaddrinfo()](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c "POSIX wrapper for zsock_getaddrinfo.") on addr:port string.

Convenience function to split addr[:port] string into address vs port components (or use default port number), and call [getaddrinfo()](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c "POSIX wrapper for zsock_getaddrinfo.") on the result.

Parameters
:   | addr\_str | String of addr[:port] format |
    | --- | --- |
    | def\_port | Default port number to use if addr\_str doesn't contain it |
    | hints | [getaddrinfo()](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c "POSIX wrapper for zsock_getaddrinfo.") hints |
    | res | Result of [getaddrinfo()](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c "POSIX wrapper for zsock_getaddrinfo.") ([freeaddrinfo()](group__bsd__sockets.md#gaf70cde067b55e04adff98d672fa41c94 "POSIX wrapper for zsock_freeaddrinfo.") should be called on it as usual. |

Returns
:   Result of [getaddrinfo()](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c "POSIX wrapper for zsock_getaddrinfo.") call.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socketutils.h](socketutils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
