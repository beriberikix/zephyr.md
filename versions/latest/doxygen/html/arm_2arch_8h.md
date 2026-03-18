---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arm_2arch_8h.html
original_path: doxygen/html/arm_2arch_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h File Reference

ARM AArch32 specific kernel interface header.
[More...](#details)

`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/arch/arm/thread.h](arch_2arm_2thread_8h_source.md)>`  
`#include <[zephyr/arch/arm/exception.h](arm_2exception_8h_source.md)>`  
`#include <[zephyr/arch/arm/irq.h](arch_2arm_2irq_8h_source.md)>`  
`#include <[zephyr/arch/arm/error.h](arm_2error_8h_source.md)>`  
`#include <[zephyr/arch/arm/misc.h](arm_2misc_8h_source.md)>`  
`#include <[zephyr/arch/common/addr_types.h](addr__types_8h_source.md)>`  
`#include <[zephyr/arch/common/ffs.h](ffs_8h_source.md)>`  
`#include <[zephyr/arch/arm/nmi.h](nmi_8h_source.md)>`  
`#include <[zephyr/arch/arm/asm_inline.h](arm_2asm__inline_8h_source.md)>`  
`#include <[zephyr/arch/common/sys_bitops.h](sys__bitops_8h_source.md)>`  
`#include <[zephyr/arch/arm/gdbstub.h](arch_2arm_2gdbstub_8h_source.md)>`  
`#include <[zephyr/fatal_types.h](fatal__types_8h_source.md)>`

[Go to the source code of this file.](arm_2arch_8h_source.md)

| Macros | |
| --- | --- |
| #define | [sys\_define\_gpr\_with\_alias](#a59d42697fc33d0b600597145a7b76dc7)(name1, name2) |
| #define | [ARCH\_STACK\_PTR\_ALIGN](#af0f8ad93611d93cd0626914837e761d3)   4 |
|  | Declare the ARCH\_STACK\_PTR\_ALIGN. |
| #define | [MPU\_GUARD\_ALIGN\_AND\_SIZE](#a08b1afe29bff127c0f3c0376ee6744b1)   0 |
|  | Declare a minimum MPU guard alignment and size. |
| #define | [MPU\_GUARD\_ALIGN\_AND\_SIZE\_FLOAT](#a28b1b91e550d6b6fb08cf9aef9e9b0f2)   0 |
|  | Declare the MPU guard alignment and size for a thread stack that is using the Floating Point services. |
| #define | [ARCH\_THREAD\_STACK\_OBJ\_ALIGN](#ab6c1d96f5e018ed166ee401dc84b7ab7)(size) |
| #define | [ARCH\_THREAD\_STACK\_SIZE\_ADJUST](#ab76d60bd06e5c5a0f995c6b11bf97fd8)(size) |
| #define | [ARCH\_THREAD\_STACK\_RESERVED](#ace8831316d471ccfb06eeddb6d69d817)   0 |

| Enumerations | |
| --- | --- |
| enum | [k\_fatal\_error\_reason\_arch](#a5891f4f431f3817d4bb9f652ff45a9c4) {     [K\_ERR\_ARM\_MEM\_GENERIC](#a5891f4f431f3817d4bb9f652ff45a9c4a7ac465c1decca4d761d420f62700c940) = K\_ERR\_ARCH\_START , [K\_ERR\_ARM\_MEM\_STACKING](#a5891f4f431f3817d4bb9f652ff45a9c4a3de9e6e036d9022537164b68c2fc8fb9) , [K\_ERR\_ARM\_MEM\_UNSTACKING](#a5891f4f431f3817d4bb9f652ff45a9c4a043da3af81148080b75ecf5002d3c6ea) , [K\_ERR\_ARM\_MEM\_DATA\_ACCESS](#a5891f4f431f3817d4bb9f652ff45a9c4af52bcf1db9ed0dfc47f4d1b9698c23a6) ,     [K\_ERR\_ARM\_MEM\_INSTRUCTION\_ACCESS](#a5891f4f431f3817d4bb9f652ff45a9c4a776523f4671f98f87ccf9a76db9a186c) , [K\_ERR\_ARM\_MEM\_FP\_LAZY\_STATE\_PRESERVATION](#a5891f4f431f3817d4bb9f652ff45a9c4a5ad278e3284e621ace082e5d1d89c599) , [K\_ERR\_ARM\_BUS\_GENERIC](#a5891f4f431f3817d4bb9f652ff45a9c4a899fe8e2d408404917b3bd166f07666c) , [K\_ERR\_ARM\_BUS\_STACKING](#a5891f4f431f3817d4bb9f652ff45a9c4a7b5e93c7163bea86dbeff21759f6472e) ,     [K\_ERR\_ARM\_BUS\_UNSTACKING](#a5891f4f431f3817d4bb9f652ff45a9c4a7a879301aa3ee1b2ce6abcacdc795b1d) , [K\_ERR\_ARM\_BUS\_PRECISE\_DATA\_BUS](#a5891f4f431f3817d4bb9f652ff45a9c4aed122da9226657dea13a9afa9dbc43d5) , [K\_ERR\_ARM\_BUS\_IMPRECISE\_DATA\_BUS](#a5891f4f431f3817d4bb9f652ff45a9c4a8cbae40f6ee1f7b65f02b330d5f7a8ae) , [K\_ERR\_ARM\_BUS\_INSTRUCTION\_BUS](#a5891f4f431f3817d4bb9f652ff45a9c4a916d2fb2799c0355aace800ed43ad69c) ,     [K\_ERR\_ARM\_BUS\_FP\_LAZY\_STATE\_PRESERVATION](#a5891f4f431f3817d4bb9f652ff45a9c4a03607bd98c8aebb5c4bd794278987317) , [K\_ERR\_ARM\_USAGE\_GENERIC](#a5891f4f431f3817d4bb9f652ff45a9c4afbe97c341bf54d94c42c4ec456d586ca) , [K\_ERR\_ARM\_USAGE\_DIV\_0](#a5891f4f431f3817d4bb9f652ff45a9c4a802af0dbe318680dfcd1805cb8b99fd8) , [K\_ERR\_ARM\_USAGE\_UNALIGNED\_ACCESS](#a5891f4f431f3817d4bb9f652ff45a9c4a5e41e262d0fb52266261a8e3a59e75ff) ,     [K\_ERR\_ARM\_USAGE\_STACK\_OVERFLOW](#a5891f4f431f3817d4bb9f652ff45a9c4ada75e6e3d5102139cbcd7df2f67f8bc3) , [K\_ERR\_ARM\_USAGE\_NO\_COPROCESSOR](#a5891f4f431f3817d4bb9f652ff45a9c4a4a10fc8ae3093fd24cb052457fa1783a) , [K\_ERR\_ARM\_USAGE\_ILLEGAL\_EXC\_RETURN](#a5891f4f431f3817d4bb9f652ff45a9c4a4646893d8e3fc6c19356c9c0e56e1766) , [K\_ERR\_ARM\_USAGE\_ILLEGAL\_EPSR](#a5891f4f431f3817d4bb9f652ff45a9c4a750a9631b59488b406f228eb74656e82) ,     [K\_ERR\_ARM\_USAGE\_UNDEFINED\_INSTRUCTION](#a5891f4f431f3817d4bb9f652ff45a9c4aabd67bae03c199605f62c83b57b54159) , [K\_ERR\_ARM\_SECURE\_GENERIC](#a5891f4f431f3817d4bb9f652ff45a9c4a3b437867ae7ec378d8a04f1da9891165) , [K\_ERR\_ARM\_SECURE\_ENTRY\_POINT](#a5891f4f431f3817d4bb9f652ff45a9c4a454c50a4bf529eaf4a2e2fda636bbc3d) , [K\_ERR\_ARM\_SECURE\_INTEGRITY\_SIGNATURE](#a5891f4f431f3817d4bb9f652ff45a9c4a50e6eccecb232ce9c9bf987be6263288) ,     [K\_ERR\_ARM\_SECURE\_EXCEPTION\_RETURN](#a5891f4f431f3817d4bb9f652ff45a9c4a78c476ea635a8c9459f1b644101f9350) , [K\_ERR\_ARM\_SECURE\_ATTRIBUTION\_UNIT](#a5891f4f431f3817d4bb9f652ff45a9c4abbe3ce01c99bd423507dca6b27c4077b) , [K\_ERR\_ARM\_SECURE\_TRANSITION](#a5891f4f431f3817d4bb9f652ff45a9c4accffbb9380478d8e1612d2481246390b) , [K\_ERR\_ARM\_SECURE\_LAZY\_STATE\_PRESERVATION](#a5891f4f431f3817d4bb9f652ff45a9c4a37e19e97425d822a062fa0502c774d8b) ,     [K\_ERR\_ARM\_SECURE\_LAZY\_STATE\_ERROR](#a5891f4f431f3817d4bb9f652ff45a9c4acf891bac81ed5e29b423507ac0a35139) , [K\_ERR\_ARM\_UNDEFINED\_INSTRUCTION](#a5891f4f431f3817d4bb9f652ff45a9c4a96392456666f9adb04ee89d78f208f6a) , [K\_ERR\_ARM\_ALIGNMENT\_FAULT](#a5891f4f431f3817d4bb9f652ff45a9c4a5be6201ceaa069b4497e5dad46e9f8c1) , [K\_ERR\_ARM\_BACKGROUND\_FAULT](#a5891f4f431f3817d4bb9f652ff45a9c4a08211aaa1c86b287354b336a8f6ef40f) ,     [K\_ERR\_ARM\_PERMISSION\_FAULT](#a5891f4f431f3817d4bb9f652ff45a9c4afbc0c25bea6fe87969248a41f58e6822) , [K\_ERR\_ARM\_SYNC\_EXTERNAL\_ABORT](#a5891f4f431f3817d4bb9f652ff45a9c4a36cf0f17b0c5c880acc9ba3da2b42665) , [K\_ERR\_ARM\_ASYNC\_EXTERNAL\_ABORT](#a5891f4f431f3817d4bb9f652ff45a9c4a54d95700befedeb1da3378d5abd8d833) , [K\_ERR\_ARM\_SYNC\_PARITY\_ERROR](#a5891f4f431f3817d4bb9f652ff45a9c4a4307218c98165be33c86e07c47fc0579) ,     [K\_ERR\_ARM\_ASYNC\_PARITY\_ERROR](#a5891f4f431f3817d4bb9f652ff45a9c4ab655e2d4d1cf6a441362e80e969287f8) , [K\_ERR\_ARM\_DEBUG\_EVENT](#a5891f4f431f3817d4bb9f652ff45a9c4abb352aab2d7667ed3c72eabe024d4c5c) , [K\_ERR\_ARM\_TRANSLATION\_FAULT](#a5891f4f431f3817d4bb9f652ff45a9c4a5c820b75e2d2941f160b1f47a6da6d76) , [K\_ERR\_ARM\_UNSUPPORTED\_EXCLUSIVE\_ACCESS\_FAULT](#a5891f4f431f3817d4bb9f652ff45a9c4a270c41c058d9fb3567a77419dae9cf3a)   } |

## Detailed Description

ARM AArch32 specific kernel interface header.

This header contains the ARM AArch32 specific kernel interface. It is included by the kernel interface architecture-abstraction header (include/arm/cpu.h)

## Macro Definition Documentation

## [◆ ](#af0f8ad93611d93cd0626914837e761d3)ARCH\_STACK\_PTR\_ALIGN

| #define ARCH\_STACK\_PTR\_ALIGN   4 |
| --- |

Declare the ARCH\_STACK\_PTR\_ALIGN.

Denotes the required alignment of the stack pointer on public API boundaries

## [◆ ](#ab6c1d96f5e018ed166ee401dc84b7ab7)ARCH\_THREAD\_STACK\_OBJ\_ALIGN

| #define ARCH\_THREAD\_STACK\_OBJ\_ALIGN | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(Z\_THREAD\_MIN\_STACK\_ALIGN, \

Z\_MPU\_GUARD\_ALIGN)

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)

