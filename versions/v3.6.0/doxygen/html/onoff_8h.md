---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/onoff_8h.html
original_path: doxygen/html/onoff_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

onoff.h File Reference

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/notify.h](notify_8h_source.md)>`

[Go to the source code of this file.](onoff_8h_source.md)

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
| #define | [ONOFF\_FLAG\_ERROR](group__resource__mgmt__onoff__apis.md#ga9ae0c3528254b10f5e1a9743aea234dd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag indicating an error state. |
| #define | [ONOFF\_STATE\_MASK](group__resource__mgmt__onoff__apis.md#ga0e06eafdf5021ce970027f20fc001acc) |
|  | Mask used to isolate bits defining the service state. |
| #define | [ONOFF\_STATE\_OFF](group__resource__mgmt__onoff__apis.md#gab9e5380dce026a5dfea770f999400484)   0U |
|  | Value exposed by ONOFF\_STATE\_MASK when service is off. |
| #define | [ONOFF\_STATE\_ON](group__resource__mgmt__onoff__apis.md#ga7cd0fba52afba2e337ab7c830d3058d7)   ONOFF\_FLAG\_ONOFF |
|  | Value exposed by ONOFF\_STATE\_MASK when service is on. |
| #define | [ONOFF\_STATE\_ERROR](group__resource__mgmt__onoff__apis.md#gac005a25d149568208a6fbaa2ceaa1ac6)   [ONOFF\_FLAG\_ERROR](group__resource__mgmt__onoff__apis.md#ga9ae0c3528254b10f5e1a9743aea234dd) |
|  | Value exposed by ONOFF\_STATE\_MASK when the service is in an error state (and not in the process of resetting its state). |
| #define | [ONOFF\_STATE\_TO\_ON](group__resource__mgmt__onoff__apis.md#gac4a0d8a7b501adb011aa1c4c4da3f2a3)   (ONOFF\_FLAG\_TRANSITION | [ONOFF\_STATE\_ON](group__resource__mgmt__onoff__apis.md#ga7cd0fba52afba2e337ab7c830d3058d7)) |
|  | Value exposed by ONOFF\_STATE\_MASK when service is transitioning to on. |
| #define | [ONOFF\_STATE\_TO\_OFF](group__resource__mgmt__onoff__apis.md#ga235a04122763f1a2cbb849c56df65d26)   (ONOFF\_FLAG\_TRANSITION | [ONOFF\_STATE\_OFF](group__resource__mgmt__onoff__apis.md#gab9e5380dce026a5dfea770f999400484)) |
|  | Value exposed by ONOFF\_STATE\_MASK when service is transitioning to off. |
| #define | [ONOFF\_STATE\_RESETTING](group__resource__mgmt__onoff__apis.md#gacc0438b5c81c639e0035ada5caec940b)   (ONOFF\_FLAG\_TRANSITION | [ONOFF\_STATE\_ERROR](group__resource__mgmt__onoff__apis.md#gac005a25d149568208a6fbaa2ceaa1ac6)) |
|  | Value exposed by ONOFF\_STATE\_MASK when service is in the process of resetting. |
| #define | [ONOFF\_TRANSITIONS\_INITIALIZER](group__resource__mgmt__onoff__apis.md#ga8c1171a844ef1d9d6541d342124492ff)(\_start, \_stop, \_reset) |
|  | Initializer for a [onoff\_transitions](structonoff__transitions.md "On-off service transition functions.") object. |
| #define | [ONOFF\_CLIENT\_EXTENSION\_POS](group__resource__mgmt__onoff__apis.md#gad61d053ae4e9ee12efe8d37372a16c63)   [SYS\_NOTIFY\_EXTENSION\_POS](notify_8h.md#aa22143622004e478668cdd98a2e04357) |
|  | Identify region of [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") flags available for containing services. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [onoff\_notify\_fn](group__resource__mgmt__onoff__apis.md#gac05f7946a14fa23ef67212eba30c98ac)) (struct [onoff\_manager](structonoff__manager.md) \*mgr, int res) |
|  | Signature used to notify an on-off manager that a transition has completed. |
| typedef void(\* | [onoff\_transition\_fn](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1)) (struct [onoff\_manager](structonoff__manager.md) \*mgr, [onoff\_notify\_fn](group__resource__mgmt__onoff__apis.md#gac05f7946a14fa23ef67212eba30c98ac) notify) |
|  | Signature used by service implementations to effect a transition. |
| typedef void(\* | [onoff\_client\_callback](group__resource__mgmt__onoff__apis.md#ga41b94526182c5772d7adebb1d1745068)) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_client](structonoff__client.md) \*cli, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), int res) |
|  | Signature used to notify an on-off service client of the completion of an operation. |
| typedef void(\* | [onoff\_monitor\_callback](group__resource__mgmt__onoff__apis.md#gaee41b38d408cf5f5efc9cd007f377545)) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_monitor](structonoff__monitor.md) \*mon, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), int res) |
|  | Signature used to notify a monitor of an onoff service of errors or completion of a state transition. |

| Functions | |
| --- | --- |
| int | [onoff\_manager\_init](group__resource__mgmt__onoff__apis.md#ga73d52272baab03d1df2f267429390978) (struct [onoff\_manager](structonoff__manager.md) \*mgr, const struct [onoff\_transitions](structonoff__transitions.md) \*transitions) |
|  | Initialize an on-off service to off state. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [onoff\_has\_error](group__resource__mgmt__onoff__apis.md#ga347efda0aa0305c134224c59677fa6cb) (const struct [onoff\_manager](structonoff__manager.md) \*mgr) |
|  | Test whether an on-off service has recorded an error. |
| int | [onoff\_request](group__resource__mgmt__onoff__apis.md#ga20dcb358e405deb87b7fbb7846ef9d68) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_client](structonoff__client.md) \*cli) |
|  | Request a reservation to use an on-off service. |
| int | [onoff\_release](group__resource__mgmt__onoff__apis.md#ga19da5359f10fa2e2eb034d1e72235ea6) (struct [onoff\_manager](structonoff__manager.md) \*mgr) |
|  | Release a reserved use of an on-off service. |
| int | [onoff\_cancel](group__resource__mgmt__onoff__apis.md#gad05d32f1548e56b508628e84ba101554) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_client](structonoff__client.md) \*cli) |
|  | Attempt to cancel an in-progress client operation. |
| static int | [onoff\_cancel\_or\_release](group__resource__mgmt__onoff__apis.md#ga7aac2aeb66907ec920557f0ef67d6795) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_client](structonoff__client.md) \*cli) |
|  | Helper function to safely cancel a request. |
| int | [onoff\_reset](group__resource__mgmt__onoff__apis.md#gaf7b46a5f2e43d1bab193c18b8f6c8ba8) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_client](structonoff__client.md) \*cli) |
|  | Clear errors on an on-off service and reset it to its off state. |
| int | [onoff\_monitor\_register](group__resource__mgmt__onoff__apis.md#ga9897d93359fe58359c0204da46b4c01e) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_monitor](structonoff__monitor.md) \*mon) |
|  | Add a monitor of state changes for a manager. |
| int | [onoff\_monitor\_unregister](group__resource__mgmt__onoff__apis.md#ga50a51da8e701a3f19f242af5183d807a) (struct [onoff\_manager](structonoff__manager.md) \*mgr, struct [onoff\_monitor](structonoff__monitor.md) \*mon) |
|  | Remove a monitor of state changes from a manager. |
| int | [onoff\_sync\_lock](group__resource__mgmt__onoff__apis.md#ga174cadf7dfa5d3c4dc5c8185994f3825) (struct [onoff\_sync\_service](structonoff__sync__service.md) \*srv, [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) \*keyp) |
|  | Lock a synchronous onoff service and provide its state. |
| int | [onoff\_sync\_finalize](group__resource__mgmt__onoff__apis.md#gae3331bdad9d03309ee78e86c487b7f26) (struct [onoff\_sync\_service](structonoff__sync__service.md) \*srv, [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) key, struct [onoff\_client](structonoff__client.md) \*cli, int res, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) on) |
|  | Process the completion of a transition in a synchronous service and release lock. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [onoff.h](onoff_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
