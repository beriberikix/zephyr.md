---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/networking/api/net_mgmt.html
original_path: connectivity/networking/api/net_mgmt.html
---

# Network Management

## [Overview](#id1)

The Network Management APIs allow applications, as well as network
layer code itself, to call defined network routines at any level in
the IP stack, or receive notifications on relevant network events. For
example, by using these APIs, application code can request a scan be done on a
Wi-Fi- or Bluetooth-based network interface, or request notification if
a network interface IP address changes.

The Network Management API implementation is designed to save memory
by eliminating code at build time for management routines that are not
used. Distinct and statically defined APIs for network management
procedures are not used. Instead, defined procedure handlers are
registered by using a [`NET_MGMT_REGISTER_REQUEST_HANDLER`](../../../doxygen/html/group__net__mgmt.md#gab67d09d1e65b806ec1957451cbf60501)
macro. Procedure requests are done through a single [`net_mgmt()`](../../../doxygen/html/group__net__mgmt.md#ga40e0f9fc86812ad9f6fe174b4c3804e6) API
that invokes the registered handler for the corresponding request.

The current implementation is experimental and may change and improve
in future releases.

## [Requesting a defined procedure](#id2)

All network management requests are of the form
`net_mgmt(mgmt_request, ...)`. The `mgmt_request` parameter is a bit
mask that tells which stack layer is targeted, if a `net_if` object is
implied, and the specific management procedure being requested. The
available procedure requests depend on what has been implemented in
the stack.

To avoid extra cost, all [`net_mgmt()`](../../../doxygen/html/group__net__mgmt.md#ga40e0f9fc86812ad9f6fe174b4c3804e6) calls are direct. Though this
may change in a future release, it will not affect the users of this
function.

## [Listening to network events](#id3)

You can receive notifications on network events by registering a
callback function and specifying a set of events used to filter when
your callback is invoked. The callback will have to be unique for a
pair of layer and code, whereas on the command part it will be a mask of
events.

At runtime two functions are available, [`net_mgmt_add_event_callback()`](../../../doxygen/html/group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f)
for registering the callback function, and [`net_mgmt_del_event_callback()`](../../../doxygen/html/group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946)
for unregistering a callback. A helper function,
[`net_mgmt_init_event_callback()`](../../../doxygen/html/group__net__mgmt.md#gaa1d086dcdeb54412073e287129bc50e0), can
be used to ease the initialization of the callback structure.

Additionally [`NET_MGMT_REGISTER_EVENT_HANDLER`](../../../doxygen/html/group__net__mgmt.md#ga3a6ca8a72ab12afd4f9b0461253eaa12) can be used to
register a callback handler at compile time.

When an event occurs that matches a callback’s event set, the
associated callback function is invoked with the actual event
code. This makes it possible for different events to be handled by the
same callback function, if desired.

Warning

Event set filtering allows false positives for events that have the same
layer and layer code. A callback handler function **must** check
the event code (passed as an argument) against the specific network
events it will handle, **regardless** of how many events were in the
set passed to [`net_mgmt_init_event_callback()`](../../../doxygen/html/group__net__mgmt.md#gaa1d086dcdeb54412073e287129bc50e0).

Note that in order to receive events from multiple layers, one must have
multiple listeners registered, one for each layer being listened.
The callback handler function can be shared between different layer events.

(False positives can occur for events which have the same layer and
layer code.)

An example follows.

```c
/*
 * Set of events to handle.
 * See e.g. include/net/net_event.h for some NET_EVENT_xxx values.
 */
#define EVENT_IFACE_SET (NET_EVENT_IF_xxx | NET_EVENT_IF_yyy)
#define EVENT_IPV4_SET (NET_EVENT_IPV4_xxx | NET_EVENT_IPV4_yyy)

struct net_mgmt_event_callback iface_callback;
struct net_mgmt_event_callback ipv4_callback;

void callback_handler(struct net_mgmt_event_callback *cb,
                      uint32_t mgmt_event,
                      struct net_if *iface)
{
        if (mgmt_event == NET_EVENT_IF_xxx) {
                /* Handle NET_EVENT_IF_xxx */
        } else if (mgmt_event == NET_EVENT_IF_yyy) {
                /* Handle NET_EVENT_IF_yyy */
        } else if (mgmt_event == NET_EVENT_IPV4_xxx) {
                /* Handle NET_EVENT_IPV4_xxx */
        } else if (mgmt_event == NET_EVENT_IPV4_yyy) {
                /* Handle NET_EVENT_IPV4_yyy */
        } else {
                /* Spurious (false positive) invocation. */
        }
}

void register_cb(void)
{
        net_mgmt_init_event_callback(&iface_callback, callback_handler,
                                     EVENT_IFACE_SET);
        net_mgmt_init_event_callback(&ipv4_callback, callback_handler,
                                     EVENT_IPV4_SET);
        net_mgmt_add_event_callback(&iface_callback);
        net_mgmt_add_event_callback(&ipv4_callback);
}
```

Or similarly using [`NET_MGMT_REGISTER_EVENT_HANDLER`](../../../doxygen/html/group__net__mgmt.md#ga3a6ca8a72ab12afd4f9b0461253eaa12).

Note

The `info` and `info_length` arguments are only usable if
[`CONFIG_NET_MGMT_EVENT_INFO`](../../../kconfig.md#CONFIG_NET_MGMT_EVENT_INFO "CONFIG_NET_MGMT_EVENT_INFO") is enabled. Otherwise these are
`NULL` and zero.

```c
/*
 * Set of events to handle.
 */
#define EVENT_IFACE_SET (NET_EVENT_IF_xxx | NET_EVENT_IF_yyy)
#define EVENT_IPV4_SET (NET_EVENT_IPV4_xxx | NET_EVENT_IPV4_yyy)

static void event_handler(uint32_t mgmt_event, struct net_if *iface,
                          void *info, size_t info_length,
                          void *user_data)
{
        if (mgmt_event == NET_EVENT_IF_xxx) {
                /* Handle NET_EVENT_IF_xxx */
        } else if (mgmt_event == NET_EVENT_IF_yyy) {
                /* Handle NET_EVENT_IF_yyy */
        } else if (mgmt_event == NET_EVENT_IPV4_xxx) {
                /* Handle NET_EVENT_IPV4_xxx */
        } else if (mgmt_event == NET_EVENT_IPV4_yyy) {
                /* Handle NET_EVENT_IPV4_yyy */
        } else {
                /* Spurious (false positive) invocation. */
        }
}

NET_MGMT_REGISTER_EVENT_HANDLER(iface_event_handler, EVENT_IFACE_SET,
                                event_handler, NULL);
NET_MGMT_REGISTER_EVENT_HANDLER(ipv4_event_handler, EVENT_IPV4_SET,
                                event_handler, NULL);
```

See [include/zephyr/net/net\_event.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/net_event.h) for available generic core events that
can be listened to.

## [Defining a network management procedure](#id4)

You can provide additional management procedures specific to your
stack implementation by defining a handler and registering it with an
associated mgmt\_request code.

Management request code are defined in relevant places depending on
the targeted layer or eventually, if l2 is the layer, on the
technology as well. For instance, all IP layer management request code
will be found in the [include/zephyr/net/net\_event.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/net_event.h) header file. But in case
of an L2 technology, let’s say Ethernet, these would be found in
[include/zephyr/net/ethernet.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/ethernet.h)

You define your handler modeled with this signature:

```c
static int your_handler(uint32_t mgmt_event, struct net_if *iface,
                        void *data, size_t len);
```

and then register it with an associated mgmt\_request code:

```c
NET_MGMT_REGISTER_REQUEST_HANDLER(<mgmt_request code>, your_handler);
```

This new management procedure could then be called by using:

```c
net_mgmt(<mgmt_request code>, ...);
```

## [Signaling a network event](#id5)

You can signal a specific network event using the [`net_mgmt_event_notify()`](../../../doxygen/html/group__net__mgmt.md#ga0648b82762467395b98a3bc13ab451d0)
function and provide the network event code. See
[include/zephyr/net/net\_mgmt.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/net_mgmt.h) for details. As for the management request
code, event code can be also found on specific L2 technology mgmt headers,
for example [include/zephyr/net/ieee802154\_mgmt.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/ieee802154_mgmt.h) would be the right place if
802.15.4 L2 is the technology one wants to listen to events.

## [API Reference](#id6)

[Network Management](../../../doxygen/html/group__net__mgmt.md)

Related code samples

- [DHCPv4 client](../../../samples/net/dhcpv4_client/README.md#dhcpv4-client "Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.")Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.
- [DNS resolve](../../../samples/net/dns_resolve/README.md#dns-resolve "Resolve an IP address for a given hostname.")Resolve an IP address for a given hostname.
- [IPv4 autoconf client](../../../samples/net/ipv4_autoconf/README.md#ipv4-autoconf "Perform IPv4 autoconfiguration and self-assign a random IPv4 address")Perform IPv4 autoconfiguration and self-assign a random IPv4 address
- [Telnet console](../../../samples/net/telnet/README.md#telnet-console "Access Zephyr shell over telnet.")Access Zephyr shell over telnet.
