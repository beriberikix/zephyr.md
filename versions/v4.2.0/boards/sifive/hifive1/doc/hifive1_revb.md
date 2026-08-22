---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/sifive/hifive1/doc/hifive1_revb.html
original_path: boards/sifive/hifive1/doc/hifive1_revb.html
---

# HiFive1 Rev B

Board Overview

[![../../../../_images/hifive1_revb.jpg](../../../../_images/hifive1_revb.jpg)
](../../../../_images/hifive1_revb.jpg)

HiFive1 Rev B

Name:
:   `hifive1_revb`

Vendor:
:   SiFive, Inc.

Architecture:
:   riscv

SoC:
:   fe310\_g002

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sifive/hifive1/doc/hifive1_revb.rst/../..)

## Overview

The HiFive1 Rev B is an Arduino-compatible development board with an FE310-G002 RISC-V SoC.

![SiFive HiFive1 Rev B board](../../../../_images/hifive1_revb1.jpg)

SiFive HiFive1 Rev B board (image courtesy of SiFive)

## Programming and debugging

The `hifive1_revb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

### Building

Applications for the HiFive1 Rev B board configuration can be built as usual (see
[Building an Application](../../../../develop/application/index.md#build-an-application)) using the corresponding board name:

```shell
west build -b hifive1_revb
```

### Flashing

The HiFive 1 Rev B uses Segger J-Link OB for flashing and debugging. To flash and
debug the board, you’ll need to install the
[Segger J-Link Software and Documentation Pack](https://www.segger.com/downloads/jlink#J-LinkSoftwareAndDocumentationPack)
and choose version V6.46a or later (Downloads for Windows, Linux, and macOS are
available).

Now you can flash the application as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details):

```shell
west flash
```

Depending on your OS you might have to run the flash command as superuser.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).
