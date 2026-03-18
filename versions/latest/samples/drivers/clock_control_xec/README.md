---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/clock_control_xec/README.html
original_path: samples/drivers/clock_control_xec/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Microchip XEC (MEC15xx/MEC172x) clock control driver sample application

## Overview

This sample demonstrates configuring the 32KHz clock
options via device tree. The application prints out
hardware configuration and exercises some clock control
driver API’s.

## Building and Running

The sample can be built and executed on boards using west.
No pins configurations, except GPIO014 is used as indicator for entry/exit and
GPIO060 for 48MHZ PLL clock out.
GPIO221 alternate function 1 is 32KHZ\_OUT and can be monitored on Assembly 6915 JP7 pin 5.

Internal Silicon 32KHz Oscillator jumper configuration
MEC172x Assembly 6915

> JP1 pin 2 to GND (ground MEC172x XTAL1 pin)
> JP2 No jumper

Dual-ended 32KHz Crystal jumper configuration
MEC172x Assembly 6915

> Jumper on JP1 1-2 connect crystal Y1 pin 1 to MEC172x XTAL1
> Jumper on JP2 2-3 connect crystal Y1 pin 2 to MEC172x XTAL2

MEC172x Assembly 6906 (baseboard)

> Remove jumper on JP121 to prevent U15 32KHz 50% duty waveform
> from coupling to JP2 on Assembly 6915.

External single-ended 32KHz waveform to MEC172x XTAL2 input
MEC172x Assembly 6915

> JP1 pin 2 to GND (ground MEC172x XTAL1 pin)
> Jumper on JP2 1-2 connect external 32KHz signal to XTAL2

MEC172x Assembly 6906 (baseboard)

> Jumper on JP121 pins 3-4 connect U15 32KHz output to
> XTAL2\_32KHZ\_IN signal routed to XTAL2 MEC172x pin on Assembly 6915

External single-ended 32KHz waveform to MEC172x 32KHZ\_IN pin
MEC172x Assembly 6915

> JP1 pin 2 to GND (ground MEC172x XTAL1 pin)
> Remove jumper on JP2

MEC172x Assembly 6906 (baseboard)

> Jumper on JP121 pins 1-2 connect U15 32KHz output to
> 32KHZ\_IN pin of MEC172x on Assembly 6915

### Sample output

```shell
Prints MEC172x VBAT and PCR register pertaining to power on status and
clock control.
```
