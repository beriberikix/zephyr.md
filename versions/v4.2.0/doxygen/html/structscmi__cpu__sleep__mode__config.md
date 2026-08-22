---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structscmi__cpu__sleep__mode__config.html
original_path: doxygen/html/structscmi__cpu__sleep__mode__config.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

scmi\_cpu\_sleep\_mode\_config Struct Reference

Describes the parameters for the CPU\_STATE\_SET command.
[More...](#details)

`#include <[zephyr/drivers/firmware/scmi/nxp/cpu.h](drivers_2firmware_2scmi_2nxp_2cpu_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cpu\_id](#ab14413f0c5cdd1a061235a750df316e0) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#ab11fddc7614f03706180cf12151d5e7d) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sleep\_mode](#a29781dcbdbaf3fd2e6aa840e78f26615) |

## Detailed Description

Describes the parameters for the CPU\_STATE\_SET command.

## Field Documentation

## [◆ ](#ab14413f0c5cdd1a061235a750df316e0)cpu\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) scmi\_cpu\_sleep\_mode\_config::cpu\_id |
| --- |

## [◆ ](#ab11fddc7614f03706180cf12151d5e7d)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) scmi\_cpu\_sleep\_mode\_config::flags |
| --- |

## [◆ ](#a29781dcbdbaf3fd2e6aa840e78f26615)sleep\_mode

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) scmi\_cpu\_sleep\_mode\_config::sleep\_mode |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/scmi/nxp/[cpu.h](drivers_2firmware_2scmi_2nxp_2cpu_8h_source.md)

- [scmi\_cpu\_sleep\_mode\_config](structscmi__cpu__sleep__mode__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
