---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/silabs/radio_boards/xg29_rb4412a/doc/index.html
original_path: boards/silabs/radio_boards/xg29_rb4412a/doc/index.html
---

# EFR32xG29 2.4 GHz 8 dBm Buck (xG29-RB4412A)

Board Overview

Name:
:   `xg29_rb4412a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32mg29b140f1024im40

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/xg29_rb4412a/doc/index.rst/../..)

## Overview

The xG24-RB4412A radio board provides support for the Silicon Labs EFR32MG29 SoC.

## Hardware

- EFR32MG29B140F1024IM40 SoC
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 1024 kB
- RAM: 256 kB
- Transmit power: up to +8 dBm
- Operation frequency: 2.4 GHz
- Crystal oscillators for LFXO (32.768 kHz) and HFXO (38.4 MHz)

### Supported Features

The `xg29_rb4412a` board target supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| CMU | on-chip | clock control |
| MSC | on-chip | flash |
| GPIO | on-chip | gpio, pin control |
| RTCC | on-chip | system clock, counter |
| MPU | on-chip | memory protection unit |
| NVIC | on-chip | interrupt controller |
| USART | on-chip | serial, spi |
| EUSART | on-chip | serial, spi |
| I2C | on-chip | i2c |
| LDMA | on-chip | dma |
| WDOG | on-chip | watchdog |
| SE | on-chip | entropy |
| RADIO | on-chip | bluetooth |
| ACMP | on-chip | comparator |

## Programming and Debugging

Applications for the `xg29_rb4412a` board target can be built, flashed, and debugged in the
usual way. See [Building an Application](../../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../../develop/application/index.md#application-run) for more details on
building and running.

### Flashing

As an example, this section shows how to build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

To build and program the sample to the xG24-RB4412A, complete the following steps:

First, plug the xG24-RB4412A to a compatible mainboard and connect the mainboard to your computer
using the USB port on the left side.
Next, build and flash the sample by running the following command:

```shell
# From the root of the zephyr repository
west build -b xg29_rb4412a samples/hello_world
west flash
```

`west flash` will by default use SEGGER JLink. Make sure that the JLinkExe binary is available on
the PATH. Alternatively, use `west flash -r silabs_commander` to use Simplicity Commander to flash.
In this case, make sure that the commander binary is available on PATH.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! xg29_rb4412a
```

### Bluetooth

To use the BLE function, run the command below to retrieve necessary binary
blobs from the SiLabs HAL repository.

```shell
west blobs fetch hal_silabs
```

Then build the Zephyr kernel and a Bluetooth sample with the following
command. The [Observer](../../../../../samples/bluetooth/observer/README.md#bluetooth_observer "Scan for Bluetooth devices nearby and print their information.") sample application is used in
this example.

```shell
# From the root of the zephyr repository
west build -b xg29_rb4412a samples/bluetooth/observer
```
