---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/policy_8h.html
original_path: doxygen/html/policy_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

policy.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/pm/state.h](state_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](policy_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) |
|  | Latency change subscription. [More...](structpm__policy__latency__subscription.md#details) |
| struct | [pm\_policy\_latency\_request](structpm__policy__latency__request.md) |
|  | Latency request. [More...](structpm__policy__latency__request.md#details) |
| struct | [pm\_policy\_event](structpm__policy__event.md) |
|  | Event. [More...](structpm__policy__event.md#details) |

| Macros | |
| --- | --- |
| #define | [PM\_ALL\_SUBSTATES](group__subsys__pm__sys__policy.md#gab241e40f9282a1c8ebc602997fbb3190)   ([UINT8\_MAX](stdint_8h.md#aeb4e270a084ee26fe73e799861bd0252)) |
|  | Special value for 'all substates'. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [pm\_policy\_latency\_changed\_cb\_t](group__subsys__pm__sys__policy.md#gab2a0a73416b3fcb535fa54a1f3b4c267)) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) latency) |
|  | Callback to notify when maximum latency changes. |

| Functions | |
| --- | --- |
| void | [pm\_policy\_state\_lock\_get](group__subsys__pm__sys__policy.md#gabbb379f8572f164addafe93ad3468f3d) (enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) substate\_id) |
|  | Increase a power state lock counter. |
| void | [pm\_policy\_state\_lock\_put](group__subsys__pm__sys__policy.md#ga12f4d121aa8be0eb66381713b481a8b1) (enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) substate\_id) |
|  | Decrease a power state lock counter. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_policy\_state\_lock\_is\_active](group__subsys__pm__sys__policy.md#ga39f14c8509dee55ed084b4111584b766) (enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) substate\_id) |
|  | Check if a power state lock is active (not allowed). |
| void | [pm\_policy\_latency\_request\_add](group__subsys__pm__sys__policy.md#ga848627f6d143ece582711a16cab5442a) (struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us) |
|  | Add a new latency requirement. |
| void | [pm\_policy\_latency\_request\_update](group__subsys__pm__sys__policy.md#ga6483bd320881d697de27493b4f2d92d1) (struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us) |
|  | Update a latency requirement. |
| void | [pm\_policy\_latency\_request\_remove](group__subsys__pm__sys__policy.md#gaadcb851b1bfb312ea0960918dc9f869e) (struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req) |
|  | Remove a latency requirement. |
| void | [pm\_policy\_latency\_changed\_subscribe](group__subsys__pm__sys__policy.md#gacf77adf6eaf5258e03ce1923d685ed3b) (struct [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) \*req, [pm\_policy\_latency\_changed\_cb\_t](group__subsys__pm__sys__policy.md#gab2a0a73416b3fcb535fa54a1f3b4c267) cb) |
|  | Subscribe to maximum latency changes. |
| void | [pm\_policy\_latency\_changed\_unsubscribe](group__subsys__pm__sys__policy.md#ga8ca62cfeef8d4ebb58800e3ac6b645ee) (struct [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) \*req) |
|  | Unsubscribe to maximum latency changes. |
| void | [pm\_policy\_event\_register](group__subsys__pm__sys__policy.md#gafab2e1484a58131a9c7cefd2b9adb3e9) (struct [pm\_policy\_event](structpm__policy__event.md) \*evt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_us) |
|  | Register an event. |
| void | [pm\_policy\_event\_update](group__subsys__pm__sys__policy.md#ga1d6d278768ed961c3856119de2fbb74b) (struct [pm\_policy\_event](structpm__policy__event.md) \*evt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_us) |
|  | Update an event. |
| void | [pm\_policy\_event\_unregister](group__subsys__pm__sys__policy.md#ga9448e31e1bd1a8b02defe6d1427197ff) (struct [pm\_policy\_event](structpm__policy__event.md) \*evt) |
|  | Unregister an event. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [pm](dir_7e6ac69b960794fd0df7b746be7e9a24.md)
- [policy.h](policy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
