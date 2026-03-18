---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/shared__multi__heap_8h_source.html
original_path: doxygen/html/shared__multi__heap_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shared\_multi\_heap.h

[Go to the documentation of this file.](shared__multi__heap_8h.md)

1/\*

2 \* Copyright (c) 2021 Carlo Caione, <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_MULTI\_HEAP\_MANAGER\_SMH\_H\_

13#define ZEPHYR\_INCLUDE\_MULTI\_HEAP\_MANAGER\_SMH\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

26

62

[ 69](group__shared__multi__heap.md#ga11861c5c373f9e5d81496ae1be7df1d4)enum [shared\_multi\_heap\_attr](group__shared__multi__heap.md#ga11861c5c373f9e5d81496ae1be7df1d4) {

[ 71](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4afb2e0bb04859ff231dee953279b8bf3a) [SMH\_REG\_ATTR\_CACHEABLE](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4afb2e0bb04859ff231dee953279b8bf3a),

72

[ 74](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4a2625b9b8aea429ab748f9e39d55f0dff) [SMH\_REG\_ATTR\_NON\_CACHEABLE](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4a2625b9b8aea429ab748f9e39d55f0dff),

75

[ 77](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4a0a41317e94fcdf459708be4a78b74c91) [SMH\_REG\_ATTR\_NUM](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4a0a41317e94fcdf459708be4a78b74c91),

78};

79

