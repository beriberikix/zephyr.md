---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/qemu/riscv64/doc/index.html
original_path: boards/qemu/riscv64/doc/index.html
---

# QEMU Emulation for RISCV64

Board Overview

Name:
:   `qemu_riscv64`

Vendor:
:   QEMU, a generic and open source machine emulator and virtualizer

Architecture:
:   riscv

SoC:
:   qemu\_virt\_riscv64

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/qemu/riscv64/doc/index.rst/../..)

## Overview

The RISCV64 QEMU board configuration is used to emulate the RISCV64 architecture.

## Get the Toolchain and QEMU

The minimum version of the [Zephyr SDK tools](https://github.com/zephyrproject-rtos/sdk-ng/releases)
with toolchain and QEMU support for the RISCV64 architecture is v0.10.2.
Please see the [installation instructions](../../../../develop/getting_started/index.md#install-required-tools)
for more details.

## Programming and Debugging

Applications for the `qemu_riscv64` board configuration can be built and run in
the usual way for emulated boards (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

While this board is emulated and you can’t “flash” it, you can use this
configuration to run basic Zephyr applications and kernel tests in the QEMU
emulated environment. For example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b qemu_riscv64 samples/synchronization
west build -t run
```

This will build an image with the synchronization sample app, boot it using
QEMU, and display the following console output:

```shell
***** BOOTING ZEPHYR OS v1.8.99 - BUILD: Jun 27 2017 13:09:26 *****
threadA: Hello World from riscv64!
threadB: Hello World from riscv64!
threadA: Hello World from riscv64!
threadB: Hello World from riscv64!
threadA: Hello World from riscv64!
threadB: Hello World from riscv64!
threadA: Hello World from riscv64!
threadB: Hello World from riscv64!
threadA: Hello World from riscv64!
threadB: Hello World from riscv64!
```

Exit QEMU by pressing `CTRL+A` `x`.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).
