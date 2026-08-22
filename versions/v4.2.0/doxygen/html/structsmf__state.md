---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structsmf__state.html
original_path: doxygen/html/structsmf__state.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smf\_state Struct Reference

[Operating System Services](group__os__services.md) » [State Machine Framework API](group__smf.md)

General state that can be used in multiple state machines.
[More...](#details)

`#include <[zephyr/smf.h](smf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [state\_method](group__smf.md#gace21c98a982b640c75951676d6ee3988) | [entry](#a742fe438b7b5b014d23bde210a512dee) |
|  | Optional method that will be run when this state is entered. |
| const [state\_execution](group__smf.md#ga050cbb0a791dc062d222c0cfb4366f43) | [run](#a94adbcd4e1a8bce8f3b30082874f1911) |
|  | Optional method that will be run repeatedly during state machine loop. |
| const [state\_method](group__smf.md#gace21c98a982b640c75951676d6ee3988) | [exit](#a0661b4257b2ff7c508aeef9822b90a2f) |
|  | Optional method that will be run when this state exists. |

## Detailed Description

General state that can be used in multiple state machines.

## Field Documentation

## [◆ ](#a742fe438b7b5b014d23bde210a512dee)entry

| const [state\_method](group__smf.md#gace21c98a982b640c75951676d6ee3988) smf\_state::entry |
| --- |

Optional method that will be run when this state is entered.

## [◆ ](#a0661b4257b2ff7c508aeef9822b90a2f)exit

| const [state\_method](group__smf.md#gace21c98a982b640c75951676d6ee3988) smf\_state::exit |
| --- |

Optional method that will be run when this state exists.

## [◆ ](#a94adbcd4e1a8bce8f3b30082874f1911)run

| const [state\_execution](group__smf.md#ga050cbb0a791dc062d222c0cfb4366f43) smf\_state::run |
| --- |

Optional method that will be run repeatedly during state machine loop.

---

The documentation for this struct was generated from the following file:

- zephyr/[smf.h](smf_8h_source.md)

- [smf\_state](structsmf__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
