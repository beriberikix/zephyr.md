---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/resource_management/index.html
original_path: services/resource_management/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Resource Management

There are various situations where it’s necessary to coordinate resource
use at runtime among multiple clients. These include power rails,
clocks, other peripherals, and binary device power management. The
complexity of properly managing multiple consumers of a device in a
multithreaded system, especially when transitions may be asynchronous,
suggests that a shared implementation is desirable.

Zephyr provides managers for several coordination policies. These
managers are embedded into services that use them for specific
functions.

## [On-Off Manager](#id1)

An on-off manager supports an arbitrary number of clients of a service
which has a binary state. Example applications are power rails, clocks,
and binary device power management.

The manager has the following properties:

- The stable states are off, on, and error. The service always begins
  in the off state. The service may also be in a transition to a given
  state.
- The core operations are request (add a dependency) and release (remove
  a dependency). Supporting operations are reset (to clear an error
  state) and cancel (to reclaim client data from an in-progress
  transition). The service manages the state based on calls to
  functions that initiate these operations.
- The service transitions from off to on when first client request is
  received.
- The service transitions from on to off when last client release is
  received.
- Each service configuration provides functions that implement the
  transition from off to on, from on to off, and optionally from an
  error state to off. Transitions must be invokable from both thread
  and interrupt context.
