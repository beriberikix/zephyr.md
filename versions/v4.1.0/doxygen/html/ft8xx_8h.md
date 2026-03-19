---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ft8xx_8h.html
original_path: doxygen/html/ft8xx_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx.h File Reference

FT8XX public API.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](ft8xx_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ft8xx\_touch\_transform](structft8xx__touch__transform.md) |
|  | Structure holding touchscreen calibration data. [More...](structft8xx__touch__transform.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [ft8xx\_int\_callback](group__ft8xx__interface.md#ga846a90d72b56f388d5b4f60cf6d658b0)) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
|  | Callback API to inform API user that FT8xx triggered interrupt. |

| Functions | |
| --- | --- |
| void | [ft8xx\_calibrate](group__ft8xx__interface.md#ga586f6ff1eddd5b596d2e35fb5fdd8148) (const struct [device](structdevice.md) \*dev, struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \*data) |
|  | Calibrate touchscreen. |
| void | [ft8xx\_touch\_transform\_set](group__ft8xx__interface.md#ga1d74a13782c6ab9f8b07a28503058356) (const struct [device](structdevice.md) \*dev, const struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \*data) |
|  | Set touchscreen calibration data. |
| int | [ft8xx\_get\_touch\_tag](group__ft8xx__interface.md#gaea3589b5a0aa34a09a81ea15c1595219) (const struct [device](structdevice.md) \*dev) |
|  | Get tag of recently touched element. |
| void | [ft8xx\_register\_int](group__ft8xx__interface.md#gaf392199312ddb82451a4f31e2955079d) (const struct [device](structdevice.md) \*dev, [ft8xx\_int\_callback](group__ft8xx__interface.md#ga846a90d72b56f388d5b4f60cf6d658b0) callback, void \*user\_data) |
|  | Set callback executed when FT8xx triggers interrupt. |

## Detailed Description

FT8XX public API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx.h](ft8xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
