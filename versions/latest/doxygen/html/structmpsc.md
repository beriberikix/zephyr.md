---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmpsc.html
original_path: doxygen/html/structmpsc.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpsc Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [MPSC Lockfree Queue API](group__mpsc__lockfree.md)

MPSC Queue.
[More...](#details)

`#include <[mpsc_lockfree.h](mpsc__lockfree_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [mpsc\_ptr\_t](group__mpsc__lockfree.md#ga15b6ff032fa4602e72415cf95c69e626) | [head](#a39a19058689c20a0485cf5982e7fc833) |
| struct [mpsc\_node](structmpsc__node.md) \* | [tail](#ac7046e3208693f0cc8937261679892df) |
| struct [mpsc\_node](structmpsc__node.md) | [stub](#a02e8a6d90efcb0838844f85244ca88dd) |

## Detailed Description

MPSC Queue.

## Field Documentation

## [◆ ](#a39a19058689c20a0485cf5982e7fc833)head

| [mpsc\_ptr\_t](group__mpsc__lockfree.md#ga15b6ff032fa4602e72415cf95c69e626) mpsc::head |
| --- |

## [◆ ](#a02e8a6d90efcb0838844f85244ca88dd)stub

| struct [mpsc\_node](structmpsc__node.md) mpsc::stub |
| --- |

## [◆ ](#ac7046e3208693f0cc8937261679892df)tail

| struct [mpsc\_node](structmpsc__node.md)\* mpsc::tail |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[mpsc\_lockfree.h](mpsc__lockfree_8h_source.md)

- [mpsc](structmpsc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
