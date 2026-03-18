---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/esp32c3-gpio-sigmap_8h.html
original_path: doxygen/html/esp32c3-gpio-sigmap_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32c3-gpio-sigmap.h File Reference

[Go to the source code of this file.](esp32c3-gpio-sigmap_8h_source.md)

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
| #define | [ESP\_I2S\_MCLK\_IN](#a0c2eefdd5846623d330a6437ecfec3ef)   12 |
| #define | [ESP\_I2S\_MCLK\_OUT](#a89708f46a7a1e03c9a654e9a529ec36c)   12 |
| #define | [ESP\_I2SO\_BCK\_IN](#aa4d5f8ce3cc15e7ab7b2d17c79da3b91)   13 |
| #define | [ESP\_I2SO\_BCK\_OUT](#ab586cc1b4ae5da20703f469bb8ff5c0e)   13 |
| #define | [ESP\_I2SO\_WS\_IN](#a2f5d7f663b568a4a609f8c9315f6cf5c)   14 |
| #define | [ESP\_I2SO\_WS\_OUT](#a4be8f5f82ae51e880973256e748ef0a3)   14 |
| #define | [ESP\_I2SI\_SD\_IN](#ac2d5d005dd8d5d5487dd24e021f2d3d5)   15 |
| #define | [ESP\_I2SO\_SD\_OUT](#a2815be93d2102f382e8ed5c5f7913257)   15 |
| #define | [ESP\_I2SI\_BCK\_IN](#a0bc2c2947bb51d411a677fc07806e3fe)   16 |
| #define | [ESP\_I2SI\_BCK\_OUT](#aa58a3701e86830736ae9b0b3d60ac6b5)   16 |
| #define | [ESP\_I2SI\_WS\_IN](#af1e51d50da781c498cda9e45e603544f)   17 |
| #define | [ESP\_I2SI\_WS\_OUT](#aa0c2097b8e33d93001180bc068b85d5c)   17 |
| #define | [ESP\_GPIO\_BT\_PRIORITY](#ab8d0a9090c64518af59274603f035042)   18 |
| #define | [ESP\_GPIO\_WLAN\_PRIO](#adf2824b1611032a81fe7b3c41253c0d8)   18 |
| #define | [ESP\_GPIO\_BT\_ACTIVE](#a47d854bfae0f88dc023613e61e6be551)   19 |
| #define | [ESP\_GPIO\_WLAN\_ACTIVE](#af675ca03172d2dcee1e19ccb5236e087)   19 |
| #define | [ESP\_BB\_DIAG0](#a304bc90cc758f90f6675fea611ab0cfe)   20 |
| #define | [ESP\_BB\_DIAG1](#ad236bf991329914d59c194ff9003974a)   21 |
| #define | [ESP\_BB\_DIAG2](#a26c20261a5e2f4293b81c802a0a33b19)   22 |
| #define | [ESP\_BB\_DIAG3](#a5124ef75b703e7805bccd8c93828faae)   23 |
| #define | [ESP\_BB\_DIAG4](#aebd2c37b71d18967bd394b32c820647f)   24 |
| #define | [ESP\_BB\_DIAG5](#ace166b18a74fb8a42f876d1aa7cfb059)   25 |
| #define | [ESP\_BB\_DIAG6](#ad5685b19c170cc428cea0ee91f9155b0)   26 |
| #define | [ESP\_BB\_DIAG7](#aedf32208932dfe4471f6a5a7feb652f8)   27 |
| #define | [ESP\_BB\_DIAG8](#a126e2108473183890c6a2e148f8fd2c7)   28 |
| #define | [ESP\_BB\_DIAG9](#a75b60b1b4d53e6fca02b3a4f14ea530e)   29 |
| #define | [ESP\_BB\_DIAG10](#aed67caee00b7ceaaaa33b2917aba60f2)   30 |
| #define | [ESP\_BB\_DIAG11](#aef4bb5d62b93dfc3f2834404b6945b90)   31 |
| #define | [ESP\_BB\_DIAG12](#acc6cd70ce139a5639022bec896a3ba5e)   32 |
| #define | [ESP\_BB\_DIAG13](#afa72089303bf662a4efc8c068b157f0d)   33 |
| #define | [ESP\_BB\_DIAG14](#a4ef00458e2547f7141741191b92854d8)   34 |
| #define | [ESP\_BB\_DIAG15](#aed7c06883c6a69303a341454aff409ed)   35 |
| #define | [ESP\_BB\_DIAG16](#a1acc29dd7c0517c30299e71c1a6ce7fa)   36 |
| #define | [ESP\_BB\_DIAG17](#a9abbf3178088e44d984b088f53c25ab1)   37 |
| #define | [ESP\_BB\_DIAG18](#af75798fba81841339510ecc5f94e542e)   38 |
| #define | [ESP\_BB\_DIAG19](#a4102e08a6e29f2164f5aafa109ab734b)   39 |
| #define | [ESP\_USB\_EXTPHY\_VP](#a7c2bcf73d61315a0d8c71d68173f9860)   40 |
| #define | [ESP\_USB\_EXTPHY\_OEN](#a28f381128449aed0ae738516df39790c)   40 |
| #define | [ESP\_USB\_EXTPHY\_VM](#aeaa130d2e220f2ebd073983921ad3679)   41 |
| #define | [ESP\_USB\_EXTPHY\_SPEED](#aedb10271abe4c1969eefbc0425681652)   41 |
| #define | [ESP\_USB\_EXTPHY\_RCV](#a095d83d616afb08c4b06d82c4d907fee)   42 |
| #define | [ESP\_USB\_EXTPHY\_VPO](#a88c6a9f957332dac96360dd3f631e59b)   42 |
| #define | [ESP\_USB\_EXTPHY\_VMO](#abaeb7b2bb8208db93655b442293976aa)   43 |
| #define | [ESP\_USB\_EXTPHY\_SUSPND](#a301551d0d524f785b3d0e2c35bc81ce5)   44 |
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
| #define | [ESP\_GPIO\_SD0\_OUT](#ae59035f8269ccd564ba0d7b2b078b3ee)   55 |
| #define | [ESP\_GPIO\_SD1\_OUT](#a3fbed77581ed14fa077f314e812b9c36)   56 |
| #define | [ESP\_GPIO\_SD2\_OUT](#a2668d9083ce28563cc160fe1102e927d)   57 |
| #define | [ESP\_GPIO\_SD3\_OUT](#a9d34f616894f98d7175c41b4ba565f8d)   58 |
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
| #define | [ESP\_TWAI\_RX](#ab3da303c2f9226f9648669c17af8377a)   74 |
| #define | [ESP\_TWAI\_TX](#a3b13bb40583aaa0f85de982509247614)   74 |
| #define | [ESP\_TWAI\_BUS\_OFF\_ON](#a6d0d41d1ec0f6fc626861f5857684e6d)   75 |
| #define | [ESP\_TWAI\_CLKOUT](#a1c69791269fdbb2a11f66f33eb4066be)   76 |
| #define | [ESP\_PCMFSYNC\_IN](#a0ad409b608ef2a418098b4e51d0e7e9a)   77 |
| #define | [ESP\_BT\_AUDIO0\_IRQ](#afd2befcf5eb0c413c0f8447558dc4863)   77 |
| #define | [ESP\_PCMCLK\_IN](#abb4d1f28362c68cf3f1e9f1696602b03)   78 |
| #define | [ESP\_BT\_AUDIO1\_IRQ](#acfe665b9ff21a51b93819a3f123180ad)   78 |
| #define | [ESP\_PCMDIN](#ae94f8dfc2be2c0cf8863a33df76d5295)   79 |
| #define | [ESP\_BT\_AUDIO2\_IRQ](#a77ac554a2a10fc6fa77106e8af9dfc86)   79 |
| #define | [ESP\_RW\_WAKEUP\_REQ](#a7abc844342f6483be73ea503d3f76d89)   80 |
| #define | [ESP\_BLE\_AUDIO0\_IRQ](#ab2e25b779a18acd66533795433291a3d)   80 |
| #define | [ESP\_BLE\_AUDIO1\_IRQ](#ab4b3d654c674536c2c63070210147372)   81 |
| #define | [ESP\_BLE\_AUDIO2\_IRQ](#a637ea6fcad7b2e5fe48cf9e3419fbed6)   82 |
| #define | [ESP\_PCMFSYNC\_OUT](#a8b79d6e15573a684058c9b933f469f09)   83 |
| #define | [ESP\_PCMCLK\_OUT](#a500651ca0d6daa86774a0f45190f8b38)   84 |
| #define | [ESP\_PCMDOUT](#ab3ecd7e5557112172c38bff3b2605e9c)   85 |
| #define | [ESP\_BLE\_AUDIO\_SYNC0\_P](#aba2aea8feedc96a0a6b3bba007df49ac)   86 |
| #define | [ESP\_BLE\_AUDIO\_SYNC1\_P](#a21e5bf1c7c33a39f11d8bf6537ed85bb)   87 |
| #define | [ESP\_BLE\_AUDIO\_SYNC2\_P](#a961f37a0b2dcb9e183331ef5684f8504)   88 |
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
| #define | [ESP\_SYNCERR](#a0206456525cd6dc235ed6892e98731c6)   101 |
| #define | [ESP\_SYNCFOUND\_FLAG](#aa62bd8539c4d89abaa542d8bd4c91efd)   102 |
| #define | [ESP\_EVT\_CNTL\_IMMEDIATE\_ABORT](#ade4ee47d8f72c009686b2454ee77ee60)   103 |
| #define | [ESP\_LINKLBL](#ac5684072c6c5fbbdb6631d73270819dc)   104 |
| #define | [ESP\_DATA\_EN](#a1029a66c0538d7eb1026ced27d54a59b)   105 |
| #define | [ESP\_DATA](#a04dc693cfec6739602b92e86a837c58d)   106 |
| #define | [ESP\_PKT\_TX\_ON](#aecac02e2195c5da81f63ed4c19bd06fb)   107 |
| #define | [ESP\_PKT\_RX\_ON](#a63f7ec6fc7927b0f0fb3bd0dc733de5a)   108 |
| #define | [ESP\_RW\_TX\_ON](#a3b8a7f22861948aa8809aa58ecbdb0ef)   109 |
| #define | [ESP\_RW\_RX\_ON](#a5f93eee3354e5fd70d11fd26c9dd25bb)   110 |
| #define | [ESP\_EVT\_REQ\_P](#af7d8fb5a97cb0e4f3dad1a73fb0610d5)   111 |
| #define | [ESP\_EVT\_STOP\_P](#a10fd19b9a6140fea7e88facaa02686be)   112 |
| #define | [ESP\_BT\_MODE\_ON](#a08a40a396cf075e77aa50acfb811885a)   113 |
| #define | [ESP\_GPIO\_LC\_DIAG0](#a80a3804720f2e69ac5caa52c0ade9d5b)   114 |
| #define | [ESP\_GPIO\_LC\_DIAG1](#ad842d1a31efaf5f3edc70326ac89df9b)   115 |
| #define | [ESP\_GPIO\_LC\_DIAG2](#ad23ea4680ce2cbf713bb456dae84e35b)   116 |
| #define | [ESP\_CH](#a83ab157d422c3004c3dc287c0c804ec5)   117 |
| #define | [ESP\_RX\_WINDOW](#a546d9b83cad2a5b2e64677be087b1f9d)   118 |
| #define | [ESP\_UPDATE\_RX](#a25d03cedd231864f508e405d0ae2fa4b)   119 |
| #define | [ESP\_RX\_STATUS](#ac2450d1a096d1adf2386ba91e0a92f75)   120 |
| #define | [ESP\_CLK\_GPIO](#ae27ee8b3a05b497ec7bea2ed69fc9230)   121 |
| #define | [ESP\_NBT\_BLE](#a9aa8b294d23efae4cd5a6dd741829aad)   122 |
| #define | [ESP\_CLK\_OUT\_OUT1](#a12a2380f8bcbf158e7c114b7dc1701a5)   123 |
| #define | [ESP\_CLK\_OUT\_OUT2](#adf7a9c85596f3a536ddb603d3218cee2)   124 |
| #define | [ESP\_CLK\_OUT\_OUT3](#af421f62c654ecca5136b7b526f168377)   125 |
| #define | [ESP\_SPICS1\_OUT](#aa4a67a38b97a3d466783c0617aa6a0c8)   126 |
| #define | [ESP\_SIG\_GPIO\_OUT](#a645411759ffdc63f51f2cd42632d2720)   128 |
| #define | [ESP\_GPIO\_MAP\_DATE](#afe5c166b887709cdd27bd37df85c45b9)   0x2006130 |

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

