---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/eval_ad4052_ardz/doc/index.html
original_path: boards/shields/eval_ad4052_ardz/doc/index.html
---

# EVAL-AD4052-ARDZ

## Overview

The EVAL-AD4052-ARDZ is a 16-Bit SAR ADC Arduino shield powered
by the Analog Devices AD4052.

## Programming

Set `--shield eval_ad4052_ardz` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b apard32690/max32690/m4 --shield eval_ad4052_ardz samples/drivers/adc/
```

## Requirements

This shield can only be used with a board which provides a configuration for
Arduino connectors and defines node aliases for SPI and GPIO interfaces (see
[Shields](../../../../hardware/porting/shields.md#shields) for more details).

## References

- [EVAL-AD4052-ARDZ product page](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad4052-ardz.html#eb-overview)
- [EVAL-AD4052-ARDZ user guide](https://www.analog.com/media/en/technical-documentation/user-guides/eval-ad4050-ad4052-ug-2222.pdf)
- [EVAL-AD4052-ARDZ schematic](https://www.analog.com/media/en/evaluation-documentation/evaluation-design-files/eval-ad4052-ardz-designsupport-files.zip)
- [AD4052 product page](https://www.analog.com/en/products/ad4052.html)
- [AD4052 data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ad4052-ad4058.pdf)
