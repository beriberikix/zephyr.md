---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structs__preempFloatReg.html
original_path: doxygen/html/structs__preempFloatReg.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

s\_preempFloatReg Struct Reference

`#include <[thread.h](arch_2x86_2ia32_2thread_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [tFpRegSet](arch_2x86_2ia32_2thread_8h.md#ac6b7d0ab9f5986eb129f362e4dc39811)   [fpRegs](#a4acaff08c1a51294d7c45e1144491d86) |  |
| [tFpRegSetEx](arch_2x86_2ia32_2thread_8h.md#a9b38503997978c6dbfdb03448cb38967)   [fpRegsEx](#a295615b119006e286338175dcb2d2944) |  |
| } | [floatRegsUnion](#a0974de9441844c906da4b91278ac1d5f) |

## Field Documentation

## [◆ ](#a0974de9441844c906da4b91278ac1d5f)[union]

| union { ... } s\_preempFloatReg::floatRegsUnion |
| --- |

## [◆ ](#a4acaff08c1a51294d7c45e1144491d86)fpRegs

| [tFpRegSet](arch_2x86_2ia32_2thread_8h.md#ac6b7d0ab9f5986eb129f362e4dc39811) s\_preempFloatReg::fpRegs |
| --- |

## [◆ ](#a295615b119006e286338175dcb2d2944)fpRegsEx

| [tFpRegSetEx](arch_2x86_2ia32_2thread_8h.md#a9b38503997978c6dbfdb03448cb38967) s\_preempFloatReg::fpRegsEx |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/arch/x86/ia32/[thread.h](arch_2x86_2ia32_2thread_8h_source.md)

- [s\_preempFloatReg](structs__preempFloatReg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
