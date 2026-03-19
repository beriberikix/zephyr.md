---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/usb__cdc_8h_source.html
original_path: doxygen/html/usb__cdc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_cdc.h

[Go to the documentation of this file.](usb__cdc_8h.md)

1/\* usb\_cdc.h - USB CDC-ACM and CDC-ECM public header \*/

2

3/\*

4 \* Copyright (c) 2017 PHYTEC Messtechnik GmbH

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9

20

21#ifndef ZEPHYR\_INCLUDE\_USB\_CLASS\_USB\_CDC\_H\_

22#define ZEPHYR\_INCLUDE\_USB\_CLASS\_USB\_CDC\_H\_

23

[ 25](usb__cdc_8h.md#a2d44425b0b0c5e525885c5764348ec54)#define CDC\_SRN\_1\_20 0x0120

26

[ 28](usb__cdc_8h.md#a01b7a28004a035df52334b64308e4b22)#define ACM\_SUBCLASS 0x02

[ 29](usb__cdc_8h.md#a39f776a70d5139575ed84be1a9faee5d)#define ECM\_SUBCLASS 0x06

[ 30](usb__cdc_8h.md#a73503e51ff8700620866be15a8d7ab43)#define EEM\_SUBCLASS 0x0c

[ 31](usb__cdc_8h.md#af4edeebbc1d4fb6f3a727083a36e731e)#define NCM\_SUBCLASS 0x0d

32

[ 34](usb__cdc_8h.md#aaf98d38c2b9c859cf86e281bb67f27b0)#define AT\_CMD\_V250\_PROTOCOL 0x01

[ 35](usb__cdc_8h.md#ab4f22c3c42b5a4efe7735bafebc1cb9b)#define EEM\_PROTOCOL 0x07

[ 36](usb__cdc_8h.md#a20396bb325a1e947b2e4b0017a134082)#define ACM\_VENDOR\_PROTOCOL 0xFF

[ 37](usb__cdc_8h.md#a6577856e991bddc829d93af0ea527ef6)#define NCM\_DATA\_PROTOCOL 0x01

38

[ 43](usb__cdc_8h.md#ae4044b943c9e54cb7a64c8c35acaf8bc)#define DATA\_INTERFACE\_CLASS 0x0A

44

[ 50](usb__cdc_8h.md#a008b7d343c5a1876a78c885f7a496b66)#define HEADER\_FUNC\_DESC 0x00

[ 51](usb__cdc_8h.md#a60552aa9506dc2c6dede5146c5251aaf)#define CALL\_MANAGEMENT\_FUNC\_DESC 0x01

[ 52](usb__cdc_8h.md#a057b9de28602442b66a8c3a7befd62a7)#define ACM\_FUNC\_DESC 0x02

[ 53](usb__cdc_8h.md#aab7f21ab95fc5916f758e66087caef25)#define UNION\_FUNC\_DESC 0x06

[ 54](usb__cdc_8h.md#a22b2b55d7ab3cdd4206df07cddcc44e9)#define ETHERNET\_FUNC\_DESC 0x0F

[ 55](usb__cdc_8h.md#ad788a76ba44ab5d02c699b110856e18e)#define ETHERNET\_FUNC\_DESC\_NCM 0x1a

56

[ 62](usb__cdc_8h.md#a926f6444745d1cdc991d97e4f1d265ad)#define CDC\_SEND\_ENC\_CMD 0x00

[ 63](usb__cdc_8h.md#ac9008f0dc0d4fc7141de9dd12352caa8)#define CDC\_GET\_ENC\_RSP 0x01

[ 64](usb__cdc_8h.md#a91a9c047339a1a5918b6a923af6d1af6)#define SET\_LINE\_CODING 0x20

[ 65](usb__cdc_8h.md#a6698d8d2ca56fafdc943aec2cede1daf)#define GET\_LINE\_CODING 0x21

[ 66](usb__cdc_8h.md#a437869c339749d5d011060cd5676659e)#define SET\_CONTROL\_LINE\_STATE 0x22

67

[ 72](usb__cdc_8h.md#a7e9384e6a613e38c543d7eba05f64c07)#define USB\_CDC\_NETWORK\_CONNECTION 0x00

[ 73](usb__cdc_8h.md#a970045b850b0195b5a4a2913d5a0b918)#define USB\_CDC\_RESPONSE\_AVAILABLE 0x01

[ 74](usb__cdc_8h.md#afdeb5f862a52b953653b9ab567979cec)#define USB\_CDC\_AUX\_JACK\_HOOK\_STATE 0x08

[ 75](usb__cdc_8h.md#a52452ce9272b97203fece115b5005aff)#define USB\_CDC\_RING\_DETECT 0x09

[ 76](usb__cdc_8h.md#ac167f480370c73b830281d98ad5899b1)#define USB\_CDC\_SERIAL\_STATE 0x20

[ 77](usb__cdc_8h.md#a6bb6650664f82fd25330af0357e5831e)#define USB\_CDC\_CALL\_STATE\_CHANGE 0x28

[ 78](usb__cdc_8h.md#ac63891d7c3321f7f4eb297f87c0978f6)#define USB\_CDC\_LINE\_STATE\_CHANGE 0x23

79

[ 84](usb__cdc_8h.md#a504f682d66f714730f35d282ce0b9177)#define USB\_CDC\_SERIAL\_STATE\_OVERRUN BIT(6)

[ 85](usb__cdc_8h.md#a1ff82c5d551211d2298128bd84eeb60a)#define USB\_CDC\_SERIAL\_STATE\_PARITY BIT(5)

[ 86](usb__cdc_8h.md#a59f5f1ebab838621cdc67668541432ca)#define USB\_CDC\_SERIAL\_STATE\_FRAMING BIT(4)

[ 87](usb__cdc_8h.md#a60f22cb2ae47789875e2542063899876)#define USB\_CDC\_SERIAL\_STATE\_RINGSIGNAL BIT(3)

[ 88](usb__cdc_8h.md#a15f3c90969106ecdf3b1cdf258cad5df)#define USB\_CDC\_SERIAL\_STATE\_BREAK BIT(2)

[ 89](usb__cdc_8h.md#ab96b4f63f2de0ef913862878bce1029f)#define USB\_CDC\_SERIAL\_STATE\_TXCARRIER BIT(1)

[ 90](usb__cdc_8h.md#ad720be9e3738bcba7e37dc9392c3b6e8)#define USB\_CDC\_SERIAL\_STATE\_RXCARRIER BIT(0)

91

[ 93](usb__cdc_8h.md#a00788c95fb39c2636d7d5a427282399f)#define SET\_CONTROL\_LINE\_STATE\_RTS 0x02

[ 94](usb__cdc_8h.md#a07623c40153f936c863627a3dc30da7a)#define SET\_CONTROL\_LINE\_STATE\_DTR 0x01

95

[ 97](usb__cdc_8h.md#a89554d686630d67d642e228b7ee0dc2c)#define USB\_CDC\_LINE\_CTRL\_BAUD\_RATE UART\_LINE\_CTRL\_BAUD\_RATE

[ 98](usb__cdc_8h.md#a7e6b9bb33debc489b7ac7e0fb0e94947)#define USB\_CDC\_LINE\_CTRL\_DCD UART\_LINE\_CTRL\_DCD

[ 99](usb__cdc_8h.md#a6876caf1b77477e259bb391216309799)#define USB\_CDC\_LINE\_CTRL\_DSR UART\_LINE\_CTRL\_DSR

[ 100](usb__cdc_8h.md#a716d9aaf772e1fa3f8b555077048ecbb)#define USB\_CDC\_LINE\_CTRL\_BREAK BIT(5)

[ 101](usb__cdc_8h.md#a8ec9b8c619c567cc174c0473dda5a5fd)#define USB\_CDC\_LINE\_CTRL\_RING\_SIGNAL BIT(6)

[ 102](usb__cdc_8h.md#a263186a0a64d9a8e7e9e97a54b951bdf)#define USB\_CDC\_LINE\_CTRL\_FRAMING BIT(7)

[ 103](usb__cdc_8h.md#ae2779672a5b5ab49a2ed7240e463f9e8)#define USB\_CDC\_LINE\_CTRL\_PARITY BIT(8)

[ 104](usb__cdc_8h.md#a8bf1722f98bf48394605efddf6be1295)#define USB\_CDC\_LINE\_CTRL\_OVER\_RUN BIT(9)

105

[ 107](usb__cdc_8h.md#ae38825267009563e0aa82a58a7fc4fd2)#define SERIAL\_STATE\_OVER\_RUN 0x40

[ 108](usb__cdc_8h.md#a738f180df5795376763ff233fb8aa68d)#define SERIAL\_STATE\_PARITY 0x20

[ 109](usb__cdc_8h.md#aacd68fe3a081441ee684bf2ef6312bec)#define SERIAL\_STATE\_FRAMING 0x10

[ 110](usb__cdc_8h.md#a935c772da45984e8d796396146413037)#define SERIAL\_STATE\_RING\_SIGNAL 0x08

[ 111](usb__cdc_8h.md#aa66ab791abfcf7ef5a37758c1b33138a)#define SERIAL\_STATE\_BREAK 0x04

[ 112](usb__cdc_8h.md#a22cd80b90c53ff44a4c1de08310ba3c2)#define SERIAL\_STATE\_TX\_CARRIER 0x02

[ 113](usb__cdc_8h.md#a9677c612766f3e788ad2960a17ad0791)#define SERIAL\_STATE\_RX\_CARRIER 0x01

114

[ 120](usb__cdc_8h.md#a8a06b3413e1c665f13ba4895c220d608)#define USB\_CDC\_LINE\_CODING\_STOP\_BITS\_1 0

[ 121](usb__cdc_8h.md#a4159f50590d647510a6a1f38875e012e)#define USB\_CDC\_LINE\_CODING\_STOP\_BITS\_1\_5 1

[ 122](usb__cdc_8h.md#a7e7fc73b4490a694aa982b4862782157)#define USB\_CDC\_LINE\_CODING\_STOP\_BITS\_2 2

123

[ 124](usb__cdc_8h.md#a549181d2cc92c42b4db8c3c34927d97f)#define USB\_CDC\_LINE\_CODING\_PARITY\_NO 0

[ 125](usb__cdc_8h.md#a44d808ad4f27ecf3502b9c14da2aa9b9)#define USB\_CDC\_LINE\_CODING\_PARITY\_ODD 1

[ 126](usb__cdc_8h.md#a327b5f99ab7e5cfc99d7592d1f9c1c25)#define USB\_CDC\_LINE\_CODING\_PARITY\_EVEN 2

[ 127](usb__cdc_8h.md#a490d381698ce91db4ab8bb24dd70820a)#define USB\_CDC\_LINE\_CODING\_PARITY\_MARK 3

[ 128](usb__cdc_8h.md#a5aa1b5cf30cb4020442131f66170fec6)#define USB\_CDC\_LINE\_CODING\_PARITY\_SPACE 4

129

[ 130](usb__cdc_8h.md#a327c495a9930b3e5519f0a9c7cd9ed18)#define USB\_CDC\_LINE\_CODING\_DATA\_BITS\_5 5

[ 131](usb__cdc_8h.md#a231932add6d9ceef4f5332a0db1b9f55)#define USB\_CDC\_LINE\_CODING\_DATA\_BITS\_6 6

[ 132](usb__cdc_8h.md#a6a276593bc4587671df5e6da8cce5ebb)#define USB\_CDC\_LINE\_CODING\_DATA\_BITS\_7 7

[ 133](usb__cdc_8h.md#a64e296aec72bbd8f9bdc1aefa5aab654)#define USB\_CDC\_LINE\_CODING\_DATA\_BITS\_8 8

134

[ 139](usb__cdc_8h.md#a4dce35ee8cf2337bab3c90081200a9f6)#define SET\_ETHERNET\_MULTICAST\_FILTERS 0x40

[ 140](usb__cdc_8h.md#a1506deda422ee354040b0feeb09ad4b6)#define SET\_ETHERNET\_PM\_FILTER 0x41

[ 141](usb__cdc_8h.md#a53ea6ae0e1fe8a88350740fd594507fd)#define GET\_ETHERNET\_PM\_FILTER 0x42

[ 142](usb__cdc_8h.md#adae019242224bbbc9d0f853da3733f1c)#define SET\_ETHERNET\_PACKET\_FILTER 0x43

[ 143](usb__cdc_8h.md#a7dffeba1576d6660fb930eabc5c515b7)#define GET\_ETHERNET\_STATISTIC 0x44

144

[ 149](usb__cdc_8h.md#a44e5dd539b8b41ccc9c61dd95ee4fb2e)#define GET\_NTB\_PARAMETERS 0x80

[ 150](usb__cdc_8h.md#a58701f26151379cd5dd8b7a7350dcda5)#define GET\_NET\_ADDRESS 0x81

[ 151](usb__cdc_8h.md#a2d8525d02e54ec44143a7732a15ad5b0)#define SET\_NET\_ADDRESS 0x82

[ 152](usb__cdc_8h.md#a2ba9ad377b20364fc811ec6d5bb74995)#define GET\_NTB\_FORMAT 0x83

[ 153](usb__cdc_8h.md#a9c48d4f5685678b1429ba90f7c0a7d9b)#define SET\_NTB\_FORMAT 0x84

[ 154](usb__cdc_8h.md#ae5ab2b5f3c10b1fc42d5873f8e8082c0)#define GET\_NTB\_INPUT\_SIZE 0x85

[ 155](usb__cdc_8h.md#a485fd89a465fb5ad82c09a686ba3bc1b)#define SET\_NTB\_INPUT\_SIZE 0x86

[ 156](usb__cdc_8h.md#aca024f2e7bb9f99d3376753589fa7c3f)#define GET\_MAX\_DATAGRAM\_SIZE 0x87

[ 157](usb__cdc_8h.md#a4d224c04ec87088b4494f43c59c59b86)#define SET\_MAX\_DATAGRAM\_SIZE 0x88

[ 158](usb__cdc_8h.md#a9dd7dad1bd3421f42a67f280826d464b)#define GET\_CRC\_MODE 0x89

[ 159](usb__cdc_8h.md#a634a3403221f33ae8506481b38840c2c)#define SET\_CRC\_MODE 0x8A

160

[ 162](usb__cdc_8h.md#a4abfd25c9ca3e70c5b33b89ee9456087)#define PACKET\_TYPE\_MULTICAST 0x10

[ 163](usb__cdc_8h.md#a3143cff5f7275d394f259c3b83e54e4b)#define PACKET\_TYPE\_BROADCAST 0x08

[ 164](usb__cdc_8h.md#a5a2d0aa22741a4a48b976cddc6f57f98)#define PACKET\_TYPE\_DIRECTED 0x04

[ 165](usb__cdc_8h.md#aac32de24c40e08d0d32d3db264fa964a)#define PACKET\_TYPE\_ALL\_MULTICAST 0x02

[ 166](usb__cdc_8h.md#a7be4d4e65526efb94ea1ef71da62f835)#define PACKET\_TYPE\_PROMISCUOUS 0x01

167

[ 169](structcdc__header__descriptor.md)struct [cdc\_header\_descriptor](structcdc__header__descriptor.md) {

[ 170](structcdc__header__descriptor.md#ac4ad6939d5a075ff2fe6d7505cba630b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionLength](structcdc__header__descriptor.md#ac4ad6939d5a075ff2fe6d7505cba630b);

[ 171](structcdc__header__descriptor.md#a3b8cc0d8b9d56db158f3b027b2cd6f6a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structcdc__header__descriptor.md#a3b8cc0d8b9d56db158f3b027b2cd6f6a);

[ 172](structcdc__header__descriptor.md#a49bf7e700891057f30cd3be77dec0752) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorSubtype](structcdc__header__descriptor.md#a49bf7e700891057f30cd3be77dec0752);

[ 173](structcdc__header__descriptor.md#ab66b3b87594a4510f11ba9ee950f230c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bcdCDC](structcdc__header__descriptor.md#ab66b3b87594a4510f11ba9ee950f230c);

174} \_\_packed;

175

[ 177](structcdc__union__descriptor.md)struct [cdc\_union\_descriptor](structcdc__union__descriptor.md) {

[ 178](structcdc__union__descriptor.md#a83ee5a04668006397663142232471606) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionLength](structcdc__union__descriptor.md#a83ee5a04668006397663142232471606);

[ 179](structcdc__union__descriptor.md#a839a6a4a7c4b2618c49649d93b7c6ff9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structcdc__union__descriptor.md#a839a6a4a7c4b2618c49649d93b7c6ff9);

[ 180](structcdc__union__descriptor.md#a965212d833550c13376b231d5e2ce125) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorSubtype](structcdc__union__descriptor.md#a965212d833550c13376b231d5e2ce125);

[ 181](structcdc__union__descriptor.md#a81bdab223598b27b620de0d9dba7bc80) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bControlInterface](structcdc__union__descriptor.md#a81bdab223598b27b620de0d9dba7bc80);

[ 182](structcdc__union__descriptor.md#a5bab5215179ecc0bb0bb6e7b9089abf6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bSubordinateInterface0](structcdc__union__descriptor.md#a5bab5215179ecc0bb0bb6e7b9089abf6);

183} \_\_packed;

184

[ 186](structcdc__cm__descriptor.md)struct [cdc\_cm\_descriptor](structcdc__cm__descriptor.md) {

[ 187](structcdc__cm__descriptor.md#a578a2a39c7c80de58cb7d952f8decd22) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionLength](structcdc__cm__descriptor.md#a578a2a39c7c80de58cb7d952f8decd22);

[ 188](structcdc__cm__descriptor.md#ad40616645c5b28754300594b43805a1f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structcdc__cm__descriptor.md#ad40616645c5b28754300594b43805a1f);

[ 189](structcdc__cm__descriptor.md#a908003360bca9ab79f55d80a2fc7aa24) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorSubtype](structcdc__cm__descriptor.md#a908003360bca9ab79f55d80a2fc7aa24);

[ 190](structcdc__cm__descriptor.md#aabbca6f88b936659124aa28264054b6d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bmCapabilities](structcdc__cm__descriptor.md#aabbca6f88b936659124aa28264054b6d);

[ 191](structcdc__cm__descriptor.md#a0a29f8dfe1dd9758f210b63d7a87bdc6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDataInterface](structcdc__cm__descriptor.md#a0a29f8dfe1dd9758f210b63d7a87bdc6);

192} \_\_packed;

193

[ 195](structcdc__acm__descriptor.md)struct [cdc\_acm\_descriptor](structcdc__acm__descriptor.md) {

[ 196](structcdc__acm__descriptor.md#a665260ce8cc55e35c941078987f92366) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionLength](structcdc__acm__descriptor.md#a665260ce8cc55e35c941078987f92366);

[ 197](structcdc__acm__descriptor.md#ab62800772430a82673004fcaac13c071) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structcdc__acm__descriptor.md#ab62800772430a82673004fcaac13c071);

[ 198](structcdc__acm__descriptor.md#ae1011a0e1520193be5c1fb0fe442915e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorSubtype](structcdc__acm__descriptor.md#ae1011a0e1520193be5c1fb0fe442915e);

[ 199](structcdc__acm__descriptor.md#a3066a08cbc5f0747d435a13ee4f22d14) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bmCapabilities](structcdc__acm__descriptor.md#a3066a08cbc5f0747d435a13ee4f22d14);

200} \_\_packed;

201

[ 203](structcdc__acm__line__coding.md)struct [cdc\_acm\_line\_coding](structcdc__acm__line__coding.md) {

[ 204](structcdc__acm__line__coding.md#a14d35b67e6f00b0d6196ba0e9ef6dfab) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dwDTERate](structcdc__acm__line__coding.md#a14d35b67e6f00b0d6196ba0e9ef6dfab);

[ 205](structcdc__acm__line__coding.md#afd2fd70a7da783d7aac0d99f9f267383) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bCharFormat](structcdc__acm__line__coding.md#afd2fd70a7da783d7aac0d99f9f267383);

[ 206](structcdc__acm__line__coding.md#a472270d84e160348e024f756b834cbb8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bParityType](structcdc__acm__line__coding.md#a472270d84e160348e024f756b834cbb8);

[ 207](structcdc__acm__line__coding.md#ab685d018d83e3e2d38c87c27902cca3e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDataBits](structcdc__acm__line__coding.md#ab685d018d83e3e2d38c87c27902cca3e);

208} \_\_packed;

209

[ 211](structcdc__acm__notification.md)struct [cdc\_acm\_notification](structcdc__acm__notification.md) {

[ 212](structcdc__acm__notification.md#a57b007a8ec893d660e6ec8a1b25f7dd3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bmRequestType](structcdc__acm__notification.md#a57b007a8ec893d660e6ec8a1b25f7dd3);

[ 213](structcdc__acm__notification.md#af24dae76a280c008e40a0d031171235c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bNotificationType](structcdc__acm__notification.md#af24dae76a280c008e40a0d031171235c);

[ 214](structcdc__acm__notification.md#a3bf290bc6e851331e93bedf49ae5dbe0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wValue](structcdc__acm__notification.md#a3bf290bc6e851331e93bedf49ae5dbe0);

[ 215](structcdc__acm__notification.md#a290717590343376c8f1f9a865cb4b0ae) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wIndex](structcdc__acm__notification.md#a290717590343376c8f1f9a865cb4b0ae);

[ 216](structcdc__acm__notification.md#af2f8fbceeaa9a3ad0ae1330b8f82bff2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wLength](structcdc__acm__notification.md#af2f8fbceeaa9a3ad0ae1330b8f82bff2);

[ 217](structcdc__acm__notification.md#a5666402ce9fbe5fad5f80592aa6f53ec) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data](structcdc__acm__notification.md#a5666402ce9fbe5fad5f80592aa6f53ec);

218} \_\_packed;

219

[ 221](structcdc__ecm__descriptor.md)struct [cdc\_ecm\_descriptor](structcdc__ecm__descriptor.md) {

[ 222](structcdc__ecm__descriptor.md#aa5cfb3a02e9818cf3faaff1dbb9dd487) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionLength](structcdc__ecm__descriptor.md#aa5cfb3a02e9818cf3faaff1dbb9dd487);

[ 223](structcdc__ecm__descriptor.md#ae000bdad185ca5af3674274ea3fa45d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structcdc__ecm__descriptor.md#ae000bdad185ca5af3674274ea3fa45d6);

[ 224](structcdc__ecm__descriptor.md#aaf95074ec751f227a33317325567c890) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorSubtype](structcdc__ecm__descriptor.md#aaf95074ec751f227a33317325567c890);

[ 225](structcdc__ecm__descriptor.md#ad43f97e428ef743d4655a1e91b91478d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iMACAddress](structcdc__ecm__descriptor.md#ad43f97e428ef743d4655a1e91b91478d);

[ 226](structcdc__ecm__descriptor.md#a3a7b901bef04212b217a69d055e37e66) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bmEthernetStatistics](structcdc__ecm__descriptor.md#a3a7b901bef04212b217a69d055e37e66);

[ 227](structcdc__ecm__descriptor.md#afdf7f4478515917b1ed653118e7a8540) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wMaxSegmentSize](structcdc__ecm__descriptor.md#afdf7f4478515917b1ed653118e7a8540);

[ 228](structcdc__ecm__descriptor.md#a196fcac7b1c9bf0f2b42a6d4ccb48de6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wNumberMCFilters](structcdc__ecm__descriptor.md#a196fcac7b1c9bf0f2b42a6d4ccb48de6);

[ 229](structcdc__ecm__descriptor.md#aed687a9629eb3c793af9260db407a136) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bNumberPowerFilters](structcdc__ecm__descriptor.md#aed687a9629eb3c793af9260db407a136);

230} \_\_packed;

231

[ 233](structcdc__ncm__descriptor.md)struct [cdc\_ncm\_descriptor](structcdc__ncm__descriptor.md) {

[ 234](structcdc__ncm__descriptor.md#a932a73d95abf90a0ba7f0de3e1760375) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionLength](structcdc__ncm__descriptor.md#a932a73d95abf90a0ba7f0de3e1760375);

[ 235](structcdc__ncm__descriptor.md#a9dea58db91413ebcff65151e006a3b2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structcdc__ncm__descriptor.md#a9dea58db91413ebcff65151e006a3b2c);

[ 236](structcdc__ncm__descriptor.md#a9fb11a778a65e5e8538619467cd6c6d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorSubtype](structcdc__ncm__descriptor.md#a9fb11a778a65e5e8538619467cd6c6d6);

[ 237](structcdc__ncm__descriptor.md#aa9b5bd71a73783e4a3c85a1d39f9def3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bcdNcmVersion](structcdc__ncm__descriptor.md#aa9b5bd71a73783e4a3c85a1d39f9def3);

[ 238](structcdc__ncm__descriptor.md#a8a88e3d7d2b36876a38fa8025118f069) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bmNetworkCapabilities](structcdc__ncm__descriptor.md#a8a88e3d7d2b36876a38fa8025118f069);

239} \_\_packed;

240

241#endif /\* ZEPHYR\_INCLUDE\_USB\_CLASS\_USB\_CDC\_H\_ \*/

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[cdc\_acm\_descriptor](structcdc__acm__descriptor.md)

Abstract Control Management Functional Descriptor.

**Definition** usb\_cdc.h:195

[cdc\_acm\_descriptor::bmCapabilities](structcdc__acm__descriptor.md#a3066a08cbc5f0747d435a13ee4f22d14)

uint8\_t bmCapabilities

**Definition** usb\_cdc.h:199

[cdc\_acm\_descriptor::bFunctionLength](structcdc__acm__descriptor.md#a665260ce8cc55e35c941078987f92366)

uint8\_t bFunctionLength

**Definition** usb\_cdc.h:196

[cdc\_acm\_descriptor::bDescriptorType](structcdc__acm__descriptor.md#ab62800772430a82673004fcaac13c071)

uint8\_t bDescriptorType

**Definition** usb\_cdc.h:197

[cdc\_acm\_descriptor::bDescriptorSubtype](structcdc__acm__descriptor.md#ae1011a0e1520193be5c1fb0fe442915e)

uint8\_t bDescriptorSubtype

**Definition** usb\_cdc.h:198

[cdc\_acm\_line\_coding](structcdc__acm__line__coding.md)

Data structure for GET\_LINE\_CODING / SET\_LINE\_CODING class requests.

**Definition** usb\_cdc.h:203

[cdc\_acm\_line\_coding::dwDTERate](structcdc__acm__line__coding.md#a14d35b67e6f00b0d6196ba0e9ef6dfab)

uint32\_t dwDTERate

**Definition** usb\_cdc.h:204

[cdc\_acm\_line\_coding::bParityType](structcdc__acm__line__coding.md#a472270d84e160348e024f756b834cbb8)

uint8\_t bParityType

**Definition** usb\_cdc.h:206

[cdc\_acm\_line\_coding::bDataBits](structcdc__acm__line__coding.md#ab685d018d83e3e2d38c87c27902cca3e)

uint8\_t bDataBits

**Definition** usb\_cdc.h:207

[cdc\_acm\_line\_coding::bCharFormat](structcdc__acm__line__coding.md#afd2fd70a7da783d7aac0d99f9f267383)

uint8\_t bCharFormat

**Definition** usb\_cdc.h:205

[cdc\_acm\_notification](structcdc__acm__notification.md)

Data structure for the notification about SerialState.

**Definition** usb\_cdc.h:211

[cdc\_acm\_notification::wIndex](structcdc__acm__notification.md#a290717590343376c8f1f9a865cb4b0ae)

uint16\_t wIndex

**Definition** usb\_cdc.h:215

[cdc\_acm\_notification::wValue](structcdc__acm__notification.md#a3bf290bc6e851331e93bedf49ae5dbe0)

uint16\_t wValue

**Definition** usb\_cdc.h:214

[cdc\_acm\_notification::data](structcdc__acm__notification.md#a5666402ce9fbe5fad5f80592aa6f53ec)

uint16\_t data

**Definition** usb\_cdc.h:217

[cdc\_acm\_notification::bmRequestType](structcdc__acm__notification.md#a57b007a8ec893d660e6ec8a1b25f7dd3)

uint8\_t bmRequestType

**Definition** usb\_cdc.h:212

[cdc\_acm\_notification::bNotificationType](structcdc__acm__notification.md#af24dae76a280c008e40a0d031171235c)

uint8\_t bNotificationType

**Definition** usb\_cdc.h:213

[cdc\_acm\_notification::wLength](structcdc__acm__notification.md#af2f8fbceeaa9a3ad0ae1330b8f82bff2)

uint16\_t wLength

**Definition** usb\_cdc.h:216

[cdc\_cm\_descriptor](structcdc__cm__descriptor.md)

Call Management Functional Descriptor.

**Definition** usb\_cdc.h:186

[cdc\_cm\_descriptor::bDataInterface](structcdc__cm__descriptor.md#a0a29f8dfe1dd9758f210b63d7a87bdc6)

uint8\_t bDataInterface

**Definition** usb\_cdc.h:191

[cdc\_cm\_descriptor::bFunctionLength](structcdc__cm__descriptor.md#a578a2a39c7c80de58cb7d952f8decd22)

uint8\_t bFunctionLength

**Definition** usb\_cdc.h:187

[cdc\_cm\_descriptor::bDescriptorSubtype](structcdc__cm__descriptor.md#a908003360bca9ab79f55d80a2fc7aa24)

uint8\_t bDescriptorSubtype

**Definition** usb\_cdc.h:189

[cdc\_cm\_descriptor::bmCapabilities](structcdc__cm__descriptor.md#aabbca6f88b936659124aa28264054b6d)

uint8\_t bmCapabilities

**Definition** usb\_cdc.h:190

[cdc\_cm\_descriptor::bDescriptorType](structcdc__cm__descriptor.md#ad40616645c5b28754300594b43805a1f)

uint8\_t bDescriptorType

**Definition** usb\_cdc.h:188

[cdc\_ecm\_descriptor](structcdc__ecm__descriptor.md)

Ethernet Networking Functional Descriptor.

**Definition** usb\_cdc.h:221

[cdc\_ecm\_descriptor::wNumberMCFilters](structcdc__ecm__descriptor.md#a196fcac7b1c9bf0f2b42a6d4ccb48de6)

uint16\_t wNumberMCFilters

**Definition** usb\_cdc.h:228

[cdc\_ecm\_descriptor::bmEthernetStatistics](structcdc__ecm__descriptor.md#a3a7b901bef04212b217a69d055e37e66)

uint32\_t bmEthernetStatistics

**Definition** usb\_cdc.h:226

[cdc\_ecm\_descriptor::bFunctionLength](structcdc__ecm__descriptor.md#aa5cfb3a02e9818cf3faaff1dbb9dd487)

uint8\_t bFunctionLength

**Definition** usb\_cdc.h:222

[cdc\_ecm\_descriptor::bDescriptorSubtype](structcdc__ecm__descriptor.md#aaf95074ec751f227a33317325567c890)

uint8\_t bDescriptorSubtype

**Definition** usb\_cdc.h:224

[cdc\_ecm\_descriptor::iMACAddress](structcdc__ecm__descriptor.md#ad43f97e428ef743d4655a1e91b91478d)

uint8\_t iMACAddress

**Definition** usb\_cdc.h:225

[cdc\_ecm\_descriptor::bDescriptorType](structcdc__ecm__descriptor.md#ae000bdad185ca5af3674274ea3fa45d6)

uint8\_t bDescriptorType

**Definition** usb\_cdc.h:223

[cdc\_ecm\_descriptor::bNumberPowerFilters](structcdc__ecm__descriptor.md#aed687a9629eb3c793af9260db407a136)

uint8\_t bNumberPowerFilters

**Definition** usb\_cdc.h:229

[cdc\_ecm\_descriptor::wMaxSegmentSize](structcdc__ecm__descriptor.md#afdf7f4478515917b1ed653118e7a8540)

uint16\_t wMaxSegmentSize

**Definition** usb\_cdc.h:227

[cdc\_header\_descriptor](structcdc__header__descriptor.md)

Header Functional Descriptor.

**Definition** usb\_cdc.h:169

[cdc\_header\_descriptor::bDescriptorType](structcdc__header__descriptor.md#a3b8cc0d8b9d56db158f3b027b2cd6f6a)

uint8\_t bDescriptorType

**Definition** usb\_cdc.h:171

[cdc\_header\_descriptor::bDescriptorSubtype](structcdc__header__descriptor.md#a49bf7e700891057f30cd3be77dec0752)

uint8\_t bDescriptorSubtype

**Definition** usb\_cdc.h:172

[cdc\_header\_descriptor::bcdCDC](structcdc__header__descriptor.md#ab66b3b87594a4510f11ba9ee950f230c)

uint16\_t bcdCDC

**Definition** usb\_cdc.h:173

[cdc\_header\_descriptor::bFunctionLength](structcdc__header__descriptor.md#ac4ad6939d5a075ff2fe6d7505cba630b)

uint8\_t bFunctionLength

**Definition** usb\_cdc.h:170

[cdc\_ncm\_descriptor](structcdc__ncm__descriptor.md)

Ethernet Network Control Model (NCM) Descriptor.

**Definition** usb\_cdc.h:233

[cdc\_ncm\_descriptor::bmNetworkCapabilities](structcdc__ncm__descriptor.md#a8a88e3d7d2b36876a38fa8025118f069)

uint8\_t bmNetworkCapabilities

**Definition** usb\_cdc.h:238

[cdc\_ncm\_descriptor::bFunctionLength](structcdc__ncm__descriptor.md#a932a73d95abf90a0ba7f0de3e1760375)

uint8\_t bFunctionLength

**Definition** usb\_cdc.h:234

[cdc\_ncm\_descriptor::bDescriptorType](structcdc__ncm__descriptor.md#a9dea58db91413ebcff65151e006a3b2c)

uint8\_t bDescriptorType

**Definition** usb\_cdc.h:235

[cdc\_ncm\_descriptor::bDescriptorSubtype](structcdc__ncm__descriptor.md#a9fb11a778a65e5e8538619467cd6c6d6)

uint8\_t bDescriptorSubtype

**Definition** usb\_cdc.h:236

[cdc\_ncm\_descriptor::bcdNcmVersion](structcdc__ncm__descriptor.md#aa9b5bd71a73783e4a3c85a1d39f9def3)

uint16\_t bcdNcmVersion

**Definition** usb\_cdc.h:237

[cdc\_union\_descriptor](structcdc__union__descriptor.md)

Union Interface Functional Descriptor.

**Definition** usb\_cdc.h:177

[cdc\_union\_descriptor::bSubordinateInterface0](structcdc__union__descriptor.md#a5bab5215179ecc0bb0bb6e7b9089abf6)

uint8\_t bSubordinateInterface0

**Definition** usb\_cdc.h:182

[cdc\_union\_descriptor::bControlInterface](structcdc__union__descriptor.md#a81bdab223598b27b620de0d9dba7bc80)

uint8\_t bControlInterface

**Definition** usb\_cdc.h:181

[cdc\_union\_descriptor::bDescriptorType](structcdc__union__descriptor.md#a839a6a4a7c4b2618c49649d93b7c6ff9)

uint8\_t bDescriptorType

**Definition** usb\_cdc.h:179

[cdc\_union\_descriptor::bFunctionLength](structcdc__union__descriptor.md#a83ee5a04668006397663142232471606)

uint8\_t bFunctionLength

**Definition** usb\_cdc.h:178

[cdc\_union\_descriptor::bDescriptorSubtype](structcdc__union__descriptor.md#a965212d833550c13376b231d5e2ce125)

uint8\_t bDescriptorSubtype

**Definition** usb\_cdc.h:180

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usb\_cdc.h](usb__cdc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
