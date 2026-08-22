---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/README.html
original_path: samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/README.html
---

# Audio output AMP sample.

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/README.rst/..)

## Overview

This sample demonstrates the use of the DSP domains on supported NXP i.MX RTxxx
platforms in an asymmetric multiprocessing (AMP) scenario. It’s a sample with
separate projects for Cortex-M and DSP domains, that are built together into a
single resulting image using Sysbuild. The Cortex-M domain is responsible for
setting up the DSP domain (clock and power setup, code load and start), the DSP
domain is programmed to write a “hello world” message to the board’s chosen
console UART, initialise hardware responsible for audio playback and capture
and, subsequently, perform simultaneous audio capture and playback
(echo / loopback).

## Building and Running

This sample can be built and started on supported boards as follows:

```shell
west build -b <board> -o --sysbuild samples/boards/nxp/adsp/rtxxx/amp_audio_loopback
west flash -r jlink
```

Currently, these boards are supported:
- `mimxrt685_evk/mimxrt685s/cm33`

The use of J-Link firmware on integrated debug probes of those boards or a
standalone J-Link probe is desired as the J-Link probes have the ability
to directly debug the Xtensa-based DSP cores.

### Sample output

```shell
*** Booting Zephyr OS build v4.1.0-1857-g5a39ed584d81 ***
Hello World! mimxrt685_evk/mimxrt685s/cm33
[ARM] Starting DSP...
*** Booting Zephyr OS build v4.1.0-1857-g5a39ed584d81 ***
Hello World! mimxrt685_evk/mimxrt685s/hifi4
[DSP] Streams started.
```
