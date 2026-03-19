---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/vcnl4040/README.html
original_path: samples/sensor/vcnl4040/README.html
---

# VCNL4040 Proximity and Ambient Light Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/vcnl4040/README.rst/..)

## Overview

> This sample periodically measures proximity and light for
> 5 sec in the interval of 300msec in polling mode. Then threshold trigger mode
> is enabled with the high threshold value of 127 and data is fetched based
> on interrupt. The result is displayed on the console.

## Requirements

> This sample uses the VCNL4040 sensor controlled using the I2C interface.
> Connect sensor INT for interrupt to Feather D5 pin on the Adafruit STM32F405 Feather.

## References

> - VCNL4040: [https://www.vishay.com/docs/84274/vcnl4040.pdf](https://www.vishay.com/docs/84274/vcnl4040.pdf)

## Building and Running

> This project outputs sensor data to the console. It requires a VCNL4040
> sensor to be connected to the desired board.
>
> ```shell
> # From the root of the zephyr repository
> west build -b None samples/sensor/vcnl4040/
> west flash
> ```

### Sample Output

> ```shell
> get device vcnl4040
> Testing the polling mode.
> Proximity: 31
> Light (lux): 288
>
> <repeats for 5sec every 300ms>
>
> Polling mode test finished.
> Testing the trigger mode.
> Testing proximity trigger.
> ...
> Triggered.
> Proximity: 122
>
> <repeats whenever triggered for 5sec>
>
> Threshold trigger test finished.
> Trigger mode test finished.
> ```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
