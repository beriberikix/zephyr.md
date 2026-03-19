---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/apds9253_8h_source.html
original_path: doxygen/html/apds9253_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

apds9253.h

[Go to the documentation of this file.](apds9253_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \* Copyright (c) 2018 PHYTEC Messtechnik GmbH

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_SENSOR\_APDS9253\_H\_

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_SENSOR\_APDS9253\_H\_

10

11#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

12

17

[ 18](apds9253_8h.md#a7ad23d39c8dc7ddf7a457e97d70f6177)#define APDS9253\_RESOLUTION\_20BIT\_400MS 0

[ 19](apds9253_8h.md#a8a497ca5f4c73858ff7fef856d3a45ac)#define APDS9253\_RESOLUTION\_19BIT\_200MS BIT(4)

[ 20](apds9253_8h.md#aca7dd96545b1f87a258d8692934eac26)#define APDS9253\_RESOLUTION\_18BIT\_100MS BIT(5) /\* default \*/

[ 21](apds9253_8h.md#a16dbc6c091d618c92446c45be558793e)#define APDS9253\_RESOLUTION\_17BIT\_50MS (BIT(5) | BIT(4))

[ 22](apds9253_8h.md#a78feda7057bc90b389dfa7107911324c)#define APDS9253\_RESOLUTION\_16BIT\_25MS BIT(6)

[ 23](apds9253_8h.md#a1a702ceafbc73c81e1fe3c8ccfc8fb9d)#define APDS9253\_RESOLUTION\_13BIT\_3MS (BIT(6) | BIT(4))

24

26

31

[ 32](apds9253_8h.md#aeb9d64852128e7186fc29f47148f8472)#define APDS9253\_MEASUREMENT\_RATE\_2000MS (BIT(2) | BIT(1) | BIT(0))

[ 33](apds9253_8h.md#ad5bf06634bc4a286ea061e52f7b38caf)#define APDS9253\_MEASUREMENT\_RATE\_1000MS (BIT(2) | BIT(0))

[ 34](apds9253_8h.md#ab028d789030caa61cc6576bc512cea51)#define APDS9253\_MEASUREMENT\_RATE\_500MS BIT(2)

[ 35](apds9253_8h.md#a2c7000f66a61442b67cec8123921de7a)#define APDS9253\_MEASUREMENT\_RATE\_200MS (BIT(1) | BIT(0))

[ 36](apds9253_8h.md#afac03ab9dfcec1352379e8f4843bf2f3)#define APDS9253\_MEASUREMENT\_RATE\_100MS BIT(1) /\* default \*/

[ 37](apds9253_8h.md#aff4512ccaaebc9552566229906a74444)#define APDS9253\_MEASUREMENT\_RATE\_50MS BIT(0)

[ 38](apds9253_8h.md#a84fa65b7d6da23e84d9150c9aeca72b1)#define APDS9253\_MEASUREMENT\_RATE\_25MS 0

39

41

46

[ 47](apds9253_8h.md#aa51f4c026e87de98d060f338e7cb020d)#define APDS9253\_GAIN\_RANGE\_18 BIT(2)

[ 48](apds9253_8h.md#a48961f6b63d915eb96ea13b235ca14fa)#define APDS9253\_GAIN\_RANGE\_9 (BIT(1) | BIT(0))

[ 49](apds9253_8h.md#adf8d5b7fa484322cb25026a851346a60)#define APDS9253\_GAIN\_RANGE\_6 BIT(1)

[ 50](apds9253_8h.md#a0ae5f62dc95dd84d8310e08bec8902a0)#define APDS9253\_GAIN\_RANGE\_3 BIT(0) /\* default \*/

[ 51](apds9253_8h.md#aefdb9ab4f906ef0ed294f1d20bd52dc2)#define APDS9253\_GAIN\_RANGE\_1 0

52

54

55#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_SENSOR\_APDS9253\_H\_\*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [apds9253.h](apds9253_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
