---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structadc__channel__cfg.html
original_path: doxygen/html/structadc__channel__cfg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc\_channel\_cfg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [ADC driver APIs](group__adc__interface.md)

Structure for specifying the configuration of an ADC channel.
[More...](#details)

`#include <[adc.h](drivers_2adc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) | [gain](#a20996396fa5b1d27eeea7da9ea9df848) |
|  | Gain selection. |
| enum [adc\_reference](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56) | [reference](#a73d11ad6411a62f8f21cbfa492bc1b20) |
|  | Reference selection. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [acquisition\_time](#a426a74cf53a4b801e91c2eeb1db3477d) |
|  | Acquisition time. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel\_id](#aeec90a3fb60f93427a92e083326c8fcf): 5 |
|  | Channel identifier. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [differential](#a372f298a2dd87660b9508ca1387084b6): 1 |
|  | Channel type: single-ended or differential. |

## Detailed Description

Structure for specifying the configuration of an ADC channel.

## Field Documentation

## [◆ ](#a426a74cf53a4b801e91c2eeb1db3477d)acquisition\_time

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) adc\_channel\_cfg::acquisition\_time |
| --- |

Acquisition time.

Use the ADC\_ACQ\_TIME macro to compose the value for this field or pass ADC\_ACQ\_TIME\_DEFAULT to use the default setting for a given hardware (e.g. when the hardware does not allow to configure the acquisition time). Particular drivers do not necessarily support all the possible units. Value range is 0-16383 for a given unit.

## [◆ ](#aeec90a3fb60f93427a92e083326c8fcf)channel\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adc\_channel\_cfg::channel\_id |
| --- |

Channel identifier.

This value primarily identifies the channel within the ADC API - when a read request is done, the corresponding bit in the "channels" field of the "adc\_sequence" structure must be set to include this channel in the sampling. For hardware that does not allow selection of analog inputs for given channels, but rather have dedicated ones, this value also selects the physical ADC input to be used in the sampling. Otherwise, when it is needed to explicitly select an analog input for the channel, or two inputs when the channel is a differential one, the selection is done in "input\_positive" and "input\_negative" fields. Particular drivers indicate which one of the above two cases they support by selecting or not a special hidden Kconfig option named ADC\_CONFIGURABLE\_INPUTS. If this option is not selected, the macro CONFIG\_ADC\_CONFIGURABLE\_INPUTS is not defined and consequently the mentioned two fields are not present in this structure. While this API allows identifiers from range 0-31, particular drivers may support only a limited number of channel identifiers (dependent on the underlying hardware capabilities or configured via a dedicated Kconfig option).

## [◆ ](#a372f298a2dd87660b9508ca1387084b6)differential

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adc\_channel\_cfg::differential |
| --- |

Channel type: single-ended or differential.

## [◆ ](#a20996396fa5b1d27eeea7da9ea9df848)gain

| enum [adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) adc\_channel\_cfg::gain |
| --- |

Gain selection.

## [◆ ](#a73d11ad6411a62f8f21cbfa492bc1b20)reference

| enum [adc\_reference](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56) adc\_channel\_cfg::reference |
| --- |

Reference selection.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[adc.h](drivers_2adc_8h_source.md)

- [adc\_channel\_cfg](structadc__channel__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
