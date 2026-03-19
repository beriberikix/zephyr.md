---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/abrobot_esp32c3_oled/doc/index.html
original_path: boards/shields/abrobot_esp32c3_oled/doc/index.html
---

# Abrobot ESP32 C3 OLED Shield

## Overview

![Abrobot ESP32 C3 OLED Shield](../../../../_images/abrobot_esp32c3_oled.webp)

Abrobot esp32c3 oled only works with sh1106\_compatible display driver. It does not support 1306 display driver commands.
Its screen resolution is 72x40.
Its screen start position is 30, 12.

## Requirements

This shield can only be used with esp32c3\_042\_oled board.

## Programming

Set `-b esp32c3_042_oled --shield abrobot_sh1106_72x40` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b esp32c3_042_oled --shield abrobot_sh1106_72x40 samples/drivers/display
```
