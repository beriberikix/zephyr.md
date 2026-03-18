---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/regulator_8h.html
original_path: doxygen/html/regulator_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

regulator.h File Reference

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](regulator_8h_source.md)

| Macros | |
| --- | --- |
| Regulator error flags. | |
|  | |
| #define | [REGULATOR\_ERROR\_OVER\_VOLTAGE](group__regulator__interface.md#ga5e17eb919086ea6e5239a240a6ac5aa1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Voltage is too high. |
| #define | [REGULATOR\_ERROR\_OVER\_CURRENT](group__regulator__interface.md#ga8705a7a63b8f187d66cda98d66372b5d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Current is too high. |
| #define | [REGULATOR\_ERROR\_OVER\_TEMP](group__regulator__interface.md#ga9570dd992355afa6ecef9610c8c45eda)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Temperature is too high. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd) |
|  | Opaque type to store regulator DVS states. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) |
|  | Opaque type to store regulator modes. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90) |
|  | Opaque bit map for regulator error flags (see [REGULATOR\_ERRORS](group__regulator__interface.md#REGULATOR_ERRORS "REGULATOR_ERRORS")). |

| Functions | |
| --- | --- |
| static int | [regulator\_parent\_dvs\_state\_set](group__regulator__parent__interface.md#ga980feabe8415a9643eb66c8566d700bf) (const struct [device](structdevice.md) \*dev, [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set a DVS state. |
| static int | [regulator\_parent\_ship\_mode](group__regulator__parent__interface.md#gaa65d0a8d792256818a2ba06ad67a4f02) (const struct [device](structdevice.md) \*dev) |
|  | Enter ship mode. |
| int | [regulator\_enable](group__regulator__interface.md#ga06e3109b9607521fe07686c6d601e460) (const struct [device](structdevice.md) \*dev) |
|  | Enable a regulator. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [regulator\_is\_enabled](group__regulator__interface.md#ga28744a6cabadfe5a22bc96792c8ad124) (const struct [device](structdevice.md) \*dev) |
|  | Check if a regulator is enabled. |
| int | [regulator\_disable](group__regulator__interface.md#gaac417fbf6e30bbbfbd5ea5029a8ef298) (const struct [device](structdevice.md) \*dev) |
|  | Disable a regulator. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [regulator\_count\_voltages](group__regulator__interface.md#ga96bf136ff2deca774931ca27300b03a6) (const struct [device](structdevice.md) \*dev) |
|  | Obtain the number of supported voltage levels. |
| static int | [regulator\_list\_voltage](group__regulator__interface.md#ga62d9ea1d7dc2987101cf31b324ca7c51) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*volt\_uv) |
|  | Obtain the value of a voltage given an index. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [regulator\_is\_supported\_voltage](group__regulator__interface.md#ga31b42ddfe94fee47158632f355ad864c) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_uv, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_uv) |
|  | Check if a voltage within a window is supported. |
| int | [regulator\_set\_voltage](group__regulator__interface.md#ga2c2b345da9029013edbf59fd8c565d85) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_uv, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_uv) |
|  | Set the output voltage. |
| static int | [regulator\_get\_voltage](group__regulator__interface.md#gaa0114ee43a137ee98f98f5bce93d8579) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*volt\_uv) |
|  | Obtain output voltage. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [regulator\_count\_current\_limits](group__regulator__interface.md#ga27de51302b5222f860457c5b8bd494d6) (const struct [device](structdevice.md) \*dev) |
|  | Obtain the number of supported current limit levels. |
| static int | [regulator\_list\_current\_limit](group__regulator__interface.md#gaf12002954c6fc0ab9689f4dd2ec39518) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*current\_ua) |
|  | Obtain the value of a current limit given an index. |
| int | [regulator\_set\_current\_limit](group__regulator__interface.md#ga2ccf66175b37754e2c21f341ecb2acbd) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_ua, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_ua) |
|  | Set output current limit. |
| static int | [regulator\_get\_current\_limit](group__regulator__interface.md#ga88c3ddeed962b5368713ad8fef0e7d7a) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*curr\_ua) |
|  | Get output current limit. |
| int | [regulator\_set\_mode](group__regulator__interface.md#ga1877bac62c2b81ee37deb86bfae302af) (const struct [device](structdevice.md) \*dev, [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) mode) |
|  | Set mode. |
| static int | [regulator\_get\_mode](group__regulator__interface.md#ga9bc0fc7ba4bd2ed2548bff25cf4badfe) (const struct [device](structdevice.md) \*dev, [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) \*mode) |
|  | Get mode. |
| static int | [regulator\_set\_active\_discharge](group__regulator__interface.md#ga8fb061502d0e94c4fe7a18c5a84d4af3) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) active\_discharge) |
|  | Set active discharge setting. |
| static int | [regulator\_get\_active\_discharge](group__regulator__interface.md#ga58d9e06c6da52a9733b3979d72915ab3) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*active\_discharge) |
|  | Get active discharge setting. |
| static int | [regulator\_get\_error\_flags](group__regulator__interface.md#ga9133662844a20eaf703d6d075347c62f) (const struct [device](structdevice.md) \*dev, [regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get active error flags. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [regulator.h](regulator_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
