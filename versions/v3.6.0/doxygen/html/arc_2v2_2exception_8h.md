---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arc_2v2_2exception_8h.html
original_path: doxygen/html/arc_2v2_2exception_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h File Reference

ARCv2 public exception handling.
[More...](#details)

[Go to the source code of this file.](arc_2v2_2exception_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARC\_EV\_RESET](#a2f8e6622ee49d9a5eed7f15288e7d8ae)   0x0 |
| #define | [ARC\_EV\_MEM\_ERROR](#a79e227883063d92c0d47cc750c37eb86)   0x1 |
| #define | [ARC\_EV\_INS\_ERROR](#a57a4267b70061307f2fed74473e17015)   0x2 |
| #define | [ARC\_EV\_MACHINE\_CHECK](#a10e5ab692a8dcb6bc6bb849222e12940)   0x3 |
| #define | [ARC\_EV\_TLB\_MISS\_I](#af2d95f9ded1396dd2c0aa7cb41952033)   0x4 |
| #define | [ARC\_EV\_TLB\_MISS\_D](#a48c63c54328299dfa3bec2b71c4ab610)   0x5 |
| #define | [ARC\_EV\_PROT\_V](#ad42a3dc7f1f4f4da9978ce667ae1ec2f)   0x6 |
| #define | [ARC\_EV\_PRIVILEGE\_V](#a604874d6ae9f845175e425bc897751f8)   0x7 |
| #define | [ARC\_EV\_SWI](#a42b3a14ded2c98e7e37a7375efd81e91)   0x8 |
| #define | [ARC\_EV\_TRAP](#abd2003e15eb7839a2454c9da245ee56b)   0x9 |
| #define | [ARC\_EV\_EXTENSION](#ab6d6036ccdf6dc66959ca3ac90aa6cde)   0xA |
| #define | [ARC\_EV\_DIV\_ZERO](#a0c132bd763cf093dd7f87318607977fa)   0xB |
| #define | [ARC\_EV\_DC\_ERROR](#aca9e2d443855714d67aa0001affd2c4a)   0xC |
| #define | [ARC\_EV\_MISALIGNED](#a2b2768d051be571940d8f0ca5acc8ddf)   0xD |
| #define | [ARC\_EV\_VEC\_UNIT](#a777a56039909a5634ad59c04cf240104)   0xE |

## Detailed Description

ARCv2 public exception handling.

ARC-specific kernel exception handling interface. Included by arc/arch.h.

## Macro Definition Documentation

## [◆ ](#aca9e2d443855714d67aa0001affd2c4a)ARC\_EV\_DC\_ERROR

| #define ARC\_EV\_DC\_ERROR   0xC |
| --- |

## [◆ ](#a0c132bd763cf093dd7f87318607977fa)ARC\_EV\_DIV\_ZERO

| #define ARC\_EV\_DIV\_ZERO   0xB |
| --- |

## [◆ ](#ab6d6036ccdf6dc66959ca3ac90aa6cde)ARC\_EV\_EXTENSION

| #define ARC\_EV\_EXTENSION   0xA |
| --- |

## [◆ ](#a57a4267b70061307f2fed74473e17015)ARC\_EV\_INS\_ERROR

| #define ARC\_EV\_INS\_ERROR   0x2 |
| --- |

## [◆ ](#a10e5ab692a8dcb6bc6bb849222e12940)ARC\_EV\_MACHINE\_CHECK

| #define ARC\_EV\_MACHINE\_CHECK   0x3 |
| --- |

## [◆ ](#a79e227883063d92c0d47cc750c37eb86)ARC\_EV\_MEM\_ERROR

| #define ARC\_EV\_MEM\_ERROR   0x1 |
| --- |

## [◆ ](#a2b2768d051be571940d8f0ca5acc8ddf)ARC\_EV\_MISALIGNED

| #define ARC\_EV\_MISALIGNED   0xD |
| --- |

## [◆ ](#a604874d6ae9f845175e425bc897751f8)ARC\_EV\_PRIVILEGE\_V

| #define ARC\_EV\_PRIVILEGE\_V   0x7 |
| --- |

## [◆ ](#ad42a3dc7f1f4f4da9978ce667ae1ec2f)ARC\_EV\_PROT\_V

| #define ARC\_EV\_PROT\_V   0x6 |
| --- |

## [◆ ](#a2f8e6622ee49d9a5eed7f15288e7d8ae)ARC\_EV\_RESET

| #define ARC\_EV\_RESET   0x0 |
| --- |

## [◆ ](#a42b3a14ded2c98e7e37a7375efd81e91)ARC\_EV\_SWI

| #define ARC\_EV\_SWI   0x8 |
| --- |

## [◆ ](#a48c63c54328299dfa3bec2b71c4ab610)ARC\_EV\_TLB\_MISS\_D

| #define ARC\_EV\_TLB\_MISS\_D   0x5 |
| --- |

## [◆ ](#af2d95f9ded1396dd2c0aa7cb41952033)ARC\_EV\_TLB\_MISS\_I

| #define ARC\_EV\_TLB\_MISS\_I   0x4 |
| --- |

## [◆ ](#abd2003e15eb7839a2454c9da245ee56b)ARC\_EV\_TRAP

| #define ARC\_EV\_TRAP   0x9 |
| --- |

## [◆ ](#a777a56039909a5634ad59c04cf240104)ARC\_EV\_VEC\_UNIT

| #define ARC\_EV\_VEC\_UNIT   0xE |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [exception.h](arc_2v2_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
