---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/sm351lt/README.html
original_path: samples/sensor/sm351lt/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SM351LT: Magnetoresistive Sensor Example

## Overview

This sample application periodically polls an SM351LT magnetoresistive sensor
and displays if a magnet near to the sensor, via the console.

## Requirements

This sample uses the Honeywell SM351LT sensor.

## References

For more information about the SM351LT magnetoresistive sensor see
[https://sensing.honeywell.com/SM351LT-low-power](https://sensing.honeywell.com/SM351LT-low-power)

## Building and Running

The SM351LT (or compatible) sensors are available on the following boards:

- [Laird Connectivity Sentrius BT510 Sensor](../../../boards/arm/bt510/doc/bt510.md#bt510)

### Building on bt510

[Laird Connectivity Sentrius BT510 Sensor](../../../boards/arm/bt510/doc/bt510.md#bt510) includes a Honeywell SM351LT magnetoresistive sensor.

```shell
west build -b bt510 samples/sensor/sm351lt
west flash
```

### Sample Output

```shell
Polling at 0.5 Hz
#1 @ 6 ms: 1
#2 @ 2007 ms: 0
#3 @ 4009 ms: 0
#4 @ 6010 ms: 1
#5 @ 8012 ms: 1
```
