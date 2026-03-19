---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/amd/acp_6_0_adsp/doc/index.html
original_path: boards/amd/acp_6_0_adsp/doc/index.html
---

# ACP 6.0 Xtensa Audio DSP

Board Overview

Name:
:   `acp_6_0_adsp`

Vendor:
:   Advanced Micro Devices (AMD), Inc.

Architecture:

SoC:
:   acp\_6\_0

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/amd/acp_6_0_adsp/doc/index.rst/../..)

## Overview

ACP 6.0 is Audio co-processor in AMD SoC based on HiFi5 DSP Xtensa Architecture,
Zephyr OS is ported to run various audio and speech use cases on
the SOF based framework.

SOF can be built with either Zephyr or Cadence’s proprietary
Xtensa OS (XTOS) and run on a ACP 6.0 AMD platforms.

## Hardware

- Board features:

  - RAM: 1.75MB HP SRAM & 512KB configurable IRAM/DRAM
  - Audio Interfaces:

    > - 1 x SP (I2S, PCM),
    > - 1 x BT (I2S, PCM),
    > - 1 x HS (I2S, PCM),
    > - DMIC

### Supported Features

The `acp_6_0_adsp` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### System Clock

The ACP 6.0 SoC operates with an audio clock frequency ranging from 200 to 800 MHz.

## System requirements

### Xtensa Toolchain (optional)

The Zephyr SDK provides GCC-based toolchains necessary to build Zephyr for
the AMD ACP boards. For users looking for higher optimization levels,
building with the proprietary Xtensa toolchain from Cadence
might be preferable.

The following instructions assume you have purchased and
installed the toolchain(s) and core(s) for your board following
instructions from Xtensa documentation.

If you choose to build with the Xtensa toolchain instead of the Zephyr SDK, set
the following environment variables specific to the board in addition to the
Xtensa toolchain environment variable listed below.

First, make sure, the necessary license is available from
Cadence and set the license variables as per the instruction from Cadence.
Next, set the following environment variables:

The bottom three variables are specific to acp\_6\_0.

```shell
export XTENSA_TOOLCHAIN_PATH="tools installed path"
export XTENSA_BUILDS_DIR="user build directory path"
export ZEPHYR_TOOLCHAIN_VARIANT=xcc
export TOOLCHAIN_VER=RI-2019.1-linux
export XTENSA_CORE=LX7_HiFi5_PROD
```

## Programming and Debugging

### Building

Build as usual.

```shell
# From the root of the zephyr repository
west build -b acp_6_0_adsp/acp_6_0 samples/hello_world
```

### Flashing

AMD supports only signed images flashing on ACP 6.0 platforms
through ACP Linux Driver.

The following boot sequence messages can be observed in dmesg

> - booting DSP firmware
> - ACP\_DSP0\_RUNSTALL : 0x0
> - ipc rx: 0x70000000
> - Firmware info: version 2:11:99-03a9d
> - Firmware: ABI 3:29:1 Kernel ABI 3:23:0
> - mailbox upstream 0x0 - size 0x400
> - mailbox downstream 0x400 - size 0x400
> - stream region 0x1000 - size 0x400
> - debug region 0x800 - size 0x400
> - fw\_state change: 3 -> 6
> - ipc rx done: 0x70000000
> - firmware boot complete
