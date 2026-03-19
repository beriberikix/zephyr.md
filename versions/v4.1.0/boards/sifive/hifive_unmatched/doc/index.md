---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/sifive/hifive_unmatched/doc/index.html
original_path: boards/sifive/hifive_unmatched/doc/index.html
---

# HiFive Unmatched

Board Overview

[![../../../../_images/hifive_unmatched.jpg](../../../../_images/hifive_unmatched.jpg)
](../../../../_images/hifive_unmatched.jpg)

HiFive Unmatched

Name:
:   `hifive_unmatched`

Vendor:
:   SiFive, Inc.

Architecture:
:   riscv

SoC:
:   fu740

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sifive/hifive_unmatched/doc/index.rst/../..)

## Overview

The HiFive Unmatched is a development board with a SiFive FU740-C000
multi-core 64bit RISC-V SoC.

## Programming and debugging

### Building

Applications for the `hifive_unmatched` board configuration can be built as
usual (see [Building an Application](../../../../develop/application/index.md#build-an-application)) using the corresponding board name:

S7U74

```shell
# From the root of the zephyr repository
west build -b hifive_unmatched/fu740/s7 samples/hello_world
```

```shell
# From the root of the zephyr repository
west build -b hifive_unmatched/fu740/u74 samples/hello_world
```

### Flashing

Current version has not yet supported flashing binary to onboard Flash ROM.

This board has USB-JTAG interface and this can be used with OpenOCD.
Load applications on DDR and run as follows:

```shell
openocd -c 'bindto 0.0.0.0' \
        -f boards/riscv/hifive_unmatched/support/openocd_hifive_unmatched.cfg
riscv64-zephyr-elf-gdb build/zephyr/zephyr.elf
(gdb) target remote :3333
(gdb) c
```

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).
