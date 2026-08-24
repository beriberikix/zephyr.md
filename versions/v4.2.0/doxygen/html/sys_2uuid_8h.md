---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/sys_2uuid_8h.html
original_path: doxygen/html/sys_2uuid_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uuid.h File Reference

Utility functions for the generation and parsing of Universal Unique Identifier.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](sys_2uuid_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [uuid](structuuid.md) |
|  | Binary representation of a UUID. [More...](structuuid.md#details) |

| Macros | |
| --- | --- |
| #define | [UUID\_SIZE](group__uuid.md#ga5db91c4b658dc322b42959cb5c851020)   16U |
|  | Number of bytes in the binary representation of a UUID. |
| #define | [UUID\_STR\_LEN](group__uuid.md#ga6d37dd9ad8391595db1b71ca2103a228)   37U |
|  | Length of the UUID canonical string representation, including the NULL terminator. |
| #define | [UUID\_BASE64\_LEN](group__uuid.md#ga1d71eb34412c3e04f9f85bb8320548d6)   25U |
|  | Length of the UUID base64 string representation, including the NULL terminator. |
| #define | [UUID\_BASE64URL\_LEN](group__uuid.md#gae28fa917e2f1ad587da4cf901f0de94a)   23U |
|  | Length of the UUID base64 URL and filename safe string representation, including the NULL terminator. |

| Functions | |
| --- | --- |
| int | [uuid\_generate\_v4](group__uuid.md#ga1e1e2f008f5ac3366bf474de27d42b66) (struct [uuid](structuuid.md) \*out) |
|  | Generate a UUIDv4. |
| int | [uuid\_generate\_v5](group__uuid.md#ga6f692b733f600e0346317f3d25d84409) (const struct [uuid](structuuid.md) \*ns, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_size, struct [uuid](structuuid.md) \*out) |
|  | Generate a UUIDv5. |
| int | [uuid\_copy](group__uuid.md#ga1fd6f837800e0bd9bd0e4c4e5891568e) (const struct [uuid](structuuid.md) \*data, struct [uuid](structuuid.md) \*out) |
|  | Copy an UUID into another UUID. |
| int | [uuid\_from\_buffer](group__uuid.md#gacf4a46349ed1a7a6a44b3cc84c687bc1) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data[16U], struct [uuid](structuuid.md) \*out) |
|  | Create a uuid\_t from a binary (big-endian) formatted UUID. |
| int | [uuid\_from\_string](group__uuid.md#gadf6084420d0ee8cc41a522ebb2c71e7d) (const char data[37U], struct [uuid](structuuid.md) \*out) |
|  | Parse a UUID from its canonical (RFC9562) string representation. |
| int | [uuid\_to\_buffer](group__uuid.md#ga2562309a55cbd49b70e1c60a761fb08f) (const struct [uuid](structuuid.md) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) out[16U]) |
|  | Create a uuid\_t from a binary (big-endian) formatted UUID. |
| int | [uuid\_to\_string](group__uuid.md#gaac4b9f9b243c9ecbeac94f0b4947ede1) (const struct [uuid](structuuid.md) \*data, char out[37U]) |
|  | Convert a UUID to its canonical (RFC9562) string representation. |
| int | [uuid\_to\_base64](group__uuid.md#ga2c73bd8b52693f1c28dbbc10e145e098) (const struct [uuid](structuuid.md) \*data, char out[25U]) |
|  | Convert a UUID to its base 64 (RFC 3548, RFC 4648) string representation. |
| int | [uuid\_to\_base64url](group__uuid.md#ga68dcce718b9e98d4873fe7c40d99ad4c) (const struct [uuid](structuuid.md) \*data, char out[23U]) |
|  | Convert a UUID to its base 64 (RFC 4648 sec. |

## Detailed Description

Utility functions for the generation and parsing of Universal Unique Identifier.

This driver is compliant with RFC9562: [https://datatracker.ietf.org/doc/rfc9562/](https://datatracker.ietf.org/doc/rfc9562/)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [uuid.h](sys_2uuid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
