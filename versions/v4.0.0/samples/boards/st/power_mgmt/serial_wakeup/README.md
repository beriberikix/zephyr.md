---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/boards/st/power_mgmt/serial_wakeup/README.html
original_path: samples/boards/st/power_mgmt/serial_wakeup/README.html
---

# Serial wakeup

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/power_mgmt/serial_wakeup/README.rst/..)

## Overview

This sample is a minimum application to demonstrate serial wakeup functionality
in low power context.

## Requirements

1. The board should support enabling PM. For a STM32 based target, it means that
it should support a clock source alternative to Cortex Systick that can be used
in core sleep states, as LPTIM ([`st,stm32-lptim`](../../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim)).

2. The serial port used by the shell should be configured, using device tree, to
be a functional wakeup source:

> - Clocked by an oscillator available in Stop mode (LSE, LSI) or an oscillator capable
>   that can be requested dynamically by device on activity detection (HSI on STM32WB).
> - Matching oscillator sources should be enabled
> - If LSE is selected as clock source and shell serial port is a LPUART current speed
>   should be adapted (9600 bauds)
> - Port should be set as “wakeup-source”

Note: Using HSI clock is a specific

## Building and Running

Build and flash this sample as follows, changing `nucleo_wb55rg` for a board
configured to be compatible with this sample.

```shell
west build -b nucleo_wb55rg samples/boards/st/power_mgmt/serial_wakeup
west flash
```

After flashing, the shell is enabled and device enter sleep mode.
User is able to wake up the device by typing into the shell

## PM configurations

By default, [`CONFIG_PM_DEVICE`](../../../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") and [`CONFIG_PM_DEVICE_RUNTIME`](../../../../../kconfig.md#CONFIG_PM_DEVICE_RUNTIME "CONFIG_PM_DEVICE_RUNTIME")
are enabled, but user can also deactivate both or former to see each configuration in play.

## Debugging

[`CONFIG_DEBUG`](../../../../../kconfig.md#CONFIG_DEBUG "CONFIG_DEBUG") could be enabled to allow debug. Note that debug mode prevents
target to reach low power consumption.
Also note that after debug mode has been disabled, target should also be powered off in order
to get back to normal mode and reach low power consumption.

## PM measurements on stm32l562e\_dk using stm32l562e\_dk PM shield

Plug Power shield
Plug ST-Link
Set JP4 To 5V ST-Link
Set SW1 to PM\_SEL\_VDD
STM32Cube PowerMonitor settings to be applied:

> - Sampling Freq: max
> - Functional Mode: High

## Optimal configuration for low power consumption

In order to reach lower power consumption numbers following parameters should be taken
into account:

> > - Use a LPUART instead of a basic U(S)ART node
> > - Chose LSE as clock source
> > - Ensure no other oscillators are enabled (disable HSI, …)
> > - Provide “sleep” pinctrl configuration to other uart nodes.
> > - Disable Debug mode
>
> With all these conditions matched, one can reach 10uA on stm32l562e\_dk with this sample.

## See also

[Device](../../../../../doxygen/html/group__subsys__pm__device.md)
