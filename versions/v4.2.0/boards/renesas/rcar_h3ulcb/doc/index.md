---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rcar_h3ulcb/doc/index.html
original_path: boards/renesas/rcar_h3ulcb/doc/index.html
---

# R-Car H3ULCB

Board Overview

[![../../../../_images/rcar_h3ulcb.jpg](https://docs.zephyrproject.org/4.2.0/_images/rcar_h3ulcb.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/rcar_h3ulcb.jpg)

R-Car H3ULCB

Name:
:   `rcar_h3ulcb`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm64, arm

SoC:
:   r8a77951

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rcar_h3ulcb/doc/index.rst/../..)

## Overview

R-Car H3ULCB starter kit board is based on the R-Car H3 SoC that features basic
functions for next-generation car navigation systems.
It is composed of a quad Cortex®-A57, a quad Cortex®-A53 cluster and a
dual lockstep Cortex®-R7.

Zephyr OS support is available for both Cortex®-A cores & Cortex®-R7 core.

More information about the H3 SoC can be fount at [Renesas R-Car H3 chip](https://www.renesas.com/eu/en/products/automotive-products/automotive-system-chips-socs/r-car-h3-high-end-automotive-system-chip-soc-vehicle-infotainment-and-driving-safety-support).

## Hardware

- H3ULCB features:

  - Storage:

    - 384KB System RAM
    - 4/8 GB LPDDR4
    - 64 MB HYPER FLASH (512 MBITS, 160 MHZ, 320 MBYTES/S)
    - 16MB QSPI FLASH (128 MBITS,80 MHZ,80 MBYTES/S)1 HEADER QSPI MODULE
    - 8/32/64/128 GB EMMC (HS400 240 MBYTES/S)
    - MICROSD-CARD SLOT (SDR104 100 MBYTES/S)
  - Connectors

    - CN1 COM Express type connector 440pin
    - CN2 QSPI Flash module
    - CN3 DEBUG JTAG
    - CN4 HDMI (HDMI-0)
    - CN5 USB 2.0 (USB2.0-1)
    - CN6 Push-Pull microSD Card Socket (SDHI-0)
    - CN7 Ethernet, Connector, RJ45
    - CN8 LINE Out
    - CN9 MIC Input
    - CN10 DEBUG SERIAL (not populated)
    - CN11 CPLD Programming JTAG
    - CN12 DEBUG SERIAL (serial)
    - CN13 Main Power Supply input (5VDC)
    - CN14 CPU Fan
  - Input

    - SW1 Hyper Flash
    - SW2 Software Readable DIPSWITCHES (4x)
    - SW3 Software Readable Push button
    - SW4 Software Readable Push button
    - SW5 Software Readable Push button
    - SW6 Mode Settings
    - SW7 CPLD Reset
    - SW8 Power
    - SW9 Reset
  - Output

    - LED1 HDMI / Hot Plug Sync Detect
    - LED4 Software Controllable LED
    - LED5 Software Controllable LED
    - LED6 Software Controllable LED
    - LED9 5V Main Supply
    - LED14 Backup LED
    - LED15 System Reset

Complete list of the H3ULCB board capabilities can be found on the [eLinux H3SK page](https://elinux.org/R-Car/Boards/H3SK) of the board.

More information about the board can be found at [Renesas R-Car Starter Kit website](https://www.renesas.com/br/en/products/automotive-products/automotive-system-chips-socs/r-car-h3-m3-starter-kit).

### Supported Features

The `rcar_h3ulcb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rcar_h3ulcb/r8a77951/a57` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| Clock control | on-chip | Renesas R8A7795 SoC Clock Pulse Generator / Module Standby and Software Reset[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L69) | [`renesas,r8a7795-cpg-mssr`](../../../../build/dts/api/bindings/clock/renesas%2Cr8a7795-cpg-mssr.md#std-dtcompatible-renesas-r8a7795-cpg-mssr) |
| GPIO & Headers | on-chip | Renesas RCAR GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L76) | [`renesas,rcar-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Crcar-gpio.md#std-dtcompatible-renesas-rcar-gpio) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L51) | [`arm,gic-v2`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v2.md#std-dtcompatible-arm-gic-v2) |
| MMC | on-chip | Renesas R-Car eMMC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L87)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L97) | [`renesas,rcar-mmc`](../../../../build/dts/api/bindings/mmc/renesas%2Crcar-emmc.md#std-dtcompatible-renesas-rcar-mmc) |
| Pin control | on-chip | Renesas R-Car Pin Function Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L109) | [`renesas,rcar-pfc`](../../../../build/dts/api/bindings/pinctrl/renesas%2Crcar-pfc.md#std-dtcompatible-renesas-rcar-pfc) |
| Power management CPU operations | on-chip | Power State Coordination Interface (PSCI) version 0.2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L17) | [`arm,psci-0.2`](../../../../build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.md#std-dtcompatible-arm-psci-0.2) |
| Regulator | on-chip | Fixed voltage regulators[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L31) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| on-board | GPIO-controlled voltage of regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rcar_h3ulcb/rcar_h3ulcb_r8a77951_a57.dts?plain=1#L43) | [`regulator-gpio`](../../../../build/dts/api/bindings/regulator/regulator-gpio.md#std-dtcompatible-regulator-gpio) |
| Serial controller | on-chip | Renesas R-Car UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L114) | [`renesas,rcar-scif`](../../../../build/dts/api/bindings/serial/renesas%2Crcar-scif.md#std-dtcompatible-renesas-rcar-scif) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L22) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |

#### `rcar_h3ulcb/r8a77951/r7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L20) | [`arm,cortex-r7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r7.md#std-dtcompatible-arm-cortex-r7) |
| CAN | on-chip | Renesas R-Car CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L91) | [`renesas,rcar-can`](../../../../build/dts/api/bindings/can/renesas%2Crcar-can.md#std-dtcompatible-renesas-rcar-can) |
| Clock control | on-chip | Renesas R8A7795 SoC Clock Pulse Generator / Module Standby and Software Reset[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/r8a77951.dtsi?plain=1#L12) | [`renesas,r8a7795-cpg-mssr`](../../../../build/dts/api/bindings/clock/renesas%2Cr8a7795-cpg-mssr.md#std-dtcompatible-renesas-r8a7795-cpg-mssr) |
| GPIO & Headers | on-chip | Renesas RCAR GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L55)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L44) | [`renesas,rcar-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Crcar-gpio.md#std-dtcompatible-renesas-rcar-gpio) |
| I2C | on-chip | Renesas R-Car I2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L100) | [`renesas,rcar-i2c`](../../../../build/dts/api/bindings/i2c/renesas%2Crcar-i2c.md#std-dtcompatible-renesas-rcar-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rcar_h3ulcb/rcar_h3ulcb_r8a77951_r7.dts?plain=1#L32) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L33) | [`arm,gic-v2`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v2.md#std-dtcompatible-arm-gic-v2) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rcar_h3ulcb/rcar_h3ulcb_r8a77951_r7.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Pin control | on-chip | Renesas R-Car Pin Function Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L66) | [`renesas,rcar-pfc`](../../../../build/dts/api/bindings/pinctrl/renesas%2Crcar-pfc.md#std-dtcompatible-renesas-rcar-pfc) |
| PWM | on-chip | Renesas R-Car PWM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L71) | [`renesas,pwm-rcar`](../../../../build/dts/api/bindings/pwm/renesas%2Cpwm-rcar.md#std-dtcompatible-renesas-pwm-rcar) |
| Serial controller | on-chip | Renesas R-Car UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L126)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L136) | [`renesas,rcar-scif`](../../../../build/dts/api/bindings/serial/renesas%2Crcar-scif.md#std-dtcompatible-renesas-rcar-scif) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Renesas R-Car CMT timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen3/rcar_gen3_cr7.dtsi?plain=1#L78) | [`renesas,rcar-cmt`](../../../../build/dts/api/bindings/timer/renesas%2Crcar-cmt.md#std-dtcompatible-renesas-rcar-cmt) |

Note

It is recommended to disable peripherals used by the R7 core on the Linux host.

### Connections and IOs

The H3ULCB Starter Kit can be plugged on a Kingfisher daughter board.

#### H3ULCB Board

Here are official IOs figures from eLinux for H3ULCB board:

[H3SK top view](https://elinux.org/images/1/1f/R-Car-H3-topview.jpg)

[H3SK bottom view](https://elinux.org/images/c/c2/R-Car-H3-bottomview.jpg)

#### Kingfisher Infotainment daughter board

When connected to Kingfisher Infotainment board through COMExpress connector, the board is exposing much more IOs.

Here are official IOs figures from eLinux for Kingfisher Infotainment board:

[Kingfisher top view](https://elinux.org/images/0/08/Kfisher_top_specs.png)

[Kingfisher bottom view](https://elinux.org/images/0/06/Kfisher_bot_specs.png)

#### GPIO

By running Zephyr on H3ULCB, the software readable push button ‘SW3’ can be used as input, and the software controllable LED ‘LED5’ can be used as output.

#### UART

H3ULCB board is providing two serial ports, only one is commonly available on the board, however, the second one can be made available either by welding components or by plugging the board on a Kingfisher Infotainment daughter board.

Here is information about these serial ports:

| Physical Interface | Physical Location | Software Interface | Converter | Further Information |
| --- | --- | --- | --- | --- |
| CN12 DEBUG SERIAL | ULCB Board | SCIF2 | FT232RQ | Used by U-BOOT & Linux |
| CN10 DEBUG SERIAL | ULCB Board | SCIF1 | CP2102 | Non-welded |
| CN04 DEBUG SERIAL | Kingfisher | SCIF1 |  | Secondary UART // Through ComExpress |

H3ULCB A53 support is assigning SCIF2 as UART while R7 supports is using SCIF1. In both cases, console are set to 115200 8N1 without hardware flow control by default.

To access SCIF1 using CN04 UART interface, please follow the following pinout (depending on your Kingfisher board version):

| Signal | Pin KF03 | Pin KF04 |
| --- | --- | --- |
| RXD | 3 | 4 |
| TXD | 5 | 2 |
| RTS | 4 | 1 |
| CTS | 6 | 3 |
| GND | 9 | 6 |

#### CAN

H3ULCB board provides two CAN interfaces. Both interfaces are available on the Kingfisher daughter board.

| Physical Interface | Software Interface | Transceiver |
| --- | --- | --- |
| CN17 | CAN0 | TCAN332GDCNT |
| CN18 | CAN1 | TCAN332GDCNT |

Note

Interfaces are set to 125 kbit/s by default.

The following table lists CAN physical interfaces pinout:

| Pin | Signal |
| --- | --- |
| 1 | CANH |
| 2 | CANL |
| 3 | GND |

#### I2C

H3ULCB board provides two I2C buses. Unfortunately direct access to these buses is not available through connectors.

I2C is mainly used to manage and power on multiple of onboard chips on the H3ULCB and Kingfisher daughter board.

Embedded I2C devices and I/O expanders are not yet supported. The current I2C support therefore does not make any devices available to the user at this time.

#### PWM

ULCB boards provide one PWM controller with a maximum of 7 channels [0..6]. H3ULCB does provide the pwm0 from test pin CP8 only.

When plugged on a Kingfisher daughter board, pwm4 channel is available on CN7 LVDS connector.

## Programming and Debugging (A53)

### Flashing

At that time, no flashing method is officially supported by this Zephyr port.

## Programming and Debugging (R7)

The `rcar_h3ulcb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Supported Debug Probe

The “Olimex ARM-USB-OCD-H” probe is the only officially supported probe. This probe is supported by OpenOCD that is shipped with the Zephyr SDK.

The “Olimex ARM-USB-OCD-H” probe needs to be connected with a SICA20I2P adapter to CN3 on H3ULCB.

Note

See [eLinux Kingfisher page](https://elinux.org/R-Car/Boards/Kingfisher) “Known issues” section if you encounter problem with JTAG.

### Configuring a Console

Connect a USB cable from your PC to CN04 of your Kingfisher daughter board.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

First of all, open your serial terminal.

Applications for the `rcar_h3ulcb/r8a77951/r7` board configuration can be built in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) for more details).

```shell
# From the root of the zephyr repository
west build -b rcar_h3ulcb/r8a77951/r7 samples/hello_world
west flash
```

You should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v2.6.0-rc1 ***
Hello World! rcar_h3ulcb
```

### Debugging

First of all, open your serial terminal.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rcar_h3ulcb/r8a77951/r7 samples/hello_world
west debug
```

You will then get access to a GDB session for debug.

By continuing the app, you should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v2.6.0-rc1 ***
Hello World! rcar_h3ulcb
```

## References

- [Renesas R-Car Starter Kit website](https://www.renesas.com/br/en/products/automotive-products/automotive-system-chips-socs/r-car-h3-m3-starter-kit)
- [Renesas R-Car H3 chip](https://www.renesas.com/eu/en/products/automotive-products/automotive-system-chips-socs/r-car-h3-high-end-automotive-system-chip-soc-vehicle-infotainment-and-driving-safety-support)
- [eLinux H3SK page](https://elinux.org/R-Car/Boards/H3SK)
- [eLinux Kingfisher page](https://elinux.org/R-Car/Boards/Kingfisher)
