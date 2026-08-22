---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/rtklcdpar1s00001be/doc/index.html
original_path: boards/shields/rtklcdpar1s00001be/doc/index.html
---

# RTKLCDPAR1S00001BE Display

## Overview

The Graphics Expansion Board includes a 1024x600 pixel TFT color LCD with a
capacitive touch overlay.

This display uses a 40-pin connector header.

### Pins Assignment of the Renesas RTKLCDPAR1S00001BE Display

| Connector Pin | Function |
| --- | --- |
| 1 | Display backlight enable |
| 2 | Touch ctrl I2C SDA |
| 3 | External interrupt |
| 4 | Touch ctrl I2C SCL |
| 6 | Display reset |

## Hardware Requirements:

Supported Renesas RA boards: EK-RA8P1

- 1 x RA Board
- 1 x Micro USB cable

## Programming

Set `--shield=rtklcdpar1s00001be` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b ek_ra8p1/r7ka8p1kflcac/cm85 --shield rtklcdpar1s00001be tests/drivers/display/display_read_write
```
