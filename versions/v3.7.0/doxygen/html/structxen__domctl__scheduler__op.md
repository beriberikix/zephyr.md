---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structxen__domctl__scheduler__op.html
original_path: doxygen/html/structxen__domctl__scheduler__op.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xen\_domctl\_scheduler\_op Struct Reference

`#include <[domctl.h](public_2domctl_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sched\_id](#ac6898bc19fb03bce4728a1f682eb5877) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cmd](#a535dd489e0c9d75e5f87f71530b51d62) |
| union { |  |
| struct [xen\_domctl\_sched\_credit](structxen__domctl__sched__credit.md)   [credit](#aeac8bec25228d32e9cc2dcc191e30372) |  |
| struct [xen\_domctl\_sched\_credit2](structxen__domctl__sched__credit2.md)   [credit2](#afee50150bdab7f4ade33e080a94f58db) |  |
| struct [xen\_domctl\_sched\_rtds](structxen__domctl__sched__rtds.md)   [rtds](#a051aaadadd7a56d0af51f936e8c889e0) |  |
| struct { |  |
| [vcpus](#a5b09041b6658123c57952356b985daf9) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [nr\_vcpus](#ac761b945a1e0f4331f547ea3a8ef44d9) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [padding](#accc76316cedabc895ea519d567d29f74) |  |
| }   [v](#a1865ada180f42b79c77d6cb2d3b66ddc) |
| } | [u](#a9fd7a528fb9673c55e6eb34fa939c9be) |

## Field Documentation

## [◆ ](#a535dd489e0c9d75e5f87f71530b51d62)cmd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_scheduler\_op::cmd |
| --- |

## [◆ ](#aeac8bec25228d32e9cc2dcc191e30372)credit

| struct [xen\_domctl\_sched\_credit](structxen__domctl__sched__credit.md) xen\_domctl\_scheduler\_op::credit |
| --- |

## [◆ ](#afee50150bdab7f4ade33e080a94f58db)credit2

| struct [xen\_domctl\_sched\_credit2](structxen__domctl__sched__credit2.md) xen\_domctl\_scheduler\_op::credit2 |
| --- |

## [◆ ](#ac761b945a1e0f4331f547ea3a8ef44d9)nr\_vcpus

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_scheduler\_op::nr\_vcpus |
| --- |

## [◆ ](#accc76316cedabc895ea519d567d29f74)padding

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_scheduler\_op::padding |
| --- |

## [◆ ](#a051aaadadd7a56d0af51f936e8c889e0)rtds

| struct [xen\_domctl\_sched\_rtds](structxen__domctl__sched__rtds.md) xen\_domctl\_scheduler\_op::rtds |
| --- |

## [◆ ](#ac6898bc19fb03bce4728a1f682eb5877)sched\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_scheduler\_op::sched\_id |
| --- |

## [◆ ](#a9fd7a528fb9673c55e6eb34fa939c9be)[union]

| union { ... } xen\_domctl\_scheduler\_op::u |
| --- |

## [◆ ](#a1865ada180f42b79c77d6cb2d3b66ddc)[struct]

| struct { ... } xen\_domctl\_scheduler\_op::v |
| --- |

## [◆ ](#a5b09041b6658123c57952356b985daf9)vcpus

| xen\_domctl\_scheduler\_op::vcpus |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[domctl.h](public_2domctl_8h_source.md)

- [xen\_domctl\_scheduler\_op](structxen__domctl__scheduler__op.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
