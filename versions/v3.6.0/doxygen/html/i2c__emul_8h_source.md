---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/i2c__emul_8h_source.html
original_path: doxygen/html/i2c__emul_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2c\_emul.h

[Go to the documentation of this file.](i2c__emul_8h.md)

1

6

7/\*

8 \* Copyright 2020 Google LLC

9 \* Copyright (c) 2020 Nordic Semiconductor ASA

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_I2C\_EMUL\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_I2C\_EMUL\_H\_

15

16#include <[zephyr/device.h](device_8h.md)>

17#include <[zephyr/drivers/emul.h](emul_8h.md)>

18#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h.md)>

19#include <[zephyr/sys/slist.h](slist_8h.md)>

20#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

21

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

33struct [i2c\_msg](structi2c__msg.md);

34struct [i2c\_emul\_api](structi2c__emul__api.md);

35

[ 37](structi2c__emul.md)struct [i2c\_emul](structi2c__emul.md) {

[ 38](structi2c__emul.md#a72324f94030625a8be49101f49875a7a) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structi2c__emul.md#a72324f94030625a8be49101f49875a7a);

39

[ 41](structi2c__emul.md#a33461303343c3f513a87f1783491324a) const struct [emul](structemul.md) \*[target](structi2c__emul.md#a33461303343c3f513a87f1783491324a);

42

43 /\* API provided for this device \*/

[ 44](structi2c__emul.md#a7e6f7e6e69064df666584027c94bf98c) const struct [i2c\_emul\_api](structi2c__emul__api.md) \*[api](structi2c__emul.md#a7e6f7e6e69064df666584027c94bf98c);

45

[ 50](structi2c__emul.md#abf57cb711e20ab11aa5af247ccc652b2) struct [i2c\_emul\_api](structi2c__emul__api.md) \*[mock\_api](structi2c__emul.md#abf57cb711e20ab11aa5af247ccc652b2);

51

52 /\* I2C address of the emulated device \*/

[ 53](structi2c__emul.md#a8d3924790bd825afe41095bfdf0087eb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structi2c__emul.md#a8d3924790bd825afe41095bfdf0087eb);

54};

55

[ 69](group__i2c__emul__interface.md#ga1b27ff11534eeac47cf50ffb2a1c7cca)typedef int (\*[i2c\_emul\_transfer\_t](group__i2c__emul__interface.md#ga1b27ff11534eeac47cf50ffb2a1c7cca))(const struct [emul](structemul.md) \*target, struct [i2c\_msg](structi2c__msg.md) \*msgs, int num\_msgs,

70 int addr);

71

[ 79](group__i2c__emul__interface.md#ga92851f09c23531bbaea25301dc2607ce)int [i2c\_emul\_register](group__i2c__emul__interface.md#ga92851f09c23531bbaea25301dc2607ce)(const struct [device](structdevice.md) \*dev, struct [i2c\_emul](structi2c__emul.md) \*[emul](structemul.md));

80

[ 82](structi2c__emul__api.md)struct [i2c\_emul\_api](structi2c__emul__api.md) {

[ 83](structi2c__emul__api.md#af155e9e2145597c9ca14473ddf01d48f) [i2c\_emul\_transfer\_t](group__i2c__emul__interface.md#ga1b27ff11534eeac47cf50ffb2a1c7cca) [transfer](structi2c__emul__api.md#af155e9e2145597c9ca14473ddf01d48f);

84};

85

86#ifdef \_\_cplusplus

87}

88#endif

89

93

94#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_I2C\_EMUL\_H\_ \*/

[device.h](device_8h.md)

[i2c.h](drivers_2i2c_8h.md)

Public APIs for the I2C drivers.

[emul.h](emul_8h.md)

[i2c\_emul\_transfer\_t](group__i2c__emul__interface.md#ga1b27ff11534eeac47cf50ffb2a1c7cca)

int(\* i2c\_emul\_transfer\_t)(const struct emul \*target, struct i2c\_msg \*msgs, int num\_msgs, int addr)

Passes I2C messages to the emulator.

**Definition** i2c\_emul.h:69

[i2c\_emul\_register](group__i2c__emul__interface.md#ga92851f09c23531bbaea25301dc2607ce)

int i2c\_emul\_register(const struct device \*dev, struct i2c\_emul \*emul)

Register an emulated device on the controller.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[types.h](include_2zephyr_2types_8h.md)

[slist.h](slist_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:78

[i2c\_emul\_api](structi2c__emul__api.md)

Definition of the emulator API.

**Definition** i2c\_emul.h:82

[i2c\_emul\_api::transfer](structi2c__emul__api.md#af155e9e2145597c9ca14473ddf01d48f)

i2c\_emul\_transfer\_t transfer

**Definition** i2c\_emul.h:83

[i2c\_emul](structi2c__emul.md)

Node in a linked list of emulators for I2C devices.

**Definition** i2c\_emul.h:37

[i2c\_emul::target](structi2c__emul.md#a33461303343c3f513a87f1783491324a)

const struct emul \* target

Target emulator - REQUIRED for all emulated bus nodes of any type.

**Definition** i2c\_emul.h:41

[i2c\_emul::node](structi2c__emul.md#a72324f94030625a8be49101f49875a7a)

sys\_snode\_t node

**Definition** i2c\_emul.h:38

[i2c\_emul::api](structi2c__emul.md#a7e6f7e6e69064df666584027c94bf98c)

const struct i2c\_emul\_api \* api

**Definition** i2c\_emul.h:44

[i2c\_emul::addr](structi2c__emul.md#a8d3924790bd825afe41095bfdf0087eb)

uint16\_t addr

**Definition** i2c\_emul.h:53

[i2c\_emul::mock\_api](structi2c__emul.md#abf57cb711e20ab11aa5af247ccc652b2)

struct i2c\_emul\_api \* mock\_api

A mock API that if not NULL will take precedence over the actual API.

**Definition** i2c\_emul.h:50

[i2c\_msg](structi2c__msg.md)

One I2C Message.

**Definition** i2c.h:182

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2c\_emul.h](i2c__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
