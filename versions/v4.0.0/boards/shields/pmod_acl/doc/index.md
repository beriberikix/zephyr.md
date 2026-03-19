---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/pmod_acl/doc/index.html
original_path: boards/shields/pmod_acl/doc/index.html
---

# Digilent Pmod ACL

## Overview

The Digilent Pmod ACL is a 3-axis digital accelerometer module powered by the
Analog Devices ADXL345.

## Programming

Set `--shield pmod_acl` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b apard32690/max32690/m4 --shield pmod_acl samples/sensor/sensor_shell
```

## Requirements

This shield can only be used with a board which provides a configuration
for Pmod connectors and defines node aliases for SPI and GPIO interfaces
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## References

- [Pmod ACL product page](https://digilent.com/shop/pmod-acl-3-axis-accelerometer/)
- [Pmod ACL reference manual](https://digilent.com/reference/pmod/pmodacl/reference-manual)
- [Pmod ACL schematic](https://digilent.com/reference/_media/reference/pmod/pmodacl/pmodacl_sch.pdf)
- [ADXL345 product page](https://www.analog.com/en/products/adxl345.html)
- [ADXL345 data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl345.pdf)
