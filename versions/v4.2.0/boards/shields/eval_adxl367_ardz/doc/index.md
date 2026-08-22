---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/eval_adxl367_ardz/doc/index.html
original_path: boards/shields/eval_adxl367_ardz/doc/index.html
---

# EVAL-ADXL367-ARDZ

## Overview

The EVAL-ADXL367-ARDZ is a 3-axis digital accelerometer Arduino shield powered
by the Analog Devices ADXL367.

## Programming

Set `--shield eval_adxl367_ardz` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b apard32690/max32690/m4 --shield eval_adxl367_ardz samples/sensor/sensor_shell
```

## Requirements

This shield can only be used with a board which provides a configuration for
Arduino connectors and defines node aliases for SPI and GPIO interfaces (see
[Shields](../../../../hardware/porting/shields.md#shields) for more details).

## References

- [ADXL367 product page](https://www.analog.com/en/products/adxl367.html)
- [ADXL367 data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl367.pdf)
