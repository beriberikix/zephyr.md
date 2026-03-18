---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/unionbt__cap__set__member.html
original_path: doxygen/html/unionbt__cap__set__member.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_set\_member Union Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Represents a Common Audio Set member that are either in a Coordinated or ad-hoc set.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct bt\_conn \* | [member](#a692a1be2fbd79c4b6a0fbce564ff2973) |
|  | Connection pointer if the type is BT\_CAP\_SET\_TYPE\_AD\_HOC. |
| struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \* | [csip](#ac17db41d21a92d8d128b70962e4eb2d6) |
|  | CSIP Coordinated Set struct used if type is BT\_CAP\_SET\_TYPE\_CSIP. |

## Detailed Description

Represents a Common Audio Set member that are either in a Coordinated or ad-hoc set.

## Field Documentation

## [◆ ](#ac17db41d21a92d8d128b70962e4eb2d6)csip

| struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md)\* bt\_cap\_set\_member::csip |
| --- |

CSIP Coordinated Set struct used if type is BT\_CAP\_SET\_TYPE\_CSIP.

## [◆ ](#a692a1be2fbd79c4b6a0fbce564ff2973)member

| struct bt\_conn\* bt\_cap\_set\_member::member |
| --- |

Connection pointer if the type is BT\_CAP\_SET\_TYPE\_AD\_HOC.

---

The documentation for this union was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_set\_member](unionbt__cap__set__member.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
