---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2adc_8h.html
original_path: doxygen/html/drivers_2adc_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc.h File Reference

ADC public API header file.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/dt-bindings/adc/adc.h](dt-bindings_2adc_2adc_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <syscalls/adc.h>`

[Go to the source code of this file.](drivers_2adc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [adc\_channel\_cfg](structadc__channel__cfg.md) |
|  | Structure for specifying the configuration of an ADC channel. [More...](structadc__channel__cfg.md#details) |
| struct | [adc\_dt\_spec](structadc__dt__spec.md) |
|  | Container for ADC channel information specified in devicetree. [More...](structadc__dt__spec.md#details) |
| struct | [adc\_sequence\_options](structadc__sequence__options.md) |
|  | Structure defining additional options for an ADC sampling sequence. [More...](structadc__sequence__options.md#details) |
| struct | [adc\_sequence](structadc__sequence.md) |
|  | Structure defining an ADC sampling sequence. [More...](structadc__sequence.md#details) |
| struct | [adc\_driver\_api](structadc__driver__api.md) |
|  | ADC driver API. [More...](structadc__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [ADC\_CHANNEL\_CFG\_DT](group__adc__interface.md#ga8d1f7d55c94fed3247c830a4569ab05e)(node\_id) |
|  | Get ADC channel configuration from a given devicetree node. |
| #define | [ADC\_DT\_SPEC\_GET\_BY\_IDX](group__adc__interface.md#gae9867df7a034d45ed3d3c58c69c246ed)(node\_id, idx) |
|  | Get ADC io-channel information from devicetree. |
| #define | [ADC\_DT\_SPEC\_INST\_GET\_BY\_IDX](group__adc__interface.md#ga4705a1e2cc22fe73b7e967e8ba220584)(inst, idx) |
|  | Get ADC io-channel information from a DT\_DRV\_COMPAT devicetree instance. |
| #define | [ADC\_DT\_SPEC\_GET](group__adc__interface.md#gad05df3d329ba785c094ea4c32e2913b7)(node\_id) |
|  | Equivalent to [ADC\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)](group__adc__interface.md#gae9867df7a034d45ed3d3c58c69c246ed "Get ADC io-channel information from devicetree."). |
| #define | [ADC\_DT\_SPEC\_INST\_GET](group__adc__interface.md#ga96222a7d374e21d477b99f74d715bae1)(inst) |
|  | Equivalent to [ADC\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)](group__adc__interface.md#ga4705a1e2cc22fe73b7e967e8ba220584 "Get ADC io-channel information from a DT_DRV_COMPAT devicetree instance."). |

| Typedefs | |
| --- | --- |
| typedef enum [adc\_action](group__adc__interface.md#ga8f6df993405679f852ae4cd8c63c6917)(\* | [adc\_sequence\_callback](group__adc__interface.md#ga9150eb6dc53d1c62b9fa225c0a371d6d)) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sampling\_index) |
|  | Type definition of the optional callback function to be called after a requested sampling is done. |
| typedef int(\* | [adc\_api\_channel\_setup](group__adc__interface.md#ga871680cf9f390bfe19a10a61eb1ca092)) (const struct [device](structdevice.md) \*dev, const struct [adc\_channel\_cfg](structadc__channel__cfg.md) \*channel\_cfg) |
|  | Type definition of ADC API function for configuring a channel. |
| typedef int(\* | [adc\_api\_read](group__adc__interface.md#ga4d4484e52ff7727fd316f50b2f404adf)) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence) |
|  | Type definition of ADC API function for setting a read request. |
| typedef int(\* | [adc\_api\_read\_async](group__adc__interface.md#gad0160f455d1901ebfe06568e8418a22c)) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence, struct [k\_poll\_signal](structk__poll__signal.md) \*async) |
|  | Type definition of ADC API function for setting an asynchronous read request. |

| Enumerations | |
| --- | --- |
| enum | [adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) {     [ADC\_GAIN\_1\_6](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0abb26700162bfc68a2beadc1e78b758c1) , [ADC\_GAIN\_1\_5](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a198c40369bddfc3c0eaa8ae3bb1be0c9) , [ADC\_GAIN\_1\_4](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0afa55c5a94bfebb9a70638e9ab32eabf8) , [ADC\_GAIN\_1\_3](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0af896fe01119930815ac78a4ee87635ee) ,     [ADC\_GAIN\_2\_5](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a4a59d3dd1e2e2fbe2ec593291ca307e0) , [ADC\_GAIN\_1\_2](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a2d36559128c21834d1188aed43d236d2) , [ADC\_GAIN\_2\_3](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ac720b0730cfef7c55f97777fec75dc62) , [ADC\_GAIN\_4\_5](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ad0ee4a6bfc749a3213f0c44d30e8e6df) ,     [ADC\_GAIN\_1](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a76b3097b0b38d33266d36f5a5d534e54) , [ADC\_GAIN\_2](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0aff4b7cc577e333a3a684e4e56b124868) , [ADC\_GAIN\_3](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a113a3324782a4517bb71fc3b03aeef5e) , [ADC\_GAIN\_4](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a12756ff0f6a345ff3fee2077e1153300) ,     [ADC\_GAIN\_6](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0aba255a08f5ff25388778057d725a77c8) , [ADC\_GAIN\_8](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ae9a429f8b69dd0e5cae0e1ab7dbe7dc3) , [ADC\_GAIN\_12](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a3ff31845095f2b0fe7e62b2b826411e8) , [ADC\_GAIN\_16](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a4b18ba08d86e630f2deeeea5b329f970) ,     [ADC\_GAIN\_24](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a5d19226b1d1728180101e65b8386ff33) , [ADC\_GAIN\_32](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ac693403ea0f70f5723a98fe11967c13f) , [ADC\_GAIN\_64](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a064c567978a50dd58d48d481388dd6eb) , [ADC\_GAIN\_128](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a1b3c6d80db15acf962192341d4754829)   } |
|  | ADC channel gain factors. [More...](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) |
| enum | [adc\_reference](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56) {     [ADC\_REF\_VDD\_1](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56ae41651d9d2ba0d3c2a976177fc6ed1b3) , [ADC\_REF\_VDD\_1\_2](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a5f47fb0b239da79577887baf2576eb0d) , [ADC\_REF\_VDD\_1\_3](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a8e5dfe37c3993e118d6e316c9fa0aad1) , [ADC\_REF\_VDD\_1\_4](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a93d4dc4332b3346a7332383ecf745d2c) ,     [ADC\_REF\_INTERNAL](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a239921743b35d32a558a43deee2ce709) , [ADC\_REF\_EXTERNAL0](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56afc15362bdf426f412e150ae9f8d224e6) , [ADC\_REF\_EXTERNAL1](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a2733819da753b01a8116d076498fe52a)   } |
|  | ADC references. [More...](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56) |
| enum | [adc\_action](group__adc__interface.md#ga8f6df993405679f852ae4cd8c63c6917) { [ADC\_ACTION\_CONTINUE](group__adc__interface.md#gga8f6df993405679f852ae4cd8c63c6917ac875a64d997cb883b49447006554ba92) = 0 , [ADC\_ACTION\_REPEAT](group__adc__interface.md#gga8f6df993405679f852ae4cd8c63c6917a8efc10c77ea616d568f88d3ef88b1715) , [ADC\_ACTION\_FINISH](group__adc__interface.md#gga8f6df993405679f852ae4cd8c63c6917a68a21759522a3d584417fa12359b4dc9) } |
|  | Action to be performed after a sampling is done. [More...](group__adc__interface.md#ga8f6df993405679f852ae4cd8c63c6917) |

| Functions | |
| --- | --- |
| int | [adc\_gain\_invert](group__adc__interface.md#ga5af65795f58e8e92672bf31dc2418e23) (enum [adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) gain, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value) |
|  | Invert the application of gain to a measurement value. |
| int | [adc\_channel\_setup](group__adc__interface.md#ga7bc0488b2d08ae2ee4996c0eed11f0bf) (const struct [device](structdevice.md) \*dev, const struct [adc\_channel\_cfg](structadc__channel__cfg.md) \*channel\_cfg) |
|  | Configure an ADC channel. |
| static int | [adc\_channel\_setup\_dt](group__adc__interface.md#gaec29595ff149508847c51f14c41a5bad) (const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec) |
|  | Configure an ADC channel from a struct [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree."). |
| int | [adc\_read](group__adc__interface.md#ga7567ce3b03ebb294620b4e32b7561ab3) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence) |
|  | Set a read request. |
| static int | [adc\_read\_dt](group__adc__interface.md#ga303a57dfd56f0870c62ba203483e96aa) (const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec, const struct [adc\_sequence](structadc__sequence.md) \*sequence) |
|  | Set a read request from a struct [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree."). |
| int | [adc\_read\_async](group__adc__interface.md#ga009e3733b5b20eb6b26a201c9f9734fc) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence, struct [k\_poll\_signal](structk__poll__signal.md) \*async) |
|  | Set an asynchronous read request. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [adc\_ref\_internal](group__adc__interface.md#gad11845f5621d0b0d03da4b6484d79aa4) (const struct [device](structdevice.md) \*dev) |
|  | Get the internal reference voltage. |
| static int | [adc\_raw\_to\_millivolts](group__adc__interface.md#gaef98dabea3e0dc1cef8add298171a950) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ref\_mv, enum [adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) gain, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) resolution, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*valp) |
|  | Convert a raw ADC value to millivolts. |
| static int | [adc\_raw\_to\_millivolts\_dt](group__adc__interface.md#ga11cf9c8f345a83f66704af83a2a26911) (const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*valp) |
|  | Convert a raw ADC value to millivolts using information stored in a struct [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree."). |
| static int | [adc\_sequence\_init\_dt](group__adc__interface.md#ga5629d37dde5eb43faa93f4d167333f94) (const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec, struct [adc\_sequence](structadc__sequence.md) \*seq) |
|  | Initialize a struct [adc\_sequence](structadc__sequence.md "Structure defining an ADC sampling sequence.") from information stored in struct [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree."). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [adc\_is\_ready\_dt](group__adc__interface.md#ga37412f10ad2c4874e4cce0d5fa8599a0) (const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec) |
|  | Validate that the ADC device is ready. |

## Detailed Description

ADC public API header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc.h](drivers_2adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
