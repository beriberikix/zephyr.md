---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structgroup.html
original_path: doxygen/html/structgroup.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

group Struct Reference

Group structure.
[More...](#details)

`#include <[grp.h](grp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char \* | [gr\_name](#a828b9f3708aa76cecd8fda0a20b61e98) |
|  | < the name of the group |
| [gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8) | [gr\_gid](#a00f124d1201a4de3cc885fe87a91431f) |
|  | pointer to a null-terminated array of character pointers to member names |
| char \*\* | [gr\_mem](#a338a8153e1e47d345a0bb578f3c2656c) |

## Detailed Description

Group structure.

## Field Documentation

## [◆ ](#a00f124d1201a4de3cc885fe87a91431f)gr\_gid

| [gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8) group::gr\_gid |
| --- |

pointer to a null-terminated array of character pointers to member names

## [◆ ](#a338a8153e1e47d345a0bb578f3c2656c)gr\_mem

| char\*\* group::gr\_mem |
| --- |

## [◆ ](#a828b9f3708aa76cecd8fda0a20b61e98)gr\_name

| char\* group::gr\_name |
| --- |

< the name of the group

numerical group ID

---

The documentation for this struct was generated from the following file:

- zephyr/posix/[grp.h](grp_8h_source.md)

- [group](structgroup.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
