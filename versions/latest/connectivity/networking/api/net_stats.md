---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/net_stats.html
original_path: connectivity/networking/api/net_stats.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Network Statistics

## [Overview](#id1)

Network statistics are collected if [`CONFIG_NET_STATISTICS`](../../../kconfig.md#CONFIG_NET_STATISTICS "CONFIG_NET_STATISTICS") is set.
Individual component statistics for IPv4 or IPv6 can be turned off
if those statistics are not needed. See various options in
[subsys/net/ip/Kconfig.stats](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats) file for details.

By default, the system collects network statistics per network interface. This
can be controlled by [`CONFIG_NET_STATISTICS_PER_INTERFACE`](../../../kconfig.md#CONFIG_NET_STATISTICS_PER_INTERFACE "CONFIG_NET_STATISTICS_PER_INTERFACE") option.

The [`CONFIG_NET_STATISTICS_USER_API`](../../../kconfig.md#CONFIG_NET_STATISTICS_USER_API "CONFIG_NET_STATISTICS_USER_API") option can be set if the
application wants to collect statistics for further processing. The network
management interface API is used for that. See [Network Management](net_mgmt.md#net-mgmt-interface) for
details.

The [`CONFIG_NET_STATISTICS_ETHERNET`](../../../kconfig.md#CONFIG_NET_STATISTICS_ETHERNET "CONFIG_NET_STATISTICS_ETHERNET") option can be set to collect
generic Ethernet statistics. If the
[`CONFIG_NET_STATISTICS_ETHERNET_VENDOR`](../../../kconfig.md#CONFIG_NET_STATISTICS_ETHERNET_VENDOR "CONFIG_NET_STATISTICS_ETHERNET_VENDOR") option is set, then
Ethernet device driver can collect Ethernet device specific statistics.
These statistics can then be transferred to application for processing.

If the [`CONFIG_NET_SHELL`](../../../kconfig.md#CONFIG_NET_SHELL "CONFIG_NET_SHELL") option is set, then network shell can
show statistics information with `net stats` command.

## [API Reference](#id2)

Related code samples

[Network statistics](../../../samples/net/stats/README.md#net-stats "Query and display network statistics from a user application.")
:   Query and display network statistics from a user application.

[Wi-Fi shell](../../../samples/net/wifi/README.md#wifi-shell "Test Wi-Fi functionality using the Wi-Fi shell module.")
:   Test Wi-Fi functionality using the Wi-Fi shell module.

*group* net\_stats
:   Network statistics library.

    Defines

    NET\_TC\_TX\_STATS\_COUNT

    NET\_TC\_RX\_STATS\_COUNT

    Typedefs

    typedef uint32\_t net\_stats\_t
    :   Network statistics counter.

    struct net\_stats\_bytes
    :   *#include <net\_stats.h>*

        Number of bytes sent and received.

        Public Members

        [net\_stats\_t](#c.net_stats_t) sent
        :   Number of bytes sent.

        [net\_stats\_t](#c.net_stats_t) received
        :   Number of bytes received.

    struct net\_stats\_pkts
    :   *#include <net\_stats.h>*

        Number of network packets sent and received.

        Public Members

        [net\_stats\_t](#c.net_stats_t) tx
        :   Number of packets sent.

        [net\_stats\_t](#c.net_stats_t) rx
        :   Number of packets received.

    struct net\_stats\_ip
    :   *#include <net\_stats.h>*

        IP layer statistics.

        Public Members

        [net\_stats\_t](#c.net_stats_t) recv
        :   Number of received packets at the IP layer.

        [net\_stats\_t](#c.net_stats_t) sent
        :   Number of sent packets at the IP layer.

        [net\_stats\_t](#c.net_stats_t) forwarded
        :   Number of forwarded packets at the IP layer.

        [net\_stats\_t](#c.net_stats_t) drop
        :   Number of dropped packets at the IP layer.

    struct net\_stats\_ip\_errors
    :   *#include <net\_stats.h>*

        IP layer error statistics.

        Public Members

        [net\_stats\_t](#c.net_stats_t) vhlerr
        :   Number of packets dropped due to wrong IP version or header length.

        [net\_stats\_t](#c.net_stats_t) hblenerr
        :   Number of packets dropped due to wrong IP length, high byte.

        [net\_stats\_t](#c.net_stats_t) lblenerr
        :   Number of packets dropped due to wrong IP length, low byte.

        [net\_stats\_t](#c.net_stats_t) fragerr
        :   Number of packets dropped because they were IP fragments.

        [net\_stats\_t](#c.net_stats_t) chkerr
        :   Number of packets dropped due to IP checksum errors.

        [net\_stats\_t](#c.net_stats_t) protoerr
        :   Number of packets dropped because they were neither ICMP, UDP nor TCP.

    struct net\_stats\_icmp
    :   *#include <net\_stats.h>*

        ICMP statistics.

        Public Members

        [net\_stats\_t](#c.net_stats_t) recv
        :   Number of received ICMP packets.

        [net\_stats\_t](#c.net_stats_t) sent
        :   Number of sent ICMP packets.

        [net\_stats\_t](#c.net_stats_t) drop
        :   Number of dropped ICMP packets.

        [net\_stats\_t](#c.net_stats_t) typeerr
        :   Number of ICMP packets with a wrong type.

        [net\_stats\_t](#c.net_stats_t) chkerr
        :   Number of ICMP packets with a bad checksum.

    struct net\_stats\_tcp
    :   *#include <net\_stats.h>*

        TCP statistics.

        Public Members

        struct [net\_stats\_bytes](#c.net_stats_bytes) bytes
        :   Amount of received and sent TCP application data.

        [net\_stats\_t](#c.net_stats_t) resent
        :   Amount of retransmitted data.

        [net\_stats\_t](#c.net_stats_t) drop
        :   Number of dropped packets at the TCP layer.

        [net\_stats\_t](#c.net_stats_t) recv
        :   Number of received TCP segments.

        [net\_stats\_t](#c.net_stats_t) sent
        :   Number of sent TCP segments.

        [net\_stats\_t](#c.net_stats_t) seg\_drop
        :   Number of dropped TCP segments.

        [net\_stats\_t](#c.net_stats_t) chkerr
        :   Number of TCP segments with a bad checksum.

        [net\_stats\_t](#c.net_stats_t) ackerr
        :   Number of received TCP segments with a bad ACK number.

        [net\_stats\_t](#c.net_stats_t) rsterr
        :   Number of received bad TCP RST (reset) segments.

        [net\_stats\_t](#c.net_stats_t) rst
        :   Number of received TCP RST (reset) segments.

        [net\_stats\_t](#c.net_stats_t) rexmit
        :   Number of retransmitted TCP segments.

        [net\_stats\_t](#c.net_stats_t) conndrop
        :   Number of dropped connection attempts because too few connections were available.

        [net\_stats\_t](#c.net_stats_t) connrst
        :   Number of connection attempts for closed ports, triggering a RST.

    struct net\_stats\_udp
    :   *#include <net\_stats.h>*

        UDP statistics.

        Public Members

        [net\_stats\_t](#c.net_stats_t) drop
        :   Number of dropped UDP segments.

        [net\_stats\_t](#c.net_stats_t) recv
        :   Number of received UDP segments.

        [net\_stats\_t](#c.net_stats_t) sent
        :   Number of sent UDP segments.

        [net\_stats\_t](#c.net_stats_t) chkerr
        :   Number of UDP segments with a bad checksum.

    struct net\_stats\_ipv6\_nd
    :   *#include <net\_stats.h>*

        IPv6 neighbor discovery statistics.

    struct net\_stats\_ipv6\_mld
    :   *#include <net\_stats.h>*

        IPv6 multicast listener daemon statistics.

        Public Members

        [net\_stats\_t](#c.net_stats_t) recv
        :   Number of received IPv6 MLD queries.

        [net\_stats\_t](#c.net_stats_t) sent
        :   Number of sent IPv6 MLD reports.

        [net\_stats\_t](#c.net_stats_t) drop
        :   Number of dropped IPv6 MLD packets.

    struct net\_stats\_ipv4\_igmp
    :   *#include <net\_stats.h>*

        IPv4 IGMP daemon statistics.

        Public Members

        [net\_stats\_t](#c.net_stats_t) recv
        :   Number of received IPv4 IGMP queries.

        [net\_stats\_t](#c.net_stats_t) sent
        :   Number of sent IPv4 IGMP reports.

        [net\_stats\_t](#c.net_stats_t) drop
        :   Number of dropped IPv4 IGMP packets.

    struct net\_stats\_tx\_time
    :   *#include <net\_stats.h>*

        Network packet transfer times for calculating average TX time.

    struct net\_stats\_rx\_time
    :   *#include <net\_stats.h>*

        Network packet receive times for calculating average RX time.

    struct net\_stats\_tc
    :   *#include <net\_stats.h>*

        Traffic class statistics.

    struct net\_stats\_pm
    :   *#include <net\_stats.h>*

        Power management statistics.

    struct net\_stats
    :   *#include <net\_stats.h>*

        All network statistics in one struct.

        Public Members

        [net\_stats\_t](#c.net_stats_t) processing\_error
        :   Count of malformed packets or packets we do not have handler for.

        struct [net\_stats\_bytes](#c.net_stats_bytes) bytes
        :   This calculates amount of data transferred through all the network interfaces.

        struct [net\_stats\_ip\_errors](#c.net_stats_ip_errors) ip\_errors
        :   IP layer errors.

    struct net\_stats\_eth\_errors
    :   *#include <net\_stats.h>*

        Ethernet error statistics.

    struct net\_stats\_eth\_flow
    :   *#include <net\_stats.h>*

        Ethernet flow control statistics.

    struct net\_stats\_eth\_csum
    :   *#include <net\_stats.h>*

        Ethernet checksum statistics.

    struct net\_stats\_eth\_hw\_timestamp
    :   *#include <net\_stats.h>*

        Ethernet hardware timestamp statistics.

    struct net\_stats\_eth
    :   *#include <net\_stats.h>*

        All Ethernet specific statistics.

    struct net\_stats\_ppp
    :   *#include <net\_stats.h>*

        All PPP specific statistics.

        Public Members

        [net\_stats\_t](#c.net_stats_t) drop
        :   Number of received and dropped PPP frames.

        [net\_stats\_t](#c.net_stats_t) chkerr
        :   Number of received PPP frames with a bad checksum.

    struct net\_stats\_sta\_mgmt
    :   *#include <net\_stats.h>*

        All Wi-Fi management statistics.

        Public Members

        [net\_stats\_t](#c.net_stats_t) beacons\_rx
        :   Number of received beacons.

        [net\_stats\_t](#c.net_stats_t) beacons\_miss
        :   Number of missed beacons.

    struct net\_stats\_wifi
    :   *#include <net\_stats.h>*

        All Wi-Fi specific statistics.
