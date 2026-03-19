---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structgnttab__map__grant__ref.html
original_path: doxygen/html/structgnttab__map__grant__ref.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnttab\_map\_grant\_ref Struct Reference

`#include <[grant_table.h](grant__table_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [host\_addr](#a2c811c2986d6d7d5236a261c50c3492c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a0db5af518a433b4441729019e65e1e3d) |
| [grant\_ref\_t](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e) | [ref](#aff19dc5005ea1082cc9b5cd6bb89a2d7) |
| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) | [dom](#a14efe928545333fb0f3544cdf98dc0ab) |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [status](#a738c22fab57008dcd5dac3651cfab66c) |
| [grant\_handle\_t](grant__table_8h.md#a1eade3c86c0fd0e71217eefaa3b38cd1) | [handle](#a6c0ce65e16e117c0678d635a2ee1d3f0) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [dev\_bus\_addr](#ac90b06b676c85d65f8311fb72f0cfa5a) |

## Field Documentation

## [◆ ](#ac90b06b676c85d65f8311fb72f0cfa5a)dev\_bus\_addr

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) gnttab\_map\_grant\_ref::dev\_bus\_addr |
| --- |

## [◆ ](#a14efe928545333fb0f3544cdf98dc0ab)dom

| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) gnttab\_map\_grant\_ref::dom |
| --- |

## [◆ ](#a0db5af518a433b4441729019e65e1e3d)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gnttab\_map\_grant\_ref::flags |
| --- |

## [◆ ](#a6c0ce65e16e117c0678d635a2ee1d3f0)handle

| [grant\_handle\_t](grant__table_8h.md#a1eade3c86c0fd0e71217eefaa3b38cd1) gnttab\_map\_grant\_ref::handle |
| --- |

## [◆ ](#a2c811c2986d6d7d5236a261c50c3492c)host\_addr

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) gnttab\_map\_grant\_ref::host\_addr |
| --- |

## [◆ ](#aff19dc5005ea1082cc9b5cd6bb89a2d7)ref

| [grant\_ref\_t](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e) gnttab\_map\_grant\_ref::ref |
| --- |

## [◆ ](#a738c22fab57008dcd5dac3651cfab66c)status

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) gnttab\_map\_grant\_ref::status |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[grant\_table.h](grant__table_8h_source.md)

- [gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
