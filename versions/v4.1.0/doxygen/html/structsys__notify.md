---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsys__notify.html
original_path: doxygen/html/structsys__notify.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_notify Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Asynchronous Notification APIs](group__sys__notify__apis.md)

State associated with notification for an asynchronous operation.
[More...](#details)

`#include <[notify.h](notify_8h_source.md)>`

| Data Structures | |
| --- | --- |
| union | [method](unionsys__notify_1_1method.md) |

| Data Fields | |
| --- | --- |
| union sys\_notify::method | [method](#a9c74bb70d56f0e5c809b26754c3b6fcd) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) volatile | [flags](#a0816d524409695b9b1480e7681507073) |
| int volatile | [result](#a6ea09c4e58d0eaaad3dd63ee4a311a21) |

## Detailed Description

State associated with notification for an asynchronous operation.

Objects of this type are allocated by a client, which must use an initialization function (e.g. [sys\_notify\_init\_signal()](group__sys__notify__apis.md#ga30f9eff4b20b7d637a3a1df5f4cb38f8 "Initialize a notify object for (k_poll) signal notification.")) to configure them. Generally the structure is a member of a service-specific client structure, such as [onoff\_client](structonoff__client.md "State associated with a client of an on-off service.").

Control of the containing object transfers to the service provider when a pointer to the object is passed to a service function that is documented to take control of the object, such as onoff\_service\_request(). While the service provider controls the object the client must not change any object fields. Control reverts to the client:

- if the call to the service API returns an error;
- when operation completion is posted. This may occur before the call to the service API returns.

Operation completion is technically posted when the flags field is updated so that [sys\_notify\_fetch\_result()](group__sys__notify__apis.md#ga823397b1917e10593d606daf3ec06a65 "Check for and read the result of an asynchronous operation.") returns success. This will happen before the signal is posted or callback is invoked. Note that although the manager will no longer reference the [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") object past this point, the containing object may have state that will be referenced within the callback. Where callbacks are used control of the containing object does not revert to the client until the callback has been invoked. (Re-use within the callback is explicitly permitted.)

After control has reverted to the client the notify object must be reinitialized for the next operation.

The content of this structure is not public API to clients: all configuration and inspection should be done with functions like [sys\_notify\_init\_callback()](group__sys__notify__apis.md#gaa9f31f78c03f48a3c649bbac15cc3a6c "Initialize a notify object for callback notification.") and [sys\_notify\_fetch\_result()](group__sys__notify__apis.md#ga823397b1917e10593d606daf3ec06a65 "Check for and read the result of an asynchronous operation."). However, services that use this structure may access certain fields directly.

## Field Documentation

## [◆ ](#a0816d524409695b9b1480e7681507073)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) volatile sys\_notify::flags |
| --- |

## [◆ ](#a9c74bb70d56f0e5c809b26754c3b6fcd)method

| union sys\_notify::method sys\_notify::method |
| --- |

## [◆ ](#a6ea09c4e58d0eaaad3dd63ee4a311a21)result

| int volatile sys\_notify::result |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[notify.h](notify_8h_source.md)

- [sys\_notify](structsys__notify.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
