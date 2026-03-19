---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/kernel_8h_source.html
original_path: doxygen/html/kernel_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

74struct k\_sem;

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

[ 346](group__thread__apis.md#gafe00cc70bac8a47ba6dda21bde508614)\_\_syscall [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[k\_thread\_stack\_alloc](group__thread__apis.md#gafe00cc70bac8a47ba6dda21bde508614)(size\_t size, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

347

[ 360](group__thread__apis.md#ga95560cb85f6656b981a9a50ff2cd70b7)\_\_syscall int [k\_thread\_stack\_free](group__thread__apis.md#ga95560cb85f6656b981a9a50ff2cd70b7)([k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack);

361

[ 410](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367)\_\_syscall [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_thread\_create](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367)(struct [k\_thread](structk__thread.md) \*new\_thread,

411 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack,

412 size\_t stack\_size,

413 [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) [entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03),

414 void \*p1, void \*p2, void \*p3,

415 int prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) options, [k\_timeout\_t](structk__timeout__t.md) delay);

416

[ 438](group__thread__apis.md#ga3fbe1c8a5f3ef1c25382c7d6fca35764)FUNC\_NORETURN void [k\_thread\_user\_mode\_enter](group__thread__apis.md#ga3fbe1c8a5f3ef1c25382c7d6fca35764)([k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) [entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03),

439 void \*p1, void \*p2,

440 void \*p3);

441

[ 455](group__thread__apis.md#gafec540511e6d2e0a074a5bfb515c53b0)#define k\_thread\_access\_grant(thread, ...) \

456 FOR\_EACH\_FIXED\_ARG(k\_object\_access\_grant, (;), (thread), \_\_VA\_ARGS\_\_)

457

[ 472](group__thread__apis.md#ga3f46c06833add2a2e0ddb7242f06702c)static inline void [k\_thread\_heap\_assign](group__thread__apis.md#ga3f46c06833add2a2e0ddb7242f06702c)(struct [k\_thread](structk__thread.md) \*thread,

473 struct [k\_heap](structk__heap.md) \*heap)

474{

475 thread->[resource\_pool](structk__thread.md#a35b859bded3a270f25ccc40efece7583) = heap;

476}

477

478#if defined(CONFIG\_INIT\_STACKS) && defined(CONFIG\_THREAD\_STACK\_INFO)

499\_\_syscall int k\_thread\_stack\_space\_get(const struct [k\_thread](structk__thread.md) \*thread,

500 size\_t \*unused\_ptr);

501#endif

502

503#if (K\_HEAP\_MEM\_POOL\_SIZE > 0)

516void k\_thread\_system\_pool\_assign(struct [k\_thread](structk__thread.md) \*thread);

517#endif /\* (K\_HEAP\_MEM\_POOL\_SIZE > 0) \*/

518

[ 538](group__thread__apis.md#ga40a733561eb1f64dcaae0e01b167d233)\_\_syscall int [k\_thread\_join](group__thread__apis.md#ga40a733561eb1f64dcaae0e01b167d233)(struct [k\_thread](structk__thread.md) \*thread, [k\_timeout\_t](structk__timeout__t.md) timeout);

539

[ 552](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)([k\_timeout\_t](structk__timeout__t.md) timeout);

553

[ 565](group__thread__apis.md#ga51307cdfe153ab3e918b18755d97c5d9)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_msleep](group__thread__apis.md#ga51307cdfe153ab3e918b18755d97c5d9)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ms)

566{

567 return [k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)(Z\_TIMEOUT\_MS(ms));

568}

569

[ 586](group__thread__apis.md#gaeac56bb072ce295b9fdc372ab8cee67e)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_usleep](group__thread__apis.md#gaeac56bb072ce295b9fdc372ab8cee67e)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) us);

587

[ 604](group__thread__apis.md#ga550b642e071480323e589866abb99c22)\_\_syscall void [k\_busy\_wait](group__thread__apis.md#ga550b642e071480323e589866abb99c22)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usec\_to\_wait);

605

[ 617](group__thread__apis.md#ga366b9daa0be65b0a69dbc9f146064b68)bool [k\_can\_yield](group__thread__apis.md#ga366b9daa0be65b0a69dbc9f146064b68)(void);

618

[ 626](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)\_\_syscall void [k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)(void);

627

[ 637](group__thread__apis.md#ga9275a019c8ff3c7fe49a81f8c078157e)\_\_syscall void [k\_wakeup](group__thread__apis.md#ga9275a019c8ff3c7fe49a81f8c078157e)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

638

652\_\_attribute\_const\_\_

[ 653](group__thread__apis.md#gac3b994b90b5bccded0895304f6b20c5d)\_\_syscall [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_sched\_current\_thread\_query](group__thread__apis.md#gac3b994b90b5bccded0895304f6b20c5d)(void);

654

661\_\_attribute\_const\_\_

[ 662](group__thread__apis.md#ga7ef1ed0fb9513df8096ede1e52fc76b2)static inline [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_current\_get](group__thread__apis.md#ga7ef1ed0fb9513df8096ede1e52fc76b2)(void)

663{

664#ifdef CONFIG\_CURRENT\_THREAD\_USE\_TLS

665

666 /\* Thread-local cache of current thread ID, set in z\_thread\_entry() \*/

667 extern Z\_THREAD\_LOCAL [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) z\_tls\_current;

668

669 return z\_tls\_current;

670#else

671 return [k\_sched\_current\_thread\_query](group__thread__apis.md#gac3b994b90b5bccded0895304f6b20c5d)();

672#endif

673}

674

[ 694](group__thread__apis.md#ga1f44bb0307bea7a97227764ecd7bf963)\_\_syscall void [k\_thread\_abort](group__thread__apis.md#ga1f44bb0307bea7a97227764ecd7bf963)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

695

696[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_timeout\_expires(const struct \_timeout \*timeout);

697[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_timeout\_remaining(const struct \_timeout \*timeout);

698

699#ifdef CONFIG\_SYS\_CLOCK\_EXISTS

700

[ 708](group__thread__apis.md#gab0b1c85b847fe74170c04538fa9949ff)\_\_syscall [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_thread\_timeout\_expires\_ticks](group__thread__apis.md#gab0b1c85b847fe74170c04538fa9949ff)(const struct [k\_thread](structk__thread.md) \*thread);

709

710static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_impl\_k\_thread\_timeout\_expires\_ticks(

711 const struct [k\_thread](structk__thread.md) \*thread)

712{

713 return z\_timeout\_expires(&thread->[base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8).timeout);

714}

715

[ 723](group__thread__apis.md#ga4688c095c86e037a18594efdb9a5e9b9)\_\_syscall [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_thread\_timeout\_remaining\_ticks](group__thread__apis.md#ga4688c095c86e037a18594efdb9a5e9b9)(const struct [k\_thread](structk__thread.md) \*thread);

724

725static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_impl\_k\_thread\_timeout\_remaining\_ticks(

726 const struct [k\_thread](structk__thread.md) \*thread)

727{

728 return z\_timeout\_remaining(&thread->[base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8).timeout);

729}

730

731#endif /\* CONFIG\_SYS\_CLOCK\_EXISTS \*/

732

736

737struct \_static\_thread\_data {

738 struct k\_thread \*init\_thread;

739 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*init\_stack;

740 unsigned int init\_stack\_size;

741 [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) init\_entry;

742 void \*init\_p1;

743 void \*init\_p2;

744 void \*init\_p3;

745 int init\_prio;

746 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) init\_options;

747 const char \*init\_name;

748#ifdef CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME

749 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) init\_delay\_ms;

750#else

751 k\_timeout\_t init\_delay;

752#endif

753};

754

755#ifdef CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME

756#define Z\_THREAD\_INIT\_DELAY\_INITIALIZER(ms) .init\_delay\_ms = (ms)

757#define Z\_THREAD\_INIT\_DELAY(thread) SYS\_TIMEOUT\_MS((thread)->init\_delay\_ms)

758#else

759#define Z\_THREAD\_INIT\_DELAY\_INITIALIZER(ms) .init\_delay = SYS\_TIMEOUT\_MS\_INIT(ms)

760#define Z\_THREAD\_INIT\_DELAY(thread) (thread)->init\_delay

761#endif

762

763#define Z\_THREAD\_INITIALIZER(thread, stack, stack\_size, \

764 entry, p1, p2, p3, \

765 prio, options, delay, tname) \

766 { \

767 .init\_thread = (thread), \

768 .init\_stack = (stack), \

769 .init\_stack\_size = (stack\_size), \

770 .init\_entry = (k\_thread\_entry\_t)entry, \

771 .init\_p1 = (void \*)p1, \

772 .init\_p2 = (void \*)p2, \

773 .init\_p3 = (void \*)p3, \

774 .init\_prio = (prio), \

775 .init\_options = (options), \

776 .init\_name = STRINGIFY(tname), \

777 Z\_THREAD\_INIT\_DELAY\_INITIALIZER(delay) \

778 }

779

780/\*

781 \* Refer to K\_THREAD\_DEFINE() and K\_KERNEL\_THREAD\_DEFINE() for

782 \* information on arguments.

783 \*/

784#define Z\_THREAD\_COMMON\_DEFINE(name, stack\_size, \

785 entry, p1, p2, p3, \

786 prio, options, delay) \

787 struct k\_thread \_k\_thread\_obj\_##name; \

788 STRUCT\_SECTION\_ITERABLE(\_static\_thread\_data, \

789 \_k\_thread\_data\_##name) = \

790 Z\_THREAD\_INITIALIZER(&\_k\_thread\_obj\_##name, \

791 \_k\_thread\_stack\_##name, stack\_size,\

792 entry, p1, p2, p3, prio, options, \

793 delay, name); \

794 const k\_tid\_t name = (k\_tid\_t)&\_k\_thread\_obj\_##name

795

799

[ 831](group__thread__apis.md#gab3ced58648ca35788a40676e8478ecd2)#define K\_THREAD\_DEFINE(name, stack\_size, \

832 entry, p1, p2, p3, \

833 prio, options, delay) \

834 K\_THREAD\_STACK\_DEFINE(\_k\_thread\_stack\_##name, stack\_size); \

835 Z\_THREAD\_COMMON\_DEFINE(name, stack\_size, entry, p1, p2, p3, \

836 prio, options, delay)

837

[ 868](group__thread__apis.md#gae25853424ec969f8431862c46b3ec294)#define K\_KERNEL\_THREAD\_DEFINE(name, stack\_size, \

869 entry, p1, p2, p3, \

870 prio, options, delay) \

871 K\_KERNEL\_STACK\_DEFINE(\_k\_thread\_stack\_##name, stack\_size); \

872 Z\_THREAD\_COMMON\_DEFINE(name, stack\_size, entry, p1, p2, p3, \

873 prio, options, delay)

874

[ 884](group__thread__apis.md#ga3a46ed8ad2c3b12416fafe11325f82b3)\_\_syscall int [k\_thread\_priority\_get](group__thread__apis.md#ga3a46ed8ad2c3b12416fafe11325f82b3)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

885

[ 911](group__thread__apis.md#ga24e50a60c524d1eb22fe21cdf269b6a6)\_\_syscall void [k\_thread\_priority\_set](group__thread__apis.md#ga24e50a60c524d1eb22fe21cdf269b6a6)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int prio);

912

913

914#ifdef CONFIG\_SCHED\_DEADLINE

[ 947](group__thread__apis.md#gad887f16c1dd6f3247682a83beb22d1ce)\_\_syscall void [k\_thread\_deadline\_set](group__thread__apis.md#gad887f16c1dd6f3247682a83beb22d1ce)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int deadline);

948#endif

949

[ 968](group__thread__apis.md#gad82575e576cd08906fbc68fe36be48bd)\_\_syscall void [k\_reschedule](group__thread__apis.md#gad82575e576cd08906fbc68fe36be48bd)(void);

969

970#ifdef CONFIG\_SCHED\_CPU\_MASK

[ 983](group__thread__apis.md#ga80b9c58df6600c7e79f16756c128f44c)int [k\_thread\_cpu\_mask\_clear](group__thread__apis.md#ga80b9c58df6600c7e79f16756c128f44c)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

984

[ 997](group__thread__apis.md#gaedcfeb0964ae72611791241580b2119d)int [k\_thread\_cpu\_mask\_enable\_all](group__thread__apis.md#gaedcfeb0964ae72611791241580b2119d)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

998

[ 1011](group__thread__apis.md#ga306587604a7496db8059bd395fd90fc0)int [k\_thread\_cpu\_mask\_enable](group__thread__apis.md#ga306587604a7496db8059bd395fd90fc0)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu);

1012

[ 1025](group__thread__apis.md#ga89e6c07ac112da75b2ef115d1a557d44)int [k\_thread\_cpu\_mask\_disable](group__thread__apis.md#ga89e6c07ac112da75b2ef115d1a557d44)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu);

1026

[ 1037](group__thread__apis.md#gae9ebd9845e14ed02944ab9282a185c03)int [k\_thread\_cpu\_pin](group__thread__apis.md#gae9ebd9845e14ed02944ab9282a185c03)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu);

1038#endif

1039

[ 1061](group__thread__apis.md#ga66cf8682fb65870eceb5e57d667a8d4e)\_\_syscall void [k\_thread\_suspend](group__thread__apis.md#ga66cf8682fb65870eceb5e57d667a8d4e)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

1062

[ 1074](group__thread__apis.md#ga117b26f8569ec3045ead1fad1851663d)\_\_syscall void [k\_thread\_resume](group__thread__apis.md#ga117b26f8569ec3045ead1fad1851663d)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

1075

[ 1089](group__thread__apis.md#gac539268e0b45c600315a6567ec27f965)static inline void [k\_thread\_start](group__thread__apis.md#gac539268e0b45c600315a6567ec27f965)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread)

1090{

1091 [k\_wakeup](group__thread__apis.md#ga9275a019c8ff3c7fe49a81f8c078157e)(thread);

1092}

1093

[ 1120](group__thread__apis.md#ga877c1bfeffbf8f097d1656f9e10a66e8)void [k\_sched\_time\_slice\_set](group__thread__apis.md#ga877c1bfeffbf8f097d1656f9e10a66e8)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) slice, int prio);

1121

[ 1160](group__thread__apis.md#ga563928f292a4134acd4142029b60e631)void [k\_thread\_time\_slice\_set](group__thread__apis.md#ga563928f292a4134acd4142029b60e631)(struct [k\_thread](structk__thread.md) \*th, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) slice\_ticks,

1161 [k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f) expired, void \*data);

1162

1164

1169

[ 1181](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)bool [k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)(void);

1182

[ 1199](group__isr__apis.md#ga91e1cf0dc7fc93a3214cadb74ed86666)\_\_syscall int [k\_is\_preempt\_thread](group__isr__apis.md#ga91e1cf0dc7fc93a3214cadb74ed86666)(void);

1200

[ 1212](group__isr__apis.md#gae74e5de996276df767b96d4b50fa47ea)static inline bool [k\_is\_pre\_kernel](group__isr__apis.md#gae74e5de996276df767b96d4b50fa47ea)(void)

1213{

1214 extern bool z\_sys\_post\_kernel; /\* in init.c \*/

1215

1216 return !z\_sys\_post\_kernel;

1217}

1218

1222

1227

[ 1253](group__thread__apis.md#ga4f0c5d0b9f279b12a4ad97db0c116a5f)void [k\_sched\_lock](group__thread__apis.md#ga4f0c5d0b9f279b12a4ad97db0c116a5f)(void);

1254

[ 1262](group__thread__apis.md#ga7b26f64523cc4c36522cc828ccf85580)void [k\_sched\_unlock](group__thread__apis.md#ga7b26f64523cc4c36522cc828ccf85580)(void);

1263

[ 1276](group__thread__apis.md#ga4834d9b81ed60c00eee77b0d4f8ab9e4)\_\_syscall void [k\_thread\_custom\_data\_set](group__thread__apis.md#ga4834d9b81ed60c00eee77b0d4f8ab9e4)(void \*value);

1277

[ 1285](group__thread__apis.md#ga19af063cff7b306ba28062996922740d)\_\_syscall void \*[k\_thread\_custom\_data\_get](group__thread__apis.md#ga19af063cff7b306ba28062996922740d)(void);

1286

[ 1300](group__thread__apis.md#ga23107333f134b9c9a8b692374211e841)\_\_syscall int [k\_thread\_name\_set](group__thread__apis.md#ga23107333f134b9c9a8b692374211e841)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, const char \*str);

1301

[ 1310](group__thread__apis.md#gadebf45da56dee393164569742459dc0a)const char \*[k\_thread\_name\_get](group__thread__apis.md#gadebf45da56dee393164569742459dc0a)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

1311

[ 1323](group__thread__apis.md#ga07b59ade055c69929ccdc08a14361794)\_\_syscall int [k\_thread\_name\_copy](group__thread__apis.md#ga07b59ade055c69929ccdc08a14361794)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, char \*buf,

1324 size\_t size);

1325

[ 1338](group__thread__apis.md#ga0c6af32096dc7ca391ffe2522bae4cb6)const char \*[k\_thread\_state\_str](group__thread__apis.md#ga0c6af32096dc7ca391ffe2522bae4cb6)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread\_id, char \*buf, size\_t buf\_size);

1339

1343

1348

[ 1357](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)#define K\_NO\_WAIT Z\_TIMEOUT\_NO\_WAIT

1358

[ 1371](group__clock__apis.md#gae2f3a80170afc5fbce0337cdf5a4ce4c)#define K\_NSEC(t) Z\_TIMEOUT\_NS(t)

1372

[ 1385](group__clock__apis.md#ga91198e325210ec052a8308e642058c0b)#define K\_USEC(t) Z\_TIMEOUT\_US(t)

1386

[ 1397](group__clock__apis.md#gab41f59fd2b724cb1279e4f6821154b33)#define K\_CYC(t) Z\_TIMEOUT\_CYC(t)

1398

[ 1409](group__clock__apis.md#gaeda983960bd25f1dba7a386ad720e395)#define K\_TICKS(t) Z\_TIMEOUT\_TICKS(t)

1410

[ 1421](group__clock__apis.md#ga302af954e87b10a9b731f1ad07775e9f)#define K\_MSEC(ms) Z\_TIMEOUT\_MS(ms)

1422

[ 1433](group__clock__apis.md#gadc361472aea59267f6ea38f5e7c7ca2a)#define K\_SECONDS(s) K\_MSEC((s) \* MSEC\_PER\_SEC)

1434

[ 1445](group__clock__apis.md#gaef02f20d4d2ebfc9aa29acae01bd3698)#define K\_MINUTES(m) K\_SECONDS((m) \* 60)

1446

[ 1457](group__clock__apis.md#gaa9e0cd890db28965b66d4bc5d719a91f)#define K\_HOURS(h) K\_MINUTES((h) \* 60)

1458

[ 1467](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)#define K\_FOREVER Z\_FOREVER

1468

1469#ifdef CONFIG\_TIMEOUT\_64BIT

1470

1482#define K\_TIMEOUT\_ABS\_TICKS(t) \

1483 Z\_TIMEOUT\_TICKS(Z\_TICK\_ABS((k\_ticks\_t)MAX(t, 0)))

1484

1496#define K\_TIMEOUT\_ABS\_MS(t) K\_TIMEOUT\_ABS\_TICKS(k\_ms\_to\_ticks\_ceil64(t))

1497

1510#define K\_TIMEOUT\_ABS\_US(t) K\_TIMEOUT\_ABS\_TICKS(k\_us\_to\_ticks\_ceil64(t))

1511

1524#define K\_TIMEOUT\_ABS\_NS(t) K\_TIMEOUT\_ABS\_TICKS(k\_ns\_to\_ticks\_ceil64(t))

1525

1538#define K\_TIMEOUT\_ABS\_CYC(t) K\_TIMEOUT\_ABS\_TICKS(k\_cyc\_to\_ticks\_ceil64(t))

1539

1540#endif

1541

1545

1549

1550struct k\_timer {

1551 /\*

1552 \* \_timeout structure must be first here if we want to use

1553 \* dynamic timer allocation. timeout.node is used in the double-linked

1554 \* list of free timers

1555 \*/

1556 struct \_timeout timeout;

1557

1558 /\* wait queue for the (single) thread waiting on this timer \*/

1559 \_wait\_q\_t wait\_q;

1560

1561 /\* runs in ISR context \*/

1562 void (\*expiry\_fn)(struct k\_timer \*timer);

1563

1564 /\* runs in the context of the thread that calls k\_timer\_stop() \*/

1565 void (\*stop\_fn)(struct k\_timer \*timer);

1566

1567 /\* timer period \*/

1568 [k\_timeout\_t](structk__timeout__t.md) period;

1569

1570 /\* timer status \*/

1571 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status;

1572

1573 /\* user-specific data, also used to support legacy features \*/

1574 void \*user\_data;

1575

1576 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_timer)

1577

1578#ifdef CONFIG\_OBJ\_CORE\_TIMER

1579 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

1580#endif

1581};

1582

1583#define Z\_TIMER\_INITIALIZER(obj, expiry, stop) \

1584 { \

1585 .timeout = { \

1586 .node = {},\

1587 .fn = z\_timer\_expiration\_handler, \

1588 .dticks = 0, \

1589 }, \

1590 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

1591 .expiry\_fn = expiry, \

1592 .stop\_fn = stop, \

1593 .status = 0, \

1594 .user\_data = 0, \

1595 }

1596

1600

1606

[ 1617](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde)typedef void (\*[k\_timer\_expiry\_t](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde))(struct k\_timer \*timer);

1618

[ 1633](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c)typedef void (\*[k\_timer\_stop\_t](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c))(struct k\_timer \*timer);

1634

[ 1646](group__timer__apis.md#gaa267fcb0a2e18cd0da29e9f9612510a6)#define K\_TIMER\_DEFINE(name, expiry\_fn, stop\_fn) \

1647 STRUCT\_SECTION\_ITERABLE(k\_timer, name) = \

1648 Z\_TIMER\_INITIALIZER(name, expiry\_fn, stop\_fn)

1649

[ 1659](group__timer__apis.md#ga318c846a740b901e5d56876a47ad7f61)void [k\_timer\_init](group__timer__apis.md#ga318c846a740b901e5d56876a47ad7f61)(struct k\_timer \*timer,

1660 [k\_timer\_expiry\_t](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde) expiry\_fn,

1661 [k\_timer\_stop\_t](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c) stop\_fn);

1662

[ 1677](group__timer__apis.md#ga3ba70e9f059ff52fd2057ab89ea7f2ee)\_\_syscall void [k\_timer\_start](group__timer__apis.md#ga3ba70e9f059ff52fd2057ab89ea7f2ee)(struct k\_timer \*timer,

1678 [k\_timeout\_t](structk__timeout__t.md) duration, [k\_timeout\_t](structk__timeout__t.md) period);

1679

[ 1696](group__timer__apis.md#ga8d3e3356a10d36570e16f7920e4c8772)\_\_syscall void [k\_timer\_stop](group__timer__apis.md#ga8d3e3356a10d36570e16f7920e4c8772)(struct k\_timer \*timer);

1697

[ 1710](group__timer__apis.md#gad532f4834cd4cf8be27b089e6ea347ce)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_timer\_status\_get](group__timer__apis.md#gad532f4834cd4cf8be27b089e6ea347ce)(struct k\_timer \*timer);

1711

[ 1729](group__timer__apis.md#ga81d6d95b7021e26ad4cab161318e04f2)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_timer\_status\_sync](group__timer__apis.md#ga81d6d95b7021e26ad4cab161318e04f2)(struct k\_timer \*timer);

1730

1731#ifdef CONFIG\_SYS\_CLOCK\_EXISTS

1732

[ 1743](group__timer__apis.md#ga022b4cf5c8d0ee21b6a3b04fd425533f)\_\_syscall [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_timer\_expires\_ticks](group__timer__apis.md#ga022b4cf5c8d0ee21b6a3b04fd425533f)(const struct k\_timer \*timer);

1744

1745static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_impl\_k\_timer\_expires\_ticks(

1746 const struct k\_timer \*timer)

1747{

1748 return z\_timeout\_expires(&timer->timeout);

1749}

1750

[ 1761](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4)\_\_syscall [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_timer\_remaining\_ticks](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4)(const struct k\_timer \*timer);

1762

1763static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_impl\_k\_timer\_remaining\_ticks(

1764 const struct k\_timer \*timer)

1765{

1766 return z\_timeout\_remaining(&timer->timeout);

1767}

1768

[ 1779](group__timer__apis.md#ga6c6d8b0aa59bfa0f5924e95ccf756259)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_timer\_remaining\_get](group__timer__apis.md#ga6c6d8b0aa59bfa0f5924e95ccf756259)(struct k\_timer \*timer)

1780{

1781 return [k\_ticks\_to\_ms\_floor32](group__timeutil__unit__apis.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)([k\_timer\_remaining\_ticks](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4)(timer));

1782}

1783

1784#endif /\* CONFIG\_SYS\_CLOCK\_EXISTS \*/

1785

[ 1798](group__timer__apis.md#gadba1884961e790dd9c5d567de91cc7e2)\_\_syscall void [k\_timer\_user\_data\_set](group__timer__apis.md#gadba1884961e790dd9c5d567de91cc7e2)(struct k\_timer \*timer, void \*user\_data);

1799

1803static inline void z\_impl\_k\_timer\_user\_data\_set(struct k\_timer \*timer,

1804 void \*user\_data)

1805{

1806 timer->user\_data = user\_data;

1807}

1808

[ 1816](group__timer__apis.md#ga19a7d99a01a83828efd7f0d3bf2dd358)\_\_syscall void \*[k\_timer\_user\_data\_get](group__timer__apis.md#ga19a7d99a01a83828efd7f0d3bf2dd358)(const struct k\_timer \*timer);

1817

1818static inline void \*z\_impl\_k\_timer\_user\_data\_get(const struct k\_timer \*timer)

1819{

1820 return timer->user\_data;

1821}

1822

1824

1830

[ 1840](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)\_\_syscall [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)(void);

1841

[ 1855](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)(void)

1856{

1857 return [k\_ticks\_to\_ms\_floor64](group__timeutil__unit__apis.md#gac417ab53d5d493d95e24e7f777f8a4e0)([k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)());

1858}

1859

[ 1879](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_uptime\_get\_32](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b)(void)

1880{

1881 return ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)();

1882}

1883

[ 1892](group__clock__apis.md#gae082928ea608a8b180b4cb3a79d21a24)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_uptime\_seconds](group__clock__apis.md#gae082928ea608a8b180b4cb3a79d21a24)(void)

1893{

1894 return [k\_ticks\_to\_sec\_floor32](group__timeutil__unit__apis.md#ga824ffc9857fa2d4bccb3a9f4a56b8f18)([k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)());

1895}

1896

[ 1908](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [k\_uptime\_delta](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80)([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*reftime)

1909{

1910 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) uptime, delta;

1911

1912 uptime = [k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)();

1913 delta = uptime - \*reftime;

1914 \*reftime = uptime;

1915

1916 return delta;

1917}

1918

[ 1927](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)(void)

1928{

1929 return [arch\_k\_cycle\_get\_32](arc_2v2_2misc_8h.md#a9ee9f897ec750957de45bf8d43349d5e)();

1930}

1931

[ 1942](group__clock__apis.md#gae09f509d02bf75a7b45d2800d823bb3a)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [k\_cycle\_get\_64](group__clock__apis.md#gae09f509d02bf75a7b45d2800d823bb3a)(void)

1943{

1944 if (![IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_TIMER\_HAS\_64BIT\_CYCLE\_COUNTER)) {

1945 \_\_ASSERT(0, "64-bit cycle counter not enabled on this platform. "

1946 "See CONFIG\_TIMER\_HAS\_64BIT\_CYCLE\_COUNTER");

1947 return 0;

1948 }

1949

1950 return [arch\_k\_cycle\_get\_64](arc_2v2_2misc_8h.md#acc1ed8d949f694a1d39e389334caf971)();

1951}

1952

1956

[ 1957](structk__queue.md)struct [k\_queue](structk__queue.md) {

[ 1958](structk__queue.md#a892371af9701ce67619e38446bc2ceae) [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) [data\_q](structk__queue.md#a892371af9701ce67619e38446bc2ceae);

[ 1959](structk__queue.md#a18fd165fec722384b3748bfdf3332a4c) struct [k\_spinlock](structk__spinlock.md) [lock](structk__queue.md#a18fd165fec722384b3748bfdf3332a4c);

[ 1960](structk__queue.md#a871d734f2b21a9cad3ca4a2ba79e64f1) \_wait\_q\_t [wait\_q](structk__queue.md#a871d734f2b21a9cad3ca4a2ba79e64f1);

1961

1962 Z\_DECL\_POLL\_EVENT

1963

1964 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_queue](structk__queue.md))

1965};

1966

1970

1971#define Z\_QUEUE\_INITIALIZER(obj) \

1972 { \

1973 .data\_q = SYS\_SFLIST\_STATIC\_INIT(&obj.data\_q), \

1974 .lock = { }, \

1975 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

1976 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

1977 }

1978

1982

1988

[ 1996](group__queue__apis.md#ga0236222d42768c2bf00942f328146c21)\_\_syscall void [k\_queue\_init](group__queue__apis.md#ga0236222d42768c2bf00942f328146c21)(struct [k\_queue](structk__queue.md) \*queue);

1997

[ 2011](group__queue__apis.md#ga7c39d86cc6509f59ff9223cac3ea5071)\_\_syscall void [k\_queue\_cancel\_wait](group__queue__apis.md#ga7c39d86cc6509f59ff9223cac3ea5071)(struct [k\_queue](structk__queue.md) \*queue);

2012

[ 2025](group__queue__apis.md#gaa84522a5ace6e7f8ba61033baca6972f)void [k\_queue\_append](group__queue__apis.md#gaa84522a5ace6e7f8ba61033baca6972f)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2026

[ 2043](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_queue\_alloc\_append](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2044

[ 2057](group__queue__apis.md#ga8ce013d8a037d4be5078797e0050e9c6)void [k\_queue\_prepend](group__queue__apis.md#ga8ce013d8a037d4be5078797e0050e9c6)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2058

[ 2075](group__queue__apis.md#gacf3dba40125073c11075e5a134919f88)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_queue\_alloc\_prepend](group__queue__apis.md#gacf3dba40125073c11075e5a134919f88)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2076

[ 2090](group__queue__apis.md#gad47336f27e433a52600a3b67ab89556a)void [k\_queue\_insert](group__queue__apis.md#gad47336f27e433a52600a3b67ab89556a)(struct [k\_queue](structk__queue.md) \*queue, void \*prev, void \*data);

2091

[ 2110](group__queue__apis.md#ga91d1a144fc2aeb3dd655accc94ca43aa)int [k\_queue\_append\_list](group__queue__apis.md#ga91d1a144fc2aeb3dd655accc94ca43aa)(struct [k\_queue](structk__queue.md) \*queue, void \*head, void \*tail);

2111

[ 2127](group__queue__apis.md#ga4eee0da7442d60572b05d60a9996e69d)int [k\_queue\_merge\_slist](group__queue__apis.md#ga4eee0da7442d60572b05d60a9996e69d)(struct [k\_queue](structk__queue.md) \*queue, [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list);

2128

[ 2146](group__queue__apis.md#ga0a77d8556e7d253319275de034f01619)\_\_syscall void \*[k\_queue\_get](group__queue__apis.md#ga0a77d8556e7d253319275de034f01619)(struct [k\_queue](structk__queue.md) \*queue, [k\_timeout\_t](structk__timeout__t.md) timeout);

2147

[ 2164](group__queue__apis.md#ga4bff929ed1d366a06e00865a5bbe2544)bool [k\_queue\_remove](group__queue__apis.md#ga4bff929ed1d366a06e00865a5bbe2544)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2165

[ 2180](group__queue__apis.md#ga287a2d81e2e3041be1cd45164e72f127)bool [k\_queue\_unique\_append](group__queue__apis.md#ga287a2d81e2e3041be1cd45164e72f127)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2181

[ 2195](group__queue__apis.md#gadb2bb8088868b3c5801c72b320389ca9)\_\_syscall int [k\_queue\_is\_empty](group__queue__apis.md#gadb2bb8088868b3c5801c72b320389ca9)(struct [k\_queue](structk__queue.md) \*queue);

2196

2197static inline int z\_impl\_k\_queue\_is\_empty(struct [k\_queue](structk__queue.md) \*queue)

2198{

2199 return [sys\_sflist\_is\_empty](group__flagged-single-linked-list__apis.md#gac506235a9df89a7a52631e9990ceaad5)(&queue->[data\_q](structk__queue.md#a892371af9701ce67619e38446bc2ceae)) ? 1 : 0;

2200}

2201

[ 2211](group__queue__apis.md#ga8ccd5137690c127a0f7d67619b88a52b)\_\_syscall void \*[k\_queue\_peek\_head](group__queue__apis.md#ga8ccd5137690c127a0f7d67619b88a52b)(struct [k\_queue](structk__queue.md) \*queue);

2212

[ 2222](group__queue__apis.md#ga27a460c42836d8b093ad9274c14bb176)\_\_syscall void \*[k\_queue\_peek\_tail](group__queue__apis.md#ga27a460c42836d8b093ad9274c14bb176)(struct [k\_queue](structk__queue.md) \*queue);

2223

[ 2233](group__queue__apis.md#gacd0bc309f0147d4669f65fafa87e0e70)#define K\_QUEUE\_DEFINE(name) \

2234 STRUCT\_SECTION\_ITERABLE(k\_queue, name) = \

2235 Z\_QUEUE\_INITIALIZER(name)

2236

2238

2239#ifdef CONFIG\_USERSPACE

[ 2249](structk__futex.md)struct [k\_futex](structk__futex.md) {

[ 2250](structk__futex.md#a454ad1b595b899306c8e9c8e1431e7a7) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [val](structk__futex.md#a454ad1b595b899306c8e9c8e1431e7a7);

2251};

2252

2260struct z\_futex\_data {

2261 \_wait\_q\_t wait\_q;

2262 struct [k\_spinlock](structk__spinlock.md) lock;

2263};

2264

2265#define Z\_FUTEX\_DATA\_INITIALIZER(obj) \

2266 { \

2267 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q) \

2268 }

2269

2275

[ 2295](group__futex__apis.md#ga596bfa265f88567ad9e80fd38cd433d3)\_\_syscall int [k\_futex\_wait](group__futex__apis.md#ga596bfa265f88567ad9e80fd38cd433d3)(struct [k\_futex](structk__futex.md) \*futex, int expected,

2296 [k\_timeout\_t](structk__timeout__t.md) timeout);

2297

[ 2312](group__futex__apis.md#ga62de1aeb7c5c273aed20d0e05336d7a0)\_\_syscall int [k\_futex\_wake](group__futex__apis.md#ga62de1aeb7c5c273aed20d0e05336d7a0)(struct [k\_futex](structk__futex.md) \*futex, bool wake\_all);

2313

2315#endif

2316

2322

2327

[ 2328](structk__event.md)struct [k\_event](structk__event.md) {

[ 2329](structk__event.md#a5bacd5f2d34da646d9d7ee229842e432) \_wait\_q\_t [wait\_q](structk__event.md#a5bacd5f2d34da646d9d7ee229842e432);

[ 2330](structk__event.md#a54c6f5997132e88406ffa5bcc0a10b83) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [events](structk__event.md#a54c6f5997132e88406ffa5bcc0a10b83);

[ 2331](structk__event.md#a1f0de9c69f29ad854f3b0d510ceb1efc) struct [k\_spinlock](structk__spinlock.md) [lock](structk__event.md#a1f0de9c69f29ad854f3b0d510ceb1efc);

2332

2333 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_event](structk__event.md))

2334

2335#ifdef CONFIG\_OBJ\_CORE\_EVENT

2336 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2337#endif

2338

2339};

2340

2341#define Z\_EVENT\_INITIALIZER(obj) \

2342 { \

2343 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

2344 .events = 0 \

2345 }

2346

[ 2354](group__event__apis.md#gacf803590b39b095056f2b1c5090c4019)\_\_syscall void [k\_event\_init](group__event__apis.md#gacf803590b39b095056f2b1c5090c4019)(struct [k\_event](structk__event.md) \*event);

2355

[ 2371](group__event__apis.md#gac88d17410a71642a903890e420d23d76)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_post](group__event__apis.md#gac88d17410a71642a903890e420d23d76)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events);

2372

[ 2388](group__event__apis.md#gac22e9d768d003246e68b4b0b64e60f49)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_set](group__event__apis.md#gac22e9d768d003246e68b4b0b64e60f49)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events);

2389

[ 2404](group__event__apis.md#ga29b3ec1022b12a8c34884da3559c5864)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_set\_masked](group__event__apis.md#ga29b3ec1022b12a8c34884da3559c5864)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events,

2405 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events\_mask);

2406

[ 2417](group__event__apis.md#gad6bfd7bfd0587bc70d3aa0b988010376)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_clear](group__event__apis.md#gad6bfd7bfd0587bc70d3aa0b988010376)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events);

2418

[ 2440](group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_wait](group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events,

2441 bool reset, [k\_timeout\_t](structk__timeout__t.md) timeout);

2442

[ 2464](group__event__apis.md#gaddd60a99de5ac3d84f643c9433b744c1)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_wait\_all](group__event__apis.md#gaddd60a99de5ac3d84f643c9433b744c1)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events,

2465 bool reset, [k\_timeout\_t](structk__timeout__t.md) timeout);

2466

[ 2475](group__event__apis.md#ga81e66be0959e8cb0414d9772056a6264)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_test](group__event__apis.md#ga81e66be0959e8cb0414d9772056a6264)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events\_mask)

2476{

2477 return [k\_event\_wait](group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753)(event, events\_mask, false, [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f));

2478}

2479

[ 2489](group__event__apis.md#ga093449cc6686d3235944f3faad284893)#define K\_EVENT\_DEFINE(name) \

2490 STRUCT\_SECTION\_ITERABLE(k\_event, name) = \

2491 Z\_EVENT\_INITIALIZER(name);

2492

2494

[ 2495](structk__fifo.md)struct [k\_fifo](structk__fifo.md) {

2496 struct [k\_queue](structk__queue.md) \_queue;

2497#ifdef CONFIG\_OBJ\_CORE\_FIFO

2498 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2499#endif

2500};

2501

2505#define Z\_FIFO\_INITIALIZER(obj) \

2506 { \

2507 .\_queue = Z\_QUEUE\_INITIALIZER(obj.\_queue) \

2508 }

2509

2513

2519

[ 2527](group__fifo__apis.md#gaeebf6ef54d4be61e19408f44a734a159)#define k\_fifo\_init(fifo) \

2528 ({ \

2529 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, init, fifo); \

2530 k\_queue\_init(&(fifo)->\_queue); \

2531 K\_OBJ\_CORE\_INIT(K\_OBJ\_CORE(fifo), \_obj\_type\_fifo); \

2532 K\_OBJ\_CORE\_LINK(K\_OBJ\_CORE(fifo)); \

2533 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, init, fifo); \

2534 })

2535

[ 2547](group__fifo__apis.md#gab744080af449e093df8dd4982e013e16)#define k\_fifo\_cancel\_wait(fifo) \

2548 ({ \

2549 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, cancel\_wait, fifo); \

2550 k\_queue\_cancel\_wait(&(fifo)->\_queue); \

2551 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, cancel\_wait, fifo); \

2552 })

2553

[ 2566](group__fifo__apis.md#ga3addb10f86f19e245c23362433d5c913)#define k\_fifo\_put(fifo, data) \

2567 ({ \

2568 void \*\_data = data; \

2569 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, put, fifo, \_data); \

2570 k\_queue\_append(&(fifo)->\_queue, \_data); \

2571 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, put, fifo, \_data); \

2572 })

2573

[ 2590](group__fifo__apis.md#gab1c5212040d12cbb92cede5cf54928ba)#define k\_fifo\_alloc\_put(fifo, data) \

2591 ({ \

2592 void \*\_data = data; \

2593 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, alloc\_put, fifo, \_data); \

2594 int fap\_ret = k\_queue\_alloc\_append(&(fifo)->\_queue, \_data); \

2595 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, alloc\_put, fifo, \_data, fap\_ret); \

2596 fap\_ret; \

2597 })

2598

[ 2613](group__fifo__apis.md#ga1bf5f52290c83e54ba14358cbbb4051b)#define k\_fifo\_put\_list(fifo, head, tail) \

2614 ({ \

2615 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, put\_list, fifo, head, tail); \

2616 k\_queue\_append\_list(&(fifo)->\_queue, head, tail); \

2617 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, put\_list, fifo, head, tail); \

2618 })

2619

[ 2633](group__fifo__apis.md#ga4cdc286a7a6f0d43acab63a4846815e7)#define k\_fifo\_put\_slist(fifo, list) \

2634 ({ \

2635 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, put\_slist, fifo, list); \

2636 k\_queue\_merge\_slist(&(fifo)->\_queue, list); \

2637 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, put\_slist, fifo, list); \

2638 })

2639

[ 2657](group__fifo__apis.md#ga1e2c480e2124116af97e94e7b4435de6)#define k\_fifo\_get(fifo, timeout) \

2658 ({ \

2659 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, get, fifo, timeout); \

2660 void \*fg\_ret = k\_queue\_get(&(fifo)->\_queue, timeout); \

2661 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, get, fifo, timeout, fg\_ret); \

2662 fg\_ret; \

2663 })

2664

[ 2678](group__fifo__apis.md#gab7cec4adc128ed1fd2d194ba6cd8c640)#define k\_fifo\_is\_empty(fifo) \

2679 k\_queue\_is\_empty(&(fifo)->\_queue)

2680

[ 2694](group__fifo__apis.md#ga2e0c8608f095a929740fa94c94a4f389)#define k\_fifo\_peek\_head(fifo) \

2695 ({ \

2696 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, peek\_head, fifo); \

2697 void \*fph\_ret = k\_queue\_peek\_head(&(fifo)->\_queue); \

2698 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, peek\_head, fifo, fph\_ret); \

2699 fph\_ret; \

2700 })

2701

[ 2713](group__fifo__apis.md#gafbe2ce9a6437b886cf149016187ba92f)#define k\_fifo\_peek\_tail(fifo) \

2714 ({ \

2715 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, peek\_tail, fifo); \

2716 void \*fpt\_ret = k\_queue\_peek\_tail(&(fifo)->\_queue); \

2717 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, peek\_tail, fifo, fpt\_ret); \

2718 fpt\_ret; \

2719 })

2720

[ 2730](group__fifo__apis.md#ga230b02a526ecb0ae1598be75cb9a8274)#define K\_FIFO\_DEFINE(name) \

2731 STRUCT\_SECTION\_ITERABLE(k\_fifo, name) = \

2732 Z\_FIFO\_INITIALIZER(name)

2733

2735

[ 2736](structk__lifo.md)struct [k\_lifo](structk__lifo.md) {

2737 struct [k\_queue](structk__queue.md) \_queue;

2738#ifdef CONFIG\_OBJ\_CORE\_LIFO

2739 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2740#endif

2741};

2742

2746

2747#define Z\_LIFO\_INITIALIZER(obj) \

2748 { \

2749 .\_queue = Z\_QUEUE\_INITIALIZER(obj.\_queue) \

2750 }

2751

2755

2761

[ 2769](group__lifo__apis.md#ga69fb19716a9014f7de79f8e524d64a3e)#define k\_lifo\_init(lifo) \

2770 ({ \

2771 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_lifo, init, lifo); \

2772 k\_queue\_init(&(lifo)->\_queue); \

2773 K\_OBJ\_CORE\_INIT(K\_OBJ\_CORE(lifo), \_obj\_type\_lifo); \

2774 K\_OBJ\_CORE\_LINK(K\_OBJ\_CORE(lifo)); \

2775 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_lifo, init, lifo); \

2776 })

2777

[ 2790](group__lifo__apis.md#gad662e36b1df8b9013e2dc61f9dfe3a8b)#define k\_lifo\_put(lifo, data) \

2791 ({ \

2792 void \*\_data = data; \

2793 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_lifo, put, lifo, \_data); \

2794 k\_queue\_prepend(&(lifo)->\_queue, \_data); \

2795 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_lifo, put, lifo, \_data); \

2796 })

2797

[ 2814](group__lifo__apis.md#ga96d885a6a36fcfcb5eaa65898eee0965)#define k\_lifo\_alloc\_put(lifo, data) \

2815 ({ \

2816 void \*\_data = data; \

2817 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_lifo, alloc\_put, lifo, \_data); \

2818 int lap\_ret = k\_queue\_alloc\_prepend(&(lifo)->\_queue, \_data); \

2819 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_lifo, alloc\_put, lifo, \_data, lap\_ret); \

2820 lap\_ret; \

2821 })

2822

[ 2840](group__lifo__apis.md#gad5f1775947b07a2a77f667aa9e41db5a)#define k\_lifo\_get(lifo, timeout) \

2841 ({ \

2842 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_lifo, get, lifo, timeout); \

2843 void \*lg\_ret = k\_queue\_get(&(lifo)->\_queue, timeout); \

2844 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_lifo, get, lifo, timeout, lg\_ret); \

2845 lg\_ret; \

2846 })

2847

[ 2857](group__lifo__apis.md#gaebd450d4181f22491623ea0aed6ee576)#define K\_LIFO\_DEFINE(name) \

2858 STRUCT\_SECTION\_ITERABLE(k\_lifo, name) = \

2859 Z\_LIFO\_INITIALIZER(name)

2860

2862

2866#define K\_STACK\_FLAG\_ALLOC ((uint8\_t)1) /\* Buffer was allocated \*/

2867

2868typedef [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) stack\_data\_t;

2869

2870struct k\_stack {

2871 \_wait\_q\_t wait\_q;

2872 struct [k\_spinlock](structk__spinlock.md) lock;

2873 stack\_data\_t \*base, \*next, \*top;

2874

2875 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

2876

2877 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_stack)

2878

2879#ifdef CONFIG\_OBJ\_CORE\_STACK

2880 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2881#endif

2882};

2883

2884#define Z\_STACK\_INITIALIZER(obj, stack\_buffer, stack\_num\_entries) \

2885 { \

2886 .wait\_q = Z\_WAIT\_Q\_INIT(&(obj).wait\_q), \

2887 .base = (stack\_buffer), \

2888 .next = (stack\_buffer), \

2889 .top = (stack\_buffer) + (stack\_num\_entries), \

2890 }

2891

2895

2901

[ 2911](group__stack__apis.md#ga4400a39ef48289305cf66a092d5c6c7d)void [k\_stack\_init](group__stack__apis.md#ga4400a39ef48289305cf66a092d5c6c7d)(struct k\_stack \*stack,

2912 stack\_data\_t \*buffer, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_entries);

2913

2914

2928

[ 2929](group__stack__apis.md#gab97d924db1aef3f6adade156a107d45c)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_stack\_alloc\_init](group__stack__apis.md#gab97d924db1aef3f6adade156a107d45c)(struct k\_stack \*stack,

2930 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_entries);

2931

[ 2943](group__stack__apis.md#ga819f4e7b2cf11cf2e1b80933fdcb67ea)int [k\_stack\_cleanup](group__stack__apis.md#ga819f4e7b2cf11cf2e1b80933fdcb67ea)(struct k\_stack \*stack);

2944

[ 2958](group__stack__apis.md#gaa6180f4db6ec93ee84149cba054d3e53)\_\_syscall int [k\_stack\_push](group__stack__apis.md#gaa6180f4db6ec93ee84149cba054d3e53)(struct k\_stack \*stack, stack\_data\_t data);

2959

[ 2980](group__stack__apis.md#ga36ce6ceb9ea3d5c36d22b10430789480)\_\_syscall int [k\_stack\_pop](group__stack__apis.md#ga36ce6ceb9ea3d5c36d22b10430789480)(struct k\_stack \*stack, stack\_data\_t \*data,

2981 [k\_timeout\_t](structk__timeout__t.md) timeout);

2982

[ 2993](group__stack__apis.md#ga8c9ca77e5de3c9757dcd4ecb55797835)#define K\_STACK\_DEFINE(name, stack\_num\_entries) \

2994 stack\_data\_t \_\_noinit \

2995 \_k\_stack\_buf\_##name[stack\_num\_entries]; \

2996 STRUCT\_SECTION\_ITERABLE(k\_stack, name) = \

2997 Z\_STACK\_INITIALIZER(name, \_k\_stack\_buf\_##name, \

2998 stack\_num\_entries)

2999

3001

3005

3006struct [k\_work](structk__work.md);

3007struct [k\_work\_q](structk__work__q.md);

3008struct [k\_work\_queue\_config](structk__work__queue__config.md);

3009extern struct [k\_work\_q](structk__work__q.md) k\_sys\_work\_q;

3010

3014

3020

[ 3025](structk__mutex.md)struct [k\_mutex](structk__mutex.md) {

[ 3027](structk__mutex.md#a4add234295bceff22551ee74f3aed802) \_wait\_q\_t [wait\_q](structk__mutex.md#a4add234295bceff22551ee74f3aed802);

[ 3029](structk__mutex.md#af910bb07dc99e50078de26fccca468e4) struct [k\_thread](structk__thread.md) \*[owner](structk__mutex.md#af910bb07dc99e50078de26fccca468e4);

3030

[ 3032](structk__mutex.md#a0db401fc8e03e1f984b8fd15af974718) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lock\_count](structk__mutex.md#a0db401fc8e03e1f984b8fd15af974718);

3033

[ 3035](structk__mutex.md#ab0d16fac9f8af960a501ffd93ec08c80) int [owner\_orig\_prio](structk__mutex.md#ab0d16fac9f8af960a501ffd93ec08c80);

3036

3037 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_mutex](structk__mutex.md))

3038

3039#ifdef CONFIG\_OBJ\_CORE\_MUTEX

3040 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

3041#endif

3042};

3043

3047#define Z\_MUTEX\_INITIALIZER(obj) \

3048 { \

3049 .wait\_q = Z\_WAIT\_Q\_INIT(&(obj).wait\_q), \

3050 .owner = NULL, \

3051 .lock\_count = 0, \

3052 .owner\_orig\_prio = K\_LOWEST\_APPLICATION\_THREAD\_PRIO, \

3053 }

3054

3058

[ 3068](group__mutex__apis.md#gab6f3d98fabbdc0918bbc9934d61d63f3)#define K\_MUTEX\_DEFINE(name) \

3069 STRUCT\_SECTION\_ITERABLE(k\_mutex, name) = \

3070 Z\_MUTEX\_INITIALIZER(name)

3071

[ 3084](group__mutex__apis.md#ga56b64952fb8b78b00268a21c28b41480)\_\_syscall int [k\_mutex\_init](group__mutex__apis.md#ga56b64952fb8b78b00268a21c28b41480)(struct [k\_mutex](structk__mutex.md) \*mutex);

3085

3086

[ 3108](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)\_\_syscall int [k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(struct [k\_mutex](structk__mutex.md) \*mutex, [k\_timeout\_t](structk__timeout__t.md) timeout);

3109

[ 3130](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)\_\_syscall int [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(struct [k\_mutex](structk__mutex.md) \*mutex);

3131

3135

3136

[ 3137](structk__condvar.md)struct [k\_condvar](structk__condvar.md) {

[ 3138](structk__condvar.md#a14b457a06420f093e779d569f4fea906) \_wait\_q\_t [wait\_q](structk__condvar.md#a14b457a06420f093e779d569f4fea906);

3139

3140#ifdef CONFIG\_OBJ\_CORE\_CONDVAR

3141 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

3142#endif

3143};

3144

3145#define Z\_CONDVAR\_INITIALIZER(obj) \

3146 { \

3147 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

3148 }

3149

3155

[ 3162](group__condvar__apis.md#gac9b497c56cc4642965afa6c0c6d7ecfc)\_\_syscall int [k\_condvar\_init](group__condvar__apis.md#gac9b497c56cc4642965afa6c0c6d7ecfc)(struct [k\_condvar](structk__condvar.md) \*condvar);

3163

[ 3170](group__condvar__apis.md#ga0376a8f7dc6e4f1e1eed55940f43015b)\_\_syscall int [k\_condvar\_signal](group__condvar__apis.md#ga0376a8f7dc6e4f1e1eed55940f43015b)(struct [k\_condvar](structk__condvar.md) \*condvar);

3171

[ 3179](group__condvar__apis.md#gad2e46a7b9e1bc934fd1f5cb38dde40d8)\_\_syscall int [k\_condvar\_broadcast](group__condvar__apis.md#gad2e46a7b9e1bc934fd1f5cb38dde40d8)(struct [k\_condvar](structk__condvar.md) \*condvar);

3180

[ 3198](group__condvar__apis.md#gab2e1d05db4f954755f430ca894e44dbc)\_\_syscall int [k\_condvar\_wait](group__condvar__apis.md#gab2e1d05db4f954755f430ca894e44dbc)(struct [k\_condvar](structk__condvar.md) \*condvar, struct [k\_mutex](structk__mutex.md) \*mutex,

3199 [k\_timeout\_t](structk__timeout__t.md) timeout);

3200

[ 3211](group__condvar__apis.md#ga770816651e25f7e7dae992a0b2260c21)#define K\_CONDVAR\_DEFINE(name) \

3212 STRUCT\_SECTION\_ITERABLE(k\_condvar, name) = \

3213 Z\_CONDVAR\_INITIALIZER(name)

3214

3217

3221

3222struct k\_sem {

3223 \_wait\_q\_t wait\_q;

3224 unsigned int count;

3225 unsigned int limit;

3226

3227 Z\_DECL\_POLL\_EVENT

3228

3229 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_sem)

3230

3231#ifdef CONFIG\_OBJ\_CORE\_SEM

3232 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

3233#endif

3234};

3235

3236#define Z\_SEM\_INITIALIZER(obj, initial\_count, count\_limit) \

3237 { \

3238 .wait\_q = Z\_WAIT\_Q\_INIT(&(obj).wait\_q), \

3239 .count = (initial\_count), \

3240 .limit = (count\_limit), \

3241 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

3242 }

3243

3247

3253

[ 3262](group__semaphore__apis.md#ga689359a77a0cebe737ef644c188f7e57)#define K\_SEM\_MAX\_LIMIT UINT\_MAX

3263

[ 3279](group__semaphore__apis.md#gadcd0e6cfba3392fb887222eafe4c1845)\_\_syscall int [k\_sem\_init](group__semaphore__apis.md#gadcd0e6cfba3392fb887222eafe4c1845)(struct k\_sem \*sem, unsigned int initial\_count,

3280 unsigned int limit);

3281

[ 3300](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)\_\_syscall int [k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)(struct k\_sem \*sem, [k\_timeout\_t](structk__timeout__t.md) timeout);

3301

[ 3312](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)\_\_syscall void [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)(struct k\_sem \*sem);

3313

[ 3323](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)\_\_syscall void [k\_sem\_reset](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)(struct k\_sem \*sem);

3324

[ 3334](group__semaphore__apis.md#ga58843b581e170a1811fc38eecbfd01f3)\_\_syscall unsigned int [k\_sem\_count\_get](group__semaphore__apis.md#ga58843b581e170a1811fc38eecbfd01f3)(struct k\_sem \*sem);

3335

3339static inline unsigned int z\_impl\_k\_sem\_count\_get(struct k\_sem \*sem)

3340{

3341 return sem->count;

3342}

3343

[ 3355](group__semaphore__apis.md#ga018a8aa43e02e704deee7b6341502946)#define K\_SEM\_DEFINE(name, initial\_count, count\_limit) \

3356 STRUCT\_SECTION\_ITERABLE(k\_sem, name) = \

3357 Z\_SEM\_INITIALIZER(name, initial\_count, count\_limit); \

3358 BUILD\_ASSERT(((count\_limit) != 0) && \

3359 (((initial\_count) < (count\_limit)) || ((initial\_count) == (count\_limit))) && \

3360 ((count\_limit) <= K\_SEM\_MAX\_LIMIT));

3361

3363

3367

3368struct [k\_work\_delayable](structk__work__delayable.md);

3369struct [k\_work\_sync](structk__work__sync.md);

3370

3374

3380

[ 3387](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda)typedef void (\*[k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda))(struct [k\_work](structk__work.md) \*work);

3388

[ 3402](group__workqueue__apis.md#gaf20080884a2893d39cd8e862b34a2a30)void [k\_work\_init](group__workqueue__apis.md#gaf20080884a2893d39cd8e862b34a2a30)(struct [k\_work](structk__work.md) \*work,

3403 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) [handler](structk__work.md#a096d6ca1338fb0fbfa330b790136f172));

3404

[ 3419](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b)int [k\_work\_busy\_get](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b)(const struct [k\_work](structk__work.md) \*work);

3420

3434static inline bool [k\_work\_is\_pending](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)(const struct [k\_work](structk__work.md) \*work);

3435

[ 3456](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c)int [k\_work\_submit\_to\_queue](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137),

3457 struct [k\_work](structk__work.md) \*work);

3458

[ 3467](group__workqueue__apis.md#gace61b59575093d7442f39ccb7be686d7)int [k\_work\_submit](group__workqueue__apis.md#gace61b59575093d7442f39ccb7be686d7)(struct [k\_work](structk__work.md) \*work);

3468

[ 3493](group__workqueue__apis.md#gabd1cda459bab538fb2d6dfd84a73b253)bool [k\_work\_flush](group__workqueue__apis.md#gabd1cda459bab538fb2d6dfd84a73b253)(struct [k\_work](structk__work.md) \*work,

3494 struct [k\_work\_sync](structk__work__sync.md) \*sync);

3495

[ 3515](group__workqueue__apis.md#ga389fe2a8fb20f9bd593cf8d990727078)int [k\_work\_cancel](group__workqueue__apis.md#ga389fe2a8fb20f9bd593cf8d990727078)(struct [k\_work](structk__work.md) \*work);

3516

[ 3547](group__workqueue__apis.md#gab2b05cfe3af08f7d32c3946fa1c808f9)bool [k\_work\_cancel\_sync](group__workqueue__apis.md#gab2b05cfe3af08f7d32c3946fa1c808f9)(struct [k\_work](structk__work.md) \*work, struct [k\_work\_sync](structk__work__sync.md) \*sync);

3548

[ 3558](group__workqueue__apis.md#gada77d818ea9e4d07c14a960872ed5492)void [k\_work\_queue\_init](group__workqueue__apis.md#gada77d818ea9e4d07c14a960872ed5492)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137));

3559

[ 3579](group__workqueue__apis.md#gadfc56554f9bfe7b52309d79660188593)void [k\_work\_queue\_start](group__workqueue__apis.md#gadfc56554f9bfe7b52309d79660188593)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137),

3580 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, size\_t stack\_size,

3581 int prio, const struct [k\_work\_queue\_config](structk__work__queue__config.md) \*cfg);

3582

3592static inline [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_work\_queue\_thread\_get](group__workqueue__apis.md#ga0b8b496f7e7bd82d08590a07293e38d7)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137));

3593

[ 3617](group__workqueue__apis.md#ga0fefe3e0225ac99b47b250849f6cd863)int [k\_work\_queue\_drain](group__workqueue__apis.md#ga0fefe3e0225ac99b47b250849f6cd863)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137), bool plug);

3618

[ 3632](group__workqueue__apis.md#gaa0463bb79af3ec470f7d3be02052139f)int [k\_work\_queue\_unplug](group__workqueue__apis.md#gaa0463bb79af3ec470f7d3be02052139f)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137));

3633

[ 3648](group__workqueue__apis.md#ga1fd2fce94eb731ccb0838ec763e62f5c)int [k\_work\_queue\_stop](group__workqueue__apis.md#ga1fd2fce94eb731ccb0838ec763e62f5c)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137), [k\_timeout\_t](structk__timeout__t.md) timeout);

3649

[ 3663](group__workqueue__apis.md#ga2876c5d82fb2340a093bc4d689a55465)void [k\_work\_init\_delayable](group__workqueue__apis.md#ga2876c5d82fb2340a093bc4d689a55465)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3664 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) [handler](structk__work.md#a096d6ca1338fb0fbfa330b790136f172));

3665

3677static inline struct [k\_work\_delayable](structk__work__delayable.md) \*

3678[k\_work\_delayable\_from\_work](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca)(struct [k\_work](structk__work.md) \*[work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629));

3679

[ 3693](group__workqueue__apis.md#ga1b76969667844f0981d348c9c671bc9f)int [k\_work\_delayable\_busy\_get](group__workqueue__apis.md#ga1b76969667844f0981d348c9c671bc9f)(const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3694

3709static inline bool [k\_work\_delayable\_is\_pending](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e)(

3710 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3711

3725static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_work\_delayable\_expires\_get](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624)(

3726 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3727

3741static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_work\_delayable\_remaining\_get](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4)(

3742 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3743

[ 3771](group__workqueue__apis.md#ga17f863c9f6ff2fb41dc0f3b7de4fdf23)int [k\_work\_schedule\_for\_queue](group__workqueue__apis.md#ga17f863c9f6ff2fb41dc0f3b7de4fdf23)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4),

3772 struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3773 [k\_timeout\_t](structk__timeout__t.md) delay);

3774

[ 3788](group__workqueue__apis.md#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)int [k\_work\_schedule](group__workqueue__apis.md#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3789 [k\_timeout\_t](structk__timeout__t.md) delay);

3790

[ 3826](group__workqueue__apis.md#gabf5db091eac19b19a4e12c0cb381f0a8)int [k\_work\_reschedule\_for\_queue](group__workqueue__apis.md#gabf5db091eac19b19a4e12c0cb381f0a8)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4),

3827 struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3828 [k\_timeout\_t](structk__timeout__t.md) delay);

3829

[ 3842](group__workqueue__apis.md#gaacaab408fb7c848d466ad1f069dfa648)int [k\_work\_reschedule](group__workqueue__apis.md#gaacaab408fb7c848d466ad1f069dfa648)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3843 [k\_timeout\_t](structk__timeout__t.md) delay);

3844

[ 3869](group__workqueue__apis.md#gad47d54e513030304be2600d75b1a965f)bool [k\_work\_flush\_delayable](group__workqueue__apis.md#gad47d54e513030304be2600d75b1a965f)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3870 struct [k\_work\_sync](structk__work__sync.md) \*sync);

3871

[ 3892](group__workqueue__apis.md#ga92355914ee178d4c3e848a1946bed3e4)int [k\_work\_cancel\_delayable](group__workqueue__apis.md#ga92355914ee178d4c3e848a1946bed3e4)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3893

[ 3922](group__workqueue__apis.md#ga7e7ec237648556fc16bfda8d35f7cd86)bool [k\_work\_cancel\_delayable\_sync](group__workqueue__apis.md#ga7e7ec237648556fc16bfda8d35f7cd86)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3923 struct [k\_work\_sync](structk__work__sync.md) \*sync);

3924

3925enum {

3929

3930 /\* The atomic API is used for all work and queue flags fields to

3931 \* enforce sequential consistency in SMP environments.

3932 \*/

3933

3934 /\* Bits that represent the work item states. At least nine of the

3935 \* combinations are distinct valid stable states.

3936 \*/

3937 K\_WORK\_RUNNING\_BIT = 0,

3938 K\_WORK\_CANCELING\_BIT = 1,

3939 K\_WORK\_QUEUED\_BIT = 2,

3940 K\_WORK\_DELAYED\_BIT = 3,

3941 K\_WORK\_FLUSHING\_BIT = 4,

3942

3943 K\_WORK\_MASK = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_DELAYED\_BIT) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUED\_BIT)

3944 | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_RUNNING\_BIT) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_CANCELING\_BIT) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_FLUSHING\_BIT),

3945

3946 /\* Static work flags \*/

3947 K\_WORK\_DELAYABLE\_BIT = 8,

3948 K\_WORK\_DELAYABLE = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_DELAYABLE\_BIT),

3949

3950 /\* Dynamic work queue flags \*/

3951 K\_WORK\_QUEUE\_STARTED\_BIT = 0,

3952 K\_WORK\_QUEUE\_STARTED = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_STARTED\_BIT),

3953 K\_WORK\_QUEUE\_BUSY\_BIT = 1,

3954 K\_WORK\_QUEUE\_BUSY = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_BUSY\_BIT),

3955 K\_WORK\_QUEUE\_DRAIN\_BIT = 2,

3956 K\_WORK\_QUEUE\_DRAIN = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_DRAIN\_BIT),

3957 K\_WORK\_QUEUE\_PLUGGED\_BIT = 3,

3958 K\_WORK\_QUEUE\_PLUGGED = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_PLUGGED\_BIT),

3959 K\_WORK\_QUEUE\_STOP\_BIT = 4,

3960 K\_WORK\_QUEUE\_STOP = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_STOP\_BIT),

3961

3962 /\* Static work queue flags \*/

3963 K\_WORK\_QUEUE\_NO\_YIELD\_BIT = 8,

3964 K\_WORK\_QUEUE\_NO\_YIELD = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_NO\_YIELD\_BIT),

3965

3969 /\* Transient work flags \*/

3970

[ 3976](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165) [K\_WORK\_RUNNING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_RUNNING\_BIT),

3977

[ 3982](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732) [K\_WORK\_CANCELING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_CANCELING\_BIT),

3983

[ 3989](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85) [K\_WORK\_QUEUED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUED\_BIT),

3990

[ 3996](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed) [K\_WORK\_DELAYED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_DELAYED\_BIT),

3997

[ 4002](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601) [K\_WORK\_FLUSHING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_FLUSHING\_BIT),

4003};

4004

[ 4006](structk__work.md)struct [k\_work](structk__work.md) {

4007 /\* All fields are protected by the work module spinlock. No fields

4008 \* are to be accessed except through kernel API.

4009 \*/

4010

4011 /\* Node to link into k\_work\_q pending list. \*/

[ 4012](structk__work.md#a85772682983e0fdeb735f0821d5710d4) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structk__work.md#a85772682983e0fdeb735f0821d5710d4);

4013

4014 /\* The function to be invoked by the work queue thread. \*/

[ 4015](structk__work.md#a096d6ca1338fb0fbfa330b790136f172) [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) [handler](structk__work.md#a096d6ca1338fb0fbfa330b790136f172);

4016

4017 /\* The queue on which the work item was last submitted. \*/

[ 4018](structk__work.md#a551be8394e041020c36a97dc2e12e137) struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137);

4019

4020 /\* State of the work item.

4021 \*

4022 \* The item can be DELAYED, QUEUED, and RUNNING simultaneously.

4023 \*

4024 \* It can be RUNNING and CANCELING simultaneously.

4025 \*/

[ 4026](structk__work.md#a391ed7d2039cd05c9894267bf8ea4dfd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structk__work.md#a391ed7d2039cd05c9894267bf8ea4dfd);

4027};

4028

4029#define Z\_WORK\_INITIALIZER(work\_handler) { \

4030 .handler = (work\_handler), \

4031}

4032

[ 4034](structk__work__delayable.md)struct [k\_work\_delayable](structk__work__delayable.md) {

4035 /\* The work item. \*/

[ 4036](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629) struct [k\_work](structk__work.md) [work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629);

4037

4038 /\* Timeout used to submit work after a delay. \*/

[ 4039](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d) struct \_timeout [timeout](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d);

4040

4041 /\* The queue to which the work should be submitted. \*/

[ 4042](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4) struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4);

4043};

4044

4045#define Z\_WORK\_DELAYABLE\_INITIALIZER(work\_handler) { \

4046 .work = { \

4047 .handler = (work\_handler), \

4048 .flags = K\_WORK\_DELAYABLE, \

4049 }, \

4050}

4051

[ 4068](group__workqueue__apis.md#ga893b281f3d2bc0088650536899e17903)#define K\_WORK\_DELAYABLE\_DEFINE(work, work\_handler) \

4069 struct k\_work\_delayable work \

4070 = Z\_WORK\_DELAYABLE\_INITIALIZER(work\_handler)

4071

4075

4076/\* Record used to wait for work to flush.

4077 \*

4078 \* The work item is inserted into the queue that will process (or is

4079 \* processing) the item, and will be processed as soon as the item

4080 \* completes. When the flusher is processed the semaphore will be

4081 \* signaled, releasing the thread waiting for the flush.

4082 \*/

4083struct z\_work\_flusher {

4084 struct [k\_work](structk__work.md) work;

4085 struct k\_sem sem;

4086};

4087

4088/\* Record used to wait for work to complete a cancellation.

4089 \*

4090 \* The work item is inserted into a global queue of pending cancels.

4091 \* When a cancelling work item goes idle any matching waiters are

4092 \* removed from pending\_cancels and are woken.

4093 \*/

4094struct z\_work\_canceller {

4095 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

4096 struct k\_work \*work;

4097 struct k\_sem sem;

4098};

4099

4103

[ 4117](structk__work__sync.md)struct [k\_work\_sync](structk__work__sync.md) {

4118 union {

[ 4119](structk__work__sync.md#ad81ff57cb9f2f3dc5f2d65917cf04f1c) struct z\_work\_flusher [flusher](structk__work__sync.md#ad81ff57cb9f2f3dc5f2d65917cf04f1c);

[ 4120](structk__work__sync.md#a7e8fd0b9d6736c403aefa8462c7c0835) struct z\_work\_canceller [canceller](structk__work__sync.md#a7e8fd0b9d6736c403aefa8462c7c0835);

4121 };

4122};

4123

[ 4130](structk__work__queue__config.md)struct [k\_work\_queue\_config](structk__work__queue__config.md) {

[ 4135](structk__work__queue__config.md#a0929d83372efff6798bc69bb7ca1eaaa) const char \*[name](structk__work__queue__config.md#a0929d83372efff6798bc69bb7ca1eaaa);

4136

[ 4149](structk__work__queue__config.md#afcf64d6e69d1ddfff8cbd749dafa4d13) bool [no\_yield](structk__work__queue__config.md#afcf64d6e69d1ddfff8cbd749dafa4d13);

4150

[ 4154](structk__work__queue__config.md#a5aa4a80d91ef36498443c163428b02c0) bool [essential](structk__work__queue__config.md#a5aa4a80d91ef36498443c163428b02c0);

4155};

4156

[ 4158](structk__work__q.md)struct [k\_work\_q](structk__work__q.md) {

4159 /\* The thread that animates the work. \*/

[ 4160](structk__work__q.md#aa42ca271a4989f129bf1a43c491327eb) struct [k\_thread](structk__thread.md) [thread](structk__work__q.md#aa42ca271a4989f129bf1a43c491327eb);

4161

4162 /\* All the following fields must be accessed only while the

4163 \* work module spinlock is held.

4164 \*/

4165

4166 /\* List of k\_work items to be worked. \*/

[ 4167](structk__work__q.md#a2012199571f6b658873550d64386b00c) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [pending](structk__work__q.md#a2012199571f6b658873550d64386b00c);

4168

4169 /\* Wait queue for idle work thread. \*/

[ 4170](structk__work__q.md#a561c90f8bb944217230e00052cdecf10) \_wait\_q\_t [notifyq](structk__work__q.md#a561c90f8bb944217230e00052cdecf10);

4171

4172 /\* Wait queue for threads waiting for the queue to drain. \*/

[ 4173](structk__work__q.md#a308d1ac78b1203b7ea78b0f18c5bdf5b) \_wait\_q\_t [drainq](structk__work__q.md#a308d1ac78b1203b7ea78b0f18c5bdf5b);

4174

4175 /\* Flags describing queue state. \*/

[ 4176](structk__work__q.md#a68bc8e9c412ebdbf34827087d91a080e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structk__work__q.md#a68bc8e9c412ebdbf34827087d91a080e);

4177};

4178

4179/\* Provide the implementation for inline functions declared above \*/

4180

[ 4181](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)static inline bool [k\_work\_is\_pending](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)(const struct [k\_work](structk__work.md) \*work)

4182{

4183 return [k\_work\_busy\_get](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b)(work) != 0;

4184}

4185

4186static inline struct [k\_work\_delayable](structk__work__delayable.md) \*

[ 4187](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca)[k\_work\_delayable\_from\_work](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca)(struct [k\_work](structk__work.md) \*[work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629))

4188{

4189 return [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)([work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629), struct [k\_work\_delayable](structk__work__delayable.md), [work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629));

4190}

4191

[ 4192](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e)static inline bool [k\_work\_delayable\_is\_pending](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e)(

4193 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork)

4194{

4195 return [k\_work\_delayable\_busy\_get](group__workqueue__apis.md#ga1b76969667844f0981d348c9c671bc9f)(dwork) != 0;

4196}

4197

[ 4198](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624)static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_work\_delayable\_expires\_get](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624)(

4199 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork)

4200{

4201 return z\_timeout\_expires(&dwork->[timeout](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d));

4202}

4203

[ 4204](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4)static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_work\_delayable\_remaining\_get](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4)(

4205 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork)

4206{

4207 return z\_timeout\_remaining(&dwork->[timeout](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d));

4208}

4209

[ 4210](group__workqueue__apis.md#ga0b8b496f7e7bd82d08590a07293e38d7)static inline [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_work\_queue\_thread\_get](group__workqueue__apis.md#ga0b8b496f7e7bd82d08590a07293e38d7)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4))

4211{

4212 return &[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4)->[thread](structk__work__q.md#aa42ca271a4989f129bf1a43c491327eb);

4213}

4214

4216

4217struct k\_work\_user;

4218

4223

[ 4233](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc)typedef void (\*[k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc))(struct k\_work\_user \*work);

4234

4238

4239struct k\_work\_user\_q {

4240 struct [k\_queue](structk__queue.md) queue;

4241 struct [k\_thread](structk__thread.md) thread;

4242};

4243

4244enum {

4245 K\_WORK\_USER\_STATE\_PENDING, /\* Work item pending state \*/

4246};

4247

4248struct k\_work\_user {

4249 void \*\_reserved; /\* Used by k\_queue implementation. \*/

4250 [k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc) handler;

4251 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

4252};

4253

4257

4258#if defined(\_\_cplusplus) && ((\_\_cplusplus - 0) < 202002L)

4259#define Z\_WORK\_USER\_INITIALIZER(work\_handler) { NULL, work\_handler, 0 }

4260#else

4261#define Z\_WORK\_USER\_INITIALIZER(work\_handler) \

4262 { \

4263 .\_reserved = NULL, \

4264 .handler = (work\_handler), \

4265 .flags = 0 \

4266 }

4267#endif

4268

[ 4280](group__workqueue__apis.md#ga4f3eac1fc56d5c9c21a3afa9b964b0bf)#define K\_WORK\_USER\_DEFINE(work, work\_handler) \

4281 struct k\_work\_user work = Z\_WORK\_USER\_INITIALIZER(work\_handler)

4282

[ 4292](group__workqueue__apis.md#ga9de9c7a7f13cc6b325e5453e34afe62d)static inline void [k\_work\_user\_init](group__workqueue__apis.md#ga9de9c7a7f13cc6b325e5453e34afe62d)(struct k\_work\_user \*work,

4293 [k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc) handler)

4294{

4295 \*work = (struct k\_work\_user)Z\_WORK\_USER\_INITIALIZER(handler);

4296}

4297

[ 4314](group__workqueue__apis.md#ga58d05d4127e4cd51104a1f1a87f626cd)static inline bool [k\_work\_user\_is\_pending](group__workqueue__apis.md#ga58d05d4127e4cd51104a1f1a87f626cd)(struct k\_work\_user \*work)

4315{

4316 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(&work->flags, K\_WORK\_USER\_STATE\_PENDING);

4317}

4318

[ 4337](group__workqueue__apis.md#ga50ae1f6f74c0bc0a41dbbf789fff8856)static inline int [k\_work\_user\_submit\_to\_queue](group__workqueue__apis.md#ga50ae1f6f74c0bc0a41dbbf789fff8856)(struct k\_work\_user\_q \*work\_q,

4338 struct k\_work\_user \*work)

4339{

4340 int ret = -[EBUSY](group__system__errno.md#ga8368025077a0385849d6817b2007c095);

4341

4342 if (![atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)(&work->flags,

4343 K\_WORK\_USER\_STATE\_PENDING)) {

4344 ret = [k\_queue\_alloc\_append](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a)(&work\_q->queue, work);

4345

4346 /\* Couldn't insert into the queue. Clear the pending bit

4347 \* so the work item can be submitted again

4348 \*/

4349 if (ret != 0) {

4350 [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)(&work->flags,

4351 K\_WORK\_USER\_STATE\_PENDING);

4352 }

4353 }

4354

4355 return ret;

4356}

4357

[ 4377](group__workqueue__apis.md#ga3091bc8fab5311252e41634a97a18589)void [k\_work\_user\_queue\_start](group__workqueue__apis.md#ga3091bc8fab5311252e41634a97a18589)(struct k\_work\_user\_q \*work\_q,

4378 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack,

4379 size\_t stack\_size, int prio,

4380 const char \*name);

4381

[ 4392](group__workqueue__apis.md#gab487068e9564cd77b6bdbac3d5670923)static inline [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_work\_user\_queue\_thread\_get](group__workqueue__apis.md#gab487068e9564cd77b6bdbac3d5670923)(struct k\_work\_user\_q \*work\_q)

4393{

4394 return &work\_q->thread;

4395}

4396

4398

4402

4403struct k\_work\_poll {

4404 struct k\_work work;

4405 struct k\_work\_q \*workq;

4406 struct z\_poller poller;

4407 struct k\_poll\_event \*events;

4408 int num\_events;

4409 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) real\_handler;

4410 struct \_timeout timeout;

4411 int poll\_result;

4412};

4413

4417

4422

[ 4434](group__workqueue__apis.md#gaf8e003eefa5dd66ba883688f9d39c333)#define K\_WORK\_DEFINE(work, work\_handler) \

4435 struct k\_work work = Z\_WORK\_INITIALIZER(work\_handler)

4436

[ 4446](group__workqueue__apis.md#ga371dab33a40622bea19b07d852863443)void [k\_work\_poll\_init](group__workqueue__apis.md#ga371dab33a40622bea19b07d852863443)(struct k\_work\_poll \*work,

4447 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) handler);

4448

[ 4483](group__workqueue__apis.md#ga0abafd7f851e42fd3572c8438e600a53)int [k\_work\_poll\_submit\_to\_queue](group__workqueue__apis.md#ga0abafd7f851e42fd3572c8438e600a53)(struct [k\_work\_q](structk__work__q.md) \*work\_q,

4484 struct k\_work\_poll \*work,

4485 struct [k\_poll\_event](structk__poll__event.md) \*events,

4486 int num\_events,

4487 [k\_timeout\_t](structk__timeout__t.md) timeout);

4488

[ 4520](group__workqueue__apis.md#gad9f222e46d72c4f98739395a0c8bb4ea)int [k\_work\_poll\_submit](group__workqueue__apis.md#gad9f222e46d72c4f98739395a0c8bb4ea)(struct k\_work\_poll \*work,

4521 struct [k\_poll\_event](structk__poll__event.md) \*events,

4522 int num\_events,

4523 [k\_timeout\_t](structk__timeout__t.md) timeout);

4524

[ 4539](group__workqueue__apis.md#ga2a19547d04dc1a202e80b752e3177215)int [k\_work\_poll\_cancel](group__workqueue__apis.md#ga2a19547d04dc1a202e80b752e3177215)(struct k\_work\_poll \*work);

4540

4542

4548

[ 4552](structk__msgq.md)struct [k\_msgq](structk__msgq.md) {

[ 4554](structk__msgq.md#ae3b3d53d60b789d69c65494cfd090076) \_wait\_q\_t [wait\_q](structk__msgq.md#ae3b3d53d60b789d69c65494cfd090076);

[ 4556](structk__msgq.md#aa2e00a7292502f0de88cff28c5e375f0) struct [k\_spinlock](structk__spinlock.md) [lock](structk__msgq.md#aa2e00a7292502f0de88cff28c5e375f0);

[ 4558](structk__msgq.md#a512fe468da96540639a0d71f1707f79d) size\_t [msg\_size](structk__msgq.md#a512fe468da96540639a0d71f1707f79d);

[ 4560](structk__msgq.md#aebd3b6e91e97b2d4369feea1a3f7b7a0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_msgs](structk__msgq.md#aebd3b6e91e97b2d4369feea1a3f7b7a0);

[ 4562](structk__msgq.md#aca77f1cf833d3aa27ae65004b446bdd2) char \*[buffer\_start](structk__msgq.md#aca77f1cf833d3aa27ae65004b446bdd2);

[ 4564](structk__msgq.md#a9d47fd25d7a70e8518d45dd48c51f0e0) char \*[buffer\_end](structk__msgq.md#a9d47fd25d7a70e8518d45dd48c51f0e0);

[ 4566](structk__msgq.md#a594e8a4a638521f42f24f85fe0742d64) char \*[read\_ptr](structk__msgq.md#a594e8a4a638521f42f24f85fe0742d64);

[ 4568](structk__msgq.md#aacf9b7b9f6e26e402f3752fc56834f23) char \*[write\_ptr](structk__msgq.md#aacf9b7b9f6e26e402f3752fc56834f23);

[ 4570](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [used\_msgs](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857);

4571

4572 Z\_DECL\_POLL\_EVENT

4573

[ 4575](structk__msgq.md#ae03025420908f8342ce12a1395c7657b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structk__msgq.md#ae03025420908f8342ce12a1395c7657b);

4576

4577 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_msgq](structk__msgq.md))

4578

4579#ifdef CONFIG\_OBJ\_CORE\_MSGQ

4580 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

4581#endif

4582};

4583

4586

4587

4588#define Z\_MSGQ\_INITIALIZER(obj, q\_buffer, q\_msg\_size, q\_max\_msgs) \

4589 { \

4590 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

4591 .msg\_size = q\_msg\_size, \

4592 .max\_msgs = q\_max\_msgs, \

4593 .buffer\_start = q\_buffer, \

4594 .buffer\_end = q\_buffer + (q\_max\_msgs \* q\_msg\_size), \

4595 .read\_ptr = q\_buffer, \

4596 .write\_ptr = q\_buffer, \

4597 .used\_msgs = 0, \

4598 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

4599 }

4600

4604

4605

[ 4606](group__msgq__apis.md#ga4bb73f46fd0818f7f7a90860b792f7ce)#define K\_MSGQ\_FLAG\_ALLOC BIT(0)

4607

[ 4611](structk__msgq__attrs.md)struct [k\_msgq\_attrs](structk__msgq__attrs.md) {

[ 4613](structk__msgq__attrs.md#a7d1d72946bdd517c07da37493a89e30e) size\_t [msg\_size](structk__msgq__attrs.md#a7d1d72946bdd517c07da37493a89e30e);

[ 4615](structk__msgq__attrs.md#ad0f5894ba0da840b91eb85015252e649) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_msgs](structk__msgq__attrs.md#ad0f5894ba0da840b91eb85015252e649);

[ 4617](structk__msgq__attrs.md#a00f936870442fa455117cbdd7821fac5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [used\_msgs](structk__msgq__attrs.md#a00f936870442fa455117cbdd7821fac5);

4618};

4619

4620

[ 4639](group__msgq__apis.md#ga95ef93002766901511d09c8cd8f8293b)#define K\_MSGQ\_DEFINE(q\_name, q\_msg\_size, q\_max\_msgs, q\_align) \

4640 static char \_\_noinit \_\_aligned(q\_align) \

4641 \_k\_fifo\_buf\_##q\_name[(q\_max\_msgs) \* (q\_msg\_size)]; \

4642 STRUCT\_SECTION\_ITERABLE(k\_msgq, q\_name) = \

4643 Z\_MSGQ\_INITIALIZER(q\_name, \_k\_fifo\_buf\_##q\_name, \

4644 (q\_msg\_size), (q\_max\_msgs))

4645

[ 4660](group__msgq__apis.md#ga54a5cdcaea2236c383ace433fedc0d39)void [k\_msgq\_init](group__msgq__apis.md#ga54a5cdcaea2236c383ace433fedc0d39)(struct [k\_msgq](structk__msgq.md) \*msgq, char \*buffer, size\_t msg\_size,

4661 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_msgs);

4662

[ 4682](group__msgq__apis.md#gabe7305b8f442ebdc147dbbc6e8cf92fc)\_\_syscall int [k\_msgq\_alloc\_init](group__msgq__apis.md#gabe7305b8f442ebdc147dbbc6e8cf92fc)(struct [k\_msgq](structk__msgq.md) \*msgq, size\_t msg\_size,

4683 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_msgs);

4684

[ 4695](group__msgq__apis.md#gafda4399aa9b8f1e44bdf752e00ea787b)int [k\_msgq\_cleanup](group__msgq__apis.md#gafda4399aa9b8f1e44bdf752e00ea787b)(struct [k\_msgq](structk__msgq.md) \*msgq);

4696

[ 4717](group__msgq__apis.md#ga54e96aaaea5462a1f963b7fd5ca82bfe)\_\_syscall int [k\_msgq\_put](group__msgq__apis.md#ga54e96aaaea5462a1f963b7fd5ca82bfe)(struct [k\_msgq](structk__msgq.md) \*msgq, const void \*data, [k\_timeout\_t](structk__timeout__t.md) timeout);

4718

[ 4739](group__msgq__apis.md#gae67f2ced2df1f9c290ae15dab9097cb7)\_\_syscall int [k\_msgq\_get](group__msgq__apis.md#gae67f2ced2df1f9c290ae15dab9097cb7)(struct [k\_msgq](structk__msgq.md) \*msgq, void \*data, [k\_timeout\_t](structk__timeout__t.md) timeout);

4740

[ 4755](group__msgq__apis.md#ga14f543472f2f63cfde0bdfa87b95c915)\_\_syscall int [k\_msgq\_peek](group__msgq__apis.md#ga14f543472f2f63cfde0bdfa87b95c915)(struct [k\_msgq](structk__msgq.md) \*msgq, void \*data);

4756

[ 4773](group__msgq__apis.md#ga69b004a40ab4ca497de314a99960fb8e)\_\_syscall int [k\_msgq\_peek\_at](group__msgq__apis.md#ga69b004a40ab4ca497de314a99960fb8e)(struct [k\_msgq](structk__msgq.md) \*msgq, void \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx);

4774

[ 4784](group__msgq__apis.md#gaa18875887773195ae44b7fe0972ee760)\_\_syscall void [k\_msgq\_purge](group__msgq__apis.md#gaa18875887773195ae44b7fe0972ee760)(struct [k\_msgq](structk__msgq.md) \*msgq);

4785

[ 4796](group__msgq__apis.md#ga7d154beb4f9c6227eddbef26d406ca24)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_msgq\_num\_free\_get](group__msgq__apis.md#ga7d154beb4f9c6227eddbef26d406ca24)(struct [k\_msgq](structk__msgq.md) \*msgq);

4797

[ 4806](group__msgq__apis.md#ga8f9d3eef67cbc9c0717a84190bbf7f41)\_\_syscall void [k\_msgq\_get\_attrs](group__msgq__apis.md#ga8f9d3eef67cbc9c0717a84190bbf7f41)(struct [k\_msgq](structk__msgq.md) \*msgq,

4807 struct [k\_msgq\_attrs](structk__msgq__attrs.md) \*attrs);

4808

4809

4810static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_k\_msgq\_num\_free\_get(struct [k\_msgq](structk__msgq.md) \*msgq)

4811{

4812 return msgq->[max\_msgs](structk__msgq.md#aebd3b6e91e97b2d4369feea1a3f7b7a0) - msgq->[used\_msgs](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857);

4813}

4814

[ 4824](group__msgq__apis.md#ga458793a89f1d9f762bda3422918a9faa)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_msgq\_num\_used\_get](group__msgq__apis.md#ga458793a89f1d9f762bda3422918a9faa)(struct [k\_msgq](structk__msgq.md) \*msgq);

4825

4826static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_k\_msgq\_num\_used\_get(struct [k\_msgq](structk__msgq.md) \*msgq)

4827{

4828 return msgq->[used\_msgs](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857);

4829}

4830

4832

4838

[ 4843](structk__mbox__msg.md)struct [k\_mbox\_msg](structk__mbox__msg.md) {

[ 4845](structk__mbox__msg.md#aeabf45e9599a64852a1cfd656b1ece8e) size\_t [size](structk__mbox__msg.md#aeabf45e9599a64852a1cfd656b1ece8e);

[ 4847](structk__mbox__msg.md#aa79f2bf71431b474ec4551ade4d7a8dd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [info](structk__mbox__msg.md#aa79f2bf71431b474ec4551ade4d7a8dd);

[ 4849](structk__mbox__msg.md#a74b0edeed4c44cb5932eb292efc9d9c2) void \*[tx\_data](structk__mbox__msg.md#a74b0edeed4c44cb5932eb292efc9d9c2);

[ 4851](structk__mbox__msg.md#a9eb145a242ac66e80d90286d83fe7a61) [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [rx\_source\_thread](structk__mbox__msg.md#a9eb145a242ac66e80d90286d83fe7a61);

[ 4853](structk__mbox__msg.md#a73236acb7d27bb0233f5abb7214fb19c) [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [tx\_target\_thread](structk__mbox__msg.md#a73236acb7d27bb0233f5abb7214fb19c);

4855 [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) \_syncing\_thread;

4856#if (CONFIG\_NUM\_MBOX\_ASYNC\_MSGS > 0)

4858 struct k\_sem \*\_async\_sem;

4859#endif

4860};

4861

[ 4865](structk__mbox.md)struct [k\_mbox](structk__mbox.md) {

[ 4867](structk__mbox.md#a0bca912a50120707ddafa66d740ade96) \_wait\_q\_t [tx\_msg\_queue](structk__mbox.md#a0bca912a50120707ddafa66d740ade96);

[ 4869](structk__mbox.md#a808a14c31892a2d042cdb0723a2956e2) \_wait\_q\_t [rx\_msg\_queue](structk__mbox.md#a808a14c31892a2d042cdb0723a2956e2);

[ 4870](structk__mbox.md#a2c549d5bd7216b62d81ad2198e0d79e4) struct [k\_spinlock](structk__spinlock.md) [lock](structk__mbox.md#a2c549d5bd7216b62d81ad2198e0d79e4);

4871

4872 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_mbox](structk__mbox.md))

4873

4874#ifdef CONFIG\_OBJ\_CORE\_MAILBOX

4875 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

4876#endif

4877};

4878

4881

4882#define Z\_MBOX\_INITIALIZER(obj) \

4883 { \

4884 .tx\_msg\_queue = Z\_WAIT\_Q\_INIT(&obj.tx\_msg\_queue), \

4885 .rx\_msg\_queue = Z\_WAIT\_Q\_INIT(&obj.rx\_msg\_queue), \

4886 }

4887

4891

[ 4901](group__mailbox__apis.md#gab55cba898db47113a06641c01f3e3714)#define K\_MBOX\_DEFINE(name) \

4902 STRUCT\_SECTION\_ITERABLE(k\_mbox, name) = \

4903 Z\_MBOX\_INITIALIZER(name) \

4904

4905

[ 4912](group__mailbox__apis.md#ga686f20c199a9e971822d8279d175d8c2)void [k\_mbox\_init](group__mailbox__apis.md#ga686f20c199a9e971822d8279d175d8c2)(struct [k\_mbox](structk__mbox.md) \*mbox);

4913

[ 4933](group__mailbox__apis.md#gaa1e5cdd992d8b9be11f82254e1886ed2)int [k\_mbox\_put](group__mailbox__apis.md#gaa1e5cdd992d8b9be11f82254e1886ed2)(struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*tx\_msg,

4934 [k\_timeout\_t](structk__timeout__t.md) timeout);

4935

[ 4949](group__mailbox__apis.md#gadd60f7b760371c0a141a1e4da253a0f0)void [k\_mbox\_async\_put](group__mailbox__apis.md#gadd60f7b760371c0a141a1e4da253a0f0)(struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*tx\_msg,

4950 struct k\_sem \*sem);

4951

[ 4969](group__mailbox__apis.md#ga2ea91154620b139dbed1ad949b97c3ef)int [k\_mbox\_get](group__mailbox__apis.md#ga2ea91154620b139dbed1ad949b97c3ef)(struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*rx\_msg,

4970 void \*buffer, [k\_timeout\_t](structk__timeout__t.md) timeout);

4971

[ 4985](group__mailbox__apis.md#ga3d19e648e67f109609259543c9a01d6e)void [k\_mbox\_data\_get](group__mailbox__apis.md#ga3d19e648e67f109609259543c9a01d6e)(struct [k\_mbox\_msg](structk__mbox__msg.md) \*rx\_msg, void \*buffer);

4986

4988

4994

[ 5004](group__pipe__apis.md#gae2c8d97af1f7e9deb93e670859525cf3)\_\_syscall void [k\_pipe\_init](group__pipe__apis.md#gae2c8d97af1f7e9deb93e670859525cf3)(struct [k\_pipe](structk__pipe.md) \*pipe, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t buffer\_size);

5005

5006#ifdef CONFIG\_PIPES

5008struct [k\_pipe](structk__pipe.md) {

5009 unsigned char \*buffer;

5010 size\_t size;

5011 size\_t bytes\_used;

5012 size\_t read\_index;

5013 size\_t write\_index;

5014 struct [k\_spinlock](structk__spinlock.md) [lock](structk__pipe.md#aa2a367a9c8f0be89bcdf1bf6d3b0b875);

5015

5016 struct {

5017 \_wait\_q\_t readers;

5018 \_wait\_q\_t writers;

5019 } wait\_q;

5020

5021 Z\_DECL\_POLL\_EVENT

5022

5023 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structk__pipe.md#a2ed95fbe24ea20c4f292a66def1d4dde);

5024

5025 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_pipe)

5026

5027#ifdef CONFIG\_OBJ\_CORE\_PIPE

5028 struct k\_obj\_core obj\_core;

5029#endif

5030};

5031

5035#define K\_PIPE\_FLAG\_ALLOC BIT(0)

5036

5037#define Z\_PIPE\_INITIALIZER(obj, pipe\_buffer, pipe\_buffer\_size) \

5038 { \

5039 .buffer = pipe\_buffer, \

5040 .size = pipe\_buffer\_size, \

5041 .bytes\_used = 0, \

5042 .read\_index = 0, \

5043 .write\_index = 0, \

5044 .lock = {}, \

5045 .wait\_q = { \

5046 .readers = Z\_WAIT\_Q\_INIT(&obj.wait\_q.readers), \

5047 .writers = Z\_WAIT\_Q\_INIT(&obj.wait\_q.writers) \

5048 }, \

5049 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

5050 .flags = 0, \

5051 }

5052

5056

5070#define K\_PIPE\_DEFINE(name, pipe\_buffer\_size, pipe\_align) \

5071 static unsigned char \_\_noinit \_\_aligned(pipe\_align) \

5072 \_k\_pipe\_buf\_##name[pipe\_buffer\_size]; \

5073 STRUCT\_SECTION\_ITERABLE(k\_pipe, name) = \

5074 Z\_PIPE\_INITIALIZER(name, \_k\_pipe\_buf\_##name, pipe\_buffer\_size)

5075

5088\_\_deprecated int k\_pipe\_cleanup(struct [k\_pipe](structk__pipe.md) \*pipe);

5089

5106\_\_deprecated \_\_syscall int k\_pipe\_alloc\_init(struct [k\_pipe](structk__pipe.md) \*pipe, size\_t size);

5107

5127\_\_deprecated \_\_syscall int k\_pipe\_put(struct [k\_pipe](structk__pipe.md) \*pipe, const void \*data,

5128 size\_t bytes\_to\_write, size\_t \*bytes\_written,

5129 size\_t min\_xfer, [k\_timeout\_t](structk__timeout__t.md) timeout);

5130

5151\_\_deprecated \_\_syscall int k\_pipe\_get(struct [k\_pipe](structk__pipe.md) \*pipe, void \*data,

5152 size\_t bytes\_to\_read, size\_t \*bytes\_read,

5153 size\_t min\_xfer, [k\_timeout\_t](structk__timeout__t.md) timeout);

5154

5164\_\_deprecated \_\_syscall size\_t k\_pipe\_read\_avail(struct [k\_pipe](structk__pipe.md) \*pipe);

5165

5175\_\_deprecated \_\_syscall size\_t k\_pipe\_write\_avail(struct [k\_pipe](structk__pipe.md) \*pipe);

5176

5188\_\_deprecated \_\_syscall void k\_pipe\_flush(struct [k\_pipe](structk__pipe.md) \*pipe);

5189

5202\_\_deprecated \_\_syscall void k\_pipe\_buffer\_flush(struct [k\_pipe](structk__pipe.md) \*pipe);

5203

5204#else /\* CONFIG\_PIPES \*/

5205

[ 5206](group__pipe__apis.md#gae5471546043f4d14e97c3f6313053ee0)enum [pipe\_flags](group__pipe__apis.md#gae5471546043f4d14e97c3f6313053ee0) {

[ 5207](group__pipe__apis.md#ggae5471546043f4d14e97c3f6313053ee0a9fc19eac7b41c00ca97c2fb0a30a2309) [PIPE\_FLAG\_OPEN](group__pipe__apis.md#ggae5471546043f4d14e97c3f6313053ee0a9fc19eac7b41c00ca97c2fb0a30a2309) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 5208](group__pipe__apis.md#ggae5471546043f4d14e97c3f6313053ee0a37642c400a675e1dce34c9b878874df4) [PIPE\_FLAG\_RESET](group__pipe__apis.md#ggae5471546043f4d14e97c3f6313053ee0a37642c400a675e1dce34c9b878874df4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

5209};

5210

[ 5211](structk__pipe.md)struct [k\_pipe](structk__pipe.md) {

[ 5212](structk__pipe.md#ac9162db42883d2c14f63cf74ff3c1179) size\_t [waiting](structk__pipe.md#ac9162db42883d2c14f63cf74ff3c1179);

[ 5213](structk__pipe.md#a62556b1fbb907dcb8fbbe29c597d8473) struct [ring\_buf](structring__buf.md) [buf](structk__pipe.md#a62556b1fbb907dcb8fbbe29c597d8473);

[ 5214](structk__pipe.md#aa2a367a9c8f0be89bcdf1bf6d3b0b875) struct [k\_spinlock](structk__spinlock.md) [lock](structk__pipe.md#aa2a367a9c8f0be89bcdf1bf6d3b0b875);

[ 5215](structk__pipe.md#a8af11082e53b56670f0ce11e581766ff) \_wait\_q\_t [data](structk__pipe.md#a8af11082e53b56670f0ce11e581766ff);

[ 5216](structk__pipe.md#aa1428192b88b97e0cb5ec83894770f47) \_wait\_q\_t [space](structk__pipe.md#aa1428192b88b97e0cb5ec83894770f47);

[ 5217](structk__pipe.md#a2ed95fbe24ea20c4f292a66def1d4dde) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structk__pipe.md#a2ed95fbe24ea20c4f292a66def1d4dde);

5218

5219 Z\_DECL\_POLL\_EVENT

5220#ifdef CONFIG\_OBJ\_CORE\_PIPE

5221 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

5222#endif

5223 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_pipe](structk__pipe.md))

5224};

5225

5229#define Z\_PIPE\_INITIALIZER(obj, pipe\_buffer, pipe\_buffer\_size) \

5230{ \

5231 .buf = RING\_BUF\_INIT(pipe\_buffer, pipe\_buffer\_size), \

5232 .data = Z\_WAIT\_Q\_INIT(&obj.data), \

5233 .space = Z\_WAIT\_Q\_INIT(&obj.space), \

5234 .flags = PIPE\_FLAG\_OPEN, \

5235 .waiting = 0, \

5236 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

5237}

5241

[ 5255](group__pipe__apis.md#gac2256aa00c59e78199be9bdefd61aa52)#define K\_PIPE\_DEFINE(name, pipe\_buffer\_size, pipe\_align) \

5256 static unsigned char \_\_noinit \_\_aligned(pipe\_align) \

5257 \_k\_pipe\_buf\_##name[pipe\_buffer\_size]; \

5258 STRUCT\_SECTION\_ITERABLE(k\_pipe, name) = \

5259 Z\_PIPE\_INITIALIZER(name, \_k\_pipe\_buf\_##name, pipe\_buffer\_size)

5260

5261

[ 5278](group__pipe__apis.md#ga514ab3d174dcada766ecbda138944ddc)\_\_syscall int [k\_pipe\_write](group__pipe__apis.md#ga514ab3d174dcada766ecbda138944ddc)(struct [k\_pipe](structk__pipe.md) \*pipe, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len,

5279 [k\_timeout\_t](structk__timeout__t.md) timeout);

5280

[ 5296](group__pipe__apis.md#gaecb07412025d9e065ee7b99121522257)\_\_syscall int [k\_pipe\_read](group__pipe__apis.md#gaecb07412025d9e065ee7b99121522257)(struct [k\_pipe](structk__pipe.md) \*pipe, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len,

5297 [k\_timeout\_t](structk__timeout__t.md) timeout);

5298

[ 5308](group__pipe__apis.md#gaaedff72169127b8227c80bf8adf1f9dd)\_\_syscall void [k\_pipe\_reset](group__pipe__apis.md#gaaedff72169127b8227c80bf8adf1f9dd)(struct [k\_pipe](structk__pipe.md) \*pipe);

5309

[ 5318](group__pipe__apis.md#ga83d4b5de8902845850d01b0c3db0702a)\_\_syscall void [k\_pipe\_close](group__pipe__apis.md#ga83d4b5de8902845850d01b0c3db0702a)(struct [k\_pipe](structk__pipe.md) \*pipe);

5319#endif /\* CONFIG\_PIPES \*/

5321

5325struct k\_mem\_slab\_info {

5326 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks;

5327 size\_t block\_size;

5328 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_used;

5329#ifdef CONFIG\_MEM\_SLAB\_TRACE\_MAX\_UTILIZATION

5330 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_used;

5331#endif

5332};

5333

5334struct k\_mem\_slab {

5335 \_wait\_q\_t wait\_q;

5336 struct k\_spinlock lock;

5337 char \*buffer;

5338 char \*free\_list;

5339 struct k\_mem\_slab\_info info;

5340

5341 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_mem\_slab)

5342

5343#ifdef CONFIG\_OBJ\_CORE\_MEM\_SLAB

5344 struct k\_obj\_core obj\_core;

5345#endif

5346};

5347

5348#define Z\_MEM\_SLAB\_INITIALIZER(\_slab, \_slab\_buffer, \_slab\_block\_size, \

5349 \_slab\_num\_blocks) \

5350 { \

5351 .wait\_q = Z\_WAIT\_Q\_INIT(&(\_slab).wait\_q), \

5352 .lock = {}, \

5353 .buffer = \_slab\_buffer, \

5354 .free\_list = NULL, \

5355 .info = {\_slab\_num\_blocks, \_slab\_block\_size, 0} \

5356 }

5357

5358

5362

5368

[ 5392](group__mem__slab__apis.md#ga60bc92eee58fcc5f121b8e4d82eaa69e)#define K\_MEM\_SLAB\_DEFINE(name, slab\_block\_size, slab\_num\_blocks, slab\_align) \

5393 char \_\_noinit\_named(k\_mem\_slab\_buf\_##name) \

5394 \_\_aligned(WB\_UP(slab\_align)) \

5395 \_k\_mem\_slab\_buf\_##name[(slab\_num\_blocks) \* WB\_UP(slab\_block\_size)]; \

5396 STRUCT\_SECTION\_ITERABLE(k\_mem\_slab, name) = \

5397 Z\_MEM\_SLAB\_INITIALIZER(name, \_k\_mem\_slab\_buf\_##name, \

5398 WB\_UP(slab\_block\_size), slab\_num\_blocks)

5399

[ 5414](group__mem__slab__apis.md#ga90bdbb15f410991f54ba16025c24bc3c)#define K\_MEM\_SLAB\_DEFINE\_STATIC(name, slab\_block\_size, slab\_num\_blocks, slab\_align) \

5415 static char \_\_noinit\_named(k\_mem\_slab\_buf\_##name) \

5416 \_\_aligned(WB\_UP(slab\_align)) \

5417 \_k\_mem\_slab\_buf\_##name[(slab\_num\_blocks) \* WB\_UP(slab\_block\_size)]; \

5418 static STRUCT\_SECTION\_ITERABLE(k\_mem\_slab, name) = \

5419 Z\_MEM\_SLAB\_INITIALIZER(name, \_k\_mem\_slab\_buf\_##name, \

5420 WB\_UP(slab\_block\_size), slab\_num\_blocks)

5421

[ 5443](group__mem__slab__apis.md#ga094a8f173f287e29bb287119c26889d1)int [k\_mem\_slab\_init](group__mem__slab__apis.md#ga094a8f173f287e29bb287119c26889d1)(struct k\_mem\_slab \*slab, void \*buffer,

5444 size\_t block\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks);

5445

[ 5468](group__mem__slab__apis.md#gab16a46d8394aca18de740ad044a8734a)int [k\_mem\_slab\_alloc](group__mem__slab__apis.md#gab16a46d8394aca18de740ad044a8734a)(struct k\_mem\_slab \*slab, void \*\*mem,

5469 [k\_timeout\_t](structk__timeout__t.md) timeout);

5470

[ 5480](group__mem__slab__apis.md#ga2635ea8f9a30b8751ec966fe62adc0e1)void [k\_mem\_slab\_free](group__mem__slab__apis.md#ga2635ea8f9a30b8751ec966fe62adc0e1)(struct k\_mem\_slab \*slab, void \*mem);

5481

[ 5492](group__mem__slab__apis.md#gac76b96d7055e4ad94765c93530dd0720)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_mem\_slab\_num\_used\_get](group__mem__slab__apis.md#gac76b96d7055e4ad94765c93530dd0720)(struct k\_mem\_slab \*slab)

5493{

5494 return slab->info.num\_used;

5495}

5496

[ 5507](group__mem__slab__apis.md#gae0e949c1c3476dd57bc0c0ed627d2346)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_mem\_slab\_max\_used\_get](group__mem__slab__apis.md#gae0e949c1c3476dd57bc0c0ed627d2346)(struct k\_mem\_slab \*slab)

5508{

5509#ifdef CONFIG\_MEM\_SLAB\_TRACE\_MAX\_UTILIZATION

5510 return slab->info.max\_used;

5511#else

5512 ARG\_UNUSED(slab);

5513 return 0;

5514#endif

5515}

5516

[ 5527](group__mem__slab__apis.md#gae87577e2873cf746db69216a82f94aea)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_mem\_slab\_num\_free\_get](group__mem__slab__apis.md#gae87577e2873cf746db69216a82f94aea)(struct k\_mem\_slab \*slab)

5528{

5529 return slab->info.num\_blocks - slab->info.num\_used;

5530}

5531

5543

[ 5544](group__mem__slab__apis.md#ga32030a5cfb44f663bd31b4e1b3d5dddb)int [k\_mem\_slab\_runtime\_stats\_get](group__mem__slab__apis.md#ga32030a5cfb44f663bd31b4e1b3d5dddb)(struct k\_mem\_slab \*slab, struct [sys\_memory\_stats](structsys__memory__stats.md) \*stats);

5545

[ 5557](group__mem__slab__apis.md#gaa1f44e30f4aee98b38e1ab5e93af505c)int [k\_mem\_slab\_runtime\_stats\_reset\_max](group__mem__slab__apis.md#gaa1f44e30f4aee98b38e1ab5e93af505c)(struct k\_mem\_slab \*slab);

5558

5560

5565

5566/\* kernel synchronized heap struct \*/

5567

[ 5568](structk__heap.md)struct [k\_heap](structk__heap.md) {

[ 5569](structk__heap.md#a4b8551f4fd1cd648c68f47ea2ebd682f) struct [sys\_heap](structsys__heap.md) [heap](structk__heap.md#a4b8551f4fd1cd648c68f47ea2ebd682f);

[ 5570](structk__heap.md#abd30d236bd986e791ea7698583e45588) \_wait\_q\_t [wait\_q](structk__heap.md#abd30d236bd986e791ea7698583e45588);

[ 5571](structk__heap.md#a3bd15b8ad69a6ab76b5c4a297673e5ec) struct [k\_spinlock](structk__spinlock.md) [lock](structk__heap.md#a3bd15b8ad69a6ab76b5c4a297673e5ec);

5572};

5573

[ 5587](group__heap__apis.md#ga9273e06dc8d6a351499f2f5abfdcb39f)void [k\_heap\_init](group__heap__apis.md#ga9273e06dc8d6a351499f2f5abfdcb39f)(struct [k\_heap](structk__heap.md) \*h, void \*mem,

5588 size\_t bytes) \_\_attribute\_nonnull(1);

5589

[ 5610](group__heap__apis.md#gaf77211a72441de389857bc13e10be4e6)void \*[k\_heap\_aligned\_alloc](group__heap__apis.md#gaf77211a72441de389857bc13e10be4e6)(struct [k\_heap](structk__heap.md) \*h, size\_t align, size\_t bytes,

5611 [k\_timeout\_t](structk__timeout__t.md) timeout) \_\_attribute\_nonnull(1);

5612

[ 5634](group__heap__apis.md#ga22b83564e50ae6177388dfe63e32a512)void \*[k\_heap\_alloc](group__heap__apis.md#ga22b83564e50ae6177388dfe63e32a512)(struct [k\_heap](structk__heap.md) \*h, size\_t bytes,

5635 [k\_timeout\_t](structk__timeout__t.md) timeout) \_\_attribute\_nonnull(1);

5636

[ 5659](group__heap__apis.md#ga53de68a83567cff1cff3eab5d8572449)void \*[k\_heap\_calloc](group__heap__apis.md#ga53de68a83567cff1cff3eab5d8572449)(struct [k\_heap](structk__heap.md) \*h, size\_t num, size\_t size, [k\_timeout\_t](structk__timeout__t.md) timeout)

5660 \_\_attribute\_nonnull(1);

5661

[ 5685](group__heap__apis.md#gabea4b2beae8ab138f2796fbeaa95d262)void \*[k\_heap\_realloc](group__heap__apis.md#gabea4b2beae8ab138f2796fbeaa95d262)(struct [k\_heap](structk__heap.md) \*h, void \*ptr, size\_t bytes, [k\_timeout\_t](structk__timeout__t.md) timeout)

5686 \_\_attribute\_nonnull(1);

5687

[ 5698](group__heap__apis.md#ga6cf917a0b3d91a0101192bd4808ada9c)void [k\_heap\_free](group__heap__apis.md#ga6cf917a0b3d91a0101192bd4808ada9c)(struct [k\_heap](structk__heap.md) \*h, void \*mem) \_\_attribute\_nonnull(1);

5699

5700/\* Hand-calculated minimum heap sizes needed to return a successful

5701 \* 1-byte allocation. See details in lib/os/heap.[ch]

5702 \*/

5703#define Z\_HEAP\_MIN\_SIZE ((sizeof(void \*) > 4) ? 56 : 44)

5704

5721#define Z\_HEAP\_DEFINE\_IN\_SECT(name, bytes, in\_section) \

5722 char in\_section \

5723 \_\_aligned(8) /\* CHUNK\_UNIT \*/ \

5724 kheap\_##name[MAX(bytes, Z\_HEAP\_MIN\_SIZE)]; \

5725 STRUCT\_SECTION\_ITERABLE(k\_heap, name) = { \

5726 .heap = { \

5727 .init\_mem = kheap\_##name, \

5728 .init\_bytes = MAX(bytes, Z\_HEAP\_MIN\_SIZE), \

5729 }, \

5730 }

5731

[ 5746](group__heap__apis.md#ga795d7f1e6d5b7b19a7a50198d7829a0f)#define K\_HEAP\_DEFINE(name, bytes) \

5747 Z\_HEAP\_DEFINE\_IN\_SECT(name, bytes, \

5748 \_\_noinit\_named(kheap\_buf\_##name))

5749

[ 5764](group__heap__apis.md#ga968f4c6a201fdf6862d62dd5d9f8d032)#define K\_HEAP\_DEFINE\_NOCACHE(name, bytes) \

5765 Z\_HEAP\_DEFINE\_IN\_SECT(name, bytes, \_\_nocache)

5766

5770

5776

[ 5795](group__heap__apis.md#gae16d486aa250f9c07fa6a57342bcd3b4)void \*[k\_aligned\_alloc](group__heap__apis.md#gae16d486aa250f9c07fa6a57342bcd3b4)(size\_t align, size\_t size);

5796

[ 5808](group__heap__apis.md#gaa8edf1e63e5d5dd78d7adcfd787394ee)void \*[k\_malloc](group__heap__apis.md#gaa8edf1e63e5d5dd78d7adcfd787394ee)(size\_t size);

5809

[ 5820](group__heap__apis.md#ga79b63cc93b3358cf82d74f40e73b69d5)void [k\_free](group__heap__apis.md#ga79b63cc93b3358cf82d74f40e73b69d5)(void \*ptr);

5821

[ 5833](group__heap__apis.md#gad031d50ed62d08202a5dcf992c20246c)void \*[k\_calloc](group__heap__apis.md#gad031d50ed62d08202a5dcf992c20246c)(size\_t nmemb, size\_t size);

5834

[ 5852](group__heap__apis.md#ga852a7a60dce5853b6925897b24a54e02)void \*[k\_realloc](group__heap__apis.md#ga852a7a60dce5853b6925897b24a54e02)(void \*ptr, size\_t size);

5853

5855

5856/\* polling API - PRIVATE \*/

5857

5858#ifdef CONFIG\_POLL

5859#define \_INIT\_OBJ\_POLL\_EVENT(obj) do { (obj)->poll\_event = NULL; } while (false)

5860#else

5861#define \_INIT\_OBJ\_POLL\_EVENT(obj) do { } while (false)

5862#endif

5863

5864/\* private - types bit positions \*/

5865enum \_poll\_types\_bits {

5866 /\* can be used to ignore an event \*/

5867 \_POLL\_TYPE\_IGNORE,

5868

5869 /\* to be signaled by k\_poll\_signal\_raise() \*/

5870 \_POLL\_TYPE\_SIGNAL,

5871

5872 /\* semaphore availability \*/

5873 \_POLL\_TYPE\_SEM\_AVAILABLE,

5874

5875 /\* queue/FIFO/LIFO data availability \*/

5876 \_POLL\_TYPE\_DATA\_AVAILABLE,

5877

5878 /\* msgq data availability \*/

5879 \_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE,

5880

5881 /\* pipe data availability \*/

5882 \_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE,

5883

5884 \_POLL\_NUM\_TYPES

5885};

5886

5887#define Z\_POLL\_TYPE\_BIT(type) (1U << ((type) - 1U))

5888

5889/\* private - states bit positions \*/

5890enum \_poll\_states\_bits {

5891 /\* default state when creating event \*/

5892 \_POLL\_STATE\_NOT\_READY,

5893

5894 /\* signaled by k\_poll\_signal\_raise() \*/

5895 \_POLL\_STATE\_SIGNALED,

5896

5897 /\* semaphore is available \*/

5898 \_POLL\_STATE\_SEM\_AVAILABLE,

5899

5900 /\* data is available to read on queue/FIFO/LIFO \*/

5901 \_POLL\_STATE\_DATA\_AVAILABLE,

5902

5903 /\* queue/FIFO/LIFO wait was cancelled \*/

5904 \_POLL\_STATE\_CANCELLED,

5905

5906 /\* data is available to read on a message queue \*/

5907 \_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE,

5908

5909 /\* data is available to read from a pipe \*/

5910 \_POLL\_STATE\_PIPE\_DATA\_AVAILABLE,

5911

5912 \_POLL\_NUM\_STATES

5913};

5914

5915#define Z\_POLL\_STATE\_BIT(state) (1U << ((state) - 1U))

5916

5917#define \_POLL\_EVENT\_NUM\_UNUSED\_BITS \

5918 (32 - (0 \

5919 + 8 /\* tag \*/ \

5920 + \_POLL\_NUM\_TYPES \

5921 + \_POLL\_NUM\_STATES \

5922 + 1 /\* modes \*/ \

5923 ))

5924

5925/\* end of polling API - PRIVATE \*/

5926

5927

5933

5934/\* Public polling API \*/

5935

5936/\* public - values for k\_poll\_event.type bitfield \*/

[ 5937](group__poll__apis.md#gafd5d801eb9e9cf6097b2c08b4933998e)#define K\_POLL\_TYPE\_IGNORE 0

[ 5938](group__poll__apis.md#ga144d8eb34d85f6053e454410a10bf56a)#define K\_POLL\_TYPE\_SIGNAL Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_SIGNAL)

[ 5939](group__poll__apis.md#ga0fd7605bdffd43dff7480a90a603ffde)#define K\_POLL\_TYPE\_SEM\_AVAILABLE Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_SEM\_AVAILABLE)

[ 5940](group__poll__apis.md#ga58d656f73f031a39b8a936133fe5504f)#define K\_POLL\_TYPE\_DATA\_AVAILABLE Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_DATA\_AVAILABLE)

[ 5941](group__poll__apis.md#ga71734fee18c523cf70276260118afb91)#define K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE K\_POLL\_TYPE\_DATA\_AVAILABLE

[ 5942](group__poll__apis.md#gaa83509b54175fb6c98324422a928d5e1)#define K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE)

[ 5943](group__poll__apis.md#ga14e113201a3b3ad768c6a5ce917d1912)#define K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE)

5944

5945/\* public - polling modes \*/

[ 5946](group__poll__apis.md#ga36d7978872a83191dd3cc16d62165add)enum [k\_poll\_modes](group__poll__apis.md#ga36d7978872a83191dd3cc16d62165add) {

5947 /\* polling thread does not take ownership of objects when available \*/

[ 5948](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda22874743e2f6b0f1fd55c5375732b681) [K\_POLL\_MODE\_NOTIFY\_ONLY](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda22874743e2f6b0f1fd55c5375732b681) = 0,

5949

[ 5950](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c) [K\_POLL\_NUM\_MODES](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c)

5951};

5952

5953/\* public - values for k\_poll\_event.state bitfield \*/

[ 5954](group__poll__apis.md#ga522822c5e06a89b22ce4dcefd10c66aa)#define K\_POLL\_STATE\_NOT\_READY 0

[ 5955](group__poll__apis.md#ga478aae7fe4fb5c7b7c76ed216c22a7f1)#define K\_POLL\_STATE\_SIGNALED Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_SIGNALED)

[ 5956](group__poll__apis.md#gae9e3eefd5a29a538d22f53592578bb37)#define K\_POLL\_STATE\_SEM\_AVAILABLE Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_SEM\_AVAILABLE)

[ 5957](group__poll__apis.md#gac166d9919d591bace163c5211e7b41f4)#define K\_POLL\_STATE\_DATA\_AVAILABLE Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_DATA\_AVAILABLE)

[ 5958](group__poll__apis.md#gabd5ac3341698534f39ded718079d6168)#define K\_POLL\_STATE\_FIFO\_DATA\_AVAILABLE K\_POLL\_STATE\_DATA\_AVAILABLE

[ 5959](group__poll__apis.md#gac236074cd43f59f28b803fe2c4a4f6f7)#define K\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE)

[ 5960](group__poll__apis.md#ga9028d6868ee964ca25931ed9170068dd)#define K\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE)

[ 5961](group__poll__apis.md#gadaf4b4c8e13afb54114af72d133e1fdb)#define K\_POLL\_STATE\_CANCELLED Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_CANCELLED)

5962

5963/\* public - poll signal object \*/

[ 5964](structk__poll__signal.md)struct [k\_poll\_signal](structk__poll__signal.md) {

[ 5966](structk__poll__signal.md#a22e88955ba0e369d39edefadcf4c60fd) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [poll\_events](structk__poll__signal.md#a22e88955ba0e369d39edefadcf4c60fd);

5967

[ 5972](structk__poll__signal.md#ae9fe6751d75f7d2b2800cb723603c0fe) unsigned int [signaled](structk__poll__signal.md#ae9fe6751d75f7d2b2800cb723603c0fe);

5973

[ 5975](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1) int [result](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1);

5976};

5977

[ 5978](group__poll__apis.md#ga6d6321e189afca73a276cd671ec531ae)#define K\_POLL\_SIGNAL\_INITIALIZER(obj) \

5979 { \

5980 .poll\_events = SYS\_DLIST\_STATIC\_INIT(&obj.poll\_events), \

5981 .signaled = 0, \

5982 .result = 0, \

5983 }

5984

[ 5988](structk__poll__event.md)struct [k\_poll\_event](structk__poll__event.md) {

5990 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \_node;

5991

[ 5993](structk__poll__event.md#ad030c37b97f33e1bbb3361057180fa4f) struct z\_poller \*[poller](structk__poll__event.md#ad030c37b97f33e1bbb3361057180fa4f);

5994

[ 5996](structk__poll__event.md#a37c5f45deaa046b356d95af569220c70) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tag](structk__poll__event.md#a37c5f45deaa046b356d95af569220c70):8;

5997

[ 5999](structk__poll__event.md#a8f9e251aa8722eb4716f622e85be34ae) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [type](structk__poll__event.md#a8f9e251aa8722eb4716f622e85be34ae):\_POLL\_NUM\_TYPES;

6000

[ 6002](structk__poll__event.md#aaf4f32852d799a406bfeea4e57891129) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](structk__poll__event.md#aaf4f32852d799a406bfeea4e57891129):\_POLL\_NUM\_STATES;

6003

[ 6005](structk__poll__event.md#acca81763486ef5ebcc911cb1cbd6c899) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mode](structk__poll__event.md#acca81763486ef5ebcc911cb1cbd6c899):1;

6006

[ 6008](structk__poll__event.md#a750ac48e7aa3c8fb70814b24e951fc85) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unused](structk__poll__event.md#a750ac48e7aa3c8fb70814b24e951fc85):\_POLL\_EVENT\_NUM\_UNUSED\_BITS;

6009

6011 union {

6012 /\* The typed\_\* fields below are used by K\_POLL\_EVENT\_\*INITIALIZER() macros to ensure

6013 \* type safety of polled objects.

6014 \*/

[ 6015](structk__poll__event.md#aeaf67f9bc91d59fb2939e1469a088f2d) void \*[obj](structk__poll__event.md#aeaf67f9bc91d59fb2939e1469a088f2d), \*[typed\_K\_POLL\_TYPE\_IGNORE](structk__poll__event.md#a0864cb03742d24d4638d5fbcb1166c5b);

[ 6016](structk__poll__event.md#a130aaff7a8908993ed6be737a94a52ab) struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](structk__poll__event.md#a130aaff7a8908993ed6be737a94a52ab), \*[typed\_K\_POLL\_TYPE\_SIGNAL](structk__poll__event.md#ad54cb4ae8d3603db02af37c833a73430);

[ 6017](structk__poll__event.md#a9ed342b8a45884f985245f55b0e1c8cc) struct k\_sem \*[sem](structk__poll__event.md#a9ed342b8a45884f985245f55b0e1c8cc), \*[typed\_K\_POLL\_TYPE\_SEM\_AVAILABLE](structk__poll__event.md#aaa57f5741e3e3a133cf8331cd68750f3);

[ 6018](structk__poll__event.md#a4ba07f42f4af03f30478ebf48a1653f7) struct [k\_fifo](structk__fifo.md) \*[fifo](structk__poll__event.md#a4ba07f42f4af03f30478ebf48a1653f7), \*[typed\_K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE](structk__poll__event.md#af578a9a6cd21412619d1482a17acb1ec);

[ 6019](structk__poll__event.md#a6e30a6ce30702817895e66f22f0abedf) struct [k\_queue](structk__queue.md) \*[queue](structk__poll__event.md#a6e30a6ce30702817895e66f22f0abedf), \*[typed\_K\_POLL\_TYPE\_DATA\_AVAILABLE](structk__poll__event.md#aa19a70be95e65636da3ebe6104a21dec);

[ 6020](structk__poll__event.md#a5bbe94482a70ec13c2106f89afd2d59c) struct [k\_msgq](structk__msgq.md) \*[msgq](structk__poll__event.md#a5bbe94482a70ec13c2106f89afd2d59c), \*[typed\_K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE](structk__poll__event.md#a038392f2f0fd314837005dc7fb57a714);

[ 6021](structk__poll__event.md#a1640577da6460fa1f3c9b5507bb66c18) struct [k\_pipe](structk__pipe.md) \*[pipe](structk__poll__event.md#a1640577da6460fa1f3c9b5507bb66c18), \*[typed\_K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE](structk__poll__event.md#a7dd3857bbeaf15392fc4d4cad7263340);

6022 };

6023};

6024

[ 6025](group__poll__apis.md#ga8e3889f2bac281a6e65e31068e58047e)#define K\_POLL\_EVENT\_INITIALIZER(\_event\_type, \_event\_mode, \_event\_obj) \

6026 { \

6027 .poller = NULL, \

6028 .type = \_event\_type, \

6029 .state = K\_POLL\_STATE\_NOT\_READY, \

6030 .mode = \_event\_mode, \

6031 .unused = 0, \

6032 { \

6033 .typed\_##\_event\_type = \_event\_obj, \

6034 }, \

6035 }

6036

[ 6037](group__poll__apis.md#gada2366896d913dc916b3c28642648b63)#define K\_POLL\_EVENT\_STATIC\_INITIALIZER(\_event\_type, \_event\_mode, \_event\_obj, \

6038 event\_tag) \

6039 { \

6040 .tag = event\_tag, \

6041 .type = \_event\_type, \

6042 .state = K\_POLL\_STATE\_NOT\_READY, \

6043 .mode = \_event\_mode, \

6044 .unused = 0, \

6045 { \

6046 .typed\_##\_event\_type = \_event\_obj, \

6047 }, \

6048 }

6049

6064

[ 6065](group__poll__apis.md#gaa06bddd93a024fc5326d93187d80eb03)void [k\_poll\_event\_init](group__poll__apis.md#gaa06bddd93a024fc5326d93187d80eb03)(struct [k\_poll\_event](structk__poll__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type,

6066 int mode, void \*obj);

6067

6110

[ 6111](group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db)\_\_syscall int [k\_poll](group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db)(struct [k\_poll\_event](structk__poll__event.md) \*events, int num\_events,

6112 [k\_timeout\_t](structk__timeout__t.md) timeout);

6113

6121

[ 6122](group__poll__apis.md#gaee3090c2a912b93b6a5855e3018c3551)\_\_syscall void [k\_poll\_signal\_init](group__poll__apis.md#gaee3090c2a912b93b6a5855e3018c3551)(struct [k\_poll\_signal](structk__poll__signal.md) \*sig);

6123

[ 6129](group__poll__apis.md#ga02d899d1455ae1f3f55ffe8f1ebd6994)\_\_syscall void [k\_poll\_signal\_reset](group__poll__apis.md#ga02d899d1455ae1f3f55ffe8f1ebd6994)(struct [k\_poll\_signal](structk__poll__signal.md) \*sig);

6130

[ 6141](group__poll__apis.md#ga69dae11c7cb2c669caa411c3e7001311)\_\_syscall void [k\_poll\_signal\_check](group__poll__apis.md#ga69dae11c7cb2c669caa411c3e7001311)(struct [k\_poll\_signal](structk__poll__signal.md) \*sig,

6142 unsigned int \*signaled, int \*result);

6143

6167

[ 6168](group__poll__apis.md#gad0bf3825f828ec3ca37481bf3cbd6723)\_\_syscall int [k\_poll\_signal\_raise](group__poll__apis.md#gad0bf3825f828ec3ca37481bf3cbd6723)(struct [k\_poll\_signal](structk__poll__signal.md) \*sig, int result);

6169

6171

[ 6190](group__cpu__idle__apis.md#ga7b25e1bed511a813b32fbd0f91b09356)static inline void [k\_cpu\_idle](group__cpu__idle__apis.md#ga7b25e1bed511a813b32fbd0f91b09356)(void)

6191{

6192 [arch\_cpu\_idle](group__arch-pm.md#ga6ce051203e6cc091d0fb42a15f662a48)();

6193}

6194

[ 6209](group__cpu__idle__apis.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f)static inline void [k\_cpu\_atomic\_idle](group__cpu__idle__apis.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f)(unsigned int key)

6210{

6211 [arch\_cpu\_atomic\_idle](group__arch-pm.md#ga4d0297717c23a3cc5df434549e26924d)(key);

6212}

6213

6217

6222#ifdef ARCH\_EXCEPT

6223/\* This architecture has direct support for triggering a CPU exception \*/

6224#define z\_except\_reason(reason) ARCH\_EXCEPT(reason)

6225#else

6226

6227#if !defined(CONFIG\_ASSERT\_NO\_FILE\_INFO)

6228#define \_\_EXCEPT\_LOC() \_\_ASSERT\_PRINT("@ %s:%d\n", \_\_FILE\_\_, \_\_LINE\_\_)

6229#else

6230#define \_\_EXCEPT\_LOC()

6231#endif

6232

6233/\* NOTE: This is the implementation for arches that do not implement

6234 \* ARCH\_EXCEPT() to generate a real CPU exception.

6235 \*

6236 \* We won't have a real exception frame to determine the PC value when

6237 \* the oops occurred, so print file and line number before we jump into

6238 \* the fatal error handler.

6239 \*/

6240#define z\_except\_reason(reason) do { \

6241 \_\_EXCEPT\_LOC(); \

6242 z\_fatal\_error(reason, NULL); \

6243 } while (false)

6244

6245#endif /\* \_ARCH\_\_EXCEPT \*/

6249

[ 6261](kernel_8h.md#abde5aa8ca5e64a045b25b88f91370dcd)#define k\_oops() z\_except\_reason(K\_ERR\_KERNEL\_OOPS)

6262

[ 6271](kernel_8h.md#aedd541f707b1463aaac15c7798340329)#define k\_panic() z\_except\_reason(K\_ERR\_KERNEL\_PANIC)

6272

6276

6277/\*

6278 \* private APIs that are utilized by one or more public APIs

6279 \*/

6280

6284void z\_timer\_expiration\_handler(struct \_timeout \*timeout);

6288

6289#ifdef CONFIG\_PRINTK

6297\_\_syscall void k\_str\_out(char \*c, size\_t n);

6298#endif

6299

6305

[ 6326](group__float__apis.md#ga2df4b2550ace30512cddebd36b6a54a1)\_\_syscall int [k\_float\_disable](group__float__apis.md#ga2df4b2550ace30512cddebd36b6a54a1)(struct [k\_thread](structk__thread.md) \*thread);

6327

[ 6366](group__float__apis.md#ga81fb955ddd41658a9aad5c083f173f77)\_\_syscall int [k\_float\_enable](group__float__apis.md#ga81fb955ddd41658a9aad5c083f173f77)(struct [k\_thread](structk__thread.md) \*thread, unsigned int options);

6367

6371

[ 6379](kernel_8h.md#a82d886a1c911b39c1b47c32200cedac6)int [k\_thread\_runtime\_stats\_get](kernel_8h.md#a82d886a1c911b39c1b47c32200cedac6)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread,

6380 [k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) \*stats);

6381

[ 6388](kernel_8h.md#abd855bb83b3be393b46833e7854a193e)int [k\_thread\_runtime\_stats\_all\_get](kernel_8h.md#abd855bb83b3be393b46833e7854a193e)([k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) \*stats);

6389

[ 6397](kernel_8h.md#aefdd9027a50143262a7482c17873f169)int [k\_thread\_runtime\_stats\_cpu\_get](kernel_8h.md#aefdd9027a50143262a7482c17873f169)(int cpu, [k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) \*stats);

6398

[ 6408](kernel_8h.md#a3e52beb93fca2231d5860fe1cf1181fd)int [k\_thread\_runtime\_stats\_enable](kernel_8h.md#a3e52beb93fca2231d5860fe1cf1181fd)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

6409

[ 6419](kernel_8h.md#ae5ea2e05a602b7d5ee78a65ced61d63b)int [k\_thread\_runtime\_stats\_disable](kernel_8h.md#ae5ea2e05a602b7d5ee78a65ced61d63b)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

6420

[ 6428](kernel_8h.md#a54f2652ba1ed613219941eaaf193180c)void [k\_sys\_runtime\_stats\_enable](kernel_8h.md#a54f2652ba1ed613219941eaaf193180c)(void);

6429

[ 6437](kernel_8h.md#a2e3c96c0b11108ee7eca3f0666c780e0)void [k\_sys\_runtime\_stats\_disable](kernel_8h.md#a2e3c96c0b11108ee7eca3f0666c780e0)(void);

6438

6439#ifdef \_\_cplusplus

6440}

6441#endif

6442

6443#include <[zephyr/tracing/tracing.h](tracing_8h.md)>

6444#include <zephyr/syscalls/kernel.h>

6445

6446#endif /\* !\_ASMLANGUAGE \*/

6447

6448#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_H\_ \*/

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

**Definition** kernel.h:1927

[K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)

#define K\_NO\_WAIT

Generate null timeout delay.

**Definition** kernel.h:1357

[k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)

int64\_t k\_uptime\_ticks(void)

Get system uptime, in system ticks.

[k\_uptime\_get\_32](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b)

static uint32\_t k\_uptime\_get\_32(void)

Get system uptime (32-bit version).

**Definition** kernel.h:1879

[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2)

uint32\_t k\_ticks\_t

Tick precision used in timeout APIs.

**Definition** sys\_clock.h:48

[k\_uptime\_delta](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80)

static int64\_t k\_uptime\_delta(int64\_t \*reftime)

Get elapsed time.

**Definition** kernel.h:1908

[k\_uptime\_seconds](group__clock__apis.md#gae082928ea608a8b180b4cb3a79d21a24)

static uint32\_t k\_uptime\_seconds(void)

Get system uptime in seconds.

**Definition** kernel.h:1892

[k\_cycle\_get\_64](group__clock__apis.md#gae09f509d02bf75a7b45d2800d823bb3a)

static uint64\_t k\_cycle\_get\_64(void)

Read the 64-bit hardware clock.

**Definition** kernel.h:1942

[k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)

static int64\_t k\_uptime\_get(void)

Get system uptime.

**Definition** kernel.h:1855

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

**Definition** kernel.h:6190

[k\_cpu\_atomic\_idle](group__cpu__idle__apis.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f)

static void k\_cpu\_atomic\_idle(unsigned int key)

Make the CPU idle in an atomic fashion.

**Definition** kernel.h:6209

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

**Definition** kernel.h:2475

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

[sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66)

struct \_sflist sys\_sflist\_t

Flagged single-linked list structure.

**Definition** sflist.h:54

[sys\_sflist\_is\_empty](group__flagged-single-linked-list__apis.md#gac506235a9df89a7a52631e9990ceaad5)

static bool sys\_sflist\_is\_empty(sys\_sflist\_t \*list)

Test if the given list is empty.

**Definition** sflist.h:336

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

**Definition** kernel.h:1212

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

**Definition** kernel.h:5492

[k\_mem\_slab\_max\_used\_get](group__mem__slab__apis.md#gae0e949c1c3476dd57bc0c0ed627d2346)

static uint32\_t k\_mem\_slab\_max\_used\_get(struct k\_mem\_slab \*slab)

Get the number of maximum used blocks so far in a memory slab.

**Definition** kernel.h:5507

[k\_mem\_slab\_num\_free\_get](group__mem__slab__apis.md#gae87577e2873cf746db69216a82f94aea)

static uint32\_t k\_mem\_slab\_num\_free\_get(struct k\_mem\_slab \*slab)

Get the number of unused blocks in a memory slab.

**Definition** kernel.h:5527

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

**Definition** kernel.h:5206

[k\_pipe\_read](group__pipe__apis.md#gaecb07412025d9e065ee7b99121522257)

int k\_pipe\_read(struct k\_pipe \*pipe, uint8\_t \*data, size\_t len, k\_timeout\_t timeout)

Read data from a pipe This routine reads up to len bytes of data from pipe.

[PIPE\_FLAG\_RESET](group__pipe__apis.md#ggae5471546043f4d14e97c3f6313053ee0a37642c400a675e1dce34c9b878874df4)

@ PIPE\_FLAG\_RESET

**Definition** kernel.h:5208

[PIPE\_FLAG\_OPEN](group__pipe__apis.md#ggae5471546043f4d14e97c3f6313053ee0a9fc19eac7b41c00ca97c2fb0a30a2309)

@ PIPE\_FLAG\_OPEN

**Definition** kernel.h:5207

[k\_poll\_signal\_reset](group__poll__apis.md#ga02d899d1455ae1f3f55ffe8f1ebd6994)

void k\_poll\_signal\_reset(struct k\_poll\_signal \*sig)

Reset a poll signal object's state to unsignaled.

[k\_poll\_modes](group__poll__apis.md#ga36d7978872a83191dd3cc16d62165add)

k\_poll\_modes

**Definition** kernel.h:5946

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

**Definition** kernel.h:5948

[K\_POLL\_NUM\_MODES](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c)

@ K\_POLL\_NUM\_MODES

**Definition** kernel.h:5950

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

**Definition** util.h:284

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

**Definition** kernel.h:472

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

**Definition** kernel.h:565

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

**Definition** kernel.h:662

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

**Definition** kernel.h:1089

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

**Definition** kernel.h:1633

[k\_timer\_remaining\_ticks](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4)

k\_ticks\_t k\_timer\_remaining\_ticks(const struct k\_timer \*timer)

Get time remaining before a timer next expires, in system ticks.

[k\_timer\_user\_data\_get](group__timer__apis.md#ga19a7d99a01a83828efd7f0d3bf2dd358)

void \* k\_timer\_user\_data\_get(const struct k\_timer \*timer)

Retrieve the user-specific data from a timer.

[k\_timer\_expiry\_t](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde)

void(\* k\_timer\_expiry\_t)(struct k\_timer \*timer)

Timer expiry function type.

**Definition** kernel.h:1617

[k\_timer\_init](group__timer__apis.md#ga318c846a740b901e5d56876a47ad7f61)

void k\_timer\_init(struct k\_timer \*timer, k\_timer\_expiry\_t expiry\_fn, k\_timer\_stop\_t stop\_fn)

Initialize a timer.

[k\_timer\_start](group__timer__apis.md#ga3ba70e9f059ff52fd2057ab89ea7f2ee)

void k\_timer\_start(struct k\_timer \*timer, k\_timeout\_t duration, k\_timeout\_t period)

Start a timer.

[k\_timer\_remaining\_get](group__timer__apis.md#ga6c6d8b0aa59bfa0f5924e95ccf756259)

static uint32\_t k\_timer\_remaining\_get(struct k\_timer \*timer)

Get time remaining before a timer next expires.

**Definition** kernel.h:1779

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

**Definition** kernel.h:4210

[k\_work\_is\_pending](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)

static bool k\_work\_is\_pending(const struct k\_work \*work)

Test whether a work item is currently pending.

**Definition** kernel.h:4181

[k\_work\_queue\_drain](group__workqueue__apis.md#ga0fefe3e0225ac99b47b250849f6cd863)

int k\_work\_queue\_drain(struct k\_work\_q \*queue, bool plug)

Wait until the work queue has drained, optionally plugging it.

[k\_work\_delayable\_expires\_get](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624)

static k\_ticks\_t k\_work\_delayable\_expires\_get(const struct k\_work\_delayable \*dwork)

Get the absolute tick count at which a scheduled delayable work will be submitted.

**Definition** kernel.h:4198

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

**Definition** kernel.h:4337

[k\_work\_submit\_to\_queue](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c)

int k\_work\_submit\_to\_queue(struct k\_work\_q \*queue, struct k\_work \*work)

Submit a work item to a queue.

[k\_work\_user\_is\_pending](group__workqueue__apis.md#ga58d05d4127e4cd51104a1f1a87f626cd)

static bool k\_work\_user\_is\_pending(struct k\_work\_user \*work)

Check if a userspace work item is pending.

**Definition** kernel.h:4314

[k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda)

void(\* k\_work\_handler\_t)(struct k\_work \*work)

The signature for a work item handler function.

**Definition** kernel.h:3387

[k\_work\_schedule](group__workqueue__apis.md#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)

int k\_work\_schedule(struct k\_work\_delayable \*dwork, k\_timeout\_t delay)

Submit an idle work item to the system work queue after a delay.

[k\_work\_delayable\_is\_pending](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e)

static bool k\_work\_delayable\_is\_pending(const struct k\_work\_delayable \*dwork)

Test whether a delayed work item is currently pending.

**Definition** kernel.h:4192

[k\_work\_cancel\_delayable\_sync](group__workqueue__apis.md#ga7e7ec237648556fc16bfda8d35f7cd86)

bool k\_work\_cancel\_delayable\_sync(struct k\_work\_delayable \*dwork, struct k\_work\_sync \*sync)

Cancel delayable work and wait.

[k\_work\_cancel\_delayable](group__workqueue__apis.md#ga92355914ee178d4c3e848a1946bed3e4)

int k\_work\_cancel\_delayable(struct k\_work\_delayable \*dwork)

Cancel delayable work.

[k\_work\_user\_init](group__workqueue__apis.md#ga9de9c7a7f13cc6b325e5453e34afe62d)

static void k\_work\_user\_init(struct k\_work\_user \*work, k\_work\_user\_handler\_t handler)

Initialize a userspace work item.

**Definition** kernel.h:4292

[k\_work\_queue\_unplug](group__workqueue__apis.md#gaa0463bb79af3ec470f7d3be02052139f)

int k\_work\_queue\_unplug(struct k\_work\_q \*queue)

Release a work queue to accept new submissions.

[k\_work\_reschedule](group__workqueue__apis.md#gaacaab408fb7c848d466ad1f069dfa648)

int k\_work\_reschedule(struct k\_work\_delayable \*dwork, k\_timeout\_t delay)

Reschedule a work item to the system work queue after a delay.

[k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc)

void(\* k\_work\_user\_handler\_t)(struct k\_work\_user \*work)

Work item handler function type for user work queues.

**Definition** kernel.h:4233

[k\_work\_cancel\_sync](group__workqueue__apis.md#gab2b05cfe3af08f7d32c3946fa1c808f9)

bool k\_work\_cancel\_sync(struct k\_work \*work, struct k\_work\_sync \*sync)

Cancel a work item and wait for it to complete.

[k\_work\_user\_queue\_thread\_get](group__workqueue__apis.md#gab487068e9564cd77b6bdbac3d5670923)

static k\_tid\_t k\_work\_user\_queue\_thread\_get(struct k\_work\_user\_q \*work\_q)

Access the user mode thread that animates a work queue.

**Definition** kernel.h:4392

[k\_work\_busy\_get](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b)

int k\_work\_busy\_get(const struct k\_work \*work)

Busy state flags from the work item.

[k\_work\_delayable\_from\_work](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca)

static struct k\_work\_delayable \* k\_work\_delayable\_from\_work(struct k\_work \*work)

Get the parent delayable work structure from a work pointer.

**Definition** kernel.h:4187

[k\_work\_delayable\_remaining\_get](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4)

static k\_ticks\_t k\_work\_delayable\_remaining\_get(const struct k\_work\_delayable \*dwork)

Get the number of ticks until a scheduled delayable work will be submitted.

**Definition** kernel.h:4204

[k\_work\_flush](group__workqueue__apis.md#gabd1cda459bab538fb2d6dfd84a73b253)

bool k\_work\_flush(struct k\_work \*work, struct k\_work\_sync \*sync)

Wait for last-submitted instance to complete.

[k\_work\_reschedule\_for\_queue](group__workqueue__apis.md#gabf5db091eac19b19a4e12c0cb381f0a8)

int k\_work\_reschedule\_for\_queue(struct k\_work\_q \*queue, struct k\_work\_delayable \*dwork, k\_timeout\_t delay)

Reschedule a work item to a queue after a delay.

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

**Definition** kernel.h:3982

[K\_WORK\_QUEUED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85)

@ K\_WORK\_QUEUED

Flag indicating a work item that has been submitted to a queue but has not started running.

**Definition** kernel.h:3989

[K\_WORK\_DELAYED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed)

@ K\_WORK\_DELAYED

Flag indicating a delayed work item that is scheduled for submission to a queue.

**Definition** kernel.h:3996

[K\_WORK\_RUNNING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165)

@ K\_WORK\_RUNNING

Flag indicating a work item that is running under a work queue thread.

**Definition** kernel.h:3976

[K\_WORK\_FLUSHING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601)

@ K\_WORK\_FLUSHING

Flag indicating a synced work item that is being flushed.

**Definition** kernel.h:4002

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:380

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

**Definition** kernel\_structs.h:322

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

**Definition** kernel.h:3137

[k\_condvar::wait\_q](structk__condvar.md#a14b457a06420f093e779d569f4fea906)

\_wait\_q\_t wait\_q

**Definition** kernel.h:3138

[k\_event](structk__event.md)

Event Structure.

**Definition** kernel.h:2328

[k\_event::lock](structk__event.md#a1f0de9c69f29ad854f3b0d510ceb1efc)

struct k\_spinlock lock

**Definition** kernel.h:2331

[k\_event::events](structk__event.md#a54c6f5997132e88406ffa5bcc0a10b83)

uint32\_t events

**Definition** kernel.h:2330

[k\_event::wait\_q](structk__event.md#a5bacd5f2d34da646d9d7ee229842e432)

\_wait\_q\_t wait\_q

**Definition** kernel.h:2329

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2495

[k\_futex](structk__futex.md)

futex structure

**Definition** kernel.h:2249

[k\_futex::val](structk__futex.md#a454ad1b595b899306c8e9c8e1431e7a7)

atomic\_t val

**Definition** kernel.h:2250

[k\_heap](structk__heap.md)

**Definition** kernel.h:5568

[k\_heap::lock](structk__heap.md#a3bd15b8ad69a6ab76b5c4a297673e5ec)

struct k\_spinlock lock

**Definition** kernel.h:5571

[k\_heap::heap](structk__heap.md#a4b8551f4fd1cd648c68f47ea2ebd682f)

struct sys\_heap heap

**Definition** kernel.h:5569

[k\_heap::wait\_q](structk__heap.md#abd30d236bd986e791ea7698583e45588)

\_wait\_q\_t wait\_q

**Definition** kernel.h:5570

[k\_lifo](structk__lifo.md)

**Definition** kernel.h:2736

[k\_mbox\_msg](structk__mbox__msg.md)

Mailbox Message Structure.

**Definition** kernel.h:4843

[k\_mbox\_msg::tx\_target\_thread](structk__mbox__msg.md#a73236acb7d27bb0233f5abb7214fb19c)

k\_tid\_t tx\_target\_thread

target thread id

**Definition** kernel.h:4853

[k\_mbox\_msg::tx\_data](structk__mbox__msg.md#a74b0edeed4c44cb5932eb292efc9d9c2)

void \* tx\_data

sender's message data buffer

**Definition** kernel.h:4849

[k\_mbox\_msg::rx\_source\_thread](structk__mbox__msg.md#a9eb145a242ac66e80d90286d83fe7a61)

k\_tid\_t rx\_source\_thread

source thread id

**Definition** kernel.h:4851

[k\_mbox\_msg::info](structk__mbox__msg.md#aa79f2bf71431b474ec4551ade4d7a8dd)

uint32\_t info

application-defined information value

**Definition** kernel.h:4847

[k\_mbox\_msg::size](structk__mbox__msg.md#aeabf45e9599a64852a1cfd656b1ece8e)

size\_t size

size of message (in bytes)

**Definition** kernel.h:4845

[k\_mbox](structk__mbox.md)

Mailbox Structure.

**Definition** kernel.h:4865

[k\_mbox::tx\_msg\_queue](structk__mbox.md#a0bca912a50120707ddafa66d740ade96)

\_wait\_q\_t tx\_msg\_queue

Transmit messages queue.

**Definition** kernel.h:4867

[k\_mbox::lock](structk__mbox.md#a2c549d5bd7216b62d81ad2198e0d79e4)

struct k\_spinlock lock

**Definition** kernel.h:4870

[k\_mbox::rx\_msg\_queue](structk__mbox.md#a808a14c31892a2d042cdb0723a2956e2)

\_wait\_q\_t rx\_msg\_queue

Receive message queue.

**Definition** kernel.h:4869

[k\_mem\_domain](structk__mem__domain.md)

Memory Domain.

**Definition** mem\_domain.h:80

[k\_mem\_partition](structk__mem__partition.md)

Memory Partition.

**Definition** mem\_domain.h:55

[k\_msgq\_attrs](structk__msgq__attrs.md)

Message Queue Attributes.

**Definition** kernel.h:4611

[k\_msgq\_attrs::used\_msgs](structk__msgq__attrs.md#a00f936870442fa455117cbdd7821fac5)

uint32\_t used\_msgs

Used messages.

**Definition** kernel.h:4617

[k\_msgq\_attrs::msg\_size](structk__msgq__attrs.md#a7d1d72946bdd517c07da37493a89e30e)

size\_t msg\_size

Message Size.

**Definition** kernel.h:4613

[k\_msgq\_attrs::max\_msgs](structk__msgq__attrs.md#ad0f5894ba0da840b91eb85015252e649)

uint32\_t max\_msgs

Maximal number of messages.

**Definition** kernel.h:4615

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4552

[k\_msgq::msg\_size](structk__msgq.md#a512fe468da96540639a0d71f1707f79d)

size\_t msg\_size

Message size.

**Definition** kernel.h:4558

[k\_msgq::read\_ptr](structk__msgq.md#a594e8a4a638521f42f24f85fe0742d64)

char \* read\_ptr

Read pointer.

**Definition** kernel.h:4566

[k\_msgq::used\_msgs](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857)

uint32\_t used\_msgs

Number of used messages.

**Definition** kernel.h:4570

[k\_msgq::buffer\_end](structk__msgq.md#a9d47fd25d7a70e8518d45dd48c51f0e0)

char \* buffer\_end

End of message buffer.

**Definition** kernel.h:4564

[k\_msgq::lock](structk__msgq.md#aa2e00a7292502f0de88cff28c5e375f0)

struct k\_spinlock lock

Lock.

**Definition** kernel.h:4556

[k\_msgq::write\_ptr](structk__msgq.md#aacf9b7b9f6e26e402f3752fc56834f23)

char \* write\_ptr

Write pointer.

**Definition** kernel.h:4568

[k\_msgq::buffer\_start](structk__msgq.md#aca77f1cf833d3aa27ae65004b446bdd2)

char \* buffer\_start

Start of message buffer.

**Definition** kernel.h:4562

[k\_msgq::flags](structk__msgq.md#ae03025420908f8342ce12a1395c7657b)

uint8\_t flags

Message queue.

**Definition** kernel.h:4575

[k\_msgq::wait\_q](structk__msgq.md#ae3b3d53d60b789d69c65494cfd090076)

\_wait\_q\_t wait\_q

Message queue wait queue.

**Definition** kernel.h:4554

[k\_msgq::max\_msgs](structk__msgq.md#aebd3b6e91e97b2d4369feea1a3f7b7a0)

uint32\_t max\_msgs

Maximal number of messages.

**Definition** kernel.h:4560

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

[k\_mutex::lock\_count](structk__mutex.md#a0db401fc8e03e1f984b8fd15af974718)

uint32\_t lock\_count

Current lock count.

**Definition** kernel.h:3032

[k\_mutex::wait\_q](structk__mutex.md#a4add234295bceff22551ee74f3aed802)

\_wait\_q\_t wait\_q

Mutex wait queue.

**Definition** kernel.h:3027

[k\_mutex::owner\_orig\_prio](structk__mutex.md#ab0d16fac9f8af960a501ffd93ec08c80)

int owner\_orig\_prio

Original thread priority.

**Definition** kernel.h:3035

[k\_mutex::owner](structk__mutex.md#af910bb07dc99e50078de26fccca468e4)

struct k\_thread \* owner

Mutex owner.

**Definition** kernel.h:3029

[k\_obj\_core](structk__obj__core.md)

Object core structure.

**Definition** obj\_core.h:121

[k\_pipe](structk__pipe.md)

**Definition** kernel.h:5211

[k\_pipe::flags](structk__pipe.md#a2ed95fbe24ea20c4f292a66def1d4dde)

uint8\_t flags

**Definition** kernel.h:5217

[k\_pipe::buf](structk__pipe.md#a62556b1fbb907dcb8fbbe29c597d8473)

struct ring\_buf buf

**Definition** kernel.h:5213

[k\_pipe::data](structk__pipe.md#a8af11082e53b56670f0ce11e581766ff)

\_wait\_q\_t data

**Definition** kernel.h:5215

[k\_pipe::space](structk__pipe.md#aa1428192b88b97e0cb5ec83894770f47)

\_wait\_q\_t space

**Definition** kernel.h:5216

[k\_pipe::lock](structk__pipe.md#aa2a367a9c8f0be89bcdf1bf6d3b0b875)

struct k\_spinlock lock

**Definition** kernel.h:5214

[k\_pipe::waiting](structk__pipe.md#ac9162db42883d2c14f63cf74ff3c1179)

size\_t waiting

**Definition** kernel.h:5212

[k\_poll\_event](structk__poll__event.md)

Poll Event.

**Definition** kernel.h:5988

[k\_poll\_event::typed\_K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE](structk__poll__event.md#a038392f2f0fd314837005dc7fb57a714)

struct k\_msgq \* typed\_K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE

**Definition** kernel.h:6020

[k\_poll\_event::typed\_K\_POLL\_TYPE\_IGNORE](structk__poll__event.md#a0864cb03742d24d4638d5fbcb1166c5b)

void \* typed\_K\_POLL\_TYPE\_IGNORE

**Definition** kernel.h:6015

[k\_poll\_event::signal](structk__poll__event.md#a130aaff7a8908993ed6be737a94a52ab)

struct k\_poll\_signal \* signal

**Definition** kernel.h:6016

[k\_poll\_event::pipe](structk__poll__event.md#a1640577da6460fa1f3c9b5507bb66c18)

struct k\_pipe \* pipe

**Definition** kernel.h:6021

[k\_poll\_event::tag](structk__poll__event.md#a37c5f45deaa046b356d95af569220c70)

uint32\_t tag

optional user-specified tag, opaque, untouched by the API

**Definition** kernel.h:5996

[k\_poll\_event::fifo](structk__poll__event.md#a4ba07f42f4af03f30478ebf48a1653f7)

struct k\_fifo \* fifo

**Definition** kernel.h:6018

[k\_poll\_event::msgq](structk__poll__event.md#a5bbe94482a70ec13c2106f89afd2d59c)

struct k\_msgq \* msgq

**Definition** kernel.h:6020

[k\_poll\_event::queue](structk__poll__event.md#a6e30a6ce30702817895e66f22f0abedf)

struct k\_queue \* queue

**Definition** kernel.h:6019

[k\_poll\_event::unused](structk__poll__event.md#a750ac48e7aa3c8fb70814b24e951fc85)

uint32\_t unused

unused bits in 32-bit word

**Definition** kernel.h:6008

[k\_poll\_event::typed\_K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE](structk__poll__event.md#a7dd3857bbeaf15392fc4d4cad7263340)

struct k\_pipe \* typed\_K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE

**Definition** kernel.h:6021

[k\_poll\_event::type](structk__poll__event.md#a8f9e251aa8722eb4716f622e85be34ae)

uint32\_t type

bitfield of event types (bitwise-ORed K\_POLL\_TYPE\_xxx values)

**Definition** kernel.h:5999

[k\_poll\_event::sem](structk__poll__event.md#a9ed342b8a45884f985245f55b0e1c8cc)

struct k\_sem \* sem

**Definition** kernel.h:6017

[k\_poll\_event::typed\_K\_POLL\_TYPE\_DATA\_AVAILABLE](structk__poll__event.md#aa19a70be95e65636da3ebe6104a21dec)

struct k\_queue \* typed\_K\_POLL\_TYPE\_DATA\_AVAILABLE

**Definition** kernel.h:6019

[k\_poll\_event::typed\_K\_POLL\_TYPE\_SEM\_AVAILABLE](structk__poll__event.md#aaa57f5741e3e3a133cf8331cd68750f3)

struct k\_sem \* typed\_K\_POLL\_TYPE\_SEM\_AVAILABLE

**Definition** kernel.h:6017

[k\_poll\_event::state](structk__poll__event.md#aaf4f32852d799a406bfeea4e57891129)

uint32\_t state

bitfield of event states (bitwise-ORed K\_POLL\_STATE\_xxx values)

**Definition** kernel.h:6002

[k\_poll\_event::mode](structk__poll__event.md#acca81763486ef5ebcc911cb1cbd6c899)

uint32\_t mode

mode of operation, from enum k\_poll\_modes

**Definition** kernel.h:6005

[k\_poll\_event::poller](structk__poll__event.md#ad030c37b97f33e1bbb3361057180fa4f)

struct z\_poller \* poller

PRIVATE - DO NOT TOUCH.

**Definition** kernel.h:5993

[k\_poll\_event::typed\_K\_POLL\_TYPE\_SIGNAL](structk__poll__event.md#ad54cb4ae8d3603db02af37c833a73430)

struct k\_poll\_signal \* typed\_K\_POLL\_TYPE\_SIGNAL

**Definition** kernel.h:6016

[k\_poll\_event::obj](structk__poll__event.md#aeaf67f9bc91d59fb2939e1469a088f2d)

void \* obj

**Definition** kernel.h:6015

[k\_poll\_event::typed\_K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE](structk__poll__event.md#af578a9a6cd21412619d1482a17acb1ec)

struct k\_fifo \* typed\_K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE

**Definition** kernel.h:6018

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5964

[k\_poll\_signal::poll\_events](structk__poll__signal.md#a22e88955ba0e369d39edefadcf4c60fd)

sys\_dlist\_t poll\_events

PRIVATE - DO NOT TOUCH.

**Definition** kernel.h:5966

[k\_poll\_signal::result](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1)

int result

custom result value passed to k\_poll\_signal\_raise() if needed

**Definition** kernel.h:5975

[k\_poll\_signal::signaled](structk__poll__signal.md#ae9fe6751d75f7d2b2800cb723603c0fe)

unsigned int signaled

1 if the event has been signaled, 0 otherwise.

**Definition** kernel.h:5972

[k\_queue](structk__queue.md)

**Definition** kernel.h:1957

[k\_queue::lock](structk__queue.md#a18fd165fec722384b3748bfdf3332a4c)

struct k\_spinlock lock

**Definition** kernel.h:1959

[k\_queue::wait\_q](structk__queue.md#a871d734f2b21a9cad3ca4a2ba79e64f1)

\_wait\_q\_t wait\_q

**Definition** kernel.h:1960

[k\_queue::data\_q](structk__queue.md#a892371af9701ce67619e38446bc2ceae)

sys\_sflist\_t data\_q

**Definition** kernel.h:1958

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[k\_thread::base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8)

struct \_thread\_base base

**Definition** thread.h:261

[k\_thread::resource\_pool](structk__thread.md#a35b859bded3a270f25ccc40efece7583)

struct k\_heap \* resource\_pool

resource pool

**Definition** thread.h:349

[k\_thread::entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03)

struct \_\_thread\_entry entry

thread entry and parameters description

**Definition** thread.h:288

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4034

[k\_work\_delayable::timeout](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d)

struct \_timeout timeout

**Definition** kernel.h:4039

[k\_work\_delayable::queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4)

struct k\_work\_q \* queue

**Definition** kernel.h:4042

[k\_work\_delayable::work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629)

struct k\_work work

**Definition** kernel.h:4036

[k\_work\_q](structk__work__q.md)

A structure used to hold work until it can be processed.

**Definition** kernel.h:4158

[k\_work\_q::pending](structk__work__q.md#a2012199571f6b658873550d64386b00c)

sys\_slist\_t pending

**Definition** kernel.h:4167

[k\_work\_q::drainq](structk__work__q.md#a308d1ac78b1203b7ea78b0f18c5bdf5b)

\_wait\_q\_t drainq

**Definition** kernel.h:4173

[k\_work\_q::notifyq](structk__work__q.md#a561c90f8bb944217230e00052cdecf10)

\_wait\_q\_t notifyq

**Definition** kernel.h:4170

[k\_work\_q::flags](structk__work__q.md#a68bc8e9c412ebdbf34827087d91a080e)

uint32\_t flags

**Definition** kernel.h:4176

[k\_work\_q::thread](structk__work__q.md#aa42ca271a4989f129bf1a43c491327eb)

struct k\_thread thread

**Definition** kernel.h:4160

[k\_work\_queue\_config](structk__work__queue__config.md)

A structure holding optional configuration items for a work queue.

**Definition** kernel.h:4130

[k\_work\_queue\_config::name](structk__work__queue__config.md#a0929d83372efff6798bc69bb7ca1eaaa)

const char \* name

The name to be given to the work queue thread.

**Definition** kernel.h:4135

[k\_work\_queue\_config::essential](structk__work__queue__config.md#a5aa4a80d91ef36498443c163428b02c0)

bool essential

Control whether the work queue thread should be marked as essential thread.

**Definition** kernel.h:4154

[k\_work\_queue\_config::no\_yield](structk__work__queue__config.md#afcf64d6e69d1ddfff8cbd749dafa4d13)

bool no\_yield

Control whether the work queue thread should yield between items.

**Definition** kernel.h:4149

[k\_work\_sync](structk__work__sync.md)

A structure holding internal state for a pending synchronous operation on a work item or queue.

**Definition** kernel.h:4117

[k\_work\_sync::canceller](structk__work__sync.md#a7e8fd0b9d6736c403aefa8462c7c0835)

struct z\_work\_canceller canceller

**Definition** kernel.h:4120

[k\_work\_sync::flusher](structk__work__sync.md#ad81ff57cb9f2f3dc5f2d65917cf04f1c)

struct z\_work\_flusher flusher

**Definition** kernel.h:4119

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:4006

[k\_work::handler](structk__work.md#a096d6ca1338fb0fbfa330b790136f172)

k\_work\_handler\_t handler

**Definition** kernel.h:4015

[k\_work::flags](structk__work.md#a391ed7d2039cd05c9894267bf8ea4dfd)

uint32\_t flags

**Definition** kernel.h:4026

[k\_work::queue](structk__work.md#a551be8394e041020c36a97dc2e12e137)

struct k\_work\_q \* queue

**Definition** kernel.h:4018

[k\_work::node](structk__work.md#a85772682983e0fdeb735f0821d5710d4)

sys\_snode\_t node

**Definition** kernel.h:4012

[ring\_buf](structring__buf.md)

A structure to represent a ring buffer.

**Definition** ring\_buffer.h:43

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
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
