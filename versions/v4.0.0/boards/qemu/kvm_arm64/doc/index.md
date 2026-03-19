---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/qemu/kvm_arm64/doc/index.html
original_path: boards/qemu/kvm_arm64/doc/index.html
---

# QEMU Emulation for ARM AArch64 Virt KVM

Board Overview

Vendor:
:   QEMU, a generic and open source machine emulator and virtualizer

Architecture:
:   arm64

SoC:
:   qemu\_virt\_arm64

## Overview

This board configuration will use QEMU to run a KVM guest on an AArch64
host.

This configuration provides support for an AArch64 Cortex-A CPU and these
devices:

- GICv3 interrupt controller
- ARM architected timer
- PL011 UART controller

## Hardware

### Supported Features

The following hardware features are supported:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| GIC | on-chip | interrupt controller |
| PL011 UART | on-chip | serial port |
| ARM TIMER | on-chip | system clock |

The kernel currently does not support other hardware features on this platform.

### Devices

#### System Clock

This board configuration uses the host system clock frequency.

#### Serial Port

This board configuration uses a single serial communication channel with the
CPU’s UART0.

## Programming and Debugging

Refer to the qemu\_cortex\_a53 board instructions for this part.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).
