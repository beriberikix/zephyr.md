---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/net_config.html
original_path: connectivity/networking/api/net_config.html
---

# Network Configuration Library

## [Overview](#id2)

The network configuration library sets up networking devices in a
semi-automatic way during the system boot, based on user-supplied
Kconfig options.

The following Kconfig options affect how configuration library will
setup the system:

Kconfig options for network configuration library

| Option name | Description |
| --- | --- |
| [`CONFIG_NET_CONFIG_SETTINGS`](../../../kconfig.md#CONFIG_NET_CONFIG_SETTINGS "CONFIG_NET_CONFIG_SETTINGS") | This option controls whether the network system is configured or initialized at all. If not set, then the config library is not used for initialization and the application needs to do all the network related configuration itself. If this option is set, then the user can optionally configure static IP addresses to be set to the first network interface in the system. Typically setting static IP addresses is only usable in testing and should not be used in production code. See the config library Kconfig file [subsys/net/lib/config/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig) for specific options to set the static IP addresses. |
| [`CONFIG_NET_CONFIG_AUTO_INIT`](../../../kconfig.md#CONFIG_NET_CONFIG_AUTO_INIT "CONFIG_NET_CONFIG_AUTO_INIT") | The networking system is automatically configured when the device is started. |
| [`CONFIG_NET_CONFIG_INIT_TIMEOUT`](../../../kconfig.md#CONFIG_NET_CONFIG_INIT_TIMEOUT "CONFIG_NET_CONFIG_INIT_TIMEOUT") | This tells how long to wait for the networking to be ready and available. If for example IPv4 address from DHCPv4 is not received within this limit, then a call to `net_config_init()` will return error during the device startup. |
| [`CONFIG_NET_CONFIG_NEED_IPV4`](../../../kconfig.md#CONFIG_NET_CONFIG_NEED_IPV4 "CONFIG_NET_CONFIG_NEED_IPV4") | The network application needs IPv4 support to function properly. This option makes sure the network application is initialized properly in order to use IPv4. If [`CONFIG_NET_IPV4`](../../../kconfig.md#CONFIG_NET_IPV4 "CONFIG_NET_IPV4") is not enabled, then setting this option will automatically enable IPv4. |
| [`CONFIG_NET_CONFIG_NEED_IPV6`](../../../kconfig.md#CONFIG_NET_CONFIG_NEED_IPV6 "CONFIG_NET_CONFIG_NEED_IPV6") | The network application needs IPv6 support to function properly. This option makes sure the network application is initialized properly in order to use IPv6. If [`CONFIG_NET_IPV6`](../../../kconfig.md#CONFIG_NET_IPV6 "CONFIG_NET_IPV6") is not enabled, then setting this option will automatically enable IPv6. |
| [`CONFIG_NET_CONFIG_NEED_IPV6_ROUTER`](../../../kconfig.md#CONFIG_NET_CONFIG_NEED_IPV6_ROUTER "CONFIG_NET_CONFIG_NEED_IPV6_ROUTER") | If IPv6 is enabled, then this option tells that the network application needs IPv6 router to exists before continuing. This means in practice that the application wants to wait until it receives IPv6 router advertisement message before continuing. |
| [`CONFIG_NET_CONFIG_MY_IPV6_ADDR`](../../../kconfig.md#CONFIG_NET_CONFIG_MY_IPV6_ADDR "CONFIG_NET_CONFIG_MY_IPV6_ADDR") | Local static IPv6 address assigned to the default network interface. |
| [`CONFIG_NET_CONFIG_PEER_IPV6_ADDR`](../../../kconfig.md#CONFIG_NET_CONFIG_PEER_IPV6_ADDR "CONFIG_NET_CONFIG_PEER_IPV6_ADDR") | Peer static IPv6 address. This is mainly useful in testing setups where the application can connect to a pre-defined host. |
| [`CONFIG_NET_CONFIG_MY_IPV4_ADDR`](../../../kconfig.md#CONFIG_NET_CONFIG_MY_IPV4_ADDR "CONFIG_NET_CONFIG_MY_IPV4_ADDR") | Local static IPv4 address assigned to the default network interface. |
| [`CONFIG_NET_CONFIG_MY_IPV4_NETMASK`](../../../kconfig.md#CONFIG_NET_CONFIG_MY_IPV4_NETMASK "CONFIG_NET_CONFIG_MY_IPV4_NETMASK") | Static IPv4 netmask assigned to the IPv4 address. |
| [`CONFIG_NET_CONFIG_MY_IPV4_GW`](../../../kconfig.md#CONFIG_NET_CONFIG_MY_IPV4_GW "CONFIG_NET_CONFIG_MY_IPV4_GW") | Static IPv4 gateway address assigned to the default network interface. |
| [`CONFIG_NET_CONFIG_PEER_IPV4_ADDR`](../../../kconfig.md#CONFIG_NET_CONFIG_PEER_IPV4_ADDR "CONFIG_NET_CONFIG_PEER_IPV4_ADDR") | Peer static IPv4 address. This is mainly useful in testing setups where the application can connect to a pre-defined host. |

## [Sample usage](#id3)

If [`CONFIG_NET_CONFIG_AUTO_INIT`](../../../kconfig.md#CONFIG_NET_CONFIG_AUTO_INIT "CONFIG_NET_CONFIG_AUTO_INIT") is set, then the configuration library
is automatically enabled and run during the device boot. In this case,
the library will call `net_config_init()` automatically and the application
does not need to do any network configuration.

If you want to use the network configuration library but without automatic
initialization, you can call `net_config_init()` manually. The `flags`
parameter can be used to give hints to the library about what kind of
functionality the application wishes to have before the actual application
starts.

## [API Reference](#id4)

[Network Configuration Library](../../../doxygen/html/group__net__config.md)

Related code samples

- [zperf: Network Traffic Generator](../../../samples/net/zperf/README.md#zperf "Use the zperf shell utility to evaluate network bandwidth.")Use the zperf shell utility to evaluate network bandwidth.
