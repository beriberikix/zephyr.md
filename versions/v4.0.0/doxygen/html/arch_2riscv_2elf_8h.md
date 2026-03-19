---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2riscv_2elf_8h.html
original_path: doxygen/html/arch_2riscv_2elf_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf.h File Reference

RISCV-Specific constants for ELF binaries.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](arch_2riscv_2elf_8h_source.md)

| Macros | |
| --- | --- |
| #define | [R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, bit) |
|  | Relocation names for RISCV-specific relocations. |
| #define | [R\_RISCV\_BTYPE\_IMM8\_MASK](#a1657a470d96458e5abdbfc08a31a92c7)(imm8) |
|  | Generate mask for immediate in B-type RISC-V instruction. |
| #define | [R\_RISCV\_JTYPE\_IMM8\_MASK](#a209ba3c784b15adc41b10b35299e43e1)(imm8) |
|  | Generate mask for immediate in J-type RISC-V instruction. |
| #define | [R\_RISCV\_STYPE\_IMM8\_MASK](#a449d28e8da3f67e6d95df42d5e578aa3)(imm8) |
|  | Generate mask for immediate in S-type RISC-V instruction. |
| #define | [R\_RISCV\_CJTYPE\_IMM8\_MASK](#a67eef921ccb1b3f70b69d263916ad05d)(imm8) |
|  | Generate mask for immediate in compressed J-type RISC-V instruction. |
| #define | [R\_RISCV\_CBTYPE\_IMM8\_MASK](#ad5c9a275a624f9ed623d6e88dd53bea3)(imm8) |
|  | Generate mask for immediate in compressed B-type RISC-V instruction. |
| #define | [R\_RISCV\_CLEAR\_BTYPE\_IMM8](#a4919535698f6a4b050504669116665b5)(operand) |
|  | Clear immediate bits in B-type instruction. |
| #define | [R\_RISCV\_SET\_BTYPE\_IMM8](#ab34a701190e589da67afae289afde4a7)(operand, imm8) |
|  | Overwrite immediate in B-type instruction. |
| #define | [R\_RISCV\_CLEAR\_JTYPE\_IMM8](#abcc19e420bb224cc8a6a159ee7b26cc2)(operand) |
|  | Clear immediate bits in J-type instruction. |
| #define | [R\_RISCV\_SET\_JTYPE\_IMM8](#a754fb9008bc4a39ad34409a757af3510)(operand, imm8) |
|  | Overwrite immediate in J-type instruction. |
| #define | [R\_RISCV\_CLEAR\_STYPE\_IMM8](#a4ed514a3b1d163d2fe3732c6b0a5a941)(operand) |
|  | Clear immediate bits in S-type instruction. |
| #define | [R\_RISCV\_SET\_STYPE\_IMM8](#af5471257051b3eff985a1a87cc2dbd5f)(operand, imm8) |
|  | Overwrite immediate in S-type instruction. |
| #define | [R\_RISCV\_CLEAR\_CJTYPE\_IMM8](#a965e0f3fcf5faad9ed08381596ac8168)(operand) |
|  | Clear immediate bits in compressed J-type instruction. |
| #define | [R\_RISCV\_SET\_CJTYPE\_IMM8](#a2989a3ea88a01998dd50ed5a9af40450)(operand, imm8) |
|  | Overwrite immediate in compressed J-type instruction. |
| #define | [R\_RISCV\_CLEAR\_CBTYPE\_IMM8](#ac79d3798e643d0fd2d703749a3618fe6)(operand) |
|  | Clear immediate bits in compressed B-type instruction. |
| #define | [R\_RISCV\_SET\_CBTYPE\_IMM8](#addf30bebbf4783ff29f2fe5b99e8d02c)(operand, imm8) |
|  | Overwrite immediate in compressed B-type instruction. |
| #define | [R\_RISCV\_CLEAR\_UTYPE\_IMM8](#a498b4a66bc5450871c5752847e813fc5)(operand) |
|  | Clear immediate bits in U-type instruction. |
| #define | [R\_RISCV\_SET\_UTYPE\_IMM8](#a00222ee6cf155a01e6c541dec88045c3)(operand, imm8) |
|  | Overwrite immediate in U-type instruction. |
| #define | [R\_RISCV\_CLEAR\_ITYPE\_IMM8](#a5fc196fd73b38a25fbbc31e2225097f4)(operand) |
|  | Clear immediate bits in I-type instruction. |
| #define | [R\_RISCV\_SET\_ITYPE\_IMM8](#a56821bda8f04f5c3596a83c77738b208)(operand, imm8) |
|  | Overwrite immediate in I-type instruction. |

