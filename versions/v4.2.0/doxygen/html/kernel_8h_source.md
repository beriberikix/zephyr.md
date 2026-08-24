---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/kernel_8h_source.html
original_path: doxygen/html/kernel_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kernel.h

[Go to the documentation of this file.](kernel_8h.md)

1/\*

2 \* Copyright (c) 2016, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_KERNEL\_H\_

14#define ZEPHYR\_INCLUDE\_KERNEL\_H\_

15

16#if !defined(\_ASMLANGUAGE)

17#include <[zephyr/kernel\_includes.h](kernel__includes_8h.md)>

18#include <[errno.h](errno_8h.md)>

19#include <[limits.h](limits_8h.md)>

20#include <[stdbool.h](stdbool_8h.md)>

21#include <[zephyr/toolchain.h](toolchain_8h.md)>

22#include <[zephyr/tracing/tracing\_macros.h](tracing__macros_8h.md)>

23#include <[zephyr/sys/mem\_stats.h](mem__stats_8h.md)>

24#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

25#include <[zephyr/sys/ring\_buffer.h](ring__buffer_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

31/\*

32 \* Zephyr currently assumes the size of a couple standard types to simplify

33 \* print string formats. Let's make sure this doesn't change without notice.

34 \*/

35BUILD\_ASSERT(sizeof([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)) == sizeof(int));

36BUILD\_ASSERT(sizeof([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)) == sizeof(long long));

37BUILD\_ASSERT(sizeof([intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c)) == sizeof(long));

38

47

