---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/conn_mgr/implementation.html
original_path: connectivity/networking/conn_mgr/implementation.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Connectivity Implementations

## Overview

Connectivity implementations are technology-specific modules that allow specific Zephyr ifaces to support [Connectivity Control](main.md#conn-mgr-control).
They are responsible for translating generic [connectivity control API](main.md#conn-mgr-control-api) calls into hardware-specific operations.
They are also responsible for implementing standardized [persistence and timeout](main.md#conn-mgr-control-persistence-timeouts) behaviors.

See the [implementation guidelines](#conn-mgr-impl-guidelines) for details on writing conformant connectivity implementations.

## Architecture

The [implementation API](#conn-mgr-impl-api) allows connectivity implementations to be [defined](#conn-mgr-impl-defining) at build time using [`CONN_MGR_CONN_DEFINE`](#c.CONN_MGR_CONN_DEFINE).

This creates a static instance of the [`conn_mgr_conn_impl`](#c.conn_mgr_conn_impl) struct, which then stores a reference to the passed in [`conn_mgr_conn_api`](#c.conn_mgr_conn_api) struct (which should be populated with implementation callbacks).

Once defined, you can reference implementations by name and bind them to any unbound iface using [`CONN_MGR_BIND_CONN`](#c.CONN_MGR_BIND_CONN).
Make sure not to accidentally bind two connectivity implementations to a single iface.

Once the iface is bound, [connectivity control API](main.md#conn-mgr-control-api) functions can be called on the iface, and they will be translated to the corresponding implementation functions in [`conn_mgr_conn_api`](#c.conn_mgr_conn_api).

Binding an iface does not directly modify its [`iface struct`](../api/net_if.md#c.net_if "net_if").

Instead, an instance of [`conn_mgr_conn_binding`](#c.conn_mgr_conn_binding) is created and appended an internal [iterable section](../../../kernel/iterable_sections/index.md#iterable-sections-api).

This binding structure will contain a reference to the bound iface, the connectivity implementation it is bound to, as well as a pointer to a per-iface [context pointer](#conn-mgr-impl-ctx).

This iterable section can then be iterated over to find out what (if any) connectivity implementation has been bound to a given iface.
This search process is used by most of the functions in the [connectivity control API](main.md#conn-mgr-control-api).
As such, these functions should be called sparingly, due to their relatively high search cost.

A single connectivity implementation may be bound to multiple ifaces.
See [Do not instance implementations](#conn-mgr-impl-guidelines-no-instancing) for more details.

![A detailed view of how Connection Manager integrates with Zephyr and the application.](../../../_images/integration_diagram_detailed.svg)

A detailed view of how Connection Manager integrates with Zephyr and the application.

See [here](main.md#conn-mgr-integration-diagram-simple) for a simplified version.

## Context Pointer

Since a single connectivity implementation may be shared by several Zephyr ifaces, each binding instantiates a context container (of [configurable type](#conn-mgr-impl-declaring)) unique to that binding.
Each binding is then instantiated with a reference to that container, which implementations can then use to access per-iface state information.

See also [Do not access bindings without locking them](#conn-mgr-impl-guidelines-binding-access) and [Do not instance implementations](#conn-mgr-impl-guidelines-no-instancing).

## Defining an implementation

A connectivity implementation may be defined as follows:

```c
/* Create the API implementation functions */
int my_connect_impl(struct conn_mgr_conn_binding *const binding) {
        /* Cause your underlying technology to associate */
}
int my_disconnect_impl(struct conn_mgr_conn_binding *const binding) {
        /* Cause your underlying technology to disassociate */
}
void my_init_impl(struct conn_mgr_conn_binding *const binding) {
        /* Perform any required initialization for your underlying technology */
}

/* Declare the API struct */
static struct conn_mgr_conn_api my_impl_api = {
        .connect = my_connect_impl,
        .disconnect = my_disconnect_impl,
        .init = my_init_impl,
        /* ... so on */
};

/* Define the implementation (named MY_CONNECTIVITY_IMPL) */
CONN_MGR_CONN_DEFINE(MY_CONNECTIVITY_IMPL, &my_impl_api);
```

Note

This does not work unless you also [declare the context pointer type](#conn-mgr-impl-declaring-ctx).

## Declaring an implementation publicly

Once defined, you can make a connectivity implementation available to other compilation units by declaring it (in a header file) as follows:

`my_connectivity_header.h`

```c
CONN_MGR_CONN_DECLARE_PUBLIC(MY_CONNECTIVITY_IMPL);
```

The header file that contains this declaration must be included in any compilation units that need to reference the implementation.

## Declaring a context type

For [`CONN_MGR_CONN_DEFINE`](#c.CONN_MGR_CONN_DEFINE) to work, you must declare a corresponding context pointer type.
This is because all connectivity bindings contain a [Context Pointer](#conn-mgr-impl-ctx) of their associated context pointer type.

If you are using [`CONN_MGR_CONN_DECLARE_PUBLIC`](#c.CONN_MGR_CONN_DECLARE_PUBLIC), declare this type alongside the declaration:

`my_connectivity_impl.h`

```c
#define MY_CONNECTIVITY_IMPL_CTX_TYPE struct my_context_type *
CONN_MGR_CONN_DECLARE_PUBLIC(MY_CONNECTIVITY_IMPL);
```

Then, make sure to include the header file before calling [`CONN_MGR_CONN_DEFINE`](#c.CONN_MGR_CONN_DEFINE):

`my_connectivity_impl.c`

```c
#include "my_connectivity_impl.h"

CONN_MGR_CONN_DEFINE(MY_CONNECTIVITY_IMPL, &my_impl_api);
```

Otherwise, it is sufficient to simply declare the context pointer type immediately before the call to [`CONN_MGR_CONN_DEFINE`](#c.CONN_MGR_CONN_DEFINE):

```c
#define MY_CONNECTIVITY_IMPL_CTX_TYPE struct my_context_type *
CONN_MGR_CONN_DEFINE(MY_CONNECTIVITY_IMPL, &my_impl_api);
```

Note

Naming is important.
Your context pointer type declaration must use the same name as your implementation declaration, but with `_CTX_TYPE` appended.

In the previous example, the context type is named `MY_CONNECTIVITY_IMPL_CTX_TYPE`, because `MY_CONNECTIVITY_IMPL` was used as the connectivity implementation name.

If your connectivity implementation does not need a context pointer, simply declare the type as void:

```c
#define MY_CONNECTIVITY_IMPL_CTX_TYPE void *
```

## Binding an iface to an implementation

A defined connectivity implementation may be bound to an iface by calling [`CONN_MGR_BIND_CONN`](#c.CONN_MGR_BIND_CONN) anywhere after the iface’s device definition:

```c
/* Define an iface */
NET_DEVICE_INIT(my_iface,
        /* ... the specifics here don't matter ... */
);

/* Now bind MY_CONNECTIVITY_IMPL to that iface --
 * the name used should match with the above
 */
CONN_MGR_BIND_CONN(my_iface, MY_CONNECTIVITY_IMPL);
```

## Connectivity implementation guidelines

Rather than implement all features centrally, Connection Manager relies on each connectivity implementation to implement many behaviors and features individually.

This approach allows Connection Manager to remain lean, and allows each connectivity implementation to choose the most appropriate approach to these behaviors for itself.
However, it relies on trust that all connectivity implementations will faithfully implement the features that have been delegated to them.

To maintain consistency between all connectivity implementations, observe the following guidelines when writing your own implementation:

### *Completely implement timeout and persistence*

All connectivity implementations must offer complete support for [timeout and persistence](main.md#conn-mgr-control-persistence-timeouts), such that a user can disable or enable these features, regardless of the inherent behavior of the underlying technology.
In other words, no matter how the underlying technology behaves, your implementation must make it appear to the end user to behave exactly as specified in the [Timeouts and Persistence](main.md#conn-mgr-control-persistence-timeouts) section.

See [Implementing timeouts and persistence](#conn-mgr-impl-timeout-persistence) for a detailed technical discussion on implementing timeouts and persistence.

### *Conform to API specifications*

Each [`implementation API function`](#c.conn_mgr_conn_api) you implement should behave as-described in the corresponding connectivity control API function.

For example, your implementation of [`conn_mgr_conn_api.connect`](#c.conn_mgr_conn_api.connect) should conform to the behavior described for [`conn_mgr_if_connect()`](main.md#c.conn_mgr_if_connect "conn_mgr_if_connect").

### *Allow connectivity pre-configuration*

Connectivity implementations should provide means for applications to pre-configure all necessary connection parameters (for example, network SSID, or PSK, if applicable), before the call to [`conn_mgr_if_connect()`](main.md#c.conn_mgr_if_connect "conn_mgr_if_connect").
It should not be necessary to provide this information as part of, or following the [`conn_mgr_if_connect()`](main.md#c.conn_mgr_if_connect "conn_mgr_if_connect") call, although implementations [should await this information if it is not provided](#conn-mgr-impl-guidelines-await-config).

### *Await valid connectivity configuration*

If network association fails because the application pre-configured invalid connection parameters, or did not configure connection parameters at all, this should be treated as a network failure.

In other words, the connectivity implementation should not give up on the connection attempt, even if valid connection parameters have not been configured.

Instead, the connectivity implementation should asynchronously wait for valid connection parameters to be configured, either indefinitely, or until the configured [connectivity timeout](main.md#conn-mgr-control-timeouts) elapses.

### *Implement iface state reporting*

All connectivity implementations must keep bound iface state up to date.

To be specific:

- Set the iface to dormant, carrier-down, or both during [`binding init`](#c.conn_mgr_conn_api.init).

  - See [Network interface state management](../api/net_if.md#net-if-interface-state-management) for details regarding iface carrier and dormant states.
- Update dormancy and carrier state so that the iface is non-dormant and carrier-up whenever (and only when) association is complete and connectivity is ready.
- Set the iface either to dormant or to carrier-down as soon as interruption of service is detected.

  - It is acceptable to gate this behind a small timeout (separate from the connection timeout) for network technologies where service is commonly intermittent.
- If the technology also handles IP assignment, ensure those IP addresses are [assigned to the iface](../api/net_if.md#net-if-interface-ip-management).

Note

iface state updates do not necessarily need to be performed directly by connectivity implementations.

For instance:

- IP assignment is not necessary if [DHCP](../api/dhcpv4.md#dhcpv4-interface) is used for the iface.
- The connectivity implementation does not need to update iface dormancy if the underlying [L2 implementation](../api/net_l2.md#net-l2-interface) already does so.

### *Do not use iface state as implementation state*

Zephyr ifaces may be accessed from other threads without respecting the binding mutex.
As such, Zephyr iface state may change unpredictably during connectivity implementation callbacks.

Therefore, do not base implementation behaviors on iface state.

Keep iface state updated to reflect network availability, but do not read iface state for any purpose.

If you need to keep track of dormancy or IP assignment, use a separate state variable stored in the [context pointer](#conn-mgr-impl-ctx).

### *Remain non-interferent*

Connectivity implementations should not prevent applications from interacting directly with associated technology-specific APIs.

In other words, it should be possible for an application to directly use your underlying technology without breaking your connectivity implementation.

If exceptions to this are absolutely necessary, they should be constrained to specific API calls and should be documented.

Note

While connectivity implementations must not break, it is acceptable for implementations to have potentially unexpected behavior if applications attempt to directly control the association state.

For instance, if an application directly instructs an underlying technology to disassociate, it would be acceptable for the connectivity implementation to interpret this as an unexpected connection loss and immediately attempt to re-associate.

### *Remain non-blocking*

All connectivity implementation callbacks should be non-blocking.

For instance, calls to [`conn_mgr_conn_api.connect`](#c.conn_mgr_conn_api.connect) should initiate a connection process and return immediately.

One exception is [`conn_mgr_conn_api.init`](#c.conn_mgr_conn_api.init), whose implementations are permitted to block.

However, bear in mind that blocking during this callback will delay system init, so still consider offloading time-consuming tasks to a background thread.

### *Make API immediately ready*

Connectivity implementations must be ready to receive API calls immediately after [`conn_mgr_conn_api.init`](#c.conn_mgr_conn_api.init).

For instance, a call to [`conn_mgr_conn_api.connect`](#c.conn_mgr_conn_api.connect) must eventually lead to an association attempt, even if called immediately after [`conn_mgr_conn_api.init`](#c.conn_mgr_conn_api.init).

If the underlying technology cannot be made ready for connect commands immediately when [`conn_mgr_conn_api.init`](#c.conn_mgr_conn_api.init) is called, calls to [`conn_mgr_conn_api.connect`](#c.conn_mgr_conn_api.connect) must be queued in a non-blocking fashion, and then executed later when ready.

### *Do not store state information outside the context pointer*

Connection Manager provides a context pointer to each binding.

Connectivity implementations should store all state information in this context pointer.

The only exception is connectivity implementations that are meant to be bound to only a single iface.
Such implementations may use statically declared state instead.

See also [Do not instance implementations](#conn-mgr-impl-guidelines-no-instancing).

### *Access ifaces only through binding structs*

Do not use statically declared ifaces or externally acquire references to ifaces.

For example, do not use [`net_if_get_default()`](../api/net_if.md#c.net_if_get_default "net_if_get_default") under the assumption that the bound iface will be the default iface.

Instead, always use the [`iface pointer`](#c.conn_mgr_conn_binding.iface) provided by the relevant [`binding struct`](#c.conn_mgr_conn_binding).
See also [Do not access bindings without locking them](#conn-mgr-impl-guidelines-binding-access).

### *Make implementations optional at compile-time*

Connectivity implementations should provide a Kconfig option to enable or disable the implementation without affecting bound iface availability.

In other words, it should be possible to configure builds that include Connectivity Manager, as well as the iface that would have been bound to the implementation, but not the implementation itself, nor its binding.

### *Do not instance implementations*

Do not declare a separate connectivity implementation for every iface you are going to bind to.

Instead, bind one global connectivity implementation to all of your ifaces, and use the context pointer to store state relevant to individual ifaces.

See also [Do not access bindings without locking them](#conn-mgr-impl-guidelines-binding-access) and [Access ifaces only through binding structs](#conn-mgr-impl-guidelines-iface-access).

### *Do not access bindings without locking them*

Bindings may be accessed and modified at random by multiple threads, so modifying or reading from a binding without first [`locking it`](#c.conn_mgr_binding_lock) may lead to unpredictable behavior.

This applies to all descendents of the binding, including anything in the [context container](#conn-mgr-impl-ctx).

Make sure to [`unlock`](#c.conn_mgr_binding_unlock) the binding when you are done accessing it.

Note

A possible exception to this rule is if the resource in question is inherently thread-safe.

However, be careful taking advantage of this exception.
It may still be possible to create a race condition, for instance when accessing multiple thread-safe resources simultaneously.

Therefore, it is recommended to simply always lock the binding, whether or not the resource being accessed is inherently thread-safe.

### *Do not disable built-in features*

Do not attempt to prevent the use of built-in features (such as [Timeouts and Persistence](main.md#conn-mgr-control-persistence-timeouts) or [Automated behaviors](main.md#conn-mgr-control-automations)).

All connectivity implementations must fully support these features.
Implementations must not attempt to force certain features to be always enabled or always disabled.

### *Trigger connectivity control events*

Connectivity control [network management](../api/net_mgmt.md#net-mgmt-interface) events are not triggered automatically by Connection Manager.

Connectivity implementations must trigger these events themselves.

Trigger [`NET_EVENT_CONN_CMD_IF_TIMEOUT`](main.md#c.net_event_conn_cmd.NET_EVENT_CONN_CMD_IF_TIMEOUT "NET_EVENT_CONN_CMD_IF_TIMEOUT") when a connection [timeout](main.md#conn-mgr-control-timeouts) occurs.
See [Timeout](main.md#conn-mgr-control-events-timeout) for details.

Trigger [`NET_EVENT_CONN_IF_FATAL_ERROR`](main.md#c.NET_EVENT_CONN_IF_FATAL_ERROR "NET_EVENT_CONN_IF_FATAL_ERROR") when a fatal (non-recoverable) connection error occurs.
See [Fatal Error](main.md#conn-mgr-control-events-fatal-error) for details.

See [Network Management](../api/net_mgmt.md#net-mgmt-interface) for details on firing network management events.

## Implementing timeouts and persistence

First, see [Timeouts and Persistence](main.md#conn-mgr-control-persistence-timeouts) for a high-level description of the expected behavior of timeouts and persistence.

Connectivity implementations must fully conform to that description, regardless of the behavior of the underlying connectivity technology.

Sometimes this means writing extra logic in the connectivity implementation to fake certain behaviors.
The following sections discuss various common edge-cases and nuances and how to handle them.

### *Inherently persistent technologies*

If the underlying technology automatically attempts to reconnect or retry connection after connection loss or failure, the connectivity implementation must manually cancel such attempts when they are in conflict with timeout or persistence settings.

For example:

> - If the underlying technology automatically attempts to reconnect after losing connection, and persistence is disabled for the iface, the connectivity implementation should immediately cancel this reconnection attempt.
> - If a connection attempt times out on an iface whose underlying technology does not have a built-in timeout, the connectivity implementation must simulate a timeout by cancelling the connection attempt manually.

### *Technologiess that give up on connection attempts*

If the underlying technology has no mechanism to retry connection attempts, or would give up on them before the user-configured timeout, or would not reconnect after connection loss, the connectivity implementation must manually re-request connection to counteract these deviances.

- If your underlying technology is not persistent, you must manually trigger reconnect attempts when persistence is enabled.
- If your underlying technology does not support a timeout, you must manually cancel connection attempts if the timeout is enabled.
- If your underlying technology forces a timeout, you must manually trigger a new connection attempts if that timeout is shorter than the Connection Manager timeout.

### *Technologies with association retry*

Many underlying technologies do not usually associate in a single attempt.

Instead, these underlying technologies may need to make multiple back-to-back association attempts in a row, usually with a small delay.

In these situations, the connectivity implementation should treat this series of back-to-back association sub-attempts as a single unified connection attempt.

For instance, after a sub-attempt failure, persistence being disabled should not prevent further sub-attempts, since they all count as one single overall connection attempt.
See also [Persistence during connection attempts](#conn-mgr-impl-tp-persistence-during-connect).

At which point a series of failed sub-attempts should be considered a failure of the connection attempt as a whole is up to each implementation to decide.

If the connection attempt crosses this threshold, but the configured timeout has not yet elapsed, or there is no timeout, sub-attempts should continue.

### *Persistence during connection attempts*

Persistence should not affect any aspect of implementation behavior during a connection attempt.
Persistence should only affect whether or not connection attempts are automatically triggered after a connection loss.

The configured timeout should fully determine whether connection retry should be performed.

## Implementation API

Include header file `include/zephyr/net/conn_mgr_connectivity_impl.h` to access these.

Only for use by connectivity implementations.

*group* conn\_mgr\_connectivity\_impl
:   Connection Manager Connectivity Implementation API.

    Defines

    CONN\_MGR\_CONN\_DEFINE(conn\_id, conn\_api)
    :   Define a conn\_mgr connectivity implementation that can be bound to network devices.

        Parameters:
        :   - **conn\_id** – The name of the new connectivity implementation
            - **conn\_api** – A pointer to a [conn\_mgr\_conn\_api](#structconn__mgr__conn__api) struct

    CONN\_MGR\_CONN\_DECLARE\_PUBLIC(conn\_id)
    :   Helper macro to make a conn\_mgr connectivity implementation publicly available.

    CONN\_MGR\_BIND\_CONN\_INST(dev\_id, inst, conn\_id)
    :   Associate a connectivity implementation with an existing network device instance.

        Parameters:
        :   - **dev\_id** – Network device id.
            - **inst** – Network device instance.
            - **conn\_id** – Name of the connectivity implementation to associate.

    CONN\_MGR\_BIND\_CONN(dev\_id, conn\_id)
    :   Associate a connectivity implementation with an existing network device.

        Parameters:
        :   - **dev\_id** – Network device id.
            - **conn\_id** – Name of the connectivity implementation to associate.

    Functions

    static inline struct [conn\_mgr\_conn\_binding](#c.conn_mgr_conn_binding) \*conn\_mgr\_if\_get\_binding(struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface)
    :   Retrieves the conn\_mgr binding struct for a provided iface if it exists.

        Bindings for connectivity implementations with missing API structs are ignored.

        For use only by connectivity implementations.

        Parameters:
        :   - **iface** – - bound network interface to obtain the binding struct for.

        Returns:
        :   struct conn\_mgr\_conn\_binding\* Pointer to the retrieved binding struct if it exists, NULL otherwise.

    static inline void conn\_mgr\_binding\_lock(struct [conn\_mgr\_conn\_binding](#c.conn_mgr_conn_binding) \*binding)
    :   Lock the passed-in binding, making it safe to access.

        Call this whenever accessing binding data, unless inside a [conn\_mgr\_conn\_api](#structconn__mgr__conn__api) callback, where it is called automatically by conn\_mgr.

        Reentrant.

        For use only by connectivity implementations.

        Parameters:
        :   - **binding** – - Binding to lock

    static inline void conn\_mgr\_binding\_unlock(struct [conn\_mgr\_conn\_binding](#c.conn_mgr_conn_binding) \*binding)
    :   Unlocks the passed-in binding.

        Call this after any call to [conn\_mgr\_binding\_lock](#group__conn__mgr__connectivity__impl_1ga27be6dec40356facce7da18a31a2c12a) once done accessing binding data.

        Reentrant.

        For use only by connectivity implementations.

        Parameters:
        :   - **binding** – - Binding to unlock

    static inline void conn\_mgr\_binding\_set\_flag(struct [conn\_mgr\_conn\_binding](#c.conn_mgr_conn_binding) \*binding, enum [conn\_mgr\_if\_flag](main.md#c.conn_mgr_if_flag "conn_mgr_if_flag") flag, bool value)
    :   Set the value of the specified connectivity flag for the provided binding.

        Can be used from any thread or callback without calling [conn\_mgr\_binding\_lock](#group__conn__mgr__connectivity__impl_1ga27be6dec40356facce7da18a31a2c12a).

        For use only by connectivity implementations

        Parameters:
        :   - **binding** – The binding to check
            - **flag** – The flag to check
            - **value** – New value for the specified flag

    static inline bool conn\_mgr\_binding\_get\_flag(struct [conn\_mgr\_conn\_binding](#c.conn_mgr_conn_binding) \*binding, enum [conn\_mgr\_if\_flag](main.md#c.conn_mgr_if_flag "conn_mgr_if_flag") flag)
    :   Check the value of the specified connectivity flag for the provided binding.

        Can be used from any thread or callback without calling [conn\_mgr\_binding\_lock](#group__conn__mgr__connectivity__impl_1ga27be6dec40356facce7da18a31a2c12a).

        For use only by connectivity implementations

        Parameters:
        :   - **binding** – The binding to check
            - **flag** – The flag to check

        Returns:
        :   bool The value of the specified flag

    struct conn\_mgr\_conn\_api
    :   *#include <conn\_mgr\_connectivity\_impl.h>*

        Connectivity Manager Connectivity API structure.

        Used to provide generic access to network association parameters and procedures

        Public Members

        int (\*connect)(struct [conn\_mgr\_conn\_binding](#c.conn_mgr_conn_binding) \*const binding)
        :   When called, the connectivity implementation should start attempting to establish connectivity (association with a network) for the bound iface pointed to by if\_conn->iface.

            Must be non-blocking.

            Called by [conn\_mgr\_if\_connect](main.md#group__conn__mgr__connectivity_1ga575d367c95592fd9f4ead694ff94543f).

        int (\*disconnect)(struct [conn\_mgr\_conn\_binding](#c.conn_mgr_conn_binding) \*const binding)
        :   When called, the connectivity implementation should disconnect (dissasociate), or stop any in-progress attempts to associate to a network, the bound iface pointed to by if\_conn->iface.

            Must be non-blocking.

            Called by [conn\_mgr\_if\_disconnect](main.md#group__conn__mgr__connectivity_1gada2b5271b3e5dbcab629e1538b3d8eb4).

        void (\*init)(struct [conn\_mgr\_conn\_binding](#c.conn_mgr_conn_binding) \*const binding)
        :   Called once for each iface that has been bound to a connectivity implementation using this API.

            Connectivity implementations should use this callback to perform any required per-bound-iface initialization.

            Implementations may choose to gracefully handle invalid buffer lengths with partial writes, rather than raise errors, if deemed appropriate.

        int (\*set\_opt)(struct [conn\_mgr\_conn\_binding](#c.conn_mgr_conn_binding) \*const binding, int optname, const void \*optval, size\_t optlen)
        :   Implementation callback for conn\_mgr\_if\_set\_opt.

            Used to set implementation-specific connectivity settings.

            Calls to conn\_mgr\_if\_set\_opt on an iface will result in calls to this callback with the [conn\_mgr\_conn\_binding](#structconn__mgr__conn__binding) struct bound to that iface.

            It is up to the connectivity implementation to interpret optname. Options can be specific to the bound iface (pointed to by if\_conn->iface), or can apply to the whole connectivity implementation.

            See the description of conn\_mgr\_if\_set\_opt for more details. set\_opt implementations should conform to that description.

            Implementations may choose to gracefully handle invalid buffer lengths with partial reads, rather than raise errors, if deemed appropriate.

        int (\*get\_opt)(struct [conn\_mgr\_conn\_binding](#c.conn_mgr_conn_binding) \*const binding, int optname, void \*optval, size\_t \*optlen)
        :   Implementation callback for conn\_mgr\_if\_get\_opt.

            Used to retrieve implementation-specific connectivity settings.

            Calls to conn\_mgr\_if\_get\_opt on an iface will result in calls to this callback with the [conn\_mgr\_conn\_binding](#structconn__mgr__conn__binding) struct bound to that iface.

            It is up to the connectivity implementation to interpret optname. Options can be specific to the bound iface (pointed to by if\_conn->iface), or can apply to the whole connectivity implementation.

            See the description of conn\_mgr\_if\_get\_opt for more details. get\_opt implementations should conform to that description.

    struct conn\_mgr\_conn\_impl
    :   *#include <conn\_mgr\_connectivity\_impl.h>*

        Connectivity Implementation struct.

        Declares a conn\_mgr connectivity layer implementation with the provided API

        Public Members

        struct [conn\_mgr\_conn\_api](#c.conn_mgr_conn_api) \*api
        :   The connectivity API used by the implementation.

    struct conn\_mgr\_conn\_binding
    :   *#include <conn\_mgr\_connectivity\_impl.h>*

        Connectivity Manager network interface binding structure.

        Binds a conn\_mgr connectivity implementation to an iface / network device. Stores per-iface state for the connectivity implementation.

        Generic connectivity state

        uint32\_t flags
        :   Connectivity flags.

            Public boolean state and configuration values supported by all bindings. See [conn\_mgr\_if\_flag](main.md#group__conn__mgr__connectivity_1gaf10fb532a3dd07ec8c692a72643d0e3f) for options.

        int timeout
        :   Timeout (seconds).

            Indicates to the connectivity implementation how long it should attempt to establish connectivity for during a connection attempt before giving up.

            The connectivity implementation should give up on establishing connectivity after this timeout, even if persistence is enabled.

            Set to [CONN\_MGR\_IF\_NO\_TIMEOUT](main.md#group__conn__mgr__connectivity_1ga605eee24f4419b5cd6a50a0272979da7) to indicate that no timeout should be used.

        Public Members

        struct [net\_if](../api/net_if.md#c.net_if "net_if") \*iface
        :   The network interface the connectivity implementation is bound to.

        const struct [conn\_mgr\_conn\_impl](#c.conn_mgr_conn_impl) \*impl
        :   The connectivity implementation the network device is bound to.

        void \*ctx
        :   Pointer to private, per-iface connectivity context.
