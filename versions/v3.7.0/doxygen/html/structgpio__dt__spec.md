---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structgpio__dt__spec.html
original_path: doxygen/html/structgpio__dt__spec.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_dt\_spec Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [GPIO Driver APIs](group__gpio__interface.md)

Container for GPIO pin information specified in devicetree.
[More...](#details)

`#include <[gpio.h](drivers_2gpio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [port](#a5d617d47e2f568c7a4402a8f5a40ed4f) |
|  | GPIO device controlling the pin. |
| [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) | [pin](#ad7e6fbb0cba0be94a47d4f2add056c84) |
|  | The pin's number on the device. |
| [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2) | [dt\_flags](#ae3b90e7e22708798c67da94f72ad1ab0) |
|  | The pin's configuration flags as specified in devicetree. |

## Detailed Description

Container for GPIO pin information specified in devicetree.

This type contains a pointer to a GPIO device, pin number for a pin controlled by that device, and the subset of pin configuration flags which may be given in devicetree.

See also
:   [GPIO\_DT\_SPEC\_GET\_BY\_IDX](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf "Static initializer for a gpio_dt_spec.")
:   [GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983 "Like GPIO_DT_SPEC_GET_BY_IDX(), with a fallback to a default value.")
:   [GPIO\_DT\_SPEC\_GET](group__gpio__interface.md#ga2fa6bb5880f46984f9fc29c70f7d503e "Equivalent to GPIO_DT_SPEC_GET_BY_IDX(node_id, prop, 0).")
:   [GPIO\_DT\_SPEC\_GET\_OR](group__gpio__interface.md#ga26b2205aa82819df1d80a22761352e71 "Equivalent to GPIO_DT_SPEC_GET_BY_IDX_OR(node_id, prop, 0, default_value).")

## Field Documentation

## [◆ ](#ae3b90e7e22708798c67da94f72ad1ab0)dt\_flags

| [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2) gpio\_dt\_spec::dt\_flags |
| --- |

The pin's configuration flags as specified in devicetree.

## [◆ ](#ad7e6fbb0cba0be94a47d4f2add056c84)pin

| [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) gpio\_dt\_spec::pin |
| --- |

The pin's number on the device.

## [◆ ](#a5d617d47e2f568c7a4402a8f5a40ed4f)port

| const struct [device](structdevice.md)\* gpio\_dt\_spec::port |
| --- |

GPIO device controlling the pin.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[gpio.h](drivers_2gpio_8h_source.md)

- [gpio\_dt\_spec](structgpio__dt__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
