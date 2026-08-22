---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rcar_salvator_xs/doc/index.html
original_path: boards/renesas/rcar_salvator_xs/doc/index.html
---

# R-Car Salvator-XS

Board Overview

[![../../../../_images/rcar_salvator_xs.jpg](../../../../_images/rcar_salvator_xs.jpg)
](../../../../_images/rcar_salvator_xs.jpg)

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

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

## References

- [Renesas R-Car Development Support website](https://www.renesas.com/us/en/support/partners/r-car-consortium/r-car-development-support)
- [eLinux Salvator-XS page](https://elinux.org/R-Car/Boards/Salvator-XS)
