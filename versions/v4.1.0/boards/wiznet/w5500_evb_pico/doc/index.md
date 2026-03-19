---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/wiznet/w5500_evb_pico/doc/index.html
original_path: boards/wiznet/w5500_evb_pico/doc/index.html
---

# W5500 Evaluation Pico

Board Overview

[![../../../../_images/w5500_evb_pico_side.png](../../../../_images/w5500_evb_pico_side.png)
](../../../../_images/w5500_evb_pico_side.png)

W5500 Evaluation Pico

Name:
:   `w5500_evb_pico`

Vendor:
:   WIZnet Co., Ltd.

Architecture:
:   arm

SoC:
:   rp2040

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/wiznet/w5500_evb_pico/doc/index.rst/../..)

## Overview

W5500-EVB-Pico is a microcontroller evaluation board based on the Raspberry
Pi RP2040 and fully hardwired TCP/IP controller W5500 - and basically works
the same as Raspberry Pi Pico board but with additional Ethernet via W5500.
The USB bootloader allows the ability to flash without any adapter, in a
drag-and-drop manner. It is also possible to flash and debug the boards with
their SWD interface, using an external adapter.

## Hardware

- Dual core Arm Cortex-M0+ processor running up to 133MHz
- 264KB on-chip SRAM
- 16MB on-board QSPI flash with XIP capabilities
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
- Wiznet W5500 Ethernet MAC/PHY

### Supported Features

The `w5500_evb_pico` board supports the hardware features listed below.

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

External pin mapping on the W5500\_EVB\_PICO is identical to the Raspberry Pi
Pico. Since GPIO 25 is routed to the on-board LED on, similar to the Raspberry
Pi Pico, the blinky example works as intended. The W5500 is routed to the SPI0
(P16-P19), with the reset and interrupt signal for the W5500 routed to P20 and
P21, respectively. All of these are shared with the edge connector on the
board.

