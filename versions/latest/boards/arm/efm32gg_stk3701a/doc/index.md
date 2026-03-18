---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/efm32gg_stk3701a/doc/index.html
original_path: boards/arm/efm32gg_stk3701a/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# EFM32 Giant Gecko GG11 Starter Kit

## Overview

The EFM32 Giant Gecko Starter Kit EFM32GG-STK3701A contains an MCU from the
EFM32GG Series 1 family built on an ARM® Cortex®-M4F processor with excellent
low power capabilities.

![EFM32GG-SLSTK3701A](../../../../_images/efm32gg_stk3701a.jpg)

EFM32GG-SLSTK3701A (image courtesy of Silicon Labs)

## Hardware

- Advanced Energy Monitoring provides real-time information about the energy
  consumption of an application or prototype design.
- Ultra low power 128x128 pixel color Memory-LCD
- 2 user buttons, 2 LEDs and a touch slider
- Relative humidity, magnetic Hall Effect and inductive-capacitive metal sensor
- USB interface for Host/Device/OTG
- 32 Mb Quad-SPI Flash memory
- SD card slot
- RJ-45 Ethernet jack
- 2 digital microphones
- On-board Segger J-Link USB debugger

For more information about the EFM32GG11 SoC and EFM32GG-STK3701A board:

- [EFM32GG Series 1 Website](https://www.silabs.com/products/mcu/32-bit/efm32-giant-gecko-s1)
- [EFM32GG11 Datasheet](https://www.silabs.com/documents/public/data-sheets/efm32gg11-datasheet.pdf)
- [EFM32GG11 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efm32gg11-rm.pdf)
- [EFM32GG-STK3701A Website](https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-giant-gecko-gg11-starter-kit)
- [EFM32GG-STK3701A User Guide](https://www.silabs.com/documents/public/user-guides/ug287-stk3701.pdf)
- [EFM32GG-STK3701A Schematics](https://www.silabs.com/documents/public/schematic-files/BRD2204A-B00-schematic.pdf)

### Supported Features

The efm32gg\_stk3701a board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| MPU | on-chip | memory protection unit |
| COUNTER | on-chip | rtcc |
| ETHERNET | on-chip | ethernet |
| FLASH | on-chip | flash memory |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c port-polling |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| UART | on-chip | serial port-polling; serial port-interrupt |

The default configuration can be found in the defconfig file:

> `boards/arm/efm32gg_stk3701a/efm32gg_stk3701a_defconfig`

Other hardware features are currently not supported by the port.

### Connections and IOs

The EFM32GG11 SoC has nine GPIO controllers (PORTA to PORTI), all of which are
currently enabled for the EFM32GG-STK3701A board.

In the following table, the column **Name** contains pin names. For example, PE1
means pin number 1 on PORTE, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PH10 | GPIO | LED0 red |
| PH11 | GPIO | LED0 green |
| PH12 | GPIO | LED0 blue |
| PH13 | GPIO | LED1 red |
| PH14 | GPIO | LED1 green |
| PH15 | GPIO | LED1 blue |
| PC8 | GPIO | Push Button PB0 |
| PC9 | GPIO | Push Button PB1 |
| PE1 | GPIO | Board Controller Enable EFM\_BC\_EN |
| PH4 | UART\_TX | UART TX Console VCOM\_TX US0\_TX #4 |
| PH5 | UART\_RX | UART RX Console VCOM\_RX US0\_RX #4 |
| PI4 | I2C\_SDA | SENSOR\_I2C\_SDA I2C2\_SDA #7 |
| PI5 | I2C\_SCL | SENSOR\_I2C\_SCL I2C2\_SCL #7 |

### System Clock

The EFM32GG11 SoC is configured to use the 50 MHz external oscillator on the
board.

### Serial Port

The EFM32GG11 SoC has six USARTs, two UARTs and two Low Energy UARTs (LEUART).
USART4 is connected to the board controller and is used for the console.

## Programming and Debugging

Note

Before using the kit the first time, you should update the J-Link firmware
from [J-Link-Downloads](https://www.segger.com/downloads/jlink)

### Flashing

The EFM32GG-STK3701A includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer, which exposes a mass storage device and a
  USB serial port.
- A serial flash device, which implements the USB flash disk file storage.
- A physical UART connection which is relayed over interface USB serial port.

#### Flashing an application to EFM32GG-STK3701A

The sample application [Hello World](../../../../samples/hello_world/README.md#hello-world) is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b efm32gg_stk3701a samples/hello_world
```

Connect the EFM32GG-STK3701A to your host computer using the USB port and you
should see a USB connection which exposes a mass storage device(STK3701A) and
a USB Serial Port. Copy the generated zephyr.bin to the STK3701A drive.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you’ll see the following message on the corresponding serial port
terminal session:

```shell
Hello World! efm32gg_stk3701a
```
