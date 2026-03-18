---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/kernel_2smp_8h.html
original_path: doxygen/html/kernel_2smp_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](kernel_2smp_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [smp\_init\_fn](#abc49de5bf9e70f48e39f41c413f7cc74)) (void \*arg) |

| Functions | |
| --- | --- |
| void | [k\_smp\_cpu\_start](#a33eb24503679583d853db1c4dc7e3812) (int id, [smp\_init\_fn](#abc49de5bf9e70f48e39f41c413f7cc74) fn, void \*arg) |
|  | Start a CPU. |
| void | [k\_smp\_cpu\_resume](#a39b4f48857baef688ee646bac36c882d) (int id, [smp\_init\_fn](#abc49de5bf9e70f48e39f41c413f7cc74) fn, void \*arg, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reinit\_timer, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) invoke\_sched) |
|  | Resume a previously suspended CPU. |

## Typedef Documentation

## [◆ ](#abc49de5bf9e70f48e39f41c413f7cc74)smp\_init\_fn

| typedef void(\* smp\_init\_fn) (void \*arg) |
| --- |

## Function Documentation

## [◆ ](#a39b4f48857baef688ee646bac36c882d)k\_smp\_cpu\_resume()

| void k\_smp\_cpu\_resume | ( | int | *id*, |
| --- | --- | --- | --- |
|  |  | [smp\_init\_fn](#abc49de5bf9e70f48e39f41c413f7cc74) | *fn*, |
|  |  | void \* | *arg*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *reinit\_timer*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *invoke\_sched* ) |

Resume a previously suspended CPU.

This function works like [k\_smp\_cpu\_start](#a33eb24503679583d853db1c4dc7e3812), but does not re-initialize the kernel's internal tracking data for the target CPU. Therefore, [k\_smp\_cpu\_start](#a33eb24503679583d853db1c4dc7e3812) must have previously been called for the target CPU, and it must have verifiably reached an idle/off state (detection of which must be provided by the platform layers). It may be used in cases where platform layers require, for example, that data on the interrupt or idle stack be preserved.

Note
:   This function must not be used on currently running CPU. The target CPU must be in suspended state, or in certain architectural [state(s)](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) where the CPU is permitted to go through the resume process. Detection of such [state(s)](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) must be provided by the platform layers.

Parameters
:   | id | ID of target CPU. |
    | --- | --- |
    | fn | Function to be called before resuming context. |
    | arg | Argument to *fn*. |
    | reinit\_timer | True if timer needs to be re-initialized. |
    | invoke\_sched | True if scheduler is invoked after the CPU has started. |

## [◆ ](#a33eb24503679583d853db1c4dc7e3812)k\_smp\_cpu\_start()

| void k\_smp\_cpu\_start | ( | int | *id*, |
| --- | --- | --- | --- |
|  |  | [smp\_init\_fn](#abc49de5bf9e70f48e39f41c413f7cc74) | *fn*, |
|  |  | void \* | *arg* ) |

Start a CPU.

This routine is used to manually start the CPU specified by *id*. It may be called to restart a CPU that had been stopped or powered down, as well as some other scenario. After the CPU has finished initialization, the CPU will be ready to participate in thread scheduling and execution.

Note
:   This function must not be used on currently running CPU. The target CPU must be in off state, or in certain architectural [state(s)](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) where the CPU is permitted to go through the power up process. Detection of such [state(s)](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) must be provided by the platform layers.
:   This initializes per-CPU kernel structs and also initializes timers needed for MP operations. Use [k\_smp\_cpu\_resume](#a39b4f48857baef688ee646bac36c882d) if these are not desired.

Parameters
:   | id | ID of target CPU. |
    | --- | --- |
    | fn | Function to be called before letting scheduler run. |
    | arg | Argument to *fn*. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [smp.h](kernel_2smp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
