---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/weact_ov2640_cam_module/doc/index.html
original_path: boards/shields/weact_ov2640_cam_module/doc/index.html
---

# WeAct Studio MiniSTM32H7xx OV2640 Camera Sensor

## Overview

The OV2640 camera sensor is designed to interface with the WeAct Studio
MiniSTM32H7xx boards, providing camera sensor capabilities. This shield
integrates the OV2640 camera module, which is capable of capturing images
and video with a resolution of up to 2 megapixels.

![OV2640 Camera Sensor](../../../../_images/ov2640.webp)

More information about the OV2640 camera sensor can be found on the
[MiniSTM32H7xx GitHub](https://github.com/WeActStudio/MiniSTM32H7xx) and in the [OV2640 datasheet](https://www.uctronics.com/download/cam_module/OV2640DS.pdf).

## Requirements

Your board needs to have a `zephyr_camera_dvp` device tree label to work with this shield.

### Pin Assignments

The shield connects to the WeAct Studio MiniSTM32H7xx board via the
following pins:

| Shield Pin | Board Pin | Function |
| --- | --- | --- |
| DCMI\_D0 | PC6 | DCMI Data Line 0 |
| DCMI\_D1 | PC7 | DCMI Data Line 1 |
| DCMI\_D2 | PE0 | DCMI Data Line 2 |
| DCMI\_D3 | PE1 | DCMI Data Line 3 |
| DCMI\_D4 | PE4 | DCMI Data Line 4 |
| DCMI\_D5 | PD3 | DCMI Data Line 5 |
| DCMI\_D6 | PE5 | DCMI Data Line 6 |
| DCMI\_D7 | PE6 | DCMI Data Line 7 |
| DCMI\_HSYNC | PA4 | DCMI HSYNC |
| DCMI\_VSYNC | PB7 | DCMI VSYNC |
| DCMI\_PIXCLK | PA6 | DCMI Pixel Clock |
| I2C\_SDA | PB9 | I2C Data Line |
| I2C\_SCL | PB8 | I2C Clock Line |
| RCC\_MCO1 | PA8 | Clock Output |
| SUPPLY | PA7 | Power Supply Control (GPIO) |

## Programming

Set `--shield weact_ov2640_cam_module` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b mini_stm32h743 --shield weact_ov2640_cam_module samples/drivers/video/capture_to_lvgl/ -- -DCONFIG_BOOT_DELAY=2000
```
