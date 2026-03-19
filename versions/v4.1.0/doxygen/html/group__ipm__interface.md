---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ipm__interface.html
original_path: doxygen/html/group__ipm__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

IPM Interface

[Device Driver APIs](group__io__interfaces.md)

IPM Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ipm\_driver\_api](structipm__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [ipm\_callback\_t](#ga20d7547dcea80bc769d5e323bd91cdaa)) (const struct [device](structdevice.md) \*ipmdev, void \*user\_data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, volatile void \*data) |
|  | Callback API for incoming IPM messages. |
| typedef int(\* | [ipm\_send\_t](#ga45fb35e92b26b04ed4c665d50912ff3b)) (const struct [device](structdevice.md) \*ipmdev, int wait, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, const void \*data, int size) |
|  | Callback API to send IPM messages. |
| typedef int(\* | [ipm\_max\_data\_size\_get\_t](#ga34c3a4782175068eda6443c521094a03)) (const struct [device](structdevice.md) \*ipmdev) |
|  | Callback API to get maximum data size. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [ipm\_max\_id\_val\_get\_t](#gaa50f765662f9d1dbea75902211de7000)) (const struct [device](structdevice.md) \*ipmdev) |
|  | Callback API to get the ID's maximum value. |
| typedef void(\* | [ipm\_register\_callback\_t](#ga8f7b338aa9f5d4aa1c218db412da562b)) (const struct [device](structdevice.md) \*port, [ipm\_callback\_t](#ga20d7547dcea80bc769d5e323bd91cdaa) cb, void \*user\_data) |
|  | Callback API upon registration. |
| typedef int(\* | [ipm\_set\_enabled\_t](#gab1faa1ebf47e2c12286bac0ce8be7784)) (const struct [device](structdevice.md) \*ipmdev, int enable) |
|  | Callback API upon enablement of interrupts. |
| typedef void(\* | [ipm\_complete\_t](#ga1aff2b36a9b7712a1fa743052282d440)) (const struct [device](structdevice.md) \*ipmdev) |
|  | Callback API upon command completion. |

| Functions | |
| --- | --- |
| int | [ipm\_send](#ga8f3fe21c1a4ffd3c38b67f81749af043) (const struct [device](structdevice.md) \*ipmdev, int wait, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, const void \*data, int size) |
|  | Try to send a message over the IPM device. |
| static void | [ipm\_register\_callback](#ga557b15bc8a353483ca55888dba27493b) (const struct [device](structdevice.md) \*ipmdev, [ipm\_callback\_t](#ga20d7547dcea80bc769d5e323bd91cdaa) cb, void \*user\_data) |
|  | Register a callback function for incoming messages. |
| int | [ipm\_max\_data\_size\_get](#ga0a11eecaa7254575ab6baf0783a18b5e) (const struct [device](structdevice.md) \*ipmdev) |
|  | Return the maximum number of bytes possible in an outbound message. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ipm\_max\_id\_val\_get](#ga168fd277b7819b639baa4e630c596a7f) (const struct [device](structdevice.md) \*ipmdev) |
|  | Return the maximum id value possible in an outbound message. |
| int | [ipm\_set\_enabled](#ga5884fa95cb38ddfe4493eb70dafebe8b) (const struct [device](structdevice.md) \*ipmdev, int enable) |
|  | Enable interrupts and callbacks for inbound channels. |
| void | [ipm\_complete](#ga53f785ecfac17b9fb2e5f3a9505c7fd2) (const struct [device](structdevice.md) \*ipmdev) |
|  | Signal asynchronous command completion. |

## Detailed Description

IPM Interface.

Since
:   1.0

Version
:   1.0.0

## Typedef Documentation

## [◆ ](#ga20d7547dcea80bc769d5e323bd91cdaa)ipm\_callback\_t

| typedef void(\* ipm\_callback\_t) (const struct [device](structdevice.md) \*ipmdev, void \*user\_data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, volatile void \*data) |
| --- |

`#include <[ipm.h](ipm_8h.md)>`

Callback API for incoming IPM messages.

These callbacks execute in interrupt context. Therefore, use only interrupt-safe APIS. Registration of callbacks is done via *ipm\_register\_callback*

Parameters
:   | ipmdev | Driver instance |
    | --- | --- |
    | user\_data | Pointer to some private data provided at registration time. |
    | id | Message type identifier. |
    | data | Message data pointer. The correct amount of data to read out must be inferred using the message id/upper level protocol. |

## [◆ ](#ga1aff2b36a9b7712a1fa743052282d440)ipm\_complete\_t

| typedef void(\* ipm\_complete\_t) (const struct [device](structdevice.md) \*ipmdev) |
| --- |

`#include <[ipm.h](ipm_8h.md)>`

Callback API upon command completion.

See *[ipm\_complete()](#ga53f785ecfac17b9fb2e5f3a9505c7fd2)* for argument definitions.

## [◆ ](#ga34c3a4782175068eda6443c521094a03)ipm\_max\_data\_size\_get\_t

| typedef int(\* ipm\_max\_data\_size\_get\_t) (const struct [device](structdevice.md) \*ipmdev) |
| --- |

`#include <[ipm.h](ipm_8h.md)>`

Callback API to get maximum data size.

See *[ipm\_max\_data\_size\_get()](#ga0a11eecaa7254575ab6baf0783a18b5e)* for argument definitions.

## [◆ ](#gaa50f765662f9d1dbea75902211de7000)ipm\_max\_id\_val\_get\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* ipm\_max\_id\_val\_get\_t) (const struct [device](structdevice.md) \*ipmdev) |
| --- |

`#include <[ipm.h](ipm_8h.md)>`

Callback API to get the ID's maximum value.

See *[ipm\_max\_id\_val\_get()](#ga168fd277b7819b639baa4e630c596a7f)* for argument definitions.

## [◆ ](#ga8f7b338aa9f5d4aa1c218db412da562b)ipm\_register\_callback\_t

| typedef void(\* ipm\_register\_callback\_t) (const struct [device](structdevice.md) \*port, [ipm\_callback\_t](#ga20d7547dcea80bc769d5e323bd91cdaa) cb, void \*user\_data) |
| --- |

`#include <[ipm.h](ipm_8h.md)>`

Callback API upon registration.

See *[ipm\_register\_callback()](#ga557b15bc8a353483ca55888dba27493b)* for argument definitions.

## [◆ ](#ga45fb35e92b26b04ed4c665d50912ff3b)ipm\_send\_t

| typedef int(\* ipm\_send\_t) (const struct [device](structdevice.md) \*ipmdev, int wait, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, const void \*data, int size) |
| --- |

`#include <[ipm.h](ipm_8h.md)>`

Callback API to send IPM messages.

See *[ipm\_send()](#ga8f3fe21c1a4ffd3c38b67f81749af043)* for argument definitions.

## [◆ ](#gab1faa1ebf47e2c12286bac0ce8be7784)ipm\_set\_enabled\_t

| typedef int(\* ipm\_set\_enabled\_t) (const struct [device](structdevice.md) \*ipmdev, int enable) |
| --- |

`#include <[ipm.h](ipm_8h.md)>`

Callback API upon enablement of interrupts.

See *[ipm\_set\_enabled()](#ga5884fa95cb38ddfe4493eb70dafebe8b)* for argument definitions.

## Function Documentation

## [◆ ](#ga53f785ecfac17b9fb2e5f3a9505c7fd2)ipm\_complete()

| void ipm\_complete | ( | const struct [device](structdevice.md) \* | *ipmdev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ipm.h](ipm_8h.md)>`

Signal asynchronous command completion.

Some IPM backends have an ability to deliver a command asynchronously. The callback will be invoked in interrupt context, but the message (including the provided data pointer) will stay "active" and unacknowledged until later code (presumably in thread mode) calls [ipm\_complete()](#ga53f785ecfac17b9fb2e5f3a9505c7fd2).

This function is, obviously, a noop on drivers without async support.

Parameters
:   | ipmdev | Driver instance pointer. |
    | --- | --- |

## [◆ ](#ga0a11eecaa7254575ab6baf0783a18b5e)ipm\_max\_data\_size\_get()

| int ipm\_max\_data\_size\_get | ( | const struct [device](structdevice.md) \* | *ipmdev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ipm.h](ipm_8h.md)>`

Return the maximum number of bytes possible in an outbound message.

IPM implementations vary on the amount of data that can be sent in a single message since the data payload is typically stored in registers.

Parameters
:   | ipmdev | Driver instance pointer. |
    | --- | --- |

Returns
:   Maximum possible size of a message in bytes.

## [◆ ](#ga168fd277b7819b639baa4e630c596a7f)ipm\_max\_id\_val\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ipm\_max\_id\_val\_get | ( | const struct [device](structdevice.md) \* | *ipmdev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ipm.h](ipm_8h.md)>`

Return the maximum id value possible in an outbound message.

Many IPM implementations store the message's ID in a register with some bits reserved for other uses.

Parameters
:   | ipmdev | Driver instance pointer. |
    | --- | --- |

Returns
:   Maximum possible value of a message ID.

## [◆ ](#ga557b15bc8a353483ca55888dba27493b)ipm\_register\_callback()

| | void ipm\_register\_callback | ( | const struct [device](structdevice.md) \* | *ipmdev*, | | --- | --- | --- | --- | |  |  | [ipm\_callback\_t](#ga20d7547dcea80bc769d5e323bd91cdaa) | *cb*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ipm.h](ipm_8h.md)>`

Register a callback function for incoming messages.

Parameters
:   | ipmdev | Driver instance pointer. |
    | --- | --- |
    | cb | Callback function to execute on incoming message interrupts. |
    | user\_data | Application-specific data pointer which will be passed to the callback function when executed. |

## [◆ ](#ga8f3fe21c1a4ffd3c38b67f81749af043)ipm\_send()

| int ipm\_send | ( | const struct [device](structdevice.md) \* | *ipmdev*, |
| --- | --- | --- | --- |
|  |  | int | *wait*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id*, |
|  |  | const void \* | *data*, |
|  |  | int | *size* ) |

`#include <[ipm.h](ipm_8h.md)>`

Try to send a message over the IPM device.

A message is considered consumed once the remote interrupt handler finishes. If there is deferred processing on the remote side, or if outgoing messages must be queued and wait on an event/semaphore, a high-level driver can implement that.

There are constraints on how much data can be sent or the maximum value of id. Use the *ipm\_max\_data\_size\_get* and *ipm\_max\_id\_val\_get* routines to determine them.

The *size* parameter is used only on the sending side to determine the amount of data to put in the message registers. It is not passed along to the receiving side. The upper-level protocol dictates the amount of data read back.

Parameters
:   | ipmdev | Driver instance |
    | --- | --- |
    | wait | If nonzero, busy-wait for remote to consume the message. The message is considered consumed once the remote interrupt handler finishes. If there is deferred processing on the remote side, or you would like to queue outgoing messages and wait on an event/semaphore, you can implement that in a high-level driver |
    | id | Message identifier. Values are constrained by *ipm\_max\_data\_size\_get* since many boards only allow for a subset of bits in a 32-bit register to store the ID. |
    | data | Pointer to the data sent in the message. |
    | size | Size of the data. |

Return values
:   | -EBUSY | If the remote hasn't yet read the last data sent. |
    | --- | --- |
    | -EMSGSIZE | If the supplied data size is unsupported by the driver. |
    | -EINVAL | If there was a bad parameter, such as: too-large id value. or the device isn't an outbound IPM channel. |
    | 0 | On success. |

## [◆ ](#ga5884fa95cb38ddfe4493eb70dafebe8b)ipm\_set\_enabled()

| int ipm\_set\_enabled | ( | const struct [device](structdevice.md) \* | *ipmdev*, |
| --- | --- | --- | --- |
|  |  | int | *enable* ) |

`#include <[ipm.h](ipm_8h.md)>`

Enable interrupts and callbacks for inbound channels.

Parameters
:   | ipmdev | Driver instance pointer. |
    | --- | --- |
    | enable | Set to 0 to disable and to nonzero to enable. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EINVAL | If it isn't an inbound channel. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
