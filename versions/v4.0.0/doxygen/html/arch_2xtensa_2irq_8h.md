---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2xtensa_2irq_8h.html
original_path: doxygen/html/arch_2xtensa_2irq_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <xtensa/config/core-isa.h>`  
`#include <[zephyr/irq.h](irq_8h_source.md)>`

[Go to the source code of this file.](arch_2xtensa_2irq_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CONFIG\_GEN\_IRQ\_START\_VECTOR](#a8216dd1abd78c9fd201320bed1496c1c)   0 |
| #define | [CONFIG\_NUM\_IRQS](#a8f2a902348157b3b8718b05df1b1e837)   XCHAL\_NUM\_INTERRUPTS |
| #define | [arch\_irq\_enable](#a5ea6488112b97755b13583cd2832c2fa)(irq) |
| #define | [arch\_irq\_disable](#a19b436a206500c3748ad5c32050db241)(irq) |
| #define | [arch\_irq\_is\_enabled](#ae95daf1bea993f1d03adaf31fc44c369)(irq) |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [xtensa\_irq\_enable](#a9d6c92219fd2390f777aff106d2eafa9) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
|  | Enable interrupt on Xtensa core. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [xtensa\_irq\_disable](#a37d1c0641f471e9492c2493c77327c96) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
|  | Disable interrupt on Xtensa core. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_irq\_lock](#a1496f4f860a99f42e1aee15ce5c9b3e2) (void) |
|  | Implementation of [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2 "arch_irq_lock"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_irq\_unlock](#a203e02b994beba0d006dad9f6d797c27) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
|  | Implementation of [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27 "arch_irq_unlock"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_irq\_unlocked](#adb441b26ed6818fea4ebba6b8853354b) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
|  | Implementation of [arch\_irq\_unlocked](arch_2arc_2v2_2irq_8h.md#adb441b26ed6818fea4ebba6b8853354b "arch_irq_unlocked"). |
| int | [xtensa\_irq\_is\_enabled](#ae6e10f2a35e679c41c11700330ce8b7a) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Query if an interrupt is enabled on Xtensa core. |

## Macro Definition Documentation

## [◆ ](#a19b436a206500c3748ad5c32050db241)arch\_irq\_disable

| #define arch\_irq\_disable | ( |  | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[xtensa\_irq\_disable](#a37d1c0641f471e9492c2493c77327c96)(irq)

[xtensa\_irq\_disable](#a37d1c0641f471e9492c2493c77327c96)

static ALWAYS\_INLINE void xtensa\_irq\_disable(uint32\_t irq)

Disable interrupt on Xtensa core.

**Definition** irq.h:128

## [◆ ](#a5ea6488112b97755b13583cd2832c2fa)arch\_irq\_enable

| #define arch\_irq\_enable | ( |  | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[xtensa\_irq\_enable](#a9d6c92219fd2390f777aff106d2eafa9)(irq)

[xtensa\_irq\_enable](#a9d6c92219fd2390f777aff106d2eafa9)

static ALWAYS\_INLINE void xtensa\_irq\_enable(uint32\_t irq)

Enable interrupt on Xtensa core.

**Definition** irq.h:118

## [◆ ](#ae95daf1bea993f1d03adaf31fc44c369)arch\_irq\_is\_enabled

| #define arch\_irq\_is\_enabled | ( |  | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[xtensa\_irq\_is\_enabled](#ae6e10f2a35e679c41c11700330ce8b7a)(irq)

[xtensa\_irq\_is\_enabled](#ae6e10f2a35e679c41c11700330ce8b7a)

int xtensa\_irq\_is\_enabled(unsigned int irq)

Query if an interrupt is enabled on Xtensa core.

## [◆ ](#a8216dd1abd78c9fd201320bed1496c1c)CONFIG\_GEN\_IRQ\_START\_VECTOR

| #define CONFIG\_GEN\_IRQ\_START\_VECTOR   0 |
| --- |

## [◆ ](#a8f2a902348157b3b8718b05df1b1e837)CONFIG\_NUM\_IRQS

| #define CONFIG\_NUM\_IRQS   XCHAL\_NUM\_INTERRUPTS |
| --- |

## Function Documentation

## [◆ ](#a1496f4f860a99f42e1aee15ce5c9b3e2)arch\_irq\_lock()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_irq\_lock | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2 "arch_irq_lock").

## [◆ ](#a203e02b994beba0d006dad9f6d797c27)arch\_irq\_unlock()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_irq\_unlock | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27 "arch_irq_unlock").

## [◆ ](#adb441b26ed6818fea4ebba6b8853354b)arch\_irq\_unlocked()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_irq\_unlocked | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_irq\_unlocked](arch_2arc_2v2_2irq_8h.md#adb441b26ed6818fea4ebba6b8853354b "arch_irq_unlocked").

## [◆ ](#a37d1c0641f471e9492c2493c77327c96)xtensa\_irq\_disable()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void xtensa\_irq\_disable | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Disable interrupt on Xtensa core.

Parameters
:   | irq | Interrupt to be disabled. |
    | --- | --- |

## [◆ ](#a9d6c92219fd2390f777aff106d2eafa9)xtensa\_irq\_enable()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void xtensa\_irq\_enable | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Enable interrupt on Xtensa core.

Parameters
:   | irq | Interrupt to be enabled. |
    | --- | --- |

## [◆ ](#ae6e10f2a35e679c41c11700330ce8b7a)xtensa\_irq\_is\_enabled()

| int xtensa\_irq\_is\_enabled | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Query if an interrupt is enabled on Xtensa core.

Parameters
:   | irq | Interrupt to be queried. |
    | --- | --- |

Returns
:   True if interrupt is enabled, false otherwise.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [irq.h](arch_2xtensa_2irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
