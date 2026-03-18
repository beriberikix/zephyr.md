---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hypercall_8h.html
original_path: doxygen/html/hypercall_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hypercall.h File Reference

[Go to the source code of this file.](hypercall_8h_source.md)

| Functions | |
| --- | --- |
| int | [HYPERVISOR\_console\_io](#a122b9d9c3cba8c0339502e9b230acee4) (int op, int cnt, char \*str) |
| int | [HYPERVISOR\_sched\_op](#a2493899aa03561ca6161f541093390a7) (int op, void \*param) |
| int | [HYPERVISOR\_event\_channel\_op](#a5b16a018f61a14ecf292227b84bce133) (int op, void \*param) |
| int | [HYPERVISOR\_hvm\_op](#ab33fe3d856e5aaaf38eb4c707fd5a684) (int op, void \*param) |
| int | [HYPERVISOR\_memory\_op](#a49970e12da5e083aa26228880c23c1c2) (int op, void \*param) |
| int | [HYPERVISOR\_grant\_table\_op](#aa13c544d327b7c24987fd54089f10e78) (int op, void \*uop, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int count) |

## Function Documentation

## [◆ ](#a122b9d9c3cba8c0339502e9b230acee4)HYPERVISOR\_console\_io()

| int HYPERVISOR\_console\_io | ( | int | *op*, |
| --- | --- | --- | --- |
|  |  | int | *cnt*, |
|  |  | char \* | *str* ) |

## [◆ ](#a5b16a018f61a14ecf292227b84bce133)HYPERVISOR\_event\_channel\_op()

| int HYPERVISOR\_event\_channel\_op | ( | int | *op*, |
| --- | --- | --- | --- |
|  |  | void \* | *param* ) |

## [◆ ](#aa13c544d327b7c24987fd54089f10e78)HYPERVISOR\_grant\_table\_op()

| int HYPERVISOR\_grant\_table\_op | ( | int | *op*, |
| --- | --- | --- | --- |
|  |  | void \* | *uop*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *count* ) |

## [◆ ](#ab33fe3d856e5aaaf38eb4c707fd5a684)HYPERVISOR\_hvm\_op()

| int HYPERVISOR\_hvm\_op | ( | int | *op*, |
| --- | --- | --- | --- |
|  |  | void \* | *param* ) |

## [◆ ](#a49970e12da5e083aa26228880c23c1c2)HYPERVISOR\_memory\_op()

| int HYPERVISOR\_memory\_op | ( | int | *op*, |
| --- | --- | --- | --- |
|  |  | void \* | *param* ) |

## [◆ ](#a2493899aa03561ca6161f541093390a7)HYPERVISOR\_sched\_op()

| int HYPERVISOR\_sched\_op | ( | int | *op*, |
| --- | --- | --- | --- |
|  |  | void \* | *param* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [hypercall.h](hypercall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
