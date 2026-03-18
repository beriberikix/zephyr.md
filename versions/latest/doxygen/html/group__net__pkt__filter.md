---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__net__pkt__filter.html
original_path: doxygen/html/group__net__pkt__filter.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Packet Filter API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network Packet Filter API.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Basic Filter Conditions](group__npf__basic__cond.md) |
|  | [Ethernet Filter Conditions](group__npf__eth__cond.md) |

| Data Structures | |
| --- | --- |
| struct | [npf\_test](structnpf__test.md) |
|  | common filter test structure to be embedded into larger structures [More...](structnpf__test.md#details) |
| struct | [npf\_rule](structnpf__rule.md) |
|  | filter rule structure [More...](structnpf__rule.md#details) |
| struct | [npf\_rule\_list](structnpf__rule__list.md) |
|  | rule set for a given test location [More...](structnpf__rule__list.md#details) |

| Macros | |
| --- | --- |
| #define | [npf\_insert\_send\_rule](#ga4d3592647f81cd44a84ded4fff8edcf5)(rule) |
| #define | [npf\_insert\_recv\_rule](#ga3f6ecadc4842b61731984968ab4c6b89)(rule) |
| #define | [npf\_append\_send\_rule](#ga8cd06cba4360c1b56709e59ff06dbeb3)(rule) |
| #define | [npf\_append\_recv\_rule](#ga263c7ee6e3c860353b5720c613690b0a)(rule) |
| #define | [npf\_remove\_send\_rule](#ga43f03a0ce73d6dee52f43fd3577aa240)(rule) |
| #define | [npf\_remove\_recv\_rule](#gae78cb092522564303a665d1a5d3596b9)(rule) |
| #define | [npf\_remove\_all\_send\_rules](#gaea48284508ee244bce6d78b29bc2f471)() |
| #define | [npf\_remove\_all\_recv\_rules](#gac08801a6e8bd14bfd6eeaf2f28a1ed1a)() |
| #define | [NPF\_RULE](#ga2f45093d5ad164d5c51a8996f7f04d32)(\_name, \_result, ...) |
|  | Statically define one packet filter rule. |

| Functions | |
| --- | --- |
| void | [npf\_insert\_rule](#ga3b2a85558b6756e76760d9a40c780e28) (struct [npf\_rule\_list](structnpf__rule__list.md) \*rules, struct [npf\_rule](structnpf__rule.md) \*rule) |
|  | Insert a rule at the front of given rule list. |
| void | [npf\_append\_rule](#gadfa956e4af3c45460846fc22f863e697) (struct [npf\_rule\_list](structnpf__rule__list.md) \*rules, struct [npf\_rule](structnpf__rule.md) \*rule) |
|  | Append a rule at the end of given rule list. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [npf\_remove\_rule](#ga4d7426db901debff35e1de5805e06c71) (struct [npf\_rule\_list](structnpf__rule__list.md) \*rules, struct [npf\_rule](structnpf__rule.md) \*rule) |
|  | Remove a rule from the given rule list. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [npf\_remove\_all\_rules](#ga54916eb4943e4b47cd31eb23827d0dd5) (struct [npf\_rule\_list](structnpf__rule__list.md) \*rules) |
|  | Remove all rules from the given rule list. |

| Variables | |
| --- | --- |
| struct [npf\_rule](structnpf__rule.md) | [npf\_default\_ok](#gaac489d75c023952243589cba7ff7367a) |
|  | Default rule list termination for accepting a packet. |
| struct [npf\_rule](structnpf__rule.md) | [npf\_default\_drop](#ga8fc592feedeceb5172f8747a29697dd7) |
|  | Default rule list termination for rejecting a packet. |
| struct [npf\_rule\_list](structnpf__rule__list.md) | [npf\_send\_rules](#ga8017a041d3168c76e39bdfac011b9315) |
|  | rule list applied to outgoing packets |
| struct [npf\_rule\_list](structnpf__rule__list.md) | [npf\_recv\_rules](#ga9714529658625e906264a46ad1a9be6f) |
|  | rule list applied to incoming packets |
| struct [npf\_rule\_list](structnpf__rule__list.md) | [npf\_local\_in\_recv\_rules](#ga571e9fb34eb4e3cbf38f885b5e786021) |
|  | rule list applied for local incoming packets |
| struct [npf\_rule\_list](structnpf__rule__list.md) | [npf\_ipv4\_recv\_rules](#gad521d7ac3270970833aec48d8a517d85) |
|  | rule list applied for IPv4 incoming packets |
| struct [npf\_rule\_list](structnpf__rule__list.md) | [npf\_ipv6\_recv\_rules](#gab91ca81aab2da48066538d72caf0c8ae) |
|  | rule list applied for IPv6 incoming packets |

## Detailed Description

Network Packet Filter API.

## Macro Definition Documentation

## [◆ ](#ga263c7ee6e3c860353b5720c613690b0a)npf\_append\_recv\_rule

| #define npf\_append\_recv\_rule | ( |  | *rule* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

[npf\_append\_rule](#gadfa956e4af3c45460846fc22f863e697)(&[npf\_recv\_rules](#ga9714529658625e906264a46ad1a9be6f), rule)

[npf\_recv\_rules](#ga9714529658625e906264a46ad1a9be6f)

struct npf\_rule\_list npf\_recv\_rules

rule list applied to incoming packets

[npf\_append\_rule](#gadfa956e4af3c45460846fc22f863e697)

void npf\_append\_rule(struct npf\_rule\_list \*rules, struct npf\_rule \*rule)

Append a rule at the end of given rule list.

## [◆ ](#ga8cd06cba4360c1b56709e59ff06dbeb3)npf\_append\_send\_rule

| #define npf\_append\_send\_rule | ( |  | *rule* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

[npf\_append\_rule](#gadfa956e4af3c45460846fc22f863e697)(&[npf\_send\_rules](#ga8017a041d3168c76e39bdfac011b9315), rule)

[npf\_send\_rules](#ga8017a041d3168c76e39bdfac011b9315)

struct npf\_rule\_list npf\_send\_rules

rule list applied to outgoing packets

## [◆ ](#ga3f6ecadc4842b61731984968ab4c6b89)npf\_insert\_recv\_rule

| #define npf\_insert\_recv\_rule | ( |  | *rule* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

[npf\_insert\_rule](#ga3b2a85558b6756e76760d9a40c780e28)(&[npf\_recv\_rules](#ga9714529658625e906264a46ad1a9be6f), rule)

[npf\_insert\_rule](#ga3b2a85558b6756e76760d9a40c780e28)

void npf\_insert\_rule(struct npf\_rule\_list \*rules, struct npf\_rule \*rule)

Insert a rule at the front of given rule list.

## [◆ ](#ga4d3592647f81cd44a84ded4fff8edcf5)npf\_insert\_send\_rule

| #define npf\_insert\_send\_rule | ( |  | *rule* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

[npf\_insert\_rule](#ga3b2a85558b6756e76760d9a40c780e28)(&[npf\_send\_rules](#ga8017a041d3168c76e39bdfac011b9315), rule)

## [◆ ](#gac08801a6e8bd14bfd6eeaf2f28a1ed1a)npf\_remove\_all\_recv\_rules

| #define npf\_remove\_all\_recv\_rules | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

[npf\_remove\_all\_rules](#ga54916eb4943e4b47cd31eb23827d0dd5)(&[npf\_recv\_rules](#ga9714529658625e906264a46ad1a9be6f))

[npf\_remove\_all\_rules](#ga54916eb4943e4b47cd31eb23827d0dd5)

bool npf\_remove\_all\_rules(struct npf\_rule\_list \*rules)

Remove all rules from the given rule list.

## [◆ ](#gaea48284508ee244bce6d78b29bc2f471)npf\_remove\_all\_send\_rules

| #define npf\_remove\_all\_send\_rules | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

[npf\_remove\_all\_rules](#ga54916eb4943e4b47cd31eb23827d0dd5)(&[npf\_send\_rules](#ga8017a041d3168c76e39bdfac011b9315))

## [◆ ](#gae78cb092522564303a665d1a5d3596b9)npf\_remove\_recv\_rule

| #define npf\_remove\_recv\_rule | ( |  | *rule* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

[npf\_remove\_rule](#ga4d7426db901debff35e1de5805e06c71)(&[npf\_recv\_rules](#ga9714529658625e906264a46ad1a9be6f), rule)

[npf\_remove\_rule](#ga4d7426db901debff35e1de5805e06c71)

bool npf\_remove\_rule(struct npf\_rule\_list \*rules, struct npf\_rule \*rule)

Remove a rule from the given rule list.

## [◆ ](#ga43f03a0ce73d6dee52f43fd3577aa240)npf\_remove\_send\_rule

| #define npf\_remove\_send\_rule | ( |  | *rule* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

[npf\_remove\_rule](#ga4d7426db901debff35e1de5805e06c71)(&[npf\_send\_rules](#ga8017a041d3168c76e39bdfac011b9315), rule)

## [◆ ](#ga2f45093d5ad164d5c51a8996f7f04d32)NPF\_RULE

| #define NPF\_RULE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_result*, |
|  |  |  | ... ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

**Value:**

struct [npf\_rule](structnpf__rule.md) \_name = { \

.result = (\_result), \

.nb\_tests = [NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)(\_\_VA\_ARGS\_\_) + 1, \

.tests = { [FOR\_EACH](group__sys-util.md#ga278c8b7cbbea2f585e371d3568f3cb12)(Z\_NPF\_TEST\_ADDR, (,), \_\_VA\_ARGS\_\_) }, \

}

[FOR\_EACH](group__sys-util.md#ga278c8b7cbbea2f585e371d3568f3cb12)

#define FOR\_EACH(F, sep,...)

Call a macro F on each provided argument with a given separator between each call.

**Definition** util\_macro.h:465

[NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)

#define NUM\_VA\_ARGS\_LESS\_1(...)

Number of arguments in the variable arguments list minus one.

**Definition** util\_macro.h:629

[npf\_rule](structnpf__rule.md)

filter rule structure

**Definition** net\_pkt\_filter.h:48

Statically define one packet filter rule.

This creates a rule from a variable amount of filter conditions. This rule can then be inserted or appended to the rule list for a given network packet path.

Example:

static [NPF\_SIZE\_MAX](group__npf__basic__cond.md#gacd56b9bcf2b2ba4759402650a9bff67a)(maxsize\_200, 200);

static [NPF\_ETH\_TYPE\_MATCH](group__npf__eth__cond.md#gace7de72d4c64e128a825f28f94d8b1b2)(ip\_packet, NET\_ETH\_PTYPE\_IP);

static [NPF\_RULE](#ga2f45093d5ad164d5c51a8996f7f04d32)(small\_ip\_pkt, [NET\_OK](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047), ip\_packet, maxsize\_200);

void install\_my\_filter(void)

{

[npf\_insert\_recv\_rule](#ga3f6ecadc4842b61731984968ab4c6b89)(&[npf\_default\_drop](#ga8fc592feedeceb5172f8747a29697dd7));

[npf\_insert\_recv\_rule](#ga3f6ecadc4842b61731984968ab4c6b89)(&small\_ip\_pkt);

}

[NET\_OK](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047)

@ NET\_OK

Packet has been taken care of.

**Definition** net\_core.h:100

[NPF\_RULE](#ga2f45093d5ad164d5c51a8996f7f04d32)

#define NPF\_RULE(\_name, \_result,...)

Statically define one packet filter rule.

**Definition** net\_pkt\_filter.h:195

[npf\_insert\_recv\_rule](#ga3f6ecadc4842b61731984968ab4c6b89)

#define npf\_insert\_recv\_rule(rule)

**Definition** net\_pkt\_filter.h:112

[npf\_default\_drop](#ga8fc592feedeceb5172f8747a29697dd7)

struct npf\_rule npf\_default\_drop

Default rule list termination for rejecting a packet.

[NPF\_SIZE\_MAX](group__npf__basic__cond.md#gacd56b9bcf2b2ba4759402650a9bff67a)

#define NPF\_SIZE\_MAX(\_name, \_size)

Statically define a "data maximum size" packet filter condition.

**Definition** net\_pkt\_filter.h:305

[NPF\_ETH\_TYPE\_MATCH](group__npf__eth__cond.md#gace7de72d4c64e128a825f28f94d8b1b2)

#define NPF\_ETH\_TYPE\_MATCH(\_name, \_type)

Statically define an "Ethernet type match" packet filter condition.

**Definition** net\_pkt\_filter.h:526

The above would accept IP packets that are 200 bytes or smaller, and drop all other packets.

Another (less efficient) way to create the same result could be:

static [NPF\_SIZE\_MIN](group__npf__basic__cond.md#gaf142455f9bea3dea8faa0a913072b63e)(minsize\_201, 201);

static [NPF\_ETH\_TYPE\_UNMATCH](group__npf__eth__cond.md#gab9bf6d58433e273220c5fab76f608545)(not\_ip\_packet, NET\_ETH\_PTYPE\_IP);

static [NPF\_RULE](#ga2f45093d5ad164d5c51a8996f7f04d32)(reject\_big\_pkts, [NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3), minsize\_201);

static [NPF\_RULE](#ga2f45093d5ad164d5c51a8996f7f04d32)(reject\_non\_ip, [NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3), not\_ip\_packet);

void install\_my\_filter(void) {

[npf\_append\_recv\_rule](#ga263c7ee6e3c860353b5720c613690b0a)(&reject\_big\_pkts);

[npf\_append\_recv\_rule](#ga263c7ee6e3c860353b5720c613690b0a)(&reject\_non\_ip);

[npf\_append\_recv\_rule](#ga263c7ee6e3c860353b5720c613690b0a)(&[npf\_default\_ok](#gaac489d75c023952243589cba7ff7367a));

}

[NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3)

@ NET\_DROP

Packet must be dropped.

**Definition** net\_core.h:106

[npf\_append\_recv\_rule](#ga263c7ee6e3c860353b5720c613690b0a)

#define npf\_append\_recv\_rule(rule)

**Definition** net\_pkt\_filter.h:114

[npf\_default\_ok](#gaac489d75c023952243589cba7ff7367a)

struct npf\_rule npf\_default\_ok

Default rule list termination for accepting a packet.

[NPF\_SIZE\_MIN](group__npf__basic__cond.md#gaf142455f9bea3dea8faa0a913072b63e)

#define NPF\_SIZE\_MIN(\_name, \_size)

Statically define a "data minimum size" packet filter condition.

**Definition** net\_pkt\_filter.h:292

[NPF\_ETH\_TYPE\_UNMATCH](group__npf__eth__cond.md#gab9bf6d58433e273220c5fab76f608545)

#define NPF\_ETH\_TYPE\_UNMATCH(\_name, \_type)

Statically define an "Ethernet type unmatch" packet filter condition.

**Definition** net\_pkt\_filter.h:538

The first rule in the list for which all conditions are true determines the fate of the packet. If one condition is false then the next rule in the list is evaluated.

Parameters
:   | \_name | Name for this rule. |
    | --- | --- |
    | \_result | Fate of the packet if all conditions are true, either [NET\_OK](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047 "Packet has been taken care of.") or [NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3 "Packet must be dropped."). |
    | ... | List of conditions for this rule. |

## Function Documentation

## [◆ ](#gadfa956e4af3c45460846fc22f863e697)npf\_append\_rule()

| void npf\_append\_rule | ( | struct [npf\_rule\_list](structnpf__rule__list.md) \* | *rules*, |
| --- | --- | --- | --- |
|  |  | struct [npf\_rule](structnpf__rule.md) \* | *rule* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

Append a rule at the end of given rule list.

Parameters
:   | rules | the affected rule list |
    | --- | --- |
    | rule | the rule to be appended |

## [◆ ](#ga3b2a85558b6756e76760d9a40c780e28)npf\_insert\_rule()

| void npf\_insert\_rule | ( | struct [npf\_rule\_list](structnpf__rule__list.md) \* | *rules*, |
| --- | --- | --- | --- |
|  |  | struct [npf\_rule](structnpf__rule.md) \* | *rule* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

Insert a rule at the front of given rule list.

Parameters
:   | rules | the affected rule list |
    | --- | --- |
    | rule | the rule to be inserted |

## [◆ ](#ga54916eb4943e4b47cd31eb23827d0dd5)npf\_remove\_all\_rules()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) npf\_remove\_all\_rules | ( | struct [npf\_rule\_list](structnpf__rule__list.md) \* | *rules* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

Remove all rules from the given rule list.

Parameters
:   | rules | the affected rule list |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if at least one rule was removed from the rule list |
    | --- | --- |

## [◆ ](#ga4d7426db901debff35e1de5805e06c71)npf\_remove\_rule()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) npf\_remove\_rule | ( | struct [npf\_rule\_list](structnpf__rule__list.md) \* | *rules*, |
| --- | --- | --- | --- |
|  |  | struct [npf\_rule](structnpf__rule.md) \* | *rule* ) |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

Remove a rule from the given rule list.

Parameters
:   | rules | the affected rule list |
    | --- | --- |
    | rule | the rule to be removed |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if given rule was found in the rule list and removed |
    | --- | --- |

## Variable Documentation

## [◆ ](#ga8fc592feedeceb5172f8747a29697dd7)npf\_default\_drop

| | struct [npf\_rule](structnpf__rule.md) npf\_default\_drop | | --- | | extern |
| --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

Default rule list termination for rejecting a packet.

## [◆ ](#gaac489d75c023952243589cba7ff7367a)npf\_default\_ok

| | struct [npf\_rule](structnpf__rule.md) npf\_default\_ok | | --- | | extern |
| --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

Default rule list termination for accepting a packet.

## [◆ ](#gad521d7ac3270970833aec48d8a517d85)npf\_ipv4\_recv\_rules

| | struct [npf\_rule\_list](structnpf__rule__list.md) npf\_ipv4\_recv\_rules | | --- | | extern |
| --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

rule list applied for IPv4 incoming packets

## [◆ ](#gab91ca81aab2da48066538d72caf0c8ae)npf\_ipv6\_recv\_rules

| | struct [npf\_rule\_list](structnpf__rule__list.md) npf\_ipv6\_recv\_rules | | --- | | extern |
| --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

rule list applied for IPv6 incoming packets

## [◆ ](#ga571e9fb34eb4e3cbf38f885b5e786021)npf\_local\_in\_recv\_rules

| | struct [npf\_rule\_list](structnpf__rule__list.md) npf\_local\_in\_recv\_rules | | --- | | extern |
| --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

rule list applied for local incoming packets

## [◆ ](#ga9714529658625e906264a46ad1a9be6f)npf\_recv\_rules

| | struct [npf\_rule\_list](structnpf__rule__list.md) npf\_recv\_rules | | --- | | extern |
| --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

rule list applied to incoming packets

## [◆ ](#ga8017a041d3168c76e39bdfac011b9315)npf\_send\_rules

| | struct [npf\_rule\_list](structnpf__rule__list.md) npf\_send\_rules | | --- | | extern |
| --- | --- | --- |

`#include <[net_pkt_filter.h](net__pkt__filter_8h.md)>`

rule list applied to outgoing packets

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
