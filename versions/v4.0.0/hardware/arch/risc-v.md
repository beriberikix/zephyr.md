---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/arch/risc-v.html
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

SMP is supported on RISC-V, but currently only on Qemu platforms. In
order to test the SMP support, one can use `qemu_riscv32_smp` or
`qemu_riscv64_smp` boards.
