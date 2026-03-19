---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/numaker__m2l31x__reset_8h_source.html
original_path: doxygen/html/numaker__m2l31x__reset_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

numaker\_m2l31x\_reset.h

[Go to the documentation of this file.](numaker__m2l31x__reset_8h.md)

1/\*

2 \* Copyright (c) 2024 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_NUMAKER\_M2L31X\_RESET\_H

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_NUMAKER\_M2L31X\_RESET\_H

9

10/\* Beginning of M2L31 BSP sys\_reg.h reset module copy \*/

11

[ 12](numaker__m2l31x__reset_8h.md#a91dbb5cd2288749de7d8d79d87b34e53)#define LPSCC\_IPRST0\_LPPDMA0RST\_Pos 0

[ 13](numaker__m2l31x__reset_8h.md#a9ec52faec3524724e8b79fc4b5651f28)#define LPSCC\_IPRST0\_LPGPIORST\_Pos 1

[ 14](numaker__m2l31x__reset_8h.md#a0f19813f5317b1133de460892c33adc7)#define LPSCC\_IPRST0\_LPSRAMRST\_Pos 2

[ 15](numaker__m2l31x__reset_8h.md#a494764b83aa78fa3998ee11297e33196)#define LPSCC\_IPRST0\_WDTRST\_Pos 16

[ 16](numaker__m2l31x__reset_8h.md#a339c7ce190d88b0eac6dd49eeb893168)#define LPSCC\_IPRST0\_LPSPI0RST\_Pos 17

[ 17](numaker__m2l31x__reset_8h.md#a91d7e2985d49b29aea95fc1de6aeae26)#define LPSCC\_IPRST0\_LPI2C0RST\_Pos 18

[ 18](numaker__m2l31x__reset_8h.md#a9772112c07eefa688b691fc6227d2eda)#define LPSCC\_IPRST0\_LPUART0RST\_Pos 19

[ 19](numaker__m2l31x__reset_8h.md#aa73782147553d540b5c2f10d1988e5a5)#define LPSCC\_IPRST0\_LPTMR0RST\_Pos 20

[ 20](numaker__m2l31x__reset_8h.md#a89e0d4641eb8c1b6a6fbe03e2e150b5a)#define LPSCC\_IPRST0\_LPTMR1RST\_Pos 21

[ 21](numaker__m2l31x__reset_8h.md#a1a87a696788782abb6e8e36ff6f58e6e)#define LPSCC\_IPRST0\_TTMR0RST\_Pos 22

[ 22](numaker__m2l31x__reset_8h.md#ae34b8264ca021974731d218c296b4aad)#define LPSCC\_IPRST0\_TTMR1RST\_Pos 23

[ 23](numaker__m2l31x__reset_8h.md#a4eac93a8de761231b68b8d103828fb40)#define LPSCC\_IPRST0\_LPADC0RST\_Pos 24

[ 24](numaker__m2l31x__reset_8h.md#a6b75f8228685418dca42a31a913df284)#define LPSCC\_IPRST0\_OPARST\_Pos 27

[ 25](numaker__m2l31x__reset_8h.md#ad96a7ffe40464351e0de11cb9117a665)#define SYS\_IPRST0\_CHIPRST\_Pos 0

[ 26](numaker__m2l31x__reset_8h.md#a5d2955bb3ae1751c94b131f639c5cbbd)#define SYS\_IPRST0\_CPURST\_Pos 1

[ 27](numaker__m2l31x__reset_8h.md#a2d6ee5e16b9ca7a8f406a9f8ce3ea19f)#define SYS\_IPRST0\_PDMA0RST\_Pos 2

[ 28](numaker__m2l31x__reset_8h.md#aa5a4bb5b7219f375f8ba81f7bd6403b4)#define SYS\_IPRST0\_EBIRST\_Pos 3

[ 29](numaker__m2l31x__reset_8h.md#a65c2e6c5536b6f9aa4c6901d09d68feb)#define SYS\_IPRST0\_USBHRST\_Pos 4

[ 30](numaker__m2l31x__reset_8h.md#a39005d8a36aea761fba8af79d2b55903)#define SYS\_IPRST0\_CRCRST\_Pos 7

[ 31](numaker__m2l31x__reset_8h.md#a4b7f7a206299423497c9256c5e03d469)#define SYS\_IPRST0\_CRPTRST\_Pos 12

[ 32](numaker__m2l31x__reset_8h.md#ae996b5e06fcbd6f41cf6e91f74f55c28)#define SYS\_IPRST0\_CANFD0RST\_Pos 20

[ 33](numaker__m2l31x__reset_8h.md#a53d8f761aaf56bae6117804f6876a358)#define SYS\_IPRST0\_CANFD1RST\_Pos 21

[ 34](numaker__m2l31x__reset_8h.md#a78984ea2de0dda8a30d39a2f5b1fda2b)#define SYS\_IPRST1\_GPIORST\_Pos 1

[ 35](numaker__m2l31x__reset_8h.md#a4eb0d85763d53ede2f2371a83e9c287e)#define SYS\_IPRST1\_TMR0RST\_Pos 2

[ 36](numaker__m2l31x__reset_8h.md#a1c6e3e5b6577bd022f0876259cce11b3)#define SYS\_IPRST1\_TMR1RST\_Pos 3

[ 37](numaker__m2l31x__reset_8h.md#a662051a72d91ede245cb4ef85eba4bb6)#define SYS\_IPRST1\_TMR2RST\_Pos 4

[ 38](numaker__m2l31x__reset_8h.md#a3413b21d0a4d954b254a90a220ab4ee3)#define SYS\_IPRST1\_TMR3RST\_Pos 5

[ 39](numaker__m2l31x__reset_8h.md#a9a75d4ae6d1602abf709cdf5336699ed)#define SYS\_IPRST1\_ACMP01RST\_Pos 7

[ 40](numaker__m2l31x__reset_8h.md#a4e49484419bef1b195d39aac50295c26)#define SYS\_IPRST1\_I2C0RST\_Pos 8

[ 41](numaker__m2l31x__reset_8h.md#abd68af9b85c12921849b079f407040ea)#define SYS\_IPRST1\_I2C1RST\_Pos 9

[ 42](numaker__m2l31x__reset_8h.md#a4288e9b48e38973b33ca682e321b6c34)#define SYS\_IPRST1\_I2C2RST\_Pos 10

[ 43](numaker__m2l31x__reset_8h.md#aba5d45fd38b4759fe8acf17ed65491a9)#define SYS\_IPRST1\_I2C3RST\_Pos 11

[ 44](numaker__m2l31x__reset_8h.md#ab52ebe7dc3f797123712566fa6da5207)#define SYS\_IPRST1\_QSPI0RST\_Pos 12

[ 45](numaker__m2l31x__reset_8h.md#ae7d0c1eb46b33b0cf1ad0aa2e67e8b4b)#define SYS\_IPRST1\_SPI0RST\_Pos 13

[ 46](numaker__m2l31x__reset_8h.md#ab7df620486a91032459cd79b556f5557)#define SYS\_IPRST1\_SPI1RST\_Pos 14

[ 47](numaker__m2l31x__reset_8h.md#a612a4b7b02b5217eb8e5b5edb463f85c)#define SYS\_IPRST1\_SPI2RST\_Pos 15

[ 48](numaker__m2l31x__reset_8h.md#afb5e9e72603c7d73994963ef67a56985)#define SYS\_IPRST1\_UART0RST\_Pos 16

[ 49](numaker__m2l31x__reset_8h.md#a0f8d25e180b12c5d81dcabbd153b9d99)#define SYS\_IPRST1\_UART1RST\_Pos 17

[ 50](numaker__m2l31x__reset_8h.md#a6aff306da98ff91e93a5f2cd24c7c763)#define SYS\_IPRST1\_UART2RST\_Pos 18

[ 51](numaker__m2l31x__reset_8h.md#a07b3feb0a60d22700dc9fb14ece813cb)#define SYS\_IPRST1\_UART3RST\_Pos 19

[ 52](numaker__m2l31x__reset_8h.md#a2c90ca0565dcdee1b211aec2ddb2a6ec)#define SYS\_IPRST1\_UART4RST\_Pos 20

[ 53](numaker__m2l31x__reset_8h.md#ae9dd60c5a73beb4ede086385b2af99c3)#define SYS\_IPRST1\_UART5RST\_Pos 21

[ 54](numaker__m2l31x__reset_8h.md#ad9102e00dc678e99b6e4a8ce15ea6f1f)#define SYS\_IPRST1\_UART6RST\_Pos 22

[ 55](numaker__m2l31x__reset_8h.md#a9c680bfd3de5168041dcbfe46f2d82fb)#define SYS\_IPRST1\_UART7RST\_Pos 23

[ 56](numaker__m2l31x__reset_8h.md#a75b1c41c6620f5f6f38e964bc284f6e5)#define SYS\_IPRST1\_OTGRST\_Pos 26

[ 57](numaker__m2l31x__reset_8h.md#afa8d2c7e199b0ab495a46a82e021dd96)#define SYS\_IPRST1\_USBDRST\_Pos 27

[ 58](numaker__m2l31x__reset_8h.md#ac6b1279ab7d72e59e2dcadf86e4b1f3b)#define SYS\_IPRST1\_EADC0RST\_Pos 28

[ 59](numaker__m2l31x__reset_8h.md#a27d57e9ee4473ba6d4362091409a2520)#define SYS\_IPRST1\_TRNGRST\_Pos 31

[ 60](numaker__m2l31x__reset_8h.md#abc6986b3a217b070b4da04f61012441a)#define SYS\_IPRST2\_SPI3RST\_Pos 6

[ 61](numaker__m2l31x__reset_8h.md#ae697fec5c6ed9e38d8ca532703890a6c)#define SYS\_IPRST2\_USCI0RST\_Pos 8

[ 62](numaker__m2l31x__reset_8h.md#aaf76aa644a31aaf29fba26bd322a40f3)#define SYS\_IPRST2\_USCI1RST\_Pos 9

[ 63](numaker__m2l31x__reset_8h.md#a559e5212bf39afe97c55ed2e171407bd)#define SYS\_IPRST2\_WWDTRST\_Pos 11

[ 64](numaker__m2l31x__reset_8h.md#ab5f9056222f898414199bd6d22ae292b)#define SYS\_IPRST2\_DACRST\_Pos 12

[ 65](numaker__m2l31x__reset_8h.md#a4c886451c6007adca14648f8a6478517)#define SYS\_IPRST2\_EPWM0RST\_Pos 16

[ 66](numaker__m2l31x__reset_8h.md#aee0777b5a4fd886c9910cf8da1ff6b66)#define SYS\_IPRST2\_EPWM1RST\_Pos 17

[ 67](numaker__m2l31x__reset_8h.md#a5f5ec9bad6964b564ace5a8fab6f2225)#define SYS\_IPRST2\_EQEI0RST\_Pos 22

[ 68](numaker__m2l31x__reset_8h.md#a7ba7265af068f547e7d8268b3a7f4ad2)#define SYS\_IPRST2\_EQEI1RST\_Pos 23

[ 69](numaker__m2l31x__reset_8h.md#a858a182cf0e97431e636212a88077a90)#define SYS\_IPRST2\_TKRST\_Pos 25

[ 70](numaker__m2l31x__reset_8h.md#a67a789dd216dc674e2904543c9e95e13)#define SYS\_IPRST2\_ECAP0RST\_Pos 26

[ 71](numaker__m2l31x__reset_8h.md#a8b9d0585241f7359520f71011af6724d)#define SYS\_IPRST2\_ECAP1RST\_Pos 27

[ 72](numaker__m2l31x__reset_8h.md#a4c265b1b8bd8098c74aa9b6912e8b035)#define SYS\_IPRST3\_ACMP2RST\_Pos 7

[ 73](numaker__m2l31x__reset_8h.md#a66d46ae8552ae31e35b40c00cf42fafb)#define SYS\_IPRST3\_PWM0RST\_Pos 8

[ 74](numaker__m2l31x__reset_8h.md#a8a6164f558d3b9778b447b3e67bc9d94)#define SYS\_IPRST3\_PWM1RST\_Pos 9

[ 75](numaker__m2l31x__reset_8h.md#ad8bb45ee2c68ae689b451456258b57f8)#define SYS\_IPRST3\_UTCPD0RST\_Pos 15

76

77/\* End of M2L31 BSP sys\_reg.h reset module copy \*/

78

79/\* Beginning of M2L31 BSP sys.h reset module copy \*/

80

81/\*---------------------------------------------------------------------

82 \* Module Reset Control Resister constant definitions.

83 \*---------------------------------------------------------------------

84 \*/

85

[ 86](numaker__m2l31x__reset_8h.md#a2ec945f466041bba124cd635cc6667dc)#define NUMAKER\_PDMA0\_RST ((0UL<<24) | SYS\_IPRST0\_PDMA0RST\_Pos)

[ 87](numaker__m2l31x__reset_8h.md#a4de27d07239c747bdae9e173c6abfd17)#define NUMAKER\_EBI\_RST ((0UL<<24) | SYS\_IPRST0\_EBIRST\_Pos)

[ 88](numaker__m2l31x__reset_8h.md#a9da1d83f45ece48bd9be2d4345931784)#define NUMAKER\_USBH\_RST ((0UL<<24) | SYS\_IPRST0\_USBHRST\_Pos)

[ 89](numaker__m2l31x__reset_8h.md#a9e10d08e25bcce46419e595468ee2140)#define NUMAKER\_CRC\_RST ((0UL<<24) | SYS\_IPRST0\_CRCRST\_Pos)

[ 90](numaker__m2l31x__reset_8h.md#a53316015ee2c28580760707b597382f7)#define NUMAKER\_CRPT\_RST ((0UL<<24) | SYS\_IPRST0\_CRPTRST\_Pos)

[ 91](numaker__m2l31x__reset_8h.md#a37c923029e0439dd6b1c449fc81c40f4)#define NUMAKER\_CANFD0\_RST ((0UL<<24) | SYS\_IPRST0\_CANFD0RST\_Pos)

[ 92](numaker__m2l31x__reset_8h.md#aa3cde3062807637c383a6a11affbace6)#define NUMAKER\_CANFD1\_RST ((0UL<<24) | SYS\_IPRST0\_CANFD1RST\_Pos)

93

[ 94](numaker__m2l31x__reset_8h.md#a78b715193110ab7029d220d288132bb6)#define NUMAKER\_GPIO\_RST ((4UL<<24) | SYS\_IPRST1\_GPIORST\_Pos)

[ 95](numaker__m2l31x__reset_8h.md#af5659ce27a84e17aeeb50cd2edb423c7)#define NUMAKER\_TMR0\_RST ((4UL<<24) | SYS\_IPRST1\_TMR0RST\_Pos)

[ 96](numaker__m2l31x__reset_8h.md#a7a8501e84864c5810d9e03e2c261bcd4)#define NUMAKER\_TMR1\_RST ((4UL<<24) | SYS\_IPRST1\_TMR1RST\_Pos)

[ 97](numaker__m2l31x__reset_8h.md#a0e7f53329931eab01b15ba09d0b1b2a4)#define NUMAKER\_TMR2\_RST ((4UL<<24) | SYS\_IPRST1\_TMR2RST\_Pos)

[ 98](numaker__m2l31x__reset_8h.md#a8e77d7bfed00350408e6d1cfe010a366)#define NUMAKER\_TMR3\_RST ((4UL<<24) | SYS\_IPRST1\_TMR3RST\_Pos)

[ 99](numaker__m2l31x__reset_8h.md#a16163237a6cbb88ef60dd465b137b0c3)#define NUMAKER\_ACMP01\_RST ((4UL<<24) | SYS\_IPRST1\_ACMP01RST\_Pos)

[ 100](numaker__m2l31x__reset_8h.md#a59c61b565df006bfff587f3468c7c0c6)#define NUMAKER\_I2C0\_RST ((4UL<<24) | SYS\_IPRST1\_I2C0RST\_Pos)

[ 101](numaker__m2l31x__reset_8h.md#ad7061d30f5fffad6396f499c4e703f30)#define NUMAKER\_I2C1\_RST ((4UL<<24) | SYS\_IPRST1\_I2C1RST\_Pos)

[ 102](numaker__m2l31x__reset_8h.md#abee67c7820c016fa124e6a6d96451ac9)#define NUMAKER\_I2C2\_RST ((4UL<<24) | SYS\_IPRST1\_I2C2RST\_Pos)

[ 103](numaker__m2l31x__reset_8h.md#a6395be9706c311db84f3563382d52482)#define NUMAKER\_I2C3\_RST ((4UL<<24) | SYS\_IPRST1\_I2C3RST\_Pos)

[ 104](numaker__m2l31x__reset_8h.md#ad95c0f26b66c02b0d76ada07e4a8ae4f)#define NUMAKER\_QSPI0\_RST ((4UL<<24) | SYS\_IPRST1\_QSPI0RST\_Pos)

[ 105](numaker__m2l31x__reset_8h.md#ac26b4c587af3877bab01d38fa51fae2c)#define NUMAKER\_SPI0\_RST ((4UL<<24) | SYS\_IPRST1\_SPI0RST\_Pos)

[ 106](numaker__m2l31x__reset_8h.md#a6ed8951e79509205becde2782955edc3)#define NUMAKER\_SPI1\_RST ((4UL<<24) | SYS\_IPRST1\_SPI1RST\_Pos)

[ 107](numaker__m2l31x__reset_8h.md#aea94605fb578f4e80084db8c24700173)#define NUMAKER\_SPI2\_RST ((4UL<<24) | SYS\_IPRST1\_SPI2RST\_Pos)

[ 108](numaker__m2l31x__reset_8h.md#a0ca6e29af1512259983d74592d86c8ac)#define NUMAKER\_UART0\_RST ((4UL<<24) | SYS\_IPRST1\_UART0RST\_Pos)

[ 109](numaker__m2l31x__reset_8h.md#a855263435d644be9a655aafaa6997e57)#define NUMAKER\_UART1\_RST ((4UL<<24) | SYS\_IPRST1\_UART1RST\_Pos)

[ 110](numaker__m2l31x__reset_8h.md#acc518471fe73a842b39a56a6c2a3d208)#define NUMAKER\_UART2\_RST ((4UL<<24) | SYS\_IPRST1\_UART2RST\_Pos)

[ 111](numaker__m2l31x__reset_8h.md#a451f38258887da534ee5c75e6dfcc28a)#define NUMAKER\_UART3\_RST ((4UL<<24) | SYS\_IPRST1\_UART3RST\_Pos)

[ 112](numaker__m2l31x__reset_8h.md#a74a3f05297b2014947e13c9e8fd7fd14)#define NUMAKER\_UART4\_RST ((4UL<<24) | SYS\_IPRST1\_UART4RST\_Pos)

[ 113](numaker__m2l31x__reset_8h.md#a83b12f8d7cc1822080bb088730033c5d)#define NUMAKER\_UART5\_RST ((4UL<<24) | SYS\_IPRST1\_UART5RST\_Pos)

[ 114](numaker__m2l31x__reset_8h.md#a42e7f4a4a1f585df59b03928f1b95b11)#define NUMAKER\_UART6\_RST ((4UL<<24) | SYS\_IPRST1\_UART6RST\_Pos)

[ 115](numaker__m2l31x__reset_8h.md#aa4f97772ca5218ae52d2105e722db6fc)#define NUMAKER\_UART7\_RST ((4UL<<24) | SYS\_IPRST1\_UART7RST\_Pos)

[ 116](numaker__m2l31x__reset_8h.md#a93cde8c56f474777ba4fe7ff47fe8f14)#define NUMAKER\_OTG\_RST ((4UL<<24) | SYS\_IPRST1\_OTGRST\_Pos)

[ 117](numaker__m2l31x__reset_8h.md#a1a74ded775d85a498a044529857c5826)#define NUMAKER\_USBD\_RST ((4UL<<24) | SYS\_IPRST1\_USBDRST\_Pos)

[ 118](numaker__m2l31x__reset_8h.md#abfb255d99741ffe50d400a09b8a80787)#define NUMAKER\_EADC0\_RST ((4UL<<24) | SYS\_IPRST1\_EADC0RST\_Pos)

[ 119](numaker__m2l31x__reset_8h.md#a7d1dca0f73d12f8cad5d4fb3941e9a34)#define NUMAKER\_TRNG\_RST ((4UL<<24) | SYS\_IPRST1\_TRNGRST\_Pos)

120

[ 121](numaker__m2l31x__reset_8h.md#a62670f2e3ed7a343b0d8338cf18484ce)#define NUMAKER\_SPI3\_RST ((8UL<<24) | SYS\_IPRST2\_SPI3RST\_Pos)

[ 122](numaker__m2l31x__reset_8h.md#ab7e650d5582aa2f623f075c5b2c2dce5)#define NUMAKER\_USCI0\_RST ((8UL<<24) | SYS\_IPRST2\_USCI0RST\_Pos)

[ 123](numaker__m2l31x__reset_8h.md#accb0fc2206b4bbd242e5d7833ea49467)#define NUMAKER\_USCI1\_RST ((8UL<<24) | SYS\_IPRST2\_USCI1RST\_Pos)

[ 124](numaker__m2l31x__reset_8h.md#acda04457b8676248debe48f55f85a779)#define NUMAKER\_WWDT\_RST ((8UL<<24) | SYS\_IPRST2\_WWDTRST\_Pos)

[ 125](numaker__m2l31x__reset_8h.md#aa244c6cee2327a190b27856b83446913)#define NUMAKER\_DAC\_RST ((8UL<<24) | SYS\_IPRST2\_DACRST\_Pos)

[ 126](numaker__m2l31x__reset_8h.md#ac7fcfa9b1c8e15744d413acb643202f7)#define NUMAKER\_EPWM0\_RST ((8UL<<24) | SYS\_IPRST2\_EPWM0RST\_Pos)

[ 127](numaker__m2l31x__reset_8h.md#a529ccc59cc243788d18e63f519cfe5c7)#define NUMAKER\_EPWM1\_RST ((8UL<<24) | SYS\_IPRST2\_EPWM1RST\_Pos)

[ 128](numaker__m2l31x__reset_8h.md#aaa793688d87486488dca737c346bfc8d)#define NUMAKER\_EQEI0\_RST ((8UL<<24) | SYS\_IPRST2\_EQEI0RST\_Pos)

[ 129](numaker__m2l31x__reset_8h.md#af1b3595e1191835a0a3a35b6a1949c2a)#define NUMAKER\_EQEI1\_RST ((8UL<<24) | SYS\_IPRST2\_EQEI1RST\_Pos)

[ 130](numaker__m2l31x__reset_8h.md#adac654ab381da0c420f76fc98d7d7622)#define NUMAKER\_TK\_RST ((8UL<<24) | SYS\_IPRST2\_TKRST\_Pos)

[ 131](numaker__m2l31x__reset_8h.md#a423d4739b6f1c7092608a2fb1eef4909)#define NUMAKER\_ECAP0\_RST ((8UL<<24) | SYS\_IPRST2\_ECAP0RST\_Pos)

[ 132](numaker__m2l31x__reset_8h.md#ae8be7edf8c201921491a45aef91cc565)#define NUMAKER\_ECAP1\_RST ((8UL<<24) | SYS\_IPRST2\_ECAP1RST\_Pos)

133

[ 134](numaker__m2l31x__reset_8h.md#a2e74dd018ac027dd9f81db6071d988ab)#define NUMAKER\_ACMP2\_RST ((0x18UL<<24) | SYS\_IPRST3\_ACMP2RST\_Pos)

[ 135](numaker__m2l31x__reset_8h.md#a89e7fcc6dbdd3ed3b2414772f0fd531b)#define NUMAKER\_PWM0\_RST ((0x18UL<<24) | SYS\_IPRST3\_PWM0RST\_Pos)

[ 136](numaker__m2l31x__reset_8h.md#a979671c43207355db378bee5b85c77e2)#define NUMAKER\_PWM1\_RST ((0x18UL<<24) | SYS\_IPRST3\_PWM1RST\_Pos)

[ 137](numaker__m2l31x__reset_8h.md#ad901b707ae7eee4573d357b7130f6c8f)#define NUMAKER\_UTCPD0\_RST ((0x18UL<<24) | SYS\_IPRST3\_UTCPD0RST\_Pos)

138

[ 139](numaker__m2l31x__reset_8h.md#ad14f336e7a771560c8236b3093b26943)#define NUMAKER\_LPPDMA0\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_LPPDMA0RST\_Pos)

[ 140](numaker__m2l31x__reset_8h.md#a417db23cca897cf9c9ccc0442a4f131b)#define NUMAKER\_LPGPIO\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_LPGPIORST\_Pos)

[ 141](numaker__m2l31x__reset_8h.md#af7d557fac7d287c5d72a16cae98acc24)#define NUMAKER\_LPSRAM\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_LPSRAMRST\_Pos)

[ 142](numaker__m2l31x__reset_8h.md#a596c83d52a8dc87f2fb930fdd2f54a70)#define NUMAKER\_WDT\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_WDTRST\_Pos)

[ 143](numaker__m2l31x__reset_8h.md#a8ef6dbb24ea8102847da7208fb6e109d)#define NUMAKER\_LPSPI0\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_LPSPI0RST\_Pos)

[ 144](numaker__m2l31x__reset_8h.md#ad6a7b4aaa911b2ed25b9fac2bd08e00f)#define NUMAKER\_LPI2C0\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_LPI2C0RST\_Pos)

[ 145](numaker__m2l31x__reset_8h.md#a115c986c4084eaac47cad34c5307c4e2)#define NUMAKER\_LPUART0\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_LPUART0RST\_Pos)

[ 146](numaker__m2l31x__reset_8h.md#ae8cbc8c1559c67550b5b1f185573ae60)#define NUMAKER\_LPTMR0\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_LPTMR0RST\_Pos)

[ 147](numaker__m2l31x__reset_8h.md#aa24cd14e74ed137af2a64435a3641ade)#define NUMAKER\_LPTMR1\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_LPTMR1RST\_Pos)

[ 148](numaker__m2l31x__reset_8h.md#ad043a8aeb4a7ec44d0c8f4b1dd7caed4)#define NUMAKER\_TTMR0\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_TTMR0RST\_Pos)

[ 149](numaker__m2l31x__reset_8h.md#aad7843372e815b198a4797fba93860b7)#define NUMAKER\_TTMR1\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_TTMR1RST\_Pos)

[ 150](numaker__m2l31x__reset_8h.md#a790be15f15374a85b67532a09fa3c198)#define NUMAKER\_LPADC0\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_LPADC0RST\_Pos)

[ 151](numaker__m2l31x__reset_8h.md#a3dfc4dc31333088bfa81e87bf5e6b248)#define NUMAKER\_OPA\_RST ((0x80UL<<24) | LPSCC\_IPRST0\_OPARST\_Pos)

152

153/\* End of M2L31 BSP sys.h reset module copy \*/

154

155#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [numaker\_m2l31x\_reset.h](numaker__m2l31x__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
