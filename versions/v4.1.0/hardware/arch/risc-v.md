---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/arch/risc-v.html
original_path: hardware/arch/risc-v.html
---

# Zephyr support status on RISC-V processors

## Overview

This page describes current state of Zephyr for RISC-V processors.
Currently, there’s support for some boards, as well as Qemu support
and support for some FPGA implementations such as neorv32 and
litex\_vexriscv.

Zephyr support includes PMP, [user mode](../../kernel/usermode/index.md#usermode-api), several
ISA extensions as well as [semihosting](semihost.md#semihost-guide).

## User mode and PMP support

When the platform has Physical Memory Protection (PMP) support, enabling
it on Zephyr allows user space support and stack protection to be
selected.

## ISA extensions

It’s possible to set in Zephyr which ISA extensions (RV32/64I(E)MAFD(G)QC)
are available on a given platform, by setting the appropriate `CONFIG_RISCV_ISA_*`
kconfig. Look at `arch/riscv/Kconfig.isa` for more information.

Note that Zephyr SDK toolchain support may not be defined for all
combinations.

## SMP support

SMP is supported on RISC-V for both QEMU-virtualized and hardware-based
platforms. In order to test the SMP support, one can use
[QEMU Emulation for RISCV32](../../boards/qemu/riscv32/doc/index.md#qemu_riscv32) or [QEMU Emulation for RISCV64](../../boards/qemu/riscv64/doc/index.md#qemu_riscv64) for QEMU-based
platforms, or [BeagleV®-Fire](../../boards/beagle/beaglev_fire/doc/index.md#beaglev_fire) or [mpfs\_icicle](../../boards/microchip/mpfs_icicle/doc/index.md#mpfs_icicle) for
hardware-based platforms.
