---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/nxp__flexram_8h_source.html
original_path: doxygen/html/nxp__flexram_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_flexram.h

[Go to the documentation of this file.](nxp__flexram_8h.md)

1/\*

2 \* Copyright 2023-2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[zephyr/devicetree.h](devicetree_8h.md)>

8#include <soc.h>

9

[ 10](nxp__flexram_8h.md#a0d3dc261902786b3dc55a1d0bc56d29e)#define FLEXRAM\_DT\_NODE DT\_INST(0, nxp\_flexram)

[ 11](nxp__flexram_8h.md#a7f83e0e78eef3970396edc636431519b)#define IOMUXC\_GPR\_DT\_NODE DT\_NODELABEL(iomuxcgpr)

12

13#if defined(CONFIG\_NXP\_FLEXRAM\_MAGIC\_ADDR\_API) || \

14 defined(CONFIG\_NXP\_FLEXRAM\_ERROR\_INTERRUPT)

15#define FLEXRAM\_INTERRUPTS\_USED

16#endif

17

18#if DT\_PROP\_HAS\_IDX(FLEXRAM\_DT\_NODE, flexram\_bank\_spec, 0)

19#define FLEXRAM\_RUNTIME\_BANKS\_USED 1

20#endif

21

22#ifdef FLEXRAM\_INTERRUPTS\_USED

23enum flexram\_interrupt\_cause {

24#ifdef CONFIG\_NXP\_FLEXRAM\_ERROR\_INTERRUPT

25 flexram\_ocram\_access\_error,

26 flexram\_itcm\_access\_error,

27 flexram\_dtcm\_access\_error,

28#endif

29#ifdef CONFIG\_NXP\_FLEXRAM\_MAGIC\_ADDR\_API

30 flexram\_ocram\_magic\_addr,

31 flexram\_itcm\_magic\_addr,

32 flexram\_dtcm\_magic\_addr,

33#endif /\* CONFIG\_NXP\_FLEXRAM\_MAGIC\_ADDR\_API \*/

34};

35

36typedef void (\*flexram\_callback\_t)(enum flexram\_interrupt\_cause, void \*user\_data);

37

38void flexram\_register\_callback(flexram\_callback\_t callback, void \*user\_data);

39#endif /\* FLEXRAM\_INTERRUPTS\_USED \*/

40

41#ifdef FLEXRAM\_RUNTIME\_BANKS\_USED

42

43/\*

44 \* call from platform\_init to set up flexram if using runtime map

45 \* must be inlined because cannot use stack

46 \*/

47#define GPR\_FLEXRAM\_REG\_FILL(node\_id, prop, idx) \

48 (((uint32\_t)DT\_PROP\_BY\_IDX(node\_id, prop, idx)) << (2 \* idx))

49static inline void flexram\_dt\_partition(void)

50{

51 /\* iomuxc\_gpr must be const (in ROM region) because used in reconfiguring ram \*/

52 static IOMUXC\_GPR\_Type \*const iomuxc\_gpr =

53 (IOMUXC\_GPR\_Type \*)[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)([IOMUXC\_GPR\_DT\_NODE](nxp__flexram_8h.md#a7f83e0e78eef3970396edc636431519b));

54 /\* do not create stack variables or use any data from ram in this function \*/

55#if defined(CONFIG\_SOC\_SERIES\_IMXRT11XX)

56 iomuxc\_gpr->GPR17 = ([DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)([FLEXRAM\_DT\_NODE](nxp__flexram_8h.md#a0d3dc261902786b3dc55a1d0bc56d29e), flexram\_bank\_spec,

57 GPR\_FLEXRAM\_REG\_FILL, (+))) & 0xFFFF;

58 iomuxc\_gpr->GPR18 = ((([DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)([FLEXRAM\_DT\_NODE](nxp__flexram_8h.md#a0d3dc261902786b3dc55a1d0bc56d29e), flexram\_bank\_spec,

59 GPR\_FLEXRAM\_REG\_FILL, (+)))) >> 16) & 0xFFFF;

60#elif defined(CONFIG\_SOC\_SERIES\_IMXRT10XX)

61 iomuxc\_gpr->GPR17 = [DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)([FLEXRAM\_DT\_NODE](nxp__flexram_8h.md#a0d3dc261902786b3dc55a1d0bc56d29e), flexram\_bank\_spec,

62 GPR\_FLEXRAM\_REG\_FILL, (+));

63#endif

64 iomuxc\_gpr->GPR16 |= IOMUXC\_GPR\_GPR16\_FLEXRAM\_BANK\_CFG\_SEL\_MASK;

65}

66#endif /\* FLEXRAM\_RUNTIME\_BANKS\_USED \*/

67

68#ifdef CONFIG\_NXP\_FLEXRAM\_MAGIC\_ADDR\_API

79int flexram\_set\_ocram\_magic\_addr([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ocram\_addr);

80

91int flexram\_set\_itcm\_magic\_addr([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) itcm\_addr);

92

103int flexram\_set\_dtcm\_magic\_addr([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dtcm\_addr);

104

105#endif /\* CONFIG\_NXP\_FLEXRAM\_MAGIC\_ADDR\_API \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)

#define DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, prop, fn, sep)

Invokes fn for each element in the value of property prop with separator.

**Definition** devicetree.h:3367

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2461

[FLEXRAM\_DT\_NODE](nxp__flexram_8h.md#a0d3dc261902786b3dc55a1d0bc56d29e)

#define FLEXRAM\_DT\_NODE

**Definition** nxp\_flexram.h:10

[IOMUXC\_GPR\_DT\_NODE](nxp__flexram_8h.md#a7f83e0e78eef3970396edc636431519b)

#define IOMUXC\_GPR\_DT\_NODE

**Definition** nxp\_flexram.h:11

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [flexram](dir_86d967f414985149d870e265b4178619.md)
- [nxp\_flexram.h](nxp__flexram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
