---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/comparator_8h_source.html
original_path: doxygen/html/comparator_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

comparator.h

[Go to the documentation of this file.](comparator_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_COMPARATOR\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_COMPARATOR\_H\_

9

18

19#include <[zephyr/device.h](device_8h.md)>

20#include <[errno.h](errno_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 27](group__comparator__interface.md#gab02743771baf02ee0105aa1303931674)enum [comparator\_trigger](group__comparator__interface.md#gab02743771baf02ee0105aa1303931674) {

[ 29](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674aef8abb95e06470906323eb67a84274ab) [COMPARATOR\_TRIGGER\_NONE](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674aef8abb95e06470906323eb67a84274ab) = 0,

[ 31](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674a2bd8d1afb67a68a0bbc6737d434d6b89) [COMPARATOR\_TRIGGER\_RISING\_EDGE](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674a2bd8d1afb67a68a0bbc6737d434d6b89),

[ 33](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674a762c9ea031595a909d2b70128adf9734) [COMPARATOR\_TRIGGER\_FALLING\_EDGE](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674a762c9ea031595a909d2b70128adf9734),

[ 35](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674a65cb9e6aa70639b15d0ca3cf16777f97) [COMPARATOR\_TRIGGER\_BOTH\_EDGES](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674a65cb9e6aa70639b15d0ca3cf16777f97)

36};

37

