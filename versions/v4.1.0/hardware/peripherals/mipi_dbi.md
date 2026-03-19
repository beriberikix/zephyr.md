---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/mipi_dbi.html
original_path: hardware/peripherals/mipi_dbi.html
---

# MIPI Display Bus Interface (DBI)

The MIPI DBI driver class implements support for MIPI DBI compliant display
controllers.

MIPI DBI defines 3 interface types:

- Type A: Motorola 6800 parallel bus
- Type B: Intel 8080 parallel bus
- Type C: SPI Type serial bit bus with 3 options:

  1. 9 write clocks per byte, final bit is command/data selection bit
  2. Same as above, but 16 write clocks per byte
  3. 8 write clocks per byte. Command/data selected via GPIO pin

Currently, the API does not support Type C controllers with 16 write clocks
(option 2).

## API Reference

[MIPI-DBI driver APIs](../../doxygen/html/group__mipi__dbi__interface.md)
