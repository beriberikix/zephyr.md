---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2x86_2ia32_2thread_8h.html
original_path: doxygen/html/arch_2x86_2ia32_2thread_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h File Reference

Per-arch thread definition.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/arch/x86/mmustructs.h](mmustructs_8h_source.md)>`

[Go to the source code of this file.](arch_2x86_2ia32_2thread_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [s\_FpRegSet](structs__FpRegSet.md) |
| struct | [s\_FpRegSetEx](structs__FpRegSetEx.md) |
| struct | [s\_preempFloatReg](structs__preempFloatReg.md) |

| Macros | |
| --- | --- |
| #define | [FP\_REG\_SET\_ALIGN](#af99d45d7fb31caf8f4abf9306fb654a3)   1 |
|  | Floating point register set alignment. |
| #define | [X86\_THREAD\_FLAG\_INT](#adb3b8047e5ebfc1305e7616991913818)   0x01 |
| #define | [X86\_THREAD\_FLAG\_EXC](#a01b9d81506f2cacafd8b5c1341d30207)   0x02 |
| #define | [X86\_THREAD\_FLAG\_ALL](#a9976b965d1010def5c40f40be6930461)   ([X86\_THREAD\_FLAG\_INT](#adb3b8047e5ebfc1305e7616991913818) | [X86\_THREAD\_FLAG\_EXC](#a01b9d81506f2cacafd8b5c1341d30207)) |

| Typedefs | |
| --- | --- |
| typedef struct [s\_FpRegSet](structs__FpRegSet.md) | [tFpRegSet](#ac6b7d0ab9f5986eb129f362e4dc39811) |
| typedef struct [s\_FpRegSetEx](structs__FpRegSetEx.md) | [tFpRegSetEx](#a9b38503997978c6dbfdb03448cb38967) |
| typedef struct [s\_preempFloatReg](structs__preempFloatReg.md) | [tPreempFloatReg](#a559de7a9ab93bd874af8fd66a3851d01) |

## Detailed Description

Per-arch thread definition.

This file contains definitions for

struct \_thread\_arch struct \_callee\_saved

necessary to instantiate instances of struct [k\_thread](structk__thread.md "Thread Structure.").

## Macro Definition Documentation

## [◆ ](#af99d45d7fb31caf8f4abf9306fb654a3)FP\_REG\_SET\_ALIGN

| #define FP\_REG\_SET\_ALIGN   1 |
| --- |

Floating point register set alignment.

If support for SSEx extensions is enabled a 16 byte boundary is required, since the 'fxsave' and 'fxrstor' instructions require this. In all other cases a 4 byte boundary is sufficient.

## [◆ ](#a9976b965d1010def5c40f40be6930461)X86\_THREAD\_FLAG\_ALL

| #define X86\_THREAD\_FLAG\_ALL   ([X86\_THREAD\_FLAG\_INT](#adb3b8047e5ebfc1305e7616991913818) | [X86\_THREAD\_FLAG\_EXC](#a01b9d81506f2cacafd8b5c1341d30207)) |
| --- |

## [◆ ](#a01b9d81506f2cacafd8b5c1341d30207)X86\_THREAD\_FLAG\_EXC

| #define X86\_THREAD\_FLAG\_EXC   0x02 |
| --- |

## [◆ ](#adb3b8047e5ebfc1305e7616991913818)X86\_THREAD\_FLAG\_INT

| #define X86\_THREAD\_FLAG\_INT   0x01 |
| --- |

## Typedef Documentation

## [◆ ](#ac6b7d0ab9f5986eb129f362e4dc39811)tFpRegSet

| typedef struct [s\_FpRegSet](structs__FpRegSet.md) [tFpRegSet](#ac6b7d0ab9f5986eb129f362e4dc39811) |
| --- |

## [◆ ](#a9b38503997978c6dbfdb03448cb38967)tFpRegSetEx

| typedef struct [s\_FpRegSetEx](structs__FpRegSetEx.md) [tFpRegSetEx](#a9b38503997978c6dbfdb03448cb38967) |
| --- |

## [◆ ](#a559de7a9ab93bd874af8fd66a3851d01)tPreempFloatReg

| typedef struct [s\_preempFloatReg](structs__preempFloatReg.md) [tPreempFloatReg](#a559de7a9ab93bd874af8fd66a3851d01) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [thread.h](arch_2x86_2ia32_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
