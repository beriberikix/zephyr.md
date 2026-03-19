---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm_2cortex__a__r_2exception_8h_source.html
original_path: doxygen/html/arm_2cortex__a__r_2exception_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](arm_2cortex__a__r_2exception_8h.md)

1/\*

2 \* Copyright (c) 2013-2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_EXCEPTION\_H\_

13#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_EXCEPTION\_H\_

14

15#ifdef \_ASMLANGUAGE

16GTEXT(z\_arm\_exc\_exit);

17#else

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

24#if defined(CONFIG\_FPU) && defined(CONFIG\_FPU\_SHARING)

25

26/\* Registers s16-s31 (d8-d15, q4-q7) must be preserved across subroutine calls.

27 \*

28 \* Registers s0-s15 (d0-d7, q0-q3) do not have to be preserved (and can be used

29 \* for passing arguments or returning results in standard procedure-call variants).

30 \*

31 \* Registers d16-d31 (q8-q15), do not have to be preserved.

32 \*/

33struct \_\_fpu\_sf {

34 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) s[16]; /\* s0~s15 (d0-d7) \*/

35#ifdef CONFIG\_VFP\_FEATURE\_REGS\_S64\_D32

36 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)[16]; /\* d16~d31 \*/

37#endif

38 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fpscr;

39 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) undefined;

40};

41#endif

42

43/\* Additional register state that is not stacked by hardware on exception

44 \* entry.

45 \*

46 \* These fields are ONLY valid in the ESF copy passed into z\_arm\_fatal\_error().

47 \* When information for a member is unavailable, the field is set to zero.

48 \*/

49#if defined(CONFIG\_EXTRA\_EXCEPTION\_INFO)

50struct \_\_extra\_esf\_info {

51 \_callee\_saved\_t \*callee;

52 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) msp;

53 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) exc\_return;

54};

55#endif /\* CONFIG\_EXTRA\_EXCEPTION\_INFO \*/

56

57/\* ARM GPRs are often designated by two different names \*/

