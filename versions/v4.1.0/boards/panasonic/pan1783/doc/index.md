---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/panasonic/pan1783/doc/index.html
original_path: boards/panasonic/pan1783/doc/index.html
---

# PAN1783 Evaluation Board

Board Overview

[![../../../../_images/pan1783_evb.webp](../../../../_images/pan1783_evb.webp)
](../../../../_images/pan1783_evb.webp)

PAN1783 Evaluation Board

Name:
:   `pan1783_evb`

Vendor:
:   Panasonic Corporation

Architecture:
:   arm

SoC:
:   nrf5340

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/panasonic/pan1783/doc/index.rst/../..)

## Overview

The PAN1783, PAN1783A and PAN1783A-PA Evaluation Boards (pan1783\_evb,
pan1783a\_evb, pan1783a\_pa\_evb) are development tools for the PAN1783,
PAN1783A and PAN1783A-PA Modules which are based on the nRF5340 chipset
from Nordic Semiconductor.

More information about the PAN1783, PAN1783A, PAN1783A-PA Modules and
Evaluation Boards can be found on the [product website](https://industry.panasonic.eu/products/devices/wireless-connectivity/bluetooth-low-energy-modules) [[1]](#id2).

## PAN1783 EVB

This variant of the board is depicted in the “Board Overview” sidebar.

## PAN1783A EVB

The PAN1783A EVB essentially looks like a PAN1783 EVB, except that it is
equipped with a UFL connector on X4.

## PAN1783A-PA EVB

The PAN1783A-PA EVB essentially resembles a PAN1783 EVB, with the addition
of a UFL connector on X4 and a power amplifier.

## Usage

For detailed information, you can find the
[pan1783\_evb user guide](https://pideu.panasonic.de/development-hub/pan1783/evaluation_board/user_guide/) [[3]](#id7) / [pan1783a\_evb user guide](https://pideu.panasonic.de/development-hub/pan1783a/evaluation_board/user_guide/) [[4]](#id9) / [pan1783a\_pa\_evb user guide](https://pideu.panasonic.de/development-hub/pan1783a_pa/evaluation_board/user_guide/) [[5]](#id11)
for the Evaluation Boards in the [Panasonic Wireless Connectivity Development Hub](https://pideu.panasonic.de/development-hub/) [[2]](#id4).

The User Guide contains (amongst other things) detailed information about

- pin mapping
- powering options
- breakout pin header interface
- current consumption measurement
- software development

The schematics for the PAN1783/PAN1783A/PAN1783A-PA Evaluation Boards are
available in the [download section PAN1783](https://pideu.panasonic.de/development-hub/pan1783/downloads/) [[6]](#id13) / [download section PAN1783A](https://pideu.panasonic.de/development-hub/pan1783a/downloads/) [[7]](#id15) / [download section PAN1783A-PA](https://pideu.panasonic.de/development-hub/pan1783a_pa/downloads/) [[8]](#id17)
of the [Panasonic Wireless Connectivity Development Hub](https://pideu.panasonic.de/development-hub/) [[2]](#id4).

## Programming and Debugging

Please use the `pan1783_evb_cpuapp`, `pan1783a_evb_cpuapp` or
`pan1783a_pa_evb_cpuapp` for application core and `pan1783_evb_cpunet`,
`pan1783a_evb_cpunet` or `pan1783a_pa_evb_cpunet` board configuration
for network core when [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run).

[[1](#id3)]

[https://industry.panasonic.eu/products/devices/wireless-connectivity/bluetooth-low-energy-modules](https://industry.panasonic.eu/products/devices/wireless-connectivity/bluetooth-low-energy-modules)

[2]
([1](#id5),[2](#id6))

[https://pideu.panasonic.de/development-hub/](https://pideu.panasonic.de/development-hub/)

[[3](#id8)]

[https://pideu.panasonic.de/development-hub/pan1783/evaluation\_board/user\_guide/](https://pideu.panasonic.de/development-hub/pan1783/evaluation_board/user_guide/)

[[4](#id10)]

[https://pideu.panasonic.de/development-hub/pan1783a/evaluation\_board/user\_guide/](https://pideu.panasonic.de/development-hub/pan1783a/evaluation_board/user_guide/)

[[5](#id12)]

[https://pideu.panasonic.de/development-hub/pan1783a\_pa/evaluation\_board/user\_guide/](https://pideu.panasonic.de/development-hub/pan1783a_pa/evaluation_board/user_guide/)

[[6](#id14)]

[https://pideu.panasonic.de/development-hub/pan1783/downloads/](https://pideu.panasonic.de/development-hub/pan1783/downloads/)

[[7](#id16)]

[https://pideu.panasonic.de/development-hub/pan1783a/downloads/](https://pideu.panasonic.de/development-hub/pan1783a/downloads/)

[[8](#id18)]

[https://pideu.panasonic.de/development-hub/pan1783a\_pa/downloads/](https://pideu.panasonic.de/development-hub/pan1783a_pa/downloads/)
