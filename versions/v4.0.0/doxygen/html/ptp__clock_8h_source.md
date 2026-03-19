---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ptp__clock_8h_source.html
original_path: doxygen/html/ptp__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ptp\_clock.h

[Go to the documentation of this file.](ptp__clock_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PTP\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_PTP\_CLOCK\_H\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[stdint.h](stdint_8h.md)>

12#include <[zephyr/device.h](device_8h.md)>

13#include <[zephyr/sys/util.h](sys_2util_8h.md)>

14#include <[zephyr/net/ptp\_time.h](ptp__time_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20/\* Name of the PTP clock driver \*/

21#if !defined(PTP\_CLOCK\_NAME)

[ 22](ptp__clock_8h.md#a31fba0e7a6444b3301cbe0372e6d1996)#define PTP\_CLOCK\_NAME "PTP\_CLOCK"

23#endif

24

[ 25](structptp__clock__driver__api.md)\_\_subsystem struct [ptp\_clock\_driver\_api](structptp__clock__driver__api.md) {

[ 26](structptp__clock__driver__api.md#aba0ef94f2bfe3e3d7fa2d5cedd473ab2) int (\*[set](structptp__clock__driver__api.md#aba0ef94f2bfe3e3d7fa2d5cedd473ab2))(const struct [device](structdevice.md) \*dev, struct [net\_ptp\_time](structnet__ptp__time.md) \*[tm](structtm.md));

[ 27](structptp__clock__driver__api.md#a5f9cfa4f61efe4eeee9dccb6d1e396b4) int (\*[get](structptp__clock__driver__api.md#a5f9cfa4f61efe4eeee9dccb6d1e396b4))(const struct [device](structdevice.md) \*dev, struct [net\_ptp\_time](structnet__ptp__time.md) \*[tm](structtm.md));

[ 28](structptp__clock__driver__api.md#a7177e1fb271aacbae2a081ef41eb585c) int (\*[adjust](structptp__clock__driver__api.md#a7177e1fb271aacbae2a081ef41eb585c))(const struct [device](structdevice.md) \*dev, int increment);

[ 29](structptp__clock__driver__api.md#a8774b43b65403de8faec5606e024f9af) int (\*[rate\_adjust](structptp__clock__driver__api.md#a8774b43b65403de8faec5606e024f9af))(const struct [device](structdevice.md) \*dev, double ratio);

30};

31

[ 40](ptp__clock_8h.md#a41123183be722b3423d5e993d3cde7c2)static inline int [ptp\_clock\_set](ptp__clock_8h.md#a41123183be722b3423d5e993d3cde7c2)(const struct [device](structdevice.md) \*dev,

41 struct [net\_ptp\_time](structnet__ptp__time.md) \*[tm](structtm.md))

42{

43 const struct [ptp\_clock\_driver\_api](structptp__clock__driver__api.md) \*api =

44 (const struct [ptp\_clock\_driver\_api](structptp__clock__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

45

46 return api->[set](structptp__clock__driver__api.md#aba0ef94f2bfe3e3d7fa2d5cedd473ab2)(dev, [tm](structtm.md));

47}

48

[ 57](ptp__clock_8h.md#a443f97ef2766e87c0b42c6ad6f7b63b4)\_\_syscall int [ptp\_clock\_get](ptp__clock_8h.md#a443f97ef2766e87c0b42c6ad6f7b63b4)(const struct [device](structdevice.md) \*dev, struct [net\_ptp\_time](structnet__ptp__time.md) \*[tm](structtm.md));

58

59static inline int z\_impl\_ptp\_clock\_get(const struct [device](structdevice.md) \*dev,

60 struct [net\_ptp\_time](structnet__ptp__time.md) \*[tm](structtm.md))

61{

62 const struct [ptp\_clock\_driver\_api](structptp__clock__driver__api.md) \*api =

63 (const struct [ptp\_clock\_driver\_api](structptp__clock__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

64

65 return api->get(dev, [tm](structtm.md));

66}

67

[ 76](ptp__clock_8h.md#abd11d19b5ec5491e5813bf7cb74ab9b0)static inline int [ptp\_clock\_adjust](ptp__clock_8h.md#abd11d19b5ec5491e5813bf7cb74ab9b0)(const struct [device](structdevice.md) \*dev, int increment)

77{

78 const struct [ptp\_clock\_driver\_api](structptp__clock__driver__api.md) \*api =

79 (const struct [ptp\_clock\_driver\_api](structptp__clock__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

80

81 return api->[adjust](structptp__clock__driver__api.md#a7177e1fb271aacbae2a081ef41eb585c)(dev, increment);

82}

83

[ 92](ptp__clock_8h.md#a310ee4974e6f3b01c4aa1b985194e57a)static inline int [ptp\_clock\_rate\_adjust](ptp__clock_8h.md#a310ee4974e6f3b01c4aa1b985194e57a)(const struct [device](structdevice.md) \*dev, double rate)

93{

94 const struct [ptp\_clock\_driver\_api](structptp__clock__driver__api.md) \*api =

95 (const struct [ptp\_clock\_driver\_api](structptp__clock__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

96

97 return api->[rate\_adjust](structptp__clock__driver__api.md#a8774b43b65403de8faec5606e024f9af)(dev, rate);

98}

99

100#ifdef \_\_cplusplus

101}

102#endif

103

104#include <zephyr/syscalls/ptp\_clock.h>

105

106#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PTP\_CLOCK\_H\_ \*/

[device.h](device_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[ptp\_clock\_rate\_adjust](ptp__clock_8h.md#a310ee4974e6f3b01c4aa1b985194e57a)

static int ptp\_clock\_rate\_adjust(const struct device \*dev, double rate)

Adjust the PTP clock time change rate when compared to its neighbor.

**Definition** ptp\_clock.h:92

[ptp\_clock\_set](ptp__clock_8h.md#a41123183be722b3423d5e993d3cde7c2)

static int ptp\_clock\_set(const struct device \*dev, struct net\_ptp\_time \*tm)

Set the time of the PTP clock.

**Definition** ptp\_clock.h:40

[ptp\_clock\_get](ptp__clock_8h.md#a443f97ef2766e87c0b42c6ad6f7b63b4)

int ptp\_clock\_get(const struct device \*dev, struct net\_ptp\_time \*tm)

Get the time of the PTP clock.

[ptp\_clock\_adjust](ptp__clock_8h.md#abd11d19b5ec5491e5813bf7cb74ab9b0)

static int ptp\_clock\_adjust(const struct device \*dev, int increment)

Adjust the PTP clock time.

**Definition** ptp\_clock.h:76

[ptp\_time.h](ptp__time_8h.md)

Public functions for the Precision Time Protocol time specification.

[stdint.h](stdint_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[net\_ptp\_time](structnet__ptp__time.md)

(Generalized) Precision Time Protocol Timestamp format.

**Definition** ptp\_time.h:111

[ptp\_clock\_driver\_api](structptp__clock__driver__api.md)

**Definition** ptp\_clock.h:25

[ptp\_clock\_driver\_api::get](structptp__clock__driver__api.md#a5f9cfa4f61efe4eeee9dccb6d1e396b4)

int(\* get)(const struct device \*dev, struct net\_ptp\_time \*tm)

**Definition** ptp\_clock.h:27

[ptp\_clock\_driver\_api::adjust](structptp__clock__driver__api.md#a7177e1fb271aacbae2a081ef41eb585c)

int(\* adjust)(const struct device \*dev, int increment)

**Definition** ptp\_clock.h:28

[ptp\_clock\_driver\_api::rate\_adjust](structptp__clock__driver__api.md#a8774b43b65403de8faec5606e024f9af)

int(\* rate\_adjust)(const struct device \*dev, double ratio)

**Definition** ptp\_clock.h:29

[ptp\_clock\_driver\_api::set](structptp__clock__driver__api.md#aba0ef94f2bfe3e3d7fa2d5cedd473ab2)

int(\* set)(const struct device \*dev, struct net\_ptp\_time \*tm)

**Definition** ptp\_clock.h:26

[tm](structtm.md)

**Definition** time.h:24

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ptp\_clock.h](ptp__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
