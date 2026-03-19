---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2x86_2intel64_2thread_8h.html
original_path: doxygen/html/arch_2x86_2intel64_2thread_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/arch/x86/mmustructs.h](mmustructs_8h_source.md)>`

[Go to the source code of this file.](arch_2x86_2intel64_2thread_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [x86\_tss64](structx86__tss64.md) |

| Macros | |
| --- | --- |
| #define | [X86\_THREAD\_FLAG\_ALL](#a9976b965d1010def5c40f40be6930461)   0x01 /\* \_thread\_arch.flags: entire [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) saved \*/ |
| #define | [X86\_KERNEL\_CS\_32](#a53141d432cd6d04e0e47c12fa796886c)   0x08 /\* 32-bit kernel code \*/ |
| #define | [X86\_KERNEL\_DS\_32](#a71032cef700766c2d1d8661ba26228d1)   0x10 /\* 32-bit kernel data \*/ |
| #define | [X86\_KERNEL\_CS](#a86a201d2fee57e06985202e366797cee)   0x18 /\* 64-bit kernel code \*/ |
| #define | [X86\_KERNEL\_DS](#aec469f2b32038a8968280fa8aa7b9eeb)   0x20 /\* 64-bit kernel data \*/ |
| #define | [X86\_USER\_CS\_32](#a346cd512e6426a7142790ffc5d8cbbc4)   0x28 /\* 32-bit user data (unused) \*/ |
| #define | [X86\_USER\_DS](#a5ee9fd539d1fa910dd924bb391566a74)   0x30 /\* 64-bit user mode data \*/ |
| #define | [X86\_USER\_CS](#a4e231b18c27e74b82d7a1021784cb65d)   0x38 /\* 64-bit user mode code \*/ |
| #define | [X86\_STAR\_UPPER](#a878f72d5fdb7380968713ef35fa86899)   (([X86\_USER\_CS\_32](#a346cd512e6426a7142790ffc5d8cbbc4) << 16) | [X86\_KERNEL\_CS](#a86a201d2fee57e06985202e366797cee)) |
| #define | [X86\_KERNEL\_CPU0\_TR](#ae5e8af7e75778451925d9a94322c39ab)   0x40 /\* 64-bit task [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) segment \*/ |
| #define | [X86\_KERNEL\_CPU1\_TR](#a3f7c36aa07ea09dfaedc41d50339d563)   0x50 /\* 64-bit task [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) segment \*/ |
| #define | [X86\_KERNEL\_CPU2\_TR](#ad706983ae625a525a0ff4d4b5e6f9df4)   0x60 /\* 64-bit task [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) segment \*/ |
| #define | [X86\_KERNEL\_CPU3\_TR](#a04c092d0b318251a296a9ed64f7b1fa5)   0x70 /\* 64-bit task [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) segment \*/ |
| #define | [X86\_FXSAVE\_SIZE](#ace21a6c2662fc989b5a51a2ebb53d129)   512 /\* size and alignment of buffer ... \*/ |
| #define | [X86\_FXSAVE\_ALIGN](#a7a6607831b2b148ce38e7715907ef31c)   16 /\* ... for FXSAVE/FXRSTOR ops \*/ |
| #define | [X86\_MXCSR\_SANE](#a1a95e6241909317576dea666aa1959c9)   0x1f80 |

| Typedefs | |
| --- | --- |
| typedef struct [x86\_tss64](structx86__tss64.md) | [x86\_tss64\_t](#af11b6454439f03e21b92bceff9ed7f00) |

## Macro Definition Documentation

## [◆ ](#a7a6607831b2b148ce38e7715907ef31c)X86\_FXSAVE\_ALIGN

| #define X86\_FXSAVE\_ALIGN   16 /\* ... for FXSAVE/FXRSTOR ops \*/ |
| --- |

## [◆ ](#ace21a6c2662fc989b5a51a2ebb53d129)X86\_FXSAVE\_SIZE

| #define X86\_FXSAVE\_SIZE   512 /\* size and alignment of buffer ... \*/ |
| --- |

## [◆ ](#ae5e8af7e75778451925d9a94322c39ab)X86\_KERNEL\_CPU0\_TR

| #define X86\_KERNEL\_CPU0\_TR   0x40 /\* 64-bit task [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) segment \*/ |
| --- |

## [◆ ](#a3f7c36aa07ea09dfaedc41d50339d563)X86\_KERNEL\_CPU1\_TR

| #define X86\_KERNEL\_CPU1\_TR   0x50 /\* 64-bit task [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) segment \*/ |
| --- |

## [◆ ](#ad706983ae625a525a0ff4d4b5e6f9df4)X86\_KERNEL\_CPU2\_TR

| #define X86\_KERNEL\_CPU2\_TR   0x60 /\* 64-bit task [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) segment \*/ |
| --- |

## [◆ ](#a04c092d0b318251a296a9ed64f7b1fa5)X86\_KERNEL\_CPU3\_TR

| #define X86\_KERNEL\_CPU3\_TR   0x70 /\* 64-bit task [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) segment \*/ |
| --- |

## [◆ ](#a86a201d2fee57e06985202e366797cee)X86\_KERNEL\_CS

| #define X86\_KERNEL\_CS   0x18 /\* 64-bit kernel code \*/ |
| --- |

## [◆ ](#a53141d432cd6d04e0e47c12fa796886c)X86\_KERNEL\_CS\_32

| #define X86\_KERNEL\_CS\_32   0x08 /\* 32-bit kernel code \*/ |
| --- |

## [◆ ](#aec469f2b32038a8968280fa8aa7b9eeb)X86\_KERNEL\_DS

| #define X86\_KERNEL\_DS   0x20 /\* 64-bit kernel data \*/ |
| --- |

## [◆ ](#a71032cef700766c2d1d8661ba26228d1)X86\_KERNEL\_DS\_32

| #define X86\_KERNEL\_DS\_32   0x10 /\* 32-bit kernel data \*/ |
| --- |

## [◆ ](#a1a95e6241909317576dea666aa1959c9)X86\_MXCSR\_SANE

| #define X86\_MXCSR\_SANE   0x1f80 |
| --- |

## [◆ ](#a878f72d5fdb7380968713ef35fa86899)X86\_STAR\_UPPER

| #define X86\_STAR\_UPPER   (([X86\_USER\_CS\_32](#a346cd512e6426a7142790ffc5d8cbbc4) << 16) | [X86\_KERNEL\_CS](#a86a201d2fee57e06985202e366797cee)) |
| --- |

## [◆ ](#a9976b965d1010def5c40f40be6930461)X86\_THREAD\_FLAG\_ALL

| #define X86\_THREAD\_FLAG\_ALL   0x01 /\* \_thread\_arch.flags: entire [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) saved \*/ |
| --- |

## [◆ ](#a4e231b18c27e74b82d7a1021784cb65d)X86\_USER\_CS

| #define X86\_USER\_CS   0x38 /\* 64-bit user mode code \*/ |
| --- |

## [◆ ](#a346cd512e6426a7142790ffc5d8cbbc4)X86\_USER\_CS\_32

| #define X86\_USER\_CS\_32   0x28 /\* 32-bit user data (unused) \*/ |
| --- |

## [◆ ](#a5ee9fd539d1fa910dd924bb391566a74)X86\_USER\_DS

| #define X86\_USER\_DS   0x30 /\* 64-bit user mode data \*/ |
| --- |

## Typedef Documentation

## [◆ ](#af11b6454439f03e21b92bceff9ed7f00)x86\_tss64\_t

| typedef struct [x86\_tss64](structx86__tss64.md) [x86\_tss64\_t](#af11b6454439f03e21b92bceff9ed7f00) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [intel64](dir_1abf87bed33eaf4508c3178cbd4d6168.md)
- [thread.h](arch_2x86_2intel64_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
