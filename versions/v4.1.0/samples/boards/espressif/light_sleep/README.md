---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/boards/espressif/light_sleep/README.html
original_path: samples/boards/espressif/light_sleep/README.html
---

# Light Sleep

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/espressif/light_sleep/README.rst/..)

## Overview

This example illustrates usage of light sleep mode. Unlike deep sleep mode,
light sleep preserves the state of the memory, CPU, and peripherals. Execution
of code on both CPUs is stopped when `esp_light_sleep_start()` function is called.
When the chip exits light sleep mode, execution continues at the point where it
was stopped, and `esp_light_sleep_start()` function returns.

The example enables the following wakeup sources:

- `Timer`: wake up the chip in 2 seconds.
- `EXT0`: wake up the chip if a button attached to GPIO0 is pressed (i.e. if
  GPIO0 goes low).

## Requirements

This example can be used with any ESP32 development board. Most boards have a
button attached to GPIO0, often labelled BOOT. If the board does not have such
button, an external button can be connected, along with a 10k pull-up resistor,
and a 100nF capacitor to ground for debouncing.

## Building, Flashing and Running

```shell
west build -b esp32_devkitc_wroom/esp32/procpu samples/boards/espressif/light_sleep
west flash
```

### Sample Output

#### ESP32 core output

In the scenario below, the button attached to GPIO0 was pressed and held for
about 500 ms, after the second wakeup from light sleep. The program has
indicated the wakeup reason after each sleep iteration.

```shell
*** Booting Zephyr OS build zephyr-v3.1.0-3667-gb42e2b225ecf  ***

Entering light sleep
Returned from light sleep, reason: timer, t=3344 ms, slept for 2001 ms
Entering light sleep
Returned from light sleep, reason: timer, t=5354 ms, slept for 2000 ms
Entering light sleep
Returned from light sleep, reason: pin, t=5885 ms, slept for 521 ms
Waiting for GPIO0 to go high...
Entering light sleep
Returned from light sleep, reason: timer, t=8765 ms, slept for 2000 ms
Entering light sleep
Returned from light sleep, reason: timer, t=10776 ms, slept for 2001 ms
Entering light sleep
```

## Troubleshooting

If pressing the button attached to GPIO0 does not affect program behavior,
check DTR/RTS configuration in the serial monitor. This is not necessary for
IDF monitor, but for other tools it might be necessary to set DTR and RTS line
state to “disabled” or “de-asserted”.
