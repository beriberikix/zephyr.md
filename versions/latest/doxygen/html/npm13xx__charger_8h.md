---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/npm13xx__charger_8h.html
original_path: doxygen/html/npm13xx__charger_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npm13xx\_charger.h File Reference

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](npm13xx__charger_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [sensor\_channel\_npm13xx\_charger](#a3b5c9edfeb25c77685d67babdc4c5299) { [SENSOR\_CHAN\_NPM13XX\_CHARGER\_STATUS](#a3b5c9edfeb25c77685d67babdc4c5299abb7d0a263602d5a4e7fddf5b7fa44946) = SENSOR\_CHAN\_PRIV\_START , [SENSOR\_CHAN\_NPM13XX\_CHARGER\_ERROR](#a3b5c9edfeb25c77685d67babdc4c5299a68daf03ea54b12dba3bd2cac5d5f142b) , [SENSOR\_CHAN\_NPM13XX\_CHARGER\_VBUS\_STATUS](#a3b5c9edfeb25c77685d67babdc4c5299aa070958a66af182e1db9c49a6a41c8c2) } |
| enum | [sensor\_attribute\_npm13xx\_charger](#add553da0fb80ee2cfb6a5b009a1d6058) {     [SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_PRESENT](#add553da0fb80ee2cfb6a5b009a1d6058ac65dd6d01c5995c1f0514daaded1c283) = SENSOR\_ATTR\_PRIV\_START , [SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_CUR\_LIMIT](#add553da0fb80ee2cfb6a5b009a1d6058a3faad43b78763a2520e9a87baf38265b) , [SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_OVERVLT\_PROT](#add553da0fb80ee2cfb6a5b009a1d6058a5674d4ecc2377640a42fc78fef60c0ab) , [SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_UNDERVLT](#add553da0fb80ee2cfb6a5b009a1d6058addc2f6fbe32fd3bdadeb6c5d3aa00a08) ,     [SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_SUSPENDED](#add553da0fb80ee2cfb6a5b009a1d6058a7e1153a7eeb8e02925d0ee57c79b8a31) , [SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_BUSOUT](#add553da0fb80ee2cfb6a5b009a1d6058abb429313846ec7adbf09d84b5385e2bc)   } |

## Enumeration Type Documentation

## [◆ ](#add553da0fb80ee2cfb6a5b009a1d6058)sensor\_attribute\_npm13xx\_charger

| enum [sensor\_attribute\_npm13xx\_charger](#add553da0fb80ee2cfb6a5b009a1d6058) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_PRESENT |  |
| SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_CUR\_LIMIT |  |
| SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_OVERVLT\_PROT |  |
| SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_UNDERVLT |  |
| SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_SUSPENDED |  |
| SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_BUSOUT |  |

## [◆ ](#a3b5c9edfeb25c77685d67babdc4c5299)sensor\_channel\_npm13xx\_charger

| enum [sensor\_channel\_npm13xx\_charger](#a3b5c9edfeb25c77685d67babdc4c5299) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_CHAN\_NPM13XX\_CHARGER\_STATUS |  |
| SENSOR\_CHAN\_NPM13XX\_CHARGER\_ERROR |  |
| SENSOR\_CHAN\_NPM13XX\_CHARGER\_VBUS\_STATUS |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [npm13xx\_charger.h](npm13xx__charger_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
