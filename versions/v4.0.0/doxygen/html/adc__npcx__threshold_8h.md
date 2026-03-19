---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/adc__npcx__threshold_8h.html
original_path: doxygen/html/adc__npcx__threshold_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc\_npcx\_threshold.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](adc__npcx__threshold_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [adc\_npcx\_threshold\_param](structadc__npcx__threshold__param.md) |

| Enumerations | |
| --- | --- |
| enum | [adc\_npcx\_threshold\_param\_l\_h](#a38f7d862a13c7894b71ff6750ab56eec) { [ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H\_HIGHER](#a38f7d862a13c7894b71ff6750ab56eeca7f0b6e9c183da7426bee511d71622ce6) , [ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H\_LOWER](#a38f7d862a13c7894b71ff6750ab56eeca66fe94a1fc6250b615a49bc282ec31b2) } |
| enum | [adc\_npcx\_threshold\_param\_type](#a7da5b595bef1edfb12ad8223fb7fc461) {     [ADC\_NPCX\_THRESHOLD\_PARAM\_CHNSEL](#a7da5b595bef1edfb12ad8223fb7fc461ab00b9cf39929edf5221af6bf147fb79b) , [ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H](#a7da5b595bef1edfb12ad8223fb7fc461ad5183bef3339ba7ee07f32c34e7d7713) , [ADC\_NPCX\_THRESHOLD\_PARAM\_THVAL](#a7da5b595bef1edfb12ad8223fb7fc461ae260faa6cb77b1466898a47de1cc35eb) , [ADC\_NPCX\_THRESHOLD\_PARAM\_WORK](#a7da5b595bef1edfb12ad8223fb7fc461a20f6e3a525932decdedae74b73ce62b3) ,     [ADC\_NPCX\_THRESHOLD\_PARAM\_MAX](#a7da5b595bef1edfb12ad8223fb7fc461a61da0191e7147c0634a954ba543f1004)   } |

| Functions | |
| --- | --- |
| int | [adc\_npcx\_threshold\_mv\_to\_thrval](#ad0d9a6c968a0699e270d07cb35a54834) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val\_mv, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*thrval) |
|  | Convert input value in millivolts to corresponding threshold register value. |
| int | [adc\_npcx\_threshold\_ctrl\_set\_param](#a8cb8e7d8947eaae2503e742cbd747f7f) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) th\_sel, const struct [adc\_npcx\_threshold\_param](structadc__npcx__threshold__param.md) \*param) |
|  | Set ADC threshold parameter. |
| int | [adc\_npcx\_threshold\_ctrl\_enable](#acd6441b45603ce1b3766a0ef24ffbe69) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) th\_sel, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enables/Disables ADC threshold interruption. |

## Enumeration Type Documentation

## [◆ ](#a38f7d862a13c7894b71ff6750ab56eec)adc\_npcx\_threshold\_param\_l\_h

| enum [adc\_npcx\_threshold\_param\_l\_h](#a38f7d862a13c7894b71ff6750ab56eec) |
| --- |

| Enumerator | |
| --- | --- |
| ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H\_HIGHER |  |
| ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H\_LOWER |  |

## [◆ ](#a7da5b595bef1edfb12ad8223fb7fc461)adc\_npcx\_threshold\_param\_type

| enum [adc\_npcx\_threshold\_param\_type](#a7da5b595bef1edfb12ad8223fb7fc461) |
| --- |

| Enumerator | |
| --- | --- |
| ADC\_NPCX\_THRESHOLD\_PARAM\_CHNSEL |  |
| ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H |  |
| ADC\_NPCX\_THRESHOLD\_PARAM\_THVAL |  |
| ADC\_NPCX\_THRESHOLD\_PARAM\_WORK |  |
| ADC\_NPCX\_THRESHOLD\_PARAM\_MAX |  |

## Function Documentation

## [◆ ](#acd6441b45603ce1b3766a0ef24ffbe69)adc\_npcx\_threshold\_ctrl\_enable()

| int adc\_npcx\_threshold\_ctrl\_enable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *th\_sel*, |
|  |  | const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

Enables/Disables ADC threshold interruption.

Note
:   This function is available only if

    ```
    CONFIG_ADC_CMP_NPCX
    ```

    is selected.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | th\_sel | Threshold selected. |
    | enable | Enable or disables threshold interruption. |

Returns
:   0 on success, negative error code otherwise. all parameters must be configure prior enabling threshold interruption, otherwise error will be returned.

## [◆ ](#a8cb8e7d8947eaae2503e742cbd747f7f)adc\_npcx\_threshold\_ctrl\_set\_param()

| int adc\_npcx\_threshold\_ctrl\_set\_param | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *th\_sel*, |
|  |  | const struct [adc\_npcx\_threshold\_param](structadc__npcx__threshold__param.md) \* | *param* ) |

Set ADC threshold parameter.

Note
:   This function is available only if

    ```
    CONFIG_ADC_CMP_NPCX
    ```

    is selected.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | th\_sel | Threshold selected. |
    | param | Pointer of parameter structure. See struct [adc\_npcx\_threshold\_param](structadc__npcx__threshold__param.md) for supported parameters. |

Returns
:   0 on success, negative error code otherwise.

## [◆ ](#ad0d9a6c968a0699e270d07cb35a54834)adc\_npcx\_threshold\_mv\_to\_thrval()

| int adc\_npcx\_threshold\_mv\_to\_thrval | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val\_mv*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *thrval* ) |

Convert input value in millivolts to corresponding threshold register value.

Note
:   This function is available only if

    ```
    CONFIG_ADC_CMP_NPCX
    ```

    is selected.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | val\_mv | Input value in millivolts to be converted. |
    | thrval | Pointer of variable to hold the result of conversion. |

Returns
:   0 on success, negative result if input cannot be converted due to overflow.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [adc\_npcx\_threshold.h](adc__npcx__threshold_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