[ 39](group__comparator__interface.md#ga409308b8ba2efdca4a6ec4bdc4d3bc31)typedef void (\*[comparator\_callback\_t](group__comparator__interface.md#ga409308b8ba2efdca4a6ec4bdc4d3bc31))(const struct [device](structdevice.md) \*dev, void \*user\_data);

40

42

43typedef int (\*comparator\_api\_get\_output)(const struct [device](structdevice.md) \*dev);

44typedef int (\*comparator\_api\_set\_trigger)(const struct [device](structdevice.md) \*dev,

45 enum [comparator\_trigger](group__comparator__interface.md#gab02743771baf02ee0105aa1303931674) trigger);

46typedef int (\*comparator\_api\_set\_trigger\_callback)(const struct [device](structdevice.md) \*dev,

47 [comparator\_callback\_t](group__comparator__interface.md#ga409308b8ba2efdca4a6ec4bdc4d3bc31) callback,

48 void \*user\_data);

49typedef int (\*comparator\_api\_trigger\_is\_pending)(const struct [device](structdevice.md) \*dev);

50

51\_\_subsystem struct comparator\_driver\_api {

52 comparator\_api\_get\_output get\_output;

53 comparator\_api\_set\_trigger set\_trigger;

54 comparator\_api\_set\_trigger\_callback set\_trigger\_callback;

55 comparator\_api\_trigger\_is\_pending trigger\_is\_pending;

56};

57

59

[ 69](group__comparator__interface.md#ga89ea48c5d4a9d8c8ec44ee4c987309f3)\_\_syscall int [comparator\_get\_output](group__comparator__interface.md#ga89ea48c5d4a9d8c8ec44ee4c987309f3)(const struct [device](structdevice.md) \*dev);

70

71static inline int z\_impl\_comparator\_get\_output(const struct [device](structdevice.md) \*dev)

72{

73 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(comparator, dev)->get\_output(dev);

74}

75

[ 85](group__comparator__interface.md#ga964fab6458e020d8717ee7c47a84c1d0)\_\_syscall int [comparator\_set\_trigger](group__comparator__interface.md#ga964fab6458e020d8717ee7c47a84c1d0)(const struct [device](structdevice.md) \*dev,

86 enum [comparator\_trigger](group__comparator__interface.md#gab02743771baf02ee0105aa1303931674) trigger);

87

88static inline int z\_impl\_comparator\_set\_trigger(const struct [device](structdevice.md) \*dev,

89 enum [comparator\_trigger](group__comparator__interface.md#gab02743771baf02ee0105aa1303931674) trigger)

90{

91 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(comparator, dev)->set\_trigger(dev, trigger);

92}

93

[ 107](group__comparator__interface.md#ga1c9dc5dd46f5bb62b3cf4e2cfcd42509)static inline int [comparator\_set\_trigger\_callback](group__comparator__interface.md#ga1c9dc5dd46f5bb62b3cf4e2cfcd42509)(const struct [device](structdevice.md) \*dev,

108 [comparator\_callback\_t](group__comparator__interface.md#ga409308b8ba2efdca4a6ec4bdc4d3bc31) callback,

109 void \*user\_data)

110{

111 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(comparator, dev)->set\_trigger\_callback(dev, callback, user\_data);

112}

113

[ 123](group__comparator__interface.md#ga28aa27594c7c3cf5cd7306d47ebf53f9)\_\_syscall int [comparator\_trigger\_is\_pending](group__comparator__interface.md#ga28aa27594c7c3cf5cd7306d47ebf53f9)(const struct [device](structdevice.md) \*dev);

124

125static inline int z\_impl\_comparator\_trigger\_is\_pending(const struct [device](structdevice.md) \*dev)

126{

127 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(comparator, dev)->trigger\_is\_pending(dev);

128}

129

130#ifdef \_\_cplusplus

131}

132#endif

133

135

136#include <zephyr/syscalls/comparator.h>

137

138#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_COMPARATOR\_H\_ \*/

[device.h](device_8h.md)

[DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)

#define DEVICE\_API\_GET(\_class, \_dev)

Expands to the pointer of a device's API for a given class.

**Definition** device.h:1263

[errno.h](errno_8h.md)

System error numbers.

[comparator\_set\_trigger\_callback](group__comparator__interface.md#ga1c9dc5dd46f5bb62b3cf4e2cfcd42509)

static int comparator\_set\_trigger\_callback(const struct device \*dev, comparator\_callback\_t callback, void \*user\_data)

Set comparator's trigger callback.

**Definition** comparator.h:107

[comparator\_trigger\_is\_pending](group__comparator__interface.md#ga28aa27594c7c3cf5cd7306d47ebf53f9)

int comparator\_trigger\_is\_pending(const struct device \*dev)

Check if comparator's trigger is pending and clear it.

[comparator\_callback\_t](group__comparator__interface.md#ga409308b8ba2efdca4a6ec4bdc4d3bc31)

void(\* comparator\_callback\_t)(const struct device \*dev, void \*user\_data)

Comparator callback template.

**Definition** comparator.h:39

[comparator\_get\_output](group__comparator__interface.md#ga89ea48c5d4a9d8c8ec44ee4c987309f3)

int comparator\_get\_output(const struct device \*dev)

Get comparator's output state.

[comparator\_set\_trigger](group__comparator__interface.md#ga964fab6458e020d8717ee7c47a84c1d0)

int comparator\_set\_trigger(const struct device \*dev, enum comparator\_trigger trigger)

Set comparator's trigger.

[comparator\_trigger](group__comparator__interface.md#gab02743771baf02ee0105aa1303931674)

comparator\_trigger

Comparator trigger enumerations.

**Definition** comparator.h:27

[COMPARATOR\_TRIGGER\_RISING\_EDGE](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674a2bd8d1afb67a68a0bbc6737d434d6b89)

@ COMPARATOR\_TRIGGER\_RISING\_EDGE

Trigger on rising edge of comparator output.

**Definition** comparator.h:31

[COMPARATOR\_TRIGGER\_BOTH\_EDGES](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674a65cb9e6aa70639b15d0ca3cf16777f97)

@ COMPARATOR\_TRIGGER\_BOTH\_EDGES

Trigger on both edges of comparator output.

**Definition** comparator.h:35

[COMPARATOR\_TRIGGER\_FALLING\_EDGE](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674a762c9ea031595a909d2b70128adf9734)

@ COMPARATOR\_TRIGGER\_FALLING\_EDGE

Trigger on falling edge of comparator output.

**Definition** comparator.h:33

[COMPARATOR\_TRIGGER\_NONE](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674aef8abb95e06470906323eb67a84274ab)

@ COMPARATOR\_TRIGGER\_NONE

No trigger.

**Definition** comparator.h:29

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [comparator.h](comparator_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
