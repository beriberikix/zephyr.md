---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arch_2arm_2irq_8h.html
original_path: doxygen/html/arch_2arm_2irq_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h File Reference

ARM AArch32 public interrupt handling.
[More...](#details)

`#include <[zephyr/sw_isr_table.h](sw__isr__table_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](arch_2arm_2irq_8h_source.md)

| Macros | |
| --- | --- |
| #define | [arch\_irq\_enable](#a5ea6488112b97755b13583cd2832c2fa)(irq) |
| #define | [arch\_irq\_disable](#a19b436a206500c3748ad5c32050db241)(irq) |
| #define | [arch\_irq\_is\_enabled](#ae95daf1bea993f1d03adaf31fc44c369)(irq) |
| #define | [IRQ\_ZERO\_LATENCY](#a1b5d8b88524f2fd81f32ed675c832a57)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Set this interrupt up as a zero-latency IRQ. |
| #define | [ARCH\_IRQ\_CONNECT](#accdf8a59e00ac1c1fcedc18b78be4b8a)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
| #define | [ARCH\_IRQ\_DIRECT\_CONNECT](#a875f2b1ca924721fe3854796bd96c2db)(irq\_p, priority\_p, isr\_p, flags\_p) |
| #define | [ARCH\_ISR\_DIRECT\_PM](#a491cb79acec18c83b9a61b0b45dfab69)() |
| #define | [ARCH\_ISR\_DIRECT\_HEADER](#a6c6d57983c066fe8ab21a78f86f7adb3)() |
| #define | [ARCH\_ISR\_DIRECT\_FOOTER](#aa7c471213fa28b3685f153ea2a72cf9d)(swap) |
| #define | [ARCH\_ISR\_DIAG\_OFF](#aea327928797d5f8a059ee3578cff9f91) |
| #define | [ARCH\_ISR\_DIAG\_ON](#ad6a5dc7416190e63eb601df2d3eab164) |
| #define | [ARCH\_ISR\_DIRECT\_DECLARE](#a5279598e93dd914614a2ae52557be1a5)(name) |

| Functions | |
| --- | --- |
| void | [arm\_irq\_enable](#a9bdba7b8dc9e2f1fa15309f7ed5be0e3) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| void | [arm\_irq\_disable](#ab21a38f95ce639a300012017626d715c) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| int | [arm\_irq\_is\_enabled](#a7a9dd209281ffee41f196ac973972aa3) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| void | [arm\_irq\_priority\_set](#a5541a808bd36f598c9f4f93cee1231e5) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| static void | [arch\_isr\_direct\_header](#ac8579cbf5edce72a6a4bfbbed3166683) (void) |
| static void | [arch\_isr\_direct\_footer](#a678e87bf86d19e45c2fcb95ec969465b) (int maybe\_swap) |

## Detailed Description

ARM AArch32 public interrupt handling.

ARM AArch32-specific kernel interrupt handling interface. Included by [arm/arch.h](arm_2arch_8h.md "ARM AArch32 specific kernel interface header.").

## Macro Definition Documentation

## [◆ ](#accdf8a59e00ac1c1fcedc18b78be4b8a)ARCH\_IRQ\_CONNECT

| #define ARCH\_IRQ\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *isr\_param\_p*, |
|  |  |  | *flags\_p* ) |

**Value:**

{ \

BUILD\_ASSERT([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_ZERO\_LATENCY\_IRQS) || !(flags\_p & [IRQ\_ZERO\_LATENCY](#a1b5d8b88524f2fd81f32ed675c832a57)), \

"ZLI interrupt registered but feature is disabled"); \

\_CHECK\_PRIO(priority\_p, flags\_p) \

Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

z\_arm\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

}

[IRQ\_ZERO\_LATENCY](#a1b5d8b88524f2fd81f32ed675c832a57)

#define IRQ\_ZERO\_LATENCY

Set this interrupt up as a zero-latency IRQ.

**Definition** irq.h:89

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

## [◆ ](#a875f2b1ca924721fe3854796bd96c2db)ARCH\_IRQ\_DIRECT\_CONNECT

| #define ARCH\_IRQ\_DIRECT\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *flags\_p* ) |

**Value:**

{ \

BUILD\_ASSERT([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_ZERO\_LATENCY\_IRQS) || !(flags\_p & [IRQ\_ZERO\_LATENCY](#a1b5d8b88524f2fd81f32ed675c832a57)), \

"ZLI interrupt registered but feature is disabled"); \

\_CHECK\_PRIO(priority\_p, flags\_p) \

Z\_ISR\_DECLARE\_DIRECT(irq\_p, [ISR\_FLAG\_DIRECT](sw__isr__table_8h.md#a1376eec61303fcd20e7656175ddbaf19), isr\_p); \

z\_arm\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

}

[ISR\_FLAG\_DIRECT](sw__isr__table_8h.md#a1376eec61303fcd20e7656175ddbaf19)

#define ISR\_FLAG\_DIRECT

This interrupt gets put directly in the vector table.

**Definition** sw\_isr\_table.h:188

## [◆ ](#a19b436a206500c3748ad5c32050db241)arch\_irq\_disable

| #define arch\_irq\_disable | ( |  | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[arm\_irq\_disable](#ab21a38f95ce639a300012017626d715c)(irq)

[arm\_irq\_disable](#ab21a38f95ce639a300012017626d715c)

void arm\_irq\_disable(unsigned int irq)

## [◆ ](#a5ea6488112b97755b13583cd2832c2fa)arch\_irq\_enable

| #define arch\_irq\_enable | ( |  | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[arm\_irq\_enable](#a9bdba7b8dc9e2f1fa15309f7ed5be0e3)(irq)

[arm\_irq\_enable](#a9bdba7b8dc9e2f1fa15309f7ed5be0e3)

void arm\_irq\_enable(unsigned int irq)

## [◆ ](#ae95daf1bea993f1d03adaf31fc44c369)arch\_irq\_is\_enabled

| #define arch\_irq\_is\_enabled | ( |  | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[arm\_irq\_is\_enabled](#a7a9dd209281ffee41f196ac973972aa3)(irq)

[arm\_irq\_is\_enabled](#a7a9dd209281ffee41f196ac973972aa3)

int arm\_irq\_is\_enabled(unsigned int irq)

## [◆ ](#aea327928797d5f8a059ee3578cff9f91)ARCH\_ISR\_DIAG\_OFF

| #define ARCH\_ISR\_DIAG\_OFF |
| --- |

**Value:**

[TOOLCHAIN\_DISABLE\_CLANG\_WARNING](toolchain_8h.md#ac4bfe24556e3dd2bfb093434a4e98517)([TOOLCHAIN\_WARNING\_EXTRA](toolchain_8h.md#a64d8f26c21ee3639e82d93783e09387e)) \

TOOLCHAIN\_DISABLE\_GCC\_WARNING([TOOLCHAIN\_WARNING\_ATTRIBUTES](toolchain_8h.md#a5f5fef9bda4762c368f26c9028cdd34a)) \

TOOLCHAIN\_DISABLE\_IAR\_WARNING([TOOLCHAIN\_WARNING\_ATTRIBUTES](toolchain_8h.md#a5f5fef9bda4762c368f26c9028cdd34a))

[TOOLCHAIN\_WARNING\_ATTRIBUTES](toolchain_8h.md#a5f5fef9bda4762c368f26c9028cdd34a)

#define TOOLCHAIN\_WARNING\_ATTRIBUTES

Toolchain-specific warning for unknown attributes.

**Definition** toolchain.h:168

[TOOLCHAIN\_WARNING\_EXTRA](toolchain_8h.md#a64d8f26c21ee3639e82d93783e09387e)

#define TOOLCHAIN\_WARNING\_EXTRA

Toolchain-specific warning for extra warnings.

**Definition** toolchain.h:191

[TOOLCHAIN\_DISABLE\_CLANG\_WARNING](toolchain_8h.md#ac4bfe24556e3dd2bfb093434a4e98517)

#define TOOLCHAIN\_DISABLE\_CLANG\_WARNING(warning)

Disable the specified compiler warning for clang.

**Definition** toolchain.h:272

## [◆ ](#ad6a5dc7416190e63eb601df2d3eab164)ARCH\_ISR\_DIAG\_ON

| #define ARCH\_ISR\_DIAG\_ON |
| --- |

**Value:**

[TOOLCHAIN\_ENABLE\_CLANG\_WARNING](toolchain_8h.md#a35eaaf7a69eae890687c196e81304667)([TOOLCHAIN\_WARNING\_EXTRA](toolchain_8h.md#a64d8f26c21ee3639e82d93783e09387e)) \

TOOLCHAIN\_ENABLE\_GCC\_WARNING([TOOLCHAIN\_WARNING\_ATTRIBUTES](toolchain_8h.md#a5f5fef9bda4762c368f26c9028cdd34a)) \

TOOLCHAIN\_ENABLE\_IAR\_WARNING([TOOLCHAIN\_WARNING\_ATTRIBUTES](toolchain_8h.md#a5f5fef9bda4762c368f26c9028cdd34a))

[TOOLCHAIN\_ENABLE\_CLANG\_WARNING](toolchain_8h.md#a35eaaf7a69eae890687c196e81304667)

#define TOOLCHAIN\_ENABLE\_CLANG\_WARNING(warning)

Re-enable the specified compiler warning for clang.

**Definition** toolchain.h:282

## [◆ ](#a5279598e93dd914614a2ae52557be1a5)ARCH\_ISR\_DIRECT\_DECLARE

| #define ARCH\_ISR\_DIRECT\_DECLARE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static inline int name##\_body(void); \

ARCH\_ISR\_DIAG\_OFF \

\_\_attribute\_\_ ((interrupt ("IRQ"))) void name(void) \

{ \

int check\_reschedule; \

ISR\_DIRECT\_HEADER(); \

check\_reschedule = name##\_body(); \

ISR\_DIRECT\_FOOTER(check\_reschedule); \

} \

ARCH\_ISR\_DIAG\_ON \

static inline int name##\_body(void)

## [◆ ](#aa7c471213fa28b3685f153ea2a72cf9d)ARCH\_ISR\_DIRECT\_FOOTER

| #define ARCH\_ISR\_DIRECT\_FOOTER | ( |  | *swap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[arch\_isr\_direct\_footer](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)(swap)

[arch\_isr\_direct\_footer](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)

static void arch\_isr\_direct\_footer(int maybe\_swap)

**Definition** irq.h:98

## [◆ ](#a6c6d57983c066fe8ab21a78f86f7adb3)ARCH\_ISR\_DIRECT\_HEADER

| #define ARCH\_ISR\_DIRECT\_HEADER | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

[arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)()

[arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)

static void arch\_isr\_direct\_header(void)

**Definition** irq.h:91

## [◆ ](#a491cb79acec18c83b9a61b0b45dfab69)ARCH\_ISR\_DIRECT\_PM

| #define ARCH\_ISR\_DIRECT\_PM | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

do { } while (false)

## [◆ ](#a1b5d8b88524f2fd81f32ed675c832a57)IRQ\_ZERO\_LATENCY

| #define IRQ\_ZERO\_LATENCY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Set this interrupt up as a zero-latency IRQ.

If CONFIG\_ZERO\_LATENCY\_LEVELS is 1 it has a fixed hardware priority level (discarding what was supplied in the interrupt's priority argument). If CONFIG\_ZERO\_LATENCY\_LEVELS is greater 1 it has the priority level assigned by the argument. The interrupt will run even if [irq\_lock()](group__isr__apis.md#ga19fdde73c3b02fcca6cf1d1e67631228 "Lock interrupts.") is active. Be careful!

## Function Documentation

## [◆ ](#a678e87bf86d19e45c2fcb95ec969465b)arch\_isr\_direct\_footer()

| | void arch\_isr\_direct\_footer | ( | int | *maybe\_swap* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac8579cbf5edce72a6a4bfbbed3166683)arch\_isr\_direct\_header()

| | void arch\_isr\_direct\_header | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab21a38f95ce639a300012017626d715c)arm\_irq\_disable()

| | void arm\_irq\_disable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9bdba7b8dc9e2f1fa15309f7ed5be0e3)arm\_irq\_enable()

| | void arm\_irq\_enable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a7a9dd209281ffee41f196ac973972aa3)arm\_irq\_is\_enabled()

| | int arm\_irq\_is\_enabled | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5541a808bd36f598c9f4f93cee1231e5)arm\_irq\_priority\_set()

| | void arm\_irq\_priority\_set | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *prio*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [irq.h](arch_2arm_2irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
