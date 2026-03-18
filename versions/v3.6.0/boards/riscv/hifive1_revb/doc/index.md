---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/riscv/hifive1_revb/doc/index.html
original_path: boards/riscv/hifive1_revb/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SiFive HiFive1 Rev B

## Overview

The HiFive1 Rev B is an Arduino-compatible development board with
a SiFive FE310-G002 RISC-V SoC.

![SiFive HiFive1 Rev B board](../../../../_images/hifive1_revb.jpg)

## Programming and debugging

### Building

Applications for the `hifive1_revb` board configuration can be built as usual
(see [Building an Application](../../../../develop/application/index.md#build-an-application)) using the corresponding board name:

```shell
west build -b hifive1_revb
```

### Flashing

The HiFive 1 Rev B uses Segger J-Link OB for flashing and debugging. To flash and
debug the board, you’ll need to install the
[Segger J-Link Software and Documentation Pack](https://www.segger.com/downloads/jlink#J-LinkSoftwareAndDocumentationPack)
and choose version V6.46a or later (Downloads for Windows, Linux, and macOS are
available).

With the Segger J-Link Software installed, you can flash the application as usual
(see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details):

```shell
west flash
```

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).
