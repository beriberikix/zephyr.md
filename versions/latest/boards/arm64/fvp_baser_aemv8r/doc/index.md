---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm64/fvp_baser_aemv8r/doc/index.html
original_path: boards/arm64/fvp_baser_aemv8r/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Arm FVP BaseR AEMv8-R

## Overview

This board configuration uses Armv8-R AEM FVP [[1]](#id7) to emulate a generic
Armv8-R [[2]](#id8) 64-bit hardware platform.

Fixed Virtual Platforms (FVP) are complete simulations of an Arm system,
including processor, memory and peripherals. These are set out in a
“programmer’s view”, which gives you a comprehensive model on which to build
and test your software.

The Armv8-R AEM FVP is a free of charge Armv8-R Fixed Virtual Platform. It
supports the latest Armv8-R feature set. Please refer to FVP documentation
page [[3]](#id9) for more details about FVP.

To Run the Fixed Virtual Platform simulation tool you must download “Armv8-R AEM
FVP” from Arm developer [[1]](#id7) (This might require the user to register) and
install it on your host PC.

The current minimum required version of “Armv8-R AEM FVP” is 11.16.16.

## Hardware

### Supported Features

The following hardware features are supported:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| GICv3 | on-chip | interrupt controller |
| PL011 UART | on-chip | serial port |
| Arm GENERIC TIMER | on-chip | system clock |
| SMSC\_91C111 | on-chip | ethernet device |

The kernel currently does not support other hardware features on this platform.

When FVP is launched with `-a, --application FILE` option, the kernel will be
loaded into DRAM region `[0x0-0x7FFFFFFF]`. For more information, please refer
to the official Armv8-R AEM FVP memory map document [[4]](#id10).

### Devices

#### System Clock

This board configuration uses a system clock frequency of 100 MHz.

#### Serial Port

This board configuration uses a single serial communication channel with the
UART0.

## Programming and Debugging

### Environment

First, set the `ARMFVP_BIN_PATH` environment variable before building.
Optionally, set `ARMFVP_EXTRA_FLAGS` to pass additional arguments to the FVP.

```shell
export ARMFVP_BIN_PATH=/path/to/fvp/directory
```

### Programming

Use this configuration to build basic Zephyr applications and kernel tests in the
Arm FVP emulated environment, for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b fvp_baser_aemv8r samples/synchronization
```

This will build an image with the synchronization sample app.
Then you can run it with `west build -t run`.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).
See [Debug with Arm DS](debug-with-arm-ds.md#debug-with-arm-ds) for how to debug with Arm Development Studio [[5]](#id11).

## References

[1]
([1](#id1),[2](#id4))

[https://developer.arm.com/tools-and-software/simulation-models/fixed-virtual-platforms/arm-ecosystem-models](https://developer.arm.com/tools-and-software/simulation-models/fixed-virtual-platforms/arm-ecosystem-models)

[[2](#id2)]

Arm Architecture Reference Manual Supplement - Armv8, for Armv8-R AArch64 architecture profile
[https://developer.arm.com/documentation/ddi0600/latest/](https://developer.arm.com/documentation/ddi0600/latest/)

[[3](#id3)]

[https://developer.arm.com/tools-and-software/simulation-models/fixed-virtual-platforms/docs](https://developer.arm.com/tools-and-software/simulation-models/fixed-virtual-platforms/docs)

[[4](#id5)]

[https://developer.arm.com/documentation/100964/1114/Base-Platform/Base—memory/BaseR-Platform-memory-map](https://developer.arm.com/documentation/100964/1114/Base-Platform/Base---memory/BaseR-Platform-memory-map)

[[5](#id6)]

[https://developer.arm.com/tools-and-software/embedded/arm-development-studio](https://developer.arm.com/tools-and-software/embedded/arm-development-studio)
