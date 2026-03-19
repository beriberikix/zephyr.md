---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch__interface_8h_source.html
original_path: doxygen/html/arch__interface_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_interface.h

[Go to the documentation of this file.](arch__interface_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

27#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARCH\_INTERFACE\_H\_

28#define ZEPHYR\_INCLUDE\_ARCH\_ARCH\_INTERFACE\_H\_

29

30#ifndef \_ASMLANGUAGE

31#include <[zephyr/toolchain.h](toolchain_8h.md)>

32#include <stddef.h>

33#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

34#include <[zephyr/arch/cpu.h](cpu_8h.md)>

35#include <[zephyr/irq\_offload.h](irq__offload_8h.md)>

36

37#ifdef \_\_cplusplus

38extern "C" {

39#endif

40

41/\* NOTE: We cannot pull in kernel.h here, need some forward declarations \*/

42struct [arch\_esf](structarch__esf.md);

43struct [k\_thread](structk__thread.md);

44struct [k\_mem\_domain](structk__mem__domain.md);

45

[ 46](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)typedef struct z\_thread\_stack\_element [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1);

47

[ 48](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717)typedef void (\*[k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717))(void \*p1, void \*p2, void \*p3);

49

50\_\_deprecated typedef struct [arch\_esf](structarch__esf.md) z\_arch\_esf\_t;

51

57

[ 72](group__arch-timing.md#ga9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](group__arch-timing.md#ga9ee9f897ec750957de45bf8d43349d5e)(void);

73

[ 86](group__arch-timing.md#gacc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](group__arch-timing.md#gacc1ed8d949f694a1d39e389334caf971)(void);

87

89

90

95

101

110

120

143

157

162

164

169

[ 187](group__arch-pm.md#ga6ce051203e6cc091d0fb42a15f662a48)void [arch\_cpu\_idle](group__arch-pm.md#ga6ce051203e6cc091d0fb42a15f662a48)(void);

188

[ 207](group__arch-pm.md#ga4d0297717c23a3cc5df434549e26924d)void [arch\_cpu\_atomic\_idle](group__arch-pm.md#ga4d0297717c23a3cc5df434549e26924d)(unsigned int key);

208

210

211

216

[ 222](group__arch-smp.md#ga4a9ac90ba7cc7c403472bfdaf3369ed2)typedef void (\*[arch\_cpustart\_t](group__arch-smp.md#ga4a9ac90ba7cc7c403472bfdaf3369ed2))(void \*data);

223

[ 244](group__arch-smp.md#ga32b7e543ce51498200c368c39c900bc8)void [arch\_cpu\_start](group__arch-smp.md#ga32b7e543ce51498200c368c39c900bc8)(int cpu\_num, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, int sz,

245 [arch\_cpustart\_t](group__arch-smp.md#ga4a9ac90ba7cc7c403472bfdaf3369ed2) fn, void \*arg);

246

[ 252](group__arch-smp.md#ga5a7f0198ee061551c300129bffe64717)bool [arch\_cpu\_active](group__arch-smp.md#ga5a7f0198ee061551c300129bffe64717)(int cpu\_num);

253

255

256

261

[ 267](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)static inline unsigned int [arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)(void);

268

[ 274](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)static inline void [arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)(unsigned int key);

275

[ 283](group__arch-irq.md#ga1b827afafc622d412962f568b78726dc)static inline bool [arch\_irq\_unlocked](group__arch-irq.md#ga1b827afafc622d412962f568b78726dc)(unsigned int key);

284

[ 299](group__arch-irq.md#ga216d692e87bfba955a60f8e570e127df)void [arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)(unsigned int irq);

300

[ 306](group__arch-irq.md#gaa278d630653b33cb339621d725ed295a)void [arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)(unsigned int irq);

307

[ 313](group__arch-irq.md#ga3bd8e963a124421bb372dab4bdc6cd83)int [arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)(unsigned int irq);

314

[ 326](group__arch-irq.md#gaa4d733913e12a12e104dc4781cca7308)int [arch\_irq\_connect\_dynamic](group__arch-irq.md#gaa4d733913e12a12e104dc4781cca7308)(unsigned int irq, unsigned int priority,

327 void (\*routine)(const void \*parameter),

328 const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

329

[ 344](group__arch-irq.md#ga41483a9fc1090d96d066e107a74ee38c)int [arch\_irq\_disconnect\_dynamic](group__arch-irq.md#ga41483a9fc1090d96d066e107a74ee38c)(unsigned int irq, unsigned int priority,

345 void (\*routine)(const void \*parameter),

346 const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

347

353

354#ifdef CONFIG\_PCIE

360#endif /\* CONFIG\_PCIE \*/

361

367

373

379

385

391

392#ifndef CONFIG\_PCIE\_CONTROLLER

[ 402](group__arch-irq.md#gaac8f60e7dfc5ce3222372798e96316ae)unsigned int [arch\_irq\_allocate](group__arch-irq.md#gaac8f60e7dfc5ce3222372798e96316ae)(void);

403

[ 412](group__arch-irq.md#ga5f0942bd035c50c9d2d91ada472f37c4)void [arch\_irq\_set\_used](group__arch-irq.md#ga5f0942bd035c50c9d2d91ada472f37c4)(unsigned int irq);

413

[ 421](group__arch-irq.md#ga5c85d7bf54a83190ed27587dc5a01de5)bool [arch\_irq\_is\_used](group__arch-irq.md#ga5c85d7bf54a83190ed27587dc5a01de5)(unsigned int irq);

422

423#endif /\* CONFIG\_PCIE\_CONTROLLER \*/

424

439

440#ifdef CONFIG\_IRQ\_OFFLOAD

457void arch\_irq\_offload([irq\_offload\_routine\_t](irq__offload_8h.md#a5bcf9956ddbf5ea75619f0cef91e1214) routine, const void \*parameter);

458

459

463void arch\_irq\_offload\_init(void);

464

465#endif /\* CONFIG\_IRQ\_OFFLOAD \*/

466

468

469

475#ifdef CONFIG\_SMP

[ 477](group__arch-smp.md#gad42138d41dff6a4aad8abf7d77fcd8b2)static inline struct \_cpu \*[arch\_curr\_cpu](group__arch-smp.md#gad42138d41dff6a4aad8abf7d77fcd8b2)(void);

478

479

[ 499](group__arch-smp.md#gad628c89816128546501e3c26eaaf9dea)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_proc\_id](group__arch-smp.md#gad628c89816128546501e3c26eaaf9dea)(void);

500

[ 506](group__arch-smp.md#ga8fe90cec57c56993df14c0d545106ca3)void [arch\_sched\_broadcast\_ipi](group__arch-smp.md#ga8fe90cec57c56993df14c0d545106ca3)(void);

507

[ 515](group__arch-smp.md#gadebac82c1ed0a8a08adb297738d2633e)void [arch\_sched\_directed\_ipi](group__arch-smp.md#gadebac82c1ed0a8a08adb297738d2633e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cpu\_bitmap);

516

[ 517](group__arch-smp.md#ga6ffc01f86f4541d1092ee4b277a07ac6)int [arch\_smp\_init](group__arch-smp.md#ga6ffc01f86f4541d1092ee4b277a07ac6)(void);

518

519#endif /\* CONFIG\_SMP \*/

520

[ 529](group__arch-smp.md#ga078e9bf1a4a557d1321ddc4848092cbe)static inline unsigned int [arch\_num\_cpus](group__arch-smp.md#ga078e9bf1a4a557d1321ddc4848092cbe)(void);

530

532

533

539

540#ifdef CONFIG\_USERSPACE

541#include <[zephyr/arch/syscall.h](arch_2syscall_8h.md)>

542

[ 564](group__arch-userspace.md#ga5e9ab24b9c980e327903fbe3f5bd97f3)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke0](group__arch-userspace.md#ga5e9ab24b9c980e327903fbe3f5bd97f3)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

565

[ 576](group__arch-userspace.md#ga4cfb3b2b38e5afca889e8b9765d6c3df)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke1](group__arch-userspace.md#ga4cfb3b2b38e5afca889e8b9765d6c3df)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1,

577 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

578

[ 590](group__arch-userspace.md#ga1e78f1022aaf10e88727b142b56d4ef0)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke2](group__arch-userspace.md#ga1e78f1022aaf10e88727b142b56d4ef0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

591 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

592

[ 605](group__arch-userspace.md#gaacb1c66a1b7bf2293fea269f6b5e1c7e)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke3](group__arch-userspace.md#gaacb1c66a1b7bf2293fea269f6b5e1c7e)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

606 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3,

607 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

608

[ 622](group__arch-userspace.md#ga0ba3ae2290827385b226ebdbf3de3b53)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke4](group__arch-userspace.md#ga0ba3ae2290827385b226ebdbf3de3b53)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

623 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

624 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

625

[ 640](group__arch-userspace.md#ga9971c78bc8f579a0dadf84225dc0c3ff)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke5](group__arch-userspace.md#ga9971c78bc8f579a0dadf84225dc0c3ff)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

641 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

642 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5,

643 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

644

[ 660](group__arch-userspace.md#gac6cae2197637993a86b6ec6803b5742b)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke6](group__arch-userspace.md#gac6cae2197637993a86b6ec6803b5742b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

661 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

662 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

663 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

664

[ 670](group__arch-userspace.md#ga89ab53a218add419e37f89c1f5fd955f)static inline bool [arch\_is\_user\_context](group__arch-userspace.md#ga89ab53a218add419e37f89c1f5fd955f)(void);

671

[ 677](group__arch-userspace.md#ga71542fcc679a94ad9ea60d7ac46da361)int [arch\_mem\_domain\_max\_partitions\_get](group__arch-userspace.md#ga71542fcc679a94ad9ea60d7ac46da361)(void);

678

679#ifdef CONFIG\_ARCH\_MEM\_DOMAIN\_DATA

701int arch\_mem\_domain\_init(struct [k\_mem\_domain](structk__mem__domain.md) \*domain);

702#endif /\* CONFIG\_ARCH\_MEM\_DOMAIN\_DATA \*/

703

704#ifdef CONFIG\_ARCH\_MEM\_DOMAIN\_SYNCHRONOUS\_API

722int arch\_mem\_domain\_thread\_add(struct [k\_thread](structk__thread.md) \*thread);

723

738int arch\_mem\_domain\_thread\_remove(struct [k\_thread](structk__thread.md) \*thread);

739

757int arch\_mem\_domain\_partition\_remove(struct [k\_mem\_domain](structk__mem__domain.md) \*domain,

758 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) partition\_id);

759

772int arch\_mem\_domain\_partition\_add(struct [k\_mem\_domain](structk__mem__domain.md) \*domain,

773 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) partition\_id);

774#endif /\* CONFIG\_ARCH\_MEM\_DOMAIN\_SYNCHRONOUS\_API \*/

775

[ 804](group__arch-userspace.md#ga13053a9233b86d5cd19dc3cea5804a16)int [arch\_buffer\_validate](group__arch-userspace.md#ga13053a9233b86d5cd19dc3cea5804a16)(const void \*addr, size\_t size, int write);

805

[ 821](group__arch-userspace.md#ga48be2412ba65ec550ded63e2f1a0470f)size\_t [arch\_virt\_region\_align](group__arch-userspace.md#ga48be2412ba65ec550ded63e2f1a0470f)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, size\_t size);

822

[ 841](group__arch-userspace.md#ga447daa0454a90a7a3a247de01e522567)FUNC\_NORETURN void [arch\_user\_mode\_enter](group__arch-userspace.md#ga447daa0454a90a7a3a247de01e522567)([k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) user\_entry,

842 void \*p1, void \*p2, void \*p3);

843

[ 858](group__arch-userspace.md#gad53908f229d7e2c333574b009493644b)FUNC\_NORETURN void [arch\_syscall\_oops](group__arch-userspace.md#gad53908f229d7e2c333574b009493644b)(void \*ssf);

859

[ 872](group__arch-userspace.md#ga174c4f356fe315c523cefbf513858c9c)size\_t [arch\_user\_string\_nlen](group__arch-userspace.md#ga174c4f356fe315c523cefbf513858c9c)(const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), size\_t maxsize, int \*err);

873#endif /\* CONFIG\_USERSPACE \*/

874

889#ifndef CONFIG\_ARCH\_HAS\_COHERENCE

[ 890](group__arch-userspace.md#ga8c6bb0f6730c115689452b016ac1761f)static inline bool [arch\_mem\_coherent](group__arch-userspace.md#ga8c6bb0f6730c115689452b016ac1761f)(void \*ptr)

891{

892 ARG\_UNUSED(ptr);

893 return true;

894}

895#endif

896

937#ifndef CONFIG\_KERNEL\_COHERENCE

[ 938](group__arch-userspace.md#ga306e9d0e5f8094cb75686f1c43d068a9)static inline void [arch\_cohere\_stacks](group__arch-userspace.md#ga306e9d0e5f8094cb75686f1c43d068a9)(struct [k\_thread](structk__thread.md) \*old\_thread,

939 void \*old\_switch\_handle,

940 struct [k\_thread](structk__thread.md) \*new\_thread)

941{

942 ARG\_UNUSED(old\_thread);

943 ARG\_UNUSED(old\_switch\_handle);

944 ARG\_UNUSED(new\_thread);

945}

946#endif

947

949

955

956#ifdef CONFIG\_GDBSTUB

957struct [gdb\_ctx](structgdb__ctx.md);

958

[ 964](group__arch-gdbstub.md#ga21c8a32d35c4d267b8306d595ff1d726)void [arch\_gdb\_init](group__arch-gdbstub.md#ga21c8a32d35c4d267b8306d595ff1d726)(void);

965

[ 971](group__arch-gdbstub.md#ga9c130421feeee919651828511743b346)void [arch\_gdb\_continue](group__arch-gdbstub.md#ga9c130421feeee919651828511743b346)(void);

972

[ 978](group__arch-gdbstub.md#ga2aa577d5e55c8b739e2be6187336aaf0)void [arch\_gdb\_step](group__arch-gdbstub.md#ga2aa577d5e55c8b739e2be6187336aaf0)(void);

979

[ 993](group__arch-gdbstub.md#ga5317106a8022bea2a0d42af0789cc016)size\_t [arch\_gdb\_reg\_readall](group__arch-gdbstub.md#ga5317106a8022bea2a0d42af0789cc016)(struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen);

994

[ 1008](group__arch-gdbstub.md#ga0ef78d7e193e98549d9665632e53d5ca)size\_t [arch\_gdb\_reg\_writeall](group__arch-gdbstub.md#ga0ef78d7e193e98549d9665632e53d5ca)(struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hex, size\_t hexlen);

1009

[ 1024](group__arch-gdbstub.md#gaa3216e9f381f974c374a6399af5cdba5)size\_t [arch\_gdb\_reg\_readone](group__arch-gdbstub.md#gaa3216e9f381f974c374a6399af5cdba5)(struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen,

1025 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) regno);

1026

[ 1041](group__arch-gdbstub.md#gad717b520d774294bbda78a56cddcaeff)size\_t [arch\_gdb\_reg\_writeone](group__arch-gdbstub.md#gad717b520d774294bbda78a56cddcaeff)(struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hex, size\_t hexlen,

1042 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) regno);

1043

[ 1056](group__arch-gdbstub.md#gab6f42110cf2340132bf2b3916810c01d)int [arch\_gdb\_add\_breakpoint](group__arch-gdbstub.md#gab6f42110cf2340132bf2b3916810c01d)(struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type,

1057 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) kind);

1058

[ 1071](group__arch-gdbstub.md#ga734041433f69030ad98439d10ef56ad6)int [arch\_gdb\_remove\_breakpoint](group__arch-gdbstub.md#ga734041433f69030ad98439d10ef56ad6)(struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type,

1072 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) kind);

1073

1074#endif

1076

1077#ifdef CONFIG\_TIMING\_FUNCTIONS

1078#include <[zephyr/timing/types.h](include_2zephyr_2timing_2types_8h.md)>

1079

1090

[ 1098](group__timing__api__arch.md#ga5d9923569b40437c28879ff4b3ff77c2)void [arch\_timing\_init](group__timing__api__arch.md#ga5d9923569b40437c28879ff4b3ff77c2)(void);

1099

[ 1112](group__timing__api__arch.md#gaf8cd88e81c2104b5eb0fbe42967b7834)void [arch\_timing\_start](group__timing__api__arch.md#gaf8cd88e81c2104b5eb0fbe42967b7834)(void);

1113

[ 1126](group__timing__api__arch.md#ga566483c64f5c5d2f0465e3f969303fd3)void [arch\_timing\_stop](group__timing__api__arch.md#ga566483c64f5c5d2f0465e3f969303fd3)(void);

1127

[ 1154](group__timing__api__arch.md#gad7a709477650c8596a96fe080f583fdd)[timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) [arch\_timing\_counter\_get](group__timing__api__arch.md#gad7a709477650c8596a96fe080f583fdd)(void);

1155

[ 1170](group__timing__api__arch.md#ga44d3a7bd8b7008c9cd6c0524e97f128c)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_timing\_cycles\_get](group__timing__api__arch.md#ga44d3a7bd8b7008c9cd6c0524e97f128c)(volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const start,

1171 volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const end);

1172

[ 1180](group__timing__api__arch.md#ga026409e1dc323ceddb82b2a6f1cc7ca2)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_timing\_freq\_get](group__timing__api__arch.md#ga026409e1dc323ceddb82b2a6f1cc7ca2)(void);

1181

[ 1190](group__timing__api__arch.md#ga8424bc96c05dcae34b7ffd445e2916fe)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_timing\_cycles\_to\_ns](group__timing__api__arch.md#ga8424bc96c05dcae34b7ffd445e2916fe)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles);

1191

[ 1201](group__timing__api__arch.md#ga925b4caff80f1dbac36531b479b24364)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_timing\_cycles\_to\_ns\_avg](group__timing__api__arch.md#ga925b4caff80f1dbac36531b479b24364)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count);

1202

[ 1210](group__timing__api__arch.md#ga1f7bfb9ce0588f3b423c2a63933d40eb)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_timing\_freq\_get\_mhz](group__timing__api__arch.md#ga1f7bfb9ce0588f3b423c2a63933d40eb)(void);

1211

1213

1214#endif /\* CONFIG\_TIMING\_FUNCTIONS \*/

1215

1216#ifdef CONFIG\_PCIE\_MSI\_MULTI\_VECTOR

1217

1218struct [msi\_vector](structmsi__vector.md);

1219typedef struct [msi\_vector](structmsi__vector.md) [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231);

1220

1230[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) arch\_pcie\_msi\_vectors\_allocate(unsigned int priority,

1231 [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vectors,

1232 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector);

1233

1244bool arch\_pcie\_msi\_vector\_connect([msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector,

1245 void (\*routine)(const void \*parameter),

1246 const void \*parameter,

1247 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1248

1249#endif /\* CONFIG\_PCIE\_MSI\_MULTI\_VECTOR \*/

1250

[ 1259](arch__interface_8h.md#a9932b29bc0c3b86e4f8cbd6708ef5d9c)void [arch\_spin\_relax](arch__interface_8h.md#a9932b29bc0c3b86e4f8cbd6708ef5d9c)(void);

1260

1271

[ 1279](group__arch-stackwalk.md#gaec9949df614728aa6d677f9f1fafd844)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[stack\_trace\_callback\_fn](group__arch-stackwalk.md#gaec9949df614728aa6d677f9f1fafd844))(void \*cookie, unsigned long addr);

1280

[ 1296](group__arch-stackwalk.md#ga7129c254277cfa162cd9c5778a7662c2)void [arch\_stack\_walk](group__arch-stackwalk.md#ga7129c254277cfa162cd9c5778a7662c2)([stack\_trace\_callback\_fn](group__arch-stackwalk.md#gaec9949df614728aa6d677f9f1fafd844) callback\_fn, void \*cookie,

1297 const struct [k\_thread](structk__thread.md) \*thread, const struct [arch\_esf](structarch__esf.md) \*esf);

1298

1303

1304#ifdef \_\_cplusplus

1305}

1306#endif /\* \_\_cplusplus \*/

1307

1308#include <[zephyr/arch/arch\_inlines.h](arch__inlines_8h.md)>

1309

1310#endif /\* \_ASMLANGUAGE \*/

1311

1312#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARCH\_INTERFACE\_H\_ \*/

[syscall.h](arch_2syscall_8h.md)

[arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)

#define arch\_irq\_disable(irq)

**Definition** irq.h:107

[arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)

#define arch\_irq\_enable(irq)

**Definition** irq.h:106

[arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)

#define arch\_irq\_is\_enabled(irq)

**Definition** irq.h:109

[arch\_inlines.h](arch__inlines_8h.md)

[k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717)

void(\* k\_thread\_entry\_t)(void \*p1, void \*p2, void \*p3)

Thread entry point function type.

**Definition** arch\_interface.h:48

[arch\_spin\_relax](arch__interface_8h.md#a9932b29bc0c3b86e4f8cbd6708ef5d9c)

void arch\_spin\_relax(void)

Perform architecture specific processing within spin loops.

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:46

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[cpu.h](cpu_8h.md)

[arch\_gdb\_reg\_writeall](group__arch-gdbstub.md#ga0ef78d7e193e98549d9665632e53d5ca)

size\_t arch\_gdb\_reg\_writeall(struct gdb\_ctx \*ctx, uint8\_t \*hex, size\_t hexlen)

Take a hexadecimal string and update all registers.

[arch\_gdb\_init](group__arch-gdbstub.md#ga21c8a32d35c4d267b8306d595ff1d726)

void arch\_gdb\_init(void)

Architecture layer debug start.

[arch\_gdb\_step](group__arch-gdbstub.md#ga2aa577d5e55c8b739e2be6187336aaf0)

void arch\_gdb\_step(void)

Continue with one step.

[arch\_gdb\_reg\_readall](group__arch-gdbstub.md#ga5317106a8022bea2a0d42af0789cc016)

size\_t arch\_gdb\_reg\_readall(struct gdb\_ctx \*ctx, uint8\_t \*buf, size\_t buflen)

Read all registers, and outputs as hexadecimal string.

[arch\_gdb\_remove\_breakpoint](group__arch-gdbstub.md#ga734041433f69030ad98439d10ef56ad6)

int arch\_gdb\_remove\_breakpoint(struct gdb\_ctx \*ctx, uint8\_t type, uintptr\_t addr, uint32\_t kind)

Remove breakpoint or watchpoint.

[arch\_gdb\_continue](group__arch-gdbstub.md#ga9c130421feeee919651828511743b346)

void arch\_gdb\_continue(void)

Continue running program.

[arch\_gdb\_reg\_readone](group__arch-gdbstub.md#gaa3216e9f381f974c374a6399af5cdba5)

size\_t arch\_gdb\_reg\_readone(struct gdb\_ctx \*ctx, uint8\_t \*buf, size\_t buflen, uint32\_t regno)

Read one register, and outputs as hexadecimal string.

[arch\_gdb\_add\_breakpoint](group__arch-gdbstub.md#gab6f42110cf2340132bf2b3916810c01d)

int arch\_gdb\_add\_breakpoint(struct gdb\_ctx \*ctx, uint8\_t type, uintptr\_t addr, uint32\_t kind)

Add breakpoint or watchpoint.

[arch\_gdb\_reg\_writeone](group__arch-gdbstub.md#gad717b520d774294bbda78a56cddcaeff)

size\_t arch\_gdb\_reg\_writeone(struct gdb\_ctx \*ctx, uint8\_t \*hex, size\_t hexlen, uint32\_t regno)

Take a hexadecimal string and update one register.

[arch\_irq\_unlocked](group__arch-irq.md#ga1b827afafc622d412962f568b78726dc)

static bool arch\_irq\_unlocked(unsigned int key)

Test if calling arch\_irq\_unlock() with this key would unlock irqs.

[arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)

static unsigned int arch\_irq\_lock(void)

Lock interrupts on the current CPU.

[arch\_irq\_disconnect\_dynamic](group__arch-irq.md#ga41483a9fc1090d96d066e107a74ee38c)

int arch\_irq\_disconnect\_dynamic(unsigned int irq, unsigned int priority, void(\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)

Arch-specific hook to dynamically uninstall a shared interrupt.

[arch\_irq\_is\_used](group__arch-irq.md#ga5c85d7bf54a83190ed27587dc5a01de5)

bool arch\_irq\_is\_used(unsigned int irq)

Arch-specific hook for checking if an IRQ is being used already.

[arch\_irq\_set\_used](group__arch-irq.md#ga5f0942bd035c50c9d2d91ada472f37c4)

void arch\_irq\_set\_used(unsigned int irq)

Arch-specific hook for declaring an IRQ being used.

[arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)

static void arch\_irq\_unlock(unsigned int key)

Unlock interrupts on the current CPU.

[arch\_irq\_connect\_dynamic](group__arch-irq.md#gaa4d733913e12a12e104dc4781cca7308)

int arch\_irq\_connect\_dynamic(unsigned int irq, unsigned int priority, void(\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)

Arch-specific hook to install a dynamic interrupt.

[arch\_irq\_allocate](group__arch-irq.md#gaac8f60e7dfc5ce3222372798e96316ae)

unsigned int arch\_irq\_allocate(void)

Arch-specific hook for allocating IRQs.

[arch\_cpu\_atomic\_idle](group__arch-pm.md#ga4d0297717c23a3cc5df434549e26924d)

void arch\_cpu\_atomic\_idle(unsigned int key)

Atomically re-enable interrupts and enter low power mode.

[arch\_cpu\_idle](group__arch-pm.md#ga6ce051203e6cc091d0fb42a15f662a48)

void arch\_cpu\_idle(void)

Power save idle routine.

[arch\_num\_cpus](group__arch-smp.md#ga078e9bf1a4a557d1321ddc4848092cbe)

static unsigned int arch\_num\_cpus(void)

Returns the number of CPUs.

[arch\_cpu\_start](group__arch-smp.md#ga32b7e543ce51498200c368c39c900bc8)

void arch\_cpu\_start(int cpu\_num, k\_thread\_stack\_t \*stack, int sz, arch\_cpustart\_t fn, void \*arg)

Start a numbered CPU on a MP-capable system.

[arch\_cpustart\_t](group__arch-smp.md#ga4a9ac90ba7cc7c403472bfdaf3369ed2)

void(\* arch\_cpustart\_t)(void \*data)

Per-cpu entry function.

**Definition** arch\_interface.h:222

[arch\_cpu\_active](group__arch-smp.md#ga5a7f0198ee061551c300129bffe64717)

bool arch\_cpu\_active(int cpu\_num)

Return CPU power status.

[arch\_smp\_init](group__arch-smp.md#ga6ffc01f86f4541d1092ee4b277a07ac6)

int arch\_smp\_init(void)

[arch\_sched\_broadcast\_ipi](group__arch-smp.md#ga8fe90cec57c56993df14c0d545106ca3)

void arch\_sched\_broadcast\_ipi(void)

Broadcast an interrupt to all CPUs.

[arch\_curr\_cpu](group__arch-smp.md#gad42138d41dff6a4aad8abf7d77fcd8b2)

static struct \_cpu \* arch\_curr\_cpu(void)

Return the CPU struct for the currently executing CPU.

[arch\_proc\_id](group__arch-smp.md#gad628c89816128546501e3c26eaaf9dea)

static uint32\_t arch\_proc\_id(void)

Processor hardware ID.

[arch\_sched\_directed\_ipi](group__arch-smp.md#gadebac82c1ed0a8a08adb297738d2633e)

void arch\_sched\_directed\_ipi(uint32\_t cpu\_bitmap)

Direct IPIs to the specified CPUs.

[arch\_stack\_walk](group__arch-stackwalk.md#ga7129c254277cfa162cd9c5778a7662c2)

void arch\_stack\_walk(stack\_trace\_callback\_fn callback\_fn, void \*cookie, const struct k\_thread \*thread, const struct arch\_esf \*esf)

Architecture-specific function to walk the stack.

[stack\_trace\_callback\_fn](group__arch-stackwalk.md#gaec9949df614728aa6d677f9f1fafd844)

bool(\* stack\_trace\_callback\_fn)(void \*cookie, unsigned long addr)

stack\_trace\_callback\_fn - Callback for arch\_stack\_walk

**Definition** arch\_interface.h:1279

[arch\_k\_cycle\_get\_32](group__arch-timing.md#ga9ee9f897ec750957de45bf8d43349d5e)

static uint32\_t arch\_k\_cycle\_get\_32(void)

Obtain the current cycle count, in units specified by CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC.

[arch\_k\_cycle\_get\_64](group__arch-timing.md#gacc1ed8d949f694a1d39e389334caf971)

static uint64\_t arch\_k\_cycle\_get\_64(void)

As for arch\_k\_cycle\_get\_32(), but with a 64 bit return value.

[arch\_syscall\_invoke4](group__arch-userspace.md#ga0ba3ae2290827385b226ebdbf3de3b53)

static uintptr\_t arch\_syscall\_invoke4(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t arg3, uintptr\_t arg4, uintptr\_t call\_id)

Invoke a system call with 4 arguments.

[arch\_buffer\_validate](group__arch-userspace.md#ga13053a9233b86d5cd19dc3cea5804a16)

int arch\_buffer\_validate(const void \*addr, size\_t size, int write)

Check memory region permissions.

[arch\_user\_string\_nlen](group__arch-userspace.md#ga174c4f356fe315c523cefbf513858c9c)

size\_t arch\_user\_string\_nlen(const char \*s, size\_t maxsize, int \*err)

Safely take the length of a potentially bad string.

[arch\_syscall\_invoke2](group__arch-userspace.md#ga1e78f1022aaf10e88727b142b56d4ef0)

static uintptr\_t arch\_syscall\_invoke2(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t call\_id)

Invoke a system call with 2 arguments.

[arch\_cohere\_stacks](group__arch-userspace.md#ga306e9d0e5f8094cb75686f1c43d068a9)

static void arch\_cohere\_stacks(struct k\_thread \*old\_thread, void \*old\_switch\_handle, struct k\_thread \*new\_thread)

Ensure cache coherence prior to context switch.

**Definition** arch\_interface.h:938

[arch\_user\_mode\_enter](group__arch-userspace.md#ga447daa0454a90a7a3a247de01e522567)

FUNC\_NORETURN void arch\_user\_mode\_enter(k\_thread\_entry\_t user\_entry, void \*p1, void \*p2, void \*p3)

Perform a one-way transition from supervisor to user mode.

[arch\_virt\_region\_align](group__arch-userspace.md#ga48be2412ba65ec550ded63e2f1a0470f)

size\_t arch\_virt\_region\_align(uintptr\_t phys, size\_t size)

Get the optimal virtual region alignment to optimize the MMU table layout.

[arch\_syscall\_invoke1](group__arch-userspace.md#ga4cfb3b2b38e5afca889e8b9765d6c3df)

static uintptr\_t arch\_syscall\_invoke1(uintptr\_t arg1, uintptr\_t call\_id)

Invoke a system call with 1 argument.

[arch\_syscall\_invoke0](group__arch-userspace.md#ga5e9ab24b9c980e327903fbe3f5bd97f3)

static uintptr\_t arch\_syscall\_invoke0(uintptr\_t call\_id)

Invoke a system call with 0 arguments.

[arch\_mem\_domain\_max\_partitions\_get](group__arch-userspace.md#ga71542fcc679a94ad9ea60d7ac46da361)

int arch\_mem\_domain\_max\_partitions\_get(void)

Get the maximum number of partitions for a memory domain.

[arch\_is\_user\_context](group__arch-userspace.md#ga89ab53a218add419e37f89c1f5fd955f)

static bool arch\_is\_user\_context(void)

Indicate whether we are currently running in user mode.

[arch\_mem\_coherent](group__arch-userspace.md#ga8c6bb0f6730c115689452b016ac1761f)

static bool arch\_mem\_coherent(void \*ptr)

Detect memory coherence type.

**Definition** arch\_interface.h:890

[arch\_syscall\_invoke5](group__arch-userspace.md#ga9971c78bc8f579a0dadf84225dc0c3ff)

static uintptr\_t arch\_syscall\_invoke5(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t arg3, uintptr\_t arg4, uintptr\_t arg5, uintptr\_t call\_id)

Invoke a system call with 5 arguments.

[arch\_syscall\_invoke3](group__arch-userspace.md#gaacb1c66a1b7bf2293fea269f6b5e1c7e)

static uintptr\_t arch\_syscall\_invoke3(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t arg3, uintptr\_t call\_id)

Invoke a system call with 3 arguments.

[arch\_syscall\_invoke6](group__arch-userspace.md#gac6cae2197637993a86b6ec6803b5742b)

static uintptr\_t arch\_syscall\_invoke6(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t arg3, uintptr\_t arg4, uintptr\_t arg5, uintptr\_t arg6, uintptr\_t call\_id)

Invoke a system call with 6 arguments.

[arch\_syscall\_oops](group__arch-userspace.md#gad53908f229d7e2c333574b009493644b)

FUNC\_NORETURN void arch\_syscall\_oops(void \*ssf)

Induce a kernel oops that appears to come from a specific location.

[msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231)

struct msi\_vector msi\_vector\_t

**Definition** msi.h:60

[arch\_timing\_freq\_get](group__timing__api__arch.md#ga026409e1dc323ceddb82b2a6f1cc7ca2)

uint64\_t arch\_timing\_freq\_get(void)

Get frequency of counter used (in Hz).

[arch\_timing\_freq\_get\_mhz](group__timing__api__arch.md#ga1f7bfb9ce0588f3b423c2a63933d40eb)

uint32\_t arch\_timing\_freq\_get\_mhz(void)

Get frequency of counter used (in MHz).

[arch\_timing\_cycles\_get](group__timing__api__arch.md#ga44d3a7bd8b7008c9cd6c0524e97f128c)

uint64\_t arch\_timing\_cycles\_get(volatile timing\_t \*const start, volatile timing\_t \*const end)

Get number of cycles between start and end.

[arch\_timing\_stop](group__timing__api__arch.md#ga566483c64f5c5d2f0465e3f969303fd3)

void arch\_timing\_stop(void)

Signal the end of the timing information gathering.

[arch\_timing\_init](group__timing__api__arch.md#ga5d9923569b40437c28879ff4b3ff77c2)

void arch\_timing\_init(void)

Initialize the timing subsystem.

[arch\_timing\_cycles\_to\_ns](group__timing__api__arch.md#ga8424bc96c05dcae34b7ffd445e2916fe)

uint64\_t arch\_timing\_cycles\_to\_ns(uint64\_t cycles)

Convert number of cycles into nanoseconds.

[arch\_timing\_cycles\_to\_ns\_avg](group__timing__api__arch.md#ga925b4caff80f1dbac36531b479b24364)

uint64\_t arch\_timing\_cycles\_to\_ns\_avg(uint64\_t cycles, uint32\_t count)

Convert number of cycles into nanoseconds with averaging.

[arch\_timing\_counter\_get](group__timing__api__arch.md#gad7a709477650c8596a96fe080f583fdd)

timing\_t arch\_timing\_counter\_get(void)

Return timing counter.

[arch\_timing\_start](group__timing__api__arch.md#gaf8cd88e81c2104b5eb0fbe42967b7834)

void arch\_timing\_start(void)

Signal the start of the timing information gathering.

[types.h](include_2zephyr_2timing_2types_8h.md)

[timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2)

uint64\_t timing\_t

**Definition** types.h:10

[types.h](include_2zephyr_2types_8h.md)

[irq\_offload.h](irq__offload_8h.md)

IRQ Offload interface.

[irq\_offload\_routine\_t](irq__offload_8h.md#a5bcf9956ddbf5ea75619f0cef91e1214)

void(\* irq\_offload\_routine\_t)(const void \*parameter)

**Definition** irq\_offload.h:18

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[gdb\_ctx](structgdb__ctx.md)

Architecture specific GDB context.

**Definition** gdbstub.h:61

[k\_mem\_domain](structk__mem__domain.md)

Memory Domain.

**Definition** mem\_domain.h:80

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[msi\_vector](structmsi__vector.md)

**Definition** msi.h:51

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arch\_interface.h](arch__interface_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
