---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structsmp__streamer.html
original_path: doxygen/html/structsmp__streamer.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_streamer Struct Reference

Decodes, encodes, and transmits SMP packets.
[More...](#details)

`#include <[smp.h](mgmt_2mcumgr_2smp_2smp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [smp\_transport](structsmp__transport.md) \* | [smpt](#a478b0732071a888bd83ccd03bdd51e85) |
| struct [cbor\_nb\_reader](structcbor__nb__reader.md) \* | [reader](#ad5f6bcfcea32075ff61afc1b6c4972be) |
| struct [cbor\_nb\_writer](structcbor__nb__writer.md) \* | [writer](#a00f6b8731e1a789939eaec106d746daf) |

## Detailed Description

Decodes, encodes, and transmits SMP packets.

## Field Documentation

## [◆ ](#ad5f6bcfcea32075ff61afc1b6c4972be)reader

| struct [cbor\_nb\_reader](structcbor__nb__reader.md)\* smp\_streamer::reader |
| --- |

## [◆ ](#a478b0732071a888bd83ccd03bdd51e85)smpt

| struct [smp\_transport](structsmp__transport.md)\* smp\_streamer::smpt |
| --- |

## [◆ ](#a00f6b8731e1a789939eaec106d746daf)writer

| struct [cbor\_nb\_writer](structcbor__nb__writer.md)\* smp\_streamer::writer |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/smp/[smp.h](mgmt_2mcumgr_2smp_2smp_8h_source.md)

- [smp\_streamer](structsmp__streamer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
