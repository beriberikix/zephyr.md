---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/shell__types_8h_source.html
original_path: doxygen/html/shell__types_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_types.h

[Go to the documentation of this file.](shell__types_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef SHELL\_TYPES\_H\_\_

7#define SHELL\_TYPES\_H\_\_

8

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

[ 14](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2)enum [shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2) {

[ 15](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a52be3094dd0400eba48c686b0b4e57c6) [SHELL\_VT100\_COLOR\_BLACK](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a52be3094dd0400eba48c686b0b4e57c6),

[ 16](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4) [SHELL\_VT100\_COLOR\_RED](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4),

[ 17](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a) [SHELL\_VT100\_COLOR\_GREEN](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a),

[ 18](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d) [SHELL\_VT100\_COLOR\_YELLOW](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d),

[ 19](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2ace5b01755eec4567f0dc65e48143e33d) [SHELL\_VT100\_COLOR\_BLUE](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2ace5b01755eec4567f0dc65e48143e33d),

[ 20](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a85c738dbb19eccc90adba2e4a131140a) [SHELL\_VT100\_COLOR\_MAGENTA](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a85c738dbb19eccc90adba2e4a131140a),

[ 21](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972) [SHELL\_VT100\_COLOR\_CYAN](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972),

[ 22](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a20523afc967f7f3bc0af645255b0b28c) [SHELL\_VT100\_COLOR\_WHITE](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a20523afc967f7f3bc0af645255b0b28c),

23

[ 24](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e) [SHELL\_VT100\_COLOR\_DEFAULT](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e),

25

[ 26](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2aab87d1e19b4d687eb1fee07c73a33bd4) [VT100\_COLOR\_END](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2aab87d1e19b4d687eb1fee07c73a33bd4)

27};

28

[ 29](structshell__vt100__colors.md)struct [shell\_vt100\_colors](structshell__vt100__colors.md) {

[ 30](structshell__vt100__colors.md#a4f75bb7b94c553ef7a704293fc98bde8) enum [shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2) [col](structshell__vt100__colors.md#a4f75bb7b94c553ef7a704293fc98bde8);

[ 31](structshell__vt100__colors.md#a085471a594831d7b585f6d9b02bc8216) enum [shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2) [bgcol](structshell__vt100__colors.md#a085471a594831d7b585f6d9b02bc8216);

32};

33

[ 34](structshell__multiline__cons.md)struct [shell\_multiline\_cons](structshell__multiline__cons.md) {

[ 35](structshell__multiline__cons.md#a52a43a16f9d2e30d82dfe019384b0f7b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cur\_x](structshell__multiline__cons.md#a52a43a16f9d2e30d82dfe019384b0f7b);

[ 36](structshell__multiline__cons.md#a54a051c1e085644e6cd1e86284fabf0d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cur\_x\_end](structshell__multiline__cons.md#a54a051c1e085644e6cd1e86284fabf0d);

[ 37](structshell__multiline__cons.md#a0ee84724f4b26ee2933c88b170445d93) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cur\_y](structshell__multiline__cons.md#a0ee84724f4b26ee2933c88b170445d93);

[ 38](structshell__multiline__cons.md#a0a07e8991006b34f111d068e22800d28) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cur\_y\_end](structshell__multiline__cons.md#a0a07e8991006b34f111d068e22800d28);

[ 39](structshell__multiline__cons.md#ae65c3c25e87841be58347cf54b5c36d8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [terminal\_hei](structshell__multiline__cons.md#ae65c3c25e87841be58347cf54b5c36d8);

[ 40](structshell__multiline__cons.md#a48b37c8d0cc4584ab05299be34008575) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [terminal\_wid](structshell__multiline__cons.md#a48b37c8d0cc4584ab05299be34008575);

[ 41](structshell__multiline__cons.md#aa4ed5794533137992a2a9d3e7eb12f6a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [name\_len](structshell__multiline__cons.md#aa4ed5794533137992a2a9d3e7eb12f6a);

42};

43

[ 44](structshell__vt100__ctx.md)struct [shell\_vt100\_ctx](structshell__vt100__ctx.md) {

[ 45](structshell__vt100__ctx.md#a600ef23980af7daf7d4abcba9043b448) struct [shell\_multiline\_cons](structshell__multiline__cons.md) [cons](structshell__vt100__ctx.md#a600ef23980af7daf7d4abcba9043b448);

[ 46](structshell__vt100__ctx.md#abc658a8e804ad3afcd3384e621cd8179) struct [shell\_vt100\_colors](structshell__vt100__colors.md) [col](structshell__vt100__ctx.md#abc658a8e804ad3afcd3384e621cd8179);

[ 47](structshell__vt100__ctx.md#a46443b4cd885a900fb3b9afe143dbb6d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [printed\_cmd](structshell__vt100__ctx.md#a46443b4cd885a900fb3b9afe143dbb6d);

48};

49

50#ifdef \_\_cplusplus

51}

52#endif

53

54#endif /\* SHELL\_TYPES\_H\_\_ \*/

[shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2)

shell\_vt100\_color

**Definition** shell\_types.h:14

[SHELL\_VT100\_COLOR\_WHITE](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a20523afc967f7f3bc0af645255b0b28c)

@ SHELL\_VT100\_COLOR\_WHITE

**Definition** shell\_types.h:22

[SHELL\_VT100\_COLOR\_DEFAULT](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e)

@ SHELL\_VT100\_COLOR\_DEFAULT

**Definition** shell\_types.h:24

[SHELL\_VT100\_COLOR\_BLACK](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a52be3094dd0400eba48c686b0b4e57c6)

@ SHELL\_VT100\_COLOR\_BLACK

**Definition** shell\_types.h:15

[SHELL\_VT100\_COLOR\_CYAN](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972)

@ SHELL\_VT100\_COLOR\_CYAN

**Definition** shell\_types.h:21

[SHELL\_VT100\_COLOR\_RED](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4)

@ SHELL\_VT100\_COLOR\_RED

**Definition** shell\_types.h:16

[SHELL\_VT100\_COLOR\_MAGENTA](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a85c738dbb19eccc90adba2e4a131140a)

@ SHELL\_VT100\_COLOR\_MAGENTA

**Definition** shell\_types.h:20

[VT100\_COLOR\_END](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2aab87d1e19b4d687eb1fee07c73a33bd4)

@ VT100\_COLOR\_END

**Definition** shell\_types.h:26

[SHELL\_VT100\_COLOR\_GREEN](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a)

@ SHELL\_VT100\_COLOR\_GREEN

**Definition** shell\_types.h:17

[SHELL\_VT100\_COLOR\_BLUE](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2ace5b01755eec4567f0dc65e48143e33d)

@ SHELL\_VT100\_COLOR\_BLUE

**Definition** shell\_types.h:19

[SHELL\_VT100\_COLOR\_YELLOW](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d)

@ SHELL\_VT100\_COLOR\_YELLOW

**Definition** shell\_types.h:18

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[shell\_multiline\_cons](structshell__multiline__cons.md)

**Definition** shell\_types.h:34

[shell\_multiline\_cons::cur\_y\_end](structshell__multiline__cons.md#a0a07e8991006b34f111d068e22800d28)

uint16\_t cur\_y\_end

vertical cursor position at the end of command.

**Definition** shell\_types.h:38

[shell\_multiline\_cons::cur\_y](structshell__multiline__cons.md#a0ee84724f4b26ee2933c88b170445d93)

uint16\_t cur\_y

vertical cursor position in edited command.

**Definition** shell\_types.h:37

[shell\_multiline\_cons::terminal\_wid](structshell__multiline__cons.md#a48b37c8d0cc4584ab05299be34008575)

uint16\_t terminal\_wid

terminal screen width.

**Definition** shell\_types.h:40

[shell\_multiline\_cons::cur\_x](structshell__multiline__cons.md#a52a43a16f9d2e30d82dfe019384b0f7b)

uint16\_t cur\_x

horizontal cursor position in edited command line.

**Definition** shell\_types.h:35

[shell\_multiline\_cons::cur\_x\_end](structshell__multiline__cons.md#a54a051c1e085644e6cd1e86284fabf0d)

uint16\_t cur\_x\_end

horizontal cursor position at the end of command.

**Definition** shell\_types.h:36

[shell\_multiline\_cons::name\_len](structshell__multiline__cons.md#aa4ed5794533137992a2a9d3e7eb12f6a)

uint8\_t name\_len

console name length.

**Definition** shell\_types.h:41

[shell\_multiline\_cons::terminal\_hei](structshell__multiline__cons.md#ae65c3c25e87841be58347cf54b5c36d8)

uint16\_t terminal\_hei

terminal screen height.

**Definition** shell\_types.h:39

[shell\_vt100\_colors](structshell__vt100__colors.md)

**Definition** shell\_types.h:29

[shell\_vt100\_colors::bgcol](structshell__vt100__colors.md#a085471a594831d7b585f6d9b02bc8216)

enum shell\_vt100\_color bgcol

Background color.

**Definition** shell\_types.h:31

[shell\_vt100\_colors::col](structshell__vt100__colors.md#a4f75bb7b94c553ef7a704293fc98bde8)

enum shell\_vt100\_color col

Text color.

**Definition** shell\_types.h:30

[shell\_vt100\_ctx](structshell__vt100__ctx.md)

**Definition** shell\_types.h:44

[shell\_vt100\_ctx::printed\_cmd](structshell__vt100__ctx.md#a46443b4cd885a900fb3b9afe143dbb6d)

uint16\_t printed\_cmd

printed commands counter

**Definition** shell\_types.h:47

[shell\_vt100\_ctx::cons](structshell__vt100__ctx.md#a600ef23980af7daf7d4abcba9043b448)

struct shell\_multiline\_cons cons

**Definition** shell\_types.h:45

[shell\_vt100\_ctx::col](structshell__vt100__ctx.md#abc658a8e804ad3afcd3384e621cd8179)

struct shell\_vt100\_colors col

**Definition** shell\_types.h:46

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_types.h](shell__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
