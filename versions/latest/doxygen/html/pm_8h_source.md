---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pm_8h_source.html
original_path: doxygen/html/pm_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pm.h

[Go to the documentation of this file.](pm_8h.md)

1/\*

2 \* Copyright (c) 2012-2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_PM\_PM\_H\_

8#define ZEPHYR\_INCLUDE\_PM\_PM\_H\_

9

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11#include <[zephyr/sys/slist.h](slist_8h.md)>

12#include <[zephyr/pm/state.h](state_8h.md)>

13#include <[zephyr/toolchain.h](toolchain_8h.md)>

14#include <[errno.h](errno_8h.md)>

15#include <[stdbool.h](stdbool_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

28

35

[ 54](structpm__notifier.md)struct [pm\_notifier](structpm__notifier.md) {

55 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

[ 60](structpm__notifier.md#ab84353bcc32f4262ea1a34f316d21278) void (\*[state\_entry](structpm__notifier.md#ab84353bcc32f4262ea1a34f316d21278))(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

[ 65](structpm__notifier.md#aeb6bcf67d2d4c5342d8d81cea3728ec5) void (\*[state\_exit](structpm__notifier.md#aeb6bcf67d2d4c5342d8d81cea3728ec5))(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

66};

67

68#if defined(CONFIG\_PM) || defined(\_\_DOXYGEN\_\_)

[ 81](group__subsys__pm__sys.md#ga075be307983f4efdcc93252a31a4258a)bool [pm\_state\_force](group__subsys__pm__sys.md#ga075be307983f4efdcc93252a31a4258a)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu, const struct [pm\_state\_info](structpm__state__info.md) \*info);

82

[ 91](group__subsys__pm__sys.md#ga066945118b8f287ee56aacf41b677a78)void [pm\_notifier\_register](group__subsys__pm__sys.md#ga066945118b8f287ee56aacf41b677a78)(struct [pm\_notifier](structpm__notifier.md) \*notifier);

92

[ 104](group__subsys__pm__sys.md#gab0856d662e50a3847a1b70cb8370849a)int [pm\_notifier\_unregister](group__subsys__pm__sys.md#gab0856d662e50a3847a1b70cb8370849a)(struct [pm\_notifier](structpm__notifier.md) \*notifier);

105

[ 115](group__subsys__pm__sys.md#ga3861a1a0009b96d15de00059257848dd)const struct [pm\_state\_info](structpm__state__info.md) \*[pm\_state\_next\_get](group__subsys__pm__sys.md#ga3861a1a0009b96d15de00059257848dd)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu);

116

120

127

[ 137](group__subsys__pm__sys__hooks.md#gaa5c707f5c9c14494a388c6c2144e8f61)void [pm\_state\_set](group__subsys__pm__sys__hooks.md#gaa5c707f5c9c14494a388c6c2144e8f61)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

138

[ 150](group__subsys__pm__sys__hooks.md#ga7594e7e9b41c180ac760b7b0c47673b2)void [pm\_state\_exit\_post\_ops](group__subsys__pm__sys__hooks.md#ga7594e7e9b41c180ac760b7b0c47673b2)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

151

155

156#else /\* CONFIG\_PM \*/

157

158static inline void [pm\_notifier\_register](group__subsys__pm__sys.md#ga066945118b8f287ee56aacf41b677a78)(struct [pm\_notifier](structpm__notifier.md) \*notifier)

159{

160 ARG\_UNUSED(notifier);

161}

162

163static inline int [pm\_notifier\_unregister](group__subsys__pm__sys.md#gab0856d662e50a3847a1b70cb8370849a)(struct [pm\_notifier](structpm__notifier.md) \*notifier)

164{

165 ARG\_UNUSED(notifier);

166

167 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

168}

169

170static inline const struct [pm\_state\_info](structpm__state__info.md) \*[pm\_state\_next\_get](group__subsys__pm__sys.md#ga3861a1a0009b96d15de00059257848dd)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu)

171{

172 ARG\_UNUSED(cpu);

173

174 return NULL;

175}

176#endif /\* CONFIG\_PM \*/

177

178void z\_pm\_save\_idle\_exit(void);

179

180#ifdef \_\_cplusplus

181}

182#endif

183

184#endif /\* ZEPHYR\_INCLUDE\_PM\_PM\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5)

pm\_state

Power management state.

**Definition** state.h:27

[pm\_state\_exit\_post\_ops](group__subsys__pm__sys__hooks.md#ga7594e7e9b41c180ac760b7b0c47673b2)

void pm\_state\_exit\_post\_ops(enum pm\_state state, uint8\_t substate\_id)

Do any SoC or architecture specific post ops after sleep state exits.

[pm\_state\_set](group__subsys__pm__sys__hooks.md#gaa5c707f5c9c14494a388c6c2144e8f61)

void pm\_state\_set(enum pm\_state state, uint8\_t substate\_id)

Put processor into a power state.

[pm\_notifier\_register](group__subsys__pm__sys.md#ga066945118b8f287ee56aacf41b677a78)

void pm\_notifier\_register(struct pm\_notifier \*notifier)

Register a power management notifier.

[pm\_state\_force](group__subsys__pm__sys.md#ga075be307983f4efdcc93252a31a4258a)

bool pm\_state\_force(uint8\_t cpu, const struct pm\_state\_info \*info)

Force usage of given power state.

[pm\_state\_next\_get](group__subsys__pm__sys.md#ga3861a1a0009b96d15de00059257848dd)

const struct pm\_state\_info \* pm\_state\_next\_get(uint8\_t cpu)

Gets the next power state that will be used.

[pm\_notifier\_unregister](group__subsys__pm__sys.md#gab0856d662e50a3847a1b70cb8370849a)

int pm\_notifier\_unregister(struct pm\_notifier \*notifier)

Unregister a power management notifier.

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[types.h](include_2zephyr_2types_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[slist.h](slist_8h.md)

[state.h](state_8h.md)

[stdbool.h](stdbool_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[pm\_notifier](structpm__notifier.md)

Power management notifier struct.

**Definition** pm.h:54

[pm\_notifier::state\_entry](structpm__notifier.md#ab84353bcc32f4262ea1a34f316d21278)

void(\* state\_entry)(enum pm\_state state)

Application defined function for doing any target specific operations for power state entry.

**Definition** pm.h:60

[pm\_notifier::state\_exit](structpm__notifier.md#aeb6bcf67d2d4c5342d8d81cea3728ec5)

void(\* state\_exit)(enum pm\_state state)

Application defined function for doing any target specific operations for power state exit.

**Definition** pm.h:65

[pm\_state\_info](structpm__state__info.md)

Information about a power management state.

**Definition** state.h:114

[pm\_state\_info::substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445)

uint8\_t substate\_id

Some platforms have multiple states that map to one Zephyr power state.

**Definition** state.h:141

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [pm](dir_7e6ac69b960794fd0df7b746be7e9a24.md)
- [pm.h](pm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