#define MAX(a, b)

Obtain the maximum of two values.

**Definition** util.h:358

## [◆ ](#ace8831316d471ccfb06eeddb6d69d817)ARCH\_THREAD\_STACK\_RESERVED

| #define ARCH\_THREAD\_STACK\_RESERVED   0 |
| --- |

## [◆ ](#ab76d60bd06e5c5a0f995c6b11bf97fd8)ARCH\_THREAD\_STACK\_SIZE\_ADJUST

| #define ARCH\_THREAD\_STACK\_SIZE\_ADJUST | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(size, CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE)

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:288

## [◆ ](#a08b1afe29bff127c0f3c0376ee6744b1)MPU\_GUARD\_ALIGN\_AND\_SIZE

| #define MPU\_GUARD\_ALIGN\_AND\_SIZE   0 |
| --- |

Declare a minimum MPU guard alignment and size.

This specifies the minimum MPU guard alignment/size for the MPU. This will be used to denote the guard section of the stack, if it exists.

One key note is that this guard results in extra bytes being added to the stack. APIs which give the stack ptr and stack size will take this guard size into account.

Stack is allocated, but initial stack pointer is at the end (highest address). Stack grows down to the actual allocation address (lowest address). Stack guard, if present, will comprise the lowest MPU\_GUARD\_ALIGN\_AND\_SIZE bytes of the stack.

