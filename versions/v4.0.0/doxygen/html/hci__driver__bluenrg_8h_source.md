---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hci__driver__bluenrg_8h_source.html
original_path: doxygen/html/hci__driver__bluenrg_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci\_driver\_bluenrg.h

[Go to the documentation of this file.](hci__driver__bluenrg_8h.md)

1

4

5/\*

6 \* Copyright (c) 2024 STMicroelectronics

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_BLUETOOTH\_HCI\_DRIVER\_BLUENRG\_H\_

11#define ZEPHYR\_INCLUDE\_DRIVERS\_BLUETOOTH\_HCI\_DRIVER\_BLUENRG\_H\_

12

19

20#include <[stdbool.h](stdbool_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

36

[ 37](group__bluenrg__hci__driver.md#gaa76b4af2fc2076deaeeb845514475483)int [bluenrg\_bt\_reset](group__bluenrg__hci__driver.md#gaa76b4af2fc2076deaeeb845514475483)(bool updater\_mode);

38

39#ifdef \_\_cplusplus

40}

41#endif

42

46

47#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_BLUETOOTH\_HCI\_DRIVER\_BLUENRG\_H\_ \*/

[bluenrg\_bt\_reset](group__bluenrg__hci__driver.md#gaa76b4af2fc2076deaeeb845514475483)

int bluenrg\_bt\_reset(bool updater\_mode)

Hardware reset the BlueNRG network coprocessor.

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [bluetooth](dir_95992648d5602e5c89adafd44bf19e08.md)
- [hci\_driver\_bluenrg.h](hci__driver__bluenrg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
