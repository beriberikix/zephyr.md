---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2coredump_8h_source.html
original_path: doxygen/html/drivers_2coredump_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coredump.h

[Go to the documentation of this file.](drivers_2coredump_8h.md)

1/\*

2 \* Copyright Meta Platforms, Inc. and its affiliates.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef INCLUDE\_ZEPHYR\_DRIVERS\_COREDUMP\_H\_

13#define INCLUDE\_ZEPHYR\_DRIVERS\_COREDUMP\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16#include <[zephyr/sys/slist.h](slist_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

28

[ 37](structcoredump__mem__region__node.md)struct [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) {

[ 39](structcoredump__mem__region__node.md#a41fb46fe6748ee9d4a2a4b8cd2230000) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structcoredump__mem__region__node.md#a41fb46fe6748ee9d4a2a4b8cd2230000);

40

[ 42](structcoredump__mem__region__node.md#a997c7ba19516bdb6f9a97ee55f488454) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [start](structcoredump__mem__region__node.md#a997c7ba19516bdb6f9a97ee55f488454);

43

[ 45](structcoredump__mem__region__node.md#a85ebc1035439aff3a6a534ddd091c26e) size\_t [size](structcoredump__mem__region__node.md#a85ebc1035439aff3a6a534ddd091c26e);

46};

47

[ 55](group__coredump__device__interface.md#ga47ab4c7475a938c294d65dd7bd0197eb)typedef void (\*[coredump\_dump\_callback\_t](group__coredump__device__interface.md#ga47ab4c7475a938c294d65dd7bd0197eb))([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) dump\_area, size\_t dump\_area\_size);

56

62

63/\*

64 \* Type definition of coredump API function for adding specified

65 \* data into coredump

66 \*/

67typedef void (\*coredump\_device\_dump\_t)(const struct [device](structdevice.md) \*dev);

68

69/\*

70 \* Type definition of coredump API function for registering a memory

71 \* region

72 \*/

73typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*coredump\_device\_register\_memory\_t)(const struct [device](structdevice.md) \*dev,

74 struct [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) \*region);

75

76/\*

77 \* Type definition of coredump API function for unregistering a memory

78 \* region

79 \*/

80typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*coredump\_device\_unregister\_memory\_t)(const struct [device](structdevice.md) \*dev,

81 struct [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) \*region);

82

83/\*

84 \* Type definition of coredump API function for registering a dump

85 \* callback

86 \*/

87typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*coredump\_device\_register\_callback\_t)(const struct [device](structdevice.md) \*dev,

88 [coredump\_dump\_callback\_t](group__coredump__device__interface.md#ga47ab4c7475a938c294d65dd7bd0197eb) callback);

89

90/\*

91 \* API which a coredump pseudo-device driver should expose

92 \*/

93\_\_subsystem struct coredump\_driver\_api {

94 coredump\_device\_dump\_t dump;

95 coredump\_device\_register\_memory\_t register\_memory;

96 coredump\_device\_unregister\_memory\_t unregister\_memory;

97 coredump\_device\_register\_callback\_t register\_callback;

98};

99

103

[ 114](group__coredump__device__interface.md#ga14ccecab2b077a32a0bc3bf4ec5df909)static inline bool [coredump\_device\_register\_memory](group__coredump__device__interface.md#ga14ccecab2b077a32a0bc3bf4ec5df909)(const struct [device](structdevice.md) \*dev,

115 struct [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) \*region)

116{

117 const struct coredump\_driver\_api \*api =

118 (const struct coredump\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

119

120 return api->register\_memory(dev, region);

121}

122

[ 133](group__coredump__device__interface.md#gafd4e43696175eeb3ad1a2894df945530)static inline bool [coredump\_device\_unregister\_memory](group__coredump__device__interface.md#gafd4e43696175eeb3ad1a2894df945530)(const struct [device](structdevice.md) \*dev,

134 struct [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) \*region)

135{

136 const struct coredump\_driver\_api \*api =

137 (const struct coredump\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

138

139 return api->unregister\_memory(dev, region);

140}

141

[ 151](group__coredump__device__interface.md#ga9a59905e1440bdc78aa115645d85d363)static inline bool [coredump\_device\_register\_callback](group__coredump__device__interface.md#ga9a59905e1440bdc78aa115645d85d363)(const struct [device](structdevice.md) \*dev,

152 [coredump\_dump\_callback\_t](group__coredump__device__interface.md#ga47ab4c7475a938c294d65dd7bd0197eb) callback)

153{

154 const struct coredump\_driver\_api \*api =

155 (const struct coredump\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

156

157 return api->register\_callback(dev, callback);

158}

159

163

164#ifdef \_\_cplusplus

165}

166#endif

167

168#endif /\* INCLUDE\_ZEPHYR\_DRIVERS\_COREDUMP\_H\_ \*/

[device.h](device_8h.md)

[coredump\_device\_register\_memory](group__coredump__device__interface.md#ga14ccecab2b077a32a0bc3bf4ec5df909)

static bool coredump\_device\_register\_memory(const struct device \*dev, struct coredump\_mem\_region\_node \*region)

Register a region of memory to be stored in core dump at the time it is generated.

**Definition** coredump.h:114

[coredump\_dump\_callback\_t](group__coredump__device__interface.md#ga47ab4c7475a938c294d65dd7bd0197eb)

void(\* coredump\_dump\_callback\_t)(uintptr\_t dump\_area, size\_t dump\_area\_size)

Callback that occurs at dump time, data copied into dump\_area will be included in the dump that is ge...

**Definition** coredump.h:55

[coredump\_device\_register\_callback](group__coredump__device__interface.md#ga9a59905e1440bdc78aa115645d85d363)

static bool coredump\_device\_register\_callback(const struct device \*dev, coredump\_dump\_callback\_t callback)

Register a callback to be invoked at dump time.

**Definition** coredump.h:151

[coredump\_device\_unregister\_memory](group__coredump__device__interface.md#gafd4e43696175eeb3ad1a2894df945530)

static bool coredump\_device\_unregister\_memory(const struct device \*dev, struct coredump\_mem\_region\_node \*region)

Unregister a region of memory to be stored in core dump at the time it is generated.

**Definition** coredump.h:133

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[slist.h](slist_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[coredump\_mem\_region\_node](structcoredump__mem__region__node.md)

Structure describing a region in memory that may be stored in core dump at the time it is generated.

**Definition** coredump.h:37

[coredump\_mem\_region\_node::node](structcoredump__mem__region__node.md#a41fb46fe6748ee9d4a2a4b8cd2230000)

sys\_snode\_t node

Node of single-linked list, do not modify.

**Definition** coredump.h:39

[coredump\_mem\_region\_node::size](structcoredump__mem__region__node.md#a85ebc1035439aff3a6a534ddd091c26e)

size\_t size

Size of memory region.

**Definition** coredump.h:45

[coredump\_mem\_region\_node::start](structcoredump__mem__region__node.md#a997c7ba19516bdb6f9a97ee55f488454)

uintptr\_t start

Address of start of memory region.

**Definition** coredump.h:42

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [coredump.h](drivers_2coredump_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
