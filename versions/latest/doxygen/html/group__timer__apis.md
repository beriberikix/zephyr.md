---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__timer__apis.html
original_path: doxygen/html/group__timer__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Timer APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [K\_TIMER\_DEFINE](#gaa267fcb0a2e18cd0da29e9f9612510a6)(name, expiry\_fn, stop\_fn) |
|  | Statically define and initialize a timer. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [k\_timer\_expiry\_t](#ga2915762e70454d98c73c179a45cafbde)) (struct k\_timer \*timer) |
|  | Timer expiry function type. |
| typedef void(\* | [k\_timer\_stop\_t](#ga106733712fc4e62b59bbe6a480bb988c)) (struct k\_timer \*timer) |
|  | Timer stop function type. |

| Functions | |
| --- | --- |
| void | [k\_timer\_init](#ga318c846a740b901e5d56876a47ad7f61) (struct k\_timer \*timer, [k\_timer\_expiry\_t](#ga2915762e70454d98c73c179a45cafbde) expiry\_fn, [k\_timer\_stop\_t](#ga106733712fc4e62b59bbe6a480bb988c) stop\_fn) |
|  | Initialize a timer. |
| void | [k\_timer\_start](#ga3ba70e9f059ff52fd2057ab89ea7f2ee) (struct k\_timer \*timer, [k\_timeout\_t](structk__timeout__t.md) duration, [k\_timeout\_t](structk__timeout__t.md) period) |
|  | Start a timer. |
| void | [k\_timer\_stop](#ga8d3e3356a10d36570e16f7920e4c8772) (struct k\_timer \*timer) |
|  | Stop a timer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_timer\_status\_get](#gad532f4834cd4cf8be27b089e6ea347ce) (struct k\_timer \*timer) |
|  | Read timer status. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_timer\_status\_sync](#ga81d6d95b7021e26ad4cab161318e04f2) (struct k\_timer \*timer) |
|  | Synchronize thread to timer expiration. |
| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [k\_timer\_expires\_ticks](#ga022b4cf5c8d0ee21b6a3b04fd425533f) (const struct k\_timer \*timer) |
|  | Get next expiration time of a timer, in system ticks. |
| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [k\_timer\_remaining\_ticks](#ga1176b36b960e786f68eaededf99a88b4) (const struct k\_timer \*timer) |
|  | Get time remaining before a timer next expires, in system ticks. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_timer\_remaining\_get](#ga6c6d8b0aa59bfa0f5924e95ccf756259) (struct k\_timer \*timer) |
|  | Get time remaining before a timer next expires. |
| void | [k\_timer\_user\_data\_set](#gadba1884961e790dd9c5d567de91cc7e2) (struct k\_timer \*timer, void \*user\_data) |
|  | Associate user-specific data with a timer. |
| void \* | [k\_timer\_user\_data\_get](#ga19a7d99a01a83828efd7f0d3bf2dd358) (const struct k\_timer \*timer) |
|  | Retrieve the user-specific data from a timer. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gaa267fcb0a2e18cd0da29e9f9612510a6)K\_TIMER\_DEFINE

| #define K\_TIMER\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *expiry\_fn*, |
|  |  |  | *stop\_fn* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(k\_timer, name) = \

Z\_TIMER\_INITIALIZER(name, expiry\_fn, stop\_fn)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

Statically define and initialize a timer.

The timer can be accessed outside the module where it is defined using:

extern struct k\_timer <name>;

Parameters
:   | name | Name of the timer variable. |
    | --- | --- |
    | expiry\_fn | Function to invoke each time the timer expires. |
    | stop\_fn | Function to invoke if the timer is stopped while running. |

## Typedef Documentation

## [◆ ](#ga2915762e70454d98c73c179a45cafbde)k\_timer\_expiry\_t

| typedef void(\* k\_timer\_expiry\_t) (struct k\_timer \*timer) |
| --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Timer expiry function type.

A timer's expiry function is executed by the system clock interrupt handler each time the timer expires. The expiry function is optional, and is only invoked if the timer has been initialized with one.

Parameters
:   | timer | Address of timer. |
    | --- | --- |

## [◆ ](#ga106733712fc4e62b59bbe6a480bb988c)k\_timer\_stop\_t

| typedef void(\* k\_timer\_stop\_t) (struct k\_timer \*timer) |
| --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Timer stop function type.

A timer's stop function is executed if the timer is stopped prematurely. The function runs in the context of call that stops the timer. As [k\_timer\_stop()](#ga8d3e3356a10d36570e16f7920e4c8772) can be invoked from an ISR, the stop function must be callable from interrupt context (isr-ok).

The stop function is optional, and is only invoked if the timer has been initialized with one.

Parameters
:   | timer | Address of timer. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga022b4cf5c8d0ee21b6a3b04fd425533f)k\_timer\_expires\_ticks()

| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) k\_timer\_expires\_ticks | ( | const struct k\_timer \* | *timer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Get next expiration time of a timer, in system ticks.

This routine returns the future system uptime reached at the next time of expiration of the timer, in units of system ticks. If the timer is not running, current system time is returned.

Parameters
:   | timer | The timer object |
    | --- | --- |

Returns
:   Uptime of expiration, in ticks

## [◆ ](#ga318c846a740b901e5d56876a47ad7f61)k\_timer\_init()

| void k\_timer\_init | ( | struct k\_timer \* | *timer*, |
| --- | --- | --- | --- |
|  |  | [k\_timer\_expiry\_t](#ga2915762e70454d98c73c179a45cafbde) | *expiry\_fn*, |
|  |  | [k\_timer\_stop\_t](#ga106733712fc4e62b59bbe6a480bb988c) | *stop\_fn* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Initialize a timer.

This routine initializes a timer, prior to its first use.

Parameters
:   | timer | Address of timer. |
    | --- | --- |
    | expiry\_fn | Function to invoke each time the timer expires. |
    | stop\_fn | Function to invoke if the timer is stopped while running. |

## [◆ ](#ga6c6d8b0aa59bfa0f5924e95ccf756259)k\_timer\_remaining\_get()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_timer\_remaining\_get | ( | struct k\_timer \* | *timer* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Get time remaining before a timer next expires.

This routine computes the (approximate) time remaining before a running timer next expires. If the timer is not running, it returns zero.

Parameters
:   | timer | Address of timer. |
    | --- | --- |

Returns
:   Remaining time (in milliseconds).

## [◆ ](#ga1176b36b960e786f68eaededf99a88b4)k\_timer\_remaining\_ticks()

| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) k\_timer\_remaining\_ticks | ( | const struct k\_timer \* | *timer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Get time remaining before a timer next expires, in system ticks.

This routine computes the time remaining before a running timer next expires, in units of system ticks. If the timer is not running, it returns zero.

## [◆ ](#ga3ba70e9f059ff52fd2057ab89ea7f2ee)k\_timer\_start()

| void k\_timer\_start | ( | struct k\_timer \* | *timer*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *duration*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *period* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Start a timer.

This routine starts a timer, and resets its status to zero. The timer begins counting down using the specified duration and period values.

Attempting to start a timer that is already running is permitted. The timer's status is reset to zero and the timer begins counting down using the new duration and period values.

Parameters
:   | timer | Address of timer. |
    | --- | --- |
    | duration | Initial timer duration. |
    | period | Timer period. |

## [◆ ](#gad532f4834cd4cf8be27b089e6ea347ce)k\_timer\_status\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_timer\_status\_get | ( | struct k\_timer \* | *timer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Read timer status.

This routine reads the timer's status, which indicates the number of times it has expired since its status was last read.

Calling this routine resets the timer's status to zero.

Parameters
:   | timer | Address of timer. |
    | --- | --- |

Returns
:   Timer status.

## [◆ ](#ga81d6d95b7021e26ad4cab161318e04f2)k\_timer\_status\_sync()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_timer\_status\_sync | ( | struct k\_timer \* | *timer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Synchronize thread to timer expiration.

This routine blocks the calling thread until the timer's status is non-zero (indicating that it has expired at least once since it was last examined) or the timer is stopped. If the timer status is already non-zero, or the timer is already stopped, the caller continues without waiting.

Calling this routine resets the timer's status to zero.

This routine must not be used by interrupt handlers, since they are not allowed to block.

Parameters
:   | timer | Address of timer. |
    | --- | --- |

Returns
:   Timer status.

## [◆ ](#ga8d3e3356a10d36570e16f7920e4c8772)k\_timer\_stop()

| void k\_timer\_stop | ( | struct k\_timer \* | *timer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Stop a timer.

This routine stops a running timer prematurely. The timer's stop function, if one exists, is invoked by the caller.

Attempting to stop a timer that is not running is permitted, but has no effect on the timer.

Note
:   The stop handler has to be callable from ISRs if *k\_timer\_stop* is to be called from ISRs.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | timer | Address of timer. |
    | --- | --- |

## [◆ ](#ga19a7d99a01a83828efd7f0d3bf2dd358)k\_timer\_user\_data\_get()

| void \* k\_timer\_user\_data\_get | ( | const struct k\_timer \* | *timer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Retrieve the user-specific data from a timer.

Parameters
:   | timer | Address of timer. |
    | --- | --- |

Returns
:   The user data.

## [◆ ](#gadba1884961e790dd9c5d567de91cc7e2)k\_timer\_user\_data\_set()

| void k\_timer\_user\_data\_set | ( | struct k\_timer \* | *timer*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Associate user-specific data with a timer.

This routine records the *user\_data* with the *timer*, to be retrieved later.

It can be used e.g. in a timer handler shared across multiple subsystems to retrieve data specific to the subsystem this timer is associated with.

Parameters
:   | timer | Address of timer. |
    | --- | --- |
    | user\_data | User data to associate with the timer. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
