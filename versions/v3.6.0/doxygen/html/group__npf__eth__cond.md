---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__npf__eth__cond.html
original_path: doxygen/html/group__npf__eth__cond.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ethernet Filter Conditions

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Packet Filter API](group__net__pkt__filter.md)

| Macros | |
| --- | --- |
| #define | [NPF\_ETH\_SRC\_ADDR\_MATCH](#gad2141ad8d6639c9b92569d55130ca1b1)(\_name, \_addr\_array) |
|  | Statically define a "source address match" packet filter condition. |
| #define | [NPF\_ETH\_SRC\_ADDR\_UNMATCH](#ga228eaa3784f663d8f2e2711e26409043)(\_name, \_addr\_array) |
|  | Statically define a "source address unmatch" packet filter condition. |
| #define | [NPF\_ETH\_DST\_ADDR\_MATCH](#ga3d22d687bcd56b7727c51c7bc7f36cac)(\_name, \_addr\_array) |
|  | Statically define a "destination address match" packet filter condition. |
| #define | [NPF\_ETH\_DST\_ADDR\_UNMATCH](#ga3b8a8a22eb992c0e02223f70723c3641)(\_name, \_addr\_array) |
|  | Statically define a "destination address unmatch" packet filter condition. |
| #define | [NPF\_ETH\_SRC\_ADDR\_MASK\_MATCH](#ga0e06ebc4c9a1a960651be1ba89eeb2fd)(\_name, \_addr\_array, ...) |
|  | Statically define a "source address match with mask" packet filter condition. |
| #define | [NPF\_ETH\_DST\_ADDR\_MASK\_MATCH](#ga7cf793af7b91eccc6e675ff19ed59a14)(\_name, \_addr\_array, ...) |
|  | Statically define a "destination address match with mask" packet filter condition. |
| #define | [NPF\_ETH\_TYPE\_MATCH](#gace7de72d4c64e128a825f28f94d8b1b2)(\_name, \_type) |
|  | Statically define an "Ethernet type match" packet filter condition. |
| #define | [NPF\_ETH\_TYPE\_UNMATCH](#gab9bf6d58433e273220c5fab76f608545)(\_name, \_type) |
|  | Statically define an "Ethernet type unmatch" packet filter condition. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga7cf793af7b91eccc6e675ff19ed59a14)NPF\_ETH\_DST\_ADDR\_MASK\_MATCH

| #define NPF\_ETH\_DST\_ADDR\_MASK\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_addr\_array*, |
|  |  |  | ... ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_addr \_name = { \

.addresses = (\_addr\_array), \

.nb\_addresses = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_addr\_array), \

.mask.addr = { \_\_VA\_ARGS\_\_ }, \

.test.fn = npf\_eth\_dst\_addr\_match, \

}

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:124

Statically define a "destination address match with mask" packet filter condition.

This tests if the packet destination address matches any of the Ethernet addresses contained in the provided set after applying specified mask.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_addr\_array | Array of struct net\_eth\_addr items to test against |
    | ... | up to 6 mask bytes |

## [◆ ](#ga3d22d687bcd56b7727c51c7bc7f36cac)NPF\_ETH\_DST\_ADDR\_MATCH

| #define NPF\_ETH\_DST\_ADDR\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_addr\_array* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_addr \_name = { \

.addresses = (\_addr\_array), \

.nb\_addresses = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_addr\_array), \

.test.fn = npf\_eth\_dst\_addr\_match, \

.mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

}

Statically define a "destination address match" packet filter condition.

This tests if the packet destination address matches any of the Ethernet addresses contained in the provided set.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_addr\_array | Array of struct net\_eth\_addr items to test against |

## [◆ ](#ga3b8a8a22eb992c0e02223f70723c3641)NPF\_ETH\_DST\_ADDR\_UNMATCH

| #define NPF\_ETH\_DST\_ADDR\_UNMATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_addr\_array* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_addr \_name = { \

.addresses = (\_addr\_array), \

.nb\_addresses = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_addr\_array), \

.test.fn = npf\_eth\_dst\_addr\_unmatch, \

.mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

}

Statically define a "destination address unmatch" packet filter condition.

This tests if the packet destination address matches none of the Ethernet addresses contained in the provided set.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_addr\_array | Array of struct net\_eth\_addr items to test against |

## [◆ ](#ga0e06ebc4c9a1a960651be1ba89eeb2fd)NPF\_ETH\_SRC\_ADDR\_MASK\_MATCH

| #define NPF\_ETH\_SRC\_ADDR\_MASK\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_addr\_array*, |
|  |  |  | ... ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_addr \_name = { \

.addresses = (\_addr\_array), \

.nb\_addresses = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_addr\_array), \

.mask.addr = { \_\_VA\_ARGS\_\_ }, \

.test.fn = npf\_eth\_src\_addr\_match, \

}

Statically define a "source address match with mask" packet filter condition.

This tests if the packet source address matches any of the Ethernet addresses contained in the provided set after applying specified mask.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_addr\_array | Array of struct net\_eth\_addr items to test against |
    | ... | up to 6 mask bytes |

## [◆ ](#gad2141ad8d6639c9b92569d55130ca1b1)NPF\_ETH\_SRC\_ADDR\_MATCH

| #define NPF\_ETH\_SRC\_ADDR\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_addr\_array* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_addr \_name = { \

.addresses = (\_addr\_array), \

.nb\_addresses = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_addr\_array), \

.test.fn = npf\_eth\_src\_addr\_match, \

.mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

}

Statically define a "source address match" packet filter condition.

This tests if the packet source address matches any of the Ethernet addresses contained in the provided set.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_addr\_array | Array of struct net\_eth\_addr items to test against |

## [◆ ](#ga228eaa3784f663d8f2e2711e26409043)NPF\_ETH\_SRC\_ADDR\_UNMATCH

| #define NPF\_ETH\_SRC\_ADDR\_UNMATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_addr\_array* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_addr \_name = { \

.addresses = (\_addr\_array), \

.nb\_addresses = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_addr\_array), \

.test.fn = npf\_eth\_src\_addr\_unmatch, \

.mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

}

Statically define a "source address unmatch" packet filter condition.

This tests if the packet source address matches none of the Ethernet addresses contained in the provided set.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_addr\_array | Array of struct net\_eth\_addr items to test against |

## [◆ ](#gace7de72d4c64e128a825f28f94d8b1b2)NPF\_ETH\_TYPE\_MATCH

| #define NPF\_ETH\_TYPE\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_type* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_type \_name = { \

.type = [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(\_type), \

.test.fn = npf\_eth\_type\_match, \

}

[htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)

#define htons(x)

Convert 16-bit value from host to network byte order.

**Definition** net\_ip.h:120

Statically define an "Ethernet type match" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_type | Ethernet type to match |

## [◆ ](#gab9bf6d58433e273220c5fab76f608545)NPF\_ETH\_TYPE\_UNMATCH

| #define NPF\_ETH\_TYPE\_UNMATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_type* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_type \_name = { \

.type = [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(\_type), \

.test.fn = npf\_eth\_type\_unmatch, \

}

Statically define an "Ethernet type unmatch" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_type | Ethernet type to exclude |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
