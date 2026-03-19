---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/microchip/mec15xxevb_assy6853/doc/index.html
original_path: boards/microchip/mec15xxevb_assy6853/doc/index.html
---

# MEC15xxEVB ASSY6853

Board Overview

[![../../../../_images/mec15xxevb_assy6853.jpg](../../../../_images/mec15xxevb_assy6853.jpg)
](../../../../_images/mec15xxevb_assy6853.jpg)

MEC15xxEVB ASSY6853

Name:
:   `mec15xxevb_assy6853`

Vendor:
:   Microchip Technology Inc.

Architecture:
:   arm

SoC:
:   mec1501\_hsz

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/mec15xxevb_assy6853/doc/index.rst/../..)

## Overview

The MEC15xxEVB\_ASSY6853 kit is a future development platform to evaluate the
Microchip MEC15XX series microcontrollers. This board needs to be mated with
part number MEC1501 144WFBA SOLDER DC ASSY 6860(cpu board) in order to operate.
The MEC152x has superseded the MEC1501 in production. MEC152x is identical to
MEC150x except for an enhanced Boot-ROM SPI loader. The SPI image format has
been updated requiring a new SPI image tool. MEC1501 and MEC152x SPI image
formats are not compatible with each other. Evaluation and cpu boards are
compatible.

## Hardware

- MEC1521HA0SZ ARM Cortex-M4 Processor
- 256 KB RAM and 64 KB boot ROM
- Keyboard interface
- ADC & GPIO headers
- UART0, UART1, and UART2
- FAN0, FAN1, FAN2 headers
- FAN PWM interface
- JTAG/SWD, ETM and MCHP Trace ports
- PECI interface 3.0
- I2C voltage translator
- 10 SMBUS headers
- 4 SGPIO headers
- VCI interface
- 5 independent Hardware Driven PS/2 Ports
- eSPI header
- 3 Breathing/Blinking LEDs
- 2 Sockets for SPI NOR chips
- One reset and VCC\_PWRDGD pushbuttons
- One external PCA9555 I/O port with jumper selectable I2C address.
- One external LTC2489 delta-sigma ADC with jumper selectable I2C address.
- Board power jumper selectable from +5V 2.1mm/5.5mm barrel connector or USB Micro A connector.

