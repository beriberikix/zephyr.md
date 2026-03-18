---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arc/hsdk4xd/doc/index.html
original_path: boards/arc/hsdk4xd/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# DesignWare(R) ARC(R) HS4x/HS4xD Development Kit

## Overview

The ARC HS4x/HS4xD Development Kit is the next revision of [Synopsys HSDK board](../../hsdk/doc/index.md#hsdk).
It includes a multicore ARC HS4xD-based chip that integrates a wide range of interfaces
including Ethernet, HDMI, WiFi, Bluetooth, USB, SDIO, I2C, SPI, UART, I2S, ADC, PWM and GPIO,
as well as a Think Silicon GPU.

![DesignWare(R) ARC(R) HS4x/HS4xD Development Kit (synopsys.com)](../../../../_images/hsdk4xd.jpg)

For details about the board, see: [ARC HS4x/HS4xD Development Kit
(HSDK4xD)](https://www.synopsys.com/dw/ipdir.php?ds=arc-hs-development-kit)

## Hardware

The ARC HSDK4xD has 24 general GPIOs, which divided into 8 groups named from `GPIO_SEL_0` to `GPIO_SEL_7`.
Each sel can configured for different functions, such as: GPIO, UART, SPI, I2C and PWM. We can program
`CREG_GPIO_MUX` register to do configuration for each sel. Tables below show the bit definition for
`CREG_GPIO_MUX` register and the details configuration for each pin.

| Bit | Name | Access | Reset value | Description |
| --- | --- | --- | --- | --- |
| 2:0 | GPIO\_SEL\_0 | RW | 0x0 | GPIO mux select for gpio[3:0] |
| 5:3 | GPIO\_SEL\_1 | RW | 0x0 | GPIO mux select for gpio[7:4] |
| 8:6 | GPIO\_SEL\_2 | RW | 0x0 | GPIO mux select for gpio[11:8] |
| 11:9 | GPIO\_SEL\_3 | RW | 0x0 | GPIO mux select for gpio[15:12] |
| 14:12 | GPIO\_SEL\_4 | RW | 0x0 | GPIO mux select for gpio[17:16] |
| 17:15 | GPIO\_SEL\_5 | RW | 0x0 | GPIO mux select for gpio[19:18] |
| 20:18 | GPIO\_SEL\_6 | RW | 0x0 | GPIO mux select for gpio[21:20] |
| 23:21 | GPIO\_SEL\_7 | RW | 0x0 | GPIO mux select for gpio[23:22] |

| SELS | GPIO PINS | FUN0 | FUN1 | FUN2 | FUN3 | FUN4 | FUN5 | FUN6 | FUN7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SEL0 | 0 | gpio[0] | uart0\_cts | spi1\_cs[0] | gpio[0] | gpio[0] | pwm\_ch[6] | pwm\_ch[6] | pwm\_ch[1] |
| 1 | gpio[1] | uart0\_txd | spi1\_mosi | gpio[1] | pwm\_ch[0] | gpio[1] | pwm\_ch[0] | pwm\_ch[0] |
| 2 | gpio[2] | uart0\_rxd | spi1 \_miso | i2c1\_scl | gpio[2] | gpio[2] | gpio[2] | gpio[2] |
| 3 | gpio[3] | uart0\_rts | spi1\_clk | i2c1\_sda | gpio[3] | gpio[3] | gpio[3] | gpio[3] |
| SEL1 | 4 | gpio[4] | uart1\_cts | spi2\_cs[0] | gpio[4] | gpio[4] | pwm\_ch[4] | pwm\_ch[4] | pwm\_ch[3] |
| 5 | gpio[5] | uart1\_txd | spi2\_mosi | gpio[5] | pwm\_ch[2] | gpio[5] | pwm\_ch[2] | pwm\_ch[2] |
| 6 | gpio[6] | uart1\_rxd | spi2\_miso | i2c2\_scl | gpio[6] | gpio[6] | gpio[6] | gpio[6] |
| 7 | gpio[7] | uart1\_rts | spi2\_clk | i2c2\_sda | gpio[7] | gpio[7] | gpio[7] | gpio[7] |
| SEL2 | 8 | gpio[8] | uart2\_cts | spi1\_cs[1] | gpio[8] | gpio[8] | pwm\_ch[2] | pwm\_ch[2] | pwm\_ch[5] |
| 9 | gpio[9] | uart2\_txd | spi1\_mosi | gpio[9] | pwm\_ch[4] | gpio[9] | pwm\_ch[4] | pwm\_ch[4] |
| 10 | gpio[10] | uart2\_rxd | spi1\_miso | i2c1\_scl | gpio[10] | gpio[10] | gpio[10] | gpio[10] |
| 11 | gpio[11] | uart2\_rts | spi1\_clk | i2c1\_sda | gpio[11] | gpio[11] | gpio[11] | gpio[11] |
| SEL3 | 12 | gpio[12] | uart0\_cts | spi2\_cs[1] | gpio[12] | gpio[12] | pwm\_ch[0] | pwm\_ch[0] | pwm\_ch[7] |
| 13 | gpio[13] | uart0\_txd | spi2\_mosi | gpio[13] | pwm\_ch[6] | gpio[13] | pwm\_ch[6] | pwm\_ch[6] |
| 14 | gpio[14] | uart0\_rxd | spi2\_miso | i2c2\_scl | gpio[14] | gpio[14] | gpio[14] | gpio[14] |
| 15 | gpio[15] | uart0\_rts | spi2\_clk | i2c2\_sda | gpio[15] | gpio[15] | gpio[15] | gpio[15] |
| SEL4 | 16 | gpio[16] | uart1\_txd | spi1\_cs[2] | i2c1\_scl | gpio[16] | pwm\_fault\_0 | gpio[16] | pwm\_fault\_0 |
| 17 | gpio[17] | uart1\_rxd | spi1\_mosi | i2c1\_sda | pwm\_ch[0] | pwm\_ch[0] | pwm\_ch[5] | pwm\_ch[5] |
| SEL5 | 18 | gpio[18] | uart2\_txd | spi1\_miso | i2c2\_scl | gpio[18] | gpio[18] | gpio[18] | gpio[18] |
| 19 | gpio[19] | uart2\_rxd | spi1\_clk | i2c2\_sda | gpio[19] | gpio[19] | gpio[19] | gpio[19] |
| SEL6 | 20 | gpio[20] | uart0\_txd | spi2\_cs[2] | i2c1\_scl | gpio[20] | pwm\_fault\_1 | gpio[20] | pwm\_fault\_1 |
| 21 | gpio[21] | uart0\_rxd | spi2\_mosi | i2c1\_sda | pwm\_ch[6] | pwm\_ch[6] | pwm\_ch[3] | pwm\_ch[3] |
| SEL7 | 22 | gpio[22] | uart2\_txd | spi2\_miso | i2c2\_scl | gpio[22] | gpio[22] | gpio[22] | gpio[22] |
| 23 | gpio[23] | uart2\_rxd | spi2\_clk | i2c2\_sda | gpio[23] | gpio[23] | gpio[23] | gpio[23] |

### Digilent Pmod

The ARC HSDK4xD features two 12-pin Pmod connectors `Pmod_A` and `Pmod_B` and one 6-pin Pmod connector `Pmod_C`.
The functionality of the Pmod connectors is programmable and includes GPIO, UART, SPI, I2C and PWM.
The location of the pins on the Pmod connectors is shown in Figure below. Detailed pin descriptions
depending on the pin multiplexer settings are provided in the subsequent sections.

![Pinout Diagram of the Pmod](../../../../_images/pinout_diagram_of_the_pmod1.jpg)

#### Pmod\_A Connector

Table below lists the pin assignment of valid protocols that can be multiplexed on the `Pmod_A`
connector. The GPIO column is the default assignment after Reset.

| Pin | GPIO | UART | SPI | I2C | PWM\_1 | PWM\_2 |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | gpio[8] | uart2\_cts | spi1\_cs[1] | gpio[8] | gpio[8] | pwm\_ch[2] |
| A2 | gpio[9] | uart2\_txd | spi1\_mosi | gpio[9] | pwm\_ch[4] | gpio[9] |
| A3 | gpio[10] | uart2\_rxd | spi1\_miso | i2c1\_scl | gpio[10] | gpio[10] |
| A4 | gpio[11] | uart2\_rts | spi1\_clk | i2c1\_sda | gpio[11] | gpio[11] |
| A5 | GND | GND | GND | GND | GND | GND |
| A6 | 3V3 | 3V3 | 3V3 | 3V3 | 3V3 | 3V3 |
| A7 | gpio[20] | gpio[20] | gpio[20] | gpio[20] | gpio[20] | gpio[20] |
| A8 | gpio[21] | gpio[21] | gpio[21] | gpio[21] | gpio[21] | gpio[21] |
| A9 | n.c. | n.c. | n.c. | n.c. | n.c. | n.c. |
| A10 | n.c. | n.c. | n.c. | n.c. | n.c. | n.c. |
| A11 | GND | GND | GND | GND | GND | GND |
| A12 | 3V3 | 3V3 | 3V3 | 3V3 | 3V3 | 3V3 |

#### Pmod\_B Connector

Table below lists the pin assignment of valid protocols that can be multiplexed on the `Pmod_B`
connector. The GPIO column is the default assignment after Reset.

| Pin | GPIO | UART | SPI | I2C | PWM\_1 | PWM\_2 |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | gpio[12] | uart0\_cts | spi2\_cs[1] | gpio[12] | gpio[12] | pwm\_ch[0] |
| B2 | gpio[13] | uart0\_txd | spi2\_mosi | gpio[13] | pwm\_ch[6] | gpio[13] |
| B3 | gpio[14] | uart0\_rxd | spi2\_miso | i2c2\_scl | gpio[14] | gpio[14] |
| B4 | gpio[15] | uart0\_rts | spi2\_clk | i2c2\_sda | gpio[15] | gpio[15] |
| B5 | GND | GND | GND | GND | GND | GND |
| B6 | 3V3 | 3V3 | 3V3 | 3V3 | 3V3 | 3V3 |
| B7 | gpio[22] | gpio[22] | gpio[22] | gpio[22] | gpio[22] | gpio[22] |
| B8 | gpio[23] | gpio[23] | gpio[23] | gpio[23] | gpio[23] | gpio[23] |
| B9 | n.c. | n.c. | n.c. | n.c. | n.c. | n.c. |
| B10 | n.c. | n.c. | n.c. | n.c. | n.c. | n.c. |
| B11 | GND | GND | GND | GND | GND | GND |
| B12 | 3V3 | 3V3 | 3V3 | 3V3 | 3V3 | 3V3 |

#### Pmod\_C Connector

Table below lists the pin assignment of valid protocols that can be multiplexed on the `Pmod_C`
connector. The GPIO column is the default assignment after Reset.

| Pin | GPIO | UART | SPI | I2C | PWM |
| --- | --- | --- | --- | --- | --- |
| C1 | gpio[16] | uart1\_txd | spi1\_cs[2] | i2c1\_scl | gpio[16] |
| C2 | gpio[17] | uart1\_rxd | spi1\_mosi | i2c1\_sda | pwm\_ch[0] |
| C3 | gpio[18] | uart2\_txd | spi1\_miso | i2c2\_scl | gpio[18] |
| C4 | gpio[19] | uart2\_rxd | spi1\_clk | i2c2\_sda | gpio[19] |
| C5 | GND | GND | GND | GND | GND |
| C6 | 3V3 | 3V3 | 3V3 | 3V3 | 3V3 |

### Mikrobus

The ARC HSDK4xD features a set of MikroBUS headers. Figure below shows the relevant function assignments,
fully compatible with the MikroBUS standard. Table below shows the pin assignment on the I/O Multiplexer.

![mikrobus header](../../../../_images/mikrobus_header1.jpg)

| Pin | I/O | Pin | I/O |
| --- | --- | --- | --- |
| AN | ADC VIN6\* | PWM | pwm\_ch[0] |
| RST | GPX\_Port0\_bit1 | INT | gpio[16] |
| CS | spi2\_cs[1] | RX | uart2\_rxd |
| SCK | spi2\_clk | TX | uart2\_txd |
| MISO | spi2\_miso | SCL | i2c2\_scl |
| MOSI | spi2\_mosi | SDA | i2c2\_sda |

Note

ADC VIN6 is available through the on-board ADC and is
read though SPI0 using SPI chip select 1.

### Arduino

The ARC HSDK4xD provides an Arduino shield interface. Figure below shows the relevant
function assignments. The Arduino shield interface is compatible with the Arduino UNO
R3 with the following exceptions: 5 Volt shields are not supported, the IOREF voltage on
the ARC HSDK4xD board is fixed to 3V3. Note that the ICSP header is also not available. Most
shields do not require this ICSP header as the SPI master interface on this ICSP header
is also available on the `IO10` to `IO13` pins.

![arduino shield interface](../../../../_images/arduino_shield_interface1.jpg)

Table below shows the pin assignment on the I/O Multiplexer. Multiplexing is controlled by software
using the `CREG_GPIO_MUX` register (see Pinmux ). After a reset, all ports are configured as GPIO inputs.

| Pin | I/O-1 | I/O-2 | I/O-3 |
| --- | --- | --- | --- |
| AD0 | ADC VIN0\* | GPX\_port0\_bit2 |  |
| AD1 | ADC VIN1\* | GPX\_port0\_bit3 |  |
| AD2 | ADC VIN2\* | GPX\_port0\_bit4 |  |
| AD3 | ADC VIN3\* | GPX\_port0\_bit5 |  |
| AD4 | ADC VIN4\* | gpio[18] | i2c2\_sda |
| AD5 | ADC VIN5\* | gpio[19] | i2c2\_scl |
| IO0 | gpio[23] | uart2\_rxd |  |
| IO1 | gpio[22] | uart2\_txd |  |
| IO2 | gpio[16] |  |  |
| IO3 | gpio[17] | pwm\_ch[5] |  |
| IO4 | gpio[11] |  |  |
| IO5 | gpio[9] | pwm\_ch[4] |  |
| IO6 | gpio[21] | pwm\_ch[3] |  |
| IO7 | gpio[20] |  |  |
| IO8 | gpio[10] |  |  |
| IO9 | gpio[8] | pwm\_ch[2] |  |
| IO10 | gpio[12] | pwm\_ch[0] | spi2\_cs[1] |
| IO11 | gpio[13] | pwm\_ch[6] | spi2\_mosi |
| IO12 | gpio[14] |  | spi2\_miso |
| IO13 | gpio[15] |  | spi2\_clk |

### I/O expander

The ARC HSDK4xD board includes a CY8C9520A I/O expander from [Cypress CY8C9520A](https://www.cypress.com/file/37971/download). The I/O
expander offers additional GPIO signals and board control signals and can be accessed
through the on-board I2C bus, we have implemented a basic driver for it.
Tables below shows an overview of relevant I/O signals.

| Pins | Usage |
| --- | --- |
| port0\_bit0 | RS9113 Bluetooth I2S RX enable (active low) |
| port0\_bit1 | mikroBUS Reset (active low) |
| port0\_bit2 | GPIO for Arduino AD0 |
| port0\_bit3 | GPIO for Arduino AD1 |
| port0\_bit4 | GPIO for Arduino AD2 |
| port0\_bit5 | GPIO for Arduino AD3 |
| port1\_bit4 | On-board user LED0 |
| port1\_bit5 | On-board user LED1 |
| port1\_bit6 | On-board user LED2 |
| port1\_bit7 | On-board user LED3 |

### On-board user LEDS

The ARC HSDK4xD includes 4 user LEDs(active high), which can be controlled through the I/O expander pins.

| LEDs | PINs |
| --- | --- |
| LED0 | GPX\_port1\_bit4 |
| LED1 | GPX\_port1\_bit5 |
| LED2 | GPX\_port1\_bit6 |
| LED3 | GPX\_port1\_bit7 |

For hardware feature details, refer to : [Designware HS4x/HS4xD Development Kit website](https://www.synopsys.com/dw/ipdir.php?ds=arc-hs-development-kit).

## Programming and Debugging

### Required Hardware and Software

To use Zephyr RTOS applications on the HS4x/HS4xD Development Kit board, a few
additional pieces of hardware are required.

- A micro USB cable provides USB-JTAG debug and USB-UART communication
  to the board
- A universal switching power adaptor (110-240V
  AC to 12V DC), provided in the package, provides power to the board.
- [The Zephyr SDK](../../../../develop/toolchains/zephyr_sdk.md#toolchain-zephyr-sdk)
- Terminal emulator software for use with the USB-UART. Suggestion:
  [Putty Website](http://www.putty.org).
- (optional) A collection of Pmods, Arduino modules, or Mikro modules.
  See [Digilent Pmod Modules](http://store.digilentinc.com/pmod-modules) or develop your custom interfaces to attach
  to the Pmod connector.

### Set up the ARC HS4x/HS4xD Development Kit

To run Zephyr application on ARC HS4x/HS4xD Development Kit, you need to
set up the board correctly.

- Connect the digilent USB cable from your host to the board.
- Connect the 12V DC power supply to your board

### Set up Zephyr Software

### Building Sample Applications

You can try many of the [sample applications and demos](../../../../samples/index.md#samples-and-demos). We’ll use [Hello World](../../../../samples/hello_world/README.md#hello-world), found in
[samples/hello\_world](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/hello_world) as an example.

#### Configuring

You may need to write a `prj_arc.conf` file if the sample doesn’t have one.
Next, you can use the menuconfig rule to configure the target. By specifying
`hsdk4xd` as the board configuration, you can select the ARC HS4x/HS4xD Development
Kit board support for Zephyr.

```shell
# From the root of the zephyr repository
west build -b hsdk4xd samples/hello_world
west build -t menuconfig
```

#### Building

You can build an application in the usual way. Refer to
[Building an Application](../../../../develop/application/index.md#build-an-application) for more details. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello-world).

```shell
# From the root of the zephyr repository
west build -b hsdk4xd samples/hello_world
```

### Connecting Serial Output

In the default configuration, Zephyr’s HS4x/HS4xD Development Kit images support
serial output via the USB-UART on the board. To enable serial output:

- Open a serial port emulator (i.e. on Linux minicom, putty, screen, etc)
- Specify the tty driver name, for example, on Linux this may be
  `/dev/ttyUSB0`
- Set the communication settings to:

| Parameter | Value |
| --- | --- |
| Baud: | 115200 |
| Data: | 8 bits |
| Parity: | None |
| Stopbits: | 1 |

### Debugging

Using the latest version of Zephyr SDK(>=0.15.2), you can debug and
flash (run) HS4x/HS4xD Development Kit directly.

One option is to build and debug the application using the usual
Zephyr build system commands.

```shell
west build -b hsdk4xd <my app>
west debug
```

At this point you can do your normal debug session. Set breakpoints and then
`c` to continue into the program.

The other option is to launch a debug server, as follows.

```shell
west build -b hsdk4xd <my app>
west debugserver
```

Then connect to the debug server at the HS4x/HS4xD Development Kit from a second
console, from the build directory containing the output `zephyr.elf`.

```shell
$ cd <my app>
$ $ZEPHYR_SDK_INSTALL_DIR/arc-zephyr-elf/arc-zephyr-elf-gdb zephyr.elf
(gdb) target remote localhost:3333
(gdb) load
(gdb) b main
(gdb) c
```

### Flashing

If you just want to download the application to the HS4x/HS4xD Development Kit’s DDR
and run, you can do so in the usual way.

```shell
west build -b hsdk4xd <my app>
west flash
```

This command still uses openocd and gdb to load the application elf file to
HS4x/HS4xD Development Kit, but it will load the application and immediately run. If
power is removed, the application will be lost since it wasn’t written to flash.

Most of the time you will not be flashing your program but will instead debug
it using openocd and gdb. The program can be download via the USB cable into
the code and data memories.

The HS4x/HS4xD Development Kit also supports flashing the Zephyr application
with the U-Boot bootloader, a powerful and flexible tool for loading
an executable from different sources and running it on the target platform.

The U-Boot implementation for the HS4x/HS4xD Development Kit was further extended with
additional functionality that allows users to better manage the broad
configurability of the HS4x/HS4xD Development Kit

When you are ready to deploy the program so that it boots up automatically on
reset or power-up, you can follow the steps to place the program on SD card.

For details, see: [Uboot-HS4x/HS4xD-Command-Reference](https://github.com/foss-for-synopsys-dwc-arc-processors/linux/wiki/Uboot-HSDK-4xD-Command-Reference#launching-baremetal-application-on-hsdk-4xd)

### Supported peripheral

The following list indicates the state of HS4x/HS4xD Development Kit peripherals’ support

| Peripheral | Support |
| --- | --- |
| ADC | No |
| Bluetooth | No |
| Ethernet | No |
| GPIO | No |
| GPU | No |
| HDMI | No |
| I2C | No |
| I2S | No |
| PWM | No |
| SDIO | No |
| SPI | No |
| UART | Yes |
| USB | No |
| WiFi | No |

## References
