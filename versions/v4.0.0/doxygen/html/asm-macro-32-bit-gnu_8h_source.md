---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/asm-macro-32-bit-gnu_8h_source.html
original_path: doxygen/html/asm-macro-32-bit-gnu_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm-macro-32-bit-gnu.h

[Go to the documentation of this file.](asm-macro-32-bit-gnu_8h.md)

1/\* SPDX-License-Identifier: Apache-2.0 \*/

2/\*

3 \* Copyright (C) 2021 Synopsys, Inc. (www.synopsys.com)

4 \*

5 \* Author: Vineet Gupta <vgupta@synopsys.com>

6 \*

7 \* ALU/Memory instructions pseudo-mnemonics for ARCv2 and ARC32 ISA

8 \*/

9

[ 10](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6).irp [cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6),,.hi,.nz

[ 11](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417).macro MOVR\cc [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

12 mov\cc \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

13.endm

14.endr

15

[ 16](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b).irp [aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b),,.ab,.as,.aw

[ 17](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394).macro LDR\aa [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)=0

18 ld\aa \d, [\[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)]

19.endm

20.endr

21

22.irp [aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b),,.ab,.as,.aw

23.macro STR\aa [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)=0

[ 24](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) ; workaround assembler barfing for ST [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [@symb, 0]

25 .if \off == 0

26 st\aa \d, [\[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)]

27 .else

28 st\aa \d, [\[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)]

29 .endif

30.endm

31.endr

32

33.macro [PUSHR](asm-macro-32-bit-mwdt_8h.md#aaecb2f53890260a5b5518501ac4ae55b) [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

34 push \r

35.endm

36

37.macro [POPR](asm-macro-32-bit-mwdt_8h.md#a0f674b4d35f1df924883bff738f5c288) [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

38 pop \r

39.endm

40

41.macro [LRR](asm-macro-32-bit-mwdt_8h.md#af065467bfff1489bf1d38337a5d60988) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), aux

42 lr \d, \aux

43.endm

44

45.macro [SRR](asm-macro-32-bit-mwdt_8h.md#a4ab637a402c195c93f2e5f1d0fcccf78) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), aux

46 sr \d, \aux

47.endm

48

49.irp [cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6),,.nz

50.macro ADDR\cc [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

51 add\cc \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

52.endm

53.endr

54

55.irp [cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6),,.nz

56.macro ADD2R\cc [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

57 add2\cc \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

58.endm

59.endr

60

61.macro [ADD3R](asm-macro-32-bit-mwdt_8h.md#a9cb390b45f968e4859be09505e376ff6) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

62 add3 \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

63.endm

64

65.macro [SUBR](asm-macro-32-bit-mwdt_8h.md#a1548d46b55a34b4830367a41995f6f48) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

66 sub \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

67.endm

68

69.macro [BMSKNR](asm-macro-32-bit-mwdt_8h.md#aa4129c1e4b6617f30740aada9bdd872d) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

70 bmskn \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

71.endm

72

73.macro [LSRR](asm-macro-32-bit-mwdt_8h.md#a8667c7c46bc57aff0cac0ca728023ed5) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

74 lsr \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

75.endm

76

77.macro [ASLR](asm-macro-32-bit-mwdt_8h.md#aaff8d26b5c5198b247467cb55a7df38b) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

78 asl \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

79.endm

80

81.macro [ANDR](asm-macro-32-bit-mwdt_8h.md#abf83bab508dfaea0c41d8093d7b1c551) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

82 and \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

83.endm

84

[ 85](asm-macro-32-bit-gnu_8h.md#ad0672a138db1d400f19f2bf7f08c0088).macro [ORR](asm-macro-32-bit-gnu_8h.md#ad0672a138db1d400f19f2bf7f08c0088), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

86 or \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

87.endm

88

[ 89](asm-macro-32-bit-gnu_8h.md#a8de167d4ebfa82a6635ea26eee8c907c).irp [cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6),[ne](asm-macro-32-bit-gnu_8h.md#a8de167d4ebfa82a6635ea26eee8c907c),eq

90.macro BRR\cc [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), lbl

91 br\cc \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \lbl

92.endm

93.endr

94

95.macro [BREQR](asm-macro-32-bit-mwdt_8h.md#abe3bac34bb316244a20ddc88ebc75937) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), lbl

96 breq \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \lbl

97.endm

98

[ 99](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd).macro [CMPR](asm-macro-32-bit-mwdt_8h.md#a2914e6612b9957eba801ab818e2cbded) [op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), op2

100 cmp \op1, \op2

101.endm

[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd)

workaround assembler barfing for ST if else st aa endif endm endr macro PUSHR r push r endm macro POPR r pop r endm macro LRR aux lr aux endm macro SRR aux sr aux endm irp nz macro ADDR cc v add cc v endm endr irp nz macro ADD2R cc v add2 cc v endm endr macro ADD3R v add3 v endm macro SUBR v sub v endm macro BMSKNR v bmskn v endm macro LSRR v lsr v endm macro ASLR v asl v endm macro ANDR v and v endm macro v or v endm irp eq macro BRR cc lbl br cc lbl endm endr macro BREQR lbl breq lbl endm macro CMPR op1

**Definition** asm-macro-32-bit-gnu.h:99

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6)

irp cc

**Definition** asm-macro-32-bit-gnu.h:10

[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b)

irp nz macro MOVR cc s mov cc s endm endr irp aa

**Definition** asm-macro-32-bit-gnu.h:16

[ne](asm-macro-32-bit-gnu_8h.md#a8de167d4ebfa82a6635ea26eee8c907c)

workaround assembler barfing for ST if else st aa endif endm endr macro PUSHR r push r endm macro POPR r pop r endm macro LRR aux lr aux endm macro SRR aux sr aux endm irp nz macro ADDR cc v add cc v endm endr irp nz macro ADD2R cc v add2 cc v endm endr macro ADD3R v add3 v endm macro SUBR v sub v endm macro BMSKNR v bmskn v endm macro LSRR v lsr v endm macro ASLR v asl v endm macro ANDR v and v endm macro v or v endm irp ne

**Definition** asm-macro-32-bit-gnu.h:89

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

[CMPR](asm-macro-32-bit-mwdt_8h.md#a2914e6612b9957eba801ab818e2cbded)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro aux sr aux endm macro v add &$suffix v endm macro v add2 &$suffix v endm macro v add3 v endm macro v sub v endm macro v bmskn v endm macro v lsr v endm macro v asl v endm macro v and v endm macro v or v endm macro lbl br &$suffix lbl endm macro lbl breq lbl endm macro CMPR

**Definition** asm-macro-32-bit-mwdt.h:91

[SRR](asm-macro-32-bit-mwdt_8h.md#a4ab637a402c195c93f2e5f1d0fcccf78)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro aux lr aux endm macro SRR

**Definition** asm-macro-32-bit-mwdt.h:42

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

[LRR](asm-macro-32-bit-mwdt_8h.md#af065467bfff1489bf1d38337a5d60988)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro off if else st &$suffix endif endm macro r push r endm macro r pop r endm macro LRR

**Definition** asm-macro-32-bit-mwdt.h:38

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [asm-compat](dir_728f9cb61d4414cdda9196b7386075ee.md)
- [asm-macro-32-bit-gnu.h](asm-macro-32-bit-gnu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
