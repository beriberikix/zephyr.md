---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/haptics_8h_source.html
original_path: doxygen/html/haptics_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

haptics.h

[Go to the documentation of this file.](haptics_8h.md)

1/\*

2 \* Copyright 2024 Cirrus Logic, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_HAPTICS\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_HAPTICS\_H\_

9

16

17#include <[zephyr/device.h](device_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 28](group__haptics__interface.md#gae34e538c40e259967f5791cc5ebd2707)typedef int (\*[haptics\_stop\_output\_t](group__haptics__interface.md#gae34e538c40e259967f5791cc5ebd2707))(const struct [device](structdevice.md) \*dev);

29

[ 34](group__haptics__interface.md#gaa6c2ff4b8ed7ae83e4006eb735f61a46)typedef int (\*[haptics\_start\_output\_t](group__haptics__interface.md#gaa6c2ff4b8ed7ae83e4006eb735f61a46))(const struct [device](structdevice.md) \*dev);

35

[ 39](structhaptics__driver__api.md)\_\_subsystem struct [haptics\_driver\_api](structhaptics__driver__api.md) {

[ 40](structhaptics__driver__api.md#a5489147ccfe08d917766bfcb328fa310) [haptics\_start\_output\_t](group__haptics__interface.md#gaa6c2ff4b8ed7ae83e4006eb735f61a46) [start\_output](structhaptics__driver__api.md#a5489147ccfe08d917766bfcb328fa310);

[ 41](structhaptics__driver__api.md#aadbec92f633f42a86458627ecf41a129) [haptics\_stop\_output\_t](group__haptics__interface.md#gae34e538c40e259967f5791cc5ebd2707) [stop\_output](structhaptics__driver__api.md#aadbec92f633f42a86458627ecf41a129);

42};

43

[ 52](group__haptics__interface.md#ga96e0b0fad35d6535adad7536a9411f44)\_\_syscall int [haptics\_start\_output](group__haptics__interface.md#ga96e0b0fad35d6535adad7536a9411f44)(const struct [device](structdevice.md) \*dev);

53

54static inline int z\_impl\_haptics\_start\_output(const struct [device](structdevice.md) \*dev)

55{

56 const struct [haptics\_driver\_api](structhaptics__driver__api.md) \*api = (const struct [haptics\_driver\_api](structhaptics__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

57

58 return api->start\_output(dev);

59}

60

[ 69](group__haptics__interface.md#ga42a5fc7e6b6247316cdf356573dbbb33)\_\_syscall int [haptics\_stop\_output](group__haptics__interface.md#ga42a5fc7e6b6247316cdf356573dbbb33)(const struct [device](structdevice.md) \*dev);

70

71static inline int z\_impl\_haptics\_stop\_output(const struct [device](structdevice.md) \*dev)

72{

73 const struct [haptics\_driver\_api](structhaptics__driver__api.md) \*api = (const struct [haptics\_driver\_api](structhaptics__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

74

75 return api->stop\_output(dev);

76}

77

81

82#ifdef \_\_cplusplus

83}

84#endif /\* \_\_cplusplus \*/

85

86#include <syscalls/haptics.h>

87

88#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_HAPTICS\_H\_ \*/

[device.h](device_8h.md)

[haptics\_stop\_output](group__haptics__interface.md#ga42a5fc7e6b6247316cdf356573dbbb33)

int haptics\_stop\_output(const struct device \*dev)

Set the haptic device to stop output for a playback event.

[haptics\_start\_output](group__haptics__interface.md#ga96e0b0fad35d6535adad7536a9411f44)

int haptics\_start\_output(const struct device \*dev)

Set the haptic device to start output for a playback event.

[haptics\_start\_output\_t](group__haptics__interface.md#gaa6c2ff4b8ed7ae83e4006eb735f61a46)

int(\* haptics\_start\_output\_t)(const struct device \*dev)

Set the haptic device to start output for a playback event.

**Definition** haptics.h:34

[haptics\_stop\_output\_t](group__haptics__interface.md#gae34e538c40e259967f5791cc5ebd2707)

int(\* haptics\_stop\_output\_t)(const struct device \*dev)

Set the haptic device to stop output.

**Definition** haptics.h:28

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[haptics\_driver\_api](structhaptics__driver__api.md)

Haptic device API.

**Definition** haptics.h:39

[haptics\_driver\_api::start\_output](structhaptics__driver__api.md#a5489147ccfe08d917766bfcb328fa310)

haptics\_start\_output\_t start\_output

**Definition** haptics.h:40

[haptics\_driver\_api::stop\_output](structhaptics__driver__api.md#aadbec92f633f42a86458627ecf41a129)

haptics\_stop\_output\_t stop\_output

**Definition** haptics.h:41

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [haptics.h](haptics_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
