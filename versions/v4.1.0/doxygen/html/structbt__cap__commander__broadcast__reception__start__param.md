---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__cap__commander__broadcast__reception__start__param.html
original_path: doxygen/html/structbt__cap__commander__broadcast__reception__start__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_broadcast\_reception\_start\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for starting broadcast reception.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) | [type](#ae4c1e6d7b345b8764f695ada56483aa1) |
|  | The type of the set. |
| struct [bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md) \* | [param](#a8bac9170f48f34fd2239da9a6d994041) |
|  | The set of devices for this procedure. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#ab0fe6fe27946a349ac33f11526ca13b7) |
|  | The number of parameters in `param`. |

## Detailed Description

Parameters for starting broadcast reception.

## Field Documentation

## [◆ ](#ab0fe6fe27946a349ac33f11526ca13b7)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_commander\_broadcast\_reception\_start\_param::count |
| --- |

The number of parameters in `param`.

## [◆ ](#a8bac9170f48f34fd2239da9a6d994041)param

| struct [bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md)\* bt\_cap\_commander\_broadcast\_reception\_start\_param::param |
| --- |

The set of devices for this procedure.

## [◆ ](#ae4c1e6d7b345b8764f695ada56483aa1)type

| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) bt\_cap\_commander\_broadcast\_reception\_start\_param::type |
| --- |

The type of the set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
