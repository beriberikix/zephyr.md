---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/counter/alarm/README.html
original_path: samples/drivers/counter/alarm/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Counter Alarm

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

- [ST Disco L475 IOT01 (B-L475E-IOT01A)](../../../../boards/arm/disco_l475_iot1/doc/index.md#disco-l475-iot1-board)

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
