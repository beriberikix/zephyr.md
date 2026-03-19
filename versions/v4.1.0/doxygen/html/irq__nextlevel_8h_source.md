---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/irq__nextlevel_8h_source.html
original_path: doxygen/html/irq__nextlevel_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq\_nextlevel.h

[Go to the documentation of this file.](irq__nextlevel_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11#ifndef ZEPHYR\_INCLUDE\_IRQ\_NEXTLEVEL\_H\_

12#define ZEPHYR\_INCLUDE\_IRQ\_NEXTLEVEL\_H\_

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18#if defined(CONFIG\_MULTI\_LEVEL\_INTERRUPTS) || defined(\_\_DOXYGEN\_\_)

25typedef void (\*irq\_next\_level\_func\_t)(const struct [device](structdevice.md) \*dev,

26 unsigned int irq);

27typedef unsigned int (\*irq\_next\_level\_get\_state\_t)(const struct [device](structdevice.md) \*dev);

28typedef void (\*irq\_next\_level\_priority\_t)(const struct [device](structdevice.md) \*dev,

29 unsigned int irq, unsigned int prio,

30 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

31typedef int (\*irq\_next\_level\_get\_line\_state\_t)(const struct [device](structdevice.md) \*dev,

32 unsigned int irq);

33

34struct irq\_next\_level\_api {

35 irq\_next\_level\_func\_t intr\_enable;

36 irq\_next\_level\_func\_t intr\_disable;

37 irq\_next\_level\_get\_state\_t intr\_get\_state;

38 irq\_next\_level\_priority\_t intr\_set\_priority;

39 irq\_next\_level\_get\_line\_state\_t intr\_get\_line\_state;

40};

44

[ 53](irq__nextlevel_8h.md#a335d42cf95c25ab8564475c4b4c3ead9)static inline void [irq\_enable\_next\_level](irq__nextlevel_8h.md#a335d42cf95c25ab8564475c4b4c3ead9)(const struct [device](structdevice.md) \*dev,

54 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq)

55{

56 const struct irq\_next\_level\_api \*api =

57 (const struct irq\_next\_level\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

58

59 api->intr\_enable(dev, irq);

60}

61

[ 70](irq__nextlevel_8h.md#ad694fcad4c3fba0d2794cdc34ddcd1bb)static inline void [irq\_disable\_next\_level](irq__nextlevel_8h.md#ad694fcad4c3fba0d2794cdc34ddcd1bb)(const struct [device](structdevice.md) \*dev,

71 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq)

72{

73 const struct irq\_next\_level\_api \*api =

74 (const struct irq\_next\_level\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

75

76 api->intr\_disable(dev, irq);

77}

78

[ 89](irq__nextlevel_8h.md#aa7178acd1058940b83c7c7500217bc01)static inline unsigned int [irq\_is\_enabled\_next\_level](irq__nextlevel_8h.md#aa7178acd1058940b83c7c7500217bc01)(const struct [device](structdevice.md) \*dev)

90{

91 const struct irq\_next\_level\_api \*api =

92 (const struct irq\_next\_level\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

93

94 return api->intr\_get\_state(dev);

95}

96

[ 108](irq__nextlevel_8h.md#af41789f946ebb445f4a402009ed2e8bb)static inline void [irq\_set\_priority\_next\_level](irq__nextlevel_8h.md#af41789f946ebb445f4a402009ed2e8bb)(const struct [device](structdevice.md) \*dev,

109 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq,

110 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

111{

112 const struct irq\_next\_level\_api \*api =

113 (const struct irq\_next\_level\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

114

115 if (api->intr\_set\_priority)

116 api->intr\_set\_priority(dev, irq, prio, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

117}

118

[ 129](irq__nextlevel_8h.md#a7e0e5fe59eae08878a8f243dd9301633)static inline unsigned int [irq\_line\_is\_enabled\_next\_level](irq__nextlevel_8h.md#a7e0e5fe59eae08878a8f243dd9301633)(const struct [device](structdevice.md) \*dev,

130 unsigned int irq)

131{

132 const struct irq\_next\_level\_api \*api =

133 (const struct irq\_next\_level\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

134

135 return api->intr\_get\_line\_state(dev, irq);

136}

137

138#endif /\* CONFIG\_MULTI\_LEVEL\_INTERRUPTS \*/

139#ifdef \_\_cplusplus

140}

141#endif

142

143#endif /\* ZEPHYR\_INCLUDE\_IRQ\_NEXTLEVEL\_H\_ \*/

[irq\_enable\_next\_level](irq__nextlevel_8h.md#a335d42cf95c25ab8564475c4b4c3ead9)

static void irq\_enable\_next\_level(const struct device \*dev, uint32\_t irq)

Enable an IRQ in the next level.

**Definition** irq\_nextlevel.h:53

[irq\_line\_is\_enabled\_next\_level](irq__nextlevel_8h.md#a7e0e5fe59eae08878a8f243dd9301633)

static unsigned int irq\_line\_is\_enabled\_next\_level(const struct device \*dev, unsigned int irq)

Get IRQ line enable state.

**Definition** irq\_nextlevel.h:129

[irq\_is\_enabled\_next\_level](irq__nextlevel_8h.md#aa7178acd1058940b83c7c7500217bc01)

static unsigned int irq\_is\_enabled\_next\_level(const struct device \*dev)

Get IRQ enable state.

**Definition** irq\_nextlevel.h:89

[irq\_disable\_next\_level](irq__nextlevel_8h.md#ad694fcad4c3fba0d2794cdc34ddcd1bb)

static void irq\_disable\_next\_level(const struct device \*dev, uint32\_t irq)

Disable an IRQ in the next level.

**Definition** irq\_nextlevel.h:70

[irq\_set\_priority\_next\_level](irq__nextlevel_8h.md#af41789f946ebb445f4a402009ed2e8bb)

static void irq\_set\_priority\_next\_level(const struct device \*dev, uint32\_t irq, uint32\_t prio, uint32\_t flags)

Set IRQ priority.

**Definition** irq\_nextlevel.h:108

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [irq\_nextlevel.h](irq__nextlevel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
