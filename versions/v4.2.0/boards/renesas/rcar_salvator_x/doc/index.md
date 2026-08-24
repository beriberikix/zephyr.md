---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rcar_salvator_x/doc/index.html
original_path: boards/renesas/rcar_salvator_x/doc/index.html
---

# R-Car Salvator-X

Board Overview

[![../../../../_images/rcar_salvator_x.jpg](https://docs.zephyrproject.org/4.2.0/_images/rcar_salvator_x.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/rcar_salvator_x.jpg)

R-Car Salvator-X

Name:
:   `rcar_salvator_x`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r8a77951

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rcar_salvator_x/doc/index.rst/../..)

## Overview

- The H3 Salvator-X board is designed for evaluating the features and performance
  of the R-CAR H3 device from Renesas Electronics and it is also used for developing
  and evaluating application software for these R-CAR H3.
- The H3 Salvator-X, based on the R-CAR H3 SIP, comes with LPDDR4 @4GB in 2-channel,
  each 64-bit wide+Hyperflash @64MB, CSI2 interfaces and several communication interfaces
  like USB, Ethernet, HDMI and can work standalone or can be adapted to other boards,
  via 440pin connector on bottom side.

More information about the H3 SoC can be found here: [Renesas R-Car H3 chip](https://www.renesas.com/eu/en/products/automotive-products/automotive-system-chips-socs/r-car-h3-high-end-automotive-system-chip-soc-vehicle-infotainment-and-driving-safety-support)

## Hardware

Hardware capabilities for the H3 Salvator-X for can be found on the [eLinux H3 Salvator-X page](https://elinux.org/R-Car/Boards/Salvator-X).

Note

Zephyr will be booted on the CR7 processor provided for RTOS purpose.

More information about the board can be found at [Renesas R-Car Development Support website](https://www.renesas.com/us/en/support/partners/r-car-consortium/r-car-development-support).

### Supported Features

The `rcar_salvator_x` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rcar_salvator_x/r8a77951/r7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L20) | [`arm,cortex-r7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r7.md#std-dtcompatible-arm-cortex-r7) |
| CAN | on-chip | Renesas R-Car CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L91) | [`renesas,rcar-can`](../../../../build/dts/api/bindings/can/renesas%2Crcar-can.md#std-dtcompatible-renesas-rcar-can) |
| Clock control | on-chip | Renesas R8A7795 SoC Clock Pulse Generator / Module Standby and Software Reset[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/r8a77951.dtsi?plain=1#L12) | [`renesas,r8a7795-cpg-mssr`](../../../../build/dts/api/bindings/clock/renesas%2Cr8a7795-cpg-mssr.md#std-dtcompatible-renesas-r8a7795-cpg-mssr) |
| GPIO & Headers | on-chip | Renesas RCAR GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L55)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L44) | [`renesas,rcar-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Crcar-gpio.md#std-dtcompatible-renesas-rcar-gpio) |
| I2C | on-chip | Renesas R-Car I2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L100) | [`renesas,rcar-i2c`](../../../../build/dts/api/bindings/i2c/renesas%2Crcar-i2c.md#std-dtcompatible-renesas-rcar-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rcar_salvator_x/rcar_salvator_x_r8a77951_r7.dts?plain=1#L40) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L33) | [`arm,gic-v2`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v2.md#std-dtcompatible-arm-gic-v2) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rcar_salvator_x/rcar_salvator_x_r8a77951_r7.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Pin control | on-chip | Renesas R-Car Pin Function Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L66) | [`renesas,rcar-pfc`](../../../../build/dts/api/bindings/pinctrl/renesas%2Crcar-pfc.md#std-dtcompatible-renesas-rcar-pfc) |
| PWM | on-chip | Renesas R-Car PWM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L71) | [`renesas,pwm-rcar`](../../../../build/dts/api/bindings/pwm/renesas%2Cpwm-rcar.md#std-dtcompatible-renesas-pwm-rcar) |
| Serial controller | on-chip | Renesas R-Car UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L126)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L136) | [`renesas,rcar-scif`](../../../../build/dts/api/bindings/serial/renesas%2Crcar-scif.md#std-dtcompatible-renesas-rcar-scif) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Renesas R-Car CMT timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L78) | [`renesas,rcar-cmt`](../../../../build/dts/api/bindings/timer/renesas%2Crcar-cmt.md#std-dtcompatible-renesas-rcar-cmt) |

Note

It is recommended to disable peripherals used by the R7 core on the Linux host.

### Connections and IOs

![R-Car Salvator-X connections](https://docs.zephyrproject.org/4.2.0/_images/r-car-h3-salvator-x-connections.jpg)

#### GPIO

By running Zephyr on H3 Salvator-X, the software readable push buttons ‘SW20’,
‘SW21’, ‘SW22’ can be used as input, and the software contollable LEDs ‘LED4’,
‘LED5’, ‘LED6’ can be used as output.

#### UART

Salvator-X board is providing two serial ports:

- one is for A53/A57 processors
- the other one is for CR7

Both ports are converted to USB through CP2102 converters and they are exposed
as follows:

| Connector | Processor |
| --- | --- |
| CN25 | A53/A57 |
| CN26 | CR7 |

## Programming and Debugging

The `rcar_salvator_x` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Supported Debug Probe

The “Olimex ARM-USB-OCD-H” probe is the only officially supported probe. This
probe is supported by OpenOCD that is shipped with the Zephyr SDK.

The “Olimex ARM-USB-OCD-H” probe needs to be connected to CN1 on Salvator-X.

### Configuring a Console

Connect a USB cable from your PC to CN25 and/or CN26 then use the following
settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

First of all, open your serial terminal.

Applications for the `rcar_salvator_x` board configuration can be built
in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) for more details).

```shell
# From the root of the zephyr repository
west build -b rcar_salvator_x samples/hello_world
west flash
```

You should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v2.6.0-rc1 ***
Hello World! rcar_salvator_x
```

### Debugging

First of all, open your serial terminal.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rcar_salvator_x samples/hello_world
west debug
```

You will then get access to a GDB session for debug.

By continuing the app, you should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v2.6.0-rc1 ***
Hello World! rcar_salvator_x
```

## References

- [Renesas R-Car H3 chip](https://www.renesas.com/eu/en/products/automotive-products/automotive-system-chips-socs/r-car-h3-high-end-automotive-system-chip-soc-vehicle-infotainment-and-driving-safety-support)
- [Renesas R-Car Development Support website](https://www.renesas.com/us/en/support/partners/r-car-consortium/r-car-development-support)
- [eLinux H3 Salvator-X page](https://elinux.org/R-Car/Boards/Salvator-X)
