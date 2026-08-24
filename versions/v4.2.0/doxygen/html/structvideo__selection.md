---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvideo__selection.html
original_path: doxygen/html/structvideo__selection.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_selection Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

Video selection (crop / compose) structure.
[More...](#details)

`#include <[zephyr/drivers/video.h](video_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) | [type](#aec9dd0ae07f995f490ebdd86d48c1a63) |
|  | buffer type, allow to select for device having both input and output |
| enum [video\_selection\_target](group__video__interface.md#gae375c0586e3505632cc69348935c9b54) | [target](#afe358118a1d3c373888674f331dd05f1) |
|  | selection target enum |
| struct [video\_rect](structvideo__rect.md) | [rect](#a2e634792c0758a3dd576e4871c250bd2) |
|  | selection target rectangle |

## Detailed Description

Video selection (crop / compose) structure.

Used to describe the query and set selection target on a video device

## Field Documentation

## [◆ ](#a2e634792c0758a3dd576e4871c250bd2)rect

| struct [video\_rect](structvideo__rect.md) video\_selection::rect |
| --- |

selection target rectangle

## [◆ ](#afe358118a1d3c373888674f331dd05f1)target

| enum [video\_selection\_target](group__video__interface.md#gae375c0586e3505632cc69348935c9b54) video\_selection::target |
| --- |

selection target enum

## [◆ ](#aec9dd0ae07f995f490ebdd86d48c1a63)type

| enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) video\_selection::type |
| --- |

buffer type, allow to select for device having both input and output

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video.h](video_8h_source.md)

- [video\_selection](structvideo__selection.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
