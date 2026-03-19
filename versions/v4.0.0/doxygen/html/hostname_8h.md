---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hostname_8h.html
original_path: doxygen/html/hostname_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hostname.h File Reference

Hostname configuration definitions.
[More...](#details)

[Go to the source code of this file.](hostname_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NET\_HOSTNAME\_MAX\_LEN](group__net__hostname.md#ga9dda37a09616f2eb1bcdcb76cd868a0f) |
|  | Maximum hostname length. |

| Functions | |
| --- | --- |
| static const char \* | [net\_hostname\_get](group__net__hostname.md#ga8870e80f16f934d1d8a86ea6bddbaf0b) (void) |
|  | Get the device hostname. |
| static int | [net\_hostname\_set](group__net__hostname.md#ga2131a7beddae249cc5a93392c44a1b27) (char \*host, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Set the device hostname. |
| static void | [net\_hostname\_init](group__net__hostname.md#ga96adbfaa629b6d450f06e19678eba9bc) (void) |
|  | Initialize and set the device hostname. |
| static int | [net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hostname\_postfix, int postfix\_len) |
|  | Set the device hostname postfix. |
| static int | [net\_hostname\_set\_postfix\_str](group__net__hostname.md#ga2b9d6f604afcde27b6d1543495e2ba8b) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hostname\_postfix, int postfix\_len) |
|  | Set the postfix string for the network hostname. |

## Detailed Description

Hostname configuration definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [hostname.h](hostname_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
