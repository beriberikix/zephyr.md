---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm64/rcar_salvator_xs_m3/doc/index.html
original_path: boards/arm64/rcar_salvator_xs_m3/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# R-CAR Salvator XS M3 ARM CA57 (ARMv8)

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

### Supported Features

The Renesas rcar\_salvator\_xs\_m3 board configuration supports the following
hardware features:

| Interface | Driver/components | Support level |
| --- | --- | --- |
| PINCTRL | pinctrl |  |
| CLOCK | clock\_control |  |
| UART | uart | serial port-polling |

Other hardware features have not been enabled yet for this board.

The default configuration can be found in the defconfig file:

> `boards/arm64/rcar_salvator_xs_m3/rcar_salvator_xs_m3_defconfig`

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

## References

- [Renesas R-Car Development Support website](https://www.renesas.com/us/en/support/partners/r-car-consortium/r-car-development-support)
- [eLinux Salvator-XS page](https://elinux.org/R-Car/Boards/Salvator-XS)
