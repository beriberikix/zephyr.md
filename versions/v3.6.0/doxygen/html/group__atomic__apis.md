---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__atomic__apis.html
original_path: doxygen/html/group__atomic__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Atomic Services APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [ATOMIC\_INIT](#gaadfbba86627ee7eeb07e04f712550f73)(i) |
|  | Initialize an atomic variable. |
| #define | [ATOMIC\_PTR\_INIT](#ga7366802f7b11d3c5f9487f4fea9fc4d7)(p) |
|  | Initialize an atomic pointer variable. |
| #define | [ATOMIC\_BITMAP\_SIZE](#gafac28874aaad3bcec72c693186e988cb)(num\_bits) |
|  | This macro computes the number of atomic variables necessary to represent a bitmap with *num\_bits*. |
| #define | [ATOMIC\_DEFINE](#ga249c575db9764486197709b327f7370e)(name, num\_bits) |
|  | Define an array of atomic variables. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_test\_bit](#ga190ddc108f45e7649689753c08658eae) (const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit) |
|  | Atomically test a bit. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_test\_and\_clear\_bit](#ga53159437721084da0ec8ee70ec212472) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit) |
|  | Atomically test and clear a bit. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_test\_and\_set\_bit](#ga7ff45e13aa5f8be5d7a550e49f5c720b) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit) |
|  | Atomically set a bit. |
| static void | [atomic\_clear\_bit](#ga1c1693d524c49d11fd32b323a39d718e) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit) |
|  | Atomically clear a bit. |
| static void | [atomic\_set\_bit](#ga17a3961ba7610ad6e595e602f70344a0) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit) |
|  | Atomically set a bit. |
| static void | [atomic\_set\_bit\_to](#gad749f16ca51ffc26e7303988de1b8dbf) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) val) |
|  | Atomically set a bit to a given value. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_cas](#gab879da5aa1ffcc317adc664c016586f7) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) old\_value, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) new\_value) |
|  | Atomic compare-and-set. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_ptr\_cas](#ga98f03db5ef2b36ff3412506a7f6d9558) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) old\_value, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) new\_value) |
|  | Atomic compare-and-set with pointer values. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_add](#ga518c07595daaca29a9e53071ed59c9c0) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic addition. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_sub](#ga84ab58fd0a6dbbf1bf675722b5900bd7) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic subtraction. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_inc](#gaae47a9cbe5a6534967b417f602b37ac2) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
|  | Atomic increment. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_dec](#gac260f0efbd970717eae4ac3bb493a0c4) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
|  | Atomic decrement. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_get](#ga33bb426a17535bd1022895a7e44b32fa) (const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
|  | Atomic get. |
| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | [atomic\_ptr\_get](#ga250c4672ce7749261bdb8b2f0c767da2) (const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target) |
|  | Atomic get a pointer value. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_set](#ga5f0555245d8932c2e7f7e94575e1a095) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic get-and-set. |
| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | [atomic\_ptr\_set](#ga3a57fd7f76f84e0f5800878b8f81fc35) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) value) |
|  | Atomic get-and-set for pointer values. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_clear](#ga879b5f540c25fd09f1b84563e3dc8a91) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
|  | Atomic clear. |
| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | [atomic\_ptr\_clear](#ga587e3134cd8176e7b1c00361711ee2df) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target) |
|  | Atomic clear of a pointer value. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_or](#ga1564a44a260e7d0d02e30ae045a99764) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic bitwise inclusive OR. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_xor](#ga18592bcf38d667fb9b428f81ea691bd4) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic bitwise exclusive OR (XOR). |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_and](#ga4bc1f6a6f5d98eef742b4541d235811d) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic bitwise AND. |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_nand](#ga3e954286e40de73e45598a00a0a2b864) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
|  | Atomic bitwise NAND. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gafac28874aaad3bcec72c693186e988cb)ATOMIC\_BITMAP\_SIZE

| #define ATOMIC\_BITMAP\_SIZE | ( |  | *num\_bits* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

**Value:**

([ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(num\_bits, ATOMIC\_BITS) / ATOMIC\_BITS)

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:288

This macro computes the number of atomic variables necessary to represent a bitmap with *num\_bits*.

Parameters
:   | num\_bits | Number of bits. |
    | --- | --- |

## [◆ ](#ga249c575db9764486197709b327f7370e)ATOMIC\_DEFINE

| #define ATOMIC\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *num\_bits* ) |

`#include <[atomic.h](atomic_8h.md)>`

**Value:**

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) name[[ATOMIC\_BITMAP\_SIZE](#gafac28874aaad3bcec72c693186e988cb)(num\_bits)]

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[ATOMIC\_BITMAP\_SIZE](#gafac28874aaad3bcec72c693186e988cb)

#define ATOMIC\_BITMAP\_SIZE(num\_bits)

This macro computes the number of atomic variables necessary to represent a bitmap with num\_bits.

**Definition** atomic.h:90

Define an array of atomic variables.

This macro defines an array of atomic variables containing at least *num\_bits* bits.

Note
:   If used from file scope, the bits of the array are initialized to zero; if used from within a function, the bits are left uninitialized.

Parameters
:   | name | Name of array of atomic variables. |
    | --- | --- |
    | num\_bits | Number of bits needed. |

## [◆ ](#gaadfbba86627ee7eeb07e04f712550f73)ATOMIC\_INIT

| #define ATOMIC\_INIT | ( |  | *i* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

**Value:**

(i)

Initialize an atomic variable.

This macro can be used to initialize an atomic variable. For example,

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) my\_var = [ATOMIC\_INIT](#gaadfbba86627ee7eeb07e04f712550f73)(75);

[ATOMIC\_INIT](#gaadfbba86627ee7eeb07e04f712550f73)

#define ATOMIC\_INIT(i)

Initialize an atomic variable.

**Definition** atomic.h:59

Parameters
:   | i | Value to assign to atomic variable. |
    | --- | --- |

## [◆ ](#ga7366802f7b11d3c5f9487f4fea9fc4d7)ATOMIC\_PTR\_INIT

| #define ATOMIC\_PTR\_INIT | ( |  | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

**Value:**

(p)

Initialize an atomic pointer variable.

This macro can be used to initialize an atomic pointer variable. For example,

[atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) my\_ptr = [ATOMIC\_PTR\_INIT](#ga7366802f7b11d3c5f9487f4fea9fc4d7)(&data);

[atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7)

void \* atomic\_ptr\_t

**Definition** atomic\_types.h:17

[ATOMIC\_PTR\_INIT](#ga7366802f7b11d3c5f9487f4fea9fc4d7)

#define ATOMIC\_PTR\_INIT(p)

Initialize an atomic pointer variable.

**Definition** atomic.h:70

Parameters
:   | p | Pointer value to assign to atomic pointer variable. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga518c07595daaca29a9e53071ed59c9c0)atomic\_add()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_add | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

`#include <[atomic.h](atomic_8h.md)>`

Atomic addition.

This routine performs an atomic addition on *target*.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |
    | value | Value to add. |

Returns
:   Previous value of *target*.

## [◆ ](#ga4bc1f6a6f5d98eef742b4541d235811d)atomic\_and()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_and | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

`#include <[atomic.h](atomic_8h.md)>`

Atomic bitwise AND.

This routine atomically sets *target* to the bitwise AND of *target* and *value*.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |
    | value | Value to AND. |

Returns
:   Previous value of *target*.

## [◆ ](#gab879da5aa1ffcc317adc664c016586f7)atomic\_cas()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) atomic\_cas | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *old\_value*, |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *new\_value* ) |

`#include <[atomic.h](atomic_8h.md)>`

Atomic compare-and-set.

This routine performs an atomic compare-and-set on *target*. If the current value of *target* equals *old\_value*, *target* is set to *new\_value*. If the current value of *target* does not equal *old\_value*, *target* is left unchanged.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |
    | old\_value | Original value to compare against. |
    | new\_value | New value to store. |

Returns
:   true if *new\_value* is written, false otherwise.

## [◆ ](#ga879b5f540c25fd09f1b84563e3dc8a91)atomic\_clear()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_clear | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

Atomic clear.

This routine atomically sets *target* to zero and returns its previous value. (Hence, it is equivalent to atomic\_set(target, 0).)

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |

Returns
:   Previous value of *target*.

## [◆ ](#ga1c1693d524c49d11fd32b323a39d718e)atomic\_clear\_bit()

| | void atomic\_clear\_bit | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | int | *bit* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

Atomically clear a bit.

Atomically clear bit number *bit* of *target*. The target may be a single atomic variable or an array of them.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable or array. |
    | --- | --- |
    | bit | Bit number (starting from 0). |

## [◆ ](#gac260f0efbd970717eae4ac3bb493a0c4)atomic\_dec()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_dec | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

Atomic decrement.

This routine performs an atomic decrement by 1 on *target*.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |

Returns
:   Previous value of *target*.

## [◆ ](#ga33bb426a17535bd1022895a7e44b32fa)atomic\_get()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_get | ( | const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

Atomic get.

This routine performs an atomic read on *target*.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |

Returns
:   Value of *target*.

## [◆ ](#gaae47a9cbe5a6534967b417f602b37ac2)atomic\_inc()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_inc | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

Atomic increment.

This routine performs an atomic increment by 1 on *target*.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |

Returns
:   Previous value of *target*.

## [◆ ](#ga3e954286e40de73e45598a00a0a2b864)atomic\_nand()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_nand | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

`#include <[atomic.h](atomic_8h.md)>`

Atomic bitwise NAND.

This routine atomically sets *target* to the bitwise NAND of *target* and *value*. (This operation is equivalent to target = ~(target & value).)

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |
    | value | Value to NAND. |

Returns
:   Previous value of *target*.

## [◆ ](#ga1564a44a260e7d0d02e30ae045a99764)atomic\_or()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_or | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

`#include <[atomic.h](atomic_8h.md)>`

Atomic bitwise inclusive OR.

This routine atomically sets *target* to the bitwise inclusive OR of *target* and *value*.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |
    | value | Value to OR. |

Returns
:   Previous value of *target*.

## [◆ ](#ga98f03db5ef2b36ff3412506a7f6d9558)atomic\_ptr\_cas()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) atomic\_ptr\_cas | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | *old\_value*, |
|  |  | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | *new\_value* ) |

`#include <[atomic.h](atomic_8h.md)>`

Atomic compare-and-set with pointer values.

This routine performs an atomic compare-and-set on *target*. If the current value of *target* equals *old\_value*, *target* is set to *new\_value*. If the current value of *target* does not equal *old\_value*, *target* is left unchanged.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |
    | old\_value | Original value to compare against. |
    | new\_value | New value to store. |

Returns
:   true if *new\_value* is written, false otherwise.

## [◆ ](#ga587e3134cd8176e7b1c00361711ee2df)atomic\_ptr\_clear()

| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) atomic\_ptr\_clear | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

Atomic clear of a pointer value.

This routine atomically sets *target* to zero and returns its previous value. (Hence, it is equivalent to atomic\_set(target, 0).)

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |

Returns
:   Previous value of *target*.

## [◆ ](#ga250c4672ce7749261bdb8b2f0c767da2)atomic\_ptr\_get()

| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) atomic\_ptr\_get | ( | const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

Atomic get a pointer value.

This routine performs an atomic read on *target*.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of pointer variable. |
    | --- | --- |

Returns
:   Value of *target*.

## [◆ ](#ga3a57fd7f76f84e0f5800878b8f81fc35)atomic\_ptr\_set()

| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) atomic\_ptr\_set | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | *value* ) |

`#include <[atomic.h](atomic_8h.md)>`

Atomic get-and-set for pointer values.

This routine atomically sets *target* to *value* and returns the previous value of *target*.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |
    | value | Value to write to *target*. |

Returns
:   Previous value of *target*.

## [◆ ](#ga5f0555245d8932c2e7f7e94575e1a095)atomic\_set()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_set | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

`#include <[atomic.h](atomic_8h.md)>`

Atomic get-and-set.

This routine atomically sets *target* to *value* and returns the previous value of *target*.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |
    | value | Value to write to *target*. |

Returns
:   Previous value of *target*.

## [◆ ](#ga17a3961ba7610ad6e595e602f70344a0)atomic\_set\_bit()

| | void atomic\_set\_bit | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | int | *bit* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

Atomically set a bit.

Atomically set bit number *bit* of *target*. The target may be a single atomic variable or an array of them.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable or array. |
    | --- | --- |
    | bit | Bit number (starting from 0). |

## [◆ ](#gad749f16ca51ffc26e7303988de1b8dbf)atomic\_set\_bit\_to()

| | void atomic\_set\_bit\_to | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | int | *bit*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

Atomically set a bit to a given value.

Atomically set bit number *bit* of *target* to value *val*. The target may be a single atomic variable or an array of them.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable or array. |
    | --- | --- |
    | bit | Bit number (starting from 0). |
    | val | true for 1, false for 0. |

## [◆ ](#ga84ab58fd0a6dbbf1bf675722b5900bd7)atomic\_sub()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_sub | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

`#include <[atomic.h](atomic_8h.md)>`

Atomic subtraction.

This routine performs an atomic subtraction on *target*.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |
    | value | Value to subtract. |

Returns
:   Previous value of *target*.

## [◆ ](#ga53159437721084da0ec8ee70ec212472)atomic\_test\_and\_clear\_bit()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) atomic\_test\_and\_clear\_bit | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | int | *bit* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

Atomically test and clear a bit.

Atomically clear bit number *bit* of *target* and return its old value. The target may be a single atomic variable or an array of them.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable or array. |
    | --- | --- |
    | bit | Bit number (starting from 0). |

Returns
:   false if the bit was already cleared, true if it wasn't.

## [◆ ](#ga7ff45e13aa5f8be5d7a550e49f5c720b)atomic\_test\_and\_set\_bit()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) atomic\_test\_and\_set\_bit | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | int | *bit* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

Atomically set a bit.

Atomically set bit number *bit* of *target* and return its old value. The target may be a single atomic variable or an array of them.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable or array. |
    | --- | --- |
    | bit | Bit number (starting from 0). |

Returns
:   true if the bit was already set, false if it wasn't.

## [◆ ](#ga190ddc108f45e7649689753c08658eae)atomic\_test\_bit()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) atomic\_test\_bit | ( | const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | int | *bit* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[atomic.h](atomic_8h.md)>`

Atomically test a bit.

This routine tests whether bit number *bit* of *target* is set or not. The target may be a single atomic variable or an array of them.

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

Parameters
:   | target | Address of atomic variable or array. |
    | --- | --- |
    | bit | Bit number (starting from 0). |

Returns
:   true if the bit was set, false if it wasn't.

## [◆ ](#ga18592bcf38d667fb9b428f81ea691bd4)atomic\_xor()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_xor | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

`#include <[atomic.h](atomic_8h.md)>`

Atomic bitwise exclusive OR (XOR).

Note
:   As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

This routine atomically sets *target* to the bitwise exclusive OR (XOR) of *target* and *value*.

Parameters
:   | target | Address of atomic variable. |
    | --- | --- |
    | value | Value to XOR |

Returns
:   Previous value of *target*.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
