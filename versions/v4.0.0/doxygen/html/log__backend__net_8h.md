---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__backend__net_8h.html
original_path: doxygen/html/log__backend__net_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_net.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`

[Go to the source code of this file.](log__backend__net_8h_source.md)

| Functions | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [log\_backend\_net\_set\_addr](#a127f2042973746f183bd3562821844cf) (const char \*addr) |
|  | Allows user to set a server IP address, provided as string, at runtime. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [log\_backend\_net\_set\_ip](#aae909fb9ee8e4dbd773f44a2666dfa3a) (const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Allows user to set a server IP address, provided as sockaddr structure, at runtime. |
| static void | [log\_backend\_net\_hostname\_set](#a539dafe8aba869f11d244db4820baf8d) (const char \*hostname, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | update the hostname |
| const struct [log\_backend](structlog__backend.md) \* | [log\_backend\_net\_get](#a6513cd9aabc8f594347d14901112f32e) (void) |
|  | Get the net logger backend. |
| void | [log\_backend\_net\_start](#aab57f963e8a9e88b1e9483872e737466) (void) |
|  | Start the net logger backend. |

## Function Documentation

## [◆ ](#a6513cd9aabc8f594347d14901112f32e)log\_backend\_net\_get()

| const struct [log\_backend](structlog__backend.md) \* log\_backend\_net\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the net logger backend.

This function returns the net logger backend.

Returns
:   Pointer to the net logger backend.

## [◆ ](#a539dafe8aba869f11d244db4820baf8d)log\_backend\_net\_hostname\_set()

| | void log\_backend\_net\_hostname\_set | ( | const char \* | *hostname*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

update the hostname

This function allows to update the hostname displayed by the logging backend. It will be called by the network stack if the hostname is set with [net\_hostname\_set()](group__net__hostname.md#ga2131a7beddae249cc5a93392c44a1b27 "Set the device hostname.").

Parameters
:   | hostname | new hostname as char array. |
    | --- | --- |
    | len | Length of the hostname array. |

## [◆ ](#a127f2042973746f183bd3562821844cf)log\_backend\_net\_set\_addr()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) log\_backend\_net\_set\_addr | ( | const char \* | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

Allows user to set a server IP address, provided as string, at runtime.

This function allows the user to set an IPv4 or IPv6 address at runtime. It can be called either before or after the backend has been initialized. If it gets called when the net logger backend context is running, it'll release it and create another one with the new address next time process() gets called.

Parameters
:   | addr | String that contains the IP address. |
    | --- | --- |

Returns
:   True if parsing could be done, false otherwise.

## [◆ ](#aae909fb9ee8e4dbd773f44a2666dfa3a)log\_backend\_net\_set\_ip()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) log\_backend\_net\_set\_ip | ( | const struct [sockaddr](structsockaddr.md) \* | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

Allows user to set a server IP address, provided as sockaddr structure, at runtime.

This function allows the user to set an IPv4 or IPv6 address at runtime. It can be called either before or after the backend has been initialized. If it gets called when the net logger backend context is running, it'll release it and create another one with the new address next time process() gets called.

Parameters
:   | addr | Pointer to the sockaddr structure that contains the IP address. |
    | --- | --- |

Returns
:   True if address could be set, false otherwise.

## [◆ ](#aab57f963e8a9e88b1e9483872e737466)log\_backend\_net\_start()

| void log\_backend\_net\_start | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Start the net logger backend.

This function starts the net logger backend.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_net.h](log__backend__net_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
