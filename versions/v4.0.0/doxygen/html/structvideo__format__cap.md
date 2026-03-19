---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structvideo__format__cap.html
original_path: doxygen/html/structvideo__format__cap.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_format\_cap Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

Video format capability.
[More...](#details)

`#include <[video.h](video_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pixelformat](#af5beb952295592dc9dc235a4151b2f59) |
|  | FourCC pixel format value ([Video pixel formats](group__video__pixel__formats.md "Video pixel formats")). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [width\_min](#a539b75ac7b1eadc8c9ee9395b5b2fba9) |
|  | minimum supported frame width in pixels. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [width\_max](#ab45cdeb28d93d670f06caca449fccd66) |
|  | maximum supported frame width in pixels. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [height\_min](#ae6f82b60ad822a37a3c97a71892d8d35) |
|  | minimum supported frame height in pixels. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [height\_max](#ae5f4de43c4fdaa6bc7085042ec67cd5f) |
|  | maximum supported frame height in pixels. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [width\_step](#ab86710dfc4da3b5d0f9dd5017f971aad) |
|  | width step size in pixels. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [height\_step](#a512907acd398e053d48d26aab611772e) |
|  | height step size in pixels. |

## Detailed Description

Video format capability.

Used to describe a video endpoint format capability.

## Field Documentation

## [◆ ](#ae5f4de43c4fdaa6bc7085042ec67cd5f)height\_max

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_format\_cap::height\_max |
| --- |

maximum supported frame height in pixels.

## [◆ ](#ae6f82b60ad822a37a3c97a71892d8d35)height\_min

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_format\_cap::height\_min |
| --- |

minimum supported frame height in pixels.

## [◆ ](#a512907acd398e053d48d26aab611772e)height\_step

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) video\_format\_cap::height\_step |
| --- |

height step size in pixels.

## [◆ ](#af5beb952295592dc9dc235a4151b2f59)pixelformat

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_format\_cap::pixelformat |
| --- |

FourCC pixel format value ([Video pixel formats](group__video__pixel__formats.md "Video pixel formats")).

## [◆ ](#ab45cdeb28d93d670f06caca449fccd66)width\_max

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_format\_cap::width\_max |
| --- |

maximum supported frame width in pixels.

## [◆ ](#a539b75ac7b1eadc8c9ee9395b5b2fba9)width\_min

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_format\_cap::width\_min |
| --- |

minimum supported frame width in pixels.

## [◆ ](#ab86710dfc4da3b5d0f9dd5017f971aad)width\_step

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) video\_format\_cap::width\_step |
| --- |

width step size in pixels.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video.h](video_8h_source.md)

- [video\_format\_cap](structvideo__format__cap.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
