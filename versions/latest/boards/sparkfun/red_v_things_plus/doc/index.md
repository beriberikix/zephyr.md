---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/sparkfun/red_v_things_plus/doc/index.html
original_path: boards/sparkfun/red_v_things_plus/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# SparkFun RED-V Things Plus

## Overview

The SparkFun RED-V Things Plus is a development board with
a SiFive FE310-G002 RISC-V SoC.

![SparkFun RED-V Things Plus board](../../../../_images/sparkfun_red_v_things_plus.jpg)

For more information about the SparkFun RED-V Things Plus and SiFive FE310-G002:

- [SparkFun RED-V Things Plus Website](https://www.sparkfun.com/products/15799)
- [SiFive FE310-G002 Datasheet](https://sifive.cdn.prismic.io/sifive/4999db8a-432f-45e4-bab2-57007eed0a43_fe310-g002-datasheet-v1p2.pdf)
- [SiFive FE310-G002 User Manual](https://sifive.cdn.prismic.io/sifive/034760b5-ac6a-4b1c-911c-f4148bb2c4a5_fe310-g002-v1p5.pdf)

## Programming and debugging

### Building

Applications for the `sparkfun_red_v_things_plus` board configuration can be built as usual
(see [Building an Application](../../../../develop/application/index.md#build-an-application)) using the corresponding board name:

```shell
west build -b sparkfun_red_v_things_plus
```

### Flashing

The SparkFun RED-V Things Plus uses Segger J-Link OB for flashing and debugging.
To flash and debug the board, you’ll need to install the
[Segger J-Link Software and Documentation Pack](https://www.segger.com/downloads/jlink#J-LinkSoftwareAndDocumentationPack)
and choose version V6.46a or later (Downloads for Windows, Linux, and macOS are
available).

With the Segger J-Link Software installed, you can flash the application as usual
(see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details):

```shell
west build -b sparkfun_red_v_things_plus
west flash
```

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).
