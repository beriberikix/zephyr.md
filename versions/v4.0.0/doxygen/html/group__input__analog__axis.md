---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__input__analog__axis.html
original_path: doxygen/html/group__input__analog__axis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Analog axis API

[Device Driver APIs](group__io__interfaces.md)

Analog axis API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [analog\_axis\_calibration](structanalog__axis__calibration.md) |
|  | Analog axis calibration data structure. [More...](structanalog__axis__calibration.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [analog\_axis\_raw\_data\_t](#ga384e901afe29ae91e01c44b458034d64)) (const struct [device](structdevice.md) \*dev, int channel, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) raw\_val) |
|  | Analog axis raw data callback. |

| Functions | |
| --- | --- |
| void | [analog\_axis\_set\_raw\_data\_cb](#ga645237cdb40113e4253a24e902091f3e) (const struct [device](structdevice.md) \*dev, [analog\_axis\_raw\_data\_t](#ga384e901afe29ae91e01c44b458034d64) cb) |
|  | Set a raw data callback. |
| int | [analog\_axis\_num\_axes](#ga99dd3b96a43f115a8c90859e7eed24d4) (const struct [device](structdevice.md) \*dev) |
|  | Get the number of defined axes. |
| int | [analog\_axis\_calibration\_get](#gad359f00fa9c46219a55a218d26d0407a) (const struct [device](structdevice.md) \*dev, int channel, struct [analog\_axis\_calibration](structanalog__axis__calibration.md) \*cal) |
|  | Get the axis calibration data. |
| int | [analog\_axis\_calibration\_set](#gaae496bde41a58d92521b0a24f762caeb) (const struct [device](structdevice.md) \*dev, int channel, struct [analog\_axis\_calibration](structanalog__axis__calibration.md) \*cal) |
|  | Set the axis calibration data. |
| int | [analog\_axis\_calibration\_save](#ga56973ef7c7a465defdb7bd2934c86778) (const struct [device](structdevice.md) \*dev) |
|  | Save the calibration data. |

## Detailed Description

Analog axis API.

## Typedef Documentation

## [◆ ](#ga384e901afe29ae91e01c44b458034d64)analog\_axis\_raw\_data\_t

| typedef void(\* analog\_axis\_raw\_data\_t) (const struct [device](structdevice.md) \*dev, int channel, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) raw\_val) |
| --- |

`#include <[input_analog_axis.h](input__analog__axis_8h.md)>`

Analog axis raw data callback.

Parameters
:   | dev | Analog axis device. |
    | --- | --- |
    | channel | Channel number. |
    | raw\_val | Raw value for the channel. |

## Function Documentation

## [◆ ](#gad359f00fa9c46219a55a218d26d0407a)analog\_axis\_calibration\_get()

| int analog\_axis\_calibration\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | int | *channel*, |
|  |  | struct [analog\_axis\_calibration](structanalog__axis__calibration.md) \* | *cal* ) |

`#include <[input_analog_axis.h](input__analog__axis_8h.md)>`

Get the axis calibration data.

Parameters
:   | dev | Analog axis device. |
    | --- | --- |
    | channel | Channel number. |
    | cal | Pointer to an [analog\_axis\_calibration](structanalog__axis__calibration.md "Analog axis calibration data structure.") structure that is going to get set with the current calibration data. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If the specified channel is not valid. |

## [◆ ](#ga56973ef7c7a465defdb7bd2934c86778)analog\_axis\_calibration\_save()

| int analog\_axis\_calibration\_save | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[input_analog_axis_settings.h](input__analog__axis__settings_8h.md)>`

Save the calibration data.

Save the calibration data permanently on the specifided device, requires the [Settings](group__settings.md "Settings") subsystem to be configured and initialized.

Parameters
:   | dev | Analog axis device. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | In case of any other error. |

## [◆ ](#gaae496bde41a58d92521b0a24f762caeb)analog\_axis\_calibration\_set()

| int analog\_axis\_calibration\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | int | *channel*, |
|  |  | struct [analog\_axis\_calibration](structanalog__axis__calibration.md) \* | *cal* ) |

`#include <[input_analog_axis.h](input__analog__axis_8h.md)>`

Set the axis calibration data.

Parameters
:   | dev | Analog axis device. |
    | --- | --- |
    | channel | Channel number. |
    | cal | Pointer to an [analog\_axis\_calibration](structanalog__axis__calibration.md "Analog axis calibration data structure.") structure with the new calibration data |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If the specified channel is not valid. |

## [◆ ](#ga99dd3b96a43f115a8c90859e7eed24d4)analog\_axis\_num\_axes()

| int analog\_axis\_num\_axes | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[input_analog_axis.h](input__analog__axis_8h.md)>`

Get the number of defined axes.

Return values
:   | n | The number of defined axes for dev. |
    | --- | --- |

## [◆ ](#ga645237cdb40113e4253a24e902091f3e)analog\_axis\_set\_raw\_data\_cb()

| void analog\_axis\_set\_raw\_data\_cb | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [analog\_axis\_raw\_data\_t](#ga384e901afe29ae91e01c44b458034d64) | *cb* ) |

`#include <[input_analog_axis.h](input__analog__axis_8h.md)>`

Set a raw data callback.

Set a callback to receive raw data for the specified analog axis device. This is meant to be use in the application to acquire the data to use for calibration. Set cb to NULL to disable the callback.

Parameters
:   | dev | Analog axis device. |
    | --- | --- |
    | cb | An [analog\_axis\_raw\_data\_t](#ga384e901afe29ae91e01c44b458034d64) callback to use, NULL disable. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
