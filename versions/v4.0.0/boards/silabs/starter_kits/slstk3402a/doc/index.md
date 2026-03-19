---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/silabs/starter_kits/slstk3402a/doc/index.html
original_path: boards/silabs/starter_kits/slstk3402a/doc/index.html
---

# EFM32 Pearl Gecko 12 (SLSTK3402A)

Board Overview

[![../../../../../_images/slstk3402a.jpg](../../../../../_images/slstk3402a.jpg)
](../../../../../_images/slstk3402a.jpg)

EFM32 Pearl Gecko 12 (SLSTK3402A)

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efm32jg12b500f1024gl125, efm32pg12b500f1024gl125

## Overview

The EFM32 Pearl Gecko 12 Starter Kit SLSTK3402A contains an MCU from the
EFM32PG family built on an ARM® Cortex®-M4F processor with excellent low
power capabilities.

## Hardware

- Advanced Energy Monitoring provides real-time information about the energy
  consumption of an application or prototype design.
- Ultra low power 128x128 pixel Memory-LCD
- 2 user buttons, 2 LEDs and a touch slider
- Humidity, temperature, and inductive-capacitive metal sensor
- On-board Segger J-Link USB debugger

For more information about the EFM32PG SoC and SLSTK3402A board:

- [EFM32PG Website](https://www.silabs.com/products/mcu/32-bit/efm32-pearl-gecko)
- [EFM32PG12 Datasheet](https://www.silabs.com/documents/public/data-sheets/efm32pg12-datasheet.pdf)
- [EFM32PG12 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efm32pg12-rm.pdf)
- [SLSTK3402A Website](https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-pearl-gecko-pg12-starter-kit)
- [SLSTK3402A User Guide](https://www.silabs.com/documents/public/user-guides/ug257-stk3402-usersguide.pdf)
- [SLSTK3402A Schematics](https://www.silabs.com/documents/public/schematic-files/BRD2501A-A01-schematic.pdf)

### Supported Features

The slstk3402a board configuration supports the following hardware features:

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
| TRNG | on-chip | true random number generator |

The default configuration can be found in
[boards/silabs/starter\_kits/slstk3402a/slstk3402a\_efm32pg12b500f1024gl125\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3402a/slstk3402a_efm32pg12b500f1024gl125_defconfig)

The default configuration when building using this board to develop for the
EFM32JG12 SoC can be found in
[boards/silabs/starter\_kits/slstk3402a/slstk3402a\_efm32jg12b500f1024gl125\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3402a/slstk3402a_efm32jg12b500f1024gl125_defconfig)

Other hardware features are currently not supported by the port.

#### EFM32 Jade Gecko SoC

The EFM32 Pearl Gecko Starter Kit SLSTK3402A can also be used to evaluate
the EFM32 Jade Gecko SoC (EFM32JG12). The only difference between the Pearl
Gecko and the Jade Gecko is their core. The Pearl Gecko contains an ARM®
Cortex®-M4F core, and the Jade Gecko an ARM® Cortex®-M3 core. Other features
such as memory and peripherals are the same.

Code that is built for the Jade Gecko also runs on an equivalent Pearl Gecko.

To build firmware for the Jade Gecko and run it on the EFM32 Pearl Gecko Starter
Kit, use the board `slstk3402a/efm32jg12b500f1024gl125` instead of
`slstk3402a/efm32pg12b500f1024gl125`.

### Connections and IOs

The EFM32PG12 SoC has twelve GPIO controllers (PORTA to PORTL), but only four
are currently enabled (PORTA, PORTB, PORTD and PORTF) for the SLSTK3402A
board.

In the following table, the column **Name** contains pin names. For example, PE2
means pin number 2 on PORTE, as used in the board’s datasheets and manuals.

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

The EFM32PG12 SoC is configured to use the 40 MHz external oscillator on the
board.

### Serial Port

The EFM32PG12 SoC has four USARTs and one Low Energy UART (LEUART).

## Programming and Debugging

Note

Before using the kit the first time, you should update the J-Link firmware
from [J-Link-Downloads](https://www.segger.com/downloads/jlink)

### Flashing

The SLSTK3402A includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer, which exposes a mass storage device and a
  USB serial port.
- A serial flash device, which implements the USB flash disk file storage.
- A physical UART connection which is relayed over interface USB serial port.

#### Flashing an application to SLSTK3402A

The sample application [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b slstk3402a/efm32pg12b500f1024gl125 samples/hello_world
```

Connect the SLSTK3402A to your host computer using the USB port and you
should see a USB connection which exposes a mass storage device(STK3402A).
Copy the generated zephyr.bin to the STK3402A drive.

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
Hello World! slstk3402a
```
