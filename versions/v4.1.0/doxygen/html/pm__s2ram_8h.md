---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pm__s2ram_8h.html
original_path: doxygen/html/pm__s2ram_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pm\_s2ram.h File Reference

public S2RAM APIs.
[More...](#details)

[Go to the source code of this file.](pm__s2ram_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef int(\* | [pm\_s2ram\_system\_off\_fn\_t](group__pm__s2ram.md#ga61b569a4b9053443c9b82b0ea1bfae53)) (void) |
|  | System off function. |

| Functions | |
| --- | --- |
| int | [arch\_pm\_s2ram\_suspend](group__pm__s2ram.md#ga6b82cf263c595b0d5cb353759000615c) ([pm\_s2ram\_system\_off\_fn\_t](group__pm__s2ram.md#ga61b569a4b9053443c9b82b0ea1bfae53) system\_off) |
|  | Save CPU context on suspend. |
| void | [pm\_s2ram\_mark\_set](group__pm__s2ram.md#ga88bb5cb4d2eb2c6014f0bad0e891ae1f) (void) |
|  | Mark that core is entering suspend-to-RAM state. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_s2ram\_mark\_check\_and\_clear](group__pm__s2ram.md#ga93f351a7dafa34ccdffd7e97763ab34b) (void) |
|  | Check suspend-to-RAM marking and clear its state. |

## Detailed Description

public S2RAM APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [common](dir_7cbd25c8850fe30be392200e83a608be.md)
- [pm\_s2ram.h](pm__s2ram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
