---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/counter/alarm/README.html
original_path: samples/drivers/counter/alarm/README.html
---

# Counter Alarm

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/counter/alarm/README.rst/..)

## Overview

This sample provides an example of alarm application using [counter API](../../../../hardware/peripherals/counter.md#counter-api).
It sets an alarm with an initial delay of 2 seconds. At each alarm
expiry, a new alarm is configured with a delay multiplied by 2.

Note

In case of 1Hz frequency (RTC for example), precision is 1 second.
Therefore, the sample output may differ in 1 second

## Requirements

This sample requires the support of a timer IP compatible with alarm setting.

## References

- [Disco L475 IOT01 (B-L475E-IOT01A)](../../../../boards/st/disco_l475_iot1/doc/index.md#disco_l475_iot1)

## Building and Running

> ```shell
> west build -b disco_l475_iot1 samples/drivers/counter/alarm
> west build -t run
> ```

### Sample Output

> ```shell
> Counter alarm sample
>
> Set alarm in 2 sec
> !!! Alarm !!!
> Now: 2
> Set alarm in 4 sec
> !!! Alarm !!!
> Now: 6
> Set alarm in 8 sec
> !!! Alarm !!!
> Now: 14
> Set alarm in 16 sec
> !!! Alarm !!!
> Now: 30
>
> <repeats endlessly>
> ```

## See also

[Counter Interface](../../../../doxygen/html/group__counter__interface.md)
