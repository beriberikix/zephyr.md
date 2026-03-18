---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/riscv_2exception_8h_source.html
original_path: doxygen/html/riscv_2exception_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](riscv_2exception_8h.md)

1/\*

2 \* Copyright (c) 2016 Jean-Paul Etienne <fractalclone@gmail.com>

3 \* Copyright (c) 2018 Foundries.io Ltd

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_RISCV\_EXCEPTION\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_RISCV\_EXCEPTION\_H\_

17

18#ifndef \_ASMLANGUAGE

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20#include <[zephyr/toolchain.h](toolchain_8h.md)>

21

22#ifdef CONFIG\_RISCV\_SOC\_CONTEXT\_SAVE

23#include <soc\_context.h>

24#endif

25

26#ifdef CONFIG\_RISCV\_SOC\_HAS\_ISR\_STACKING

27#include <soc\_isr\_stacking.h>

28#endif

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

34/\*

35 \* The name of the structure which contains soc-specific state, if

36 \* any, as well as the soc\_esf\_t typedef below, are part of the RISC-V

37 \* arch API.

38 \*

39 \* The contents of the struct are provided by a SOC-specific

40 \* definition in soc\_context.h.

41 \*/

42#ifdef CONFIG\_RISCV\_SOC\_CONTEXT\_SAVE

43struct soc\_esf {

44 SOC\_ESF\_MEMBERS;

45};

46#endif

47

48#if defined(CONFIG\_RISCV\_SOC\_HAS\_ISR\_STACKING)

49 SOC\_ISR\_STACKING\_ESF\_DECLARE;

50#else

