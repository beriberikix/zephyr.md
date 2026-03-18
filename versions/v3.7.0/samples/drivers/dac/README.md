---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/dac/README.html
original_path: samples/drivers/dac/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Digital-to-Analog Converter (DAC)

## Overview

This sample demonstrates how to use the [DAC driver API](../../../hardware/peripherals/dac.md#dac-api).

## Building and Running

The DAC output is defined in the board’s devicetree and pinmux file.

The board’s [/zephyr,user](../../../build/dts/zephyr-user-node.md#dt-zephyr-user) node must have `dac`,
`dac-channel-id`, and `dac-resolution` properties set. See the predefined
overlays in [samples/drivers/dac/boards](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/dac/boards) for examples.

### Building and Running for ST Nucleo L073RZ

The sample can be built and executed for the
[ST Nucleo L073RZ](../../../boards/st/nucleo_l073rz/doc/index.md#nucleo-l073rz-board) as follows:

```shell
west build -b nucleo_l073rz samples/drivers/dac
west flash
```

### Building and Running for ST Nucleo L152RE

The sample can be built and executed for the
[ST Nucleo L152RE](../../../boards/st/nucleo_l152re/doc/index.md#nucleo-l152re-board) as follows:

```shell
west build -b nucleo_l152re samples/drivers/dac
west flash
```

### Building and Running for ST Nucleo F767ZI

The sample can be built and executed for the
[ST Nucleo F767ZI](../../../boards/st/nucleo_f767zi/doc/index.md#nucleo-f767zi-board) as follows:

```shell
west build -b nucleo_f767zi samples/drivers/dac
west flash
```

### Building and Running for ST Disco F3

The sample can be built and executed for the
[ST STM32F3 Discovery](../../../boards/st/stm32f3_disco/doc/index.md#stm32f3-disco-board) as follows:

```shell
west build -b stm32f3_disco samples/drivers/dac
west flash
```

### Building and Running for ST Nucleo F429ZI

The sample can be built and executed for the
[ST Nucleo F429ZI](../../../boards/st/nucleo_f429zi/doc/index.md#nucleo-f429zi-board) as follows:

```shell
west build -b nucleo_f429zi samples/drivers/dac
west flash
```

### Building and Running for STM32L562E DK

The sample can be built and executed for the
[ST STM32L562E-DK Discovery](../../../boards/st/stm32l562e_dk/doc/index.md#stm32l562e-dk-board) as follows:

```shell
west build -b stm32l562e_dk samples/drivers/dac
west flash
```

### Building and Running for ST Nucleo L552ZE Q

The sample can be built and executed for the
[ST Nucleo L552ZE Q](../../../boards/st/nucleo_l552ze_q/doc/nucleol552ze_q.md#nucleo-l552ze-q-board) as follows:

```shell
west build -b nucleo_l552ze_q samples/drivers/dac
west flash
```

### Building and Running for NXP TWR-KE18F

The sample can be built and executed for the [NXP TWR-KE18F](../../../boards/nxp/twr_ke18f/doc/index.md#twr-ke18f) as
follows:

```shell
west build -b twr_ke18f samples/drivers/dac
west flash
```

DAC output is available on pin A32 of the primary TWR elevator
connector.

### Building and Running for NXP FRDM-K64F

The sample can be built and executed for the [NXP FRDM-K64F](../../../boards/nxp/frdm_k64f/doc/index.md#frdm-k64f) as
follows:

```shell
west build -b frdm_k64f samples/drivers/dac
west flash
```

DAC output is available on connector J4 pin 11.

### Building and Running for BL652

The BL652 DVK PCB contains a footprint for a MCP4725 to use as an external
DAC. Note this is not populated by default. The sample can be built and
executed for the [Ezurio BL652 DVK](../../../boards/ezurio/bl652_dvk/doc/bl652_dvk.md#bl652-dvk) as follows:

```shell
west build -b bl652_dvk samples/drivers/dac
west flash
```

DAC output is available on pin 1 of the MCP4725.

### Building and Running for BL653

The BL653 DVK PCB contains a footprint for a MCP4725 to use as an external
DAC. Note this is not populated by default. The sample can be built and
executed for the [Ezurio BL653 DVK](../../../boards/ezurio/bl653_dvk/doc/bl653_dvk.md#bl653-dvk) as follows:

```shell
west build -b bl653_dvk samples/drivers/dac
west flash
```

DAC output is available on pin 1 of the MCP4725.

### Building and Running for BL654

The BL654 DVK PCB contains a footprint for a MCP4725 to use as an external
DAC. Note this is not populated by default. The sample can be built and
executed for the [Ezurio BL654 DVK](../../../boards/ezurio/bl654_dvk/doc/bl654_dvk.md#bl654-dvk) as follows:

```shell
west build -b bl654_dvk samples/drivers/dac
west flash
```

DAC output is available on pin 1 of the MCP4725.

### Building and Running for BL5340

The BL5340 DVK PCB contains a MCP4725 to use as a DAC. The sample can be
built and executed for the [Ezurio BL5340 DVK](../../../boards/ezurio/bl5340_dvk/doc/index.md#bl5340-dvk) as follows:

```shell
west build -b bl5340_dvk/nrf5340/cpuapp samples/drivers/dac
west flash
```

DAC output is available on pin 1 of the MCP4725.

### Building and Running for GD32450I-EVAL

The sample can be built and executed for the
[GigaDevice GD32F450I-EVAL](../../../boards/gd/gd32f450i_eval/doc/index.md#gd32f450i-eval) as follows:

```shell
west build -b gd32f450i_eval samples/drivers/dac
west flash
```

Bridge the JP23 to DAC with the jumper cap, then DAC output will available on JP7.

### Building and Running for Longan Nano and Longan Nano Lite

The sample can be built and executed for the
[Sipeed Longan Nano](../../../boards/sipeed/longan_nano/doc/index.md#longan-nano) as follows:

```shell
west build -b longan_nano samples/drivers/dac
west flash
```

also can run for the
:ref: longan\_nano\_lite as follows:

```shell
west build -b longan_nano/gd32vf103/lite samples/drivers/dac
west flash
```

### Building and Running for NXP LPCXpresso55S36

The sample can be built and executed for the [NXP LPCXpresso55S36](../../../boards/nxp/lpcxpresso55s36/doc/index.md#lpcxpresso55s36) as
follows:

```shell
west build -b lpcxpresso55s36 samples/drivers/dac
west flash
```

DAC output is available on connector J12 pin 4.

### Sample output

You should see a sawtooth signal with an amplitude of the DAC reference
voltage and a period of approx. 4 seconds at the DAC output pin specified
by the board.

The following output is printed:

```shell
Generating sawtooth signal at DAC channel 1.
```

Note

If the DAC is not supported, the output will be an error message.
