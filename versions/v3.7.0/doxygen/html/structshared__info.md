---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structshared__info.html
original_path: doxygen/html/structshared__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shared\_info Struct Reference

`#include <[xen.h](xen_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [vcpu\_info](structvcpu__info.md) | [vcpu\_info](#ac2546d512495d021e8e22d3eae260153) [[XEN\_LEGACY\_MAX\_VCPUS](arch-arm_8h.md#a57246b966cc182f34ca4f9bfa101e449)] |
| [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) | [evtchn\_pending](#a7911652d7ce578705e852d4518d1abb9) [[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)) \*8] |
| [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) | [evtchn\_mask](#a45398e8bb0df581eedb48cd9902f811d) [[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)) \*8] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [wc\_version](#aca3778d0bbd570d4ced2634b4da8a046) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [wc\_sec](#a29cb80aa1a44985e5a84b4dcaf035708) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [wc\_nsec](#a29699e4b3d1953edfc3d836d5f582cf0) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [wc\_sec\_hi](#a22add85abac7eae2240a9ef088772b15) |
| struct [arch\_shared\_info](structarch__shared__info.md) | [arch](#a4eab2a6ca5ab006c3d3d0cd938dfa7f7) |

## Field Documentation

## [◆ ](#a4eab2a6ca5ab006c3d3d0cd938dfa7f7)arch

| struct [arch\_shared\_info](structarch__shared__info.md) shared\_info::arch |
| --- |

## [◆ ](#a45398e8bb0df581eedb48cd9902f811d)evtchn\_mask

| [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) shared\_info::evtchn\_mask[[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)) \*8] |
| --- |

## [◆ ](#a7911652d7ce578705e852d4518d1abb9)evtchn\_pending

| [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) shared\_info::evtchn\_pending[[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)) \*8] |
| --- |

## [◆ ](#ac2546d512495d021e8e22d3eae260153)vcpu\_info

| struct [vcpu\_info](structvcpu__info.md) shared\_info::vcpu\_info[[XEN\_LEGACY\_MAX\_VCPUS](arch-arm_8h.md#a57246b966cc182f34ca4f9bfa101e449)] |
| --- |

## [◆ ](#a29699e4b3d1953edfc3d836d5f582cf0)wc\_nsec

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shared\_info::wc\_nsec |
| --- |

## [◆ ](#a29cb80aa1a44985e5a84b4dcaf035708)wc\_sec

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shared\_info::wc\_sec |
| --- |

## [◆ ](#a22add85abac7eae2240a9ef088772b15)wc\_sec\_hi

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shared\_info::wc\_sec\_hi |
| --- |

## [◆ ](#aca3778d0bbd570d4ced2634b4da8a046)wc\_version

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shared\_info::wc\_version |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[xen.h](xen_8h_source.md)

- [shared\_info](structshared__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
