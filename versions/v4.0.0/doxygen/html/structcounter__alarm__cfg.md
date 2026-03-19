---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structcounter__alarm__cfg.html
original_path: doxygen/html/structcounter__alarm__cfg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

counter\_alarm\_cfg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Counter Interface](group__counter__interface.md)

Alarm callback structure.
[More...](#details)

`#include <[counter.h](drivers_2counter_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [counter\_alarm\_callback\_t](group__counter__interface.md#ga36c570c3e57e635753d163400e437b77) | [callback](#aeef670ee73dd4d7d65e02a66313b092d) |
|  | Callback called on alarm (cannot be NULL). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ticks](#a85b6b86d7a82f2e238000dd31ff1f779) |
|  | Number of ticks that triggers the alarm. |
| void \* | [user\_data](#aeaf2bd9042a28b626e0972aff4ad09e5) |
|  | User data returned in callback. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#ab043cd1ea9be54449bb75c4a5affe620) |
|  | Alarm flags (see [COUNTER\_ALARM\_FLAGS](group__counter__interface.md#COUNTER_ALARM_FLAGS "COUNTER_ALARM_FLAGS")). |

## Detailed Description

Alarm callback structure.

## Field Documentation

## [◆ ](#aeef670ee73dd4d7d65e02a66313b092d)callback

| [counter\_alarm\_callback\_t](group__counter__interface.md#ga36c570c3e57e635753d163400e437b77) counter\_alarm\_cfg::callback |
| --- |

Callback called on alarm (cannot be NULL).

## [◆ ](#ab043cd1ea9be54449bb75c4a5affe620)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) counter\_alarm\_cfg::flags |
| --- |

Alarm flags (see [COUNTER\_ALARM\_FLAGS](group__counter__interface.md#COUNTER_ALARM_FLAGS "COUNTER_ALARM_FLAGS")).

## [◆ ](#a85b6b86d7a82f2e238000dd31ff1f779)ticks

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) counter\_alarm\_cfg::ticks |
| --- |

Number of ticks that triggers the alarm.

It can be relative (to now) or an absolute value (see [COUNTER\_ALARM\_CFG\_ABSOLUTE](group__counter__interface.md#ga4842d212424f92c5a3b39116ec6c2fd2 "COUNTER_ALARM_CFG_ABSOLUTE")). Both, relative and absolute, alarm values can be any value between zero and the current top value (see [counter\_get\_top\_value](group__counter__interface.md#ga13d14903a03ab10062002a81b8302424 "counter_get_top_value")). When setting an absolute alarm value close to the current counter value there is a risk that the counter will have counted past the given absolute value before the driver manages to activate the alarm. Therefore a guard period can be defined that lets the driver decide unambiguously whether it is late or not (see [counter\_set\_guard\_period](group__counter__interface.md#gab6851411dabf191d3391715d632111b0 "counter_set_guard_period")). If the counter is clock driven then ticks can be converted to microseconds (see [counter\_ticks\_to\_us](group__counter__interface.md#ga9fbcb710091084e638c45f62c25d954c "counter_ticks_to_us")). Alternatively, the counter implementation may count asynchronous events.

## [◆ ](#aeaf2bd9042a28b626e0972aff4ad09e5)user\_data

| void\* counter\_alarm\_cfg::user\_data |
| --- |

User data returned in callback.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[counter.h](drivers_2counter_8h_source.md)

- [counter\_alarm\_cfg](structcounter__alarm__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
