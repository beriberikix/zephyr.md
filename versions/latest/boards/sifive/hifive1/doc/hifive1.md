---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/sifive/hifive1/doc/hifive1.html
original_path: boards/sifive/hifive1/doc/hifive1.html
---

# HiFive1

Board Overview

[![../../../../_images/hifive1.jpg](../../../../_images/hifive1.jpg)
](../../../../_images/hifive1.jpg)

HiFive1

Name:
:   `hifive1`

Vendor:
:   SiFive, Inc.

Architecture:
:   riscv

SoC:
:   fe310\_g000

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sifive/hifive1/doc/hifive1.rst/../..)

## Overview

The HiFive1 is an Arduino-compatible development board with an FE310-G000 RISC-V SoC.

![SiFive HiFive1 board](../../../../_images/hifive11.jpg)

SiFive HiFive1 board (image courtesy of SiFive)

## Programming and debugging

The `hifive1` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** | **simulate** | **robot** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **hifive1** | ✅ (default) |  |  |  |  |  |  |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |  |  |
| **renode** |  |  |  |  |  | ✅ |  |
| **renode-robot** |  |  |  |  |  |  | ✅ |

### Building

Applications for the HiFive1 board configuration can be built as usual (see
[Building an Application](../../../../develop/application/index.md#build-an-application)) using the corresponding board name:

```shell
west build -b hifive1
```

### Flashing

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

Now you can flash the application as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details):

```shell
west flash
```

Depending on your OS you might have to run the flash command as superuser.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).
