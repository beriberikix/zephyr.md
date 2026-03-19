---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/avrcp_8h_source.html
original_path: doxygen/html/avrcp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

avrcp.h

[Go to the documentation of this file.](avrcp_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \* Copyright (C) 2024 Xiaomi Corporation

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AVRCP\_H\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AVRCP\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 20](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618e)typedef enum \_\_packed {

[ 21](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618ea1a2aa36da42f3751f3a94b218118ae04) [BT\_AVRCP\_CTYPE\_CONTROL](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618ea1a2aa36da42f3751f3a94b218118ae04) = 0x0,

[ 22](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618ea9a1b0564c98a0637a2ca5a0b97c3e6ce) [BT\_AVRCP\_CTYPE\_STATUS](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618ea9a1b0564c98a0637a2ca5a0b97c3e6ce) = 0x1,

[ 23](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618eac4c9dfbce497d9a043d7ac42ee932bdb) [BT\_AVRCP\_CTYPE\_SPECIFIC\_INQUIRY](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618eac4c9dfbce497d9a043d7ac42ee932bdb) = 0x2,

[ 24](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618ead58dcc95df3973a7bed94068be913290) [BT\_AVRCP\_CTYPE\_NOTIFY](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618ead58dcc95df3973a7bed94068be913290) = 0x3,

[ 25](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618ea0eefcdda49616cf818efdc0a7b5975f7) [BT\_AVRCP\_CTYPE\_GENERAL\_INQUIRY](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618ea0eefcdda49616cf818efdc0a7b5975f7) = 0x4,

26} [bt\_avrcp\_ctype\_t](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618e);

27

[ 29](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326)typedef enum \_\_packed {

[ 30](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a8a4cfe6ca8f5b92402c029d02b625696) [BT\_AVRCP\_RSP\_NOT\_IMPLEMENTED](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a8a4cfe6ca8f5b92402c029d02b625696) = 0x8,

[ 31](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a2c93dc0bfd19305d8012b73001989cd8) [BT\_AVRCP\_RSP\_ACCEPTED](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a2c93dc0bfd19305d8012b73001989cd8) = 0x9,

[ 32](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a1775849a3c303b61975c569cc85e943c) [BT\_AVRCP\_RSP\_REJECTED](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a1775849a3c303b61975c569cc85e943c) = 0xa,

[ 33](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326ab4b63e5cf84ea34895702ceea5ae81ad) [BT\_AVRCP\_RSP\_IN\_TRANSITION](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326ab4b63e5cf84ea34895702ceea5ae81ad) = 0xb,

[ 34](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326aa49f2871cf4e5f493128f574ad0d6144) [BT\_AVRCP\_RSP\_IMPLEMENTED](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326aa49f2871cf4e5f493128f574ad0d6144) = 0xc,

[ 35](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a4136d697a8a0ea5daa1a6e89b314b992) [BT\_AVRCP\_RSP\_STABLE](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a4136d697a8a0ea5daa1a6e89b314b992) = 0xc,

[ 36](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326acf6f13da82b371efbcdf03fbedcb6988) [BT\_AVRCP\_RSP\_CHANGED](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326acf6f13da82b371efbcdf03fbedcb6988) = 0xd,

[ 37](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a4a2ed58a814be12b93753a6458b15e88) [BT\_AVRCP\_RSP\_INTERIM](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a4a2ed58a814be12b93753a6458b15e88) = 0xf,

38} [bt\_avrcp\_rsp\_t](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326);

39

