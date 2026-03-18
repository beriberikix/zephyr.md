---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structxen__domctl__schedparam__vcpu.html
original_path: doxygen/html/structxen__domctl__schedparam__vcpu.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xen\_domctl\_schedparam\_vcpu Struct Reference

`#include <[domctl.h](public_2domctl_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct [xen\_domctl\_sched\_credit](structxen__domctl__sched__credit.md)   [credit](#a17a024fce3c2e1b51e56ddae4928d253) |  |
| struct [xen\_domctl\_sched\_credit2](structxen__domctl__sched__credit2.md)   [credit2](#a96e8bf39fabec20d86f4caa2a47f8114) |  |
| struct [xen\_domctl\_sched\_rtds](structxen__domctl__sched__rtds.md)   [rtds](#a15fe4501207b8198b5a87591112d9a48) |  |
| } | [u](#a0c6818fb83e36a05c2eebad138206cd3) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [vcpuid](#a063292bc431df3f1677cfd27a3a788f5) |

## Field Documentation

## [◆ ](#a17a024fce3c2e1b51e56ddae4928d253)credit

| struct [xen\_domctl\_sched\_credit](structxen__domctl__sched__credit.md) xen\_domctl\_schedparam\_vcpu::credit |
| --- |

## [◆ ](#a96e8bf39fabec20d86f4caa2a47f8114)credit2

| struct [xen\_domctl\_sched\_credit2](structxen__domctl__sched__credit2.md) xen\_domctl\_schedparam\_vcpu::credit2 |
| --- |

## [◆ ](#a15fe4501207b8198b5a87591112d9a48)rtds

| struct [xen\_domctl\_sched\_rtds](structxen__domctl__sched__rtds.md) xen\_domctl\_schedparam\_vcpu::rtds |
| --- |

## [◆ ](#a0c6818fb83e36a05c2eebad138206cd3)[union]

| union { ... } xen\_domctl\_schedparam\_vcpu::u |
| --- |

## [◆ ](#a063292bc431df3f1677cfd27a3a788f5)vcpuid

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_schedparam\_vcpu::vcpuid |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[domctl.h](public_2domctl_8h_source.md)

- [xen\_domctl\_schedparam\_vcpu](structxen__domctl__schedparam__vcpu.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
