---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/rtc/README.html
original_path: samples/drivers/rtc/README.html
---

# Real-Time Clock (RTC)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/rtc/README.rst/..)

## Overview

This sample shows how to use the [rtc driver API](../../../hardware/peripherals/rtc.md#rtc-api)
to set and read the date/time from RTC and display on the console
and can be built and executed on boards supporting RTC.

## Building and Running

Build and flash as follows, replacing `stm32f3_disco` with your board:

```shell
west build -b stm32f3_disco samples/drivers/rtc
west flash
```

### Sample Output

```shell
RTC date and time: 2024-11-17 04:19:00
RTC date and time: 2024-11-17 04:19:01

<repeats endlessly>
```

## See also

[RTC Interface](../../../doxygen/html/group__rtc__interface.md)
