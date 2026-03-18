---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/net_l2.html
original_path: connectivity/networking/api/net_l2.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# L2 Layer Management

## [Overview](#id1)

The L2 stack is designed to hide the whole networking link-layer part
and the related device drivers from the upper network stack. This is made
through a [`net_if`](net_if.md#c.net_if "net_if") declared in
[include/zephyr/net/net\_if.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/net_if.h).

The upper layers are unaware of implementation details beyond the net\_if
object and the generic API provided by the L2 layer in
[include/zephyr/net/net\_l2.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/net_l2.h) as [`net_l2`](#c.net_l2).

Only the L2 layer can talk to the device driver, linked to the net\_if
object. The L2 layer dictates the API provided by the device driver,
specific for that device, and optimized for working together.

Currently, there are L2 layers for [Ethernet](ethernet.md#ethernet-interface),
[IEEE 802.15.4 Soft-MAC](ieee802154.md#ieee802154-interface), [CANBUS](../../../hardware/peripherals/can/controller.md#can-api),
[OpenThread](thread.md#thread-protocol-interface), Wi-Fi, and a dummy layer example
that can be used as a template for writing a new one.

## [L2 layer API](#id2)

In order to create an L2 layer, or a driver for a specific L2 layer,
one needs to understand how the L3 layer interacts with it and
how the L2 layer is supposed to behave.
See also [network stack architecture](../net-stack-architecture.md#network-stack-architecture) for
more details. The generic L2 API has these functions:

- `recv()`: All device drivers, once they receive a packet which they put
  into a [`net_pkt`](net_pkt.md#c.net_pkt "net_pkt"), will push this buffer to the network
  stack via [`net_recv_data()`](net_core.md#c.net_recv_data "net_recv_data"). At this point, the network
  stack does not know what to do with it. Instead, it passes the
  buffer along to the L2 stack’s `recv()` function for handling.
  The L2 stack does what it needs to do with the packet, for example, parsing
  the link layer header, or handling link-layer only packets. The `recv()`
  function will return `NET_DROP` in case of an erroneous packet,
  `NET_OK` if the packet was fully consumed by the L2, or `NET_CONTINUE`
  if the network stack should then handle it.
- `send()`: Similar to receive function, the network stack will call this
  function to actually send a network packet. All relevant link-layer content
  will be generated and added by this function.
  The `send()` function returns the number of bytes sent, or a negative
  error code if there was a failure sending the network packet.
- `enable()`: This function is used to enable/disable traffic over a network
  interface. The function returns `<0` if error and `>=0` if no error.
- `get_flags()`: This function will return the capabilities of an L2 driver,
  for example whether the L2 supports multicast or promiscuous mode.

## [Network Device drivers](#id3)

Network device drivers fully follows Zephyr device driver model as a
basis. Please refer to [Device Driver Model](../../../kernel/drivers/index.md#device-model-api).

There are, however, two differences:

- The driver\_api pointer must point to a valid `net_if_api`
  pointer.
- The network device driver must use [`NET_DEVICE_INIT_INSTANCE()`](net_if.md#c.NET_DEVICE_INIT_INSTANCE "NET_DEVICE_INIT_INSTANCE")
  or [`ETH_NET_DEVICE_INIT()`](ethernet.md#c.ETH_NET_DEVICE_INIT "ETH_NET_DEVICE_INIT") for Ethernet devices. These
  macros will call the [`DEVICE_DEFINE()`](../../../kernel/drivers/index.md#c.DEVICE_DEFINE "DEVICE_DEFINE") macro, and also
  instantiate a unique [`net_if`](net_if.md#c.net_if "net_if") related to the created
  device driver instance.

Implementing a network device driver depends on the L2 stack it
belongs to: [Ethernet](ethernet.md#ethernet-interface),
[IEEE 802.15.4](ieee802154.md#ieee802154-interface), etc.
In the next section, we will describe how a device driver should behave when
receiving or sending a network packet. The rest is hardware dependent
and is not detailed here.

### [Ethernet device driver](#id4)

On reception, it is up to the device driver to fill-in the network packet with
as many data buffers as required. The network packet itself is a
[`net_pkt`](net_pkt.md#c.net_pkt "net_pkt") and should be allocated through
`net_pkt_rx_alloc_with_buffer()`. Then all data buffers will be
automatically allocated and filled by [`net_pkt_write()`](net_pkt.md#c.net_pkt_write "net_pkt_write").

After all the network data has been received, the device driver needs to
call [`net_recv_data()`](net_core.md#c.net_recv_data "net_recv_data"). If that call fails, it will be up to the
device driver to unreference the buffer via [`net_pkt_unref()`](net_pkt.md#c.net_pkt_unref "net_pkt_unref").

On sending, the device driver send function will be called, and it is up to
the device driver to send the network packet all at once, with all the buffers.

Each Ethernet device driver will need, in the end, to call
`ETH_NET_DEVICE_INIT()` like this:

```c
ETH_NET_DEVICE_INIT(..., CONFIG_ETH_INIT_PRIORITY,
                    &the_valid_net_if_api_instance, 1500);
```

### [IEEE 802.15.4 device driver](#id5)

Device drivers for IEEE 802.15.4 L2 work basically the same as for
Ethernet. What has been described above, especially for `recv()`, applies
here as well. There are two specific differences however:

- It requires a dedicated device driver API: [`ieee802154_radio_api`](ieee802154.md#c.ieee802154_radio_api "ieee802154_radio_api"),
  which overloads `net_if_api`. This is because 802.15.4 L2 needs more from the device
  driver than just `send()` and `recv()` functions. This dedicated API is
  declared in [include/zephyr/net/ieee802154\_radio.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/ieee802154_radio.h). Each and every
  IEEE 802.15.4 device driver must provide a valid pointer on such
  relevantly filled-in API structure.
- Sending a packet is slightly different than in Ethernet. Most IEEE 802.15.4
  PHYs support relatively small frames only, 127 bytes all inclusive: frame
  header, payload and frame checksum. Buffers to be sent over the radio will
  often not fit this frame size limitation, e.g. a buffer containing an IPv6
  packet will often have to be split into several fragments and IP6 packet headers
  and fragments need to be compressed using a protocol like 6LoWPAN before being
  passed on to the radio driver. Additionally the IEEE 802.15.4 standard defines
  medium access (e.g. CSMA/CA), frame retransmission, encryption and other pre-
  processing procedures (e.g. addition of information elements) that individual
  radio drivers should not have to care about. This is why the
  [`ieee802154_radio_api`](ieee802154.md#c.ieee802154_radio_api "ieee802154_radio_api") requires a tx function pointer which differs
  from the `net_if_api` send function pointer. Zephyr’s native
  IEEE 802.15.4 L2 implementation provides a generic `ieee802154_send()`
  instead, meant to be given as [`net_if`](net_if.md#c.net_if "net_if") send function. The implementation
  of `ieee802154_send()` takes care of IEEE 802.15.4 standard packet
  preparation procedures, splitting the packet into possibly compressed,
  encrypted and otherwise pre-processed fragment buffers, sending one buffer
  at a time through [`ieee802154_radio_api`](ieee802154.md#c.ieee802154_radio_api "ieee802154_radio_api") tx function and unreferencing
  the network packet only when the transmission as a whole was either successful
  or failed.

Interaction between IEEE 802.15.4 radio device drivers and L2 is bidirectional:

- L2 -> L1: Methods as `ieee802154_send()` and several IEEE 802.15.4 net
  management calls will call into the driver, e.g. to send a packet over the
  radio link or re-configure the driver at runtime. These incoming calls will
  all be handled by the methods in the [`ieee802154_radio_api`](ieee802154.md#c.ieee802154_radio_api "ieee802154_radio_api").
- L1 -> L2: There are several situations in which the driver needs to initiate
  calls into the L2/MAC layer. Zephyr’s IEEE 802.15.4 L1 -> L2 adaptation API
  employs an “inversion-of-control” pattern in such cases avoids duplication of
  complex logic across independent driver implementations and ensures
  implementation agnostic loose coupling and clean separation of concerns between
  MAC (L2) and PHY (L1) whenever reverse information transfer or close co-operation
  between hardware and L2 is required. During driver initialization, for example,
  the driver calls [`ieee802154_init()`](ieee802154.md#c.ieee802154_init "ieee802154_init") to pass the interface’s MAC address
  as well as other hardware-related configuration to L2. Similarly, drivers may
  indicate performance or timing critical radio events to L2 that require close
  integration with the hardware (e.g. [`ieee802154_handle_ack()`](ieee802154.md#c.ieee802154_handle_ack "ieee802154_handle_ack")). Calls
  from L1 into L2 are not implemented as methods in [`ieee802154_radio_api`](ieee802154.md#c.ieee802154_radio_api "ieee802154_radio_api")
  but are standalone functions declared and documented as such in
  [include/zephyr/net/ieee802154\_radio.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/ieee802154_radio.h). The API documentation will
  clearly state which functions must be implemented by all L2 stacks as part
  of the L1 -> L2 “inversion-of-control” adaptation API.

Note: Standalone functions in [include/zephyr/net/ieee802154\_radio.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/ieee802154_radio.h)
that are not explicitly documented as callbacks are considered to be helper functions
within the PHY (L1) layer implemented independently of any specific L2 stack, see for
example [`ieee802154_is_ar_flag_set()`](ieee802154.md#c.ieee802154_is_ar_flag_set "ieee802154_is_ar_flag_set").

As all net interfaces, IEEE 802.15.4 device driver implementations will have to call
`NET_DEVICE_INIT_INSTANCE()` in the end:

```c
NET_DEVICE_INIT_INSTANCE(...,
                         the_device_init_prio,
                         &the_valid_ieee802154_radio_api_instance,
                         IEEE802154_L2,
                         NET_L2_GET_CTX_TYPE(IEEE802154_L2), 125);
```

## [API Reference](#id6)

Related code samples

[Link Layer Discovery Protocol (LLDP)](../../../samples/net/lldp/README.md#lldp "Enable LLDP support and setup VLANs.")
:   Enable LLDP support and setup VLANs.

[Virtual LAN](../../../samples/net/vlan/README.md#vlan "Setup two virtual LAN networks and use net-shell to view the networks' settings.")
:   Setup two virtual LAN networks and use net-shell to view the networks' settings.

*group* Network L2 Abstraction Layer
:   Network Layer 2 abstraction layer.

    Enums

    enum net\_l2\_flags
    :   L2 flags.

        *Values:*

        enumerator NET\_L2\_MULTICAST = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   IP multicast supported.

        enumerator NET\_L2\_MULTICAST\_SKIP\_JOIN\_SOLICIT\_NODE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Do not join solicited node multicast group.

        enumerator NET\_L2\_PROMISC\_MODE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Is promiscuous mode supported.

        enumerator NET\_L2\_POINT\_TO\_POINT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Is this L2 point-to-point with tunneling so no need to have IP address etc to network interface.

    struct net\_l2
    :   *#include <net\_l2.h>*

        Network L2 structure.

        Used to provide an interface to lower network stack.

        Public Members

        enum [net\_verdict](net_core.md#c.net_verdict "net_verdict") (\*recv)(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, struct [net\_pkt](net_pkt.md#c.net_pkt "net_pkt") \*pkt)
        :   This function is used by net core to get iface’s L2 layer parsing what’s relevant to itself.

        int (\*send)(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, struct [net\_pkt](net_pkt.md#c.net_pkt "net_pkt") \*pkt)
        :   This function is used by net core to push a packet to lower layer (interface’s L2), which in turn might work on the packet relevantly.

            (adding proper header etc…) Returns a negative error code, or the number of bytes sent otherwise.

        int (\*enable)(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, bool state)
        :   This function is used to enable/disable traffic over a network interface.

            The function returns <0 if error and >=0 if no error.

        enum [net\_l2\_flags](#c.net_l2_flags) (\*get\_flags)(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
        :   Return L2 flags for the network interface.
