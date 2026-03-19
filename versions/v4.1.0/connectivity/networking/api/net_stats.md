---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/networking/api/net_stats.html
original_path: connectivity/networking/api/net_stats.html
---

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

[Network Statistics Library](../../../doxygen/html/group__net__stats.md)

Related code samples

- [Network statistics](../../../samples/net/stats/README.md#net-stats "Query and display network statistics from a user application.")Query and display network statistics from a user application.
- [OpenThread shell](../../../samples/net/openthread/shell/README.md#openthread-shell "Test Thread and IEEE 802.15.4 using the OpenThread shell.")Test Thread and IEEE 802.15.4 using the OpenThread shell.
- [Wi-Fi shell](../../../samples/net/wifi/shell/README.md#wifi-shell "Test Wi-Fi functionality using the Wi-Fi shell module.")Test Wi-Fi functionality using the Wi-Fi shell module.
