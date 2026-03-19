---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__sys__notify__apis.html
original_path: doxygen/html/group__sys__notify__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Asynchronous Notification APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_notify](structsys__notify.md) |
|  | State associated with notification for an asynchronous operation. [More...](structsys__notify.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [sys\_notify\_generic\_callback](#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499)) () |
|  | Generic signature used to notify of result completion by callback. |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_notify\_get\_method](#ga19a2ca050ef4fcd4fac70e73c3fd3514) (const struct [sys\_notify](structsys__notify.md) \*notify) |
| int | [sys\_notify\_validate](#ga71a9ccb690151020a6abea2ec9ffc667) (struct [sys\_notify](structsys__notify.md) \*notify) |
|  | Validate and initialize the notify structure. |
| [sys\_notify\_generic\_callback](#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499) | [sys\_notify\_finalize](#ga424b1c94c1010bdc4170cf06c7f2ec72) (struct [sys\_notify](structsys__notify.md) \*notify, int res) |
|  | Record and signal the operation completion. |
| static int | [sys\_notify\_fetch\_result](#ga823397b1917e10593d606daf3ec06a65) (const struct [sys\_notify](structsys__notify.md) \*notify, int \*result) |
|  | Check for and read the result of an asynchronous operation. |
| static void | [sys\_notify\_init\_spinwait](#gad1a5c3e58ff962ab3cac743dde8c6c1e) (struct [sys\_notify](structsys__notify.md) \*notify) |
|  | Initialize a notify object for spin-wait notification. |
| static void | [sys\_notify\_init\_signal](#ga30f9eff4b20b7d637a3a1df5f4cb38f8) (struct [sys\_notify](structsys__notify.md) \*notify, struct [k\_poll\_signal](structk__poll__signal.md) \*sigp) |
|  | Initialize a notify object for (k\_poll) signal notification. |
| static void | [sys\_notify\_init\_callback](#gaa9f31f78c03f48a3c649bbac15cc3a6c) (struct [sys\_notify](structsys__notify.md) \*notify, [sys\_notify\_generic\_callback](#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499) handler) |
|  | Initialize a notify object for callback notification. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_notify\_uses\_callback](#ga9772f8b356685acd707bd905860a2ca7) (const struct [sys\_notify](structsys__notify.md) \*notify) |
|  | Detect whether a particular notification uses a callback. |

## Detailed Description

## Typedef Documentation

## [◆ ](#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499)sys\_notify\_generic\_callback

| typedef void(\* sys\_notify\_generic\_callback) () |
| --- |

`#include <[notify.h](notify_8h.md)>`

Generic signature used to notify of result completion by callback.

Functions with this role may be invoked from any context including pre-kernel, ISR, or cooperative or pre-emptible threads. Compatible functions must be isr-ok and not sleep.

Parameters that should generally be passed to such functions include:

- a pointer to a specific client request structure, i.e. the one that contains the [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") structure.
- the result of the operation, either as passed to [sys\_notify\_finalize()](#ga424b1c94c1010bdc4170cf06c7f2ec72) or extracted afterwards using [sys\_notify\_fetch\_result()](#ga823397b1917e10593d606daf3ec06a65). Expected values are service-specific, but the value shall be non-negative if the operation succeeded, and negative if the operation failed.

## Function Documentation

## [◆ ](#ga823397b1917e10593d606daf3ec06a65)sys\_notify\_fetch\_result()

| | int sys\_notify\_fetch\_result | ( | const struct [sys\_notify](structsys__notify.md) \* | *notify*, | | --- | --- | --- | --- | |  |  | int \* | *result* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[notify.h](notify_8h.md)>`

Check for and read the result of an asynchronous operation.

Parameters
:   | notify | pointer to the object used to specify asynchronous function behavior and store completion information. |
    | --- | --- |
    | result | pointer to storage for the result of the operation. The result is stored only if the operation has completed. |

Return values
:   | 0 | if the operation has completed. |
    | --- | --- |
    | -EAGAIN | if the operation has not completed. |

## [◆ ](#ga424b1c94c1010bdc4170cf06c7f2ec72)sys\_notify\_finalize()

| [sys\_notify\_generic\_callback](#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499) sys\_notify\_finalize | ( | struct [sys\_notify](structsys__notify.md) \* | *notify*, |
| --- | --- | --- | --- |
|  |  | int | *res* ) |

`#include <[notify.h](notify_8h.md)>`

Record and signal the operation completion.

Parameters
:   | notify | pointer to the notification state structure. |
    | --- | --- |
    | res | the result of the operation. Expected values are service-specific, but the value shall be non-negative if the operation succeeded, and negative if the operation failed. |

Returns
:   If the notification is to be done by callback this returns the generic version of the function to be invoked. The caller must immediately invoke that function with whatever arguments are expected by the callback. If notification is by spin-wait or signal, the notification has been completed by the point this function returns, and a null pointer is returned.

## [◆ ](#ga19a2ca050ef4fcd4fac70e73c3fd3514)sys\_notify\_get\_method()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_notify\_get\_method | ( | const struct [sys\_notify](structsys__notify.md) \* | *notify* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[notify.h](notify_8h.md)>`

## [◆ ](#gaa9f31f78c03f48a3c649bbac15cc3a6c)sys\_notify\_init\_callback()

| | void sys\_notify\_init\_callback | ( | struct [sys\_notify](structsys__notify.md) \* | *notify*, | | --- | --- | --- | --- | |  |  | [sys\_notify\_generic\_callback](#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499) | *handler* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[notify.h](notify_8h.md)>`

Initialize a notify object for callback notification.

Clients that use this initialization will be notified of the completion of operations through the provided callback. Note that callbacks may be invoked from various contexts depending on the specific service; see [sys\_notify\_generic\_callback](#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499).

On completion of the operation the client object must be reinitialized before it can be re-used.

Parameters
:   | notify | pointer to the notification configuration object. |
    | --- | --- |
    | handler | a function pointer to use for notification. |

## [◆ ](#ga30f9eff4b20b7d637a3a1df5f4cb38f8)sys\_notify\_init\_signal()

| | void sys\_notify\_init\_signal | ( | struct [sys\_notify](structsys__notify.md) \* | *notify*, | | --- | --- | --- | --- | |  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sigp* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[notify.h](notify_8h.md)>`

Initialize a notify object for (k\_poll) signal notification.

Clients that use this initialization will be notified of the completion of operations through the provided signal.

On completion of the operation the client object must be reinitialized before it can be re-used.

Note
:   This capability is available only when `CONFIG_POLL` is selected.

Parameters
:   | notify | pointer to the notification configuration object. |
    | --- | --- |
    | sigp | pointer to the signal to use for notification. The value must not be null. The signal must be reset before the client object is passed to the on-off service API. |

## [◆ ](#gad1a5c3e58ff962ab3cac743dde8c6c1e)sys\_notify\_init\_spinwait()

| | void sys\_notify\_init\_spinwait | ( | struct [sys\_notify](structsys__notify.md) \* | *notify* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[notify.h](notify_8h.md)>`

Initialize a notify object for spin-wait notification.

Clients that use this initialization receive no asynchronous notification, and instead must periodically check for completion using [sys\_notify\_fetch\_result()](#ga823397b1917e10593d606daf3ec06a65).

On completion of the operation the client object must be reinitialized before it can be re-used.

Parameters
:   | notify | pointer to the notification configuration object. |
    | --- | --- |

## [◆ ](#ga9772f8b356685acd707bd905860a2ca7)sys\_notify\_uses\_callback()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_notify\_uses\_callback | ( | const struct [sys\_notify](structsys__notify.md) \* | *notify* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[notify.h](notify_8h.md)>`

Detect whether a particular notification uses a callback.

The generic handler does not capture the signature expected by the callback, and the translation to a service-specific callback must be provided by the service. This check allows abstracted services to reject callback notification requests when the service doesn't provide a translation function.

Returns
:   true if and only if a callback is to be used for notification.

## [◆ ](#ga71a9ccb690151020a6abea2ec9ffc667)sys\_notify\_validate()

| int sys\_notify\_validate | ( | struct [sys\_notify](structsys__notify.md) \* | *notify* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[notify.h](notify_8h.md)>`

Validate and initialize the notify structure.

This should be invoked at the start of any service-specific configuration validation. It ensures that the basic asynchronous notification configuration is consistent, and clears the result.

Note that this function does not validate extension bits (zeroed by async notify API init functions like [sys\_notify\_init\_callback()](#gaa9f31f78c03f48a3c649bbac15cc3a6c)). It may fail to recognize that an uninitialized structure has been passed because only method bits of flags are tested against method settings. To reduce the chance of accepting an uninitialized operation service validation of structures that contain an [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") instance should confirm that the extension bits are set or cleared as expected.

Return values
:   | 0 | on successful validation and reinitialization |
    | --- | --- |
    | -EINVAL | if the configuration is not valid. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
