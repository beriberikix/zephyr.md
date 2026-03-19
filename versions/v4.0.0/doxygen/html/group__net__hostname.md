---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__net__hostname.html
original_path: doxygen/html/group__net__hostname.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Hostname Library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network hostname configuration library.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [NET\_HOSTNAME\_MAX\_LEN](#ga9dda37a09616f2eb1bcdcb76cd868a0f) |
|  | Maximum hostname length. |

| Functions | |
| --- | --- |
| static const char \* | [net\_hostname\_get](#ga8870e80f16f934d1d8a86ea6bddbaf0b) (void) |
|  | Get the device hostname. |
| static int | [net\_hostname\_set](#ga2131a7beddae249cc5a93392c44a1b27) (char \*host, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Set the device hostname. |
| static void | [net\_hostname\_init](#ga96adbfaa629b6d450f06e19678eba9bc) (void) |
|  | Initialize and set the device hostname. |
| static int | [net\_hostname\_set\_postfix](#ga6aa3799b3b0d7eec7fb8b276485ae2c5) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hostname\_postfix, int postfix\_len) |
|  | Set the device hostname postfix. |
| static int | [net\_hostname\_set\_postfix\_str](#ga2b9d6f604afcde27b6d1543495e2ba8b) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hostname\_postfix, int postfix\_len) |
|  | Set the postfix string for the network hostname. |

## Detailed Description

Network hostname configuration library.

Since
:   1.10

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#ga9dda37a09616f2eb1bcdcb76cd868a0f)NET\_HOSTNAME\_MAX\_LEN

| #define NET\_HOSTNAME\_MAX\_LEN |
| --- |

`#include <[hostname.h](hostname_8h.md)>`

**Value:**

(sizeof(CONFIG\_NET\_HOSTNAME) - 1 + \

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_HOSTNAME\_UNIQUE) ? sizeof("0011223344556677") - 1 : 0))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:140

Maximum hostname length.

## Function Documentation

## [◆ ](#ga8870e80f16f934d1d8a86ea6bddbaf0b)net\_hostname\_get()

| | const char \* net\_hostname\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hostname.h](hostname_8h.md)>`

Get the device hostname.

Return pointer to device hostname.

Returns
:   Pointer to hostname or NULL if not set.

## [◆ ](#ga96adbfaa629b6d450f06e19678eba9bc)net\_hostname\_init()

| | void net\_hostname\_init | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hostname.h](hostname_8h.md)>`

Initialize and set the device hostname.

## [◆ ](#ga2131a7beddae249cc5a93392c44a1b27)net\_hostname\_set()

| | int net\_hostname\_set | ( | char \* | *host*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hostname.h](hostname_8h.md)>`

Set the device hostname.

Parameters
:   | host | new hostname as char array. |
    | --- | --- |
    | len | Length of the hostname array. |

Returns
:   0 if ok, <0 on error

## [◆ ](#ga6aa3799b3b0d7eec7fb8b276485ae2c5)net\_hostname\_set\_postfix()

| | int net\_hostname\_set\_postfix | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *hostname\_postfix*, | | --- | --- | --- | --- | |  |  | int | *postfix\_len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hostname.h](hostname_8h.md)>`

Set the device hostname postfix.

Convert the hostname postfix to hexadecimal value and set the device hostname with the converted value. This is only used if CONFIG\_NET\_HOSTNAME\_UNIQUE is set.

Parameters
:   | hostname\_postfix | Usually link address. The function will convert this to a hexadecimal string. |
    | --- | --- |
    | postfix\_len | Length of the hostname\_postfix array. |

Returns
:   0 if ok, <0 if error

## [◆ ](#ga2b9d6f604afcde27b6d1543495e2ba8b)net\_hostname\_set\_postfix\_str()

| | int net\_hostname\_set\_postfix\_str | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *hostname\_postfix*, | | --- | --- | --- | --- | |  |  | int | *postfix\_len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hostname.h](hostname_8h.md)>`

Set the postfix string for the network hostname.

Set the hostname postfix string for the network hostname as is, without any conversion. This is only used if CONFIG\_NET\_HOSTNAME\_UNIQUE is set. The function checks if the combined length of the default hostname (defined by CONFIG\_NET\_HOSTNAME) and the postfix does not exceed NET\_HOSTNAME\_MAX\_LEN. If the postfix is too long, the function returns an error.

Parameters
:   | hostname\_postfix | Pointer to the postfix string to be appended to the network hostname. |
    | --- | --- |
    | postfix\_len | Length of the hostname\_postfix array. |

Returns
:   0 if ok, <0 if error

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
