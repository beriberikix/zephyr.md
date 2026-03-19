---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/qemu/cortex_r5/doc/index.html
original_path: boards/qemu/cortex_r5/doc/index.html
---

# QEMU Emulation for ARM Cortex-R5

Board Overview

Vendor:
:   QEMU, a generic and open source machine emulator and virtualizer

Architecture:
:   arm

SoC:
:   zynqmp\_rpu

## Overview

This board configuration will use QEMU to emulate the Xilinx Zynq UltraScale+
(ZynqMP) platform.

This configuration provides support for an ARM Cortex-R5 CPU and these devices:

- ARM PL-390 Generic Interrupt Controller
- Xilinx Zynq TTC (Cadence TTC)
- Xilinx Zynq UART

Note

This board configuration makes no claims about its suitability for use
with an actual ZCU102 hardware system, or any other hardware system.

## Hardware

### Supported Features

The following hardware features are supported:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| GIC | on-chip | generic interrupt controller |
| TTC | on-chip | system timer |
| UART | on-chip | serial port |

The kernel currently does not support other hardware features on this platform.

### Devices

#### System Timer

This board configuration uses a system timer tick frequency of 1000 Hz.

#### Serial Port

This board configuration uses a single serial communication channel with the
on-chip UART0.

### Known Problems or Limitations

The following platform features are unsupported:

- Dual-redundant Core Lock-step (DCLS) execution is not emulated.
- Xilinx Zynq TTC driver does not support tickless mode operation.

## Programming and Debugging

Use this configuration to run basic Zephyr applications and kernel tests in the
QEMU emulated environment, for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b qemu_cortex_r5 samples/synchronization
west build -t run
```

This will build an image with the synchronization sample app, boot it using
QEMU, and display the following console output:

```shell
*** Booting Zephyr OS build v2.2.0  ***
threadA: Hello World from qemu_cortex_r5!
threadB: Hello World from qemu_cortex_r5!
threadA: Hello World from qemu_cortex_r5!
threadB: Hello World from qemu_cortex_r5!
threadA: Hello World from qemu_cortex_r5!
threadB: Hello World from qemu_cortex_r5!
threadA: Hello World from qemu_cortex_r5!
threadB: Hello World from qemu_cortex_r5!
threadA: Hello World from qemu_cortex_r5!
threadB: Hello World from qemu_cortex_r5!
```

Exit QEMU by pressing `CTRL`+`A` `x`.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).

## References

1. ARMv7-A and ARMv7-R Architecture Reference Manual (ARM DDI 0406C ID051414)
2. Cortex-R5 and Cortex-R5F Technical Reference Manual (ARM DDI 0460C ID021511)
3. Zynq UltraScale+ Device Technical Reference Manual (UG1085)
