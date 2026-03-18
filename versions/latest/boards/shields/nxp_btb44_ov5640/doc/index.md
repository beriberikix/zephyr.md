---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/shields/nxp_btb44_ov5640/doc/index.html
original_path: boards/shields/nxp_btb44_ov5640/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# NXP BTB-44 OV5640 Camera Module

## Overview

This shield supports ov5640 camera modules which use a 44-pin board-to-board connector and
a MIPI CSI or DVP (parallel) interface. These camera modules are made specifically for and
provided together with NXP’s i.MX RT1160 and RT1170 EVK boards.

More information about this OV5640 camera module can be found at [Camera iMXRT](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183) [[1]](#id1).

### Pins assignment of the NXP board-to-board 44-pin OV5640 camera module

| Camera Connector Pin | Function |
| --- | --- |
| 1 | AGND |
| 2 | AF\_GND |
| 3 | STROBE |
| 4 | AF\_VCC |
| 5 | SDA |
| 6 | VCMSINK |
| 7 | SCL |
| 8 | AVDD |
| 9 | RESETB |
| 10 | GPIO1 |
| 11 | PCLK |
| 12 | GPIO0 |
| 13 | VSYNC |
| 14 | FREX |
| 15 | HREF |
| 16 | MIPI\_CSI\_DP1 / D9 |
| 17 | PWDN |
| 18 | MIPI\_CSI\_DN1 / D8 |
| 19 | MIPI\_CSI\_DP1 / D9 |
| 20 | DGND |
| 21 | MIPI\_CSI\_DN1 / D8 |
| 22 | MIPI\_CSI\_CLKP / D7 |
| 23 | MIPI\_CSI\_CLKP / D7 |
| 24 | MIPI\_CSI\_CLKN / D6 |
| 25 | MIPI\_CSI\_CLKN / D6 |
| 26 | DGND |
| 27 | MIPI\_CSI\_DP0 / D5 |
| 28 | MIPI\_CSI\_DP0 / D5 |
| 29 | MIPI\_CSI\_DN0 / D4 |
| 30 | MIPI\_CSI\_DN0 / D4 |
| 31 | D3 |
| 32 | DGND |
| 33 | D2 |
| 34 | XCLK |
| 35 | D1 |
| 36 | DVDD |
| 37 | D0 |
| 38 | DOVDD |
| 39 | DGND |
| 40 | DGND |
| 41 | GND |
| 42 | GND |
| 43 | GND |
| 44 | AF\_GND |

## Requirements

This shield can only be used with a board which provides a 44-pin board-to-board
connector with MIPI CSI or DVP (parallel) interface where the pinouts are defined
as above, such as i.MX RT1160 and RT1170 EVK boards.

## Programming

Set `--shield nxp_btb44_ov5640` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b mimxrt1170_evk/mimxrt1176/cm7 --shield nxp_btb44_ov5640 samples/subsys/video/capture
```

## References

[[1](#id2)]

[https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183)
