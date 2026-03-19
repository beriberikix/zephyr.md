---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structsmf__state.html
original_path: doxygen/html/structsmf__state.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smf\_state Struct Reference

[Operating System Services](group__os__services.md) » [State Machine Framework API](group__smf.md)

General state that can be used in multiple state machines.
[More...](#details)

`#include <[smf.h](smf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [state\_execution](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6) | [entry](#a63ea395c90fa8118cf355e55e60cee26) |
|  | Optional method that will be run when this state is entered. |
| const [state\_execution](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6) | [run](#a94adbcd4e1a8bce8f3b30082874f1911) |
|  | Optional method that will be run repeatedly during state machine loop. |
| const [state\_execution](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6) | [exit](#a2df810ca49fbb9438ee78317feaaf09b) |
|  | Optional method that will be run when this state exists. |

## Detailed Description

General state that can be used in multiple state machines.

## Field Documentation

## [◆ ](#a63ea395c90fa8118cf355e55e60cee26)entry

| const [state\_execution](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6) smf\_state::entry |
| --- |

Optional method that will be run when this state is entered.

## [◆ ](#a2df810ca49fbb9438ee78317feaaf09b)exit

| const [state\_execution](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6) smf\_state::exit |
| --- |

Optional method that will be run when this state exists.

## [◆ ](#a94adbcd4e1a8bce8f3b30082874f1911)run

| const [state\_execution](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6) smf\_state::run |
| --- |

Optional method that will be run repeatedly during state machine loop.

---

The documentation for this struct was generated from the following file:

- zephyr/[smf.h](smf_8h_source.md)

- [smf\_state](structsmf__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
