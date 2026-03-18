---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsmp__transport__api__t.html
original_path: doxygen/html/structsmp__transport__api__t.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_transport\_api\_t Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr transport SMP API](group__mcumgr__transport__smp.md)

Function pointers of SMP transport functions, if a handler is NULL then it is not supported/implemented.
[More...](#details)

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [smp\_transport\_out\_fn](group__mcumgr__transport__smp.md#ga4da3579b031ba6a90448ad9248f52155) | [output](#aa779d7dcea55385963a0c0054b95f9da) |
|  | Transport's send function. |
| [smp\_transport\_get\_mtu\_fn](group__mcumgr__transport__smp.md#ga2085e89b99428a61596d90e084d7c5e2) | [get\_mtu](#a798d89289e913d966cbc1b914fe47952) |
|  | Transport's get-MTU function. |
| [smp\_transport\_ud\_copy\_fn](group__mcumgr__transport__smp.md#ga840da7e00d590459b656dcbe0dd6f6f4) | [ud\_copy](#ae3153c9a27123de510e4ee83cc9c0c62) |
|  | Transport buffer user\_data copy function. |
| [smp\_transport\_ud\_free\_fn](group__mcumgr__transport__smp.md#ga0f249aa3fed3044d9bad811e92e4135c) | [ud\_free](#acc98fb8a8e7e674ec907939831de1809) |
|  | Transport buffer user\_data free function. |
| [smp\_transport\_query\_valid\_check\_fn](group__mcumgr__transport__smp.md#ga77d54c0bd6afc69f73613575b671e089) | [query\_valid\_check](#a811fefe5287c7050701705f8db51f16d) |
|  | Transport's check function for if a query is valid. |

## Detailed Description

Function pointers of SMP transport functions, if a handler is NULL then it is not supported/implemented.

## Field Documentation

## [◆ ](#a798d89289e913d966cbc1b914fe47952)get\_mtu

| [smp\_transport\_get\_mtu\_fn](group__mcumgr__transport__smp.md#ga2085e89b99428a61596d90e084d7c5e2) smp\_transport\_api\_t::get\_mtu |
| --- |

Transport's get-MTU function.

## [◆ ](#aa779d7dcea55385963a0c0054b95f9da)output

| [smp\_transport\_out\_fn](group__mcumgr__transport__smp.md#ga4da3579b031ba6a90448ad9248f52155) smp\_transport\_api\_t::output |
| --- |

Transport's send function.

## [◆ ](#a811fefe5287c7050701705f8db51f16d)query\_valid\_check

| [smp\_transport\_query\_valid\_check\_fn](group__mcumgr__transport__smp.md#ga77d54c0bd6afc69f73613575b671e089) smp\_transport\_api\_t::query\_valid\_check |
| --- |

Transport's check function for if a query is valid.

## [◆ ](#ae3153c9a27123de510e4ee83cc9c0c62)ud\_copy

| [smp\_transport\_ud\_copy\_fn](group__mcumgr__transport__smp.md#ga840da7e00d590459b656dcbe0dd6f6f4) smp\_transport\_api\_t::ud\_copy |
| --- |

Transport buffer user\_data copy function.

## [◆ ](#acc98fb8a8e7e674ec907939831de1809)ud\_free

| [smp\_transport\_ud\_free\_fn](group__mcumgr__transport__smp.md#ga0f249aa3fed3044d9bad811e92e4135c) smp\_transport\_api\_t::ud\_free |
| --- |

Transport buffer user\_data free function.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/transport/[smp.h](mgmt_2mcumgr_2transport_2smp_8h_source.md)

- [smp\_transport\_api\_t](structsmp__transport__api__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
