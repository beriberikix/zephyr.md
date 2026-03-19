---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/irq__offload_8h.html
original_path: doxygen/html/irq__offload_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq\_offload.h File Reference

IRQ Offload interface.
[More...](#details)

[Go to the source code of this file.](irq__offload_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [irq\_offload\_routine\_t](#a5bcf9956ddbf5ea75619f0cef91e1214)) (const void \*parameter) |

| Functions | |
| --- | --- |
| void | [irq\_offload](#a429859dd7ac3d88a4b7ae858835847ce) ([irq\_offload\_routine\_t](#a5bcf9956ddbf5ea75619f0cef91e1214) routine, const void \*parameter) |
|  | Run a function in interrupt context. |

## Detailed Description

IRQ Offload interface.

## Typedef Documentation

## [◆ ](#a5bcf9956ddbf5ea75619f0cef91e1214)irq\_offload\_routine\_t

| typedef void(\* irq\_offload\_routine\_t) (const void \*parameter) |
| --- |

## Function Documentation

## [◆ ](#a429859dd7ac3d88a4b7ae858835847ce)irq\_offload()

| void irq\_offload | ( | [irq\_offload\_routine\_t](#a5bcf9956ddbf5ea75619f0cef91e1214) | *routine*, |
| --- | --- | --- | --- |
|  |  | const void \* | *parameter* ) |

Run a function in interrupt context.

This function synchronously runs the provided function in interrupt context, passing in the supplied device. Useful for test code which needs to show that kernel objects work correctly in interrupt context.

Additionally, when CONFIG\_IRQ\_OFFLOAD\_NESTED is set by the architecture, this routine works to synchronously invoke a nested interrupt when called from an ISR context (i.e. when [k\_is\_in\_isr()](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16 "Determine if code is running at interrupt level.") is true). Note that not all platforms will have hardware support for this capability, and even on those some interrupts may be running at unpreemptible priorities.

Parameters
:   | routine | The function to run |
    | --- | --- |
    | parameter | Argument to pass to the function when it is run as an interrupt |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [irq\_offload.h](irq__offload_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
