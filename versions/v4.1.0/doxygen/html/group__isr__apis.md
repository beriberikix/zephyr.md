---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__isr__apis.html
original_path: doxygen/html/group__isr__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Interrupt Service Routine APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [IRQ\_CONNECT](#ga131739d1faf501a15590053817aba984)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
|  | Initialize an interrupt handler. |
| #define | [IRQ\_DIRECT\_CONNECT](#gac6c8746ac28da6ce02b24714f4144ff3)(irq\_p, priority\_p, isr\_p, flags\_p) |
|  | Initialize a 'direct' interrupt handler. |
| #define | [ISR\_DIRECT\_HEADER](#ga1ab99dbeb50b228001e1fca808cbaeea)() |
|  | Common tasks before executing the body of an ISR. |
| #define | [ISR\_DIRECT\_FOOTER](#ga31581157c9dbacf935f0e6a8dd456335)(check\_reschedule) |
|  | Common tasks before exiting the body of an ISR. |
| #define | [ISR\_DIRECT\_PM](#ga3c1327551dfca7818975e3fbf1470227)() |
|  | Perform power management idle exit logic. |
| #define | [ISR\_DIRECT\_DECLARE](#gaf86866cd07fd37f381d98866f8874ebf)(name) |
|  | Helper macro to declare a direct interrupt service routine. |
| #define | [irq\_lock](#ga19fdde73c3b02fcca6cf1d1e67631228)() |
|  | Lock interrupts. |
| #define | [irq\_unlock](#ga646045943b3b2a130738bcc48867bf57)(key) |
|  | Unlock interrupts. |
| #define | [irq\_enable](#ga7ea700ee31e4ff036c997a554dbedfeb)(irq) |
|  | Enable an IRQ. |
| #define | [irq\_disable](#ga82c3a15d812f58e0f6525f358d031e6d)(irq) |
|  | Disable an IRQ. |
| #define | [irq\_is\_enabled](#ga71fef3867ba9818cf0a5baf8410a6354)(irq) |
|  | Get IRQ enable state. |

| Functions | |
| --- | --- |
| static int | [irq\_connect\_dynamic](#ga4e9915b92b09df49b99bc449f0cc31a1) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Configure a dynamic interrupt. |
| static int | [irq\_disconnect\_dynamic](#gabdab7745edc1e15862e1772d8673fc00) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Disconnect a dynamic interrupt. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_is\_in\_isr](#ga8482b0dd2283d12677a9ebe321667d16) (void) |
|  | Determine if code is running at interrupt level. |
| int | [k\_is\_preempt\_thread](#ga91e1cf0dc7fc93a3214cadb74ed86666) (void) |
|  | Determine if code is running in a preemptible thread. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_is\_pre\_kernel](#gae74e5de996276df767b96d4b50fa47ea) (void) |
|  | Test whether startup is in the before-main-task phase. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga131739d1faf501a15590053817aba984)IRQ\_CONNECT

| #define IRQ\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *isr\_param\_p*, |
|  |  |  | *flags\_p* ) |

`#include <[irq.h](irq_8h.md)>`

**Value:**

[ARCH\_IRQ\_CONNECT](arch_2arc_2v2_2irq_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p)

[ARCH\_IRQ\_CONNECT](arch_2arc_2v2_2irq_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)

#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p)

**Definition** irq.h:51

Initialize an interrupt handler.

This routine initializes an interrupt handler for an IRQ. The IRQ must be subsequently enabled before the interrupt handler begins servicing interrupts.

Warning
:   Although this routine is invoked at run-time, all of its arguments must be computable by the compiler at build time.

Parameters
:   | irq\_p | IRQ line number. |
    | --- | --- |
    | priority\_p | Interrupt priority. |
    | isr\_p | Address of interrupt service routine. |
    | isr\_param\_p | Parameter passed to interrupt service routine. |
    | flags\_p | Architecture-specific IRQ configuration flags.. |

## [◆ ](#gac6c8746ac28da6ce02b24714f4144ff3)IRQ\_DIRECT\_CONNECT

| #define IRQ\_DIRECT\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *flags\_p* ) |

`#include <[irq.h](irq_8h.md)>`

**Value:**

[ARCH\_IRQ\_DIRECT\_CONNECT](arch_2arc_2v2_2irq_8h.md#a875f2b1ca924721fe3854796bd96c2db)(irq\_p, priority\_p, isr\_p, flags\_p)

[ARCH\_IRQ\_DIRECT\_CONNECT](arch_2arc_2v2_2irq_8h.md#a875f2b1ca924721fe3854796bd96c2db)

#define ARCH\_IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, isr\_p, flags\_p)

Configure a 'direct' static interrupt.

**Definition** irq.h:78

Initialize a 'direct' interrupt handler.

This routine initializes an interrupt handler for an IRQ. The IRQ must be subsequently enabled via [irq\_enable()](#ga7ea700ee31e4ff036c997a554dbedfeb) before the interrupt handler begins servicing interrupts.

These ISRs are designed for performance-critical interrupt handling and do not go through common interrupt handling code. They must be implemented in such a way that it is safe to put them directly in the vector table. For ISRs written in C, The [ISR\_DIRECT\_DECLARE()](#gaf86866cd07fd37f381d98866f8874ebf) macro will do this automatically. For ISRs written in assembly it is entirely up to the developer to ensure that the right steps are taken.

This type of interrupt currently has a few limitations compared to normal Zephyr interrupts:

- No parameters are passed to the ISR.
- No stack switch is done, the ISR will run on the interrupted context's stack, unless the architecture automatically does the stack switch in HW.
- Interrupt locking state is unchanged from how the HW sets it when the ISR runs. On arches that enter ISRs with interrupts locked, they will remain locked.
- Scheduling decisions are now optional, controlled by the return value of ISRs implemented with the [ISR\_DIRECT\_DECLARE()](#gaf86866cd07fd37f381d98866f8874ebf) macro
- The call into the OS to exit power management idle state is now optional. Normal interrupts always do this before the ISR is run, but when it runs is now controlled by the placement of a [ISR\_DIRECT\_PM()](#ga3c1327551dfca7818975e3fbf1470227) macro, or omitted entirely.

Warning
:   Although this routine is invoked at run-time, all of its arguments must be computable by the compiler at build time.

Parameters
:   | irq\_p | IRQ line number. |
    | --- | --- |
    | priority\_p | Interrupt priority. |
    | isr\_p | Address of interrupt service routine. |
    | flags\_p | Architecture-specific IRQ configuration flags. |

## [◆ ](#ga82c3a15d812f58e0f6525f358d031e6d)irq\_disable

| #define irq\_disable | ( |  | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[irq.h](irq_8h.md)>`

**Value:**

[arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)(irq)

[arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)

#define arch\_irq\_disable(irq)

**Definition** irq.h:107

Disable an IRQ.

This routine disables interrupts from source *irq*.

Parameters
:   | irq | IRQ line. |
    | --- | --- |

## [◆ ](#ga7ea700ee31e4ff036c997a554dbedfeb)irq\_enable

| #define irq\_enable | ( |  | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[irq.h](irq_8h.md)>`

**Value:**

[arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)(irq)

[arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)

#define arch\_irq\_enable(irq)

**Definition** irq.h:106

Enable an IRQ.

This routine enables interrupts from source *irq*.

Parameters
:   | irq | IRQ line. |
    | --- | --- |

## [◆ ](#ga71fef3867ba9818cf0a5baf8410a6354)irq\_is\_enabled

| #define irq\_is\_enabled | ( |  | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[irq.h](irq_8h.md)>`

**Value:**

[arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)(irq)

[arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)

#define arch\_irq\_is\_enabled(irq)

**Definition** irq.h:109

Get IRQ enable state.

This routine indicates if interrupts from source *irq* are enabled.

Parameters
:   | irq | IRQ line. |
    | --- | --- |

Returns
:   interrupt enable state, true or false

## [◆ ](#ga19fdde73c3b02fcca6cf1d1e67631228)irq\_lock

| #define irq\_lock | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[irq.h](irq_8h.md)>`

**Value:**

z\_smp\_global\_lock()

Lock interrupts.

This routine disables all interrupts on the CPU. It returns an unsigned integer "lock-out key", which is an architecture-dependent indicator of whether interrupts were locked prior to the call. The lock-out key must be passed to [irq\_unlock()](#ga646045943b3b2a130738bcc48867bf57) to re-enable interrupts.

Note
:   This routine must also serve as a memory barrier to ensure the uniprocessor implementation of spinlocks is correct.

This routine can be called recursively, as long as the caller keeps track of each lock-out key that is generated. Interrupts are re-enabled by passing each of the keys to [irq\_unlock()](#ga646045943b3b2a130738bcc48867bf57) in the reverse order they were acquired. (That is, each call to [irq\_lock()](#ga19fdde73c3b02fcca6cf1d1e67631228) must be balanced by a corresponding call to [irq\_unlock()](#ga646045943b3b2a130738bcc48867bf57).)

This routine can only be invoked from supervisor mode. Some architectures (for example, ARM) will fail silently if invoked from user mode instead of generating an exception.

Note
:   This routine can be called by ISRs or by threads. If it is called by a thread, the interrupt lock is thread-specific; this means that interrupts remain disabled only while the thread is running. If the thread performs an operation that allows another thread to run (for example, giving a semaphore or sleeping for N milliseconds), the interrupt lock no longer applies and interrupts may be re-enabled while other processing occurs. When the thread once again becomes the current thread, the kernel re-establishes its interrupt lock; this ensures the thread won't be interrupted until it has explicitly released the interrupt lock it established.

Warning
:   The lock-out key should never be used to manually re-enable interrupts or to inspect or manipulate the contents of the CPU's interrupt bits.

Returns
:   An architecture-dependent lock-out key representing the "interrupt disable state" prior to the call.

## [◆ ](#ga646045943b3b2a130738bcc48867bf57)irq\_unlock

| #define irq\_unlock | ( |  | *key* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[irq.h](irq_8h.md)>`

**Value:**

z\_smp\_global\_unlock(key)

Unlock interrupts.

This routine reverses the effect of a previous call to [irq\_lock()](#ga19fdde73c3b02fcca6cf1d1e67631228) using the associated lock-out key. The caller must call the routine once for each time it called [irq\_lock()](#ga19fdde73c3b02fcca6cf1d1e67631228), supplying the keys in the reverse order they were acquired, before interrupts are enabled.

Note
:   This routine must also serve as a memory barrier to ensure the uniprocessor implementation of spinlocks is correct.

This routine can only be invoked from supervisor mode. Some architectures (for example, ARM) will fail silently if invoked from user mode instead of generating an exception.

Note
:   Can be called by ISRs.

Parameters
:   | key | Lock-out key generated by [irq\_lock()](#ga19fdde73c3b02fcca6cf1d1e67631228). |
    | --- | --- |

## [◆ ](#gaf86866cd07fd37f381d98866f8874ebf)ISR\_DIRECT\_DECLARE

| #define ISR\_DIRECT\_DECLARE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[irq.h](irq_8h.md)>`

**Value:**

[ARCH\_ISR\_DIRECT\_DECLARE](arch_2arc_2v2_2irq_8h.md#a5279598e93dd914614a2ae52557be1a5)(name)

[ARCH\_ISR\_DIRECT\_DECLARE](arch_2arc_2v2_2irq_8h.md#a5279598e93dd914614a2ae52557be1a5)

#define ARCH\_ISR\_DIRECT\_DECLARE(name)

**Definition** irq.h:125

Helper macro to declare a direct interrupt service routine.

This will declare the function in a proper way and automatically include the [ISR\_DIRECT\_FOOTER()](#ga31581157c9dbacf935f0e6a8dd456335) and [ISR\_DIRECT\_HEADER()](#ga1ab99dbeb50b228001e1fca808cbaeea) macros. The function should return nonzero status if a scheduling decision should potentially be made. See [ISR\_DIRECT\_FOOTER()](#ga31581157c9dbacf935f0e6a8dd456335) for more details on the scheduling decision.

For architectures that support 'regular' and 'fast' interrupt types, where these interrupt types require different assembly language handling of registers by the ISR, this will always generate code for the 'fast' interrupt type.

Example usage:

```
ISR_DIRECT_DECLARE(my_isr)
{
        bool done = do_stuff();
        ISR_DIRECT_PM(); // done after do_stuff() due to latency concerns
        if (!done) {
            return 0; // don't bother checking if we have to z_swap()
        }

        k_sem_give(some_sem);
        return 1;
 }
```

Parameters
:   | name | symbol name of the ISR |
    | --- | --- |

## [◆ ](#ga31581157c9dbacf935f0e6a8dd456335)ISR\_DIRECT\_FOOTER

| #define ISR\_DIRECT\_FOOTER | ( |  | *check\_reschedule* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[irq.h](irq_8h.md)>`

**Value:**

[ARCH\_ISR\_DIRECT\_FOOTER](arch_2arc_2v2_2irq_8h.md#aa7c471213fa28b3685f153ea2a72cf9d)(check\_reschedule)

[ARCH\_ISR\_DIRECT\_FOOTER](arch_2arc_2v2_2irq_8h.md#aa7c471213fa28b3685f153ea2a72cf9d)

#define ARCH\_ISR\_DIRECT\_FOOTER(swap)

**Definition** irq.h:113

Common tasks before exiting the body of an ISR.

This macro must be at the end of all direct interrupts and performs minimal architecture-specific tasks like EOI. It has no return value.

In a normal interrupt, a check is done at end of interrupt to invoke z\_swap() logic if the current thread is preemptible and there is another thread ready to run in the kernel's ready queue cache. This is now optional and controlled by the check\_reschedule argument. If unsure, set to nonzero. On systems that do stack switching and nested interrupt tracking in software, z\_swap() should only be called if this was a non-nested interrupt.

Parameters
:   | check\_reschedule | If nonzero, additionally invoke scheduling logic |
    | --- | --- |

## [◆ ](#ga1ab99dbeb50b228001e1fca808cbaeea)ISR\_DIRECT\_HEADER

| #define ISR\_DIRECT\_HEADER | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[irq.h](irq_8h.md)>`

**Value:**

[ARCH\_ISR\_DIRECT\_HEADER](arch_2arc_2v2_2irq_8h.md#a6c6d57983c066fe8ab21a78f86f7adb3)()

[ARCH\_ISR\_DIRECT\_HEADER](arch_2arc_2v2_2irq_8h.md#a6c6d57983c066fe8ab21a78f86f7adb3)

#define ARCH\_ISR\_DIRECT\_HEADER()

**Definition** irq.h:110

Common tasks before executing the body of an ISR.

This macro must be at the beginning of all direct interrupts and performs minimal architecture-specific tasks before the ISR itself can run. It takes no arguments and has no return value.

## [◆ ](#ga3c1327551dfca7818975e3fbf1470227)ISR\_DIRECT\_PM

| #define ISR\_DIRECT\_PM | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[irq.h](irq_8h.md)>`

**Value:**

[ARCH\_ISR\_DIRECT\_PM](arch_2arm_2irq_8h.md#a491cb79acec18c83b9a61b0b45dfab69)()

[ARCH\_ISR\_DIRECT\_PM](arch_2arm_2irq_8h.md#a491cb79acec18c83b9a61b0b45dfab69)

#define ARCH\_ISR\_DIRECT\_PM()

**Definition** irq.h:138

Perform power management idle exit logic.

This macro may optionally be invoked somewhere in between IRQ\_DIRECT\_HEADER() and IRQ\_DIRECT\_FOOTER() invocations. It performs tasks necessary to exit power management idle state. It takes no parameters and returns no arguments. It may be omitted, but be careful!

## Function Documentation

## [◆ ](#ga4e9915b92b09df49b99bc449f0cc31a1)irq\_connect\_dynamic()

| | int irq\_connect\_dynamic | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *priority*, | |  |  | void(\* | *routine*)(const void \*parameter), | |  |  | const void \* | *parameter*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[irq.h](irq_8h.md)>`

Configure a dynamic interrupt.

Use this instead of [IRQ\_CONNECT()](#ga131739d1faf501a15590053817aba984) if arguments cannot be known at build time.

Parameters
:   | irq | IRQ line number |
    | --- | --- |
    | priority | Interrupt priority |
    | routine | Interrupt service routine |
    | parameter | ISR parameter |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Arch-specific IRQ configuration flags |

Returns
:   The vector assigned to this interrupt

## [◆ ](#gabdab7745edc1e15862e1772d8673fc00)irq\_disconnect\_dynamic()

| | int irq\_disconnect\_dynamic | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *priority*, | |  |  | void(\* | *routine*)(const void \*parameter), | |  |  | const void \* | *parameter*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[irq.h](irq_8h.md)>`

Disconnect a dynamic interrupt.

Use this in conjunction with shared interrupts to remove a routine/parameter pair from the list of clients using the same interrupt line. If the interrupt is not being shared then the associated \_sw\_isr\_table entry will be replaced by (NULL, z\_irq\_spurious) (default entry).

Parameters
:   | irq | IRQ line number |
    | --- | --- |
    | priority | Interrupt priority |
    | routine | Interrupt service routine |
    | parameter | ISR parameter |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Arch-specific IRQ configuration flags |

Returns
:   0 in case of success, negative value otherwise

## [◆ ](#ga8482b0dd2283d12677a9ebe321667d16)k\_is\_in\_isr()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_is\_in\_isr | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Determine if code is running at interrupt level.

This routine allows the caller to customize its actions, depending on whether it is a thread or an ISR.

Function properties (list may not be complete)

Returns
:   false if invoked by a thread.
:   true if invoked by an ISR.

## [◆ ](#gae74e5de996276df767b96d4b50fa47ea)k\_is\_pre\_kernel()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_is\_pre\_kernel | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestaticisr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Test whether startup is in the before-main-task phase.

This routine allows the caller to customize its actions, depending on whether it being invoked before the kernel is fully active.

Function properties (list may not be complete)

Returns
:   true if invoked before post-kernel initialization
:   false if invoked during/after post-kernel initialization

## [◆ ](#ga91e1cf0dc7fc93a3214cadb74ed86666)k\_is\_preempt\_thread()

| | int k\_is\_preempt\_thread | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Determine if code is running in a preemptible thread.

This routine allows the caller to customize its actions, depending on whether it can be preempted by another thread. The routine returns a 'true' value if all of the following conditions are met:

- The code is running in a thread, not at ISR.
- The thread's priority is in the preemptible range.
- The thread has not locked the scheduler.

Function properties (list may not be complete)

Returns
:   0 if invoked by an ISR or by a cooperative thread.
:   Non-zero if invoked by a preemptible thread.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
