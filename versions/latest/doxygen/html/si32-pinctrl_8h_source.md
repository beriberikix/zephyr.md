---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/si32-pinctrl_8h_source.html
original_path: doxygen/html/si32-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

si32-pinctrl.h

[Go to the documentation of this file.](si32-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2024 GARDENA GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_SI32\_PINCTRL\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_SI32\_PINCTRL\_

9

[ 10](si32-pinctrl_8h.md#ad4b8db8eccc425a32efe693f3990795a)#define SI32\_SIGNAL\_USART0\_TX 0

[ 11](si32-pinctrl_8h.md#a8f820379eac8a9457d956d0df47f5ab3)#define SI32\_SIGNAL\_USART0\_RX 1

[ 12](si32-pinctrl_8h.md#a821c99fe6d0904413309ca2c59abed40)#define SI32\_SIGNAL\_USART0\_RTS 2

[ 13](si32-pinctrl_8h.md#a1bf0461021350680ad9e9238187f2a14)#define SI32\_SIGNAL\_USART0\_CTS 3

[ 14](si32-pinctrl_8h.md#a3f9597efa079cfeaecb73fa38874560d)#define SI32\_SIGNAL\_USART0\_UCLK 4

15

[ 16](si32-pinctrl_8h.md#a564031ff57f625dff8f954e09143b414)#define SI32\_SIGNAL\_SPI0\_SCK 5

[ 17](si32-pinctrl_8h.md#a9cdf0205715f7e0df69b0884ec4eb034)#define SI32\_SIGNAL\_SPI0\_MISO 6

[ 18](si32-pinctrl_8h.md#a774f11fb89f1873a12d00fc18ad61bc4)#define SI32\_SIGNAL\_SPI0\_MOSI 7

[ 19](si32-pinctrl_8h.md#ac3b65fd167275b28846e222f3e862ad7)#define SI32\_SIGNAL\_SPI0\_NSS 8

20

[ 21](si32-pinctrl_8h.md#ad133ca912e8e41101f9a0b2be50a3e52)#define SI32\_SIGNAL\_USART1\_TX 9

[ 22](si32-pinctrl_8h.md#aa2f9e6c5285c5e563ed5391a0ea91cc7)#define SI32\_SIGNAL\_USART1\_RX 10

[ 23](si32-pinctrl_8h.md#a2035a9adf607726fb5584c5e891bda6c)#define SI32\_SIGNAL\_USART1\_RTS 11

[ 24](si32-pinctrl_8h.md#aa996cf5cc67047e835f9a4a564e301c8)#define SI32\_SIGNAL\_USART1\_CTS 12

[ 25](si32-pinctrl_8h.md#a28feea74c6c30294a391a7c3f0d61a6c)#define SI32\_SIGNAL\_USART1\_UCLK 13

26

[ 27](si32-pinctrl_8h.md#a0fd7c19cea300f6ab487f8aa87e99b26)#define SI32\_SIGNAL\_EPCA0\_CEX0 14

[ 28](si32-pinctrl_8h.md#a17e070c993d8197f6b8b64e671600fb2)#define SI32\_SIGNAL\_EPCA0\_CEX1 15

[ 29](si32-pinctrl_8h.md#a18f5f4be2d5e594f5ecd89891fd98d09)#define SI32\_SIGNAL\_EPCA0\_CEX2 16

[ 30](si32-pinctrl_8h.md#ab21c11a798beb90032ae57769a71db99)#define SI32\_SIGNAL\_EPCA0\_CEX3 17

[ 31](si32-pinctrl_8h.md#aa17085122f5f0d48c21af77502ff4c34)#define SI32\_SIGNAL\_EPCA0\_CEX4 18

32#define SI32\_SIGNAL\_EPCA0\_CEX4 19

33

[ 34](si32-pinctrl_8h.md#a9caa557fbb413deacad3328af0be9280)#define SI32\_SIGNAL\_PCA0\_CEX0 20

[ 35](si32-pinctrl_8h.md#aa833436d438c238177d875fbe8fa9f1d)#define SI32\_SIGNAL\_PCA0\_CEX1 21

36

[ 37](si32-pinctrl_8h.md#ad3437a2568c0f4c372f2f23aefdb9cc2)#define SI32\_SIGNAL\_PCA1\_CEX0 22

[ 38](si32-pinctrl_8h.md#ab6de6954edc1461916ee3ac724d4305c)#define SI32\_SIGNAL\_PCA1\_CEX1 23

39

[ 40](si32-pinctrl_8h.md#a83d737ad09d19ff3237e27b0f94a39f0)#define SI32\_SIGNAL\_EPCA0\_ECI 24

41

[ 42](si32-pinctrl_8h.md#a34a3158f0315aaec4b98a30c06bec6b9)#define SI32\_SIGNAL\_PCA0\_ECI 25

43

[ 44](si32-pinctrl_8h.md#a3ed602d8d72a91d29a0341fa343dc70d)#define SI32\_SIGNAL\_PCA1\_ECI 26

45

[ 46](si32-pinctrl_8h.md#acc070e46bdefe24363725a3301fe8bea)#define SI32\_SIGNAL\_I2S0\_TX\_WS 27

[ 47](si32-pinctrl_8h.md#a8a7f9761515ffcb6b2ea91d91cf8749a)#define SI32\_SIGNAL\_I2S0\_TX\_SCK 28

[ 48](si32-pinctrl_8h.md#a705d457bc068c183bc0c0fc8b3fa04cc)#define SI32\_SIGNAL\_I2S0\_TX\_SD 29

49

[ 50](si32-pinctrl_8h.md#a8749d0785c59968f9852a9261706885a)#define SI32\_SIGNAL\_I2C0\_SDA 30

[ 51](si32-pinctrl_8h.md#a85a70bf27b1a8ebcd74122dd39c0b61d)#define SI32\_SIGNAL\_I2C0\_SCL 31

52

[ 53](si32-pinctrl_8h.md#af0a10273a3f0bd24d869ef3eb4fe5d5d)#define SI32\_SIGNAL\_CMP0S 32

[ 54](si32-pinctrl_8h.md#a04d4a091f0f2f76098e4dc9fa27ee53b)#define SI32\_SIGNAL\_CMP0A 33

55

[ 56](si32-pinctrl_8h.md#a888361f8d34da62b6a3196ea51e1c117)#define SI32\_SIGNAL\_CMP1S 34

[ 57](si32-pinctrl_8h.md#a1744cb05cc79080708631955da4bb749)#define SI32\_SIGNAL\_CMP1A 35

58

[ 59](si32-pinctrl_8h.md#a193824af0d6d7867a3ed1daf20220052)#define SI32\_SIGNAL\_TIMER0\_CT 36

[ 60](si32-pinctrl_8h.md#a82b0bd59b9f99f7da1de73bab97c1e4a)#define SI32\_SIGNAL\_TIMER0\_EX 37

61

[ 62](si32-pinctrl_8h.md#a777b57705877efd09413a193ec61684a)#define SI32\_SIGNAL\_TIMER1\_CT 38

[ 63](si32-pinctrl_8h.md#a6564af1986f32e1ee4cd4819c46a9e6c)#define SI32\_SIGNAL\_TIMER1\_EX 39

64

[ 65](si32-pinctrl_8h.md#a250a8295d76d2b7c86ef92d7dea652ed)#define SI32\_SIGNAL\_UART0\_TX 40

[ 66](si32-pinctrl_8h.md#a9cbaee5a7e9bb49959b4c4728889479a)#define SI32\_SIGNAL\_UART0\_RX 41

[ 67](si32-pinctrl_8h.md#aa850463b8ddf026989cac9d55e3ae5ba)#define SI32\_SIGNAL\_UART0\_RTS 42

[ 68](si32-pinctrl_8h.md#a0853a0918a2acc788fa1b6ed7cbf44f6)#define SI32\_SIGNAL\_UART0\_CTS 43

69

[ 70](si32-pinctrl_8h.md#a7ef5f83e7342af31285e1bc12797777b)#define SI32\_SIGNAL\_UART1\_TX 44

[ 71](si32-pinctrl_8h.md#a3554209ac5136f3833331e55b67017a8)#define SI32\_SIGNAL\_UART1\_RX 45

72

[ 73](si32-pinctrl_8h.md#a6142acf0eb65a87fdb746e664faf7b5b)#define SI32\_SIGNAL\_SPI1\_SCK 46

[ 74](si32-pinctrl_8h.md#a27a95029482bab7182519e9348c54436)#define SI32\_SIGNAL\_SPI1\_MISO 47

[ 75](si32-pinctrl_8h.md#af196332c9297e7f5d72df8baa86c2263)#define SI32\_SIGNAL\_SPI1\_MOSI 48

[ 76](si32-pinctrl_8h.md#aeb29351af1c24eae781834d97a48747a)#define SI32\_SIGNAL\_SPI1\_NSS 49

77

[ 78](si32-pinctrl_8h.md#ace10227a5009fb1605fc3425abc2804b)#define SI32\_SIGNAL\_SPI2\_SCK 50

[ 79](si32-pinctrl_8h.md#a17ede16a40ffe7133a7aba89bdc144bc)#define SI32\_SIGNAL\_SPI2\_MISO 51

[ 80](si32-pinctrl_8h.md#a80f7a458c932dcab00516f7449471fa3)#define SI32\_SIGNAL\_SPI2\_MOSI 52

[ 81](si32-pinctrl_8h.md#a976e8a64aa84d4d898f3cc6a85dbea86)#define SI32\_SIGNAL\_SPI2\_NSS 53

82

[ 83](si32-pinctrl_8h.md#a088f8e2c65760933276036ac3a5b0a2d)#define SI32\_SIGNAL\_AHB\_OUT 54

84

[ 85](si32-pinctrl_8h.md#a782681a2f204f9f07959c8d609a1cef0)#define SI32\_SIGNAL\_SSG0\_EX0 55

[ 86](si32-pinctrl_8h.md#a3e4496a7555d4d7bea456758987e7e54)#define SI32\_SIGNAL\_SSG0\_EX1 56

[ 87](si32-pinctrl_8h.md#a2cf79ed49d349f824a5f39e92956314a)#define SI32\_SIGNAL\_SSG0\_EX2 57

[ 88](si32-pinctrl_8h.md#a66163427c744424a27143911e98d6945)#define SI32\_SIGNAL\_SSG0\_EX3 58

89

[ 90](si32-pinctrl_8h.md#a521c8e2cdfa538e2668eb94bf3cf8305)#define SI32\_SIGNAL\_RTC0\_OUT 59

91

[ 92](si32-pinctrl_8h.md#a9301f41eb82131adc3f3d584e3f76877)#define SI32\_SIGNAL\_I2S0\_RX\_WS 60

[ 93](si32-pinctrl_8h.md#a4f87733a1b6052ee1120c6727f01c737)#define SI32\_SIGNAL\_I2S0\_RX\_SCK 61

[ 94](si32-pinctrl_8h.md#a7375a9748019f270252d3dbfd7d46f78)#define SI32\_SIGNAL\_I2S0\_RX\_SD 62

95

[ 96](si32-pinctrl_8h.md#a6289cd501727672c0d57f56f3718e3db)#define SI32\_SIGNAL\_LPTIMER0\_OUT 63

97

[ 98](si32-pinctrl_8h.md#a402e807b19fb92ee4bdeba9d25ad6ef1)#define SI32\_SIGNAL\_I2C1\_SDA 64

[ 99](si32-pinctrl_8h.md#ae84d7bf702433c6b32d3e339165c3cf0)#define SI32\_SIGNAL\_I2C1\_SCL 65

100

[ 101](si32-pinctrl_8h.md#a276c1f555242257da535b04944067767)#define SI32\_SIGNAL\_PB\_HDKILL 66

102

[ 110](si32-pinctrl_8h.md#a46f9809ef3476aca9aadc07081003e42)#define SI32\_MUX(fun, port, pin) \

111 ((((port)&0x7)) | (((pin)&0xF) << 3) | ((SI32\_SIGNAL\_##fun & 0x7F) << 22))

112

113#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_SI32\_PINCTRL\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [si32-pinctrl.h](si32-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
