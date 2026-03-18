---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structtee__shm.html
original_path: doxygen/html/structtee__shm.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tee\_shm Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [TEE Interface](group__tee__interface.md)

Tee shared memory structure.
[More...](#details)

`#include <[tee.h](tee_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#ab761c1d3d5e64c21725eff97521b4b86) |
|  | [out] pointer to the device driver structure |
| void \* | [addr](#a65446310f73319aa5f8e100e4d83198e) |
|  | [out] shared buffer pointer |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [size](#a02fe0fd69f1e8d5650cfa116136ea9ca) |
|  | [out] shared buffer size |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#ac2738d87cbe439f093cad67a375c2807) |
|  | [out] shared buffer flags |

## Detailed Description

Tee shared memory structure.

## Field Documentation

## [◆ ](#a65446310f73319aa5f8e100e4d83198e)addr

| void\* tee\_shm::addr |
| --- |

[out] shared buffer pointer

## [◆ ](#ab761c1d3d5e64c21725eff97521b4b86)dev

| const struct [device](structdevice.md)\* tee\_shm::dev |
| --- |

[out] pointer to the device driver structure

## [◆ ](#ac2738d87cbe439f093cad67a375c2807)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_shm::flags |
| --- |

[out] shared buffer flags

## [◆ ](#a02fe0fd69f1e8d5650cfa116136ea9ca)size

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) tee\_shm::size |
| --- |

[out] shared buffer size

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[tee.h](tee_8h_source.md)

- [tee\_shm](structtee__shm.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
