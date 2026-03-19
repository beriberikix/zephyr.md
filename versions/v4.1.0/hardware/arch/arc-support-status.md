---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/arch/arc-support-status.html
original_path: hardware/arch/arc-support-status.html
---

# Zephyr support status on ARC processors

## Overview

This page describes current state of Zephyr for ARC processors and some future
plans. Please note that

> - plans are given without exact deadlines
> - software features require corresponding hardware to be present and
>   configured the proper way
> - not all the features can be enabled at the same time

## Support status

Legend:
**Y** - yes, supported; **N** - no, not supported; **WIP** - Work In Progress;
**TBD** - to be decided

|  | **Processor families** | | | | |
| --- | --- | --- | --- | --- | --- |
|  | **EM** | **HS3x/4x** | **VPX** | **HS5x** | **HS6x** |
| Port status | upstreamed | upstreamed | upstreamed [[6]](#f6) | upstreamed | upstreamed |
| **Features** | | | | | |
| Closely coupled memories (ICCM, DCCM) [[1]](#f1) | Y | Y | Y | TBD | TBD |
| Execution with caches - Instruction/Data, L1/L2 caches | Y | Y | Y | Y | Y |
| Hardware-assisted unaligned memory access | Y [[2]](#f2) | Y | Y | Y | Y |
| Regular interrupts with multiple priority levels, direct interrupts | Y | Y | Y | Y | Y |
| Fast interrupts, separate register banks for fast interrupts | Y | Y | TBD | N | N |
| Hardware floating point unit (FPU) | Y | Y | TBD [[6]](#f6) | TBD | TBD |
| Symmetric multiprocessing (SMP) support, switch-based | N/A | Y | TBD | Y | Y |
| Hardware-assisted stack checking | Y | Y | Y | N | N |
| Hardware-assisted atomic operations | N/A | Y | Y | Y | Y |
| DSP ISA | Y | N [[3]](#f3) | TBD [[6]](#f6) | TBD | TBD |
| DSP AGU/XY extensions | Y | N [[3]](#f3) | N/A | TBD | TBD |
| Userspace | Y | Y | N | TBD | TBD |
| Memory protection unit (MPU) | Y | Y | TBD | N | N |
| Memory management unit (MMU) | N/A | N | TBD | N | N |
| SecureShield | Y | N/A | N/A | N/A | N/A |
| Single-thread kernel support [[5]](#f5) | Y | Y | Y | Y | Y |
| **Toolchains** | | | | | |
| GNU (open source GCC-based) | Y | Y | N | Y | Y |
| MetaWare (proprietary Clang-based) | Y | Y | Y | Y | Y |
| **Simulators** | | | | | |
| QEMU (open source) [[4]](#f4) | Y | Y | N | Y | Y |
| nSIM (proprietary, provided by MetaWare Development Tools) | Y | Y | Y | Y | Y |

## Notes

[[1](#id2)]

usage of CCMs is limited on SMP systems

[[2](#id3)]

except the systems with secure features (SecureShield) due to HW
limitation

[3]
([1](#id5),[2](#id7))

We only support save/restore ACCL/ACCH registers in task’s context.
Rest of DSP/AGU registers save/restore isn’t implemented but kernel
itself does not use these registers. This allows single task per
core to use DSP/AGU safely.

[[4](#id9)]

QEMU doesn’t support all the ARC processor’s HW features. For the
detailed info please check the ARC QEMU documentation

[[5](#id8)]

Single-thread kernel is support only for single core targets

[6]
([1](#id1),[2](#id4),[3](#id6))

currently only ARC VPX scalar port is supported. The support of VPX vector pipeline, VCCM,
STU is not included in this port, and require additional development and / or other runtime
integration.

### VPX Vector Registers

Zephyr supports a limited form sharing of the VPX vector registers known as
cooperative sharing. Threads that use these registers must bookend the relevant
sections with calls to [`arc_vpx_lock()`](../../doxygen/html/arc__vpx_8h.md#a97f5476f56ce69acf4a0d169c6a78ba6) and [`arc_vpx_unlock()`](../../doxygen/html/arc__vpx_8h.md#a40a9dcc39bc184cb1a5aca5b8e7ad3ad) to
control access to this resource.

Note

If the system has multiple CPUs, then it is the responsibility of the
application developer to both pin the thread to a single CPU before it
attempts to get the cooperative lock, and not modify the CPU affinity
while it is waiting for or holding that cooperative lock.

#### Configuration Options

The cooperative sharing of the VPX vector registers is selected when
configuration option [`CONFIG_ARC_VPX_COOPERATIVE_SHARING`](../../kconfig.md#CONFIG_ARC_VPX_COOPERATIVE_SHARING "CONFIG_ARC_VPX_COOPERATIVE_SHARING")
is enabled.
