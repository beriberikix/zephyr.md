---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/qemu/malta/doc/index.html
original_path: boards/qemu/malta/doc/index.html
---

# QEMU Emulation for MIPS Malta

Board Overview

Vendor:
:   QEMU, a generic and open source machine emulator and virtualizer

Architecture:
:   mips

SoC:
:   qemu\_malta

## Overview

This board configuration will use QEMU to emulate the MIPS Malta platform.

This configuration provides support for an MIPS 4Kc/24Kc CPU cores and these devices:

- CP0 Interrupt Controller
- CP0 Core Timer
- NS16550 UART

Note

This board configuration makes no claims about its suitability for use
with an actual MIPS Malta hardware system, or any other hardware system.

## Hardware

### Supported Features

The following hardware features are supported:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| CP0 IntC | on-chip | interrupt controller |
| CP0 Core Timer | on-chip | system clock |
| NS16550 UART | FPGA | serial port |

The kernel currently does not support other hardware features on this platform.

### Devices

#### System Clock

Qemu CP0 timer uses a clock frequency of 200 MHz,
see target/mips/cp0\_timer.c in Qemu source tree for details.

#### Serial Port

This board configuration uses a single serial communication channel
with the FPGA UART2.

## Programming and Debugging

Use this configuration to run basic Zephyr applications and kernel tests in the QEMU
emulated environment, for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b qemu_malta samples/synchronization
west build -t run
```

This will build an image with the synchronization sample app, boot it using
QEMU, and display the following console output:

```shell
*** Booting Zephyr OS build v2.7.99-1627-g9bea7790d620  ***
thread_a: Hello World from cpu 0 on qemu_malta!
thread_b: Hello World from cpu 0 on qemu_malta!
thread_a: Hello World from cpu 0 on qemu_malta!
thread_b: Hello World from cpu 0 on qemu_malta!
thread_a: Hello World from cpu 0 on qemu_malta!
thread_b: Hello World from cpu 0 on qemu_malta!
thread_a: Hello World from cpu 0 on qemu_malta!
thread_b: Hello World from cpu 0 on qemu_malta!
thread_a: Hello World from cpu 0 on qemu_malta!
thread_b: Hello World from cpu 0 on qemu_malta!
```

Exit QEMU by pressing `CTRL`+`A` `x`.

### Big-Endian

Use this configuration to run [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample in big-endian mode:

```shell
# From the root of the zephyr repository
west build -b qemu_malta/qemu_malta/be samples/synchronization
west build -t run
```

## References

[https://www.qemu.org/](https://www.qemu.org/)
[https://www.linux-mips.org/wiki/MIPS\_Malta](https://www.linux-mips.org/wiki/MIPS_Malta)
