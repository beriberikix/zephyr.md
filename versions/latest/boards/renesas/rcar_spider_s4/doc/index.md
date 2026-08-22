---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rcar_spider_s4/doc/index.html
original_path: boards/renesas/rcar_spider_s4/doc/index.html
---

# R-Car Spider

Board Overview

[![../../../../_images/rcar_spider_s4.jpg](../../../../_images/rcar_spider_s4.jpg)
](../../../../_images/rcar_spider_s4.jpg)

R-Car Spider

Name:
:   `rcar_spider_s4`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm64, arm

SoC:
:   r8a779f0

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rcar_spider_s4/doc/index.rst/../..)

## Overview

R-Car S4 Spider board is based on the R-Car S4 SoC made for Car
Server/Communication Gateway and that is composed of a octo Cortex®-A55, a
dual lockstep Cortex®-R52 and a double dual lockstep G4MH.

The R-Car S4 SoC enables the launch of Car Server/CoGW with high performance,
high-speed networking, high security and high functional safety levels that are
required as E/E architectures evolve into domains and zones.

The R-Car S4 solution allows designers to re-use up to 88 percent of software
code developed for 3rd generation R-Car SoCs and RH850 MCU applications.
The software package supports the real-time cores with various drivers and
basic software such as Linux BSP and hypervisors.

The Renesas R-Car Spider board is the Renesas R-Car S4 reference board and is designed for
evaluating features and performance of this SoC.

Zephyr OS support is available for both Cortex®-A cores & Cortex®-R52 core.

