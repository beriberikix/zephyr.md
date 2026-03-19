---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arch_2arm_2thread_8h_source.html
original_path: doxygen/html/arch_2arm_2thread_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](arch_2arm_2thread_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

18

19#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_THREAD\_H\_

20#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_THREAD\_H\_

21

22#ifndef \_ASMLANGUAGE

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24

25struct \_callee\_saved {

26 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) v1; /\* r4 \*/

27 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) v2; /\* r5 \*/

28 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) v3; /\* r6 \*/

29 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) v4; /\* r7 \*/

30 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) v5; /\* r8 \*/

31 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) v6; /\* r9 \*/

32 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) v7; /\* r10 \*/

33 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) v8; /\* r11 \*/

34 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) psp; /\* r13 \*/

35#ifdef CONFIG\_USE\_SWITCH

36 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lr; /\* lr \*/

37#endif

38};

39

40typedef struct \_callee\_saved \_callee\_saved\_t;

41

42#if defined(CONFIG\_FPU) && defined(CONFIG\_FPU\_SHARING)

43struct \_preempt\_float {

44 float s16;

45 float s17;

46 float s18;

47 float s19;

48 float s20;

49 float s21;

50 float s22;

51 float s23;

52 float s24;

53 float s25;

54 float s26;

55 float s27;

56 float s28;

57 float s29;

58 float s30;

59 float s31;

60};

61#endif

62

63struct \_thread\_arch {

64

65 /\* interrupt locking key \*/

66 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) basepri;

67

68 /\* r0 in stack frame cannot be written to reliably \*/

69 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) swap\_return\_value;

70

71#if defined(CONFIG\_FPU) && defined(CONFIG\_FPU\_SHARING)

72 /\*

73 \* No cooperative floating point register set structure exists for

74 \* the Cortex-M as it automatically saves the necessary registers

75 \* in its exception stack frame.

76 \*/

77 struct \_preempt\_float preempt\_float;

78#endif

79

80#if defined(CONFIG\_CPU\_AARCH32\_CORTEX\_A) || defined(CONFIG\_CPU\_AARCH32\_CORTEX\_R)

81 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) exception\_depth;

82#endif

83

84#if defined(CONFIG\_ARM\_STORE\_EXC\_RETURN) || defined(CONFIG\_USERSPACE)

85 /\*

86 \* Status variable holding several thread status flags

87 \* as follows:

88 \*

89 \* byte 0

90 \* +-bits 4-7-----bit-3----------bit-2--------bit-1---+----bit-0------+

91 \* : | | | | |

92 \* : reserved |<Guard FLOAT>| reserved | reserved | <priv mode> |

93 \* : bits | | | | CONTROL.nPRIV |

94 \* +------------------------------------------------------------------+

95 \*

96 \* byte 1

97 \* +----------------------------bits 8-15-----------------------------+

98 \* : Least significant byte of EXC\_RETURN |

99 \* : bit 15| bit 14| bit 13 | bit 12| bit 11 | bit 10 | bit 9 | bit 8 |

100 \* : Res | S | DCRS | FType | Mode | SPSel | Res | ES |

101 \* +------------------------------------------------------------------+

102 \*

103 \* Bit 0: thread's current privileged mode (Supervisor or User mode)

104 \* Mirrors CONTROL.nPRIV flag.

105 \* Bit 2: Deprecated in favor of FType. Note: FType = !CONTROL.FPCA.

106 \* indicating whether the thread has an active FP context.

107 \* Mirrors CONTROL.FPCA flag.

108 \* Bit 3: indicating whether the thread is applying the long (FLOAT)

109 \* or the default MPU stack guard size.

110 \*

111 \* Bits 8-15: Least significant octet of the EXC\_RETURN value when a

112 \* thread is switched-out. The value is copied from LR when

113 \* entering the PendSV handler. When the thread is

114 \* switched in again, the value is restored to LR before

115 \* exiting the PendSV handler.

116 \*/

117 union {

118 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mode;

119

120#if defined(CONFIG\_ARM\_STORE\_EXC\_RETURN)

121 struct {

122 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode\_bits;

123 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode\_exc\_return;

124 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mode\_reserved2;

125 };

126#endif

127 };

128

129#if defined(CONFIG\_USERSPACE)

130 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) priv\_stack\_start;

131#if defined(CONFIG\_CPU\_AARCH32\_CORTEX\_R)

132 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) priv\_stack\_end;

133 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sp\_usr;

134#endif

135#endif

136#endif

137};

138

139#if defined(CONFIG\_FPU\_SHARING) && defined(CONFIG\_MPU\_STACK\_GUARD)

140#define Z\_ARM\_MODE\_MPU\_GUARD\_FLOAT\_Msk (1 << 3)

141#endif

142typedef struct \_thread\_arch \_thread\_arch\_t;

143

144#endif /\* \_ASMLANGUAGE \*/

145

146#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_THREAD\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [thread.h](arch_2arm_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
