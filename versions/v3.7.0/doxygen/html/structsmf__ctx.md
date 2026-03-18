---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsmf__ctx.html
original_path: doxygen/html/structsmf__ctx.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smf\_ctx Struct Reference

[Operating System Services](group__os__services.md) » [State Machine Framework API](group__smf.md)

Defines the current context of the state machine.
[More...](#details)

`#include <[smf.h](smf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [smf\_state](structsmf__state.md) \* | [current](#a48736dbfad38f0b25e4ab2a36d2f482a) |
|  | Current state the state machine is executing. |
| const struct [smf\_state](structsmf__state.md) \* | [previous](#a2cebcd02bfc6b36278c20fe8e0f95418) |
|  | Previous state the state machine executed. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [terminate\_val](#a1018c3dc6d7cc94ac2b64f95e5c053cd) |
|  | This value is set by the set\_terminate function and should terminate the state machine when its set to a value other than zero when it's returned by the run\_state function. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [internal](#afb094c0e87d42ec7ca780a2859be7bf8) |
|  | The state machine casts this to a "struct internal\_ctx" and it's used to track state machine context. |

## Detailed Description

Defines the current context of the state machine.

## Field Documentation

## [◆ ](#a48736dbfad38f0b25e4ab2a36d2f482a)current

| const struct [smf\_state](structsmf__state.md)\* smf\_ctx::current |
| --- |

Current state the state machine is executing.

## [◆ ](#afb094c0e87d42ec7ca780a2859be7bf8)internal

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) smf\_ctx::internal |
| --- |

The state machine casts this to a "struct internal\_ctx" and it's used to track state machine context.

## [◆ ](#a2cebcd02bfc6b36278c20fe8e0f95418)previous

| const struct [smf\_state](structsmf__state.md)\* smf\_ctx::previous |
| --- |

Previous state the state machine executed.

## [◆ ](#a1018c3dc6d7cc94ac2b64f95e5c053cd)terminate\_val

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) smf\_ctx::terminate\_val |
| --- |

This value is set by the set\_terminate function and should terminate the state machine when its set to a value other than zero when it's returned by the run\_state function.

---

The documentation for this struct was generated from the following file:

- zephyr/[smf.h](smf_8h_source.md)

- [smf\_ctx](structsmf__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
