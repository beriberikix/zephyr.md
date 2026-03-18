---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/net_pkt_filter.html
original_path: connectivity/networking/api/net_pkt_filter.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Network Packet Filtering

## [Overview](#id1)

The Network Packet Filtering facility provides the infrastructure to
construct custom rules for accepting and/or denying packet transmission
and reception. This can be used to create a basic firewall, control
network traffic, etc.

The [`CONFIG_NET_PKT_FILTER`](../../../kconfig.md#CONFIG_NET_PKT_FILTER "CONFIG_NET_PKT_FILTER") must be set in order to enable the
relevant APIs.

Both the transmission and reception paths may have a list of filter rules.
Each rule is made of a set of conditions and a packet outcome. Every packet
is subjected to the conditions attached to a rule. When all the conditions
for a given rule are true then the packet outcome is immediately determined
as specified by the current rule and no more rules are considered. If one
condition is false then the next rule in the list is considered.

Packet outcome is either `NET_OK` to accept the packet or `NET_DROP` to
drop it.

A rule is represented by a [`npf_rule`](#c.npf_rule) object. It can be inserted to,
appended to or removed from a rule list contained in a
[`npf_rule_list`](#c.npf_rule_list) object using [`npf_insert_rule()`](#c.npf_insert_rule),
[`npf_append_rule()`](#c.npf_append_rule), and [`npf_remove_rule()`](#c.npf_remove_rule).
Currently, two such rule lists exist: `npf_send_rules` for outgoing packets,
and `npf_recv_rules` for incoming packets.

If a filter rule list is empty then `NET_OK` is assumed. If a non-empty
rule list runs to the end then `NET_DROP` is assumed. However it is
recommended to always terminate a non-empty rule list with an explicit
default termination rule, either `npf_default_ok` or `npf_default_drop`.

Rule conditions are represented by a [`npf_test`](#c.npf_test). This structure
can be embedded into a larger structure when a specific condition requires
extra test data. It is up to the test function for such conditions to
retrieve the outer structure from the provided `npf_test` structure pointer.

Convenience macros are provided in [include/zephyr/net/net\_pkt\_filter.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/net_pkt_filter.h)
to statically define condition instances for various conditions, and
[`NPF_RULE()`](#c.NPF_RULE) to create a rule instance to tie them.

## [Examples](#id2)

Here’s an example usage:

```c
static NPF_SIZE_MAX(maxsize_200, 200);
static NPF_ETH_TYPE_MATCH(ip_packet, NET_ETH_PTYPE_IP);

static NPF_RULE(small_ip_pkt, NET_OK, ip_packet, maxsize_200);

void install_my_filter(void)
{
    npf_insert_recv_rule(&npf_default_drop);
    npf_insert_recv_rule(&small_ip_pkt);
}
```

The above would accept IP packets that are 200 bytes or smaller, and drop
all other packets.

Another (less efficient) way to achieve the same result could be:

```c
static NPF_SIZE_MIN(minsize_201, 201);
static NPF_ETH_TYPE_UNMATCH(not_ip_packet, NET_ETH_PTYPE_IP);

static NPF_RULE(reject_big_pkts, NET_DROP, minsize_201);
static NPF_RULE(reject_non_ip, NET_DROP, not_ip_packet);

void install_my_filter(void) {
    npf_append_recv_rule(&reject_big_pkts);
    npf_append_recv_rule(&reject_non_ip);
    npf_append_recv_rule(&npf_default_ok);
}
```

## [API Reference](#id3)

*group* Network Packet Filter API
:   Network Packet Filter API.

    Defines

    NPF\_RULE(\_name, \_result, ...)
    :   Statically define one packet filter rule.

        This creates a rule from a variable amount of filter conditions. This rule can then be inserted or appended to the rule list for a given network packet path.

        Example:

        ```c
        static NPF_SIZE_MAX(maxsize_200, 200);
        static NPF_ETH_TYPE_MATCH(ip_packet, NET_ETH_PTYPE_IP);

        static NPF_RULE(small_ip_pkt, NET_OK, ip_packet, maxsize_200);

        void install_my_filter(void)
        {
            npf_insert_recv_rule(&npf_default_drop);
            npf_insert_recv_rule(&small_ip_pkt);
        }
        ```

        The above would accept IP packets that are 200 bytes or smaller, and drop all other packets.

        Another (less efficient) way to create the same result could be:

        ```c
        static NPF_SIZE_MIN(minsize_201, 201);
        static NPF_ETH_TYPE_UNMATCH(not_ip_packet, NET_ETH_PTYPE_IP);

        static NPF_RULE(reject_big_pkts, NET_DROP, minsize_201);
        static NPF_RULE(reject_non_ip, NET_DROP, not_ip_packet);

        void install_my_filter(void) {
            npf_append_recv_rule(&reject_big_pkts);
            npf_append_recv_rule(&reject_non_ip);
            npf_append_recv_rule(&npf_default_ok);
        }
        ```

        The first rule in the list for which all conditions are true determines the fate of the packet. If one condition is false then the next rule in the list is evaluated.

        Parameters:
        :   - **\_name** – Name for this rule.
            - **\_result** – Fate of the packet if all conditions are true, either `[NET_OK](net_core.md#group__net__core_1gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047)` or `[NET_DROP](net_core.md#group__net__core_1gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3)`.
            - **...** – List of conditions for this rule.

    Functions

    void npf\_insert\_rule(struct [npf\_rule\_list](#c.npf_rule_list) \*rules, struct [npf\_rule](#c.npf_rule) \*rule)
    :   Insert a rule at the front of given rule list.

        Parameters:
        :   - **rules** – the affected rule list
            - **rule** – the rule to be inserted

    void npf\_append\_rule(struct [npf\_rule\_list](#c.npf_rule_list) \*rules, struct [npf\_rule](#c.npf_rule) \*rule)
    :   Append a rule at the end of given rule list.

        Parameters:
        :   - **rules** – the affected rule list
            - **rule** – the rule to be appended

    bool npf\_remove\_rule(struct [npf\_rule\_list](#c.npf_rule_list) \*rules, struct [npf\_rule](#c.npf_rule) \*rule)
    :   Remove a rule from the given rule list.

        Parameters:
        :   - **rules** – the affected rule list
            - **rule** – the rule to be removed

        Return values:
        :   **true** – if given rule was found in the rule list and removed

    bool npf\_remove\_all\_rules(struct [npf\_rule\_list](#c.npf_rule_list) \*rules)
    :   Remove all rules from the given rule list.

        Parameters:
        :   - **rules** – the affected rule list

        Return values:
        :   **true** – if at least one rule was removed from the rule list

    Variables

    struct [npf\_rule](#c.npf_rule) npf\_default\_ok
    :   Default rule list termination for accepting a packet.

    struct [npf\_rule](#c.npf_rule) npf\_default\_drop
    :   Default rule list termination for rejecting a packet.

    struct [npf\_rule\_list](#c.npf_rule_list) npf\_send\_rules
    :   rule list applied to outgoing packets

    struct [npf\_rule\_list](#c.npf_rule_list) npf\_recv\_rules
    :   rule list applied to incoming packets

    struct [npf\_rule\_list](#c.npf_rule_list) npf\_local\_in\_recv\_rules
    :   rule list applied for local incoming packets

    struct [npf\_rule\_list](#c.npf_rule_list) npf\_ipv4\_recv\_rules
    :   rule list applied for IPv4 incoming packets

    struct [npf\_rule\_list](#c.npf_rule_list) npf\_ipv6\_recv\_rules
    :   rule list applied for IPv6 incoming packets

    struct npf\_test
    :   *#include <net\_pkt\_filter.h>*

        common filter test structure to be embedded into larger structures

        Public Members

        npf\_test\_fn\_t \*fn
        :   packet condition test function

    struct npf\_rule
    :   *#include <net\_pkt\_filter.h>*

        filter rule structure

        Public Members

        [sys\_snode\_t](../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Slist rule list node.

        enum [net\_verdict](net_core.md#c.net_verdict "net_verdict") result
        :   result if all tests pass

        uint32\_t nb\_tests
        :   number of tests for this rule

        struct [npf\_test](#c.npf_test) \*tests[]
        :   pointers to [npf\_test](#structnpf__test) instances

    struct npf\_rule\_list
    :   *#include <net\_pkt\_filter.h>*

        rule set for a given test location

        Public Members

        [sys\_slist\_t](../../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") rule\_head
        :   List head.

        struct [k\_spinlock](../../../kernel/services/smp/smp.md#c.k_spinlock "k_spinlock") lock
        :   Lock protecting the list access.

*group* Basic Filter Conditions
:   Defines

    NPF\_IFACE\_MATCH(\_name, \_iface)
    :   Statically define an “interface match” packet filter condition.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_iface** – Interface to match

    NPF\_IFACE\_UNMATCH(\_name, \_iface)
    :   Statically define an “interface unmatch” packet filter condition.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_iface** – Interface to exclude

    NPF\_ORIG\_IFACE\_MATCH(\_name, \_iface)
    :   Statically define an “orig interface match” packet filter condition.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_iface** – Interface to match

    NPF\_ORIG\_IFACE\_UNMATCH(\_name, \_iface)
    :   Statically define an “orig interface unmatch” packet filter condition.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_iface** – Interface to exclude

    NPF\_SIZE\_MIN(\_name, \_size)
    :   Statically define a “data minimum size” packet filter condition.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_size** – Lower bound of the packet’s data size

    NPF\_SIZE\_MAX(\_name, \_size)
    :   Statically define a “data maximum size” packet filter condition.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_size** – Higher bound of the packet’s data size

    NPF\_SIZE\_BOUNDS(\_name, \_min\_size, \_max\_size)
    :   Statically define a “data bounded size” packet filter condition.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_min\_size** – Lower bound of the packet’s data size
            - **\_max\_size** – Higher bound of the packet’s data size

    NPF\_IP\_SRC\_ADDR\_ALLOWLIST(\_name, \_ip\_addr\_array, \_ip\_addr\_num, \_af)
    :   Statically define a “ip address allowlist” packet filter condition.

        This tests if the packet source ip address matches any of the ip addresses contained in the provided set.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_ip\_addr\_array** – Array of `struct [in_addr](ip_4_6.md#structin__addr)` or `struct [in6_addr](ip_4_6.md#structin6__addr)` items to test against
            - **\_ip\_addr\_num** – number of IP addresses in the array
            - **\_af** – Addresses family type (AF\_INET / AF\_INET6) in the array

    NPF\_IP\_SRC\_ADDR\_BLOCKLIST(\_name, \_ip\_addr\_array, \_ip\_addr\_num, \_af)
    :   Statically define a “ip address blocklist” packet filter condition.

        This tests if the packet source ip address matches any of the ip addresses contained in the provided set.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_ip\_addr\_array** – Array of `struct [in_addr](ip_4_6.md#structin__addr)` or `struct [in6_addr](ip_4_6.md#structin6__addr)` items to test against
            - **\_ip\_addr\_num** – number of IP addresses in the array
            - **\_af** – Addresses family type (AF\_INET / AF\_INET6) in the array

*group* Ethernet Filter Conditions
:   Defines

    NPF\_ETH\_SRC\_ADDR\_MATCH(\_name, \_addr\_array)
    :   Statically define a “source address match” packet filter condition.

        This tests if the packet source address matches any of the Ethernet addresses contained in the provided set.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_addr\_array** – Array of `struct [net_eth_addr](ethernet.md#structnet__eth__addr)` items to test against

    NPF\_ETH\_SRC\_ADDR\_UNMATCH(\_name, \_addr\_array)
    :   Statically define a “source address unmatch” packet filter condition.

        This tests if the packet source address matches none of the Ethernet addresses contained in the provided set.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_addr\_array** – Array of `struct [net_eth_addr](ethernet.md#structnet__eth__addr)` items to test against

    NPF\_ETH\_DST\_ADDR\_MATCH(\_name, \_addr\_array)
    :   Statically define a “destination address match” packet filter condition.

        This tests if the packet destination address matches any of the Ethernet addresses contained in the provided set.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_addr\_array** – Array of `struct [net_eth_addr](ethernet.md#structnet__eth__addr)` items to test against

    NPF\_ETH\_DST\_ADDR\_UNMATCH(\_name, \_addr\_array)
    :   Statically define a “destination address unmatch” packet filter condition.

        This tests if the packet destination address matches none of the Ethernet addresses contained in the provided set.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_addr\_array** – Array of `struct [net_eth_addr](ethernet.md#structnet__eth__addr)` items to test against

    NPF\_ETH\_SRC\_ADDR\_MASK\_MATCH(\_name, \_addr\_array, ...)
    :   Statically define a “source address match with mask” packet filter condition.

        This tests if the packet source address matches any of the Ethernet addresses contained in the provided set after applying specified mask.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_addr\_array** – Array of `struct [net_eth_addr](ethernet.md#structnet__eth__addr)` items to test against
            - **...** – up to 6 mask bytes

    NPF\_ETH\_DST\_ADDR\_MASK\_MATCH(\_name, \_addr\_array, ...)
    :   Statically define a “destination address match with mask” packet filter condition.

        This tests if the packet destination address matches any of the Ethernet addresses contained in the provided set after applying specified mask.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_addr\_array** – Array of `struct [net_eth_addr](ethernet.md#structnet__eth__addr)` items to test against
            - **...** – up to 6 mask bytes

    NPF\_ETH\_TYPE\_MATCH(\_name, \_type)
    :   Statically define an “Ethernet type match” packet filter condition.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_type** – Ethernet type to match

    NPF\_ETH\_TYPE\_UNMATCH(\_name, \_type)
    :   Statically define an “Ethernet type unmatch” packet filter condition.

        Parameters:
        :   - **\_name** – Name of the condition
            - **\_type** – Ethernet type to exclude
