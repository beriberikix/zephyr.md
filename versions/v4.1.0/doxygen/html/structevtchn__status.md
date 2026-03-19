---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structevtchn__status.html
original_path: doxygen/html/structevtchn__status.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

evtchn\_status Struct Reference

`#include <[event_channel.h](event__channel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) | [dom](#ab2af6d86b1121d78bcd44a7deab22429) |
| [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) | [port](#a371c715eff52f12ecc45b8c0396724a2) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [status](#a366e123cce2040e4a9c098b893647077) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [vcpu](#a73b3355dc9a49f0f463944c963d9c99a) |
| union { |  |
| struct { |  |
| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee)   [dom](#ab2af6d86b1121d78bcd44a7deab22429) |  |
| }   [unbound](#a450e072e1a3e19b118c77f28296b16af) |
| struct { |  |
| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee)   [dom](#ab2af6d86b1121d78bcd44a7deab22429) |  |
| [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f)   [port](#a371c715eff52f12ecc45b8c0396724a2) |  |
| }   [interdomain](#afa5fef85870db40407579ae3d4a0a021) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [pirq](#abbb84f973ee49ddab13783de648cb382) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [virq](#acd976827543c4192186f68da8f8be701) |  |
| } | [u](#a332ac0bb8666e0e1d8a0ae015cdcacc6) |

## Field Documentation

## [◆ ](#ab2af6d86b1121d78bcd44a7deab22429)dom

| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) evtchn\_status::dom |
| --- |

## [◆ ](#afa5fef85870db40407579ae3d4a0a021)[struct]

| struct { ... } evtchn\_status::interdomain |
| --- |

## [◆ ](#abbb84f973ee49ddab13783de648cb382)pirq

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) evtchn\_status::pirq |
| --- |

## [◆ ](#a371c715eff52f12ecc45b8c0396724a2)port

| [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) evtchn\_status::port |
| --- |

## [◆ ](#a366e123cce2040e4a9c098b893647077)status

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) evtchn\_status::status |
| --- |

## [◆ ](#a332ac0bb8666e0e1d8a0ae015cdcacc6)[union]

| union { ... } evtchn\_status::u |
| --- |

## [◆ ](#a450e072e1a3e19b118c77f28296b16af)[struct]

| struct { ... } evtchn\_status::unbound |
| --- |

## [◆ ](#a73b3355dc9a49f0f463944c963d9c99a)vcpu

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) evtchn\_status::vcpu |
| --- |

## [◆ ](#acd976827543c4192186f68da8f8be701)virq

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) evtchn\_status::virq |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[event\_channel.h](event__channel_8h_source.md)

- [evtchn\_status](structevtchn__status.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
