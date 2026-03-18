---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/input__analog__axis_8h.html
original_path: doxygen/html/input__analog__axis_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_analog\_axis.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](input__analog__axis_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [analog\_axis\_calibration](structanalog__axis__calibration.md) |
|  | Analog axis calibration data structure. [More...](structanalog__axis__calibration.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [analog\_axis\_raw\_data\_t](group__input__analog__axis.md#ga384e901afe29ae91e01c44b458034d64)) (const struct [device](structdevice.md) \*dev, int channel, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) raw\_val) |
|  | Analog axis raw data callback. |

| Functions | |
| --- | --- |
| void | [analog\_axis\_set\_raw\_data\_cb](group__input__analog__axis.md#ga645237cdb40113e4253a24e902091f3e) (const struct [device](structdevice.md) \*dev, [analog\_axis\_raw\_data\_t](group__input__analog__axis.md#ga384e901afe29ae91e01c44b458034d64) cb) |
|  | Set a raw data callback. |
| int | [analog\_axis\_num\_axes](group__input__analog__axis.md#ga99dd3b96a43f115a8c90859e7eed24d4) (const struct [device](structdevice.md) \*dev) |
|  | Get the number of defined axes. |
| int | [analog\_axis\_calibration\_get](group__input__analog__axis.md#gad359f00fa9c46219a55a218d26d0407a) (const struct [device](structdevice.md) \*dev, int channel, struct [analog\_axis\_calibration](structanalog__axis__calibration.md) \*cal) |
|  | Get the axis calibration data. |
| int | [analog\_axis\_calibration\_set](group__input__analog__axis.md#gaae496bde41a58d92521b0a24f762caeb) (const struct [device](structdevice.md) \*dev, int channel, struct [analog\_axis\_calibration](structanalog__axis__calibration.md) \*cal) |
|  | Set the axis calibration data. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_analog\_axis.h](input__analog__axis_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
