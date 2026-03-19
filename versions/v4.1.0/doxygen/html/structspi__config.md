---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structspi__config.html
original_path: doxygen/html/structspi__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SPI Interface](group__spi__interface.md)

SPI controller configuration structure.
[More...](#details)

`#include <[spi.h](drivers_2spi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [frequency](#aa1ec6933fe66f91653c5be488e4c9b2a) |
|  | Bus frequency in Hertz. |
| [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a) | [operation](#a71a02ea548e187e6511abf10fdfa4829) |
|  | Operation flags. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [slave](#a020ca853537483b9641c37be70ab6ca0) |
|  | Slave number from 0 to host controller slave limit. |
| struct [spi\_cs\_control](structspi__cs__control.md) | [cs](#a537dbfe323fafedaa219de1be2097dde) |
|  | GPIO chip-select line (optional, must be initialized to zero if not used). |

## Detailed Description

SPI controller configuration structure.

## Field Documentation

## [◆ ](#a537dbfe323fafedaa219de1be2097dde)cs

| struct [spi\_cs\_control](structspi__cs__control.md) spi\_config::cs |
| --- |

GPIO chip-select line (optional, must be initialized to zero if not used).

## [◆ ](#aa1ec6933fe66f91653c5be488e4c9b2a)frequency

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spi\_config::frequency |
| --- |

Bus frequency in Hertz.

## [◆ ](#a71a02ea548e187e6511abf10fdfa4829)operation

| [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a) spi\_config::operation |
| --- |

Operation flags.

It is a bit field with the following parts:

- 0: Master or slave.
- 1..3: Polarity, phase and loop mode.
- 4: LSB or MSB first.
- 5..10: Size of a data frame (word) in bits.
- 11: Full/half duplex.
- 12: Hold on the CS line if possible.
- 13: Keep resource locked for the caller.
- 14: Active high CS logic.
- 15: Motorola or TI frame format (optional).

If `CONFIG_SPI_EXTENDED_MODES` is enabled:

- 16..17: MISO lines (Single/Dual/Quad/Octal).
- 18..31: Reserved for future use.

## [◆ ](#a020ca853537483b9641c37be70ab6ca0)slave

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) spi\_config::slave |
| --- |

Slave number from 0 to host controller slave limit.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[spi.h](drivers_2spi_8h_source.md)

- [spi\_config](structspi__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
