---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/include_2zephyr_2kernel_8h_source.html
original_path: doxygen/html/include_2zephyr_2kernel_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kernel.h

[Go to the documentation of this file.](include_2zephyr_2kernel_8h.md)

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

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

30/\*

31 \* Zephyr currently assumes the size of a couple standard types to simplify

32 \* print string formats. Let's make sure this doesn't change without notice.

33 \*/

34BUILD\_ASSERT(sizeof([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)) == sizeof(int));

35BUILD\_ASSERT(sizeof([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)) == sizeof(long long));

36BUILD\_ASSERT(sizeof([intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c)) == sizeof(long));

37

44

[ 45](include_2zephyr_2kernel_8h.md#ac627cc4c3da16be4b74f0a4ab036a603)#define K\_ANY NULL

46

47#if CONFIG\_NUM\_COOP\_PRIORITIES + CONFIG\_NUM\_PREEMPT\_PRIORITIES == 0

48#error Zero available thread priorities defined!

49#endif

50

[ 51](include_2zephyr_2kernel_8h.md#ac145d4747518572acfc8ee1579007d54)#define K\_PRIO\_COOP(x) (-(CONFIG\_NUM\_COOP\_PRIORITIES - (x)))

[ 52](include_2zephyr_2kernel_8h.md#aa0e916aae3ddd0e998cd41ac32afe30a)#define K\_PRIO\_PREEMPT(x) (x)

53

[ 54](include_2zephyr_2kernel_8h.md#a5fd4365cb6e8742e750b5e4950fb1e47)#define K\_HIGHEST\_THREAD\_PRIO (-CONFIG\_NUM\_COOP\_PRIORITIES)

[ 55](include_2zephyr_2kernel_8h.md#afa4bcc2fdfea5cd7c63d56f476b1b32f)#define K\_LOWEST\_THREAD\_PRIO CONFIG\_NUM\_PREEMPT\_PRIORITIES

[ 56](include_2zephyr_2kernel_8h.md#a8f3f1d910dd847f0b223a4aa00788fa2)#define K\_IDLE\_PRIO K\_LOWEST\_THREAD\_PRIO

[ 57](include_2zephyr_2kernel_8h.md#ab326c7eb1d248650e6017dcaee8d24b2)#define K\_HIGHEST\_APPLICATION\_THREAD\_PRIO (K\_HIGHEST\_THREAD\_PRIO)

[ 58](include_2zephyr_2kernel_8h.md#ad4c2df561988fa1194c2f8c768d667cd)#define K\_LOWEST\_APPLICATION\_THREAD\_PRIO (K\_LOWEST\_THREAD\_PRIO - 1)

59

60#ifdef CONFIG\_POLL

61#define Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

62 .poll\_events = SYS\_DLIST\_STATIC\_INIT(&obj.poll\_events),

63#define Z\_DECL\_POLL\_EVENT sys\_dlist\_t poll\_events;

64#else

65#define Z\_POLL\_EVENT\_OBJ\_INIT(obj)

66#define Z\_DECL\_POLL\_EVENT

67#endif

68

69struct [k\_thread](structk__thread.md);

70struct [k\_mutex](structk__mutex.md);

71struct k\_sem;

72struct [k\_msgq](structk__msgq.md);

73struct [k\_mbox](structk__mbox.md);

74struct [k\_pipe](structk__pipe.md);

75struct [k\_queue](structk__queue.md);

76struct [k\_fifo](structk__fifo.md);

77struct [k\_lifo](structk__lifo.md);

78struct k\_stack;

79struct k\_mem\_slab;

80struct k\_timer;

81struct [k\_poll\_event](structk__poll__event.md);

82struct [k\_poll\_signal](structk__poll__signal.md);

83struct [k\_mem\_domain](structk__mem__domain.md);

84struct [k\_mem\_partition](structk__mem__partition.md);

85struct [k\_futex](structk__futex.md);

86struct [k\_event](structk__event.md);

87

[ 88](include_2zephyr_2kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779c)enum [execution\_context\_types](include_2zephyr_2kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779c) {

[ 89](include_2zephyr_2kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779ca30593044743695f8184a157283dac4d5) [K\_ISR](include_2zephyr_2kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779ca30593044743695f8184a157283dac4d5) = 0,

[ 90](include_2zephyr_2kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779ca62c0b731a1bb3c5e4aadeba3f93df58b) [K\_COOP\_THREAD](include_2zephyr_2kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779ca62c0b731a1bb3c5e4aadeba3f93df58b),

[ 91](include_2zephyr_2kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779cae84f57f4ac996c751d1f4c9e49789322) [K\_PREEMPT\_THREAD](include_2zephyr_2kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779cae84f57f4ac996c751d1f4c9e49789322),

92};

93

94/\* private, used by k\_poll and k\_work\_poll \*/

95struct k\_work\_poll;

96typedef int (\*\_poller\_cb\_t)(struct [k\_poll\_event](structk__poll__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

97

102

[ 103](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75)typedef void (\*[k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75))(const struct [k\_thread](structk__thread.md) \*thread,

104 void \*user\_data);

105

[ 121](group__thread__apis.md#gae2596d56800769b06fc03c194a126a97)void [k\_thread\_foreach](group__thread__apis.md#gae2596d56800769b06fc03c194a126a97)([k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data);

122

[ 150](group__thread__apis.md#ga30ef8b445a6c1b4a82651674dbb737fc)void [k\_thread\_foreach\_unlocked](group__thread__apis.md#ga30ef8b445a6c1b4a82651674dbb737fc)(

151 [k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data);

152

154

160

161#endif /\* !\_ASMLANGUAGE \*/

162

163

164/\*

165 \* Thread user options. May be needed by assembly code. Common part uses low

166 \* bits, arch-specific use high bits.

167 \*/

168

[ 172](group__thread__apis.md#gad503fbcca905a9266b0e154e3ded258c)#define K\_ESSENTIAL (BIT(0))

173

[ 183](group__thread__apis.md#ga4b2378312ea9b410be025b40e8d6a395)#define K\_FP\_IDX 1

[ 184](group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951)#define K\_FP\_REGS (BIT(K\_FP\_IDX))

185

[ 192](group__thread__apis.md#gacb5340339892f22301e02697c6039ccc)#define K\_USER (BIT(2))

193

[ 202](group__thread__apis.md#gaa1788a413a055745d1de71b4da7c2eb2)#define K\_INHERIT\_PERMS (BIT(3))

203

[ 213](group__thread__apis.md#gacbdb579370978fe07e4a863a84bd8bee)#define K\_CALLBACK\_STATE (BIT(4))

214

[ 224](group__thread__apis.md#gacbd163e5bc79fc0282def5ff4321fa30)#define K\_DSP\_IDX 6

[ 225](group__thread__apis.md#ga8e1aeb428a418ed23e17448b796363cb)#define K\_DSP\_REGS (BIT(K\_DSP\_IDX))

226

[ 235](group__thread__apis.md#gab01cfd20675ebef8f5e81d7d17e6babb)#define K\_AGU\_IDX 7

[ 236](group__thread__apis.md#ga718088c1a68f03fffa960164cab60b72)#define K\_AGU\_REGS (BIT(K\_AGU\_IDX))

237

[ 247](group__thread__apis.md#gaa5b7de51b26773aa4485a711a041d9a7)#define K\_SSE\_REGS (BIT(7))

248

249/\* end - thread options \*/

250

251#if !defined(\_ASMLANGUAGE)

[ 266](group__thread__apis.md#gafe00cc70bac8a47ba6dda21bde508614)\_\_syscall [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[k\_thread\_stack\_alloc](group__thread__apis.md#gafe00cc70bac8a47ba6dda21bde508614)(size\_t size, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

267

[ 280](group__thread__apis.md#ga95560cb85f6656b981a9a50ff2cd70b7)\_\_syscall int [k\_thread\_stack\_free](group__thread__apis.md#ga95560cb85f6656b981a9a50ff2cd70b7)([k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack);

281

[ 330](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367)\_\_syscall [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_thread\_create](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367)(struct [k\_thread](structk__thread.md) \*new\_thread,

331 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack,

332 size\_t stack\_size,

333 [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) [entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03),

334 void \*p1, void \*p2, void \*p3,

335 int prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) options, [k\_timeout\_t](structk__timeout__t.md) delay);

336

[ 358](group__thread__apis.md#ga3fbe1c8a5f3ef1c25382c7d6fca35764)FUNC\_NORETURN void [k\_thread\_user\_mode\_enter](group__thread__apis.md#ga3fbe1c8a5f3ef1c25382c7d6fca35764)([k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) [entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03),

359 void \*p1, void \*p2,

360 void \*p3);

361

[ 375](group__thread__apis.md#gafec540511e6d2e0a074a5bfb515c53b0)#define k\_thread\_access\_grant(thread, ...) \

376 FOR\_EACH\_FIXED\_ARG(k\_object\_access\_grant, (;), thread, \_\_VA\_ARGS\_\_)

377

[ 392](group__thread__apis.md#ga3f46c06833add2a2e0ddb7242f06702c)static inline void [k\_thread\_heap\_assign](group__thread__apis.md#ga3f46c06833add2a2e0ddb7242f06702c)(struct [k\_thread](structk__thread.md) \*thread,

393 struct [k\_heap](structk__heap.md) \*heap)

394{

395 thread->[resource\_pool](structk__thread.md#a35b859bded3a270f25ccc40efece7583) = heap;

396}

397

398#if defined(CONFIG\_INIT\_STACKS) && defined(CONFIG\_THREAD\_STACK\_INFO)

419\_\_syscall int k\_thread\_stack\_space\_get(const struct [k\_thread](structk__thread.md) \*thread,

420 size\_t \*unused\_ptr);

421#endif

422

423#if (K\_HEAP\_MEM\_POOL\_SIZE > 0)

436void k\_thread\_system\_pool\_assign(struct [k\_thread](structk__thread.md) \*thread);

437#endif /\* (K\_HEAP\_MEM\_POOL\_SIZE > 0) \*/

438

[ 458](group__thread__apis.md#ga40a733561eb1f64dcaae0e01b167d233)\_\_syscall int [k\_thread\_join](group__thread__apis.md#ga40a733561eb1f64dcaae0e01b167d233)(struct [k\_thread](structk__thread.md) \*thread, [k\_timeout\_t](structk__timeout__t.md) timeout);

459

[ 474](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)([k\_timeout\_t](structk__timeout__t.md) timeout);

475

[ 487](group__thread__apis.md#ga51307cdfe153ab3e918b18755d97c5d9)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_msleep](group__thread__apis.md#ga51307cdfe153ab3e918b18755d97c5d9)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ms)

488{

489 return [k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)(Z\_TIMEOUT\_MS(ms));

490}

491

[ 508](group__thread__apis.md#gaeac56bb072ce295b9fdc372ab8cee67e)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_usleep](group__thread__apis.md#gaeac56bb072ce295b9fdc372ab8cee67e)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) us);

509

[ 526](group__thread__apis.md#ga550b642e071480323e589866abb99c22)\_\_syscall void [k\_busy\_wait](group__thread__apis.md#ga550b642e071480323e589866abb99c22)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usec\_to\_wait);

527

[ 539](group__thread__apis.md#ga366b9daa0be65b0a69dbc9f146064b68)bool [k\_can\_yield](group__thread__apis.md#ga366b9daa0be65b0a69dbc9f146064b68)(void);

540

[ 548](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)\_\_syscall void [k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)(void);

549

[ 559](group__thread__apis.md#ga9275a019c8ff3c7fe49a81f8c078157e)\_\_syscall void [k\_wakeup](group__thread__apis.md#ga9275a019c8ff3c7fe49a81f8c078157e)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

560

574\_\_attribute\_const\_\_

[ 575](group__thread__apis.md#gac3b994b90b5bccded0895304f6b20c5d)\_\_syscall [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_sched\_current\_thread\_query](group__thread__apis.md#gac3b994b90b5bccded0895304f6b20c5d)(void);

576

583\_\_attribute\_const\_\_

[ 584](group__thread__apis.md#ga7ef1ed0fb9513df8096ede1e52fc76b2)static inline [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_current\_get](group__thread__apis.md#ga7ef1ed0fb9513df8096ede1e52fc76b2)(void)

585{

586#ifdef CONFIG\_CURRENT\_THREAD\_USE\_TLS

587

588 /\* Thread-local cache of current thread ID, set in z\_thread\_entry() \*/

589 extern \_\_thread [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) z\_tls\_current;

590

591 return z\_tls\_current;

592#else

593 return [k\_sched\_current\_thread\_query](group__thread__apis.md#gac3b994b90b5bccded0895304f6b20c5d)();

594#endif

595}

596

[ 616](group__thread__apis.md#ga1f44bb0307bea7a97227764ecd7bf963)\_\_syscall void [k\_thread\_abort](group__thread__apis.md#ga1f44bb0307bea7a97227764ecd7bf963)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

617

618

[ 628](group__thread__apis.md#ga88031bd9fcfcd4305bae4029a4d8416f)\_\_syscall void [k\_thread\_start](group__thread__apis.md#ga88031bd9fcfcd4305bae4029a4d8416f)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

629

630[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_timeout\_expires(const struct \_timeout \*timeout);

631[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_timeout\_remaining(const struct \_timeout \*timeout);

632

633#ifdef CONFIG\_SYS\_CLOCK\_EXISTS

634

[ 642](group__thread__apis.md#ga80013f10d12ccdffbbd88cee048f1c21)\_\_syscall [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_thread\_timeout\_expires\_ticks](group__thread__apis.md#ga80013f10d12ccdffbbd88cee048f1c21)(const struct [k\_thread](structk__thread.md) \*t);

643

644static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_impl\_k\_thread\_timeout\_expires\_ticks(

645 const struct [k\_thread](structk__thread.md) \*t)

646{

647 return z\_timeout\_expires(&t->[base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8).timeout);

648}

649

[ 657](group__thread__apis.md#ga4cb4126c8e4f62bd44f3dd03f2e4a423)\_\_syscall [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_thread\_timeout\_remaining\_ticks](group__thread__apis.md#ga4cb4126c8e4f62bd44f3dd03f2e4a423)(const struct [k\_thread](structk__thread.md) \*t);

658

659static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_impl\_k\_thread\_timeout\_remaining\_ticks(

660 const struct [k\_thread](structk__thread.md) \*t)

661{

662 return z\_timeout\_remaining(&t->[base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8).timeout);

663}

664

665#endif /\* CONFIG\_SYS\_CLOCK\_EXISTS \*/

666

670

671struct \_static\_thread\_data {

672 struct k\_thread \*init\_thread;

673 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*init\_stack;

674 unsigned int init\_stack\_size;

675 [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) init\_entry;

676 void \*init\_p1;

677 void \*init\_p2;

678 void \*init\_p3;

679 int init\_prio;

680 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) init\_options;

681 const char \*init\_name;

682#ifdef CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME

683 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) init\_delay\_ms;

684#else

685 k\_timeout\_t init\_delay;

686#endif

687};

688

689#ifdef CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME

690#define Z\_THREAD\_INIT\_DELAY\_INITIALIZER(ms) .init\_delay\_ms = (ms)

691#define Z\_THREAD\_INIT\_DELAY(thread) SYS\_TIMEOUT\_MS((thread)->init\_delay\_ms)

692#else

693#define Z\_THREAD\_INIT\_DELAY\_INITIALIZER(ms) .init\_delay = SYS\_TIMEOUT\_MS(ms)

694#define Z\_THREAD\_INIT\_DELAY(thread) (thread)->init\_delay

695#endif

696

697#define Z\_THREAD\_INITIALIZER(thread, stack, stack\_size, \

698 entry, p1, p2, p3, \

699 prio, options, delay, tname) \

700 { \

701 .init\_thread = (thread), \

702 .init\_stack = (stack), \

703 .init\_stack\_size = (stack\_size), \

704 .init\_entry = (k\_thread\_entry\_t)entry, \

705 .init\_p1 = (void \*)p1, \

706 .init\_p2 = (void \*)p2, \

707 .init\_p3 = (void \*)p3, \

708 .init\_prio = (prio), \

709 .init\_options = (options), \

710 .init\_name = STRINGIFY(tname), \

711 Z\_THREAD\_INIT\_DELAY\_INITIALIZER(delay) \

712 }

713

714/\*

715 \* Refer to K\_THREAD\_DEFINE() and K\_KERNEL\_THREAD\_DEFINE() for

716 \* information on arguments.

717 \*/

718#define Z\_THREAD\_COMMON\_DEFINE(name, stack\_size, \

719 entry, p1, p2, p3, \

720 prio, options, delay) \

721 struct k\_thread \_k\_thread\_obj\_##name; \

722 STRUCT\_SECTION\_ITERABLE(\_static\_thread\_data, \

723 \_k\_thread\_data\_##name) = \

724 Z\_THREAD\_INITIALIZER(&\_k\_thread\_obj\_##name, \

725 \_k\_thread\_stack\_##name, stack\_size,\

726 entry, p1, p2, p3, prio, options, \

727 delay, name); \

728 const k\_tid\_t name = (k\_tid\_t)&\_k\_thread\_obj\_##name

729

733

[ 765](group__thread__apis.md#gab3ced58648ca35788a40676e8478ecd2)#define K\_THREAD\_DEFINE(name, stack\_size, \

766 entry, p1, p2, p3, \

767 prio, options, delay) \

768 K\_THREAD\_STACK\_DEFINE(\_k\_thread\_stack\_##name, stack\_size); \

769 Z\_THREAD\_COMMON\_DEFINE(name, stack\_size, entry, p1, p2, p3, \

770 prio, options, delay)

771

[ 802](group__thread__apis.md#gae25853424ec969f8431862c46b3ec294)#define K\_KERNEL\_THREAD\_DEFINE(name, stack\_size, \

803 entry, p1, p2, p3, \

804 prio, options, delay) \

805 K\_KERNEL\_STACK\_DEFINE(\_k\_thread\_stack\_##name, stack\_size); \

806 Z\_THREAD\_COMMON\_DEFINE(name, stack\_size, entry, p1, p2, p3, \

807 prio, options, delay)

808

[ 818](group__thread__apis.md#ga3a46ed8ad2c3b12416fafe11325f82b3)\_\_syscall int [k\_thread\_priority\_get](group__thread__apis.md#ga3a46ed8ad2c3b12416fafe11325f82b3)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

819

[ 845](group__thread__apis.md#ga24e50a60c524d1eb22fe21cdf269b6a6)\_\_syscall void [k\_thread\_priority\_set](group__thread__apis.md#ga24e50a60c524d1eb22fe21cdf269b6a6)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int prio);

846

847

848#ifdef CONFIG\_SCHED\_DEADLINE

[ 881](group__thread__apis.md#gad887f16c1dd6f3247682a83beb22d1ce)\_\_syscall void [k\_thread\_deadline\_set](group__thread__apis.md#gad887f16c1dd6f3247682a83beb22d1ce)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int deadline);

882#endif

883

884#ifdef CONFIG\_SCHED\_CPU\_MASK

[ 897](group__thread__apis.md#ga80b9c58df6600c7e79f16756c128f44c)int [k\_thread\_cpu\_mask\_clear](group__thread__apis.md#ga80b9c58df6600c7e79f16756c128f44c)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

898

[ 911](group__thread__apis.md#gaedcfeb0964ae72611791241580b2119d)int [k\_thread\_cpu\_mask\_enable\_all](group__thread__apis.md#gaedcfeb0964ae72611791241580b2119d)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

912

[ 925](group__thread__apis.md#ga306587604a7496db8059bd395fd90fc0)int [k\_thread\_cpu\_mask\_enable](group__thread__apis.md#ga306587604a7496db8059bd395fd90fc0)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu);

926

[ 939](group__thread__apis.md#ga89e6c07ac112da75b2ef115d1a557d44)int [k\_thread\_cpu\_mask\_disable](group__thread__apis.md#ga89e6c07ac112da75b2ef115d1a557d44)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu);

940

[ 951](group__thread__apis.md#gae9ebd9845e14ed02944ab9282a185c03)int [k\_thread\_cpu\_pin](group__thread__apis.md#gae9ebd9845e14ed02944ab9282a185c03)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu);

952#endif

953

[ 974](group__thread__apis.md#ga66cf8682fb65870eceb5e57d667a8d4e)\_\_syscall void [k\_thread\_suspend](group__thread__apis.md#ga66cf8682fb65870eceb5e57d667a8d4e)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

975

[ 986](group__thread__apis.md#ga117b26f8569ec3045ead1fad1851663d)\_\_syscall void [k\_thread\_resume](group__thread__apis.md#ga117b26f8569ec3045ead1fad1851663d)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

987

[ 1014](group__thread__apis.md#ga877c1bfeffbf8f097d1656f9e10a66e8)void [k\_sched\_time\_slice\_set](group__thread__apis.md#ga877c1bfeffbf8f097d1656f9e10a66e8)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) slice, int prio);

1015

[ 1054](group__thread__apis.md#ga563928f292a4134acd4142029b60e631)void [k\_thread\_time\_slice\_set](group__thread__apis.md#ga563928f292a4134acd4142029b60e631)(struct [k\_thread](structk__thread.md) \*th, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) slice\_ticks,

1055 [k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f) expired, void \*data);

1056

1058

1063

[ 1075](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)bool [k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)(void);

1076

[ 1093](group__isr__apis.md#ga91e1cf0dc7fc93a3214cadb74ed86666)\_\_syscall int [k\_is\_preempt\_thread](group__isr__apis.md#ga91e1cf0dc7fc93a3214cadb74ed86666)(void);

1094

[ 1106](group__isr__apis.md#gae74e5de996276df767b96d4b50fa47ea)static inline bool [k\_is\_pre\_kernel](group__isr__apis.md#gae74e5de996276df767b96d4b50fa47ea)(void)

1107{

1108 extern bool z\_sys\_post\_kernel; /\* in init.c \*/

1109

1110 return !z\_sys\_post\_kernel;

1111}

1112

1116

1121

[ 1147](group__thread__apis.md#ga4f0c5d0b9f279b12a4ad97db0c116a5f)void [k\_sched\_lock](group__thread__apis.md#ga4f0c5d0b9f279b12a4ad97db0c116a5f)(void);

1148

[ 1156](group__thread__apis.md#ga7b26f64523cc4c36522cc828ccf85580)void [k\_sched\_unlock](group__thread__apis.md#ga7b26f64523cc4c36522cc828ccf85580)(void);

1157

[ 1170](group__thread__apis.md#ga4834d9b81ed60c00eee77b0d4f8ab9e4)\_\_syscall void [k\_thread\_custom\_data\_set](group__thread__apis.md#ga4834d9b81ed60c00eee77b0d4f8ab9e4)(void \*value);

1171

[ 1179](group__thread__apis.md#ga19af063cff7b306ba28062996922740d)\_\_syscall void \*[k\_thread\_custom\_data\_get](group__thread__apis.md#ga19af063cff7b306ba28062996922740d)(void);

1180

[ 1194](group__thread__apis.md#ga23107333f134b9c9a8b692374211e841)\_\_syscall int [k\_thread\_name\_set](group__thread__apis.md#ga23107333f134b9c9a8b692374211e841)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, const char \*str);

1195

[ 1204](group__thread__apis.md#gadebf45da56dee393164569742459dc0a)const char \*[k\_thread\_name\_get](group__thread__apis.md#gadebf45da56dee393164569742459dc0a)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

1205

[ 1217](group__thread__apis.md#ga07b59ade055c69929ccdc08a14361794)\_\_syscall int [k\_thread\_name\_copy](group__thread__apis.md#ga07b59ade055c69929ccdc08a14361794)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, char \*buf,

1218 size\_t size);

1219

[ 1232](group__thread__apis.md#ga0c6af32096dc7ca391ffe2522bae4cb6)const char \*[k\_thread\_state\_str](group__thread__apis.md#ga0c6af32096dc7ca391ffe2522bae4cb6)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread\_id, char \*buf, size\_t buf\_size);

1233

1237

1242

[ 1251](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)#define K\_NO\_WAIT Z\_TIMEOUT\_NO\_WAIT

1252

[ 1265](group__clock__apis.md#gae2f3a80170afc5fbce0337cdf5a4ce4c)#define K\_NSEC(t) Z\_TIMEOUT\_NS(t)

1266

[ 1279](group__clock__apis.md#ga91198e325210ec052a8308e642058c0b)#define K\_USEC(t) Z\_TIMEOUT\_US(t)

1280

[ 1291](group__clock__apis.md#gab41f59fd2b724cb1279e4f6821154b33)#define K\_CYC(t) Z\_TIMEOUT\_CYC(t)

1292

[ 1303](group__clock__apis.md#gaeda983960bd25f1dba7a386ad720e395)#define K\_TICKS(t) Z\_TIMEOUT\_TICKS(t)

1304

[ 1315](group__clock__apis.md#ga302af954e87b10a9b731f1ad07775e9f)#define K\_MSEC(ms) Z\_TIMEOUT\_MS(ms)

1316

[ 1327](group__clock__apis.md#gadc361472aea59267f6ea38f5e7c7ca2a)#define K\_SECONDS(s) K\_MSEC((s) \* MSEC\_PER\_SEC)

1328

[ 1339](group__clock__apis.md#gaef02f20d4d2ebfc9aa29acae01bd3698)#define K\_MINUTES(m) K\_SECONDS((m) \* 60)

1340

[ 1351](group__clock__apis.md#gaa9e0cd890db28965b66d4bc5d719a91f)#define K\_HOURS(h) K\_MINUTES((h) \* 60)

1352

[ 1361](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)#define K\_FOREVER Z\_FOREVER

1362

1363#ifdef CONFIG\_TIMEOUT\_64BIT

1364

1376#define K\_TIMEOUT\_ABS\_TICKS(t) \

1377 Z\_TIMEOUT\_TICKS(Z\_TICK\_ABS((k\_ticks\_t)MAX(t, 0)))

1378

1390#define K\_TIMEOUT\_ABS\_MS(t) K\_TIMEOUT\_ABS\_TICKS(k\_ms\_to\_ticks\_ceil64(t))

1391

1404#define K\_TIMEOUT\_ABS\_US(t) K\_TIMEOUT\_ABS\_TICKS(k\_us\_to\_ticks\_ceil64(t))

1405

1418#define K\_TIMEOUT\_ABS\_NS(t) K\_TIMEOUT\_ABS\_TICKS(k\_ns\_to\_ticks\_ceil64(t))

1419

1432#define K\_TIMEOUT\_ABS\_CYC(t) K\_TIMEOUT\_ABS\_TICKS(k\_cyc\_to\_ticks\_ceil64(t))

1433

1434#endif

1435

1439

1443

1444struct k\_timer {

1445 /\*

1446 \* \_timeout structure must be first here if we want to use

1447 \* dynamic timer allocation. timeout.node is used in the double-linked

1448 \* list of free timers

1449 \*/

1450 struct \_timeout timeout;

1451

1452 /\* wait queue for the (single) thread waiting on this timer \*/

1453 \_wait\_q\_t wait\_q;

1454

1455 /\* runs in ISR context \*/

1456 void (\*expiry\_fn)(struct k\_timer \*timer);

1457

1458 /\* runs in the context of the thread that calls k\_timer\_stop() \*/

1459 void (\*stop\_fn)(struct k\_timer \*timer);

1460

1461 /\* timer period \*/

1462 [k\_timeout\_t](structk__timeout__t.md) period;

1463

1464 /\* timer status \*/

1465 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status;

1466

1467 /\* user-specific data, also used to support legacy features \*/

1468 void \*user\_data;

1469

1470 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_timer)

1471

1472#ifdef CONFIG\_OBJ\_CORE\_TIMER

1473 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

1474#endif

1475};

1476

1477#define Z\_TIMER\_INITIALIZER(obj, expiry, stop) \

1478 { \

1479 .timeout = { \

1480 .node = {},\

1481 .fn = z\_timer\_expiration\_handler, \

1482 .dticks = 0, \

1483 }, \

1484 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

1485 .expiry\_fn = expiry, \

1486 .stop\_fn = stop, \

1487 .status = 0, \

1488 .user\_data = 0, \

1489 }

1490

1494

1500

[ 1511](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde)typedef void (\*[k\_timer\_expiry\_t](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde))(struct k\_timer \*timer);

1512

[ 1527](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c)typedef void (\*[k\_timer\_stop\_t](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c))(struct k\_timer \*timer);

1528

[ 1540](group__timer__apis.md#gaa267fcb0a2e18cd0da29e9f9612510a6)#define K\_TIMER\_DEFINE(name, expiry\_fn, stop\_fn) \

1541 STRUCT\_SECTION\_ITERABLE(k\_timer, name) = \

1542 Z\_TIMER\_INITIALIZER(name, expiry\_fn, stop\_fn)

1543

[ 1553](group__timer__apis.md#ga318c846a740b901e5d56876a47ad7f61)void [k\_timer\_init](group__timer__apis.md#ga318c846a740b901e5d56876a47ad7f61)(struct k\_timer \*timer,

1554 [k\_timer\_expiry\_t](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde) expiry\_fn,

1555 [k\_timer\_stop\_t](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c) stop\_fn);

1556

[ 1571](group__timer__apis.md#ga3ba70e9f059ff52fd2057ab89ea7f2ee)\_\_syscall void [k\_timer\_start](group__timer__apis.md#ga3ba70e9f059ff52fd2057ab89ea7f2ee)(struct k\_timer \*timer,

1572 [k\_timeout\_t](structk__timeout__t.md) duration, [k\_timeout\_t](structk__timeout__t.md) period);

1573

[ 1590](group__timer__apis.md#ga8d3e3356a10d36570e16f7920e4c8772)\_\_syscall void [k\_timer\_stop](group__timer__apis.md#ga8d3e3356a10d36570e16f7920e4c8772)(struct k\_timer \*timer);

1591

[ 1604](group__timer__apis.md#gad532f4834cd4cf8be27b089e6ea347ce)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_timer\_status\_get](group__timer__apis.md#gad532f4834cd4cf8be27b089e6ea347ce)(struct k\_timer \*timer);

1605

[ 1623](group__timer__apis.md#ga81d6d95b7021e26ad4cab161318e04f2)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_timer\_status\_sync](group__timer__apis.md#ga81d6d95b7021e26ad4cab161318e04f2)(struct k\_timer \*timer);

1624

1625#ifdef CONFIG\_SYS\_CLOCK\_EXISTS

1626

[ 1637](group__timer__apis.md#ga022b4cf5c8d0ee21b6a3b04fd425533f)\_\_syscall [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_timer\_expires\_ticks](group__timer__apis.md#ga022b4cf5c8d0ee21b6a3b04fd425533f)(const struct k\_timer \*timer);

1638

1639static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_impl\_k\_timer\_expires\_ticks(

1640 const struct k\_timer \*timer)

1641{

1642 return z\_timeout\_expires(&timer->timeout);

1643}

1644

[ 1652](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4)\_\_syscall [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_timer\_remaining\_ticks](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4)(const struct k\_timer \*timer);

1653

1654static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) z\_impl\_k\_timer\_remaining\_ticks(

1655 const struct k\_timer \*timer)

1656{

1657 return z\_timeout\_remaining(&timer->timeout);

1658}

1659

[ 1670](group__timer__apis.md#ga6c6d8b0aa59bfa0f5924e95ccf756259)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_timer\_remaining\_get](group__timer__apis.md#ga6c6d8b0aa59bfa0f5924e95ccf756259)(struct k\_timer \*timer)

1671{

1672 return [k\_ticks\_to\_ms\_floor32](group__timeutil__unit__apis.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)([k\_timer\_remaining\_ticks](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4)(timer));

1673}

1674

1675#endif /\* CONFIG\_SYS\_CLOCK\_EXISTS \*/

1676

[ 1689](group__timer__apis.md#gadba1884961e790dd9c5d567de91cc7e2)\_\_syscall void [k\_timer\_user\_data\_set](group__timer__apis.md#gadba1884961e790dd9c5d567de91cc7e2)(struct k\_timer \*timer, void \*user\_data);

1690

1694static inline void z\_impl\_k\_timer\_user\_data\_set(struct k\_timer \*timer,

1695 void \*user\_data)

1696{

1697 timer->user\_data = user\_data;

1698}

1699

[ 1707](group__timer__apis.md#ga19a7d99a01a83828efd7f0d3bf2dd358)\_\_syscall void \*[k\_timer\_user\_data\_get](group__timer__apis.md#ga19a7d99a01a83828efd7f0d3bf2dd358)(const struct k\_timer \*timer);

1708

1709static inline void \*z\_impl\_k\_timer\_user\_data\_get(const struct k\_timer \*timer)

1710{

1711 return timer->user\_data;

1712}

1713

1715

1721

[ 1731](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)\_\_syscall [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)(void);

1732

[ 1746](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)(void)

1747{

1748 return [k\_ticks\_to\_ms\_floor64](group__timeutil__unit__apis.md#gac417ab53d5d493d95e24e7f777f8a4e0)([k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)());

1749}

1750

[ 1770](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_uptime\_get\_32](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b)(void)

1771{

1772 return ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)();

1773}

1774

[ 1786](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [k\_uptime\_delta](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80)([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*reftime)

1787{

1788 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) uptime, delta;

1789

1790 uptime = [k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)();

1791 delta = uptime - \*reftime;

1792 \*reftime = uptime;

1793

1794 return delta;

1795}

1796

[ 1805](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)(void)

1806{

1807 return [arch\_k\_cycle\_get\_32](group__arch-timing.md#ga9ee9f897ec750957de45bf8d43349d5e)();

1808}

1809

[ 1820](group__clock__apis.md#gae09f509d02bf75a7b45d2800d823bb3a)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [k\_cycle\_get\_64](group__clock__apis.md#gae09f509d02bf75a7b45d2800d823bb3a)(void)

1821{

1822 if (![IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_TIMER\_HAS\_64BIT\_CYCLE\_COUNTER)) {

1823 \_\_ASSERT(0, "64-bit cycle counter not enabled on this platform. "

1824 "See CONFIG\_TIMER\_HAS\_64BIT\_CYCLE\_COUNTER");

1825 return 0;

1826 }

1827

1828 return [arch\_k\_cycle\_get\_64](group__arch-timing.md#gacc1ed8d949f694a1d39e389334caf971)();

1829}

1830

1834

[ 1835](structk__queue.md)struct [k\_queue](structk__queue.md) {

[ 1836](structk__queue.md#a892371af9701ce67619e38446bc2ceae) [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) [data\_q](structk__queue.md#a892371af9701ce67619e38446bc2ceae);

[ 1837](structk__queue.md#a18fd165fec722384b3748bfdf3332a4c) struct [k\_spinlock](structk__spinlock.md) [lock](structk__queue.md#a18fd165fec722384b3748bfdf3332a4c);

[ 1838](structk__queue.md#a871d734f2b21a9cad3ca4a2ba79e64f1) \_wait\_q\_t [wait\_q](structk__queue.md#a871d734f2b21a9cad3ca4a2ba79e64f1);

1839

1840 Z\_DECL\_POLL\_EVENT

1841

1842 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_queue](structk__queue.md))

1843};

1844

1848

1849#define Z\_QUEUE\_INITIALIZER(obj) \

1850 { \

1851 .data\_q = SYS\_SFLIST\_STATIC\_INIT(&obj.data\_q), \

1852 .lock = { }, \

1853 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

1854 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

1855 }

1856

1860

1866

[ 1874](group__queue__apis.md#ga0236222d42768c2bf00942f328146c21)\_\_syscall void [k\_queue\_init](group__queue__apis.md#ga0236222d42768c2bf00942f328146c21)(struct [k\_queue](structk__queue.md) \*queue);

1875

[ 1889](group__queue__apis.md#ga7c39d86cc6509f59ff9223cac3ea5071)\_\_syscall void [k\_queue\_cancel\_wait](group__queue__apis.md#ga7c39d86cc6509f59ff9223cac3ea5071)(struct [k\_queue](structk__queue.md) \*queue);

1890

[ 1903](group__queue__apis.md#gaa84522a5ace6e7f8ba61033baca6972f)void [k\_queue\_append](group__queue__apis.md#gaa84522a5ace6e7f8ba61033baca6972f)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

1904

[ 1921](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_queue\_alloc\_append](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

1922

[ 1935](group__queue__apis.md#ga8ce013d8a037d4be5078797e0050e9c6)void [k\_queue\_prepend](group__queue__apis.md#ga8ce013d8a037d4be5078797e0050e9c6)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

1936

[ 1953](group__queue__apis.md#gacf3dba40125073c11075e5a134919f88)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_queue\_alloc\_prepend](group__queue__apis.md#gacf3dba40125073c11075e5a134919f88)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

1954

[ 1968](group__queue__apis.md#gad47336f27e433a52600a3b67ab89556a)void [k\_queue\_insert](group__queue__apis.md#gad47336f27e433a52600a3b67ab89556a)(struct [k\_queue](structk__queue.md) \*queue, void \*prev, void \*data);

1969

[ 1988](group__queue__apis.md#ga91d1a144fc2aeb3dd655accc94ca43aa)int [k\_queue\_append\_list](group__queue__apis.md#ga91d1a144fc2aeb3dd655accc94ca43aa)(struct [k\_queue](structk__queue.md) \*queue, void \*head, void \*tail);

1989

[ 2005](group__queue__apis.md#ga4eee0da7442d60572b05d60a9996e69d)int [k\_queue\_merge\_slist](group__queue__apis.md#ga4eee0da7442d60572b05d60a9996e69d)(struct [k\_queue](structk__queue.md) \*queue, [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list);

2006

[ 2025](group__queue__apis.md#ga0a77d8556e7d253319275de034f01619)\_\_syscall void \*[k\_queue\_get](group__queue__apis.md#ga0a77d8556e7d253319275de034f01619)(struct [k\_queue](structk__queue.md) \*queue, [k\_timeout\_t](structk__timeout__t.md) timeout);

2026

[ 2043](group__queue__apis.md#ga4bff929ed1d366a06e00865a5bbe2544)bool [k\_queue\_remove](group__queue__apis.md#ga4bff929ed1d366a06e00865a5bbe2544)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2044

[ 2059](group__queue__apis.md#ga287a2d81e2e3041be1cd45164e72f127)bool [k\_queue\_unique\_append](group__queue__apis.md#ga287a2d81e2e3041be1cd45164e72f127)(struct [k\_queue](structk__queue.md) \*queue, void \*data);

2060

[ 2074](group__queue__apis.md#gadb2bb8088868b3c5801c72b320389ca9)\_\_syscall int [k\_queue\_is\_empty](group__queue__apis.md#gadb2bb8088868b3c5801c72b320389ca9)(struct [k\_queue](structk__queue.md) \*queue);

2075

2076static inline int z\_impl\_k\_queue\_is\_empty(struct [k\_queue](structk__queue.md) \*queue)

2077{

2078 return (int)[sys\_sflist\_is\_empty](group__flagged-single-linked-list__apis.md#gac506235a9df89a7a52631e9990ceaad5)(&queue->[data\_q](structk__queue.md#a892371af9701ce67619e38446bc2ceae));

2079}

2080

[ 2090](group__queue__apis.md#ga8ccd5137690c127a0f7d67619b88a52b)\_\_syscall void \*[k\_queue\_peek\_head](group__queue__apis.md#ga8ccd5137690c127a0f7d67619b88a52b)(struct [k\_queue](structk__queue.md) \*queue);

2091

[ 2101](group__queue__apis.md#ga27a460c42836d8b093ad9274c14bb176)\_\_syscall void \*[k\_queue\_peek\_tail](group__queue__apis.md#ga27a460c42836d8b093ad9274c14bb176)(struct [k\_queue](structk__queue.md) \*queue);

2102

[ 2112](group__queue__apis.md#gacd0bc309f0147d4669f65fafa87e0e70)#define K\_QUEUE\_DEFINE(name) \

2113 STRUCT\_SECTION\_ITERABLE(k\_queue, name) = \

2114 Z\_QUEUE\_INITIALIZER(name)

2115

2117

2118#ifdef CONFIG\_USERSPACE

[ 2128](structk__futex.md)struct [k\_futex](structk__futex.md) {

[ 2129](structk__futex.md#a454ad1b595b899306c8e9c8e1431e7a7) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [val](structk__futex.md#a454ad1b595b899306c8e9c8e1431e7a7);

2130};

2131

2139struct z\_futex\_data {

2140 \_wait\_q\_t wait\_q;

2141 struct [k\_spinlock](structk__spinlock.md) lock;

2142};

2143

2144#define Z\_FUTEX\_DATA\_INITIALIZER(obj) \

2145 { \

2146 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q) \

2147 }

2148

2154

[ 2174](group__futex__apis.md#ga596bfa265f88567ad9e80fd38cd433d3)\_\_syscall int [k\_futex\_wait](group__futex__apis.md#ga596bfa265f88567ad9e80fd38cd433d3)(struct [k\_futex](structk__futex.md) \*futex, int expected,

2175 [k\_timeout\_t](structk__timeout__t.md) timeout);

2176

[ 2191](group__futex__apis.md#ga62de1aeb7c5c273aed20d0e05336d7a0)\_\_syscall int [k\_futex\_wake](group__futex__apis.md#ga62de1aeb7c5c273aed20d0e05336d7a0)(struct [k\_futex](structk__futex.md) \*futex, bool wake\_all);

2192

2194#endif

2195

2201

2206

[ 2207](structk__event.md)struct [k\_event](structk__event.md) {

[ 2208](structk__event.md#a5bacd5f2d34da646d9d7ee229842e432) \_wait\_q\_t [wait\_q](structk__event.md#a5bacd5f2d34da646d9d7ee229842e432);

[ 2209](structk__event.md#a54c6f5997132e88406ffa5bcc0a10b83) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [events](structk__event.md#a54c6f5997132e88406ffa5bcc0a10b83);

[ 2210](structk__event.md#a1f0de9c69f29ad854f3b0d510ceb1efc) struct [k\_spinlock](structk__spinlock.md) [lock](structk__event.md#a1f0de9c69f29ad854f3b0d510ceb1efc);

2211

2212 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_event](structk__event.md))

2213

2214#ifdef CONFIG\_OBJ\_CORE\_EVENT

2215 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2216#endif

2217

2218};

2219

2220#define Z\_EVENT\_INITIALIZER(obj) \

2221 { \

2222 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

2223 .events = 0 \

2224 }

2225

[ 2233](group__event__apis.md#gacf803590b39b095056f2b1c5090c4019)\_\_syscall void [k\_event\_init](group__event__apis.md#gacf803590b39b095056f2b1c5090c4019)(struct [k\_event](structk__event.md) \*event);

2234

[ 2250](group__event__apis.md#gac88d17410a71642a903890e420d23d76)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_post](group__event__apis.md#gac88d17410a71642a903890e420d23d76)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events);

2251

[ 2267](group__event__apis.md#gac22e9d768d003246e68b4b0b64e60f49)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_set](group__event__apis.md#gac22e9d768d003246e68b4b0b64e60f49)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events);

2268

[ 2283](group__event__apis.md#ga29b3ec1022b12a8c34884da3559c5864)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_set\_masked](group__event__apis.md#ga29b3ec1022b12a8c34884da3559c5864)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events,

2284 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events\_mask);

2285

[ 2296](group__event__apis.md#gad6bfd7bfd0587bc70d3aa0b988010376)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_clear](group__event__apis.md#gad6bfd7bfd0587bc70d3aa0b988010376)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events);

2297

[ 2319](group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_wait](group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events,

2320 bool reset, [k\_timeout\_t](structk__timeout__t.md) timeout);

2321

[ 2343](group__event__apis.md#gaddd60a99de5ac3d84f643c9433b744c1)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_wait\_all](group__event__apis.md#gaddd60a99de5ac3d84f643c9433b744c1)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events,

2344 bool reset, [k\_timeout\_t](structk__timeout__t.md) timeout);

2345

[ 2354](group__event__apis.md#ga81e66be0959e8cb0414d9772056a6264)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_event\_test](group__event__apis.md#ga81e66be0959e8cb0414d9772056a6264)(struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events\_mask)

2355{

2356 return [k\_event\_wait](group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753)(event, events\_mask, false, [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f));

2357}

2358

[ 2368](group__event__apis.md#ga093449cc6686d3235944f3faad284893)#define K\_EVENT\_DEFINE(name) \

2369 STRUCT\_SECTION\_ITERABLE(k\_event, name) = \

2370 Z\_EVENT\_INITIALIZER(name);

2371

2373

[ 2374](structk__fifo.md)struct [k\_fifo](structk__fifo.md) {

2375 struct [k\_queue](structk__queue.md) \_queue;

2376#ifdef CONFIG\_OBJ\_CORE\_FIFO

2377 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2378#endif

2379};

2380

2384#define Z\_FIFO\_INITIALIZER(obj) \

2385 { \

2386 .\_queue = Z\_QUEUE\_INITIALIZER(obj.\_queue) \

2387 }

2388

2392

2398

[ 2406](group__fifo__apis.md#gaeebf6ef54d4be61e19408f44a734a159)#define k\_fifo\_init(fifo) \

2407 ({ \

2408 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, init, fifo); \

2409 k\_queue\_init(&(fifo)->\_queue); \

2410 K\_OBJ\_CORE\_INIT(K\_OBJ\_CORE(fifo), \_obj\_type\_fifo); \

2411 K\_OBJ\_CORE\_LINK(K\_OBJ\_CORE(fifo)); \

2412 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, init, fifo); \

2413 })

2414

[ 2426](group__fifo__apis.md#gab744080af449e093df8dd4982e013e16)#define k\_fifo\_cancel\_wait(fifo) \

2427 ({ \

2428 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, cancel\_wait, fifo); \

2429 k\_queue\_cancel\_wait(&(fifo)->\_queue); \

2430 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, cancel\_wait, fifo); \

2431 })

2432

[ 2445](group__fifo__apis.md#ga3addb10f86f19e245c23362433d5c913)#define k\_fifo\_put(fifo, data) \

2446 ({ \

2447 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, put, fifo, data); \

2448 k\_queue\_append(&(fifo)->\_queue, data); \

2449 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, put, fifo, data); \

2450 })

2451

[ 2468](group__fifo__apis.md#gab1c5212040d12cbb92cede5cf54928ba)#define k\_fifo\_alloc\_put(fifo, data) \

2469 ({ \

2470 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, alloc\_put, fifo, data); \

2471 int fap\_ret = k\_queue\_alloc\_append(&(fifo)->\_queue, data); \

2472 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, alloc\_put, fifo, data, fap\_ret); \

2473 fap\_ret; \

2474 })

2475

[ 2490](group__fifo__apis.md#ga1bf5f52290c83e54ba14358cbbb4051b)#define k\_fifo\_put\_list(fifo, head, tail) \

2491 ({ \

2492 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, put\_list, fifo, head, tail); \

2493 k\_queue\_append\_list(&(fifo)->\_queue, head, tail); \

2494 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, put\_list, fifo, head, tail); \

2495 })

2496

[ 2510](group__fifo__apis.md#ga4cdc286a7a6f0d43acab63a4846815e7)#define k\_fifo\_put\_slist(fifo, list) \

2511 ({ \

2512 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, put\_slist, fifo, list); \

2513 k\_queue\_merge\_slist(&(fifo)->\_queue, list); \

2514 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, put\_slist, fifo, list); \

2515 })

2516

[ 2534](group__fifo__apis.md#ga1e2c480e2124116af97e94e7b4435de6)#define k\_fifo\_get(fifo, timeout) \

2535 ({ \

2536 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, get, fifo, timeout); \

2537 void \*fg\_ret = k\_queue\_get(&(fifo)->\_queue, timeout); \

2538 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, get, fifo, timeout, fg\_ret); \

2539 fg\_ret; \

2540 })

2541

[ 2555](group__fifo__apis.md#gab7cec4adc128ed1fd2d194ba6cd8c640)#define k\_fifo\_is\_empty(fifo) \

2556 k\_queue\_is\_empty(&(fifo)->\_queue)

2557

[ 2571](group__fifo__apis.md#ga2e0c8608f095a929740fa94c94a4f389)#define k\_fifo\_peek\_head(fifo) \

2572 ({ \

2573 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, peek\_head, fifo); \

2574 void \*fph\_ret = k\_queue\_peek\_head(&(fifo)->\_queue); \

2575 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, peek\_head, fifo, fph\_ret); \

2576 fph\_ret; \

2577 })

2578

[ 2590](group__fifo__apis.md#gafbe2ce9a6437b886cf149016187ba92f)#define k\_fifo\_peek\_tail(fifo) \

2591 ({ \

2592 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_fifo, peek\_tail, fifo); \

2593 void \*fpt\_ret = k\_queue\_peek\_tail(&(fifo)->\_queue); \

2594 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_fifo, peek\_tail, fifo, fpt\_ret); \

2595 fpt\_ret; \

2596 })

2597

[ 2607](group__fifo__apis.md#ga230b02a526ecb0ae1598be75cb9a8274)#define K\_FIFO\_DEFINE(name) \

2608 STRUCT\_SECTION\_ITERABLE(k\_fifo, name) = \

2609 Z\_FIFO\_INITIALIZER(name)

2610

2612

[ 2613](structk__lifo.md)struct [k\_lifo](structk__lifo.md) {

2614 struct [k\_queue](structk__queue.md) \_queue;

2615#ifdef CONFIG\_OBJ\_CORE\_LIFO

2616 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2617#endif

2618};

2619

2623

2624#define Z\_LIFO\_INITIALIZER(obj) \

2625 { \

2626 .\_queue = Z\_QUEUE\_INITIALIZER(obj.\_queue) \

2627 }

2628

2632

2638

[ 2646](group__lifo__apis.md#ga69fb19716a9014f7de79f8e524d64a3e)#define k\_lifo\_init(lifo) \

2647 ({ \

2648 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_lifo, init, lifo); \

2649 k\_queue\_init(&(lifo)->\_queue); \

2650 K\_OBJ\_CORE\_INIT(K\_OBJ\_CORE(lifo), \_obj\_type\_lifo); \

2651 K\_OBJ\_CORE\_LINK(K\_OBJ\_CORE(lifo)); \

2652 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_lifo, init, lifo); \

2653 })

2654

[ 2667](group__lifo__apis.md#gad662e36b1df8b9013e2dc61f9dfe3a8b)#define k\_lifo\_put(lifo, data) \

2668 ({ \

2669 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_lifo, put, lifo, data); \

2670 k\_queue\_prepend(&(lifo)->\_queue, data); \

2671 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_lifo, put, lifo, data); \

2672 })

2673

[ 2690](group__lifo__apis.md#ga96d885a6a36fcfcb5eaa65898eee0965)#define k\_lifo\_alloc\_put(lifo, data) \

2691 ({ \

2692 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_lifo, alloc\_put, lifo, data); \

2693 int lap\_ret = k\_queue\_alloc\_prepend(&(lifo)->\_queue, data); \

2694 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_lifo, alloc\_put, lifo, data, lap\_ret); \

2695 lap\_ret; \

2696 })

2697

[ 2715](group__lifo__apis.md#gad5f1775947b07a2a77f667aa9e41db5a)#define k\_lifo\_get(lifo, timeout) \

2716 ({ \

2717 SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(k\_lifo, get, lifo, timeout); \

2718 void \*lg\_ret = k\_queue\_get(&(lifo)->\_queue, timeout); \

2719 SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(k\_lifo, get, lifo, timeout, lg\_ret); \

2720 lg\_ret; \

2721 })

2722

[ 2732](group__lifo__apis.md#gaebd450d4181f22491623ea0aed6ee576)#define K\_LIFO\_DEFINE(name) \

2733 STRUCT\_SECTION\_ITERABLE(k\_lifo, name) = \

2734 Z\_LIFO\_INITIALIZER(name)

2735

2737

2741#define K\_STACK\_FLAG\_ALLOC ((uint8\_t)1) /\* Buffer was allocated \*/

2742

2743typedef [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) stack\_data\_t;

2744

2745struct k\_stack {

2746 \_wait\_q\_t wait\_q;

2747 struct [k\_spinlock](structk__spinlock.md) lock;

2748 stack\_data\_t \*base, \*next, \*top;

2749

2750 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

2751

2752 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_stack)

2753

2754#ifdef CONFIG\_OBJ\_CORE\_STACK

2755 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2756#endif

2757};

2758

2759#define Z\_STACK\_INITIALIZER(obj, stack\_buffer, stack\_num\_entries) \

2760 { \

2761 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

2762 .base = stack\_buffer, \

2763 .next = stack\_buffer, \

2764 .top = stack\_buffer + stack\_num\_entries, \

2765 }

2766

2770

2776

[ 2786](group__stack__apis.md#ga4400a39ef48289305cf66a092d5c6c7d)void [k\_stack\_init](group__stack__apis.md#ga4400a39ef48289305cf66a092d5c6c7d)(struct k\_stack \*stack,

2787 stack\_data\_t \*buffer, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_entries);

2788

2789

2803

[ 2804](group__stack__apis.md#gab97d924db1aef3f6adade156a107d45c)\_\_syscall [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [k\_stack\_alloc\_init](group__stack__apis.md#gab97d924db1aef3f6adade156a107d45c)(struct k\_stack \*stack,

2805 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_entries);

2806

[ 2818](group__stack__apis.md#ga819f4e7b2cf11cf2e1b80933fdcb67ea)int [k\_stack\_cleanup](group__stack__apis.md#ga819f4e7b2cf11cf2e1b80933fdcb67ea)(struct k\_stack \*stack);

2819

[ 2833](group__stack__apis.md#gaa6180f4db6ec93ee84149cba054d3e53)\_\_syscall int [k\_stack\_push](group__stack__apis.md#gaa6180f4db6ec93ee84149cba054d3e53)(struct k\_stack \*stack, stack\_data\_t data);

2834

[ 2855](group__stack__apis.md#ga36ce6ceb9ea3d5c36d22b10430789480)\_\_syscall int [k\_stack\_pop](group__stack__apis.md#ga36ce6ceb9ea3d5c36d22b10430789480)(struct k\_stack \*stack, stack\_data\_t \*data,

2856 [k\_timeout\_t](structk__timeout__t.md) timeout);

2857

[ 2868](group__stack__apis.md#ga8c9ca77e5de3c9757dcd4ecb55797835)#define K\_STACK\_DEFINE(name, stack\_num\_entries) \

2869 stack\_data\_t \_\_noinit \

2870 \_k\_stack\_buf\_##name[stack\_num\_entries]; \

2871 STRUCT\_SECTION\_ITERABLE(k\_stack, name) = \

2872 Z\_STACK\_INITIALIZER(name, \_k\_stack\_buf\_##name, \

2873 stack\_num\_entries)

2874

2876

2880

2881struct [k\_work](structk__work.md);

2882struct [k\_work\_q](structk__work__q.md);

2883struct [k\_work\_queue\_config](structk__work__queue__config.md);

2884extern struct [k\_work\_q](structk__work__q.md) k\_sys\_work\_q;

2885

2889

2895

[ 2900](structk__mutex.md)struct [k\_mutex](structk__mutex.md) {

[ 2902](structk__mutex.md#a4add234295bceff22551ee74f3aed802) \_wait\_q\_t [wait\_q](structk__mutex.md#a4add234295bceff22551ee74f3aed802);

[ 2904](structk__mutex.md#af910bb07dc99e50078de26fccca468e4) struct [k\_thread](structk__thread.md) \*[owner](structk__mutex.md#af910bb07dc99e50078de26fccca468e4);

2905

[ 2907](structk__mutex.md#a0db401fc8e03e1f984b8fd15af974718) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lock\_count](structk__mutex.md#a0db401fc8e03e1f984b8fd15af974718);

2908

[ 2910](structk__mutex.md#ab0d16fac9f8af960a501ffd93ec08c80) int [owner\_orig\_prio](structk__mutex.md#ab0d16fac9f8af960a501ffd93ec08c80);

2911

2912 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_mutex](structk__mutex.md))

2913

2914#ifdef CONFIG\_OBJ\_CORE\_MUTEX

2915 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

2916#endif

2917};

2918

2922#define Z\_MUTEX\_INITIALIZER(obj) \

2923 { \

2924 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

2925 .owner = NULL, \

2926 .lock\_count = 0, \

2927 .owner\_orig\_prio = K\_LOWEST\_APPLICATION\_THREAD\_PRIO, \

2928 }

2929

2933

[ 2943](group__mutex__apis.md#gab6f3d98fabbdc0918bbc9934d61d63f3)#define K\_MUTEX\_DEFINE(name) \

2944 STRUCT\_SECTION\_ITERABLE(k\_mutex, name) = \

2945 Z\_MUTEX\_INITIALIZER(name)

2946

[ 2959](group__mutex__apis.md#ga56b64952fb8b78b00268a21c28b41480)\_\_syscall int [k\_mutex\_init](group__mutex__apis.md#ga56b64952fb8b78b00268a21c28b41480)(struct [k\_mutex](structk__mutex.md) \*mutex);

2960

2961

[ 2983](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)\_\_syscall int [k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(struct [k\_mutex](structk__mutex.md) \*mutex, [k\_timeout\_t](structk__timeout__t.md) timeout);

2984

[ 3005](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)\_\_syscall int [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(struct [k\_mutex](structk__mutex.md) \*mutex);

3006

3010

3011

[ 3012](structk__condvar.md)struct [k\_condvar](structk__condvar.md) {

[ 3013](structk__condvar.md#a14b457a06420f093e779d569f4fea906) \_wait\_q\_t [wait\_q](structk__condvar.md#a14b457a06420f093e779d569f4fea906);

3014

3015#ifdef CONFIG\_OBJ\_CORE\_CONDVAR

3016 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

3017#endif

3018};

3019

3020#define Z\_CONDVAR\_INITIALIZER(obj) \

3021 { \

3022 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

3023 }

3024

3030

[ 3037](group__condvar__apis.md#gac9b497c56cc4642965afa6c0c6d7ecfc)\_\_syscall int [k\_condvar\_init](group__condvar__apis.md#gac9b497c56cc4642965afa6c0c6d7ecfc)(struct [k\_condvar](structk__condvar.md) \*condvar);

3038

[ 3045](group__condvar__apis.md#ga0376a8f7dc6e4f1e1eed55940f43015b)\_\_syscall int [k\_condvar\_signal](group__condvar__apis.md#ga0376a8f7dc6e4f1e1eed55940f43015b)(struct [k\_condvar](structk__condvar.md) \*condvar);

3046

[ 3054](group__condvar__apis.md#gad2e46a7b9e1bc934fd1f5cb38dde40d8)\_\_syscall int [k\_condvar\_broadcast](group__condvar__apis.md#gad2e46a7b9e1bc934fd1f5cb38dde40d8)(struct [k\_condvar](structk__condvar.md) \*condvar);

3055

[ 3073](group__condvar__apis.md#gab2e1d05db4f954755f430ca894e44dbc)\_\_syscall int [k\_condvar\_wait](group__condvar__apis.md#gab2e1d05db4f954755f430ca894e44dbc)(struct [k\_condvar](structk__condvar.md) \*condvar, struct [k\_mutex](structk__mutex.md) \*mutex,

3074 [k\_timeout\_t](structk__timeout__t.md) timeout);

3075

[ 3086](group__condvar__apis.md#ga770816651e25f7e7dae992a0b2260c21)#define K\_CONDVAR\_DEFINE(name) \

3087 STRUCT\_SECTION\_ITERABLE(k\_condvar, name) = \

3088 Z\_CONDVAR\_INITIALIZER(name)

3089

3092

3096

3097struct k\_sem {

3098 \_wait\_q\_t wait\_q;

3099 unsigned int count;

3100 unsigned int limit;

3101

3102 Z\_DECL\_POLL\_EVENT

3103

3104 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_sem)

3105

3106#ifdef CONFIG\_OBJ\_CORE\_SEM

3107 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

3108#endif

3109};

3110

3111#define Z\_SEM\_INITIALIZER(obj, initial\_count, count\_limit) \

3112 { \

3113 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

3114 .count = initial\_count, \

3115 .limit = count\_limit, \

3116 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

3117 }

3118

3122

3128

[ 3137](group__semaphore__apis.md#ga689359a77a0cebe737ef644c188f7e57)#define K\_SEM\_MAX\_LIMIT UINT\_MAX

3138

[ 3154](group__semaphore__apis.md#gadcd0e6cfba3392fb887222eafe4c1845)\_\_syscall int [k\_sem\_init](group__semaphore__apis.md#gadcd0e6cfba3392fb887222eafe4c1845)(struct k\_sem \*sem, unsigned int initial\_count,

3155 unsigned int limit);

3156

[ 3175](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)\_\_syscall int [k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)(struct k\_sem \*sem, [k\_timeout\_t](structk__timeout__t.md) timeout);

3176

[ 3187](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)\_\_syscall void [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)(struct k\_sem \*sem);

3188

[ 3198](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)\_\_syscall void [k\_sem\_reset](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)(struct k\_sem \*sem);

3199

[ 3209](group__semaphore__apis.md#ga58843b581e170a1811fc38eecbfd01f3)\_\_syscall unsigned int [k\_sem\_count\_get](group__semaphore__apis.md#ga58843b581e170a1811fc38eecbfd01f3)(struct k\_sem \*sem);

3210

3214static inline unsigned int z\_impl\_k\_sem\_count\_get(struct k\_sem \*sem)

3215{

3216 return sem->count;

3217}

3218

[ 3230](group__semaphore__apis.md#ga018a8aa43e02e704deee7b6341502946)#define K\_SEM\_DEFINE(name, initial\_count, count\_limit) \

3231 STRUCT\_SECTION\_ITERABLE(k\_sem, name) = \

3232 Z\_SEM\_INITIALIZER(name, initial\_count, count\_limit); \

3233 BUILD\_ASSERT(((count\_limit) != 0) && \

3234 ((initial\_count) <= (count\_limit)) && \

3235 ((count\_limit) <= K\_SEM\_MAX\_LIMIT));

3236

3238

3242

3243struct [k\_work\_delayable](structk__work__delayable.md);

3244struct [k\_work\_sync](structk__work__sync.md);

3245

3249

3255

[ 3262](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda)typedef void (\*[k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda))(struct [k\_work](structk__work.md) \*work);

3263

[ 3277](group__workqueue__apis.md#gaf20080884a2893d39cd8e862b34a2a30)void [k\_work\_init](group__workqueue__apis.md#gaf20080884a2893d39cd8e862b34a2a30)(struct [k\_work](structk__work.md) \*work,

3278 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) [handler](structk__work.md#a096d6ca1338fb0fbfa330b790136f172));

3279

[ 3294](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b)int [k\_work\_busy\_get](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b)(const struct [k\_work](structk__work.md) \*work);

3295

3309static inline bool [k\_work\_is\_pending](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)(const struct [k\_work](structk__work.md) \*work);

3310

[ 3331](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c)int [k\_work\_submit\_to\_queue](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137),

3332 struct [k\_work](structk__work.md) \*work);

3333

[ 3342](group__workqueue__apis.md#gace61b59575093d7442f39ccb7be686d7)int [k\_work\_submit](group__workqueue__apis.md#gace61b59575093d7442f39ccb7be686d7)(struct [k\_work](structk__work.md) \*work);

3343

[ 3368](group__workqueue__apis.md#gabd1cda459bab538fb2d6dfd84a73b253)bool [k\_work\_flush](group__workqueue__apis.md#gabd1cda459bab538fb2d6dfd84a73b253)(struct [k\_work](structk__work.md) \*work,

3369 struct [k\_work\_sync](structk__work__sync.md) \*sync);

3370

[ 3390](group__workqueue__apis.md#ga389fe2a8fb20f9bd593cf8d990727078)int [k\_work\_cancel](group__workqueue__apis.md#ga389fe2a8fb20f9bd593cf8d990727078)(struct [k\_work](structk__work.md) \*work);

3391

[ 3422](group__workqueue__apis.md#gab2b05cfe3af08f7d32c3946fa1c808f9)bool [k\_work\_cancel\_sync](group__workqueue__apis.md#gab2b05cfe3af08f7d32c3946fa1c808f9)(struct [k\_work](structk__work.md) \*work, struct [k\_work\_sync](structk__work__sync.md) \*sync);

3423

[ 3433](group__workqueue__apis.md#gada77d818ea9e4d07c14a960872ed5492)void [k\_work\_queue\_init](group__workqueue__apis.md#gada77d818ea9e4d07c14a960872ed5492)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137));

3434

[ 3454](group__workqueue__apis.md#gadfc56554f9bfe7b52309d79660188593)void [k\_work\_queue\_start](group__workqueue__apis.md#gadfc56554f9bfe7b52309d79660188593)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137),

3455 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, size\_t stack\_size,

3456 int prio, const struct [k\_work\_queue\_config](structk__work__queue__config.md) \*cfg);

3457

3467static inline [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_work\_queue\_thread\_get](group__workqueue__apis.md#ga0b8b496f7e7bd82d08590a07293e38d7)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137));

3468

[ 3492](group__workqueue__apis.md#ga0fefe3e0225ac99b47b250849f6cd863)int [k\_work\_queue\_drain](group__workqueue__apis.md#ga0fefe3e0225ac99b47b250849f6cd863)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137), bool plug);

3493

[ 3507](group__workqueue__apis.md#gaa0463bb79af3ec470f7d3be02052139f)int [k\_work\_queue\_unplug](group__workqueue__apis.md#gaa0463bb79af3ec470f7d3be02052139f)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137));

3508

[ 3522](group__workqueue__apis.md#ga2876c5d82fb2340a093bc4d689a55465)void [k\_work\_init\_delayable](group__workqueue__apis.md#ga2876c5d82fb2340a093bc4d689a55465)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3523 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) [handler](structk__work.md#a096d6ca1338fb0fbfa330b790136f172));

3524

3536static inline struct [k\_work\_delayable](structk__work__delayable.md) \*

3537[k\_work\_delayable\_from\_work](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca)(struct [k\_work](structk__work.md) \*[work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629));

3538

[ 3552](group__workqueue__apis.md#ga1b76969667844f0981d348c9c671bc9f)int [k\_work\_delayable\_busy\_get](group__workqueue__apis.md#ga1b76969667844f0981d348c9c671bc9f)(const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3553

3568static inline bool [k\_work\_delayable\_is\_pending](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e)(

3569 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3570

3584static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_work\_delayable\_expires\_get](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624)(

3585 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3586

3600static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_work\_delayable\_remaining\_get](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4)(

3601 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3602

[ 3628](group__workqueue__apis.md#ga17f863c9f6ff2fb41dc0f3b7de4fdf23)int [k\_work\_schedule\_for\_queue](group__workqueue__apis.md#ga17f863c9f6ff2fb41dc0f3b7de4fdf23)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4),

3629 struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3630 [k\_timeout\_t](structk__timeout__t.md) delay);

3631

[ 3645](group__workqueue__apis.md#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)int [k\_work\_schedule](group__workqueue__apis.md#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3646 [k\_timeout\_t](structk__timeout__t.md) delay);

3647

[ 3683](group__workqueue__apis.md#gabf5db091eac19b19a4e12c0cb381f0a8)int [k\_work\_reschedule\_for\_queue](group__workqueue__apis.md#gabf5db091eac19b19a4e12c0cb381f0a8)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4),

3684 struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3685 [k\_timeout\_t](structk__timeout__t.md) delay);

3686

[ 3699](group__workqueue__apis.md#gaacaab408fb7c848d466ad1f069dfa648)int [k\_work\_reschedule](group__workqueue__apis.md#gaacaab408fb7c848d466ad1f069dfa648)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3700 [k\_timeout\_t](structk__timeout__t.md) delay);

3701

[ 3726](group__workqueue__apis.md#gad47d54e513030304be2600d75b1a965f)bool [k\_work\_flush\_delayable](group__workqueue__apis.md#gad47d54e513030304be2600d75b1a965f)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3727 struct [k\_work\_sync](structk__work__sync.md) \*sync);

3728

[ 3749](group__workqueue__apis.md#ga92355914ee178d4c3e848a1946bed3e4)int [k\_work\_cancel\_delayable](group__workqueue__apis.md#ga92355914ee178d4c3e848a1946bed3e4)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork);

3750

[ 3779](group__workqueue__apis.md#ga7e7ec237648556fc16bfda8d35f7cd86)bool [k\_work\_cancel\_delayable\_sync](group__workqueue__apis.md#ga7e7ec237648556fc16bfda8d35f7cd86)(struct [k\_work\_delayable](structk__work__delayable.md) \*dwork,

3780 struct [k\_work\_sync](structk__work__sync.md) \*sync);

3781

3782enum {

3786

3787 /\* The atomic API is used for all work and queue flags fields to

3788 \* enforce sequential consistency in SMP environments.

3789 \*/

3790

3791 /\* Bits that represent the work item states. At least nine of the

3792 \* combinations are distinct valid stable states.

3793 \*/

3794 K\_WORK\_RUNNING\_BIT = 0,

3795 K\_WORK\_CANCELING\_BIT = 1,

3796 K\_WORK\_QUEUED\_BIT = 2,

3797 K\_WORK\_DELAYED\_BIT = 3,

3798 K\_WORK\_FLUSHING\_BIT = 4,

3799

3800 K\_WORK\_MASK = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_DELAYED\_BIT) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUED\_BIT)

3801 | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_RUNNING\_BIT) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_CANCELING\_BIT) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_FLUSHING\_BIT),

3802

3803 /\* Static work flags \*/

3804 K\_WORK\_DELAYABLE\_BIT = 8,

3805 K\_WORK\_DELAYABLE = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_DELAYABLE\_BIT),

3806

3807 /\* Dynamic work queue flags \*/

3808 K\_WORK\_QUEUE\_STARTED\_BIT = 0,

3809 K\_WORK\_QUEUE\_STARTED = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_STARTED\_BIT),

3810 K\_WORK\_QUEUE\_BUSY\_BIT = 1,

3811 K\_WORK\_QUEUE\_BUSY = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_BUSY\_BIT),

3812 K\_WORK\_QUEUE\_DRAIN\_BIT = 2,

3813 K\_WORK\_QUEUE\_DRAIN = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_DRAIN\_BIT),

3814 K\_WORK\_QUEUE\_PLUGGED\_BIT = 3,

3815 K\_WORK\_QUEUE\_PLUGGED = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_PLUGGED\_BIT),

3816

3817 /\* Static work queue flags \*/

3818 K\_WORK\_QUEUE\_NO\_YIELD\_BIT = 8,

3819 K\_WORK\_QUEUE\_NO\_YIELD = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUE\_NO\_YIELD\_BIT),

3820

3824 /\* Transient work flags \*/

3825

[ 3831](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165) [K\_WORK\_RUNNING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_RUNNING\_BIT),

3832

[ 3837](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732) [K\_WORK\_CANCELING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_CANCELING\_BIT),

3838

[ 3844](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85) [K\_WORK\_QUEUED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_QUEUED\_BIT),

3845

[ 3851](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed) [K\_WORK\_DELAYED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_DELAYED\_BIT),

3852

[ 3857](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601) [K\_WORK\_FLUSHING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(K\_WORK\_FLUSHING\_BIT),

3858};

3859

[ 3861](structk__work.md)struct [k\_work](structk__work.md) {

3862 /\* All fields are protected by the work module spinlock. No fields

3863 \* are to be accessed except through kernel API.

3864 \*/

3865

3866 /\* Node to link into k\_work\_q pending list. \*/

[ 3867](structk__work.md#a85772682983e0fdeb735f0821d5710d4) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structk__work.md#a85772682983e0fdeb735f0821d5710d4);

3868

3869 /\* The function to be invoked by the work queue thread. \*/

[ 3870](structk__work.md#a096d6ca1338fb0fbfa330b790136f172) [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) [handler](structk__work.md#a096d6ca1338fb0fbfa330b790136f172);

3871

3872 /\* The queue on which the work item was last submitted. \*/

[ 3873](structk__work.md#a551be8394e041020c36a97dc2e12e137) struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work.md#a551be8394e041020c36a97dc2e12e137);

3874

3875 /\* State of the work item.

3876 \*

3877 \* The item can be DELAYED, QUEUED, and RUNNING simultaneously.

3878 \*

3879 \* It can be RUNNING and CANCELING simultaneously.

3880 \*/

[ 3881](structk__work.md#a391ed7d2039cd05c9894267bf8ea4dfd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structk__work.md#a391ed7d2039cd05c9894267bf8ea4dfd);

3882};

3883

3884#define Z\_WORK\_INITIALIZER(work\_handler) { \

3885 .handler = work\_handler, \

3886}

3887

[ 3889](structk__work__delayable.md)struct [k\_work\_delayable](structk__work__delayable.md) {

3890 /\* The work item. \*/

[ 3891](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629) struct [k\_work](structk__work.md) [work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629);

3892

3893 /\* Timeout used to submit work after a delay. \*/

[ 3894](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d) struct \_timeout [timeout](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d);

3895

3896 /\* The queue to which the work should be submitted. \*/

[ 3897](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4) struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4);

3898};

3899

3900#define Z\_WORK\_DELAYABLE\_INITIALIZER(work\_handler) { \

3901 .work = { \

3902 .handler = work\_handler, \

3903 .flags = K\_WORK\_DELAYABLE, \

3904 }, \

3905}

3906

[ 3923](group__workqueue__apis.md#ga893b281f3d2bc0088650536899e17903)#define K\_WORK\_DELAYABLE\_DEFINE(work, work\_handler) \

3924 struct k\_work\_delayable work \

3925 = Z\_WORK\_DELAYABLE\_INITIALIZER(work\_handler)

3926

3930

3931/\* Record used to wait for work to flush.

3932 \*

3933 \* The work item is inserted into the queue that will process (or is

3934 \* processing) the item, and will be processed as soon as the item

3935 \* completes. When the flusher is processed the semaphore will be

3936 \* signaled, releasing the thread waiting for the flush.

3937 \*/

3938struct z\_work\_flusher {

3939 struct [k\_work](structk__work.md) work;

3940 struct k\_sem sem;

3941};

3942

3943/\* Record used to wait for work to complete a cancellation.

3944 \*

3945 \* The work item is inserted into a global queue of pending cancels.

3946 \* When a cancelling work item goes idle any matching waiters are

3947 \* removed from pending\_cancels and are woken.

3948 \*/

3949struct z\_work\_canceller {

3950 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

3951 struct k\_work \*work;

3952 struct k\_sem sem;

3953};

3954

3958

[ 3972](structk__work__sync.md)struct [k\_work\_sync](structk__work__sync.md) {

3973 union {

[ 3974](structk__work__sync.md#ad81ff57cb9f2f3dc5f2d65917cf04f1c) struct z\_work\_flusher [flusher](structk__work__sync.md#ad81ff57cb9f2f3dc5f2d65917cf04f1c);

[ 3975](structk__work__sync.md#a7e8fd0b9d6736c403aefa8462c7c0835) struct z\_work\_canceller [canceller](structk__work__sync.md#a7e8fd0b9d6736c403aefa8462c7c0835);

3976 };

3977};

3978

[ 3985](structk__work__queue__config.md)struct [k\_work\_queue\_config](structk__work__queue__config.md) {

[ 3990](structk__work__queue__config.md#a0929d83372efff6798bc69bb7ca1eaaa) const char \*[name](structk__work__queue__config.md#a0929d83372efff6798bc69bb7ca1eaaa);

3991

[ 4004](structk__work__queue__config.md#afcf64d6e69d1ddfff8cbd749dafa4d13) bool [no\_yield](structk__work__queue__config.md#afcf64d6e69d1ddfff8cbd749dafa4d13);

4005};

4006

[ 4008](structk__work__q.md)struct [k\_work\_q](structk__work__q.md) {

4009 /\* The thread that animates the work. \*/

[ 4010](structk__work__q.md#aa42ca271a4989f129bf1a43c491327eb) struct [k\_thread](structk__thread.md) [thread](structk__work__q.md#aa42ca271a4989f129bf1a43c491327eb);

4011

4012 /\* All the following fields must be accessed only while the

4013 \* work module spinlock is held.

4014 \*/

4015

4016 /\* List of k\_work items to be worked. \*/

[ 4017](structk__work__q.md#a2012199571f6b658873550d64386b00c) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [pending](structk__work__q.md#a2012199571f6b658873550d64386b00c);

4018

4019 /\* Wait queue for idle work thread. \*/

[ 4020](structk__work__q.md#a561c90f8bb944217230e00052cdecf10) \_wait\_q\_t [notifyq](structk__work__q.md#a561c90f8bb944217230e00052cdecf10);

4021

4022 /\* Wait queue for threads waiting for the queue to drain. \*/

[ 4023](structk__work__q.md#a308d1ac78b1203b7ea78b0f18c5bdf5b) \_wait\_q\_t [drainq](structk__work__q.md#a308d1ac78b1203b7ea78b0f18c5bdf5b);

4024

4025 /\* Flags describing queue state. \*/

[ 4026](structk__work__q.md#a68bc8e9c412ebdbf34827087d91a080e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structk__work__q.md#a68bc8e9c412ebdbf34827087d91a080e);

4027};

4028

4029/\* Provide the implementation for inline functions declared above \*/

4030

[ 4031](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)static inline bool [k\_work\_is\_pending](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)(const struct [k\_work](structk__work.md) \*work)

4032{

4033 return [k\_work\_busy\_get](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b)(work) != 0;

4034}

4035

4036static inline struct [k\_work\_delayable](structk__work__delayable.md) \*

[ 4037](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca)[k\_work\_delayable\_from\_work](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca)(struct [k\_work](structk__work.md) \*[work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629))

4038{

4039 return [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)([work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629), struct [k\_work\_delayable](structk__work__delayable.md), [work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629));

4040}

4041

[ 4042](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e)static inline bool [k\_work\_delayable\_is\_pending](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e)(

4043 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork)

4044{

4045 return [k\_work\_delayable\_busy\_get](group__workqueue__apis.md#ga1b76969667844f0981d348c9c671bc9f)(dwork) != 0;

4046}

4047

[ 4048](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624)static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_work\_delayable\_expires\_get](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624)(

4049 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork)

4050{

4051 return z\_timeout\_expires(&dwork->[timeout](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d));

4052}

4053

[ 4054](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4)static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [k\_work\_delayable\_remaining\_get](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4)(

4055 const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork)

4056{

4057 return z\_timeout\_remaining(&dwork->[timeout](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d));

4058}

4059

[ 4060](group__workqueue__apis.md#ga0b8b496f7e7bd82d08590a07293e38d7)static inline [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_work\_queue\_thread\_get](group__workqueue__apis.md#ga0b8b496f7e7bd82d08590a07293e38d7)(struct [k\_work\_q](structk__work__q.md) \*[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4))

4061{

4062 return &[queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4)->[thread](structk__work__q.md#aa42ca271a4989f129bf1a43c491327eb);

4063}

4064

4066

4067struct k\_work\_user;

4068

4073

[ 4083](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc)typedef void (\*[k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc))(struct k\_work\_user \*work);

4084

4088

4089struct k\_work\_user\_q {

4090 struct [k\_queue](structk__queue.md) queue;

4091 struct [k\_thread](structk__thread.md) thread;

4092};

4093

4094enum {

4095 K\_WORK\_USER\_STATE\_PENDING, /\* Work item pending state \*/

4096};

4097

4098struct k\_work\_user {

4099 void \*\_reserved; /\* Used by k\_queue implementation. \*/

4100 [k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc) handler;

4101 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

4102};

4103

4107

4108#if defined(\_\_cplusplus) && ((\_\_cplusplus - 0) < 202002L)

4109#define Z\_WORK\_USER\_INITIALIZER(work\_handler) { NULL, work\_handler, 0 }

4110#else

4111#define Z\_WORK\_USER\_INITIALIZER(work\_handler) \

4112 { \

4113 .\_reserved = NULL, \

4114 .handler = work\_handler, \

4115 .flags = 0 \

4116 }

4117#endif

4118

[ 4130](group__workqueue__apis.md#ga4f3eac1fc56d5c9c21a3afa9b964b0bf)#define K\_WORK\_USER\_DEFINE(work, work\_handler) \

4131 struct k\_work\_user work = Z\_WORK\_USER\_INITIALIZER(work\_handler)

4132

[ 4142](group__workqueue__apis.md#ga9de9c7a7f13cc6b325e5453e34afe62d)static inline void [k\_work\_user\_init](group__workqueue__apis.md#ga9de9c7a7f13cc6b325e5453e34afe62d)(struct k\_work\_user \*work,

4143 [k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc) handler)

4144{

4145 \*work = (struct k\_work\_user)Z\_WORK\_USER\_INITIALIZER(handler);

4146}

4147

[ 4164](group__workqueue__apis.md#ga58d05d4127e4cd51104a1f1a87f626cd)static inline bool [k\_work\_user\_is\_pending](group__workqueue__apis.md#ga58d05d4127e4cd51104a1f1a87f626cd)(struct k\_work\_user \*work)

4165{

4166 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(&work->flags, K\_WORK\_USER\_STATE\_PENDING);

4167}

4168

[ 4187](group__workqueue__apis.md#ga50ae1f6f74c0bc0a41dbbf789fff8856)static inline int [k\_work\_user\_submit\_to\_queue](group__workqueue__apis.md#ga50ae1f6f74c0bc0a41dbbf789fff8856)(struct k\_work\_user\_q \*work\_q,

4188 struct k\_work\_user \*work)

4189{

4190 int ret = -[EBUSY](group__system__errno.md#ga8368025077a0385849d6817b2007c095);

4191

4192 if (![atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)(&work->flags,

4193 K\_WORK\_USER\_STATE\_PENDING)) {

4194 ret = [k\_queue\_alloc\_append](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a)(&work\_q->queue, work);

4195

4196 /\* Couldn't insert into the queue. Clear the pending bit

4197 \* so the work item can be submitted again

4198 \*/

4199 if (ret != 0) {

4200 [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)(&work->flags,

4201 K\_WORK\_USER\_STATE\_PENDING);

4202 }

4203 }

4204

4205 return ret;

4206}

4207

[ 4227](group__workqueue__apis.md#ga3091bc8fab5311252e41634a97a18589)void [k\_work\_user\_queue\_start](group__workqueue__apis.md#ga3091bc8fab5311252e41634a97a18589)(struct k\_work\_user\_q \*work\_q,

4228 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack,

4229 size\_t stack\_size, int prio,

4230 const char \*name);

4231

[ 4242](group__workqueue__apis.md#gab487068e9564cd77b6bdbac3d5670923)static inline [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [k\_work\_user\_queue\_thread\_get](group__workqueue__apis.md#gab487068e9564cd77b6bdbac3d5670923)(struct k\_work\_user\_q \*work\_q)

4243{

4244 return &work\_q->thread;

4245}

4246

4248

4252

4253struct k\_work\_poll {

4254 struct k\_work work;

4255 struct k\_work\_q \*workq;

4256 struct z\_poller poller;

4257 struct k\_poll\_event \*events;

4258 int num\_events;

4259 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) real\_handler;

4260 struct \_timeout timeout;

4261 int poll\_result;

4262};

4263

4267

4272

[ 4284](group__workqueue__apis.md#gaf8e003eefa5dd66ba883688f9d39c333)#define K\_WORK\_DEFINE(work, work\_handler) \

4285 struct k\_work work = Z\_WORK\_INITIALIZER(work\_handler)

4286

[ 4296](group__workqueue__apis.md#ga371dab33a40622bea19b07d852863443)void [k\_work\_poll\_init](group__workqueue__apis.md#ga371dab33a40622bea19b07d852863443)(struct k\_work\_poll \*work,

4297 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) handler);

4298

[ 4333](group__workqueue__apis.md#ga0abafd7f851e42fd3572c8438e600a53)int [k\_work\_poll\_submit\_to\_queue](group__workqueue__apis.md#ga0abafd7f851e42fd3572c8438e600a53)(struct [k\_work\_q](structk__work__q.md) \*work\_q,

4334 struct k\_work\_poll \*work,

4335 struct [k\_poll\_event](structk__poll__event.md) \*events,

4336 int num\_events,

4337 [k\_timeout\_t](structk__timeout__t.md) timeout);

4338

[ 4370](group__workqueue__apis.md#gad9f222e46d72c4f98739395a0c8bb4ea)int [k\_work\_poll\_submit](group__workqueue__apis.md#gad9f222e46d72c4f98739395a0c8bb4ea)(struct k\_work\_poll \*work,

4371 struct [k\_poll\_event](structk__poll__event.md) \*events,

4372 int num\_events,

4373 [k\_timeout\_t](structk__timeout__t.md) timeout);

4374

[ 4389](group__workqueue__apis.md#ga2a19547d04dc1a202e80b752e3177215)int [k\_work\_poll\_cancel](group__workqueue__apis.md#ga2a19547d04dc1a202e80b752e3177215)(struct k\_work\_poll \*work);

4390

4392

4398

[ 4402](structk__msgq.md)struct [k\_msgq](structk__msgq.md) {

[ 4404](structk__msgq.md#ae3b3d53d60b789d69c65494cfd090076) \_wait\_q\_t [wait\_q](structk__msgq.md#ae3b3d53d60b789d69c65494cfd090076);

[ 4406](structk__msgq.md#aa2e00a7292502f0de88cff28c5e375f0) struct [k\_spinlock](structk__spinlock.md) [lock](structk__msgq.md#aa2e00a7292502f0de88cff28c5e375f0);

[ 4408](structk__msgq.md#a512fe468da96540639a0d71f1707f79d) size\_t [msg\_size](structk__msgq.md#a512fe468da96540639a0d71f1707f79d);

[ 4410](structk__msgq.md#aebd3b6e91e97b2d4369feea1a3f7b7a0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_msgs](structk__msgq.md#aebd3b6e91e97b2d4369feea1a3f7b7a0);

[ 4412](structk__msgq.md#aca77f1cf833d3aa27ae65004b446bdd2) char \*[buffer\_start](structk__msgq.md#aca77f1cf833d3aa27ae65004b446bdd2);

[ 4414](structk__msgq.md#a9d47fd25d7a70e8518d45dd48c51f0e0) char \*[buffer\_end](structk__msgq.md#a9d47fd25d7a70e8518d45dd48c51f0e0);

[ 4416](structk__msgq.md#a594e8a4a638521f42f24f85fe0742d64) char \*[read\_ptr](structk__msgq.md#a594e8a4a638521f42f24f85fe0742d64);

[ 4418](structk__msgq.md#aacf9b7b9f6e26e402f3752fc56834f23) char \*[write\_ptr](structk__msgq.md#aacf9b7b9f6e26e402f3752fc56834f23);

[ 4420](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [used\_msgs](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857);

4421

4422 Z\_DECL\_POLL\_EVENT

4423

[ 4425](structk__msgq.md#ae03025420908f8342ce12a1395c7657b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structk__msgq.md#ae03025420908f8342ce12a1395c7657b);

4426

4427 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_msgq](structk__msgq.md))

4428

4429#ifdef CONFIG\_OBJ\_CORE\_MSGQ

4430 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

4431#endif

4432};

4433

4436

4437

4438#define Z\_MSGQ\_INITIALIZER(obj, q\_buffer, q\_msg\_size, q\_max\_msgs) \

4439 { \

4440 .wait\_q = Z\_WAIT\_Q\_INIT(&obj.wait\_q), \

4441 .msg\_size = q\_msg\_size, \

4442 .max\_msgs = q\_max\_msgs, \

4443 .buffer\_start = q\_buffer, \

4444 .buffer\_end = q\_buffer + (q\_max\_msgs \* q\_msg\_size), \

4445 .read\_ptr = q\_buffer, \

4446 .write\_ptr = q\_buffer, \

4447 .used\_msgs = 0, \

4448 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

4449 }

4450

4454

4455

[ 4456](group__msgq__apis.md#ga4bb73f46fd0818f7f7a90860b792f7ce)#define K\_MSGQ\_FLAG\_ALLOC BIT(0)

4457

[ 4461](structk__msgq__attrs.md)struct [k\_msgq\_attrs](structk__msgq__attrs.md) {

[ 4463](structk__msgq__attrs.md#a7d1d72946bdd517c07da37493a89e30e) size\_t [msg\_size](structk__msgq__attrs.md#a7d1d72946bdd517c07da37493a89e30e);

[ 4465](structk__msgq__attrs.md#ad0f5894ba0da840b91eb85015252e649) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_msgs](structk__msgq__attrs.md#ad0f5894ba0da840b91eb85015252e649);

[ 4467](structk__msgq__attrs.md#a00f936870442fa455117cbdd7821fac5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [used\_msgs](structk__msgq__attrs.md#a00f936870442fa455117cbdd7821fac5);

4468};

4469

4470

[ 4489](group__msgq__apis.md#ga95ef93002766901511d09c8cd8f8293b)#define K\_MSGQ\_DEFINE(q\_name, q\_msg\_size, q\_max\_msgs, q\_align) \

4490 static char \_\_noinit \_\_aligned(q\_align) \

4491 \_k\_fifo\_buf\_##q\_name[(q\_max\_msgs) \* (q\_msg\_size)]; \

4492 STRUCT\_SECTION\_ITERABLE(k\_msgq, q\_name) = \

4493 Z\_MSGQ\_INITIALIZER(q\_name, \_k\_fifo\_buf\_##q\_name, \

4494 (q\_msg\_size), (q\_max\_msgs))

4495

[ 4510](group__msgq__apis.md#ga54a5cdcaea2236c383ace433fedc0d39)void [k\_msgq\_init](group__msgq__apis.md#ga54a5cdcaea2236c383ace433fedc0d39)(struct [k\_msgq](structk__msgq.md) \*msgq, char \*buffer, size\_t msg\_size,

4511 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_msgs);

4512

[ 4532](group__msgq__apis.md#gabe7305b8f442ebdc147dbbc6e8cf92fc)\_\_syscall int [k\_msgq\_alloc\_init](group__msgq__apis.md#gabe7305b8f442ebdc147dbbc6e8cf92fc)(struct [k\_msgq](structk__msgq.md) \*msgq, size\_t msg\_size,

4533 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_msgs);

4534

[ 4545](group__msgq__apis.md#gafda4399aa9b8f1e44bdf752e00ea787b)int [k\_msgq\_cleanup](group__msgq__apis.md#gafda4399aa9b8f1e44bdf752e00ea787b)(struct [k\_msgq](structk__msgq.md) \*msgq);

4546

[ 4568](group__msgq__apis.md#ga54e96aaaea5462a1f963b7fd5ca82bfe)\_\_syscall int [k\_msgq\_put](group__msgq__apis.md#ga54e96aaaea5462a1f963b7fd5ca82bfe)(struct [k\_msgq](structk__msgq.md) \*msgq, const void \*data, [k\_timeout\_t](structk__timeout__t.md) timeout);

4569

[ 4590](group__msgq__apis.md#gae67f2ced2df1f9c290ae15dab9097cb7)\_\_syscall int [k\_msgq\_get](group__msgq__apis.md#gae67f2ced2df1f9c290ae15dab9097cb7)(struct [k\_msgq](structk__msgq.md) \*msgq, void \*data, [k\_timeout\_t](structk__timeout__t.md) timeout);

4591

[ 4606](group__msgq__apis.md#ga14f543472f2f63cfde0bdfa87b95c915)\_\_syscall int [k\_msgq\_peek](group__msgq__apis.md#ga14f543472f2f63cfde0bdfa87b95c915)(struct [k\_msgq](structk__msgq.md) \*msgq, void \*data);

4607

[ 4624](group__msgq__apis.md#ga69b004a40ab4ca497de314a99960fb8e)\_\_syscall int [k\_msgq\_peek\_at](group__msgq__apis.md#ga69b004a40ab4ca497de314a99960fb8e)(struct [k\_msgq](structk__msgq.md) \*msgq, void \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx);

4625

[ 4635](group__msgq__apis.md#gaa18875887773195ae44b7fe0972ee760)\_\_syscall void [k\_msgq\_purge](group__msgq__apis.md#gaa18875887773195ae44b7fe0972ee760)(struct [k\_msgq](structk__msgq.md) \*msgq);

4636

[ 4647](group__msgq__apis.md#ga7d154beb4f9c6227eddbef26d406ca24)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_msgq\_num\_free\_get](group__msgq__apis.md#ga7d154beb4f9c6227eddbef26d406ca24)(struct [k\_msgq](structk__msgq.md) \*msgq);

4648

[ 4657](group__msgq__apis.md#ga8f9d3eef67cbc9c0717a84190bbf7f41)\_\_syscall void [k\_msgq\_get\_attrs](group__msgq__apis.md#ga8f9d3eef67cbc9c0717a84190bbf7f41)(struct [k\_msgq](structk__msgq.md) \*msgq,

4658 struct [k\_msgq\_attrs](structk__msgq__attrs.md) \*attrs);

4659

4660

4661static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_k\_msgq\_num\_free\_get(struct [k\_msgq](structk__msgq.md) \*msgq)

4662{

4663 return msgq->[max\_msgs](structk__msgq.md#aebd3b6e91e97b2d4369feea1a3f7b7a0) - msgq->[used\_msgs](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857);

4664}

4665

[ 4675](group__msgq__apis.md#ga458793a89f1d9f762bda3422918a9faa)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_msgq\_num\_used\_get](group__msgq__apis.md#ga458793a89f1d9f762bda3422918a9faa)(struct [k\_msgq](structk__msgq.md) \*msgq);

4676

4677static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_k\_msgq\_num\_used\_get(struct [k\_msgq](structk__msgq.md) \*msgq)

4678{

4679 return msgq->[used\_msgs](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857);

4680}

4681

4683

4689

[ 4694](structk__mbox__msg.md)struct [k\_mbox\_msg](structk__mbox__msg.md) {

[ 4696](structk__mbox__msg.md#aeabf45e9599a64852a1cfd656b1ece8e) size\_t [size](structk__mbox__msg.md#aeabf45e9599a64852a1cfd656b1ece8e);

[ 4698](structk__mbox__msg.md#aa79f2bf71431b474ec4551ade4d7a8dd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [info](structk__mbox__msg.md#aa79f2bf71431b474ec4551ade4d7a8dd);

[ 4700](structk__mbox__msg.md#a74b0edeed4c44cb5932eb292efc9d9c2) void \*[tx\_data](structk__mbox__msg.md#a74b0edeed4c44cb5932eb292efc9d9c2);

[ 4702](structk__mbox__msg.md#a9eb145a242ac66e80d90286d83fe7a61) [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [rx\_source\_thread](structk__mbox__msg.md#a9eb145a242ac66e80d90286d83fe7a61);

[ 4704](structk__mbox__msg.md#a73236acb7d27bb0233f5abb7214fb19c) [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [tx\_target\_thread](structk__mbox__msg.md#a73236acb7d27bb0233f5abb7214fb19c);

4706 [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) \_syncing\_thread;

4707#if (CONFIG\_NUM\_MBOX\_ASYNC\_MSGS > 0)

4709 struct k\_sem \*\_async\_sem;

4710#endif

4711};

4712

[ 4716](structk__mbox.md)struct [k\_mbox](structk__mbox.md) {

[ 4718](structk__mbox.md#a0bca912a50120707ddafa66d740ade96) \_wait\_q\_t [tx\_msg\_queue](structk__mbox.md#a0bca912a50120707ddafa66d740ade96);

[ 4720](structk__mbox.md#a808a14c31892a2d042cdb0723a2956e2) \_wait\_q\_t [rx\_msg\_queue](structk__mbox.md#a808a14c31892a2d042cdb0723a2956e2);

[ 4721](structk__mbox.md#a2c549d5bd7216b62d81ad2198e0d79e4) struct [k\_spinlock](structk__spinlock.md) [lock](structk__mbox.md#a2c549d5bd7216b62d81ad2198e0d79e4);

4722

4723 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_mbox](structk__mbox.md))

4724

4725#ifdef CONFIG\_OBJ\_CORE\_MAILBOX

4726 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

4727#endif

4728};

4729

4732

4733#define Z\_MBOX\_INITIALIZER(obj) \

4734 { \

4735 .tx\_msg\_queue = Z\_WAIT\_Q\_INIT(&obj.tx\_msg\_queue), \

4736 .rx\_msg\_queue = Z\_WAIT\_Q\_INIT(&obj.rx\_msg\_queue), \

4737 }

4738

4742

[ 4752](group__mailbox__apis.md#gab55cba898db47113a06641c01f3e3714)#define K\_MBOX\_DEFINE(name) \

4753 STRUCT\_SECTION\_ITERABLE(k\_mbox, name) = \

4754 Z\_MBOX\_INITIALIZER(name) \

4755

4756

[ 4763](group__mailbox__apis.md#ga686f20c199a9e971822d8279d175d8c2)void [k\_mbox\_init](group__mailbox__apis.md#ga686f20c199a9e971822d8279d175d8c2)(struct [k\_mbox](structk__mbox.md) \*mbox);

4764

[ 4784](group__mailbox__apis.md#gaa1e5cdd992d8b9be11f82254e1886ed2)int [k\_mbox\_put](group__mailbox__apis.md#gaa1e5cdd992d8b9be11f82254e1886ed2)(struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*tx\_msg,

4785 [k\_timeout\_t](structk__timeout__t.md) timeout);

4786

[ 4800](group__mailbox__apis.md#gadd60f7b760371c0a141a1e4da253a0f0)void [k\_mbox\_async\_put](group__mailbox__apis.md#gadd60f7b760371c0a141a1e4da253a0f0)(struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*tx\_msg,

4801 struct k\_sem \*sem);

4802

[ 4820](group__mailbox__apis.md#ga2ea91154620b139dbed1ad949b97c3ef)int [k\_mbox\_get](group__mailbox__apis.md#ga2ea91154620b139dbed1ad949b97c3ef)(struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*rx\_msg,

4821 void \*buffer, [k\_timeout\_t](structk__timeout__t.md) timeout);

4822

[ 4836](group__mailbox__apis.md#ga3d19e648e67f109609259543c9a01d6e)void [k\_mbox\_data\_get](group__mailbox__apis.md#ga3d19e648e67f109609259543c9a01d6e)(struct [k\_mbox\_msg](structk__mbox__msg.md) \*rx\_msg, void \*buffer);

4837

4839

4845

[ 4847](structk__pipe.md)struct [k\_pipe](structk__pipe.md) {

[ 4848](structk__pipe.md#acb78995d6b7df28a5452f5d2e88b4dfb) unsigned char \*[buffer](structk__pipe.md#acb78995d6b7df28a5452f5d2e88b4dfb);

[ 4849](structk__pipe.md#aca3472fb8d68f01af4e26b0b88736d64) size\_t [size](structk__pipe.md#aca3472fb8d68f01af4e26b0b88736d64);

[ 4850](structk__pipe.md#a91bedad65285546734b8724811dc6eb8) size\_t [bytes\_used](structk__pipe.md#a91bedad65285546734b8724811dc6eb8);

[ 4851](structk__pipe.md#ae40f81d9c1459fa42f179cbc728aadd0) size\_t [read\_index](structk__pipe.md#ae40f81d9c1459fa42f179cbc728aadd0);

[ 4852](structk__pipe.md#a8f46bd01da0e52e4ee918d9ebe6ad739) size\_t [write\_index](structk__pipe.md#a8f46bd01da0e52e4ee918d9ebe6ad739);

[ 4853](structk__pipe.md#aa2a367a9c8f0be89bcdf1bf6d3b0b875) struct [k\_spinlock](structk__spinlock.md) [lock](structk__pipe.md#aa2a367a9c8f0be89bcdf1bf6d3b0b875);

4854

4855 struct {

[ 4856](structk__pipe.md#a81ab4435d9ca7e5246164fc4fcd9ad59) \_wait\_q\_t [readers](structk__pipe.md#a81ab4435d9ca7e5246164fc4fcd9ad59);

[ 4857](structk__pipe.md#ac61ce23d990cf4cef44a1ecfc5047ccc) \_wait\_q\_t [writers](structk__pipe.md#ac61ce23d990cf4cef44a1ecfc5047ccc);

[ 4858](structk__pipe.md#a2b7ab1aceb3f380c4adfe740d57dbeed) } [wait\_q](structk__pipe.md#a2b7ab1aceb3f380c4adfe740d57dbeed);

4859

4860 Z\_DECL\_POLL\_EVENT

4861

[ 4862](structk__pipe.md#a2ed95fbe24ea20c4f292a66def1d4dde) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structk__pipe.md#a2ed95fbe24ea20c4f292a66def1d4dde);

4863

4864 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)([k\_pipe](structk__pipe.md))

4865

4866#ifdef CONFIG\_OBJ\_CORE\_PIPE

4867 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

4868#endif

4869};

4870

4874#define K\_PIPE\_FLAG\_ALLOC BIT(0)

4875

4876#define Z\_PIPE\_INITIALIZER(obj, pipe\_buffer, pipe\_buffer\_size) \

4877 { \

4878 .buffer = pipe\_buffer, \

4879 .size = pipe\_buffer\_size, \

4880 .bytes\_used = 0, \

4881 .read\_index = 0, \

4882 .write\_index = 0, \

4883 .lock = {}, \

4884 .wait\_q = { \

4885 .readers = Z\_WAIT\_Q\_INIT(&obj.wait\_q.readers), \

4886 .writers = Z\_WAIT\_Q\_INIT(&obj.wait\_q.writers) \

4887 }, \

4888 Z\_POLL\_EVENT\_OBJ\_INIT(obj) \

4889 .flags = 0, \

4890 }

4891

4895

[ 4909](group__pipe__apis.md#gac2256aa00c59e78199be9bdefd61aa52)#define K\_PIPE\_DEFINE(name, pipe\_buffer\_size, pipe\_align) \

4910 static unsigned char \_\_noinit \_\_aligned(pipe\_align) \

4911 \_k\_pipe\_buf\_##name[pipe\_buffer\_size]; \

4912 STRUCT\_SECTION\_ITERABLE(k\_pipe, name) = \

4913 Z\_PIPE\_INITIALIZER(name, \_k\_pipe\_buf\_##name, pipe\_buffer\_size)

4914

[ 4926](group__pipe__apis.md#gae9e807fb63bb7186b87015664f2c762d)void [k\_pipe\_init](group__pipe__apis.md#gae9e807fb63bb7186b87015664f2c762d)(struct [k\_pipe](structk__pipe.md) \*pipe, unsigned char \*buffer, size\_t size);

4927

[ 4939](group__pipe__apis.md#gaad0ab1b97b537da408031e4bcbe04f36)int [k\_pipe\_cleanup](group__pipe__apis.md#gaad0ab1b97b537da408031e4bcbe04f36)(struct [k\_pipe](structk__pipe.md) \*pipe);

4940

[ 4956](group__pipe__apis.md#ga32a902a5d12ca54b17c2b58783214613)\_\_syscall int [k\_pipe\_alloc\_init](group__pipe__apis.md#ga32a902a5d12ca54b17c2b58783214613)(struct [k\_pipe](structk__pipe.md) \*pipe, size\_t size);

4957

[ 4976](group__pipe__apis.md#gaff77638ad7217974a10c23a0a7e336ae)\_\_syscall int [k\_pipe\_put](group__pipe__apis.md#gaff77638ad7217974a10c23a0a7e336ae)(struct [k\_pipe](structk__pipe.md) \*pipe, const void \*data,

4977 size\_t bytes\_to\_write, size\_t \*bytes\_written,

4978 size\_t min\_xfer, [k\_timeout\_t](structk__timeout__t.md) timeout);

4979

[ 4999](group__pipe__apis.md#gada9aaf9a336d98a95441212f4223e9ef)\_\_syscall int [k\_pipe\_get](group__pipe__apis.md#gada9aaf9a336d98a95441212f4223e9ef)(struct [k\_pipe](structk__pipe.md) \*pipe, void \*data,

5000 size\_t bytes\_to\_read, size\_t \*bytes\_read,

5001 size\_t min\_xfer, [k\_timeout\_t](structk__timeout__t.md) timeout);

5002

[ 5011](group__pipe__apis.md#ga21849ebf856532de6e3ea38489071220)\_\_syscall size\_t [k\_pipe\_read\_avail](group__pipe__apis.md#ga21849ebf856532de6e3ea38489071220)(struct [k\_pipe](structk__pipe.md) \*pipe);

5012

[ 5021](group__pipe__apis.md#gaff3ed3e93591d72c60a3640d195998c3)\_\_syscall size\_t [k\_pipe\_write\_avail](group__pipe__apis.md#gaff3ed3e93591d72c60a3640d195998c3)(struct [k\_pipe](structk__pipe.md) \*pipe);

5022

[ 5033](group__pipe__apis.md#ga41484bb5c7dcd97e7a7b7f1422f8026f)\_\_syscall void [k\_pipe\_flush](group__pipe__apis.md#ga41484bb5c7dcd97e7a7b7f1422f8026f)(struct [k\_pipe](structk__pipe.md) \*pipe);

5034

[ 5046](group__pipe__apis.md#ga71e0e38a15fa27f27c1f028223936445)\_\_syscall void [k\_pipe\_buffer\_flush](group__pipe__apis.md#ga71e0e38a15fa27f27c1f028223936445)(struct [k\_pipe](structk__pipe.md) \*pipe);

5047

5049

5053

5054struct k\_mem\_slab\_info {

5055 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks;

5056 size\_t block\_size;

5057 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_used;

5058#ifdef CONFIG\_MEM\_SLAB\_TRACE\_MAX\_UTILIZATION

5059 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_used;

5060#endif

5061};

5062

5063struct k\_mem\_slab {

5064 \_wait\_q\_t wait\_q;

5065 struct k\_spinlock lock;

5066 char \*buffer;

5067 char \*free\_list;

5068 struct k\_mem\_slab\_info info;

5069

5070 [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(k\_mem\_slab)

5071

5072#ifdef CONFIG\_OBJ\_CORE\_MEM\_SLAB

5073 struct k\_obj\_core obj\_core;

5074#endif

5075};

5076

5077#define Z\_MEM\_SLAB\_INITIALIZER(\_slab, \_slab\_buffer, \_slab\_block\_size, \

5078 \_slab\_num\_blocks) \

5079 { \

5080 .wait\_q = Z\_WAIT\_Q\_INIT(&(\_slab).wait\_q), \

5081 .lock = {}, \

5082 .buffer = \_slab\_buffer, \

5083 .free\_list = NULL, \

5084 .info = {\_slab\_num\_blocks, \_slab\_block\_size, 0} \

5085 }

5086

5087

5091

5097

[ 5121](group__mem__slab__apis.md#ga60bc92eee58fcc5f121b8e4d82eaa69e)#define K\_MEM\_SLAB\_DEFINE(name, slab\_block\_size, slab\_num\_blocks, slab\_align) \

5122 char \_\_noinit\_named(k\_mem\_slab\_buf\_##name) \

5123 \_\_aligned(WB\_UP(slab\_align)) \

5124 \_k\_mem\_slab\_buf\_##name[(slab\_num\_blocks) \* WB\_UP(slab\_block\_size)]; \

5125 STRUCT\_SECTION\_ITERABLE(k\_mem\_slab, name) = \

5126 Z\_MEM\_SLAB\_INITIALIZER(name, \_k\_mem\_slab\_buf\_##name, \

5127 WB\_UP(slab\_block\_size), slab\_num\_blocks)

5128

[ 5143](group__mem__slab__apis.md#ga90bdbb15f410991f54ba16025c24bc3c)#define K\_MEM\_SLAB\_DEFINE\_STATIC(name, slab\_block\_size, slab\_num\_blocks, slab\_align) \

5144 static char \_\_noinit\_named(k\_mem\_slab\_buf\_##name) \

5145 \_\_aligned(WB\_UP(slab\_align)) \

5146 \_k\_mem\_slab\_buf\_##name[(slab\_num\_blocks) \* WB\_UP(slab\_block\_size)]; \

5147 static STRUCT\_SECTION\_ITERABLE(k\_mem\_slab, name) = \

5148 Z\_MEM\_SLAB\_INITIALIZER(name, \_k\_mem\_slab\_buf\_##name, \

5149 WB\_UP(slab\_block\_size), slab\_num\_blocks)

5150

[ 5172](group__mem__slab__apis.md#ga094a8f173f287e29bb287119c26889d1)int [k\_mem\_slab\_init](group__mem__slab__apis.md#ga094a8f173f287e29bb287119c26889d1)(struct k\_mem\_slab \*slab, void \*buffer,

5173 size\_t block\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks);

5174

[ 5197](group__mem__slab__apis.md#gab16a46d8394aca18de740ad044a8734a)int [k\_mem\_slab\_alloc](group__mem__slab__apis.md#gab16a46d8394aca18de740ad044a8734a)(struct k\_mem\_slab \*slab, void \*\*mem,

5198 [k\_timeout\_t](structk__timeout__t.md) timeout);

5199

[ 5209](group__mem__slab__apis.md#ga2635ea8f9a30b8751ec966fe62adc0e1)void [k\_mem\_slab\_free](group__mem__slab__apis.md#ga2635ea8f9a30b8751ec966fe62adc0e1)(struct k\_mem\_slab \*slab, void \*mem);

5210

[ 5221](group__mem__slab__apis.md#gac76b96d7055e4ad94765c93530dd0720)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_mem\_slab\_num\_used\_get](group__mem__slab__apis.md#gac76b96d7055e4ad94765c93530dd0720)(struct k\_mem\_slab \*slab)

5222{

5223 return slab->info.num\_used;

5224}

5225

[ 5236](group__mem__slab__apis.md#gae0e949c1c3476dd57bc0c0ed627d2346)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_mem\_slab\_max\_used\_get](group__mem__slab__apis.md#gae0e949c1c3476dd57bc0c0ed627d2346)(struct k\_mem\_slab \*slab)

5237{

5238#ifdef CONFIG\_MEM\_SLAB\_TRACE\_MAX\_UTILIZATION

5239 return slab->info.max\_used;

5240#else

5241 ARG\_UNUSED(slab);

5242 return 0;

5243#endif

5244}

5245

[ 5256](group__mem__slab__apis.md#gae87577e2873cf746db69216a82f94aea)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_mem\_slab\_num\_free\_get](group__mem__slab__apis.md#gae87577e2873cf746db69216a82f94aea)(struct k\_mem\_slab \*slab)

5257{

5258 return slab->info.num\_blocks - slab->info.num\_used;

5259}

5260

5272

[ 5273](group__mem__slab__apis.md#ga32030a5cfb44f663bd31b4e1b3d5dddb)int [k\_mem\_slab\_runtime\_stats\_get](group__mem__slab__apis.md#ga32030a5cfb44f663bd31b4e1b3d5dddb)(struct k\_mem\_slab \*slab, struct [sys\_memory\_stats](structsys__memory__stats.md) \*stats);

5274

[ 5286](group__mem__slab__apis.md#gaa1f44e30f4aee98b38e1ab5e93af505c)int [k\_mem\_slab\_runtime\_stats\_reset\_max](group__mem__slab__apis.md#gaa1f44e30f4aee98b38e1ab5e93af505c)(struct k\_mem\_slab \*slab);

5287

5289

5294

5295/\* kernel synchronized heap struct \*/

5296

[ 5297](structk__heap.md)struct [k\_heap](structk__heap.md) {

[ 5298](structk__heap.md#a4b8551f4fd1cd648c68f47ea2ebd682f) struct [sys\_heap](structsys__heap.md) [heap](structk__heap.md#a4b8551f4fd1cd648c68f47ea2ebd682f);

[ 5299](structk__heap.md#abd30d236bd986e791ea7698583e45588) \_wait\_q\_t [wait\_q](structk__heap.md#abd30d236bd986e791ea7698583e45588);

[ 5300](structk__heap.md#a3bd15b8ad69a6ab76b5c4a297673e5ec) struct [k\_spinlock](structk__spinlock.md) [lock](structk__heap.md#a3bd15b8ad69a6ab76b5c4a297673e5ec);

5301};

5302

[ 5316](group__heap__apis.md#ga9273e06dc8d6a351499f2f5abfdcb39f)void [k\_heap\_init](group__heap__apis.md#ga9273e06dc8d6a351499f2f5abfdcb39f)(struct [k\_heap](structk__heap.md) \*h, void \*mem,

5317 size\_t bytes) \_\_attribute\_nonnull(1);

5318

[ 5338](group__heap__apis.md#gaf77211a72441de389857bc13e10be4e6)void \*[k\_heap\_aligned\_alloc](group__heap__apis.md#gaf77211a72441de389857bc13e10be4e6)(struct [k\_heap](structk__heap.md) \*h, size\_t align, size\_t bytes,

5339 [k\_timeout\_t](structk__timeout__t.md) timeout) \_\_attribute\_nonnull(1);

5340

[ 5362](group__heap__apis.md#ga22b83564e50ae6177388dfe63e32a512)void \*[k\_heap\_alloc](group__heap__apis.md#ga22b83564e50ae6177388dfe63e32a512)(struct [k\_heap](structk__heap.md) \*h, size\_t bytes,

5363 [k\_timeout\_t](structk__timeout__t.md) timeout) \_\_attribute\_nonnull(1);

5364

[ 5375](group__heap__apis.md#ga6cf917a0b3d91a0101192bd4808ada9c)void [k\_heap\_free](group__heap__apis.md#ga6cf917a0b3d91a0101192bd4808ada9c)(struct [k\_heap](structk__heap.md) \*h, void \*mem) \_\_attribute\_nonnull(1);

5376

5377/\* Hand-calculated minimum heap sizes needed to return a successful

5378 \* 1-byte allocation. See details in lib/os/heap.[ch]

5379 \*/

5380#define Z\_HEAP\_MIN\_SIZE (sizeof(void \*) > 4 ? 56 : 44)

5381

5398#define Z\_HEAP\_DEFINE\_IN\_SECT(name, bytes, in\_section) \

5399 char in\_section \

5400 \_\_aligned(8) /\* CHUNK\_UNIT \*/ \

5401 kheap\_##name[MAX(bytes, Z\_HEAP\_MIN\_SIZE)]; \

5402 STRUCT\_SECTION\_ITERABLE(k\_heap, name) = { \

5403 .heap = { \

5404 .init\_mem = kheap\_##name, \

5405 .init\_bytes = MAX(bytes, Z\_HEAP\_MIN\_SIZE), \

5406 }, \

5407 }

5408

[ 5423](group__heap__apis.md#ga795d7f1e6d5b7b19a7a50198d7829a0f)#define K\_HEAP\_DEFINE(name, bytes) \

5424 Z\_HEAP\_DEFINE\_IN\_SECT(name, bytes, \

5425 \_\_noinit\_named(kheap\_buf\_##name))

5426

[ 5441](group__heap__apis.md#ga968f4c6a201fdf6862d62dd5d9f8d032)#define K\_HEAP\_DEFINE\_NOCACHE(name, bytes) \

5442 Z\_HEAP\_DEFINE\_IN\_SECT(name, bytes, \_\_nocache)

5443

5447

5453

[ 5472](group__heap__apis.md#gae16d486aa250f9c07fa6a57342bcd3b4)void \*[k\_aligned\_alloc](group__heap__apis.md#gae16d486aa250f9c07fa6a57342bcd3b4)(size\_t align, size\_t size);

5473

[ 5485](group__heap__apis.md#gaa8edf1e63e5d5dd78d7adcfd787394ee)void \*[k\_malloc](group__heap__apis.md#gaa8edf1e63e5d5dd78d7adcfd787394ee)(size\_t size);

5486

[ 5497](group__heap__apis.md#ga79b63cc93b3358cf82d74f40e73b69d5)void [k\_free](group__heap__apis.md#ga79b63cc93b3358cf82d74f40e73b69d5)(void \*ptr);

5498

[ 5510](group__heap__apis.md#gad031d50ed62d08202a5dcf992c20246c)void \*[k\_calloc](group__heap__apis.md#gad031d50ed62d08202a5dcf992c20246c)(size\_t nmemb, size\_t size);

5511

5513

5514/\* polling API - PRIVATE \*/

5515

5516#ifdef CONFIG\_POLL

5517#define \_INIT\_OBJ\_POLL\_EVENT(obj) do { (obj)->poll\_event = NULL; } while (false)

5518#else

5519#define \_INIT\_OBJ\_POLL\_EVENT(obj) do { } while (false)

5520#endif

5521

5522/\* private - types bit positions \*/

5523enum \_poll\_types\_bits {

5524 /\* can be used to ignore an event \*/

5525 \_POLL\_TYPE\_IGNORE,

5526

5527 /\* to be signaled by k\_poll\_signal\_raise() \*/

5528 \_POLL\_TYPE\_SIGNAL,

5529

5530 /\* semaphore availability \*/

5531 \_POLL\_TYPE\_SEM\_AVAILABLE,

5532

5533 /\* queue/FIFO/LIFO data availability \*/

5534 \_POLL\_TYPE\_DATA\_AVAILABLE,

5535

5536 /\* msgq data availability \*/

5537 \_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE,

5538

5539 /\* pipe data availability \*/

5540 \_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE,

5541

5542 \_POLL\_NUM\_TYPES

5543};

5544

5545#define Z\_POLL\_TYPE\_BIT(type) (1U << ((type) - 1U))

5546

5547/\* private - states bit positions \*/

5548enum \_poll\_states\_bits {

5549 /\* default state when creating event \*/

5550 \_POLL\_STATE\_NOT\_READY,

5551

5552 /\* signaled by k\_poll\_signal\_raise() \*/

5553 \_POLL\_STATE\_SIGNALED,

5554

5555 /\* semaphore is available \*/

5556 \_POLL\_STATE\_SEM\_AVAILABLE,

5557

5558 /\* data is available to read on queue/FIFO/LIFO \*/

5559 \_POLL\_STATE\_DATA\_AVAILABLE,

5560

5561 /\* queue/FIFO/LIFO wait was cancelled \*/

5562 \_POLL\_STATE\_CANCELLED,

5563

5564 /\* data is available to read on a message queue \*/

5565 \_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE,

5566

5567 /\* data is available to read from a pipe \*/

5568 \_POLL\_STATE\_PIPE\_DATA\_AVAILABLE,

5569

5570 \_POLL\_NUM\_STATES

5571};

5572

5573#define Z\_POLL\_STATE\_BIT(state) (1U << ((state) - 1U))

5574

5575#define \_POLL\_EVENT\_NUM\_UNUSED\_BITS \

5576 (32 - (0 \

5577 + 8 /\* tag \*/ \

5578 + \_POLL\_NUM\_TYPES \

5579 + \_POLL\_NUM\_STATES \

5580 + 1 /\* modes \*/ \

5581 ))

5582

5583/\* end of polling API - PRIVATE \*/

5584

5585

5591

5592/\* Public polling API \*/

5593

5594/\* public - values for k\_poll\_event.type bitfield \*/

[ 5595](group__poll__apis.md#gafd5d801eb9e9cf6097b2c08b4933998e)#define K\_POLL\_TYPE\_IGNORE 0

[ 5596](group__poll__apis.md#ga144d8eb34d85f6053e454410a10bf56a)#define K\_POLL\_TYPE\_SIGNAL Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_SIGNAL)

[ 5597](group__poll__apis.md#ga0fd7605bdffd43dff7480a90a603ffde)#define K\_POLL\_TYPE\_SEM\_AVAILABLE Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_SEM\_AVAILABLE)

[ 5598](group__poll__apis.md#ga58d656f73f031a39b8a936133fe5504f)#define K\_POLL\_TYPE\_DATA\_AVAILABLE Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_DATA\_AVAILABLE)

[ 5599](group__poll__apis.md#ga71734fee18c523cf70276260118afb91)#define K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE K\_POLL\_TYPE\_DATA\_AVAILABLE

[ 5600](group__poll__apis.md#gaa83509b54175fb6c98324422a928d5e1)#define K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE)

[ 5601](group__poll__apis.md#ga14e113201a3b3ad768c6a5ce917d1912)#define K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE)

5602

5603/\* public - polling modes \*/

[ 5604](group__poll__apis.md#ga36d7978872a83191dd3cc16d62165add)enum [k\_poll\_modes](group__poll__apis.md#ga36d7978872a83191dd3cc16d62165add) {

5605 /\* polling thread does not take ownership of objects when available \*/

[ 5606](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda22874743e2f6b0f1fd55c5375732b681) [K\_POLL\_MODE\_NOTIFY\_ONLY](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda22874743e2f6b0f1fd55c5375732b681) = 0,

5607

[ 5608](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c) [K\_POLL\_NUM\_MODES](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c)

5609};

5610

5611/\* public - values for k\_poll\_event.state bitfield \*/

[ 5612](group__poll__apis.md#ga522822c5e06a89b22ce4dcefd10c66aa)#define K\_POLL\_STATE\_NOT\_READY 0

[ 5613](group__poll__apis.md#ga478aae7fe4fb5c7b7c76ed216c22a7f1)#define K\_POLL\_STATE\_SIGNALED Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_SIGNALED)

[ 5614](group__poll__apis.md#gae9e3eefd5a29a538d22f53592578bb37)#define K\_POLL\_STATE\_SEM\_AVAILABLE Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_SEM\_AVAILABLE)

[ 5615](group__poll__apis.md#gac166d9919d591bace163c5211e7b41f4)#define K\_POLL\_STATE\_DATA\_AVAILABLE Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_DATA\_AVAILABLE)

[ 5616](group__poll__apis.md#gabd5ac3341698534f39ded718079d6168)#define K\_POLL\_STATE\_FIFO\_DATA\_AVAILABLE K\_POLL\_STATE\_DATA\_AVAILABLE

[ 5617](group__poll__apis.md#gac236074cd43f59f28b803fe2c4a4f6f7)#define K\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE)

[ 5618](group__poll__apis.md#ga9028d6868ee964ca25931ed9170068dd)#define K\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE)

[ 5619](group__poll__apis.md#gadaf4b4c8e13afb54114af72d133e1fdb)#define K\_POLL\_STATE\_CANCELLED Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_CANCELLED)

5620

5621/\* public - poll signal object \*/

[ 5622](structk__poll__signal.md)struct [k\_poll\_signal](structk__poll__signal.md) {

[ 5624](structk__poll__signal.md#a22e88955ba0e369d39edefadcf4c60fd) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [poll\_events](structk__poll__signal.md#a22e88955ba0e369d39edefadcf4c60fd);

5625

[ 5630](structk__poll__signal.md#ae9fe6751d75f7d2b2800cb723603c0fe) unsigned int [signaled](structk__poll__signal.md#ae9fe6751d75f7d2b2800cb723603c0fe);

5631

[ 5633](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1) int [result](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1);

5634};

5635

[ 5636](group__poll__apis.md#ga6d6321e189afca73a276cd671ec531ae)#define K\_POLL\_SIGNAL\_INITIALIZER(obj) \

5637 { \

5638 .poll\_events = SYS\_DLIST\_STATIC\_INIT(&obj.poll\_events), \

5639 .signaled = 0, \

5640 .result = 0, \

5641 }

5642

[ 5646](structk__poll__event.md)struct [k\_poll\_event](structk__poll__event.md) {

5648 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \_node;

5649

[ 5651](structk__poll__event.md#ad030c37b97f33e1bbb3361057180fa4f) struct z\_poller \*[poller](structk__poll__event.md#ad030c37b97f33e1bbb3361057180fa4f);

5652

[ 5654](structk__poll__event.md#a37c5f45deaa046b356d95af569220c70) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tag](structk__poll__event.md#a37c5f45deaa046b356d95af569220c70):8;

5655

[ 5657](structk__poll__event.md#a8f9e251aa8722eb4716f622e85be34ae) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [type](structk__poll__event.md#a8f9e251aa8722eb4716f622e85be34ae):\_POLL\_NUM\_TYPES;

5658

[ 5660](structk__poll__event.md#aaf4f32852d799a406bfeea4e57891129) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](structk__poll__event.md#aaf4f32852d799a406bfeea4e57891129):\_POLL\_NUM\_STATES;

5661

[ 5663](structk__poll__event.md#acca81763486ef5ebcc911cb1cbd6c899) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mode](structk__poll__event.md#acca81763486ef5ebcc911cb1cbd6c899):1;

5664

[ 5666](structk__poll__event.md#a750ac48e7aa3c8fb70814b24e951fc85) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unused](structk__poll__event.md#a750ac48e7aa3c8fb70814b24e951fc85):\_POLL\_EVENT\_NUM\_UNUSED\_BITS;

5667

5669 union {

[ 5670](structk__poll__event.md#aeaf67f9bc91d59fb2939e1469a088f2d) void \*[obj](structk__poll__event.md#aeaf67f9bc91d59fb2939e1469a088f2d);

[ 5671](structk__poll__event.md#a130aaff7a8908993ed6be737a94a52ab) struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](structk__poll__event.md#a130aaff7a8908993ed6be737a94a52ab);

[ 5672](structk__poll__event.md#a9ed342b8a45884f985245f55b0e1c8cc) struct k\_sem \*[sem](structk__poll__event.md#a9ed342b8a45884f985245f55b0e1c8cc);

[ 5673](structk__poll__event.md#a4ba07f42f4af03f30478ebf48a1653f7) struct [k\_fifo](structk__fifo.md) \*[fifo](structk__poll__event.md#a4ba07f42f4af03f30478ebf48a1653f7);

[ 5674](structk__poll__event.md#a6e30a6ce30702817895e66f22f0abedf) struct [k\_queue](structk__queue.md) \*[queue](structk__poll__event.md#a6e30a6ce30702817895e66f22f0abedf);

[ 5675](structk__poll__event.md#a5bbe94482a70ec13c2106f89afd2d59c) struct [k\_msgq](structk__msgq.md) \*[msgq](structk__poll__event.md#a5bbe94482a70ec13c2106f89afd2d59c);

5676#ifdef CONFIG\_PIPES

5677 struct [k\_pipe](structk__pipe.md) \*pipe;

5678#endif

5679 };

5680};

5681

[ 5682](group__poll__apis.md#ga8e3889f2bac281a6e65e31068e58047e)#define K\_POLL\_EVENT\_INITIALIZER(\_event\_type, \_event\_mode, \_event\_obj) \

5683 { \

5684 .poller = NULL, \

5685 .type = \_event\_type, \

5686 .state = K\_POLL\_STATE\_NOT\_READY, \

5687 .mode = \_event\_mode, \

5688 .unused = 0, \

5689 { \

5690 .obj = \_event\_obj, \

5691 }, \

5692 }

5693

[ 5694](group__poll__apis.md#gada2366896d913dc916b3c28642648b63)#define K\_POLL\_EVENT\_STATIC\_INITIALIZER(\_event\_type, \_event\_mode, \_event\_obj, \

5695 event\_tag) \

5696 { \

5697 .tag = event\_tag, \

5698 .type = \_event\_type, \

5699 .state = K\_POLL\_STATE\_NOT\_READY, \

5700 .mode = \_event\_mode, \

5701 .unused = 0, \

5702 { \

5703 .obj = \_event\_obj, \

5704 }, \

5705 }

5706

5721

[ 5722](group__poll__apis.md#gaa06bddd93a024fc5326d93187d80eb03)void [k\_poll\_event\_init](group__poll__apis.md#gaa06bddd93a024fc5326d93187d80eb03)(struct [k\_poll\_event](structk__poll__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type,

5723 int mode, void \*obj);

5724

5767

[ 5768](group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db)\_\_syscall int [k\_poll](group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db)(struct [k\_poll\_event](structk__poll__event.md) \*events, int num\_events,

5769 [k\_timeout\_t](structk__timeout__t.md) timeout);

5770

5778

[ 5779](group__poll__apis.md#gaee3090c2a912b93b6a5855e3018c3551)\_\_syscall void [k\_poll\_signal\_init](group__poll__apis.md#gaee3090c2a912b93b6a5855e3018c3551)(struct [k\_poll\_signal](structk__poll__signal.md) \*sig);

5780

5781/\*

5782 \* @brief Reset a poll signal object's state to unsignaled.

5783 \*

5784 \* @param sig A poll signal object

5785 \*/

[ 5786](group__poll__apis.md#ga02d899d1455ae1f3f55ffe8f1ebd6994)\_\_syscall void [k\_poll\_signal\_reset](group__poll__apis.md#ga02d899d1455ae1f3f55ffe8f1ebd6994)(struct [k\_poll\_signal](structk__poll__signal.md) \*sig);

5787

[ 5798](group__poll__apis.md#ga69dae11c7cb2c669caa411c3e7001311)\_\_syscall void [k\_poll\_signal\_check](group__poll__apis.md#ga69dae11c7cb2c669caa411c3e7001311)(struct [k\_poll\_signal](structk__poll__signal.md) \*sig,

5799 unsigned int \*signaled, int \*result);

5800

5824

[ 5825](group__poll__apis.md#gad0bf3825f828ec3ca37481bf3cbd6723)\_\_syscall int [k\_poll\_signal\_raise](group__poll__apis.md#gad0bf3825f828ec3ca37481bf3cbd6723)(struct [k\_poll\_signal](structk__poll__signal.md) \*sig, int result);

5826

5828

[ 5847](group__cpu__idle__apis.md#ga7b25e1bed511a813b32fbd0f91b09356)static inline void [k\_cpu\_idle](group__cpu__idle__apis.md#ga7b25e1bed511a813b32fbd0f91b09356)(void)

5848{

5849 [arch\_cpu\_idle](group__arch-pm.md#ga6ce051203e6cc091d0fb42a15f662a48)();

5850}

5851

[ 5866](group__cpu__idle__apis.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f)static inline void [k\_cpu\_atomic\_idle](group__cpu__idle__apis.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f)(unsigned int key)

5867{

5868 [arch\_cpu\_atomic\_idle](group__arch-pm.md#ga4d0297717c23a3cc5df434549e26924d)(key);

5869}

5870

5874

5879#ifdef ARCH\_EXCEPT

5880/\* This architecture has direct support for triggering a CPU exception \*/

5881#define z\_except\_reason(reason) ARCH\_EXCEPT(reason)

5882#else

5883

5884#if !defined(CONFIG\_ASSERT\_NO\_FILE\_INFO)

5885#define \_\_EXCEPT\_LOC() \_\_ASSERT\_PRINT("@ %s:%d\n", \_\_FILE\_\_, \_\_LINE\_\_)

5886#else

5887#define \_\_EXCEPT\_LOC()

5888#endif

5889

5890/\* NOTE: This is the implementation for arches that do not implement

5891 \* ARCH\_EXCEPT() to generate a real CPU exception.

5892 \*

5893 \* We won't have a real exception frame to determine the PC value when

5894 \* the oops occurred, so print file and line number before we jump into

5895 \* the fatal error handler.

5896 \*/

5897#define z\_except\_reason(reason) do { \

5898 \_\_EXCEPT\_LOC(); \

5899 z\_fatal\_error(reason, NULL); \

5900 } while (false)

5901

5902#endif /\* \_ARCH\_\_EXCEPT \*/

5906

[ 5918](include_2zephyr_2kernel_8h.md#abde5aa8ca5e64a045b25b88f91370dcd)#define k\_oops() z\_except\_reason(K\_ERR\_KERNEL\_OOPS)

5919

[ 5928](include_2zephyr_2kernel_8h.md#aedd541f707b1463aaac15c7798340329)#define k\_panic() z\_except\_reason(K\_ERR\_KERNEL\_PANIC)

5929

5933

5934/\*

5935 \* private APIs that are utilized by one or more public APIs

5936 \*/

5937

5941#ifdef CONFIG\_MULTITHREADING

5945void z\_init\_static\_threads(void);

5946#else

5950#define z\_init\_static\_threads() do { } while (false)

5951#endif

5952

5956void z\_timer\_expiration\_handler(struct \_timeout \*t);

5960

5961#ifdef CONFIG\_PRINTK

5969\_\_syscall void k\_str\_out(char \*c, size\_t n);

5970#endif

5971

5977

[ 5998](group__float__apis.md#ga2df4b2550ace30512cddebd36b6a54a1)\_\_syscall int [k\_float\_disable](group__float__apis.md#ga2df4b2550ace30512cddebd36b6a54a1)(struct [k\_thread](structk__thread.md) \*thread);

5999

[ 6038](group__float__apis.md#ga81fb955ddd41658a9aad5c083f173f77)\_\_syscall int [k\_float\_enable](group__float__apis.md#ga81fb955ddd41658a9aad5c083f173f77)(struct [k\_thread](structk__thread.md) \*thread, unsigned int options);

6039

6043

[ 6051](include_2zephyr_2kernel_8h.md#a82d886a1c911b39c1b47c32200cedac6)int [k\_thread\_runtime\_stats\_get](include_2zephyr_2kernel_8h.md#a82d886a1c911b39c1b47c32200cedac6)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread,

6052 [k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) \*stats);

6053

[ 6060](include_2zephyr_2kernel_8h.md#abd855bb83b3be393b46833e7854a193e)int [k\_thread\_runtime\_stats\_all\_get](include_2zephyr_2kernel_8h.md#abd855bb83b3be393b46833e7854a193e)([k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) \*stats);

6061

[ 6071](include_2zephyr_2kernel_8h.md#a3e52beb93fca2231d5860fe1cf1181fd)int [k\_thread\_runtime\_stats\_enable](include_2zephyr_2kernel_8h.md#a3e52beb93fca2231d5860fe1cf1181fd)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

6072

[ 6082](include_2zephyr_2kernel_8h.md#ae5ea2e05a602b7d5ee78a65ced61d63b)int [k\_thread\_runtime\_stats\_disable](include_2zephyr_2kernel_8h.md#ae5ea2e05a602b7d5ee78a65ced61d63b)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

6083

[ 6091](include_2zephyr_2kernel_8h.md#a54f2652ba1ed613219941eaaf193180c)void [k\_sys\_runtime\_stats\_enable](include_2zephyr_2kernel_8h.md#a54f2652ba1ed613219941eaaf193180c)(void);

6092

[ 6100](include_2zephyr_2kernel_8h.md#a2e3c96c0b11108ee7eca3f0666c780e0)void [k\_sys\_runtime\_stats\_disable](include_2zephyr_2kernel_8h.md#a2e3c96c0b11108ee7eca3f0666c780e0)(void);

6101

6102#ifdef \_\_cplusplus

6103}

6104#endif

6105

6106#include <[zephyr/tracing/tracing.h](tracing_2tracing_8h.md)>

6107#include <[syscalls/kernel.h](subsys_2testsuite_2ztest_2include_2zephyr_2syscalls_2kernel_8h.md)>

6108

6109#endif /\* !\_ASMLANGUAGE \*/

6110

6111#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_H\_ \*/

[k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717)

void(\* k\_thread\_entry\_t)(void \*p1, void \*p2, void \*p3)

Thread entry point function type.

**Definition** arch\_interface.h:47

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:45

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

[arch\_k\_cycle\_get\_32](group__arch-timing.md#ga9ee9f897ec750957de45bf8d43349d5e)

static uint32\_t arch\_k\_cycle\_get\_32(void)

Obtain the current cycle count, in units specified by CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC.

[arch\_k\_cycle\_get\_64](group__arch-timing.md#gacc1ed8d949f694a1d39e389334caf971)

static uint64\_t arch\_k\_cycle\_get\_64(void)

As for arch\_k\_cycle\_get\_32(), but with a 64 bit return value.

[atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)

static bool atomic\_test\_bit(const atomic\_t \*target, int bit)

Atomically test a bit.

**Definition** atomic.h:127

[atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)

static void atomic\_clear\_bit(atomic\_t \*target, int bit)

Atomically clear a bit.

**Definition** atomic.h:191

[atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)

static bool atomic\_test\_and\_set\_bit(atomic\_t \*target, int bit)

Atomically set a bit.

**Definition** atomic.h:170

[k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)

static uint32\_t k\_cycle\_get\_32(void)

Read the hardware clock.

**Definition** kernel.h:1805

[K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)

#define K\_NO\_WAIT

Generate null timeout delay.

**Definition** kernel.h:1251

[k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)

int64\_t k\_uptime\_ticks(void)

Get system uptime, in system ticks.

[k\_uptime\_get\_32](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b)

static uint32\_t k\_uptime\_get\_32(void)

Get system uptime (32-bit version).

**Definition** kernel.h:1770

[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2)

uint32\_t k\_ticks\_t

Tick precision used in timeout APIs.

**Definition** sys\_clock.h:48

[k\_uptime\_delta](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80)

static int64\_t k\_uptime\_delta(int64\_t \*reftime)

Get elapsed time.

**Definition** kernel.h:1786

[k\_cycle\_get\_64](group__clock__apis.md#gae09f509d02bf75a7b45d2800d823bb3a)

static uint64\_t k\_cycle\_get\_64(void)

Read the 64-bit hardware clock.

**Definition** kernel.h:1820

[k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)

static int64\_t k\_uptime\_get(void)

Get system uptime.

**Definition** kernel.h:1746

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

**Definition** kernel.h:5847

[k\_cpu\_atomic\_idle](group__cpu__idle__apis.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f)

static void k\_cpu\_atomic\_idle(unsigned int key)

Make the CPU idle in an atomic fashion.

**Definition** kernel.h:5866

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:55

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:51

[k\_event\_wait](group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753)

uint32\_t k\_event\_wait(struct k\_event \*event, uint32\_t events, bool reset, k\_timeout\_t timeout)

Wait for any of the specified events.

[k\_event\_set\_masked](group__event__apis.md#ga29b3ec1022b12a8c34884da3559c5864)

uint32\_t k\_event\_set\_masked(struct k\_event \*event, uint32\_t events, uint32\_t events\_mask)

Set or clear the events in an event object.

[k\_event\_test](group__event__apis.md#ga81e66be0959e8cb0414d9772056a6264)

static uint32\_t k\_event\_test(struct k\_event \*event, uint32\_t events\_mask)

Test the events currently tracked in the event object.

**Definition** kernel.h:2354

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

**Definition** sflist.h:60

[sys\_sflist\_is\_empty](group__flagged-single-linked-list__apis.md#gac506235a9df89a7a52631e9990ceaad5)

static bool sys\_sflist\_is\_empty(sys\_sflist\_t \*list)

Test if the given list is empty.

**Definition** sflist.h:335

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

[k\_heap\_free](group__heap__apis.md#ga6cf917a0b3d91a0101192bd4808ada9c)

void k\_heap\_free(struct k\_heap \*h, void \*mem)

Free memory allocated by k\_heap\_alloc().

[k\_free](group__heap__apis.md#ga79b63cc93b3358cf82d74f40e73b69d5)

void k\_free(void \*ptr)

Free memory allocated from heap.

[k\_heap\_init](group__heap__apis.md#ga9273e06dc8d6a351499f2f5abfdcb39f)

void k\_heap\_init(struct k\_heap \*h, void \*mem, size\_t bytes)

Initialize a k\_heap.

[k\_malloc](group__heap__apis.md#gaa8edf1e63e5d5dd78d7adcfd787394ee)

void \* k\_malloc(size\_t size)

Allocate memory from the heap.

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

**Definition** kernel.h:1106

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

**Definition** kernel.h:5221

[k\_mem\_slab\_max\_used\_get](group__mem__slab__apis.md#gae0e949c1c3476dd57bc0c0ed627d2346)

static uint32\_t k\_mem\_slab\_max\_used\_get(struct k\_mem\_slab \*slab)

Get the number of maximum used blocks so far in a memory slab.

**Definition** kernel.h:5236

[k\_mem\_slab\_num\_free\_get](group__mem__slab__apis.md#gae87577e2873cf746db69216a82f94aea)

static uint32\_t k\_mem\_slab\_num\_free\_get(struct k\_mem\_slab \*slab)

Get the number of unused blocks in a memory slab.

**Definition** kernel.h:5256

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

[k\_pipe\_read\_avail](group__pipe__apis.md#ga21849ebf856532de6e3ea38489071220)

size\_t k\_pipe\_read\_avail(struct k\_pipe \*pipe)

Query the number of bytes that may be read from pipe.

[k\_pipe\_alloc\_init](group__pipe__apis.md#ga32a902a5d12ca54b17c2b58783214613)

int k\_pipe\_alloc\_init(struct k\_pipe \*pipe, size\_t size)

Initialize a pipe and allocate a buffer for it.

[k\_pipe\_flush](group__pipe__apis.md#ga41484bb5c7dcd97e7a7b7f1422f8026f)

void k\_pipe\_flush(struct k\_pipe \*pipe)

Flush the pipe of write data.

[k\_pipe\_buffer\_flush](group__pipe__apis.md#ga71e0e38a15fa27f27c1f028223936445)

void k\_pipe\_buffer\_flush(struct k\_pipe \*pipe)

Flush the pipe's internal buffer.

[k\_pipe\_cleanup](group__pipe__apis.md#gaad0ab1b97b537da408031e4bcbe04f36)

int k\_pipe\_cleanup(struct k\_pipe \*pipe)

Release a pipe's allocated buffer.

[k\_pipe\_get](group__pipe__apis.md#gada9aaf9a336d98a95441212f4223e9ef)

int k\_pipe\_get(struct k\_pipe \*pipe, void \*data, size\_t bytes\_to\_read, size\_t \*bytes\_read, size\_t min\_xfer, k\_timeout\_t timeout)

Read data from a pipe.

[k\_pipe\_init](group__pipe__apis.md#gae9e807fb63bb7186b87015664f2c762d)

void k\_pipe\_init(struct k\_pipe \*pipe, unsigned char \*buffer, size\_t size)

Initialize a pipe.

[k\_pipe\_write\_avail](group__pipe__apis.md#gaff3ed3e93591d72c60a3640d195998c3)

size\_t k\_pipe\_write\_avail(struct k\_pipe \*pipe)

Query the number of bytes that may be written to pipe.

[k\_pipe\_put](group__pipe__apis.md#gaff77638ad7217974a10c23a0a7e336ae)

int k\_pipe\_put(struct k\_pipe \*pipe, const void \*data, size\_t bytes\_to\_write, size\_t \*bytes\_written, size\_t min\_xfer, k\_timeout\_t timeout)

Write data to a pipe.

[k\_poll\_signal\_reset](group__poll__apis.md#ga02d899d1455ae1f3f55ffe8f1ebd6994)

void k\_poll\_signal\_reset(struct k\_poll\_signal \*sig)

[k\_poll\_modes](group__poll__apis.md#ga36d7978872a83191dd3cc16d62165add)

k\_poll\_modes

**Definition** kernel.h:5604

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

**Definition** kernel.h:5606

[K\_POLL\_NUM\_MODES](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c)

@ K\_POLL\_NUM\_MODES

**Definition** kernel.h:5608

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

**Definition** tracing\_macros.h:354

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)

#define CONTAINER\_OF(ptr, type, field)

Get a pointer to a structure containing the element.

**Definition** util.h:265

[EBUSY](group__system__errno.md#ga8368025077a0385849d6817b2007c095)

#define EBUSY

Mount device busy.

**Definition** errno.h:55

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

**Definition** kernel.h:392

[k\_thread\_user\_mode\_enter](group__thread__apis.md#ga3fbe1c8a5f3ef1c25382c7d6fca35764)

FUNC\_NORETURN void k\_thread\_user\_mode\_enter(k\_thread\_entry\_t entry, void \*p1, void \*p2, void \*p3)

Drop a thread's privileges permanently to user mode.

[k\_thread\_join](group__thread__apis.md#ga40a733561eb1f64dcaae0e01b167d233)

int k\_thread\_join(struct k\_thread \*thread, k\_timeout\_t timeout)

Sleep until a thread exits.

[k\_thread\_custom\_data\_set](group__thread__apis.md#ga4834d9b81ed60c00eee77b0d4f8ab9e4)

void k\_thread\_custom\_data\_set(void \*value)

Set current thread's custom data.

[k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)

int32\_t k\_sleep(k\_timeout\_t timeout)

Put the current thread to sleep.

[k\_thread\_timeout\_remaining\_ticks](group__thread__apis.md#ga4cb4126c8e4f62bd44f3dd03f2e4a423)

k\_ticks\_t k\_thread\_timeout\_remaining\_ticks(const struct k\_thread \*t)

Get time remaining before a thread wakes up, in system ticks.

[k\_sched\_lock](group__thread__apis.md#ga4f0c5d0b9f279b12a4ad97db0c116a5f)

void k\_sched\_lock(void)

Lock the scheduler.

[k\_msleep](group__thread__apis.md#ga51307cdfe153ab3e918b18755d97c5d9)

static int32\_t k\_msleep(int32\_t ms)

Put the current thread to sleep.

**Definition** kernel.h:487

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

**Definition** kernel.h:584

[k\_thread\_timeout\_expires\_ticks](group__thread__apis.md#ga80013f10d12ccdffbbd88cee048f1c21)

k\_ticks\_t k\_thread\_timeout\_expires\_ticks(const struct k\_thread \*t)

Get time when a thread wakes up, in system ticks.

[k\_thread\_cpu\_mask\_clear](group__thread__apis.md#ga80b9c58df6600c7e79f16756c128f44c)

int k\_thread\_cpu\_mask\_clear(k\_tid\_t thread)

Sets all CPU enable masks to zero.

[k\_sched\_time\_slice\_set](group__thread__apis.md#ga877c1bfeffbf8f097d1656f9e10a66e8)

void k\_sched\_time\_slice\_set(int32\_t slice, int prio)

Set time-slicing period and scope.

[k\_thread\_start](group__thread__apis.md#ga88031bd9fcfcd4305bae4029a4d8416f)

void k\_thread\_start(k\_tid\_t thread)

Start an inactive thread.

[k\_thread\_cpu\_mask\_disable](group__thread__apis.md#ga89e6c07ac112da75b2ef115d1a557d44)

int k\_thread\_cpu\_mask\_disable(k\_tid\_t thread, int cpu)

Prevent thread to run on specified CPU.

[k\_wakeup](group__thread__apis.md#ga9275a019c8ff3c7fe49a81f8c078157e)

void k\_wakeup(k\_tid\_t thread)

Wake up a sleeping thread.

[k\_thread\_stack\_free](group__thread__apis.md#ga95560cb85f6656b981a9a50ff2cd70b7)

int k\_thread\_stack\_free(k\_thread\_stack\_t \*stack)

Free a dynamically allocated thread stack.

[k\_sched\_current\_thread\_query](group__thread__apis.md#gac3b994b90b5bccded0895304f6b20c5d)

\_\_attribute\_const\_\_ k\_tid\_t k\_sched\_current\_thread\_query(void)

Query thread ID of the current thread.

[k\_thread\_create](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367)

k\_tid\_t k\_thread\_create(struct k\_thread \*new\_thread, k\_thread\_stack\_t \*stack, size\_t stack\_size, k\_thread\_entry\_t entry, void \*p1, void \*p2, void \*p3, int prio, uint32\_t options, k\_timeout\_t delay)

Create a thread.

[k\_thread\_deadline\_set](group__thread__apis.md#gad887f16c1dd6f3247682a83beb22d1ce)

void k\_thread\_deadline\_set(k\_tid\_t thread, int deadline)

Set deadline expiration time for scheduler.

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

**Definition** kernel.h:103

[k\_thread\_stack\_alloc](group__thread__apis.md#gafe00cc70bac8a47ba6dda21bde508614)

k\_thread\_stack\_t \* k\_thread\_stack\_alloc(size\_t size, int flags)

Dynamically allocate a thread stack.

[k\_timer\_expires\_ticks](group__timer__apis.md#ga022b4cf5c8d0ee21b6a3b04fd425533f)

k\_ticks\_t k\_timer\_expires\_ticks(const struct k\_timer \*timer)

Get next expiration time of a timer, in system ticks.

[k\_timer\_stop\_t](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c)

void(\* k\_timer\_stop\_t)(struct k\_timer \*timer)

Timer stop function type.

**Definition** kernel.h:1527

[k\_timer\_remaining\_ticks](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4)

k\_ticks\_t k\_timer\_remaining\_ticks(const struct k\_timer \*timer)

Get time remaining before a timer next expires, in system ticks.

[k\_timer\_user\_data\_get](group__timer__apis.md#ga19a7d99a01a83828efd7f0d3bf2dd358)

void \* k\_timer\_user\_data\_get(const struct k\_timer \*timer)

Retrieve the user-specific data from a timer.

[k\_timer\_expiry\_t](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde)

void(\* k\_timer\_expiry\_t)(struct k\_timer \*timer)

Timer expiry function type.

**Definition** kernel.h:1511

[k\_timer\_init](group__timer__apis.md#ga318c846a740b901e5d56876a47ad7f61)

void k\_timer\_init(struct k\_timer \*timer, k\_timer\_expiry\_t expiry\_fn, k\_timer\_stop\_t stop\_fn)

Initialize a timer.

[k\_timer\_start](group__timer__apis.md#ga3ba70e9f059ff52fd2057ab89ea7f2ee)

void k\_timer\_start(struct k\_timer \*timer, k\_timeout\_t duration, k\_timeout\_t period)

Start a timer.

[k\_timer\_remaining\_get](group__timer__apis.md#ga6c6d8b0aa59bfa0f5924e95ccf756259)

static uint32\_t k\_timer\_remaining\_get(struct k\_timer \*timer)

Get time remaining before a timer next expires.

**Definition** kernel.h:1670

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

**Definition** time\_units.h:1254

[k\_ticks\_to\_ms\_floor64](group__timeutil__unit__apis.md#gac417ab53d5d493d95e24e7f777f8a4e0)

#define k\_ticks\_to\_ms\_floor64(t)

Convert ticks to milliseconds.

**Definition** time\_units.h:1269

[k\_work\_poll\_submit\_to\_queue](group__workqueue__apis.md#ga0abafd7f851e42fd3572c8438e600a53)

int k\_work\_poll\_submit\_to\_queue(struct k\_work\_q \*work\_q, struct k\_work\_poll \*work, struct k\_poll\_event \*events, int num\_events, k\_timeout\_t timeout)

Submit a triggered work item.

[k\_work\_queue\_thread\_get](group__workqueue__apis.md#ga0b8b496f7e7bd82d08590a07293e38d7)

static k\_tid\_t k\_work\_queue\_thread\_get(struct k\_work\_q \*queue)

Access the thread that animates a work queue.

**Definition** kernel.h:4060

[k\_work\_is\_pending](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)

static bool k\_work\_is\_pending(const struct k\_work \*work)

Test whether a work item is currently pending.

**Definition** kernel.h:4031

[k\_work\_queue\_drain](group__workqueue__apis.md#ga0fefe3e0225ac99b47b250849f6cd863)

int k\_work\_queue\_drain(struct k\_work\_q \*queue, bool plug)

Wait until the work queue has drained, optionally plugging it.

[k\_work\_delayable\_expires\_get](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624)

static k\_ticks\_t k\_work\_delayable\_expires\_get(const struct k\_work\_delayable \*dwork)

Get the absolute tick count at which a scheduled delayable work will be submitted.

**Definition** kernel.h:4048

[k\_work\_schedule\_for\_queue](group__workqueue__apis.md#ga17f863c9f6ff2fb41dc0f3b7de4fdf23)

int k\_work\_schedule\_for\_queue(struct k\_work\_q \*queue, struct k\_work\_delayable \*dwork, k\_timeout\_t delay)

Submit an idle work item to a queue after a delay.

[k\_work\_delayable\_busy\_get](group__workqueue__apis.md#ga1b76969667844f0981d348c9c671bc9f)

int k\_work\_delayable\_busy\_get(const struct k\_work\_delayable \*dwork)

Busy state flags from the delayable work item.

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

**Definition** kernel.h:4187

[k\_work\_submit\_to\_queue](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c)

int k\_work\_submit\_to\_queue(struct k\_work\_q \*queue, struct k\_work \*work)

Submit a work item to a queue.

[k\_work\_user\_is\_pending](group__workqueue__apis.md#ga58d05d4127e4cd51104a1f1a87f626cd)

static bool k\_work\_user\_is\_pending(struct k\_work\_user \*work)

Check if a userspace work item is pending.

**Definition** kernel.h:4164

[k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda)

void(\* k\_work\_handler\_t)(struct k\_work \*work)

The signature for a work item handler function.

**Definition** kernel.h:3262

[k\_work\_schedule](group__workqueue__apis.md#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)

int k\_work\_schedule(struct k\_work\_delayable \*dwork, k\_timeout\_t delay)

Submit an idle work item to the system work queue after a delay.

[k\_work\_delayable\_is\_pending](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e)

static bool k\_work\_delayable\_is\_pending(const struct k\_work\_delayable \*dwork)

Test whether a delayed work item is currently pending.

**Definition** kernel.h:4042

[k\_work\_cancel\_delayable\_sync](group__workqueue__apis.md#ga7e7ec237648556fc16bfda8d35f7cd86)

bool k\_work\_cancel\_delayable\_sync(struct k\_work\_delayable \*dwork, struct k\_work\_sync \*sync)

Cancel delayable work and wait.

[k\_work\_cancel\_delayable](group__workqueue__apis.md#ga92355914ee178d4c3e848a1946bed3e4)

int k\_work\_cancel\_delayable(struct k\_work\_delayable \*dwork)

Cancel delayable work.

[k\_work\_user\_init](group__workqueue__apis.md#ga9de9c7a7f13cc6b325e5453e34afe62d)

static void k\_work\_user\_init(struct k\_work\_user \*work, k\_work\_user\_handler\_t handler)

Initialize a userspace work item.

**Definition** kernel.h:4142

[k\_work\_queue\_unplug](group__workqueue__apis.md#gaa0463bb79af3ec470f7d3be02052139f)

int k\_work\_queue\_unplug(struct k\_work\_q \*queue)

Release a work queue to accept new submissions.

[k\_work\_reschedule](group__workqueue__apis.md#gaacaab408fb7c848d466ad1f069dfa648)

int k\_work\_reschedule(struct k\_work\_delayable \*dwork, k\_timeout\_t delay)

Reschedule a work item to the system work queue after a delay.

[k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc)

void(\* k\_work\_user\_handler\_t)(struct k\_work\_user \*work)

Work item handler function type for user work queues.

**Definition** kernel.h:4083

[k\_work\_cancel\_sync](group__workqueue__apis.md#gab2b05cfe3af08f7d32c3946fa1c808f9)

bool k\_work\_cancel\_sync(struct k\_work \*work, struct k\_work\_sync \*sync)

Cancel a work item and wait for it to complete.

[k\_work\_user\_queue\_thread\_get](group__workqueue__apis.md#gab487068e9564cd77b6bdbac3d5670923)

static k\_tid\_t k\_work\_user\_queue\_thread\_get(struct k\_work\_user\_q \*work\_q)

Access the user mode thread that animates a work queue.

**Definition** kernel.h:4242

[k\_work\_busy\_get](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b)

int k\_work\_busy\_get(const struct k\_work \*work)

Busy state flags from the work item.

[k\_work\_delayable\_from\_work](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca)

static struct k\_work\_delayable \* k\_work\_delayable\_from\_work(struct k\_work \*work)

Get the parent delayable work structure from a work pointer.

**Definition** kernel.h:4037

[k\_work\_delayable\_remaining\_get](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4)

static k\_ticks\_t k\_work\_delayable\_remaining\_get(const struct k\_work\_delayable \*dwork)

Get the number of ticks until a scheduled delayable work will be submitted.

**Definition** kernel.h:4054

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

**Definition** kernel.h:3837

[K\_WORK\_QUEUED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85)

@ K\_WORK\_QUEUED

Flag indicating a work item that has been submitted to a queue but has not started running.

**Definition** kernel.h:3844

[K\_WORK\_DELAYED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed)

@ K\_WORK\_DELAYED

Flag indicating a delayed work item that is scheduled for submission to a queue.

**Definition** kernel.h:3851

[K\_WORK\_RUNNING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165)

@ K\_WORK\_RUNNING

Flag indicating a work item that is running under a work queue thread.

**Definition** kernel.h:3831

[K\_WORK\_FLUSHING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601)

@ K\_WORK\_FLUSHING

Flag indicating a synced work item that is being flushed.

**Definition** kernel.h:3857

[k\_sys\_runtime\_stats\_disable](include_2zephyr_2kernel_8h.md#a2e3c96c0b11108ee7eca3f0666c780e0)

void k\_sys\_runtime\_stats\_disable(void)

Disable gathering of system runtime statistics.

[k\_thread\_runtime\_stats\_enable](include_2zephyr_2kernel_8h.md#a3e52beb93fca2231d5860fe1cf1181fd)

int k\_thread\_runtime\_stats\_enable(k\_tid\_t thread)

Enable gathering of runtime statistics for specified thread.

[k\_sys\_runtime\_stats\_enable](include_2zephyr_2kernel_8h.md#a54f2652ba1ed613219941eaaf193180c)

void k\_sys\_runtime\_stats\_enable(void)

Enable gathering of system runtime statistics.

[k\_thread\_runtime\_stats\_get](include_2zephyr_2kernel_8h.md#a82d886a1c911b39c1b47c32200cedac6)

int k\_thread\_runtime\_stats\_get(k\_tid\_t thread, k\_thread\_runtime\_stats\_t \*stats)

Get the runtime statistics of a thread.

[execution\_context\_types](include_2zephyr_2kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779c)

execution\_context\_types

**Definition** kernel.h:88

[K\_ISR](include_2zephyr_2kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779ca30593044743695f8184a157283dac4d5)

@ K\_ISR

**Definition** kernel.h:89

[K\_COOP\_THREAD](include_2zephyr_2kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779ca62c0b731a1bb3c5e4aadeba3f93df58b)

@ K\_COOP\_THREAD

**Definition** kernel.h:90

[K\_PREEMPT\_THREAD](include_2zephyr_2kernel_8h.md#ab0b42f9804777dfa5fed2b7cd866779cae84f57f4ac996c751d1f4c9e49789322)

@ K\_PREEMPT\_THREAD

**Definition** kernel.h:91

[k\_thread\_runtime\_stats\_all\_get](include_2zephyr_2kernel_8h.md#abd855bb83b3be393b46833e7854a193e)

int k\_thread\_runtime\_stats\_all\_get(k\_thread\_runtime\_stats\_t \*stats)

Get the runtime statistics of all threads.

[k\_thread\_runtime\_stats\_disable](include_2zephyr_2kernel_8h.md#ae5ea2e05a602b7d5ee78a65ced61d63b)

int k\_thread\_runtime\_stats\_disable(k\_tid\_t thread)

Disable gathering of runtime statistics for specified thread.

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:364

[k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf)

struct k\_thread\_runtime\_stats k\_thread\_runtime\_stats\_t

[kernel\_includes.h](kernel__includes_8h.md)

Header files included by kernel.h.

[k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f)

void(\* k\_thread\_timeslice\_fn\_t)(struct k\_thread \*thread, void \*data)

**Definition** kernel\_structs.h:268

[limits.h](limits_8h.md)

[mem\_stats.h](mem__stats_8h.md)

Memory Statistics.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

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

**Definition** kernel.h:3012

[k\_condvar::wait\_q](structk__condvar.md#a14b457a06420f093e779d569f4fea906)

\_wait\_q\_t wait\_q

**Definition** kernel.h:3013

[k\_event](structk__event.md)

Event Structure.

**Definition** kernel.h:2207

[k\_event::lock](structk__event.md#a1f0de9c69f29ad854f3b0d510ceb1efc)

struct k\_spinlock lock

**Definition** kernel.h:2210

[k\_event::events](structk__event.md#a54c6f5997132e88406ffa5bcc0a10b83)

uint32\_t events

**Definition** kernel.h:2209

[k\_event::wait\_q](structk__event.md#a5bacd5f2d34da646d9d7ee229842e432)

\_wait\_q\_t wait\_q

**Definition** kernel.h:2208

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

[k\_futex](structk__futex.md)

futex structure

**Definition** kernel.h:2128

[k\_futex::val](structk__futex.md#a454ad1b595b899306c8e9c8e1431e7a7)

atomic\_t val

**Definition** kernel.h:2129

[k\_heap](structk__heap.md)

**Definition** kernel.h:5297

[k\_heap::lock](structk__heap.md#a3bd15b8ad69a6ab76b5c4a297673e5ec)

struct k\_spinlock lock

**Definition** kernel.h:5300

[k\_heap::heap](structk__heap.md#a4b8551f4fd1cd648c68f47ea2ebd682f)

struct sys\_heap heap

**Definition** kernel.h:5298

[k\_heap::wait\_q](structk__heap.md#abd30d236bd986e791ea7698583e45588)

\_wait\_q\_t wait\_q

**Definition** kernel.h:5299

[k\_lifo](structk__lifo.md)

**Definition** kernel.h:2613

[k\_mbox\_msg](structk__mbox__msg.md)

Mailbox Message Structure.

**Definition** kernel.h:4694

[k\_mbox\_msg::tx\_target\_thread](structk__mbox__msg.md#a73236acb7d27bb0233f5abb7214fb19c)

k\_tid\_t tx\_target\_thread

target thread id

**Definition** kernel.h:4704

[k\_mbox\_msg::tx\_data](structk__mbox__msg.md#a74b0edeed4c44cb5932eb292efc9d9c2)

void \* tx\_data

sender's message data buffer

**Definition** kernel.h:4700

[k\_mbox\_msg::rx\_source\_thread](structk__mbox__msg.md#a9eb145a242ac66e80d90286d83fe7a61)

k\_tid\_t rx\_source\_thread

source thread id

**Definition** kernel.h:4702

[k\_mbox\_msg::info](structk__mbox__msg.md#aa79f2bf71431b474ec4551ade4d7a8dd)

uint32\_t info

application-defined information value

**Definition** kernel.h:4698

[k\_mbox\_msg::size](structk__mbox__msg.md#aeabf45e9599a64852a1cfd656b1ece8e)

size\_t size

size of message (in bytes)

**Definition** kernel.h:4696

[k\_mbox](structk__mbox.md)

Mailbox Structure.

**Definition** kernel.h:4716

[k\_mbox::tx\_msg\_queue](structk__mbox.md#a0bca912a50120707ddafa66d740ade96)

\_wait\_q\_t tx\_msg\_queue

Transmit messages queue.

**Definition** kernel.h:4718

[k\_mbox::lock](structk__mbox.md#a2c549d5bd7216b62d81ad2198e0d79e4)

struct k\_spinlock lock

**Definition** kernel.h:4721

[k\_mbox::rx\_msg\_queue](structk__mbox.md#a808a14c31892a2d042cdb0723a2956e2)

\_wait\_q\_t rx\_msg\_queue

Receive message queue.

**Definition** kernel.h:4720

[k\_mem\_domain](structk__mem__domain.md)

Memory Domain.

**Definition** mem\_domain.h:80

[k\_mem\_partition](structk__mem__partition.md)

Memory Partition.

**Definition** mem\_domain.h:55

[k\_msgq\_attrs](structk__msgq__attrs.md)

Message Queue Attributes.

**Definition** kernel.h:4461

[k\_msgq\_attrs::used\_msgs](structk__msgq__attrs.md#a00f936870442fa455117cbdd7821fac5)

uint32\_t used\_msgs

Used messages.

**Definition** kernel.h:4467

[k\_msgq\_attrs::msg\_size](structk__msgq__attrs.md#a7d1d72946bdd517c07da37493a89e30e)

size\_t msg\_size

Message Size.

**Definition** kernel.h:4463

[k\_msgq\_attrs::max\_msgs](structk__msgq__attrs.md#ad0f5894ba0da840b91eb85015252e649)

uint32\_t max\_msgs

Maximal number of messages.

**Definition** kernel.h:4465

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4402

[k\_msgq::msg\_size](structk__msgq.md#a512fe468da96540639a0d71f1707f79d)

size\_t msg\_size

Message size.

**Definition** kernel.h:4408

[k\_msgq::read\_ptr](structk__msgq.md#a594e8a4a638521f42f24f85fe0742d64)

char \* read\_ptr

Read pointer.

**Definition** kernel.h:4416

[k\_msgq::used\_msgs](structk__msgq.md#a5c0cc83eaaf44d7fd7de8fffc7b2f857)

uint32\_t used\_msgs

Number of used messages.

**Definition** kernel.h:4420

[k\_msgq::buffer\_end](structk__msgq.md#a9d47fd25d7a70e8518d45dd48c51f0e0)

char \* buffer\_end

End of message buffer.

**Definition** kernel.h:4414

[k\_msgq::lock](structk__msgq.md#aa2e00a7292502f0de88cff28c5e375f0)

struct k\_spinlock lock

Lock.

**Definition** kernel.h:4406

[k\_msgq::write\_ptr](structk__msgq.md#aacf9b7b9f6e26e402f3752fc56834f23)

char \* write\_ptr

Write pointer.

**Definition** kernel.h:4418

[k\_msgq::buffer\_start](structk__msgq.md#aca77f1cf833d3aa27ae65004b446bdd2)

char \* buffer\_start

Start of message buffer.

**Definition** kernel.h:4412

[k\_msgq::flags](structk__msgq.md#ae03025420908f8342ce12a1395c7657b)

uint8\_t flags

Message queue.

**Definition** kernel.h:4425

[k\_msgq::wait\_q](structk__msgq.md#ae3b3d53d60b789d69c65494cfd090076)

\_wait\_q\_t wait\_q

Message queue wait queue.

**Definition** kernel.h:4404

[k\_msgq::max\_msgs](structk__msgq.md#aebd3b6e91e97b2d4369feea1a3f7b7a0)

uint32\_t max\_msgs

Maximal number of messages.

**Definition** kernel.h:4410

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

[k\_mutex::lock\_count](structk__mutex.md#a0db401fc8e03e1f984b8fd15af974718)

uint32\_t lock\_count

Current lock count.

**Definition** kernel.h:2907

[k\_mutex::wait\_q](structk__mutex.md#a4add234295bceff22551ee74f3aed802)

\_wait\_q\_t wait\_q

Mutex wait queue.

**Definition** kernel.h:2902

[k\_mutex::owner\_orig\_prio](structk__mutex.md#ab0d16fac9f8af960a501ffd93ec08c80)

int owner\_orig\_prio

Original thread priority.

**Definition** kernel.h:2910

[k\_mutex::owner](structk__mutex.md#af910bb07dc99e50078de26fccca468e4)

struct k\_thread \* owner

Mutex owner.

**Definition** kernel.h:2904

[k\_obj\_core](structk__obj__core.md)

Object core structure.

**Definition** obj\_core.h:121

[k\_pipe](structk__pipe.md)

Pipe Structure.

**Definition** kernel.h:4847

[k\_pipe::wait\_q](structk__pipe.md#a2b7ab1aceb3f380c4adfe740d57dbeed)

struct k\_pipe::@222111176077001144107333331325352300257015060074 wait\_q

[k\_pipe::flags](structk__pipe.md#a2ed95fbe24ea20c4f292a66def1d4dde)

uint8\_t flags

Wait queue.

**Definition** kernel.h:4862

[k\_pipe::readers](structk__pipe.md#a81ab4435d9ca7e5246164fc4fcd9ad59)

\_wait\_q\_t readers

Reader wait queue.

**Definition** kernel.h:4856

[k\_pipe::write\_index](structk__pipe.md#a8f46bd01da0e52e4ee918d9ebe6ad739)

size\_t write\_index

Where in buffer to write.

**Definition** kernel.h:4852

[k\_pipe::bytes\_used](structk__pipe.md#a91bedad65285546734b8724811dc6eb8)

size\_t bytes\_used

**Definition** kernel.h:4850

[k\_pipe::lock](structk__pipe.md#aa2a367a9c8f0be89bcdf1bf6d3b0b875)

struct k\_spinlock lock

Synchronization lock.

**Definition** kernel.h:4853

[k\_pipe::writers](structk__pipe.md#ac61ce23d990cf4cef44a1ecfc5047ccc)

\_wait\_q\_t writers

Writer wait queue.

**Definition** kernel.h:4857

[k\_pipe::size](structk__pipe.md#aca3472fb8d68f01af4e26b0b88736d64)

size\_t size

Buffer size.

**Definition** kernel.h:4849

[k\_pipe::buffer](structk__pipe.md#acb78995d6b7df28a5452f5d2e88b4dfb)

unsigned char \* buffer

Pipe buffer: may be NULL.

**Definition** kernel.h:4848

[k\_pipe::read\_index](structk__pipe.md#ae40f81d9c1459fa42f179cbc728aadd0)

size\_t read\_index

Where in buffer to read from.

**Definition** kernel.h:4851

[k\_poll\_event](structk__poll__event.md)

Poll Event.

**Definition** kernel.h:5646

[k\_poll\_event::signal](structk__poll__event.md#a130aaff7a8908993ed6be737a94a52ab)

struct k\_poll\_signal \* signal

**Definition** kernel.h:5671

[k\_poll\_event::tag](structk__poll__event.md#a37c5f45deaa046b356d95af569220c70)

uint32\_t tag

optional user-specified tag, opaque, untouched by the API

**Definition** kernel.h:5654

[k\_poll\_event::fifo](structk__poll__event.md#a4ba07f42f4af03f30478ebf48a1653f7)

struct k\_fifo \* fifo

**Definition** kernel.h:5673

[k\_poll\_event::msgq](structk__poll__event.md#a5bbe94482a70ec13c2106f89afd2d59c)

struct k\_msgq \* msgq

**Definition** kernel.h:5675

[k\_poll\_event::queue](structk__poll__event.md#a6e30a6ce30702817895e66f22f0abedf)

struct k\_queue \* queue

**Definition** kernel.h:5674

[k\_poll\_event::unused](structk__poll__event.md#a750ac48e7aa3c8fb70814b24e951fc85)

uint32\_t unused

unused bits in 32-bit word

**Definition** kernel.h:5666

[k\_poll\_event::type](structk__poll__event.md#a8f9e251aa8722eb4716f622e85be34ae)

uint32\_t type

bitfield of event types (bitwise-ORed K\_POLL\_TYPE\_xxx values)

**Definition** kernel.h:5657

[k\_poll\_event::sem](structk__poll__event.md#a9ed342b8a45884f985245f55b0e1c8cc)

struct k\_sem \* sem

**Definition** kernel.h:5672

[k\_poll\_event::state](structk__poll__event.md#aaf4f32852d799a406bfeea4e57891129)

uint32\_t state

bitfield of event states (bitwise-ORed K\_POLL\_STATE\_xxx values)

**Definition** kernel.h:5660

[k\_poll\_event::mode](structk__poll__event.md#acca81763486ef5ebcc911cb1cbd6c899)

uint32\_t mode

mode of operation, from enum k\_poll\_modes

**Definition** kernel.h:5663

[k\_poll\_event::poller](structk__poll__event.md#ad030c37b97f33e1bbb3361057180fa4f)

struct z\_poller \* poller

PRIVATE - DO NOT TOUCH.

**Definition** kernel.h:5651

[k\_poll\_event::obj](structk__poll__event.md#aeaf67f9bc91d59fb2939e1469a088f2d)

void \* obj

**Definition** kernel.h:5670

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5622

[k\_poll\_signal::poll\_events](structk__poll__signal.md#a22e88955ba0e369d39edefadcf4c60fd)

sys\_dlist\_t poll\_events

PRIVATE - DO NOT TOUCH.

**Definition** kernel.h:5624

[k\_poll\_signal::result](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1)

int result

custom result value passed to k\_poll\_signal\_raise() if needed

**Definition** kernel.h:5633

[k\_poll\_signal::signaled](structk__poll__signal.md#ae9fe6751d75f7d2b2800cb723603c0fe)

unsigned int signaled

1 if the event has been signaled, 0 otherwise.

**Definition** kernel.h:5630

[k\_queue](structk__queue.md)

**Definition** kernel.h:1835

[k\_queue::lock](structk__queue.md#a18fd165fec722384b3748bfdf3332a4c)

struct k\_spinlock lock

**Definition** kernel.h:1837

[k\_queue::wait\_q](structk__queue.md#a871d734f2b21a9cad3ca4a2ba79e64f1)

\_wait\_q\_t wait\_q

**Definition** kernel.h:1838

[k\_queue::data\_q](structk__queue.md#a892371af9701ce67619e38446bc2ceae)

sys\_sflist\_t data\_q

**Definition** kernel.h:1836

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:250

[k\_thread::base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8)

struct \_thread\_base base

**Definition** thread.h:252

[k\_thread::resource\_pool](structk__thread.md#a35b859bded3a270f25ccc40efece7583)

struct k\_heap \* resource\_pool

resource pool

**Definition** thread.h:333

[k\_thread::entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03)

struct \_\_thread\_entry entry

thread entry and parameters description

**Definition** thread.h:279

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3889

[k\_work\_delayable::timeout](structk__work__delayable.md#a1db9148a05731100d3d3915534ac2d4d)

struct \_timeout timeout

**Definition** kernel.h:3894

[k\_work\_delayable::queue](structk__work__delayable.md#a25dc6aaf1713e1db0f2530370afd4dc4)

struct k\_work\_q \* queue

**Definition** kernel.h:3897

[k\_work\_delayable::work](structk__work__delayable.md#a594ad30acf08249909c30c0af76c1629)

struct k\_work work

**Definition** kernel.h:3891

[k\_work\_q](structk__work__q.md)

A structure used to hold work until it can be processed.

**Definition** kernel.h:4008

[k\_work\_q::pending](structk__work__q.md#a2012199571f6b658873550d64386b00c)

sys\_slist\_t pending

**Definition** kernel.h:4017

[k\_work\_q::drainq](structk__work__q.md#a308d1ac78b1203b7ea78b0f18c5bdf5b)

\_wait\_q\_t drainq

**Definition** kernel.h:4023

[k\_work\_q::notifyq](structk__work__q.md#a561c90f8bb944217230e00052cdecf10)

\_wait\_q\_t notifyq

**Definition** kernel.h:4020

[k\_work\_q::flags](structk__work__q.md#a68bc8e9c412ebdbf34827087d91a080e)

uint32\_t flags

**Definition** kernel.h:4026

[k\_work\_q::thread](structk__work__q.md#aa42ca271a4989f129bf1a43c491327eb)

struct k\_thread thread

**Definition** kernel.h:4010

[k\_work\_queue\_config](structk__work__queue__config.md)

A structure holding optional configuration items for a work queue.

**Definition** kernel.h:3985

[k\_work\_queue\_config::name](structk__work__queue__config.md#a0929d83372efff6798bc69bb7ca1eaaa)

const char \* name

The name to be given to the work queue thread.

**Definition** kernel.h:3990

[k\_work\_queue\_config::no\_yield](structk__work__queue__config.md#afcf64d6e69d1ddfff8cbd749dafa4d13)

bool no\_yield

Control whether the work queue thread should yield between items.

**Definition** kernel.h:4004

[k\_work\_sync](structk__work__sync.md)

A structure holding internal state for a pending synchronous operation on a work item or queue.

**Definition** kernel.h:3972

[k\_work\_sync::canceller](structk__work__sync.md#a7e8fd0b9d6736c403aefa8462c7c0835)

struct z\_work\_canceller canceller

**Definition** kernel.h:3975

[k\_work\_sync::flusher](structk__work__sync.md#ad81ff57cb9f2f3dc5f2d65917cf04f1c)

struct z\_work\_flusher flusher

**Definition** kernel.h:3974

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3861

[k\_work::handler](structk__work.md#a096d6ca1338fb0fbfa330b790136f172)

k\_work\_handler\_t handler

**Definition** kernel.h:3870

[k\_work::flags](structk__work.md#a391ed7d2039cd05c9894267bf8ea4dfd)

uint32\_t flags

**Definition** kernel.h:3881

[k\_work::queue](structk__work.md#a551be8394e041020c36a97dc2e12e137)

struct k\_work\_q \* queue

**Definition** kernel.h:3873

[k\_work::node](structk__work.md#a85772682983e0fdeb735f0821d5710d4)

sys\_snode\_t node

**Definition** kernel.h:3867

[sys\_heap](structsys__heap.md)

**Definition** sys\_heap.h:56

[sys\_memory\_stats](structsys__memory__stats.md)

**Definition** mem\_stats.h:24

[kernel.h](subsys_2testsuite_2ztest_2include_2zephyr_2syscalls_2kernel_8h.md)

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[tracing.h](tracing_2tracing_8h.md)

[tracing\_macros.h](tracing__macros_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel.h](include_2zephyr_2kernel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