## [◆ ](#a304bc90cc758f90f6675fea611ab0cfe)ESP\_BB\_DIAG0

| #define ESP\_BB\_DIAG0   20 |
| --- |

## [◆ ](#ad236bf991329914d59c194ff9003974a)ESP\_BB\_DIAG1

| #define ESP\_BB\_DIAG1   21 |
| --- |

## [◆ ](#aed67caee00b7ceaaaa33b2917aba60f2)ESP\_BB\_DIAG10

| #define ESP\_BB\_DIAG10   30 |
| --- |

## [◆ ](#aef4bb5d62b93dfc3f2834404b6945b90)ESP\_BB\_DIAG11

| #define ESP\_BB\_DIAG11   31 |
| --- |

## [◆ ](#acc6cd70ce139a5639022bec896a3ba5e)ESP\_BB\_DIAG12

| #define ESP\_BB\_DIAG12   32 |
| --- |

## [◆ ](#afa72089303bf662a4efc8c068b157f0d)ESP\_BB\_DIAG13

| #define ESP\_BB\_DIAG13   33 |
| --- |

## [◆ ](#a4ef00458e2547f7141741191b92854d8)ESP\_BB\_DIAG14

| #define ESP\_BB\_DIAG14   34 |
| --- |

## [◆ ](#aed7c06883c6a69303a341454aff409ed)ESP\_BB\_DIAG15

