---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsdhc__driver__api.html
original_path: doxygen/html/structsdhc__driver__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdhc\_driver\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SDHC interface](group__sdhc__interface.md)

`#include <[sdhc.h](sdhc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [reset](#ac034dfc17e064170e76280394005c76c) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [request](#a577d162b282b2f9eeb91cf07e7578905) )(const struct [device](structdevice.md) \*dev, struct [sdhc\_command](structsdhc__command.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), struct [sdhc\_data](structsdhc__data.md) \*data) |
| int(\* | [set\_io](#adb40a93f64a1a8dc1548a4651091ecf9) )(const struct [device](structdevice.md) \*dev, struct [sdhc\_io](structsdhc__io.md) \*ios) |
| int(\* | [get\_card\_present](#a06fb6fdfd0c528056c36476f914f94c9) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [execute\_tuning](#a6075f8ef38200e700ec133fbeb8c8121) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [card\_busy](#ac642c06d5ec9f697be8fa46cede3bc64) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [get\_host\_props](#af2b83b0ea2afbbdf065b5919c6b822c2) )(const struct [device](structdevice.md) \*dev, struct [sdhc\_host\_props](structsdhc__host__props.md) \*props) |
| int(\* | [enable\_interrupt](#a42941f226f2adfe5b8275923bff434ff) )(const struct [device](structdevice.md) \*dev, [sdhc\_interrupt\_cb\_t](group__sdhc__interface.md#ga5d207e3b3d76ed9dbfa7d68a92755cbe) callback, int sources, void \*user\_data) |
| int(\* | [disable\_interrupt](#aa50466e31e01d639e459bab204cf1ee5) )(const struct [device](structdevice.md) \*dev, int sources) |

## Field Documentation

## [◆ ](#ac642c06d5ec9f697be8fa46cede3bc64)card\_busy

| int(\* sdhc\_driver\_api::card\_busy) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#aa50466e31e01d639e459bab204cf1ee5)disable\_interrupt

| int(\* sdhc\_driver\_api::disable\_interrupt) (const struct [device](structdevice.md) \*dev, int sources) |
| --- |

## [◆ ](#a42941f226f2adfe5b8275923bff434ff)enable\_interrupt

| int(\* sdhc\_driver\_api::enable\_interrupt) (const struct [device](structdevice.md) \*dev, [sdhc\_interrupt\_cb\_t](group__sdhc__interface.md#ga5d207e3b3d76ed9dbfa7d68a92755cbe) callback, int sources, void \*user\_data) |
| --- |

## [◆ ](#a6075f8ef38200e700ec133fbeb8c8121)execute\_tuning

| int(\* sdhc\_driver\_api::execute\_tuning) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a06fb6fdfd0c528056c36476f914f94c9)get\_card\_present

| int(\* sdhc\_driver\_api::get\_card\_present) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#af2b83b0ea2afbbdf065b5919c6b822c2)get\_host\_props

| int(\* sdhc\_driver\_api::get\_host\_props) (const struct [device](structdevice.md) \*dev, struct [sdhc\_host\_props](structsdhc__host__props.md) \*props) |
| --- |

## [◆ ](#a577d162b282b2f9eeb91cf07e7578905)request

| int(\* sdhc\_driver\_api::request) (const struct [device](structdevice.md) \*dev, struct [sdhc\_command](structsdhc__command.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), struct [sdhc\_data](structsdhc__data.md) \*data) |
| --- |

## [◆ ](#ac034dfc17e064170e76280394005c76c)reset

| int(\* sdhc\_driver\_api::reset) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#adb40a93f64a1a8dc1548a4651091ecf9)set\_io

| int(\* sdhc\_driver\_api::set\_io) (const struct [device](structdevice.md) \*dev, struct [sdhc\_io](structsdhc__io.md) \*ios) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sdhc.h](sdhc_8h_source.md)

- [sdhc\_driver\_api](structsdhc__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
