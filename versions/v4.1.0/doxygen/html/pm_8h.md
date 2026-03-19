---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pm_8h.html
original_path: doxygen/html/pm_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pm.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/pm/state.h](state_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](pm_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pm\_notifier](structpm__notifier.md) |
|  | Power management notifier struct. [More...](structpm__notifier.md#details) |

| Functions | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_state\_force](group__subsys__pm__sys.md#ga075be307983f4efdcc93252a31a4258a) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu, const struct [pm\_state\_info](structpm__state__info.md) \*info) |
|  | Force usage of given power state. |
| void | [pm\_notifier\_register](group__subsys__pm__sys.md#ga066945118b8f287ee56aacf41b677a78) (struct [pm\_notifier](structpm__notifier.md) \*notifier) |
|  | Register a power management notifier. |
| int | [pm\_notifier\_unregister](group__subsys__pm__sys.md#gab0856d662e50a3847a1b70cb8370849a) (struct [pm\_notifier](structpm__notifier.md) \*notifier) |
|  | Unregister a power management notifier. |
| const struct [pm\_state\_info](structpm__state__info.md) \* | [pm\_state\_next\_get](group__subsys__pm__sys.md#ga3861a1a0009b96d15de00059257848dd) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu) |
|  | Gets the next power state that will be used. |
| void | [pm\_system\_resume](group__subsys__pm__sys.md#ga40a040996ab6746aa7714499b41d500e) (void) |
|  | Notify exit from kernel sleep. |
| void | [pm\_state\_set](group__subsys__pm__sys__hooks.md#gaa5c707f5c9c14494a388c6c2144e8f61) (enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) substate\_id) |
|  | Put processor into a power state. |
| void | [pm\_state\_exit\_post\_ops](group__subsys__pm__sys__hooks.md#ga7594e7e9b41c180ac760b7b0c47673b2) (enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) substate\_id) |
|  | Do any SoC or architecture specific post ops after sleep state exits. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [pm](dir_7e6ac69b960794fd0df7b746be7e9a24.md)
- [pm.h](pm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
