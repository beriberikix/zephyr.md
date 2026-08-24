---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__npf__eth__cond.html
original_path: doxygen/html/group__npf__eth__cond.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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
| #define | [NPF\_ETH\_VLAN\_TYPE\_MATCH](#ga2d67631c0fdd659a8e9db62c6f0a87bf)(\_name, \_type) |
|  | Statically define an "Ethernet VLAN header type match" packet filter condition. |
| #define | [NPF\_ETH\_VLAN\_TYPE\_UNMATCH](#ga49af5d0231e15932607da955ca7e4b34)(\_name, \_type) |
|  | Statically define an "Ethernet VLAN header type unmatch" packet filter condition. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [npf\_rule\_cb\_t](#ga7522a5a2188f7afbdc1a0528782ce0ef)) (struct [npf\_rule](structnpf__rule.md) \*rule, enum [npf\_rule\_type](#gaad4624a8e6c9491572e2a89739304530) type, void \*user\_data) |
|  | Callback used while iterating over network packet filter rules. |

| Enumerations | |
| --- | --- |
| enum | [npf\_rule\_type](#gaad4624a8e6c9491572e2a89739304530) {     [NPF\_RULE\_TYPE\_UNKNOWN](#ggaad4624a8e6c9491572e2a89739304530a0c66a2772501fbaf5e8521c19e1378ca) = 0 , [NPF\_RULE\_TYPE\_SEND](#ggaad4624a8e6c9491572e2a89739304530a2817a29d560b9ff6cfbc6bd69a99fd81) , [NPF\_RULE\_TYPE\_RECV](#ggaad4624a8e6c9491572e2a89739304530a0ecff39e652e912433e3dd36739eb41f) , [NPF\_RULE\_TYPE\_LOCAL\_IN\_RECV](#ggaad4624a8e6c9491572e2a89739304530a15eb4c6dbd1c855a24154243ca91b49b) ,     [NPF\_RULE\_TYPE\_IPV4\_RECV](#ggaad4624a8e6c9491572e2a89739304530a9ca4ae82040d060855db63ff193854fc) , [NPF\_RULE\_TYPE\_IPV6\_RECV](#ggaad4624a8e6c9491572e2a89739304530acb0785310ca00b7fc0030c5ee0115db2)   } |
|  | Type of the packet filter rule. [More...](#gaad4624a8e6c9491572e2a89739304530) |

| Functions | |
| --- | --- |
| void | [npf\_rules\_foreach](#ga188b9d73f47a77ce05d728250606e7ec) ([npf\_rule\_cb\_t](#ga7522a5a2188f7afbdc1a0528782ce0ef) cb, void \*user\_data) |
|  | Go through all the network packet filter rules and call callback for each of them. |

## Detailed Description

Since
:   3.0

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#ga7cf793af7b91eccc6e675ff19ed59a14)NPF\_ETH\_DST\_ADDR\_MASK\_MATCH

| #define NPF\_ETH\_DST\_ADDR\_MASK\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_addr\_array*, |
|  |  |  | ... ) |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_addr \_name = { \

.addresses = (\_addr\_array), \

.nb\_addresses = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_addr\_array), \

.mask.addr = { \_\_VA\_ARGS\_\_ }, \

.test.fn = npf\_eth\_dst\_addr\_match, \

IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

(.test.name = "eth dst mask", \

.test.type = NPF\_TEST\_TYPE\_ETH\_DST\_ADDR\_MASK\_MATCH,)) \

}

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:121

Statically define a "destination address match with mask" packet filter condition.

This tests if the packet destination address matches any of the Ethernet addresses contained in the provided set after applying specified mask.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_addr\_array | Array of struct [net\_eth\_addr](structnet__eth__addr.md "Ethernet address.") items to test against |
    | ... | up to 6 mask bytes |

## [◆ ](#ga3d22d687bcd56b7727c51c7bc7f36cac)NPF\_ETH\_DST\_ADDR\_MATCH

| #define NPF\_ETH\_DST\_ADDR\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_addr\_array* ) |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_addr \_name = { \

.addresses = (\_addr\_array), \

.nb\_addresses = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_addr\_array), \

.test.fn = npf\_eth\_dst\_addr\_match, \

.mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

(.test.name = "eth dst", \

.test.type = NPF\_TEST\_TYPE\_ETH\_DST\_ADDR\_MATCH,)) \

}

