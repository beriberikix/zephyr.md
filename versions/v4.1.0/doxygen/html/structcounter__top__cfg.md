---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcounter__top__cfg.html
original_path: doxygen/html/structcounter__top__cfg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

counter\_top\_cfg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Counter Interface](group__counter__interface.md)

Top value configuration structure.
[More...](#details)

`#include <[counter.h](drivers_2counter_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ticks](#abb60a9d468fa6d6802ba56a02a515751) |
|  | Top value. |
| [counter\_top\_callback\_t](group__counter__interface.md#ga3686fe1f86a53469659f79897e4e1baf) | [callback](#adf1cf3a9c67278f5f5f1cba72f6dd934) |
|  | Callback function (can be NULL). |
| void \* | [user\_data](#af033941769c710e82cf9dd9f12ff011c) |
|  | User data passed to callback function (not valid if callback is NULL). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#ad5caa9f1c80badf14c2c313e60e3e8e6) |
|  | Flags (see [COUNTER\_TOP\_FLAGS](group__counter__interface.md#COUNTER_TOP_FLAGS "COUNTER_TOP_FLAGS")). |

## Detailed Description

Top value configuration structure.

## Field Documentation

## [◆ ](#adf1cf3a9c67278f5f5f1cba72f6dd934)callback

| [counter\_top\_callback\_t](group__counter__interface.md#ga3686fe1f86a53469659f79897e4e1baf) counter\_top\_cfg::callback |
| --- |

Callback function (can be NULL).

## [◆ ](#ad5caa9f1c80badf14c2c313e60e3e8e6)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) counter\_top\_cfg::flags |
| --- |

Flags (see [COUNTER\_TOP\_FLAGS](group__counter__interface.md#COUNTER_TOP_FLAGS "COUNTER_TOP_FLAGS")).

## [◆ ](#abb60a9d468fa6d6802ba56a02a515751)ticks

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) counter\_top\_cfg::ticks |
| --- |

Top value.

## [◆ ](#af033941769c710e82cf9dd9f12ff011c)user\_data

| void\* counter\_top\_cfg::user\_data |
| --- |

User data passed to callback function (not valid if callback is NULL).

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[counter.h](drivers_2counter_8h_source.md)

- [counter\_top\_cfg](structcounter__top__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
