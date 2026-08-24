---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_source.html
original_path: doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_rtxxx\_dsp\_ctrl.h

[Go to the documentation of this file.](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md)

1/\*

2 \* Copyright 2025 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[zephyr/device.h](device_8h.md)>

8#include <[zephyr/dt-bindings/misc/nxp\_rtxxx\_dsp\_ctrl.h](dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.md)>

9

10#ifndef \_\_NXP\_RTXXX\_DSP\_CTRL\_H\_\_

11#define \_\_NXP\_RTXXX\_DSP\_CTRL\_H\_\_

12

[ 16](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762)enum [nxp\_rtxxx\_dsp\_ctrl\_section\_type](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762) {

[ 17](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762a8c63b3117b7c525e96be2b054395cfff) [NXP\_RTXXX\_DSP\_CTRL\_SECTION\_RESET](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762a8c63b3117b7c525e96be2b054395cfff) = [NXP\_RTXXX\_DSP\_REGION\_RESET](dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.md#abb4669be96440c29192dc3cf707fce65),

[ 18](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762ab0c726ddfdf30c89075fcf9c7b4586e7) [NXP\_RTXXX\_DSP\_CTRL\_SECTION\_TEXT](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762ab0c726ddfdf30c89075fcf9c7b4586e7) = [NXP\_RTXXX\_DSP\_REGION\_TEXT](dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.md#a2ae85fcd536b453408eca1cba00b308b),

[ 19](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762aa43ff75c06ea161e322d77b8dede7791) [NXP\_RTXXX\_DSP\_CTRL\_SECTION\_DATA](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762aa43ff75c06ea161e322d77b8dede7791) = [NXP\_RTXXX\_DSP\_REGION\_DATA](dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.md#a70bd7dc09d64c9f7ed92d743a900d068)

20};

21

[ 22](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#ab6ed31cfcaa45744f960bc19d89f642f)typedef int (\*[nxp\_rtxxx\_dsp\_ctrl\_api\_load\_section](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#ab6ed31cfcaa45744f960bc19d89f642f))(

23 const struct [device](structdevice.md) \*,

24 const void \*,

25 [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9),

26 enum [nxp\_rtxxx\_dsp\_ctrl\_section\_type](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762)

27);

[ 28](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a561283f2992839e0191d2fcfef12d989)typedef void (\*[nxp\_rtxxx\_dsp\_ctrl\_api\_enable](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a561283f2992839e0191d2fcfef12d989))(const struct [device](structdevice.md) \*dev);

[ 29](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a17b3a647a7798b34c820366916b2a1c5)typedef void (\*[nxp\_rtxxx\_dsp\_ctrl\_api\_disable](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a17b3a647a7798b34c820366916b2a1c5))(const struct [device](structdevice.md) \*dev);

30

[ 31](structnxp__rtxxx__dsp__ctrl__api.md)struct [nxp\_rtxxx\_dsp\_ctrl\_api](structnxp__rtxxx__dsp__ctrl__api.md) {

[ 32](structnxp__rtxxx__dsp__ctrl__api.md#a5c8bbe71bd90f2a375011ac15695de1d) [nxp\_rtxxx\_dsp\_ctrl\_api\_load\_section](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#ab6ed31cfcaa45744f960bc19d89f642f) [load\_section](structnxp__rtxxx__dsp__ctrl__api.md#a5c8bbe71bd90f2a375011ac15695de1d);

[ 33](structnxp__rtxxx__dsp__ctrl__api.md#a234285d700833f09ca73d80d35d13a87) [nxp\_rtxxx\_dsp\_ctrl\_api\_enable](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a561283f2992839e0191d2fcfef12d989) [enable](structnxp__rtxxx__dsp__ctrl__api.md#a234285d700833f09ca73d80d35d13a87);

[ 34](structnxp__rtxxx__dsp__ctrl__api.md#a2c98dc2c0d65b1004b94be86d99778c5) [nxp\_rtxxx\_dsp\_ctrl\_api\_disable](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a17b3a647a7798b34c820366916b2a1c5) [disable](structnxp__rtxxx__dsp__ctrl__api.md#a2c98dc2c0d65b1004b94be86d99778c5);

35};

36

[ 48](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#af1bd0005fe3a6d46d559b249b3ff8ca8)static inline int [nxp\_rtxxx\_dsp\_ctrl\_load\_section](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#af1bd0005fe3a6d46d559b249b3ff8ca8)(

49 const struct [device](structdevice.md) \*dev,

50 const void \*base,

51 size\_t length,

52 enum [nxp\_rtxxx\_dsp\_ctrl\_section\_type](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762) section

53)

54{

55 return ((struct [nxp\_rtxxx\_dsp\_ctrl\_api](structnxp__rtxxx__dsp__ctrl__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d))

56 ->load\_section(dev, base, length, section);

57}

58

[ 64](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a9cc6dd311f29f2e7c79fc74c39658041)static inline void [nxp\_rtxxx\_dsp\_ctrl\_enable](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a9cc6dd311f29f2e7c79fc74c39658041)(const struct [device](structdevice.md) \*dev)

65{

66 ((struct [nxp\_rtxxx\_dsp\_ctrl\_api](structnxp__rtxxx__dsp__ctrl__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d))->[enable](structnxp__rtxxx__dsp__ctrl__api.md#a234285d700833f09ca73d80d35d13a87)(dev);

67}

68

[ 74](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a2efeac2828998f896f2e1bfb532700cd)static inline void [nxp\_rtxxx\_dsp\_ctrl\_disable](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a2efeac2828998f896f2e1bfb532700cd)(const struct [device](structdevice.md) \*dev)

75{

76 ((struct [nxp\_rtxxx\_dsp\_ctrl\_api](structnxp__rtxxx__dsp__ctrl__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d))->[disable](structnxp__rtxxx__dsp__ctrl__api.md#a2c98dc2c0d65b1004b94be86d99778c5)(dev);

77}

78

79#endif

[device.h](device_8h.md)

[nxp\_rtxxx\_dsp\_ctrl\_section\_type](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762)

nxp\_rtxxx\_dsp\_ctrl\_section\_type

Describes an image section type selection.

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:16

[NXP\_RTXXX\_DSP\_CTRL\_SECTION\_RESET](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762a8c63b3117b7c525e96be2b054395cfff)

@ NXP\_RTXXX\_DSP\_CTRL\_SECTION\_RESET

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:17

[NXP\_RTXXX\_DSP\_CTRL\_SECTION\_DATA](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762aa43ff75c06ea161e322d77b8dede7791)

@ NXP\_RTXXX\_DSP\_CTRL\_SECTION\_DATA

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:19

[NXP\_RTXXX\_DSP\_CTRL\_SECTION\_TEXT](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a1230a21b6c11930f80fc5f12605de762ab0c726ddfdf30c89075fcf9c7b4586e7)

@ NXP\_RTXXX\_DSP\_CTRL\_SECTION\_TEXT

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:18

[nxp\_rtxxx\_dsp\_ctrl\_api\_disable](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a17b3a647a7798b34c820366916b2a1c5)

void(\* nxp\_rtxxx\_dsp\_ctrl\_api\_disable)(const struct device \*dev)

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:29

[nxp\_rtxxx\_dsp\_ctrl\_disable](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a2efeac2828998f896f2e1bfb532700cd)

static void nxp\_rtxxx\_dsp\_ctrl\_disable(const struct device \*dev)

Stops (stalls) the DSP.

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:74

[nxp\_rtxxx\_dsp\_ctrl\_api\_enable](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a561283f2992839e0191d2fcfef12d989)

void(\* nxp\_rtxxx\_dsp\_ctrl\_api\_enable)(const struct device \*dev)

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:28

[nxp\_rtxxx\_dsp\_ctrl\_enable](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#a9cc6dd311f29f2e7c79fc74c39658041)

static void nxp\_rtxxx\_dsp\_ctrl\_enable(const struct device \*dev)

Starts (unstalls) the DSP.

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:64

[nxp\_rtxxx\_dsp\_ctrl\_api\_load\_section](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#ab6ed31cfcaa45744f960bc19d89f642f)

int(\* nxp\_rtxxx\_dsp\_ctrl\_api\_load\_section)(const struct device \*, const void \*, size\_t, enum nxp\_rtxxx\_dsp\_ctrl\_section\_type)

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:22

[nxp\_rtxxx\_dsp\_ctrl\_load\_section](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md#af1bd0005fe3a6d46d559b249b3ff8ca8)

static int nxp\_rtxxx\_dsp\_ctrl\_load\_section(const struct device \*dev, const void \*base, size\_t length, enum nxp\_rtxxx\_dsp\_ctrl\_section\_type section)

Loads a specified image representing a specified section to a particular region in the DSP's memory.

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:48

[nxp\_rtxxx\_dsp\_ctrl.h](dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.md)

[NXP\_RTXXX\_DSP\_REGION\_TEXT](dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.md#a2ae85fcd536b453408eca1cba00b308b)

#define NXP\_RTXXX\_DSP\_REGION\_TEXT

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:11

[NXP\_RTXXX\_DSP\_REGION\_DATA](dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.md#a70bd7dc09d64c9f7ed92d743a900d068)

#define NXP\_RTXXX\_DSP\_REGION\_DATA

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:12

[NXP\_RTXXX\_DSP\_REGION\_RESET](dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.md#abb4669be96440c29192dc3cf707fce65)

#define NXP\_RTXXX\_DSP\_REGION\_RESET

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:10

[size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)

Size of off\_t must be equal or less than size of size\_t

**Definition** retained\_mem.h:28

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[nxp\_rtxxx\_dsp\_ctrl\_api](structnxp__rtxxx__dsp__ctrl__api.md)

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:31

[nxp\_rtxxx\_dsp\_ctrl\_api::enable](structnxp__rtxxx__dsp__ctrl__api.md#a234285d700833f09ca73d80d35d13a87)

nxp\_rtxxx\_dsp\_ctrl\_api\_enable enable

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:33

[nxp\_rtxxx\_dsp\_ctrl\_api::disable](structnxp__rtxxx__dsp__ctrl__api.md#a2c98dc2c0d65b1004b94be86d99778c5)

nxp\_rtxxx\_dsp\_ctrl\_api\_disable disable

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:34

[nxp\_rtxxx\_dsp\_ctrl\_api::load\_section](structnxp__rtxxx__dsp__ctrl__api.md#a5c8bbe71bd90f2a375011ac15695de1d)

nxp\_rtxxx\_dsp\_ctrl\_api\_load\_section load\_section

**Definition** nxp\_rtxxx\_dsp\_ctrl.h:32

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [nxp\_rtxxx\_dsp\_ctrl](dir_6ae4f57dc0f23a67287970302be617ac.md)
- [nxp\_rtxxx\_dsp\_ctrl.h](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
