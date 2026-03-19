---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__cap__commander__broadcast__reception__stop__member__param.html
original_path: doxygen/html/structbt__cap__commander__broadcast__reception__stop__member__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for stopping broadcast reception.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) | [member](#aa934af2e197c129b1fcb1eea9359ea6d) |
|  | Coordinated or ad-hoc set member. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [src\_id](#a72d606f6a83b1c84aa41d9db22cb955a) |
|  | Source ID of the receive state. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [num\_subgroups](#aeeab53e8bd7ae4f36433c0d4b60c313b) |
|  | Number of subgroups. |

## Detailed Description

Parameters for stopping broadcast reception.

## Field Documentation

## [◆ ](#aa934af2e197c129b1fcb1eea9359ea6d)member

| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param::member |
| --- |

Coordinated or ad-hoc set member.

## [◆ ](#aeeab53e8bd7ae4f36433c0d4b60c313b)num\_subgroups

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param::num\_subgroups |
| --- |

Number of subgroups.

## [◆ ](#a72d606f6a83b1c84aa41d9db22cb955a)src\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param::src\_id |
| --- |

Source ID of the receive state.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param](structbt__cap__commander__broadcast__reception__stop__member__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
