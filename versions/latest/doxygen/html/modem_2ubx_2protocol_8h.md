---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/modem_2ubx_2protocol_8h.html
original_path: doxygen/html/modem_2ubx_2protocol_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

protocol.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/modem/ubx/checksum.h](checksum_8h_source.md)>`

[Go to the source code of this file.](modem_2ubx_2protocol_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ubx\_frame](structubx__frame.md) |
| struct | [ubx\_frame\_match](structubx__frame__match.md) |
| struct | [ubx\_nav\_pvt](structubx__nav__pvt.md) |
| struct | [ubx\_nav\_sat](structubx__nav__sat.md) |
| struct | [ubx\_nav\_sat::ubx\_nav\_sat\_info](structubx__nav__sat_1_1ubx__nav__sat__info.md) |
| struct | [ubx\_ack](structubx__ack.md) |
| struct | [ubx\_mon\_gnss](structubx__mon__gnss.md) |
| struct | [ubx\_cfg\_prt](structubx__cfg__prt.md) |
| struct | [ubx\_cfg\_nav5](structubx__cfg__nav5.md) |
| struct | [ubx\_cfg\_rst](structubx__cfg__rst.md) |
| struct | [ubx\_cfg\_rate](structubx__cfg__rate.md) |
| struct | [ubx\_cfg\_val\_hdr](structubx__cfg__val__hdr.md) |
| struct | [ubx\_cfg\_val\_u8](structubx__cfg__val__u8.md) |
| struct | [ubx\_cfg\_val\_u16](structubx__cfg__val__u16.md) |
| struct | [ubx\_cfg\_val\_u32](structubx__cfg__val__u32.md) |
| struct | [ubx\_cfg\_msg\_rate](structubx__cfg__msg__rate.md) |
| struct | [ubx\_mon\_ver](structubx__mon__ver.md) |

| Macros | |
| --- | --- |
| #define | [UBX\_FRAME\_HEADER\_SZ](#a1342f8e944fcd9f45fe94eef9bda307c)   6 |
| #define | [UBX\_FRAME\_FOOTER\_SZ](#aa0392f4a081c1077b4f235a757431aee)   2 |
| #define | [UBX\_FRAME\_SZ\_WITHOUT\_PAYLOAD](#a8e1aded66fd229f071c9d5e060a001a6)   ([UBX\_FRAME\_HEADER\_SZ](#a1342f8e944fcd9f45fe94eef9bda307c) + [UBX\_FRAME\_FOOTER\_SZ](#aa0392f4a081c1077b4f235a757431aee)) |
| #define | [UBX\_FRAME\_SZ](#a4c64b9118da471baa6a7a88ee345bf66)(payload\_size) |
| #define | [UBX\_PREAMBLE\_SYNC\_CHAR\_1](#a1693f3584605a0197076cba71c79b0df)   0xB5 |
| #define | [UBX\_PREAMBLE\_SYNC\_CHAR\_2](#ad8d6229db563db619d4f0a9f225fb640)   0x62 |
| #define | [UBX\_FRAME\_PREAMBLE\_SYNC\_CHAR\_1\_IDX](#a1b417ed30e090d3399f96c87dfe842c4)   0 |
| #define | [UBX\_FRAME\_PREAMBLE\_SYNC\_CHAR\_2\_IDX](#af940bf4cc68adff5b8b187dcf1e93735)   1 |
| #define | [UBX\_FRAME\_MSG\_CLASS\_IDX](#a2c667ef9bb2d12effb251f4df6827c73)   2 |
| #define | [UBX\_PAYLOAD\_SZ\_MAX](#a9c66cd27732153c56d0872339bc3deae)   512 |
| #define | [UBX\_FRAME\_SZ\_MAX](#a1cab11988642144cfcc6c7309f5806d0)   [UBX\_FRAME\_SZ](#a4c64b9118da471baa6a7a88ee345bf66)([UBX\_PAYLOAD\_SZ\_MAX](#a9c66cd27732153c56d0872339bc3deae)) |
| #define | [UBX\_NAV\_PVT\_VALID\_DATE](#ae9c98287cbaf17e7fc1beaedc1679fa4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [UBX\_NAV\_PVT\_VALID\_TIME](#a583269f4c0ea39e43671fd9267b129af)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [UBX\_NAV\_PVT\_VALID\_UTC\_TOD](#a4ea40193fa60a75bf5ede5586da92931)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [UBX\_NAV\_PVT\_VALID\_MAGN](#a1f067fe87ff51b4b59e7bfce2c4b9880)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [UBX\_NAV\_PVT\_FLAGS\_GNSS\_FIX\_OK](#af79a6a074065fb7d792109b4d99ba32f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [UBX\_NAV\_PVT\_FLAGS3\_INVALID\_LLH](#ac348d618c31a5ae7b243243267b041c6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [UBX\_NAV\_SAT\_FLAGS\_SV\_USED](#aaaa4b2e1968a45f4c7ee336a45b4164b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [UBX\_GNSS\_SELECTION\_GPS](#ae23528d7cc5a34a48f062a084ae2dbd0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [UBX\_GNSS\_SELECTION\_GLONASS](#ab767685719aa08364b5e77262fae232a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [UBX\_GNSS\_SELECTION\_BEIDOU](#ad57613b25d1716b7ca3e01d37b64a16d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [UBX\_GNSS\_SELECTION\_GALILEO](#aa338a732341e0e1560a749123cecd700)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [UBX\_CFG\_PRT\_MODE\_CHAR\_LEN](#a0eb35bbe06a126aa8aed1738b6dd56c2)(val) |
| #define | [UBX\_CFG\_PRT\_MODE\_PARITY](#abe8dd1db5cf126f76f7a44f4715e9cfa)(val) |
| #define | [UBX\_CFG\_PRT\_MODE\_STOP\_BITS](#a23d980439eed2fe310c8be5107333489)(val) |
| #define | [UBX\_CFG\_PRT\_PROTO\_MASK\_UBX](#a3f8c1064b9f51778df32e0b713302a2e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [UBX\_CFG\_PRT\_PROTO\_MASK\_NMEA](#a174c408931fd4ca3e6c8128dd540d2dd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [UBX\_CFG\_PRT\_PROTO\_MASK\_RTCM3](#ad481e57bb7b8707c468990ad0568d53c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [UBX\_CFG\_NAV5\_APPLY\_DYN](#adcfe7daa815d7a1a7dea67642b88ebbf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [UBX\_CFG\_NAV5\_APPLY\_FIX\_MODE](#a93b02f16b10968f47932c502e300c5a6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [UBX\_FRAME\_DEFINE](#ad79a0ce05086ada71822ccb9100bc100)(\_name, \_frame) |
| #define | [UBX\_FRAME\_ARRAY\_DEFINE](#aca7cb6846e6d01cc84df655f22832987)(\_name, ...) |
| #define | [UBX\_FRAME\_ACK\_INITIALIZER](#a8cf6388d5ee4509e36742e30dc640889)(\_class\_id, \_msg\_id) |
| #define | [UBX\_FRAME\_NAK\_INITIALIZER](#a5b5ffd92f5894fc966b1875c7ce4c1a3)(\_class\_id, \_msg\_id) |
| #define | [UBX\_FRAME\_CFG\_RST\_INITIALIZER](#aed21b263c25f39d499b37dfff38bca39)(\_start\_mode, \_reset\_mode) |
| #define | [UBX\_FRAME\_CFG\_RATE\_INITIALIZER](#a3192675717120efc97a8858605b3f45d)(\_meas\_rate\_ms, \_nav\_rate, \_time\_ref) |
| #define | [UBX\_FRAME\_CFG\_MSG\_RATE\_INITIALIZER](#af9ce35b33de7f9ebc68d11731beb02f0)(\_class\_id, \_msg\_id, \_rate) |
| #define | [UBX\_FRAME\_CFG\_VAL\_SET\_U8\_INITIALIZER](#a5b4484d44a25068f960f7f1196cffe89)(\_key, \_value) |
| #define | [UBX\_FRAME\_CFG\_VAL\_SET\_U16\_INITIALIZER](#a66b9664185ed9cfb096df2b375e41f0e)(\_key, \_value) |
| #define | [UBX\_FRAME\_CFG\_VAL\_SET\_U32\_INITIALIZER](#a997cd3bd57d5cfc6c4f1eeca2bc6ba37)(\_key, \_value) |
| #define | [UBX\_FRAME\_CFG\_VAL\_GET\_INITIALIZER](#a1d7a930de22dadce2aae88e64e246dd9)(\_key) |
| #define | [UBX\_FRAME\_INITIALIZER\_PAYLOAD](#a4d90346d76d003aeddf16fc665203926)(\_class\_id, \_msg\_id, ...) |
| #define | [UBX\_FRAME\_GET\_INITIALIZER](#a1cf8842293fe70f3ea22686a55d9beda)(\_class\_id, \_msg\_id) |

| Enumerations | |
| --- | --- |
| enum | [ubx\_class\_id](#ad0dac3b7e7cbf3649aa5b8813e40fc18) {     [UBX\_CLASS\_ID\_NAV](#ad0dac3b7e7cbf3649aa5b8813e40fc18a8f46002e33dddab6782bad93ab3fd8b1) = 0x01 , [UBX\_CLASS\_ID\_RXM](#ad0dac3b7e7cbf3649aa5b8813e40fc18a5e4eaf66a7356e73b4c6e4949160f321) = 0x02 , [UBX\_CLASS\_ID\_INF](#ad0dac3b7e7cbf3649aa5b8813e40fc18a898b493832d06586cf48f9a2545651d0) = 0x04 , [UBX\_CLASS\_ID\_ACK](#ad0dac3b7e7cbf3649aa5b8813e40fc18aee43a865c5815ce058261f5f0550fa2b) = 0x05 ,     [UBX\_CLASS\_ID\_CFG](#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c) = 0x06 , [UBX\_CLASS\_ID\_UPD](#ad0dac3b7e7cbf3649aa5b8813e40fc18aba0a811e14f9e87bd47bfbeaad24e11b) = 0x09 , [UBX\_CLASS\_ID\_MON](#ad0dac3b7e7cbf3649aa5b8813e40fc18ac9200dedb25cfa03b80f4336e86db5ed) = 0x0A , [UBX\_CLASS\_ID\_TIM](#ad0dac3b7e7cbf3649aa5b8813e40fc18a8c700fd2062d8dc51c5e4b28c98c6cf0) = 0x0D ,     [UBX\_CLASS\_ID\_MGA](#ad0dac3b7e7cbf3649aa5b8813e40fc18a418aca13d3bd1608869494d26559e52f) = 0x13 , [UBX\_CLASS\_ID\_LOG](#ad0dac3b7e7cbf3649aa5b8813e40fc18a1e35a224f4809d3a59d0f1570bf382bb) = 0x21 , [UBX\_CLASS\_ID\_SEC](#ad0dac3b7e7cbf3649aa5b8813e40fc18a760de1a9f06cc6d4832da868d01702c4) = 0x27 , [UBX\_CLASS\_ID\_NMEA\_STD](#ad0dac3b7e7cbf3649aa5b8813e40fc18a7e7c3645f46ba3c2e8329ae3a9eeaa79) = 0xF0 ,     [UBX\_CLASS\_ID\_NMEA\_PUBX](#ad0dac3b7e7cbf3649aa5b8813e40fc18a0d9d5044c9df2a6b61b7a46a4f24e895) = 0xF1   } |
| enum | [ubx\_msg\_id\_nav](#a8a935ea7debb4ac73ea99c98d6ef4d3b) { [UBX\_MSG\_ID\_NAV\_PVT](#a8a935ea7debb4ac73ea99c98d6ef4d3ba8f887b777e29fc05107ac406d4a87458) = 0x07 , [UBX\_MSG\_ID\_NAV\_SAT](#a8a935ea7debb4ac73ea99c98d6ef4d3bae87d4355340186b8a049346e3076f9ae) = 0x35 } |
| enum | [ubx\_nav\_fix\_type](#a173b6c1016562da43b8131b8d8f04fef) {     [UBX\_NAV\_FIX\_TYPE\_NO\_FIX](#a173b6c1016562da43b8131b8d8f04fefad351fdc11590580b88ba5b486113e498) = 0 , [UBX\_NAV\_FIX\_TYPE\_DR](#a173b6c1016562da43b8131b8d8f04fefae28182c06da19d2b498f92d09d74b33e) = 1 , [UBX\_NAV\_FIX\_TYPE\_2D](#a173b6c1016562da43b8131b8d8f04fefae47dad429327e6a0cc89e339729b2651) = 2 , [UBX\_NAV\_FIX\_TYPE\_3D](#a173b6c1016562da43b8131b8d8f04fefa1f8c2845d6e8e41f62cc28b7f1681f43) = 3 ,     [UBX\_NAV\_FIX\_TYPE\_GNSS\_DR\_COMBINED](#a173b6c1016562da43b8131b8d8f04fefa648f596240841758588749574998bd71) = 4 , [UBX\_NAV\_FIX\_TYPE\_TIME\_ONLY](#a173b6c1016562da43b8131b8d8f04fefa2c20469f6893f651ad14b8ed6a7c3845) = 5   } |
| enum | [ubx\_nav\_sat\_health](#afbba8ada09d6c6489d52a3b9dc31725f) { [UBX\_NAV\_SAT\_HEALTH\_UNKNOWN](#afbba8ada09d6c6489d52a3b9dc31725fa3661b89022659975720d3a022b21f194) = 0 , [UBX\_NAV\_SAT\_HEALTH\_HEALTHY](#afbba8ada09d6c6489d52a3b9dc31725fa7dcaa32f001d1a7b5b071cdf7621081e) = 1 , [UBX\_NAV\_SAT\_HEALTH\_UNHEALTHY](#afbba8ada09d6c6489d52a3b9dc31725fa95ea7c01a987a1e334f41c79642b8139) = 2 } |
| enum | [ubx\_gnss\_id](#a6711a33292bf25327950406b96585690) {     [UBX\_GNSS\_ID\_GPS](#a6711a33292bf25327950406b96585690adca8434b24978430d03939b81d76fbb9) = 0 , [UBX\_GNSS\_ID\_SBAS](#a6711a33292bf25327950406b96585690a31a403a2013dc9da3da56366fa95f19b) = 1 , [UBX\_GNSS\_ID\_GALILEO](#a6711a33292bf25327950406b96585690a931ed807a91dd1f0e6e2cfa013860cbe) = 2 , [UBX\_GNSS\_ID\_BEIDOU](#a6711a33292bf25327950406b96585690ac3f1631647cfd0246be61fc78549a9f7) = 3 ,     [UBX\_GNSS\_ID\_QZSS](#a6711a33292bf25327950406b96585690a2dad67829bb51786024771c0d5a6d103) = 5 , [UBX\_GNSS\_ID\_GLONASS](#a6711a33292bf25327950406b96585690a4e14cf64a03e9d37af198870b0616497) = 6   } |
| enum | [ubx\_msg\_id\_ack](#a260c4adbe9524bd747127a4e3f14bbca) { [UBX\_MSG\_ID\_ACK](#a260c4adbe9524bd747127a4e3f14bbcaa88bba7f61485369188998bc1c18b2511) = 0x01 , [UBX\_MSG\_ID\_NAK](#a260c4adbe9524bd747127a4e3f14bbcaacd2316ff6386c7eb2da90de1f4466469) = 0x00 } |
| enum | [ubx\_msg\_id\_cfg](#a3cf04300758f1802e0703428707035d7) {     [UBX\_MSG\_ID\_CFG\_PRT](#a3cf04300758f1802e0703428707035d7a871b880c791ad49c55164856ac4f83f9) = 0x00 , [UBX\_MSG\_ID\_CFG\_MSG](#a3cf04300758f1802e0703428707035d7ace6e98ad1c1ac7232327d42b0f4302ef) = 0x01 , [UBX\_MSG\_ID\_CFG\_RST](#a3cf04300758f1802e0703428707035d7ad2c8bf68306ca6bb22e88c5c6d957453) = 0x04 , [UBX\_MSG\_ID\_CFG\_RATE](#a3cf04300758f1802e0703428707035d7a89a96eb89044b208d3a6c29fc273fa26) = 0x08 ,     [UBX\_MSG\_ID\_CFG\_NAV5](#a3cf04300758f1802e0703428707035d7a036303b6caf601b73bfb48b3a7423309) = 0x24 , [UBX\_MSG\_ID\_CFG\_VAL\_SET](#a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3) = 0x8A , [UBX\_MSG\_ID\_CFG\_VAL\_GET](#a3cf04300758f1802e0703428707035d7aa31397b2154b0f1f9b1e906c91a6bc8c) = 0x8B   } |
| enum | [ubx\_msg\_id\_mon](#a0d969e434f941cf5af7143cca0cf0fe4) { [UBX\_MSG\_ID\_MON\_VER](#a0d969e434f941cf5af7143cca0cf0fe4a43aa77232e6c2aed82ecf2033c0a06b0) = 0x04 , [UBX\_MSG\_ID\_MON\_GNSS](#a0d969e434f941cf5af7143cca0cf0fe4a66c14a28074edc8631bd6b47f5c45888) = 0x28 } |
| enum | [ubx\_cfg\_port\_id](#adb6a6e16f193bc70840b2dd12dbc9baa) { [UBX\_CFG\_PORT\_ID\_DDC](#adb6a6e16f193bc70840b2dd12dbc9baaa5c7c1a24670995305bcb8e98cfd1fa19) = 0 , [UBX\_CFG\_PORT\_ID\_UART](#adb6a6e16f193bc70840b2dd12dbc9baaaccb591a437d0ed7cca8888f41b855efb) = 1 , [UBX\_CFG\_PORT\_ID\_USB](#adb6a6e16f193bc70840b2dd12dbc9baaa3af5f6c24fade976d4ece339e9240114) = 2 , [UBX\_CFG\_PORT\_ID\_SPI](#adb6a6e16f193bc70840b2dd12dbc9baaaa0ee1de6e26bb0585f24fddbe3d7ec9a) = 3 } |
| enum | [ubx\_cfg\_char\_len](#a887b1fa6af0d6d08cc51ed65de64a78a) { [UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_5](#a887b1fa6af0d6d08cc51ed65de64a78aa019364b4a4482098acc0d7821b456b83) = 0 , [UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_6](#a887b1fa6af0d6d08cc51ed65de64a78aaeea043882f976e34008f261e1b2ee5ac) = 1 , [UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_7](#a887b1fa6af0d6d08cc51ed65de64a78aaeacece1ca309918fa3abe7a02911f5ca) = 2 , [UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_8](#a887b1fa6af0d6d08cc51ed65de64a78aae7769c1dd298aabbad37ddaf6260eb4d) = 3 } |
| enum | [ubx\_cfg\_parity](#a2e5de1479afbcf20caa3300282bb0d1a) { [UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_EVEN](#a2e5de1479afbcf20caa3300282bb0d1aa1ef24c67f4e90f7c6fb011ec433ebb68) = 0 , [UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_ODD](#a2e5de1479afbcf20caa3300282bb0d1aa5db544370f64f19224e9243eae0942ac) = 1 , [UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_NONE](#a2e5de1479afbcf20caa3300282bb0d1aa46b4ba80de7ca4c9d1ea403dd6efb385) = 4 } |
| enum | [ubx\_cfg\_stop\_bits](#a94709ee4f4afe0194790893251ee2b4c) { [UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_1](#a94709ee4f4afe0194790893251ee2b4caf762dc50babaacd4cbb1ce753a8c0ae9) = 0 , [UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_1\_5](#a94709ee4f4afe0194790893251ee2b4ca06c8d5338db83ce4a74a92228f04ffb1) = 1 , [UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_2](#a94709ee4f4afe0194790893251ee2b4caea0ef9695c70807a5bdfb1725f31ea3f) = 2 , [UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_0\_5](#a94709ee4f4afe0194790893251ee2b4ca461834aa0d5d6ddec370ecd247e330e6) = 3 } |
| enum | [ubx\_dyn\_model](#a9e5e9af7a281e53f2b950089ee66561f) {     [UBX\_DYN\_MODEL\_PORTABLE](#a9e5e9af7a281e53f2b950089ee66561fa59c3bbc8cb2a44e26920adbe0251375b) = 0 , [UBX\_DYN\_MODEL\_STATIONARY](#a9e5e9af7a281e53f2b950089ee66561fa4f147b313644dba74c95930038201cf7) = 2 , [UBX\_DYN\_MODEL\_PEDESTRIAN](#a9e5e9af7a281e53f2b950089ee66561fa8a2a4bb1bb5b7f69960fdcde374f2ee6) = 3 , [UBX\_DYN\_MODEL\_AUTOMOTIVE](#a9e5e9af7a281e53f2b950089ee66561fa736709e926d95754fef9260c596530e2) = 4 ,     [UBX\_DYN\_MODEL\_SEA](#a9e5e9af7a281e53f2b950089ee66561fa6d89a732b306e21feeaee51cdbcc0bed) = 5 , [UBX\_DYN\_MODEL\_AIRBORNE\_1G](#a9e5e9af7a281e53f2b950089ee66561fa9bb36ad38aca4f118fe1bdc2f0351476) = 6 , [UBX\_DYN\_MODEL\_AIRBORNE\_2G](#a9e5e9af7a281e53f2b950089ee66561fa1a39257d816910b26f2323b61a278519) = 7 , [UBX\_DYN\_MODEL\_AIRBORNE\_4G](#a9e5e9af7a281e53f2b950089ee66561fae4640365810ae80e8c24507fd7279f3d) = 8 ,     [UBX\_DYN\_MODEL\_WRIST](#a9e5e9af7a281e53f2b950089ee66561fa172bc7d2ed80cadb4077ae42233764b2) = 9 , [UBX\_DYN\_MODEL\_BIKE](#a9e5e9af7a281e53f2b950089ee66561faa062bfc1af7cc119d025dee309ac1d25) = 10   } |
| enum | [ubx\_fix\_mode](#a342c0d62cf874ccb8b657ce85d91efe0) { [UBX\_FIX\_MODE\_2D\_ONLY](#a342c0d62cf874ccb8b657ce85d91efe0a29354369703a5e54ae7e49edfff886ff) = 1 , [UBX\_FIX\_MODE\_3D\_ONLY](#a342c0d62cf874ccb8b657ce85d91efe0aa60a16ce7e100e06e0bab9a3922003a6) = 2 , [UBX\_FIX\_MODE\_AUTO](#a342c0d62cf874ccb8b657ce85d91efe0a1e324c97e68e6d7ce35feb4ffe2ca617) = 3 } |
| enum | [ubx\_utc\_standard](#a359b0f88d3769af43c2b1699eb172f23) {     [UBX\_UTC\_STANDARD\_AUTOMATIC](#a359b0f88d3769af43c2b1699eb172f23a8bc6c6397d5bc342ebe0ea36522e96a5) = 0 , [UBX\_UTC\_STANDARD\_GPS](#a359b0f88d3769af43c2b1699eb172f23a34b4b516760245d0a5bbfcbb5937d74c) = 3 , [UBX\_UTC\_STANDARD\_GALILEO](#a359b0f88d3769af43c2b1699eb172f23a6fe85d7688c6730a492981fdc4623c67) = 5 , [UBX\_UTC\_STANDARD\_GLONASS](#a359b0f88d3769af43c2b1699eb172f23ab6c294e0f55696a8c90ec8211673ca80) = 6 ,     [UBX\_UTC\_STANDARD\_BEIDOU](#a359b0f88d3769af43c2b1699eb172f23a8eeae948253c11b7f097dd06896e66f8) = 7   } |
| enum | [ubx\_cfg\_rst\_start\_mode](#a43766ad4c0fd1d31fd547c090e3f39b6) { [UBX\_CFG\_RST\_HOT\_START](#a43766ad4c0fd1d31fd547c090e3f39b6a67b9cba109cc8f57a38c41b1d521e3c7) = 0x0000 , [UBX\_CFG\_RST\_WARM\_START](#a43766ad4c0fd1d31fd547c090e3f39b6a1621ed3281429f96fc598d90cc388c95) = 0x0001 , [UBX\_CFG\_RST\_COLD\_START](#a43766ad4c0fd1d31fd547c090e3f39b6aaef8449ed29d6dd76bdd34157d873896) = 0xFFFF } |
| enum | [ubx\_cfg\_rst\_mode](#a5cc2a8f42fd62032afa3cd7687452896) { [UBX\_CFG\_RST\_MODE\_HW](#a5cc2a8f42fd62032afa3cd7687452896ac02d28b95ef601af32dc898e35ad252e) = 0x00 , [UBX\_CFG\_RST\_MODE\_SW](#a5cc2a8f42fd62032afa3cd7687452896a7fd6f4b7557dfa6511dcb6354963d342) = 0x01 , [UBX\_CFG\_RST\_MODE\_GNSS\_STOP](#a5cc2a8f42fd62032afa3cd7687452896a0e9177345e82ad614c1ab4c8b52b9265) = 0x08 , [UBX\_CFG\_RST\_MODE\_GNSS\_START](#a5cc2a8f42fd62032afa3cd7687452896aca25f86cc1d85c60b1d67509d0e9506b) = 0x09 } |
| enum | [ubx\_cfg\_rate\_time\_ref](#a621d2fae9721b6dc62a71801f3b7952e) {     [UBX\_CFG\_RATE\_TIME\_REF\_UTC](#a621d2fae9721b6dc62a71801f3b7952eacc3989fab9e22270c389b0318bbe45ea) = 0 , [UBX\_CFG\_RATE\_TIME\_REF\_GPS](#a621d2fae9721b6dc62a71801f3b7952ea7a2d00bdb7fef5ff7da1d3a682a1b82e) = 1 , [UBX\_CFG\_RATE\_TIME\_REF\_GLONASS](#a621d2fae9721b6dc62a71801f3b7952ea519dc8f11c80b5a08771fbc36c70fbb8) = 2 , [UBX\_CFG\_RATE\_TIME\_REF\_BEIDOU](#a621d2fae9721b6dc62a71801f3b7952ea30f66599c483f622607f0b13ad0451f8) = 3 ,     [UBX\_CFG\_RATE\_TIME\_REF\_GALILEO](#a621d2fae9721b6dc62a71801f3b7952eab7ed326b5da1087afb8d531d97bb9f16) = 4 , [UBX\_CFG\_RATE\_TIME\_REF\_NAVIC](#a621d2fae9721b6dc62a71801f3b7952ea5be3c906a6c528f65575990041b7e6ce) = 5   } |
| enum | [ubx\_cfg\_val\_ver](#ad7e0ffe55e8dbd97caa5bc089d33540c) { [UBX\_CFG\_VAL\_VER\_SIMPLE](#ad7e0ffe55e8dbd97caa5bc089d33540ca1fe2554bbbf05c86d3f9b0bc50927c1b) = 0 , [UBX\_CFG\_VAL\_VER\_TRANSACTION](#ad7e0ffe55e8dbd97caa5bc089d33540caca3b7f2a39ff93b91b8317245e8375ab) = 1 } |
| enum | [ubx\_msg\_id\_nmea\_std](#aa221b68c53f25634d9f2f435f28c1a6c) {     [UBX\_MSG\_ID\_NMEA\_STD\_DTM](#aa221b68c53f25634d9f2f435f28c1a6cac84f9ad61c85bbce60e680639c3d88ad) = 0x0A , [UBX\_MSG\_ID\_NMEA\_STD\_GBQ](#aa221b68c53f25634d9f2f435f28c1a6ca5174a26b3b79356bf06402de46bc0774) = 0x44 , [UBX\_MSG\_ID\_NMEA\_STD\_GBS](#aa221b68c53f25634d9f2f435f28c1a6caef6c925e20f072665bf55e435d37a6ac) = 0x09 , [UBX\_MSG\_ID\_NMEA\_STD\_GGA](#aa221b68c53f25634d9f2f435f28c1a6ca07aa8c55e3504c0d19b1e123f4d2e7c7) = 0x00 ,     [UBX\_MSG\_ID\_NMEA\_STD\_GLL](#aa221b68c53f25634d9f2f435f28c1a6ca6435225efac8c7ef6e336a84fa2e8932) = 0x01 , [UBX\_MSG\_ID\_NMEA\_STD\_GLQ](#aa221b68c53f25634d9f2f435f28c1a6ca263a724b491a6303d5486828a49a8961) = 0x43 , [UBX\_MSG\_ID\_NMEA\_STD\_GNQ](#aa221b68c53f25634d9f2f435f28c1a6caa2c68fe9d01bc4acf3054d667f3e2a77) = 0x42 , [UBX\_MSG\_ID\_NMEA\_STD\_GNS](#aa221b68c53f25634d9f2f435f28c1a6cafea982067c784c47ae5b1ad7e91b4191) = 0x0D ,     [UBX\_MSG\_ID\_NMEA\_STD\_GPQ](#aa221b68c53f25634d9f2f435f28c1a6ca39492ba0c78d0290819b9410e2e55781) = 0x40 , [UBX\_MSG\_ID\_NMEA\_STD\_GRS](#aa221b68c53f25634d9f2f435f28c1a6ca7f1d764aa078c284c575ec610d4f4853) = 0x06 , [UBX\_MSG\_ID\_NMEA\_STD\_GSA](#aa221b68c53f25634d9f2f435f28c1a6cae3c6e42e75e69a34d7017d2f2aa3c70d) = 0x02 , [UBX\_MSG\_ID\_NMEA\_STD\_GST](#aa221b68c53f25634d9f2f435f28c1a6ca99b8f62b1d204b335a06ed6f3ef214e6) = 0x07 ,     [UBX\_MSG\_ID\_NMEA\_STD\_GSV](#aa221b68c53f25634d9f2f435f28c1a6ca2a5cc3b49abc9be0c6bbab0a9963ba03) = 0x03 , [UBX\_MSG\_ID\_NMEA\_STD\_RMC](#aa221b68c53f25634d9f2f435f28c1a6ca8787502b2d9a14d2ce79b1ce1713d6f3) = 0x04 , [UBX\_MSG\_ID\_NMEA\_STD\_THS](#aa221b68c53f25634d9f2f435f28c1a6ca884ab2ce56a1f7a08d4b9d06b944ad37) = 0x0E , [UBX\_MSG\_ID\_NMEA\_STD\_TXT](#aa221b68c53f25634d9f2f435f28c1a6cad58d4ac5b57cbdd42d360560cc16fc0e) = 0x41 ,     [UBX\_MSG\_ID\_NMEA\_STD\_VLW](#aa221b68c53f25634d9f2f435f28c1a6ca58ad56a546a2df6c9359927375da9904) = 0x0F , [UBX\_MSG\_ID\_NMEA\_STD\_VTG](#aa221b68c53f25634d9f2f435f28c1a6ca5c12f57e0b4de16d09fc42f23740908b) = 0x05 , [UBX\_MSG\_ID\_NMEA\_STD\_ZDA](#aa221b68c53f25634d9f2f435f28c1a6cae6a2501b586793e75cdd0085170a9a27) = 0x08   } |
| enum | [ubx\_msg\_id\_nmea\_pubx](#a58dc8b84784731500aa7f55afeb7e582) {     [UBX\_MSG\_ID\_NMEA\_PUBX\_CONFIG](#a58dc8b84784731500aa7f55afeb7e582a43616a8ad2465c7521aa9ed28460cf57) = 0x41 , [UBX\_MSG\_ID\_NMEA\_PUBX\_POSITION](#a58dc8b84784731500aa7f55afeb7e582a61cbc043ccd0a96ba2327d7bd95189c6) = 0x00 , [UBX\_MSG\_ID\_NMEA\_PUBX\_RATE](#a58dc8b84784731500aa7f55afeb7e582af5ccdcc3eed53b0906b83667443e3667) = 0x40 , [UBX\_MSG\_ID\_NMEA\_PUBX\_SVSTATUS](#a58dc8b84784731500aa7f55afeb7e582a73aeb813a098d600dfb60561bc042e2a) = 0x03 ,     [UBX\_MSG\_ID\_NMEA\_PUBX\_TIME](#a58dc8b84784731500aa7f55afeb7e582a9f36e6c7688a62737beb203e82de91ef) = 0x04   } |

| Functions | |
| --- | --- |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ubx\_calc\_checksum](#a450f46250ef486af4f933e69ddbb42d2) (const struct [ubx\_frame](structubx__frame.md) \*frame, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| static int | [ubx\_frame\_encode](#acdc0d9b7d25df6aba6bb091e7034f5ba) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) class, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) payload\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_len) |

## Macro Definition Documentation

## [◆ ](#adcfe7daa815d7a1a7dea67642b88ebbf)UBX\_CFG\_NAV5\_APPLY\_DYN

| #define UBX\_CFG\_NAV5\_APPLY\_DYN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a93b02f16b10968f47932c502e300c5a6)UBX\_CFG\_NAV5\_APPLY\_FIX\_MODE

| #define UBX\_CFG\_NAV5\_APPLY\_FIX\_MODE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a0eb35bbe06a126aa8aed1738b6dd56c2)UBX\_CFG\_PRT\_MODE\_CHAR\_LEN

| #define UBX\_CFG\_PRT\_MODE\_CHAR\_LEN | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((val) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(2)) << 6)

[BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)

#define BIT\_MASK(n)

Bit mask with bits 0 through n-1 (inclusive) set, or 0 if n is 0.

**Definition** util\_macro.h:68

## [◆ ](#abe8dd1db5cf126f76f7a44f4715e9cfa)UBX\_CFG\_PRT\_MODE\_PARITY

| #define UBX\_CFG\_PRT\_MODE\_PARITY | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((val) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(3)) << 9)

## [◆ ](#a23d980439eed2fe310c8be5107333489)UBX\_CFG\_PRT\_MODE\_STOP\_BITS

| #define UBX\_CFG\_PRT\_MODE\_STOP\_BITS | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((val) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(2)) << 12)

## [◆ ](#a174c408931fd4ca3e6c8128dd540d2dd)UBX\_CFG\_PRT\_PROTO\_MASK\_NMEA

| #define UBX\_CFG\_PRT\_PROTO\_MASK\_NMEA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#ad481e57bb7b8707c468990ad0568d53c)UBX\_CFG\_PRT\_PROTO\_MASK\_RTCM3

| #define UBX\_CFG\_PRT\_PROTO\_MASK\_RTCM3   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a3f8c1064b9f51778df32e0b713302a2e)UBX\_CFG\_PRT\_PROTO\_MASK\_UBX

| #define UBX\_CFG\_PRT\_PROTO\_MASK\_UBX   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a8cf6388d5ee4509e36742e30dc640889)UBX\_FRAME\_ACK\_INITIALIZER

| #define UBX\_FRAME\_ACK\_INITIALIZER | ( |  | *\_class\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_msg\_id* ) |

**Value:**

[UBX\_FRAME\_INITIALIZER\_PAYLOAD](#a4d90346d76d003aeddf16fc665203926)([UBX\_CLASS\_ID\_ACK](#ad0dac3b7e7cbf3649aa5b8813e40fc18aee43a865c5815ce058261f5f0550fa2b), [UBX\_MSG\_ID\_ACK](#a260c4adbe9524bd747127a4e3f14bbcaa88bba7f61485369188998bc1c18b2511), \_class\_id, \_msg\_id)

[UBX\_MSG\_ID\_ACK](#a260c4adbe9524bd747127a4e3f14bbcaa88bba7f61485369188998bc1c18b2511)

@ UBX\_MSG\_ID\_ACK

**Definition** protocol.h:164

[UBX\_FRAME\_INITIALIZER\_PAYLOAD](#a4d90346d76d003aeddf16fc665203926)

#define UBX\_FRAME\_INITIALIZER\_PAYLOAD(\_class\_id, \_msg\_id,...)

**Definition** protocol.h:506

[UBX\_CLASS\_ID\_ACK](#ad0dac3b7e7cbf3649aa5b8813e40fc18aee43a865c5815ce058261f5f0550fa2b)

@ UBX\_CLASS\_ID\_ACK

**Definition** protocol.h:51

## [◆ ](#aca7cb6846e6d01cc84df655f22832987)UBX\_FRAME\_ARRAY\_DEFINE

| #define UBX\_FRAME\_ARRAY\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

const struct [ubx\_frame](structubx__frame.md) \*\_name[] = {\_\_VA\_ARGS\_\_};

[ubx\_frame](structubx__frame.md)

**Definition** protocol.h:29

## [◆ ](#af9ce35b33de7f9ebc68d11731beb02f0)UBX\_FRAME\_CFG\_MSG\_RATE\_INITIALIZER

| #define UBX\_FRAME\_CFG\_MSG\_RATE\_INITIALIZER | ( |  | *\_class\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_msg\_id*, |
|  |  |  | *\_rate* ) |

**Value:**

[UBX\_FRAME\_INITIALIZER\_PAYLOAD](#a4d90346d76d003aeddf16fc665203926)([UBX\_CLASS\_ID\_CFG](#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c), [UBX\_MSG\_ID\_CFG\_MSG](#a3cf04300758f1802e0703428707035d7ace6e98ad1c1ac7232327d42b0f4302ef), \

\_class\_id, \_msg\_id, \_rate)

[UBX\_MSG\_ID\_CFG\_MSG](#a3cf04300758f1802e0703428707035d7ace6e98ad1c1ac7232327d42b0f4302ef)

@ UBX\_MSG\_ID\_CFG\_MSG

**Definition** protocol.h:170

[UBX\_CLASS\_ID\_CFG](#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c)

@ UBX\_CLASS\_ID\_CFG

**Definition** protocol.h:52

## [◆ ](#a3192675717120efc97a8858605b3f45d)UBX\_FRAME\_CFG\_RATE\_INITIALIZER

| #define UBX\_FRAME\_CFG\_RATE\_INITIALIZER | ( |  | *\_meas\_rate\_ms*, |
| --- | --- | --- | --- |
|  |  |  | *\_nav\_rate*, |
|  |  |  | *\_time\_ref* ) |

**Value:**

[UBX\_FRAME\_INITIALIZER\_PAYLOAD](#a4d90346d76d003aeddf16fc665203926)([UBX\_CLASS\_ID\_CFG](#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c), [UBX\_MSG\_ID\_CFG\_RATE](#a3cf04300758f1802e0703428707035d7a89a96eb89044b208d3a6c29fc273fa26), \

(\_meas\_rate\_ms & 0xFF), ((\_meas\_rate\_ms >> 8) & 0xFF), \

(\_nav\_rate & 0xFF), ((\_nav\_rate >> 8) & 0xFF), \

(\_time\_ref & 0xFF), ((\_time\_ref >> 8) & 0xFF))

[UBX\_MSG\_ID\_CFG\_RATE](#a3cf04300758f1802e0703428707035d7a89a96eb89044b208d3a6c29fc273fa26)

@ UBX\_MSG\_ID\_CFG\_RATE

**Definition** protocol.h:172

## [◆ ](#aed21b263c25f39d499b37dfff38bca39)UBX\_FRAME\_CFG\_RST\_INITIALIZER

| #define UBX\_FRAME\_CFG\_RST\_INITIALIZER | ( |  | *\_start\_mode*, |
| --- | --- | --- | --- |
|  |  |  | *\_reset\_mode* ) |

**Value:**

[UBX\_FRAME\_INITIALIZER\_PAYLOAD](#a4d90346d76d003aeddf16fc665203926)([UBX\_CLASS\_ID\_CFG](#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c), [UBX\_MSG\_ID\_CFG\_RST](#a3cf04300758f1802e0703428707035d7ad2c8bf68306ca6bb22e88c5c6d957453), \

(\_start\_mode & 0xFF), ((\_start\_mode >> 8) & 0xFF), \

\_reset\_mode, 0)

[UBX\_MSG\_ID\_CFG\_RST](#a3cf04300758f1802e0703428707035d7ad2c8bf68306ca6bb22e88c5c6d957453)

@ UBX\_MSG\_ID\_CFG\_RST

**Definition** protocol.h:171

## [◆ ](#a1d7a930de22dadce2aae88e64e246dd9)UBX\_FRAME\_CFG\_VAL\_GET\_INITIALIZER

| #define UBX\_FRAME\_CFG\_VAL\_GET\_INITIALIZER | ( |  | *\_key* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UBX\_FRAME\_INITIALIZER\_PAYLOAD](#a4d90346d76d003aeddf16fc665203926)([UBX\_CLASS\_ID\_CFG](#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c), [UBX\_MSG\_ID\_CFG\_VAL\_GET](#a3cf04300758f1802e0703428707035d7aa31397b2154b0f1f9b1e906c91a6bc8c), \

0x00, 0x00, 0x00, 0x00, \

((\_key) & 0xFF), (((\_key) >> 8) & 0xFF), \

(((\_key) >> 16) & 0xFF), (((\_key) >> 24) & 0xFF))

[UBX\_MSG\_ID\_CFG\_VAL\_GET](#a3cf04300758f1802e0703428707035d7aa31397b2154b0f1f9b1e906c91a6bc8c)

@ UBX\_MSG\_ID\_CFG\_VAL\_GET

**Definition** protocol.h:175

## [◆ ](#a66b9664185ed9cfb096df2b375e41f0e)UBX\_FRAME\_CFG\_VAL\_SET\_U16\_INITIALIZER

| #define UBX\_FRAME\_CFG\_VAL\_SET\_U16\_INITIALIZER | ( |  | *\_key*, |
| --- | --- | --- | --- |
|  |  |  | *\_value* ) |

**Value:**

[UBX\_FRAME\_INITIALIZER\_PAYLOAD](#a4d90346d76d003aeddf16fc665203926)([UBX\_CLASS\_ID\_CFG](#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c), [UBX\_MSG\_ID\_CFG\_VAL\_SET](#a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3), \

0x00, 0x01, 0x00, 0x00, \

((\_key) & 0xFF), (((\_key) >> 8) & 0xFF), \

(((\_key) >> 16) & 0xFF), (((\_key) >> 24) & 0xFF), \

((\_value) & 0xFF), (((\_value) >> 8) & 0xFF))

[UBX\_MSG\_ID\_CFG\_VAL\_SET](#a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3)

@ UBX\_MSG\_ID\_CFG\_VAL\_SET

**Definition** protocol.h:174

## [◆ ](#a997cd3bd57d5cfc6c4f1eeca2bc6ba37)UBX\_FRAME\_CFG\_VAL\_SET\_U32\_INITIALIZER

| #define UBX\_FRAME\_CFG\_VAL\_SET\_U32\_INITIALIZER | ( |  | *\_key*, |
| --- | --- | --- | --- |
|  |  |  | *\_value* ) |

**Value:**

[UBX\_FRAME\_INITIALIZER\_PAYLOAD](#a4d90346d76d003aeddf16fc665203926)([UBX\_CLASS\_ID\_CFG](#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c), [UBX\_MSG\_ID\_CFG\_VAL\_SET](#a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3), \

0x00, 0x01, 0x00, 0x00, \

((\_key) & 0xFF), (((\_key) >> 8) & 0xFF), \

(((\_key) >> 16) & 0xFF), (((\_key) >> 24) & 0xFF), \

((\_value) & 0xFF), (((\_value) >> 8) & 0xFF), \

(((\_value) >> 16) & 0xFF), (((\_value) >> 24) & 0xFF))

## [◆ ](#a5b4484d44a25068f960f7f1196cffe89)UBX\_FRAME\_CFG\_VAL\_SET\_U8\_INITIALIZER

| #define UBX\_FRAME\_CFG\_VAL\_SET\_U8\_INITIALIZER | ( |  | *\_key*, |
| --- | --- | --- | --- |
|  |  |  | *\_value* ) |

**Value:**

[UBX\_FRAME\_INITIALIZER\_PAYLOAD](#a4d90346d76d003aeddf16fc665203926)([UBX\_CLASS\_ID\_CFG](#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c), [UBX\_MSG\_ID\_CFG\_VAL\_SET](#a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3), \

0x00, 0x01, 0x00, 0x00, \

((\_key) & 0xFF), (((\_key) >> 8) & 0xFF), \

(((\_key) >> 16) & 0xFF), (((\_key) >> 24) & 0xFF), \

((\_value) & 0xFF))

## [◆ ](#ad79a0ce05086ada71822ccb9100bc100)UBX\_FRAME\_DEFINE

| #define UBX\_FRAME\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_frame* ) |

**Value:**

const static struct [ubx\_frame](structubx__frame.md) \_name = \_frame

## [◆ ](#aa0392f4a081c1077b4f235a757431aee)UBX\_FRAME\_FOOTER\_SZ

| #define UBX\_FRAME\_FOOTER\_SZ   2 |
| --- |

## [◆ ](#a1cf8842293fe70f3ea22686a55d9beda)UBX\_FRAME\_GET\_INITIALIZER

| #define UBX\_FRAME\_GET\_INITIALIZER | ( |  | *\_class\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_msg\_id* ) |

**Value:**

{ \

.preamble\_sync\_char\_1 = [UBX\_PREAMBLE\_SYNC\_CHAR\_1](#a1693f3584605a0197076cba71c79b0df), \

.preamble\_sync\_char\_2 = [UBX\_PREAMBLE\_SYNC\_CHAR\_2](#ad8d6229db563db619d4f0a9f225fb640), \

.class = \_class\_id, \

.id = \_msg\_id, \

.payload\_size = 0, \

.payload\_and\_checksum = { \

UBX\_CSUM(\_class\_id, \_msg\_id, 0, 0), \

}, \

}

[UBX\_PREAMBLE\_SYNC\_CHAR\_1](#a1693f3584605a0197076cba71c79b0df)

#define UBX\_PREAMBLE\_SYNC\_CHAR\_1

**Definition** protocol.h:19

[UBX\_PREAMBLE\_SYNC\_CHAR\_2](#ad8d6229db563db619d4f0a9f225fb640)

#define UBX\_PREAMBLE\_SYNC\_CHAR\_2

**Definition** protocol.h:20

## [◆ ](#a1342f8e944fcd9f45fe94eef9bda307c)UBX\_FRAME\_HEADER\_SZ

| #define UBX\_FRAME\_HEADER\_SZ   6 |
| --- |

## [◆ ](#a4d90346d76d003aeddf16fc665203926)UBX\_FRAME\_INITIALIZER\_PAYLOAD

| #define UBX\_FRAME\_INITIALIZER\_PAYLOAD | ( |  | *\_class\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_msg\_id*, |
|  |  |  | ... ) |

**Value:**

\_UBX\_FRAME\_INITIALIZER\_PAYLOAD(\_class\_id, \_msg\_id, \_\_VA\_ARGS\_\_)

## [◆ ](#a2c667ef9bb2d12effb251f4df6827c73)UBX\_FRAME\_MSG\_CLASS\_IDX

| #define UBX\_FRAME\_MSG\_CLASS\_IDX   2 |
| --- |

## [◆ ](#a5b5ffd92f5894fc966b1875c7ce4c1a3)UBX\_FRAME\_NAK\_INITIALIZER

| #define UBX\_FRAME\_NAK\_INITIALIZER | ( |  | *\_class\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_msg\_id* ) |

**Value:**

[UBX\_FRAME\_INITIALIZER\_PAYLOAD](#a4d90346d76d003aeddf16fc665203926)([UBX\_CLASS\_ID\_ACK](#ad0dac3b7e7cbf3649aa5b8813e40fc18aee43a865c5815ce058261f5f0550fa2b), [UBX\_MSG\_ID\_NAK](#a260c4adbe9524bd747127a4e3f14bbcaacd2316ff6386c7eb2da90de1f4466469), \_class\_id, \_msg\_id)

[UBX\_MSG\_ID\_NAK](#a260c4adbe9524bd747127a4e3f14bbcaacd2316ff6386c7eb2da90de1f4466469)

@ UBX\_MSG\_ID\_NAK

**Definition** protocol.h:165

## [◆ ](#a1b417ed30e090d3399f96c87dfe842c4)UBX\_FRAME\_PREAMBLE\_SYNC\_CHAR\_1\_IDX

| #define UBX\_FRAME\_PREAMBLE\_SYNC\_CHAR\_1\_IDX   0 |
| --- |

## [◆ ](#af940bf4cc68adff5b8b187dcf1e93735)UBX\_FRAME\_PREAMBLE\_SYNC\_CHAR\_2\_IDX

| #define UBX\_FRAME\_PREAMBLE\_SYNC\_CHAR\_2\_IDX   1 |
| --- |

## [◆ ](#a4c64b9118da471baa6a7a88ee345bf66)UBX\_FRAME\_SZ

| #define UBX\_FRAME\_SZ | ( |  | *payload\_size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(payload\_size + [UBX\_FRAME\_SZ\_WITHOUT\_PAYLOAD](#a8e1aded66fd229f071c9d5e060a001a6))

[UBX\_FRAME\_SZ\_WITHOUT\_PAYLOAD](#a8e1aded66fd229f071c9d5e060a001a6)

#define UBX\_FRAME\_SZ\_WITHOUT\_PAYLOAD

**Definition** protocol.h:16

## [◆ ](#a1cab11988642144cfcc6c7309f5806d0)UBX\_FRAME\_SZ\_MAX

| #define UBX\_FRAME\_SZ\_MAX   [UBX\_FRAME\_SZ](#a4c64b9118da471baa6a7a88ee345bf66)([UBX\_PAYLOAD\_SZ\_MAX](#a9c66cd27732153c56d0872339bc3deae)) |
| --- |

## [◆ ](#a8e1aded66fd229f071c9d5e060a001a6)UBX\_FRAME\_SZ\_WITHOUT\_PAYLOAD

| #define UBX\_FRAME\_SZ\_WITHOUT\_PAYLOAD   ([UBX\_FRAME\_HEADER\_SZ](#a1342f8e944fcd9f45fe94eef9bda307c) + [UBX\_FRAME\_FOOTER\_SZ](#aa0392f4a081c1077b4f235a757431aee)) |
| --- |

## [◆ ](#ad57613b25d1716b7ca3e01d37b64a16d)UBX\_GNSS\_SELECTION\_BEIDOU

| #define UBX\_GNSS\_SELECTION\_BEIDOU   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#aa338a732341e0e1560a749123cecd700)UBX\_GNSS\_SELECTION\_GALILEO

| #define UBX\_GNSS\_SELECTION\_GALILEO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#ab767685719aa08364b5e77262fae232a)UBX\_GNSS\_SELECTION\_GLONASS

| #define UBX\_GNSS\_SELECTION\_GLONASS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#ae23528d7cc5a34a48f062a084ae2dbd0)UBX\_GNSS\_SELECTION\_GPS

| #define UBX\_GNSS\_SELECTION\_GPS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#ac348d618c31a5ae7b243243267b041c6)UBX\_NAV\_PVT\_FLAGS3\_INVALID\_LLH

| #define UBX\_NAV\_PVT\_FLAGS3\_INVALID\_LLH   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#af79a6a074065fb7d792109b4d99ba32f)UBX\_NAV\_PVT\_FLAGS\_GNSS\_FIX\_OK

| #define UBX\_NAV\_PVT\_FLAGS\_GNSS\_FIX\_OK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#ae9c98287cbaf17e7fc1beaedc1679fa4)UBX\_NAV\_PVT\_VALID\_DATE

| #define UBX\_NAV\_PVT\_VALID\_DATE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a1f067fe87ff51b4b59e7bfce2c4b9880)UBX\_NAV\_PVT\_VALID\_MAGN

| #define UBX\_NAV\_PVT\_VALID\_MAGN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a583269f4c0ea39e43671fd9267b129af)UBX\_NAV\_PVT\_VALID\_TIME

| #define UBX\_NAV\_PVT\_VALID\_TIME   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a4ea40193fa60a75bf5ede5586da92931)UBX\_NAV\_PVT\_VALID\_UTC\_TOD

| #define UBX\_NAV\_PVT\_VALID\_UTC\_TOD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#aaaa4b2e1968a45f4c7ee336a45b4164b)UBX\_NAV\_SAT\_FLAGS\_SV\_USED

| #define UBX\_NAV\_SAT\_FLAGS\_SV\_USED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a9c66cd27732153c56d0872339bc3deae)UBX\_PAYLOAD\_SZ\_MAX

| #define UBX\_PAYLOAD\_SZ\_MAX   512 |
| --- |

## [◆ ](#a1693f3584605a0197076cba71c79b0df)UBX\_PREAMBLE\_SYNC\_CHAR\_1

| #define UBX\_PREAMBLE\_SYNC\_CHAR\_1   0xB5 |
| --- |

## [◆ ](#ad8d6229db563db619d4f0a9f225fb640)UBX\_PREAMBLE\_SYNC\_CHAR\_2

| #define UBX\_PREAMBLE\_SYNC\_CHAR\_2   0x62 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a887b1fa6af0d6d08cc51ed65de64a78a)ubx\_cfg\_char\_len

| enum [ubx\_cfg\_char\_len](#a887b1fa6af0d6d08cc51ed65de64a78a) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_5 |  |
| UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_6 |  |
| UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_7 |  |
| UBX\_CFG\_PRT\_PORT\_MODE\_CHAR\_LEN\_8 |  |

## [◆ ](#a2e5de1479afbcf20caa3300282bb0d1a)ubx\_cfg\_parity

| enum [ubx\_cfg\_parity](#a2e5de1479afbcf20caa3300282bb0d1a) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_EVEN |  |
| UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_ODD |  |
| UBX\_CFG\_PRT\_PORT\_MODE\_PARITY\_NONE |  |

## [◆ ](#adb6a6e16f193bc70840b2dd12dbc9baa)ubx\_cfg\_port\_id

| enum [ubx\_cfg\_port\_id](#adb6a6e16f193bc70840b2dd12dbc9baa) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_CFG\_PORT\_ID\_DDC |  |
| UBX\_CFG\_PORT\_ID\_UART |  |
| UBX\_CFG\_PORT\_ID\_USB |  |
| UBX\_CFG\_PORT\_ID\_SPI |  |

## [◆ ](#a621d2fae9721b6dc62a71801f3b7952e)ubx\_cfg\_rate\_time\_ref

| enum [ubx\_cfg\_rate\_time\_ref](#a621d2fae9721b6dc62a71801f3b7952e) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_CFG\_RATE\_TIME\_REF\_UTC |  |
| UBX\_CFG\_RATE\_TIME\_REF\_GPS |  |
| UBX\_CFG\_RATE\_TIME\_REF\_GLONASS |  |
| UBX\_CFG\_RATE\_TIME\_REF\_BEIDOU |  |
| UBX\_CFG\_RATE\_TIME\_REF\_GALILEO |  |
| UBX\_CFG\_RATE\_TIME\_REF\_NAVIC |  |

## [◆ ](#a5cc2a8f42fd62032afa3cd7687452896)ubx\_cfg\_rst\_mode

| enum [ubx\_cfg\_rst\_mode](#a5cc2a8f42fd62032afa3cd7687452896) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_CFG\_RST\_MODE\_HW |  |
| UBX\_CFG\_RST\_MODE\_SW |  |
| UBX\_CFG\_RST\_MODE\_GNSS\_STOP |  |
| UBX\_CFG\_RST\_MODE\_GNSS\_START |  |

## [◆ ](#a43766ad4c0fd1d31fd547c090e3f39b6)ubx\_cfg\_rst\_start\_mode

| enum [ubx\_cfg\_rst\_start\_mode](#a43766ad4c0fd1d31fd547c090e3f39b6) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_CFG\_RST\_HOT\_START |  |
| UBX\_CFG\_RST\_WARM\_START |  |
| UBX\_CFG\_RST\_COLD\_START |  |

## [◆ ](#a94709ee4f4afe0194790893251ee2b4c)ubx\_cfg\_stop\_bits

| enum [ubx\_cfg\_stop\_bits](#a94709ee4f4afe0194790893251ee2b4c) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_1 |  |
| UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_1\_5 |  |
| UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_2 |  |
| UBX\_CFG\_PRT\_PORT\_MODE\_STOP\_BITS\_0\_5 |  |

## [◆ ](#ad7e0ffe55e8dbd97caa5bc089d33540c)ubx\_cfg\_val\_ver

| enum [ubx\_cfg\_val\_ver](#ad7e0ffe55e8dbd97caa5bc089d33540c) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_CFG\_VAL\_VER\_SIMPLE |  |
| UBX\_CFG\_VAL\_VER\_TRANSACTION |  |

## [◆ ](#ad0dac3b7e7cbf3649aa5b8813e40fc18)ubx\_class\_id

| enum [ubx\_class\_id](#ad0dac3b7e7cbf3649aa5b8813e40fc18) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_CLASS\_ID\_NAV |  |
| UBX\_CLASS\_ID\_RXM |  |
| UBX\_CLASS\_ID\_INF |  |
| UBX\_CLASS\_ID\_ACK |  |
| UBX\_CLASS\_ID\_CFG |  |
| UBX\_CLASS\_ID\_UPD |  |
| UBX\_CLASS\_ID\_MON |  |
| UBX\_CLASS\_ID\_TIM |  |
| UBX\_CLASS\_ID\_MGA |  |
| UBX\_CLASS\_ID\_LOG |  |
| UBX\_CLASS\_ID\_SEC |  |
| UBX\_CLASS\_ID\_NMEA\_STD |  |
| UBX\_CLASS\_ID\_NMEA\_PUBX |  |

## [◆ ](#a9e5e9af7a281e53f2b950089ee66561f)ubx\_dyn\_model

| enum [ubx\_dyn\_model](#a9e5e9af7a281e53f2b950089ee66561f) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_DYN\_MODEL\_PORTABLE |  |
| UBX\_DYN\_MODEL\_STATIONARY |  |
| UBX\_DYN\_MODEL\_PEDESTRIAN |  |
| UBX\_DYN\_MODEL\_AUTOMOTIVE |  |
| UBX\_DYN\_MODEL\_SEA |  |
| UBX\_DYN\_MODEL\_AIRBORNE\_1G |  |
| UBX\_DYN\_MODEL\_AIRBORNE\_2G |  |
| UBX\_DYN\_MODEL\_AIRBORNE\_4G |  |
| UBX\_DYN\_MODEL\_WRIST |  |
| UBX\_DYN\_MODEL\_BIKE |  |

## [◆ ](#a342c0d62cf874ccb8b657ce85d91efe0)ubx\_fix\_mode

| enum [ubx\_fix\_mode](#a342c0d62cf874ccb8b657ce85d91efe0) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_FIX\_MODE\_2D\_ONLY |  |
| UBX\_FIX\_MODE\_3D\_ONLY |  |
| UBX\_FIX\_MODE\_AUTO |  |

## [◆ ](#a6711a33292bf25327950406b96585690)ubx\_gnss\_id

| enum [ubx\_gnss\_id](#a6711a33292bf25327950406b96585690) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_GNSS\_ID\_GPS |  |
| UBX\_GNSS\_ID\_SBAS |  |
| UBX\_GNSS\_ID\_GALILEO |  |
| UBX\_GNSS\_ID\_BEIDOU |  |
| UBX\_GNSS\_ID\_QZSS |  |
| UBX\_GNSS\_ID\_GLONASS |  |

## [◆ ](#a260c4adbe9524bd747127a4e3f14bbca)ubx\_msg\_id\_ack

| enum [ubx\_msg\_id\_ack](#a260c4adbe9524bd747127a4e3f14bbca) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_MSG\_ID\_ACK |  |
| UBX\_MSG\_ID\_NAK |  |

## [◆ ](#a3cf04300758f1802e0703428707035d7)ubx\_msg\_id\_cfg

| enum [ubx\_msg\_id\_cfg](#a3cf04300758f1802e0703428707035d7) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_MSG\_ID\_CFG\_PRT |  |
| UBX\_MSG\_ID\_CFG\_MSG |  |
| UBX\_MSG\_ID\_CFG\_RST |  |
| UBX\_MSG\_ID\_CFG\_RATE |  |
| UBX\_MSG\_ID\_CFG\_NAV5 |  |
| UBX\_MSG\_ID\_CFG\_VAL\_SET |  |
| UBX\_MSG\_ID\_CFG\_VAL\_GET |  |

## [◆ ](#a0d969e434f941cf5af7143cca0cf0fe4)ubx\_msg\_id\_mon

| enum [ubx\_msg\_id\_mon](#a0d969e434f941cf5af7143cca0cf0fe4) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_MSG\_ID\_MON\_VER |  |
| UBX\_MSG\_ID\_MON\_GNSS |  |

## [◆ ](#a8a935ea7debb4ac73ea99c98d6ef4d3b)ubx\_msg\_id\_nav

| enum [ubx\_msg\_id\_nav](#a8a935ea7debb4ac73ea99c98d6ef4d3b) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_MSG\_ID\_NAV\_PVT |  |
| UBX\_MSG\_ID\_NAV\_SAT |  |

## [◆ ](#a58dc8b84784731500aa7f55afeb7e582)ubx\_msg\_id\_nmea\_pubx

| enum [ubx\_msg\_id\_nmea\_pubx](#a58dc8b84784731500aa7f55afeb7e582) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_MSG\_ID\_NMEA\_PUBX\_CONFIG |  |
| UBX\_MSG\_ID\_NMEA\_PUBX\_POSITION |  |
| UBX\_MSG\_ID\_NMEA\_PUBX\_RATE |  |
| UBX\_MSG\_ID\_NMEA\_PUBX\_SVSTATUS |  |
| UBX\_MSG\_ID\_NMEA\_PUBX\_TIME |  |

## [◆ ](#aa221b68c53f25634d9f2f435f28c1a6c)ubx\_msg\_id\_nmea\_std

| enum [ubx\_msg\_id\_nmea\_std](#aa221b68c53f25634d9f2f435f28c1a6c) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_MSG\_ID\_NMEA\_STD\_DTM |  |
| UBX\_MSG\_ID\_NMEA\_STD\_GBQ |  |
| UBX\_MSG\_ID\_NMEA\_STD\_GBS |  |
| UBX\_MSG\_ID\_NMEA\_STD\_GGA |  |
| UBX\_MSG\_ID\_NMEA\_STD\_GLL |  |
| UBX\_MSG\_ID\_NMEA\_STD\_GLQ |  |
| UBX\_MSG\_ID\_NMEA\_STD\_GNQ |  |
| UBX\_MSG\_ID\_NMEA\_STD\_GNS |  |
| UBX\_MSG\_ID\_NMEA\_STD\_GPQ |  |
| UBX\_MSG\_ID\_NMEA\_STD\_GRS |  |
| UBX\_MSG\_ID\_NMEA\_STD\_GSA |  |
| UBX\_MSG\_ID\_NMEA\_STD\_GST |  |
| UBX\_MSG\_ID\_NMEA\_STD\_GSV |  |
| UBX\_MSG\_ID\_NMEA\_STD\_RMC |  |
| UBX\_MSG\_ID\_NMEA\_STD\_THS |  |
| UBX\_MSG\_ID\_NMEA\_STD\_TXT |  |
| UBX\_MSG\_ID\_NMEA\_STD\_VLW |  |
| UBX\_MSG\_ID\_NMEA\_STD\_VTG |  |
| UBX\_MSG\_ID\_NMEA\_STD\_ZDA |  |

## [◆ ](#a173b6c1016562da43b8131b8d8f04fef)ubx\_nav\_fix\_type

| enum [ubx\_nav\_fix\_type](#a173b6c1016562da43b8131b8d8f04fef) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_NAV\_FIX\_TYPE\_NO\_FIX |  |
| UBX\_NAV\_FIX\_TYPE\_DR |  |
| UBX\_NAV\_FIX\_TYPE\_2D |  |
| UBX\_NAV\_FIX\_TYPE\_3D |  |
| UBX\_NAV\_FIX\_TYPE\_GNSS\_DR\_COMBINED |  |
| UBX\_NAV\_FIX\_TYPE\_TIME\_ONLY |  |

## [◆ ](#afbba8ada09d6c6489d52a3b9dc31725f)ubx\_nav\_sat\_health

| enum [ubx\_nav\_sat\_health](#afbba8ada09d6c6489d52a3b9dc31725f) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_NAV\_SAT\_HEALTH\_UNKNOWN |  |
| UBX\_NAV\_SAT\_HEALTH\_HEALTHY |  |
| UBX\_NAV\_SAT\_HEALTH\_UNHEALTHY |  |

## [◆ ](#a359b0f88d3769af43c2b1699eb172f23)ubx\_utc\_standard

| enum [ubx\_utc\_standard](#a359b0f88d3769af43c2b1699eb172f23) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_UTC\_STANDARD\_AUTOMATIC |  |
| UBX\_UTC\_STANDARD\_GPS |  |
| UBX\_UTC\_STANDARD\_GALILEO |  |
| UBX\_UTC\_STANDARD\_GLONASS |  |
| UBX\_UTC\_STANDARD\_BEIDOU |  |

## Function Documentation

## [◆ ](#a450f46250ef486af4f933e69ddbb42d2)ubx\_calc\_checksum()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ubx\_calc\_checksum | ( | const struct [ubx\_frame](structubx__frame.md) \* | *frame*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Mismatch in expected and actual length results in an invalid frame

## [◆ ](#acdc0d9b7d25df6aba6bb091e7034f5ba)ubx\_frame\_encode()

| | int ubx\_frame\_encode | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *class*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id*, | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *payload*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *payload\_len*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buf\_len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ubx](dir_0a499179f9adf90767e72c7eb481b4fc.md)
- [protocol.h](modem_2ubx_2protocol_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
