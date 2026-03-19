---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/adc/adc_sequence/README.html
original_path: samples/drivers/adc/adc_sequence/README.html
---

# Analog-to-Digital Converter (ADC) sequence sample

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/adc/adc_sequence/README.rst/..)

## Overview

This sample demonstrates how to use the [ADC driver API](../../../../hardware/peripherals/adc.md#adc-api) using sequences.

Depending on the target board, it reads ADC samples from two channels
and prints the readings on the console, based on the sequence specifications.
Notice how for the whole sequence reading, only one call to the [`adc_read()`](../../../../doxygen/html/group__adc__interface.md#ga7567ce3b03ebb294620b4e32b7561ab3) API is made.
If voltage of the used reference can be obtained, the raw readings are converted to millivolts.

This example constructs an adc device and setups its channels, according to the
given devicetree configuration.

## Building and Running

Make sure that the ADC is enabled (`status = "okay";`) and has each channel as a
child node, with your desired settings like gain, reference, or acquisition time and
oversampling setting (if used). It is also needed to provide an alias `adc0` for the
desired adc. See [boards/nrf52840dk\_nrf52840.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/adc/adc_dt/boards/nrf52840dk_nrf52840.overlay) for an example of
such setup.

### Building and Running for Nordic nRF52840

The sample can be built and executed for the
[nRF52840 DK](../../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) as follows:

```shell
west build -b nrf52840dk/nrf52840 samples/drivers/adc/adc_sequence
west flash
```

To build for another board, change “nrf52840dk/nrf52840” above to that board’s name
and provide a corresponding devicetree overlay.

### Sample output

You should get a similar output as below, repeated every second:

```shell
ADC sequence reading [1]:
- ADC_0, channel 0, 5 sequence samples:
- - 36 = 65mV
- - 35 = 63mV
- - 36 = 65mV
- - 35 = 63mV
- - 36 = 65mV
- ADC_0, channel 1, 5 sequence samples:
- - 0 = 0mV
- - 0 = 0mV
- - 1 = 1mV
- - 0 = 0mV
- - 1 = 1mV
```

Note

If the ADC is not supported, the output will be an error message.

## See also

[ADC driver APIs](../../../../doxygen/html/group__adc__interface.md)
