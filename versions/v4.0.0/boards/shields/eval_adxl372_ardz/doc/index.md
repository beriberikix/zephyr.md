---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/eval_adxl372_ardz/doc/index.html
original_path: boards/shields/eval_adxl372_ardz/doc/index.html
---

# EVAL-ADXL372-ARDZ

## Overview

The EVAL-ADXL372-ARDZ is a 3-axis digital accelerometer Arduino shield powered
by the Analog Devices ADXL372.

## Programming

Set `--shield eval_adxl372_ardz` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b apard32690/max32690/m4 --shield eval_adxl372_ardz samples/sensor/sensor_shell
```

## Requirements

This shield can only be used with a board which provides a configuration for
Arduino connectors and defines node aliases for SPI and GPIO interfaces (see
[Shields](../../../../hardware/porting/shields.md#shields) for more details).

## References

- [EVAL-ADXL372-ARDZ product page](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adxl372-ardz.html)
- [EVAL-ADXL372-ARDZ user guide](https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029/hardware/adxl372)
- [EVAL-ADXL372-ARDZ schematic](https://www.analog.com/media/en/evaluation-documentation/evaluation-design-files/eval-adxl372-ardz-designsupport.zip)
- [ADXL372 product page](https://www.analog.com/en/products/adxl372.html)
- [ADXL372 data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl372.pdf)
