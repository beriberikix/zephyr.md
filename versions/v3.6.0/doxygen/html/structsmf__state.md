---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsmf__state.html
original_path: doxygen/html/structsmf__state.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smf\_state Struct Reference

General state that can be used in multiple state machines.
[More...](#details)

`#include <[smf.h](smf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [state\_execution](smf_8h.md#aff08e9a57d55107fd8d13ffe86295ca6) | [entry](#a63ea395c90fa8118cf355e55e60cee26) |
|  | Optional method that will be run when this state is entered. |
| const [state\_execution](smf_8h.md#aff08e9a57d55107fd8d13ffe86295ca6) | [run](#a94adbcd4e1a8bce8f3b30082874f1911) |
|  | Optional method that will be run repeatedly during state machine loop. |
| const [state\_execution](smf_8h.md#aff08e9a57d55107fd8d13ffe86295ca6) | [exit](#a2df810ca49fbb9438ee78317feaaf09b) |
|  | Optional method that will be run when this state exists. |
| const struct [smf\_state](structsmf__state.md) \* | [parent](#ac4267b2d8279d9c2d4897d97357b8e25) |
|  | Optional parent state that contains common entry/run/exit implementation among various child states. |

## Detailed Description

General state that can be used in multiple state machines.

## Field Documentation

## [◆ ](#a63ea395c90fa8118cf355e55e60cee26)entry

| const [state\_execution](smf_8h.md#aff08e9a57d55107fd8d13ffe86295ca6) smf\_state::entry |
| --- |

Optional method that will be run when this state is entered.

## [◆ ](#a2df810ca49fbb9438ee78317feaaf09b)exit

| const [state\_execution](smf_8h.md#aff08e9a57d55107fd8d13ffe86295ca6) smf\_state::exit |
| --- |

Optional method that will be run when this state exists.

## [◆ ](#ac4267b2d8279d9c2d4897d97357b8e25)parent

| const struct [smf\_state](structsmf__state.md)\* smf\_state::parent |
| --- |

Optional parent state that contains common entry/run/exit implementation among various child states.

entry: Parent function executes BEFORE child function. run: Parent function executes AFTER child function. exit: Parent function executes AFTER child function.

Note: When transitioning between two child states with a shared parent, that parent's exit and entry functions do not execute.

## [◆ ](#a94adbcd4e1a8bce8f3b30082874f1911)run

| const [state\_execution](smf_8h.md#aff08e9a57d55107fd8d13ffe86295ca6) smf\_state::run |
| --- |

Optional method that will be run repeatedly during state machine loop.

---

The documentation for this struct was generated from the following file:

- zephyr/[smf.h](smf_8h_source.md)

- [smf\_state](structsmf__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
