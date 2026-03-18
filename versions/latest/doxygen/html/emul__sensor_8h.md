---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/emul__sensor_8h.html
original_path: doxygen/html/emul__sensor_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul\_sensor.h File Reference

`#include <[zephyr/drivers/emul.h](emul_8h_source.md)>`  
`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`  
`#include <[zephyr/drivers/sensor_attribute_types.h](sensor__attribute__types_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](emul__sensor_8h_source.md)

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [emul\_sensor\_backend\_is\_supported](group__sensor__emulator__backend.md#gadb7174783ab8466ab55aebb463fdfdd7) (const struct [emul](structemul.md) \*target) |
|  | Check if a given sensor emulator supports the backend API. |
| static int | [emul\_sensor\_backend\_set\_channel](group__sensor__emulator__backend.md#ga53ecc5c20890546ee15b5ccf10945172) (const struct [emul](structemul.md) \*target, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) ch, const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*value, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift) |
|  | Set an expected value for a given channel on a given sensor emulator. |
| static int | [emul\_sensor\_backend\_get\_sample\_range](group__sensor__emulator__backend.md#ga7662fbe6ebe090cacc4b1436975beeef) (const struct [emul](structemul.md) \*target, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) ch, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*lower, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*upper, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*epsilon, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*shift) |
|  | Query an emulator for a channel's supported sample value range and tolerance. |
| static int | [emul\_sensor\_backend\_set\_attribute](group__sensor__emulator__backend.md#ga4011dd5d98c2ef63cdaccddd306c9d67) (const struct [emul](structemul.md) \*target, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) ch, enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attribute, const void \*value) |
|  | Set the emulator's attribute values. |
| static int | [emul\_sensor\_backend\_get\_attribute\_metadata](group__sensor__emulator__backend.md#ga66aa2b47e79047a749b331265a66e215) (const struct [emul](structemul.md) \*target, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) ch, enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attribute, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*min, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*max, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*increment, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*shift) |
|  | Get metadata about an attribute. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [emul\_sensor.h](emul__sensor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
