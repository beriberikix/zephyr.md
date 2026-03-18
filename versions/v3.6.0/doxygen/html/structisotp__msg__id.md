---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structisotp__msg__id.html
original_path: doxygen/html/structisotp__msg__id.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

isotp\_msg\_id Struct Reference

[Connectivity](group__connectivity.md) » [CAN ISO-TP Protocol](group__can__isotp.md)

ISO-TP message id struct.
[More...](#details)

`#include <[isotp.h](isotp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [std\_id](#ac9ded92f8e0afa88609003c5cf819704): 11 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [ext\_id](#a3f9d4a6efd9b1c147f889a6396d7ef1c): 29 |  |
| }; |  |
|  | CAN identifier. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ext\_addr](#a7b818e7c6dab02347b32bcc74dfc44a3) |
|  | ISO-TP extended address (if used). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dl](#adc7ff4eac4573221b89a5bb5a5e53d49) |
|  | ISO-TP frame data length (TX\_DL for TX address or RX\_DL for RX address). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a3185e5b5fddb5d7fc94b86c8d30e61a9) |
|  | Flags. |

## Detailed Description

ISO-TP message id struct.

Used to pass addresses to the bind and send functions.

## Field Documentation

## [◆ ](#aa2952d55f06018920a2033244dfb2582)[union]

| union { ... } [isotp\_msg\_id](structisotp__msg__id.md) |
| --- |

CAN identifier.

If ISO-TP fixed addressing is used, isotp\_bind ignores SA and priority sections and modifies TA section in flow control frames.

## [◆ ](#adc7ff4eac4573221b89a5bb5a5e53d49)dl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) isotp\_msg\_id::dl |
| --- |

ISO-TP frame data length (TX\_DL for TX address or RX\_DL for RX address).

Valid values are 8 for classical CAN or 8, 12, 16, 20, 24, 32, 48 and 64 for CAN FD.

0 will be interpreted as 8 or 64 (if ISOTP\_MSG\_FDF is set).

The value for incoming transmissions (RX\_DL) is determined automatically based on the received first frame and does not need to be set during initialization.

## [◆ ](#a7b818e7c6dab02347b32bcc74dfc44a3)ext\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) isotp\_msg\_id::ext\_addr |
| --- |

ISO-TP extended address (if used).

## [◆ ](#a3f9d4a6efd9b1c147f889a6396d7ef1c)ext\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) isotp\_msg\_id::ext\_id |
| --- |

## [◆ ](#a3185e5b5fddb5d7fc94b86c8d30e61a9)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) isotp\_msg\_id::flags |
| --- |

Flags.

See also
:   [ISOTP\_MSG\_FLAGS](group__can__isotp.md#ISOTP_MSG_FLAGS "ISOTP_MSG_FLAGS").

## [◆ ](#ac9ded92f8e0afa88609003c5cf819704)std\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) isotp\_msg\_id::std\_id |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/canbus/[isotp.h](isotp_8h_source.md)

- [isotp\_msg\_id](structisotp__msg__id.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
