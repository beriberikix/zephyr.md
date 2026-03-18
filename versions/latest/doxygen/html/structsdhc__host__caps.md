---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsdhc__host__caps.html
original_path: doxygen/html/structsdhc__host__caps.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdhc\_host\_caps Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SDHC interface](group__sdhc__interface.md)

SD host controller capabilities.
[More...](#details)

`#include <[sdhc.h](sdhc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [timeout\_clk\_freq](#a3a57e12aa8f53ad1c1fb44696622f587): 5 |
|  | Timeout clock frequency. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [timeout\_clk\_unit](#a8af558ed3b7af437f1782aea9ee6794e): 1 |
|  | Timeout clock unit. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [sd\_base\_clk](#a20ada015fecce002d233fefac5c4ead4): 8 |
|  | SD base clock frequency. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [max\_blk\_len](#a97dbad3360b56a44fb1ab0d77aa90bc4): 2 |
|  | Max block length. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [bus\_8\_bit\_support](#ad09f103fc8ce341d25e1f824e97bd665): 1 |
|  | 8-bit Support for embedded device |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [bus\_4\_bit\_support](#a70b8180301c72db291b9d53bf5379655): 1 |
|  | 4 bit bus support |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [adma\_2\_support](#acfa1c5e96f2afeab40185a1ef37d7efb): 1 |
|  | ADMA2 support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [high\_spd\_support](#aaec0cd01cc4e8bf334e5c3ee151d5d98): 1 |
|  | High speed support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [sdma\_support](#a22f2877854669589f0483cf91e504df6): 1 |
|  | SDMA support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [suspend\_res\_support](#af343879ebc21f5c2d57ffa962dacb796): 1 |
|  | Suspend/Resume support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [vol\_330\_support](#ac6e2eb088ed7d7c3f3f5011ad55ba543): 1 |
|  | Voltage support 3.3V. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [vol\_300\_support](#a7fdf6832fbcc9dce7e20ee87d9063665): 1 |
|  | Voltage support 3.0V. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [vol\_180\_support](#aa39ef2d70314dbf2517bd3df6fbd4694): 1 |
|  | Voltage support 1.8V. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [address\_64\_bit\_support\_v4](#ad8e4ca0d2fb39486b469224218d2eb7b): 1 |
|  | 64-bit system address support for V4 |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [address\_64\_bit\_support\_v3](#a0f33c7e168ade12675795d2c0d5b5ea2): 1 |
|  | 64-bit system address support for V3 |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [sdio\_async\_interrupt\_support](#a6fa0525ee3b2a0313cc9b83dc820b831): 1 |
|  | Asynchronous interrupt support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [slot\_type](#a3231007bc5fcc731e97236b29333f7ee): 2 |
|  | Slot type. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [sdr50\_support](#a63dabbc7c24dc41c8103be81ee6e673f): 1 |
|  | SDR50 support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [sdr104\_support](#a3e6f73ea9df9c207cddda31de45621be): 1 |
|  | SDR104 support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ddr50\_support](#aa22adb0079aa3864df4461d841852684): 1 |
|  | DDR50 support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [uhs\_2\_support](#a146c7403d7ecbbffbd6aa0c1c4fad1b5): 1 |
|  | UHS-II support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [drv\_type\_a\_support](#a43086e5bc5d6384b8eb0709c1cf1756e): 1 |
|  | Driver type A support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [drv\_type\_c\_support](#aafcfb75fd131430df0a372e6ac2c8b34): 1 |
|  | Driver type C support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [drv\_type\_d\_support](#ad2c9e66bbd9a442d872fd559fd7a833c): 1 |
|  | Driver type D support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [retune\_timer\_count](#ab7a145bf44747d7d9e68ff743520cc2c): 4 |
|  | Timer count for re-tuning. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [sdr50\_needs\_tuning](#ac54a191e04ff6c266390d1fb8d4f84d3): 1 |
|  | Use tuning for SDR50. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [retuning\_mode](#a48680d522d417e68ec3371b3831faa01): 2 |
|  | Re-tuning mode. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [clk\_multiplier](#afffade3ad661ead23ed0f74b770172ff): 8 |
|  | Clock multiplier. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [adma3\_support](#a90a90218bcd866cbfae2354c5b0af3de): 1 |
|  | ADMA3 support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [vdd2\_180\_support](#a2f5d5859cbe06ab449f95c0a108c2250): 1 |
|  | 1.8V VDD2 support |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [hs200\_support](#a956a426ca18a02aa4c81e7b2c576531c): 1 |
|  | HS200 support. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [hs400\_support](#ad23716b3541a99dfe935e06aa9c8f256): 1 |
|  | HS400 support. |

## Detailed Description

SD host controller capabilities.

SD host controller capability flags. These flags should be set by the SDHC driver, using the [sdhc\_get\_host\_props](group__sdhc__interface.md#gab55cf88ae79e5aa9e2110b298048df8e "sdhc_get_host_props") api.

## Field Documentation

## [◆ ](#a0f33c7e168ade12675795d2c0d5b5ea2)address\_64\_bit\_support\_v3

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::address\_64\_bit\_support\_v3 |
| --- |

64-bit system address support for V3

## [◆ ](#ad8e4ca0d2fb39486b469224218d2eb7b)address\_64\_bit\_support\_v4

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::address\_64\_bit\_support\_v4 |
| --- |

64-bit system address support for V4

## [◆ ](#a90a90218bcd866cbfae2354c5b0af3de)adma3\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::adma3\_support |
| --- |

ADMA3 support.

## [◆ ](#acfa1c5e96f2afeab40185a1ef37d7efb)adma\_2\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::adma\_2\_support |
| --- |

ADMA2 support.

## [◆ ](#a70b8180301c72db291b9d53bf5379655)bus\_4\_bit\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::bus\_4\_bit\_support |
| --- |

4 bit bus support

## [◆ ](#ad09f103fc8ce341d25e1f824e97bd665)bus\_8\_bit\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::bus\_8\_bit\_support |
| --- |

8-bit Support for embedded device

## [◆ ](#afffade3ad661ead23ed0f74b770172ff)clk\_multiplier

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::clk\_multiplier |
| --- |

Clock multiplier.

## [◆ ](#aa22adb0079aa3864df4461d841852684)ddr50\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::ddr50\_support |
| --- |

DDR50 support.

## [◆ ](#a43086e5bc5d6384b8eb0709c1cf1756e)drv\_type\_a\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::drv\_type\_a\_support |
| --- |

Driver type A support.

## [◆ ](#aafcfb75fd131430df0a372e6ac2c8b34)drv\_type\_c\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::drv\_type\_c\_support |
| --- |

Driver type C support.

## [◆ ](#ad2c9e66bbd9a442d872fd559fd7a833c)drv\_type\_d\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::drv\_type\_d\_support |
| --- |

Driver type D support.

## [◆ ](#aaec0cd01cc4e8bf334e5c3ee151d5d98)high\_spd\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::high\_spd\_support |
| --- |

High speed support.

## [◆ ](#a956a426ca18a02aa4c81e7b2c576531c)hs200\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::hs200\_support |
| --- |

HS200 support.

## [◆ ](#ad23716b3541a99dfe935e06aa9c8f256)hs400\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::hs400\_support |
| --- |

HS400 support.

## [◆ ](#a97dbad3360b56a44fb1ab0d77aa90bc4)max\_blk\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::max\_blk\_len |
| --- |

Max block length.

## [◆ ](#ab7a145bf44747d7d9e68ff743520cc2c)retune\_timer\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::retune\_timer\_count |
| --- |

Timer count for re-tuning.

## [◆ ](#a48680d522d417e68ec3371b3831faa01)retuning\_mode

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::retuning\_mode |
| --- |

Re-tuning mode.

## [◆ ](#a20ada015fecce002d233fefac5c4ead4)sd\_base\_clk

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::sd\_base\_clk |
| --- |

SD base clock frequency.

## [◆ ](#a6fa0525ee3b2a0313cc9b83dc820b831)sdio\_async\_interrupt\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::sdio\_async\_interrupt\_support |
| --- |

Asynchronous interrupt support.

## [◆ ](#a22f2877854669589f0483cf91e504df6)sdma\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::sdma\_support |
| --- |

SDMA support.

## [◆ ](#a3e6f73ea9df9c207cddda31de45621be)sdr104\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::sdr104\_support |
| --- |

SDR104 support.

## [◆ ](#ac54a191e04ff6c266390d1fb8d4f84d3)sdr50\_needs\_tuning

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::sdr50\_needs\_tuning |
| --- |

Use tuning for SDR50.

## [◆ ](#a63dabbc7c24dc41c8103be81ee6e673f)sdr50\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::sdr50\_support |
| --- |

SDR50 support.

## [◆ ](#a3231007bc5fcc731e97236b29333f7ee)slot\_type

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::slot\_type |
| --- |

Slot type.

## [◆ ](#af343879ebc21f5c2d57ffa962dacb796)suspend\_res\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::suspend\_res\_support |
| --- |

Suspend/Resume support.

## [◆ ](#a3a57e12aa8f53ad1c1fb44696622f587)timeout\_clk\_freq

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::timeout\_clk\_freq |
| --- |

Timeout clock frequency.

## [◆ ](#a8af558ed3b7af437f1782aea9ee6794e)timeout\_clk\_unit

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::timeout\_clk\_unit |
| --- |

Timeout clock unit.

## [◆ ](#a146c7403d7ecbbffbd6aa0c1c4fad1b5)uhs\_2\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::uhs\_2\_support |
| --- |

UHS-II support.

## [◆ ](#a2f5d5859cbe06ab449f95c0a108c2250)vdd2\_180\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::vdd2\_180\_support |
| --- |

1.8V VDD2 support

## [◆ ](#aa39ef2d70314dbf2517bd3df6fbd4694)vol\_180\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::vol\_180\_support |
| --- |

Voltage support 1.8V.

## [◆ ](#a7fdf6832fbcc9dce7e20ee87d9063665)vol\_300\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::vol\_300\_support |
| --- |

Voltage support 3.0V.

## [◆ ](#ac6e2eb088ed7d7c3f3f5011ad55ba543)vol\_330\_support

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_caps::vol\_330\_support |
| --- |

Voltage support 3.3V.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sdhc.h](sdhc_8h_source.md)

- [sdhc\_host\_caps](structsdhc__host__caps.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
