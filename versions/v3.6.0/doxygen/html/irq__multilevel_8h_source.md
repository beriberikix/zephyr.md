---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/irq__multilevel_8h_source.html
original_path: doxygen/html/irq__multilevel_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq\_multilevel.h

[Go to the documentation of this file.](irq__multilevel_8h.md)

1/\*

2 \* Copyright (c) 2023 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11#ifndef ZEPHYR\_INCLUDE\_IRQ\_MULTILEVEL\_H\_

12#define ZEPHYR\_INCLUDE\_IRQ\_MULTILEVEL\_H\_

13

14#ifndef \_ASMLANGUAGE

15#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

22#if defined(CONFIG\_MULTI\_LEVEL\_INTERRUPTS) || defined(\_\_DOXYGEN\_\_)

[ 31](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)static inline unsigned int [irq\_get\_level](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)(unsigned int irq)

32{

33 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask2 = [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS) <<

34 CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS;

35 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask3 = [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(CONFIG\_3RD\_LEVEL\_INTERRUPT\_BITS) <<

36 (CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS + CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS);

37

38 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_3RD\_LEVEL\_INTERRUPTS) && (irq & mask3) != 0) {

39 return 3;

40 }

41

42 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_2ND\_LEVEL\_INTERRUPTS) && (irq & mask2) != 0) {

43 return 2;

44 }

45

46 return 1;

47}

48

[ 59](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)static inline unsigned int [irq\_from\_level\_2](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)(unsigned int irq)

60{

61 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_3RD\_LEVEL\_INTERRUPTS)) {

62 return ((irq >> CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS) &

63 [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS)) - 1;

64 } else {

65 return (irq >> CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS) - 1;

66 }

67}

68

[ 76](irq__multilevel_8h.md#a9a94c2cecb8c8d3394c1ff5ed3cc4db3)#define IRQ\_TO\_L2(irq) ((irq + 1) << CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS)

77

[ 90](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)static inline unsigned int [irq\_to\_level\_2](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)(unsigned int irq)

91{

92 return [IRQ\_TO\_L2](irq__multilevel_8h.md#a9a94c2cecb8c8d3394c1ff5ed3cc4db3)(irq);

93}

94

[ 105](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)static inline unsigned int [irq\_parent\_level\_2](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)(unsigned int irq)

106{

107 return irq & [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS);

108}

109

[ 121](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)static inline unsigned int [irq\_from\_level\_3](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)(unsigned int irq)

122{

123 return (irq >> (CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS + CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS)) - 1;

124}

125

[ 133](irq__multilevel_8h.md#a1aa1eaa367e7c8baa250900de4eb0daf)#define IRQ\_TO\_L3(irq) \

134 ((irq + 1) << (CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS + CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS))

135

[ 148](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)static inline unsigned int [irq\_to\_level\_3](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)(unsigned int irq)

149{

150 return [IRQ\_TO\_L3](irq__multilevel_8h.md#a1aa1eaa367e7c8baa250900de4eb0daf)(irq);

151}

152

[ 163](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)static inline unsigned int [irq\_parent\_level\_3](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)(unsigned int irq)

164{

165 return (irq >> CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS) &

166 [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS);

167}

168

169#endif /\* CONFIG\_MULTI\_LEVEL\_INTERRUPTS \*/

170#ifdef \_\_cplusplus

171}

172#endif

173

174#endif /\* \_ASMLANGUAGE \*/

175#endif /\* ZEPHYR\_INCLUDE\_IRQ\_MULTILEVEL\_H\_ \*/

[BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)

#define BIT\_MASK(n)

**Definition** adc.h:14

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

[types.h](include_2zephyr_2types_8h.md)

[IRQ\_TO\_L3](irq__multilevel_8h.md#a1aa1eaa367e7c8baa250900de4eb0daf)

#define IRQ\_TO\_L3(irq)

Preprocessor macro to convert irq from level 1 to level 3 format.

**Definition** irq\_multilevel.h:133

[irq\_to\_level\_3](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)

static unsigned int irq\_to\_level\_3(unsigned int irq)

Converts irq from level 1 to level 3 format.

**Definition** irq\_multilevel.h:148

[irq\_from\_level\_3](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)

static unsigned int irq\_from\_level\_3(unsigned int irq)

Return the 3rd level interrupt number.

**Definition** irq\_multilevel.h:121

[irq\_from\_level\_2](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)

static unsigned int irq\_from\_level\_2(unsigned int irq)

Return the 2nd level interrupt number.

**Definition** irq\_multilevel.h:59

[irq\_get\_level](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)

static unsigned int irq\_get\_level(unsigned int irq)

Return IRQ level This routine returns the interrupt level number of the provided interrupt.

**Definition** irq\_multilevel.h:31

[irq\_to\_level\_2](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)

static unsigned int irq\_to\_level\_2(unsigned int irq)

Converts irq from level 1 to level 2 format.

**Definition** irq\_multilevel.h:90

[IRQ\_TO\_L2](irq__multilevel_8h.md#a9a94c2cecb8c8d3394c1ff5ed3cc4db3)

#define IRQ\_TO\_L2(irq)

Preprocessor macro to convert irq from level 1 to level 2 format.

**Definition** irq\_multilevel.h:76

[irq\_parent\_level\_2](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)

static unsigned int irq\_parent\_level\_2(unsigned int irq)

Returns the parent IRQ of the level 2 raw IRQ number.

**Definition** irq\_multilevel.h:105

[irq\_parent\_level\_3](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)

static unsigned int irq\_parent\_level\_3(unsigned int irq)

Returns the parent IRQ of the level 3 raw IRQ number.

**Definition** irq\_multilevel.h:163

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [irq\_multilevel.h](irq__multilevel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
