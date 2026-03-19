---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__cs__trace__defmt.html
original_path: doxygen/html/group__cs__trace__defmt.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Coresight Trace Deformatter

[Coresight APIs](group__coresight__apis.md)

| Macros | |
| --- | --- |
| #define | [CORESIGHT\_TRACE\_FRAME\_SIZE32](#gabecbf043f9f0888a0b60d2784aff55e3)   4 |
|  | Size of trace deformatter frame size in 32 bit words. |
| #define | [CORESIGHT\_TRACE\_FRAME\_SIZE](#ga7a31378ad5570f930cab4227a018d80d)   ([CORESIGHT\_TRACE\_FRAME\_SIZE32](#gabecbf043f9f0888a0b60d2784aff55e3) \* [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))) |
|  | Size of trace deformatter frame size in bytes. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [cs\_trace\_defmt\_cb](#gaccc05f92bfbc04b787f6f959e954115d)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Callback signature. |

| Functions | |
| --- | --- |
| int | [cs\_trace\_defmt\_init](#gaaeaaefe2221161691144d82c932196ca) ([cs\_trace\_defmt\_cb](#gaccc05f92bfbc04b787f6f959e954115d) cb) |
|  | Initialize Coresight Trace Deformatter. |
| int | [cs\_trace\_defmt\_process](#ga109bab752da74692779aa3eb96b771ba) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Decode data from the stream. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga7a31378ad5570f930cab4227a018d80d)CORESIGHT\_TRACE\_FRAME\_SIZE

| #define CORESIGHT\_TRACE\_FRAME\_SIZE   ([CORESIGHT\_TRACE\_FRAME\_SIZE32](#gabecbf043f9f0888a0b60d2784aff55e3) \* [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))) |
| --- |

`#include <[cs_trace_defmt.h](cs__trace__defmt_8h.md)>`

Size of trace deformatter frame size in bytes.

## [◆ ](#gabecbf043f9f0888a0b60d2784aff55e3)CORESIGHT\_TRACE\_FRAME\_SIZE32

| #define CORESIGHT\_TRACE\_FRAME\_SIZE32   4 |
| --- |

`#include <[cs_trace_defmt.h](cs__trace__defmt_8h.md)>`

Size of trace deformatter frame size in 32 bit words.

## Typedef Documentation

## [◆ ](#gaccc05f92bfbc04b787f6f959e954115d)cs\_trace\_defmt\_cb

| typedef void(\* cs\_trace\_defmt\_cb) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

`#include <[cs_trace_defmt.h](cs__trace__defmt_8h.md)>`

Callback signature.

Parameters
:   | id | Stream ID. |
    | --- | --- |
    | data | Data. |
    | len | Data length. |

## Function Documentation

## [◆ ](#gaaeaaefe2221161691144d82c932196ca)cs\_trace\_defmt\_init()

| int cs\_trace\_defmt\_init | ( | [cs\_trace\_defmt\_cb](#gaccc05f92bfbc04b787f6f959e954115d) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cs_trace_defmt.h](cs__trace__defmt_8h.md)>`

Initialize Coresight Trace Deformatter.

Parameters
:   | cb | Callback. |
    | --- | --- |

## [◆ ](#ga109bab752da74692779aa3eb96b771ba)cs\_trace\_defmt\_process()

| int cs\_trace\_defmt\_process | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[cs_trace_defmt.h](cs__trace__defmt_8h.md)>`

Decode data from the stream.

Trace formatter puts data in the 16 byte long blocks.

Callback is called with decoded data.

Parameters
:   | data | Data. |
    | --- | --- |
    | len | Data length. Must equal 16. |

Return values
:   | 0 | On successful deformatting. |
    | --- | --- |
    | -EINVAL | If wrong length is provided. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
