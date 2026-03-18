---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structlwm2m__res__item.html
original_path: doxygen/html/structlwm2m__res__item.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lwm2m\_res\_item Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [LwM2M high-level API](group__lwm2m__api.md)

LwM2M resource item structure.
[More...](#details)

`#include <[lwm2m.h](lwm2m_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | [path](#ab1aecc059a1f88d84b37131884afbf2f) |
|  | Pointer to LwM2M path as a struct. |
| void \* | [value](#a7edf4cf404d4fae3ba0193fde76a66ff) |
|  | Pointer to resource value. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [size](#a7693d039248f61eaed193b131a7f6d5a) |
|  | Size of the value. |

## Detailed Description

LwM2M resource item structure.

Value type must match the target resource as no type conversion are done and the value is just memcopied.

Following C types are used for resource types:

- BOOL is [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- U8 is [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- S8 is [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)
- U16 is [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)
- S16 is [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)
- U32 is [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)
- S32 is [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)
- S64 is [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)
- TIME is [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- FLOAT is double
- OBJLNK is struct [lwm2m\_objlnk](structlwm2m__objlnk.md "LWM2M Objlnk resource type structure.")
- STRING is char \* and the null-terminator should be included in the size.
- OPAQUE is any binary data. When null-terminated string is written in OPAQUE resource, the terminator should not be included in size.

## Field Documentation

## [◆ ](#ab1aecc059a1f88d84b37131884afbf2f)path

| struct [lwm2m\_obj\_path](structlwm2m__obj__path.md)\* lwm2m\_res\_item::path |
| --- |

Pointer to LwM2M path as a struct.

## [◆ ](#a7693d039248f61eaed193b131a7f6d5a)size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lwm2m\_res\_item::size |
| --- |

Size of the value.

For string resources, it should contain the null-terminator.

## [◆ ](#a7edf4cf404d4fae3ba0193fde76a66ff)value

| void\* lwm2m\_res\_item::value |
| --- |

Pointer to resource value.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[lwm2m.h](lwm2m_8h_source.md)

- [lwm2m\_res\_item](structlwm2m__res__item.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
