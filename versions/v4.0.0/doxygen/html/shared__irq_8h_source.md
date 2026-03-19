---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/shared__irq_8h_source.html
original_path: doxygen/html/shared__irq_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shared\_irq.h

[Go to the documentation of this file.](shared__irq_8h.md)

1/\* shared\_irq - Shared interrupt driver \*/

2

3/\*

4 \* Copyright (c) 2015 - 2023 Intel corporation

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_SHARED\_IRQ\_H\_

10#define ZEPHYR\_INCLUDE\_SHARED\_IRQ\_H\_

11

12#include <[zephyr/device.h](device_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 18](shared__irq_8h.md#af6d98f7cd2cde7482b7276aa6e0b487c)typedef int (\*[isr\_t](shared__irq_8h.md#af6d98f7cd2cde7482b7276aa6e0b487c))(const struct [device](structdevice.md) \*dev, unsigned int irq\_number);

19

20/\* driver API definition \*/

[ 21](shared__irq_8h.md#ae400920b45bedf3da66831597ebca841)typedef int (\*[shared\_irq\_register\_t](shared__irq_8h.md#ae400920b45bedf3da66831597ebca841))(const struct [device](structdevice.md) \*dev,

22 [isr\_t](shared__irq_8h.md#af6d98f7cd2cde7482b7276aa6e0b487c) isr\_func,

23 const struct [device](structdevice.md) \*isr\_dev);

[ 24](shared__irq_8h.md#a0ff7a6ee448eb3e889aa9a7bd63e49bc)typedef int (\*[shared\_irq\_enable\_t](shared__irq_8h.md#a0ff7a6ee448eb3e889aa9a7bd63e49bc))(const struct [device](structdevice.md) \*dev,

25 const struct [device](structdevice.md) \*isr\_dev);

[ 26](shared__irq_8h.md#a22cf2ce082fea27f2087cd1abd74934c)typedef int (\*[shared\_irq\_disable\_t](shared__irq_8h.md#a22cf2ce082fea27f2087cd1abd74934c))(const struct [device](structdevice.md) \*dev,

27 const struct [device](structdevice.md) \*isr\_dev);

28

[ 29](structshared__irq__driver__api.md)\_\_subsystem struct [shared\_irq\_driver\_api](structshared__irq__driver__api.md) {

[ 30](structshared__irq__driver__api.md#a8e908b0d6e596905f11a3de1a6f907ad) [shared\_irq\_register\_t](shared__irq_8h.md#ae400920b45bedf3da66831597ebca841) [isr\_register](structshared__irq__driver__api.md#a8e908b0d6e596905f11a3de1a6f907ad);

[ 31](structshared__irq__driver__api.md#a5a4ef3888a3d35497c47b67f4511fd5e) [shared\_irq\_enable\_t](shared__irq_8h.md#a0ff7a6ee448eb3e889aa9a7bd63e49bc) [enable](structshared__irq__driver__api.md#a5a4ef3888a3d35497c47b67f4511fd5e);

[ 32](structshared__irq__driver__api.md#a2e339779ddec773a536f681b9df9997e) [shared\_irq\_disable\_t](shared__irq_8h.md#a22cf2ce082fea27f2087cd1abd74934c) [disable](structshared__irq__driver__api.md#a2e339779ddec773a536f681b9df9997e);

33};

34

[ 41](shared__irq_8h.md#a6ef6d536da13ebd8aa75830516dc0696)static inline int [shared\_irq\_isr\_register](shared__irq_8h.md#a6ef6d536da13ebd8aa75830516dc0696)(const struct [device](structdevice.md) \*dev,

42 [isr\_t](shared__irq_8h.md#af6d98f7cd2cde7482b7276aa6e0b487c) isr\_func,

43 const struct [device](structdevice.md) \*isr\_dev)

44{

45 const struct [shared\_irq\_driver\_api](structshared__irq__driver__api.md) \*api =

46 (const struct [shared\_irq\_driver\_api](structshared__irq__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

47

48 return api->[isr\_register](structshared__irq__driver__api.md#a8e908b0d6e596905f11a3de1a6f907ad)(dev, isr\_func, isr\_dev);

49}

50

[ 56](shared__irq_8h.md#af36534589858c1e02ea50ed3cc888d41)static inline int [shared\_irq\_enable](shared__irq_8h.md#af36534589858c1e02ea50ed3cc888d41)(const struct [device](structdevice.md) \*dev,

57 const struct [device](structdevice.md) \*isr\_dev)

58{

59 const struct [shared\_irq\_driver\_api](structshared__irq__driver__api.md) \*api =

60 (const struct [shared\_irq\_driver\_api](structshared__irq__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

61

62 return api->[enable](structshared__irq__driver__api.md#a5a4ef3888a3d35497c47b67f4511fd5e)(dev, isr\_dev);

63}

64

[ 70](shared__irq_8h.md#adcdb9702c30ca0911103fc8b9857abb4)static inline int [shared\_irq\_disable](shared__irq_8h.md#adcdb9702c30ca0911103fc8b9857abb4)(const struct [device](structdevice.md) \*dev,

71 const struct [device](structdevice.md) \*isr\_dev)

72{

73 const struct [shared\_irq\_driver\_api](structshared__irq__driver__api.md) \*api =

74 (const struct [shared\_irq\_driver\_api](structshared__irq__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

75

76 return api->[disable](structshared__irq__driver__api.md#a2e339779ddec773a536f681b9df9997e)(dev, isr\_dev);

77}

78

79#ifdef \_\_cplusplus

80}

81#endif

82

83#endif /\* ZEPHYR\_INCLUDE\_SHARED\_IRQ\_H\_ \*/

[device.h](device_8h.md)

[shared\_irq\_enable\_t](shared__irq_8h.md#a0ff7a6ee448eb3e889aa9a7bd63e49bc)

int(\* shared\_irq\_enable\_t)(const struct device \*dev, const struct device \*isr\_dev)

**Definition** shared\_irq.h:24

[shared\_irq\_disable\_t](shared__irq_8h.md#a22cf2ce082fea27f2087cd1abd74934c)

int(\* shared\_irq\_disable\_t)(const struct device \*dev, const struct device \*isr\_dev)

**Definition** shared\_irq.h:26

[shared\_irq\_isr\_register](shared__irq_8h.md#a6ef6d536da13ebd8aa75830516dc0696)

static int shared\_irq\_isr\_register(const struct device \*dev, isr\_t isr\_func, const struct device \*isr\_dev)

Register a device ISR.

**Definition** shared\_irq.h:41

[shared\_irq\_disable](shared__irq_8h.md#adcdb9702c30ca0911103fc8b9857abb4)

static int shared\_irq\_disable(const struct device \*dev, const struct device \*isr\_dev)

Disable ISR for device.

**Definition** shared\_irq.h:70

[shared\_irq\_register\_t](shared__irq_8h.md#ae400920b45bedf3da66831597ebca841)

int(\* shared\_irq\_register\_t)(const struct device \*dev, isr\_t isr\_func, const struct device \*isr\_dev)

**Definition** shared\_irq.h:21

[shared\_irq\_enable](shared__irq_8h.md#af36534589858c1e02ea50ed3cc888d41)

static int shared\_irq\_enable(const struct device \*dev, const struct device \*isr\_dev)

Enable ISR for device.

**Definition** shared\_irq.h:56

[isr\_t](shared__irq_8h.md#af6d98f7cd2cde7482b7276aa6e0b487c)

int(\* isr\_t)(const struct device \*dev, unsigned int irq\_number)

**Definition** shared\_irq.h:18

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[shared\_irq\_driver\_api](structshared__irq__driver__api.md)

**Definition** shared\_irq.h:29

[shared\_irq\_driver\_api::disable](structshared__irq__driver__api.md#a2e339779ddec773a536f681b9df9997e)

shared\_irq\_disable\_t disable

**Definition** shared\_irq.h:32

[shared\_irq\_driver\_api::enable](structshared__irq__driver__api.md#a5a4ef3888a3d35497c47b67f4511fd5e)

shared\_irq\_enable\_t enable

**Definition** shared\_irq.h:31

[shared\_irq\_driver\_api::isr\_register](structshared__irq__driver__api.md#a8e908b0d6e596905f11a3de1a6f907ad)

shared\_irq\_register\_t isr\_register

**Definition** shared\_irq.h:30

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shared\_irq.h](shared__irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
