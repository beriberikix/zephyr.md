---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arm-smccc_8h.html
original_path: doxygen/html/arm-smccc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm-smccc.h File Reference

[Go to the source code of this file.](arm-smccc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arm\_smccc\_res](structarm__smccc__res.md) |

| Typedefs | |
| --- | --- |
| typedef struct [arm\_smccc\_res](structarm__smccc__res.md) | [arm\_smccc\_res\_t](#a2443c54e127b7804b733ba18d94378ba) |

| Enumerations | |
| --- | --- |
| enum | [arm\_smccc\_conduit](#a3c5dbd5d749131b224b0c9f4ec75fd80) { [SMCCC\_CONDUIT\_NONE](#a3c5dbd5d749131b224b0c9f4ec75fd80aad2f223e1d078eda0d631cccfb1062ff) , [SMCCC\_CONDUIT\_SMC](#a3c5dbd5d749131b224b0c9f4ec75fd80ab60fe907e7211885992f784a270887fb) , [SMCCC\_CONDUIT\_HVC](#a3c5dbd5d749131b224b0c9f4ec75fd80a8acc5857666d57a8d15ab66d6857f58d) } |

| Functions | |
| --- | --- |
| void | [arm\_smccc\_hvc](#afa839fbf56047be56c9b2d632fdcdc4e) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a0, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a1, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a2, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a3, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a4, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a5, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a6, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a7, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res) |
| void | [arm\_smccc\_smc](#a5c5b69d74ff042a8714b42d9f82b2676) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a0, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a1, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a2, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a3, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a4, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a5, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a6, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long a7, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res) |

## Typedef Documentation

## [◆ ](#a2443c54e127b7804b733ba18d94378ba)arm\_smccc\_res\_t

| typedef struct [arm\_smccc\_res](structarm__smccc__res.md) [arm\_smccc\_res\_t](#a2443c54e127b7804b733ba18d94378ba) |
| --- |

## Enumeration Type Documentation

## [◆ ](#a3c5dbd5d749131b224b0c9f4ec75fd80)arm\_smccc\_conduit

| enum [arm\_smccc\_conduit](#a3c5dbd5d749131b224b0c9f4ec75fd80) |
| --- |

| Enumerator | |
| --- | --- |
| SMCCC\_CONDUIT\_NONE |  |
| SMCCC\_CONDUIT\_SMC |  |
| SMCCC\_CONDUIT\_HVC |  |

## Function Documentation

## [◆ ](#afa839fbf56047be56c9b2d632fdcdc4e)arm\_smccc\_hvc()

| void arm\_smccc\_hvc | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a0*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a1*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a2*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a3*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a4*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a5*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a6*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a7*, |
|  |  | struct [arm\_smccc\_res](structarm__smccc__res.md) \* | *res* ) |

## [◆ ](#a5c5b69d74ff042a8714b42d9f82b2676)arm\_smccc\_smc()

| void arm\_smccc\_smc | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a0*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a1*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a2*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a3*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a4*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a5*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a6*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *a7*, |
|  |  | struct [arm\_smccc\_res](structarm__smccc__res.md) \* | *res* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [arm-smccc.h](arm-smccc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
