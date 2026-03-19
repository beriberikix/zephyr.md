---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/st_b_cams_omv_mb1683/doc/index.html
original_path: boards/shields/st_b_cams_omv_mb1683/doc/index.html
---

# ST B-CAMS-OMV-MB1683

## Overview

The camera module bundle (B-CAMS-OMV) provides extension connectors
for the MB1379 STMicroelectronics camera module daughterboard or
third-party modules like OpenMV and Waveshare modules. It can be used
with the STM32 boards featuring a 1 x 30 pin ZIF connector for the
connection of multiple cameras to implement computer vision on STM32
microcontrollers easily.

The camera module bundle is compatible with all STM32 Discovery kits and
Evaluation boards featuring a ZIF connector, such as the STM32H747I-DISCO,
STM32H7B3I-DK, and 32L4R9IDISCOVERY Discovery kits.

[![B-CAMS-OMV-MB1683](../../../../_images/st_b_cams_omv.webp)
](../../../../_images/st_b_cams_omv.webp)

B-CAMS-OMV MB1683 Image (Credit: STMicroelectronics.)

The camera signals go into the shield from one of the supported input
connectors (CN1, CN2, CN4), and out of the shield towards Zephyr through
the output 30-pin ZIF connector CN5.

Refer to the [User manual](https://www.st.com/resource/en/user_manual/um2779-camera-module-bundle-for-stm32-boards-stmicroelectronics.pdf) for the pinout of CN1 and CN2.

## Waveshare camera board connector CN4 (camera input)

| Pin number | Description | Pin number | Description |
| --- | --- | --- | --- |
| 1 | GND | 2 | VCAM |
| 3 | I2C\_SDA | 4 | I2C\_SCL |
| 5 | DCMI\_HSYNC | 6 | DCMI\_VSYNC |
| 7 | Camera\_CLK | 8 | DCMI\_PIXCLK |
| 9 | DCMI\_D6 | 10 | DCMI\_D7 |
| 11 | DCMI\_D4 | 12 | DCMI\_D5 |
| 13 | DCMI\_D2 | 14 | DCMI\_D3 |
| 15 | DCMI\_D0 | 16 | DCMI\_D1 |
| 17 | PWR\_EN / LED1 | 18 | RESET# |

## ZIF connector CN5 (camera output)

| Pin number | Description |
| --- | --- |
| 1 | 3V3 |
| 2 | GND |
| 3 | I2C\_SCL |
| 4 | I2C\_SDA |
| 5 | RESET# |
| 6 | PWR\_EN / LED1 |
| 7 | SHUTTER |
| 8 | GND |
| 9 | PULLDOWN / LED2 |
| 10 | Camera\_CLK |
| 11 | 3V3 |
| 12 | DCMI\_VSYNC |
| 13 | 5V (RSU) |
| 14 | DCMI\_HSYNC |
| 15 | GND |
| 16 | DCMI\_PIXCK |
| 17 | GND |
| 18 | SPI\_MISO |
| 19 | SPI\_CS |
| 20 | DCMI\_D7 |
| 21 | DCMI\_D6 |
| 22 | DCMI\_D5 |
| 23 | DCMI\_D4 |
| 24 | DCMI\_D3 |
| 25 | DCMI\_D2 |
| 26 | DCMI\_D1 |
| 27 | DCMI\_D0 |
| 28 | SPI\_MOSI |
| 29 | SPI\_CLK |
| 30 | GND |

## Requirements

The camera module bundle is compatible with all STM32 Discovery kits and
Evaluation boards featuring a ZIF connector, such as the STM32H747I-DISCO,
STM32H7B3I-DK, and 32L4R9IDISCOVERY Discovery kits.

## Usage

The shield can be used in any application by setting `SHIELD` to
`_st_b_cams_omv_mb1683` and adding the necessary device tree properties.

Set `--shield "st_b_cams_omv_mb1683"` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b stm32h7b3i_dk --shield st_b_cams_omv_mb1683 samples/drivers/video/capture_to_lvgl
```

## References

- [Product page](https://www.st.com/en/evaluation-tools/b-cams-omv.html)
- [Databrief](https://www.st.com/resource/en/data_brief/b-cams-omv.pdf)
- [User manual](https://www.st.com/resource/en/user_manual/um2779-camera-module-bundle-for-stm32-boards-stmicroelectronics.pdf)
