---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mips_2exception_8h_source.html
original_path: doxygen/html/mips_2exception_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](mips_2exception_8h.md)

1/\*

2 \* Copyright (c) 2021 Antony Pavlov <antonynpavlov@gmail.com>

3 \*

4 \* based on include/arch/riscv/exception.h

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_MIPS\_EXCEPTION\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_MIPS\_EXCEPTION\_H\_

11

12#ifndef \_ASMLANGUAGE

13#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

14#include <[zephyr/toolchain.h](toolchain_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20struct [arch\_esf](structarch__esf.md) {

[ 21](structarch__esf.md#a22241917474aaf5718780c55c65be33f) unsigned long [ra](structarch__esf.md#a22241917474aaf5718780c55c65be33f); /\* return address \*/

[ 22](structarch__esf.md#a0256d0bf331458b345ea25e1862e1bf1) unsigned long [gp](structarch__esf.md#a0256d0bf331458b345ea25e1862e1bf1); /\* global pointer \*/

23

[ 24](structarch__esf.md#a3669d6b58ca5da0dd89a904186ad74ba) unsigned long [t0](structarch__esf.md#a3669d6b58ca5da0dd89a904186ad74ba); /\* Caller-saved temporary register \*/

[ 25](structarch__esf.md#ae96b6de3f7fe95b12a5590b68cfca40e) unsigned long [t1](structarch__esf.md#ae96b6de3f7fe95b12a5590b68cfca40e); /\* Caller-saved temporary register \*/

[ 26](structarch__esf.md#aba3b4051cbac23bbadfaa262b83de953) unsigned long [t2](structarch__esf.md#aba3b4051cbac23bbadfaa262b83de953); /\* Caller-saved temporary register \*/

[ 27](structarch__esf.md#af280445d5be52877f9a7d48787bd5604) unsigned long [t3](structarch__esf.md#af280445d5be52877f9a7d48787bd5604); /\* Caller-saved temporary register \*/

[ 28](structarch__esf.md#a81163becab1b4d7c244f0b5af3accae9) unsigned long [t4](structarch__esf.md#a81163becab1b4d7c244f0b5af3accae9); /\* Caller-saved temporary register \*/

[ 29](structarch__esf.md#ad01a8b2c465aead38705b0b6cbb4af96) unsigned long [t5](structarch__esf.md#ad01a8b2c465aead38705b0b6cbb4af96); /\* Caller-saved temporary register \*/

[ 30](structarch__esf.md#a7247ee9003b3c26a6bab8c82ab61786b) unsigned long [t6](structarch__esf.md#a7247ee9003b3c26a6bab8c82ab61786b); /\* Caller-saved temporary register \*/

[ 31](structarch__esf.md#a8e98b1d9dffeb236db5f4df952842b78) unsigned long [t7](structarch__esf.md#a8e98b1d9dffeb236db5f4df952842b78); /\* Caller-saved temporary register \*/

[ 32](structarch__esf.md#a41e3b393531a98223054e525bd18237e) unsigned long [t8](structarch__esf.md#a41e3b393531a98223054e525bd18237e); /\* Caller-saved temporary register \*/

[ 33](structarch__esf.md#a91f025811139eb2ed9f9d6f3a1ee482f) unsigned long [t9](structarch__esf.md#a91f025811139eb2ed9f9d6f3a1ee482f); /\* Caller-saved temporary register \*/

34

[ 35](structarch__esf.md#a0186f8ac5c6949fea58d1da9061fa419) unsigned long [a0](structarch__esf.md#a0186f8ac5c6949fea58d1da9061fa419); /\* function argument \*/

[ 36](structarch__esf.md#a62a1feb37b8724ada83d70caae38a673) unsigned long [a1](structarch__esf.md#a62a1feb37b8724ada83d70caae38a673); /\* function argument \*/

[ 37](structarch__esf.md#adc1040e4224662f77875db24635ceb84) unsigned long [a2](structarch__esf.md#adc1040e4224662f77875db24635ceb84); /\* function argument \*/

[ 38](structarch__esf.md#a3f2e9029daddabeefd2b2c253efd6c83) unsigned long [a3](structarch__esf.md#a3f2e9029daddabeefd2b2c253efd6c83); /\* function argument \*/

39

[ 40](structarch__esf.md#ac2e9705feb9d23a650939cb42efb0ed7) unsigned long [v0](structarch__esf.md#ac2e9705feb9d23a650939cb42efb0ed7); /\* return value \*/

[ 41](structarch__esf.md#a53bcb9b20c29225952fa15ed94fc56ff) unsigned long [v1](structarch__esf.md#a53bcb9b20c29225952fa15ed94fc56ff); /\* return value \*/

42

[ 43](structarch__esf.md#a84c6de4138983cb180f6d8f1faa30e3b) unsigned long [at](structarch__esf.md#a84c6de4138983cb180f6d8f1faa30e3b); /\* assembly temporary \*/

44

[ 45](structarch__esf.md#a2c97b72603f596d88e2b01367a230a4c) unsigned long [epc](structarch__esf.md#a2c97b72603f596d88e2b01367a230a4c);

[ 46](structarch__esf.md#a1094f36597a23bf73c6574b4457049c5) unsigned long [badvaddr](structarch__esf.md#a1094f36597a23bf73c6574b4457049c5);

[ 47](structarch__esf.md#af249e64a0c2755e2bdab36cc5af721e1) unsigned long [hi](structarch__esf.md#af249e64a0c2755e2bdab36cc5af721e1);

[ 48](structarch__esf.md#a5c608ad064989abef5fb69fcd422d617) unsigned long [lo](structarch__esf.md#a5c608ad064989abef5fb69fcd422d617);

[ 49](structarch__esf.md#abe2ac128675534aa53d4434b32e39fb4) unsigned long [status](structarch__esf.md#abe2ac128675534aa53d4434b32e39fb4);

[ 50](structarch__esf.md#aa0f0105b2ae3986c3b8f1f8927064568) unsigned long [cause](structarch__esf.md#aa0f0105b2ae3986c3b8f1f8927064568);

51};

52

53#ifdef \_\_cplusplus

54}

55#endif

56

57#endif /\* \_ASMLANGUAGE \*/

58

59#endif /\* ZEPHYR\_INCLUDE\_ARCH\_MIPS\_EXCEPTION\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[arch\_esf::a0](structarch__esf.md#a0186f8ac5c6949fea58d1da9061fa419)

unsigned long a0

**Definition** exception.h:35

[arch\_esf::gp](structarch__esf.md#a0256d0bf331458b345ea25e1862e1bf1)

unsigned long gp

**Definition** exception.h:22

[arch\_esf::badvaddr](structarch__esf.md#a1094f36597a23bf73c6574b4457049c5)

unsigned long badvaddr

**Definition** exception.h:46

[arch\_esf::ra](structarch__esf.md#a22241917474aaf5718780c55c65be33f)

unsigned long ra

**Definition** exception.h:21

[arch\_esf::epc](structarch__esf.md#a2c97b72603f596d88e2b01367a230a4c)

unsigned long epc

**Definition** exception.h:45

[arch\_esf::t0](structarch__esf.md#a3669d6b58ca5da0dd89a904186ad74ba)

unsigned long t0

**Definition** exception.h:24

[arch\_esf::a3](structarch__esf.md#a3f2e9029daddabeefd2b2c253efd6c83)

unsigned long a3

**Definition** exception.h:38

[arch\_esf::t8](structarch__esf.md#a41e3b393531a98223054e525bd18237e)

unsigned long t8

**Definition** exception.h:32

[arch\_esf::v1](structarch__esf.md#a53bcb9b20c29225952fa15ed94fc56ff)

unsigned long v1

**Definition** exception.h:41

[arch\_esf::lo](structarch__esf.md#a5c608ad064989abef5fb69fcd422d617)

unsigned long lo

**Definition** exception.h:48

[arch\_esf::a1](structarch__esf.md#a62a1feb37b8724ada83d70caae38a673)

unsigned long a1

**Definition** exception.h:36

[arch\_esf::t6](structarch__esf.md#a7247ee9003b3c26a6bab8c82ab61786b)

unsigned long t6

**Definition** exception.h:30

[arch\_esf::t4](structarch__esf.md#a81163becab1b4d7c244f0b5af3accae9)

unsigned long t4

**Definition** exception.h:28

[arch\_esf::at](structarch__esf.md#a84c6de4138983cb180f6d8f1faa30e3b)

unsigned long at

**Definition** exception.h:43

[arch\_esf::t7](structarch__esf.md#a8e98b1d9dffeb236db5f4df952842b78)

unsigned long t7

**Definition** exception.h:31

[arch\_esf::t9](structarch__esf.md#a91f025811139eb2ed9f9d6f3a1ee482f)

unsigned long t9

**Definition** exception.h:33

[arch\_esf::cause](structarch__esf.md#aa0f0105b2ae3986c3b8f1f8927064568)

unsigned long cause

**Definition** exception.h:50

[arch\_esf::t2](structarch__esf.md#aba3b4051cbac23bbadfaa262b83de953)

unsigned long t2

**Definition** exception.h:26

[arch\_esf::status](structarch__esf.md#abe2ac128675534aa53d4434b32e39fb4)

unsigned long status

**Definition** exception.h:49

[arch\_esf::v0](structarch__esf.md#ac2e9705feb9d23a650939cb42efb0ed7)

unsigned long v0

**Definition** exception.h:40

[arch\_esf::t5](structarch__esf.md#ad01a8b2c465aead38705b0b6cbb4af96)

unsigned long t5

**Definition** exception.h:29

[arch\_esf::a2](structarch__esf.md#adc1040e4224662f77875db24635ceb84)

unsigned long a2

**Definition** exception.h:37

[arch\_esf::t1](structarch__esf.md#ae96b6de3f7fe95b12a5590b68cfca40e)

unsigned long t1

**Definition** exception.h:25

[arch\_esf::hi](structarch__esf.md#af249e64a0c2755e2bdab36cc5af721e1)

unsigned long hi

**Definition** exception.h:47

[arch\_esf::t3](structarch__esf.md#af280445d5be52877f9a7d48787bd5604)

unsigned long t3

**Definition** exception.h:27

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [mips](dir_fc8c8ea71cc5b300c3fa15bb05243853.md)
- [exception.h](mips_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
