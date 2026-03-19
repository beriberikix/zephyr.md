---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcharger__current__notifier.html
original_path: doxygen/html/structcharger__current__notifier.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

charger\_current\_notifier Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Charger Interface](group__charger__interface.md)

The input current thresholds for the charger to notify the system.
[More...](#details)

`#include <[charger.h](charger_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [severity](#a22c26477263e5abedb200de36a29d9de) |
|  | The severity of the notification where CHARGER\_SEVERITY\_PEAK is the most severe. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [current\_ua](#acb54706bf47f55e197e799393b9eb87e) |
|  | The current threshold to be exceeded. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [duration\_us](#a4998999ef893d18fa64b86ec4fd9ad94) |
|  | The duration of excess current before notifying the system. |

## Detailed Description

The input current thresholds for the charger to notify the system.

## Field Documentation

## [◆ ](#acb54706bf47f55e197e799393b9eb87e)current\_ua

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) charger\_current\_notifier::current\_ua |
| --- |

The current threshold to be exceeded.

## [◆ ](#a4998999ef893d18fa64b86ec4fd9ad94)duration\_us

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) charger\_current\_notifier::duration\_us |
| --- |

The duration of excess current before notifying the system.

## [◆ ](#a22c26477263e5abedb200de36a29d9de)severity

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) charger\_current\_notifier::severity |
| --- |

The severity of the notification where CHARGER\_SEVERITY\_PEAK is the most severe.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[charger.h](charger_8h_source.md)

- [charger\_current\_notifier](structcharger__current__notifier.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
