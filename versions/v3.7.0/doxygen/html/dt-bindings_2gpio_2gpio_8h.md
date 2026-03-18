---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dt-bindings_2gpio_2gpio_8h.html
original_path: doxygen/html/dt-bindings_2gpio_2gpio_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio.h File Reference

[Go to the source code of this file.](dt-bindings_2gpio_2gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [GPIO\_DT\_FLAGS\_MASK](group__gpio__interface.md#ga335bf7efee07e03961ab91a86295897a)   0x3F |
|  | Mask for DT GPIO flags. |
| #define | [GPIO\_INT\_WAKEUP](group__gpio__interface.md#ga644109ce84c8feffe1226b9b50122a96)   (1 << 6) |
|  | Configures GPIO interrupt to wakeup the system from low power mode. |
| GPIO pin active level flags | |
| #define | [GPIO\_ACTIVE\_LOW](group__gpio__interface.md#ga62cea8989df2425e5e5e712217d65f46)   (1 << 0) |
|  | GPIO pin is active (has logical value '1') in low state. |
| #define | [GPIO\_ACTIVE\_HIGH](group__gpio__interface.md#gad93badd2828d065e7fd14cf40dd05039)   (0 << 0) |
|  | GPIO pin is active (has logical value '1') in high state. |
| GPIO pin drive flags | |
| #define | [GPIO\_OPEN\_DRAIN](group__gpio__interface.md#ga72b7ac5b3613d972b88268bee9068e35)   (GPIO\_SINGLE\_ENDED | GPIO\_LINE\_OPEN\_DRAIN) |
|  | Configures GPIO output in open drain mode (wired AND). |
| #define | [GPIO\_OPEN\_SOURCE](group__gpio__interface.md#ga5ace024873272a3f6727fc186afa0320)   (GPIO\_SINGLE\_ENDED | GPIO\_LINE\_OPEN\_SOURCE) |
|  | Configures GPIO output in open source mode (wired OR). |
| GPIO pin bias flags | |
| #define | [GPIO\_PULL\_UP](group__gpio__interface.md#gaaa7921da231fd2b96575fa522e2c1970)   (1 << 4) |
|  | Enables GPIO pin pull-up. |
| #define | [GPIO\_PULL\_DOWN](group__gpio__interface.md#gadec1802e074f3021d464da09cd66c7cf)   (1 << 5) |
|  | Enable GPIO pin pull-down. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [gpio.h](dt-bindings_2gpio_2gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
