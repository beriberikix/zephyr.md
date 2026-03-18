---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/input__pat912x_8h.html
original_path: doxygen/html/input__pat912x_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_pat912x.h File Reference

[Go to the source code of this file.](input__pat912x_8h_source.md)

| Functions | |
| --- | --- |
| int | [pat912x\_set\_resolution](#a1c9f11b31312dbaf5cf24ddaaad7eada) (const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) res\_x\_cpi, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) res\_y\_cpi) |
|  | Set resolution on a pat912x device. |

## Function Documentation

## [◆ ](#a1c9f11b31312dbaf5cf24ddaaad7eada)pat912x\_set\_resolution()

| int pat912x\_set\_resolution | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *res\_x\_cpi*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *res\_y\_cpi* ) |

Set resolution on a pat912x device.

Parameters
:   | dev | pat912x device. |
    | --- | --- |
    | res\_x\_cpi | CPI resolution for the X axis, 0 to 1275, -1 to keep the current value. |
    | res\_y\_cpi | CPI resolution for the Y axis, 0 to 1275, -1 to keep the current value. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_pat912x.h](input__pat912x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
