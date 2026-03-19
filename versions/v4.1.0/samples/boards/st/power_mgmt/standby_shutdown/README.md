---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/boards/st/power_mgmt/standby_shutdown/README.html
original_path: samples/boards/st/power_mgmt/standby_shutdown/README.html
---

# Standby/Shutdown mode

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/power_mgmt/standby_shutdown/README.rst/..)

## Overview

This sample is a minimum application to demonstrate basic power management of Standby mode and
shutdown mode
behavior in a basic blinking LED set up you can enter in shutdown mode or in standbymode mode.
Press and hold the user button:
when LED2 is OFF to enter to Shutdown Mode
when LED2 is ON to enter to Standby Mode
release the user button to exit from shutdown mode or from shutdown mode.

## Requirements

The board should support enabling PM. For a STM32 based target, it means that
it should support a clock source alternative to Cortex Systick that can be used
in core sleep states, as LPTIM ([`st,stm32-lptim`](../../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim)).
For another board than nucleo\_L476RG please adjust wakeup pin into config\_wakeup\_features().

## Building and Running

Build and flash standby\_shutdown as follows, changing `nucleo_L476RG` for your board:

```shell
west build -b nucleo_L476RG samples/boards/st/power_mgmt/standby_shutdown
west flash
```

After flashing, the LED starts to blink.
Press and hold the user button:
when LED2 is OFF to enter to Shutdown Mode
when LED2 is ON to enter to Standby Mode
release the user button to exit from shutdown mode or from shutdown mode.

## PM configurations

By default, [`CONFIG_PM`](../../../../../kconfig.md#CONFIG_PM "CONFIG_PM") is enabled.

## See also

[System power off](../../../../../doxygen/html/group__sys__poweroff.md)

[System](../../../../../doxygen/html/group__subsys__pm__sys.md)
