---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/boards/nxp/adsp/rtxxx/amp_blinky/README.html
original_path: samples/boards/nxp/adsp/rtxxx/amp_blinky/README.html
---

# Blinky AMP sample

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/adsp/rtxxx/amp_blinky/README.rst/..)

## Overview

This sample demonstrates the use of the DSP domains on supported NXP i.MX RTxxx
platforms in an asymmetric multiprocessing (AMP) scenario. It’s a sample with
separate projects for Cortex-M and DSP domains, that are built together into a
single resulting image using Sysbuild. The Cortex-M domain is responsible for
setting up the DSP domain (clock and power setup, code load and start), the DSP
domain is programmed to write a “hello world” message to the board’s chosen
console UART and blink an LED. By pressing an associated button, the blinking
can be turned off, demonstrating interrupt servicing and GPIO callbacks on the
DSP domain.

## Building and Running

This sample can be built and started on supported boards as follows:

```shell
west build -b <board> -o --sysbuild samples/boards/nxp/adsp/rtxxx/amp_blinky
west flash -r jlink
```

Currently, these boards are supported:
- `mimxrt685_evk/mimxrt685s/cm33`

The use of J-Link firmware on integrated debug probes of those boards or a
standalone J-Link probe is desired as the J-Link probes have the ability
to directly debug the Xtensa-based DSP cores.

### Sample output

```shell
*** Booting Zephyr OS build v4.1.0-1858-g6bd0a62b0bde ***
Hello World! mimxrt685_evk/mimxrt685s/cm33
[CM33] Starting HiFi4 DSP...
*** Booting Zephyr OS build v4.1.0-1858-g6bd0a62b0bde ***
[DSP] Hello World! mimxrt685_evk/mimxrt685s/hifi4
[DSP] Button pressed!
```
