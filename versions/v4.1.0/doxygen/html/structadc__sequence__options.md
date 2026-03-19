---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structadc__sequence__options.html
original_path: doxygen/html/structadc__sequence__options.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc\_sequence\_options Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [ADC driver APIs](group__adc__interface.md)

Structure defining additional options for an ADC sampling sequence.
[More...](#details)

`#include <[adc.h](drivers_2adc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [interval\_us](#ad2f11727ab0eb7e32a5fbd07f04a85b2) |
|  | Interval between consecutive samplings (in microseconds), 0 means sample as fast as possible, without involving any timer. |
| [adc\_sequence\_callback](group__adc__interface.md#ga9150eb6dc53d1c62b9fa225c0a371d6d) | [callback](#a71bd082c14f01a1b5d1b491e7510aa91) |
|  | Callback function to be called after each sampling is done. |
| void \* | [user\_data](#a262fd6daefb22df02c726aafcddc6d47) |
|  | Pointer to user data. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [extra\_samplings](#a29f8ac4cdf6740f56bcd70a0a027e56a) |
|  | Number of extra samplings to perform (the total number of samplings is 1 + extra\_samplings). |

## Detailed Description

Structure defining additional options for an ADC sampling sequence.

## Field Documentation

## [◆ ](#a71bd082c14f01a1b5d1b491e7510aa91)callback

| [adc\_sequence\_callback](group__adc__interface.md#ga9150eb6dc53d1c62b9fa225c0a371d6d) adc\_sequence\_options::callback |
| --- |

Callback function to be called after each sampling is done.

Optional - set to NULL if it is not needed.

## [◆ ](#a29f8ac4cdf6740f56bcd70a0a027e56a)extra\_samplings

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) adc\_sequence\_options::extra\_samplings |
| --- |

Number of extra samplings to perform (the total number of samplings is 1 + extra\_samplings).

## [◆ ](#ad2f11727ab0eb7e32a5fbd07f04a85b2)interval\_us

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) adc\_sequence\_options::interval\_us |
| --- |

Interval between consecutive samplings (in microseconds), 0 means sample as fast as possible, without involving any timer.

The accuracy of this interval is dependent on the implementation of a given driver. The default routine that handles the intervals uses a kernel timer for this purpose, thus, it has the accuracy of the kernel's system clock. Particular drivers may use some dedicated hardware timers and achieve a better precision.

## [◆ ](#a262fd6daefb22df02c726aafcddc6d47)user\_data

| void\* adc\_sequence\_options::user\_data |
| --- |

Pointer to user data.

It can be used to associate the sequence with any other data that is needed in the callback function.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[adc.h](drivers_2adc_8h_source.md)

- [adc\_sequence\_options](structadc__sequence__options.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
