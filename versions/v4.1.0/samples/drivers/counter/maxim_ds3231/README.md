---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/counter/maxim_ds3231/README.html
original_path: samples/drivers/counter/maxim_ds3231/README.html
---

# DS3231 TCXO RTC

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/counter/maxim_ds3231/README.rst/..)

## Overview

The [DS3231](https://www.maximintegrated.com/en/products/analog/real-time-clocks/DS3231.html) temperature-compensated real-time clock is a
high-precision (2 ppm) battery backed clock that maintains civil time
and supports alarms. The [Chronodot](https://www.adafruit.com/product/255) breakout board can be used to
test it.

## Annotated Example Output

The sample first displays the boot banner, board name and
frequency of the local clock used for synchronization, and whether the
DS3231 has recorded a loss-of-oscillator:

```text
***** Booting Zephyr OS build zephyr-v1.14.0-2409-g322d53aedaa0 *****
DS3231 on particle_xenon syncclock 1000 Hz
.
DS3231 has not experienced an oscillator fault
```

Next, information about the device as a counter is displayed. The
counter value is read, and its value formatted as the date, time, day of
week, and day of year (19 July 2019 is a Friday, and is the 200th day of
2019):

```text
Counter at 0x20001a58
        Max top value: 4294967295 (ffffffff)
        2 channels
        1 Hz
Top counter value: 4294967295 (ffffffff)
Now 1563512509: 2019-07-19 05:01:49 Fri 200
```

The DS3231 control and status register values are displayed:

```text
DS3231 ctrl 04 ; ctrl_stat 08
```

Next, if the sample application option `CONFIG_APP_SET_ALIGNED_CLOCK`
is set, the civil time will be advanced to the start of the next hour,
and the clock will be set to align that time with the time of the boot,
which in the output below is 34 ms in the past. The time required to
synchronize the clock is 967 ms, and the whole second value of one
second past the hour is written at 1000 ms local uptime:

```text
Set 2019-07-19 06:00:00.034000000 Fri 200 at 34 ms past: 0
Synchronize final: 0 0 in 967 ms
wrote sync 0: 1563516001 0 at 1000
```

Then a synchronization point is read. This takes 894 ms (it must align
to an RTC one-second rollover):

```text
Synchronize init: 0
Synchronize complete in 894 ms: 0 0
.
read sync 0: 1563516002 0 at 2000
```

The alarm configuration is read from non-volatile memory and displayed.
See the `maxim_ds3231.h` for interpretation of the integer value and
flags:

```text
Alarm 1 flags 0 at 254034017: 0
Alarm 2 flags e at 252374400: 0
```

Five seconds is added to the current time and the civil time
representation displayed. The second-resolution alarm is configured to
fire at that time on the current day-of-week. The minute-resolution
alarm is configured to fire once per minute:

```text
Min Sec base time: 2019-07-19 06:00:07 Fri 200
Set sec alarm 90 at 1563516007 ~ 2019-07-19 06:00:07 Fri 200: 5
Set min alarm flags f at 1563516007 ~ 2019-07-19 06:00:07 Fri 200: 7
```

We’re now 2.131 ms into the run, at which point the alarms are read back
and displayed. Alarms do not include date but can include day-of-week
or day-of-month; the date is selected to preserve that information:

```text
2131 ms in: get alarms: 0 0
Sec alarm flags 10 at 252914407 ~ 1978-01-06 06:00:07 Fri 006
Min alarm flags e at 252374400 ~ 1977-12-31 00:00:00 Sat 365
```

The second-resolution alarm was signalled, and processed by the
application at 7.002 s into the run, as scheduled (plus callback
latency). The callback uses the counter alarm API to schedule a second
alarm in 10 seconds:

```text
Sec signaled at 7002 ms, param 0x20000048, delay 1; set 7
```

The counter API callback is called at the correct time:

```text
Counter callback at 17001 ms, id 0, ticks 1563516017, ud 0x20000048
```

From here on the sample sleeps except when the minute-resolution alarm
fires, at which point it displays the RTC time; the
nanosecond-resolution offset in seconds between the RTC time and the
local time; the local time from `k_uptime_get()`; and the aggregate
error between local and RTC time measured in parts-per-million:

```text
2019-07-19 06:01:00 Fri 200: adj 0.002000000, uptime 0:01:00.002, clk err 34 ppm
2019-07-19 06:02:00 Fri 200: adj 0.003000000, uptime 0:02:00.004, clk err 25 ppm
2019-07-19 06:03:00 Fri 200: adj 0.005000000, uptime 0:03:00.005, clk err 28 ppm
2019-07-19 06:04:00 Fri 200: adj 0.006000000, uptime 0:04:00.007, clk err 25 ppm
2019-07-19 06:05:00 Fri 200: adj 0.008000000, uptime 0:05:00.008, clk err 26 ppm
```

The output shows that the Zephyr system clock is running about 25 ppm
faster than civil time on this device. This amount of error is expected
for this target as the system time derives from a crystal oscillator
with a similar accuracy.

## Building and Running

Wire a Chronodot to one of the supported boards as specified in the
corresponding devicetree overlay.

- Particle Xenon

  ```shell
  west build -b particle-xenon samples/drivers/counter/maxim_ds3231
  ```
- NXP Freedom K64F

  ```shell
  west build -b frdm_k64f samples/drivers/counter/maxim_ds3231
  ```
- ST Nucleo L476RG

  ```shell
  west build -b nucleo_l476rg samples/drivers/counter/maxim_ds3231
  ```
- EFR32 Mighty Gecko Thunderboard Sense 2

  ```shell
  west build -b sltb004a samples/drivers/counter/maxim_ds3231
  ```

## See also

[Counter Interface](../../../../doxygen/html/group__counter__interface.md)
