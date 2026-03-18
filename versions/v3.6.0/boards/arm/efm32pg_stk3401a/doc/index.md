---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/efm32pg_stk3401a/doc/index.html
original_path: boards/arm/efm32pg_stk3401a/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# EFM32 Pearl Gecko Starter Kit

## Overview

The EFM32 Pearl Gecko Starter Kit EFM32PG-STK3401A contains an MCU from the
EFM32PG family built on an ARM® Cortex®-M4F processor with excellent low
power capabilities.

![EFM32PG-SLSTK3401A](../../../../_images/efm32pg_stk3401a.jpg)

EFM32PG-SLSTK3401A (image courtesy of Silicon Labs)

## Hardware

- Advanced Energy Monitoring provides real-time information about the energy
  consumption of an application or prototype design.
- Ultra low power 128x128 pixel Memory-LCD
- 2 user buttons, 2 LEDs and 2 capacitive buttons
- Humidity and temperature sensor
- On-board Segger J-Link USB debugger

For more information about the EFM32PG SoC and EFM32PG-STK3401A board:

- [EFM32PG Website](https://www.silabs.com/products/mcu/32-bit/efm32-pearl-gecko)
- [EFM32PG1 Datasheet](https://www.silabs.com/documents/public/data-sheets/efm32pg1-datasheet.pdf)
- [EFM32PG1 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efm32pg1-rm.pdf)
- [EFM32PG-STK3401A Website](https://www.silabs.com/development-tools/mcu/32-bit/efm32pg1-starter-kit)
- [EFM32PG-STK3401A User Guide](https://www.silabs.com/documents/public/user-guides/ug154-stk3401-user-guide.pdf)

### Supported Features

The efm32pg\_stk3401a board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| MPU | on-chip | memory protection unit |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| COUNTER | on-chip | rtcc |
| FLASH | on-chip | flash memory |
| GPIO | on-chip | gpio |
| UART | on-chip | serial port-polling; serial port-interrupt |
| I2C | on-chip | i2c port-polling |
| WATCHDOG | on-chip | watchdog |

The default configuration can be found in the defconfig file:

> `boards/arm/efm32pg_stk3401a/efm32pg_stk3401a_defconfig`

Other hardware features are currently not supported by the port.

### Connections and IOs

The EFM32PG1 SoC has five GPIO controllers (PORTA to PORTD and PORTF) and
all are enabled for the EFM32PG-STK3401A board.

In the following table, the column **Name** contains pin names. For example, PF4
means pin number 4 on PORTF, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PF4 | GPIO | LED0 |
| PF5 | GPIO | LED1 |
| PF6 | GPIO | Push Button PB0 |
| PF7 | GPIO | Push Button PB1 |
| PA5 | GPIO | Board Controller Enable EFM\_BC\_EN |
| PA0 | UART\_TX | UART TX Console VCOM\_TX US0\_TX #0 |
| PA1 | UART\_RX | UART RX Console VCOM\_RX US0\_RX #0 |
| PD10 | UART\_TX | EXP12\_UART\_TX LEU0\_TX #18 |
| PD11 | UART\_RX | EXP14\_UART\_RX LEU0\_RX #18 |
| PC10 | I2C\_SDA | ENV\_I2C\_SDA I2C0\_SDA #15 |
| PC11 | I2C\_SCL | ENV\_I2C\_SCL I2C0\_SCL #15 |

### System Clock

The EFM32PG SoC is configured to use the 40 MHz external oscillator on the
board.

### Serial Port

The EFM32PG SoC has two USARTs and one Low Energy UART (LEUART).

## Programming and Debugging

Note

Before using the kit the first time, you should update the J-Link firmware
from [J-Link-Downloads](https://www.segger.com/downloads/jlink)

### Flashing

The EFM32PG-STK3401A includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer, which exposes a mass storage device and a
  USB serial port.
- A serial flash device, which implements the USB flash disk file storage.
- A physical UART connection which is relayed over interface USB serial port.

#### Flashing an application to EFM32PG-STK3401A

The sample application [Hello World](../../../../samples/hello_world/README.md#hello-world) is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b efm32pg_stk3401a samples/hello_world
```

Connect the EFM32PG-STK3401A to your host computer using the USB port and you
should see a USB connection which exposes a mass storage device(STK3401A).
Copy the generated zephyr.bin to the STK3401A drive.

Use a USB-to-UART converter such as an FT232/CP2102 to connect to the UART on the
expansion header.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you’ll see the following message on the corresponding serial port
terminal session:

```shell
Hello World! arm
```
