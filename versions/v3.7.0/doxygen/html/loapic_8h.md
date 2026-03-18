---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/loapic_8h.html
original_path: doxygen/html/loapic_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

loapic.h File Reference

`#include <[zephyr/arch/cpu.h](cpu_8h_source.md)>`  
`#include <[zephyr/arch/x86/msr.h](msr_8h_source.md)>`  
`#include <[zephyr/sys/device_mmio.h](device__mmio_8h_source.md)>`

[Go to the source code of this file.](loapic_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LOAPIC\_ID](#aabaee35aa87c8c7e9dbd8e4ca04ec5fa)   0x020 /\* Local APIC ID Reg \*/ |
| #define | [LOAPIC\_VER](#a6865f3d12fa22ca44d37c555595f9a82)   0x030 /\* Local APIC Version Reg \*/ |
| #define | [LOAPIC\_TPR](#ab821cf0c98ad7eaa74e682de764f8802)   0x080 /\* Task Priority Reg \*/ |
| #define | [LOAPIC\_APR](#a22b09ea2abe05d6dc693d9891b1b10dc)   0x090 /\* Arbitration Priority Reg \*/ |
| #define | [LOAPIC\_PPR](#ab2ffcef005ced8514635a628ca13462f)   0x0a0 /\* Processor Priority Reg \*/ |
| #define | [LOAPIC\_EOI](#a5cc8ffe88a717189312314661d489e52)   0x0b0 /\* EOI Reg \*/ |
| #define | [LOAPIC\_LDR](#abc2a39fa145706f72295cd34a5e89862)   0x0d0 /\* Logical Destination Reg \*/ |
| #define | [LOAPIC\_DFR](#a43f1bb7e6e9492bddfe8dd00ab789f51)   0x0e0 /\* Destination Format Reg \*/ |
| #define | [LOAPIC\_SVR](#abf0572a04563cff27b01acde823b75d0)   0x0f0 /\* Spurious Interrupt Reg \*/ |
| #define | [LOAPIC\_ISR](#acba6145af5fd413d8985f700b7376881)   0x100 /\* In-service Reg \*/ |
| #define | [LOAPIC\_TMR](#a8c2a2d604d222ecd9d1e91ebd1793877)   0x180 /\* Trigger Mode Reg \*/ |
| #define | [LOAPIC\_IRR](#a98b3ebb077835af6b185953a260ee62c)   0x200 /\* Interrupt Request Reg \*/ |
| #define | [LOAPIC\_ESR](#a610671b710fafe94cc41631d8275d4b5)   0x280 /\* Error Status Reg \*/ |
| #define | [LOAPIC\_ICRLO](#a29270aa4461ff9a94bda5ef2dd59e950)   0x300 /\* Interrupt Command Reg \*/ |
| #define | [LOAPIC\_ICRHI](#a5d5cd6ba2e4ca22fc15f666e0231bc6e)   0x310 /\* Interrupt Command Reg \*/ |
| #define | [LOAPIC\_TIMER](#ad2c049f84d86360481bf39f1c769d33a)   0x320 /\* LVT (Timer) \*/ |
| #define | [LOAPIC\_THERMAL](#a909c6e0ee5fc88de8f444436ea3cfdac)   0x330 /\* LVT (Thermal) \*/ |
| #define | [LOAPIC\_PMC](#a3eb80c82f8f006729add8777f99d545b)   0x340 /\* LVT (PMC) \*/ |
| #define | [LOAPIC\_LINT0](#a1353f571e91132ca48eec99b9de70803)   0x350 /\* LVT (LINT0) \*/ |
| #define | [LOAPIC\_LINT1](#a7293b3baa5944f0f8ef80533483a8b58)   0x360 /\* LVT (LINT1) \*/ |
| #define | [LOAPIC\_ERROR](#ab7911822a48695ea33abe3321623fe98)   0x370 /\* LVT (ERROR) \*/ |
| #define | [LOAPIC\_TIMER\_ICR](#a32f96a18492f74193e60ed7b58c66018)   0x380 /\* Timer Initial Count Reg \*/ |
| #define | [LOAPIC\_TIMER\_CCR](#a33fd2d6104705d5b222d7a40133608b9)   0x390 /\* Timer Current Count Reg \*/ |
| #define | [LOAPIC\_TIMER\_CONFIG](#a9033fab28d4760b5861984890a31589e)   0x3e0 /\* Timer Divide Config Reg \*/ |
| #define | [LOAPIC\_SELF\_IPI](#aeea0b064b955e73205f882cd80132455)   0x3f0 /\* Self IPI Reg, only support in X2APIC mode \*/ |
| #define | [LOAPIC\_ICR\_BUSY](#a7a95e68934f45e785ac88345d751ef00)   0x00001000 /\* delivery status: 1 = busy \*/ |
| #define | [LOAPIC\_ICR\_IPI\_OTHERS](#af2037e08d1e66a8ac00b71c944bc36aa)   0x000C4000U /\* normal IPI to other CPUs \*/ |
| #define | [LOAPIC\_ICR\_IPI\_INIT](#aeda0d6d2a4bc948dc97c1b548e0b424a)   0x00004500U |
| #define | [LOAPIC\_ICR\_IPI\_STARTUP](#a256c3ccf1e2dd2f7dd0f6c7006aab99c)   0x00004600U |
| #define | [LOAPIC\_LVT\_MASKED](#a4da1bd27f6148a30f40eebe70c890a4b)   0x00010000 /\* mask \*/ |
| #define | [LOAPIC\_REGS\_STR](#a83cfcf18004022e6f77a5db51a7521cc)   loapic\_regs /\* mmio [device](structdevice.md) name \*/ |

| Functions | |
| --- | --- |
|  | [DEVICE\_MMIO\_TOPLEVEL\_DECLARE](#a6fab4c5cc1444a7f69cc0ae005e6c582) (loapic\_regs) |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x86\_read\_x2apic](#a797471308f74780dfcec277b18853fca) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
|  | Read 64-bit value from the local APIC in x2APIC mode. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [x86\_read\_xapic](#a4807ae47f62151774877f21939fafeab) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
|  | Read 32-bit value from the local APIC in xAPIC (MMIO) mode. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [x86\_read\_loapic](#a6ba00d305469ab62f89888cf0aa64033) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
|  | Read value from the local APIC using the default mode. |
| static void | [x86\_write\_x2apic](#a060a375336bf44c2dde9537d32f9416d) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Write 64-bit value to the local APIC in x2APIC mode. |
| static void | [x86\_write\_xapic](#a9d7e889e4e4718d2205f647af172762a) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Write 32-bit value to the local APIC in xAPIC (MMIO) mode. |
| static void | [x86\_write\_loapic](#a884390389c9c7cef65801bba00395e4d) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Write 32-bit value to the local APIC using the default mode. |

## Macro Definition Documentation

## [◆ ](#a22b09ea2abe05d6dc693d9891b1b10dc)LOAPIC\_APR

| #define LOAPIC\_APR   0x090 /\* Arbitration Priority Reg \*/ |
| --- |

## [◆ ](#a43f1bb7e6e9492bddfe8dd00ab789f51)LOAPIC\_DFR

| #define LOAPIC\_DFR   0x0e0 /\* Destination Format Reg \*/ |
| --- |

## [◆ ](#a5cc8ffe88a717189312314661d489e52)LOAPIC\_EOI

| #define LOAPIC\_EOI   0x0b0 /\* EOI Reg \*/ |
| --- |

## [◆ ](#ab7911822a48695ea33abe3321623fe98)LOAPIC\_ERROR

| #define LOAPIC\_ERROR   0x370 /\* LVT (ERROR) \*/ |
| --- |

## [◆ ](#a610671b710fafe94cc41631d8275d4b5)LOAPIC\_ESR

| #define LOAPIC\_ESR   0x280 /\* Error Status Reg \*/ |
| --- |

## [◆ ](#a7a95e68934f45e785ac88345d751ef00)LOAPIC\_ICR\_BUSY

| #define LOAPIC\_ICR\_BUSY   0x00001000 /\* delivery status: 1 = busy \*/ |
| --- |

## [◆ ](#aeda0d6d2a4bc948dc97c1b548e0b424a)LOAPIC\_ICR\_IPI\_INIT

| #define LOAPIC\_ICR\_IPI\_INIT   0x00004500U |
| --- |

## [◆ ](#af2037e08d1e66a8ac00b71c944bc36aa)LOAPIC\_ICR\_IPI\_OTHERS

| #define LOAPIC\_ICR\_IPI\_OTHERS   0x000C4000U /\* normal IPI to other CPUs \*/ |
| --- |

## [◆ ](#a256c3ccf1e2dd2f7dd0f6c7006aab99c)LOAPIC\_ICR\_IPI\_STARTUP

| #define LOAPIC\_ICR\_IPI\_STARTUP   0x00004600U |
| --- |

## [◆ ](#a5d5cd6ba2e4ca22fc15f666e0231bc6e)LOAPIC\_ICRHI

| #define LOAPIC\_ICRHI   0x310 /\* Interrupt Command Reg \*/ |
| --- |

## [◆ ](#a29270aa4461ff9a94bda5ef2dd59e950)LOAPIC\_ICRLO

| #define LOAPIC\_ICRLO   0x300 /\* Interrupt Command Reg \*/ |
| --- |

## [◆ ](#aabaee35aa87c8c7e9dbd8e4ca04ec5fa)LOAPIC\_ID

| #define LOAPIC\_ID   0x020 /\* Local APIC ID Reg \*/ |
| --- |

## [◆ ](#a98b3ebb077835af6b185953a260ee62c)LOAPIC\_IRR

| #define LOAPIC\_IRR   0x200 /\* Interrupt Request Reg \*/ |
| --- |

## [◆ ](#acba6145af5fd413d8985f700b7376881)LOAPIC\_ISR

| #define LOAPIC\_ISR   0x100 /\* In-service Reg \*/ |
| --- |

## [◆ ](#abc2a39fa145706f72295cd34a5e89862)LOAPIC\_LDR

| #define LOAPIC\_LDR   0x0d0 /\* Logical Destination Reg \*/ |
| --- |

## [◆ ](#a1353f571e91132ca48eec99b9de70803)LOAPIC\_LINT0

| #define LOAPIC\_LINT0   0x350 /\* LVT (LINT0) \*/ |
| --- |

## [◆ ](#a7293b3baa5944f0f8ef80533483a8b58)LOAPIC\_LINT1

| #define LOAPIC\_LINT1   0x360 /\* LVT (LINT1) \*/ |
| --- |

## [◆ ](#a4da1bd27f6148a30f40eebe70c890a4b)LOAPIC\_LVT\_MASKED

| #define LOAPIC\_LVT\_MASKED   0x00010000 /\* mask \*/ |
| --- |

## [◆ ](#a3eb80c82f8f006729add8777f99d545b)LOAPIC\_PMC

| #define LOAPIC\_PMC   0x340 /\* LVT (PMC) \*/ |
| --- |

## [◆ ](#ab2ffcef005ced8514635a628ca13462f)LOAPIC\_PPR

| #define LOAPIC\_PPR   0x0a0 /\* Processor Priority Reg \*/ |
| --- |

## [◆ ](#a83cfcf18004022e6f77a5db51a7521cc)LOAPIC\_REGS\_STR

| #define LOAPIC\_REGS\_STR   loapic\_regs /\* mmio [device](structdevice.md) name \*/ |
| --- |

## [◆ ](#aeea0b064b955e73205f882cd80132455)LOAPIC\_SELF\_IPI

| #define LOAPIC\_SELF\_IPI   0x3f0 /\* Self IPI Reg, only support in X2APIC mode \*/ |
| --- |

## [◆ ](#abf0572a04563cff27b01acde823b75d0)LOAPIC\_SVR

| #define LOAPIC\_SVR   0x0f0 /\* Spurious Interrupt Reg \*/ |
| --- |

## [◆ ](#a909c6e0ee5fc88de8f444436ea3cfdac)LOAPIC\_THERMAL

| #define LOAPIC\_THERMAL   0x330 /\* LVT (Thermal) \*/ |
| --- |

## [◆ ](#ad2c049f84d86360481bf39f1c769d33a)LOAPIC\_TIMER

| #define LOAPIC\_TIMER   0x320 /\* LVT (Timer) \*/ |
| --- |

## [◆ ](#a33fd2d6104705d5b222d7a40133608b9)LOAPIC\_TIMER\_CCR

| #define LOAPIC\_TIMER\_CCR   0x390 /\* Timer Current Count Reg \*/ |
| --- |

## [◆ ](#a9033fab28d4760b5861984890a31589e)LOAPIC\_TIMER\_CONFIG

| #define LOAPIC\_TIMER\_CONFIG   0x3e0 /\* Timer Divide Config Reg \*/ |
| --- |

## [◆ ](#a32f96a18492f74193e60ed7b58c66018)LOAPIC\_TIMER\_ICR

| #define LOAPIC\_TIMER\_ICR   0x380 /\* Timer Initial Count Reg \*/ |
| --- |

## [◆ ](#a8c2a2d604d222ecd9d1e91ebd1793877)LOAPIC\_TMR

| #define LOAPIC\_TMR   0x180 /\* Trigger Mode Reg \*/ |
| --- |

## [◆ ](#ab821cf0c98ad7eaa74e682de764f8802)LOAPIC\_TPR

| #define LOAPIC\_TPR   0x080 /\* Task Priority Reg \*/ |
| --- |

## [◆ ](#a6865f3d12fa22ca44d37c555595f9a82)LOAPIC\_VER

| #define LOAPIC\_VER   0x030 /\* Local APIC Version Reg \*/ |
| --- |

## Function Documentation

## [◆ ](#a6fab4c5cc1444a7f69cc0ae005e6c582)DEVICE\_MMIO\_TOPLEVEL\_DECLARE()

| DEVICE\_MMIO\_TOPLEVEL\_DECLARE | ( | loapic\_regs |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a6ba00d305469ab62f89888cf0aa64033)x86\_read\_loapic()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x86\_read\_loapic | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Read value from the local APIC using the default mode.

Returns a 32-bit value read from the local APIC, using the access method determined by CONFIG\_X2APIC (either xAPIC or x2APIC). Note that 64-bit reads are only allowed in x2APIC mode and can only be done by calling [x86\_read\_x2apic()](#a797471308f74780dfcec277b18853fca) directly. (This is intentional.)

Parameters
:   | reg | the LOAPIC register number to read (LOAPIC\_\*) |
    | --- | --- |

## [◆ ](#a797471308f74780dfcec277b18853fca)x86\_read\_x2apic()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x86\_read\_x2apic | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Read 64-bit value from the local APIC in x2APIC mode.

Parameters
:   | reg | the LOAPIC register number to read (LOAPIC\_\*) |
    | --- | --- |

## [◆ ](#a4807ae47f62151774877f21939fafeab)x86\_read\_xapic()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x86\_read\_xapic | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Read 32-bit value from the local APIC in xAPIC (MMIO) mode.

Parameters
:   | reg | the LOAPIC register number to read (LOAPIC\_\*) |
    | --- | --- |

## [◆ ](#a884390389c9c7cef65801bba00395e4d)x86\_write\_loapic()

| | void x86\_write\_loapic | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Write 32-bit value to the local APIC using the default mode.

Write a 32-bit value to the local APIC, using the access method determined by CONFIG\_X2APIC (either xAPIC or x2APIC). Note that 64-bit writes are only available in x2APIC mode and can only be done by calling [x86\_write\_x2apic()](#a060a375336bf44c2dde9537d32f9416d) directly. (This is intentional.)

Parameters
:   | reg | the LOAPIC register number to write (one of LOAPIC\_\*) |
    | --- | --- |
    | val | 32-bit value to write |

## [◆ ](#a060a375336bf44c2dde9537d32f9416d)x86\_write\_x2apic()

| | void x86\_write\_x2apic | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Write 64-bit value to the local APIC in x2APIC mode.

Parameters
:   | reg | the LOAPIC register number to write (one of LOAPIC\_\*) |
    | --- | --- |
    | val | 64-bit value to write |

## [◆ ](#a9d7e889e4e4718d2205f647af172762a)x86\_write\_xapic()

| | void x86\_write\_xapic | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Write 32-bit value to the local APIC in xAPIC (MMIO) mode.

Parameters
:   | reg | the LOAPIC register number to write (one of LOAPIC\_\*) |
    | --- | --- |
    | val | 32-bit value to write |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [loapic.h](loapic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