More information about the S4 SoC can be fount at [Renesas R-Car S4 chip](https://www.renesas.com/us/en/products/automotive-products/automotive-system-chips-socs/r-car-s4-automotive-system-chip-soc-car-servercommunication-gateway).

## Hardware

- Spider features:

  - Connectors

    - CPU Board:

      - CN1 JTAG1
      - CN2 JTAG2
      - CN3 EX-SPI (QSPI0)
      - CN4 MicroSD Slot (back side)
      - CN11 EXIO Connector A (back side)
      - CN12 EXIO Connector B (back side)
      - CN14 EVT
      - CN16 OcuLink (PCIe0,PCIe1)
      - CN24 CAN 4pin
      - CN20 USB microAB (SCIF0)
      - CN21 USB microAB (HSCIF0)
      - CN22 SW Board
      - CN23 CPLD JTAG
      - CN27 FAN
      - CN30 Buck3
      - CN31 Buck1
      - CN32 CAN 8pin (back side)
    - Breakout Board:

      - CN11 EXIO Connector A
      - CN12 EXIO Connector B
      - CN13 CAN 0/1
      - CN15 CAN 3/4/5
      - CN18 CAN 6/7/8
      - CN21 CAN 2/9/10/11
      - CN24 CAN 12/13/14/15
      - CN28 LIN0
      - CN29 LIN1
      - CN30 LIN2
      - CN31 LIN3
      - CN32 LIN4
      - CN33 LIN5
      - CN34 LIN6
      - CN35 LIN7
      - CN36 EtherTS
      - CN37 MSIOF0
      - CN38 CAN/LIN BOARD
      - CN39 GPIO CN\_A
      - CN40 GPIO
      - CN41 I2C
      - CN42 HSCIF0
      - CN43 SCIF0
      - CN44 TSN\_CN
      - CN45 Legacy 12V-in
      - CN46 AC Adapter
      - CN48 POWER CONTROL
      - CN50 Debug Serial
      - CN51 FAN
  - Input

    - SW1 (SPI Flash Memory / EX-SPI connector)
    - SW2 (Hyper Flash Memory / SPI Flash Memory)
    - SW3 (MicroSD Card Slot / eMMC Memory)
    - SW4 (PRESETn)
    - SW6 (Interface Voltage Setting for MMC/JTAG2)
    - SW8 Mode Setting
    - SW10 (Software Switch)
    - SW11 (Board Power-Supply Circuit Control)
    - SW12 (AURORES#)
    - SW13 (CANFD0 RX)
    - SW14 (CANFD0 TX)
    - SW15 (System Reset Switch)
  - Output

    - LED7 Software Controllable LED
    - LED8 Software Controllable LED

### Supported Features

The `rcar_spider_s4` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rcar_spider_s4/r8a779f0/a55` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| Clock control | on-chip | Renesas R8A779F0 SoC Clock Pulse Generator / Module Standby and Software Reset[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/r8a779f0.dtsi?plain=1#L83) | [`renesas,r8a779f0-cpg-mssr`](../../../../build/dts/api/bindings/clock/renesas%2Cr8a779f0-cpg-mssr.md#std-dtcompatible-renesas-r8a779f0-cpg-mssr) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/r8a779f0.dtsi?plain=1#L73) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| MMC | on-chip | Renesas R-Car eMMC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/r8a779f0.dtsi?plain=1#L91) | [`renesas,rcar-mmc`](../../../../build/dts/api/bindings/mmc/renesas%2Crcar-emmc.md#std-dtcompatible-renesas-rcar-mmc) |
| Pin control | on-chip | Renesas R-Car Pin Function Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/r8a779f0.dtsi?plain=1#L102) | [`renesas,rcar-pfc`](../../../../build/dts/api/bindings/pinctrl/renesas%2Crcar-pfc.md#std-dtcompatible-renesas-rcar-pfc) |
| Power management CPU operations | on-chip | Power State Coordination Interface (PSCI) version 0.2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/r8a779f0.dtsi?plain=1#L31) | [`arm,psci-0.2`](../../../../build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.md#std-dtcompatible-arm-psci-0.2) |
| Regulator | on-chip | Fixed voltage regulators[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/r8a779f0.dtsi?plain=1#L45) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| Serial controller | on-chip | Renesas R-Car HSCIF controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/r8a779f0.dtsi?plain=1#L110) | [`renesas,rcar-hscif`](../../../../build/dts/api/bindings/serial/renesas%2Crcar-hscif.md#std-dtcompatible-renesas-rcar-hscif) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/r8a779f0.dtsi?plain=1#L36) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |

#### `rcar_spider_s4/r8a779f0/r52` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R52 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen4/rcar_gen4_cr52.dtsi?plain=1#L17) | [`arm,cortex-r52`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r52.md#std-dtcompatible-arm-cortex-r52) |
| Clock control | on-chip | Renesas R8A779F0 SoC Clock Pulse Generator / Module Standby and Software Reset[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen4/r8a779f0.dtsi?plain=1#L28) | [`renesas,r8a779f0-cpg-mssr`](../../../../build/dts/api/bindings/clock/renesas%2Cr8a779f0-cpg-mssr.md#std-dtcompatible-renesas-r8a779f0-cpg-mssr) |
| GPIO & Headers | on-chip | Renesas RCAR GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen4/r8a779f0.dtsi?plain=1#L34) | [`renesas,rcar-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Crcar-gpio.md#std-dtcompatible-renesas-rcar-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rcar_spider_s4/rcar_spider_s4_r8a779f0_r52.dts?plain=1#L31) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen4/rcar_gen4_cr52.dtsi?plain=1#L45) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rcar_spider_s4/rcar_spider_s4_r8a779f0_r52.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Pin control | on-chip | Renesas R-Car Pin Function Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen4/r8a779f0.dtsi?plain=1#L17) | [`renesas,rcar-pfc`](../../../../build/dts/api/bindings/pinctrl/renesas%2Crcar-pfc.md#std-dtcompatible-renesas-rcar-pfc) |
| Serial controller | on-chip | Renesas R-Car UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen4/rcar_gen4_cr52.dtsi?plain=1#L54)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen4/rcar_gen4_cr52.dtsi?plain=1#L61) | [`renesas,rcar-scif`](../../../../build/dts/api/bindings/serial/renesas%2Crcar-scif.md#std-dtcompatible-renesas-rcar-scif) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen4/rcar_gen4_cr52.dtsi?plain=1#L40) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rcar/gen4/rcar_gen4_cr52.dtsi?plain=1#L24) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |

Note

It is recommended to disable peripherals used by the R52 core on the Linux host.

### Connections and IOs

The Spider board consists of a CPU board plugged on top of a Breakout board.

Here are the official IOs figures from eLinux for S4 board:

[S4 Spider CPU board IOs](https://elinux.org/images/6/6d/Rcar_s4_spider_cpu_board.jpg)

[S4 Spider breakout board IOs](https://elinux.org/images/2/29/Rcar_s4_spider_breakout_board.jpg)

#### GPIO

By running Zephyr on S4 Spider, the software controllable LED ‘LED8’ can be used as output.

#### UART

Here is information about both serial ports provided on the S4 Spider board :

| Physical Interface | Location | Software Interface | Converter | Further Information |
| --- | --- | --- | --- | --- |
| CN20 USB Port | CPU Board | SCIF0/HSCIF1 | FT232HQ | Default Zephyr serial |
| CN21 USB Port | CPU Board | SCIF3/HSCIF0 | FT2232H-56Q | Used by U-BOOT & Linux |

Note

The Zephyr console output is assigned to SCIF0 (CN20 USB Port) with settings:
115200 8N1 without hardware flow control by default.

#### I2C

I2C is mainly used to manage and power-on some onboard chips on the S4 Spider board.

Embedded I2C devices and I/O expanders are not yet supported.
The current I2C support therefore does not make any devices available to the user at this time.

## Programming and Debugging (A55)

At that time, no direct flashing method is officially supported by this Zephyr port.
However, it is possible to load the Zephyr binary using U-Boot commands.

One of the ways to load Zephyr is shown below.

```shell
tftp 0x48000000 <tftp_server_path/zephyr.bin>
booti 0x48000000
```

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rcar_spider_s4/r8a779f0/a55 samples/hello_world
```

## Programming and Debugging (R52)

The `rcar_spider_s4` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Supported Debug Probe

The “Olimex ARM-USB-OCD-H” probe is the only officially supported probe.

This probe is supported by OpenOCD that is shipped with the Zephyr SDK.

The “Olimex ARM-USB-OCD-H” probe needs to be connected with a “Coresight 20 pins”
adapter to CN1 connector on Spider board.

### Configuring a Console

Connect a USB cable from your PC to CN20 USB port of your Spider board.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

First of all, open your serial terminal.

Applications for the `rcar_spider_s4/r8a779f0/r52` board configuration can be built in the
usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) for more details).

```shell
# From the root of the zephyr repository
west build -b rcar_spider_s4/r8a779f0/r52 samples/hello_world
west flash
```

You should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.3.0-rc2 ***
Hello World! rcar_spider_s4
```

### Debugging

First of all, open your serial terminal.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rcar_spider_s4/r8a779f0/r52 samples/hello_world
west debug
```

You will then get access to a GDB session for debugging.

By continuing the app, you should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.3.0-rc2 ***
Hello World! rcar_spider_s4
```

## References

- [Renesas R-Car S4 Spider](https://www.renesas.com/us/en/products/automotive-products/automotive-system-chips-socs/rtp8a779f0askb0sp2s-r-car-s4-reference-boardspider)
- [Renesas R-Car S4 chip](https://www.renesas.com/us/en/products/automotive-products/automotive-system-chips-socs/r-car-s4-automotive-system-chip-soc-car-servercommunication-gateway)
- [eLinux S4 Spider](https://elinux.org/R-Car/Boards/Spider)
