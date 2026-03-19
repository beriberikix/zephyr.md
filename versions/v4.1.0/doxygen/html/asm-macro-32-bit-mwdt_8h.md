---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/asm-macro-32-bit-mwdt_8h.html
original_path: doxygen/html/asm-macro-32-bit-mwdt_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm-macro-32-bit-mwdt.h File Reference

[Go to the source code of this file.](asm-macro-32-bit-mwdt_8h_source.md)

| Variables | |
| --- | --- |
| macro | [MOVR](#a62c92c2e7e269b0afb80256c5207da7b) |
| macro | [d](#aabf7c54edb88081579e2b6fc941f10e9) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro | [LDR](#a1a46311eefaef8a6a42bae236b114d6b) |
| macro s mov &$suffix s endm macro | [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if | [$narg](#ac743b07138dff5c6fe59b445965c1fc7) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro | [STR](#a2559ca808b98187e087954aafba01ad1) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro | [PUSHR](#aaecb2f53890260a5b5518501ac4ae55b) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro | [POPR](#a0f674b4d35f1df924883bff738f5c288) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro | [LRR](#af065467bfff1489bf1d38337a5d60988) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro | [SRR](#a4ab637a402c195c93f2e5f1d0fcccf78) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro | [ADDR](#a74d94870ad16a58f150bf43374bcc908) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro | [ADD2R](#a4213081f87edc43524180616979bd1b8) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro | [ADD3R](#a9cb390b45f968e4859be09505e376ff6) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro | [SUBR](#a1548d46b55a34b4830367a41995f6f48) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro | [BMSKNR](#aa4129c1e4b6617f30740aada9bdd872d) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro | [LSRR](#a8667c7c46bc57aff0cac0ca728023ed5) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro | [ASLR](#aaff8d26b5c5198b247467cb55a7df38b) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro | [ANDR](#abf83bab508dfaea0c41d8093d7b1c551) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro | [ORR](#ac61c6a6fd2801a19a8746a437a7b2a4a) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro | [BRR](#a3b737f39fe46787abeecc3661fad4946) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro lbl br &$suffix lbl endm macro | [BREQR](#abe3bac34bb316244a20ddc88ebc75937) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro lbl br &$suffix lbl endm macro lbl breq lbl endm macro | [CMPR](#a2914e6612b9957eba801ab818e2cbded) |
| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro lbl br &$suffix lbl endm macro lbl breq lbl endm macro | [op1](#a511259cb12c7f1112602eda6a77fab92) |

## Variable Documentation

## [◆ ](#ac743b07138dff5c6fe59b445965c1fc7)$narg

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) movl &$suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if $narg |
| --- |

**Initial value:**

== 2

ld\&$suffix [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

## [◆ ](#a4213081f87edc43524180616979bd1b8)ADD2R

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro ADD2R |
| --- |

## [◆ ](#a9cb390b45f968e4859be09505e376ff6)ADD3R

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro ADD3R |
| --- |

## [◆ ](#a74d94870ad16a58f150bf43374bcc908)ADDR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro ADDR |
| --- |

## [◆ ](#abf83bab508dfaea0c41d8093d7b1c551)ANDR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro ANDR |
| --- |

## [◆ ](#aaff8d26b5c5198b247467cb55a7df38b)ASLR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro ASLR |
| --- |

## [◆ ](#aa4129c1e4b6617f30740aada9bdd872d)BMSKNR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro v add3 v endm macro v sub v endm macro BMSKNR |
| --- |

## [◆ ](#abe3bac34bb316244a20ddc88ebc75937)BREQR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro lbl br& $suffix lbl endm macro BREQR |
| --- |

## [◆ ](#a3b737f39fe46787abeecc3661fad4946)BRR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro BRR |
| --- |

## [◆ ](#a2914e6612b9957eba801ab818e2cbded)CMPR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro lbl br& $suffix lbl endm macro lbl breq lbl endm macro CMPR |
| --- |

## [◆ ](#aabf7c54edb88081579e2b6fc941f10e9)d

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro lbl br& $suffix lbl endm macro lbl breq d |
| --- |

## [◆ ](#a1a46311eefaef8a6a42bae236b114d6b)LDR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro LDR |
| --- |

## [◆ ](#af065467bfff1489bf1d38337a5d60988)LRR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro LRR |
| --- |

## [◆ ](#a8667c7c46bc57aff0cac0ca728023ed5)LSRR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro LSRR |
| --- |

## [◆ ](#a62c92c2e7e269b0afb80256c5207da7b)MOVR

| macro MOVR |
| --- |

## [◆ ](#a511259cb12c7f1112602eda6a77fab92)op1

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro lbl br& $suffix lbl endm macro lbl breq lbl endm macro op2 cmp op1 |
| --- |

## [◆ ](#ac61c6a6fd2801a19a8746a437a7b2a4a)ORR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro ORR |
| --- |

## [◆ ](#a0f674b4d35f1df924883bff738f5c288)POPR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro POPR |
| --- |

## [◆ ](#aaecb2f53890260a5b5518501ac4ae55b)PUSHR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro PUSHR |
| --- |

## [◆ ](#a54157b9c4080ed8fdbe7272d4ffe2b34)s

| macro s mov& $suffix s endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro lbl br& $suffix lbl endm macro lbl breq s |
| --- |

## [◆ ](#a4ab637a402c195c93f2e5f1d0fcccf78)SRR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro SRR |
| --- |

## [◆ ](#a2559ca808b98187e087954aafba01ad1)STR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro STR |
| --- |

## [◆ ](#a1548d46b55a34b4830367a41995f6f48)SUBR

| macro [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) mov& $suffix [s](#a54157b9c4080ed8fdbe7272d4ffe2b34) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ld& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else st& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lr aux endm macro aux sr aux endm macro v add& $suffix v endm macro v add2& $suffix v endm macro v add3 v endm macro SUBR |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [asm-compat](dir_728f9cb61d4414cdda9196b7386075ee.md)
- [asm-macro-32-bit-mwdt.h](asm-macro-32-bit-mwdt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