Refer to [W55500 Evaluation Board Documentation](https://docs.wiznet.io/Product/iEthernet/W5500/w5500-evb-pico) [[3]](#id9) for a board schematic and
other certifications.

#### Default Zephyr Peripheral Mapping:

- UART0\_TX : P0
- UART0\_RX : P1
- I2C0\_SDA : P4
- I2C0\_SCL : P5
- I2C1\_SDA : P14
- I2C1\_SCL : P15
- SPI0\_RX : P16
- SPI0\_CSN : P17
- SPI0\_SCK : P18
- SPI0\_TX : P19
- W5500 Reset : P20
- W5500 Interrupt : P21
- ADC\_CH0 : P26
- ADC\_CH1 : P27
- ADC\_CH2 : P28
- ADC\_CH3 : P29

## Programming and Debugging

### Flashing

#### Using SEGGER JLink

You can Flash the w5500\_evb\_pico with a SEGGER JLink debug probe as described in
[Building, Flashing and Debugging](../../../../develop/west/build-flash-debug.md#west-flashing).

Here is an example of building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b w5500_evb_pico samples/basic/blinky
```

```shell
west flash --runner jlink
```

#### Using OpenOCD

To use PicoProbe, You must configure **udev**.

Create a file in /etc/udev.rules.d with any name, and write the line below.

```shell
ATTRS{idVendor}=="2e8a", ATTRS{idProduct}=="000c", MODE="660", GROUP="plugdev", TAG+="uaccess"
```

This example is valid for the case that the user joins to `plugdev` groups.

The Raspberry Pi Pico, and thus the W55500 Evaluation Board, has an SWD
interface that can be used to program and debug the on board RP2040. This
interface can be utilized by OpenOCD. To use it with the RP2040, OpenOCD
version 0.12.0 or later is needed.

If you are using a Debian based system (including RaspberryPi OS, Ubuntu. and
more), using the [pico\_setup.sh](https://raw.githubusercontent.com/raspberrypi/pico-setup/master/pico_setup.sh) [[1]](#id4) script is a convenient way to set up the
forked version of OpenOCD.

Depending on the interface used (such as JLink), you might need to
checkout to a branch that supports this interface, before proceeding.
Build and install OpenOCD as described in the README.

Here is an example of building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
application.

```shell
# From the root of the zephyr repository
west build -b w5500_evb_pico samples/basic/blinky -- -DOPENOCD=/usr/local/bin/openocd -DOPENOCD_DEFAULT_PATH=/usr/local/share/openocd/scripts -DRPI_PICO_DEBUG_ADAPTER=picoprobe
west flash
```

Set the environment variables **OPENOCD** to `/usr/local/bin/openocd` and
**OPENOCD\_DEFAULT\_PATH** to `/usr/local/share/openocd/scripts`. This should
work with the OpenOCD that was installed with the default configuration. This
configuration also works with an environment that is set up by the
[pico\_setup.sh](https://raw.githubusercontent.com/raspberrypi/pico-setup/master/pico_setup.sh) [[1]](#id4) script.

**RPI\_PICO\_DEBUG\_ADAPTER** specifies what debug adapter is used for debugging.

If **RPI\_PICO\_DEBUG\_ADAPTER** was not assigned, `picoprobe` is used by default.
The other supported adapters are `raspberrypi-swd`, `jlink` and
`blackmagicprobe`. How to connect `picoprobe` and `raspberrypi-swd` is
described in [Getting Started with Raspberry Pi Pico](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf) [[2]](#id7). Any other SWD debug
adapter maybe also work with this configuration.

The value of **RPI\_PICO\_DEBUG\_ADAPTER** is cached, so it can be omitted from
`west flash` and `west debug` if it was previously set while running
`west build`.

**RPI\_PICO\_DEBUG\_ADAPTER** is used in an argument to OpenOCD as
`"source [find interface/${RPI_PICO_DEBUG_ADAPTER}.cfg]"`. Thus,
**RPI\_PICO\_DEBUG\_ADAPTER** needs to be assigned the file name of the debug
adapter.

You can also flash the board with the following
command that directly calls OpenOCD (assuming a SEGGER JLink adapter is used):

```shell
$ openocd -f interface/jlink.cfg -c 'transport select swd' -f target/rp2040.cfg -c "adapter speed 2000" -c 'targets rp2040.core0' -c 'program path/to/zephyr.elf verify reset exit'
```

#### Using UF2

If you don’t have an SWD adapter, you can flash the Raspberry Pi Pico with
a UF2 file. By default, building an app for this board will generate a
`build/zephyr/zephyr.uf2` file. If the Pico is powered on with the `BOOTSEL`
button pressed, it will appear on the host as a mass storage device. The
UF2 file should be drag-and-dropped to the device, which will flash the Pico.

### Debugging

The SWD interface can also be used to debug the board. To achieve this, you can
either use SEGGER JLink or OpenOCD.

#### Using SEGGER JLink

Use a SEGGER JLink debug probe and follow the instruction in
[Building, Flashing and Debugging](../../../../develop/west/build-flash-debug.md#west-debugging).

#### Using OpenOCD

Install OpenOCD as described for flashing the board.

Here is an example for debugging the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b w5500_evb_pico samples/basic/blinky -- -DOPENOCD=/usr/local/bin/openocd -DOPENOCD_DEFAULT_PATH=/usr/local/share/openocd/scripts -DRPI_PICO_DEBUG_ADAPTER=raspberrypi-swd
west debug
```

As with flashing, you can specify the debug adapter by specifying
**RPI\_PICO\_DEBUG\_ADAPTER** at `west build` time. No needs to specify it at
`west debug` time.

You can also debug with OpenOCD and gdb launching from command-line.
Run the following command:

```shell
$ openocd -f interface/jlink.cfg -c 'transport select swd' -f target/rp2040.cfg -c "adapter speed 2000" -c 'targets rp2040.core0'
```

On another terminal, run:

```shell
$ gdb-multiarch
```

Inside gdb, run:

```shell
(gdb) tar ext :3333
(gdb) file path/to/zephyr.elf
```

You can then start debugging the board.

[1]
([1](#id5),[2](#id6))

[https://raw.githubusercontent.com/raspberrypi/pico-setup/master/pico\_setup.sh](https://raw.githubusercontent.com/raspberrypi/pico-setup/master/pico_setup.sh)

[[2](#id8)]

[https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)

[[3](#id10)]

[https://docs.wiznet.io/Product/iEthernet/W5500/w5500-evb-pico](https://docs.wiznet.io/Product/iEthernet/W5500/w5500-evb-pico)
