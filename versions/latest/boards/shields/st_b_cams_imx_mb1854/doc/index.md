---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/st_b_cams_imx_mb1854/doc/index.html
original_path: boards/shields/st_b_cams_imx_mb1854/doc/index.html
---

# ST B-CAMS-IMX-MB1854

## Overview

The B-CAMS-IMX camera module provides a compelling hardware set to
handle multiple computer vision scenarios and use cases. It features
a high-resolution 5‑Mpx RGB CMOS image sensor, an inertial motion unit,
and a Time‑of‑Flight sensor. It can be used with any STM32 boards featuring
a MIPI CSI-2® interface with a 22‑pin FFC connector to enable full-featured
computer vision on STM32 microcontrollers and microprocessors easily.

[![B-CAMS-IMX-MB1854](https://docs.zephyrproject.org/4.2.0/_images/st_b_cams_imx.webp)
](https://docs.zephyrproject.org/4.2.0/_images/st_b_cams_imx.webp)

B-CAMS-IMX MB1854 Image (Credit: STMicroelectronics.)

## Requirements

The camera module bundle is compatible with all STM32 Discovery kits and
Evaluation boards featuring a 22 pins FFC connector, such as the STM32N6570\_DK
Discovery kit.

## Usage

The shield can be used in any application by setting `SHIELD` to
`st_b_cams_imx_mb1854` for boards with the necessary device tree node labels.

Set `--shield "st_b_cams_imx_mb1854"` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b stm32n6570_dk --shield st_b_cams_imx_mb1854 samples/drivers/video/capture
```

## References

- [Product page](https://www.st.com/en/evaluation-tools/b-cams-imx.html)
- [Databrief](https://www.st.com/resource/en/data_brief/b-cams-imx.pdf)
- [User manual](https://www.st.com/resource/en/user_manual/um3354-camera-module-bundle-for-stm32-boards-stmicroelectronics.pdf)
