---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/sam4s_xplained/doc/index.html
original_path: boards/arm/sam4s_xplained/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SAM4S Xplained

## Overview

The SAM4S Xplained evaluation kit is a development platform to evaluate the
Atmel SAM4S series microcontrollers.

![SAM4S Xplained](../../../../_images/sam4s_xplained.jpg)

## Hardware

- ATSAM4S16C ARM Cortex-M4 Processor
- 12 MHz crystal oscillator
- internal 32.768 kHz crystal oscillator
- IS66WV51216DALL 8 Mb SRAM
- Micro-AB USB device
- Micro-AB USB debug interface supporting SEGGER OB and Virtual COM Port and
  Data
- One reset and one user pushbutton
- 2 yellow user LEDs
- IC pads for external flash chip

### Supported Features

The sam4s\_xplained board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| UART | on-chip | serial port |
| USART | on-chip | serial port |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| WATCHDOG | on-chip | watchdog |
| GPIO | on-chip | gpio |
| HWINFO | on-chip | Unique device serial number |
| SMC | on-chip | memc (PSRAM) |
| PWM | on-chip | pwm |
| ADC | on-chip | adc |

Other hardware features are not currently supported by Zephyr.

The default configuration can be found in the Kconfig
[boards/arm/sam4s\_xplained/sam4s\_xplained\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/sam4s_xplained/sam4s_xplained_defconfig).

### Connections and IOs

Download the [SAM4S Xplained Design Files](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4S-XPLD__KitsFiles.zip) [[2]](#id4) for more information. It has
full schematic and gerbers files.

### System Clock

The SAM4S MCU is configured to use the 12 MHz internal oscillator on the board
with the on-chip PLL to generate an 84 MHz system clock.

### Serial Port

The ATSAM4S16C MCU has 2 UARTs and 2 USARTs. One of the UARTs (UART0) is
connected to the Segger J-Link OB chip (the AT91SAM3U4 is programmed to be
Segger J-Link OB). Segger J-Link OB brings the UART out as a virtual COM port.
The section flashing uses the UART from the Segger USB debug connection.

## Programming and Debugging

The SAM4S Xplained board comes with Segger [J-Link OB](https://www.segger.com/jlink-ob.html). This provides a debug
interface to the SAM4S16C chip. You can use Ozone or JLink to communicate with
the SAM4S16C.

### Flashing

For flash the board Zephyr provides two paths. One uses the default JLink
tool and the second one uses [SAM Boot Assistant (SAM-BA)](../../../../develop/flash_debug/host-tools.md#atmel-sam-ba-bootloader).

#### Using JLink

1. Download JLink from the Segger [JLink Downloads Page](https://www.segger.com/downloads/jlink) [[1]](#id2). Go to the section
   “J-Link Software and Documentation Pack” and install the “J-Link Software
   and Documentation pack for Linux”. The application JLinkExe needs to be
   accessible from your path.
2. Connect the SAM4S Xplained board to your host computer using the USB debug
   port. Then build and flash the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4s_xplained samples/hello_world
   west flash
   ```

#### Using SAM-BA bootloader

1. Close the `J25` jumper on the SAM4S Xplained board. Power on the board
   for 10s.
2. Open the `J25` jumper.
3. Connect the SAM4S Xplained board to your host computer using the SoC USB
   port. Then build and flash the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4s_xplained samples/hello_world
   ```

   ```shell
   $ west flash -r bossac
   ```

#### Visualizing the message

1. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization string.
   Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
2. Press reset button

   You should see “Hello World! sam4s\_xplained” in your terminal.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b sam4s_xplained samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.segger.com/downloads/jlink](https://www.segger.com/downloads/jlink)

[[2](#id5)]

[http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4S-XPLD\_\_KitsFiles.zip](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4S-XPLD__KitsFiles.zip)
