---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/spi__emul_8h_source.html
original_path: doxygen/html/spi__emul_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi\_emul.h

[Go to the documentation of this file.](spi__emul_8h.md)

1/\*

2 \* Copyright 2020 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SPI\_SPI\_EMUL\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SPI\_SPI\_EMUL\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/emul.h](emul_8h.md)>

12#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>

13#include <[zephyr/sys/slist.h](slist_8h.md)>

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15

21

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

33struct spi\_msg;

34struct [spi\_emul\_api](structspi__emul__api.md);

35

[ 37](structspi__emul.md)struct [spi\_emul](structspi__emul.md) {

[ 38](structspi__emul.md#a4c49c2c9966eec74a9d010d22176bdd1) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structspi__emul.md#a4c49c2c9966eec74a9d010d22176bdd1);

39

[ 41](structspi__emul.md#a371b2447cf16752c191cc5a0aff26a57) const struct [emul](structemul.md) \*[target](structspi__emul.md#a371b2447cf16752c191cc5a0aff26a57);

42

43 /\* API provided for this device \*/

[ 44](structspi__emul.md#a96649e8ea8360ad07ebbd721f999b0e7) const struct [spi\_emul\_api](structspi__emul__api.md) \*[api](structspi__emul.md#a96649e8ea8360ad07ebbd721f999b0e7);

45

[ 50](structspi__emul.md#a4d174e7170a21e2f53c49e0da096a93e) struct [spi\_emul\_api](structspi__emul__api.md) \*[mock\_api](structspi__emul.md#a4d174e7170a21e2f53c49e0da096a93e);

51

52 /\* SPI chip-select of the emulated device \*/

[ 53](structspi__emul.md#a81450c3d7701c20da8d945e390e7cd33) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chipsel](structspi__emul.md#a81450c3d7701c20da8d945e390e7cd33);

54};

55

[ 72](group__spi__emul__interface.md#ga034da8d578cd4facdff61ce3afb19487)typedef int (\*[spi\_emul\_io\_t](group__spi__emul__interface.md#ga034da8d578cd4facdff61ce3afb19487))(const struct [emul](structemul.md) \*target, const struct [spi\_config](structspi__config.md) \*config,

73 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs);

74

[ 82](group__spi__emul__interface.md#ga6c782e1c480a9bf4640c82360e562703)int [spi\_emul\_register](group__spi__emul__interface.md#ga6c782e1c480a9bf4640c82360e562703)(const struct [device](structdevice.md) \*dev, struct [spi\_emul](structspi__emul.md) \*[emul](structemul.md));

83

[ 85](structspi__emul__api.md)struct [spi\_emul\_api](structspi__emul__api.md) {

[ 86](structspi__emul__api.md#a357c2c19a5d6eb7a14d895eb9b042085) [spi\_emul\_io\_t](group__spi__emul__interface.md#ga034da8d578cd4facdff61ce3afb19487) [io](structspi__emul__api.md#a357c2c19a5d6eb7a14d895eb9b042085);

87};

88

[ 95](group__spi__emul__interface.md#ga8b872edd18ec2911618919cc68229362)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [spi\_emul\_get\_config](group__spi__emul__interface.md#ga8b872edd18ec2911618919cc68229362)(const struct [device](structdevice.md) \*dev);

96

97#ifdef \_\_cplusplus

98}

99#endif

100

104

105#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SPI\_SPI\_EMUL\_H\_ \*/

[device.h](device_8h.md)

[spi.h](drivers_2spi_8h.md)

Public API for SPI drivers and applications.

[emul.h](emul_8h.md)

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[spi\_emul\_io\_t](group__spi__emul__interface.md#ga034da8d578cd4facdff61ce3afb19487)

int(\* spi\_emul\_io\_t)(const struct emul \*target, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Passes SPI messages to the emulator.

**Definition** spi\_emul.h:72

[spi\_emul\_register](group__spi__emul__interface.md#ga6c782e1c480a9bf4640c82360e562703)

int spi\_emul\_register(const struct device \*dev, struct spi\_emul \*emul)

Register an emulated device on the controller.

[spi\_emul\_get\_config](group__spi__emul__interface.md#ga8b872edd18ec2911618919cc68229362)

uint32\_t spi\_emul\_get\_config(const struct device \*dev)

Back door to allow an emulator to retrieve the host configuration.

[types.h](include_2zephyr_2types_8h.md)

[slist.h](slist_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:78

[spi\_buf\_set](structspi__buf__set.md)

SPI buffer array structure.

**Definition** spi.h:436

[spi\_config](structspi__config.md)

SPI controller configuration structure.

**Definition** spi.h:299

[spi\_emul\_api](structspi__emul__api.md)

Definition of the emulator API.

**Definition** spi\_emul.h:85

[spi\_emul\_api::io](structspi__emul__api.md#a357c2c19a5d6eb7a14d895eb9b042085)

spi\_emul\_io\_t io

**Definition** spi\_emul.h:86

[spi\_emul](structspi__emul.md)

Node in a linked list of emulators for SPI devices.

**Definition** spi\_emul.h:37

[spi\_emul::target](structspi__emul.md#a371b2447cf16752c191cc5a0aff26a57)

const struct emul \* target

Target emulator - REQUIRED for all bus emulators.

**Definition** spi\_emul.h:41

[spi\_emul::node](structspi__emul.md#a4c49c2c9966eec74a9d010d22176bdd1)

sys\_snode\_t node

**Definition** spi\_emul.h:38

[spi\_emul::mock\_api](structspi__emul.md#a4d174e7170a21e2f53c49e0da096a93e)

struct spi\_emul\_api \* mock\_api

A mock API that if not NULL will take precedence over the actual API.

**Definition** spi\_emul.h:50

[spi\_emul::chipsel](structspi__emul.md#a81450c3d7701c20da8d945e390e7cd33)

uint16\_t chipsel

**Definition** spi\_emul.h:53

[spi\_emul::api](structspi__emul.md#a96649e8ea8360ad07ebbd721f999b0e7)

const struct spi\_emul\_api \* api

**Definition** spi\_emul.h:44

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [spi\_emul.h](spi__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
