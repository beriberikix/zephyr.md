---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/clock_control_litex/README.html
original_path: samples/drivers/clock_control_litex/README.html
---

# LiteX clock control driver

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/clock_control_litex/README.rst/..)

## Introduction

This sample is providing an overview of LiteX clock control driver capabilities.
The driver uses Mixed Mode Clock Manager (MMCM) module to generate up to 7 clocks with defined phase, frequency and duty cycle.

## Requirements

- LiteX-capable FPGA platform with MMCM modules (for example Digilent Arty A7 development board)
- SoC configuration with VexRiscv soft CPU and Xilinx 7-series MMCM interface in LiteX (S7MMCM module)
- Optional: clock output signals redirected to output pins for testing

## Configuration

Basic configuration of the driver, including default settings for clock outputs, is held in Device Tree clock control nodes.

```dts
clk0: clock-controller@0 {
	#clock-cells = <1>;
	reg = <0>;
	compatible = "litex,clkout";
	clock-output-names = "CLK_0";
	litex,clock-frequency = <11289600>;
	litex,clock-phase = <0>;
	litex,clock-duty-num = <1>;
	litex,clock-duty-den = <2>;
	litex,clock-margin = <1>;
	litex,clock-margin-exp = <2>;
	status = "disabled";
};
```

```dts
clk1: clock-controller@1 {
	#clock-cells = <1>;
	reg = <1>;
	compatible = "litex,clkout";
	clock-output-names = "CLK_1";
	litex,clock-frequency = <22579200>;
	litex,clock-phase = <0>;
	litex,clock-duty-num = <1>;
	litex,clock-duty-den = <2>;
	litex,clock-margin = <1>;
	litex,clock-margin-exp = <2>;
	status = "disabled";
};
```

```dts
clock0: clock@e0004800 {
	compatible = "litex,clk";
	reg = <0xe0004800 0x4
		0xe0004804 0x4
		0xe0004808 0x4
		0xe000480c 0x4
		0xe0004810 0x4
		0xe0004814 0x4
		0xe0004818 0x4
		0xe000481c 0x4>;
	reg-names = "drp_reset",
		"drp_locked",
		"drp_read",
		"drp_write",
		"drp_drdy",
		"drp_adr",
		"drp_dat_w",
		"drp_dat_r";
	#clock-cells = <1>;
	clocks = <&clk0 0>, <&clk1 1>;
	clock-output-names = "CLK_0", "CLK_1";
	litex,lock-timeout = <10>;
	litex,drdy-timeout = <10>;
	litex,divclk-divide-min = <1>;
	litex,divclk-divide-max = <107>;
	litex,clkfbout-mult-min = <2>;
	litex,clkfbout-mult-max = <65>;
	litex,vco-freq-min = <600000000>;
	litex,vco-freq-max = <1200000000>;
	litex,clkout-divide-min = <1>;
	litex,clkout-divide-max = <126>;
	litex,vco-margin = <0>;
	status = "disabled";
};
```

This configuration defines 2 clock outputs: `clk0` and `clk1` with default frequency set to 100MHz, 0 degrees phase offset and 50% duty cycle. Special care should be taken when defining values for FPGA-specific configuration (parameters from `litex,divclk-divide-min` to `litex,vco-margin`).

**Important note:** `reg` properties in `clk0` and `clk1` nodes reference the clock output number (`clkout_nr`)

## Driver Usage

