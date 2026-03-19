---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/peregrine/sam4l_wm400_cape/doc/index.html
original_path: boards/peregrine/sam4l_wm400_cape/doc/index.html
---

# SAM4L WM-400 Cape Board

Board Overview

[![../../../../_images/wm-400-pin-out.webp](../../../../_images/wm-400-pin-out.webp)
](../../../../_images/wm-400-pin-out.webp)

SAM4L WM-400 Cape Board

Name:
:   `sam4l_wm400_cape`

Vendor:
:   Peregrine Consultoria e Servicos

Architecture:
:   arm

SoC:
:   sam4lc4b

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/peregrine/sam4l_wm400_cape/doc/index.rst/../..)

## Overview

The SAM4L WM-400 Cape is a full featured design to enable IEEE 802.15.4 low
power nodes. It is a Beaglebone Black cape concept with an Atmel AT86RF233
radio transceiver. User can develop Touch interface and have access to many
sensors and conectivity buses.

## Hardware

- ATSAM4LC4B ARM Cortex-M4 Processor
- 12 MHz crystal oscillator
- 32.768 kHz crystal oscillator
- 1 RS-232 interface
- 1 RS-485 full duplex interface
- Micro-AB USB OTG host/device
- 1 user touch button and One user pushbutton
- 4 user LEDs
- 1 AT86RF233 IEEE 802.15.4 transceiver
- 1 MPL115A2 I²C Barometric Pressure/Temperature Sensor
- 1 VCNL4010 Proximity/Light Sensor
- 1 CC2D33S Advanced Humidity Temperature Sensor
- 1 NCP18WF104J03RB NTC Temperature Sensor
- 1 TEMT6000X01 Ambient Light Sensor

### Supported Features

The `sam4l_wm400_cape` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

For detailed information see [SAM4L WM-400 Cape](https://gfbudke.wordpress.com/2014/04/30/modulo-wireless-ieee-802-15-4zigbee-wm-400-e-wm-400l-bbbs) [[1]](#id2) Information.

### System Clock

The SAM4L MCU is configured to use the 12 MHz internal oscillator on the board
with the on-chip PLL to generate an 48 MHz system clock.

### Serial Port

The ATSAM4LC4B MCU has 4 USARTs. One of the USARTs (USART3) is shared between
RS-232 and RS-485 interfaces. The default console terminal is available at
RS-232 onboard port or via USB device.

## Programming and Debugging

The SAM4L WM-400 Cape board has a 10-pin header to connect to a Segger JLink.
Using the JLink is possible to program and debug the SAM4LC4B chip. The board
came with a SAM-BA bootloader that only can be used to flash the software.

### Flashing

1. For JLink instructions, see [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools).
2. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
3. Connect the SAM4L WM-400 Cape board to your host computer using the
   USB debug port. Then build and flash the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
   application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4l_wm400_cape samples/hello_world
   west flash
   ```

   You should see `Hello World! sam4l_wm400_cape` in your terminal.
4. For SAM-BA bootloader instructions, see [SAM Boot Assistant (SAM-BA)](../../../../develop/flash_debug/host-tools.md#atmel-sam-ba-bootloader).
5. Connect the SAM4L WM-400 Cape board to your host computer using the
   USB debug port pressing the S1 button. Then build and flash the
   [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. After programming the board
   the application will start automatically.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4l_wm400_cape samples/hello_world
   west flash -r bossac
   ```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b sam4l_wm400_cape samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://gfbudke.wordpress.com/2014/04/30/modulo-wireless-ieee-802-15-4zigbee-wm-400-e-wm-400l-bbbs](https://gfbudke.wordpress.com/2014/04/30/modulo-wireless-ieee-802-15-4zigbee-wm-400-e-wm-400l-bbbs)
