---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/raspberrypi/rpi_pico/doc/index.html
original_path: boards/raspberrypi/rpi_pico/doc/index.html
---

# Raspberry Pi Pico

Board Overview

[![../../../../_images/rpi_pico.jpg](../../../../_images/rpi_pico.jpg)
](../../../../_images/rpi_pico.jpg)

Raspberry Pi Pico

Name:
:   `rpi_pico`

Vendor:
:   Raspberry Pi Foundation

Architecture:
:   arm

SoC:
:   rp2040

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/raspberrypi/rpi_pico/doc/index.rst/../..)

## Overview

The [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) [[1]](#id3) and Pico W are small, low-cost, versatile boards from
Raspberry Pi. They are equipped with an [RP2040](RP2040_Datasheet) SoC, an on-board LED,
a USB connector, and an SWD interface.

The Pico W additionally contains an [Infineon CYW43439](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-4-802.11n/cyw43439/) [[2]](#id5) 2.4 GHz Wi-Fi/Bluetooth module.

The USB bootloader allows the ability to flash without any adapter,
in a drag-and-drop manner.
It is also possible to flash and debug the boards with their SWD interface,
using an external adapter.

## Hardware

- Dual core Arm Cortex-M0+ processor running up to 133MHz
- 264KB on-chip SRAM
- 2MB on-board QSPI flash with XIP capabilities
- 26 GPIO pins
- 3 Analog inputs
- 2 UART peripherals
- 2 SPI controllers
- 2 I2C controllers
- 16 PWM channels
- USB 1.1 controller (host/device)
- 8 Programmable I/O (PIO) for custom peripherals
- On-board LED
- 1 Watchdog timer peripheral
- Infineon CYW43439 2.4 GHz Wi-Fi chip (Pico W only)

![Raspberry Pi Pico](../../../../_images/rpi_pico1.jpg)

![Raspberry Pi Pico W](../../../../_images/rpi_pico_w.jpg)

Raspberry Pi Pico (above) and Pico W (below)
(Images courtesy of Raspberry Pi)

### Supported Features

The `rpi_pico` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

The peripherals of the RP2040 SoC can be routed to various pins on the board.
The configuration of these routes can be modified through DTS. Please refer to
the datasheet to see the possible routings for each peripheral.

External pin mapping on the Pico W is identical to the Pico, but note that internal
RP2040 GPIO lines 23, 24, 25, and 29 are routed to the Infineon module on the W.
Since GPIO 25 is routed to the on-board LED on the Pico, but to the Infineon module
on the Pico W, the “blinky” sample program does not work on the W (use hello\_world for
a simple test program instead).

#### Default Zephyr Peripheral Mapping:

- UART0\_TX : P0
- UART0\_RX : P1
- I2C0\_SDA : P4
- I2C0\_SCL : P5
- I2C1\_SDA : P6
- I2C1\_SCL : P7
- SPI0\_RX : P16
- SPI0\_CSN : P17
- SPI0\_SCK : P18
- SPI0\_TX : P19
- ADC\_CH0 : P26
- ADC\_CH1 : P27
- ADC\_CH2 : P28
- ADC\_CH3 : P29

## Programmable I/O (PIO)

The RP2040 SoC comes with two PIO peripherals. These are two simple
co-processors that are designed for I/O operations. The PIOs run
a custom instruction set, generated from a custom assembly language.
PIO programs are assembled using **pioasm**, a tool provided by Raspberry Pi.

Zephyr does not (currently) assemble PIO programs. Rather, they should be
manually assembled and embedded in source code. An example of how this is done
can be found at [drivers/serial/uart\_rpi\_pico\_pio.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/uart_rpi_pico_pio.c).

### Sample: SPI via PIO

The [samples/sensor/bme280/README.rst](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/bme280/README.rst) sample includes a
demonstration of using the PIO SPI driver to communicate with an
environmental sensor. The PIO SPI driver supports using any
combination of GPIO pins for an SPI bus, as well as allowing up to
four independent SPI buses on a single board (using the two SPI
devices as well as both PIO devices).

### PIO Based Features

Raspberry Pi Pico’s PIO is a programmable chip that can implement a variety of peripherals.

| Peripheral | Kconfig option | Devicetree compatible |
| --- | --- | --- |
| UART (PIO) | [`CONFIG_SERIAL`](../../../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL") | [`raspberrypi,pico-uart-pio`](../../../../build/dts/api/bindings/serial/raspberrypi%2Cpico-uart-pio.md#std-dtcompatible-raspberrypi-pico-uart-pio) |
| SPI (PIO) | [`CONFIG_SPI`](../../../../kconfig.md#CONFIG_SPI "CONFIG_SPI") | [`raspberrypi,pico-spi-pio`](../../../../build/dts/api/bindings/spi/raspberrypi%2Cpico-spi-pio.md#std-dtcompatible-raspberrypi-pico-spi-pio) |
| WS2812 (PIO) | [`CONFIG_LED_STRIP`](../../../../kconfig.md#CONFIG_LED_STRIP "CONFIG_LED_STRIP") | [`worldsemi,ws2812-rpi_pico-pio`](../../../../build/dts/api/bindings/led_strip/worldsemi%2Cws2812-rpi_pico-pio.md#std-dtcompatible-worldsemi-ws2812-rpi_pico-pio) |

## Programming and Debugging

Applications for the `rpi_pico` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### System requirements

#### Prerequisites for the Pico W

Building for the Raspberry Pi Pico W requires the AIROC binary blobs
provided by Infineon. Run the command below to retrieve those files:

```shell
west blobs fetch hal_infineon
```

Note

It is recommended running the command above after `west update`.

#### Debug Probe and Host Tools

Several debugging tools support the Raspberry Pi Pico.
The [Raspberry Pi Debug Probe](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) [[5]](#id12) is an easy-to-obtain CMSIS-DAP adapter
officially provided by the Raspberry Pi Foundation,
making it a convenient choice for debugging `rpi_pico`.

It can be used with

- [OpenOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#openocd-debug-host-tools)
- [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools)

OpenOCD is the default for `rpi_pico`.

- [SEGGER J-Link](https://www.segger.com/products/debug-probes/j-link/) [[6]](#id15)
- [Black Magic Debug Probe](BlackMagicDebug)

can also be used.
These are used with dedicated probes.

### Flashing

The `rpi_pico` can flash with Zephyr’s standard method.
See also [Building, Flashing and Debugging](../../../../develop/west/build-flash-debug.md#west-flashing).

Here is an example of building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b rpi_pico samples/basic/blinky
```

```shell
west flash --runner jlink
```

#### Using OpenOCD

To use a debugging adapter such as the Raspberry Pi Debug Probe,
You must configure **udev**. Refer to [Setting udev rules](../../../../develop/beyond-GSG.md#setting-udev-rules) for details.

The Raspberry Pi Pico has an SWD interface that can be used to program
and debug the onboard SoC. This interface can be used with OpenOCD.
To use it, OpenOCD version 0.12.0 or later is needed.

If you are using a Debian based system (including RaspberryPi OS, Ubuntu. and more),
using the [pico\_setup.sh](https://raw.githubusercontent.com/raspberrypi/pico-setup/master/pico_setup.sh) [[3]](#id7) script is a convenient way to set up the forked version of OpenOCD.

Here is an example of building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b rpi_pico samples/basic/blinky -- -DOPENOCD=/usr/local/bin/openocd -DRPI_PICO_DEBUG_ADAPTER=cmsis-dap
west flash
```

Set the CMake option **OPENOCD** to `/usr/local/bin/openocd`. This should work
with the OpenOCD that was installed with the default configuration.
This configuration also works with an environment that is set up by the [pico\_setup.sh](https://raw.githubusercontent.com/raspberrypi/pico-setup/master/pico_setup.sh) [[3]](#id7) script.

**RPI\_PICO\_DEBUG\_ADAPTER** specifies what debug adapter is used for debugging.

If **RPI\_PICO\_DEBUG\_ADAPTER** was not set, `cmsis-dap` is used by default.
The `raspberrypi-swd` and `jlink` are verified to work.
How to connect `cmsis-dap` and `raspberrypi-swd` is described in [Getting Started with Raspberry Pi Pico](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf) [[4]](#id10).
Any other SWD debug adapter maybe also work with this configuration.

The value of **RPI\_PICO\_DEBUG\_ADAPTER** is cached, so it can be omitted from
`west flash` and `west debug` if it was previously set while running
`west build`.

**RPI\_PICO\_DEBUG\_ADAPTER** is used in an argument to OpenOCD as `"source [find interface/${RPI_PICO_DEBUG_ADAPTER}.cfg]"`.
Thus, **RPI\_PICO\_DEBUG\_ADAPTER** needs to be assigned the file name of the debug adapter.

#### Using UF2

If you don’t have an SWD adapter, you can flash the Raspberry Pi Pico with
a UF2 file. By default, building an app for this board will generate a
`build/zephyr/zephyr.uf2` file. If the Pico is powered on with the `BOOTSEL`
button pressed, it will appear on the host as a mass storage device. The
UF2 file should be drag-and-dropped to the device, which will flash the Pico.

### Debugging

Like flashing, debugging can also be performed using Zephyr’s standard method
(see [Run an Application](../../../../develop/application/index.md#application-run)).
The following sample demonstrates how to debug using OpenOCD and
the [Raspberry Pi Debug Probe](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) [[5]](#id12).

```shell
# From the root of the zephyr repository
west build -b rpi_pico samples/basic/blinky -- -DOPENOCD=/usr/local/bin/openocd -DRPI_PICO_DEBUG_ADAPTER=cmsis-dap
west debug
```

The default debugging tool is `openocd`.
If you use a different tool, specify it with the `--runner`,
such as `jlink`.

If you use OpenOCD, see also the description about flashing [Using UF2](#rpi-pico-flashing-using-uf2)
for more information.

[[1](#id4)]

[https://www.raspberrypi.com/products/raspberry-pi-pico/](https://www.raspberrypi.com/products/raspberry-pi-pico/)

[[2](#id6)]

[https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-4-802.11n/cyw43439/](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-4-802.11n/cyw43439/)

[3]
([1](#id8),[2](#id9))

[https://raw.githubusercontent.com/raspberrypi/pico-setup/master/pico\_setup.sh](https://raw.githubusercontent.com/raspberrypi/pico-setup/master/pico_setup.sh)

[[4](#id11)]

[https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)

[5]
([1](#id13),[2](#id14))

[https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html)

[[6](#id16)]

[https://www.segger.com/products/debug-probes/j-link/](https://www.segger.com/products/debug-probes/j-link/)
