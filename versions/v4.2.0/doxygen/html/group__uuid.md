---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__uuid.html
original_path: doxygen/html/group__uuid.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

UUID

[Utilities](group__utilities.md)

| Data Structures | |
| --- | --- |
| struct | [uuid](structuuid.md) |
|  | Binary representation of a UUID. [More...](structuuid.md#details) |

| Macros | |
| --- | --- |
| #define | [UUID\_SIZE](#ga5db91c4b658dc322b42959cb5c851020)   16U |
|  | Number of bytes in the binary representation of a UUID. |
| #define | [UUID\_STR\_LEN](#ga6d37dd9ad8391595db1b71ca2103a228)   37U |
|  | Length of the UUID canonical string representation, including the NULL terminator. |
| #define | [UUID\_BASE64\_LEN](#ga1d71eb34412c3e04f9f85bb8320548d6)   25U |
|  | Length of the UUID base64 string representation, including the NULL terminator. |
| #define | [UUID\_BASE64URL\_LEN](#gae28fa917e2f1ad587da4cf901f0de94a)   23U |
|  | Length of the UUID base64 URL and filename safe string representation, including the NULL terminator. |

| Functions | |
| --- | --- |
| int | [uuid\_generate\_v4](#ga1e1e2f008f5ac3366bf474de27d42b66) (struct [uuid](structuuid.md) \*out) |
|  | Generate a UUIDv4. |
| int | [uuid\_generate\_v5](#ga6f692b733f600e0346317f3d25d84409) (const struct [uuid](structuuid.md) \*ns, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_size, struct [uuid](structuuid.md) \*out) |
|  | Generate a UUIDv5. |
| int | [uuid\_copy](#ga1fd6f837800e0bd9bd0e4c4e5891568e) (const struct [uuid](structuuid.md) \*data, struct [uuid](structuuid.md) \*out) |
|  | Copy an UUID into another UUID. |
| int | [uuid\_from\_buffer](#gacf4a46349ed1a7a6a44b3cc84c687bc1) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data[16U], struct [uuid](structuuid.md) \*out) |
|  | Create a uuid\_t from a binary (big-endian) formatted UUID. |
| int | [uuid\_from\_string](#gadf6084420d0ee8cc41a522ebb2c71e7d) (const char data[37U], struct [uuid](structuuid.md) \*out) |
|  | Parse a UUID from its canonical (RFC9562) string representation. |
| int | [uuid\_to\_buffer](#ga2562309a55cbd49b70e1c60a761fb08f) (const struct [uuid](structuuid.md) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) out[16U]) |
|  | Create a uuid\_t from a binary (big-endian) formatted UUID. |
| int | [uuid\_to\_string](#gaac4b9f9b243c9ecbeac94f0b4947ede1) (const struct [uuid](structuuid.md) \*data, char out[37U]) |
|  | Convert a UUID to its canonical (RFC9562) string representation. |
| int | [uuid\_to\_base64](#ga2c73bd8b52693f1c28dbbc10e145e098) (const struct [uuid](structuuid.md) \*data, char out[25U]) |
|  | Convert a UUID to its base 64 (RFC 3548, RFC 4648) string representation. |
| int | [uuid\_to\_base64url](#ga68dcce718b9e98d4873fe7c40d99ad4c) (const struct [uuid](structuuid.md) \*data, char out[23U]) |
|  | Convert a UUID to its base 64 (RFC 4648 sec. |

## Detailed Description

Since
:   4.0

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga1d71eb34412c3e04f9f85bb8320548d6)UUID\_BASE64\_LEN

| #define UUID\_BASE64\_LEN   25U |
| --- |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Length of the UUID base64 string representation, including the NULL terminator.

## [◆ ](#gae28fa917e2f1ad587da4cf901f0de94a)UUID\_BASE64URL\_LEN

| #define UUID\_BASE64URL\_LEN   23U |
| --- |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Length of the UUID base64 URL and filename safe string representation, including the NULL terminator.

## [◆ ](#ga5db91c4b658dc322b42959cb5c851020)UUID\_SIZE

| #define UUID\_SIZE   16U |
| --- |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Number of bytes in the binary representation of a UUID.

## [◆ ](#ga6d37dd9ad8391595db1b71ca2103a228)UUID\_STR\_LEN

| #define UUID\_STR\_LEN   37U |
| --- |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Length of the UUID canonical string representation, including the NULL terminator.

## Function Documentation

## [◆ ](#ga1fd6f837800e0bd9bd0e4c4e5891568e)uuid\_copy()

| int uuid\_copy | ( | const struct [uuid](structuuid.md) \* | *data*, |
| --- | --- | --- | --- |
|  |  | struct [uuid](structuuid.md) \* | *out* ) |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Copy an UUID into another UUID.

Parameters
:   | data | Input data to copy. |
    | --- | --- |
    | out | Destination for the copy. |

Return values
:   | 0 | The UUID has been correctly copied in `dst` |
    | --- | --- |
    | -EINVAL | `dst` is not acceptable |

## [◆ ](#gacf4a46349ed1a7a6a44b3cc84c687bc1)uuid\_from\_buffer()

| int uuid\_from\_buffer | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data*[16U], |
| --- | --- | --- | --- |
|  |  | struct [uuid](structuuid.md) \* | *out* ) |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Create a uuid\_t from a binary (big-endian) formatted UUID.

Parameters
:   | data | The buffer where the binary UUID is stored in a big-endian order. |
    | --- | --- |
    | out | The UUID where the result will be written. |

Return values
:   | 0 | The UUID has been correctly parsed and stored in `out` |
    | --- | --- |
    | -EINVAL | `data` or `out` are not acceptable |

## [◆ ](#gadf6084420d0ee8cc41a522ebb2c71e7d)uuid\_from\_string()

| int uuid\_from\_string | ( | const char | *data*[37U], |
| --- | --- | --- | --- |
|  |  | struct [uuid](structuuid.md) \* | *out* ) |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Parse a UUID from its canonical (RFC9562) string representation.

Parameters
:   | data | A pointer to the string to be parsed. |
    | --- | --- |
    | out | The UUID where the result will be written. |

Return values
:   | 0 | The UUID has been correctly parsed and stored in `out` |
    | --- | --- |
    | -EINVAL | `input` or `out` are not acceptable |

## [◆ ](#ga1e1e2f008f5ac3366bf474de27d42b66)uuid\_generate\_v4()

| int uuid\_generate\_v4 | ( | struct [uuid](structuuid.md) \* | *out* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Generate a UUIDv4.

Parameters
:   | out | The UUID where the result will be written. |
    | --- | --- |

Return values
:   | 0 | The UUID has been correctly generated and stored in `out` |
    | --- | --- |
    | -EINVAL | `out` is not acceptable |

## [◆ ](#ga6f692b733f600e0346317f3d25d84409)uuid\_generate\_v5()

| int uuid\_generate\_v5 | ( | const struct [uuid](structuuid.md) \* | *ns*, |
| --- | --- | --- | --- |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_size*, |
|  |  | struct [uuid](structuuid.md) \* | *out* ) |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Generate a UUIDv5.

This function computes a deterministic UUID starting from a namespace UUID and binary data.

Parameters
:   | ns | A pointer to an UUID to be used as namespace. |
    | --- | --- |
    | data | A pointer to the data that will be hashed to produce the UUID. |
    | data\_size | The size of the data buffer. |
    | out | The UUID where the result will be written. |

Return values
:   | 0 | The UUID has been correctly generated and stored in `out` |
    | --- | --- |
    | -EINVAL | `out` is not acceptable |
    | -ENOMEM | Memory allocation failed |
    | -ENOTSUP | mbedTLS returned an unrecognized error |

## [◆ ](#ga2c73bd8b52693f1c28dbbc10e145e098)uuid\_to\_base64()

| int uuid\_to\_base64 | ( | const struct [uuid](structuuid.md) \* | *data*, |
| --- | --- | --- | --- |
|  |  | char | *out*[25U] ) |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Convert a UUID to its base 64 (RFC 3548, RFC 4648) string representation.

Parameters
:   | data | The UUID to convert to string. |
    | --- | --- |
    | out | A pointer to a previously allocated buffer where the result will be written. |

Return values
:   | 0 | The UUID has been converted and written in `out` |
    | --- | --- |
    | -EINVAL | `out` is not acceptable |

## [◆ ](#ga68dcce718b9e98d4873fe7c40d99ad4c)uuid\_to\_base64url()

| int uuid\_to\_base64url | ( | const struct [uuid](structuuid.md) \* | *data*, |
| --- | --- | --- | --- |
|  |  | char | *out*[23U] ) |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Convert a UUID to its base 64 (RFC 4648 sec.

5) URL and filename safe string representation.

Parameters
:   | data | The UUID to convert to string. |
    | --- | --- |
    | out | A pointer to a previously allocated buffer where the result will be written. |

Return values
:   | 0 | The UUID has been converted and written in `out` |
    | --- | --- |
    | -EINVAL | `out` is not acceptable |

## [◆ ](#ga2562309a55cbd49b70e1c60a761fb08f)uuid\_to\_buffer()

| int uuid\_to\_buffer | ( | const struct [uuid](structuuid.md) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *out*[16U] ) |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Create a uuid\_t from a binary (big-endian) formatted UUID.

Parameters
:   | data | The input UUID to store in the buffer. |
    | --- | --- |
    | out | The buffer where the binary UUID is stored in a big-endian order. |

Return values
:   | 0 | The UUID has been correctly parsed and stored in `buff` |
    | --- | --- |
    | -EINVAL | `buff` is not acceptable |

## [◆ ](#gaac4b9f9b243c9ecbeac94f0b4947ede1)uuid\_to\_string()

| int uuid\_to\_string | ( | const struct [uuid](structuuid.md) \* | *data*, |
| --- | --- | --- | --- |
|  |  | char | *out*[37U] ) |

`#include <[zephyr/sys/uuid.h](sys_2uuid_8h.md)>`

Convert a UUID to its canonical (RFC9562) string representation.

Parameters
:   | data | The UUID to convert to string. |
    | --- | --- |
    | out | A pointer to a previously allocated buffer where the result will be written. |

Return values
:   | 0 | The UUID has been converted and written in `out` |
    | --- | --- |
    | -EINVAL | `out` is not acceptable |

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