[ 41](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84)typedef enum \_\_packed {

[ 42](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84acbaded78ac1e41d16464ea9db667c27f) [BT\_AVRCP\_OPID\_SELECT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84acbaded78ac1e41d16464ea9db667c27f) = 0x00,

[ 43](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84aae8fe4a27cf2b70bb289f38d4016b9d9) [BT\_AVRCP\_OPID\_UP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84aae8fe4a27cf2b70bb289f38d4016b9d9) = 0x01,

[ 44](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a0d81584ba5cc6bb9c790b87fcf638537) [BT\_AVRCP\_OPID\_DOWN](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a0d81584ba5cc6bb9c790b87fcf638537) = 0x02,

[ 45](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a734fa5664a306957cb28eec36806e4ba) [BT\_AVRCP\_OPID\_LEFT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a734fa5664a306957cb28eec36806e4ba) = 0x03,

[ 46](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a9030a666a42a54b02b4c7f876f1ae9d2) [BT\_AVRCP\_OPID\_RIGHT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a9030a666a42a54b02b4c7f876f1ae9d2) = 0x04,

[ 47](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a831592a4b2634815f9716e80252dce63) [BT\_AVRCP\_OPID\_RIGHT\_UP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a831592a4b2634815f9716e80252dce63) = 0x05,

[ 48](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a61d7145a6aa482256cd8aaad7bb96745) [BT\_AVRCP\_OPID\_RIGHT\_DOWN](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a61d7145a6aa482256cd8aaad7bb96745) = 0x06,

[ 49](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a8445dd492ab9e6a9b387162f2f7ab779) [BT\_AVRCP\_OPID\_LEFT\_UP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a8445dd492ab9e6a9b387162f2f7ab779) = 0x07,

[ 50](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a6660a000e5bc1d8ead271924a3780366) [BT\_AVRCP\_OPID\_LEFT\_DOWN](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a6660a000e5bc1d8ead271924a3780366) = 0x08,

[ 51](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a002efdb93a2dd52bb5bbec05d9537f87) [BT\_AVRCP\_OPID\_ROOT\_MENU](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a002efdb93a2dd52bb5bbec05d9537f87) = 0x09,

[ 52](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a827d1eaa2f12a37219fc1f78f617d372) [BT\_AVRCP\_OPID\_SETUP\_MENU](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a827d1eaa2f12a37219fc1f78f617d372) = 0x0a,

[ 53](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84aa9d64afb98b2fc91cae3810990451472) [BT\_AVRCP\_OPID\_CONTENTS\_MENU](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84aa9d64afb98b2fc91cae3810990451472) = 0x0b,

[ 54](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a470fa709a8a7e35ec12a593ae9dd1574) [BT\_AVRCP\_OPID\_FAVORITE\_MENU](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a470fa709a8a7e35ec12a593ae9dd1574) = 0x0c,

[ 55](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a9ecca98aa1f55ee6a2b6824e0940a7c3) [BT\_AVRCP\_OPID\_EXIT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a9ecca98aa1f55ee6a2b6824e0940a7c3) = 0x0d,

56

[ 57](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ae6430b447ccd9e15d0ef2ae62152bade) [BT\_AVRCP\_OPID\_0](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ae6430b447ccd9e15d0ef2ae62152bade) = 0x20,

[ 58](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a94ca82a18f2c06379160e69675d927d0) [BT\_AVRCP\_OPID\_1](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a94ca82a18f2c06379160e69675d927d0) = 0x21,

[ 59](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84acb3f6e1f71628853bb457bfb8163c566) [BT\_AVRCP\_OPID\_2](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84acb3f6e1f71628853bb457bfb8163c566) = 0x22,

[ 60](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84af1d1ea7e57a0a16c8e6ad8b9961d4459) [BT\_AVRCP\_OPID\_3](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84af1d1ea7e57a0a16c8e6ad8b9961d4459) = 0x23,

[ 61](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a23d18efccc7b1940e72b62b08fa5ab6c) [BT\_AVRCP\_OPID\_4](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a23d18efccc7b1940e72b62b08fa5ab6c) = 0x24,

[ 62](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a91a40f7dfb02c38cd7998adf5fe948b5) [BT\_AVRCP\_OPID\_5](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a91a40f7dfb02c38cd7998adf5fe948b5) = 0x25,

[ 63](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a029017bcc52cf7c4ffac3db5f92f4e2a) [BT\_AVRCP\_OPID\_6](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a029017bcc52cf7c4ffac3db5f92f4e2a) = 0x26,

[ 64](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84aac755d13a6f53ead21818a9fb90217ff) [BT\_AVRCP\_OPID\_7](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84aac755d13a6f53ead21818a9fb90217ff) = 0x27,

[ 65](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ac751478296cc6a9e5de77fdf3c8fce06) [BT\_AVRCP\_OPID\_8](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ac751478296cc6a9e5de77fdf3c8fce06) = 0x28,

[ 66](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a07ed4fda3e230d4e95576a25c6d02dcb) [BT\_AVRCP\_OPID\_9](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a07ed4fda3e230d4e95576a25c6d02dcb) = 0x29,

[ 67](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a5d3a33be8473fc401e3f38a9f234debf) [BT\_AVRCP\_OPID\_DOT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a5d3a33be8473fc401e3f38a9f234debf) = 0x2a,

[ 68](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a28d5c8b1960aa1e70c0659c40cac32ae) [BT\_AVRCP\_OPID\_ENTER](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a28d5c8b1960aa1e70c0659c40cac32ae) = 0x2b,

[ 69](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ae6046a270ff9f8939059248cddc7a8a2) [BT\_AVRCP\_OPID\_CLEAR](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ae6046a270ff9f8939059248cddc7a8a2) = 0x2c,

70

[ 71](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ad39e69c55c571eb3c2492d5aa086e586) [BT\_AVRCP\_OPID\_CHANNEL\_UP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ad39e69c55c571eb3c2492d5aa086e586) = 0x30,

[ 72](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a300bbf8fe3236a55bfc97e2d7d8323de) [BT\_AVRCP\_OPID\_CHANNEL\_DOWN](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a300bbf8fe3236a55bfc97e2d7d8323de) = 0x31,

[ 73](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a3e59a9dc846182d2bc26cf2e5960558e) [BT\_AVRCP\_OPID\_PREVIOUS\_CHANNEL](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a3e59a9dc846182d2bc26cf2e5960558e) = 0x32,

[ 74](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a1fb2420a2130a9f22f1837c0c3e0896b) [BT\_AVRCP\_OPID\_SOUND\_SELECT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a1fb2420a2130a9f22f1837c0c3e0896b) = 0x33,

[ 75](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a8fa3d0ac9fc3feefedf3b2d370df748c) [BT\_AVRCP\_OPID\_INPUT\_SELECT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a8fa3d0ac9fc3feefedf3b2d370df748c) = 0x34,

[ 76](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a735b97b85b1183c862955131a09b1eef) [BT\_AVRCP\_OPID\_DISPLAY\_INFORMATION](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a735b97b85b1183c862955131a09b1eef) = 0x35,

[ 77](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ab3a7619c2c3cafe2eab868d471c8066b) [BT\_AVRCP\_OPID\_HELP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ab3a7619c2c3cafe2eab868d471c8066b) = 0x36,

[ 78](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a93ffda310d3a0999256b42cd4652e321) [BT\_AVRCP\_OPID\_PAGE\_UP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a93ffda310d3a0999256b42cd4652e321) = 0x37,

[ 79](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a3078b64d3c759e83d04923ca6bcf079a) [BT\_AVRCP\_OPID\_PAGE\_DOWN](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a3078b64d3c759e83d04923ca6bcf079a) = 0x38,

80

[ 81](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a9623c492b7a04750fb3938dde65a9358) [BT\_AVRCP\_OPID\_POWER](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a9623c492b7a04750fb3938dde65a9358) = 0x40,

[ 82](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84af5f5b89b6f81961f7bf235c91f59b487) [BT\_AVRCP\_OPID\_VOLUME\_UP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84af5f5b89b6f81961f7bf235c91f59b487) = 0x41,

[ 83](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a49d2a954862bdf45c30ed734e5a29a62) [BT\_AVRCP\_OPID\_VOLUME\_DOWN](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a49d2a954862bdf45c30ed734e5a29a62) = 0x42,

[ 84](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a5c37fbe03a5e7b8cda842262f7a504e1) [BT\_AVRCP\_OPID\_MUTE](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a5c37fbe03a5e7b8cda842262f7a504e1) = 0x43,

[ 85](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ae76461b7c08169ad190a83545b9e584b) [BT\_AVRCP\_OPID\_PLAY](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ae76461b7c08169ad190a83545b9e584b) = 0x44,

[ 86](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a69254767fc4183e1534b12cd6bd88f60) [BT\_AVRCP\_OPID\_STOP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a69254767fc4183e1534b12cd6bd88f60) = 0x45,

[ 87](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a0e7877d88781dbacdac095c7d36f186a) [BT\_AVRCP\_OPID\_PAUSE](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a0e7877d88781dbacdac095c7d36f186a) = 0x46,

[ 88](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a8364f5d44be3b666f5d995368e3dda27) [BT\_AVRCP\_OPID\_RECORD](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a8364f5d44be3b666f5d995368e3dda27) = 0x47,

[ 89](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a4bba25ed6730766902ecb92e4f546dc8) [BT\_AVRCP\_OPID\_REWIND](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a4bba25ed6730766902ecb92e4f546dc8) = 0x48,

[ 90](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a6c83aff2115939aa17f6bbd68c792e4f) [BT\_AVRCP\_OPID\_FAST\_FORWARD](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a6c83aff2115939aa17f6bbd68c792e4f) = 0x49,

[ 91](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ae34d68953054ef4446403a1e240e3344) [BT\_AVRCP\_OPID\_EJECT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ae34d68953054ef4446403a1e240e3344) = 0x4a,

[ 92](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a004689a6684c527035f06fa8d715a09e) [BT\_AVRCP\_OPID\_FORWARD](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a004689a6684c527035f06fa8d715a09e) = 0x4b,

[ 93](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a0030ffc7149baf83def17e4e2be76f23) [BT\_AVRCP\_OPID\_BACKWARD](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a0030ffc7149baf83def17e4e2be76f23) = 0x4c,

94

[ 95](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84afc51d7bc6acd64c3dbeb1f10a06113c2) [BT\_AVRCP\_OPID\_ANGLE](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84afc51d7bc6acd64c3dbeb1f10a06113c2) = 0x50,

[ 96](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ac1e3dd409b98c71eaf12567ce5028a98) [BT\_AVRCP\_OPID\_SUBPICTURE](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ac1e3dd409b98c71eaf12567ce5028a98) = 0x51,

97

[ 98](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a91595d93490cfe27e239c799e927b2b5) [BT\_AVRCP\_OPID\_F1](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a91595d93490cfe27e239c799e927b2b5) = 0x71,

[ 99](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a8b0656fed7b936e131a5c9dbdb32a7a4) [BT\_AVRCP\_OPID\_F2](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a8b0656fed7b936e131a5c9dbdb32a7a4) = 0x72,

[ 100](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a1380078d446b892a25b8b2d28a405e40) [BT\_AVRCP\_OPID\_F3](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a1380078d446b892a25b8b2d28a405e40) = 0x73,

[ 101](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a01fc4e91d59b8c530fe142d2f1c95283) [BT\_AVRCP\_OPID\_F4](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a01fc4e91d59b8c530fe142d2f1c95283) = 0x74,

[ 102](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a86a61c08b203d0bcc8b8a3ed5090ef7d) [BT\_AVRCP\_OPID\_F5](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a86a61c08b203d0bcc8b8a3ed5090ef7d) = 0x75,

[ 103](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ad6eac39b4aced31534fde97a411b8c4d) [BT\_AVRCP\_OPID\_VENDOR\_UNIQUE](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ad6eac39b4aced31534fde97a411b8c4d) = 0x7e,

104} [bt\_avrcp\_opid\_t](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84);

