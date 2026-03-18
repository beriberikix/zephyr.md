---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gicv3__its_8h_source.html
original_path: doxygen/html/gicv3__its_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gicv3\_its.h

[Go to the documentation of this file.](gicv3__its_8h.md)

1/\*

2 \* Copyright (c) 2021 BayLibre, SAS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_GICV3\_ITS\_H\_

17#define ZEPHYR\_INCLUDE\_DRIVERS\_GICV3\_ITS\_H\_

18

[ 19](gicv3__its_8h.md#a49dff2553cbd48edc7057157d2ecb45d)typedef unsigned int (\*[its\_api\_alloc\_intid\_t](gicv3__its_8h.md#a49dff2553cbd48edc7057157d2ecb45d))(const struct [device](structdevice.md) \*dev);

[ 20](gicv3__its_8h.md#a39f4a213de953b77615b270f3ff13832)typedef int (\*[its\_api\_setup\_deviceid\_t](gicv3__its_8h.md#a39f4a213de953b77615b270f3ff13832))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id,

21 unsigned int nites);

[ 22](gicv3__its_8h.md#a2642c1f7ecf45d404c17cdbcd824bb45)typedef int (\*[its\_api\_map\_intid\_t](gicv3__its_8h.md#a2642c1f7ecf45d404c17cdbcd824bb45))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id,

23 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_id, unsigned int intid);

[ 24](gicv3__its_8h.md#a26bf8d071e3cb856fc81d8911e942f5a)typedef int (\*[its\_api\_send\_int\_t](gicv3__its_8h.md#a26bf8d071e3cb856fc81d8911e942f5a))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_id);

[ 25](gicv3__its_8h.md#add616700e3aeee952187ef96cb2d19c9)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[its\_api\_get\_msi\_addr\_t](gicv3__its_8h.md#add616700e3aeee952187ef96cb2d19c9))(const struct [device](structdevice.md) \*dev);

26

[ 27](structits__driver__api.md)\_\_subsystem struct [its\_driver\_api](structits__driver__api.md) {

[ 28](structits__driver__api.md#affc7190b95d16fa0223f6fd7b1ae9c14) [its\_api\_alloc\_intid\_t](gicv3__its_8h.md#a49dff2553cbd48edc7057157d2ecb45d) [alloc\_intid](structits__driver__api.md#affc7190b95d16fa0223f6fd7b1ae9c14);

[ 29](structits__driver__api.md#aa853404a1105b0cc4d1b6c976579ae4a) [its\_api\_setup\_deviceid\_t](gicv3__its_8h.md#a39f4a213de953b77615b270f3ff13832) [setup\_deviceid](structits__driver__api.md#aa853404a1105b0cc4d1b6c976579ae4a);

[ 30](structits__driver__api.md#a0a71be1a078b6e1a82624e0ef9a619ac) [its\_api\_map\_intid\_t](gicv3__its_8h.md#a2642c1f7ecf45d404c17cdbcd824bb45) [map\_intid](structits__driver__api.md#a0a71be1a078b6e1a82624e0ef9a619ac);

[ 31](structits__driver__api.md#aec4b32cea8d6c5fa2a59d2d25e6053cf) [its\_api\_send\_int\_t](gicv3__its_8h.md#a26bf8d071e3cb856fc81d8911e942f5a) [send\_int](structits__driver__api.md#aec4b32cea8d6c5fa2a59d2d25e6053cf);

[ 32](structits__driver__api.md#aa87bb10ac8f165c2acbc6033591b9aa8) [its\_api\_get\_msi\_addr\_t](gicv3__its_8h.md#add616700e3aeee952187ef96cb2d19c9) [get\_msi\_addr](structits__driver__api.md#aa87bb10ac8f165c2acbc6033591b9aa8);

33};

34

[ 35](gicv3__its_8h.md#a5c50167a84a3b7d8e3cf01d226deb3d3)static inline int [its\_alloc\_intid](gicv3__its_8h.md#a5c50167a84a3b7d8e3cf01d226deb3d3)(const struct [device](structdevice.md) \*dev)

36{

37 const struct [its\_driver\_api](structits__driver__api.md) \*api =

38 (const struct [its\_driver\_api](structits__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

39

40 return api->[alloc\_intid](structits__driver__api.md#affc7190b95d16fa0223f6fd7b1ae9c14)(dev);

41}

42

[ 43](gicv3__its_8h.md#a05032faf2fdcde27760871345756d3e5)static inline int [its\_setup\_deviceid](gicv3__its_8h.md#a05032faf2fdcde27760871345756d3e5)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id,

44 unsigned int nites)

45{

46 const struct [its\_driver\_api](structits__driver__api.md) \*api =

47 (const struct [its\_driver\_api](structits__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

48

49 return api->[setup\_deviceid](structits__driver__api.md#aa853404a1105b0cc4d1b6c976579ae4a)(dev, device\_id, nites);

50}

51

[ 52](gicv3__its_8h.md#ac4899e33d0636465265a3072aa5510cc)static inline int [its\_map\_intid](gicv3__its_8h.md#ac4899e33d0636465265a3072aa5510cc)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id,

53 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_id, unsigned int intid)

54{

55 const struct [its\_driver\_api](structits__driver__api.md) \*api =

56 (const struct [its\_driver\_api](structits__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

57

58 return api->[map\_intid](structits__driver__api.md#a0a71be1a078b6e1a82624e0ef9a619ac)(dev, device\_id, event\_id, intid);

59}

60

[ 61](gicv3__its_8h.md#a6139a7f275a6016ecadcb0ee2dfcc327)static inline int [its\_send\_int](gicv3__its_8h.md#a6139a7f275a6016ecadcb0ee2dfcc327)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_id)

62{

63 const struct [its\_driver\_api](structits__driver__api.md) \*api =

64 (const struct [its\_driver\_api](structits__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

65

66 return api->[send\_int](structits__driver__api.md#aec4b32cea8d6c5fa2a59d2d25e6053cf)(dev, device\_id, event\_id);

67}

68

[ 69](gicv3__its_8h.md#afcd0b4735367a10465e81b46d333b06b)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [its\_get\_msi\_addr](gicv3__its_8h.md#afcd0b4735367a10465e81b46d333b06b)(const struct [device](structdevice.md) \*dev)

70{

71 const struct [its\_driver\_api](structits__driver__api.md) \*api =

72 (const struct [its\_driver\_api](structits__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

73

74 return api->[get\_msi\_addr](structits__driver__api.md#aa87bb10ac8f165c2acbc6033591b9aa8)(dev);

75}

76

77#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GICV3\_ITS\_H\_ \*/

[its\_setup\_deviceid](gicv3__its_8h.md#a05032faf2fdcde27760871345756d3e5)

static int its\_setup\_deviceid(const struct device \*dev, uint32\_t device\_id, unsigned int nites)

**Definition** gicv3\_its.h:43

[its\_api\_map\_intid\_t](gicv3__its_8h.md#a2642c1f7ecf45d404c17cdbcd824bb45)

int(\* its\_api\_map\_intid\_t)(const struct device \*dev, uint32\_t device\_id, uint32\_t event\_id, unsigned int intid)

**Definition** gicv3\_its.h:22

[its\_api\_send\_int\_t](gicv3__its_8h.md#a26bf8d071e3cb856fc81d8911e942f5a)

int(\* its\_api\_send\_int\_t)(const struct device \*dev, uint32\_t device\_id, uint32\_t event\_id)

**Definition** gicv3\_its.h:24

[its\_api\_setup\_deviceid\_t](gicv3__its_8h.md#a39f4a213de953b77615b270f3ff13832)

int(\* its\_api\_setup\_deviceid\_t)(const struct device \*dev, uint32\_t device\_id, unsigned int nites)

**Definition** gicv3\_its.h:20

[its\_api\_alloc\_intid\_t](gicv3__its_8h.md#a49dff2553cbd48edc7057157d2ecb45d)

unsigned int(\* its\_api\_alloc\_intid\_t)(const struct device \*dev)

**Definition** gicv3\_its.h:19

[its\_alloc\_intid](gicv3__its_8h.md#a5c50167a84a3b7d8e3cf01d226deb3d3)

static int its\_alloc\_intid(const struct device \*dev)

**Definition** gicv3\_its.h:35

[its\_send\_int](gicv3__its_8h.md#a6139a7f275a6016ecadcb0ee2dfcc327)

static int its\_send\_int(const struct device \*dev, uint32\_t device\_id, uint32\_t event\_id)

**Definition** gicv3\_its.h:61

[its\_map\_intid](gicv3__its_8h.md#ac4899e33d0636465265a3072aa5510cc)

static int its\_map\_intid(const struct device \*dev, uint32\_t device\_id, uint32\_t event\_id, unsigned int intid)

**Definition** gicv3\_its.h:52

[its\_api\_get\_msi\_addr\_t](gicv3__its_8h.md#add616700e3aeee952187ef96cb2d19c9)

uint32\_t(\* its\_api\_get\_msi\_addr\_t)(const struct device \*dev)

**Definition** gicv3\_its.h:25

[its\_get\_msi\_addr](gicv3__its_8h.md#afcd0b4735367a10465e81b46d333b06b)

static uint32\_t its\_get\_msi\_addr(const struct device \*dev)

**Definition** gicv3\_its.h:69

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[its\_driver\_api](structits__driver__api.md)

**Definition** gicv3\_its.h:27

[its\_driver\_api::map\_intid](structits__driver__api.md#a0a71be1a078b6e1a82624e0ef9a619ac)

its\_api\_map\_intid\_t map\_intid

**Definition** gicv3\_its.h:30

[its\_driver\_api::setup\_deviceid](structits__driver__api.md#aa853404a1105b0cc4d1b6c976579ae4a)

its\_api\_setup\_deviceid\_t setup\_deviceid

**Definition** gicv3\_its.h:29

[its\_driver\_api::get\_msi\_addr](structits__driver__api.md#aa87bb10ac8f165c2acbc6033591b9aa8)

its\_api\_get\_msi\_addr\_t get\_msi\_addr

**Definition** gicv3\_its.h:32

[its\_driver\_api::send\_int](structits__driver__api.md#aec4b32cea8d6c5fa2a59d2d25e6053cf)

its\_api\_send\_int\_t send\_int

**Definition** gicv3\_its.h:31

[its\_driver\_api::alloc\_intid](structits__driver__api.md#affc7190b95d16fa0223f6fd7b1ae9c14)

its\_api\_alloc\_intid\_t alloc\_intid

**Definition** gicv3\_its.h:28

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [gicv3\_its.h](gicv3__its_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
