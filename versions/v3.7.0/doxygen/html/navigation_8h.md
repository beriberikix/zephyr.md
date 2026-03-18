---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/navigation_8h.html
original_path: doxygen/html/navigation_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

navigation.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](navigation_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [navigation\_data](structnavigation__data.md) |
|  | Navigation data structure. [More...](structnavigation__data.md#details) |

| Functions | |
| --- | --- |
| int | [navigation\_distance](group__navigation.md#ga99b3460548c6e88cb16391ba77303829) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*distance, const struct [navigation\_data](structnavigation__data.md) \*p1, const struct [navigation\_data](structnavigation__data.md) \*p2) |
|  | Calculate the distance between two navigation points along the surface of the sphere they are relative to. |
| int | [navigation\_bearing](group__navigation.md#ga36655c6a733ba4e96cc6bfd055a0bf8b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bearing, const struct [navigation\_data](structnavigation__data.md) \*from, const struct [navigation\_data](structnavigation__data.md) \*to) |
|  | Calculate the bearing from one navigation point to another. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [data](dir_f6906818b29bc0a2a087f651f21ae7e0.md)
- [navigation.h](navigation_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
