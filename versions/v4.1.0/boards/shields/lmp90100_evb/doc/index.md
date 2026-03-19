---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/lmp90100_evb/doc/index.html
original_path: boards/shields/lmp90100_evb/doc/index.html
---

# LMP90100 Sensor AFE Evaluation Board

## Overview

The Texas Instruments LMP90100 Sensor AFE Evaluation Board (EVB) is a
development kit for the TI LMP90xxx series of analog sensor frontends.

![LMP90100 EVB](../../../../_images/lmp90100eb_lmp90100eb.jpg)

LMP90100 EVB (Credit: Texas Instruments)

## Requirements

This shield can only be used with a development board that provides a
configuration for Arduino connectors and defines a node alias for the
SPI interface (see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

The SPIO connector pins on the LMP90100 EVB can be connected to the
Arduino headers of the development board using jumper wires.

For more information about interfacing the LMP90xxx series and the
LMP90100 EVB in particular, see these TI documents:

- [LMP90100 Sensor AFE Evaluation Board User’s Guide](https://www.farnell.com/datasheets/1604987.pdf)
- [LMP90100 Multi-Channel, Low Power 24-Bit Sensor AFE](http://www.ti.com/product/LMP90100)

## Samples

Zephyr RTOS includes one sample targeting the LMP90100 EVB:

- [LMP90100 Sensor AFE Evaluation Board: RTD Sample](../../../../samples/shields/lmp90100_evb/rtd/README.md#lmp90100-evb-rtd-sample)

## Programming

Set `--shield lmp90100_evb` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b frdm_k64f --shield lmp90100_evb samples/shields/lmp90100_evb/rtd
```
