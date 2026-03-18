---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/nios2_2arch_8h.html
original_path: doxygen/html/nios2_2arch_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h File Reference

Nios II specific kernel interface header This header contains the Nios II specific kernel interface.
[More...](#details)

`#include <system.h>`  
`#include <[zephyr/arch/nios2/thread.h](arch_2nios2_2thread_8h_source.md)>`  
`#include <[zephyr/arch/nios2/asm_inline.h](nios2_2asm__inline_8h_source.md)>`  
`#include <[zephyr/arch/common/addr_types.h](addr__types_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/arch/nios2/nios2.h](nios2_8h_source.md)>`  
`#include <[zephyr/arch/common/sys_bitops.h](sys__bitops_8h_source.md)>`  
`#include <[zephyr/sys/sys_io.h](sys_2sys__io_8h_source.md)>`  
`#include <[zephyr/arch/common/ffs.h](ffs_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/irq.h](irq_8h_source.md)>`  
`#include <[zephyr/sw_isr_table.h](sw__isr__table_8h_source.md)>`

[Go to the source code of this file.](nios2_2arch_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARCH\_STACK\_PTR\_ALIGN](#af0f8ad93611d93cd0626914837e761d3)   4 |
| #define | [ARCH\_IRQ\_CONNECT](#accdf8a59e00ac1c1fcedc18b78be4b8a)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
| #define | [NIOS2\_BADADDR\_CAUSE\_MASK](#a70ed7e577dcd2644cbd4c4e964736c05) |

| Enumerations | |
| --- | --- |
| enum | [nios2\_exception\_cause](#a74caf934553c660658877ace2e17d5eb) {     [NIOS2\_EXCEPTION\_UNKNOWN](#a74caf934553c660658877ace2e17d5eba25e598ae2f7e517970f8f797e4f1b30a) = -1 , [NIOS2\_EXCEPTION\_RESET](#a74caf934553c660658877ace2e17d5ebaf6c6a73adf1aa0df7a4d5bf9892423ee) = 0 , [NIOS2\_EXCEPTION\_CPU\_ONLY\_RESET\_REQUEST](#a74caf934553c660658877ace2e17d5eba7fc081560604efa925848ed4204b589c) = 1 , [NIOS2\_EXCEPTION\_INTERRUPT](#a74caf934553c660658877ace2e17d5ebaf4d926e02d36e21e78902fc404bbf4f5) = 2 ,     [NIOS2\_EXCEPTION\_TRAP\_INST](#a74caf934553c660658877ace2e17d5ebaebf7c6f50a51346242135178592fec50) = 3 , [NIOS2\_EXCEPTION\_UNIMPLEMENTED\_INST](#a74caf934553c660658877ace2e17d5ebabfc872ef21b65fe5a2dd77833f5daf59) = 4 , [NIOS2\_EXCEPTION\_ILLEGAL\_INST](#a74caf934553c660658877ace2e17d5eba894eb715964b668ec2d4ed0e32dadb70) = 5 , [NIOS2\_EXCEPTION\_MISALIGNED\_DATA\_ADDR](#a74caf934553c660658877ace2e17d5ebae388771d5651cbda528c168fbc2b045f) = 6 ,     [NIOS2\_EXCEPTION\_MISALIGNED\_TARGET\_PC](#a74caf934553c660658877ace2e17d5ebad4daa79baaf28b7e57a41ab10c1a056b) = 7 , [NIOS2\_EXCEPTION\_DIVISION\_ERROR](#a74caf934553c660658877ace2e17d5ebad831a5dd045c258c7586f33b4af5ca85) = 8 , [NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_INST\_ADDR](#a74caf934553c660658877ace2e17d5eba9a08eea9bdf84fb5bce9b39126c7f407) = 9 , [NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_INST](#a74caf934553c660658877ace2e17d5ebae6258162d85c0c3b0a780b1e905a2d56) = 10 ,     [NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_DATA\_ADDR](#a74caf934553c660658877ace2e17d5eba732e002953cc38c05f87a6aa61a662bf) = 11 , [NIOS2\_EXCEPTION\_TLB\_MISS](#a74caf934553c660658877ace2e17d5eba810fce3ab2f5ceb92b6e73e707f1d22e) = 12 , [NIOS2\_EXCEPTION\_TLB\_EXECUTE\_PERM\_VIOLATION](#a74caf934553c660658877ace2e17d5ebae8101069360e03367af48e97e2d689a7) = 13 , [NIOS2\_EXCEPTION\_TLB\_READ\_PERM\_VIOLATION](#a74caf934553c660658877ace2e17d5ebad6cf84739e1469a0e8a4ba614d19a18a) = 14 ,     [NIOS2\_EXCEPTION\_TLB\_WRITE\_PERM\_VIOLATION](#a74caf934553c660658877ace2e17d5eba32fd876bb736d600090d68f9d5c30055) = 15 , [NIOS2\_EXCEPTION\_MPU\_INST\_REGION\_VIOLATION](#a74caf934553c660658877ace2e17d5eba6403b7c0a411db595de90af57b3ac25a) = 16 , [NIOS2\_EXCEPTION\_MPU\_DATA\_REGION\_VIOLATION](#a74caf934553c660658877ace2e17d5ebacb7c66d2e8e211b82d74da89d6a1855a) = 17 , [NIOS2\_EXCEPTION\_ECC\_TLB\_ERR](#a74caf934553c660658877ace2e17d5eba4cad710f904b74d686b286828a12c006) = 18 ,     [NIOS2\_EXCEPTION\_ECC\_FETCH\_ERR](#a74caf934553c660658877ace2e17d5ebad2c112e52af6240e77e3cb532d7890a1) = 19 , [NIOS2\_EXCEPTION\_ECC\_REGISTER\_FILE\_ERR](#a74caf934553c660658877ace2e17d5ebaec6269ebaf6592bc20f2acfee2420a33) = 20 , [NIOS2\_EXCEPTION\_ECC\_DATA\_ERR](#a74caf934553c660658877ace2e17d5ebaf5b4a2d54e230de79b36a4ca5d262ca0) = 21 , [NIOS2\_EXCEPTION\_ECC\_DATA\_CACHE\_WRITEBACK\_ERR](#a74caf934553c660658877ace2e17d5eba157e694bc9bbae8aa20ef35e94f621b8) = 22   } |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_irq\_lock](#a1496f4f860a99f42e1aee15ce5c9b3e2) (void) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_irq\_unlock](#a203e02b994beba0d006dad9f6d797c27) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_irq\_unlocked](#adb441b26ed6818fea4ebba6b8853354b) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| void | [arch\_irq\_enable](#aa278d630653b33cb339621d725ed295a) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| void | [arch\_irq\_disable](#a216d692e87bfba955a60f8e570e127df) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_clock\_cycle\_get\_32](#a42dcd1878309a82246dbfa26510f868a) (void) |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_k\_cycle\_get\_32](#a9ee9f897ec750957de45bf8d43349d5e) (void) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_clock\_cycle\_get\_64](#a25328a181bd0229ef5110c15e8452fc1) (void) |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_k\_cycle\_get\_64](#acc1ed8d949f694a1d39e389334caf971) (void) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_nop](#a0af98dc5138e02248173c30b8f07210f) (void) |

## Detailed Description

Nios II specific kernel interface header This header contains the Nios II specific kernel interface.

It is included by the generic kernel interface header (include/arch/cpu.h)

## Macro Definition Documentation

## [◆ ](#accdf8a59e00ac1c1fcedc18b78be4b8a)ARCH\_IRQ\_CONNECT

| #define ARCH\_IRQ\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *isr\_param\_p*, |
|  |  |  | *flags\_p* ) |

**Value:**

{ \

Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

}

## [◆ ](#af0f8ad93611d93cd0626914837e761d3)ARCH\_STACK\_PTR\_ALIGN

| #define ARCH\_STACK\_PTR\_ALIGN   4 |
| --- |

## [◆ ](#a70ed7e577dcd2644cbd4c4e964736c05)NIOS2\_BADADDR\_CAUSE\_MASK

| #define NIOS2\_BADADDR\_CAUSE\_MASK |
| --- |

**Value:**

([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_DATA\_ADDR](#a74caf934553c660658877ace2e17d5eba732e002953cc38c05f87a6aa61a662bf)) | \

BIT([NIOS2\_EXCEPTION\_MISALIGNED\_DATA\_ADDR](#a74caf934553c660658877ace2e17d5ebae388771d5651cbda528c168fbc2b045f)) | \

BIT([NIOS2\_EXCEPTION\_MISALIGNED\_TARGET\_PC](#a74caf934553c660658877ace2e17d5ebad4daa79baaf28b7e57a41ab10c1a056b)) | \

BIT([NIOS2\_EXCEPTION\_TLB\_READ\_PERM\_VIOLATION](#a74caf934553c660658877ace2e17d5ebad6cf84739e1469a0e8a4ba614d19a18a)) | \

BIT([NIOS2\_EXCEPTION\_TLB\_WRITE\_PERM\_VIOLATION](#a74caf934553c660658877ace2e17d5eba32fd876bb736d600090d68f9d5c30055)) | \

BIT([NIOS2\_EXCEPTION\_MPU\_DATA\_REGION\_VIOLATION](#a74caf934553c660658877ace2e17d5ebacb7c66d2e8e211b82d74da89d6a1855a)) | \

BIT([NIOS2\_EXCEPTION\_ECC\_DATA\_ERR](#a74caf934553c660658877ace2e17d5ebaf5b4a2d54e230de79b36a4ca5d262ca0)))

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[NIOS2\_EXCEPTION\_TLB\_WRITE\_PERM\_VIOLATION](#a74caf934553c660658877ace2e17d5eba32fd876bb736d600090d68f9d5c30055)

@ NIOS2\_EXCEPTION\_TLB\_WRITE\_PERM\_VIOLATION

**Definition** arch.h:148

[NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_DATA\_ADDR](#a74caf934553c660658877ace2e17d5eba732e002953cc38c05f87a6aa61a662bf)

@ NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_DATA\_ADDR

**Definition** arch.h:144

[NIOS2\_EXCEPTION\_MPU\_DATA\_REGION\_VIOLATION](#a74caf934553c660658877ace2e17d5ebacb7c66d2e8e211b82d74da89d6a1855a)

@ NIOS2\_EXCEPTION\_MPU\_DATA\_REGION\_VIOLATION

**Definition** arch.h:150

[NIOS2\_EXCEPTION\_MISALIGNED\_TARGET\_PC](#a74caf934553c660658877ace2e17d5ebad4daa79baaf28b7e57a41ab10c1a056b)

@ NIOS2\_EXCEPTION\_MISALIGNED\_TARGET\_PC

**Definition** arch.h:140

[NIOS2\_EXCEPTION\_TLB\_READ\_PERM\_VIOLATION](#a74caf934553c660658877ace2e17d5ebad6cf84739e1469a0e8a4ba614d19a18a)

@ NIOS2\_EXCEPTION\_TLB\_READ\_PERM\_VIOLATION

**Definition** arch.h:147

[NIOS2\_EXCEPTION\_MISALIGNED\_DATA\_ADDR](#a74caf934553c660658877ace2e17d5ebae388771d5651cbda528c168fbc2b045f)

@ NIOS2\_EXCEPTION\_MISALIGNED\_DATA\_ADDR

**Definition** arch.h:139

[NIOS2\_EXCEPTION\_ECC\_DATA\_ERR](#a74caf934553c660658877ace2e17d5ebaf5b4a2d54e230de79b36a4ca5d262ca0)

@ NIOS2\_EXCEPTION\_ECC\_DATA\_ERR

**Definition** arch.h:154

## Enumeration Type Documentation

## [◆ ](#a74caf934553c660658877ace2e17d5eb)nios2\_exception\_cause

| enum [nios2\_exception\_cause](#a74caf934553c660658877ace2e17d5eb) |
| --- |

| Enumerator | |
| --- | --- |
| NIOS2\_EXCEPTION\_UNKNOWN |  |
| NIOS2\_EXCEPTION\_RESET |  |
| NIOS2\_EXCEPTION\_CPU\_ONLY\_RESET\_REQUEST |  |
| NIOS2\_EXCEPTION\_INTERRUPT |  |
| NIOS2\_EXCEPTION\_TRAP\_INST |  |
| NIOS2\_EXCEPTION\_UNIMPLEMENTED\_INST |  |
| NIOS2\_EXCEPTION\_ILLEGAL\_INST |  |
| NIOS2\_EXCEPTION\_MISALIGNED\_DATA\_ADDR |  |
| NIOS2\_EXCEPTION\_MISALIGNED\_TARGET\_PC |  |
| NIOS2\_EXCEPTION\_DIVISION\_ERROR |  |
| NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_INST\_ADDR |  |
| NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_INST |  |
| NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_DATA\_ADDR |  |
| NIOS2\_EXCEPTION\_TLB\_MISS |  |
| NIOS2\_EXCEPTION\_TLB\_EXECUTE\_PERM\_VIOLATION |  |
| NIOS2\_EXCEPTION\_TLB\_READ\_PERM\_VIOLATION |  |
| NIOS2\_EXCEPTION\_TLB\_WRITE\_PERM\_VIOLATION |  |
| NIOS2\_EXCEPTION\_MPU\_INST\_REGION\_VIOLATION |  |
| NIOS2\_EXCEPTION\_MPU\_DATA\_REGION\_VIOLATION |  |
| NIOS2\_EXCEPTION\_ECC\_TLB\_ERR |  |
| NIOS2\_EXCEPTION\_ECC\_FETCH\_ERR |  |
| NIOS2\_EXCEPTION\_ECC\_REGISTER\_FILE\_ERR |  |
| NIOS2\_EXCEPTION\_ECC\_DATA\_ERR |  |
| NIOS2\_EXCEPTION\_ECC\_DATA\_CACHE\_WRITEBACK\_ERR |  |

## Function Documentation

## [◆ ](#a216d692e87bfba955a60f8e570e127df)arch\_irq\_disable()

| void arch\_irq\_disable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aa278d630653b33cb339621d725ed295a)arch\_irq\_enable()

| void arch\_irq\_enable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a1496f4f860a99f42e1aee15ce5c9b3e2)arch\_irq\_lock()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_irq\_lock | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a203e02b994beba0d006dad9f6d797c27)arch\_irq\_unlock()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_irq\_unlock | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#adb441b26ed6818fea4ebba6b8853354b)arch\_irq\_unlocked()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_irq\_unlocked | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9ee9f897ec750957de45bf8d43349d5e)arch\_k\_cycle\_get\_32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_k\_cycle\_get\_32 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#acc1ed8d949f694a1d39e389334caf971)arch\_k\_cycle\_get\_64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_k\_cycle\_get\_64 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0af98dc5138e02248173c30b8f07210f)arch\_nop()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_nop | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a42dcd1878309a82246dbfa26510f868a)sys\_clock\_cycle\_get\_32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_clock\_cycle\_get\_32 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a25328a181bd0229ef5110c15e8452fc1)sys\_clock\_cycle\_get\_64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_clock\_cycle\_get\_64 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [nios2](dir_bcfa142ae77c1ee311b7ef8e30037d11.md)
- [arch.h](nios2_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
