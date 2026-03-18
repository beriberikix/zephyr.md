---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__subsys__pm__sys__policy.html
original_path: doxygen/html/group__subsys__pm__sys__policy.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Policy

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md) » [System](group__subsys__pm__sys.md)

System Power Management Policy API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) |
|  | Latency change subscription. [More...](structpm__policy__latency__subscription.md#details) |
| struct | [pm\_policy\_latency\_request](structpm__policy__latency__request.md) |
|  | Latency request. [More...](structpm__policy__latency__request.md#details) |
| struct | [pm\_policy\_event](structpm__policy__event.md) |
|  | Event. [More...](structpm__policy__event.md#details) |

| Macros | |
| --- | --- |
| #define | [PM\_ALL\_SUBSTATES](#gab241e40f9282a1c8ebc602997fbb3190)   ([UINT8\_MAX](stdint_8h.md#aeb4e270a084ee26fe73e799861bd0252)) |
|  | Special value for 'all substates'. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [pm\_policy\_latency\_changed\_cb\_t](#gab2a0a73416b3fcb535fa54a1f3b4c267)) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) latency) |
|  | Callback to notify when maximum latency changes. |

| Functions | |
| --- | --- |
| void | [pm\_policy\_state\_lock\_get](#gabbb379f8572f164addafe93ad3468f3d) (enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) substate\_id) |
|  | Increase a power state lock counter. |
| void | [pm\_policy\_state\_lock\_put](#ga12f4d121aa8be0eb66381713b481a8b1) (enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) substate\_id) |
|  | Decrease a power state lock counter. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_policy\_state\_lock\_is\_active](#ga39f14c8509dee55ed084b4111584b766) (enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) substate\_id) |
|  | Check if a power state lock is active (not allowed). |
| void | [pm\_policy\_latency\_request\_add](#ga848627f6d143ece582711a16cab5442a) (struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us) |
|  | Add a new latency requirement. |
| void | [pm\_policy\_latency\_request\_update](#ga6483bd320881d697de27493b4f2d92d1) (struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us) |
|  | Update a latency requirement. |
| void | [pm\_policy\_latency\_request\_remove](#gaadcb851b1bfb312ea0960918dc9f869e) (struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req) |
|  | Remove a latency requirement. |
| void | [pm\_policy\_latency\_changed\_subscribe](#gacf77adf6eaf5258e03ce1923d685ed3b) (struct [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) \*req, [pm\_policy\_latency\_changed\_cb\_t](#gab2a0a73416b3fcb535fa54a1f3b4c267) cb) |
|  | Subscribe to maximum latency changes. |
| void | [pm\_policy\_latency\_changed\_unsubscribe](#ga8ca62cfeef8d4ebb58800e3ac6b645ee) (struct [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) \*req) |
|  | Unsubscribe to maximum latency changes. |
| void | [pm\_policy\_event\_register](#gafab2e1484a58131a9c7cefd2b9adb3e9) (struct [pm\_policy\_event](structpm__policy__event.md) \*evt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_us) |
|  | Register an event. |
| void | [pm\_policy\_event\_update](#ga1d6d278768ed961c3856119de2fbb74b) (struct [pm\_policy\_event](structpm__policy__event.md) \*evt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_us) |
|  | Update an event. |
| void | [pm\_policy\_event\_unregister](#ga9448e31e1bd1a8b02defe6d1427197ff) (struct [pm\_policy\_event](structpm__policy__event.md) \*evt) |
|  | Unregister an event. |

## Detailed Description

System Power Management Policy API.

## Macro Definition Documentation

## [◆ ](#gab241e40f9282a1c8ebc602997fbb3190)PM\_ALL\_SUBSTATES

| #define PM\_ALL\_SUBSTATES   ([UINT8\_MAX](stdint_8h.md#aeb4e270a084ee26fe73e799861bd0252)) |
| --- |

`#include <[policy.h](policy_8h.md)>`

Special value for 'all substates'.

## Typedef Documentation

## [◆ ](#gab2a0a73416b3fcb535fa54a1f3b4c267)pm\_policy\_latency\_changed\_cb\_t

| typedef void(\* pm\_policy\_latency\_changed\_cb\_t) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) latency) |
| --- |

`#include <[policy.h](policy_8h.md)>`

Callback to notify when maximum latency changes.

Parameters
:   | latency | New maximum latency. Positive value represents latency in microseconds. SYS\_FOREVER\_US value lifts the latency constraint. Other values are forbidden. |
    | --- | --- |

## Function Documentation

## [◆ ](#gafab2e1484a58131a9c7cefd2b9adb3e9)pm\_policy\_event\_register()

| void pm\_policy\_event\_register | ( | struct [pm\_policy\_event](structpm__policy__event.md) \* | *evt*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *time\_us* ) |

`#include <[policy.h](policy_8h.md)>`

Register an event.

Events in the power-management policy context are defined as any source that will wake up the system at a known time in the future. By registering such event, the policy manager will be able to decide whether certain power states are worth entering or not.

Note
:   It is mandatory to unregister events once they have happened by using [pm\_policy\_event\_unregister()](#ga9448e31e1bd1a8b02defe6d1427197ff). Not doing so is an API contract violation, because the system would continue to consider them as valid events in the *far* future, that is, after the cycle counter rollover.

Parameters
:   | evt | Event. |
    | --- | --- |
    | time\_us | When the event will occur, in microseconds from now. |

See also
:   [pm\_policy\_event\_unregister](#ga9448e31e1bd1a8b02defe6d1427197ff)

## [◆ ](#ga9448e31e1bd1a8b02defe6d1427197ff)pm\_policy\_event\_unregister()

| void pm\_policy\_event\_unregister | ( | struct [pm\_policy\_event](structpm__policy__event.md) \* | *evt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[policy.h](policy_8h.md)>`

Unregister an event.

Parameters
:   | evt | Event. |
    | --- | --- |

See also
:   [pm\_policy\_event\_register](#gafab2e1484a58131a9c7cefd2b9adb3e9)

## [◆ ](#ga1d6d278768ed961c3856119de2fbb74b)pm\_policy\_event\_update()

| void pm\_policy\_event\_update | ( | struct [pm\_policy\_event](structpm__policy__event.md) \* | *evt*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *time\_us* ) |

`#include <[policy.h](policy_8h.md)>`

Update an event.

Parameters
:   | evt | Event. |
    | --- | --- |
    | time\_us | When the event will occur, in microseconds from now. |

See also
:   [pm\_policy\_event\_register](#gafab2e1484a58131a9c7cefd2b9adb3e9)

## [◆ ](#gacf77adf6eaf5258e03ce1923d685ed3b)pm\_policy\_latency\_changed\_subscribe()

| void pm\_policy\_latency\_changed\_subscribe | ( | struct [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) \* | *req*, |
| --- | --- | --- | --- |
|  |  | [pm\_policy\_latency\_changed\_cb\_t](#gab2a0a73416b3fcb535fa54a1f3b4c267) | *cb* ) |

`#include <[policy.h](policy_8h.md)>`

Subscribe to maximum latency changes.

Parameters
:   | req | Subscription request. |
    | --- | --- |
    | cb | Callback function (NULL to disable). |

## [◆ ](#ga8ca62cfeef8d4ebb58800e3ac6b645ee)pm\_policy\_latency\_changed\_unsubscribe()

| void pm\_policy\_latency\_changed\_unsubscribe | ( | struct [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) \* | *req* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[policy.h](policy_8h.md)>`

Unsubscribe to maximum latency changes.

Parameters
:   | req | Subscription request. |
    | --- | --- |

## [◆ ](#ga848627f6d143ece582711a16cab5442a)pm\_policy\_latency\_request\_add()

| void pm\_policy\_latency\_request\_add | ( | struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \* | *req*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *value\_us* ) |

`#include <[policy.h](policy_8h.md)>`

Add a new latency requirement.

The system will not enter any power state that would make the system to exceed the given latency value.

Parameters
:   | req | Latency request. |
    | --- | --- |
    | value\_us | Maximum allowed latency in microseconds. |

## [◆ ](#gaadcb851b1bfb312ea0960918dc9f869e)pm\_policy\_latency\_request\_remove()

| void pm\_policy\_latency\_request\_remove | ( | struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \* | *req* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[policy.h](policy_8h.md)>`

Remove a latency requirement.

Parameters
:   | req | Latency request. |
    | --- | --- |

## [◆ ](#ga6483bd320881d697de27493b4f2d92d1)pm\_policy\_latency\_request\_update()

| void pm\_policy\_latency\_request\_update | ( | struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \* | *req*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *value\_us* ) |

`#include <[policy.h](policy_8h.md)>`

Update a latency requirement.

Parameters
:   | req | Latency request. |
    | --- | --- |
    | value\_us | New maximum allowed latency in microseconds. |

## [◆ ](#gabbb379f8572f164addafe93ad3468f3d)pm\_policy\_state\_lock\_get()

| void pm\_policy\_state\_lock\_get | ( | enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) | *state*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *substate\_id* ) |

`#include <[policy.h](policy_8h.md)>`

Increase a power state lock counter.

A power state will not be allowed on the first call of [pm\_policy\_state\_lock\_get()](#gabbb379f8572f164addafe93ad3468f3d). Subsequent calls will just increase a reference count, thus meaning this API can be safely used concurrently. A state will be allowed again after [pm\_policy\_state\_lock\_put()](#ga12f4d121aa8be0eb66381713b481a8b1) is called as many times as [pm\_policy\_state\_lock\_get()](#gabbb379f8572f164addafe93ad3468f3d).

Note that the PM\_STATE\_ACTIVE state is always allowed, so calling this API with PM\_STATE\_ACTIVE will have no effect.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Power state. |
    | --- | --- |
    | substate\_id | Power substate ID. Use PM\_ALL\_SUBSTATES to affect all the substates in the given power state. |

See also
:   [pm\_policy\_state\_lock\_put()](#ga12f4d121aa8be0eb66381713b481a8b1)

## [◆ ](#ga39f14c8509dee55ed084b4111584b766)pm\_policy\_state\_lock\_is\_active()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pm\_policy\_state\_lock\_is\_active | ( | enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) | *state*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *substate\_id* ) |

`#include <[policy.h](policy_8h.md)>`

Check if a power state lock is active (not allowed).

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Power state. |
    | --- | --- |
    | substate\_id | Power substate ID. Use PM\_ALL\_SUBSTATES to affect all the substates in the given power state. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if power state lock is active. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if power state lock is not active. |

## [◆ ](#ga12f4d121aa8be0eb66381713b481a8b1)pm\_policy\_state\_lock\_put()

| void pm\_policy\_state\_lock\_put | ( | enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) | *state*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *substate\_id* ) |

`#include <[policy.h](policy_8h.md)>`

Decrease a power state lock counter.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Power state. |
    | --- | --- |
    | substate\_id | Power substate ID. Use PM\_ALL\_SUBSTATES to affect all the substates in the given power state. |

See also
:   [pm\_policy\_state\_lock\_get()](#gabbb379f8572f164addafe93ad3468f3d)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
