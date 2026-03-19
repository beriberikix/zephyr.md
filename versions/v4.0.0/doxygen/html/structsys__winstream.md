---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structsys__winstream.html
original_path: doxygen/html/structsys__winstream.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_winstream Struct Reference

Lockless shared memory byte stream IPC.
[More...](#details)

`#include <[winstream.h](winstream_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#a30b03df76a51ecbf0cbe33975d5aaa66) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [start](#a1cc84dfd9f812b3491135d13365c7a98) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [end](#a6b80cf715e4a3ca7b7b74b9efd150a23) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [seq](#a7d946d6a54652a8ac035dd8cd0ba861a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#a341203116bfee52d4b801466097fc3eb) [] |

## Detailed Description

Lockless shared memory byte stream IPC.

The [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC.") utility implements a unidirectional byte stream with simple read/write semantics on top of a memory region shared by the writer and reader. It requires no locking or synchronization mechanisms beyond reliable ordering of memory operations, and so is a good fit for use with heterogeneous shared memory environments (for example, where Zephyr needs to talk to other CPUs in the system running their own software).

This object does not keep track of the last sequence number read: the reader must keep that state and provide it on every read operation. After reaching "steady state", 'end' and 'start' are one byte apart because the buffer is always full.

## Field Documentation

## [◆ ](#a341203116bfee52d4b801466097fc3eb)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sys\_winstream::data[] |
| --- |

## [◆ ](#a6b80cf715e4a3ca7b7b74b9efd150a23)end

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_winstream::end |
| --- |

## [◆ ](#a30b03df76a51ecbf0cbe33975d5aaa66)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_winstream::len |
| --- |

## [◆ ](#a7d946d6a54652a8ac035dd8cd0ba861a)seq

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_winstream::seq |
| --- |

## [◆ ](#a1cc84dfd9f812b3491135d13365c7a98)start

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_winstream::start |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[winstream.h](winstream_8h_source.md)

- [sys\_winstream](structsys__winstream.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
