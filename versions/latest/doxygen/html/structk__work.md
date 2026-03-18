---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structk__work.html
original_path: doxygen/html/structk__work.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_work Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Work Queue APIs](group__workqueue__apis.md)

A structure used to submit work.
[More...](#details)

`#include <[kernel.h](include_2zephyr_2kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a85772682983e0fdeb735f0821d5710d4) |
| [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) | [handler](#a096d6ca1338fb0fbfa330b790136f172) |
| struct [k\_work\_q](structk__work__q.md) \* | [queue](#a551be8394e041020c36a97dc2e12e137) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a391ed7d2039cd05c9894267bf8ea4dfd) |

## Detailed Description

A structure used to submit work.

## Field Documentation

## [◆ ](#a391ed7d2039cd05c9894267bf8ea4dfd)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_work::flags |
| --- |

## [◆ ](#a096d6ca1338fb0fbfa330b790136f172)handler

| [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) k\_work::handler |
| --- |

## [◆ ](#a85772682983e0fdeb735f0821d5710d4)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) k\_work::node |
| --- |

## [◆ ](#a551be8394e041020c36a97dc2e12e137)queue

| struct [k\_work\_q](structk__work__q.md)\* k\_work::queue |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](include_2zephyr_2kernel_8h_source.md)

- [k\_work](structk__work.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
