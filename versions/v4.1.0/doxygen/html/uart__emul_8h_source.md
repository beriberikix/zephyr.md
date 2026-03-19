---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/uart__emul_8h_source.html
original_path: doxygen/html/uart__emul_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_emul.h

[Go to the documentation of this file.](uart__emul_8h.md)

1/\*

2 \* Copyright 2024 Basalte bv

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_UART\_EMUL\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_UART\_EMUL\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/emul.h](drivers_2emul_8h.md)>

12#include <[zephyr/drivers/uart.h](drivers_2uart_8h.md)>

13#include <[zephyr/sys/slist.h](slist_8h.md)>

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15

21

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

33struct [uart\_emul\_device\_api](structuart__emul__device__api.md);

34

[ 42](group__uart__emul__interface.md#gab4b5940f6e0c55c594a9ccddae04c8ae)typedef void (\*[uart\_emul\_device\_tx\_data\_ready\_t](group__uart__emul__interface.md#gab4b5940f6e0c55c594a9ccddae04c8ae))(const struct [device](structdevice.md) \*dev, size\_t size,

43 const struct [emul](structemul.md) \*target);

44

[ 46](structuart__emul.md)struct [uart\_emul](structuart__emul.md) {

[ 47](structuart__emul.md#a5d363d3cd85e7fed7ce2f24f5a75243a) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structuart__emul.md#a5d363d3cd85e7fed7ce2f24f5a75243a);

[ 49](structuart__emul.md#ab0fa46fc3bae0c089555ca1045924e60) const struct [emul](structemul.md) \*[target](structuart__emul.md#ab0fa46fc3bae0c089555ca1045924e60);

[ 51](structuart__emul.md#a6bf13a7090376d6f3419f5c6a6ca1608) const struct [uart\_emul\_device\_api](structuart__emul__device__api.md) \*[api](structuart__emul.md#a6bf13a7090376d6f3419f5c6a6ca1608);

52};

53

[ 55](structuart__emul__device__api.md)struct [uart\_emul\_device\_api](structuart__emul__device__api.md) {

[ 56](structuart__emul__device__api.md#ab44f47b71ef668357bcc5531d287ae9a) [uart\_emul\_device\_tx\_data\_ready\_t](group__uart__emul__interface.md#gab4b5940f6e0c55c594a9ccddae04c8ae) [tx\_data\_ready](structuart__emul__device__api.md#ab44f47b71ef668357bcc5531d287ae9a);

57};

58

[ 66](group__uart__emul__interface.md#gaa457b7ca5ac20a588a6fce562221e824)int [uart\_emul\_register](group__uart__emul__interface.md#gaa457b7ca5ac20a588a6fce562221e824)(const struct [device](structdevice.md) \*dev, struct [uart\_emul](structuart__emul.md) \*[emul](structemul.md));

67

68#ifdef \_\_cplusplus

69}

70#endif

71

75

76#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_UART\_EMUL\_H\_ \*/

[device.h](device_8h.md)

[emul.h](drivers_2emul_8h.md)

[uart.h](drivers_2uart_8h.md)

Public APIs for UART drivers.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[uart\_emul\_register](group__uart__emul__interface.md#gaa457b7ca5ac20a588a6fce562221e824)

int uart\_emul\_register(const struct device \*dev, struct uart\_emul \*emul)

Register an emulated device on the controller.

[uart\_emul\_device\_tx\_data\_ready\_t](group__uart__emul__interface.md#gab4b5940f6e0c55c594a9ccddae04c8ae)

void(\* uart\_emul\_device\_tx\_data\_ready\_t)(const struct device \*dev, size\_t size, const struct emul \*target)

Define the emulation callback function signature.

**Definition** uart\_emul.h:42

[types.h](include_2zephyr_2types_8h.md)

[slist.h](slist_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:82

[uart\_emul\_device\_api](structuart__emul__device__api.md)

Definition of the emulator API.

**Definition** uart\_emul.h:55

[uart\_emul\_device\_api::tx\_data\_ready](structuart__emul__device__api.md#ab44f47b71ef668357bcc5531d287ae9a)

uart\_emul\_device\_tx\_data\_ready\_t tx\_data\_ready

**Definition** uart\_emul.h:56

[uart\_emul](structuart__emul.md)

Node in a linked list of emulators for UART devices.

**Definition** uart\_emul.h:46

[uart\_emul::node](structuart__emul.md#a5d363d3cd85e7fed7ce2f24f5a75243a)

sys\_snode\_t node

**Definition** uart\_emul.h:47

[uart\_emul::api](structuart__emul.md#a6bf13a7090376d6f3419f5c6a6ca1608)

const struct uart\_emul\_device\_api \* api

API provided for this device.

**Definition** uart\_emul.h:51

[uart\_emul::target](structuart__emul.md#ab0fa46fc3bae0c089555ca1045924e60)

const struct emul \* target

Target emulator - REQUIRED for all emulated bus nodes of any type.

**Definition** uart\_emul.h:49

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart\_emul.h](uart__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
