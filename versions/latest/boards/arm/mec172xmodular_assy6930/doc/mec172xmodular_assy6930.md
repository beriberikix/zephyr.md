---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/mec172xmodular_assy6930/doc/mec172xmodular_assy6930.html
original_path: boards/arm/mec172xmodular_assy6930/doc/mec172xmodular_assy6930.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Microchip MEC172x Modular Card ASSY6930 (Rev. B)

## Overview

The MEC172x Modular Card ASSY6930 (Rev. B) is a development board to evaluate the
Microchip MEC172X series microcontrollers. This board can work standalone
or be mated with any platform that complies with MECC specification.

[![MEC172x Modular ASSY 6930](../../../../_images/mec172xmodular_assy6930.jpg)](../../../../_images/mec172xmodular_assy6930.jpg)

## Hardware

- MEC172x (MEC1723, MEC1727 and MEC1728) ARM Cortex-M4 Processor
- 416 KB RAM and 128 KB boot ROM
- UART1 using microUSB
- PECI interface 3.0
- FAN, PWM and TACHO pins
- 5 SMBus instances
- eSPI header
- VCI interface
- 1 hardware driven PS/2 ports
- Keyboard interface headers

For more information about the SOC please see [MEC172x Reference Manual](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC172x/MEC172x-Data-Sheet.pdf) [[1]](#id1)

At difference from MEC172x evaluation board, modular MEC172x exposes the pins in 2 different ways:

1. Standalone mode via headers

   - GPIOs
   - JTAG port
   - eSPI bus
   - I2C0, I2C1 and I2C6
   - PWM1, PWM2, PWM3
   - Shared SPI
   - Keyboard Interface
2. Mated mode with another platform that has a high density MECC connector

   - FAN, PWM8
   - I2C3 and I2C7
   - eSPI bus

The board is powered through the +5V USB micro-A connector or from the MECC connector.

### Supported Features

The mec172xmodular\_assy6930 (Rev. B) board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| PINMUX | on-chip | pinmux |
| PS/2 | on-chip | ps2 |
| KSCAN | on-chip | kscan |
| TACH | on-chip | tachometer |
| RPMFAN | on-chip | Fan speed controller |

Other hardware features are not currently supported by Zephyr (at the moment)

The default configuration can be found in the
[boards/arm/mec172xmodular\_assy6930/mec172xmodular\_assy6930\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mec172xmodular_assy6930/mec172xmodular_assy6930_defconfig) Kconfig file.

### Connections and IOs

This evaluation board kit is comprised of the following HW blocks:

- MEC172x Modular ASSY 6930 Rev B1 [MEC172x Modular EC Card - Assy\_6930 Rev B1p1](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC172x/MEC172X-MECC_Assy_6930_B1p1-SCH.pdf) [[2]](#id3)

### System Clock

The MEC172x MCU is configured to use the 96Mhz internal oscillator with the
on-chip PLL to generate a resulting EC clock rate of 12 MHz. See Processor clock
control register in chapter 4 “4.0 POWER, CLOCKS, and RESETS” of the data sheet in
the references at the end of this document.

### Serial Port

UART1 is configured for serial logs.

## Jumper settings

Please follow the jumper settings below to properly demo this
board. Advanced users may deviate from this recommendation.

### Jumper setting for MEC172x Modular Assy 6930 Rev B1p1

#### Power-Related Jumpers

If you wish to power from type A/B connector `P1` set the jumper `JP22 1-2`.
This is required for standalone mode.
If you wish to power through MECC connector `P2` and mate to external platform,
set the jumper to `JP22 2-3`.

NOTE: A single jumper is required in JP22.

If you wish to set VTR2 to 3.3V, set the jumper `JP26 2-3`.
This is required for Windows application.
If you wish to set VTR2 to 1.8V, set the jumper `JP26 1-2`.
This is required for Chrome application.

#### Boot-ROM Straps

This jumper configures MEC172x Boot-ROM strap.

| JP23 (UART\_BSTRAP) |
| --- |
| 1-2 |

`JP23 1-2` pulls UART\_BSTRAP to GND. MEC172x Boot-ROM samples UART\_BSTRAP and if low,
UART interface is used for Crisis Recovery.

#### Boot Source Select

The jumpers below configure MEC172x to boot from Shared SPI, Slave Attached Flash (SAF)
or Master Attached Flash (MAF).

| Boot Source | JP25 |
| --- | --- |
| Shared SPI or SAF | 5-6 |
| MAF | 1-2, 4-6 |

## Programming and Debugging

### Setup

1. If you use Dediprog SF100 programmer, then setup it.

   Windows version can be found at the [SF100 Product page](https://www.dediprog.com/product/SF100) [[5]](#id9).

   Linux version source code can be found at [SF100 Linux GitHub](https://github.com/DediProgSW/SF100Linux) [[4]](#id7).
   Follow the [SF100 Linux manual](https://www.dediprog.com/download/save/727.pdf) [[6]](#id11) to complete setup of the SF100 programmer.
   For Linux please make sure that you copied `60-dediprog.rules`
   from the `SF100Linux` folder to the `/etc/udev/rules.s` (or rules.d)
   then restart service using:

   ```shell
   $ udevadm control --reload
   ```

   Add directory with program `dpcmd` (on Linux)
   or `dpcmd.exe` (on Windows) to your `PATH`.
2. Clone the [MEC172x SPI Image Gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC172x/SPI_image_gen) [[3]](#id5) repository or download the files within
   that directory.
3. Make the image generation available for Zephyr, by making the tool
   searchable by path, for example:

   ```shell
   -DMEC172X_SPI_GEN=<path to spi_gen tool>/mec172x_spi_gen_lin_x86_64
   ```

   Note that the tools for Linux and Windows have different file names.
4. The default MEC172X\_SPI\_CFG file is spi\_cfg.txt located in ${BOARD\_DIR}/support.
   Example of SPI\_CFG for 4MBit (spi\_cfg\_4MBit.txt) and 128MBit (spi\_cfg\_128MBit.txt)
   SPI flash can be found in the same folder. If needed, a custom SPI image
   configuration file can be specified to override the default one.

   ```shell
   -DMEC172X_SPI_CFG=<path to spi_cfg file>/spi_cfg.txt
   ```
5. Example command to generate 128MBit spi image for hello\_world:

   ```shell
   west build -p auto -b mec172xmodular_assy6930 samples/hello_world -- -DMEC172X_SPI_GEN=$HOME/CPGZephyrDocs/MEC172x/SPI_image_gen/mec172x_spi_gen_lin_x86_64 -DMEC172X_SPI_CFG=$HOME/zephyrproject/zephyr/boards/arm/mec172xmodular_assy6930/support/spi_cfg_128MBit.txt
   ```

### Wiring

1. Connect programmer to the header J2 on the ASSY6930 board, it will flash the SPI NOR chip
   `U2`. Make sure that your programmer’s offset is 0x0.
   For programming you can use Dediprog SF100 or a similar tool for flashing SPI chips.

   | Dediprog Connector | J2 |
   | --- | --- |
   | VCC | 1 |
   | GND | 2 |
   | CS | 3 |
   | CLK | 4 |
   | MISO | 6 |
   | MOSI | 5 |
2. Connect UART1 port of the mec172xmodular\_assy6930 (Rev. B) board
   to your host computer using the RS232 cable.
3. Apply power to the board via a micro-USB cable.
   Configure this option by using a jumper between `JP22 1-2`.

### Building

1. Build [Hello World](../../../../samples/hello_world/README.md#hello-world) application as you would normally do.
2. The file `spi_image.bin` will be created if the build system
   can find the image generation tool. This binary image can be used
   to flash the SPI chip.

### Flashing

1. Run your favorite terminal program to listen for output.
   Under Linux the terminal should be `/dev/ttyUSB0`. Do not close it.

   For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
2. Flash your board using `west` from the second terminal window.
   Split first and second terminal windows to view both of them.

   ```shell
   $ west flash
   ```

   Note

   When west process started press Reset button `S1` and do not release it
   till the whole west process will not be finished successfully.
3. You should see `"Hello World! mec172xmodular_assy6930"` in the first terminal window.
   If you don’t see this message, press the Reset button and the message should appear.

### Debugging

`J1` header on the board allows for JTAG connections for debug.

### Troubleshooting

1. In case you don’t see your application running, please make sure `LED1` is lit.
   If `LED1` is off, check the power-related jumpers again.
2. If you can’t program the board using Dediprog, disconnect and reconnect cable connected to
   `P1` and try again.
3. If Dediprog can’t detect the onboard flash, press the board’s `S1` Reset button and try again.

## References

[[1](#id2)]

[https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC172x/MEC172x-Data-Sheet.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC172x/MEC172x-Data-Sheet.pdf)

[[2](#id4)]

[https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC172x/MEC172X-MECC\_Assy\_6930\_B1p1-SCH.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC172x/MEC172X-MECC_Assy_6930_B1p1-SCH.pdf)

[[3](#id6)]

[https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC172x/SPI\_image\_gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC172x/SPI_image_gen)

[[4](#id8)]

[https://github.com/DediProgSW/SF100Linux](https://github.com/DediProgSW/SF100Linux)

[[5](#id10)]

[https://www.dediprog.com/product/SF100](https://www.dediprog.com/product/SF100)

[[6](#id12)]

[https://www.dediprog.com/download/save/727.pdf](https://www.dediprog.com/download/save/727.pdf)
