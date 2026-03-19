---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__sensor__emulator__backend.html
original_path: doxygen/html/group__sensor__emulator__backend.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Sensor emulator backend API

[Device Driver APIs](group__io__interfaces.md)

Sensor emulator backend API.
[More...](#details)

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [emul\_sensor\_backend\_is\_supported](#gadb7174783ab8466ab55aebb463fdfdd7) (const struct [emul](structemul.md) \*target) |
|  | Check if a given sensor emulator supports the backend API. |
| static int | [emul\_sensor\_backend\_set\_channel](#gadfa5c6618361bb382e5b44dc1a03f735) (const struct [emul](structemul.md) \*target, struct [sensor\_chan\_spec](structsensor__chan__spec.md) ch, const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*value, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift) |
|  | Set an expected value for a given channel on a given sensor emulator. |
| static int | [emul\_sensor\_backend\_get\_sample\_range](#ga271513cf5b2b5ee28d5f37e42449ee1e) (const struct [emul](structemul.md) \*target, struct [sensor\_chan\_spec](structsensor__chan__spec.md) ch, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*lower, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*upper, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*epsilon, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*shift) |
|  | Query an emulator for a channel's supported sample value range and tolerance. |
| static int | [emul\_sensor\_backend\_set\_attribute](#gaec1ddd02bc6ff1c66c83ca3f3af98fa8) (const struct [emul](structemul.md) \*target, struct [sensor\_chan\_spec](structsensor__chan__spec.md) ch, enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attribute, const void \*value) |
|  | Set the emulator's attribute values. |
| static int | [emul\_sensor\_backend\_get\_attribute\_metadata](#ga3bf83e34c2218823386489cf4f1cd84c) (const struct [emul](structemul.md) \*target, struct [sensor\_chan\_spec](structsensor__chan__spec.md) ch, enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attribute, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*min, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*max, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*increment, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*shift) |
|  | Get metadata about an attribute. |

## Detailed Description

Sensor emulator backend API.

## Function Documentation

## [◆ ](#ga3bf83e34c2218823386489cf4f1cd84c)emul\_sensor\_backend\_get\_attribute\_metadata()

| | int emul\_sensor\_backend\_get\_attribute\_metadata | ( | const struct [emul](structemul.md) \* | *target*, | | --- | --- | --- | --- | |  |  | struct [sensor\_chan\_spec](structsensor__chan__spec.md) | *ch*, | |  |  | enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) | *attribute*, | |  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *min*, | |  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *max*, | |  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *increment*, | |  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \* | *shift* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[emul_sensor.h](emul__sensor_8h.md)>`

Get metadata about an attribute.

Information provided by this function includes the minimum/maximum values of the attribute as well as the increment (value per LSB) which can be used as an epsilon when comparing results.

Parameters
:   | [in] | target | Pointer to emulator instance to operate on |
    | --- | --- | --- |
    | [in] | ch | The channel to request info for. If `ch` is unsupported, return '-ENOTSUP' |
    | [in] | attribute | The attribute to request info for. If `attribute` is unsupported, return '-ENOTSUP' |
    | [out] | min | The minimum value the attribute can be set to |
    | [out] | max | The maximum value the attribute can be set to |
    | [out] | increment | The value that the attribute increases by for every LSB |
    | [out] | shift | The shift for `min`, `max`, and `increment` |

Returns
:   0 on SUCCESS
:   < 0 on error

## [◆ ](#ga271513cf5b2b5ee28d5f37e42449ee1e)emul\_sensor\_backend\_get\_sample\_range()

| | int emul\_sensor\_backend\_get\_sample\_range | ( | const struct [emul](structemul.md) \* | *target*, | | --- | --- | --- | --- | |  |  | struct [sensor\_chan\_spec](structsensor__chan__spec.md) | *ch*, | |  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *lower*, | |  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *upper*, | |  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *epsilon*, | |  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \* | *shift* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[emul_sensor.h](emul__sensor_8h.md)>`

Query an emulator for a channel's supported sample value range and tolerance.

Parameters
:   |  | target | Pointer to emulator instance to operate on |
    | --- | --- | --- |
    |  | ch | The channel to request info for. If `ch` is unsupported, return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") |
    | [out] | lower | Minimum supported sample value in SI units, fixed-point format |
    | [out] | upper | Maximum supported sample value in SI units, fixed-point format |
    | [out] | epsilon | Tolerance to use comparing expected and actual values to account for rounding and sensor precision issues. This can usually be set to the minimum sample value step size. Uses SI units and fixed-point format. |
    | [out] | shift | The shift value (scaling factor) associated with `lower`, `upper`, and `epsilon`. |

Returns
:   0 if successful
:   -ENOTSUP if no backend API or if channel not supported by emul

## [◆ ](#gadb7174783ab8466ab55aebb463fdfdd7)emul\_sensor\_backend\_is\_supported()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) emul\_sensor\_backend\_is\_supported | ( | const struct [emul](structemul.md) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[emul_sensor.h](emul__sensor_8h.md)>`

Check if a given sensor emulator supports the backend API.

Parameters
:   | target | Pointer to emulator instance to query |
    | --- | --- |

Returns
:   True if supported, false if unsupported or if `target` is NULL.

## [◆ ](#gaec1ddd02bc6ff1c66c83ca3f3af98fa8)emul\_sensor\_backend\_set\_attribute()

| | int emul\_sensor\_backend\_set\_attribute | ( | const struct [emul](structemul.md) \* | *target*, | | --- | --- | --- | --- | |  |  | struct [sensor\_chan\_spec](structsensor__chan__spec.md) | *ch*, | |  |  | enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) | *attribute*, | |  |  | const void \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[emul_sensor.h](emul__sensor_8h.md)>`

Set the emulator's attribute values.

Parameters
:   | [in] | target | Pointer to emulator instance to operate on |
    | --- | --- | --- |
    | [in] | ch | The channel to request info for. If `ch` is unsupported, return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") |
    | [in] | attribute | The attribute to set |
    | [in] | value | the value to use (cast according to the channel/attribute pair) |

Returns
:   0 is successful
:   < 0 on error

## [◆ ](#gadfa5c6618361bb382e5b44dc1a03f735)emul\_sensor\_backend\_set\_channel()

| | int emul\_sensor\_backend\_set\_channel | ( | const struct [emul](structemul.md) \* | *target*, | | --- | --- | --- | --- | |  |  | struct [sensor\_chan\_spec](structsensor__chan__spec.md) | *ch*, | |  |  | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *value*, | |  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *shift* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[emul_sensor.h](emul__sensor_8h.md)>`

Set an expected value for a given channel on a given sensor emulator.

Parameters
:   | target | Pointer to emulator instance to operate on |
    | --- | --- |
    | ch | Sensor channel to set expected value for |
    | value | Expected value in fixed-point format using standard SI unit for sensor type |
    | shift | Shift value (scaling factor) applied to `value` |

Returns
:   0 if successful
:   -ENOTSUP if no backend API or if channel not supported by emul
:   -ERANGE if provided value is not in the sensor's supported range

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
