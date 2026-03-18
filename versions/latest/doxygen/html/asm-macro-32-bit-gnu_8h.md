---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/asm-macro-32-bit-gnu_8h.html
original_path: doxygen/html/asm-macro-32-bit-gnu_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm-macro-32-bit-gnu.h File Reference

[Go to the source code of this file.](asm-macro-32-bit-gnu_8h_source.md)

| Variables | |
| --- | --- |
| irp | [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) |
| irp | [hi](#a0ef89636f8d03ae88717291e66d59527) |
| irp nz macro [MOVR](asm-macro-32-bit-mwdt_8h.md#a62c92c2e7e269b0afb80256c5207da7b) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) | [d](#abaebda2ebe87111969af89be8895e417) |
| irp nz macro [MOVR](asm-macro-32-bit-mwdt_8h.md#a62c92c2e7e269b0afb80256c5207da7b) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) mov [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) endm endr irp | [aa](#a8be979fed261ea1fe93f3bf629f3aa9b) |
| irp nz macro [MOVR](asm-macro-32-bit-mwdt_8h.md#a62c92c2e7e269b0afb80256c5207da7b) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) mov [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) endm endr irp | [ab](#a65db1da5eb749b340685303a403ae14d) |
| irp nz macro [MOVR](asm-macro-32-bit-mwdt_8h.md#a62c92c2e7e269b0afb80256c5207da7b) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) mov [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) endm endr irp | [as](#ac93d5f4341d561a6bd9864e880cffcf4) |
| irp nz macro [MOVR](asm-macro-32-bit-mwdt_8h.md#a62c92c2e7e269b0afb80256c5207da7b) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) s mov [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) s endm endr irp aw macro [LDR](asm-macro-32-bit-mwdt_8h.md#a1a46311eefaef8a6a42bae236b114d6b) [aa](#a8be979fed261ea1fe93f3bf629f3aa9b) | [s](#a53a876d393ad3ed42cfeb2173695978d) |
| irp nz macro [MOVR](asm-macro-32-bit-mwdt_8h.md#a62c92c2e7e269b0afb80256c5207da7b) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) mov [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) endm endr irp aw macro [LDR](asm-macro-32-bit-mwdt_8h.md#a1a46311eefaef8a6a42bae236b114d6b) [aa](#a8be979fed261ea1fe93f3bf629f3aa9b) | [off](#adbc19a384ffe3a93866980a920b08394) |
| workaround assembler barfing for ST | [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) |
| workaround assembler barfing for ST if else st [aa](#a8be979fed261ea1fe93f3bf629f3aa9b) endif endm endr macro [PUSHR](asm-macro-32-bit-mwdt_8h.md#aaecb2f53890260a5b5518501ac4ae55b) [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [POPR](asm-macro-32-bit-mwdt_8h.md#a0f674b4d35f1df924883bff738f5c288) [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [LRR](asm-macro-32-bit-mwdt_8h.md#af065467bfff1489bf1d38337a5d60988) aux lr aux endm macro [SRR](asm-macro-32-bit-mwdt_8h.md#a4ab637a402c195c93f2e5f1d0fcccf78) aux sr aux endm irp nz macro [ADDR](asm-macro-32-bit-mwdt_8h.md#a74d94870ad16a58f150bf43374bcc908) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v add [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v endm endr irp nz macro [ADD2R](asm-macro-32-bit-mwdt_8h.md#a4213081f87edc43524180616979bd1b8) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v add2 [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v endm endr macro [ADD3R](asm-macro-32-bit-mwdt_8h.md#a9cb390b45f968e4859be09505e376ff6) v add3 v endm macro [SUBR](asm-macro-32-bit-mwdt_8h.md#a1548d46b55a34b4830367a41995f6f48) v sub v endm macro [BMSKNR](asm-macro-32-bit-mwdt_8h.md#aa4129c1e4b6617f30740aada9bdd872d) v bmskn v endm macro [LSRR](asm-macro-32-bit-mwdt_8h.md#a8667c7c46bc57aff0cac0ca728023ed5) v lsr v endm macro [ASLR](asm-macro-32-bit-mwdt_8h.md#aaff8d26b5c5198b247467cb55a7df38b) v asl v endm macro [ANDR](asm-macro-32-bit-mwdt_8h.md#abf83bab508dfaea0c41d8093d7b1c551) v and v endm macro | [ORR](#ad0672a138db1d400f19f2bf7f08c0088) |
| workaround assembler barfing for ST if else st [aa](#a8be979fed261ea1fe93f3bf629f3aa9b) endif endm endr macro [PUSHR](asm-macro-32-bit-mwdt_8h.md#aaecb2f53890260a5b5518501ac4ae55b) [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [POPR](asm-macro-32-bit-mwdt_8h.md#a0f674b4d35f1df924883bff738f5c288) [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [LRR](asm-macro-32-bit-mwdt_8h.md#af065467bfff1489bf1d38337a5d60988) aux lr aux endm macro [SRR](asm-macro-32-bit-mwdt_8h.md#a4ab637a402c195c93f2e5f1d0fcccf78) aux sr aux endm irp nz macro [ADDR](asm-macro-32-bit-mwdt_8h.md#a74d94870ad16a58f150bf43374bcc908) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v add [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v endm endr irp nz macro [ADD2R](asm-macro-32-bit-mwdt_8h.md#a4213081f87edc43524180616979bd1b8) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v add2 [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v endm endr macro [ADD3R](asm-macro-32-bit-mwdt_8h.md#a9cb390b45f968e4859be09505e376ff6) v add3 v endm macro [SUBR](asm-macro-32-bit-mwdt_8h.md#a1548d46b55a34b4830367a41995f6f48) v sub v endm macro [BMSKNR](asm-macro-32-bit-mwdt_8h.md#aa4129c1e4b6617f30740aada9bdd872d) v bmskn v endm macro [LSRR](asm-macro-32-bit-mwdt_8h.md#a8667c7c46bc57aff0cac0ca728023ed5) v lsr v endm macro [ASLR](asm-macro-32-bit-mwdt_8h.md#aaff8d26b5c5198b247467cb55a7df38b) v asl v endm macro [ANDR](asm-macro-32-bit-mwdt_8h.md#abf83bab508dfaea0c41d8093d7b1c551) v and v endm macro v or v endm irp | [ne](#a8de167d4ebfa82a6635ea26eee8c907c) |
| workaround assembler barfing for ST if else st [aa](#a8be979fed261ea1fe93f3bf629f3aa9b) endif endm endr macro [PUSHR](asm-macro-32-bit-mwdt_8h.md#aaecb2f53890260a5b5518501ac4ae55b) [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [POPR](asm-macro-32-bit-mwdt_8h.md#a0f674b4d35f1df924883bff738f5c288) [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [LRR](asm-macro-32-bit-mwdt_8h.md#af065467bfff1489bf1d38337a5d60988) aux lr aux endm macro [SRR](asm-macro-32-bit-mwdt_8h.md#a4ab637a402c195c93f2e5f1d0fcccf78) aux sr aux endm irp nz macro [ADDR](asm-macro-32-bit-mwdt_8h.md#a74d94870ad16a58f150bf43374bcc908) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v add [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v endm endr irp nz macro [ADD2R](asm-macro-32-bit-mwdt_8h.md#a4213081f87edc43524180616979bd1b8) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v add2 [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v endm endr macro [ADD3R](asm-macro-32-bit-mwdt_8h.md#a9cb390b45f968e4859be09505e376ff6) v add3 v endm macro [SUBR](asm-macro-32-bit-mwdt_8h.md#a1548d46b55a34b4830367a41995f6f48) v sub v endm macro [BMSKNR](asm-macro-32-bit-mwdt_8h.md#aa4129c1e4b6617f30740aada9bdd872d) v bmskn v endm macro [LSRR](asm-macro-32-bit-mwdt_8h.md#a8667c7c46bc57aff0cac0ca728023ed5) v lsr v endm macro [ASLR](asm-macro-32-bit-mwdt_8h.md#aaff8d26b5c5198b247467cb55a7df38b) v asl v endm macro [ANDR](asm-macro-32-bit-mwdt_8h.md#abf83bab508dfaea0c41d8093d7b1c551) v and v endm macro v or v endm irp eq macro [BRR](asm-macro-32-bit-mwdt_8h.md#a3b737f39fe46787abeecc3661fad4946) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) lbl br [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) lbl endm endr macro [BREQR](asm-macro-32-bit-mwdt_8h.md#abe3bac34bb316244a20ddc88ebc75937) lbl breq lbl endm macro [CMPR](asm-macro-32-bit-mwdt_8h.md#a2914e6612b9957eba801ab818e2cbded) | [op1](#a1b3df9ba4c3032118bbf49c7c7e28edd) |

## Variable Documentation

## [◆ ](#a8be979fed261ea1fe93f3bf629f3aa9b)aa

| irp nz macro [MOVR](asm-macro-32-bit-mwdt_8h.md#a62c92c2e7e269b0afb80256c5207da7b) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) movl [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) endm endr irp aw macro [LDR](asm-macro-32-bit-mwdt_8h.md#a1a46311eefaef8a6a42bae236b114d6b) aa endm endr irp aa |
| --- |

## [◆ ](#a65db1da5eb749b340685303a403ae14d)ab

| irp nz macro [MOVR](asm-macro-32-bit-mwdt_8h.md#a62c92c2e7e269b0afb80256c5207da7b) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) movl [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) endm endr irp aw macro [LDR](asm-macro-32-bit-mwdt_8h.md#a1a46311eefaef8a6a42bae236b114d6b) [aa](#a8be979fed261ea1fe93f3bf629f3aa9b) endm endr irp ab |
| --- |

## [◆ ](#ac93d5f4341d561a6bd9864e880cffcf4)as

| irp nz macro [MOVR](asm-macro-32-bit-mwdt_8h.md#a62c92c2e7e269b0afb80256c5207da7b) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) movl [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) [s](#a53a876d393ad3ed42cfeb2173695978d) endm endr irp aw macro [LDR](asm-macro-32-bit-mwdt_8h.md#a1a46311eefaef8a6a42bae236b114d6b) [aa](#a8be979fed261ea1fe93f3bf629f3aa9b) endm endr irp as |
| --- |

## [◆ ](#a6bcd6506e83f22db3e77c1172a6d7ba6)cc

| workaround assembler barfing for ST if else stl [aa](#a8be979fed261ea1fe93f3bf629f3aa9b) endif endm endr macro [STR](asm-macro-32-bit-mwdt_8h.md#a2559ca808b98187e087954aafba01ad1) else if [off](#adbc19a384ffe3a93866980a920b08394) [STR](asm-macro-32-bit-mwdt_8h.md#a2559ca808b98187e087954aafba01ad1) [as](#ac93d5f4341d561a6bd9864e880cffcf4) [off](#adbc19a384ffe3a93866980a920b08394) else stl endif endif endm macro [PUSHR](asm-macro-32-bit-mwdt_8h.md#aaecb2f53890260a5b5518501ac4ae55b) [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [POPR](asm-macro-32-bit-mwdt_8h.md#a0f674b4d35f1df924883bff738f5c288) [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [LRR](asm-macro-32-bit-mwdt_8h.md#af065467bfff1489bf1d38337a5d60988) aux lrl aux endm macro [SRR](asm-macro-32-bit-mwdt_8h.md#a4ab637a402c195c93f2e5f1d0fcccf78) aux srl aux endm irp nz macro [ADDR](asm-macro-32-bit-mwdt_8h.md#a74d94870ad16a58f150bf43374bcc908) cc v addl cc v endm endr irp nz macro [ADD2R](asm-macro-32-bit-mwdt_8h.md#a4213081f87edc43524180616979bd1b8) cc v add2l cc v endm endr macro [ADD3R](asm-macro-32-bit-mwdt_8h.md#a9cb390b45f968e4859be09505e376ff6) v add3l v endm macro [SUBR](asm-macro-32-bit-mwdt_8h.md#a1548d46b55a34b4830367a41995f6f48) v subl v endm macro [BMSKNR](asm-macro-32-bit-mwdt_8h.md#aa4129c1e4b6617f30740aada9bdd872d) v bmsknl v endm macro [LSRR](asm-macro-32-bit-mwdt_8h.md#a8667c7c46bc57aff0cac0ca728023ed5) v lsrl v endm macro [ASLR](asm-macro-32-bit-mwdt_8h.md#aaff8d26b5c5198b247467cb55a7df38b) v asll v endm macro [ANDR](asm-macro-32-bit-mwdt_8h.md#abf83bab508dfaea0c41d8093d7b1c551) v andl v endm macro v orl v endm irp eq macro [BRR](asm-macro-32-bit-mwdt_8h.md#a3b737f39fe46787abeecc3661fad4946) cc lbl br cc |
| --- |

## [◆ ](#abaebda2ebe87111969af89be8895e417)d

| macro [s](#a53a876d393ad3ed42cfeb2173695978d) movl &$suffix [s](#a53a876d393ad3ed42cfeb2173695978d) endm macro [off](#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro lbl br &$suffix l lbl endm macro lbl breql d |
| --- |

## [◆ ](#a0ef89636f8d03ae88717291e66d59527)hi

| irp hi |
| --- |

## [◆ ](#a8de167d4ebfa82a6635ea26eee8c907c)ne

| workaround assembler barfing for ST if else st [aa](#a8be979fed261ea1fe93f3bf629f3aa9b) endif endm endr macro [PUSHR](asm-macro-32-bit-mwdt_8h.md#aaecb2f53890260a5b5518501ac4ae55b) [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [POPR](asm-macro-32-bit-mwdt_8h.md#a0f674b4d35f1df924883bff738f5c288) [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [LRR](asm-macro-32-bit-mwdt_8h.md#af065467bfff1489bf1d38337a5d60988) aux lr aux endm macro [SRR](asm-macro-32-bit-mwdt_8h.md#a4ab637a402c195c93f2e5f1d0fcccf78) aux sr aux endm irp nz macro [ADDR](asm-macro-32-bit-mwdt_8h.md#a74d94870ad16a58f150bf43374bcc908) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v add [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v endm endr irp nz macro [ADD2R](asm-macro-32-bit-mwdt_8h.md#a4213081f87edc43524180616979bd1b8) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v add2 [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v endm endr macro [ADD3R](asm-macro-32-bit-mwdt_8h.md#a9cb390b45f968e4859be09505e376ff6) v add3 v endm macro [SUBR](asm-macro-32-bit-mwdt_8h.md#a1548d46b55a34b4830367a41995f6f48) v sub v endm macro [BMSKNR](asm-macro-32-bit-mwdt_8h.md#aa4129c1e4b6617f30740aada9bdd872d) v bmskn v endm macro [LSRR](asm-macro-32-bit-mwdt_8h.md#a8667c7c46bc57aff0cac0ca728023ed5) v lsr v endm macro [ASLR](asm-macro-32-bit-mwdt_8h.md#aaff8d26b5c5198b247467cb55a7df38b) v asl v endm macro [ANDR](asm-macro-32-bit-mwdt_8h.md#abf83bab508dfaea0c41d8093d7b1c551) v and v endm macro v or v endm irp ne |
| --- |

## [◆ ](#adbc19a384ffe3a93866980a920b08394)off

| workaround assembler barfing for ST if else stl [aa](#a8be979fed261ea1fe93f3bf629f3aa9b) endif endm endr macro [STR](asm-macro-32-bit-mwdt_8h.md#a2559ca808b98187e087954aafba01ad1) off |
| --- |

**Initial value:**

=0

ld\aa \d

## [◆ ](#a1b3df9ba4c3032118bbf49c7c7e28edd)op1

| macro [s](#a53a876d393ad3ed42cfeb2173695978d) movl &$suffix [s](#a53a876d393ad3ed42cfeb2173695978d) endm macro [off](#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro lbl br &$suffix l lbl endm macro lbl breql lbl endm macro op2 cmpl op1 |
| --- |

## [◆ ](#ad0672a138db1d400f19f2bf7f08c0088)ORR

| workaround assembler barfing for ST if else st [aa](#a8be979fed261ea1fe93f3bf629f3aa9b) endif endm endr macro [PUSHR](asm-macro-32-bit-mwdt_8h.md#aaecb2f53890260a5b5518501ac4ae55b) [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) push [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [POPR](asm-macro-32-bit-mwdt_8h.md#a0f674b4d35f1df924883bff738f5c288) [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) pop [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [LRR](asm-macro-32-bit-mwdt_8h.md#af065467bfff1489bf1d38337a5d60988) aux lr aux endm macro [SRR](asm-macro-32-bit-mwdt_8h.md#a4ab637a402c195c93f2e5f1d0fcccf78) aux sr aux endm irp nz macro [ADDR](asm-macro-32-bit-mwdt_8h.md#a74d94870ad16a58f150bf43374bcc908) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v add [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v endm endr irp nz macro [ADD2R](asm-macro-32-bit-mwdt_8h.md#a4213081f87edc43524180616979bd1b8) [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v add2 [cc](#a6bcd6506e83f22db3e77c1172a6d7ba6) v endm endr macro [ADD3R](asm-macro-32-bit-mwdt_8h.md#a9cb390b45f968e4859be09505e376ff6) v add3 v endm macro [SUBR](asm-macro-32-bit-mwdt_8h.md#a1548d46b55a34b4830367a41995f6f48) v sub v endm macro [BMSKNR](asm-macro-32-bit-mwdt_8h.md#aa4129c1e4b6617f30740aada9bdd872d) v bmskn v endm macro [LSRR](asm-macro-32-bit-mwdt_8h.md#a8667c7c46bc57aff0cac0ca728023ed5) v lsr v endm macro [ASLR](asm-macro-32-bit-mwdt_8h.md#aaff8d26b5c5198b247467cb55a7df38b) v asl v endm macro [ANDR](asm-macro-32-bit-mwdt_8h.md#abf83bab508dfaea0c41d8093d7b1c551) v and v endm macro ORR |
| --- |

## [◆ ](#af16d2973cfd145a2ebdbf9528d5d9ae2)r

| workaround assembler barfing for ST r |
| --- |

## [◆ ](#a53a876d393ad3ed42cfeb2173695978d)s

| macro s movl &$suffix s endm macro [off](#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro lbl br &$suffix l lbl endm macro lbl breql s |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [asm-compat](dir_728f9cb61d4414cdda9196b7386075ee.md)
- [asm-macro-32-bit-gnu.h](asm-macro-32-bit-gnu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
