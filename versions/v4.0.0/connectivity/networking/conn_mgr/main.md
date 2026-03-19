---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/conn_mgr/main.html
original_path: connectivity/networking/conn_mgr/main.html
---

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

  - This means the iface has been instructed to become operational-up (ready for use). This is done by a call to [`net_if_up()`](../../../doxygen/html/group__net__if.md#ga02644cc623fc7a8878c17d54984e4210).
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

When at least one iface is ready, the [`NET_EVENT_L4_CONNECTED`](../../../doxygen/html/group__net__mgmt.md#gacbd2b10cc345359c07de4a62eb172a09) [network management](../api/net_mgmt.md#net-mgmt-interface) event is triggered, and IP connectivity is said to be ready.

Afterwards, ifaces can become ready or unready without firing additional events, so long as there always remains at least one ready iface.

When there are no longer any ready ifaces left, the [`NET_EVENT_L4_DISCONNECTED`](../../../doxygen/html/group__net__mgmt.md#gacd9e0b5e2f540794b20f11b070ffbd65) [network management](../api/net_mgmt.md#net-mgmt-interface) event is triggered, and IP connectivity is said to be unready.

Note

Connection Manager also fires the following more specific `CONNECTED` / `DISCONNECTED` events:

- [`NET_EVENT_L4_IPV4_CONNECTED`](../../../doxygen/html/group__net__mgmt.md#ga532fdc2f199e047a5d17e325cee12cf1)
- [`NET_EVENT_L4_IPV4_DISCONNECTED`](../../../doxygen/html/group__net__mgmt.md#gaa92cc806d93446d548a05edb8e0074c2)
- [`NET_EVENT_L4_IPV6_CONNECTED`](../../../doxygen/html/group__net__mgmt.md#gaf6bb88ed90df5aacb40e42fcc5bfbcf5)
- [`NET_EVENT_L4_IPV6_DISCONNECTED`](../../../doxygen/html/group__net__mgmt.md#gac81abeab44fbf2b6f29d4e11a1e1bd17)

These are similar to [`NET_EVENT_L4_CONNECTED`](../../../doxygen/html/group__net__mgmt.md#gacbd2b10cc345359c07de4a62eb172a09) and [`NET_EVENT_L4_DISCONNECTED`](../../../doxygen/html/group__net__mgmt.md#gacd9e0b5e2f540794b20f11b070ffbd65), but specifically track whether IPv4- and IPv6-capable ifaces are ready.

## Usage

Connectivity monitoring is enabled if the [`CONFIG_NET_CONNECTION_MANAGER`](../../../kconfig.md#CONFIG_NET_CONNECTION_MANAGER "CONFIG_NET_CONNECTION_MANAGER") Kconfig option is enabled.

To receive connectivity updates, create and register a listener for the [`NET_EVENT_L4_CONNECTED`](../../../doxygen/html/group__net__mgmt.md#gacbd2b10cc345359c07de4a62eb172a09) and [`NET_EVENT_L4_DISCONNECTED`](../../../doxygen/html/group__net__mgmt.md#gacd9e0b5e2f540794b20f11b070ffbd65) [network management](../api/net_mgmt.md#net-mgmt-interface) events:

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

Connectivity monitoring initializes using the [`SYS_INIT`](../../../doxygen/html/group__sys__init.md#gaf507cc0613add8113c41896bd631254f) `APPLICATION` initialization priority specified by the [`CONFIG_NET_CONNECTION_MANAGER_MONITOR_PRIORITY`](../../../kconfig.md#CONFIG_NET_CONNECTION_MANAGER_MONITOR_PRIORITY "CONFIG_NET_CONNECTION_MANAGER_MONITOR_PRIORITY") Kconfig option.

You can register your callbacks before this initialization by using [`SYS_INIT`](../../../doxygen/html/group__sys__init.md#gaf507cc0613add8113c41896bd631254f) with an earlier initialization priority than this value, for instance priority 0:

```c
static int my_application_setup(void)
{
        /* Register callbacks here */
        return 0;
}

SYS_INIT(my_application_setup, APPLICATION, 0);
```

If this is not feasible, you can instead request that connectivity monitoring resend the latest connectivity events at any time by calling [`conn_mgr_mon_resend_status()`](../../../doxygen/html/group__conn__mgr.md#gacdde95f41f32e7a829d8cd3a6d0e2277):

```c
static void my_late_application_setup(void)
{
  /* Register callbacks here */

  /* Once done, request that events be re-triggered */
  conn_mgr_mon_resend_status();
}
```

## Ignoring ifaces

Applications can request that ifaces be ignored by Connection Manager by calling [`conn_mgr_ignore_iface()`](../../../doxygen/html/group__conn__mgr.md#ga7bad393c43a24df7a03176830b05b288) with the iface to be ignored.

Alternatively, an entire [L2 implementation](../api/net_l2.md#net-l2-interface) can be ignored by calling [`conn_mgr_ignore_l2()`](../../../doxygen/html/group__conn__mgr.md#ga6bd1ee46dc2e3dae554fce49e82c6187).

This has the effect of individually ignoring all the ifaces using that [L2 implementation](../api/net_l2.md#net-l2-interface).

While ignored, the iface is treated by Connection Manager as though it were unready for network traffic, no matter its actual state.

This may be useful, for instance, if your application has configured one or more ifaces that cannot (or for whatever reason should not) be used to contact the wider Internet.

[Bulk convenience functions](#conn-mgr-control-api-bulk) optionally skip ignored ifaces.

See [`conn_mgr_ignore_iface()`](../../../doxygen/html/group__conn__mgr.md#ga7bad393c43a24df7a03176830b05b288) and [`conn_mgr_watch_iface()`](../../../doxygen/html/group__conn__mgr.md#gacc8735b835dea9b31531fcca9fe8a979) for more details.

## Connectivity monitoring API

Include header file `include/zephyr/net/conn_mgr_monitoring.h` to access these.

[Connection Manager API](../../../doxygen/html/group__conn__mgr.md)

# Connectivity control

Many network interfaces require a network association procedure to be completed before being usable.

For such ifaces, connectivity control can provide a generic API to request network association ([`conn_mgr_if_connect()`](../../../doxygen/html/group__conn__mgr__connectivity.md#ga575d367c95592fd9f4ead694ff94543f)) and disassociation ([`conn_mgr_if_disconnect()`](../../../doxygen/html/group__conn__mgr__connectivity.md#gada2b5271b3e5dbcab629e1538b3d8eb4)).
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

Once an iface is bound, all connectivity commands passed to it (such as [`conn_mgr_if_connect()`](../../../doxygen/html/group__conn__mgr__connectivity.md#ga575d367c95592fd9f4ead694ff94543f) or [`conn_mgr_if_disconnect()`](../../../doxygen/html/group__conn__mgr__connectivity.md#gada2b5271b3e5dbcab629e1538b3d8eb4)) will be routed to the corresponding implementation function in the connectivity implementation.

Note

To avoid inconsistent behavior, all connectivity implementations must adhere to the [implementation guidelines](implementation.md#conn-mgr-impl-guidelines).

### Connecting

Once a bound iface is admin-up (see [Network interface state management](../api/net_if.md#net-if-interface-state-management)), [`conn_mgr_if_connect()`](../../../doxygen/html/group__conn__mgr__connectivity.md#ga575d367c95592fd9f4ead694ff94543f) can be called to cause it to associate with a network.

If association succeeds, the connectivity implementation will mark the iface as operational-up (see [Network interface state management](../api/net_if.md#net-if-interface-state-management)).

If association fails unrecoverably, the [fatal error event](#conn-mgr-control-events-fatal-error) will be triggered.

You can configure an optional [timeout](#conn-mgr-control-timeouts) for this process.

Note

The [`conn_mgr_if_connect()`](../../../doxygen/html/group__conn__mgr__connectivity.md#ga575d367c95592fd9f4ead694ff94543f) function is intentionally minimalistic, and does not take any kind of configuration.
Each connectivity implementation should provide a way to pre-configure or automatically configure any required association settings or credentials.
See [Allow connectivity pre-configuration](implementation.md#conn-mgr-impl-guidelines-preconfig) for details.

### Connection loss

If connectivity is lost due to external factors, the connectivity implementation will mark the iface as operational-down.

Depending on whether [persistence](#conn-mgr-control-persistence) is set, the iface may then attempt to reconnect.

### Manual disconnection

The application can also request that connectivity be intentionally abandoned by calling [`conn_mgr_if_disconnect()`](../../../doxygen/html/group__conn__mgr__connectivity.md#gada2b5271b3e5dbcab629e1538b3d8eb4).

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

When [`conn_mgr_if_connect()`](../../../doxygen/html/group__conn__mgr__connectivity.md#ga575d367c95592fd9f4ead694ff94543f) is called on an iface, a connection attempt begins.

The connection attempt continues indefinitely until it succeeds, unless a timeout has been specified for the iface (using [`conn_mgr_if_set_timeout()`](../../../doxygen/html/group__conn__mgr__connectivity.md#ga467ecbb330d21b8dfea3e0ce08448400)).

In that case, the connection attempt will be abandoned if the timeout elapses before it succeeds.
If this happens, the [timeout event](#conn-mgr-control-events-timeout) is raised.

### Connection Persistence

Each iface also has a connection persistence setting that you can enable or disable by setting the [`CONN_MGR_IF_PERSISTENT`](../../../doxygen/html/group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fa0edb461193b3486d06f75fd1da93746f) flag with [`conn_mgr_binding_set_flag()`](../../../doxygen/html/group__conn__mgr__connectivity__impl.md#ga4f0f3244f48c5e0204faf8278c2bd94f).

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

The [`NET_EVENT_CONN_IF_FATAL_ERROR`](../../../doxygen/html/group__conn__mgr__connectivity.md#gae8f207559a7123bd2eca5ef08086d377) event is raised when an iface encounters an error from which it cannot recover (meaning any subsequent attempts to associate are guaranteed to fail, and all such attempts should be abandoned).

Handlers of this event will be passed a pointer to the iface for which the fatal error occurred.
Individual connectivity implementations may also pass an application-specific data pointer.

### Timeout

The [`NET_EVENT_CONN_IF_TIMEOUT`](../../../doxygen/html/group__conn__mgr__connectivity.md#ga5ea6e37ca9eda2b6fd8b165b8182dd38) event is raised when an [iface association](#conn-mgr-control-operation-connecting) attempt [times out](#conn-mgr-control-timeouts).

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

Applications can disable this behavior by setting the [`NET_IF_NO_AUTO_START`](../../../doxygen/html/group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05) interface flag with [`net_if_flag_set()`](../../../doxygen/html/group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2).

Automatic connect

By default, Connection Manager will automatically connect any [bound](implementation.md#conn-mgr-impl-binding) iface that becomes admin-up.

Applications can disable this by setting the [`CONN_MGR_IF_NO_AUTO_CONNECT`](../../../doxygen/html/group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fadaf5c01734a04f70f3caf5c841c936dd) connectivity flag with [`conn_mgr_if_set_flag()`](../../../doxygen/html/group__conn__mgr__connectivity.md#gae86d1c808f31b8ca5e67bacbc844ef47).

Automatic admin-down

By default, Connection Manager will automatically take any bound iface admin-down if it has given up on associating.

Applications can disable this for all ifaces by disabling the [`CONFIG_NET_CONNECTION_MANAGER_AUTO_IF_DOWN`](../../../kconfig.md#CONFIG_NET_CONNECTION_MANAGER_AUTO_IF_DOWN "CONFIG_NET_CONNECTION_MANAGER_AUTO_IF_DOWN") Kconfig option, or for individual ifaces by setting the [`CONN_MGR_IF_NO_AUTO_DOWN`](../../../doxygen/html/group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fa2b65e55f411eef6b9805c9977097f86d) connectivity flag with [`conn_mgr_if_set_flag()`](../../../doxygen/html/group__conn__mgr__connectivity.md#gae86d1c808f31b8ca5e67bacbc844ef47).

## Connectivity control API

Include header file `include/zephyr/net/conn_mgr_connectivity.h` to access these.

[Connection Manager Connectivity API](../../../doxygen/html/group__conn__mgr__connectivity.md)

### Bulk API

Connectivity control provides several bulk functions allowing all ifaces to be controlled at once.

You can restrict these functions to operate only on non-[ignored](#conn-mgr-monitoring-ignoring-ifaces) ifaces if desired.

Include header file `include/zephyr/net/conn_mgr_connectivity.h` to access these.

[Connection Manager Connectivity Bulk API](../../../doxygen/html/group__conn__mgr__connectivity__bulk.md)
