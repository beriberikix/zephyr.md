---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/smf_8h_source.html
original_path: doxygen/html/smf_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smf.h

[Go to the documentation of this file.](smf_8h.md)

1/\*

2 \* Copyright 2021 The Chromium OS Authors

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_SMF\_H\_

14#define ZEPHYR\_INCLUDE\_SMF\_H\_

15

16#include <[zephyr/sys/util.h](sys_2util_8h.md)>

17

25

35/\* clang-format off \*/

[ 36](group__smf.md#ga5760b98a36ed1ac55eba700cf44c7e1e)#define SMF\_CREATE\_STATE(\_entry, \_run, \_exit, \_parent, \_initial) \

37{ \

38 .entry = \_entry, \

39 .run = \_run, \

40 .exit = \_exit, \

41 IF\_ENABLED(CONFIG\_SMF\_ANCESTOR\_SUPPORT, (.parent = \_parent,)) \

42 IF\_ENABLED(CONFIG\_SMF\_INITIAL\_TRANSITION, (.initial = \_initial,)) \

43}

44/\* clang-format on \*/

45

[ 52](group__smf.md#ga0bccd3bf96e0887e8a610c1b06e22237)#define SMF\_CTX(o) ((struct smf\_ctx \*)o)

53

54#ifdef \_\_cplusplus

55extern "C" {

56#endif

57

58#include <[zephyr/kernel.h](kernel_8h.md)>

59

[ 63](group__smf.md#ga01e4e2d2f35a9ec790d5e3c5b9b91b55)enum [smf\_state\_result](group__smf.md#ga01e4e2d2f35a9ec790d5e3c5b9b91b55) {

[ 64](group__smf.md#gga01e4e2d2f35a9ec790d5e3c5b9b91b55a088a71df8c1eb56aec8e4ef647a2248a) [SMF\_EVENT\_HANDLED](group__smf.md#gga01e4e2d2f35a9ec790d5e3c5b9b91b55a088a71df8c1eb56aec8e4ef647a2248a),

[ 65](group__smf.md#gga01e4e2d2f35a9ec790d5e3c5b9b91b55af86126b6ae29cfa0c1816bc5fb2873b6) [SMF\_EVENT\_PROPAGATE](group__smf.md#gga01e4e2d2f35a9ec790d5e3c5b9b91b55af86126b6ae29cfa0c1816bc5fb2873b6),

66};

67

[ 74](group__smf.md#ga050cbb0a791dc062d222c0cfb4366f43)typedef void (\*[state\_method](group__smf.md#gace21c98a982b640c75951676d6ee3988))(void \*obj);

75

83typedef enum [smf\_state\_result](group__smf.md#ga01e4e2d2f35a9ec790d5e3c5b9b91b55) (\*[state\_execution](group__smf.md#ga050cbb0a791dc062d222c0cfb4366f43))(void \*obj);

84

[ 86](structsmf__state.md)struct [smf\_state](structsmf__state.md) {

[ 88](structsmf__state.md#a742fe438b7b5b014d23bde210a512dee) const [state\_method](group__smf.md#gace21c98a982b640c75951676d6ee3988) [entry](structsmf__state.md#a742fe438b7b5b014d23bde210a512dee);

89

[ 94](structsmf__state.md#a94adbcd4e1a8bce8f3b30082874f1911) const [state\_execution](group__smf.md#ga050cbb0a791dc062d222c0cfb4366f43) [run](structsmf__state.md#a94adbcd4e1a8bce8f3b30082874f1911);

95

[ 97](structsmf__state.md#a0661b4257b2ff7c508aeef9822b90a2f) const [state\_method](group__smf.md#gace21c98a982b640c75951676d6ee3988) [exit](structsmf__state.md#a0661b4257b2ff7c508aeef9822b90a2f);

98#ifdef CONFIG\_SMF\_ANCESTOR\_SUPPORT

109 const struct [smf\_state](structsmf__state.md) \*parent;

110

111#ifdef CONFIG\_SMF\_INITIAL\_TRANSITION

115 const struct [smf\_state](structsmf__state.md) \*initial;

116#endif /\* CONFIG\_SMF\_INITIAL\_TRANSITION \*/

117#endif /\* CONFIG\_SMF\_ANCESTOR\_SUPPORT \*/

118};

119

[ 121](structsmf__ctx.md)struct [smf\_ctx](structsmf__ctx.md) {

[ 123](structsmf__ctx.md#a48736dbfad38f0b25e4ab2a36d2f482a) const struct [smf\_state](structsmf__state.md) \*[current](structsmf__ctx.md#a48736dbfad38f0b25e4ab2a36d2f482a);

[ 125](structsmf__ctx.md#a2cebcd02bfc6b36278c20fe8e0f95418) const struct [smf\_state](structsmf__state.md) \*[previous](structsmf__ctx.md#a2cebcd02bfc6b36278c20fe8e0f95418);

126

127#ifdef CONFIG\_SMF\_ANCESTOR\_SUPPORT

129 const struct [smf\_state](structsmf__state.md) \*executing;

130#endif /\* CONFIG\_SMF\_ANCESTOR\_SUPPORT \*/

[ 137](structsmf__ctx.md#a1018c3dc6d7cc94ac2b64f95e5c053cd) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [terminate\_val](structsmf__ctx.md#a1018c3dc6d7cc94ac2b64f95e5c053cd);

[ 142](structsmf__ctx.md#afb094c0e87d42ec7ca780a2859be7bf8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [internal](structsmf__ctx.md#afb094c0e87d42ec7ca780a2859be7bf8);

143};

144

[ 151](group__smf.md#ga4389086c6aa3167e8c49226323ae208d)void [smf\_set\_initial](group__smf.md#ga4389086c6aa3167e8c49226323ae208d)(struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*init\_state);

152

[ 161](group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)void [smf\_set\_state](group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)(struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*new\_state);

162

[ 170](group__smf.md#gaae28c66f0652c99ba8e843eeaf02aaf7)void [smf\_set\_terminate](group__smf.md#gaae28c66f0652c99ba8e843eeaf02aaf7)(struct [smf\_ctx](structsmf__ctx.md) \*ctx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val);

171

[ 181](group__smf.md#ga8399cfa9e793a7f188b4ed4fec9f4f90)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [smf\_run\_state](group__smf.md#ga8399cfa9e793a7f188b4ed4fec9f4f90)(struct [smf\_ctx](structsmf__ctx.md) \*ctx);

182

183#ifdef \_\_cplusplus

184}

185#endif

186

190

191#endif /\* ZEPHYR\_INCLUDE\_SMF\_H\_ \*/

[smf\_state\_result](group__smf.md#ga01e4e2d2f35a9ec790d5e3c5b9b91b55)

smf\_state\_result

enum for the return value of a state\_execution function

**Definition** smf.h:63

[state\_execution](group__smf.md#ga050cbb0a791dc062d222c0cfb4366f43)

enum smf\_state\_result(\* state\_execution)(void \*obj)

Function pointer that implements a the run action of a state.

**Definition** smf.h:83

[smf\_set\_state](group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)

void smf\_set\_state(struct smf\_ctx \*ctx, const struct smf\_state \*new\_state)

Changes a state machines state.

[smf\_set\_initial](group__smf.md#ga4389086c6aa3167e8c49226323ae208d)

void smf\_set\_initial(struct smf\_ctx \*ctx, const struct smf\_state \*init\_state)

Initializes the state machine and sets its initial state.

[smf\_run\_state](group__smf.md#ga8399cfa9e793a7f188b4ed4fec9f4f90)

int32\_t smf\_run\_state(struct smf\_ctx \*ctx)

Runs one iteration of a state machine (including any parent states).

[smf\_set\_terminate](group__smf.md#gaae28c66f0652c99ba8e843eeaf02aaf7)

void smf\_set\_terminate(struct smf\_ctx \*ctx, int32\_t val)

Terminate a state machine.

[state\_method](group__smf.md#gace21c98a982b640c75951676d6ee3988)

void(\* state\_method)(void \*obj)

Function pointer that implements a entry and exit actions of a state.

**Definition** smf.h:74

[SMF\_EVENT\_HANDLED](group__smf.md#gga01e4e2d2f35a9ec790d5e3c5b9b91b55a088a71df8c1eb56aec8e4ef647a2248a)

@ SMF\_EVENT\_HANDLED

**Definition** smf.h:64

[SMF\_EVENT\_PROPAGATE](group__smf.md#gga01e4e2d2f35a9ec790d5e3c5b9b91b55af86126b6ae29cfa0c1816bc5fb2873b6)

@ SMF\_EVENT\_PROPAGATE

**Definition** smf.h:65

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[smf\_ctx](structsmf__ctx.md)

Defines the current context of the state machine.

**Definition** smf.h:121

[smf\_ctx::terminate\_val](structsmf__ctx.md#a1018c3dc6d7cc94ac2b64f95e5c053cd)

int32\_t terminate\_val

This value is set by the set\_terminate function and should terminate the state machine when its set t...

**Definition** smf.h:137

[smf\_ctx::previous](structsmf__ctx.md#a2cebcd02bfc6b36278c20fe8e0f95418)

const struct smf\_state \* previous

Previous state the state machine executed.

**Definition** smf.h:125

[smf\_ctx::current](structsmf__ctx.md#a48736dbfad38f0b25e4ab2a36d2f482a)

const struct smf\_state \* current

Current state the state machine is executing.

**Definition** smf.h:123

[smf\_ctx::internal](structsmf__ctx.md#afb094c0e87d42ec7ca780a2859be7bf8)

uint32\_t internal

The state machine casts this to a "struct internal\_ctx" and it's used to track state machine context.

**Definition** smf.h:142

[smf\_state](structsmf__state.md)

General state that can be used in multiple state machines.

**Definition** smf.h:86

[smf\_state::exit](structsmf__state.md#a0661b4257b2ff7c508aeef9822b90a2f)

const state\_method exit

Optional method that will be run when this state exists.

**Definition** smf.h:97

[smf\_state::entry](structsmf__state.md#a742fe438b7b5b014d23bde210a512dee)

const state\_method entry

Optional method that will be run when this state is entered.

**Definition** smf.h:88

[smf\_state::run](structsmf__state.md#a94adbcd4e1a8bce8f3b30082874f1911)

const state\_execution run

Optional method that will be run repeatedly during state machine loop.

**Definition** smf.h:94

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [smf.h](smf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
