---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/shmem_8h.html
original_path: doxygen/html/shmem_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shmem.h File Reference

SCMI SHMEM API.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/arch/cpu.h](cpu_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`

[Go to the source code of this file.](shmem_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SCMI\_SHMEM\_CHAN\_STATUS\_BUSY\_BIT](#ad073313589ccad29f911e5f965100ea0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [SCMI\_SHMEM\_CHAN\_FLAG\_IRQ\_BIT](#a4d2087d9db2b128a96537ab85d8a23bd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |

| Functions | |
| --- | --- |
| int | [scmi\_shmem\_write\_message](#ade8c9c325245b2c2c838b86a62dea0a7) (const struct [device](structdevice.md) \*shmem, struct [scmi\_message](structscmi__message.md) \*msg) |
|  | Write a message in the SHMEM area. |
| int | [scmi\_shmem\_read\_message](#af0f9657082d02048c2d5df7c14833228) (const struct [device](structdevice.md) \*shmem, struct [scmi\_message](structscmi__message.md) \*msg) |
|  | Read a message from a SHMEM area. |
| void | [scmi\_shmem\_update\_flags](#aa61c9eea220cc353b97c316bc94e0072) (const struct [device](structdevice.md) \*shmem, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Update the channel flags. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [scmi\_shmem\_channel\_status](#a32f0c9fdfca8450b5ab2dc33ce64896c) (const struct [device](structdevice.md) \*shmem) |
|  | Read a channel's status. |

## Detailed Description

SCMI SHMEM API.

## Macro Definition Documentation

## [◆ ](#a4d2087d9db2b128a96537ab85d8a23bd)SCMI\_SHMEM\_CHAN\_FLAG\_IRQ\_BIT

| #define SCMI\_SHMEM\_CHAN\_FLAG\_IRQ\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#ad073313589ccad29f911e5f965100ea0)SCMI\_SHMEM\_CHAN\_STATUS\_BUSY\_BIT

| #define SCMI\_SHMEM\_CHAN\_STATUS\_BUSY\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## Function Documentation

## [◆ ](#a32f0c9fdfca8450b5ab2dc33ce64896c)scmi\_shmem\_channel\_status()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) scmi\_shmem\_channel\_status | ( | const struct [device](structdevice.md) \* | *shmem* | ) |  |
| --- | --- | --- | --- | --- | --- |

Read a channel's status.

Parameters
:   | shmem | pointer to shmem device |
    | --- | --- |

## [◆ ](#af0f9657082d02048c2d5df7c14833228)scmi\_shmem\_read\_message()

| int scmi\_shmem\_read\_message | ( | const struct [device](structdevice.md) \* | *shmem*, |
| --- | --- | --- | --- |
|  |  | struct [scmi\_message](structscmi__message.md) \* | *msg* ) |

Read a message from a SHMEM area.

Parameters
:   | shmem | pointer to shmem device |
    | --- | --- |
    | msg | message to write the data into |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#aa61c9eea220cc353b97c316bc94e0072)scmi\_shmem\_update\_flags()

| void scmi\_shmem\_update\_flags | ( | const struct [device](structdevice.md) \* | *shmem*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mask*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

Update the channel flags.

Parameters
:   | shmem | pointer to shmem device |
    | --- | --- |
    | mask | value to negate and bitwise-and the old channel flags value |
    | val | value to bitwise and with the mask and bitwise-or with the masked old value |

## [◆ ](#ade8c9c325245b2c2c838b86a62dea0a7)scmi\_shmem\_write\_message()

| int scmi\_shmem\_write\_message | ( | const struct [device](structdevice.md) \* | *shmem*, |
| --- | --- | --- | --- |
|  |  | struct [scmi\_message](structscmi__message.md) \* | *msg* ) |

Write a message in the SHMEM area.

Parameters
:   | shmem | pointer to shmem device |
    | --- | --- |
    | msg | message to write |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno if failure |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [shmem.h](shmem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
