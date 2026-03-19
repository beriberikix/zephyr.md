---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structec__host__cmd__tx__buf.html
original_path: doxygen/html/structec__host__cmd__tx__buf.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ec\_host\_cmd\_tx\_buf Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [EC Host Command Interface](group__ec__host__cmd__interface.md)

Context for host command backend and handler to pass tx data.
[More...](#details)

`#include <[backend.h](backend_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [buf](#a6444723bccc196fb9792e95957bd98a5) |
|  | Data to write to the host The buffer is provided by the handler if CONFIG\_EC\_HOST\_CMD\_HANDLER\_TX\_BUFFER\_SIZE > 0. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [len](#afaff8fbcb798a0445b029db1cedb6fd1) |
|  | Number of bytes to write from *buf*. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [len\_max](#a0f115f85bd271fa0defec1a2fc461d4c) |
|  | Maximum number of bytes to send with one response packet. |

## Detailed Description

Context for host command backend and handler to pass tx data.

## Field Documentation

## [◆ ](#a6444723bccc196fb9792e95957bd98a5)buf

| void\* ec\_host\_cmd\_tx\_buf::buf |
| --- |

Data to write to the host The buffer is provided by the handler if CONFIG\_EC\_HOST\_CMD\_HANDLER\_TX\_BUFFER\_SIZE > 0.

Otherwise, the backend should provide the buffer on its own and overwrites *buf* pointer and *len\_max* in the init function.

## [◆ ](#afaff8fbcb798a0445b029db1cedb6fd1)len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ec\_host\_cmd\_tx\_buf::len |
| --- |

Number of bytes to write from *buf*.

## [◆ ](#a0f115f85bd271fa0defec1a2fc461d4c)len\_max

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ec\_host\_cmd\_tx\_buf::len\_max |
| --- |

Maximum number of bytes to send with one response packet.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/ec\_host\_cmd/[backend.h](backend_8h_source.md)

- [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
