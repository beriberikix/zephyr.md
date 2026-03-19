---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structtee__param.html
original_path: doxygen/html/structtee__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tee\_param Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [TEE Interface](group__tee__interface.md)

Tee parameter.
[More...](#details)

`#include <[tee.h](tee_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [attr](#ac8ced719ce993735e22d68ca50f54e5b) |
|  | attributes |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [a](#aea8916d1bc24ab5a56f59fa4608f1a38) |
|  | if a memref, offset into the shared memory object, else a value |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [b](#a22785fe00950c3a7d6353c39b12d72a8) |
|  | if a memref, size of the buffer, else a value parameter |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [c](#a79b39571785949e32629216742e34d72) |
|  | if a memref, shared memory identifier, else a value parameter |

## Detailed Description

Tee parameter.

[attr](#ac8ced719ce993735e22d68ca50f54e5b) & TEE\_PARAM\_ATTR\_TYPE\_MASK indicates if memref or value is used in the union. TEE\_PARAM\_ATTR\_TYPE\_VALUE\_\* indicates value and TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_\* indicates memref. TEE\_PARAM\_ATTR\_TYPE\_NONE indicates that none of the members are used.

Shared memory is allocated with TEE\_IOC\_SHM\_ALLOC which returns an identifier representing the shared memory object. A memref can reference a part of a shared memory by specifying an offset ([a](#aea8916d1bc24ab5a56f59fa4608f1a38)) and size ([b](#a22785fe00950c3a7d6353c39b12d72a8)) of the object. To supply the entire shared memory object set the offset ([a](#aea8916d1bc24ab5a56f59fa4608f1a38)) to 0 and size ([b](#a22785fe00950c3a7d6353c39b12d72a8)) to the previously returned size of the object.

## Field Documentation

## [◆ ](#aea8916d1bc24ab5a56f59fa4608f1a38)a

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) tee\_param::a |
| --- |

if a memref, offset into the shared memory object, else a value

## [◆ ](#ac8ced719ce993735e22d68ca50f54e5b)attr

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) tee\_param::attr |
| --- |

attributes

## [◆ ](#a22785fe00950c3a7d6353c39b12d72a8)b

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) tee\_param::b |
| --- |

if a memref, size of the buffer, else a value parameter

## [◆ ](#a79b39571785949e32629216742e34d72)c

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) tee\_param::c |
| --- |

if a memref, shared memory identifier, else a value parameter

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[tee.h](tee_8h_source.md)

- [tee\_param](structtee__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
