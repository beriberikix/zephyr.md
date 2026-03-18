---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hvm_8h.html
original_path: doxygen/html/hvm_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hvm.h File Reference

`#include <[zephyr/xen/public/hvm/hvm_op.h](hvm__op_8h_source.md)>`  
`#include <[zephyr/xen/public/hvm/params.h](params_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`

[Go to the source code of this file.](hvm_8h_source.md)

| Functions | |
| --- | --- |
| int | [hvm\_set\_parameter](#ae375499424094b2f6f8059160456b53e) (int idx, int domid, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value) |
| int | [hvm\_get\_parameter](#aa4c66d130a846c3effc5ec3052d95f82) (int idx, int domid, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |

## Function Documentation

## [◆ ](#aa4c66d130a846c3effc5ec3052d95f82)hvm\_get\_parameter()

| int hvm\_get\_parameter | ( | int | *idx*, |
| --- | --- | --- | --- |
|  |  | int | *domid*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *value* ) |

## [◆ ](#ae375499424094b2f6f8059160456b53e)hvm\_set\_parameter()

| int hvm\_set\_parameter | ( | int | *idx*, |
| --- | --- | --- | --- |
|  |  | int | *domid*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *value* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [hvm.h](hvm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
