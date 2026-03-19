---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/esp32c2-gpio-sigmap_8h.html
original_path: doxygen/html/esp32c2-gpio-sigmap_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32c2-gpio-sigmap.h File Reference

[Go to the source code of this file.](esp32c2-gpio-sigmap_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP\_NOSIG](#af80260535bc3aee44c28c972a29483e0)   [ESP\_SIG\_INVAL](esp-pinctrl-common_8h.md#ae0d2e726ab8d90343e5c80e1d9b85ad8) |
| #define | [ESP\_SPICLK\_OUT\_MUX](#aaf157f6b85a07f18b181876a7a04f142)   [ESP\_SPICLK\_OUT](#a5f440c922a53085bb7b28f469c2a14b0) |
| #define | [ESP\_SPIQ\_IN](#aec51ff955c6be50e529affc87ec9d5cb)   0 |
| #define | [ESP\_SPIQ\_OUT](#a5816deeca8853397a830a8eb251704ee)   0 |
| #define | [ESP\_SPID\_IN](#a26c603fd58dbd7526d2be3bb3e37758a)   1 |
| #define | [ESP\_SPID\_OUT](#af81b2fc65b68ed2238ab3367a8731102)   1 |
| #define | [ESP\_SPIHD\_IN](#a49783f877b666aff9362cf605590b991)   2 |
| #define | [ESP\_SPIHD\_OUT](#a8851b5256482790f3304efecafc13afd)   2 |
| #define | [ESP\_SPIWP\_IN](#aa74adc2812d9c6bd143c679fa4d9ca8d)   3 |
| #define | [ESP\_SPIWP\_OUT](#a470408f8102937dc017336e320e6147b)   3 |
| #define | [ESP\_SPICLK\_OUT](#a5f440c922a53085bb7b28f469c2a14b0)   4 |
| #define | [ESP\_SPICS0\_OUT](#a5d97c07ba0d8cda594d52310e90fa6a4)   5 |
| #define | [ESP\_U0RXD\_IN](#aca502efa55ce2286dc9eba28192681fd)   6 |
| #define | [ESP\_U0TXD\_OUT](#af1e58fb8e7ef86a92171eca7bb1671af)   6 |
| #define | [ESP\_U0CTS\_IN](#a530d7a918a97cd1fff1acf2f90edd4ca)   7 |
| #define | [ESP\_U0RTS\_OUT](#a4257bbc044af6ea3612313e3a0b7e7c9)   7 |
| #define | [ESP\_U0DSR\_IN](#a53e3a4557a4eb1f7f98250abef03c02a)   8 |
| #define | [ESP\_U0DTR\_OUT](#acc8716af947169c9f167bdf215c5314c)   8 |
| #define | [ESP\_U1RXD\_IN](#a2293e0646e0ad2f76d62f76425ae6770)   9 |
| #define | [ESP\_U1TXD\_OUT](#a6053b38147e28e3a7479b38e7d195136)   9 |
| #define | [ESP\_U1CTS\_IN](#a3c005e616da21a058960d6aed79427b3)   10 |
| #define | [ESP\_U1RTS\_OUT](#a8f6399745566bd5caa2020e4dcb2bb3b)   10 |
| #define | [ESP\_U1DSR\_IN](#a5f29b138691540598d0b977dc4bd5971)   11 |
| #define | [ESP\_U1DTR\_OUT](#a1f7df042d40ec6f20b559ef6778d7497)   11 |
| #define | [ESP\_SPIQ\_MONITOR](#a6abe131ab233461292f2987aadfee11a)   15 |
| #define | [ESP\_SPID\_MONITOR](#a6292a461f60010aec29fcc8356d514fd)   16 |
| #define | [ESP\_SPIHD\_MONITOR](#aff145e44d8e8e506225362072c6c6710)   17 |
| #define | [ESP\_SPIWP\_MONITOR](#a610bf782c52a09f754e16890a13851da)   18 |
| #define | [ESP\_SPICS1\_OUT](#aa4a67a38b97a3d466783c0617aa6a0c8)   19 |
| #define | [ESP\_CPU\_TESTBUS0](#a944cd61f21b48eb29d6a02dd36cadccf)   20 |
| #define | [ESP\_CPU\_TESTBUS1](#a2410d405f9a5a5ce1540eb9aea9b9f9e)   21 |
| #define | [ESP\_CPU\_TESTBUS2](#ae2f12f49b45db8f086ed1aa16fdb2e1b)   22 |
| #define | [ESP\_CPU\_TESTBUS3](#a225737984d07250e17b56aaf8e60289f)   23 |
| #define | [ESP\_CPU\_TESTBUS4](#ae3fbd8b602f8b71f7e8961442d38b720)   24 |
| #define | [ESP\_CPU\_TESTBUS5](#a5ce40632a364fdbfd94369806fc8dabc)   25 |
| #define | [ESP\_CPU\_TESTBUS6](#ae90382a0bb5727cf4981518b04e7b339)   26 |
| #define | [ESP\_CPU\_TESTBUS7](#ad21e1f7daa92fd691e1be1d9079e7cc2)   27 |
| #define | [ESP\_CPU\_GPIO\_IN0](#ac0df832ec7feeb3042f50c1eb1617f53)   28 |
| #define | [ESP\_CPU\_GPIO\_OUT0](#aef48b51b644720c53dacdc6037ec7bc0)   28 |
| #define | [ESP\_CPU\_GPIO\_IN1](#a0cc3cac4ad6eeb0c8c3cf0105f118554)   29 |
| #define | [ESP\_CPU\_GPIO\_OUT1](#a8c9087d7ac05fa248d42b86997d79f01)   29 |
| #define | [ESP\_CPU\_GPIO\_IN2](#ad7bce49dbf1ed089e8695d5a1ae99861)   30 |
| #define | [ESP\_CPU\_GPIO\_OUT2](#a6d7108dcd0de2f3a6bbb84c6703baa3f)   30 |
| #define | [ESP\_CPU\_GPIO\_IN3](#a553b001f496ac3689979841a04a7a862)   31 |
| #define | [ESP\_CPU\_GPIO\_OUT3](#ad3d027b5581594073ea70b1955bb5733)   31 |
| #define | [ESP\_CPU\_GPIO\_IN4](#a848b0915100b8e3b75089854d32910ee)   32 |
| #define | [ESP\_CPU\_GPIO\_OUT4](#ac761dfb305a0e44a2447789680fd0ff9)   32 |
| #define | [ESP\_CPU\_GPIO\_IN5](#abb64fd2a84298157b6071cc127a3c0ca)   33 |
| #define | [ESP\_CPU\_GPIO\_OUT5](#add1c492755091bcdeafabe38cb65617b)   33 |
| #define | [ESP\_CPU\_GPIO\_IN6](#a1695bafbd25037bcd848c5b58bdae422)   34 |
| #define | [ESP\_CPU\_GPIO\_OUT6](#a929fc17e60b97257fef693b9ac1682ad)   34 |
| #define | [ESP\_CPU\_GPIO\_IN7](#a10dc617c0b532ee5a8ae3d913a984007)   35 |
| #define | [ESP\_CPU\_GPIO\_OUT7](#ad54946b60e601390d863b20dd1c13e32)   35 |
| #define | [ESP\_EXT\_ADC\_START](#ae49b4527d8fbd0f5c8e3edc72704c54a)   45 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT0](#a62dfcd88747c61acb53dc85c1751f1d3)   45 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT1](#a5cad9206cfeea93b42e5456228c7d580)   46 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT2](#ab408070e7c700805db165c3876b6c588)   47 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT3](#a438aee217c6c94a2962a3d98935b5717)   48 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT4](#ada93dcffffc15362be4b7432a8033559)   49 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT5](#a34fc029ec45756ca7064580f57db1cc7)   50 |
| #define | [ESP\_RMT\_SIG\_IN0](#ad9bae9b4884a356e465656d1ee8d61cd)   51 |
| #define | [ESP\_RMT\_SIG\_OUT0](#a25343fbc20a0c542bcdc21cdfade867b)   51 |
| #define | [ESP\_RMT\_SIG\_IN1](#ab6c6293e6845ba4bf4d05b84102ffdcf)   52 |
| #define | [ESP\_RMT\_SIG\_OUT1](#a6d082fb1c7397d784a3075108e0dea73)   52 |
| #define | [ESP\_I2CEXT0\_SCL\_IN](#ab607ce367da34ab0f1bd7fa648273cf1)   53 |
| #define | [ESP\_I2CEXT0\_SCL\_OUT](#a2144cc62df795547ccf2bbe3ee4c629f)   53 |
| #define | [ESP\_I2CEXT0\_SDA\_IN](#afa7061c87135b9dabe5c54f5f4ce16e6)   54 |
| #define | [ESP\_I2CEXT0\_SDA\_OUT](#aabf1378b0ad2028c36c3bb74c81d7049)   54 |
| #define | [ESP\_FSPICLK\_IN](#ade88988460c131e8c6775794588b0eb8)   63 |
| #define | [ESP\_FSPICLK\_OUT](#ab8c5397dc530f6326c3d10b31e59e168)   63 |
| #define | [ESP\_FSPIQ\_IN](#ab603b7bf7d016e85653a5c3be5c01293)   64 |
| #define | [ESP\_FSPIQ\_OUT](#a8b3ea6ad374fa010b46b48072fa87ccb)   64 |
| #define | [ESP\_FSPID\_IN](#a7910521af840d42edd3c0a667cf90c5f)   65 |
| #define | [ESP\_FSPID\_OUT](#a02bd34821e8a4bf0038b9af417ec161a)   65 |
| #define | [ESP\_FSPIHD\_IN](#a60ff087a3d85a356d77f060a6698d00b)   66 |
| #define | [ESP\_FSPIHD\_OUT](#ac71bc137b93bd6c0c8a1ebe24a70a613)   66 |
| #define | [ESP\_FSPIWP\_IN](#a4d4c4a13b820cab6d94da8fe08120a2f)   67 |
| #define | [ESP\_FSPIWP\_OUT](#a83c4f18d726984cc98caeea9b7677ca1)   67 |
| #define | [ESP\_FSPICS0\_IN](#a96ca1328e76337d289f6e65faf33d75c)   68 |
| #define | [ESP\_FSPICS0\_OUT](#ad1be1401b282275eaef46b9a598c6a40)   68 |
| #define | [ESP\_FSPICS1\_OUT](#a44ade9179a7ea00586359a009799661d)   69 |
| #define | [ESP\_FSPICS2\_OUT](#af991963f29c5b268a5f8fead8fd15348)   70 |
| #define | [ESP\_FSPICS3\_OUT](#a65d1170c5a68ac7f6a4457c3380ddfde)   71 |
| #define | [ESP\_FSPICS4\_OUT](#a83dafe68703c701dcd07d7ff0aadad01)   72 |
| #define | [ESP\_FSPICS5\_OUT](#ad8fab64bb220fd198a6cd931f4ea1e8e)   73 |
| #define | [ESP\_EXTERN\_PRIORITY\_I](#a39627b897d55107e1ecee725bd662ec2)   77 |
| #define | [ESP\_EXTERN\_PRIORITY\_O](#ab50a3b95442a89e070163c623a261578)   77 |
| #define | [ESP\_EXTERN\_ACTIVE\_I](#a533fcce69d815e97b58d7f1af1d4505c)   78 |
| #define | [ESP\_EXTERN\_ACTIVE\_O](#a198d1c07a648c5353e1c127e855d47c9)   78 |
| #define | [ESP\_GPIO\_EVENT\_MATRIX\_IN0](#a2af8dc70a06105740ae181a616186624)   79 |
| #define | [ESP\_GPIO\_TASK\_MATRIX\_OUT0](#aeee7dc180a750016e7711282b252ccf6)   79 |
| #define | [ESP\_GPIO\_EVENT\_MATRIX\_IN1](#a7a2ce6558a5368d1fc0325ce37487d1a)   80 |
| #define | [ESP\_GPIO\_TASK\_MATRIX\_OUT1](#a4ce0ef64cebc11e961d73fc58d8bb954)   80 |
| #define | [ESP\_GPIO\_EVENT\_MATRIX\_IN2](#a2ae077cc87f156e9545eca4a091890e3)   81 |
| #define | [ESP\_GPIO\_TASK\_MATRIX\_OUT2](#a0ac11865f0be99e81bebeb7dfbe1424b)   81 |
| #define | [ESP\_GPIO\_EVENT\_MATRIX\_IN3](#a97d8c86a5d7ba47196816c7d04ef7efb)   82 |
| #define | [ESP\_GPIO\_TASK\_MATRIX\_OUT3](#a165323f111794aeff16e7073501ff16e)   82 |
| #define | [ESP\_BB\_DIAG8\_OUT](#af142a270dafe58997f617efb61512d30)   83 |
| #define | [ESP\_BB\_DIAG9\_OUT](#a617d3a75257f691b0797e50de7a7b465)   84 |
| #define | [ESP\_BB\_DIAG10\_OUT](#aab71da6e85a906a438d27e2b6bd9a921)   85 |
| #define | [ESP\_BB\_DIAG11\_OUT](#a189e37f0d904a0ba97354a7c3a54ca40)   86 |
| #define | [ESP\_BB\_DIAG12\_OUT](#a0d59630bc17c91a35eb36a5c5aa0a80c)   87 |
| #define | [ESP\_BB\_DIAG13\_OUT](#ac851f634048c53a550a07e6bec6c6b8a)   88 |
| #define | [ESP\_ANT\_SEL0](#aec2dfb198f69d923686404a0a6330833)   89 |
| #define | [ESP\_ANT\_SEL1](#a15c080ea1e4c8e2db9f1640e9b8c4f0a)   90 |
| #define | [ESP\_ANT\_SEL2](#ae3042ff86ecc0f2e78ebe9477055e819)   91 |
| #define | [ESP\_ANT\_SEL3](#ab8e5cca4b9eb1a7bda7868ecd792c76d)   92 |
| #define | [ESP\_ANT\_SEL4](#a821cc4b81f76043b1ecb751118a2f416)   93 |
| #define | [ESP\_ANT\_SEL5](#a28a954881fd9d5f5e7ff25d715f0bcc2)   94 |
| #define | [ESP\_ANT\_SEL6](#a2122dad1966cbe214e9c82cb9a46bd8a)   95 |
| #define | [ESP\_ANT\_SEL7](#a8f9cedf15c49cee3fbac2a22df7675ec)   96 |
| #define | [ESP\_SIG\_IN\_FUNC\_97](#a66890ae0c0e6a875c19099abb1918ca1)   97 |
| #define | [ESP\_SIG\_IN\_FUNC97](#a919b1b0e57d8785970c702fcd49d5563)   97 |
| #define | [ESP\_SIG\_IN\_FUNC\_98](#a848f955ed1b3b04d0a3d90f8c0acedec)   98 |
| #define | [ESP\_SIG\_IN\_FUNC98](#ae6043332289b10b68dc1d278681f3df1)   98 |
| #define | [ESP\_SIG\_IN\_FUNC\_99](#ab6956182e8d06463813e94843398a45f)   99 |
| #define | [ESP\_SIG\_IN\_FUNC99](#a11dcdffc24ff5d98c7c8d0f609a0c7b9)   99 |
| #define | [ESP\_SIG\_IN\_FUNC\_100](#a6684d495dfe99d0798f576018ffe0aba)   100 |
| #define | [ESP\_SIG\_IN\_FUNC100](#a33f1fad3bde9b252dfb3a291d600c019)   100 |
| #define | [ESP\_BLE\_DBG\_SYNCERR](#aa80adfd043a26d791a5e9c31de201164)   101 |
| #define | [ESP\_BLE\_DBG\_SYNC\_FOUND](#a8f7e3cba06744a8a0fa588630928d423)   102 |
| #define | [ESP\_BLE\_DBG\_CH\_IDX](#aa46207fab7ed6822b75880b531879190)   103 |
| #define | [ESP\_BLE\_DBG\_SYNC\_WINDOW](#afa25c4867b6f4f78e32618d2ed804ccb)   104 |
| #define | [ESP\_BLE\_DBG\_DATA\_EN](#afa5cc2bba649ccc7532eca43c80c31bf)   105 |
| #define | [ESP\_BLE\_DBG\_DATA](#a1c9ccf8879588f15c83be60de6c2a9ca)   106 |
| #define | [ESP\_BLE\_DBG\_PKT\_TX\_ON](#a5b9f79d6c4a300f6949ee075fb462814)   107 |
| #define | [ESP\_BLE\_DBG\_PKT\_RX\_ON](#a0592bcc99eb7e739a1daf53fbae72965)   108 |
| #define | [ESP\_BLE\_DBG\_TXRU\_ON](#a81d7d01938d7b4a840f21b48bc702d95)   109 |
| #define | [ESP\_BLE\_DBG\_RXRU\_ON](#a3766af70b405de3b991e90996a758d83)   110 |
| #define | [ESP\_BLE\_DBG\_LELC\_ST0](#ab87a5364ee77e3c700f6180ac45d4bf2)   111 |
| #define | [ESP\_BLE\_DBG\_LELC\_ST1](#ad4560183706658c3c6a41e6e705fb804)   112 |
| #define | [ESP\_BLE\_DBG\_LELC\_ST2](#af4a076c4f02e0d5eb390aa148e51c1f7)   113 |
| #define | [ESP\_BLE\_DBG\_LELC\_ST3](#ada8272aaa110794ae2214bb1fd2b44b0)   114 |
| #define | [ESP\_BLE\_DBG\_CRCOK](#a65b96d0f1327dcc17316f45d4286ce91)   115 |
| #define | [ESP\_BLE\_DBG\_CLK\_GPIO](#aeec8db4ffecedcc300f5961a55a48cc3)   116 |
| #define | [ESP\_BLE\_DBG\_RADIO\_START](#ae2cec5790ab61dd15dde088619708c2c)   117 |
| #define | [ESP\_BLE\_DBG\_SEQUENCE\_ON](#ad93ceefefe24132e4a194b322b20bccf)   118 |
| #define | [ESP\_BLE\_DBG\_COEX\_BT\_ON](#a9bca795190774e353d52eec0d90574bc)   119 |
| #define | [ESP\_BLE\_DBG\_COEX\_WIFI\_ON](#aa342f766b48aae7b5444505888673923)   120 |
| #define | [ESP\_CLK\_OUT\_OUT1](#a12a2380f8bcbf158e7c114b7dc1701a5)   123 |
| #define | [ESP\_CLK\_OUT\_OUT2](#adf7a9c85596f3a536ddb603d3218cee2)   124 |
| #define | [ESP\_CLK\_OUT\_OUT3](#af421f62c654ecca5136b7b526f168377)   125 |
| #define | [ESP\_SIG\_GPIO\_OUT](#a645411759ffdc63f51f2cd42632d2720)   128 |
| #define | [ESP\_GPIO\_MAP\_DATE](#afe5c166b887709cdd27bd37df85c45b9)   0x2106190 |

## Macro Definition Documentation

## [◆ ](#aec2dfb198f69d923686404a0a6330833)ESP\_ANT\_SEL0

| #define ESP\_ANT\_SEL0   89 |
| --- |

## [◆ ](#a15c080ea1e4c8e2db9f1640e9b8c4f0a)ESP\_ANT\_SEL1

| #define ESP\_ANT\_SEL1   90 |
| --- |

## [◆ ](#ae3042ff86ecc0f2e78ebe9477055e819)ESP\_ANT\_SEL2

| #define ESP\_ANT\_SEL2   91 |
| --- |

## [◆ ](#ab8e5cca4b9eb1a7bda7868ecd792c76d)ESP\_ANT\_SEL3

| #define ESP\_ANT\_SEL3   92 |
| --- |

## [◆ ](#a821cc4b81f76043b1ecb751118a2f416)ESP\_ANT\_SEL4

| #define ESP\_ANT\_SEL4   93 |
| --- |

## [◆ ](#a28a954881fd9d5f5e7ff25d715f0bcc2)ESP\_ANT\_SEL5

| #define ESP\_ANT\_SEL5   94 |
| --- |

## [◆ ](#a2122dad1966cbe214e9c82cb9a46bd8a)ESP\_ANT\_SEL6

| #define ESP\_ANT\_SEL6   95 |
| --- |

## [◆ ](#a8f9cedf15c49cee3fbac2a22df7675ec)ESP\_ANT\_SEL7

| #define ESP\_ANT\_SEL7   96 |
| --- |

## [◆ ](#aab71da6e85a906a438d27e2b6bd9a921)ESP\_BB\_DIAG10\_OUT

| #define ESP\_BB\_DIAG10\_OUT   85 |
| --- |

## [◆ ](#a189e37f0d904a0ba97354a7c3a54ca40)ESP\_BB\_DIAG11\_OUT

| #define ESP\_BB\_DIAG11\_OUT   86 |
| --- |

## [◆ ](#a0d59630bc17c91a35eb36a5c5aa0a80c)ESP\_BB\_DIAG12\_OUT

| #define ESP\_BB\_DIAG12\_OUT   87 |
| --- |

## [◆ ](#ac851f634048c53a550a07e6bec6c6b8a)ESP\_BB\_DIAG13\_OUT

| #define ESP\_BB\_DIAG13\_OUT   88 |
| --- |

## [◆ ](#af142a270dafe58997f617efb61512d30)ESP\_BB\_DIAG8\_OUT

| #define ESP\_BB\_DIAG8\_OUT   83 |
| --- |

## [◆ ](#a617d3a75257f691b0797e50de7a7b465)ESP\_BB\_DIAG9\_OUT

| #define ESP\_BB\_DIAG9\_OUT   84 |
| --- |

## [◆ ](#aa46207fab7ed6822b75880b531879190)ESP\_BLE\_DBG\_CH\_IDX

| #define ESP\_BLE\_DBG\_CH\_IDX   103 |
| --- |

## [◆ ](#aeec8db4ffecedcc300f5961a55a48cc3)ESP\_BLE\_DBG\_CLK\_GPIO

| #define ESP\_BLE\_DBG\_CLK\_GPIO   116 |
| --- |

## [◆ ](#a9bca795190774e353d52eec0d90574bc)ESP\_BLE\_DBG\_COEX\_BT\_ON

| #define ESP\_BLE\_DBG\_COEX\_BT\_ON   119 |
| --- |

## [◆ ](#aa342f766b48aae7b5444505888673923)ESP\_BLE\_DBG\_COEX\_WIFI\_ON

| #define ESP\_BLE\_DBG\_COEX\_WIFI\_ON   120 |
| --- |

## [◆ ](#a65b96d0f1327dcc17316f45d4286ce91)ESP\_BLE\_DBG\_CRCOK

| #define ESP\_BLE\_DBG\_CRCOK   115 |
| --- |

## [◆ ](#a1c9ccf8879588f15c83be60de6c2a9ca)ESP\_BLE\_DBG\_DATA

| #define ESP\_BLE\_DBG\_DATA   106 |
| --- |

## [◆ ](#afa5cc2bba649ccc7532eca43c80c31bf)ESP\_BLE\_DBG\_DATA\_EN

| #define ESP\_BLE\_DBG\_DATA\_EN   105 |
| --- |

## [◆ ](#ab87a5364ee77e3c700f6180ac45d4bf2)ESP\_BLE\_DBG\_LELC\_ST0

| #define ESP\_BLE\_DBG\_LELC\_ST0   111 |
| --- |

## [◆ ](#ad4560183706658c3c6a41e6e705fb804)ESP\_BLE\_DBG\_LELC\_ST1

| #define ESP\_BLE\_DBG\_LELC\_ST1   112 |
| --- |

## [◆ ](#af4a076c4f02e0d5eb390aa148e51c1f7)ESP\_BLE\_DBG\_LELC\_ST2

| #define ESP\_BLE\_DBG\_LELC\_ST2   113 |
| --- |

## [◆ ](#ada8272aaa110794ae2214bb1fd2b44b0)ESP\_BLE\_DBG\_LELC\_ST3

| #define ESP\_BLE\_DBG\_LELC\_ST3   114 |
| --- |

## [◆ ](#a0592bcc99eb7e739a1daf53fbae72965)ESP\_BLE\_DBG\_PKT\_RX\_ON

| #define ESP\_BLE\_DBG\_PKT\_RX\_ON   108 |
| --- |

## [◆ ](#a5b9f79d6c4a300f6949ee075fb462814)ESP\_BLE\_DBG\_PKT\_TX\_ON

| #define ESP\_BLE\_DBG\_PKT\_TX\_ON   107 |
| --- |

## [◆ ](#ae2cec5790ab61dd15dde088619708c2c)ESP\_BLE\_DBG\_RADIO\_START

| #define ESP\_BLE\_DBG\_RADIO\_START   117 |
| --- |

## [◆ ](#a3766af70b405de3b991e90996a758d83)ESP\_BLE\_DBG\_RXRU\_ON

| #define ESP\_BLE\_DBG\_RXRU\_ON   110 |
| --- |

## [◆ ](#ad93ceefefe24132e4a194b322b20bccf)ESP\_BLE\_DBG\_SEQUENCE\_ON

| #define ESP\_BLE\_DBG\_SEQUENCE\_ON   118 |
| --- |

## [◆ ](#a8f7e3cba06744a8a0fa588630928d423)ESP\_BLE\_DBG\_SYNC\_FOUND

| #define ESP\_BLE\_DBG\_SYNC\_FOUND   102 |
| --- |

## [◆ ](#afa25c4867b6f4f78e32618d2ed804ccb)ESP\_BLE\_DBG\_SYNC\_WINDOW

| #define ESP\_BLE\_DBG\_SYNC\_WINDOW   104 |
| --- |

## [◆ ](#aa80adfd043a26d791a5e9c31de201164)ESP\_BLE\_DBG\_SYNCERR

| #define ESP\_BLE\_DBG\_SYNCERR   101 |
| --- |

## [◆ ](#a81d7d01938d7b4a840f21b48bc702d95)ESP\_BLE\_DBG\_TXRU\_ON

| #define ESP\_BLE\_DBG\_TXRU\_ON   109 |
| --- |

## [◆ ](#a12a2380f8bcbf158e7c114b7dc1701a5)ESP\_CLK\_OUT\_OUT1

| #define ESP\_CLK\_OUT\_OUT1   123 |
| --- |

## [◆ ](#adf7a9c85596f3a536ddb603d3218cee2)ESP\_CLK\_OUT\_OUT2

| #define ESP\_CLK\_OUT\_OUT2   124 |
| --- |

## [◆ ](#af421f62c654ecca5136b7b526f168377)ESP\_CLK\_OUT\_OUT3

| #define ESP\_CLK\_OUT\_OUT3   125 |
| --- |

## [◆ ](#ac0df832ec7feeb3042f50c1eb1617f53)ESP\_CPU\_GPIO\_IN0

| #define ESP\_CPU\_GPIO\_IN0   28 |
| --- |

## [◆ ](#a0cc3cac4ad6eeb0c8c3cf0105f118554)ESP\_CPU\_GPIO\_IN1

| #define ESP\_CPU\_GPIO\_IN1   29 |
| --- |

## [◆ ](#ad7bce49dbf1ed089e8695d5a1ae99861)ESP\_CPU\_GPIO\_IN2

| #define ESP\_CPU\_GPIO\_IN2   30 |
| --- |

## [◆ ](#a553b001f496ac3689979841a04a7a862)ESP\_CPU\_GPIO\_IN3

| #define ESP\_CPU\_GPIO\_IN3   31 |
| --- |

## [◆ ](#a848b0915100b8e3b75089854d32910ee)ESP\_CPU\_GPIO\_IN4

| #define ESP\_CPU\_GPIO\_IN4   32 |
| --- |

## [◆ ](#abb64fd2a84298157b6071cc127a3c0ca)ESP\_CPU\_GPIO\_IN5

| #define ESP\_CPU\_GPIO\_IN5   33 |
| --- |

## [◆ ](#a1695bafbd25037bcd848c5b58bdae422)ESP\_CPU\_GPIO\_IN6

| #define ESP\_CPU\_GPIO\_IN6   34 |
| --- |

## [◆ ](#a10dc617c0b532ee5a8ae3d913a984007)ESP\_CPU\_GPIO\_IN7

| #define ESP\_CPU\_GPIO\_IN7   35 |
| --- |

## [◆ ](#aef48b51b644720c53dacdc6037ec7bc0)ESP\_CPU\_GPIO\_OUT0

| #define ESP\_CPU\_GPIO\_OUT0   28 |
| --- |

## [◆ ](#a8c9087d7ac05fa248d42b86997d79f01)ESP\_CPU\_GPIO\_OUT1

| #define ESP\_CPU\_GPIO\_OUT1   29 |
| --- |

## [◆ ](#a6d7108dcd0de2f3a6bbb84c6703baa3f)ESP\_CPU\_GPIO\_OUT2

| #define ESP\_CPU\_GPIO\_OUT2   30 |
| --- |

## [◆ ](#ad3d027b5581594073ea70b1955bb5733)ESP\_CPU\_GPIO\_OUT3

| #define ESP\_CPU\_GPIO\_OUT3   31 |
| --- |

## [◆ ](#ac761dfb305a0e44a2447789680fd0ff9)ESP\_CPU\_GPIO\_OUT4

| #define ESP\_CPU\_GPIO\_OUT4   32 |
| --- |

## [◆ ](#add1c492755091bcdeafabe38cb65617b)ESP\_CPU\_GPIO\_OUT5

| #define ESP\_CPU\_GPIO\_OUT5   33 |
| --- |

## [◆ ](#a929fc17e60b97257fef693b9ac1682ad)ESP\_CPU\_GPIO\_OUT6

| #define ESP\_CPU\_GPIO\_OUT6   34 |
| --- |

## [◆ ](#ad54946b60e601390d863b20dd1c13e32)ESP\_CPU\_GPIO\_OUT7

| #define ESP\_CPU\_GPIO\_OUT7   35 |
| --- |

## [◆ ](#a944cd61f21b48eb29d6a02dd36cadccf)ESP\_CPU\_TESTBUS0

| #define ESP\_CPU\_TESTBUS0   20 |
| --- |

## [◆ ](#a2410d405f9a5a5ce1540eb9aea9b9f9e)ESP\_CPU\_TESTBUS1

| #define ESP\_CPU\_TESTBUS1   21 |
| --- |

## [◆ ](#ae2f12f49b45db8f086ed1aa16fdb2e1b)ESP\_CPU\_TESTBUS2

| #define ESP\_CPU\_TESTBUS2   22 |
| --- |

## [◆ ](#a225737984d07250e17b56aaf8e60289f)ESP\_CPU\_TESTBUS3

| #define ESP\_CPU\_TESTBUS3   23 |
| --- |

## [◆ ](#ae3fbd8b602f8b71f7e8961442d38b720)ESP\_CPU\_TESTBUS4

| #define ESP\_CPU\_TESTBUS4   24 |
| --- |

## [◆ ](#a5ce40632a364fdbfd94369806fc8dabc)ESP\_CPU\_TESTBUS5

| #define ESP\_CPU\_TESTBUS5   25 |
| --- |

## [◆ ](#ae90382a0bb5727cf4981518b04e7b339)ESP\_CPU\_TESTBUS6

| #define ESP\_CPU\_TESTBUS6   26 |
| --- |

## [◆ ](#ad21e1f7daa92fd691e1be1d9079e7cc2)ESP\_CPU\_TESTBUS7

| #define ESP\_CPU\_TESTBUS7   27 |
| --- |

## [◆ ](#ae49b4527d8fbd0f5c8e3edc72704c54a)ESP\_EXT\_ADC\_START

| #define ESP\_EXT\_ADC\_START   45 |
| --- |

## [◆ ](#a533fcce69d815e97b58d7f1af1d4505c)ESP\_EXTERN\_ACTIVE\_I

| #define ESP\_EXTERN\_ACTIVE\_I   78 |
| --- |

## [◆ ](#a198d1c07a648c5353e1c127e855d47c9)ESP\_EXTERN\_ACTIVE\_O

| #define ESP\_EXTERN\_ACTIVE\_O   78 |
| --- |

## [◆ ](#a39627b897d55107e1ecee725bd662ec2)ESP\_EXTERN\_PRIORITY\_I

| #define ESP\_EXTERN\_PRIORITY\_I   77 |
| --- |

## [◆ ](#ab50a3b95442a89e070163c623a261578)ESP\_EXTERN\_PRIORITY\_O

| #define ESP\_EXTERN\_PRIORITY\_O   77 |
| --- |

## [◆ ](#ade88988460c131e8c6775794588b0eb8)ESP\_FSPICLK\_IN

| #define ESP\_FSPICLK\_IN   63 |
| --- |

## [◆ ](#ab8c5397dc530f6326c3d10b31e59e168)ESP\_FSPICLK\_OUT

| #define ESP\_FSPICLK\_OUT   63 |
| --- |

## [◆ ](#a96ca1328e76337d289f6e65faf33d75c)ESP\_FSPICS0\_IN

| #define ESP\_FSPICS0\_IN   68 |
| --- |

## [◆ ](#ad1be1401b282275eaef46b9a598c6a40)ESP\_FSPICS0\_OUT

| #define ESP\_FSPICS0\_OUT   68 |
| --- |

## [◆ ](#a44ade9179a7ea00586359a009799661d)ESP\_FSPICS1\_OUT

| #define ESP\_FSPICS1\_OUT   69 |
| --- |

## [◆ ](#af991963f29c5b268a5f8fead8fd15348)ESP\_FSPICS2\_OUT

| #define ESP\_FSPICS2\_OUT   70 |
| --- |

## [◆ ](#a65d1170c5a68ac7f6a4457c3380ddfde)ESP\_FSPICS3\_OUT

| #define ESP\_FSPICS3\_OUT   71 |
| --- |

## [◆ ](#a83dafe68703c701dcd07d7ff0aadad01)ESP\_FSPICS4\_OUT

| #define ESP\_FSPICS4\_OUT   72 |
| --- |

## [◆ ](#ad8fab64bb220fd198a6cd931f4ea1e8e)ESP\_FSPICS5\_OUT

| #define ESP\_FSPICS5\_OUT   73 |
| --- |

## [◆ ](#a7910521af840d42edd3c0a667cf90c5f)ESP\_FSPID\_IN

| #define ESP\_FSPID\_IN   65 |
| --- |

## [◆ ](#a02bd34821e8a4bf0038b9af417ec161a)ESP\_FSPID\_OUT

| #define ESP\_FSPID\_OUT   65 |
| --- |

## [◆ ](#a60ff087a3d85a356d77f060a6698d00b)ESP\_FSPIHD\_IN

| #define ESP\_FSPIHD\_IN   66 |
| --- |

## [◆ ](#ac71bc137b93bd6c0c8a1ebe24a70a613)ESP\_FSPIHD\_OUT

| #define ESP\_FSPIHD\_OUT   66 |
| --- |

## [◆ ](#ab603b7bf7d016e85653a5c3be5c01293)ESP\_FSPIQ\_IN

| #define ESP\_FSPIQ\_IN   64 |
| --- |

## [◆ ](#a8b3ea6ad374fa010b46b48072fa87ccb)ESP\_FSPIQ\_OUT

| #define ESP\_FSPIQ\_OUT   64 |
| --- |

## [◆ ](#a4d4c4a13b820cab6d94da8fe08120a2f)ESP\_FSPIWP\_IN

| #define ESP\_FSPIWP\_IN   67 |
| --- |

## [◆ ](#a83c4f18d726984cc98caeea9b7677ca1)ESP\_FSPIWP\_OUT

| #define ESP\_FSPIWP\_OUT   67 |
| --- |

## [◆ ](#a2af8dc70a06105740ae181a616186624)ESP\_GPIO\_EVENT\_MATRIX\_IN0

| #define ESP\_GPIO\_EVENT\_MATRIX\_IN0   79 |
| --- |

## [◆ ](#a7a2ce6558a5368d1fc0325ce37487d1a)ESP\_GPIO\_EVENT\_MATRIX\_IN1

| #define ESP\_GPIO\_EVENT\_MATRIX\_IN1   80 |
| --- |

## [◆ ](#a2ae077cc87f156e9545eca4a091890e3)ESP\_GPIO\_EVENT\_MATRIX\_IN2

| #define ESP\_GPIO\_EVENT\_MATRIX\_IN2   81 |
| --- |

## [◆ ](#a97d8c86a5d7ba47196816c7d04ef7efb)ESP\_GPIO\_EVENT\_MATRIX\_IN3

| #define ESP\_GPIO\_EVENT\_MATRIX\_IN3   82 |
| --- |

## [◆ ](#afe5c166b887709cdd27bd37df85c45b9)ESP\_GPIO\_MAP\_DATE

| #define ESP\_GPIO\_MAP\_DATE   0x2106190 |
| --- |

## [◆ ](#aeee7dc180a750016e7711282b252ccf6)ESP\_GPIO\_TASK\_MATRIX\_OUT0

| #define ESP\_GPIO\_TASK\_MATRIX\_OUT0   79 |
| --- |

## [◆ ](#a4ce0ef64cebc11e961d73fc58d8bb954)ESP\_GPIO\_TASK\_MATRIX\_OUT1

| #define ESP\_GPIO\_TASK\_MATRIX\_OUT1   80 |
| --- |

## [◆ ](#a0ac11865f0be99e81bebeb7dfbe1424b)ESP\_GPIO\_TASK\_MATRIX\_OUT2

| #define ESP\_GPIO\_TASK\_MATRIX\_OUT2   81 |
| --- |

## [◆ ](#a165323f111794aeff16e7073501ff16e)ESP\_GPIO\_TASK\_MATRIX\_OUT3

| #define ESP\_GPIO\_TASK\_MATRIX\_OUT3   82 |
| --- |

## [◆ ](#ab607ce367da34ab0f1bd7fa648273cf1)ESP\_I2CEXT0\_SCL\_IN

| #define ESP\_I2CEXT0\_SCL\_IN   53 |
| --- |

## [◆ ](#a2144cc62df795547ccf2bbe3ee4c629f)ESP\_I2CEXT0\_SCL\_OUT

| #define ESP\_I2CEXT0\_SCL\_OUT   53 |
| --- |

## [◆ ](#afa7061c87135b9dabe5c54f5f4ce16e6)ESP\_I2CEXT0\_SDA\_IN

| #define ESP\_I2CEXT0\_SDA\_IN   54 |
| --- |

## [◆ ](#aabf1378b0ad2028c36c3bb74c81d7049)ESP\_I2CEXT0\_SDA\_OUT

| #define ESP\_I2CEXT0\_SDA\_OUT   54 |
| --- |

## [◆ ](#a62dfcd88747c61acb53dc85c1751f1d3)ESP\_LEDC\_LS\_SIG\_OUT0

| #define ESP\_LEDC\_LS\_SIG\_OUT0   45 |
| --- |

## [◆ ](#a5cad9206cfeea93b42e5456228c7d580)ESP\_LEDC\_LS\_SIG\_OUT1

| #define ESP\_LEDC\_LS\_SIG\_OUT1   46 |
| --- |

## [◆ ](#ab408070e7c700805db165c3876b6c588)ESP\_LEDC\_LS\_SIG\_OUT2

| #define ESP\_LEDC\_LS\_SIG\_OUT2   47 |
| --- |

## [◆ ](#a438aee217c6c94a2962a3d98935b5717)ESP\_LEDC\_LS\_SIG\_OUT3

| #define ESP\_LEDC\_LS\_SIG\_OUT3   48 |
| --- |

## [◆ ](#ada93dcffffc15362be4b7432a8033559)ESP\_LEDC\_LS\_SIG\_OUT4

| #define ESP\_LEDC\_LS\_SIG\_OUT4   49 |
| --- |

## [◆ ](#a34fc029ec45756ca7064580f57db1cc7)ESP\_LEDC\_LS\_SIG\_OUT5

| #define ESP\_LEDC\_LS\_SIG\_OUT5   50 |
| --- |

## [◆ ](#af80260535bc3aee44c28c972a29483e0)ESP\_NOSIG

| #define ESP\_NOSIG   [ESP\_SIG\_INVAL](esp-pinctrl-common_8h.md#ae0d2e726ab8d90343e5c80e1d9b85ad8) |
| --- |

## [◆ ](#ad9bae9b4884a356e465656d1ee8d61cd)ESP\_RMT\_SIG\_IN0

| #define ESP\_RMT\_SIG\_IN0   51 |
| --- |

## [◆ ](#ab6c6293e6845ba4bf4d05b84102ffdcf)ESP\_RMT\_SIG\_IN1

| #define ESP\_RMT\_SIG\_IN1   52 |
| --- |

## [◆ ](#a25343fbc20a0c542bcdc21cdfade867b)ESP\_RMT\_SIG\_OUT0

| #define ESP\_RMT\_SIG\_OUT0   51 |
| --- |

## [◆ ](#a6d082fb1c7397d784a3075108e0dea73)ESP\_RMT\_SIG\_OUT1

| #define ESP\_RMT\_SIG\_OUT1   52 |
| --- |

## [◆ ](#a645411759ffdc63f51f2cd42632d2720)ESP\_SIG\_GPIO\_OUT

| #define ESP\_SIG\_GPIO\_OUT   128 |
| --- |

## [◆ ](#a33f1fad3bde9b252dfb3a291d600c019)ESP\_SIG\_IN\_FUNC100

| #define ESP\_SIG\_IN\_FUNC100   100 |
| --- |

## [◆ ](#a919b1b0e57d8785970c702fcd49d5563)ESP\_SIG\_IN\_FUNC97

| #define ESP\_SIG\_IN\_FUNC97   97 |
| --- |

## [◆ ](#ae6043332289b10b68dc1d278681f3df1)ESP\_SIG\_IN\_FUNC98

| #define ESP\_SIG\_IN\_FUNC98   98 |
| --- |

## [◆ ](#a11dcdffc24ff5d98c7c8d0f609a0c7b9)ESP\_SIG\_IN\_FUNC99

| #define ESP\_SIG\_IN\_FUNC99   99 |
| --- |

## [◆ ](#a6684d495dfe99d0798f576018ffe0aba)ESP\_SIG\_IN\_FUNC\_100

| #define ESP\_SIG\_IN\_FUNC\_100   100 |
| --- |

## [◆ ](#a66890ae0c0e6a875c19099abb1918ca1)ESP\_SIG\_IN\_FUNC\_97

| #define ESP\_SIG\_IN\_FUNC\_97   97 |
| --- |

## [◆ ](#a848f955ed1b3b04d0a3d90f8c0acedec)ESP\_SIG\_IN\_FUNC\_98

| #define ESP\_SIG\_IN\_FUNC\_98   98 |
| --- |

## [◆ ](#ab6956182e8d06463813e94843398a45f)ESP\_SIG\_IN\_FUNC\_99

| #define ESP\_SIG\_IN\_FUNC\_99   99 |
| --- |

## [◆ ](#a5f440c922a53085bb7b28f469c2a14b0)ESP\_SPICLK\_OUT

| #define ESP\_SPICLK\_OUT   4 |
| --- |

## [◆ ](#aaf157f6b85a07f18b181876a7a04f142)ESP\_SPICLK\_OUT\_MUX

| #define ESP\_SPICLK\_OUT\_MUX   [ESP\_SPICLK\_OUT](#a5f440c922a53085bb7b28f469c2a14b0) |
| --- |

## [◆ ](#a5d97c07ba0d8cda594d52310e90fa6a4)ESP\_SPICS0\_OUT

| #define ESP\_SPICS0\_OUT   5 |
| --- |

## [◆ ](#aa4a67a38b97a3d466783c0617aa6a0c8)ESP\_SPICS1\_OUT

| #define ESP\_SPICS1\_OUT   19 |
| --- |

## [◆ ](#a26c603fd58dbd7526d2be3bb3e37758a)ESP\_SPID\_IN

| #define ESP\_SPID\_IN   1 |
| --- |

## [◆ ](#a6292a461f60010aec29fcc8356d514fd)ESP\_SPID\_MONITOR

| #define ESP\_SPID\_MONITOR   16 |
| --- |

## [◆ ](#af81b2fc65b68ed2238ab3367a8731102)ESP\_SPID\_OUT

| #define ESP\_SPID\_OUT   1 |
| --- |

## [◆ ](#a49783f877b666aff9362cf605590b991)ESP\_SPIHD\_IN

| #define ESP\_SPIHD\_IN   2 |
| --- |

## [◆ ](#aff145e44d8e8e506225362072c6c6710)ESP\_SPIHD\_MONITOR

| #define ESP\_SPIHD\_MONITOR   17 |
| --- |

## [◆ ](#a8851b5256482790f3304efecafc13afd)ESP\_SPIHD\_OUT

| #define ESP\_SPIHD\_OUT   2 |
| --- |

## [◆ ](#aec51ff955c6be50e529affc87ec9d5cb)ESP\_SPIQ\_IN

| #define ESP\_SPIQ\_IN   0 |
| --- |

## [◆ ](#a6abe131ab233461292f2987aadfee11a)ESP\_SPIQ\_MONITOR

| #define ESP\_SPIQ\_MONITOR   15 |
| --- |

## [◆ ](#a5816deeca8853397a830a8eb251704ee)ESP\_SPIQ\_OUT

| #define ESP\_SPIQ\_OUT   0 |
| --- |

## [◆ ](#aa74adc2812d9c6bd143c679fa4d9ca8d)ESP\_SPIWP\_IN

| #define ESP\_SPIWP\_IN   3 |
| --- |

## [◆ ](#a610bf782c52a09f754e16890a13851da)ESP\_SPIWP\_MONITOR

| #define ESP\_SPIWP\_MONITOR   18 |
| --- |

## [◆ ](#a470408f8102937dc017336e320e6147b)ESP\_SPIWP\_OUT

| #define ESP\_SPIWP\_OUT   3 |
| --- |

## [◆ ](#a530d7a918a97cd1fff1acf2f90edd4ca)ESP\_U0CTS\_IN

| #define ESP\_U0CTS\_IN   7 |
| --- |

## [◆ ](#a53e3a4557a4eb1f7f98250abef03c02a)ESP\_U0DSR\_IN

| #define ESP\_U0DSR\_IN   8 |
| --- |

## [◆ ](#acc8716af947169c9f167bdf215c5314c)ESP\_U0DTR\_OUT

| #define ESP\_U0DTR\_OUT   8 |
| --- |

## [◆ ](#a4257bbc044af6ea3612313e3a0b7e7c9)ESP\_U0RTS\_OUT

| #define ESP\_U0RTS\_OUT   7 |
| --- |

## [◆ ](#aca502efa55ce2286dc9eba28192681fd)ESP\_U0RXD\_IN

| #define ESP\_U0RXD\_IN   6 |
| --- |

## [◆ ](#af1e58fb8e7ef86a92171eca7bb1671af)ESP\_U0TXD\_OUT

| #define ESP\_U0TXD\_OUT   6 |
| --- |

## [◆ ](#a3c005e616da21a058960d6aed79427b3)ESP\_U1CTS\_IN

| #define ESP\_U1CTS\_IN   10 |
| --- |

## [◆ ](#a5f29b138691540598d0b977dc4bd5971)ESP\_U1DSR\_IN

| #define ESP\_U1DSR\_IN   11 |
| --- |

## [◆ ](#a1f7df042d40ec6f20b559ef6778d7497)ESP\_U1DTR\_OUT

| #define ESP\_U1DTR\_OUT   11 |
| --- |

## [◆ ](#a8f6399745566bd5caa2020e4dcb2bb3b)ESP\_U1RTS\_OUT

| #define ESP\_U1RTS\_OUT   10 |
| --- |

## [◆ ](#a2293e0646e0ad2f76d62f76425ae6770)ESP\_U1RXD\_IN

| #define ESP\_U1RXD\_IN   9 |
| --- |

## [◆ ](#a6053b38147e28e3a7479b38e7d195136)ESP\_U1TXD\_OUT

| #define ESP\_U1TXD\_OUT   9 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp32c2-gpio-sigmap.h](esp32c2-gpio-sigmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
