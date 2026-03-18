---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/input-event-codes_8h_source.html
original_path: doxygen/html/input-event-codes_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input-event-codes.h

[Go to the documentation of this file.](input-event-codes_8h.md)

1/\*

2 \* Copyright 2023 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*

6 \* Input event codes, for codes available in Linux, use the same values as in

7 \* https://elixir.bootlin.com/linux/latest/source/include/uapi/linux/input-event-codes.h

8 \*/

9

10#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INPUT\_INPUT\_EVENT\_CODES\_H\_

11#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INPUT\_INPUT\_EVENT\_CODES\_H\_

12

18

19

[ 25](group__input__events.md#ga4a517c31bdbdd1bd82ba456d256ef1f1)#define INPUT\_EV\_KEY 0x01

[ 26](group__input__events.md#ga02de6c85efab3d21eb81e88e54d58e03)#define INPUT\_EV\_REL 0x02

[ 27](group__input__events.md#gaa6bcd6755fbdb3eb103f03a72759ce4f)#define INPUT\_EV\_ABS 0x03

[ 28](group__input__events.md#ga40ab1faa2e28e32c30016ad854afa6cf)#define INPUT\_EV\_MSC 0x04

[ 29](group__input__events.md#ga7037a9ea2e0a63c40a5d206e507e5f42)#define INPUT\_EV\_VENDOR\_START 0xf0

[ 30](group__input__events.md#gaa19a341e18ff5c43e1b8ddf58c7b9676)#define INPUT\_EV\_VENDOR\_STOP 0xff

32

[ 38](group__input__events.md#ga94e5a0d74dad76e57679b97af90ecb65)#define INPUT\_KEY\_RESERVED 0

39

[ 40](group__input__events.md#gab41cb2f1768b0a0667ab6509b6d3af21)#define INPUT\_KEY\_0 11

[ 41](group__input__events.md#gad62520853a15b74d68c1bab5a3119eaa)#define INPUT\_KEY\_1 2

[ 42](group__input__events.md#gadb02e289d07d4d4457c88b1ada7e2534)#define INPUT\_KEY\_2 3

[ 43](group__input__events.md#ga95a246cefcaafd26d15c1c124bdf2ca4)#define INPUT\_KEY\_3 4

[ 44](group__input__events.md#ga0c16c2e62a65eab0fe8952a4cf60254d)#define INPUT\_KEY\_4 5

[ 45](group__input__events.md#ga386e2c69d5e5a9549668b1a2a2d297e1)#define INPUT\_KEY\_5 6

[ 46](group__input__events.md#ga87e0cea90040710253718ce29c407f3e)#define INPUT\_KEY\_6 7

[ 47](group__input__events.md#ga090686eaaacddb8c2f58b31b4b9801b8)#define INPUT\_KEY\_7 8

[ 48](group__input__events.md#ga6f2b66c0eea17b044778a326ffcd3f57)#define INPUT\_KEY\_8 9

[ 49](group__input__events.md#ga91473de481c47f3f9e40caf42e49250f)#define INPUT\_KEY\_9 10

[ 50](group__input__events.md#ga553b457efaafb3cdc41e7b1e953cd6fe)#define INPUT\_KEY\_A 30

[ 51](group__input__events.md#gaa528a10eb85fa9dc46198e08962fab3a)#define INPUT\_KEY\_APOSTROPHE 40

[ 52](group__input__events.md#gaaae2c60e8907c14c094e5c1c4e3dae3b)#define INPUT\_KEY\_B 48

[ 53](group__input__events.md#gab5ad87c6e97f6b09f9dc1a1570a9c299)#define INPUT\_KEY\_BACK 158

[ 54](group__input__events.md#ga180fcae595fbc580bfe1a94414a4b02b)#define INPUT\_KEY\_BACKSLASH 43

[ 55](group__input__events.md#ga654ffbdc8f2fef696ee0237704cebc34)#define INPUT\_KEY\_BACKSPACE 14

[ 56](group__input__events.md#ga26f6330d7631bdae0f2bb34f623a85ae)#define INPUT\_KEY\_BLUETOOTH 237

[ 57](group__input__events.md#gac4afc3e97b18a1f22e3d59730177e27f)#define INPUT\_KEY\_BRIGHTNESSDOWN 224

[ 58](group__input__events.md#gaff59e776a3e3a0fe4d32caeb41a32c53)#define INPUT\_KEY\_BRIGHTNESSUP 225

[ 59](group__input__events.md#ga1b88afc2eacfbbd778785398baebd287)#define INPUT\_KEY\_C 46

[ 60](group__input__events.md#ga8dfa14142766962272afc77538f8a909)#define INPUT\_KEY\_CAPSLOCK 58

[ 61](group__input__events.md#ga345dc788101108c27f488cfa0fc885c8)#define INPUT\_KEY\_COFFEE 152

[ 62](group__input__events.md#ga1220a9e90676992fcd3c308a7f1038f7)#define INPUT\_KEY\_COMMA 51

[ 63](group__input__events.md#ga52882fff91dc0c288cf0b60baa60be65)#define INPUT\_KEY\_COMPOSE 127

[ 64](group__input__events.md#gaedf1f55d35163e56ca03f4409ea6b7d0)#define INPUT\_KEY\_CONNECT 218

[ 65](group__input__events.md#ga206eda236c1ce08e3ad6eef192ac303e)#define INPUT\_KEY\_D 32

[ 66](group__input__events.md#ga2abef21124d504927c675959331a4c3b)#define INPUT\_KEY\_DELETE 111

[ 67](group__input__events.md#gacbd30145c479c472d105a0c5251c0e4d)#define INPUT\_KEY\_DOT 52

[ 68](group__input__events.md#gad80b82e35e50f775a091b8f5031d2c9b)#define INPUT\_KEY\_DOWN 108

[ 69](group__input__events.md#ga4c1a1f169d8159ed36b194ae3d0aa0e7)#define INPUT\_KEY\_E 18

[ 70](group__input__events.md#gaff91435e45612b50955523d029dfd1e4)#define INPUT\_KEY\_END 107

[ 71](group__input__events.md#ga8e4e6c4072fd5595a80a4e4ff1ae1c32)#define INPUT\_KEY\_ENTER 28

[ 72](group__input__events.md#ga0775ec23155f396f368425fb4dc35e54)#define INPUT\_KEY\_EQUAL 13

[ 73](group__input__events.md#ga2026ab8608c7013781cdcf1e546e4d93)#define INPUT\_KEY\_ESC 1

[ 74](group__input__events.md#gaed15f4e46a5e80bd9d8508f2f0317386)#define INPUT\_KEY\_F 33

[ 75](group__input__events.md#ga06374b0c4c42d708874d799afac87f54)#define INPUT\_KEY\_F1 59

[ 76](group__input__events.md#ga925bd568cbef2c8241a8bc38cd1fc0ee)#define INPUT\_KEY\_F10 68

[ 77](group__input__events.md#gaf8db5439ca4244843ddea6c78e235227)#define INPUT\_KEY\_F11 87

[ 78](group__input__events.md#gac206e26c278998da99fc7907f2d68d90)#define INPUT\_KEY\_F12 88

[ 79](group__input__events.md#gafe37c9d54407b3401974a400831d9200)#define INPUT\_KEY\_F13 183

[ 80](group__input__events.md#ga57112c273fb46a4f748047953355e430)#define INPUT\_KEY\_F14 184

[ 81](group__input__events.md#ga379756870b1a1d808f97f60cf2d3ecc5)#define INPUT\_KEY\_F15 185

[ 82](group__input__events.md#ga0336cf1cdcaa5ee62c1a4a7d7b5f94b0)#define INPUT\_KEY\_F16 186

[ 83](group__input__events.md#ga15ae8eaffd7978c3d91fe05bfedaec0d)#define INPUT\_KEY\_F17 187

[ 84](group__input__events.md#gaf58e8117aadc979c00e99e5d2944e572)#define INPUT\_KEY\_F18 188

[ 85](group__input__events.md#ga45127f8182970453761bea5703e164ca)#define INPUT\_KEY\_F19 189

[ 86](group__input__events.md#gae7ea4afc3ee03cba0820e1230a1bc844)#define INPUT\_KEY\_F2 60

[ 87](group__input__events.md#gaa0d8d5c8f17f26a6571bd50acd7e7c56)#define INPUT\_KEY\_F20 190

[ 88](group__input__events.md#ga958fc836aa61bd04731563b97b3f2c3b)#define INPUT\_KEY\_F21 191

[ 89](group__input__events.md#ga9f865f6f67f7ad3e747450cbe7bd001b)#define INPUT\_KEY\_F22 192

[ 90](group__input__events.md#ga201402a9046f510fcc818fc281acdd74)#define INPUT\_KEY\_F23 193

[ 91](group__input__events.md#gade48ffdee4f9fc816467f61444e388d4)#define INPUT\_KEY\_F24 194

[ 92](group__input__events.md#gaa186203f9efabb0868348938e5eabcfd)#define INPUT\_KEY\_F3 61

[ 93](group__input__events.md#gace5db941d06022b3b33dd9e72a799b68)#define INPUT\_KEY\_F4 62

[ 94](group__input__events.md#ga5ab64f326303e6b097eac8f9a1827feb)#define INPUT\_KEY\_F5 63

[ 95](group__input__events.md#ga3f8d3788cd179ffb9d68de85e23ee1b0)#define INPUT\_KEY\_F6 64

[ 96](group__input__events.md#ga647c9e3d15d4866c3ae486b09f6182fa)#define INPUT\_KEY\_F7 65

[ 97](group__input__events.md#ga6a1be4c1720c9bbd18950ba7d9b91042)#define INPUT\_KEY\_F8 66

[ 98](group__input__events.md#ga16baac9275d3b860e117705aba632681)#define INPUT\_KEY\_F9 67

[ 99](group__input__events.md#ga6c9a01c0a070b213af72cb8088e75876)#define INPUT\_KEY\_FASTFORWARD 208

[ 100](group__input__events.md#gad64d70c2ccc65f5189666efa0847ca7a)#define INPUT\_KEY\_FORWARD 159

[ 101](group__input__events.md#ga5480ba49acaa553a194984a98b92f552)#define INPUT\_KEY\_G 34

[ 102](group__input__events.md#ga1aaa62276091bde62d4e5aa872902559)#define INPUT\_KEY\_GRAVE 41

[ 103](group__input__events.md#ga3014cf5abad3b71a0ae45b5b7c713f38)#define INPUT\_KEY\_H 35

[ 104](group__input__events.md#gaa8314d1e4f4ca225922f039791b36d42)#define INPUT\_KEY\_HOME 102

[ 105](group__input__events.md#ga6c987aa5736663b7f309f2b2fb9423c5)#define INPUT\_KEY\_I 23

[ 106](group__input__events.md#gabfa379fe24dd23461e435de41c23864d)#define INPUT\_KEY\_INSERT 110

[ 107](group__input__events.md#ga7d5c3e334909eb4b2c76217b69a61260)#define INPUT\_KEY\_J 36

[ 108](group__input__events.md#ga8cb73e35923639e77e861631565134df)#define INPUT\_KEY\_K 37

[ 109](group__input__events.md#ga8e5438fce6c7a717da4322de2982a2ed)#define INPUT\_KEY\_KP0 82

[ 110](group__input__events.md#gaa5b65c8ff4b94208ff434f3ed8c9f1f1)#define INPUT\_KEY\_KP1 79

[ 111](group__input__events.md#gad50d9044613b97c6d6292afe15cceb06)#define INPUT\_KEY\_KP2 80

[ 112](group__input__events.md#ga8a084e91c2906b1f8dd43939293d4812)#define INPUT\_KEY\_KP3 81

[ 113](group__input__events.md#ga1a9ca528816497bf32bee4e524d2977c)#define INPUT\_KEY\_KP4 75

[ 114](group__input__events.md#ga83e04456cf68db301973d09af1a19641)#define INPUT\_KEY\_KP5 76

[ 115](group__input__events.md#gabd7a6dc0d9440de1ffef2a3643583966)#define INPUT\_KEY\_KP6 77

[ 116](group__input__events.md#ga58709627a1190549d0e0004e4b5bcd74)#define INPUT\_KEY\_KP7 71

[ 117](group__input__events.md#ga94e64bbd09dda7434d8a9f086daca1a7)#define INPUT\_KEY\_KP8 72

[ 118](group__input__events.md#ga7dda283e4603e0ce4d14a9a87ea74c4f)#define INPUT\_KEY\_KP9 73

[ 119](group__input__events.md#gaa0c33b6ba975617f93230aa75a49fef5)#define INPUT\_KEY\_KPASTERISK 55

[ 120](group__input__events.md#gabb3767d06adbe20b3fb580e8816f916f)#define INPUT\_KEY\_KPCOMMA 121

[ 121](group__input__events.md#gac6c07467b6202089166c56c498fd4b27)#define INPUT\_KEY\_KPDOT 83

[ 122](group__input__events.md#gae8fd841f81d29788d5d0b602538bbd0e)#define INPUT\_KEY\_KPENTER 96

[ 123](group__input__events.md#gaefdae376c1daf752b698efaf89a07b18)#define INPUT\_KEY\_KPEQUAL 117

[ 124](group__input__events.md#gad4f23f54ec4f2252864c507e09ad9cea)#define INPUT\_KEY\_KPMINUS 74

[ 125](group__input__events.md#ga3d6307d0237d8f34a3d448dc9e40528f)#define INPUT\_KEY\_KPPLUS 78

[ 126](group__input__events.md#ga21a77384e45feb96ecc322032dc7231e)#define INPUT\_KEY\_KPPLUSMINUS 118

[ 127](group__input__events.md#gab3f0ce8548cef85df2672d09d021fe39)#define INPUT\_KEY\_KPSLASH 98

[ 128](group__input__events.md#gad79329b4b6c3eaad43aabac8c3538622)#define INPUT\_KEY\_L 38

[ 129](group__input__events.md#gae8c0a4811cd2056d0b6885239d635492)#define INPUT\_KEY\_LEFT 105

[ 130](group__input__events.md#ga8d384257be19e2eb0d807d35f2656f16)#define INPUT\_KEY\_LEFTALT 56

[ 131](group__input__events.md#gaecdffb7aff0fee1e078319a23a97e10e)#define INPUT\_KEY\_LEFTBRACE 26

[ 132](group__input__events.md#ga1bc52bc876c50da66cc292f250603db7)#define INPUT\_KEY\_LEFTCTRL 29

[ 133](group__input__events.md#gad18b505a7f718887f932a5b7fedfecd3)#define INPUT\_KEY\_LEFTMETA 125

[ 134](group__input__events.md#gacaf73383130558303396a7add94bdafd)#define INPUT\_KEY\_LEFTSHIFT 42

[ 135](group__input__events.md#ga7c8f628eb719d1d4b428805914c376a7)#define INPUT\_KEY\_M 50

[ 136](group__input__events.md#gab159cae18818e930e4d928ebcc206651)#define INPUT\_KEY\_MENU 139

[ 137](group__input__events.md#gae9779c5f21b9e14e5cbe1db8c5073819)#define INPUT\_KEY\_MINUS 12

[ 138](group__input__events.md#ga8554adab31fc9c20c9de01bcb2aff839)#define INPUT\_KEY\_MUTE 113

[ 139](group__input__events.md#ga09c0c860ee76803bb317dbac1072cd1d)#define INPUT\_KEY\_N 49

[ 140](group__input__events.md#ga93e220e43b3d33ffa985445f6dbf9c3c)#define INPUT\_KEY\_NUMLOCK 69

[ 141](group__input__events.md#gae964cb377e0bcd958dad6da9626d298c)#define INPUT\_KEY\_O 24

[ 142](group__input__events.md#ga396def37642dee65c74c48ff72aaa53d)#define INPUT\_KEY\_P 25

[ 143](group__input__events.md#gaf6bc999ac2a136235fe95803c6df73c1)#define INPUT\_KEY\_PAGEDOWN 109

[ 144](group__input__events.md#gaebb169acd4c3ce873353fd595364b374)#define INPUT\_KEY\_PAGEUP 104

[ 145](group__input__events.md#ga08319efd258cd774ff8bc964c5a402dd)#define INPUT\_KEY\_PAUSE 119

[ 146](group__input__events.md#ga1a377fdb1967aeff84e96d47c71bcf41)#define INPUT\_KEY\_PLAY 207

[ 147](group__input__events.md#ga2b05b5429ef1b0dc37698b82201d257d)#define INPUT\_KEY\_POWER 116

[ 148](group__input__events.md#ga4927612cf9f69324b15d8d9e46ab3326)#define INPUT\_KEY\_PRINT 210

[ 149](group__input__events.md#ga9ee8d6012d74e489ee8072f71497a36e)#define INPUT\_KEY\_Q 16

[ 150](group__input__events.md#ga421f14c501d86ed907ed4249f93a9e7e)#define INPUT\_KEY\_R 19

[ 151](group__input__events.md#ga1bf6f292c1ab3ca25001b4ef4ca2626b)#define INPUT\_KEY\_RIGHT 106

[ 152](group__input__events.md#gac02b6a2133d5ddf8847e1ce94250536f)#define INPUT\_KEY\_RIGHTALT 100

[ 153](group__input__events.md#gaa0802d3471f6c774d37a8827e632d7fb)#define INPUT\_KEY\_RIGHTBRACE 27

[ 154](group__input__events.md#gabb2e15ee9c30a649c92e82c42f513a35)#define INPUT\_KEY\_RIGHTCTRL 97

[ 155](group__input__events.md#ga23ebc28da84872b585c9dcfeb057bfc9)#define INPUT\_KEY\_RIGHTMETA 126

[ 156](group__input__events.md#ga4fce26a4ffc693507043c1cfe95d279d)#define INPUT\_KEY\_RIGHTSHIFT 54

[ 157](group__input__events.md#gadefb5566a41148a0df4dd95cb2c5e2d2)#define INPUT\_KEY\_S 31

[ 158](group__input__events.md#ga32491acdefb2e9f0eab5e7fc5755d2bc)#define INPUT\_KEY\_SCALE 120

[ 159](group__input__events.md#ga1d0958d93ddb7f3ff662e84a06c95a7c)#define INPUT\_KEY\_SCROLLLOCK 70

[ 160](group__input__events.md#ga7d45c7e2399dc6b20b6e470cb35d1dd6)#define INPUT\_KEY\_SEMICOLON 39

[ 161](group__input__events.md#gab17a459ab34d1353809c1a7360db3818)#define INPUT\_KEY\_SLASH 53

[ 162](group__input__events.md#gaf826720ad8af092655351c0527b849df)#define INPUT\_KEY\_SLEEP 142

[ 163](group__input__events.md#ga4d6d5af48ea84fbea0df2fcb38ac7812)#define INPUT\_KEY\_SPACE 57

[ 164](group__input__events.md#ga41b7f92a09624c06eee3a3650ac36139)#define INPUT\_KEY\_SYSRQ 99

[ 165](group__input__events.md#gadc43d9d7846b0e87dc217dcab831e4fe)#define INPUT\_KEY\_T 20

[ 166](group__input__events.md#gac38db99311ad987f019f16e601a6911d)#define INPUT\_KEY\_TAB 15

[ 167](group__input__events.md#gab6403be2f0b9b60f626a57e5c9ed2666)#define INPUT\_KEY\_U 22

[ 168](group__input__events.md#ga01e7f6a6aee5972612536c70a84db848)#define INPUT\_KEY\_UP 103

[ 169](group__input__events.md#ga74c693d33698eac543ee6ad4943c2d81)#define INPUT\_KEY\_UWB 239

[ 170](group__input__events.md#ga9f37deb8d631a8705cc0506d9b46b42c)#define INPUT\_KEY\_V 47

[ 171](group__input__events.md#ga36b4c1340f9d7c5374e4fbe82244d492)#define INPUT\_KEY\_VOLUMEDOWN 114

[ 172](group__input__events.md#gaa876076df525fa996dbced370c1be2e3)#define INPUT\_KEY\_VOLUMEUP 115

[ 173](group__input__events.md#gaafc7f5b6c9d8f7ef13527ce60c08d36d)#define INPUT\_KEY\_W 17

[ 174](group__input__events.md#gaeba4b122e3850b8c96e803353ac7bd35)#define INPUT\_KEY\_WAKEUP 143

[ 175](group__input__events.md#gae008f06aa7ca74912fe8ebbcd3dda45f)#define INPUT\_KEY\_WLAN 238

[ 176](group__input__events.md#ga8665fe56c47f02bd98793674dbc145b9)#define INPUT\_KEY\_X 45

[ 177](group__input__events.md#gae86058bcd4e4a5393b35253176dc498f)#define INPUT\_KEY\_Y 21

[ 178](group__input__events.md#ga32a1603a3c0127e6ebe059af32314273)#define INPUT\_KEY\_Z 44

180

181

[ 187](group__input__events.md#ga30976f1bb4418fccbae30a56f714bea1)#define INPUT\_BTN\_0 0x100

[ 188](group__input__events.md#ga1f76026fc79560722aaf95aee0985705)#define INPUT\_BTN\_1 0x101

[ 189](group__input__events.md#ga73129f8a7a6216f629f3d3b3433c4430)#define INPUT\_BTN\_2 0x102

[ 190](group__input__events.md#gae8651f9708cb6def0e64094542018b6e)#define INPUT\_BTN\_3 0x103

[ 191](group__input__events.md#ga11b176175bd1ff1d062d2dfc111c80f3)#define INPUT\_BTN\_4 0x104

[ 192](group__input__events.md#ga9ea411071196ca3e90df6bbfbb48cf57)#define INPUT\_BTN\_5 0x105

[ 193](group__input__events.md#ga66d852c7078d65fcb2e34cee8a5fcd61)#define INPUT\_BTN\_6 0x106

[ 194](group__input__events.md#ga55330f8419dacc72404607f4abd2ac3e)#define INPUT\_BTN\_7 0x107

[ 195](group__input__events.md#gab92962cc2fd0784c1afbf0ed036a92a4)#define INPUT\_BTN\_8 0x108

[ 196](group__input__events.md#ga790321e6da41ee0dfe7550b03166f514)#define INPUT\_BTN\_9 0x109

[ 197](group__input__events.md#ga1e7a8c57c7a0a33cd3311ee141a0836c)#define INPUT\_BTN\_A BTN\_SOUTH

[ 198](group__input__events.md#gae4355ae2a831823486b28388a78dd964)#define INPUT\_BTN\_B BTN\_EAST

[ 199](group__input__events.md#ga1aae01791507acfc119387d7600e8e6a)#define INPUT\_BTN\_BACK 0x116

[ 200](group__input__events.md#ga0e20c12420205d110a4e20c3a798cd8f)#define INPUT\_BTN\_C 0x132

[ 201](group__input__events.md#ga912a826581f671fbc3f04b9bb2582432)#define INPUT\_BTN\_DPAD\_DOWN 0x221

[ 202](group__input__events.md#ga7360624be8436db1e33ecc62e4e74b14)#define INPUT\_BTN\_DPAD\_LEFT 0x222

[ 203](group__input__events.md#gabcf0e865e8c374ec77ef8bd3abf23117)#define INPUT\_BTN\_DPAD\_RIGHT 0x223

[ 204](group__input__events.md#ga3b2879d72a2e4a4292442cee04f6a5c6)#define INPUT\_BTN\_DPAD\_UP 0x220

[ 205](group__input__events.md#gae57dc96a45c1a29169a6df702bb70cb7)#define INPUT\_BTN\_EAST 0x131

[ 206](group__input__events.md#ga296364e72a76c9d03729b35ff64a3ea3)#define INPUT\_BTN\_EXTRA 0x114

[ 207](group__input__events.md#ga1483e1ef939172b42b98be83961d3668)#define INPUT\_BTN\_FORWARD 0x115

[ 208](group__input__events.md#gac1810029daec295ab8df9c2463c3b12d)#define INPUT\_BTN\_GEAR\_DOWN 0x150

[ 209](group__input__events.md#ga5f84880e2febbd344348a235cba670d1)#define INPUT\_BTN\_GEAR\_UP 0x151

[ 210](group__input__events.md#ga391066a02e4297af7c214031037aeb3e)#define INPUT\_BTN\_LEFT 0x110

[ 211](group__input__events.md#ga86b7c6fbd3e37e21bd6b0fb379c89b44)#define INPUT\_BTN\_MIDDLE 0x112

[ 212](group__input__events.md#ga0b1db382e01c7d8f88dd531625f4b759)#define INPUT\_BTN\_MODE 0x13c

[ 213](group__input__events.md#gab1378ad64c11487f0f607d039db61d82)#define INPUT\_BTN\_NORTH 0x133

[ 214](group__input__events.md#ga300d9d3924d22f27180272908f6ad8db)#define INPUT\_BTN\_RIGHT 0x111

[ 215](group__input__events.md#gaad0c944797cd368eca5f6753326fe28a)#define INPUT\_BTN\_SELECT 0x13a

[ 216](group__input__events.md#gaf34f37dd3c5ef85af7805c1a307bdcc4)#define INPUT\_BTN\_SIDE 0x113

[ 217](group__input__events.md#ga5bbd97c212dbd08288cbdf1dc1a64cb5)#define INPUT\_BTN\_SOUTH 0x130

[ 218](group__input__events.md#ga874350c63269e66869d3424d108bf891)#define INPUT\_BTN\_START 0x13b

[ 219](group__input__events.md#ga14273a631fbaec99bf96c7929034cb2d)#define INPUT\_BTN\_TASK 0x117

[ 220](group__input__events.md#ga5809e3b7e5f922904b5177f551880ceb)#define INPUT\_BTN\_THUMBL 0x13d

[ 221](group__input__events.md#ga83061a701ecd88a543a1ff9850cfd070)#define INPUT\_BTN\_THUMBR 0x13e

[ 222](group__input__events.md#ga3c5f6d03b079c2771d5b5a0dbed75cad)#define INPUT\_BTN\_TL 0x136

[ 223](group__input__events.md#ga59b1954abc7d0f4d05e025a570439155)#define INPUT\_BTN\_TL2 0x138

[ 224](group__input__events.md#ga80661f579f180f02e05fa3c1175728c4)#define INPUT\_BTN\_TOUCH 0x14a

[ 225](group__input__events.md#gacc3e39f0e70af828684efe126931b5ff)#define INPUT\_BTN\_TR 0x137

[ 226](group__input__events.md#ga7401c1c0ec2b6d20ab4ca0bfa87b06bd)#define INPUT\_BTN\_TR2 0x139

[ 227](group__input__events.md#ga0913edaa3f7176c942c6708090719d48)#define INPUT\_BTN\_WEST 0x134

[ 228](group__input__events.md#gad205e660b5cc9e148db7b0acd22c4560)#define INPUT\_BTN\_X BTN\_NORTH

[ 229](group__input__events.md#ga4a11b785ae5dab8922f481217e01fd08)#define INPUT\_BTN\_Y BTN\_WEST

[ 230](group__input__events.md#ga09f473104f9c92f40e2f481b1e02a28f)#define INPUT\_BTN\_Z 0x135

232

[ 238](group__input__events.md#ga79930c9f3260ca7ae2026e85280b9808)#define INPUT\_ABS\_BRAKE 0x0a

[ 239](group__input__events.md#ga77831126c364a12132db3e51af8002e3)#define INPUT\_ABS\_GAS 0x09

[ 240](group__input__events.md#ga7dbd7e0140f5d13c7b92243568dba95b)#define INPUT\_ABS\_MT\_SLOT 0x2f

[ 241](group__input__events.md#ga5c9daa51741ad28757bfb4e7538bf2c7)#define INPUT\_ABS\_RUDDER 0x07

[ 242](group__input__events.md#ga2564b261dc72e0d48776bfd80282baf4)#define INPUT\_ABS\_RX 0x03

[ 243](group__input__events.md#ga69109075f91f270b43de41f7e558f894)#define INPUT\_ABS\_RY 0x04

[ 244](group__input__events.md#gad4f9589ef67776adc52a2cee72bb1634)#define INPUT\_ABS\_RZ 0x05

[ 245](group__input__events.md#ga44d3e48d42006c73e011d9ee8d5656c3)#define INPUT\_ABS\_THROTTLE 0x06

[ 246](group__input__events.md#ga5fde78f9e113ac35ebb4f1735a08d3e3)#define INPUT\_ABS\_WHEEL 0x08

[ 247](group__input__events.md#ga6bb2cf3decdbbeac354f66db7239f8c1)#define INPUT\_ABS\_X 0x00

[ 248](group__input__events.md#gad2f731397644733e4b3d9f8f96d4f87a)#define INPUT\_ABS\_Y 0x01

[ 249](group__input__events.md#gae007afd99bf586fdc4c6b1a5ae1a3859)#define INPUT\_ABS\_Z 0x02

251

[ 257](group__input__events.md#gab8aeb81a612ec63d687cbe1d9becb823)#define INPUT\_REL\_DIAL 0x07

[ 258](group__input__events.md#ga5b9989321b8e8f883bd338c1a37d50c2)#define INPUT\_REL\_HWHEEL 0x06

[ 259](group__input__events.md#gaf2a08d3d5a0aa60b8f56ff7e2110a54e)#define INPUT\_REL\_MISC 0x09

[ 260](group__input__events.md#ga5727f75f795b31982dc8681a0eed3378)#define INPUT\_REL\_RX 0x03

[ 261](group__input__events.md#ga85cde1de349dffef0c7dd5757e94cb4a)#define INPUT\_REL\_RY 0x04

[ 262](group__input__events.md#ga1f1ed1ce01e943906e5cecf071c0bf96)#define INPUT\_REL\_RZ 0x05

[ 263](group__input__events.md#ga3884c7bbfb3b23e9cbc054f327b4344c)#define INPUT\_REL\_WHEEL 0x08

[ 264](group__input__events.md#ga6afab29530dfffbb81b191b90548ffd2)#define INPUT\_REL\_X 0x00

[ 265](group__input__events.md#ga5fbdf5c33ac1e5330c3f30b37ee8f51d)#define INPUT\_REL\_Y 0x01

[ 266](group__input__events.md#gae5626b188d77b39a79df4bb7790cd316)#define INPUT\_REL\_Z 0x02

268

[ 274](group__input__events.md#ga62a5a51f0beb512236dfa276211e1f43)#define INPUT\_MSC\_SCAN 0x04

276

278

279#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INPUT\_INPUT\_EVENT\_CODES\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [input](dir_ab844d62c7a22d129cc80e6c359d2c21.md)
- [input-event-codes.h](input-event-codes_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
