---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structscmi__clock__rate__config.html
original_path: doxygen/html/structscmi__clock__rate__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

scmi\_clock\_rate\_config Struct Reference

Describes the parameters for the CLOCK\_RATE\_SET command.
[More...](#details)

`#include <[clk.h](clk_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a784dfe157fad46cfa038be4cac21560c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [clk\_id](#ab9a77f5d0213008afc023ae3406cbb81) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rate](#a240149068386c9da08236589186ba4d8) [2] |

## Detailed Description

Describes the parameters for the CLOCK\_RATE\_SET command.

## Field Documentation

## [◆ ](#ab9a77f5d0213008afc023ae3406cbb81)clk\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) scmi\_clock\_rate\_config::clk\_id |
| --- |

## [◆ ](#a784dfe157fad46cfa038be4cac21560c)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) scmi\_clock\_rate\_config::flags |
| --- |

## [◆ ](#a240149068386c9da08236589186ba4d8)rate

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) scmi\_clock\_rate\_config::rate[2] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/scmi/[clk.h](clk_8h_source.md)

- [scmi\_clock\_rate\_config](structscmi__clock__rate__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
