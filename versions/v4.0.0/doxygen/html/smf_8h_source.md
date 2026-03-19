---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/smf_8h_source.html
original_path: doxygen/html/smf_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

[ 35](group__smf.md#ga5760b98a36ed1ac55eba700cf44c7e1e)#define SMF\_CREATE\_STATE(\_entry, \_run, \_exit, \_parent, \_initial) \

36{ \

37 .entry = \_entry, \

38 .run = \_run, \

39 .exit = \_exit, \

40 IF\_ENABLED(CONFIG\_SMF\_ANCESTOR\_SUPPORT, (.parent = \_parent,)) \

41 IF\_ENABLED(CONFIG\_SMF\_INITIAL\_TRANSITION, (.initial = \_initial,)) \

42}

43

[ 50](group__smf.md#ga0bccd3bf96e0887e8a610c1b06e22237)#define SMF\_CTX(o) ((struct smf\_ctx \*)o)

51

52#ifdef \_\_cplusplus

53extern "C" {

54#endif

55

56#include <[zephyr/kernel.h](kernel_8h.md)>

57

[ 63](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6)typedef void (\*[state\_execution](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6))(void \*obj);

64

[ 66](structsmf__state.md)struct [smf\_state](structsmf__state.md) {

[ 68](structsmf__state.md#a63ea395c90fa8118cf355e55e60cee26) const [state\_execution](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6) [entry](structsmf__state.md#a63ea395c90fa8118cf355e55e60cee26);

[ 73](structsmf__state.md#a94adbcd4e1a8bce8f3b30082874f1911) const [state\_execution](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6) [run](structsmf__state.md#a94adbcd4e1a8bce8f3b30082874f1911);

[ 75](structsmf__state.md#a2df810ca49fbb9438ee78317feaaf09b) const [state\_execution](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6) [exit](structsmf__state.md#a2df810ca49fbb9438ee78317feaaf09b);

76#ifdef CONFIG\_SMF\_ANCESTOR\_SUPPORT

87 const struct [smf\_state](structsmf__state.md) \*parent;

88

89#ifdef CONFIG\_SMF\_INITIAL\_TRANSITION

93 const struct [smf\_state](structsmf__state.md) \*initial;

94#endif /\* CONFIG\_SMF\_INITIAL\_TRANSITION \*/

95#endif /\* CONFIG\_SMF\_ANCESTOR\_SUPPORT \*/

96};

97

[ 99](structsmf__ctx.md)struct [smf\_ctx](structsmf__ctx.md) {

[ 101](structsmf__ctx.md#a48736dbfad38f0b25e4ab2a36d2f482a) const struct [smf\_state](structsmf__state.md) \*[current](structsmf__ctx.md#a48736dbfad38f0b25e4ab2a36d2f482a);

[ 103](structsmf__ctx.md#a2cebcd02bfc6b36278c20fe8e0f95418) const struct [smf\_state](structsmf__state.md) \*[previous](structsmf__ctx.md#a2cebcd02bfc6b36278c20fe8e0f95418);

104

105#ifdef CONFIG\_SMF\_ANCESTOR\_SUPPORT

107 const struct [smf\_state](structsmf__state.md) \*executing;

108#endif /\* CONFIG\_SMF\_ANCESTOR\_SUPPORT \*/

[ 115](structsmf__ctx.md#a1018c3dc6d7cc94ac2b64f95e5c053cd) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [terminate\_val](structsmf__ctx.md#a1018c3dc6d7cc94ac2b64f95e5c053cd);

[ 120](structsmf__ctx.md#afb094c0e87d42ec7ca780a2859be7bf8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [internal](structsmf__ctx.md#afb094c0e87d42ec7ca780a2859be7bf8);

121};

122

[ 129](group__smf.md#ga4389086c6aa3167e8c49226323ae208d)void [smf\_set\_initial](group__smf.md#ga4389086c6aa3167e8c49226323ae208d)(struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*init\_state);

130

[ 139](group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)void [smf\_set\_state](group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)(struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*new\_state);

140

[ 148](group__smf.md#gaae28c66f0652c99ba8e843eeaf02aaf7)void [smf\_set\_terminate](group__smf.md#gaae28c66f0652c99ba8e843eeaf02aaf7)(struct [smf\_ctx](structsmf__ctx.md) \*ctx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val);

149

[ 157](group__smf.md#gaa187bbd70434d29c319089faf50c2526)void [smf\_set\_handled](group__smf.md#gaa187bbd70434d29c319089faf50c2526)(struct [smf\_ctx](structsmf__ctx.md) \*ctx);

158

[ 168](group__smf.md#ga8399cfa9e793a7f188b4ed4fec9f4f90)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [smf\_run\_state](group__smf.md#ga8399cfa9e793a7f188b4ed4fec9f4f90)(struct [smf\_ctx](structsmf__ctx.md) \*ctx);

169

170#ifdef \_\_cplusplus

171}

172#endif

173

177

178#endif /\* ZEPHYR\_INCLUDE\_SMF\_H\_ \*/

[smf\_set\_state](group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)

void smf\_set\_state(struct smf\_ctx \*ctx, const struct smf\_state \*new\_state)

Changes a state machines state.

[smf\_set\_initial](group__smf.md#ga4389086c6aa3167e8c49226323ae208d)

void smf\_set\_initial(struct smf\_ctx \*ctx, const struct smf\_state \*init\_state)

Initializes the state machine and sets its initial state.

[smf\_run\_state](group__smf.md#ga8399cfa9e793a7f188b4ed4fec9f4f90)

int32\_t smf\_run\_state(struct smf\_ctx \*ctx)

Runs one iteration of a state machine (including any parent states).

[smf\_set\_handled](group__smf.md#gaa187bbd70434d29c319089faf50c2526)

void smf\_set\_handled(struct smf\_ctx \*ctx)

Tell the SMF to stop propagating the event to ancestors.

[smf\_set\_terminate](group__smf.md#gaae28c66f0652c99ba8e843eeaf02aaf7)

void smf\_set\_terminate(struct smf\_ctx \*ctx, int32\_t val)

Terminate a state machine.

[state\_execution](group__smf.md#gaff08e9a57d55107fd8d13ffe86295ca6)

void(\* state\_execution)(void \*obj)

Function pointer that implements a portion of a state.

**Definition** smf.h:63

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

**Definition** smf.h:99

[smf\_ctx::terminate\_val](structsmf__ctx.md#a1018c3dc6d7cc94ac2b64f95e5c053cd)

int32\_t terminate\_val

This value is set by the set\_terminate function and should terminate the state machine when its set t...

**Definition** smf.h:115

[smf\_ctx::previous](structsmf__ctx.md#a2cebcd02bfc6b36278c20fe8e0f95418)

const struct smf\_state \* previous

Previous state the state machine executed.

**Definition** smf.h:103

[smf\_ctx::current](structsmf__ctx.md#a48736dbfad38f0b25e4ab2a36d2f482a)

const struct smf\_state \* current

Current state the state machine is executing.

**Definition** smf.h:101

[smf\_ctx::internal](structsmf__ctx.md#afb094c0e87d42ec7ca780a2859be7bf8)

uint32\_t internal

The state machine casts this to a "struct internal\_ctx" and it's used to track state machine context.

**Definition** smf.h:120

[smf\_state](structsmf__state.md)

General state that can be used in multiple state machines.

**Definition** smf.h:66

[smf\_state::exit](structsmf__state.md#a2df810ca49fbb9438ee78317feaaf09b)

const state\_execution exit

Optional method that will be run when this state exists.

**Definition** smf.h:75

[smf\_state::entry](structsmf__state.md#a63ea395c90fa8118cf355e55e60cee26)

const state\_execution entry

Optional method that will be run when this state is entered.

**Definition** smf.h:68

[smf\_state::run](structsmf__state.md#a94adbcd4e1a8bce8f3b30082874f1911)

const state\_execution run

Optional method that will be run repeatedly during state machine loop.

**Definition** smf.h:73

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [smf.h](smf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
