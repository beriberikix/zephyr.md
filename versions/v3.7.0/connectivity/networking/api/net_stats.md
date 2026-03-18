---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/net_stats.html
original_path: connectivity/networking/api/net_stats.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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

*group* Network Statistics Library
:   Network statistics library.

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

        Public Members

        [net\_stats\_t](#c.net_stats_t) drop
        :   Number of dropped IPv6 neighbor discovery packets.

        [net\_stats\_t](#c.net_stats_t) recv
        :   Number of received IPv6 neighbor discovery packets.

        [net\_stats\_t](#c.net_stats_t) sent
        :   Number of sent IPv6 neighbor discovery packets.

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

        Public Members

        uint64\_t sum
        :   Sum of network packet transfer times.

        [net\_stats\_t](#c.net_stats_t) count
        :   Number of network packets transferred.

    struct net\_stats\_rx\_time
    :   *#include <net\_stats.h>*

        Network packet receive times for calculating average RX time.

        Public Members

        uint64\_t sum
        :   Sum of network packet receive times.

        [net\_stats\_t](#c.net_stats_t) count
        :   Number of network packets received.

    struct net\_stats\_tc
    :   *#include <net\_stats.h>*

        Traffic class statistics.

        Public Members

        struct [net\_stats\_tx\_time](#c.net_stats_tx_time) tx\_time
        :   Helper for calculating average TX time statistics.

        [net\_stats\_t](#c.net_stats_t) pkts
        :   Number of packets sent for this traffic class.

            Number of packets received for this traffic class.

        [net\_stats\_t](#c.net_stats_t) bytes
        :   Number of bytes sent for this traffic class.

            Number of bytes received for this traffic class.

        uint8\_t priority
        :   Priority of this traffic class.

        struct [net\_stats\_tc](#c.net_stats_tc).[anonymous] sent[NET\_TC\_TX\_STATS\_COUNT]
        :   TX statistics for each traffic class.

        struct [net\_stats\_rx\_time](#c.net_stats_rx_time) rx\_time
        :   Helper for calculating average RX time statistics.

        struct [net\_stats\_tc](#c.net_stats_tc).[anonymous] recv[NET\_TC\_RX\_STATS\_COUNT]
        :   RX statistics for each traffic class.

    struct net\_stats\_pm
    :   *#include <net\_stats.h>*

        Power management statistics.

        Public Members

        uint64\_t overall\_suspend\_time
        :   Total suspend time.

        [net\_stats\_t](#c.net_stats_t) suspend\_count
        :   How many times we were suspended.

        uint32\_t last\_suspend\_time
        :   How long the last suspend took.

        uint32\_t start\_time
        :   Network interface last suspend start time.

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

        Public Members

        [net\_stats\_t](#c.net_stats_t) rx\_length\_errors
        :   Number of RX length errors.

        [net\_stats\_t](#c.net_stats_t) rx\_over\_errors
        :   Number of RX overrun errors.

        [net\_stats\_t](#c.net_stats_t) rx\_crc\_errors
        :   Number of RX CRC errors.

        [net\_stats\_t](#c.net_stats_t) rx\_frame\_errors
        :   Number of RX frame errors.

        [net\_stats\_t](#c.net_stats_t) rx\_no\_buffer\_count
        :   Number of RX [net\_pkt](net_pkt.md#structnet__pkt) allocation errors.

        [net\_stats\_t](#c.net_stats_t) rx\_missed\_errors
        :   Number of RX missed errors.

        [net\_stats\_t](#c.net_stats_t) rx\_long\_length\_errors
        :   Number of RX long length errors.

        [net\_stats\_t](#c.net_stats_t) rx\_short\_length\_errors
        :   Number of RX short length errors.

        [net\_stats\_t](#c.net_stats_t) rx\_align\_errors
        :   Number of RX buffer align errors.

        [net\_stats\_t](#c.net_stats_t) rx\_dma\_failed
        :   Number of RX DMA failed errors.

        [net\_stats\_t](#c.net_stats_t) rx\_buf\_alloc\_failed
        :   Number of RX [net\_buf](net_buf.md#structnet__buf) allocation errors.

        [net\_stats\_t](#c.net_stats_t) tx\_aborted\_errors
        :   Number of TX aborted errors.

        [net\_stats\_t](#c.net_stats_t) tx\_carrier\_errors
        :   Number of TX carrier errors.

        [net\_stats\_t](#c.net_stats_t) tx\_fifo\_errors
        :   Number of TX FIFO errors.

        [net\_stats\_t](#c.net_stats_t) tx\_heartbeat\_errors
        :   Number of TX heartbeat errors.

        [net\_stats\_t](#c.net_stats_t) tx\_window\_errors
        :   Number of TX window errors.

        [net\_stats\_t](#c.net_stats_t) tx\_dma\_failed
        :   Number of TX DMA failed errors.

        [net\_stats\_t](#c.net_stats_t) uncorr\_ecc\_errors
        :   Number of uncorrected ECC errors.

        [net\_stats\_t](#c.net_stats_t) corr\_ecc\_errors
        :   Number of corrected ECC errors.

    struct net\_stats\_eth\_flow
    :   *#include <net\_stats.h>*

        Ethernet flow control statistics.

        Public Members

        [net\_stats\_t](#c.net_stats_t) rx\_flow\_control\_xon
        :   Number of RX XON flow control.

        [net\_stats\_t](#c.net_stats_t) rx\_flow\_control\_xoff
        :   Number of RX XOFF flow control.

        [net\_stats\_t](#c.net_stats_t) tx\_flow\_control\_xon
        :   Number of TX XON flow control.

        [net\_stats\_t](#c.net_stats_t) tx\_flow\_control\_xoff
        :   Number of TX XOFF flow control.

    struct net\_stats\_eth\_csum
    :   *#include <net\_stats.h>*

        Ethernet checksum statistics.

        Public Members

        [net\_stats\_t](#c.net_stats_t) rx\_csum\_offload\_good
        :   Number of good RX checksum offloading.

        [net\_stats\_t](#c.net_stats_t) rx\_csum\_offload\_errors
        :   Number of failed RX checksum offloading.

    struct net\_stats\_eth\_hw\_timestamp
    :   *#include <net\_stats.h>*

        Ethernet hardware timestamp statistics.

        Public Members

        [net\_stats\_t](#c.net_stats_t) rx\_hwtstamp\_cleared
        :   Number of RX hardware timestamp cleared.

        [net\_stats\_t](#c.net_stats_t) tx\_hwtstamp\_timeouts
        :   Number of RX hardware timestamp timeout.

        [net\_stats\_t](#c.net_stats_t) tx\_hwtstamp\_skipped
        :   Number of RX hardware timestamp skipped.

    struct net\_stats\_eth
    :   *#include <net\_stats.h>*

        All Ethernet specific statistics.

        Public Members

        struct [net\_stats\_bytes](#c.net_stats_bytes) bytes
        :   Total number of bytes received and sent.

        struct [net\_stats\_pkts](#c.net_stats_pkts) pkts
        :   Total number of packets received and sent.

        struct [net\_stats\_pkts](#c.net_stats_pkts) broadcast
        :   Total number of broadcast packets received and sent.

        struct [net\_stats\_pkts](#c.net_stats_pkts) multicast
        :   Total number of multicast packets received and sent.

        struct [net\_stats\_pkts](#c.net_stats_pkts) errors
        :   Total number of errors in RX and TX.

        struct [net\_stats\_eth\_errors](#c.net_stats_eth_errors) error\_details
        :   Total number of errors in RX and TX.

        struct [net\_stats\_eth\_flow](#c.net_stats_eth_flow) flow\_control
        :   Total number of flow control errors in RX and TX.

        struct [net\_stats\_eth\_csum](#c.net_stats_eth_csum) csum
        :   Total number of checksum errors in RX and TX.

        struct [net\_stats\_eth\_hw\_timestamp](#c.net_stats_eth_hw_timestamp) hw\_timestamp
        :   Total number of hardware timestamp errors in RX and TX.

        [net\_stats\_t](#c.net_stats_t) collisions
        :   Total number of collisions.

        [net\_stats\_t](#c.net_stats_t) tx\_dropped
        :   Total number of dropped TX packets.

        [net\_stats\_t](#c.net_stats_t) tx\_timeout\_count
        :   Total number of TX timeout errors.

        [net\_stats\_t](#c.net_stats_t) tx\_restart\_queue
        :   Total number of TX queue restarts.

        [net\_stats\_t](#c.net_stats_t) unknown\_protocol
        :   Total number of RX unknown protocol packets.

    struct net\_stats\_ppp
    :   *#include <net\_stats.h>*

        All PPP specific statistics.

        Public Members

        struct [net\_stats\_bytes](#c.net_stats_bytes) bytes
        :   Total number of bytes received and sent.

        struct [net\_stats\_pkts](#c.net_stats_pkts) pkts
        :   Total number of packets received and sent.

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

        Public Members

        struct [net\_stats\_sta\_mgmt](#c.net_stats_sta_mgmt) sta\_mgmt
        :   Total number of beacon errors.

        struct [net\_stats\_bytes](#c.net_stats_bytes) bytes
        :   Total number of bytes received and sent.

        struct [net\_stats\_pkts](#c.net_stats_pkts) pkts
        :   Total number of packets received and sent.

        struct [net\_stats\_pkts](#c.net_stats_pkts) broadcast
        :   Total number of broadcast packets received and sent.

        struct [net\_stats\_pkts](#c.net_stats_pkts) multicast
        :   Total number of multicast packets received and sent.

        struct [net\_stats\_pkts](#c.net_stats_pkts) errors
        :   Total number of errors in RX and TX.

        struct [net\_stats\_pkts](#c.net_stats_pkts) unicast
        :   Total number of unicast packets received and sent.
