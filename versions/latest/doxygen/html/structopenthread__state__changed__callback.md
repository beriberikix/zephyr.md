---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structopenthread__state__changed__callback.html
original_path: doxygen/html/structopenthread__state__changed__callback.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

openthread\_state\_changed\_callback Struct Reference

OpenThread state change callback.
[More...](#details)

`#include <[/tmp/zephyrproject/zephyr/modules/openthread/include/openthread.h](modules_2openthread_2include_2openthread_8h_source.md)>`

| Data Fields | |
| --- | --- |
| otStateChangedCallback | [otCallback](#a8bf9761ba1e70d9bfcdcda108109d52f) |
|  | Callback for notifying configuration or state changes. |
| void \* | [user\_data](#ae5a1648859eeb3df7a285becf33c8219) |
|  | User data if required. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a5c36164b8db65f2493c17a61c3434128) |
|  | Internally used field for list handling. |

## Detailed Description

OpenThread state change callback.

OpenThread state change callback structure

Used to register a callback in the callback list. As many callbacks as needed can be added as long as each of them are unique pointers of struct [openthread\_state\_changed\_callback](structopenthread__state__changed__callback.md "OpenThread state change callback.").

Note
:   You may destroy the object only after it is unregistered from the callback list.

## Field Documentation

## [◆ ](#a5c36164b8db65f2493c17a61c3434128)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) openthread\_state\_changed\_callback::node |
| --- |

Internally used field for list handling.

- user must not directly modify

## [◆ ](#a8bf9761ba1e70d9bfcdcda108109d52f)otCallback

| otStateChangedCallback openthread\_state\_changed\_callback::otCallback |
| --- |

Callback for notifying configuration or state changes.

Parameters
:   | [otCallback](#a8bf9761ba1e70d9bfcdcda108109d52f) | OpenThread callback to register. See [https://openthread.io/reference/group/api-instance#otstatechangedcallback](https://openthread.io/reference/group/api-instance#otstatechangedcallback) for details. |
    | --- | --- |

## [◆ ](#ae5a1648859eeb3df7a285becf33c8219)user\_data

| void\* openthread\_state\_changed\_callback::user\_data |
| --- |

User data if required.

---

The documentation for this struct was generated from the following file:

- /tmp/zephyrproject/zephyr/modules/openthread/include/[openthread.h](modules_2openthread_2include_2openthread_8h_source.md)

- [openthread\_state\_changed\_callback](structopenthread__state__changed__callback.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
