---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structosdp__event.html
original_path: doxygen/html/structosdp__event.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp\_event Struct Reference

OSDP Event structure.
[More...](#details)

`#include <[osdp.h](osdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [osdp\_event\_type](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984d) | [type](#ae72763214c94751d359bf1887d8ea35a) |
|  | Event type. |
| union { |  |
| struct [osdp\_event\_keypress](structosdp__event__keypress.md)   [keypress](#a35759c65fc80592e42d948059f8178d3) |  |
|  | Keypress event structure. [More...](#a35759c65fc80592e42d948059f8178d3) |
| struct [osdp\_event\_cardread](structosdp__event__cardread.md)   [cardread](#ae2488838c114c72ebf0286a6f5c67814) |  |
|  | Card read event structure. [More...](#ae2488838c114c72ebf0286a6f5c67814) |
| }; |  |
|  | Event. |

## Detailed Description

OSDP Event structure.

## Field Documentation

## [◆ ](#a9aaea46780bc4ab60b805b46dc9f26ba)[union]

| union { ... } [osdp\_event](structosdp__event.md) |
| --- |

Event.

## [◆ ](#ae2488838c114c72ebf0286a6f5c67814)cardread

| struct [osdp\_event\_cardread](structosdp__event__cardread.md) osdp\_event::cardread |
| --- |

Card read event structure.

## [◆ ](#a35759c65fc80592e42d948059f8178d3)keypress

| struct [osdp\_event\_keypress](structosdp__event__keypress.md) osdp\_event::keypress |
| --- |

Keypress event structure.

## [◆ ](#ae72763214c94751d359bf1887d8ea35a)type

| enum [osdp\_event\_type](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984d) osdp\_event::type |
| --- |

Event type.

Used to select specific event in union.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/[osdp.h](osdp_8h_source.md)

- [osdp\_event](structosdp__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
