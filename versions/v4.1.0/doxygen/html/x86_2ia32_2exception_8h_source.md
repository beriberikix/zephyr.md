---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/x86_2ia32_2exception_8h_source.html
original_path: doxygen/html/x86_2ia32_2exception_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](x86_2ia32_2exception_8h.md)

1/\*

2 \* Copyright (c) 2010-2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_EXCEPTION\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_EXCEPTION\_H\_

9

10#ifndef \_ASMLANGUAGE

11#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

29

30struct [arch\_esf](structarch__esf.md) {

31#ifdef CONFIG\_GDBSTUB

[ 32](structarch__esf.md#a25aae07c91f6946596f92f0069d6729a) unsigned int [ss](structarch__esf.md#a25aae07c91f6946596f92f0069d6729a);

[ 33](structarch__esf.md#a353cd21036946b829a01ab9e247bf72d) unsigned int [gs](structarch__esf.md#a353cd21036946b829a01ab9e247bf72d);

[ 34](structarch__esf.md#a1f127199573607f22a4c0e95d3b5ce74) unsigned int [fs](structarch__esf.md#a1f127199573607f22a4c0e95d3b5ce74);

[ 35](structarch__esf.md#aac9b040d864214b71afb15e618a300da) unsigned int [es](structarch__esf.md#aac9b040d864214b71afb15e618a300da);

[ 36](structarch__esf.md#adbdb731abf4be35509eec853ecddc601) unsigned int [ds](structarch__esf.md#adbdb731abf4be35509eec853ecddc601);

37#endif

[ 38](structarch__esf.md#a6c501100e54db4c1e4685090b0785889) unsigned int [esp](structarch__esf.md#a6c501100e54db4c1e4685090b0785889);

[ 39](structarch__esf.md#aa66aa75f640c3f5c1455b3c185fa92a0) unsigned int [ebp](structarch__esf.md#aa66aa75f640c3f5c1455b3c185fa92a0);

[ 40](structarch__esf.md#a7dee4cd6c1c3fe496754c1e9c37d6e5e) unsigned int [ebx](structarch__esf.md#a7dee4cd6c1c3fe496754c1e9c37d6e5e);

[ 41](structarch__esf.md#a260832877afcad7ae2be72244a6c30a4) unsigned int [esi](structarch__esf.md#a260832877afcad7ae2be72244a6c30a4);

[ 42](structarch__esf.md#a7247267fa4d4771bc389bef8ba38e820) unsigned int [edi](structarch__esf.md#a7247267fa4d4771bc389bef8ba38e820);

[ 43](structarch__esf.md#ace05744212c1665a672b2ced419f9bfc) unsigned int [edx](structarch__esf.md#ace05744212c1665a672b2ced419f9bfc);

[ 44](structarch__esf.md#a56d08dbd84879425ec2e905c03929048) unsigned int [eax](structarch__esf.md#a56d08dbd84879425ec2e905c03929048);

[ 45](structarch__esf.md#a899ead638078796464d40e4f67702df8) unsigned int [ecx](structarch__esf.md#a899ead638078796464d40e4f67702df8);

[ 46](structarch__esf.md#a7f8bfa097d38019069d787f15fa535dc) unsigned int [errorCode](structarch__esf.md#a7f8bfa097d38019069d787f15fa535dc);

[ 47](structarch__esf.md#a9053fc737ec314b9c97095e0267a92f7) unsigned int [eip](structarch__esf.md#a9053fc737ec314b9c97095e0267a92f7);

[ 48](structarch__esf.md#ad8b1433dc80019463acefab616d74782) unsigned int [cs](structarch__esf.md#ad8b1433dc80019463acefab616d74782);

[ 49](structarch__esf.md#ac64b0d4af1e920f75c7c844725a84c7c) unsigned int [eflags](structarch__esf.md#ac64b0d4af1e920f75c7c844725a84c7c);

50};

51

52extern unsigned int z\_x86\_exception\_vector;

53

54struct \_x86\_syscall\_stack\_frame {

55 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) eip;

56 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cs;

57 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) eflags;

58

59 /\* These are only present if cs = USER\_CODE\_SEG \*/

60 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) esp;

61 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ss;

62};

63

64#ifdef \_\_cplusplus

65}

66#endif

67

68#endif /\* \_ASMLANGUAGE \*/

69

70#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_EXCEPTION\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[arch\_esf::fs](structarch__esf.md#a1f127199573607f22a4c0e95d3b5ce74)

unsigned int fs

**Definition** exception.h:34

[arch\_esf::ss](structarch__esf.md#a25aae07c91f6946596f92f0069d6729a)

unsigned int ss

**Definition** exception.h:32

[arch\_esf::esi](structarch__esf.md#a260832877afcad7ae2be72244a6c30a4)

unsigned int esi

**Definition** exception.h:41

[arch\_esf::gs](structarch__esf.md#a353cd21036946b829a01ab9e247bf72d)

unsigned int gs

**Definition** exception.h:33

[arch\_esf::eax](structarch__esf.md#a56d08dbd84879425ec2e905c03929048)

unsigned int eax

**Definition** exception.h:44

[arch\_esf::esp](structarch__esf.md#a6c501100e54db4c1e4685090b0785889)

unsigned int esp

**Definition** exception.h:38

[arch\_esf::edi](structarch__esf.md#a7247267fa4d4771bc389bef8ba38e820)

unsigned int edi

**Definition** exception.h:42

[arch\_esf::ebx](structarch__esf.md#a7dee4cd6c1c3fe496754c1e9c37d6e5e)

unsigned int ebx

**Definition** exception.h:40

[arch\_esf::errorCode](structarch__esf.md#a7f8bfa097d38019069d787f15fa535dc)

unsigned int errorCode

**Definition** exception.h:46

[arch\_esf::ecx](structarch__esf.md#a899ead638078796464d40e4f67702df8)

unsigned int ecx

**Definition** exception.h:45

[arch\_esf::eip](structarch__esf.md#a9053fc737ec314b9c97095e0267a92f7)

unsigned int eip

**Definition** exception.h:47

[arch\_esf::ebp](structarch__esf.md#aa66aa75f640c3f5c1455b3c185fa92a0)

unsigned int ebp

**Definition** exception.h:39

[arch\_esf::es](structarch__esf.md#aac9b040d864214b71afb15e618a300da)

unsigned int es

**Definition** exception.h:35

[arch\_esf::eflags](structarch__esf.md#ac64b0d4af1e920f75c7c844725a84c7c)

unsigned int eflags

**Definition** exception.h:49

[arch\_esf::edx](structarch__esf.md#ace05744212c1665a672b2ced419f9bfc)

unsigned int edx

**Definition** exception.h:43

[arch\_esf::cs](structarch__esf.md#ad8b1433dc80019463acefab616d74782)

unsigned int cs

**Definition** exception.h:48

[arch\_esf::ds](structarch__esf.md#adbdb731abf4be35509eec853ecddc601)

unsigned int ds

**Definition** exception.h:36

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [exception.h](x86_2ia32_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
