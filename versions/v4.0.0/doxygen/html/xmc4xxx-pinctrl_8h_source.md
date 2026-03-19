---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/xmc4xxx-pinctrl_8h_source.html
original_path: doxygen/html/xmc4xxx-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xmc4xxx-pinctrl.h

[Go to the documentation of this file.](xmc4xxx-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2022 Schlumberger

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_XMC4XXX\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_XMC4XXX\_PINCTRL\_H\_

9

10/\* Bit Masks \*/

11

[ 12](xmc4xxx-pinctrl_8h.md#aab30618ebe31012b3bf6a72d55f9335c)#define XMC4XXX\_PORT\_POS 0

[ 13](xmc4xxx-pinctrl_8h.md#a99aa017fa346da406fca137d0c42c1e4)#define XMC4XXX\_PORT\_MASK 0xf

14

[ 15](xmc4xxx-pinctrl_8h.md#a511179d787ebfbb7f37a92326d4a8984)#define XMC4XXX\_PIN\_POS 4

[ 16](xmc4xxx-pinctrl_8h.md#a693fe19f7d6073121d89c4bd6dbff99b)#define XMC4XXX\_PIN\_MASK 0xf

17

[ 18](xmc4xxx-pinctrl_8h.md#a532151552d5ea717d093deb4c9c9d233)#define XMC4XXX\_ALT\_POS 8

[ 19](xmc4xxx-pinctrl_8h.md#aba9bea82a961c304cb90a7c24527d531)#define XMC4XXX\_ALT\_MASK 0xf

20

[ 21](xmc4xxx-pinctrl_8h.md#ac6ec7a70bdaae2909baea4f179327871)#define XMC4XXX\_PULL\_DOWN\_POS 12

[ 22](xmc4xxx-pinctrl_8h.md#ac202c2ad9b97865b1d7f9d282c9a7d10)#define XMC4XXX\_PULL\_DOWN\_MASK 0x1

23

[ 24](xmc4xxx-pinctrl_8h.md#a87e81f7624a28d5fea5ad3a2074329a0)#define XMC4XXX\_PULL\_UP\_POS 13

[ 25](xmc4xxx-pinctrl_8h.md#ac165407103a525da4919fee7c4dc22c9)#define XMC4XXX\_PULL\_UP\_MASK 0x1

26

[ 27](xmc4xxx-pinctrl_8h.md#a9f50c28d310a0cc771b979e731c05060)#define XMC4XXX\_PUSH\_PULL\_POS 14

[ 28](xmc4xxx-pinctrl_8h.md#a308fe5c756b2058b2eec25d9e95d439a)#define XMC4XXX\_PUSH\_PULL\_MASK 0x1

29

[ 30](xmc4xxx-pinctrl_8h.md#ad8da22497d5f36d3cd56477506eca3b5)#define XMC4XXX\_OPEN\_DRAIN\_POS 15

[ 31](xmc4xxx-pinctrl_8h.md#a4dbdbb0b4fe95db634c55b7840a08a47)#define XMC4XXX\_OPEN\_DRAIN\_MASK 0x1

32

[ 33](xmc4xxx-pinctrl_8h.md#ada9fafd51a6d8e7e6b4f2b05bf2d3dd0)#define XMC4XXX\_OUT\_HIGH\_POS 16

[ 34](xmc4xxx-pinctrl_8h.md#a58396a809d6950afd8b5cc6fd4193589)#define XMC4XXX\_OUT\_HIGH\_MASK 0x1

35

[ 36](xmc4xxx-pinctrl_8h.md#abbac18ae6e6d52b33db5b352ca323e11)#define XMC4XXX\_OUT\_LOW\_POS 17

[ 37](xmc4xxx-pinctrl_8h.md#af8c9d1c2e5664ff59538c08b4ed8fa8b)#define XMC4XXX\_OUT\_LOW\_MASK 0x1

38

[ 39](xmc4xxx-pinctrl_8h.md#a2da9db848ad0c85751747df0f3948f97)#define XMC4XXX\_INV\_INPUT\_POS 18

[ 40](xmc4xxx-pinctrl_8h.md#aab423e91fbddbe908d9393447ff943f0)#define XMC4XXX\_INV\_INPUT\_MASK 0x1

41

[ 42](xmc4xxx-pinctrl_8h.md#ac8284e39124ff71b5335e46e56fb8000)#define XMC4XXX\_DRIVE\_POS 19

[ 43](xmc4xxx-pinctrl_8h.md#aa6829bced6bf9f7908e31fb3c9205f93)#define XMC4XXX\_DRIVE\_MASK 0x7

44

[ 45](xmc4xxx-pinctrl_8h.md#a80e80262f3abb20055891211ee43201a)#define XMC4XXX\_HWCTRL\_POS 22

[ 46](xmc4xxx-pinctrl_8h.md#a0fc560c059b8fabf8e811e81783f5e2a)#define XMC4XXX\_HWCTRL\_MASK 0x3

47

48/\* Setters and getters \*/

49

[ 50](xmc4xxx-pinctrl_8h.md#a30211ecff4f4b6b3f02386ae55d1cb8d)#define XMC4XXX\_PINMUX\_SET(port, pin, alt\_fun) \

51 ((port) << XMC4XXX\_PORT\_POS | (pin) << XMC4XXX\_PIN\_POS | (alt\_fun) << XMC4XXX\_ALT\_POS)

52

[ 53](xmc4xxx-pinctrl_8h.md#ae0748e6dbb9ca36ad0ab40e3a53daea2)#define XMC4XXX\_PINMUX\_GET\_PORT(mx) ((mx >> XMC4XXX\_PORT\_POS) & XMC4XXX\_PORT\_MASK)

[ 54](xmc4xxx-pinctrl_8h.md#a3d889d7f75a6b88b252cb13f3004ea6a)#define XMC4XXX\_PINMUX\_GET\_PIN(mx) ((mx >> XMC4XXX\_PIN\_POS) & XMC4XXX\_PIN\_MASK)

[ 55](xmc4xxx-pinctrl_8h.md#afdad7ccafbdee5a2b1d512f0e280abfe)#define XMC4XXX\_PINMUX\_GET\_ALT(mx) ((mx >> XMC4XXX\_ALT\_POS) & XMC4XXX\_ALT\_MASK)

[ 56](xmc4xxx-pinctrl_8h.md#a56ebba3de971f70ad47005cf0a5246c1)#define XMC4XXX\_PINMUX\_GET\_PULL\_DOWN(mx) ((mx >> XMC4XXX\_PULL\_DOWN\_POS) & XMC4XXX\_PULL\_DOWN\_MASK)

[ 57](xmc4xxx-pinctrl_8h.md#ac28a73b740da97d7d0008ab0af577a92)#define XMC4XXX\_PINMUX\_GET\_PULL\_UP(mx) ((mx >> XMC4XXX\_PULL\_UP\_POS) & XMC4XXX\_PULL\_UP\_MASK)

[ 58](xmc4xxx-pinctrl_8h.md#a376e85562e0dc5a1ea2c9f3b8eaeeb9e)#define XMC4XXX\_PINMUX\_GET\_PUSH\_PULL(mx) ((mx >> XMC4XXX\_PUSH\_PULL\_POS) & XMC4XXX\_PUSH\_PULL\_MASK)

[ 59](xmc4xxx-pinctrl_8h.md#a57626f3b88704a87ed5f9bfba44c8daf)#define XMC4XXX\_PINMUX\_GET\_OPEN\_DRAIN(mx) ((mx >> XMC4XXX\_OPEN\_DRAIN\_POS) & XMC4XXX\_OPEN\_DRAIN\_MASK)

[ 60](xmc4xxx-pinctrl_8h.md#a1de2bc4e89167d9a0399edf63078d928)#define XMC4XXX\_PINMUX\_GET\_OUT\_HIGH(mx) ((mx >> XMC4XXX\_OUT\_HIGH\_POS) & XMC4XXX\_OUT\_HIGH\_MASK)

[ 61](xmc4xxx-pinctrl_8h.md#abbeef6122d273c9f074fb1cc5456febf)#define XMC4XXX\_PINMUX\_GET\_OUT\_LOW(mx) ((mx >> XMC4XXX\_OUT\_LOW\_POS) & XMC4XXX\_OUT\_LOW\_MASK)

[ 62](xmc4xxx-pinctrl_8h.md#a43ce0d809351bef0989f0330073f9453)#define XMC4XXX\_PINMUX\_GET\_INV\_INPUT(mx) ((mx >> XMC4XXX\_INV\_INPUT\_POS) & XMC4XXX\_INV\_INPUT\_MASK)

[ 63](xmc4xxx-pinctrl_8h.md#a11bd50351e3aabed088cc4158474edc3)#define XMC4XXX\_PINMUX\_GET\_DRIVE(mx) ((mx >> XMC4XXX\_DRIVE\_POS) & XMC4XXX\_DRIVE\_MASK)

[ 64](xmc4xxx-pinctrl_8h.md#a33694b664b4212d95cc18659173675c0)#define XMC4XXX\_PINMUX\_GET\_HWCTRL(mx) ((mx >> XMC4XXX\_HWCTRL\_POS) & XMC4XXX\_HWCTRL\_MASK)

65

66#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_XMC4XXX\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [xmc4xxx-pinctrl.h](xmc4xxx-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