Statically define a "destination address match" packet filter condition.

This tests if the packet destination address matches any of the Ethernet addresses contained in the provided set.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_addr\_array | Array of struct [net\_eth\_addr](structnet__eth__addr.md "Ethernet address.") items to test against |

## [◆ ](#ga3b8a8a22eb992c0e02223f70723c3641)NPF\_ETH\_DST\_ADDR\_UNMATCH

| #define NPF\_ETH\_DST\_ADDR\_UNMATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_addr\_array* ) |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_addr \_name = { \

.addresses = (\_addr\_array), \

.nb\_addresses = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_addr\_array), \

.test.fn = npf\_eth\_dst\_addr\_unmatch, \

.mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

(.test.name = "!eth dst", \

.test.type = NPF\_TEST\_TYPE\_ETH\_DST\_ADDR\_UNMATCH,)) \

}

Statically define a "destination address unmatch" packet filter condition.

This tests if the packet destination address matches none of the Ethernet addresses contained in the provided set.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_addr\_array | Array of struct [net\_eth\_addr](structnet__eth__addr.md "Ethernet address.") items to test against |

## [◆ ](#ga0e06ebc4c9a1a960651be1ba89eeb2fd)NPF\_ETH\_SRC\_ADDR\_MASK\_MATCH

| #define NPF\_ETH\_SRC\_ADDR\_MASK\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_addr\_array*, |
|  |  |  | ... ) |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_addr \_name = { \

.addresses = (\_addr\_array), \

.nb\_addresses = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_addr\_array), \

.mask.addr = { \_\_VA\_ARGS\_\_ }, \

.test.fn = npf\_eth\_src\_addr\_match, \

IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

(.test.name = "eth src mask", \

.test.type = NPF\_TEST\_TYPE\_ETH\_SRC\_ADDR\_MASK\_MATCH,)) \

}

Statically define a "source address match with mask" packet filter condition.

This tests if the packet source address matches any of the Ethernet addresses contained in the provided set after applying specified mask.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_addr\_array | Array of struct [net\_eth\_addr](structnet__eth__addr.md "Ethernet address.") items to test against |
    | ... | up to 6 mask bytes |

## [◆ ](#gad2141ad8d6639c9b92569d55130ca1b1)NPF\_ETH\_SRC\_ADDR\_MATCH

| #define NPF\_ETH\_SRC\_ADDR\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_addr\_array* ) |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_addr \_name = { \

.addresses = (\_addr\_array), \

.nb\_addresses = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_addr\_array), \

.test.fn = npf\_eth\_src\_addr\_match, \

.mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

(.test.name = "eth src", \

.test.type = NPF\_TEST\_TYPE\_ETH\_SRC\_ADDR\_MATCH,)) \

}

Statically define a "source address match" packet filter condition.

This tests if the packet source address matches any of the Ethernet addresses contained in the provided set.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_addr\_array | Array of struct [net\_eth\_addr](structnet__eth__addr.md "Ethernet address.") items to test against |

## [◆ ](#ga228eaa3784f663d8f2e2711e26409043)NPF\_ETH\_SRC\_ADDR\_UNMATCH

| #define NPF\_ETH\_SRC\_ADDR\_UNMATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_addr\_array* ) |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_addr \_name = { \

.addresses = (\_addr\_array), \

.nb\_addresses = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_addr\_array), \

.test.fn = npf\_eth\_src\_addr\_unmatch, \

.mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

(.test.name = "!eth src", \

.test.type = NPF\_TEST\_TYPE\_ETH\_SRC\_ADDR\_UNMATCH,)) \

}

Statically define a "source address unmatch" packet filter condition.

This tests if the packet source address matches none of the Ethernet addresses contained in the provided set.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_addr\_array | Array of struct [net\_eth\_addr](structnet__eth__addr.md "Ethernet address.") items to test against |

## [◆ ](#gace7de72d4c64e128a825f28f94d8b1b2)NPF\_ETH\_TYPE\_MATCH

| #define NPF\_ETH\_TYPE\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_type* ) |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_type \_name = { \

.type = [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(\_type), \

.test.fn = npf\_eth\_type\_match, \

IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

(.test.name = "eth type", \

.test.type = NPF\_TEST\_TYPE\_ETH\_TYPE\_MATCH,)) \

}

[htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)

#define htons(x)

Convert 16-bit value from host to network byte order.

**Definition** net\_ip.h:124

Statically define an "Ethernet type match" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_type | Ethernet type to match |

## [◆ ](#gab9bf6d58433e273220c5fab76f608545)NPF\_ETH\_TYPE\_UNMATCH

| #define NPF\_ETH\_TYPE\_UNMATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_type* ) |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_type \_name = { \

.type = [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(\_type), \

.test.fn = npf\_eth\_type\_unmatch, \

IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

(.test.name = "!eth type", \

.test.type = NPF\_TEST\_TYPE\_ETH\_TYPE\_UNMATCH,)) \

}

Statically define an "Ethernet type unmatch" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_type | Ethernet type to exclude |

## [◆ ](#ga2d67631c0fdd659a8e9db62c6f0a87bf)NPF\_ETH\_VLAN\_TYPE\_MATCH

| #define NPF\_ETH\_VLAN\_TYPE\_MATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_type* ) |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_type \_name = { \

.type = [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(\_type), \

.test.fn = npf\_eth\_vlan\_type\_match, \

IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

(.test.name = "eth vlan type", \

.test.type = NPF\_TEST\_TYPE\_ETH\_VLAN\_TYPE\_MATCH,)) \

}

Statically define an "Ethernet VLAN header type match" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_type | Ethernet VLAN header type to match |

## [◆ ](#ga49af5d0231e15932607da955ca7e4b34)NPF\_ETH\_VLAN\_TYPE\_UNMATCH

| #define NPF\_ETH\_VLAN\_TYPE\_UNMATCH | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_type* ) |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct npf\_test\_eth\_type \_name = { \

.type = [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(\_type), \

.test.fn = npf\_eth\_vlan\_type\_unmatch, \

IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

(.test.name = "!eth vlan type", \

.test.type = NPF\_TEST\_TYPE\_ETH\_VLAN\_TYPE\_UNMATCH,)) \

}

Statically define an "Ethernet VLAN header type unmatch" packet filter condition.

Parameters
:   | \_name | Name of the condition |
    | --- | --- |
    | \_type | Ethernet VLAN header type to exclude |

## Typedef Documentation

## [◆ ](#ga7522a5a2188f7afbdc1a0528782ce0ef)npf\_rule\_cb\_t

| typedef void(\* npf\_rule\_cb\_t) (struct [npf\_rule](structnpf__rule.md) \*rule, enum [npf\_rule\_type](#gaad4624a8e6c9491572e2a89739304530) type, void \*user\_data) |
| --- |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

Callback used while iterating over network packet filter rules.

Parameters
:   | rule | Pointer to current network packet filter rule |
    | --- | --- |
    | type | Type of the rule (rx, tx, local\_in, IPv4 or IPv6) |
    | user\_data | A valid pointer to user data or NULL |

## Enumeration Type Documentation

## [◆ ](#gaad4624a8e6c9491572e2a89739304530)npf\_rule\_type

| enum [npf\_rule\_type](#gaad4624a8e6c9491572e2a89739304530) |
| --- |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

Type of the packet filter rule.

| Enumerator | |
| --- | --- |
| NPF\_RULE\_TYPE\_UNKNOWN | Unknown rule type. |
| NPF\_RULE\_TYPE\_SEND | Rule for outgoing packets. |
| NPF\_RULE\_TYPE\_RECV | Rule for incoming packets. |
| NPF\_RULE\_TYPE\_LOCAL\_IN\_RECV | Rule for local incoming packets. |
| NPF\_RULE\_TYPE\_IPV4\_RECV | Rule for IPv4 incoming packets. |
| NPF\_RULE\_TYPE\_IPV6\_RECV | Rule for IPv6 incoming packets. |

## Function Documentation

## [◆ ](#ga188b9d73f47a77ce05d728250606e7ec)npf\_rules\_foreach()

| void npf\_rules\_foreach | ( | [npf\_rule\_cb\_t](#ga7522a5a2188f7afbdc1a0528782ce0ef) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[zephyr/net/net_pkt_filter.h](net__pkt__filter_8h.md)>`

Go through all the network packet filter rules and call callback for each of them.

Parameters
:   | cb | User-supplied callback function to call |
    | --- | --- |
    | user\_data | User specified data |

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
