---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/m5stack_core2_ext/doc/index.html
original_path: boards/shields/m5stack_core2_ext/doc/index.html
---

# M5Stack-Core2 base shield

## Overview

[M5Stack-Core2](https://docs.m5stack.com/en/core/core2) [[1]](#id2) comes with a base shield that is connected to the M5Stack
extension connector. It features an MPU6886 6-axis motion tracker (6DOF IMU)
and a SPM1423 microphone.

[![M5Stack-Core2-EXT](../../../../_images/m5stack_core2_ext.webp)
](../../../../_images/m5stack_core2_ext.webp)

M5Stack-Core2-Extension module

Note

The SPM1423 microphone functionality is not implemented yet.

### Pins Assignments

| Shield Connector Pin | Function |
| --- | --- |
| 0 | GND |
| 11 | 3.3V |
| 16 | I2C - intSDA |
| 17 | I2C - intSCL |

## Programming

Set `--shield m5stack_core2_ext` when you invoke `west build`.
For example:

```shell
# From the root of the zephyr repository
west build -b m5stack_core2/esp32/procpu --shield m5stack_core2_ext samples/sensor/mpu6050
```

## References

[[1](#id3)]

[https://docs.m5stack.com/en/core/core2](https://docs.m5stack.com/en/core/core2)
