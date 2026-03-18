---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2x86_2ia32_2gdbstub_8h_source.html
original_path: doxygen/html/arch_2x86_2ia32_2gdbstub_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gdbstub.h

[Go to the documentation of this file.](arch_2x86_2ia32_2gdbstub_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_GDBSTUB\_SYS\_H\_

13#define ZEPHYR\_INCLUDE\_ARCH\_X86\_GDBSTUB\_SYS\_H\_

14

15#ifndef \_ASMLANGUAGE

16

17#include <[stdint.h](stdint_8h.md)>

18#include <[zephyr/toolchain.h](toolchain_8h.md)>

19

[ 23](arch_2x86_2ia32_2gdbstub_8h.md#a235bb190327ce0586e0b111186fe1b95)#define GDB\_STUB\_NUM\_REGISTERS 16

24

32

[ 33](structgdb__interrupt__ctx.md)struct [gdb\_interrupt\_ctx](structgdb__interrupt__ctx.md) {

[ 34](structgdb__interrupt__ctx.md#aa9270fa78d2485bc74090ac125686001) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ss](structgdb__interrupt__ctx.md#aa9270fa78d2485bc74090ac125686001);

[ 35](structgdb__interrupt__ctx.md#ac030129b89c096a3a63d500f7bad3694) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gs](structgdb__interrupt__ctx.md#ac030129b89c096a3a63d500f7bad3694);

[ 36](structgdb__interrupt__ctx.md#aa848335652cd22a13d23417eceaba37c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fs](structgdb__interrupt__ctx.md#aa848335652cd22a13d23417eceaba37c);

[ 37](structgdb__interrupt__ctx.md#a23a3d136237cf2db7a49a538e9cbb5c1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [es](structgdb__interrupt__ctx.md#a23a3d136237cf2db7a49a538e9cbb5c1);

[ 38](structgdb__interrupt__ctx.md#afe9a8264a1ba4402f1d6ceed42c2fe35) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ds](structgdb__interrupt__ctx.md#afe9a8264a1ba4402f1d6ceed42c2fe35);

[ 39](structgdb__interrupt__ctx.md#a9bdc030dfe999ce4d2c5dacf999a8152) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [edi](structgdb__interrupt__ctx.md#a9bdc030dfe999ce4d2c5dacf999a8152);

[ 40](structgdb__interrupt__ctx.md#aa174bfc58d6f4bd0aa10e48139aae073) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [esi](structgdb__interrupt__ctx.md#aa174bfc58d6f4bd0aa10e48139aae073);

[ 41](structgdb__interrupt__ctx.md#ac7ae28c665e573abbfcdafe07e5da473) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ebp](structgdb__interrupt__ctx.md#ac7ae28c665e573abbfcdafe07e5da473);

[ 42](structgdb__interrupt__ctx.md#a8284780b26c1ba6fd3117fc1f5a1ea1f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [esp](structgdb__interrupt__ctx.md#a8284780b26c1ba6fd3117fc1f5a1ea1f);

[ 43](structgdb__interrupt__ctx.md#a61abfb0bf1858ae4cba3d72bd5f8d95d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ebx](structgdb__interrupt__ctx.md#a61abfb0bf1858ae4cba3d72bd5f8d95d);

[ 44](structgdb__interrupt__ctx.md#a483bef7f8235e91ba450073dcdf9d6bb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [edx](structgdb__interrupt__ctx.md#a483bef7f8235e91ba450073dcdf9d6bb);

[ 45](structgdb__interrupt__ctx.md#ae23b76372e6aa71488427327240d078a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ecx](structgdb__interrupt__ctx.md#ae23b76372e6aa71488427327240d078a);

[ 46](structgdb__interrupt__ctx.md#ad60975255b667db74255d1a8534b759a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [eax](structgdb__interrupt__ctx.md#ad60975255b667db74255d1a8534b759a);

[ 47](structgdb__interrupt__ctx.md#af3d805bf15d0c6bac1382e2cfe58bef4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vector](structgdb__interrupt__ctx.md#af3d805bf15d0c6bac1382e2cfe58bef4);

[ 48](structgdb__interrupt__ctx.md#a106553cd8345cd8179aa3e5b6d9a10b8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [error\_code](structgdb__interrupt__ctx.md#a106553cd8345cd8179aa3e5b6d9a10b8);

[ 49](structgdb__interrupt__ctx.md#a4c77f1335eb4dfe2d54f2e3d2526af92) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [eip](structgdb__interrupt__ctx.md#a4c77f1335eb4dfe2d54f2e3d2526af92);

[ 50](structgdb__interrupt__ctx.md#ad09b829083a190226461accdfc7bf17d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cs](structgdb__interrupt__ctx.md#ad09b829083a190226461accdfc7bf17d);

[ 51](structgdb__interrupt__ctx.md#a248f18679b999bc4cf5438d729725a1e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [eflags](structgdb__interrupt__ctx.md#a248f18679b999bc4cf5438d729725a1e);

52} \_\_packed;

53

57

[ 58](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57)enum [GDB\_REGISTER](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57) {

[ 59](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57ab4c205bdcc3be6a5050e7bebd4fb6b66) [GDB\_EAX](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57ab4c205bdcc3be6a5050e7bebd4fb6b66),

[ 60](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57abee48d7c6075a3c8928ec45a8a609429) [GDB\_ECX](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57abee48d7c6075a3c8928ec45a8a609429),

[ 61](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a22a0a7034fcd3674658eecef1f2dade8) [GDB\_EDX](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a22a0a7034fcd3674658eecef1f2dade8),

[ 62](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57abaaf1dc478746db2a60681141fc35156) [GDB\_EBX](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57abaaf1dc478746db2a60681141fc35156),

[ 63](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57af4f770bdcdbcca2db69c917f2525ea44) [GDB\_ESP](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57af4f770bdcdbcca2db69c917f2525ea44),

[ 64](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a001777bf465ee869d25c247dd8c4916b) [GDB\_EBP](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a001777bf465ee869d25c247dd8c4916b),

[ 65](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a0ee89015912e10141cd809b8d0578e6f) [GDB\_ESI](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a0ee89015912e10141cd809b8d0578e6f),

[ 66](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57ade30ceaa244559a00e83b0f7a8f669a7) [GDB\_EDI](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57ade30ceaa244559a00e83b0f7a8f669a7),

[ 67](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a22b538160b178a0438fbaf3596425086) [GDB\_PC](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a22b538160b178a0438fbaf3596425086),

[ 68](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a8c5ef12c827f25bdb506a9bfd35a4fca) [GDB\_EFLAGS](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a8c5ef12c827f25bdb506a9bfd35a4fca),

[ 69](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57acc9df508ccc4168e9f77e4054d99fd6b) [GDB\_CS](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57acc9df508ccc4168e9f77e4054d99fd6b),

[ 70](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a1cefa340d9b999a519dbb60c18098b28) [GDB\_SS](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a1cefa340d9b999a519dbb60c18098b28),

[ 71](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57acb0bd3c78585106edca9f1f933d9e715) [GDB\_DS](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57acb0bd3c78585106edca9f1f933d9e715),

[ 72](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a9880757bbfebbf1a4cc54fea187209b9) [GDB\_ES](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a9880757bbfebbf1a4cc54fea187209b9),

[ 73](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a41774764a1340a3003020ba07b90f175) [GDB\_FS](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a41774764a1340a3003020ba07b90f175),

[ 74](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a97870647fb9b956008034d5b8f07c333) [GDB\_GS](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a97870647fb9b956008034d5b8f07c333),

[ 75](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a07753f9e894968bb44a885731d3c6a7c) [GDB\_ORIG\_EAX](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a07753f9e894968bb44a885731d3c6a7c) = 41,

76};

77

78struct [gdb\_ctx](structgdb__ctx.md) {

79 unsigned int [exception](structgdb__ctx.md#adba5c39e347abc419b365bab2a1a0999);

80 unsigned int [registers](structgdb__ctx.md#a3932959d4a31a75c6cf77b42b95bd511)[[GDB\_STUB\_NUM\_REGISTERS](arch_2x86_2ia32_2gdbstub_8h.md#a235bb190327ce0586e0b111186fe1b95)];

81};

82

83#endif /\* \_ASMLANGUAGE \*/

84

85#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_GDBSTUB\_SYS\_H\_ \*/

[GDB\_REGISTER](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57)

GDB\_REGISTER

IA-32 register used in gdbstub.

**Definition** gdbstub.h:58

[GDB\_EBP](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a001777bf465ee869d25c247dd8c4916b)

@ GDB\_EBP

**Definition** gdbstub.h:64

[GDB\_ORIG\_EAX](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a07753f9e894968bb44a885731d3c6a7c)

@ GDB\_ORIG\_EAX

**Definition** gdbstub.h:75

[GDB\_ESI](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a0ee89015912e10141cd809b8d0578e6f)

@ GDB\_ESI

**Definition** gdbstub.h:65

[GDB\_SS](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a1cefa340d9b999a519dbb60c18098b28)

@ GDB\_SS

**Definition** gdbstub.h:70

[GDB\_EDX](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a22a0a7034fcd3674658eecef1f2dade8)

@ GDB\_EDX

**Definition** gdbstub.h:61

[GDB\_PC](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a22b538160b178a0438fbaf3596425086)

@ GDB\_PC

**Definition** gdbstub.h:67

[GDB\_FS](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a41774764a1340a3003020ba07b90f175)

@ GDB\_FS

**Definition** gdbstub.h:73

[GDB\_EFLAGS](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a8c5ef12c827f25bdb506a9bfd35a4fca)

@ GDB\_EFLAGS

**Definition** gdbstub.h:68

[GDB\_GS](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a97870647fb9b956008034d5b8f07c333)

@ GDB\_GS

**Definition** gdbstub.h:74

[GDB\_ES](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57a9880757bbfebbf1a4cc54fea187209b9)

@ GDB\_ES

**Definition** gdbstub.h:72

[GDB\_EAX](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57ab4c205bdcc3be6a5050e7bebd4fb6b66)

@ GDB\_EAX

**Definition** gdbstub.h:59

[GDB\_EBX](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57abaaf1dc478746db2a60681141fc35156)

@ GDB\_EBX

**Definition** gdbstub.h:62

[GDB\_ECX](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57abee48d7c6075a3c8928ec45a8a609429)

@ GDB\_ECX

**Definition** gdbstub.h:60

[GDB\_DS](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57acb0bd3c78585106edca9f1f933d9e715)

@ GDB\_DS

**Definition** gdbstub.h:71

[GDB\_CS](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57acc9df508ccc4168e9f77e4054d99fd6b)

@ GDB\_CS

**Definition** gdbstub.h:69

[GDB\_EDI](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57ade30ceaa244559a00e83b0f7a8f669a7)

@ GDB\_EDI

**Definition** gdbstub.h:66

[GDB\_ESP](arch_2x86_2ia32_2gdbstub_8h.md#a02deeb8532e144b369c484cdd4bc1a57af4f770bdcdbcca2db69c917f2525ea44)

@ GDB\_ESP

**Definition** gdbstub.h:63

[GDB\_STUB\_NUM\_REGISTERS](arch_2x86_2ia32_2gdbstub_8h.md#a235bb190327ce0586e0b111186fe1b95)

#define GDB\_STUB\_NUM\_REGISTERS

Number of register used by gdbstub in IA-32.

**Definition** gdbstub.h:23

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[gdb\_ctx](structgdb__ctx.md)

Architecture specific GDB context.

**Definition** gdbstub.h:61

[gdb\_ctx::registers](structgdb__ctx.md#a3932959d4a31a75c6cf77b42b95bd511)

unsigned int registers[GDB\_NUM\_REGS]

**Definition** gdbstub.h:64

[gdb\_ctx::exception](structgdb__ctx.md#adba5c39e347abc419b365bab2a1a0999)

unsigned int exception

Exception reason.

**Definition** gdbstub.h:63

[gdb\_interrupt\_ctx](structgdb__interrupt__ctx.md)

GDB interruption context.

**Definition** gdbstub.h:33

[gdb\_interrupt\_ctx::error\_code](structgdb__interrupt__ctx.md#a106553cd8345cd8179aa3e5b6d9a10b8)

uint32\_t error\_code

**Definition** gdbstub.h:48

[gdb\_interrupt\_ctx::es](structgdb__interrupt__ctx.md#a23a3d136237cf2db7a49a538e9cbb5c1)

uint32\_t es

**Definition** gdbstub.h:37

[gdb\_interrupt\_ctx::eflags](structgdb__interrupt__ctx.md#a248f18679b999bc4cf5438d729725a1e)

uint32\_t eflags

**Definition** gdbstub.h:51

[gdb\_interrupt\_ctx::edx](structgdb__interrupt__ctx.md#a483bef7f8235e91ba450073dcdf9d6bb)

uint32\_t edx

**Definition** gdbstub.h:44

[gdb\_interrupt\_ctx::eip](structgdb__interrupt__ctx.md#a4c77f1335eb4dfe2d54f2e3d2526af92)

uint32\_t eip

**Definition** gdbstub.h:49

[gdb\_interrupt\_ctx::ebx](structgdb__interrupt__ctx.md#a61abfb0bf1858ae4cba3d72bd5f8d95d)

uint32\_t ebx

**Definition** gdbstub.h:43

[gdb\_interrupt\_ctx::esp](structgdb__interrupt__ctx.md#a8284780b26c1ba6fd3117fc1f5a1ea1f)

uint32\_t esp

**Definition** gdbstub.h:42

[gdb\_interrupt\_ctx::edi](structgdb__interrupt__ctx.md#a9bdc030dfe999ce4d2c5dacf999a8152)

uint32\_t edi

**Definition** gdbstub.h:39

[gdb\_interrupt\_ctx::esi](structgdb__interrupt__ctx.md#aa174bfc58d6f4bd0aa10e48139aae073)

uint32\_t esi

**Definition** gdbstub.h:40

[gdb\_interrupt\_ctx::fs](structgdb__interrupt__ctx.md#aa848335652cd22a13d23417eceaba37c)

uint32\_t fs

**Definition** gdbstub.h:36

[gdb\_interrupt\_ctx::ss](structgdb__interrupt__ctx.md#aa9270fa78d2485bc74090ac125686001)

uint32\_t ss

**Definition** gdbstub.h:34

[gdb\_interrupt\_ctx::gs](structgdb__interrupt__ctx.md#ac030129b89c096a3a63d500f7bad3694)

uint32\_t gs

**Definition** gdbstub.h:35

[gdb\_interrupt\_ctx::ebp](structgdb__interrupt__ctx.md#ac7ae28c665e573abbfcdafe07e5da473)

uint32\_t ebp

**Definition** gdbstub.h:41

[gdb\_interrupt\_ctx::cs](structgdb__interrupt__ctx.md#ad09b829083a190226461accdfc7bf17d)

uint32\_t cs

**Definition** gdbstub.h:50

[gdb\_interrupt\_ctx::eax](structgdb__interrupt__ctx.md#ad60975255b667db74255d1a8534b759a)

uint32\_t eax

**Definition** gdbstub.h:46

[gdb\_interrupt\_ctx::ecx](structgdb__interrupt__ctx.md#ae23b76372e6aa71488427327240d078a)

uint32\_t ecx

**Definition** gdbstub.h:45

[gdb\_interrupt\_ctx::vector](structgdb__interrupt__ctx.md#af3d805bf15d0c6bac1382e2cfe58bef4)

uint32\_t vector

**Definition** gdbstub.h:47

[gdb\_interrupt\_ctx::ds](structgdb__interrupt__ctx.md#afe9a8264a1ba4402f1d6ceed42c2fe35)

uint32\_t ds

**Definition** gdbstub.h:38

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [gdbstub.h](arch_2x86_2ia32_2gdbstub_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
