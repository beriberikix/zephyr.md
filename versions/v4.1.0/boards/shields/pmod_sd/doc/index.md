---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/pmod_sd/doc/index.html
original_path: boards/shields/pmod_sd/doc/index.html
---

# Digilent Pmod SD

## Overview

The Digilent Pmod SD (Revision B) allows system boards to read from and write to SD cards.

## Features

- Full-sized SD card slot
- Store and access large amounts of date from your system board
- No limitation on file system or memory size of SD card used
- 1-bit and 4-bit communication
- 12-pin Pmod port with SPI interface

## Programming

Set `--shield pmod_sd` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b ek_ra8m1 --shield pmod_sd tests/drivers/disk/disk_access
```

### Pinout

![PMOD SD Pinout](../../../../_images/pmod_sd_pins.webp)

PMOD SD Pinout (Credit: Digilent)

## References

- [Pmod SD product page](https://digilent.com/shop/pmod-sd-full-sized-sd-card-slot/)
- [Pmod SD reference manual](https://digilent.com/reference/pmod/pmodsd/reference-manual)
- [Pmod SD schematic](https://digilent.com/reference/_media/reference/pmod/pmodsd/pmodsd_sch.pdf)
