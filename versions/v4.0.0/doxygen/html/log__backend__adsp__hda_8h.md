---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__backend__adsp__hda_8h.html
original_path: doxygen/html/log__backend__adsp__hda_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_adsp\_hda.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](log__backend__adsp__hda_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [adsp\_hda\_log\_hook\_t](#a8d50e67fece0cf916b72fcaa7c2bd11a)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) written) |
|  | HDA logger requires a hook for IPC messages. |

| Functions | |
| --- | --- |
| void | [adsp\_hda\_log\_init](#ac9ae5b9b36f95d30643c0acf95d51e82) ([adsp\_hda\_log\_hook\_t](#a8d50e67fece0cf916b72fcaa7c2bd11a) hook, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Initialize the Intel ADSP HDA logger. |

## Typedef Documentation

## [◆ ](#a8d50e67fece0cf916b72fcaa7c2bd11a)adsp\_hda\_log\_hook\_t

| typedef void(\* adsp\_hda\_log\_hook\_t) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) written) |
| --- |

HDA logger requires a hook for IPC messages.

When the log is flushed and written with DMA an IPC message should be sent to inform the host. This hook function pointer allows for that

## Function Documentation

## [◆ ](#ac9ae5b9b36f95d30643c0acf95d51e82)adsp\_hda\_log\_init()

| void adsp\_hda\_log\_init | ( | [adsp\_hda\_log\_hook\_t](#a8d50e67fece0cf916b72fcaa7c2bd11a) | *hook*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel* ) |

Initialize the Intel ADSP HDA logger.

Parameters
:   | hook | Function is called after each HDA flush in order to inform the Host of DMA log data. This hook may be called from multiple CPUs and multiple calling contexts concurrently. It is up to the author of the hook to serialize if needed. It is guaranteed to be called once for every flush. |
    | --- | --- |
    | channel | HDA stream (DMA Channel) to use for logging |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_adsp\_hda.h](log__backend__adsp__hda_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
