---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pinctrl__nxp__port__common_8h_source.html
original_path: doxygen/html/pinctrl__nxp__port__common_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_nxp\_port\_common.h

[Go to the documentation of this file.](pinctrl__nxp__port__common_8h.md)

1/\*

2 \* Copyright 2022, 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\*

8 \* @file

9 \* NXP PORT SOC specific helpers for pinctrl driver

10 \*/

11

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_NXP\_PORT\_COMMON\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_NXP\_PORT\_COMMON\_H\_

15

17

18#include <[zephyr/devicetree.h](devicetree_8h.md)>

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20

21/\* Include SOC headers, so we get definitions for PCR bitmasks \*/

22#include <soc.h>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

28/\*

29 \* Some PORT IP instantiations lack certain features, include input buffers,

30 \* open drain, and slew rate. If masks aren't defined for these bitfields,

31 \* define them to have no effect

32 \*/

33#ifndef PORT\_PCR\_IBE\_MASK /\* Input buffer enable \*/

34#define PORT\_PCR\_IBE\_MASK 0x0

35#define PORT\_PCR\_IBE(x) 0x0

36#endif

37

38#ifndef PORT\_PCR\_SRE\_MASK /\* Slew rate \*/

39#define PORT\_PCR\_SRE\_MASK 0x0

40#define PORT\_PCR\_SRE(x) 0x0

41#endif

42

43#ifndef PORT\_PCR\_ODE\_MASK /\* Open drain \*/

44#define PORT\_PCR\_ODE\_MASK 0x0

45#define PORT\_PCR\_ODE(x) 0x0

46#endif

47

48

49typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d);

50

51#define Z\_PINCTRL\_NXP\_PORT\_PINCFG(node\_id) \

52 (PORT\_PCR\_DSE(DT\_ENUM\_IDX(node\_id, drive\_strength)) | \

53 PORT\_PCR\_PS(DT\_PROP(node\_id, bias\_pull\_up)) | \

54 PORT\_PCR\_PE(DT\_PROP(node\_id, bias\_pull\_up)) | \

55 PORT\_PCR\_PE(DT\_PROP(node\_id, bias\_pull\_down)) | \

56 PORT\_PCR\_ODE(DT\_PROP(node\_id, drive\_open\_drain)) | \

57 PORT\_PCR\_SRE(DT\_ENUM\_IDX(node\_id, slew\_rate)) | \

58 PORT\_PCR\_IBE(DT\_PROP(node\_id, input\_enable)) | \

59 PORT\_PCR\_PFE(DT\_PROP(node\_id, nxp\_passive\_filter)))

60

61#define Z\_PINCTRL\_NXP\_PORT\_PCR\_MASK \

62 (PORT\_PCR\_MUX\_MASK | PORT\_PCR\_DSE\_MASK | PORT\_PCR\_ODE\_MASK | PORT\_PCR\_PFE\_MASK | \

63 PORT\_PCR\_IBE\_MASK | PORT\_PCR\_SRE\_MASK | PORT\_PCR\_PE\_MASK | PORT\_PCR\_PS\_MASK)

64

65#define Z\_PINCTRL\_STATE\_PIN\_INIT(group, pin\_prop, idx) \

66 DT\_PROP\_BY\_IDX(group, pin\_prop, idx) | Z\_PINCTRL\_NXP\_PORT\_PINCFG(group),

67

68#define Z\_PINCTRL\_STATE\_PINS\_INIT(node\_id, prop) \

69 {DT\_FOREACH\_CHILD\_VARGS(DT\_PHANDLE(node\_id, prop), DT\_FOREACH\_PROP\_ELEM, pinmux, \

70 Z\_PINCTRL\_STATE\_PIN\_INIT)};

71

72#ifdef \_\_cplusplus

73}

74#endif

75

77

78#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_NXP\_PORT\_COMMON\_H\_ \*/

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
- [pinctrl\_nxp\_port\_common.h](pinctrl__nxp__port__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
