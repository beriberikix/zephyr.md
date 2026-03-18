---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__arch-misc.html
original_path: doxygen/html/group__arch-misc.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Miscellaneous architecture APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

| Functions | |
| --- | --- |
| int | [arch\_printk\_char\_out](#ga6860efc93b8ba35911cfb0afbe372623) (int c) |
|  | Early boot console output hook. |
| static void | [arch\_kernel\_init](#ga62cc65268b396d2683e47c09c9b62af5) (void) |
|  | Architecture-specific kernel initialization hook. |
| static void | [arch\_nop](#gabb087b9e158824121212d65646ae4154) (void) |
|  | Do nothing and return. |

## Detailed Description

## Function Documentation

## [◆ ](#ga62cc65268b396d2683e47c09c9b62af5)arch\_kernel\_init()

| | void arch\_kernel\_init | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Architecture-specific kernel initialization hook.

This function is invoked near the top of z\_cstart, for additional architecture-specific setup before the rest of the kernel is brought up.

## [◆ ](#gabb087b9e158824121212d65646ae4154)arch\_nop()

| | void arch\_nop | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Do nothing and return.

Yawn.

## [◆ ](#ga6860efc93b8ba35911cfb0afbe372623)arch\_printk\_char\_out()

| int arch\_printk\_char\_out | ( | int | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Early boot console output hook.

Definition of this function is optional. If implemented, any invocation of [printk()](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54 "Print kernel debugging message.") (or logging calls with CONFIG\_LOG\_MODE\_MINIMAL which are backed by printk) will default to sending characters to this function. It is useful for early boot debugging before main serial or console drivers come up.

This can be overridden at runtime with \_\_printk\_hook\_install().

The default \_\_weak implementation of this does nothing.

Parameters
:   | c | Character to print |
    | --- | --- |

Returns
:   The character printed

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
