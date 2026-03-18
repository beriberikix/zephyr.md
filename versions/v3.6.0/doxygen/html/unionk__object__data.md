---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/unionk__object__data.html
original_path: doxygen/html/unionk__object__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_object\_data Union Reference

[Internal and System API](group__internal__api.md) » [User Mode Internal APIs](group__usermode__internal__apis.md)

`#include <[kobject_internal.h](kobject__internal_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_mutex](structk__mutex.md) \* | [mutex](#ab285ad5a6119657341be525276837fda) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [thread\_id](#ada581c427efa9e48b441b1a323bd57e6) |
| const struct z\_stack\_data \* | [stack\_data](#ac8fdffd51c0b32ea262fa98a827a5bd4) |
| struct z\_futex\_data \* | [futex\_data](#adc43cc4603b527b252e05df004cdbd64) |
| int | [unused](#a2f95fd75c72a619e8c5224e64d1aacc0) |

## Field Documentation

## [◆ ](#adc43cc4603b527b252e05df004cdbd64)futex\_data

| struct z\_futex\_data\* k\_object\_data::futex\_data |
| --- |

## [◆ ](#ab285ad5a6119657341be525276837fda)mutex

| struct [k\_mutex](structk__mutex.md)\* k\_object\_data::mutex |
| --- |

## [◆ ](#ac8fdffd51c0b32ea262fa98a827a5bd4)stack\_data

| const struct z\_stack\_data\* k\_object\_data::stack\_data |
| --- |

## [◆ ](#ada581c427efa9e48b441b1a323bd57e6)thread\_id

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int k\_object\_data::thread\_id |
| --- |

## [◆ ](#a2f95fd75c72a619e8c5224e64d1aacc0)unused

| int k\_object\_data::unused |
| --- |

---

The documentation for this union was generated from the following file:

- zephyr/sys/internal/[kobject\_internal.h](kobject__internal_8h_source.md)

- [k\_object\_data](unionk__object__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
