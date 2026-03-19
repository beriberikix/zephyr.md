---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/msr_8h_source.html
original_path: doxygen/html/msr_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

msr.h

[Go to the documentation of this file.](msr_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corp.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_MSR\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_X86\_MSR\_H\_

8

9/\*

10 \* Model specific registers (MSR). Access with z\_x86\_msr\_read/write().

11 \*/

12

[ 13](msr_8h.md#a6a8159994070c5d75a390f81ae460dee)#define X86\_TIME\_STAMP\_COUNTER\_MSR 0x00000010

14

[ 15](msr_8h.md#ab89835f2b734a80195db70d28749e7c1)#define X86\_SPEC\_CTRL\_MSR 0x00000048

[ 16](msr_8h.md#aa7de592375a86f19136972a5bd4c8453)#define X86\_SPEC\_CTRL\_MSR\_IBRS BIT(0)

[ 17](msr_8h.md#aa267e6d482addf97eb630f208281000d)#define X86\_SPEC\_CTRL\_MSR\_SSBD BIT(2)

18

[ 19](msr_8h.md#a0083758907f732a480f8a9ec2ccb3778)#define X86\_APIC\_BASE\_MSR 0x0000001b

[ 20](msr_8h.md#a940221ed627aad8120e2abb0c12ff196)#define X86\_APIC\_BASE\_MSR\_X2APIC BIT(10)

21

[ 22](msr_8h.md#aa5479ba3ca3bbda70d35819b67d3583f)#define X86\_MTRR\_DEF\_TYPE\_MSR 0x000002ff

[ 23](msr_8h.md#a2c5d224b53d927e325b710484ebfb2a0)#define X86\_MTRR\_DEF\_TYPE\_MSR\_ENABLE BIT(11)

24

[ 25](msr_8h.md#ab5ccd444077064e6b7a399ceb3d61f9f)#define X86\_X2APIC\_BASE\_MSR 0x00000800 /\* .. thru 0x00000BFF \*/

26

[ 27](msr_8h.md#a4226ff6b5ecc23277e9cb0433b0d6c22)#define X86\_EFER\_MSR 0xC0000080U

[ 28](msr_8h.md#ae20fe7661b62a20885d6cef7f83e917e)#define X86\_EFER\_MSR\_SCE BIT(0)

[ 29](msr_8h.md#a4484482d4a9eee0288970fb8a6fc70f5)#define X86\_EFER\_MSR\_LME BIT(8)

[ 30](msr_8h.md#a410a6e81d01226d399b8e24d5506013d)#define X86\_EFER\_MSR\_NXE BIT(11)

31

32/\* STAR 31:0 Unused in long mode

33 \* 47:32 Kernel CS (SS = CS+8)

34 \* 63:48 User CS (SS = CS+8)

35 \*/

[ 36](msr_8h.md#a48b0da8dc9cdd319cf75ac0d5933ce0f)#define X86\_STAR\_MSR 0xC0000081U

37

38/\* Location for system call entry point \*/

[ 39](msr_8h.md#a64cac416a2f72c129bd8e01fd885aaea)#define X86\_LSTAR\_MSR 0xC0000082U

40

41/\* Low 32 bits in this MSR are the SYSCALL mask applied to EFLAGS \*/

[ 42](msr_8h.md#af28b1c23c69f1658384a5de5b9461c64)#define X86\_FMASK\_MSR 0xC0000084U

43

[ 44](msr_8h.md#a935167aeb9bc9b1f4e73d8001c3c72f0)#define X86\_FS\_BASE 0xC0000100U

[ 45](msr_8h.md#a263e74097e9162fd54f5d05af74f4aa1)#define X86\_GS\_BASE 0xC0000101U

[ 46](msr_8h.md#af832b3ce587c52ff9764d42fbd1c1b25)#define X86\_KERNEL\_GS\_BASE 0xC0000102U

47

48#ifndef \_ASMLANGUAGE

49#ifdef \_\_cplusplus

50extern "C" {

51#endif

52

53/\*

54 \* z\_x86\_msr\_write() is shared between 32- and 64-bit implementations, but

55 \* due to ABI differences with long return values, z\_x86\_msr\_read() is not.

56 \*/

57

58static inline void z\_x86\_msr\_write(unsigned int msr, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) data)

59{

60 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) high = data >> 32;

61 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) low = data & 0xFFFFFFFFU;

62

63 \_\_asm\_\_ volatile ("wrmsr" : : "c"(msr), "a"(low), "d"(high));

64}

65

66#ifdef CONFIG\_X86\_64

67

68static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) z\_x86\_msr\_read(unsigned int msr)

69{

70 union {

71 struct {

72 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lo;

73 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hi](asm-macro-32-bit-gnu_8h.md#a0ef89636f8d03ae88717291e66d59527);

74 };

75 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value;

76 } rv;

77

78 \_\_asm\_\_ volatile ("rdmsr" : "=a" (rv.lo), "=d" (rv.hi) : "c" (msr));

79

80 return rv.value;

81}

82

83#else

84

85static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) z\_x86\_msr\_read(unsigned int msr)

86{

87 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ret;

88

89 \_\_asm\_\_ volatile("rdmsr" : "=A" (ret) : "c" (msr));

90

91 return ret;

92}

93

94#endif

95

96#ifdef \_\_cplusplus

97}

98#endif

99#endif /\* \_ASMLANGUAGE \*/

100

101#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_MSR\_H\_ \*/

[hi](asm-macro-32-bit-gnu_8h.md#a0ef89636f8d03ae88717291e66d59527)

irp hi

**Definition** asm-macro-32-bit-gnu.h:10

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [msr.h](msr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
