---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cc13xx__cc26xx-pinctrl_8h.html
original_path: doxygen/html/cc13xx__cc26xx-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cc13xx\_cc26xx-pinctrl.h File Reference

[Go to the source code of this file.](cc13xx__cc26xx-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IOC\_PORT\_GPIO](#a28f8e101ae30e86989a5c7b35be8f2d1)   0x00000000 /\* Default general purpose IO usage \*/ |
| #define | [IOC\_PORT\_AON\_CLK32K](#a2dade73b9db2292ee357ec1ae92ed2d0)   0x00000007 /\* AON External 32kHz clock \*/ |
| #define | [IOC\_PORT\_AUX\_IO](#a1b04b35124c351075fe3974adeb4d9aa)   0x00000008 /\* AUX IO Pin \*/ |
| #define | [IOC\_PORT\_MCU\_SSI0\_RX](#a3ee91cd12de013161c91f231676b279c)   0x00000009 /\* MCU SSI0 Receive Pin \*/ |
| #define | [IOC\_PORT\_MCU\_SSI0\_TX](#a984735dec2b09061ab1be699a708367f)   0x0000000A /\* MCU SSI0 Transmit Pin \*/ |
| #define | [IOC\_PORT\_MCU\_SSI0\_FSS](#a5e72bbc3a52d1bd643059f9a2037db03)   0x0000000B /\* MCU SSI0 FSS Pin \*/ |
| #define | [IOC\_PORT\_MCU\_SSI0\_CLK](#acfeabd6ba536f550b52c98eba600f99c)   0x0000000C /\* MCU SSI0 Clock Pin \*/ |
| #define | [IOC\_PORT\_MCU\_I2C\_MSSDA](#aa318c337f1371b5f81ebf427a43cf318)   0x0000000D /\* MCU I2C Data Pin \*/ |
| #define | [IOC\_PORT\_MCU\_I2C\_MSSCL](#a7d3e1312e3803326770e4d734e25b2eb)   0x0000000E /\* MCU I2C Clock Pin \*/ |
| #define | [IOC\_PORT\_MCU\_UART0\_RX](#aab1fbb3fbc8a90bd4d8fb1b55f69eb44)   0x0000000F /\* MCU UART0 Receive Pin \*/ |
| #define | [IOC\_PORT\_MCU\_UART0\_TX](#ac1adc319c3a412383fbd03d4dc9f08f5)   0x00000010 /\* MCU UART0 Transmit Pin \*/ |
| #define | [IOC\_PORT\_MCU\_UART0\_CTS](#ad86b00b6011d22d55d31c8c2681edea8)   0x00000011 /\* MCU UART0 Clear To Send Pin \*/ |
| #define | [IOC\_PORT\_MCU\_UART0\_RTS](#acdc4b3216e14a0525a9bff563c618505)   0x00000012 /\* MCU UART0 Request To Send Pin \*/ |
| #define | [IOC\_PORT\_MCU\_UART1\_RX](#a81eb684c41b27ab5c2e434f74cac653a)   0x00000013 /\* MCU UART1 Receive Pin \*/ |
| #define | [IOC\_PORT\_MCU\_UART1\_TX](#aabad6396786ac0fba4e030fa3bafaebe)   0x00000014 /\* MCU UART1 Transmit Pin \*/ |
| #define | [IOC\_PORT\_MCU\_UART1\_CTS](#a3891eea57014086f4d9665c5659df9f9)   0x00000015 /\* MCU UART1 Clear To Send Pin \*/ |
| #define | [IOC\_PORT\_MCU\_UART1\_RTS](#a07f27135f53b5f70c9cf611fee1da81c)   0x00000016 /\* MCU UART1 Request To Send Pin \*/ |
| #define | [IOC\_PORT\_MCU\_PORT\_EVENT0](#abb2e44fdb358359785db59197e43bf77)   0x00000017 /\* MCU PORT EVENT 0 \*/ |
| #define | [IOC\_PORT\_MCU\_PORT\_EVENT1](#a53158c583bdc22b05a3ab803976f86f3)   0x00000018 /\* MCU PORT EVENT 1 \*/ |
| #define | [IOC\_PORT\_MCU\_PORT\_EVENT2](#a3c31d2aee7d57f0b939678d24489b288)   0x00000019 /\* MCU PORT EVENT 2 \*/ |
| #define | [IOC\_PORT\_MCU\_PORT\_EVENT3](#af74865ea575600cdef510d96b765fcaa)   0x0000001A /\* MCU PORT EVENT 3 \*/ |
| #define | [IOC\_PORT\_MCU\_PORT\_EVENT4](#a8c29bb202c04366637a067403cb04798)   0x0000001B /\* MCU PORT EVENT 4 \*/ |
| #define | [IOC\_PORT\_MCU\_PORT\_EVENT5](#a5018eb7bb384ce6240bc5ce37f684fd4)   0x0000001C /\* MCU PORT EVENT 5 \*/ |
| #define | [IOC\_PORT\_MCU\_PORT\_EVENT6](#a627f8281323ce4d84edc61c921e5fc35)   0x0000001D /\* MCU PORT EVENT 6 \*/ |
| #define | [IOC\_PORT\_MCU\_PORT\_EVENT7](#ae058c9773b968e08c17f848e8a17e33e)   0x0000001E /\* MCU PORT EVENT 7 \*/ |
| #define | [IOC\_PORT\_MCU\_SWV](#a5bf13b897900e2f62c82d84d23558c9b)   0x00000020 /\* Serial Wire Viewer \*/ |
| #define | [IOC\_PORT\_MCU\_SSI1\_RX](#adc4c2aa534badaa6a40a994012968226)   0x00000021 /\* MCU SSI1 Receive Pin \*/ |
| #define | [IOC\_PORT\_MCU\_SSI1\_TX](#a9024a0c4d78a72ff56c12d9ef6bce984)   0x00000022 /\* MCU SSI1 Transmit Pin \*/ |
| #define | [IOC\_PORT\_MCU\_SSI1\_FSS](#a8517079f7b23895467d0c6c5cee74051)   0x00000023 /\* MCU SSI1 FSS Pin \*/ |
| #define | [IOC\_PORT\_MCU\_SSI1\_CLK](#aa657dc9b3b551a535207a5c70944c7ad)   0x00000024 /\* MCU SSI1 Clock Pin \*/ |
| #define | [IOC\_PORT\_MCU\_I2S\_AD0](#ad8d7633125f181d03a832504ca0333af)   0x00000025 /\* MCU I2S Data Pin 0 \*/ |
| #define | [IOC\_PORT\_MCU\_I2S\_AD1](#a3e3c593f43d20f8b976104e4370e2bfe)   0x00000026 /\* MCU I2S Data Pin 1 \*/ |
| #define | [IOC\_PORT\_MCU\_I2S\_WCLK](#a87f51f7808c53fb7a1d0ab0cfc7c3bfb)   0x00000027 /\* MCU I2S Frame/Word Clock \*/ |
| #define | [IOC\_PORT\_MCU\_I2S\_BCLK](#a27b5fe5cdbd768684939c52662ed919a)   0x00000028 /\* MCU I2S Bit Clock \*/ |
| #define | [IOC\_PORT\_MCU\_I2S\_MCLK](#a72287ec0a2c5f0423e785d3e371a120e)   0x00000029 /\* MCU I2S Master clock 2 \*/ |
| #define | [IOC\_PORT\_RFC\_TRC](#ae6a1e66015d48324657ede92613381be)   0x0000002E /\* RF Core Tracer \*/ |
| #define | [IOC\_PORT\_RFC\_GPO0](#a00a019e1ddf52b2913e8358c18095ed4)   0x0000002F /\* RC Core Data Out Pin 0 \*/ |
| #define | [IOC\_PORT\_RFC\_GPO1](#a00ea75c9456ac6b11e666757750ae342)   0x00000030 /\* RC Core Data Out Pin 1 \*/ |
| #define | [IOC\_PORT\_RFC\_GPO2](#a5f19fce0ef7c834714af2e7f1c2bd06d)   0x00000031 /\* RC Core Data Out Pin 2 \*/ |
| #define | [IOC\_PORT\_RFC\_GPO3](#ac940779073013ae6912da19fe598d999)   0x00000032 /\* RC Core Data Out Pin 3 \*/ |
| #define | [IOC\_PORT\_RFC\_GPI0](#af0c7ce805a62bed97029d997406e8ec7)   0x00000033 /\* RC Core Data In Pin 0 \*/ |
| #define | [IOC\_PORT\_RFC\_GPI1](#a6f1fc00a44a3311866187ce0c7470b1f)   0x00000034 /\* RC Core Data In Pin 1 \*/ |
| #define | [IOC\_PORT\_RFC\_SMI\_DL\_OUT](#a34286b14818f96f8e3955eebc3f453eb)   0x00000035 /\* RF Core SMI Data Link Out \*/ |
| #define | [IOC\_PORT\_RFC\_SMI\_DL\_IN](#a38268821c556568eb9b8d0bd1b6bf4a4)   0x00000036 /\* RF Core SMI Data Link in \*/ |
| #define | [IOC\_PORT\_RFC\_SMI\_CL\_OUT](#a8fa600a45bb7210a0a869232883a36d7)   0x00000037 /\* RF Core SMI Command Link Out \*/ |
| #define | [IOC\_PORT\_RFC\_SMI\_CL\_IN](#a8955bb4c29c837e71983307d2fc46155)   0x00000038 /\* RF Core SMI Command Link In \*/ |
| #define | [IOC\_NO\_EDGE](#a86134934e741c66f26bd4490e1f48553)   0x00000000 /\* No edge detection \*/ |
| #define | [IOC\_FALLING\_EDGE](#a812505ce5828cd40a9030f37445b7860)   0x00010000 /\* Edge detection on falling edge \*/ |
| #define | [IOC\_RISING\_EDGE](#ac7124cf50c094bfc24313d88aa8c06f4)   0x00020000 /\* Edge detection on rising edge \*/ |
| #define | [IOC\_BOTH\_EDGES](#aff5b936c3bbd5bd0e9429c8c7ac5f6a8)   0x00030000 /\* Edge detection on both edges \*/ |

## Macro Definition Documentation

## [◆ ](#aff5b936c3bbd5bd0e9429c8c7ac5f6a8)IOC\_BOTH\_EDGES

| #define IOC\_BOTH\_EDGES   0x00030000 /\* Edge detection on both edges \*/ |
| --- |

## [◆ ](#a812505ce5828cd40a9030f37445b7860)IOC\_FALLING\_EDGE

| #define IOC\_FALLING\_EDGE   0x00010000 /\* Edge detection on falling edge \*/ |
| --- |

## [◆ ](#a86134934e741c66f26bd4490e1f48553)IOC\_NO\_EDGE

| #define IOC\_NO\_EDGE   0x00000000 /\* No edge detection \*/ |
| --- |

## [◆ ](#a2dade73b9db2292ee357ec1ae92ed2d0)IOC\_PORT\_AON\_CLK32K

| #define IOC\_PORT\_AON\_CLK32K   0x00000007 /\* AON External 32kHz clock \*/ |
| --- |

## [◆ ](#a1b04b35124c351075fe3974adeb4d9aa)IOC\_PORT\_AUX\_IO

| #define IOC\_PORT\_AUX\_IO   0x00000008 /\* AUX IO Pin \*/ |
| --- |

## [◆ ](#a28f8e101ae30e86989a5c7b35be8f2d1)IOC\_PORT\_GPIO

| #define IOC\_PORT\_GPIO   0x00000000 /\* Default general purpose IO usage \*/ |
| --- |

## [◆ ](#a7d3e1312e3803326770e4d734e25b2eb)IOC\_PORT\_MCU\_I2C\_MSSCL

| #define IOC\_PORT\_MCU\_I2C\_MSSCL   0x0000000E /\* MCU I2C Clock Pin \*/ |
| --- |

## [◆ ](#aa318c337f1371b5f81ebf427a43cf318)IOC\_PORT\_MCU\_I2C\_MSSDA

| #define IOC\_PORT\_MCU\_I2C\_MSSDA   0x0000000D /\* MCU I2C Data Pin \*/ |
| --- |

## [◆ ](#ad8d7633125f181d03a832504ca0333af)IOC\_PORT\_MCU\_I2S\_AD0

| #define IOC\_PORT\_MCU\_I2S\_AD0   0x00000025 /\* MCU I2S Data Pin 0 \*/ |
| --- |

## [◆ ](#a3e3c593f43d20f8b976104e4370e2bfe)IOC\_PORT\_MCU\_I2S\_AD1

| #define IOC\_PORT\_MCU\_I2S\_AD1   0x00000026 /\* MCU I2S Data Pin 1 \*/ |
| --- |

## [◆ ](#a27b5fe5cdbd768684939c52662ed919a)IOC\_PORT\_MCU\_I2S\_BCLK

| #define IOC\_PORT\_MCU\_I2S\_BCLK   0x00000028 /\* MCU I2S Bit Clock \*/ |
| --- |

## [◆ ](#a72287ec0a2c5f0423e785d3e371a120e)IOC\_PORT\_MCU\_I2S\_MCLK

| #define IOC\_PORT\_MCU\_I2S\_MCLK   0x00000029 /\* MCU I2S Master clock 2 \*/ |
| --- |

## [◆ ](#a87f51f7808c53fb7a1d0ab0cfc7c3bfb)IOC\_PORT\_MCU\_I2S\_WCLK

| #define IOC\_PORT\_MCU\_I2S\_WCLK   0x00000027 /\* MCU I2S Frame/Word Clock \*/ |
| --- |

## [◆ ](#abb2e44fdb358359785db59197e43bf77)IOC\_PORT\_MCU\_PORT\_EVENT0

| #define IOC\_PORT\_MCU\_PORT\_EVENT0   0x00000017 /\* MCU PORT EVENT 0 \*/ |
| --- |

## [◆ ](#a53158c583bdc22b05a3ab803976f86f3)IOC\_PORT\_MCU\_PORT\_EVENT1

| #define IOC\_PORT\_MCU\_PORT\_EVENT1   0x00000018 /\* MCU PORT EVENT 1 \*/ |
| --- |

## [◆ ](#a3c31d2aee7d57f0b939678d24489b288)IOC\_PORT\_MCU\_PORT\_EVENT2

| #define IOC\_PORT\_MCU\_PORT\_EVENT2   0x00000019 /\* MCU PORT EVENT 2 \*/ |
| --- |

## [◆ ](#af74865ea575600cdef510d96b765fcaa)IOC\_PORT\_MCU\_PORT\_EVENT3

| #define IOC\_PORT\_MCU\_PORT\_EVENT3   0x0000001A /\* MCU PORT EVENT 3 \*/ |
| --- |

## [◆ ](#a8c29bb202c04366637a067403cb04798)IOC\_PORT\_MCU\_PORT\_EVENT4

| #define IOC\_PORT\_MCU\_PORT\_EVENT4   0x0000001B /\* MCU PORT EVENT 4 \*/ |
| --- |

## [◆ ](#a5018eb7bb384ce6240bc5ce37f684fd4)IOC\_PORT\_MCU\_PORT\_EVENT5

| #define IOC\_PORT\_MCU\_PORT\_EVENT5   0x0000001C /\* MCU PORT EVENT 5 \*/ |
| --- |

## [◆ ](#a627f8281323ce4d84edc61c921e5fc35)IOC\_PORT\_MCU\_PORT\_EVENT6

| #define IOC\_PORT\_MCU\_PORT\_EVENT6   0x0000001D /\* MCU PORT EVENT 6 \*/ |
| --- |

## [◆ ](#ae058c9773b968e08c17f848e8a17e33e)IOC\_PORT\_MCU\_PORT\_EVENT7

| #define IOC\_PORT\_MCU\_PORT\_EVENT7   0x0000001E /\* MCU PORT EVENT 7 \*/ |
| --- |

## [◆ ](#acfeabd6ba536f550b52c98eba600f99c)IOC\_PORT\_MCU\_SSI0\_CLK

| #define IOC\_PORT\_MCU\_SSI0\_CLK   0x0000000C /\* MCU SSI0 Clock Pin \*/ |
| --- |

## [◆ ](#a5e72bbc3a52d1bd643059f9a2037db03)IOC\_PORT\_MCU\_SSI0\_FSS

| #define IOC\_PORT\_MCU\_SSI0\_FSS   0x0000000B /\* MCU SSI0 FSS Pin \*/ |
| --- |

## [◆ ](#a3ee91cd12de013161c91f231676b279c)IOC\_PORT\_MCU\_SSI0\_RX

| #define IOC\_PORT\_MCU\_SSI0\_RX   0x00000009 /\* MCU SSI0 Receive Pin \*/ |
| --- |

## [◆ ](#a984735dec2b09061ab1be699a708367f)IOC\_PORT\_MCU\_SSI0\_TX

| #define IOC\_PORT\_MCU\_SSI0\_TX   0x0000000A /\* MCU SSI0 Transmit Pin \*/ |
| --- |

## [◆ ](#aa657dc9b3b551a535207a5c70944c7ad)IOC\_PORT\_MCU\_SSI1\_CLK

| #define IOC\_PORT\_MCU\_SSI1\_CLK   0x00000024 /\* MCU SSI1 Clock Pin \*/ |
| --- |

## [◆ ](#a8517079f7b23895467d0c6c5cee74051)IOC\_PORT\_MCU\_SSI1\_FSS

| #define IOC\_PORT\_MCU\_SSI1\_FSS   0x00000023 /\* MCU SSI1 FSS Pin \*/ |
| --- |

## [◆ ](#adc4c2aa534badaa6a40a994012968226)IOC\_PORT\_MCU\_SSI1\_RX

| #define IOC\_PORT\_MCU\_SSI1\_RX   0x00000021 /\* MCU SSI1 Receive Pin \*/ |
| --- |

## [◆ ](#a9024a0c4d78a72ff56c12d9ef6bce984)IOC\_PORT\_MCU\_SSI1\_TX

| #define IOC\_PORT\_MCU\_SSI1\_TX   0x00000022 /\* MCU SSI1 Transmit Pin \*/ |
| --- |

## [◆ ](#a5bf13b897900e2f62c82d84d23558c9b)IOC\_PORT\_MCU\_SWV

| #define IOC\_PORT\_MCU\_SWV   0x00000020 /\* Serial Wire Viewer \*/ |
| --- |

## [◆ ](#ad86b00b6011d22d55d31c8c2681edea8)IOC\_PORT\_MCU\_UART0\_CTS

| #define IOC\_PORT\_MCU\_UART0\_CTS   0x00000011 /\* MCU UART0 Clear To Send Pin \*/ |
| --- |

## [◆ ](#acdc4b3216e14a0525a9bff563c618505)IOC\_PORT\_MCU\_UART0\_RTS

| #define IOC\_PORT\_MCU\_UART0\_RTS   0x00000012 /\* MCU UART0 Request To Send Pin \*/ |
| --- |

## [◆ ](#aab1fbb3fbc8a90bd4d8fb1b55f69eb44)IOC\_PORT\_MCU\_UART0\_RX

| #define IOC\_PORT\_MCU\_UART0\_RX   0x0000000F /\* MCU UART0 Receive Pin \*/ |
| --- |

## [◆ ](#ac1adc319c3a412383fbd03d4dc9f08f5)IOC\_PORT\_MCU\_UART0\_TX

| #define IOC\_PORT\_MCU\_UART0\_TX   0x00000010 /\* MCU UART0 Transmit Pin \*/ |
| --- |

## [◆ ](#a3891eea57014086f4d9665c5659df9f9)IOC\_PORT\_MCU\_UART1\_CTS

| #define IOC\_PORT\_MCU\_UART1\_CTS   0x00000015 /\* MCU UART1 Clear To Send Pin \*/ |
| --- |

## [◆ ](#a07f27135f53b5f70c9cf611fee1da81c)IOC\_PORT\_MCU\_UART1\_RTS

| #define IOC\_PORT\_MCU\_UART1\_RTS   0x00000016 /\* MCU UART1 Request To Send Pin \*/ |
| --- |

## [◆ ](#a81eb684c41b27ab5c2e434f74cac653a)IOC\_PORT\_MCU\_UART1\_RX

| #define IOC\_PORT\_MCU\_UART1\_RX   0x00000013 /\* MCU UART1 Receive Pin \*/ |
| --- |

## [◆ ](#aabad6396786ac0fba4e030fa3bafaebe)IOC\_PORT\_MCU\_UART1\_TX

| #define IOC\_PORT\_MCU\_UART1\_TX   0x00000014 /\* MCU UART1 Transmit Pin \*/ |
| --- |

## [◆ ](#af0c7ce805a62bed97029d997406e8ec7)IOC\_PORT\_RFC\_GPI0

| #define IOC\_PORT\_RFC\_GPI0   0x00000033 /\* RC Core Data In Pin 0 \*/ |
| --- |

## [◆ ](#a6f1fc00a44a3311866187ce0c7470b1f)IOC\_PORT\_RFC\_GPI1

| #define IOC\_PORT\_RFC\_GPI1   0x00000034 /\* RC Core Data In Pin 1 \*/ |
| --- |

## [◆ ](#a00a019e1ddf52b2913e8358c18095ed4)IOC\_PORT\_RFC\_GPO0

| #define IOC\_PORT\_RFC\_GPO0   0x0000002F /\* RC Core Data Out Pin 0 \*/ |
| --- |

## [◆ ](#a00ea75c9456ac6b11e666757750ae342)IOC\_PORT\_RFC\_GPO1

| #define IOC\_PORT\_RFC\_GPO1   0x00000030 /\* RC Core Data Out Pin 1 \*/ |
| --- |

## [◆ ](#a5f19fce0ef7c834714af2e7f1c2bd06d)IOC\_PORT\_RFC\_GPO2

| #define IOC\_PORT\_RFC\_GPO2   0x00000031 /\* RC Core Data Out Pin 2 \*/ |
| --- |

## [◆ ](#ac940779073013ae6912da19fe598d999)IOC\_PORT\_RFC\_GPO3

| #define IOC\_PORT\_RFC\_GPO3   0x00000032 /\* RC Core Data Out Pin 3 \*/ |
| --- |

## [◆ ](#a8955bb4c29c837e71983307d2fc46155)IOC\_PORT\_RFC\_SMI\_CL\_IN

| #define IOC\_PORT\_RFC\_SMI\_CL\_IN   0x00000038 /\* RF Core SMI Command Link In \*/ |
| --- |

## [◆ ](#a8fa600a45bb7210a0a869232883a36d7)IOC\_PORT\_RFC\_SMI\_CL\_OUT

| #define IOC\_PORT\_RFC\_SMI\_CL\_OUT   0x00000037 /\* RF Core SMI Command Link Out \*/ |
| --- |

## [◆ ](#a38268821c556568eb9b8d0bd1b6bf4a4)IOC\_PORT\_RFC\_SMI\_DL\_IN

| #define IOC\_PORT\_RFC\_SMI\_DL\_IN   0x00000036 /\* RF Core SMI Data Link in \*/ |
| --- |

## [◆ ](#a34286b14818f96f8e3955eebc3f453eb)IOC\_PORT\_RFC\_SMI\_DL\_OUT

| #define IOC\_PORT\_RFC\_SMI\_DL\_OUT   0x00000035 /\* RF Core SMI Data Link Out \*/ |
| --- |

## [◆ ](#ae6a1e66015d48324657ede92613381be)IOC\_PORT\_RFC\_TRC

| #define IOC\_PORT\_RFC\_TRC   0x0000002E /\* RF Core Tracer \*/ |
| --- |

## [◆ ](#ac7124cf50c094bfc24313d88aa8c06f4)IOC\_RISING\_EDGE

| #define IOC\_RISING\_EDGE   0x00020000 /\* Edge detection on rising edge \*/ |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [cc13xx\_cc26xx-pinctrl.h](cc13xx__cc26xx-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
