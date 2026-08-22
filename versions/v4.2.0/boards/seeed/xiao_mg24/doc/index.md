---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/seeed/xiao_mg24/doc/index.html
original_path: boards/seeed/xiao_mg24/doc/index.html
---

# XIAO MG24

Board Overview

[![../../../../_images/xiao_mg24.webp](../../../../_images/xiao_mg24.webp)
](../../../../_images/xiao_mg24.webp)

XIAO MG24

Name:
:   `xiao_mg24`

Vendor:
:   Seeed Technology Co., Ltd

Architecture:
:   arm

SoC:
:   efr32mg24b220f1536im48

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/seeed/xiao_mg24/doc/index.rst/../..)

## Overview

Seeed Studio XIAO MG24 is a mini development board based on Silicon Labs’ MG24. XIAO MG24 is based
on ARM Cortex-M33 core, 32-bit RISC architecture with a maximum clock speed of 78MHz, supporting DSP
instructions and FPU floating-point operations, possessing powerful computing power, and built-in
AL/ML hardware accelerator MVP, which can efficiently process AI/machine learning algorithms.
Secondly, it has excellent RF performance, with a transmission power of up to+19.5 dBm and a
reception sensitivity as low as -105.4 dBm. It supports multiple IoT and wireless transmission
protocols such as Matter, Thread, Zigbee, Bluetooth LE 5.3,Bluetooth mesh etc.

## Hardware

- EFR32MG24B220F1536IM48 Mighty Gecko SoC
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 1536 kB
- RAM: 256 kB
- Transmit power: up to +20 dBm
- Operation frequency: 2.4 GHz
- Crystals for LFXO (32.768 kHz) and HFXO (39 MHz).
- 3.7v LiPo power and charge support
- User and battery charge LEDs

For more information about the EFR32MG24 SoC and XIAO MG24 board, refer to these
documents:

- [EFR32MG24 Website](https://www.silabs.com/wireless/zigbee/efr32mg24-series-2-socs)
- [EFR32MG24 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg24-datasheet.pdf)
- [EFR32xG24 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/brd4187c-rm.pdf)
- [XIAO MG24 Wiki](https://wiki.seeedstudio.com/xiao_mg24_getting_started/)

### Supported Features

The `xiao_mg24` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

In the following table, the column **Name** contains Pin names. For example, PA2
means Pin number 2 on PORTA, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PA7 | GPIO | LED0 |
| PA8 | USART0\_TX | UART Console TX |
| PA9 | USART0\_RX | UART Console RX |

The default configuration can be found in
[boards/seeed/xiao\_mg24/xiao\_mg24\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/xiao_mg24/xiao_mg24_defconfig)

### System Clock

The EFR32MG24 SoC is configured to use the 39 MHz external oscillator on the
board.

### Serial Port

The EFR32MG24 SoC has one USART and two EUSARTs.
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

The XIAO MG24 contains an SAMD11 with CMSIS-DAP, allowing flashing, debugging, logging, etc. over
the USB port. Doing so requires a version of OpenOCD that includes support for the flash on the MG24
MCU. Until those changes are included in stock OpenOCD, the version bundled with Arduino can be
used, or can be installed from the [OpenOCD Arduino Fork](https://github.com/facchinm/OpenOCD/tree/arduino-0.12.0-rtx5). When flashing, debugging, etc. you may
need to include `--openocd=/usr/local/bin/openocd
--openocd-search=/usr/local/share/openocd/scripts/` options to the command.

### Flashing

Connect the XIAO MG24 board to your host computer using the USB port. A USB CDC ACM serial port
should appear on the host, that can be used to view logs from the flashed application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b xiao_mg24 samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) connecting to the UCB CDC ACM serial port.

Reset the board and you should see the following message in the terminal:

```shell
Hello World! xiao_mg24
```
