---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dw__ace_8h_source.html
original_path: doxygen/html/dw__ace_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dw\_ace.h

[Go to the documentation of this file.](dw__ace_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DW\_ACE\_H

7#define ZEPHYR\_INCLUDE\_DRIVERS\_DW\_ACE\_H

8

9#include <[zephyr/device.h](device_8h.md)>

10

[ 11](dw__ace_8h.md#a99f66a0736502ea18deb13e0a5d9958e)typedef void (\*[irq\_enable\_t](dw__ace_8h.md#a99f66a0736502ea18deb13e0a5d9958e))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq);

[ 12](dw__ace_8h.md#a1e71aa00761ed1a478f92de8a1342564)typedef void (\*[irq\_disable\_t](dw__ace_8h.md#a1e71aa00761ed1a478f92de8a1342564))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq);

[ 13](dw__ace_8h.md#af94ebd4f440b084d94d42eed62e159cc)typedef int (\*[irq\_is\_enabled\_t](dw__ace_8h.md#af94ebd4f440b084d94d42eed62e159cc))(const struct [device](structdevice.md) \*dev, unsigned int irq);

[ 14](dw__ace_8h.md#a5b6d1259c32080069df86d5e4fd506cb)typedef int (\*[irq\_connect\_dynamic\_t](dw__ace_8h.md#a5b6d1259c32080069df86d5e4fd506cb))(const struct [device](structdevice.md) \*dev,

15 unsigned int irq, unsigned int priority,

16 void (\*routine)(const void \*parameter),

17 const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

18

[ 19](structdw__ace__v1__ictl__driver__api.md)struct [dw\_ace\_v1\_ictl\_driver\_api](structdw__ace__v1__ictl__driver__api.md) {

[ 20](structdw__ace__v1__ictl__driver__api.md#aa7984ba6960a07a33ae0746717bc45ac) [irq\_enable\_t](dw__ace_8h.md#a99f66a0736502ea18deb13e0a5d9958e) [intr\_enable](structdw__ace__v1__ictl__driver__api.md#aa7984ba6960a07a33ae0746717bc45ac);

[ 21](structdw__ace__v1__ictl__driver__api.md#a549b3e3c36f4bd632ab52ec4eee5fd80) [irq\_disable\_t](dw__ace_8h.md#a1e71aa00761ed1a478f92de8a1342564) [intr\_disable](structdw__ace__v1__ictl__driver__api.md#a549b3e3c36f4bd632ab52ec4eee5fd80);

[ 22](structdw__ace__v1__ictl__driver__api.md#ac2bbb8a07be14882b6763e58bf79be43) [irq\_is\_enabled\_t](dw__ace_8h.md#af94ebd4f440b084d94d42eed62e159cc) [intr\_is\_enabled](structdw__ace__v1__ictl__driver__api.md#ac2bbb8a07be14882b6763e58bf79be43);

23#ifdef CONFIG\_DYNAMIC\_INTERRUPTS

24 [irq\_connect\_dynamic\_t](dw__ace_8h.md#a5b6d1259c32080069df86d5e4fd506cb) intr\_connect\_dynamic;

25#endif

26};

27

28#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DW\_ACE\_H \*/

[device.h](device_8h.md)

[irq\_disable\_t](dw__ace_8h.md#a1e71aa00761ed1a478f92de8a1342564)

void(\* irq\_disable\_t)(const struct device \*dev, uint32\_t irq)

**Definition** dw\_ace.h:12

[irq\_connect\_dynamic\_t](dw__ace_8h.md#a5b6d1259c32080069df86d5e4fd506cb)

int(\* irq\_connect\_dynamic\_t)(const struct device \*dev, unsigned int irq, unsigned int priority, void(\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)

**Definition** dw\_ace.h:14

[irq\_enable\_t](dw__ace_8h.md#a99f66a0736502ea18deb13e0a5d9958e)

void(\* irq\_enable\_t)(const struct device \*dev, uint32\_t irq)

**Definition** dw\_ace.h:11

[irq\_is\_enabled\_t](dw__ace_8h.md#af94ebd4f440b084d94d42eed62e159cc)

int(\* irq\_is\_enabled\_t)(const struct device \*dev, unsigned int irq)

**Definition** dw\_ace.h:13

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[dw\_ace\_v1\_ictl\_driver\_api](structdw__ace__v1__ictl__driver__api.md)

**Definition** dw\_ace.h:19

[dw\_ace\_v1\_ictl\_driver\_api::intr\_disable](structdw__ace__v1__ictl__driver__api.md#a549b3e3c36f4bd632ab52ec4eee5fd80)

irq\_disable\_t intr\_disable

**Definition** dw\_ace.h:21

[dw\_ace\_v1\_ictl\_driver\_api::intr\_enable](structdw__ace__v1__ictl__driver__api.md#aa7984ba6960a07a33ae0746717bc45ac)

irq\_enable\_t intr\_enable

**Definition** dw\_ace.h:20

[dw\_ace\_v1\_ictl\_driver\_api::intr\_is\_enabled](structdw__ace__v1__ictl__driver__api.md#ac2bbb8a07be14882b6763e58bf79be43)

irq\_is\_enabled\_t intr\_is\_enabled

**Definition** dw\_ace.h:22

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [dw\_ace.h](dw__ace_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
