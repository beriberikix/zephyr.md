---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nxp/rd_rw612_bga/doc/index.html
original_path: boards/nxp/rd_rw612_bga/doc/index.html
---

# RD-RW612-BGA

Board Overview

Name:
:   `rd_rw612_bga`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   rw612

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/rd_rw612_bga/doc/index.rst/../..)

## Overview

The RW612 is a highly integrated, low-power tri-radio wireless MCU with an
integrated 260 MHz ARM Cortex-M33 MCU and Wi-Fi 6 + Bluetooth Low Energy (LE) 5.3 / 802.15.4
radios designed for a broad array of applications, including connected smart home devices,
gaming controllers, enterprise and industrial automation, smart accessories and smart energy.

The RW612 MCU subsystem includes 1.2 MB of on-chip SRAM and a high-bandwidth Quad SPI interface
with an on-the-fly decryption engine for securely accessing off-chip XIP flash.

The advanced design of the RW612 delivers tight integration, low power and highly secure
operation in a space- and cost-efficient wireless MCU requiring only a single 3.3 V power supply.

## Hardware

- 260 MHz ARM Cortex-M33, tri-radio cores for Wifi 6 + BLE 5.3 + 802.15.4
- 1.2 MB on-chip SRAM

### Supported Features

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| MCI\_IOMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| USART | on-chip | serial |
| DMA | on-chip | dma |
| SPI | on-chip | spi |
| I2C | on-chip | i2c |
| FLEXSPI | on-chip | flash/memc |
| TRNG | on-chip | entropy |
| DMIC | on-chip | dmic |
| LCDIC | on-chip | mipi-dbi |
| WWDT | on-chip | watchdog |
| USBOTG | on-chip | usb |
| CTIMER | on-chip | counter |
| SCTIMER | on-chip | pwm |
| MRT | on-chip | counter |
| OS\_TIMER | on-chip | os timer |
| PM | on-chip | power management; uses SoC Power Modes 1 and 2 |
| BLE | on-chip | Bluetooth |
| ADC | on-chip | adc |
| DAC | on-chip | dac |
| ENET | on-chip | ethernet |
| Wi-Fi | on-chip | Wi-Fi |

The default configuration can be found in the defconfig file:

> [boards/nxp/rd\_rw612\_bga/rd\_rw612\_bga\_defconfig/](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga_defconfig/)

Other hardware features are not currently supported

## Display Support

The rd\_rw612\_bga board supports several in-tree display modules. Setup for
each module is described below:

### GoWorld 16880 LCM

This module does not connect directly to the board, and must be connected
via an adapter board and jumper wires. Connections are described in
[boards/nxp/rd\_rw612\_bga/dts/goworld\_16880\_lcm.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/dts/goworld_16880_lcm.overlay). The
display sample can be built for this board like so:

```shell
west build -b rd_rw612_bga samples/drivers/display -- -DDTC_OVERLAY_FILE=goworld_16880_lcm.overlay
```

### Adafruit 2.8 TFT

The [Adafruit 2.8” TFT Touch Shield v2](../../../shields/adafruit_2_8_tft_touch_v2/doc/index.md#adafruit-2-8-tft-touch-v2) connects to the board’s Arduino headers
directly, but some modifications are required (see
[boards/shields/adafruit\_2\_8\_tft\_touch\_v2/boards/rd\_rw612\_bga.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_2_8_tft_touch_v2/boards/rd_rw612_bga.overlay)
for a list). The display sample can be built for this module like so:

```shell
west build -b rd_rw612_bga --shield adafruit_2_8_tft_touch_v2 samples/drivers/display
```

### NXP LCD\_PAR\_S035

The [NXP LCD\_PAR\_S035 TFT LCD Module](../../../shields/lcd_par_s035/doc/index.md#lcd-par-s035) does not connect directly to the board, and must be
connected via jumper wires. Connections and required board changes are
described in
[boards/shields/lcd\_par\_s035/boards/rd\_rw612\_bga.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/lcd_par_s035/boards/rd_rw612_bga.overlay). The
display sample can be built for the module like so:

```shell
west build -b rd_rw612_bga --shield lcd_par_s035_8080 samples/drivers/display
```

## Fetch Binary Blobs

To support Bluetooth or Wi-Fi, rd\_rw612\_bga requires fetching binary blobs, which can be
achieved by running the following command:

```shell
west blobs fetch hal_nxp
```

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the JLink Firmware.

### Configuring a Console

Connect a USB cable from your PC to J7, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b rd_rw612_bga samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.4.0 *****
Hello World! rd_rw612_bga
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b rd_rw612_bga samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS zephyr-v3.6.0 *****
Hello World! rd_rw612_bga
```

## Bluetooth

BLE functionality requires to fetch binary blobs, so make sure to follow
the `Fetch Binary Blobs` section first.

rd\_rw612\_bga platform supports the monolithic feature. The required binary blob
`<zephyr workspace>/modules/hal/nxp/zephyr/blobs/rw61x_sb_ble_a2.bin` will be linked
with the application image directly, forming one single monolithic image.

## Wi-Fi

Wi-Fi functionality requires to fetch binary blobs, so make sure to follow
the `Fetch Binary Blobs` section first.

rd\_rw612\_bga platform supports the monolithic feature. The required binary blob
`<zephyr workspace>/modules/hal/nxp/zephyr/blobs/rw61x_sb_wifi_a2.bin` will be linked
with the application image directly, forming one single monolithic image.

## Board variants

### Ethernet

To use ethernet on the RD\_RW612\_BGA board, you first need to make the following
modifications to the board hardware:

Add resistors:

- R485
- R486
- R487
- R488
- R489
- R491
- R490

Remove resistors:

- R522
- R521
- R520
- R524
- R523
- R508
- R505

Then, build for the board target `rd_rw612_bga//ethernet`.

## Resources
