---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/public_2memory_8h_source.html
original_path: doxygen/html/public_2memory_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory.h

[Go to the documentation of this file.](public_2memory_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2

3/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

4 \* memory.h

5 \*

6 \* Memory reservation and information.

7 \*

8 \* Permission is hereby granted, free of charge, to any person obtaining a copy

9 \* of this software and associated documentation files (the "Software"), to

10 \* deal in the Software without restriction, including without limitation the

11 \* rights to use, copy, modify, merge, publish, distribute, sublicense, and/or

12 \* sell copies of the Software, and to permit persons to whom the Software is

13 \* furnished to do so, subject to the following conditions:

14 \*

15 \* The above copyright notice and this permission notice shall be included in

16 \* all copies or substantial portions of the Software.

17 \*

18 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

19 \* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

20 \* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

21 \* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

22 \* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING

23 \* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER

24 \* DEALINGS IN THE SOFTWARE.

25 \*

26 \* Copyright (c) 2005, Keir Fraser <keir@xensource.com>

27 \*/

28

29#ifndef \_\_XEN\_PUBLIC\_MEMORY\_H\_\_

30#define \_\_XEN\_PUBLIC\_MEMORY\_H\_\_

31

32#include "[xen.h](xen_8h.md)"

33

[ 34](public_2memory_8h.md#a6ec885dfced1bae6da54202b3d63ecaf)#define XENMEM\_populate\_physmap 6

35

[ 36](structxen__memory__reservation.md)struct [xen\_memory\_reservation](structxen__memory__reservation.md) {

37

38 /\*

39 \* XENMEM\_increase\_reservation:

40 \* OUT: MFN (\*not\* GMFN) bases of extents that were allocated

41 \* XENMEM\_decrease\_reservation:

42 \* IN: GMFN bases of extents to free

43 \* XENMEM\_populate\_physmap:

44 \* IN: GPFN bases of extents to populate with memory

45 \* OUT: GMFN bases of extents that were allocated

46 \* (NB. This command also updates the mach\_to\_phys translation table)

47 \* XENMEM\_claim\_pages:

48 \* IN: must be zero

49 \*/

[ 50](structxen__memory__reservation.md#a94ed3926aa2d7f7c759fe9cbd59b042a) [XEN\_GUEST\_HANDLE](structxen__memory__reservation.md#a94ed3926aa2d7f7c759fe9cbd59b042a)([xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226)) extent\_start;

51

52 /\* Number of extents, and size/alignment of each (2^extent\_order pages). \*/

[ 53](structxen__memory__reservation.md#a0ab0fec872492d02f73d5dde37ef93bb) [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) [nr\_extents](structxen__memory__reservation.md#a0ab0fec872492d02f73d5dde37ef93bb);

[ 54](structxen__memory__reservation.md#ad0acf08be6cf896b508744cc6398b6b6) unsigned int [extent\_order](structxen__memory__reservation.md#ad0acf08be6cf896b508744cc6398b6b6);

55

56#if \_\_XEN\_INTERFACE\_VERSION\_\_ >= 0x00030209

57 /\* XENMEMF flags. \*/

58 unsigned int mem\_flags;

59#else

[ 60](structxen__memory__reservation.md#a18732ad7ad5cde2ab44cef84af689ee2) unsigned int [address\_bits](structxen__memory__reservation.md#a18732ad7ad5cde2ab44cef84af689ee2);

61#endif

62

63 /\*

64 \* Domain whose reservation is being changed.

65 \* Unprivileged domains can specify only DOMID\_SELF.

66 \*/

[ 67](structxen__memory__reservation.md#a20ea11d84f179b236346ec129e94f6d0) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [domid](structxen__memory__reservation.md#a20ea11d84f179b236346ec129e94f6d0);

68};

[ 69](public_2memory_8h.md#a2328386982b62de8d81d891e257cab9b)typedef struct [xen\_memory\_reservation](structxen__memory__reservation.md) [xen\_memory\_reservation\_t](public_2memory_8h.md#a2328386982b62de8d81d891e257cab9b);

[ 70](public_2memory_8h.md#acc691af99a28d99e4f6101403dfda8fc)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([xen\_memory\_reservation\_t](public_2memory_8h.md#a2328386982b62de8d81d891e257cab9b));

71

72/\* A batched version of add\_to\_physmap. \*/

[ 73](public_2memory_8h.md#a7d95089177a14df927c60432925acbfa)#define XENMEM\_add\_to\_physmap\_batch 23

[ 74](structxen__add__to__physmap__batch.md)struct [xen\_add\_to\_physmap\_batch](structxen__add__to__physmap__batch.md) {

75 /\* IN \*/

76 /\* Which domain to change the mapping for. \*/

[ 77](structxen__add__to__physmap__batch.md#a9e7325563f39256e35fbada075bc1e4c) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [domid](structxen__add__to__physmap__batch.md#a9e7325563f39256e35fbada075bc1e4c);

[ 78](structxen__add__to__physmap__batch.md#a2d0bd5efa6e425e4c583c1fb8e028fe5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [space](structxen__add__to__physmap__batch.md#a2d0bd5efa6e425e4c583c1fb8e028fe5); /\* => enum phys\_map\_space \*/

79

80 /\* Number of pages to go through \*/

[ 81](structxen__add__to__physmap__batch.md#a47f58749bd833fc81f4ac7e714530a4b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [size](structxen__add__to__physmap__batch.md#a47f58749bd833fc81f4ac7e714530a4b);

82

83#if \_\_XEN\_INTERFACE\_VERSION\_\_ < 0x00040700

[ 84](structxen__add__to__physmap__batch.md#aeba66d4e050258147caf95828c3fa1d4) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [foreign\_domid](structxen__add__to__physmap__batch.md#aeba66d4e050258147caf95828c3fa1d4); /\* IFF gmfn\_foreign. Should be 0 for other spaces. \*/

85#else

86 union xen\_add\_to\_physmap\_batch\_extra {

87 [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [foreign\_domid](structxen__add__to__physmap__batch.md#aeba66d4e050258147caf95828c3fa1d4); /\* gmfn\_foreign \*/

88 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res0; /\* All the other spaces. Should be 0 \*/

89 } u;

90#endif

91

92 /\* Indexes into space being mapped. \*/

[ 93](structxen__add__to__physmap__batch.md#ae21559560d005afcadcb4e63306ea5ed) [XEN\_GUEST\_HANDLE](structxen__add__to__physmap__batch.md#ae21559560d005afcadcb4e63306ea5ed)([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)) idxs;

94

95 /\* GPFN in domid where the source mapping page should appear. \*/

[ 96](structxen__add__to__physmap__batch.md#acd92848c32fd218aa28a8544db8bf780) [XEN\_GUEST\_HANDLE](structxen__add__to__physmap__batch.md#acd92848c32fd218aa28a8544db8bf780)([xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226)) gpfns;

97

98 /\* OUT \*/

99 /\* Per index error code. \*/

[ 100](structxen__add__to__physmap__batch.md#ac3dcc0adb6f94a4c040658f3366bf098) [XEN\_GUEST\_HANDLE](structxen__add__to__physmap__batch.md#ac3dcc0adb6f94a4c040658f3366bf098)(int) errs;

101};

[ 102](public_2memory_8h.md#a7d0453db07f6593afa9ea5657ddf8815)typedef struct [xen\_add\_to\_physmap\_batch](structxen__add__to__physmap__batch.md) [xen\_add\_to\_physmap\_batch\_t](public_2memory_8h.md#a7d0453db07f6593afa9ea5657ddf8815);

[ 103](public_2memory_8h.md#a527825096ff8c47a16a6e911cc7c6cd4)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([xen\_add\_to\_physmap\_batch\_t](public_2memory_8h.md#a7d0453db07f6593afa9ea5657ddf8815));

104

105

[ 106](public_2memory_8h.md#a4369cb99e8d27ca45dc163373d103309)#define XENMAPSPACE\_shared\_info 0 /\* shared info page \*/

[ 107](public_2memory_8h.md#ad115b9759532e6d0358cc704409c6270)#define XENMAPSPACE\_grant\_table 1 /\* grant table page \*/

[ 108](public_2memory_8h.md#a5675ec2efeed7e5c40dda7483b10d569)#define XENMAPSPACE\_gmfn 2 /\* GMFN \*/

109

110/\* GMFN range, XENMEM\_add\_to\_physmap only.\*/

[ 111](public_2memory_8h.md#a2c34663ef8ef5bd369e2d73520649e50)#define XENMAPSPACE\_gmfn\_range 3

112

113/\* GMFN from another dom, XENMEM\_add\_to\_physmap\_batch only. \*/

[ 114](public_2memory_8h.md#a565fab9b43c0a1be2866b9aa934841ba)#define XENMAPSPACE\_gmfn\_foreign 4

115

116/\*

117 \* Device mmio region ARM only; the region is mapped in Stage-2 using the

118 \* Normal Memory Inner/Outer Write-Back Cacheable memory attribute.

119 \*/

[ 120](public_2memory_8h.md#acb4d47c69fee4afe3c722cb6ee8d61b6)#define XENMAPSPACE\_dev\_mmio 5

121

122/\*

123 \* Sets the GPFN at which a particular page appears in the specified guest's

124 \* physical address space (translated guests only).

125 \* arg == addr of xen\_add\_to\_physmap\_t.

126 \*/

[ 127](public_2memory_8h.md#a1475409f6e69603d9797b94efc148b4d)#define XENMEM\_add\_to\_physmap 7

[ 128](structxen__add__to__physmap.md)struct [xen\_add\_to\_physmap](structxen__add__to__physmap.md) {

129 /\* Which domain to change the mapping for. \*/

[ 130](structxen__add__to__physmap.md#aefcfb9f5ab697d058a5304b7bb3ba978) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [domid](structxen__add__to__physmap.md#aefcfb9f5ab697d058a5304b7bb3ba978);

131

132 /\* Number of pages to go through for gmfn\_range \*/

[ 133](structxen__add__to__physmap.md#a4582b6f9d96315c89cc813fb58e4b2c7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [size](structxen__add__to__physmap.md#a4582b6f9d96315c89cc813fb58e4b2c7);

134

[ 135](structxen__add__to__physmap.md#ab1fbe037fedba84791aa56a18084e125) unsigned int [space](structxen__add__to__physmap.md#ab1fbe037fedba84791aa56a18084e125); /\* => enum phys\_map\_space \*/

136

[ 137](public_2memory_8h.md#a203b04fe93d4686b1c12337bc3973747)#define XENMAPIDX\_grant\_table\_status 0x80000000

138

139 /\* Index into space being mapped. \*/

[ 140](structxen__add__to__physmap.md#a57e7c955f8e67ded78781d0088da6a12) [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) [idx](structxen__add__to__physmap.md#a57e7c955f8e67ded78781d0088da6a12);

141

142 /\* GPFN in domid where the source mapping page should appear. \*/

[ 143](structxen__add__to__physmap.md#abae5d800038c5a4518f5ef7e6ee92c9d) [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) [gpfn](structxen__add__to__physmap.md#abae5d800038c5a4518f5ef7e6ee92c9d);

144};

[ 145](public_2memory_8h.md#afe3890ecc3ae521c121d3bcdf1e4b39b)typedef struct [xen\_add\_to\_physmap](structxen__add__to__physmap.md) [xen\_add\_to\_physmap\_t](public_2memory_8h.md#afe3890ecc3ae521c121d3bcdf1e4b39b);

[ 146](public_2memory_8h.md#a2fcb0b67b88e3de8a1dd66d5eeaa7df5)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([xen\_add\_to\_physmap\_t](public_2memory_8h.md#afe3890ecc3ae521c121d3bcdf1e4b39b));

147

148/\*

149 \* Unmaps the page appearing at a particular GPFN from the specified guest's

150 \* physical address space (translated guests only).

151 \* arg == addr of xen\_remove\_from\_physmap\_t.

152 \*/

[ 153](public_2memory_8h.md#a684c3081ab104b422ea40c68fc421c1c)#define XENMEM\_remove\_from\_physmap 15

[ 154](structxen__remove__from__physmap.md)struct [xen\_remove\_from\_physmap](structxen__remove__from__physmap.md) {

155 /\* Which domain to change the mapping for. \*/

[ 156](structxen__remove__from__physmap.md#a87f4fff5f1740aaabc4839b13755027f) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [domid](structxen__remove__from__physmap.md#a87f4fff5f1740aaabc4839b13755027f);

157

158 /\* GPFN of the current mapping of the page. \*/

[ 159](structxen__remove__from__physmap.md#a1bca82887e69eac74edc3c8afa81634a) [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) [gpfn](structxen__remove__from__physmap.md#a1bca82887e69eac74edc3c8afa81634a);

160};

[ 161](public_2memory_8h.md#a7ac5899f2de1e9d6d775142c9ee4616b)typedef struct [xen\_remove\_from\_physmap](structxen__remove__from__physmap.md) [xen\_remove\_from\_physmap\_t](public_2memory_8h.md#a7ac5899f2de1e9d6d775142c9ee4616b);

[ 162](public_2memory_8h.md#a96fd5cc1e36746fa9ad613912d519f4b)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([xen\_remove\_from\_physmap\_t](public_2memory_8h.md#a7ac5899f2de1e9d6d775142c9ee4616b));

163

164#endif /\* \_\_XEN\_PUBLIC\_MEMORY\_H\_\_ \*/

[xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226)

uint64\_t xen\_pfn\_t

**Definition** arch-arm.h:204

[xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)

uint64\_t xen\_ulong\_t

**Definition** arch-arm.h:214

[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)

#define DEFINE\_XEN\_GUEST\_HANDLE(name)

**Definition** arch-arm.h:192

[xen\_memory\_reservation\_t](public_2memory_8h.md#a2328386982b62de8d81d891e257cab9b)

struct xen\_memory\_reservation xen\_memory\_reservation\_t

**Definition** memory.h:69

[xen\_remove\_from\_physmap\_t](public_2memory_8h.md#a7ac5899f2de1e9d6d775142c9ee4616b)

struct xen\_remove\_from\_physmap xen\_remove\_from\_physmap\_t

**Definition** memory.h:161

[xen\_add\_to\_physmap\_batch\_t](public_2memory_8h.md#a7d0453db07f6593afa9ea5657ddf8815)

struct xen\_add\_to\_physmap\_batch xen\_add\_to\_physmap\_batch\_t

**Definition** memory.h:102

[xen\_add\_to\_physmap\_t](public_2memory_8h.md#afe3890ecc3ae521c121d3bcdf1e4b39b)

struct xen\_add\_to\_physmap xen\_add\_to\_physmap\_t

**Definition** memory.h:145

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[xen\_add\_to\_physmap\_batch](structxen__add__to__physmap__batch.md)

**Definition** memory.h:74

[xen\_add\_to\_physmap\_batch::space](structxen__add__to__physmap__batch.md#a2d0bd5efa6e425e4c583c1fb8e028fe5)

uint16\_t space

**Definition** memory.h:78

[xen\_add\_to\_physmap\_batch::size](structxen__add__to__physmap__batch.md#a47f58749bd833fc81f4ac7e714530a4b)

uint16\_t size

**Definition** memory.h:81

[xen\_add\_to\_physmap\_batch::domid](structxen__add__to__physmap__batch.md#a9e7325563f39256e35fbada075bc1e4c)

domid\_t domid

**Definition** memory.h:77

[xen\_add\_to\_physmap\_batch::XEN\_GUEST\_HANDLE](structxen__add__to__physmap__batch.md#ac3dcc0adb6f94a4c040658f3366bf098)

XEN\_GUEST\_HANDLE(int) errs

[xen\_add\_to\_physmap\_batch::XEN\_GUEST\_HANDLE](structxen__add__to__physmap__batch.md#acd92848c32fd218aa28a8544db8bf780)

XEN\_GUEST\_HANDLE(xen\_pfn\_t) gpfns

[xen\_add\_to\_physmap\_batch::XEN\_GUEST\_HANDLE](structxen__add__to__physmap__batch.md#ae21559560d005afcadcb4e63306ea5ed)

XEN\_GUEST\_HANDLE(xen\_ulong\_t) idxs

[xen\_add\_to\_physmap\_batch::foreign\_domid](structxen__add__to__physmap__batch.md#aeba66d4e050258147caf95828c3fa1d4)

domid\_t foreign\_domid

**Definition** memory.h:84

[xen\_add\_to\_physmap](structxen__add__to__physmap.md)

**Definition** memory.h:128

[xen\_add\_to\_physmap::size](structxen__add__to__physmap.md#a4582b6f9d96315c89cc813fb58e4b2c7)

uint16\_t size

**Definition** memory.h:133

[xen\_add\_to\_physmap::idx](structxen__add__to__physmap.md#a57e7c955f8e67ded78781d0088da6a12)

xen\_ulong\_t idx

**Definition** memory.h:140

[xen\_add\_to\_physmap::space](structxen__add__to__physmap.md#ab1fbe037fedba84791aa56a18084e125)

unsigned int space

**Definition** memory.h:135

[xen\_add\_to\_physmap::gpfn](structxen__add__to__physmap.md#abae5d800038c5a4518f5ef7e6ee92c9d)

xen\_pfn\_t gpfn

**Definition** memory.h:143

[xen\_add\_to\_physmap::domid](structxen__add__to__physmap.md#aefcfb9f5ab697d058a5304b7bb3ba978)

domid\_t domid

**Definition** memory.h:130

[xen\_memory\_reservation](structxen__memory__reservation.md)

**Definition** memory.h:36

[xen\_memory\_reservation::nr\_extents](structxen__memory__reservation.md#a0ab0fec872492d02f73d5dde37ef93bb)

xen\_ulong\_t nr\_extents

**Definition** memory.h:53

[xen\_memory\_reservation::address\_bits](structxen__memory__reservation.md#a18732ad7ad5cde2ab44cef84af689ee2)

unsigned int address\_bits

**Definition** memory.h:60

[xen\_memory\_reservation::domid](structxen__memory__reservation.md#a20ea11d84f179b236346ec129e94f6d0)

domid\_t domid

**Definition** memory.h:67

[xen\_memory\_reservation::XEN\_GUEST\_HANDLE](structxen__memory__reservation.md#a94ed3926aa2d7f7c759fe9cbd59b042a)

XEN\_GUEST\_HANDLE(xen\_pfn\_t) extent\_start

[xen\_memory\_reservation::extent\_order](structxen__memory__reservation.md#ad0acf08be6cf896b508744cc6398b6b6)

unsigned int extent\_order

**Definition** memory.h:54

[xen\_remove\_from\_physmap](structxen__remove__from__physmap.md)

**Definition** memory.h:154

[xen\_remove\_from\_physmap::gpfn](structxen__remove__from__physmap.md#a1bca82887e69eac74edc3c8afa81634a)

xen\_pfn\_t gpfn

**Definition** memory.h:159

[xen\_remove\_from\_physmap::domid](structxen__remove__from__physmap.md#a87f4fff5f1740aaabc4839b13755027f)

domid\_t domid

**Definition** memory.h:156

[xen.h](xen_8h.md)

[domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee)

uint16\_t domid\_t

**Definition** xen.h:217

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [memory.h](public_2memory_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
