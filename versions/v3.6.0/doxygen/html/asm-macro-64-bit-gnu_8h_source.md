---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/asm-macro-64-bit-gnu_8h_source.html
original_path: doxygen/html/asm-macro-64-bit-gnu_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm-macro-64-bit-gnu.h

[Go to the documentation of this file.](asm-macro-64-bit-gnu_8h.md)

1/\* SPDX-License-Identifier: Apache-2.0 \*/

2/\*

3 \* Copyright (C) 2021 Synopsys, Inc. (www.synopsys.com)

4 \*

5 \* Author: Vineet Gupta <vgupta@synopsys.com>

6 \*

7 \* pseudo-mnemonics for ALU/Memory instructions for ARC64 ISA

8 \*/

9

[ 10](asm-macro-64-bit-gnu_8h.md#a542424a4ef87da5a865ce186a46d9c58).irp [cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6),,.hi,.nz

[ 11](asm-macro-64-bit-gnu_8h.md#a6b6a358e951559f7fd95cb1da716005c).macro MOVR\cc [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

12 movl\cc \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

13.endm

14.endr

15

[ 16](asm-macro-64-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b).irp [aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b),,.ab,.as,.aw

[ 17](asm-macro-64-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394).macro LDR\aa [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)=0

18 ldl\aa \d, [\[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)]

19.endm

20.endr

21

22.irp [aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b),.ab,.as,.aw

23.macro STR\aa [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)=0

[ 24](asm-macro-64-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) ; workaround assembler barfing for ST [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [@symb, 0]

25 .if \off == 0

26 stl\aa \d, [\[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)]

27 .else

28 stl\aa \d, [\[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)]

29 .endif

30.endm

31.endr

32

33.macro [STR](asm-macro-32-bit-mwdt_8h.md#a2559ca808b98187e087954aafba01ad1) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)=0

34 .if \off == 0

35 stl \d, [\[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)]

36 .else

37 .if \off > 255

38 [STR](asm-macro-32-bit-mwdt_8h.md#a2559ca808b98187e087954aafba01ad1).as \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) / 8

39 .else

40 stl \d, [\[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)]

41 .endif

42 .endif

43.endm

44

45.macro [PUSHR](asm-macro-32-bit-mwdt_8h.md#aaecb2f53890260a5b5518501ac4ae55b) [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

46 pushl \r

47.endm

48

49.macro [POPR](asm-macro-32-bit-mwdt_8h.md#a0f674b4d35f1df924883bff738f5c288) [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

50 popl \r

51.endm

52

53.macro [LRR](asm-macro-32-bit-mwdt_8h.md#af065467bfff1489bf1d38337a5d60988) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), aux

54 lrl \d, \aux

55.endm

56

57.macro [SRR](asm-macro-32-bit-mwdt_8h.md#a4ab637a402c195c93f2e5f1d0fcccf78) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), aux

58 srl \d, \aux

59.endm

60

61.irp [cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6),,.nz

62.macro ADDR\cc [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

63 addl\cc \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

64.endm

65.endr

66

67.irp [cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6),,.nz

68.macro ADD2R\cc [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

69 add2l\cc \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

70.endm

71.endr

72

73.macro [ADD3R](asm-macro-32-bit-mwdt_8h.md#a9cb390b45f968e4859be09505e376ff6) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

74 add3l \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

75.endm

76

77.macro [SUBR](asm-macro-32-bit-mwdt_8h.md#a1548d46b55a34b4830367a41995f6f48) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

78 subl \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

79.endm

80

81.macro [BMSKNR](asm-macro-32-bit-mwdt_8h.md#aa4129c1e4b6617f30740aada9bdd872d) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

82 bmsknl \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

83.endm

84

85.macro [LSRR](asm-macro-32-bit-mwdt_8h.md#a8667c7c46bc57aff0cac0ca728023ed5) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

86 lsrl \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

87.endm

88

89.macro [ASLR](asm-macro-32-bit-mwdt_8h.md#aaff8d26b5c5198b247467cb55a7df38b) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

90 asll \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

91.endm

92

93.macro [ANDR](asm-macro-32-bit-mwdt_8h.md#abf83bab508dfaea0c41d8093d7b1c551) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

94 andl \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

95.endm

96

[ 97](asm-macro-64-bit-gnu_8h.md#a73772c29f6eea427991a6d445478808d).macro [ORR](asm-macro-32-bit-gnu_8h.md#ad0672a138db1d400f19f2bf7f08c0088), [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), v

98 orl \d, \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \v

99.endm

100

[ 101](asm-macro-64-bit-gnu_8h.md#a69384ae28398c3f7eb9ffc42f9fb3df2).irp [cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6),[ne](asm-macro-32-bit-gnu_8h.md#a8de167d4ebfa82a6635ea26eee8c907c),eq

102.macro BRR\cc [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), lbl

103 br\cc\‍()l \[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \lbl

104.endm

105.endr

106

107.macro [BREQR](asm-macro-32-bit-mwdt_8h.md#abe3bac34bb316244a20ddc88ebc75937) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), lbl

108 breql \[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), \[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), \lbl

109.endm

110

[ 111](asm-macro-64-bit-gnu_8h.md#a0f83c16c864dd25dbe54e81e22ea092a).macro [CMPR](asm-macro-32-bit-mwdt_8h.md#a2914e6612b9957eba801ab818e2cbded) [op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), op2

112 cmpl \[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), \op2

113.endm

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

[STR](asm-macro-32-bit-mwdt_8h.md#a2559ca808b98187e087954aafba01ad1)

macro s mov &$suffix s endm macro off if else ld &$suffix endif endm macro STR

**Definition** asm-macro-32-bit-mwdt.h:21

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
- [asm-macro-64-bit-gnu.h](asm-macro-64-bit-gnu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
