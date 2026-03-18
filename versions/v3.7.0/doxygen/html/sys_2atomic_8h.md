---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sys_2atomic_8h.html
original_path: doxygen/html/sys_2atomic_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/sys/atomic_types.h](atomic__types_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/sys/atomic_builtin.h](atomic__builtin_8h_source.md)>`

[Go to the source code of this file.](sys_2atomic_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ATOMIC\_INIT](group__atomic__apis.md#gaadfbba86627ee7eeb07e04f712550f73)(i) |
|  | Initialize an atomic variable. |
| #define | [ATOMIC\_PTR\_INIT](group__atomic__apis.md#ga7366802f7b11d3c5f9487f4fea9fc4d7)(p) |
|  | Initialize an atomic pointer variable. |
| #define | [ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)(num\_bits) |
|  | This macro computes the number of atomic variables necessary to represent a bitmap with *num\_bits*. |
| #define | [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)(name, num\_bits) |
|  | Define an array of atomic variables. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae) (const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit) |
|  | Atomically test a bit. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_test\_and\_clear\_bit](group__atomic__apis.md#ga53159437721084da0ec8ee70ec212472) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit) |
|  | Atomically test and clear a bit. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit) |
|  | Atomically set a bit. |
| static void | [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit) |
|  | Atomically clear a bit. |
| static void | [atomic\_set\_bit](group__atomic__apis.md#ga17a3961ba7610ad6e595e602f70344a0) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit) |
|  | Atomically set a bit. |
| static void | [atomic\_set\_bit\_to](group__atomic__apis.md#gad749f16ca51ffc26e7303988de1b8dbf) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) val) |
|  | Atomically set a bit to a given value. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) old\_value, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) new\_value) |
|  | Atomic compare-and-set. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_ptr\_cas](group__atomic__apis.md#ga98f03db5ef2b36ff3412506a7f6d9558) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) old\_value, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) new\_value) |
|  | Atomic compare-and-set with pointer values. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_add](group__atomic__apis.md#ga518c07595daaca29a9e53071ed59c9c0) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic addition. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_sub](group__atomic__apis.md#ga84ab58fd0a6dbbf1bf675722b5900bd7) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic subtraction. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
|  | Atomic increment. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_dec](group__atomic__apis.md#gac260f0efbd970717eae4ac3bb493a0c4) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
|  | Atomic decrement. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa) (const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
|  | Atomic get. |
| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | [atomic\_ptr\_get](group__atomic__apis.md#ga250c4672ce7749261bdb8b2f0c767da2) (const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target) |
|  | Atomic get a pointer value. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_set](group__atomic__apis.md#ga5f0555245d8932c2e7f7e94575e1a095) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic get-and-set. |
| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | [atomic\_ptr\_set](group__atomic__apis.md#ga3a57fd7f76f84e0f5800878b8f81fc35) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) value) |
|  | Atomic get-and-set for pointer values. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_clear](group__atomic__apis.md#ga879b5f540c25fd09f1b84563e3dc8a91) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
|  | Atomic clear. |
| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | [atomic\_ptr\_clear](group__atomic__apis.md#ga587e3134cd8176e7b1c00361711ee2df) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target) |
|  | Atomic clear of a pointer value. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_or](group__atomic__apis.md#ga1564a44a260e7d0d02e30ae045a99764) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic bitwise inclusive OR. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_xor](group__atomic__apis.md#ga18592bcf38d667fb9b428f81ea691bd4) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic bitwise exclusive OR (XOR). |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_and](group__atomic__apis.md#ga4bc1f6a6f5d98eef742b4541d235811d) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic bitwise AND. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_nand](group__atomic__apis.md#ga3e954286e40de73e45598a00a0a2b864) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic bitwise NAND. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [atomic.h](sys_2atomic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
