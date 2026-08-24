---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rcar_salvator_xs/doc/index.html
original_path: boards/renesas/rcar_salvator_xs/doc/index.html
---

# R-Car Salvator-XS

Board Overview

[![../../../../_images/rcar_salvator_xs.jpg](https://docs.zephyrproject.org/4.2.0/_images/rcar_salvator_xs.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/rcar_salvator_xs.jpg)

R-Car Salvator-XS

Name:
:   `rcar_salvator_xs`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm64

SoC:
:   r8a77961

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rcar_salvator_xs/doc/index.rst/../..)

## Overview

The R-Car M3-W is an SOC that features the basic functions for next-generation
car navigation systems.

## Hardware

The R-Car M3-W includes:

- two 1.5-GHz ARM Cortex-A57 MPCore cores;
- four 1.3-GHz ARM Cortex-A53 MPCore cores,
- memory controller for LPDDR4-3200 with 32 bits x 2 channels;
- 1 channels for HDMI1.4b output and 1 channel for RGB888 output and 1channel for LVDS;
- 2 channels MIPI-CSI2 Video Input, 2 channels digital Video Input;
- USB3.0 x 1ch and USB2.0 x 2ch interfaces;
- 800-MHz ARM Cortex-R7 core;
- two- and three-dimensional graphics engines;
- video processing units;
- sound processing units;
- MediaLB interface;
- SD card host interface;
- USB3.0 and USB2.0 interfaces;
- PCI Express interface;
- CAN interface;
- EtherAVB.

Hardware capabilities for the Salvator-XS for can be found on the [eLinux Salvator-XS page](https://elinux.org/R-Car/Boards/Salvator-XS).

### Supported Features

The `rcar_salvator_xs` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rcar_salvator_xs/r8a77961` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| Clock control | on-chip | Renesas R8A7795 SoC Clock Pulse Generator / Module Standby and Software Reset[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L69) | [`renesas,r8a7795-cpg-mssr`](../../../../build/dts/api/bindings/clock/renesas%2Cr8a7795-cpg-mssr.md#std-dtcompatible-renesas-r8a7795-cpg-mssr) |
| GPIO & Headers | on-chip | Renesas RCAR GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L76) | [`renesas,rcar-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Crcar-gpio.md#std-dtcompatible-renesas-rcar-gpio) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L51) | [`arm,gic-v2`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v2.md#std-dtcompatible-arm-gic-v2) |
| MMC | on-chip | Renesas R-Car eMMC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L87) | [`renesas,rcar-mmc`](../../../../build/dts/api/bindings/mmc/renesas%2Crcar-emmc.md#std-dtcompatible-renesas-rcar-mmc) |
| Pin control | on-chip | Renesas R-Car Pin Function Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L109) | [`renesas,rcar-pfc`](../../../../build/dts/api/bindings/pinctrl/renesas%2Crcar-pfc.md#std-dtcompatible-renesas-rcar-pfc) |
| Power management CPU operations | on-chip | Power State Coordination Interface (PSCI) version 0.2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L17) | [`arm,psci-0.2`](../../../../build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.md#std-dtcompatible-arm-psci-0.2) |
| Regulator | on-chip | Fixed voltage regulators[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L31) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| Serial controller | on-chip | Renesas R-Car UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L114) | [`renesas,rcar-scif`](../../../../build/dts/api/bindings/serial/renesas%2Crcar-scif.md#std-dtcompatible-renesas-rcar-scif) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L22) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

## References

- [Renesas R-Car Development Support website](https://www.renesas.com/us/en/support/partners/r-car-consortium/r-car-development-support)
- [eLinux Salvator-XS page](https://elinux.org/R-Car/Boards/Salvator-XS)
