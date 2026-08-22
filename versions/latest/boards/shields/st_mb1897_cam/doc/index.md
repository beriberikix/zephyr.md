---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/st_mb1897_cam/doc/index.html
original_path: boards/shields/st_mb1897_cam/doc/index.html
---

# ST\_MB1897\_CAM

## Overview

The STM32MP135F discovery board is delivered with a CSI camera module
connected to the STM32MP135F-DK board via a 15pins FFC connector.
The camera module board (MB1897) embeds a Galaxycore GC2145 CSI sensor.

![ST-MB1897-CAM](../../../../_images/st_mb1897_cam.webp)

MB1897 Image (Credit: STMicroelectronics.)

## Requirements

The camera module bundle is compatible with STM32 Discovery kits and
Evaluation boards featuring a 15 pins FFC connector, such as the STM32MP13
Discovery kit.

## Usage

The shield can be used in any application by setting `SHIELD` to
`st_mb1897_cam` for boards with the necessary device tree node labels.

Set `--shield "st_mb1897_cam"` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b stm32mp135f_dk --shield st_mb1897_cam samples/drivers/video/capture
```
