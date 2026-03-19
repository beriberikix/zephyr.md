---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/flash__simulator_8h.html
original_path: doxygen/html/flash__simulator_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash\_simulator.h File Reference

Flash simulator specific API.
[More...](#details)

`#include <zephyr/syscalls/flash_simulator.h>`

[Go to the source code of this file.](flash__simulator_8h_source.md)

| Functions | |
| --- | --- |
| void \* | [flash\_simulator\_get\_memory](#a71cca7b794f8e9402d81491c7e93cc3f) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*mock\_size) |
|  | Obtain a pointer to the RAM buffer used but by the simulator. |

## Detailed Description

Flash simulator specific API.

Extension for flash simulator.

## Function Documentation

## [◆ ](#a71cca7b794f8e9402d81491c7e93cc3f)flash\_simulator\_get\_memory()

| void \* flash\_simulator\_get\_memory | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *mock\_size* ) |

Obtain a pointer to the RAM buffer used but by the simulator.

This function allows the caller to get the address and size of the RAM buffer in which the flash simulator emulates its flash memory content.

Parameters
:   | [in] | dev | flash simulator device pointer. |
    | --- | --- | --- |
    | [out] | mock\_size | size of the ram buffer. |

Return values
:   | pointer | to the ram buffer |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash](dir_b5b0d43e6264d65db716db62f9858e50.md)
- [flash\_simulator.h](flash__simulator_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
