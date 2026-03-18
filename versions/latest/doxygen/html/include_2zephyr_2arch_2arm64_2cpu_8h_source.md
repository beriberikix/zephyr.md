---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/include_2zephyr_2arch_2arm64_2cpu_8h_source.html
original_path: doxygen/html/include_2zephyr_2arch_2arm64_2cpu_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpu.h

[Go to the documentation of this file.](include_2zephyr_2arch_2arm64_2cpu_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_CPU\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_CPU\_H\_

9

10#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

11#include <[stdbool.h](stdbool_8h.md)>

12

[ 13](include_2zephyr_2arch_2arm64_2cpu_8h.md#a53fb1a3ffce153d445525392fb411687)#define DAIFSET\_FIQ\_BIT BIT(0)

[ 14](include_2zephyr_2arch_2arm64_2cpu_8h.md#a22d4cee27b78fddece088591958ca037)#define DAIFSET\_IRQ\_BIT BIT(1)

[ 15](include_2zephyr_2arch_2arm64_2cpu_8h.md#a4a9605b3286e62a9d878c7cfdccbf6f6)#define DAIFSET\_ABT\_BIT BIT(2)

[ 16](include_2zephyr_2arch_2arm64_2cpu_8h.md#ae8f3edaddcaaf22a1155da424838b326)#define DAIFSET\_DBG\_BIT BIT(3)

17

[ 18](include_2zephyr_2arch_2arm64_2cpu_8h.md#abf5cf8b639767836af6967f6d07e07b3)#define DAIFCLR\_FIQ\_BIT BIT(0)

[ 19](include_2zephyr_2arch_2arm64_2cpu_8h.md#a6f6ae405bbde72ffef083bca9448269b)#define DAIFCLR\_IRQ\_BIT BIT(1)

[ 20](include_2zephyr_2arch_2arm64_2cpu_8h.md#a21a0f602ba0c8b87cc082e3e13aa5d98)#define DAIFCLR\_ABT\_BIT BIT(2)

[ 21](include_2zephyr_2arch_2arm64_2cpu_8h.md#afb4bae58d424e6460802949ef0355d21)#define DAIFCLR\_DBG\_BIT BIT(3)

22

[ 23](include_2zephyr_2arch_2arm64_2cpu_8h.md#a5e04c9f2838f5bb1741bffa1444c299e)#define DAIF\_FIQ\_BIT BIT(6)

[ 24](include_2zephyr_2arch_2arm64_2cpu_8h.md#ad4a89cfde4c1112886aaa11b1004e2db)#define DAIF\_IRQ\_BIT BIT(7)

[ 25](include_2zephyr_2arch_2arm64_2cpu_8h.md#a6a85c27138f0c3925e1c51e9d6768cfd)#define DAIF\_ABT\_BIT BIT(8)

[ 26](include_2zephyr_2arch_2arm64_2cpu_8h.md#a3293a3a9e486e835a22439820cffb06d)#define DAIF\_DBG\_BIT BIT(9)

27

[ 28](include_2zephyr_2arch_2arm64_2cpu_8h.md#a193071e5757a40fc372e0d1ab10f280f)#define SPSR\_DAIF\_SHIFT (6)

[ 29](include_2zephyr_2arch_2arm64_2cpu_8h.md#af5444cb52ad93024bf6bfd6487a9de46)#define SPSR\_DAIF\_MASK (0xf << SPSR\_DAIF\_SHIFT)

30

[ 31](include_2zephyr_2arch_2arm64_2cpu_8h.md#a5ac2f987d02999da93878c4b7b6a39ce)#define SPSR\_MODE\_EL0T (0x0)

[ 32](include_2zephyr_2arch_2arm64_2cpu_8h.md#a440d11721e78f76bd7022cc8aef83aca)#define SPSR\_MODE\_EL1T (0x4)

[ 33](include_2zephyr_2arch_2arm64_2cpu_8h.md#afb0eeebb254ef2cd71960f9e77af181e)#define SPSR\_MODE\_EL1H (0x5)

[ 34](include_2zephyr_2arch_2arm64_2cpu_8h.md#a5c065c9fe9bbeefc64dcdda2f6c4b5bd)#define SPSR\_MODE\_EL2T (0x8)

[ 35](include_2zephyr_2arch_2arm64_2cpu_8h.md#a3ad33c29d57e86dc7f416a6bf267d257)#define SPSR\_MODE\_EL2H (0x9)

[ 36](include_2zephyr_2arch_2arm64_2cpu_8h.md#ad42eefed5f9728f8dd454d2fad321ae3)#define SPSR\_MODE\_MASK (0xf)

37

38

[ 39](include_2zephyr_2arch_2arm64_2cpu_8h.md#aa5f1069250ab50a42e788f8eb655e0a7)#define SCTLR\_EL3\_RES1 (BIT(29) | BIT(28) | BIT(23) | \

40 BIT(22) | BIT(18) | BIT(16) | \

41 BIT(11) | BIT(5) | BIT(4))

42

[ 43](include_2zephyr_2arch_2arm64_2cpu_8h.md#acee5ccd8b0a2f885465442ef777c964a)#define SCTLR\_EL2\_RES1 (BIT(29) | BIT(28) | BIT(23) | \

44 BIT(22) | BIT(18) | BIT(16) | \

45 BIT(11) | BIT(5) | BIT(4))

46

[ 47](include_2zephyr_2arch_2arm64_2cpu_8h.md#ac53a7152c26719a8bb4d9cafdfca2045)#define SCTLR\_EL1\_RES1 (BIT(29) | BIT(28) | BIT(23) | \

48 BIT(22) | BIT(20) | BIT(11))

49

[ 50](include_2zephyr_2arch_2arm64_2cpu_8h.md#a223e38830566f400f6d592a6bb7dd361)#define SCTLR\_M\_BIT BIT(0)

[ 51](include_2zephyr_2arch_2arm64_2cpu_8h.md#ad9dc6fc20549b11dc1b2cc5ed02d5ee7)#define SCTLR\_A\_BIT BIT(1)

[ 52](include_2zephyr_2arch_2arm64_2cpu_8h.md#a752ac38bb53a96c6749fbfc09a1fb88d)#define SCTLR\_C\_BIT BIT(2)

[ 53](include_2zephyr_2arch_2arm64_2cpu_8h.md#a7a33d6c6dc85bc5aef0aebafa1f2f223)#define SCTLR\_SA\_BIT BIT(3)

[ 54](include_2zephyr_2arch_2arm64_2cpu_8h.md#ac9fd86e6613531ab567031f4c02a2900)#define SCTLR\_I\_BIT BIT(12)

[ 55](include_2zephyr_2arch_2arm64_2cpu_8h.md#a6bbbc667734e9749f0cbb63cc3ff4341)#define SCTLR\_BR\_BIT BIT(17)

56

[ 57](include_2zephyr_2arch_2arm64_2cpu_8h.md#a93a25e810ffc65f91f94c8ed389b4138)#define CPACR\_EL1\_FPEN\_NOTRAP (0x3 << 20)

58

[ 59](include_2zephyr_2arch_2arm64_2cpu_8h.md#a3356501dba79206460819c2b99617a8e)#define SCR\_NS\_BIT BIT(0)

[ 60](include_2zephyr_2arch_2arm64_2cpu_8h.md#aae3302d2a8466a2b9a771721548e5263)#define SCR\_IRQ\_BIT BIT(1)

[ 61](include_2zephyr_2arch_2arm64_2cpu_8h.md#a819b23e7868c4662bd4b3d19fa6eed5d)#define SCR\_FIQ\_BIT BIT(2)

[ 62](include_2zephyr_2arch_2arm64_2cpu_8h.md#ae86fa2091d1dbac36137aa064eee7d4e)#define SCR\_EA\_BIT BIT(3)

[ 63](include_2zephyr_2arch_2arm64_2cpu_8h.md#a7c0a0c7d1d0865d4454b88f4ae14f45f)#define SCR\_SMD\_BIT BIT(7)

[ 64](include_2zephyr_2arch_2arm64_2cpu_8h.md#a547675dd8352ffb1fcfb6dec5914225a)#define SCR\_HCE\_BIT BIT(8)

[ 65](include_2zephyr_2arch_2arm64_2cpu_8h.md#a1ab9bded034ce4f46ead5d01b59674be)#define SCR\_RW\_BIT BIT(10)

[ 66](include_2zephyr_2arch_2arm64_2cpu_8h.md#a9497ad7be55a9e2afcd3033d2c2e6d03)#define SCR\_ST\_BIT BIT(11)

[ 67](include_2zephyr_2arch_2arm64_2cpu_8h.md#ad912faedaeee2519ec8207ed2d0a4704)#define SCR\_EEL2\_BIT BIT(18)

68

[ 69](include_2zephyr_2arch_2arm64_2cpu_8h.md#a4596599ea8aa7c7d7be74cb60319535d)#define SCR\_RES1 (BIT(4) | BIT(5))

70

71/\* MPIDR \*/

[ 72](include_2zephyr_2arch_2arm64_2cpu_8h.md#a9bce40a5c0fceea5298a899b174c3e1c)#define MPIDR\_AFFLVL\_MASK (0xffULL)

73

[ 74](include_2zephyr_2arch_2arm64_2cpu_8h.md#a7a2087ca83455cf2759a5aee220105e2)#define MPIDR\_AFF0\_SHIFT (0)

[ 75](include_2zephyr_2arch_2arm64_2cpu_8h.md#a3a7ffd9f7a014257a725513d531edab2)#define MPIDR\_AFF1\_SHIFT (8)

[ 76](include_2zephyr_2arch_2arm64_2cpu_8h.md#a61d65102667e48cb00b7f9133dcd60f2)#define MPIDR\_AFF2\_SHIFT (16)

[ 77](include_2zephyr_2arch_2arm64_2cpu_8h.md#adcd8397ffe05b55aec4ae2505879eed5)#define MPIDR\_AFF3\_SHIFT (32)

78

[ 79](include_2zephyr_2arch_2arm64_2cpu_8h.md#aa64dd15e6bcb1b034ccadf54f358f02d)#define MPIDR\_AFF\_MASK (GENMASK(23, 0) | GENMASK(39, 32))

80

[ 81](include_2zephyr_2arch_2arm64_2cpu_8h.md#a35278aa57b0b98cd0cb541cfea58b177)#define MPIDR\_AFFLVL(mpidr, aff\_level) \

82 (((mpidr) >> MPIDR\_AFF##aff\_level##\_SHIFT) & MPIDR\_AFFLVL\_MASK)

83

[ 84](include_2zephyr_2arch_2arm64_2cpu_8h.md#a958d9c5f047f5dc318ecf4b171a68949)#define GET\_MPIDR() read\_sysreg(mpidr\_el1)

[ 85](include_2zephyr_2arch_2arm64_2cpu_8h.md#a850e9ad6314a72da4ef5ff09d5e1e024)#define MPIDR\_TO\_CORE(mpidr) (mpidr & MPIDR\_AFF\_MASK)

86

[ 87](include_2zephyr_2arch_2arm64_2cpu_8h.md#a22ce702a54ad18a7b76edb2fb665f8fd)#define MODE\_EL\_SHIFT (0x2)

[ 88](include_2zephyr_2arch_2arm64_2cpu_8h.md#af57f4ebf8044288140b76f1063de6d6d)#define MODE\_EL\_MASK (0x3)

89

[ 90](include_2zephyr_2arch_2arm64_2cpu_8h.md#ad51a9827564f8457d36f167593de7b83)#define MODE\_EL3 (0x3)

[ 91](include_2zephyr_2arch_2arm64_2cpu_8h.md#a8c3515664794ffdcd08191f5c48c3ed0)#define MODE\_EL2 (0x2)

[ 92](include_2zephyr_2arch_2arm64_2cpu_8h.md#ad3372878ec0c895ae1c791b0ef2d24c0)#define MODE\_EL1 (0x1)

[ 93](include_2zephyr_2arch_2arm64_2cpu_8h.md#affee69f2502d7e1b743d1fc79dd78c1d)#define MODE\_EL0 (0x0)

94

[ 95](include_2zephyr_2arch_2arm64_2cpu_8h.md#a16a04b233cad3fb65cb16dbeff32f8f2)#define GET\_EL(\_mode) (((\_mode) >> MODE\_EL\_SHIFT) & MODE\_EL\_MASK)

96

[ 97](include_2zephyr_2arch_2arm64_2cpu_8h.md#a6b4d7e44bdb5912494cb830ba3e09641)#define ESR\_EC\_SHIFT (26)

[ 98](include_2zephyr_2arch_2arm64_2cpu_8h.md#a423881002388f48bd9c18ee87d4186ef)#define ESR\_EC\_MASK BIT\_MASK(6)

[ 99](include_2zephyr_2arch_2arm64_2cpu_8h.md#a18f0cf88a43e06fd81ed66905c039add)#define ESR\_ISS\_SHIFT (0)

[ 100](include_2zephyr_2arch_2arm64_2cpu_8h.md#a011b740985880817c10c3bee7bdb3af8)#define ESR\_ISS\_MASK BIT\_MASK(25)

[ 101](include_2zephyr_2arch_2arm64_2cpu_8h.md#a8b063b9a94bd5e3a0a52d60be5875637)#define ESR\_IL\_SHIFT (25)

[ 102](include_2zephyr_2arch_2arm64_2cpu_8h.md#a705fbfa04a5eb82c44d0a6dc3db9c43c)#define ESR\_IL\_MASK BIT\_MASK(1)

103

[ 104](include_2zephyr_2arch_2arm64_2cpu_8h.md#a25719cf4bed7192f43a897085dae1dc1)#define GET\_ESR\_EC(esr) (((esr) >> ESR\_EC\_SHIFT) & ESR\_EC\_MASK)

[ 105](include_2zephyr_2arch_2arm64_2cpu_8h.md#a93440f95cef11bffbbcec8a8bea3eb21)#define GET\_ESR\_IL(esr) (((esr) >> ESR\_IL\_SHIFT) & ESR\_IL\_MASK)

[ 106](include_2zephyr_2arch_2arm64_2cpu_8h.md#a2dc6b6b21a499764da19b26839bbc2b5)#define GET\_ESR\_ISS(esr) (((esr) >> ESR\_ISS\_SHIFT) & ESR\_ISS\_MASK)

107

[ 108](include_2zephyr_2arch_2arm64_2cpu_8h.md#a0001886233fa8459922ad8338eba1dc8)#define CNTV\_CTL\_ENABLE\_BIT BIT(0)

[ 109](include_2zephyr_2arch_2arm64_2cpu_8h.md#a382fbb7831e299acfd89e9f03c08aebb)#define CNTV\_CTL\_IMASK\_BIT BIT(1)

110

[ 111](include_2zephyr_2arch_2arm64_2cpu_8h.md#aacb0fe06a7e7a04c95ce845448c6d436)#define ID\_AA64PFR0\_EL0\_SHIFT (0)

[ 112](include_2zephyr_2arch_2arm64_2cpu_8h.md#a9add6e194aac9e74e71c2dc2dd025eb7)#define ID\_AA64PFR0\_EL1\_SHIFT (4)

[ 113](include_2zephyr_2arch_2arm64_2cpu_8h.md#a22dea24f7bdc4ae44c39f5aa4bcc5615)#define ID\_AA64PFR0\_EL2\_SHIFT (8)

[ 114](include_2zephyr_2arch_2arm64_2cpu_8h.md#a77322f61c0e4e872809b46b769e2ec51)#define ID\_AA64PFR0\_EL3\_SHIFT (12)

[ 115](include_2zephyr_2arch_2arm64_2cpu_8h.md#ad296dae475a3598559cb5f53d74a62b0)#define ID\_AA64PFR0\_ELX\_MASK (0xf)

[ 116](include_2zephyr_2arch_2arm64_2cpu_8h.md#a7ebf5636fdc14822cb8bbe10c7f2e1b4)#define ID\_AA64PFR0\_SEL2\_SHIFT (36)

[ 117](include_2zephyr_2arch_2arm64_2cpu_8h.md#a233d4971a3bcb773cfe17e4dbe0ee750)#define ID\_AA64PFR0\_SEL2\_MASK (0xf)

118

119/\*

120 \* TODO: ACTLR is of class implementation defined. All core implementations

121 \* in armv8a have the same implementation so far w.r.t few controls.

122 \* When there will be differences we have to create core specific headers.

123 \*/

[ 124](include_2zephyr_2arch_2arm64_2cpu_8h.md#ac50b16ec53bcc4bdf8e7aef09cb335bf)#define ACTLR\_EL3\_CPUACTLR\_BIT BIT(0)

[ 125](include_2zephyr_2arch_2arm64_2cpu_8h.md#a685f4f4eaee539caa215a539c7f14c74)#define ACTLR\_EL3\_CPUECTLR\_BIT BIT(1)

[ 126](include_2zephyr_2arch_2arm64_2cpu_8h.md#a7be92abd63f3a3915495f497460bc89b)#define ACTLR\_EL3\_L2CTLR\_BIT BIT(4)

[ 127](include_2zephyr_2arch_2arm64_2cpu_8h.md#a73da30b946e047bf4b736deb26270571)#define ACTLR\_EL3\_L2ECTLR\_BIT BIT(5)

[ 128](include_2zephyr_2arch_2arm64_2cpu_8h.md#ae1d807d116307b1321d75ed0917f912d)#define ACTLR\_EL3\_L2ACTLR\_BIT BIT(6)

129

[ 130](include_2zephyr_2arch_2arm64_2cpu_8h.md#aff636f95d6e6c2eb2e2c447606c7504f)#define CPTR\_EZ\_BIT BIT(8)

[ 131](include_2zephyr_2arch_2arm64_2cpu_8h.md#ab772d9f0f8054ae06af80cc85b956dc7)#define CPTR\_TFP\_BIT BIT(10)

[ 132](include_2zephyr_2arch_2arm64_2cpu_8h.md#a5935d340bf480b94c8268209d8528530)#define CPTR\_TTA\_BIT BIT(20)

[ 133](include_2zephyr_2arch_2arm64_2cpu_8h.md#af3ee0801abd2c3c7aff03daad16222ea)#define CPTR\_TCPAC\_BIT BIT(31)

134

[ 135](include_2zephyr_2arch_2arm64_2cpu_8h.md#a671504449ea674af44e47995678f0a5b)#define CPTR\_EL2\_RES1 BIT(13) | BIT(12) | BIT(9) | (0xff)

136

[ 137](include_2zephyr_2arch_2arm64_2cpu_8h.md#a223d70f2acad7d361ee6fb7b44bdb2e5)#define HCR\_FMO\_BIT BIT(3)

[ 138](include_2zephyr_2arch_2arm64_2cpu_8h.md#a1792be817d3129a78d60d8bf0d1e5689)#define HCR\_IMO\_BIT BIT(4)

[ 139](include_2zephyr_2arch_2arm64_2cpu_8h.md#ad67b4ccd0f2888823525fcc71ea76419)#define HCR\_AMO\_BIT BIT(5)

[ 140](include_2zephyr_2arch_2arm64_2cpu_8h.md#a5d2f11fc2059239829db563c8a2bbafe)#define HCR\_TGE\_BIT BIT(27)

[ 141](include_2zephyr_2arch_2arm64_2cpu_8h.md#a2ecb1fa994da111656e57828a2fb5015)#define HCR\_RW\_BIT BIT(31)

142

143/\* System register interface to GICv3 \*/

[ 144](include_2zephyr_2arch_2arm64_2cpu_8h.md#aeb7f0f2d77b8c2015a23e12982e35a01)#define ICC\_IGRPEN1\_EL1 S3\_0\_C12\_C12\_7

[ 145](include_2zephyr_2arch_2arm64_2cpu_8h.md#ae36e32afe169a9173e3294a807af3234)#define ICC\_SGI1R S3\_0\_C12\_C11\_5

[ 146](include_2zephyr_2arch_2arm64_2cpu_8h.md#a178411409386d40d5927250161b2c3d3)#define ICC\_SRE\_EL1 S3\_0\_C12\_C12\_5

[ 147](include_2zephyr_2arch_2arm64_2cpu_8h.md#a57664b4d9a0768fd26e0f9e79271d775)#define ICC\_SRE\_EL2 S3\_4\_C12\_C9\_5

[ 148](include_2zephyr_2arch_2arm64_2cpu_8h.md#a2aae8716b04b563cfabdeb549ec76b11)#define ICC\_SRE\_EL3 S3\_6\_C12\_C12\_5

[ 149](include_2zephyr_2arch_2arm64_2cpu_8h.md#a24b75fc3f9337d1a0fa0570b5e9a5681)#define ICC\_CTLR\_EL1 S3\_0\_C12\_C12\_4

[ 150](include_2zephyr_2arch_2arm64_2cpu_8h.md#ae4ef3359d57cb8862bd140ed52a169a2)#define ICC\_CTLR\_EL3 S3\_6\_C12\_C12\_4

[ 151](include_2zephyr_2arch_2arm64_2cpu_8h.md#a569e3c45407957f8e9b6786441dd1954)#define ICC\_PMR\_EL1 S3\_0\_C4\_C6\_0

[ 152](include_2zephyr_2arch_2arm64_2cpu_8h.md#ac6b780289029a1bfa5f1597272e92087)#define ICC\_RPR\_EL1 S3\_0\_C12\_C11\_3

[ 153](include_2zephyr_2arch_2arm64_2cpu_8h.md#a75ffb5b6ea7d3a96e5d9efae9969773d)#define ICC\_IGRPEN1\_EL3 S3\_6\_C12\_C12\_7

[ 154](include_2zephyr_2arch_2arm64_2cpu_8h.md#ae1e035983563d473d79be122004f6d4a)#define ICC\_IGRPEN0\_EL1 S3\_0\_C12\_C12\_6

[ 155](include_2zephyr_2arch_2arm64_2cpu_8h.md#a1537602c3ecea4f1ce6488a94403ca17)#define ICC\_HPPIR0\_EL1 S3\_0\_C12\_C8\_2

[ 156](include_2zephyr_2arch_2arm64_2cpu_8h.md#a5c52945c05fec71d2879ac109a6367db)#define ICC\_HPPIR1\_EL1 S3\_0\_C12\_C12\_2

[ 157](include_2zephyr_2arch_2arm64_2cpu_8h.md#ab617bac1549d87e76f6aa4f7bccb484a)#define ICC\_IAR0\_EL1 S3\_0\_C12\_C8\_0

[ 158](include_2zephyr_2arch_2arm64_2cpu_8h.md#a35f0be43473c740c83e32af88e2d0625)#define ICC\_IAR1\_EL1 S3\_0\_C12\_C12\_0

[ 159](include_2zephyr_2arch_2arm64_2cpu_8h.md#af3c07fa13d6f7c298954276bd7e162ba)#define ICC\_EOIR0\_EL1 S3\_0\_C12\_C8\_1

[ 160](include_2zephyr_2arch_2arm64_2cpu_8h.md#a5dbe3c5dfb9ff381fac5c1a004116592)#define ICC\_EOIR1\_EL1 S3\_0\_C12\_C12\_1

[ 161](include_2zephyr_2arch_2arm64_2cpu_8h.md#a6a15fbfb9c3de076e12f6dedc1c8736b)#define ICC\_SGI0R\_EL1 S3\_0\_C12\_C11\_7

162

163/\* register constants \*/

[ 164](include_2zephyr_2arch_2arm64_2cpu_8h.md#a581240d06f8f27d299a303941934d0a9)#define ICC\_SRE\_ELx\_SRE\_BIT BIT(0)

[ 165](include_2zephyr_2arch_2arm64_2cpu_8h.md#a54ea5ad3d9d0c66c5787b4c10feaeffb)#define ICC\_SRE\_ELx\_DFB\_BIT BIT(1)

[ 166](include_2zephyr_2arch_2arm64_2cpu_8h.md#a6464acd03121adf32b11764b8e16a59f)#define ICC\_SRE\_ELx\_DIB\_BIT BIT(2)

[ 167](include_2zephyr_2arch_2arm64_2cpu_8h.md#a89642941ffefc853013b0f92cc80f131)#define ICC\_SRE\_EL3\_EN\_BIT BIT(3)

168

169/\* ICC SGI macros \*/

[ 170](include_2zephyr_2arch_2arm64_2cpu_8h.md#aef12617a687736364283ba5fc45eb29a)#define SGIR\_TGT\_MASK (0xffff)

[ 171](include_2zephyr_2arch_2arm64_2cpu_8h.md#a54fd53204f64c9081d7c0c9fc3209c37)#define SGIR\_AFF1\_SHIFT (16)

[ 172](include_2zephyr_2arch_2arm64_2cpu_8h.md#afcb9746b2d5edfd88af4af2759c931d7)#define SGIR\_AFF2\_SHIFT (32)

[ 173](include_2zephyr_2arch_2arm64_2cpu_8h.md#ac4364d68d92dd7b7e1bb7ffac6e81eef)#define SGIR\_AFF3\_SHIFT (48)

[ 174](include_2zephyr_2arch_2arm64_2cpu_8h.md#aaebf9f7f5e67965fac91a7eb0336f3e4)#define SGIR\_AFF\_MASK (0xf)

[ 175](include_2zephyr_2arch_2arm64_2cpu_8h.md#a9bd0096ceb2f20d31173b61127dc5bd3)#define SGIR\_INTID\_SHIFT (24)

[ 176](include_2zephyr_2arch_2arm64_2cpu_8h.md#a6e5a1e0b98322addaa87188e4d9a03f1)#define SGIR\_INTID\_MASK (0xf)

[ 177](include_2zephyr_2arch_2arm64_2cpu_8h.md#a0a9ae05724f25a9f9e55e664823eeb6b)#define SGIR\_IRM\_SHIFT (40)

[ 178](include_2zephyr_2arch_2arm64_2cpu_8h.md#a31c2a71ebf8c2e296f0c8417012ca7f4)#define SGIR\_IRM\_MASK (0x1)

[ 179](include_2zephyr_2arch_2arm64_2cpu_8h.md#a410f4b9c7089a847d01bc6592335871f)#define SGIR\_IRM\_TO\_AFF (0)

180

[ 181](include_2zephyr_2arch_2arm64_2cpu_8h.md#a2df77921af208fb2202cb6d03a9ea004)#define GICV3\_SGIR\_VALUE(\_aff3, \_aff2, \_aff1, \_intid, \_irm, \_tgt) \

182 ((((uint64\_t) (\_aff3) & SGIR\_AFF\_MASK) << SGIR\_AFF3\_SHIFT) | \

183 (((uint64\_t) (\_irm) & SGIR\_IRM\_MASK) << SGIR\_IRM\_SHIFT) | \

184 (((uint64\_t) (\_aff2) & SGIR\_AFF\_MASK) << SGIR\_AFF2\_SHIFT) | \

185 (((\_intid) & SGIR\_INTID\_MASK) << SGIR\_INTID\_SHIFT) | \

186 (((\_aff1) & SGIR\_AFF\_MASK) << SGIR\_AFF1\_SHIFT) | \

187 ((\_tgt) & SGIR\_TGT\_MASK))

188

189/\* Implementation defined register definitions \*/

190#if defined(CONFIG\_CPU\_CORTEX\_A72)

191

192#define CORTEX\_A72\_L2CTLR\_EL1 S3\_1\_C11\_C0\_2

193#define CORTEX\_A72\_L2CTLR\_DATA\_RAM\_LATENCY\_SHIFT (0)

194#define CORTEX\_A72\_L2CTLR\_DATA\_RAM\_SETUP\_SHIFT (5)

195#define CORTEX\_A72\_L2CTLR\_TAG\_RAM\_LATENCY\_SHIFT (6)

196#define CORTEX\_A72\_L2CTLR\_TAG\_RAM\_SETUP\_SHIFT (9)

197

198#define CORTEX\_A72\_L2\_DATA\_RAM\_LATENCY\_3\_CYCLES (2)

199#define CORTEX\_A72\_L2\_DATA\_RAM\_LATENCY\_MASK (0x7)

200#define CORTEX\_A72\_L2\_DATA\_RAM\_SETUP\_1\_CYCLE (1)

201#define CORTEX\_A72\_L2\_TAG\_RAM\_LATENCY\_2\_CYCLES (1)

202#define CORTEX\_A72\_L2\_TAG\_RAM\_LATENCY\_3\_CYCLES (2)

203#define CORTEX\_A72\_L2\_TAG\_RAM\_LATENCY\_MASK (0x7)

204#define CORTEX\_A72\_L2\_TAG\_RAM\_SETUP\_1\_CYCLE (1)

205

206#define CORTEX\_A72\_L2ACTLR\_EL1 S3\_1\_C15\_C0\_0

207#define CORTEX\_A72\_L2ACTLR\_DISABLE\_ACE\_SH\_OR\_CHI\_BIT BIT(6)

208

209#endif /\* CONFIG\_CPU\_CORTEX\_A72 \*/

210

[ 211](include_2zephyr_2arch_2arm64_2cpu_8h.md#a29cd99f347d3f9cfccf2ea01d64b2117)#define L1\_CACHE\_SHIFT (6)

[ 212](include_2zephyr_2arch_2arm64_2cpu_8h.md#a9400cc2ba37e33279bdbc510a6311fb4)#define L1\_CACHE\_BYTES BIT(L1\_CACHE\_SHIFT)

[ 213](include_2zephyr_2arch_2arm64_2cpu_8h.md#ab5541d63dd4db4182ab1da587f29189a)#define ARM64\_CPU\_INIT\_SIZE L1\_CACHE\_BYTES

214

215#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_CPU\_H\_ \*/

[stdbool.h](stdbool_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [cpu.h](include_2zephyr_2arch_2arm64_2cpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
