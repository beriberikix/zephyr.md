---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/conn_mgr/main.html
original_path: connectivity/networking/conn_mgr/main.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Overview

Connection Manager is a collection of optional Zephyr features that aim to allow applications to monitor and control connectivity (access to IP-capable networks) with minimal concern for the specifics of underlying network technologies.

Using Connection Manager, applications can use a single abstract API to control network association and monitor Internet access, and avoid excessive use of technology-specific boilerplate.

This allows an application to potentially support several very different connectivity technologies (for example, Wi-Fi and LTE) with a single codebase.

Applications can also use Connection Manager to generically manage and use multiple connectivity technologies simultaneously.

## Structure

Connection Manager is split into the following two subsystems:

- [Connectivity monitoring](#conn-mgr-monitoring) (header file `include/zephyr/net/conn_mgr_monitoring.h`) monitors all available [Zephyr network interfaces (ifaces)](../api/net_if.md#net-if-interface) and triggers [network management](../api/net_mgmt.md#net-mgmt-interface) events indicating when IP connectivity is gained or lost.
- [Connectivity control](#conn-mgr-control) (header file `include/zephyr/net/conn_mgr_connectivity.h`) provides an abstract API for controlling iface network association.

![A simplified view of how Connection Manager integrates with Zephyr and the application.](../../../_images/integration_diagram_simplified.svg)

A simplified view of how Connection Manager integrates with Zephyr and the application.

See [here](implementation.md#conn-mgr-integration-diagram-detailed) for a more detailed version.

# Connectivity monitoring

Connectivity monitoring tracks all available ifaces (whether or not they support [Connectivity control](#conn-mgr-control)) as they transition through various [operational states](../api/net_if.md#net-if-interface-state-management) and acquire or lose assigned IP addresses.

Each available iface is considered ready if it meets the following criteria:

- The iface is admin-up

  - This means the iface has been instructed to become operational-up (ready for use). This is done by a call to [`net_if_up()`](../api/net_if.md#c.net_if_up "net_if_up").
- The iface is oper-up

  - This means the interface is completely ready for use; It is online, and if applicable, has associated with a network.
  - See [Network interface state management](../api/net_if.md#net-if-interface-state-management) for details.
- The iface has at least one assigned IP address

  - Both IPv4 and IPv6 addresses are acceptable.
    This condition is met as soon as one or both of these is assigned.
  - See [Network Interface](../api/net_if.md#net-if-interface) for details on iface IP assignment.
- The iface has not been ignored

  - Ignored ifaces are always treated as unready.
  - See [Ignoring ifaces](#conn-mgr-monitoring-ignoring-ifaces) for more details.

Note

Typically, iface state and IP assignment are updated either by the iface’s [L2 implementation](../api/net_l2.md#net-l2-interface) or bound [connectivity implementation](implementation.md#conn-mgr-impl).

See [Implement iface state reporting](implementation.md#conn-mgr-impl-guidelines-iface-state-reporting) for details.

A ready iface ceases to be ready the moment any of the above conditions is lost.

When at least one iface is ready, the [`NET_EVENT_L4_CONNECTED`](../api/net_mgmt.md#c.NET_EVENT_L4_CONNECTED "NET_EVENT_L4_CONNECTED") [network management](../api/net_mgmt.md#net-mgmt-interface) event is triggered, and IP connectivity is said to be ready.

Afterwards, ifaces can become ready or unready without firing additional events, so long as there always remains at least one ready iface.

When there are no longer any ready ifaces left, the [`NET_EVENT_L4_DISCONNECTED`](../api/net_mgmt.md#c.NET_EVENT_L4_DISCONNECTED "NET_EVENT_L4_DISCONNECTED") [network management](../api/net_mgmt.md#net-mgmt-interface) event is triggered, and IP connectivity is said to be unready.

Note

Connection Manager also fires the following more specific `CONNECTED` / `DISCONNECTED` events:

- [`NET_EVENT_L4_IPV4_CONNECTED`](../api/net_mgmt.md#c.NET_EVENT_L4_IPV4_CONNECTED "NET_EVENT_L4_IPV4_CONNECTED")
- [`NET_EVENT_L4_IPV4_DISCONNECTED`](../api/net_mgmt.md#c.NET_EVENT_L4_IPV4_DISCONNECTED "NET_EVENT_L4_IPV4_DISCONNECTED")
- [`NET_EVENT_L4_IPV6_CONNECTED`](../api/net_mgmt.md#c.NET_EVENT_L4_IPV6_CONNECTED "NET_EVENT_L4_IPV6_CONNECTED")
- [`NET_EVENT_L4_IPV6_DISCONNECTED`](../api/net_mgmt.md#c.NET_EVENT_L4_IPV6_DISCONNECTED "NET_EVENT_L4_IPV6_DISCONNECTED")

These are similar to [`NET_EVENT_L4_CONNECTED`](../api/net_mgmt.md#c.NET_EVENT_L4_CONNECTED "NET_EVENT_L4_CONNECTED") and [`NET_EVENT_L4_DISCONNECTED`](../api/net_mgmt.md#c.NET_EVENT_L4_DISCONNECTED "NET_EVENT_L4_DISCONNECTED"), but specifically track whether IPv4- and IPv6-capable ifaces are ready.

## Usage

Connectivity monitoring is enabled if the [`CONFIG_NET_CONNECTION_MANAGER`](../../../kconfig.md#CONFIG_NET_CONNECTION_MANAGER "CONFIG_NET_CONNECTION_MANAGER") Kconfig option is enabled.

To receive connectivity updates, create and register a listener for the [`NET_EVENT_L4_CONNECTED`](../api/net_mgmt.md#c.NET_EVENT_L4_CONNECTED "NET_EVENT_L4_CONNECTED") and [`NET_EVENT_L4_DISCONNECTED`](../api/net_mgmt.md#c.NET_EVENT_L4_DISCONNECTED "NET_EVENT_L4_DISCONNECTED") [network management](../api/net_mgmt.md#net-mgmt-interface) events:

```c
/* Callback struct where the callback will be stored */
struct net_mgmt_event_callback l4_callback;

/* Callback handler */
static void l4_event_handler(struct net_mgmt_event_callback *cb,
                             uint32_t event, struct net_if *iface)
{
        if (event == NET_EVENT_L4_CONNECTED) {
                LOG_INF("Network connectivity gained!");
        } else if (event == NET_EVENT_L4_DISCONNECTED) {
                LOG_INF("Network connectivity lost!");
        }

        /* Otherwise, it's some other event type we didn't register for. */
}

/* Call this before Connection Manager monitoring initializes */
static void my_application_setup(void)
{
        /* Configure the callback struct to respond to (at least) the L4_CONNECTED
         * and L4_DISCONNECTED events.
         *
         *
         * Note that the callback may also be triggered for events other than those specified here!
         * (See the net_mgmt documentation)
         */
        net_mgmt_init_event_callback(
                &l4_callback, l4_event_handler,
                NET_EVENT_L4_CONNECTED | NET_EVENT_L4_DISCONNECTED
        );

        /* Register the callback */
        net_mgmt_add_event_callback(&l4_callback);
}
```

See [Listening to network events](../api/net_mgmt.md#net-mgmt-listening) for more details on listening for net\_mgmt events.

Note

To avoid missing initial connectivity events, you should register your listener(s) before Connection Manager monitoring initializes.
See [Avoiding missed notifications](#conn-mgr-monitoring-missing-notifications) for strategies to ensure this.

## Avoiding missed notifications

Connectivity monitoring may trigger events immediately upon initialization.

If your application registers its event listeners after connectivity monitoring initializes, it is possible to miss this first wave of events, and not be informed the first time network connectivity is gained.

If this is a concern, your application should [register its event listeners](#conn-mgr-monitoring-usage) before connectivity monitoring initializes.

Connectivity monitoring initializes using the `SYS_INIT` `APPLICATION` initialization priority specified by the [`CONFIG_NET_CONNECTION_MANAGER_MONITOR_PRIORITY`](../../../kconfig.md#CONFIG_NET_CONNECTION_MANAGER_MONITOR_PRIORITY "CONFIG_NET_CONNECTION_MANAGER_MONITOR_PRIORITY") Kconfig option.

You can register your callbacks before this initialization by using `SYS_INIT` with an earlier initialization priority than this value, for instance priority 0:

```c
static int my_application_setup(void)
{
        /* Register callbacks here */
        return 0;
}

SYS_INIT(my_application_setup, APPLICATION, 0);
```

If this is not feasible, you can instead request that connectivity monitoring resend the latest connectivity events at any time by calling [`conn_mgr_mon_resend_status()`](#c.conn_mgr_mon_resend_status):

```c
static void my_late_application_setup(void)
{
  /* Register callbacks here */

  /* Once done, request that events be re-triggered */
  conn_mgr_mon_resend_status();
}
```

## Ignoring ifaces

Applications can request that ifaces be ignored by Connection Manager by calling [`conn_mgr_ignore_iface()`](#c.conn_mgr_ignore_iface) with the iface to be ignored.

Alternatively, an entire [L2 implementation](../api/net_l2.md#net-l2-interface) can be ignored by calling [`conn_mgr_ignore_l2()`](#c.conn_mgr_ignore_l2).

This has the effect of individually ignoring all the ifaces using that [L2 implementation](../api/net_l2.md#net-l2-interface).

While ignored, the iface is treated by Connection Manager as though it were unready for network traffic, no matter its actual state.

This may be useful, for instance, if your application has configured one or more ifaces that cannot (or for whatever reason should not) be used to contact the wider Internet.

[Bulk convenience functions](#conn-mgr-control-api-bulk) optionally skip ignored ifaces.

See [`conn_mgr_ignore_iface()`](#c.conn_mgr_ignore_iface) and [`conn_mgr_watch_iface()`](#c.conn_mgr_watch_iface) for more details.

## Connectivity monitoring API

Include header file `include/zephyr/net/conn_mgr_monitoring.h` to access these.

*group* Connection Manager API
:   Connection Manager API.

    Functions

    void conn\_mgr\_mon\_resend\_status(void)
    :   Resend either NET\_L4\_CONNECTED or NET\_L4\_DISCONNECTED depending on whether connectivity is currently available.

    void conn\_mgr\_ignore\_iface(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface)
    :   Mark an iface to be ignored by conn\_mgr.

        Ignoring an iface forces conn\_mgr to consider it unready/disconnected.

        This means that events related to the iface connecting/disconnecting will not be fired, and if the iface was connected before being ignored, events will be fired as though it disconnected at that moment.

        Parameters:
        :   - **iface** – iface to be ignored.

    void conn\_mgr\_watch\_iface(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface)
    :   Watch (stop ignoring) an iface.

        conn\_mgr will no longer be forced to consider the iface unreadly/disconnected.

        Events related to the iface connecting/disconnecting will no longer be blocked, and if the iface was connected before being watched, events will be fired as though it connected in that moment.

        All ifaces default to watched at boot.

        Parameters:
        :   - **iface** – iface to no longer ignore.

    bool conn\_mgr\_is\_iface\_ignored(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface)
    :   Check whether the provided iface is currently ignored.

        Parameters:
        :   - **iface** – The iface to check.

        Return values:
        :   - **true** – if the iface is being ignored by conn\_mgr.
            - **false** – if the iface is being watched by conn\_mgr.

    void conn\_mgr\_ignore\_l2(const struct [net\_l2](../api/net_l2.md#c.net_l2 "net_l2") \*l2)
    :   Mark an L2 to be ignored by conn\_mgr.

        This is a wrapper for conn\_mgr\_ignore\_iface that ignores all ifaces that use the L2.

        Parameters:
        :   - **l2** – L2 to be ignored.

    void conn\_mgr\_watch\_l2(const struct [net\_l2](../api/net_l2.md#c.net_l2 "net_l2") \*l2)
    :   Watch (stop ignoring) an L2.

        This is a wrapper for conn\_mgr\_watch\_iface that watches all ifaces that use the L2.

        Parameters:
        :   - **l2** – L2 to watch.

# Connectivity control

Many network interfaces require a network association procedure to be completed before being usable.

For such ifaces, connectivity control can provide a generic API to request network association ([`conn_mgr_if_connect()`](#c.conn_mgr_if_connect)) and disassociation ([`conn_mgr_if_disconnect()`](#c.conn_mgr_if_disconnect)).
Network interfaces implement support for this API by [binding themselves to a connectivity implementation](implementation.md#conn-mgr-impl-binding).

Using this API, applications can associate with networks with minimal technology-specific boilerplate.

Connectivity control also provides the following additional features:

- Standardized [persistence and timeout](#conn-mgr-control-persistence-timeouts) behaviors during association.
- [Bulk functions](#conn-mgr-control-api-bulk) for controlling the admin state and network association of all available ifaces simultaneously.
- Optional [convenience automations](#conn-mgr-control-automations) for common connectivity actions.

## Basic operation

The following sections outline the basic operation of Connection Manager’s connectivity control.

### Binding

Before an iface can be commanded to associate or disassociate using Connection Manager, it must first be bound to a [connectivity implementation](implementation.md#conn-mgr-impl).
Binding is performed by the provider of the iface, not by the application (see [Binding an iface to an implementation](implementation.md#conn-mgr-impl-binding)), and can be thought of as an extension of the iface declaration.

Once an iface is bound, all connectivity commands passed to it (such as [`conn_mgr_if_connect()`](#c.conn_mgr_if_connect) or [`conn_mgr_if_disconnect()`](#c.conn_mgr_if_disconnect)) will be routed to the corresponding implementation function in the connectivity implementation.

Note

To avoid inconsistent behavior, all connectivity implementations must adhere to the [implementation guidelines](implementation.md#conn-mgr-impl-guidelines).

### Connecting

Once a bound iface is admin-up (see [Network interface state management](../api/net_if.md#net-if-interface-state-management)), [`conn_mgr_if_connect()`](#c.conn_mgr_if_connect) can be called to cause it to associate with a network.

If association succeeds, the connectivity implementation will mark the iface as operational-up (see [Network interface state management](../api/net_if.md#net-if-interface-state-management)).

If association fails unrecoverably, the [fatal error event](#conn-mgr-control-events-fatal-error) will be triggered.

You can configure an optional [timeout](#conn-mgr-control-timeouts) for this process.

Note

The [`conn_mgr_if_connect()`](#c.conn_mgr_if_connect) function is intentionally minimalistic, and does not take any kind of configuration.
Each connectivity implementation should provide a way to pre-configure or automatically configure any required association settings or credentials.
See [Allow connectivity pre-configuration](implementation.md#conn-mgr-impl-guidelines-preconfig) for details.

### Connection loss

If connectivity is lost due to external factors, the connectivity implementation will mark the iface as operational-down.

Depending on whether [persistence](#conn-mgr-control-persistence) is set, the iface may then attempt to reconnect.

### Manual disconnection

The application can also request that connectivity be intentionally abandoned by calling [`conn_mgr_if_disconnect()`](#c.conn_mgr_if_disconnect).

In this case, the connectivity implementation will disassociate the iface from its network and mark the iface as operational-down (see [Network interface state management](../api/net_if.md#net-if-interface-state-management)).
A new connection attempt will not be initiated, regardless of whether persistence is enabled.

## Timeouts and Persistence

Connection Manager requires that all connectivity implementations support the following standard key features:

- [Connection timeouts](#conn-mgr-control-timeouts)
- [Connection persistence](#conn-mgr-control-persistence)

These features describe how ifaces should behave during connect and disconnect events.
You can individually set them for each iface.

Note

It is left to connectivity implementations to successfully and accurately implement these two features as described below.
See [Implementing timeouts and persistence](implementation.md#conn-mgr-impl-timeout-persistence) for more details from the connectivity implementation perspective.

### Connection Timeouts

When [`conn_mgr_if_connect()`](#c.conn_mgr_if_connect) is called on an iface, a connection attempt begins.

The connection attempt continues indefinitely until it succeeds, unless a timeout has been specified for the iface (using [`conn_mgr_if_set_timeout()`](#c.conn_mgr_if_set_timeout)).

In that case, the connection attempt will be abandoned if the timeout elapses before it succeeds.
If this happens, the [timeout event](#conn-mgr-control-events-timeout) is raised.

### Connection Persistence

Each iface also has a connection persistence setting that you can enable or disable by setting the [`CONN_MGR_IF_PERSISTENT`](#c.conn_mgr_if_flag.CONN_MGR_IF_PERSISTENT) flag with [`conn_mgr_binding_set_flag()`](implementation.md#c.conn_mgr_binding_set_flag "conn_mgr_binding_set_flag").

This setting specifies how the iface should handle unintentional connection loss.

If persistence is enabled, any unintentional connection loss will initiate a new connection attempt, with a new timeout if applicable.

Otherwise, the iface will not attempt to reconnect.

Note

Persistence not does affect connection attempt behavior.
Only the timeout setting affects this.

For instance, if a connection attempt on an iface times out, the iface will not attempt to reconnect, even if it is persistent.

Conversely, if there is not a specified timeout, the iface will try to connect forever until it succeeds, even if it is not persistent.

See [Persistence during connection attempts](implementation.md#conn-mgr-impl-tp-persistence-during-connect) for the equivalent implementation guideline.

## Control events

Connectivity control triggers [network management](../api/net_mgmt.md#net-mgmt-interface) events to inform the application of important state changes.

See [Trigger connectivity control events](implementation.md#conn-mgr-impl-guidelines-trigger-events) for the corresponding connectivity implementation guideline.

### Fatal Error

The [`NET_EVENT_CONN_IF_FATAL_ERROR`](#c.NET_EVENT_CONN_IF_FATAL_ERROR) event is raised when an iface encounters an error from which it cannot recover (meaning any subsequent attempts to associate are guaranteed to fail, and all such attempts should be abandoned).

Handlers of this event will be passed a pointer to the iface for which the fatal error occurred.
Individual connectivity implementations may also pass an application-specific data pointer.

### Timeout

The [`NET_EVENT_CONN_IF_TIMEOUT`](#c.NET_EVENT_CONN_IF_TIMEOUT) event is raised when an [iface association](#conn-mgr-control-operation-connecting) attempt [times out](#conn-mgr-control-timeouts).

Handlers of this event will be passed a pointer to the iface that timed out attempting to associate.

### Listening for control events

You can listen for control events as follows:

```c
/* Declare a net_mgmt callback struct to store the callback */
struct net_mgmt_event_callback my_conn_evt_callback;

/* Declare a handler to receive control events */
static void my_conn_evt_handler(struct net_mgmt_event_callback *cb,
                                uint32_t event, struct net_if *iface)
{
        if (event == NET_EVENT_CONN_IF_TIMEOUT) {
                /* Timeout occurred, handle it */
        } else if (event == NET_EVENT_CONN_IF_FATAL_ERROR) {
                /* Fatal error occurred, handle it */
        }

        /* Otherwise, it's some other event type we didn't register for. */
}

int main()
{
        /* Configure the callback struct to respond to (at least) the CONN_IF_TIMEOUT
         * and CONN_IF_FATAL_ERROR events.
         *
         * Note that the callback may also be triggered for events other than those specified here!
         * (See the net_mgmt documentation)
         */

        net_mgmt_init_event_callback(
                &conn_mgr_conn_callback, conn_mgr_conn_handler,
                    NET_EVENT_CONN_IF_TIMEOUT | NET_EVENT_CONN_IF_FATAL_ERROR
        );

        /* Register the callback */
        net_mgmt_add_event_callback(&conn_mgr_conn_callback);
        return 0;
}
```

See [Listening to network events](../api/net_mgmt.md#net-mgmt-listening) for more details on listening for net\_mgmt events.

## Automated behaviors

There are a few actions related to connectivity that are (by default at least) performed automatically for the user.

Automatic admin-up

In Zephyr, ifaces are automatically taken admin-up (see [Network interface state management](../api/net_if.md#net-if-interface-state-management) for details on iface states) during initialization.

Applications can disable this behavior by setting the [`NET_IF_NO_AUTO_START`](../api/net_if.md#c.net_if_flag.NET_IF_NO_AUTO_START "net_if_flag.NET_IF_NO_AUTO_START") interface flag with [`net_if_flag_set()`](../api/net_if.md#c.net_if_flag_set "net_if_flag_set").

Automatic connect

By default, Connection Manager will automatically connect any [bound](implementation.md#conn-mgr-impl-binding) iface that becomes admin-up.

Applications can disable this by setting the [`CONN_MGR_IF_NO_AUTO_CONNECT`](#c.conn_mgr_if_flag.CONN_MGR_IF_NO_AUTO_CONNECT) connectivity flag with [`conn_mgr_if_set_flag()`](#c.conn_mgr_if_set_flag).

Automatic admin-down

By default, Connection Manager will automatically take any bound iface admin-down if it has given up on associating.

Applications can disable this for all ifaces by disabling the [`CONFIG_NET_CONNECTION_MANAGER_AUTO_IF_DOWN`](../../../kconfig.md#CONFIG_NET_CONNECTION_MANAGER_AUTO_IF_DOWN "CONFIG_NET_CONNECTION_MANAGER_AUTO_IF_DOWN") Kconfig option, or for individual ifaces by setting the [`CONN_MGR_IF_NO_AUTO_DOWN`](#c.conn_mgr_if_flag.CONN_MGR_IF_NO_AUTO_DOWN) connectivity flag with [`conn_mgr_if_set_flag()`](#c.conn_mgr_if_set_flag).

## Connectivity control API

Include header file `include/zephyr/net/conn_mgr_connectivity.h` to access these.

*group* Connection Manager Connectivity API
:   Connection Manager Connectivity API.

    **Since**
    :   3.4

    **Version**
    :   0.1.0

    Defines

    NET\_EVENT\_CONN\_IF\_TIMEOUT
    :   net\_mgmt event raised when a connection attempt times out

    NET\_EVENT\_CONN\_IF\_FATAL\_ERROR
    :   net\_mgmt event raised when a non-recoverable connectivity error occurs on an iface

    CONN\_MGR\_IF\_NO\_TIMEOUT
    :   Value to use with [conn\_mgr\_if\_set\_timeout](#group__conn__mgr__connectivity_1ga467ecbb330d21b8dfea3e0ce08448400) and [conn\_mgr\_conn\_binding::timeout](implementation.md#structconn__mgr__conn__binding_1a8474461cf7b00132441227aae07511ab) to indicate no timeout.

    Enums

    enum conn\_mgr\_if\_flag
    :   Per-iface connectivity flags.

        *Values:*

        enumerator CONN\_MGR\_IF\_PERSISTENT
        :   Persistent.

            When set, indicates that the connectivity implementation bound to this iface should attempt to persist connectivity by automatically reconnecting after connection loss.

        enumerator CONN\_MGR\_IF\_NO\_AUTO\_CONNECT
        :   No auto-connect.

            When set, conn\_mgr will not automatically attempt to connect this iface when it reaches admin-up.

        enumerator CONN\_MGR\_IF\_NO\_AUTO\_DOWN
        :   No auto-down.

            When set, conn\_mgr will not automatically take the iface admin-down when it stops trying to connect, even if CONFIG\_NET\_CONNECTION\_MANAGER\_AUTO\_IF\_DOWN is enabled.

    Functions

    int conn\_mgr\_if\_connect(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface)
    :   Connect interface.

        If the provided iface has been bound to a connectivity implementation, initiate network connect/association.

        Automatically takes the iface admin-up (by calling [net\_if\_up](../api/net_if.md#group__net__if_1ga02644cc623fc7a8878c17d54984e4210)) if it isn’t already.

        Non-Blocking.

        Parameters:
        :   - **iface** – Pointer to network interface

        Return values:
        :   - **0** – on success.
            - **-ESHUTDOWN** – if the iface is not admin-up.
            - **-ENOTSUP** – if the iface does not have a connectivity implementation.
            - **implementation-specific** – status code otherwise.

    int conn\_mgr\_if\_disconnect(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface)
    :   Disconnect interface.

        If the provided iface has been bound to a connectivity implementation, disconnect/disassociate it from the network, and cancel any pending attempts to connect/associate.

        Does nothing if the iface is currently admin-down.

        Parameters:
        :   - **iface** – Pointer to network interface

        Return values:
        :   - **0** – on success.
            - **-ENOTSUP** – if the iface does not have a connectivity implementation.
            - **implementation-specific** – status code otherwise.

    bool conn\_mgr\_if\_is\_bound(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface)
    :   Check whether the provided network interface supports connectivity / has been bound to a connectivity implementation.

        Parameters:
        :   - **iface** – Pointer to the iface to check.

        Return values:
        :   - **true** – if connectivity is supported (a connectivity implementation has been bound).
            - **false** – otherwise.

    int conn\_mgr\_if\_set\_opt(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface, int optname, const void \*optval, size\_t optlen)
    :   Set implementation-specific connectivity options.

        If the provided iface has been bound to a connectivity implementation that supports it, implementation-specific connectivity options related to the iface.

        Parameters:
        :   - **iface** – Pointer to the network interface.
            - **optname** – Integer value representing the option to set. The meaning of values is up to the [conn\_mgr\_conn\_api](implementation.md#structconn__mgr__conn__api) implementation. Some settings may affect multiple ifaces.
            - **optval** – Pointer to the value to be assigned to the option.
            - **optlen** – Length (in bytes) of the value to be assigned to the option.

        Return values:
        :   - **0** – if successful.
            - **-ENOTSUP** – if conn\_mgr\_if\_set\_opt not implemented by the iface.
            - **-ENOBUFS** – if optlen is too long.
            - **-EINVAL** – if NULL optval pointer provided.
            - **-ENOPROTOOPT** – if the optname is not recognized.
            - **implementation-specific** – error code otherwise.

    int conn\_mgr\_if\_get\_opt(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface, int optname, void \*optval, size\_t \*optlen)
    :   Get implementation-specific connectivity options.

        If the provided iface has been bound to a connectivity implementation that supports it, retrieves implementation-specific connectivity options related to the iface.

        optlen will always be set to the total number of bytes written, regardless of whether an error is returned, even if zero bytes were written.

        Parameters:
        :   - **iface** – Pointer to the network interface.
            - **optname** – Integer value representing the option to set. The meaning of values is up to the [conn\_mgr\_conn\_api](implementation.md#structconn__mgr__conn__api) implementation. Some settings may be shared by multiple ifaces.
            - **optval** – Pointer to where the retrieved value should be stored.
            - **optlen** – Pointer to length (in bytes) of the destination buffer available for storing the retrieved value. If the available space is less than what is needed, -ENOBUFS is returned. If the available space is invalid, -EINVAL is returned.

        Return values:
        :   - **0** – if successful.
            - **-ENOTSUP** – if conn\_mgr\_if\_get\_opt is not implemented by the iface.
            - **-ENOBUFS** – if retrieval buffer is too small.
            - **-EINVAL** – if invalid retrieval buffer length is provided, or if NULL optval or optlen pointer provided.
            - **-ENOPROTOOPT** – if the optname is not recognized.
            - **implementation-specific** – error code otherwise.

    bool conn\_mgr\_if\_get\_flag(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface, enum [conn\_mgr\_if\_flag](#c.conn_mgr_if_flag) flag)
    :   Check the value of connectivity flags.

        If the provided iface is bound to a connectivity implementation, retrieves the value of the specified connectivity flag associated with that iface.

        Parameters:
        :   - **iface** – - Pointer to the network interface to check.
            - **flag** – - The flag to check.

        Returns:
        :   True if the flag is set, otherwise False. Also returns False if the provided iface is not bound to a connectivity implementation, or the requested flag doesn’t exist.

    int conn\_mgr\_if\_set\_flag(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface, enum [conn\_mgr\_if\_flag](#c.conn_mgr_if_flag) flag, bool value)
    :   Set the value of a connectivity flags.

        If the provided iface is bound to a connectivity implementation, sets the value of the specified connectivity flag associated with that iface.

        Parameters:
        :   - **iface** – - Pointer to the network interface to modify.
            - **flag** – - The flag to set.
            - **value** – - Whether the flag should be enabled or disabled.

        Return values:
        :   - **0** – on success.
            - **-EINVAL** – if the flag does not exist.
            - **-ENOTSUP** – if the provided iface is not bound to a connectivity implementation.

    int conn\_mgr\_if\_get\_timeout(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface)
    :   Get the connectivity timeout for an iface.

        If the provided iface is bound to a connectivity implementation, retrieves the timeout setting in seconds for it.

        Parameters:
        :   - **iface** – - Pointer to the iface to check.

        Returns:
        :   int - The connectivity timeout value (in seconds) if it could be retrieved, otherwise CONN\_MGR\_IF\_NO\_TIMEOUT.

    int conn\_mgr\_if\_set\_timeout(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface, int timeout)
    :   Set the connectivity timeout for an iface.

        If the provided iface is bound to a connectivity implementation, sets the timeout setting in seconds for it.

        Parameters:
        :   - **iface** – - Pointer to the network interface to modify.
            - **timeout** – - The timeout value to set (in seconds). Pass [CONN\_MGR\_IF\_NO\_TIMEOUT](#group__conn__mgr__connectivity_1ga605eee24f4419b5cd6a50a0272979da7) to disable the timeout.

        Return values:
        :   - **0** – on success.
            - **-ENOTSUP** – if the provided iface is not bound to a connectivity implementation.

### Bulk API

Connectivity control provides several bulk functions allowing all ifaces to be controlled at once.

You can restrict these functions to operate only on non-[ignored](#conn-mgr-monitoring-ignoring-ifaces) ifaces if desired.

Include header file `include/zephyr/net/conn_mgr_connectivity.h` to access these.

*group* Connection Manager Connectivity Bulk API
:   Connection Manager Bulk API.

    Functions

    int conn\_mgr\_all\_if\_up(bool skip\_ignored)
    :   Convenience function that takes all available ifaces into the admin-up state.

        Essentially a wrapper for [net\_if\_up](../api/net_if.md#group__net__if_1ga02644cc623fc7a8878c17d54984e4210).

        Parameters:
        :   - **skip\_ignored** – - If true, only affect ifaces that aren’t ignored by conn\_mgr. Otherwise, affect all ifaces.

        Returns:
        :   0 if all net\_if\_up calls returned 0, otherwise the first nonzero value returned by a net\_if\_up call.

    int conn\_mgr\_all\_if\_down(bool skip\_ignored)
    :   Convenience function that takes all available ifaces into the admin-down state.

        Essentially a wrapper for [net\_if\_down](../api/net_if.md#group__net__if_1ga2187650062d6139b9f4b81745a206803).

        Parameters:
        :   - **skip\_ignored** – - If true, only affect ifaces that aren’t ignored by conn\_mgr. Otherwise, affect all ifaces.

        Returns:
        :   0 if all net\_if\_down calls returned 0, otherwise the first nonzero value returned by a net\_if\_down call.

    int conn\_mgr\_all\_if\_connect(bool skip\_ignored)
    :   Convenience function that takes all available ifaces into the admin-up state, and connects those that support connectivity.

        Essentially a wrapper for [net\_if\_up](../api/net_if.md#group__net__if_1ga02644cc623fc7a8878c17d54984e4210) and [conn\_mgr\_if\_connect](#group__conn__mgr__connectivity_1ga575d367c95592fd9f4ead694ff94543f).

        Parameters:
        :   - **skip\_ignored** – - If true, only affect ifaces that aren’t ignored by conn\_mgr. Otherwise, affect all ifaces.

        Returns:
        :   0 if all net\_if\_up and conn\_mgr\_if\_connect calls returned 0, otherwise the first nonzero value returned by either net\_if\_up or conn\_mgr\_if\_connect.

    int conn\_mgr\_all\_if\_disconnect(bool skip\_ignored)
    :   Convenience function that disconnects all available ifaces that support connectivity without putting them into admin-down state (unless auto-down is enabled for the iface).

        Essentially a wrapper for [net\_if\_down](../api/net_if.md#group__net__if_1ga2187650062d6139b9f4b81745a206803).

        Parameters:
        :   - **skip\_ignored** – - If true, only affect ifaces that aren’t ignored by conn\_mgr. Otherwise, affect all ifaces.

        Returns:
        :   0 if all net\_if\_up and conn\_mgr\_if\_connect calls returned 0, otherwise the first nonzero value returned by either net\_if\_up or conn\_mgr\_if\_connect.
