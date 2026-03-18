---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/net_mgmt.html
original_path: connectivity/networking/api/net_mgmt.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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
registered by using a [`NET_MGMT_REGISTER_REQUEST_HANDLER`](#c.NET_MGMT_REGISTER_REQUEST_HANDLER)
macro. Procedure requests are done through a single [`net_mgmt()`](#c.net_mgmt) API
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

To avoid extra cost, all [`net_mgmt()`](#c.net_mgmt) calls are direct. Though this
may change in a future release, it will not affect the users of this
function.

## [Listening to network events](#id3)

You can receive notifications on network events by registering a
callback function and specifying a set of events used to filter when
your callback is invoked. The callback will have to be unique for a
pair of layer and code, whereas on the command part it will be a mask of
events.

At runtime two functions are available, [`net_mgmt_add_event_callback()`](#c.net_mgmt_add_event_callback)
for registering the callback function, and [`net_mgmt_del_event_callback()`](#c.net_mgmt_del_event_callback)
for unregistering a callback. A helper function,
[`net_mgmt_init_event_callback()`](#c.net_mgmt_init_event_callback), can
be used to ease the initialization of the callback structure.

Additionally [`NET_MGMT_REGISTER_EVENT_HANDLER`](#c.NET_MGMT_REGISTER_EVENT_HANDLER) can be used to
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
set passed to [`net_mgmt_init_event_callback()`](#c.net_mgmt_init_event_callback).

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

Or similarly using [`NET_MGMT_REGISTER_EVENT_HANDLER`](#c.NET_MGMT_REGISTER_EVENT_HANDLER).

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

You can signal a specific network event using the [`net_mgmt_event_notify()`](#c.net_mgmt_event_notify)
function and provide the network event code. See
[include/zephyr/net/net\_mgmt.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/net_mgmt.h) for details. As for the management request
code, event code can be also found on specific L2 technology mgmt headers,
for example [include/zephyr/net/ieee802154\_mgmt.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/ieee802154_mgmt.h) would be the right place if
802.15.4 L2 is the technology one wants to listen to events.

## [API Reference](#id6)

Related code samples

[DHCPv4 client](../../../samples/net/dhcpv4_client/README.md#dhcpv4-client "Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.")
:   Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.

[DNS resolve](../../../samples/net/dns_resolve/README.md#dns-resolve "Resolve an IP address for a given hostname.")
:   Resolve an IP address for a given hostname.

[IPv4 autoconf client](../../../samples/net/ipv4_autoconf/README.md#ipv4-autoconf "Perform IPv4 autoconfiguration and self-assign a random IPv4 address")
:   Perform IPv4 autoconfiguration and self-assign a random IPv4 address

[Telnet console](../../../samples/net/telnet/README.md#telnet-console "Access Zephyr shell over telnet.")
:   Access Zephyr shell over telnet.

*group* net\_mgmt
:   Network Management.

    Defines

    net\_mgmt(\_mgmt\_request, \_iface, \_data, \_len)

    NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

    NET\_MGMT\_REGISTER\_REQUEST\_HANDLER(\_mgmt\_request, \_func)

    NET\_MGMT\_REGISTER\_EVENT\_HANDLER(\_name, \_event\_mask, \_func, \_user\_data)
    :   Define a static network event handler.

        Parameters:
        :   - **\_name** – Name of the event handler.
            - **\_event\_mask** – A mask of network events on which the passed handler should be called in case those events come. Note that only the command part is treated as a mask, matching one to several commands. Layer and layer code will be made of an exact match. This means that in order to receive events from multiple layers, one must have multiple listeners registered, one for each layer being listened.
            - **\_func** – The function to be called upon network events being emitted.
            - **\_user\_data** – User data passed to the handler being called on network events.

    Typedefs

    typedef int (\*net\_mgmt\_request\_handler\_t)(uint32\_t mgmt\_request, struct [net\_if](net_if.md#c.net_if "net_if") \*iface, void \*data, size\_t len)
    :   Signature which all Net MGMT request handler need to follow.

        Param mgmt\_request:
        :   The exact request value the handler is being called through

        Param iface:
        :   A valid pointer on struct [net\_if](net_if.md#structnet__if) if the request is meant to be tight to a network interface. NULL otherwise.

        Param data:
        :   A valid pointer on a data understood by the handler. NULL otherwise.

        Param len:
        :   Length in byte of the memory pointed by data.

    typedef void (\*net\_mgmt\_event\_handler\_t)(struct [net\_mgmt\_event\_callback](#c.net_mgmt_event_callback) \*cb, uint32\_t mgmt\_event, struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Define the user’s callback handler function signature.

        Param cb:
        :   Original struct [net\_mgmt\_event\_callback](#structnet__mgmt__event__callback) owning this handler.

        Param mgmt\_event:
        :   The network event being notified.

        Param iface:
        :   A pointer on a struct [net\_if](net_if.md#structnet__if) to which the event belongs to, if it’s an event on an iface. NULL otherwise.

    typedef void (\*net\_mgmt\_event\_static\_handler\_t)(uint32\_t mgmt\_event, struct [net\_if](net_if.md#c.net_if "net_if") \*iface, void \*info, size\_t info\_length, void \*user\_data)
    :   Define the user’s callback handler function signature.

        Param mgmt\_event:
        :   The network event being notified.

        Param iface:
        :   A pointer on a struct [net\_if](net_if.md#structnet__if) to which the event belongs to, if it’s an event on an iface. NULL otherwise.

        Param info:
        :   A valid pointer on a data understood by the handler. NULL otherwise.

        Param info\_length:
        :   Length in bytes of the memory pointed by `info`.

        Param user\_data:
        :   Data provided by the user to the handler.

    Functions

    static inline void net\_mgmt\_init\_event\_callback(struct [net\_mgmt\_event\_callback](#c.net_mgmt_event_callback) \*cb, [net\_mgmt\_event\_handler\_t](#c.net_mgmt_event_handler_t) handler, uint32\_t mgmt\_event\_mask)
    :   Helper to initialize a struct [net\_mgmt\_event\_callback](#structnet__mgmt__event__callback) properly.

        Parameters:
        :   - **cb** – A valid application’s callback structure pointer.
            - **handler** – A valid handler function pointer.
            - **mgmt\_event\_mask** – A mask of relevant events for the handler

    void net\_mgmt\_add\_event\_callback(struct [net\_mgmt\_event\_callback](#c.net_mgmt_event_callback) \*cb)
    :   Add a user callback.

        Parameters:
        :   - **cb** – A valid pointer on user’s callback to add.

    void net\_mgmt\_del\_event\_callback(struct [net\_mgmt\_event\_callback](#c.net_mgmt_event_callback) \*cb)
    :   Delete a user callback.

        Parameters:
        :   - **cb** – A valid pointer on user’s callback to delete.

    void net\_mgmt\_event\_notify\_with\_info(uint32\_t mgmt\_event, struct [net\_if](net_if.md#c.net_if "net_if") \*iface, const void \*info, size\_t length)
    :   Used by the system to notify an event.

        Note: info and length are disabled if CONFIG\_NET\_MGMT\_EVENT\_INFO is not defined.

        Parameters:
        :   - **mgmt\_event** – The actual network event code to notify
            - **iface** – a valid pointer on a struct [net\_if](net_if.md#structnet__if) if only the event is based on an iface. NULL otherwise.
            - **info** – a valid pointer on the information you want to pass along with the event. NULL otherwise. Note the data pointed there is normalized by the related event.
            - **length** – size of the data pointed by info pointer.

    static inline void net\_mgmt\_event\_notify(uint32\_t mgmt\_event, struct [net\_if](net_if.md#c.net_if "net_if") \*iface)

    int net\_mgmt\_event\_wait(uint32\_t mgmt\_event\_mask, uint32\_t \*raised\_event, struct [net\_if](net_if.md#c.net_if "net_if") \*\*iface, const void \*\*info, size\_t \*info\_length, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Used to wait synchronously on an event mask.

        Parameters:
        :   - **mgmt\_event\_mask** – A mask of relevant events to wait on.
            - **raised\_event** – a pointer on a uint32\_t to get which event from the mask generated the event. Can be NULL if the caller is not interested in that information.
            - **iface** – a pointer on a place holder for the iface on which the event has originated from. This is valid if only the event mask has bit NET\_MGMT\_IFACE\_BIT set relevantly, depending on events the caller wants to listen to.
            - **info** – a valid pointer if user wants to get the information the event might bring along. NULL otherwise.
            - **info\_length** – tells how long the info memory area is. Only valid if the info is not NULL.
            - **timeout** – A timeout delay. K\_FOREVER can be used to wait indefinitely.

        Returns:
        :   0 on success, a negative error code otherwise. -ETIMEDOUT will be specifically returned if the timeout kick-in instead of an actual event.

    int net\_mgmt\_event\_wait\_on\_iface(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, uint32\_t mgmt\_event\_mask, uint32\_t \*raised\_event, const void \*\*info, size\_t \*info\_length, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Used to wait synchronously on an event mask for a specific iface.

        Parameters:
        :   - **iface** – a pointer on a valid network interface to listen event to
            - **mgmt\_event\_mask** – A mask of relevant events to wait on. Listened to events should be relevant to iface events and thus have the bit NET\_MGMT\_IFACE\_BIT set.
            - **raised\_event** – a pointer on a uint32\_t to get which event from the mask generated the event. Can be NULL if the caller is not interested in that information.
            - **info** – a valid pointer if user wants to get the information the event might bring along. NULL otherwise.
            - **info\_length** – tells how long the info memory area is. Only valid if the info is not NULL.
            - **timeout** – A timeout delay. K\_FOREVER can be used to wait indefinitely.

        Returns:
        :   0 on success, a negative error code otherwise. -ETIMEDOUT will be specifically returned if the timeout kick-in instead of an actual event.

    void net\_mgmt\_event\_init(void)
    :   Used by the core of the network stack to initialize the network event processing.

    struct net\_event\_ipv6\_addr
    :   *#include <net\_event.h>*

        Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_ADDR\_ADD, NET\_EVENT\_IPV6\_ADDR\_DEL, NET\_EVENT\_IPV6\_MADDR\_ADD and NET\_EVENT\_IPV6\_MADDR\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.

    struct net\_event\_ipv6\_nbr
    :   *#include <net\_event.h>*

        Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_NBR\_ADD and NET\_EVENT\_IPV6\_NBR\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.

        Note

        : idx will be ‘-1’ in case of NET\_EVENT\_IPV6\_NBR\_DEL event.

    struct net\_event\_ipv6\_route
    :   *#include <net\_event.h>*

        Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_ROUTE\_ADD and NET\_EVENT\_IPV6\_ROUTE\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.

    struct net\_event\_ipv6\_prefix
    :   *#include <net\_event.h>*

        Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_PREFIX\_ADD and NET\_EVENT\_IPV6\_PREFIX\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information.

    struct net\_event\_l4\_hostname
    :   *#include <net\_event.h>*

        Network Management event information structure Used to pass information on NET\_EVENT\_HOSTNAME\_CHANGED event when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information.

    struct net\_mgmt\_event\_callback
    :   *#include <net\_mgmt.h>*

        Network Management event callback structure Used to register a callback into the network management event part, in order to let the owner of this struct to get network event notification based on given event mask.

        Public Members

        [sys\_snode\_t](../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Meant to be used internally, to insert the callback into a list.

            So nobody should mess with it.

        [net\_mgmt\_event\_handler\_t](#c.net_mgmt_event_handler_t) handler
        :   Actual callback function being used to notify the owner.

        struct k\_sem \*sync\_call
        :   Semaphore meant to be used internally for the synchronous [net\_mgmt\_event\_wait()](#group__net__mgmt_1gacbaa95c65717747d802dc80eb745aa17) function.

        uint32\_t event\_mask
        :   A mask of network events on which the above handler should be called in case those events come.

            Note that only the command part is treated as a mask, matching one to several commands. Layer and layer code will be made of an exact match. This means that in order to receive events from multiple layers, one must have multiple listeners registered, one for each layer being listened.

        uint32\_t raised\_event
        :   Internal place holder when a synchronous event wait is successfully unlocked on a event.

        union [net\_mgmt\_event\_callback](#c.net_mgmt_event_callback).[anonymous] [anonymous]
        :   A mask of network events on which the above handler should be called in case those events come.

            Such mask can be modified whenever necessary by the owner, and thus will affect the handler being called or not.
