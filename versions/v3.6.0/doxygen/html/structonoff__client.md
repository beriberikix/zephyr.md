---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structonoff__client.html
original_path: doxygen/html/structonoff__client.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

onoff\_client Struct Reference

[Kernel APIs](group__kernel__apis.md) » [On-Off Service APIs](group__resource__mgmt__onoff__apis.md)

State associated with a client of an on-off service.
[More...](#details)

`#include <[onoff.h](onoff_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [sys\_notify](structsys__notify.md) | [notify](#a40f8029732122f7887bb021de362742c) |
|  | Notification configuration. |

## Detailed Description

State associated with a client of an on-off service.

Objects of this type are allocated by a client, which is responsible for zero-initializing the node field and invoking the appropriate [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") init function to configure notification.

Control of the object content transfers to the service provider when a pointer to the object is passed to any on-off manager function. While the service provider controls the object the client must not change any object fields. Control reverts to the client concurrent with release of the owned [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") structure, or when indicated by an [onoff\_cancel()](group__resource__mgmt__onoff__apis.md#gad05d32f1548e56b508628e84ba101554 "Attempt to cancel an in-progress client operation.") return value.

After control has reverted to the client the notify field must be reinitialized for the next operation.

## Field Documentation

## [◆ ](#a40f8029732122f7887bb021de362742c)notify

| struct [sys\_notify](structsys__notify.md) onoff\_client::notify |
| --- |

Notification configuration.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[onoff.h](onoff_8h_source.md)

- [onoff\_client](structonoff__client.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
