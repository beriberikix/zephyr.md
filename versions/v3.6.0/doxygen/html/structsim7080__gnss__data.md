---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsim7080__gnss__data.html
original_path: doxygen/html/structsim7080__gnss__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sim7080\_gnss\_data Struct Reference

`#include <[simcom-sim7080.h](simcom-sim7080_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [run\_status](#ab917d70a3c5adffb8aecc9e521c36599) |
|  | Whether gnss is powered or not. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [fix\_status](#a881db8b7b52d481416bc5f373446bfc2) |
|  | Whether fix is acquired or not. |
| char | [utc](#a8a42fbb4a716a0eefe317996f8fe7a8a) [20] |
|  | UTC in format yyyyMMddhhmmss.sss. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [lat](#a545077bd8eb1d6827c50b59d469bdc4a) |
|  | Latitude in 10^-7 degree. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [lon](#a23dc6e7aa0cc507cf5141aa5329e17ef) |
|  | Longitude in 10^-7 degree. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [alt](#aa481937aedd2817e3a301663648d9f7d) |
|  | Altitude in mm. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [hdop](#aca6603b72f8ac67a0a0084a3fc8a60a1) |
|  | Horizontal dilution of precision in 10^-2. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cog](#a7dee72b39dc718ade2cc27bedc691d6e) |
|  | Course over ground un 10^-2 degree. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [kmh](#a62b8a5072942a325156a90607888612b) |
|  | Speed in 10^-1 km/h. |

## Field Documentation

## [◆ ](#aa481937aedd2817e3a301663648d9f7d)alt

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) sim7080\_gnss\_data::alt |
| --- |

Altitude in mm.

## [◆ ](#a7dee72b39dc718ade2cc27bedc691d6e)cog

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sim7080\_gnss\_data::cog |
| --- |

Course over ground un 10^-2 degree.

## [◆ ](#a881db8b7b52d481416bc5f373446bfc2)fix\_status

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sim7080\_gnss\_data::fix\_status |
| --- |

Whether fix is acquired or not.

## [◆ ](#aca6603b72f8ac67a0a0084a3fc8a60a1)hdop

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sim7080\_gnss\_data::hdop |
| --- |

Horizontal dilution of precision in 10^-2.

## [◆ ](#a62b8a5072942a325156a90607888612b)kmh

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sim7080\_gnss\_data::kmh |
| --- |

Speed in 10^-1 km/h.

## [◆ ](#a545077bd8eb1d6827c50b59d469bdc4a)lat

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) sim7080\_gnss\_data::lat |
| --- |

Latitude in 10^-7 degree.

## [◆ ](#a23dc6e7aa0cc507cf5141aa5329e17ef)lon

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) sim7080\_gnss\_data::lon |
| --- |

Longitude in 10^-7 degree.

## [◆ ](#ab917d70a3c5adffb8aecc9e521c36599)run\_status

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sim7080\_gnss\_data::run\_status |
| --- |

Whether gnss is powered or not.

## [◆ ](#a8a42fbb4a716a0eefe317996f8fe7a8a)utc

| char sim7080\_gnss\_data::utc[20] |
| --- |

UTC in format yyyyMMddhhmmss.sss.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/modem/[simcom-sim7080.h](simcom-sim7080_8h_source.md)

- [sim7080\_gnss\_data](structsim7080__gnss__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
