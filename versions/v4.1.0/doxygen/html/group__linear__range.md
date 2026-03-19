---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__linear__range.html
original_path: doxygen/html/group__linear__range.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Linear Range

[Utilities](group__utilities.md)

The linear range API maps values in a linear range to a range index.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [linear\_range](structlinear__range.md) |
|  | Linear range. [More...](structlinear__range.md#details) |

| Macros | |
| --- | --- |
| #define | [LINEAR\_RANGE\_INIT](#ga3f936124e81ea46aa5f8dd4d9bde9ece)(\_min, \_step, \_min\_idx, \_max\_idx) |
|  | Initializer for [Linear Range](group__linear__range.md "Linear Range"). |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [linear\_range\_values\_count](#gae02547c7922e5a36c815dc89bc1df128) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Obtain the number of values representable in a linear range. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [linear\_range\_group\_values\_count](#ga67b24d9d6e7088daf39020c8c02f8d96) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) r\_cnt) |
|  | Obtain the number of values representable by a group of linear ranges. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [linear\_range\_get\_max\_value](#gae6315858afa73945bc44d8c5c997645c) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Obtain the maximum value representable by a linear range. |
| static int | [linear\_range\_get\_value](#ga72b800d1c6af44cb247130139176a59e) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*val) |
|  | Obtain value given a linear range index. |
| static int | [linear\_range\_group\_get\_value](#gac054f5cc2aad11de223fa968ebeaa55c) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) r\_cnt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*val) |
|  | Obtain value in a group given a linear range index. |
| static int | [linear\_range\_get\_index](#ga90610e42e63eb4290e5ae6187a53143f) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*idx) |
|  | Obtain index given a value. |
| static int | [linear\_range\_group\_get\_index](#gab8b661f6ed1caba2ab4796a02c1b24a8) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) r\_cnt, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*idx) |
|  | Obtain index in a group given a value. |
| static int | [linear\_range\_get\_win\_index](#ga6c06a26d629f4d7a195188e7c5df5db1) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val\_min, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val\_max, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*idx) |
|  | Obtain index given a window of values. |
| static int | [linear\_range\_group\_get\_win\_index](#ga11dc5408be53887e9ddf992b574aa16c) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) r\_cnt, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val\_min, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val\_max, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*idx) |
|  | Obtain index in a group given a value that must be within a window of values. |

## Detailed Description

The linear range API maps values in a linear range to a range index.

A linear range can be fully defined by four parameters:

- Minimum value
- Step value
- Minimum index value
- Maximum index value

For example, in a voltage regulator, supported voltages typically map to a register index value like this:

- 1000uV: 0x00
- 1250uV: 0x01
- 1500uV: 0x02
- ...
- 3000uV: 0x08

In this case, we have:

- Minimum value: 1000uV
- Step value: 250uV
- Minimum index value: 0x00
- Maximum index value: 0x08

A linear range may also be constant, that is, step set to zero.

It is often the case where the same device has discontinuous linear ranges. The API offers utility functions to deal with groups of linear ranges as well.

Implementation uses fixed-width integers. Range is limited to [INT32\_MIN, INT32\_MAX], while number of indices is limited to UINT16\_MAX.

Original idea borrowed from Linux.

## Macro Definition Documentation

## [◆ ](#ga3f936124e81ea46aa5f8dd4d9bde9ece)LINEAR\_RANGE\_INIT

| #define LINEAR\_RANGE\_INIT | ( |  | *\_min*, |
| --- | --- | --- | --- |
|  |  |  | *\_step*, |
|  |  |  | *\_min\_idx*, |
|  |  |  | *\_max\_idx* ) |

`#include <[linear_range.h](linear__range_8h.md)>`

**Value:**

{ \

.min = (\_min), \

.step = (\_step), \

.min\_idx = (\_min\_idx), \

.max\_idx = (\_max\_idx), \

}

Initializer for [Linear Range](group__linear__range.md "Linear Range").

Parameters
:   | \_min | Minimum value in range. |
    | --- | --- |
    | \_step | Step value. |
    | \_min\_idx | Minimum index. |
    | \_max\_idx | Maximum index. |

## Function Documentation

## [◆ ](#ga90610e42e63eb4290e5ae6187a53143f)linear\_range\_get\_index()

| | int linear\_range\_get\_index | ( | const struct [linear\_range](structlinear__range.md) \* | *r*, | | --- | --- | --- | --- | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *val*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *idx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[linear_range.h](linear__range_8h.md)>`

Obtain index given a value.

If the value falls outside the range, the nearest index will be stored and -ERANGE returned. That is, if the value falls below or above the range, the index will take the minimum or maximum value, respectively. For constant ranges, the minimum index will be returned.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | Linear range instance. |
    | --- | --- | --- |
    |  | val | Value. |
    | [out] | idx | Where index will be stored. |

Return values
:   | 0 | If value falls within the range. |
    | --- | --- |
    | -ERANGE | If the value falls out of the range. |

## [◆ ](#gae6315858afa73945bc44d8c5c997645c)linear\_range\_get\_max\_value()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) linear\_range\_get\_max\_value | ( | const struct [linear\_range](structlinear__range.md) \* | *r* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[linear_range.h](linear__range_8h.md)>`

Obtain the maximum value representable by a linear range.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | Linear range instance. |
    | --- | --- | --- |

Returns
:   Maximum value representable by `r`.

## [◆ ](#ga72b800d1c6af44cb247130139176a59e)linear\_range\_get\_value()

| | int linear\_range\_get\_value | ( | const struct [linear\_range](structlinear__range.md) \* | *r*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *idx*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[linear_range.h](linear__range_8h.md)>`

Obtain value given a linear range index.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | Linear range instance. |
    | --- | --- | --- |
    |  | idx | Range index. |
    | [out] | val | Where value will be stored. |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -EINVAL | If index is out of range. |

## [◆ ](#ga6c06a26d629f4d7a195188e7c5df5db1)linear\_range\_get\_win\_index()

| | int linear\_range\_get\_win\_index | ( | const struct [linear\_range](structlinear__range.md) \* | *r*, | | --- | --- | --- | --- | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *val\_min*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *val\_max*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *idx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[linear_range.h](linear__range_8h.md)>`

Obtain index given a window of values.

If the window of values does not intersect with the range, -EINVAL will be returned. If intersection is partial (any of the window edges does not intersect), the nearest index will be stored and -ERANGE returned.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | Linear range instance. |
    | --- | --- | --- |
    |  | val\_min | Minimum window value. |
    |  | val\_max | Maximum window value. |
    | [out] | idx | Where index will be stored. |

Return values
:   | 0 | If a valid index is found within linear range. |
    | --- | --- |
    | -ERANGE | If the given window of values falls partially out of the linear range. |
    | -EINVAL | If the given window of values does not intersect with the linear range or if they are too narrow. |

## [◆ ](#gab8b661f6ed1caba2ab4796a02c1b24a8)linear\_range\_group\_get\_index()

| | int linear\_range\_group\_get\_index | ( | const struct [linear\_range](structlinear__range.md) \* | *r*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *r\_cnt*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *val*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *idx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[linear_range.h](linear__range_8h.md)>`

Obtain index in a group given a value.

This function works the same way as [linear\_range\_get\_index()](#ga90610e42e63eb4290e5ae6187a53143f), but considering all ranges in the group.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | Linear range instances. |
    | --- | --- | --- |
    |  | r\_cnt | Number of linear range instances. |
    |  | val | Value. |
    | [out] | idx | Where index will be stored. |

Return values
:   | 0 | If value falls within the range group. |
    | --- | --- |
    | -ERANGE | If the value falls out of the range group. |
    | -EINVAL | If input is not valid (i.e. zero groups). |

## [◆ ](#gac054f5cc2aad11de223fa968ebeaa55c)linear\_range\_group\_get\_value()

| | int linear\_range\_group\_get\_value | ( | const struct [linear\_range](structlinear__range.md) \* | *r*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *r\_cnt*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *idx*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[linear_range.h](linear__range_8h.md)>`

Obtain value in a group given a linear range index.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | Array of linear range instances. |
    | --- | --- | --- |
    |  | r\_cnt | Number of linear range instances. |
    |  | idx | Range index. |
    | [out] | val | Where value will be stored. |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -EINVAL | If index is out of range. |

## [◆ ](#ga11dc5408be53887e9ddf992b574aa16c)linear\_range\_group\_get\_win\_index()

| | int linear\_range\_group\_get\_win\_index | ( | const struct [linear\_range](structlinear__range.md) \* | *r*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *r\_cnt*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *val\_min*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *val\_max*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *idx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[linear_range.h](linear__range_8h.md)>`

Obtain index in a group given a value that must be within a window of values.

This function works the same way as [linear\_range\_get\_win\_index()](#ga6c06a26d629f4d7a195188e7c5df5db1), but considering all ranges in the group.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | Linear range instances. |
    | --- | --- | --- |
    |  | r\_cnt | Number of linear range instances. |
    |  | val\_min | Minimum window value. |
    |  | val\_max | Maximum window value. |
    | [out] | idx | Where index will be stored. |

Return values
:   | 0 | If a valid index is found within linear range group. |
    | --- | --- |
    | -ERANGE | If the given window of values falls partially out of the linear range group. |
    | -EINVAL | If the given window of values does not intersect with the linear range group, if they are too narrow, or if input is invalid (i.e. zero groups). |

## [◆ ](#ga67b24d9d6e7088daf39020c8c02f8d96)linear\_range\_group\_values\_count()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) linear\_range\_group\_values\_count | ( | const struct [linear\_range](structlinear__range.md) \* | *r*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *r\_cnt* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[linear_range.h](linear__range_8h.md)>`

Obtain the number of values representable by a group of linear ranges.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | Array of linear range instances. |
    | --- | --- | --- |
    |  | r\_cnt | Number of linear range instances. |

Returns
:   Number of ranges representable by the `r` group.

## [◆ ](#gae02547c7922e5a36c815dc89bc1df128)linear\_range\_values\_count()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) linear\_range\_values\_count | ( | const struct [linear\_range](structlinear__range.md) \* | *r* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[linear_range.h](linear__range_8h.md)>`

Obtain the number of values representable in a linear range.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | Linear range instance. |
    | --- | --- | --- |

Returns
:   Number of ranges representable by `r`.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
