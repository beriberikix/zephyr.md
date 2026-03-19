---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/speculation_8h.html
original_path: doxygen/html/speculation_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

speculation.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](speculation_8h_source.md)

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_array\_index\_sanitize](#aa677f654a5febe3a9b7525e4306ede09) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) index, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) array\_size) |
|  | Sanitize an array index against bounds check bypass attacks aka the Spectre V1 vulnerability. |

## Function Documentation

## [◆ ](#aa677f654a5febe3a9b7525e4306ede09)k\_array\_index\_sanitize()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_array\_index\_sanitize | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *index*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *array\_size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Sanitize an array index against bounds check bypass attacks aka the Spectre V1 vulnerability.

CPUs with speculative execution may speculate past any size checks and leak confidential data due to analysis of micro-architectural properties. This will unconditionally truncate any out-of-bounds indexes to zero in the speculative execution path using bit twiddling instead of any branch instructions.

Example usage:

if (index < size) { index = k\_array\_index\_sanitize(index, size); data = array[index]; }

Parameters
:   | index | Untrusted array index which has been validated, but not used |
    | --- | --- |
    | array\_size | Size of the array |

Returns
:   The original index value if < size, or 0

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [speculation.h](speculation_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
