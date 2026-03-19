---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structrtio__cqe.html
original_path: doxygen/html/structrtio__cqe.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio\_cqe Struct Reference

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md)

A completion queue event.
[More...](#details)

`#include <[rtio.h](rtio_2rtio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [mpsc\_node](structmpsc__node.md) | [q](#a27272bca31c170f406799633ec82098d) |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [result](#acbe2e6607a752b676d9336b9ca6ce435) |
|  | Result from operation. |
| void \* | [userdata](#a15128387ccbea55812ef229eab7241e7) |
|  | Associated userdata with operation. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a8a7632ef1cfd31529d782bd761908d93) |
|  | Flags associated with the operation. |

## Detailed Description

A completion queue event.

## Field Documentation

## [◆ ](#a8a7632ef1cfd31529d782bd761908d93)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rtio\_cqe::flags |
| --- |

Flags associated with the operation.

## [◆ ](#a27272bca31c170f406799633ec82098d)q

| struct [mpsc\_node](structmpsc__node.md) rtio\_cqe::q |
| --- |

## [◆ ](#acbe2e6607a752b676d9336b9ca6ce435)result

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) rtio\_cqe::result |
| --- |

Result from operation.

## [◆ ](#a15128387ccbea55812ef229eab7241e7)userdata

| void\* rtio\_cqe::userdata |
| --- |

Associated userdata with operation.

---

The documentation for this struct was generated from the following file:

- zephyr/rtio/[rtio.h](rtio_2rtio_8h_source.md)

- [rtio\_cqe](structrtio__cqe.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
