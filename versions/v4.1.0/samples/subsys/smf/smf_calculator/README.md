---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/smf/smf_calculator/README.html
original_path: samples/subsys/smf/smf_calculator/README.html
---

# SMF Calculator

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/smf/smf_calculator/README.rst/..)

## Overview

This sample creates a basic desk calculator driven by a state machine written
with the [State Machine Framework](../../../../services/smf/index.md#smf).

The ‘business logic’ of the calculator is based on the statechart given in
Fig 2.18 of *Practical UML Statecharts in C/C++* 2nd Edition by Miro Samek.
This uses a three-layer hierarchical statechart to handle situations such as
ignoring leading zeroes, and disallowing multiple decimal points.

The statechart has been slightly modified to display different output on the
screen in the `op_entered` state depending on if a previous result is
available or not.

![SMF Calculator Statechart](../../../../_images/smf_calculator.svg)

Statechart for the SMF Calculator business logic.

The graphical interface uses an LVGL button matrix for input and text label for
output, based on the sample in samples/drivers/display. The state machine updates
the output text label after every call to [`smf_run_state()`](../../../../doxygen/html/group__smf.md#ga8399cfa9e793a7f188b4ed4fec9f4f90).

[`CONFIG_LV_Z_VDB_SIZE`](../../../../kconfig.md#CONFIG_LV_Z_VDB_SIZE "CONFIG_LV_Z_VDB_SIZE") has been reduced to 14% to allow it to run
on RAM-constrained boards like the [Disco L475 IOT01 (B-L475E-IOT01A)](../../../../boards/st/disco_l475_iot1/doc/index.md#disco_l475_iot1).

## Requirements

The GUI should work with any touchscreen display supported by Zephyr. The shield
must be passed to `west build` using the `--shield` option, e.g.
`--shield adafruit_2_8_tft_touch_v2`

List of Arduino-based touchscreen shields:

- [Adafruit 2.8” TFT Touch Shield v2](../../../../boards/shields/adafruit_2_8_tft_touch_v2/doc/index.md#adafruit-2-8-tft-touch-v2)
- [Buydisplay 2.8” TFT Touch Shield with Arduino adapter](../../../../boards/shields/buydisplay_2_8_tft_touch_arduino/doc/index.md#buydisplay-2-8-tft-touch-arduino)
- [Buydisplay 3.5” TFT Touch Shield with Arduino adapter](../../../../boards/shields/buydisplay_3_5_tft_touch_arduino/doc/index.md#buydisplay-3-5-tft-touch-arduino)

The demo should also work on STM32 Discovery Kits with built-in touchscreens e.g.

- [STM32F412G Discovery](../../../../boards/st/stm32f412g_disco/doc/index.md#stm32f412g_disco)
- [ST25DV Discovery, MB1283 version](../../../../boards/st/st25dv_mb1283_disco/doc/index.md#st25dv_mb1283_disco)
- [STM32F7508-DK Discovery Kit](../../../../boards/st/stm32f7508_dk/doc/index.md#stm32f7508_dk)
- [STM32F769I Discovery](../../../../boards/st/stm32f769i_disco/doc/index.md#stm32f769i_disco)

etc. These will not need a shield defined as the touchscreen is built-in.

## Building and Running

Below is an example on how to build for a [Disco L475 IOT01 (B-L475E-IOT01A)](../../../../boards/st/disco_l475_iot1/doc/index.md#disco_l475_iot1) board with
a [Adafruit 2.8” TFT Touch Shield v2](../../../../boards/shields/adafruit_2_8_tft_touch_v2/doc/index.md#adafruit-2-8-tft-touch-v2).

```shell
west build -b disco_l475_iot1 --shield adafruit_2_8_tft_touch_v2 samples/subsys/smf/smf_calculator
```

For testing purpose without the need of any hardware, the [native\_sim](../../../../boards/native/native_sim/doc/index.md#native-sim)
board is also supported and can be built as follows;

```shell
west build -b native_sim samples/subsys/smf/smf_calculator
```

### CLI control

As well as control through the GUI, the calculator can be controlled through the shell,
demonstrating a state machine can receive inputs from multiple sources.
The `key <key>` command sends a keypress to the state machine. Valid keys are
`0` through `9` for numbers, `.`, `+`, `-`, `*`, `/` and `=` to
perform the expected function, `C` for Cancel, and `E` for Cancel Entry.

GUI update speed on the [Disco L475 IOT01 (B-L475E-IOT01A)](../../../../boards/st/disco_l475_iot1/doc/index.md#disco_l475_iot1) with [Adafruit 2.8” TFT Touch Shield v2](../../../../boards/shields/adafruit_2_8_tft_touch_v2/doc/index.md#adafruit-2-8-tft-touch-v2)
touchscreen is of the order of 0.8s due to button matrices invalidating the entire
matrix area when pressed, rather than just the button that was selected. This could
be sped up by using 18 individual buttons rather than a single matrix, but is sufficient
for this demo.

## References

*Practical UML Statecharts in C/C++* 2nd Edition by Miro Samek
[https://www.state-machine.com/psicc2](https://www.state-machine.com/psicc2)

## See also

[State Machine Framework API](../../../../doxygen/html/group__smf.md)