105

[ 107](avrcp_8h.md#a15f9f868b056f17ea12d96530b7da881)typedef enum \_\_packed {

[ 108](avrcp_8h.md#a15f9f868b056f17ea12d96530b7da881a1465f08940f04a7b35832e6d5f73a4e3) [BT\_AVRCP\_BUTTON\_PRESSED](avrcp_8h.md#a15f9f868b056f17ea12d96530b7da881a1465f08940f04a7b35832e6d5f73a4e3) = 0,

[ 109](avrcp_8h.md#a15f9f868b056f17ea12d96530b7da881a0eb47ec4ca3d7e0bf613de53d5e50706) [BT\_AVRCP\_BUTTON\_RELEASED](avrcp_8h.md#a15f9f868b056f17ea12d96530b7da881a0eb47ec4ca3d7e0bf613de53d5e50706) = 1,

110} [bt\_avrcp\_button\_state\_t](avrcp_8h.md#a15f9f868b056f17ea12d96530b7da881);

111

113struct bt\_avrcp;

114

[ 115](structbt__avrcp__unit__info__rsp.md)struct [bt\_avrcp\_unit\_info\_rsp](structbt__avrcp__unit__info__rsp.md) {

[ 116](structbt__avrcp__unit__info__rsp.md#af799f80a07f3e4f523b55d12820c93c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [unit\_type](structbt__avrcp__unit__info__rsp.md#af799f80a07f3e4f523b55d12820c93c0);

[ 117](structbt__avrcp__unit__info__rsp.md#a0225755bf457bc6d4046d8172af49217) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [company\_id](structbt__avrcp__unit__info__rsp.md#a0225755bf457bc6d4046d8172af49217);

118};

119

[ 120](structbt__avrcp__subunit__info__rsp.md)struct [bt\_avrcp\_subunit\_info\_rsp](structbt__avrcp__subunit__info__rsp.md) {

[ 121](structbt__avrcp__subunit__info__rsp.md#a70bffb3209acd47beb37aeeb1700bfad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subunit\_type](structbt__avrcp__subunit__info__rsp.md#a70bffb3209acd47beb37aeeb1700bfad);

[ 122](structbt__avrcp__subunit__info__rsp.md#a85cf595920ba2dbf9f0e4deca1d27483) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_subunit\_id](structbt__avrcp__subunit__info__rsp.md#a85cf595920ba2dbf9f0e4deca1d27483);

[ 123](structbt__avrcp__subunit__info__rsp.md#a47b69412c61682ed336737f34ac614dc) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[extended\_subunit\_type](structbt__avrcp__subunit__info__rsp.md#a47b69412c61682ed336737f34ac614dc);

[ 124](structbt__avrcp__subunit__info__rsp.md#a0be33096e6edf251c23a5322b3c30421) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[extended\_subunit\_id](structbt__avrcp__subunit__info__rsp.md#a0be33096e6edf251c23a5322b3c30421);

125};

126

[ 127](structbt__avrcp__passthrough__rsp.md)struct [bt\_avrcp\_passthrough\_rsp](structbt__avrcp__passthrough__rsp.md) {

[ 128](structbt__avrcp__passthrough__rsp.md#a90c8c59bf3f333fa06d2b49d6e58af19) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response](structbt__avrcp__passthrough__rsp.md#a90c8c59bf3f333fa06d2b49d6e58af19);

[ 129](structbt__avrcp__passthrough__rsp.md#a940eb51fabd1987016f6888d1b38c18e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [operation\_id](structbt__avrcp__passthrough__rsp.md#a940eb51fabd1987016f6888d1b38c18e);

[ 130](structbt__avrcp__passthrough__rsp.md#aaa4ab701c9dee8d2ce8b4676f3ae140b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](structbt__avrcp__passthrough__rsp.md#aaa4ab701c9dee8d2ce8b4676f3ae140b);

[ 131](structbt__avrcp__passthrough__rsp.md#ad657103f9c751ba1e5fb1d447aff1718) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__avrcp__passthrough__rsp.md#ad657103f9c751ba1e5fb1d447aff1718);

[ 132](structbt__avrcp__passthrough__rsp.md#a9bd874797764bafb73a5663ccbb30bf8) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[payload](structbt__avrcp__passthrough__rsp.md#a9bd874797764bafb73a5663ccbb30bf8);

133};

134

[ 135](structbt__avrcp__cb.md)struct [bt\_avrcp\_cb](structbt__avrcp__cb.md) {

[ 143](structbt__avrcp__cb.md#ac9b46b911f061a588cf87dd381364d0f) void (\*[connected](structbt__avrcp__cb.md#ac9b46b911f061a588cf87dd381364d0f))(struct bt\_avrcp \*avrcp);

144

[ 152](structbt__avrcp__cb.md#acea85b2e1da11e0fd5835ce18c67ded1) void (\*[disconnected](structbt__avrcp__cb.md#acea85b2e1da11e0fd5835ce18c67ded1))(struct bt\_avrcp \*avrcp);

153

[ 161](structbt__avrcp__cb.md#ad2ea0d60add3fde24c291159cf365596) void (\*[unit\_info\_rsp](structbt__avrcp__cb.md#ad2ea0d60add3fde24c291159cf365596))(struct bt\_avrcp \*avrcp, struct [bt\_avrcp\_unit\_info\_rsp](structbt__avrcp__unit__info__rsp.md) \*rsp);

162

[ 170](structbt__avrcp__cb.md#a75343c9da504a3dfa12e5f1959c9c58b) void (\*[subunit\_info\_rsp](structbt__avrcp__cb.md#a75343c9da504a3dfa12e5f1959c9c58b))(struct bt\_avrcp \*avrcp, struct [bt\_avrcp\_subunit\_info\_rsp](structbt__avrcp__subunit__info__rsp.md) \*rsp);

171

[ 179](structbt__avrcp__cb.md#a55be9880812b2e8fcc97480e1f0359dd) void (\*[passthrough\_rsp](structbt__avrcp__cb.md#a55be9880812b2e8fcc97480e1f0359dd))(struct bt\_avrcp \*avrcp, struct [bt\_avrcp\_passthrough\_rsp](structbt__avrcp__passthrough__rsp.md) \*rsp);

180};

181

[ 193](avrcp_8h.md#addc1f4f530b9e3eb4a669fe606479c59)struct bt\_avrcp \*[bt\_avrcp\_connect](avrcp_8h.md#addc1f4f530b9e3eb4a669fe606479c59)(struct bt\_conn \*conn);

194

[ 203](avrcp_8h.md#af68c54ea0b17ebaa9872d271b0fee9bd)int [bt\_avrcp\_disconnect](avrcp_8h.md#af68c54ea0b17ebaa9872d271b0fee9bd)(struct bt\_avrcp \*avrcp);

204

[ 213](avrcp_8h.md#aedb1bc8dd553aa44fdaec2b9f5c76607)int [bt\_avrcp\_register\_cb](avrcp_8h.md#aedb1bc8dd553aa44fdaec2b9f5c76607)(const struct [bt\_avrcp\_cb](structbt__avrcp__cb.md) \*cb);

214

[ 223](avrcp_8h.md#aba521a01fea4e7aee8b40ba72ca10bcf)int [bt\_avrcp\_get\_unit\_info](avrcp_8h.md#aba521a01fea4e7aee8b40ba72ca10bcf)(struct bt\_avrcp \*avrcp);

224

[ 234](avrcp_8h.md#a127eaf05867a84fb5183e044fdfb55c0)int [bt\_avrcp\_get\_subunit\_info](avrcp_8h.md#a127eaf05867a84fb5183e044fdfb55c0)(struct bt\_avrcp \*avrcp);

235

[ 249](avrcp_8h.md#afeea270bacac6a59af74c02fc1d98945)int [bt\_avrcp\_passthrough](avrcp_8h.md#afeea270bacac6a59af74c02fc1d98945)(struct bt\_avrcp \*avrcp, [bt\_avrcp\_opid\_t](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84) operation\_id,

250 [bt\_avrcp\_button\_state\_t](avrcp_8h.md#a15f9f868b056f17ea12d96530b7da881) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len);

251

252#ifdef \_\_cplusplus

253}

254#endif

255

256#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AVRCP\_H\_ \*/

[bt\_avrcp\_get\_subunit\_info](avrcp_8h.md#a127eaf05867a84fb5183e044fdfb55c0)

int bt\_avrcp\_get\_subunit\_info(struct bt\_avrcp \*avrcp)

Get AVRCP Subunit Info.

[bt\_avrcp\_button\_state\_t](avrcp_8h.md#a15f9f868b056f17ea12d96530b7da881)

bt\_avrcp\_button\_state\_t

AVRCP button state flag.

**Definition** avrcp.h:107

[BT\_AVRCP\_BUTTON\_RELEASED](avrcp_8h.md#a15f9f868b056f17ea12d96530b7da881a0eb47ec4ca3d7e0bf613de53d5e50706)

@ BT\_AVRCP\_BUTTON\_RELEASED

**Definition** avrcp.h:109

[BT\_AVRCP\_BUTTON\_PRESSED](avrcp_8h.md#a15f9f868b056f17ea12d96530b7da881a1465f08940f04a7b35832e6d5f73a4e3)

@ BT\_AVRCP\_BUTTON\_PRESSED

**Definition** avrcp.h:108

[bt\_avrcp\_ctype\_t](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618e)

bt\_avrcp\_ctype\_t

AV/C command types.

**Definition** avrcp.h:20

[BT\_AVRCP\_CTYPE\_GENERAL\_INQUIRY](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618ea0eefcdda49616cf818efdc0a7b5975f7)

@ BT\_AVRCP\_CTYPE\_GENERAL\_INQUIRY

**Definition** avrcp.h:25

[BT\_AVRCP\_CTYPE\_CONTROL](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618ea1a2aa36da42f3751f3a94b218118ae04)

@ BT\_AVRCP\_CTYPE\_CONTROL

**Definition** avrcp.h:21

[BT\_AVRCP\_CTYPE\_STATUS](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618ea9a1b0564c98a0637a2ca5a0b97c3e6ce)

@ BT\_AVRCP\_CTYPE\_STATUS

**Definition** avrcp.h:22

[BT\_AVRCP\_CTYPE\_SPECIFIC\_INQUIRY](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618eac4c9dfbce497d9a043d7ac42ee932bdb)

@ BT\_AVRCP\_CTYPE\_SPECIFIC\_INQUIRY

**Definition** avrcp.h:23

[BT\_AVRCP\_CTYPE\_NOTIFY](avrcp_8h.md#a2a4c610e00ba9832f954f30bd6b6618ead58dcc95df3973a7bed94068be913290)

@ BT\_AVRCP\_CTYPE\_NOTIFY

**Definition** avrcp.h:24

[bt\_avrcp\_opid\_t](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84)

bt\_avrcp\_opid\_t

AV/C operation ids used in AVRCP passthrough commands.

**Definition** avrcp.h:41

[BT\_AVRCP\_OPID\_ROOT\_MENU](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a002efdb93a2dd52bb5bbec05d9537f87)

@ BT\_AVRCP\_OPID\_ROOT\_MENU

**Definition** avrcp.h:51

[BT\_AVRCP\_OPID\_BACKWARD](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a0030ffc7149baf83def17e4e2be76f23)

@ BT\_AVRCP\_OPID\_BACKWARD

**Definition** avrcp.h:93

[BT\_AVRCP\_OPID\_FORWARD](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a004689a6684c527035f06fa8d715a09e)

@ BT\_AVRCP\_OPID\_FORWARD

**Definition** avrcp.h:92

[BT\_AVRCP\_OPID\_F4](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a01fc4e91d59b8c530fe142d2f1c95283)

@ BT\_AVRCP\_OPID\_F4

**Definition** avrcp.h:101

[BT\_AVRCP\_OPID\_6](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a029017bcc52cf7c4ffac3db5f92f4e2a)

@ BT\_AVRCP\_OPID\_6

**Definition** avrcp.h:63

[BT\_AVRCP\_OPID\_9](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a07ed4fda3e230d4e95576a25c6d02dcb)

@ BT\_AVRCP\_OPID\_9

**Definition** avrcp.h:66

[BT\_AVRCP\_OPID\_DOWN](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a0d81584ba5cc6bb9c790b87fcf638537)

@ BT\_AVRCP\_OPID\_DOWN

**Definition** avrcp.h:44

[BT\_AVRCP\_OPID\_PAUSE](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a0e7877d88781dbacdac095c7d36f186a)

@ BT\_AVRCP\_OPID\_PAUSE

**Definition** avrcp.h:87

[BT\_AVRCP\_OPID\_F3](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a1380078d446b892a25b8b2d28a405e40)

@ BT\_AVRCP\_OPID\_F3

**Definition** avrcp.h:100

[BT\_AVRCP\_OPID\_SOUND\_SELECT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a1fb2420a2130a9f22f1837c0c3e0896b)

@ BT\_AVRCP\_OPID\_SOUND\_SELECT

**Definition** avrcp.h:74

[BT\_AVRCP\_OPID\_4](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a23d18efccc7b1940e72b62b08fa5ab6c)

@ BT\_AVRCP\_OPID\_4

**Definition** avrcp.h:61

[BT\_AVRCP\_OPID\_ENTER](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a28d5c8b1960aa1e70c0659c40cac32ae)

@ BT\_AVRCP\_OPID\_ENTER

**Definition** avrcp.h:68

[BT\_AVRCP\_OPID\_CHANNEL\_DOWN](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a300bbf8fe3236a55bfc97e2d7d8323de)

@ BT\_AVRCP\_OPID\_CHANNEL\_DOWN

**Definition** avrcp.h:72

[BT\_AVRCP\_OPID\_PAGE\_DOWN](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a3078b64d3c759e83d04923ca6bcf079a)

@ BT\_AVRCP\_OPID\_PAGE\_DOWN

**Definition** avrcp.h:79

[BT\_AVRCP\_OPID\_PREVIOUS\_CHANNEL](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a3e59a9dc846182d2bc26cf2e5960558e)

@ BT\_AVRCP\_OPID\_PREVIOUS\_CHANNEL

**Definition** avrcp.h:73

[BT\_AVRCP\_OPID\_FAVORITE\_MENU](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a470fa709a8a7e35ec12a593ae9dd1574)

@ BT\_AVRCP\_OPID\_FAVORITE\_MENU

**Definition** avrcp.h:54

[BT\_AVRCP\_OPID\_VOLUME\_DOWN](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a49d2a954862bdf45c30ed734e5a29a62)

@ BT\_AVRCP\_OPID\_VOLUME\_DOWN

**Definition** avrcp.h:83

[BT\_AVRCP\_OPID\_REWIND](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a4bba25ed6730766902ecb92e4f546dc8)

@ BT\_AVRCP\_OPID\_REWIND

**Definition** avrcp.h:89

[BT\_AVRCP\_OPID\_MUTE](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a5c37fbe03a5e7b8cda842262f7a504e1)

@ BT\_AVRCP\_OPID\_MUTE

**Definition** avrcp.h:84

[BT\_AVRCP\_OPID\_DOT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a5d3a33be8473fc401e3f38a9f234debf)

@ BT\_AVRCP\_OPID\_DOT

**Definition** avrcp.h:67

[BT\_AVRCP\_OPID\_RIGHT\_DOWN](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a61d7145a6aa482256cd8aaad7bb96745)

@ BT\_AVRCP\_OPID\_RIGHT\_DOWN

**Definition** avrcp.h:48

[BT\_AVRCP\_OPID\_LEFT\_DOWN](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a6660a000e5bc1d8ead271924a3780366)

@ BT\_AVRCP\_OPID\_LEFT\_DOWN

**Definition** avrcp.h:50

[BT\_AVRCP\_OPID\_STOP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a69254767fc4183e1534b12cd6bd88f60)

@ BT\_AVRCP\_OPID\_STOP

**Definition** avrcp.h:86

[BT\_AVRCP\_OPID\_FAST\_FORWARD](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a6c83aff2115939aa17f6bbd68c792e4f)

@ BT\_AVRCP\_OPID\_FAST\_FORWARD

**Definition** avrcp.h:90

[BT\_AVRCP\_OPID\_LEFT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a734fa5664a306957cb28eec36806e4ba)

@ BT\_AVRCP\_OPID\_LEFT

**Definition** avrcp.h:45

[BT\_AVRCP\_OPID\_DISPLAY\_INFORMATION](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a735b97b85b1183c862955131a09b1eef)

@ BT\_AVRCP\_OPID\_DISPLAY\_INFORMATION

**Definition** avrcp.h:76

[BT\_AVRCP\_OPID\_SETUP\_MENU](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a827d1eaa2f12a37219fc1f78f617d372)

@ BT\_AVRCP\_OPID\_SETUP\_MENU

**Definition** avrcp.h:52

[BT\_AVRCP\_OPID\_RIGHT\_UP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a831592a4b2634815f9716e80252dce63)

@ BT\_AVRCP\_OPID\_RIGHT\_UP

**Definition** avrcp.h:47

[BT\_AVRCP\_OPID\_RECORD](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a8364f5d44be3b666f5d995368e3dda27)

@ BT\_AVRCP\_OPID\_RECORD

**Definition** avrcp.h:88

[BT\_AVRCP\_OPID\_LEFT\_UP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a8445dd492ab9e6a9b387162f2f7ab779)

@ BT\_AVRCP\_OPID\_LEFT\_UP

**Definition** avrcp.h:49

[BT\_AVRCP\_OPID\_F5](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a86a61c08b203d0bcc8b8a3ed5090ef7d)

@ BT\_AVRCP\_OPID\_F5

**Definition** avrcp.h:102

[BT\_AVRCP\_OPID\_F2](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a8b0656fed7b936e131a5c9dbdb32a7a4)

@ BT\_AVRCP\_OPID\_F2

**Definition** avrcp.h:99

[BT\_AVRCP\_OPID\_INPUT\_SELECT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a8fa3d0ac9fc3feefedf3b2d370df748c)

@ BT\_AVRCP\_OPID\_INPUT\_SELECT

**Definition** avrcp.h:75

[BT\_AVRCP\_OPID\_RIGHT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a9030a666a42a54b02b4c7f876f1ae9d2)

@ BT\_AVRCP\_OPID\_RIGHT

**Definition** avrcp.h:46

[BT\_AVRCP\_OPID\_F1](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a91595d93490cfe27e239c799e927b2b5)

@ BT\_AVRCP\_OPID\_F1

**Definition** avrcp.h:98

[BT\_AVRCP\_OPID\_5](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a91a40f7dfb02c38cd7998adf5fe948b5)

@ BT\_AVRCP\_OPID\_5

**Definition** avrcp.h:62

[BT\_AVRCP\_OPID\_PAGE\_UP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a93ffda310d3a0999256b42cd4652e321)

@ BT\_AVRCP\_OPID\_PAGE\_UP

**Definition** avrcp.h:78

[BT\_AVRCP\_OPID\_1](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a94ca82a18f2c06379160e69675d927d0)

@ BT\_AVRCP\_OPID\_1

**Definition** avrcp.h:58

[BT\_AVRCP\_OPID\_POWER](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a9623c492b7a04750fb3938dde65a9358)

@ BT\_AVRCP\_OPID\_POWER

**Definition** avrcp.h:81

[BT\_AVRCP\_OPID\_EXIT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84a9ecca98aa1f55ee6a2b6824e0940a7c3)

@ BT\_AVRCP\_OPID\_EXIT

**Definition** avrcp.h:55

[BT\_AVRCP\_OPID\_CONTENTS\_MENU](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84aa9d64afb98b2fc91cae3810990451472)

@ BT\_AVRCP\_OPID\_CONTENTS\_MENU

**Definition** avrcp.h:53

[BT\_AVRCP\_OPID\_7](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84aac755d13a6f53ead21818a9fb90217ff)

@ BT\_AVRCP\_OPID\_7

**Definition** avrcp.h:64

[BT\_AVRCP\_OPID\_UP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84aae8fe4a27cf2b70bb289f38d4016b9d9)

@ BT\_AVRCP\_OPID\_UP

**Definition** avrcp.h:43

[BT\_AVRCP\_OPID\_HELP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ab3a7619c2c3cafe2eab868d471c8066b)

@ BT\_AVRCP\_OPID\_HELP

**Definition** avrcp.h:77

[BT\_AVRCP\_OPID\_SUBPICTURE](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ac1e3dd409b98c71eaf12567ce5028a98)

@ BT\_AVRCP\_OPID\_SUBPICTURE

**Definition** avrcp.h:96

[BT\_AVRCP\_OPID\_8](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ac751478296cc6a9e5de77fdf3c8fce06)

@ BT\_AVRCP\_OPID\_8

**Definition** avrcp.h:65

[BT\_AVRCP\_OPID\_2](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84acb3f6e1f71628853bb457bfb8163c566)

@ BT\_AVRCP\_OPID\_2

**Definition** avrcp.h:59

[BT\_AVRCP\_OPID\_SELECT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84acbaded78ac1e41d16464ea9db667c27f)

@ BT\_AVRCP\_OPID\_SELECT

**Definition** avrcp.h:42

[BT\_AVRCP\_OPID\_CHANNEL\_UP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ad39e69c55c571eb3c2492d5aa086e586)

@ BT\_AVRCP\_OPID\_CHANNEL\_UP

**Definition** avrcp.h:71

[BT\_AVRCP\_OPID\_VENDOR\_UNIQUE](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ad6eac39b4aced31534fde97a411b8c4d)

@ BT\_AVRCP\_OPID\_VENDOR\_UNIQUE

**Definition** avrcp.h:103

[BT\_AVRCP\_OPID\_EJECT](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ae34d68953054ef4446403a1e240e3344)

@ BT\_AVRCP\_OPID\_EJECT

**Definition** avrcp.h:91

[BT\_AVRCP\_OPID\_CLEAR](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ae6046a270ff9f8939059248cddc7a8a2)

@ BT\_AVRCP\_OPID\_CLEAR

**Definition** avrcp.h:69

[BT\_AVRCP\_OPID\_0](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ae6430b447ccd9e15d0ef2ae62152bade)

@ BT\_AVRCP\_OPID\_0

**Definition** avrcp.h:57

[BT\_AVRCP\_OPID\_PLAY](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84ae76461b7c08169ad190a83545b9e584b)

@ BT\_AVRCP\_OPID\_PLAY

**Definition** avrcp.h:85

[BT\_AVRCP\_OPID\_3](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84af1d1ea7e57a0a16c8e6ad8b9961d4459)

@ BT\_AVRCP\_OPID\_3

**Definition** avrcp.h:60

[BT\_AVRCP\_OPID\_VOLUME\_UP](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84af5f5b89b6f81961f7bf235c91f59b487)

@ BT\_AVRCP\_OPID\_VOLUME\_UP

**Definition** avrcp.h:82

[BT\_AVRCP\_OPID\_ANGLE](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84afc51d7bc6acd64c3dbeb1f10a06113c2)

@ BT\_AVRCP\_OPID\_ANGLE

**Definition** avrcp.h:95

[bt\_avrcp\_rsp\_t](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326)

bt\_avrcp\_rsp\_t

AV/C response codes.

**Definition** avrcp.h:29

[BT\_AVRCP\_RSP\_REJECTED](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a1775849a3c303b61975c569cc85e943c)

@ BT\_AVRCP\_RSP\_REJECTED

**Definition** avrcp.h:32

[BT\_AVRCP\_RSP\_ACCEPTED](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a2c93dc0bfd19305d8012b73001989cd8)

@ BT\_AVRCP\_RSP\_ACCEPTED

**Definition** avrcp.h:31

[BT\_AVRCP\_RSP\_STABLE](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a4136d697a8a0ea5daa1a6e89b314b992)

@ BT\_AVRCP\_RSP\_STABLE

For STATUS commands.

**Definition** avrcp.h:35

[BT\_AVRCP\_RSP\_INTERIM](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a4a2ed58a814be12b93753a6458b15e88)

@ BT\_AVRCP\_RSP\_INTERIM

**Definition** avrcp.h:37

[BT\_AVRCP\_RSP\_NOT\_IMPLEMENTED](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326a8a4cfe6ca8f5b92402c029d02b625696)

@ BT\_AVRCP\_RSP\_NOT\_IMPLEMENTED

**Definition** avrcp.h:30

[BT\_AVRCP\_RSP\_IMPLEMENTED](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326aa49f2871cf4e5f493128f574ad0d6144)

@ BT\_AVRCP\_RSP\_IMPLEMENTED

For SPECIFIC\_INQUIRY and GENERAL\_INQUIRY commands.

**Definition** avrcp.h:34

[BT\_AVRCP\_RSP\_IN\_TRANSITION](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326ab4b63e5cf84ea34895702ceea5ae81ad)

@ BT\_AVRCP\_RSP\_IN\_TRANSITION

**Definition** avrcp.h:33

[BT\_AVRCP\_RSP\_CHANGED](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326acf6f13da82b371efbcdf03fbedcb6988)

@ BT\_AVRCP\_RSP\_CHANGED

**Definition** avrcp.h:36

[bt\_avrcp\_get\_unit\_info](avrcp_8h.md#aba521a01fea4e7aee8b40ba72ca10bcf)

int bt\_avrcp\_get\_unit\_info(struct bt\_avrcp \*avrcp)

Get AVRCP Unit Info.

[bt\_avrcp\_connect](avrcp_8h.md#addc1f4f530b9e3eb4a669fe606479c59)

struct bt\_avrcp \* bt\_avrcp\_connect(struct bt\_conn \*conn)

Connect AVRCP.

[bt\_avrcp\_register\_cb](avrcp_8h.md#aedb1bc8dd553aa44fdaec2b9f5c76607)

int bt\_avrcp\_register\_cb(const struct bt\_avrcp\_cb \*cb)

Register callback.

[bt\_avrcp\_disconnect](avrcp_8h.md#af68c54ea0b17ebaa9872d271b0fee9bd)

int bt\_avrcp\_disconnect(struct bt\_avrcp \*avrcp)

Disconnect AVRCP.

[bt\_avrcp\_passthrough](avrcp_8h.md#afeea270bacac6a59af74c02fc1d98945)

int bt\_avrcp\_passthrough(struct bt\_avrcp \*avrcp, bt\_avrcp\_opid\_t operation\_id, bt\_avrcp\_button\_state\_t state, const uint8\_t \*payload, uint8\_t len)

Send AVRCP Pass Through command.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_avrcp\_cb](structbt__avrcp__cb.md)

**Definition** avrcp.h:135

[bt\_avrcp\_cb::passthrough\_rsp](structbt__avrcp__cb.md#a55be9880812b2e8fcc97480e1f0359dd)

void(\* passthrough\_rsp)(struct bt\_avrcp \*avrcp, struct bt\_avrcp\_passthrough\_rsp \*rsp)

Callback function for bt\_avrcp\_passthrough().

**Definition** avrcp.h:179

[bt\_avrcp\_cb::subunit\_info\_rsp](structbt__avrcp__cb.md#a75343c9da504a3dfa12e5f1959c9c58b)

void(\* subunit\_info\_rsp)(struct bt\_avrcp \*avrcp, struct bt\_avrcp\_subunit\_info\_rsp \*rsp)

Callback function for bt\_avrcp\_get\_subunit\_info().

**Definition** avrcp.h:170

[bt\_avrcp\_cb::connected](structbt__avrcp__cb.md#ac9b46b911f061a588cf87dd381364d0f)

void(\* connected)(struct bt\_avrcp \*avrcp)

An AVRCP connection has been established.

**Definition** avrcp.h:143

[bt\_avrcp\_cb::disconnected](structbt__avrcp__cb.md#acea85b2e1da11e0fd5835ce18c67ded1)

void(\* disconnected)(struct bt\_avrcp \*avrcp)

An AVRCP connection has been disconnected.

**Definition** avrcp.h:152

[bt\_avrcp\_cb::unit\_info\_rsp](structbt__avrcp__cb.md#ad2ea0d60add3fde24c291159cf365596)

void(\* unit\_info\_rsp)(struct bt\_avrcp \*avrcp, struct bt\_avrcp\_unit\_info\_rsp \*rsp)

Callback function for bt\_avrcp\_get\_unit\_info().

**Definition** avrcp.h:161

[bt\_avrcp\_passthrough\_rsp](structbt__avrcp__passthrough__rsp.md)

**Definition** avrcp.h:127

[bt\_avrcp\_passthrough\_rsp::response](structbt__avrcp__passthrough__rsp.md#a90c8c59bf3f333fa06d2b49d6e58af19)

uint8\_t response

bt\_avrcp\_rsp\_t

**Definition** avrcp.h:128

[bt\_avrcp\_passthrough\_rsp::operation\_id](structbt__avrcp__passthrough__rsp.md#a940eb51fabd1987016f6888d1b38c18e)

uint8\_t operation\_id

bt\_avrcp\_opid\_t

**Definition** avrcp.h:129

[bt\_avrcp\_passthrough\_rsp::payload](structbt__avrcp__passthrough__rsp.md#a9bd874797764bafb73a5663ccbb30bf8)

const uint8\_t \* payload

**Definition** avrcp.h:132

[bt\_avrcp\_passthrough\_rsp::state](structbt__avrcp__passthrough__rsp.md#aaa4ab701c9dee8d2ce8b4676f3ae140b)

uint8\_t state

bt\_avrcp\_button\_state\_t

**Definition** avrcp.h:130

[bt\_avrcp\_passthrough\_rsp::len](structbt__avrcp__passthrough__rsp.md#ad657103f9c751ba1e5fb1d447aff1718)

uint8\_t len

**Definition** avrcp.h:131

[bt\_avrcp\_subunit\_info\_rsp](structbt__avrcp__subunit__info__rsp.md)

**Definition** avrcp.h:120

[bt\_avrcp\_subunit\_info\_rsp::extended\_subunit\_id](structbt__avrcp__subunit__info__rsp.md#a0be33096e6edf251c23a5322b3c30421)

const uint8\_t \* extended\_subunit\_id

contains max\_subunit\_id items

**Definition** avrcp.h:124

[bt\_avrcp\_subunit\_info\_rsp::extended\_subunit\_type](structbt__avrcp__subunit__info__rsp.md#a47b69412c61682ed336737f34ac614dc)

const uint8\_t \* extended\_subunit\_type

contains max\_subunit\_id items

**Definition** avrcp.h:123

[bt\_avrcp\_subunit\_info\_rsp::subunit\_type](structbt__avrcp__subunit__info__rsp.md#a70bffb3209acd47beb37aeeb1700bfad)

uint8\_t subunit\_type

**Definition** avrcp.h:121

[bt\_avrcp\_subunit\_info\_rsp::max\_subunit\_id](structbt__avrcp__subunit__info__rsp.md#a85cf595920ba2dbf9f0e4deca1d27483)

uint8\_t max\_subunit\_id

**Definition** avrcp.h:122

[bt\_avrcp\_unit\_info\_rsp](structbt__avrcp__unit__info__rsp.md)

**Definition** avrcp.h:115

[bt\_avrcp\_unit\_info\_rsp::company\_id](structbt__avrcp__unit__info__rsp.md#a0225755bf457bc6d4046d8172af49217)

uint32\_t company\_id

**Definition** avrcp.h:117

[bt\_avrcp\_unit\_info\_rsp::unit\_type](structbt__avrcp__unit__info__rsp.md#af799f80a07f3e4f523b55d12820c93c0)

uint8\_t unit\_type

**Definition** avrcp.h:116

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [avrcp.h](avrcp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
