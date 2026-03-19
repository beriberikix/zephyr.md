---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/eval_adxl362_ardz/doc/index.html
original_path: boards/shields/eval_adxl362_ardz/doc/index.html
---

# EVAL-ADXL362-ARDZ

## Overview

The EVAL-ADXL362-ARDZ is a 3-axis digital accelerometer Arduino shield powered
by the Analog Devices ADXL362.

## Programming

Set `--shield eval_adxl362_ardz` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b apard32690/max32690/m4 --shield eval_adxl362_ardz samples/sensor/sensor_shell
```

## Requirements

This shield can only be used with a board which provides a configuration for
Arduino connectors and defines node aliases for SPI and GPIO interfaces (see
[Shields](../../../../hardware/porting/shields.md#shields) for more details).

## References

- [EVAL-ADXL362-ARDZ product page](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adxl362-ardz.html)
- [EVAL-ADXL362-ARDZ user guide](https://wiki.analog.com/resources/eval/user-guides/eval-adicup360/hardware/adxl362)
- [EVAL-ADXL362-ARDZ schematic](https://www.analog.com/media/en/reference-design-documentation/design-integration-files/eval-adxl362-ardz-designsupport.zip)
- [ADXL362 product page](https://www.analog.com/en/products/adxl362.html)
- [ADXL362 data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl362.pdf)
