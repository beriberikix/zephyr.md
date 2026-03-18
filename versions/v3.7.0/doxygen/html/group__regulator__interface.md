---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__regulator__interface.html
original_path: doxygen/html/group__regulator__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Regulator Interface

[Device Driver APIs](group__io__interfaces.md)

Regulator Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [ADP5360 Devicetree helpers.](group__regulator__adp5360.md) |
|  | [AXP192 Devicetree helpers.](group__regulator__axp192.md) |
|  | [Devicetree helpers](group__regulator__nxp__vref.md) |
|  | [MAX20335 Devicetree helpers.](group__regulator__max20335.md) |
|  | [NPM1100 Devicetree helpers.](group__regulator__npm1100.md) |
|  | [NPM1300 Devicetree helpers.](group__regulator__npm1300.md) |
|  | [NPM6001 Devicetree helpers.](group__regulator__npm6001.md) |
|  | [Regulator Parent Interface](group__regulator__parent__interface.md) |
|  | Regulator Parent Interface. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [regulator\_dvs\_state\_t](#ga9a15a21a532e497713724f42052b1dbd) |
|  | Opaque type to store regulator DVS states. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [regulator\_mode\_t](#ga1971bd21b504979a0cecab16048a0d03) |
|  | Opaque type to store regulator modes. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [regulator\_error\_flags\_t](#ga31dae130509d28ee41602ab16ab31a90) |
|  | Opaque bit map for regulator error flags (see [REGULATOR\_ERRORS](#REGULATOR_ERRORS)). |

| Functions | |
| --- | --- |
| int | [regulator\_enable](#ga06e3109b9607521fe07686c6d601e460) (const struct [device](structdevice.md) \*dev) |
|  | Enable a regulator. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [regulator\_is\_enabled](#ga28744a6cabadfe5a22bc96792c8ad124) (const struct [device](structdevice.md) \*dev) |
|  | Check if a regulator is enabled. |
| int | [regulator\_disable](#gaac417fbf6e30bbbfbd5ea5029a8ef298) (const struct [device](structdevice.md) \*dev) |
|  | Disable a regulator. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [regulator\_count\_voltages](#ga96bf136ff2deca774931ca27300b03a6) (const struct [device](structdevice.md) \*dev) |
|  | Obtain the number of supported voltage levels. |
| static int | [regulator\_list\_voltage](#ga62d9ea1d7dc2987101cf31b324ca7c51) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*volt\_uv) |
|  | Obtain the value of a voltage given an index. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [regulator\_is\_supported\_voltage](#ga31b42ddfe94fee47158632f355ad864c) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_uv, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_uv) |
|  | Check if a voltage within a window is supported. |
| int | [regulator\_set\_voltage](#ga2c2b345da9029013edbf59fd8c565d85) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_uv, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_uv) |
|  | Set the output voltage. |
| static int | [regulator\_get\_voltage](#gaa0114ee43a137ee98f98f5bce93d8579) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*volt\_uv) |
|  | Obtain output voltage. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [regulator\_count\_current\_limits](#ga27de51302b5222f860457c5b8bd494d6) (const struct [device](structdevice.md) \*dev) |
|  | Obtain the number of supported current limit levels. |
| static int | [regulator\_list\_current\_limit](#gaf12002954c6fc0ab9689f4dd2ec39518) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*current\_ua) |
|  | Obtain the value of a current limit given an index. |
| int | [regulator\_set\_current\_limit](#ga2ccf66175b37754e2c21f341ecb2acbd) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_ua, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_ua) |
|  | Set output current limit. |
| static int | [regulator\_get\_current\_limit](#ga88c3ddeed962b5368713ad8fef0e7d7a) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*curr\_ua) |
|  | Get output current limit. |
| int | [regulator\_set\_mode](#ga1877bac62c2b81ee37deb86bfae302af) (const struct [device](structdevice.md) \*dev, [regulator\_mode\_t](#ga1971bd21b504979a0cecab16048a0d03) mode) |
|  | Set mode. |
| static int | [regulator\_get\_mode](#ga9bc0fc7ba4bd2ed2548bff25cf4badfe) (const struct [device](structdevice.md) \*dev, [regulator\_mode\_t](#ga1971bd21b504979a0cecab16048a0d03) \*mode) |
|  | Get mode. |
| static int | [regulator\_set\_active\_discharge](#ga8fb061502d0e94c4fe7a18c5a84d4af3) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) active\_discharge) |
|  | Set active discharge setting. |
| static int | [regulator\_get\_active\_discharge](#ga58d9e06c6da52a9733b3979d72915ab3) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*active\_discharge) |
|  | Get active discharge setting. |
| static int | [regulator\_get\_error\_flags](#ga9133662844a20eaf703d6d075347c62f) (const struct [device](structdevice.md) \*dev, [regulator\_error\_flags\_t](#ga31dae130509d28ee41602ab16ab31a90) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get active error flags. |

| Regulator error flags. | |
| --- | --- |
|  | |
| #define | [REGULATOR\_ERROR\_OVER\_VOLTAGE](#ga5e17eb919086ea6e5239a240a6ac5aa1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Voltage is too high. |
| #define | [REGULATOR\_ERROR\_OVER\_CURRENT](#ga8705a7a63b8f187d66cda98d66372b5d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Current is too high. |
| #define | [REGULATOR\_ERROR\_OVER\_TEMP](#ga9570dd992355afa6ecef9610c8c45eda)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Temperature is too high. |

## Detailed Description

Regulator Interface.

Since
:   2.4

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga8705a7a63b8f187d66cda98d66372b5d)REGULATOR\_ERROR\_OVER\_CURRENT

| #define REGULATOR\_ERROR\_OVER\_CURRENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[regulator.h](regulator_8h.md)>`

Current is too high.

## [◆ ](#ga9570dd992355afa6ecef9610c8c45eda)REGULATOR\_ERROR\_OVER\_TEMP

| #define REGULATOR\_ERROR\_OVER\_TEMP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[regulator.h](regulator_8h.md)>`

Temperature is too high.

## [◆ ](#ga5e17eb919086ea6e5239a240a6ac5aa1)REGULATOR\_ERROR\_OVER\_VOLTAGE

| #define REGULATOR\_ERROR\_OVER\_VOLTAGE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[regulator.h](regulator_8h.md)>`

Voltage is too high.

## Typedef Documentation

## [◆ ](#ga9a15a21a532e497713724f42052b1dbd)regulator\_dvs\_state\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [regulator\_dvs\_state\_t](#ga9a15a21a532e497713724f42052b1dbd) |
| --- |

`#include <[regulator.h](regulator_8h.md)>`

Opaque type to store regulator DVS states.

## [◆ ](#ga31dae130509d28ee41602ab16ab31a90)regulator\_error\_flags\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [regulator\_error\_flags\_t](#ga31dae130509d28ee41602ab16ab31a90) |
| --- |

`#include <[regulator.h](regulator_8h.md)>`

Opaque bit map for regulator error flags (see [REGULATOR\_ERRORS](#REGULATOR_ERRORS)).

## [◆ ](#ga1971bd21b504979a0cecab16048a0d03)regulator\_mode\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [regulator\_mode\_t](#ga1971bd21b504979a0cecab16048a0d03) |
| --- |

`#include <[regulator.h](regulator_8h.md)>`

Opaque type to store regulator modes.

## Function Documentation

## [◆ ](#ga27de51302b5222f860457c5b8bd494d6)regulator\_count\_current\_limits()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int regulator\_count\_current\_limits | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Obtain the number of supported current limit levels.

Each current limit level supported by a regulator gets an index, starting from zero. The total number of supported current limit levels can be used together with [regulator\_list\_current\_limit()](#gaf12002954c6fc0ab9689f4dd2ec39518) to list all supported current limit levels.

Parameters
:   | dev | Regulator device instance. |
    | --- | --- |

Returns
:   Number of supported current limits.

## [◆ ](#ga96bf136ff2deca774931ca27300b03a6)regulator\_count\_voltages()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int regulator\_count\_voltages | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Obtain the number of supported voltage levels.

Each voltage level supported by a regulator gets an index, starting from zero. The total number of supported voltage levels can be used together with [regulator\_list\_voltage()](#ga62d9ea1d7dc2987101cf31b324ca7c51) to list all supported voltage levels.

Parameters
:   | dev | Regulator device instance. |
    | --- | --- |

Returns
:   Number of supported voltages.

## [◆ ](#gaac417fbf6e30bbbfbd5ea5029a8ef298)regulator\_disable()

| int regulator\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Disable a regulator.

Release a regulator after a previous [regulator\_enable()](#ga06e3109b9607521fe07686c6d601e460) completed successfully. Regulators that are always on, or configured in devicetree with regulator-always-on will always stay enabled, and so this function will always succeed.

This must be invoked at most once for each successful [regulator\_enable()](#ga06e3109b9607521fe07686c6d601e460).

Parameters
:   | dev | Regulator device instance. |
    | --- | --- |

Return values
:   | 0 | If regulator has been successfully disabled. |
    | --- | --- |
    | -errno | Negative errno in case of failure. |
    | -ENOTSUP | If regulator disablement can not be controlled. |

## [◆ ](#ga06e3109b9607521fe07686c6d601e460)regulator\_enable()

| int regulator\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Enable a regulator.

Reference-counted request that a regulator be turned on. A regulator is considered "on" when it has reached a stable/usable state. Regulators that are always on, or configured in devicetree with regulator-always-on will always stay enabled, and so this function will always succeed.

Parameters
:   | dev | Regulator device instance |
    | --- | --- |

Return values
:   | 0 | If regulator has been successfully enabled. |
    | --- | --- |
    | -errno | Negative errno in case of failure. |
    | -ENOTSUP | If regulator enablement can not be controlled. |

## [◆ ](#ga58d9e06c6da52a9733b3979d72915ab3)regulator\_get\_active\_discharge()

| | int regulator\_get\_active\_discharge | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *active\_discharge* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Get active discharge setting.

Parameters
:   |  | dev | Regulator device instance. |
    | --- | --- | --- |
    | [out] | active\_discharge | Where active discharge will be stored. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If function is not implemented. |
    | -errno | In case of any other error. |

## [◆ ](#ga88c3ddeed962b5368713ad8fef0e7d7a)regulator\_get\_current\_limit()

| | int regulator\_get\_current\_limit | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *curr\_ua* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Get output current limit.

Parameters
:   |  | dev | Regulator device instance. |
    | --- | --- | --- |
    | [out] | curr\_ua | Where output current limit will be stored. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If function is not implemented. |
    | -errno | In case of any other error. |

## [◆ ](#ga9133662844a20eaf703d6d075347c62f)regulator\_get\_error\_flags()

| | int regulator\_get\_error\_flags | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [regulator\_error\_flags\_t](#ga31dae130509d28ee41602ab16ab31a90) \* | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Get active error flags.

Parameters
:   |  | dev | Regulator device instance. |
    | --- | --- | --- |
    | [out] | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Where error flags will be stored. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If function is not implemented. |
    | -errno | In case of any other error. |

## [◆ ](#ga9bc0fc7ba4bd2ed2548bff25cf4badfe)regulator\_get\_mode()

| | int regulator\_get\_mode | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [regulator\_mode\_t](#ga1971bd21b504979a0cecab16048a0d03) \* | *mode* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Get mode.

Parameters
:   |  | dev | Regulator device instance. |
    | --- | --- | --- |
    | [out] | mode | Where mode will be stored. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If function is not implemented. |
    | -errno | In case of any other error. |

## [◆ ](#gaa0114ee43a137ee98f98f5bce93d8579)regulator\_get\_voltage()

| | int regulator\_get\_voltage | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *volt\_uv* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Obtain output voltage.

Parameters
:   |  | dev | Regulator device instance. |
    | --- | --- | --- |
    | [out] | volt\_uv | Where configured output voltage will be stored. |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -ENOSYS | If function is not implemented. |
    | -errno | In case of any other error. |

## [◆ ](#ga28744a6cabadfe5a22bc96792c8ad124)regulator\_is\_enabled()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) regulator\_is\_enabled | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Check if a regulator is enabled.

Parameters
:   | dev | Regulator device instance. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If regulator is enabled. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If regulator is disabled. |

## [◆ ](#ga31b42ddfe94fee47158632f355ad864c)regulator\_is\_supported\_voltage()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) regulator\_is\_supported\_voltage | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *min\_uv*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *max\_uv* ) |

`#include <[regulator.h](regulator_8h.md)>`

Check if a voltage within a window is supported.

Parameters
:   | dev | Regulator device instance. |
    | --- | --- |
    | min\_uv | Minimum voltage in microvolts. |
    | max\_uv | maximum voltage in microvolts. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If voltage is supported. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If voltage is not supported. |

## [◆ ](#gaf12002954c6fc0ab9689f4dd2ec39518)regulator\_list\_current\_limit()

| | int regulator\_list\_current\_limit | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *idx*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *current\_ua* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Obtain the value of a current limit given an index.

Each current limit level supported by a regulator gets an index, starting from zero. Together with [regulator\_count\_current\_limits()](#ga27de51302b5222f860457c5b8bd494d6), this function can be used to iterate over all supported current limits.

Parameters
:   |  | dev | Regulator device instance. |
    | --- | --- | --- |
    |  | idx | Current index. |
    | [out] | current\_ua | Where current for the given `index` will be stored, in microamps. |

Return values
:   | 0 | If `index` corresponds to a supported current limit. |
    | --- | --- |
    | -EINVAL | If `index` does not correspond to a supported current limit. |

## [◆ ](#ga62d9ea1d7dc2987101cf31b324ca7c51)regulator\_list\_voltage()

| | int regulator\_list\_voltage | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *idx*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *volt\_uv* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Obtain the value of a voltage given an index.

Each voltage level supported by a regulator gets an index, starting from zero. Together with [regulator\_count\_voltages()](#ga96bf136ff2deca774931ca27300b03a6), this function can be used to iterate over all supported voltages.

Parameters
:   |  | dev | Regulator device instance. |
    | --- | --- | --- |
    |  | idx | Voltage index. |
    | [out] | volt\_uv | Where voltage for the given `index` will be stored, in microvolts. |

Return values
:   | 0 | If `index` corresponds to a supported voltage. |
    | --- | --- |
    | -EINVAL | If `index` does not correspond to a supported voltage. |

## [◆ ](#ga8fb061502d0e94c4fe7a18c5a84d4af3)regulator\_set\_active\_discharge()

| | int regulator\_set\_active\_discharge | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *active\_discharge* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Set active discharge setting.

Parameters
:   | dev | Regulator device instance. |
    | --- | --- |
    | active\_discharge | Active discharge enable or disable. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If function is not implemented. |
    | -errno | In case of any other error. |

## [◆ ](#ga2ccf66175b37754e2c21f341ecb2acbd)regulator\_set\_current\_limit()

| int regulator\_set\_current\_limit | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *min\_ua*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *max\_ua* ) |

`#include <[regulator.h](regulator_8h.md)>`

Set output current limit.

The output current limit will be configured to the closest supported output current limit. [regulator\_get\_current\_limit()](#ga88c3ddeed962b5368713ad8fef0e7d7a) can be used to obtain the actual configured current limit. Current may be limited using current-min-microamp and/or current-max-microamp in Devicetree.

Parameters
:   | dev | Regulator device instance. |
    | --- | --- |
    | min\_ua | Minimum acceptable current limit in microamps. |
    | max\_ua | Maximum acceptable current limit in microamps. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If the given current limit window is not valid. |
    | -ENOSYS | If function is not implemented. |
    | -errno | In case of any other error. |

## [◆ ](#ga1877bac62c2b81ee37deb86bfae302af)regulator\_set\_mode()

| int regulator\_set\_mode | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [regulator\_mode\_t](#ga1971bd21b504979a0cecab16048a0d03) | *mode* ) |

`#include <[regulator.h](regulator_8h.md)>`

Set mode.

Regulators can support multiple modes in order to permit different voltage configuration or better power savings. This API will apply a mode for the regulator. Allowed modes may be limited using regulator-allowed-modes devicetree property.

Parameters
:   | dev | Regulator device instance. |
    | --- | --- |
    | mode | Mode to select for this regulator. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If mode is not supported. |
    | -ENOSYS | If function is not implemented. |
    | -errno | In case of any other error. |

## [◆ ](#ga2c2b345da9029013edbf59fd8c565d85)regulator\_set\_voltage()

| int regulator\_set\_voltage | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *min\_uv*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *max\_uv* ) |

`#include <[regulator.h](regulator_8h.md)>`

Set the output voltage.

The output voltage will be configured to the closest supported output voltage. [regulator\_get\_voltage()](#gaa0114ee43a137ee98f98f5bce93d8579) can be used to obtain the actual configured voltage. The voltage will be applied to the active or selected mode. Output voltage may be limited using regulator-min-microvolt and/or regulator-max-microvolt in devicetree.

Parameters
:   | dev | Regulator device instance. |
    | --- | --- |
    | min\_uv | Minimum acceptable voltage in microvolts. |
    | max\_uv | Maximum acceptable voltage in microvolts. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If the given voltage window is not valid. |
    | -ENOSYS | If function is not implemented. |
    | -errno | In case of any other error. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
