---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__smf.html
original_path: doxygen/html/group__smf.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| typedef void(\* | [state\_execution](#gaff08e9a57d55107fd8d13ffe86295ca6)) (void \*obj) |
|  | Function pointer that implements a portion of a state. |

| Functions | |
| --- | --- |
| void | [smf\_set\_initial](#ga4389086c6aa3167e8c49226323ae208d) (struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*init\_state) |
|  | Initializes the state machine and sets its initial state. |
| void | [smf\_set\_state](#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb) (struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*new\_state) |
|  | Changes a state machines state. |
| void | [smf\_set\_terminate](#gaae28c66f0652c99ba8e843eeaf02aaf7) (struct [smf\_ctx](structsmf__ctx.md) \*ctx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val) |
|  | Terminate a state machine. |
| void | [smf\_set\_handled](#gaa187bbd70434d29c319089faf50c2526) (struct [smf\_ctx](structsmf__ctx.md) \*ctx) |
|  | Tell the SMF to stop propagating the event to ancestors. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [smf\_run\_state](#ga8399cfa9e793a7f188b4ed4fec9f4f90) (struct [smf\_ctx](structsmf__ctx.md) \*ctx) |
|  | Runs one iteration of a state machine (including any parent states). |

## Detailed Description

State Machine Framework API.

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga5760b98a36ed1ac55eba700cf44c7e1e)SMF\_CREATE\_STATE

| #define SMF\_CREATE\_STATE | ( |  | *\_entry*, |
| --- | --- | --- | --- |
|  |  |  | *\_run*, |
|  |  |  | *\_exit*, |
|  |  |  | *\_parent*, |
|  |  |  | *\_initial* ) |

`#include <[smf.h](smf_8h.md)>`

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

`#include <[smf.h](smf_8h.md)>`

**Value:**

((struct [smf\_ctx](structsmf__ctx.md) \*)o)

[smf\_ctx](structsmf__ctx.md)

Defines the current context of the state machine.

**Definition** smf.h:99

Macro to cast user defined object to state machine context.

Parameters
:   | o | A pointer to the user defined object |
    | --- | --- |

## Typedef Documentation

## [◆ ](#gaff08e9a57d55107fd8d13ffe86295ca6)state\_execution

| typedef void(\* state\_execution) (void \*obj) |
| --- |

`#include <[smf.h](smf_8h.md)>`

Function pointer that implements a portion of a state.

Parameters
:   | obj | pointer user defined object |
    | --- | --- |

## Function Documentation

## [◆ ](#ga8399cfa9e793a7f188b4ed4fec9f4f90)smf\_run\_state()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) smf\_run\_state | ( | struct [smf\_ctx](structsmf__ctx.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[smf.h](smf_8h.md)>`

Runs one iteration of a state machine (including any parent states).

Parameters
:   | ctx | State machine context |
    | --- | --- |

Returns
:   A non-zero value should terminate the state machine. This non-zero value could represent a terminal state being reached or the detection of an error that should result in the termination of the state machine.

## [◆ ](#gaa187bbd70434d29c319089faf50c2526)smf\_set\_handled()

| void smf\_set\_handled | ( | struct [smf\_ctx](structsmf__ctx.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[smf.h](smf_8h.md)>`

Tell the SMF to stop propagating the event to ancestors.

This allows HSMs to implement 'programming by difference' where substates can handle events on their own or propagate up to a common handler.

Parameters
:   | ctx | State machine context |
    | --- | --- |

## [◆ ](#ga4389086c6aa3167e8c49226323ae208d)smf\_set\_initial()

| void smf\_set\_initial | ( | struct [smf\_ctx](structsmf__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [smf\_state](structsmf__state.md) \* | *init\_state* ) |

`#include <[smf.h](smf_8h.md)>`

Initializes the state machine and sets its initial state.

Parameters
:   | ctx | State machine context |
    | --- | --- |
    | init\_state | Initial state the state machine starts in. |

## [◆ ](#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)smf\_set\_state()

| void smf\_set\_state | ( | struct [smf\_ctx](structsmf__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [smf\_state](structsmf__state.md) \* | *new\_state* ) |

`#include <[smf.h](smf_8h.md)>`

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

`#include <[smf.h](smf_8h.md)>`

Terminate a state machine.

Parameters
:   | ctx | State machine context |
    | --- | --- |
    | val | Non-Zero termination value that's returned by the smf\_run\_state function. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
