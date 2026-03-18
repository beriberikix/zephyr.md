---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structec__host__cmd__rx__ctx.html
original_path: doxygen/html/structec__host__cmd__rx__ctx.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ec\_host\_cmd\_rx\_ctx Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [EC Host Command Interface](group__ec__host__cmd__interface.md)

Context for host command backend and handler to pass rx data.
[More...](#details)

`#include <[backend.h](backend_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buf](#afcae3b7881f1c8634bb3ac1315111294) |
|  | Buffer to hold received data. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [len](#ae9f1c0c78d27dd5aa9bf47c56452a75a) |
|  | Number of bytes written to *buf* by backend. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [len\_max](#a2db5dc5740436c8e0e232b959472ed0f) |
|  | Maximum number of bytes to receive with one request packet. |

## Detailed Description

Context for host command backend and handler to pass rx data.

## Field Documentation

## [◆ ](#afcae3b7881f1c8634bb3ac1315111294)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* ec\_host\_cmd\_rx\_ctx::buf |
| --- |

Buffer to hold received data.

The buffer is provided by the handler if CONFIG\_EC\_HOST\_CMD\_HANDLER\_RX\_BUFFER\_SIZE > 0. Otherwise, the backend should provide the buffer on its own and overwrites *buf* pointer and *len\_max* in the init function.

## [◆ ](#ae9f1c0c78d27dd5aa9bf47c56452a75a)len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ec\_host\_cmd\_rx\_ctx::len |
| --- |

Number of bytes written to *buf* by backend.

## [◆ ](#a2db5dc5740436c8e0e232b959472ed0f)len\_max

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ec\_host\_cmd\_rx\_ctx::len\_max |
| --- |

Maximum number of bytes to receive with one request packet.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/ec\_host\_cmd/[backend.h](backend_8h_source.md)

- [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
