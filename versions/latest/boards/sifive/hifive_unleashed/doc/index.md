---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/sifive/hifive_unleashed/doc/index.html
original_path: boards/sifive/hifive_unleashed/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# SiFive HiFive Unleashed

## Overview

The HiFive Unleashed is a development board with a SiFive FU540-C000
multi-core 64bit RISC-V SoC.

![SiFive HiFive Unleashed board](../../../../_images/hifive_unleashed.jpg)

## Programming and debugging

### Building

Applications for the `hifive_unleashed` board configuration can be built as
usual (see [Building an Application](../../../../develop/application/index.md#build-an-application)) using the corresponding board name:

```shell
west build -b hifive_unleashed
```

### Flashing

Current version has not yet supported flashing binary to onboard Flash ROM.

This board has USB-JTAG interface and this can be used with OpenOCD.
Load applications on DDR and run as follows:

```shell
openocd -c 'bindto 0.0.0.0' \
        -f boards/riscv/hifive_unleashed/support/openocd_hifive_unleashed.cfg
riscv64-zephyr-elf-gdb build/zephyr/zephyr.elf
(gdb) target remote :3333
(gdb) c
```

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).
