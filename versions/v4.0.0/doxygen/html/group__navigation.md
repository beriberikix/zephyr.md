---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__navigation.html
original_path: doxygen/html/group__navigation.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Navigation

[Utilities](group__utilities.md)

Navigation utilities.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [navigation\_data](structnavigation__data.md) |
|  | Navigation data structure. [More...](structnavigation__data.md#details) |

| Functions | |
| --- | --- |
| int | [navigation\_distance](#ga99b3460548c6e88cb16391ba77303829) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*distance, const struct [navigation\_data](structnavigation__data.md) \*p1, const struct [navigation\_data](structnavigation__data.md) \*p2) |
|  | Calculate the distance between two navigation points along the surface of the sphere they are relative to. |
| int | [navigation\_bearing](#ga36655c6a733ba4e96cc6bfd055a0bf8b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bearing, const struct [navigation\_data](structnavigation__data.md) \*from, const struct [navigation\_data](structnavigation__data.md) \*to) |
|  | Calculate the bearing from one navigation point to another. |

## Detailed Description

Navigation utilities.

## Function Documentation

## [◆ ](#ga36655c6a733ba4e96cc6bfd055a0bf8b)navigation\_bearing()

| int navigation\_bearing | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *bearing*, |
| --- | --- | --- | --- |
|  |  | const struct [navigation\_data](structnavigation__data.md) \* | *from*, |
|  |  | const struct [navigation\_data](structnavigation__data.md) \* | *to* ) |

`#include <[navigation.h](navigation_8h.md)>`

Calculate the bearing from one navigation point to another.

Parameters
:   | bearing | Destination for calculated bearing angle in millidegrees |
    | --- | --- |
    | from | First navigation point |
    | to | Second navigation point |

Returns
:   0 if successful
:   -EINVAL if either navigation point is invalid

## [◆ ](#ga99b3460548c6e88cb16391ba77303829)navigation\_distance()

| int navigation\_distance | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *distance*, |
| --- | --- | --- | --- |
|  |  | const struct [navigation\_data](structnavigation__data.md) \* | *p1*, |
|  |  | const struct [navigation\_data](structnavigation__data.md) \* | *p2* ) |

`#include <[navigation.h](navigation_8h.md)>`

Calculate the distance between two navigation points along the surface of the sphere they are relative to.

Parameters
:   | distance | Destination for calculated distance in millimeters |
    | --- | --- |
    | p1 | First navigation point |
    | p2 | Second navigation point |

Returns
:   0 if successful
:   -EINVAL if either navigation point is invalid

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
