---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__smf.html
original_path: doxygen/html/group__smf.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

State Machine Framework API

[Operating System Services](group__os__services.md)

State Machine Framework API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [smf\_state](structsmf__state.md) |
|  | General state that can be used in multiple state machines. [More...](structsmf__state.md#details) |
| struct | [smf\_ctx](structsmf__ctx.md) |
|  | Defines the current context of the state machine. [More...](structsmf__ctx.md#details) |

| Macros | |
| --- | --- |
| #define | [SMF\_CREATE\_STATE](#ga5760b98a36ed1ac55eba700cf44c7e1e)(\_entry, \_run, \_exit, \_parent, \_initial) |
|  | Macro to create a hierarchical state with initial transitions. |
| #define | [SMF\_CTX](#ga0bccd3bf96e0887e8a610c1b06e22237)(o) |
|  | Macro to cast user defined object to state machine context. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [state\_method](#gace21c98a982b640c75951676d6ee3988)) (void \*obj) |
|  | Function pointer that implements a entry and exit actions of a state. |
| typedef enum [smf\_state\_result](#ga01e4e2d2f35a9ec790d5e3c5b9b91b55)(\* | [state\_execution](#ga050cbb0a791dc062d222c0cfb4366f43)) (void \*obj) |
|  | Function pointer that implements a the run action of a state. |

| Enumerations | |
| --- | --- |
| enum | [smf\_state\_result](#ga01e4e2d2f35a9ec790d5e3c5b9b91b55) { [SMF\_EVENT\_HANDLED](#gga01e4e2d2f35a9ec790d5e3c5b9b91b55a088a71df8c1eb56aec8e4ef647a2248a) , [SMF\_EVENT\_PROPAGATE](#gga01e4e2d2f35a9ec790d5e3c5b9b91b55af86126b6ae29cfa0c1816bc5fb2873b6) } |
|  | enum for the return value of a [state\_execution](#ga050cbb0a791dc062d222c0cfb4366f43) function [More...](#ga01e4e2d2f35a9ec790d5e3c5b9b91b55) |

| Functions | |
| --- | --- |
| void | [smf\_set\_initial](#ga4389086c6aa3167e8c49226323ae208d) (struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*init\_state) |
|  | Initializes the state machine and sets its initial state. |
| void | [smf\_set\_state](#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb) (struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*new\_state) |
|  | Changes a state machines state. |
| void | [smf\_set\_terminate](#gaae28c66f0652c99ba8e843eeaf02aaf7) (struct [smf\_ctx](structsmf__ctx.md) \*ctx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val) |
|  | Terminate a state machine. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [smf\_run\_state](#ga8399cfa9e793a7f188b4ed4fec9f4f90) (struct [smf\_ctx](structsmf__ctx.md) \*ctx) |
|  | Runs one iteration of a state machine (including any parent states). |

## Detailed Description

State Machine Framework API.

Version
:   0.2.0

## Macro Definition Documentation

## [◆ ](#ga5760b98a36ed1ac55eba700cf44c7e1e)SMF\_CREATE\_STATE

| #define SMF\_CREATE\_STATE | ( |  | *\_entry*, |
| --- | --- | --- | --- |
|  |  |  | *\_run*, |
|  |  |  | *\_exit*, |
|  |  |  | *\_parent*, |
|  |  |  | *\_initial* ) |

`#include <[zephyr/smf.h](smf_8h.md)>`

**Value:**

{ \

.entry = \_entry, \

.run = \_run, \

.exit = \_exit, \

IF\_ENABLED(CONFIG\_SMF\_ANCESTOR\_SUPPORT, (.parent = \_parent,)) \

IF\_ENABLED(CONFIG\_SMF\_INITIAL\_TRANSITION, (.initial = \_initial,)) \

}

Macro to create a hierarchical state with initial transitions.

Parameters
:   | \_entry | State entry function or NULL |
    | --- | --- |
    | \_run | State run function or NULL |
    | \_exit | State exit function or NULL |
    | \_parent | State parent object or NULL |
    | \_initial | State initial transition object or NULL |

## [◆ ](#ga0bccd3bf96e0887e8a610c1b06e22237)SMF\_CTX

| #define SMF\_CTX | ( |  | *o* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/smf.h](smf_8h.md)>`

**Value:**

((struct [smf\_ctx](structsmf__ctx.md) \*)o)

[smf\_ctx](structsmf__ctx.md)

Defines the current context of the state machine.

**Definition** smf.h:121

Macro to cast user defined object to state machine context.

Parameters
:   | o | A pointer to the user defined object |
    | --- | --- |

## Typedef Documentation

## [◆ ](#ga050cbb0a791dc062d222c0cfb4366f43)state\_execution

| typedef enum [smf\_state\_result](#ga01e4e2d2f35a9ec790d5e3c5b9b91b55)(\* state\_execution) (void \*obj) |
| --- |

`#include <[zephyr/smf.h](smf_8h.md)>`

Function pointer that implements a the run action of a state.

Parameters
:   | obj | pointer user defined object |
    | --- | --- |

Returns
:   If the event should be propagated to parent states or not (Ignored when CONFIG\_SMF\_ANCESTOR\_SUPPORT not defined)

## [◆ ](#gace21c98a982b640c75951676d6ee3988)state\_method

| typedef void(\* state\_method) (void \*obj) |
| --- |

`#include <[zephyr/smf.h](smf_8h.md)>`

Function pointer that implements a entry and exit actions of a state.

Parameters
:   | obj | pointer user defined object |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#ga01e4e2d2f35a9ec790d5e3c5b9b91b55)smf\_state\_result

| enum [smf\_state\_result](#ga01e4e2d2f35a9ec790d5e3c5b9b91b55) |
| --- |

`#include <[zephyr/smf.h](smf_8h.md)>`

enum for the return value of a [state\_execution](#ga050cbb0a791dc062d222c0cfb4366f43) function

| Enumerator | |
| --- | --- |
| SMF\_EVENT\_HANDLED |  |
| SMF\_EVENT\_PROPAGATE |  |

## Function Documentation

## [◆ ](#ga8399cfa9e793a7f188b4ed4fec9f4f90)smf\_run\_state()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) smf\_run\_state | ( | struct [smf\_ctx](structsmf__ctx.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/smf.h](smf_8h.md)>`

Runs one iteration of a state machine (including any parent states).

Parameters
:   | ctx | State machine context |
    | --- | --- |

Returns
:   A non-zero value should terminate the state machine. This non-zero value could represent a terminal state being reached or the detection of an error that should result in the termination of the state machine.

## [◆ ](#ga4389086c6aa3167e8c49226323ae208d)smf\_set\_initial()

| void smf\_set\_initial | ( | struct [smf\_ctx](structsmf__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [smf\_state](structsmf__state.md) \* | *init\_state* ) |

`#include <[zephyr/smf.h](smf_8h.md)>`

Initializes the state machine and sets its initial state.

Parameters
:   | ctx | State machine context |
    | --- | --- |
    | init\_state | Initial state the state machine starts in. |

## [◆ ](#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)smf\_set\_state()

| void smf\_set\_state | ( | struct [smf\_ctx](structsmf__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [smf\_state](structsmf__state.md) \* | *new\_state* ) |

`#include <[zephyr/smf.h](smf_8h.md)>`

Changes a state machines state.

This handles exiting the previous state and entering the target state. For HSMs the entry and exit actions of the Least Common Ancestor will not be run.

Parameters
:   | ctx | State machine context |
    | --- | --- |
    | new\_state | State to transition to (NULL is valid and exits all states) |

## [◆ ](#gaae28c66f0652c99ba8e843eeaf02aaf7)smf\_set\_terminate()

| void smf\_set\_terminate | ( | struct [smf\_ctx](structsmf__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *val* ) |

`#include <[zephyr/smf.h](smf_8h.md)>`

Terminate a state machine.

Parameters
:   | ctx | State machine context |
    | --- | --- |
    | val | Non-Zero termination value that's returned by the smf\_run\_state function. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
