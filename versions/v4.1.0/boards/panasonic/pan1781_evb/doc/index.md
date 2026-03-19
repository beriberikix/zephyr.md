---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/panasonic/pan1781_evb/doc/index.html
original_path: boards/panasonic/pan1781_evb/doc/index.html
---

# PAN1781 Evaluation Board

Board Overview

[![../../../../_images/pan1781_evaluation_board.jpg](../../../../_images/pan1781_evaluation_board.jpg)
](../../../../_images/pan1781_evaluation_board.jpg)

PAN1781 Evaluation Board

Name:
:   `pan1781_evb`

Vendor:
:   Panasonic Corporation

Architecture:
:   arm

SoC:
:   nrf52820

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/panasonic/pan1781_evb/doc/index.rst/../..)

## Overview

The PAN1781 Evaluation Board is a development tool for the PAN1781 module
which is based on the nRF52820 chipset from Nordic Semiconductor.

You can find more information about the PAN1781 module and the PAN1781
evaluation board on the [product website](https://industry.panasonic.eu/products/devices/wireless-connectivity/bluetooth-low-energy-modules/pan1781-nrf52820) [[1]](#id2).

Please also refer to [nRF52820 emulation on nRF52833 DK](../../../nordic/nrf52833dk/doc/index.md#nrf52833dk-nrf52820) for general information about
development kits for the nRF52820 from Nordic Semiconductor.

The PAN1781 evaluation board is closely linked to these other evaluation
boards:

- [PAN1780 Evaluation Board](../../pan1780_evb/doc/index.md#pan1780_evb)
- [PAN1782 Evaluation Board](../../pan1782_evb/doc/index.md#pan1782_evb)

## Usage

You can find the [user guide](https://pideu.panasonic.de/development-hub/pan1781/evaluation_board/user_guide/) [[3]](#id7) for the PAN1781 Evaluation Board in the
[Panasonic Wireless Connectivity Development Hub](https://pideu.panasonic.de/development-hub/) [[2]](#id4).

The user guide contains (amongst other things) detailed information about

- pin mapping
- powering options
- breakout pin header interface
- current consumption measurement
- software development

and other things.

The schematics for the PAN1781 Evaluation Board are available in the
[download section](https://pideu.panasonic.de/development-hub/pan1781/downloads/) [[4]](#id9) of the [Panasonic Wireless Connectivity Development Hub](https://pideu.panasonic.de/development-hub/) [[2]](#id4).

## Programming and Debugging

Please use the `pan1781_evb` board configuration when
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run).

[[1](#id3)]

[https://industry.panasonic.eu/products/devices/wireless-connectivity/bluetooth-low-energy-modules/pan1781-nrf52820](https://industry.panasonic.eu/products/devices/wireless-connectivity/bluetooth-low-energy-modules/pan1781-nrf52820)

[2]
([1](#id5),[2](#id6))

[https://pideu.panasonic.de/development-hub/](https://pideu.panasonic.de/development-hub/)

[[3](#id8)]

[https://pideu.panasonic.de/development-hub/pan1781/evaluation\_board/user\_guide/](https://pideu.panasonic.de/development-hub/pan1781/evaluation_board/user_guide/)

[[4](#id10)]

[https://pideu.panasonic.de/development-hub/pan1781/downloads/](https://pideu.panasonic.de/development-hub/pan1781/downloads/)