| #define ESP\_BB\_DIAG15   35 |
| --- |

## [◆ ](#a1acc29dd7c0517c30299e71c1a6ce7fa)ESP\_BB\_DIAG16

| #define ESP\_BB\_DIAG16   36 |
| --- |

## [◆ ](#a9abbf3178088e44d984b088f53c25ab1)ESP\_BB\_DIAG17

| #define ESP\_BB\_DIAG17   37 |
| --- |

## [◆ ](#af75798fba81841339510ecc5f94e542e)ESP\_BB\_DIAG18

| #define ESP\_BB\_DIAG18   38 |
| --- |

## [◆ ](#a4102e08a6e29f2164f5aafa109ab734b)ESP\_BB\_DIAG19

| #define ESP\_BB\_DIAG19   39 |
| --- |

## [◆ ](#a26c20261a5e2f4293b81c802a0a33b19)ESP\_BB\_DIAG2

| #define ESP\_BB\_DIAG2   22 |
| --- |

## [◆ ](#a5124ef75b703e7805bccd8c93828faae)ESP\_BB\_DIAG3

| #define ESP\_BB\_DIAG3   23 |
| --- |

## [◆ ](#aebd2c37b71d18967bd394b32c820647f)ESP\_BB\_DIAG4

| #define ESP\_BB\_DIAG4   24 |
| --- |

