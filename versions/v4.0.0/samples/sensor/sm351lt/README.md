---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/sm351lt/README.html
original_path: samples/sensor/sm351lt/README.html
---

# SM351LT Magnetoresistive Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/sm351lt/README.rst/..)

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

- [Sentrius BT510 Sensor](../../../boards/ezurio/bt510/doc/bt510.md#bt510)

### Building on bt510

[Sentrius BT510 Sensor](../../../boards/ezurio/bt510/doc/bt510.md#bt510) includes a Honeywell SM351LT magnetoresistive sensor.

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

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
