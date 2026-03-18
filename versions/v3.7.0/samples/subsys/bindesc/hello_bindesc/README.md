---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/bindesc/hello_bindesc/README.html
original_path: samples/subsys/bindesc/hello_bindesc/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Binary descriptors “Hello World”

## Overview

A simple sample of [binary descriptor](../../../../services/binary_descriptors/index.md#binary-descriptors) definition and usage.

## Building and Running

Follow these steps to build the `hello_bindesc` sample application:

```shell
west build -b <board to use> samples/subsys/bindesc/hello_bindesc
```

To dump all binary descriptors in the image, run:

```shell
west bindesc dump build/zephyr/zephyr.bin
```

(Note: you can also dump the contents of `zephyr.elf`, if your build system
does not produce a `*.bin` file, e.g. compiling for `native_sim`.)

For more details see [Binary Descriptors](../../../../services/binary_descriptors/index.md#binary-descriptors) and [Working with binary descriptors: west bindesc](../../../../develop/west/zephyr-cmds.md#west-bindesc).
