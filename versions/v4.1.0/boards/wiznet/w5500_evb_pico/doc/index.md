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

#### `w5500_evb_pico/rp2040` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L35) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | RaspberryPi Pico ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L295) | [`raspberrypi,pico-adc`](../../../../build/dts/api/bindings/adc/raspberrypi%2Cpico-adc.md#std-dtcompatible-raspberrypi-pico-adc) |
| Clock control | on-chip | Raspberry Pi Pico clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L219) | [`raspberrypi,pico-clock-controller`](../../../../build/dts/api/bindings/clock/raspberrypi%2Cpico-clock-controller.md#std-dtcompatible-raspberrypi-pico-clock-controller) |
| on-chip | The representation of Raspberry Pi Pico’s clock[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L47)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L174) | [`raspberrypi,pico-clock`](../../../../build/dts/api/bindings/clock/raspberrypi%2Cpico-clock.md#std-dtcompatible-raspberrypi-pico-clock) |
| on-chip | The representation of Raspberry Pi Pico’s PLL[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L128) | [`raspberrypi,pico-pll`](../../../../build/dts/api/bindings/clock/raspberrypi%2Cpico-pll.md#std-dtcompatible-raspberrypi-pico-pll) |
| on-chip | The representation of Raspberry Pi Pico ring oscillator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L150) | [`raspberrypi,pico-rosc`](../../../../build/dts/api/bindings/clock/raspberrypi%2Cpico-rosc.md#std-dtcompatible-raspberrypi-pico-rosc) |
| on-chip | The representation of Raspberry Pi Pico external oscillator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L168) | [`raspberrypi,pico-xosc`](../../../../build/dts/api/bindings/clock/raspberrypi%2Cpico-xosc.md#std-dtcompatible-raspberrypi-pico-xosc) |
| Counter | on-chip | RaspberryPi Pico timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L359) | [`raspberrypi,pico-timer`](../../../../build/dts/api/bindings/counter/raspberrypi%2Cpico-timer.md#std-dtcompatible-raspberrypi-pico-timer) |
| DMA | on-chip | Raspberry Pi Pico DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L375) | [`raspberrypi,pico-dma`](../../../../build/dts/api/bindings/dma/raspberrypi%2Cpico-dma.md#std-dtcompatible-raspberrypi-pico-dma) |
| Ethernet | on-board | W5500 standalone 10/100BASE-T Ethernet controller with SPI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wiznet/w5500_evb_pico/w5500_evb_pico.dts?plain=1#L147) | [`wiznet,w5500`](../../../../build/dts/api/bindings/ethernet/wiznet%2Cw5500.md#std-dtcompatible-wiznet-w5500) |
| Flash controller | on-chip | Raspberry Pi Pico flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L197) | [`raspberrypi,pico-flash-controller`](../../../../build/dts/api/bindings/flash_controller/raspberrypi%2Cpico-flash-controller.md#std-dtcompatible-raspberrypi-pico-flash-controller) |
| GPIO & Headers | on-chip | Raspberry Pi Pico GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L241) | [`raspberrypi,pico-gpio`](../../../../build/dts/api/bindings/gpio/raspberrypi%2Cpico-gpio.md#std-dtcompatible-raspberrypi-pico-gpio) |
| on-board | GPIO pins exposed on Raspberry Pi Pico headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wiznet/w5500_evb_pico/w5500_evb_pico.dts?plain=1#L28) | [`raspberrypi,pico-header`](../../../../build/dts/api/bindings/gpio/raspberrypi%2Cpico-header.md#std-dtcompatible-raspberrypi-pico-header) |
| I2C | on-chip | Raspberry Pi Pico I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L306)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L318) | [`raspberrypi,pico-i2c`](../../../../build/dts/api/bindings/i2c/raspberrypi%2Cpico-i2c.md#std-dtcompatible-raspberrypi-pico-i2c) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wiznet/w5500_evb_pico/w5500_evb_pico.dts?plain=1#L61) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wiznet/w5500_evb_pico/w5500_evb_pico.dts?plain=1#L69) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Miscellaneous | on-chip | Raspberry Pi Pico PIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L396) | [`raspberrypi,pico-pio`](../../../../build/dts/api/bindings/misc/raspberrypi%2Cpico-pio.md#std-dtcompatible-raspberrypi-pico-pio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L204) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wiznet/w5500_evb_pico/w5500_evb_pico.dts?plain=1#L91) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | The RPi Pico pin controller is a node responsible for controlling pin function selection and pin properties, such as routing a UART0 Rx to pin 1 and enabling the pullup resistor on that pin[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L423) | [`raspberrypi,pico-pinctrl`](../../../../build/dts/api/bindings/pinctrl/raspberrypi%2Cpico-pinctrl.md#std-dtcompatible-raspberrypi-pico-pinctrl) |
| PWM | on-chip | Raspberry Pi Pico PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L348) | [`raspberrypi,pico-pwm`](../../../../build/dts/api/bindings/pwm/raspberrypi%2Cpico-pwm.md#std-dtcompatible-raspberrypi-pico-pwm) |
| Regulator | on-chip | RaspberryPi Pico core supply regurator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L388) | [`raspberrypi,core-supply-regulator`](../../../../build/dts/api/bindings/regulator/raspberrypi%2Ccore-supply-regulator.md#std-dtcompatible-raspberrypi-core-supply-regulator) |
| Reset controller | on-chip | Raspberry Pi Pico Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L211) | [`raspberrypi,pico-reset`](../../../../build/dts/api/bindings/reset/raspberrypi%2Cpico-reset.md#std-dtcompatible-raspberrypi-pico-reset) |
| RTC | on-chip | RaspberryPi Pico RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L412) | [`raspberrypi,pico-rtc`](../../../../build/dts/api/bindings/rtc/raspberrypi%2Cpico-rtc.md#std-dtcompatible-raspberrypi-pico-rtc) |
| Sensors | on-chip | RaspberryPi Pico family temperature sensor node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L427) | [`raspberrypi,pico-temp`](../../../../build/dts/api/bindings/sensor/raspberrrypi%2Cpico-temp.md#std-dtcompatible-raspberrypi-pico-temp) |
| Serial controller | on-chip | Raspberry Pi Pico UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L251)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L261) | [`raspberrypi,pico-uart`](../../../../build/dts/api/bindings/serial/raspberrypi%2Cpico-uart.md#std-dtcompatible-raspberrypi-pico-uart) |
| SPI | on-chip | Raspberry Pi Pico SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L271)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L283) | [`raspberrypi,pico-spi`](../../../../build/dts/api/bindings/spi/raspberrypi%2Cpico-spi.md#std-dtcompatible-raspberrypi-pico-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L192) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| USB | on-chip | RaspberryPi Pico USB Device Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L337) | [`raspberrypi,pico-usbd`](../../../../build/dts/api/bindings/usb/raspberrypi%2Cpico-usbd.md#std-dtcompatible-raspberrypi-pico-usbd) |
| Watchdog | on-chip | Raspberry Pi Pico Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L330) | [`raspberrypi,pico-watchdog`](../../../../build/dts/api/bindings/watchdog/raspberrypi%2Cpico-watchdog.md#std-dtcompatible-raspberrypi-pico-watchdog) |

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
