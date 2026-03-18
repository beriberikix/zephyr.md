---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/notify_8h.html
original_path: doxygen/html/notify_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

notify.h File Reference

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](notify_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_notify](structsys__notify.md) |
|  | State associated with notification for an asynchronous operation. [More...](structsys__notify.md#details) |
| union | [sys\_notify::method](unionsys__notify_1_1method.md) |

| Macros | |
| --- | --- |
| #define | [SYS\_NOTIFY\_METHOD\_COMPLETED](#ad408b122f7f121c0739ac09e3399baa4)   0 |
| #define | [SYS\_NOTIFY\_METHOD\_SPINWAIT](#a36fc74f78d421ddf0fe3dfd48d0e5a99)   1 |
| #define | [SYS\_NOTIFY\_METHOD\_SIGNAL](#aba2f89370639d6733ec8d75fadb44678)   2 |
| #define | [SYS\_NOTIFY\_METHOD\_CALLBACK](#a541b0198e2425c4dfa0d3e7abbdb9c60)   3 |
| #define | [SYS\_NOTIFY\_METHOD\_MASK](#a5f13b732e247f2903dcd82dc52f9d797)   0x03U |
| #define | [SYS\_NOTIFY\_METHOD\_POS](#a63af5c6773172a0f3881d11b7b2e58b6)   0 |
| #define | [SYS\_NOTIFY\_EXTENSION\_POS](#aa22143622004e478668cdd98a2e04357)   2 |
|  | Identify the region of [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") flags available for containing services. |
| #define | [SYS\_NOTIFY\_EXTENSION\_MASK](#a87d3145d44e9638070131dcfb21c6636)   (~[BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)([SYS\_NOTIFY\_EXTENSION\_POS](#aa22143622004e478668cdd98a2e04357))) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [sys\_notify\_generic\_callback](group__sys__notify__apis.md#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499)) () |
|  | Generic signature used to notify of result completion by callback. |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_notify\_get\_method](group__sys__notify__apis.md#ga19a2ca050ef4fcd4fac70e73c3fd3514) (const struct [sys\_notify](structsys__notify.md) \*notify) |
| int | [sys\_notify\_validate](group__sys__notify__apis.md#ga71a9ccb690151020a6abea2ec9ffc667) (struct [sys\_notify](structsys__notify.md) \*notify) |
|  | Validate and initialize the notify structure. |
| [sys\_notify\_generic\_callback](group__sys__notify__apis.md#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499) | [sys\_notify\_finalize](group__sys__notify__apis.md#ga424b1c94c1010bdc4170cf06c7f2ec72) (struct [sys\_notify](structsys__notify.md) \*notify, int res) |
|  | Record and signal the operation completion. |
| static int | [sys\_notify\_fetch\_result](group__sys__notify__apis.md#ga823397b1917e10593d606daf3ec06a65) (const struct [sys\_notify](structsys__notify.md) \*notify, int \*result) |
|  | Check for and read the result of an asynchronous operation. |
| static void | [sys\_notify\_init\_spinwait](group__sys__notify__apis.md#gad1a5c3e58ff962ab3cac743dde8c6c1e) (struct [sys\_notify](structsys__notify.md) \*notify) |
|  | Initialize a notify object for spin-wait notification. |
| static void | [sys\_notify\_init\_signal](group__sys__notify__apis.md#ga30f9eff4b20b7d637a3a1df5f4cb38f8) (struct [sys\_notify](structsys__notify.md) \*notify, struct [k\_poll\_signal](structk__poll__signal.md) \*sigp) |
|  | Initialize a notify object for (k\_poll) signal notification. |
| static void | [sys\_notify\_init\_callback](group__sys__notify__apis.md#gaa9f31f78c03f48a3c649bbac15cc3a6c) (struct [sys\_notify](structsys__notify.md) \*notify, [sys\_notify\_generic\_callback](group__sys__notify__apis.md#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499) handler) |
|  | Initialize a notify object for callback notification. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_notify\_uses\_callback](group__sys__notify__apis.md#ga9772f8b356685acd707bd905860a2ca7) (const struct [sys\_notify](structsys__notify.md) \*notify) |
|  | Detect whether a particular notification uses a callback. |

## Macro Definition Documentation

## [◆ ](#a87d3145d44e9638070131dcfb21c6636)SYS\_NOTIFY\_EXTENSION\_MASK

| #define SYS\_NOTIFY\_EXTENSION\_MASK   (~[BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)([SYS\_NOTIFY\_EXTENSION\_POS](#aa22143622004e478668cdd98a2e04357))) |
| --- |

## [◆ ](#aa22143622004e478668cdd98a2e04357)SYS\_NOTIFY\_EXTENSION\_POS

| #define SYS\_NOTIFY\_EXTENSION\_POS   2 |
| --- |

Identify the region of [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") flags available for containing services.

Bits of the flags field of the [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") structure at and above this position may be used by extensions to the [sys\_notify](structsys__notify.md "State associated with notification for an asynchronous operation.") structure.

These bits are intended for use by containing service implementations to record client-specific information. The bits are cleared by [sys\_notify\_validate()](group__sys__notify__apis.md#ga71a9ccb690151020a6abea2ec9ffc667 "Validate and initialize the notify structure."). Use of these does not imply that the flags field becomes public API.

## [◆ ](#a541b0198e2425c4dfa0d3e7abbdb9c60)SYS\_NOTIFY\_METHOD\_CALLBACK

| #define SYS\_NOTIFY\_METHOD\_CALLBACK   3 |
| --- |

## [◆ ](#ad408b122f7f121c0739ac09e3399baa4)SYS\_NOTIFY\_METHOD\_COMPLETED

| #define SYS\_NOTIFY\_METHOD\_COMPLETED   0 |
| --- |

## [◆ ](#a5f13b732e247f2903dcd82dc52f9d797)SYS\_NOTIFY\_METHOD\_MASK

| #define SYS\_NOTIFY\_METHOD\_MASK   0x03U |
| --- |

## [◆ ](#a63af5c6773172a0f3881d11b7b2e58b6)SYS\_NOTIFY\_METHOD\_POS

| #define SYS\_NOTIFY\_METHOD\_POS   0 |
| --- |

## [◆ ](#aba2f89370639d6733ec8d75fadb44678)SYS\_NOTIFY\_METHOD\_SIGNAL

| #define SYS\_NOTIFY\_METHOD\_SIGNAL   2 |
| --- |

## [◆ ](#a36fc74f78d421ddf0fe3dfd48d0e5a99)SYS\_NOTIFY\_METHOD\_SPINWAIT

| #define SYS\_NOTIFY\_METHOD\_SPINWAIT   1 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [notify.h](notify_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
