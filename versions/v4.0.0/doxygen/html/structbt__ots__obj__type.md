---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__ots__obj__type.html
original_path: doxygen/html/structbt__ots__obj__type.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_ots\_obj\_type Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Object Transfer Service (OTS)](group__bt__ots.md)

Type of an OTS object.
[More...](#details)

`#include <[ots.h](ots_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct [bt\_uuid](structbt__uuid.md)   [uuid](#a89a8dbe566579422df503dd577ea8d42) |  |
| struct [bt\_uuid\_16](structbt__uuid__16.md)   [uuid\_16](#ae39b7a368314d1a771cf3573d2077095) |  |
| struct [bt\_uuid\_128](structbt__uuid__128.md)   [uuid\_128](#aedf0e5d45f6f4912a8eeae077eda17be) |  |
| }; |  |

## Detailed Description

Type of an OTS object.

## Field Documentation

## [◆ ](#a64cec1015024fa9cb7ff605d955e4bd1)[union]

| union { ... } [bt\_ots\_obj\_type](structbt__ots__obj__type.md) |
| --- |

## [◆ ](#a89a8dbe566579422df503dd577ea8d42)uuid

| struct [bt\_uuid](structbt__uuid.md) bt\_ots\_obj\_type::uuid |
| --- |

## [◆ ](#aedf0e5d45f6f4912a8eeae077eda17be)uuid\_128

| struct [bt\_uuid\_128](structbt__uuid__128.md) bt\_ots\_obj\_type::uuid\_128 |
| --- |

## [◆ ](#ae39b7a368314d1a771cf3573d2077095)uuid\_16

| struct [bt\_uuid\_16](structbt__uuid__16.md) bt\_ots\_obj\_type::uuid\_16 |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/[ots.h](ots_8h_source.md)

- [bt\_ots\_obj\_type](structbt__ots__obj__type.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
