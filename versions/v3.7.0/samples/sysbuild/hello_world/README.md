---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sysbuild/hello_world/README.html
original_path: samples/sysbuild/hello_world/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Hello World for multiple board targets using Sysbuild

## Overview

The sample demonstrates how to build a Hello World application for two board
targets with [Sysbuild (System build)](../../../build/sysbuild/index.md#sysbuild). This sample can be useful to test, for example,
SoCs with multiple cores as each core is exposed as a board target. Other
scenarios could include boards embedding multiple SoCs. When building with
Zephyr Sysbuild, the build system adds additional images based on the options
selected in the project’s additional configuration and build files.

All images use the same `main.c` that prints the board target on which the
application is programmed.

## Building and Running

This sample needs to be built with Sysbuild by using the `--sysbuild` option.
The remote board needs to be specified using `SB_CONFIG_REMOTE_BOARD`. Some
additional settings may be required depending on the platform, for example,
to boot a remote core.

Note

It is recommended to use sample setups from
[samples/sysbuild/hello\_world/sample.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sysbuild/hello_world/sample.yaml) using the
`-T` option.

Here’s an example to build and flash the sample for the
[nRF54H20 DK](../../../boards/nordic/nrf54h20dk/doc/index.md#nrf54h20dk-nrf54h20), using application and radio cores:

```shell
west build -b nrf54h20dk/nrf54h20/cpuapp --sysbuild samples/sysbuild/hello_world -- -DSB_CONFIG_REMOTE_BOARD='"nrf54h20dk/nrf54h20/cpurad"'
west flash
```

The same can be achieved by using the
[samples/basic/multitarget\_hello\_world/sample.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/basic/multitarget_hello_world/sample.yaml) setup:

```shell
west build -b nrf54h20dk/nrf54h20/cpuapp -T sample.sysbuild.hello_world.nrf54h20dk_cpuapp_cpurad samples/sysbuild/hello_world
west flash
```

After programming the sample to your board, you should observe a hello world
message in the Zephyr console configured on each target. For example, for the
sample above:

Application core

> ```shell
> *** Booting Zephyr OS build v3.6.0-274-g466084bd8c5d ***
> Hello world from nrf54h20dk/nrf54h20/cpuapp
> ```

Radio core

> ```shell
> *** Booting Zephyr OS build v3.6.0-274-g466084bd8c5d ***
> Hello world from nrf54h20dk/nrf54h20/cpurad
> ```
