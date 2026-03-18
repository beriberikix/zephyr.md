---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcan__mcan__rx__fifo.html
original_path: doxygen/html/structcan__mcan__rx__fifo.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_mcan\_rx\_fifo Struct Reference

Bosch M\_CAN Rx Buffer and FIFO Element.
[More...](#details)

`#include <[can_mcan.h](can__mcan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [can\_mcan\_rx\_fifo\_hdr](structcan__mcan__rx__fifo__hdr.md) | [hdr](#a8ddf6a5aa6f9847c3b5c0fce66631133) |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [data](#aeafd55c4d4f637c66e5a57d329e42a2b) [64] |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [data\_32](#a9a5e7e970f2733b68894edcbaf98cc82) [16] |  |
| }; |  |

## Detailed Description

Bosch M\_CAN Rx Buffer and FIFO Element.

See Bosch M\_CAN Users Manual section 2.4.2 for details.

## Field Documentation

## [◆ ](#aca40b28e8899337cd28c6e5bddd2538b)[union]

| union { ... } [can\_mcan\_rx\_fifo](structcan__mcan__rx__fifo.md) |
| --- |

## [◆ ](#aeafd55c4d4f637c66e5a57d329e42a2b)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_rx\_fifo::data[64] |
| --- |

## [◆ ](#a9a5e7e970f2733b68894edcbaf98cc82)data\_32

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo::data\_32[16] |
| --- |

## [◆ ](#a8ddf6a5aa6f9847c3b5c0fce66631133)hdr

| struct [can\_mcan\_rx\_fifo\_hdr](structcan__mcan__rx__fifo__hdr.md) can\_mcan\_rx\_fifo::hdr |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_mcan.h](can__mcan_8h_source.md)

- [can\_mcan\_rx\_fifo](structcan__mcan__rx__fifo.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