## [◆ ](#ace166b18a74fb8a42f876d1aa7cfb059)ESP\_BB\_DIAG5

| #define ESP\_BB\_DIAG5   25 |
| --- |

## [◆ ](#ad5685b19c170cc428cea0ee91f9155b0)ESP\_BB\_DIAG6

| #define ESP\_BB\_DIAG6   26 |
| --- |

## [◆ ](#aedf32208932dfe4471f6a5a7feb652f8)ESP\_BB\_DIAG7

| #define ESP\_BB\_DIAG7   27 |
| --- |

## [◆ ](#a126e2108473183890c6a2e148f8fd2c7)ESP\_BB\_DIAG8

| #define ESP\_BB\_DIAG8   28 |
| --- |

## [◆ ](#a75b60b1b4d53e6fca02b3a4f14ea530e)ESP\_BB\_DIAG9

| #define ESP\_BB\_DIAG9   29 |
| --- |

## [◆ ](#ab2e25b779a18acd66533795433291a3d)ESP\_BLE\_AUDIO0\_IRQ

| #define ESP\_BLE\_AUDIO0\_IRQ   80 |
| --- |

## [◆ ](#ab4b3d654c674536c2c63070210147372)ESP\_BLE\_AUDIO1\_IRQ

| #define ESP\_BLE\_AUDIO1\_IRQ   81 |
| --- |

