---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usbc__vbus_8h_source.html
original_path: doxygen/html/usbc__vbus_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_vbus.h

[Go to the documentation of this file.](usbc__vbus_8h.md)

1/\*

2 \* Copyright 2022 The Chromium OS Authors

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_VBUS\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_VBUS\_H\_

17

24

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[zephyr/device.h](device_8h.md)>

27#include <[zephyr/drivers/usb\_c/usbc\_tc.h](usbc__tc_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 33](structusbc__vbus__driver__api.md)struct [usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md) {

[ 34](structusbc__vbus__driver__api.md#adce9dc1f3065a029b53ee954d734cfac) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[check\_level](structusbc__vbus__driver__api.md#adce9dc1f3065a029b53ee954d734cfac))(const struct [device](structdevice.md) \*dev, enum [tc\_vbus\_level](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161) level);

[ 35](structusbc__vbus__driver__api.md#a373b4435b3e4a1a88a78a15d24bdcbab) int (\*[measure](structusbc__vbus__driver__api.md#a373b4435b3e4a1a88a78a15d24bdcbab))(const struct [device](structdevice.md) \*dev, int \*vbus\_meas);

[ 36](structusbc__vbus__driver__api.md#a164ae753995e293460fc408edebe21df) int (\*[discharge](structusbc__vbus__driver__api.md#a164ae753995e293460fc408edebe21df))(const struct [device](structdevice.md) \*dev, bool [enable](structusbc__vbus__driver__api.md#a5a7e6383279dc17c01d478a063efcac0));

[ 37](structusbc__vbus__driver__api.md#a5a7e6383279dc17c01d478a063efcac0) int (\*[enable](structusbc__vbus__driver__api.md#a5a7e6383279dc17c01d478a063efcac0))(const struct [device](structdevice.md) \*dev, bool [enable](structusbc__vbus__driver__api.md#a5a7e6383279dc17c01d478a063efcac0));

38};

39

[ 49](group__usbc__vbus__api.md#ga421653274fe9b8e2e6237a4bbe47e3ad)static inline bool [usbc\_vbus\_check\_level](group__usbc__vbus__api.md#ga421653274fe9b8e2e6237a4bbe47e3ad)(const struct [device](structdevice.md) \*dev, enum [tc\_vbus\_level](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161) level)

50{

51 const struct [usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md) \*api = (const struct [usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

52

53 return api->[check\_level](structusbc__vbus__driver__api.md#adce9dc1f3065a029b53ee954d734cfac)(dev, level);

54}

55

[ 65](group__usbc__vbus__api.md#ga0b6c561c5f74a30d54397294cb21660d)static inline int [usbc\_vbus\_measure](group__usbc__vbus__api.md#ga0b6c561c5f74a30d54397294cb21660d)(const struct [device](structdevice.md) \*dev, int \*meas)

66{

67 const struct [usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md) \*api = (const struct [usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

68

69 return api->[measure](structusbc__vbus__driver__api.md#a373b4435b3e4a1a88a78a15d24bdcbab)(dev, meas);

70}

71

[ 82](group__usbc__vbus__api.md#ga8414cfcfeee7799ea57854c59c0c1677)static inline int [usbc\_vbus\_discharge](group__usbc__vbus__api.md#ga8414cfcfeee7799ea57854c59c0c1677)(const struct [device](structdevice.md) \*dev, bool [enable](structusbc__vbus__driver__api.md#a5a7e6383279dc17c01d478a063efcac0))

83{

84 const struct [usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md) \*api = (const struct [usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

85

86 return api->[discharge](structusbc__vbus__driver__api.md#a164ae753995e293460fc408edebe21df)(dev, [enable](structusbc__vbus__driver__api.md#a5a7e6383279dc17c01d478a063efcac0));

87}

88

[ 99](group__usbc__vbus__api.md#ga7c94eac0f28be6cd12717d2f1a50ec54)static inline int [usbc\_vbus\_enable](group__usbc__vbus__api.md#ga7c94eac0f28be6cd12717d2f1a50ec54)(const struct [device](structdevice.md) \*dev, bool [enable](structusbc__vbus__driver__api.md#a5a7e6383279dc17c01d478a063efcac0))

100{

101 const struct [usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md) \*api = (const struct [usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

102

103 return api->[enable](structusbc__vbus__driver__api.md#a5a7e6383279dc17c01d478a063efcac0)(dev, [enable](structusbc__vbus__driver__api.md#a5a7e6383279dc17c01d478a063efcac0));

104}

105

109

110#ifdef \_\_cplusplus

111}

112#endif

113

114#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_VBUS\_H\_ \*/

[device.h](device_8h.md)

[tc\_vbus\_level](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161)

tc\_vbus\_level

VBUS level voltages.

**Definition** usbc\_tc.h:326

[usbc\_vbus\_measure](group__usbc__vbus__api.md#ga0b6c561c5f74a30d54397294cb21660d)

static int usbc\_vbus\_measure(const struct device \*dev, int \*meas)

Reads and returns VBUS measured in mV.

**Definition** usbc\_vbus.h:65

[usbc\_vbus\_check\_level](group__usbc__vbus__api.md#ga421653274fe9b8e2e6237a4bbe47e3ad)

static bool usbc\_vbus\_check\_level(const struct device \*dev, enum tc\_vbus\_level level)

Checks if VBUS is at a particular level.

**Definition** usbc\_vbus.h:49

[usbc\_vbus\_enable](group__usbc__vbus__api.md#ga7c94eac0f28be6cd12717d2f1a50ec54)

static int usbc\_vbus\_enable(const struct device \*dev, bool enable)

Controls a pin that enables VBUS measurments.

**Definition** usbc\_vbus.h:99

[usbc\_vbus\_discharge](group__usbc__vbus__api.md#ga8414cfcfeee7799ea57854c59c0c1677)

static int usbc\_vbus\_discharge(const struct device \*dev, bool enable)

Controls a pin that discharges VBUS.

**Definition** usbc\_vbus.h:82

[types.h](include_2zephyr_2types_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md)

**Definition** usbc\_vbus.h:33

[usbc\_vbus\_driver\_api::discharge](structusbc__vbus__driver__api.md#a164ae753995e293460fc408edebe21df)

int(\* discharge)(const struct device \*dev, bool enable)

**Definition** usbc\_vbus.h:36

[usbc\_vbus\_driver\_api::measure](structusbc__vbus__driver__api.md#a373b4435b3e4a1a88a78a15d24bdcbab)

int(\* measure)(const struct device \*dev, int \*vbus\_meas)

**Definition** usbc\_vbus.h:35

[usbc\_vbus\_driver\_api::enable](structusbc__vbus__driver__api.md#a5a7e6383279dc17c01d478a063efcac0)

int(\* enable)(const struct device \*dev, bool enable)

**Definition** usbc\_vbus.h:37

[usbc\_vbus\_driver\_api::check\_level](structusbc__vbus__driver__api.md#adce9dc1f3065a029b53ee954d734cfac)

bool(\* check\_level)(const struct device \*dev, enum tc\_vbus\_level level)

**Definition** usbc\_vbus.h:34

[usbc\_tc.h](usbc__tc_8h.md)

USB Type-C Cable and Connector API used for USB-C drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [usbc\_vbus.h](usbc__vbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
