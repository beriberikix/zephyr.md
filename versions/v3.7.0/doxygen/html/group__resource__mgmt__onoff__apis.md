---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__resource__mgmt__onoff__apis.html
original_path: doxygen/html/group__resource__mgmt__onoff__apis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

On-Off Service APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [onoff\_transitions](structonoff__transitions.md) |
|  | On-off service transition functions. [More...](structonoff__transitions.md#details) |
| struct | [onoff\_manager](structonoff__manager.md) |
|  | State associated with an on-off manager. [More...](structonoff__manager.md#details) |
| struct | [onoff\_client](structonoff__client.md) |
|  | State associated with a client of an on-off service. [More...](structonoff__client.md#details) |
| struct | [onoff\_monitor](structonoff__monitor.md) |
|  | Registration state for notifications of onoff service transitions. [More...](structonoff__monitor.md#details) |
| struct | [onoff\_sync\_service](structonoff__sync__service.md) |
|  | State used when a driver uses the on-off service API for synchronous operations. [More...](structonoff__sync__service.md#details) |

| Macros | |
| --- | --- |
| #define | [ONOFF\_FLAG\_ERROR](#ga9ae0c3528254b10f5e1a9743aea234dd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag indicating an error state. |
| #define | [ONOFF\_STATE\_MASK](#ga0e06eafdf5021ce970027f20fc001acc) |
|  | Mask used to isolate bits defining the service state. |
| #define | [ONOFF\_STATE\_OFF](#gab9e5380dce026a5dfea770f999400484)   0U |
|  | Value exposed by ONOFF\_STATE\_MASK when service is off. |
| #define | [ONOFF\_STATE\_ON](#ga7cd0fba52afba2e337ab7c830d3058d7)   ONOFF\_FLAG\_ONOFF |
|  | Value exposed by ONOFF\_STATE\_MASK when service is on. |
| #define | [ONOFF\_STATE\_ERROR](#gac005a25d149568208a6fbaa2ceaa1ac6)   [ONOFF\_FLAG\_ERROR](#ga9ae0c3528254b10f5e1a9743aea234dd) |
|  | Value exposed by ONOFF\_STATE\_MASK when the service is in an error state (and not in the process of resetting its state). |
| #define | [ONOFF\_STATE\_TO\_ON](#gac4a0d8a7b501adb011aa1c4c4da3f2a3)   (ONOFF\_FLAG\_TRANSITION | [ONOFF\_STATE\_ON](#ga7cd0fba52afba2e337ab7c830d3058d7)) |
|  | Value exposed by ONOFF\_STATE\_MASK when service is transitioning to on. |
| #define | [ONOFF\_STATE\_TO\_OFF](#ga235a04122763f1a2cbb849c56df65d26)   (ONOFF\_FLAG\_TRANSITION | [ONOFF\_STATE\_OFF](#gab9e5380dce026a5dfea770f999400484)) |
|  | Value exposed by ONOFF\_STATE\_MASK when service is transitioning to off. |
| #define | [ONOFF\_STATE\_RESETTING](#gacc0438b5c81c639e0035ada5caec940b)   (ONOFF\_FLAG\_TRANSITION | [ONOFF\_STATE\_ERROR](#gac005a25d149568208a6fbaa2ceaa1ac6)) |
|  | Value exposed by ONOFF\_STATE\_MASK when service is in the process of resetting. |
| #define | [ONOFF\_TRANSITIONS\_INITIALIZER](#ga8c1171a844ef1d9d6541d342124492ff)(\_start, \_stop, \_reset) |
|  | Initializer for a [onoff\_transitions](structonoff__transitions.md "On-off service transition functions.") object. |
| #define | [ONOFF\_CLIENT\_EXTENSION\_POS](#gad61d053ae4e9ee12efe8d37372a16c63)   [SYS\_NOTIFY\_EXTENSION\_POS](notify_8h.md#aa22143622004e478668cdd98a2e04357) |
|  | Identify region of [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") flags available for containing services. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [onoff\_notify\_fn](#gac05f7946a14fa23ef67212eba30c98ac)) (struct [onoff\_manager](structonoff__manager.md) \*mgr, int res) |
|  | Signature used to notify an on-off manager that a transition has completed. |
| typedef void(\* | [onoff\_transition\_fn](#ga51fdf83642c5fa16112ce143382ec5d1)) (struct [onoff\_manager](structonoff__manager.md) \*mgr, [onoff\_notify\_fn](#gac05f7946a14fa23ef67212eba30c98ac) notify) |
|  | Signature used by service implementations to effect a transition. |
| typedef void(\* | [onoff\_client\_callback](#ga41b94526182c5772d7adebb1d1745068)) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_client](structonoff__client.md) \*cli, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), int res) |
|  | Signature used to notify an on-off service client of the completion of an operation. |
| typedef void(\* | [onoff\_monitor\_callback](#gaee41b38d408cf5f5efc9cd007f377545)) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_monitor](structonoff__monitor.md) \*mon, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), int res) |
|  | Signature used to notify a monitor of an onoff service of errors or completion of a state transition. |

| Functions | |
| --- | --- |
| int | [onoff\_manager\_init](#ga73d52272baab03d1df2f267429390978) (struct [onoff\_manager](structonoff__manager.md) \*mgr, const struct [onoff\_transitions](structonoff__transitions.md) \*transitions) |
|  | Initialize an on-off service to off state. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [onoff\_has\_error](#ga347efda0aa0305c134224c59677fa6cb) (const struct [onoff\_manager](structonoff__manager.md) \*mgr) |
|  | Test whether an on-off service has recorded an error. |
| int | [onoff\_request](#ga20dcb358e405deb87b7fbb7846ef9d68) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_client](structonoff__client.md) \*cli) |
|  | Request a reservation to use an on-off service. |
| int | [onoff\_release](#ga19da5359f10fa2e2eb034d1e72235ea6) (struct [onoff\_manager](structonoff__manager.md) \*mgr) |
|  | Release a reserved use of an on-off service. |
| int | [onoff\_cancel](#gad05d32f1548e56b508628e84ba101554) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_client](structonoff__client.md) \*cli) |
|  | Attempt to cancel an in-progress client operation. |
| static int | [onoff\_cancel\_or\_release](#ga7aac2aeb66907ec920557f0ef67d6795) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_client](structonoff__client.md) \*cli) |
|  | Helper function to safely cancel a request. |
| int | [onoff\_reset](#gaf7b46a5f2e43d1bab193c18b8f6c8ba8) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_client](structonoff__client.md) \*cli) |
|  | Clear errors on an on-off service and reset it to its off state. |
| int | [onoff\_monitor\_register](#ga9897d93359fe58359c0204da46b4c01e) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_monitor](structonoff__monitor.md) \*mon) |
|  | Add a monitor of state changes for a manager. |
| int | [onoff\_monitor\_unregister](#ga50a51da8e701a3f19f242af5183d807a) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_monitor](structonoff__monitor.md) \*mon) |
|  | Remove a monitor of state changes from a manager. |
| int | [onoff\_sync\_lock](#ga174cadf7dfa5d3c4dc5c8185994f3825) (struct [onoff\_sync\_service](structonoff__sync__service.md) \*srv, [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) \*keyp) |
|  | Lock a synchronous onoff service and provide its state. |
| int | [onoff\_sync\_finalize](#gae3331bdad9d03309ee78e86c487b7f26) (struct [onoff\_sync\_service](structonoff__sync__service.md) \*srv, [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) key, struct [onoff\_client](structonoff__client.md) \*cli, int res, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) on) |
|  | Process the completion of a transition in a synchronous service and release lock. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gad61d053ae4e9ee12efe8d37372a16c63)ONOFF\_CLIENT\_EXTENSION\_POS

| #define ONOFF\_CLIENT\_EXTENSION\_POS   [SYS\_NOTIFY\_EXTENSION\_POS](notify_8h.md#aa22143622004e478668cdd98a2e04357) |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

Identify region of [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") flags available for containing services.

Bits of the flags field of the [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") structure contained within the queued\_operation structure at and above this position may be used by extensions to the [onoff\_client](structonoff__client.md "State associated with a client of an on-off service.") structure.

These bits are intended for use by containing service implementations to record client-specific information and are subject to other conditions of use specified on the [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") API.

## [◆ ](#ga9ae0c3528254b10f5e1a9743aea234dd)ONOFF\_FLAG\_ERROR

| #define ONOFF\_FLAG\_ERROR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

Flag indicating an error state.

Error states are cleared using [onoff\_reset()](#gaf7b46a5f2e43d1bab193c18b8f6c8ba8).

## [◆ ](#gac005a25d149568208a6fbaa2ceaa1ac6)ONOFF\_STATE\_ERROR

| #define ONOFF\_STATE\_ERROR   [ONOFF\_FLAG\_ERROR](#ga9ae0c3528254b10f5e1a9743aea234dd) |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

Value exposed by ONOFF\_STATE\_MASK when the service is in an error state (and not in the process of resetting its state).

## [◆ ](#ga0e06eafdf5021ce970027f20fc001acc)ONOFF\_STATE\_MASK

| #define ONOFF\_STATE\_MASK |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

**Value:**

([ONOFF\_FLAG\_ERROR](#ga9ae0c3528254b10f5e1a9743aea234dd) \

| ONOFF\_FLAG\_ONOFF \

| ONOFF\_FLAG\_TRANSITION)

[ONOFF\_FLAG\_ERROR](#ga9ae0c3528254b10f5e1a9743aea234dd)

#define ONOFF\_FLAG\_ERROR

Flag indicating an error state.

**Definition** onoff.h:30

Mask used to isolate bits defining the service state.

Mask a value with this then test for ONOFF\_FLAG\_ERROR to determine whether the machine has an unfixed error, or compare against ONOFF\_STATE\_ON, ONOFF\_STATE\_OFF, ONOFF\_STATE\_TO\_ON, ONOFF\_STATE\_TO\_OFF, or ONOFF\_STATE\_RESETTING.

## [◆ ](#gab9e5380dce026a5dfea770f999400484)ONOFF\_STATE\_OFF

| #define ONOFF\_STATE\_OFF   0U |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

Value exposed by ONOFF\_STATE\_MASK when service is off.

## [◆ ](#ga7cd0fba52afba2e337ab7c830d3058d7)ONOFF\_STATE\_ON

| #define ONOFF\_STATE\_ON   ONOFF\_FLAG\_ONOFF |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

Value exposed by ONOFF\_STATE\_MASK when service is on.

## [◆ ](#gacc0438b5c81c639e0035ada5caec940b)ONOFF\_STATE\_RESETTING

| #define ONOFF\_STATE\_RESETTING   (ONOFF\_FLAG\_TRANSITION | [ONOFF\_STATE\_ERROR](#gac005a25d149568208a6fbaa2ceaa1ac6)) |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

Value exposed by ONOFF\_STATE\_MASK when service is in the process of resetting.

## [◆ ](#ga235a04122763f1a2cbb849c56df65d26)ONOFF\_STATE\_TO\_OFF

| #define ONOFF\_STATE\_TO\_OFF   (ONOFF\_FLAG\_TRANSITION | [ONOFF\_STATE\_OFF](#gab9e5380dce026a5dfea770f999400484)) |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

Value exposed by ONOFF\_STATE\_MASK when service is transitioning to off.

## [◆ ](#gac4a0d8a7b501adb011aa1c4c4da3f2a3)ONOFF\_STATE\_TO\_ON

| #define ONOFF\_STATE\_TO\_ON   (ONOFF\_FLAG\_TRANSITION | [ONOFF\_STATE\_ON](#ga7cd0fba52afba2e337ab7c830d3058d7)) |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

Value exposed by ONOFF\_STATE\_MASK when service is transitioning to on.

## [◆ ](#ga8c1171a844ef1d9d6541d342124492ff)ONOFF\_TRANSITIONS\_INITIALIZER

| #define ONOFF\_TRANSITIONS\_INITIALIZER | ( |  | *\_start*, |
| --- | --- | --- | --- |
|  |  |  | *\_stop*, |
|  |  |  | *\_reset* ) |

`#include <[onoff.h](onoff_8h.md)>`

**Value:**

{ \

.start = (\_start), \

.stop = (\_stop), \

.reset = (\_reset), \

}

Initializer for a [onoff\_transitions](structonoff__transitions.md "On-off service transition functions.") object.

Parameters
:   | \_start | a function used to transition from off to on state. |
    | --- | --- |
    | \_stop | a function used to transition from on to off state. |
    | \_reset | a function used to clear errors and force the service to an off state. Can be null. |

## Typedef Documentation

## [◆ ](#ga41b94526182c5772d7adebb1d1745068)onoff\_client\_callback

| typedef void(\* onoff\_client\_callback) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_client](structonoff__client.md) \*cli, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), int res) |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

Signature used to notify an on-off service client of the completion of an operation.

These functions may be invoked from any context including pre-kernel, ISR, or cooperative or pre-emptible threads. Compatible functions must be isr-ok and not sleep.

Parameters
:   | mgr | the manager for which the operation was initiated. This may be null if the on-off service uses synchronous transitions. |
    | --- | --- |
    | cli | the client structure passed to the function that initiated the operation. |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | the state of the machine at the time of completion, restricted by ONOFF\_STATE\_MASK. ONOFF\_FLAG\_ERROR must be checked independently of whether res is negative as a machine error may indicate that all future operations except [onoff\_reset()](#gaf7b46a5f2e43d1bab193c18b8f6c8ba8) will fail. |
    | res | the result of the operation. Expected values are service-specific, but the value shall be non-negative if the operation succeeded, and negative if the operation failed. If res is negative ONOFF\_FLAG\_ERROR will be set in state, but if res is non-negative ONOFF\_FLAG\_ERROR may still be set in state. |

## [◆ ](#gaee41b38d408cf5f5efc9cd007f377545)onoff\_monitor\_callback

| typedef void(\* onoff\_monitor\_callback) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_monitor](structonoff__monitor.md) \*mon, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), int res) |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

Signature used to notify a monitor of an onoff service of errors or completion of a state transition.

This is similar to [onoff\_client\_callback](#ga41b94526182c5772d7adebb1d1745068) but provides information about all transitions, not just ones associated with a specific client. Monitor callbacks are invoked before any completion notifications associated with the state change are made.

These functions may be invoked from any context including pre-kernel, ISR, or cooperative or pre-emptible threads. Compatible functions must be isr-ok and not sleep.

The callback is permitted to unregister itself from the manager, but must not register or unregister any other monitors.

Parameters
:   | mgr | the manager for which a transition has completed. |
    | --- | --- |
    | mon | the monitor instance through which this notification arrived. |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | the state of the machine at the time of completion, restricted by ONOFF\_STATE\_MASK. All valid states may be observed. |
    | res | the result of the operation. Expected values are service- and state-specific, but the value shall be non-negative if the operation succeeded, and negative if the operation failed. |

## [◆ ](#gac05f7946a14fa23ef67212eba30c98ac)onoff\_notify\_fn

| typedef void(\* onoff\_notify\_fn) (struct [onoff\_manager](structonoff__manager.md) \*mgr, int res) |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

Signature used to notify an on-off manager that a transition has completed.

Functions of this type are passed to service-specific transition functions to be used to report the completion of the operation. The functions may be invoked from any context.

Parameters
:   | mgr | the manager for which transition was requested. |
    | --- | --- |
    | res | the result of the transition. This shall be non-negative on success, or a negative error code. If an error is indicated the service shall enter an error state. |

## [◆ ](#ga51fdf83642c5fa16112ce143382ec5d1)onoff\_transition\_fn

| typedef void(\* onoff\_transition\_fn) (struct [onoff\_manager](structonoff__manager.md) \*mgr, [onoff\_notify\_fn](#gac05f7946a14fa23ef67212eba30c98ac) notify) |
| --- |

`#include <[onoff.h](onoff_8h.md)>`

Signature used by service implementations to effect a transition.

Service definitions use two required function pointers of this type to be notified that a transition is required, and a third optional one to reset the service when it is in an error state.

The start function will be called only from the off state.

The stop function will be called only from the on state.

The reset function (where supported) will be called only when [onoff\_has\_error()](#ga347efda0aa0305c134224c59677fa6cb) returns true.

Note
:   All transitions functions must be isr-ok.

Parameters
:   | mgr | the manager for which transition was requested. |
    | --- | --- |
    | notify | the function to be invoked when the transition has completed. If the transition is synchronous, notify shall be invoked by the implementation before the transition function returns. Otherwise the implementation shall capture this parameter and invoke it when the transition completes. |

## Function Documentation

## [◆ ](#gad05d32f1548e56b508628e84ba101554)onoff\_cancel()

| int onoff\_cancel | ( | struct [onoff\_manager](structonoff__manager.md) \* | *mgr*, |
| --- | --- | --- | --- |
|  |  | struct [onoff\_client](structonoff__client.md) \* | *cli* ) |

`#include <[onoff.h](onoff_8h.md)>`

Attempt to cancel an in-progress client operation.

It may be that a client has initiated an operation but needs to shut down before the operation has completed. For example, when a request was made and the need is no longer present.

Cancelling is supported only for [onoff\_request()](#ga20dcb358e405deb87b7fbb7846ef9d68) and [onoff\_reset()](#gaf7b46a5f2e43d1bab193c18b8f6c8ba8) operations, and is a synchronous operation. Be aware that any transition that was initiated on behalf of the client will continue to progress to completion: it is only notification of transition completion that may be eliminated. If there are no active requests when a transition to on completes the manager will initiate a transition to off.

Client notification does not occur for cancelled operations.

Parameters
:   | mgr | the manager for which an operation is to be cancelled. |
    | --- | --- |
    | cli | a pointer to the same client state that was provided when the operation to be cancelled was issued. |

Return values
:   | non-negative | the observed state of the machine at the time of the cancellation, if the cancellation succeeds. On successful cancellation ownership of `*cli` reverts to the client. |
    | --- | --- |
    | -EINVAL | if the parameters are invalid. |
    | -EALREADY | if cli was not a record of an uncompleted notification at the time the cancellation was processed. This likely indicates that the operation and client notification had already completed. |

## [◆ ](#ga7aac2aeb66907ec920557f0ef67d6795)onoff\_cancel\_or\_release()

| | int onoff\_cancel\_or\_release | ( | struct [onoff\_manager](structonoff__manager.md) \* | *mgr*, | | --- | --- | --- | --- | |  |  | struct [onoff\_client](structonoff__client.md) \* | *cli* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[onoff.h](onoff_8h.md)>`

Helper function to safely cancel a request.

Some applications may want to issue requests on an asynchronous event (such as connection to a USB bus) and to release on a paired event (such as loss of connection to a USB bus). Applications cannot precisely determine that an in-progress request is still pending without using [onoff\_monitor](structonoff__monitor.md "Registration state for notifications of onoff service transitions.") and carefully avoiding race conditions.

This function is a helper that attempts to cancel the operation and issues a release if cancellation fails because the request was completed. This synchronously ensures that ownership of the client data reverts to the client so is available for a future request.

Parameters
:   | mgr | the manager for which an operation is to be cancelled. |
    | --- | --- |
    | cli | a pointer to the same client state that was provided when [onoff\_request()](#ga20dcb358e405deb87b7fbb7846ef9d68) was invoked. Behavior is undefined if this is a pointer to client data associated with an [onoff\_reset()](#gaf7b46a5f2e43d1bab193c18b8f6c8ba8) request. |

Return values
:   | [ONOFF\_STATE\_TO\_ON](#gac4a0d8a7b501adb011aa1c4c4da3f2a3) | if the cancellation occurred before the transition completed. |
    | --- | --- |
    | [ONOFF\_STATE\_ON](#ga7cd0fba52afba2e337ab7c830d3058d7) | if the cancellation occurred after the transition completed. |
    | -EINVAL | if the parameters are invalid. |
    | negative | other errors produced by [onoff\_release()](#ga19da5359f10fa2e2eb034d1e72235ea6). |

## [◆ ](#ga347efda0aa0305c134224c59677fa6cb)onoff\_has\_error()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) onoff\_has\_error | ( | const struct [onoff\_manager](structonoff__manager.md) \* | *mgr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[onoff.h](onoff_8h.md)>`

Test whether an on-off service has recorded an error.

This function can be used to determine whether the service has recorded an error. Errors may be cleared by invoking [onoff\_reset()](#gaf7b46a5f2e43d1bab193c18b8f6c8ba8).

This is an unlocked convenience function suitable for use only when it is known that no other process might invoke an operation that transitions the service between an error and non-error state.

Returns
:   true if and only if the service has an uncleared error.

## [◆ ](#ga73d52272baab03d1df2f267429390978)onoff\_manager\_init()

| int onoff\_manager\_init | ( | struct [onoff\_manager](structonoff__manager.md) \* | *mgr*, |
| --- | --- | --- | --- |
|  |  | const struct [onoff\_transitions](structonoff__transitions.md) \* | *transitions* ) |

`#include <[onoff.h](onoff_8h.md)>`

Initialize an on-off service to off state.

This function must be invoked exactly once per service instance, by the infrastructure that provides the service, and before any other on-off service API is invoked on the service.

This function should never be invoked by clients of an on-off service.

Parameters
:   | mgr | the manager definition object to be initialized. |
    | --- | --- |
    | transitions | pointer to a structure providing transition functions. The referenced object must persist as long as the manager can be referenced. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | if start, stop, or flags are invalid |

## [◆ ](#ga9897d93359fe58359c0204da46b4c01e)onoff\_monitor\_register()

| int onoff\_monitor\_register | ( | struct [onoff\_manager](structonoff__manager.md) \* | *mgr*, |
| --- | --- | --- | --- |
|  |  | struct [onoff\_monitor](structonoff__monitor.md) \* | *mon* ) |

`#include <[onoff.h](onoff_8h.md)>`

Add a monitor of state changes for a manager.

Parameters
:   | mgr | the manager for which a state changes are to be monitored. |
    | --- | --- |
    | mon | a linkable node providing a non-null callback to be invoked on state changes. |

Returns
:   non-negative on successful addition, or a negative error code.

## [◆ ](#ga50a51da8e701a3f19f242af5183d807a)onoff\_monitor\_unregister()

| int onoff\_monitor\_unregister | ( | struct [onoff\_manager](structonoff__manager.md) \* | *mgr*, |
| --- | --- | --- | --- |
|  |  | struct [onoff\_monitor](structonoff__monitor.md) \* | *mon* ) |

`#include <[onoff.h](onoff_8h.md)>`

Remove a monitor of state changes from a manager.

Parameters
:   | mgr | the manager for which a state changes are to be monitored. |
    | --- | --- |
    | mon | a linkable node providing the callback to be invoked on state changes. |

Returns
:   non-negative on successful removal, or a negative error code.

## [◆ ](#ga19da5359f10fa2e2eb034d1e72235ea6)onoff\_release()

| int onoff\_release | ( | struct [onoff\_manager](structonoff__manager.md) \* | *mgr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[onoff.h](onoff_8h.md)>`

Release a reserved use of an on-off service.

This synchronously releases the caller's previous request. If the last request is released the manager will initiate a transition to off, which can be observed by registering an [onoff\_monitor](structonoff__monitor.md "Registration state for notifications of onoff service transitions.").

Note
:   Behavior is undefined if this is not paired with a preceding [onoff\_request()](#ga20dcb358e405deb87b7fbb7846ef9d68) call that completed successfully.

Parameters
:   | mgr | the manager for which a request was successful. |
    | --- | --- |

Return values
:   | non-negative | the observed state (ONOFF\_STATE\_ON) of the machine at the time of the release, if the release succeeds. |
    | --- | --- |
    | -EIO | if service has recorded an error. |
    | -ENOTSUP | if the machine is not in a state that permits release. |

## [◆ ](#ga20dcb358e405deb87b7fbb7846ef9d68)onoff\_request()

| int onoff\_request | ( | struct [onoff\_manager](structonoff__manager.md) \* | *mgr*, |
| --- | --- | --- | --- |
|  |  | struct [onoff\_client](structonoff__client.md) \* | *cli* ) |

`#include <[onoff.h](onoff_8h.md)>`

Request a reservation to use an on-off service.

The return value indicates the success or failure of an attempt to initiate an operation to request the resource be made available. If initiation of the operation succeeds the result of the request operation is provided through the configured client notification method, possibly before this call returns.

Note that the call to this function may succeed in a case where the actual request fails. Always check the operation completion result.

Parameters
:   | mgr | the manager that will be used. |
    | --- | --- |
    | cli | a non-null pointer to client state providing instructions on synchronous expectations and how to notify the client when the request completes. Behavior is undefined if client passes a pointer object associated with an incomplete service operation. |

Return values
:   | non-negative | the observed state of the machine at the time the request was processed, if successful. |
    | --- | --- |
    | -EIO | if service has recorded an error. |
    | -EINVAL | if the parameters are invalid. |
    | -EAGAIN | if the reference count would overflow. |

## [◆ ](#gaf7b46a5f2e43d1bab193c18b8f6c8ba8)onoff\_reset()

| int onoff\_reset | ( | struct [onoff\_manager](structonoff__manager.md) \* | *mgr*, |
| --- | --- | --- | --- |
|  |  | struct [onoff\_client](structonoff__client.md) \* | *cli* ) |

`#include <[onoff.h](onoff_8h.md)>`

Clear errors on an on-off service and reset it to its off state.

A service can only be reset when it is in an error state as indicated by [onoff\_has\_error()](#ga347efda0aa0305c134224c59677fa6cb).

The return value indicates the success or failure of an attempt to initiate an operation to reset the resource. If initiation of the operation succeeds the result of the reset operation itself is provided through the configured client notification method, possibly before this call returns. Multiple clients may request a reset; all are notified when it is complete.

Note that the call to this function may succeed in a case where the actual reset fails. Always check the operation completion result.

Note
:   Due to the conditions on state transition all incomplete asynchronous operations will have been informed of the error when it occurred. There need be no concern about dangling requests left after a reset completes.

Parameters
:   | mgr | the manager to be reset. |
    | --- | --- |
    | cli | pointer to client state, including instructions on how to notify the client when reset completes. Behavior is undefined if cli references an object associated with an incomplete service operation. |

Return values
:   | non-negative | the observed state of the machine at the time of the reset, if the reset succeeds. |
    | --- | --- |
    | -ENOTSUP | if reset is not supported by the service. |
    | -EINVAL | if the parameters are invalid. |
    | -EALREADY | if the service does not have a recorded error. |

## [◆ ](#gae3331bdad9d03309ee78e86c487b7f26)onoff\_sync\_finalize()

| int onoff\_sync\_finalize | ( | struct [onoff\_sync\_service](structonoff__sync__service.md) \* | *srv*, |
| --- | --- | --- | --- |
|  |  | [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) | *key*, |
|  |  | struct [onoff\_client](structonoff__client.md) \* | *cli*, |
|  |  | int | *res*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *on* ) |

`#include <[onoff.h](onoff_8h.md)>`

Process the completion of a transition in a synchronous service and release lock.

This function updates the service state on the `res` and `on` parameters then releases the lock. If `cli` is not null it finalizes the client notification using `res`.

If the service was in an error state when locked, and `res` is non-negative when finalized, the count is reset to zero before completing finalization.

Parameters
:   | srv | pointer to the synchronous service state |
    | --- | --- |
    | key | the key returned by the preceding invocation of [onoff\_sync\_lock()](#ga174cadf7dfa5d3c4dc5c8185994f3825). |
    | cli | pointer to the onoff client through which completion information is returned. If a null pointer is passed only the state of the service is updated. For compatibility with the behavior of callbacks used with the manager API `cli` must be null when `on` is false (the manager does not support callbacks when turning off devices). |
    | res | the result of the transition. A negative value places the service into an error state. A non-negative value increments or decrements the reference count as specified by `on`. |
    | on | Only when `res` is non-negative, the service reference count will be incremented if`on` is `true`, and decremented if `on` is `false`. |

Returns
:   negative if the service is left or put into an error state, otherwise the number of active requests at the time the lock was released.

## [◆ ](#ga174cadf7dfa5d3c4dc5c8185994f3825)onoff\_sync\_lock()

| int onoff\_sync\_lock | ( | struct [onoff\_sync\_service](structonoff__sync__service.md) \* | *srv*, |
| --- | --- | --- | --- |
|  |  | [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) \* | *keyp* ) |

`#include <[onoff.h](onoff_8h.md)>`

Lock a synchronous onoff service and provide its state.

Note
:   If an error state is returned it is the caller's responsibility to decide whether to preserve it (finalize with the same error state) or clear the error (finalize with a non-error result).

Parameters
:   | srv | pointer to the synchronous service state. |
    | --- | --- |
    | keyp | pointer to where the lock key should be stored |

Returns
:   negative if the service is in an error state, otherwise the number of active requests at the time the lock was taken. The lock is held on return regardless of whether a negative state is returned.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
