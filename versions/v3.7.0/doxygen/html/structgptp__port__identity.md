---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structgptp__port__identity.html
original_path: doxygen/html/structgptp__port__identity.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gptp\_port\_identity Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [gPTP support](group__gptp.md)

Port Identity.
[More...](#details)

`#include <[gptp.h](gptp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [clk\_id](#a6e8473ae6ecb4ec35e3a6b5d79851fc3) [GPTP\_CLOCK\_ID\_LEN] |
|  | Clock identity of the port. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [port\_number](#a5a0d4038aa88792290bc4619379ee48f) |
|  | Number of the port. |

## Detailed Description

Port Identity.

## Field Documentation

## [◆ ](#a6e8473ae6ecb4ec35e3a6b5d79851fc3)clk\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gptp\_port\_identity::clk\_id[GPTP\_CLOCK\_ID\_LEN] |
| --- |

Clock identity of the port.

## [◆ ](#a5a0d4038aa88792290bc4619379ee48f)port\_number

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) gptp\_port\_identity::port\_number |
| --- |

Number of the port.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[gptp.h](gptp_8h_source.md)

- [gptp\_port\_identity](structgptp__port__identity.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
