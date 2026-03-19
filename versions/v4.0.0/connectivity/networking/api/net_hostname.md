---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/net_hostname.html
original_path: connectivity/networking/api/net_hostname.html
---

# Hostname Configuration

## [Overview](#id1)

A networked device might need a hostname, for example, if the device
is configured to be a mDNS responder (see [DNS Resolve](dns_resolve.md#dns-resolve-interface) for
details) and needs to respond to `<hostname>.local` DNS queries.

The [`CONFIG_NET_HOSTNAME_ENABLE`](../../../kconfig.md#CONFIG_NET_HOSTNAME_ENABLE "CONFIG_NET_HOSTNAME_ENABLE") must be set in order
to store the hostname and enable the relevant APIs. If the option is enabled,
then the default hostname is set to be `zephyr` by
[`CONFIG_NET_HOSTNAME`](../../../kconfig.md#CONFIG_NET_HOSTNAME "CONFIG_NET_HOSTNAME") option.

If the same firmware image is used to flash multiple boards, then it is not
practical to use the same hostname in all of the boards. In that case, one
can enable [`CONFIG_NET_HOSTNAME_UNIQUE`](../../../kconfig.md#CONFIG_NET_HOSTNAME_UNIQUE "CONFIG_NET_HOSTNAME_UNIQUE") which will add a unique
postfix to the hostname. By default the link local address of the first network
interface is used as a postfix. In Ethernet networks, the link local address
refers to MAC address. For example, if the link local address is
`01:02:03:04:05:06`, then the unique hostname could be
`zephyr010203040506`. If you want to set the prefix yourself, then call
`net_hostname_set_postfix_str()` before the network interfaces are created.
Alternatively, if you prefer a hexadecimal conversion for the prefix, then call
`net_hostname_set_postfix()`. For example for the Ethernet networks,
the initialization priority is set by [`CONFIG_ETH_INIT_PRIORITY`](../../../kconfig.md#CONFIG_ETH_INIT_PRIORITY "CONFIG_ETH_INIT_PRIORITY")
so you would need to set the postfix before that.
The postfix can be set only once.

## [API Reference](#id2)

[Network Hostname Library](../../../doxygen/html/group__net__hostname.md)
