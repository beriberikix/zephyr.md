---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnavigation__data.html
original_path: doxygen/html/structnavigation__data.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

navigation\_data Struct Reference

[Utilities](group__utilities.md) » [Navigation](group__navigation.md)

Navigation data structure.
[More...](#details)

`#include <[navigation.h](navigation_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [latitude](#a02d9f8cea5fe68810123bb2bf554d59c) |
|  | Latitudal position in nanodegrees (0 to +-180E9). |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [longitude](#a530eb9c4e3750bbb03b26256794d0914) |
|  | Longitudal position in nanodegrees (0 to +-180E9). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [bearing](#af9887a29823fc3e083dbd14d1f6cfce1) |
|  | Bearing angle in millidegrees (0 to 360E3). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [speed](#a5fd501c07c21e66217a7634d7d607d1d) |
|  | Speed in millimeters per second. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [altitude](#addd80254be4619c4ea7707f9c9bc434e) |
|  | Altitude in millimeters. |

## Detailed Description

Navigation data structure.

The structure describes the momentary navigation details of a point relative to a sphere (commonly Earth)

## Field Documentation

## [◆ ](#addd80254be4619c4ea7707f9c9bc434e)altitude

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) navigation\_data::altitude |
| --- |

Altitude in millimeters.

## [◆ ](#af9887a29823fc3e083dbd14d1f6cfce1)bearing

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) navigation\_data::bearing |
| --- |

Bearing angle in millidegrees (0 to 360E3).

## [◆ ](#a02d9f8cea5fe68810123bb2bf554d59c)latitude

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) navigation\_data::latitude |
| --- |

Latitudal position in nanodegrees (0 to +-180E9).

## [◆ ](#a530eb9c4e3750bbb03b26256794d0914)longitude

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) navigation\_data::longitude |
| --- |

Longitudal position in nanodegrees (0 to +-180E9).

## [◆ ](#a5fd501c07c21e66217a7634d7d607d1d)speed

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) navigation\_data::speed |
| --- |

Speed in millimeters per second.

---

The documentation for this struct was generated from the following file:

- zephyr/data/[navigation.h](navigation_8h_source.md)

- [navigation\_data](structnavigation__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
