---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/boards/st/mco/README.html
original_path: samples/boards/st/mco/README.html
---

# Master Clock Output (MCO)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/mco/README.rst/..)

## Overview

This sample is a minimum application to demonstrate how to output one of the internal clocks for
external use by the application.

## Requirements

The SoC should support MCO functionality and use a pin that has the MCO alternate function.
To support another board, add a dts overlay file in boards folder.
Make sure that the output clock is enabled in dts overlay file.
Depending on the stm32 serie, several clock source and prescaler are possible for each MCOx.
The clock source is set by the DTS among the possible values for each stm32 serie.
The prescaler is set by the DTS, through the property `prescaler = <MCOx_PRE(MCO_PRE_DIV_n)>;`

See [dts/bindings/clock/st,stm32-clock-mco.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/clock/st,stm32-clock-mco.yaml)

It is required to check the Reference Manual to configure the DTS correctly.

## Building and Running

```shell
# From the root of the zephyr repository
west build -b nucleo_u5a5zj_q samples/boards/st/mco
west flash
```

After flashing, the LSE clock will be output on the MCO pin enabled in Device Tree.
The clock can be observed using a probing device, such as a logic analyzer.

## See also

[Pin Controller Interface](../../../../doxygen/html/group__pinctrl__interface.md)
