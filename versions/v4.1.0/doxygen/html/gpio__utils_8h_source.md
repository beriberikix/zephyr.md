---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gpio__utils_8h_source.html
original_path: doxygen/html/gpio__utils_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_utils.h

[Go to the documentation of this file.](gpio__utils_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_UTILS\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_UTILS\_H\_

10

11#include <[stdbool.h](stdbool_8h.md)>

12#include <[stdint.h](stdint_8h.md)>

13#include <[errno.h](errno_8h.md)>

14

15#include <[zephyr/devicetree.h](devicetree_8h.md)>

16#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

17#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

18#include <[zephyr/sys/slist.h](slist_8h.md)>

19#include <[zephyr/tracing/tracing.h](tracing_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

[ 25](gpio__utils_8h.md#a696fbe0e6868902fbec77afc06f55e0a)#define GPIO\_PORT\_PIN\_MASK\_FROM\_NGPIOS(ngpios) \

26 ((gpio\_port\_pins\_t)(((uint64\_t)1 << (ngpios)) - 1U))

27

[ 36](gpio__utils_8h.md#a570c8e724c799b1bb0edeafa249d9730)#define GPIO\_PORT\_PIN\_MASK\_FROM\_DT\_NODE(node\_id) \

37 GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC(node\_id, DT\_PROP(node\_id, ngpios))

38

[ 47](gpio__utils_8h.md#a34528b682ca57bfc77cef745ed235e04)#define GPIO\_PORT\_PIN\_MASK\_FROM\_DT\_INST(inst) \

48 GPIO\_PORT\_PIN\_MASK\_FROM\_DT\_NODE(DT\_DRV\_INST(inst))

49

[ 59](gpio__utils_8h.md#ac9d36599625b79bd2ebb9f3603a2a122)static inline int [gpio\_manage\_callback](gpio__utils_8h.md#ac9d36599625b79bd2ebb9f3603a2a122)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*callbacks,

60 struct [gpio\_callback](structgpio__callback.md) \*callback,

61 bool set)

62{

63 \_\_ASSERT(callback, "No callback!");

64 \_\_ASSERT(callback->[handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb), "No callback handler!");

65

66 if (![sys\_slist\_is\_empty](group__single-linked-list__apis.md#ga7d729bbb7bba57c5784ad0d2c341670a)(callbacks)) {

67 if (![sys\_slist\_find\_and\_remove](group__single-linked-list__apis.md#ga296560229ffdfd0054c9c7b0602825a6)(callbacks, &callback->[node](structgpio__callback.md#ab60e7093072964bd818d536c746211e4))) {

68 if (!set) {

69 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

70 }

71 }

72 } else if (!set) {

73 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

74 }

75

76 if (set) {

77 [sys\_slist\_prepend](group__single-linked-list__apis.md#gac962e3ec8440e4adb2ba6682dbf186ff)(callbacks, &callback->[node](structgpio__callback.md#ab60e7093072964bd818d536c746211e4));

78 }

79

80 return 0;

81}

82

[ 90](gpio__utils_8h.md#ac7193ccc60e2f1c62569f80cd9973702)static inline void [gpio\_fire\_callbacks](gpio__utils_8h.md#ac7193ccc60e2f1c62569f80cd9973702)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list,

91 const struct [device](structdevice.md) \*port,

92 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pins)

93{

94 struct [gpio\_callback](structgpio__callback.md) \*cb, \*tmp;

95

96 [sys\_port\_trace\_gpio\_fire\_callbacks\_enter](group__subsys__tracing__apis__gpio.md#ga9cf081771e5f4724b02de3a89eec339c)(list, port, pins);

97

98 [SYS\_SLIST\_FOR\_EACH\_CONTAINER\_SAFE](group__single-linked-list__apis.md#gacf3aaf32a6a3389229b548588c6d655e)(list, cb, tmp, [node](structgpio__callback.md#ab60e7093072964bd818d536c746211e4)) {

99 if (cb->[pin\_mask](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67) & pins) {

100 \_\_ASSERT(cb->[handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb), "No callback handler!");

101

102 cb->[handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb)(port, cb, cb->[pin\_mask](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67) & pins);

103 [sys\_port\_trace\_gpio\_fire\_callback](group__subsys__tracing__apis__gpio.md#gaed3026e592853a9a97c0900a0687974b)(port, cb);

104 }

105 }

106}

107

108#ifdef \_\_cplusplus

109}

110#endif

111

112#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_UTILS\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[errno.h](errno_8h.md)

System error numbers.

[gpio\_fire\_callbacks](gpio__utils_8h.md#ac7193ccc60e2f1c62569f80cd9973702)

static void gpio\_fire\_callbacks(sys\_slist\_t \*list, const struct device \*port, uint32\_t pins)

Generic function to go through and fire callback from a callback list.

**Definition** gpio\_utils.h:90

[gpio\_manage\_callback](gpio__utils_8h.md#ac9d36599625b79bd2ebb9f3603a2a122)

static int gpio\_manage\_callback(sys\_slist\_t \*callbacks, struct gpio\_callback \*callback, bool set)

Generic function to insert or remove a callback from a callback list.

**Definition** gpio\_utils.h:59

[sys\_slist\_find\_and\_remove](group__single-linked-list__apis.md#ga296560229ffdfd0054c9c7b0602825a6)

static bool sys\_slist\_find\_and\_remove(sys\_slist\_t \*list, sys\_snode\_t \*node)

Find and remove a node from a list.

**Definition** slist.h:450

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_slist\_is\_empty](group__single-linked-list__apis.md#ga7d729bbb7bba57c5784ad0d2c341670a)

static bool sys\_slist\_is\_empty(sys\_slist\_t \*list)

Test if the given list is empty.

**Definition** slist.h:268

[sys\_slist\_prepend](group__single-linked-list__apis.md#gac962e3ec8440e4adb2ba6682dbf186ff)

static void sys\_slist\_prepend(sys\_slist\_t \*list, sys\_snode\_t \*node)

Prepend a node to the given list.

**Definition** slist.h:305

[SYS\_SLIST\_FOR\_EACH\_CONTAINER\_SAFE](group__single-linked-list__apis.md#gacf3aaf32a6a3389229b548588c6d655e)

#define SYS\_SLIST\_FOR\_EACH\_CONTAINER\_SAFE(\_\_sl, \_\_cn, \_\_cns, \_\_n)

Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached,...

**Definition** slist.h:183

[sys\_port\_trace\_gpio\_fire\_callbacks\_enter](group__subsys__tracing__apis__gpio.md#ga9cf081771e5f4724b02de3a89eec339c)

#define sys\_port\_trace\_gpio\_fire\_callbacks\_enter(list, port, pins)

**Definition** tracing.h:2708

[sys\_port\_trace\_gpio\_fire\_callback](group__subsys__tracing__apis__gpio.md#gaed3026e592853a9a97c0900a0687974b)

#define sys\_port\_trace\_gpio\_fire\_callback(port, callback)

**Definition** tracing.h:2715

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[slist.h](slist_8h.md)

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[gpio\_callback](structgpio__callback.md)

GPIO callback structure.

**Definition** gpio.h:741

[gpio\_callback::node](structgpio__callback.md#ab60e7093072964bd818d536c746211e4)

sys\_snode\_t node

This is meant to be used in the driver and the user should not mess with it (see drivers/gpio/gpio\_ut...

**Definition** gpio.h:745

[gpio\_callback::pin\_mask](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67)

gpio\_port\_pins\_t pin\_mask

A mask of pins the callback is interested in, if 0 the callback will never be called.

**Definition** gpio.h:756

[gpio\_callback::handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb)

gpio\_callback\_handler\_t handler

Actual callback function being called when relevant.

**Definition** gpio.h:748

[tracing.h](tracing_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_utils.h](gpio__utils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
