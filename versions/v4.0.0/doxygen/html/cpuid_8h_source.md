---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cpuid_8h_source.html
original_path: doxygen/html/cpuid_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpuid.h

[Go to the documentation of this file.](cpuid_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corp.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_CPUID\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_X86\_CPUID\_H\_

8

9#ifndef \_ASMLANGUAGE

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

[ 14](cpuid_8h.md#a63a5857996ced41057dec195c2d18461)#define CPUID\_BASIC\_INFO\_1 0x01

[ 15](cpuid_8h.md#aac8c403e59b4b990005ca3d37b056ded)#define CPUID\_EXTENDED\_FEATURES\_LVL 0x07

[ 16](cpuid_8h.md#aa3535d8f0adf8c0d0b28e96cb5c89e49)#define CPUID\_EXTENDED\_TOPOLOGY\_ENUMERATION 0x0B

[ 17](cpuid_8h.md#ac53ef814aebfd98874b03a2ae5ca3a14)#define CPUID\_EXTENDED\_TOPOLOGY\_ENUMERATION\_V2 0x1F

18

19/\* Bits to check in CPUID extended features \*/

[ 20](cpuid_8h.md#a5f26a3dceccfc89473b8ae8c52c8a2c5)#define CPUID\_SPEC\_CTRL\_SSBD BIT(31)

[ 21](cpuid_8h.md#a0e7c0e86743ad10b5cb1603b012ec76d)#define CPUID\_SPEC\_CTRL\_IBRS BIT(26)

22

23[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_x86\_cpuid\_extended\_features(void);

24

25[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) z\_x86\_cpuid\_get\_current\_physical\_apic\_id(void);

26

27#ifdef \_\_cplusplus

28}

29#endif

30#endif /\* \_ASMLANGUAGE \*/

31

32#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_CPUID\_H\_ \*/

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [cpuid.h](cpuid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
