---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ft8xx_8h.html
original_path: doxygen/html/ft8xx_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx.h File Reference

FT8XX public API.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](ft8xx_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ft8xx\_touch\_transform](structft8xx__touch__transform.md) |
|  | Structure holding touchscreen calibration data. [More...](structft8xx__touch__transform.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [ft8xx\_int\_callback](group__ft8xx__interface.md#ga3841a8c74d795b14b7fbdd6115410217)) (void) |
|  | Callback API to inform API user that FT8xx triggered interrupt. |

| Functions | |
| --- | --- |
| void | [ft8xx\_calibrate](group__ft8xx__interface.md#gaa563d0378314c304277e5bf54ab90c47) (struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \*data) |
|  | Calibrate touchscreen. |
| void | [ft8xx\_touch\_transform\_set](group__ft8xx__interface.md#gae45273c4617b565b4712a286f4f77c9c) (const struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \*data) |
|  | Set touchscreen calibration data. |
| int | [ft8xx\_get\_touch\_tag](group__ft8xx__interface.md#ga532142aba69b418b1d8f19ca954ba3bf) (void) |
|  | Get tag of recently touched element. |
| void | [ft8xx\_register\_int](group__ft8xx__interface.md#ga02bded8612961be5ff72c8cf3bf4afe3) ([ft8xx\_int\_callback](group__ft8xx__interface.md#ga3841a8c74d795b14b7fbdd6115410217) callback) |
|  | Set callback executed when FT8xx triggers interrupt. |

## Detailed Description

FT8XX public API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx.h](ft8xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
