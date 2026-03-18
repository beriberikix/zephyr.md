---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/smf_8h.html
original_path: doxygen/html/smf_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smf.h File Reference

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`

[Go to the source code of this file.](smf_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [smf\_state](structsmf__state.md) |
|  | General state that can be used in multiple state machines. [More...](structsmf__state.md#details) |
| struct | [smf\_ctx](structsmf__ctx.md) |
|  | Defines the current context of the state machine. [More...](structsmf__ctx.md#details) |

| Macros | |
| --- | --- |
| #define | [SMF\_CREATE\_STATE](#a7bcef10d761c099633867066ecef49f6)(\_entry, \_run, \_exit) |
|  | Macro to create a flat state. |
| #define | [SMF\_CTX](#a0bccd3bf96e0887e8a610c1b06e22237)(o) |
|  | Macro to cast user defined object to state machine context. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [state\_execution](#aff08e9a57d55107fd8d13ffe86295ca6)) (void \*obj) |
|  | Function pointer that implements a portion of a state. |

| Functions | |
| --- | --- |
| void | [smf\_set\_initial](#a4389086c6aa3167e8c49226323ae208d) (struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*init\_state) |
|  | Initializes the state machine and sets its initial state. |
| void | [smf\_set\_state](#a3e5ac3e2ad105d1a01b4cf0b1a8a6fcb) (struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*new\_state) |
|  | Changes a state machines state. |
| void | [smf\_set\_terminate](#aae28c66f0652c99ba8e843eeaf02aaf7) (struct [smf\_ctx](structsmf__ctx.md) \*ctx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val) |
|  | Terminate a state machine. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [smf\_run\_state](#a8399cfa9e793a7f188b4ed4fec9f4f90) (struct [smf\_ctx](structsmf__ctx.md) \*ctx) |
|  | Runs one iteration of a state machine (including any parent states). |

## Macro Definition Documentation

## [◆ ](#a7bcef10d761c099633867066ecef49f6)SMF\_CREATE\_STATE

| #define SMF\_CREATE\_STATE | ( |  | *\_entry*, |
| --- | --- | --- | --- |
|  |  |  | *\_run*, |
|  |  |  | *\_exit* ) |

**Value:**

{ \

.entry = \_entry, \

.run = \_run, \

.exit = \_exit \

}

Macro to create a flat state.

Parameters
:   | \_entry | State entry function |
    | --- | --- |
    | \_run | State run function |
    | \_exit | State exit function |

## [◆ ](#a0bccd3bf96e0887e8a610c1b06e22237)SMF\_CTX

| #define SMF\_CTX | ( |  | *o* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((struct [smf\_ctx](structsmf__ctx.md) \*)o)

[smf\_ctx](structsmf__ctx.md)

Defines the current context of the state machine.

**Definition** smf.h:93

Macro to cast user defined object to state machine context.

Parameters
:   | o | A pointer to the user defined object |
    | --- | --- |

## Typedef Documentation

## [◆ ](#aff08e9a57d55107fd8d13ffe86295ca6)state\_execution

| typedef void(\* state\_execution) (void \*obj) |
| --- |

Function pointer that implements a portion of a state.

Parameters
:   | obj | pointer user defined object |
    | --- | --- |

## Function Documentation

## [◆ ](#a8399cfa9e793a7f188b4ed4fec9f4f90)smf\_run\_state()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) smf\_run\_state | ( | struct [smf\_ctx](structsmf__ctx.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

Runs one iteration of a state machine (including any parent states).

Parameters
:   | ctx | State machine context |
    | --- | --- |

Returns
:   A non-zero value should terminate the state machine. This non-zero value could represent a terminal state being reached or the detection of an error that should result in the termination of the state machine.

## [◆ ](#a4389086c6aa3167e8c49226323ae208d)smf\_set\_initial()

| void smf\_set\_initial | ( | struct [smf\_ctx](structsmf__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [smf\_state](structsmf__state.md) \* | *init\_state* ) |

Initializes the state machine and sets its initial state.

Parameters
:   | ctx | State machine context |
    | --- | --- |
    | init\_state | Initial state the state machine starts in. |

## [◆ ](#a3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)smf\_set\_state()

| void smf\_set\_state | ( | struct [smf\_ctx](structsmf__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [smf\_state](structsmf__state.md) \* | *new\_state* ) |

Changes a state machines state.

This handles exiting the previous state and entering the target state. A common parent state will not exited nor be re-entered.

Parameters
:   | ctx | State machine context |
    | --- | --- |
    | new\_state | State to transition to (NULL is valid and exits all states) |

## [◆ ](#aae28c66f0652c99ba8e843eeaf02aaf7)smf\_set\_terminate()

| void smf\_set\_terminate | ( | struct [smf\_ctx](structsmf__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *val* ) |

Terminate a state machine.

Parameters
:   | ctx | State machine context |
    | --- | --- |
    | val | Non-Zero termination value that's returned by the smf\_run\_state function. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [smf.h](smf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
