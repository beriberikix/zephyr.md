---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/net_shell.html
original_path: connectivity/networking/api/net_shell.html
---

# Network Shell

Network shell provides helpers for figuring out network status,
enabling/disabling features, and issuing commands like ping or DNS resolving.
Note that `net-shell` should probably not be used in production code
as it will require extra memory. See also [generic shell](../../../services/shell/index.md#shell-api)
for detailed shell information.

The following net-shell commands are implemented:

net-shell commands

| Command | Description |
| --- | --- |
| net allocs | Print network memory allocations. Only available if [`CONFIG_NET_DEBUG_NET_PKT_ALLOC`](../../../kconfig.md#CONFIG_NET_DEBUG_NET_PKT_ALLOC "CONFIG_NET_DEBUG_NET_PKT_ALLOC") is set. |
| net arp | Print information about IPv4 ARP cache. Only available if [`CONFIG_NET_ARP`](../../../kconfig.md#CONFIG_NET_ARP "CONFIG_NET_ARP") is set in IPv4 enabled networks. |
| net capture | Monitor network traffic See [Monitor Network Traffic](../network_monitoring.md#network-monitoring) for details. |
| net conn | Print information about network connections. |
| net dns | Show how DNS is configured. The command can also be used to resolve a DNS name. Only available if [`CONFIG_DNS_RESOLVER`](../../../kconfig.md#CONFIG_DNS_RESOLVER "CONFIG_DNS_RESOLVER") is set. |
| net events | Enable network event monitoring. Only available if [`CONFIG_NET_MGMT_EVENT_MONITOR`](../../../kconfig.md#CONFIG_NET_MGMT_EVENT_MONITOR "CONFIG_NET_MGMT_EVENT_MONITOR") is set. |
| net gptp | Print information about gPTP support. Only available if [`CONFIG_NET_GPTP`](../../../kconfig.md#CONFIG_NET_GPTP "CONFIG_NET_GPTP") is set. |
| net iface | Print information about network interfaces. |
| net ipv6 | Print IPv6 specific information and configuration. Only available if [`CONFIG_NET_IPV6`](../../../kconfig.md#CONFIG_NET_IPV6 "CONFIG_NET_IPV6") is set. |
| net mem | Print information about network memory usage. The command will print more information if [`CONFIG_NET_BUF_POOL_USAGE`](../../../kconfig.md#CONFIG_NET_BUF_POOL_USAGE "CONFIG_NET_BUF_POOL_USAGE") is set. |
| net nbr | Print neighbor information. Only available if [`CONFIG_NET_IPV6`](../../../kconfig.md#CONFIG_NET_IPV6 "CONFIG_NET_IPV6") is set. |
| net ping | Ping a network host. |
| net route | Show IPv6 network routes. Only available if `CONFIG_NET_ROUTE` is set. |
| net sockets | Show network socket information and statistics. Only available if [`CONFIG_NET_SOCKETS_OBJ_CORE`](../../../kconfig.md#CONFIG_NET_SOCKETS_OBJ_CORE "CONFIG_NET_SOCKETS_OBJ_CORE") and [`CONFIG_OBJ_CORE`](../../../kconfig.md#CONFIG_OBJ_CORE "CONFIG_OBJ_CORE") are set. |
| net stats | Show network statistics. |
| net tcp | Connect/send data/close TCP connection. Only available if [`CONFIG_NET_TCP`](../../../kconfig.md#CONFIG_NET_TCP "CONFIG_NET_TCP") is set. |
| net vlan | Show Ethernet virtual LAN information. Only available if [`CONFIG_NET_VLAN`](../../../kconfig.md#CONFIG_NET_VLAN "CONFIG_NET_VLAN") is set. |
