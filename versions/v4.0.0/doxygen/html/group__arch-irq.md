---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__arch-irq.html
original_path: doxygen/html/group__arch-irq.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture-specific IRQ APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

| Functions | |
| --- | --- |
| static \_Bool | [arch\_is\_in\_isr](#gaee3fe4c82d94c4d307ea3e1169eb9573) (void) |
|  | Test if the current context is in interrupt context. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_irq\_lock](#ga25bca3069cb999b6d4f924b87bf7de38) (void) |
|  | Lock interrupts on the current CPU. |
| static void | [arch\_irq\_unlock](#gaa2b2745d8e99b8730b44805f4d3bbf05) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
|  | Unlock interrupts on the current CPU. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_irq\_unlocked](#ga1b827afafc622d412962f568b78726dc) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
|  | Test if calling [arch\_irq\_unlock()](#gaa2b2745d8e99b8730b44805f4d3bbf05) with this key would unlock irqs. |
| void | [arch\_irq\_disable](#ga216d692e87bfba955a60f8e570e127df) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Disable the specified interrupt line. |
| void | [arch\_irq\_enable](#gaa278d630653b33cb339621d725ed295a) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Enable the specified interrupt line. |
| int | [arch\_irq\_is\_enabled](#ga3bd8e963a124421bb372dab4bdc6cd83) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Test if an interrupt line is enabled. |
| int | [arch\_irq\_connect\_dynamic](#gaa4d733913e12a12e104dc4781cca7308) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Arch-specific hook to install a dynamic interrupt. |
| int | [arch\_irq\_disconnect\_dynamic](#ga41483a9fc1090d96d066e107a74ee38c) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Arch-specific hook to dynamically uninstall a shared interrupt. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_irq\_allocate](#gaac8f60e7dfc5ce3222372798e96316ae) (void) |
|  | Arch-specific hook for allocating IRQs. |
| void | [arch\_irq\_set\_used](#ga5f0942bd035c50c9d2d91ada472f37c4) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Arch-specific hook for declaring an IRQ being used. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_irq\_is\_used](#ga5c85d7bf54a83190ed27587dc5a01de5) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Arch-specific hook for checking if an IRQ is being used already. |

## Detailed Description

## Function Documentation

## [◆ ](#gaac8f60e7dfc5ce3222372798e96316ae)arch\_irq\_allocate()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_irq\_allocate | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Arch-specific hook for allocating IRQs.

Note: disable/enable IRQ relevantly inside the implementation of such function to avoid concurrency issues. Also, an allocated IRQ is assumed to be used thus a following

See also
:   [arch\_irq\_is\_used()](#ga5c85d7bf54a83190ed27587dc5a01de5) should return [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7).

Returns
:   The newly allocated IRQ or UINT\_MAX on error.

## [◆ ](#gaa4d733913e12a12e104dc4781cca7308)arch\_irq\_connect\_dynamic()

| int arch\_irq\_connect\_dynamic | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *priority*, |
|  |  | void(\* | *routine*)(const void \*parameter), |
|  |  | const void \* | *parameter*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Arch-specific hook to install a dynamic interrupt.

Parameters
:   | irq | IRQ line number |
    | --- | --- |
    | priority | Interrupt priority |
    | routine | Interrupt service routine |
    | parameter | ISR parameter |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Arch-specific IRQ configuration flag |

Returns
:   The vector assigned to this interrupt

## [◆ ](#ga216d692e87bfba955a60f8e570e127df)arch\_irq\_disable()

| void arch\_irq\_disable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Disable the specified interrupt line.

Note
:   : The behavior of interrupts that arrive after this call returns and before the corresponding call to [arch\_irq\_enable()](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa) is undefined. The hardware is not required to latch and deliver such an interrupt, though on some architectures that may work. Other architectures will simply lose such an interrupt and never deliver it. Many drivers and subsystems are not tolerant of such dropped interrupts and it is the job of the application layer to ensure that behavior remains correct.

See also
:   [irq\_disable()](group__isr__apis.md#ga82c3a15d812f58e0f6525f358d031e6d "Disable an IRQ.")

## [◆ ](#ga41483a9fc1090d96d066e107a74ee38c)arch\_irq\_disconnect\_dynamic()

| int arch\_irq\_disconnect\_dynamic | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *priority*, |
|  |  | void(\* | *routine*)(const void \*parameter), |
|  |  | const void \* | *parameter*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Arch-specific hook to dynamically uninstall a shared interrupt.

If the interrupt is not being shared, then the associated \_sw\_isr\_table entry will be replaced by (NULL, z\_irq\_spurious) (default entry).

Parameters
:   | irq | IRQ line number |
    | --- | --- |
    | priority | Interrupt priority |
    | routine | Interrupt service routine |
    | parameter | ISR parameter |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Arch-specific IRQ configuration flag |

Returns
:   0 in case of success, negative value otherwise

## [◆ ](#gaa278d630653b33cb339621d725ed295a)arch\_irq\_enable()

| void arch\_irq\_enable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Enable the specified interrupt line.

See also
:   [irq\_enable()](group__isr__apis.md#ga7ea700ee31e4ff036c997a554dbedfeb "Enable an IRQ.")

## [◆ ](#ga3bd8e963a124421bb372dab4bdc6cd83)arch\_irq\_is\_enabled()

| int arch\_irq\_is\_enabled | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Test if an interrupt line is enabled.

See also
:   [irq\_is\_enabled()](group__isr__apis.md#ga71fef3867ba9818cf0a5baf8410a6354 "Get IRQ enable state.")

## [◆ ](#ga5c85d7bf54a83190ed27587dc5a01de5)arch\_irq\_is\_used()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_irq\_is\_used | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Arch-specific hook for checking if an IRQ is being used already.

Parameters
:   | irq | the IRQ to check |
    | --- | --- |

Returns
:   true if being, false otherwise

## [◆ ](#ga25bca3069cb999b6d4f924b87bf7de38)arch\_irq\_lock()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_irq\_lock | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Lock interrupts on the current CPU.

See also
:   [irq\_lock()](group__isr__apis.md#ga19fdde73c3b02fcca6cf1d1e67631228 "Lock interrupts.")

## [◆ ](#ga5f0942bd035c50c9d2d91ada472f37c4)arch\_irq\_set\_used()

| void arch\_irq\_set\_used | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Arch-specific hook for declaring an IRQ being used.

Note: disable/enable IRQ relevantly inside the implementation of such function to avoid concurrency issues.

Parameters
:   | irq | the IRQ to declare being used |
    | --- | --- |

## [◆ ](#gaa2b2745d8e99b8730b44805f4d3bbf05)arch\_irq\_unlock()

| | void arch\_irq\_unlock | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Unlock interrupts on the current CPU.

See also
:   [irq\_unlock()](group__isr__apis.md#ga646045943b3b2a130738bcc48867bf57 "Unlock interrupts.")

## [◆ ](#ga1b827afafc622d412962f568b78726dc)arch\_irq\_unlocked()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_irq\_unlocked | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Test if calling [arch\_irq\_unlock()](#gaa2b2745d8e99b8730b44805f4d3bbf05) with this key would unlock irqs.

Parameters
:   | key | value returned by [arch\_irq\_lock()](#ga25bca3069cb999b6d4f924b87bf7de38) |
    | --- | --- |

Returns
:   true if interrupts were unlocked prior to the [arch\_irq\_lock()](#ga25bca3069cb999b6d4f924b87bf7de38) call that produced the key argument.

## [◆ ](#gaee3fe4c82d94c4d307ea3e1169eb9573)arch\_is\_in\_isr()

| | \_Bool arch\_is\_in\_isr | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Test if the current context is in interrupt context.

XXX: This is inconsistently handled among arches wrt exception context See: #17656

Returns
:   true if we are in interrupt context

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
