---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/boostxl_ulpsense/doc/index.html
original_path: boards/shields/boostxl_ulpsense/doc/index.html
---

# BOOSTXL-ULPSENSE: Ultra-low Power Sensor BoosterPack

## Overview

The Ultra-low Power Sensor BoosterPack (BOOSTXL-ULPSENSE) adds analog and
digital sensors to a TI LaunchPad™ development kit. The plug-in module
features inductive flow meter measurement circuits, two capacitive touch
buttons, a light sensor, a reed switch, and an ultra-low power accelerometer.

More information about the board can be found at the
[BOOSTXL\_ULPSENSE website](http://www.ti.com/tool/BOOSTXL-ULPSENSE) [[1]](#id1).

## Requirements

This shield can be used with any TI LaunchPad™ development kit with
BoosterPack connectors.

## Programming

Set `--shield boostxl_ulpsense` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b cc1352r1_launchxl --shield boostxl_ulpsense samples/sensor/accel_polling/
```

## References

[[1](#id2)]

[http://www.ti.com/tool/BOOSTXL-ULPSENSE](http://www.ti.com/tool/BOOSTXL-ULPSENSE)
