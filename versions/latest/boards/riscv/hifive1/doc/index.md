---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/riscv/hifive1/doc/index.html
original_path: boards/riscv/hifive1/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SiFive HiFive1

## Overview

The HiFive1 is an Arduino-compatible development board with
an FE310 RISC-V SoC.
More information can be found on
[SiFive’s website](https://www.sifive.com/boards/hifive1).

![SiFive HiFive1 board](../../../../_images/hifive1.jpg)

## Programming and debugging

### Building

Applications for the `hifive1` board configuration can be built as usual
(see [Building an Application](../../../../develop/application/index.md#build-an-application)) using the corresponding board name:

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
ninja flash
```

Depending on your OS you might have to run the flash command as superuser.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).