51struct [arch\_esf](structarch__esf.md) {

52 unsigned long [ra](structarch__esf.md#a22241917474aaf5718780c55c65be33f); /\* return address \*/

53

54 unsigned long [t0](structarch__esf.md#a3669d6b58ca5da0dd89a904186ad74ba); /\* Caller-saved temporary register \*/

55 unsigned long [t1](structarch__esf.md#ae96b6de3f7fe95b12a5590b68cfca40e); /\* Caller-saved temporary register \*/

56 unsigned long [t2](structarch__esf.md#aba3b4051cbac23bbadfaa262b83de953); /\* Caller-saved temporary register \*/

57#if !defined(CONFIG\_RISCV\_ISA\_RV32E)

58 unsigned long [t3](structarch__esf.md#af280445d5be52877f9a7d48787bd5604); /\* Caller-saved temporary register \*/

59 unsigned long [t4](structarch__esf.md#a81163becab1b4d7c244f0b5af3accae9); /\* Caller-saved temporary register \*/

60 unsigned long [t5](structarch__esf.md#ad01a8b2c465aead38705b0b6cbb4af96); /\* Caller-saved temporary register \*/

61 unsigned long [t6](structarch__esf.md#a7247ee9003b3c26a6bab8c82ab61786b); /\* Caller-saved temporary register \*/

62#endif /\* !CONFIG\_RISCV\_ISA\_RV32E \*/

63

64 unsigned long [a0](structarch__esf.md#a0186f8ac5c6949fea58d1da9061fa419); /\* function argument/return value \*/

65 unsigned long [a1](structarch__esf.md#a62a1feb37b8724ada83d70caae38a673); /\* function argument \*/

66 unsigned long [a2](structarch__esf.md#adc1040e4224662f77875db24635ceb84); /\* function argument \*/

67 unsigned long [a3](structarch__esf.md#a3f2e9029daddabeefd2b2c253efd6c83); /\* function argument \*/

[ 68](structarch__esf.md#a2a794aaedfc9c499f5f98a0bb62936ad) unsigned long [a4](structarch__esf.md#a2a794aaedfc9c499f5f98a0bb62936ad); /\* function argument \*/

[ 69](structarch__esf.md#abab1419a6c1fd7b294f997f0e58bcc45) unsigned long [a5](structarch__esf.md#abab1419a6c1fd7b294f997f0e58bcc45); /\* function argument \*/

70#if !defined(CONFIG\_RISCV\_ISA\_RV32E)

[ 71](structarch__esf.md#a463bd3c45ff943e618c9dd628918b520) unsigned long [a6](structarch__esf.md#a463bd3c45ff943e618c9dd628918b520); /\* function argument \*/

[ 72](structarch__esf.md#a7fcc14965783e368cd0f3ecc33517147) unsigned long [a7](structarch__esf.md#a7fcc14965783e368cd0f3ecc33517147); /\* function argument \*/

73#endif /\* !CONFIG\_RISCV\_ISA\_RV32E \*/

74

[ 75](structarch__esf.md#a62c66377b82031f09d6e1ec6591b3b86) unsigned long [mepc](structarch__esf.md#a62c66377b82031f09d6e1ec6591b3b86); /\* machine exception program counter \*/

[ 76](structarch__esf.md#a6e1afae6a77e6eb0624aa982a07813c3) unsigned long [mstatus](structarch__esf.md#a6e1afae6a77e6eb0624aa982a07813c3); /\* machine status register \*/

77

[ 78](structarch__esf.md#a8138142006da6c5abd397faac0379cfa) unsigned long [s0](structarch__esf.md#a8138142006da6c5abd397faac0379cfa); /\* callee-saved s0 \*/

79

80#ifdef CONFIG\_USERSPACE

[ 81](structarch__esf.md#a9c3e060a48caeb59d2625e921f1f6d15) unsigned long [sp](structarch__esf.md#a9c3e060a48caeb59d2625e921f1f6d15); /\* preserved (user or kernel) stack pointer \*/

82#endif

83

84#ifdef CONFIG\_RISCV\_SOC\_CONTEXT\_SAVE

85 struct soc\_esf soc\_context;

86#endif

87} \_\_aligned(16);

88#endif /\* CONFIG\_RISCV\_SOC\_HAS\_ISR\_STACKING \*/

89

90#ifdef CONFIG\_RISCV\_SOC\_CONTEXT\_SAVE

91typedef struct soc\_esf soc\_esf\_t;

92#endif

93

94#ifdef \_\_cplusplus

95}

96#endif

97

98#endif /\* \_ASMLANGUAGE \*/

99

100#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RISCV\_EXCEPTION\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:57

[arch\_esf::a0](structarch__esf.md#a0186f8ac5c6949fea58d1da9061fa419)

unsigned long a0

**Definition** exception.h:35

[arch\_esf::ra](structarch__esf.md#a22241917474aaf5718780c55c65be33f)

unsigned long ra

**Definition** exception.h:21

[arch\_esf::a4](structarch__esf.md#a2a794aaedfc9c499f5f98a0bb62936ad)

unsigned long a4

**Definition** exception.h:68

[arch\_esf::t0](structarch__esf.md#a3669d6b58ca5da0dd89a904186ad74ba)

unsigned long t0

**Definition** exception.h:24

[arch\_esf::a3](structarch__esf.md#a3f2e9029daddabeefd2b2c253efd6c83)

unsigned long a3

**Definition** exception.h:38

[arch\_esf::a6](structarch__esf.md#a463bd3c45ff943e618c9dd628918b520)

unsigned long a6

**Definition** exception.h:71

[arch\_esf::a1](structarch__esf.md#a62a1feb37b8724ada83d70caae38a673)

unsigned long a1

**Definition** exception.h:36

[arch\_esf::mepc](structarch__esf.md#a62c66377b82031f09d6e1ec6591b3b86)

unsigned long mepc

**Definition** exception.h:75

[arch\_esf::mstatus](structarch__esf.md#a6e1afae6a77e6eb0624aa982a07813c3)

unsigned long mstatus

**Definition** exception.h:76

[arch\_esf::t6](structarch__esf.md#a7247ee9003b3c26a6bab8c82ab61786b)

unsigned long t6

**Definition** exception.h:30

[arch\_esf::a7](structarch__esf.md#a7fcc14965783e368cd0f3ecc33517147)

unsigned long a7

**Definition** exception.h:72

[arch\_esf::t4](structarch__esf.md#a81163becab1b4d7c244f0b5af3accae9)

unsigned long t4

**Definition** exception.h:28

[arch\_esf::s0](structarch__esf.md#a8138142006da6c5abd397faac0379cfa)

unsigned long s0

**Definition** exception.h:78

[arch\_esf::sp](structarch__esf.md#a9c3e060a48caeb59d2625e921f1f6d15)

unsigned long sp

**Definition** exception.h:81

[arch\_esf::t2](structarch__esf.md#aba3b4051cbac23bbadfaa262b83de953)

unsigned long t2

**Definition** exception.h:26

[arch\_esf::a5](structarch__esf.md#abab1419a6c1fd7b294f997f0e58bcc45)

unsigned long a5

**Definition** exception.h:69

[arch\_esf::t5](structarch__esf.md#ad01a8b2c465aead38705b0b6cbb4af96)

unsigned long t5

**Definition** exception.h:29

[arch\_esf::a2](structarch__esf.md#adc1040e4224662f77875db24635ceb84)

unsigned long a2

**Definition** exception.h:37

[arch\_esf::t1](structarch__esf.md#ae96b6de3f7fe95b12a5590b68cfca40e)

unsigned long t1

**Definition** exception.h:25

[arch\_esf::t3](structarch__esf.md#af280445d5be52877f9a7d48787bd5604)

unsigned long t3

**Definition** exception.h:27

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [exception.h](riscv_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
