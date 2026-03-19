---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sysbuild/with_mcuboot/README.html
original_path: samples/sysbuild/with_mcuboot/README.html
---

# MCUboot with sysbuild

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sysbuild/with_mcuboot/README.rst/..)

## Overview

A simple example that demonstrates how building a sample using sysbuild can
automatically include MCUboot as the bootloader.
It showcases how the sample can adjust the configuration of extra image by
creating a image specific Kconfig fragment.

## Sysbuild specific settings

This sample automatically includes MCUboot as bootloader when built using
sysbuild.

This is achieved with a sysbuild specific Kconfig configuration,
`sysbuild.conf`.

The `SB_CONFIG_BOOTLOADER_MCUBOOT=y` setting in the sysbuild Kconfig file
enables the bootloader when building with sysbuild.

The `sysbuild/mcuboot.conf` file will be used as an extra fragment that
is merged together with the default configuration files used by MCUboot.

`sysbuild/mcuboot.conf` adjusts the log level in MCUboot, as well as
configures MCUboot to prevent downgrades and operate in upgrade-only mode.

To build both the sample and MCUboot with `west` for the `reel_board`, run:

```shell
west build -b reel_board --sysbuild samples/sysbuild/with_mcuboot
```

Execution output:

```shell
*** Booting Zephyr OS build v3.2.0-rc3-209-gdcf4201d3573  ***
*** Booting Zephyr OS build v3.2.0-rc3-209-gdcf4201d3573  ***
Address of sample 0xc000
Hello sysbuild with mcuboot! nrf52840dk
```

The first `Booting Zephyr OS build` is printed by MCUboot itself and the
following lines are printed by the `with_mcuboot` sample.
This sample also prints its flash location.
