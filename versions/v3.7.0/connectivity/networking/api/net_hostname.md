---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/net_hostname.html
original_path: connectivity/networking/api/net_hostname.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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
`net_hostname_set_postfix()` before the network interfaces are created.
For example for the Ethernet networks, the initialization priority is set by
[`CONFIG_ETH_INIT_PRIORITY`](../../../kconfig.md#CONFIG_ETH_INIT_PRIORITY "CONFIG_ETH_INIT_PRIORITY") so you would need to set the postfix before
that. The postfix can be set only once.

## [API Reference](#id2)

*group* Network Hostname Library
:   Network hostname configuration library.

    Defines

    NET\_HOSTNAME\_MAX\_LEN
    :   Maximum hostname length.

    Functions

    static inline const char \*net\_hostname\_get(void)
    :   Get the device hostname.

        Return pointer to device hostname.

        Returns:
        :   Pointer to hostname or NULL if not set.

    static inline int net\_hostname\_set(char \*host, size\_t len)
    :   Set the device hostname.

        Parameters:
        :   - **host** – new hostname as char array.
            - **len** – Length of the hostname array.

        Returns:
        :   0 if ok, <0 on error

    static inline void net\_hostname\_init(void)
    :   Initialize and set the device hostname.

    static inline int net\_hostname\_set\_postfix(const uint8\_t \*hostname\_postfix, int postfix\_len)
    :   Set the device hostname postfix.

        Set the device hostname to some value. This is only used if CONFIG\_NET\_HOSTNAME\_UNIQUE is set.

        Parameters:
        :   - **hostname\_postfix** – Usually link address. The function will convert this to a string.
            - **postfix\_len** – Length of the hostname\_postfix array.

        Returns:
        :   0 if ok, <0 if error
