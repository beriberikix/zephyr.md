---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structzperf__upload__params.html
original_path: doxygen/html/structzperf__upload__params.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zperf\_upload\_params Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Zperf API](group__zperf.md)

`#include <[zperf.h](zperf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [sockaddr](structsockaddr.md) | [peer\_addr](#a78307a038b6a4fb02c8d89387a20b29c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [duration\_ms](#ac6f7bb4aa70c20d70d8644d647ad5b0f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rate\_kbps](#ab639ac94ca20c742114fa5e7bb89df4b) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [packet\_size](#a7815d9556cab97fb87742922663a5daf) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [tos](#afe1767e2c82ffe7e014a75b4ad833cb0) |  |
| int   [tcp\_nodelay](#a5a48be96c6b537c54dc500a28a3d307e) |  |
| int   [priority](#a90ce9f0e4e2526104ea4dd2837bc059b) |  |
| } | [options](#a7b453046c1c682941de34714cafc2fb6) |

## Field Documentation

## [◆ ](#ac6f7bb4aa70c20d70d8644d647ad5b0f)duration\_ms

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zperf\_upload\_params::duration\_ms |
| --- |

## [◆ ](#a7b453046c1c682941de34714cafc2fb6)[struct]

| struct { ... } zperf\_upload\_params::options |
| --- |

## [◆ ](#a7815d9556cab97fb87742922663a5daf)packet\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) zperf\_upload\_params::packet\_size |
| --- |

## [◆ ](#a78307a038b6a4fb02c8d89387a20b29c)peer\_addr

| struct [sockaddr](structsockaddr.md) zperf\_upload\_params::peer\_addr |
| --- |

## [◆ ](#a90ce9f0e4e2526104ea4dd2837bc059b)priority

| int zperf\_upload\_params::priority |
| --- |

## [◆ ](#ab639ac94ca20c742114fa5e7bb89df4b)rate\_kbps

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zperf\_upload\_params::rate\_kbps |
| --- |

## [◆ ](#a5a48be96c6b537c54dc500a28a3d307e)tcp\_nodelay

| int zperf\_upload\_params::tcp\_nodelay |
| --- |

## [◆ ](#afe1767e2c82ffe7e014a75b4ad833cb0)tos

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) zperf\_upload\_params::tos |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[zperf.h](zperf_8h_source.md)

- [zperf\_upload\_params](structzperf__upload__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
