---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structfs__statvfs.html
original_path: doxygen/html/structfs__statvfs.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_statvfs Struct Reference

[Operating System Services](group__os__services.md) » [File System APIs](group__file__system__api.md)

Structure to receive volume statistics.
[More...](#details)

`#include <[fs.h](fs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [f\_bsize](#a52680f515f68ec36ce6a459f35cb2fa0) |
|  | Optimal transfer block size. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [f\_frsize](#a575b703b19d5ac15624075d64fa4bfdc) |
|  | Allocation unit size. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [f\_blocks](#a6a6d04bdeae1976a80e51c8f679e216d) |
|  | Size of FS in f\_frsize units. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [f\_bfree](#abd27b93cd5ce72d63c1b4e982cb399a6) |
|  | Number of free blocks. |

## Detailed Description

Structure to receive volume statistics.

Used to retrieve information about total and available space in the volume.

## Field Documentation

## [◆ ](#abd27b93cd5ce72d63c1b4e982cb399a6)f\_bfree

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long fs\_statvfs::f\_bfree |
| --- |

Number of free blocks.

## [◆ ](#a6a6d04bdeae1976a80e51c8f679e216d)f\_blocks

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long fs\_statvfs::f\_blocks |
| --- |

Size of FS in f\_frsize units.

## [◆ ](#a52680f515f68ec36ce6a459f35cb2fa0)f\_bsize

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long fs\_statvfs::f\_bsize |
| --- |

Optimal transfer block size.

## [◆ ](#a575b703b19d5ac15624075d64fa4bfdc)f\_frsize

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long fs\_statvfs::f\_frsize |
| --- |

Allocation unit size.

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[fs.h](fs_8h_source.md)

- [fs\_statvfs](structfs__statvfs.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
