---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structinput__event.html
original_path: doxygen/html/structinput__event.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_event Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Input Interface](group__input__interface.md)

Input event structure.
[More...](#details)

`#include <[input.h](input_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#a4022d0ddf8ca5be9b478cd0b2758d067) |
|  | Device generating the event or NULL. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sync](#a015732c5d67a5374b93e980282a2a9d7) |
|  | Sync flag. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#af74a1741fef30ee375d4a71628a9656e) |
|  | Event type (see [INPUT\_EV\_CODES](group__input__events.md#INPUT_EV_CODES "INPUT_EV_CODES")). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [code](#a5abe903fbf3b29643578be85c17ba6aa) |
|  | Event code (see [INPUT\_KEY\_CODES](group__input__events.md#INPUT_KEY_CODES "INPUT_KEY_CODES"), [INPUT\_BTN\_CODES](group__input__events.md#INPUT_BTN_CODES "INPUT_BTN_CODES"), [INPUT\_ABS\_CODES](group__input__events.md#INPUT_ABS_CODES "INPUT_ABS_CODES"), [INPUT\_REL\_CODES](group__input__events.md#INPUT_REL_CODES "INPUT_REL_CODES"), [INPUT\_MSC\_CODES](group__input__events.md#INPUT_MSC_CODES "INPUT_MSC_CODES")). |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [value](#af18b63e5263e73fce8e38838e37d2bae) |
|  | Event value. |

## Detailed Description

Input event structure.

This structure represents a single input event, for example a key or button press for a single button, or an absolute or relative coordinate for a single axis.

## Field Documentation

## [◆ ](#a5abe903fbf3b29643578be85c17ba6aa)code

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) input\_event::code |
| --- |

Event code (see [INPUT\_KEY\_CODES](group__input__events.md#INPUT_KEY_CODES "INPUT_KEY_CODES"), [INPUT\_BTN\_CODES](group__input__events.md#INPUT_BTN_CODES "INPUT_BTN_CODES"), [INPUT\_ABS\_CODES](group__input__events.md#INPUT_ABS_CODES "INPUT_ABS_CODES"), [INPUT\_REL\_CODES](group__input__events.md#INPUT_REL_CODES "INPUT_REL_CODES"), [INPUT\_MSC\_CODES](group__input__events.md#INPUT_MSC_CODES "INPUT_MSC_CODES")).

## [◆ ](#a4022d0ddf8ca5be9b478cd0b2758d067)dev

| const struct [device](structdevice.md)\* input\_event::dev |
| --- |

Device generating the event or NULL.

## [◆ ](#a015732c5d67a5374b93e980282a2a9d7)sync

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) input\_event::sync |
| --- |

Sync flag.

## [◆ ](#af74a1741fef30ee375d4a71628a9656e)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) input\_event::type |
| --- |

Event type (see [INPUT\_EV\_CODES](group__input__events.md#INPUT_EV_CODES "INPUT_EV_CODES")).

## [◆ ](#af18b63e5263e73fce8e38838e37d2bae)value

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) input\_event::value |
| --- |

Event value.

---

The documentation for this struct was generated from the following file:

- zephyr/input/[input.h](input_8h_source.md)

- [input\_event](structinput__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
