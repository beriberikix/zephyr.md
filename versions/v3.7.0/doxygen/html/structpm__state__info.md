---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structpm__state__info.html
original_path: doxygen/html/structpm__state__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pm\_state\_info Struct Reference

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md) » [States](group__subsys__pm__states.md)

Information about a power management state.
[More...](#details)

`#include <[state.h](state_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) | [state](#aed57fc8a935951aa2687614b954c7225) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [substate\_id](#a422bc0c9aedc107dbfa57c3ac8eb2445) |
|  | Some platforms have multiple states that map to one Zephyr power state. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_disabled](#ac0a5ee091648225ba25ea34c75163814) |
|  | Whether or not this state triggers device power management. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [min\_residency\_us](#a442654715d3872de1b7b0dcf08bffb8b) |
|  | Minimum residency duration in microseconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [exit\_latency\_us](#a6fc8e0a78df78c7a28a0bc2a27292818) |
|  | Worst case latency in microseconds required to exit the idle state. |

## Detailed Description

Information about a power management state.

## Field Documentation

## [◆ ](#a6fc8e0a78df78c7a28a0bc2a27292818)exit\_latency\_us

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pm\_state\_info::exit\_latency\_us |
| --- |

Worst case latency in microseconds required to exit the idle state.

Note
:   0 means that this property is not available for this state.

## [◆ ](#a442654715d3872de1b7b0dcf08bffb8b)min\_residency\_us

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pm\_state\_info::min\_residency\_us |
| --- |

Minimum residency duration in microseconds.

It is the minimum time for a given idle state to be worthwhile energywise.

Note
:   0 means that this property is not available for this state.

## [◆ ](#ac0a5ee091648225ba25ea34c75163814)pm\_device\_disabled

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pm\_state\_info::pm\_device\_disabled |
| --- |

Whether or not this state triggers device power management.

When this property is false the power management subsystem will suspend devices before entering this state and will properly resume them when leaving it.

## [◆ ](#aed57fc8a935951aa2687614b954c7225)state

| enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) pm\_state\_info::state |
| --- |

## [◆ ](#a422bc0c9aedc107dbfa57c3ac8eb2445)substate\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pm\_state\_info::substate\_id |
| --- |

Some platforms have multiple states that map to one Zephyr power state.

This property allows the platform distinguish them. e.g:

power-states {

state0: state0 {

compatible = "zephyr,power-state";

power-state-name = "suspend-to-idle";

substate-id = <1>;

min-residency-us = <10000>;

exit-latency-us = <100>;

};

state1: state1 {

compatible = "zephyr,power-state";

power-state-name = "suspend-to-idle";

substate-id = <2>;

min-residency-us = <20000>;

exit-latency-us = <200>;

zephyr,pm-device-disabled;

};

};

---

The documentation for this struct was generated from the following file:

- zephyr/pm/[state.h](state_8h_source.md)

- [pm\_state\_info](structpm__state__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
