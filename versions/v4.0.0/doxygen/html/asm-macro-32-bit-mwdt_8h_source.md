---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/asm-macro-32-bit-mwdt_8h_source.html
original_path: doxygen/html/asm-macro-32-bit-mwdt_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm-macro-32-bit-mwdt.h

[Go to the documentation of this file.](asm-macro-32-bit-mwdt_8h.md)

1/\* SPDX-License-Identifier: Apache-2.0 \*/

2/\*

3 \* Copyright (C) 2021 Synopsys, Inc. (www.synopsys.com)

4 \*

5 \* ALU/Memory instructions pseudo-mnemonics for ARCv2 and ARC32 ISA

6 \*/

7

[ 8](asm-macro-32-bit-mwdt_8h.md#aabf7c54edb88081579e2b6fc941f10e9).macro [MOVR](asm-macro-32-bit-mwdt_8h.md#a62c92c2e7e269b0afb80256c5207da7b), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

9 mov\&$suffix [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

10.endm

11

12

[ 13](asm-macro-32-bit-mwdt_8h.md#a1a46311eefaef8a6a42bae236b114d6b).macro [LDR](asm-macro-32-bit-mwdt_8h.md#a1a46311eefaef8a6a42bae236b114d6b), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

[ 14](asm-macro-32-bit-mwdt_8h.md#ac743b07138dff5c6fe59b445965c1fc7) .if [$narg](asm-macro-32-bit-mwdt_8h.md#ac743b07138dff5c6fe59b445965c1fc7) == 2

15 ld\&$suffix [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)]

16 .else

17 ld\&$suffix [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)]

18 .endif

19.endm

20

[ 21](asm-macro-32-bit-mwdt_8h.md#a2559ca808b98187e087954aafba01ad1).macro [STR](asm-macro-32-bit-mwdt_8h.md#a2559ca808b98187e087954aafba01ad1), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

22 .if [$narg](asm-macro-32-bit-mwdt_8h.md#ac743b07138dff5c6fe59b445965c1fc7) == 2

23 st\&$suffix [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)]

24 .else

25 st\&$suffix [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)]

26 .endif

27.endm

28

29

[ 30](asm-macro-32-bit-mwdt_8h.md#aaecb2f53890260a5b5518501ac4ae55b).macro [PUSHR](asm-macro-32-bit-mwdt_8h.md#aaecb2f53890260a5b5518501ac4ae55b), [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

31 push [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

32.endm

33

[ 34](asm-macro-32-bit-mwdt_8h.md#a0f674b4d35f1df924883bff738f5c288).macro [POPR](asm-macro-32-bit-mwdt_8h.md#a0f674b4d35f1df924883bff738f5c288), [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

35 pop [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

36.endm

37

[ 38](asm-macro-32-bit-mwdt_8h.md#af065467bfff1489bf1d38337a5d60988).macro [LRR](asm-macro-32-bit-mwdt_8h.md#af065467bfff1489bf1d38337a5d60988), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), aux

39 lr [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), aux

40.endm

41

[ 42](asm-macro-32-bit-mwdt_8h.md#a4ab637a402c195c93f2e5f1d0fcccf78).macro [SRR](asm-macro-32-bit-mwdt_8h.md#a4ab637a402c195c93f2e5f1d0fcccf78), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), aux

43 sr [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), aux

44.endm

45

46

[ 47](asm-macro-32-bit-mwdt_8h.md#a74d94870ad16a58f150bf43374bcc908).macro [ADDR](asm-macro-32-bit-mwdt_8h.md#a74d94870ad16a58f150bf43374bcc908), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

48 add\&$suffix [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

49.endm

50

[ 51](asm-macro-32-bit-mwdt_8h.md#a4213081f87edc43524180616979bd1b8).macro [ADD2R](asm-macro-32-bit-mwdt_8h.md#a4213081f87edc43524180616979bd1b8), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

52 add2\&$suffix [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

53.endm

54

[ 55](asm-macro-32-bit-mwdt_8h.md#a9cb390b45f968e4859be09505e376ff6).macro [ADD3R](asm-macro-32-bit-mwdt_8h.md#a9cb390b45f968e4859be09505e376ff6), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

56 add3 [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

57.endm

58

[ 59](asm-macro-32-bit-mwdt_8h.md#a1548d46b55a34b4830367a41995f6f48).macro [SUBR](asm-macro-32-bit-mwdt_8h.md#a1548d46b55a34b4830367a41995f6f48), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

60 sub [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

61.endm

62

[ 63](asm-macro-32-bit-mwdt_8h.md#aa4129c1e4b6617f30740aada9bdd872d).macro [BMSKNR](asm-macro-32-bit-mwdt_8h.md#aa4129c1e4b6617f30740aada9bdd872d), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

64 bmskn [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

65.endm

66

[ 67](asm-macro-32-bit-mwdt_8h.md#a8667c7c46bc57aff0cac0ca728023ed5).macro [LSRR](asm-macro-32-bit-mwdt_8h.md#a8667c7c46bc57aff0cac0ca728023ed5), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

68 lsr [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

69.endm

70

[ 71](asm-macro-32-bit-mwdt_8h.md#aaff8d26b5c5198b247467cb55a7df38b).macro [ASLR](asm-macro-32-bit-mwdt_8h.md#aaff8d26b5c5198b247467cb55a7df38b), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

72 asl [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

73.endm

74

[ 75](asm-macro-32-bit-mwdt_8h.md#abf83bab508dfaea0c41d8093d7b1c551).macro [ANDR](asm-macro-32-bit-mwdt_8h.md#abf83bab508dfaea0c41d8093d7b1c551), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

76 and [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

77.endm

78

[ 79](asm-macro-32-bit-mwdt_8h.md#ac61c6a6fd2801a19a8746a437a7b2a4a).macro [ORR](asm-macro-32-bit-gnu_8h.md#ad0672a138db1d400f19f2bf7f08c0088), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

80 or [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

81.endm

82

[ 83](asm-macro-32-bit-mwdt_8h.md#a3b737f39fe46787abeecc3661fad4946).macro [BRR](asm-macro-32-bit-mwdt_8h.md#a3b737f39fe46787abeecc3661fad4946), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), lbl

84 br\&$suffix [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), lbl

85.endm

86

[ 87](asm-macro-32-bit-mwdt_8h.md#abe3bac34bb316244a20ddc88ebc75937).macro [BREQR](asm-macro-32-bit-mwdt_8h.md#abe3bac34bb316244a20ddc88ebc75937), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), lbl

88 breq [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), lbl

89.endm

90

[ 91](asm-macro-32-bit-mwdt_8h.md#a2914e6612b9957eba801ab818e2cbded).macro [CMPR](asm-macro-32-bit-mwdt_8h.md#a2914e6612b9957eba801ab818e2cbded), [op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), op2

92 cmp [op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), op2

93.endm

[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd)

workaround assembler barfing for ST if else st aa endif endm endr macro PUSHR r push r endm macro POPR r pop r endm macro LRR aux lr aux endm macro SRR aux sr aux endm irp nz macro ADDR cc v add cc v endm endr irp nz macro ADD2R cc v add2 cc v endm endr macro ADD3R v add3 v endm macro SUBR v sub v endm macro BMSKNR v bmskn v endm macro LSRR v lsr v endm macro ASLR v asl v endm macro ANDR v and v endm macro v or v endm irp eq macro BRR cc lbl br cc lbl endm endr macro BREQR lbl breq lbl endm macro CMPR op1

**Definition** asm-macro-32-bit-gnu.h:99

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[ORR](asm-macro-32-bit-gnu_8h.md#ad0672a138db1d400f19f2bf7f08c0088)

workaround assembler barfing for ST if else st aa endif endm endr macro PUSHR r push r endm macro POPR r pop r endm macro LRR aux lr aux endm macro SRR aux sr aux endm irp nz macro ADDR cc v add cc v endm endr irp nz macro ADD2R cc v add2 cc v endm endr macro ADD3R v add3 v endm macro SUBR v sub v endm macro BMSKNR v bmskn v endm macro LSRR v lsr v endm macro ASLR v asl v endm macro ANDR v and v endm macro ORR

**Definition** asm-macro-32-bit-gnu.h:85

[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa off

**Definition** asm-macro-32-bit-gnu.h:17

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[POPR](asm-macro-32-bit-mwdt_8h.md#a0f674b4d35f1df924883bff738f5c288)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro POPR

**Definition** asm-macro-32-bit-mwdt.h:34

[SUBR](asm-macro-32-bit-mwdt_8h.md#a1548d46b55a34b4830367a41995f6f48)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro SUBR

**Definition** asm-macro-32-bit-mwdt.h:59

[LDR](asm-macro-32-bit-mwdt_8h.md#a1a46311eefaef8a6a42bae236b114d6b)

macro s mov &$suffix s endm macro LDR

**Definition** asm-macro-32-bit-mwdt.h:13

[STR](asm-macro-32-bit-mwdt_8h.md#a2559ca808b98187e087954aafba01ad1)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro STR

**Definition** asm-macro-32-bit-mwdt.h:21

[CMPR](asm-macro-32-bit-mwdt_8h.md#a2914e6612b9957eba801ab818e2cbded)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro lbl br &$suffix lbl endm macro lbl breq lbl endm macro CMPR

**Definition** asm-macro-32-bit-mwdt.h:91

[BRR](asm-macro-32-bit-mwdt_8h.md#a3b737f39fe46787abeecc3661fad4946)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro BRR

**Definition** asm-macro-32-bit-mwdt.h:83

[ADD2R](asm-macro-32-bit-mwdt_8h.md#a4213081f87edc43524180616979bd1b8)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro ADD2R

**Definition** asm-macro-32-bit-mwdt.h:51

[SRR](asm-macro-32-bit-mwdt_8h.md#a4ab637a402c195c93f2e5f1d0fcccf78)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro SRR

**Definition** asm-macro-32-bit-mwdt.h:42

[MOVR](asm-macro-32-bit-mwdt_8h.md#a62c92c2e7e269b0afb80256c5207da7b)

macro MOVR

**Definition** asm-macro-32-bit-mwdt.h:8

[ADDR](asm-macro-32-bit-mwdt_8h.md#a74d94870ad16a58f150bf43374bcc908)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro aux sr aux endm macro ADDR

**Definition** asm-macro-32-bit-mwdt.h:47

[LSRR](asm-macro-32-bit-mwdt_8h.md#a8667c7c46bc57aff0cac0ca728023ed5)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro LSRR

**Definition** asm-macro-32-bit-mwdt.h:67

[ADD3R](asm-macro-32-bit-mwdt_8h.md#a9cb390b45f968e4859be09505e376ff6)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro ADD3R

**Definition** asm-macro-32-bit-mwdt.h:55

[BMSKNR](asm-macro-32-bit-mwdt_8h.md#aa4129c1e4b6617f30740aada9bdd872d)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro BMSKNR

**Definition** asm-macro-32-bit-mwdt.h:63

[PUSHR](asm-macro-32-bit-mwdt_8h.md#aaecb2f53890260a5b5518501ac4ae55b)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro PUSHR

**Definition** asm-macro-32-bit-mwdt.h:30

[ASLR](asm-macro-32-bit-mwdt_8h.md#aaff8d26b5c5198b247467cb55a7df38b)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro ASLR

**Definition** asm-macro-32-bit-mwdt.h:71

[BREQR](asm-macro-32-bit-mwdt_8h.md#abe3bac34bb316244a20ddc88ebc75937)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro lbl br &$suffix lbl endm macro BREQR

**Definition** asm-macro-32-bit-mwdt.h:87

[ANDR](asm-macro-32-bit-mwdt_8h.md#abf83bab508dfaea0c41d8093d7b1c551)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro ANDR

**Definition** asm-macro-32-bit-mwdt.h:75

[$narg](asm-macro-32-bit-mwdt_8h.md#ac743b07138dff5c6fe59b445965c1fc7)

macro s mov &$suffix s endm macro off if $narg

**Definition** asm-macro-32-bit-mwdt.h:14

[LRR](asm-macro-32-bit-mwdt_8h.md#af065467bfff1489bf1d38337a5d60988)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro LRR

**Definition** asm-macro-32-bit-mwdt.h:38

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [asm-compat](dir_728f9cb61d4414cdda9196b7386075ee.md)
- [asm-macro-32-bit-mwdt.h](asm-macro-32-bit-mwdt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
