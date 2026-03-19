---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/udc__buf_8h_source.html
original_path: doxygen/html/udc__buf_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udc\_buf.h

[Go to the documentation of this file.](udc__buf_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_UDC\_BUF\_H

13#define ZEPHYR\_INCLUDE\_UDC\_BUF\_H

14

15#include <[zephyr/kernel.h](kernel_8h.md)>

16#include <[zephyr/net\_buf.h](net__buf_8h.md)>

17

18#if defined(CONFIG\_DCACHE) && !defined(CONFIG\_UDC\_BUF\_FORCE\_NOCACHE)

19/\*

20 \* Here we try to get DMA-safe buffers, but we lack a consistent source of

21 \* information about data cache properties, such as line cache size, and a

22 \* consistent source of information about what part of memory is DMA'able.

23 \* For now, we simply assume that all available memory is DMA'able and use

24 \* Kconfig option DCACHE\_LINE\_SIZE for alignment and granularity.

25 \*/

26#define Z\_UDC\_BUF\_ALIGN CONFIG\_DCACHE\_LINE\_SIZE

27#define Z\_UDC\_BUF\_GRANULARITY CONFIG\_DCACHE\_LINE\_SIZE

28#else

29/\*

30 \* Default alignment and granularity to pointer size if the platform does not

31 \* have a data cache or buffers are placed in nocache memory region.

32 \*/

33#define Z\_UDC\_BUF\_ALIGN sizeof(void \*)

34#define Z\_UDC\_BUF\_GRANULARITY sizeof(void \*)

35#endif

36

37

38#if defined(CONFIG\_UDC\_BUF\_FORCE\_NOCACHE)

39/\*

40 \* The usb transfer buffer needs to be in \_\_nocache section

41 \*/

42#define Z\_UDC\_BUF\_SECTION \_\_nocache

43#else

44#define Z\_UDC\_BUF\_SECTION

45#endif

46

55

[ 57](group__udc__buf.md#gaf53404357b1184c1eda430e92cd696dc)#define UDC\_BUF\_ALIGN Z\_UDC\_BUF\_ALIGN

58

[ 60](group__udc__buf.md#ga87ea6bf98e8be1ca3378928fbf03bf8e)#define UDC\_BUF\_GRANULARITY Z\_UDC\_BUF\_GRANULARITY

61

[ 71](group__udc__buf.md#gae5cb6affd574da5f4cd0c25e9178a0eb)#define UDC\_STATIC\_BUF\_DEFINE(name, size) \

72 static uint8\_t Z\_UDC\_BUF\_SECTION \_\_aligned(UDC\_BUF\_ALIGN) \

73 name[ROUND\_UP(size, UDC\_BUF\_GRANULARITY)];

74

[ 82](group__udc__buf.md#ga4e77ceb9142c9d414966f0c4e0eb7710)#define IS\_UDC\_ALIGNED(buf) IS\_ALIGNED(buf, UDC\_BUF\_ALIGN)

83

87#define UDC\_HEAP\_DEFINE(name, bytes, in\_section) \

88 uint8\_t in\_section \_\_aligned(UDC\_BUF\_ALIGN) \

89 kheap\_##name[MAX(bytes, Z\_HEAP\_MIN\_SIZE)]; \

90 STRUCT\_SECTION\_ITERABLE(k\_heap, name) = { \

91 .heap = { \

92 .init\_mem = kheap\_##name, \

93 .init\_bytes = MAX(bytes, Z\_HEAP\_MIN\_SIZE), \

94 }, \

95 }

96

97#define UDC\_K\_HEAP\_DEFINE(name, size) \

98 COND\_CODE\_1(CONFIG\_UDC\_BUF\_FORCE\_NOCACHE, \

99 (UDC\_HEAP\_DEFINE(name, size, \_\_nocache)), \

100 (UDC\_HEAP\_DEFINE(name, size, \_\_noinit)))

101

102extern const struct net\_buf\_data\_cb net\_buf\_dma\_cb;

104

[ 119](group__udc__buf.md#ga064d3f73dbde0f98479ffdad5141e8c0)#define UDC\_BUF\_POOL\_VAR\_DEFINE(pname, count, size, ud\_size, fdestroy) \

120 \_NET\_BUF\_ARRAY\_DEFINE(pname, count, ud\_size); \

121 UDC\_K\_HEAP\_DEFINE(net\_buf\_mem\_pool\_##pname, size); \

122 static const struct net\_buf\_data\_alloc net\_buf\_data\_alloc\_##pname = { \

123 .cb = &net\_buf\_dma\_cb, \

124 .alloc\_data = &net\_buf\_mem\_pool\_##pname, \

125 .max\_alloc\_size = 0, \

126 }; \

127 static STRUCT\_SECTION\_ITERABLE(net\_buf\_pool, pname) = \

128 NET\_BUF\_POOL\_INITIALIZER(pname, &net\_buf\_data\_alloc\_##pname, \

129 \_net\_buf\_##pname, count, ud\_size, \

130 fdestroy)

131

[ 146](group__udc__buf.md#gac96f1518df5748927c3377cb3abc222d)#define UDC\_BUF\_POOL\_DEFINE(pname, count, size, ud\_size, fdestroy) \

147 \_NET\_BUF\_ARRAY\_DEFINE(pname, count, ud\_size); \

148 BUILD\_ASSERT((UDC\_BUF\_GRANULARITY) % (UDC\_BUF\_ALIGN) == 0, \

149 "Code assumes granurality is multiple of alignment"); \

150 static uint8\_t Z\_UDC\_BUF\_SECTION \_\_aligned(UDC\_BUF\_ALIGN) \

151 net\_buf\_data\_##pname[count][ROUND\_UP(size, UDC\_BUF\_GRANULARITY)];\

152 static const struct net\_buf\_pool\_fixed net\_buf\_fixed\_##pname = { \

153 .data\_pool = (uint8\_t \*)net\_buf\_data\_##pname, \

154 }; \

155 static const struct net\_buf\_data\_alloc net\_buf\_fixed\_alloc\_##pname = { \

156 .cb = &net\_buf\_fixed\_cb, \

157 .alloc\_data = (void \*)&net\_buf\_fixed\_##pname, \

158 .max\_alloc\_size = ROUND\_UP(size, UDC\_BUF\_GRANULARITY), \

159 }; \

160 static STRUCT\_SECTION\_ITERABLE(net\_buf\_pool, pname) = \

161 NET\_BUF\_POOL\_INITIALIZER(pname, &net\_buf\_fixed\_alloc\_##pname, \

162 \_net\_buf\_##pname, count, ud\_size, \

163 fdestroy)

164

168

169#endif /\* ZEPHYR\_INCLUDE\_UDC\_BUF\_H \*/

[kernel.h](kernel_8h.md)

Public kernel APIs.

[net\_buf.h](net__buf_8h.md)

Buffer management.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [udc\_buf.h](udc__buf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
