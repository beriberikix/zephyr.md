---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pinctrl__soc__kinetis__common_8h_source.html
original_path: doxygen/html/pinctrl__soc__kinetis__common_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_soc\_kinetis\_common.h

[Go to the documentation of this file.](pinctrl__soc__kinetis__common_8h.md)

1/\*

2 \* Copyright 2022, 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\*

8 \* @file

9 \* NXP Kinetis SOC specific helpers for pinctrl driver

10 \*/

11

12

13#ifndef ZEPHYR\_SOC\_ARM\_NXP\_KINETIS\_COMMON\_PINCTRL\_SOC\_H\_

14#define ZEPHYR\_SOC\_ARM\_NXP\_KINETIS\_COMMON\_PINCTRL\_SOC\_H\_

15

17

18#include <[zephyr/devicetree.h](devicetree_8h.md)>

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

25

26typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d);

27

28/\* Kinetis KW/KL/KE series does not support open drain. Define macros to have no effect

29 \* Note: KW22 and KW24 do support open drain, rest of KW series does not

30 \*/

31/\* clang-format off \*/

32#if (defined(CONFIG\_SOC\_SERIES\_KINETIS\_KWX) && \

33 !(defined(CONFIG\_SOC\_MKW24D5) || defined(CONFIG\_SOC\_MKW22D5))) || \

34 defined(CONFIG\_SOC\_SERIES\_KINETIS\_KL2X) || defined(CONFIG\_SOC\_SERIES\_KINETIS\_KE1XF) || \

35 defined(CONFIG\_SOC\_SERIES\_KE1XZ)

36#define PORT\_PCR\_ODE(x) 0x0

37#define PORT\_PCR\_ODE\_MASK 0x0

38#endif

39/\* clang-format on \*/

40

41/\* Kinetis KE series does not support slew rate. Define macros to have no effect \*/

42#if defined(CONFIG\_SOC\_SERIES\_KINETIS\_KE1XF) || defined(CONFIG\_SOC\_SERIES\_KE1XZ)

43#define PORT\_PCR\_SRE(x) 0x0

44#define PORT\_PCR\_SRE\_MASK 0x0

45#endif

46

47#if !(defined(CONFIG\_SOC\_SERIES\_MCXA))

48#define PORT\_PCR\_IBE(x) 0x0

49#define PORT\_PCR\_IBE\_MASK 0x0

50#endif

51

52#define Z\_PINCTRL\_KINETIS\_PINCFG(node\_id) \

53 (PORT\_PCR\_DSE(DT\_ENUM\_IDX(node\_id, drive\_strength)) | \

54 PORT\_PCR\_PS(DT\_PROP(node\_id, bias\_pull\_up)) | \

55 PORT\_PCR\_PE(DT\_PROP(node\_id, bias\_pull\_up)) | \

56 PORT\_PCR\_PE(DT\_PROP(node\_id, bias\_pull\_down)) | \

57 PORT\_PCR\_ODE(DT\_PROP(node\_id, drive\_open\_drain)) | \

58 PORT\_PCR\_SRE(DT\_ENUM\_IDX(node\_id, slew\_rate)) | \

59 PORT\_PCR\_IBE(DT\_PROP(node\_id, input\_enable)) | \

60 PORT\_PCR\_PFE(DT\_PROP(node\_id, nxp\_passive\_filter)))

61

62#define Z\_PINCTRL\_KINETIS\_PCR\_MASK \

63 (PORT\_PCR\_MUX\_MASK | PORT\_PCR\_DSE\_MASK | PORT\_PCR\_ODE\_MASK | PORT\_PCR\_PFE\_MASK | \

64 PORT\_PCR\_IBE\_MASK | PORT\_PCR\_SRE\_MASK | PORT\_PCR\_PE\_MASK | PORT\_PCR\_PS\_MASK)

65

66#define Z\_PINCTRL\_STATE\_PIN\_INIT(group, pin\_prop, idx) \

67 DT\_PROP\_BY\_IDX(group, pin\_prop, idx) | Z\_PINCTRL\_KINETIS\_PINCFG(group),

68

69#define Z\_PINCTRL\_STATE\_PINS\_INIT(node\_id, prop) \

70 {DT\_FOREACH\_CHILD\_VARGS(DT\_PHANDLE(node\_id, prop), DT\_FOREACH\_PROP\_ELEM, pinmux, \

71 Z\_PINCTRL\_STATE\_PIN\_INIT)};

72

73#ifdef \_\_cplusplus

74}

75#endif

76

78

79#endif /\* ZEPHYR\_SOC\_ARM\_NXP\_KINETIS\_COMMON\_PINCTRL\_SOC\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[types.h](include_2zephyr_2types_8h.md)

[pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d)

struct pinctrl\_soc\_pin pinctrl\_soc\_pin\_t

Type for R-Car pin.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pinctrl](dir_c0bb3bf986f9412b3a6b9d85dc06c157.md)
- [pinctrl\_soc\_kinetis\_common.h](pinctrl__soc__kinetis__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
