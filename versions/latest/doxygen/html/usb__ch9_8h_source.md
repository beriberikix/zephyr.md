---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usb__ch9_8h_source.html
original_path: doxygen/html/usb__ch9_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_ch9.h

[Go to the documentation of this file.](usb__ch9_8h.md)

1/\*

2 \* Copyright (c) 2020 PHYTEC Messtechnik GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#include <version.h>

16#include <[zephyr/sys/util.h](util_8h.md)>

17#include <[zephyr/usb/class/usb\_hub.h](usb__hub_8h.md)>

18

19#ifndef ZEPHYR\_INCLUDE\_USB\_CH9\_H\_

20#define ZEPHYR\_INCLUDE\_USB\_CH9\_H\_

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 26](structusb__req__type__field.md)struct [usb\_req\_type\_field](structusb__req__type__field.md) {

27#ifdef CONFIG\_LITTLE\_ENDIAN

28 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [recipient](structusb__req__type__field.md#aa75b3b73833a9c8163ab9539817d1f31) : 5;

29 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structusb__req__type__field.md#ab3c23439784768b6ddf71b81d58452d0) : 2;

30 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [direction](structusb__req__type__field.md#af312d3f2c354d2ed987a25b55b299efd) : 1;

31#else

[ 32](structusb__req__type__field.md#af312d3f2c354d2ed987a25b55b299efd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [direction](structusb__req__type__field.md#af312d3f2c354d2ed987a25b55b299efd) : 1;

[ 33](structusb__req__type__field.md#ab3c23439784768b6ddf71b81d58452d0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structusb__req__type__field.md#ab3c23439784768b6ddf71b81d58452d0) : 2;

[ 34](structusb__req__type__field.md#aa75b3b73833a9c8163ab9539817d1f31) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [recipient](structusb__req__type__field.md#aa75b3b73833a9c8163ab9539817d1f31) : 5;

35#endif

36} \_\_packed;

37

[ 39](structusb__setup__packet.md)struct [usb\_setup\_packet](structusb__setup__packet.md) {

40 union {

[ 41](structusb__setup__packet.md#a326cfb3e8b11cc2e7cf4738d593cf10a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bmRequestType](structusb__setup__packet.md#a326cfb3e8b11cc2e7cf4738d593cf10a);

[ 42](structusb__setup__packet.md#afa3d273ae57c3124b14ab100ac9f9a24) struct [usb\_req\_type\_field](structusb__req__type__field.md) [RequestType](structusb__setup__packet.md#afa3d273ae57c3124b14ab100ac9f9a24);

43 };

[ 44](structusb__setup__packet.md#aab50ed2f2cdcc1d747f6f224fe9d2018) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bRequest](structusb__setup__packet.md#aab50ed2f2cdcc1d747f6f224fe9d2018);

[ 45](structusb__setup__packet.md#a619fbc1b9b6452f4394da713bdbc6a89) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wValue](structusb__setup__packet.md#a619fbc1b9b6452f4394da713bdbc6a89);

[ 46](structusb__setup__packet.md#a953c058f0e31481a3d59b404037be009) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wIndex](structusb__setup__packet.md#a953c058f0e31481a3d59b404037be009);

[ 47](structusb__setup__packet.md#a3421c921569bf3727534652c5f71da96) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wLength](structusb__setup__packet.md#a3421c921569bf3727534652c5f71da96);

48};

49

[ 51](usb__ch9_8h.md#a3e431a6f30304833b6aa45a454c8bdbd)#define USB\_REQTYPE\_DIR\_TO\_DEVICE 0

[ 52](usb__ch9_8h.md#aa080957f00a9459f9f7c533da893b31f)#define USB\_REQTYPE\_DIR\_TO\_HOST 1

53

[ 55](usb__ch9_8h.md#a9529fae2802d82fd37d4ad58ab9d6f67)#define USB\_REQTYPE\_TYPE\_STANDARD 0

[ 56](usb__ch9_8h.md#abaeb448434207462bcb312973a013f3d)#define USB\_REQTYPE\_TYPE\_CLASS 1

[ 57](usb__ch9_8h.md#ad06cc151ffddfeba7bc99b819101d11d)#define USB\_REQTYPE\_TYPE\_VENDOR 2

[ 58](usb__ch9_8h.md#ab43bb12a355f38ea09a1dee177619b78)#define USB\_REQTYPE\_TYPE\_RESERVED 3

59

[ 61](usb__ch9_8h.md#ab71be1695c56514626b15d3790e3d934)#define USB\_REQTYPE\_RECIPIENT\_DEVICE 0

[ 62](usb__ch9_8h.md#a8c2c0646290270444df73b1319232ea7)#define USB\_REQTYPE\_RECIPIENT\_INTERFACE 1

[ 63](usb__ch9_8h.md#a32154b80a8d73dfb4e261d31a8d351fa)#define USB\_REQTYPE\_RECIPIENT\_ENDPOINT 2

[ 64](usb__ch9_8h.md#a2e07a8841cf9d67dc0c60badc00761b0)#define USB\_REQTYPE\_RECIPIENT\_OTHER 3

65

[ 67](usb__ch9_8h.md#ab9c7b95bb1467f3d116432ac9194e92d)#define USB\_REQTYPE\_GET\_DIR(bmRequestType) (((bmRequestType) >> 7) & 0x01U)

[ 69](usb__ch9_8h.md#a18dd1450e8fe287b2de1f8871274a3b9)#define USB\_REQTYPE\_GET\_TYPE(bmRequestType) (((bmRequestType) >> 5) & 0x03U)

[ 71](usb__ch9_8h.md#a933742b41b1da36545639df1a08c0db5)#define USB\_REQTYPE\_GET\_RECIPIENT(bmRequestType) ((bmRequestType) & 0x1FU)

72

[ 79](usb__ch9_8h.md#a88dd2eb9cd06e825eb5de6a8ad38c97c)static inline bool [usb\_reqtype\_is\_to\_host](usb__ch9_8h.md#a88dd2eb9cd06e825eb5de6a8ad38c97c)(const struct [usb\_setup\_packet](structusb__setup__packet.md) \*setup)

80{

81 return setup->[RequestType](structusb__setup__packet.md#afa3d273ae57c3124b14ab100ac9f9a24).[direction](structusb__req__type__field.md#af312d3f2c354d2ed987a25b55b299efd) == [USB\_REQTYPE\_DIR\_TO\_HOST](usb__ch9_8h.md#aa080957f00a9459f9f7c533da893b31f);

82}

83

[ 90](usb__ch9_8h.md#a7542609be1ae1730be4e14d4242d9696)static inline bool [usb\_reqtype\_is\_to\_device](usb__ch9_8h.md#a7542609be1ae1730be4e14d4242d9696)(const struct [usb\_setup\_packet](structusb__setup__packet.md) \*setup)

91{

92 return setup->[RequestType](structusb__setup__packet.md#afa3d273ae57c3124b14ab100ac9f9a24).[direction](structusb__req__type__field.md#af312d3f2c354d2ed987a25b55b299efd) == [USB\_REQTYPE\_DIR\_TO\_DEVICE](usb__ch9_8h.md#a3e431a6f30304833b6aa45a454c8bdbd);

93}

94

[ 96](usb__ch9_8h.md#afffb7748ffdb525572e407024df9a201)#define USB\_SREQ\_GET\_STATUS 0x00

[ 97](usb__ch9_8h.md#a16d58595c13caa66989d63343de6bccb)#define USB\_SREQ\_CLEAR\_FEATURE 0x01

[ 98](usb__ch9_8h.md#ac1ef5c9fe1f3107f1a55560f81b6e25a)#define USB\_SREQ\_SET\_FEATURE 0x03

[ 99](usb__ch9_8h.md#ac20c25ea20acac5d0f4484e3d9a5c759)#define USB\_SREQ\_SET\_ADDRESS 0x05

[ 100](usb__ch9_8h.md#ab3b49f2eb21dcd597ca73ea62bfa5523)#define USB\_SREQ\_GET\_DESCRIPTOR 0x06

[ 101](usb__ch9_8h.md#ac95699668d43a49f1dd17ee86220984c)#define USB\_SREQ\_SET\_DESCRIPTOR 0x07

[ 102](usb__ch9_8h.md#a505c325ea65c44f9df6df87bef30f5ee)#define USB\_SREQ\_GET\_CONFIGURATION 0x08

[ 103](usb__ch9_8h.md#a0f87cedfecf77bba9c52514684a13bf3)#define USB\_SREQ\_SET\_CONFIGURATION 0x09

[ 104](usb__ch9_8h.md#a26034252f1f8ddc5d7793e1ff3974764)#define USB\_SREQ\_GET\_INTERFACE 0x0A

[ 105](usb__ch9_8h.md#acf5ea7c90528a4d9d86c279318a6cb52)#define USB\_SREQ\_SET\_INTERFACE 0x0B

[ 106](usb__ch9_8h.md#a390ddf7167cc081fd3d3f24f09967d06)#define USB\_SREQ\_SYNCH\_FRAME 0x0C

107

[ 109](usb__ch9_8h.md#aefeff68c3a236749d1105d94ed9bad68)#define USB\_DESC\_DEVICE 1

[ 110](usb__ch9_8h.md#a7764131f2e59070eb032bd9d68d32620)#define USB\_DESC\_CONFIGURATION 2

[ 111](usb__ch9_8h.md#a6a5678b964f3a9b4ba2f52e9a51bebf5)#define USB\_DESC\_STRING 3

[ 112](usb__ch9_8h.md#ab98b6a1b7ec1dc4adcbd188c3a38f69f)#define USB\_DESC\_INTERFACE 4

[ 113](usb__ch9_8h.md#a1428ae675c4b17d84b91eda705fe0498)#define USB\_DESC\_ENDPOINT 5

[ 114](usb__ch9_8h.md#aae4580f7a31247f2bce47af2f27b3a64)#define USB\_DESC\_DEVICE\_QUALIFIER 6

[ 115](usb__ch9_8h.md#a3a8acce20fbea73ab685bb55a4a6356d)#define USB\_DESC\_OTHER\_SPEED 7

[ 116](usb__ch9_8h.md#a075dd47d721cfd6cdf804f3cdf0feae1)#define USB\_DESC\_INTERFACE\_POWER 8

[ 118](usb__ch9_8h.md#a162988e9c51e1094635a553999f52d51)#define USB\_DESC\_OTG 9

[ 119](usb__ch9_8h.md#a0a7ab16adb76e6b9af587a82d5a7fbb3)#define USB\_DESC\_DEBUG 10

[ 120](usb__ch9_8h.md#ac84354aa0bfec12d3e21e72d29caf48b)#define USB\_DESC\_INTERFACE\_ASSOC 11

[ 121](usb__ch9_8h.md#a9f6e306632b56036d4dd7cc2430bcec9)#define USB\_DESC\_BOS 15

[ 122](usb__ch9_8h.md#a8ff1997b326965664d90926658af7e98)#define USB\_DESC\_DEVICE\_CAPABILITY 16

123

[ 127](usb__ch9_8h.md#a4ee3b5be16342ce919483c66cc701cb4)#define USB\_DESC\_CS\_DEVICE 0x21

[ 128](usb__ch9_8h.md#a7221e0186e4e17a624b739d1807c161d)#define USB\_DESC\_CS\_CONFIGURATION 0x22

[ 129](usb__ch9_8h.md#a0a89e53a56fcadd9f7b9e08e4d9ef5f8)#define USB\_DESC\_CS\_STRING 0x23

[ 130](usb__ch9_8h.md#ae47a98df81bbd33336e11c3742418217)#define USB\_DESC\_CS\_INTERFACE 0x24

[ 131](usb__ch9_8h.md#a3222223114b6d7ecea051a862fb685e2)#define USB\_DESC\_CS\_ENDPOINT 0x25

132

[ 134](usb__ch9_8h.md#a78ee83859d881216f702a349e9c5133b)#define USB\_SFS\_ENDPOINT\_HALT 0x00

[ 135](usb__ch9_8h.md#a954bd576fddb8178e15bb3081733e49c)#define USB\_SFS\_REMOTE\_WAKEUP 0x01

[ 136](usb__ch9_8h.md#ae2a2cf879eace08bf86d330b39578792)#define USB\_SFS\_TEST\_MODE 0x02

137

[ 139](usb__ch9_8h.md#a9dd608d5ce8d45fdd76bad3df4fdf34d)#define USB\_GET\_STATUS\_SELF\_POWERED BIT(0)

[ 140](usb__ch9_8h.md#a6d896f4f58e13f87f8e74af6909fada9)#define USB\_GET\_STATUS\_REMOTE\_WAKEUP BIT(1)

141

[ 143](structusb__desc__header.md)struct [usb\_desc\_header](structusb__desc__header.md) {

[ 144](structusb__desc__header.md#a630c1fe55342f903d9a17663ef2729da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusb__desc__header.md#a630c1fe55342f903d9a17663ef2729da);

[ 145](structusb__desc__header.md#a43ae191657b7be54357d445ff1d98950) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusb__desc__header.md#a43ae191657b7be54357d445ff1d98950);

146} \_\_packed;

147

[ 149](structusb__device__descriptor.md)struct [usb\_device\_descriptor](structusb__device__descriptor.md) {

[ 150](structusb__device__descriptor.md#af3f980ad55af3fd6c222a8802996ab63) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusb__device__descriptor.md#af3f980ad55af3fd6c222a8802996ab63);

[ 151](structusb__device__descriptor.md#ad1ba08da6ad5b6023f1d0d1461daab7d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusb__device__descriptor.md#ad1ba08da6ad5b6023f1d0d1461daab7d);

[ 152](structusb__device__descriptor.md#aa400edb6c3183d4922411cdaf980b84e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bcdUSB](structusb__device__descriptor.md#aa400edb6c3183d4922411cdaf980b84e);

[ 153](structusb__device__descriptor.md#aa657267e1d9762b7d2ed3eb60a78d9ad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDeviceClass](structusb__device__descriptor.md#aa657267e1d9762b7d2ed3eb60a78d9ad);

[ 154](structusb__device__descriptor.md#aecfbe730bc3eeccc9c4b5fd17f5f3c3c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDeviceSubClass](structusb__device__descriptor.md#aecfbe730bc3eeccc9c4b5fd17f5f3c3c);

[ 155](structusb__device__descriptor.md#a56829af76e57a6ea4fc621b52a0664f8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDeviceProtocol](structusb__device__descriptor.md#a56829af76e57a6ea4fc621b52a0664f8);

[ 156](structusb__device__descriptor.md#ac7f47eb197506ac5c555bb4f2fe82d32) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bMaxPacketSize0](structusb__device__descriptor.md#ac7f47eb197506ac5c555bb4f2fe82d32);

[ 157](structusb__device__descriptor.md#a043126e48bebbab536540e44428b6b4f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [idVendor](structusb__device__descriptor.md#a043126e48bebbab536540e44428b6b4f);

[ 158](structusb__device__descriptor.md#a70d5ecc7bad486b8a8840d86aa151579) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [idProduct](structusb__device__descriptor.md#a70d5ecc7bad486b8a8840d86aa151579);

[ 159](structusb__device__descriptor.md#a41416aa4a49999d2f3f0f67bdc5fa7da) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bcdDevice](structusb__device__descriptor.md#a41416aa4a49999d2f3f0f67bdc5fa7da);

[ 160](structusb__device__descriptor.md#ad082330020575944b8471459b816cb40) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iManufacturer](structusb__device__descriptor.md#ad082330020575944b8471459b816cb40);

[ 161](structusb__device__descriptor.md#acb90b91c59e65adbcc21949cf0f486f7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iProduct](structusb__device__descriptor.md#acb90b91c59e65adbcc21949cf0f486f7);

[ 162](structusb__device__descriptor.md#a105d91b68091e61c9b13ea673fb98eaf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iSerialNumber](structusb__device__descriptor.md#a105d91b68091e61c9b13ea673fb98eaf);

[ 163](structusb__device__descriptor.md#a603204b0517e9ece9bc0d8476b2a7cdc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bNumConfigurations](structusb__device__descriptor.md#a603204b0517e9ece9bc0d8476b2a7cdc);

164} \_\_packed;

165

[ 167](structusb__cfg__descriptor.md)struct [usb\_cfg\_descriptor](structusb__cfg__descriptor.md) {

[ 168](structusb__cfg__descriptor.md#a04fb3193880a8676f686f0f2ad8adbf4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusb__cfg__descriptor.md#a04fb3193880a8676f686f0f2ad8adbf4);

[ 169](structusb__cfg__descriptor.md#aa89fd9e8dd2bace7709d77de1d0b2588) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusb__cfg__descriptor.md#aa89fd9e8dd2bace7709d77de1d0b2588);

[ 170](structusb__cfg__descriptor.md#ae7f2a2fde3210e6460b20b0d17b820de) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wTotalLength](structusb__cfg__descriptor.md#ae7f2a2fde3210e6460b20b0d17b820de);

[ 171](structusb__cfg__descriptor.md#adcb6ff8c1accd4b950c9ebfd4f98718f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bNumInterfaces](structusb__cfg__descriptor.md#adcb6ff8c1accd4b950c9ebfd4f98718f);

[ 172](structusb__cfg__descriptor.md#a7500c52ffbb63ece0be5cde7c672615d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bConfigurationValue](structusb__cfg__descriptor.md#a7500c52ffbb63ece0be5cde7c672615d);

[ 173](structusb__cfg__descriptor.md#ac3b8ca556e08a9b31fd0de906e000038) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iConfiguration](structusb__cfg__descriptor.md#ac3b8ca556e08a9b31fd0de906e000038);

[ 174](structusb__cfg__descriptor.md#a6cc23afd69dd7fb77f4bc5ea55315f4c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bmAttributes](structusb__cfg__descriptor.md#a6cc23afd69dd7fb77f4bc5ea55315f4c);

[ 175](structusb__cfg__descriptor.md#a717343eaf80cb0012cf87c9bc0c1c08f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bMaxPower](structusb__cfg__descriptor.md#a717343eaf80cb0012cf87c9bc0c1c08f);

176} \_\_packed;

177

[ 179](structusb__if__descriptor.md)struct [usb\_if\_descriptor](structusb__if__descriptor.md) {

[ 180](structusb__if__descriptor.md#af2e39b46da3fc3bc52cd9a4b38a3c897) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusb__if__descriptor.md#af2e39b46da3fc3bc52cd9a4b38a3c897);

[ 181](structusb__if__descriptor.md#aed00a5334643e15dca23b72ec9d0bc32) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusb__if__descriptor.md#aed00a5334643e15dca23b72ec9d0bc32);

[ 182](structusb__if__descriptor.md#af3227603f9169d7edc173318d3da298c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bInterfaceNumber](structusb__if__descriptor.md#af3227603f9169d7edc173318d3da298c);

[ 183](structusb__if__descriptor.md#a170fa703535138cdb1032b149707aae1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bAlternateSetting](structusb__if__descriptor.md#a170fa703535138cdb1032b149707aae1);

[ 184](structusb__if__descriptor.md#a9c67427276ada4d9370eba1bd50d6e3f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bNumEndpoints](structusb__if__descriptor.md#a9c67427276ada4d9370eba1bd50d6e3f);

[ 185](structusb__if__descriptor.md#acd9c54c2ff9e2b92c61b0313d6403bac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bInterfaceClass](structusb__if__descriptor.md#acd9c54c2ff9e2b92c61b0313d6403bac);

[ 186](structusb__if__descriptor.md#a3288bd3444a757496b7ec45a33d3c0c8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bInterfaceSubClass](structusb__if__descriptor.md#a3288bd3444a757496b7ec45a33d3c0c8);

[ 187](structusb__if__descriptor.md#a85e85e0adac6a61d9ed2faeb2051cf71) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bInterfaceProtocol](structusb__if__descriptor.md#a85e85e0adac6a61d9ed2faeb2051cf71);

[ 188](structusb__if__descriptor.md#ae189cb0fd93f2b7720908932aa0b983e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iInterface](structusb__if__descriptor.md#ae189cb0fd93f2b7720908932aa0b983e);

189} \_\_packed;

190

[ 191](structusb__ep__desc__bmattr.md)struct [usb\_ep\_desc\_bmattr](structusb__ep__desc__bmattr.md) {

192#ifdef CONFIG\_LITTLE\_ENDIAN

193 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transfer](structusb__ep__desc__bmattr.md#a00c87e3fc2a32a759f7627c363f533a8) : 2;

194 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [synch](structusb__ep__desc__bmattr.md#a20a1a476ad08ab95f6118627abd72375): 2;

195 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [usage](structusb__ep__desc__bmattr.md#ace1957268116f35f93fc67e7ed2f827b): 2;

196 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structusb__ep__desc__bmattr.md#aad0fafee643f870dc6b9e04b805be4c1): 2;

197#else

[ 198](structusb__ep__desc__bmattr.md#aad0fafee643f870dc6b9e04b805be4c1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structusb__ep__desc__bmattr.md#aad0fafee643f870dc6b9e04b805be4c1): 2;

[ 199](structusb__ep__desc__bmattr.md#ace1957268116f35f93fc67e7ed2f827b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [usage](structusb__ep__desc__bmattr.md#ace1957268116f35f93fc67e7ed2f827b) : 2;

[ 200](structusb__ep__desc__bmattr.md#a20a1a476ad08ab95f6118627abd72375) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [synch](structusb__ep__desc__bmattr.md#a20a1a476ad08ab95f6118627abd72375) : 2;

[ 201](structusb__ep__desc__bmattr.md#a00c87e3fc2a32a759f7627c363f533a8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transfer](structusb__ep__desc__bmattr.md#a00c87e3fc2a32a759f7627c363f533a8) : 2;

202#endif

203} \_\_packed;

204

[ 206](structusb__ep__descriptor.md)struct [usb\_ep\_descriptor](structusb__ep__descriptor.md) {

[ 207](structusb__ep__descriptor.md#ae75468872ec37d8c986534cd78fce717) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusb__ep__descriptor.md#ae75468872ec37d8c986534cd78fce717);

[ 208](structusb__ep__descriptor.md#a21412242cf380750e2623f50b5c294e6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusb__ep__descriptor.md#a21412242cf380750e2623f50b5c294e6);

[ 209](structusb__ep__descriptor.md#a60234a9d35e232957672a5bc5573d541) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bEndpointAddress](structusb__ep__descriptor.md#a60234a9d35e232957672a5bc5573d541);

210 union {

[ 211](structusb__ep__descriptor.md#ada1c690dfdee3427f303c04b5825ccca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bmAttributes](structusb__ep__descriptor.md#ada1c690dfdee3427f303c04b5825ccca);

[ 212](structusb__ep__descriptor.md#a6be879be0aac0c679c9d50bbaa9e6dda) struct [usb\_ep\_desc\_bmattr](structusb__ep__desc__bmattr.md) [Attributes](structusb__ep__descriptor.md#a6be879be0aac0c679c9d50bbaa9e6dda);

213 };

[ 214](structusb__ep__descriptor.md#a802ba531354e1d8a1c361af1d0716d82) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wMaxPacketSize](structusb__ep__descriptor.md#a802ba531354e1d8a1c361af1d0716d82);

[ 215](structusb__ep__descriptor.md#a6facefd49d301bbe357e1d420583cf1d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bInterval](structusb__ep__descriptor.md#a6facefd49d301bbe357e1d420583cf1d);

216} \_\_packed;

217

[ 219](structusb__string__descriptor.md)struct [usb\_string\_descriptor](structusb__string__descriptor.md) {

[ 220](structusb__string__descriptor.md#a93d9bb7c2c44f6f0cae1a871a4a18789) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusb__string__descriptor.md#a93d9bb7c2c44f6f0cae1a871a4a18789);

[ 221](structusb__string__descriptor.md#a37d44e07cb6d5b449b03fb70c9677b15) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusb__string__descriptor.md#a37d44e07cb6d5b449b03fb70c9677b15);

[ 222](structusb__string__descriptor.md#aefde51bb570c2bb2eb172c07d48233f1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bString](structusb__string__descriptor.md#aefde51bb570c2bb2eb172c07d48233f1);

223} \_\_packed;

224

[ 226](structusb__association__descriptor.md)struct [usb\_association\_descriptor](structusb__association__descriptor.md) {

[ 227](structusb__association__descriptor.md#a11b2d1b6a8330dcb237e433db277e487) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusb__association__descriptor.md#a11b2d1b6a8330dcb237e433db277e487);

[ 228](structusb__association__descriptor.md#ac7c1237aafde77115977bd05b1b8b0ff) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusb__association__descriptor.md#ac7c1237aafde77115977bd05b1b8b0ff);

[ 229](structusb__association__descriptor.md#aa2ad28cdb50d50627ef16d29bfba5a88) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFirstInterface](structusb__association__descriptor.md#aa2ad28cdb50d50627ef16d29bfba5a88);

[ 230](structusb__association__descriptor.md#a7d3aad4fa259c865402a41b75bff3ff9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bInterfaceCount](structusb__association__descriptor.md#a7d3aad4fa259c865402a41b75bff3ff9);

[ 231](structusb__association__descriptor.md#a1acdb21ad26400d1785a14c637a2b857) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionClass](structusb__association__descriptor.md#a1acdb21ad26400d1785a14c637a2b857);

[ 232](structusb__association__descriptor.md#a30ee67b37bfdbe56a5b58fab1d195dc9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionSubClass](structusb__association__descriptor.md#a30ee67b37bfdbe56a5b58fab1d195dc9);

[ 233](structusb__association__descriptor.md#a7205b1693998e6471ac9dbafa446a6a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFunctionProtocol](structusb__association__descriptor.md#a7205b1693998e6471ac9dbafa446a6a5);

[ 234](structusb__association__descriptor.md#a416fd6c3c27bb0453f1b2d201c9619b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iFunction](structusb__association__descriptor.md#a416fd6c3c27bb0453f1b2d201c9619b1);

235} \_\_packed;

236

[ 238](usb__ch9_8h.md#a2a8b7c42705cd1e0fd0aecb0028cb2ba)#define USB\_SCD\_RESERVED BIT(7)

[ 239](usb__ch9_8h.md#a0122c49a39e67e2443e491132aa0ecfd)#define USB\_SCD\_SELF\_POWERED BIT(6)

[ 240](usb__ch9_8h.md#aa1fa7548e67cc2755d91b68fd1545088)#define USB\_SCD\_REMOTE\_WAKEUP BIT(5)

241

[ 243](usb__ch9_8h.md#ae7de426be60abc372396692f11a0d087)#define USB\_BCC\_AUDIO 0x01

[ 244](usb__ch9_8h.md#a1d41de530a4da0ac75ff9bb875fe037e)#define USB\_BCC\_CDC\_CONTROL 0x02

[ 245](usb__ch9_8h.md#ad5904a6d6835614adc9ab914778da4a4)#define USB\_BCC\_HID 0x03

[ 246](usb__ch9_8h.md#ab0c954d8432828c1a8baa63514053cf3)#define USB\_BCC\_MASS\_STORAGE 0x08

[ 247](usb__ch9_8h.md#a83fa62678f36459d11f9cec677990d44)#define USB\_BCC\_CDC\_DATA 0x0A

[ 248](usb__ch9_8h.md#a96a42b56555daa525605e124d50ecac6)#define USB\_BCC\_VIDEO 0x0E

[ 249](usb__ch9_8h.md#a960d92dd43d279b6def9a0cca3d88dc2)#define USB\_BCC\_WIRELESS\_CONTROLLER 0xE0

[ 250](usb__ch9_8h.md#a62bf5e94c7c36c9d1d94438d7a12a482)#define USB\_BCC\_MISCELLANEOUS 0xEF

[ 251](usb__ch9_8h.md#a732af05b87cb1c53dbc7496a0da6434e)#define USB\_BCC\_APPLICATION 0xFE

[ 252](usb__ch9_8h.md#ac016944fd71362ce3924ec92cbd8f35b)#define USB\_BCC\_VENDOR 0xFF

253

[ 255](usb__ch9_8h.md#a0aadee41a18ac57c3ff4cd8af79c954c)#define USB\_SRN\_1\_1 0x0110

[ 256](usb__ch9_8h.md#a14527f51ba0e1634b3b477c80e7ae31f)#define USB\_SRN\_2\_0 0x0200

[ 257](usb__ch9_8h.md#aa39f04e0a9ad954389f19ba55ca16954)#define USB\_SRN\_2\_1 0x0210

258

[ 259](usb__ch9_8h.md#aa021c46e7c0e127c513adbac04bc77ba)#define USB\_DEC\_TO\_BCD(dec) ((((dec) / 10) << 4) | ((dec) % 10))

260

[ 262](usb__ch9_8h.md#a2f6e90e87d7a1d53418ce084a293e6fc)#define USB\_BCD\_DRN (USB\_DEC\_TO\_BCD(KERNEL\_VERSION\_MAJOR) << 8 | \

263 USB\_DEC\_TO\_BCD(KERNEL\_VERSION\_MINOR))

264

[ 266](usb__ch9_8h.md#a2916665797ca49936ed0572fb3b39a81)#define USB\_GET\_DESCRIPTOR\_TYPE(wValue) ((uint8\_t)((wValue) >> 8))

267

[ 269](usb__ch9_8h.md#a653a141a5084536362396149e81b6b9a)#define USB\_GET\_DESCRIPTOR\_INDEX(wValue) ((uint8\_t)(wValue))

270

[ 272](usb__ch9_8h.md#a8c4dd61ae766f50c9398c9753b4156b5)#define USB\_CONTROL\_EP\_MPS 64U

273

[ 275](usb__ch9_8h.md#afb744cb324e47124f93424a47d874b2a)#define USB\_EP\_DIR\_MASK (uint8\_t)BIT(7)

276

[ 278](usb__ch9_8h.md#aae8411e95f26738326bc25a0161dde99)#define USB\_EP\_DIR\_IN (uint8\_t)BIT(7)

279

[ 281](usb__ch9_8h.md#a0510b0a04d9cef144e4d9793310abccf)#define USB\_EP\_DIR\_OUT 0U

282

283/\*

284 \* REVISE: this should actually be (ep) & 0x0F, but is causes

285 \* many regressions in the current device support that are difficult

286 \* to handle.

287 \*/

[ 289](usb__ch9_8h.md#a4fd2505dba51e8f198276a032d3f0523)#define USB\_EP\_GET\_IDX(ep) ((ep) & ~USB\_EP\_DIR\_MASK)

290

[ 292](usb__ch9_8h.md#aa974862712344d5d806d521a87549284)#define USB\_EP\_GET\_DIR(ep) ((ep) & USB\_EP\_DIR\_MASK)

293

[ 295](usb__ch9_8h.md#aa5963d81b4b5bee364fb0078229c71cf)#define USB\_EP\_GET\_ADDR(idx, dir) ((idx) | ((dir) & USB\_EP\_DIR\_MASK))

296

[ 298](usb__ch9_8h.md#a495d790dfb00609ce029631f40d0a422)#define USB\_EP\_DIR\_IS\_IN(ep) (USB\_EP\_GET\_DIR(ep) == USB\_EP\_DIR\_IN)

299

[ 301](usb__ch9_8h.md#a1734aa980e0f135ddc7873bb1a60c1a1)#define USB\_EP\_DIR\_IS\_OUT(ep) (USB\_EP\_GET\_DIR(ep) == USB\_EP\_DIR\_OUT)

302

[ 304](usb__ch9_8h.md#a9af36e318a50a982ebf826ef1d9e384e)#define USB\_CONTROL\_EP\_OUT (USB\_EP\_DIR\_OUT | 0U)

305

[ 307](usb__ch9_8h.md#ad907649f48bf773b010ce8fa36639b99)#define USB\_CONTROL\_EP\_IN (USB\_EP\_DIR\_IN | 0U)

308

[ 310](usb__ch9_8h.md#a619c400cb86d083c38d59366bf18ee0c)#define USB\_EP\_TRANSFER\_TYPE\_MASK 0x3U

311

[ 313](usb__ch9_8h.md#a1cecaf205acbc73308396af4f540c012)#define USB\_EP\_TYPE\_CONTROL 0U

314

[ 316](usb__ch9_8h.md#ad128f0d04114e8a5d40a943bb58eb7d2)#define USB\_EP\_TYPE\_ISO 1U

317

[ 319](usb__ch9_8h.md#a89eb27133e7e106c3637039f6f49d187)#define USB\_EP\_TYPE\_BULK 2U

320

[ 322](usb__ch9_8h.md#a904b4eef8e7bcab363757e19832617ee)#define USB\_EP\_TYPE\_INTERRUPT 3U

323

324#ifdef \_\_cplusplus

325}

326#endif

327

328#endif /\* ZEPHYR\_INCLUDE\_USB\_CH9\_H\_ \*/

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[usb\_association\_descriptor](structusb__association__descriptor.md)

USB Association Descriptor defined in USB 3 spec.

**Definition** usb\_ch9.h:226

[usb\_association\_descriptor::bLength](structusb__association__descriptor.md#a11b2d1b6a8330dcb237e433db277e487)

uint8\_t bLength

**Definition** usb\_ch9.h:227

[usb\_association\_descriptor::bFunctionClass](structusb__association__descriptor.md#a1acdb21ad26400d1785a14c637a2b857)

uint8\_t bFunctionClass

**Definition** usb\_ch9.h:231

[usb\_association\_descriptor::bFunctionSubClass](structusb__association__descriptor.md#a30ee67b37bfdbe56a5b58fab1d195dc9)

uint8\_t bFunctionSubClass

**Definition** usb\_ch9.h:232

[usb\_association\_descriptor::iFunction](structusb__association__descriptor.md#a416fd6c3c27bb0453f1b2d201c9619b1)

uint8\_t iFunction

**Definition** usb\_ch9.h:234

[usb\_association\_descriptor::bFunctionProtocol](structusb__association__descriptor.md#a7205b1693998e6471ac9dbafa446a6a5)

uint8\_t bFunctionProtocol

**Definition** usb\_ch9.h:233

[usb\_association\_descriptor::bInterfaceCount](structusb__association__descriptor.md#a7d3aad4fa259c865402a41b75bff3ff9)

uint8\_t bInterfaceCount

**Definition** usb\_ch9.h:230

[usb\_association\_descriptor::bFirstInterface](structusb__association__descriptor.md#aa2ad28cdb50d50627ef16d29bfba5a88)

uint8\_t bFirstInterface

**Definition** usb\_ch9.h:229

[usb\_association\_descriptor::bDescriptorType](structusb__association__descriptor.md#ac7c1237aafde77115977bd05b1b8b0ff)

uint8\_t bDescriptorType

**Definition** usb\_ch9.h:228

[usb\_cfg\_descriptor](structusb__cfg__descriptor.md)

USB Standard Configuration Descriptor defined in spec.

**Definition** usb\_ch9.h:167

[usb\_cfg\_descriptor::bLength](structusb__cfg__descriptor.md#a04fb3193880a8676f686f0f2ad8adbf4)

uint8\_t bLength

**Definition** usb\_ch9.h:168

[usb\_cfg\_descriptor::bmAttributes](structusb__cfg__descriptor.md#a6cc23afd69dd7fb77f4bc5ea55315f4c)

uint8\_t bmAttributes

**Definition** usb\_ch9.h:174

[usb\_cfg\_descriptor::bMaxPower](structusb__cfg__descriptor.md#a717343eaf80cb0012cf87c9bc0c1c08f)

uint8\_t bMaxPower

**Definition** usb\_ch9.h:175

[usb\_cfg\_descriptor::bConfigurationValue](structusb__cfg__descriptor.md#a7500c52ffbb63ece0be5cde7c672615d)

uint8\_t bConfigurationValue

**Definition** usb\_ch9.h:172

[usb\_cfg\_descriptor::bDescriptorType](structusb__cfg__descriptor.md#aa89fd9e8dd2bace7709d77de1d0b2588)

uint8\_t bDescriptorType

**Definition** usb\_ch9.h:169

[usb\_cfg\_descriptor::iConfiguration](structusb__cfg__descriptor.md#ac3b8ca556e08a9b31fd0de906e000038)

uint8\_t iConfiguration

**Definition** usb\_ch9.h:173

[usb\_cfg\_descriptor::bNumInterfaces](structusb__cfg__descriptor.md#adcb6ff8c1accd4b950c9ebfd4f98718f)

uint8\_t bNumInterfaces

**Definition** usb\_ch9.h:171

[usb\_cfg\_descriptor::wTotalLength](structusb__cfg__descriptor.md#ae7f2a2fde3210e6460b20b0d17b820de)

uint16\_t wTotalLength

**Definition** usb\_ch9.h:170

[usb\_desc\_header](structusb__desc__header.md)

Header of an USB descriptor.

**Definition** usb\_ch9.h:143

[usb\_desc\_header::bDescriptorType](structusb__desc__header.md#a43ae191657b7be54357d445ff1d98950)

uint8\_t bDescriptorType

**Definition** usb\_ch9.h:145

[usb\_desc\_header::bLength](structusb__desc__header.md#a630c1fe55342f903d9a17663ef2729da)

uint8\_t bLength

**Definition** usb\_ch9.h:144

[usb\_device\_descriptor](structusb__device__descriptor.md)

USB Standard Device Descriptor defined in spec.

**Definition** usb\_ch9.h:149

[usb\_device\_descriptor::idVendor](structusb__device__descriptor.md#a043126e48bebbab536540e44428b6b4f)

uint16\_t idVendor

**Definition** usb\_ch9.h:157

[usb\_device\_descriptor::iSerialNumber](structusb__device__descriptor.md#a105d91b68091e61c9b13ea673fb98eaf)

uint8\_t iSerialNumber

**Definition** usb\_ch9.h:162

[usb\_device\_descriptor::bcdDevice](structusb__device__descriptor.md#a41416aa4a49999d2f3f0f67bdc5fa7da)

uint16\_t bcdDevice

**Definition** usb\_ch9.h:159

[usb\_device\_descriptor::bDeviceProtocol](structusb__device__descriptor.md#a56829af76e57a6ea4fc621b52a0664f8)

uint8\_t bDeviceProtocol

**Definition** usb\_ch9.h:155

[usb\_device\_descriptor::bNumConfigurations](structusb__device__descriptor.md#a603204b0517e9ece9bc0d8476b2a7cdc)

uint8\_t bNumConfigurations

**Definition** usb\_ch9.h:163

[usb\_device\_descriptor::idProduct](structusb__device__descriptor.md#a70d5ecc7bad486b8a8840d86aa151579)

uint16\_t idProduct

**Definition** usb\_ch9.h:158

[usb\_device\_descriptor::bcdUSB](structusb__device__descriptor.md#aa400edb6c3183d4922411cdaf980b84e)

uint16\_t bcdUSB

**Definition** usb\_ch9.h:152

[usb\_device\_descriptor::bDeviceClass](structusb__device__descriptor.md#aa657267e1d9762b7d2ed3eb60a78d9ad)

uint8\_t bDeviceClass

**Definition** usb\_ch9.h:153

[usb\_device\_descriptor::bMaxPacketSize0](structusb__device__descriptor.md#ac7f47eb197506ac5c555bb4f2fe82d32)

uint8\_t bMaxPacketSize0

**Definition** usb\_ch9.h:156

[usb\_device\_descriptor::iProduct](structusb__device__descriptor.md#acb90b91c59e65adbcc21949cf0f486f7)

uint8\_t iProduct

**Definition** usb\_ch9.h:161

[usb\_device\_descriptor::iManufacturer](structusb__device__descriptor.md#ad082330020575944b8471459b816cb40)

uint8\_t iManufacturer

**Definition** usb\_ch9.h:160

[usb\_device\_descriptor::bDescriptorType](structusb__device__descriptor.md#ad1ba08da6ad5b6023f1d0d1461daab7d)

uint8\_t bDescriptorType

**Definition** usb\_ch9.h:151

[usb\_device\_descriptor::bDeviceSubClass](structusb__device__descriptor.md#aecfbe730bc3eeccc9c4b5fd17f5f3c3c)

uint8\_t bDeviceSubClass

**Definition** usb\_ch9.h:154

[usb\_device\_descriptor::bLength](structusb__device__descriptor.md#af3f980ad55af3fd6c222a8802996ab63)

uint8\_t bLength

**Definition** usb\_ch9.h:150

[usb\_ep\_desc\_bmattr](structusb__ep__desc__bmattr.md)

**Definition** usb\_ch9.h:191

[usb\_ep\_desc\_bmattr::transfer](structusb__ep__desc__bmattr.md#a00c87e3fc2a32a759f7627c363f533a8)

uint8\_t transfer

**Definition** usb\_ch9.h:201

[usb\_ep\_desc\_bmattr::synch](structusb__ep__desc__bmattr.md#a20a1a476ad08ab95f6118627abd72375)

uint8\_t synch

**Definition** usb\_ch9.h:200

[usb\_ep\_desc\_bmattr::reserved](structusb__ep__desc__bmattr.md#aad0fafee643f870dc6b9e04b805be4c1)

uint8\_t reserved

**Definition** usb\_ch9.h:198

[usb\_ep\_desc\_bmattr::usage](structusb__ep__desc__bmattr.md#ace1957268116f35f93fc67e7ed2f827b)

uint8\_t usage

**Definition** usb\_ch9.h:199

[usb\_ep\_descriptor](structusb__ep__descriptor.md)

USB Standard Endpoint Descriptor defined in spec.

**Definition** usb\_ch9.h:206

[usb\_ep\_descriptor::bDescriptorType](structusb__ep__descriptor.md#a21412242cf380750e2623f50b5c294e6)

uint8\_t bDescriptorType

**Definition** usb\_ch9.h:208

[usb\_ep\_descriptor::bEndpointAddress](structusb__ep__descriptor.md#a60234a9d35e232957672a5bc5573d541)

uint8\_t bEndpointAddress

**Definition** usb\_ch9.h:209

[usb\_ep\_descriptor::Attributes](structusb__ep__descriptor.md#a6be879be0aac0c679c9d50bbaa9e6dda)

struct usb\_ep\_desc\_bmattr Attributes

**Definition** usb\_ch9.h:212

[usb\_ep\_descriptor::bInterval](structusb__ep__descriptor.md#a6facefd49d301bbe357e1d420583cf1d)

uint8\_t bInterval

**Definition** usb\_ch9.h:215

[usb\_ep\_descriptor::wMaxPacketSize](structusb__ep__descriptor.md#a802ba531354e1d8a1c361af1d0716d82)

uint16\_t wMaxPacketSize

**Definition** usb\_ch9.h:214

[usb\_ep\_descriptor::bmAttributes](structusb__ep__descriptor.md#ada1c690dfdee3427f303c04b5825ccca)

uint8\_t bmAttributes

**Definition** usb\_ch9.h:211

[usb\_ep\_descriptor::bLength](structusb__ep__descriptor.md#ae75468872ec37d8c986534cd78fce717)

uint8\_t bLength

**Definition** usb\_ch9.h:207

[usb\_if\_descriptor](structusb__if__descriptor.md)

USB Standard Interface Descriptor defined in spec.

**Definition** usb\_ch9.h:179

[usb\_if\_descriptor::bAlternateSetting](structusb__if__descriptor.md#a170fa703535138cdb1032b149707aae1)

uint8\_t bAlternateSetting

**Definition** usb\_ch9.h:183

[usb\_if\_descriptor::bInterfaceSubClass](structusb__if__descriptor.md#a3288bd3444a757496b7ec45a33d3c0c8)

uint8\_t bInterfaceSubClass

**Definition** usb\_ch9.h:186

[usb\_if\_descriptor::bInterfaceProtocol](structusb__if__descriptor.md#a85e85e0adac6a61d9ed2faeb2051cf71)

uint8\_t bInterfaceProtocol

**Definition** usb\_ch9.h:187

[usb\_if\_descriptor::bNumEndpoints](structusb__if__descriptor.md#a9c67427276ada4d9370eba1bd50d6e3f)

uint8\_t bNumEndpoints

**Definition** usb\_ch9.h:184

[usb\_if\_descriptor::bInterfaceClass](structusb__if__descriptor.md#acd9c54c2ff9e2b92c61b0313d6403bac)

uint8\_t bInterfaceClass

**Definition** usb\_ch9.h:185

[usb\_if\_descriptor::iInterface](structusb__if__descriptor.md#ae189cb0fd93f2b7720908932aa0b983e)

uint8\_t iInterface

**Definition** usb\_ch9.h:188

[usb\_if\_descriptor::bDescriptorType](structusb__if__descriptor.md#aed00a5334643e15dca23b72ec9d0bc32)

uint8\_t bDescriptorType

**Definition** usb\_ch9.h:181

[usb\_if\_descriptor::bLength](structusb__if__descriptor.md#af2e39b46da3fc3bc52cd9a4b38a3c897)

uint8\_t bLength

**Definition** usb\_ch9.h:180

[usb\_if\_descriptor::bInterfaceNumber](structusb__if__descriptor.md#af3227603f9169d7edc173318d3da298c)

uint8\_t bInterfaceNumber

**Definition** usb\_ch9.h:182

[usb\_req\_type\_field](structusb__req__type__field.md)

**Definition** usb\_ch9.h:26

[usb\_req\_type\_field::recipient](structusb__req__type__field.md#aa75b3b73833a9c8163ab9539817d1f31)

uint8\_t recipient

**Definition** usb\_ch9.h:34

[usb\_req\_type\_field::type](structusb__req__type__field.md#ab3c23439784768b6ddf71b81d58452d0)

uint8\_t type

**Definition** usb\_ch9.h:33

[usb\_req\_type\_field::direction](structusb__req__type__field.md#af312d3f2c354d2ed987a25b55b299efd)

uint8\_t direction

**Definition** usb\_ch9.h:32

[usb\_setup\_packet](structusb__setup__packet.md)

USB Setup Data packet defined in spec.

**Definition** usb\_ch9.h:39

[usb\_setup\_packet::bmRequestType](structusb__setup__packet.md#a326cfb3e8b11cc2e7cf4738d593cf10a)

uint8\_t bmRequestType

**Definition** usb\_ch9.h:41

[usb\_setup\_packet::wLength](structusb__setup__packet.md#a3421c921569bf3727534652c5f71da96)

uint16\_t wLength

**Definition** usb\_ch9.h:47

[usb\_setup\_packet::wValue](structusb__setup__packet.md#a619fbc1b9b6452f4394da713bdbc6a89)

uint16\_t wValue

**Definition** usb\_ch9.h:45

[usb\_setup\_packet::wIndex](structusb__setup__packet.md#a953c058f0e31481a3d59b404037be009)

uint16\_t wIndex

**Definition** usb\_ch9.h:46

[usb\_setup\_packet::bRequest](structusb__setup__packet.md#aab50ed2f2cdcc1d747f6f224fe9d2018)

uint8\_t bRequest

**Definition** usb\_ch9.h:44

[usb\_setup\_packet::RequestType](structusb__setup__packet.md#afa3d273ae57c3124b14ab100ac9f9a24)

struct usb\_req\_type\_field RequestType

**Definition** usb\_ch9.h:42

[usb\_string\_descriptor](structusb__string__descriptor.md)

USB Unicode (UTF16LE) String Descriptor defined in spec.

**Definition** usb\_ch9.h:219

[usb\_string\_descriptor::bDescriptorType](structusb__string__descriptor.md#a37d44e07cb6d5b449b03fb70c9677b15)

uint8\_t bDescriptorType

**Definition** usb\_ch9.h:221

[usb\_string\_descriptor::bLength](structusb__string__descriptor.md#a93d9bb7c2c44f6f0cae1a871a4a18789)

uint8\_t bLength

**Definition** usb\_ch9.h:220

[usb\_string\_descriptor::bString](structusb__string__descriptor.md#aefde51bb570c2bb2eb172c07d48233f1)

uint16\_t bString

**Definition** usb\_ch9.h:222

[USB\_REQTYPE\_DIR\_TO\_DEVICE](usb__ch9_8h.md#a3e431a6f30304833b6aa45a454c8bdbd)

#define USB\_REQTYPE\_DIR\_TO\_DEVICE

USB Setup packet RequestType Direction values (from Table 9-2).

**Definition** usb\_ch9.h:51

[usb\_reqtype\_is\_to\_device](usb__ch9_8h.md#a7542609be1ae1730be4e14d4242d9696)

static bool usb\_reqtype\_is\_to\_device(const struct usb\_setup\_packet \*setup)

Check if request transfer direction is to device.

**Definition** usb\_ch9.h:90

[usb\_reqtype\_is\_to\_host](usb__ch9_8h.md#a88dd2eb9cd06e825eb5de6a8ad38c97c)

static bool usb\_reqtype\_is\_to\_host(const struct usb\_setup\_packet \*setup)

Check if request transfer direction is to host.

**Definition** usb\_ch9.h:79

[USB\_REQTYPE\_DIR\_TO\_HOST](usb__ch9_8h.md#aa080957f00a9459f9f7c533da893b31f)

#define USB\_REQTYPE\_DIR\_TO\_HOST

**Definition** usb\_ch9.h:52

[usb\_hub.h](usb__hub_8h.md)

USB Hub Class device API header.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [usb\_ch9.h](usb__ch9_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
