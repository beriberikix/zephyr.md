---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structinput__listener.html
original_path: doxygen/html/structinput__listener.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_listener Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Input Interface](group__input__interface.md)

Input listener callback structure.
[More...](#details)

`#include <[input.h](input_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#abdb8a9db08f9a90b434fd93c11d293f5) |
|  | [device](structdevice.md "device") pointer or NULL. |
| void(\* | [callback](#aaa16d02d88cd5c2ee05951edcea3698e) )(struct [input\_event](structinput__event.md) \*evt) |
|  | The callback function. |

## Detailed Description

Input listener callback structure.

## Field Documentation

## [◆ ](#aaa16d02d88cd5c2ee05951edcea3698e)callback

| void(\* input\_listener::callback) (struct [input\_event](structinput__event.md) \*evt) |
| --- |

The callback function.

## [◆ ](#abdb8a9db08f9a90b434fd93c11d293f5)dev

| const struct [device](structdevice.md)\* input\_listener::dev |
| --- |

[device](structdevice.md "device") pointer or NULL.

---

The documentation for this struct was generated from the following file:

- zephyr/input/[input.h](input_8h_source.md)

- [input\_listener](structinput__listener.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
