---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/shields/dvp_fpc24_mt9m114/doc/index.html
original_path: boards/shields/dvp_fpc24_mt9m114/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# DVP FPC-24 MT9M114 Camera Module

## Overview

This shield supports mt9m114 camera modules which use a 24-pin FPC connector and a DVP
(Digital Video Port), aka parallel interface. These camera modules are compatible and provided
together with the i.MX RT1050, RT1060 and RT1064 EVKs as specified here [Camera iMXRT](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183) [[1]](#id1).

### Pins assignment of the DVP FPC-24 MT9M114 camera module

| FPC Connector Pin | Function |
| --- | --- |
| 1 | NC |
| 2 | AGND |
| 3 | SDA |
| 4 | AVDD |
| 5 | SCL |
| 6 | Reset |
| 7 | Vsync |
| 8 | Powerdown |
| 9 | Hsync |
| 10 | DVDD |
| 11 | DOVDD |
| 12 | Data 9 |
| 13 | Master Clock |
| 14 | Data 8 |
| 15 | DGND |
| 16 | Data 7 |
| 17 | Pixel Clock |
| 18 | Data 6 |
| 19 | Data 2 |
| 20 | Data 5 |
| 21 | Data 3 |
| 22 | Data 4 |
| 23 | Data 1 |
| 24 | Data 0 |

## Requirements

This shield can only be used with a board which provides a configuration for a 24-pins FPC
connector with DVP (parallel) interface, such as the i.MX RT1050, RT1060, RT1064 EVKs.

## Programming

Set `--shield dvp_fpc24_mt9m114` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b mimxrt1064_evk --shield dvp_fpc24_mt9m114 samples/subsys/video/capture
```

## References

[[1](#id2)]

[https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183)
