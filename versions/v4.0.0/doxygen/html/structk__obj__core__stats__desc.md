---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structk__obj__core__stats__desc.html
original_path: doxygen/html/structk__obj__core__stats__desc.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_obj\_core\_stats\_desc Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Object Core APIs](group__obj__core__apis.md)

Object core statistics descriptor.
[More...](#details)

`#include <[obj_core.h](obj__core_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [raw\_size](#a2e81dccd36b1355f9e685917cbd8eed8) |
|  | Internal representation stats buffer size. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [query\_size](#a9d0757daab439142711e3866e6dabb8d) |
|  | Stats buffer size used for reporting. |
| int(\* | [raw](#a0b206ae290639095e722c1705a122c2f) )(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats) |
|  | Function pointer to retrieve internal representation of stats. |
| int(\* | [query](#a94723e6cd5c03769e9cc1be9f0ec784f) )(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats) |
|  | Function pointer to retrieve reported statistics. |
| int(\* | [reset](#a2ab464c373aa3830eaf15e46de2e9370) )(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Function pointer to reset object's statistics. |
| int(\* | [disable](#ab2959fb71fc5750d1a2ad71519f354b3) )(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Function pointer to disable object's statistics gathering. |
| int(\* | [enable](#aabc9df81e93aa0ff0ec84983dd07f58f) )(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Function pointer to enable object's statistics gathering. |

## Detailed Description

Object core statistics descriptor.

## Field Documentation

## [◆ ](#ab2959fb71fc5750d1a2ad71519f354b3)disable

| int(\* k\_obj\_core\_stats\_desc::disable) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
| --- |

Function pointer to disable object's statistics gathering.

## [◆ ](#aabc9df81e93aa0ff0ec84983dd07f58f)enable

| int(\* k\_obj\_core\_stats\_desc::enable) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
| --- |

Function pointer to enable object's statistics gathering.

## [◆ ](#a94723e6cd5c03769e9cc1be9f0ec784f)query

| int(\* k\_obj\_core\_stats\_desc::query) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats) |
| --- |

Function pointer to retrieve reported statistics.

## [◆ ](#a9d0757daab439142711e3866e6dabb8d)query\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_obj\_core\_stats\_desc::query\_size |
| --- |

Stats buffer size used for reporting.

## [◆ ](#a0b206ae290639095e722c1705a122c2f)raw

| int(\* k\_obj\_core\_stats\_desc::raw) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats) |
| --- |

Function pointer to retrieve internal representation of stats.

## [◆ ](#a2e81dccd36b1355f9e685917cbd8eed8)raw\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_obj\_core\_stats\_desc::raw\_size |
| --- |

Internal representation stats buffer size.

## [◆ ](#a2ab464c373aa3830eaf15e46de2e9370)reset

| int(\* k\_obj\_core\_stats\_desc::reset) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
| --- |

Function pointer to reset object's statistics.

---

The documentation for this struct was generated from the following file:

- zephyr/kernel/[obj\_core.h](obj__core_8h_source.md)

- [k\_obj\_core\_stats\_desc](structk__obj__core__stats__desc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
