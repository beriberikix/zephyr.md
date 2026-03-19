---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/shmem_8h_source.html
original_path: doxygen/html/shmem_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shmem.h

[Go to the documentation of this file.](shmem_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_SHMEM\_H\_

13#define \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_SHMEM\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16#include <[zephyr/arch/cpu.h](cpu_8h.md)>

17#include <[errno.h](errno_8h.md)>

18

[ 19](shmem_8h.md#ad073313589ccad29f911e5f965100ea0)#define SCMI\_SHMEM\_CHAN\_STATUS\_BUSY\_BIT BIT(0)

[ 20](shmem_8h.md#a4d2087d9db2b128a96537ab85d8a23bd)#define SCMI\_SHMEM\_CHAN\_FLAG\_IRQ\_BIT BIT(0)

21

22struct [scmi\_message](structscmi__message.md);

23

[ 33](shmem_8h.md#ade8c9c325245b2c2c838b86a62dea0a7)int [scmi\_shmem\_write\_message](shmem_8h.md#ade8c9c325245b2c2c838b86a62dea0a7)(const struct [device](structdevice.md) \*shmem,

34 struct [scmi\_message](structscmi__message.md) \*msg);

35

[ 45](shmem_8h.md#af0f9657082d02048c2d5df7c14833228)int [scmi\_shmem\_read\_message](shmem_8h.md#af0f9657082d02048c2d5df7c14833228)(const struct [device](structdevice.md) \*shmem,

46 struct [scmi\_message](structscmi__message.md) \*msg);

47

[ 57](shmem_8h.md#aa61c9eea220cc353b97c316bc94e0072)void [scmi\_shmem\_update\_flags](shmem_8h.md#aa61c9eea220cc353b97c316bc94e0072)(const struct [device](structdevice.md) \*shmem,

58 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

59

[ 65](shmem_8h.md#a32f0c9fdfca8450b5ab2dc33ce64896c)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [scmi\_shmem\_channel\_status](shmem_8h.md#a32f0c9fdfca8450b5ab2dc33ce64896c)(const struct [device](structdevice.md) \*shmem);

66

67#endif /\* \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_SHMEM\_H\_ \*/

[cpu.h](cpu_8h.md)

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[scmi\_shmem\_channel\_status](shmem_8h.md#a32f0c9fdfca8450b5ab2dc33ce64896c)

uint32\_t scmi\_shmem\_channel\_status(const struct device \*shmem)

Read a channel's status.

[scmi\_shmem\_update\_flags](shmem_8h.md#aa61c9eea220cc353b97c316bc94e0072)

void scmi\_shmem\_update\_flags(const struct device \*shmem, uint32\_t mask, uint32\_t val)

Update the channel flags.

[scmi\_shmem\_write\_message](shmem_8h.md#ade8c9c325245b2c2c838b86a62dea0a7)

int scmi\_shmem\_write\_message(const struct device \*shmem, struct scmi\_message \*msg)

Write a message in the SHMEM area.

[scmi\_shmem\_read\_message](shmem_8h.md#af0f9657082d02048c2d5df7c14833228)

int scmi\_shmem\_read\_message(const struct device \*shmem, struct scmi\_message \*msg)

Read a message from a SHMEM area.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[scmi\_message](structscmi__message.md)

SCMI message structure.

**Definition** protocol.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [shmem.h](shmem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
