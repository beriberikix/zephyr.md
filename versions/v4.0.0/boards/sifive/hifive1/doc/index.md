---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/sifive/hifive1/doc/index.html
original_path: boards/sifive/hifive1/doc/index.html
---

# HiFive1

Board Overview

[![../../../../_images/hifive1.jpg](../../../../_images/hifive1.jpg)
](../../../../_images/hifive1.jpg)

HiFive1

Vendor:
:   SiFive, Inc.

Architecture:
:   riscv

SoC:
:   fe310

## Overview

The HiFive1 is an Arduino-compatible development board with
an FE310 RISC-V SoC. Two revisions of this board are supported in Zephyr:
[HiFive1](https://www.sifive.com/boards/hifive1) (also known as HiFive1 Rev A)
and [HiFive1 Rev B](https://www.sifive.com/boards/hifive1-rev-b).

![SiFive HiFive1 board](../../../../_images/hifive11.jpg)

SiFive HiFive1 board (image courtesy of SiFive)

![SiFive HiFive1 Rev B board](../../../../_images/hifive1_revb.jpg)

SiFive HiFive1 Rev B board (image courtesy of SiFive)

## Programming and debugging

### Building

Applications for the HiFive1 board configuration can be built as usual (see
[Building an Application](../../../../develop/application/index.md#build-an-application)) using the corresponding board name:

HiFive1HiFive1 Rev B

```shell
west build -b hifive1
```

```shell
west build -b hifive1@B
```

### Flashing

#### HiFive1

HiFive1HiFive1 Rev B

In order to upload the application to the device, you’ll need OpenOCD with
RISC-V support. Download the tarball for your OS from the [SiFive website](https://www.sifive.com/boards) and extract it.

The Zephyr SDK uses a bundled version of OpenOCD by default. You can
overwrite that behavior by adding the
`-DOPENOCD=<path/to/riscv-openocd/bin/openocd>` parameter when building:

```shell
west build -b hifive1 -- -DOPENOCD=<path/to/riscv-openocd/bin/openocd>
```

When using a custom toolchain it should be enough to have the downloaded
version of the binary in your `PATH`.

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