## Detailed Description

RISCV-Specific constants for ELF binaries.

References can be found here: [https://github.com/riscv-non-isa/riscv-elf-psabi-doc/blob/master/riscv-elf.adoc](https://github.com/riscv-non-isa/riscv-elf-psabi-doc/blob/master/riscv-elf.adoc)

## Macro Definition Documentation

## [◆ ](#a1657a470d96458e5abdbfc08a31a92c7)R\_RISCV\_BTYPE\_IMM8\_MASK

| #define R\_RISCV\_BTYPE\_IMM8\_MASK | ( |  | *imm8* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 12) << 31) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 10) << 30) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 9) << 29) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 8) << 28) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 7) << 27) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 6) << 26) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 5) << 25) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 4) << 11) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 3) << 10) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 2) << 9) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 1) << 8) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 11) << 7))

[R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)

#define R\_RISCV\_IMM8\_GET\_BIT(imm8, bit)

Relocation names for RISCV-specific relocations.

**Definition** elf.h:110

Generate mask for immediate in B-type RISC-V instruction.

Parameters
:   | imm8 | immediate value, lower 12 bits used; due to alignment requirements, imm8[0] is implicitly 0 |
    | --- | --- |

## [◆ ](#ad5c9a275a624f9ed623d6e88dd53bea3)R\_RISCV\_CBTYPE\_IMM8\_MASK

| #define R\_RISCV\_CBTYPE\_IMM8\_MASK | ( |  | *imm8* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 8) << 12) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 4) << 11) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 3) << 10) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 7) << 6) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 6) << 5) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 2) << 4) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 1) << 3) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 5) << 2))

Generate mask for immediate in compressed B-type RISC-V instruction.

Parameters
:   | imm8 | immediate value, lower 9 bits used; due to alignment requirements, imm8[0] is implicitly 0 |
    | --- | --- |

## [◆ ](#a67eef921ccb1b3f70b69d263916ad05d)R\_RISCV\_CJTYPE\_IMM8\_MASK

| #define R\_RISCV\_CJTYPE\_IMM8\_MASK | ( |  | *imm8* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 11) << 12) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 4) << 11) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 9) << 10) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 8) << 9) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 10) << 8) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 6) << 7) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 7) << 6) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 3) << 5) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 2) << 4) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 1) << 3) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 5) << 2))

Generate mask for immediate in compressed J-type RISC-V instruction.

Parameters
:   | imm8 | immediate value, lower 12 bits used; due to alignment requirements, imm8[0] is implicitly 0 |
    | --- | --- |

## [◆ ](#a4919535698f6a4b050504669116665b5)R\_RISCV\_CLEAR\_BTYPE\_IMM8

| #define R\_RISCV\_CLEAR\_BTYPE\_IMM8 | ( |  | *operand* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((operand) & [~R\_RISCV\_BTYPE\_IMM8\_MASK](#a1657a470d96458e5abdbfc08a31a92c7)(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) -1))

[R\_RISCV\_BTYPE\_IMM8\_MASK](#a1657a470d96458e5abdbfc08a31a92c7)

#define R\_RISCV\_BTYPE\_IMM8\_MASK(imm8)

Generate mask for immediate in B-type RISC-V instruction.

**Definition** elf.h:118

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Clear immediate bits in B-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, B-type |
    | --- | --- |

## [◆ ](#ac79d3798e643d0fd2d703749a3618fe6)R\_RISCV\_CLEAR\_CBTYPE\_IMM8

| #define R\_RISCV\_CLEAR\_CBTYPE\_IMM8 | ( |  | *operand* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((operand) & [~R\_RISCV\_CBTYPE\_IMM8\_MASK](#ad5c9a275a624f9ed623d6e88dd53bea3)(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) -1))

[R\_RISCV\_CBTYPE\_IMM8\_MASK](#ad5c9a275a624f9ed623d6e88dd53bea3)

#define R\_RISCV\_CBTYPE\_IMM8\_MASK(imm8)

Generate mask for immediate in compressed B-type RISC-V instruction.

**Definition** elf.h:177

Clear immediate bits in compressed B-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, compressed-B-type |
    | --- | --- |

## [◆ ](#a965e0f3fcf5faad9ed08381596ac8168)R\_RISCV\_CLEAR\_CJTYPE\_IMM8

| #define R\_RISCV\_CLEAR\_CJTYPE\_IMM8 | ( |  | *operand* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((operand) & [~R\_RISCV\_CJTYPE\_IMM8\_MASK](#a67eef921ccb1b3f70b69d263916ad05d)(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) -1))

[R\_RISCV\_CJTYPE\_IMM8\_MASK](#a67eef921ccb1b3f70b69d263916ad05d)

#define R\_RISCV\_CJTYPE\_IMM8\_MASK(imm8)

Generate mask for immediate in compressed J-type RISC-V instruction.

**Definition** elf.h:163

Clear immediate bits in compressed J-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, compressed-J-type |
    | --- | --- |

## [◆ ](#a5fc196fd73b38a25fbbc31e2225097f4)R\_RISCV\_CLEAR\_ITYPE\_IMM8

| #define R\_RISCV\_CLEAR\_ITYPE\_IMM8 | ( |  | *operand* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((operand) & ~(0xFFF00000))

Clear immediate bits in I-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, I-type |
    | --- | --- |

## [◆ ](#abcc19e420bb224cc8a6a159ee7b26cc2)R\_RISCV\_CLEAR\_JTYPE\_IMM8

| #define R\_RISCV\_CLEAR\_JTYPE\_IMM8 | ( |  | *operand* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((operand) & [~R\_RISCV\_JTYPE\_IMM8\_MASK](#a209ba3c784b15adc41b10b35299e43e1)(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) -1))

[R\_RISCV\_JTYPE\_IMM8\_MASK](#a209ba3c784b15adc41b10b35299e43e1)

#define R\_RISCV\_JTYPE\_IMM8\_MASK(imm8)

Generate mask for immediate in J-type RISC-V instruction.

**Definition** elf.h:132

Clear immediate bits in J-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, J-type |
    | --- | --- |

## [◆ ](#a4ed514a3b1d163d2fe3732c6b0a5a941)R\_RISCV\_CLEAR\_STYPE\_IMM8

| #define R\_RISCV\_CLEAR\_STYPE\_IMM8 | ( |  | *operand* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((operand) & [~R\_RISCV\_STYPE\_IMM8\_MASK](#a449d28e8da3f67e6d95df42d5e578aa3)(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) -1))

[R\_RISCV\_STYPE\_IMM8\_MASK](#a449d28e8da3f67e6d95df42d5e578aa3)

#define R\_RISCV\_STYPE\_IMM8\_MASK(imm8)

Generate mask for immediate in S-type RISC-V instruction.

**Definition** elf.h:149

Clear immediate bits in S-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, S-type |
    | --- | --- |

## [◆ ](#a498b4a66bc5450871c5752847e813fc5)R\_RISCV\_CLEAR\_UTYPE\_IMM8

| #define R\_RISCV\_CLEAR\_UTYPE\_IMM8 | ( |  | *operand* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((operand) & ~(0xFFFFF000))

Clear immediate bits in U-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, U-type |
    | --- | --- |

## [◆ ](#a373699c920d9ff459a0ae2bedf4b71d6)R\_RISCV\_IMM8\_GET\_BIT

| #define R\_RISCV\_IMM8\_GET\_BIT | ( |  | *imm8*, |
| --- | --- | --- | --- |
|  |  |  | *bit* ) |

**Value:**

(((imm8) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(bit)) >> (bit))

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

Relocation names for RISCV-specific relocations.

"wordclass" from RISC-V specification

Extract bit from immediate

Parameters
:   | imm8 | immediate value (usually upper 20 or lower 12 bit) |
    | --- | --- |
    | bit | which bit to extract |

## [◆ ](#a209ba3c784b15adc41b10b35299e43e1)R\_RISCV\_JTYPE\_IMM8\_MASK

| #define R\_RISCV\_JTYPE\_IMM8\_MASK | ( |  | *imm8* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 20) << 31) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 10) << 30) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 9) << 29) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 8) << 28) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 7) << 27) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 6) << 26) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 5) << 25) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 4) << 24) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 3) << 23) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 2) << 22) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 1) << 21) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 11) << 20) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 19) << 19) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 18) << 18) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 17) << 17) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 16) << 16) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 15) << 15) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 14) << 14) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 13) << 13) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 12) << 12))

Generate mask for immediate in J-type RISC-V instruction.

Parameters
:   | imm8 | immediate value, lower 21 bits used; due to alignment requirements, imm8[0] is implicitly 0 |
    | --- | --- |

## [◆ ](#ab34a701190e589da67afae289afde4a7)R\_RISCV\_SET\_BTYPE\_IMM8

| #define R\_RISCV\_SET\_BTYPE\_IMM8 | ( |  | *operand*, |
| --- | --- | --- | --- |
|  |  |  | *imm8* ) |

**Value:**

(([R\_RISCV\_CLEAR\_BTYPE\_IMM8](#a4919535698f6a4b050504669116665b5)(operand)) | [R\_RISCV\_BTYPE\_IMM8\_MASK](#a1657a470d96458e5abdbfc08a31a92c7)(imm8))

[R\_RISCV\_CLEAR\_BTYPE\_IMM8](#a4919535698f6a4b050504669116665b5)

#define R\_RISCV\_CLEAR\_BTYPE\_IMM8(operand)

Clear immediate bits in B-type instruction.

**Definition** elf.h:188

Overwrite immediate in B-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, B-type |
    | --- | --- |
    | imm8 | New immediate |

## [◆ ](#addf30bebbf4783ff29f2fe5b99e8d02c)R\_RISCV\_SET\_CBTYPE\_IMM8

| #define R\_RISCV\_SET\_CBTYPE\_IMM8 | ( |  | *operand*, |
| --- | --- | --- | --- |
|  |  |  | *imm8* ) |

**Value:**

(([R\_RISCV\_CLEAR\_CBTYPE\_IMM8](#ac79d3798e643d0fd2d703749a3618fe6)(operand)) | [R\_RISCV\_CBTYPE\_IMM8\_MASK](#ad5c9a275a624f9ed623d6e88dd53bea3)(imm8))

[R\_RISCV\_CLEAR\_CBTYPE\_IMM8](#ac79d3798e643d0fd2d703749a3618fe6)

#define R\_RISCV\_CLEAR\_CBTYPE\_IMM8(operand)

Clear immediate bits in compressed B-type instruction.

**Definition** elf.h:252

Overwrite immediate in compressed B-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, compressed-B-type |
    | --- | --- |
    | imm8 | New immediate |

## [◆ ](#a2989a3ea88a01998dd50ed5a9af40450)R\_RISCV\_SET\_CJTYPE\_IMM8

| #define R\_RISCV\_SET\_CJTYPE\_IMM8 | ( |  | *operand*, |
| --- | --- | --- | --- |
|  |  |  | *imm8* ) |

**Value:**

(([R\_RISCV\_CLEAR\_CJTYPE\_IMM8](#a965e0f3fcf5faad9ed08381596ac8168)(operand)) | [R\_RISCV\_CJTYPE\_IMM8\_MASK](#a67eef921ccb1b3f70b69d263916ad05d)(imm8))

[R\_RISCV\_CLEAR\_CJTYPE\_IMM8](#a965e0f3fcf5faad9ed08381596ac8168)

#define R\_RISCV\_CLEAR\_CJTYPE\_IMM8(operand)

Clear immediate bits in compressed J-type instruction.

**Definition** elf.h:236

Overwrite immediate in compressed J-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, compressed-J-type |
    | --- | --- |
    | imm8 | New immediate |

## [◆ ](#a56821bda8f04f5c3596a83c77738b208)R\_RISCV\_SET\_ITYPE\_IMM8

| #define R\_RISCV\_SET\_ITYPE\_IMM8 | ( |  | *operand*, |
| --- | --- | --- | --- |
|  |  |  | *imm8* ) |

**Value:**

(([R\_RISCV\_CLEAR\_ITYPE\_IMM8](#a5fc196fd73b38a25fbbc31e2225097f4)(operand)) | ((imm8) << 20))

[R\_RISCV\_CLEAR\_ITYPE\_IMM8](#a5fc196fd73b38a25fbbc31e2225097f4)

#define R\_RISCV\_CLEAR\_ITYPE\_IMM8(operand)

Clear immediate bits in I-type instruction.

**Definition** elf.h:284

Overwrite immediate in I-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, I-type |
    | --- | --- |
    | imm8 | New immediate |

## [◆ ](#a754fb9008bc4a39ad34409a757af3510)R\_RISCV\_SET\_JTYPE\_IMM8

| #define R\_RISCV\_SET\_JTYPE\_IMM8 | ( |  | *operand*, |
| --- | --- | --- | --- |
|  |  |  | *imm8* ) |

**Value:**

(([R\_RISCV\_CLEAR\_JTYPE\_IMM8](#abcc19e420bb224cc8a6a159ee7b26cc2)(operand)) | [R\_RISCV\_JTYPE\_IMM8\_MASK](#a209ba3c784b15adc41b10b35299e43e1)(imm8))

[R\_RISCV\_CLEAR\_JTYPE\_IMM8](#abcc19e420bb224cc8a6a159ee7b26cc2)

#define R\_RISCV\_CLEAR\_JTYPE\_IMM8(operand)

Clear immediate bits in J-type instruction.

**Definition** elf.h:204

Overwrite immediate in J-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, J-type |
    | --- | --- |
    | imm8 | New immediate |

## [◆ ](#af5471257051b3eff985a1a87cc2dbd5f)R\_RISCV\_SET\_STYPE\_IMM8

| #define R\_RISCV\_SET\_STYPE\_IMM8 | ( |  | *operand*, |
| --- | --- | --- | --- |
|  |  |  | *imm8* ) |

**Value:**

(([R\_RISCV\_CLEAR\_STYPE\_IMM8](#a4ed514a3b1d163d2fe3732c6b0a5a941)(operand)) | [R\_RISCV\_STYPE\_IMM8\_MASK](#a449d28e8da3f67e6d95df42d5e578aa3)(imm8))

[R\_RISCV\_CLEAR\_STYPE\_IMM8](#a4ed514a3b1d163d2fe3732c6b0a5a941)

#define R\_RISCV\_CLEAR\_STYPE\_IMM8(operand)

Clear immediate bits in S-type instruction.

**Definition** elf.h:220

Overwrite immediate in S-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, S-type |
    | --- | --- |
    | imm8 | New immediate |

## [◆ ](#a00222ee6cf155a01e6c541dec88045c3)R\_RISCV\_SET\_UTYPE\_IMM8

| #define R\_RISCV\_SET\_UTYPE\_IMM8 | ( |  | *operand*, |
| --- | --- | --- | --- |
|  |  |  | *imm8* ) |

**Value:**

(([R\_RISCV\_CLEAR\_UTYPE\_IMM8](#a498b4a66bc5450871c5752847e813fc5)(operand)) | ((imm8) & 0xFFFFF000))

[R\_RISCV\_CLEAR\_UTYPE\_IMM8](#a498b4a66bc5450871c5752847e813fc5)

#define R\_RISCV\_CLEAR\_UTYPE\_IMM8(operand)

Clear immediate bits in U-type instruction.

**Definition** elf.h:268

Overwrite immediate in U-type instruction.

Parameters
:   | operand | Address of RISC-V instruction, U-type |
    | --- | --- |
    | imm8 | New immediate |

## [◆ ](#a449d28e8da3f67e6d95df42d5e578aa3)R\_RISCV\_STYPE\_IMM8\_MASK

| #define R\_RISCV\_STYPE\_IMM8\_MASK | ( |  | *imm8* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 11) << 31) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 10) << 30) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 9) << 29) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 8) << 28) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 7) << 27) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 6) << 26) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 5) << 25) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 4) << 11) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 3) << 10) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 2) << 9) | \

([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 1) << 8) | ([R\_RISCV\_IMM8\_GET\_BIT](#a373699c920d9ff459a0ae2bedf4b71d6)(imm8, 0) << 7))

Generate mask for immediate in S-type RISC-V instruction.

Parameters
:   | imm8 | immediate value, lower 12 bits used |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [elf.h](arch_2riscv_2elf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