## [◆ ](#a637ea6fcad7b2e5fe48cf9e3419fbed6)ESP\_BLE\_AUDIO2\_IRQ

| #define ESP\_BLE\_AUDIO2\_IRQ   82 |
| --- |

## [◆ ](#aba2aea8feedc96a0a6b3bba007df49ac)ESP\_BLE\_AUDIO\_SYNC0\_P

| #define ESP\_BLE\_AUDIO\_SYNC0\_P   86 |
| --- |

## [◆ ](#a21e5bf1c7c33a39f11d8bf6537ed85bb)ESP\_BLE\_AUDIO\_SYNC1\_P

| #define ESP\_BLE\_AUDIO\_SYNC1\_P   87 |
| --- |

## [◆ ](#a961f37a0b2dcb9e183331ef5684f8504)ESP\_BLE\_AUDIO\_SYNC2\_P

| #define ESP\_BLE\_AUDIO\_SYNC2\_P   88 |
| --- |

## [◆ ](#afd2befcf5eb0c413c0f8447558dc4863)ESP\_BT\_AUDIO0\_IRQ

| #define ESP\_BT\_AUDIO0\_IRQ   77 |
| --- |

## [◆ ](#acfe665b9ff21a51b93819a3f123180ad)ESP\_BT\_AUDIO1\_IRQ

| #define ESP\_BT\_AUDIO1\_IRQ   78 |
| --- |

## [◆ ](#a77ac554a2a10fc6fa77106e8af9dfc86)ESP\_BT\_AUDIO2\_IRQ

| #define ESP\_BT\_AUDIO2\_IRQ   79 |
| --- |

## [◆ ](#a08a40a396cf075e77aa50acfb811885a)ESP\_BT\_MODE\_ON

| #define ESP\_BT\_MODE\_ON   113 |
| --- |

## [◆ ](#a83ab157d422c3004c3dc287c0c804ec5)ESP\_CH

| #define ESP\_CH   117 |
| --- |

## [◆ ](#ae27ee8b3a05b497ec7bea2ed69fc9230)ESP\_CLK\_GPIO

| #define ESP\_CLK\_GPIO   121 |
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

## [◆ ](#a04dc693cfec6739602b92e86a837c58d)ESP\_DATA

| #define ESP\_DATA   106 |
| --- |

## [◆ ](#a1029a66c0538d7eb1026ced27d54a59b)ESP\_DATA\_EN

| #define ESP\_DATA\_EN   105 |
| --- |

## [◆ ](#ade4ee47d8f72c009686b2454ee77ee60)ESP\_EVT\_CNTL\_IMMEDIATE\_ABORT

| #define ESP\_EVT\_CNTL\_IMMEDIATE\_ABORT   103 |
| --- |

## [◆ ](#af7d8fb5a97cb0e4f3dad1a73fb0610d5)ESP\_EVT\_REQ\_P

| #define ESP\_EVT\_REQ\_P   111 |
| --- |

## [◆ ](#a10fd19b9a6140fea7e88facaa02686be)ESP\_EVT\_STOP\_P

| #define ESP\_EVT\_STOP\_P   112 |
| --- |

## [◆ ](#ae49b4527d8fbd0f5c8e3edc72704c54a)ESP\_EXT\_ADC\_START

| #define ESP\_EXT\_ADC\_START   45 |
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

## [◆ ](#a47d854bfae0f88dc023613e61e6be551)ESP\_GPIO\_BT\_ACTIVE

| #define ESP\_GPIO\_BT\_ACTIVE   19 |
| --- |

## [◆ ](#ab8d0a9090c64518af59274603f035042)ESP\_GPIO\_BT\_PRIORITY

