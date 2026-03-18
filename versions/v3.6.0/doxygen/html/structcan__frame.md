---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structcan__frame.html
original_path: doxygen/html/structcan__frame.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_frame Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [CAN Interface](group__can__interface.md)

CAN frame structure.
[More...](#details)

`#include <[can.h](drivers_2can_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [id](#a7ad0d8d62322affafbfd23839ee81d5d): 29 |
|  | Standard (11-bit) or extended (29-bit) CAN identifier. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dlc](#a014c42277e886906e6c761bc6f21fb47) |
|  | Data Length Code (DLC) indicating data length in bytes. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a1e71125342a01a6e5a68a14cb075ce7c) |
|  | Flags. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timestamp](#ae46f8b0821c638517959274bbbda5932) |
|  | Captured value of the free-running timer in the CAN controller when this frame was received. |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [data](#ac4b43443b2a338d35f0e1d3ef8355960) [CAN\_MAX\_DLEN] |  |
|  | Payload data accessed as unsigned 8 bit values. [More...](#ac4b43443b2a338d35f0e1d3ef8355960) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [data\_32](#ad88af93a2171e4c9d617b91b403d842a) [[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(CAN\_MAX\_DLEN,         [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)))] |  |
|  | Payload data accessed as unsigned 32 bit values. [More...](#ad88af93a2171e4c9d617b91b403d842a) |
| }; |  |
|  | The frame payload data. |

## Detailed Description

CAN frame structure.

## Field Documentation

## [◆ ](#a52945d3269775ba0491f4d2e8a414722)[union]

| union { ... } [can\_frame](structcan__frame.md) |
| --- |

The frame payload data.

## [◆ ](#ac4b43443b2a338d35f0e1d3ef8355960)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_frame::data[CAN\_MAX\_DLEN] |
| --- |

Payload data accessed as unsigned 8 bit values.

## [◆ ](#ad88af93a2171e4c9d617b91b403d842a)data\_32

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_frame::data\_32[[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(CAN\_MAX\_DLEN, [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)))] |
| --- |

Payload data accessed as unsigned 32 bit values.

## [◆ ](#a014c42277e886906e6c761bc6f21fb47)dlc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_frame::dlc |
| --- |

Data Length Code (DLC) indicating data length in bytes.

## [◆ ](#a1e71125342a01a6e5a68a14cb075ce7c)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_frame::flags |
| --- |

Flags.

See also
:   [CAN\_FRAME\_FLAGS](group__can__interface.md#CAN_FRAME_FLAGS "CAN_FRAME_FLAGS").

## [◆ ](#a7ad0d8d62322affafbfd23839ee81d5d)id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_frame::id |
| --- |

Standard (11-bit) or extended (29-bit) CAN identifier.

## [◆ ](#ae46f8b0821c638517959274bbbda5932)timestamp

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) can\_frame::timestamp |
| --- |

Captured value of the free-running timer in the CAN controller when this frame was received.

The timer is incremented every bit time and captured at the start of frame bit (SOF).

Note
:   `CONFIG_CAN_RX_TIMESTAMP` must be selected for this field to be available.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[can.h](drivers_2can_8h_source.md)

- [can\_frame](structcan__frame.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
