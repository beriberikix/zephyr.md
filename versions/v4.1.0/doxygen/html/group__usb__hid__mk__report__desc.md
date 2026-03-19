---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__usb__hid__mk__report__desc.html
original_path: doxygen/html/group__usb__hid__mk__report__desc.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Mouse and keyboard report descriptors

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB HID common definitions](group__usb__hid__definitions.md)

| Macros | |
| --- | --- |
| #define | [HID\_MOUSE\_REPORT\_DESC](#ga3696f0782268d504b0c8bb540236779f)(bcnt) |
|  | Simple HID mouse report descriptor for n button mouse. |
| #define | [HID\_KEYBOARD\_REPORT\_DESC](#gaea973ffbe1612187c90614133956cfd6)() |
|  | Simple HID keyboard report descriptor. |

| Enumerations | |
| --- | --- |
| enum | [hid\_kbd\_code](#ga4f2bb15109c64695f852afd6bd99e3bf) {     [HID\_KEY\_A](#gga4f2bb15109c64695f852afd6bd99e3bfa5413afa6a28a21dd52f07db101f2d139) = 4 , [HID\_KEY\_B](#gga4f2bb15109c64695f852afd6bd99e3bfabb0b25fe8c201dc75b72c7b078f745d6) = 5 , [HID\_KEY\_C](#gga4f2bb15109c64695f852afd6bd99e3bfa932c610512cc99157654c3997bc2b922) = 6 , [HID\_KEY\_D](#gga4f2bb15109c64695f852afd6bd99e3bfabc172093417a4c40a7443eee551e9700) = 7 ,     [HID\_KEY\_E](#gga4f2bb15109c64695f852afd6bd99e3bfaff7192b9ddd4228e02c44b6fb2d7bf85) = 8 , [HID\_KEY\_F](#gga4f2bb15109c64695f852afd6bd99e3bfacc002ca9f0f3bdc01b4de42d00e5560b) = 9 , [HID\_KEY\_G](#gga4f2bb15109c64695f852afd6bd99e3bfa1eadd56346bbd64b1c33fa5393f65bda) = 10 , [HID\_KEY\_H](#gga4f2bb15109c64695f852afd6bd99e3bfa4bfc341fccde664ec9267af6e705ba0c) = 11 ,     [HID\_KEY\_I](#gga4f2bb15109c64695f852afd6bd99e3bfafcd25dc5bba218f7097698f8f49fdc45) = 12 , [HID\_KEY\_J](#gga4f2bb15109c64695f852afd6bd99e3bfa2a78196208c634941d63429cd1e1df7a) = 13 , [HID\_KEY\_K](#gga4f2bb15109c64695f852afd6bd99e3bfa4ceddaaaa90d84f0afb3e1ee9a35a976) = 14 , [HID\_KEY\_L](#gga4f2bb15109c64695f852afd6bd99e3bfaf5de66adc9eb2aa183eab1e23f977894) = 15 ,     [HID\_KEY\_M](#gga4f2bb15109c64695f852afd6bd99e3bfa4f8174feca1eb72901576c4e24c8f8a9) = 16 , [HID\_KEY\_N](#gga4f2bb15109c64695f852afd6bd99e3bfab4d202043e8b0b7a8c2d4c519fd1eb07) = 17 , [HID\_KEY\_O](#gga4f2bb15109c64695f852afd6bd99e3bfad8884ef7e77722099e6bd61265f6564c) = 18 , [HID\_KEY\_P](#gga4f2bb15109c64695f852afd6bd99e3bfaca0480331288d15eccec9f072f123817) = 19 ,     [HID\_KEY\_Q](#gga4f2bb15109c64695f852afd6bd99e3bfa05fb920f8129f57dd350036f17fbe519) = 20 , [HID\_KEY\_R](#gga4f2bb15109c64695f852afd6bd99e3bfa037de00c763ae6b270895b7a5f0f57a7) = 21 , [HID\_KEY\_S](#gga4f2bb15109c64695f852afd6bd99e3bfae6a84e8474b6c3e8f9f7d344408cfa0b) = 22 , [HID\_KEY\_T](#gga4f2bb15109c64695f852afd6bd99e3bfa893799f48b30c438349335556a0e15b6) = 23 ,     [HID\_KEY\_U](#gga4f2bb15109c64695f852afd6bd99e3bfab3c7c9f3a73e83623c651cdfddddeb05) = 24 , [HID\_KEY\_V](#gga4f2bb15109c64695f852afd6bd99e3bfa02f14e6303b4d2e4e46747324d649dda) = 25 , [HID\_KEY\_W](#gga4f2bb15109c64695f852afd6bd99e3bfadf81a88f3f92f15e2abec83911bf3732) = 26 , [HID\_KEY\_X](#gga4f2bb15109c64695f852afd6bd99e3bfa9f3b8bb63f6628db9a1678b72ec12b6d) = 27 ,     [HID\_KEY\_Y](#gga4f2bb15109c64695f852afd6bd99e3bfa4ca2ebe26c09f2400a8ebc0aa445ce89) = 28 , [HID\_KEY\_Z](#gga4f2bb15109c64695f852afd6bd99e3bfaa5cd01ad23ede98de1ae176920b8fc8f) = 29 , [HID\_KEY\_1](#gga4f2bb15109c64695f852afd6bd99e3bfa039ced168420140b97e2d0676e1bb12a) = 30 , [HID\_KEY\_2](#gga4f2bb15109c64695f852afd6bd99e3bfae98dd71460def5e66fcf32e9783b96ea) = 31 ,     [HID\_KEY\_3](#gga4f2bb15109c64695f852afd6bd99e3bfaf58d848786f8d2dfac702f7fae178311) = 32 , [HID\_KEY\_4](#gga4f2bb15109c64695f852afd6bd99e3bfa17019d72e84302486f72f7d8101baca5) = 33 , [HID\_KEY\_5](#gga4f2bb15109c64695f852afd6bd99e3bfaf32ab36da2e30066c9ed2816596011c8) = 34 , [HID\_KEY\_6](#gga4f2bb15109c64695f852afd6bd99e3bfae16b76c1bf9f7aa58a1b1c556a6b6022) = 35 ,     [HID\_KEY\_7](#gga4f2bb15109c64695f852afd6bd99e3bfa5887a1854f7d0787121bd75034cdd726) = 36 , [HID\_KEY\_8](#gga4f2bb15109c64695f852afd6bd99e3bfa1761228849d7dc2b84d0565d3337b2e2) = 37 , [HID\_KEY\_9](#gga4f2bb15109c64695f852afd6bd99e3bfa758aec2540a6a2153702d6905c44ce52) = 38 , [HID\_KEY\_0](#gga4f2bb15109c64695f852afd6bd99e3bfa856ca663233681e789ef4aa94c44ebaf) = 39 ,     [HID\_KEY\_ENTER](#gga4f2bb15109c64695f852afd6bd99e3bfaeeab6ddad27c449cbc44ca2458912a75) = 40 , [HID\_KEY\_ESC](#gga4f2bb15109c64695f852afd6bd99e3bfa763b39fe76a92c4cc1fc32f47d2a760a) = 41 , [HID\_KEY\_BACKSPACE](#gga4f2bb15109c64695f852afd6bd99e3bfafd6cf6a44966d518b173df4ed57ae720) = 42 , [HID\_KEY\_TAB](#gga4f2bb15109c64695f852afd6bd99e3bfa5a6c79e8ea85f6593c06d19098d69a03) = 43 ,     [HID\_KEY\_SPACE](#gga4f2bb15109c64695f852afd6bd99e3bfaf4fc3d7b4b86f9f095cec624d190ebec) = 44 , [HID\_KEY\_MINUS](#gga4f2bb15109c64695f852afd6bd99e3bfaa59864204064d3e8fac5271b69a7da23) = 45 , [HID\_KEY\_EQUAL](#gga4f2bb15109c64695f852afd6bd99e3bfac8d82858905175ba79c24b0be1b1b1a8) = 46 , [HID\_KEY\_LEFTBRACE](#gga4f2bb15109c64695f852afd6bd99e3bfac232473666b21ca772c84b68be6c1f3d) = 47 ,     [HID\_KEY\_RIGHTBRACE](#gga4f2bb15109c64695f852afd6bd99e3bfaef692bd882621d292255cb99d4697513) = 48 , [HID\_KEY\_BACKSLASH](#gga4f2bb15109c64695f852afd6bd99e3bfa25ba5457bc128593b1624d95ec536182) = 49 , [HID\_KEY\_HASH](#gga4f2bb15109c64695f852afd6bd99e3bfa0d57ce7c99d06ee9b15fef880af075eb) = 50 , [HID\_KEY\_SEMICOLON](#gga4f2bb15109c64695f852afd6bd99e3bfa3743f920856a12e726e1be05932c7411) = 51 ,     [HID\_KEY\_APOSTROPHE](#gga4f2bb15109c64695f852afd6bd99e3bfa7325a5bd52e9dc0cc38a85609b1c55ab) = 52 , [HID\_KEY\_GRAVE](#gga4f2bb15109c64695f852afd6bd99e3bfa8b84c64da5b8c5f5d99b86c1cfe09ffc) = 53 , [HID\_KEY\_COMMA](#gga4f2bb15109c64695f852afd6bd99e3bfaa81aa5b3424f02fdf02295de47b11b19) = 54 , [HID\_KEY\_DOT](#gga4f2bb15109c64695f852afd6bd99e3bfa403fe927ebb0014e2c1b3dc25e1d9779) = 55 ,     [HID\_KEY\_SLASH](#gga4f2bb15109c64695f852afd6bd99e3bfa24c2c93a1c895745828311affc011dea) = 56 , [HID\_KEY\_CAPSLOCK](#gga4f2bb15109c64695f852afd6bd99e3bfa4d40549a59fdcfdd0b2d592a6675bc89) = 57 , [HID\_KEY\_F1](#gga4f2bb15109c64695f852afd6bd99e3bfa9642163abbbad8aa5c7088c8529aadd7) = 58 , [HID\_KEY\_F2](#gga4f2bb15109c64695f852afd6bd99e3bfa9ce331f5f41ba3e3e05f485bc2d4138e) = 59 ,     [HID\_KEY\_F3](#gga4f2bb15109c64695f852afd6bd99e3bfa76adde1d9295cf62e7efb35e27911a1e) = 60 , [HID\_KEY\_F4](#gga4f2bb15109c64695f852afd6bd99e3bfaa9956a2b95afe1a05fda65db5cc66467) = 61 , [HID\_KEY\_F5](#gga4f2bb15109c64695f852afd6bd99e3bface9e8d409d981f193f69fc5b29f38ca7) = 62 , [HID\_KEY\_F6](#gga4f2bb15109c64695f852afd6bd99e3bfabc92147e725c8108c18f4e03005afbdc) = 63 ,     [HID\_KEY\_F7](#gga4f2bb15109c64695f852afd6bd99e3bfa1e2eabf8b9fa6cbfea613696b2c4122a) = 64 , [HID\_KEY\_F8](#gga4f2bb15109c64695f852afd6bd99e3bfa5092add2863231d273ba60cd583ebe33) = 65 , [HID\_KEY\_F9](#gga4f2bb15109c64695f852afd6bd99e3bfa5a09deabde1a3a44378b7de44dad27b6) = 66 , [HID\_KEY\_F10](#gga4f2bb15109c64695f852afd6bd99e3bfac2c4a3aec85b4d8171de4429ccabbe19) = 67 ,     [HID\_KEY\_F11](#gga4f2bb15109c64695f852afd6bd99e3bfa76bb35a0f71733b0a0f1bd7e3837064c) = 68 , [HID\_KEY\_F12](#gga4f2bb15109c64695f852afd6bd99e3bfab44ba4426c1574f4b296794b7bfe2172) = 69 , [HID\_KEY\_SYSRQ](#gga4f2bb15109c64695f852afd6bd99e3bfae5405b62cb20962cb5864ba6e90a4ab2) = 70 , [HID\_KEY\_SCROLLLOCK](#gga4f2bb15109c64695f852afd6bd99e3bfae16bd57629c7aba96a554d0446e83d98) = 71 ,     [HID\_KEY\_PAUSE](#gga4f2bb15109c64695f852afd6bd99e3bfa1905733a0fe81f78e0752e3b0bb99c69) = 72 , [HID\_KEY\_INSERT](#gga4f2bb15109c64695f852afd6bd99e3bfa1e1c320cea0644c3dc38da06c865837b) = 73 , [HID\_KEY\_HOME](#gga4f2bb15109c64695f852afd6bd99e3bfa5fc1127fe9014018f4831cbf272c883b) = 74 , [HID\_KEY\_PAGEUP](#gga4f2bb15109c64695f852afd6bd99e3bfa2468ac3b37d38b6158cd989ed54bcd8c) = 75 ,     [HID\_KEY\_DELETE](#gga4f2bb15109c64695f852afd6bd99e3bfae8f5051cb476c3e9253b008094c431fc) = 76 , [HID\_KEY\_END](#gga4f2bb15109c64695f852afd6bd99e3bfa8f933f0f6e5a1a3c3cdc1819ffcdce63) = 77 , [HID\_KEY\_PAGEDOWN](#gga4f2bb15109c64695f852afd6bd99e3bfaf7615ff4f608d64ae20a61540d939065) = 78 , [HID\_KEY\_RIGHT](#gga4f2bb15109c64695f852afd6bd99e3bfa4c203feb452e3212089e8246b8d75f6c) = 79 ,     [HID\_KEY\_LEFT](#gga4f2bb15109c64695f852afd6bd99e3bfaf7d3c678a8ac31916068a0c5aff54d4b) = 80 , [HID\_KEY\_DOWN](#gga4f2bb15109c64695f852afd6bd99e3bfa9e2597c2a109abda1c63c8d5ca5376b3) = 81 , [HID\_KEY\_UP](#gga4f2bb15109c64695f852afd6bd99e3bfaf5fe431b55adf16d82604e0fc2239090) = 82 , [HID\_KEY\_NUMLOCK](#gga4f2bb15109c64695f852afd6bd99e3bfafec8c71efd5ee9decd156f0d33739fbe) = 83 ,     [HID\_KEY\_KPSLASH](#gga4f2bb15109c64695f852afd6bd99e3bfa44e83040efab214dcfe462ac0d338e0c) = 84 , [HID\_KEY\_KPASTERISK](#gga4f2bb15109c64695f852afd6bd99e3bfaff47eb8157a7118183573e3aefb7df08) = 85 , [HID\_KEY\_KPMINUS](#gga4f2bb15109c64695f852afd6bd99e3bfa6fb35c78b12ae434cb7a7280501886e9) = 86 , [HID\_KEY\_KPPLUS](#gga4f2bb15109c64695f852afd6bd99e3bfa2cb7852467d2ebd785e2f7556383a883) = 87 ,     [HID\_KEY\_KPENTER](#gga4f2bb15109c64695f852afd6bd99e3bfab5b923992d0bdc176f716cd8ace3a66e) = 88 , [HID\_KEY\_KP\_1](#gga4f2bb15109c64695f852afd6bd99e3bfa7eea75b0eb4b4f0306daa3e6fccf09e4) = 89 , [HID\_KEY\_KP\_2](#gga4f2bb15109c64695f852afd6bd99e3bfa68db65e7002e7cc599394a7eea116e3c) = 90 , [HID\_KEY\_KP\_3](#gga4f2bb15109c64695f852afd6bd99e3bfa4210f9a5ae469c8b863b28b9b2d8189d) = 91 ,     [HID\_KEY\_KP\_4](#gga4f2bb15109c64695f852afd6bd99e3bfa48eefeeb48a942eaaa0726bd4a2df01d) = 92 , [HID\_KEY\_KP\_5](#gga4f2bb15109c64695f852afd6bd99e3bfa1b8d299d56a0289ae15cbf8c67e36a7c) = 93 , [HID\_KEY\_KP\_6](#gga4f2bb15109c64695f852afd6bd99e3bfa90f2c51ad42e335a474061c4d5e4e5a9) = 94 , [HID\_KEY\_KP\_7](#gga4f2bb15109c64695f852afd6bd99e3bfa1e191017084fadf830a7394de0e1cc05) = 95 ,     [HID\_KEY\_KP\_8](#gga4f2bb15109c64695f852afd6bd99e3bfadd7c795e2c9c212a4adeaba904bda447) = 96 , [HID\_KEY\_KP\_9](#gga4f2bb15109c64695f852afd6bd99e3bface8d41615c6afd45724f4b6d16238c36) = 97 , [HID\_KEY\_KP\_0](#gga4f2bb15109c64695f852afd6bd99e3bfa4ae4af2b06f6f2585a598353bfef9af7) = 98   } |
|  | HID keyboard button codes. [More...](#ga4f2bb15109c64695f852afd6bd99e3bf) |
| enum | [hid\_kbd\_modifier](#ga12f11556b697518b00fa86eb040f9eb8) {     [HID\_KBD\_MODIFIER\_NONE](#gga12f11556b697518b00fa86eb040f9eb8a79b0eb4f485bedb745180f1b8798c603) = 0x00 , [HID\_KBD\_MODIFIER\_LEFT\_CTRL](#gga12f11556b697518b00fa86eb040f9eb8a4df663509a05599fd66657cfc90a37c7) = 0x01 , [HID\_KBD\_MODIFIER\_LEFT\_SHIFT](#gga12f11556b697518b00fa86eb040f9eb8aba69ca183306d3d1427b66666803e57f) = 0x02 , [HID\_KBD\_MODIFIER\_LEFT\_ALT](#gga12f11556b697518b00fa86eb040f9eb8a829d884291b546c0e276afa4ad92ac18) = 0x04 ,     [HID\_KBD\_MODIFIER\_LEFT\_UI](#gga12f11556b697518b00fa86eb040f9eb8a718c92a2d0ca9dd6603825b97a99fc77) = 0x08 , [HID\_KBD\_MODIFIER\_RIGHT\_CTRL](#gga12f11556b697518b00fa86eb040f9eb8a8e346c0e9c7d5b58e4b8748380423a92) = 0x10 , [HID\_KBD\_MODIFIER\_RIGHT\_SHIFT](#gga12f11556b697518b00fa86eb040f9eb8affdba298e8860b000a0916be7495c2dc) = 0x20 , [HID\_KBD\_MODIFIER\_RIGHT\_ALT](#gga12f11556b697518b00fa86eb040f9eb8a85ce29a6ab9feef68350deca92001db2) = 0x40 ,     [HID\_KBD\_MODIFIER\_RIGHT\_UI](#gga12f11556b697518b00fa86eb040f9eb8a1b4b75cd0364824cbfc80dfc68e294dd) = 0x80   } |
|  | HID keyboard modifiers. [More...](#ga12f11556b697518b00fa86eb040f9eb8) |
| enum | [hid\_kbd\_led](#ga8cef56ba216d0a01c6cc89f723d1740b) {     [HID\_KBD\_LED\_NUM\_LOCK](#gga8cef56ba216d0a01c6cc89f723d1740ba6cb2e1acb52cc5bab8dd3aa6ef6ac01b) = 0x01 , [HID\_KBD\_LED\_CAPS\_LOCK](#gga8cef56ba216d0a01c6cc89f723d1740baa17e5130bd8c45eb21661d8783517266) = 0x02 , [HID\_KBD\_LED\_SCROLL\_LOCK](#gga8cef56ba216d0a01c6cc89f723d1740ba6ea943f59b98680aefd0d5be4ef22e36) = 0x04 , [HID\_KBD\_LED\_COMPOSE](#gga8cef56ba216d0a01c6cc89f723d1740bad62692e71ae45351311c8bf2ce13e3c9) = 0x08 ,     [HID\_KBD\_LED\_KANA](#gga8cef56ba216d0a01c6cc89f723d1740bafd5d599c1955bdb1c62c7b17286b37f1) = 0x10   } |
|  | HID keyboard LEDs. [More...](#ga8cef56ba216d0a01c6cc89f723d1740b) |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gaea973ffbe1612187c90614133956cfd6)HID\_KEYBOARD\_REPORT\_DESC

| #define HID\_KEYBOARD\_REPORT\_DESC | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

{ \

HID\_USAGE\_PAGE([HID\_USAGE\_GEN\_DESKTOP](group__usb__hid__definitions.md#gacb3fc5b0f838dfa5eb95e9e1bf52b589)), \

HID\_USAGE([HID\_USAGE\_GEN\_DESKTOP\_KEYBOARD](group__usb__hid__definitions.md#ga0bdaa3d23c79204a1064cb53b279bd77)), \

HID\_COLLECTION([HID\_COLLECTION\_APPLICATION](group__usb__hid__definitions.md#ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd)), \

HID\_USAGE\_PAGE([HID\_USAGE\_GEN\_DESKTOP\_KEYPAD](group__usb__hid__definitions.md#ga69f8e44306828b3f44d3a7704ff07807)), \

/\* HID\_USAGE\_MINIMUM(Keyboard LeftControl) \*/ \

HID\_USAGE\_MIN8(0xE0), \

/\* HID\_USAGE\_MAXIMUM(Keyboard Right GUI) \*/ \

HID\_USAGE\_MAX8(0xE7), \

HID\_LOGICAL\_MIN8(0), \

HID\_LOGICAL\_MAX8(1), \

HID\_REPORT\_SIZE(1), \

HID\_REPORT\_COUNT(8), \

/\* HID\_INPUT(Data,Var,Abs) \*/ \

HID\_INPUT(0x02), \

HID\_REPORT\_SIZE(8), \

HID\_REPORT\_COUNT(1), \

/\* HID\_INPUT(Cnst,Var,Abs) \*/ \

HID\_INPUT(0x03), \

HID\_REPORT\_SIZE(1), \

HID\_REPORT\_COUNT(5), \

HID\_USAGE\_PAGE([HID\_USAGE\_GEN\_LEDS](group__usb__hid__definitions.md#gae632e9a37203506c051c3cacfdf0c2c7)), \

/\* HID\_USAGE\_MINIMUM(Num Lock) \*/ \

HID\_USAGE\_MIN8(1), \

/\* HID\_USAGE\_MAXIMUM(Kana) \*/ \

HID\_USAGE\_MAX8(5), \

/\* HID\_OUTPUT(Data,Var,Abs) \*/ \

HID\_OUTPUT(0x02), \

HID\_REPORT\_SIZE(3), \

HID\_REPORT\_COUNT(1), \

/\* HID\_OUTPUT(Cnst,Var,Abs) \*/ \

HID\_OUTPUT(0x03), \

HID\_REPORT\_SIZE(8), \

HID\_REPORT\_COUNT(6), \

HID\_LOGICAL\_MIN8(0), \

HID\_LOGICAL\_MAX8(101), \

HID\_USAGE\_PAGE([HID\_USAGE\_GEN\_DESKTOP\_KEYPAD](group__usb__hid__definitions.md#ga69f8e44306828b3f44d3a7704ff07807)), \

/\* HID\_USAGE\_MIN8(Reserved) \*/ \

HID\_USAGE\_MIN8(0), \

/\* HID\_USAGE\_MAX8(Keyboard Application) \*/ \

HID\_USAGE\_MAX8(101), \

/\* HID\_INPUT (Data,Ary,Abs) \*/ \

HID\_INPUT(0x00), \

[HID\_END\_COLLECTION](group__usb__hid__items.md#ga6cd6affb9d52e0bf98c7a5c83d03a764), \

}

[HID\_USAGE\_GEN\_DESKTOP\_KEYBOARD](group__usb__hid__definitions.md#ga0bdaa3d23c79204a1064cb53b279bd77)

#define HID\_USAGE\_GEN\_DESKTOP\_KEYBOARD

HID Generic Desktop Keyboard Usage ID.

**Definition** hid.h:156

[HID\_COLLECTION\_APPLICATION](group__usb__hid__definitions.md#ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd)

#define HID\_COLLECTION\_APPLICATION

Application collection type.

**Definition** hid.h:121

[HID\_USAGE\_GEN\_DESKTOP\_KEYPAD](group__usb__hid__definitions.md#ga69f8e44306828b3f44d3a7704ff07807)

#define HID\_USAGE\_GEN\_DESKTOP\_KEYPAD

HID Generic Desktop Keypad Usage ID.

**Definition** hid.h:158

[HID\_USAGE\_GEN\_DESKTOP](group__usb__hid__definitions.md#gacb3fc5b0f838dfa5eb95e9e1bf52b589)

#define HID\_USAGE\_GEN\_DESKTOP

HID Generic Desktop Controls Usage page.

**Definition** hid.h:137

[HID\_USAGE\_GEN\_LEDS](group__usb__hid__definitions.md#gae632e9a37203506c051c3cacfdf0c2c7)

#define HID\_USAGE\_GEN\_LEDS

HID LEDs Usage page.

**Definition** hid.h:141

[HID\_END\_COLLECTION](group__usb__hid__items.md#ga6cd6affb9d52e0bf98c7a5c83d03a764)

#define HID\_END\_COLLECTION

Define HID End Collection (non-data) item.

**Definition** hid.h:238

Simple HID keyboard report descriptor.

## [◆ ](#ga3696f0782268d504b0c8bb540236779f)HID\_MOUSE\_REPORT\_DESC

| #define HID\_MOUSE\_REPORT\_DESC | ( |  | *bcnt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

{ \

HID\_USAGE\_PAGE([HID\_USAGE\_GEN\_DESKTOP](group__usb__hid__definitions.md#gacb3fc5b0f838dfa5eb95e9e1bf52b589)), \

HID\_USAGE([HID\_USAGE\_GEN\_DESKTOP\_MOUSE](group__usb__hid__definitions.md#ga983274dd50058de26e0e86d10d50e81a)), \

HID\_COLLECTION([HID\_COLLECTION\_APPLICATION](group__usb__hid__definitions.md#ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd)), \

HID\_USAGE([HID\_USAGE\_GEN\_DESKTOP\_POINTER](group__usb__hid__definitions.md#ga77a7162980a77efa1e2e7b21942bb7dd)), \

HID\_COLLECTION([HID\_COLLECTION\_PHYSICAL](group__usb__hid__definitions.md#gaca1e227f9241c217b8b1aeae6c4bd672)), \

/\* Bits used for button signalling \*/ \

HID\_USAGE\_PAGE([HID\_USAGE\_GEN\_BUTTON](group__usb__hid__definitions.md#ga13401731a0ead5448a0823d0f6142404)), \

HID\_USAGE\_MIN8(1), \

HID\_USAGE\_MAX8(bcnt), \

HID\_LOGICAL\_MIN8(0), \

HID\_LOGICAL\_MAX8(1), \

HID\_REPORT\_SIZE(1), \

HID\_REPORT\_COUNT(bcnt), \

/\* HID\_INPUT (Data,Var,Abs) \*/ \

HID\_INPUT(0x02), \

/\* Unused bits \*/ \

HID\_REPORT\_SIZE(8 - bcnt), \

HID\_REPORT\_COUNT(1), \

/\* HID\_INPUT (Cnst,Ary,Abs) \*/ \

HID\_INPUT(1), \

/\* X and Y axis, scroll \*/ \

HID\_USAGE\_PAGE([HID\_USAGE\_GEN\_DESKTOP](group__usb__hid__definitions.md#gacb3fc5b0f838dfa5eb95e9e1bf52b589)), \

HID\_USAGE([HID\_USAGE\_GEN\_DESKTOP\_X](group__usb__hid__definitions.md#gae283a3558ba536e163140a3b6cdbb273)), \

HID\_USAGE([HID\_USAGE\_GEN\_DESKTOP\_Y](group__usb__hid__definitions.md#gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb)), \

HID\_USAGE([HID\_USAGE\_GEN\_DESKTOP\_WHEEL](group__usb__hid__definitions.md#gaa8c772d412ac1ac7a36739c52f04c0a9)), \

HID\_LOGICAL\_MIN8(-127), \

HID\_LOGICAL\_MAX8(127), \

HID\_REPORT\_SIZE(8), \

HID\_REPORT\_COUNT(3), \

/\* HID\_INPUT (Data,Var,Rel) \*/ \

HID\_INPUT(0x06), \

[HID\_END\_COLLECTION](group__usb__hid__items.md#ga6cd6affb9d52e0bf98c7a5c83d03a764), \

[HID\_END\_COLLECTION](group__usb__hid__items.md#ga6cd6affb9d52e0bf98c7a5c83d03a764), \

}

[HID\_USAGE\_GEN\_BUTTON](group__usb__hid__definitions.md#ga13401731a0ead5448a0823d0f6142404)

#define HID\_USAGE\_GEN\_BUTTON

HID Button Usage page.

**Definition** hid.h:143

[HID\_USAGE\_GEN\_DESKTOP\_POINTER](group__usb__hid__definitions.md#ga77a7162980a77efa1e2e7b21942bb7dd)

#define HID\_USAGE\_GEN\_DESKTOP\_POINTER

HID Generic Desktop Pointer Usage ID.

**Definition** hid.h:148

[HID\_USAGE\_GEN\_DESKTOP\_MOUSE](group__usb__hid__definitions.md#ga983274dd50058de26e0e86d10d50e81a)

#define HID\_USAGE\_GEN\_DESKTOP\_MOUSE

HID Generic Desktop Mouse Usage ID.

**Definition** hid.h:150

[HID\_USAGE\_GEN\_DESKTOP\_WHEEL](group__usb__hid__definitions.md#gaa8c772d412ac1ac7a36739c52f04c0a9)

#define HID\_USAGE\_GEN\_DESKTOP\_WHEEL

HID Generic Desktop Wheel Usage ID.

**Definition** hid.h:164

[HID\_COLLECTION\_PHYSICAL](group__usb__hid__definitions.md#gaca1e227f9241c217b8b1aeae6c4bd672)

#define HID\_COLLECTION\_PHYSICAL

Physical collection type.

**Definition** hid.h:119

[HID\_USAGE\_GEN\_DESKTOP\_Y](group__usb__hid__definitions.md#gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb)

#define HID\_USAGE\_GEN\_DESKTOP\_Y

HID Generic Desktop Y Usage ID.

**Definition** hid.h:162

[HID\_USAGE\_GEN\_DESKTOP\_X](group__usb__hid__definitions.md#gae283a3558ba536e163140a3b6cdbb273)

#define HID\_USAGE\_GEN\_DESKTOP\_X

HID Generic Desktop X Usage ID.

**Definition** hid.h:160

Simple HID mouse report descriptor for n button mouse.

Parameters
:   | bcnt | Button count. Allowed values from 1 to 8. |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#ga4f2bb15109c64695f852afd6bd99e3bf)hid\_kbd\_code

| enum [hid\_kbd\_code](#ga4f2bb15109c64695f852afd6bd99e3bf) |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID keyboard button codes.

| Enumerator | |
| --- | --- |
| HID\_KEY\_A |  |
| HID\_KEY\_B |  |
| HID\_KEY\_C |  |
| HID\_KEY\_D |  |
| HID\_KEY\_E |  |
| HID\_KEY\_F |  |
| HID\_KEY\_G |  |
| HID\_KEY\_H |  |
| HID\_KEY\_I |  |
| HID\_KEY\_J |  |
| HID\_KEY\_K |  |
| HID\_KEY\_L |  |
| HID\_KEY\_M |  |
| HID\_KEY\_N |  |
| HID\_KEY\_O |  |
| HID\_KEY\_P |  |
| HID\_KEY\_Q |  |
| HID\_KEY\_R |  |
| HID\_KEY\_S |  |
| HID\_KEY\_T |  |
| HID\_KEY\_U |  |
| HID\_KEY\_V |  |
| HID\_KEY\_W |  |
| HID\_KEY\_X |  |
| HID\_KEY\_Y |  |
| HID\_KEY\_Z |  |
| HID\_KEY\_1 |  |
| HID\_KEY\_2 |  |
| HID\_KEY\_3 |  |
| HID\_KEY\_4 |  |
| HID\_KEY\_5 |  |
| HID\_KEY\_6 |  |
| HID\_KEY\_7 |  |
| HID\_KEY\_8 |  |
| HID\_KEY\_9 |  |
| HID\_KEY\_0 |  |
| HID\_KEY\_ENTER |  |
| HID\_KEY\_ESC |  |
| HID\_KEY\_BACKSPACE |  |
| HID\_KEY\_TAB |  |
| HID\_KEY\_SPACE |  |
| HID\_KEY\_MINUS |  |
| HID\_KEY\_EQUAL |  |
| HID\_KEY\_LEFTBRACE |  |
| HID\_KEY\_RIGHTBRACE |  |
| HID\_KEY\_BACKSLASH |  |
| HID\_KEY\_HASH |  |
| HID\_KEY\_SEMICOLON |  |
| HID\_KEY\_APOSTROPHE |  |
| HID\_KEY\_GRAVE |  |
| HID\_KEY\_COMMA |  |
| HID\_KEY\_DOT |  |
| HID\_KEY\_SLASH |  |
| HID\_KEY\_CAPSLOCK |  |
| HID\_KEY\_F1 |  |
| HID\_KEY\_F2 |  |
| HID\_KEY\_F3 |  |
| HID\_KEY\_F4 |  |
| HID\_KEY\_F5 |  |
| HID\_KEY\_F6 |  |
| HID\_KEY\_F7 |  |
| HID\_KEY\_F8 |  |
| HID\_KEY\_F9 |  |
| HID\_KEY\_F10 |  |
| HID\_KEY\_F11 |  |
| HID\_KEY\_F12 |  |
| HID\_KEY\_SYSRQ |  |
| HID\_KEY\_SCROLLLOCK |  |
| HID\_KEY\_PAUSE |  |
| HID\_KEY\_INSERT |  |
| HID\_KEY\_HOME |  |
| HID\_KEY\_PAGEUP |  |
| HID\_KEY\_DELETE |  |
| HID\_KEY\_END |  |
| HID\_KEY\_PAGEDOWN |  |
| HID\_KEY\_RIGHT |  |
| HID\_KEY\_LEFT |  |
| HID\_KEY\_DOWN |  |
| HID\_KEY\_UP |  |
| HID\_KEY\_NUMLOCK |  |
| HID\_KEY\_KPSLASH |  |
| HID\_KEY\_KPASTERISK |  |
| HID\_KEY\_KPMINUS |  |
| HID\_KEY\_KPPLUS |  |
| HID\_KEY\_KPENTER |  |
| HID\_KEY\_KP\_1 |  |
| HID\_KEY\_KP\_2 |  |
| HID\_KEY\_KP\_3 |  |
| HID\_KEY\_KP\_4 |  |
| HID\_KEY\_KP\_5 |  |
| HID\_KEY\_KP\_6 |  |
| HID\_KEY\_KP\_7 |  |
| HID\_KEY\_KP\_8 |  |
| HID\_KEY\_KP\_9 |  |
| HID\_KEY\_KP\_0 |  |

## [◆ ](#ga8cef56ba216d0a01c6cc89f723d1740b)hid\_kbd\_led

| enum [hid\_kbd\_led](#ga8cef56ba216d0a01c6cc89f723d1740b) |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID keyboard LEDs.

| Enumerator | |
| --- | --- |
| HID\_KBD\_LED\_NUM\_LOCK |  |
| HID\_KBD\_LED\_CAPS\_LOCK |  |
| HID\_KBD\_LED\_SCROLL\_LOCK |  |
| HID\_KBD\_LED\_COMPOSE |  |
| HID\_KBD\_LED\_KANA |  |

## [◆ ](#ga12f11556b697518b00fa86eb040f9eb8)hid\_kbd\_modifier

| enum [hid\_kbd\_modifier](#ga12f11556b697518b00fa86eb040f9eb8) |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID keyboard modifiers.

| Enumerator | |
| --- | --- |
| HID\_KBD\_MODIFIER\_NONE |  |
| HID\_KBD\_MODIFIER\_LEFT\_CTRL |  |
| HID\_KBD\_MODIFIER\_LEFT\_SHIFT |  |
| HID\_KBD\_MODIFIER\_LEFT\_ALT |  |
| HID\_KBD\_MODIFIER\_LEFT\_UI |  |
| HID\_KBD\_MODIFIER\_RIGHT\_CTRL |  |
| HID\_KBD\_MODIFIER\_RIGHT\_SHIFT |  |
| HID\_KBD\_MODIFIER\_RIGHT\_ALT |  |
| HID\_KBD\_MODIFIER\_RIGHT\_UI |  |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