For more information about the SOC’s please see [MEC152x Reference Manual](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC152x/MEC152x_Datasheet.pdf) [[1]](#id3)

### Supported Features

The `mec15xxevb_assy6853` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

This evaluation board kit is comprised of the following HW blocks:

- MEC15xx EVB ASSY 6853 Rev A [MEC15xx EVB Schematic](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/Everglades%20EVB%20-%20Assy_6853%20Rev%20A1p1%20-%20SCH.pdf) [[2]](#id5)
- MEC1501 144WFBA SOLDER DC ASSY 6883 with MEC152x silicon [MEC1501 Daughter Card Schematic](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/MEC1501%20Socket%20DC%20for%20EVERGLADES%20EVB%20-%20Assy_6883%20Rev%20A0p1%20-%20SCH.pdf) [[3]](#id7)
- SPI DONGLE ASSY 6791 [SPI Dongle Schematic](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/SPI%20Dongles%20and%20Aardvark%20Interposer%20Assy%206791%20Rev%20A1p1%20-%20SCH.pdf) [[4]](#id9)

### System Clock

The MEC1521 MCU is configured to use the 48Mhz internal oscillator with the
on-chip PLL to generate a resulting EC clock rate of 12 MHz. See Processor clock
control register in chapter 4 “4.0 POWER, CLOCKS, and RESETS” of the data sheet in
the references at the end of this document.

### Serial Port

UART2 is configured for serial logs.

## Jumper settings

Please follow the jumper settings below to properly demo this
board. Advanced users may deviate from this recommendation.

### Jumper setting for MEC15xx EVB Assy 6853 Rev A1p0

#### Power-related jumpers

If you wish to power from +5V power brick, then connect to barrel connector `P11`
(5.5mm OD, 2.1mm ID) and move the jumper to `JP88 5-6`.

If you wish to power from micro-USB type A/B connector `P12`, move the
jumper to `JP88 7-8`.

Note

A single jumper is required in JP88.

| JP22 | JP32 | JP33 | JP37 | JP43 | JP47 | JP54 | JP56 | JP58 | JP64 | JP65 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 |

| JP72 | JP73 | JP76 | JP79 | JP80 | JP81 | JP82 | JP84 | JP87 | JP89 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 |

| JP90 | JP91 | JP100 | JP101 | JP118 |
| --- | --- | --- | --- | --- |
| 1-2 | 1-2 | 1-2 | 1-2 | 2-3 |

These jumpers configure VCC Power good, nRESETI and JTAG\_STRAP respectively.

| JP5 (VCC Power good) | JP4 (nRESETI) | JP45 (JTAG\_STRAP) |
| --- | --- | --- |
| 1-2 | 1-2 | 2-3 |

#### Boot-ROM Straps.

These jumpers configure MEC1501 Boot-ROM straps.

| JP93 (CMP\_STRAP) | JP11 (CR\_STRAP) | JP46 (VTR2\_STRAP) | JP96 (BSS\_STRAP) |
| --- | --- | --- | --- |
| 2-3 | 1-2 | 2-3 | 1-2 |

`JP96 1-2` pulls SHD SPI CS0# up to VTR2. MEC1501 Boot-ROM samples
SHD SPI CS0# and if high, it loads code from SHD SPI.

#### Peripheral Routing Jumpers

Each column of the following table illustrates how to enable UART2, SWD,
PVT SPI, SHD SPI and LED0-2 respectively.

| JP48 (UART2) | JP9 (UART2) | JP9 (SWD) | JP38 (PVT SPI) | JP98 (SHD SPI) | JP41 (LED0-2) |
| --- | --- | --- | --- | --- | --- |
| 1-2 |  | 2-3 | 2-3 | 2-3 | 1-2 |
| 4-5 | 4-5 |  | 5-6 | 5-6 | 3-4 |
| 7-8 |  | 8-9 | 8-9 | 8-9 | 5-6 |
| 10-11 | 10-11 |  | 11-12 | 11-12 |  |
|  |  |  | 14-15 | 14-15 |  |
|  |  |  | 17-18 | 20-21 |  |

Note

For UART2 make sure JP39 have jumpers connected 1-2, 3-4.

To receive UART2 serial output, please refer to the picture below
to make sure that JP9 configured for UART2 output.

![JP9 header Assy6853](../../../../_images/mec15xxevb_assy6853_jp9_1.jpg)

### Jumper settings for MEC1501 144WFBGA Socket DC Assy 6883 Rev B1p0

The jumper configuration explained above covers the base board. The ASSY
6883 MEC1501 CPU board provides capability for an optional, external 32KHz
clock source. The card includes a 32KHz crystal oscillator. The card can
also be configured to use an external 50% duty cycle 32KHz source on the
XTAL2/32KHZ\_IN pin. Note, firmware must set the MEC15xx clock enable
register to select the external source matching the jumper settings. If
using the MEC15xx internal silicon oscillator then the 32K jumper settings
are don’t cares. `JP1` is for scoping test clock outputs. Please refer to
the schematic in reference section below.

#### Parallel 32KHz crystal configuration

| JP2 | JP3 |
| --- | --- |
| 1-2 | 2-3 |

#### External 32KHz 50% duty cycle configuration

| JP2 | JP3 |
| --- | --- |
| NC | 1-2 |

### Jumper settings for MEC1503 144WFBGA Socket DC Assy 6856 Rev B1p0

The MEC1503 ASSY 6856 CPU card does not include an onboard external
32K crystal or oscillator. The one jumper block `JP1` is for scoping
test clock outputs not for configuration. Please refer to schematic
in reference section below.

## Programming and Debugging

### Setup

1. If you use Dediprog SF100 programmer, then setup it.

   Windows version can be found at the [SF100 Product page](https://www.dediprog.com/product/SF100) [[8]](#id17).

   Linux version source code can be found at [SF100 Linux GitHub](https://github.com/DediProgSW/SF100Linux) [[7]](#id15).
   Follow the [SF100 Linux manual](https://www.dediprog.com/download/save/727.pdf) [[9]](#id19) to complete setup of the SF100 programmer.
   For Linux please make sure that you copied `60-dediprog.rules`
   from the `SF100Linux` folder to the `/etc/udev/rules.s` (or rules.d)
   then restart service using:

   ```shell
   $ udevadm control --reload
   ```

   Add directory with program `dpcmd` (on Linux)
   or `dpcmd.exe` (on Windows) to your `PATH`.
2. Clone the [MEC152x SPI Image Gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI_image_gen) [[5]](#id11) repository or download the files within
   that directory. For the pre-production MEC150x use [MEC150x SPI Image Gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC1501/SPI_image_gen) [[6]](#id13)
   repository.
3. Make the image generation available for Zephyr, by making the tool
   searchable by path, or by setting an environment variable
   `EVERGLADES_SPI_GEN`, for example:

   ```shell
   export EVERGLADES_SPI_GEN=<path to tool>/everglades_spi_gen_RomE
   ```

   Note that the tools for Linux and Windows have different file names.
   For the pre-production MEC1501 SOC use everglades\_spi\_gen\_lin64.
4. If needed, a custom SPI image configuration file can be specified
   to override the default one.

   ```shell
   export EVERGLADES_SPI_CFG=custom_spi_cfg.txt
   ```

### Wiring

1. Connect the SPI Dongle ASSY 6791 to `J44` in the EVB.

   ![SPI DONGLE ASSY 6791 Connected](../../../../_images/spidongle_assy6791_view1.jpg)
2. Connect programmer to the header J6 on the Assy6791 board, it will flash the SPI NOR chip `U3`
   Make sure that your programmer’s offset is 0x0.
   For programming you can use Dediprog SF100 or a similar tool for flashing SPI chips.

   Microchip board wiring

   | SPI DONGLE ASSY 6791 | SPI DONGLE ASSY 6791 view 2  SPI DONGLE ASSY 6791 Connected |
   | --- | --- |

   Note

   Remember that SPI MISO/MOSI are swapped on Dediprog headers!
   Use separate wires to connect Dediprog pins with pins on the Assy6791 SPI board.
   Wiring connection is described in the table below.

   | Dediprog Connector | Assy6791 J6 Connector |
   | --- | --- |
   | VCC | 1 |
   | GND | 2 |
   | CS | 3 |
   | CLK | 4 |
   | MISO | 6 |
   | MOSI | 5 |
3. Connect UART2 port of the MEC15xxEVB\_ASSY\_6853 board
   to your host computer using the RS232 cable.
4. Apply power to the board via a micro-USB cable.
   Configure this option by using a jumper between `JP88 7-8`.

   ![SPI DONGLE ASSY 6791 Connected](../../../../_images/jp88_power_options.jpg)
5. Final wiring for the board should look like this:

   ![SPI DONGLE ASSY 6791 Connected](../../../../_images/mec_board_setup.jpg)

### Building

1. Build [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application as you would normally do.
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

   When west process started press Reset button and do not release it
   till the whole west process will not be finished successfully.

   ![SPI DONGLE ASSY 6791 Connected](../../../../_images/reset_button_1.jpg)

   Note

   If you don’t want to press Reset button every time, you can disconnect
   SPI Dongle ASSY 6791 from the EVB during the west flash programming.
   Then connect it back to the `J44` header and apply power to the EVB.
   Result will be the same.
3. You should see `"Hello World! mec15xxevb_assy6853"` in the first terminal window.
   If you don’t see this message, press the Reset button and the message should appear.

### Debugging

This board comes with a Cortex ETM port which facilitates tracing and debugging
using a single physical connection. In addition, it comes with sockets for
JTAG only sessions.

### Troubleshooting

1. In case you don’t see your application running, please make sure `LED7`, `LED8`, and `LED1`
   are lit. If one of these is off, then check the power-related jumpers again.
2. If you can’t program the board using Dediprog, disconnect the Assy6791
   from the main board Assy6853 and try again.
3. If Dediprog can’t detect the onboard flash, press the board’s Reset button and try again.

### Notes

1. To enable PCA9555PW and test the I2C on mec15xxevb\_assy6853, additional works are needed:

   As the I2C slave device NXP pca95xx on mec15xxevb\_assy6853 is connected to I2C00 port,
   however, I2C00 port is shared with UART2 RS232 to TTL converter used to catch serial log,
   so it’s not possible to use UART2 and I2C00 port simultaneously. We need to change to use
   I2C01 port by making some jumpers setting as below:

> - JP99 1-2 Connected Connect I2C01\_SDA from CPU to header J5
> - JP99 13-14 Connected Connect I2C01\_SCL from CPU to header J5
> - JP25 21-22 Connected External pull-up for I2C01\_SDA
> - JP25 23-24 Connected External pull-up for I2C01\_SCL
> - JP44.1 J5.1 Connected Connect NXP PCA95xx to I2C01
> - JP44.3 J5.3 Connected Connect NXP PCA95xx to I2C01

## References

[[1](#id4)]

[https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC152x/MEC152x\_Datasheet.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC152x/MEC152x_Datasheet.pdf)

[[2](#id6)]

[https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/Everglades%20EVB%20-%20Assy\_6853%20Rev%20A1p1%20-%20SCH.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/Everglades%20EVB%20-%20Assy_6853%20Rev%20A1p1%20-%20SCH.pdf)

[[3](#id8)]

[https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/MEC1501%20Socket%20DC%20for%20EVERGLADES%20EVB%20-%20Assy\_6883%20Rev%20A0p1%20-%20SCH.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/MEC1501%20Socket%20DC%20for%20EVERGLADES%20EVB%20-%20Assy_6883%20Rev%20A0p1%20-%20SCH.pdf)

[[4](#id10)]

[https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/SPI%20Dongles%20and%20Aardvark%20Interposer%20Assy%206791%20Rev%20A1p1%20-%20SCH.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/SPI%20Dongles%20and%20Aardvark%20Interposer%20Assy%206791%20Rev%20A1p1%20-%20SCH.pdf)

[[5](#id12)]

[https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI\_image\_gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI_image_gen)

[[6](#id14)]

[https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC1501/SPI\_image\_gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC1501/SPI_image_gen)

[[7](#id16)]

[https://github.com/DediProgSW/SF100Linux](https://github.com/DediProgSW/SF100Linux)

[[8](#id18)]

[https://www.dediprog.com/product/SF100](https://www.dediprog.com/product/SF100)

[[9](#id20)]

[https://www.dediprog.com/download/save/727.pdf](https://www.dediprog.com/download/save/727.pdf)
