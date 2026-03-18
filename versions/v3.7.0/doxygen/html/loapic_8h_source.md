---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/loapic_8h_source.html
original_path: doxygen/html/loapic_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

loapic.h

[Go to the documentation of this file.](loapic_8h.md)

1/\* loapic.h - public LOAPIC APIs \*/

2

3/\*

4 \* Copyright (c) 2015 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_LOAPIC\_H\_

10#define ZEPHYR\_INCLUDE\_DRIVERS\_LOAPIC\_H\_

11

12#include <[zephyr/arch/cpu.h](cpu_8h.md)>

13#include <[zephyr/arch/x86/msr.h](msr_8h.md)>

14#include <[zephyr/sys/device\_mmio.h](device__mmio_8h.md)>

15

16/\* Local APIC Register Offset \*/

17

[ 18](loapic_8h.md#aabaee35aa87c8c7e9dbd8e4ca04ec5fa)#define LOAPIC\_ID 0x020 /\* Local APIC ID Reg \*/

[ 19](loapic_8h.md#a6865f3d12fa22ca44d37c555595f9a82)#define LOAPIC\_VER 0x030 /\* Local APIC Version Reg \*/

[ 20](loapic_8h.md#ab821cf0c98ad7eaa74e682de764f8802)#define LOAPIC\_TPR 0x080 /\* Task Priority Reg \*/

[ 21](loapic_8h.md#a22b09ea2abe05d6dc693d9891b1b10dc)#define LOAPIC\_APR 0x090 /\* Arbitration Priority Reg \*/

[ 22](loapic_8h.md#ab2ffcef005ced8514635a628ca13462f)#define LOAPIC\_PPR 0x0a0 /\* Processor Priority Reg \*/

[ 23](loapic_8h.md#a5cc8ffe88a717189312314661d489e52)#define LOAPIC\_EOI 0x0b0 /\* EOI Reg \*/

[ 24](loapic_8h.md#abc2a39fa145706f72295cd34a5e89862)#define LOAPIC\_LDR 0x0d0 /\* Logical Destination Reg \*/

[ 25](loapic_8h.md#a43f1bb7e6e9492bddfe8dd00ab789f51)#define LOAPIC\_DFR 0x0e0 /\* Destination Format Reg \*/

[ 26](loapic_8h.md#abf0572a04563cff27b01acde823b75d0)#define LOAPIC\_SVR 0x0f0 /\* Spurious Interrupt Reg \*/

[ 27](loapic_8h.md#acba6145af5fd413d8985f700b7376881)#define LOAPIC\_ISR 0x100 /\* In-service Reg \*/

[ 28](loapic_8h.md#a8c2a2d604d222ecd9d1e91ebd1793877)#define LOAPIC\_TMR 0x180 /\* Trigger Mode Reg \*/

[ 29](loapic_8h.md#a98b3ebb077835af6b185953a260ee62c)#define LOAPIC\_IRR 0x200 /\* Interrupt Request Reg \*/

[ 30](loapic_8h.md#a610671b710fafe94cc41631d8275d4b5)#define LOAPIC\_ESR 0x280 /\* Error Status Reg \*/

[ 31](loapic_8h.md#a29270aa4461ff9a94bda5ef2dd59e950)#define LOAPIC\_ICRLO 0x300 /\* Interrupt Command Reg \*/

[ 32](loapic_8h.md#a5d5cd6ba2e4ca22fc15f666e0231bc6e)#define LOAPIC\_ICRHI 0x310 /\* Interrupt Command Reg \*/

[ 33](loapic_8h.md#ad2c049f84d86360481bf39f1c769d33a)#define LOAPIC\_TIMER 0x320 /\* LVT (Timer) \*/

[ 34](loapic_8h.md#a909c6e0ee5fc88de8f444436ea3cfdac)#define LOAPIC\_THERMAL 0x330 /\* LVT (Thermal) \*/

[ 35](loapic_8h.md#a3eb80c82f8f006729add8777f99d545b)#define LOAPIC\_PMC 0x340 /\* LVT (PMC) \*/

[ 36](loapic_8h.md#a1353f571e91132ca48eec99b9de70803)#define LOAPIC\_LINT0 0x350 /\* LVT (LINT0) \*/

[ 37](loapic_8h.md#a7293b3baa5944f0f8ef80533483a8b58)#define LOAPIC\_LINT1 0x360 /\* LVT (LINT1) \*/

[ 38](loapic_8h.md#ab7911822a48695ea33abe3321623fe98)#define LOAPIC\_ERROR 0x370 /\* LVT (ERROR) \*/

[ 39](loapic_8h.md#a32f96a18492f74193e60ed7b58c66018)#define LOAPIC\_TIMER\_ICR 0x380 /\* Timer Initial Count Reg \*/

[ 40](loapic_8h.md#a33fd2d6104705d5b222d7a40133608b9)#define LOAPIC\_TIMER\_CCR 0x390 /\* Timer Current Count Reg \*/

[ 41](loapic_8h.md#a9033fab28d4760b5861984890a31589e)#define LOAPIC\_TIMER\_CONFIG 0x3e0 /\* Timer Divide Config Reg \*/

[ 42](loapic_8h.md#aeea0b064b955e73205f882cd80132455)#define LOAPIC\_SELF\_IPI 0x3f0 /\* Self IPI Reg, only support in X2APIC mode \*/

43

[ 44](loapic_8h.md#a7a95e68934f45e785ac88345d751ef00)#define LOAPIC\_ICR\_BUSY 0x00001000 /\* delivery status: 1 = busy \*/

45

[ 46](loapic_8h.md#af2037e08d1e66a8ac00b71c944bc36aa)#define LOAPIC\_ICR\_IPI\_OTHERS 0x000C4000U /\* normal IPI to other CPUs \*/

[ 47](loapic_8h.md#aeda0d6d2a4bc948dc97c1b548e0b424a)#define LOAPIC\_ICR\_IPI\_INIT 0x00004500U

[ 48](loapic_8h.md#a256c3ccf1e2dd2f7dd0f6c7006aab99c)#define LOAPIC\_ICR\_IPI\_STARTUP 0x00004600U

49

[ 50](loapic_8h.md#a4da1bd27f6148a30f40eebe70c890a4b)#define LOAPIC\_LVT\_MASKED 0x00010000 /\* mask \*/

51

52/\* Defined in intc\_loapic.c \*/

[ 53](loapic_8h.md#a83cfcf18004022e6f77a5db51a7521cc)#define LOAPIC\_REGS\_STR loapic\_regs /\* mmio device name \*/

54

55#ifndef \_ASMLANGUAGE

56

57#ifdef \_\_cplusplus

58extern "C" {

59#endif

60

[ 61](loapic_8h.md#a6fab4c5cc1444a7f69cc0ae005e6c582)[DEVICE\_MMIO\_TOPLEVEL\_DECLARE](group__device-mmio-toplevel.md#ga8a712886defe59972f4cf00bb2266f95)([LOAPIC\_REGS\_STR](loapic_8h.md#a83cfcf18004022e6f77a5db51a7521cc));

62

63[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_loapic\_irq\_base(void);

64void z\_loapic\_enable(unsigned char cpu\_number);

65void z\_loapic\_int\_vec\_set(unsigned int irq, unsigned int vector);

66void z\_loapic\_irq\_enable(unsigned int irq);

67void z\_loapic\_irq\_disable(unsigned int irq);

68

[ 74](loapic_8h.md#a797471308f74780dfcec277b18853fca)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x86\_read\_x2apic](loapic_8h.md#a797471308f74780dfcec277b18853fca)(unsigned int reg)

75{

76 reg >>= 4;

77 return z\_x86\_msr\_read([X86\_X2APIC\_BASE\_MSR](msr_8h.md#ab5ccd444077064e6b7a399ceb3d61f9f) + reg);

78}

79

[ 85](loapic_8h.md#a4807ae47f62151774877f21939fafeab)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [x86\_read\_xapic](loapic_8h.md#a4807ae47f62151774877f21939fafeab)(unsigned int reg)

86{

87 [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) base;

88 base = [DEVICE\_MMIO\_TOPLEVEL\_GET](group__device-mmio-toplevel.md#gaad7ad99277cf2be684bd70c46d358338)([LOAPIC\_REGS\_STR](loapic_8h.md#a83cfcf18004022e6f77a5db51a7521cc));

89 return [sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)(base + reg);

90}

91

[ 102](loapic_8h.md#a6ba00d305469ab62f89888cf0aa64033)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [x86\_read\_loapic](loapic_8h.md#a6ba00d305469ab62f89888cf0aa64033)(unsigned int reg)

103{

104#ifdef CONFIG\_X2APIC

105 return [x86\_read\_x2apic](loapic_8h.md#a797471308f74780dfcec277b18853fca)(reg);

106#else

107 return [x86\_read\_xapic](loapic_8h.md#a4807ae47f62151774877f21939fafeab)(reg);

108#endif

109}

110

[ 117](loapic_8h.md#a060a375336bf44c2dde9537d32f9416d)static inline void [x86\_write\_x2apic](loapic_8h.md#a060a375336bf44c2dde9537d32f9416d)(unsigned int reg, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

118{

119 reg >>= 4;

120 z\_x86\_msr\_write([X86\_X2APIC\_BASE\_MSR](msr_8h.md#ab5ccd444077064e6b7a399ceb3d61f9f) + reg, val);

121}

122

[ 129](loapic_8h.md#a9d7e889e4e4718d2205f647af172762a)static inline void [x86\_write\_xapic](loapic_8h.md#a9d7e889e4e4718d2205f647af172762a)(unsigned int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

130{

131 [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) base;

132 base = [DEVICE\_MMIO\_TOPLEVEL\_GET](group__device-mmio-toplevel.md#gaad7ad99277cf2be684bd70c46d358338)([LOAPIC\_REGS\_STR](loapic_8h.md#a83cfcf18004022e6f77a5db51a7521cc));

133 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)(val, base + reg);

134}

135

[ 147](loapic_8h.md#a884390389c9c7cef65801bba00395e4d)static inline void [x86\_write\_loapic](loapic_8h.md#a884390389c9c7cef65801bba00395e4d)(unsigned int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

148{

149#ifdef CONFIG\_X2APIC

150 [x86\_write\_x2apic](loapic_8h.md#a060a375336bf44c2dde9537d32f9416d)(reg, val);

151#else

152 [x86\_write\_xapic](loapic_8h.md#a9d7e889e4e4718d2205f647af172762a)(reg, val);

153#endif

154}

155

163static inline void z\_loapic\_ipi([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) apic\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ipi, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vector)

164{

165 ipi |= vector;

166

167#ifndef CONFIG\_X2APIC

168 /\*

169 \* Legacy xAPIC mode: first wait for any previous IPI to be delivered.

170 \*/

171

172 while ([x86\_read\_xapic](loapic_8h.md#a4807ae47f62151774877f21939fafeab)([LOAPIC\_ICRLO](loapic_8h.md#a29270aa4461ff9a94bda5ef2dd59e950)) & [LOAPIC\_ICR\_BUSY](loapic_8h.md#a7a95e68934f45e785ac88345d751ef00)) {

173 }

174

175 [x86\_write\_xapic](loapic_8h.md#a9d7e889e4e4718d2205f647af172762a)([LOAPIC\_ICRHI](loapic_8h.md#a5d5cd6ba2e4ca22fc15f666e0231bc6e), apic\_id << 24);

176 [x86\_write\_xapic](loapic_8h.md#a9d7e889e4e4718d2205f647af172762a)([LOAPIC\_ICRLO](loapic_8h.md#a29270aa4461ff9a94bda5ef2dd59e950), ipi);

177#else

178 /\*

179 \* x2APIC mode is greatly simplified: one write, no delivery status.

180 \*/

181

182 [x86\_write\_x2apic](loapic_8h.md#a060a375336bf44c2dde9537d32f9416d)([LOAPIC\_ICRLO](loapic_8h.md#a29270aa4461ff9a94bda5ef2dd59e950), ((([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)) apic\_id) << 32) | ipi);

183#endif

184}

185

186#ifdef \_\_cplusplus

187}

188#endif

189

190#endif /\* \_ASMLANGUAGE \*/

191

192#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LOAPIC\_H\_ \*/

[cpu.h](cpu_8h.md)

[device\_mmio.h](device__mmio_8h.md)

[DEVICE\_MMIO\_TOPLEVEL\_DECLARE](group__device-mmio-toplevel.md#ga8a712886defe59972f4cf00bb2266f95)

#define DEVICE\_MMIO\_TOPLEVEL\_DECLARE(name)

Provide an extern reference to a top-level MMIO region.

**Definition** device\_mmio.h:638

[DEVICE\_MMIO\_TOPLEVEL\_GET](group__device-mmio-toplevel.md#gaad7ad99277cf2be684bd70c46d358338)

#define DEVICE\_MMIO\_TOPLEVEL\_GET(name)

Obtain the MMIO address for a device declared top-level.

**Definition** device\_mmio.h:734

[x86\_write\_x2apic](loapic_8h.md#a060a375336bf44c2dde9537d32f9416d)

static void x86\_write\_x2apic(unsigned int reg, uint64\_t val)

Write 64-bit value to the local APIC in x2APIC mode.

**Definition** loapic.h:117

[LOAPIC\_ICRLO](loapic_8h.md#a29270aa4461ff9a94bda5ef2dd59e950)

#define LOAPIC\_ICRLO

**Definition** loapic.h:31

[x86\_read\_xapic](loapic_8h.md#a4807ae47f62151774877f21939fafeab)

static uint32\_t x86\_read\_xapic(unsigned int reg)

Read 32-bit value from the local APIC in xAPIC (MMIO) mode.

**Definition** loapic.h:85

[LOAPIC\_ICRHI](loapic_8h.md#a5d5cd6ba2e4ca22fc15f666e0231bc6e)

#define LOAPIC\_ICRHI

**Definition** loapic.h:32

[x86\_read\_loapic](loapic_8h.md#a6ba00d305469ab62f89888cf0aa64033)

static uint32\_t x86\_read\_loapic(unsigned int reg)

Read value from the local APIC using the default mode.

**Definition** loapic.h:102

[x86\_read\_x2apic](loapic_8h.md#a797471308f74780dfcec277b18853fca)

static uint64\_t x86\_read\_x2apic(unsigned int reg)

Read 64-bit value from the local APIC in x2APIC mode.

**Definition** loapic.h:74

[LOAPIC\_ICR\_BUSY](loapic_8h.md#a7a95e68934f45e785ac88345d751ef00)

#define LOAPIC\_ICR\_BUSY

**Definition** loapic.h:44

[LOAPIC\_REGS\_STR](loapic_8h.md#a83cfcf18004022e6f77a5db51a7521cc)

#define LOAPIC\_REGS\_STR

**Definition** loapic.h:53

[x86\_write\_loapic](loapic_8h.md#a884390389c9c7cef65801bba00395e4d)

static void x86\_write\_loapic(unsigned int reg, uint32\_t val)

Write 32-bit value to the local APIC using the default mode.

**Definition** loapic.h:147

[x86\_write\_xapic](loapic_8h.md#a9d7e889e4e4718d2205f647af172762a)

static void x86\_write\_xapic(unsigned int reg, uint32\_t val)

Write 32-bit value to the local APIC in xAPIC (MMIO) mode.

**Definition** loapic.h:129

[msr.h](msr_8h.md)

[X86\_X2APIC\_BASE\_MSR](msr_8h.md#ab5ccd444077064e6b7a399ceb3d61f9f)

#define X86\_X2APIC\_BASE\_MSR

**Definition** msr.h:25

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)

static ALWAYS\_INLINE void sys\_write32(uint32\_t data, mem\_addr\_t addr)

**Definition** sys-io-common.h:70

[sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)

static ALWAYS\_INLINE uint32\_t sys\_read32(mem\_addr\_t addr)

**Definition** sys-io-common.h:59

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [loapic.h](loapic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
