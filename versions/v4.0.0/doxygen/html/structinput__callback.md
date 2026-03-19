---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structinput__callback.html
original_path: doxygen/html/structinput__callback.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| void(\* | [callback](#a1f50a902f5f1ce10ee9131fcd1e7865d) )(struct [input\_event](structinput__event.md) \*evt, void \*[user\_data](#a353255145aabf43c92faab719b8f524c)) |
|  | The callback function. |
| void \* | [user\_data](#a353255145aabf43c92faab719b8f524c) |
|  | User data pointer. |

## Detailed Description

Input callback structure.

## Field Documentation

## [◆ ](#a1f50a902f5f1ce10ee9131fcd1e7865d)callback

| void(\* input\_callback::callback) (struct [input\_event](structinput__event.md) \*evt, void \*[user\_data](#a353255145aabf43c92faab719b8f524c)) |
| --- |

The callback function.

## [◆ ](#afe8fa2362e5c2ad35a00e05f33498a20)dev

| const struct [device](structdevice.md)\* input\_callback::dev |
| --- |

[device](structdevice.md "device") pointer or NULL.

## [◆ ](#a353255145aabf43c92faab719b8f524c)user\_data

| void\* input\_callback::user\_data |
| --- |

User data pointer.

---

The documentation for this struct was generated from the following file:

- zephyr/input/[input.h](input_8h_source.md)

- [input\_callback](structinput__callback.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
