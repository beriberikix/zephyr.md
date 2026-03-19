---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnpf__rule.html
original_path: doxygen/html/structnpf__rule.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npf\_rule Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Packet Filter API](group__net__pkt__filter.md)

filter rule structure
[More...](#details)

`#include <[net_pkt_filter.h](net__pkt__filter_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#ad5ae58fbcee5112e2defde1d7f4320dc) |
|  | Slist rule list node. |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) | [result](#a872daf53310dd8e20477eafd6808481f) |
|  | result if all tests pass |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nb\_tests](#a06045c693cf06e6ebfc5a74b8c3f5ef7) |
|  | number of tests for this rule |
| struct [npf\_test](structnpf__test.md) \* | [tests](#a72c032c55535c82f365b2cd1229cb1e0) [] |
|  | pointers to [npf\_test](structnpf__test.md "npf_test") instances |

## Detailed Description

filter rule structure

## Field Documentation

## [◆ ](#a06045c693cf06e6ebfc5a74b8c3f5ef7)nb\_tests

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) npf\_rule::nb\_tests |
| --- |

number of tests for this rule

## [◆ ](#ad5ae58fbcee5112e2defde1d7f4320dc)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) npf\_rule::node |
| --- |

Slist rule list node.

## [◆ ](#a872daf53310dd8e20477eafd6808481f)result

| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) npf\_rule::result |
| --- |

result if all tests pass

## [◆ ](#a72c032c55535c82f365b2cd1229cb1e0)tests

| struct [npf\_test](structnpf__test.md)\* npf\_rule::tests[] |
| --- |

pointers to [npf\_test](structnpf__test.md "npf_test") instances

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_pkt\_filter.h](net__pkt__filter_8h_source.md)

- [npf\_rule](structnpf__rule.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
