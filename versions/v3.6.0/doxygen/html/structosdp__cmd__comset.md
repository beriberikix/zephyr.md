---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structosdp__cmd__comset.html
original_path: doxygen/html/structosdp__cmd__comset.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp\_cmd\_comset Struct Reference

Sent in response to a COMSET command.
[More...](#details)

`#include <[osdp.h](osdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [address](#af318dc8d5c8148902a2f824d72120ddc) |
|  | Unit ID to which this PD will respond after the change takes effect. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [baud\_rate](#a9de97b54c83b9643f1dd3413ec3b15e6) |
|  | Baud rate. |

## Detailed Description

Sent in response to a COMSET command.

Set communication parameters to PD. Must be stored in PD non-volatile memory.

## Field Documentation

## [◆ ](#af318dc8d5c8148902a2f824d72120ddc)address

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_comset::address |
| --- |

Unit ID to which this PD will respond after the change takes effect.

## [◆ ](#a9de97b54c83b9643f1dd3413ec3b15e6)baud\_rate

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) osdp\_cmd\_comset::baud\_rate |
| --- |

Baud rate.

Valid values: 9600, 19200, 38400, 115200, 230400.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/[osdp.h](osdp_8h_source.md)

- [osdp\_cmd\_comset](structosdp__cmd__comset.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
