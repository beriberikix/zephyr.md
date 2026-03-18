---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pinctrl-r8a779f0_8h_source.html
original_path: doxygen/html/pinctrl-r8a779f0_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-r8a779f0.h

[Go to the documentation of this file.](pinctrl-r8a779f0_8h.md)

1/\*

2 \* Copyright (c) 2023 IoT.bzh

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_R8A779F0\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_R8A779F0\_H\_

8

9#include "[pinctrl-rcar-common.h](pinctrl-rcar-common_8h.md)"

10

11/\* Pins declaration \*/

[ 12](pinctrl-r8a779f0_8h.md#a61ae8c246db04e2ac956ccf175b217c6)#define PIN\_NONE -1

[ 13](pinctrl-r8a779f0_8h.md#a23ebfbcf2484691ef7dbf490054aa8ec)#define PIN\_SCIF\_CLK RCAR\_GP\_PIN(0, 0)

[ 14](pinctrl-r8a779f0_8h.md#aae52ed4df2cbea0bad32c9386fe043b2)#define PIN\_HSCK0 RCAR\_GP\_PIN(0, 1)

[ 15](pinctrl-r8a779f0_8h.md#a7155ba5d8ae93665a43b2ebe82d5603b)#define PIN\_HRX0 RCAR\_GP\_PIN(0, 2)

[ 16](pinctrl-r8a779f0_8h.md#ae18a748003b0c3b29355e9ad5f2dc9c9)#define PIN\_HTX0 RCAR\_GP\_PIN(0, 3)

[ 17](pinctrl-r8a779f0_8h.md#a5223b6d093d2beab4fe1564bac2a5827)#define PIN\_HCTS0\_N RCAR\_GP\_PIN(0, 4)

[ 18](pinctrl-r8a779f0_8h.md#a88c83e232ecaea7f0254d8c7ba2c4306)#define PIN\_HRTS0\_N RCAR\_GP\_PIN(0, 5)

[ 19](pinctrl-r8a779f0_8h.md#a6844ffe71c9cb20c6b4fe67289b58f40)#define PIN\_RX0 RCAR\_GP\_PIN(0, 6)

[ 20](pinctrl-r8a779f0_8h.md#a6c8efa60d2db765b46d88aa2a6df0318)#define PIN\_TX0 RCAR\_GP\_PIN(0, 7)

[ 21](pinctrl-r8a779f0_8h.md#a8a51b481e5ddab9dd843411171383b0c)#define PIN\_SCK0 RCAR\_GP\_PIN(0, 8)

[ 22](pinctrl-r8a779f0_8h.md#ae92b98335228c8cb723ce68ff6a8d60c)#define PIN\_RTS0\_N RCAR\_GP\_PIN(0, 9)

[ 23](pinctrl-r8a779f0_8h.md#a99f5a72c774fb5ad660300419ad75e95)#define PIN\_CTS0\_N RCAR\_GP\_PIN(0, 10)

[ 24](pinctrl-r8a779f0_8h.md#a53dcd276122e302a448058c662d4db4d)#define PIN\_MSIOF0\_SYNC RCAR\_GP\_PIN(0, 11)

[ 25](pinctrl-r8a779f0_8h.md#a924265fb5625164c8798e5e9e22a44c4)#define PIN\_MSIOF0\_RXD RCAR\_GP\_PIN(0, 12)

[ 26](pinctrl-r8a779f0_8h.md#a4d27c592b780f5f4d5c87e1e4f2c0d4b)#define PIN\_MSIOF0\_TXD RCAR\_GP\_PIN(0, 13)

[ 27](pinctrl-r8a779f0_8h.md#a69ed37349d43d4214adce06f067265d6)#define PIN\_MSIOF0\_SCK RCAR\_GP\_PIN(0, 14)

[ 28](pinctrl-r8a779f0_8h.md#a2b31a8f747dd87216ecea5cbc94d1896)#define PIN\_MSIOF0\_SS1 RCAR\_GP\_PIN(0, 15)

[ 29](pinctrl-r8a779f0_8h.md#a98b300e3af1451c327da1f89c5deb38e)#define PIN\_MSIOF0\_SS2 RCAR\_GP\_PIN(0, 16)

[ 30](pinctrl-r8a779f0_8h.md#a99ed780c4dd8d2e01c5ff66064306abf)#define PIN\_IRQ0 RCAR\_GP\_PIN(0, 17)

[ 31](pinctrl-r8a779f0_8h.md#a14204df3192ece77fc1b651c6625bc30)#define PIN\_IRQ1 RCAR\_GP\_PIN(0, 18)

[ 32](pinctrl-r8a779f0_8h.md#a6506051b7159eb6245d67a289ed548d1)#define PIN\_IRQ2 RCAR\_GP\_PIN(0, 19)

[ 33](pinctrl-r8a779f0_8h.md#a6e11e3ba86f107ad6f95cfd2cc922cf5)#define PIN\_IRQ3 RCAR\_GP\_PIN(0, 20)

[ 34](pinctrl-r8a779f0_8h.md#aef3aea97cd4567f898323bb63582ba10)#define PIN\_GP1\_00 RCAR\_GP\_PIN(1, 0)

[ 35](pinctrl-r8a779f0_8h.md#af10c42789a677c29fc453ae56bfd4671)#define PIN\_GP1\_01 RCAR\_GP\_PIN(1, 1)

[ 36](pinctrl-r8a779f0_8h.md#a02254ccde6e5a7ea59f3b2852d0f203e)#define PIN\_GP1\_02 RCAR\_GP\_PIN(1, 2)

[ 37](pinctrl-r8a779f0_8h.md#a5f5775e63f7c048df48a353924ae90a8)#define PIN\_GP1\_03 RCAR\_GP\_PIN(1, 3)

[ 38](pinctrl-r8a779f0_8h.md#a64ad1a03ccbd4938b4749b16fad69c22)#define PIN\_GP1\_04 RCAR\_GP\_PIN(1, 4)

[ 39](pinctrl-r8a779f0_8h.md#ade6719226599bd4f88e5421cd5ec2c18)#define PIN\_GP1\_05 RCAR\_GP\_PIN(1, 5)

[ 40](pinctrl-r8a779f0_8h.md#ab17359256d82f1f521b88ebcf2bc9dcd)#define PIN\_GP1\_06 RCAR\_GP\_PIN(1, 6)

[ 41](pinctrl-r8a779f0_8h.md#aff3ca182bfd773c441ca12b41c44502e)#define PIN\_GP1\_07 RCAR\_GP\_PIN(1, 7)

[ 42](pinctrl-r8a779f0_8h.md#a04d77969b7adc78323a42aaa7ea28800)#define PIN\_GP1\_08 RCAR\_GP\_PIN(1, 8)

[ 43](pinctrl-r8a779f0_8h.md#adbae97390397faa2c7ee503ffd462e6e)#define PIN\_GP1\_09 RCAR\_GP\_PIN(1, 9)

[ 44](pinctrl-r8a779f0_8h.md#a303118df2a9eb67e40b33637ae83749d)#define PIN\_GP1\_10 RCAR\_GP\_PIN(1, 10)

[ 45](pinctrl-r8a779f0_8h.md#a22b5c8e3aeda4db6f4977903af0c5b52)#define PIN\_GP1\_11 RCAR\_GP\_PIN(1, 11)

[ 46](pinctrl-r8a779f0_8h.md#a70d9b084dec16ff70b10a88b69814116)#define PIN\_MMC\_SD\_CLK RCAR\_GP\_PIN(1, 12)

[ 47](pinctrl-r8a779f0_8h.md#a51c2fa6fece32a48e0c4856d83d4fd1a)#define PIN\_MMC\_SD\_D0 RCAR\_GP\_PIN(1, 13)

[ 48](pinctrl-r8a779f0_8h.md#a99546403af550fc685e9471250082ef6)#define PIN\_MMC\_SD\_D1 RCAR\_GP\_PIN(1, 14)

[ 49](pinctrl-r8a779f0_8h.md#ad6a80e8ca8a623020305420a5d39c75c)#define PIN\_MMC\_SD\_D2 RCAR\_GP\_PIN(1, 15)

[ 50](pinctrl-r8a779f0_8h.md#ae287174d9ca20485540ac9af17b09ec2)#define PIN\_MMC\_SD\_D3 RCAR\_GP\_PIN(1, 16)

[ 51](pinctrl-r8a779f0_8h.md#a37f34e36bcc9b680b66638fd4103ecec)#define PIN\_MMC\_D5 RCAR\_GP\_PIN(1, 17)

[ 52](pinctrl-r8a779f0_8h.md#afdca9066dde9dfe542d6b5ffd1dc722e)#define PIN\_MMC\_D4 RCAR\_GP\_PIN(1, 18)

[ 53](pinctrl-r8a779f0_8h.md#a2954eb5a0da49a240d37712ce91f2618)#define PIN\_MMC\_D6 RCAR\_GP\_PIN(1, 19)

[ 54](pinctrl-r8a779f0_8h.md#a2c61c04d069d444e378107788de98da1)#define PIN\_MMC\_DS RCAR\_GP\_PIN(1, 20)

[ 55](pinctrl-r8a779f0_8h.md#a1999f6e72137cfdcd9c7df81158f211b)#define PIN\_MMC\_D7 RCAR\_GP\_PIN(1, 21)

[ 56](pinctrl-r8a779f0_8h.md#a15c3de73c180e7a2eadf928618b28612)#define PIN\_MMC\_SD\_CMD RCAR\_GP\_PIN(1, 22)

[ 57](pinctrl-r8a779f0_8h.md#a4ab5facdc05366f7b9dfb19469d53f47)#define PIN\_SD\_CD RCAR\_GP\_PIN(1, 23)

[ 58](pinctrl-r8a779f0_8h.md#ac161966d07d3031aa245417dbd3afb04)#define PIN\_SD\_WP RCAR\_GP\_PIN(1, 24)

[ 59](pinctrl-r8a779f0_8h.md#ae445f51a0031da7deb1a5e279c7f55f6)#define PIN\_RPC\_INT\_N RCAR\_GP\_PIN(2, 0)

[ 60](pinctrl-r8a779f0_8h.md#a3f139531d8d50cfc031b2163fe16e885)#define PIN\_RPC\_WP\_N RCAR\_GP\_PIN(2, 1)

[ 61](pinctrl-r8a779f0_8h.md#a0f73d041e18bfeedd28f98ba895272ed)#define PIN\_RPC\_RESET\_N RCAR\_GP\_PIN(2, 2)

[ 62](pinctrl-r8a779f0_8h.md#a2d81e5fdef8cb97a4cf2d18c68325746)#define PIN\_QSPI1\_SSL RCAR\_GP\_PIN(2, 3)

[ 63](pinctrl-r8a779f0_8h.md#a9c9ae11c6c6c6ac9c9c1b19a94d1b6fd)#define PIN\_QSPI1\_IO3 RCAR\_GP\_PIN(2, 4)

[ 64](pinctrl-r8a779f0_8h.md#ab5e70699dc556ff6d30df1618924a928)#define PIN\_QSPI1\_MISO\_IO1 RCAR\_GP\_PIN(2, 5)

[ 65](pinctrl-r8a779f0_8h.md#ad28db9650b74336e2b7d2a724894a706)#define PIN\_QSPI1\_IO2 RCAR\_GP\_PIN(2, 6)

[ 66](pinctrl-r8a779f0_8h.md#aaa596198d60346c91822c8b52fbf44c7)#define PIN\_QSPI1\_MOSI\_IO0 RCAR\_GP\_PIN(2, 7)

[ 67](pinctrl-r8a779f0_8h.md#aa6b8aad6a047b3173abb358c345e557c)#define PIN\_QSPI1\_SPCLK RCAR\_GP\_PIN(2, 8)

[ 68](pinctrl-r8a779f0_8h.md#a49c45fe433bb57486cb1ded9c3fbf275)#define PIN\_QSPI0\_MOSI\_IO0 RCAR\_GP\_PIN(2, 9)

[ 69](pinctrl-r8a779f0_8h.md#a68c69e86d4457a5d637d64ef75bdfd85)#define PIN\_QSPI0\_SPCLK RCAR\_GP\_PIN(2, 10)

[ 70](pinctrl-r8a779f0_8h.md#ae8e8f603407a3db8830e7c0f6156c647)#define PIN\_QSPI0\_IO2 RCAR\_GP\_PIN(2, 11)

[ 71](pinctrl-r8a779f0_8h.md#a8a4db281c1d7eeb4a8b683e579b0ab4e)#define PIN\_QSPI0\_MISO\_IO1 RCAR\_GP\_PIN(2, 12)

[ 72](pinctrl-r8a779f0_8h.md#a147f808337f1bbe0917f1a8ce1ca419d)#define PIN\_QSPI0\_SSL RCAR\_GP\_PIN(2, 13)

[ 73](pinctrl-r8a779f0_8h.md#ab0ef23683d3b80c9710a82340d779566)#define PIN\_QSPI0\_IO3 RCAR\_GP\_PIN(2, 14)

[ 74](pinctrl-r8a779f0_8h.md#a91b1e2540969867edaac239b272cc1e3)#define PIN\_PCIE0\_CLKREQ\_N RCAR\_GP\_PIN(2, 15)

[ 75](pinctrl-r8a779f0_8h.md#a093cf7f6e3675c5ada8bed78332b1d2b)#define PIN\_PCIE1\_CLKREQ\_N RCAR\_GP\_PIN(2, 16)

[ 76](pinctrl-r8a779f0_8h.md#a9cd9a3de2335cab61740da050b9c75b2)#define PIN\_TSN1\_MDIO RCAR\_GP\_PIN(3, 0)

[ 77](pinctrl-r8a779f0_8h.md#a41a8dd5df86ec02baa4890ef66034181)#define PIN\_TSN2\_MDIO RCAR\_GP\_PIN(3, 1)

[ 78](pinctrl-r8a779f0_8h.md#a309bcc830559562e70a137f9ea49d6f1)#define PIN\_TSN0\_MDIO RCAR\_GP\_PIN(3, 2)

[ 79](pinctrl-r8a779f0_8h.md#a44f0c929ff1e47f45b846e2f3c51ca2a)#define PIN\_TSN2\_MDC RCAR\_GP\_PIN(3, 3)

[ 80](pinctrl-r8a779f0_8h.md#a7d93e22d33550e4c1291063149ba9f84)#define PIN\_TSN0\_MDC RCAR\_GP\_PIN(3, 4)

[ 81](pinctrl-r8a779f0_8h.md#abd8786363f7374be297d0d5908218c01)#define PIN\_TSN1\_MDC RCAR\_GP\_PIN(3, 5)

[ 82](pinctrl-r8a779f0_8h.md#a9ca153b4ea9e91aaefb235678d4c4c5a)#define PIN\_TSN1\_LINK RCAR\_GP\_PIN(3, 6)

[ 83](pinctrl-r8a779f0_8h.md#ad3f9ac104997820d652388d61ff91e3a)#define PIN\_TSN2\_LINK RCAR\_GP\_PIN(3, 7)

[ 84](pinctrl-r8a779f0_8h.md#a7e0fd90d2fa0a1c517794dae135ac02d)#define PIN\_TSN0\_LINK RCAR\_GP\_PIN(3, 8)

[ 85](pinctrl-r8a779f0_8h.md#a5fc60c4ded24b47e326a6448a1ed0f98)#define PIN\_TSN2\_PHY\_INT RCAR\_GP\_PIN(3, 9)

[ 86](pinctrl-r8a779f0_8h.md#a73c9a2054a075e90f5169df89f3b98ba)#define PIN\_TSN0\_PHY\_INT RCAR\_GP\_PIN(3, 10)

[ 87](pinctrl-r8a779f0_8h.md#a7b4a42ef7bbb623dc5a5e8d8679c3593)#define PIN\_TSN1\_PHY\_INT RCAR\_GP\_PIN(3, 11)

[ 88](pinctrl-r8a779f0_8h.md#a47f937cdc3cd2163672d89a7411ff697)#define PIN\_TSN0\_MAGIC RCAR\_GP\_PIN(3, 12)

[ 89](pinctrl-r8a779f0_8h.md#a92663df3b83592651ae841e044e23aa7)#define PIN\_TSN1\_AVTP\_PPS RCAR\_GP\_PIN(3, 13)

[ 90](pinctrl-r8a779f0_8h.md#a7ee14955cb20b34b89a4d4697de7219c)#define PIN\_TSN1\_AVTP\_MATCH RCAR\_GP\_PIN(3, 14)

[ 91](pinctrl-r8a779f0_8h.md#a82618988bb6087b94c0dca8082522398)#define PIN\_TSN1\_AVTP\_CAPTURE RCAR\_GP\_PIN(3, 15)

[ 92](pinctrl-r8a779f0_8h.md#a695d279faed8c3b4c9f1df3d98043663)#define PIN\_TSN0\_AVTP\_PPS RCAR\_GP\_PIN(3, 16)

[ 93](pinctrl-r8a779f0_8h.md#a9bf96054da1630760a8e2145df813243)#define PIN\_TSN0\_AVTP\_MATCH RCAR\_GP\_PIN(3, 17)

[ 94](pinctrl-r8a779f0_8h.md#ac4d590fb546d2b58b7e4480e34d697b4)#define PIN\_TSN0\_AVTP\_CAPTURE RCAR\_GP\_PIN(3, 18)

[ 95](pinctrl-r8a779f0_8h.md#ab8ddb9dc2aa3d7b43013786e3de1479f)#define PIN\_GP4\_00 RCAR\_GP\_PIN(4, 0)

[ 96](pinctrl-r8a779f0_8h.md#a4a0e3acb220d978fc7694ee11880917d)#define PIN\_GP4\_01 RCAR\_GP\_PIN(4, 1)

[ 97](pinctrl-r8a779f0_8h.md#a76fd574a9105c5485ff9b063bd76ce69)#define PIN\_GP4\_02 RCAR\_GP\_PIN(4, 2)

[ 98](pinctrl-r8a779f0_8h.md#a3bb82ef9e59ca76447e1f389ab5ba1bc)#define PIN\_GP4\_03 RCAR\_GP\_PIN(4, 3)

[ 99](pinctrl-r8a779f0_8h.md#a05228794dd9d29d8d64da4c19ba96bc7)#define PIN\_GP4\_04 RCAR\_GP\_PIN(4, 4)

[ 100](pinctrl-r8a779f0_8h.md#af859918eddae5c94cd944685eb7b3099)#define PIN\_GP4\_05 RCAR\_GP\_PIN(4, 5)

[ 101](pinctrl-r8a779f0_8h.md#a5df323909449f6c4eecbdeda0af9a8e3)#define PIN\_GP4\_06 RCAR\_GP\_PIN(4, 6)

[ 102](pinctrl-r8a779f0_8h.md#ab281b2eede748b8e713518560bde5631)#define PIN\_GP4\_07 RCAR\_GP\_PIN(4, 7)

[ 103](pinctrl-r8a779f0_8h.md#ab4c8cae28535c02511e4be0ce5df4984)#define PIN\_GP4\_08 RCAR\_GP\_PIN(4, 8)

[ 104](pinctrl-r8a779f0_8h.md#a8e372290bb2c9c7c5e6df11b4429ab99)#define PIN\_GP4\_09 RCAR\_GP\_PIN(4, 9)

[ 105](pinctrl-r8a779f0_8h.md#ac82815b12697d457044c5766ae0fc439)#define PIN\_GP4\_10 RCAR\_GP\_PIN(4, 10)

[ 106](pinctrl-r8a779f0_8h.md#aa7ba730191e0636fedc9e1fb73d6a054)#define PIN\_GP4\_11 RCAR\_GP\_PIN(4, 11)

[ 107](pinctrl-r8a779f0_8h.md#ae940b5cde1f81df10d10f4ee54fb7ba7)#define PIN\_GP4\_12 RCAR\_GP\_PIN(4, 12)

[ 108](pinctrl-r8a779f0_8h.md#a61dc718f72bddd87ac3279f3a412de34)#define PIN\_GP4\_13 RCAR\_GP\_PIN(4, 13)

[ 109](pinctrl-r8a779f0_8h.md#ac8628d5166b90c4a494f317cae205096)#define PIN\_GP4\_14 RCAR\_GP\_PIN(4, 14)

[ 110](pinctrl-r8a779f0_8h.md#a3b83a26d74fc7cf315ba241979624f01)#define PIN\_GP4\_15 RCAR\_GP\_PIN(4, 15)

[ 111](pinctrl-r8a779f0_8h.md#aced4ff077e6ae68b786f28183a9c2177)#define PIN\_GP4\_16 RCAR\_GP\_PIN(4, 16)

[ 112](pinctrl-r8a779f0_8h.md#aab0a54b9ee8b237992457955d02234eb)#define PIN\_GP4\_17 RCAR\_GP\_PIN(4, 17)

[ 113](pinctrl-r8a779f0_8h.md#a96878fbe537a7b6b313cc8687f508453)#define PIN\_GP4\_18 RCAR\_GP\_PIN(4, 18)

[ 114](pinctrl-r8a779f0_8h.md#aa050c60b2dc866616813018184a4305e)#define PIN\_GP4\_19 RCAR\_GP\_PIN(4, 19)

[ 115](pinctrl-r8a779f0_8h.md#ae0214f468f1c5ef67a062aab83666803)#define PIN\_MSPI0SC RCAR\_GP\_PIN(4, 20)

[ 116](pinctrl-r8a779f0_8h.md#a12c32bcb6b903f7d6c63b30be2158798)#define PIN\_MSPI0SI RCAR\_GP\_PIN(4, 21)

[ 117](pinctrl-r8a779f0_8h.md#a40fe04c477c36a94a4f217c28db8b50c)#define PIN\_MSPI0SO\_MSPI0DCS RCAR\_GP\_PIN(4, 22)

[ 118](pinctrl-r8a779f0_8h.md#a50a6161e901b0bdc3dbf68ef9f063f69)#define PIN\_MSPI0CSS1 RCAR\_GP\_PIN(4, 23)

[ 119](pinctrl-r8a779f0_8h.md#a83a95e8ea8f635c810aa4669745362cf)#define PIN\_MSPI0CSS0 RCAR\_GP\_PIN(4, 24)

[ 120](pinctrl-r8a779f0_8h.md#a5f0b80943626e9e3bd1367fd75e6fc31)#define PIN\_MSPI1SI RCAR\_GP\_PIN(4, 25)

[ 121](pinctrl-r8a779f0_8h.md#ad7bbe5904208ddf0717ddc86fd37d40a)#define PIN\_MSPI1SO\_MSPI1DCS RCAR\_GP\_PIN(4, 26)

[ 122](pinctrl-r8a779f0_8h.md#a6b89666a0edb22460f525b1826ad77ea)#define PIN\_MSPI1CSS0 RCAR\_GP\_PIN(4, 27)

[ 123](pinctrl-r8a779f0_8h.md#aa9377e2bd34f816f049fcf639f570769)#define PIN\_MSPI1SC RCAR\_GP\_PIN(4, 28)

[ 124](pinctrl-r8a779f0_8h.md#aa6ec14b6c6e1a67da177f3c20f4f66ff)#define PIN\_MSPI1CSS2 RCAR\_GP\_PIN(4, 29)

[ 125](pinctrl-r8a779f0_8h.md#a19ef91765370c495d27233042fdd2230)#define PIN\_MSPI1CSS1 RCAR\_GP\_PIN(4, 30)

[ 126](pinctrl-r8a779f0_8h.md#a261ee8ab72c101b7fa356d214bdab307)#define PIN\_RIIC0SCL RCAR\_GP\_PIN(5, 0)

[ 127](pinctrl-r8a779f0_8h.md#a24f187b75251c617abb1f6d1a3eba982)#define PIN\_RIIC0SDA RCAR\_GP\_PIN(5, 1)

[ 128](pinctrl-r8a779f0_8h.md#aad9a0a288dc7f275a02a28782dccdcc1)#define PIN\_ETNB0MD RCAR\_GP\_PIN(5, 2)

[ 129](pinctrl-r8a779f0_8h.md#a486d879b55cc4499bc1f72c786c839d9)#define PIN\_ETNB0WOL RCAR\_GP\_PIN(5, 3)

[ 130](pinctrl-r8a779f0_8h.md#af75562234e373c5be6289dfa93f5e27e)#define PIN\_ETNB0LINKSTA RCAR\_GP\_PIN(5, 4)

[ 131](pinctrl-r8a779f0_8h.md#a136da0f8673acb48487a78a409a7ec04)#define PIN\_ETNB0MDC RCAR\_GP\_PIN(5, 5)

[ 132](pinctrl-r8a779f0_8h.md#a00c42facd77202ae4fa9d7882a0e9b79)#define PIN\_ETNB0RXER RCAR\_GP\_PIN(5, 6)

[ 133](pinctrl-r8a779f0_8h.md#a2244e4030264cc9ffaa709c952e725e2)#define PIN\_ETNB0RXD3 RCAR\_GP\_PIN(5, 7)

[ 134](pinctrl-r8a779f0_8h.md#abc340191710f72c425f80499aa15733f)#define PIN\_ETNB0RXD1 RCAR\_GP\_PIN(5, 8)

[ 135](pinctrl-r8a779f0_8h.md#aca3eb58f478b788aeb906abb9e4c3177)#define PIN\_ETNB0RXD2 RCAR\_GP\_PIN(5, 9)

[ 136](pinctrl-r8a779f0_8h.md#af47f55ebd01535e4bf231e90e75b10fc)#define PIN\_ETNB0RXDV RCAR\_GP\_PIN(5, 10)

[ 137](pinctrl-r8a779f0_8h.md#ae7f60672a60d5dd2b16d4b421bb77ad0)#define PIN\_ETNB0RXD0 RCAR\_GP\_PIN(5, 11)

[ 138](pinctrl-r8a779f0_8h.md#a4590cf683d70fd8235de8e48d3b6e929)#define PIN\_ETNB0RXCLK RCAR\_GP\_PIN(5, 12)

[ 139](pinctrl-r8a779f0_8h.md#af351e56467acb802d7bdc7fdec74700f)#define PIN\_ETNB0TXER RCAR\_GP\_PIN(5, 13)

[ 140](pinctrl-r8a779f0_8h.md#a775646011d9eab3af41b770999b64ed8)#define PIN\_ETNB0TXD3 RCAR\_GP\_PIN(5, 14)

[ 141](pinctrl-r8a779f0_8h.md#a250c34c547c08f1a1dde9a9292744906)#define PIN\_ETNB0TXCLK RCAR\_GP\_PIN(5, 15)

[ 142](pinctrl-r8a779f0_8h.md#ae0b7042bb8ebb8a50d125b670ecde884)#define PIN\_ETNB0TXD1 RCAR\_GP\_PIN(5, 16)

[ 143](pinctrl-r8a779f0_8h.md#a83f7e3dccf2d720c6c7ecec99fcf9403)#define PIN\_ETNB0TXD2 RCAR\_GP\_PIN(5, 17)

[ 144](pinctrl-r8a779f0_8h.md#a0601b25a54c0982b8d83d8301911cec7)#define PIN\_ETNB0TXEN RCAR\_GP\_PIN(5, 18)

[ 145](pinctrl-r8a779f0_8h.md#acdd4d82bcb4a7c7eb1fd6a6907869684)#define PIN\_ETNB0TXD0 RCAR\_GP\_PIN(5, 19)

[ 146](pinctrl-r8a779f0_8h.md#a4d1611216c59276d57d46855a7677234)#define PIN\_RLIN37TX RCAR\_GP\_PIN(6, 0)

[ 147](pinctrl-r8a779f0_8h.md#a5d7537af02438eb11e89aca986fb1991)#define PIN\_RLIN37RX\_INTP23 RCAR\_GP\_PIN(6, 1)

[ 148](pinctrl-r8a779f0_8h.md#ada114796cad15bdeb5c9ebc79424362c)#define PIN\_RLIN36TX RCAR\_GP\_PIN(6, 2)

[ 149](pinctrl-r8a779f0_8h.md#a141483a8392aa709205b960bc2f8ec0a)#define PIN\_RLIN36RX\_INTP22 RCAR\_GP\_PIN(6, 3)

[ 150](pinctrl-r8a779f0_8h.md#add8f7b7cc9798f41db084f6ae19ae63d)#define PIN\_RLIN35TX RCAR\_GP\_PIN(6, 4)

[ 151](pinctrl-r8a779f0_8h.md#a00004edc21517cc6b27bfec417287992)#define PIN\_RLIN35RX\_INTP21 RCAR\_GP\_PIN(6, 5)

[ 152](pinctrl-r8a779f0_8h.md#a799ebf91721e1d8a314941c46b57f7fb)#define PIN\_RLIN34TX RCAR\_GP\_PIN(6, 6)

[ 153](pinctrl-r8a779f0_8h.md#aefc7c5b31f6f99cefcb4ff3fbbf2662d)#define PIN\_RLIN34RX\_INTP20 RCAR\_GP\_PIN(6, 7)

[ 154](pinctrl-r8a779f0_8h.md#a00527c2d97e350eff25043b62212a263)#define PIN\_RLIN33TX RCAR\_GP\_PIN(6, 8)

[ 155](pinctrl-r8a779f0_8h.md#ab732b816c978ba3acaf2db8d4885bf96)#define PIN\_RLIN33RX\_INTP19 RCAR\_GP\_PIN(6, 9)

[ 156](pinctrl-r8a779f0_8h.md#a95831f66e94ce58d86257b3ced51c83e)#define PIN\_RLIN32TX RCAR\_GP\_PIN(6, 10)

[ 157](pinctrl-r8a779f0_8h.md#a6f0575f9f2f7870997f38143a4626b7e)#define PIN\_RLIN32RX\_INTP18 RCAR\_GP\_PIN(6, 11)

[ 158](pinctrl-r8a779f0_8h.md#a7dd886871ec3e2dcba4d01aadbdef7fc)#define PIN\_RLIN31TX RCAR\_GP\_PIN(6, 12)

[ 159](pinctrl-r8a779f0_8h.md#af804ff3a43707a1de48b31e6989dffb0)#define PIN\_RLIN31RX\_INTP17 RCAR\_GP\_PIN(6, 13)

[ 160](pinctrl-r8a779f0_8h.md#a805c6614df5799a763739db8b4746031)#define PIN\_RLIN30TX RCAR\_GP\_PIN(6, 14)

[ 161](pinctrl-r8a779f0_8h.md#ae1fbd6e7b3cf06a46f7b4b176f974ee1)#define PIN\_RLIN30RX\_INTP16 RCAR\_GP\_PIN(6, 15)

[ 162](pinctrl-r8a779f0_8h.md#ab2f8a964d639817a66c2748e6cae0a10)#define PIN\_INTP37 RCAR\_GP\_PIN(6, 16)

[ 163](pinctrl-r8a779f0_8h.md#a0e13e1006198018c14aa5b490266f60b)#define PIN\_INTP36 RCAR\_GP\_PIN(6, 17)

[ 164](pinctrl-r8a779f0_8h.md#ab3b335357d4a2a94c59da764ff1424fa)#define PIN\_INTP35 RCAR\_GP\_PIN(6, 18)

[ 165](pinctrl-r8a779f0_8h.md#ae0467e3d6c71686e0a722d62036e6681)#define PIN\_INTP34 RCAR\_GP\_PIN(6, 19)

[ 166](pinctrl-r8a779f0_8h.md#aa1724eca8ceefe60bf1c63c1ef9c0810)#define PIN\_INTP33 RCAR\_GP\_PIN(6, 20)

[ 167](pinctrl-r8a779f0_8h.md#a614b093f0f31d58558c2409259b81ed9)#define PIN\_INTP32 RCAR\_GP\_PIN(6, 21)

[ 168](pinctrl-r8a779f0_8h.md#af477fefede1e5f889a8cdd66e548dcf5)#define PIN\_NMI1 RCAR\_GP\_PIN(6, 22)

[ 169](pinctrl-r8a779f0_8h.md#af8ea9389f46ffe8314fc0927e8884f44)#define PIN\_PRESETOUT1\_N RCAR\_GP\_PIN(6, 31)

[ 170](pinctrl-r8a779f0_8h.md#a91f4087c5e2ee3c96918db5fd6137480)#define PIN\_CAN0TX RCAR\_GP\_PIN(7, 0)

[ 171](pinctrl-r8a779f0_8h.md#a48e1aa0caa7c4e19e2fdb246568957be)#define PIN\_CAN0RX\_INTP0 RCAR\_GP\_PIN(7, 1)

[ 172](pinctrl-r8a779f0_8h.md#a8ad123e52422dae8187b7601d746663c)#define PIN\_CAN1TX RCAR\_GP\_PIN(7, 2)

[ 173](pinctrl-r8a779f0_8h.md#a65831a84f85fa7b7479590b39efad99d)#define PIN\_CAN1RX\_INTP1 RCAR\_GP\_PIN(7, 3)

[ 174](pinctrl-r8a779f0_8h.md#ab22ff84e00937f1aa7bbc1aa15a0eedd)#define PIN\_CAN2TX RCAR\_GP\_PIN(7, 4)

[ 175](pinctrl-r8a779f0_8h.md#a2e5dfa4d079c4059a15900c9999e9dcd)#define PIN\_CAN2RX\_INTP2 RCAR\_GP\_PIN(7, 5)

[ 176](pinctrl-r8a779f0_8h.md#a900d98b6550cf9dcca3b14af3f2d8582)#define PIN\_CAN3TX RCAR\_GP\_PIN(7, 6)

[ 177](pinctrl-r8a779f0_8h.md#a3246d7209bf9ec55056f69137efd109c)#define PIN\_CAN3RX\_INTP3 RCAR\_GP\_PIN(7, 7)

[ 178](pinctrl-r8a779f0_8h.md#aadc2d9e53a8a1fc699ec60544d879c79)#define PIN\_CAN4TX RCAR\_GP\_PIN(7, 8)

[ 179](pinctrl-r8a779f0_8h.md#a0a7a38cb814288c5cdb96716b01e1ebc)#define PIN\_CAN4RX\_INTP4 RCAR\_GP\_PIN(7, 9)

[ 180](pinctrl-r8a779f0_8h.md#a5ee45a18ca6a47a4aec9aba4b28b921e)#define PIN\_CAN5TX RCAR\_GP\_PIN(7, 10)

[ 181](pinctrl-r8a779f0_8h.md#aa33e90012374a282149691e40a27de91)#define PIN\_CAN5RX\_INTP5 RCAR\_GP\_PIN(7, 11)

[ 182](pinctrl-r8a779f0_8h.md#a5fc140d63d7e53097b3bce6fd7fa1db8)#define PIN\_CAN6TX RCAR\_GP\_PIN(7, 12)

[ 183](pinctrl-r8a779f0_8h.md#aedc5711bde47c6bcef3a418246dced0e)#define PIN\_CAN6RX\_INTP6 RCAR\_GP\_PIN(7, 13)

[ 184](pinctrl-r8a779f0_8h.md#ac823cccd79e4355bed8128425ea0bc64)#define PIN\_CAN7TX RCAR\_GP\_PIN(7, 14)

[ 185](pinctrl-r8a779f0_8h.md#a971f18b78b3a1affc998d7d63bbce147)#define PIN\_CAN7RX\_INTP7 RCAR\_GP\_PIN(7, 15)

[ 186](pinctrl-r8a779f0_8h.md#a50a51f4588ddadbab5b49dd5b24eed38)#define PIN\_CAN8TX RCAR\_GP\_PIN(7, 16)

[ 187](pinctrl-r8a779f0_8h.md#a089edb5b2bac4d19d2aef5224c9b69f7)#define PIN\_CAN8RX\_INTP8 RCAR\_GP\_PIN(7, 17)

[ 188](pinctrl-r8a779f0_8h.md#a531499f6ed16f16f040ad74328f12a68)#define PIN\_CAN9TX RCAR\_GP\_PIN(7, 18)

[ 189](pinctrl-r8a779f0_8h.md#a32881ffd56cfe0d6c2eed762e74a6ab0)#define PIN\_CAN9RX\_INTP9 RCAR\_GP\_PIN(7, 19)

[ 190](pinctrl-r8a779f0_8h.md#a5e7aa320607fe93bc55f42fd6cf4ba02)#define PIN\_CAN10TX RCAR\_GP\_PIN(7, 20)

[ 191](pinctrl-r8a779f0_8h.md#aeca646b3c76cd415f7a61cb499307c5e)#define PIN\_CAN10RX\_INTP10 RCAR\_GP\_PIN(7, 21)

[ 192](pinctrl-r8a779f0_8h.md#adfe3ac919296b2c95d2ef984b0b63a5b)#define PIN\_CAN11TX RCAR\_GP\_PIN(7, 22)

[ 193](pinctrl-r8a779f0_8h.md#a5b05cee3869fd6d48a78fe15b92f1b0c)#define PIN\_CAN11RX\_INTP11 RCAR\_GP\_PIN(7, 23)

[ 194](pinctrl-r8a779f0_8h.md#acd7e4d164a5aeee593840c916883f633)#define PIN\_CAN12TX RCAR\_GP\_PIN(7, 24)

[ 195](pinctrl-r8a779f0_8h.md#a1d67dbf5f5a1141e9862ec79fa1af6b2)#define PIN\_CAN12RX\_INTP12 RCAR\_GP\_PIN(7, 25)

[ 196](pinctrl-r8a779f0_8h.md#a8078aad78ec1e23bc35aba85c84220a0)#define PIN\_CAN13TX RCAR\_GP\_PIN(7, 26)

[ 197](pinctrl-r8a779f0_8h.md#ae6a000c991caaec9484b2997ebbed94f)#define PIN\_CAN13RX\_INTP13 RCAR\_GP\_PIN(7, 27)

[ 198](pinctrl-r8a779f0_8h.md#a878ead71f8bed5c9fc7ffac21ee8ab01)#define PIN\_CAN14TX RCAR\_GP\_PIN(7, 28)

[ 199](pinctrl-r8a779f0_8h.md#aaaa27ae8b36cada4428992b75b5b08e9)#define PIN\_CAN14RX\_INTP14 RCAR\_GP\_PIN(7, 29)

[ 200](pinctrl-r8a779f0_8h.md#a66ce52fe74d02340c47679774d633768)#define PIN\_CAN15TX RCAR\_GP\_PIN(7, 30)

[ 201](pinctrl-r8a779f0_8h.md#abdd8b34212236210c491fe3cfc601dcc)#define PIN\_CAN15RX\_INTP15 RCAR\_GP\_PIN(7, 31)

202

203/\* Pinmux function declarations \*/

[ 204](pinctrl-r8a779f0_8h.md#a4383103ef55d7738821f35c66f799480)#define FUNC\_SCIF\_CLK IP0SR0(0, 0)

[ 205](pinctrl-r8a779f0_8h.md#ac34dcbc3b29209202c8814557d95ea55)#define FUNC\_HSCK0 IP0SR0(4, 0)

[ 206](pinctrl-r8a779f0_8h.md#aef23d90678d28a442690cf64f7d9f658)#define FUNC\_SCK3 IP0SR0(4, 1)

[ 207](pinctrl-r8a779f0_8h.md#a1863b6d1c08147dd03b1618b7693a20e)#define FUNC\_MSIOF3\_SCK IP0SR0(4, 2)

[ 208](pinctrl-r8a779f0_8h.md#a620ae3eb90bf2eacd43a652e2c881ae2)#define FUNC\_TSN0\_AVTP\_CAPTURE\_A IP0SR0(4, 5)

[ 209](pinctrl-r8a779f0_8h.md#a0083d7f84d9cd9a43bce4ead53660e10)#define FUNC\_HRX0 IP0SR0(8, 0)

[ 210](pinctrl-r8a779f0_8h.md#a47721943b5c8b3831d7d8c26507ad36b)#define FUNC\_RX3 IP0SR0(8, 1)

[ 211](pinctrl-r8a779f0_8h.md#a74a54b4a144208f176b1c6b1a56ebc7b)#define FUNC\_MSIOF3\_RXD IP0SR0(8, 2)

[ 212](pinctrl-r8a779f0_8h.md#a2cab5440388f0d7e6c86a331b333854e)#define FUNC\_TSN0\_AVTP\_MATCH\_A IP0SR0(8, 5)

[ 213](pinctrl-r8a779f0_8h.md#a05b9319c6c2228449a956a3377ccff44)#define FUNC\_HTX0 IP0SR0(12, 0)

[ 214](pinctrl-r8a779f0_8h.md#af4773e6b771fac4eacac1f9b8b789e49)#define FUNC\_TX3 IP0SR0(12, 1)

[ 215](pinctrl-r8a779f0_8h.md#aaac26cfb6e1628b7a3df6be84aebf719)#define FUNC\_MSIOF3\_TXD IP0SR0(12, 2)

[ 216](pinctrl-r8a779f0_8h.md#a7739b47f4b7b6fbbfc6a86a70bdbcb4d)#define FUNC\_HCTS0\_N IP0SR0(16, 0)

[ 217](pinctrl-r8a779f0_8h.md#a0f2117dc4381a92aadb82e812196a770)#define FUNC\_CTS3\_N IP0SR0(16, 1)

[ 218](pinctrl-r8a779f0_8h.md#a8c11679f1198ffa3708f51a0588bb7f3)#define FUNC\_MSIOF3\_SS1 IP0SR0(16, 2)

[ 219](pinctrl-r8a779f0_8h.md#a465da76a93d1138818eefe830b27a756)#define FUNC\_TSN0\_MDC\_A IP0SR0(16, 5)

[ 220](pinctrl-r8a779f0_8h.md#a71382cd3a87fa52b3ccb8609fdbe6a06)#define FUNC\_HRTS0\_N IP0SR0(20, 0)

[ 221](pinctrl-r8a779f0_8h.md#a62ad79fc0395e1919d66d7aeeb4c5198)#define FUNC\_RTS3\_N IP0SR0(20, 1)

[ 222](pinctrl-r8a779f0_8h.md#a5e7c7012df0246fbd4a4f880b34f267e)#define FUNC\_MSIOF3\_SS2 IP0SR0(20, 2)

[ 223](pinctrl-r8a779f0_8h.md#a7d1b940745f92b4c2f70446ff094c0e2)#define FUNC\_TSN0\_MDIO\_A IP0SR0(20, 5)

[ 224](pinctrl-r8a779f0_8h.md#aa9a2dc363e864c2e72f727a1cf8cbbd4)#define FUNC\_RX0 IP0SR0(24, 0)

[ 225](pinctrl-r8a779f0_8h.md#a4cda0365d251f6c4ddaa2670849ed596)#define FUNC\_HRX1 IP0SR0(24, 1)

[ 226](pinctrl-r8a779f0_8h.md#afa4857e4c2cdc35b5486d2851442a6be)#define FUNC\_MSIOF1\_RXD IP0SR0(24, 3)

[ 227](pinctrl-r8a779f0_8h.md#af21598d2089ca01e4f149bbfc1d15075)#define FUNC\_TSN1\_AVTP\_MATCH\_A IP0SR0(24, 5)

[ 228](pinctrl-r8a779f0_8h.md#ad75b08ecf2acef89e349615d95652ebd)#define FUNC\_TX0 IP0SR0(28, 0)

[ 229](pinctrl-r8a779f0_8h.md#a84a48ac4b0e6f2f7fc76bc92e71dbbc7)#define FUNC\_HTX1 IP0SR0(28, 1)

[ 230](pinctrl-r8a779f0_8h.md#a12f2c15eb68cf2f94a192319e33d9f24)#define FUNC\_MSIOF1\_TXD IP0SR0(28, 3)

[ 231](pinctrl-r8a779f0_8h.md#a303fa885ee6eea891bdc2761b8235eff)#define FUNC\_TSN1\_AVTP\_CAPTURE\_A IP0SR0(28, 5)

[ 232](pinctrl-r8a779f0_8h.md#a2564af7b243f9cfdff885c89b55a03f1)#define FUNC\_SCK0 IP1SR0(0, 0)

[ 233](pinctrl-r8a779f0_8h.md#a374884c406ec4ddf0e5bfa2ddf8d1994)#define FUNC\_HSCK1 IP1SR0(0, 1)

[ 234](pinctrl-r8a779f0_8h.md#aec8a3c86e45fe23b7d054980acfc2020)#define FUNC\_MSIOF1\_SCK IP1SR0(0, 3)

[ 235](pinctrl-r8a779f0_8h.md#ab3ec1e3ba367b62f5c166d49d77b93b8)#define FUNC\_RTS0\_N IP1SR0(4, 0)

[ 236](pinctrl-r8a779f0_8h.md#a861e3cbfd2486a406eb70d3508d2ee78)#define FUNC\_HRTS1\_N IP1SR0(4, 1)

[ 237](pinctrl-r8a779f0_8h.md#ac59256bc200b286c667a8966e628fe57)#define FUNC\_MSIOF3\_SYNC IP1SR0(4, 2)

[ 238](pinctrl-r8a779f0_8h.md#a8d7f8bf0d1ae2ced5f25256aca9dbb0c)#define FUNC\_TSN1\_MDIO\_A IP1SR0(4, 5)

[ 239](pinctrl-r8a779f0_8h.md#a0a614b349eaee8271652cbe9735d841f)#define FUNC\_CTS0\_N IP1SR0(8, 0)

[ 240](pinctrl-r8a779f0_8h.md#a2a7bc3f84450448e8cd4f1284d71800e)#define FUNC\_HCTS1\_N IP1SR0(8, 1)

[ 241](pinctrl-r8a779f0_8h.md#a1ff0ef7bf58b4f45952c3191409789a3)#define FUNC\_MSIOF1\_SYNC IP1SR0(8, 3)

[ 242](pinctrl-r8a779f0_8h.md#a231c294a5d9d0d6ee800b295dbfaffcd)#define FUNC\_TSN1\_MDC\_A IP1SR0(8, 5)

[ 243](pinctrl-r8a779f0_8h.md#a694da81cb9ea8a3810117bdb2d3305c9)#define FUNC\_MSIOF0\_SYNC IP1SR0(12, 0)

[ 244](pinctrl-r8a779f0_8h.md#aaa64b22be712661c25699263604cd57a)#define FUNC\_HCTS3\_N IP1SR0(12, 1)

[ 245](pinctrl-r8a779f0_8h.md#afb5bcac1912aef8f7580b9c68830bc25)#define FUNC\_CTS1\_N IP1SR0(12, 2)

[ 246](pinctrl-r8a779f0_8h.md#a1e7493f35e9cbbf98922470ea8c88b6e)#define FUNC\_IRQ4 IP1SR0(12, 3)

[ 247](pinctrl-r8a779f0_8h.md#a55958317f1235d2284f4bbc707106fce)#define FUNC\_TSN0\_LINK\_A IP1SR0(12, 5)

[ 248](pinctrl-r8a779f0_8h.md#ac500140f028463f946e4fee244b99dc8)#define FUNC\_MSIOF0\_RXD IP1SR0(16, 0)

[ 249](pinctrl-r8a779f0_8h.md#ae0e1b2608a3ab3e43e5e2fa6cebe493e)#define FUNC\_HRX3 IP1SR0(16, 1)

[ 250](pinctrl-r8a779f0_8h.md#a852324214d7876284cb4caecaa93f3f3)#define FUNC\_RX1 IP1SR0(16, 2)

[ 251](pinctrl-r8a779f0_8h.md#a415b19e98854914a5268b781154aeac0)#define FUNC\_MSIOF0\_TXD IP1SR0(20, 0)

[ 252](pinctrl-r8a779f0_8h.md#a1c20f218f9efe3fcab84df6c045191fd)#define FUNC\_HTX3 IP1SR0(20, 1)

[ 253](pinctrl-r8a779f0_8h.md#a4f9d5c7e39572896ae3b424434a58b90)#define FUNC\_TX1 IP1SR0(20, 2)

[ 254](pinctrl-r8a779f0_8h.md#aec3bf52a08c15cf225b46c067de79b29)#define FUNC\_MSIOF0\_SCK IP1SR0(24, 0)

[ 255](pinctrl-r8a779f0_8h.md#ab969df1d788a635cabbe5cc64e1cea61)#define FUNC\_HSCK3 IP1SR0(24, 1)

[ 256](pinctrl-r8a779f0_8h.md#a2e2564694ce3d9bab2ca634110babd12)#define FUNC\_SCK1 IP1SR0(24, 2)

[ 257](pinctrl-r8a779f0_8h.md#a3af1cd4a0b729bcf95bd8648be9e8b76)#define FUNC\_MSIOF0\_SS1 IP1SR0(28, 0)

[ 258](pinctrl-r8a779f0_8h.md#a91636ed706ff199ac7e5b6a6c2f300be)#define FUNC\_HRTS3\_N IP1SR0(28, 1)

[ 259](pinctrl-r8a779f0_8h.md#a429d41290ac7e1e8d02f6c05b32f7376)#define FUNC\_RTS1\_N IP1SR0(28, 2)

[ 260](pinctrl-r8a779f0_8h.md#afa85b0631ba88f21389f0e39be80c35e)#define FUNC\_IRQ5 IP1SR0(28, 3)

[ 261](pinctrl-r8a779f0_8h.md#a4cd893b2275b293c30d810359fdff317)#define FUNC\_TSN1\_LINK\_A IP1SR0(28, 5)

[ 262](pinctrl-r8a779f0_8h.md#a8a36e419e0beb0bbb418e6e63b51d42a)#define FUNC\_MSIOF0\_SS2 IP2SR0(0, 0)

[ 263](pinctrl-r8a779f0_8h.md#a094fb4b873cd0a8fef48335f2ad58fb8)#define FUNC\_TSN2\_LINK\_A IP2SR0(0, 5)

[ 264](pinctrl-r8a779f0_8h.md#a8093a0a22fe179ba8542a89a013fb573)#define FUNC\_IRQ0 IP2SR0(4, 0)

[ 265](pinctrl-r8a779f0_8h.md#a0426e56ed21b8a4a4285232720a1e2ad)#define FUNC\_MSIOF1\_SS1 IP2SR0(4, 3)

[ 266](pinctrl-r8a779f0_8h.md#a5940900ebeb89169aa97b9e075959858)#define FUNC\_TSN0\_MAGIC\_A IP2SR0(4, 5)

[ 267](pinctrl-r8a779f0_8h.md#ab175aaaa927f86b485c6589f1949a66d)#define FUNC\_IRQ1 IP2SR0(8, 0)

[ 268](pinctrl-r8a779f0_8h.md#a303ffbc93ffcfb3d498e54c5f02cfa7f)#define FUNC\_MSIOF1\_SS2 IP2SR0(8, 3)

[ 269](pinctrl-r8a779f0_8h.md#abd4cdb788cac8f49e6a22766cad787d9)#define FUNC\_TSN0\_PHY\_INT\_A IP2SR0(8, 5)

[ 270](pinctrl-r8a779f0_8h.md#a3637e038ae0080707f61877f978e304e)#define FUNC\_IRQ2 IP2SR0(12, 0)

[ 271](pinctrl-r8a779f0_8h.md#a9a237bf368a101f28477daec589610dd)#define FUNC\_TSN1\_PHY\_INT\_A IP2SR0(12, 5)

[ 272](pinctrl-r8a779f0_8h.md#a463e1089b96456cdf50231bf43129ad1)#define FUNC\_IRQ3 IP2SR0(16, 0)

[ 273](pinctrl-r8a779f0_8h.md#adc9e3bdf6e8a9674a7ae867449923055)#define FUNC\_TSN2\_PHY\_INT\_A IP2SR0(16, 5)

[ 274](pinctrl-r8a779f0_8h.md#a629fc8d4c5add9f363594173a7b45a52)#define FUNC\_GP1\_00 IP0SR1(0, 0)

[ 275](pinctrl-r8a779f0_8h.md#a967767a4147624cfabb667b3cb4a5bb8)#define FUNC\_TCLK1 IP0SR1(0, 1)

[ 276](pinctrl-r8a779f0_8h.md#a65323e5df1ea213897bdd18bc733f8cf)#define FUNC\_HSCK2 IP0SR1(0, 2)

[ 277](pinctrl-r8a779f0_8h.md#ab1f25dd65f25ca96ed311498508b06a4)#define FUNC\_GP1\_01 IP0SR1(4, 0)

[ 278](pinctrl-r8a779f0_8h.md#ab1c606b29c9a594046252a9f427b83b8)#define FUNC\_TCLK4 IP0SR1(4, 1)

[ 279](pinctrl-r8a779f0_8h.md#ad174cc12c687ca5aadcad445b2d717e7)#define FUNC\_HRX2 IP0SR1(4, 2)

[ 280](pinctrl-r8a779f0_8h.md#a22b2e6fec2076e216b478b38bfed7ae5)#define FUNC\_GP1\_02 IP0SR1(8, 0)

[ 281](pinctrl-r8a779f0_8h.md#ac96b17dbf57e2597e0639f444be4dfbd)#define FUNC\_HTX2 IP0SR1(8, 2)

[ 282](pinctrl-r8a779f0_8h.md#ac5836d0f35460a7b8ac3c39242b5ec3d)#define FUNC\_MSIOF2\_SS1 IP0SR1(8, 3)

[ 283](pinctrl-r8a779f0_8h.md#aeda40835777b5b5d9d75726fb2a44e35)#define FUNC\_TSN2\_MDC\_A IP0SR1(8, 5)

[ 284](pinctrl-r8a779f0_8h.md#ad63a35775813dc0d7a4bfecc6f2fb76c)#define FUNC\_GP1\_03 IP0SR1(12, 0)

[ 285](pinctrl-r8a779f0_8h.md#a7c4874fb7fb122fffcddeb66e9c985ba)#define FUNC\_TCLK2 IP0SR1(12, 1)

[ 286](pinctrl-r8a779f0_8h.md#a265ae68f728c384024b8f95d6a89c9e7)#define FUNC\_HCTS2\_N IP0SR1(12, 2)

[ 287](pinctrl-r8a779f0_8h.md#ad0a6a7dbe625eb9ae31ad0d212aa5efb)#define FUNC\_MSIOF2\_SS2 IP0SR1(12, 3)

[ 288](pinctrl-r8a779f0_8h.md#a36bb52913fdfda9128f33282ffbe5dd2)#define FUNC\_CTS4\_N IP0SR1(12, 4)

[ 289](pinctrl-r8a779f0_8h.md#a19d37d2184dc33fcf76731bde9774549)#define FUNC\_TSN2\_MDIO\_A IP0SR1(12, 5)

[ 290](pinctrl-r8a779f0_8h.md#aec54a0086c96e65184a3856378049b55)#define FUNC\_GP1\_04 IP0SR1(16, 0)

[ 291](pinctrl-r8a779f0_8h.md#a8c54ee420f1b00115fbf5aa528cdfc07)#define FUNC\_TCLK3 IP0SR1(16, 1)

[ 292](pinctrl-r8a779f0_8h.md#a6ab4e3d5d8bd816e95e533e7d4bcef5e)#define FUNC\_HRTS2\_N IP0SR1(16, 2)

[ 293](pinctrl-r8a779f0_8h.md#a98b747d96d6ebedb560e44603b480f53)#define FUNC\_MSIOF2\_SYNC IP0SR1(16, 3)

[ 294](pinctrl-r8a779f0_8h.md#a41afdf8e2382bea1f81e25a8859410c0)#define FUNC\_RTS4\_N IP0SR1(16, 4)

[ 295](pinctrl-r8a779f0_8h.md#a2a36748a9646444635cf0c4f323ba3e0)#define FUNC\_GP1\_05 IP0SR1(20, 0)

[ 296](pinctrl-r8a779f0_8h.md#af1e34f0fdfe5efb52b8ae79f04416279)#define FUNC\_MSIOF2\_SCK IP0SR1(20, 1)

[ 297](pinctrl-r8a779f0_8h.md#aa4a9e28c208e2285a09a2e754486dd7c)#define FUNC\_SCK4 IP0SR1(20, 2)

[ 298](pinctrl-r8a779f0_8h.md#a710adac0ff75a578106789f2a37a73da)#define FUNC\_GP1\_06 IP0SR1(24, 0)

[ 299](pinctrl-r8a779f0_8h.md#a2def3f6d3290e2196c2900bc8c19c799)#define FUNC\_MSIOF2\_RXD IP0SR1(24, 1)

[ 300](pinctrl-r8a779f0_8h.md#a01cde3510e3bcbb9b413b626fc43cab4)#define FUNC\_RX4 IP0SR1(24, 2)

[ 301](pinctrl-r8a779f0_8h.md#aecffcc460c3b854afd379172348ba4d3)#define FUNC\_GP1\_07 IP0SR1(28, 0)

[ 302](pinctrl-r8a779f0_8h.md#a0b18d353079959b755d8a6b80a25dc4e)#define FUNC\_MSIOF2\_TXD IP0SR1(28, 1)

[ 303](pinctrl-r8a779f0_8h.md#a71422f4e48922d028d3fe71e8ba18eb0)#define FUNC\_TX4 IP0SR1(28, 2)

[ 304](pinctrl-r8a779f0_8h.md#a06ca3ba00a965d4979ceb9b2ea0d032a)#define FUNC\_GP4\_00 IP0SR4(0, 0)

[ 305](pinctrl-r8a779f0_8h.md#ac1e1b6609c33bd48c29bbd1bbf36756b)#define FUNC\_MSPI4SC IP0SR4(0, 1)

[ 306](pinctrl-r8a779f0_8h.md#a7b9f5ca5e424912c02ffd6c6753325b2)#define FUNC\_TAUD0I2 IP0SR4(0, 3)

[ 307](pinctrl-r8a779f0_8h.md#a26915bce1f087909939ee41161ddd08a)#define FUNC\_TAUD0O2 IP0SR4(0, 4)

[ 308](pinctrl-r8a779f0_8h.md#ab89f72beb59330d14879652bafa8e2d4)#define FUNC\_GP4\_01 IP0SR4(4, 0)

[ 309](pinctrl-r8a779f0_8h.md#aae174e57784fb9a6ddccb1eeb2e513b0)#define FUNC\_MSPI4SI IP0SR4(4, 1)

[ 310](pinctrl-r8a779f0_8h.md#a4d4b756dfad60c5bec9a72d10acf595d)#define FUNC\_TAUD0I4 IP0SR4(4, 3)

[ 311](pinctrl-r8a779f0_8h.md#a4c7a3f19315630da3ef66855398cdb36)#define FUNC\_TAUD0O4 IP0SR4(4, 4)

[ 312](pinctrl-r8a779f0_8h.md#a4ccc54b6e7deb858f95cb06d5f8bd297)#define FUNC\_GP4\_02 IP0SR4(8, 0)

[ 313](pinctrl-r8a779f0_8h.md#a5dc96d81cafd215a0273fc1b7363ae8d)#define FUNC\_MSPI4SO\_MSPI4DCS IP0SR4(8, 1)

[ 314](pinctrl-r8a779f0_8h.md#ad85b6db6cd2e734107c368f49433370f)#define FUNC\_TAUD0I3 IP0SR4(8, 3)

[ 315](pinctrl-r8a779f0_8h.md#a035da4e923aff4825ffedef7ce7c4799)#define FUNC\_TAUD0O3 IP0SR4(8, 4)

[ 316](pinctrl-r8a779f0_8h.md#af0bf04b0a354feb9a852c60e1ab1c3bf)#define FUNC\_GP4\_03 IP0SR4(12, 0)

[ 317](pinctrl-r8a779f0_8h.md#a55b09bb604123e225e091e48c3794727)#define FUNC\_MSPI4CSS1 IP0SR4(12, 1)

[ 318](pinctrl-r8a779f0_8h.md#a47471c659b6d6591619e7b2edc093f6f)#define FUNC\_TAUD0I6 IP0SR4(12, 3)

[ 319](pinctrl-r8a779f0_8h.md#aff8d0b63fc49df63491fd8ceda3416c4)#define FUNC\_TAUD0O6 IP0SR4(12, 4)

[ 320](pinctrl-r8a779f0_8h.md#a0164f27e3408e0b7fc42d12d64f72555)#define FUNC\_GP4\_04 IP0SR4(16, 0)

[ 321](pinctrl-r8a779f0_8h.md#ab4c26c7d25cfe7470a4e0c81a413ae3c)#define FUNC\_MSPI4CSS0 IP0SR4(16, 1)

[ 322](pinctrl-r8a779f0_8h.md#a02f9eeda49f6a57031c135b92e8f8b9f)#define FUNC\_MSPI4SSI\_N IP0SR4(16, 2)

[ 323](pinctrl-r8a779f0_8h.md#a5caeda433deac9e8d023b31198b80d27)#define FUNC\_TAUD0I5 IP0SR4(16, 3)

[ 324](pinctrl-r8a779f0_8h.md#af6d5367e4395d2c9f93e6bd5d31a4962)#define FUNC\_TAUD0O5 IP0SR4(16, 4)

[ 325](pinctrl-r8a779f0_8h.md#a04c3b6dea6ad4ee5622eb5ee210a5471)#define FUNC\_GP4\_05 IP0SR4(20, 0)

[ 326](pinctrl-r8a779f0_8h.md#ab3ae750ea6c3872a307074af02ee27a9)#define FUNC\_MSPI4CSS3 IP0SR4(20, 1)

[ 327](pinctrl-r8a779f0_8h.md#a3074cb4b265840331aedd455d5c9c081)#define FUNC\_TAUD0I8 IP0SR4(20, 3)

[ 328](pinctrl-r8a779f0_8h.md#a09c8b0fd9f71780a5cfb0ebfa52af240)#define FUNC\_TAUD0O8 IP0SR4(20, 4)

[ 329](pinctrl-r8a779f0_8h.md#a3f1d99fe5ad32a56d7687478921c480e)#define FUNC\_GP4\_06 IP0SR4(24, 0)

[ 330](pinctrl-r8a779f0_8h.md#ac303505ec2c4bbf380169b657e6e4c89)#define FUNC\_MSPI4CSS2 IP0SR4(24, 1)

[ 331](pinctrl-r8a779f0_8h.md#af5d43c9c801a02870bb2f4bd5af5073c)#define FUNC\_TAUD0I7 IP0SR4(24, 3)

[ 332](pinctrl-r8a779f0_8h.md#a175c5b85af3462d4e5b1644b65159b1a)#define FUNC\_TAUD0O7 IP0SR4(24, 4)

[ 333](pinctrl-r8a779f0_8h.md#ac835b08b0592312d8bf7b03f211a239a)#define FUNC\_GP4\_07 IP0SR4(28, 0)

[ 334](pinctrl-r8a779f0_8h.md#a76982922ff4cd95bbc2e00a2e776abc7)#define FUNC\_MSPI4CSS5 IP0SR4(28, 1)

[ 335](pinctrl-r8a779f0_8h.md#affc322b77b703f0a9fc7cbbf76484cc3)#define FUNC\_TAUD0I10 IP0SR4(28, 3)

[ 336](pinctrl-r8a779f0_8h.md#a17806055471e4c56a909a2ab36f6ad5a)#define FUNC\_TAUD0O10 IP0SR4(28, 4)

[ 337](pinctrl-r8a779f0_8h.md#adb825d728de5aac2c79fb79eee4dcca1)#define FUNC\_GP4\_08 IP1SR4(0, 0)

[ 338](pinctrl-r8a779f0_8h.md#a991e1b495b737bc531561408d136c8ad)#define FUNC\_MSPI4CSS4 IP1SR4(0, 1)

[ 339](pinctrl-r8a779f0_8h.md#a7c026b93886007c4955bf9e7a82f7949)#define FUNC\_TAUD0I9 IP1SR4(0, 3)

[ 340](pinctrl-r8a779f0_8h.md#a4c09da934e12a08508eab2370d45b2c9)#define FUNC\_TAUD0O9 IP1SR4(0, 4)

[ 341](pinctrl-r8a779f0_8h.md#acd9c279cbe8f1f790a3f1f58239d4157)#define FUNC\_GP4\_09 IP1SR4(4, 0)

[ 342](pinctrl-r8a779f0_8h.md#a09cc4c00a0559754e37879866a4ac086)#define FUNC\_MSPI4CSS7 IP1SR4(4, 1)

[ 343](pinctrl-r8a779f0_8h.md#aa0535a53f6dbb4d068aac9147a78de7b)#define FUNC\_TAUD0I12 IP1SR4(4, 3)

[ 344](pinctrl-r8a779f0_8h.md#a7b61ab06bb94da1e782726495b084a8b)#define FUNC\_TAUD0O12 IP1SR4(4, 4)

[ 345](pinctrl-r8a779f0_8h.md#a615a3a3803a6b1d50e47d05e5fba0f11)#define FUNC\_GP4\_10 IP1SR4(8, 0)

[ 346](pinctrl-r8a779f0_8h.md#a85bd554569df8c1983305e66ffcb6761)#define FUNC\_MSPI4CSS6 IP1SR4(8, 1)

[ 347](pinctrl-r8a779f0_8h.md#af5fbaf09740fb12443bfb6f24ba1b560)#define FUNC\_TAUD0I11 IP1SR4(8, 3)

[ 348](pinctrl-r8a779f0_8h.md#ab3d72c9c4a249dd4bf4424f39dffa096)#define FUNC\_TAUD0O11 IP1SR4(8, 4)

[ 349](pinctrl-r8a779f0_8h.md#af8319750cf4ec1ee2f8a98f2bebde6d2)#define FUNC\_GP4\_11 IP1SR4(12, 0)

[ 350](pinctrl-r8a779f0_8h.md#a98bfac011236e740b026f999d6f7b1c8)#define FUNC\_ERRORIN0\_N IP1SR4(12, 1)

[ 351](pinctrl-r8a779f0_8h.md#a73b6bae20b6948f58f14290df733de87)#define FUNC\_TAUD0I14 IP1SR4(12, 3)

[ 352](pinctrl-r8a779f0_8h.md#a46023b2dd345cabb7fd0c805c022080f)#define FUNC\_TAUD0O14 IP1SR4(12, 4)

[ 353](pinctrl-r8a779f0_8h.md#a5d93ae2071f53ff26a9aef07d755e709)#define FUNC\_GP4\_12 IP1SR4(16, 0)

[ 354](pinctrl-r8a779f0_8h.md#a48f51fb526e801eb5f2f617af459768f)#define FUNC\_ERROROUT\_C\_N IP1SR4(16, 1)

[ 355](pinctrl-r8a779f0_8h.md#a7d3e48e236546a3cd915c00ee5e447a7)#define FUNC\_TAUD0I13 IP1SR4(16, 3)

[ 356](pinctrl-r8a779f0_8h.md#a435b8a23d52a9d5a0dcb3550b9392498)#define FUNC\_TAUD0O13 IP1SR4(16, 4)

[ 357](pinctrl-r8a779f0_8h.md#a1deca89a5f7cad9dd98c4a5d9bf5b965)#define FUNC\_GP4\_13 IP1SR4(20, 0)

[ 358](pinctrl-r8a779f0_8h.md#ae5312d9f07264b1eb7eec8c1ecc210b1)#define FUNC\_GP4\_14 IP1SR4(24, 0)

[ 359](pinctrl-r8a779f0_8h.md#a6d0cf573dda5198106ac6cd24219689b)#define FUNC\_ERRORIN1\_N IP1SR4(24, 1)

[ 360](pinctrl-r8a779f0_8h.md#a8977afd7bd7dcdf6a4189f4f581ac1d5)#define FUNC\_TAUD0I15 IP1SR4(24, 3)

[ 361](pinctrl-r8a779f0_8h.md#aea68a7392a9c86ffe069a3413cb29b4f)#define FUNC\_TAUD0O15 IP1SR4(24, 4)

[ 362](pinctrl-r8a779f0_8h.md#a6dce908f8561388a2392f001b3cab069)#define FUNC\_GP4\_15 IP1SR4(28, 0)

[ 363](pinctrl-r8a779f0_8h.md#acb9ae1dafd4c93060b53bb75bd8fd73b)#define FUNC\_MSPI1CSS3 IP1SR4(28, 1)

[ 364](pinctrl-r8a779f0_8h.md#a6f0ea9f12c53cb73374856884d2d65a0)#define FUNC\_TAUD1I1 IP1SR4(28, 3)

[ 365](pinctrl-r8a779f0_8h.md#a95a9d693f69423e3215981b3cef32647)#define FUNC\_TAUD1O1 IP1SR4(28, 4)

[ 366](pinctrl-r8a779f0_8h.md#ad5781304335a73cec655632f2ef06ba2)#define FUNC\_GP4\_16 IP2SR4(0, 0)

[ 367](pinctrl-r8a779f0_8h.md#a1c9a69536f9282307ff98deda6ccf90d)#define FUNC\_TAUD1I0 IP2SR4(0, 3)

[ 368](pinctrl-r8a779f0_8h.md#a5b3b08b03f0348f0d948bff8eb5f7d30)#define FUNC\_TAUD1O0 IP2SR4(0, 4)

[ 369](pinctrl-r8a779f0_8h.md#a4ec94501c43bbe889194a12cca258838)#define FUNC\_GP4\_17 IP2SR4(4, 0)

[ 370](pinctrl-r8a779f0_8h.md#a817c944e1d98fe379285393292043200)#define FUNC\_MSPI1CSS5 IP2SR4(4, 1)

[ 371](pinctrl-r8a779f0_8h.md#a256f06b48aba0757077edde8d92869f4)#define FUNC\_TAUD1I3 IP2SR4(4, 3)

[ 372](pinctrl-r8a779f0_8h.md#aaeb48dc87fc82e1fe11ad377147db569)#define FUNC\_TAUD1O3 IP2SR4(4, 4)

[ 373](pinctrl-r8a779f0_8h.md#a332bfe03c3b781963d4ddcac8ac42cf9)#define FUNC\_GP4\_18 IP2SR4(8, 0)

[ 374](pinctrl-r8a779f0_8h.md#a4abbdca00422285f90f1d7f9be9fc566)#define FUNC\_MSPI1CSS4 IP2SR4(8, 1)

[ 375](pinctrl-r8a779f0_8h.md#a84b52194e3f61e164174e6a38e75e9c2)#define FUNC\_TAUD1I2 IP2SR4(8, 3)

[ 376](pinctrl-r8a779f0_8h.md#adc97a6db1cb1d1ad875840a443de28e9)#define FUNC\_TAUD1O2 IP2SR4(8, 4)

[ 377](pinctrl-r8a779f0_8h.md#a4260a776e2d837d3cfe292723eafd7dd)#define FUNC\_GP4\_19 IP2SR4(12, 0)

[ 378](pinctrl-r8a779f0_8h.md#aef2bf268bb91cae310534542f610339d)#define FUNC\_MSPI1CSS6 IP2SR4(12, 1)

[ 379](pinctrl-r8a779f0_8h.md#a8a467d9a3f5126b950dda53e6551c599)#define FUNC\_TAUD1I4 IP2SR4(12, 3)

[ 380](pinctrl-r8a779f0_8h.md#a6c5da1cda5636684503b69571c89089c)#define FUNC\_TAUD1O4 IP2SR4(12, 4)

[ 381](pinctrl-r8a779f0_8h.md#a625cf8f2a4b63556e6f7a7de54e92e1b)#define FUNC\_MSPI0SC IP2SR4(16, 0)

[ 382](pinctrl-r8a779f0_8h.md#a44b1fb1f9e840f0b886066c97c515094)#define FUNC\_MSPI1CSS7 IP2SR4(16, 1)

[ 383](pinctrl-r8a779f0_8h.md#aa36f81987c9563f26e0f8c2cab5097f5)#define FUNC\_TAUD1I5 IP2SR4(16, 3)

[ 384](pinctrl-r8a779f0_8h.md#a0128432cc38b1849238677d3801be165)#define FUNC\_TAUD1O5 IP2SR4(16, 4)

[ 385](pinctrl-r8a779f0_8h.md#a4c697b619972a84c178f69c62ffa218c)#define FUNC\_MSPI0SI IP2SR4(20, 0)

[ 386](pinctrl-r8a779f0_8h.md#ac2eb05f03605659c400c425f601d2e91)#define FUNC\_TAUD1I7 IP2SR4(20, 3)

[ 387](pinctrl-r8a779f0_8h.md#aefc0419f08976e9fce0e4054ded2b26e)#define FUNC\_TAUD1O7 IP2SR4(20, 4)

[ 388](pinctrl-r8a779f0_8h.md#aff5b3d236045291d59e494cd95b8dfc9)#define FUNC\_MSPI0SO\_MSPI0DCS IP2SR4(24, 0)

[ 389](pinctrl-r8a779f0_8h.md#a34ea94788ece3c9810707e973b315e31)#define FUNC\_TAUD1I6 IP2SR4(24, 3)

[ 390](pinctrl-r8a779f0_8h.md#a3156497bd9d314894678ec66b785c4b1)#define FUNC\_TAUD1O6 IP2SR4(24, 4)

[ 391](pinctrl-r8a779f0_8h.md#a0a61e3300d8852bee4302a34064c9579)#define FUNC\_MSPI0CSS1 IP2SR4(28, 0)

[ 392](pinctrl-r8a779f0_8h.md#af8951616c61380df67eb79526aa80b47)#define FUNC\_TAUD1I9 IP2SR4(28, 3)

[ 393](pinctrl-r8a779f0_8h.md#a0d050b4db0ebb0f37fde43f26b090f13)#define FUNC\_TAUD1O9 IP2SR4(28, 4)

[ 394](pinctrl-r8a779f0_8h.md#a0615ec8427839da437c5b82931aeb772)#define FUNC\_MSPI0CSS0 IP3SR4(0, 0)

[ 395](pinctrl-r8a779f0_8h.md#adea2bd90a1a8095a5e9de8e856e8a62c)#define FUNC\_MSPI0SSI\_N IP3SR4(0, 1)

[ 396](pinctrl-r8a779f0_8h.md#af16f8cec300f262ba6834f791ed2f4f9)#define FUNC\_TAUD1I8 IP3SR4(0, 3)

[ 397](pinctrl-r8a779f0_8h.md#a9152a44e54bed114e19ed2119d312e38)#define FUNC\_TAUD1O8 IP3SR4(0, 4)

[ 398](pinctrl-r8a779f0_8h.md#aae113f752847e66d95fd7bf7ec1ef40e)#define FUNC\_MSPI1SO\_MSPI1DCS IP3SR4(8, 0)

[ 399](pinctrl-r8a779f0_8h.md#a2db077ed10647290bc29a95a558170d4)#define FUNC\_MSPI0CSS3 IP3SR4(8, 2)

[ 400](pinctrl-r8a779f0_8h.md#a0ebdb3b9aa0ca34a79bd27112573dcfa)#define FUNC\_TAUD1I11 IP3SR4(8, 3)

[ 401](pinctrl-r8a779f0_8h.md#a52895f2a652b116ebaaf673d75a7bc9f)#define FUNC\_TAUD1O11 IP3SR4(8, 4)

[ 402](pinctrl-r8a779f0_8h.md#ac30abb5b0adc11ca69a3e905f8bf3418)#define FUNC\_MSPI1SC IP3SR4(16, 0)

[ 403](pinctrl-r8a779f0_8h.md#a73daf025c61b0425b3a5c3bb43277bda)#define FUNC\_MSPI0CSS2 IP3SR4(16, 2)

[ 404](pinctrl-r8a779f0_8h.md#a13a86a4ed7844a781453624c8588063e)#define FUNC\_TAUD1I10 IP3SR4(16, 3)

[ 405](pinctrl-r8a779f0_8h.md#aefb3cc01fcd9e4344cbc7204f8c22c3c)#define FUNC\_TAUD1O10 IP3SR4(16, 4)

[ 406](pinctrl-r8a779f0_8h.md#a5ae6d85452086310e37aab72eefd56cb)#define FUNC\_RIIC0SCL IP0SR5(0, 0)

[ 407](pinctrl-r8a779f0_8h.md#a098c5785ae5ce82a9842b81391c3a9ca)#define FUNC\_TAUD0I0 IP0SR5(0, 3)

[ 408](pinctrl-r8a779f0_8h.md#abfad3700bc984432527c6fb98c3e3a94)#define FUNC\_TAUD0O0 IP0SR5(0, 4)

[ 409](pinctrl-r8a779f0_8h.md#a9ebd98c8147bcfbb8391df7ff4636998)#define FUNC\_RIIC0SDA IP0SR5(4, 0)

[ 410](pinctrl-r8a779f0_8h.md#a65e4d2759ab44c1697267427c94ba8f9)#define FUNC\_TAUD0I1 IP0SR5(4, 3)

[ 411](pinctrl-r8a779f0_8h.md#a135967cf4283a3a12af050e19a282b51)#define FUNC\_TAUD0O1 IP0SR5(4, 4)

[ 412](pinctrl-r8a779f0_8h.md#a93d4163050deb941a8a0a5ca0535ca57)#define FUNC\_ETNB0MD IP0SR5(8, 0)

[ 413](pinctrl-r8a779f0_8h.md#aa518cfa30d25beb32e0e57c37d9ea746)#define FUNC\_ETNB0WOL IP0SR5(12, 0)

[ 414](pinctrl-r8a779f0_8h.md#a1cec3d66a78232350bf48b8a5461f8e9)#define FUNC\_ETNB0LINKSTA IP0SR5(16, 0)

[ 415](pinctrl-r8a779f0_8h.md#af31869551fde5708034ea804158285d7)#define FUNC\_ETNB0MDC IP0SR5(20, 0)

[ 416](pinctrl-r8a779f0_8h.md#acd929aeebb2dfd607f58710823402650)#define FUNC\_ETNB0RXCLK IP0SR5(24, 0)

[ 417](pinctrl-r8a779f0_8h.md#a53dd2130db3c30a35a049644d3972b8b)#define FUNC\_ETNB0CRS\_DV IP0SR5(24, 1)

[ 418](pinctrl-r8a779f0_8h.md#a29550dc915dc267364808f4f350592c7)#define FUNC\_ETNB0TXCLK IP0SR5(28, 0)

[ 419](pinctrl-r8a779f0_8h.md#a4629c7b0e4fcebe8df78a6c2b8a1b61e)#define FUNC\_ETNB0REFCLK IP0SR5(28, 1)

[ 420](pinctrl-r8a779f0_8h.md#ae53994d1f5ba689b90444f8654110c78)#define FUNC\_RLIN33TX IP1SR6(0, 0)

[ 421](pinctrl-r8a779f0_8h.md#abb4444f30a037e3e5b55207dde64645f)#define FUNC\_TAUJ3O3 IP1SR6(0, 3)

[ 422](pinctrl-r8a779f0_8h.md#a506f97f9286493524317bc31f172e0ba)#define FUNC\_TAUJ3I3 IP1SR6(0, 4)

[ 423](pinctrl-r8a779f0_8h.md#acc92b494aed6b625cf7535650ead75d2)#define FUNC\_NMI1 IP1SR6(0, 5)

[ 424](pinctrl-r8a779f0_8h.md#a33b91e6c6a174f473ab1ce32432436e1)#define FUNC\_RLIN33RX\_INTP19 IP1SR6(4, 0)

[ 425](pinctrl-r8a779f0_8h.md#a5a6f99a85b4d4a8982a3eb19b34df97a)#define FUNC\_TAUJ3O2 IP1SR6(4, 3)

[ 426](pinctrl-r8a779f0_8h.md#a66ef9980e8b3075ec21853173e241a76)#define FUNC\_TAUJ3I2 IP1SR6(4, 4)

[ 427](pinctrl-r8a779f0_8h.md#a94b65750fa4dfb82358045352c23cdbb)#define FUNC\_RLIN32TX IP1SR6(8, 0)

[ 428](pinctrl-r8a779f0_8h.md#a91258305cc97bc53d047ce4f6bc95312)#define FUNC\_TAUJ3O1 IP1SR6(8, 3)

[ 429](pinctrl-r8a779f0_8h.md#afd56e84b2d6c6138c9188b0678e5798b)#define FUNC\_TAUJ3I1 IP1SR6(8, 4)

[ 430](pinctrl-r8a779f0_8h.md#a0bb6e6c55312f900824c63b040853d33)#define FUNC\_RLIN32RX\_INTP18 IP1SR6(12, 0)

[ 431](pinctrl-r8a779f0_8h.md#a7a599e8825d863d3ec0eae5525591074)#define FUNC\_TAUJ3O0 IP1SR6(12, 3)

[ 432](pinctrl-r8a779f0_8h.md#adec0301cbf507ecc0ee55604003ef2bb)#define FUNC\_TAUJ3I0 IP1SR6(12, 4)

[ 433](pinctrl-r8a779f0_8h.md#ac299ddb1499a670c8ff5a353dd3c5de4)#define FUNC\_INTP35 IP1SR6(12, 5)

[ 434](pinctrl-r8a779f0_8h.md#a0238d883452a17ba8a2e59574946919f)#define FUNC\_RLIN31TX IP1SR6(16, 0)

[ 435](pinctrl-r8a779f0_8h.md#aa7e29257402048be837ec1583a5570c6)#define FUNC\_TAUJ1I3 IP1SR6(16, 3)

[ 436](pinctrl-r8a779f0_8h.md#a43627e0aa8f9106aa1e5aec361996d69)#define FUNC\_TAUJ1O3 IP1SR6(16, 4)

[ 437](pinctrl-r8a779f0_8h.md#ae3b713c3130580cc9a0081639d5ee3bd)#define FUNC\_INTP34 IP1SR6(16, 5)

[ 438](pinctrl-r8a779f0_8h.md#a5cca155b631d2282193cf9db10f21ddf)#define FUNC\_RLIN31RX\_INTP17 IP1SR6(20, 0)

[ 439](pinctrl-r8a779f0_8h.md#adb6521a13a4610a4818888846046537d)#define FUNC\_TAUJ1I2 IP1SR6(20, 3)

[ 440](pinctrl-r8a779f0_8h.md#a7c02bef6621efba57f8a20c2827ad2f8)#define FUNC\_TAUJ1O2 IP1SR6(20, 4)

[ 441](pinctrl-r8a779f0_8h.md#aacba0f3673da37e2db7a22be40547a54)#define FUNC\_INTP33 IP1SR6(20, 5)

[ 442](pinctrl-r8a779f0_8h.md#a88edd6a7bf04c0f21687b118b9e9ef39)#define FUNC\_RLIN30TX IP1SR6(24, 0)

[ 443](pinctrl-r8a779f0_8h.md#a02fb4d0ac2c6e65604b09bd6517ac83a)#define FUNC\_TAUJ1I1 IP1SR6(24, 3)

[ 444](pinctrl-r8a779f0_8h.md#ae85de394d9862b261b7cfc4c51b49754)#define FUNC\_TAUJ1O1 IP1SR6(24, 4)

[ 445](pinctrl-r8a779f0_8h.md#a777553df7df25d727d93d433b8f369dc)#define FUNC\_RLIN30RX\_INTP16 IP1SR6(28, 0)

[ 446](pinctrl-r8a779f0_8h.md#a8d1b5397b45af690a343509c717c1204)#define FUNC\_TAUJ1I0 IP1SR6(28, 3)

[ 447](pinctrl-r8a779f0_8h.md#a05bfc60905796a4bc02e1be715bdb210)#define FUNC\_TAUJ1O0 IP1SR6(28, 4)

[ 448](pinctrl-r8a779f0_8h.md#a8404c1c71cb4ac4947c369c4a86bf883)#define FUNC\_FLXA0STPWT IP2SR6(8, 2)

[ 449](pinctrl-r8a779f0_8h.md#a222bb15d27c977033f1a027625bffaf8)#define FUNC\_CAN0TX IP0SR7(0, 0)

[ 450](pinctrl-r8a779f0_8h.md#ace0f864653b864a30cacb17ce8a7fcc7)#define FUNC\_RSENT0SPCO IP0SR7(0, 1)

[ 451](pinctrl-r8a779f0_8h.md#abfa5ba5bfab0668090c291556c09e250)#define FUNC\_MSPI2SO\_MSPI2DCS IP0SR7(0, 3)

[ 452](pinctrl-r8a779f0_8h.md#ab8641544f5a541934a57ad81340a0611)#define FUNC\_CAN0RX\_INTP0 IP0SR7(4, 0)

[ 453](pinctrl-r8a779f0_8h.md#a8d9c25f5294bc636d3c402cbb9c6469b)#define FUNC\_RSENT0RX IP0SR7(4, 1)

[ 454](pinctrl-r8a779f0_8h.md#a23065537df39b84f3b3b1965d93bd52f)#define FUNC\_RSENT0RX\_RSENT0SPCO IP0SR7(4, 2)

[ 455](pinctrl-r8a779f0_8h.md#a8407bdbf7942afe59ca460d0512a307c)#define FUNC\_MSPI2SC IP0SR7(4, 3)

[ 456](pinctrl-r8a779f0_8h.md#abec997847ca390348fc0865c72c5fdf8)#define FUNC\_CAN1TX IP0SR7(8, 0)

[ 457](pinctrl-r8a779f0_8h.md#a76f2c632fa5bc51bc66e16bc98760161)#define FUNC\_RSENT1SPCO IP0SR7(8, 1)

[ 458](pinctrl-r8a779f0_8h.md#ad0bd4c820a9c9637f74c5bedb33bb59f)#define FUNC\_MSPI2SSI\_N IP0SR7(8, 3)

[ 459](pinctrl-r8a779f0_8h.md#ac730d75c324d544984fbe157b30bfd09)#define FUNC\_MSPI2CSS0 IP0SR7(8, 4)

[ 460](pinctrl-r8a779f0_8h.md#aae8669abdfefa9117925bbb4f492514e)#define FUNC\_CAN1RX\_INTP1 IP0SR7(12, 0)

[ 461](pinctrl-r8a779f0_8h.md#af2cc92e439553e0a46e1ee2dbd932194)#define FUNC\_RSENT1RX IP0SR7(12, 1)

[ 462](pinctrl-r8a779f0_8h.md#a9d22716cf58447981a4087c30fd2ddf4)#define FUNC\_RSENT1RX\_RSENT1SPCO IP0SR7(12, 2)

[ 463](pinctrl-r8a779f0_8h.md#ad2f9ff030db1c5bc79b3b446dc273444)#define FUNC\_MSPI2SI IP0SR7(12, 3)

[ 464](pinctrl-r8a779f0_8h.md#aa9304a9454ab05c48f830907d52d2eec)#define FUNC\_CAN2TX IP0SR7(16, 0)

[ 465](pinctrl-r8a779f0_8h.md#aa5d34a2e34570944e54690fa16bfbee6)#define FUNC\_RSENT2SPCO IP0SR7(16, 1)

[ 466](pinctrl-r8a779f0_8h.md#aac84b0378d85eafa1ac2b6156bab24c7)#define FUNC\_MSPI2CSS2 IP0SR7(16, 4)

[ 467](pinctrl-r8a779f0_8h.md#a3b19af19e76b774cae535905142d38f5)#define FUNC\_CAN2RX\_INTP2 IP0SR7(20, 0)

[ 468](pinctrl-r8a779f0_8h.md#a7ba45955c8c568b909cd252a789799d0)#define FUNC\_RSENT2RX IP0SR7(20, 1)

[ 469](pinctrl-r8a779f0_8h.md#a2a2bb0b8cadaa15b11996bb85e01fd51)#define FUNC\_RSENT2RX\_RSENT2SPCO IP0SR7(20, 2)

[ 470](pinctrl-r8a779f0_8h.md#aef44db4ac75a69c9d719c7e7413c498b)#define FUNC\_MSPI2CSS1 IP0SR7(20, 4)

[ 471](pinctrl-r8a779f0_8h.md#aa479d3ff28b2d94cc489fc0eadc22039)#define FUNC\_CAN3TX IP0SR7(24, 0)

[ 472](pinctrl-r8a779f0_8h.md#ad4aecab7016937bb605265594203ff5a)#define FUNC\_RSENT3SPCO IP0SR7(24, 1)

[ 473](pinctrl-r8a779f0_8h.md#a093e3f9a4960898c0d5c0c3b901377dd)#define FUNC\_MSPI2CSS4 IP0SR7(24, 4)

[ 474](pinctrl-r8a779f0_8h.md#a4663b75818fddfd79625c67efd017195)#define FUNC\_CAN3RX\_INTP3 IP0SR7(28, 0)

[ 475](pinctrl-r8a779f0_8h.md#a5ef33d55bdb3080b16781e2912f7afa3)#define FUNC\_RSENT3RX IP0SR7(28, 1)

[ 476](pinctrl-r8a779f0_8h.md#a26a96188451029f27697883aa3b55c18)#define FUNC\_RSENT3RX\_RSENT3SPCO IP0SR7(28, 2)

[ 477](pinctrl-r8a779f0_8h.md#a7062223ad93987483398988277aec350)#define FUNC\_MSPI2CSS3 IP0SR7(28, 4)

[ 478](pinctrl-r8a779f0_8h.md#a899e366d999892884834b2e7d4fef591)#define FUNC\_CAN4TX IP1SR7(0, 0)

[ 479](pinctrl-r8a779f0_8h.md#afbdec33e3f2641d39d522175aba49d44)#define FUNC\_RSENT4SPCO IP1SR7(0, 1)

[ 480](pinctrl-r8a779f0_8h.md#a701a2ca92009fdc6ac01424fd7f4b198)#define FUNC\_MSPI2CSS6 IP1SR7(0, 4)

[ 481](pinctrl-r8a779f0_8h.md#ad99d37fe43a9cb266da39f39ff22e636)#define FUNC\_CAN4RX\_INTP4 IP1SR7(4, 0)

[ 482](pinctrl-r8a779f0_8h.md#a6360416521a0e22d79fc54a3cbc502e1)#define FUNC\_RSENT4RX IP1SR7(4, 1)

[ 483](pinctrl-r8a779f0_8h.md#adcd7ec0f8daa5a6bf7782ee9a5a21d31)#define FUNC\_RSENT4RX\_RSENT4SPCO IP1SR7(4, 2)

[ 484](pinctrl-r8a779f0_8h.md#a1d732335f5baea3fcb601302db357641)#define FUNC\_MSPI2CSS5 IP1SR7(4, 4)

[ 485](pinctrl-r8a779f0_8h.md#a3567f6a66c108014c031929bc2ad566f)#define FUNC\_CAN5TX IP1SR7(8, 0)

[ 486](pinctrl-r8a779f0_8h.md#a55260e91026e0e5e20275312958cdf6e)#define FUNC\_RSENT5SPCO IP1SR7(8, 1)

[ 487](pinctrl-r8a779f0_8h.md#a592302578069981c31c7c641355eae0f)#define FUNC\_CAN5RX\_INTP5 IP1SR7(12, 0)

[ 488](pinctrl-r8a779f0_8h.md#a709b8927bef5ea0ef9962d99ea89ba49)#define FUNC\_RSENT5RX IP1SR7(12, 1)

[ 489](pinctrl-r8a779f0_8h.md#a5d1e5c5bfc0a7829248cf20914fb9257)#define FUNC\_RSENT5RX\_RSENT5SPCO IP1SR7(12, 2)

[ 490](pinctrl-r8a779f0_8h.md#a9430bac452edbbc497b7fe6d8d44242a)#define FUNC\_MSPI2CSS7 IP1SR7(12, 4)

[ 491](pinctrl-r8a779f0_8h.md#aac4037724a440b6f01cd3a74c4ebb3e6)#define FUNC\_CAN6TX IP1SR7(16, 0)

[ 492](pinctrl-r8a779f0_8h.md#af0e198daca84ed3d7ae4d86a5b7b5c25)#define FUNC\_RSENT6SPCO IP1SR7(16, 1)

[ 493](pinctrl-r8a779f0_8h.md#ab3b49ba7350e2a8d09ed7ea82c64d8c0)#define FUNC\_MSPI3SO\_MSPI3DCS IP1SR7(16, 3)

[ 494](pinctrl-r8a779f0_8h.md#a0fe5b12f5fa0e2dcb900c63dcfb1c42e)#define FUNC\_CAN6RX\_INTP6 IP1SR7(20, 0)

[ 495](pinctrl-r8a779f0_8h.md#a8700c3d065a54ecae1c5061e9e6e4d93)#define FUNC\_RSENT6RX IP1SR7(20, 1)

[ 496](pinctrl-r8a779f0_8h.md#aaf6bd802402bd3ef428ed1c87b5e634b)#define FUNC\_RSENT6RX\_RSENT6SPCO IP1SR7(20, 2)

[ 497](pinctrl-r8a779f0_8h.md#a2d2b4756138938b8065375c7bb360e9a)#define FUNC\_MSPI3SC IP1SR7(20, 3)

[ 498](pinctrl-r8a779f0_8h.md#a7414c543f8afc1cc1650b25cc34a8c69)#define FUNC\_CAN7TX IP1SR7(24, 0)

[ 499](pinctrl-r8a779f0_8h.md#a7a4d840855a52a1642ca06d151170dbb)#define FUNC\_RSENT7SPCO IP1SR7(24, 1)

[ 500](pinctrl-r8a779f0_8h.md#a095c6884678f5b2d2f3585ceb489ce73)#define FUNC\_MSPI3SSI\_N IP1SR7(24, 3)

[ 501](pinctrl-r8a779f0_8h.md#a64a6f3228145dd6a01cc95101979e6ef)#define FUNC\_CAN7RX\_INTP7 IP1SR7(28, 0)

[ 502](pinctrl-r8a779f0_8h.md#a8e62d22236813f84c75bf24531ed15e8)#define FUNC\_RSENT7RX IP1SR7(28, 1)

[ 503](pinctrl-r8a779f0_8h.md#a9338de3268c4c1c8f6c99a02b9c4d485)#define FUNC\_RSENT7RX\_RSENT7SPCO IP1SR7(28, 2)

[ 504](pinctrl-r8a779f0_8h.md#a8fc26204285ebd3f68d0a96539b6c661)#define FUNC\_MSPI3SI IP1SR7(28, 3)

[ 505](pinctrl-r8a779f0_8h.md#aab0317376eda764fc5e45309924c1bb9)#define FUNC\_CAN8TX IP2SR7(0, 0)

[ 506](pinctrl-r8a779f0_8h.md#a749de5b49f8602e4be100500144d3a19)#define FUNC\_RLIN38TX IP2SR7(0, 1)

[ 507](pinctrl-r8a779f0_8h.md#a7b08d68acb55cf9f3df70e5db09a9c8f)#define FUNC\_MSPI3CSS1 IP2SR7(0, 3)

[ 508](pinctrl-r8a779f0_8h.md#ae974a7610639eebf5d9278eca37b440b)#define FUNC\_CAN8RX\_INTP8 IP2SR7(4, 0)

[ 509](pinctrl-r8a779f0_8h.md#a6ecd65d589bf27bfde2e14d7d3403b0f)#define FUNC\_RLIN38RX\_INTP24 IP2SR7(4, 1)

[ 510](pinctrl-r8a779f0_8h.md#aa60675d0bb2129e9f56ad26f9ca57f24)#define FUNC\_MSPI3CSS0 IP2SR7(4, 3)

[ 511](pinctrl-r8a779f0_8h.md#a56049e3dcfc2bcf12c954a1fdfaa6cbc)#define FUNC\_CAN9TX IP2SR7(8, 0)

[ 512](pinctrl-r8a779f0_8h.md#a2ed5c7bf5670da9d737644cf950f3e45)#define FUNC\_RLIN39TX IP2SR7(8, 1)

[ 513](pinctrl-r8a779f0_8h.md#a066a033b8c57121ab7d2c0571eac9a54)#define FUNC\_MSPI3CSS3 IP2SR7(8, 3)

[ 514](pinctrl-r8a779f0_8h.md#ae427b3d4f6b159005cc0bb4776f67c4d)#define FUNC\_CAN9RX\_INTP9 IP2SR7(12, 0)

[ 515](pinctrl-r8a779f0_8h.md#aeca69e03a6cdeec3870ac2930b327d13)#define FUNC\_RLIN39RX\_INTP25 IP2SR7(12, 1)

[ 516](pinctrl-r8a779f0_8h.md#aa910c62ec7abd34039ff1aa2f0086f2d)#define FUNC\_MSPI3CSS2 IP2SR7(12, 3)

[ 517](pinctrl-r8a779f0_8h.md#acffae50fb7368d84b02ff0214395614f)#define FUNC\_CAN10TX IP2SR7(16, 0)

[ 518](pinctrl-r8a779f0_8h.md#a7270022b223afc372b3b9e5810b7037b)#define FUNC\_RLIN310TX IP2SR7(16, 1)

[ 519](pinctrl-r8a779f0_8h.md#a6249f7cf50607bb781255e755af65687)#define FUNC\_MSPI3CSS5 IP2SR7(16, 3)

[ 520](pinctrl-r8a779f0_8h.md#af6151bb5e4d7ee00856a65066ffee85f)#define FUNC\_CAN10RX\_INTP10 IP2SR7(20, 0)

[ 521](pinctrl-r8a779f0_8h.md#a11e990c65016bd043d37ba4a1c68a6b6)#define FUNC\_RLIN310RX\_INTP26 IP2SR7(20, 1)

[ 522](pinctrl-r8a779f0_8h.md#aa05f90a97bea0e2756e9b050ec62b16a)#define FUNC\_MSPI3CSS4 IP2SR7(20, 3)

[ 523](pinctrl-r8a779f0_8h.md#a565589610f5c0d6dbd98459ad016e9c7)#define FUNC\_CAN11TX IP2SR7(24, 0)

[ 524](pinctrl-r8a779f0_8h.md#ad3c2ef41492b94d673fe6c882ec21934)#define FUNC\_RLIN311TX IP2SR7(24, 1)

[ 525](pinctrl-r8a779f0_8h.md#a56c168ac3d7fb71a7f7c12b98bb07572)#define FUNC\_MSPI3CSS7 IP2SR7(24, 3)

[ 526](pinctrl-r8a779f0_8h.md#a3e28397a4720c9efabcf85338b730cc1)#define FUNC\_CAN11RX\_INTP11 IP2SR7(28, 0)

[ 527](pinctrl-r8a779f0_8h.md#a943b41637879c12337989e1cab3099f9)#define FUNC\_RLIN311RX\_INTP27 IP2SR7(28, 1)

[ 528](pinctrl-r8a779f0_8h.md#abf2de5016bf7e2cbbbd811dcde123733)#define FUNC\_MSPI3CSS6 IP2SR7(28, 3)

[ 529](pinctrl-r8a779f0_8h.md#a98185d124caf30b7ba24ec772824abe1)#define FUNC\_FLXA0RXDB IP3SR7(8, 2)

[ 530](pinctrl-r8a779f0_8h.md#a93d75ec717be4420a897c3503ad6412f)#define FUNC\_FLXA0RXDA IP3SR7(12, 2)

[ 531](pinctrl-r8a779f0_8h.md#a2cfe98a4fd9eb2808edd76890c09afbb)#define FUNC\_FLXA0TXDB IP3SR7(16, 2)

[ 532](pinctrl-r8a779f0_8h.md#a47b82a7868e70e05703464d668c0a06d)#define FUNC\_FLXA0TXDA IP3SR7(20, 2)

[ 533](pinctrl-r8a779f0_8h.md#a692ea3e360510854d7b3ed92468a053d)#define FUNC\_FLXA0TXENB IP3SR7(24, 2)

[ 534](pinctrl-r8a779f0_8h.md#a8d8a481ad65537c44291fe768fa203fe)#define FUNC\_FLXA0TXENA IP3SR7(28, 2)

535

536#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_R8A779F0\_H\_ \*/

[pinctrl-rcar-common.h](pinctrl-rcar-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-r8a779f0.h](pinctrl-r8a779f0_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