| #define ESP\_GPIO\_BT\_PRIORITY   18 |
| --- |

## [◆ ](#a80a3804720f2e69ac5caa52c0ade9d5b)ESP\_GPIO\_LC\_DIAG0

| #define ESP\_GPIO\_LC\_DIAG0   114 |
| --- |

## [◆ ](#ad842d1a31efaf5f3edc70326ac89df9b)ESP\_GPIO\_LC\_DIAG1

| #define ESP\_GPIO\_LC\_DIAG1   115 |
| --- |

## [◆ ](#ad23ea4680ce2cbf713bb456dae84e35b)ESP\_GPIO\_LC\_DIAG2

| #define ESP\_GPIO\_LC\_DIAG2   116 |
| --- |

## [◆ ](#afe5c166b887709cdd27bd37df85c45b9)ESP\_GPIO\_MAP\_DATE

| #define ESP\_GPIO\_MAP\_DATE   0x2006130 |
| --- |

## [◆ ](#ae59035f8269ccd564ba0d7b2b078b3ee)ESP\_GPIO\_SD0\_OUT

| #define ESP\_GPIO\_SD0\_OUT   55 |
| --- |

## [◆ ](#a3fbed77581ed14fa077f314e812b9c36)ESP\_GPIO\_SD1\_OUT

| #define ESP\_GPIO\_SD1\_OUT   56 |
| --- |

## [◆ ](#a2668d9083ce28563cc160fe1102e927d)ESP\_GPIO\_SD2\_OUT

| #define ESP\_GPIO\_SD2\_OUT   57 |
| --- |

## [◆ ](#a9d34f616894f98d7175c41b4ba565f8d)ESP\_GPIO\_SD3\_OUT

| #define ESP\_GPIO\_SD3\_OUT   58 |
| --- |

## [◆ ](#af675ca03172d2dcee1e19ccb5236e087)ESP\_GPIO\_WLAN\_ACTIVE

| #define ESP\_GPIO\_WLAN\_ACTIVE   19 |
| --- |

## [◆ ](#adf2824b1611032a81fe7b3c41253c0d8)ESP\_GPIO\_WLAN\_PRIO

| #define ESP\_GPIO\_WLAN\_PRIO   18 |
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

## [◆ ](#a0c2eefdd5846623d330a6437ecfec3ef)ESP\_I2S\_MCLK\_IN

| #define ESP\_I2S\_MCLK\_IN   12 |
| --- |

## [◆ ](#a89708f46a7a1e03c9a654e9a529ec36c)ESP\_I2S\_MCLK\_OUT

| #define ESP\_I2S\_MCLK\_OUT   12 |
| --- |

## [◆ ](#a0bc2c2947bb51d411a677fc07806e3fe)ESP\_I2SI\_BCK\_IN

| #define ESP\_I2SI\_BCK\_IN   16 |
| --- |

## [◆ ](#aa58a3701e86830736ae9b0b3d60ac6b5)ESP\_I2SI\_BCK\_OUT

| #define ESP\_I2SI\_BCK\_OUT   16 |
| --- |

## [◆ ](#ac2d5d005dd8d5d5487dd24e021f2d3d5)ESP\_I2SI\_SD\_IN

| #define ESP\_I2SI\_SD\_IN   15 |
| --- |

## [◆ ](#af1e51d50da781c498cda9e45e603544f)ESP\_I2SI\_WS\_IN

| #define ESP\_I2SI\_WS\_IN   17 |
| --- |

## [◆ ](#aa0c2097b8e33d93001180bc068b85d5c)ESP\_I2SI\_WS\_OUT

| #define ESP\_I2SI\_WS\_OUT   17 |
| --- |

## [◆ ](#aa4d5f8ce3cc15e7ab7b2d17c79da3b91)ESP\_I2SO\_BCK\_IN

| #define ESP\_I2SO\_BCK\_IN   13 |
| --- |

## [◆ ](#ab586cc1b4ae5da20703f469bb8ff5c0e)ESP\_I2SO\_BCK\_OUT

| #define ESP\_I2SO\_BCK\_OUT   13 |
| --- |

