---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/adc/adc_dt/README.html
original_path: samples/drivers/adc/adc_dt/README.html
---

# Analog-to-Digital Converter (ADC) with devicetree

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/adc/adc_dt/README.rst/..)

## Overview

This sample demonstrates how to use the [ADC driver API](../../../../hardware/peripherals/adc.md#adc-api).

Depending on the target board, it reads ADC samples from one or more channels
and prints the readings on the console. If voltage of the used reference can
be obtained, the raw readings are converted to millivolts.

The pins of the ADC channels are board-specific. Please refer to the board
or MCU datasheet for further details.

## Building and Running

The ADC peripheral and pinmux is configured in the board’s `.dts` file. Make
sure that the ADC is enabled (`status = "okay";`).

In addition to that, this sample requires an ADC channel specified in the
`io-channels` property of the `zephyr,user` node. This is usually done with
a devicetree overlay. The example overlay in the `boards` subdirectory for
the `nucleo_l073rz` board can be easily adjusted for other boards.

Configuration of channels (settings like gain, reference, or acquisition time)
also needs to be specified in devicetree, in ADC controller child nodes. Also
the ADC resolution and oversampling setting (if used) need to be specified
there. See [boards/nrf52840dk\_nrf52840.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/adc/adc_dt/boards/nrf52840dk_nrf52840.overlay) for an example of
such setup.

### Building and Running for ST Nucleo L073RZ

The sample can be built and executed for the
[Nucleo L073RZ](../../../../boards/st/nucleo_l073rz/doc/index.md#nucleo_l073rz) as follows:

```shell
west build -b nucleo_l073rz samples/drivers/adc/adc_dt
west flash
```

To build for another board, change “nucleo\_l073rz” above to that board’s name
and provide a corresponding devicetree overlay.

### Sample output

You should get a similar output as below, repeated every second:

```shell
ADC reading:
- ADC_0, channel 7: 36 = 65mV
```

Note

If the ADC is not supported, the output will be an error message.

## See also

[ADC driver APIs](../../../../doxygen/html/group__adc__interface.md)
