---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structshell__adsp__memory__window.html
original_path: doxygen/html/structshell__adsp__memory__window.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_adsp\_memory\_window Struct Reference

Memwindow based shell transport.
[More...](#details)

`#include <[shell_adsp_memory_window.h](shell__adsp__memory__window_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) | [shell\_handler](#a730dbada8e6804b6eeadfa278971ad4d) |
|  | Handler function registered by shell. |
| struct k\_timer | [timer](#a398c24153b3263c74fe995a3c369a4cc) |
| void \* | [shell\_context](#a1baf124df654fc375612f6530652285d) |
|  | Context registered by shell. |
| struct [sys\_winstream](structsys__winstream.md) \* | [ws\_rx](#a00650a08293ddbc232002d36a9d5dffb) |
|  | Receive winstream object. |
| struct [sys\_winstream](structsys__winstream.md) \* | [ws\_tx](#a89d8688c922ce5b7ccb93e04d4e6d68a) |
|  | Transmit winstream object. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_seqno](#aa9809847f068296c4f610d93b288ec54) |
|  | Last read sequence number. |

## Detailed Description

Memwindow based shell transport.

## Field Documentation

## [◆ ](#aa9809847f068296c4f610d93b288ec54)read\_seqno

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_adsp\_memory\_window::read\_seqno |
| --- |

Last read sequence number.

## [◆ ](#a1baf124df654fc375612f6530652285d)shell\_context

| void\* shell\_adsp\_memory\_window::shell\_context |
| --- |

Context registered by shell.

## [◆ ](#a730dbada8e6804b6eeadfa278971ad4d)shell\_handler

| [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) shell\_adsp\_memory\_window::shell\_handler |
| --- |

Handler function registered by shell.

## [◆ ](#a398c24153b3263c74fe995a3c369a4cc)timer

| struct k\_timer shell\_adsp\_memory\_window::timer |
| --- |

## [◆ ](#a00650a08293ddbc232002d36a9d5dffb)ws\_rx

| struct [sys\_winstream](structsys__winstream.md)\* shell\_adsp\_memory\_window::ws\_rx |
| --- |

Receive winstream object.

## [◆ ](#a89d8688c922ce5b7ccb93e04d4e6d68a)ws\_tx

| struct [sys\_winstream](structsys__winstream.md)\* shell\_adsp\_memory\_window::ws\_tx |
| --- |

Transmit winstream object.

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_adsp\_memory\_window.h](shell__adsp__memory__window_8h_source.md)

- [shell\_adsp\_memory\_window](structshell__adsp__memory__window.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