## [◆ ](#a2815be93d2102f382e8ed5c5f7913257)ESP\_I2SO\_SD\_OUT

| #define ESP\_I2SO\_SD\_OUT   15 |
| --- |

## [◆ ](#a2f5d7f663b568a4a609f8c9315f6cf5c)ESP\_I2SO\_WS\_IN

| #define ESP\_I2SO\_WS\_IN   14 |
| --- |

## [◆ ](#a4be8f5f82ae51e880973256e748ef0a3)ESP\_I2SO\_WS\_OUT

| #define ESP\_I2SO\_WS\_OUT   14 |
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

## [◆ ](#ac5684072c6c5fbbdb6631d73270819dc)ESP\_LINKLBL

| #define ESP\_LINKLBL   104 |
| --- |

## [◆ ](#a9aa8b294d23efae4cd5a6dd741829aad)ESP\_NBT\_BLE

| #define ESP\_NBT\_BLE   122 |
| --- |

## [◆ ](#af80260535bc3aee44c28c972a29483e0)ESP\_NOSIG

| #define ESP\_NOSIG   [ESP\_SIG\_INVAL](esp-pinctrl-common_8h.md#ae0d2e726ab8d90343e5c80e1d9b85ad8) |
| --- |

## [◆ ](#abb4d1f28362c68cf3f1e9f1696602b03)ESP\_PCMCLK\_IN

| #define ESP\_PCMCLK\_IN   78 |
| --- |

## [◆ ](#a500651ca0d6daa86774a0f45190f8b38)ESP\_PCMCLK\_OUT

| #define ESP\_PCMCLK\_OUT   84 |
| --- |

## [◆ ](#ae94f8dfc2be2c0cf8863a33df76d5295)ESP\_PCMDIN

| #define ESP\_PCMDIN   79 |
| --- |

## [◆ ](#ab3ecd7e5557112172c38bff3b2605e9c)ESP\_PCMDOUT

| #define ESP\_PCMDOUT   85 |
| --- |

## [◆ ](#a0ad409b608ef2a418098b4e51d0e7e9a)ESP\_PCMFSYNC\_IN

| #define ESP\_PCMFSYNC\_IN   77 |
| --- |

## [◆ ](#a8b79d6e15573a684058c9b933f469f09)ESP\_PCMFSYNC\_OUT

| #define ESP\_PCMFSYNC\_OUT   83 |
| --- |

## [◆ ](#a63f7ec6fc7927b0f0fb3bd0dc733de5a)ESP\_PKT\_RX\_ON

| #define ESP\_PKT\_RX\_ON   108 |
| --- |

## [◆ ](#aecac02e2195c5da81f63ed4c19bd06fb)ESP\_PKT\_TX\_ON

| #define ESP\_PKT\_TX\_ON   107 |
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

## [◆ ](#a5f93eee3354e5fd70d11fd26c9dd25bb)ESP\_RW\_RX\_ON

| #define ESP\_RW\_RX\_ON   110 |
| --- |

## [◆ ](#a3b8a7f22861948aa8809aa58ecbdb0ef)ESP\_RW\_TX\_ON

| #define ESP\_RW\_TX\_ON   109 |
| --- |

## [◆ ](#a7abc844342f6483be73ea503d3f76d89)ESP\_RW\_WAKEUP\_REQ

| #define ESP\_RW\_WAKEUP\_REQ   80 |
| --- |

## [◆ ](#ac2450d1a096d1adf2386ba91e0a92f75)ESP\_RX\_STATUS

| #define ESP\_RX\_STATUS   120 |
| --- |

## [◆ ](#a546d9b83cad2a5b2e64677be087b1f9d)ESP\_RX\_WINDOW

| #define ESP\_RX\_WINDOW   118 |
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

| #define ESP\_SPICS1\_OUT   126 |
| --- |

## [◆ ](#a26c603fd58dbd7526d2be3bb3e37758a)ESP\_SPID\_IN

| #define ESP\_SPID\_IN   1 |
| --- |

## [◆ ](#af81b2fc65b68ed2238ab3367a8731102)ESP\_SPID\_OUT

| #define ESP\_SPID\_OUT   1 |
| --- |

