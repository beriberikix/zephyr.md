---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structqspi__dev.html
original_path: doxygen/html/structqspi__dev.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

qspi\_dev Struct Reference

`#include <[qspi_if.h](qspi__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [deinit](#a29a97c1f869a4538bcf829e3d6b3c2ab) )(void) |
| void \* | [config](#af25dcbe7de18525172dfb3fd8fc9e6fc) |
| int(\* | [init](#affbb12cc141db791e43db4e10e396a39) )(struct [qspi\_config](structqspi__config.md) \*[config](#af25dcbe7de18525172dfb3fd8fc9e6fc)) |
| int(\* | [write](#adb95f998ffb510ea555c14ca4edfdbb0) )([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int addr, const void \*data, int len) |
| int(\* | [read](#a4aa5d9952cea1d00f104a2299cee2669) )([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int addr, void \*data, int len) |
| int(\* | [hl\_read](#a591de50877cd5c1de7e4c2a4aa4f1a53) )([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int addr, void \*data, int len) |
| void(\* | [hard\_reset](#a5ffd087ce38cd40a4db3fa6dcd5872aa) )(void) |

## Field Documentation

## [◆ ](#af25dcbe7de18525172dfb3fd8fc9e6fc)config

| void\* qspi\_dev::config |
| --- |

## [◆ ](#a29a97c1f869a4538bcf829e3d6b3c2ab)deinit

| int(\* qspi\_dev::deinit) (void) |
| --- |

## [◆ ](#a5ffd087ce38cd40a4db3fa6dcd5872aa)hard\_reset

| void(\* qspi\_dev::hard\_reset) (void) |
| --- |

## [◆ ](#a591de50877cd5c1de7e4c2a4aa4f1a53)hl\_read

| int(\* qspi\_dev::hl\_read) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int addr, void \*data, int len) |
| --- |

## [◆ ](#affbb12cc141db791e43db4e10e396a39)init

| int(\* qspi\_dev::init) (struct [qspi\_config](structqspi__config.md) \*[config](#af25dcbe7de18525172dfb3fd8fc9e6fc)) |
| --- |

## [◆ ](#a4aa5d9952cea1d00f104a2299cee2669)read

| int(\* qspi\_dev::read) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int addr, void \*data, int len) |
| --- |

## [◆ ](#adb95f998ffb510ea555c14ca4edfdbb0)write

| int(\* qspi\_dev::write) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int addr, const void \*data, int len) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/wifi/nrf\_wifi/bus/[qspi\_if.h](qspi__if_8h_source.md)

- [qspi\_dev](structqspi__dev.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
