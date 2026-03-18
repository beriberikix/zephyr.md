---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__adc__emul.html
original_path: doxygen/html/group__adc__emul.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Emulated ADC

[Device Driver APIs](group__io__interfaces.md) » [ADC driver APIs](group__adc__interface.md)

Emulated ADC backend API.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef int(\* | [adc\_emul\_value\_func](#ga8047a2a3700e085df84dc1dbc2ca155f)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int chan, void \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
|  | Type definition of the function which is used to obtain ADC mV input values. |

| Functions | |
| --- | --- |
| int | [adc\_emul\_const\_value\_set](#ga564c588b71ec63aedb32f0c6221abd69) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int chan, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Set constant mV value input for emulated ADC `chan`. |
| int | [adc\_emul\_value\_func\_set](#gae5036c155341dd61d37558c311d3c554) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int chan, [adc\_emul\_value\_func](#ga8047a2a3700e085df84dc1dbc2ca155f) func, void \*data) |
|  | Set function used to obtain voltage for input of emulated ADC `chan`. |
| int | [adc\_emul\_ref\_voltage\_set](#ga53179798ec576b329927e5b6c845aa04) (const struct [device](structdevice.md) \*dev, enum [adc\_reference](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56) ref, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value) |
|  | Set reference voltage. |

## Detailed Description

Emulated ADC backend API.

Behaviour of emulated ADC is application-defined. As-such, each application may

- define a Device Tree overlay file to indicate the number of ADC controllers as well as the number of channels for each controller
- set default reference voltages in Device Tree or using [adc\_emul\_ref\_voltage\_set](#ga53179798ec576b329927e5b6c845aa04)
- asynchronously call [adc\_emul\_const\_value\_set](#ga564c588b71ec63aedb32f0c6221abd69) in order to set constant mV value on emulated ADC input
- asynchronously call [adc\_emul\_value\_func\_set](#gae5036c155341dd61d37558c311d3c554) in order to assign function which will be used to obtain voltage on emulated ADC input

An example of an appropriate Device Tree overlay file is in tests/drivers/adc/adc\_api/boards/native\_sim.overlay

An example of using emulated ADC backend API is in the file tests/drivers/adc/adc\_emul/src/main.c

## Typedef Documentation

## [◆ ](#ga8047a2a3700e085df84dc1dbc2ca155f)adc\_emul\_value\_func

| typedef int(\* adc\_emul\_value\_func) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int chan, void \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
| --- |

`#include <[adc_emul.h](adc__emul_8h.md)>`

Type definition of the function which is used to obtain ADC mV input values.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | chan | ADC channel to sample |
    | data | User data which was passed on [adc\_emul\_value\_func\_set](#gae5036c155341dd61d37558c311d3c554) |
    | result | The result value which will be set as input for ADC `chan` |

Returns
:   0 on success
:   other as error code which ends ADC context

## Function Documentation

## [◆ ](#ga564c588b71ec63aedb32f0c6221abd69)adc\_emul\_const\_value\_set()

| int adc\_emul\_const\_value\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *chan*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *value* ) |

`#include <[adc_emul.h](adc__emul_8h.md)>`

Set constant mV value input for emulated ADC `chan`.

Parameters
:   | dev | The emulated ADC device |
    | --- | --- |
    | chan | The channel of ADC which input is assigned |
    | value | New voltage in mV to assign to `chan` input |

Returns
:   0 on success
:   -EINVAL if an invalid argument is provided

## [◆ ](#ga53179798ec576b329927e5b6c845aa04)adc\_emul\_ref\_voltage\_set()

| int adc\_emul\_ref\_voltage\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [adc\_reference](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56) | *ref*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *value* ) |

`#include <[adc_emul.h](adc__emul_8h.md)>`

Set reference voltage.

Parameters
:   | dev | The emulated ADC device |
    | --- | --- |
    | ref | Reference config which is changed |
    | value | New reference voltage in mV |

Returns
:   0 on success
:   -EINVAL if an invalid argument is provided

## [◆ ](#gae5036c155341dd61d37558c311d3c554)adc\_emul\_value\_func\_set()

| int adc\_emul\_value\_func\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *chan*, |
|  |  | [adc\_emul\_value\_func](#ga8047a2a3700e085df84dc1dbc2ca155f) | *func*, |
|  |  | void \* | *data* ) |

`#include <[adc_emul.h](adc__emul_8h.md)>`

Set function used to obtain voltage for input of emulated ADC `chan`.

Parameters
:   | dev | The emulated ADC device |
    | --- | --- |
    | chan | The channel of ADC to which `func` is assigned |
    | func | New function to assign to `chan` |
    | data | Pointer to data passed to `func` on call |

Returns
:   0 on success
:   -EINVAL if an invalid argument is provided

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
