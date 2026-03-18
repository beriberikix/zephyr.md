---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sdp_8h_source.html
original_path: doxygen/html/sdp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdp.h

[Go to the documentation of this file.](sdp_8h.md)

1

4

5/\*

6 \* Copyright (c) 2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SDP\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SDP\_H\_

12

20

21#include <[zephyr/bluetooth/uuid.h](uuid_8h.md)>

22#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

28/\*

29 \* All definitions are based on Bluetooth Assigned Numbers

30 \* of the Bluetooth Specification

31 \*/

32

[ 37](group__bt__sdp.md#gac2c2379f8e483939826297dc49657837)#define BT\_SDP\_SDP\_SERVER\_SVCLASS 0x1000

[ 38](group__bt__sdp.md#gabe05780702a9be7da54a8c04f79ad752)#define BT\_SDP\_BROWSE\_GRP\_DESC\_SVCLASS 0x1001

[ 39](group__bt__sdp.md#ga383233a0ff3159ed653786490a4c06ae)#define BT\_SDP\_PUBLIC\_BROWSE\_GROUP 0x1002

[ 40](group__bt__sdp.md#gab1234d808a7e347328bf95ad065fd9c4)#define BT\_SDP\_SERIAL\_PORT\_SVCLASS 0x1101

[ 41](group__bt__sdp.md#gaf0199837105ded0d65314e573da6a3ed)#define BT\_SDP\_LAN\_ACCESS\_SVCLASS 0x1102

[ 42](group__bt__sdp.md#gaab655c1f93029ed64743156734e2519e)#define BT\_SDP\_DIALUP\_NET\_SVCLASS 0x1103

[ 43](group__bt__sdp.md#ga28fc78fc21e4d88569e5ca5727ed6202)#define BT\_SDP\_IRMC\_SYNC\_SVCLASS 0x1104

[ 44](group__bt__sdp.md#gaaf64788e0cc6d54a8511c07af22f6740)#define BT\_SDP\_OBEX\_OBJPUSH\_SVCLASS 0x1105

[ 45](group__bt__sdp.md#gacd25278a573edcb16aa4b60f8ffad20d)#define BT\_SDP\_OBEX\_FILETRANS\_SVCLASS 0x1106

[ 46](group__bt__sdp.md#ga39d4ce2465b10c10ee746c1491c49bea)#define BT\_SDP\_IRMC\_SYNC\_CMD\_SVCLASS 0x1107

[ 47](group__bt__sdp.md#ga6eb16aacf468b460fa7675ffc4703e68)#define BT\_SDP\_HEADSET\_SVCLASS 0x1108

[ 48](group__bt__sdp.md#ga16e1bc10528ac82f6cec822912f97d8c)#define BT\_SDP\_CORDLESS\_TELEPHONY\_SVCLASS 0x1109

[ 49](group__bt__sdp.md#gafeb3a3184a0b83e0045187cbe3cf24dc)#define BT\_SDP\_AUDIO\_SOURCE\_SVCLASS 0x110a

[ 50](group__bt__sdp.md#gaa0e334873b5477523572caa2359a4098)#define BT\_SDP\_AUDIO\_SINK\_SVCLASS 0x110b

[ 51](group__bt__sdp.md#gafe96e9d32797a83c793f0ed278054b80)#define BT\_SDP\_AV\_REMOTE\_TARGET\_SVCLASS 0x110c

[ 52](group__bt__sdp.md#ga2fdc3eb32196b5135b7f595a36cacb4c)#define BT\_SDP\_ADVANCED\_AUDIO\_SVCLASS 0x110d

[ 53](group__bt__sdp.md#gaea94250bed4c5e6ad47749a1237778f5)#define BT\_SDP\_AV\_REMOTE\_SVCLASS 0x110e

[ 54](group__bt__sdp.md#gaaae997769dfc8325c38830707f4d22e3)#define BT\_SDP\_AV\_REMOTE\_CONTROLLER\_SVCLASS 0x110f

[ 55](group__bt__sdp.md#ga9681e34d78cea87e413fa4be40e4239a)#define BT\_SDP\_INTERCOM\_SVCLASS 0x1110

[ 56](group__bt__sdp.md#ga31962fab5bed7c54311c4b291713a836)#define BT\_SDP\_FAX\_SVCLASS 0x1111

[ 57](group__bt__sdp.md#ga4c9322cf28a8b1aa96828152e8ee7379)#define BT\_SDP\_HEADSET\_AGW\_SVCLASS 0x1112

[ 58](group__bt__sdp.md#ga2ab79d7ff4e88820773cf24f0b0b6e20)#define BT\_SDP\_WAP\_SVCLASS 0x1113

[ 59](group__bt__sdp.md#ga22624d29917aaeaa0c281d9517178821)#define BT\_SDP\_WAP\_CLIENT\_SVCLASS 0x1114

[ 60](group__bt__sdp.md#gaa9abb444e3b43c1164d6b450b1c066e5)#define BT\_SDP\_PANU\_SVCLASS 0x1115

[ 61](group__bt__sdp.md#ga78a7be1db8be8d7eece0d17c629dd009)#define BT\_SDP\_NAP\_SVCLASS 0x1116

[ 62](group__bt__sdp.md#gaed2d6f72c344e2e9b9bdcefd23cb4086)#define BT\_SDP\_GN\_SVCLASS 0x1117

[ 63](group__bt__sdp.md#ga30f6edbd67d96f7752a223409c8e4431)#define BT\_SDP\_DIRECT\_PRINTING\_SVCLASS 0x1118

[ 64](group__bt__sdp.md#ga6bc247854656613d2fa9b47d55bd69d6)#define BT\_SDP\_REFERENCE\_PRINTING\_SVCLASS 0x1119

[ 65](group__bt__sdp.md#ga08730b1fd7088101fadb85e5dc13fd24)#define BT\_SDP\_IMAGING\_SVCLASS 0x111a

[ 66](group__bt__sdp.md#gaf19cd136b780ef303c1290b26ab2ca17)#define BT\_SDP\_IMAGING\_RESPONDER\_SVCLASS 0x111b

[ 67](group__bt__sdp.md#ga3f04a28d9764a0c7755babe379c25393)#define BT\_SDP\_IMAGING\_ARCHIVE\_SVCLASS 0x111c

[ 68](group__bt__sdp.md#ga51a4cfc28f86a650b03a7bbe6e5b883a)#define BT\_SDP\_IMAGING\_REFOBJS\_SVCLASS 0x111d

[ 69](group__bt__sdp.md#gab9f99989420545b3b0e71da6c5475f90)#define BT\_SDP\_HANDSFREE\_SVCLASS 0x111e

[ 70](group__bt__sdp.md#ga1c44ae236a292c91dc81539c9c89947c)#define BT\_SDP\_HANDSFREE\_AGW\_SVCLASS 0x111f

[ 71](group__bt__sdp.md#ga79d34c3b7641cf523adf6515720ceceb)#define BT\_SDP\_DIRECT\_PRT\_REFOBJS\_SVCLASS 0x1120

[ 72](group__bt__sdp.md#ga78607a42f5228b37d348614b12e48a77)#define BT\_SDP\_REFLECTED\_UI\_SVCLASS 0x1121

[ 73](group__bt__sdp.md#gac727f387a55a76c9a071cf62792f50e4)#define BT\_SDP\_BASIC\_PRINTING\_SVCLASS 0x1122

[ 74](group__bt__sdp.md#ga9298ac73a26a1ab2e53733f404e5c6ea)#define BT\_SDP\_PRINTING\_STATUS\_SVCLASS 0x1123

[ 75](group__bt__sdp.md#gab63eab5791898a47bd540eed4d55cddc)#define BT\_SDP\_HID\_SVCLASS 0x1124

[ 76](group__bt__sdp.md#ga873f8e03aeb696d3eb287a8d00796a4f)#define BT\_SDP\_HCR\_SVCLASS 0x1125

[ 77](group__bt__sdp.md#ga4ca1e6eb6fe385e526f8d84ed65ab285)#define BT\_SDP\_HCR\_PRINT\_SVCLASS 0x1126

[ 78](group__bt__sdp.md#ga621afe0f5a6d176c26e140c4162bee07)#define BT\_SDP\_HCR\_SCAN\_SVCLASS 0x1127

[ 79](group__bt__sdp.md#ga9617c02c6999d9fe987e91c6c2dc5dca)#define BT\_SDP\_CIP\_SVCLASS 0x1128

[ 80](group__bt__sdp.md#ga3e087c095a78f07efae660eceae9c11e)#define BT\_SDP\_VIDEO\_CONF\_GW\_SVCLASS 0x1129

[ 81](group__bt__sdp.md#ga629179357eff2cd60621f0e1e435df06)#define BT\_SDP\_UDI\_MT\_SVCLASS 0x112a

[ 82](group__bt__sdp.md#ga846599abf75f1cbb27028aea8a619f31)#define BT\_SDP\_UDI\_TA\_SVCLASS 0x112b

[ 83](group__bt__sdp.md#gab7a8499dbb73a2700389d55d331bd23e)#define BT\_SDP\_AV\_SVCLASS 0x112c

[ 84](group__bt__sdp.md#gad2234f8e0bce0e6b55d18c7a7c950e1d)#define BT\_SDP\_SAP\_SVCLASS 0x112d

[ 85](group__bt__sdp.md#gaec2475b7ba36b860c0f8a9cfc33df4a8)#define BT\_SDP\_PBAP\_PCE\_SVCLASS 0x112e

[ 86](group__bt__sdp.md#ga612bb83e9f08edd163433a5fbe9528fc)#define BT\_SDP\_PBAP\_PSE\_SVCLASS 0x112f

[ 87](group__bt__sdp.md#ga60a9fad26300c15e988e101f90c06435)#define BT\_SDP\_PBAP\_SVCLASS 0x1130

[ 88](group__bt__sdp.md#ga58f5cc54014e3723720e7c3b7ba82fd8)#define BT\_SDP\_MAP\_MSE\_SVCLASS 0x1132

[ 89](group__bt__sdp.md#ga47849c599678f7ec48c237b8b36e9cb7)#define BT\_SDP\_MAP\_MCE\_SVCLASS 0x1133

[ 90](group__bt__sdp.md#gaec665050af4cc3affcef3912bb212fc0)#define BT\_SDP\_MAP\_SVCLASS 0x1134

[ 91](group__bt__sdp.md#ga300585062ed9ae05daca226cb3c5440d)#define BT\_SDP\_GNSS\_SVCLASS 0x1135

[ 92](group__bt__sdp.md#gacdfb8ca6a776f57a2df38b4a6eaa8403)#define BT\_SDP\_GNSS\_SERVER\_SVCLASS 0x1136

[ 93](group__bt__sdp.md#ga9cce7e3a576329661b363b102cefa494)#define BT\_SDP\_MPS\_SC\_SVCLASS 0x113a

[ 94](group__bt__sdp.md#gaf847b2675482d3bb9674f569c3604e40)#define BT\_SDP\_MPS\_SVCLASS 0x113b

[ 95](group__bt__sdp.md#gaed5403661e0eb8f798a950bead59369a)#define BT\_SDP\_PNP\_INFO\_SVCLASS 0x1200

[ 96](group__bt__sdp.md#ga1b9a169ff4db4fda939cba3ce21f808b)#define BT\_SDP\_GENERIC\_NETWORKING\_SVCLASS 0x1201

[ 97](group__bt__sdp.md#gaa8e5c423fca1fb0d06504cdc5be276d1)#define BT\_SDP\_GENERIC\_FILETRANS\_SVCLASS 0x1202

[ 98](group__bt__sdp.md#gaec7548467ffb686b22a907d05e38f275)#define BT\_SDP\_GENERIC\_AUDIO\_SVCLASS 0x1203

[ 99](group__bt__sdp.md#ga010b005cfdb69c67cfc7e3c5c8426778)#define BT\_SDP\_GENERIC\_TELEPHONY\_SVCLASS 0x1204

[ 100](group__bt__sdp.md#ga9e7fa3bcf139462a2c33f90b526e1ad1)#define BT\_SDP\_UPNP\_SVCLASS 0x1205

[ 101](group__bt__sdp.md#ga102b24708429877c4f37a5008fb176b1)#define BT\_SDP\_UPNP\_IP\_SVCLASS 0x1206

[ 102](group__bt__sdp.md#ga3f50947a742b24089f86193e773d623b)#define BT\_SDP\_UPNP\_PAN\_SVCLASS 0x1300

[ 103](group__bt__sdp.md#gad418094573383e6252719abed97d24dd)#define BT\_SDP\_UPNP\_LAP\_SVCLASS 0x1301

[ 104](group__bt__sdp.md#gad4d97c0b664c48bdc0842f92240409c7)#define BT\_SDP\_UPNP\_L2CAP\_SVCLASS 0x1302

[ 105](group__bt__sdp.md#ga17d7fb3a77ef7266ea2d760fb3696a83)#define BT\_SDP\_VIDEO\_SOURCE\_SVCLASS 0x1303

[ 106](group__bt__sdp.md#ga1e3428b6d0197bd7c9d72154c025e9f5)#define BT\_SDP\_VIDEO\_SINK\_SVCLASS 0x1304

[ 107](group__bt__sdp.md#ga4e2ef8310c9396f9fb7781ab4732f308)#define BT\_SDP\_VIDEO\_DISTRIBUTION\_SVCLASS 0x1305

[ 108](group__bt__sdp.md#gaf8fc80f3b2ff245b7d354aa0488bb42b)#define BT\_SDP\_HDP\_SVCLASS 0x1400

[ 109](group__bt__sdp.md#ga87ba9fdf39fb99397a6dec4d92b6e3f1)#define BT\_SDP\_HDP\_SOURCE\_SVCLASS 0x1401

[ 110](group__bt__sdp.md#ga2125a92c6eb724a63d04188919a12bf1)#define BT\_SDP\_HDP\_SINK\_SVCLASS 0x1402

[ 111](group__bt__sdp.md#gae8010af5b12cd1c1b1633a4d2c9f5ab0)#define BT\_SDP\_GENERIC\_ACCESS\_SVCLASS 0x1800

[ 112](group__bt__sdp.md#gad3f345431526bb713921f4b51c48b056)#define BT\_SDP\_GENERIC\_ATTRIB\_SVCLASS 0x1801

[ 113](group__bt__sdp.md#ga694b04c2dae3b06b7fd66640468a5a38)#define BT\_SDP\_APPLE\_AGENT\_SVCLASS 0x2112

117

[ 118](group__bt__sdp.md#ga610e7cab0a598f272eeb2838f4c4c996)#define BT\_SDP\_SERVER\_RECORD\_HANDLE 0x0000

119

[ 128](group__bt__sdp.md#ga38f32cae462272b51eb4edca0c5c95a2)#define BT\_SDP\_ATTR\_RECORD\_HANDLE 0x0000

[ 129](group__bt__sdp.md#gab5c5be56c54d3f8bd4ac6defff0b1e7c)#define BT\_SDP\_ATTR\_SVCLASS\_ID\_LIST 0x0001

[ 130](group__bt__sdp.md#ga4d458591f8eba26feaab1220c49f6a29)#define BT\_SDP\_ATTR\_RECORD\_STATE 0x0002

[ 131](group__bt__sdp.md#gad2149fd761f7ae2ea6ef761ab2545ab4)#define BT\_SDP\_ATTR\_SERVICE\_ID 0x0003

[ 132](group__bt__sdp.md#ga3e7dad966deab42ff9fa0fd04d3d4514)#define BT\_SDP\_ATTR\_PROTO\_DESC\_LIST 0x0004

[ 133](group__bt__sdp.md#ga2609212bf5400c31351bc3ec5f60a7e1)#define BT\_SDP\_ATTR\_BROWSE\_GRP\_LIST 0x0005

[ 134](group__bt__sdp.md#ga462ec997a81c6b439a24e2de085676ab)#define BT\_SDP\_ATTR\_LANG\_BASE\_ATTR\_ID\_LIST 0x0006

[ 135](group__bt__sdp.md#ga7ef037ed6628aa7354736295e0e4ec77)#define BT\_SDP\_ATTR\_SVCINFO\_TTL 0x0007

[ 136](group__bt__sdp.md#gaf55a72ce05def1da08d15a23cee4c5e3)#define BT\_SDP\_ATTR\_SERVICE\_AVAILABILITY 0x0008

[ 137](group__bt__sdp.md#ga0b5b19caa523e4cb9da8a2bfc6eab20a)#define BT\_SDP\_ATTR\_PROFILE\_DESC\_LIST 0x0009

[ 138](group__bt__sdp.md#gad8302739bca706f6da851d912ada0f82)#define BT\_SDP\_ATTR\_DOC\_URL 0x000a

[ 139](group__bt__sdp.md#ga0bc613d68dace4cce7a4eec654f5a1e4)#define BT\_SDP\_ATTR\_CLNT\_EXEC\_URL 0x000b

[ 140](group__bt__sdp.md#ga365048bcb0ad2989aec9dd0d89abbfb9)#define BT\_SDP\_ATTR\_ICON\_URL 0x000c

[ 141](group__bt__sdp.md#gaf7f0b2f30ede36cf280bf31c5e76a99c)#define BT\_SDP\_ATTR\_ADD\_PROTO\_DESC\_LIST 0x000d

142

[ 143](group__bt__sdp.md#ga15a104c78357f2353cd49eb858de057d)#define BT\_SDP\_ATTR\_GROUP\_ID 0x0200

[ 144](group__bt__sdp.md#ga23a63b424ab381048cb898ebbdb64a02)#define BT\_SDP\_ATTR\_IP\_SUBNET 0x0200

[ 145](group__bt__sdp.md#gab698c476197acca0d499e39f7f246c66)#define BT\_SDP\_ATTR\_VERSION\_NUM\_LIST 0x0200

[ 146](group__bt__sdp.md#ga8a693e5265c7801e3c1125473c31445f)#define BT\_SDP\_ATTR\_SUPPORTED\_FEATURES\_LIST 0x0200

[ 147](group__bt__sdp.md#gac7583b3d2a0ebc82e5cf2e6705249201)#define BT\_SDP\_ATTR\_GOEP\_L2CAP\_PSM 0x0200

[ 148](group__bt__sdp.md#gab8fe8881b4470ab3522e710e36470ddb)#define BT\_SDP\_ATTR\_SVCDB\_STATE 0x0201

149

[ 150](group__bt__sdp.md#ga39b3436f9da303bd2ce1ad38f072ed9f)#define BT\_SDP\_ATTR\_MPSD\_SCENARIOS 0x0200

[ 151](group__bt__sdp.md#gaa3cc3d9a6ac7375e66b0892631698fd0)#define BT\_SDP\_ATTR\_MPMD\_SCENARIOS 0x0201

[ 152](group__bt__sdp.md#ga45795e50564492ac9bce8d6832883741)#define BT\_SDP\_ATTR\_MPS\_DEPENDENCIES 0x0202

153

[ 154](group__bt__sdp.md#ga230f70b576c14ba1dbe0cf6eda6220e0)#define BT\_SDP\_ATTR\_SERVICE\_VERSION 0x0300

[ 155](group__bt__sdp.md#ga617dc829eb1192cd283bef67a357d75f)#define BT\_SDP\_ATTR\_EXTERNAL\_NETWORK 0x0301

[ 156](group__bt__sdp.md#gae12e2daea8febbbd047c1c3843f56933)#define BT\_SDP\_ATTR\_SUPPORTED\_DATA\_STORES\_LIST 0x0301

[ 157](group__bt__sdp.md#ga4732f83c88de43a90ca3d58a136907b6)#define BT\_SDP\_ATTR\_DATA\_EXCHANGE\_SPEC 0x0301

[ 158](group__bt__sdp.md#ga9c78d47f54e82a51f7d04a6f6c97663c)#define BT\_SDP\_ATTR\_NETWORK 0x0301

[ 159](group__bt__sdp.md#gaeebfb4a085417db65241b21a27258d84)#define BT\_SDP\_ATTR\_FAX\_CLASS1\_SUPPORT 0x0302

[ 160](group__bt__sdp.md#gaa122bfee476a8e83346823e23978f7a0)#define BT\_SDP\_ATTR\_REMOTE\_AUDIO\_VOLUME\_CONTROL 0x0302

[ 161](group__bt__sdp.md#ga54e285c7a12becef9742093e1777c06b)#define BT\_SDP\_ATTR\_MCAP\_SUPPORTED\_PROCEDURES 0x0302

[ 162](group__bt__sdp.md#ga861470cd4b505d074abb727ba72c088a)#define BT\_SDP\_ATTR\_FAX\_CLASS20\_SUPPORT 0x0303

[ 163](group__bt__sdp.md#gac12ed37044c3f12c2d41b1fd23eacada)#define BT\_SDP\_ATTR\_SUPPORTED\_FORMATS\_LIST 0x0303

[ 164](group__bt__sdp.md#ga2475947ccdb9f30ece61a34959fd6ce2)#define BT\_SDP\_ATTR\_FAX\_CLASS2\_SUPPORT 0x0304

[ 165](group__bt__sdp.md#gac4906f9fa368fbf604830cd5c5fdcb57)#define BT\_SDP\_ATTR\_AUDIO\_FEEDBACK\_SUPPORT 0x0305

[ 166](group__bt__sdp.md#ga74dacfd7807d7f3ec7a7594a9329f0b2)#define BT\_SDP\_ATTR\_NETWORK\_ADDRESS 0x0306

[ 167](group__bt__sdp.md#ga1ef964c955473601910ee3997b9ce5cd)#define BT\_SDP\_ATTR\_WAP\_GATEWAY 0x0307

[ 168](group__bt__sdp.md#gafeff5e5b60bd47c44f8edbe8ff7e78a0)#define BT\_SDP\_ATTR\_HOMEPAGE\_URL 0x0308

[ 169](group__bt__sdp.md#gae1a3ff84a5588e55258c35ee57d6a5b5)#define BT\_SDP\_ATTR\_WAP\_STACK\_TYPE 0x0309

[ 170](group__bt__sdp.md#ga21214c2236a5dca24a45998640761e7b)#define BT\_SDP\_ATTR\_SECURITY\_DESC 0x030a

[ 171](group__bt__sdp.md#ga13851f9f9a5ba8514d20cffbe5eb9f14)#define BT\_SDP\_ATTR\_NET\_ACCESS\_TYPE 0x030b

[ 172](group__bt__sdp.md#ga7347caab1c7e8755250567d9d8cc7266)#define BT\_SDP\_ATTR\_MAX\_NET\_ACCESSRATE 0x030c

[ 173](group__bt__sdp.md#ga01c0cdb8975484242e6c4b052dabfd91)#define BT\_SDP\_ATTR\_IP4\_SUBNET 0x030d

[ 174](group__bt__sdp.md#ga10b3d4826904489d474af5e9c21c0831)#define BT\_SDP\_ATTR\_IP6\_SUBNET 0x030e

[ 175](group__bt__sdp.md#ga5347dbc038ac9c259d17c14ed9a812d3)#define BT\_SDP\_ATTR\_SUPPORTED\_CAPABILITIES 0x0310

[ 176](group__bt__sdp.md#ga498d9beaa7877570fe834d854de36fcb)#define BT\_SDP\_ATTR\_SUPPORTED\_FEATURES 0x0311

[ 177](group__bt__sdp.md#gabc7cdfd247da5e2ecfd441c0436471f3)#define BT\_SDP\_ATTR\_SUPPORTED\_FUNCTIONS 0x0312

[ 178](group__bt__sdp.md#gadbce181b739c201070d6abcbdc4139f4)#define BT\_SDP\_ATTR\_TOTAL\_IMAGING\_DATA\_CAPACITY 0x0313

[ 179](group__bt__sdp.md#gada3d989d6c8c0664ba0bf998414a0328)#define BT\_SDP\_ATTR\_SUPPORTED\_REPOSITORIES 0x0314

[ 180](group__bt__sdp.md#ga03d653957d68b5d0eeda1fa7c9aa4587)#define BT\_SDP\_ATTR\_MAS\_INSTANCE\_ID 0x0315

[ 181](group__bt__sdp.md#ga41fc674e8571556397135734d28b829a)#define BT\_SDP\_ATTR\_SUPPORTED\_MESSAGE\_TYPES 0x0316

[ 182](group__bt__sdp.md#gaa681b17ebfe013c196cf372dcd030c6e)#define BT\_SDP\_ATTR\_PBAP\_SUPPORTED\_FEATURES 0x0317

[ 183](group__bt__sdp.md#gaa50f16945c15f7a954c10dbc8fc394bf)#define BT\_SDP\_ATTR\_MAP\_SUPPORTED\_FEATURES 0x0317

184

[ 185](group__bt__sdp.md#ga4af959fbdfe7cee84008642091df948d)#define BT\_SDP\_ATTR\_SPECIFICATION\_ID 0x0200

[ 186](group__bt__sdp.md#gab5c2534491b43cfc9d2c7e8807b29ff2)#define BT\_SDP\_ATTR\_VENDOR\_ID 0x0201

[ 187](group__bt__sdp.md#gaac9298efffbcf07303f972a12b50f4b6)#define BT\_SDP\_ATTR\_PRODUCT\_ID 0x0202

[ 188](group__bt__sdp.md#gae0f4af728f964ee1c11d86b785575a87)#define BT\_SDP\_ATTR\_VERSION 0x0203

[ 189](group__bt__sdp.md#ga0868f7d90e3944f105028868511896cf)#define BT\_SDP\_ATTR\_PRIMARY\_RECORD 0x0204

[ 190](group__bt__sdp.md#gad0ac4a65c51ccdf4cd128eb8697e56ca)#define BT\_SDP\_ATTR\_VENDOR\_ID\_SOURCE 0x0205

191

[ 192](group__bt__sdp.md#gab33be247c7574e985dfb34e3c121dd23)#define BT\_SDP\_ATTR\_HID\_DEVICE\_RELEASE\_NUMBER 0x0200

[ 193](group__bt__sdp.md#ga8bb0a4f69b029048958a1395cc98d285)#define BT\_SDP\_ATTR\_HID\_PARSER\_VERSION 0x0201

[ 194](group__bt__sdp.md#ga43aa99ef47032c04be1bdee571dcfa5c)#define BT\_SDP\_ATTR\_HID\_DEVICE\_SUBCLASS 0x0202

[ 195](group__bt__sdp.md#ga5c06a7b07412b0a319656208700ac48e)#define BT\_SDP\_ATTR\_HID\_COUNTRY\_CODE 0x0203

[ 196](group__bt__sdp.md#ga26ff5394958b41c5a595952992e0bbbe)#define BT\_SDP\_ATTR\_HID\_VIRTUAL\_CABLE 0x0204

[ 197](group__bt__sdp.md#ga30c601e79bd47f29bcc8325ac19a8391)#define BT\_SDP\_ATTR\_HID\_RECONNECT\_INITIATE 0x0205

[ 198](group__bt__sdp.md#gaadf6a1c7740d5055e1877142b75d07c2)#define BT\_SDP\_ATTR\_HID\_DESCRIPTOR\_LIST 0x0206

[ 199](group__bt__sdp.md#ga732063505ff39f236b03646f8b7a78c6)#define BT\_SDP\_ATTR\_HID\_LANG\_ID\_BASE\_LIST 0x0207

[ 200](group__bt__sdp.md#ga498779c65f410192862aa288cb1e277f)#define BT\_SDP\_ATTR\_HID\_SDP\_DISABLE 0x0208

[ 201](group__bt__sdp.md#gac92ef24a03422abdc6ca932e0675aa57)#define BT\_SDP\_ATTR\_HID\_BATTERY\_POWER 0x0209

[ 202](group__bt__sdp.md#ga4bd0452184af1530887b0a785e30fca7)#define BT\_SDP\_ATTR\_HID\_REMOTE\_WAKEUP 0x020a

[ 203](group__bt__sdp.md#gaa792255345fe4f62062a848aebb220c7)#define BT\_SDP\_ATTR\_HID\_PROFILE\_VERSION 0x020b

[ 204](group__bt__sdp.md#ga1cd5f256115ef60736eb1089bf66988c)#define BT\_SDP\_ATTR\_HID\_SUPERVISION\_TIMEOUT 0x020c

[ 205](group__bt__sdp.md#ga866194b8e0ec3eebe086998ae0c6e2ab)#define BT\_SDP\_ATTR\_HID\_NORMALLY\_CONNECTABLE 0x020d

[ 206](group__bt__sdp.md#ga511980e049b047618f97ac38a4ea3f4e)#define BT\_SDP\_ATTR\_HID\_BOOT\_DEVICE 0x020e

210

211/\*

212 \* These identifiers are based on the SDP spec stating that

213 \* "base attribute id of the primary (universal) language must be 0x0100"

214 \*

215 \* Other languages should have their own offset; e.g.:

216 \* #define XXXLangBase yyyy

217 \* #define AttrServiceName\_XXX 0x0000+XXXLangBase

218 \*/

[ 219](group__bt__sdp.md#gab502c9288e5f01dfdaaf8390bb3f6e49)#define BT\_SDP\_PRIMARY\_LANG\_BASE 0x0100

220

[ 221](group__bt__sdp.md#ga76737502226c623bf508ae53a6015e08)#define BT\_SDP\_ATTR\_SVCNAME\_PRIMARY (0x0000 + BT\_SDP\_PRIMARY\_LANG\_BASE)

[ 222](group__bt__sdp.md#ga3e991ec1d5467c0b3ce5d9a7e750a300)#define BT\_SDP\_ATTR\_SVCDESC\_PRIMARY (0x0001 + BT\_SDP\_PRIMARY\_LANG\_BASE)

[ 223](group__bt__sdp.md#gab8b0110be857d6eca206e00c3b5e373a)#define BT\_SDP\_ATTR\_PROVNAME\_PRIMARY (0x0002 + BT\_SDP\_PRIMARY\_LANG\_BASE)

224

[ 246](group__bt__sdp.md#ga36f257de103356c3ebeb55e23186ed99)#define BT\_SDP\_DATA\_NIL 0x00

[ 247](group__bt__sdp.md#ga546a46c2aa7eb3306eb46768fb8737a4)#define BT\_SDP\_UINT8 0x08

[ 248](group__bt__sdp.md#ga1129f3a1364f29c9ce36f6f74ca21327)#define BT\_SDP\_UINT16 0x09

[ 249](group__bt__sdp.md#ga4f3bcb36dfce975c2d9ab68894a9e49c)#define BT\_SDP\_UINT32 0x0a

[ 250](group__bt__sdp.md#ga11261bf1c63a6d463ed41225c1e1a0c7)#define BT\_SDP\_UINT64 0x0b

[ 251](group__bt__sdp.md#ga9a815c6efe976f29e9f6f35a566245fd)#define BT\_SDP\_UINT128 0x0c

[ 252](group__bt__sdp.md#gaeed1818ca1bf762b23ab2bfcd18b8a66)#define BT\_SDP\_INT8 0x10

[ 253](group__bt__sdp.md#gaf6a3795d22cff4a522a2225339fb5a57)#define BT\_SDP\_INT16 0x11

[ 254](group__bt__sdp.md#ga0ad987ebeac3dab3ef2196f4dfeca1ab)#define BT\_SDP\_INT32 0x12

[ 255](group__bt__sdp.md#gaae793fef5690c6013e6e0e34ededb75f)#define BT\_SDP\_INT64 0x13

[ 256](group__bt__sdp.md#gaf754bbfd9cdc0e6a2bf7d6c46fab3f29)#define BT\_SDP\_INT128 0x14

[ 257](group__bt__sdp.md#ga4f829572cca9669a8a96a857874bb022)#define BT\_SDP\_UUID\_UNSPEC 0x18

[ 258](group__bt__sdp.md#ga45598f1c663acd3a3e5a409696cb3d2f)#define BT\_SDP\_UUID16 0x19

[ 259](group__bt__sdp.md#ga78245bb059feb3ec039e05aba24746e7)#define BT\_SDP\_UUID32 0x1a

[ 260](group__bt__sdp.md#gaadf48ba3e96687fff99ff58789d79a50)#define BT\_SDP\_UUID128 0x1c

[ 261](group__bt__sdp.md#gaca9942a42701cda835a5bf7b7aaf1d75)#define BT\_SDP\_TEXT\_STR\_UNSPEC 0x20

[ 262](group__bt__sdp.md#ga885ace6b1def91f3fa4dd16cb391d2b8)#define BT\_SDP\_TEXT\_STR8 0x25

[ 263](group__bt__sdp.md#gaa5301cdac5fc9299837f29b92aa3c10b)#define BT\_SDP\_TEXT\_STR16 0x26

[ 264](group__bt__sdp.md#ga29657a21117a3fbe05942778a8d7637e)#define BT\_SDP\_TEXT\_STR32 0x27

[ 265](group__bt__sdp.md#gac48f198f6609fac95db69c09ac69efab)#define BT\_SDP\_BOOL 0x28

[ 266](group__bt__sdp.md#gaa884191d772bfa24484cb33c0f614334)#define BT\_SDP\_SEQ\_UNSPEC 0x30

[ 267](group__bt__sdp.md#ga5a64e3bec70b40114a3160dbfb1e484b)#define BT\_SDP\_SEQ8 0x35

[ 268](group__bt__sdp.md#gadf5b15a0296a872ffefc24bbc90dc45b)#define BT\_SDP\_SEQ16 0x36

[ 269](group__bt__sdp.md#ga639e86b5103168917cb7202100e3124d)#define BT\_SDP\_SEQ32 0x37

[ 270](group__bt__sdp.md#gaee1bd735929cb2c4bca48cc7663407fd)#define BT\_SDP\_ALT\_UNSPEC 0x38

[ 271](group__bt__sdp.md#gab7460f41f05a418d58f4b6807d84cb40)#define BT\_SDP\_ALT8 0x3d

[ 272](group__bt__sdp.md#gab976bc87f0dcba0e4bc61575ea04ccc7)#define BT\_SDP\_ALT16 0x3e

[ 273](group__bt__sdp.md#ga420936f672ae31ca701ae277b69d592a)#define BT\_SDP\_ALT32 0x3f

[ 274](group__bt__sdp.md#ga32a7a79422f52b75c2eb2d2eb467dc00)#define BT\_SDP\_URL\_STR\_UNSPEC 0x40

[ 275](group__bt__sdp.md#gafb2a77d6097c8c4cf9f01b7e16df26f1)#define BT\_SDP\_URL\_STR8 0x45

[ 276](group__bt__sdp.md#gac1acc712468e5af1f54022ac3551882a)#define BT\_SDP\_URL\_STR16 0x46

[ 277](group__bt__sdp.md#ga37476681e9d4eee53b710c44e2da9a2f)#define BT\_SDP\_URL\_STR32 0x47

281

[ 282](group__bt__sdp.md#ga3eb2a5501341f6c5186a27219cf27cdf)#define BT\_SDP\_TYPE\_DESC\_MASK 0xf8

[ 283](group__bt__sdp.md#ga2d1040ccd11d1dd4c697525ebc323243)#define BT\_SDP\_SIZE\_DESC\_MASK 0x07

[ 284](group__bt__sdp.md#ga6e8f843aeb2d325058214d2a1454737a)#define BT\_SDP\_SIZE\_INDEX\_OFFSET 5

285

[ 287](structbt__sdp__data__elem.md)struct [bt\_sdp\_data\_elem](structbt__sdp__data__elem.md) {

[ 288](structbt__sdp__data__elem.md#ac6d5cbc71d1133f30bc20919ffd2d263) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__sdp__data__elem.md#ac6d5cbc71d1133f30bc20919ffd2d263);

[ 289](structbt__sdp__data__elem.md#a88b38121f91d55ca796dedb99b1e18d6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data\_size](structbt__sdp__data__elem.md#a88b38121f91d55ca796dedb99b1e18d6);

[ 290](structbt__sdp__data__elem.md#a8b7f4943ad968953edb7a3a6f541369b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [total\_size](structbt__sdp__data__elem.md#a8b7f4943ad968953edb7a3a6f541369b);

[ 291](structbt__sdp__data__elem.md#a0572a0c34ddf3ba340ee63d28c330dd1) const void \*[data](structbt__sdp__data__elem.md#a0572a0c34ddf3ba340ee63d28c330dd1);

292};

293

[ 295](structbt__sdp__attribute.md)struct [bt\_sdp\_attribute](structbt__sdp__attribute.md) {

[ 296](structbt__sdp__attribute.md#a1221009053aa7911ea82b3169ea330a1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structbt__sdp__attribute.md#a1221009053aa7911ea82b3169ea330a1);

[ 297](structbt__sdp__attribute.md#a424c2ae038fda8dfd96e2a9cd876f9a1) struct [bt\_sdp\_data\_elem](structbt__sdp__data__elem.md) [val](structbt__sdp__attribute.md#a424c2ae038fda8dfd96e2a9cd876f9a1);

298};

299

[ 301](structbt__sdp__record.md)struct [bt\_sdp\_record](structbt__sdp__record.md) {

[ 302](structbt__sdp__record.md#ae94becbbce55a43661ef0c563e314b6b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [handle](structbt__sdp__record.md#ae94becbbce55a43661ef0c563e314b6b);

[ 303](structbt__sdp__record.md#ad8ee5b17c45ca32696a492bc9c62d4fd) struct [bt\_sdp\_attribute](structbt__sdp__attribute.md) \*[attrs](structbt__sdp__record.md#ad8ee5b17c45ca32696a492bc9c62d4fd);

[ 304](structbt__sdp__record.md#a2bbcb54c385f88d512c1ccd4cf5e05ff) size\_t [attr\_count](structbt__sdp__record.md#a2bbcb54c385f88d512c1ccd4cf5e05ff);

[ 305](structbt__sdp__record.md#ad54ca76a96964df3a6ac909eb54274df) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [index](structbt__sdp__record.md#ad54ca76a96964df3a6ac909eb54274df);

[ 306](structbt__sdp__record.md#ab1e1b5a630a62ca892b7ff0bb7a00eea) struct [bt\_sdp\_record](structbt__sdp__record.md) \*[next](structbt__sdp__record.md#ab1e1b5a630a62ca892b7ff0bb7a00eea);

307};

308

309/\*

310 \* --------------------------------------------------- ------------------

311 \* | Service Hdl | Attr list ptr | Attr count | Next | -> | Service Hdl | ...

312 \* --------------------------------------------------- ------------------

313 \*/

314

[ 318](group__bt__sdp.md#gaef264fa3621c3df7a164128bb95b30fc)#define BT\_SDP\_ARRAY\_8(...) ((uint8\_t[]) {\_\_VA\_ARGS\_\_})

319

[ 323](group__bt__sdp.md#gaa4bb67164ae1f16b26081668d00f45c7)#define BT\_SDP\_ARRAY\_16(...) ((uint16\_t[]) {\_\_VA\_ARGS\_\_})

324

[ 328](group__bt__sdp.md#ga7a17ee4872190a087cf2e5ea4db9e737)#define BT\_SDP\_ARRAY\_32(...) ((uint32\_t[]) {\_\_VA\_ARGS\_\_})

329

[ 335](group__bt__sdp.md#ga66778ac38fb5b82d3b514fe0da008393)#define BT\_SDP\_TYPE\_SIZE(\_type) .type = \_type, \

336 .data\_size = BIT(\_type & BT\_SDP\_SIZE\_DESC\_MASK), \

337 .total\_size = BIT(\_type & BT\_SDP\_SIZE\_DESC\_MASK) + 1

338

[ 345](group__bt__sdp.md#gabbb2bd6a8321513082851fe73dfa44bc)#define BT\_SDP\_TYPE\_SIZE\_VAR(\_type, \_size) .type = \_type, \

346 .data\_size = \_size, \

347 .total\_size = BIT((\_type & BT\_SDP\_SIZE\_DESC\_MASK) - \

348 BT\_SDP\_SIZE\_INDEX\_OFFSET) + \_size + 1

349

[ 353](group__bt__sdp.md#gaa2954f3df4d0ee9684721cbc6182e37c)#define BT\_SDP\_DATA\_ELEM\_LIST(...) ((struct bt\_sdp\_data\_elem[]) {\_\_VA\_ARGS\_\_})

354

355

[ 364](group__bt__sdp.md#gaee13722587e4eb8c4beaaa0abad88fe5)#define BT\_SDP\_NEW\_SERVICE \

365{ \

366 BT\_SDP\_ATTR\_RECORD\_HANDLE, \

367 { BT\_SDP\_TYPE\_SIZE(BT\_SDP\_UINT32), BT\_SDP\_ARRAY\_32(0) } \

368}, \

369{ \

370 BT\_SDP\_ATTR\_RECORD\_STATE, \

371 { BT\_SDP\_TYPE\_SIZE(BT\_SDP\_UINT32), BT\_SDP\_ARRAY\_32(0) } \

372}, \

373{ \

374 BT\_SDP\_ATTR\_LANG\_BASE\_ATTR\_ID\_LIST, \

375 { BT\_SDP\_TYPE\_SIZE\_VAR(BT\_SDP\_SEQ8, 9), \

376 BT\_SDP\_DATA\_ELEM\_LIST( \

377 { BT\_SDP\_TYPE\_SIZE(BT\_SDP\_UINT16), BT\_SDP\_ARRAY\_8('n', 'e') }, \

378 { BT\_SDP\_TYPE\_SIZE(BT\_SDP\_UINT16), BT\_SDP\_ARRAY\_16(106) }, \

379 { BT\_SDP\_TYPE\_SIZE(BT\_SDP\_UINT16), \

380 BT\_SDP\_ARRAY\_16(BT\_SDP\_PRIMARY\_LANG\_BASE) } \

381 ), \

382 } \

383}, \

384{ \

385 BT\_SDP\_ATTR\_BROWSE\_GRP\_LIST, \

386 { BT\_SDP\_TYPE\_SIZE\_VAR(BT\_SDP\_SEQ8, 3), \

387 BT\_SDP\_DATA\_ELEM\_LIST( \

388 { BT\_SDP\_TYPE\_SIZE(BT\_SDP\_UUID16), \

389 BT\_SDP\_ARRAY\_16(BT\_SDP\_PUBLIC\_BROWSE\_GROUP) }, \

390 ), \

391 } \

392}

393

394

[ 404](group__bt__sdp.md#ga25b31454ee5b5fe23b617b5256ba00c4)#define BT\_SDP\_LIST(\_att\_id, \_type\_size, \_data\_elem\_seq) \

405{ \

406 \_att\_id, { \_type\_size, \_data\_elem\_seq } \

407}

408

[ 416](group__bt__sdp.md#gaa57f3c9a52ae29c02d7577be99f91e7c)#define BT\_SDP\_SERVICE\_ID(\_uuid) \

417{ \

418 BT\_SDP\_ATTR\_SERVICE\_ID, \

419 { BT\_SDP\_TYPE\_SIZE(BT\_SDP\_UUID16), &((struct bt\_uuid\_16) \_uuid) } \

420}

421

[ 429](group__bt__sdp.md#ga83de8e62415d3e31b3b5434b9db633d0)#define BT\_SDP\_SERVICE\_NAME(\_name) \

430{ \

431 BT\_SDP\_ATTR\_SVCNAME\_PRIMARY, \

432 { BT\_SDP\_TYPE\_SIZE\_VAR(BT\_SDP\_TEXT\_STR8, (sizeof(\_name)-1)), \_name } \

433}

434

[ 442](group__bt__sdp.md#ga096c84414b429aa05bed45cf6175361e)#define BT\_SDP\_SUPPORTED\_FEATURES(\_features) \

443{ \

444 BT\_SDP\_ATTR\_SUPPORTED\_FEATURES, \

445 { BT\_SDP\_TYPE\_SIZE(BT\_SDP\_UINT16), BT\_SDP\_ARRAY\_16(\_features) } \

446}

447

[ 455](group__bt__sdp.md#ga555f10b8f3ae3710c6dda9f37e78547b)#define BT\_SDP\_RECORD(\_attrs) \

456{ \

457 .attrs = \_attrs, \

458 .attr\_count = ARRAY\_SIZE((\_attrs)), \

459}

460

461/\* Server API \*/

462

[ 474](group__bt__sdp.md#ga6006e3cd593ef793273fb291913790fa)int [bt\_sdp\_register\_service](group__bt__sdp.md#ga6006e3cd593ef793273fb291913790fa)(struct [bt\_sdp\_record](structbt__sdp__record.md) \*service);

475

476/\* Client API \*/

477

[ 479](structbt__sdp__client__result.md)struct [bt\_sdp\_client\_result](structbt__sdp__client__result.md) {

[ 481](structbt__sdp__client__result.md#aa223dc666cbeaaebea462362188c531d) struct [net\_buf](structnet__buf.md) \*[resp\_buf](structbt__sdp__client__result.md#aa223dc666cbeaaebea462362188c531d);

[ 483](structbt__sdp__client__result.md#aa1d12c7e550773963691e3b40ec6dd8e) bool [next\_record\_hint](structbt__sdp__client__result.md#aa1d12c7e550773963691e3b40ec6dd8e);

[ 485](structbt__sdp__client__result.md#adf3dc871b32d50ed70bd27635bd176aa) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__sdp__client__result.md#adf3dc871b32d50ed70bd27635bd176aa);

486};

487

491enum {

[ 492](group__bt__sdp.md#gga278df12ff5def68ca4663defd178582ca990fbea48866b2acb7ccd67391b19636) [BT\_SDP\_DISCOVER\_UUID\_STOP](group__bt__sdp.md#gga278df12ff5def68ca4663defd178582ca990fbea48866b2acb7ccd67391b19636) = 0,

[ 493](group__bt__sdp.md#gga278df12ff5def68ca4663defd178582ca94e15ea86b69d65ca9c1947d1e2157ef) [BT\_SDP\_DISCOVER\_UUID\_CONTINUE](group__bt__sdp.md#gga278df12ff5def68ca4663defd178582ca94e15ea86b69d65ca9c1947d1e2157ef),

494};

495

[ 523](group__bt__sdp.md#gae5fa4166e3b909f9dcaace11b302f98f)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_sdp\_discover\_func\_t](group__bt__sdp.md#gae5fa4166e3b909f9dcaace11b302f98f))

524 (struct bt\_conn \*conn, struct [bt\_sdp\_client\_result](structbt__sdp__client__result.md) \*result);

525

[ 527](structbt__sdp__discover__params.md)struct [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md) {

528 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

[ 530](structbt__sdp__discover__params.md#a4c6073d7afda09be462902f5a95eaaed) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__sdp__discover__params.md#a4c6073d7afda09be462902f5a95eaaed);

[ 532](structbt__sdp__discover__params.md#a650143f0733958cf1186543c3469facc) [bt\_sdp\_discover\_func\_t](group__bt__sdp.md#gae5fa4166e3b909f9dcaace11b302f98f) [func](structbt__sdp__discover__params.md#a650143f0733958cf1186543c3469facc);

[ 534](structbt__sdp__discover__params.md#a6f8728e5b74211852e2ce8872c21e5fb) struct [net\_buf\_pool](structnet__buf__pool.md) \*[pool](structbt__sdp__discover__params.md#a6f8728e5b74211852e2ce8872c21e5fb);

535};

536

551

[ 552](group__bt__sdp.md#gaf49c299d269ee7b93d41e6ce71df9f77)int [bt\_sdp\_discover](group__bt__sdp.md#gaf49c299d269ee7b93d41e6ce71df9f77)(struct bt\_conn \*conn,

553 const struct [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md) \*params);

554

[ 565](group__bt__sdp.md#ga4659915e85ac2f440d6ea6be71f856fa)int [bt\_sdp\_discover\_cancel](group__bt__sdp.md#ga4659915e85ac2f440d6ea6be71f856fa)(struct bt\_conn \*conn,

566 const struct [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md) \*params);

567

568

569/\* Helper types & functions for SDP client to get essential data from server \*/

570

[ 572](group__bt__sdp.md#gaf01cb8d69aee9e06ab944ceae4d7df7c)enum [bt\_sdp\_proto](group__bt__sdp.md#gaf01cb8d69aee9e06ab944ceae4d7df7c) {

[ 573](group__bt__sdp.md#ggaf01cb8d69aee9e06ab944ceae4d7df7ca1ccc0f7ecd38ef83d6c1bb6afd72d71d) [BT\_SDP\_PROTO\_RFCOMM](group__bt__sdp.md#ggaf01cb8d69aee9e06ab944ceae4d7df7ca1ccc0f7ecd38ef83d6c1bb6afd72d71d) = 0x0003,

[ 574](group__bt__sdp.md#ggaf01cb8d69aee9e06ab944ceae4d7df7ca197184aa86b3777edca7c58e3597e688) [BT\_SDP\_PROTO\_L2CAP](group__bt__sdp.md#ggaf01cb8d69aee9e06ab944ceae4d7df7ca197184aa86b3777edca7c58e3597e688) = 0x0100,

575};

576

[ 589](group__bt__sdp.md#gaff14678f465af239ac79d1e34bdb9409)int [bt\_sdp\_get\_proto\_param](group__bt__sdp.md#gaff14678f465af239ac79d1e34bdb9409)(const struct [net\_buf](structnet__buf.md) \*buf, enum [bt\_sdp\_proto](group__bt__sdp.md#gaf01cb8d69aee9e06ab944ceae4d7df7c) proto,

590 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*param);

591

[ 608](group__bt__sdp.md#gacfcec85582954a80ba94822175d61092)int [bt\_sdp\_get\_addl\_proto\_param](group__bt__sdp.md#gacfcec85582954a80ba94822175d61092)(const struct [net\_buf](structnet__buf.md) \*buf, enum [bt\_sdp\_proto](group__bt__sdp.md#gaf01cb8d69aee9e06ab944ceae4d7df7c) proto,

609 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) param\_index, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*param);

610

[ 623](group__bt__sdp.md#ga9e7d4bd0a407fe8254410f907db90f00)int [bt\_sdp\_get\_profile\_version](group__bt__sdp.md#ga9e7d4bd0a407fe8254410f907db90f00)(const struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) profile,

624 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*version);

625

[ 636](group__bt__sdp.md#gae1c3110dfe24a939cc02d998c4699ca7)int [bt\_sdp\_get\_features](group__bt__sdp.md#gae1c3110dfe24a939cc02d998c4699ca7)(const struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*features);

637

638#ifdef \_\_cplusplus

639}

640#endif

641

645

646#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SDP\_H\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_sdp\_discover\_cancel](group__bt__sdp.md#ga4659915e85ac2f440d6ea6be71f856fa)

int bt\_sdp\_discover\_cancel(struct bt\_conn \*conn, const struct bt\_sdp\_discover\_params \*params)

Release waiting SDP discovery request.

[bt\_sdp\_register\_service](group__bt__sdp.md#ga6006e3cd593ef793273fb291913790fa)

int bt\_sdp\_register\_service(struct bt\_sdp\_record \*service)

Register a Service Record.

[bt\_sdp\_get\_profile\_version](group__bt__sdp.md#ga9e7d4bd0a407fe8254410f907db90f00)

int bt\_sdp\_get\_profile\_version(const struct net\_buf \*buf, uint16\_t profile, uint16\_t \*version)

Get profile version.

[bt\_sdp\_get\_addl\_proto\_param](group__bt__sdp.md#gacfcec85582954a80ba94822175d61092)

int bt\_sdp\_get\_addl\_proto\_param(const struct net\_buf \*buf, enum bt\_sdp\_proto proto, uint8\_t param\_index, uint16\_t \*param)

Get additional parameter value related to given stacked protocol UUID.

[bt\_sdp\_get\_features](group__bt__sdp.md#gae1c3110dfe24a939cc02d998c4699ca7)

int bt\_sdp\_get\_features(const struct net\_buf \*buf, uint16\_t \*features)

Get SupportedFeatures attribute value.

[bt\_sdp\_discover\_func\_t](group__bt__sdp.md#gae5fa4166e3b909f9dcaace11b302f98f)

uint8\_t(\* bt\_sdp\_discover\_func\_t)(struct bt\_conn \*conn, struct bt\_sdp\_client\_result \*result)

Callback type reporting to user that there is a resolved result on remote for given UUID and the resu...

**Definition** sdp.h:524

[bt\_sdp\_proto](group__bt__sdp.md#gaf01cb8d69aee9e06ab944ceae4d7df7c)

bt\_sdp\_proto

Protocols to be asked about specific parameters.

**Definition** sdp.h:572

[bt\_sdp\_discover](group__bt__sdp.md#gaf49c299d269ee7b93d41e6ce71df9f77)

int bt\_sdp\_discover(struct bt\_conn \*conn, const struct bt\_sdp\_discover\_params \*params)

Allows user to start SDP discovery session.

[bt\_sdp\_get\_proto\_param](group__bt__sdp.md#gaff14678f465af239ac79d1e34bdb9409)

int bt\_sdp\_get\_proto\_param(const struct net\_buf \*buf, enum bt\_sdp\_proto proto, uint16\_t \*param)

Give to user parameter value related to given stacked protocol UUID.

[BT\_SDP\_DISCOVER\_UUID\_CONTINUE](group__bt__sdp.md#gga278df12ff5def68ca4663defd178582ca94e15ea86b69d65ca9c1947d1e2157ef)

@ BT\_SDP\_DISCOVER\_UUID\_CONTINUE

**Definition** sdp.h:493

[BT\_SDP\_DISCOVER\_UUID\_STOP](group__bt__sdp.md#gga278df12ff5def68ca4663defd178582ca990fbea48866b2acb7ccd67391b19636)

@ BT\_SDP\_DISCOVER\_UUID\_STOP

**Definition** sdp.h:492

[BT\_SDP\_PROTO\_L2CAP](group__bt__sdp.md#ggaf01cb8d69aee9e06ab944ceae4d7df7ca197184aa86b3777edca7c58e3597e688)

@ BT\_SDP\_PROTO\_L2CAP

**Definition** sdp.h:574

[BT\_SDP\_PROTO\_RFCOMM](group__bt__sdp.md#ggaf01cb8d69aee9e06ab944ceae4d7df7ca1ccc0f7ecd38ef83d6c1bb6afd72d71d)

@ BT\_SDP\_PROTO\_RFCOMM

**Definition** sdp.h:573

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_sdp\_attribute](structbt__sdp__attribute.md)

SDP Attribute Value.

**Definition** sdp.h:295

[bt\_sdp\_attribute::id](structbt__sdp__attribute.md#a1221009053aa7911ea82b3169ea330a1)

uint16\_t id

Attribute ID.

**Definition** sdp.h:296

[bt\_sdp\_attribute::val](structbt__sdp__attribute.md#a424c2ae038fda8dfd96e2a9cd876f9a1)

struct bt\_sdp\_data\_elem val

Attribute data.

**Definition** sdp.h:297

[bt\_sdp\_client\_result](structbt__sdp__client__result.md)

Generic SDP Client Query Result data holder.

**Definition** sdp.h:479

[bt\_sdp\_client\_result::next\_record\_hint](structbt__sdp__client__result.md#aa1d12c7e550773963691e3b40ec6dd8e)

bool next\_record\_hint

flag pointing that there are more result chunks for given UUID

**Definition** sdp.h:483

[bt\_sdp\_client\_result::resp\_buf](structbt__sdp__client__result.md#aa223dc666cbeaaebea462362188c531d)

struct net\_buf \* resp\_buf

buffer containing unparsed SDP record result for given UUID

**Definition** sdp.h:481

[bt\_sdp\_client\_result::uuid](structbt__sdp__client__result.md#adf3dc871b32d50ed70bd27635bd176aa)

const struct bt\_uuid \* uuid

Reference to UUID object on behalf one discovery was started.

**Definition** sdp.h:485

[bt\_sdp\_data\_elem](structbt__sdp__data__elem.md)

SDP Generic Data Element Value.

**Definition** sdp.h:287

[bt\_sdp\_data\_elem::data](structbt__sdp__data__elem.md#a0572a0c34ddf3ba340ee63d28c330dd1)

const void \* data

**Definition** sdp.h:291

[bt\_sdp\_data\_elem::data\_size](structbt__sdp__data__elem.md#a88b38121f91d55ca796dedb99b1e18d6)

uint32\_t data\_size

Size of the data element.

**Definition** sdp.h:289

[bt\_sdp\_data\_elem::total\_size](structbt__sdp__data__elem.md#a8b7f4943ad968953edb7a3a6f541369b)

uint32\_t total\_size

Total size of the data element.

**Definition** sdp.h:290

[bt\_sdp\_data\_elem::type](structbt__sdp__data__elem.md#ac6d5cbc71d1133f30bc20919ffd2d263)

uint8\_t type

Type of the data element.

**Definition** sdp.h:288

[bt\_sdp\_discover\_params](structbt__sdp__discover__params.md)

Main user structure used in SDP discovery of remote.

**Definition** sdp.h:527

[bt\_sdp\_discover\_params::uuid](structbt__sdp__discover__params.md#a4c6073d7afda09be462902f5a95eaaed)

const struct bt\_uuid \* uuid

UUID (service) to be discovered on remote SDP entity.

**Definition** sdp.h:530

[bt\_sdp\_discover\_params::func](structbt__sdp__discover__params.md#a650143f0733958cf1186543c3469facc)

bt\_sdp\_discover\_func\_t func

Discover callback to be called on resolved SDP record.

**Definition** sdp.h:532

[bt\_sdp\_discover\_params::pool](structbt__sdp__discover__params.md#a6f8728e5b74211852e2ce8872c21e5fb)

struct net\_buf\_pool \* pool

Memory buffer enabled by user for SDP query results.

**Definition** sdp.h:534

[bt\_sdp\_record](structbt__sdp__record.md)

SDP Service Record Value.

**Definition** sdp.h:301

[bt\_sdp\_record::attr\_count](structbt__sdp__record.md#a2bbcb54c385f88d512c1ccd4cf5e05ff)

size\_t attr\_count

Number of attributes.

**Definition** sdp.h:304

[bt\_sdp\_record::next](structbt__sdp__record.md#ab1e1b5a630a62ca892b7ff0bb7a00eea)

struct bt\_sdp\_record \* next

Next service record.

**Definition** sdp.h:306

[bt\_sdp\_record::index](structbt__sdp__record.md#ad54ca76a96964df3a6ac909eb54274df)

uint8\_t index

Index of the record in LL.

**Definition** sdp.h:305

[bt\_sdp\_record::attrs](structbt__sdp__record.md#ad8ee5b17c45ca32696a492bc9c62d4fd)

struct bt\_sdp\_attribute \* attrs

Base addr of attr array.

**Definition** sdp.h:303

[bt\_sdp\_record::handle](structbt__sdp__record.md#ae94becbbce55a43661ef0c563e314b6b)

uint32\_t handle

Redundant, for quick ref.

**Definition** sdp.h:302

[bt\_uuid](structbt__uuid.md)

This is a 'tentative' type and should be used as a pointer only.

**Definition** uuid.h:49

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** buf.h:1076

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:1004

[uuid.h](uuid_8h.md)

Bluetooth UUID handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [sdp.h](sdp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
