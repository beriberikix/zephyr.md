---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__w1__network.html
original_path: doxygen/html/group__w1__network.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

1-Wire network layer

[Device Driver APIs](group__io__interfaces.md) » [1-Wire Interface](group__w1__interface.md)

1-Wire network layer
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [w1\_rom](structw1__rom.md) |
|  | [w1\_rom](structw1__rom.md "w1_rom struct.") struct. [More...](structw1__rom.md#details) |
| struct | [w1\_slave\_config](structw1__slave__config.md) |
|  | Node specific 1-wire configuration struct. [More...](structw1__slave__config.md#details) |

| Macros | |
| --- | --- |
| #define | [W1\_SEARCH\_ALL\_FAMILIES](#ga909502b9b18c15a9ab0da8d3605e8c37)   0x00 |
|  | This flag can be passed to searches in order to not filter on family ID. |
| #define | [W1\_ROM\_INIT\_ZERO](#ga17770ecebad7170e9004afd9a7735c73) |
|  | Initialize all [w1\_rom](structw1__rom.md "w1_rom struct.") struct members to zero. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [w1\_search\_callback\_t](#ga2f5540f2a86fd55edcd7a8ffecbfd786)) (struct [w1\_rom](structw1__rom.md) rom, void \*user\_data) |
|  | Define the application callback handler function signature for searches. |

| Functions | |
| --- | --- |
| int | [w1\_read\_rom](#ga93abefbd0e7067db474e6480301a0c4c) (const struct [device](structdevice.md) \*dev, struct [w1\_rom](structw1__rom.md) \*rom) |
|  | Read Peripheral 64-bit ROM. |
| int | [w1\_match\_rom](#ga53f34d64504498dbb194bc2119727908) (const struct [device](structdevice.md) \*dev, const struct [w1\_slave\_config](structw1__slave__config.md) \*config) |
|  | Select a specific slave by broadcasting a selected ROM. |
| int | [w1\_resume\_command](#ga67c815bb99b75c862a483d4f8556b24a) (const struct [device](structdevice.md) \*dev) |
|  | Select the slave last addressed with a Match ROM or Search ROM command. |
| int | [w1\_skip\_rom](#gaba2be4e87ff472e90b705dbd73b913de) (const struct [device](structdevice.md) \*dev, const struct [w1\_slave\_config](structw1__slave__config.md) \*config) |
|  | Select all slaves regardless of ROM. |
| int | [w1\_reset\_select](#gaa0acc88fe02535a3d512b866b6d34b8a) (const struct [device](structdevice.md) \*dev, const struct [w1\_slave\_config](structw1__slave__config.md) \*config) |
|  | In single drop configurations use Skip Select command, otherwise use Match ROM command. |
| int | [w1\_write\_read](#ga1cf8c016ac66c3970f72fa1f409fa680) (const struct [device](structdevice.md) \*dev, const struct [w1\_slave\_config](structw1__slave__config.md) \*config, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) write\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) read\_len) |
|  | Write then read data from the 1-Wire slave with matching ROM. |
| int | [w1\_search\_bus](#ga19533f445029a69aac7d4ca5a7aeedcd) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) command, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) family, [w1\_search\_callback\_t](#ga2f5540f2a86fd55edcd7a8ffecbfd786) callback, void \*user\_data) |
|  | Search 1-wire slaves on the bus. |
| static int | [w1\_search\_rom](#ga024af0ee5018d7078808cc0a544cfd26) (const struct [device](structdevice.md) \*dev, [w1\_search\_callback\_t](#ga2f5540f2a86fd55edcd7a8ffecbfd786) callback, void \*user\_data) |
|  | Search for 1-Wire slave on bus. |
| static int | [w1\_search\_alarm](#ga0f510bd3720e54b4eeb4e368934db7f0) (const struct [device](structdevice.md) \*dev, [w1\_search\_callback\_t](#ga2f5540f2a86fd55edcd7a8ffecbfd786) callback, void \*user\_data) |
|  | Search for 1-Wire slaves with an active alarm. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [w1\_rom\_to\_uint64](#ga178a88d0c585d5df0405aadde3ea9178) (const struct [w1\_rom](structw1__rom.md) \*rom) |
|  | Function to convert a [w1\_rom](structw1__rom.md "w1_rom struct.") struct to an [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1). |
| static void | [w1\_uint64\_to\_rom](#ga6e4dba051a6b29c974e499db17315034) (const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rom64, struct [w1\_rom](structw1__rom.md) \*rom) |
|  | Function to write an [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) to struct [w1\_rom](structw1__rom.md "w1_rom struct.") pointer. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [w1\_crc8](#ga350a384a6040d1fbb86bfb804013ade3) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute CRC-8 chacksum as defined in the 1-Wire specification. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [w1\_crc16](#ga5635f79a54a2e5b96c8b7ca9a8ab8366) (const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute 1-Wire variant of CRC 16. |

| 1-Wire ROM Commands | |
| --- | --- |
| #define | [W1\_CMD\_SKIP\_ROM](#ga9792cb2093e911a4722b7fa9457093dc)   0xCC |
|  | This command allows the bus master to read the slave devices without providing their ROM code. |
| #define | [W1\_CMD\_MATCH\_ROM](#gae97f7ecda699ccf9b63030f2af632bc8)   0x55 |
|  | This command allows the bus master to address a specific slave device by providing its ROM code. |
| #define | [W1\_CMD\_RESUME](#ga31230559122289c179f01e09e3847830)   0xA5 |
|  | This command allows the bus master to resume a previous read out from where it left off. |
| #define | [W1\_CMD\_READ\_ROM](#ga9e1a9a38889bf165370670c28778028b)   0x33 |
|  | This command allows the bus master to read the ROM code from a single slave device. |
| #define | [W1\_CMD\_SEARCH\_ROM](#ga57f17871edab0b771f2f664bf9bafb79)   0xF0 |
|  | This command allows the bus master to discover the addresses (i.e., ROM codes) of all slave devices on the bus. |
| #define | [W1\_CMD\_SEARCH\_ALARM](#gafc7a257428c69bb4549c6cd05a928957)   0xEC |
|  | This command allows the bus master to identify which devices have experienced an alarm condition. |
| #define | [W1\_CMD\_OVERDRIVE\_SKIP\_ROM](#ga8b61b2308f2681801894f24ea2c95b12)   0x3C |
|  | This command allows the bus master to address all devices on the bus and then switch them to overdrive speed. |
| #define | [W1\_CMD\_OVERDRIVE\_MATCH\_ROM](#ga3e3f9fa70074188a2e489f34555b519b)   0x69 |
|  | This command allows the bus master to address a specific device and switch it to overdrive speed. |

| CRC Defines | |
| --- | --- |
| #define | [W1\_CRC8\_SEED](#gaa4ad8d9a3791fbca6c99d49b9793a002)   0x00 |
|  | Seed value used to calculate the 1-Wire 8-bit crc. |
| #define | [W1\_CRC8\_POLYNOMIAL](#gabe56ffbe20c2ba7e0a5c87c8e36c45e5)   0x8C |
|  | Polynomial used to calculate the 1-Wire 8-bit crc. |
| #define | [W1\_CRC16\_SEED](#ga324f30f17c6cd1b33650b58055a3a57f)   0x0000 |
|  | Seed value used to calculate the 1-Wire 16-bit crc. |
| #define | [W1\_CRC16\_POLYNOMIAL](#gab94362fbf4eec5f115f93fc8976cff0d)   0xa001 |
|  | Polynomial used to calculate the 1-Wire 16-bit crc. |

## Detailed Description

1-Wire network layer

## Macro Definition Documentation

## [◆ ](#gae97f7ecda699ccf9b63030f2af632bc8)W1\_CMD\_MATCH\_ROM

| #define W1\_CMD\_MATCH\_ROM   0x55 |
| --- |

`#include <[w1.h](w1_8h.md)>`

This command allows the bus master to address a specific slave device by providing its ROM code.

## [◆ ](#ga3e3f9fa70074188a2e489f34555b519b)W1\_CMD\_OVERDRIVE\_MATCH\_ROM

| #define W1\_CMD\_OVERDRIVE\_MATCH\_ROM   0x69 |
| --- |

`#include <[w1.h](w1_8h.md)>`

This command allows the bus master to address a specific device and switch it to overdrive speed.

## [◆ ](#ga8b61b2308f2681801894f24ea2c95b12)W1\_CMD\_OVERDRIVE\_SKIP\_ROM

| #define W1\_CMD\_OVERDRIVE\_SKIP\_ROM   0x3C |
| --- |

`#include <[w1.h](w1_8h.md)>`

This command allows the bus master to address all devices on the bus and then switch them to overdrive speed.

## [◆ ](#ga9e1a9a38889bf165370670c28778028b)W1\_CMD\_READ\_ROM

| #define W1\_CMD\_READ\_ROM   0x33 |
| --- |

`#include <[w1.h](w1_8h.md)>`

This command allows the bus master to read the ROM code from a single slave device.

This command should be used when there is only a single slave device on the bus.

## [◆ ](#ga31230559122289c179f01e09e3847830)W1\_CMD\_RESUME

| #define W1\_CMD\_RESUME   0xA5 |
| --- |

`#include <[w1.h](w1_8h.md)>`

This command allows the bus master to resume a previous read out from where it left off.

## [◆ ](#gafc7a257428c69bb4549c6cd05a928957)W1\_CMD\_SEARCH\_ALARM

| #define W1\_CMD\_SEARCH\_ALARM   0xEC |
| --- |

`#include <[w1.h](w1_8h.md)>`

This command allows the bus master to identify which devices have experienced an alarm condition.

## [◆ ](#ga57f17871edab0b771f2f664bf9bafb79)W1\_CMD\_SEARCH\_ROM

| #define W1\_CMD\_SEARCH\_ROM   0xF0 |
| --- |

`#include <[w1.h](w1_8h.md)>`

This command allows the bus master to discover the addresses (i.e., ROM codes) of all slave devices on the bus.

## [◆ ](#ga9792cb2093e911a4722b7fa9457093dc)W1\_CMD\_SKIP\_ROM

| #define W1\_CMD\_SKIP\_ROM   0xCC |
| --- |

`#include <[w1.h](w1_8h.md)>`

This command allows the bus master to read the slave devices without providing their ROM code.

## [◆ ](#gab94362fbf4eec5f115f93fc8976cff0d)W1\_CRC16\_POLYNOMIAL

| #define W1\_CRC16\_POLYNOMIAL   0xa001 |
| --- |

`#include <[w1.h](w1_8h.md)>`

Polynomial used to calculate the 1-Wire 16-bit crc.

## [◆ ](#ga324f30f17c6cd1b33650b58055a3a57f)W1\_CRC16\_SEED

| #define W1\_CRC16\_SEED   0x0000 |
| --- |

`#include <[w1.h](w1_8h.md)>`

Seed value used to calculate the 1-Wire 16-bit crc.

## [◆ ](#gabe56ffbe20c2ba7e0a5c87c8e36c45e5)W1\_CRC8\_POLYNOMIAL

| #define W1\_CRC8\_POLYNOMIAL   0x8C |
| --- |

`#include <[w1.h](w1_8h.md)>`

Polynomial used to calculate the 1-Wire 8-bit crc.

## [◆ ](#gaa4ad8d9a3791fbca6c99d49b9793a002)W1\_CRC8\_SEED

| #define W1\_CRC8\_SEED   0x00 |
| --- |

`#include <[w1.h](w1_8h.md)>`

Seed value used to calculate the 1-Wire 8-bit crc.

## [◆ ](#ga17770ecebad7170e9004afd9a7735c73)W1\_ROM\_INIT\_ZERO

| #define W1\_ROM\_INIT\_ZERO |
| --- |

`#include <[w1.h](w1_8h.md)>`

**Value:**

{ \

.family = 0, .serial = { 0 }, .crc = 0, \

}

Initialize all [w1\_rom](structw1__rom.md "w1_rom struct.") struct members to zero.

## [◆ ](#ga909502b9b18c15a9ab0da8d3605e8c37)W1\_SEARCH\_ALL\_FAMILIES

| #define W1\_SEARCH\_ALL\_FAMILIES   0x00 |
| --- |

`#include <[w1.h](w1_8h.md)>`

This flag can be passed to searches in order to not filter on family ID.

## Typedef Documentation

## [◆ ](#ga2f5540f2a86fd55edcd7a8ffecbfd786)w1\_search\_callback\_t

| typedef void(\* w1\_search\_callback\_t) (struct [w1\_rom](structw1__rom.md) rom, void \*user\_data) |
| --- |

`#include <[w1.h](w1_8h.md)>`

Define the application callback handler function signature for searches.

Parameters
:   | rom | found The ROM of the found slave. |
    | --- | --- |
    | user\_data | User data provided to the [w1\_search\_bus()](#ga19533f445029a69aac7d4ca5a7aeedcd) call. |

## Function Documentation

## [◆ ](#ga5635f79a54a2e5b96c8b7ca9a8ab8366)w1\_crc16()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) w1\_crc16 | ( | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *seed*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, | |  |  | const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Compute 1-Wire variant of CRC 16.

The 16-bit 1-Wire crc variant is using the reflected polynomial function X^16 + X^15 \* + X^2 + 1 with the initial value set to 0x0000. See also APPLICATION NOTE 27: "UNDERSTANDING AND USING CYCLIC REDUNDANCY CHECKS WITH MAXIM 1-WIRE AND IBUTTON PRODUCTS" [https://www.analog.com/en/resources/technical-articles/understanding-and-using-cyclic-redundancy-checks-with-maxim-1wire-and-ibutton-products.html](https://www.analog.com/en/resources/technical-articles/understanding-and-using-cyclic-redundancy-checks-with-maxim-1wire-and-ibutton-products.html)

Parameters
:   |  | seed | Init value for the CRC, it is usually set to 0x0000. |
    | --- | --- | --- |
    | [in] | src | Input bytes for the computation. |
    |  | len | Length of the input in bytes. |

Return values
:   | [CRC](group__crc.md) | The computed CRC16 value. |
    | --- | --- |

## [◆ ](#ga350a384a6040d1fbb86bfb804013ade3)w1\_crc8()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) w1\_crc8 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Compute CRC-8 chacksum as defined in the 1-Wire specification.

The 1-Wire of CRC 8 variant is using 0x31 as its polynomial with the initial value set to 0x00. This CRC is used to check the correctness of the unique 56-bit ROM.

Parameters
:   | [in] | src | Input bytes for the computation. |
    | --- | --- | --- |
    |  | len | Length of the input in bytes. |

Return values
:   | [CRC](group__crc.md) | The computed CRC8 value. |
    | --- | --- |

## [◆ ](#ga53f34d64504498dbb194bc2119727908)w1\_match\_rom()

| int w1\_match\_rom | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [w1\_slave\_config](structw1__slave__config.md) \* | *config* ) |

`#include <[w1.h](w1_8h.md)>`

Select a specific slave by broadcasting a selected ROM.

This routine allows the 1-Wire bus master to select a slave identified by its unique ROM, such that the next command will target only this single selected slave.

This command is only necessary in multidrop environments, otherwise the Skip ROM command can be issued. Once a slave has been selected, to reduce the communication overhead, the resume command can be used instead of this command to communicate with the selected slave.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [in] | config | Pointer to the slave specific 1-Wire config. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENODEV | In case no slave responds to reset. |
    | -errno | Other negative error code on error. |

## [◆ ](#ga93abefbd0e7067db474e6480301a0c4c)w1\_read\_rom()

| int w1\_read\_rom | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [w1\_rom](structw1__rom.md) \* | *rom* ) |

`#include <[w1.h](w1_8h.md)>`

Read Peripheral 64-bit ROM.

This procedure allows the 1-Wire bus master to read the peripherals’ 64-bit ROM without using the Search ROM procedure. This command can be used as long as not more than a single peripheral is connected to the bus. Otherwise data collisions occur and a faulty ROM is read.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [out] | rom | Pointer to the ROM structure. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENODEV | In case no slave responds to reset. |
    | -errno | Other negative error code in case of invalid crc and communication errors. |

## [◆ ](#gaa0acc88fe02535a3d512b866b6d34b8a)w1\_reset\_select()

| int w1\_reset\_select | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [w1\_slave\_config](structw1__slave__config.md) \* | *config* ) |

`#include <[w1.h](w1_8h.md)>`

In single drop configurations use Skip Select command, otherwise use Match ROM command.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [in] | config | Pointer to the slave specific 1-Wire config. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENODEV | In case no slave responds to reset. |
    | -errno | Other negative error code on error. |

## [◆ ](#ga67c815bb99b75c862a483d4f8556b24a)w1\_resume\_command()

| int w1\_resume\_command | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Select the slave last addressed with a Match ROM or Search ROM command.

This routine allows the 1-Wire bus master to re-select a slave device that was already addressed using a Match ROM or Search ROM command.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENODEV | In case no slave responds to reset. |
    | -errno | Other negative error code on error. |

## [◆ ](#ga178a88d0c585d5df0405aadde3ea9178)w1\_rom\_to\_uint64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) w1\_rom\_to\_uint64 | ( | const struct [w1\_rom](structw1__rom.md) \* | *rom* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Function to convert a [w1\_rom](structw1__rom.md "w1_rom struct.") struct to an [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1).

Parameters
:   | [in] | rom | Pointer to the ROM struct. |
    | --- | --- | --- |

Return values
:   | rom64 | The ROM converted to an unsigned integer in endianness. |
    | --- | --- |

## [◆ ](#ga0f510bd3720e54b4eeb4e368934db7f0)w1\_search\_alarm()

| | int w1\_search\_alarm | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [w1\_search\_callback\_t](#ga2f5540f2a86fd55edcd7a8ffecbfd786) | *callback*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Search for 1-Wire slaves with an active alarm.

This routine searches 1-Wire slaves on the bus, which currently have an active alarm.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    |  | callback | Application callback handler function to be called for each found slave. |
    | [in] | user\_data | User data to pass to the application callback handler function. |

Return values
:   | slave\_count | Number of slaves found. |
    | --- | --- |
    | -errno | Negative error code on error. |

## [◆ ](#ga19533f445029a69aac7d4ca5a7aeedcd)w1\_search\_bus()

| int w1\_search\_bus | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *command*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *family*, |
|  |  | [w1\_search\_callback\_t](#ga2f5540f2a86fd55edcd7a8ffecbfd786) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[w1.h](w1_8h.md)>`

Search 1-wire slaves on the bus.

This function searches slaves on the 1-wire bus, with the possibility to search either all slaves or only slaves that have an active alarm state. If a callback is passed, the callback is called for each found slave.

The algorithm mostly follows the suggestions of [https://www.analog.com/en/resources/app-notes/1wire-search-algorithm.html](https://www.analog.com/en/resources/app-notes/1wire-search-algorithm.html)

Note: Filtering on families is not supported.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    |  | command | Can either be W1\_SEARCH\_ALARM or W1\_SEARCH\_ROM. |
    |  | family | W1\_SEARCH\_ALL\_FAMILIES searcheas all families, filtering on a specific family is not yet supported. |
    |  | callback | Application callback handler function to be called for each found slave. |
    | [in] | user\_data | User data to pass to the application callback handler function. |

Return values
:   | slave\_count | Number of slaves found. |
    | --- | --- |
    | -errno | Negative error code on error. |

## [◆ ](#ga024af0ee5018d7078808cc0a544cfd26)w1\_search\_rom()

| | int w1\_search\_rom | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [w1\_search\_callback\_t](#ga2f5540f2a86fd55edcd7a8ffecbfd786) | *callback*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Search for 1-Wire slave on bus.

This routine can discover unknown slaves on the bus by scanning for the unique 64-bit registration number.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    |  | callback | Application callback handler function to be called for each found slave. |
    | [in] | user\_data | User data to pass to the application callback handler function. |

Return values
:   | slave\_count | Number of slaves found. |
    | --- | --- |
    | -errno | Negative error code on error. |

## [◆ ](#gaba2be4e87ff472e90b705dbd73b913de)w1\_skip\_rom()

| int w1\_skip\_rom | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [w1\_slave\_config](structw1__slave__config.md) \* | *config* ) |

`#include <[w1.h](w1_8h.md)>`

Select all slaves regardless of ROM.

This routine sets up the bus slaves to receive a command. It is usually used when there is only one peripheral on the bus to avoid the overhead of the Match ROM command. But it can also be used to concurrently write to all slave devices.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [in] | config | Pointer to the slave specific 1-Wire config. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENODEV | In case no slave responds to reset. |
    | -errno | Other negative error code on error. |

## [◆ ](#ga6e4dba051a6b29c974e499db17315034)w1\_uint64\_to\_rom()

| | void w1\_uint64\_to\_rom | ( | const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *rom64*, | | --- | --- | --- | --- | |  |  | struct [w1\_rom](structw1__rom.md) \* | *rom* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Function to write an [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) to struct [w1\_rom](structw1__rom.md "w1_rom struct.") pointer.

Parameters
:   |  | rom64 | Unsigned 64 bit integer representing the ROM in host endianness. |
    | --- | --- | --- |
    | [out] | rom | The ROM struct pointer. |

## [◆ ](#ga1cf8c016ac66c3970f72fa1f409fa680)w1\_write\_read()

| int w1\_write\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [w1\_slave\_config](structw1__slave__config.md) \* | *config*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *write\_buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *write\_len*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *read\_buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *read\_len* ) |

`#include <[w1.h](w1_8h.md)>`

Write then read data from the 1-Wire slave with matching ROM.

This routine uses w1\_reset\_select to select the given ROM. Then writes given data and reads the response back from the slave.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [in] | config | Pointer to the slave specific 1-Wire config. |
    | [in] | write\_buf | Pointer to the data to be written. |
    |  | write\_len | Number of bytes to write. |
    | [out] | read\_buf | Pointer to storage for read data. |
    |  | read\_len | Number of bytes to read. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENODEV | In case no slave responds to reset. |
    | -errno | Other negative error code on error. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
