---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/adc__emul_8h.html
original_path: doxygen/html/adc__emul_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc\_emul.h File Reference

Backend API for emulated ADC.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/drivers/adc.h](drivers_2adc_8h_source.md)>`

[Go to the source code of this file.](adc__emul_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef int(\* | [adc\_emul\_value\_func](group__adc__emul.md#ga8047a2a3700e085df84dc1dbc2ca155f)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int chan, void \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
|  | Type definition of the function which is used to obtain ADC mV input values. |

| Functions | |
| --- | --- |
| int | [adc\_emul\_const\_value\_set](group__adc__emul.md#ga564c588b71ec63aedb32f0c6221abd69) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int chan, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Set constant mV value input for emulated ADC `chan`. |
| int | [adc\_emul\_value\_func\_set](group__adc__emul.md#gae5036c155341dd61d37558c311d3c554) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int chan, [adc\_emul\_value\_func](group__adc__emul.md#ga8047a2a3700e085df84dc1dbc2ca155f) func, void \*data) |
|  | Set function used to obtain voltage for input of emulated ADC `chan`. |
| int | [adc\_emul\_ref\_voltage\_set](group__adc__emul.md#ga53179798ec576b329927e5b6c845aa04) (const struct [device](structdevice.md) \*dev, enum [adc\_reference](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56) ref, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value) |
|  | Set reference voltage. |

## Detailed Description

Backend API for emulated ADC.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [adc\_emul.h](adc__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