The guard region must include enough space for an exception frame below the trapping region as a stack fault will end up storing the exception data (0x20 bytes) onto the stack below wherever the stack pointer refers, even if that is within the guard region, so we make sure the region is strictly larger than this size by setting it to 0x40 (to respect any power-of-two requirements).

As the stack grows down, it will reach the end of the stack when it encounters either the stack guard region, or the stack allocation address.

--------------------— <-— Stack allocation address + stack size + | | MPU\_GUARD\_ALIGN\_AND\_SIZE | Some thread data | <-— Defined when thread is created | ... | |------------------—| <-— Actual initial stack ptr | Initial Stack Ptr | aligned to ARCH\_STACK\_PTR\_ALIGN | ... | | ... | | ... | | ... | | ... | | ... | | ... | | ... | | Stack Ends | |-------------------— <-— Stack Buffer Ptr from API | MPU Guard, | | if present | --------------------— <-— Stack Allocation address

## [◆ ](#a28b1b91e550d6b6fb08cf9aef9e9b0f2)MPU\_GUARD\_ALIGN\_AND\_SIZE\_FLOAT

| #define MPU\_GUARD\_ALIGN\_AND\_SIZE\_FLOAT   0 |
| --- |

Declare the MPU guard alignment and size for a thread stack that is using the Floating Point services.