[ 58](arm_2cortex__a__r_2exception_8h.md#a59d42697fc33d0b600597145a7b76dc7)#define sys\_define\_gpr\_with\_alias(name1, name2) union { uint32\_t name1, name2; }

59

[ 60](structarch__esf.md)struct [arch\_esf](structarch__esf.md) {

61#if defined(CONFIG\_EXTRA\_EXCEPTION\_INFO)

62 struct \_\_extra\_esf\_info extra\_info;

63#endif

64#if defined(CONFIG\_FPU) && defined(CONFIG\_FPU\_SHARING)

[ 65](structarch__esf.md#a89304485b8d99aa30facbddf22465170) struct \_\_fpu\_sf [fpu](structarch__esf.md#a89304485b8d99aa30facbddf22465170);

66#endif

[ 67](structarch__esf_1_1____basic__sf.md) struct [\_\_basic\_sf](structarch__esf_1_1____basic__sf.md) {

[ 68](structarch__esf_1_1____basic__sf.md#acb7d6496540137f4a819b5ab6f00de46) [sys\_define\_gpr\_with\_alias](arm_2cortex__a__r_2exception_8h.md#a59d42697fc33d0b600597145a7b76dc7)([a1](structarch__esf_1_1____basic__sf.md#acb7d6496540137f4a819b5ab6f00de46), [r0](structarch__esf_1_1____basic__sf.md#ab8c428b3066806e7789bad6b7df4cbcc));

[ 69](structarch__esf_1_1____basic__sf.md#a7f8d55f8ebaa527994476d5b97ddc547) [sys\_define\_gpr\_with\_alias](arm_2cortex__a__r_2exception_8h.md#a59d42697fc33d0b600597145a7b76dc7)([a2](structarch__esf_1_1____basic__sf.md#a7f8d55f8ebaa527994476d5b97ddc547), [r1](structarch__esf_1_1____basic__sf.md#a7b75693298f528936d5f3cd3fdbd4901));

[ 70](structarch__esf_1_1____basic__sf.md#a95ac464533542cd555070834029cab59) [sys\_define\_gpr\_with\_alias](arm_2cortex__a__r_2exception_8h.md#a59d42697fc33d0b600597145a7b76dc7)([a3](structarch__esf_1_1____basic__sf.md#a95ac464533542cd555070834029cab59), [r2](structarch__esf_1_1____basic__sf.md#a7a9e40f0527189a095bc630dc125dc90));

[ 71](structarch__esf_1_1____basic__sf.md#ad4021b6b0c30cef23131abecd27dcbc0) [sys\_define\_gpr\_with\_alias](arm_2cortex__a__r_2exception_8h.md#a59d42697fc33d0b600597145a7b76dc7)([a4](structarch__esf_1_1____basic__sf.md#ad4021b6b0c30cef23131abecd27dcbc0), [r3](structarch__esf_1_1____basic__sf.md#a3cc86f158b71f5f86a90196eef244846));

[ 72](structarch__esf_1_1____basic__sf.md#ac313d550596e4c3aa41193cd5c1d5f98) [sys\_define\_gpr\_with\_alias](arm_2cortex__a__r_2exception_8h.md#a59d42697fc33d0b600597145a7b76dc7)([ip](structarch__esf_1_1____basic__sf.md#ac313d550596e4c3aa41193cd5c1d5f98), [r12](structarch__esf_1_1____basic__sf.md#aea146c77f76da4a659aa88783b509b29));

[ 73](structarch__esf_1_1____basic__sf.md#a70034ceba1064be9c6ee49db0fec6a7c) [sys\_define\_gpr\_with\_alias](arm_2cortex__a__r_2exception_8h.md#a59d42697fc33d0b600597145a7b76dc7)([lr](structarch__esf_1_1____basic__sf.md#a70034ceba1064be9c6ee49db0fec6a7c), [r14](structarch__esf_1_1____basic__sf.md#a121a9d133f2252317cb7879a5919685d));

[ 74](structarch__esf_1_1____basic__sf.md#a84e11a089563f12ab34ba613cd4d7af0) [sys\_define\_gpr\_with\_alias](arm_2cortex__a__r_2exception_8h.md#a59d42697fc33d0b600597145a7b76dc7)([pc](structarch__esf_1_1____basic__sf.md#a84e11a089563f12ab34ba613cd4d7af0), [r15](structarch__esf_1_1____basic__sf.md#aff58ca7b77f1d606bbb678071934bd9a));

[ 75](structarch__esf_1_1____basic__sf.md#a1371011f09ff1a5143f24dbd31b064a5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [xpsr](structarch__esf_1_1____basic__sf.md#a1371011f09ff1a5143f24dbd31b064a5);

[ 76](structarch__esf.md#a0b4a5972bfeab496a9a0cf0ab7821d63) } [basic](structarch__esf.md#a0b4a5972bfeab496a9a0cf0ab7821d63);

77};

78

79extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arm\_coredump\_fault\_sp;

80

81extern void z\_arm\_exc\_exit(bool [fatal](test__utils_8h.md#a0c05eeb12526a2c168109f7e5a40d833));

82

83#ifdef \_\_cplusplus

84}

85#endif

86

87#endif /\* \_ASMLANGUAGE \*/

88

89#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_EXCEPTION\_H\_ \*/

[sys\_define\_gpr\_with\_alias](arm_2cortex__a__r_2exception_8h.md#a59d42697fc33d0b600597145a7b76dc7)

#define sys\_define\_gpr\_with\_alias(name1, name2)

**Definition** exception.h:58

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[arch\_esf::\_\_basic\_sf](structarch__esf_1_1____basic__sf.md)

**Definition** exception.h:67

[arch\_esf::\_\_basic\_sf::r14](structarch__esf_1_1____basic__sf.md#a121a9d133f2252317cb7879a5919685d)

uint32\_t r14

**Definition** exception.h:73

[arch\_esf::\_\_basic\_sf::xpsr](structarch__esf_1_1____basic__sf.md#a1371011f09ff1a5143f24dbd31b064a5)

uint32\_t xpsr

**Definition** exception.h:75

[arch\_esf::\_\_basic\_sf::r3](structarch__esf_1_1____basic__sf.md#a3cc86f158b71f5f86a90196eef244846)

uint32\_t r3

**Definition** exception.h:71

[arch\_esf::\_\_basic\_sf::lr](structarch__esf_1_1____basic__sf.md#a70034ceba1064be9c6ee49db0fec6a7c)

uint32\_t lr

**Definition** exception.h:73

[arch\_esf::\_\_basic\_sf::r2](structarch__esf_1_1____basic__sf.md#a7a9e40f0527189a095bc630dc125dc90)

uint32\_t r2

**Definition** exception.h:70

[arch\_esf::\_\_basic\_sf::r1](structarch__esf_1_1____basic__sf.md#a7b75693298f528936d5f3cd3fdbd4901)

uint32\_t r1

**Definition** exception.h:69

[arch\_esf::\_\_basic\_sf::a2](structarch__esf_1_1____basic__sf.md#a7f8d55f8ebaa527994476d5b97ddc547)

uint32\_t a2

**Definition** exception.h:69

[arch\_esf::\_\_basic\_sf::pc](structarch__esf_1_1____basic__sf.md#a84e11a089563f12ab34ba613cd4d7af0)

uint32\_t pc

**Definition** exception.h:74

[arch\_esf::\_\_basic\_sf::a3](structarch__esf_1_1____basic__sf.md#a95ac464533542cd555070834029cab59)

uint32\_t a3

**Definition** exception.h:70

[arch\_esf::\_\_basic\_sf::r0](structarch__esf_1_1____basic__sf.md#ab8c428b3066806e7789bad6b7df4cbcc)

uint32\_t r0

**Definition** exception.h:68

[arch\_esf::\_\_basic\_sf::ip](structarch__esf_1_1____basic__sf.md#ac313d550596e4c3aa41193cd5c1d5f98)

uint32\_t ip

**Definition** exception.h:72

[arch\_esf::\_\_basic\_sf::a1](structarch__esf_1_1____basic__sf.md#acb7d6496540137f4a819b5ab6f00de46)

uint32\_t a1

**Definition** exception.h:68

[arch\_esf::\_\_basic\_sf::a4](structarch__esf_1_1____basic__sf.md#ad4021b6b0c30cef23131abecd27dcbc0)

uint32\_t a4

**Definition** exception.h:71

[arch\_esf::\_\_basic\_sf::r12](structarch__esf_1_1____basic__sf.md#aea146c77f76da4a659aa88783b509b29)

uint32\_t r12

**Definition** exception.h:72

[arch\_esf::\_\_basic\_sf::r15](structarch__esf_1_1____basic__sf.md#aff58ca7b77f1d606bbb678071934bd9a)

uint32\_t r15

**Definition** exception.h:74

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[arch\_esf::basic](structarch__esf.md#a0b4a5972bfeab496a9a0cf0ab7821d63)

struct arch\_esf::\_\_basic\_sf basic

[arch\_esf::fpu](structarch__esf.md#a89304485b8d99aa30facbddf22465170)

struct \_\_fpu\_sf fpu

**Definition** exception.h:65

[fatal](test__utils_8h.md#a0c05eeb12526a2c168109f7e5a40d833)

static void fatal(uint32\_t testnum, const void \*expected, size\_t expectedlen, const void \*computed, size\_t computedlen)

**Definition** test\_utils.h:50

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_a\_r](dir_cde462911e3dbfe61dba09f2df37ee97.md)
- [exception.h](arm_2cortex__a__r_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
