---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structisotp__fc__opts.html
original_path: doxygen/html/structisotp__fc__opts.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

isotp\_fc\_opts Struct Reference

[Connectivity](group__connectivity.md) » [CAN ISO-TP Protocol](group__can__isotp.md)

ISO-TP frame control options struct.
[More...](#details)

`#include <[isotp.h](isotp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bs](#a8f31bf5c95069352043da33541911b3c) |
|  | Block size. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [stmin](#a5db0ceeed259c26d1d8fe0a901edcbca) |
|  | Minimum separation time. |

## Detailed Description

ISO-TP frame control options struct.

Used to pass the options to the bind and send functions.

## Field Documentation

## [◆ ](#a8f31bf5c95069352043da33541911b3c)bs

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) isotp\_fc\_opts::bs |
| --- |

Block size.

Number of CF PDUs before next CF is sent

## [◆ ](#a5db0ceeed259c26d1d8fe0a901edcbca)stmin

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) isotp\_fc\_opts::stmin |
| --- |

Minimum separation time.

Min time between frames

---

The documentation for this struct was generated from the following file:

- zephyr/canbus/[isotp.h](isotp_8h_source.md)

- [isotp\_fc\_opts](structisotp__fc__opts.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
