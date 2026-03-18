---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nrf__qspi__nor_8h.html
original_path: doxygen/html/nrf__qspi__nor_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_qspi\_nor.h File Reference

`#include <zephyr/syscalls/nrf_qspi_nor.h>`

[Go to the source code of this file.](nrf__qspi__nor_8h_source.md)

| Functions | |
| --- | --- |
| void | [nrf\_qspi\_nor\_xip\_enable](#abfe75f149d6a54c7fefe9d3a2ed21ea3) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Specifies whether XIP (execute in place) operation should be possible. |

## Function Documentation

## [◆ ](#abfe75f149d6a54c7fefe9d3a2ed21ea3)nrf\_qspi\_nor\_xip\_enable()

| void nrf\_qspi\_nor\_xip\_enable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

Specifies whether XIP (execute in place) operation should be possible.

Normally, the driver deactivates the QSPI peripheral for periods when no QSPI operation is performed. This is done to avoid increased current consumption when the peripheral is idle. For the same reason, the base clock on nRF53 Series SoCs (HFCLK192M) is configured for those periods with the default /4 divider that cannot be used otherwise. However, when XIP accesses are used, the driver must be prevented from doing both these things as that would make XIP to fail. Hence, the application should use this function to signal to the driver that XIP accesses are expected to occur so that it keeps the QSPI peripheral operable. When XIP operation is no longer needed, it should be disabled with this function.

Parameters
:   | dev | flash device |
    | --- | --- |
    | enable | if true, the driver enables XIP operation and suppresses idle actions that would make XIP to fail |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash](dir_b5b0d43e6264d65db716db62f9858e50.md)
- [nrf\_qspi\_nor.h](nrf__qspi__nor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
