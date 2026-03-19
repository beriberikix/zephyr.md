---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/video/capture_to_lvgl/README.html
original_path: samples/drivers/video/capture_to_lvgl/README.html
---

# Video capture to LVGL

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/video/capture_to_lvgl/README.rst/..)

## Description

The application uses the [Video API](../../../../hardware/peripherals/video.md#video-api) to retrieve video frames from
a video capture device, write a frame count message to the console, and then send
the frame to an LCD display.

## Requirements

This sample requires a supported [video capture device](../../../../hardware/peripherals/video.md#video-api) (e.g., a camera)
and a [display](../../../../hardware/peripherals/display/index.md#display-api).

## Wiring

On the [WeAct Studio STM32H743](https://github.com/WeActStudio/MiniSTM32H7xx) [[1]](#id1), connect the OV2640 camera module and the 0.96” ST7735
TFT LCD display. Connect a USB cable from a host to the micro USB-C connector on the
board to receive console output messages.

## Building and Running

For [MiniSTM32H743 Core Board](../../../../boards/weact/mini_stm32h743/doc/index.md#mini_stm32h743), build this sample application with the following commands:

```shell
west build -b mini_stm32h743 --shield weact_ov2640_cam_module samples/drivers/video/capture_to_lvgl/ -- -DCONFIG_BOOT_DELAY=2000
west flash
```

### Sample Output

```shell
[00:00:02.779,000] <inf> main: - Device name: dcmi@48020000
[00:00:02.779,000] <inf> main: - Capabilities:
[00:00:02.779,000] <inf> main:   RGBP width [160; 160; 0] height [120; 120; 0]
[00:00:02.779,000] <inf> main:   RGBP width [176; 176; 0] height [144; 144; 0]
[00:00:02.780,000] <inf> main:   RGBP width [240; 240; 0] height [160; 160; 0]
[00:00:02.780,000] <inf> main:   RGBP width [320; 320; 0] height [240; 240; 0]
[00:00:02.780,000] <inf> main:   RGBP width [352; 352; 0] height [288; 288; 0]
[00:00:02.780,000] <inf> main:   RGBP width [640; 640; 0] height [480; 480; 0]
[00:00:02.780,000] <inf> main:   RGBP width [800; 800; 0] height [600; 600; 0]
[00:00:02.780,000] <inf> main:   RGBP width [1024; 1024; 0] height [768; 768; 0]
[00:00:02.780,000] <inf> main:   RGBP width [1280; 1280; 0] height [1024; 1024; 0]
[00:00:02.780,000] <inf> main:   RGBP width [1600; 1600; 0] height [1200; 1200; 0]
[00:00:02.780,000] <inf> main:   JPEG width [160; 160; 0] height [120; 120; 0]
[00:00:02.780,000] <inf> main:   JPEG width [176; 176; 0] height [144; 144; 0]
[00:00:02.780,000] <inf> main:   JPEG width [240; 240; 0] height [160; 160; 0]
[00:00:02.780,000] <inf> main:   JPEG width [320; 320; 0] height [240; 240; 0]
[00:00:02.780,000] <inf> main:   JPEG width [352; 352; 0] height [288; 288; 0]
[00:00:02.780,000] <inf> main:   JPEG width [640; 640; 0] height [480; 480; 0]
[00:00:02.780,000] <inf> main:   JPEG width [800; 800; 0] height [600; 600; 0]
[00:00:02.780,000] <inf> main:   JPEG width [1024; 1024; 0] height [768; 768; 0]
[00:00:02.780,000] <inf> main:   JPEG width [1280; 1280; 0] height [1024; 1024; 0]
[00:00:02.780,000] <inf> main:   JPEG width [1600; 1600; 0] height [1200; 1200; 0]
[00:00:02.852,000] <inf> main: - Format: RGBP 160x120 320
[00:00:02.854,000] <inf> main: - Capture started
```

## References

[[1](#id2)]

[https://github.com/WeActStudio/MiniSTM32H7xx](https://github.com/WeActStudio/MiniSTM32H7xx)

## See also

[Video Interface](../../../../doxygen/html/group__video__interface.md)
