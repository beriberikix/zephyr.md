---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/modem_2ubx_2protocol_8h_source.html
original_path: doxygen/html/modem_2ubx_2protocol_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

protocol.h

[Go to the documentation of this file.](modem_2ubx_2protocol_8h.md)

1/\*

2 \* Copyright (c) 2025 Croxel Inc.

3 \* Copyright (c) 2025 CogniPilot Foundation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_MODEM\_UBX\_PROTOCOL\_

9#define ZEPHYR\_MODEM\_UBX\_PROTOCOL\_

10

11#include <[stdint.h](stdint_8h.md)>

12#include <[zephyr/modem/ubx/checksum.h](checksum_8h.md)>

13

[ 14](modem_2ubx_2protocol_8h.md#a1342f8e944fcd9f45fe94eef9bda307c)#define UBX\_FRAME\_HEADER\_SZ 6

[ 15](modem_2ubx_2protocol_8h.md#aa0392f4a081c1077b4f235a757431aee)#define UBX\_FRAME\_FOOTER\_SZ 2

[ 16](modem_2ubx_2protocol_8h.md#a8e1aded66fd229f071c9d5e060a001a6)#define UBX\_FRAME\_SZ\_WITHOUT\_PAYLOAD (UBX\_FRAME\_HEADER\_SZ + UBX\_FRAME\_FOOTER\_SZ)

[ 17](modem_2ubx_2protocol_8h.md#a4c64b9118da471baa6a7a88ee345bf66)#define UBX\_FRAME\_SZ(payload\_size) (payload\_size + UBX\_FRAME\_SZ\_WITHOUT\_PAYLOAD)

18

[ 19](modem_2ubx_2protocol_8h.md#a1693f3584605a0197076cba71c79b0df)#define UBX\_PREAMBLE\_SYNC\_CHAR\_1 0xB5

[ 20](modem_2ubx_2protocol_8h.md#ad8d6229db563db619d4f0a9f225fb640)#define UBX\_PREAMBLE\_SYNC\_CHAR\_2 0x62

21

[ 22](modem_2ubx_2protocol_8h.md#a1b417ed30e090d3399f96c87dfe842c4)#define UBX\_FRAME\_PREAMBLE\_SYNC\_CHAR\_1\_IDX 0

[ 23](modem_2ubx_2protocol_8h.md#af940bf4cc68adff5b8b187dcf1e93735)#define UBX\_FRAME\_PREAMBLE\_SYNC\_CHAR\_2\_IDX 1

[ 24](modem_2ubx_2protocol_8h.md#a2c667ef9bb2d12effb251f4df6827c73)#define UBX\_FRAME\_MSG\_CLASS\_IDX 2

25

[ 26](modem_2ubx_2protocol_8h.md#a9c66cd27732153c56d0872339bc3deae)#define UBX\_PAYLOAD\_SZ\_MAX 512

[ 27](modem_2ubx_2protocol_8h.md#a1cab11988642144cfcc6c7309f5806d0)#define UBX\_FRAME\_SZ\_MAX UBX\_FRAME\_SZ(UBX\_PAYLOAD\_SZ\_MAX)

28

[ 29](structubx__frame.md)struct [ubx\_frame](structubx__frame.md) {

[ 30](structubx__frame.md#acf80f38e8f26bb32848ae2978a1f87a1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [preamble\_sync\_char\_1](structubx__frame.md#acf80f38e8f26bb32848ae2978a1f87a1);

[ 31](structubx__frame.md#ac61fb72df7c1cd8a9bacb787071cb77d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [preamble\_sync\_char\_2](structubx__frame.md#ac61fb72df7c1cd8a9bacb787071cb77d);

[ 32](structubx__frame.md#a2dcc29a82e7dfff2d1e4194f1bc035e8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) class;

[ 33](structubx__frame.md#a4e578da5900365d498708f7a61d48ba4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structubx__frame.md#a4e578da5900365d498708f7a61d48ba4);

[ 34](structubx__frame.md#a77b5030a6b95aef58b1c17f0368dd7ce) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [payload\_size](structubx__frame.md#a77b5030a6b95aef58b1c17f0368dd7ce);

[ 35](structubx__frame.md#a70c465b5bd1e9837c253d78fb210f4ce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [payload\_and\_checksum](structubx__frame.md#a70c465b5bd1e9837c253d78fb210f4ce)[];

36};

37

[ 38](structubx__frame__match.md)struct [ubx\_frame\_match](structubx__frame__match.md) {

[ 39](structubx__frame__match.md#a40d79aebd93db1349820a7f6bef9c53e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) class;

[ 40](structubx__frame__match.md#ae65eaf921576c61ad758bfedc56d89c6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structubx__frame__match.md#ae65eaf921576c61ad758bfedc56d89c6);

41 struct {

[ 42](structubx__frame__match.md#af78f70c27f4334fd1dcaac72d9e4ece6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structubx__frame__match.md#af78f70c27f4334fd1dcaac72d9e4ece6);

[ 43](structubx__frame__match.md#a36c5fd74bd6d506111b1ef2ac39cb68a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structubx__frame__match.md#a36c5fd74bd6d506111b1ef2ac39cb68a);

[ 44](structubx__frame__match.md#abbc954596995ca2dfe65de3e310e02a0) } [payload](structubx__frame__match.md#abbc954596995ca2dfe65de3e310e02a0);

45};

46

[ 47](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18)enum [ubx\_class\_id](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18) {

[ 48](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a8f46002e33dddab6782bad93ab3fd8b1) [UBX\_CLASS\_ID\_NAV](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a8f46002e33dddab6782bad93ab3fd8b1) = 0x01, /\* Navigation Results Messages \*/

[ 49](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a5e4eaf66a7356e73b4c6e4949160f321) [UBX\_CLASS\_ID\_RXM](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a5e4eaf66a7356e73b4c6e4949160f321) = 0x02, /\* Receiver Manager Messages \*/

[ 50](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a898b493832d06586cf48f9a2545651d0) [UBX\_CLASS\_ID\_INF](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a898b493832d06586cf48f9a2545651d0) = 0x04, /\* Information Messages \*/

[ 51](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18aee43a865c5815ce058261f5f0550fa2b) [UBX\_CLASS\_ID\_ACK](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18aee43a865c5815ce058261f5f0550fa2b) = 0x05, /\* Ack/Nak Messages \*/

[ 52](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c) [UBX\_CLASS\_ID\_CFG](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c) = 0x06, /\* Configuration Input Messages \*/

[ 53](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18aba0a811e14f9e87bd47bfbeaad24e11b) [UBX\_CLASS\_ID\_UPD](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18aba0a811e14f9e87bd47bfbeaad24e11b) = 0x09, /\* Firmware Update Messages \*/

[ 54](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18ac9200dedb25cfa03b80f4336e86db5ed) [UBX\_CLASS\_ID\_MON](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18ac9200dedb25cfa03b80f4336e86db5ed) = 0x0A, /\* Monitoring Messages \*/

[ 55](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a8c700fd2062d8dc51c5e4b28c98c6cf0) [UBX\_CLASS\_ID\_TIM](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a8c700fd2062d8dc51c5e4b28c98c6cf0) = 0x0D, /\* Timing Messages \*/

[ 56](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a418aca13d3bd1608869494d26559e52f) [UBX\_CLASS\_ID\_MGA](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a418aca13d3bd1608869494d26559e52f) = 0x13, /\* Multiple GNSS Assistance Messages \*/

[ 57](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a1e35a224f4809d3a59d0f1570bf382bb) [UBX\_CLASS\_ID\_LOG](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a1e35a224f4809d3a59d0f1570bf382bb) = 0x21, /\* Logging Messages \*/

[ 58](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a760de1a9f06cc6d4832da868d01702c4) [UBX\_CLASS\_ID\_SEC](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a760de1a9f06cc6d4832da868d01702c4) = 0x27, /\* Security Feature Messages \*/

[ 59](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a7e7c3645f46ba3c2e8329ae3a9eeaa79) [UBX\_CLASS\_ID\_NMEA\_STD](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a7e7c3645f46ba3c2e8329ae3a9eeaa79) = 0xF0, /\* Note: Only used to configure message rate \*/

[ 60](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a0d9d5044c9df2a6b61b7a46a4f24e895) [UBX\_CLASS\_ID\_NMEA\_PUBX](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a0d9d5044c9df2a6b61b7a46a4f24e895) = 0xF1, /\* Note: Only used to configure message rate \*/

61};

62

[ 63](modem_2ubx_2protocol_8h.md#a8a935ea7debb4ac73ea99c98d6ef4d3b)enum [ubx\_msg\_id\_nav](modem_2ubx_2protocol_8h.md#a8a935ea7debb4ac73ea99c98d6ef4d3b) {

[ 64](modem_2ubx_2protocol_8h.md#a8a935ea7debb4ac73ea99c98d6ef4d3ba8f887b777e29fc05107ac406d4a87458) [UBX\_MSG\_ID\_NAV\_PVT](modem_2ubx_2protocol_8h.md#a8a935ea7debb4ac73ea99c98d6ef4d3ba8f887b777e29fc05107ac406d4a87458) = 0x07,

[ 65](modem_2ubx_2protocol_8h.md#a8a935ea7debb4ac73ea99c98d6ef4d3bae87d4355340186b8a049346e3076f9ae) [UBX\_MSG\_ID\_NAV\_SAT](modem_2ubx_2protocol_8h.md#a8a935ea7debb4ac73ea99c98d6ef4d3bae87d4355340186b8a049346e3076f9ae) = 0x35,

66};

67

[ 68](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fef)enum [ubx\_nav\_fix\_type](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fef) {

[ 69](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefad351fdc11590580b88ba5b486113e498) [UBX\_NAV\_FIX\_TYPE\_NO\_FIX](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefad351fdc11590580b88ba5b486113e498) = 0,

[ 70](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefae28182c06da19d2b498f92d09d74b33e) [UBX\_NAV\_FIX\_TYPE\_DR](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefae28182c06da19d2b498f92d09d74b33e) = 1,

[ 71](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefae47dad429327e6a0cc89e339729b2651) [UBX\_NAV\_FIX\_TYPE\_2D](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefae47dad429327e6a0cc89e339729b2651) = 2,

[ 72](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefa1f8c2845d6e8e41f62cc28b7f1681f43) [UBX\_NAV\_FIX\_TYPE\_3D](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefa1f8c2845d6e8e41f62cc28b7f1681f43) = 3,

[ 73](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefa648f596240841758588749574998bd71) [UBX\_NAV\_FIX\_TYPE\_GNSS\_DR\_COMBINED](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefa648f596240841758588749574998bd71) = 4,

[ 74](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefa2c20469f6893f651ad14b8ed6a7c3845) [UBX\_NAV\_FIX\_TYPE\_TIME\_ONLY](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefa2c20469f6893f651ad14b8ed6a7c3845) = 5,

75};

76

[ 77](modem_2ubx_2protocol_8h.md#ae9c98287cbaf17e7fc1beaedc1679fa4)#define UBX\_NAV\_PVT\_VALID\_DATE BIT(0)

[ 78](modem_2ubx_2protocol_8h.md#a583269f4c0ea39e43671fd9267b129af)#define UBX\_NAV\_PVT\_VALID\_TIME BIT(1)

[ 79](modem_2ubx_2protocol_8h.md#a4ea40193fa60a75bf5ede5586da92931)#define UBX\_NAV\_PVT\_VALID\_UTC\_TOD BIT(2)

[ 80](modem_2ubx_2protocol_8h.md#a1f067fe87ff51b4b59e7bfce2c4b9880)#define UBX\_NAV\_PVT\_VALID\_MAGN BIT(3)

81

[ 82](modem_2ubx_2protocol_8h.md#af79a6a074065fb7d792109b4d99ba32f)#define UBX\_NAV\_PVT\_FLAGS\_GNSS\_FIX\_OK BIT(0)

83

[ 84](modem_2ubx_2protocol_8h.md#ac348d618c31a5ae7b243243267b041c6)#define UBX\_NAV\_PVT\_FLAGS3\_INVALID\_LLH BIT(0)

85

[ 86](structubx__nav__pvt.md)struct [ubx\_nav\_pvt](structubx__nav__pvt.md) {

87 struct {

[ 88](structubx__nav__pvt.md#a426086b12ff09fb8a00dd4623fea307e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [itow](structubx__nav__pvt.md#a426086b12ff09fb8a00dd4623fea307e);

[ 89](structubx__nav__pvt.md#a84c6640806485f270b8d51d06cc49709) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [year](structubx__nav__pvt.md#a84c6640806485f270b8d51d06cc49709);

[ 90](structubx__nav__pvt.md#ad90042dc5e00b91f004badcb0c3a5f4c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [month](structubx__nav__pvt.md#ad90042dc5e00b91f004badcb0c3a5f4c);

[ 91](structubx__nav__pvt.md#aeadb05fe45a3a0539c899129e40059fd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [day](structubx__nav__pvt.md#aeadb05fe45a3a0539c899129e40059fd);

[ 92](structubx__nav__pvt.md#aeb710663626935d21c77a5cfe1030795) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hour](structubx__nav__pvt.md#aeb710663626935d21c77a5cfe1030795);

[ 93](structubx__nav__pvt.md#a18b61263b433dc5f81c2becff9c6743c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [minute](structubx__nav__pvt.md#a18b61263b433dc5f81c2becff9c6743c);

[ 94](structubx__nav__pvt.md#a10b14934d80d80d3c2f0c36866bd4a64) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [second](structubx__nav__pvt.md#a10b14934d80d80d3c2f0c36866bd4a64);

[ 95](structubx__nav__pvt.md#a450638fda7b9d1929145575e4c576ec1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [valid](structubx__nav__pvt.md#a450638fda7b9d1929145575e4c576ec1);

[ 96](structubx__nav__pvt.md#a1753595f0a3935449dee4d0c57e88a6e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tacc](structubx__nav__pvt.md#a1753595f0a3935449dee4d0c57e88a6e);

[ 97](structubx__nav__pvt.md#a1c21c3b882412f36f96c59cda1d948d9) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [nano](structubx__nav__pvt.md#a1c21c3b882412f36f96c59cda1d948d9);

[ 98](structubx__nav__pvt.md#ad63cfcbcefd262731920954bab9c6758) } \_\_packed [time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067);

[ 99](structubx__nav__pvt.md#a3b780d7b790b07a8ee23431969cbc318) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fix\_type](structubx__nav__pvt.md#a3b780d7b790b07a8ee23431969cbc318);

[ 100](structubx__nav__pvt.md#a1bdc3cb0e4a2b6bef1c4216963e5c29c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structubx__nav__pvt.md#a1bdc3cb0e4a2b6bef1c4216963e5c29c);

[ 101](structubx__nav__pvt.md#a2ff7d8bcc13ee956d9535c61efefada6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags2](structubx__nav__pvt.md#a2ff7d8bcc13ee956d9535c61efefada6);

102 struct {

[ 103](structubx__nav__pvt.md#aea613eb3d604d33120e82c569c5f10e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_sv](structubx__nav__pvt.md#aea613eb3d604d33120e82c569c5f10e9);

[ 104](structubx__nav__pvt.md#ae47fc34dfd91687590bd96afe2fab091) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [longitude](structubx__nav__pvt.md#ae47fc34dfd91687590bd96afe2fab091); /\* Longitude. Degrees. scaling: 1e-7 \*/

[ 105](structubx__nav__pvt.md#a34ec5fc41c4b323b4719803f1ff01bed) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [latitude](structubx__nav__pvt.md#a34ec5fc41c4b323b4719803f1ff01bed); /\* Latitude. Degrees. scaling: 1e-7 \*/

[ 106](structubx__nav__pvt.md#ab0df156e9f8009bebfbbdb39c63c4191) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [height](structubx__nav__pvt.md#ab0df156e9f8009bebfbbdb39c63c4191); /\* Height above ellipsoid. mm \*/

[ 107](structubx__nav__pvt.md#ae6ba97f3406b9fdbbf04c4bb3e744668) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [hmsl](structubx__nav__pvt.md#ae6ba97f3406b9fdbbf04c4bb3e744668); /\* Height above mean sea level. mm \*/

[ 108](structubx__nav__pvt.md#acbb58f36eb572ce27b050a8c7540f91d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [horiz\_acc](structubx__nav__pvt.md#acbb58f36eb572ce27b050a8c7540f91d); /\* Horizontal accuracy estimate. mm \*/

[ 109](structubx__nav__pvt.md#af5b3e0e70b3470bd1686ddbfefb419f9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vert\_acc](structubx__nav__pvt.md#af5b3e0e70b3470bd1686ddbfefb419f9); /\* Vertical accuracy estimate. mm \*/

[ 110](structubx__nav__pvt.md#a1d50e696fa2684b55d04c652c85f2e16) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [vel\_north](structubx__nav__pvt.md#a1d50e696fa2684b55d04c652c85f2e16); /\* NED north velocity. mm/s \*/

[ 111](structubx__nav__pvt.md#a17c628b0acca293f068b58eff32ae4dd) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [vel\_east](structubx__nav__pvt.md#a17c628b0acca293f068b58eff32ae4dd); /\* NED east velocity. mm/s \*/

[ 112](structubx__nav__pvt.md#a4958a6c11bd812477d11467ab3384161) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [vel\_down](structubx__nav__pvt.md#a4958a6c11bd812477d11467ab3384161); /\* NED down velocity. mm/s \*/

[ 113](structubx__nav__pvt.md#a38a8612a53966a1d598bf6d17443da7d) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [ground\_speed](structubx__nav__pvt.md#a38a8612a53966a1d598bf6d17443da7d); /\* Ground Speed (2D). mm/s \*/

[ 114](structubx__nav__pvt.md#abd97f003ba43b70ffea2e9fdf5702c4f) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [head\_motion](structubx__nav__pvt.md#abd97f003ba43b70ffea2e9fdf5702c4f); /\* Heading of Motion (2D). Degrees. scaling: 1e-5 \*/

[ 115](structubx__nav__pvt.md#a955d0f7927f68f540f2e9a2c91e46e79) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [speed\_acc](structubx__nav__pvt.md#a955d0f7927f68f540f2e9a2c91e46e79); /\* Speed accuracy estimated. mm/s \*/

[ 116](structubx__nav__pvt.md#aa332fc93448eb6b30ad8bbaa5760db5c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [head\_acc](structubx__nav__pvt.md#aa332fc93448eb6b30ad8bbaa5760db5c);

[ 119](structubx__nav__pvt.md#a7e5dc3449e52a36cb2bc5841bbf6fec8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pdop](structubx__nav__pvt.md#a7e5dc3449e52a36cb2bc5841bbf6fec8); /\* scaling: 1e-2 \*/

[ 120](structubx__nav__pvt.md#a39b72f654fc8130c611ac839189914ed) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags3](structubx__nav__pvt.md#a39b72f654fc8130c611ac839189914ed);

[ 121](structubx__nav__pvt.md#a80139f6d95bf943f5c6de6af1ea50e3e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved](structubx__nav__pvt.md#a80139f6d95bf943f5c6de6af1ea50e3e);

[ 122](structubx__nav__pvt.md#a8fc4b24fb8ffde02d306bc1b6770b1d8) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [head\_vehicle](structubx__nav__pvt.md#a8fc4b24fb8ffde02d306bc1b6770b1d8); /\* Heading of vehicle (2D). Degrees. Valid if

123 \* flags.head\_vehicle\_valid is set.

124 \*/

[ 125](structubx__nav__pvt.md#a4f63a0f15b823e5258fdb826d2636828) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [mag\_decl](structubx__nav__pvt.md#a4f63a0f15b823e5258fdb826d2636828); /\* Magnetic declination. Degrees. \*/

[ 126](structubx__nav__pvt.md#ac0265c113f01ae2bab8553eb7148e3ae) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [magacc](structubx__nav__pvt.md#ac0265c113f01ae2bab8553eb7148e3ae); /\* Magnetic declination accuracy. Degrees. scaling: 1e-2 \*/

[ 127](structubx__nav__pvt.md#aa8b31a49c2844501505412da226872e1) } \_\_packed [nav](structubx__nav__pvt.md#aa8b31a49c2844501505412da226872e1);

128} \_\_packed;

129

[ 130](modem_2ubx_2protocol_8h.md#afbba8ada09d6c6489d52a3b9dc31725f)enum [ubx\_nav\_sat\_health](modem_2ubx_2protocol_8h.md#afbba8ada09d6c6489d52a3b9dc31725f) {

[ 131](modem_2ubx_2protocol_8h.md#afbba8ada09d6c6489d52a3b9dc31725fa3661b89022659975720d3a022b21f194) [UBX\_NAV\_SAT\_HEALTH\_UNKNOWN](modem_2ubx_2protocol_8h.md#afbba8ada09d6c6489d52a3b9dc31725fa3661b89022659975720d3a022b21f194) = 0,

[ 132](modem_2ubx_2protocol_8h.md#afbba8ada09d6c6489d52a3b9dc31725fa7dcaa32f001d1a7b5b071cdf7621081e) [UBX\_NAV\_SAT\_HEALTH\_HEALTHY](modem_2ubx_2protocol_8h.md#afbba8ada09d6c6489d52a3b9dc31725fa7dcaa32f001d1a7b5b071cdf7621081e) = 1,

[ 133](modem_2ubx_2protocol_8h.md#afbba8ada09d6c6489d52a3b9dc31725fa95ea7c01a987a1e334f41c79642b8139) [UBX\_NAV\_SAT\_HEALTH\_UNHEALTHY](modem_2ubx_2protocol_8h.md#afbba8ada09d6c6489d52a3b9dc31725fa95ea7c01a987a1e334f41c79642b8139) = 2,

134};

135

[ 136](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690)enum [ubx\_gnss\_id](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690) {

[ 137](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690adca8434b24978430d03939b81d76fbb9) [UBX\_GNSS\_ID\_GPS](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690adca8434b24978430d03939b81d76fbb9) = 0,

[ 138](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690a31a403a2013dc9da3da56366fa95f19b) [UBX\_GNSS\_ID\_SBAS](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690a31a403a2013dc9da3da56366fa95f19b) = 1,

[ 139](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690a931ed807a91dd1f0e6e2cfa013860cbe) [UBX\_GNSS\_ID\_GALILEO](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690a931ed807a91dd1f0e6e2cfa013860cbe) = 2,

[ 140](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690ac3f1631647cfd0246be61fc78549a9f7) [UBX\_GNSS\_ID\_BEIDOU](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690ac3f1631647cfd0246be61fc78549a9f7) = 3,

[ 141](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690a2dad67829bb51786024771c0d5a6d103) [UBX\_GNSS\_ID\_QZSS](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690a2dad67829bb51786024771c0d5a6d103) = 5,

[ 142](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690a4e14cf64a03e9d37af198870b0616497) [UBX\_GNSS\_ID\_GLONASS](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690a4e14cf64a03e9d37af198870b0616497) = 6,

143};

144

[ 145](modem_2ubx_2protocol_8h.md#aaaa4b2e1968a45f4c7ee336a45b4164b)#define UBX\_NAV\_SAT\_FLAGS\_SV\_USED BIT(3)

146

[ 147](structubx__nav__sat.md)struct [ubx\_nav\_sat](structubx__nav__sat.md) {

[ 148](structubx__nav__sat.md#aac587fd77fa832021ebca87e7897eb2e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [itow](structubx__nav__sat.md#aac587fd77fa832021ebca87e7897eb2e);

[ 149](structubx__nav__sat.md#a7204f8b1b28f3dc0970fa62567885cdc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [version](structubx__nav__sat.md#a7204f8b1b28f3dc0970fa62567885cdc); /\* Message version. \*/

[ 150](structubx__nav__sat.md#ae0bea798d815cc25e837e3fa394fb429) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_sv](structubx__nav__sat.md#ae0bea798d815cc25e837e3fa394fb429);

[ 151](structubx__nav__sat.md#a6f5bf3da0f5633aa95ff4d736656cb21) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved1](structubx__nav__sat.md#a6f5bf3da0f5633aa95ff4d736656cb21);

[ 152](structubx__nav__sat_1_1ubx__nav__sat__info.md) struct [ubx\_nav\_sat\_info](structubx__nav__sat_1_1ubx__nav__sat__info.md) {

[ 153](structubx__nav__sat_1_1ubx__nav__sat__info.md#a04fc29e6cf9f1ff6f1f638ae633d5a11) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gnss\_id](structubx__nav__sat_1_1ubx__nav__sat__info.md#a04fc29e6cf9f1ff6f1f638ae633d5a11); /\* See ubx\_gnss\_id \*/

[ 154](structubx__nav__sat_1_1ubx__nav__sat__info.md#ab7ba4e9d36ab136c0bb8fde9b4f9b3e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sv\_id](structubx__nav__sat_1_1ubx__nav__sat__info.md#ab7ba4e9d36ab136c0bb8fde9b4f9b3e5);

[ 155](structubx__nav__sat_1_1ubx__nav__sat__info.md#a83e6ba9e50cc24fc0d80de3947daf571) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cno](structubx__nav__sat_1_1ubx__nav__sat__info.md#a83e6ba9e50cc24fc0d80de3947daf571); /\* Carrier-to-noise ratio. dBHz \*/

[ 156](structubx__nav__sat_1_1ubx__nav__sat__info.md#a9133131e06119371d14be09f99b24a8e) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [elevation](structubx__nav__sat_1_1ubx__nav__sat__info.md#a9133131e06119371d14be09f99b24a8e); /\* Elevation (range: +/- 90). Degrees \*/

[ 157](structubx__nav__sat_1_1ubx__nav__sat__info.md#a3a50255230b6ed80bfa4eb8ff83acf89) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [azimuth](structubx__nav__sat_1_1ubx__nav__sat__info.md#a3a50255230b6ed80bfa4eb8ff83acf89); /\* Azimuth (range: 0 - 360). Degrees \*/

[ 158](structubx__nav__sat_1_1ubx__nav__sat__info.md#a442709d1e9b43ae8c27606a5fb878c89) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [pseu\_res](structubx__nav__sat_1_1ubx__nav__sat__info.md#a442709d1e9b43ae8c27606a5fb878c89); /\* Pseudorange Residual. Meters \*/

[ 159](structubx__nav__sat_1_1ubx__nav__sat__info.md#ac6872360564b383ce2cd5a061717c8fe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structubx__nav__sat_1_1ubx__nav__sat__info.md#ac6872360564b383ce2cd5a061717c8fe);

[ 160](structubx__nav__sat.md#ade983d7b35cf81a6d769979f7cb5919d) } [sat](structubx__nav__sat.md#ade983d7b35cf81a6d769979f7cb5919d)[];

161};

162

[ 163](modem_2ubx_2protocol_8h.md#a260c4adbe9524bd747127a4e3f14bbca)enum [ubx\_msg\_id\_ack](modem_2ubx_2protocol_8h.md#a260c4adbe9524bd747127a4e3f14bbca) {

[ 164](modem_2ubx_2protocol_8h.md#a260c4adbe9524bd747127a4e3f14bbcaa88bba7f61485369188998bc1c18b2511) [UBX\_MSG\_ID\_ACK](modem_2ubx_2protocol_8h.md#a260c4adbe9524bd747127a4e3f14bbcaa88bba7f61485369188998bc1c18b2511) = 0x01,

[ 165](modem_2ubx_2protocol_8h.md#a260c4adbe9524bd747127a4e3f14bbcaacd2316ff6386c7eb2da90de1f4466469) [UBX\_MSG\_ID\_NAK](modem_2ubx_2protocol_8h.md#a260c4adbe9524bd747127a4e3f14bbcaacd2316ff6386c7eb2da90de1f4466469) = 0x00

166};

167

[ 168](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7)enum [ubx\_msg\_id\_cfg](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7) {

[ 169](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7a871b880c791ad49c55164856ac4f83f9) [UBX\_MSG\_ID\_CFG\_PRT](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7a871b880c791ad49c55164856ac4f83f9) = 0x00,

[ 170](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7ace6e98ad1c1ac7232327d42b0f4302ef) [UBX\_MSG\_ID\_CFG\_MSG](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7ace6e98ad1c1ac7232327d42b0f4302ef) = 0x01,

[ 171](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7ad2c8bf68306ca6bb22e88c5c6d957453) [UBX\_MSG\_ID\_CFG\_RST](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7ad2c8bf68306ca6bb22e88c5c6d957453) = 0x04,

[ 172](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7a89a96eb89044b208d3a6c29fc273fa26) [UBX\_MSG\_ID\_CFG\_RATE](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7a89a96eb89044b208d3a6c29fc273fa26) = 0x08,

[ 173](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7a036303b6caf601b73bfb48b3a7423309) [UBX\_MSG\_ID\_CFG\_NAV5](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7a036303b6caf601b73bfb48b3a7423309) = 0x24,

[ 174](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3) [UBX\_MSG\_ID\_CFG\_VAL\_SET](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3) = 0x8A,

[ 175](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7aa31397b2154b0f1f9b1e906c91a6bc8c) [UBX\_MSG\_ID\_CFG\_VAL\_GET](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7aa31397b2154b0f1f9b1e906c91a6bc8c) = 0x8B,

176};

177

[ 178](modem_2ubx_2protocol_8h.md#a0d969e434f941cf5af7143cca0cf0fe4)enum [ubx\_msg\_id\_mon](modem_2ubx_2protocol_8h.md#a0d969e434f941cf5af7143cca0cf0fe4) {

[ 179](modem_2ubx_2protocol_8h.md#a0d969e434f941cf5af7143cca0cf0fe4a43aa77232e6c2aed82ecf2033c0a06b0) [UBX\_MSG\_ID\_MON\_VER](modem_2ubx_2protocol_8h.md#a0d969e434f941cf5af7143cca0cf0fe4a43aa77232e6c2aed82ecf2033c0a06b0) = 0x04,

[ 180](modem_2ubx_2protocol_8h.md#a0d969e434f941cf5af7143cca0cf0fe4a66c14a28074edc8631bd6b47f5c45888) [UBX\_MSG\_ID\_MON\_GNSS](modem_2ubx_2protocol_8h.md#a0d969e434f941cf5af7143cca0cf0fe4a66c14a28074edc8631bd6b47f5c45888) = 0x28,

181};

182

[ 183](structubx__ack.md)struct [ubx\_ack](structubx__ack.md) {

[ 184](structubx__ack.md#ac8f56f9375b0edeb9788032e0d5b2ac5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) class;

[ 185](structubx__ack.md#ab68abe2083b8446a2e3ffc4b603ac47d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structubx__ack.md#ab68abe2083b8446a2e3ffc4b603ac47d);

186};

187

[ 188](modem_2ubx_2protocol_8h.md#ae23528d7cc5a34a48f062a084ae2dbd0)#define UBX\_GNSS\_SELECTION\_GPS BIT(0)

[ 189](modem_2ubx_2protocol_8h.md#ab767685719aa08364b5e77262fae232a)#define UBX\_GNSS\_SELECTION\_GLONASS BIT(1)

[ 190](modem_2ubx_2protocol_8h.md#ad57613b25d1716b7ca3e01d37b64a16d)#define UBX\_GNSS\_SELECTION\_BEIDOU BIT(2)

[ 191](modem_2ubx_2protocol_8h.md#aa338a732341e0e1560a749123cecd700)#define UBX\_GNSS\_SELECTION\_GALILEO BIT(3)

192

[ 193](structubx__mon__gnss.md)struct [ubx\_mon\_gnss](structubx__mon__gnss.md) {

[ 194](structubx__mon__gnss.md#aebcccc44a80ef3b327d7d479ccb5ebe5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ver](structubx__mon__gnss.md#aebcccc44a80ef3b327d7d479ccb5ebe5);

195 struct {

[ 196](structubx__mon__gnss.md#a8f76d361c23ae4a94d29277be0aa36f8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [supported](structubx__mon__gnss.md#a8f76d361c23ae4a94d29277be0aa36f8);

[ 197](structubx__mon__gnss.md#a2b94264d40d0aa740b20d9fa9565d155) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [default\_enabled](structubx__mon__gnss.md#a2b94264d40d0aa740b20d9fa9565d155);

[ 198](structubx__mon__gnss.md#ad09bcd6e739e385c275f8a1cae8725b3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enabled](structubx__mon__gnss.md#ad09bcd6e739e385c275f8a1cae8725b3);

[ 199](structubx__mon__gnss.md#ae004377f656dede9b0ebe98caeea588f) } [selection](structubx__mon__gnss.md#ae004377f656dede9b0ebe98caeea588f);

[ 200](structubx__mon__gnss.md#a34b9073dda3d6ad734109cea8ba5a0d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [simultaneous](structubx__mon__gnss.md#a34b9073dda3d6ad734109cea8ba5a0d2);

[ 201](structubx__mon__gnss.md#a045256bfbf8fe9b398ef77d10e00395a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved1](structubx__mon__gnss.md#a045256bfbf8fe9b398ef77d10e00395a)[3];

202} \_\_packed;

203

[ 204](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baa)enum [ubx\_cfg\_port\_id](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baa) {

[ 205](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baaa5c7c1a24670995305bcb8e98cfd1fa19) [UBX\_CFG\_PORT\_ID\_DDC](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baaa5c7c1a24670995305bcb8e98cfd1fa19) = 0,

[ 206](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baaaccb591a437d0ed7cca8888f41b855efb) [UBX\_CFG\_PORT\_ID\_UART](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baaaccb591a437d0ed7cca8888f41b855efb) = 1,

[ 207](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baaa3af5f6c24fade976d4ece339e9240114) [UBX\_CFG\_PORT\_ID\_USB](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baaa3af5f6c24fade976d4ece339e9240114) = 2,

[ 208](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baaaa0ee1de6e26bb0585f24fddbe3d7ec9a) [UBX\_CFG\_PORT\_ID\_SPI](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baaaa0ee1de6e26bb0585f24fddbe3d7ec9a) = 3,

209};

210

[ 211](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78a)enum [ubx\_cfg\_char\_len](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78a) {

[ 212](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78aa019364b4a4482098acc0d7821b456b83) [UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_5](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78aa019364b4a4482098acc0d7821b456b83) = 0, /\* Not supported \*/

[ 213](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78aaeea043882f976e34008f261e1b2ee5ac) [UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_6](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78aaeea043882f976e34008f261e1b2ee5ac) = 1, /\* Not supported \*/

[ 214](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78aaeacece1ca309918fa3abe7a02911f5ca) [UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_7](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78aaeacece1ca309918fa3abe7a02911f5ca) = 2, /\* Supported only with parity \*/

[ 215](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78aae7769c1dd298aabbad37ddaf6260eb4d) [UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_8](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78aae7769c1dd298aabbad37ddaf6260eb4d) = 3,

216};

217

[ 218](modem_2ubx_2protocol_8h.md#a2e5de1479afbcf20caa3300282bb0d1a)enum [ubx\_cfg\_parity](modem_2ubx_2protocol_8h.md#a2e5de1479afbcf20caa3300282bb0d1a) {

[ 219](modem_2ubx_2protocol_8h.md#a2e5de1479afbcf20caa3300282bb0d1aa1ef24c67f4e90f7c6fb011ec433ebb68) [UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_EVEN](modem_2ubx_2protocol_8h.md#a2e5de1479afbcf20caa3300282bb0d1aa1ef24c67f4e90f7c6fb011ec433ebb68) = 0,

[ 220](modem_2ubx_2protocol_8h.md#a2e5de1479afbcf20caa3300282bb0d1aa5db544370f64f19224e9243eae0942ac) [UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_ODD](modem_2ubx_2protocol_8h.md#a2e5de1479afbcf20caa3300282bb0d1aa5db544370f64f19224e9243eae0942ac) = 1,

[ 221](modem_2ubx_2protocol_8h.md#a2e5de1479afbcf20caa3300282bb0d1aa46b4ba80de7ca4c9d1ea403dd6efb385) [UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_NONE](modem_2ubx_2protocol_8h.md#a2e5de1479afbcf20caa3300282bb0d1aa46b4ba80de7ca4c9d1ea403dd6efb385) = 4,

222};

223

[ 224](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4c)enum [ubx\_cfg\_stop\_bits](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4c) {

[ 225](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4caf762dc50babaacd4cbb1ce753a8c0ae9) [UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_1](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4caf762dc50babaacd4cbb1ce753a8c0ae9) = 0,

[ 226](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4ca06c8d5338db83ce4a74a92228f04ffb1) [UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_1\_5](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4ca06c8d5338db83ce4a74a92228f04ffb1) = 1,

[ 227](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4caea0ef9695c70807a5bdfb1725f31ea3f) [UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_2](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4caea0ef9695c70807a5bdfb1725f31ea3f) = 2,

[ 228](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4ca461834aa0d5d6ddec370ecd247e330e6) [UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_0\_5](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4ca461834aa0d5d6ddec370ecd247e330e6) = 3,

229};

230

[ 231](modem_2ubx_2protocol_8h.md#a0eb35bbe06a126aa8aed1738b6dd56c2)#define UBX\_CFG\_PRT\_MODE\_CHAR\_LEN(val) (((val) & BIT\_MASK(2)) << 6)

[ 232](modem_2ubx_2protocol_8h.md#abe8dd1db5cf126f76f7a44f4715e9cfa)#define UBX\_CFG\_PRT\_MODE\_PARITY(val) (((val) & BIT\_MASK(3)) << 9)

[ 233](modem_2ubx_2protocol_8h.md#a23d980439eed2fe310c8be5107333489)#define UBX\_CFG\_PRT\_MODE\_STOP\_BITS(val) (((val) & BIT\_MASK(2)) << 12)

234

[ 235](modem_2ubx_2protocol_8h.md#a3f8c1064b9f51778df32e0b713302a2e)#define UBX\_CFG\_PRT\_PROTO\_MASK\_UBX BIT(0)

[ 236](modem_2ubx_2protocol_8h.md#a174c408931fd4ca3e6c8128dd540d2dd)#define UBX\_CFG\_PRT\_PROTO\_MASK\_NMEA BIT(1)

[ 237](modem_2ubx_2protocol_8h.md#ad481e57bb7b8707c468990ad0568d53c)#define UBX\_CFG\_PRT\_PROTO\_MASK\_RTCM3 BIT(5)

238

[ 239](structubx__cfg__prt.md)struct [ubx\_cfg\_prt](structubx__cfg__prt.md) {

[ 240](structubx__cfg__prt.md#af5a445ab598a2b93e884c916fe13affc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [port\_id](structubx__cfg__prt.md#af5a445ab598a2b93e884c916fe13affc); /\* See ubx\_cfg\_port\_id \*/

[ 241](structubx__cfg__prt.md#aba6bef46b7818a2396b77a0b1245ecc5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved1](structubx__cfg__prt.md#aba6bef46b7818a2396b77a0b1245ecc5);

[ 242](structubx__cfg__prt.md#a1d4df224a3a9e7e6031a418745ee4e95) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rx\_ready\_pin](structubx__cfg__prt.md#a1d4df224a3a9e7e6031a418745ee4e95);

[ 243](structubx__cfg__prt.md#a571753eb8aba5610fb7bc3546b7bfce9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mode](structubx__cfg__prt.md#a571753eb8aba5610fb7bc3546b7bfce9);

[ 244](structubx__cfg__prt.md#ac83072a87e0b29b30e6406f4f61cf26d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [baudrate](structubx__cfg__prt.md#ac83072a87e0b29b30e6406f4f61cf26d);

[ 245](structubx__cfg__prt.md#a960fd4543476b89b56f23dd29774b196) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [in\_proto\_mask](structubx__cfg__prt.md#a960fd4543476b89b56f23dd29774b196);

[ 246](structubx__cfg__prt.md#a1f4f3ab473e80648043b792bc4d5022f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [out\_proto\_mask](structubx__cfg__prt.md#a1f4f3ab473e80648043b792bc4d5022f);

[ 247](structubx__cfg__prt.md#a836be3302c1e038fbc09712242a51e69) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structubx__cfg__prt.md#a836be3302c1e038fbc09712242a51e69);

[ 248](structubx__cfg__prt.md#ad2bf468b82cc86ae1ce99c2fa129c231) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved2](structubx__cfg__prt.md#ad2bf468b82cc86ae1ce99c2fa129c231);

249};

250

[ 251](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561f)enum [ubx\_dyn\_model](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561f) {

[ 252](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa59c3bbc8cb2a44e26920adbe0251375b) [UBX\_DYN\_MODEL\_PORTABLE](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa59c3bbc8cb2a44e26920adbe0251375b) = 0,

[ 253](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa4f147b313644dba74c95930038201cf7) [UBX\_DYN\_MODEL\_STATIONARY](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa4f147b313644dba74c95930038201cf7) = 2,

[ 254](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa8a2a4bb1bb5b7f69960fdcde374f2ee6) [UBX\_DYN\_MODEL\_PEDESTRIAN](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa8a2a4bb1bb5b7f69960fdcde374f2ee6) = 3,

[ 255](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa736709e926d95754fef9260c596530e2) [UBX\_DYN\_MODEL\_AUTOMOTIVE](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa736709e926d95754fef9260c596530e2) = 4,

[ 256](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa6d89a732b306e21feeaee51cdbcc0bed) [UBX\_DYN\_MODEL\_SEA](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa6d89a732b306e21feeaee51cdbcc0bed) = 5,

[ 257](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa9bb36ad38aca4f118fe1bdc2f0351476) [UBX\_DYN\_MODEL\_AIRBORNE\_1G](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa9bb36ad38aca4f118fe1bdc2f0351476) = 6,

[ 258](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa1a39257d816910b26f2323b61a278519) [UBX\_DYN\_MODEL\_AIRBORNE\_2G](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa1a39257d816910b26f2323b61a278519) = 7,

[ 259](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fae4640365810ae80e8c24507fd7279f3d) [UBX\_DYN\_MODEL\_AIRBORNE\_4G](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fae4640365810ae80e8c24507fd7279f3d) = 8,

[ 260](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa172bc7d2ed80cadb4077ae42233764b2) [UBX\_DYN\_MODEL\_WRIST](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa172bc7d2ed80cadb4077ae42233764b2) = 9,

[ 261](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561faa062bfc1af7cc119d025dee309ac1d25) [UBX\_DYN\_MODEL\_BIKE](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561faa062bfc1af7cc119d025dee309ac1d25) = 10,

262};

263

[ 264](modem_2ubx_2protocol_8h.md#a342c0d62cf874ccb8b657ce85d91efe0)enum [ubx\_fix\_mode](modem_2ubx_2protocol_8h.md#a342c0d62cf874ccb8b657ce85d91efe0) {

[ 265](modem_2ubx_2protocol_8h.md#a342c0d62cf874ccb8b657ce85d91efe0a29354369703a5e54ae7e49edfff886ff) [UBX\_FIX\_MODE\_2D\_ONLY](modem_2ubx_2protocol_8h.md#a342c0d62cf874ccb8b657ce85d91efe0a29354369703a5e54ae7e49edfff886ff) = 1,

[ 266](modem_2ubx_2protocol_8h.md#a342c0d62cf874ccb8b657ce85d91efe0aa60a16ce7e100e06e0bab9a3922003a6) [UBX\_FIX\_MODE\_3D\_ONLY](modem_2ubx_2protocol_8h.md#a342c0d62cf874ccb8b657ce85d91efe0aa60a16ce7e100e06e0bab9a3922003a6) = 2,

[ 267](modem_2ubx_2protocol_8h.md#a342c0d62cf874ccb8b657ce85d91efe0a1e324c97e68e6d7ce35feb4ffe2ca617) [UBX\_FIX\_MODE\_AUTO](modem_2ubx_2protocol_8h.md#a342c0d62cf874ccb8b657ce85d91efe0a1e324c97e68e6d7ce35feb4ffe2ca617) = 3,

268};

269

[ 270](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23)enum [ubx\_utc\_standard](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23) {

[ 271](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23a8bc6c6397d5bc342ebe0ea36522e96a5) [UBX\_UTC\_STANDARD\_AUTOMATIC](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23a8bc6c6397d5bc342ebe0ea36522e96a5) = 0,

[ 272](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23a34b4b516760245d0a5bbfcbb5937d74c) [UBX\_UTC\_STANDARD\_GPS](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23a34b4b516760245d0a5bbfcbb5937d74c) = 3,

[ 273](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23a6fe85d7688c6730a492981fdc4623c67) [UBX\_UTC\_STANDARD\_GALILEO](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23a6fe85d7688c6730a492981fdc4623c67) = 5,

[ 274](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23ab6c294e0f55696a8c90ec8211673ca80) [UBX\_UTC\_STANDARD\_GLONASS](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23ab6c294e0f55696a8c90ec8211673ca80) = 6,

[ 275](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23a8eeae948253c11b7f097dd06896e66f8) [UBX\_UTC\_STANDARD\_BEIDOU](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23a8eeae948253c11b7f097dd06896e66f8) = 7,

276};

277

[ 278](modem_2ubx_2protocol_8h.md#adcfe7daa815d7a1a7dea67642b88ebbf)#define UBX\_CFG\_NAV5\_APPLY\_DYN BIT(0)

[ 279](modem_2ubx_2protocol_8h.md#a93b02f16b10968f47932c502e300c5a6)#define UBX\_CFG\_NAV5\_APPLY\_FIX\_MODE BIT(2)

280

[ 281](structubx__cfg__nav5.md)struct [ubx\_cfg\_nav5](structubx__cfg__nav5.md) {

[ 282](structubx__cfg__nav5.md#a564548f9609493061e995219f6397060) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [apply](structubx__cfg__nav5.md#a564548f9609493061e995219f6397060);

[ 283](structubx__cfg__nav5.md#a70f931b76bcd7a07a225648a15e73493) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dyn\_model](structubx__cfg__nav5.md#a70f931b76bcd7a07a225648a15e73493); /\* Dynamic platform model. See ubx\_dyn\_model \*/

[ 284](structubx__cfg__nav5.md#aab1b8aec77c186c576be839f728bba70) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fix\_mode](structubx__cfg__nav5.md#aab1b8aec77c186c576be839f728bba70); /\* Position fixing mode. See ubx\_fix\_mode \*/

[ 285](structubx__cfg__nav5.md#af915a692066df1855c270e106c1981ca) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [fixed\_alt](structubx__cfg__nav5.md#af915a692066df1855c270e106c1981ca); /\* Fixed altitude for 2D fix mode. Meters \*/

[ 286](structubx__cfg__nav5.md#abb48bda50e725eb8c2973518b468916f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fixed\_alt\_var](structubx__cfg__nav5.md#abb48bda50e725eb8c2973518b468916f); /\* Variance for Fixed altitude in 2D mode. Sq. meters \*/

[ 287](structubx__cfg__nav5.md#a2e7353d4ef2f0b3eef4ae3d1cc2be5ed) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [min\_elev](structubx__cfg__nav5.md#a2e7353d4ef2f0b3eef4ae3d1cc2be5ed); /\* Minimum Elevation to use a GNSS satellite in Navigation. Degrees \*/

[ 288](structubx__cfg__nav5.md#ace7d12cf8f63904274e658a6afe149d5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dr\_limit](structubx__cfg__nav5.md#ace7d12cf8f63904274e658a6afe149d5); /\* Reserved \*/

[ 289](structubx__cfg__nav5.md#a7c7f4338463e4d0c8040971ec31dc92c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_dop](structubx__cfg__nav5.md#a7c7f4338463e4d0c8040971ec31dc92c); /\* Position DOP mask \*/

[ 290](structubx__cfg__nav5.md#a4d8537de40aa5c98ae2e2183da9d44c3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_dop](structubx__cfg__nav5.md#a4d8537de40aa5c98ae2e2183da9d44c3); /\* Time DOP mask \*/

[ 291](structubx__cfg__nav5.md#a19d69c52edac0f65e2892b4c476d5a76) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_acc](structubx__cfg__nav5.md#a19d69c52edac0f65e2892b4c476d5a76); /\* Position accuracy mask. Meters \*/

[ 292](structubx__cfg__nav5.md#ad78a8828482ce26597f80f5e5a548afd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_acc](structubx__cfg__nav5.md#ad78a8828482ce26597f80f5e5a548afd); /\* Time accuracy mask. Meters \*/

[ 293](structubx__cfg__nav5.md#a5afd803452c65c4f03b122c9ff59cf2b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [static\_hold\_thresh](structubx__cfg__nav5.md#a5afd803452c65c4f03b122c9ff59cf2b); /\* Static hold threshold. cm/s \*/

[ 294](structubx__cfg__nav5.md#a2ee4fc58054c5f049890914c73089c99) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dgnss\_timeout](structubx__cfg__nav5.md#a2ee4fc58054c5f049890914c73089c99); /\* DGNSS timeout. Seconds \*/

[ 295](structubx__cfg__nav5.md#a648e22442293b24b2aa8b264a78b9bd2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cno\_thresh\_num\_svs](structubx__cfg__nav5.md#a648e22442293b24b2aa8b264a78b9bd2); /\* Number of satellites required above cno\_thresh \*/

[ 296](structubx__cfg__nav5.md#abf2a3de97f8d9cade6ec18408452938a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cno\_thresh](structubx__cfg__nav5.md#abf2a3de97f8d9cade6ec18408452938a); /\* C/N0 threshold for GNSS signals. dbHz \*/

[ 297](structubx__cfg__nav5.md#ab6b5cd2ef8db8c281f77c6684f6f8c0c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved1](structubx__cfg__nav5.md#ab6b5cd2ef8db8c281f77c6684f6f8c0c)[2];

[ 298](structubx__cfg__nav5.md#a6108faff3832cab3d734020c030c5c6c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [static\_hold\_max\_dist](structubx__cfg__nav5.md#a6108faff3832cab3d734020c030c5c6c); /\* Static hold distance threshold. Meters \*/

[ 299](structubx__cfg__nav5.md#ae0ecd871977ad119009cf1a2ac617327) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [utc\_standard](structubx__cfg__nav5.md#ae0ecd871977ad119009cf1a2ac617327); /\* UTC standard to be used. See ubx\_utc\_standard \*/

[ 300](structubx__cfg__nav5.md#ac3d21a048e77c404bcfa180af2e41992) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved2](structubx__cfg__nav5.md#ac3d21a048e77c404bcfa180af2e41992)[5];

301} \_\_packed;

302

[ 303](modem_2ubx_2protocol_8h.md#a43766ad4c0fd1d31fd547c090e3f39b6)enum [ubx\_cfg\_rst\_start\_mode](modem_2ubx_2protocol_8h.md#a43766ad4c0fd1d31fd547c090e3f39b6) {

[ 304](modem_2ubx_2protocol_8h.md#a43766ad4c0fd1d31fd547c090e3f39b6a67b9cba109cc8f57a38c41b1d521e3c7) [UBX\_CFG\_RST\_HOT\_START](modem_2ubx_2protocol_8h.md#a43766ad4c0fd1d31fd547c090e3f39b6a67b9cba109cc8f57a38c41b1d521e3c7) = 0x0000,

[ 305](modem_2ubx_2protocol_8h.md#a43766ad4c0fd1d31fd547c090e3f39b6a1621ed3281429f96fc598d90cc388c95) [UBX\_CFG\_RST\_WARM\_START](modem_2ubx_2protocol_8h.md#a43766ad4c0fd1d31fd547c090e3f39b6a1621ed3281429f96fc598d90cc388c95) = 0x0001,

[ 306](modem_2ubx_2protocol_8h.md#a43766ad4c0fd1d31fd547c090e3f39b6aaef8449ed29d6dd76bdd34157d873896) [UBX\_CFG\_RST\_COLD\_START](modem_2ubx_2protocol_8h.md#a43766ad4c0fd1d31fd547c090e3f39b6aaef8449ed29d6dd76bdd34157d873896) = 0xFFFF,

307};

308

[ 309](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896)enum [ubx\_cfg\_rst\_mode](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896) {

[ 310](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896ac02d28b95ef601af32dc898e35ad252e) [UBX\_CFG\_RST\_MODE\_HW](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896ac02d28b95ef601af32dc898e35ad252e) = 0x00,

[ 311](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896a7fd6f4b7557dfa6511dcb6354963d342) [UBX\_CFG\_RST\_MODE\_SW](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896a7fd6f4b7557dfa6511dcb6354963d342) = 0x01,

[ 312](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896a0e9177345e82ad614c1ab4c8b52b9265) [UBX\_CFG\_RST\_MODE\_GNSS\_STOP](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896a0e9177345e82ad614c1ab4c8b52b9265) = 0x08,

[ 313](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896aca25f86cc1d85c60b1d67509d0e9506b) [UBX\_CFG\_RST\_MODE\_GNSS\_START](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896aca25f86cc1d85c60b1d67509d0e9506b) = 0x09,

314};

315

[ 316](structubx__cfg__rst.md)struct [ubx\_cfg\_rst](structubx__cfg__rst.md) {

[ 317](structubx__cfg__rst.md#a7d7e94ffc6aa9518a31b3f829a732362) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [nav\_bbr\_mask](structubx__cfg__rst.md#a7d7e94ffc6aa9518a31b3f829a732362);

[ 318](structubx__cfg__rst.md#a1a63d295cf71e23a4afdb31637741b4f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reset\_mode](structubx__cfg__rst.md#a1a63d295cf71e23a4afdb31637741b4f);

[ 319](structubx__cfg__rst.md#aa1f7a46662f14e498b8bce84fb349d33) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structubx__cfg__rst.md#aa1f7a46662f14e498b8bce84fb349d33);

320};

321

[ 322](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952e)enum [ubx\_cfg\_rate\_time\_ref](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952e) {

[ 323](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952eacc3989fab9e22270c389b0318bbe45ea) [UBX\_CFG\_RATE\_TIME\_REF\_UTC](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952eacc3989fab9e22270c389b0318bbe45ea) = 0,

[ 324](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952ea7a2d00bdb7fef5ff7da1d3a682a1b82e) [UBX\_CFG\_RATE\_TIME\_REF\_GPS](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952ea7a2d00bdb7fef5ff7da1d3a682a1b82e) = 1,

[ 325](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952ea519dc8f11c80b5a08771fbc36c70fbb8) [UBX\_CFG\_RATE\_TIME\_REF\_GLONASS](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952ea519dc8f11c80b5a08771fbc36c70fbb8) = 2,

[ 326](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952ea30f66599c483f622607f0b13ad0451f8) [UBX\_CFG\_RATE\_TIME\_REF\_BEIDOU](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952ea30f66599c483f622607f0b13ad0451f8) = 3,

[ 327](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952eab7ed326b5da1087afb8d531d97bb9f16) [UBX\_CFG\_RATE\_TIME\_REF\_GALILEO](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952eab7ed326b5da1087afb8d531d97bb9f16) = 4,

[ 328](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952ea5be3c906a6c528f65575990041b7e6ce) [UBX\_CFG\_RATE\_TIME\_REF\_NAVIC](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952ea5be3c906a6c528f65575990041b7e6ce) = 5,

329};

330

[ 331](structubx__cfg__rate.md)struct [ubx\_cfg\_rate](structubx__cfg__rate.md) {

[ 332](structubx__cfg__rate.md#ae64d779c4a3fe255710be8f742f5b6c6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [meas\_rate\_ms](structubx__cfg__rate.md#ae64d779c4a3fe255710be8f742f5b6c6);

[ 333](structubx__cfg__rate.md#aafcbb36f844534c77e698dceccb2f5dc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [nav\_rate](structubx__cfg__rate.md#aafcbb36f844534c77e698dceccb2f5dc);

[ 334](structubx__cfg__rate.md#a444822a3a37dd51313bfc6968a3b4721) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [time\_ref](structubx__cfg__rate.md#a444822a3a37dd51313bfc6968a3b4721);

335};

336

[ 337](modem_2ubx_2protocol_8h.md#ad7e0ffe55e8dbd97caa5bc089d33540c)enum [ubx\_cfg\_val\_ver](modem_2ubx_2protocol_8h.md#ad7e0ffe55e8dbd97caa5bc089d33540c) {

[ 338](modem_2ubx_2protocol_8h.md#ad7e0ffe55e8dbd97caa5bc089d33540ca1fe2554bbbf05c86d3f9b0bc50927c1b) [UBX\_CFG\_VAL\_VER\_SIMPLE](modem_2ubx_2protocol_8h.md#ad7e0ffe55e8dbd97caa5bc089d33540ca1fe2554bbbf05c86d3f9b0bc50927c1b) = 0,

[ 339](modem_2ubx_2protocol_8h.md#ad7e0ffe55e8dbd97caa5bc089d33540caca3b7f2a39ff93b91b8317245e8375ab) [UBX\_CFG\_VAL\_VER\_TRANSACTION](modem_2ubx_2protocol_8h.md#ad7e0ffe55e8dbd97caa5bc089d33540caca3b7f2a39ff93b91b8317245e8375ab) = 1,

340};

341

[ 342](structubx__cfg__val__hdr.md)struct [ubx\_cfg\_val\_hdr](structubx__cfg__val__hdr.md) {

[ 343](structubx__cfg__val__hdr.md#a4d7a91e9521428e5b528ced88b030cd3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ver](structubx__cfg__val__hdr.md#a4d7a91e9521428e5b528ced88b030cd3); /\* See ubx\_cfg\_val\_ver \*/

[ 344](structubx__cfg__val__hdr.md#aa835050e25c8db0a5a88954ff0def88c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [layer](structubx__cfg__val__hdr.md#aa835050e25c8db0a5a88954ff0def88c);

[ 345](structubx__cfg__val__hdr.md#a6206dc714df9656cc37e0b802ab541b8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [position](structubx__cfg__val__hdr.md#a6206dc714df9656cc37e0b802ab541b8);

346} \_\_packed;

347

[ 348](structubx__cfg__val__u8.md)struct [ubx\_cfg\_val\_u8](structubx__cfg__val__u8.md) {

[ 349](structubx__cfg__val__u8.md#a793646932ce054ab8561078981f57250) struct [ubx\_cfg\_val\_hdr](structubx__cfg__val__hdr.md) [hdr](structubx__cfg__val__u8.md#a793646932ce054ab8561078981f57250);

[ 350](structubx__cfg__val__u8.md#a2c1cbf9a552608150eafc1f2d92b03b5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [key](structubx__cfg__val__u8.md#a2c1cbf9a552608150eafc1f2d92b03b5);

[ 351](structubx__cfg__val__u8.md#a325aaaf688433cab710d0c3e835fb9ed) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structubx__cfg__val__u8.md#a325aaaf688433cab710d0c3e835fb9ed);

352} \_\_packed;

353

[ 354](structubx__cfg__val__u16.md)struct [ubx\_cfg\_val\_u16](structubx__cfg__val__u16.md) {

[ 355](structubx__cfg__val__u16.md#a32e877f1e2f60b209fbcdd057aa82c4f) struct [ubx\_cfg\_val\_hdr](structubx__cfg__val__hdr.md) [hdr](structubx__cfg__val__u16.md#a32e877f1e2f60b209fbcdd057aa82c4f);

[ 356](structubx__cfg__val__u16.md#a87a9c181318e297935bb1eb65093d4a8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [key](structubx__cfg__val__u16.md#a87a9c181318e297935bb1eb65093d4a8);

[ 357](structubx__cfg__val__u16.md#a6226f1b8f4cb89cb318c07ff8ddcbbde) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value](structubx__cfg__val__u16.md#a6226f1b8f4cb89cb318c07ff8ddcbbde);

358} \_\_packed;

359

[ 360](structubx__cfg__val__u32.md)struct [ubx\_cfg\_val\_u32](structubx__cfg__val__u32.md) {

[ 361](structubx__cfg__val__u32.md#adc51df7bc8a50e1ca8843067bb309ac9) struct [ubx\_cfg\_val\_hdr](structubx__cfg__val__hdr.md) [hdr](structubx__cfg__val__u32.md#adc51df7bc8a50e1ca8843067bb309ac9);

[ 362](structubx__cfg__val__u32.md#ab02aa8d3b7039c06692a805aed30f246) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [key](structubx__cfg__val__u32.md#ab02aa8d3b7039c06692a805aed30f246);

[ 363](structubx__cfg__val__u32.md#a2c1d446c7c8bef80052d2438fb998d58) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [value](structubx__cfg__val__u32.md#a2c1d446c7c8bef80052d2438fb998d58);

364} \_\_packed;

365

[ 366](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6c)enum [ubx\_msg\_id\_nmea\_std](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6c) {

[ 367](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cac84f9ad61c85bbce60e680639c3d88ad) [UBX\_MSG\_ID\_NMEA\_STD\_DTM](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cac84f9ad61c85bbce60e680639c3d88ad) = 0x0A,

[ 368](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca5174a26b3b79356bf06402de46bc0774) [UBX\_MSG\_ID\_NMEA\_STD\_GBQ](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca5174a26b3b79356bf06402de46bc0774) = 0x44,

[ 369](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6caef6c925e20f072665bf55e435d37a6ac) [UBX\_MSG\_ID\_NMEA\_STD\_GBS](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6caef6c925e20f072665bf55e435d37a6ac) = 0x09,

[ 370](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca07aa8c55e3504c0d19b1e123f4d2e7c7) [UBX\_MSG\_ID\_NMEA\_STD\_GGA](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca07aa8c55e3504c0d19b1e123f4d2e7c7) = 0x00,

[ 371](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca6435225efac8c7ef6e336a84fa2e8932) [UBX\_MSG\_ID\_NMEA\_STD\_GLL](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca6435225efac8c7ef6e336a84fa2e8932) = 0x01,

[ 372](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca263a724b491a6303d5486828a49a8961) [UBX\_MSG\_ID\_NMEA\_STD\_GLQ](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca263a724b491a6303d5486828a49a8961) = 0x43,

[ 373](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6caa2c68fe9d01bc4acf3054d667f3e2a77) [UBX\_MSG\_ID\_NMEA\_STD\_GNQ](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6caa2c68fe9d01bc4acf3054d667f3e2a77) = 0x42,

[ 374](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cafea982067c784c47ae5b1ad7e91b4191) [UBX\_MSG\_ID\_NMEA\_STD\_GNS](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cafea982067c784c47ae5b1ad7e91b4191) = 0x0D,

[ 375](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca39492ba0c78d0290819b9410e2e55781) [UBX\_MSG\_ID\_NMEA\_STD\_GPQ](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca39492ba0c78d0290819b9410e2e55781) = 0x40,

[ 376](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca7f1d764aa078c284c575ec610d4f4853) [UBX\_MSG\_ID\_NMEA\_STD\_GRS](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca7f1d764aa078c284c575ec610d4f4853) = 0x06,

[ 377](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cae3c6e42e75e69a34d7017d2f2aa3c70d) [UBX\_MSG\_ID\_NMEA\_STD\_GSA](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cae3c6e42e75e69a34d7017d2f2aa3c70d) = 0x02,

[ 378](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca99b8f62b1d204b335a06ed6f3ef214e6) [UBX\_MSG\_ID\_NMEA\_STD\_GST](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca99b8f62b1d204b335a06ed6f3ef214e6) = 0x07,

[ 379](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca2a5cc3b49abc9be0c6bbab0a9963ba03) [UBX\_MSG\_ID\_NMEA\_STD\_GSV](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca2a5cc3b49abc9be0c6bbab0a9963ba03) = 0x03,

[ 380](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca8787502b2d9a14d2ce79b1ce1713d6f3) [UBX\_MSG\_ID\_NMEA\_STD\_RMC](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca8787502b2d9a14d2ce79b1ce1713d6f3) = 0x04,

[ 381](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca884ab2ce56a1f7a08d4b9d06b944ad37) [UBX\_MSG\_ID\_NMEA\_STD\_THS](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca884ab2ce56a1f7a08d4b9d06b944ad37) = 0x0E,

[ 382](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cad58d4ac5b57cbdd42d360560cc16fc0e) [UBX\_MSG\_ID\_NMEA\_STD\_TXT](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cad58d4ac5b57cbdd42d360560cc16fc0e) = 0x41,

[ 383](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca58ad56a546a2df6c9359927375da9904) [UBX\_MSG\_ID\_NMEA\_STD\_VLW](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca58ad56a546a2df6c9359927375da9904) = 0x0F,

[ 384](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca5c12f57e0b4de16d09fc42f23740908b) [UBX\_MSG\_ID\_NMEA\_STD\_VTG](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca5c12f57e0b4de16d09fc42f23740908b) = 0x05,

[ 385](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cae6a2501b586793e75cdd0085170a9a27) [UBX\_MSG\_ID\_NMEA\_STD\_ZDA](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cae6a2501b586793e75cdd0085170a9a27) = 0x08,

386};

387

[ 388](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582)enum [ubx\_msg\_id\_nmea\_pubx](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582) {

[ 389](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582a43616a8ad2465c7521aa9ed28460cf57) [UBX\_MSG\_ID\_NMEA\_PUBX\_CONFIG](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582a43616a8ad2465c7521aa9ed28460cf57) = 0x41,

[ 390](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582a61cbc043ccd0a96ba2327d7bd95189c6) [UBX\_MSG\_ID\_NMEA\_PUBX\_POSITION](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582a61cbc043ccd0a96ba2327d7bd95189c6) = 0x00,

[ 391](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582af5ccdcc3eed53b0906b83667443e3667) [UBX\_MSG\_ID\_NMEA\_PUBX\_RATE](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582af5ccdcc3eed53b0906b83667443e3667) = 0x40,

[ 392](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582a73aeb813a098d600dfb60561bc042e2a) [UBX\_MSG\_ID\_NMEA\_PUBX\_SVSTATUS](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582a73aeb813a098d600dfb60561bc042e2a) = 0x03,

[ 393](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582a9f36e6c7688a62737beb203e82de91ef) [UBX\_MSG\_ID\_NMEA\_PUBX\_TIME](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582a9f36e6c7688a62737beb203e82de91ef) = 0x04,

394};

395

[ 396](structubx__cfg__msg__rate.md)struct [ubx\_cfg\_msg\_rate](structubx__cfg__msg__rate.md) {

[ 397](structubx__cfg__msg__rate.md#aeed290a2702b7c0792df350b32b66069) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) class;

[ 398](structubx__cfg__msg__rate.md#aee7d34d68f3665c665f8ae4bc6d1a04a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structubx__cfg__msg__rate.md#aee7d34d68f3665c665f8ae4bc6d1a04a);

[ 399](structubx__cfg__msg__rate.md#a7a030b3e70356b899ed7284e750041b0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rate](structubx__cfg__msg__rate.md#a7a030b3e70356b899ed7284e750041b0);

400};

401

[ 402](structubx__mon__ver.md)struct [ubx\_mon\_ver](structubx__mon__ver.md) {

[ 403](structubx__mon__ver.md#aa0495c27ac850d56ddaa92bc4689ba7f) char [sw\_ver](structubx__mon__ver.md#aa0495c27ac850d56ddaa92bc4689ba7f)[30];

[ 404](structubx__mon__ver.md#a07a2fdbe52fa48e9412f39bff1256318) char [hw\_ver](structubx__mon__ver.md#a07a2fdbe52fa48e9412f39bff1256318)[10];

405};

406

[ 407](modem_2ubx_2protocol_8h.md#a450f46250ef486af4f933e69ddbb42d2)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ubx\_calc\_checksum](modem_2ubx_2protocol_8h.md#a450f46250ef486af4f933e69ddbb42d2)(const struct [ubx\_frame](structubx__frame.md) \*frame, size\_t len)

408{

409 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ck\_a = 0;

410 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ck\_b = 0;

411 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data = (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)frame;

412

414 if (len != [UBX\_FRAME\_SZ](modem_2ubx_2protocol_8h.md#a4c64b9118da471baa6a7a88ee345bf66)(frame->[payload\_size](structubx__frame.md#a77b5030a6b95aef58b1c17f0368dd7ce))) {

415 return 0xFFFF;

416 }

417

418 for (int i = [UBX\_FRAME\_MSG\_CLASS\_IDX](modem_2ubx_2protocol_8h.md#a2c667ef9bb2d12effb251f4df6827c73) ; i < ([UBX\_FRAME\_SZ](modem_2ubx_2protocol_8h.md#a4c64b9118da471baa6a7a88ee345bf66)(frame->[payload\_size](structubx__frame.md#a77b5030a6b95aef58b1c17f0368dd7ce)) - 2) ; i++) {

419 ck\_a = ck\_a + data[i];

420 ck\_b = ck\_b + ck\_a;

421 }

422

423 return ((ck\_a & 0xFF) | ((ck\_b & 0xFF) << 8));

424}

425

[ 426](modem_2ubx_2protocol_8h.md#acdc0d9b7d25df6aba6bb091e7034f5ba)static inline int [ubx\_frame\_encode](modem_2ubx_2protocol_8h.md#acdc0d9b7d25df6aba6bb091e7034f5ba)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) class, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id,

427 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, size\_t payload\_len,

428 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buf\_len)

429{

430 if (buf\_len < [UBX\_FRAME\_SZ](modem_2ubx_2protocol_8h.md#a4c64b9118da471baa6a7a88ee345bf66)(payload\_len)) {

431 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

432 }

433

434 struct [ubx\_frame](structubx__frame.md) \*frame = (struct [ubx\_frame](structubx__frame.md) \*)buf;

435

436 frame->[preamble\_sync\_char\_1](structubx__frame.md#acf80f38e8f26bb32848ae2978a1f87a1) = [UBX\_PREAMBLE\_SYNC\_CHAR\_1](modem_2ubx_2protocol_8h.md#a1693f3584605a0197076cba71c79b0df);

437 frame->[preamble\_sync\_char\_2](structubx__frame.md#ac61fb72df7c1cd8a9bacb787071cb77d) = [UBX\_PREAMBLE\_SYNC\_CHAR\_2](modem_2ubx_2protocol_8h.md#ad8d6229db563db619d4f0a9f225fb640);

438 frame->[class](structubx__frame.md#a2dcc29a82e7dfff2d1e4194f1bc035e8) = class;

439 frame->[id](structubx__frame.md#a4e578da5900365d498708f7a61d48ba4) = [id](structubx__frame.md#a4e578da5900365d498708f7a61d48ba4);

440 frame->[payload\_size](structubx__frame.md#a77b5030a6b95aef58b1c17f0368dd7ce) = payload\_len;

441 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(frame->[payload\_and\_checksum](structubx__frame.md#a70c465b5bd1e9837c253d78fb210f4ce), payload, payload\_len);

442

443 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) checksum = [ubx\_calc\_checksum](modem_2ubx_2protocol_8h.md#a450f46250ef486af4f933e69ddbb42d2)(frame, [UBX\_FRAME\_SZ](modem_2ubx_2protocol_8h.md#a4c64b9118da471baa6a7a88ee345bf66)(payload\_len));

444

445 frame->[payload\_and\_checksum](structubx__frame.md#a70c465b5bd1e9837c253d78fb210f4ce)[payload\_len] = checksum & 0xFF;

446 frame->[payload\_and\_checksum](structubx__frame.md#a70c465b5bd1e9837c253d78fb210f4ce)[payload\_len + 1] = (checksum >> 8) & 0xFF;

447

448 return [UBX\_FRAME\_SZ](modem_2ubx_2protocol_8h.md#a4c64b9118da471baa6a7a88ee345bf66)(payload\_len);

449}

450

[ 451](modem_2ubx_2protocol_8h.md#ad79a0ce05086ada71822ccb9100bc100)#define UBX\_FRAME\_DEFINE(\_name, \_frame) \

452 const static struct ubx\_frame \_name = \_frame

453

[ 454](modem_2ubx_2protocol_8h.md#aca7cb6846e6d01cc84df655f22832987)#define UBX\_FRAME\_ARRAY\_DEFINE(\_name, ...) \

455 const struct ubx\_frame \*\_name[] = {\_\_VA\_ARGS\_\_};

456

[ 457](modem_2ubx_2protocol_8h.md#a8cf6388d5ee4509e36742e30dc640889)#define UBX\_FRAME\_ACK\_INITIALIZER(\_class\_id, \_msg\_id) \

458 UBX\_FRAME\_INITIALIZER\_PAYLOAD(UBX\_CLASS\_ID\_ACK, UBX\_MSG\_ID\_ACK, \_class\_id, \_msg\_id)

459

[ 460](modem_2ubx_2protocol_8h.md#a5b5ffd92f5894fc966b1875c7ce4c1a3)#define UBX\_FRAME\_NAK\_INITIALIZER(\_class\_id, \_msg\_id) \

461 UBX\_FRAME\_INITIALIZER\_PAYLOAD(UBX\_CLASS\_ID\_ACK, UBX\_MSG\_ID\_NAK, \_class\_id, \_msg\_id)

462

[ 463](modem_2ubx_2protocol_8h.md#aed21b263c25f39d499b37dfff38bca39)#define UBX\_FRAME\_CFG\_RST\_INITIALIZER(\_start\_mode, \_reset\_mode) \

464 UBX\_FRAME\_INITIALIZER\_PAYLOAD(UBX\_CLASS\_ID\_CFG, UBX\_MSG\_ID\_CFG\_RST, \

465 (\_start\_mode & 0xFF), ((\_start\_mode >> 8) & 0xFF), \

466 \_reset\_mode, 0)

467

[ 468](modem_2ubx_2protocol_8h.md#a3192675717120efc97a8858605b3f45d)#define UBX\_FRAME\_CFG\_RATE\_INITIALIZER(\_meas\_rate\_ms, \_nav\_rate, \_time\_ref) \

469 UBX\_FRAME\_INITIALIZER\_PAYLOAD(UBX\_CLASS\_ID\_CFG, UBX\_MSG\_ID\_CFG\_RATE, \

470 (\_meas\_rate\_ms & 0xFF), ((\_meas\_rate\_ms >> 8) & 0xFF), \

471 (\_nav\_rate & 0xFF), ((\_nav\_rate >> 8) & 0xFF), \

472 (\_time\_ref & 0xFF), ((\_time\_ref >> 8) & 0xFF))

473

[ 474](modem_2ubx_2protocol_8h.md#af9ce35b33de7f9ebc68d11731beb02f0)#define UBX\_FRAME\_CFG\_MSG\_RATE\_INITIALIZER(\_class\_id, \_msg\_id, \_rate) \

475 UBX\_FRAME\_INITIALIZER\_PAYLOAD(UBX\_CLASS\_ID\_CFG, UBX\_MSG\_ID\_CFG\_MSG, \

476 \_class\_id, \_msg\_id, \_rate)

477

[ 478](modem_2ubx_2protocol_8h.md#a5b4484d44a25068f960f7f1196cffe89)#define UBX\_FRAME\_CFG\_VAL\_SET\_U8\_INITIALIZER(\_key, \_value) \

479 UBX\_FRAME\_INITIALIZER\_PAYLOAD(UBX\_CLASS\_ID\_CFG, UBX\_MSG\_ID\_CFG\_VAL\_SET, \

480 0x00, 0x01, 0x00, 0x00, \

481 ((\_key) & 0xFF), (((\_key) >> 8) & 0xFF), \

482 (((\_key) >> 16) & 0xFF), (((\_key) >> 24) & 0xFF), \

483 ((\_value) & 0xFF))

484

[ 485](modem_2ubx_2protocol_8h.md#a66b9664185ed9cfb096df2b375e41f0e)#define UBX\_FRAME\_CFG\_VAL\_SET\_U16\_INITIALIZER(\_key, \_value) \

486 UBX\_FRAME\_INITIALIZER\_PAYLOAD(UBX\_CLASS\_ID\_CFG, UBX\_MSG\_ID\_CFG\_VAL\_SET, \

487 0x00, 0x01, 0x00, 0x00, \

488 ((\_key) & 0xFF), (((\_key) >> 8) & 0xFF), \

489 (((\_key) >> 16) & 0xFF), (((\_key) >> 24) & 0xFF), \

490 ((\_value) & 0xFF), (((\_value) >> 8) & 0xFF))

491

[ 492](modem_2ubx_2protocol_8h.md#a997cd3bd57d5cfc6c4f1eeca2bc6ba37)#define UBX\_FRAME\_CFG\_VAL\_SET\_U32\_INITIALIZER(\_key, \_value) \

493 UBX\_FRAME\_INITIALIZER\_PAYLOAD(UBX\_CLASS\_ID\_CFG, UBX\_MSG\_ID\_CFG\_VAL\_SET, \

494 0x00, 0x01, 0x00, 0x00, \

495 ((\_key) & 0xFF), (((\_key) >> 8) & 0xFF), \

496 (((\_key) >> 16) & 0xFF), (((\_key) >> 24) & 0xFF), \

497 ((\_value) & 0xFF), (((\_value) >> 8) & 0xFF), \

498 (((\_value) >> 16) & 0xFF), (((\_value) >> 24) & 0xFF))

499

[ 500](modem_2ubx_2protocol_8h.md#a1d7a930de22dadce2aae88e64e246dd9)#define UBX\_FRAME\_CFG\_VAL\_GET\_INITIALIZER(\_key) \

501 UBX\_FRAME\_INITIALIZER\_PAYLOAD(UBX\_CLASS\_ID\_CFG, UBX\_MSG\_ID\_CFG\_VAL\_GET, \

502 0x00, 0x00, 0x00, 0x00, \

503 ((\_key) & 0xFF), (((\_key) >> 8) & 0xFF), \

504 (((\_key) >> 16) & 0xFF), (((\_key) >> 24) & 0xFF))

505

[ 506](modem_2ubx_2protocol_8h.md#a4d90346d76d003aeddf16fc665203926)#define UBX\_FRAME\_INITIALIZER\_PAYLOAD(\_class\_id, \_msg\_id, ...) \

507 \_UBX\_FRAME\_INITIALIZER\_PAYLOAD(\_class\_id, \_msg\_id, \_\_VA\_ARGS\_\_)

508

509#define \_UBX\_FRAME\_INITIALIZER\_PAYLOAD(\_class\_id, \_msg\_id, ...) \

510 { \

511 .preamble\_sync\_char\_1 = UBX\_PREAMBLE\_SYNC\_CHAR\_1, \

512 .preamble\_sync\_char\_2 = UBX\_PREAMBLE\_SYNC\_CHAR\_2, \

513 .class = \_class\_id, \

514 .id = \_msg\_id, \

515 .payload\_size = (NUM\_VA\_ARGS(\_\_VA\_ARGS\_\_)) & 0xFFFF, \

516 .payload\_and\_checksum = { \

517 \_\_VA\_ARGS\_\_, \

518 UBX\_CSUM(\_class\_id, \_msg\_id, \

519 ((NUM\_VA\_ARGS(\_\_VA\_ARGS\_\_)) & 0xFF), \

520 (((NUM\_VA\_ARGS(\_\_VA\_ARGS\_\_)) >> 8) & 0xFF), \

521 \_\_VA\_ARGS\_\_), \

522 }, \

523 }

524

[ 525](modem_2ubx_2protocol_8h.md#a1cf8842293fe70f3ea22686a55d9beda)#define UBX\_FRAME\_GET\_INITIALIZER(\_class\_id, \_msg\_id) \

526 { \

527 .preamble\_sync\_char\_1 = UBX\_PREAMBLE\_SYNC\_CHAR\_1, \

528 .preamble\_sync\_char\_2 = UBX\_PREAMBLE\_SYNC\_CHAR\_2, \

529 .class = \_class\_id, \

530 .id = \_msg\_id, \

531 .payload\_size = 0, \

532 .payload\_and\_checksum = { \

533 UBX\_CSUM(\_class\_id, \_msg\_id, 0, 0), \

534 }, \

535 }

536

537#endif /\* ZEPHYR\_MODEM\_UBX\_PROTOCOL\_ \*/

[checksum.h](checksum_8h.md)

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)

time\_t time(time\_t \*tloc)

[ubx\_msg\_id\_mon](modem_2ubx_2protocol_8h.md#a0d969e434f941cf5af7143cca0cf0fe4)

ubx\_msg\_id\_mon

**Definition** protocol.h:178

[UBX\_MSG\_ID\_MON\_VER](modem_2ubx_2protocol_8h.md#a0d969e434f941cf5af7143cca0cf0fe4a43aa77232e6c2aed82ecf2033c0a06b0)

@ UBX\_MSG\_ID\_MON\_VER

**Definition** protocol.h:179

[UBX\_MSG\_ID\_MON\_GNSS](modem_2ubx_2protocol_8h.md#a0d969e434f941cf5af7143cca0cf0fe4a66c14a28074edc8631bd6b47f5c45888)

@ UBX\_MSG\_ID\_MON\_GNSS

**Definition** protocol.h:180

[UBX\_PREAMBLE\_SYNC\_CHAR\_1](modem_2ubx_2protocol_8h.md#a1693f3584605a0197076cba71c79b0df)

#define UBX\_PREAMBLE\_SYNC\_CHAR\_1

**Definition** protocol.h:19

[ubx\_nav\_fix\_type](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fef)

ubx\_nav\_fix\_type

**Definition** protocol.h:68

[UBX\_NAV\_FIX\_TYPE\_3D](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefa1f8c2845d6e8e41f62cc28b7f1681f43)

@ UBX\_NAV\_FIX\_TYPE\_3D

**Definition** protocol.h:72

[UBX\_NAV\_FIX\_TYPE\_TIME\_ONLY](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefa2c20469f6893f651ad14b8ed6a7c3845)

@ UBX\_NAV\_FIX\_TYPE\_TIME\_ONLY

**Definition** protocol.h:74

[UBX\_NAV\_FIX\_TYPE\_GNSS\_DR\_COMBINED](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefa648f596240841758588749574998bd71)

@ UBX\_NAV\_FIX\_TYPE\_GNSS\_DR\_COMBINED

**Definition** protocol.h:73

[UBX\_NAV\_FIX\_TYPE\_NO\_FIX](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefad351fdc11590580b88ba5b486113e498)

@ UBX\_NAV\_FIX\_TYPE\_NO\_FIX

**Definition** protocol.h:69

[UBX\_NAV\_FIX\_TYPE\_DR](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefae28182c06da19d2b498f92d09d74b33e)

@ UBX\_NAV\_FIX\_TYPE\_DR

**Definition** protocol.h:70

[UBX\_NAV\_FIX\_TYPE\_2D](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fefae47dad429327e6a0cc89e339729b2651)

@ UBX\_NAV\_FIX\_TYPE\_2D

**Definition** protocol.h:71

[ubx\_msg\_id\_ack](modem_2ubx_2protocol_8h.md#a260c4adbe9524bd747127a4e3f14bbca)

ubx\_msg\_id\_ack

**Definition** protocol.h:163

[UBX\_MSG\_ID\_ACK](modem_2ubx_2protocol_8h.md#a260c4adbe9524bd747127a4e3f14bbcaa88bba7f61485369188998bc1c18b2511)

@ UBX\_MSG\_ID\_ACK

**Definition** protocol.h:164

[UBX\_MSG\_ID\_NAK](modem_2ubx_2protocol_8h.md#a260c4adbe9524bd747127a4e3f14bbcaacd2316ff6386c7eb2da90de1f4466469)

@ UBX\_MSG\_ID\_NAK

**Definition** protocol.h:165

[UBX\_FRAME\_MSG\_CLASS\_IDX](modem_2ubx_2protocol_8h.md#a2c667ef9bb2d12effb251f4df6827c73)

#define UBX\_FRAME\_MSG\_CLASS\_IDX

**Definition** protocol.h:24

[ubx\_cfg\_parity](modem_2ubx_2protocol_8h.md#a2e5de1479afbcf20caa3300282bb0d1a)

ubx\_cfg\_parity

**Definition** protocol.h:218

[UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_EVEN](modem_2ubx_2protocol_8h.md#a2e5de1479afbcf20caa3300282bb0d1aa1ef24c67f4e90f7c6fb011ec433ebb68)

@ UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_EVEN

**Definition** protocol.h:219

[UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_NONE](modem_2ubx_2protocol_8h.md#a2e5de1479afbcf20caa3300282bb0d1aa46b4ba80de7ca4c9d1ea403dd6efb385)

@ UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_NONE

**Definition** protocol.h:221

[UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_ODD](modem_2ubx_2protocol_8h.md#a2e5de1479afbcf20caa3300282bb0d1aa5db544370f64f19224e9243eae0942ac)

@ UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_ODD

**Definition** protocol.h:220

[ubx\_fix\_mode](modem_2ubx_2protocol_8h.md#a342c0d62cf874ccb8b657ce85d91efe0)

ubx\_fix\_mode

**Definition** protocol.h:264

[UBX\_FIX\_MODE\_AUTO](modem_2ubx_2protocol_8h.md#a342c0d62cf874ccb8b657ce85d91efe0a1e324c97e68e6d7ce35feb4ffe2ca617)

@ UBX\_FIX\_MODE\_AUTO

**Definition** protocol.h:267

[UBX\_FIX\_MODE\_2D\_ONLY](modem_2ubx_2protocol_8h.md#a342c0d62cf874ccb8b657ce85d91efe0a29354369703a5e54ae7e49edfff886ff)

@ UBX\_FIX\_MODE\_2D\_ONLY

**Definition** protocol.h:265

[UBX\_FIX\_MODE\_3D\_ONLY](modem_2ubx_2protocol_8h.md#a342c0d62cf874ccb8b657ce85d91efe0aa60a16ce7e100e06e0bab9a3922003a6)

@ UBX\_FIX\_MODE\_3D\_ONLY

**Definition** protocol.h:266

[ubx\_utc\_standard](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23)

ubx\_utc\_standard

**Definition** protocol.h:270

[UBX\_UTC\_STANDARD\_GPS](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23a34b4b516760245d0a5bbfcbb5937d74c)

@ UBX\_UTC\_STANDARD\_GPS

**Definition** protocol.h:272

[UBX\_UTC\_STANDARD\_GALILEO](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23a6fe85d7688c6730a492981fdc4623c67)

@ UBX\_UTC\_STANDARD\_GALILEO

**Definition** protocol.h:273

[UBX\_UTC\_STANDARD\_AUTOMATIC](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23a8bc6c6397d5bc342ebe0ea36522e96a5)

@ UBX\_UTC\_STANDARD\_AUTOMATIC

**Definition** protocol.h:271

[UBX\_UTC\_STANDARD\_BEIDOU](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23a8eeae948253c11b7f097dd06896e66f8)

@ UBX\_UTC\_STANDARD\_BEIDOU

**Definition** protocol.h:275

[UBX\_UTC\_STANDARD\_GLONASS](modem_2ubx_2protocol_8h.md#a359b0f88d3769af43c2b1699eb172f23ab6c294e0f55696a8c90ec8211673ca80)

@ UBX\_UTC\_STANDARD\_GLONASS

**Definition** protocol.h:274

[ubx\_msg\_id\_cfg](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7)

ubx\_msg\_id\_cfg

**Definition** protocol.h:168

[UBX\_MSG\_ID\_CFG\_NAV5](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7a036303b6caf601b73bfb48b3a7423309)

@ UBX\_MSG\_ID\_CFG\_NAV5

**Definition** protocol.h:173

[UBX\_MSG\_ID\_CFG\_VAL\_SET](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3)

@ UBX\_MSG\_ID\_CFG\_VAL\_SET

**Definition** protocol.h:174

[UBX\_MSG\_ID\_CFG\_PRT](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7a871b880c791ad49c55164856ac4f83f9)

@ UBX\_MSG\_ID\_CFG\_PRT

**Definition** protocol.h:169

[UBX\_MSG\_ID\_CFG\_RATE](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7a89a96eb89044b208d3a6c29fc273fa26)

@ UBX\_MSG\_ID\_CFG\_RATE

**Definition** protocol.h:172

[UBX\_MSG\_ID\_CFG\_VAL\_GET](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7aa31397b2154b0f1f9b1e906c91a6bc8c)

@ UBX\_MSG\_ID\_CFG\_VAL\_GET

**Definition** protocol.h:175

[UBX\_MSG\_ID\_CFG\_MSG](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7ace6e98ad1c1ac7232327d42b0f4302ef)

@ UBX\_MSG\_ID\_CFG\_MSG

**Definition** protocol.h:170

[UBX\_MSG\_ID\_CFG\_RST](modem_2ubx_2protocol_8h.md#a3cf04300758f1802e0703428707035d7ad2c8bf68306ca6bb22e88c5c6d957453)

@ UBX\_MSG\_ID\_CFG\_RST

**Definition** protocol.h:171

[ubx\_cfg\_rst\_start\_mode](modem_2ubx_2protocol_8h.md#a43766ad4c0fd1d31fd547c090e3f39b6)

ubx\_cfg\_rst\_start\_mode

**Definition** protocol.h:303

[UBX\_CFG\_RST\_WARM\_START](modem_2ubx_2protocol_8h.md#a43766ad4c0fd1d31fd547c090e3f39b6a1621ed3281429f96fc598d90cc388c95)

@ UBX\_CFG\_RST\_WARM\_START

**Definition** protocol.h:305

[UBX\_CFG\_RST\_HOT\_START](modem_2ubx_2protocol_8h.md#a43766ad4c0fd1d31fd547c090e3f39b6a67b9cba109cc8f57a38c41b1d521e3c7)

@ UBX\_CFG\_RST\_HOT\_START

**Definition** protocol.h:304

[UBX\_CFG\_RST\_COLD\_START](modem_2ubx_2protocol_8h.md#a43766ad4c0fd1d31fd547c090e3f39b6aaef8449ed29d6dd76bdd34157d873896)

@ UBX\_CFG\_RST\_COLD\_START

**Definition** protocol.h:306

[ubx\_calc\_checksum](modem_2ubx_2protocol_8h.md#a450f46250ef486af4f933e69ddbb42d2)

static uint16\_t ubx\_calc\_checksum(const struct ubx\_frame \*frame, size\_t len)

**Definition** protocol.h:407

[UBX\_FRAME\_SZ](modem_2ubx_2protocol_8h.md#a4c64b9118da471baa6a7a88ee345bf66)

#define UBX\_FRAME\_SZ(payload\_size)

**Definition** protocol.h:17

[ubx\_msg\_id\_nmea\_pubx](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582)

ubx\_msg\_id\_nmea\_pubx

**Definition** protocol.h:388

[UBX\_MSG\_ID\_NMEA\_PUBX\_CONFIG](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582a43616a8ad2465c7521aa9ed28460cf57)

@ UBX\_MSG\_ID\_NMEA\_PUBX\_CONFIG

**Definition** protocol.h:389

[UBX\_MSG\_ID\_NMEA\_PUBX\_POSITION](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582a61cbc043ccd0a96ba2327d7bd95189c6)

@ UBX\_MSG\_ID\_NMEA\_PUBX\_POSITION

**Definition** protocol.h:390

[UBX\_MSG\_ID\_NMEA\_PUBX\_SVSTATUS](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582a73aeb813a098d600dfb60561bc042e2a)

@ UBX\_MSG\_ID\_NMEA\_PUBX\_SVSTATUS

**Definition** protocol.h:392

[UBX\_MSG\_ID\_NMEA\_PUBX\_TIME](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582a9f36e6c7688a62737beb203e82de91ef)

@ UBX\_MSG\_ID\_NMEA\_PUBX\_TIME

**Definition** protocol.h:393

[UBX\_MSG\_ID\_NMEA\_PUBX\_RATE](modem_2ubx_2protocol_8h.md#a58dc8b84784731500aa7f55afeb7e582af5ccdcc3eed53b0906b83667443e3667)

@ UBX\_MSG\_ID\_NMEA\_PUBX\_RATE

**Definition** protocol.h:391

[ubx\_cfg\_rst\_mode](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896)

ubx\_cfg\_rst\_mode

**Definition** protocol.h:309

[UBX\_CFG\_RST\_MODE\_GNSS\_STOP](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896a0e9177345e82ad614c1ab4c8b52b9265)

@ UBX\_CFG\_RST\_MODE\_GNSS\_STOP

**Definition** protocol.h:312

[UBX\_CFG\_RST\_MODE\_SW](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896a7fd6f4b7557dfa6511dcb6354963d342)

@ UBX\_CFG\_RST\_MODE\_SW

**Definition** protocol.h:311

[UBX\_CFG\_RST\_MODE\_HW](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896ac02d28b95ef601af32dc898e35ad252e)

@ UBX\_CFG\_RST\_MODE\_HW

**Definition** protocol.h:310

[UBX\_CFG\_RST\_MODE\_GNSS\_START](modem_2ubx_2protocol_8h.md#a5cc2a8f42fd62032afa3cd7687452896aca25f86cc1d85c60b1d67509d0e9506b)

@ UBX\_CFG\_RST\_MODE\_GNSS\_START

**Definition** protocol.h:313

[ubx\_cfg\_rate\_time\_ref](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952e)

ubx\_cfg\_rate\_time\_ref

**Definition** protocol.h:322

[UBX\_CFG\_RATE\_TIME\_REF\_BEIDOU](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952ea30f66599c483f622607f0b13ad0451f8)

@ UBX\_CFG\_RATE\_TIME\_REF\_BEIDOU

**Definition** protocol.h:326

[UBX\_CFG\_RATE\_TIME\_REF\_GLONASS](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952ea519dc8f11c80b5a08771fbc36c70fbb8)

@ UBX\_CFG\_RATE\_TIME\_REF\_GLONASS

**Definition** protocol.h:325

[UBX\_CFG\_RATE\_TIME\_REF\_NAVIC](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952ea5be3c906a6c528f65575990041b7e6ce)

@ UBX\_CFG\_RATE\_TIME\_REF\_NAVIC

**Definition** protocol.h:328

[UBX\_CFG\_RATE\_TIME\_REF\_GPS](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952ea7a2d00bdb7fef5ff7da1d3a682a1b82e)

@ UBX\_CFG\_RATE\_TIME\_REF\_GPS

**Definition** protocol.h:324

[UBX\_CFG\_RATE\_TIME\_REF\_GALILEO](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952eab7ed326b5da1087afb8d531d97bb9f16)

@ UBX\_CFG\_RATE\_TIME\_REF\_GALILEO

**Definition** protocol.h:327

[UBX\_CFG\_RATE\_TIME\_REF\_UTC](modem_2ubx_2protocol_8h.md#a621d2fae9721b6dc62a71801f3b7952eacc3989fab9e22270c389b0318bbe45ea)

@ UBX\_CFG\_RATE\_TIME\_REF\_UTC

**Definition** protocol.h:323

[ubx\_gnss\_id](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690)

ubx\_gnss\_id

**Definition** protocol.h:136

[UBX\_GNSS\_ID\_QZSS](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690a2dad67829bb51786024771c0d5a6d103)

@ UBX\_GNSS\_ID\_QZSS

**Definition** protocol.h:141

[UBX\_GNSS\_ID\_SBAS](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690a31a403a2013dc9da3da56366fa95f19b)

@ UBX\_GNSS\_ID\_SBAS

**Definition** protocol.h:138

[UBX\_GNSS\_ID\_GLONASS](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690a4e14cf64a03e9d37af198870b0616497)

@ UBX\_GNSS\_ID\_GLONASS

**Definition** protocol.h:142

[UBX\_GNSS\_ID\_GALILEO](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690a931ed807a91dd1f0e6e2cfa013860cbe)

@ UBX\_GNSS\_ID\_GALILEO

**Definition** protocol.h:139

[UBX\_GNSS\_ID\_BEIDOU](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690ac3f1631647cfd0246be61fc78549a9f7)

@ UBX\_GNSS\_ID\_BEIDOU

**Definition** protocol.h:140

[UBX\_GNSS\_ID\_GPS](modem_2ubx_2protocol_8h.md#a6711a33292bf25327950406b96585690adca8434b24978430d03939b81d76fbb9)

@ UBX\_GNSS\_ID\_GPS

**Definition** protocol.h:137

[ubx\_cfg\_char\_len](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78a)

ubx\_cfg\_char\_len

**Definition** protocol.h:211

[UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_5](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78aa019364b4a4482098acc0d7821b456b83)

@ UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_5

**Definition** protocol.h:212

[UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_8](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78aae7769c1dd298aabbad37ddaf6260eb4d)

@ UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_8

**Definition** protocol.h:215

[UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_7](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78aaeacece1ca309918fa3abe7a02911f5ca)

@ UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_7

**Definition** protocol.h:214

[UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_6](modem_2ubx_2protocol_8h.md#a887b1fa6af0d6d08cc51ed65de64a78aaeea043882f976e34008f261e1b2ee5ac)

@ UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_6

**Definition** protocol.h:213

[ubx\_msg\_id\_nav](modem_2ubx_2protocol_8h.md#a8a935ea7debb4ac73ea99c98d6ef4d3b)

ubx\_msg\_id\_nav

**Definition** protocol.h:63

[UBX\_MSG\_ID\_NAV\_PVT](modem_2ubx_2protocol_8h.md#a8a935ea7debb4ac73ea99c98d6ef4d3ba8f887b777e29fc05107ac406d4a87458)

@ UBX\_MSG\_ID\_NAV\_PVT

**Definition** protocol.h:64

[UBX\_MSG\_ID\_NAV\_SAT](modem_2ubx_2protocol_8h.md#a8a935ea7debb4ac73ea99c98d6ef4d3bae87d4355340186b8a049346e3076f9ae)

@ UBX\_MSG\_ID\_NAV\_SAT

**Definition** protocol.h:65

[ubx\_cfg\_stop\_bits](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4c)

ubx\_cfg\_stop\_bits

**Definition** protocol.h:224

[UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_1\_5](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4ca06c8d5338db83ce4a74a92228f04ffb1)

@ UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_1\_5

**Definition** protocol.h:226

[UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_0\_5](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4ca461834aa0d5d6ddec370ecd247e330e6)

@ UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_0\_5

**Definition** protocol.h:228

[UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_2](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4caea0ef9695c70807a5bdfb1725f31ea3f)

@ UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_2

**Definition** protocol.h:227

[UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_1](modem_2ubx_2protocol_8h.md#a94709ee4f4afe0194790893251ee2b4caf762dc50babaacd4cbb1ce753a8c0ae9)

@ UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_1

**Definition** protocol.h:225

[ubx\_dyn\_model](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561f)

ubx\_dyn\_model

**Definition** protocol.h:251

[UBX\_DYN\_MODEL\_WRIST](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa172bc7d2ed80cadb4077ae42233764b2)

@ UBX\_DYN\_MODEL\_WRIST

**Definition** protocol.h:260

[UBX\_DYN\_MODEL\_AIRBORNE\_2G](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa1a39257d816910b26f2323b61a278519)

@ UBX\_DYN\_MODEL\_AIRBORNE\_2G

**Definition** protocol.h:258

[UBX\_DYN\_MODEL\_STATIONARY](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa4f147b313644dba74c95930038201cf7)

@ UBX\_DYN\_MODEL\_STATIONARY

**Definition** protocol.h:253

[UBX\_DYN\_MODEL\_PORTABLE](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa59c3bbc8cb2a44e26920adbe0251375b)

@ UBX\_DYN\_MODEL\_PORTABLE

**Definition** protocol.h:252

[UBX\_DYN\_MODEL\_SEA](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa6d89a732b306e21feeaee51cdbcc0bed)

@ UBX\_DYN\_MODEL\_SEA

**Definition** protocol.h:256

[UBX\_DYN\_MODEL\_AUTOMOTIVE](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa736709e926d95754fef9260c596530e2)

@ UBX\_DYN\_MODEL\_AUTOMOTIVE

**Definition** protocol.h:255

[UBX\_DYN\_MODEL\_PEDESTRIAN](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa8a2a4bb1bb5b7f69960fdcde374f2ee6)

@ UBX\_DYN\_MODEL\_PEDESTRIAN

**Definition** protocol.h:254

[UBX\_DYN\_MODEL\_AIRBORNE\_1G](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fa9bb36ad38aca4f118fe1bdc2f0351476)

@ UBX\_DYN\_MODEL\_AIRBORNE\_1G

**Definition** protocol.h:257

[UBX\_DYN\_MODEL\_BIKE](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561faa062bfc1af7cc119d025dee309ac1d25)

@ UBX\_DYN\_MODEL\_BIKE

**Definition** protocol.h:261

[UBX\_DYN\_MODEL\_AIRBORNE\_4G](modem_2ubx_2protocol_8h.md#a9e5e9af7a281e53f2b950089ee66561fae4640365810ae80e8c24507fd7279f3d)

@ UBX\_DYN\_MODEL\_AIRBORNE\_4G

**Definition** protocol.h:259

[ubx\_msg\_id\_nmea\_std](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6c)

ubx\_msg\_id\_nmea\_std

**Definition** protocol.h:366

[UBX\_MSG\_ID\_NMEA\_STD\_GGA](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca07aa8c55e3504c0d19b1e123f4d2e7c7)

@ UBX\_MSG\_ID\_NMEA\_STD\_GGA

**Definition** protocol.h:370

[UBX\_MSG\_ID\_NMEA\_STD\_GLQ](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca263a724b491a6303d5486828a49a8961)

@ UBX\_MSG\_ID\_NMEA\_STD\_GLQ

**Definition** protocol.h:372

[UBX\_MSG\_ID\_NMEA\_STD\_GSV](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca2a5cc3b49abc9be0c6bbab0a9963ba03)

@ UBX\_MSG\_ID\_NMEA\_STD\_GSV

**Definition** protocol.h:379

[UBX\_MSG\_ID\_NMEA\_STD\_GPQ](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca39492ba0c78d0290819b9410e2e55781)

@ UBX\_MSG\_ID\_NMEA\_STD\_GPQ

**Definition** protocol.h:375

[UBX\_MSG\_ID\_NMEA\_STD\_GBQ](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca5174a26b3b79356bf06402de46bc0774)

@ UBX\_MSG\_ID\_NMEA\_STD\_GBQ

**Definition** protocol.h:368

[UBX\_MSG\_ID\_NMEA\_STD\_VLW](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca58ad56a546a2df6c9359927375da9904)

@ UBX\_MSG\_ID\_NMEA\_STD\_VLW

**Definition** protocol.h:383

[UBX\_MSG\_ID\_NMEA\_STD\_VTG](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca5c12f57e0b4de16d09fc42f23740908b)

@ UBX\_MSG\_ID\_NMEA\_STD\_VTG

**Definition** protocol.h:384

[UBX\_MSG\_ID\_NMEA\_STD\_GLL](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca6435225efac8c7ef6e336a84fa2e8932)

@ UBX\_MSG\_ID\_NMEA\_STD\_GLL

**Definition** protocol.h:371

[UBX\_MSG\_ID\_NMEA\_STD\_GRS](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca7f1d764aa078c284c575ec610d4f4853)

@ UBX\_MSG\_ID\_NMEA\_STD\_GRS

**Definition** protocol.h:376

[UBX\_MSG\_ID\_NMEA\_STD\_RMC](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca8787502b2d9a14d2ce79b1ce1713d6f3)

@ UBX\_MSG\_ID\_NMEA\_STD\_RMC

**Definition** protocol.h:380

[UBX\_MSG\_ID\_NMEA\_STD\_THS](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca884ab2ce56a1f7a08d4b9d06b944ad37)

@ UBX\_MSG\_ID\_NMEA\_STD\_THS

**Definition** protocol.h:381

[UBX\_MSG\_ID\_NMEA\_STD\_GST](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6ca99b8f62b1d204b335a06ed6f3ef214e6)

@ UBX\_MSG\_ID\_NMEA\_STD\_GST

**Definition** protocol.h:378

[UBX\_MSG\_ID\_NMEA\_STD\_GNQ](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6caa2c68fe9d01bc4acf3054d667f3e2a77)

@ UBX\_MSG\_ID\_NMEA\_STD\_GNQ

**Definition** protocol.h:373

[UBX\_MSG\_ID\_NMEA\_STD\_DTM](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cac84f9ad61c85bbce60e680639c3d88ad)

@ UBX\_MSG\_ID\_NMEA\_STD\_DTM

**Definition** protocol.h:367

[UBX\_MSG\_ID\_NMEA\_STD\_TXT](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cad58d4ac5b57cbdd42d360560cc16fc0e)

@ UBX\_MSG\_ID\_NMEA\_STD\_TXT

**Definition** protocol.h:382

[UBX\_MSG\_ID\_NMEA\_STD\_GSA](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cae3c6e42e75e69a34d7017d2f2aa3c70d)

@ UBX\_MSG\_ID\_NMEA\_STD\_GSA

**Definition** protocol.h:377

[UBX\_MSG\_ID\_NMEA\_STD\_ZDA](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cae6a2501b586793e75cdd0085170a9a27)

@ UBX\_MSG\_ID\_NMEA\_STD\_ZDA

**Definition** protocol.h:385

[UBX\_MSG\_ID\_NMEA\_STD\_GBS](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6caef6c925e20f072665bf55e435d37a6ac)

@ UBX\_MSG\_ID\_NMEA\_STD\_GBS

**Definition** protocol.h:369

[UBX\_MSG\_ID\_NMEA\_STD\_GNS](modem_2ubx_2protocol_8h.md#aa221b68c53f25634d9f2f435f28c1a6cafea982067c784c47ae5b1ad7e91b4191)

@ UBX\_MSG\_ID\_NMEA\_STD\_GNS

**Definition** protocol.h:374

[ubx\_frame\_encode](modem_2ubx_2protocol_8h.md#acdc0d9b7d25df6aba6bb091e7034f5ba)

static int ubx\_frame\_encode(uint8\_t class, uint8\_t id, const uint8\_t \*payload, size\_t payload\_len, uint8\_t \*buf, size\_t buf\_len)

**Definition** protocol.h:426

[ubx\_class\_id](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18)

ubx\_class\_id

**Definition** protocol.h:47

[UBX\_CLASS\_ID\_NMEA\_PUBX](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a0d9d5044c9df2a6b61b7a46a4f24e895)

@ UBX\_CLASS\_ID\_NMEA\_PUBX

**Definition** protocol.h:60

[UBX\_CLASS\_ID\_LOG](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a1e35a224f4809d3a59d0f1570bf382bb)

@ UBX\_CLASS\_ID\_LOG

**Definition** protocol.h:57

[UBX\_CLASS\_ID\_MGA](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a418aca13d3bd1608869494d26559e52f)

@ UBX\_CLASS\_ID\_MGA

**Definition** protocol.h:56

[UBX\_CLASS\_ID\_RXM](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a5e4eaf66a7356e73b4c6e4949160f321)

@ UBX\_CLASS\_ID\_RXM

**Definition** protocol.h:49

[UBX\_CLASS\_ID\_SEC](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a760de1a9f06cc6d4832da868d01702c4)

@ UBX\_CLASS\_ID\_SEC

**Definition** protocol.h:58

[UBX\_CLASS\_ID\_NMEA\_STD](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a7e7c3645f46ba3c2e8329ae3a9eeaa79)

@ UBX\_CLASS\_ID\_NMEA\_STD

**Definition** protocol.h:59

[UBX\_CLASS\_ID\_INF](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a898b493832d06586cf48f9a2545651d0)

@ UBX\_CLASS\_ID\_INF

**Definition** protocol.h:50

[UBX\_CLASS\_ID\_TIM](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a8c700fd2062d8dc51c5e4b28c98c6cf0)

@ UBX\_CLASS\_ID\_TIM

**Definition** protocol.h:55

[UBX\_CLASS\_ID\_NAV](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a8f46002e33dddab6782bad93ab3fd8b1)

@ UBX\_CLASS\_ID\_NAV

**Definition** protocol.h:48

[UBX\_CLASS\_ID\_UPD](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18aba0a811e14f9e87bd47bfbeaad24e11b)

@ UBX\_CLASS\_ID\_UPD

**Definition** protocol.h:53

[UBX\_CLASS\_ID\_MON](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18ac9200dedb25cfa03b80f4336e86db5ed)

@ UBX\_CLASS\_ID\_MON

**Definition** protocol.h:54

[UBX\_CLASS\_ID\_ACK](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18aee43a865c5815ce058261f5f0550fa2b)

@ UBX\_CLASS\_ID\_ACK

**Definition** protocol.h:51

[UBX\_CLASS\_ID\_CFG](modem_2ubx_2protocol_8h.md#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c)

@ UBX\_CLASS\_ID\_CFG

**Definition** protocol.h:52

[ubx\_cfg\_val\_ver](modem_2ubx_2protocol_8h.md#ad7e0ffe55e8dbd97caa5bc089d33540c)

ubx\_cfg\_val\_ver

**Definition** protocol.h:337

[UBX\_CFG\_VAL\_VER\_SIMPLE](modem_2ubx_2protocol_8h.md#ad7e0ffe55e8dbd97caa5bc089d33540ca1fe2554bbbf05c86d3f9b0bc50927c1b)

@ UBX\_CFG\_VAL\_VER\_SIMPLE

**Definition** protocol.h:338

[UBX\_CFG\_VAL\_VER\_TRANSACTION](modem_2ubx_2protocol_8h.md#ad7e0ffe55e8dbd97caa5bc089d33540caca3b7f2a39ff93b91b8317245e8375ab)

@ UBX\_CFG\_VAL\_VER\_TRANSACTION

**Definition** protocol.h:339

[UBX\_PREAMBLE\_SYNC\_CHAR\_2](modem_2ubx_2protocol_8h.md#ad8d6229db563db619d4f0a9f225fb640)

#define UBX\_PREAMBLE\_SYNC\_CHAR\_2

**Definition** protocol.h:20

[ubx\_cfg\_port\_id](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baa)

ubx\_cfg\_port\_id

**Definition** protocol.h:204

[UBX\_CFG\_PORT\_ID\_USB](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baaa3af5f6c24fade976d4ece339e9240114)

@ UBX\_CFG\_PORT\_ID\_USB

**Definition** protocol.h:207

[UBX\_CFG\_PORT\_ID\_DDC](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baaa5c7c1a24670995305bcb8e98cfd1fa19)

@ UBX\_CFG\_PORT\_ID\_DDC

**Definition** protocol.h:205

[UBX\_CFG\_PORT\_ID\_SPI](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baaaa0ee1de6e26bb0585f24fddbe3d7ec9a)

@ UBX\_CFG\_PORT\_ID\_SPI

**Definition** protocol.h:208

[UBX\_CFG\_PORT\_ID\_UART](modem_2ubx_2protocol_8h.md#adb6a6e16f193bc70840b2dd12dbc9baaaccb591a437d0ed7cca8888f41b855efb)

@ UBX\_CFG\_PORT\_ID\_UART

**Definition** protocol.h:206

[ubx\_nav\_sat\_health](modem_2ubx_2protocol_8h.md#afbba8ada09d6c6489d52a3b9dc31725f)

ubx\_nav\_sat\_health

**Definition** protocol.h:130

[UBX\_NAV\_SAT\_HEALTH\_UNKNOWN](modem_2ubx_2protocol_8h.md#afbba8ada09d6c6489d52a3b9dc31725fa3661b89022659975720d3a022b21f194)

@ UBX\_NAV\_SAT\_HEALTH\_UNKNOWN

**Definition** protocol.h:131

[UBX\_NAV\_SAT\_HEALTH\_HEALTHY](modem_2ubx_2protocol_8h.md#afbba8ada09d6c6489d52a3b9dc31725fa7dcaa32f001d1a7b5b071cdf7621081e)

@ UBX\_NAV\_SAT\_HEALTH\_HEALTHY

**Definition** protocol.h:132

[UBX\_NAV\_SAT\_HEALTH\_UNHEALTHY](modem_2ubx_2protocol_8h.md#afbba8ada09d6c6489d52a3b9dc31725fa95ea7c01a987a1e334f41c79642b8139)

@ UBX\_NAV\_SAT\_HEALTH\_UNHEALTHY

**Definition** protocol.h:133

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[ubx\_ack](structubx__ack.md)

**Definition** protocol.h:183

[ubx\_ack::id](structubx__ack.md#ab68abe2083b8446a2e3ffc4b603ac47d)

uint8\_t id

**Definition** protocol.h:185

[ubx\_cfg\_msg\_rate](structubx__cfg__msg__rate.md)

**Definition** protocol.h:396

[ubx\_cfg\_msg\_rate::rate](structubx__cfg__msg__rate.md#a7a030b3e70356b899ed7284e750041b0)

uint8\_t rate

**Definition** protocol.h:399

[ubx\_cfg\_msg\_rate::id](structubx__cfg__msg__rate.md#aee7d34d68f3665c665f8ae4bc6d1a04a)

uint8\_t id

**Definition** protocol.h:398

[ubx\_cfg\_nav5](structubx__cfg__nav5.md)

**Definition** protocol.h:281

[ubx\_cfg\_nav5::p\_acc](structubx__cfg__nav5.md#a19d69c52edac0f65e2892b4c476d5a76)

uint16\_t p\_acc

**Definition** protocol.h:291

[ubx\_cfg\_nav5::min\_elev](structubx__cfg__nav5.md#a2e7353d4ef2f0b3eef4ae3d1cc2be5ed)

int8\_t min\_elev

**Definition** protocol.h:287

[ubx\_cfg\_nav5::dgnss\_timeout](structubx__cfg__nav5.md#a2ee4fc58054c5f049890914c73089c99)

uint8\_t dgnss\_timeout

**Definition** protocol.h:294

[ubx\_cfg\_nav5::t\_dop](structubx__cfg__nav5.md#a4d8537de40aa5c98ae2e2183da9d44c3)

uint16\_t t\_dop

**Definition** protocol.h:290

[ubx\_cfg\_nav5::apply](structubx__cfg__nav5.md#a564548f9609493061e995219f6397060)

uint16\_t apply

**Definition** protocol.h:282

[ubx\_cfg\_nav5::static\_hold\_thresh](structubx__cfg__nav5.md#a5afd803452c65c4f03b122c9ff59cf2b)

uint8\_t static\_hold\_thresh

**Definition** protocol.h:293

[ubx\_cfg\_nav5::static\_hold\_max\_dist](structubx__cfg__nav5.md#a6108faff3832cab3d734020c030c5c6c)

uint16\_t static\_hold\_max\_dist

**Definition** protocol.h:298

[ubx\_cfg\_nav5::cno\_thresh\_num\_svs](structubx__cfg__nav5.md#a648e22442293b24b2aa8b264a78b9bd2)

uint8\_t cno\_thresh\_num\_svs

**Definition** protocol.h:295

[ubx\_cfg\_nav5::dyn\_model](structubx__cfg__nav5.md#a70f931b76bcd7a07a225648a15e73493)

uint8\_t dyn\_model

**Definition** protocol.h:283

[ubx\_cfg\_nav5::p\_dop](structubx__cfg__nav5.md#a7c7f4338463e4d0c8040971ec31dc92c)

uint16\_t p\_dop

**Definition** protocol.h:289

[ubx\_cfg\_nav5::fix\_mode](structubx__cfg__nav5.md#aab1b8aec77c186c576be839f728bba70)

uint8\_t fix\_mode

**Definition** protocol.h:284

[ubx\_cfg\_nav5::reserved1](structubx__cfg__nav5.md#ab6b5cd2ef8db8c281f77c6684f6f8c0c)

uint8\_t reserved1[2]

**Definition** protocol.h:297

[ubx\_cfg\_nav5::fixed\_alt\_var](structubx__cfg__nav5.md#abb48bda50e725eb8c2973518b468916f)

uint32\_t fixed\_alt\_var

**Definition** protocol.h:286

[ubx\_cfg\_nav5::cno\_thresh](structubx__cfg__nav5.md#abf2a3de97f8d9cade6ec18408452938a)

uint8\_t cno\_thresh

**Definition** protocol.h:296

[ubx\_cfg\_nav5::reserved2](structubx__cfg__nav5.md#ac3d21a048e77c404bcfa180af2e41992)

uint8\_t reserved2[5]

**Definition** protocol.h:300

[ubx\_cfg\_nav5::dr\_limit](structubx__cfg__nav5.md#ace7d12cf8f63904274e658a6afe149d5)

uint8\_t dr\_limit

**Definition** protocol.h:288

[ubx\_cfg\_nav5::t\_acc](structubx__cfg__nav5.md#ad78a8828482ce26597f80f5e5a548afd)

uint16\_t t\_acc

**Definition** protocol.h:292

[ubx\_cfg\_nav5::utc\_standard](structubx__cfg__nav5.md#ae0ecd871977ad119009cf1a2ac617327)

uint8\_t utc\_standard

**Definition** protocol.h:299

[ubx\_cfg\_nav5::fixed\_alt](structubx__cfg__nav5.md#af915a692066df1855c270e106c1981ca)

int32\_t fixed\_alt

**Definition** protocol.h:285

[ubx\_cfg\_prt](structubx__cfg__prt.md)

**Definition** protocol.h:239

[ubx\_cfg\_prt::rx\_ready\_pin](structubx__cfg__prt.md#a1d4df224a3a9e7e6031a418745ee4e95)

uint16\_t rx\_ready\_pin

**Definition** protocol.h:242

[ubx\_cfg\_prt::out\_proto\_mask](structubx__cfg__prt.md#a1f4f3ab473e80648043b792bc4d5022f)

uint16\_t out\_proto\_mask

**Definition** protocol.h:246

[ubx\_cfg\_prt::mode](structubx__cfg__prt.md#a571753eb8aba5610fb7bc3546b7bfce9)

uint32\_t mode

**Definition** protocol.h:243

[ubx\_cfg\_prt::flags](structubx__cfg__prt.md#a836be3302c1e038fbc09712242a51e69)

uint16\_t flags

**Definition** protocol.h:247

[ubx\_cfg\_prt::in\_proto\_mask](structubx__cfg__prt.md#a960fd4543476b89b56f23dd29774b196)

uint16\_t in\_proto\_mask

**Definition** protocol.h:245

[ubx\_cfg\_prt::reserved1](structubx__cfg__prt.md#aba6bef46b7818a2396b77a0b1245ecc5)

uint8\_t reserved1

**Definition** protocol.h:241

[ubx\_cfg\_prt::baudrate](structubx__cfg__prt.md#ac83072a87e0b29b30e6406f4f61cf26d)

uint32\_t baudrate

**Definition** protocol.h:244

[ubx\_cfg\_prt::reserved2](structubx__cfg__prt.md#ad2bf468b82cc86ae1ce99c2fa129c231)

uint16\_t reserved2

**Definition** protocol.h:248

[ubx\_cfg\_prt::port\_id](structubx__cfg__prt.md#af5a445ab598a2b93e884c916fe13affc)

uint8\_t port\_id

**Definition** protocol.h:240

[ubx\_cfg\_rate](structubx__cfg__rate.md)

**Definition** protocol.h:331

[ubx\_cfg\_rate::time\_ref](structubx__cfg__rate.md#a444822a3a37dd51313bfc6968a3b4721)

uint16\_t time\_ref

**Definition** protocol.h:334

[ubx\_cfg\_rate::nav\_rate](structubx__cfg__rate.md#aafcbb36f844534c77e698dceccb2f5dc)

uint16\_t nav\_rate

**Definition** protocol.h:333

[ubx\_cfg\_rate::meas\_rate\_ms](structubx__cfg__rate.md#ae64d779c4a3fe255710be8f742f5b6c6)

uint16\_t meas\_rate\_ms

**Definition** protocol.h:332

[ubx\_cfg\_rst](structubx__cfg__rst.md)

**Definition** protocol.h:316

[ubx\_cfg\_rst::reset\_mode](structubx__cfg__rst.md#a1a63d295cf71e23a4afdb31637741b4f)

uint8\_t reset\_mode

**Definition** protocol.h:318

[ubx\_cfg\_rst::nav\_bbr\_mask](structubx__cfg__rst.md#a7d7e94ffc6aa9518a31b3f829a732362)

uint16\_t nav\_bbr\_mask

**Definition** protocol.h:317

[ubx\_cfg\_rst::reserved](structubx__cfg__rst.md#aa1f7a46662f14e498b8bce84fb349d33)

uint8\_t reserved

**Definition** protocol.h:319

[ubx\_cfg\_val\_hdr](structubx__cfg__val__hdr.md)

**Definition** protocol.h:342

[ubx\_cfg\_val\_hdr::ver](structubx__cfg__val__hdr.md#a4d7a91e9521428e5b528ced88b030cd3)

uint8\_t ver

**Definition** protocol.h:343

[ubx\_cfg\_val\_hdr::position](structubx__cfg__val__hdr.md#a6206dc714df9656cc37e0b802ab541b8)

uint16\_t position

**Definition** protocol.h:345

[ubx\_cfg\_val\_hdr::layer](structubx__cfg__val__hdr.md#aa835050e25c8db0a5a88954ff0def88c)

uint8\_t layer

**Definition** protocol.h:344

[ubx\_cfg\_val\_u16](structubx__cfg__val__u16.md)

**Definition** protocol.h:354

[ubx\_cfg\_val\_u16::hdr](structubx__cfg__val__u16.md#a32e877f1e2f60b209fbcdd057aa82c4f)

struct ubx\_cfg\_val\_hdr hdr

**Definition** protocol.h:355

[ubx\_cfg\_val\_u16::value](structubx__cfg__val__u16.md#a6226f1b8f4cb89cb318c07ff8ddcbbde)

uint16\_t value

**Definition** protocol.h:357

[ubx\_cfg\_val\_u16::key](structubx__cfg__val__u16.md#a87a9c181318e297935bb1eb65093d4a8)

uint32\_t key

**Definition** protocol.h:356

[ubx\_cfg\_val\_u32](structubx__cfg__val__u32.md)

**Definition** protocol.h:360

[ubx\_cfg\_val\_u32::value](structubx__cfg__val__u32.md#a2c1d446c7c8bef80052d2438fb998d58)

uint32\_t value

**Definition** protocol.h:363

[ubx\_cfg\_val\_u32::key](structubx__cfg__val__u32.md#ab02aa8d3b7039c06692a805aed30f246)

uint32\_t key

**Definition** protocol.h:362

[ubx\_cfg\_val\_u32::hdr](structubx__cfg__val__u32.md#adc51df7bc8a50e1ca8843067bb309ac9)

struct ubx\_cfg\_val\_hdr hdr

**Definition** protocol.h:361

[ubx\_cfg\_val\_u8](structubx__cfg__val__u8.md)

**Definition** protocol.h:348

[ubx\_cfg\_val\_u8::key](structubx__cfg__val__u8.md#a2c1cbf9a552608150eafc1f2d92b03b5)

uint32\_t key

**Definition** protocol.h:350

[ubx\_cfg\_val\_u8::value](structubx__cfg__val__u8.md#a325aaaf688433cab710d0c3e835fb9ed)

uint8\_t value

**Definition** protocol.h:351

[ubx\_cfg\_val\_u8::hdr](structubx__cfg__val__u8.md#a793646932ce054ab8561078981f57250)

struct ubx\_cfg\_val\_hdr hdr

**Definition** protocol.h:349

[ubx\_frame\_match](structubx__frame__match.md)

**Definition** protocol.h:38

[ubx\_frame\_match::len](structubx__frame__match.md#a36c5fd74bd6d506111b1ef2ac39cb68a)

uint16\_t len

**Definition** protocol.h:43

[ubx\_frame\_match::payload](structubx__frame__match.md#abbc954596995ca2dfe65de3e310e02a0)

struct ubx\_frame\_match::@352213364356211272240131006112257113241046164202 payload

[ubx\_frame\_match::id](structubx__frame__match.md#ae65eaf921576c61ad758bfedc56d89c6)

uint8\_t id

**Definition** protocol.h:40

[ubx\_frame\_match::buf](structubx__frame__match.md#af78f70c27f4334fd1dcaac72d9e4ece6)

uint8\_t \* buf

**Definition** protocol.h:42

[ubx\_frame](structubx__frame.md)

**Definition** protocol.h:29

[ubx\_frame::class](structubx__frame.md#a2dcc29a82e7dfff2d1e4194f1bc035e8)

uint8\_t class

**Definition** protocol.h:32

[ubx\_frame::id](structubx__frame.md#a4e578da5900365d498708f7a61d48ba4)

uint8\_t id

**Definition** protocol.h:33

[ubx\_frame::payload\_and\_checksum](structubx__frame.md#a70c465b5bd1e9837c253d78fb210f4ce)

uint8\_t payload\_and\_checksum[]

**Definition** protocol.h:35

[ubx\_frame::payload\_size](structubx__frame.md#a77b5030a6b95aef58b1c17f0368dd7ce)

uint16\_t payload\_size

**Definition** protocol.h:34

[ubx\_frame::preamble\_sync\_char\_2](structubx__frame.md#ac61fb72df7c1cd8a9bacb787071cb77d)

uint8\_t preamble\_sync\_char\_2

**Definition** protocol.h:31

[ubx\_frame::preamble\_sync\_char\_1](structubx__frame.md#acf80f38e8f26bb32848ae2978a1f87a1)

uint8\_t preamble\_sync\_char\_1

**Definition** protocol.h:30

[ubx\_mon\_gnss](structubx__mon__gnss.md)

**Definition** protocol.h:193

[ubx\_mon\_gnss::reserved1](structubx__mon__gnss.md#a045256bfbf8fe9b398ef77d10e00395a)

uint8\_t reserved1[3]

**Definition** protocol.h:201

[ubx\_mon\_gnss::default\_enabled](structubx__mon__gnss.md#a2b94264d40d0aa740b20d9fa9565d155)

uint8\_t default\_enabled

**Definition** protocol.h:197

[ubx\_mon\_gnss::simultaneous](structubx__mon__gnss.md#a34b9073dda3d6ad734109cea8ba5a0d2)

uint8\_t simultaneous

**Definition** protocol.h:200

[ubx\_mon\_gnss::supported](structubx__mon__gnss.md#a8f76d361c23ae4a94d29277be0aa36f8)

uint8\_t supported

**Definition** protocol.h:196

[ubx\_mon\_gnss::enabled](structubx__mon__gnss.md#ad09bcd6e739e385c275f8a1cae8725b3)

uint8\_t enabled

**Definition** protocol.h:198

[ubx\_mon\_gnss::selection](structubx__mon__gnss.md#ae004377f656dede9b0ebe98caeea588f)

struct ubx\_mon\_gnss::@224205002314270241172347203256350144274361054317 selection

[ubx\_mon\_gnss::ver](structubx__mon__gnss.md#aebcccc44a80ef3b327d7d479ccb5ebe5)

uint8\_t ver

**Definition** protocol.h:194

[ubx\_mon\_ver](structubx__mon__ver.md)

**Definition** protocol.h:402

[ubx\_mon\_ver::hw\_ver](structubx__mon__ver.md#a07a2fdbe52fa48e9412f39bff1256318)

char hw\_ver[10]

**Definition** protocol.h:404

[ubx\_mon\_ver::sw\_ver](structubx__mon__ver.md#aa0495c27ac850d56ddaa92bc4689ba7f)

char sw\_ver[30]

**Definition** protocol.h:403

[ubx\_nav\_pvt](structubx__nav__pvt.md)

**Definition** protocol.h:86

[ubx\_nav\_pvt::second](structubx__nav__pvt.md#a10b14934d80d80d3c2f0c36866bd4a64)

uint8\_t second

**Definition** protocol.h:94

[ubx\_nav\_pvt::tacc](structubx__nav__pvt.md#a1753595f0a3935449dee4d0c57e88a6e)

uint32\_t tacc

**Definition** protocol.h:96

[ubx\_nav\_pvt::vel\_east](structubx__nav__pvt.md#a17c628b0acca293f068b58eff32ae4dd)

int32\_t vel\_east

**Definition** protocol.h:111

[ubx\_nav\_pvt::minute](structubx__nav__pvt.md#a18b61263b433dc5f81c2becff9c6743c)

uint8\_t minute

**Definition** protocol.h:93

[ubx\_nav\_pvt::flags](structubx__nav__pvt.md#a1bdc3cb0e4a2b6bef1c4216963e5c29c)

uint8\_t flags

See ubx\_nav\_fix\_type.

**Definition** protocol.h:100

[ubx\_nav\_pvt::nano](structubx__nav__pvt.md#a1c21c3b882412f36f96c59cda1d948d9)

int32\_t nano

**Definition** protocol.h:97

[ubx\_nav\_pvt::vel\_north](structubx__nav__pvt.md#a1d50e696fa2684b55d04c652c85f2e16)

int32\_t vel\_north

**Definition** protocol.h:110

[ubx\_nav\_pvt::flags2](structubx__nav__pvt.md#a2ff7d8bcc13ee956d9535c61efefada6)

uint8\_t flags2

**Definition** protocol.h:101

[ubx\_nav\_pvt::latitude](structubx__nav__pvt.md#a34ec5fc41c4b323b4719803f1ff01bed)

int32\_t latitude

**Definition** protocol.h:105

[ubx\_nav\_pvt::ground\_speed](structubx__nav__pvt.md#a38a8612a53966a1d598bf6d17443da7d)

int32\_t ground\_speed

**Definition** protocol.h:113

[ubx\_nav\_pvt::flags3](structubx__nav__pvt.md#a39b72f654fc8130c611ac839189914ed)

uint16\_t flags3

**Definition** protocol.h:120

[ubx\_nav\_pvt::fix\_type](structubx__nav__pvt.md#a3b780d7b790b07a8ee23431969cbc318)

uint8\_t fix\_type

**Definition** protocol.h:99

[ubx\_nav\_pvt::itow](structubx__nav__pvt.md#a426086b12ff09fb8a00dd4623fea307e)

uint32\_t itow

**Definition** protocol.h:88

[ubx\_nav\_pvt::valid](structubx__nav__pvt.md#a450638fda7b9d1929145575e4c576ec1)

uint8\_t valid

**Definition** protocol.h:95

[ubx\_nav\_pvt::vel\_down](structubx__nav__pvt.md#a4958a6c11bd812477d11467ab3384161)

int32\_t vel\_down

**Definition** protocol.h:112

[ubx\_nav\_pvt::mag\_decl](structubx__nav__pvt.md#a4f63a0f15b823e5258fdb826d2636828)

int16\_t mag\_decl

**Definition** protocol.h:125

[ubx\_nav\_pvt::pdop](structubx__nav__pvt.md#a7e5dc3449e52a36cb2bc5841bbf6fec8)

uint16\_t pdop

Heading accuracy estimate (both motion and vehicle).

**Definition** protocol.h:119

[ubx\_nav\_pvt::reserved](structubx__nav__pvt.md#a80139f6d95bf943f5c6de6af1ea50e3e)

uint32\_t reserved

**Definition** protocol.h:121

[ubx\_nav\_pvt::year](structubx__nav__pvt.md#a84c6640806485f270b8d51d06cc49709)

uint16\_t year

**Definition** protocol.h:89

[ubx\_nav\_pvt::head\_vehicle](structubx__nav__pvt.md#a8fc4b24fb8ffde02d306bc1b6770b1d8)

int32\_t head\_vehicle

**Definition** protocol.h:122

[ubx\_nav\_pvt::speed\_acc](structubx__nav__pvt.md#a955d0f7927f68f540f2e9a2c91e46e79)

uint32\_t speed\_acc

**Definition** protocol.h:115

[ubx\_nav\_pvt::head\_acc](structubx__nav__pvt.md#aa332fc93448eb6b30ad8bbaa5760db5c)

uint32\_t head\_acc

**Definition** protocol.h:116

[ubx\_nav\_pvt::nav](structubx__nav__pvt.md#aa8b31a49c2844501505412da226872e1)

struct ubx\_nav\_pvt::@124110107202070056152323072100221212357171026061 nav

[ubx\_nav\_pvt::height](structubx__nav__pvt.md#ab0df156e9f8009bebfbbdb39c63c4191)

int32\_t height

**Definition** protocol.h:106

[ubx\_nav\_pvt::head\_motion](structubx__nav__pvt.md#abd97f003ba43b70ffea2e9fdf5702c4f)

int32\_t head\_motion

**Definition** protocol.h:114

[ubx\_nav\_pvt::magacc](structubx__nav__pvt.md#ac0265c113f01ae2bab8553eb7148e3ae)

uint16\_t magacc

**Definition** protocol.h:126

[ubx\_nav\_pvt::horiz\_acc](structubx__nav__pvt.md#acbb58f36eb572ce27b050a8c7540f91d)

uint32\_t horiz\_acc

**Definition** protocol.h:108

[ubx\_nav\_pvt::month](structubx__nav__pvt.md#ad90042dc5e00b91f004badcb0c3a5f4c)

uint8\_t month

**Definition** protocol.h:90

[ubx\_nav\_pvt::longitude](structubx__nav__pvt.md#ae47fc34dfd91687590bd96afe2fab091)

int32\_t longitude

**Definition** protocol.h:104

[ubx\_nav\_pvt::hmsl](structubx__nav__pvt.md#ae6ba97f3406b9fdbbf04c4bb3e744668)

int32\_t hmsl

**Definition** protocol.h:107

[ubx\_nav\_pvt::num\_sv](structubx__nav__pvt.md#aea613eb3d604d33120e82c569c5f10e9)

uint8\_t num\_sv

**Definition** protocol.h:103

[ubx\_nav\_pvt::day](structubx__nav__pvt.md#aeadb05fe45a3a0539c899129e40059fd)

uint8\_t day

**Definition** protocol.h:91

[ubx\_nav\_pvt::hour](structubx__nav__pvt.md#aeb710663626935d21c77a5cfe1030795)

uint8\_t hour

**Definition** protocol.h:92

[ubx\_nav\_pvt::vert\_acc](structubx__nav__pvt.md#af5b3e0e70b3470bd1686ddbfefb419f9)

uint32\_t vert\_acc

**Definition** protocol.h:109

[ubx\_nav\_sat::ubx\_nav\_sat\_info](structubx__nav__sat_1_1ubx__nav__sat__info.md)

**Definition** protocol.h:152

[ubx\_nav\_sat::ubx\_nav\_sat\_info::gnss\_id](structubx__nav__sat_1_1ubx__nav__sat__info.md#a04fc29e6cf9f1ff6f1f638ae633d5a11)

uint8\_t gnss\_id

**Definition** protocol.h:153

[ubx\_nav\_sat::ubx\_nav\_sat\_info::azimuth](structubx__nav__sat_1_1ubx__nav__sat__info.md#a3a50255230b6ed80bfa4eb8ff83acf89)

int16\_t azimuth

**Definition** protocol.h:157

[ubx\_nav\_sat::ubx\_nav\_sat\_info::pseu\_res](structubx__nav__sat_1_1ubx__nav__sat__info.md#a442709d1e9b43ae8c27606a5fb878c89)

int16\_t pseu\_res

**Definition** protocol.h:158

[ubx\_nav\_sat::ubx\_nav\_sat\_info::cno](structubx__nav__sat_1_1ubx__nav__sat__info.md#a83e6ba9e50cc24fc0d80de3947daf571)

uint8\_t cno

**Definition** protocol.h:155

[ubx\_nav\_sat::ubx\_nav\_sat\_info::elevation](structubx__nav__sat_1_1ubx__nav__sat__info.md#a9133131e06119371d14be09f99b24a8e)

int8\_t elevation

**Definition** protocol.h:156

[ubx\_nav\_sat::ubx\_nav\_sat\_info::sv\_id](structubx__nav__sat_1_1ubx__nav__sat__info.md#ab7ba4e9d36ab136c0bb8fde9b4f9b3e5)

uint8\_t sv\_id

**Definition** protocol.h:154

[ubx\_nav\_sat::ubx\_nav\_sat\_info::flags](structubx__nav__sat_1_1ubx__nav__sat__info.md#ac6872360564b383ce2cd5a061717c8fe)

uint32\_t flags

**Definition** protocol.h:159

[ubx\_nav\_sat](structubx__nav__sat.md)

**Definition** protocol.h:147

[ubx\_nav\_sat::reserved1](structubx__nav__sat.md#a6f5bf3da0f5633aa95ff4d736656cb21)

uint16\_t reserved1

**Definition** protocol.h:151

[ubx\_nav\_sat::version](structubx__nav__sat.md#a7204f8b1b28f3dc0970fa62567885cdc)

uint8\_t version

**Definition** protocol.h:149

[ubx\_nav\_sat::itow](structubx__nav__sat.md#aac587fd77fa832021ebca87e7897eb2e)

uint32\_t itow

**Definition** protocol.h:148

[ubx\_nav\_sat::sat](structubx__nav__sat.md#ade983d7b35cf81a6d769979f7cb5919d)

struct ubx\_nav\_sat::ubx\_nav\_sat\_info sat[]

[ubx\_nav\_sat::num\_sv](structubx__nav__sat.md#ae0bea798d815cc25e837e3fa394fb429)

uint8\_t num\_sv

**Definition** protocol.h:150

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ubx](dir_0a499179f9adf90767e72c7eb481b4fc.md)
- [protocol.h](modem_2ubx_2protocol_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
