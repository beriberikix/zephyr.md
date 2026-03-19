---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/irq_8h.html
original_path: doxygen/html/irq_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h File Reference

Public interface for configuring interrupts.
[More...](#details)

`#include <[zephyr/arch/cpu.h](cpu_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](irq_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IRQ\_CONNECT](group__isr__apis.md#ga131739d1faf501a15590053817aba984)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
|  | Initialize an interrupt handler. |
| #define | [IRQ\_DIRECT\_CONNECT](group__isr__apis.md#gac6c8746ac28da6ce02b24714f4144ff3)(irq\_p, priority\_p, isr\_p, flags\_p) |
|  | Initialize a 'direct' interrupt handler. |
| #define | [ISR\_DIRECT\_HEADER](group__isr__apis.md#ga1ab99dbeb50b228001e1fca808cbaeea)() |
|  | Common tasks before executing the body of an ISR. |
| #define | [ISR\_DIRECT\_FOOTER](group__isr__apis.md#ga31581157c9dbacf935f0e6a8dd456335)(check\_reschedule) |
|  | Common tasks before exiting the body of an ISR. |
| #define | [ISR\_DIRECT\_PM](group__isr__apis.md#ga3c1327551dfca7818975e3fbf1470227)() |
|  | Perform power management idle exit logic. |
| #define | [ISR\_DIRECT\_DECLARE](group__isr__apis.md#gaf86866cd07fd37f381d98866f8874ebf)(name) |
|  | Helper macro to declare a direct interrupt service routine. |
| #define | [irq\_lock](group__isr__apis.md#ga19fdde73c3b02fcca6cf1d1e67631228)() |
|  | Lock interrupts. |
| #define | [irq\_unlock](group__isr__apis.md#ga646045943b3b2a130738bcc48867bf57)(key) |
|  | Unlock interrupts. |
| #define | [irq\_enable](group__isr__apis.md#ga7ea700ee31e4ff036c997a554dbedfeb)(irq) |
|  | Enable an IRQ. |
| #define | [irq\_disable](group__isr__apis.md#ga82c3a15d812f58e0f6525f358d031e6d)(irq) |
|  | Disable an IRQ. |
| #define | [irq\_is\_enabled](group__isr__apis.md#ga71fef3867ba9818cf0a5baf8410a6354)(irq) |
|  | Get IRQ enable state. |

| Functions | |
| --- | --- |
| static int | [irq\_connect\_dynamic](group__isr__apis.md#ga4e9915b92b09df49b99bc449f0cc31a1) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Configure a dynamic interrupt. |
| static int | [irq\_disconnect\_dynamic](group__isr__apis.md#gabdab7745edc1e15862e1772d8673fc00) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Disconnect a dynamic interrupt. |

## Detailed Description

Public interface for configuring interrupts.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [irq.h](irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
