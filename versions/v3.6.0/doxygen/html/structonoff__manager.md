---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structonoff__manager.html
original_path: doxygen/html/structonoff__manager.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

onoff\_manager Struct Reference

[Kernel APIs](group__kernel__apis.md) » [On-Off Service APIs](group__resource__mgmt__onoff__apis.md)

State associated with an on-off manager.
[More...](#details)

`#include <[onoff.h](onoff_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [clients](#a3eb50568d4b7c83597a194c7facd383b) |
|  | List of clients waiting for request or reset completion notifications. |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [monitors](#a501bb2c1c84293b1e4fbd011c62f5c69) |
|  | List of monitors to be notified of state changes including errors and transition completion. |
| const struct [onoff\_transitions](structonoff__transitions.md) \* | [transitions](#adcbe3b90e1618d3e7e223da106790457) |
|  | Transition functions. |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#af87f180f0494f02054e33086ee940493) |
|  | Mutex protection for other fields. |
| int | [last\_res](#a5f555de973d72ba1889655c3342c8dc7) |
|  | The result of the last transition. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#a50d51cd3700e610b2f650607373afeb4) |
|  | Flags identifying the service state. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [refs](#a43c40829b6acd4c91517a34ebd371dd9) |
|  | Number of active clients for the service. |

## Detailed Description

State associated with an on-off manager.

No fields in this structure are intended for use by service providers or clients. The state is to be initialized once, using [onoff\_manager\_init()](group__resource__mgmt__onoff__apis.md#ga73d52272baab03d1df2f267429390978 "Initialize an on-off service to off state."), when the service provider is initialized. In case of error it may be reset through the [onoff\_reset()](group__resource__mgmt__onoff__apis.md#gaf7b46a5f2e43d1bab193c18b8f6c8ba8 "Clear errors on an on-off service and reset it to its off state.") API.

## Field Documentation

## [◆ ](#a3eb50568d4b7c83597a194c7facd383b)clients

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) onoff\_manager::clients |
| --- |

List of clients waiting for request or reset completion notifications.

## [◆ ](#a50d51cd3700e610b2f650607373afeb4)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) onoff\_manager::flags |
| --- |

Flags identifying the service state.

## [◆ ](#a5f555de973d72ba1889655c3342c8dc7)last\_res

| int onoff\_manager::last\_res |
| --- |

The result of the last transition.

## [◆ ](#af87f180f0494f02054e33086ee940493)lock

| struct [k\_spinlock](structk__spinlock.md) onoff\_manager::lock |
| --- |

Mutex protection for other fields.

## [◆ ](#a501bb2c1c84293b1e4fbd011c62f5c69)monitors

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) onoff\_manager::monitors |
| --- |

List of monitors to be notified of state changes including errors and transition completion.

## [◆ ](#a43c40829b6acd4c91517a34ebd371dd9)refs

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) onoff\_manager::refs |
| --- |

Number of active clients for the service.

## [◆ ](#adcbe3b90e1618d3e7e223da106790457)transitions

| const struct [onoff\_transitions](structonoff__transitions.md)\* onoff\_manager::transitions |
| --- |

Transition functions.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[onoff.h](onoff_8h_source.md)

- [onoff\_manager](structonoff__manager.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