## [◆ ](#a49783f877b666aff9362cf605590b991)ESP\_SPIHD\_IN

| #define ESP\_SPIHD\_IN   2 |
| --- |

## [◆ ](#a8851b5256482790f3304efecafc13afd)ESP\_SPIHD\_OUT

| #define ESP\_SPIHD\_OUT   2 |
| --- |

## [◆ ](#aec51ff955c6be50e529affc87ec9d5cb)ESP\_SPIQ\_IN

| #define ESP\_SPIQ\_IN   0 |
| --- |

## [◆ ](#a5816deeca8853397a830a8eb251704ee)ESP\_SPIQ\_OUT

| #define ESP\_SPIQ\_OUT   0 |
| --- |

## [◆ ](#aa74adc2812d9c6bd143c679fa4d9ca8d)ESP\_SPIWP\_IN

| #define ESP\_SPIWP\_IN   3 |
| --- |

## [◆ ](#a470408f8102937dc017336e320e6147b)ESP\_SPIWP\_OUT

| #define ESP\_SPIWP\_OUT   3 |
| --- |

## [◆ ](#a0206456525cd6dc235ed6892e98731c6)ESP\_SYNCERR

| #define ESP\_SYNCERR   101 |
| --- |

## [◆ ](#aa62bd8539c4d89abaa542d8bd4c91efd)ESP\_SYNCFOUND\_FLAG

| #define ESP\_SYNCFOUND\_FLAG   102 |
| --- |

## [◆ ](#a6d0d41d1ec0f6fc626861f5857684e6d)ESP\_TWAI\_BUS\_OFF\_ON

| #define ESP\_TWAI\_BUS\_OFF\_ON   75 |
| --- |

## [◆ ](#a1c69791269fdbb2a11f66f33eb4066be)ESP\_TWAI\_CLKOUT

| #define ESP\_TWAI\_CLKOUT   76 |
| --- |

## [◆ ](#ab3da303c2f9226f9648669c17af8377a)ESP\_TWAI\_RX

| #define ESP\_TWAI\_RX   74 |
| --- |

## [◆ ](#a3b13bb40583aaa0f85de982509247614)ESP\_TWAI\_TX

| #define ESP\_TWAI\_TX   74 |
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

## [◆ ](#a25d03cedd231864f508e405d0ae2fa4b)ESP\_UPDATE\_RX

| #define ESP\_UPDATE\_RX   119 |
| --- |

## [◆ ](#a28f381128449aed0ae738516df39790c)ESP\_USB\_EXTPHY\_OEN

| #define ESP\_USB\_EXTPHY\_OEN   40 |
| --- |

## [◆ ](#a095d83d616afb08c4b06d82c4d907fee)ESP\_USB\_EXTPHY\_RCV

| #define ESP\_USB\_EXTPHY\_RCV   42 |
| --- |

## [◆ ](#aedb10271abe4c1969eefbc0425681652)ESP\_USB\_EXTPHY\_SPEED

| #define ESP\_USB\_EXTPHY\_SPEED   41 |
| --- |

## [◆ ](#a301551d0d524f785b3d0e2c35bc81ce5)ESP\_USB\_EXTPHY\_SUSPND

| #define ESP\_USB\_EXTPHY\_SUSPND   44 |
| --- |

## [◆ ](#aeaa130d2e220f2ebd073983921ad3679)ESP\_USB\_EXTPHY\_VM

| #define ESP\_USB\_EXTPHY\_VM   41 |
| --- |

## [◆ ](#abaeb7b2bb8208db93655b442293976aa)ESP\_USB\_EXTPHY\_VMO

| #define ESP\_USB\_EXTPHY\_VMO   43 |
| --- |

## [◆ ](#a7c2bcf73d61315a0d8c71d68173f9860)ESP\_USB\_EXTPHY\_VP

| #define ESP\_USB\_EXTPHY\_VP   40 |
| --- |

## [◆ ](#a88c6a9f957332dac96360dd3f631e59b)ESP\_USB\_EXTPHY\_VPO

| #define ESP\_USB\_EXTPHY\_VPO   42 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp32c3-gpio-sigmap.h](esp32c3-gpio-sigmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