The driver is interfaced with the [Clock Control API](../../../hardware/peripherals/clock_control.md#clock-control-api) function `clock_control_on()` and a LiteX driver specific structure ([`litex_clk_setup`](../../../doxygen/html/structlitex__clk__setup.md)).

To change clock parameter it is needed to cast a pointer to structure [`litex_clk_setup`](../../../doxygen/html/structlitex__clk__setup.md) onto [`clock_control_subsys_t`](../../../doxygen/html/group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) and use it with [`clock_control_on()`](../../../doxygen/html/group__clock__control__interface.md#gaec69b0989cefad79ffd5c92f060150b9).

This code will try to set on `clk0` frequency 50MHz, 90 degrees of phase offset and 75% duty cycle.

```c
struct device *dev;
int ret;
struct litex_clk_setup setup = {
        .clkout_nr = 0,
        .rate = 50000000,
        .duty = 75,
        .phase = 90
};
dev = DEVICE_DT_GET(MMCM);
clock_control_subsys_t sub_system = (clock_control_subsys_t)&setup;
if ((ret = clock_control_on(dev, sub_system)) != 0) {
        LOG_ERR("Set CLKOUT%d param error!", setup.clkout_nr);
        return ret;
}
```

Clock output status (frequency, duty and phase offset) can be acquired with function `clock_control_get_status()` and clock output frequency only can be queried with `clock_control_get_rate()`

In both getter functions, basic usage is similar to `clock_control_on()`. Structure `litex_clk_setup` is used to set `clkout_nr` of clock output from which data is to be acquired.

## Sample usage

This example provides a simple way of checking various clock output settings. User can pick one of 4 possible scenarios:

- Frequency range,
- Duty cycle range,
- Phase range,
- Setting frequency, duty and phase at once, then check clock status and rate,

Scenarios are selected by defining `LITEX_CLK_TEST` as one of:

- `LITEX_TEST_FREQUENCY`
- `LITEX_TEST_DUTY`
- `LITEX_TEST_PHASE`
- `LITEX_TEST_SINGLE`

Code is performed on 2 clock outputs with `clkout_nr` defined in `LITEX_CLK_TEST_CLK1` and `LITEX_CLK_TEST_CLK2`. Tests are controlled by separate defines for each scenario.

## Building

```text
west build -b litex_vexriscv zephyr/samples/drivers/clock_control
```

Drivers prints a lot of useful debugging information to the log. It is highly recommended to enable logging and synchronous processing of log messages and set log level to `Info`.

## Sample output

```text
[00:00:00.200,000] <inf> CLK_CTRL_LITEX: CLKOUT0: set rate: 100000000 HZ
[00:00:00.240,000] <inf> CLK_CTRL_LITEX: CLKOUT1: updated rate: 100000000 to 100000000 HZ
[00:00:00.280,000] <inf> CLK_CTRL_LITEX: CLKOUT0: set duty: 50%
[00:00:00.320,000] <inf> CLK_CTRL_LITEX: CLKOUT0: set phase: 0 deg
[00:00:00.360,000] <inf> CLK_CTRL_LITEX: CLKOUT1: set rate: 100000000 HZ
[00:00:00.400,000] <inf> CLK_CTRL_LITEX: CLKOUT1: set duty: 50%
[00:00:00.440,000] <inf> CLK_CTRL_LITEX: CLKOUT1: set phase: 0 deg
[00:00:00.440,000] <inf> CLK_CTRL_LITEX: LiteX Clock Control driver initialized
*** Booting Zephyr OS build zephyr-v2.2.0-2810-g1ca5dda196c3  ***
Clock Control Example! riscv32
device name: clock0
clock control device is 0x40013460, name is clock0
Clock test
Single test
[00:00:00.510,000] <inf> CLK_CTRL_LITEX: CLKOUT0: set rate: 15000000 HZ
[00:00:00.550,000] <inf> CLK_CTRL_LITEX: CLKOUT0: set phase: 90 deg
[00:00:00.590,000] <inf> CLK_CTRL_LITEX: CLKOUT0: set duty: 25%
[00:00:00.630,000] <inf> CLK_CTRL_LITEX: CLKOUT1: set rate: 15000000 HZ
[00:00:00.670,000] <inf> CLK_CTRL_LITEX: CLKOUT1: set duty: 75%
Getters test
CLKOUT0: get_status: rate:15000000 phase:90 duty:25
CLKOUT0: get_rate:15000000
CLKOUT1: get_status: rate:15000000 phase:0 duty:75
CLKOUT1: get_rate:15000000
Clock test done returning: 0
```

## References

- [LiteX VexRiscv](../../../boards/enjoydigital/litex_vexriscv/doc/index.md#litex-vexriscv)

## See also

[Clock Control Interface](../../../doxygen/html/group__clock__control__interface.md)
