---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/event__channel_8h.html
original_path: doxygen/html/event__channel_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

event\_channel.h File Reference

`#include "[xen.h](xen_8h_source.md)"`

[Go to the source code of this file.](event__channel_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [evtchn\_alloc\_unbound](structevtchn__alloc__unbound.md) |
| struct | [evtchn\_bind\_interdomain](structevtchn__bind__interdomain.md) |
| struct | [evtchn\_close](structevtchn__close.md) |
| struct | [evtchn\_send](structevtchn__send.md) |
| struct | [evtchn\_status](structevtchn__status.md) |
| struct | [evtchn\_unmask](structevtchn__unmask.md) |
| struct | [evtchn\_reset](structevtchn__reset.md) |
| struct | [evtchn\_set\_priority](structevtchn__set__priority.md) |

| Macros | |
| --- | --- |
| #define | [EVTCHNOP\_bind\_interdomain](#a3483f93d8b78e60ec7856e2a4ee57304)   0 |
| #define | [EVTCHNOP\_bind\_virq](#a795dc96341925d710075030e45f65750)   1 |
| #define | [EVTCHNOP\_bind\_pirq](#a42a0680c05b55a0447e0f6bdb1805cf3)   2 |
| #define | [EVTCHNOP\_close](#a078653022bf42296dfe21769e4b9c1f0)   3 |
| #define | [EVTCHNOP\_send](#a59f6c29f7ef47d003f192d1c8fc9676a)   4 |
| #define | [EVTCHNOP\_status](#aa1ba0fec605174cae49dbe4d7d33ffcd)   5 |
| #define | [EVTCHNOP\_alloc\_unbound](#a688357b79034d6c9cadc9fde62716e67)   6 |
| #define | [EVTCHNOP\_bind\_ipi](#a547b2ee658a9ebaeb38e732da7241575)   7 |
| #define | [EVTCHNOP\_bind\_vcpu](#a8677a6dccd99efb40a218e0affeee20f)   8 |
| #define | [EVTCHNOP\_unmask](#a56d70d3fcc8ed685a3282aea1715df56)   9 |
| #define | [EVTCHNOP\_reset](#aa055408833212f615860a0d839f9e749)   10 |
| #define | [EVTCHNOP\_init\_control](#ac27259ea173feb1bdf032f2e5f7d9b24)   11 |
| #define | [EVTCHNOP\_expand\_array](#ae3638932df91767358c8b1258ee8a14a)   12 |
| #define | [EVTCHNOP\_set\_priority](#a2aff242f251d2ac6a3f1d65e10e5d4e0)   13 |
| #define | [EVTCHNSTAT\_closed](#a783b78a1ff275d6b2dfa9592bcfebdbc)   0 /\* Channel is not in use. \*/ |
| #define | [EVTCHNSTAT\_unbound](#aaf73995f43bc61feecd6ab6d77255b7c)   1 /\* Channel is waiting interdom connection.\*/ |
| #define | [EVTCHNSTAT\_interdomain](#a556deda7942e60afce2f039f93899c5f)   2 /\* Channel is connected to remote domain. \*/ |
| #define | [EVTCHNSTAT\_pirq](#aec1a18deba5a52f84abac495cb2ef698)   3 /\* Channel is bound to a phys IRQ line. \*/ |
| #define | [EVTCHNSTAT\_virq](#ac2db0aaa42a834598a9efaf22e59c7e3)   4 /\* Channel is bound to a virtual IRQ line \*/ |
| #define | [EVTCHNSTAT\_ipi](#a7214c690ed8bbfd4d68f4c1b44d9ce92)   5 /\* Channel is bound to a virtual IPI line \*/ |
| #define | [EVTCHN\_2L\_NR\_CHANNELS](#acdcf92372fa5ac60b219cd5e34d82fdf)   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)) \* [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)) \* 64) |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [evtchn\_port\_t](#aaad5124a66f37437561260d1170ab33f) |
| typedef struct [evtchn\_alloc\_unbound](structevtchn__alloc__unbound.md) | [evtchn\_alloc\_unbound\_t](#a2f53913488e4b1105b164c429ef21bac) |
| typedef struct [evtchn\_bind\_interdomain](structevtchn__bind__interdomain.md) | [evtchn\_bind\_interdomain\_t](#ac758af7badcae4377a5df682ff4ea248) |
| typedef struct [evtchn\_close](structevtchn__close.md) | [evtchn\_close\_t](#ad19c601c41adcd9e235695073e11fa31) |
| typedef struct [evtchn\_send](structevtchn__send.md) | [evtchn\_send\_t](#a7c4630750087f7f7586488f49cd55d4e) |
| typedef struct [evtchn\_status](structevtchn__status.md) | [evtchn\_status\_t](#a8ed9ed5019e8da76a67eaddc44c3f6a9) |
| typedef struct [evtchn\_unmask](structevtchn__unmask.md) | [evtchn\_unmask\_t](#adf108a8c569745708da92551dcad289c) |
| typedef struct [evtchn\_reset](structevtchn__reset.md) | [evtchn\_reset\_t](#a6338f2371d708c16d85dcabfe88ebffb) |
| typedef struct [evtchn\_set\_priority](structevtchn__set__priority.md) | [evtchn\_set\_priority\_t](#a497a6a153a0f6152a9c33686d4601a3b) |

| Functions | |
| --- | --- |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#afc32a45a04eafa1b7f1ddae5231ac694) ([evtchn\_port\_t](#aaad5124a66f37437561260d1170ab33f)) |

## Macro Definition Documentation

## [◆ ](#acdcf92372fa5ac60b219cd5e34d82fdf)EVTCHN\_2L\_NR\_CHANNELS

| #define EVTCHN\_2L\_NR\_CHANNELS   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)) \* [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)) \* 64) |
| --- |

## [◆ ](#a688357b79034d6c9cadc9fde62716e67)EVTCHNOP\_alloc\_unbound

| #define EVTCHNOP\_alloc\_unbound   6 |
| --- |

## [◆ ](#a3483f93d8b78e60ec7856e2a4ee57304)EVTCHNOP\_bind\_interdomain

| #define EVTCHNOP\_bind\_interdomain   0 |
| --- |

## [◆ ](#a547b2ee658a9ebaeb38e732da7241575)EVTCHNOP\_bind\_ipi

| #define EVTCHNOP\_bind\_ipi   7 |
| --- |

## [◆ ](#a42a0680c05b55a0447e0f6bdb1805cf3)EVTCHNOP\_bind\_pirq

| #define EVTCHNOP\_bind\_pirq   2 |
| --- |

## [◆ ](#a8677a6dccd99efb40a218e0affeee20f)EVTCHNOP\_bind\_vcpu

| #define EVTCHNOP\_bind\_vcpu   8 |
| --- |

## [◆ ](#a795dc96341925d710075030e45f65750)EVTCHNOP\_bind\_virq

| #define EVTCHNOP\_bind\_virq   1 |
| --- |

## [◆ ](#a078653022bf42296dfe21769e4b9c1f0)EVTCHNOP\_close

| #define EVTCHNOP\_close   3 |
| --- |

## [◆ ](#ae3638932df91767358c8b1258ee8a14a)EVTCHNOP\_expand\_array

| #define EVTCHNOP\_expand\_array   12 |
| --- |

## [◆ ](#ac27259ea173feb1bdf032f2e5f7d9b24)EVTCHNOP\_init\_control

| #define EVTCHNOP\_init\_control   11 |
| --- |

## [◆ ](#aa055408833212f615860a0d839f9e749)EVTCHNOP\_reset

| #define EVTCHNOP\_reset   10 |
| --- |

## [◆ ](#a59f6c29f7ef47d003f192d1c8fc9676a)EVTCHNOP\_send

| #define EVTCHNOP\_send   4 |
| --- |

## [◆ ](#a2aff242f251d2ac6a3f1d65e10e5d4e0)EVTCHNOP\_set\_priority

| #define EVTCHNOP\_set\_priority   13 |
| --- |

## [◆ ](#aa1ba0fec605174cae49dbe4d7d33ffcd)EVTCHNOP\_status

| #define EVTCHNOP\_status   5 |
| --- |

## [◆ ](#a56d70d3fcc8ed685a3282aea1715df56)EVTCHNOP\_unmask

| #define EVTCHNOP\_unmask   9 |
| --- |

## [◆ ](#a783b78a1ff275d6b2dfa9592bcfebdbc)EVTCHNSTAT\_closed

| #define EVTCHNSTAT\_closed   0 /\* Channel is not in use. \*/ |
| --- |

## [◆ ](#a556deda7942e60afce2f039f93899c5f)EVTCHNSTAT\_interdomain

| #define EVTCHNSTAT\_interdomain   2 /\* Channel is connected to remote domain. \*/ |
| --- |

## [◆ ](#a7214c690ed8bbfd4d68f4c1b44d9ce92)EVTCHNSTAT\_ipi

| #define EVTCHNSTAT\_ipi   5 /\* Channel is bound to a virtual IPI line \*/ |
| --- |

## [◆ ](#aec1a18deba5a52f84abac495cb2ef698)EVTCHNSTAT\_pirq

| #define EVTCHNSTAT\_pirq   3 /\* Channel is bound to a phys IRQ line. \*/ |
| --- |

## [◆ ](#aaf73995f43bc61feecd6ab6d77255b7c)EVTCHNSTAT\_unbound

| #define EVTCHNSTAT\_unbound   1 /\* Channel is waiting interdom connection.\*/ |
| --- |

## [◆ ](#ac2db0aaa42a834598a9efaf22e59c7e3)EVTCHNSTAT\_virq

| #define EVTCHNSTAT\_virq   4 /\* Channel is bound to a virtual IRQ line \*/ |
| --- |

## Typedef Documentation

## [◆ ](#a2f53913488e4b1105b164c429ef21bac)evtchn\_alloc\_unbound\_t

| typedef struct [evtchn\_alloc\_unbound](structevtchn__alloc__unbound.md) [evtchn\_alloc\_unbound\_t](#a2f53913488e4b1105b164c429ef21bac) |
| --- |

## [◆ ](#ac758af7badcae4377a5df682ff4ea248)evtchn\_bind\_interdomain\_t

| typedef struct [evtchn\_bind\_interdomain](structevtchn__bind__interdomain.md) [evtchn\_bind\_interdomain\_t](#ac758af7badcae4377a5df682ff4ea248) |
| --- |

## [◆ ](#ad19c601c41adcd9e235695073e11fa31)evtchn\_close\_t

| typedef struct [evtchn\_close](structevtchn__close.md) [evtchn\_close\_t](#ad19c601c41adcd9e235695073e11fa31) |
| --- |

## [◆ ](#aaad5124a66f37437561260d1170ab33f)evtchn\_port\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [evtchn\_port\_t](#aaad5124a66f37437561260d1170ab33f) |
| --- |

## [◆ ](#a6338f2371d708c16d85dcabfe88ebffb)evtchn\_reset\_t

| typedef struct [evtchn\_reset](structevtchn__reset.md) [evtchn\_reset\_t](#a6338f2371d708c16d85dcabfe88ebffb) |
| --- |

## [◆ ](#a7c4630750087f7f7586488f49cd55d4e)evtchn\_send\_t

| typedef struct [evtchn\_send](structevtchn__send.md) [evtchn\_send\_t](#a7c4630750087f7f7586488f49cd55d4e) |
| --- |

## [◆ ](#a497a6a153a0f6152a9c33686d4601a3b)evtchn\_set\_priority\_t

| typedef struct [evtchn\_set\_priority](structevtchn__set__priority.md) [evtchn\_set\_priority\_t](#a497a6a153a0f6152a9c33686d4601a3b) |
| --- |

## [◆ ](#a8ed9ed5019e8da76a67eaddc44c3f6a9)evtchn\_status\_t

| typedef struct [evtchn\_status](structevtchn__status.md) [evtchn\_status\_t](#a8ed9ed5019e8da76a67eaddc44c3f6a9) |
| --- |

## [◆ ](#adf108a8c569745708da92551dcad289c)evtchn\_unmask\_t

| typedef struct [evtchn\_unmask](structevtchn__unmask.md) [evtchn\_unmask\_t](#adf108a8c569745708da92551dcad289c) |
| --- |

## Function Documentation

## [◆ ](#afc32a45a04eafa1b7f1ddae5231ac694)DEFINE\_XEN\_GUEST\_HANDLE()

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [evtchn\_port\_t](#aaad5124a66f37437561260d1170ab33f) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [event\_channel.h](event__channel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
