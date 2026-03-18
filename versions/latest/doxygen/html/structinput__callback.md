---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structinput__callback.html
original_path: doxygen/html/structinput__callback.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_callback Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Input Interface](group__input__interface.md)

Input callback structure.
[More...](#details)

`#include <[input.h](input_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#afe8fa2362e5c2ad35a00e05f33498a20) |
|  | [device](structdevice.md "device") pointer or NULL. |
| void(\* | [callback](#ace43e97a826282e97227980adfec52f9) )(struct [input\_event](structinput__event.md) \*evt) |
|  | The callback function. |

## Detailed Description

Input callback structure.

## Field Documentation

## [◆ ](#ace43e97a826282e97227980adfec52f9)callback

| void(\* input\_callback::callback) (struct [input\_event](structinput__event.md) \*evt) |
| --- |

The callback function.

## [◆ ](#afe8fa2362e5c2ad35a00e05f33498a20)dev

| const struct [device](structdevice.md)\* input\_callback::dev |
| --- |

[device](structdevice.md "device") pointer or NULL.

---

The documentation for this struct was generated from the following file:

- zephyr/input/[input.h](input_8h_source.md)

- [input\_callback](structinput__callback.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
