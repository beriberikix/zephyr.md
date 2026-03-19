---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lsm6dsv16x_8h_source.html
original_path: doxygen/html/lsm6dsv16x_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lsm6dsv16x.h

[Go to the documentation of this file.](lsm6dsv16x_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM6DSV16X\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM6DSV16X\_H\_

8

9/\* Accel range \*/

[ 10](lsm6dsv16x_8h.md#a0062d4a16bf431f8429ae06c1926dd13)#define LSM6DSV16X\_DT\_FS\_2G 0

[ 11](lsm6dsv16x_8h.md#a90b5d8955a2e8d4cfc1741f426433668)#define LSM6DSV16X\_DT\_FS\_4G 1

[ 12](lsm6dsv16x_8h.md#a5416be4ee0699ccf0994c7decfd9637f)#define LSM6DSV16X\_DT\_FS\_8G 2

[ 13](lsm6dsv16x_8h.md#a8106285e2a93c6dfc3b9c704166938e7)#define LSM6DSV16X\_DT\_FS\_16G 3

14

15/\* Gyro range \*/

[ 16](lsm6dsv16x_8h.md#aba0ad1e516dc73ce4f610474db2cf8f0)#define LSM6DSV16X\_DT\_FS\_125DPS 0x0

[ 17](lsm6dsv16x_8h.md#a4b908bb6e1684b69e3023a9b3056461d)#define LSM6DSV16X\_DT\_FS\_250DPS 0x1

[ 18](lsm6dsv16x_8h.md#a02d9fa7e2f077d98c4f6882555f74162)#define LSM6DSV16X\_DT\_FS\_500DPS 0x2

[ 19](lsm6dsv16x_8h.md#a062069e117674a493a3100369c6bae0c)#define LSM6DSV16X\_DT\_FS\_1000DPS 0x3

[ 20](lsm6dsv16x_8h.md#a7568fcc223af82319d884138ff43fcaa)#define LSM6DSV16X\_DT\_FS\_2000DPS 0x4

[ 21](lsm6dsv16x_8h.md#aad0a2d26bab54aff65bcf922db56d5dd)#define LSM6DSV16X\_DT\_FS\_4000DPS 0xc

22

23/\* Accel and Gyro Data rates \*/

[ 24](lsm6dsv16x_8h.md#a0b11f0f939bc10587ca0f8cc1e8da7d0)#define LSM6DSV16X\_DT\_ODR\_OFF 0x0

[ 25](lsm6dsv16x_8h.md#a51ad08e5e99e7da94cb4948f04cb7931)#define LSM6DSV16X\_DT\_ODR\_AT\_1Hz875 0x1

[ 26](lsm6dsv16x_8h.md#a908f07f0e822f1776f0e59166986fb43)#define LSM6DSV16X\_DT\_ODR\_AT\_7Hz5 0x2

[ 27](lsm6dsv16x_8h.md#af25ef10ac9e3183392ea6f3b4c8872ad)#define LSM6DSV16X\_DT\_ODR\_AT\_15Hz 0x3

[ 28](lsm6dsv16x_8h.md#acb735ed313c5813c26206dc0a8c649a0)#define LSM6DSV16X\_DT\_ODR\_AT\_30Hz 0x4

[ 29](lsm6dsv16x_8h.md#ac4763e79340953fdec46a2557cc3a7e9)#define LSM6DSV16X\_DT\_ODR\_AT\_60Hz 0x5

[ 30](lsm6dsv16x_8h.md#a4a8d2eb4eef9d6137b02aab5cf60d9b3)#define LSM6DSV16X\_DT\_ODR\_AT\_120Hz 0x6

[ 31](lsm6dsv16x_8h.md#a6cc44855f1c9ba6a44063c59204ab6e7)#define LSM6DSV16X\_DT\_ODR\_AT\_240Hz 0x7

[ 32](lsm6dsv16x_8h.md#a3814c412b7314efc062a8ed31a95a530)#define LSM6DSV16X\_DT\_ODR\_AT\_480Hz 0x8

[ 33](lsm6dsv16x_8h.md#abd274f980523545640e31b5e8fa373b0)#define LSM6DSV16X\_DT\_ODR\_AT\_960Hz 0x9

[ 34](lsm6dsv16x_8h.md#ae0d6b562ee0cb8523a1a9b974332f74c)#define LSM6DSV16X\_DT\_ODR\_AT\_1920Hz 0xA

[ 35](lsm6dsv16x_8h.md#a349976f99ae8bd144054eb4b6d5601a6)#define LSM6DSV16X\_DT\_ODR\_AT\_3840Hz 0xB

[ 36](lsm6dsv16x_8h.md#a7adb88cac62df5b3e63b9cf647ddfea3)#define LSM6DSV16X\_DT\_ODR\_AT\_7680Hz 0xC

[ 37](lsm6dsv16x_8h.md#af7f63bb894b71c67c933651539f370fa)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_15Hz625 0x13

[ 38](lsm6dsv16x_8h.md#ab3da725c6833f45b7a33afa55cfc40b3)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_31Hz25 0x14

[ 39](lsm6dsv16x_8h.md#ab024dfe5fc460ce2a9001732e21d9f05)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_62Hz5 0x15

[ 40](lsm6dsv16x_8h.md#a23da2ed6467ffb0cd1f2ab9ae9584ec8)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_125Hz 0x16

[ 41](lsm6dsv16x_8h.md#a62eaf6164a041b9280933dc50e3dca89)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_250Hz 0x17

[ 42](lsm6dsv16x_8h.md#a5875eadae47c3b41ee32c6571f5fd7e9)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_500Hz 0x18

[ 43](lsm6dsv16x_8h.md#a37a462e9411d24b07ffa0266baf4b0e8)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_1000Hz 0x19

[ 44](lsm6dsv16x_8h.md#a797db8e4aa3fa0ceae95f9af0a720767)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_2000Hz 0x1A

[ 45](lsm6dsv16x_8h.md#a312e7af10f7387764d4760017c8d19fd)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_4000Hz 0x1B

[ 46](lsm6dsv16x_8h.md#a490ba6a741e42ab2cf6a8260c1481bf7)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_8000Hz 0x1C

[ 47](lsm6dsv16x_8h.md#ae9f6bae9e1bec8194d9ce6a42e30f472)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_12Hz5 0x23

[ 48](lsm6dsv16x_8h.md#a3996f051df14448dfa2b91864ee0e951)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_25Hz 0x24

[ 49](lsm6dsv16x_8h.md#a76bee41aedef974a0db131751047db55)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_50Hz 0x25

[ 50](lsm6dsv16x_8h.md#adfc3e88f261d411102538e9e73352b55)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_100Hz 0x26

[ 51](lsm6dsv16x_8h.md#a30137882a4c78ddb51cff91a3775780c)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_200Hz 0x27

[ 52](lsm6dsv16x_8h.md#a2b30fdf564d398b52d8f0ca7ab39ec92)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_400Hz 0x28

[ 53](lsm6dsv16x_8h.md#adc01cf297fde9fa86865c80343107e6c)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_800Hz 0x29

[ 54](lsm6dsv16x_8h.md#ae2f10f581548e9c1b91680f044b70815)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_1600Hz 0x2A

[ 55](lsm6dsv16x_8h.md#a0685e049b46f34e3cff3590827a4cd04)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_3200Hz 0x2B

[ 56](lsm6dsv16x_8h.md#ae52f4d001cefe4730ff81224871821c7)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_6400Hz 0x2C

57

58/\* Accelerometer batching rates \*/

[ 59](lsm6dsv16x_8h.md#a4ef4f13c41aa295be449873b24c05f9c)#define LSM6DSV16X\_DT\_XL\_NOT\_BATCHED 0x0

[ 60](lsm6dsv16x_8h.md#adf6c8ffc133f1378d93ebfd06db51421)#define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_1Hz875 0x1

[ 61](lsm6dsv16x_8h.md#a61aab608d630df418dbda1e07f1ef59c)#define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_7Hz5 0x2

[ 62](lsm6dsv16x_8h.md#a0fbabfdc2567db259f0b20101359d2f9)#define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_15Hz 0x3

[ 63](lsm6dsv16x_8h.md#a5ae8341f1afd0dcf0eb57a848ee3e858)#define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_30Hz 0x4

[ 64](lsm6dsv16x_8h.md#a9e33dc1dbe6f3174e384b40593522991)#define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_60Hz 0x5

[ 65](lsm6dsv16x_8h.md#a95474384a2628c70dc3ebea4d4e1b506)#define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_120Hz 0x6

[ 66](lsm6dsv16x_8h.md#ac9c6e6e83c2f65b5e96517c474d2d5e1)#define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_240Hz 0x7

[ 67](lsm6dsv16x_8h.md#a8ef8c856d92fd2354d288635ca8b9257)#define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_480Hz 0x8

[ 68](lsm6dsv16x_8h.md#acf5fe0be8745dd5980f91e924e422f43)#define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_960Hz 0x9

[ 69](lsm6dsv16x_8h.md#a38847f0caf107ca88a4b2abf9940c425)#define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_1920Hz 0xa

[ 70](lsm6dsv16x_8h.md#a3a1a00ad577aede4ed2fcc961ed960bc)#define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_3840Hz 0xb

[ 71](lsm6dsv16x_8h.md#a32bd8c6d3b54fef541cdeadbfd34de96)#define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_7680Hz 0xc

72

73/\* Gyroscope batching rates \*/

[ 74](lsm6dsv16x_8h.md#a0805396bb4287ceb7afb52d3a9050b9a)#define LSM6DSV16X\_DT\_GY\_NOT\_BATCHED 0x0

[ 75](lsm6dsv16x_8h.md#a542a32ac0a25cac670f23225b1309e25)#define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_1Hz875 0x1

[ 76](lsm6dsv16x_8h.md#a7bd4e5d535e70450ec097298e6b34f4b)#define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_7Hz5 0x2

[ 77](lsm6dsv16x_8h.md#a60d78a7a0640b0f5f977a7af5b35160f)#define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_15Hz 0x3

[ 78](lsm6dsv16x_8h.md#a8d7b90c563ec26ef63120b39db208f9e)#define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_30Hz 0x4

[ 79](lsm6dsv16x_8h.md#a6d91f98f62bf25fbfb4c8a80a02fe590)#define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_60Hz 0x5

[ 80](lsm6dsv16x_8h.md#ad514e99fcd6951ceae37e15fa30bd56a)#define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_120Hz 0x6

[ 81](lsm6dsv16x_8h.md#aee057f81eec4ea3c9b97118b2029889d)#define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_240Hz 0x7

[ 82](lsm6dsv16x_8h.md#a61e8fe8cc642c818906a4a0905818453)#define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_480Hz 0x8

[ 83](lsm6dsv16x_8h.md#a3d3faee9ca754ac9b8d43bf42b15369e)#define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_960Hz 0x9

[ 84](lsm6dsv16x_8h.md#addf5efdd37d6dc7a2ec016b96853696b)#define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_1920Hz 0xa

[ 85](lsm6dsv16x_8h.md#a5102eb772bbfff3718d8691d89743169)#define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_3840Hz 0xb

[ 86](lsm6dsv16x_8h.md#a43005c15632a48a218ef26c71ccc5fc4)#define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_7680Hz 0xc

87

88/\* Temperature sensor batching rates \*/

[ 89](lsm6dsv16x_8h.md#a1d01297fd684f9baa36cde4c740a7805)#define LSM6DSV16X\_DT\_TEMP\_NOT\_BATCHED 0x0

[ 90](lsm6dsv16x_8h.md#a9b0f2f7f6f41d59b31c50eb73fe48186)#define LSM6DSV16X\_DT\_TEMP\_BATCHED\_AT\_1Hz875 0x1

[ 91](lsm6dsv16x_8h.md#a7557d711268e0db453913e2b4a761801)#define LSM6DSV16X\_DT\_TEMP\_BATCHED\_AT\_15Hz 0x2

[ 92](lsm6dsv16x_8h.md#aca5c0f34e41602a89925930a668b9811)#define LSM6DSV16X\_DT\_TEMP\_BATCHED\_AT\_60Hz 0x3

93

94/\* Sensor Fusion Low Power Data rates \*/

[ 95](lsm6dsv16x_8h.md#a8efcfdc7f0bd2c8161698dce91733fda)#define LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_15Hz 0x0

[ 96](lsm6dsv16x_8h.md#ab58b04372359a2676fbdf491f6e057e3)#define LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_30Hz 0x1

[ 97](lsm6dsv16x_8h.md#a357ede63697d797a4eccb0059c7a0796)#define LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_60Hz 0x2

[ 98](lsm6dsv16x_8h.md#a88efe57bf97af9d3818ca9701eb05bd1)#define LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_120Hz 0x3

[ 99](lsm6dsv16x_8h.md#ac9498844ce5357f85430f56234a35c43)#define LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_240Hz 0x4

[ 100](lsm6dsv16x_8h.md#a7f3fd0ec24d25ee9cc82bb328276f5ff)#define LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_480Hz 0x5

101

102/\* Sensor Fusion Low Power FIFO enable defs \*/

[ 103](lsm6dsv16x_8h.md#a3754cdaa4af134dfb0e474057b59dc2a)#define LSM6DSV16X\_DT\_SFLP\_FIFO\_OFF 0x0

[ 104](lsm6dsv16x_8h.md#a435cca9b30698e3eb75312d2fe59adbc)#define LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION 0x1

[ 105](lsm6dsv16x_8h.md#a8ce1813524567fae1a1ffaba524b1234)#define LSM6DSV16X\_DT\_SFLP\_FIFO\_GRAVITY 0x2

[ 106](lsm6dsv16x_8h.md#a7ae44c60e8a17870abd9e6d6fd78e22c)#define LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION\_GRAVITY 0x3

[ 107](lsm6dsv16x_8h.md#ac901645248e2b892c05aa6fb01ca8569)#define LSM6DSV16X\_DT\_SFLP\_FIFO\_GBIAS 0x4

[ 108](lsm6dsv16x_8h.md#a4851a7f7f1eccffbdf7ba630a0c54db9)#define LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION\_GBIAS 0x5

[ 109](lsm6dsv16x_8h.md#aa745b4ad6353c5ab492d80e09479291b)#define LSM6DSV16X\_DT\_SFLP\_FIFO\_GRAVITY\_GBIAS 0x6

[ 110](lsm6dsv16x_8h.md#a237a051673771c476a66f6b22dbee47d)#define LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION\_GRAVITY\_GBIAS 0x7

111

112

113#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM6DSV16X\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lsm6dsv16x.h](lsm6dsv16x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
