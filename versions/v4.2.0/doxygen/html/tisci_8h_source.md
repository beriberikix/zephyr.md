---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/tisci_8h_source.html
original_path: doxygen/html/tisci_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tisci.h

[Go to the documentation of this file.](tisci_8h.md)

1/\*

2 \* Copyright (c) 2025, Texas Instruments

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef INCLUDE\_ZEPHYR\_DRIVERS\_TISCI\_H\_

14#define INCLUDE\_ZEPHYR\_DRIVERS\_TISCI\_H\_

15

16#include <[zephyr/device.h](device_8h.md)>

17

[ 18](tisci_8h.md#a396f8869a1aee7aa1b88a039a17746bf)#define MAILBOX\_MBOX\_SIZE 60

19

[ 30](structtisci__version__info.md)struct [tisci\_version\_info](structtisci__version__info.md) {

[ 31](structtisci__version__info.md#a7371d69f5f0993dfd1e582c165d2ddc5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [abi\_major](structtisci__version__info.md#a7371d69f5f0993dfd1e582c165d2ddc5);

[ 32](structtisci__version__info.md#a8547f04843609b8a324ea4ecb91c17a7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [abi\_minor](structtisci__version__info.md#a8547f04843609b8a324ea4ecb91c17a7);

[ 33](structtisci__version__info.md#a711c9ca4b063958fcb46ad0e298caa27) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [firmware\_revision](structtisci__version__info.md#a711c9ca4b063958fcb46ad0e298caa27);

[ 34](structtisci__version__info.md#a62cb5c8e86a94dbf53430d73c9f241a9) char [firmware\_description](structtisci__version__info.md#a62cb5c8e86a94dbf53430d73c9f241a9)[32];

35};

36

[ 54](structtisci__msg__fwl__region.md)struct [tisci\_msg\_fwl\_region](structtisci__msg__fwl__region.md) {

[ 55](structtisci__msg__fwl__region.md#ab3b3ae28613a3ef9e7c83b9d2af9f4ce) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fwl\_id](structtisci__msg__fwl__region.md#ab3b3ae28613a3ef9e7c83b9d2af9f4ce);

[ 56](structtisci__msg__fwl__region.md#a2cb0672482a7859294a1c95b7f42d265) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [region](structtisci__msg__fwl__region.md#a2cb0672482a7859294a1c95b7f42d265);

[ 57](structtisci__msg__fwl__region.md#aae2b9a8670d5e799347606d48408980f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [n\_permission\_regs](structtisci__msg__fwl__region.md#aae2b9a8670d5e799347606d48408980f);

[ 58](structtisci__msg__fwl__region.md#a4e5c3b596b1e60524ac386c8506c3870) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [control](structtisci__msg__fwl__region.md#a4e5c3b596b1e60524ac386c8506c3870);

[ 59](structtisci__msg__fwl__region.md#a4c091b340c1dc21f866d623489ab8451) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [permissions](structtisci__msg__fwl__region.md#a4c091b340c1dc21f866d623489ab8451)[3];

[ 60](structtisci__msg__fwl__region.md#a4378cc7f160a86af3708284a7cb068a6) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [start\_address](structtisci__msg__fwl__region.md#a4378cc7f160a86af3708284a7cb068a6);

[ 61](structtisci__msg__fwl__region.md#a789bcad9536d23d0cca4e8791f01c95c) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [end\_address](structtisci__msg__fwl__region.md#a789bcad9536d23d0cca4e8791f01c95c);

62};

63

[ 82](structtisci__msg__fwl__owner.md)struct [tisci\_msg\_fwl\_owner](structtisci__msg__fwl__owner.md) {

[ 83](structtisci__msg__fwl__owner.md#a370a1aff0233b53b035cbcd7b4c264b5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fwl\_id](structtisci__msg__fwl__owner.md#a370a1aff0233b53b035cbcd7b4c264b5);

[ 84](structtisci__msg__fwl__owner.md#a7ccaf9d3c1bd3639e8c170acd5d535a8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [region](structtisci__msg__fwl__owner.md#a7ccaf9d3c1bd3639e8c170acd5d535a8);

[ 85](structtisci__msg__fwl__owner.md#a2010d9ee65f9a94e5477a0fc1f21774e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [owner\_index](structtisci__msg__fwl__owner.md#a2010d9ee65f9a94e5477a0fc1f21774e);

[ 86](structtisci__msg__fwl__owner.md#a5e5e33a9a2f7c04022ce51fa1dcb8eef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [owner\_privid](structtisci__msg__fwl__owner.md#a5e5e33a9a2f7c04022ce51fa1dcb8eef);

[ 87](structtisci__msg__fwl__owner.md#a31ec3f0e90fdb8cea887d67004b066a7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [owner\_permission\_bits](structtisci__msg__fwl__owner.md#a31ec3f0e90fdb8cea887d67004b066a7);

88};

89

[ 96](structtisci__msg__rm__udmap__tx__ch__cfg.md)struct [tisci\_msg\_rm\_udmap\_tx\_ch\_cfg](structtisci__msg__rm__udmap__tx__ch__cfg.md) {

[ 97](structtisci__msg__rm__udmap__tx__ch__cfg.md#acb243dd0b94ab38fa50ddd14a758b33a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [valid\_params](structtisci__msg__rm__udmap__tx__ch__cfg.md#acb243dd0b94ab38fa50ddd14a758b33a);

[ 98](tisci_8h.md#a736e0c626ee9d1df858ce5936bf4029e)#define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_FILT\_EINFO\_VALID BIT(9)

[ 99](tisci_8h.md#a6db1d6169cc2def41e73ce4c22fa118e)#define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_FILT\_PSWORDS\_VALID BIT(10)

[ 100](tisci_8h.md#a64195889325d54d493923b95620b1550)#define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_SUPR\_TDPKT\_VALID BIT(11)

[ 101](tisci_8h.md#a1110504d079ae51a526ed80144560b27)#define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_CREDIT\_COUNT\_VALID BIT(12)

[ 102](tisci_8h.md#af8dbd5c7af94ec3690012458d35f2456)#define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_FDEPTH\_VALID BIT(13)

[ 103](tisci_8h.md#a4de2b535f4d2548218dde6c2dddc9448)#define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_TDTYPE\_VALID BIT(15)

[ 104](tisci_8h.md#abb692a88d05498a4c0dd5e69857cda92)#define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_EXTENDED\_CH\_TYPE\_VALID BIT(16)

[ 105](structtisci__msg__rm__udmap__tx__ch__cfg.md#a646845b965fee520329a118ade711f02) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [nav\_id](structtisci__msg__rm__udmap__tx__ch__cfg.md#a646845b965fee520329a118ade711f02);

[ 106](structtisci__msg__rm__udmap__tx__ch__cfg.md#ab8327c9b3896c8294f47349572546e70) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [index](structtisci__msg__rm__udmap__tx__ch__cfg.md#ab8327c9b3896c8294f47349572546e70);

[ 107](structtisci__msg__rm__udmap__tx__ch__cfg.md#ad255f2c020bfc237f5f22a747e68c1b8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_pause\_on\_err](structtisci__msg__rm__udmap__tx__ch__cfg.md#ad255f2c020bfc237f5f22a747e68c1b8);

[ 108](structtisci__msg__rm__udmap__tx__ch__cfg.md#a9d298e2ae456dcad3cbfdce595f0655c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_filt\_einfo](structtisci__msg__rm__udmap__tx__ch__cfg.md#a9d298e2ae456dcad3cbfdce595f0655c);

[ 109](structtisci__msg__rm__udmap__tx__ch__cfg.md#ab9a869848d253d09f9fafc91dc8958cc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_filt\_pswords](structtisci__msg__rm__udmap__tx__ch__cfg.md#ab9a869848d253d09f9fafc91dc8958cc);

[ 110](structtisci__msg__rm__udmap__tx__ch__cfg.md#a75147fe8091db6c41050ded22c9eefa3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_atype](structtisci__msg__rm__udmap__tx__ch__cfg.md#a75147fe8091db6c41050ded22c9eefa3);

[ 111](structtisci__msg__rm__udmap__tx__ch__cfg.md#a14b9ea920df0ff044bd9cf45c2084f3a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_chan\_type](structtisci__msg__rm__udmap__tx__ch__cfg.md#a14b9ea920df0ff044bd9cf45c2084f3a);

[ 112](structtisci__msg__rm__udmap__tx__ch__cfg.md#aaa18a6837a0271781164a353ce729623) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_supr\_tdpkt](structtisci__msg__rm__udmap__tx__ch__cfg.md#aaa18a6837a0271781164a353ce729623);

[ 113](structtisci__msg__rm__udmap__tx__ch__cfg.md#afd02dd108fd620f1bc9d66fac5a3e775) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_fetch\_size](structtisci__msg__rm__udmap__tx__ch__cfg.md#afd02dd108fd620f1bc9d66fac5a3e775);

[ 114](structtisci__msg__rm__udmap__tx__ch__cfg.md#a90a701c601691c79cd37192fac02d052) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_credit\_count](structtisci__msg__rm__udmap__tx__ch__cfg.md#a90a701c601691c79cd37192fac02d052);

[ 115](structtisci__msg__rm__udmap__tx__ch__cfg.md#a89f3ac8683240274b5bbc635e08b659f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [txcq\_qnum](structtisci__msg__rm__udmap__tx__ch__cfg.md#a89f3ac8683240274b5bbc635e08b659f);

[ 116](structtisci__msg__rm__udmap__tx__ch__cfg.md#aeaf51ae045dbc4079c02d61f13e487ed) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_priority](structtisci__msg__rm__udmap__tx__ch__cfg.md#aeaf51ae045dbc4079c02d61f13e487ed);

[ 117](structtisci__msg__rm__udmap__tx__ch__cfg.md#af377d65e1fb43ed7fceda8a0665605d0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_qos](structtisci__msg__rm__udmap__tx__ch__cfg.md#af377d65e1fb43ed7fceda8a0665605d0);

[ 118](structtisci__msg__rm__udmap__tx__ch__cfg.md#ada34a3a63d1ed339a86804f906d4dbc5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_orderid](structtisci__msg__rm__udmap__tx__ch__cfg.md#ada34a3a63d1ed339a86804f906d4dbc5);

[ 119](structtisci__msg__rm__udmap__tx__ch__cfg.md#ad8aec84ccd12e9f02c4cafac7eadb4a4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fdepth](structtisci__msg__rm__udmap__tx__ch__cfg.md#ad8aec84ccd12e9f02c4cafac7eadb4a4);

[ 120](structtisci__msg__rm__udmap__tx__ch__cfg.md#a01334fae8a1e94ffbbba28d9c59ed0b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_sched\_priority](structtisci__msg__rm__udmap__tx__ch__cfg.md#a01334fae8a1e94ffbbba28d9c59ed0b1);

[ 121](structtisci__msg__rm__udmap__tx__ch__cfg.md#a7e0bfdb950b1b285ddc0e58282bc224b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_burst\_size](structtisci__msg__rm__udmap__tx__ch__cfg.md#a7e0bfdb950b1b285ddc0e58282bc224b);

[ 122](structtisci__msg__rm__udmap__tx__ch__cfg.md#ab36b40f8989fa7cdc5419bc0e9dd5a68) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_tdtype](structtisci__msg__rm__udmap__tx__ch__cfg.md#ab36b40f8989fa7cdc5419bc0e9dd5a68);

[ 123](structtisci__msg__rm__udmap__tx__ch__cfg.md#a37b6f2565ccdf51fcc09801a72fde7e4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [extended\_ch\_type](structtisci__msg__rm__udmap__tx__ch__cfg.md#a37b6f2565ccdf51fcc09801a72fde7e4);

124};

125

[ 132](structtisci__msg__rm__udmap__rx__ch__cfg.md)struct [tisci\_msg\_rm\_udmap\_rx\_ch\_cfg](structtisci__msg__rm__udmap__rx__ch__cfg.md) {

[ 133](structtisci__msg__rm__udmap__rx__ch__cfg.md#a88fa4f4bf94a290a035419a65054b544) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [valid\_params](structtisci__msg__rm__udmap__rx__ch__cfg.md#a88fa4f4bf94a290a035419a65054b544);

[ 134](tisci_8h.md#ae0c03a2c76f884f37f472b081d0dd028)#define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_FLOWID\_START\_VALID BIT(9)

[ 135](tisci_8h.md#a04febde272953c690f94d44db18663f7)#define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_FLOWID\_CNT\_VALID BIT(10)

[ 136](tisci_8h.md#a512091ff6dff198c2801a8f51fe18755)#define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_IGNORE\_SHORT\_VALID BIT(11)

[ 137](tisci_8h.md#a818ed2617f42b219d3e3aed2a46ed7d8)#define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_IGNORE\_LONG\_VALID BIT(12)

[ 138](structtisci__msg__rm__udmap__rx__ch__cfg.md#a691a478fa65af24279638789433dca6f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [nav\_id](structtisci__msg__rm__udmap__rx__ch__cfg.md#a691a478fa65af24279638789433dca6f);

[ 139](structtisci__msg__rm__udmap__rx__ch__cfg.md#a459ca9cb93410be5747595a57d88c7ed) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [index](structtisci__msg__rm__udmap__rx__ch__cfg.md#a459ca9cb93410be5747595a57d88c7ed);

[ 140](structtisci__msg__rm__udmap__rx__ch__cfg.md#ad57a6d0dca932c95cff2a4675dc72990) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rx\_fetch\_size](structtisci__msg__rm__udmap__rx__ch__cfg.md#ad57a6d0dca932c95cff2a4675dc72990);

[ 141](structtisci__msg__rm__udmap__rx__ch__cfg.md#a554db2ab8742b2f15a6c7531638a6d74) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rxcq\_qnum](structtisci__msg__rm__udmap__rx__ch__cfg.md#a554db2ab8742b2f15a6c7531638a6d74);

[ 142](structtisci__msg__rm__udmap__rx__ch__cfg.md#a03ec736938d7b3eb05fcd56c62fd736a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_priority](structtisci__msg__rm__udmap__rx__ch__cfg.md#a03ec736938d7b3eb05fcd56c62fd736a);

[ 143](structtisci__msg__rm__udmap__rx__ch__cfg.md#a54f4136011d83df5441004dde0d5e696) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_qos](structtisci__msg__rm__udmap__rx__ch__cfg.md#a54f4136011d83df5441004dde0d5e696);

[ 144](structtisci__msg__rm__udmap__rx__ch__cfg.md#a9782a0a412413087ecf669beed77ff77) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_orderid](structtisci__msg__rm__udmap__rx__ch__cfg.md#a9782a0a412413087ecf669beed77ff77);

[ 145](structtisci__msg__rm__udmap__rx__ch__cfg.md#a4e9720567203889d41fdccb769d56025) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_sched\_priority](structtisci__msg__rm__udmap__rx__ch__cfg.md#a4e9720567203889d41fdccb769d56025);

[ 146](structtisci__msg__rm__udmap__rx__ch__cfg.md#abde08f01f02f26e1538cd82d9e87b19a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flowid\_start](structtisci__msg__rm__udmap__rx__ch__cfg.md#abde08f01f02f26e1538cd82d9e87b19a);

[ 147](structtisci__msg__rm__udmap__rx__ch__cfg.md#ac10643f49f4d685af2bf14bb7b9b90f0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flowid\_cnt](structtisci__msg__rm__udmap__rx__ch__cfg.md#ac10643f49f4d685af2bf14bb7b9b90f0);

[ 148](structtisci__msg__rm__udmap__rx__ch__cfg.md#ad008f77af3d4edbfeedb863ee2f8dcd0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_pause\_on\_err](structtisci__msg__rm__udmap__rx__ch__cfg.md#ad008f77af3d4edbfeedb863ee2f8dcd0);

[ 149](structtisci__msg__rm__udmap__rx__ch__cfg.md#a7a36a9e37b22229c6ec90528aa7f9a9c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_atype](structtisci__msg__rm__udmap__rx__ch__cfg.md#a7a36a9e37b22229c6ec90528aa7f9a9c);

[ 150](structtisci__msg__rm__udmap__rx__ch__cfg.md#aecf4e3eaaa8b8c604504eb525d3e1a5f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_chan\_type](structtisci__msg__rm__udmap__rx__ch__cfg.md#aecf4e3eaaa8b8c604504eb525d3e1a5f);

[ 151](structtisci__msg__rm__udmap__rx__ch__cfg.md#ab1245dc9783e74cd3cb1fcb648714e76) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_ignore\_short](structtisci__msg__rm__udmap__rx__ch__cfg.md#ab1245dc9783e74cd3cb1fcb648714e76);

[ 152](structtisci__msg__rm__udmap__rx__ch__cfg.md#a8e9b939089204b70469afedcb6c5ad8c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_ignore\_long](structtisci__msg__rm__udmap__rx__ch__cfg.md#a8e9b939089204b70469afedcb6c5ad8c);

[ 153](structtisci__msg__rm__udmap__rx__ch__cfg.md#a57c0675af1fdefd1c270d11183fa77d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_burst\_size](structtisci__msg__rm__udmap__rx__ch__cfg.md#a57c0675af1fdefd1c270d11183fa77d6);

154};

155

[ 156](tisci_8h.md#ae309074218959da90a5978304c34e916)#define TISCI\_MSG\_VALUE\_RM\_DST\_ID\_VALID (1u << 0u)

[ 157](tisci_8h.md#a69aa4a4b3a5e99a86adbc6a0ccf74560)#define TISCI\_MSG\_VALUE\_RM\_DST\_HOST\_IRQ\_VALID (1u << 1u)

[ 158](tisci_8h.md#abf34b43187cdc7ea4b68ee151816d97a)#define TISCI\_MSG\_VALUE\_RM\_IA\_ID\_VALID (1u << 2u)

[ 159](tisci_8h.md#a334a7f7a6fd37286c5635f1cfe2d061f)#define TISCI\_MSG\_VALUE\_RM\_VINT\_VALID (1u << 3u)

[ 160](tisci_8h.md#aad5b430c5924f794b35cfb7c9830b48b)#define TISCI\_MSG\_VALUE\_RM\_GLOBAL\_EVENT\_VALID (1u << 4u)

[ 161](tisci_8h.md#ae2c0b651fc864d6904bfef4fdacb2aea)#define TISCI\_MSG\_VALUE\_RM\_VINT\_STATUS\_BIT\_INDEX\_VALID (1u << 5u)

162

[ 187](structtisci__irq__set__req.md)struct [tisci\_irq\_set\_req](structtisci__irq__set__req.md) {

[ 188](structtisci__irq__set__req.md#ac5dddf4f1bc933e82eb7dfdfdfb35307) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [valid\_params](structtisci__irq__set__req.md#ac5dddf4f1bc933e82eb7dfdfdfb35307);

[ 189](structtisci__irq__set__req.md#af1c6cc734902f14d51ff46c971c1a576) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [src\_id](structtisci__irq__set__req.md#af1c6cc734902f14d51ff46c971c1a576);

[ 190](structtisci__irq__set__req.md#a290247006f410254d3a4dbcdefc0ba75) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [src\_index](structtisci__irq__set__req.md#a290247006f410254d3a4dbcdefc0ba75);

[ 191](structtisci__irq__set__req.md#a2a17ba4d83290d1ca8ae8bf39760a31a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dst\_id](structtisci__irq__set__req.md#a2a17ba4d83290d1ca8ae8bf39760a31a);

[ 192](structtisci__irq__set__req.md#a1b01430d7e9140891589f0e48e79590a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dst\_host\_irq](structtisci__irq__set__req.md#a1b01430d7e9140891589f0e48e79590a);

[ 193](structtisci__irq__set__req.md#a2b8fd0bc0825d47fba8c961f68fcaef4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ia\_id](structtisci__irq__set__req.md#a2b8fd0bc0825d47fba8c961f68fcaef4);

[ 194](structtisci__irq__set__req.md#a2e3dd0054d9d0b029a6821f4df0af4ea) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vint](structtisci__irq__set__req.md#a2e3dd0054d9d0b029a6821f4df0af4ea);

[ 195](structtisci__irq__set__req.md#ab5f9849aef439771e81daf6a98303d17) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [global\_event](structtisci__irq__set__req.md#ab5f9849aef439771e81daf6a98303d17);

[ 196](structtisci__irq__set__req.md#a94ad73384be1f64054829a32ad70b066) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vint\_status\_bit\_index](structtisci__irq__set__req.md#a94ad73384be1f64054829a32ad70b066);

[ 197](structtisci__irq__set__req.md#ad122a8cf2af3f3df9615c3ca70ed3b06) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [secondary\_host](structtisci__irq__set__req.md#ad122a8cf2af3f3df9615c3ca70ed3b06);

198};

199

223

[ 224](structtisci__irq__release__req.md)struct [tisci\_irq\_release\_req](structtisci__irq__release__req.md) {

[ 225](structtisci__irq__release__req.md#a068b9b4217d606f03898bdca2219bbf0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [valid\_params](structtisci__irq__release__req.md#a068b9b4217d606f03898bdca2219bbf0);

[ 226](structtisci__irq__release__req.md#adddef8e01c4ecd9b44327418bcc8a3ef) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [src\_id](structtisci__irq__release__req.md#adddef8e01c4ecd9b44327418bcc8a3ef);

[ 227](structtisci__irq__release__req.md#abb9cedc15e5923125e57f153ee1ed22a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [src\_index](structtisci__irq__release__req.md#abb9cedc15e5923125e57f153ee1ed22a);

[ 228](structtisci__irq__release__req.md#ae646b23593b5f724fca6800c5c2e76bf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dst\_id](structtisci__irq__release__req.md#ae646b23593b5f724fca6800c5c2e76bf);

[ 229](structtisci__irq__release__req.md#a3643554ea453300f33806b5128cc6c0a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dst\_host\_irq](structtisci__irq__release__req.md#a3643554ea453300f33806b5128cc6c0a);

[ 230](structtisci__irq__release__req.md#aa6c09862a5e955a5ccbb78c7df2675fa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ia\_id](structtisci__irq__release__req.md#aa6c09862a5e955a5ccbb78c7df2675fa);

[ 231](structtisci__irq__release__req.md#a754e7c93d218a58e2bc18fd4ec086e40) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vint](structtisci__irq__release__req.md#a754e7c93d218a58e2bc18fd4ec086e40);

[ 232](structtisci__irq__release__req.md#a12eb81324f28254daece1170b1e6764d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [global\_event](structtisci__irq__release__req.md#a12eb81324f28254daece1170b1e6764d);

[ 233](structtisci__irq__release__req.md#aedc07d5425720146b75b6757ca17c0d3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vint\_status\_bit\_index](structtisci__irq__release__req.md#aedc07d5425720146b75b6757ca17c0d3);

[ 234](structtisci__irq__release__req.md#a032e94a7d3c7384dc1f36c08b2d73e71) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [secondary\_host](structtisci__irq__release__req.md#a032e94a7d3c7384dc1f36c08b2d73e71);

235};

236

237/\* Version/Revision Functions \*/

238

[ 250](tisci_8h.md#aea0b9addbd3cfcb2be691f0801128fe1)int [tisci\_cmd\_get\_revision](tisci_8h.md#aea0b9addbd3cfcb2be691f0801128fe1)(const struct [device](structdevice.md) \*dev, struct [tisci\_version\_info](structtisci__version__info.md) \*ver);

251

252/\* Clock Management Functions \*/

253

[ 265](tisci_8h.md#a3f8128fa6c8c6f10bb7e302e6e9cfeaf)int [tisci\_cmd\_get\_clock\_state](tisci_8h.md#a3f8128fa6c8c6f10bb7e302e6e9cfeaf)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id,

266 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*programmed\_state, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*current\_state);

267

[ 279](tisci_8h.md#a086d96bed3d789bf303f56405a791aa6)int [tisci\_set\_clock\_state](tisci_8h.md#a086d96bed3d789bf303f56405a791aa6)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

280 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

281

[ 293](tisci_8h.md#a7f0bafa6005d46d2786db590a27add25)int [tisci\_cmd\_clk\_is\_on](tisci_8h.md#a7f0bafa6005d46d2786db590a27add25)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, bool \*req\_state,

294 bool \*curr\_state);

295

[ 307](tisci_8h.md#a20276a83e2037db6895085770353a194)int [tisci\_cmd\_clk\_is\_off](tisci_8h.md#a20276a83e2037db6895085770353a194)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, bool \*req\_state,

308 bool \*curr\_state);

309

[ 320](tisci_8h.md#aaebb0012c291ded1b9303d634b1bb245)int [tisci\_cmd\_clk\_is\_auto](tisci_8h.md#aaebb0012c291ded1b9303d634b1bb245)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id,

321 bool \*req\_state);

322

[ 333](tisci_8h.md#a5c69f5f12b79a0b37a1f704624106960)int [tisci\_cmd\_clk\_get\_freq](tisci_8h.md#a5c69f5f12b79a0b37a1f704624106960)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id,

334 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*freq);

335

[ 348](tisci_8h.md#ad3563b7ec2fa13eb4b1faa564062ae12)int [tisci\_cmd\_clk\_set\_freq](tisci_8h.md#ad3563b7ec2fa13eb4b1faa564062ae12)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id,

349 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) min\_freq, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) target\_freq, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) max\_freq);

350

[ 366](tisci_8h.md#a9801b388e5dc60f10aa624040cb8bfe2)int [tisci\_cmd\_clk\_get\_match\_freq](tisci_8h.md#a9801b388e5dc60f10aa624040cb8bfe2)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id,

367 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) min\_freq, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) target\_freq, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) max\_freq,

368 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*match\_freq);

369

[ 380](tisci_8h.md#a6ad9804cf3e23246955bcab1e98aecdb)int [tisci\_cmd\_clk\_set\_parent](tisci_8h.md#a6ad9804cf3e23246955bcab1e98aecdb)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id,

381 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) parent\_id);

382

[ 393](tisci_8h.md#a86e0ed2c8711363dc5ea710b12a303af)int [tisci\_cmd\_clk\_get\_parent](tisci_8h.md#a86e0ed2c8711363dc5ea710b12a303af)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id,

394 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*parent\_id);

395

[ 406](tisci_8h.md#ae93fb7c70a4f2299415a51b993d36741)int [tisci\_cmd\_clk\_get\_num\_parents](tisci_8h.md#ae93fb7c70a4f2299415a51b993d36741)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id,

407 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*num\_parents);

408

[ 421](tisci_8h.md#ab63106de04e579ba18f34763b3efa8b3)int [tisci\_cmd\_get\_clock](tisci_8h.md#ab63106de04e579ba18f34763b3efa8b3)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, bool needs\_ssc,

422 bool can\_change\_freq, bool enable\_input\_term);

423

[ 433](tisci_8h.md#a3d39780a18358066ec8f187474c18f71)int [tisci\_cmd\_idle\_clock](tisci_8h.md#a3d39780a18358066ec8f187474c18f71)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id);

434

[ 444](tisci_8h.md#ae48c6c78db3f4bee6520c0af66e37e7d)int [tisci\_cmd\_put\_clock](tisci_8h.md#ae48c6c78db3f4bee6520c0af66e37e7d)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id);

445

446/\* Device Management Functions \*/

447

[ 462](tisci_8h.md#a8b6d6f99df32eeba9131ce130ee4f12d)int [tisci\_set\_device\_state](tisci_8h.md#a8b6d6f99df32eeba9131ce130ee4f12d)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

463 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

464

[ 479](tisci_8h.md#a05f871388f68d9c71620ea43bde1e3ab)int [tisci\_set\_device\_state\_no\_wait](tisci_8h.md#a05f871388f68d9c71620ea43bde1e3ab)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

480 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

481

[ 494](tisci_8h.md#ada78c57b3cb24e57a3f6cc155e3a3d09)int [tisci\_get\_device\_state](tisci_8h.md#ada78c57b3cb24e57a3f6cc155e3a3d09)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*clcnt,

495 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*resets, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*p\_state, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*c\_state);

496

[ 505](tisci_8h.md#a4011bbe29370fb581ab2dd0fcaa151db)int [tisci\_cmd\_get\_device](tisci_8h.md#a4011bbe29370fb581ab2dd0fcaa151db)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id);

[ 506](tisci_8h.md#adc16227f1ec150d0c6cf32442fa3e915)int [tisci\_cmd\_get\_device\_exclusive](tisci_8h.md#adc16227f1ec150d0c6cf32442fa3e915)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id);

507

[ 516](tisci_8h.md#ab8203c5d0b699ec726a889e7027ae034)int [tisci\_cmd\_idle\_device](tisci_8h.md#ab8203c5d0b699ec726a889e7027ae034)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id);

[ 517](tisci_8h.md#aab1720913f75a771e041e2195b9deede)int [tisci\_cmd\_idle\_device\_exclusive](tisci_8h.md#aab1720913f75a771e041e2195b9deede)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id);

518

[ 527](tisci_8h.md#a5a7c9ff34ad1ffa87c62fef6b2ac8719)int [tisci\_cmd\_put\_device](tisci_8h.md#a5a7c9ff34ad1ffa87c62fef6b2ac8719)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id);

528

[ 537](tisci_8h.md#a4f4072f951c0ebbeb75e8cd2f06b6e8f)int [tisci\_cmd\_dev\_is\_valid](tisci_8h.md#a4f4072f951c0ebbeb75e8cd2f06b6e8f)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id);

538

[ 548](tisci_8h.md#a01393f21cb5a88388ce51e36ba1843fc)int [tisci\_cmd\_dev\_get\_clcnt](tisci_8h.md#a01393f21cb5a88388ce51e36ba1843fc)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*count);

549

[ 559](tisci_8h.md#af9ff6eee5bca675c50c28fbc4af3048c)int [tisci\_cmd\_dev\_is\_idle](tisci_8h.md#af9ff6eee5bca675c50c28fbc4af3048c)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, bool \*r\_state);

560

[ 571](tisci_8h.md#a1a441bdad9bfef9a0136f0b737c9c7aa)int [tisci\_cmd\_dev\_is\_stop](tisci_8h.md#a1a441bdad9bfef9a0136f0b737c9c7aa)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, bool \*r\_state,

572 bool \*curr\_state);

573

[ 584](tisci_8h.md#aa7bb463be840666d87a68c1e65496b19)int [tisci\_cmd\_dev\_is\_on](tisci_8h.md#aa7bb463be840666d87a68c1e65496b19)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, bool \*r\_state, bool \*curr\_state);

585

[ 595](tisci_8h.md#a4a3b7acb3098f71b2a9f85fbb318d595)int [tisci\_cmd\_dev\_is\_trans](tisci_8h.md#a4a3b7acb3098f71b2a9f85fbb318d595)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, bool \*curr\_state);

596

[ 606](tisci_8h.md#a94f43ead8c81320f651fa9c0450a2493)int [tisci\_cmd\_set\_device\_resets](tisci_8h.md#a94f43ead8c81320f651fa9c0450a2493)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reset\_state);

607

[ 617](tisci_8h.md#a90613df222309651abc1adb2f4d82272)int [tisci\_cmd\_get\_device\_resets](tisci_8h.md#a90613df222309651abc1adb2f4d82272)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*reset\_state);

618

619/\* Resource Management Functions \*/

620

[ 633](tisci_8h.md#a8ced32499c14aae81994368d4450422d)int [tisci\_get\_resource\_range](tisci_8h.md#a8ced32499c14aae81994368d4450422d)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subtype,

634 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) s\_host, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*range\_start, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*range\_num);

635

[ 647](tisci_8h.md#ae249d114c60b6b1a76f7de8dab5c3ce1)int [tisci\_cmd\_get\_resource\_range](tisci_8h.md#ae249d114c60b6b1a76f7de8dab5c3ce1)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subtype,

648 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*range\_start, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*range\_num);

649

[ 662](tisci_8h.md#aa261b08c9141360c5f4f9e50ab151ed5)int [tisci\_cmd\_get\_resource\_range\_from\_shost](tisci_8h.md#aa261b08c9141360c5f4f9e50ab151ed5)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id,

663 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subtype, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) s\_host, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*range\_start,

664 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*range\_num);

665

666/\* Processor Management Functions \*/

667

[ 676](tisci_8h.md#a3181b68860761b0060048a01d71888a8)int [tisci\_cmd\_proc\_request](tisci_8h.md#a3181b68860761b0060048a01d71888a8)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id);

677

[ 686](tisci_8h.md#a2e0e3e88c635a4e6399941696056b8a9)int [tisci\_cmd\_proc\_release](tisci_8h.md#a2e0e3e88c635a4e6399941696056b8a9)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id);

687

[ 698](tisci_8h.md#a1acfab0f8fd3b1db050f97aa21d26ce3)int [tisci\_cmd\_proc\_handover](tisci_8h.md#a1acfab0f8fd3b1db050f97aa21d26ce3)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) host\_id);

699

[ 711](tisci_8h.md#a3551276e98c3f03ea4beb9086c3b89c3)int [tisci\_cmd\_set\_proc\_boot\_cfg](tisci_8h.md#a3551276e98c3f03ea4beb9086c3b89c3)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) bootvector,

712 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) config\_flags\_set, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) config\_flags\_clear);

713

[ 724](tisci_8h.md#aee60c2eb75e6786b91d9dc73c7a7e2c6)int [tisci\_cmd\_set\_proc\_boot\_ctrl](tisci_8h.md#aee60c2eb75e6786b91d9dc73c7a7e2c6)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id,

725 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) control\_flags\_set, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) control\_flags\_clear);

726

[ 736](tisci_8h.md#aaa3b1c5f5072b40e2eb1c626cb6f6f29)int [tisci\_cmd\_proc\_auth\_boot\_image](tisci_8h.md#aaa3b1c5f5072b40e2eb1c626cb6f6f29)(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*image\_addr,

737 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*image\_size);

738

[ 751](tisci_8h.md#a9e057dd13353ccdd7df3b2263ef22940)int [tisci\_cmd\_get\_proc\_boot\_status](tisci_8h.md#a9e057dd13353ccdd7df3b2263ef22940)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*bv,

752 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cfg\_flags, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ctrl\_flags, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*sts\_flags);

753

[ 771](tisci_8h.md#a8a29455ba732efa082c1a72922f46f9e)int [tisci\_proc\_wait\_boot\_status\_no\_wait](tisci_8h.md#a8a29455ba732efa082c1a72922f46f9e)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id,

772 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_wait\_iterations, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_match\_iterations,

773 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) delay\_per\_iteration\_us,

774 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) delay\_before\_iterations\_us,

775 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status\_flags\_1\_set\_all\_wait,

776 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status\_flags\_1\_set\_any\_wait,

777 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status\_flags\_1\_clr\_all\_wait,

778 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status\_flags\_1\_clr\_any\_wait);

779

[ 788](tisci_8h.md#a9a80ade10fb08159e3fdfbd85ac8dfbf)int [tisci\_cmd\_proc\_shutdown\_no\_wait](tisci_8h.md#a9a80ade10fb08159e3fdfbd85ac8dfbf)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id);

789

790/\* Board Configuration Functions \*/

791

[ 805](tisci_8h.md#ac83cc7874ddc4c42c35e6a9f41e64ee7)int [cmd\_set\_board\_config\_using\_msg](tisci_8h.md#ac83cc7874ddc4c42c35e6a9f41e64ee7)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) msg\_type, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) addr,

806 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

807

808/\* Ring Configuration Function \*/

809

[ 826](tisci_8h.md#a9110e6b0fd37057ea72c64c8c2067a21)int [tisci\_cmd\_ring\_config](tisci_8h.md#a9110e6b0fd37057ea72c64c8c2067a21)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) valid\_params, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) nav\_id,

827 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) index, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_lo, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_hi, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count,

828 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order\_id);

829

830/\* System Control Functions \*/

831

[ 841](tisci_8h.md#aa7b6bef27ce24be4762d28499197a8bd)int [tisci\_cmd\_sys\_reset](tisci_8h.md#aa7b6bef27ce24be4762d28499197a8bd)(const struct [device](structdevice.md) \*dev);

842

843/\* Memory Management Functions \*/

844

[ 857](tisci_8h.md#a01625817d1a222c2979443413c7d712c)int [tisci\_cmd\_query\_msmc](tisci_8h.md#a01625817d1a222c2979443413c7d712c)(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*msmc\_start, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*msmc\_end);

858

859/\* Firewall Management Functions \*/

860

[ 872](tisci_8h.md#a2a1873dd1b47f7437cfd8adbea2decab)int [tisci\_cmd\_set\_fwl\_region](tisci_8h.md#a2a1873dd1b47f7437cfd8adbea2decab)(const struct [device](structdevice.md) \*dev, const struct [tisci\_msg\_fwl\_region](structtisci__msg__fwl__region.md) \*region);

873

874/\* INCLUDE\_ZEPHYR\_DRIVERS\_TISCI\_H\_ \*/

875

876/\* Firewall Management Functions \*/

877/\* ... previous firewall functions ... \*/

878

[ 892](tisci_8h.md#aafb0c859914130228e6c229725f87eca)int [tisci\_cmd\_get\_fwl\_region](tisci_8h.md#aafb0c859914130228e6c229725f87eca)(const struct [device](structdevice.md) \*dev, struct [tisci\_msg\_fwl\_region](structtisci__msg__fwl__region.md) \*region);

893

894/\* INCLUDE\_ZEPHYR\_DRIVERS\_TISCI\_H\_ \*/

895

896/\* Firewall Management Functions \*/

897/\* ... previous firewall functions ... \*/

898

912int [tisci\_cmd\_get\_fwl\_region](tisci_8h.md#aafb0c859914130228e6c229725f87eca)(const struct [device](structdevice.md) \*dev, struct [tisci\_msg\_fwl\_region](structtisci__msg__fwl__region.md) \*region);

913

914/\* Firewall Management Functions \*/

915/\* ... previous firewall functions ... \*/

916

930int [tisci\_cmd\_get\_fwl\_region](tisci_8h.md#aafb0c859914130228e6c229725f87eca)(const struct [device](structdevice.md) \*dev, struct [tisci\_msg\_fwl\_region](structtisci__msg__fwl__region.md) \*region);

931

932/\* Firewall Management Functions \*/

933/\* ... previous firewall functions ... \*/

934

[ 948](tisci_8h.md#afe30856eaa98b6f30b11ab99daf1dc91)int [tisci\_cmd\_change\_fwl\_owner](tisci_8h.md#afe30856eaa98b6f30b11ab99daf1dc91)(const struct [device](structdevice.md) \*dev, struct [tisci\_msg\_fwl\_owner](structtisci__msg__fwl__owner.md) \*owner);

949

950/\* UDMAP Management Functions \*/

951

[ 963](tisci_8h.md#a98a90edf1033e5146c51da785ee29581)int [tisci\_cmd\_rm\_udmap\_tx\_ch\_cfg](tisci_8h.md#a98a90edf1033e5146c51da785ee29581)(const struct [device](structdevice.md) \*dev,

964 const struct [tisci\_msg\_rm\_udmap\_tx\_ch\_cfg](structtisci__msg__rm__udmap__tx__ch__cfg.md) \*params);

965

[ 977](tisci_8h.md#a5217423ca42a90a472777a907864128e)int [tisci\_cmd\_rm\_udmap\_rx\_ch\_cfg](tisci_8h.md#a5217423ca42a90a472777a907864128e)(const struct [device](structdevice.md) \*dev,

978 const struct [tisci\_msg\_rm\_udmap\_rx\_ch\_cfg](structtisci__msg__rm__udmap__rx__ch__cfg.md) \*params);

979

980/\* PSI-L Management Functions \*/

981

[ 995](tisci_8h.md#a64b6aa840b820beed84fc9a21ffde350)int [tisci\_cmd\_rm\_psil\_pair](tisci_8h.md#a64b6aa840b820beed84fc9a21ffde350)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) nav\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) src\_thread,

996 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dst\_thread);

997

[ 1011](tisci_8h.md#a61d3ce5732bbd5a25d5d63af5a059666)int [tisci\_cmd\_rm\_psil\_unpair](tisci_8h.md#a61d3ce5732bbd5a25d5d63af5a059666)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) nav\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) src\_thread,

1012 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dst\_thread);

1013

[ 1024](tisci_8h.md#a0d5c1b5afc2842e38de56c64c62f17fd)int [tisci\_cmd\_rm\_irq\_set](tisci_8h.md#a0d5c1b5afc2842e38de56c64c62f17fd)(const struct [device](structdevice.md) \*dev, struct [tisci\_irq\_set\_req](structtisci__irq__set__req.md) \*req);

1025

[ 1036](tisci_8h.md#ac30ac2d3539999418f8b200e7b78d259)int [tisci\_cmd\_rm\_irq\_release](tisci_8h.md#ac30ac2d3539999418f8b200e7b78d259)(const struct [device](structdevice.md) \*dev, struct [tisci\_irq\_release\_req](structtisci__irq__release__req.md) \*req);

1037#endif

[device.h](device_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[tisci\_irq\_release\_req](structtisci__irq__release__req.md)

Request to release interrupt peripheral resources.

**Definition** tisci.h:224

[tisci\_irq\_release\_req::secondary\_host](structtisci__irq__release__req.md#a032e94a7d3c7384dc1f36c08b2d73e71)

uint8\_t secondary\_host

**Definition** tisci.h:234

[tisci\_irq\_release\_req::valid\_params](structtisci__irq__release__req.md#a068b9b4217d606f03898bdca2219bbf0)

uint32\_t valid\_params

**Definition** tisci.h:225

[tisci\_irq\_release\_req::global\_event](structtisci__irq__release__req.md#a12eb81324f28254daece1170b1e6764d)

uint16\_t global\_event

**Definition** tisci.h:232

[tisci\_irq\_release\_req::dst\_host\_irq](structtisci__irq__release__req.md#a3643554ea453300f33806b5128cc6c0a)

uint16\_t dst\_host\_irq

**Definition** tisci.h:229

[tisci\_irq\_release\_req::vint](structtisci__irq__release__req.md#a754e7c93d218a58e2bc18fd4ec086e40)

uint16\_t vint

**Definition** tisci.h:231

[tisci\_irq\_release\_req::ia\_id](structtisci__irq__release__req.md#aa6c09862a5e955a5ccbb78c7df2675fa)

uint16\_t ia\_id

**Definition** tisci.h:230

[tisci\_irq\_release\_req::src\_index](structtisci__irq__release__req.md#abb9cedc15e5923125e57f153ee1ed22a)

uint16\_t src\_index

**Definition** tisci.h:227

[tisci\_irq\_release\_req::src\_id](structtisci__irq__release__req.md#adddef8e01c4ecd9b44327418bcc8a3ef)

uint16\_t src\_id

**Definition** tisci.h:226

[tisci\_irq\_release\_req::dst\_id](structtisci__irq__release__req.md#ae646b23593b5f724fca6800c5c2e76bf)

uint16\_t dst\_id

**Definition** tisci.h:228

[tisci\_irq\_release\_req::vint\_status\_bit\_index](structtisci__irq__release__req.md#aedc07d5425720146b75b6757ca17c0d3)

uint8\_t vint\_status\_bit\_index

**Definition** tisci.h:233

[tisci\_irq\_set\_req](structtisci__irq__set__req.md)

Request to set up an interrupt route.

**Definition** tisci.h:187

[tisci\_irq\_set\_req::dst\_host\_irq](structtisci__irq__set__req.md#a1b01430d7e9140891589f0e48e79590a)

uint16\_t dst\_host\_irq

**Definition** tisci.h:192

[tisci\_irq\_set\_req::src\_index](structtisci__irq__set__req.md#a290247006f410254d3a4dbcdefc0ba75)

uint16\_t src\_index

**Definition** tisci.h:190

[tisci\_irq\_set\_req::dst\_id](structtisci__irq__set__req.md#a2a17ba4d83290d1ca8ae8bf39760a31a)

uint16\_t dst\_id

**Definition** tisci.h:191

[tisci\_irq\_set\_req::ia\_id](structtisci__irq__set__req.md#a2b8fd0bc0825d47fba8c961f68fcaef4)

uint16\_t ia\_id

**Definition** tisci.h:193

[tisci\_irq\_set\_req::vint](structtisci__irq__set__req.md#a2e3dd0054d9d0b029a6821f4df0af4ea)

uint16\_t vint

**Definition** tisci.h:194

[tisci\_irq\_set\_req::vint\_status\_bit\_index](structtisci__irq__set__req.md#a94ad73384be1f64054829a32ad70b066)

uint8\_t vint\_status\_bit\_index

**Definition** tisci.h:196

[tisci\_irq\_set\_req::global\_event](structtisci__irq__set__req.md#ab5f9849aef439771e81daf6a98303d17)

uint16\_t global\_event

**Definition** tisci.h:195

[tisci\_irq\_set\_req::valid\_params](structtisci__irq__set__req.md#ac5dddf4f1bc933e82eb7dfdfdfb35307)

uint32\_t valid\_params

**Definition** tisci.h:188

[tisci\_irq\_set\_req::secondary\_host](structtisci__irq__set__req.md#ad122a8cf2af3f3df9615c3ca70ed3b06)

uint8\_t secondary\_host

**Definition** tisci.h:197

[tisci\_irq\_set\_req::src\_id](structtisci__irq__set__req.md#af1c6cc734902f14d51ff46c971c1a576)

uint16\_t src\_id

**Definition** tisci.h:189

[tisci\_msg\_fwl\_owner](structtisci__msg__fwl__owner.md)

Request and Response for firewall owner change.

**Definition** tisci.h:82

[tisci\_msg\_fwl\_owner::owner\_index](structtisci__msg__fwl__owner.md#a2010d9ee65f9a94e5477a0fc1f21774e)

uint8\_t owner\_index

**Definition** tisci.h:85

[tisci\_msg\_fwl\_owner::owner\_permission\_bits](structtisci__msg__fwl__owner.md#a31ec3f0e90fdb8cea887d67004b066a7)

uint16\_t owner\_permission\_bits

**Definition** tisci.h:87

[tisci\_msg\_fwl\_owner::fwl\_id](structtisci__msg__fwl__owner.md#a370a1aff0233b53b035cbcd7b4c264b5)

uint16\_t fwl\_id

**Definition** tisci.h:83

[tisci\_msg\_fwl\_owner::owner\_privid](structtisci__msg__fwl__owner.md#a5e5e33a9a2f7c04022ce51fa1dcb8eef)

uint8\_t owner\_privid

**Definition** tisci.h:86

[tisci\_msg\_fwl\_owner::region](structtisci__msg__fwl__owner.md#a7ccaf9d3c1bd3639e8c170acd5d535a8)

uint16\_t region

**Definition** tisci.h:84

[tisci\_msg\_fwl\_region](structtisci__msg__fwl__region.md)

**Definition** tisci.h:54

[tisci\_msg\_fwl\_region::region](structtisci__msg__fwl__region.md#a2cb0672482a7859294a1c95b7f42d265)

uint16\_t region

**Definition** tisci.h:56

[tisci\_msg\_fwl\_region::start\_address](structtisci__msg__fwl__region.md#a4378cc7f160a86af3708284a7cb068a6)

uint64\_t start\_address

**Definition** tisci.h:60

[tisci\_msg\_fwl\_region::permissions](structtisci__msg__fwl__region.md#a4c091b340c1dc21f866d623489ab8451)

uint32\_t permissions[3]

**Definition** tisci.h:59

[tisci\_msg\_fwl\_region::control](structtisci__msg__fwl__region.md#a4e5c3b596b1e60524ac386c8506c3870)

uint32\_t control

**Definition** tisci.h:58

[tisci\_msg\_fwl\_region::end\_address](structtisci__msg__fwl__region.md#a789bcad9536d23d0cca4e8791f01c95c)

uint64\_t end\_address

**Definition** tisci.h:61

[tisci\_msg\_fwl\_region::n\_permission\_regs](structtisci__msg__fwl__region.md#aae2b9a8670d5e799347606d48408980f)

uint32\_t n\_permission\_regs

**Definition** tisci.h:57

[tisci\_msg\_fwl\_region::fwl\_id](structtisci__msg__fwl__region.md#ab3b3ae28613a3ef9e7c83b9d2af9f4ce)

uint16\_t fwl\_id

**Definition** tisci.h:55

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg](structtisci__msg__rm__udmap__rx__ch__cfg.md)

Configures a Navigator Subsystem UDMAP receive channel.

**Definition** tisci.h:132

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_priority](structtisci__msg__rm__udmap__rx__ch__cfg.md#a03ec736938d7b3eb05fcd56c62fd736a)

uint8\_t rx\_priority

**Definition** tisci.h:142

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::index](structtisci__msg__rm__udmap__rx__ch__cfg.md#a459ca9cb93410be5747595a57d88c7ed)

uint16\_t index

**Definition** tisci.h:139

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_sched\_priority](structtisci__msg__rm__udmap__rx__ch__cfg.md#a4e9720567203889d41fdccb769d56025)

uint8\_t rx\_sched\_priority

**Definition** tisci.h:145

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_qos](structtisci__msg__rm__udmap__rx__ch__cfg.md#a54f4136011d83df5441004dde0d5e696)

uint8\_t rx\_qos

**Definition** tisci.h:143

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rxcq\_qnum](structtisci__msg__rm__udmap__rx__ch__cfg.md#a554db2ab8742b2f15a6c7531638a6d74)

uint16\_t rxcq\_qnum

**Definition** tisci.h:141

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_burst\_size](structtisci__msg__rm__udmap__rx__ch__cfg.md#a57c0675af1fdefd1c270d11183fa77d6)

uint8\_t rx\_burst\_size

**Definition** tisci.h:153

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::nav\_id](structtisci__msg__rm__udmap__rx__ch__cfg.md#a691a478fa65af24279638789433dca6f)

uint16\_t nav\_id

**Definition** tisci.h:138

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_atype](structtisci__msg__rm__udmap__rx__ch__cfg.md#a7a36a9e37b22229c6ec90528aa7f9a9c)

uint8\_t rx\_atype

**Definition** tisci.h:149

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::valid\_params](structtisci__msg__rm__udmap__rx__ch__cfg.md#a88fa4f4bf94a290a035419a65054b544)

uint32\_t valid\_params

**Definition** tisci.h:133

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_ignore\_long](structtisci__msg__rm__udmap__rx__ch__cfg.md#a8e9b939089204b70469afedcb6c5ad8c)

uint8\_t rx\_ignore\_long

**Definition** tisci.h:152

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_orderid](structtisci__msg__rm__udmap__rx__ch__cfg.md#a9782a0a412413087ecf669beed77ff77)

uint8\_t rx\_orderid

**Definition** tisci.h:144

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_ignore\_short](structtisci__msg__rm__udmap__rx__ch__cfg.md#ab1245dc9783e74cd3cb1fcb648714e76)

uint8\_t rx\_ignore\_short

**Definition** tisci.h:151

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::flowid\_start](structtisci__msg__rm__udmap__rx__ch__cfg.md#abde08f01f02f26e1538cd82d9e87b19a)

uint16\_t flowid\_start

**Definition** tisci.h:146

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::flowid\_cnt](structtisci__msg__rm__udmap__rx__ch__cfg.md#ac10643f49f4d685af2bf14bb7b9b90f0)

uint16\_t flowid\_cnt

**Definition** tisci.h:147

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_pause\_on\_err](structtisci__msg__rm__udmap__rx__ch__cfg.md#ad008f77af3d4edbfeedb863ee2f8dcd0)

uint8\_t rx\_pause\_on\_err

**Definition** tisci.h:148

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_fetch\_size](structtisci__msg__rm__udmap__rx__ch__cfg.md#ad57a6d0dca932c95cff2a4675dc72990)

uint16\_t rx\_fetch\_size

**Definition** tisci.h:140

[tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_chan\_type](structtisci__msg__rm__udmap__rx__ch__cfg.md#aecf4e3eaaa8b8c604504eb525d3e1a5f)

uint8\_t rx\_chan\_type

**Definition** tisci.h:150

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg](structtisci__msg__rm__udmap__tx__ch__cfg.md)

Configures a Navigator Subsystem UDMAP transmit channel.

**Definition** tisci.h:96

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_sched\_priority](structtisci__msg__rm__udmap__tx__ch__cfg.md#a01334fae8a1e94ffbbba28d9c59ed0b1)

uint8\_t tx\_sched\_priority

**Definition** tisci.h:120

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_chan\_type](structtisci__msg__rm__udmap__tx__ch__cfg.md#a14b9ea920df0ff044bd9cf45c2084f3a)

uint8\_t tx\_chan\_type

**Definition** tisci.h:111

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::extended\_ch\_type](structtisci__msg__rm__udmap__tx__ch__cfg.md#a37b6f2565ccdf51fcc09801a72fde7e4)

uint8\_t extended\_ch\_type

**Definition** tisci.h:123

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::nav\_id](structtisci__msg__rm__udmap__tx__ch__cfg.md#a646845b965fee520329a118ade711f02)

uint16\_t nav\_id

**Definition** tisci.h:105

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_atype](structtisci__msg__rm__udmap__tx__ch__cfg.md#a75147fe8091db6c41050ded22c9eefa3)

uint8\_t tx\_atype

**Definition** tisci.h:110

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_burst\_size](structtisci__msg__rm__udmap__tx__ch__cfg.md#a7e0bfdb950b1b285ddc0e58282bc224b)

uint8\_t tx\_burst\_size

**Definition** tisci.h:121

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::txcq\_qnum](structtisci__msg__rm__udmap__tx__ch__cfg.md#a89f3ac8683240274b5bbc635e08b659f)

uint16\_t txcq\_qnum

**Definition** tisci.h:115

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_credit\_count](structtisci__msg__rm__udmap__tx__ch__cfg.md#a90a701c601691c79cd37192fac02d052)

uint8\_t tx\_credit\_count

**Definition** tisci.h:114

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_filt\_einfo](structtisci__msg__rm__udmap__tx__ch__cfg.md#a9d298e2ae456dcad3cbfdce595f0655c)

uint8\_t tx\_filt\_einfo

**Definition** tisci.h:108

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_supr\_tdpkt](structtisci__msg__rm__udmap__tx__ch__cfg.md#aaa18a6837a0271781164a353ce729623)

uint8\_t tx\_supr\_tdpkt

**Definition** tisci.h:112

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_tdtype](structtisci__msg__rm__udmap__tx__ch__cfg.md#ab36b40f8989fa7cdc5419bc0e9dd5a68)

uint8\_t tx\_tdtype

**Definition** tisci.h:122

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::index](structtisci__msg__rm__udmap__tx__ch__cfg.md#ab8327c9b3896c8294f47349572546e70)

uint16\_t index

**Definition** tisci.h:106

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_filt\_pswords](structtisci__msg__rm__udmap__tx__ch__cfg.md#ab9a869848d253d09f9fafc91dc8958cc)

uint8\_t tx\_filt\_pswords

**Definition** tisci.h:109

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::valid\_params](structtisci__msg__rm__udmap__tx__ch__cfg.md#acb243dd0b94ab38fa50ddd14a758b33a)

uint32\_t valid\_params

**Definition** tisci.h:97

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_pause\_on\_err](structtisci__msg__rm__udmap__tx__ch__cfg.md#ad255f2c020bfc237f5f22a747e68c1b8)

uint8\_t tx\_pause\_on\_err

**Definition** tisci.h:107

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::fdepth](structtisci__msg__rm__udmap__tx__ch__cfg.md#ad8aec84ccd12e9f02c4cafac7eadb4a4)

uint16\_t fdepth

**Definition** tisci.h:119

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_orderid](structtisci__msg__rm__udmap__tx__ch__cfg.md#ada34a3a63d1ed339a86804f906d4dbc5)

uint8\_t tx\_orderid

**Definition** tisci.h:118

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_priority](structtisci__msg__rm__udmap__tx__ch__cfg.md#aeaf51ae045dbc4079c02d61f13e487ed)

uint8\_t tx\_priority

**Definition** tisci.h:116

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_qos](structtisci__msg__rm__udmap__tx__ch__cfg.md#af377d65e1fb43ed7fceda8a0665605d0)

uint8\_t tx\_qos

**Definition** tisci.h:117

[tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_fetch\_size](structtisci__msg__rm__udmap__tx__ch__cfg.md#afd02dd108fd620f1bc9d66fac5a3e775)

uint16\_t tx\_fetch\_size

**Definition** tisci.h:113

[tisci\_version\_info](structtisci__version__info.md)

version information structure

**Definition** tisci.h:30

[tisci\_version\_info::firmware\_description](structtisci__version__info.md#a62cb5c8e86a94dbf53430d73c9f241a9)

char firmware\_description[32]

**Definition** tisci.h:34

[tisci\_version\_info::firmware\_revision](structtisci__version__info.md#a711c9ca4b063958fcb46ad0e298caa27)

uint16\_t firmware\_revision

**Definition** tisci.h:33

[tisci\_version\_info::abi\_major](structtisci__version__info.md#a7371d69f5f0993dfd1e582c165d2ddc5)

uint8\_t abi\_major

**Definition** tisci.h:31

[tisci\_version\_info::abi\_minor](structtisci__version__info.md#a8547f04843609b8a324ea4ecb91c17a7)

uint8\_t abi\_minor

**Definition** tisci.h:32

[tisci\_cmd\_dev\_get\_clcnt](tisci_8h.md#a01393f21cb5a88388ce51e36ba1843fc)

int tisci\_cmd\_dev\_get\_clcnt(const struct device \*dev, uint32\_t dev\_id, uint32\_t \*count)

Get the context loss counter for a device.

[tisci\_cmd\_query\_msmc](tisci_8h.md#a01625817d1a222c2979443413c7d712c)

int tisci\_cmd\_query\_msmc(const struct device \*dev, uint64\_t \*msmc\_start, uint64\_t \*msmc\_end)

Query the available MSMC memory range.

[tisci\_set\_device\_state\_no\_wait](tisci_8h.md#a05f871388f68d9c71620ea43bde1e3ab)

int tisci\_set\_device\_state\_no\_wait(const struct device \*dev, uint32\_t dev\_id, uint32\_t flags, uint8\_t state)

Set the state of a device without waiting for a response.

[tisci\_set\_clock\_state](tisci_8h.md#a086d96bed3d789bf303f56405a791aa6)

int tisci\_set\_clock\_state(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id, uint32\_t flags, uint8\_t state)

Set the state of a clock.

[tisci\_cmd\_rm\_irq\_set](tisci_8h.md#a0d5c1b5afc2842e38de56c64c62f17fd)

int tisci\_cmd\_rm\_irq\_set(const struct device \*dev, struct tisci\_irq\_set\_req \*req)

Set a Navigator Subsystem IRQ.

[tisci\_cmd\_dev\_is\_stop](tisci_8h.md#a1a441bdad9bfef9a0136f0b737c9c7aa)

int tisci\_cmd\_dev\_is\_stop(const struct device \*dev, uint32\_t dev\_id, bool \*r\_state, bool \*curr\_state)

Check if the device is requested to be stopped.

[tisci\_cmd\_proc\_handover](tisci_8h.md#a1acfab0f8fd3b1db050f97aa21d26ce3)

int tisci\_cmd\_proc\_handover(const struct device \*dev, uint8\_t proc\_id, uint8\_t host\_id)

Command to handover a physical processor control to a host in the processor's access control list.

[tisci\_cmd\_clk\_is\_off](tisci_8h.md#a20276a83e2037db6895085770353a194)

int tisci\_cmd\_clk\_is\_off(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id, bool \*req\_state, bool \*curr\_state)

Check if the clock is OFF.

[tisci\_cmd\_set\_fwl\_region](tisci_8h.md#a2a1873dd1b47f7437cfd8adbea2decab)

int tisci\_cmd\_set\_fwl\_region(const struct device \*dev, const struct tisci\_msg\_fwl\_region \*region)

Configure a firewall region.

[tisci\_cmd\_proc\_release](tisci_8h.md#a2e0e3e88c635a4e6399941696056b8a9)

int tisci\_cmd\_proc\_release(const struct device \*dev, uint8\_t proc\_id)

Command to release a physical processor control.

[tisci\_cmd\_proc\_request](tisci_8h.md#a3181b68860761b0060048a01d71888a8)

int tisci\_cmd\_proc\_request(const struct device \*dev, uint8\_t proc\_id)

Command to request a physical processor control.

[tisci\_cmd\_set\_proc\_boot\_cfg](tisci_8h.md#a3551276e98c3f03ea4beb9086c3b89c3)

int tisci\_cmd\_set\_proc\_boot\_cfg(const struct device \*dev, uint8\_t proc\_id, uint64\_t bootvector, uint32\_t config\_flags\_set, uint32\_t config\_flags\_clear)

Command to set the processor boot configuration flags.

[tisci\_cmd\_idle\_clock](tisci_8h.md#a3d39780a18358066ec8f187474c18f71)

int tisci\_cmd\_idle\_clock(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id)

Idle a clock that is under control of TI SCI.

[tisci\_cmd\_get\_clock\_state](tisci_8h.md#a3f8128fa6c8c6f10bb7e302e6e9cfeaf)

int tisci\_cmd\_get\_clock\_state(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id, uint8\_t \*programmed\_state, uint8\_t \*current\_state)

Get the state of a clock.

[tisci\_cmd\_get\_device](tisci_8h.md#a4011bbe29370fb581ab2dd0fcaa151db)

int tisci\_cmd\_get\_device(const struct device \*dev, uint32\_t dev\_id)

Request exclusive access to a device managed by TISCI.

[tisci\_cmd\_dev\_is\_trans](tisci_8h.md#a4a3b7acb3098f71b2a9f85fbb318d595)

int tisci\_cmd\_dev\_is\_trans(const struct device \*dev, uint32\_t dev\_id, bool \*curr\_state)

Check if the device is currently transitioning.

[tisci\_cmd\_dev\_is\_valid](tisci_8h.md#a4f4072f951c0ebbeb75e8cd2f06b6e8f)

int tisci\_cmd\_dev\_is\_valid(const struct device \*dev, uint32\_t dev\_id)

Check if a device ID is valid.

[tisci\_cmd\_rm\_udmap\_rx\_ch\_cfg](tisci_8h.md#a5217423ca42a90a472777a907864128e)

int tisci\_cmd\_rm\_udmap\_rx\_ch\_cfg(const struct device \*dev, const struct tisci\_msg\_rm\_udmap\_rx\_ch\_cfg \*params)

Configure a UDMAP receive channel.

[tisci\_cmd\_put\_device](tisci_8h.md#a5a7c9ff34ad1ffa87c62fef6b2ac8719)

int tisci\_cmd\_put\_device(const struct device \*dev, uint32\_t dev\_id)

Command to release a device managed by TISCI.

[tisci\_cmd\_clk\_get\_freq](tisci_8h.md#a5c69f5f12b79a0b37a1f704624106960)

int tisci\_cmd\_clk\_get\_freq(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id, uint64\_t \*freq)

Get the current frequency of a clock.

[tisci\_cmd\_rm\_psil\_unpair](tisci_8h.md#a61d3ce5732bbd5a25d5d63af5a059666)

int tisci\_cmd\_rm\_psil\_unpair(const struct device \*dev, uint32\_t nav\_id, uint32\_t src\_thread, uint32\_t dst\_thread)

Unpair PSI-L source thread from destination thread.

[tisci\_cmd\_rm\_psil\_pair](tisci_8h.md#a64b6aa840b820beed84fc9a21ffde350)

int tisci\_cmd\_rm\_psil\_pair(const struct device \*dev, uint32\_t nav\_id, uint32\_t src\_thread, uint32\_t dst\_thread)

Pair PSI-L source thread to destination thread.

[tisci\_cmd\_clk\_set\_parent](tisci_8h.md#a6ad9804cf3e23246955bcab1e98aecdb)

int tisci\_cmd\_clk\_set\_parent(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id, uint8\_t parent\_id)

Set the parent clock for a clock.

[tisci\_cmd\_clk\_is\_on](tisci_8h.md#a7f0bafa6005d46d2786db590a27add25)

int tisci\_cmd\_clk\_is\_on(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id, bool \*req\_state, bool \*curr\_state)

Check if the clock is ON.

[tisci\_cmd\_clk\_get\_parent](tisci_8h.md#a86e0ed2c8711363dc5ea710b12a303af)

int tisci\_cmd\_clk\_get\_parent(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id, uint8\_t \*parent\_id)

Get the parent clock for a clock.

[tisci\_proc\_wait\_boot\_status\_no\_wait](tisci_8h.md#a8a29455ba732efa082c1a72922f46f9e)

int tisci\_proc\_wait\_boot\_status\_no\_wait(const struct device \*dev, uint8\_t proc\_id, uint8\_t num\_wait\_iterations, uint8\_t num\_match\_iterations, uint8\_t delay\_per\_iteration\_us, uint8\_t delay\_before\_iterations\_us, uint32\_t status\_flags\_1\_set\_all\_wait, uint32\_t status\_flags\_1\_set\_any\_wait, uint32\_t status\_flags\_1\_clr\_all\_wait, uint32\_t status\_flags\_1\_clr\_any\_wait)

Helper function to wait for a processor boot status without requesting or waiting for a response.

[tisci\_set\_device\_state](tisci_8h.md#a8b6d6f99df32eeba9131ce130ee4f12d)

int tisci\_set\_device\_state(const struct device \*dev, uint32\_t dev\_id, uint32\_t flags, uint8\_t state)

Set the state of a device.

[tisci\_get\_resource\_range](tisci_8h.md#a8ced32499c14aae81994368d4450422d)

int tisci\_get\_resource\_range(const struct device \*dev, uint32\_t dev\_id, uint8\_t subtype, uint8\_t s\_host, uint16\_t \*range\_start, uint16\_t \*range\_num)

Get a range of resources assigned to a host.

[tisci\_cmd\_get\_device\_resets](tisci_8h.md#a90613df222309651abc1adb2f4d82272)

int tisci\_cmd\_get\_device\_resets(const struct device \*dev, uint32\_t dev\_id, uint32\_t \*reset\_state)

Get reset state for a device managed by TISCI.

[tisci\_cmd\_ring\_config](tisci_8h.md#a9110e6b0fd37057ea72c64c8c2067a21)

int tisci\_cmd\_ring\_config(const struct device \*dev, uint32\_t valid\_params, uint16\_t nav\_id, uint16\_t index, uint32\_t addr\_lo, uint32\_t addr\_hi, uint32\_t count, uint8\_t mode, uint8\_t size, uint8\_t order\_id)

Configure a RA ring.

[tisci\_cmd\_set\_device\_resets](tisci_8h.md#a94f43ead8c81320f651fa9c0450a2493)

int tisci\_cmd\_set\_device\_resets(const struct device \*dev, uint32\_t dev\_id, uint32\_t reset\_state)

Set resets for a device managed by TISCI.

[tisci\_cmd\_clk\_get\_match\_freq](tisci_8h.md#a9801b388e5dc60f10aa624040cb8bfe2)

int tisci\_cmd\_clk\_get\_match\_freq(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id, uint64\_t min\_freq, uint64\_t target\_freq, uint64\_t max\_freq, uint64\_t \*match\_freq)

Get a matching frequency for a clock.

[tisci\_cmd\_rm\_udmap\_tx\_ch\_cfg](tisci_8h.md#a98a90edf1033e5146c51da785ee29581)

int tisci\_cmd\_rm\_udmap\_tx\_ch\_cfg(const struct device \*dev, const struct tisci\_msg\_rm\_udmap\_tx\_ch\_cfg \*params)

Configure a UDMAP transmit channel.

[tisci\_cmd\_proc\_shutdown\_no\_wait](tisci_8h.md#a9a80ade10fb08159e3fdfbd85ac8dfbf)

int tisci\_cmd\_proc\_shutdown\_no\_wait(const struct device \*dev, uint8\_t proc\_id)

Command to shutdown a core without requesting or waiting for a response.

[tisci\_cmd\_get\_proc\_boot\_status](tisci_8h.md#a9e057dd13353ccdd7df3b2263ef22940)

int tisci\_cmd\_get\_proc\_boot\_status(const struct device \*dev, uint8\_t proc\_id, uint64\_t \*bv, uint32\_t \*cfg\_flags, uint32\_t \*ctrl\_flags, uint32\_t \*sts\_flags)

Command to get the processor boot status.

[tisci\_cmd\_get\_resource\_range\_from\_shost](tisci_8h.md#aa261b08c9141360c5f4f9e50ab151ed5)

int tisci\_cmd\_get\_resource\_range\_from\_shost(const struct device \*dev, uint32\_t dev\_id, uint8\_t subtype, uint8\_t s\_host, uint16\_t \*range\_start, uint16\_t \*range\_num)

Get a range of resources assigned to a specified host.

[tisci\_cmd\_sys\_reset](tisci_8h.md#aa7b6bef27ce24be4762d28499197a8bd)

int tisci\_cmd\_sys\_reset(const struct device \*dev)

Request a system reset.

[tisci\_cmd\_dev\_is\_on](tisci_8h.md#aa7bb463be840666d87a68c1e65496b19)

int tisci\_cmd\_dev\_is\_on(const struct device \*dev, uint32\_t dev\_id, bool \*r\_state, bool \*curr\_state)

Check if the device is requested to be ON.

[tisci\_cmd\_proc\_auth\_boot\_image](tisci_8h.md#aaa3b1c5f5072b40e2eb1c626cb6f6f29)

int tisci\_cmd\_proc\_auth\_boot\_image(const struct device \*dev, uint64\_t \*image\_addr, uint32\_t \*image\_size)

Command to authenticate and load the image, then set the processor configuration flags.

[tisci\_cmd\_idle\_device\_exclusive](tisci_8h.md#aab1720913f75a771e041e2195b9deede)

int tisci\_cmd\_idle\_device\_exclusive(const struct device \*dev, uint32\_t dev\_id)

[tisci\_cmd\_clk\_is\_auto](tisci_8h.md#aaebb0012c291ded1b9303d634b1bb245)

int tisci\_cmd\_clk\_is\_auto(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id, bool \*req\_state)

Check if the clock is being auto-managed.

[tisci\_cmd\_get\_fwl\_region](tisci_8h.md#aafb0c859914130228e6c229725f87eca)

int tisci\_cmd\_get\_fwl\_region(const struct device \*dev, struct tisci\_msg\_fwl\_region \*region)

Get firewall region configuration.

[tisci\_cmd\_get\_clock](tisci_8h.md#ab63106de04e579ba18f34763b3efa8b3)

int tisci\_cmd\_get\_clock(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id, bool needs\_ssc, bool can\_change\_freq, bool enable\_input\_term)

Get control of a clock from TI SCI.

[tisci\_cmd\_idle\_device](tisci_8h.md#ab8203c5d0b699ec726a889e7027ae034)

int tisci\_cmd\_idle\_device(const struct device \*dev, uint32\_t dev\_id)

Command to idle a device managed by TISCI.

[tisci\_cmd\_rm\_irq\_release](tisci_8h.md#ac30ac2d3539999418f8b200e7b78d259)

int tisci\_cmd\_rm\_irq\_release(const struct device \*dev, struct tisci\_irq\_release\_req \*req)

Release a Navigator Subsystem IRQ.

[cmd\_set\_board\_config\_using\_msg](tisci_8h.md#ac83cc7874ddc4c42c35e6a9f41e64ee7)

int cmd\_set\_board\_config\_using\_msg(const struct device \*dev, uint16\_t msg\_type, uint64\_t addr, uint32\_t size)

Set board configuration using a specified message type.

[tisci\_cmd\_clk\_set\_freq](tisci_8h.md#ad3563b7ec2fa13eb4b1faa564062ae12)

int tisci\_cmd\_clk\_set\_freq(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id, uint64\_t min\_freq, uint64\_t target\_freq, uint64\_t max\_freq)

Set a frequency for a clock.

[tisci\_get\_device\_state](tisci_8h.md#ada78c57b3cb24e57a3f6cc155e3a3d09)

int tisci\_get\_device\_state(const struct device \*dev, uint32\_t dev\_id, uint32\_t \*clcnt, uint32\_t \*resets, uint8\_t \*p\_state, uint8\_t \*c\_state)

Get the state of a device.

[tisci\_cmd\_get\_device\_exclusive](tisci_8h.md#adc16227f1ec150d0c6cf32442fa3e915)

int tisci\_cmd\_get\_device\_exclusive(const struct device \*dev, uint32\_t dev\_id)

[tisci\_cmd\_get\_resource\_range](tisci_8h.md#ae249d114c60b6b1a76f7de8dab5c3ce1)

int tisci\_cmd\_get\_resource\_range(const struct device \*dev, uint32\_t dev\_id, uint8\_t subtype, uint16\_t \*range\_start, uint16\_t \*range\_num)

Get a range of resources assigned to the host.

[tisci\_cmd\_put\_clock](tisci_8h.md#ae48c6c78db3f4bee6520c0af66e37e7d)

int tisci\_cmd\_put\_clock(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id)

Release a clock from control back to TI SCI.

[tisci\_cmd\_clk\_get\_num\_parents](tisci_8h.md#ae93fb7c70a4f2299415a51b993d36741)

int tisci\_cmd\_clk\_get\_num\_parents(const struct device \*dev, uint32\_t dev\_id, uint8\_t clk\_id, uint8\_t \*num\_parents)

Get the number of parent clocks for a clock.

[tisci\_cmd\_get\_revision](tisci_8h.md#aea0b9addbd3cfcb2be691f0801128fe1)

int tisci\_cmd\_get\_revision(const struct device \*dev, struct tisci\_version\_info \*ver)

Get the revision information of the TI SCI firmware.

[tisci\_cmd\_set\_proc\_boot\_ctrl](tisci_8h.md#aee60c2eb75e6786b91d9dc73c7a7e2c6)

int tisci\_cmd\_set\_proc\_boot\_ctrl(const struct device \*dev, uint8\_t proc\_id, uint32\_t control\_flags\_set, uint32\_t control\_flags\_clear)

Command to set the processor boot control flags.

[tisci\_cmd\_dev\_is\_idle](tisci_8h.md#af9ff6eee5bca675c50c28fbc4af3048c)

int tisci\_cmd\_dev\_is\_idle(const struct device \*dev, uint32\_t dev\_id, bool \*r\_state)

Check if the device is requested to be idle.

[tisci\_cmd\_change\_fwl\_owner](tisci_8h.md#afe30856eaa98b6f30b11ab99daf1dc91)

int tisci\_cmd\_change\_fwl\_owner(const struct device \*dev, struct tisci\_msg\_fwl\_owner \*owner)

Change firewall region owner.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [tisci](dir_32233e7c9e492e9cba0b091ed92f7703.md)
- [tisci.h](tisci_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
