---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ra__flash__api__extensions_8h_source.html
original_path: doxygen/html/ra__flash__api__extensions_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra\_flash\_api\_extensions.h

[Go to the documentation of this file.](ra__flash__api__extensions_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_RA\_EXTENSIONS\_H\_\_

8#define \_\_ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_RA\_EXTENSIONS\_H\_\_

9

10#include <[zephyr/drivers/flash.h](flash_8h.md)>

11

[ 12](ra__flash__api__extensions_8h.md#a00ad044f5928882300e87ff9a13c1f74)enum [ra\_ex\_ops](ra__flash__api__extensions_8h.md#a00ad044f5928882300e87ff9a13c1f74) {

[ 13](ra__flash__api__extensions_8h.md#a00ad044f5928882300e87ff9a13c1f74a4404f66075376689dc4670d556f31f48) [FLASH\_RA\_EX\_OP\_WRITE\_PROTECT](ra__flash__api__extensions_8h.md#a00ad044f5928882300e87ff9a13c1f74a4404f66075376689dc4670d556f31f48) = [FLASH\_EX\_OP\_VENDOR\_BASE](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3),

14};

15

[ 16](structflash__ra__cf__block__map.md)typedef struct {

17 union {

[ 18](structflash__ra__cf__block__map.md#a101c65bd2aec6ca07fa625939614673c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [BPS](structflash__ra__cf__block__map.md#a101c65bd2aec6ca07fa625939614673c)[4];

19

20 struct {

[ 21](structflash__ra__cf__block__map.md#aab665bbc1e9ff1a7daa74acb6dc191c0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b000](structflash__ra__cf__block__map.md#aab665bbc1e9ff1a7daa74acb6dc191c0): 1;

[ 22](structflash__ra__cf__block__map.md#ac0a4b33efd9c4bf4ddf705000a566830) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b001](structflash__ra__cf__block__map.md#ac0a4b33efd9c4bf4ddf705000a566830): 1;

[ 23](structflash__ra__cf__block__map.md#aff993abeb30ea8d8054f96b41100af2b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b002](structflash__ra__cf__block__map.md#aff993abeb30ea8d8054f96b41100af2b): 1;

[ 24](structflash__ra__cf__block__map.md#a476ade06264c7d8748589684e8d659d7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b003](structflash__ra__cf__block__map.md#a476ade06264c7d8748589684e8d659d7): 1;

[ 25](structflash__ra__cf__block__map.md#ad2fd670a9fc1cb21fc2b7ec05ffd1190) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b004](structflash__ra__cf__block__map.md#ad2fd670a9fc1cb21fc2b7ec05ffd1190): 1;

[ 26](structflash__ra__cf__block__map.md#a2389957ae22cfcd8ba7a04c71e56a598) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b005](structflash__ra__cf__block__map.md#a2389957ae22cfcd8ba7a04c71e56a598): 1;

[ 27](structflash__ra__cf__block__map.md#acbe4d9e8b4a28d61c340d3bc6ef3b58f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b006](structflash__ra__cf__block__map.md#acbe4d9e8b4a28d61c340d3bc6ef3b58f): 1;

[ 28](structflash__ra__cf__block__map.md#a4913252756d3c3603adfb53ecfd4ca30) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b007](structflash__ra__cf__block__map.md#a4913252756d3c3603adfb53ecfd4ca30): 1;

[ 29](structflash__ra__cf__block__map.md#a395cecde2aede749366cf98d77671f20) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b008](structflash__ra__cf__block__map.md#a395cecde2aede749366cf98d77671f20): 1;

[ 30](structflash__ra__cf__block__map.md#a1e30edab982ea030c12fd6769c609dae) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b009](structflash__ra__cf__block__map.md#a1e30edab982ea030c12fd6769c609dae): 1;

[ 31](structflash__ra__cf__block__map.md#a0c44c3265eaeeafdc3d99cb6cc75c181) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b010](structflash__ra__cf__block__map.md#a0c44c3265eaeeafdc3d99cb6cc75c181): 1;

[ 32](structflash__ra__cf__block__map.md#a8b50ba68eb37b6efc2c0965144a57a1b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b011](structflash__ra__cf__block__map.md#a8b50ba68eb37b6efc2c0965144a57a1b): 1;

[ 33](structflash__ra__cf__block__map.md#a0252324460746c1e7ee79fccd50c23bd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b012](structflash__ra__cf__block__map.md#a0252324460746c1e7ee79fccd50c23bd): 1;

[ 34](structflash__ra__cf__block__map.md#ae53254d344fec51cde3de9daff5fee7e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b013](structflash__ra__cf__block__map.md#ae53254d344fec51cde3de9daff5fee7e): 1;

[ 35](structflash__ra__cf__block__map.md#a77cb77c43ff3a75b655f912f352e74af) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b014](structflash__ra__cf__block__map.md#a77cb77c43ff3a75b655f912f352e74af): 1;

[ 36](structflash__ra__cf__block__map.md#a94c9bfc6b185bb9f6dfc12f85bf92ccd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b015](structflash__ra__cf__block__map.md#a94c9bfc6b185bb9f6dfc12f85bf92ccd): 1;

[ 37](structflash__ra__cf__block__map.md#a41ce7c7853f6c5f2eb216e5ec376233a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b016](structflash__ra__cf__block__map.md#a41ce7c7853f6c5f2eb216e5ec376233a): 1;

[ 38](structflash__ra__cf__block__map.md#a6e5eae2dccd25da5d5f810a28c13febc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b017](structflash__ra__cf__block__map.md#a6e5eae2dccd25da5d5f810a28c13febc): 1;

[ 39](structflash__ra__cf__block__map.md#af3723aa40307c3394e5892c6fc7c449f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b018](structflash__ra__cf__block__map.md#af3723aa40307c3394e5892c6fc7c449f): 1;

[ 40](structflash__ra__cf__block__map.md#a22a077382154519b867a7f2e74935111) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b019](structflash__ra__cf__block__map.md#a22a077382154519b867a7f2e74935111): 1;

[ 41](structflash__ra__cf__block__map.md#ae0610211a298f68244d3c7e8eeda324f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b020](structflash__ra__cf__block__map.md#ae0610211a298f68244d3c7e8eeda324f): 1;

[ 42](structflash__ra__cf__block__map.md#af3167f6678a3b7ebf19a9b51318fabef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b021](structflash__ra__cf__block__map.md#af3167f6678a3b7ebf19a9b51318fabef): 1;

[ 43](structflash__ra__cf__block__map.md#af4ac762cc131c66834186c20276ee0bc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b022](structflash__ra__cf__block__map.md#af4ac762cc131c66834186c20276ee0bc): 1;

[ 44](structflash__ra__cf__block__map.md#a864feb35216f5a0d287a3e995f60c46a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b023](structflash__ra__cf__block__map.md#a864feb35216f5a0d287a3e995f60c46a): 1;

[ 45](structflash__ra__cf__block__map.md#acb026914242bd25ab7aeb38f63251a91) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b024](structflash__ra__cf__block__map.md#acb026914242bd25ab7aeb38f63251a91): 1;

[ 46](structflash__ra__cf__block__map.md#a4b3257ad9cb7aff11c96b1be8e93b938) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b025](structflash__ra__cf__block__map.md#a4b3257ad9cb7aff11c96b1be8e93b938): 1;

[ 47](structflash__ra__cf__block__map.md#a7267903aef20133fcc65fe13adaf9dce) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b026](structflash__ra__cf__block__map.md#a7267903aef20133fcc65fe13adaf9dce): 1;

[ 48](structflash__ra__cf__block__map.md#a9a004f814ecc9295d0bfb6a058603a4d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b027](structflash__ra__cf__block__map.md#a9a004f814ecc9295d0bfb6a058603a4d): 1;

[ 49](structflash__ra__cf__block__map.md#acf7e1c4c60cc9a55608450038c60076e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b028](structflash__ra__cf__block__map.md#acf7e1c4c60cc9a55608450038c60076e): 1;

[ 50](structflash__ra__cf__block__map.md#a378ded6128b4a0c46b621d2a20d41785) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b029](structflash__ra__cf__block__map.md#a378ded6128b4a0c46b621d2a20d41785): 1;

[ 51](structflash__ra__cf__block__map.md#a3aff2f55fa9746c65fab3d8fa73f8f28) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b030](structflash__ra__cf__block__map.md#a3aff2f55fa9746c65fab3d8fa73f8f28): 1;

[ 52](structflash__ra__cf__block__map.md#a0a75ae0c1580b20370edf626b7089e96) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b031](structflash__ra__cf__block__map.md#a0a75ae0c1580b20370edf626b7089e96): 1;

[ 53](structflash__ra__cf__block__map.md#a6a1c1afb76b55f9ca7c8ca8921aeab94) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b032](structflash__ra__cf__block__map.md#a6a1c1afb76b55f9ca7c8ca8921aeab94): 1;

[ 54](structflash__ra__cf__block__map.md#a561164667e632832f3f36d2dfc99194e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b033](structflash__ra__cf__block__map.md#a561164667e632832f3f36d2dfc99194e): 1;

[ 55](structflash__ra__cf__block__map.md#ac6f2969063187429f296f00ddee15dc5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b034](structflash__ra__cf__block__map.md#ac6f2969063187429f296f00ddee15dc5): 1;

[ 56](structflash__ra__cf__block__map.md#ad28df448a10e65c4d45f0591df45863f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b035](structflash__ra__cf__block__map.md#ad28df448a10e65c4d45f0591df45863f): 1;

[ 57](structflash__ra__cf__block__map.md#a0965d4c1ce6ad9b15c992cbee7e43581) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b036](structflash__ra__cf__block__map.md#a0965d4c1ce6ad9b15c992cbee7e43581): 1;

[ 58](structflash__ra__cf__block__map.md#a193d2edbca49b718ea376ecf505ceed1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b037](structflash__ra__cf__block__map.md#a193d2edbca49b718ea376ecf505ceed1): 1;

[ 59](structflash__ra__cf__block__map.md#aecbdc2ba15bfe55a890c52ac45b09fdd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b038](structflash__ra__cf__block__map.md#aecbdc2ba15bfe55a890c52ac45b09fdd): 1;

[ 60](structflash__ra__cf__block__map.md#a3680fae5d1a4c9c3b48fc882b12067ae) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b039](structflash__ra__cf__block__map.md#a3680fae5d1a4c9c3b48fc882b12067ae): 1;

[ 61](structflash__ra__cf__block__map.md#ae662e4d2c2e5adac1c19fb0298c7b4ad) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b040](structflash__ra__cf__block__map.md#ae662e4d2c2e5adac1c19fb0298c7b4ad): 1;

[ 62](structflash__ra__cf__block__map.md#aff3eca7d27b10df6affe86af33d21e0a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b041](structflash__ra__cf__block__map.md#aff3eca7d27b10df6affe86af33d21e0a): 1;

[ 63](structflash__ra__cf__block__map.md#a78b1ad51fe8dbc438fd099195a6ea986) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b042](structflash__ra__cf__block__map.md#a78b1ad51fe8dbc438fd099195a6ea986): 1;

[ 64](structflash__ra__cf__block__map.md#a80697ee52d28c583896d5c7ed5d488f5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b043](structflash__ra__cf__block__map.md#a80697ee52d28c583896d5c7ed5d488f5): 1;

[ 65](structflash__ra__cf__block__map.md#a720b5de073fa683ccd37080a1cec2cbf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b044](structflash__ra__cf__block__map.md#a720b5de073fa683ccd37080a1cec2cbf): 1;

[ 66](structflash__ra__cf__block__map.md#a8d3fa1d37b1aa526ded7d470e9af55dd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b045](structflash__ra__cf__block__map.md#a8d3fa1d37b1aa526ded7d470e9af55dd): 1;

[ 67](structflash__ra__cf__block__map.md#aa149c469d2afab259d0b8713901dbdc1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b046](structflash__ra__cf__block__map.md#aa149c469d2afab259d0b8713901dbdc1): 1;

[ 68](structflash__ra__cf__block__map.md#ae664ecf070f0ebca55d12cacd75cc175) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b047](structflash__ra__cf__block__map.md#ae664ecf070f0ebca55d12cacd75cc175): 1;

[ 69](structflash__ra__cf__block__map.md#a89d41c4ed781723ddf46f82d96388171) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b048](structflash__ra__cf__block__map.md#a89d41c4ed781723ddf46f82d96388171): 1;

[ 70](structflash__ra__cf__block__map.md#a9bc8e17cf5e726e3f4c6f447feb8b6cc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b049](structflash__ra__cf__block__map.md#a9bc8e17cf5e726e3f4c6f447feb8b6cc): 1;

[ 71](structflash__ra__cf__block__map.md#adaaf903d2d26f8420af85870427cc077) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b050](structflash__ra__cf__block__map.md#adaaf903d2d26f8420af85870427cc077): 1;

[ 72](structflash__ra__cf__block__map.md#a3d7f074c57806c9ea231f1833952dfa5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b051](structflash__ra__cf__block__map.md#a3d7f074c57806c9ea231f1833952dfa5): 1;

[ 73](structflash__ra__cf__block__map.md#a441a9092824122b640aebd23bf375455) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b052](structflash__ra__cf__block__map.md#a441a9092824122b640aebd23bf375455): 1;

[ 74](structflash__ra__cf__block__map.md#ae4a6353ea5ea3782717b64d244ab0f6d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b053](structflash__ra__cf__block__map.md#ae4a6353ea5ea3782717b64d244ab0f6d): 1;

[ 75](structflash__ra__cf__block__map.md#adb0d60c86cdd968016693847a76b7fcf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b054](structflash__ra__cf__block__map.md#adb0d60c86cdd968016693847a76b7fcf): 1;

[ 76](structflash__ra__cf__block__map.md#a8d5882d109314f72e9168a53a95f88b7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b055](structflash__ra__cf__block__map.md#a8d5882d109314f72e9168a53a95f88b7): 1;

[ 77](structflash__ra__cf__block__map.md#afe45733316726992bcfebb604da5fee1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b056](structflash__ra__cf__block__map.md#afe45733316726992bcfebb604da5fee1): 1;

[ 78](structflash__ra__cf__block__map.md#a1457c2d9117a476800a494565c49be5b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b057](structflash__ra__cf__block__map.md#a1457c2d9117a476800a494565c49be5b): 1;

[ 79](structflash__ra__cf__block__map.md#aec302f0382977f82a89f8b9f03c00c43) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b058](structflash__ra__cf__block__map.md#aec302f0382977f82a89f8b9f03c00c43): 1;

[ 80](structflash__ra__cf__block__map.md#acea3a50b7663d7a1a7ae32df8edb543b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b059](structflash__ra__cf__block__map.md#acea3a50b7663d7a1a7ae32df8edb543b): 1;

[ 81](structflash__ra__cf__block__map.md#a262a98868ffe43c200502fa2320690a7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b060](structflash__ra__cf__block__map.md#a262a98868ffe43c200502fa2320690a7): 1;

[ 82](structflash__ra__cf__block__map.md#ad5d6e34e3f8988b44f5a83b975371495) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b061](structflash__ra__cf__block__map.md#ad5d6e34e3f8988b44f5a83b975371495): 1;

[ 83](structflash__ra__cf__block__map.md#a0e2874f723fe0f08ad3fb124d87537a5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b062](structflash__ra__cf__block__map.md#a0e2874f723fe0f08ad3fb124d87537a5): 1;

[ 84](structflash__ra__cf__block__map.md#a3ee5d4cded42a95d20af476cd0f1d11b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b063](structflash__ra__cf__block__map.md#a3ee5d4cded42a95d20af476cd0f1d11b): 1;

[ 85](structflash__ra__cf__block__map.md#a6804c794d52c12112b422887751b0505) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b064](structflash__ra__cf__block__map.md#a6804c794d52c12112b422887751b0505): 1;

[ 86](structflash__ra__cf__block__map.md#a650eeff10b6f8fb39781b135c76e3719) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b065](structflash__ra__cf__block__map.md#a650eeff10b6f8fb39781b135c76e3719): 1;

[ 87](structflash__ra__cf__block__map.md#a1163f8a0a4a3112aa1985a283e17ecfc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b066](structflash__ra__cf__block__map.md#a1163f8a0a4a3112aa1985a283e17ecfc): 1;

[ 88](structflash__ra__cf__block__map.md#aeb4dea7898da9f5cbc0e645a140fb83e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b067](structflash__ra__cf__block__map.md#aeb4dea7898da9f5cbc0e645a140fb83e): 1;

[ 89](structflash__ra__cf__block__map.md#a9982c0ede4ff499f29bc31c07fb2e4e0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b068](structflash__ra__cf__block__map.md#a9982c0ede4ff499f29bc31c07fb2e4e0): 1;

[ 90](structflash__ra__cf__block__map.md#af4139fb3c97a934b2d852bb789ecc7cb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b069](structflash__ra__cf__block__map.md#af4139fb3c97a934b2d852bb789ecc7cb): 1;

[ 91](structflash__ra__cf__block__map.md#a19b70fe75c0bc35233f81137d2b1b9de) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b070](structflash__ra__cf__block__map.md#a19b70fe75c0bc35233f81137d2b1b9de): 1;

[ 92](structflash__ra__cf__block__map.md#ace79cf904d9e7cade53b69a9bb399b20) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b071](structflash__ra__cf__block__map.md#ace79cf904d9e7cade53b69a9bb399b20): 1;

[ 93](structflash__ra__cf__block__map.md#acd5d3b551788b54c057ff12a94e00298) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b072](structflash__ra__cf__block__map.md#acd5d3b551788b54c057ff12a94e00298): 1;

[ 94](structflash__ra__cf__block__map.md#ae90d8579cecfc5b4dca41146ba24fe12) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b073](structflash__ra__cf__block__map.md#ae90d8579cecfc5b4dca41146ba24fe12): 1;

[ 95](structflash__ra__cf__block__map.md#abcbb9236f45d28a4c00b65f2a836b506) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b074](structflash__ra__cf__block__map.md#abcbb9236f45d28a4c00b65f2a836b506): 1;

[ 96](structflash__ra__cf__block__map.md#aac819746680655ef6badfcb7153a541c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b075](structflash__ra__cf__block__map.md#aac819746680655ef6badfcb7153a541c): 1;

[ 97](structflash__ra__cf__block__map.md#a4437ed4c525685b80967bbec8ed8a9be) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b076](structflash__ra__cf__block__map.md#a4437ed4c525685b80967bbec8ed8a9be): 1;

[ 98](structflash__ra__cf__block__map.md#a8a6a13d75573a6e30a1e5f2f4c923723) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b077](structflash__ra__cf__block__map.md#a8a6a13d75573a6e30a1e5f2f4c923723): 1;

[ 99](structflash__ra__cf__block__map.md#aa8b5ecbd829ac2eb63a467c388a25bfd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b078](structflash__ra__cf__block__map.md#aa8b5ecbd829ac2eb63a467c388a25bfd): 1;

[ 100](structflash__ra__cf__block__map.md#a1cb41bd08cf5405b442df75bc5b99cbc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b079](structflash__ra__cf__block__map.md#a1cb41bd08cf5405b442df75bc5b99cbc): 1;

[ 101](structflash__ra__cf__block__map.md#a54a1fe008cb4455da6e9cc196e53b173) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b080](structflash__ra__cf__block__map.md#a54a1fe008cb4455da6e9cc196e53b173): 1;

[ 102](structflash__ra__cf__block__map.md#a30127614e9518b8904b45c83724d62d0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b081](structflash__ra__cf__block__map.md#a30127614e9518b8904b45c83724d62d0): 1;

[ 103](structflash__ra__cf__block__map.md#a3f8ec64524f4639678eaeff0154d5949) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b082](structflash__ra__cf__block__map.md#a3f8ec64524f4639678eaeff0154d5949): 1;

[ 104](structflash__ra__cf__block__map.md#a22cac6f8d6ba2a3f52d0b0e99940bac7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b083](structflash__ra__cf__block__map.md#a22cac6f8d6ba2a3f52d0b0e99940bac7): 1;

[ 105](structflash__ra__cf__block__map.md#a86c57f04b3e0ed408cafdfa30c99ec1d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b084](structflash__ra__cf__block__map.md#a86c57f04b3e0ed408cafdfa30c99ec1d): 1;

[ 106](structflash__ra__cf__block__map.md#a82c55914a45ca14872d5fbc3d9a287f6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b085](structflash__ra__cf__block__map.md#a82c55914a45ca14872d5fbc3d9a287f6): 1;

[ 107](structflash__ra__cf__block__map.md#a18b552766e446ab6b626d17323249af8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b086](structflash__ra__cf__block__map.md#a18b552766e446ab6b626d17323249af8): 1;

[ 108](structflash__ra__cf__block__map.md#af1b0588b223374b4cb3ce3a5c28a5e01) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b087](structflash__ra__cf__block__map.md#af1b0588b223374b4cb3ce3a5c28a5e01): 1;

[ 109](structflash__ra__cf__block__map.md#afda4683b4cd8848dff0c45a3de10bf37) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b088](structflash__ra__cf__block__map.md#afda4683b4cd8848dff0c45a3de10bf37): 1;

[ 110](structflash__ra__cf__block__map.md#a820f214df5c798162a486e807ee016d2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b089](structflash__ra__cf__block__map.md#a820f214df5c798162a486e807ee016d2): 1;

[ 111](structflash__ra__cf__block__map.md#a09ec9fa84702dd8e5e4af8d05bcc3f7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b090](structflash__ra__cf__block__map.md#a09ec9fa84702dd8e5e4af8d05bcc3f7c): 1;

[ 112](structflash__ra__cf__block__map.md#a7549a67515bf980dca171a6231caf53d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b091](structflash__ra__cf__block__map.md#a7549a67515bf980dca171a6231caf53d): 1;

[ 113](structflash__ra__cf__block__map.md#acab46bd7cab0c24fe441eaa2cbcbba16) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b092](structflash__ra__cf__block__map.md#acab46bd7cab0c24fe441eaa2cbcbba16): 1;

[ 114](structflash__ra__cf__block__map.md#a4a3d690ba13a80b9e30c51216c299a8d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b093](structflash__ra__cf__block__map.md#a4a3d690ba13a80b9e30c51216c299a8d): 1;

[ 115](structflash__ra__cf__block__map.md#a8a3c150461c95c4fc98131b6cdcf3ee0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b094](structflash__ra__cf__block__map.md#a8a3c150461c95c4fc98131b6cdcf3ee0): 1;

[ 116](structflash__ra__cf__block__map.md#a9d9b2d3c78decfe2a529c58424d2d2e9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b095](structflash__ra__cf__block__map.md#a9d9b2d3c78decfe2a529c58424d2d2e9): 1;

[ 117](structflash__ra__cf__block__map.md#add7bbdf8d9c3a0d91aabad9c166b60a4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b096](structflash__ra__cf__block__map.md#add7bbdf8d9c3a0d91aabad9c166b60a4): 1;

[ 118](structflash__ra__cf__block__map.md#a27aa6e2dbc549227dcff32cfc33f357f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b097](structflash__ra__cf__block__map.md#a27aa6e2dbc549227dcff32cfc33f357f): 1;

[ 119](structflash__ra__cf__block__map.md#af4cc1e04ace8aed70371ea4bd5ee7ab6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b098](structflash__ra__cf__block__map.md#af4cc1e04ace8aed70371ea4bd5ee7ab6): 1;

[ 120](structflash__ra__cf__block__map.md#afa848d20fede294bc05bb5736a8a9a45) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b099](structflash__ra__cf__block__map.md#afa848d20fede294bc05bb5736a8a9a45): 1;

[ 121](structflash__ra__cf__block__map.md#a2e462fd2de0697b9c7e8e82a99976d7d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b100](structflash__ra__cf__block__map.md#a2e462fd2de0697b9c7e8e82a99976d7d): 1;

[ 122](structflash__ra__cf__block__map.md#a6300ccbb6f0c4ddcd43ca1230756a906) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b101](structflash__ra__cf__block__map.md#a6300ccbb6f0c4ddcd43ca1230756a906): 1;

[ 123](structflash__ra__cf__block__map.md#abfcb1a394afba0f928a752514b53bf16) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b102](structflash__ra__cf__block__map.md#abfcb1a394afba0f928a752514b53bf16): 1;

[ 124](structflash__ra__cf__block__map.md#a8928be6391ad42b1f7488543a3317aa8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b103](structflash__ra__cf__block__map.md#a8928be6391ad42b1f7488543a3317aa8): 1;

[ 125](structflash__ra__cf__block__map.md#aa022976dea15d2bca3f7f727e0df36f7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b104](structflash__ra__cf__block__map.md#aa022976dea15d2bca3f7f727e0df36f7): 1;

[ 126](structflash__ra__cf__block__map.md#acbbaa4a46afcda697e81ed25cc54355c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b105](structflash__ra__cf__block__map.md#acbbaa4a46afcda697e81ed25cc54355c): 1;

[ 127](structflash__ra__cf__block__map.md#a091d60cb37a43b839d00fd58f0530e8a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b106](structflash__ra__cf__block__map.md#a091d60cb37a43b839d00fd58f0530e8a): 1;

128 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f): 21;

[ 129](structflash__ra__cf__block__map.md#a837aec4b3c8eb75201f9f0569aa0c7b5) } BPS\_b;

130 };

131} [flash\_ra\_cf\_block\_map](structflash__ra__cf__block__map.md);

132

133#if defined(CONFIG\_FLASH\_RA\_WRITE\_PROTECT)

134typedef struct flash\_ra\_ex\_write\_protect\_in {

135 flash\_ra\_cf\_block\_map protect\_enable;

136 flash\_ra\_cf\_block\_map protect\_disable;

137 flash\_ra\_cf\_block\_map protect\_permanent;

138} flash\_ra\_ex\_write\_protect\_in\_t;

139

140typedef struct flash\_ra\_ex\_write\_protect\_out {

141 flash\_ra\_cf\_block\_map protected\_enabled;

142 flash\_ra\_cf\_block\_map protected\_premanent;

143} flash\_ra\_ex\_write\_protect\_out\_t;

144#endif /\* CONFIG\_FLASH\_RA\_WRITE\_PROTECT \*/

145

146#endif

[flash.h](flash_8h.md)

Public API for FLASH drivers.

[FLASH\_EX\_OP\_VENDOR\_BASE](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3)

#define FLASH\_EX\_OP\_VENDOR\_BASE

**Definition** flash.h:630

[ra\_ex\_ops](ra__flash__api__extensions_8h.md#a00ad044f5928882300e87ff9a13c1f74)

ra\_ex\_ops

**Definition** ra\_flash\_api\_extensions.h:12

[FLASH\_RA\_EX\_OP\_WRITE\_PROTECT](ra__flash__api__extensions_8h.md#a00ad044f5928882300e87ff9a13c1f74a4404f66075376689dc4670d556f31f48)

@ FLASH\_RA\_EX\_OP\_WRITE\_PROTECT

**Definition** ra\_flash\_api\_extensions.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[flash\_ra\_cf\_block\_map](structflash__ra__cf__block__map.md)

**Definition** ra\_flash\_api\_extensions.h:16

[flash\_ra\_cf\_block\_map::b012](structflash__ra__cf__block__map.md#a0252324460746c1e7ee79fccd50c23bd)

uint32\_t b012

**Definition** ra\_flash\_api\_extensions.h:33

[flash\_ra\_cf\_block\_map::b106](structflash__ra__cf__block__map.md#a091d60cb37a43b839d00fd58f0530e8a)

uint32\_t b106

**Definition** ra\_flash\_api\_extensions.h:127

[flash\_ra\_cf\_block\_map::b036](structflash__ra__cf__block__map.md#a0965d4c1ce6ad9b15c992cbee7e43581)

uint32\_t b036

**Definition** ra\_flash\_api\_extensions.h:57

[flash\_ra\_cf\_block\_map::b090](structflash__ra__cf__block__map.md#a09ec9fa84702dd8e5e4af8d05bcc3f7c)

uint32\_t b090

**Definition** ra\_flash\_api\_extensions.h:111

[flash\_ra\_cf\_block\_map::b031](structflash__ra__cf__block__map.md#a0a75ae0c1580b20370edf626b7089e96)

uint32\_t b031

**Definition** ra\_flash\_api\_extensions.h:52

[flash\_ra\_cf\_block\_map::b010](structflash__ra__cf__block__map.md#a0c44c3265eaeeafdc3d99cb6cc75c181)

uint32\_t b010

**Definition** ra\_flash\_api\_extensions.h:31

[flash\_ra\_cf\_block\_map::b062](structflash__ra__cf__block__map.md#a0e2874f723fe0f08ad3fb124d87537a5)

uint32\_t b062

**Definition** ra\_flash\_api\_extensions.h:83

[flash\_ra\_cf\_block\_map::BPS](structflash__ra__cf__block__map.md#a101c65bd2aec6ca07fa625939614673c)

uint32\_t BPS[4]

**Definition** ra\_flash\_api\_extensions.h:18

[flash\_ra\_cf\_block\_map::b066](structflash__ra__cf__block__map.md#a1163f8a0a4a3112aa1985a283e17ecfc)

uint32\_t b066

**Definition** ra\_flash\_api\_extensions.h:87

[flash\_ra\_cf\_block\_map::b057](structflash__ra__cf__block__map.md#a1457c2d9117a476800a494565c49be5b)

uint32\_t b057

**Definition** ra\_flash\_api\_extensions.h:78

[flash\_ra\_cf\_block\_map::b086](structflash__ra__cf__block__map.md#a18b552766e446ab6b626d17323249af8)

uint32\_t b086

**Definition** ra\_flash\_api\_extensions.h:107

[flash\_ra\_cf\_block\_map::b037](structflash__ra__cf__block__map.md#a193d2edbca49b718ea376ecf505ceed1)

uint32\_t b037

**Definition** ra\_flash\_api\_extensions.h:58

[flash\_ra\_cf\_block\_map::b070](structflash__ra__cf__block__map.md#a19b70fe75c0bc35233f81137d2b1b9de)

uint32\_t b070

**Definition** ra\_flash\_api\_extensions.h:91

[flash\_ra\_cf\_block\_map::b079](structflash__ra__cf__block__map.md#a1cb41bd08cf5405b442df75bc5b99cbc)

uint32\_t b079

**Definition** ra\_flash\_api\_extensions.h:100

[flash\_ra\_cf\_block\_map::b009](structflash__ra__cf__block__map.md#a1e30edab982ea030c12fd6769c609dae)

uint32\_t b009

**Definition** ra\_flash\_api\_extensions.h:30

[flash\_ra\_cf\_block\_map::b019](structflash__ra__cf__block__map.md#a22a077382154519b867a7f2e74935111)

uint32\_t b019

**Definition** ra\_flash\_api\_extensions.h:40

[flash\_ra\_cf\_block\_map::b083](structflash__ra__cf__block__map.md#a22cac6f8d6ba2a3f52d0b0e99940bac7)

uint32\_t b083

**Definition** ra\_flash\_api\_extensions.h:104

[flash\_ra\_cf\_block\_map::b005](structflash__ra__cf__block__map.md#a2389957ae22cfcd8ba7a04c71e56a598)

uint32\_t b005

**Definition** ra\_flash\_api\_extensions.h:26

[flash\_ra\_cf\_block\_map::b060](structflash__ra__cf__block__map.md#a262a98868ffe43c200502fa2320690a7)

uint32\_t b060

**Definition** ra\_flash\_api\_extensions.h:81

[flash\_ra\_cf\_block\_map::b097](structflash__ra__cf__block__map.md#a27aa6e2dbc549227dcff32cfc33f357f)

uint32\_t b097

**Definition** ra\_flash\_api\_extensions.h:118

[flash\_ra\_cf\_block\_map::b100](structflash__ra__cf__block__map.md#a2e462fd2de0697b9c7e8e82a99976d7d)

uint32\_t b100

**Definition** ra\_flash\_api\_extensions.h:121

[flash\_ra\_cf\_block\_map::b081](structflash__ra__cf__block__map.md#a30127614e9518b8904b45c83724d62d0)

uint32\_t b081

**Definition** ra\_flash\_api\_extensions.h:102

[flash\_ra\_cf\_block\_map::b039](structflash__ra__cf__block__map.md#a3680fae5d1a4c9c3b48fc882b12067ae)

uint32\_t b039

**Definition** ra\_flash\_api\_extensions.h:60

[flash\_ra\_cf\_block\_map::b029](structflash__ra__cf__block__map.md#a378ded6128b4a0c46b621d2a20d41785)

uint32\_t b029

**Definition** ra\_flash\_api\_extensions.h:50

[flash\_ra\_cf\_block\_map::b008](structflash__ra__cf__block__map.md#a395cecde2aede749366cf98d77671f20)

uint32\_t b008

**Definition** ra\_flash\_api\_extensions.h:29

[flash\_ra\_cf\_block\_map::b030](structflash__ra__cf__block__map.md#a3aff2f55fa9746c65fab3d8fa73f8f28)

uint32\_t b030

**Definition** ra\_flash\_api\_extensions.h:51

[flash\_ra\_cf\_block\_map::b051](structflash__ra__cf__block__map.md#a3d7f074c57806c9ea231f1833952dfa5)

uint32\_t b051

**Definition** ra\_flash\_api\_extensions.h:72

[flash\_ra\_cf\_block\_map::b063](structflash__ra__cf__block__map.md#a3ee5d4cded42a95d20af476cd0f1d11b)

uint32\_t b063

**Definition** ra\_flash\_api\_extensions.h:84

[flash\_ra\_cf\_block\_map::b082](structflash__ra__cf__block__map.md#a3f8ec64524f4639678eaeff0154d5949)

uint32\_t b082

**Definition** ra\_flash\_api\_extensions.h:103

[flash\_ra\_cf\_block\_map::b016](structflash__ra__cf__block__map.md#a41ce7c7853f6c5f2eb216e5ec376233a)

uint32\_t b016

**Definition** ra\_flash\_api\_extensions.h:37

[flash\_ra\_cf\_block\_map::b052](structflash__ra__cf__block__map.md#a441a9092824122b640aebd23bf375455)

uint32\_t b052

**Definition** ra\_flash\_api\_extensions.h:73

[flash\_ra\_cf\_block\_map::b076](structflash__ra__cf__block__map.md#a4437ed4c525685b80967bbec8ed8a9be)

uint32\_t b076

**Definition** ra\_flash\_api\_extensions.h:97

[flash\_ra\_cf\_block\_map::b003](structflash__ra__cf__block__map.md#a476ade06264c7d8748589684e8d659d7)

uint32\_t b003

**Definition** ra\_flash\_api\_extensions.h:24

[flash\_ra\_cf\_block\_map::b007](structflash__ra__cf__block__map.md#a4913252756d3c3603adfb53ecfd4ca30)

uint32\_t b007

**Definition** ra\_flash\_api\_extensions.h:28

[flash\_ra\_cf\_block\_map::b093](structflash__ra__cf__block__map.md#a4a3d690ba13a80b9e30c51216c299a8d)

uint32\_t b093

**Definition** ra\_flash\_api\_extensions.h:114

[flash\_ra\_cf\_block\_map::b025](structflash__ra__cf__block__map.md#a4b3257ad9cb7aff11c96b1be8e93b938)

uint32\_t b025

**Definition** ra\_flash\_api\_extensions.h:46

[flash\_ra\_cf\_block\_map::b080](structflash__ra__cf__block__map.md#a54a1fe008cb4455da6e9cc196e53b173)

uint32\_t b080

**Definition** ra\_flash\_api\_extensions.h:101

[flash\_ra\_cf\_block\_map::b033](structflash__ra__cf__block__map.md#a561164667e632832f3f36d2dfc99194e)

uint32\_t b033

**Definition** ra\_flash\_api\_extensions.h:54

[flash\_ra\_cf\_block\_map::b101](structflash__ra__cf__block__map.md#a6300ccbb6f0c4ddcd43ca1230756a906)

uint32\_t b101

**Definition** ra\_flash\_api\_extensions.h:122

[flash\_ra\_cf\_block\_map::b065](structflash__ra__cf__block__map.md#a650eeff10b6f8fb39781b135c76e3719)

uint32\_t b065

**Definition** ra\_flash\_api\_extensions.h:86

[flash\_ra\_cf\_block\_map::b064](structflash__ra__cf__block__map.md#a6804c794d52c12112b422887751b0505)

uint32\_t b064

**Definition** ra\_flash\_api\_extensions.h:85

[flash\_ra\_cf\_block\_map::b032](structflash__ra__cf__block__map.md#a6a1c1afb76b55f9ca7c8ca8921aeab94)

uint32\_t b032

**Definition** ra\_flash\_api\_extensions.h:53

[flash\_ra\_cf\_block\_map::b017](structflash__ra__cf__block__map.md#a6e5eae2dccd25da5d5f810a28c13febc)

uint32\_t b017

**Definition** ra\_flash\_api\_extensions.h:38

[flash\_ra\_cf\_block\_map::b044](structflash__ra__cf__block__map.md#a720b5de073fa683ccd37080a1cec2cbf)

uint32\_t b044

**Definition** ra\_flash\_api\_extensions.h:65

[flash\_ra\_cf\_block\_map::b026](structflash__ra__cf__block__map.md#a7267903aef20133fcc65fe13adaf9dce)

uint32\_t b026

**Definition** ra\_flash\_api\_extensions.h:47

[flash\_ra\_cf\_block\_map::b091](structflash__ra__cf__block__map.md#a7549a67515bf980dca171a6231caf53d)

uint32\_t b091

**Definition** ra\_flash\_api\_extensions.h:112

[flash\_ra\_cf\_block\_map::b014](structflash__ra__cf__block__map.md#a77cb77c43ff3a75b655f912f352e74af)

uint32\_t b014

**Definition** ra\_flash\_api\_extensions.h:35

[flash\_ra\_cf\_block\_map::b042](structflash__ra__cf__block__map.md#a78b1ad51fe8dbc438fd099195a6ea986)

uint32\_t b042

**Definition** ra\_flash\_api\_extensions.h:63

[flash\_ra\_cf\_block\_map::b043](structflash__ra__cf__block__map.md#a80697ee52d28c583896d5c7ed5d488f5)

uint32\_t b043

**Definition** ra\_flash\_api\_extensions.h:64

[flash\_ra\_cf\_block\_map::b089](structflash__ra__cf__block__map.md#a820f214df5c798162a486e807ee016d2)

uint32\_t b089

**Definition** ra\_flash\_api\_extensions.h:110

[flash\_ra\_cf\_block\_map::b085](structflash__ra__cf__block__map.md#a82c55914a45ca14872d5fbc3d9a287f6)

uint32\_t b085

**Definition** ra\_flash\_api\_extensions.h:106

[flash\_ra\_cf\_block\_map::b023](structflash__ra__cf__block__map.md#a864feb35216f5a0d287a3e995f60c46a)

uint32\_t b023

**Definition** ra\_flash\_api\_extensions.h:44

[flash\_ra\_cf\_block\_map::b084](structflash__ra__cf__block__map.md#a86c57f04b3e0ed408cafdfa30c99ec1d)

uint32\_t b084

**Definition** ra\_flash\_api\_extensions.h:105

[flash\_ra\_cf\_block\_map::b103](structflash__ra__cf__block__map.md#a8928be6391ad42b1f7488543a3317aa8)

uint32\_t b103

**Definition** ra\_flash\_api\_extensions.h:124

[flash\_ra\_cf\_block\_map::b048](structflash__ra__cf__block__map.md#a89d41c4ed781723ddf46f82d96388171)

uint32\_t b048

**Definition** ra\_flash\_api\_extensions.h:69

[flash\_ra\_cf\_block\_map::b094](structflash__ra__cf__block__map.md#a8a3c150461c95c4fc98131b6cdcf3ee0)

uint32\_t b094

**Definition** ra\_flash\_api\_extensions.h:115

[flash\_ra\_cf\_block\_map::b077](structflash__ra__cf__block__map.md#a8a6a13d75573a6e30a1e5f2f4c923723)

uint32\_t b077

**Definition** ra\_flash\_api\_extensions.h:98

[flash\_ra\_cf\_block\_map::b011](structflash__ra__cf__block__map.md#a8b50ba68eb37b6efc2c0965144a57a1b)

uint32\_t b011

**Definition** ra\_flash\_api\_extensions.h:32

[flash\_ra\_cf\_block\_map::b045](structflash__ra__cf__block__map.md#a8d3fa1d37b1aa526ded7d470e9af55dd)

uint32\_t b045

**Definition** ra\_flash\_api\_extensions.h:66

[flash\_ra\_cf\_block\_map::b055](structflash__ra__cf__block__map.md#a8d5882d109314f72e9168a53a95f88b7)

uint32\_t b055

**Definition** ra\_flash\_api\_extensions.h:76

[flash\_ra\_cf\_block\_map::b015](structflash__ra__cf__block__map.md#a94c9bfc6b185bb9f6dfc12f85bf92ccd)

uint32\_t b015

**Definition** ra\_flash\_api\_extensions.h:36

[flash\_ra\_cf\_block\_map::b068](structflash__ra__cf__block__map.md#a9982c0ede4ff499f29bc31c07fb2e4e0)

uint32\_t b068

**Definition** ra\_flash\_api\_extensions.h:89

[flash\_ra\_cf\_block\_map::b027](structflash__ra__cf__block__map.md#a9a004f814ecc9295d0bfb6a058603a4d)

uint32\_t b027

**Definition** ra\_flash\_api\_extensions.h:48

[flash\_ra\_cf\_block\_map::b049](structflash__ra__cf__block__map.md#a9bc8e17cf5e726e3f4c6f447feb8b6cc)

uint32\_t b049

**Definition** ra\_flash\_api\_extensions.h:70

[flash\_ra\_cf\_block\_map::b095](structflash__ra__cf__block__map.md#a9d9b2d3c78decfe2a529c58424d2d2e9)

uint32\_t b095

**Definition** ra\_flash\_api\_extensions.h:116

[flash\_ra\_cf\_block\_map::b104](structflash__ra__cf__block__map.md#aa022976dea15d2bca3f7f727e0df36f7)

uint32\_t b104

**Definition** ra\_flash\_api\_extensions.h:125

[flash\_ra\_cf\_block\_map::b046](structflash__ra__cf__block__map.md#aa149c469d2afab259d0b8713901dbdc1)

uint32\_t b046

**Definition** ra\_flash\_api\_extensions.h:67

[flash\_ra\_cf\_block\_map::b078](structflash__ra__cf__block__map.md#aa8b5ecbd829ac2eb63a467c388a25bfd)

uint32\_t b078

**Definition** ra\_flash\_api\_extensions.h:99

[flash\_ra\_cf\_block\_map::b000](structflash__ra__cf__block__map.md#aab665bbc1e9ff1a7daa74acb6dc191c0)

uint32\_t b000

**Definition** ra\_flash\_api\_extensions.h:21

[flash\_ra\_cf\_block\_map::b075](structflash__ra__cf__block__map.md#aac819746680655ef6badfcb7153a541c)

uint32\_t b075

**Definition** ra\_flash\_api\_extensions.h:96

[flash\_ra\_cf\_block\_map::b074](structflash__ra__cf__block__map.md#abcbb9236f45d28a4c00b65f2a836b506)

uint32\_t b074

**Definition** ra\_flash\_api\_extensions.h:95

[flash\_ra\_cf\_block\_map::b102](structflash__ra__cf__block__map.md#abfcb1a394afba0f928a752514b53bf16)

uint32\_t b102

**Definition** ra\_flash\_api\_extensions.h:123

[flash\_ra\_cf\_block\_map::b001](structflash__ra__cf__block__map.md#ac0a4b33efd9c4bf4ddf705000a566830)

uint32\_t b001

**Definition** ra\_flash\_api\_extensions.h:22

[flash\_ra\_cf\_block\_map::b034](structflash__ra__cf__block__map.md#ac6f2969063187429f296f00ddee15dc5)

uint32\_t b034

**Definition** ra\_flash\_api\_extensions.h:55

[flash\_ra\_cf\_block\_map::b092](structflash__ra__cf__block__map.md#acab46bd7cab0c24fe441eaa2cbcbba16)

uint32\_t b092

**Definition** ra\_flash\_api\_extensions.h:113

[flash\_ra\_cf\_block\_map::b024](structflash__ra__cf__block__map.md#acb026914242bd25ab7aeb38f63251a91)

uint32\_t b024

**Definition** ra\_flash\_api\_extensions.h:45

[flash\_ra\_cf\_block\_map::b105](structflash__ra__cf__block__map.md#acbbaa4a46afcda697e81ed25cc54355c)

uint32\_t b105

**Definition** ra\_flash\_api\_extensions.h:126

[flash\_ra\_cf\_block\_map::b006](structflash__ra__cf__block__map.md#acbe4d9e8b4a28d61c340d3bc6ef3b58f)

uint32\_t b006

**Definition** ra\_flash\_api\_extensions.h:27

[flash\_ra\_cf\_block\_map::b072](structflash__ra__cf__block__map.md#acd5d3b551788b54c057ff12a94e00298)

uint32\_t b072

**Definition** ra\_flash\_api\_extensions.h:93

[flash\_ra\_cf\_block\_map::b071](structflash__ra__cf__block__map.md#ace79cf904d9e7cade53b69a9bb399b20)

uint32\_t b071

**Definition** ra\_flash\_api\_extensions.h:92

[flash\_ra\_cf\_block\_map::b059](structflash__ra__cf__block__map.md#acea3a50b7663d7a1a7ae32df8edb543b)

uint32\_t b059

**Definition** ra\_flash\_api\_extensions.h:80

[flash\_ra\_cf\_block\_map::b028](structflash__ra__cf__block__map.md#acf7e1c4c60cc9a55608450038c60076e)

uint32\_t b028

**Definition** ra\_flash\_api\_extensions.h:49

[flash\_ra\_cf\_block\_map::b035](structflash__ra__cf__block__map.md#ad28df448a10e65c4d45f0591df45863f)

uint32\_t b035

**Definition** ra\_flash\_api\_extensions.h:56

[flash\_ra\_cf\_block\_map::b004](structflash__ra__cf__block__map.md#ad2fd670a9fc1cb21fc2b7ec05ffd1190)

uint32\_t b004

**Definition** ra\_flash\_api\_extensions.h:25

[flash\_ra\_cf\_block\_map::b061](structflash__ra__cf__block__map.md#ad5d6e34e3f8988b44f5a83b975371495)

uint32\_t b061

**Definition** ra\_flash\_api\_extensions.h:82

[flash\_ra\_cf\_block\_map::b050](structflash__ra__cf__block__map.md#adaaf903d2d26f8420af85870427cc077)

uint32\_t b050

**Definition** ra\_flash\_api\_extensions.h:71

[flash\_ra\_cf\_block\_map::b054](structflash__ra__cf__block__map.md#adb0d60c86cdd968016693847a76b7fcf)

uint32\_t b054

**Definition** ra\_flash\_api\_extensions.h:75

[flash\_ra\_cf\_block\_map::b096](structflash__ra__cf__block__map.md#add7bbdf8d9c3a0d91aabad9c166b60a4)

uint32\_t b096

**Definition** ra\_flash\_api\_extensions.h:117

[flash\_ra\_cf\_block\_map::b020](structflash__ra__cf__block__map.md#ae0610211a298f68244d3c7e8eeda324f)

uint32\_t b020

**Definition** ra\_flash\_api\_extensions.h:41

[flash\_ra\_cf\_block\_map::b053](structflash__ra__cf__block__map.md#ae4a6353ea5ea3782717b64d244ab0f6d)

uint32\_t b053

**Definition** ra\_flash\_api\_extensions.h:74

[flash\_ra\_cf\_block\_map::b013](structflash__ra__cf__block__map.md#ae53254d344fec51cde3de9daff5fee7e)

uint32\_t b013

**Definition** ra\_flash\_api\_extensions.h:34

[flash\_ra\_cf\_block\_map::b040](structflash__ra__cf__block__map.md#ae662e4d2c2e5adac1c19fb0298c7b4ad)

uint32\_t b040

**Definition** ra\_flash\_api\_extensions.h:61

[flash\_ra\_cf\_block\_map::b047](structflash__ra__cf__block__map.md#ae664ecf070f0ebca55d12cacd75cc175)

uint32\_t b047

**Definition** ra\_flash\_api\_extensions.h:68

[flash\_ra\_cf\_block\_map::b073](structflash__ra__cf__block__map.md#ae90d8579cecfc5b4dca41146ba24fe12)

uint32\_t b073

**Definition** ra\_flash\_api\_extensions.h:94

[flash\_ra\_cf\_block\_map::b067](structflash__ra__cf__block__map.md#aeb4dea7898da9f5cbc0e645a140fb83e)

uint32\_t b067

**Definition** ra\_flash\_api\_extensions.h:88

[flash\_ra\_cf\_block\_map::b058](structflash__ra__cf__block__map.md#aec302f0382977f82a89f8b9f03c00c43)

uint32\_t b058

**Definition** ra\_flash\_api\_extensions.h:79

[flash\_ra\_cf\_block\_map::b038](structflash__ra__cf__block__map.md#aecbdc2ba15bfe55a890c52ac45b09fdd)

uint32\_t b038

**Definition** ra\_flash\_api\_extensions.h:59

[flash\_ra\_cf\_block\_map::b087](structflash__ra__cf__block__map.md#af1b0588b223374b4cb3ce3a5c28a5e01)

uint32\_t b087

**Definition** ra\_flash\_api\_extensions.h:108

[flash\_ra\_cf\_block\_map::b021](structflash__ra__cf__block__map.md#af3167f6678a3b7ebf19a9b51318fabef)

uint32\_t b021

**Definition** ra\_flash\_api\_extensions.h:42

[flash\_ra\_cf\_block\_map::b018](structflash__ra__cf__block__map.md#af3723aa40307c3394e5892c6fc7c449f)

uint32\_t b018

**Definition** ra\_flash\_api\_extensions.h:39

[flash\_ra\_cf\_block\_map::b069](structflash__ra__cf__block__map.md#af4139fb3c97a934b2d852bb789ecc7cb)

uint32\_t b069

**Definition** ra\_flash\_api\_extensions.h:90

[flash\_ra\_cf\_block\_map::b022](structflash__ra__cf__block__map.md#af4ac762cc131c66834186c20276ee0bc)

uint32\_t b022

**Definition** ra\_flash\_api\_extensions.h:43

[flash\_ra\_cf\_block\_map::b098](structflash__ra__cf__block__map.md#af4cc1e04ace8aed70371ea4bd5ee7ab6)

uint32\_t b098

**Definition** ra\_flash\_api\_extensions.h:119

[flash\_ra\_cf\_block\_map::b099](structflash__ra__cf__block__map.md#afa848d20fede294bc05bb5736a8a9a45)

uint32\_t b099

**Definition** ra\_flash\_api\_extensions.h:120

[flash\_ra\_cf\_block\_map::b088](structflash__ra__cf__block__map.md#afda4683b4cd8848dff0c45a3de10bf37)

uint32\_t b088

**Definition** ra\_flash\_api\_extensions.h:109

[flash\_ra\_cf\_block\_map::b056](structflash__ra__cf__block__map.md#afe45733316726992bcfebb604da5fee1)

uint32\_t b056

**Definition** ra\_flash\_api\_extensions.h:77

[flash\_ra\_cf\_block\_map::b041](structflash__ra__cf__block__map.md#aff3eca7d27b10df6affe86af33d21e0a)

uint32\_t b041

**Definition** ra\_flash\_api\_extensions.h:62

[flash\_ra\_cf\_block\_map::b002](structflash__ra__cf__block__map.md#aff993abeb30ea8d8054f96b41100af2b)

uint32\_t b002

**Definition** ra\_flash\_api\_extensions.h:23

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash](dir_b5b0d43e6264d65db716db62f9858e50.md)
- [ra\_flash\_api\_extensions.h](ra__flash__api__extensions_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
