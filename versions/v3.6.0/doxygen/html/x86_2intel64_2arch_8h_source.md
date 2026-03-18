---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/x86_2intel64_2arch_8h_source.html
original_path: doxygen/html/x86_2intel64_2arch_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](x86_2intel64_2arch_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corp.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_ARCH\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_ARCH\_H\_

8

9#include <[zephyr/arch/x86/intel64/thread.h](arch_2x86_2intel64_2thread_8h.md)>

10#include <[zephyr/arch/x86/thread\_stack.h](arch_2x86_2thread__stack_8h.md)>

11#if defined(CONFIG\_PCIE) && !defined(\_ASMLANGUAGE)

12#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

13#endif

14

15#if CONFIG\_ISR\_STACK\_SIZE != (CONFIG\_ISR\_SUBSTACK\_SIZE \* CONFIG\_ISR\_DEPTH)

16#error "Check ISR stack configuration (CONFIG\_ISR\_\*)"

17#endif

18

19#if CONFIG\_ISR\_SUBSTACK\_SIZE % ARCH\_STACK\_PTR\_ALIGN

20#error "CONFIG\_ISR\_SUBSTACK\_SIZE must be a multiple of 16"

21#endif

22

23#ifndef \_ASMLANGUAGE

24

[ 25](x86_2intel64_2arch_8h.md#aed9cf591fb95242f161e6fc8719cf3e3)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write64](x86_2intel64_2arch_8h.md#aed9cf591fb95242f161e6fc8719cf3e3)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

26{

27 \_\_asm\_\_ volatile("movq %0, %1"

28 :

29 : "r"(data), "m" (\*(volatile [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*)

30 ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

31 : "memory");

32}

33

[ 34](x86_2intel64_2arch_8h.md#a7ba6099642d909c50219d174c35f6a94)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_read64](x86_2intel64_2arch_8h.md#a7ba6099642d909c50219d174c35f6a94)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

35{

36 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ret;

37

38 \_\_asm\_\_ volatile("movq %1, %0"

39 : "=r"(ret)

40 : "m" (\*(volatile [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

41 : "memory");

42

43 return ret;

44}

45

[ 46](x86_2intel64_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

47{

48 unsigned long key;

49

50 \_\_asm\_\_ volatile ("pushfq; cli; popq %0" : "=g" (key) : : "memory");

51

52 return (unsigned int) key;

53}

54

55/\*

56 \* the exception stack frame

57 \*/

58

[ 59](structx86__esf.md)struct [x86\_esf](structx86__esf.md) {

60#ifdef CONFIG\_EXCEPTION\_DEBUG

61 /\* callee-saved \*/

62 unsigned long rbx;

63 unsigned long r12;

64 unsigned long r13;

65 unsigned long r14;

66 unsigned long r15;

67#endif /\* CONFIG\_EXCEPTION\_DEBUG \*/

[ 68](structx86__esf.md#a4bb58040b5089732faab5d191d5a557c) unsigned long [rbp](structx86__esf.md#a4bb58040b5089732faab5d191d5a557c);

69

70 /\* Caller-saved regs \*/

[ 71](structx86__esf.md#adb1487de787c2a8890391e9fdf86d9f0) unsigned long [rax](structx86__esf.md#adb1487de787c2a8890391e9fdf86d9f0);

[ 72](structx86__esf.md#a5e74e3d0dff1c92b6ba4853b113e4460) unsigned long [rcx](structx86__esf.md#a5e74e3d0dff1c92b6ba4853b113e4460);

[ 73](structx86__esf.md#aa1c6d9f92b5f2590d46194dd83a9831e) unsigned long [rdx](structx86__esf.md#aa1c6d9f92b5f2590d46194dd83a9831e);

[ 74](structx86__esf.md#ac826cfb5b6ade812b3772dd38e38bf5b) unsigned long [rsi](structx86__esf.md#ac826cfb5b6ade812b3772dd38e38bf5b);

[ 75](structx86__esf.md#ad809fba61de38b1563955b85036b152a) unsigned long [rdi](structx86__esf.md#ad809fba61de38b1563955b85036b152a);

[ 76](structx86__esf.md#a3c311b599eac76c582efbbacb5b778fc) unsigned long [r8](structx86__esf.md#a3c311b599eac76c582efbbacb5b778fc);

[ 77](structx86__esf.md#a85c0faf730d28f68ed1e036996b8077e) unsigned long [r9](structx86__esf.md#a85c0faf730d28f68ed1e036996b8077e);

[ 78](structx86__esf.md#a50317edcc041bb0c6ff06b053cc78792) unsigned long [r10](structx86__esf.md#a50317edcc041bb0c6ff06b053cc78792);

79 /\* Must be aligned 16 bytes from the end of this struct due to

80 \* requirements of 'fxsave (%rsp)'

81 \*/

[ 82](structx86__esf.md#a95a1902a651546b9158ae53b15e8c729) char [fxsave](structx86__esf.md#a95a1902a651546b9158ae53b15e8c729)[[X86\_FXSAVE\_SIZE](arch_2x86_2intel64_2thread_8h.md#ace21a6c2662fc989b5a51a2ebb53d129)];

[ 83](structx86__esf.md#a12a86c2d8d41a182a9ec3081e8ed93f3) unsigned long [r11](structx86__esf.md#a12a86c2d8d41a182a9ec3081e8ed93f3);

84

85 /\* Pushed by CPU or assembly stub \*/

[ 86](structx86__esf.md#a17da935fbc2a07a151bb5c4ab957f7a5) unsigned long [vector](structx86__esf.md#a17da935fbc2a07a151bb5c4ab957f7a5);

[ 87](structx86__esf.md#a8121fb267057487fc1d98fdd275c8b8c) unsigned long [code](structx86__esf.md#a8121fb267057487fc1d98fdd275c8b8c);

[ 88](structx86__esf.md#a2d922908b9c71b6254ee5f4278d554a9) unsigned long [rip](structx86__esf.md#a2d922908b9c71b6254ee5f4278d554a9);

[ 89](structx86__esf.md#a19f756adfde210556d11372e2372b245) unsigned long [cs](structx86__esf.md#a19f756adfde210556d11372e2372b245);

[ 90](structx86__esf.md#ae04678ba8e34ece57ebbeea081539ff3) unsigned long [rflags](structx86__esf.md#ae04678ba8e34ece57ebbeea081539ff3);

[ 91](structx86__esf.md#a07f64a14e57e1670b56ab1ce664e9526) unsigned long [rsp](structx86__esf.md#a07f64a14e57e1670b56ab1ce664e9526);

[ 92](structx86__esf.md#a3083baa8633209ca1314bd70fec9d7b4) unsigned long [ss](structx86__esf.md#a3083baa8633209ca1314bd70fec9d7b4);

93};

94

95typedef struct [x86\_esf](structx86__esf.md) z\_arch\_esf\_t;

96

[ 97](structx86__ssf.md)struct [x86\_ssf](structx86__ssf.md) {

[ 98](structx86__ssf.md#ab184936f5e61bd1d131930343999e7e1) unsigned long [rip](structx86__ssf.md#ab184936f5e61bd1d131930343999e7e1);

[ 99](structx86__ssf.md#a437b96d8a4918fac172debb55d2c4767) unsigned long [rflags](structx86__ssf.md#a437b96d8a4918fac172debb55d2c4767);

[ 100](structx86__ssf.md#a284dbdfac8e9d81b4a076b631f9267ec) unsigned long [r10](structx86__ssf.md#a284dbdfac8e9d81b4a076b631f9267ec);

[ 101](structx86__ssf.md#a2512b589af2b9c0f0dfbb908428ff21b) unsigned long [r9](structx86__ssf.md#a2512b589af2b9c0f0dfbb908428ff21b);

[ 102](structx86__ssf.md#a0f9f74e4f2790197819babea4c9c5e7e) unsigned long [r8](structx86__ssf.md#a0f9f74e4f2790197819babea4c9c5e7e);

[ 103](structx86__ssf.md#a29bf7a38c8fc2347a2930a71d1b724ec) unsigned long [rdx](structx86__ssf.md#a29bf7a38c8fc2347a2930a71d1b724ec);

[ 104](structx86__ssf.md#adec257b785157623eb9932bb3ff62932) unsigned long [rsi](structx86__ssf.md#adec257b785157623eb9932bb3ff62932);

[ 105](structx86__ssf.md#ac00879a99d2369b2832ab41febe08ced) char [fxsave](structx86__ssf.md#ac00879a99d2369b2832ab41febe08ced)[[X86\_FXSAVE\_SIZE](arch_2x86_2intel64_2thread_8h.md#ace21a6c2662fc989b5a51a2ebb53d129)];

[ 106](structx86__ssf.md#a9afd12452d8f44c1c4b391bc77afbaec) unsigned long [rdi](structx86__ssf.md#a9afd12452d8f44c1c4b391bc77afbaec);

[ 107](structx86__ssf.md#a080aae764546e381f6455abf18fb6853) unsigned long [rsp](structx86__ssf.md#a080aae764546e381f6455abf18fb6853);

108};

109

[ 110](x86_2intel64_2arch_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) do { \

111 \_\_asm\_\_ volatile( \

112 "movq %[reason], %%rax\n\t" \

113 "int $32\n\t" \

114 : \

115 : [reason] "i" (reason\_p)); \

116 CODE\_UNREACHABLE; /\* LCOV\_EXCL\_LINE \*/ \

117} while (false)

118

119#ifdef CONFIG\_PCIE

120#define X86\_RESERVE\_IRQ(irq\_p, name) \

121 static TYPE\_SECTION\_ITERABLE(uint8\_t, name, irq\_alloc, name) = irq\_p

122#else

[ 123](x86_2intel64_2arch_8h.md#a7b93ddbf458746ef3d189dfd10888077)#define X86\_RESERVE\_IRQ(irq\_p, name)

124#endif

125

126#endif /\* \_ASMLANGUAGE \*/

127

128/\*

129 \* All Intel64 interrupts are dynamically connected.

130 \*/

131

[ 132](x86_2intel64_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

133 X86\_RESERVE\_IRQ(irq\_p, \_CONCAT(\_irq\_alloc\_fixed, \_\_COUNTER\_\_)); \

134 arch\_irq\_connect\_dynamic(irq\_p, priority\_p, \

135 (void (\*)(const void \*))isr\_p, \

136 isr\_param\_p, flags\_p)

137

138#ifdef CONFIG\_PCIE

139

140#define ARCH\_PCIE\_IRQ\_CONNECT(bdf\_p, irq\_p, priority\_p, \

141 isr\_p, isr\_param\_p, flags\_p) \

142 X86\_RESERVE\_IRQ(irq\_p, \_CONCAT(\_irq\_alloc\_fixed, \_\_COUNTER\_\_)); \

143 pcie\_connect\_dynamic\_irq(bdf\_p, irq\_p, priority\_p, \

144 (void (\*)(const void \*))isr\_p, \

145 isr\_param\_p, flags\_p)

146

147#endif /\* CONFIG\_PCIE \*/

148

149/\*

150 \* Thread object needs to be 16-byte aligned.

151 \*/

[ 152](x86_2intel64_2arch_8h.md#ad0a10d482624ef8d91859f5bcdc2f647)#define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT 16

153

154#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_ARCH\_H\_ \*/

[thread.h](arch_2x86_2intel64_2thread_8h.md)

[X86\_FXSAVE\_SIZE](arch_2x86_2intel64_2thread_8h.md#ace21a6c2662fc989b5a51a2ebb53d129)

#define X86\_FXSAVE\_SIZE

**Definition** thread.h:37

[thread\_stack.h](arch_2x86_2thread__stack_8h.md)

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** arch.h:63

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[x86\_esf](structx86__esf.md)

**Definition** arch.h:59

[x86\_esf::rsp](structx86__esf.md#a07f64a14e57e1670b56ab1ce664e9526)

unsigned long rsp

**Definition** arch.h:91

[x86\_esf::r11](structx86__esf.md#a12a86c2d8d41a182a9ec3081e8ed93f3)

unsigned long r11

**Definition** arch.h:83

[x86\_esf::vector](structx86__esf.md#a17da935fbc2a07a151bb5c4ab957f7a5)

unsigned long vector

**Definition** arch.h:86

[x86\_esf::cs](structx86__esf.md#a19f756adfde210556d11372e2372b245)

unsigned long cs

**Definition** arch.h:89

[x86\_esf::rip](structx86__esf.md#a2d922908b9c71b6254ee5f4278d554a9)

unsigned long rip

**Definition** arch.h:88

[x86\_esf::ss](structx86__esf.md#a3083baa8633209ca1314bd70fec9d7b4)

unsigned long ss

**Definition** arch.h:92

[x86\_esf::r8](structx86__esf.md#a3c311b599eac76c582efbbacb5b778fc)

unsigned long r8

**Definition** arch.h:76

[x86\_esf::rbp](structx86__esf.md#a4bb58040b5089732faab5d191d5a557c)

unsigned long rbp

**Definition** arch.h:68

[x86\_esf::r10](structx86__esf.md#a50317edcc041bb0c6ff06b053cc78792)

unsigned long r10

**Definition** arch.h:78

[x86\_esf::rcx](structx86__esf.md#a5e74e3d0dff1c92b6ba4853b113e4460)

unsigned long rcx

**Definition** arch.h:72

[x86\_esf::code](structx86__esf.md#a8121fb267057487fc1d98fdd275c8b8c)

unsigned long code

**Definition** arch.h:87

[x86\_esf::r9](structx86__esf.md#a85c0faf730d28f68ed1e036996b8077e)

unsigned long r9

**Definition** arch.h:77

[x86\_esf::fxsave](structx86__esf.md#a95a1902a651546b9158ae53b15e8c729)

char fxsave[512]

**Definition** arch.h:82

[x86\_esf::rdx](structx86__esf.md#aa1c6d9f92b5f2590d46194dd83a9831e)

unsigned long rdx

**Definition** arch.h:73

[x86\_esf::rsi](structx86__esf.md#ac826cfb5b6ade812b3772dd38e38bf5b)

unsigned long rsi

**Definition** arch.h:74

[x86\_esf::rdi](structx86__esf.md#ad809fba61de38b1563955b85036b152a)

unsigned long rdi

**Definition** arch.h:75

[x86\_esf::rax](structx86__esf.md#adb1487de787c2a8890391e9fdf86d9f0)

unsigned long rax

**Definition** arch.h:71

[x86\_esf::rflags](structx86__esf.md#ae04678ba8e34ece57ebbeea081539ff3)

unsigned long rflags

**Definition** arch.h:90

[x86\_ssf](structx86__ssf.md)

**Definition** arch.h:97

[x86\_ssf::rsp](structx86__ssf.md#a080aae764546e381f6455abf18fb6853)

unsigned long rsp

**Definition** arch.h:107

[x86\_ssf::r8](structx86__ssf.md#a0f9f74e4f2790197819babea4c9c5e7e)

unsigned long r8

**Definition** arch.h:102

[x86\_ssf::r9](structx86__ssf.md#a2512b589af2b9c0f0dfbb908428ff21b)

unsigned long r9

**Definition** arch.h:101

[x86\_ssf::r10](structx86__ssf.md#a284dbdfac8e9d81b4a076b631f9267ec)

unsigned long r10

**Definition** arch.h:100

[x86\_ssf::rdx](structx86__ssf.md#a29bf7a38c8fc2347a2930a71d1b724ec)

unsigned long rdx

**Definition** arch.h:103

[x86\_ssf::rflags](structx86__ssf.md#a437b96d8a4918fac172debb55d2c4767)

unsigned long rflags

**Definition** arch.h:99

[x86\_ssf::rdi](structx86__ssf.md#a9afd12452d8f44c1c4b391bc77afbaec)

unsigned long rdi

**Definition** arch.h:106

[x86\_ssf::rip](structx86__ssf.md#ab184936f5e61bd1d131930343999e7e1)

unsigned long rip

**Definition** arch.h:98

[x86\_ssf::fxsave](structx86__ssf.md#ac00879a99d2369b2832ab41febe08ced)

char fxsave[512]

**Definition** arch.h:105

[x86\_ssf::rsi](structx86__ssf.md#adec257b785157623eb9932bb3ff62932)

unsigned long rsi

**Definition** arch.h:104

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

[sys\_read64](x86_2intel64_2arch_8h.md#a7ba6099642d909c50219d174c35f6a94)

static ALWAYS\_INLINE uint64\_t sys\_read64(mm\_reg\_t addr)

**Definition** arch.h:34

[sys\_write64](x86_2intel64_2arch_8h.md#aed9cf591fb95242f161e6fc8719cf3e3)

static ALWAYS\_INLINE void sys\_write64(uint64\_t data, mm\_reg\_t addr)

**Definition** arch.h:25

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [intel64](dir_1abf87bed33eaf4508c3178cbd4d6168.md)
- [arch.h](x86_2intel64_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
