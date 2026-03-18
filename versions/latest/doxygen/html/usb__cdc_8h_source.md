---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usb__cdc_8h_source.html
original_path: doxygen/html/usb__cdc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

31

[ 33](usb__cdc_8h.md#aaf98d38c2b9c859cf86e281bb67f27b0)#define AT\_CMD\_V250\_PROTOCOL 0x01

[ 34](usb__cdc_8h.md#ab4f22c3c42b5a4efe7735bafebc1cb9b)#define EEM\_PROTOCOL 0x07

[ 35](usb__cdc_8h.md#a20396bb325a1e947b2e4b0017a134082)#define ACM\_VENDOR\_PROTOCOL 0xFF

36

[ 41](usb__cdc_8h.md#ae4044b943c9e54cb7a64c8c35acaf8bc)#define DATA\_INTERFACE\_CLASS 0x0A

42

[ 48](usb__cdc_8h.md#a008b7d343c5a1876a78c885f7a496b66)#define HEADER\_FUNC\_DESC 0x00

[ 49](usb__cdc_8h.md#a60552aa9506dc2c6dede5146c5251aaf)#define CALL\_MANAGEMENT\_FUNC\_DESC 0x01

[ 50](usb__cdc_8h.md#a057b9de28602442b66a8c3a7befd62a7)#define ACM\_FUNC\_DESC 0x02

[ 51](usb__cdc_8h.md#aab7f21ab95fc5916f758e66087caef25)#define UNION\_FUNC\_DESC 0x06

[ 52](usb__cdc_8h.md#a22b2b55d7ab3cdd4206df07cddcc44e9)#define ETHERNET\_FUNC\_DESC 0x0F

53

[ 59](usb__cdc_8h.md#a926f6444745d1cdc991d97e4f1d265ad)#define CDC\_SEND\_ENC\_CMD 0x00

[ 60](usb__cdc_8h.md#ac9008f0dc0d4fc7141de9dd12352caa8)#define CDC\_GET\_ENC\_RSP 0x01

[ 61](usb__cdc_8h.md#a91a9c047339a1a5918b6a923af6d1af6)#define SET\_LINE\_CODING 0x20

[ 62](usb__cdc_8h.md#a6698d8d2ca56fafdc943aec2cede1daf)#define GET\_LINE\_CODING 0x21

[ 63](usb__cdc_8h.md#a437869c339749d5d011060cd5676659e)#define SET\_CONTROL\_LINE\_STATE 0x22

64

[ 69](usb__cdc_8h.md#a7e9384e6a613e38c543d7eba05f64c07)#define USB\_CDC\_NETWORK\_CONNECTION 0x00

[ 70](usb__cdc_8h.md#a970045b850b0195b5a4a2913d5a0b918)#define USB\_CDC\_RESPONSE\_AVAILABLE 0x01

[ 71](usb__cdc_8h.md#afdeb5f862a52b953653b9ab567979cec)#define USB\_CDC\_AUX\_JACK\_HOOK\_STATE 0x08

[ 72](usb__cdc_8h.md#a52452ce9272b97203fece115b5005aff)#define USB\_CDC\_RING\_DETECT 0x09

[ 73](usb__cdc_8h.md#ac167f480370c73b830281d98ad5899b1)#define USB\_CDC\_SERIAL\_STATE 0x20

[ 74](usb__cdc_8h.md#a6bb6650664f82fd25330af0357e5831e)#define USB\_CDC\_CALL\_STATE\_CHANGE 0x28

[ 75](usb__cdc_8h.md#ac63891d7c3321f7f4eb297f87c0978f6)#define USB\_CDC\_LINE\_STATE\_CHANGE 0x23

76

[ 81](usb__cdc_8h.md#a504f682d66f714730f35d282ce0b9177)#define USB\_CDC\_SERIAL\_STATE\_OVERRUN BIT(6)

[ 82](usb__cdc_8h.md#a1ff82c5d551211d2298128bd84eeb60a)#define USB\_CDC\_SERIAL\_STATE\_PARITY BIT(5)

[ 83](usb__cdc_8h.md#a59f5f1ebab838621cdc67668541432ca)#define USB\_CDC\_SERIAL\_STATE\_FRAMING BIT(4)

[ 84](usb__cdc_8h.md#a60f22cb2ae47789875e2542063899876)#define USB\_CDC\_SERIAL\_STATE\_RINGSIGNAL BIT(3)

[ 85](usb__cdc_8h.md#a15f3c90969106ecdf3b1cdf258cad5df)#define USB\_CDC\_SERIAL\_STATE\_BREAK BIT(2)

[ 86](usb__cdc_8h.md#ab96b4f63f2de0ef913862878bce1029f)#define USB\_CDC\_SERIAL\_STATE\_TXCARRIER BIT(1)

[ 87](usb__cdc_8h.md#ad720be9e3738bcba7e37dc9392c3b6e8)#define USB\_CDC\_SERIAL\_STATE\_RXCARRIER BIT(0)

88

[ 90](usb__cdc_8h.md#a00788c95fb39c2636d7d5a427282399f)#define SET\_CONTROL\_LINE\_STATE\_RTS 0x02

[ 91](usb__cdc_8h.md#a07623c40153f936c863627a3dc30da7a)#define SET\_CONTROL\_LINE\_STATE\_DTR 0x01

92

[ 94](usb__cdc_8h.md#a89554d686630d67d642e228b7ee0dc2c)#define USB\_CDC\_LINE\_CTRL\_BAUD\_RATE UART\_LINE\_CTRL\_BAUD\_RATE

[ 95](usb__cdc_8h.md#a7e6b9bb33debc489b7ac7e0fb0e94947)#define USB\_CDC\_LINE\_CTRL\_DCD UART\_LINE\_CTRL\_DCD

[ 96](usb__cdc_8h.md#a6876caf1b77477e259bb391216309799)#define USB\_CDC\_LINE\_CTRL\_DSR UART\_LINE\_CTRL\_DSR

[ 97](usb__cdc_8h.md#a716d9aaf772e1fa3f8b555077048ecbb)#define USB\_CDC\_LINE\_CTRL\_BREAK BIT(5)

[ 98](usb__cdc_8h.md#a8ec9b8c619c567cc174c0473dda5a5fd)#define USB\_CDC\_LINE\_CTRL\_RING\_SIGNAL BIT(6)

[ 99](usb__cdc_8h.md#a263186a0a64d9a8e7e9e97a54b951bdf)#define USB\_CDC\_LINE\_CTRL\_FRAMING BIT(7)

[ 100](usb__cdc_8h.md#ae2779672a5b5ab49a2ed7240e463f9e8)#define USB\_CDC\_LINE\_CTRL\_PARITY BIT(8)

[ 101](usb__cdc_8h.md#a8bf1722f98bf48394605efddf6be1295)#define USB\_CDC\_LINE\_CTRL\_OVER\_RUN BIT(9)

102

[ 104](usb__cdc_8h.md#ae38825267009563e0aa82a58a7fc4fd2)#define SERIAL\_STATE\_OVER\_RUN 0x40

[ 105](usb__cdc_8h.md#a738f180df5795376763ff233fb8aa68d)#define SERIAL\_STATE\_PARITY 0x20

[ 106](usb__cdc_8h.md#aacd68fe3a081441ee684bf2ef6312bec)#define SERIAL\_STATE\_FRAMING 0x10

[ 107](usb__cdc_8h.md#a935c772da45984e8d796396146413037)#define SERIAL\_STATE\_RING\_SIGNAL 0x08

[ 108](usb__cdc_8h.md#aa66ab791abfcf7ef5a37758c1b33138a)#define SERIAL\_STATE\_BREAK 0x04

[ 109](usb__cdc_8h.md#a22cd80b90c53ff44a4c1de08310ba3c2)#define SERIAL\_STATE\_TX\_CARRIER 0x02

[ 110](usb__cdc_8h.md#a9677c612766f3e788ad2960a17ad0791)#define SERIAL\_STATE\_RX\_CARRIER 0x01

111

[ 117](usb__cdc_8h.md#a8a06b3413e1c665f13ba4895c220d608)#define USB\_CDC\_LINE\_CODING\_STOP\_BITS\_1 0

[ 118](usb__cdc_8h.md#a4159f50590d647510a6a1f38875e012e)#define USB\_CDC\_LINE\_CODING\_STOP\_BITS\_1\_5 1

[ 119](usb__cdc_8h.md#a7e7fc73b4490a694aa982b4862782157)#define USB\_CDC\_LINE\_CODING\_STOP\_BITS\_2 2

120

[ 121](usb__cdc_8h.md#a549181d2cc92c42b4db8c3c34927d97f)#define USB\_CDC\_LINE\_CODING\_PARITY\_NO 0

[ 122](usb__cdc_8h.md#a44d808ad4f27ecf3502b9c14da2aa9b9)#define USB\_CDC\_LINE\_CODING\_PARITY\_ODD 1

[ 123](usb__cdc_8h.md#a327b5f99ab7e5cfc99d7592d1f9c1c25)#define USB\_CDC\_LINE\_CODING\_PARITY\_EVEN 2

[ 124](usb__cdc_8h.md#a490d381698ce91db4ab8bb24dd70820a)#define USB\_CDC\_LINE\_CODING\_PARITY\_MARK 3

[ 125](usb__cdc_8h.md#a5aa1b5cf30cb4020442131f66170fec6)#define USB\_CDC\_LINE\_CODING\_PARITY\_SPACE 4

126

[ 127](usb__cdc_8h.md#a327c495a9930b3e5519f0a9c7cd9ed18)#define USB\_CDC\_LINE\_CODING\_DATA\_BITS\_5 5

[ 128](usb__cdc_8h.md#a231932add6d9ceef4f5332a0db1b9f55)#define USB\_CDC\_LINE\_CODING\_DATA\_BITS\_6 6

[ 129](usb__cdc_8h.md#a6a276593bc4587671df5e6da8cce5ebb)#define USB\_CDC\_LINE\_CODING\_DATA\_BITS\_7 7

[ 130](usb__cdc_8h.md#a64e296aec72bbd8f9bdc1aefa5aab654)#define USB\_CDC\_LINE\_CODING\_DATA\_BITS\_8 8

131

[ 136](usb__cdc_8h.md#a4dce35ee8cf2337bab3c90081200a9f6)#define SET\_ETHERNET\_MULTICAST\_FILTERS 0x40

[ 137](usb__cdc_8h.md#a1506deda422ee354040b0feeb09ad4b6)#define SET\_ETHERNET\_PM\_FILTER 0x41

[ 138](usb__cdc_8h.md#a53ea6ae0e1fe8a88350740fd594507fd)#define GET\_ETHERNET\_PM\_FILTER 0x42

[ 139](usb__cdc_8h.md#adae019242224bbbc9d0f853da3733f1c)#define SET\_ETHERNET\_PACKET\_FILTER 0x43

[ 140](usb__cdc_8h.md#a7dffeba1576d6660fb930eabc5c515b7)#define GET\_ETHERNET\_STATISTIC 0x44

141

[ 143](usb__cdc_8h.md#a4abfd25c9ca3e70c5b33b89ee9456087)#define PACKET\_TYPE\_MULTICAST 0x10

[ 144](usb__cdc_8h.md#a3143cff5f7275d394f259c3b83e54e4b)#define PACKET\_TYPE\_BROADCAST 0x08

[ 145](usb__cdc_8h.md#a5a2d0aa22741a4a48b976cddc6f57f98)#define PACKET\_TYPE\_DIRECTED 0x04

[ 146](usb__cdc_8h.md#aac32de24c40e08d0d32d3db264fa964a)#define PACKET\_TYPE\_ALL\_MULTICAST 0x02

[ 147](usb__cdc_8h.md#a7be4d4e65526efb94ea1ef71da62f835)#define PACKET\_TYPE\_PROMISCUOUS 0x01

148

[ 150](structcdc__header__descriptor.md)struct [cdc\_header\_descriptor](structcdc__header__descriptor.md) {

[ 151](structcdc__header__descriptor.md#ac4ad6939d5a075ff2fe6d7505cba630b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionLength](structcdc__header__descriptor.md#ac4ad6939d5a075ff2fe6d7505cba630b);

[ 152](structcdc__header__descriptor.md#a3b8cc0d8b9d56db158f3b027b2cd6f6a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structcdc__header__descriptor.md#a3b8cc0d8b9d56db158f3b027b2cd6f6a);

[ 153](structcdc__header__descriptor.md#a49bf7e700891057f30cd3be77dec0752) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorSubtype](structcdc__header__descriptor.md#a49bf7e700891057f30cd3be77dec0752);

[ 154](structcdc__header__descriptor.md#ab66b3b87594a4510f11ba9ee950f230c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bcdCDC](structcdc__header__descriptor.md#ab66b3b87594a4510f11ba9ee950f230c);

155} \_\_packed;

156

[ 158](structcdc__union__descriptor.md)struct [cdc\_union\_descriptor](structcdc__union__descriptor.md) {

[ 159](structcdc__union__descriptor.md#a83ee5a04668006397663142232471606) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionLength](structcdc__union__descriptor.md#a83ee5a04668006397663142232471606);

[ 160](structcdc__union__descriptor.md#a839a6a4a7c4b2618c49649d93b7c6ff9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structcdc__union__descriptor.md#a839a6a4a7c4b2618c49649d93b7c6ff9);

[ 161](structcdc__union__descriptor.md#a965212d833550c13376b231d5e2ce125) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorSubtype](structcdc__union__descriptor.md#a965212d833550c13376b231d5e2ce125);

[ 162](structcdc__union__descriptor.md#a81bdab223598b27b620de0d9dba7bc80) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bControlInterface](structcdc__union__descriptor.md#a81bdab223598b27b620de0d9dba7bc80);

[ 163](structcdc__union__descriptor.md#a5bab5215179ecc0bb0bb6e7b9089abf6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bSubordinateInterface0](structcdc__union__descriptor.md#a5bab5215179ecc0bb0bb6e7b9089abf6);

164} \_\_packed;

165

[ 167](structcdc__cm__descriptor.md)struct [cdc\_cm\_descriptor](structcdc__cm__descriptor.md) {

[ 168](structcdc__cm__descriptor.md#a578a2a39c7c80de58cb7d952f8decd22) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionLength](structcdc__cm__descriptor.md#a578a2a39c7c80de58cb7d952f8decd22);

[ 169](structcdc__cm__descriptor.md#ad40616645c5b28754300594b43805a1f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structcdc__cm__descriptor.md#ad40616645c5b28754300594b43805a1f);

[ 170](structcdc__cm__descriptor.md#a908003360bca9ab79f55d80a2fc7aa24) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorSubtype](structcdc__cm__descriptor.md#a908003360bca9ab79f55d80a2fc7aa24);

[ 171](structcdc__cm__descriptor.md#aabbca6f88b936659124aa28264054b6d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bmCapabilities](structcdc__cm__descriptor.md#aabbca6f88b936659124aa28264054b6d);

[ 172](structcdc__cm__descriptor.md#a0a29f8dfe1dd9758f210b63d7a87bdc6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDataInterface](structcdc__cm__descriptor.md#a0a29f8dfe1dd9758f210b63d7a87bdc6);

173} \_\_packed;

174

[ 176](structcdc__acm__descriptor.md)struct [cdc\_acm\_descriptor](structcdc__acm__descriptor.md) {

[ 177](structcdc__acm__descriptor.md#a665260ce8cc55e35c941078987f92366) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionLength](structcdc__acm__descriptor.md#a665260ce8cc55e35c941078987f92366);

[ 178](structcdc__acm__descriptor.md#ab62800772430a82673004fcaac13c071) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structcdc__acm__descriptor.md#ab62800772430a82673004fcaac13c071);

[ 179](structcdc__acm__descriptor.md#ae1011a0e1520193be5c1fb0fe442915e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorSubtype](structcdc__acm__descriptor.md#ae1011a0e1520193be5c1fb0fe442915e);

[ 180](structcdc__acm__descriptor.md#a3066a08cbc5f0747d435a13ee4f22d14) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bmCapabilities](structcdc__acm__descriptor.md#a3066a08cbc5f0747d435a13ee4f22d14);

181} \_\_packed;

182

[ 184](structcdc__acm__line__coding.md)struct [cdc\_acm\_line\_coding](structcdc__acm__line__coding.md) {

[ 185](structcdc__acm__line__coding.md#a14d35b67e6f00b0d6196ba0e9ef6dfab) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dwDTERate](structcdc__acm__line__coding.md#a14d35b67e6f00b0d6196ba0e9ef6dfab);

[ 186](structcdc__acm__line__coding.md#afd2fd70a7da783d7aac0d99f9f267383) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bCharFormat](structcdc__acm__line__coding.md#afd2fd70a7da783d7aac0d99f9f267383);

[ 187](structcdc__acm__line__coding.md#a472270d84e160348e024f756b834cbb8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bParityType](structcdc__acm__line__coding.md#a472270d84e160348e024f756b834cbb8);

[ 188](structcdc__acm__line__coding.md#ab685d018d83e3e2d38c87c27902cca3e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDataBits](structcdc__acm__line__coding.md#ab685d018d83e3e2d38c87c27902cca3e);

189} \_\_packed;

190

[ 192](structcdc__acm__notification.md)struct [cdc\_acm\_notification](structcdc__acm__notification.md) {

[ 193](structcdc__acm__notification.md#a57b007a8ec893d660e6ec8a1b25f7dd3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bmRequestType](structcdc__acm__notification.md#a57b007a8ec893d660e6ec8a1b25f7dd3);

[ 194](structcdc__acm__notification.md#af24dae76a280c008e40a0d031171235c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bNotificationType](structcdc__acm__notification.md#af24dae76a280c008e40a0d031171235c);

[ 195](structcdc__acm__notification.md#a3bf290bc6e851331e93bedf49ae5dbe0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wValue](structcdc__acm__notification.md#a3bf290bc6e851331e93bedf49ae5dbe0);

[ 196](structcdc__acm__notification.md#a290717590343376c8f1f9a865cb4b0ae) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wIndex](structcdc__acm__notification.md#a290717590343376c8f1f9a865cb4b0ae);

[ 197](structcdc__acm__notification.md#af2f8fbceeaa9a3ad0ae1330b8f82bff2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wLength](structcdc__acm__notification.md#af2f8fbceeaa9a3ad0ae1330b8f82bff2);

[ 198](structcdc__acm__notification.md#a5666402ce9fbe5fad5f80592aa6f53ec) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data](structcdc__acm__notification.md#a5666402ce9fbe5fad5f80592aa6f53ec);

199} \_\_packed;

200

[ 202](structcdc__ecm__descriptor.md)struct [cdc\_ecm\_descriptor](structcdc__ecm__descriptor.md) {

[ 203](structcdc__ecm__descriptor.md#aa5cfb3a02e9818cf3faaff1dbb9dd487) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionLength](structcdc__ecm__descriptor.md#aa5cfb3a02e9818cf3faaff1dbb9dd487);

[ 204](structcdc__ecm__descriptor.md#ae000bdad185ca5af3674274ea3fa45d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structcdc__ecm__descriptor.md#ae000bdad185ca5af3674274ea3fa45d6);

[ 205](structcdc__ecm__descriptor.md#aaf95074ec751f227a33317325567c890) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorSubtype](structcdc__ecm__descriptor.md#aaf95074ec751f227a33317325567c890);

[ 206](structcdc__ecm__descriptor.md#ad43f97e428ef743d4655a1e91b91478d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iMACAddress](structcdc__ecm__descriptor.md#ad43f97e428ef743d4655a1e91b91478d);

[ 207](structcdc__ecm__descriptor.md#a3a7b901bef04212b217a69d055e37e66) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bmEthernetStatistics](structcdc__ecm__descriptor.md#a3a7b901bef04212b217a69d055e37e66);

[ 208](structcdc__ecm__descriptor.md#afdf7f4478515917b1ed653118e7a8540) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wMaxSegmentSize](structcdc__ecm__descriptor.md#afdf7f4478515917b1ed653118e7a8540);

[ 209](structcdc__ecm__descriptor.md#a196fcac7b1c9bf0f2b42a6d4ccb48de6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wNumberMCFilters](structcdc__ecm__descriptor.md#a196fcac7b1c9bf0f2b42a6d4ccb48de6);

[ 210](structcdc__ecm__descriptor.md#aed687a9629eb3c793af9260db407a136) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bNumberPowerFilters](structcdc__ecm__descriptor.md#aed687a9629eb3c793af9260db407a136);

211} \_\_packed;

212

213#endif /\* ZEPHYR\_INCLUDE\_USB\_CLASS\_USB\_CDC\_H\_ \*/

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

**Definition** usb\_cdc.h:176

[cdc\_acm\_descriptor::bmCapabilities](structcdc__acm__descriptor.md#a3066a08cbc5f0747d435a13ee4f22d14)

uint8\_t bmCapabilities

**Definition** usb\_cdc.h:180

[cdc\_acm\_descriptor::bFunctionLength](structcdc__acm__descriptor.md#a665260ce8cc55e35c941078987f92366)

uint8\_t bFunctionLength

**Definition** usb\_cdc.h:177

[cdc\_acm\_descriptor::bDescriptorType](structcdc__acm__descriptor.md#ab62800772430a82673004fcaac13c071)

uint8\_t bDescriptorType

**Definition** usb\_cdc.h:178

[cdc\_acm\_descriptor::bDescriptorSubtype](structcdc__acm__descriptor.md#ae1011a0e1520193be5c1fb0fe442915e)

uint8\_t bDescriptorSubtype

**Definition** usb\_cdc.h:179

[cdc\_acm\_line\_coding](structcdc__acm__line__coding.md)

Data structure for GET\_LINE\_CODING / SET\_LINE\_CODING class requests.

**Definition** usb\_cdc.h:184

[cdc\_acm\_line\_coding::dwDTERate](structcdc__acm__line__coding.md#a14d35b67e6f00b0d6196ba0e9ef6dfab)

uint32\_t dwDTERate

**Definition** usb\_cdc.h:185

[cdc\_acm\_line\_coding::bParityType](structcdc__acm__line__coding.md#a472270d84e160348e024f756b834cbb8)

uint8\_t bParityType

**Definition** usb\_cdc.h:187

[cdc\_acm\_line\_coding::bDataBits](structcdc__acm__line__coding.md#ab685d018d83e3e2d38c87c27902cca3e)

uint8\_t bDataBits

**Definition** usb\_cdc.h:188

[cdc\_acm\_line\_coding::bCharFormat](structcdc__acm__line__coding.md#afd2fd70a7da783d7aac0d99f9f267383)

uint8\_t bCharFormat

**Definition** usb\_cdc.h:186

[cdc\_acm\_notification](structcdc__acm__notification.md)

Data structure for the notification about SerialState.

**Definition** usb\_cdc.h:192

[cdc\_acm\_notification::wIndex](structcdc__acm__notification.md#a290717590343376c8f1f9a865cb4b0ae)

uint16\_t wIndex

**Definition** usb\_cdc.h:196

[cdc\_acm\_notification::wValue](structcdc__acm__notification.md#a3bf290bc6e851331e93bedf49ae5dbe0)

uint16\_t wValue

**Definition** usb\_cdc.h:195

[cdc\_acm\_notification::data](structcdc__acm__notification.md#a5666402ce9fbe5fad5f80592aa6f53ec)

uint16\_t data

**Definition** usb\_cdc.h:198

[cdc\_acm\_notification::bmRequestType](structcdc__acm__notification.md#a57b007a8ec893d660e6ec8a1b25f7dd3)

uint8\_t bmRequestType

**Definition** usb\_cdc.h:193

[cdc\_acm\_notification::bNotificationType](structcdc__acm__notification.md#af24dae76a280c008e40a0d031171235c)

uint8\_t bNotificationType

**Definition** usb\_cdc.h:194

[cdc\_acm\_notification::wLength](structcdc__acm__notification.md#af2f8fbceeaa9a3ad0ae1330b8f82bff2)

uint16\_t wLength

**Definition** usb\_cdc.h:197

[cdc\_cm\_descriptor](structcdc__cm__descriptor.md)

Call Management Functional Descriptor.

**Definition** usb\_cdc.h:167

[cdc\_cm\_descriptor::bDataInterface](structcdc__cm__descriptor.md#a0a29f8dfe1dd9758f210b63d7a87bdc6)

uint8\_t bDataInterface

**Definition** usb\_cdc.h:172

[cdc\_cm\_descriptor::bFunctionLength](structcdc__cm__descriptor.md#a578a2a39c7c80de58cb7d952f8decd22)

uint8\_t bFunctionLength

**Definition** usb\_cdc.h:168

[cdc\_cm\_descriptor::bDescriptorSubtype](structcdc__cm__descriptor.md#a908003360bca9ab79f55d80a2fc7aa24)

uint8\_t bDescriptorSubtype

**Definition** usb\_cdc.h:170

[cdc\_cm\_descriptor::bmCapabilities](structcdc__cm__descriptor.md#aabbca6f88b936659124aa28264054b6d)

uint8\_t bmCapabilities

**Definition** usb\_cdc.h:171

[cdc\_cm\_descriptor::bDescriptorType](structcdc__cm__descriptor.md#ad40616645c5b28754300594b43805a1f)

uint8\_t bDescriptorType

**Definition** usb\_cdc.h:169

[cdc\_ecm\_descriptor](structcdc__ecm__descriptor.md)

Ethernet Networking Functional Descriptor.

**Definition** usb\_cdc.h:202

[cdc\_ecm\_descriptor::wNumberMCFilters](structcdc__ecm__descriptor.md#a196fcac7b1c9bf0f2b42a6d4ccb48de6)

uint16\_t wNumberMCFilters

**Definition** usb\_cdc.h:209

[cdc\_ecm\_descriptor::bmEthernetStatistics](structcdc__ecm__descriptor.md#a3a7b901bef04212b217a69d055e37e66)

uint32\_t bmEthernetStatistics

**Definition** usb\_cdc.h:207

[cdc\_ecm\_descriptor::bFunctionLength](structcdc__ecm__descriptor.md#aa5cfb3a02e9818cf3faaff1dbb9dd487)

uint8\_t bFunctionLength

**Definition** usb\_cdc.h:203

[cdc\_ecm\_descriptor::bDescriptorSubtype](structcdc__ecm__descriptor.md#aaf95074ec751f227a33317325567c890)

uint8\_t bDescriptorSubtype

**Definition** usb\_cdc.h:205

[cdc\_ecm\_descriptor::iMACAddress](structcdc__ecm__descriptor.md#ad43f97e428ef743d4655a1e91b91478d)

uint8\_t iMACAddress

**Definition** usb\_cdc.h:206

[cdc\_ecm\_descriptor::bDescriptorType](structcdc__ecm__descriptor.md#ae000bdad185ca5af3674274ea3fa45d6)

uint8\_t bDescriptorType

**Definition** usb\_cdc.h:204

[cdc\_ecm\_descriptor::bNumberPowerFilters](structcdc__ecm__descriptor.md#aed687a9629eb3c793af9260db407a136)

uint8\_t bNumberPowerFilters

**Definition** usb\_cdc.h:210

[cdc\_ecm\_descriptor::wMaxSegmentSize](structcdc__ecm__descriptor.md#afdf7f4478515917b1ed653118e7a8540)

uint16\_t wMaxSegmentSize

**Definition** usb\_cdc.h:208

[cdc\_header\_descriptor](structcdc__header__descriptor.md)

Header Functional Descriptor.

**Definition** usb\_cdc.h:150

[cdc\_header\_descriptor::bDescriptorType](structcdc__header__descriptor.md#a3b8cc0d8b9d56db158f3b027b2cd6f6a)

uint8\_t bDescriptorType

**Definition** usb\_cdc.h:152

[cdc\_header\_descriptor::bDescriptorSubtype](structcdc__header__descriptor.md#a49bf7e700891057f30cd3be77dec0752)

uint8\_t bDescriptorSubtype

**Definition** usb\_cdc.h:153

[cdc\_header\_descriptor::bcdCDC](structcdc__header__descriptor.md#ab66b3b87594a4510f11ba9ee950f230c)

uint16\_t bcdCDC

**Definition** usb\_cdc.h:154

[cdc\_header\_descriptor::bFunctionLength](structcdc__header__descriptor.md#ac4ad6939d5a075ff2fe6d7505cba630b)

uint8\_t bFunctionLength

**Definition** usb\_cdc.h:151

[cdc\_union\_descriptor](structcdc__union__descriptor.md)

Union Interface Functional Descriptor.

**Definition** usb\_cdc.h:158

[cdc\_union\_descriptor::bSubordinateInterface0](structcdc__union__descriptor.md#a5bab5215179ecc0bb0bb6e7b9089abf6)

uint8\_t bSubordinateInterface0

**Definition** usb\_cdc.h:163

[cdc\_union\_descriptor::bControlInterface](structcdc__union__descriptor.md#a81bdab223598b27b620de0d9dba7bc80)

uint8\_t bControlInterface

**Definition** usb\_cdc.h:162

[cdc\_union\_descriptor::bDescriptorType](structcdc__union__descriptor.md#a839a6a4a7c4b2618c49649d93b7c6ff9)

uint8\_t bDescriptorType

**Definition** usb\_cdc.h:160

[cdc\_union\_descriptor::bFunctionLength](structcdc__union__descriptor.md#a83ee5a04668006397663142232471606)

uint8\_t bFunctionLength

**Definition** usb\_cdc.h:159

[cdc\_union\_descriptor::bDescriptorSubtype](structcdc__union__descriptor.md#a965212d833550c13376b231d5e2ce125)

uint8\_t bDescriptorSubtype

**Definition** usb\_cdc.h:161

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usb\_cdc.h](usb__cdc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
