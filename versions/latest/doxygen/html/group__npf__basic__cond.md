---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__npf__basic__cond.html
original_path: doxygen/html/group__npf__basic__cond.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Basic Filter Conditions

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Packet Filter API](group__net__pkt__filter.md)

| Macros | |
| --- | --- |
| #define | [NPF\_IFACE\_MATCH](#ga465578272b616c6267ecd13fd86ca73b)(\_name, \_iface) |
|  | Statically define an "interface match" packet filter condition. |
| #define | [NPF\_IFACE\_UNMATCH](#gac3607a6736d70b0ea044a2ec7ab6d313)(\_name, \_iface) |
|  | Statically define an "interface unmatch" packet filter condition. |
| #define | [NPF\_ORIG\_IFACE\_MATCH](#ga55021acd131e4684568aaf6434b08789)(\_name, \_iface) |
|  | Statically define an "orig interface match" packet filter condition. |
| #define | [NPF\_ORIG\_IFACE\_UNMATCH](#gad959dc62d47ca3b4d2f24a6c862c7623)(\_name, \_iface) |
|  | Statically define an "orig interface unmatch" packet filter condition. |
| #define | [NPF\_SIZE\_MIN](#gaf142455f9bea3dea8faa0a913072b63e)(\_name, \_size) |
|  | Statically define a "data minimum size" packet filter condition. |
| #define | [NPF\_SIZE\_MAX](#gacd56b9bcf2b2ba4759402650a9bff67a)(\_name, \_size) |
|  | Statically define a "data maximum size" packet filter condition. |
| #define | [NPF\_SIZE\_BOUNDS](#gab402bb13c7899d57532d3dcf8a36ed4b)(\_name, \_min\_size, \_max\_size) |
|  | Statically define a "data bounded size" packet filter condition. |
| #define | [NPF\_IP\_SRC\_ADDR\_ALLOWLIST](#ga4dd013f0fb92eb0433f174cf40e89e00)(\_name, \_ip\_addr\_array, \_ip\_addr\_num, \_af) |
|  | Statically define a "ip address allowlist" packet filter condition. |
| #define | [NPF\_IP\_SRC\_ADDR\_BLOCKLIST](#ga57fe28a992b1afaf33581292fe5015bd)(\_name, \_ip\_addr\_array, \_ip\_addr\_num, \_af) |
|  | Statically define a "ip address blocklist" packet filter condition. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga465578272b616c6267ecd13fd86ca73b)NPF\_IFACE\_MATCH

| #define NPF\_IFACE\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_iface* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_iface \_name = { \

.iface = (\_iface), \

.test.fn = npf\_iface\_match, \

}

Statically define an "interface match" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_iface | Interface to match |

## [◆ ](#gac3607a6736d70b0ea044a2ec7ab6d313)NPF\_IFACE\_UNMATCH

| #define NPF\_IFACE\_UNMATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_iface* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_iface \_name = { \

.iface = (\_iface), \

.test.fn = npf\_iface\_unmatch, \

}

Statically define an "interface unmatch" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_iface | Interface to exclude |

## [◆ ](#ga4dd013f0fb92eb0433f174cf40e89e00)NPF\_IP\_SRC\_ADDR\_ALLOWLIST

| #define NPF\_IP\_SRC\_ADDR\_ALLOWLIST | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_ip\_addr\_array*, |
|  |  |  | *\_ip\_addr\_num*, |
|  |  |  | *\_af* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_ip \_name = { \

.addr\_family = \_af, \

.ipaddr = (\_ip\_addr\_array), \

.ipaddr\_num = \_ip\_addr\_num, \

.test.fn = npf\_ip\_src\_addr\_match, \

}

Statically define a "ip address allowlist" packet filter condition.

This tests if the packet source ip address matches any of the ip addresses contained in the provided set.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_ip\_addr\_array | Array of struct [in\_addr](structin__addr.md "IPv4 address struct.") or struct [in6\_addr](structin6__addr.md "IPv6 address struct.") items to test against |
    | \_ip\_addr\_num | number of IP addresses in the array |
    | \_af | Addresses family type (AF\_INET / AF\_INET6) in the array |

## [◆ ](#ga57fe28a992b1afaf33581292fe5015bd)NPF\_IP\_SRC\_ADDR\_BLOCKLIST

| #define NPF\_IP\_SRC\_ADDR\_BLOCKLIST | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_ip\_addr\_array*, |
|  |  |  | *\_ip\_addr\_num*, |
|  |  |  | *\_af* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_ip \_name = { \

.addr\_family = \_af, \

.ipaddr = (\_ip\_addr\_array), \

.ipaddr\_num = \_ip\_addr\_num, \

.test.fn = npf\_ip\_src\_addr\_unmatch, \

}

Statically define a "ip address blocklist" packet filter condition.

This tests if the packet source ip address matches any of the ip addresses contained in the provided set.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_ip\_addr\_array | Array of struct [in\_addr](structin__addr.md "IPv4 address struct.") or struct [in6\_addr](structin6__addr.md "IPv6 address struct.") items to test against |
    | \_ip\_addr\_num | number of IP addresses in the array |
    | \_af | Addresses family type (AF\_INET / AF\_INET6) in the array |

## [◆ ](#ga55021acd131e4684568aaf6434b08789)NPF\_ORIG\_IFACE\_MATCH

| #define NPF\_ORIG\_IFACE\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_iface* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_iface \_name = { \

.iface = (\_iface), \

.test.fn = npf\_orig\_iface\_match, \

}

Statically define an "orig interface match" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_iface | Interface to match |

## [◆ ](#gad959dc62d47ca3b4d2f24a6c862c7623)NPF\_ORIG\_IFACE\_UNMATCH

| #define NPF\_ORIG\_IFACE\_UNMATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_iface* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_iface \_name = { \

.iface = (\_iface), \

.test.fn = npf\_orig\_iface\_unmatch, \

}

Statically define an "orig interface unmatch" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_iface | Interface to exclude |

## [◆ ](#gab402bb13c7899d57532d3dcf8a36ed4b)NPF\_SIZE\_BOUNDS

| #define NPF\_SIZE\_BOUNDS | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_min\_size*, |
|  |  |  | *\_max\_size* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_size\_bounds \_name = { \

.min = (\_min\_size), \

.max = (\_max\_size), \

.test.fn = npf\_size\_inbounds, \

}

Statically define a "data bounded size" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_min\_size | Lower bound of the packet's data size |
    | \_max\_size | Higher bound of the packet's data size |

## [◆ ](#gacd56b9bcf2b2ba4759402650a9bff67a)NPF\_SIZE\_MAX

| #define NPF\_SIZE\_MAX | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_size* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_size\_bounds \_name = { \

.min = 0, \

.max = (\_size), \

.test.fn = npf\_size\_inbounds, \

}

Statically define a "data maximum size" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_size | Higher bound of the packet's data size |

## [◆ ](#gaf142455f9bea3dea8faa0a913072b63e)NPF\_SIZE\_MIN

| #define NPF\_SIZE\_MIN | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_size* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_size\_bounds \_name = { \

.min = (\_size), \

.max = [SIZE\_MAX](stdint_8h.md#a3c75bb398badb69c7577b21486f9963f), \

.test.fn = npf\_size\_inbounds, \

}

[SIZE\_MAX](stdint_8h.md#a3c75bb398badb69c7577b21486f9963f)

#define SIZE\_MAX

**Definition** stdint.h:70

Statically define a "data minimum size" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_size | Lower bound of the packet's data size |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