[ 48](kernel_8h.md#ac627cc4c3da16be4b74f0a4ab036a603)#define K\_ANY NULL

49

50#if (CONFIG\_NUM\_COOP\_PRIORITIES + CONFIG\_NUM\_PREEMPT\_PRIORITIES) == 0

51#error Zero available thread priorities defined!

52#endif

53

[ 54](kernel_8h.md#ac145d4747518572acfc8ee1579007d54)#define K\_PRIO\_COOP(x) (-(CONFIG\_NUM\_COOP\_PRIORITIES - (x)))

[ 55](kernel_8h.md#aa0e916aae3ddd0e998cd41ac32afe30a)#define K\_PRIO\_PREEMPT(x) (x)

56

[ 57](kernel_8h.md#a5fd4365cb6e8742e750b5e4950fb1e47)#define K\_HIGHEST\_THREAD\_PRIO (-CONFIG\_NUM\_COOP\_PRIORITIES)

[ 58](kernel_8h.md#afa4bcc2fdfea5cd7c63d56f476b1b32f)#define K\_LOWEST\_THREAD\_PRIO CONFIG\_NUM\_PREEMPT\_PRIORITIES

[ 59](kernel_8h.md#a8f3f1d910dd847f0b223a4aa00788fa2)#define K\_IDLE\_PRIO K\_LOWEST\_THREAD\_PRIO

[ 60](kernel_8h.md#ab326c7eb1d248650e6017dcaee8d24b2)#define K\_HIGHEST\_APPLICATION\_THREAD\_PRIO (K\_HIGHEST\_THREAD\_PRIO)

[ 61](kernel_8h.md#ad4c2df561988fa1194c2f8c768d667cd)#define K\_LOWEST\_APPLICATION\_THREAD\_PRIO (K\_LOWEST\_THREAD\_PRIO - 1)

62

63#ifdef CONFIG\_POLL

64#define Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

65 .poll\_events = SYS\_DLIST\_STATIC\_INIT(&obj.poll\_events),

66#define Z\_DECL\_POLL\_EVENT sys\_dlist\_t poll\_events;

67#else

68#define Z\_POLL\_EVENT\_OBJ\_INIT(obj)

69#define Z\_DECL\_POLL\_EVENT

70#endif

71

72struct [k\_thread](structk__thread.md);

73struct [k\_mutex](structk__mutex.md);

74struct [k\_sem](structk__sem.md);

75struct [k\_msgq](structk__msgq.md);

76struct [k\_mbox](structk__mbox.md);

77struct [k\_pipe](structk__pipe.md);

78struct [k\_queue](structk__queue.md);

79struct [k\_fifo](structk__fifo.md);

80struct [k\_lifo](structk__lifo.md);

81struct k\_stack;

82struct k\_mem\_slab;

83struct k\_timer;

84struct [k\_poll\_event](structk__poll__event.md);

85struct [k\_poll\_signal](structk__poll__signal.md);

86struct [k\_mem\_domain](structk__mem__domain.md);

87struct [k\_mem\_partition](structk__mem__partition.md);

88struct [k\_futex](structk__futex.md);

89struct [k\_event](structk__event.md);

90

[ 91](kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779c)enum [execution\_context\_types](kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779c) {

[ 92](kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779ca30593044743695f8184a157283dac4d5) [K\_ISR](kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779ca30593044743695f8184a157283dac4d5) = 0,

[ 93](kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779ca62c0b731a1bb3c5e4aadeba3f93df58b) [K\_COOP\_THREAD](kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779ca62c0b731a1bb3c5e4aadeba3f93df58b),

[ 94](kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779cae84f57f4ac996c751d1f4c9e49789322) [K\_PREEMPT\_THREAD](kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779cae84f57f4ac996c751d1f4c9e49789322),

95};

96

97/\* private, used by k\_poll and k\_work\_poll \*/

98struct k\_work\_poll;

99typedef int (\*\_poller\_cb\_t)(struct [k\_poll\_event](structk__poll__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

100

105

[ 106](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75)typedef void (\*[k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75))(const struct [k\_thread](structk__thread.md) \*thread,

107 void \*user\_data);

108

[ 124](group__thread__apis.md#gae2596d56800769b06fc03c194a126a97)void [k\_thread\_foreach](group__thread__apis.md#gae2596d56800769b06fc03c194a126a97)([k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data);

125

144#ifdef CONFIG\_SMP

[ 145](group__thread__apis.md#ga82a83c2db36b34596dcb5afa5b28e41c)void [k\_thread\_foreach\_filter\_by\_cpu](group__thread__apis.md#ga82a83c2db36b34596dcb5afa5b28e41c)(unsigned int cpu,

146 [k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data);

147#else

148static inline

149void [k\_thread\_foreach\_filter\_by\_cpu](group__thread__apis.md#ga82a83c2db36b34596dcb5afa5b28e41c)(unsigned int cpu,

150 [k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data)

151{

152 \_\_ASSERT(cpu == 0, "cpu filter out of bounds");

153 ARG\_UNUSED(cpu);

154 [k\_thread\_foreach](group__thread__apis.md#gae2596d56800769b06fc03c194a126a97)(user\_cb, user\_data);

155}

156#endif

157

[ 185](group__thread__apis.md#ga30ef8b445a6c1b4a82651674dbb737fc)void [k\_thread\_foreach\_unlocked](group__thread__apis.md#ga30ef8b445a6c1b4a82651674dbb737fc)(

186 [k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data);

187

219#ifdef CONFIG\_SMP

[ 220](group__thread__apis.md#gad908a1b9014aa048cf12997804ab7be2)void [k\_thread\_foreach\_unlocked\_filter\_by\_cpu](group__thread__apis.md#gad908a1b9014aa048cf12997804ab7be2)(unsigned int cpu,

221 [k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data);

222#else

223static inline

224void [k\_thread\_foreach\_unlocked\_filter\_by\_cpu](group__thread__apis.md#gad908a1b9014aa048cf12997804ab7be2)(unsigned int cpu,

225 [k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data)

226{

227 \_\_ASSERT(cpu == 0, "cpu filter out of bounds");

228 ARG\_UNUSED(cpu);

229 [k\_thread\_foreach\_unlocked](group__thread__apis.md#ga30ef8b445a6c1b4a82651674dbb737fc)(user\_cb, user\_data);

230}

231#endif

232

234

240

241#endif /\* !\_ASMLANGUAGE \*/

242

243

244/\*

245 \* Thread user options. May be needed by assembly code. Common part uses low

246 \* bits, arch-specific use high bits.

247 \*/

248

[ 252](group__thread__apis.md#gad503fbcca905a9266b0e154e3ded258c)#define K\_ESSENTIAL (BIT(0))

253

[ 254](group__thread__apis.md#ga4b2378312ea9b410be025b40e8d6a395)#define K\_FP\_IDX 1

[ 264](group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951)#define K\_FP\_REGS (BIT(K\_FP\_IDX))

265

[ 272](group__thread__apis.md#gacb5340339892f22301e02697c6039ccc)#define K\_USER (BIT(2))

273

[ 282](group__thread__apis.md#gaa1788a413a055745d1de71b4da7c2eb2)#define K\_INHERIT\_PERMS (BIT(3))

283

[ 293](group__thread__apis.md#gacbdb579370978fe07e4a863a84bd8bee)#define K\_CALLBACK\_STATE (BIT(4))

294

[ 304](group__thread__apis.md#gacbd163e5bc79fc0282def5ff4321fa30)#define K\_DSP\_IDX 6

[ 305](group__thread__apis.md#ga8e1aeb428a418ed23e17448b796363cb)#define K\_DSP\_REGS (BIT(K\_DSP\_IDX))

306

[ 315](group__thread__apis.md#gab01cfd20675ebef8f5e81d7d17e6babb)#define K\_AGU\_IDX 7

[ 316](group__thread__apis.md#ga718088c1a68f03fffa960164cab60b72)#define K\_AGU\_REGS (BIT(K\_AGU\_IDX))

317

[ 327](group__thread__apis.md#gaa5b7de51b26773aa4485a711a041d9a7)#define K\_SSE\_REGS (BIT(7))

328

329/\* end - thread options \*/

330

331#if !defined(\_ASMLANGUAGE)

[ 356](group__thread__apis.md#gafe00cc70bac8a47ba6dda21bde508614)\_\_syscall [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[k\_thread\_stack\_alloc](group__thread__apis.md#gafe00cc70bac8a47ba6dda21bde508614)(size\_t size, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

357

[ 370](group__thread__apis.md#ga95560cb85f6656b981a9a50ff2cd70b7)\_\_syscall int [k\_thread\_stack\_free](group__thread__apis.md#ga95560cb85f6656b981a9a50ff2cd70b7)([k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack);

371

[ 423](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367)\_\_syscall [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_thread\_create](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367)(struct [k\_thread](structk__thread.md) \*new\_thread,

424 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack,

425 size\_t stack\_size,

426 [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) [entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03),

427 void \*p1, void \*p2, void \*p3,

428 int prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) options, [k\_timeout\_t](structk__timeout__t.md) delay);

429

[ 451](group__thread__apis.md#ga3fbe1c8a5f3ef1c25382c7d6fca35764)FUNC\_NORETURN void [k\_thread\_user\_mode\_enter](group__thread__apis.md#ga3fbe1c8a5f3ef1c25382c7d6fca35764)([k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) [entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03),

452 void \*p1, void \*p2,

453 void \*p3);

454

[ 468](group__thread__apis.md#gafec540511e6d2e0a074a5bfb515c53b0)#define k\_thread\_access\_grant(thread, ...) \

469 FOR\_EACH\_FIXED\_ARG(k\_object\_access\_grant, (;), (thread), \_\_VA\_ARGS\_\_)

470

[ 485](group__thread__apis.md#ga3f46c06833add2a2e0ddb7242f06702c)static inline void [k\_thread\_heap\_assign](group__thread__apis.md#ga3f46c06833add2a2e0ddb7242f06702c)(struct [k\_thread](structk__thread.md) \*thread,

486 struct [k\_heap](structk__heap.md) \*heap)

487{

488 thread->[resource\_pool](structk__thread.md#a35b859bded3a270f25ccc40efece7583) = heap;

489}

490

491#if defined(CONFIG\_INIT\_STACKS) && defined(CONFIG\_THREAD\_STACK\_INFO)

512\_\_syscall int k\_thread\_stack\_space\_get(const struct [k\_thread](structk__thread.md) \*thread,

513 size\_t \*unused\_ptr);

514#endif

515

516#if (K\_HEAP\_MEM\_POOL\_SIZE > 0)

529void k\_thread\_system\_pool\_assign(struct [k\_thread](structk__thread.md) \*thread);

530#endif /\* (K\_HEAP\_MEM\_POOL\_SIZE > 0) \*/

531

[ 551](group__thread__apis.md#ga40a733561eb1f64dcaae0e01b167d233)\_\_syscall int [k\_thread\_join](group__thread__apis.md#ga40a733561eb1f64dcaae0e01b167d233)(struct [k\_thread](structk__thread.md) \*thread, [k\_timeout\_t](structk__timeout__t.md) timeout);

552

[ 566](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)([k\_timeout\_t](structk__timeout__t.md) timeout);

567

[ 579](group__thread__apis.md#ga51307cdfe153ab3e918b18755d97c5d9)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_msleep](group__thread__apis.md#ga51307cdfe153ab3e918b18755d97c5d9)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ms)

580{

581 return [k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)(Z\_TIMEOUT\_MS(ms));

582}

583

[ 600](group__thread__apis.md#gaeac56bb072ce295b9fdc372ab8cee67e)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_usleep](group__thread__apis.md#gaeac56bb072ce295b9fdc372ab8cee67e)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) us);

601

[ 618](group__thread__apis.md#ga550b642e071480323e589866abb99c22)\_\_syscall void [k\_busy\_wait](group__thread__apis.md#ga550b642e071480323e589866abb99c22)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usec\_to\_wait);

619

[ 631](group__thread__apis.md#ga366b9daa0be65b0a69dbc9f146064b68)bool [k\_can\_yield](group__thread__apis.md#ga366b9daa0be65b0a69dbc9f146064b68)(void);

632

[ 640](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)\_\_syscall void [k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)(void);

641

[ 651](group__thread__apis.md#ga9275a019c8ff3c7fe49a81f8c078157e)\_\_syscall void [k\_wakeup](group__thread__apis.md#ga9275a019c8ff3c7fe49a81f8c078157e)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

652

666\_\_attribute\_const\_\_

[ 667](group__thread__apis.md#gac3b994b90b5bccded0895304f6b20c5d)\_\_syscall [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_sched\_current\_thread\_query](group__thread__apis.md#gac3b994b90b5bccded0895304f6b20c5d)(void);

668

675\_\_attribute\_const\_\_

[ 676](group__thread__apis.md#ga7ef1ed0fb9513df8096ede1e52fc76b2)static inline [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_current\_get](group__thread__apis.md#ga7ef1ed0fb9513df8096ede1e52fc76b2)(void)

677{

678#ifdef CONFIG\_CURRENT\_THREAD\_USE\_TLS

679

680 /\* Thread-local cache of current thread ID, set in z\_thread\_entry() \*/

681 extern Z\_THREAD\_LOCAL [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) z\_tls\_current;

682

683 return z\_tls\_current;

684#else

685 return [k\_sched\_current\_thread\_query](group__thread__apis.md#gac3b994b90b5bccded0895304f6b20c5d)();

686#endif

687}

688

[ 708](group__thread__apis.md#ga1f44bb0307bea7a97227764ecd7bf963)\_\_syscall void [k\_thread\_abort](group__thread__apis.md#ga1f44bb0307bea7a97227764ecd7bf963)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

709

710[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_timeout\_expires(const struct \_timeout \*timeout);

711[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_timeout\_remaining(const struct \_timeout \*timeout);

712

713#ifdef CONFIG\_SYS\_CLOCK\_EXISTS

714

[ 722](group__thread__apis.md#gab0b1c85b847fe74170c04538fa9949ff)\_\_syscall [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_thread\_timeout\_expires\_ticks](group__thread__apis.md#gab0b1c85b847fe74170c04538fa9949ff)(const struct [k\_thread](structk__thread.md) \*thread);

723

724static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_impl\_k\_thread\_timeout\_expires\_ticks(

725 const struct [k\_thread](structk__thread.md) \*thread)

726{

727 return z\_timeout\_expires(&thread->[base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8).timeout);

728}

729

[ 737](group__thread__apis.md#ga4688c095c86e037a18594efdb9a5e9b9)\_\_syscall [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_thread\_timeout\_remaining\_ticks](group__thread__apis.md#ga4688c095c86e037a18594efdb9a5e9b9)(const struct [k\_thread](structk__thread.md) \*thread);

738

739static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_impl\_k\_thread\_timeout\_remaining\_ticks(

740 const struct [k\_thread](structk__thread.md) \*thread)

741{

742 return z\_timeout\_remaining(&thread->[base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8).timeout);

743}

744

745#endif /\* CONFIG\_SYS\_CLOCK\_EXISTS \*/

746

750

751struct \_static\_thread\_data {

752 struct k\_thread \*init\_thread;

753 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*init\_stack;

754 unsigned int init\_stack\_size;

755 [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) init\_entry;

756 void \*init\_p1;

757 void \*init\_p2;

758 void \*init\_p3;

759 int init\_prio;

760 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) init\_options;

761 const char \*init\_name;

762#ifdef CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME

763 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) init\_delay\_ms;

764#else

765 k\_timeout\_t init\_delay;

766#endif

767};

768

769#ifdef CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME

770#define Z\_THREAD\_INIT\_DELAY\_INITIALIZER(ms) .init\_delay\_ms = (ms)

771#define Z\_THREAD\_INIT\_DELAY(thread) SYS\_TIMEOUT\_MS((thread)->init\_delay\_ms)

772#else

773#define Z\_THREAD\_INIT\_DELAY\_INITIALIZER(ms) .init\_delay = SYS\_TIMEOUT\_MS\_INIT(ms)

774#define Z\_THREAD\_INIT\_DELAY(thread) (thread)->init\_delay

775#endif

776

777#define Z\_THREAD\_INITIALIZER(thread, stack, stack\_size, \

778 entry, p1, p2, p3, \

779 prio, options, delay, tname) \

780 { \

781 .init\_thread = (thread), \

782 .init\_stack = (stack), \

783 .init\_stack\_size = (stack\_size), \

784 .init\_entry = (k\_thread\_entry\_t)entry, \

785 .init\_p1 = (void \*)p1, \

786 .init\_p2 = (void \*)p2, \

787 .init\_p3 = (void \*)p3, \

788 .init\_prio = (prio), \

789 .init\_options = (options), \

790 .init\_name = STRINGIFY(tname), \

791 Z\_THREAD\_INIT\_DELAY\_INITIALIZER(delay) \

792 }

793

794/\*

795 \* Refer to K\_THREAD\_DEFINE() and K\_KERNEL\_THREAD\_DEFINE() for

796 \* information on arguments.

797 \*/

798#define Z\_THREAD\_COMMON\_DEFINE(name, stack\_size, \

799 entry, p1, p2, p3, \

800 prio, options, delay) \

801 struct k\_thread \_k\_thread\_obj\_##name; \

802 STRUCT\_SECTION\_ITERABLE(\_static\_thread\_data, \

803 \_k\_thread\_data\_##name) = \

804 Z\_THREAD\_INITIALIZER(&\_k\_thread\_obj\_##name, \

805 \_k\_thread\_stack\_##name, stack\_size,\

806 entry, p1, p2, p3, prio, options, \

807 delay, name); \

808 const k\_tid\_t name = (k\_tid\_t)&\_k\_thread\_obj\_##name

809

813

[ 845](group__thread__apis.md#gab3ced58648ca35788a40676e8478ecd2)#define K\_THREAD\_DEFINE(name, stack\_size, \

846 entry, p1, p2, p3, \

847 prio, options, delay) \

848 K\_THREAD\_STACK\_DEFINE(\_k\_thread\_stack\_##name, stack\_size); \

849 Z\_THREAD\_COMMON\_DEFINE(name, stack\_size, entry, p1, p2, p3, \

850 prio, options, delay)

851

[ 882](group__thread__apis.md#gae25853424ec969f8431862c46b3ec294)#define K\_KERNEL\_THREAD\_DEFINE(name, stack\_size, \

883 entry, p1, p2, p3, \

884 prio, options, delay) \

885 K\_KERNEL\_STACK\_DEFINE(\_k\_thread\_stack\_##name, stack\_size); \

886 Z\_THREAD\_COMMON\_DEFINE(name, stack\_size, entry, p1, p2, p3, \

887 prio, options, delay)

888

[ 898](group__thread__apis.md#ga3a46ed8ad2c3b12416fafe11325f82b3)\_\_syscall int [k\_thread\_priority\_get](group__thread__apis.md#ga3a46ed8ad2c3b12416fafe11325f82b3)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

899

[ 925](group__thread__apis.md#ga24e50a60c524d1eb22fe21cdf269b6a6)\_\_syscall void [k\_thread\_priority\_set](group__thread__apis.md#ga24e50a60c524d1eb22fe21cdf269b6a6)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int prio);

926

927

928#ifdef CONFIG\_SCHED\_DEADLINE

[ 961](group__thread__apis.md#gad887f16c1dd6f3247682a83beb22d1ce)\_\_syscall void [k\_thread\_deadline\_set](group__thread__apis.md#gad887f16c1dd6f3247682a83beb22d1ce)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int deadline);

962#endif

963

[ 982](group__thread__apis.md#gad82575e576cd08906fbc68fe36be48bd)\_\_syscall void [k\_reschedule](group__thread__apis.md#gad82575e576cd08906fbc68fe36be48bd)(void);

983

984#ifdef CONFIG\_SCHED\_CPU\_MASK

[ 997](group__thread__apis.md#ga80b9c58df6600c7e79f16756c128f44c)int [k\_thread\_cpu\_mask\_clear](group__thread__apis.md#ga80b9c58df6600c7e79f16756c128f44c)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

998

[ 1011](group__thread__apis.md#gaedcfeb0964ae72611791241580b2119d)int [k\_thread\_cpu\_mask\_enable\_all](group__thread__apis.md#gaedcfeb0964ae72611791241580b2119d)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

1012

[ 1025](group__thread__apis.md#ga306587604a7496db8059bd395fd90fc0)int [k\_thread\_cpu\_mask\_enable](group__thread__apis.md#ga306587604a7496db8059bd395fd90fc0)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu);

1026

[ 1039](group__thread__apis.md#ga89e6c07ac112da75b2ef115d1a557d44)int [k\_thread\_cpu\_mask\_disable](group__thread__apis.md#ga89e6c07ac112da75b2ef115d1a557d44)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu);

1040

[ 1051](group__thread__apis.md#gae9ebd9845e14ed02944ab9282a185c03)int [k\_thread\_cpu\_pin](group__thread__apis.md#gae9ebd9845e14ed02944ab9282a185c03)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu);

1052#endif

1053

[ 1075](group__thread__apis.md#ga66cf8682fb65870eceb5e57d667a8d4e)\_\_syscall void [k\_thread\_suspend](group__thread__apis.md#ga66cf8682fb65870eceb5e57d667a8d4e)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

1076

[ 1088](group__thread__apis.md#ga117b26f8569ec3045ead1fad1851663d)\_\_syscall void [k\_thread\_resume](group__thread__apis.md#ga117b26f8569ec3045ead1fad1851663d)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

1089

[ 1103](group__thread__apis.md#gac539268e0b45c600315a6567ec27f965)static inline void [k\_thread\_start](group__thread__apis.md#gac539268e0b45c600315a6567ec27f965)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread)

1104{

1105 [k\_wakeup](group__thread__apis.md#ga9275a019c8ff3c7fe49a81f8c078157e)(thread);

1106}

1107

[ 1134](group__thread__apis.md#ga877c1bfeffbf8f097d1656f9e10a66e8)void [k\_sched\_time\_slice\_set](group__thread__apis.md#ga877c1bfeffbf8f097d1656f9e10a66e8)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) slice, int prio);

1135

[ 1174](group__thread__apis.md#ga563928f292a4134acd4142029b60e631)void [k\_thread\_time\_slice\_set](group__thread__apis.md#ga563928f292a4134acd4142029b60e631)(struct [k\_thread](structk__thread.md) \*th, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) slice\_ticks,

1175 [k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f) expired, void \*data);

1176

1178

1183

[ 1195](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)bool [k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)(void);

1196

[ 1213](group__isr__apis.md#ga91e1cf0dc7fc93a3214cadb74ed86666)\_\_syscall int [k\_is\_preempt\_thread](group__isr__apis.md#ga91e1cf0dc7fc93a3214cadb74ed86666)(void);

1214

[ 1226](group__isr__apis.md#gae74e5de996276df767b96d4b50fa47ea)static inline bool [k\_is\_pre\_kernel](group__isr__apis.md#gae74e5de996276df767b96d4b50fa47ea)(void)

1227{

1228 extern bool z\_sys\_post\_kernel; /\* in init.c \*/

1229

1230 return !z\_sys\_post\_kernel;

1231}

1232

1236

1241

[ 1267](group__thread__apis.md#ga4f0c5d0b9f279b12a4ad97db0c116a5f)void [k\_sched\_lock](group__thread__apis.md#ga4f0c5d0b9f279b12a4ad97db0c116a5f)(void);

1268

[ 1276](group__thread__apis.md#ga7b26f64523cc4c36522cc828ccf85580)void [k\_sched\_unlock](group__thread__apis.md#ga7b26f64523cc4c36522cc828ccf85580)(void);

1277

[ 1290](group__thread__apis.md#ga4834d9b81ed60c00eee77b0d4f8ab9e4)\_\_syscall void [k\_thread\_custom\_data\_set](group__thread__apis.md#ga4834d9b81ed60c00eee77b0d4f8ab9e4)(void \*value);

1291

[ 1299](group__thread__apis.md#ga19af063cff7b306ba28062996922740d)\_\_syscall void \*[k\_thread\_custom\_data\_get](group__thread__apis.md#ga19af063cff7b306ba28062996922740d)(void);

1300

[ 1314](group__thread__apis.md#ga23107333f134b9c9a8b692374211e841)\_\_syscall int [k\_thread\_name\_set](group__thread__apis.md#ga23107333f134b9c9a8b692374211e841)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, const char \*str);

1315

[ 1324](group__thread__apis.md#gadebf45da56dee393164569742459dc0a)const char \*[k\_thread\_name\_get](group__thread__apis.md#gadebf45da56dee393164569742459dc0a)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

1325

[ 1337](group__thread__apis.md#ga07b59ade055c69929ccdc08a14361794)\_\_syscall int [k\_thread\_name\_copy](group__thread__apis.md#ga07b59ade055c69929ccdc08a14361794)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, char \*buf,

1338 size\_t size);

1339

[ 1352](group__thread__apis.md#ga0c6af32096dc7ca391ffe2522bae4cb6)const char \*[k\_thread\_state\_str](group__thread__apis.md#ga0c6af32096dc7ca391ffe2522bae4cb6)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread\_id, char \*buf, size\_t buf\_size);

1353

1357

1362

[ 1371](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)#define K\_NO\_WAIT Z\_TIMEOUT\_NO\_WAIT

1372

[ 1385](group__clock__apis.md#gae2f3a80170afc5fbce0337cdf5a4ce4c)#define K\_NSEC(t) Z\_TIMEOUT\_NS(t)

1386

[ 1399](group__clock__apis.md#ga91198e325210ec052a8308e642058c0b)#define K\_USEC(t) Z\_TIMEOUT\_US(t)

1400

[ 1411](group__clock__apis.md#gab41f59fd2b724cb1279e4f6821154b33)#define K\_CYC(t) Z\_TIMEOUT\_CYC(t)

1412

[ 1423](group__clock__apis.md#gaeda983960bd25f1dba7a386ad720e395)#define K\_TICKS(t) Z\_TIMEOUT\_TICKS(t)

1424

[ 1435](group__clock__apis.md#ga302af954e87b10a9b731f1ad07775e9f)#define K\_MSEC(ms) Z\_TIMEOUT\_MS(ms)

1436

[ 1447](group__clock__apis.md#gadc361472aea59267f6ea38f5e7c7ca2a)#define K\_SECONDS(s) K\_MSEC((s) \* MSEC\_PER\_SEC)

1448

[ 1459](group__clock__apis.md#gaef02f20d4d2ebfc9aa29acae01bd3698)#define K\_MINUTES(m) K\_SECONDS((m) \* 60)

1460

[ 1471](group__clock__apis.md#gaa9e0cd890db28965b66d4bc5d719a91f)#define K\_HOURS(h) K\_MINUTES((h) \* 60)

1472

[ 1481](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)#define K\_FOREVER Z\_FOREVER

1482

1483#ifdef CONFIG\_TIMEOUT\_64BIT

1484

1496#define K\_TIMEOUT\_ABS\_TICKS(t) \

1497 Z\_TIMEOUT\_TICKS(Z\_TICK\_ABS((k\_ticks\_t)CLAMP(t, 0, (INT64\_MAX - 1))))

1498

1510#define K\_TIMEOUT\_ABS\_SEC(t) K\_TIMEOUT\_ABS\_TICKS(k\_sec\_to\_ticks\_ceil64(t))

1511

1523#define K\_TIMEOUT\_ABS\_MS(t) K\_TIMEOUT\_ABS\_TICKS(k\_ms\_to\_ticks\_ceil64(t))

1524

1537#define K\_TIMEOUT\_ABS\_US(t) K\_TIMEOUT\_ABS\_TICKS(k\_us\_to\_ticks\_ceil64(t))

1538

1551#define K\_TIMEOUT\_ABS\_NS(t) K\_TIMEOUT\_ABS\_TICKS(k\_ns\_to\_ticks\_ceil64(t))

1552

1565#define K\_TIMEOUT\_ABS\_CYC(t) K\_TIMEOUT\_ABS\_TICKS(k\_cyc\_to\_ticks\_ceil64(t))

1566

1567#endif

1568

1572

1576

1577struct k\_timer {

1578 /\*

1579 \* \_timeout structure must be first here if we want to use

1580 \* dynamic timer allocation. timeout.node is used in the double-linked

1581 \* list of free timers

1582 \*/

1583 struct \_timeout timeout;

1584

1585 /\* wait queue for the (single) thread waiting on this timer \*/

1586 \_wait\_q\_t wait\_q;

1587

1588 /\* runs in ISR context \*/

1589 void (\*expiry\_fn)(struct k\_timer \*timer);

1590

1591 /\* runs in the context of the thread that calls k\_timer\_stop() \*/

1592 void (\*stop\_fn)(struct k\_timer \*timer);

1593

1594 /\* timer period \*/

1595 [k\_timeout\_t](structk__timeout__t.md) period;

1596

1597 /\* timer status \*/

1598 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status;

1599

1600 /\* user-specific data, also used to support legacy features \*/

1601 void \*user\_data;

1602

1603 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_timer)

1604

1605#ifdef CONFIG\_OBJ\_CORE\_TIMER

1606 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

1607#endif

1608};

1609

1610#define Z\_TIMER\_INITIALIZER(obj, expiry, stop) \

1611 { \

1612 .timeout = { \

1613 .node = {},\

1614 .fn = z\_timer\_expiration\_handler, \

1615 .dticks = 0, \

1616 }, \

1617 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

1618 .expiry\_fn = expiry, \

1619 .stop\_fn = stop, \

1620 .period = {}, \

1621 .status = 0, \

1622 .user\_data = 0, \

1623 }

1624

1628

1634

[ 1645](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde)typedef void (\*[k\_timer\_expiry\_t](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde))(struct k\_timer \*timer);

1646

[ 1661](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c)typedef void (\*[k\_timer\_stop\_t](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c))(struct k\_timer \*timer);

1662

[ 1674](group__timer__apis.md#gaa267fcb0a2e18cd0da29e9f9612510a6)#define K\_TIMER\_DEFINE(name, expiry\_fn, stop\_fn) \

1675 STRUCT\_SECTION\_ITERABLE(k\_timer, name) = \

1676 Z\_TIMER\_INITIALIZER(name, expiry\_fn, stop\_fn)

1677

[ 1687](group__timer__apis.md#ga318c846a740b901e5d56876a47ad7f61)void [k\_timer\_init](group__timer__apis.md#ga318c846a740b901e5d56876a47ad7f61)(struct k\_timer \*timer,

1688 [k\_timer\_expiry\_t](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde) expiry\_fn,

1689 [k\_timer\_stop\_t](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c) stop\_fn);

1690

[ 1705](group__timer__apis.md#ga3ba70e9f059ff52fd2057ab89ea7f2ee)\_\_syscall void [k\_timer\_start](group__timer__apis.md#ga3ba70e9f059ff52fd2057ab89ea7f2ee)(struct k\_timer \*timer,

1706 [k\_timeout\_t](structk__timeout__t.md) duration, [k\_timeout\_t](structk__timeout__t.md) period);

1707

[ 1724](group__timer__apis.md#ga8d3e3356a10d36570e16f7920e4c8772)\_\_syscall void [k\_timer\_stop](group__timer__apis.md#ga8d3e3356a10d36570e16f7920e4c8772)(struct k\_timer \*timer);

1725

[ 1738](group__timer__apis.md#gad532f4834cd4cf8be27b089e6ea347ce)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_timer\_status\_get](group__timer__apis.md#gad532f4834cd4cf8be27b089e6ea347ce)(struct k\_timer \*timer);

1739

[ 1757](group__timer__apis.md#ga81d6d95b7021e26ad4cab161318e04f2)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_timer\_status\_sync](group__timer__apis.md#ga81d6d95b7021e26ad4cab161318e04f2)(struct k\_timer \*timer);

1758

1759#ifdef CONFIG\_SYS\_CLOCK\_EXISTS

1760

[ 1771](group__timer__apis.md#ga022b4cf5c8d0ee21b6a3b04fd425533f)\_\_syscall [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_timer\_expires\_ticks](group__timer__apis.md#ga022b4cf5c8d0ee21b6a3b04fd425533f)(const struct k\_timer \*timer);

1772

1773static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_impl\_k\_timer\_expires\_ticks(

1774 const struct k\_timer \*timer)

1775{

1776 return z\_timeout\_expires(&timer->timeout);

1777}

1778

[ 1789](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4)\_\_syscall [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_timer\_remaining\_ticks](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4)(const struct k\_timer \*timer);

1790

1791static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_impl\_k\_timer\_remaining\_ticks(

1792 const struct k\_timer \*timer)

1793{

1794 return z\_timeout\_remaining(&timer->timeout);

1795}

1796

[ 1807](group__timer__apis.md#ga6c6d8b0aa59bfa0f5924e95ccf756259)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_timer\_remaining\_get](group__timer__apis.md#ga6c6d8b0aa59bfa0f5924e95ccf756259)(struct k\_timer \*timer)

1808{

1809 return [k\_ticks\_to\_ms\_floor32](group__timeutil__unit__apis.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)([k\_timer\_remaining\_ticks](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4)(timer));

1810}

1811

1812#endif /\* CONFIG\_SYS\_CLOCK\_EXISTS \*/

1813

[ 1826](group__timer__apis.md#gadba1884961e790dd9c5d567de91cc7e2)\_\_syscall void [k\_timer\_user\_data\_set](group__timer__apis.md#gadba1884961e790dd9c5d567de91cc7e2)(struct k\_timer \*timer, void \*user\_data);

1827

1831static inline void z\_impl\_k\_timer\_user\_data\_set(struct k\_timer \*timer,

1832 void \*user\_data)

1833{

1834 timer->user\_data = user\_data;

1835}

1836

[ 1844](group__timer__apis.md#ga19a7d99a01a83828efd7f0d3bf2dd358)\_\_syscall void \*[k\_timer\_user\_data\_get](group__timer__apis.md#ga19a7d99a01a83828efd7f0d3bf2dd358)(const struct k\_timer \*timer);

1845

1846static inline void \*z\_impl\_k\_timer\_user\_data\_get(const struct k\_timer \*timer)

1847{

1848 return timer->user\_data;

1849}

1850

1852

1858

[ 1868](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)\_\_syscall [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)(void);

1869

[ 1883](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)(void)

1884{

1885 return [k\_ticks\_to\_ms\_floor64](group__timeutil__unit__apis.md#gac417ab53d5d493d95e24e7f777f8a4e0)([k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)());

1886}

1887

[ 1907](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_uptime\_get\_32](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b)(void)

1908{

1909 return ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)();

1910}

1911

[ 1920](group__clock__apis.md#gae082928ea608a8b180b4cb3a79d21a24)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_uptime\_seconds](group__clock__apis.md#gae082928ea608a8b180b4cb3a79d21a24)(void)

1921{

1922 return [k\_ticks\_to\_sec\_floor32](group__timeutil__unit__apis.md#ga824ffc9857fa2d4bccb3a9f4a56b8f18)([k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)());

1923}

1924

[ 1936](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [k\_uptime\_delta](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80)([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*reftime)

1937{

1938 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) uptime, delta;

1939

1940 uptime = [k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)();

1941 delta = uptime - \*reftime;

1942 \*reftime = uptime;

1943

1944 return delta;

1945}

1946

[ 1955](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)(void)

1956{

1957 return [arch\_k\_cycle\_get\_32](arc_2v2_2misc_8h.md#a9ee9f897ec750957de45bf8d43349d5e)();

1958}

1959

[ 1970](group__clock__apis.md#gae09f509d02bf75a7b45d2800d823bb3a)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [k\_cycle\_get\_64](group__clock__apis.md#gae09f509d02bf75a7b45d2800d823bb3a)(void)

1971{

1972 if (![IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_TIMER\_HAS\_64BIT\_CYCLE\_COUNTER)) {

1973 \_\_ASSERT(0, "64-bit cycle counter not enabled on this platform. "

1974 "See CONFIG\_TIMER\_HAS\_64BIT\_CYCLE\_COUNTER");

1975 return 0;

1976 }

1977

1978 return [arch\_k\_cycle\_get\_64](arc_2v2_2misc_8h.md#acc1ed8d949f694a1d39e389334caf971)();

1979}

1980

1984

[ 1985](structk__queue.md)struct [k\_queue](structk__queue.md) {

[ 1986](structk__queue.md#a892371af9701ce67619e38446bc2ceae) [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) [data\_q](structk__queue.md#a892371af9701ce67619e38446bc2ceae);

[ 1987](structk__queue.md#a18fd165fec722384b3748bfdf3332a4c) struct [k\_spinlock](structk__spinlock.md) [lock](structk__queue.md#a18fd165fec722384b3748bfdf3332a4c);

[ 1988](structk__queue.md#a871d734f2b21a9cad3ca4a2ba79e64f1) \_wait\_q\_t [wait\_q](structk__queue.md#a871d734f2b21a9cad3ca4a2ba79e64f1);

1989

1990 Z\_DECL\_POLL\_EVENT

1991

1992 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_queue](structk__queue.md))

1993};

1994

1998

1999#define Z\_QUEUE\_INITIALIZER(obj) \

2000 { \

2001 .data\_q = SYS\_SFLIST\_STATIC\_INIT(&obj.data\_q), \

2002 .lock = { }, \

2003 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

2004 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

2005 }

2006

2010

2016

[ 2024](group__queue__apis.md#ga0236222d42768c2bf00942f328146c21)\_\_syscall void [k\_queue\_init](group__queue__apis.md#ga0236222d42768c2bf00942f328146c21)(struct [k\_queue](structk__queue.md) \*queue);

2025

[ 2039](group__queue__apis.md#ga7c39d86cc6509f59ff9223cac3ea5071)\_\_syscall void [k\_queue\_cancel\_wait](group__queue__apis.md#ga7c39d86cc6509f59ff9223cac3ea5071)(struct [k\_queue](structk__queue.md) \*queue);

2040

[ 2053](group__queue__apis.md#gaa84522a5ace6e7f8ba61033baca6972f)void [k\_queue\_append](group__queue__apis.md#gaa84522a5ace6e7f8ba61033baca6972f)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2054

[ 2071](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_queue\_alloc\_append](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2072

[ 2085](group__queue__apis.md#ga8ce013d8a037d4be5078797e0050e9c6)void [k\_queue\_prepend](group__queue__apis.md#ga8ce013d8a037d4be5078797e0050e9c6)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2086

[ 2103](group__queue__apis.md#gacf3dba40125073c11075e5a134919f88)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_queue\_alloc\_prepend](group__queue__apis.md#gacf3dba40125073c11075e5a134919f88)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2104

[ 2118](group__queue__apis.md#gad47336f27e433a52600a3b67ab89556a)void [k\_queue\_insert](group__queue__apis.md#gad47336f27e433a52600a3b67ab89556a)(struct [k\_queue](structk__queue.md) \*queue, void \*prev, void \*data);

2119

[ 2138](group__queue__apis.md#ga91d1a144fc2aeb3dd655accc94ca43aa)int [k\_queue\_append\_list](group__queue__apis.md#ga91d1a144fc2aeb3dd655accc94ca43aa)(struct [k\_queue](structk__queue.md) \*queue, void \*head, void \*tail);

2139

[ 2155](group__queue__apis.md#ga4eee0da7442d60572b05d60a9996e69d)int [k\_queue\_merge\_slist](group__queue__apis.md#ga4eee0da7442d60572b05d60a9996e69d)(struct [k\_queue](structk__queue.md) \*queue, [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list);

2156

[ 2174](group__queue__apis.md#ga0a77d8556e7d253319275de034f01619)\_\_syscall void \*[k\_queue\_get](group__queue__apis.md#ga0a77d8556e7d253319275de034f01619)(struct [k\_queue](structk__queue.md) \*queue, [k\_timeout\_t](structk__timeout__t.md) timeout);

2175

[ 2192](group__queue__apis.md#ga4bff929ed1d366a06e00865a5bbe2544)bool [k\_queue\_remove](group__queue__apis.md#ga4bff929ed1d366a06e00865a5bbe2544)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2193

[ 2208](group__queue__apis.md#ga287a2d81e2e3041be1cd45164e72f127)bool [k\_queue\_unique\_append](group__queue__apis.md#ga287a2d81e2e3041be1cd45164e72f127)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2209

[ 2223](group__queue__apis.md#gadb2bb8088868b3c5801c72b320389ca9)\_\_syscall int [k\_queue\_is\_empty](group__queue__apis.md#gadb2bb8088868b3c5801c72b320389ca9)(struct [k\_queue](structk__queue.md) \*queue);

2224

2225static inline int z\_impl\_k\_queue\_is\_empty(struct [k\_queue](structk__queue.md) \*queue)

2226{

2227 return [sys\_sflist\_is\_empty](group__flagged-single-linked-list__apis.md#ga039ad5d35670e5d18acb38a174258a7e)(&queue->[data\_q](structk__queue.md#a892371af9701ce67619e38446bc2ceae)) ? 1 : 0;

2228}

2229

[ 2239](group__queue__apis.md#ga8ccd5137690c127a0f7d67619b88a52b)\_\_syscall void \*[k\_queue\_peek\_head](group__queue__apis.md#ga8ccd5137690c127a0f7d67619b88a52b)(struct [k\_queue](structk__queue.md) \*queue);

2240

[ 2250](group__queue__apis.md#ga27a460c42836d8b093ad9274c14bb176)\_\_syscall void \*[k\_queue\_peek\_tail](group__queue__apis.md#ga27a460c42836d8b093ad9274c14bb176)(struct [k\_queue](structk__queue.md) \*queue);

2251

[ 2261](group__queue__apis.md#gacd0bc309f0147d4669f65fafa87e0e70)#define K\_QUEUE\_DEFINE(name) \

2262 STRUCT\_SECTION\_ITERABLE(k\_queue, name) = \

2263 Z\_QUEUE\_INITIALIZER(name)

2264

2266

2267#ifdef CONFIG\_USERSPACE

[ 2277](structk__futex.md)struct [k\_futex](structk__futex.md) {

[ 2278](structk__futex.md#a454ad1b595b899306c8e9c8e1431e7a7) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [val](structk__futex.md#a454ad1b595b899306c8e9c8e1431e7a7);

2279};

2280

2288struct z\_futex\_data {

2289 \_wait\_q\_t wait\_q;

2290 struct [k\_spinlock](structk__spinlock.md) lock;

2291};

2292

2293#define Z\_FUTEX\_DATA\_INITIALIZER(obj) \

2294 { \

2295 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q) \

2296 }

2297

2303

[ 2323](group__futex__apis.md#ga596bfa265f88567ad9e80fd38cd433d3)\_\_syscall int [k\_futex\_wait](group__futex__apis.md#ga596bfa265f88567ad9e80fd38cd433d3)(struct [k\_futex](structk__futex.md) \*futex, int expected,

2324 [k\_timeout\_t](structk__timeout__t.md) timeout);

2325

[ 2340](group__futex__apis.md#ga62de1aeb7c5c273aed20d0e05336d7a0)\_\_syscall int [k\_futex\_wake](group__futex__apis.md#ga62de1aeb7c5c273aed20d0e05336d7a0)(struct [k\_futex](structk__futex.md) \*futex, bool wake\_all);

2341

2343#endif

2344

2350

2355

[ 2356](structk__event.md)struct [k\_event](structk__event.md) {

[ 2357](structk__event.md#a5bacd5f2d34da646d9d7ee229842e432) \_wait\_q\_t [wait\_q](structk__event.md#a5bacd5f2d34da646d9d7ee229842e432);

[ 2358](structk__event.md#a54c6f5997132e88406ffa5bcc0a10b83) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [events](structk__event.md#a54c6f5997132e88406ffa5bcc0a10b83);

[ 2359](structk__event.md#a1f0de9c69f29ad854f3b0d510ceb1efc) struct [k\_spinlock](structk__spinlock.md) [lock](structk__event.md#a1f0de9c69f29ad854f3b0d510ceb1efc);

2360

2361 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_event](structk__event.md))

2362

2363#ifdef CONFIG\_OBJ\_CORE\_EVENT

2364 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2365#endif

2366

2367};

2368

2369#define Z\_EVENT\_INITIALIZER(obj) \

2370 { \

2371 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

2372 .events = 0, \

2373 .lock = {}, \

2374 }

2375

[ 2383](group__event__apis.md#gacf803590b39b095056f2b1c5090c4019)\_\_syscall void [k\_event\_init](group__event__apis.md#gacf803590b39b095056f2b1c5090c4019)(struct [k\_event](structk__event.md) \*event);

2384

[ 2402](group__event__apis.md#gac88d17410a71642a903890e420d23d76)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_post](group__event__apis.md#gac88d17410a71642a903890e420d23d76)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events);

2403

[ 2421](group__event__apis.md#gac22e9d768d003246e68b4b0b64e60f49)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_set](group__event__apis.md#gac22e9d768d003246e68b4b0b64e60f49)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events);

2422

[ 2439](group__event__apis.md#ga29b3ec1022b12a8c34884da3559c5864)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_set\_masked](group__event__apis.md#ga29b3ec1022b12a8c34884da3559c5864)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events,

2440 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events\_mask);

2441

[ 2454](group__event__apis.md#gad6bfd7bfd0587bc70d3aa0b988010376)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_clear](group__event__apis.md#gad6bfd7bfd0587bc70d3aa0b988010376)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events);

2455

[ 2480](group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_wait](group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events,

2481 bool reset, [k\_timeout\_t](structk__timeout__t.md) timeout);

2482

[ 2507](group__event__apis.md#gaddd60a99de5ac3d84f643c9433b744c1)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_wait\_all](group__event__apis.md#gaddd60a99de5ac3d84f643c9433b744c1)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events,

2508 bool reset, [k\_timeout\_t](structk__timeout__t.md) timeout);

2509

[ 2520](group__event__apis.md#ga81e66be0959e8cb0414d9772056a6264)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_test](group__event__apis.md#ga81e66be0959e8cb0414d9772056a6264)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events\_mask)

2521{

2522 return [k\_event\_wait](group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753)(event, events\_mask, false, [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f));

2523}

2524

[ 2534](group__event__apis.md#ga093449cc6686d3235944f3faad284893)#define K\_EVENT\_DEFINE(name) \

2535 STRUCT\_SECTION\_ITERABLE(k\_event, name) = \

2536 Z\_EVENT\_INITIALIZER(name);

2537

2539

[ 2540](structk__fifo.md)struct [k\_fifo](structk__fifo.md) {

2541 struct [k\_queue](structk__queue.md) \_queue;

2542#ifdef CONFIG\_OBJ\_CORE\_FIFO

2543 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2544#endif

2545};

2546

2550#define Z\_FIFO\_INITIALIZER(obj) \

2551 { \

2552 .\_queue = Z\_QUEUE\_INITIALIZER(obj.\_queue) \

2553 }

2554

2558

2564

[ 2572](group__fifo__apis.md#gaeebf6ef54d4be61e19408f44a734a159)#define k\_fifo\_init(fifo) \

2573 ({ \

2574 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, init, fifo); \

2575 k\_queue\_init(&(fifo)->\_queue); \

2576 K\_OBJ\_CORE\_INIT(K\_OBJ\_CORE(fifo), \_obj\_type\_fifo); \

2577 K\_OBJ\_CORE\_LINK(K\_OBJ\_CORE(fifo)); \

2578 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, init, fifo); \

2579 })

2580

[ 2592](group__fifo__apis.md#gab744080af449e093df8dd4982e013e16)#define k\_fifo\_cancel\_wait(fifo) \

2593 ({ \

2594 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, cancel\_wait, fifo); \

2595 k\_queue\_cancel\_wait(&(fifo)->\_queue); \

2596 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, cancel\_wait, fifo); \

2597 })

2598

[ 2611](group__fifo__apis.md#ga3addb10f86f19e245c23362433d5c913)#define k\_fifo\_put(fifo, data) \

2612 ({ \

2613 void \*\_data = data; \

2614 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, put, fifo, \_data); \

2615 k\_queue\_append(&(fifo)->\_queue, \_data); \

2616 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, put, fifo, \_data); \

2617 })

2618

[ 2635](group__fifo__apis.md#gab1c5212040d12cbb92cede5cf54928ba)#define k\_fifo\_alloc\_put(fifo, data) \

2636 ({ \

2637 void \*\_data = data; \

2638 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, alloc\_put, fifo, \_data); \

2639 int fap\_ret = k\_queue\_alloc\_append(&(fifo)->\_queue, \_data); \

2640 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, alloc\_put, fifo, \_data, fap\_ret); \

2641 fap\_ret; \

2642 })

2643

[ 2658](group__fifo__apis.md#ga1bf5f52290c83e54ba14358cbbb4051b)#define k\_fifo\_put\_list(fifo, head, tail) \

2659 ({ \

2660 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, put\_list, fifo, head, tail); \

2661 k\_queue\_append\_list(&(fifo)->\_queue, head, tail); \

2662 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, put\_list, fifo, head, tail); \

2663 })

2664

[ 2678](group__fifo__apis.md#ga4cdc286a7a6f0d43acab63a4846815e7)#define k\_fifo\_put\_slist(fifo, list) \

2679 ({ \

2680 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, put\_slist, fifo, list); \

2681 k\_queue\_merge\_slist(&(fifo)->\_queue, list); \

2682 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, put\_slist, fifo, list); \

2683 })

2684

[ 2702](group__fifo__apis.md#ga1e2c480e2124116af97e94e7b4435de6)#define k\_fifo\_get(fifo, timeout) \

2703 ({ \

2704 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, get, fifo, timeout); \

2705 void \*fg\_ret = k\_queue\_get(&(fifo)->\_queue, timeout); \

2706 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, get, fifo, timeout, fg\_ret); \

2707 fg\_ret; \

2708 })

2709

[ 2723](group__fifo__apis.md#gab7cec4adc128ed1fd2d194ba6cd8c640)#define k\_fifo\_is\_empty(fifo) \

2724 k\_queue\_is\_empty(&(fifo)->\_queue)

2725

[ 2739](group__fifo__apis.md#ga2e0c8608f095a929740fa94c94a4f389)#define k\_fifo\_peek\_head(fifo) \

2740 ({ \

2741 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, peek\_head, fifo); \

2742 void \*fph\_ret = k\_queue\_peek\_head(&(fifo)->\_queue); \

2743 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, peek\_head, fifo, fph\_ret); \

2744 fph\_ret; \

2745 })

2746

[ 2758](group__fifo__apis.md#gafbe2ce9a6437b886cf149016187ba92f)#define k\_fifo\_peek\_tail(fifo) \

2759 ({ \

2760 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, peek\_tail, fifo); \

2761 void \*fpt\_ret = k\_queue\_peek\_tail(&(fifo)->\_queue); \

2762 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, peek\_tail, fifo, fpt\_ret); \

2763 fpt\_ret; \

2764 })

2765

[ 2775](group__fifo__apis.md#ga230b02a526ecb0ae1598be75cb9a8274)#define K\_FIFO\_DEFINE(name) \

2776 STRUCT\_SECTION\_ITERABLE(k\_fifo, name) = \

2777 Z\_FIFO\_INITIALIZER(name)

2778

2780

[ 2781](structk__lifo.md)struct [k\_lifo](structk__lifo.md) {

2782 struct [k\_queue](structk__queue.md) \_queue;

2783#ifdef CONFIG\_OBJ\_CORE\_LIFO

2784 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2785#endif

2786};

2787

2791

2792#define Z\_LIFO\_INITIALIZER(obj) \

2793 { \

2794 .\_queue = Z\_QUEUE\_INITIALIZER(obj.\_queue) \

2795 }

2796

2800

2806

[ 2814](group__lifo__apis.md#ga69fb19716a9014f7de79f8e524d64a3e)#define k\_lifo\_init(lifo) \

2815 ({ \

2816 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_lifo, init, lifo); \

2817 k\_queue\_init(&(lifo)->\_queue); \

2818 K\_OBJ\_CORE\_INIT(K\_OBJ\_CORE(lifo), \_obj\_type\_lifo); \

2819 K\_OBJ\_CORE\_LINK(K\_OBJ\_CORE(lifo)); \

2820 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_lifo, init, lifo); \

2821 })

2822

[ 2835](group__lifo__apis.md#gad662e36b1df8b9013e2dc61f9dfe3a8b)#define k\_lifo\_put(lifo, data) \

2836 ({ \

2837 void \*\_data = data; \

2838 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_lifo, put, lifo, \_data); \

2839 k\_queue\_prepend(&(lifo)->\_queue, \_data); \

2840 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_lifo, put, lifo, \_data); \

2841 })

2842

[ 2859](group__lifo__apis.md#ga96d885a6a36fcfcb5eaa65898eee0965)#define k\_lifo\_alloc\_put(lifo, data) \

2860 ({ \

2861 void \*\_data = data; \

2862 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_lifo, alloc\_put, lifo, \_data); \

2863 int lap\_ret = k\_queue\_alloc\_prepend(&(lifo)->\_queue, \_data); \

2864 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_lifo, alloc\_put, lifo, \_data, lap\_ret); \

2865 lap\_ret; \

2866 })

2867

[ 2885](group__lifo__apis.md#gad5f1775947b07a2a77f667aa9e41db5a)#define k\_lifo\_get(lifo, timeout) \

2886 ({ \

2887 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_lifo, get, lifo, timeout); \

2888 void \*lg\_ret = k\_queue\_get(&(lifo)->\_queue, timeout); \

2889 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_lifo, get, lifo, timeout, lg\_ret); \

2890 lg\_ret; \

2891 })

2892

[ 2902](group__lifo__apis.md#gaebd450d4181f22491623ea0aed6ee576)#define K\_LIFO\_DEFINE(name) \

2903 STRUCT\_SECTION\_ITERABLE(k\_lifo, name) = \

2904 Z\_LIFO\_INITIALIZER(name)

2905

2907

2911#define K\_STACK\_FLAG\_ALLOC ((uint8\_t)1) /\* Buffer was allocated \*/

2912

2913typedef [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) stack\_data\_t;

2914

2915struct k\_stack {

2916 \_wait\_q\_t wait\_q;

2917 struct [k\_spinlock](structk__spinlock.md) lock;

2918 stack\_data\_t \*base, \*next, \*top;

2919

2920 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

2921

2922 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_stack)

2923

2924#ifdef CONFIG\_OBJ\_CORE\_STACK

2925 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2926#endif

2927};

2928

2929#define Z\_STACK\_INITIALIZER(obj, stack\_buffer, stack\_num\_entries) \

2930 { \

2931 .wait\_q = Z\_WAIT\_Q\_INIT(&(obj).wait\_q), \

2932 .base = (stack\_buffer), \

2933 .next = (stack\_buffer), \

2934 .top = (stack\_buffer) + (stack\_num\_entries), \

2935 }

2936

2940

2946

[ 2956](group__stack__apis.md#ga4400a39ef48289305cf66a092d5c6c7d)void [k\_stack\_init](group__stack__apis.md#ga4400a39ef48289305cf66a092d5c6c7d)(struct k\_stack \*stack,

2957 stack\_data\_t \*buffer, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_entries);

2958

2959

2973

[ 2974](group__stack__apis.md#gab97d924db1aef3f6adade156a107d45c)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_stack\_alloc\_init](group__stack__apis.md#gab97d924db1aef3f6adade156a107d45c)(struct k\_stack \*stack,

2975 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_entries);

2976

[ 2988](group__stack__apis.md#ga819f4e7b2cf11cf2e1b80933fdcb67ea)int [k\_stack\_cleanup](group__stack__apis.md#ga819f4e7b2cf11cf2e1b80933fdcb67ea)(struct k\_stack \*stack);

2989

[ 3003](group__stack__apis.md#gaa6180f4db6ec93ee84149cba054d3e53)\_\_syscall int [k\_stack\_push](group__stack__apis.md#gaa6180f4db6ec93ee84149cba054d3e53)(struct k\_stack \*stack, stack\_data\_t data);

3004

[ 3025](group__stack__apis.md#ga36ce6ceb9ea3d5c36d22b10430789480)\_\_syscall int [k\_stack\_pop](group__stack__apis.md#ga36ce6ceb9ea3d5c36d22b10430789480)(struct k\_stack \*stack, stack\_data\_t \*data,

3026 [k\_timeout\_t](structk__timeout__t.md) timeout);

3027

[ 3038](group__stack__apis.md#ga8c9ca77e5de3c9757dcd4ecb55797835)#define K\_STACK\_DEFINE(name, stack\_num\_entries) \

3039 stack\_data\_t \_\_noinit \

3040 \_k\_stack\_buf\_##name[stack\_num\_entries]; \

3041 STRUCT\_SECTION\_ITERABLE(k\_stack, name) = \

3042 Z\_STACK\_INITIALIZER(name, \_k\_stack\_buf\_##name, \

3043 stack\_num\_entries)

3044

3046

3050

3051struct [k\_work](structk__work.md);

3052struct [k\_work\_q](structk__work__q.md);

3053struct [k\_work\_queue\_config](structk__work__queue__config.md);

3054extern struct [k\_work\_q](structk__work__q.md) k\_sys\_work\_q;

3055

3059

3065

[ 3070](structk__mutex.md)struct [k\_mutex](structk__mutex.md) {

[ 3072](structk__mutex.md#a4add234295bceff22551ee74f3aed802) \_wait\_q\_t [wait\_q](structk__mutex.md#a4add234295bceff22551ee74f3aed802);

[ 3074](structk__mutex.md#af910bb07dc99e50078de26fccca468e4) struct [k\_thread](structk__thread.md) \*[owner](structk__mutex.md#af910bb07dc99e50078de26fccca468e4);

3075

[ 3077](structk__mutex.md#a0db401fc8e03e1f984b8fd15af974718) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lock\_count](structk__mutex.md#a0db401fc8e03e1f984b8fd15af974718);

3078

[ 3080](structk__mutex.md#ab0d16fac9f8af960a501ffd93ec08c80) int [owner\_orig\_prio](structk__mutex.md#ab0d16fac9f8af960a501ffd93ec08c80);

3081

3082 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_mutex](structk__mutex.md))

3083

3084#ifdef CONFIG\_OBJ\_CORE\_MUTEX

3085 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

3086#endif

3087};

3088

3092#define Z\_MUTEX\_INITIALIZER(obj) \

3093 { \

3094 .wait\_q = Z\_WAIT\_Q\_INIT(&(obj).wait\_q), \

3095 .owner = NULL, \

3096 .lock\_count = 0, \

3097 .owner\_orig\_prio = K\_LOWEST\_APPLICATION\_THREAD\_PRIO, \

3098 }

3099

3103

[ 3113](group__mutex__apis.md#gab6f3d98fabbdc0918bbc9934d61d63f3)#define K\_MUTEX\_DEFINE(name) \

3114 STRUCT\_SECTION\_ITERABLE(k\_mutex, name) = \

3115 Z\_MUTEX\_INITIALIZER(name)

3116

[ 3129](group__mutex__apis.md#ga56b64952fb8b78b00268a21c28b41480)\_\_syscall int [k\_mutex\_init](group__mutex__apis.md#ga56b64952fb8b78b00268a21c28b41480)(struct [k\_mutex](structk__mutex.md) \*mutex);

3130

3131

[ 3153](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)\_\_syscall int [k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(struct [k\_mutex](structk__mutex.md) \*mutex, [k\_timeout\_t](structk__timeout__t.md) timeout);

3154

[ 3175](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)\_\_syscall int [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(struct [k\_mutex](structk__mutex.md) \*mutex);

3176

3180

3181

[ 3182](structk__condvar.md)struct [k\_condvar](structk__condvar.md) {

[ 3183](structk__condvar.md#a14b457a06420f093e779d569f4fea906) \_wait\_q\_t [wait\_q](structk__condvar.md#a14b457a06420f093e779d569f4fea906);

3184

3185#ifdef CONFIG\_OBJ\_CORE\_CONDVAR

3186 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

3187#endif

3188};

3189

3190#define Z\_CONDVAR\_INITIALIZER(obj) \

3191 { \

3192 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

3193 }

3194

3200

[ 3207](group__condvar__apis.md#gac9b497c56cc4642965afa6c0c6d7ecfc)\_\_syscall int [k\_condvar\_init](group__condvar__apis.md#gac9b497c56cc4642965afa6c0c6d7ecfc)(struct [k\_condvar](structk__condvar.md) \*condvar);

3208

[ 3215](group__condvar__apis.md#ga0376a8f7dc6e4f1e1eed55940f43015b)\_\_syscall int [k\_condvar\_signal](group__condvar__apis.md#ga0376a8f7dc6e4f1e1eed55940f43015b)(struct [k\_condvar](structk__condvar.md) \*condvar);

3216

[ 3224](group__condvar__apis.md#gad2e46a7b9e1bc934fd1f5cb38dde40d8)\_\_syscall int [k\_condvar\_broadcast](group__condvar__apis.md#gad2e46a7b9e1bc934fd1f5cb38dde40d8)(struct [k\_condvar](structk__condvar.md) \*condvar);

3225

[ 3243](group__condvar__apis.md#gab2e1d05db4f954755f430ca894e44dbc)\_\_syscall int [k\_condvar\_wait](group__condvar__apis.md#gab2e1d05db4f954755f430ca894e44dbc)(struct [k\_condvar](structk__condvar.md) \*condvar, struct [k\_mutex](structk__mutex.md) \*mutex,

3244 [k\_timeout\_t](structk__timeout__t.md) timeout);

3245

[ 3256](group__condvar__apis.md#ga770816651e25f7e7dae992a0b2260c21)#define K\_CONDVAR\_DEFINE(name) \

3257 STRUCT\_SECTION\_ITERABLE(k\_condvar, name) = \

3258 Z\_CONDVAR\_INITIALIZER(name)

3259

3262

3268

[ 3275](structk__sem.md)struct [k\_sem](structk__sem.md) {

3279 \_wait\_q\_t wait\_q;

3280 unsigned int count;

3281 unsigned int limit;

3282

3283 Z\_DECL\_POLL\_EVENT

3284

3285 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_sem](structk__sem.md))

3286

3287#ifdef CONFIG\_OBJ\_CORE\_SEM

3288 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

3289#endif

3291};

3292

3296

3297#define Z\_SEM\_INITIALIZER(obj, initial\_count, count\_limit) \

3298 { \

3299 .wait\_q = Z\_WAIT\_Q\_INIT(&(obj).wait\_q), \

3300 .count = (initial\_count), \

3301 .limit = (count\_limit), \

3302 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

3303 }

3304

3308

[ 3317](group__semaphore__apis.md#ga689359a77a0cebe737ef644c188f7e57)#define K\_SEM\_MAX\_LIMIT UINT\_MAX

3318

[ 3334](group__semaphore__apis.md#gadcd0e6cfba3392fb887222eafe4c1845)\_\_syscall int [k\_sem\_init](group__semaphore__apis.md#gadcd0e6cfba3392fb887222eafe4c1845)(struct [k\_sem](structk__sem.md) \*sem, unsigned int initial\_count,

3335 unsigned int limit);

3336

[ 3355](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)\_\_syscall int [k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)(struct [k\_sem](structk__sem.md) \*sem, [k\_timeout\_t](structk__timeout__t.md) timeout);

3356

[ 3367](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)\_\_syscall void [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)(struct [k\_sem](structk__sem.md) \*sem);

3368

[ 3378](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)\_\_syscall void [k\_sem\_reset](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)(struct [k\_sem](structk__sem.md) \*sem);

3379

[ 3389](group__semaphore__apis.md#ga58843b581e170a1811fc38eecbfd01f3)\_\_syscall unsigned int [k\_sem\_count\_get](group__semaphore__apis.md#ga58843b581e170a1811fc38eecbfd01f3)(struct [k\_sem](structk__sem.md) \*sem);

3390

3394static inline unsigned int z\_impl\_k\_sem\_count\_get(struct [k\_sem](structk__sem.md) \*sem)

3395{

3396 return sem->count;

3397}

3398

[ 3410](group__semaphore__apis.md#ga018a8aa43e02e704deee7b6341502946)#define K\_SEM\_DEFINE(name, initial\_count, count\_limit) \

3411 STRUCT\_SECTION\_ITERABLE(k\_sem, name) = \

3412 Z\_SEM\_INITIALIZER(name, initial\_count, count\_limit); \

3413 BUILD\_ASSERT(((count\_limit) != 0) && \

3414 (((initial\_count) < (count\_limit)) || ((initial\_count) == (count\_limit))) && \

3415 ((count\_limit) <= K\_SEM\_MAX\_LIMIT));

3416

3418

3422

3423struct [k\_work\_delayable](structk__work__delayable.md);

3424struct [k\_work\_sync](structk__work__sync.md);

3425

3429

3435

[ 3442](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda)typedef void (\*[k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda))(struct [k\_work](structk__work.md) \*work);

3443

[ 3457](group__workqueue__apis.md#gaf20080884a2893d39cd8e862b34a2a30)void [k\_work\_init](group__workqueue__apis.md#gaf20080884a2893d39cd8e862b34a2a30)(struct [k\_work](structk__work.md) \*work,

3458 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) [handler](structk__work.md#a096d6ca1338fb0fbfa330b790136f172));

3459

[ 3474](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b)int [k\_work\_busy\_get](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b)(const struct [k\_work](structk__work.md) \*work);

3475

3489static inline bool [k\_work\_is\_pending](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)(const struct [k\_work](structk__work.md) \*work);

3490

[ 3511](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c)int [k\_work\_submit\_to\_queue](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137),

3512 struct [k\_work](structk__work.md) \*work);

3513

[ 3522](group__workqueue__apis.md#gace61b59575093d7442f39ccb7be686d7)int [k\_work\_submit](group__workqueue__apis.md#gace61b59575093d7442f39ccb7be686d7)(struct [k\_work](structk__work.md) \*work);

3523

[ 3548](group__workqueue__apis.md#gabd1cda459bab538fb2d6dfd84a73b253)bool [k\_work\_flush](group__workqueue__apis.md#gabd1cda459bab538fb2d6dfd84a73b253)(struct [k\_work](structk__work.md) \*work,

3549 struct [k\_work\_sync](structk__work__sync.md) \*sync);

3550

[ 3570](group__workqueue__apis.md#ga389fe2a8fb20f9bd593cf8d990727078)int [k\_work\_cancel](group__workqueue__apis.md#ga389fe2a8fb20f9bd593cf8d990727078)(struct [k\_work](structk__work.md) \*work);

3571

[ 3602](group__workqueue__apis.md#gab2b05cfe3af08f7d32c3946fa1c808f9)bool [k\_work\_cancel\_sync](group__workqueue__apis.md#gab2b05cfe3af08f7d32c3946fa1c808f9)(struct [k\_work](structk__work.md) \*work, struct [k\_work\_sync](structk__work__sync.md) \*sync);

3603

[ 3613](group__workqueue__apis.md#gada77d818ea9e4d07c14a960872ed5492)void [k\_work\_queue\_init](group__workqueue__apis.md#gada77d818ea9e4d07c14a960872ed5492)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137));

3614

[ 3634](group__workqueue__apis.md#gadfc56554f9bfe7b52309d79660188593)void [k\_work\_queue\_start](group__workqueue__apis.md#gadfc56554f9bfe7b52309d79660188593)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137),

3635 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, size\_t stack\_size,

3636 int prio, const struct [k\_work\_queue\_config](structk__work__queue__config.md) \*cfg);

3637

[ 3648](group__workqueue__apis.md#gac7fc60238574769e4eae6a2cc38da87b)void [k\_work\_queue\_run](group__workqueue__apis.md#gac7fc60238574769e4eae6a2cc38da87b)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137), const struct [k\_work\_queue\_config](structk__work__queue__config.md) \*cfg);

3649

3659static inline [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_work\_queue\_thread\_get](group__workqueue__apis.md#ga0b8b496f7e7bd82d08590a07293e38d7)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137));

3660

[ 3684](group__workqueue__apis.md#ga0fefe3e0225ac99b47b250849f6cd863)int [k\_work\_queue\_drain](group__workqueue__apis.md#ga0fefe3e0225ac99b47b250849f6cd863)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137), bool plug);

3685

[ 3699](group__workqueue__apis.md#gaa0463bb79af3ec470f7d3be02052139f)int [k\_work\_queue\_unplug](group__workqueue__apis.md#gaa0463bb79af3ec470f7d3be02052139f)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137));

3700

[ 3715](group__workqueue__apis.md#ga1fd2fce94eb731ccb0838ec763e62f5c)int [k\_work\_queue\_stop](group__workqueue__apis.md#ga1fd2fce94eb731ccb0838ec763e62f5c)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137), [k\_timeout\_t](structk__timeout__t.md) timeout);

3716

[ 3730](group__workqueue__apis.md#ga2876c5d82fb2340a093bc4d689a55465)void [k\_work\_init\_delayable](group__workqueue__apis.md#ga2876c5d82fb2340a093bc4d689a55465)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3731 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) [handler](structk__work.md#a096d6ca1338fb0fbfa330b790136f172));

3732

3744static inline struct [k\_work\_delayable](structk__work__delayable.md) \*

3745[k\_work\_delayable\_from\_work](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca)(struct [k\_work](structk__work.md) \*[work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629));

3746

[ 3760](group__workqueue__apis.md#ga1b76969667844f0981d348c9c671bc9f)int [k\_work\_delayable\_busy\_get](group__workqueue__apis.md#ga1b76969667844f0981d348c9c671bc9f)(const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3761

3776static inline bool [k\_work\_delayable\_is\_pending](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e)(

3777 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3778

3792static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_work\_delayable\_expires\_get](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624)(

3793 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3794

3808static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_work\_delayable\_remaining\_get](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4)(

3809 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3810

[ 3838](group__workqueue__apis.md#ga17f863c9f6ff2fb41dc0f3b7de4fdf23)int [k\_work\_schedule\_for\_queue](group__workqueue__apis.md#ga17f863c9f6ff2fb41dc0f3b7de4fdf23)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4),

3839 struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3840 [k\_timeout\_t](structk__timeout__t.md) delay);

3841

[ 3855](group__workqueue__apis.md#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)int [k\_work\_schedule](group__workqueue__apis.md#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3856 [k\_timeout\_t](structk__timeout__t.md) delay);

3857

[ 3893](group__workqueue__apis.md#gabf5db091eac19b19a4e12c0cb381f0a8)int [k\_work\_reschedule\_for\_queue](group__workqueue__apis.md#gabf5db091eac19b19a4e12c0cb381f0a8)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4),

3894 struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3895 [k\_timeout\_t](structk__timeout__t.md) delay);

3896

[ 3909](group__workqueue__apis.md#gaacaab408fb7c848d466ad1f069dfa648)int [k\_work\_reschedule](group__workqueue__apis.md#gaacaab408fb7c848d466ad1f069dfa648)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3910 [k\_timeout\_t](structk__timeout__t.md) delay);

3911

[ 3936](group__workqueue__apis.md#gad47d54e513030304be2600d75b1a965f)bool [k\_work\_flush\_delayable](group__workqueue__apis.md#gad47d54e513030304be2600d75b1a965f)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3937 struct [k\_work\_sync](structk__work__sync.md) \*sync);

3938

[ 3959](group__workqueue__apis.md#ga92355914ee178d4c3e848a1946bed3e4)int [k\_work\_cancel\_delayable](group__workqueue__apis.md#ga92355914ee178d4c3e848a1946bed3e4)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3960

[ 3989](group__workqueue__apis.md#ga7e7ec237648556fc16bfda8d35f7cd86)bool [k\_work\_cancel\_delayable\_sync](group__workqueue__apis.md#ga7e7ec237648556fc16bfda8d35f7cd86)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3990 struct [k\_work\_sync](structk__work__sync.md) \*sync);

3991

3992enum {

3996

3997 /\* The atomic API is used for all work and queue flags fields to

3998 \* enforce sequential consistency in SMP environments.

3999 \*/

4000

4001 /\* Bits that represent the work item states. At least nine of the

4002 \* combinations are distinct valid stable states.

4003 \*/

4004 K\_WORK\_RUNNING\_BIT = 0,

4005 K\_WORK\_CANCELING\_BIT = 1,

4006 K\_WORK\_QUEUED\_BIT = 2,

4007 K\_WORK\_DELAYED\_BIT = 3,

4008 K\_WORK\_FLUSHING\_BIT = 4,

4009

4010 K\_WORK\_MASK = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_DELAYED\_BIT) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUED\_BIT)

4011 | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_RUNNING\_BIT) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_CANCELING\_BIT) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_FLUSHING\_BIT),

4012

4013 /\* Static work flags \*/

4014 K\_WORK\_DELAYABLE\_BIT = 8,

4015 K\_WORK\_DELAYABLE = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_DELAYABLE\_BIT),

4016

4017 /\* Dynamic work queue flags \*/

4018 K\_WORK\_QUEUE\_STARTED\_BIT = 0,

4019 K\_WORK\_QUEUE\_STARTED = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_STARTED\_BIT),

4020 K\_WORK\_QUEUE\_BUSY\_BIT = 1,

4021 K\_WORK\_QUEUE\_BUSY = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_BUSY\_BIT),

4022 K\_WORK\_QUEUE\_DRAIN\_BIT = 2,

4023 K\_WORK\_QUEUE\_DRAIN = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_DRAIN\_BIT),

4024 K\_WORK\_QUEUE\_PLUGGED\_BIT = 3,

4025 K\_WORK\_QUEUE\_PLUGGED = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_PLUGGED\_BIT),

4026 K\_WORK\_QUEUE\_STOP\_BIT = 4,

4027 K\_WORK\_QUEUE\_STOP = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_STOP\_BIT),

4028

4029 /\* Static work queue flags \*/

4030 K\_WORK\_QUEUE\_NO\_YIELD\_BIT = 8,

4031 K\_WORK\_QUEUE\_NO\_YIELD = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_NO\_YIELD\_BIT),

4032

4036 /\* Transient work flags \*/

4037

[ 4043](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165) [K\_WORK\_RUNNING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_RUNNING\_BIT),

4044

[ 4049](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732) [K\_WORK\_CANCELING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_CANCELING\_BIT),

4050

[ 4056](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85) [K\_WORK\_QUEUED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUED\_BIT),

4057

[ 4063](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed) [K\_WORK\_DELAYED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_DELAYED\_BIT),

4064

[ 4069](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601) [K\_WORK\_FLUSHING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_FLUSHING\_BIT),

4070};

4071

[ 4073](structk__work.md)struct [k\_work](structk__work.md) {

4074 /\* All fields are protected by the work module spinlock. No fields

4075 \* are to be accessed except through kernel API.

4076 \*/

4077

4078 /\* Node to link into k\_work\_q pending list. \*/

[ 4079](structk__work.md#a85772682983e0fdeb735f0821d5710d4) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structk__work.md#a85772682983e0fdeb735f0821d5710d4);

4080

4081 /\* The function to be invoked by the work queue thread. \*/

[ 4082](structk__work.md#a096d6ca1338fb0fbfa330b790136f172) [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) [handler](structk__work.md#a096d6ca1338fb0fbfa330b790136f172);

4083

4084 /\* The queue on which the work item was last submitted. \*/

[ 4085](structk__work.md#a551be8394e041020c36a97dc2e12e137) struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137);

4086

4087 /\* State of the work item.

4088 \*

4089 \* The item can be DELAYED, QUEUED, and RUNNING simultaneously.

4090 \*

4091 \* It can be RUNNING and CANCELING simultaneously.

4092 \*/

[ 4093](structk__work.md#a391ed7d2039cd05c9894267bf8ea4dfd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structk__work.md#a391ed7d2039cd05c9894267bf8ea4dfd);

4094};

4095

4096#define Z\_WORK\_INITIALIZER(work\_handler) { \

4097 .handler = (work\_handler), \

4098}

4099

[ 4101](structk__work__delayable.md)struct [k\_work\_delayable](structk__work__delayable.md) {

4102 /\* The work item. \*/

[ 4103](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629) struct [k\_work](structk__work.md) [work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629);

4104

4105 /\* Timeout used to submit work after a delay. \*/

[ 4106](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d) struct \_timeout [timeout](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d);

4107

4108 /\* The queue to which the work should be submitted. \*/

[ 4109](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4) struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4);

4110};

4111

4112#define Z\_WORK\_DELAYABLE\_INITIALIZER(work\_handler) { \

4113 .work = { \

4114 .handler = (work\_handler), \

4115 .flags = K\_WORK\_DELAYABLE, \

4116 }, \

4117}

4118

[ 4135](group__workqueue__apis.md#ga893b281f3d2bc0088650536899e17903)#define K\_WORK\_DELAYABLE\_DEFINE(work, work\_handler) \

4136 struct k\_work\_delayable work \

4137 = Z\_WORK\_DELAYABLE\_INITIALIZER(work\_handler)

4138

4142

4143/\* Record used to wait for work to flush.

4144 \*

4145 \* The work item is inserted into the queue that will process (or is

4146 \* processing) the item, and will be processed as soon as the item

4147 \* completes. When the flusher is processed the semaphore will be

4148 \* signaled, releasing the thread waiting for the flush.

4149 \*/

4150struct z\_work\_flusher {

4151 struct [k\_work](structk__work.md) work;

4152 struct [k\_sem](structk__sem.md) sem;

4153};

4154

4155/\* Record used to wait for work to complete a cancellation.

4156 \*

4157 \* The work item is inserted into a global queue of pending cancels.

4158 \* When a cancelling work item goes idle any matching waiters are

4159 \* removed from pending\_cancels and are woken.

4160 \*/

4161struct z\_work\_canceller {

4162 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

4163 struct k\_work \*work;

4164 struct k\_sem sem;

4165};

4166

4170

[ 4184](structk__work__sync.md)struct [k\_work\_sync](structk__work__sync.md) {

4185 union {

[ 4186](structk__work__sync.md#ad81ff57cb9f2f3dc5f2d65917cf04f1c) struct z\_work\_flusher [flusher](structk__work__sync.md#ad81ff57cb9f2f3dc5f2d65917cf04f1c);

[ 4187](structk__work__sync.md#a7e8fd0b9d6736c403aefa8462c7c0835) struct z\_work\_canceller [canceller](structk__work__sync.md#a7e8fd0b9d6736c403aefa8462c7c0835);

4188 };

4189};

4190

[ 4197](structk__work__queue__config.md)struct [k\_work\_queue\_config](structk__work__queue__config.md) {

[ 4202](structk__work__queue__config.md#a0929d83372efff6798bc69bb7ca1eaaa) const char \*[name](structk__work__queue__config.md#a0929d83372efff6798bc69bb7ca1eaaa);

4203

[ 4216](structk__work__queue__config.md#afcf64d6e69d1ddfff8cbd749dafa4d13) bool [no\_yield](structk__work__queue__config.md#afcf64d6e69d1ddfff8cbd749dafa4d13);

4217

[ 4221](structk__work__queue__config.md#a5aa4a80d91ef36498443c163428b02c0) bool [essential](structk__work__queue__config.md#a5aa4a80d91ef36498443c163428b02c0);

4222

[ 4231](structk__work__queue__config.md#a517d9895f211d886de4b18f2f16d06c3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [work\_timeout\_ms](structk__work__queue__config.md#a517d9895f211d886de4b18f2f16d06c3);

4232};

4233

[ 4235](structk__work__q.md)struct [k\_work\_q](structk__work__q.md) {

4236 /\* The thread that animates the work. \*/

[ 4237](structk__work__q.md#aa42ca271a4989f129bf1a43c491327eb) struct [k\_thread](structk__thread.md) [thread](structk__work__q.md#aa42ca271a4989f129bf1a43c491327eb);

4238

4239 /\* The thread ID that animates the work. This may be an external thread

4240 \* if k\_work\_queue\_run() is used.

4241 \*/

[ 4242](structk__work__q.md#a48f58baa029424bb0bceb07361fe2e53) [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [thread\_id](structk__work__q.md#a48f58baa029424bb0bceb07361fe2e53);

4243

4244 /\* All the following fields must be accessed only while the

4245 \* work module spinlock is held.

4246 \*/

4247

4248 /\* List of k\_work items to be worked. \*/

[ 4249](structk__work__q.md#a2012199571f6b658873550d64386b00c) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [pending](structk__work__q.md#a2012199571f6b658873550d64386b00c);

4250

4251 /\* Wait queue for idle work thread. \*/

[ 4252](structk__work__q.md#a561c90f8bb944217230e00052cdecf10) \_wait\_q\_t [notifyq](structk__work__q.md#a561c90f8bb944217230e00052cdecf10);

4253

4254 /\* Wait queue for threads waiting for the queue to drain. \*/

[ 4255](structk__work__q.md#a308d1ac78b1203b7ea78b0f18c5bdf5b) \_wait\_q\_t [drainq](structk__work__q.md#a308d1ac78b1203b7ea78b0f18c5bdf5b);

4256

4257 /\* Flags describing queue state. \*/

[ 4258](structk__work__q.md#a68bc8e9c412ebdbf34827087d91a080e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structk__work__q.md#a68bc8e9c412ebdbf34827087d91a080e);

4259

4260#if defined(CONFIG\_WORKQUEUE\_WORK\_TIMEOUT)

4261 struct \_timeout work\_timeout\_record;

4262 struct [k\_work](structk__work.md) \*work;

4263 [k\_timeout\_t](structk__timeout__t.md) work\_timeout;

4264#endif /\* defined(CONFIG\_WORKQUEUE\_WORK\_TIMEOUT) \*/

4265};

4266

4267/\* Provide the implementation for inline functions declared above \*/

4268

[ 4269](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)static inline bool [k\_work\_is\_pending](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)(const struct [k\_work](structk__work.md) \*work)

4270{

4271 return [k\_work\_busy\_get](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b)(work) != 0;

4272}

4273

4274static inline struct [k\_work\_delayable](structk__work__delayable.md) \*

[ 4275](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca)[k\_work\_delayable\_from\_work](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca)(struct [k\_work](structk__work.md) \*[work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629))

4276{

4277 return [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)([work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629), struct [k\_work\_delayable](structk__work__delayable.md), [work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629));

4278}

4279

[ 4280](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e)static inline bool [k\_work\_delayable\_is\_pending](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e)(

4281 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork)

4282{

4283 return [k\_work\_delayable\_busy\_get](group__workqueue__apis.md#ga1b76969667844f0981d348c9c671bc9f)(dwork) != 0;

4284}

4285

[ 4286](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624)static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_work\_delayable\_expires\_get](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624)(

4287 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork)

4288{

4289 return z\_timeout\_expires(&dwork->[timeout](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d));

4290}

4291

[ 4292](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4)static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_work\_delayable\_remaining\_get](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4)(

4293 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork)

4294{

4295 return z\_timeout\_remaining(&dwork->[timeout](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d));

4296}

4297

[ 4298](group__workqueue__apis.md#ga0b8b496f7e7bd82d08590a07293e38d7)static inline [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_work\_queue\_thread\_get](group__workqueue__apis.md#ga0b8b496f7e7bd82d08590a07293e38d7)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4))

4299{

4300 return [queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4)->[thread\_id](structk__work__q.md#a48f58baa029424bb0bceb07361fe2e53);

4301}

4302

4304

4305struct k\_work\_user;

4306

4311

[ 4321](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc)typedef void (\*[k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc))(struct k\_work\_user \*work);

4322

4326

4327struct k\_work\_user\_q {

4328 struct [k\_queue](structk__queue.md) queue;

4329 struct [k\_thread](structk__thread.md) thread;

4330};

4331

4332enum {

4333 K\_WORK\_USER\_STATE\_PENDING, /\* Work item pending state \*/

4334};

4335

4336struct k\_work\_user {

4337 void \*\_reserved; /\* Used by k\_queue implementation. \*/

4338 [k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc) handler;

4339 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

4340};

4341

4345

4346#if defined(\_\_cplusplus) && ((\_\_cplusplus - 0) < 202002L)

4347#define Z\_WORK\_USER\_INITIALIZER(work\_handler) { NULL, work\_handler, 0 }

4348#else

4349#define Z\_WORK\_USER\_INITIALIZER(work\_handler) \

4350 { \

4351 .\_reserved = NULL, \

4352 .handler = (work\_handler), \

4353 .flags = 0 \

4354 }

4355#endif

4356

[ 4368](group__workqueue__apis.md#ga4f3eac1fc56d5c9c21a3afa9b964b0bf)#define K\_WORK\_USER\_DEFINE(work, work\_handler) \

4369 struct k\_work\_user work = Z\_WORK\_USER\_INITIALIZER(work\_handler)

4370

[ 4380](group__workqueue__apis.md#ga9de9c7a7f13cc6b325e5453e34afe62d)static inline void [k\_work\_user\_init](group__workqueue__apis.md#ga9de9c7a7f13cc6b325e5453e34afe62d)(struct k\_work\_user \*work,

4381 [k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc) handler)

4382{

4383 \*work = (struct k\_work\_user)Z\_WORK\_USER\_INITIALIZER(handler);

4384}

4385

[ 4402](group__workqueue__apis.md#ga58d05d4127e4cd51104a1f1a87f626cd)static inline bool [k\_work\_user\_is\_pending](group__workqueue__apis.md#ga58d05d4127e4cd51104a1f1a87f626cd)(struct k\_work\_user \*work)

4403{

4404 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(&work->flags, K\_WORK\_USER\_STATE\_PENDING);

4405}

4406

[ 4425](group__workqueue__apis.md#ga50ae1f6f74c0bc0a41dbbf789fff8856)static inline int [k\_work\_user\_submit\_to\_queue](group__workqueue__apis.md#ga50ae1f6f74c0bc0a41dbbf789fff8856)(struct k\_work\_user\_q \*work\_q,

4426 struct k\_work\_user \*work)

4427{

4428 int ret = -[EBUSY](group__system__errno.md#ga8368025077a0385849d6817b2007c095);

4429

4430 if (![atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)(&work->flags,

4431 K\_WORK\_USER\_STATE\_PENDING)) {

4432 ret = [k\_queue\_alloc\_append](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a)(&work\_q->queue, work);

4433

4434 /\* Couldn't insert into the queue. Clear the pending bit

4435 \* so the work item can be submitted again

4436 \*/

4437 if (ret != 0) {

4438 [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)(&work->flags,

4439 K\_WORK\_USER\_STATE\_PENDING);

4440 }

4441 }

4442

4443 return ret;

4444}

4445

[ 4465](group__workqueue__apis.md#ga3091bc8fab5311252e41634a97a18589)void [k\_work\_user\_queue\_start](group__workqueue__apis.md#ga3091bc8fab5311252e41634a97a18589)(struct k\_work\_user\_q \*work\_q,

4466 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack,

4467 size\_t stack\_size, int prio,

4468 const char \*name);

4469

[ 4480](group__workqueue__apis.md#gab487068e9564cd77b6bdbac3d5670923)static inline [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_work\_user\_queue\_thread\_get](group__workqueue__apis.md#gab487068e9564cd77b6bdbac3d5670923)(struct k\_work\_user\_q \*work\_q)

4481{

4482 return &work\_q->thread;

4483}

4484

4486

4490

4491struct k\_work\_poll {

4492 struct k\_work work;

4493 struct k\_work\_q \*workq;

4494 struct z\_poller poller;

4495 struct k\_poll\_event \*events;

4496 int num\_events;

4497 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) real\_handler;

4498 struct \_timeout timeout;

4499 int poll\_result;

4500};

4501

4505

4510

[ 4522](group__workqueue__apis.md#gaf8e003eefa5dd66ba883688f9d39c333)#define K\_WORK\_DEFINE(work, work\_handler) \

4523 struct k\_work work = Z\_WORK\_INITIALIZER(work\_handler)

4524

[ 4534](group__workqueue__apis.md#ga371dab33a40622bea19b07d852863443)void [k\_work\_poll\_init](group__workqueue__apis.md#ga371dab33a40622bea19b07d852863443)(struct k\_work\_poll \*work,

4535 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) handler);

4536

[ 4571](group__workqueue__apis.md#ga0abafd7f851e42fd3572c8438e600a53)int [k\_work\_poll\_submit\_to\_queue](group__workqueue__apis.md#ga0abafd7f851e42fd3572c8438e600a53)(struct [k\_work\_q](structk__work__q.md) \*work\_q,

4572 struct k\_work\_poll \*work,

4573 struct [k\_poll\_event](structk__poll__event.md) \*events,

4574 int num\_events,

4575 [k\_timeout\_t](structk__timeout__t.md) timeout);

4576

[ 4608](group__workqueue__apis.md#gad9f222e46d72c4f98739395a0c8bb4ea)int [k\_work\_poll\_submit](group__workqueue__apis.md#gad9f222e46d72c4f98739395a0c8bb4ea)(struct k\_work\_poll \*work,

4609 struct [k\_poll\_event](structk__poll__event.md) \*events,

4610 int num\_events,

4611 [k\_timeout\_t](structk__timeout__t.md) timeout);

4612

[ 4627](group__workqueue__apis.md#ga2a19547d04dc1a202e80b752e3177215)int [k\_work\_poll\_cancel](group__workqueue__apis.md#ga2a19547d04dc1a202e80b752e3177215)(struct k\_work\_poll \*work);

4628

4630

4636

[ 4640](structk__msgq.md)struct [k\_msgq](structk__msgq.md) {

[ 4642](structk__msgq.md#ae3b3d53d60b789d69c65494cfd090076) \_wait\_q\_t [wait\_q](structk__msgq.md#ae3b3d53d60b789d69c65494cfd090076);

[ 4644](structk__msgq.md#aa2e00a7292502f0de88cff28c5e375f0) struct [k\_spinlock](structk__spinlock.md) [lock](structk__msgq.md#aa2e00a7292502f0de88cff28c5e375f0);

[ 4646](structk__msgq.md#a512fe468da96540639a0d71f1707f79d) size\_t [msg\_size](structk__msgq.md#a512fe468da96540639a0d71f1707f79d);

[ 4648](structk__msgq.md#aebd3b6e91e97b2d4369feea1a3f7b7a0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_msgs](structk__msgq.md#aebd3b6e91e97b2d4369feea1a3f7b7a0);

[ 4650](structk__msgq.md#aca77f1cf833d3aa27ae65004b446bdd2) char \*[buffer\_start](structk__msgq.md#aca77f1cf833d3aa27ae65004b446bdd2);

[ 4652](structk__msgq.md#a9d47fd25d7a70e8518d45dd48c51f0e0) char \*[buffer\_end](structk__msgq.md#a9d47fd25d7a70e8518d45dd48c51f0e0);

[ 4654](structk__msgq.md#a594e8a4a638521f42f24f85fe0742d64) char \*[read\_ptr](structk__msgq.md#a594e8a4a638521f42f24f85fe0742d64);

[ 4656](structk__msgq.md#aacf9b7b9f6e26e402f3752fc56834f23) char \*[write\_ptr](structk__msgq.md#aacf9b7b9f6e26e402f3752fc56834f23);

[ 4658](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [used\_msgs](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857);

4659

4660 Z\_DECL\_POLL\_EVENT

4661

[ 4663](structk__msgq.md#ae03025420908f8342ce12a1395c7657b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structk__msgq.md#ae03025420908f8342ce12a1395c7657b);

4664

4665 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_msgq](structk__msgq.md))

4666

4667#ifdef CONFIG\_OBJ\_CORE\_MSGQ

4668 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

4669#endif

4670};

4671

4674

4675

4676#define Z\_MSGQ\_INITIALIZER(obj, q\_buffer, q\_msg\_size, q\_max\_msgs) \

4677 { \

4678 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

4679 .lock = {}, \

4680 .msg\_size = q\_msg\_size, \

4681 .max\_msgs = q\_max\_msgs, \

4682 .buffer\_start = q\_buffer, \

4683 .buffer\_end = q\_buffer + (q\_max\_msgs \* q\_msg\_size), \

4684 .read\_ptr = q\_buffer, \

4685 .write\_ptr = q\_buffer, \

4686 .used\_msgs = 0, \

4687 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

4688 .flags = 0, \

4689 }

4690

4694

4695

[ 4696](group__msgq__apis.md#ga4bb73f46fd0818f7f7a90860b792f7ce)#define K\_MSGQ\_FLAG\_ALLOC BIT(0)

4697

[ 4701](structk__msgq__attrs.md)struct [k\_msgq\_attrs](structk__msgq__attrs.md) {

[ 4703](structk__msgq__attrs.md#a7d1d72946bdd517c07da37493a89e30e) size\_t [msg\_size](structk__msgq__attrs.md#a7d1d72946bdd517c07da37493a89e30e);

[ 4705](structk__msgq__attrs.md#ad0f5894ba0da840b91eb85015252e649) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_msgs](structk__msgq__attrs.md#ad0f5894ba0da840b91eb85015252e649);

[ 4707](structk__msgq__attrs.md#a00f936870442fa455117cbdd7821fac5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [used\_msgs](structk__msgq__attrs.md#a00f936870442fa455117cbdd7821fac5);

4708};

4709

4710

[ 4729](group__msgq__apis.md#ga95ef93002766901511d09c8cd8f8293b)#define K\_MSGQ\_DEFINE(q\_name, q\_msg\_size, q\_max\_msgs, q\_align) \

4730 static char \_\_noinit \_\_aligned(q\_align) \

4731 \_k\_fifo\_buf\_##q\_name[(q\_max\_msgs) \* (q\_msg\_size)]; \

4732 STRUCT\_SECTION\_ITERABLE(k\_msgq, q\_name) = \

4733 Z\_MSGQ\_INITIALIZER(q\_name, \_k\_fifo\_buf\_##q\_name, \

4734 (q\_msg\_size), (q\_max\_msgs))

4735

[ 4750](group__msgq__apis.md#ga54a5cdcaea2236c383ace433fedc0d39)void [k\_msgq\_init](group__msgq__apis.md#ga54a5cdcaea2236c383ace433fedc0d39)(struct [k\_msgq](structk__msgq.md) \*msgq, char \*buffer, size\_t msg\_size,

4751 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_msgs);

4752

[ 4772](group__msgq__apis.md#gabe7305b8f442ebdc147dbbc6e8cf92fc)\_\_syscall int [k\_msgq\_alloc\_init](group__msgq__apis.md#gabe7305b8f442ebdc147dbbc6e8cf92fc)(struct [k\_msgq](structk__msgq.md) \*msgq, size\_t msg\_size,

4773 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_msgs);

4774

[ 4785](group__msgq__apis.md#gafda4399aa9b8f1e44bdf752e00ea787b)int [k\_msgq\_cleanup](group__msgq__apis.md#gafda4399aa9b8f1e44bdf752e00ea787b)(struct [k\_msgq](structk__msgq.md) \*msgq);

4786

[ 4807](group__msgq__apis.md#ga54e96aaaea5462a1f963b7fd5ca82bfe)\_\_syscall int [k\_msgq\_put](group__msgq__apis.md#ga54e96aaaea5462a1f963b7fd5ca82bfe)(struct [k\_msgq](structk__msgq.md) \*msgq, const void \*data, [k\_timeout\_t](structk__timeout__t.md) timeout);

4808

[ 4829](group__msgq__apis.md#gae67f2ced2df1f9c290ae15dab9097cb7)\_\_syscall int [k\_msgq\_get](group__msgq__apis.md#gae67f2ced2df1f9c290ae15dab9097cb7)(struct [k\_msgq](structk__msgq.md) \*msgq, void \*data, [k\_timeout\_t](structk__timeout__t.md) timeout);

4830

[ 4845](group__msgq__apis.md#ga14f543472f2f63cfde0bdfa87b95c915)\_\_syscall int [k\_msgq\_peek](group__msgq__apis.md#ga14f543472f2f63cfde0bdfa87b95c915)(struct [k\_msgq](structk__msgq.md) \*msgq, void \*data);

4846

[ 4863](group__msgq__apis.md#ga69b004a40ab4ca497de314a99960fb8e)\_\_syscall int [k\_msgq\_peek\_at](group__msgq__apis.md#ga69b004a40ab4ca497de314a99960fb8e)(struct [k\_msgq](structk__msgq.md) \*msgq, void \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx);

4864

[ 4874](group__msgq__apis.md#gaa18875887773195ae44b7fe0972ee760)\_\_syscall void [k\_msgq\_purge](group__msgq__apis.md#gaa18875887773195ae44b7fe0972ee760)(struct [k\_msgq](structk__msgq.md) \*msgq);

4875

[ 4886](group__msgq__apis.md#ga7d154beb4f9c6227eddbef26d406ca24)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_msgq\_num\_free\_get](group__msgq__apis.md#ga7d154beb4f9c6227eddbef26d406ca24)(struct [k\_msgq](structk__msgq.md) \*msgq);

4887

[ 4896](group__msgq__apis.md#ga8f9d3eef67cbc9c0717a84190bbf7f41)\_\_syscall void [k\_msgq\_get\_attrs](group__msgq__apis.md#ga8f9d3eef67cbc9c0717a84190bbf7f41)(struct [k\_msgq](structk__msgq.md) \*msgq,

4897 struct [k\_msgq\_attrs](structk__msgq__attrs.md) \*attrs);

4898

4899

4900static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_k\_msgq\_num\_free\_get(struct [k\_msgq](structk__msgq.md) \*msgq)

4901{

4902 return msgq->[max\_msgs](structk__msgq.md#aebd3b6e91e97b2d4369feea1a3f7b7a0) - msgq->[used\_msgs](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857);

4903}

4904

[ 4914](group__msgq__apis.md#ga458793a89f1d9f762bda3422918a9faa)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_msgq\_num\_used\_get](group__msgq__apis.md#ga458793a89f1d9f762bda3422918a9faa)(struct [k\_msgq](structk__msgq.md) \*msgq);

4915

4916static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_k\_msgq\_num\_used\_get(struct [k\_msgq](structk__msgq.md) \*msgq)

4917{

4918 return msgq->[used\_msgs](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857);

4919}

4920

4922

4928

[ 4933](structk__mbox__msg.md)struct [k\_mbox\_msg](structk__mbox__msg.md) {

[ 4935](structk__mbox__msg.md#aeabf45e9599a64852a1cfd656b1ece8e) size\_t [size](structk__mbox__msg.md#aeabf45e9599a64852a1cfd656b1ece8e);

[ 4937](structk__mbox__msg.md#aa79f2bf71431b474ec4551ade4d7a8dd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [info](structk__mbox__msg.md#aa79f2bf71431b474ec4551ade4d7a8dd);

[ 4939](structk__mbox__msg.md#a74b0edeed4c44cb5932eb292efc9d9c2) void \*[tx\_data](structk__mbox__msg.md#a74b0edeed4c44cb5932eb292efc9d9c2);

[ 4941](structk__mbox__msg.md#a9eb145a242ac66e80d90286d83fe7a61) [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [rx\_source\_thread](structk__mbox__msg.md#a9eb145a242ac66e80d90286d83fe7a61);

[ 4943](structk__mbox__msg.md#a73236acb7d27bb0233f5abb7214fb19c) [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [tx\_target\_thread](structk__mbox__msg.md#a73236acb7d27bb0233f5abb7214fb19c);

4945 [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) \_syncing\_thread;

4946#if (CONFIG\_NUM\_MBOX\_ASYNC\_MSGS > 0)

4948 struct [k\_sem](structk__sem.md) \*\_async\_sem;

4949#endif

4950};

4951

[ 4955](structk__mbox.md)struct [k\_mbox](structk__mbox.md) {

[ 4957](structk__mbox.md#a0bca912a50120707ddafa66d740ade96) \_wait\_q\_t [tx\_msg\_queue](structk__mbox.md#a0bca912a50120707ddafa66d740ade96);

[ 4959](structk__mbox.md#a808a14c31892a2d042cdb0723a2956e2) \_wait\_q\_t [rx\_msg\_queue](structk__mbox.md#a808a14c31892a2d042cdb0723a2956e2);

[ 4960](structk__mbox.md#a2c549d5bd7216b62d81ad2198e0d79e4) struct [k\_spinlock](structk__spinlock.md) [lock](structk__mbox.md#a2c549d5bd7216b62d81ad2198e0d79e4);

4961

4962 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_mbox](structk__mbox.md))

4963

4964#ifdef CONFIG\_OBJ\_CORE\_MAILBOX

4965 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

4966#endif

4967};

4968

4971

4972#define Z\_MBOX\_INITIALIZER(obj) \

4973 { \

4974 .tx\_msg\_queue = Z\_WAIT\_Q\_INIT(&obj.tx\_msg\_queue), \

4975 .rx\_msg\_queue = Z\_WAIT\_Q\_INIT(&obj.rx\_msg\_queue), \

4976 }

4977

4981

[ 4991](group__mailbox__apis.md#gab55cba898db47113a06641c01f3e3714)#define K\_MBOX\_DEFINE(name) \

4992 STRUCT\_SECTION\_ITERABLE(k\_mbox, name) = \

4993 Z\_MBOX\_INITIALIZER(name) \

4994

4995

[ 5002](group__mailbox__apis.md#ga686f20c199a9e971822d8279d175d8c2)void [k\_mbox\_init](group__mailbox__apis.md#ga686f20c199a9e971822d8279d175d8c2)(struct [k\_mbox](structk__mbox.md) \*mbox);

5003

[ 5023](group__mailbox__apis.md#gaa1e5cdd992d8b9be11f82254e1886ed2)int [k\_mbox\_put](group__mailbox__apis.md#gaa1e5cdd992d8b9be11f82254e1886ed2)(struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*tx\_msg,

5024 [k\_timeout\_t](structk__timeout__t.md) timeout);

5025

[ 5039](group__mailbox__apis.md#gadd60f7b760371c0a141a1e4da253a0f0)void [k\_mbox\_async\_put](group__mailbox__apis.md#gadd60f7b760371c0a141a1e4da253a0f0)(struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*tx\_msg,

5040 struct [k\_sem](structk__sem.md) \*sem);

5041

[ 5059](group__mailbox__apis.md#ga2ea91154620b139dbed1ad949b97c3ef)int [k\_mbox\_get](group__mailbox__apis.md#ga2ea91154620b139dbed1ad949b97c3ef)(struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*rx\_msg,

5060 void \*buffer, [k\_timeout\_t](structk__timeout__t.md) timeout);

5061

[ 5075](group__mailbox__apis.md#ga3d19e648e67f109609259543c9a01d6e)void [k\_mbox\_data\_get](group__mailbox__apis.md#ga3d19e648e67f109609259543c9a01d6e)(struct [k\_mbox\_msg](structk__mbox__msg.md) \*rx\_msg, void \*buffer);

5076

5078

5084

[ 5094](group__pipe__apis.md#gae2c8d97af1f7e9deb93e670859525cf3)\_\_syscall void [k\_pipe\_init](group__pipe__apis.md#gae2c8d97af1f7e9deb93e670859525cf3)(struct [k\_pipe](structk__pipe.md) \*pipe, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t buffer\_size);

5095

5096#ifdef CONFIG\_PIPES

5098struct [k\_pipe](structk__pipe.md) {

5099 unsigned char \*buffer;

5100 size\_t size;

5101 size\_t bytes\_used;

5102 size\_t read\_index;

5103 size\_t write\_index;

5104 struct [k\_spinlock](structk__spinlock.md) [lock](structk__pipe.md#aa2a367a9c8f0be89bcdf1bf6d3b0b875);

5105

5106 struct {

5107 \_wait\_q\_t readers;

5108 \_wait\_q\_t writers;

5109 } wait\_q;

5110

5111 Z\_DECL\_POLL\_EVENT

5112

5113 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structk__pipe.md#a2ed95fbe24ea20c4f292a66def1d4dde);

5114

5115 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_pipe)

5116

5117#ifdef CONFIG\_OBJ\_CORE\_PIPE

5118 struct k\_obj\_core obj\_core;

5119#endif

5120};

5121

5125#define K\_PIPE\_FLAG\_ALLOC BIT(0)

5126

5127#define Z\_PIPE\_INITIALIZER(obj, pipe\_buffer, pipe\_buffer\_size) \

5128 { \

5129 .buffer = pipe\_buffer, \

5130 .size = pipe\_buffer\_size, \

5131 .bytes\_used = 0, \

5132 .read\_index = 0, \

5133 .write\_index = 0, \

5134 .lock = {}, \

5135 .wait\_q = { \

5136 .readers = Z\_WAIT\_Q\_INIT(&obj.wait\_q.readers), \

5137 .writers = Z\_WAIT\_Q\_INIT(&obj.wait\_q.writers) \

5138 }, \

5139 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

5140 .flags = 0, \

5141 }

5142

5146

5160#define K\_PIPE\_DEFINE(name, pipe\_buffer\_size, pipe\_align) \

5161 static unsigned char \_\_noinit \_\_aligned(pipe\_align) \

5162 \_k\_pipe\_buf\_##name[pipe\_buffer\_size]; \

5163 STRUCT\_SECTION\_ITERABLE(k\_pipe, name) = \

5164 Z\_PIPE\_INITIALIZER(name, \_k\_pipe\_buf\_##name, pipe\_buffer\_size)

5165

5178\_\_deprecated int k\_pipe\_cleanup(struct [k\_pipe](structk__pipe.md) \*pipe);

5179

5196\_\_deprecated \_\_syscall int k\_pipe\_alloc\_init(struct [k\_pipe](structk__pipe.md) \*pipe, size\_t size);

5197

5217\_\_deprecated \_\_syscall int k\_pipe\_put(struct [k\_pipe](structk__pipe.md) \*pipe, const void \*data,

5218 size\_t bytes\_to\_write, size\_t \*bytes\_written,

5219 size\_t min\_xfer, [k\_timeout\_t](structk__timeout__t.md) timeout);

5220

5241\_\_deprecated \_\_syscall int k\_pipe\_get(struct [k\_pipe](structk__pipe.md) \*pipe, void \*data,

5242 size\_t bytes\_to\_read, size\_t \*bytes\_read,

5243 size\_t min\_xfer, [k\_timeout\_t](structk__timeout__t.md) timeout);

5244

5254\_\_deprecated \_\_syscall size\_t k\_pipe\_read\_avail(struct [k\_pipe](structk__pipe.md) \*pipe);

5255

5265\_\_deprecated \_\_syscall size\_t k\_pipe\_write\_avail(struct [k\_pipe](structk__pipe.md) \*pipe);

5266

5278\_\_deprecated \_\_syscall void k\_pipe\_flush(struct [k\_pipe](structk__pipe.md) \*pipe);

5279

5292\_\_deprecated \_\_syscall void k\_pipe\_buffer\_flush(struct [k\_pipe](structk__pipe.md) \*pipe);

5293

5294#else /\* CONFIG\_PIPES \*/

5295

[ 5296](group__pipe__apis.md#gae5471546043f4d14e97c3f6313053ee0)enum [pipe\_flags](group__pipe__apis.md#gae5471546043f4d14e97c3f6313053ee0) {

[ 5297](group__pipe__apis.md#ggae5471546043f4d14e97c3f6313053ee0a9fc19eac7b41c00ca97c2fb0a30a2309) [PIPE\_FLAG\_OPEN](group__pipe__apis.md#ggae5471546043f4d14e97c3f6313053ee0a9fc19eac7b41c00ca97c2fb0a30a2309) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 5298](group__pipe__apis.md#ggae5471546043f4d14e97c3f6313053ee0a37642c400a675e1dce34c9b878874df4) [PIPE\_FLAG\_RESET](group__pipe__apis.md#ggae5471546043f4d14e97c3f6313053ee0a37642c400a675e1dce34c9b878874df4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

5299};

5300

[ 5301](structk__pipe.md)struct [k\_pipe](structk__pipe.md) {

[ 5302](structk__pipe.md#ac9162db42883d2c14f63cf74ff3c1179) size\_t [waiting](structk__pipe.md#ac9162db42883d2c14f63cf74ff3c1179);

[ 5303](structk__pipe.md#a62556b1fbb907dcb8fbbe29c597d8473) struct [ring\_buf](structring__buf.md) [buf](structk__pipe.md#a62556b1fbb907dcb8fbbe29c597d8473);

[ 5304](structk__pipe.md#aa2a367a9c8f0be89bcdf1bf6d3b0b875) struct [k\_spinlock](structk__spinlock.md) [lock](structk__pipe.md#aa2a367a9c8f0be89bcdf1bf6d3b0b875);

[ 5305](structk__pipe.md#a8af11082e53b56670f0ce11e581766ff) \_wait\_q\_t [data](structk__pipe.md#a8af11082e53b56670f0ce11e581766ff);

[ 5306](structk__pipe.md#aa1428192b88b97e0cb5ec83894770f47) \_wait\_q\_t [space](structk__pipe.md#aa1428192b88b97e0cb5ec83894770f47);

[ 5307](structk__pipe.md#a2ed95fbe24ea20c4f292a66def1d4dde) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structk__pipe.md#a2ed95fbe24ea20c4f292a66def1d4dde);

5308

5309 Z\_DECL\_POLL\_EVENT

5310#ifdef CONFIG\_OBJ\_CORE\_PIPE

5311 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

5312#endif

5313 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_pipe](structk__pipe.md))

5314};

5315

5319#define Z\_PIPE\_INITIALIZER(obj, pipe\_buffer, pipe\_buffer\_size) \

5320{ \

5321 .buf = RING\_BUF\_INIT(pipe\_buffer, pipe\_buffer\_size), \

5322 .data = Z\_WAIT\_Q\_INIT(&obj.data), \

5323 .space = Z\_WAIT\_Q\_INIT(&obj.space), \

5324 .flags = PIPE\_FLAG\_OPEN, \

5325 .waiting = 0, \

5326 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

5327}

5331

[ 5345](group__pipe__apis.md#gac2256aa00c59e78199be9bdefd61aa52)#define K\_PIPE\_DEFINE(name, pipe\_buffer\_size, pipe\_align) \

5346 static unsigned char \_\_noinit \_\_aligned(pipe\_align) \

5347 \_k\_pipe\_buf\_##name[pipe\_buffer\_size]; \

5348 STRUCT\_SECTION\_ITERABLE(k\_pipe, name) = \

5349 Z\_PIPE\_INITIALIZER(name, \_k\_pipe\_buf\_##name, pipe\_buffer\_size)

5350

5351

[ 5368](group__pipe__apis.md#ga514ab3d174dcada766ecbda138944ddc)\_\_syscall int [k\_pipe\_write](group__pipe__apis.md#ga514ab3d174dcada766ecbda138944ddc)(struct [k\_pipe](structk__pipe.md) \*pipe, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len,

5369 [k\_timeout\_t](structk__timeout__t.md) timeout);

5370

[ 5386](group__pipe__apis.md#gaecb07412025d9e065ee7b99121522257)\_\_syscall int [k\_pipe\_read](group__pipe__apis.md#gaecb07412025d9e065ee7b99121522257)(struct [k\_pipe](structk__pipe.md) \*pipe, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len,

5387 [k\_timeout\_t](structk__timeout__t.md) timeout);

5388

[ 5398](group__pipe__apis.md#gaaedff72169127b8227c80bf8adf1f9dd)\_\_syscall void [k\_pipe\_reset](group__pipe__apis.md#gaaedff72169127b8227c80bf8adf1f9dd)(struct [k\_pipe](structk__pipe.md) \*pipe);

5399

[ 5408](group__pipe__apis.md#ga83d4b5de8902845850d01b0c3db0702a)\_\_syscall void [k\_pipe\_close](group__pipe__apis.md#ga83d4b5de8902845850d01b0c3db0702a)(struct [k\_pipe](structk__pipe.md) \*pipe);

5409#endif /\* CONFIG\_PIPES \*/

5411

5415struct k\_mem\_slab\_info {

5416 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks;

5417 size\_t block\_size;

5418 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_used;

5419#ifdef CONFIG\_MEM\_SLAB\_TRACE\_MAX\_UTILIZATION

5420 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_used;

5421#endif

5422};

5423

5424struct k\_mem\_slab {

5425 \_wait\_q\_t wait\_q;

5426 struct k\_spinlock lock;

5427 char \*buffer;

5428 char \*free\_list;

5429 struct k\_mem\_slab\_info info;

5430

5431 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_mem\_slab)

5432

5433#ifdef CONFIG\_OBJ\_CORE\_MEM\_SLAB

5434 struct k\_obj\_core obj\_core;

5435#endif

5436};

5437

5438#define Z\_MEM\_SLAB\_INITIALIZER(\_slab, \_slab\_buffer, \_slab\_block\_size, \

5439 \_slab\_num\_blocks) \

5440 { \

5441 .wait\_q = Z\_WAIT\_Q\_INIT(&(\_slab).wait\_q), \

5442 .lock = {}, \

5443 .buffer = \_slab\_buffer, \

5444 .free\_list = NULL, \

5445 .info = {\_slab\_num\_blocks, \_slab\_block\_size, 0} \

5446 }

5447

5448

5452

5458

[ 5484](group__mem__slab__apis.md#ga6b6751464262505c1117dea1bea56a08)#define K\_MEM\_SLAB\_DEFINE\_IN\_SECT(name, in\_section, slab\_block\_size, slab\_num\_blocks, slab\_align) \

5485 BUILD\_ASSERT(((slab\_block\_size) % (slab\_align)) == 0, \

5486 "slab\_block\_size must be a multiple of slab\_align"); \

5487 BUILD\_ASSERT((((slab\_align) & ((slab\_align) - 1)) == 0), \

5488 "slab\_align must be a power of 2"); \

5489 char in\_section \_\_aligned(WB\_UP( \

5490 slab\_align)) \_k\_mem\_slab\_buf\_##name[(slab\_num\_blocks) \* WB\_UP(slab\_block\_size)]; \

5491 STRUCT\_SECTION\_ITERABLE(k\_mem\_slab, name) = Z\_MEM\_SLAB\_INITIALIZER( \

5492 name, \_k\_mem\_slab\_buf\_##name, WB\_UP(slab\_block\_size), slab\_num\_blocks)

5493

[ 5517](group__mem__slab__apis.md#ga60bc92eee58fcc5f121b8e4d82eaa69e)#define K\_MEM\_SLAB\_DEFINE(name, slab\_block\_size, slab\_num\_blocks, slab\_align) \

5518 K\_MEM\_SLAB\_DEFINE\_IN\_SECT(name, \_\_noinit\_named(k\_mem\_slab\_buf\_##name), slab\_block\_size, \

5519 slab\_num\_blocks, slab\_align)

5520

[ 5537](group__mem__slab__apis.md#ga7f0750f940b9a9f94b5c52373d4161f1)#define K\_MEM\_SLAB\_DEFINE\_IN\_SECT\_STATIC(name, in\_section, slab\_block\_size, slab\_num\_blocks, \

5538 slab\_align) \

5539 BUILD\_ASSERT(((slab\_block\_size) % (slab\_align)) == 0, \

5540 "slab\_block\_size must be a multiple of slab\_align"); \

5541 BUILD\_ASSERT((((slab\_align) & ((slab\_align) - 1)) == 0), \

5542 "slab\_align must be a power of 2"); \

5543 static char in\_section \_\_aligned(WB\_UP( \

5544 slab\_align)) \_k\_mem\_slab\_buf\_##name[(slab\_num\_blocks) \* WB\_UP(slab\_block\_size)]; \

5545 static STRUCT\_SECTION\_ITERABLE(k\_mem\_slab, name) = Z\_MEM\_SLAB\_INITIALIZER( \

5546 name, \_k\_mem\_slab\_buf\_##name, WB\_UP(slab\_block\_size), slab\_num\_blocks)

5547

[ 5562](group__mem__slab__apis.md#ga90bdbb15f410991f54ba16025c24bc3c)#define K\_MEM\_SLAB\_DEFINE\_STATIC(name, slab\_block\_size, slab\_num\_blocks, slab\_align) \

5563 K\_MEM\_SLAB\_DEFINE\_IN\_SECT\_STATIC(name, \_\_noinit\_named(k\_mem\_slab\_buf\_##name), \

5564 slab\_block\_size, slab\_num\_blocks, slab\_align)

5565

[ 5587](group__mem__slab__apis.md#ga094a8f173f287e29bb287119c26889d1)int [k\_mem\_slab\_init](group__mem__slab__apis.md#ga094a8f173f287e29bb287119c26889d1)(struct k\_mem\_slab \*slab, void \*buffer,

5588 size\_t block\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks);

5589

[ 5612](group__mem__slab__apis.md#gab16a46d8394aca18de740ad044a8734a)int [k\_mem\_slab\_alloc](group__mem__slab__apis.md#gab16a46d8394aca18de740ad044a8734a)(struct k\_mem\_slab \*slab, void \*\*mem,

5613 [k\_timeout\_t](structk__timeout__t.md) timeout);

5614

[ 5624](group__mem__slab__apis.md#ga2635ea8f9a30b8751ec966fe62adc0e1)void [k\_mem\_slab\_free](group__mem__slab__apis.md#ga2635ea8f9a30b8751ec966fe62adc0e1)(struct k\_mem\_slab \*slab, void \*mem);

5625

[ 5636](group__mem__slab__apis.md#gac76b96d7055e4ad94765c93530dd0720)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_mem\_slab\_num\_used\_get](group__mem__slab__apis.md#gac76b96d7055e4ad94765c93530dd0720)(struct k\_mem\_slab \*slab)

5637{

5638 return slab->info.num\_used;

5639}

5640

[ 5651](group__mem__slab__apis.md#gae0e949c1c3476dd57bc0c0ed627d2346)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_mem\_slab\_max\_used\_get](group__mem__slab__apis.md#gae0e949c1c3476dd57bc0c0ed627d2346)(struct k\_mem\_slab \*slab)

5652{

5653#ifdef CONFIG\_MEM\_SLAB\_TRACE\_MAX\_UTILIZATION

5654 return slab->info.max\_used;

5655#else

5656 ARG\_UNUSED(slab);

5657 return 0;

5658#endif

5659}

5660

[ 5671](group__mem__slab__apis.md#gae87577e2873cf746db69216a82f94aea)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_mem\_slab\_num\_free\_get](group__mem__slab__apis.md#gae87577e2873cf746db69216a82f94aea)(struct k\_mem\_slab \*slab)

5672{

5673 return slab->info.num\_blocks - slab->info.num\_used;

5674}

5675

5687

[ 5688](group__mem__slab__apis.md#ga32030a5cfb44f663bd31b4e1b3d5dddb)int [k\_mem\_slab\_runtime\_stats\_get](group__mem__slab__apis.md#ga32030a5cfb44f663bd31b4e1b3d5dddb)(struct k\_mem\_slab \*slab, struct [sys\_memory\_stats](structsys__memory__stats.md) \*stats);

5689

[ 5701](group__mem__slab__apis.md#gaa1f44e30f4aee98b38e1ab5e93af505c)int [k\_mem\_slab\_runtime\_stats\_reset\_max](group__mem__slab__apis.md#gaa1f44e30f4aee98b38e1ab5e93af505c)(struct k\_mem\_slab \*slab);

5702

5704

5709

5710/\* kernel synchronized heap struct \*/

5711

[ 5712](structk__heap.md)struct [k\_heap](structk__heap.md) {

[ 5713](structk__heap.md#a4b8551f4fd1cd648c68f47ea2ebd682f) struct [sys\_heap](structsys__heap.md) [heap](structk__heap.md#a4b8551f4fd1cd648c68f47ea2ebd682f);

[ 5714](structk__heap.md#abd30d236bd986e791ea7698583e45588) \_wait\_q\_t [wait\_q](structk__heap.md#abd30d236bd986e791ea7698583e45588);

[ 5715](structk__heap.md#a3bd15b8ad69a6ab76b5c4a297673e5ec) struct [k\_spinlock](structk__spinlock.md) [lock](structk__heap.md#a3bd15b8ad69a6ab76b5c4a297673e5ec);

5716};

5717

[ 5731](group__heap__apis.md#ga9273e06dc8d6a351499f2f5abfdcb39f)void [k\_heap\_init](group__heap__apis.md#ga9273e06dc8d6a351499f2f5abfdcb39f)(struct [k\_heap](structk__heap.md) \*h, void \*mem,

5732 size\_t bytes) \_\_attribute\_nonnull(1);

5733

[ 5754](group__heap__apis.md#gaf77211a72441de389857bc13e10be4e6)void \*[k\_heap\_aligned\_alloc](group__heap__apis.md#gaf77211a72441de389857bc13e10be4e6)(struct [k\_heap](structk__heap.md) \*h, size\_t align, size\_t bytes,

5755 [k\_timeout\_t](structk__timeout__t.md) timeout) \_\_attribute\_nonnull(1);

5756

[ 5778](group__heap__apis.md#ga22b83564e50ae6177388dfe63e32a512)void \*[k\_heap\_alloc](group__heap__apis.md#ga22b83564e50ae6177388dfe63e32a512)(struct [k\_heap](structk__heap.md) \*h, size\_t bytes,

5779 [k\_timeout\_t](structk__timeout__t.md) timeout) \_\_attribute\_nonnull(1);

5780

[ 5803](group__heap__apis.md#ga53de68a83567cff1cff3eab5d8572449)void \*[k\_heap\_calloc](group__heap__apis.md#ga53de68a83567cff1cff3eab5d8572449)(struct [k\_heap](structk__heap.md) \*h, size\_t num, size\_t size, [k\_timeout\_t](structk__timeout__t.md) timeout)

5804 \_\_attribute\_nonnull(1);

5805

[ 5829](group__heap__apis.md#gabea4b2beae8ab138f2796fbeaa95d262)void \*[k\_heap\_realloc](group__heap__apis.md#gabea4b2beae8ab138f2796fbeaa95d262)(struct [k\_heap](structk__heap.md) \*h, void \*ptr, size\_t bytes, [k\_timeout\_t](structk__timeout__t.md) timeout)

5830 \_\_attribute\_nonnull(1);

5831

[ 5842](group__heap__apis.md#ga6cf917a0b3d91a0101192bd4808ada9c)void [k\_heap\_free](group__heap__apis.md#ga6cf917a0b3d91a0101192bd4808ada9c)(struct [k\_heap](structk__heap.md) \*h, void \*mem) \_\_attribute\_nonnull(1);

5843

5844/\* Hand-calculated minimum heap sizes needed to return a successful

5845 \* 1-byte allocation. See details in lib/os/heap.[ch]

5846 \*/

5847#define Z\_HEAP\_MIN\_SIZE ((sizeof(void \*) > 4) ? 56 : 44)

5848

5865#define Z\_HEAP\_DEFINE\_IN\_SECT(name, bytes, in\_section) \

5866 char in\_section \

5867 \_\_aligned(8) /\* CHUNK\_UNIT \*/ \

5868 kheap\_##name[MAX(bytes, Z\_HEAP\_MIN\_SIZE)]; \

5869 STRUCT\_SECTION\_ITERABLE(k\_heap, name) = { \

5870 .heap = { \

5871 .init\_mem = kheap\_##name, \

5872 .init\_bytes = MAX(bytes, Z\_HEAP\_MIN\_SIZE), \

5873 }, \

5874 }

5875

[ 5890](group__heap__apis.md#ga795d7f1e6d5b7b19a7a50198d7829a0f)#define K\_HEAP\_DEFINE(name, bytes) \

5891 Z\_HEAP\_DEFINE\_IN\_SECT(name, bytes, \

5892 \_\_noinit\_named(kheap\_buf\_##name))

5893

[ 5908](group__heap__apis.md#ga968f4c6a201fdf6862d62dd5d9f8d032)#define K\_HEAP\_DEFINE\_NOCACHE(name, bytes) \

5909 Z\_HEAP\_DEFINE\_IN\_SECT(name, bytes, \_\_nocache)

5910

[ 5920](group__heap__apis.md#ga3aa215396381e1513edf50bd9563dee5)int [k\_heap\_array\_get](group__heap__apis.md#ga3aa215396381e1513edf50bd9563dee5)(struct [k\_heap](structk__heap.md) \*\*heap);

5921

5925

5932

[ 5951](group__heap__apis.md#gae16d486aa250f9c07fa6a57342bcd3b4)void \*[k\_aligned\_alloc](group__heap__apis.md#gae16d486aa250f9c07fa6a57342bcd3b4)(size\_t align, size\_t size);

5952

[ 5964](group__heap__apis.md#gaa8edf1e63e5d5dd78d7adcfd787394ee)void \*[k\_malloc](group__heap__apis.md#gaa8edf1e63e5d5dd78d7adcfd787394ee)(size\_t size);

5965

[ 5976](group__heap__apis.md#ga79b63cc93b3358cf82d74f40e73b69d5)void [k\_free](group__heap__apis.md#ga79b63cc93b3358cf82d74f40e73b69d5)(void \*ptr);

5977

[ 5989](group__heap__apis.md#gad031d50ed62d08202a5dcf992c20246c)void \*[k\_calloc](group__heap__apis.md#gad031d50ed62d08202a5dcf992c20246c)(size\_t nmemb, size\_t size);

5990

[ 6008](group__heap__apis.md#ga852a7a60dce5853b6925897b24a54e02)void \*[k\_realloc](group__heap__apis.md#ga852a7a60dce5853b6925897b24a54e02)(void \*ptr, size\_t size);

6009

6011

6012/\* polling API - PRIVATE \*/

6013

6014#ifdef CONFIG\_POLL

6015#define \_INIT\_OBJ\_POLL\_EVENT(obj) do { (obj)->poll\_event = NULL; } while (false)

6016#else

6017#define \_INIT\_OBJ\_POLL\_EVENT(obj) do { } while (false)

6018#endif

6019

6020/\* private - types bit positions \*/

6021enum \_poll\_types\_bits {

6022 /\* can be used to ignore an event \*/

6023 \_POLL\_TYPE\_IGNORE,

6024

6025 /\* to be signaled by k\_poll\_signal\_raise() \*/

6026 \_POLL\_TYPE\_SIGNAL,

6027

6028 /\* semaphore availability \*/

6029 \_POLL\_TYPE\_SEM\_AVAILABLE,

6030

6031 /\* queue/FIFO/LIFO data availability \*/

6032 \_POLL\_TYPE\_DATA\_AVAILABLE,

6033

6034 /\* msgq data availability \*/

6035 \_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE,

6036

6037 /\* pipe data availability \*/

6038 \_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE,

6039

6040 \_POLL\_NUM\_TYPES

6041};

6042

6043#define Z\_POLL\_TYPE\_BIT(type) (1U << ((type) - 1U))

6044

6045/\* private - states bit positions \*/

6046enum \_poll\_states\_bits {

6047 /\* default state when creating event \*/

6048 \_POLL\_STATE\_NOT\_READY,

6049

6050 /\* signaled by k\_poll\_signal\_raise() \*/

6051 \_POLL\_STATE\_SIGNALED,

6052

6053 /\* semaphore is available \*/

6054 \_POLL\_STATE\_SEM\_AVAILABLE,

6055

6056 /\* data is available to read on queue/FIFO/LIFO \*/

6057 \_POLL\_STATE\_DATA\_AVAILABLE,

6058

6059 /\* queue/FIFO/LIFO wait was cancelled \*/

6060 \_POLL\_STATE\_CANCELLED,

6061

6062 /\* data is available to read on a message queue \*/

6063 \_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE,

6064

6065 /\* data is available to read from a pipe \*/

6066 \_POLL\_STATE\_PIPE\_DATA\_AVAILABLE,

6067

6068 \_POLL\_NUM\_STATES

6069};

6070

6071#define Z\_POLL\_STATE\_BIT(state) (1U << ((state) - 1U))

6072

6073#define \_POLL\_EVENT\_NUM\_UNUSED\_BITS \

6074 (32 - (0 \

6075 + 8 /\* tag \*/ \

6076 + \_POLL\_NUM\_TYPES \

6077 + \_POLL\_NUM\_STATES \

6078 + 1 /\* modes \*/ \

6079 ))

6080

6081/\* end of polling API - PRIVATE \*/

6082

6083

6091

6092/\* Public polling API \*/

6093

6094/\* public - values for k\_poll\_event.type bitfield \*/

[ 6095](group__poll__apis.md#gafd5d801eb9e9cf6097b2c08b4933998e)#define K\_POLL\_TYPE\_IGNORE 0

[ 6096](group__poll__apis.md#ga144d8eb34d85f6053e454410a10bf56a)#define K\_POLL\_TYPE\_SIGNAL Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_SIGNAL)

[ 6097](group__poll__apis.md#ga0fd7605bdffd43dff7480a90a603ffde)#define K\_POLL\_TYPE\_SEM\_AVAILABLE Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_SEM\_AVAILABLE)

[ 6098](group__poll__apis.md#ga58d656f73f031a39b8a936133fe5504f)#define K\_POLL\_TYPE\_DATA\_AVAILABLE Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_DATA\_AVAILABLE)

[ 6099](group__poll__apis.md#ga71734fee18c523cf70276260118afb91)#define K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE K\_POLL\_TYPE\_DATA\_AVAILABLE

[ 6100](group__poll__apis.md#gaa83509b54175fb6c98324422a928d5e1)#define K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE)

[ 6101](group__poll__apis.md#ga14e113201a3b3ad768c6a5ce917d1912)#define K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE)

6102

6103/\* public - polling modes \*/

[ 6104](group__poll__apis.md#ga36d7978872a83191dd3cc16d62165add)enum [k\_poll\_modes](group__poll__apis.md#ga36d7978872a83191dd3cc16d62165add) {

6105 /\* polling thread does not take ownership of objects when available \*/

[ 6106](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda22874743e2f6b0f1fd55c5375732b681) [K\_POLL\_MODE\_NOTIFY\_ONLY](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda22874743e2f6b0f1fd55c5375732b681) = 0,

6107

[ 6108](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c) [K\_POLL\_NUM\_MODES](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c)

6109};

6110

6111/\* public - values for k\_poll\_event.state bitfield \*/

[ 6112](group__poll__apis.md#ga522822c5e06a89b22ce4dcefd10c66aa)#define K\_POLL\_STATE\_NOT\_READY 0

[ 6113](group__poll__apis.md#ga478aae7fe4fb5c7b7c76ed216c22a7f1)#define K\_POLL\_STATE\_SIGNALED Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_SIGNALED)

[ 6114](group__poll__apis.md#gae9e3eefd5a29a538d22f53592578bb37)#define K\_POLL\_STATE\_SEM\_AVAILABLE Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_SEM\_AVAILABLE)

[ 6115](group__poll__apis.md#gac166d9919d591bace163c5211e7b41f4)#define K\_POLL\_STATE\_DATA\_AVAILABLE Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_DATA\_AVAILABLE)

[ 6116](group__poll__apis.md#gabd5ac3341698534f39ded718079d6168)#define K\_POLL\_STATE\_FIFO\_DATA\_AVAILABLE K\_POLL\_STATE\_DATA\_AVAILABLE

[ 6117](group__poll__apis.md#gac236074cd43f59f28b803fe2c4a4f6f7)#define K\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE)

[ 6118](group__poll__apis.md#ga9028d6868ee964ca25931ed9170068dd)#define K\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE)

[ 6119](group__poll__apis.md#gadaf4b4c8e13afb54114af72d133e1fdb)#define K\_POLL\_STATE\_CANCELLED Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_CANCELLED)

6120

6121/\* public - poll signal object \*/

[ 6122](structk__poll__signal.md)struct [k\_poll\_signal](structk__poll__signal.md) {

[ 6124](structk__poll__signal.md#a22e88955ba0e369d39edefadcf4c60fd) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [poll\_events](structk__poll__signal.md#a22e88955ba0e369d39edefadcf4c60fd);

6125

[ 6130](structk__poll__signal.md#ae9fe6751d75f7d2b2800cb723603c0fe) unsigned int [signaled](structk__poll__signal.md#ae9fe6751d75f7d2b2800cb723603c0fe);

6131

[ 6133](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1) int [result](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1);

6134};

6135

[ 6136](group__poll__apis.md#ga6d6321e189afca73a276cd671ec531ae)#define K\_POLL\_SIGNAL\_INITIALIZER(obj) \

6137 { \

6138 .poll\_events = SYS\_DLIST\_STATIC\_INIT(&obj.poll\_events), \

6139 .signaled = 0, \

6140 .result = 0, \

6141 }

6142

[ 6146](structk__poll__event.md)struct [k\_poll\_event](structk__poll__event.md) {

6148 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \_node;

6149

[ 6151](structk__poll__event.md#ad030c37b97f33e1bbb3361057180fa4f) struct z\_poller \*[poller](structk__poll__event.md#ad030c37b97f33e1bbb3361057180fa4f);

6152

[ 6154](structk__poll__event.md#a37c5f45deaa046b356d95af569220c70) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tag](structk__poll__event.md#a37c5f45deaa046b356d95af569220c70):8;

6155

[ 6157](structk__poll__event.md#a8f9e251aa8722eb4716f622e85be34ae) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [type](structk__poll__event.md#a8f9e251aa8722eb4716f622e85be34ae):\_POLL\_NUM\_TYPES;

6158

[ 6160](structk__poll__event.md#aaf4f32852d799a406bfeea4e57891129) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](structk__poll__event.md#aaf4f32852d799a406bfeea4e57891129):\_POLL\_NUM\_STATES;

6161

[ 6163](structk__poll__event.md#acca81763486ef5ebcc911cb1cbd6c899) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mode](structk__poll__event.md#acca81763486ef5ebcc911cb1cbd6c899):1;

6164

[ 6166](structk__poll__event.md#a750ac48e7aa3c8fb70814b24e951fc85) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unused](structk__poll__event.md#a750ac48e7aa3c8fb70814b24e951fc85):\_POLL\_EVENT\_NUM\_UNUSED\_BITS;

6167

6169 union {

6170 /\* The typed\_\* fields below are used by K\_POLL\_EVENT\_\*INITIALIZER() macros to ensure

6171 \* type safety of polled objects.

6172 \*/

[ 6173](structk__poll__event.md#aeaf67f9bc91d59fb2939e1469a088f2d) void \*[obj](structk__poll__event.md#aeaf67f9bc91d59fb2939e1469a088f2d), \*[typed\_K\_POLL\_TYPE\_IGNORE](structk__poll__event.md#a0864cb03742d24d4638d5fbcb1166c5b);

[ 6174](structk__poll__event.md#a130aaff7a8908993ed6be737a94a52ab) struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](structk__poll__event.md#a130aaff7a8908993ed6be737a94a52ab), \*[typed\_K\_POLL\_TYPE\_SIGNAL](structk__poll__event.md#ad54cb4ae8d3603db02af37c833a73430);

[ 6175](structk__poll__event.md#a9ed342b8a45884f985245f55b0e1c8cc) struct [k\_sem](structk__sem.md) \*[sem](structk__poll__event.md#a9ed342b8a45884f985245f55b0e1c8cc), \*[typed\_K\_POLL\_TYPE\_SEM\_AVAILABLE](structk__poll__event.md#aaa57f5741e3e3a133cf8331cd68750f3);

[ 6176](structk__poll__event.md#a4ba07f42f4af03f30478ebf48a1653f7) struct [k\_fifo](structk__fifo.md) \*[fifo](structk__poll__event.md#a4ba07f42f4af03f30478ebf48a1653f7), \*[typed\_K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE](structk__poll__event.md#af578a9a6cd21412619d1482a17acb1ec);

[ 6177](structk__poll__event.md#a6e30a6ce30702817895e66f22f0abedf) struct [k\_queue](structk__queue.md) \*[queue](structk__poll__event.md#a6e30a6ce30702817895e66f22f0abedf), \*[typed\_K\_POLL\_TYPE\_DATA\_AVAILABLE](structk__poll__event.md#aa19a70be95e65636da3ebe6104a21dec);

[ 6178](structk__poll__event.md#a5bbe94482a70ec13c2106f89afd2d59c) struct [k\_msgq](structk__msgq.md) \*[msgq](structk__poll__event.md#a5bbe94482a70ec13c2106f89afd2d59c), \*[typed\_K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE](structk__poll__event.md#a038392f2f0fd314837005dc7fb57a714);

[ 6179](structk__poll__event.md#a1640577da6460fa1f3c9b5507bb66c18) struct [k\_pipe](structk__pipe.md) \*[pipe](structk__poll__event.md#a1640577da6460fa1f3c9b5507bb66c18), \*[typed\_K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE](structk__poll__event.md#a7dd3857bbeaf15392fc4d4cad7263340);

6180 };

6181};

6182

[ 6183](group__poll__apis.md#ga8e3889f2bac281a6e65e31068e58047e)#define K\_POLL\_EVENT\_INITIALIZER(\_event\_type, \_event\_mode, \_event\_obj) \

6184 { \

6185 .poller = NULL, \

6186 .type = \_event\_type, \

6187 .state = K\_POLL\_STATE\_NOT\_READY, \

6188 .mode = \_event\_mode, \

6189 .unused = 0, \

6190 { \

6191 .typed\_##\_event\_type = \_event\_obj, \

6192 }, \

6193 }

6194

[ 6195](group__poll__apis.md#gada2366896d913dc916b3c28642648b63)#define K\_POLL\_EVENT\_STATIC\_INITIALIZER(\_event\_type, \_event\_mode, \_event\_obj, \

6196 event\_tag) \

6197 { \

6198 .tag = event\_tag, \

6199 .type = \_event\_type, \

6200 .state = K\_POLL\_STATE\_NOT\_READY, \

6201 .mode = \_event\_mode, \

6202 .unused = 0, \

6203 { \

6204 .typed\_##\_event\_type = \_event\_obj, \

6205 }, \

6206 }

6207

6222

[ 6223](group__poll__apis.md#gaa06bddd93a024fc5326d93187d80eb03)void [k\_poll\_event\_init](group__poll__apis.md#gaa06bddd93a024fc5326d93187d80eb03)(struct [k\_poll\_event](structk__poll__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type,

6224 int mode, void \*obj);

6225

6268

[ 6269](group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db)\_\_syscall int [k\_poll](group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db)(struct [k\_poll\_event](structk__poll__event.md) \*events, int num\_events,

6270 [k\_timeout\_t](structk__timeout__t.md) timeout);

6271

6279

[ 6280](group__poll__apis.md#gaee3090c2a912b93b6a5855e3018c3551)\_\_syscall void [k\_poll\_signal\_init](group__poll__apis.md#gaee3090c2a912b93b6a5855e3018c3551)(struct [k\_poll\_signal](structk__poll__signal.md) \*sig);

6281

[ 6287](group__poll__apis.md#ga02d899d1455ae1f3f55ffe8f1ebd6994)\_\_syscall void [k\_poll\_signal\_reset](group__poll__apis.md#ga02d899d1455ae1f3f55ffe8f1ebd6994)(struct [k\_poll\_signal](structk__poll__signal.md) \*sig);

6288

[ 6299](group__poll__apis.md#ga69dae11c7cb2c669caa411c3e7001311)\_\_syscall void [k\_poll\_signal\_check](group__poll__apis.md#ga69dae11c7cb2c669caa411c3e7001311)(struct [k\_poll\_signal](structk__poll__signal.md) \*sig,

6300 unsigned int \*signaled, int \*result);

6301

6325

[ 6326](group__poll__apis.md#gad0bf3825f828ec3ca37481bf3cbd6723)\_\_syscall int [k\_poll\_signal\_raise](group__poll__apis.md#gad0bf3825f828ec3ca37481bf3cbd6723)(struct [k\_poll\_signal](structk__poll__signal.md) \*sig, int result);

6327

6329

[ 6348](group__cpu__idle__apis.md#ga7b25e1bed511a813b32fbd0f91b09356)static inline void [k\_cpu\_idle](group__cpu__idle__apis.md#ga7b25e1bed511a813b32fbd0f91b09356)(void)

6349{

6350 [arch\_cpu\_idle](group__arch-pm.md#ga6ce051203e6cc091d0fb42a15f662a48)();

6351}

6352

[ 6367](group__cpu__idle__apis.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f)static inline void [k\_cpu\_atomic\_idle](group__cpu__idle__apis.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f)(unsigned int key)

6368{

6369 [arch\_cpu\_atomic\_idle](group__arch-pm.md#ga4d0297717c23a3cc5df434549e26924d)(key);

6370}

6371

6375

6380#ifdef ARCH\_EXCEPT

6381/\* This architecture has direct support for triggering a CPU exception \*/

6382#define z\_except\_reason(reason) ARCH\_EXCEPT(reason)

6383#else

6384

6385#if !defined(CONFIG\_ASSERT\_NO\_FILE\_INFO)

6386#define \_\_EXCEPT\_LOC() \_\_ASSERT\_PRINT("@ %s:%d\n", \_\_FILE\_\_, \_\_LINE\_\_)

6387#else

6388#define \_\_EXCEPT\_LOC()

6389#endif

6390

6391/\* NOTE: This is the implementation for arches that do not implement

6392 \* ARCH\_EXCEPT() to generate a real CPU exception.

6393 \*

6394 \* We won't have a real exception frame to determine the PC value when

6395 \* the oops occurred, so print file and line number before we jump into

6396 \* the fatal error handler.

6397 \*/

6398#define z\_except\_reason(reason) do { \

6399 \_\_EXCEPT\_LOC(); \

6400 z\_fatal\_error(reason, NULL); \

6401 } while (false)

6402

6403#endif /\* \_ARCH\_\_EXCEPT \*/

6407

[ 6419](kernel_8h.md#abde5aa8ca5e64a045b25b88f91370dcd)#define k\_oops() z\_except\_reason(K\_ERR\_KERNEL\_OOPS)

6420

[ 6429](kernel_8h.md#aedd541f707b1463aaac15c7798340329)#define k\_panic() z\_except\_reason(K\_ERR\_KERNEL\_PANIC)

6430

6434

6435/\*

6436 \* private APIs that are utilized by one or more public APIs

6437 \*/

6438

6442void z\_timer\_expiration\_handler(struct \_timeout \*timeout);

6446

6447#ifdef CONFIG\_PRINTK

6455\_\_syscall void k\_str\_out(char \*c, size\_t n);

6456#endif

6457

6463

[ 6484](group__float__apis.md#ga2df4b2550ace30512cddebd36b6a54a1)\_\_syscall int [k\_float\_disable](group__float__apis.md#ga2df4b2550ace30512cddebd36b6a54a1)(struct [k\_thread](structk__thread.md) \*thread);

6485

[ 6524](group__float__apis.md#ga81fb955ddd41658a9aad5c083f173f77)\_\_syscall int [k\_float\_enable](group__float__apis.md#ga81fb955ddd41658a9aad5c083f173f77)(struct [k\_thread](structk__thread.md) \*thread, unsigned int options);

6525

6529

[ 6537](kernel_8h.md#a82d886a1c911b39c1b47c32200cedac6)int [k\_thread\_runtime\_stats\_get](kernel_8h.md#a82d886a1c911b39c1b47c32200cedac6)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread,

6538 [k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) \*stats);

6539

[ 6546](kernel_8h.md#abd855bb83b3be393b46833e7854a193e)int [k\_thread\_runtime\_stats\_all\_get](kernel_8h.md#abd855bb83b3be393b46833e7854a193e)([k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) \*stats);

6547

[ 6555](kernel_8h.md#aefdd9027a50143262a7482c17873f169)int [k\_thread\_runtime\_stats\_cpu\_get](kernel_8h.md#aefdd9027a50143262a7482c17873f169)(int cpu, [k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) \*stats);

6556

[ 6566](kernel_8h.md#a3e52beb93fca2231d5860fe1cf1181fd)int [k\_thread\_runtime\_stats\_enable](kernel_8h.md#a3e52beb93fca2231d5860fe1cf1181fd)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

6567

[ 6577](kernel_8h.md#ae5ea2e05a602b7d5ee78a65ced61d63b)int [k\_thread\_runtime\_stats\_disable](kernel_8h.md#ae5ea2e05a602b7d5ee78a65ced61d63b)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

6578

[ 6586](kernel_8h.md#a54f2652ba1ed613219941eaaf193180c)void [k\_sys\_runtime\_stats\_enable](kernel_8h.md#a54f2652ba1ed613219941eaaf193180c)(void);

6587

[ 6595](kernel_8h.md#a2e3c96c0b11108ee7eca3f0666c780e0)void [k\_sys\_runtime\_stats\_disable](kernel_8h.md#a2e3c96c0b11108ee7eca3f0666c780e0)(void);

6596

6597#ifdef \_\_cplusplus

6598}

6599#endif

6600

6601#include <[zephyr/tracing/tracing.h](tracing_8h.md)>

6602#include <zephyr/syscalls/kernel.h>

6603

6604#endif /\* !\_ASMLANGUAGE \*/

6605

6606#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_H\_ \*/

[arch\_k\_cycle\_get\_32](arc_2v2_2misc_8h.md#a9ee9f897ec750957de45bf8d43349d5e)

static uint32\_t arch\_k\_cycle\_get\_32(void)

**Definition** misc.h:26

[arch\_k\_cycle\_get\_64](arc_2v2_2misc_8h.md#acc1ed8d949f694a1d39e389334caf971)

static uint64\_t arch\_k\_cycle\_get\_64(void)

**Definition** misc.h:33

[k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717)

void(\* k\_thread\_entry\_t)(void \*p1, void \*p2, void \*p3)

Thread entry point function type.

**Definition** arch\_interface.h:48

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:46

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[errno.h](errno_8h.md)

System error numbers.

[arch\_cpu\_atomic\_idle](group__arch-pm.md#ga4d0297717c23a3cc5df434549e26924d)

void arch\_cpu\_atomic\_idle(unsigned int key)

Atomically re-enable interrupts and enter low power mode.

[arch\_cpu\_idle](group__arch-pm.md#ga6ce051203e6cc091d0fb42a15f662a48)

void arch\_cpu\_idle(void)

Power save idle routine.

[atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)

static bool atomic\_test\_bit(const atomic\_t \*target, int bit)

Atomically get and test a bit.

**Definition** atomic.h:127

[atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)

static void atomic\_clear\_bit(atomic\_t \*target, int bit)

Atomically clear a bit.

**Definition** atomic.h:191

[atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)

static bool atomic\_test\_and\_set\_bit(atomic\_t \*target, int bit)

Atomically set a bit and test it.

**Definition** atomic.h:170

[k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)

static uint32\_t k\_cycle\_get\_32(void)

Read the hardware clock.

**Definition** kernel.h:1955

[K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)

#define K\_NO\_WAIT

Generate null timeout delay.

**Definition** kernel.h:1371

[k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)

int64\_t k\_uptime\_ticks(void)

Get system uptime, in system ticks.

[k\_uptime\_get\_32](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b)

static uint32\_t k\_uptime\_get\_32(void)

Get system uptime (32-bit version).

**Definition** kernel.h:1907

[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2)

uint32\_t k\_ticks\_t

Tick precision used in timeout APIs.

**Definition** clock.h:48

[k\_uptime\_delta](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80)

static int64\_t k\_uptime\_delta(int64\_t \*reftime)

Get elapsed time.

**Definition** kernel.h:1936

[k\_uptime\_seconds](group__clock__apis.md#gae082928ea608a8b180b4cb3a79d21a24)

static uint32\_t k\_uptime\_seconds(void)

Get system uptime in seconds.

**Definition** kernel.h:1920

[k\_cycle\_get\_64](group__clock__apis.md#gae09f509d02bf75a7b45d2800d823bb3a)

static uint64\_t k\_cycle\_get\_64(void)

Read the 64-bit hardware clock.

**Definition** kernel.h:1970

[k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)

static int64\_t k\_uptime\_get(void)

Get system uptime.

**Definition** kernel.h:1883

[k\_condvar\_signal](group__condvar__apis.md#ga0376a8f7dc6e4f1e1eed55940f43015b)

int k\_condvar\_signal(struct k\_condvar \*condvar)

Signals one thread that is pending on the condition variable.

[k\_condvar\_wait](group__condvar__apis.md#gab2e1d05db4f954755f430ca894e44dbc)

int k\_condvar\_wait(struct k\_condvar \*condvar, struct k\_mutex \*mutex, k\_timeout\_t timeout)

Waits on the condition variable releasing the mutex lock.

[k\_condvar\_init](group__condvar__apis.md#gac9b497c56cc4642965afa6c0c6d7ecfc)

int k\_condvar\_init(struct k\_condvar \*condvar)

Initialize a condition variable.

[k\_condvar\_broadcast](group__condvar__apis.md#gad2e46a7b9e1bc934fd1f5cb38dde40d8)

int k\_condvar\_broadcast(struct k\_condvar \*condvar)

Unblock all threads that are pending on the condition variable.

[k\_cpu\_idle](group__cpu__idle__apis.md#ga7b25e1bed511a813b32fbd0f91b09356)

static void k\_cpu\_idle(void)

Make the CPU idle.

**Definition** kernel.h:6348

[k\_cpu\_atomic\_idle](group__cpu__idle__apis.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f)

static void k\_cpu\_atomic\_idle(unsigned int key)

Make the CPU idle in an atomic fashion.

**Definition** kernel.h:6367

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:54

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:50

[k\_event\_wait](group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753)

uint32\_t k\_event\_wait(struct k\_event \*event, uint32\_t events, bool reset, k\_timeout\_t timeout)

Wait for any of the specified events.

[k\_event\_set\_masked](group__event__apis.md#ga29b3ec1022b12a8c34884da3559c5864)

uint32\_t k\_event\_set\_masked(struct k\_event \*event, uint32\_t events, uint32\_t events\_mask)

Set or clear the events in an event object.

[k\_event\_test](group__event__apis.md#ga81e66be0959e8cb0414d9772056a6264)

static uint32\_t k\_event\_test(struct k\_event \*event, uint32\_t events\_mask)

Test the events currently tracked in the event object.

**Definition** kernel.h:2520

[k\_event\_set](group__event__apis.md#gac22e9d768d003246e68b4b0b64e60f49)

uint32\_t k\_event\_set(struct k\_event \*event, uint32\_t events)

Set the events in an event object.

[k\_event\_post](group__event__apis.md#gac88d17410a71642a903890e420d23d76)

uint32\_t k\_event\_post(struct k\_event \*event, uint32\_t events)

Post one or more events to an event object.

[k\_event\_init](group__event__apis.md#gacf803590b39b095056f2b1c5090c4019)

void k\_event\_init(struct k\_event \*event)

Initialize an event object.

[k\_event\_clear](group__event__apis.md#gad6bfd7bfd0587bc70d3aa0b988010376)

uint32\_t k\_event\_clear(struct k\_event \*event, uint32\_t events)

Clear the events in an event object.

[k\_event\_wait\_all](group__event__apis.md#gaddd60a99de5ac3d84f643c9433b744c1)

uint32\_t k\_event\_wait\_all(struct k\_event \*event, uint32\_t events, bool reset, k\_timeout\_t timeout)

Wait for all of the specified events.

[sys\_sflist\_is\_empty](group__flagged-single-linked-list__apis.md#ga039ad5d35670e5d18acb38a174258a7e)

static bool sys\_sflist\_is\_empty(const sys\_sflist\_t \*list)

Test if the given list is empty.

**Definition** sflist.h:336

[sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66)

struct \_sflist sys\_sflist\_t

Flagged single-linked list structure.

**Definition** sflist.h:54

[k\_float\_disable](group__float__apis.md#ga2df4b2550ace30512cddebd36b6a54a1)

int k\_float\_disable(struct k\_thread \*thread)

Disable preservation of floating point context information.

[k\_float\_enable](group__float__apis.md#ga81fb955ddd41658a9aad5c083f173f77)

int k\_float\_enable(struct k\_thread \*thread, unsigned int options)

Enable preservation of floating point context information.

[k\_futex\_wait](group__futex__apis.md#ga596bfa265f88567ad9e80fd38cd433d3)

int k\_futex\_wait(struct k\_futex \*futex, int expected, k\_timeout\_t timeout)

Pend the current thread on a futex.

[k\_futex\_wake](group__futex__apis.md#ga62de1aeb7c5c273aed20d0e05336d7a0)

int k\_futex\_wake(struct k\_futex \*futex, bool wake\_all)

Wake one/all threads pending on a futex.

[k\_heap\_alloc](group__heap__apis.md#ga22b83564e50ae6177388dfe63e32a512)

void \* k\_heap\_alloc(struct k\_heap \*h, size\_t bytes, k\_timeout\_t timeout)

Allocate memory from a k\_heap.

[k\_heap\_array\_get](group__heap__apis.md#ga3aa215396381e1513edf50bd9563dee5)

int k\_heap\_array\_get(struct k\_heap \*\*heap)

Get the array of statically defined heaps.

[k\_heap\_calloc](group__heap__apis.md#ga53de68a83567cff1cff3eab5d8572449)

void \* k\_heap\_calloc(struct k\_heap \*h, size\_t num, size\_t size, k\_timeout\_t timeout)

Allocate and initialize memory for an array of objects from a k\_heap.

[k\_heap\_free](group__heap__apis.md#ga6cf917a0b3d91a0101192bd4808ada9c)

void k\_heap\_free(struct k\_heap \*h, void \*mem)

Free memory allocated by k\_heap\_alloc().

[k\_free](group__heap__apis.md#ga79b63cc93b3358cf82d74f40e73b69d5)

void k\_free(void \*ptr)

Free memory allocated from heap.

[k\_realloc](group__heap__apis.md#ga852a7a60dce5853b6925897b24a54e02)

void \* k\_realloc(void \*ptr, size\_t size)

Expand the size of an existing allocation.

[k\_heap\_init](group__heap__apis.md#ga9273e06dc8d6a351499f2f5abfdcb39f)

void k\_heap\_init(struct k\_heap \*h, void \*mem, size\_t bytes)

Initialize a k\_heap.

[k\_malloc](group__heap__apis.md#gaa8edf1e63e5d5dd78d7adcfd787394ee)

void \* k\_malloc(size\_t size)

Allocate memory from the heap.

[k\_heap\_realloc](group__heap__apis.md#gabea4b2beae8ab138f2796fbeaa95d262)

void \* k\_heap\_realloc(struct k\_heap \*h, void \*ptr, size\_t bytes, k\_timeout\_t timeout)

Reallocate memory from a k\_heap.

[k\_calloc](group__heap__apis.md#gad031d50ed62d08202a5dcf992c20246c)

void \* k\_calloc(size\_t nmemb, size\_t size)

Allocate memory from heap, array style.

[k\_aligned\_alloc](group__heap__apis.md#gae16d486aa250f9c07fa6a57342bcd3b4)

void \* k\_aligned\_alloc(size\_t align, size\_t size)

Allocate memory from the heap with a specified alignment.

[k\_heap\_aligned\_alloc](group__heap__apis.md#gaf77211a72441de389857bc13e10be4e6)

void \* k\_heap\_aligned\_alloc(struct k\_heap \*h, size\_t align, size\_t bytes, k\_timeout\_t timeout)

Allocate aligned memory from a k\_heap.

[k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)

bool k\_is\_in\_isr(void)

Determine if code is running at interrupt level.

[k\_is\_preempt\_thread](group__isr__apis.md#ga91e1cf0dc7fc93a3214cadb74ed86666)

int k\_is\_preempt\_thread(void)

Determine if code is running in a preemptible thread.

[k\_is\_pre\_kernel](group__isr__apis.md#gae74e5de996276df767b96d4b50fa47ea)

static bool k\_is\_pre\_kernel(void)

Test whether startup is in the before-main-task phase.

**Definition** kernel.h:1226

[k\_mbox\_get](group__mailbox__apis.md#ga2ea91154620b139dbed1ad949b97c3ef)

int k\_mbox\_get(struct k\_mbox \*mbox, struct k\_mbox\_msg \*rx\_msg, void \*buffer, k\_timeout\_t timeout)

Receive a mailbox message.

[k\_mbox\_data\_get](group__mailbox__apis.md#ga3d19e648e67f109609259543c9a01d6e)

void k\_mbox\_data\_get(struct k\_mbox\_msg \*rx\_msg, void \*buffer)

Retrieve mailbox message data into a buffer.

[k\_mbox\_init](group__mailbox__apis.md#ga686f20c199a9e971822d8279d175d8c2)

void k\_mbox\_init(struct k\_mbox \*mbox)

Initialize a mailbox.

[k\_mbox\_put](group__mailbox__apis.md#gaa1e5cdd992d8b9be11f82254e1886ed2)

int k\_mbox\_put(struct k\_mbox \*mbox, struct k\_mbox\_msg \*tx\_msg, k\_timeout\_t timeout)

Send a mailbox message in a synchronous manner.

[k\_mbox\_async\_put](group__mailbox__apis.md#gadd60f7b760371c0a141a1e4da253a0f0)

void k\_mbox\_async\_put(struct k\_mbox \*mbox, struct k\_mbox\_msg \*tx\_msg, struct k\_sem \*sem)

Send a mailbox message in an asynchronous manner.

[k\_mem\_slab\_init](group__mem__slab__apis.md#ga094a8f173f287e29bb287119c26889d1)

int k\_mem\_slab\_init(struct k\_mem\_slab \*slab, void \*buffer, size\_t block\_size, uint32\_t num\_blocks)

Initialize a memory slab.

[k\_mem\_slab\_free](group__mem__slab__apis.md#ga2635ea8f9a30b8751ec966fe62adc0e1)

void k\_mem\_slab\_free(struct k\_mem\_slab \*slab, void \*mem)

Free memory allocated from a memory slab.

[k\_mem\_slab\_runtime\_stats\_get](group__mem__slab__apis.md#ga32030a5cfb44f663bd31b4e1b3d5dddb)

int k\_mem\_slab\_runtime\_stats\_get(struct k\_mem\_slab \*slab, struct sys\_memory\_stats \*stats)

Get the memory stats for a memory slab.

[k\_mem\_slab\_runtime\_stats\_reset\_max](group__mem__slab__apis.md#gaa1f44e30f4aee98b38e1ab5e93af505c)

int k\_mem\_slab\_runtime\_stats\_reset\_max(struct k\_mem\_slab \*slab)

Reset the maximum memory usage for a slab.

[k\_mem\_slab\_alloc](group__mem__slab__apis.md#gab16a46d8394aca18de740ad044a8734a)

int k\_mem\_slab\_alloc(struct k\_mem\_slab \*slab, void \*\*mem, k\_timeout\_t timeout)

Allocate memory from a memory slab.

[k\_mem\_slab\_num\_used\_get](group__mem__slab__apis.md#gac76b96d7055e4ad94765c93530dd0720)

static uint32\_t k\_mem\_slab\_num\_used\_get(struct k\_mem\_slab \*slab)

Get the number of used blocks in a memory slab.

**Definition** kernel.h:5636

[k\_mem\_slab\_max\_used\_get](group__mem__slab__apis.md#gae0e949c1c3476dd57bc0c0ed627d2346)

static uint32\_t k\_mem\_slab\_max\_used\_get(struct k\_mem\_slab \*slab)

Get the number of maximum used blocks so far in a memory slab.

**Definition** kernel.h:5651

[k\_mem\_slab\_num\_free\_get](group__mem__slab__apis.md#gae87577e2873cf746db69216a82f94aea)

static uint32\_t k\_mem\_slab\_num\_free\_get(struct k\_mem\_slab \*slab)

Get the number of unused blocks in a memory slab.

**Definition** kernel.h:5671

[k\_msgq\_peek](group__msgq__apis.md#ga14f543472f2f63cfde0bdfa87b95c915)

int k\_msgq\_peek(struct k\_msgq \*msgq, void \*data)

Peek/read a message from a message queue.

[k\_msgq\_num\_used\_get](group__msgq__apis.md#ga458793a89f1d9f762bda3422918a9faa)

uint32\_t k\_msgq\_num\_used\_get(struct k\_msgq \*msgq)

Get the number of messages in a message queue.

[k\_msgq\_init](group__msgq__apis.md#ga54a5cdcaea2236c383ace433fedc0d39)

void k\_msgq\_init(struct k\_msgq \*msgq, char \*buffer, size\_t msg\_size, uint32\_t max\_msgs)

Initialize a message queue.

[k\_msgq\_put](group__msgq__apis.md#ga54e96aaaea5462a1f963b7fd5ca82bfe)

int k\_msgq\_put(struct k\_msgq \*msgq, const void \*data, k\_timeout\_t timeout)

Send a message to a message queue.

[k\_msgq\_peek\_at](group__msgq__apis.md#ga69b004a40ab4ca497de314a99960fb8e)

int k\_msgq\_peek\_at(struct k\_msgq \*msgq, void \*data, uint32\_t idx)

Peek/read a message from a message queue at the specified index.

[k\_msgq\_num\_free\_get](group__msgq__apis.md#ga7d154beb4f9c6227eddbef26d406ca24)

uint32\_t k\_msgq\_num\_free\_get(struct k\_msgq \*msgq)

Get the amount of free space in a message queue.

[k\_msgq\_get\_attrs](group__msgq__apis.md#ga8f9d3eef67cbc9c0717a84190bbf7f41)

void k\_msgq\_get\_attrs(struct k\_msgq \*msgq, struct k\_msgq\_attrs \*attrs)

Get basic attributes of a message queue.

[k\_msgq\_purge](group__msgq__apis.md#gaa18875887773195ae44b7fe0972ee760)

void k\_msgq\_purge(struct k\_msgq \*msgq)

Purge a message queue.

[k\_msgq\_alloc\_init](group__msgq__apis.md#gabe7305b8f442ebdc147dbbc6e8cf92fc)

int k\_msgq\_alloc\_init(struct k\_msgq \*msgq, size\_t msg\_size, uint32\_t max\_msgs)

Initialize a message queue.

[k\_msgq\_get](group__msgq__apis.md#gae67f2ced2df1f9c290ae15dab9097cb7)

int k\_msgq\_get(struct k\_msgq \*msgq, void \*data, k\_timeout\_t timeout)

Receive a message from a message queue.

[k\_msgq\_cleanup](group__msgq__apis.md#gafda4399aa9b8f1e44bdf752e00ea787b)

int k\_msgq\_cleanup(struct k\_msgq \*msgq)

Release allocated buffer for a queue.

[k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)

int k\_mutex\_unlock(struct k\_mutex \*mutex)

Unlock a mutex.

[k\_mutex\_init](group__mutex__apis.md#ga56b64952fb8b78b00268a21c28b41480)

int k\_mutex\_init(struct k\_mutex \*mutex)

Initialize a mutex.

[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)

int k\_mutex\_lock(struct k\_mutex \*mutex, k\_timeout\_t timeout)

Lock a mutex.

[k\_pipe\_write](group__pipe__apis.md#ga514ab3d174dcada766ecbda138944ddc)

int k\_pipe\_write(struct k\_pipe \*pipe, const uint8\_t \*data, size\_t len, k\_timeout\_t timeout)

Write data to a pipe.

[k\_pipe\_close](group__pipe__apis.md#ga83d4b5de8902845850d01b0c3db0702a)

void k\_pipe\_close(struct k\_pipe \*pipe)

Close a pipe.

[k\_pipe\_reset](group__pipe__apis.md#gaaedff72169127b8227c80bf8adf1f9dd)

void k\_pipe\_reset(struct k\_pipe \*pipe)

Reset a pipe This routine resets the pipe, discarding any unread data and unblocking any threads wait...

[k\_pipe\_init](group__pipe__apis.md#gae2c8d97af1f7e9deb93e670859525cf3)

void k\_pipe\_init(struct k\_pipe \*pipe, uint8\_t \*buffer, size\_t buffer\_size)

initialize a pipe

[pipe\_flags](group__pipe__apis.md#gae5471546043f4d14e97c3f6313053ee0)

pipe\_flags

**Definition** kernel.h:5296

[k\_pipe\_read](group__pipe__apis.md#gaecb07412025d9e065ee7b99121522257)

int k\_pipe\_read(struct k\_pipe \*pipe, uint8\_t \*data, size\_t len, k\_timeout\_t timeout)

Read data from a pipe This routine reads up to len bytes of data from pipe.

[PIPE\_FLAG\_RESET](group__pipe__apis.md#ggae5471546043f4d14e97c3f6313053ee0a37642c400a675e1dce34c9b878874df4)

@ PIPE\_FLAG\_RESET

**Definition** kernel.h:5298

[PIPE\_FLAG\_OPEN](group__pipe__apis.md#ggae5471546043f4d14e97c3f6313053ee0a9fc19eac7b41c00ca97c2fb0a30a2309)

@ PIPE\_FLAG\_OPEN

**Definition** kernel.h:5297

[k\_poll\_signal\_reset](group__poll__apis.md#ga02d899d1455ae1f3f55ffe8f1ebd6994)

void k\_poll\_signal\_reset(struct k\_poll\_signal \*sig)

Reset a poll signal object's state to unsignaled.

[k\_poll\_modes](group__poll__apis.md#ga36d7978872a83191dd3cc16d62165add)

k\_poll\_modes

**Definition** kernel.h:6104

[k\_poll\_signal\_check](group__poll__apis.md#ga69dae11c7cb2c669caa411c3e7001311)

void k\_poll\_signal\_check(struct k\_poll\_signal \*sig, unsigned int \*signaled, int \*result)

Fetch the signaled state and result value of a poll signal.

[k\_poll\_event\_init](group__poll__apis.md#gaa06bddd93a024fc5326d93187d80eb03)

void k\_poll\_event\_init(struct k\_poll\_event \*event, uint32\_t type, int mode, void \*obj)

Initialize one struct k\_poll\_event instance.

[k\_poll](group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db)

int k\_poll(struct k\_poll\_event \*events, int num\_events, k\_timeout\_t timeout)

Wait for one or many of multiple poll events to occur.

[k\_poll\_signal\_raise](group__poll__apis.md#gad0bf3825f828ec3ca37481bf3cbd6723)

int k\_poll\_signal\_raise(struct k\_poll\_signal \*sig, int result)

Signal a poll signal object.

[k\_poll\_signal\_init](group__poll__apis.md#gaee3090c2a912b93b6a5855e3018c3551)

void k\_poll\_signal\_init(struct k\_poll\_signal \*sig)

Initialize a poll signal object.

[K\_POLL\_MODE\_NOTIFY\_ONLY](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda22874743e2f6b0f1fd55c5375732b681)

@ K\_POLL\_MODE\_NOTIFY\_ONLY

**Definition** kernel.h:6106

[K\_POLL\_NUM\_MODES](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c)

@ K\_POLL\_NUM\_MODES

**Definition** kernel.h:6108

[k\_queue\_init](group__queue__apis.md#ga0236222d42768c2bf00942f328146c21)

void k\_queue\_init(struct k\_queue \*queue)

Initialize a queue.

[k\_queue\_get](group__queue__apis.md#ga0a77d8556e7d253319275de034f01619)

void \* k\_queue\_get(struct k\_queue \*queue, k\_timeout\_t timeout)

Get an element from a queue.

[k\_queue\_peek\_tail](group__queue__apis.md#ga27a460c42836d8b093ad9274c14bb176)

void \* k\_queue\_peek\_tail(struct k\_queue \*queue)

Peek element at the tail of queue.

[k\_queue\_unique\_append](group__queue__apis.md#ga287a2d81e2e3041be1cd45164e72f127)

bool k\_queue\_unique\_append(struct k\_queue \*queue, void \*data)

Append an element to a queue only if it's not present already.

[k\_queue\_remove](group__queue__apis.md#ga4bff929ed1d366a06e00865a5bbe2544)

bool k\_queue\_remove(struct k\_queue \*queue, void \*data)

Remove an element from a queue.

[k\_queue\_merge\_slist](group__queue__apis.md#ga4eee0da7442d60572b05d60a9996e69d)

int k\_queue\_merge\_slist(struct k\_queue \*queue, sys\_slist\_t \*list)

Atomically add a list of elements to a queue.

[k\_queue\_alloc\_append](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a)

int32\_t k\_queue\_alloc\_append(struct k\_queue \*queue, void \*data)

Append an element to a queue.

[k\_queue\_cancel\_wait](group__queue__apis.md#ga7c39d86cc6509f59ff9223cac3ea5071)

void k\_queue\_cancel\_wait(struct k\_queue \*queue)

Cancel waiting on a queue.

[k\_queue\_peek\_head](group__queue__apis.md#ga8ccd5137690c127a0f7d67619b88a52b)

void \* k\_queue\_peek\_head(struct k\_queue \*queue)

Peek element at the head of queue.

[k\_queue\_prepend](group__queue__apis.md#ga8ce013d8a037d4be5078797e0050e9c6)

void k\_queue\_prepend(struct k\_queue \*queue, void \*data)

Prepend an element to a queue.

[k\_queue\_append\_list](group__queue__apis.md#ga91d1a144fc2aeb3dd655accc94ca43aa)

int k\_queue\_append\_list(struct k\_queue \*queue, void \*head, void \*tail)

Atomically append a list of elements to a queue.

[k\_queue\_append](group__queue__apis.md#gaa84522a5ace6e7f8ba61033baca6972f)

void k\_queue\_append(struct k\_queue \*queue, void \*data)

Append an element to the end of a queue.

[k\_queue\_alloc\_prepend](group__queue__apis.md#gacf3dba40125073c11075e5a134919f88)

int32\_t k\_queue\_alloc\_prepend(struct k\_queue \*queue, void \*data)

Prepend an element to a queue.

[k\_queue\_insert](group__queue__apis.md#gad47336f27e433a52600a3b67ab89556a)

void k\_queue\_insert(struct k\_queue \*queue, void \*prev, void \*data)

Inserts an element to a queue.

[k\_queue\_is\_empty](group__queue__apis.md#gadb2bb8088868b3c5801c72b320389ca9)

int k\_queue\_is\_empty(struct k\_queue \*queue)

Query a queue to see if it has data available.

[k\_sem\_reset](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)

void k\_sem\_reset(struct k\_sem \*sem)

Resets a semaphore's count to zero.

[k\_sem\_count\_get](group__semaphore__apis.md#ga58843b581e170a1811fc38eecbfd01f3)

unsigned int k\_sem\_count\_get(struct k\_sem \*sem)

Get a semaphore's count.

[k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)

void k\_sem\_give(struct k\_sem \*sem)

Give a semaphore.

[k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)

int k\_sem\_take(struct k\_sem \*sem, k\_timeout\_t timeout)

Take a semaphore.

[k\_sem\_init](group__semaphore__apis.md#gadcd0e6cfba3392fb887222eafe4c1845)

int k\_sem\_init(struct k\_sem \*sem, unsigned int initial\_count, unsigned int limit)

Initialize a semaphore.

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[k\_stack\_pop](group__stack__apis.md#ga36ce6ceb9ea3d5c36d22b10430789480)

int k\_stack\_pop(struct k\_stack \*stack, stack\_data\_t \*data, k\_timeout\_t timeout)

Pop an element from a stack.

[k\_stack\_init](group__stack__apis.md#ga4400a39ef48289305cf66a092d5c6c7d)

void k\_stack\_init(struct k\_stack \*stack, stack\_data\_t \*buffer, uint32\_t num\_entries)

Initialize a stack.

[k\_stack\_cleanup](group__stack__apis.md#ga819f4e7b2cf11cf2e1b80933fdcb67ea)

int k\_stack\_cleanup(struct k\_stack \*stack)

Release a stack's allocated buffer.

[k\_stack\_push](group__stack__apis.md#gaa6180f4db6ec93ee84149cba054d3e53)

int k\_stack\_push(struct k\_stack \*stack, stack\_data\_t data)

Push an element onto a stack.

[k\_stack\_alloc\_init](group__stack__apis.md#gab97d924db1aef3f6adade156a107d45c)

int32\_t k\_stack\_alloc\_init(struct k\_stack \*stack, uint32\_t num\_entries)

Initialize a stack.

[SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)

#define SYS\_PORT\_TRACING\_TRACKING\_FIELD(type)

Field added to kernel objects so they are tracked.

**Definition** tracing\_macros.h:366

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)

#define CONTAINER\_OF(ptr, type, field)

Get a pointer to a structure containing the element.

**Definition** util.h:285

[EBUSY](group__system__errno.md#ga8368025077a0385849d6817b2007c095)

#define EBUSY

Mount device busy.

**Definition** errno.h:54

[k\_thread\_name\_copy](group__thread__apis.md#ga07b59ade055c69929ccdc08a14361794)

int k\_thread\_name\_copy(k\_tid\_t thread, char \*buf, size\_t size)

Copy the thread name into a supplied buffer.

[k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)

void k\_yield(void)

Yield the current thread.

[k\_thread\_state\_str](group__thread__apis.md#ga0c6af32096dc7ca391ffe2522bae4cb6)

const char \* k\_thread\_state\_str(k\_tid\_t thread\_id, char \*buf, size\_t buf\_size)

Get thread state string.

[k\_thread\_resume](group__thread__apis.md#ga117b26f8569ec3045ead1fad1851663d)

void k\_thread\_resume(k\_tid\_t thread)

Resume a suspended thread.

[k\_thread\_custom\_data\_get](group__thread__apis.md#ga19af063cff7b306ba28062996922740d)

void \* k\_thread\_custom\_data\_get(void)

Get current thread's custom data.

[k\_thread\_abort](group__thread__apis.md#ga1f44bb0307bea7a97227764ecd7bf963)

void k\_thread\_abort(k\_tid\_t thread)

Abort a thread.

[k\_thread\_name\_set](group__thread__apis.md#ga23107333f134b9c9a8b692374211e841)

int k\_thread\_name\_set(k\_tid\_t thread, const char \*str)

Set current thread name.

[k\_thread\_priority\_set](group__thread__apis.md#ga24e50a60c524d1eb22fe21cdf269b6a6)

void k\_thread\_priority\_set(k\_tid\_t thread, int prio)

Set a thread's priority.

[k\_thread\_cpu\_mask\_enable](group__thread__apis.md#ga306587604a7496db8059bd395fd90fc0)

int k\_thread\_cpu\_mask\_enable(k\_tid\_t thread, int cpu)

Enable thread to run on specified CPU.

[k\_thread\_foreach\_unlocked](group__thread__apis.md#ga30ef8b445a6c1b4a82651674dbb737fc)

void k\_thread\_foreach\_unlocked(k\_thread\_user\_cb\_t user\_cb, void \*user\_data)

Iterate over all the threads in the system without locking.

[k\_can\_yield](group__thread__apis.md#ga366b9daa0be65b0a69dbc9f146064b68)

bool k\_can\_yield(void)

Check whether it is possible to yield in the current context.

[k\_thread\_priority\_get](group__thread__apis.md#ga3a46ed8ad2c3b12416fafe11325f82b3)

int k\_thread\_priority\_get(k\_tid\_t thread)

Get a thread's priority.

[k\_thread\_heap\_assign](group__thread__apis.md#ga3f46c06833add2a2e0ddb7242f06702c)

static void k\_thread\_heap\_assign(struct k\_thread \*thread, struct k\_heap \*heap)

Assign a resource memory pool to a thread.

**Definition** kernel.h:485

[k\_thread\_user\_mode\_enter](group__thread__apis.md#ga3fbe1c8a5f3ef1c25382c7d6fca35764)

FUNC\_NORETURN void k\_thread\_user\_mode\_enter(k\_thread\_entry\_t entry, void \*p1, void \*p2, void \*p3)

Drop a thread's privileges permanently to user mode.

[k\_thread\_join](group__thread__apis.md#ga40a733561eb1f64dcaae0e01b167d233)

int k\_thread\_join(struct k\_thread \*thread, k\_timeout\_t timeout)

Sleep until a thread exits.

[k\_thread\_timeout\_remaining\_ticks](group__thread__apis.md#ga4688c095c86e037a18594efdb9a5e9b9)

k\_ticks\_t k\_thread\_timeout\_remaining\_ticks(const struct k\_thread \*thread)

Get time remaining before a thread wakes up, in system ticks.

[k\_thread\_custom\_data\_set](group__thread__apis.md#ga4834d9b81ed60c00eee77b0d4f8ab9e4)

void k\_thread\_custom\_data\_set(void \*value)

Set current thread's custom data.

[k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)

int32\_t k\_sleep(k\_timeout\_t timeout)

Put the current thread to sleep.

[k\_sched\_lock](group__thread__apis.md#ga4f0c5d0b9f279b12a4ad97db0c116a5f)

void k\_sched\_lock(void)

Lock the scheduler.

[k\_msleep](group__thread__apis.md#ga51307cdfe153ab3e918b18755d97c5d9)

static int32\_t k\_msleep(int32\_t ms)

Put the current thread to sleep.

**Definition** kernel.h:579

[k\_busy\_wait](group__thread__apis.md#ga550b642e071480323e589866abb99c22)

void k\_busy\_wait(uint32\_t usec\_to\_wait)

Cause the current thread to busy wait.

[k\_thread\_time\_slice\_set](group__thread__apis.md#ga563928f292a4134acd4142029b60e631)

void k\_thread\_time\_slice\_set(struct k\_thread \*th, int32\_t slice\_ticks, k\_thread\_timeslice\_fn\_t expired, void \*data)

Set thread time slice.

[k\_thread\_suspend](group__thread__apis.md#ga66cf8682fb65870eceb5e57d667a8d4e)

void k\_thread\_suspend(k\_tid\_t thread)

Suspend a thread.

[k\_sched\_unlock](group__thread__apis.md#ga7b26f64523cc4c36522cc828ccf85580)

void k\_sched\_unlock(void)

Unlock the scheduler.

[k\_current\_get](group__thread__apis.md#ga7ef1ed0fb9513df8096ede1e52fc76b2)

static \_\_attribute\_const\_\_ k\_tid\_t k\_current\_get(void)

Get thread ID of the current thread.

**Definition** kernel.h:676

[k\_thread\_cpu\_mask\_clear](group__thread__apis.md#ga80b9c58df6600c7e79f16756c128f44c)

int k\_thread\_cpu\_mask\_clear(k\_tid\_t thread)

Sets all CPU enable masks to zero.

[k\_thread\_foreach\_filter\_by\_cpu](group__thread__apis.md#ga82a83c2db36b34596dcb5afa5b28e41c)

void k\_thread\_foreach\_filter\_by\_cpu(unsigned int cpu, k\_thread\_user\_cb\_t user\_cb, void \*user\_data)

Iterate over all the threads in running on specified cpu.

[k\_sched\_time\_slice\_set](group__thread__apis.md#ga877c1bfeffbf8f097d1656f9e10a66e8)

void k\_sched\_time\_slice\_set(int32\_t slice, int prio)

Set time-slicing period and scope.

[k\_thread\_cpu\_mask\_disable](group__thread__apis.md#ga89e6c07ac112da75b2ef115d1a557d44)

int k\_thread\_cpu\_mask\_disable(k\_tid\_t thread, int cpu)

Prevent thread to run on specified CPU.

[k\_wakeup](group__thread__apis.md#ga9275a019c8ff3c7fe49a81f8c078157e)

void k\_wakeup(k\_tid\_t thread)

Wake up a sleeping thread.

[k\_thread\_stack\_free](group__thread__apis.md#ga95560cb85f6656b981a9a50ff2cd70b7)

int k\_thread\_stack\_free(k\_thread\_stack\_t \*stack)

Free a dynamically allocated thread stack.

[k\_thread\_timeout\_expires\_ticks](group__thread__apis.md#gab0b1c85b847fe74170c04538fa9949ff)

k\_ticks\_t k\_thread\_timeout\_expires\_ticks(const struct k\_thread \*thread)

Get time when a thread wakes up, in system ticks.

[k\_sched\_current\_thread\_query](group__thread__apis.md#gac3b994b90b5bccded0895304f6b20c5d)

\_\_attribute\_const\_\_ k\_tid\_t k\_sched\_current\_thread\_query(void)

Query thread ID of the current thread.

[k\_thread\_start](group__thread__apis.md#gac539268e0b45c600315a6567ec27f965)

static void k\_thread\_start(k\_tid\_t thread)

Start an inactive thread.

**Definition** kernel.h:1103

[k\_thread\_create](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367)

k\_tid\_t k\_thread\_create(struct k\_thread \*new\_thread, k\_thread\_stack\_t \*stack, size\_t stack\_size, k\_thread\_entry\_t entry, void \*p1, void \*p2, void \*p3, int prio, uint32\_t options, k\_timeout\_t delay)

Create a thread.

[k\_reschedule](group__thread__apis.md#gad82575e576cd08906fbc68fe36be48bd)

void k\_reschedule(void)

Invoke the scheduler.

[k\_thread\_deadline\_set](group__thread__apis.md#gad887f16c1dd6f3247682a83beb22d1ce)

void k\_thread\_deadline\_set(k\_tid\_t thread, int deadline)

Set deadline expiration time for scheduler.

[k\_thread\_foreach\_unlocked\_filter\_by\_cpu](group__thread__apis.md#gad908a1b9014aa048cf12997804ab7be2)

void k\_thread\_foreach\_unlocked\_filter\_by\_cpu(unsigned int cpu, k\_thread\_user\_cb\_t user\_cb, void \*user\_data)

Iterate over the threads in running on current cpu without locking.

[k\_thread\_name\_get](group__thread__apis.md#gadebf45da56dee393164569742459dc0a)

const char \* k\_thread\_name\_get(k\_tid\_t thread)

Get thread name.

[k\_thread\_foreach](group__thread__apis.md#gae2596d56800769b06fc03c194a126a97)

void k\_thread\_foreach(k\_thread\_user\_cb\_t user\_cb, void \*user\_data)

Iterate over all the threads in the system.

[k\_thread\_cpu\_pin](group__thread__apis.md#gae9ebd9845e14ed02944ab9282a185c03)

int k\_thread\_cpu\_pin(k\_tid\_t thread, int cpu)

Pin a thread to a CPU.

[k\_usleep](group__thread__apis.md#gaeac56bb072ce295b9fdc372ab8cee67e)

int32\_t k\_usleep(int32\_t us)

Put the current thread to sleep with microsecond resolution.

[k\_thread\_cpu\_mask\_enable\_all](group__thread__apis.md#gaedcfeb0964ae72611791241580b2119d)

int k\_thread\_cpu\_mask\_enable\_all(k\_tid\_t thread)

Sets all CPU enable masks to one.

[k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75)

void(\* k\_thread\_user\_cb\_t)(const struct k\_thread \*thread, void \*user\_data)

**Definition** kernel.h:106

[k\_thread\_stack\_alloc](group__thread__apis.md#gafe00cc70bac8a47ba6dda21bde508614)

k\_thread\_stack\_t \* k\_thread\_stack\_alloc(size\_t size, int flags)

Dynamically allocate a thread stack.

[k\_timer\_expires\_ticks](group__timer__apis.md#ga022b4cf5c8d0ee21b6a3b04fd425533f)

k\_ticks\_t k\_timer\_expires\_ticks(const struct k\_timer \*timer)

Get next expiration time of a timer, in system ticks.

[k\_timer\_stop\_t](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c)

void(\* k\_timer\_stop\_t)(struct k\_timer \*timer)

Timer stop function type.

**Definition** kernel.h:1661

[k\_timer\_remaining\_ticks](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4)

k\_ticks\_t k\_timer\_remaining\_ticks(const struct k\_timer \*timer)

Get time remaining before a timer next expires, in system ticks.

[k\_timer\_user\_data\_get](group__timer__apis.md#ga19a7d99a01a83828efd7f0d3bf2dd358)

void \* k\_timer\_user\_data\_get(const struct k\_timer \*timer)

Retrieve the user-specific data from a timer.

[k\_timer\_expiry\_t](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde)

void(\* k\_timer\_expiry\_t)(struct k\_timer \*timer)

Timer expiry function type.

**Definition** kernel.h:1645

[k\_timer\_init](group__timer__apis.md#ga318c846a740b901e5d56876a47ad7f61)

void k\_timer\_init(struct k\_timer \*timer, k\_timer\_expiry\_t expiry\_fn, k\_timer\_stop\_t stop\_fn)

Initialize a timer.

[k\_timer\_start](group__timer__apis.md#ga3ba70e9f059ff52fd2057ab89ea7f2ee)

void k\_timer\_start(struct k\_timer \*timer, k\_timeout\_t duration, k\_timeout\_t period)

Start a timer.

[k\_timer\_remaining\_get](group__timer__apis.md#ga6c6d8b0aa59bfa0f5924e95ccf756259)

static uint32\_t k\_timer\_remaining\_get(struct k\_timer \*timer)

Get time remaining before a timer next expires.

**Definition** kernel.h:1807

[k\_timer\_status\_sync](group__timer__apis.md#ga81d6d95b7021e26ad4cab161318e04f2)

uint32\_t k\_timer\_status\_sync(struct k\_timer \*timer)

Synchronize thread to timer expiration.

[k\_timer\_stop](group__timer__apis.md#ga8d3e3356a10d36570e16f7920e4c8772)

void k\_timer\_stop(struct k\_timer \*timer)

Stop a timer.

[k\_timer\_status\_get](group__timer__apis.md#gad532f4834cd4cf8be27b089e6ea347ce)

uint32\_t k\_timer\_status\_get(struct k\_timer \*timer)

Read timer status.

[k\_timer\_user\_data\_set](group__timer__apis.md#gadba1884961e790dd9c5d567de91cc7e2)

void k\_timer\_user\_data\_set(struct k\_timer \*timer, void \*user\_data)

Associate user-specific data with a timer.

[k\_ticks\_to\_ms\_floor32](group__timeutil__unit__apis.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)

#define k\_ticks\_to\_ms\_floor32(t)

Convert ticks to milliseconds.

**Definition** time\_units.h:1707

[k\_ticks\_to\_sec\_floor32](group__timeutil__unit__apis.md#ga824ffc9857fa2d4bccb3a9f4a56b8f18)

#define k\_ticks\_to\_sec\_floor32(t)

Convert ticks to seconds.

**Definition** time\_units.h:1611

[k\_ticks\_to\_ms\_floor64](group__timeutil__unit__apis.md#gac417ab53d5d493d95e24e7f777f8a4e0)

#define k\_ticks\_to\_ms\_floor64(t)

Convert ticks to milliseconds.

**Definition** time\_units.h:1723

[k\_work\_poll\_submit\_to\_queue](group__workqueue__apis.md#ga0abafd7f851e42fd3572c8438e600a53)

int k\_work\_poll\_submit\_to\_queue(struct k\_work\_q \*work\_q, struct k\_work\_poll \*work, struct k\_poll\_event \*events, int num\_events, k\_timeout\_t timeout)

Submit a triggered work item.

[k\_work\_queue\_thread\_get](group__workqueue__apis.md#ga0b8b496f7e7bd82d08590a07293e38d7)

static k\_tid\_t k\_work\_queue\_thread\_get(struct k\_work\_q \*queue)

Access the thread that animates a work queue.

**Definition** kernel.h:4298

[k\_work\_is\_pending](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)

static bool k\_work\_is\_pending(const struct k\_work \*work)

Test whether a work item is currently pending.

**Definition** kernel.h:4269

[k\_work\_queue\_drain](group__workqueue__apis.md#ga0fefe3e0225ac99b47b250849f6cd863)

int k\_work\_queue\_drain(struct k\_work\_q \*queue, bool plug)

Wait until the work queue has drained, optionally plugging it.

[k\_work\_delayable\_expires\_get](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624)

static k\_ticks\_t k\_work\_delayable\_expires\_get(const struct k\_work\_delayable \*dwork)

Get the absolute tick count at which a scheduled delayable work will be submitted.

**Definition** kernel.h:4286

[k\_work\_schedule\_for\_queue](group__workqueue__apis.md#ga17f863c9f6ff2fb41dc0f3b7de4fdf23)

int k\_work\_schedule\_for\_queue(struct k\_work\_q \*queue, struct k\_work\_delayable \*dwork, k\_timeout\_t delay)

Submit an idle work item to a queue after a delay.

[k\_work\_delayable\_busy\_get](group__workqueue__apis.md#ga1b76969667844f0981d348c9c671bc9f)

int k\_work\_delayable\_busy\_get(const struct k\_work\_delayable \*dwork)

Busy state flags from the delayable work item.

[k\_work\_queue\_stop](group__workqueue__apis.md#ga1fd2fce94eb731ccb0838ec763e62f5c)

int k\_work\_queue\_stop(struct k\_work\_q \*queue, k\_timeout\_t timeout)

Stop a work queue.

[k\_work\_init\_delayable](group__workqueue__apis.md#ga2876c5d82fb2340a093bc4d689a55465)

void k\_work\_init\_delayable(struct k\_work\_delayable \*dwork, k\_work\_handler\_t handler)

Initialize a delayable work structure.

[k\_work\_poll\_cancel](group__workqueue__apis.md#ga2a19547d04dc1a202e80b752e3177215)

int k\_work\_poll\_cancel(struct k\_work\_poll \*work)

Cancel a triggered work item.

[k\_work\_user\_queue\_start](group__workqueue__apis.md#ga3091bc8fab5311252e41634a97a18589)

void k\_work\_user\_queue\_start(struct k\_work\_user\_q \*work\_q, k\_thread\_stack\_t \*stack, size\_t stack\_size, int prio, const char \*name)

Start a workqueue in user mode.

[k\_work\_poll\_init](group__workqueue__apis.md#ga371dab33a40622bea19b07d852863443)

void k\_work\_poll\_init(struct k\_work\_poll \*work, k\_work\_handler\_t handler)

Initialize a triggered work item.

[k\_work\_cancel](group__workqueue__apis.md#ga389fe2a8fb20f9bd593cf8d990727078)

int k\_work\_cancel(struct k\_work \*work)

Cancel a work item.

[k\_work\_user\_submit\_to\_queue](group__workqueue__apis.md#ga50ae1f6f74c0bc0a41dbbf789fff8856)

static int k\_work\_user\_submit\_to\_queue(struct k\_work\_user\_q \*work\_q, struct k\_work\_user \*work)

Submit a work item to a user mode workqueue.

**Definition** kernel.h:4425

[k\_work\_submit\_to\_queue](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c)

int k\_work\_submit\_to\_queue(struct k\_work\_q \*queue, struct k\_work \*work)

Submit a work item to a queue.

[k\_work\_user\_is\_pending](group__workqueue__apis.md#ga58d05d4127e4cd51104a1f1a87f626cd)

static bool k\_work\_user\_is\_pending(struct k\_work\_user \*work)

Check if a userspace work item is pending.

**Definition** kernel.h:4402

[k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda)

void(\* k\_work\_handler\_t)(struct k\_work \*work)

The signature for a work item handler function.

**Definition** kernel.h:3442

[k\_work\_schedule](group__workqueue__apis.md#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)

int k\_work\_schedule(struct k\_work\_delayable \*dwork, k\_timeout\_t delay)

Submit an idle work item to the system work queue after a delay.

[k\_work\_delayable\_is\_pending](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e)

static bool k\_work\_delayable\_is\_pending(const struct k\_work\_delayable \*dwork)

Test whether a delayed work item is currently pending.

**Definition** kernel.h:4280

[k\_work\_cancel\_delayable\_sync](group__workqueue__apis.md#ga7e7ec237648556fc16bfda8d35f7cd86)

bool k\_work\_cancel\_delayable\_sync(struct k\_work\_delayable \*dwork, struct k\_work\_sync \*sync)

Cancel delayable work and wait.

[k\_work\_cancel\_delayable](group__workqueue__apis.md#ga92355914ee178d4c3e848a1946bed3e4)

int k\_work\_cancel\_delayable(struct k\_work\_delayable \*dwork)

Cancel delayable work.

[k\_work\_user\_init](group__workqueue__apis.md#ga9de9c7a7f13cc6b325e5453e34afe62d)

static void k\_work\_user\_init(struct k\_work\_user \*work, k\_work\_user\_handler\_t handler)

Initialize a userspace work item.

**Definition** kernel.h:4380

[k\_work\_queue\_unplug](group__workqueue__apis.md#gaa0463bb79af3ec470f7d3be02052139f)

int k\_work\_queue\_unplug(struct k\_work\_q \*queue)

Release a work queue to accept new submissions.

[k\_work\_reschedule](group__workqueue__apis.md#gaacaab408fb7c848d466ad1f069dfa648)

int k\_work\_reschedule(struct k\_work\_delayable \*dwork, k\_timeout\_t delay)

Reschedule a work item to the system work queue after a delay.

[k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc)

void(\* k\_work\_user\_handler\_t)(struct k\_work\_user \*work)

Work item handler function type for user work queues.

**Definition** kernel.h:4321

[k\_work\_cancel\_sync](group__workqueue__apis.md#gab2b05cfe3af08f7d32c3946fa1c808f9)

bool k\_work\_cancel\_sync(struct k\_work \*work, struct k\_work\_sync \*sync)

Cancel a work item and wait for it to complete.

[k\_work\_user\_queue\_thread\_get](group__workqueue__apis.md#gab487068e9564cd77b6bdbac3d5670923)

static k\_tid\_t k\_work\_user\_queue\_thread\_get(struct k\_work\_user\_q \*work\_q)

Access the user mode thread that animates a work queue.

**Definition** kernel.h:4480

[k\_work\_busy\_get](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b)

int k\_work\_busy\_get(const struct k\_work \*work)

Busy state flags from the work item.

[k\_work\_delayable\_from\_work](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca)

static struct k\_work\_delayable \* k\_work\_delayable\_from\_work(struct k\_work \*work)

Get the parent delayable work structure from a work pointer.

**Definition** kernel.h:4275

[k\_work\_delayable\_remaining\_get](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4)

static k\_ticks\_t k\_work\_delayable\_remaining\_get(const struct k\_work\_delayable \*dwork)

Get the number of ticks until a scheduled delayable work will be submitted.

**Definition** kernel.h:4292

[k\_work\_flush](group__workqueue__apis.md#gabd1cda459bab538fb2d6dfd84a73b253)

bool k\_work\_flush(struct k\_work \*work, struct k\_work\_sync \*sync)

Wait for last-submitted instance to complete.

[k\_work\_reschedule\_for\_queue](group__workqueue__apis.md#gabf5db091eac19b19a4e12c0cb381f0a8)

int k\_work\_reschedule\_for\_queue(struct k\_work\_q \*queue, struct k\_work\_delayable \*dwork, k\_timeout\_t delay)

Reschedule a work item to a queue after a delay.

[k\_work\_queue\_run](group__workqueue__apis.md#gac7fc60238574769e4eae6a2cc38da87b)

void k\_work\_queue\_run(struct k\_work\_q \*queue, const struct k\_work\_queue\_config \*cfg)

Run work queue using calling thread.

[k\_work\_submit](group__workqueue__apis.md#gace61b59575093d7442f39ccb7be686d7)

int k\_work\_submit(struct k\_work \*work)

Submit a work item to the system queue.

[k\_work\_flush\_delayable](group__workqueue__apis.md#gad47d54e513030304be2600d75b1a965f)

bool k\_work\_flush\_delayable(struct k\_work\_delayable \*dwork, struct k\_work\_sync \*sync)

Flush delayable work.

[k\_work\_poll\_submit](group__workqueue__apis.md#gad9f222e46d72c4f98739395a0c8bb4ea)

int k\_work\_poll\_submit(struct k\_work\_poll \*work, struct k\_poll\_event \*events, int num\_events, k\_timeout\_t timeout)

Submit a triggered work item to the system workqueue.

[k\_work\_queue\_init](group__workqueue__apis.md#gada77d818ea9e4d07c14a960872ed5492)

void k\_work\_queue\_init(struct k\_work\_q \*queue)

Initialize a work queue structure.

[k\_work\_queue\_start](group__workqueue__apis.md#gadfc56554f9bfe7b52309d79660188593)

void k\_work\_queue\_start(struct k\_work\_q \*queue, k\_thread\_stack\_t \*stack, size\_t stack\_size, int prio, const struct k\_work\_queue\_config \*cfg)

Initialize a work queue.

[k\_work\_init](group__workqueue__apis.md#gaf20080884a2893d39cd8e862b34a2a30)

void k\_work\_init(struct k\_work \*work, k\_work\_handler\_t handler)

Initialize a (non-delayable) work structure.

[K\_WORK\_CANCELING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732)

@ K\_WORK\_CANCELING

Flag indicating a work item that is being canceled.

**Definition** kernel.h:4049

[K\_WORK\_QUEUED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85)

@ K\_WORK\_QUEUED

Flag indicating a work item that has been submitted to a queue but has not started running.

**Definition** kernel.h:4056

[K\_WORK\_DELAYED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed)

@ K\_WORK\_DELAYED

Flag indicating a delayed work item that is scheduled for submission to a queue.

**Definition** kernel.h:4063

[K\_WORK\_RUNNING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165)

@ K\_WORK\_RUNNING

Flag indicating a work item that is running under a work queue thread.

**Definition** kernel.h:4043

[K\_WORK\_FLUSHING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601)

@ K\_WORK\_FLUSHING

Flag indicating a synced work item that is being flushed.

**Definition** kernel.h:4069

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:383

[k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf)

struct k\_thread\_runtime\_stats k\_thread\_runtime\_stats\_t

[k\_sys\_runtime\_stats\_disable](kernel_8h.md#a2e3c96c0b11108ee7eca3f0666c780e0)

void k\_sys\_runtime\_stats\_disable(void)

Disable gathering of system runtime statistics.

[k\_thread\_runtime\_stats\_enable](kernel_8h.md#a3e52beb93fca2231d5860fe1cf1181fd)

int k\_thread\_runtime\_stats\_enable(k\_tid\_t thread)

Enable gathering of runtime statistics for specified thread.

[k\_sys\_runtime\_stats\_enable](kernel_8h.md#a54f2652ba1ed613219941eaaf193180c)

void k\_sys\_runtime\_stats\_enable(void)

Enable gathering of system runtime statistics.

[k\_thread\_runtime\_stats\_get](kernel_8h.md#a82d886a1c911b39c1b47c32200cedac6)

int k\_thread\_runtime\_stats\_get(k\_tid\_t thread, k\_thread\_runtime\_stats\_t \*stats)

Get the runtime statistics of a thread.

[execution\_context\_types](kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779c)

execution\_context\_types

**Definition** kernel.h:91

[K\_ISR](kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779ca30593044743695f8184a157283dac4d5)

@ K\_ISR

**Definition** kernel.h:92

[K\_COOP\_THREAD](kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779ca62c0b731a1bb3c5e4aadeba3f93df58b)

@ K\_COOP\_THREAD

**Definition** kernel.h:93

[K\_PREEMPT\_THREAD](kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779cae84f57f4ac996c751d1f4c9e49789322)

@ K\_PREEMPT\_THREAD

**Definition** kernel.h:94

[k\_thread\_runtime\_stats\_all\_get](kernel_8h.md#abd855bb83b3be393b46833e7854a193e)

int k\_thread\_runtime\_stats\_all\_get(k\_thread\_runtime\_stats\_t \*stats)

Get the runtime statistics of all threads.

[k\_thread\_runtime\_stats\_disable](kernel_8h.md#ae5ea2e05a602b7d5ee78a65ced61d63b)

int k\_thread\_runtime\_stats\_disable(k\_tid\_t thread)

Disable gathering of runtime statistics for specified thread.

[k\_thread\_runtime\_stats\_cpu\_get](kernel_8h.md#aefdd9027a50143262a7482c17873f169)

int k\_thread\_runtime\_stats\_cpu\_get(int cpu, k\_thread\_runtime\_stats\_t \*stats)

Get the runtime statistics of all threads on specified cpu.

[kernel\_includes.h](kernel__includes_8h.md)

Header files included by kernel.h.

[k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f)

void(\* k\_thread\_timeslice\_fn\_t)(struct k\_thread \*thread, void \*data)

**Definition** kernel\_structs.h:310

[limits.h](limits_8h.md)

[mem\_stats.h](mem__stats_8h.md)

Memory Statistics.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[ring\_buffer.h](ring__buffer_8h.md)

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c)

\_\_INTPTR\_TYPE\_\_ intptr\_t

**Definition** stdint.h:104

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[k\_condvar](structk__condvar.md)

**Definition** kernel.h:3182

[k\_condvar::wait\_q](structk__condvar.md#a14b457a06420f093e779d569f4fea906)

\_wait\_q\_t wait\_q

**Definition** kernel.h:3183

[k\_event](structk__event.md)

Event Structure.

**Definition** kernel.h:2356

[k\_event::lock](structk__event.md#a1f0de9c69f29ad854f3b0d510ceb1efc)

struct k\_spinlock lock

**Definition** kernel.h:2359

[k\_event::events](structk__event.md#a54c6f5997132e88406ffa5bcc0a10b83)

uint32\_t events

**Definition** kernel.h:2358

[k\_event::wait\_q](structk__event.md#a5bacd5f2d34da646d9d7ee229842e432)

\_wait\_q\_t wait\_q

**Definition** kernel.h:2357

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2540

[k\_futex](structk__futex.md)

futex structure

**Definition** kernel.h:2277

[k\_futex::val](structk__futex.md#a454ad1b595b899306c8e9c8e1431e7a7)

atomic\_t val

**Definition** kernel.h:2278

[k\_heap](structk__heap.md)

**Definition** kernel.h:5712

[k\_heap::lock](structk__heap.md#a3bd15b8ad69a6ab76b5c4a297673e5ec)

struct k\_spinlock lock

**Definition** kernel.h:5715

[k\_heap::heap](structk__heap.md#a4b8551f4fd1cd648c68f47ea2ebd682f)

struct sys\_heap heap

**Definition** kernel.h:5713

[k\_heap::wait\_q](structk__heap.md#abd30d236bd986e791ea7698583e45588)

\_wait\_q\_t wait\_q

**Definition** kernel.h:5714

[k\_lifo](structk__lifo.md)

**Definition** kernel.h:2781

[k\_mbox\_msg](structk__mbox__msg.md)

Mailbox Message Structure.

**Definition** kernel.h:4933

[k\_mbox\_msg::tx\_target\_thread](structk__mbox__msg.md#a73236acb7d27bb0233f5abb7214fb19c)

k\_tid\_t tx\_target\_thread

target thread id

**Definition** kernel.h:4943

[k\_mbox\_msg::tx\_data](structk__mbox__msg.md#a74b0edeed4c44cb5932eb292efc9d9c2)

void \* tx\_data

sender's message data buffer

**Definition** kernel.h:4939

[k\_mbox\_msg::rx\_source\_thread](structk__mbox__msg.md#a9eb145a242ac66e80d90286d83fe7a61)

k\_tid\_t rx\_source\_thread

source thread id

**Definition** kernel.h:4941

[k\_mbox\_msg::info](structk__mbox__msg.md#aa79f2bf71431b474ec4551ade4d7a8dd)

uint32\_t info

application-defined information value

**Definition** kernel.h:4937

[k\_mbox\_msg::size](structk__mbox__msg.md#aeabf45e9599a64852a1cfd656b1ece8e)

size\_t size

size of message (in bytes)

**Definition** kernel.h:4935

[k\_mbox](structk__mbox.md)

Mailbox Structure.

**Definition** kernel.h:4955

[k\_mbox::tx\_msg\_queue](structk__mbox.md#a0bca912a50120707ddafa66d740ade96)

\_wait\_q\_t tx\_msg\_queue

Transmit messages queue.

**Definition** kernel.h:4957

[k\_mbox::lock](structk__mbox.md#a2c549d5bd7216b62d81ad2198e0d79e4)

struct k\_spinlock lock

**Definition** kernel.h:4960

[k\_mbox::rx\_msg\_queue](structk__mbox.md#a808a14c31892a2d042cdb0723a2956e2)

\_wait\_q\_t rx\_msg\_queue

Receive message queue.

**Definition** kernel.h:4959

[k\_mem\_domain](structk__mem__domain.md)

Memory Domain.

**Definition** mem\_domain.h:80

[k\_mem\_partition](structk__mem__partition.md)

Memory Partition.

**Definition** mem\_domain.h:55

[k\_msgq\_attrs](structk__msgq__attrs.md)

Message Queue Attributes.

**Definition** kernel.h:4701

[k\_msgq\_attrs::used\_msgs](structk__msgq__attrs.md#a00f936870442fa455117cbdd7821fac5)

uint32\_t used\_msgs

Used messages.

**Definition** kernel.h:4707

[k\_msgq\_attrs::msg\_size](structk__msgq__attrs.md#a7d1d72946bdd517c07da37493a89e30e)

size\_t msg\_size

Message Size.

**Definition** kernel.h:4703

[k\_msgq\_attrs::max\_msgs](structk__msgq__attrs.md#ad0f5894ba0da840b91eb85015252e649)

uint32\_t max\_msgs

Maximal number of messages.

**Definition** kernel.h:4705

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4640

[k\_msgq::msg\_size](structk__msgq.md#a512fe468da96540639a0d71f1707f79d)

size\_t msg\_size

Message size.

**Definition** kernel.h:4646

[k\_msgq::read\_ptr](structk__msgq.md#a594e8a4a638521f42f24f85fe0742d64)

char \* read\_ptr

Read pointer.

**Definition** kernel.h:4654

[k\_msgq::used\_msgs](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857)

uint32\_t used\_msgs

Number of used messages.

**Definition** kernel.h:4658

[k\_msgq::buffer\_end](structk__msgq.md#a9d47fd25d7a70e8518d45dd48c51f0e0)

char \* buffer\_end

End of message buffer.

**Definition** kernel.h:4652

[k\_msgq::lock](structk__msgq.md#aa2e00a7292502f0de88cff28c5e375f0)

struct k\_spinlock lock

Lock.

**Definition** kernel.h:4644

[k\_msgq::write\_ptr](structk__msgq.md#aacf9b7b9f6e26e402f3752fc56834f23)

char \* write\_ptr

Write pointer.

**Definition** kernel.h:4656

[k\_msgq::buffer\_start](structk__msgq.md#aca77f1cf833d3aa27ae65004b446bdd2)

char \* buffer\_start

Start of message buffer.

**Definition** kernel.h:4650

[k\_msgq::flags](structk__msgq.md#ae03025420908f8342ce12a1395c7657b)

uint8\_t flags

Message queue.

**Definition** kernel.h:4663

[k\_msgq::wait\_q](structk__msgq.md#ae3b3d53d60b789d69c65494cfd090076)

\_wait\_q\_t wait\_q

Message queue wait queue.

**Definition** kernel.h:4642

[k\_msgq::max\_msgs](structk__msgq.md#aebd3b6e91e97b2d4369feea1a3f7b7a0)

uint32\_t max\_msgs

Maximal number of messages.

**Definition** kernel.h:4648

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3070

[k\_mutex::lock\_count](structk__mutex.md#a0db401fc8e03e1f984b8fd15af974718)

uint32\_t lock\_count

Current lock count.

**Definition** kernel.h:3077

[k\_mutex::wait\_q](structk__mutex.md#a4add234295bceff22551ee74f3aed802)

\_wait\_q\_t wait\_q

Mutex wait queue.

**Definition** kernel.h:3072

[k\_mutex::owner\_orig\_prio](structk__mutex.md#ab0d16fac9f8af960a501ffd93ec08c80)

int owner\_orig\_prio

Original thread priority.

**Definition** kernel.h:3080

[k\_mutex::owner](structk__mutex.md#af910bb07dc99e50078de26fccca468e4)

struct k\_thread \* owner

Mutex owner.

**Definition** kernel.h:3074

[k\_obj\_core](structk__obj__core.md)

Object core structure.

**Definition** obj\_core.h:121

[k\_pipe](structk__pipe.md)

**Definition** kernel.h:5301

[k\_pipe::flags](structk__pipe.md#a2ed95fbe24ea20c4f292a66def1d4dde)

uint8\_t flags

**Definition** kernel.h:5307

[k\_pipe::buf](structk__pipe.md#a62556b1fbb907dcb8fbbe29c597d8473)

struct ring\_buf buf

**Definition** kernel.h:5303

[k\_pipe::data](structk__pipe.md#a8af11082e53b56670f0ce11e581766ff)

\_wait\_q\_t data

**Definition** kernel.h:5305

[k\_pipe::space](structk__pipe.md#aa1428192b88b97e0cb5ec83894770f47)

\_wait\_q\_t space

**Definition** kernel.h:5306

[k\_pipe::lock](structk__pipe.md#aa2a367a9c8f0be89bcdf1bf6d3b0b875)

struct k\_spinlock lock

**Definition** kernel.h:5304

[k\_pipe::waiting](structk__pipe.md#ac9162db42883d2c14f63cf74ff3c1179)

size\_t waiting

**Definition** kernel.h:5302

[k\_poll\_event](structk__poll__event.md)

Poll Event.

**Definition** kernel.h:6146

[k\_poll\_event::typed\_K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE](structk__poll__event.md#a038392f2f0fd314837005dc7fb57a714)

struct k\_msgq \* typed\_K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE

**Definition** kernel.h:6178

[k\_poll\_event::typed\_K\_POLL\_TYPE\_IGNORE](structk__poll__event.md#a0864cb03742d24d4638d5fbcb1166c5b)

void \* typed\_K\_POLL\_TYPE\_IGNORE

**Definition** kernel.h:6173

[k\_poll\_event::signal](structk__poll__event.md#a130aaff7a8908993ed6be737a94a52ab)

struct k\_poll\_signal \* signal

**Definition** kernel.h:6174

[k\_poll\_event::pipe](structk__poll__event.md#a1640577da6460fa1f3c9b5507bb66c18)

struct k\_pipe \* pipe

**Definition** kernel.h:6179

[k\_poll\_event::tag](structk__poll__event.md#a37c5f45deaa046b356d95af569220c70)

uint32\_t tag

optional user-specified tag, opaque, untouched by the API

**Definition** kernel.h:6154

[k\_poll\_event::fifo](structk__poll__event.md#a4ba07f42f4af03f30478ebf48a1653f7)

struct k\_fifo \* fifo

**Definition** kernel.h:6176

[k\_poll\_event::msgq](structk__poll__event.md#a5bbe94482a70ec13c2106f89afd2d59c)

struct k\_msgq \* msgq

**Definition** kernel.h:6178

[k\_poll\_event::queue](structk__poll__event.md#a6e30a6ce30702817895e66f22f0abedf)

struct k\_queue \* queue

**Definition** kernel.h:6177

[k\_poll\_event::unused](structk__poll__event.md#a750ac48e7aa3c8fb70814b24e951fc85)

uint32\_t unused

unused bits in 32-bit word

**Definition** kernel.h:6166

[k\_poll\_event::typed\_K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE](structk__poll__event.md#a7dd3857bbeaf15392fc4d4cad7263340)

struct k\_pipe \* typed\_K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE

**Definition** kernel.h:6179

[k\_poll\_event::type](structk__poll__event.md#a8f9e251aa8722eb4716f622e85be34ae)

uint32\_t type

bitfield of event types (bitwise-ORed K\_POLL\_TYPE\_xxx values)

**Definition** kernel.h:6157

[k\_poll\_event::sem](structk__poll__event.md#a9ed342b8a45884f985245f55b0e1c8cc)

struct k\_sem \* sem

**Definition** kernel.h:6175

[k\_poll\_event::typed\_K\_POLL\_TYPE\_DATA\_AVAILABLE](structk__poll__event.md#aa19a70be95e65636da3ebe6104a21dec)

struct k\_queue \* typed\_K\_POLL\_TYPE\_DATA\_AVAILABLE

**Definition** kernel.h:6177

[k\_poll\_event::typed\_K\_POLL\_TYPE\_SEM\_AVAILABLE](structk__poll__event.md#aaa57f5741e3e3a133cf8331cd68750f3)

struct k\_sem \* typed\_K\_POLL\_TYPE\_SEM\_AVAILABLE

**Definition** kernel.h:6175

[k\_poll\_event::state](structk__poll__event.md#aaf4f32852d799a406bfeea4e57891129)

uint32\_t state

bitfield of event states (bitwise-ORed K\_POLL\_STATE\_xxx values)

**Definition** kernel.h:6160

[k\_poll\_event::mode](structk__poll__event.md#acca81763486ef5ebcc911cb1cbd6c899)

uint32\_t mode

mode of operation, from enum k\_poll\_modes

**Definition** kernel.h:6163

[k\_poll\_event::poller](structk__poll__event.md#ad030c37b97f33e1bbb3361057180fa4f)

struct z\_poller \* poller

PRIVATE - DO NOT TOUCH.

**Definition** kernel.h:6151

[k\_poll\_event::typed\_K\_POLL\_TYPE\_SIGNAL](structk__poll__event.md#ad54cb4ae8d3603db02af37c833a73430)

struct k\_poll\_signal \* typed\_K\_POLL\_TYPE\_SIGNAL

**Definition** kernel.h:6174

[k\_poll\_event::obj](structk__poll__event.md#aeaf67f9bc91d59fb2939e1469a088f2d)

void \* obj

**Definition** kernel.h:6173

[k\_poll\_event::typed\_K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE](structk__poll__event.md#af578a9a6cd21412619d1482a17acb1ec)

struct k\_fifo \* typed\_K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE

**Definition** kernel.h:6176

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:6122

[k\_poll\_signal::poll\_events](structk__poll__signal.md#a22e88955ba0e369d39edefadcf4c60fd)

sys\_dlist\_t poll\_events

PRIVATE - DO NOT TOUCH.

**Definition** kernel.h:6124

[k\_poll\_signal::result](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1)

int result

custom result value passed to k\_poll\_signal\_raise() if needed

**Definition** kernel.h:6133

[k\_poll\_signal::signaled](structk__poll__signal.md#ae9fe6751d75f7d2b2800cb723603c0fe)

unsigned int signaled

1 if the event has been signaled, 0 otherwise.

**Definition** kernel.h:6130

[k\_queue](structk__queue.md)

**Definition** kernel.h:1985

[k\_queue::lock](structk__queue.md#a18fd165fec722384b3748bfdf3332a4c)

struct k\_spinlock lock

**Definition** kernel.h:1987

[k\_queue::wait\_q](structk__queue.md#a871d734f2b21a9cad3ca4a2ba79e64f1)

\_wait\_q\_t wait\_q

**Definition** kernel.h:1988

[k\_queue::data\_q](structk__queue.md#a892371af9701ce67619e38446bc2ceae)

sys\_sflist\_t data\_q

**Definition** kernel.h:1986

[k\_sem](structk__sem.md)

Semaphore structure.

**Definition** kernel.h:3275

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:262

[k\_thread::base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8)

struct \_thread\_base base

**Definition** thread.h:264

[k\_thread::resource\_pool](structk__thread.md#a35b859bded3a270f25ccc40efece7583)

struct k\_heap \* resource\_pool

resource pool

**Definition** thread.h:352

[k\_thread::entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03)

struct \_\_thread\_entry entry

thread entry and parameters description

**Definition** thread.h:291

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4101

[k\_work\_delayable::timeout](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d)

struct \_timeout timeout

**Definition** kernel.h:4106

[k\_work\_delayable::queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4)

struct k\_work\_q \* queue

**Definition** kernel.h:4109

[k\_work\_delayable::work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629)

struct k\_work work

**Definition** kernel.h:4103

[k\_work\_q](structk__work__q.md)

A structure used to hold work until it can be processed.

**Definition** kernel.h:4235

[k\_work\_q::pending](structk__work__q.md#a2012199571f6b658873550d64386b00c)

sys\_slist\_t pending

**Definition** kernel.h:4249

[k\_work\_q::drainq](structk__work__q.md#a308d1ac78b1203b7ea78b0f18c5bdf5b)

\_wait\_q\_t drainq

**Definition** kernel.h:4255

[k\_work\_q::thread\_id](structk__work__q.md#a48f58baa029424bb0bceb07361fe2e53)

k\_tid\_t thread\_id

**Definition** kernel.h:4242

[k\_work\_q::notifyq](structk__work__q.md#a561c90f8bb944217230e00052cdecf10)

\_wait\_q\_t notifyq

**Definition** kernel.h:4252

[k\_work\_q::flags](structk__work__q.md#a68bc8e9c412ebdbf34827087d91a080e)

uint32\_t flags

**Definition** kernel.h:4258

[k\_work\_q::thread](structk__work__q.md#aa42ca271a4989f129bf1a43c491327eb)

struct k\_thread thread

**Definition** kernel.h:4237

[k\_work\_queue\_config](structk__work__queue__config.md)

A structure holding optional configuration items for a work queue.

**Definition** kernel.h:4197

[k\_work\_queue\_config::name](structk__work__queue__config.md#a0929d83372efff6798bc69bb7ca1eaaa)

const char \* name

The name to be given to the work queue thread.

**Definition** kernel.h:4202

[k\_work\_queue\_config::work\_timeout\_ms](structk__work__queue__config.md#a517d9895f211d886de4b18f2f16d06c3)

uint32\_t work\_timeout\_ms

Controls whether work queue monitors work timeouts.

**Definition** kernel.h:4231

[k\_work\_queue\_config::essential](structk__work__queue__config.md#a5aa4a80d91ef36498443c163428b02c0)

bool essential

Control whether the work queue thread should be marked as essential thread.

**Definition** kernel.h:4221

[k\_work\_queue\_config::no\_yield](structk__work__queue__config.md#afcf64d6e69d1ddfff8cbd749dafa4d13)

bool no\_yield

Control whether the work queue thread should yield between items.

**Definition** kernel.h:4216

[k\_work\_sync](structk__work__sync.md)

A structure holding internal state for a pending synchronous operation on a work item or queue.

**Definition** kernel.h:4184

[k\_work\_sync::canceller](structk__work__sync.md#a7e8fd0b9d6736c403aefa8462c7c0835)

struct z\_work\_canceller canceller

**Definition** kernel.h:4187

[k\_work\_sync::flusher](structk__work__sync.md#ad81ff57cb9f2f3dc5f2d65917cf04f1c)

struct z\_work\_flusher flusher

**Definition** kernel.h:4186

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:4073

[k\_work::handler](structk__work.md#a096d6ca1338fb0fbfa330b790136f172)

k\_work\_handler\_t handler

**Definition** kernel.h:4082

[k\_work::flags](structk__work.md#a391ed7d2039cd05c9894267bf8ea4dfd)

uint32\_t flags

**Definition** kernel.h:4093

[k\_work::queue](structk__work.md#a551be8394e041020c36a97dc2e12e137)

struct k\_work\_q \* queue

**Definition** kernel.h:4085

[k\_work::node](structk__work.md#a85772682983e0fdeb735f0821d5710d4)

sys\_snode\_t node

**Definition** kernel.h:4079

[ring\_buf](structring__buf.md)

A structure to represent a ring buffer.

**Definition** ring\_buffer.h:49

[sys\_heap](structsys__heap.md)

**Definition** sys\_heap.h:57

[sys\_memory\_stats](structsys__memory__stats.md)

**Definition** mem\_stats.h:24

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[tracing.h](tracing_8h.md)

[tracing\_macros.h](tracing__macros_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel.h](kernel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