- The request and reset operations are asynchronous using
  [Asynchronous Notifications](../notify.md#async-notification). Both operations may be cancelled, but
  cancellation has no effect on the in-progress transition.
- Requests to turn on may be queued while a transition to off is in
  progress: when the service has turned off successfully it will be
  immediately turned on again (where context allows) and waiting clients
  notified when the start completes.

Requests are reference counted, but not tracked. That means clients are
responsible for recording whether their requests were accepted, and for
initiating a release only if they have previously successfully completed
a request. Improper use of the API can cause an active client to be
shut out, and the manager does not maintain a record of specific clients
that have been granted a request.

Failures in executing a transition are recorded and inhibit further
requests or releases until the manager is reset. Pending requests are
notified (and cancelled) when errors are discovered.

Transition operation completion notifications are provided through
[Asynchronous Notifications](../notify.md#async-notification).

Clients and other components interested in tracking all service state
changes, including when a service begins turning off or enters an error
state, can be informed of state transitions by registering a monitor
with onoff\_monitor\_register(). Notification of changes are provided
before issuing completion notifications associated with the new
state.

Note

A generic API may be implemented by multiple drivers where the common
case is asynchronous. The on-off client structure may be an
appropriate solution for the generic API. Where drivers that can
guarantee synchronous context-independent transitions a driver may
use [`onoff_sync_service`](#c.onoff_sync_service) and its supporting API rather than
[`onoff_manager`](#c.onoff_manager), with only a small reduction in functionality
(primarily no support for the monitor API).

*group* On-Off Service APIs
:   Defines

    ONOFF\_FLAG\_ERROR
    :   Flag indicating an error state.

        Error states are cleared using [onoff\_reset()](#group__resource__mgmt__onoff__apis_1gaf7b46a5f2e43d1bab193c18b8f6c8ba8).

    ONOFF\_STATE\_MASK
    :   Mask used to isolate bits defining the service state.

        Mask a value with this then test for ONOFF\_FLAG\_ERROR to determine whether the machine has an unfixed error, or compare against ONOFF\_STATE\_ON, ONOFF\_STATE\_OFF, ONOFF\_STATE\_TO\_ON, ONOFF\_STATE\_TO\_OFF, or ONOFF\_STATE\_RESETTING.

    ONOFF\_STATE\_OFF
    :   Value exposed by ONOFF\_STATE\_MASK when service is off.

    ONOFF\_STATE\_ON
    :   Value exposed by ONOFF\_STATE\_MASK when service is on.

    ONOFF\_STATE\_ERROR
    :   Value exposed by ONOFF\_STATE\_MASK when the service is in an error state (and not in the process of resetting its state).

    ONOFF\_STATE\_TO\_ON
    :   Value exposed by ONOFF\_STATE\_MASK when service is transitioning to on.

    ONOFF\_STATE\_TO\_OFF
    :   Value exposed by ONOFF\_STATE\_MASK when service is transitioning to off.

    ONOFF\_STATE\_RESETTING
    :   Value exposed by ONOFF\_STATE\_MASK when service is in the process of resetting.

    ONOFF\_TRANSITIONS\_INITIALIZER(\_start, \_stop, \_reset)
    :   Initializer for a [onoff\_transitions](#structonoff__transitions) object.

        Parameters:
        :   - **\_start** – a function used to transition from off to on state.
            - **\_stop** – a function used to transition from on to off state.
            - **\_reset** – a function used to clear errors and force the service to an off state. Can be null.

    ONOFF\_CLIENT\_EXTENSION\_POS
    :   Identify region of [sys\_notify](../notify.md#structsys__notify) flags available for containing services.

        Bits of the flags field of the [sys\_notify](../notify.md#structsys__notify) structure contained within the queued\_operation structure at and above this position may be used by extensions to the [onoff\_client](#structonoff__client) structure.

        These bits are intended for use by containing service implementations to record client-specific information and are subject to other conditions of use specified on the [sys\_notify](../notify.md#structsys__notify) API.

    Typedefs

    typedef void (\*onoff\_notify\_fn)(struct [onoff\_manager](#c.onoff_manager) \*mgr, int res)
    :   Signature used to notify an on-off manager that a transition has completed.

        Functions of this type are passed to service-specific transition functions to be used to report the completion of the operation. The functions may be invoked from any context.

        Param mgr:
        :   the manager for which transition was requested.

        Param res:
        :   the result of the transition. This shall be non-negative on success, or a negative error code. If an error is indicated the service shall enter an error state.

    typedef void (\*onoff\_transition\_fn)(struct [onoff\_manager](#c.onoff_manager) \*mgr, [onoff\_notify\_fn](#c.onoff_notify_fn) notify)
    :   Signature used by service implementations to effect a transition.

        Service definitions use two required function pointers of this type to be notified that a transition is required, and a third optional one to reset the service when it is in an error state.

        The start function will be called only from the off state.

        The stop function will be called only from the on state.

        The reset function (where supported) will be called only when [onoff\_has\_error()](#group__resource__mgmt__onoff__apis_1ga347efda0aa0305c134224c59677fa6cb) returns true.

        Note

        All transitions functions must be isr-ok.

        Param mgr:
        :   the manager for which transition was requested.

        Param notify:
        :   the function to be invoked when the transition has completed. If the transition is synchronous, notify shall be invoked by the implementation before the transition function returns. Otherwise the implementation shall capture this parameter and invoke it when the transition completes.

    typedef void (\*onoff\_client\_callback)(struct [onoff\_manager](#c.onoff_manager) \*mgr, struct [onoff\_client](#c.onoff_client) \*cli, uint32\_t state, int res)
    :   Signature used to notify an on-off service client of the completion of an operation.

        These functions may be invoked from any context including pre-kernel, ISR, or cooperative or pre-emptible threads. Compatible functions must be isr-ok and not sleep.

        Param mgr:
        :   the manager for which the operation was initiated. This may be null if the on-off service uses synchronous transitions.

        Param cli:
        :   the client structure passed to the function that initiated the operation.

        Param state:
        :   the state of the machine at the time of completion, restricted by ONOFF\_STATE\_MASK. ONOFF\_FLAG\_ERROR must be checked independently of whether res is negative as a machine error may indicate that all future operations except [onoff\_reset()](#group__resource__mgmt__onoff__apis_1gaf7b46a5f2e43d1bab193c18b8f6c8ba8) will fail.

        Param res:
        :   the result of the operation. Expected values are service-specific, but the value shall be non-negative if the operation succeeded, and negative if the operation failed. If res is negative ONOFF\_FLAG\_ERROR will be set in state, but if res is non-negative ONOFF\_FLAG\_ERROR may still be set in state.

    typedef void (\*onoff\_monitor\_callback)(struct [onoff\_manager](#c.onoff_manager) \*mgr, struct [onoff\_monitor](#c.onoff_monitor) \*mon, uint32\_t state, int res)
    :   Signature used to notify a monitor of an onoff service of errors or completion of a state transition.

        This is similar to [onoff\_client\_callback](#group__resource__mgmt__onoff__apis_1ga41b94526182c5772d7adebb1d1745068) but provides information about all transitions, not just ones associated with a specific client. Monitor callbacks are invoked before any completion notifications associated with the state change are made.

        These functions may be invoked from any context including pre-kernel, ISR, or cooperative or pre-emptible threads. Compatible functions must be isr-ok and not sleep.

        The callback is permitted to unregister itself from the manager, but must not register or unregister any other monitors.

        Param mgr:
        :   the manager for which a transition has completed.

        Param mon:
        :   the monitor instance through which this notification arrived.

        Param state:
        :   the state of the machine at the time of completion, restricted by ONOFF\_STATE\_MASK. All valid states may be observed.

        Param res:
        :   the result of the operation. Expected values are service- and state-specific, but the value shall be non-negative if the operation succeeded, and negative if the operation failed.

    Functions

    int onoff\_manager\_init(struct [onoff\_manager](#c.onoff_manager) \*mgr, const struct [onoff\_transitions](#c.onoff_transitions) \*transitions)
    :   Initialize an on-off service to off state.

        This function must be invoked exactly once per service instance, by the infrastructure that provides the service, and before any other on-off service API is invoked on the service.

        This function should never be invoked by clients of an on-off service.

        Parameters:
        :   - **mgr** – the manager definition object to be initialized.
            - **transitions** – pointer to a structure providing transition functions. The referenced object must persist as long as the manager can be referenced.

        Return values:
        :   - **0** – on success
            - **-EINVAL** – if start, stop, or flags are invalid

    static inline bool onoff\_has\_error(const struct [onoff\_manager](#c.onoff_manager) \*mgr)
    :   Test whether an on-off service has recorded an error.

        This function can be used to determine whether the service has recorded an error. Errors may be cleared by invoking [onoff\_reset()](#group__resource__mgmt__onoff__apis_1gaf7b46a5f2e43d1bab193c18b8f6c8ba8).

        This is an unlocked convenience function suitable for use only when it is known that no other process might invoke an operation that transitions the service between an error and non-error state.

        Returns:
        :   true if and only if the service has an uncleared error.

    int onoff\_request(struct [onoff\_manager](#c.onoff_manager) \*mgr, struct [onoff\_client](#c.onoff_client) \*cli)
    :   Request a reservation to use an on-off service.

        The return value indicates the success or failure of an attempt to initiate an operation to request the resource be made available. If initiation of the operation succeeds the result of the request operation is provided through the configured client notification method, possibly before this call returns.

        Note that the call to this function may succeed in a case where the actual request fails. Always check the operation completion result.

        Parameters:
        :   - **mgr** – the manager that will be used.
            - **cli** – a non-null pointer to client state providing instructions on synchronous expectations and how to notify the client when the request completes. Behavior is undefined if client passes a pointer object associated with an incomplete service operation.

        Return values:
        :   - **non-negative** – the observed state of the machine at the time the request was processed, if successful.
            - **-EIO** – if service has recorded an error.
            - **-EINVAL** – if the parameters are invalid.
            - **-EAGAIN** – if the reference count would overflow.

    int onoff\_release(struct [onoff\_manager](#c.onoff_manager) \*mgr)
    :   Release a reserved use of an on-off service.

        This synchronously releases the caller’s previous request. If the last request is released the manager will initiate a transition to off, which can be observed by registering an [onoff\_monitor](#structonoff__monitor).

        Note

        Behavior is undefined if this is not paired with a preceding [onoff\_request()](#group__resource__mgmt__onoff__apis_1ga20dcb358e405deb87b7fbb7846ef9d68) call that completed successfully.

        Parameters:
        :   - **mgr** – the manager for which a request was successful.

        Return values:
        :   - **non-negative** – the observed state (ONOFF\_STATE\_ON) of the machine at the time of the release, if the release succeeds.
            - **-EIO** – if service has recorded an error.
            - **-ENOTSUP** – if the machine is not in a state that permits release.

    int onoff\_cancel(struct [onoff\_manager](#c.onoff_manager) \*mgr, struct [onoff\_client](#c.onoff_client) \*cli)
    :   Attempt to cancel an in-progress client operation.

        It may be that a client has initiated an operation but needs to shut down before the operation has completed. For example, when a request was made and the need is no longer present.

        Cancelling is supported only for [onoff\_request()](#group__resource__mgmt__onoff__apis_1ga20dcb358e405deb87b7fbb7846ef9d68) and [onoff\_reset()](#group__resource__mgmt__onoff__apis_1gaf7b46a5f2e43d1bab193c18b8f6c8ba8) operations, and is a synchronous operation. Be aware that any transition that was initiated on behalf of the client will continue to progress to completion: it is only notification of transition completion that may be eliminated. If there are no active requests when a transition to on completes the manager will initiate a transition to off.

        Client notification does not occur for cancelled operations.

        Parameters:
        :   - **mgr** – the manager for which an operation is to be cancelled.
            - **cli** – a pointer to the same client state that was provided when the operation to be cancelled was issued.

        Return values:
        :   - **non-negative** – the observed state of the machine at the time of the cancellation, if the cancellation succeeds. On successful cancellation ownership of `*cli` reverts to the client.
            - **-EINVAL** – if the parameters are invalid.
            - **-EALREADY** – if cli was not a record of an uncompleted notification at the time the cancellation was processed. This likely indicates that the operation and client notification had already completed.

    static inline int onoff\_cancel\_or\_release(struct [onoff\_manager](#c.onoff_manager) \*mgr, struct [onoff\_client](#c.onoff_client) \*cli)
    :   Helper function to safely cancel a request.

        Some applications may want to issue requests on an asynchronous event (such as connection to a USB bus) and to release on a paired event (such as loss of connection to a USB bus). Applications cannot precisely determine that an in-progress request is still pending without using [onoff\_monitor](#structonoff__monitor) and carefully avoiding race conditions.

        This function is a helper that attempts to cancel the operation and issues a release if cancellation fails because the request was completed. This synchronously ensures that ownership of the client data reverts to the client so is available for a future request.

        Parameters:
        :   - **mgr** – the manager for which an operation is to be cancelled.
            - **cli** – a pointer to the same client state that was provided when [onoff\_request()](#group__resource__mgmt__onoff__apis_1ga20dcb358e405deb87b7fbb7846ef9d68) was invoked. Behavior is undefined if this is a pointer to client data associated with an [onoff\_reset()](#group__resource__mgmt__onoff__apis_1gaf7b46a5f2e43d1bab193c18b8f6c8ba8) request.

        Return values:
        :   - **ONOFF\_STATE\_TO\_ON** – if the cancellation occurred before the transition completed.
            - **ONOFF\_STATE\_ON** – if the cancellation occurred after the transition completed.
            - **-EINVAL** – if the parameters are invalid.
            - **negative** – other errors produced by [onoff\_release()](#group__resource__mgmt__onoff__apis_1ga19da5359f10fa2e2eb034d1e72235ea6).

    int onoff\_reset(struct [onoff\_manager](#c.onoff_manager) \*mgr, struct [onoff\_client](#c.onoff_client) \*cli)
    :   Clear errors on an on-off service and reset it to its off state.

        A service can only be reset when it is in an error state as indicated by [onoff\_has\_error()](#group__resource__mgmt__onoff__apis_1ga347efda0aa0305c134224c59677fa6cb).

        The return value indicates the success or failure of an attempt to initiate an operation to reset the resource. If initiation of the operation succeeds the result of the reset operation itself is provided through the configured client notification method, possibly before this call returns. Multiple clients may request a reset; all are notified when it is complete.

        Note that the call to this function may succeed in a case where the actual reset fails. Always check the operation completion result.

        Note

        Due to the conditions on state transition all incomplete asynchronous operations will have been informed of the error when it occurred. There need be no concern about dangling requests left after a reset completes.

        Parameters:
        :   - **mgr** – the manager to be reset.
            - **cli** – pointer to client state, including instructions on how to notify the client when reset completes. Behavior is undefined if cli references an object associated with an incomplete service operation.

        Return values:
        :   - **non-negative** – the observed state of the machine at the time of the reset, if the reset succeeds.
            - **-ENOTSUP** – if reset is not supported by the service.
            - **-EINVAL** – if the parameters are invalid.
            - **-EALREADY** – if the service does not have a recorded error.

    int onoff\_monitor\_register(struct [onoff\_manager](#c.onoff_manager) \*mgr, struct [onoff\_monitor](#c.onoff_monitor) \*mon)
    :   Add a monitor of state changes for a manager.

        Parameters:
        :   - **mgr** – the manager for which a state changes are to be monitored.
            - **mon** – a linkable node providing a non-null callback to be invoked on state changes.

        Returns:
        :   non-negative on successful addition, or a negative error code.

    int onoff\_monitor\_unregister(struct [onoff\_manager](#c.onoff_manager) \*mgr, struct [onoff\_monitor](#c.onoff_monitor) \*mon)
    :   Remove a monitor of state changes from a manager.

        Parameters:
        :   - **mgr** – the manager for which a state changes are to be monitored.
            - **mon** – a linkable node providing the callback to be invoked on state changes.

        Returns:
        :   non-negative on successful removal, or a negative error code.

    int onoff\_sync\_lock(struct [onoff\_sync\_service](#c.onoff_sync_service) \*srv, [k\_spinlock\_key\_t](../../kernel/services/smp/smp.md#c.k_spinlock_key_t "k_spinlock_key_t") \*keyp)
    :   Lock a synchronous onoff service and provide its state.

        Note

        If an error state is returned it is the caller’s responsibility to decide whether to preserve it (finalize with the same error state) or clear the error (finalize with a non-error result).

        Parameters:
        :   - **srv** – pointer to the synchronous service state.
            - **keyp** – pointer to where the lock key should be stored

        Returns:
        :   negative if the service is in an error state, otherwise the number of active requests at the time the lock was taken. The lock is held on return regardless of whether a negative state is returned.

    int onoff\_sync\_finalize(struct [onoff\_sync\_service](#c.onoff_sync_service) \*srv, [k\_spinlock\_key\_t](../../kernel/services/smp/smp.md#c.k_spinlock_key_t "k_spinlock_key_t") key, struct [onoff\_client](#c.onoff_client) \*cli, int res, bool on)
    :   Process the completion of a transition in a synchronous service and release lock.

        This function updates the service state on the `res` and `on` parameters then releases the lock. If `cli` is not null it finalizes the client notification using `res`.

        If the service was in an error state when locked, and `res` is non-negative when finalized, the count is reset to zero before completing finalization.

        Parameters:
        :   - **srv** – pointer to the synchronous service state
            - **key** – the key returned by the preceding invocation of [onoff\_sync\_lock()](#group__resource__mgmt__onoff__apis_1ga174cadf7dfa5d3c4dc5c8185994f3825).
            - **cli** – pointer to the onoff client through which completion information is returned. If a null pointer is passed only the state of the service is updated. For compatibility with the behavior of callbacks used with the manager API `cli` must be null when `on` is false (the manager does not support callbacks when turning off devices).
            - **res** – the result of the transition. A negative value places the service into an error state. A non-negative value increments or decrements the reference count as specified by `on`.
            - **on** – Only when `res` is non-negative, the service reference count will be incremented if`on` is `true`, and decremented if `on` is `false`.

        Returns:
        :   negative if the service is left or put into an error state, otherwise the number of active requests at the time the lock was released.

    struct onoff\_transitions
    :   *#include <onoff.h>*

        On-off service transition functions.

        Public Members

        [onoff\_transition\_fn](#c.onoff_transition_fn) start
        :   Function to invoke to transition the service to on.

        [onoff\_transition\_fn](#c.onoff_transition_fn) stop
        :   Function to invoke to transition the service to off.

        [onoff\_transition\_fn](#c.onoff_transition_fn) reset
        :   Function to force the service state to reset, where supported.

    struct onoff\_manager
    :   *#include <onoff.h>*

        State associated with an on-off manager.

        No fields in this structure are intended for use by service providers or clients. The state is to be initialized once, using [onoff\_manager\_init()](#group__resource__mgmt__onoff__apis_1ga73d52272baab03d1df2f267429390978), when the service provider is initialized. In case of error it may be reset through the [onoff\_reset()](#group__resource__mgmt__onoff__apis_1gaf7b46a5f2e43d1bab193c18b8f6c8ba8) API.

        Public Members

        [sys\_slist\_t](../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") clients
        :   List of clients waiting for request or reset completion notifications.

        [sys\_slist\_t](../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") monitors
        :   List of monitors to be notified of state changes including errors and transition completion.

        const struct [onoff\_transitions](#c.onoff_transitions) \*transitions
        :   Transition functions.

        struct [k\_spinlock](../../kernel/services/smp/smp.md#c.k_spinlock "k_spinlock") lock
        :   Mutex protection for other fields.

        int last\_res
        :   The result of the last transition.

        uint16\_t flags
        :   Flags identifying the service state.

        uint16\_t refs
        :   Number of active clients for the service.

    struct onoff\_client
    :   *#include <onoff.h>*

        State associated with a client of an on-off service.

        Objects of this type are allocated by a client, which is responsible for zero-initializing the node field and invoking the appropriate [sys\_notify](../notify.md#structsys__notify) init function to configure notification.

        Control of the object content transfers to the service provider when a pointer to the object is passed to any on-off manager function. While the service provider controls the object the client must not change any object fields. Control reverts to the client concurrent with release of the owned [sys\_notify](../notify.md#structsys__notify) structure, or when indicated by an [onoff\_cancel()](#group__resource__mgmt__onoff__apis_1gad05d32f1548e56b508628e84ba101554) return value.

        After control has reverted to the client the notify field must be reinitialized for the next operation.

        Public Members

        struct [sys\_notify](../notify.md#c.sys_notify "sys_notify") notify
        :   Notification configuration.

    struct onoff\_monitor
    :   *#include <onoff.h>*

        Registration state for notifications of onoff service transitions.

        Any given [onoff\_monitor](#structonoff__monitor) structure can be associated with at most one [onoff\_manager](#structonoff__manager) instance.

        Public Members

        [sys\_snode\_t](../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Links the client into the set of waiting service users.

            This must be zero-initialized.

        [onoff\_monitor\_callback](#c.onoff_monitor_callback) callback
        :   Callback to be invoked on state change.

            This must not be null.

    struct onoff\_sync\_service
    :   *#include <onoff.h>*

        State used when a driver uses the on-off service API for synchronous operations.

        This is useful when a subsystem API uses the on-off API to support asynchronous operations but the transitions required by a particular driver are isr-ok and not sleep. It serves as a substitute for [onoff\_manager](#structonoff__manager), with locking and persisted state updates supported by [onoff\_sync\_lock()](#group__resource__mgmt__onoff__apis_1ga174cadf7dfa5d3c4dc5c8185994f3825) and [onoff\_sync\_finalize()](#group__resource__mgmt__onoff__apis_1gae3331bdad9d03309ee78e86c487b7f26).

        Public Members

        struct [k\_spinlock](../../kernel/services/smp/smp.md#c.k_spinlock "k_spinlock") lock
        :   Mutex protection for other fields.

        int32\_t count
        :   Negative is error, non-negative is reference count.
