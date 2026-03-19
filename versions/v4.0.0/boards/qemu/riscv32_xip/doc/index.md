---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/qemu/riscv32_xip/doc/index.html
original_path: boards/qemu/riscv32_xip/doc/index.html
---

# QEMU Emulation for RISCV32 XIP

Board Overview

Vendor:
:   QEMU, a generic and open source machine emulator and virtualizer

Architecture:
:   riscv

SoC:
:   fe310

## Overview

The RISCV32 XIP QEMU board configuration is used to emulate the RISCV32 architecture.

## Programming and Debugging

Applications for the `qemu_riscv32_xip` board configuration can be built and run in
the usual way for emulated boards (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

While this board is emulated and you can’t “flash” it, you can use this
configuration to run basic Zephyr applications and kernel tests in the QEMU
emulated environment. For example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b qemu_riscv32_xip samples/synchronization
west build -t run
```

This will build an image with the synchronization sample app, boot it using
QEMU, and display the following console output:

```shell
thread_a: Hello World from cpu 0 on qemu_riscv32_xip!
thread_b: Hello World from cpu 0 on qemu_riscv32_xip!
thread_a: Hello World from cpu 0 on qemu_riscv32_xip!
thread_b: Hello World from cpu 0 on qemu_riscv32_xip!
thread_a: Hello World from cpu 0 on qemu_riscv32_xip!
thread_b: Hello World from cpu 0 on qemu_riscv32_xip!
thread_a: Hello World from cpu 0 on qemu_riscv32_xip!
thread_b: Hello World from cpu 0 on qemu_riscv32_xip!
thread_a: Hello World from cpu 0 on qemu_riscv32_xip!
thread_b: Hello World from cpu 0 on qemu_riscv32_xip!
thread_a: Hello World from cpu 0 on qemu_riscv32_xip!
thread_b: Hello World from cpu 0 on qemu_riscv32_xip!
thread_a: Hello World from cpu 0 on qemu_riscv32_xip!
```

Exit QEMU by pressing `CTRL`+`A` `x`.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).
