---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/smf_8h.html
original_path: doxygen/html/smf_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smf.h File Reference

State Machine Framework header file.
[More...](#details)

`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](smf_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [smf\_state](structsmf__state.md) |
|  | General state that can be used in multiple state machines. [More...](structsmf__state.md#details) |
| struct | [smf\_ctx](structsmf__ctx.md) |
|  | Defines the current context of the state machine. [More...](structsmf__ctx.md#details) |

| Macros | |
| --- | --- |
| #define | [SMF\_CREATE\_STATE](group__smf.md#ga5760b98a36ed1ac55eba700cf44c7e1e)(\_entry, \_run, \_exit, \_parent, \_initial) |
|  | Macro to create a hierarchical state with initial transitions. |
| #define | [SMF\_CTX](group__smf.md#ga0bccd3bf96e0887e8a610c1b06e22237)(o) |
|  | Macro to cast user defined object to state machine context. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [state\_execution](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6)) (void \*obj) |
|  | Function pointer that implements a portion of a state. |

| Functions | |
| --- | --- |
| void | [smf\_set\_initial](group__smf.md#ga4389086c6aa3167e8c49226323ae208d) (struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*init\_state) |
|  | Initializes the state machine and sets its initial state. |
| void | [smf\_set\_state](group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb) (struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*new\_state) |
|  | Changes a state machines state. |
| void | [smf\_set\_terminate](group__smf.md#gaae28c66f0652c99ba8e843eeaf02aaf7) (struct [smf\_ctx](structsmf__ctx.md) \*ctx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val) |
|  | Terminate a state machine. |
| void | [smf\_set\_handled](group__smf.md#gaa187bbd70434d29c319089faf50c2526) (struct [smf\_ctx](structsmf__ctx.md) \*ctx) |
|  | Tell the SMF to stop propagating the event to ancestors. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [smf\_run\_state](group__smf.md#ga8399cfa9e793a7f188b4ed4fec9f4f90) (struct [smf\_ctx](structsmf__ctx.md) \*ctx) |
|  | Runs one iteration of a state machine (including any parent states). |

## Detailed Description

State Machine Framework header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [smf.h](smf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
