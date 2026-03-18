---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structonoff__monitor.html
original_path: doxygen/html/structonoff__monitor.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

onoff\_monitor Struct Reference

[Kernel APIs](group__kernel__apis.md) » [On-Off Service APIs](group__resource__mgmt__onoff__apis.md)

Registration state for notifications of onoff service transitions.
[More...](#details)

`#include <[onoff.h](onoff_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a732a81eb0d9b36376b39b1a340fd1fe6) |
|  | Links the client into the set of waiting service users. |
| [onoff\_monitor\_callback](group__resource__mgmt__onoff__apis.md#gaee41b38d408cf5f5efc9cd007f377545) | [callback](#ab26d8ae8a0dac5e03549e2d9aca243a4) |
|  | Callback to be invoked on state change. |

## Detailed Description

Registration state for notifications of onoff service transitions.

Any given [onoff\_monitor](structonoff__monitor.md "Registration state for notifications of onoff service transitions.") structure can be associated with at most one [onoff\_manager](structonoff__manager.md "State associated with an on-off manager.") instance.

## Field Documentation

## [◆ ](#ab26d8ae8a0dac5e03549e2d9aca243a4)callback

| [onoff\_monitor\_callback](group__resource__mgmt__onoff__apis.md#gaee41b38d408cf5f5efc9cd007f377545) onoff\_monitor::callback |
| --- |

Callback to be invoked on state change.

This must not be null.

## [◆ ](#a732a81eb0d9b36376b39b1a340fd1fe6)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) onoff\_monitor::node |
| --- |

Links the client into the set of waiting service users.

This must be zero-initialized.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[onoff.h](onoff_8h_source.md)

- [onoff\_monitor](structonoff__monitor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
