---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gap_8h_source.html
original_path: doxygen/html/gap_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gap.h

[Go to the documentation of this file.](gap_8h.md)

1

4

5/\*

6 \* Copyright (c) 2019 Nordic Semiconductor ASA

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_GAP\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_GAP\_H\_

13

14#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

15#include <[zephyr/bluetooth/byteorder.h](bluetooth_2byteorder_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

27

[ 32](group__bt__gap__defines.md#ga6bbf21c05f24d2c2c710be9bcf05af5f)#define BT\_COMP\_ID\_LF 0x05f1

36

[ 41](group__bt__gap__defines.md#ga396b92d418fcb8263895e420b9df3df2)#define BT\_DATA\_FLAGS 0x01

[ 42](group__bt__gap__defines.md#ga6c725bd3d31c159a4d046561dbca38ba)#define BT\_DATA\_UUID16\_SOME 0x02

[ 43](group__bt__gap__defines.md#ga0d55063b9ad321b5c530a0012337df8a)#define BT\_DATA\_UUID16\_ALL 0x03

[ 44](group__bt__gap__defines.md#ga2486a6748490ba57e442ca15223482ef)#define BT\_DATA\_UUID32\_SOME 0x04

[ 45](group__bt__gap__defines.md#gaaf825c3e4686e572a35ddd46ee6fe2e8)#define BT\_DATA\_UUID32\_ALL 0x05

[ 46](group__bt__gap__defines.md#ga5c4f7fc1b93c611e95f735330fba243b)#define BT\_DATA\_UUID128\_SOME 0x06

[ 47](group__bt__gap__defines.md#gaafcade3dbbcb4005f4590e994f91884b)#define BT\_DATA\_UUID128\_ALL 0x07

[ 48](group__bt__gap__defines.md#gafc509b33a8d2dd9124f6893eadbe1662)#define BT\_DATA\_NAME\_SHORTENED 0x08

[ 49](group__bt__gap__defines.md#gab94a7c5689d296acf47f976538056ab5)#define BT\_DATA\_NAME\_COMPLETE 0x09

[ 50](group__bt__gap__defines.md#ga4988c17578c4cf76fcdd9d44e1c931b0)#define BT\_DATA\_TX\_POWER 0x0a

[ 51](group__bt__gap__defines.md#ga5014acb2fe8e76b855b55bf98abe6d05)#define BT\_DATA\_SM\_TK\_VALUE 0x10

[ 52](group__bt__gap__defines.md#gaa12c742d1c955036aa3f55e84df69890)#define BT\_DATA\_SM\_OOB\_FLAGS 0x11

[ 53](group__bt__gap__defines.md#gabcf872eafc60c21287f6be63174dc7c8)#define BT\_DATA\_PERIPHERAL\_INT\_RANGE 0x12

[ 54](group__bt__gap__defines.md#ga2ad4d2ec2ff29c0aad5159de12d3f741)#define BT\_DATA\_SOLICIT16 0x14

[ 55](group__bt__gap__defines.md#ga217df3f70846e86fa09e5605d5acd291)#define BT\_DATA\_SOLICIT128 0x15

[ 56](group__bt__gap__defines.md#ga76990dda919688b369decaf9d3606b32)#define BT\_DATA\_SVC\_DATA16 0x16

[ 57](group__bt__gap__defines.md#gacb867f0436d38c5c80e3426ca6247a46)#define BT\_DATA\_PUB\_TARGET\_ADDR 0x17

[ 58](group__bt__gap__defines.md#ga3d9097d8f53213ccafc152c51ad6fdbd)#define BT\_DATA\_RAND\_TARGET\_ADDR 0x18

[ 59](group__bt__gap__defines.md#ga67fc721da05758b7d7a36aecaa035fac)#define BT\_DATA\_GAP\_APPEARANCE 0x19

[ 60](group__bt__gap__defines.md#ga6fd8c0f32bbcb97aaafee51fda0b601e)#define BT\_DATA\_ADV\_INT 0x1a

[ 61](group__bt__gap__defines.md#gad9e8a273239fa160a6b2797ef5563a94)#define BT\_DATA\_LE\_BT\_DEVICE\_ADDRESS 0x1b

[ 62](group__bt__gap__defines.md#ga255c7cb16eb24b95fa0f531fc4574273)#define BT\_DATA\_LE\_ROLE 0x1c

[ 63](group__bt__gap__defines.md#ga324f91521eacd1e9d579c9d52d02eb06)#define BT\_DATA\_SIMPLE\_PAIRING\_HASH 0x1d

[ 64](group__bt__gap__defines.md#gad7e7dd2d3a972e53f9e5e80627bd07e6)#define BT\_DATA\_SIMPLE\_PAIRING\_RAND 0x1e

[ 65](group__bt__gap__defines.md#ga76e7e8971ed841b87fda08793a00b14f)#define BT\_DATA\_SOLICIT32 0x1f

[ 66](group__bt__gap__defines.md#ga7d411a723ff2f038c3b7a1e09c88cb3d)#define BT\_DATA\_SVC\_DATA32 0x20

[ 67](group__bt__gap__defines.md#gaa53847910515d9488b490f17a4fdf0d1)#define BT\_DATA\_SVC\_DATA128 0x21

[ 68](group__bt__gap__defines.md#ga883dda02c157f0de8157b1c5f66aafd0)#define BT\_DATA\_LE\_SC\_CONFIRM\_VALUE 0x22

[ 69](group__bt__gap__defines.md#gacbc31c67684e3c68481501cf89f9ec68)#define BT\_DATA\_LE\_SC\_RANDOM\_VALUE 0x23

[ 70](group__bt__gap__defines.md#ga3c6a5903cc4a46aaf0b30a0de0179403)#define BT\_DATA\_URI 0x24

[ 71](group__bt__gap__defines.md#ga0f29f9d8f5a336af430f0a603e87e995)#define BT\_DATA\_INDOOR\_POS 0x25

[ 72](group__bt__gap__defines.md#ga8e9ccc669ee545152b2d9b3120692d55)#define BT\_DATA\_TRANS\_DISCOVER\_DATA 0x26

[ 73](group__bt__gap__defines.md#ga207bc1e5405a4fd3f39863a2cb304ebc)#define BT\_DATA\_LE\_SUPPORTED\_FEATURES 0x27

[ 74](group__bt__gap__defines.md#gae3eb96c0f127b6417d7cad288faaaceb)#define BT\_DATA\_CHANNEL\_MAP\_UPDATE\_IND 0x28

[ 75](group__bt__gap__defines.md#gafc5984d58b0b54ee824dd83bc78dfbe9)#define BT\_DATA\_MESH\_PROV 0x29

[ 76](group__bt__gap__defines.md#gac351c67ab58520b796fa713602d9f602)#define BT\_DATA\_MESH\_MESSAGE 0x2a

[ 77](group__bt__gap__defines.md#ga59cc479be1f6c61a4a47aa6f479fe67a)#define BT\_DATA\_MESH\_BEACON 0x2b

[ 78](group__bt__gap__defines.md#ga16feb94cd09c04d020450f61646f5486)#define BT\_DATA\_BIG\_INFO 0x2c

[ 79](group__bt__gap__defines.md#ga72d2e55819db593a6db77579ebfe1e9d)#define BT\_DATA\_BROADCAST\_CODE 0x2d

[ 80](group__bt__gap__defines.md#ga122da4184d606ae140f8a311aaebeedd)#define BT\_DATA\_CSIS\_RSI 0x2e

[ 81](group__bt__gap__defines.md#gad4ac2e0de80dddcacc4ca6d25765eebd)#define BT\_DATA\_ADV\_INT\_LONG 0x2f

[ 82](group__bt__gap__defines.md#ga7d781791bc85fe3c7ea839ff617ee6e7)#define BT\_DATA\_BROADCAST\_NAME 0x30

[ 83](group__bt__gap__defines.md#ga41d5c898144e89b6035f92ff506f38a3)#define BT\_DATA\_ENCRYPTED\_AD\_DATA 0x31

[ 84](group__bt__gap__defines.md#gaecab0c77f9f912c16c264e7eaf2e4707)#define BT\_DATA\_3D\_INFO 0x3D

85

[ 86](group__bt__gap__defines.md#ga63b846807bff632b1cdd49b1e46e63b4)#define BT\_DATA\_MANUFACTURER\_DATA 0xff

87

[ 88](group__bt__gap__defines.md#ga36191ee000a2098fd679c398b31e0906)#define BT\_LE\_AD\_LIMITED 0x01

[ 89](group__bt__gap__defines.md#ga13d9b4a24e2a8b58402bfb21f8b782c8)#define BT\_LE\_AD\_GENERAL 0x02

[ 90](group__bt__gap__defines.md#gabf5725f481cb73cbd974f3653c904bc9)#define BT\_LE\_AD\_NO\_BREDR 0x04

94

[ 102](group__bt__gap__defines.md#gafd1c9ca638a362a01897792e5a00a0c5)#define BT\_APPEARANCE\_UNKNOWN 0x0000

[ 104](group__bt__gap__defines.md#gae7061e78f960563af6e1b3dea71655a9)#define BT\_APPEARANCE\_GENERIC\_PHONE 0x0040

[ 106](group__bt__gap__defines.md#ga6b74ad86efc0e9a745f2c9e64079b1cd)#define BT\_APPEARANCE\_GENERIC\_COMPUTER 0x0080

[ 108](group__bt__gap__defines.md#ga1aa0565ca7e00e3a1aa8968e0a7f1bef)#define BT\_APPEARANCE\_COMPUTER\_DESKTOP\_WORKSTATION 0x0081

[ 110](group__bt__gap__defines.md#gab71a3c3f836561ac7bd8e52f5e01c769)#define BT\_APPEARANCE\_COMPUTER\_SERVER\_CLASS 0x0082

[ 112](group__bt__gap__defines.md#ga55ce2ad96a153ed6bdfd841276145c28)#define BT\_APPEARANCE\_COMPUTER\_LAPTOP 0x0083

[ 114](group__bt__gap__defines.md#gab64312ea16f03c5998db4429b194b8b0)#define BT\_APPEARANCE\_COMPUTER\_HANDHELD\_PCPDA 0x0084

[ 116](group__bt__gap__defines.md#ga9340ed60911fc7c5aab7d317b6925c10)#define BT\_APPEARANCE\_COMPUTER\_PALMSIZE\_PCPDA 0x0085

[ 118](group__bt__gap__defines.md#ga7c6667ba4c68dec380a548ba9530c110)#define BT\_APPEARANCE\_COMPUTER\_WEARABLE\_COMPUTER 0x0086

[ 120](group__bt__gap__defines.md#ga11bc881cb5f88956edbf2bb2fe5b358c)#define BT\_APPEARANCE\_COMPUTER\_TABLET 0x0087

[ 122](group__bt__gap__defines.md#ga36187d2651d08c4b3e17c36565a2d3c9)#define BT\_APPEARANCE\_COMPUTER\_DOCKING\_STATION 0x0088

[ 124](group__bt__gap__defines.md#gaa4d962ad8661c28ed48f5cf8cd75ad6e)#define BT\_APPEARANCE\_COMPUTER\_ALL\_IN\_ONE 0x0089

[ 126](group__bt__gap__defines.md#ga53e8eff26f2020b1fc89b21684e54698)#define BT\_APPEARANCE\_COMPUTER\_BLADE\_SERVER 0x008A

[ 128](group__bt__gap__defines.md#ga073dca362cabfd2a07cdc1cb787a0f58)#define BT\_APPEARANCE\_COMPUTER\_CONVERTIBLE 0x008B

[ 130](group__bt__gap__defines.md#ga8f35f76cc9de4170006669d6e9e7d72a)#define BT\_APPEARANCE\_COMPUTER\_DETACHABLE 0x008C

[ 132](group__bt__gap__defines.md#ga6ae353795476853bc3be2196ed220aa7)#define BT\_APPEARANCE\_COMPUTER\_IOT\_GATEWAY 0x008D

[ 134](group__bt__gap__defines.md#ga3c47c11f56eabec15e960662c64f6fcb)#define BT\_APPEARANCE\_COMPUTER\_MINI\_PC 0x008E

[ 136](group__bt__gap__defines.md#gabb53daf3eb4ac9ba0cbb1614056ee214)#define BT\_APPEARANCE\_COMPUTER\_STICK\_PC 0x008F

[ 138](group__bt__gap__defines.md#ga0c512fd6aa5d35e78f02176073f5f121)#define BT\_APPEARANCE\_GENERIC\_WATCH 0x00C0

[ 140](group__bt__gap__defines.md#gaca9cc93d768145ec3d87b88740954b50)#define BT\_APPEARANCE\_SPORTS\_WATCH 0x00C1

[ 142](group__bt__gap__defines.md#gaa5662d4a544b034243faa45245a9728b)#define BT\_APPEARANCE\_SMARTWATCH 0x00C2

[ 144](group__bt__gap__defines.md#ga100d26d6b9e9a3af925d64c0b006c6bd)#define BT\_APPEARANCE\_GENERIC\_CLOCK 0x0100

[ 146](group__bt__gap__defines.md#ga0a21cb58861a48875002af38ee82ac08)#define BT\_APPEARANCE\_GENERIC\_DISPLAY 0x0140

[ 148](group__bt__gap__defines.md#ga0b47897768b27d26b8687dd2ab28703b)#define BT\_APPEARANCE\_GENERIC\_REMOTE 0x0180

[ 150](group__bt__gap__defines.md#gab2b5f6385662519a2ece8fb654a6194b)#define BT\_APPEARANCE\_GENERIC\_EYEGLASSES 0x01C0

[ 152](group__bt__gap__defines.md#gaca6d810977e6da1a3174ee2b6b36662d)#define BT\_APPEARANCE\_GENERIC\_TAG 0x0200

[ 154](group__bt__gap__defines.md#gaf73b11c4dbf366a854b4c68e802e3c1c)#define BT\_APPEARANCE\_GENERIC\_KEYRING 0x0240

[ 156](group__bt__gap__defines.md#ga17e94209c0c96b5ca039b1613de0d05e)#define BT\_APPEARANCE\_GENERIC\_MEDIA\_PLAYER 0x0280

[ 158](group__bt__gap__defines.md#gadca19a01611ca83e18156bb540dd96c1)#define BT\_APPEARANCE\_GENERIC\_BARCODE\_SCANNER 0x02C0

[ 160](group__bt__gap__defines.md#ga2e0fde88d83e1f4533d69c8dc472255f)#define BT\_APPEARANCE\_GENERIC\_THERMOMETER 0x0300

[ 162](group__bt__gap__defines.md#ga54283061a207491dcfced899c0fc3008)#define BT\_APPEARANCE\_THERMOMETER\_EAR 0x0301

[ 164](group__bt__gap__defines.md#gac5bdf195b81215932848151d765e84d6)#define BT\_APPEARANCE\_GENERIC\_HEART\_RATE 0x0340

[ 166](group__bt__gap__defines.md#ga895f6570a09f3eee8d821eca57cdeb03)#define BT\_APPEARANCE\_HEART\_RATE\_BELT 0x0341

[ 168](group__bt__gap__defines.md#ga3ab7a9595e00208a9e6a56dca99b56c2)#define BT\_APPEARANCE\_GENERIC\_BLOOD\_PRESSURE 0x0380

[ 170](group__bt__gap__defines.md#ga55c3e67d27c8fd8ae06880ccdd9259ce)#define BT\_APPEARANCE\_BLOOD\_PRESSURE\_ARM 0x0381

[ 172](group__bt__gap__defines.md#ga89684ca0544a400293b663cdf0063cfa)#define BT\_APPEARANCE\_BLOOD\_PRESSURE\_WRIST 0x0382

[ 174](group__bt__gap__defines.md#gaf2050baedf0863ec37177dd2ef872d39)#define BT\_APPEARANCE\_GENERIC\_HID 0x03C0

[ 176](group__bt__gap__defines.md#gaa74af272423a80d5489ed8cf6c3ee66c)#define BT\_APPEARANCE\_HID\_KEYBOARD 0x03C1

[ 178](group__bt__gap__defines.md#ga3b6ba8ffe424db08583186c448e37149)#define BT\_APPEARANCE\_HID\_MOUSE 0x03C2

[ 180](group__bt__gap__defines.md#ga2f9f15df2260a1307f5142f37437bf0c)#define BT\_APPEARANCE\_HID\_JOYSTICK 0x03C3

[ 182](group__bt__gap__defines.md#ga770336524e74d106cb18354f9dbfad76)#define BT\_APPEARANCE\_HID\_GAMEPAD 0x03C4

[ 184](group__bt__gap__defines.md#gacac11dcb96ab60963a1118e171a731de)#define BT\_APPEARANCE\_HID\_DIGITIZER\_TABLET 0x03C5

[ 186](group__bt__gap__defines.md#gaa03c3b4d7ea8211748316146afab8bd4)#define BT\_APPEARANCE\_HID\_CARD\_READER 0x03C6

[ 188](group__bt__gap__defines.md#ga002a1d7965b23ec62c8a196f4e5452d9)#define BT\_APPEARANCE\_HID\_DIGITAL\_PEN 0x03C7

[ 190](group__bt__gap__defines.md#gaf88f83afd454fe88dd7146e10ef6d35e)#define BT\_APPEARANCE\_HID\_BARCODE\_SCANNER 0x03C8

[ 192](group__bt__gap__defines.md#gaee207f9434bce7d0f7e096bf3b37a01c)#define BT\_APPEARANCE\_HID\_TOUCHPAD 0x03C9

[ 194](group__bt__gap__defines.md#gae415dd9e8d620dfd1981719f4ed2d796)#define BT\_APPEARANCE\_HID\_PRESENTATION\_REMOTE 0x03CA

[ 196](group__bt__gap__defines.md#ga209645f7445873beb50c388cc82aff2a)#define BT\_APPEARANCE\_GENERIC\_GLUCOSE 0x0400

[ 198](group__bt__gap__defines.md#ga9cf19d97db0c4c5b8473b72809b51d42)#define BT\_APPEARANCE\_GENERIC\_WALKING 0x0440

[ 200](group__bt__gap__defines.md#gad748f5dc2e0622353d6159c3a3e4241b)#define BT\_APPEARANCE\_WALKING\_IN\_SHOE 0x0441

[ 202](group__bt__gap__defines.md#ga0a4541459ba8b41a3938c5b8d35b1c8c)#define BT\_APPEARANCE\_WALKING\_ON\_SHOE 0x0442

[ 204](group__bt__gap__defines.md#gad211a7e2f11dc7effe3ba28e8c4f7092)#define BT\_APPEARANCE\_WALKING\_ON\_HIP 0x0443

[ 206](group__bt__gap__defines.md#ga7a0463b9b0df37bce80cada38b10ee54)#define BT\_APPEARANCE\_GENERIC\_CYCLING 0x0480

[ 208](group__bt__gap__defines.md#ga3e81dce23c3d005a9b48ff83c7b8f896)#define BT\_APPEARANCE\_CYCLING\_COMPUTER 0x0481

[ 210](group__bt__gap__defines.md#ga16fb08fa70272252ab6b2d3a5aec485a)#define BT\_APPEARANCE\_CYCLING\_SPEED 0x0482

[ 212](group__bt__gap__defines.md#ga71dc370aad015e88fce7c3e758c647ed)#define BT\_APPEARANCE\_CYCLING\_CADENCE 0x0483

[ 214](group__bt__gap__defines.md#ga02fd9566d9b932aeaa1163d312fbc4d8)#define BT\_APPEARANCE\_CYCLING\_POWER 0x0484

[ 216](group__bt__gap__defines.md#ga48d8f2a285795785f8f51ce220d46371)#define BT\_APPEARANCE\_CYCLING\_SPEED\_CADENCE 0x0485

[ 218](group__bt__gap__defines.md#ga5e16df5eefcae8556dfc387135e2b1b6)#define BT\_APPEARANCE\_GENERIC\_CONTROL\_DEVICE 0x04C0

[ 220](group__bt__gap__defines.md#gac53247d00e3da69595274e0b94fa670f)#define BT\_APPEARANCE\_CONTROL\_SWITCH 0x04C1

[ 222](group__bt__gap__defines.md#gad30c40df58e160128893e545a11ab44c)#define BT\_APPEARANCE\_CONTROL\_MULTI\_SWITCH 0x04C2

[ 224](group__bt__gap__defines.md#ga52dfd2858663b7ab624f0c4b08cee7dc)#define BT\_APPEARANCE\_CONTROL\_BUTTON 0x04C3

[ 226](group__bt__gap__defines.md#gaa849d890c000defcaf29893296c86cc5)#define BT\_APPEARANCE\_CONTROL\_SLIDER 0x04C4

[ 228](group__bt__gap__defines.md#ga946b6a8bb49bf0b5cd3ded93ee8dfe89)#define BT\_APPEARANCE\_CONTROL\_ROTARY\_SWITCH 0x04C5

[ 230](group__bt__gap__defines.md#ga4d5763288557e7b7f6da0f3e9831171d)#define BT\_APPEARANCE\_CONTROL\_TOUCH\_PANEL 0x04C6

[ 232](group__bt__gap__defines.md#ga979ca0f4febeaa55daec07e2b3b0179e)#define BT\_APPEARANCE\_CONTROL\_SINGLE\_SWITCH 0x04C7

[ 234](group__bt__gap__defines.md#gac1c80dbb8aaa327b6125bf632692c3be)#define BT\_APPEARANCE\_CONTROL\_DOUBLE\_SWITCH 0x04C8

[ 236](group__bt__gap__defines.md#gaa532fd1bd67c2c5b72822704a62df143)#define BT\_APPEARANCE\_CONTROL\_TRIPLE\_SWITCH 0x04C9

[ 238](group__bt__gap__defines.md#gaea669671a53b3df5b1aa4c43e5bde9b9)#define BT\_APPEARANCE\_CONTROL\_BATTERY\_SWITCH 0x04CA

[ 240](group__bt__gap__defines.md#gadec2907a822e302d5027f162ef9ce4b6)#define BT\_APPEARANCE\_CONTROL\_ENERGY\_HARVESTING\_SWITCH 0x04CB

[ 242](group__bt__gap__defines.md#ga9bb358864e1388cc00502b5586ec581f)#define BT\_APPEARANCE\_CONTROL\_PUSH\_BUTTON 0x04CC

[ 244](group__bt__gap__defines.md#gac4727ec720344ece687256ac517800e7)#define BT\_APPEARANCE\_GENERIC\_NETWORK\_DEVICE 0x0500

[ 246](group__bt__gap__defines.md#ga265ba959769d56f42ff621a20e193aba)#define BT\_APPEARANCE\_NETWORK\_ACCESS\_POINT 0x0501

[ 248](group__bt__gap__defines.md#gadcc3d795579a731ae03ade14d5193408)#define BT\_APPEARANCE\_NETWORK\_MESH\_DEVICE 0x0502

[ 250](group__bt__gap__defines.md#gad4c5f5840a8caba73d55b0138e506bd0)#define BT\_APPEARANCE\_NETWORK\_MESH\_PROXY 0x0503

[ 252](group__bt__gap__defines.md#gab3241fe012482e716c3f18e2962ca15d)#define BT\_APPEARANCE\_GENERIC\_SENSOR 0x0540

[ 254](group__bt__gap__defines.md#gab49b84183136e9b65ba2e1f5490a79ed)#define BT\_APPEARANCE\_SENSOR\_MOTION 0x0541

[ 256](group__bt__gap__defines.md#gaacb0779499ad4aaa83f0b6303460caf8)#define BT\_APPEARANCE\_SENSOR\_AIR\_QUALITY 0x0542

[ 258](group__bt__gap__defines.md#ga5e072a902bf145dc2b00dbd1c8a64b52)#define BT\_APPEARANCE\_SENSOR\_TEMPERATURE 0x0543

[ 260](group__bt__gap__defines.md#ga2deff206602e1e0784af9456ef8abd5b)#define BT\_APPEARANCE\_SENSOR\_HUMIDITY 0x0544

[ 262](group__bt__gap__defines.md#ga2cbac5e931080f1f5cb3c9bb4c73e9d8)#define BT\_APPEARANCE\_SENSOR\_LEAK 0x0545

[ 264](group__bt__gap__defines.md#gaeedc0612f8ca171aec061cf02ee907e4)#define BT\_APPEARANCE\_SENSOR\_SMOKE 0x0546

[ 266](group__bt__gap__defines.md#ga8e8b7834c82c42a0076300aca20c2d35)#define BT\_APPEARANCE\_SENSOR\_OCCUPANCY 0x0547

[ 268](group__bt__gap__defines.md#gac71e281cf1b8d1b6535623ec34c7d63f)#define BT\_APPEARANCE\_SENSOR\_CONTACT 0x0548

[ 270](group__bt__gap__defines.md#ga0e60b365f871c17c0015ffcf8bc1646e)#define BT\_APPEARANCE\_SENSOR\_CARBON\_MONOXIDE 0x0549

[ 272](group__bt__gap__defines.md#ga34ed8c9aefe34d5030209f073c9ecd24)#define BT\_APPEARANCE\_SENSOR\_CARBON\_DIOXIDE 0x054A

[ 274](group__bt__gap__defines.md#ga622508f9b051ed0320700b01967f6446)#define BT\_APPEARANCE\_SENSOR\_AMBIENT\_LIGHT 0x054B

[ 276](group__bt__gap__defines.md#gaca0cfcd560fa4133c0bc62a61d2874c7)#define BT\_APPEARANCE\_SENSOR\_ENERGY 0x054C

[ 278](group__bt__gap__defines.md#ga8106142ddb6445e7462137e032e50854)#define BT\_APPEARANCE\_SENSOR\_COLOR\_LIGHT 0x054D

[ 280](group__bt__gap__defines.md#ga380da83e3a69de3fd5091cdc89f7fcbc)#define BT\_APPEARANCE\_SENSOR\_RAIN 0x054E

[ 282](group__bt__gap__defines.md#ga425115e6c251a9c493c98d79f659077d)#define BT\_APPEARANCE\_SENSOR\_FIRE 0x054F

[ 284](group__bt__gap__defines.md#gaa710c0666d8b5bf1e1230672cbbf55fa)#define BT\_APPEARANCE\_SENSOR\_WIND 0x0550

[ 286](group__bt__gap__defines.md#ga6d3447e24d5d75051b81998fd9ad8bfe)#define BT\_APPEARANCE\_SENSOR\_PROXIMITY 0x0551

[ 288](group__bt__gap__defines.md#gaeec9666dbdb31e9302a25aaa536f3180)#define BT\_APPEARANCE\_SENSOR\_MULTI 0x0552

[ 290](group__bt__gap__defines.md#gaf9a9c0191ec175d14061058cf3da163c)#define BT\_APPEARANCE\_SENSOR\_FLUSH\_MOUNTED 0x0553

[ 292](group__bt__gap__defines.md#gadfb6808db5a7060316b724c24c8ceaf8)#define BT\_APPEARANCE\_SENSOR\_CEILING\_MOUNTED 0x0554

[ 294](group__bt__gap__defines.md#gae564900f0517d393ceffcca8d27f6e45)#define BT\_APPEARANCE\_SENSOR\_WALL\_MOUNTED 0x0555

[ 296](group__bt__gap__defines.md#ga90237753920702380321e9f858344741)#define BT\_APPEARANCE\_MULTISENSOR 0x0556

[ 298](group__bt__gap__defines.md#ga7238d3a45f9e62f0189db9d7eeac4d15)#define BT\_APPEARANCE\_SENSOR\_ENERGY\_METER 0x0557

[ 300](group__bt__gap__defines.md#gaae8f95ef639cb7d5e97063eed710a07d)#define BT\_APPEARANCE\_SENSOR\_FLAME\_DETECTOR 0x0558

[ 302](group__bt__gap__defines.md#ga4d0877a3cd9b7efebbaa5fd8a988a2a3)#define BT\_APPEARANCE\_SENSOR\_VEHICLE\_TIRE\_PRESSURE 0x0559

[ 304](group__bt__gap__defines.md#gae01be867f730c06b59fcb03289ae66d7)#define BT\_APPEARANCE\_GENERIC\_LIGHT\_FIXTURES 0x0580

[ 306](group__bt__gap__defines.md#gae1b2b535754f9cdc24c4a6cee63ef5cb)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_WALL 0x0581

[ 308](group__bt__gap__defines.md#ga2d77fb5f5ed9a43771186ecc5693da8f)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_CEILING 0x0582

[ 310](group__bt__gap__defines.md#ga57bb461b0ddd045d21d7fbd3843fbabb)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_FLOOR 0x0583

[ 312](group__bt__gap__defines.md#gadc48840b6590a89593a5d17fbdb1e9e9)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_CABINET 0x0584

[ 314](group__bt__gap__defines.md#ga2f37bf95ea6057b999bbf2cf94016e5d)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_DESK 0x0585

[ 316](group__bt__gap__defines.md#gaa57b538ecad380ad77354e0cd9576e5b)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_TROFFER 0x0586

[ 318](group__bt__gap__defines.md#ga336147b54406237e25d8cf9ed152928b)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_PENDANT 0x0587

[ 320](group__bt__gap__defines.md#ga583b7432ba6ac4cc078d3a069e3a54e1)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_IN\_GROUND 0x0588

[ 322](group__bt__gap__defines.md#gab41f8b6f1ff0f624bb6666ef2ac6dab3)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_FLOOD 0x0589

[ 324](group__bt__gap__defines.md#ga83f50305a23250e5e2cef5004762e122)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_UNDERWATER 0x058A

[ 326](group__bt__gap__defines.md#ga20a7b241f292475d70626a38d983886c)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_BOLLARD\_WITH 0x058B

[ 328](group__bt__gap__defines.md#ga7c5811bd50d9f78e67e3e56faa432aae)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_PATHWAY 0x058C

[ 330](group__bt__gap__defines.md#ga348e64ffe0f3d6301dd8c911f70ead68)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_GARDEN 0x058D

[ 332](group__bt__gap__defines.md#ga0da0cbeebd2b20bf28dfc06def016068)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_POLE\_TOP 0x058E

[ 334](group__bt__gap__defines.md#ga58e1989c99b5a223a318a716d62f6e2b)#define BT\_APPEARANCE\_SPOT\_LIGHT 0x058F

[ 336](group__bt__gap__defines.md#ga5388daf123e629d6f7a0b9af13fbc366)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_LINEAR 0x0590

[ 338](group__bt__gap__defines.md#gac938fb03553d2d3c27b50af2a9a1ac48)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_STREET 0x0591

[ 340](group__bt__gap__defines.md#ga1bf2889f7a8a7ae363bc1d4355ee8d65)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_SHELVES 0x0592

[ 342](group__bt__gap__defines.md#ga8f98c2d32664a6e03ebc2a43ae1eb52a)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_BAY 0x0593

[ 344](group__bt__gap__defines.md#ga3f687f994ffff2ce70b81a992195d210)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_EMERGENCY\_EXIT 0x0594

[ 346](group__bt__gap__defines.md#ga35a90a4e3bfef7b0cfec0d5fa7b36c4a)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_CONTROLLER 0x0595

[ 348](group__bt__gap__defines.md#gac2b6de99b4e87f7c40063ba844c75ead)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_DRIVER 0x0596

[ 350](group__bt__gap__defines.md#ga8325830f2c977dc238a9ca1b9837803e)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_BULB 0x0597

[ 352](group__bt__gap__defines.md#gafc924bbc1b6aff0130c2be3d5fe59e33)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_LOW\_BAY 0x0598

[ 354](group__bt__gap__defines.md#ga738e87008c6a64450bb7ec22dbcdd113)#define BT\_APPEARANCE\_LIGHT\_FIXTURES\_HIGH\_BAY 0x0599

[ 356](group__bt__gap__defines.md#ga82cc89321c4f4ffbf3ef25eff624943c)#define BT\_APPEARANCE\_GENERIC\_FAN 0x05C0

[ 358](group__bt__gap__defines.md#ga8cd83cd08846ac276cc65f31333ee62e)#define BT\_APPEARANCE\_FAN\_CEILING 0x05C1

[ 360](group__bt__gap__defines.md#ga32dd73ffa211d632617018aa510b89c4)#define BT\_APPEARANCE\_FAN\_AXIAL 0x05C2

[ 362](group__bt__gap__defines.md#ga1e842c97b90678908f4d18c86c1227c2)#define BT\_APPEARANCE\_FAN\_EXHAUST 0x05C3

[ 364](group__bt__gap__defines.md#ga2e54f8de862435f2dbd7f56b98615c84)#define BT\_APPEARANCE\_FAN\_PEDESTAL 0x05C4

[ 366](group__bt__gap__defines.md#gaa9e17b8b5e06d2fb365bf152e0cbef5d)#define BT\_APPEARANCE\_FAN\_DESK 0x05C5

[ 368](group__bt__gap__defines.md#ga498be79799cb778c9df6629411fe32ad)#define BT\_APPEARANCE\_FAN\_WALL 0x05C6

[ 370](group__bt__gap__defines.md#gaf1f01946f6acadcaf719d3d7cc06e55f)#define BT\_APPEARANCE\_GENERIC\_HVAC 0x0600

[ 372](group__bt__gap__defines.md#ga33055b50c10bfc713b18823fca525488)#define BT\_APPEARANCE\_HVAC\_THERMOSTAT 0x0601

[ 374](group__bt__gap__defines.md#gaf55f3f3f07cc78509e7fe19cea6cea4e)#define BT\_APPEARANCE\_HVAC\_HUMIDIFIER 0x0602

[ 376](group__bt__gap__defines.md#gaa3b96e44638048b8891a2dece29f4b3f)#define BT\_APPEARANCE\_HVAC\_DEHUMIDIFIER 0x0603

[ 378](group__bt__gap__defines.md#gacef9145f435d10cbf5a775b9a2c9b756)#define BT\_APPEARANCE\_HVAC\_HEATER 0x0604

[ 380](group__bt__gap__defines.md#gad90f108f3d33d68e27ac545cdb520f18)#define BT\_APPEARANCE\_HVAC\_RADIATOR 0x0605

[ 382](group__bt__gap__defines.md#gacc28a1bc1a809c574019455de4ac9d0b)#define BT\_APPEARANCE\_HVAC\_BOILER 0x0606

[ 384](group__bt__gap__defines.md#gaead4ebeabb8855111ab9080aca4e035a)#define BT\_APPEARANCE\_HVAC\_HEAT\_PUMP 0x0607

[ 386](group__bt__gap__defines.md#ga50c5df52d8471fc8e1dc65e31079566d)#define BT\_APPEARANCE\_HVAC\_INFRARED\_HEATER 0x0608

[ 388](group__bt__gap__defines.md#gad43d27ff96a7fba1ed7d5e20ebd472d9)#define BT\_APPEARANCE\_HVAC\_RADIANT\_PANEL\_HEATER 0x0609

[ 390](group__bt__gap__defines.md#ga2a044c3369ed48d216707f6e6a541a23)#define BT\_APPEARANCE\_HVAC\_FAN\_HEATER 0x060A

[ 392](group__bt__gap__defines.md#ga182ade4b2c8f4705ba132248e504bb95)#define BT\_APPEARANCE\_HVAC\_AIR\_CURTAIN 0x060B

[ 394](group__bt__gap__defines.md#gaa13ae6496d47df2be0a0692a28806007)#define BT\_APPEARANCE\_GENERIC\_AIR\_CONDITIONING 0x0640

[ 396](group__bt__gap__defines.md#ga0b552243744bc598467421555e935cd0)#define BT\_APPEARANCE\_GENERIC\_HUMIDIFIER 0x0680

[ 398](group__bt__gap__defines.md#ga8ea92ea92ca4e2bad4e5e2baba1271dd)#define BT\_APPEARANCE\_GENERIC\_HEATING 0x06C0

[ 400](group__bt__gap__defines.md#ga05b0b91c74aed5bc73a92f336bdae33a)#define BT\_APPEARANCE\_HEATING\_RADIATOR 0x06C1

[ 402](group__bt__gap__defines.md#gac1abc9ae0b8ede2197720ea9e67b692e)#define BT\_APPEARANCE\_HEATING\_BOILER 0x06C2

[ 404](group__bt__gap__defines.md#ga99537968fdc7e680d922ca309fba7678)#define BT\_APPEARANCE\_HEATING\_HEAT\_PUMP 0x06C3

[ 406](group__bt__gap__defines.md#ga8e40496a351c7ec5ea836805925f1e13)#define BT\_APPEARANCE\_HEATING\_INFRARED\_HEATER 0x06C4

[ 408](group__bt__gap__defines.md#ga46fe051c7e50492dba5ae824e154cf69)#define BT\_APPEARANCE\_HEATING\_RADIANT\_PANEL\_HEATER 0x06C5

[ 410](group__bt__gap__defines.md#ga995ca18db114ea062df0d76c9e241937)#define BT\_APPEARANCE\_HEATING\_FAN\_HEATER 0x06C6

[ 412](group__bt__gap__defines.md#gac74bc8e109f5d9b4c0988ee6378ed471)#define BT\_APPEARANCE\_HEATING\_AIR\_CURTAIN 0x06C7

[ 414](group__bt__gap__defines.md#gac856a99a5db04dc20229a6e60a18d310)#define BT\_APPEARANCE\_GENERIC\_ACCESS\_CONTROL 0x0700

[ 416](group__bt__gap__defines.md#ga8e21f7df9d789b7c3aa6f7dab500df8c)#define BT\_APPEARANCE\_CONTROL\_ACCESS\_DOOR 0x0701

[ 418](group__bt__gap__defines.md#ga39134568b56c1d33e6567c893eb441f1)#define BT\_APPEARANCE\_CONTROL\_GARAGE\_DOOR 0x0702

[ 420](group__bt__gap__defines.md#ga2b6c7987ee4040216a385e665ff92321)#define BT\_APPEARANCE\_CONTROL\_EMERGENCY\_EXIT\_DOOR 0x0703

[ 422](group__bt__gap__defines.md#gac2f588b6202e9d6140ec682cfe45f65d)#define BT\_APPEARANCE\_CONTROL\_ACCESS\_LOCK 0x0704

[ 424](group__bt__gap__defines.md#ga321d63ead349c0a83ef289bd2e4efb33)#define BT\_APPEARANCE\_CONTROL\_ELEVATOR 0x0705

[ 426](group__bt__gap__defines.md#gaedc6415432862889e7f002fc9ef46b74)#define BT\_APPEARANCE\_CONTROL\_WINDOW 0x0706

[ 428](group__bt__gap__defines.md#gab2a476a90f20576c0a1784fdc1e5e633)#define BT\_APPEARANCE\_CONTROL\_ENTRANCE\_GATE 0x0707

[ 430](group__bt__gap__defines.md#ga29d07ce1101740b5f6f980660e405278)#define BT\_APPEARANCE\_CONTROL\_DOOR\_LOCK 0x0708

[ 432](group__bt__gap__defines.md#ga824236ba19c7f54d06b9abcd7df8c767)#define BT\_APPEARANCE\_CONTROL\_LOCKER 0x0709

[ 434](group__bt__gap__defines.md#ga414b202e93d1db533853093d66603720)#define BT\_APPEARANCE\_GENERIC\_MOTORIZED\_DEVICE 0x0740

[ 436](group__bt__gap__defines.md#ga376ef909868a5c273b71d1c372755707)#define BT\_APPEARANCE\_MOTORIZED\_GATE 0x0741

[ 438](group__bt__gap__defines.md#ga338de5523abf3fd81e913f3cdb4a31b6)#define BT\_APPEARANCE\_MOTORIZED\_AWNING 0x0742

[ 440](group__bt__gap__defines.md#gaaa39c48ed2d6edd5650743b82154462b)#define BT\_APPEARANCE\_MOTORIZED\_BLINDS\_OR\_SHADES 0x0743

[ 442](group__bt__gap__defines.md#ga53f6a4df5ccc2117525952be2e174ddc)#define BT\_APPEARANCE\_MOTORIZED\_CURTAINS 0x0744

[ 444](group__bt__gap__defines.md#ga5f32cab5c7a155fffbe0c33cadfef31a)#define BT\_APPEARANCE\_MOTORIZED\_SCREEN 0x0745

[ 446](group__bt__gap__defines.md#gadae82e45d9aafd34cafd3f0e793b1b24)#define BT\_APPEARANCE\_GENERIC\_POWER\_DEVICE 0x0780

[ 448](group__bt__gap__defines.md#gad9efd19e2c95525a3972c8b0f0417449)#define BT\_APPEARANCE\_POWER\_OUTLET 0x0781

[ 450](group__bt__gap__defines.md#ga2c5bd38d4eeb1aad2d29b004390a6d18)#define BT\_APPEARANCE\_POWER\_STRIP 0x0782

[ 452](group__bt__gap__defines.md#ga0d9aadc19f5f5f484769b225164866e4)#define BT\_APPEARANCE\_POWER\_PLUG 0x0783

[ 454](group__bt__gap__defines.md#ga07acce808c9cf2b5e84aacd65e8f256d)#define BT\_APPEARANCE\_POWER\_SUPPLY 0x0784

[ 456](group__bt__gap__defines.md#ga31842298741c822dcebba942453975c6)#define BT\_APPEARANCE\_POWER\_LED\_DRIVER 0x0785

[ 458](group__bt__gap__defines.md#ga7de26016aa039e3e72ddd61653e1c1d8)#define BT\_APPEARANCE\_POWER\_FLUORESCENT\_LAMP\_GEAR 0x0786

[ 460](group__bt__gap__defines.md#ga6396b1d813c9764bdfe92c4f2ba961b1)#define BT\_APPEARANCE\_POWER\_HID\_LAMP\_GEAR 0x0787

[ 462](group__bt__gap__defines.md#ga5d6b28b9660d2357e2af2bf0ceab9c18)#define BT\_APPEARANCE\_POWER\_CHARGE\_CASE 0x0788

[ 464](group__bt__gap__defines.md#gab6a5ac3941a5707f052126810a7f22e0)#define BT\_APPEARANCE\_POWER\_POWER\_BANK 0x0789

[ 466](group__bt__gap__defines.md#gacb3340c5193588eea2d42fe1bef443d0)#define BT\_APPEARANCE\_GENERIC\_LIGHT\_SOURCE 0x07C0

[ 468](group__bt__gap__defines.md#gafed8531ffde21d0ad6e8d477d64496f0)#define BT\_APPEARANCE\_LIGHT\_SOURCE\_INCANDESCENT\_BULB 0x07C1

[ 470](group__bt__gap__defines.md#ga66bf91b8a25ac88a0fd6ab9456201de1)#define BT\_APPEARANCE\_LIGHT\_SOURCE\_LED\_LAMP 0x07C2

[ 472](group__bt__gap__defines.md#ga1babd2989112bafb5819235fe5b6c556)#define BT\_APPEARANCE\_LIGHT\_SOURCE\_HID\_LAMP 0x07C3

[ 474](group__bt__gap__defines.md#ga39957a77aa54255ab3a06441e422e7e3)#define BT\_APPEARANCE\_LIGHT\_SOURCE\_FLUORESCENT\_LAMP 0x07C4

[ 476](group__bt__gap__defines.md#ga242d324cf5cf33e4edd5cf33e8c3c89b)#define BT\_APPEARANCE\_LIGHT\_SOURCE\_LED\_ARRAY 0x07C5

[ 478](group__bt__gap__defines.md#ga8449006920ed1fdd562c702ee2e16a21)#define BT\_APPEARANCE\_LIGHT\_SOURCE\_MULTICOLOR\_LED\_ARRAY 0x07C6

[ 480](group__bt__gap__defines.md#gaf47bce54f4ae1915cd64c3c2d254e353)#define BT\_APPEARANCE\_LIGHT\_SOURCE\_LOW\_VOLTAGE\_HALOGEN 0x07C7

[ 482](group__bt__gap__defines.md#gaed4400a94dae4f536a456cc55eb6f6d5)#define BT\_APPEARANCE\_LIGHT\_SOURCE\_OLED 0x07C8

[ 484](group__bt__gap__defines.md#ga1e70d961fca2719243c866464132684c)#define BT\_APPEARANCE\_GENERIC\_WINDOW\_COVERING 0x0800

[ 486](group__bt__gap__defines.md#ga37614ae63c8287bc4bd0c9a5bf00502e)#define BT\_APPEARANCE\_WINDOW\_SHADES 0x0801

[ 488](group__bt__gap__defines.md#ga717efaeab0329ded066567761b9983a7)#define BT\_APPEARANCE\_WINDOW\_BLINDS 0x0802

[ 490](group__bt__gap__defines.md#ga9945bb52a9ee3268efda7d5e05421e12)#define BT\_APPEARANCE\_WINDOW\_AWNING 0x0803

[ 492](group__bt__gap__defines.md#ga20352e58e6cec63efbb6beaa75c0e330)#define BT\_APPEARANCE\_WINDOW\_CURTAIN 0x0804

[ 494](group__bt__gap__defines.md#ga7ead13b128fbc50be3f5c101fb1383cb)#define BT\_APPEARANCE\_WINDOW\_EXTERIOR\_SHUTTER 0x0805

[ 496](group__bt__gap__defines.md#ga0a0b87095177af0560a540e545c97f42)#define BT\_APPEARANCE\_WINDOW\_EXTERIOR\_SCREEN 0x0806

[ 498](group__bt__gap__defines.md#ga32bb0f06096ce5259676a31342b9f0d9)#define BT\_APPEARANCE\_GENERIC\_AUDIO\_SINK 0x0840

[ 500](group__bt__gap__defines.md#gabcb109c4660a177494329faf353406f4)#define BT\_APPEARANCE\_AUDIO\_SINK\_STANDALONE\_SPEAKER 0x0841

[ 502](group__bt__gap__defines.md#ga93e3a858b2efabea72a8855a28ad21c2)#define BT\_APPEARANCE\_AUDIO\_SINK\_SOUNDBAR 0x0842

[ 504](group__bt__gap__defines.md#ga666aed968e9a0f9566edcc1bcba0bfbd)#define BT\_APPEARANCE\_AUDIO\_SINK\_BOOKSHELF\_SPEAKER 0x0843

[ 506](group__bt__gap__defines.md#ga6b3ddddf1de7d95a15aa6194ddc656ee)#define BT\_APPEARANCE\_AUDIO\_SINK\_STANDMOUNTED\_SPEAKER 0x0844

[ 508](group__bt__gap__defines.md#gadd82602d251aa555a06123ef0388d1b1)#define BT\_APPEARANCE\_AUDIO\_SINK\_SPEAKERPHONE 0x0845

[ 510](group__bt__gap__defines.md#gac85b90f2585044d0efa61191dba3c596)#define BT\_APPEARANCE\_GENERIC\_AUDIO\_SOURCE 0x0880

[ 512](group__bt__gap__defines.md#ga6dd1354de34ed79702d9d7878d859fcb)#define BT\_APPEARANCE\_AUDIO\_SOURCE\_MICROPHONE 0x0881

[ 514](group__bt__gap__defines.md#gaa8d5a95cb181e27efb2409d5dce3da57)#define BT\_APPEARANCE\_AUDIO\_SOURCE\_ALARM 0x0882

[ 516](group__bt__gap__defines.md#ga748b4fa86145f3950069ed44cde8cacb)#define BT\_APPEARANCE\_AUDIO\_SOURCE\_BELL 0x0883

[ 518](group__bt__gap__defines.md#ga3415afbd526b29b5bbafc1ac889bd371)#define BT\_APPEARANCE\_AUDIO\_SOURCE\_HORN 0x0884

[ 520](group__bt__gap__defines.md#ga35ecc1a1051379010123582c82e9b31c)#define BT\_APPEARANCE\_AUDIO\_SOURCE\_BROADCASTING\_DEVICE 0x0885

[ 522](group__bt__gap__defines.md#ga48fc37d769211cba1e6121e670b02e25)#define BT\_APPEARANCE\_AUDIO\_SOURCE\_SERVICE\_DESK 0x0886

[ 524](group__bt__gap__defines.md#ga6ad3ee00ed05c8a7ed182df5c82a5af4)#define BT\_APPEARANCE\_AUDIO\_SOURCE\_KIOSK 0x0887

[ 526](group__bt__gap__defines.md#gaad0fe38e5246c55cc562729448b9f390)#define BT\_APPEARANCE\_AUDIO\_SOURCE\_BROADCASTING\_ROOM 0x0888

[ 528](group__bt__gap__defines.md#gac8ab0549f83c9d6b68dc4dd75cfe7b1e)#define BT\_APPEARANCE\_AUDIO\_SOURCE\_AUDITORIUM 0x0889

[ 530](group__bt__gap__defines.md#ga49328394fd7505da9476d4d62ae60c03)#define BT\_APPEARANCE\_GENERIC\_MOTORIZED\_VEHICLE 0x08C0

[ 532](group__bt__gap__defines.md#ga6257291ed3e6d09ce6197e2081b36d04)#define BT\_APPEARANCE\_VEHICLE\_CAR 0x08C1

[ 534](group__bt__gap__defines.md#ga31ff643e1efccffd9ba73c793f63837c)#define BT\_APPEARANCE\_VEHICLE\_LARGE\_GOODS 0x08C2

[ 536](group__bt__gap__defines.md#ga68ade931a12e5d9e9863decad3d8de9e)#define BT\_APPEARANCE\_VEHICLE\_TWO\_WHEELED 0x08C3

[ 538](group__bt__gap__defines.md#gaa71eaa4fd0eef66a794475cb44aaf397)#define BT\_APPEARANCE\_VEHICLE\_MOTORBIKE 0x08C4

[ 540](group__bt__gap__defines.md#gae082982b90d94404b69c57987d8a2c5a)#define BT\_APPEARANCE\_VEHICLE\_SCOOTER 0x08C5

[ 542](group__bt__gap__defines.md#ga18b0231dbd97d8871f685774f9e1b4e1)#define BT\_APPEARANCE\_VEHICLE\_MOPED 0x08C6

[ 544](group__bt__gap__defines.md#ga8159dfd6933a2a5fdb2c72da9623bc2e)#define BT\_APPEARANCE\_VEHICLE\_THREE\_WHEELED 0x08C7

[ 546](group__bt__gap__defines.md#gac22a0476760c42eb8f00b36b74361c5e)#define BT\_APPEARANCE\_VEHICLE\_LIGHT 0x08C8

[ 548](group__bt__gap__defines.md#ga03e3660bdc2e439126f2f8df8ea335ee)#define BT\_APPEARANCE\_VEHICLE\_QUAD\_BIKE 0x08C9

[ 550](group__bt__gap__defines.md#ga0cf473bbf07d4576ab9f0116ca48f161)#define BT\_APPEARANCE\_VEHICLE\_MINIBUS 0x08CA

[ 552](group__bt__gap__defines.md#ga0da02a18987c653a3232c28a3e4908f7)#define BT\_APPEARANCE\_VEHICLE\_BUS 0x08CB

[ 554](group__bt__gap__defines.md#gabde7af9f7c25d56f5fb9643398273526)#define BT\_APPEARANCE\_VEHICLE\_TROLLEY 0x08CC

[ 556](group__bt__gap__defines.md#gaa149e56e4b4a1b6dde821fbdac3d9c32)#define BT\_APPEARANCE\_VEHICLE\_AGRICULTURAL 0x08CD

[ 558](group__bt__gap__defines.md#gafcb3909bf61bb130f8c0a217e69477b8)#define BT\_APPEARANCE\_VEHICLE\_CAMPER\_OR\_CARAVAN 0x08CE

[ 560](group__bt__gap__defines.md#ga9366a994d42c88490313380d419b2a8e)#define BT\_APPEARANCE\_VEHICLE\_RECREATIONAL 0x08CF

[ 562](group__bt__gap__defines.md#gac08b31ff9b618b19e4c1b43ae2056b5f)#define BT\_APPEARANCE\_GENERIC\_DOMESTIC\_APPLIANCE 0x0900

[ 564](group__bt__gap__defines.md#gad02c3dc8fa1321b14ee70264a36c4950)#define BT\_APPEARANCE\_APPLIANCE\_REFRIGERATOR 0x0901

[ 566](group__bt__gap__defines.md#ga6ec2458a171142a5e22ec339d23a5a0c)#define BT\_APPEARANCE\_APPLIANCE\_FREEZER 0x0902

[ 568](group__bt__gap__defines.md#ga7a48c5a07e677167ae10412ed2c1040b)#define BT\_APPEARANCE\_APPLIANCE\_OVEN 0x0903

[ 570](group__bt__gap__defines.md#gabaac12b866cd29547165331333e8be3d)#define BT\_APPEARANCE\_APPLIANCE\_MICROWAVE 0x0904

[ 572](group__bt__gap__defines.md#ga5b0d9632cb2ed4afd856f05a1e857394)#define BT\_APPEARANCE\_APPLIANCE\_TOASTER 0x0905

[ 574](group__bt__gap__defines.md#ga1febcada2c95105648831094a4de6a8d)#define BT\_APPEARANCE\_APPLIANCE\_WASHING\_MACHINE 0x0906

[ 576](group__bt__gap__defines.md#gaac26996e0de10b16e24900a08c1098f5)#define BT\_APPEARANCE\_APPLIANCE\_DRYER 0x0907

[ 578](group__bt__gap__defines.md#gac601c74c6132decf13527bdacbc5a08b)#define BT\_APPEARANCE\_APPLIANCE\_COFFEE\_MAKER 0x0908

[ 580](group__bt__gap__defines.md#gaeb66941a8e8b38ed0ea47305da157e24)#define BT\_APPEARANCE\_APPLIANCE\_CLOTHES\_IRON 0x0909

[ 582](group__bt__gap__defines.md#ga6a9885e9a2133c0732d056ecd63313ad)#define BT\_APPEARANCE\_APPLIANCE\_CURLING\_IRON 0x090A

[ 584](group__bt__gap__defines.md#ga15be0164f5883558fb61c9cb9679b78f)#define BT\_APPEARANCE\_APPLIANCE\_HAIR\_DRYER 0x090B

[ 586](group__bt__gap__defines.md#ga46d5f18bb8c764c43af97fddcec4a1ec)#define BT\_APPEARANCE\_APPLIANCE\_VACUUM\_CLEANER 0x090C

[ 588](group__bt__gap__defines.md#ga423e85d0816a4bd0205f4d8188e6c406)#define BT\_APPEARANCE\_APPLIANCE\_ROBOTIC\_VACUUM\_CLEANER 0x090D

[ 590](group__bt__gap__defines.md#ga78511e0ef7d509deeba65352e7f81ad8)#define BT\_APPEARANCE\_APPLIANCE\_RICE\_COOKER 0x090E

[ 592](group__bt__gap__defines.md#ga0292c6123b655964311d0e6027b5af20)#define BT\_APPEARANCE\_APPLIANCE\_CLOTHES\_STEAMER 0x090F

[ 594](group__bt__gap__defines.md#gabad761094a16873dcebbc6238825d84b)#define BT\_APPEARANCE\_GENERIC\_WEARABLE\_AUDIO\_DEVICE 0x0940

[ 596](group__bt__gap__defines.md#gab480735e2ba8db23d2668ea3a2137214)#define BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_EARBUD 0x0941

[ 598](group__bt__gap__defines.md#ga8bd98ba3a4c1cbf8dbf8235d9ad0f943)#define BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_HEADSET 0x0942

[ 600](group__bt__gap__defines.md#gae420044380309abba1b9570d26735315)#define BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_HEADPHONES 0x0943

[ 602](group__bt__gap__defines.md#ga59ea8ff5efec7a19bce8440e7ae78a1e)#define BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_NECK\_BAND 0x0944

[ 604](group__bt__gap__defines.md#ga24c9bcf9646ec5049abf310b31ab355e)#define BT\_APPEARANCE\_GENERIC\_AIRCRAFT 0x0980

[ 606](group__bt__gap__defines.md#ga6f1d2fb56f53ac5317b024d7487b8742)#define BT\_APPEARANCE\_AIRCRAFT\_LIGHT 0x0981

[ 608](group__bt__gap__defines.md#gad2d0b1c4b710e50127049ec4cd299396)#define BT\_APPEARANCE\_AIRCRAFT\_MICROLIGHT 0x0982

[ 610](group__bt__gap__defines.md#ga6f827322066333fe926f0912099e6903)#define BT\_APPEARANCE\_AIRCRAFT\_PARAGLIDER 0x0983

[ 612](group__bt__gap__defines.md#gae7be5c3bf9ad97e34d6c62bb791c39c0)#define BT\_APPEARANCE\_AIRCRAFT\_LARGE\_PASSENGER 0x0984

[ 614](group__bt__gap__defines.md#gadb3b07d6c3d3f679b15069fdd8d4e1ee)#define BT\_APPEARANCE\_GENERIC\_AV\_EQUIPMENT 0x09C0

[ 616](group__bt__gap__defines.md#ga7294c7b26ac8da3b9800c91ec824ad22)#define BT\_APPEARANCE\_AV\_EQUIPMENT\_AMPLIFIER 0x09C1

[ 618](group__bt__gap__defines.md#gac826e2e5326d1aa5fdd7ebf55fe395e6)#define BT\_APPEARANCE\_AV\_EQUIPMENT\_RECEIVER 0x09C2

[ 620](group__bt__gap__defines.md#gad60d1a387a1c62218baa3044e5acc3db)#define BT\_APPEARANCE\_AV\_EQUIPMENT\_RADIO 0x09C3

[ 622](group__bt__gap__defines.md#ga7ccf41932861fa5f33d12060a12d5aa7)#define BT\_APPEARANCE\_AV\_EQUIPMENT\_TUNER 0x09C4

[ 624](group__bt__gap__defines.md#ga69417cb3e9c434e751483328d6134cdf)#define BT\_APPEARANCE\_AV\_EQUIPMENT\_TURNTABLE 0x09C5

[ 626](group__bt__gap__defines.md#ga6c9ad45a9b22a94ae0cce16bfe749a33)#define BT\_APPEARANCE\_AV\_EQUIPMENT\_CD\_PLAYER 0x09C6

[ 628](group__bt__gap__defines.md#ga02681af8d755c701d9caef3f89a5c35a)#define BT\_APPEARANCE\_AV\_EQUIPMENT\_DVD\_PLAYER 0x09C7

[ 630](group__bt__gap__defines.md#ga1394bc80927fb8db4eef1786111c65c7)#define BT\_APPEARANCE\_AV\_EQUIPMENT\_BLURAY\_PLAYER 0x09C8

[ 632](group__bt__gap__defines.md#gaa01c862bff9aaaad09ed925da60fcb25)#define BT\_APPEARANCE\_AV\_EQUIPMENT\_OPTICAL\_DISC\_PLAYER 0x09C9

[ 634](group__bt__gap__defines.md#gad0ac86cf291b781b772fa9e85dda283a)#define BT\_APPEARANCE\_AV\_EQUIPMENT\_SET\_TOP\_BOX 0x09CA

[ 636](group__bt__gap__defines.md#ga44b70b2f515416baf686b1e127ef4375)#define BT\_APPEARANCE\_GENERIC\_DISPLAY\_EQUIPMENT 0x0A00

[ 638](group__bt__gap__defines.md#ga9a6684aa8677575625e049fa0da2c26c)#define BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_TELEVISION 0x0A01

[ 640](group__bt__gap__defines.md#gabbcb0fbbeb6423052db9d5e04410499c)#define BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_MONITOR 0x0A02

[ 642](group__bt__gap__defines.md#gaa98f5139c99b46515746fb76e9ae7f9b)#define BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_PROJECTOR 0x0A03

[ 644](group__bt__gap__defines.md#gadb5595a41edf5974e03649a675618b7b)#define BT\_APPEARANCE\_GENERIC\_HEARING\_AID 0x0A40

[ 646](group__bt__gap__defines.md#ga28cc6555937d9d5a9e8ae0079fc8a534)#define BT\_APPEARANCE\_HEARING\_AID\_IN\_EAR 0x0A41

[ 648](group__bt__gap__defines.md#ga1fa6231e14dcfa90a5518e61f0e4e302)#define BT\_APPEARANCE\_HEARING\_AID\_BEHIND\_EAR 0x0A42

[ 650](group__bt__gap__defines.md#ga82ba79bd9fd04a3fbdb6d8b4e35e3877)#define BT\_APPEARANCE\_HEARING\_AID\_COCHLEAR\_IMPLANT 0x0A43

[ 652](group__bt__gap__defines.md#gaca727b215a8277d921c0a3bfeccb3f14)#define BT\_APPEARANCE\_GENERIC\_GAMING 0x0A80

[ 654](group__bt__gap__defines.md#ga8fbaf0fced0cce12e08c4a516351b166)#define BT\_APPEARANCE\_HOME\_VIDEO\_GAME\_CONSOLE 0x0A81

[ 656](group__bt__gap__defines.md#ga39ad633d1795af4546bd930d0e799447)#define BT\_APPEARANCE\_PORTABLE\_HANDHELD\_CONSOLE 0x0A82

[ 658](group__bt__gap__defines.md#gabc243c7449804749704c1862db286eab)#define BT\_APPEARANCE\_GENERIC\_SIGNAGE 0x0AC0

[ 660](group__bt__gap__defines.md#gace31a591ef3b5f0812e4cbf417a2205a)#define BT\_APPEARANCE\_SIGNAGE\_DIGITAL 0x0AC1

[ 662](group__bt__gap__defines.md#gaa4674b06751edf98fa88ede568a68ad4)#define BT\_APPEARANCE\_SIGNAGE\_ELECTRONIC\_LABEL 0x0AC2

[ 664](group__bt__gap__defines.md#ga93ee753bf3b8819239041c065eaf024f)#define BT\_APPEARANCE\_GENERIC\_PULSE\_OXIMETER 0x0C40

[ 666](group__bt__gap__defines.md#ga8a298130c73299b6079dae3065954c0c)#define BT\_APPEARANCE\_PULSE\_OXIMETER\_FINGERTIP 0x0C41

[ 668](group__bt__gap__defines.md#gaebcadd5c37e6d87903e2cb97e03aeb7d)#define BT\_APPEARANCE\_PULSE\_OXIMETER\_WRIST 0x0C42

[ 670](group__bt__gap__defines.md#ga1aec23cd4f531a57260c7c8faf9caf40)#define BT\_APPEARANCE\_GENERIC\_WEIGHT\_SCALE 0x0C80

[ 672](group__bt__gap__defines.md#ga7387d717c77b38374e981991278aeb1c)#define BT\_APPEARANCE\_GENERIC\_PERSONAL\_MOBILITY\_DEVICE 0x0CC0

[ 674](group__bt__gap__defines.md#ga7966ec64cafe708fe94a7c323fbe3713)#define BT\_APPEARANCE\_MOBILITY\_POWERED\_WHEELCHAIR 0x0CC1

[ 676](group__bt__gap__defines.md#ga21f21a73f355ffaa408376ca4fc802a8)#define BT\_APPEARANCE\_MOBILITY\_SCOOTER 0x0CC2

[ 678](group__bt__gap__defines.md#gab77dd4cfe254df84cbe0b8d45247e198)#define BT\_APPEARANCE\_CONTINUOUS\_GLUCOSE\_MONITOR 0x0D00

[ 680](group__bt__gap__defines.md#ga481169a27fab19628f81a68af31d543c)#define BT\_APPEARANCE\_GENERIC\_INSULIN\_PUMP 0x0D40

[ 682](group__bt__gap__defines.md#ga63512439364307259010bededf7bfd8b)#define BT\_APPEARANCE\_INSULIN\_PUMP\_DURABLE 0x0D41

[ 684](group__bt__gap__defines.md#ga0979695247b96321e5a8b6869d09227a)#define BT\_APPEARANCE\_INSULIN\_PUMP\_PATCH 0x0D44

[ 686](group__bt__gap__defines.md#ga1562514d0182e8862edad570b7a346e6)#define BT\_APPEARANCE\_INSULIN\_PEN 0x0D48

[ 688](group__bt__gap__defines.md#ga08453eebe2ae8f53deddaa64a029c2b5)#define BT\_APPEARANCE\_GENERIC\_MEDICATION\_DELIVERY 0x0D80

[ 690](group__bt__gap__defines.md#ga1332c44cc3371fa9006993d03ba4ae12)#define BT\_APPEARANCE\_GENERIC\_SPIROMETER 0x0DC0

[ 692](group__bt__gap__defines.md#ga42b9d596efb757b209f080a8c33f3723)#define BT\_APPEARANCE\_SPIROMETER\_HANDHELD 0x0DC1

[ 694](group__bt__gap__defines.md#ga0d39ca2892bd96013b8c82111eecc1cb)#define BT\_APPEARANCE\_GENERIC\_OUTDOOR\_SPORTS 0x1440

[ 696](group__bt__gap__defines.md#ga30c97d6f5bff1a4a67e4f59eb4d49d2d)#define BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION 0x1441

[ 698](group__bt__gap__defines.md#ga52b6c51c9afcbbba12d9d3cae824f4a7)#define BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_AND\_NAV 0x1442

[ 700](group__bt__gap__defines.md#gadf053353789183d1b1c3ca13ad98559f)#define BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_POD 0x1443

[ 702](group__bt__gap__defines.md#ga8fbc7782099e724febb712ee108e8cba)#define BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_POD\_AND\_NAV 0x1444

706

[ 711](group__bt__gap__defines.md#gae9356673ee78d9abb27891738344513a)#define BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN 0x0030 /\* 30 ms \*/

[ 712](group__bt__gap__defines.md#ga747caa714962215453a966a323e77cf8)#define BT\_GAP\_SCAN\_FAST\_INTERVAL 0x0060 /\* 60 ms \*/

[ 713](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0)#define BT\_GAP\_SCAN\_FAST\_WINDOW 0x0030 /\* 30 ms \*/

[ 714](group__bt__gap__defines.md#ga1acb5143221e9f94af4d5dc3a9eab125)#define BT\_GAP\_SCAN\_SLOW\_INTERVAL\_1 0x0800 /\* 1.28 s \*/

[ 715](group__bt__gap__defines.md#ga29a1a15bfbe035f439c48d1db96db392)#define BT\_GAP\_SCAN\_SLOW\_WINDOW\_1 0x0012 /\* 11.25 ms \*/

[ 716](group__bt__gap__defines.md#ga38455c10880fddac0a1b4303a642e44d)#define BT\_GAP\_SCAN\_SLOW\_INTERVAL\_2 0x1000 /\* 2.56 s \*/

[ 717](group__bt__gap__defines.md#gaa809fd8143c2805768874195ac24936f)#define BT\_GAP\_SCAN\_SLOW\_WINDOW\_2 0x0012 /\* 11.25 ms \*/

[ 718](group__bt__gap__defines.md#ga397a52fe616416665b46a2bc454c2e11)#define BT\_GAP\_ADV\_FAST\_INT\_MIN\_1 0x0030 /\* 30 ms \*/

[ 719](group__bt__gap__defines.md#ga13acf16d3d8edd39636bb10df752775a)#define BT\_GAP\_ADV\_FAST\_INT\_MAX\_1 0x0060 /\* 60 ms \*/

[ 720](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60)#define BT\_GAP\_ADV\_FAST\_INT\_MIN\_2 0x00a0 /\* 100 ms \*/

[ 721](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb)#define BT\_GAP\_ADV\_FAST\_INT\_MAX\_2 0x00f0 /\* 150 ms \*/

[ 722](group__bt__gap__defines.md#ga647f70c07c15f11287b735cbaad2a326)#define BT\_GAP\_ADV\_SLOW\_INT\_MIN 0x0640 /\* 1 s \*/

[ 723](group__bt__gap__defines.md#gadecbfb823bbb6ffdd48be02df2f05f87)#define BT\_GAP\_ADV\_SLOW\_INT\_MAX 0x0780 /\* 1.2 s \*/

[ 724](group__bt__gap__defines.md#gafd724ebc809044574283c5547beda824)#define BT\_GAP\_PER\_ADV\_FAST\_INT\_MIN\_1 0x0018 /\* 30 ms \*/

[ 725](group__bt__gap__defines.md#ga849315b0b724af6017b910e78db0cfae)#define BT\_GAP\_PER\_ADV\_FAST\_INT\_MAX\_1 0x0030 /\* 60 ms \*/

[ 726](group__bt__gap__defines.md#ga61eb4d6d65f1dd9c475a6f2f44b27957)#define BT\_GAP\_PER\_ADV\_FAST\_INT\_MIN\_2 0x0050 /\* 100 ms \*/

[ 727](group__bt__gap__defines.md#ga264134294d8378d6e7d2bc52d4e0af1c)#define BT\_GAP\_PER\_ADV\_FAST\_INT\_MAX\_2 0x0078 /\* 150 ms \*/

[ 728](group__bt__gap__defines.md#gab51898ce46ee9ae468ed7ffc1d117321)#define BT\_GAP\_PER\_ADV\_SLOW\_INT\_MIN 0x0320 /\* 1 s \*/

[ 729](group__bt__gap__defines.md#gaa618da2a7c217527b0d962315caa1c22)#define BT\_GAP\_PER\_ADV\_SLOW\_INT\_MAX 0x03C0 /\* 1.2 s \*/

[ 730](group__bt__gap__defines.md#gadaa7f1547c4ea22936087c181d82a552)#define BT\_GAP\_INIT\_CONN\_INT\_MIN 0x0018 /\* 30 ms \*/

[ 731](group__bt__gap__defines.md#ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1)#define BT\_GAP\_INIT\_CONN\_INT\_MAX 0x0028 /\* 50 ms \*/

735

737enum {

[ 739](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20baaf7e1b40f6464a603e5116db269cacab) [BT\_GAP\_LE\_PHY\_NONE](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20baaf7e1b40f6464a603e5116db269cacab) = 0,

[ 741](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba53eff400720a20fe1a91da4834bad752) [BT\_GAP\_LE\_PHY\_1M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba53eff400720a20fe1a91da4834bad752) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 743](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba662049cc8293959194bcb481e1dd50a8) [BT\_GAP\_LE\_PHY\_2M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba662049cc8293959194bcb481e1dd50a8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 745](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba97d042e48448fdf6a9e35e5d38cb14c3) [BT\_GAP\_LE\_PHY\_CODED](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba97d042e48448fdf6a9e35e5d38cb14c3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

746};

747

749enum {

[ 751](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3eaf4d48e46c1da164e876e4ded28470c82) [BT\_GAP\_ADV\_TYPE\_ADV\_IND](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3eaf4d48e46c1da164e876e4ded28470c82) = 0x00,

[ 753](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea05b182a44fea67f52015cbfb4d775be8) [BT\_GAP\_ADV\_TYPE\_ADV\_DIRECT\_IND](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea05b182a44fea67f52015cbfb4d775be8) = 0x01,

[ 755](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3eae48316c135886d9f6d20f7bdba0858c1) [BT\_GAP\_ADV\_TYPE\_ADV\_SCAN\_IND](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3eae48316c135886d9f6d20f7bdba0858c1) = 0x02,

[ 757](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3eabb587b376bd6511881d6b70ceaa2af56) [BT\_GAP\_ADV\_TYPE\_ADV\_NONCONN\_IND](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3eabb587b376bd6511881d6b70ceaa2af56) = 0x03,

[ 759](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea5387de0177d3a9da9fd0c44ca30c7018) [BT\_GAP\_ADV\_TYPE\_SCAN\_RSP](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea5387de0177d3a9da9fd0c44ca30c7018) = 0x04,

[ 761](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea09292ffe2f0b76b8761fcaad6fbf9ba8) [BT\_GAP\_ADV\_TYPE\_EXT\_ADV](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea09292ffe2f0b76b8761fcaad6fbf9ba8) = 0x05,

762};

763

765enum {

[ 767](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711baf843db0752f3360ccb1a02c456ca9e5e) [BT\_GAP\_ADV\_PROP\_CONNECTABLE](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711baf843db0752f3360ccb1a02c456ca9e5e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 769](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba6c5ea1b8392783568b568c74f9f17571) [BT\_GAP\_ADV\_PROP\_SCANNABLE](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba6c5ea1b8392783568b568c74f9f17571) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 771](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba4595d3a3ea30bd4cd51ba4f1c4ab7de9) [BT\_GAP\_ADV\_PROP\_DIRECTED](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba4595d3a3ea30bd4cd51ba4f1c4ab7de9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 773](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba55258ac9a7b355db87aeec5d443718f7) [BT\_GAP\_ADV\_PROP\_SCAN\_RESPONSE](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba55258ac9a7b355db87aeec5d443718f7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 775](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711baeda2301e9eb191e742375e54bb765684) [BT\_GAP\_ADV\_PROP\_EXT\_ADV](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711baeda2301e9eb191e742375e54bb765684) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

776};

777

[ 779](group__bt__gap__defines.md#ga39ab5040c9471631486da7dbebd9c36f)#define BT\_GAP\_ADV\_MAX\_ADV\_DATA\_LEN 31

[ 785](group__bt__gap__defines.md#ga53af114e4925482739dc50dc84c2f641)#define BT\_GAP\_ADV\_MAX\_EXT\_ADV\_DATA\_LEN 1650

786

[ 787](group__bt__gap__defines.md#ga61ccce819d75313cb2ee58309ed4b275)#define BT\_GAP\_TX\_POWER\_INVALID 0x7f

[ 788](group__bt__gap__defines.md#ga64b5c5e429dadf1e875984f69cd399dc)#define BT\_GAP\_RSSI\_INVALID 0x7f

[ 789](group__bt__gap__defines.md#ga103af3e3142473be8897cd2647dca915)#define BT\_GAP\_SID\_INVALID 0xff

[ 790](group__bt__gap__defines.md#ga9d6b2af6b96eab6356ded93c54301ef6)#define BT\_GAP\_NO\_TIMEOUT 0x0000

791

792/\* The maximum allowed high duty cycle directed advertising timeout, 1.28

793 \* seconds in 10 ms unit.

794 \*/

[ 795](group__bt__gap__defines.md#gabe483d4dd601b11ac3eea570c962b1ec)#define BT\_GAP\_ADV\_HIGH\_DUTY\_CYCLE\_MAX\_TIMEOUT 128

796

[ 798](group__bt__gap__defines.md#ga90cfab7c375a8af6f9224a5635cbd023)#define BT\_GAP\_DATA\_LEN\_DEFAULT 0x001b /\* 27 bytes \*/

[ 800](group__bt__gap__defines.md#gacf5f35866d4677bd45c6e567886cabb9)#define BT\_GAP\_DATA\_LEN\_MAX 0x00fb /\* 251 bytes \*/

801

[ 803](group__bt__gap__defines.md#ga245249c0b6f8ccc419f2132f76362908)#define BT\_GAP\_DATA\_TIME\_DEFAULT 0x0148 /\* 328 us \*/

[ 805](group__bt__gap__defines.md#ga379b5d8d7f243abbc584c288cd01815f)#define BT\_GAP\_DATA\_TIME\_MAX 0x4290 /\* 17040 us \*/

806

[ 808](group__bt__gap__defines.md#gafa6f803fe3ada07030fb1f2f725940c4)#define BT\_GAP\_SID\_MAX 0x0F

[ 812](group__bt__gap__defines.md#gaf92b229c47309a7a5e99047f28b860e7)#define BT\_GAP\_PER\_ADV\_MAX\_SKIP 0x01F3

[ 814](group__bt__gap__defines.md#ga17d8ae7e98f6a1dfead4f8ecb75f9645)#define BT\_GAP\_PER\_ADV\_MIN\_TIMEOUT 0x000A /\* 100 ms \*/

[ 816](group__bt__gap__defines.md#gad6674199f615fa6ecaeb1fe9d099e04c)#define BT\_GAP\_PER\_ADV\_MAX\_TIMEOUT 0x4000 /\* 163.84 s \*/

[ 818](group__bt__gap__defines.md#ga07e21fdeb8a0a0b967690898bef2f7aa)#define BT\_GAP\_PER\_ADV\_MIN\_INTERVAL 0x0006 /\* 7.5 ms \*/

[ 820](group__bt__gap__defines.md#ga80bf3f1fb6f34a2c4363687149c365bd)#define BT\_GAP\_PER\_ADV\_MAX\_INTERVAL 0xFFFF /\* 81.91875 s \*/

821

[ 827](group__bt__gap__defines.md#ga450799e76dd71888ed3a045f68f58908)#define BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_MS(interval) ((interval) \* 5 / 4)

828

830enum {

[ 832](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966a8a82746ee64ffbcc62e79fdd8e0e30a0) [BT\_GAP\_CTE\_AOA](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966a8a82746ee64ffbcc62e79fdd8e0e30a0) = 0x00,

[ 834](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966aa8587383f9ea245e8c279fdd63417a19) [BT\_GAP\_CTE\_AOD\_1US](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966aa8587383f9ea245e8c279fdd63417a19) = 0x01,

[ 836](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966a2385af24a5a82f4d799674443b92e966) [BT\_GAP\_CTE\_AOD\_2US](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966a2385af24a5a82f4d799674443b92e966) = 0x02,

[ 838](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966aec9324d8e0997e1ace59895e168087e8) [BT\_GAP\_CTE\_NONE](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966aec9324d8e0997e1ace59895e168087e8) = 0xFF,

839};

840

842enum {

[ 843](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bace5a2d3f9fcb1a8913203ee6f437b910) [BT\_GAP\_SCA\_UNKNOWN](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bace5a2d3f9fcb1a8913203ee6f437b910) = 0,

[ 844](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba96900858c146259fc41af27b4cb62247) [BT\_GAP\_SCA\_251\_500](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba96900858c146259fc41af27b4cb62247) = 0,

[ 845](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bab19b506bc13aad6af3dba925153f4e7d) [BT\_GAP\_SCA\_151\_250](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bab19b506bc13aad6af3dba925153f4e7d) = 1,

[ 846](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba7f41d38c1a2125bd7c4d1765c8fbee73) [BT\_GAP\_SCA\_101\_150](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba7f41d38c1a2125bd7c4d1765c8fbee73) = 2,

[ 847](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6baa4011892d3409238f668c87626587bfd) [BT\_GAP\_SCA\_76\_100](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6baa4011892d3409238f668c87626587bfd) = 3,

[ 848](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba999a15d6ed8c860af7323af1b4d86fe9) [BT\_GAP\_SCA\_51\_75](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba999a15d6ed8c860af7323af1b4d86fe9) = 4,

[ 849](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba5fa53f708753d67bd6ec4f54b164b005) [BT\_GAP\_SCA\_31\_50](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba5fa53f708753d67bd6ec4f54b164b005) = 5,

[ 850](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba164fe8b7df50d8e393373153a1f70d1d) [BT\_GAP\_SCA\_21\_30](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba164fe8b7df50d8e393373153a1f70d1d) = 6,

[ 851](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bab8fd607ccdc30216fd90d4c6f568b9f6) [BT\_GAP\_SCA\_0\_20](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bab8fd607ccdc30216fd90d4c6f568b9f6) = 7,

852};

853

[ 873](group__bt__gap__defines.md#ga799f6cb9dd02b9995ed76fbe97be3eb3)#define BT\_LE\_SUPP\_FEAT\_40\_ENCODE(w64) BT\_BYTES\_LIST\_LE40(w64)

874

[ 893](group__bt__gap__defines.md#ga7aa92098e33840ff02cb8c0435637094)#define BT\_LE\_SUPP\_FEAT\_32\_ENCODE(w64) BT\_BYTES\_LIST\_LE32(w64)

894

[ 914](group__bt__gap__defines.md#gab8739c92f8d50b796539a21027c3b6eb)#define BT\_LE\_SUPP\_FEAT\_24\_ENCODE(w64) BT\_BYTES\_LIST\_LE24(w64)

915

[ 935](group__bt__gap__defines.md#ga3c29ad99d6a6e020148590381ab08b17)#define BT\_LE\_SUPP\_FEAT\_16\_ENCODE(w64) BT\_BYTES\_LIST\_LE16(w64)

936

[ 956](group__bt__gap__defines.md#ga8fac302925ac3ef8982630e6a0ec13af)#define BT\_LE\_SUPP\_FEAT\_8\_ENCODE(w64) \

957 (((w64) >> 0) & 0xFF)

958

[ 967](group__bt__gap__defines.md#ga86266eaf452dfaf82f097992e01397c8)#define BT\_LE\_SUPP\_FEAT\_VALIDATE(w64) \

968 BUILD\_ASSERT(!((w64) & (~BIT64\_MASK(40))), \

969 "RFU bit in LE Supported Features are not zeros.")

970

974

975#ifdef \_\_cplusplus

976}

977#endif

978

979#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_GAP\_H\_ \*/

[byteorder.h](bluetooth_2byteorder_8h.md)

Bluetooth byteorder API.

[BT\_GAP\_LE\_PHY\_1M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba53eff400720a20fe1a91da4834bad752)

@ BT\_GAP\_LE\_PHY\_1M

LE 1M PHY.

**Definition** gap.h:741

[BT\_GAP\_LE\_PHY\_2M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba662049cc8293959194bcb481e1dd50a8)

@ BT\_GAP\_LE\_PHY\_2M

LE 2M PHY.

**Definition** gap.h:743

[BT\_GAP\_LE\_PHY\_CODED](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba97d042e48448fdf6a9e35e5d38cb14c3)

@ BT\_GAP\_LE\_PHY\_CODED

LE Coded PHY.

**Definition** gap.h:745

[BT\_GAP\_LE\_PHY\_NONE](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20baaf7e1b40f6464a603e5116db269cacab)

@ BT\_GAP\_LE\_PHY\_NONE

Convenience macro for when no PHY is set.

**Definition** gap.h:739

[BT\_GAP\_ADV\_TYPE\_ADV\_DIRECT\_IND](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea05b182a44fea67f52015cbfb4d775be8)

@ BT\_GAP\_ADV\_TYPE\_ADV\_DIRECT\_IND

Directed connectable advertising.

**Definition** gap.h:753

[BT\_GAP\_ADV\_TYPE\_EXT\_ADV](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea09292ffe2f0b76b8761fcaad6fbf9ba8)

@ BT\_GAP\_ADV\_TYPE\_EXT\_ADV

Extended advertising, see advertising properties.

**Definition** gap.h:761

[BT\_GAP\_ADV\_TYPE\_SCAN\_RSP](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea5387de0177d3a9da9fd0c44ca30c7018)

@ BT\_GAP\_ADV\_TYPE\_SCAN\_RSP

Additional advertising data requested by an active scanner.

**Definition** gap.h:759

[BT\_GAP\_ADV\_TYPE\_ADV\_NONCONN\_IND](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3eabb587b376bd6511881d6b70ceaa2af56)

@ BT\_GAP\_ADV\_TYPE\_ADV\_NONCONN\_IND

Non-connectable and non-scannable advertising.

**Definition** gap.h:757

[BT\_GAP\_ADV\_TYPE\_ADV\_SCAN\_IND](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3eae48316c135886d9f6d20f7bdba0858c1)

@ BT\_GAP\_ADV\_TYPE\_ADV\_SCAN\_IND

Non-connectable and scannable advertising.

**Definition** gap.h:755

[BT\_GAP\_ADV\_TYPE\_ADV\_IND](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3eaf4d48e46c1da164e876e4ded28470c82)

@ BT\_GAP\_ADV\_TYPE\_ADV\_IND

Scannable and connectable advertising.

**Definition** gap.h:751

[BT\_GAP\_ADV\_PROP\_DIRECTED](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba4595d3a3ea30bd4cd51ba4f1c4ab7de9)

@ BT\_GAP\_ADV\_PROP\_DIRECTED

Directed advertising.

**Definition** gap.h:771

[BT\_GAP\_ADV\_PROP\_SCAN\_RESPONSE](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba55258ac9a7b355db87aeec5d443718f7)

@ BT\_GAP\_ADV\_PROP\_SCAN\_RESPONSE

Additional advertising data requested by an active scanner.

**Definition** gap.h:773

[BT\_GAP\_ADV\_PROP\_SCANNABLE](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba6c5ea1b8392783568b568c74f9f17571)

@ BT\_GAP\_ADV\_PROP\_SCANNABLE

Scannable advertising.

**Definition** gap.h:769

[BT\_GAP\_ADV\_PROP\_EXT\_ADV](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711baeda2301e9eb191e742375e54bb765684)

@ BT\_GAP\_ADV\_PROP\_EXT\_ADV

Extended advertising.

**Definition** gap.h:775

[BT\_GAP\_ADV\_PROP\_CONNECTABLE](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711baf843db0752f3360ccb1a02c456ca9e5e)

@ BT\_GAP\_ADV\_PROP\_CONNECTABLE

Connectable advertising.

**Definition** gap.h:767

[BT\_GAP\_CTE\_AOD\_2US](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966a2385af24a5a82f4d799674443b92e966)

@ BT\_GAP\_CTE\_AOD\_2US

Angle of Departure with 2 us slots.

**Definition** gap.h:836

[BT\_GAP\_CTE\_AOA](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966a8a82746ee64ffbcc62e79fdd8e0e30a0)

@ BT\_GAP\_CTE\_AOA

Angle of Arrival.

**Definition** gap.h:832

[BT\_GAP\_CTE\_AOD\_1US](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966aa8587383f9ea245e8c279fdd63417a19)

@ BT\_GAP\_CTE\_AOD\_1US

Angle of Departure with 1 us slots.

**Definition** gap.h:834

[BT\_GAP\_CTE\_NONE](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966aec9324d8e0997e1ace59895e168087e8)

@ BT\_GAP\_CTE\_NONE

No extensions.

**Definition** gap.h:838

[BT\_GAP\_SCA\_21\_30](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba164fe8b7df50d8e393373153a1f70d1d)

@ BT\_GAP\_SCA\_21\_30

21 ppm to 30 ppm

**Definition** gap.h:850

[BT\_GAP\_SCA\_31\_50](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba5fa53f708753d67bd6ec4f54b164b005)

@ BT\_GAP\_SCA\_31\_50

31 ppm to 50 ppm

**Definition** gap.h:849

[BT\_GAP\_SCA\_101\_150](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba7f41d38c1a2125bd7c4d1765c8fbee73)

@ BT\_GAP\_SCA\_101\_150

101 ppm to 150 ppm

**Definition** gap.h:846

[BT\_GAP\_SCA\_251\_500](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba96900858c146259fc41af27b4cb62247)

@ BT\_GAP\_SCA\_251\_500

251 ppm to 500 ppm

**Definition** gap.h:844

[BT\_GAP\_SCA\_51\_75](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba999a15d6ed8c860af7323af1b4d86fe9)

@ BT\_GAP\_SCA\_51\_75

51 ppm to 75 ppm

**Definition** gap.h:848

[BT\_GAP\_SCA\_76\_100](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6baa4011892d3409238f668c87626587bfd)

@ BT\_GAP\_SCA\_76\_100

76 ppm to 100 ppm

**Definition** gap.h:847

[BT\_GAP\_SCA\_151\_250](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bab19b506bc13aad6af3dba925153f4e7d)

@ BT\_GAP\_SCA\_151\_250

151 ppm to 250 ppm

**Definition** gap.h:845

[BT\_GAP\_SCA\_0\_20](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bab8fd607ccdc30216fd90d4c6f568b9f6)

@ BT\_GAP\_SCA\_0\_20

0 ppm to 20 ppm

**Definition** gap.h:851

[BT\_GAP\_SCA\_UNKNOWN](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bace5a2d3f9fcb1a8913203ee6f437b910)

@ BT\_GAP\_SCA\_UNKNOWN

Unknown.

**Definition** gap.h:843

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [gap.h](gap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
