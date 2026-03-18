---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/grow__r502a_8h_source.html
original_path: doxygen/html/grow__r502a_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

grow\_r502a.h

[Go to the documentation of this file.](grow__r502a_8h.md)

1/\*

2 \* Copyright (c) 2022 Linumiz

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_GROW\_R502A\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_GROW\_R502A\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

15

[ 16](grow__r502a_8h.md#a8ff24814059dda20e6b36fe8cc0be30c)enum [sensor\_channel\_grow\_r502a](grow__r502a_8h.md#a8ff24814059dda20e6b36fe8cc0be30c) {

[ 18](grow__r502a_8h.md#a8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2) [SENSOR\_CHAN\_FINGERPRINT](grow__r502a_8h.md#a8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

19};

20

[ 21](grow__r502a_8h.md#a721dcba985d9010bb1f48e82b0027eb4)enum [sensor\_trigger\_type\_grow\_r502a](grow__r502a_8h.md#a721dcba985d9010bb1f48e82b0027eb4) {

[ 23](grow__r502a_8h.md#a721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4) [SENSOR\_TRIG\_TOUCH](grow__r502a_8h.md#a721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4) = [SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921),

24};

25

[ 26](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684b)enum [sensor\_attribute\_grow\_r502a](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684b) {

[ 28](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb) [SENSOR\_ATTR\_R502A\_RECORD\_ADD](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 30](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922) [SENSOR\_ATTR\_R502A\_RECORD\_FIND](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922),

[ 32](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef) [SENSOR\_ATTR\_R502A\_RECORD\_DEL](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef),

[ 34](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df) [SENSOR\_ATTR\_R502A\_RECORD\_FREE\_IDX](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df),

[ 36](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b) [SENSOR\_ATTR\_R502A\_RECORD\_EMPTY](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b),

37};

38

39#ifdef \_\_cplusplus

40}

41#endif

42

43#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_DRIVERS\_SENSOR\_GROW\_R502A\_H\_ \*/

[SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)

@ SENSOR\_TRIG\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:269

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:350

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:202

[sensor\_attribute\_grow\_r502a](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684b)

sensor\_attribute\_grow\_r502a

**Definition** grow\_r502a.h:26

[SENSOR\_ATTR\_R502A\_RECORD\_ADD](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb)

@ SENSOR\_ATTR\_R502A\_RECORD\_ADD

Add values to the sensor which are having record storage facility.

**Definition** grow\_r502a.h:28

[SENSOR\_ATTR\_R502A\_RECORD\_DEL](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef)

@ SENSOR\_ATTR\_R502A\_RECORD\_DEL

To delete mentioned data from record storage.

**Definition** grow\_r502a.h:32

[SENSOR\_ATTR\_R502A\_RECORD\_FREE\_IDX](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df)

@ SENSOR\_ATTR\_R502A\_RECORD\_FREE\_IDX

To get available position to store data on record storage.

**Definition** grow\_r502a.h:34

[SENSOR\_ATTR\_R502A\_RECORD\_EMPTY](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b)

@ SENSOR\_ATTR\_R502A\_RECORD\_EMPTY

To empty the storage record.

**Definition** grow\_r502a.h:36

[SENSOR\_ATTR\_R502A\_RECORD\_FIND](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922)

@ SENSOR\_ATTR\_R502A\_RECORD\_FIND

To find requested data in record storage.

**Definition** grow\_r502a.h:30

[sensor\_trigger\_type\_grow\_r502a](grow__r502a_8h.md#a721dcba985d9010bb1f48e82b0027eb4)

sensor\_trigger\_type\_grow\_r502a

**Definition** grow\_r502a.h:21

[SENSOR\_TRIG\_TOUCH](grow__r502a_8h.md#a721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4)

@ SENSOR\_TRIG\_TOUCH

Trigger fires when a touch is detected.

**Definition** grow\_r502a.h:23

[sensor\_channel\_grow\_r502a](grow__r502a_8h.md#a8ff24814059dda20e6b36fe8cc0be30c)

sensor\_channel\_grow\_r502a

**Definition** grow\_r502a.h:16

[SENSOR\_CHAN\_FINGERPRINT](grow__r502a_8h.md#a8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2)

@ SENSOR\_CHAN\_FINGERPRINT

Fingerprint template count, ID number for enrolling and searching.

**Definition** grow\_r502a.h:18

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [grow\_r502a.h](grow__r502a_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
