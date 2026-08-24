---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/uniondac161s997__status.html
original_path: doxygen/html/uniondac161s997__status.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dac161s997\_status Union Reference

`#include <[zephyr/drivers/dac/dac161s997.h](dac161s997_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [raw](#ae607e4cf155134e1924ab6e82fd4c77c) |
| struct { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [current\_loop\_status](#a976624fa275ddcdbe02532ef49df1bec): 1 |  |
|  | True if the DAC161S997 is unable to maintain the output current. [More...](#a976624fa275ddcdbe02532ef49df1bec) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [loop\_status](#ae6b7aa08e791c7a16734ab0f749fba7f): 1 |  |
|  | Identical to current\_loop\_status except this bit is sticky. [More...](#ae6b7aa08e791c7a16734ab0f749fba7f) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [spi\_timeout\_error](#a607f3408e26204ab5d7587f45551a31e): 1 |  |
|  | True if a SPI command has not been received within SPI timeout period (default 100 ms). [More...](#a607f3408e26204ab5d7587f45551a31e) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [frame\_status](#a39d07d6166ac1472f79eaf9e3d13c750): 1 |  |
|  | A frame error is caused by an incorrect number of clocks during a register write. [More...](#a39d07d6166ac1472f79eaf9e3d13c750) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [error\_level\_pin\_state](#a96c43cb002dea17b7824288d9092cb90): 1 |  |
|  | Returns the state of the ERR\_LVL pin. [More...](#a96c43cb002dea17b7824288d9092cb90) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [dac\_resolution](#a55ea538eb473b99d4f15831f59844094): 3 |  |
|  | DAC resolution register. [More...](#a55ea538eb473b99d4f15831f59844094) |
| }; |  |

## Field Documentation

## [◆ ](#a745edaacaeb552dc778c86e70e350441)[struct]

| struct { ... } [dac161s997\_status](uniondac161s997__status.md) |
| --- |

## [◆ ](#a976624fa275ddcdbe02532ef49df1bec)current\_loop\_status

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dac161s997\_status::current\_loop\_status |
| --- |

True if the DAC161S997 is unable to maintain the output current.

## [◆ ](#a55ea538eb473b99d4f15831f59844094)dac\_resolution

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dac161s997\_status::dac\_resolution |
| --- |

DAC resolution register.

Always returns 0x7.

## [◆ ](#a96c43cb002dea17b7824288d9092cb90)error\_level\_pin\_state

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dac161s997\_status::error\_level\_pin\_state |
| --- |

Returns the state of the ERR\_LVL pin.

## [◆ ](#a39d07d6166ac1472f79eaf9e3d13c750)frame\_status

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dac161s997\_status::frame\_status |
| --- |

A frame error is caused by an incorrect number of clocks during a register write.

A register write without an integer multiple of 24 clock cycles will cause a Frame error.

## [◆ ](#ae6b7aa08e791c7a16734ab0f749fba7f)loop\_status

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dac161s997\_status::loop\_status |
| --- |

Identical to current\_loop\_status except this bit is sticky.

## [◆ ](#ae607e4cf155134e1924ab6e82fd4c77c)raw

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dac161s997\_status::raw |
| --- |

## [◆ ](#a607f3408e26204ab5d7587f45551a31e)spi\_timeout\_error

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dac161s997\_status::spi\_timeout\_error |
| --- |

True if a SPI command has not been received within SPI timeout period (default 100 ms).

If this error occurs, it is cleared with a properly formatted write command to a valid address.

---

The documentation for this union was generated from the following file:

- zephyr/drivers/dac/[dac161s997.h](dac161s997_8h_source.md)

- [dac161s997\_status](uniondac161s997__status.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
