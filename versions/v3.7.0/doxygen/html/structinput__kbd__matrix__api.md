---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structinput__kbd__matrix__api.html
original_path: doxygen/html/structinput__kbd__matrix__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_kbd\_matrix\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Keyboard Matrix API](group__input__kbd__matrix.md)

Keyboard matrix internal APIs.
[More...](#details)

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [drive\_column](#af8211d738527ac44876dd07869862f20) )(const struct [device](structdevice.md) \*dev, int col) |
|  | Request to drive a specific column. |
| [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86)(\* | [read\_row](#af04e3f78fde3297a70a63c8a8addb477) )(const struct [device](structdevice.md) \*dev) |
|  | Read the matrix row. |
| void(\* | [set\_detect\_mode](#aaae2b1eb357fb4b7f1881ef496d79560) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Request to put the matrix in detection mode. |

## Detailed Description

Keyboard matrix internal APIs.

## Field Documentation

## [◆ ](#af8211d738527ac44876dd07869862f20)drive\_column

| void(\* input\_kbd\_matrix\_api::drive\_column) (const struct [device](structdevice.md) \*dev, int col) |
| --- |

Request to drive a specific column.

Request to drive a specific matrix column, or none, or all.

Parameters
:   | dev | Pointer to the keyboard matrix device. |
    | --- | --- |
    | col | The column to drive, or [INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_NONE](group__input__kbd__matrix.md#ga2f35f23d426f93f71057a31f612a88de "INPUT_KBD_MATRIX_COLUMN_DRIVE_NONE") or [INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_ALL](group__input__kbd__matrix.md#ga6d27ba5612c09d80087e854b21fb9e65 "INPUT_KBD_MATRIX_COLUMN_DRIVE_ALL"). |

## [◆ ](#af04e3f78fde3297a70a63c8a8addb477)read\_row

| [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86)(\* input\_kbd\_matrix\_api::read\_row) (const struct [device](structdevice.md) \*dev) |
| --- |

Read the matrix row.

Parameters
:   | dev | Pointer to the keyboard matrix device. |
    | --- | --- |

## [◆ ](#aaae2b1eb357fb4b7f1881ef496d79560)set\_detect\_mode

| void(\* input\_kbd\_matrix\_api::set\_detect\_mode) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
| --- |

Request to put the matrix in detection mode.

Request to put the driver in detection mode, this is called after a request to drive all the column and typically involves reenabling interrupts row pin changes.

Parameters
:   | dev | Pointer to the keyboard matrix device. |
    | --- | --- |
    | enable | Whether detection mode has to be enabled or disabled. |

---

The documentation for this struct was generated from the following file:

- zephyr/input/[input\_kbd\_matrix.h](input__kbd__matrix_8h_source.md)

- [input\_kbd\_matrix\_api](structinput__kbd__matrix__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