[ 81](group__shared__multi__heap.md#gae582ce2dfaaf9554d43aab717c85c17c)#define MAX\_SHARED\_MULTI\_HEAP\_ATTR SMH\_REG\_ATTR\_NUM

82

[ 89](structshared__multi__heap__region.md)struct [shared\_multi\_heap\_region](structshared__multi__heap__region.md) {

[ 91](structshared__multi__heap__region.md#a5fcdce28a57be4b652a9a53a70ae796f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attr](structshared__multi__heap__region.md#a5fcdce28a57be4b652a9a53a70ae796f);

92

[ 94](structshared__multi__heap__region.md#a905df61648eaa18cebf53bb10dcde91d) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [addr](structshared__multi__heap__region.md#a905df61648eaa18cebf53bb10dcde91d);

95

[ 97](structshared__multi__heap__region.md#a3f6565062f70b2c8d25c3a0be579482c) size\_t [size](structshared__multi__heap__region.md#a3f6565062f70b2c8d25c3a0be579482c);

98};

99

[ 114](group__shared__multi__heap.md#ga5b7f09666e3eac051b4c4942572f9ca3)int [shared\_multi\_heap\_pool\_init](group__shared__multi__heap.md#ga5b7f09666e3eac051b4c4942572f9ca3)(void);

115

[ 129](group__shared__multi__heap.md#ga8cd3d321f5ae516cd55812d304289971)void \*[shared\_multi\_heap\_alloc](group__shared__multi__heap.md#ga8cd3d321f5ae516cd55812d304289971)(enum [shared\_multi\_heap\_attr](group__shared__multi__heap.md#ga11861c5c373f9e5d81496ae1be7df1d4) attr, size\_t bytes);

130

[ 145](group__shared__multi__heap.md#ga328b199253da06ed724e9b0157167ede)void \*[shared\_multi\_heap\_aligned\_alloc](group__shared__multi__heap.md#ga328b199253da06ed724e9b0157167ede)(enum [shared\_multi\_heap\_attr](group__shared__multi__heap.md#ga11861c5c373f9e5d81496ae1be7df1d4) attr,

146 size\_t align, size\_t bytes);

147

[ 159](group__shared__multi__heap.md#gab968bf26483d22939aaa7c2b1b6743ad)void [shared\_multi\_heap\_free](group__shared__multi__heap.md#gab968bf26483d22939aaa7c2b1b6743ad)(void \*block);

160

[ 174](group__shared__multi__heap.md#ga086362a2a8fce827a246039ef8757cc5)int [shared\_multi\_heap\_add](group__shared__multi__heap.md#ga086362a2a8fce827a246039ef8757cc5)(struct [shared\_multi\_heap\_region](structshared__multi__heap__region.md) \*region, void \*user\_data);

175

179

180#ifdef \_\_cplusplus

181}

182#endif

183

184#endif /\* ZEPHYR\_INCLUDE\_MULTI\_HEAP\_MANAGER\_SMH\_H\_ \*/

[shared\_multi\_heap\_add](group__shared__multi__heap.md#ga086362a2a8fce827a246039ef8757cc5)

int shared\_multi\_heap\_add(struct shared\_multi\_heap\_region \*region, void \*user\_data)

Add an heap region to the shared multi-heap pool.

[shared\_multi\_heap\_attr](group__shared__multi__heap.md#ga11861c5c373f9e5d81496ae1be7df1d4)

shared\_multi\_heap\_attr

SMH region attributes enumeration type.

**Definition** shared\_multi\_heap.h:69

[shared\_multi\_heap\_aligned\_alloc](group__shared__multi__heap.md#ga328b199253da06ed724e9b0157167ede)

void \* shared\_multi\_heap\_aligned\_alloc(enum shared\_multi\_heap\_attr attr, size\_t align, size\_t bytes)

Allocate aligned memory from the memory shared multi-heap pool.

[shared\_multi\_heap\_pool\_init](group__shared__multi__heap.md#ga5b7f09666e3eac051b4c4942572f9ca3)

int shared\_multi\_heap\_pool\_init(void)

Init the pool.

[shared\_multi\_heap\_alloc](group__shared__multi__heap.md#ga8cd3d321f5ae516cd55812d304289971)

void \* shared\_multi\_heap\_alloc(enum shared\_multi\_heap\_attr attr, size\_t bytes)

Allocate memory from the memory shared multi-heap pool.

[shared\_multi\_heap\_free](group__shared__multi__heap.md#gab968bf26483d22939aaa7c2b1b6743ad)

void shared\_multi\_heap\_free(void \*block)

Free memory from the shared multi-heap pool.

[SMH\_REG\_ATTR\_NUM](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4a0a41317e94fcdf459708be4a78b74c91)

@ SMH\_REG\_ATTR\_NUM

must be the last item

**Definition** shared\_multi\_heap.h:77

[SMH\_REG\_ATTR\_NON\_CACHEABLE](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4a2625b9b8aea429ab748f9e39d55f0dff)

@ SMH\_REG\_ATTR\_NON\_CACHEABLE

non-cacheable

**Definition** shared\_multi\_heap.h:74

[SMH\_REG\_ATTR\_CACHEABLE](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4afb2e0bb04859ff231dee953279b8bf3a)

@ SMH\_REG\_ATTR\_CACHEABLE

cacheable

**Definition** shared\_multi\_heap.h:71

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[shared\_multi\_heap\_region](structshared__multi__heap__region.md)

SMH region struct.

**Definition** shared\_multi\_heap.h:89

[shared\_multi\_heap\_region::size](structshared__multi__heap__region.md#a3f6565062f70b2c8d25c3a0be579482c)

size\_t size

Memory heap size in bytes.

**Definition** shared\_multi\_heap.h:97

[shared\_multi\_heap\_region::attr](structshared__multi__heap__region.md#a5fcdce28a57be4b652a9a53a70ae796f)

uint32\_t attr

Memory heap attribute.

**Definition** shared\_multi\_heap.h:91

[shared\_multi\_heap\_region::addr](structshared__multi__heap__region.md#a905df61648eaa18cebf53bb10dcde91d)

uintptr\_t addr

Memory heap starting virtual address.

**Definition** shared\_multi\_heap.h:94

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [multi\_heap](dir_bbf885d0562205ffed4d60b82c4fd442.md)
- [shared\_multi\_heap.h](shared__multi__heap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
