---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__arch-tls.html
original_path: doxygen/html/group__arch-tls.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture-specific Thread Local Storage APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

| Functions | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_tls\_stack\_setup](#ga7f159caca46063b04cf03a54b39255fc) (struct [k\_thread](structk__thread.md) \*new\_thread, char \*stack\_ptr) |
|  | Setup Architecture-specific TLS area in stack. |

## Detailed Description

## Function Documentation

## [◆ ](#ga7f159caca46063b04cf03a54b39255fc)arch\_tls\_stack\_setup()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) arch\_tls\_stack\_setup | ( | struct [k\_thread](structk__thread.md) \* | *new\_thread*, |
| --- | --- | --- | --- |
|  |  | char \* | *stack\_ptr* ) |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Setup Architecture-specific TLS area in stack.

This sets up the stack area for thread local storage. The structure inside TLS area is architecture specific.

Parameters
:   | new\_thread | New thread object |
    | --- | --- |
    | stack\_ptr | Stack pointer |

Returns
:   Number of bytes taken by the TLS area

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
