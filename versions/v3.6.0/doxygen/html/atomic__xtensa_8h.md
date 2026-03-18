---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/atomic__xtensa_8h.html
original_path: doxygen/html/atomic__xtensa_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic\_xtensa.h File Reference

[Go to the source code of this file.](atomic__xtensa_8h_source.md)

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_get](#a70641cc94157f8d7be8f7fc2ebb72e02) (const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
|  | Implementation of [atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa "atomic_get"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [xtensa\_cas](#a44f4f8164c1db8c54a93d36cb0457339) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*addr, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) oldval, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) newval) |
|  | Xtensa specific atomic compare-and-set (CAS). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_cas](#a6c96fd0f67a7e091035ab989e2cbbfb1) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) oldval, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) newval) |
|  | Implementation of [atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7 "atomic_cas"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_ptr\_cas](#ad949b788f6573e626a03e7b38fbd5645) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, void \*oldval, void \*newval) |
|  | Implementation of [atomic\_ptr\_cas](group__atomic__apis.md#ga98f03db5ef2b36ff3412506a7f6d9558 "atomic_ptr_cas"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_set](#a5da5d59cfe0071203119b4881c2edf25) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Implementation of [atomic\_set](group__atomic__apis.md#ga5f0555245d8932c2e7f7e94575e1a095 "atomic_set"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_add](#a734abed45962c79745a48b6468c499f1) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Implementation of [atomic\_add](group__atomic__apis.md#ga518c07595daaca29a9e53071ed59c9c0 "atomic_add"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_sub](#a59692f87d456173352f4ae3f777eb1b6) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Implementation of [atomic\_sub](group__atomic__apis.md#ga84ab58fd0a6dbbf1bf675722b5900bd7 "atomic_sub"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_inc](#a3fe69bb02a07b9445fcab9d8d7e92ea1) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
|  | Implementation of [atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2 "atomic_inc"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_dec](#aed9de77ab7834e8e0715fc2dba0c7587) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
|  | Implementation of [atomic\_dec](group__atomic__apis.md#gac260f0efbd970717eae4ac3bb493a0c4 "atomic_dec"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_or](#ae81ba87f31b1b2deee0da61697711b48) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Implementation of [atomic\_or](group__atomic__apis.md#ga1564a44a260e7d0d02e30ae045a99764 "atomic_or"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_xor](#ab9c8fddee80b212bfe3d5da8d8fd09f1) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Implementation of [atomic\_xor](group__atomic__apis.md#ga18592bcf38d667fb9b428f81ea691bd4 "atomic_xor"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_and](#a41fc4b2cdd3fa7a407c2e28a9be581ac) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Implementation of [atomic\_and](group__atomic__apis.md#ga4bc1f6a6f5d98eef742b4541d235811d "atomic_and"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_nand](#acc0cbd2fd07f3d25b6e9366e0c01829a) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Implementation of [atomic\_nand](group__atomic__apis.md#ga3e954286e40de73e45598a00a0a2b864 "atomic_nand"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \* | [atomic\_ptr\_get](#a6271fb71dfdcdc389f6703d8ffb3f99e) (const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target) |
|  | Implementation of [atomic\_ptr\_get](group__atomic__apis.md#ga250c4672ce7749261bdb8b2f0c767da2 "atomic_ptr_get"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \* | [atomic\_ptr\_set](#a1448d2fb67f55f6084114dfd17f18b5f) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, void \*value) |
|  | Implementation of [atomic\_ptr\_set](group__atomic__apis.md#ga3a57fd7f76f84e0f5800878b8f81fc35 "atomic_ptr_set"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_clear](#a88898c1c167b04955fb276e6f4b0e5f1) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
|  | Implementation of [atomic\_clear](group__atomic__apis.md#ga879b5f540c25fd09f1b84563e3dc8a91 "atomic_clear"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \* | [atomic\_ptr\_clear](#af4eeda2b2d7cae6989a1deaa370fc266) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target) |
|  | Implementation of [atomic\_ptr\_clear](group__atomic__apis.md#ga587e3134cd8176e7b1c00361711ee2df "atomic_ptr_clear"). |

## Function Documentation

## [◆ ](#a734abed45962c79745a48b6468c499f1)atomic\_add()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_add | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_add](group__atomic__apis.md#ga518c07595daaca29a9e53071ed59c9c0 "atomic_add").

## [◆ ](#a41fc4b2cdd3fa7a407c2e28a9be581ac)atomic\_and()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_and | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_and](group__atomic__apis.md#ga4bc1f6a6f5d98eef742b4541d235811d "atomic_and").

## [◆ ](#a6c96fd0f67a7e091035ab989e2cbbfb1)atomic\_cas()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) atomic\_cas | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *oldval*, | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *newval* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7 "atomic_cas").

## [◆ ](#a88898c1c167b04955fb276e6f4b0e5f1)atomic\_clear()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_clear | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_clear](group__atomic__apis.md#ga879b5f540c25fd09f1b84563e3dc8a91 "atomic_clear").

## [◆ ](#aed9de77ab7834e8e0715fc2dba0c7587)atomic\_dec()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_dec | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_dec](group__atomic__apis.md#gac260f0efbd970717eae4ac3bb493a0c4 "atomic_dec").

## [◆ ](#a70641cc94157f8d7be8f7fc2ebb72e02)atomic\_get()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_get | ( | const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa "atomic_get").

## [◆ ](#a3fe69bb02a07b9445fcab9d8d7e92ea1)atomic\_inc()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_inc | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2 "atomic_inc").

## [◆ ](#acc0cbd2fd07f3d25b6e9366e0c01829a)atomic\_nand()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_nand | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_nand](group__atomic__apis.md#ga3e954286e40de73e45598a00a0a2b864 "atomic_nand").

## [◆ ](#ae81ba87f31b1b2deee0da61697711b48)atomic\_or()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_or | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_or](group__atomic__apis.md#ga1564a44a260e7d0d02e30ae045a99764 "atomic_or").

## [◆ ](#ad949b788f6573e626a03e7b38fbd5645)atomic\_ptr\_cas()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) atomic\_ptr\_cas | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target*, | | --- | --- | --- | --- | |  |  | void \* | *oldval*, | |  |  | void \* | *newval* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_ptr\_cas](group__atomic__apis.md#ga98f03db5ef2b36ff3412506a7f6d9558 "atomic_ptr_cas").

## [◆ ](#af4eeda2b2d7cae6989a1deaa370fc266)atomic\_ptr\_clear()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \* atomic\_ptr\_clear | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_ptr\_clear](group__atomic__apis.md#ga587e3134cd8176e7b1c00361711ee2df "atomic_ptr_clear").

## [◆ ](#a6271fb71dfdcdc389f6703d8ffb3f99e)atomic\_ptr\_get()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \* atomic\_ptr\_get | ( | const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_ptr\_get](group__atomic__apis.md#ga250c4672ce7749261bdb8b2f0c767da2 "atomic_ptr_get").

## [◆ ](#a1448d2fb67f55f6084114dfd17f18b5f)atomic\_ptr\_set()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \* atomic\_ptr\_set | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target*, | | --- | --- | --- | --- | |  |  | void \* | *value* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_ptr\_set](group__atomic__apis.md#ga3a57fd7f76f84e0f5800878b8f81fc35 "atomic_ptr_set").

## [◆ ](#a5da5d59cfe0071203119b4881c2edf25)atomic\_set()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_set | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_set](group__atomic__apis.md#ga5f0555245d8932c2e7f7e94575e1a095 "atomic_set").

## [◆ ](#a59692f87d456173352f4ae3f777eb1b6)atomic\_sub()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_sub | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_sub](group__atomic__apis.md#ga84ab58fd0a6dbbf1bf675722b5900bd7 "atomic_sub").

## [◆ ](#ab9c8fddee80b212bfe3d5da8d8fd09f1)atomic\_xor()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_xor | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [atomic\_xor](group__atomic__apis.md#ga18592bcf38d667fb9b428f81ea691bd4 "atomic_xor").

## [◆ ](#a44f4f8164c1db8c54a93d36cb0457339)xtensa\_cas()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) xtensa\_cas | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *addr*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *oldval*, | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *newval* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Xtensa specific atomic compare-and-set (CAS).

Parameters
:   | addr | Address of atomic variable. |
    | --- | --- |
    | oldval | Original value to compare against. |
    | newval | New value to store. |

This utilizes SCOMPARE1 register and s32c1i instruction to perform compare-and-set atomic operation. This will unconditionally read from the atomic variable at `addr` before the comparison. This value is returned from the function.

Returns
:   The value at the memory location before CAS.

See also
:   [atomic\_cas](#a6c96fd0f67a7e091035ab989e2cbbfb1).

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [atomic\_xtensa.h](atomic__xtensa_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