For threads that are using the Floating Point services under Shared Registers (CONFIG\_FPU\_SHARING=y) mode, the exception stack frame may contain both the basic stack frame and the FP caller-saved context, upon exception entry. Therefore, a wide guard region is required to guarantee that stack-overflow detection will always be successful.

## [◆ ](#a59d42697fc33d0b600597145a7b76dc7)sys\_define\_gpr\_with\_alias

| #define sys\_define\_gpr\_with\_alias | ( |  | *name1*, |
| --- | --- | --- | --- |
|  |  |  | *name2* ) |

**Value:**

union { [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) name1, name2; }

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

## Enumeration Type Documentation

## [◆ ](#a5891f4f431f3817d4bb9f652ff45a9c4)k\_fatal\_error\_reason\_arch

| enum [k\_fatal\_error\_reason\_arch](#a5891f4f431f3817d4bb9f652ff45a9c4) |
| --- |

| Enumerator | |
| --- | --- |
| K\_ERR\_ARM\_MEM\_GENERIC |  |
| K\_ERR\_ARM\_MEM\_STACKING |  |
| K\_ERR\_ARM\_MEM\_UNSTACKING |  |
| K\_ERR\_ARM\_MEM\_DATA\_ACCESS |  |
| K\_ERR\_ARM\_MEM\_INSTRUCTION\_ACCESS |  |
| K\_ERR\_ARM\_MEM\_FP\_LAZY\_STATE\_PRESERVATION |  |
| K\_ERR\_ARM\_BUS\_GENERIC |  |
| K\_ERR\_ARM\_BUS\_STACKING |  |
| K\_ERR\_ARM\_BUS\_UNSTACKING |  |
| K\_ERR\_ARM\_BUS\_PRECISE\_DATA\_BUS |  |
| K\_ERR\_ARM\_BUS\_IMPRECISE\_DATA\_BUS |  |
| K\_ERR\_ARM\_BUS\_INSTRUCTION\_BUS |  |
| K\_ERR\_ARM\_BUS\_FP\_LAZY\_STATE\_PRESERVATION |  |
| K\_ERR\_ARM\_USAGE\_GENERIC |  |
| K\_ERR\_ARM\_USAGE\_DIV\_0 |  |
| K\_ERR\_ARM\_USAGE\_UNALIGNED\_ACCESS |  |
| K\_ERR\_ARM\_USAGE\_STACK\_OVERFLOW |  |
| K\_ERR\_ARM\_USAGE\_NO\_COPROCESSOR |  |
| K\_ERR\_ARM\_USAGE\_ILLEGAL\_EXC\_RETURN |  |
| K\_ERR\_ARM\_USAGE\_ILLEGAL\_EPSR |  |
| K\_ERR\_ARM\_USAGE\_UNDEFINED\_INSTRUCTION |  |
| K\_ERR\_ARM\_SECURE\_GENERIC |  |
| K\_ERR\_ARM\_SECURE\_ENTRY\_POINT |  |
| K\_ERR\_ARM\_SECURE\_INTEGRITY\_SIGNATURE |  |
| K\_ERR\_ARM\_SECURE\_EXCEPTION\_RETURN |  |
| K\_ERR\_ARM\_SECURE\_ATTRIBUTION\_UNIT |  |
| K\_ERR\_ARM\_SECURE\_TRANSITION |  |
| K\_ERR\_ARM\_SECURE\_LAZY\_STATE\_PRESERVATION |  |
| K\_ERR\_ARM\_SECURE\_LAZY\_STATE\_ERROR |  |
| K\_ERR\_ARM\_UNDEFINED\_INSTRUCTION |  |
| K\_ERR\_ARM\_ALIGNMENT\_FAULT |  |
| K\_ERR\_ARM\_BACKGROUND\_FAULT |  |
| K\_ERR\_ARM\_PERMISSION\_FAULT |  |
| K\_ERR\_ARM\_SYNC\_EXTERNAL\_ABORT |  |
| K\_ERR\_ARM\_ASYNC\_EXTERNAL\_ABORT |  |
| K\_ERR\_ARM\_SYNC\_PARITY\_ERROR |  |
| K\_ERR\_ARM\_ASYNC\_PARITY\_ERROR |  |
| K\_ERR\_ARM\_DEBUG\_EVENT |  |
| K\_ERR\_ARM\_TRANSLATION\_FAULT |  |
| K\_ERR\_ARM\_UNSUPPORTED\_EXCLUSIVE\_ACCESS\_FAULT |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [arch.h](arm_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
