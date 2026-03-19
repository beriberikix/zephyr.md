---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/ethernet.html
original_path: connectivity/networking/api/ethernet.html
---

# Ethernet

## [Overview](#id1)

Ethernet is a networking technology commonly used in local area networks (LAN).
For more information, see this
[Ethernet Wikipedia article](https://en.wikipedia.org/wiki/Ethernet).

Zephyr supports following Ethernet features:

- 10, 100 and 1000 Mbit/sec links
- Auto negotiation
- Half/full duplex
- Promiscuous mode
- TX and RX checksum offloading
- MAC address filtering
- [Virtual LANs](vlan.md#vlan-interface)
- [Priority queues](traffic-class.md#traffic-class-support)
- [IEEE 802.1AS (gPTP)](gptp.md#gptp-interface)
- [IEEE 802.1Qav (credit based shaping)](8021Qav.md#qav)
- [LLDP (Link Layer Discovery Protocol)](lldp.md#lldp-interface)

Not all Ethernet device drivers support all of these features. You can
see what is supported by `net iface` net-shell command. It will print
currently supported Ethernet features.

## [API Reference](#id2)

[Ethernet Support Functions](../../../doxygen/html/group__ethernet.md)

Related code samples

- [Inter-VM Shared Memory (ivshmem) Ethernet](../../../samples/drivers/ethernet/eth_ivshmem/README.md#eth-ivshmem "Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.")Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.
- [Packet socket](../../../samples/net/sockets/packet/README.md#packet-socket "Use raw packet sockets over Ethernet.")Use raw packet sockets over Ethernet.
- [UDP sender using SO\_TXTIME](../../../samples/net/sockets/txtime/README.md#so_txtime "Control the transmission time of a packet using SO_TXTIME socket option.")Control the transmission time of a packet using SO\_TXTIME socket option.

[Ethernet MII Support Functions](../../../doxygen/html/group__ethernet__mii.md)
