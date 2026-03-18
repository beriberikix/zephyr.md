---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structopenthread__state__changed__cb.html
original_path: doxygen/html/structopenthread__state__changed__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

openthread\_state\_changed\_cb Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [OpenThread L2 abstraction layer](group__openthread.md)

OpenThread state change callback.
[More...](#details)

`#include <[openthread.h](openthread_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [state\_changed\_cb](#a79ddff2e80e29fd5f931c81902d4b740) )(otChangedFlags [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct openthread\_context \*ot\_context, void \*[user\_data](#afdcd1fd3a9604bfe7754a66d5e446745)) |
|  | Callback for notifying configuration or state changes. |
| void \* | [user\_data](#afdcd1fd3a9604bfe7754a66d5e446745) |
|  | User data if required. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a362bd80c0be9bc5d5fb27a8912c91b8b) |
|  | Internally used field for list handling. |

## Detailed Description

OpenThread state change callback.

OpenThread state change callback structure

Used to register a callback in the callback list. As many callbacks as needed can be added as long as each of them are unique pointers of struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md "OpenThread state change callback."). Beware such structure should not be allocated on stack.

## Field Documentation

## [◆ ](#a362bd80c0be9bc5d5fb27a8912c91b8b)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) openthread\_state\_changed\_cb::node |
| --- |

Internally used field for list handling.

- user must not directly modify

## [◆ ](#a79ddff2e80e29fd5f931c81902d4b740)state\_changed\_cb

| void(\* openthread\_state\_changed\_cb::state\_changed\_cb) (otChangedFlags [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct openthread\_context \*ot\_context, void \*[user\_data](#afdcd1fd3a9604bfe7754a66d5e446745)) |
| --- |

Callback for notifying configuration or state changes.

Parameters
:   | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | as per OpenThread otStateChangedCallback() aFlags parameter. See [https://openthread.io/reference/group/api-instance#otstatechangedcallback](https://openthread.io/reference/group/api-instance#otstatechangedcallback) |
    | --- | --- |
    | ot\_context | the OpenThread context the callback is registered with. |
    | [user\_data](#afdcd1fd3a9604bfe7754a66d5e446745) | Data to pass to the callback. |

## [◆ ](#afdcd1fd3a9604bfe7754a66d5e446745)user\_data

| void\* openthread\_state\_changed\_cb::user\_data |
| --- |

User data if required.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[openthread.h](openthread_8h_source.md)

- [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
