---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gpio__intel_8h_source.html
original_path: doxygen/html/gpio__intel_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_intel.h

[Go to the documentation of this file.](gpio__intel_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

[ 7](structgpio__acpi__res.md)struct [gpio\_acpi\_res](structgpio__acpi__res.md) {

[ 8](structgpio__acpi__res.md#af89b2304ea9cfabeddc487d84c2297a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_pins](structgpio__acpi__res.md#af89b2304ea9cfabeddc487d84c2297a9);

[ 9](structgpio__acpi__res.md#a85c88312042b134a2f80f63853c086fa) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pad\_base](structgpio__acpi__res.md#a85c88312042b134a2f80f63853c086fa);

[ 10](structgpio__acpi__res.md#ac0f83a85d2ff41fbc9f1b598d1ca4036) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [host\_owner\_reg](structgpio__acpi__res.md#ac0f83a85d2ff41fbc9f1b598d1ca4036);

[ 11](structgpio__acpi__res.md#a53c789cbddde23ec54c39af61ee433fa) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pad\_owner\_reg](structgpio__acpi__res.md#a53c789cbddde23ec54c39af61ee433fa);

[ 12](structgpio__acpi__res.md#aa912c56ae09d4ef0fc0467b03091b8ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [intr\_stat\_reg](structgpio__acpi__res.md#aa912c56ae09d4ef0fc0467b03091b8ef);

[ 13](structgpio__acpi__res.md#a82ef9374bee9aeda5b825cf5179057e8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [base\_num](structgpio__acpi__res.md#a82ef9374bee9aeda5b825cf5179057e8);

[ 14](structgpio__acpi__res.md#ad4738c083000ac8f4aa6770082c2ddbb) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [reg\_base](structgpio__acpi__res.md#ad4738c083000ac8f4aa6770082c2ddbb);

15};

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[gpio\_acpi\_res](structgpio__acpi__res.md)

**Definition** gpio\_intel.h:7

[gpio\_acpi\_res::pad\_owner\_reg](structgpio__acpi__res.md#a53c789cbddde23ec54c39af61ee433fa)

uint32\_t pad\_owner\_reg

**Definition** gpio\_intel.h:11

[gpio\_acpi\_res::base\_num](structgpio__acpi__res.md#a82ef9374bee9aeda5b825cf5179057e8)

uint16\_t base\_num

**Definition** gpio\_intel.h:13

[gpio\_acpi\_res::pad\_base](structgpio__acpi__res.md#a85c88312042b134a2f80f63853c086fa)

uint32\_t pad\_base

**Definition** gpio\_intel.h:9

[gpio\_acpi\_res::intr\_stat\_reg](structgpio__acpi__res.md#aa912c56ae09d4ef0fc0467b03091b8ef)

uint32\_t intr\_stat\_reg

**Definition** gpio\_intel.h:12

[gpio\_acpi\_res::host\_owner\_reg](structgpio__acpi__res.md#ac0f83a85d2ff41fbc9f1b598d1ca4036)

uint32\_t host\_owner\_reg

**Definition** gpio\_intel.h:10

[gpio\_acpi\_res::reg\_base](structgpio__acpi__res.md#ad4738c083000ac8f4aa6770082c2ddbb)

uintptr\_t reg\_base

**Definition** gpio\_intel.h:14

[gpio\_acpi\_res::num\_pins](structgpio__acpi__res.md#af89b2304ea9cfabeddc487d84c2297a9)

uint8\_t num\_pins

**Definition** gpio\_intel.h:8

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_intel.h](gpio__intel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
