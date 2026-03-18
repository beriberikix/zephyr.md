---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structinput__kbd__matrix__common__data.html
original_path: doxygen/html/structinput__kbd__matrix__common__data.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_kbd\_matrix\_common\_data Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Keyboard Matrix API](group__input__kbd__matrix.md)

Common keyboard matrix data.
[More...](#details)

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h_source.md)>`

| Public Member Functions | |
| --- | --- |
|  | [K\_KERNEL\_STACK\_MEMBER](#ac66f323c17cd346bb1b0b0aa8fc2965a) (thread\_stack, CONFIG\_INPUT\_KBD\_MATRIX\_THREAD\_STACK\_SIZE) |

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [scan\_clk\_cycle](#ac54780c609eb2abc67e468470ac3ef83) [30U] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [scan\_cycles\_idx](#a53b66dca86734fa149b672583455bc61) |
| struct k\_sem | [poll\_lock](#afe0d57cf725c825097ba26b81bd2640c) |
| struct [k\_thread](structk__thread.md) | [thread](#a526586907a6f0e4d1316c4304adda336) |

## Detailed Description

Common keyboard matrix data.

This structure **must** be placed first in the driver's data structure.

## Member Function Documentation

## [◆ ](#ac66f323c17cd346bb1b0b0aa8fc2965a)K\_KERNEL\_STACK\_MEMBER()

| input\_kbd\_matrix\_common\_data::K\_KERNEL\_STACK\_MEMBER | ( | thread\_stack | , |
| --- | --- | --- | --- |
|  |  | CONFIG\_INPUT\_KBD\_MATRIX\_THREAD\_STACK\_SIZE | ) |

## Field Documentation

## [◆ ](#afe0d57cf725c825097ba26b81bd2640c)poll\_lock

| struct k\_sem input\_kbd\_matrix\_common\_data::poll\_lock |
| --- |

## [◆ ](#ac54780c609eb2abc67e468470ac3ef83)scan\_clk\_cycle

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) input\_kbd\_matrix\_common\_data::scan\_clk\_cycle[30U] |
| --- |

## [◆ ](#a53b66dca86734fa149b672583455bc61)scan\_cycles\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) input\_kbd\_matrix\_common\_data::scan\_cycles\_idx |
| --- |

## [◆ ](#a526586907a6f0e4d1316c4304adda336)thread

| struct [k\_thread](structk__thread.md) input\_kbd\_matrix\_common\_data::thread |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/input/[input\_kbd\_matrix.h](input__kbd__matrix_8h_source.md)

- [input\_kbd\_matrix\_common\_data](structinput__kbd__matrix__common__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
