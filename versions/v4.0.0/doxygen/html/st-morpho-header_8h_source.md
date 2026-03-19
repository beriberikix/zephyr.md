---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/st-morpho-header_8h_source.html
original_path: doxygen/html/st-morpho-header_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

st-morpho-header.h

[Go to the documentation of this file.](st-morpho-header_8h.md)

1/\*

2 \* Copyright (c) 2023 Teslabs Engineering S.L.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5#ifndef INCLUDE\_ZEPHYR\_DT\_BINDINGS\_GPIO\_ST\_MORPHO\_HEADER\_H\_

6#define INCLUDE\_ZEPHYR\_DT\_BINDINGS\_GPIO\_ST\_MORPHO\_HEADER\_H\_

7

[ 9](st-morpho-header_8h.md#af4c4ac0e90f06a1c438e83e86e43efc4)#define ST\_MORPHO\_PIN\_MASK 0xFF

10

[ 15](st-morpho-header_8h.md#aec4c885872fcd25043c88cc7880d1bdf)#define ST\_MORPHO\_L\_1 0

[ 16](st-morpho-header_8h.md#a744eb2f0189e6b835089f326ebca37ae)#define ST\_MORPHO\_L\_2 1

[ 17](st-morpho-header_8h.md#af15169af46408875b02a910a7d05b7cf)#define ST\_MORPHO\_L\_3 2

[ 18](st-morpho-header_8h.md#a71bb4a5d49826e7344f8273abbf6f1ff)#define ST\_MORPHO\_L\_4 3

[ 19](st-morpho-header_8h.md#a79601a70183288c3596590db02dfc917)#define ST\_MORPHO\_L\_5 4

[ 20](st-morpho-header_8h.md#a3927476a33f62b76929d2f3a81f3fc51)#define ST\_MORPHO\_L\_6 5

[ 21](st-morpho-header_8h.md#af98087926d93feb66169d2caf3da9783)#define ST\_MORPHO\_L\_7 6

[ 22](st-morpho-header_8h.md#a8f6b6a3768553753297cd9c9486f81a4)#define ST\_MORPHO\_L\_8 7

[ 23](st-morpho-header_8h.md#a9a48e48a738a741a88016bba35c7db1d)#define ST\_MORPHO\_L\_9 8

[ 24](st-morpho-header_8h.md#a39612dc32c4583b7809e415256e4f2f7)#define ST\_MORPHO\_L\_10 9

[ 25](st-morpho-header_8h.md#a5c118461a72ed3af45f0b6a9dd100ec2)#define ST\_MORPHO\_L\_11 10

[ 26](st-morpho-header_8h.md#a2e35b0d8cff585595670787bc7e5fcc8)#define ST\_MORPHO\_L\_12 11

[ 27](st-morpho-header_8h.md#a019a15fb232bb2c90f0cf5250b47a760)#define ST\_MORPHO\_L\_13 12

[ 28](st-morpho-header_8h.md#aa10fb53090b113f8b895d5c175ab7d3e)#define ST\_MORPHO\_L\_14 13

[ 29](st-morpho-header_8h.md#a6b1b1cc46ff81837cbd10d8affd25759)#define ST\_MORPHO\_L\_15 14

[ 30](st-morpho-header_8h.md#a2e947a6508d8aded395f124f236833ce)#define ST\_MORPHO\_L\_16 15

[ 31](st-morpho-header_8h.md#a126800c0af4e120058aa29374c32dfca)#define ST\_MORPHO\_L\_17 16

[ 32](st-morpho-header_8h.md#a360ad282e32c2db75df167a5429b1c8e)#define ST\_MORPHO\_L\_18 17

[ 33](st-morpho-header_8h.md#a743a3ab1466157e594f1f1df20078add)#define ST\_MORPHO\_L\_19 18

[ 34](st-morpho-header_8h.md#a599429ea62f56ce446a34471a2820ec1)#define ST\_MORPHO\_L\_20 19

[ 35](st-morpho-header_8h.md#aa8f7f6e01bf12283e62524b857ab157c)#define ST\_MORPHO\_L\_21 20

[ 36](st-morpho-header_8h.md#aaa1e799292c758f4d49a3b1e15320fb1)#define ST\_MORPHO\_L\_22 21

[ 37](st-morpho-header_8h.md#a8fba61554ce080c859f0fcc1b8dc6ba4)#define ST\_MORPHO\_L\_23 22

[ 38](st-morpho-header_8h.md#a86c15c33304c5d9cf6780e0fb0f1f5c8)#define ST\_MORPHO\_L\_24 23

[ 39](st-morpho-header_8h.md#ad8a92064e906d255260739a870049d62)#define ST\_MORPHO\_L\_25 24

[ 40](st-morpho-header_8h.md#aab2a3b7a8debcf2201a5eb1dd187276c)#define ST\_MORPHO\_L\_26 25

[ 41](st-morpho-header_8h.md#abcc82dfc6bcf802d46526f6027e3fd7e)#define ST\_MORPHO\_L\_27 26

[ 42](st-morpho-header_8h.md#a305100e4f83503828b13a9db76caf47e)#define ST\_MORPHO\_L\_28 27

[ 43](st-morpho-header_8h.md#a232e94783d5d74c6c18c63d478f46504)#define ST\_MORPHO\_L\_29 28

[ 44](st-morpho-header_8h.md#a3c6efb4ed29be7549fae5e3b0401da3c)#define ST\_MORPHO\_L\_30 29

[ 45](st-morpho-header_8h.md#a209fa960d432c550c89a05c0daa89929)#define ST\_MORPHO\_L\_31 30

[ 46](st-morpho-header_8h.md#a7e87747ad400cb40869223cae73cf96f)#define ST\_MORPHO\_L\_32 31

[ 47](st-morpho-header_8h.md#ab77d4422d229ea432ead96b191bcd461)#define ST\_MORPHO\_L\_33 32

[ 48](st-morpho-header_8h.md#a94f53e50d3e3ee717a01e2b23a676f8e)#define ST\_MORPHO\_L\_34 33

[ 49](st-morpho-header_8h.md#a5b1712c33edd7f4182e0bf6a990d2447)#define ST\_MORPHO\_L\_35 34

[ 50](st-morpho-header_8h.md#a7174f33cbd854f975d151671ff114e95)#define ST\_MORPHO\_L\_36 35

[ 51](st-morpho-header_8h.md#af852fbedd3fae06a78273d20c97ba926)#define ST\_MORPHO\_L\_37 36

[ 52](st-morpho-header_8h.md#a17f2c83b1ee5a57f7f9f4b8e2622646d)#define ST\_MORPHO\_L\_38 37

[ 53](st-morpho-header_8h.md#a205493fab8c1104868c254eabcb0d8ba)#define ST\_MORPHO\_L\_39 38

[ 54](st-morpho-header_8h.md#ac52077e3239059f4288cfc20fc33e1ae)#define ST\_MORPHO\_L\_40 39

[ 55](st-morpho-header_8h.md#a761d8234bd114f08dc6c3a609a9ddf04)#define ST\_MORPHO\_L\_41 40

[ 56](st-morpho-header_8h.md#ae8faa1b2ad722276597937019572769e)#define ST\_MORPHO\_L\_42 41

[ 57](st-morpho-header_8h.md#a8affcfac10cabeaee42bc4a62c66c743)#define ST\_MORPHO\_L\_43 42

[ 58](st-morpho-header_8h.md#ab14501c9564b5135fe0abead9c92f209)#define ST\_MORPHO\_L\_44 43

[ 59](st-morpho-header_8h.md#a85c37a3426ed1439fa84949d291918d5)#define ST\_MORPHO\_L\_45 44

[ 60](st-morpho-header_8h.md#a7c976f185048f0dfacdc79a12d64f83f)#define ST\_MORPHO\_L\_46 45

[ 61](st-morpho-header_8h.md#ababefc6821f097c4bf54eef8c0c9c3b7)#define ST\_MORPHO\_L\_47 46

[ 62](st-morpho-header_8h.md#a7130f3da9bd79ffcf3f781e18adef198)#define ST\_MORPHO\_L\_48 47

[ 63](st-morpho-header_8h.md#a5084b520b02dbd827a72a1202f92f3e1)#define ST\_MORPHO\_L\_49 48

[ 64](st-morpho-header_8h.md#aab51e14dc3e206f23eaa178c14e80855)#define ST\_MORPHO\_L\_50 49

[ 65](st-morpho-header_8h.md#a740fe6c42be92a0e5702871978f6ffea)#define ST\_MORPHO\_L\_51 50

[ 66](st-morpho-header_8h.md#a9bab7d6685c0065f21d33595be581013)#define ST\_MORPHO\_L\_52 51

[ 67](st-morpho-header_8h.md#abcf2825b9c4daf7c39cf51524efdc6dd)#define ST\_MORPHO\_L\_53 52

[ 68](st-morpho-header_8h.md#ac237ca25c10e7128f95be26ddb2f5662)#define ST\_MORPHO\_L\_54 53

[ 69](st-morpho-header_8h.md#a93a21e7d82a23d22c9ec6342fb35801b)#define ST\_MORPHO\_L\_55 54

[ 70](st-morpho-header_8h.md#ada243e09f6bc8d762a121f509d7f35d0)#define ST\_MORPHO\_L\_56 55

[ 71](st-morpho-header_8h.md#a1a598452f0e651c3e48e383b67f78334)#define ST\_MORPHO\_L\_57 56

[ 72](st-morpho-header_8h.md#a968bb384a0c59ad4c12623fedbe9f5e6)#define ST\_MORPHO\_L\_58 57

[ 73](st-morpho-header_8h.md#af6652e7124d7ae5b7eae21b0e294497a)#define ST\_MORPHO\_L\_59 58

[ 74](st-morpho-header_8h.md#a40b94b970bffc5400e55eaf2b9afb790)#define ST\_MORPHO\_L\_60 59

[ 75](st-morpho-header_8h.md#aa5aef00f15902f08e837f70d210e9755)#define ST\_MORPHO\_L\_61 60

[ 76](st-morpho-header_8h.md#a32169b2ba9944d32b7920a820db6dd31)#define ST\_MORPHO\_L\_62 61

[ 77](st-morpho-header_8h.md#a2ef43eee84c2caa9f9562733fda5be51)#define ST\_MORPHO\_L\_63 62

[ 78](st-morpho-header_8h.md#a591518b39ddb0fcc779118491acf0417)#define ST\_MORPHO\_L\_64 63

[ 79](st-morpho-header_8h.md#a4a22e7be98eccbf0c34bbde2f9bc8f61)#define ST\_MORPHO\_L\_65 64

[ 80](st-morpho-header_8h.md#aacdb9fc891e6f8bc7cf4a8fc029b905d)#define ST\_MORPHO\_L\_66 65

[ 81](st-morpho-header_8h.md#a8c8f46bcae0509cb1845b5b0d5bf4f35)#define ST\_MORPHO\_L\_67 66

[ 82](st-morpho-header_8h.md#a3b8db2b96e9872545928810f93f8138d)#define ST\_MORPHO\_L\_68 67

[ 83](st-morpho-header_8h.md#a16e300411c5b1a31a9dfa4dc2c3c1e7f)#define ST\_MORPHO\_L\_69 68

[ 84](st-morpho-header_8h.md#a55eecbccfc14ff0324d0561488715d84)#define ST\_MORPHO\_L\_70 69

[ 85](st-morpho-header_8h.md#a832b5cf86625834cffadcee7e9746d24)#define ST\_MORPHO\_L\_71 70

[ 86](st-morpho-header_8h.md#afa49104ced2509cc6db39ff37ffe6310)#define ST\_MORPHO\_L\_72 71

87

[ 88](st-morpho-header_8h.md#a76a61933e0c61591ea986414b375e7ed)#define ST\_MORPHO\_R\_1 72

[ 89](st-morpho-header_8h.md#ab13b526b90284fe6fc3584caafe40617)#define ST\_MORPHO\_R\_2 73

[ 90](st-morpho-header_8h.md#ae7a0c2084b7eed22a91bc5e4b802eb27)#define ST\_MORPHO\_R\_3 74

[ 91](st-morpho-header_8h.md#a7689fb0c9a49ebb263287ab298568307)#define ST\_MORPHO\_R\_4 75

[ 92](st-morpho-header_8h.md#a03df1fe95b3813709754016f9a9bf0c6)#define ST\_MORPHO\_R\_5 76

[ 93](st-morpho-header_8h.md#a6a4a173191015a23a4cce6616d8c3140)#define ST\_MORPHO\_R\_6 77

[ 94](st-morpho-header_8h.md#af6c9b8afc7bb91a08e8f0518777f5cd5)#define ST\_MORPHO\_R\_7 78

[ 95](st-morpho-header_8h.md#abf653c8e66e8fe76dc0559e05c8518f5)#define ST\_MORPHO\_R\_8 79

[ 96](st-morpho-header_8h.md#a8967a7092dc10042460e0a5e51c2aa92)#define ST\_MORPHO\_R\_9 80

[ 97](st-morpho-header_8h.md#a98aa9aeb1af8cfb41c1640dfea0f2753)#define ST\_MORPHO\_R\_10 81

[ 98](st-morpho-header_8h.md#a13b40b7b33fa8aec73add3b3d2cb70e9)#define ST\_MORPHO\_R\_11 82

[ 99](st-morpho-header_8h.md#a245a95538f671247b09f41feaeeed011)#define ST\_MORPHO\_R\_12 83

[ 100](st-morpho-header_8h.md#a0cf8ed73dbb537a4b747f25cb5be956a)#define ST\_MORPHO\_R\_13 84

[ 101](st-morpho-header_8h.md#aa724314fa7e256a31e6ccf5833cf82e7)#define ST\_MORPHO\_R\_14 85

[ 102](st-morpho-header_8h.md#a907bcc3df218c720c94d0bb9116c08ef)#define ST\_MORPHO\_R\_15 86

[ 103](st-morpho-header_8h.md#a6b13b2ccaba49026b3ed2b7fc63722bd)#define ST\_MORPHO\_R\_16 87

[ 104](st-morpho-header_8h.md#a889f48e62a128fa0f1f1609e22edee53)#define ST\_MORPHO\_R\_17 88

[ 105](st-morpho-header_8h.md#a5fed472e2d14d506cf69db1b6c9ddd4b)#define ST\_MORPHO\_R\_18 89

[ 106](st-morpho-header_8h.md#a2d751789b4dedf7821a4cb7ae9f7204c)#define ST\_MORPHO\_R\_19 90

[ 107](st-morpho-header_8h.md#aff35032167dfb9c5705001b0c9cc9182)#define ST\_MORPHO\_R\_20 91

[ 108](st-morpho-header_8h.md#a164c35d72e884c81aa07a0a9fd5880cf)#define ST\_MORPHO\_R\_21 92

[ 109](st-morpho-header_8h.md#a767e261fd1e6265681da6d457a6e7264)#define ST\_MORPHO\_R\_22 93

[ 110](st-morpho-header_8h.md#a46de2c38e92e0e45e6b389370640bfc2)#define ST\_MORPHO\_R\_23 94

[ 111](st-morpho-header_8h.md#a66a7780ea324e56a080b2750f7897094)#define ST\_MORPHO\_R\_24 95

[ 112](st-morpho-header_8h.md#ac052ae1a9d4de25e070ead9d4a41df78)#define ST\_MORPHO\_R\_25 96

[ 113](st-morpho-header_8h.md#abe6184b84c4ce46303bc321252849fba)#define ST\_MORPHO\_R\_26 97

[ 114](st-morpho-header_8h.md#abad9b23cc8b9f163b66f7e08e63ae82e)#define ST\_MORPHO\_R\_27 98

[ 115](st-morpho-header_8h.md#ae83add66ebc6bef0d288bfca06002b2c)#define ST\_MORPHO\_R\_28 99

[ 116](st-morpho-header_8h.md#a1ffe7134a54899ccfc2f9dd914034eb7)#define ST\_MORPHO\_R\_29 100

[ 117](st-morpho-header_8h.md#a9e728ff30ee7a0b84d383e45d167992a)#define ST\_MORPHO\_R\_30 101

[ 118](st-morpho-header_8h.md#a550ebeb4af3791a2adbf898a13778ce8)#define ST\_MORPHO\_R\_31 102

[ 119](st-morpho-header_8h.md#aea3f7ef4f1269ed91642e42b1596c3a2)#define ST\_MORPHO\_R\_32 103

[ 120](st-morpho-header_8h.md#afc9ed3f5d65f09a7efe7fca0fb0a0b2c)#define ST\_MORPHO\_R\_33 104

[ 121](st-morpho-header_8h.md#a9d4e1df66ece78e6a6953c8ecbaeb73b)#define ST\_MORPHO\_R\_34 105

[ 122](st-morpho-header_8h.md#af5f9d64a8b569f85e7f19ed522ac8a57)#define ST\_MORPHO\_R\_35 106

[ 123](st-morpho-header_8h.md#aa650fe5fb805bccad6139ed4f4256817)#define ST\_MORPHO\_R\_36 107

[ 124](st-morpho-header_8h.md#afbd5b257426c7dbfce5df4200552b1bc)#define ST\_MORPHO\_R\_37 108

[ 125](st-morpho-header_8h.md#aa52b614c36d9a26e064448c2385c95ce)#define ST\_MORPHO\_R\_38 109

[ 126](st-morpho-header_8h.md#a4b484d69c4b39ba48adaadc019036afb)#define ST\_MORPHO\_R\_39 110

[ 127](st-morpho-header_8h.md#a4f0b3e2c43ba27be4a1f4e5d62c97e9c)#define ST\_MORPHO\_R\_40 111

[ 128](st-morpho-header_8h.md#a7c46de2186397370df9c42801faee380)#define ST\_MORPHO\_R\_41 112

[ 129](st-morpho-header_8h.md#a38e3185f00a2d25f50be7babad5d8c0e)#define ST\_MORPHO\_R\_42 113

[ 130](st-morpho-header_8h.md#aaea5071983ac3c4e1e0a424711082e41)#define ST\_MORPHO\_R\_43 114

[ 131](st-morpho-header_8h.md#ad29c759f058a7604043cc542ac7d921d)#define ST\_MORPHO\_R\_44 115

[ 132](st-morpho-header_8h.md#a629e7111e1885641529c5b8123e5da45)#define ST\_MORPHO\_R\_45 116

[ 133](st-morpho-header_8h.md#ac3b90147b88cdf4a5ae2b037505d3ad5)#define ST\_MORPHO\_R\_46 117

[ 134](st-morpho-header_8h.md#a5768774a3ab39e23abe93b3beec2a9be)#define ST\_MORPHO\_R\_47 118

[ 135](st-morpho-header_8h.md#a70091a75ae5adf9d9a2e86ec717c0c50)#define ST\_MORPHO\_R\_48 119

[ 136](st-morpho-header_8h.md#a2281027b9062bd8ddf8a96928f01c8a5)#define ST\_MORPHO\_R\_49 120

[ 137](st-morpho-header_8h.md#a5fb68c2e113bae39328de4564fbebb4b)#define ST\_MORPHO\_R\_50 121

[ 138](st-morpho-header_8h.md#a632a699ac0be5e03b7106b451943d911)#define ST\_MORPHO\_R\_51 122

[ 139](st-morpho-header_8h.md#a91bf844a770fea58dce4a435289e2ebc)#define ST\_MORPHO\_R\_52 123

[ 140](st-morpho-header_8h.md#ab3e6858cdd5f31c236464181ded221ef)#define ST\_MORPHO\_R\_53 124

[ 141](st-morpho-header_8h.md#a4c82ed1fab2e1976469ddb9a636f2aac)#define ST\_MORPHO\_R\_54 125

[ 142](st-morpho-header_8h.md#a9c2d0adff9b3046d6d1aea46dec6bef2)#define ST\_MORPHO\_R\_55 126

[ 143](st-morpho-header_8h.md#a3e83a14566b122d9a41295c11b90eca6)#define ST\_MORPHO\_R\_56 127

[ 144](st-morpho-header_8h.md#a4fae4ca54188e42f096c8d36b1cc60df)#define ST\_MORPHO\_R\_57 128

[ 145](st-morpho-header_8h.md#ad9d6dedab1420cfde4cb899d99182028)#define ST\_MORPHO\_R\_58 129

[ 146](st-morpho-header_8h.md#accfb22345c4491c61857d6e06be16d58)#define ST\_MORPHO\_R\_59 130

[ 147](st-morpho-header_8h.md#a51069c38405f7ae9a8c54919137a2dd8)#define ST\_MORPHO\_R\_60 131

[ 148](st-morpho-header_8h.md#aac0ba09c411ce7c44552dca49241b70a)#define ST\_MORPHO\_R\_61 132

[ 149](st-morpho-header_8h.md#ab15f6b8145acea22d7239ae42287551e)#define ST\_MORPHO\_R\_62 133

[ 150](st-morpho-header_8h.md#a2d07c9984a89ffc7f693729a08c64c1b)#define ST\_MORPHO\_R\_63 134

[ 151](st-morpho-header_8h.md#a307834d865d27c972c61e4bc33a82a00)#define ST\_MORPHO\_R\_64 135

[ 152](st-morpho-header_8h.md#a8a724f2b528cbbea81e48ec88acc8834)#define ST\_MORPHO\_R\_65 136

[ 153](st-morpho-header_8h.md#a4064509127251858aec848f383bcc42c)#define ST\_MORPHO\_R\_66 137

[ 154](st-morpho-header_8h.md#a359c31a08c1c746b6e1368a117961442)#define ST\_MORPHO\_R\_67 138

[ 155](st-morpho-header_8h.md#a5f00cada04ccd2f91e82d01a93deb6f1)#define ST\_MORPHO\_R\_68 139

[ 156](st-morpho-header_8h.md#a3c6da64bf8795a14149093a88d1cbaa2)#define ST\_MORPHO\_R\_69 140

[ 157](st-morpho-header_8h.md#a14074f7cacd85dcfdf0ca2134e2d32e9)#define ST\_MORPHO\_R\_70 141

[ 158](st-morpho-header_8h.md#aa778cef9b49e70713643784c83d52256)#define ST\_MORPHO\_R\_71 142

[ 159](st-morpho-header_8h.md#ae0ec7e049c1c9104cf18d88b4cf4bada)#define ST\_MORPHO\_R\_72 143

160

162

163#endif /\* INCLUDE\_ZEPHYR\_DT\_BINDINGS\_GPIO\_ST\_MORPHO\_HEADER\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [st-morpho-header.h](st-morpho-header_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
