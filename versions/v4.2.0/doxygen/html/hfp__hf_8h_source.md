---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/hfp__hf_8h_source.html
original_path: doxygen/html/hfp__hf_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hfp\_hf.h

[Go to the documentation of this file.](hfp__hf_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_HFP\_HF\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_HFP\_HF\_H\_

12

19

20#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

26/\* HFP CODEC IDs \*/

[ 27](group__bt__hfp.md#ga0e46a981a70dcdecbae119ebb6d61aa0)#define BT\_HFP\_HF\_CODEC\_CVSD 0x01

[ 28](group__bt__hfp.md#gaea9fb177ae8ba32650dc93f1b2953333)#define BT\_HFP\_HF\_CODEC\_MSBC 0x02

[ 29](group__bt__hfp.md#gac8ab2e9ff6c8b9a06ac460f751dec1ad)#define BT\_HFP\_HF\_CODEC\_LC3\_SWB 0x03

30

31struct bt\_hfp\_hf;

32

33struct bt\_hfp\_hf\_call;

34

[ 36](structbt__hfp__hf__cb.md)struct [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) {

[ 45](structbt__hfp__hf__cb.md#a68c09fe6aac4ff7f3b24e6a550e75d1e) void (\*[connected](structbt__hfp__hf__cb.md#a68c09fe6aac4ff7f3b24e6a550e75d1e))(struct bt\_conn \*conn, struct bt\_hfp\_hf \*hf);

[ 56](structbt__hfp__hf__cb.md#afdf28b8d8f9598ee2f6fa826aba4fbba) void (\*[disconnected](structbt__hfp__hf__cb.md#afdf28b8d8f9598ee2f6fa826aba4fbba))(struct bt\_hfp\_hf \*hf);

[ 65](structbt__hfp__hf__cb.md#a6ea6f5a866d7e4da5e3fe894d700f6b6) void (\*[sco\_connected](structbt__hfp__hf__cb.md#a6ea6f5a866d7e4da5e3fe894d700f6b6))(struct bt\_hfp\_hf \*hf, struct bt\_conn \*sco\_conn);

[ 74](structbt__hfp__hf__cb.md#a4586240506c876c9f58cf60a091b4044) void (\*[sco\_disconnected](structbt__hfp__hf__cb.md#a4586240506c876c9f58cf60a091b4044))(struct bt\_conn \*sco\_conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

[ 82](structbt__hfp__hf__cb.md#a8483c3a3ba8b0e5131bec6fce5dbc36d) void (\*[service](structbt__hfp__hf__cb.md#a8483c3a3ba8b0e5131bec6fce5dbc36d))(struct bt\_hfp\_hf \*hf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

[ 91](structbt__hfp__hf__cb.md#a46677dbfe7e73dcdc3b6cacb0aa9fa58) void (\*[outgoing](structbt__hfp__hf__cb.md#a46677dbfe7e73dcdc3b6cacb0aa9fa58))(struct bt\_hfp\_hf \*hf, struct bt\_hfp\_hf\_call \*call);

[ 99](structbt__hfp__hf__cb.md#ace8989f64fea9301d6f48e5252ceb2de) void (\*[remote\_ringing](structbt__hfp__hf__cb.md#ace8989f64fea9301d6f48e5252ceb2de))(struct bt\_hfp\_hf\_call \*call);

[ 108](structbt__hfp__hf__cb.md#a597d2e9b20ffc2dfedd53aea2969727e) void (\*[incoming](structbt__hfp__hf__cb.md#a597d2e9b20ffc2dfedd53aea2969727e))(struct bt\_hfp\_hf \*hf, struct bt\_hfp\_hf\_call \*call);

[ 116](structbt__hfp__hf__cb.md#a71f0f50a83defe014b3b364dcc16ad9d) void (\*[incoming\_held](structbt__hfp__hf__cb.md#a71f0f50a83defe014b3b364dcc16ad9d))(struct bt\_hfp\_hf\_call \*call);

[ 124](structbt__hfp__hf__cb.md#a44ae68eb055f23c30dd761fd6eb1c6cd) void (\*[accept](structbt__hfp__hf__cb.md#a44ae68eb055f23c30dd761fd6eb1c6cd))(struct bt\_hfp\_hf\_call \*call);

[ 132](structbt__hfp__hf__cb.md#a9f248f9c7e3830c6941225bd4d2363d3) void (\*[reject](structbt__hfp__hf__cb.md#a9f248f9c7e3830c6941225bd4d2363d3))(struct bt\_hfp\_hf\_call \*call);

[ 140](structbt__hfp__hf__cb.md#a691ec076d6fba14636b873cf75262e81) void (\*[terminate](structbt__hfp__hf__cb.md#a691ec076d6fba14636b873cf75262e81))(struct bt\_hfp\_hf\_call \*call);

[ 147](structbt__hfp__hf__cb.md#af6fe24140f5a5a1aea2eff7b1e534cfd) void (\*[held](structbt__hfp__hf__cb.md#af6fe24140f5a5a1aea2eff7b1e534cfd))(struct bt\_hfp\_hf\_call \*call);

[ 154](structbt__hfp__hf__cb.md#a4977076381a5c4daf620aa6c6ab558d3) void (\*[retrieve](structbt__hfp__hf__cb.md#a4977076381a5c4daf620aa6c6ab558d3))(struct bt\_hfp\_hf\_call \*call);

[ 162](structbt__hfp__hf__cb.md#add68ca4e00f7a5dbc28282ee29bea087) void (\*[signal](structbt__hfp__hf__cb.md#add68ca4e00f7a5dbc28282ee29bea087))(struct bt\_hfp\_hf \*hf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

[ 170](structbt__hfp__hf__cb.md#a13b35eb32e4f579d853657a2ea89af42) void (\*[roam](structbt__hfp__hf__cb.md#a13b35eb32e4f579d853657a2ea89af42))(struct bt\_hfp\_hf \*hf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

[ 178](structbt__hfp__hf__cb.md#a17faaab9a9af5dc53018fc2f94855bea) void (\*[battery](structbt__hfp__hf__cb.md#a17faaab9a9af5dc53018fc2f94855bea))(struct bt\_hfp\_hf \*hf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

[ 186](structbt__hfp__hf__cb.md#a2712d3a5d68bdf2de6dc27f938590c0a) void (\*[ring\_indication](structbt__hfp__hf__cb.md#a2712d3a5d68bdf2de6dc27f938590c0a))(struct bt\_hfp\_hf\_call \*call);

[ 194](structbt__hfp__hf__cb.md#a80e98b5dd212158c255215b8a304d67c) void (\*[dialing](structbt__hfp__hf__cb.md#a80e98b5dd212158c255215b8a304d67c))(struct bt\_hfp\_hf \*hf, int err);

[ 207](structbt__hfp__hf__cb.md#abcbdaa8312f6efe3711da0aabba52bce) void (\*[clip](structbt__hfp__hf__cb.md#abcbdaa8312f6efe3711da0aabba52bce))(struct bt\_hfp\_hf\_call \*call, char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type);

[ 219](structbt__hfp__hf__cb.md#a512de9839559def9c2110a310f21ca03) void (\*[vgm](structbt__hfp__hf__cb.md#a512de9839559def9c2110a310f21ca03))(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain);

[ 231](structbt__hfp__hf__cb.md#a385cbe2c3a9c402a09b873a3ce753d8b) void (\*[vgs](structbt__hfp__hf__cb.md#a385cbe2c3a9c402a09b873a3ce753d8b))(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain);

[ 242](structbt__hfp__hf__cb.md#acc1ff77f98329986c2120b0c9c4f565a) void (\*[inband\_ring](structbt__hfp__hf__cb.md#acc1ff77f98329986c2120b0c9c4f565a))(struct bt\_hfp\_hf \*hf, bool inband);

[ 258](structbt__hfp__hf__cb.md#a187ef5f2b7e4a4d8a4963e51453aefdb) void (\*operator)(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) format, char \*operator);

281 void (\*codec\_negotiate)(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id);

[ 292](structbt__hfp__hf__cb.md#a0f2da8d9169658c03d2dabe2c8b1cf6f) void (\*[ecnr\_turn\_off](structbt__hfp__hf__cb.md#a0f2da8d9169658c03d2dabe2c8b1cf6f))(struct bt\_hfp\_hf \*hf, int err);

[ 307](structbt__hfp__hf__cb.md#a283a791f330a49f402cde0233ad05f6e) void (\*[call\_waiting](structbt__hfp__hf__cb.md#a283a791f330a49f402cde0233ad05f6e))(struct bt\_hfp\_hf\_call \*call, char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type);

[ 321](structbt__hfp__hf__cb.md#a07da1a6c86031c42749972d5d9fb7677) void (\*[voice\_recognition](structbt__hfp__hf__cb.md#a07da1a6c86031c42749972d5d9fb7677))(struct bt\_hfp\_hf \*hf, bool activate);

[ 338](structbt__hfp__hf__cb.md#a298a6d3315535331ffb779899db9f973) void (\*[vre\_state](structbt__hfp__hf__cb.md#a298a6d3315535331ffb779899db9f973))(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

[ 374](structbt__hfp__hf__cb.md#a1e7a4046b01ce4753352f86c209e171f) void (\*[textual\_representation](structbt__hfp__hf__cb.md#a1e7a4046b01ce4753352f86c209e171f))(struct bt\_hfp\_hf \*hf, char \*id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type,

375 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) operation, char \*text);

[ 385](structbt__hfp__hf__cb.md#ac1e9fb5d0446d498b6cf3705a05633e2) void (\*[request\_phone\_number](structbt__hfp__hf__cb.md#ac1e9fb5d0446d498b6cf3705a05633e2))(struct bt\_hfp\_hf \*hf, const char \*number);

386

[ 417](structbt__hfp__hf__cb.md#ae5682d96bdf18b148fac7ce1d9cbdb75) void (\*[subscriber\_number](structbt__hfp__hf__cb.md#ae5682d96bdf18b148fac7ce1d9cbdb75))(struct bt\_hfp\_hf \*hf, const char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type,

418 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [service](structbt__hfp__hf__cb.md#a8483c3a3ba8b0e5131bec6fce5dbc36d));

419};

420

[ 430](group__bt__hfp.md#ga2e4a7c05a3ba9a32eab50b9904f7f161)int [bt\_hfp\_hf\_register](group__bt__hfp.md#ga2e4a7c05a3ba9a32eab50b9904f7f161)(struct [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) \*cb);

431

[ 456](group__bt__hfp.md#ga302e9ed397b056edef518470c6ea1d62)int [bt\_hfp\_hf\_connect](group__bt__hfp.md#ga302e9ed397b056edef518470c6ea1d62)(struct bt\_conn \*conn, struct bt\_hfp\_hf \*\*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel);

457

[ 479](group__bt__hfp.md#gaf5e7ef119731c0dc35bec61fb7c34774)int [bt\_hfp\_hf\_disconnect](group__bt__hfp.md#gaf5e7ef119731c0dc35bec61fb7c34774)(struct bt\_hfp\_hf \*hf);

480

[ 494](group__bt__hfp.md#ga64ac1971dc7b1dacf6685bdc0c71e34c)int [bt\_hfp\_hf\_cli](group__bt__hfp.md#ga64ac1971dc7b1dacf6685bdc0c71e34c)(struct bt\_hfp\_hf \*hf, bool enable);

495

[ 517](group__bt__hfp.md#ga0602cee7a90ca4afe90b65d748024472)int [bt\_hfp\_hf\_vgm](group__bt__hfp.md#ga0602cee7a90ca4afe90b65d748024472)(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain);

518

[ 540](group__bt__hfp.md#ga0c1c35b3117f78f43a6300d4ff7dd18b)int [bt\_hfp\_hf\_vgs](group__bt__hfp.md#ga0c1c35b3117f78f43a6300d4ff7dd18b)(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain);

541

[ 551](group__bt__hfp.md#gaaa9fbdceec140f274fc88c063a4cd4b8)int [bt\_hfp\_hf\_get\_operator](group__bt__hfp.md#gaaa9fbdceec140f274fc88c063a4cd4b8)(struct bt\_hfp\_hf \*hf);

552

[ 565](group__bt__hfp.md#ga5bad80355fd7903abcee84437d399829)int [bt\_hfp\_hf\_accept](group__bt__hfp.md#ga5bad80355fd7903abcee84437d399829)(struct bt\_hfp\_hf\_call \*call);

566

[ 579](group__bt__hfp.md#gac4e3d88b80b69840d52050dcd72c9ab3)int [bt\_hfp\_hf\_reject](group__bt__hfp.md#gac4e3d88b80b69840d52050dcd72c9ab3)(struct bt\_hfp\_hf\_call \*call);

580

[ 591](group__bt__hfp.md#gabbce5fbf0dec27e1c5a4da144fbfc9c1)int [bt\_hfp\_hf\_terminate](group__bt__hfp.md#gabbce5fbf0dec27e1c5a4da144fbfc9c1)(struct bt\_hfp\_hf\_call \*call);

592

[ 605](group__bt__hfp.md#ga540bf6ec23c632b3f736e6302ef32ebd)int [bt\_hfp\_hf\_hold\_incoming](group__bt__hfp.md#ga540bf6ec23c632b3f736e6302ef32ebd)(struct bt\_hfp\_hf\_call \*call);

606

[ 617](group__bt__hfp.md#ga70e086f6a02cb116317a8e80f76abf6d)int [bt\_hfp\_hf\_query\_respond\_hold\_status](group__bt__hfp.md#ga70e086f6a02cb116317a8e80f76abf6d)(struct bt\_hfp\_hf \*hf);

618

[ 632](group__bt__hfp.md#gac57d7188e3f8b6e1e28d2a55c2567dbf)int [bt\_hfp\_hf\_number\_call](group__bt__hfp.md#gac57d7188e3f8b6e1e28d2a55c2567dbf)(struct bt\_hfp\_hf \*hf, const char \*number);

633

[ 647](group__bt__hfp.md#gabacb666eb0f43db8614413a4ae0ce60a)int [bt\_hfp\_hf\_memory\_dial](group__bt__hfp.md#gabacb666eb0f43db8614413a4ae0ce60a)(struct bt\_hfp\_hf \*hf, const char \*location);

648

[ 661](group__bt__hfp.md#ga9611012a35df66fac324b99b16e5d958)int [bt\_hfp\_hf\_redial](group__bt__hfp.md#ga9611012a35df66fac324b99b16e5d958)(struct bt\_hfp\_hf \*hf);

662

[ 673](group__bt__hfp.md#gad29bf40953faf638cc08acf919eb8f4f)int [bt\_hfp\_hf\_audio\_connect](group__bt__hfp.md#gad29bf40953faf638cc08acf919eb8f4f)(struct bt\_hfp\_hf \*hf);

674

[ 691](group__bt__hfp.md#ga34649dbecca2513c0b5bcd0e109b2551)int [bt\_hfp\_hf\_select\_codec](group__bt__hfp.md#ga34649dbecca2513c0b5bcd0e109b2551)(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) codec\_id);

692

[ 705](group__bt__hfp.md#ga91fc2204f50df07567f87a2b7a18e69f)int [bt\_hfp\_hf\_set\_codecs](group__bt__hfp.md#ga91fc2204f50df07567f87a2b7a18e69f)(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) codec\_ids);

706

[ 719](group__bt__hfp.md#ga7f37a9c009b4e55b7060d635c5b0c67b)int [bt\_hfp\_hf\_turn\_off\_ecnr](group__bt__hfp.md#ga7f37a9c009b4e55b7060d635c5b0c67b)(struct bt\_hfp\_hf \*hf);

720

[ 733](group__bt__hfp.md#ga3afb0d82551708975dbeb9c903c3d1fb)int [bt\_hfp\_hf\_call\_waiting\_notify](group__bt__hfp.md#ga3afb0d82551708975dbeb9c903c3d1fb)(struct bt\_hfp\_hf \*hf, bool enable);

734

[ 745](group__bt__hfp.md#ga06e7e93578601693fa377a240e0d18a7)int [bt\_hfp\_hf\_release\_all\_held](group__bt__hfp.md#ga06e7e93578601693fa377a240e0d18a7)(struct bt\_hfp\_hf \*hf);

746

[ 758](group__bt__hfp.md#ga7389e5723e01b661b5e9c9d2114918b8)int [bt\_hfp\_hf\_set\_udub](group__bt__hfp.md#ga7389e5723e01b661b5e9c9d2114918b8)(struct bt\_hfp\_hf \*hf);

759

[ 771](group__bt__hfp.md#ga36be4ff5fd805c4413ba90b1f62b9143)int [bt\_hfp\_hf\_release\_active\_accept\_other](group__bt__hfp.md#ga36be4ff5fd805c4413ba90b1f62b9143)(struct bt\_hfp\_hf \*hf);

772

[ 784](group__bt__hfp.md#ga40de46a6651eb85aa6d04ad66f528803)int [bt\_hfp\_hf\_hold\_active\_accept\_other](group__bt__hfp.md#ga40de46a6651eb85aa6d04ad66f528803)(struct bt\_hfp\_hf \*hf);

785

[ 796](group__bt__hfp.md#ga04d9fe3524c9522e98830507886bdfc6)int [bt\_hfp\_hf\_join\_conversation](group__bt__hfp.md#ga04d9fe3524c9522e98830507886bdfc6)(struct bt\_hfp\_hf \*hf);

797

[ 809](group__bt__hfp.md#ga2b48a0938e65899417b2f3ab1fa4c548)int [bt\_hfp\_hf\_explicit\_call\_transfer](group__bt__hfp.md#ga2b48a0938e65899417b2f3ab1fa4c548)(struct bt\_hfp\_hf \*hf);

810

[ 822](group__bt__hfp.md#ga1ad888c3b967d3f9b2e5ccee303b9ad7)int [bt\_hfp\_hf\_release\_specified\_call](group__bt__hfp.md#ga1ad888c3b967d3f9b2e5ccee303b9ad7)(struct bt\_hfp\_hf\_call \*call);

823

[ 837](group__bt__hfp.md#gac3c038818cda3645eaadc5374d18c3ee)int [bt\_hfp\_hf\_private\_consultation\_mode](group__bt__hfp.md#gac3c038818cda3645eaadc5374d18c3ee)(struct bt\_hfp\_hf\_call \*call);

838

[ 850](group__bt__hfp.md#gaeed952ce163ef2466ece04af24b76a28)int [bt\_hfp\_hf\_voice\_recognition](group__bt__hfp.md#gaeed952ce163ef2466ece04af24b76a28)(struct bt\_hfp\_hf \*hf, bool activate);

851

[ 864](group__bt__hfp.md#ga3f6b43bf53fa04a6e71e883dc38f988b)int [bt\_hfp\_hf\_ready\_to\_accept\_audio](group__bt__hfp.md#ga3f6b43bf53fa04a6e71e883dc38f988b)(struct bt\_hfp\_hf \*hf);

865

[ 874](group__bt__hfp.md#ga92d89b0b37186688e86091a7a8015245)int [bt\_hfp\_hf\_request\_phone\_number](group__bt__hfp.md#ga92d89b0b37186688e86091a7a8015245)(struct bt\_hfp\_hf \*hf);

875

[ 888](group__bt__hfp.md#ga6a3a6bc61a3a74f5a4a48d7e39bd74a0)int [bt\_hfp\_hf\_transmit\_dtmf\_code](group__bt__hfp.md#ga6a3a6bc61a3a74f5a4a48d7e39bd74a0)(struct bt\_hfp\_hf\_call \*call, char code);

889

[ 898](group__bt__hfp.md#gad5dab4dcb66d52a80e0689a86de5fec3)int [bt\_hfp\_hf\_query\_subscriber](group__bt__hfp.md#gad5dab4dcb66d52a80e0689a86de5fec3)(struct bt\_hfp\_hf \*hf);

899

900/\* HFP HF Indicators \*/

[ 901](group__bt__hfp.md#ga862b201be555821e932f6df5599eaa57)enum [hfp\_hf\_ag\_indicators](group__bt__hfp.md#ga862b201be555821e932f6df5599eaa57) {

[ 902](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57adb3fae0b3684e8d035e195a91d24deb8) [HF\_SERVICE\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57adb3fae0b3684e8d035e195a91d24deb8) = 0, /\* AG service indicator \*/

[ 903](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57ad8620b141e11f48b46b9cd5ef1842fe6) [HF\_CALL\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57ad8620b141e11f48b46b9cd5ef1842fe6), /\* AG call indicator \*/

[ 904](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57a24ceb35eba4e18dbde198b77a7db98de) [HF\_CALL\_SETUP\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57a24ceb35eba4e18dbde198b77a7db98de), /\* AG call setup indicator \*/

[ 905](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57ad0cfee8ab087438502689d12cafa39cf) [HF\_CALL\_HELD\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57ad0cfee8ab087438502689d12cafa39cf), /\* AG call held indicator \*/

[ 906](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57ac5055465440ffe897930cbfdabb7c3d0) [HF\_SIGNAL\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57ac5055465440ffe897930cbfdabb7c3d0), /\* AG signal indicator \*/

[ 907](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57a3f9c27a235db99073918a904d6902eae) [HF\_ROAM\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57a3f9c27a235db99073918a904d6902eae), /\* AG roaming indicator \*/

[ 908](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57a1444cacc3f0307e7b53a0375807668c5) [HF\_BATTERY\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57a1444cacc3f0307e7b53a0375807668c5) /\* AG battery indicator \*/

909};

910

[ 927](group__bt__hfp.md#gab743d3e14fa13b71ddaf26d46cf41fb3)int [bt\_hfp\_hf\_indicator\_status](group__bt__hfp.md#gab743d3e14fa13b71ddaf26d46cf41fb3)(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status);

928

[ 940](group__bt__hfp.md#gab6710ce433812c3bf785b787008c36be)int [bt\_hfp\_hf\_enhanced\_safety](group__bt__hfp.md#gab6710ce433812c3bf785b787008c36be)(struct bt\_hfp\_hf \*hf, bool enable);

941

[ 953](group__bt__hfp.md#ga2f0e6012503a9b59b03a0fb508d12f88)int [bt\_hfp\_hf\_battery](group__bt__hfp.md#ga2f0e6012503a9b59b03a0fb508d12f88)(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level);

954

955#ifdef \_\_cplusplus

956}

957#endif

958

962

963#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_HFP\_HF\_H\_ \*/

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[bt\_hfp\_hf\_join\_conversation](group__bt__hfp.md#ga04d9fe3524c9522e98830507886bdfc6)

int bt\_hfp\_hf\_join\_conversation(struct bt\_hfp\_hf \*hf)

Handsfree HF add a held call to the conversation.

[bt\_hfp\_hf\_vgm](group__bt__hfp.md#ga0602cee7a90ca4afe90b65d748024472)

int bt\_hfp\_hf\_vgm(struct bt\_hfp\_hf \*hf, uint8\_t gain)

Handsfree HF report Gain of Microphone (VGM).

[bt\_hfp\_hf\_release\_all\_held](group__bt__hfp.md#ga06e7e93578601693fa377a240e0d18a7)

int bt\_hfp\_hf\_release\_all\_held(struct bt\_hfp\_hf \*hf)

Handsfree HF release all held calls.

[bt\_hfp\_hf\_vgs](group__bt__hfp.md#ga0c1c35b3117f78f43a6300d4ff7dd18b)

int bt\_hfp\_hf\_vgs(struct bt\_hfp\_hf \*hf, uint8\_t gain)

Handsfree HF report Gain of Speaker (VGS).

[bt\_hfp\_hf\_release\_specified\_call](group__bt__hfp.md#ga1ad888c3b967d3f9b2e5ccee303b9ad7)

int bt\_hfp\_hf\_release\_specified\_call(struct bt\_hfp\_hf\_call \*call)

Handsfree HF release call with specified index.

[bt\_hfp\_hf\_explicit\_call\_transfer](group__bt__hfp.md#ga2b48a0938e65899417b2f3ab1fa4c548)

int bt\_hfp\_hf\_explicit\_call\_transfer(struct bt\_hfp\_hf \*hf)

Handsfree HF explicit call transfer.

[bt\_hfp\_hf\_register](group__bt__hfp.md#ga2e4a7c05a3ba9a32eab50b9904f7f161)

int bt\_hfp\_hf\_register(struct bt\_hfp\_hf\_cb \*cb)

Register HFP HF profile.

[bt\_hfp\_hf\_battery](group__bt__hfp.md#ga2f0e6012503a9b59b03a0fb508d12f88)

int bt\_hfp\_hf\_battery(struct bt\_hfp\_hf \*hf, uint8\_t level)

Handsfree HF remaining battery level.

[bt\_hfp\_hf\_connect](group__bt__hfp.md#ga302e9ed397b056edef518470c6ea1d62)

int bt\_hfp\_hf\_connect(struct bt\_conn \*conn, struct bt\_hfp\_hf \*\*hf, uint8\_t channel)

Initiate the service level connection establishment procedure.

[bt\_hfp\_hf\_select\_codec](group__bt__hfp.md#ga34649dbecca2513c0b5bcd0e109b2551)

int bt\_hfp\_hf\_select\_codec(struct bt\_hfp\_hf \*hf, uint8\_t codec\_id)

Handsfree HF set selected codec id.

[bt\_hfp\_hf\_release\_active\_accept\_other](group__bt__hfp.md#ga36be4ff5fd805c4413ba90b1f62b9143)

int bt\_hfp\_hf\_release\_active\_accept\_other(struct bt\_hfp\_hf \*hf)

Handsfree HF release all active calls and accept other call.

[bt\_hfp\_hf\_call\_waiting\_notify](group__bt__hfp.md#ga3afb0d82551708975dbeb9c903c3d1fb)

int bt\_hfp\_hf\_call\_waiting\_notify(struct bt\_hfp\_hf \*hf, bool enable)

Handsfree HF enable/disable call waiting notification.

[bt\_hfp\_hf\_ready\_to\_accept\_audio](group__bt__hfp.md#ga3f6b43bf53fa04a6e71e883dc38f988b)

int bt\_hfp\_hf\_ready\_to\_accept\_audio(struct bt\_hfp\_hf \*hf)

Handsfree HF indicate that the HF is ready to accept audio.

[bt\_hfp\_hf\_hold\_active\_accept\_other](group__bt__hfp.md#ga40de46a6651eb85aa6d04ad66f528803)

int bt\_hfp\_hf\_hold\_active\_accept\_other(struct bt\_hfp\_hf \*hf)

Handsfree HF hold all active calls and accept other call.

[bt\_hfp\_hf\_hold\_incoming](group__bt__hfp.md#ga540bf6ec23c632b3f736e6302ef32ebd)

int bt\_hfp\_hf\_hold\_incoming(struct bt\_hfp\_hf\_call \*call)

Handsfree HF put the incoming call on hold.

[bt\_hfp\_hf\_accept](group__bt__hfp.md#ga5bad80355fd7903abcee84437d399829)

int bt\_hfp\_hf\_accept(struct bt\_hfp\_hf\_call \*call)

Handsfree HF accept the incoming call.

[bt\_hfp\_hf\_cli](group__bt__hfp.md#ga64ac1971dc7b1dacf6685bdc0c71e34c)

int bt\_hfp\_hf\_cli(struct bt\_hfp\_hf \*hf, bool enable)

Handsfree HF enable/disable Calling Line Identification (CLI) Notification.

[bt\_hfp\_hf\_transmit\_dtmf\_code](group__bt__hfp.md#ga6a3a6bc61a3a74f5a4a48d7e39bd74a0)

int bt\_hfp\_hf\_transmit\_dtmf\_code(struct bt\_hfp\_hf\_call \*call, char code)

Handsfree HF Transmit A specific DTMF Code.

[bt\_hfp\_hf\_query\_respond\_hold\_status](group__bt__hfp.md#ga70e086f6a02cb116317a8e80f76abf6d)

int bt\_hfp\_hf\_query\_respond\_hold\_status(struct bt\_hfp\_hf \*hf)

Handsfree HF query respond and hold status of AG.

[bt\_hfp\_hf\_set\_udub](group__bt__hfp.md#ga7389e5723e01b661b5e9c9d2114918b8)

int bt\_hfp\_hf\_set\_udub(struct bt\_hfp\_hf \*hf)

Handsfree HF set User Determined User Busy (UDUB) for a waiting call.

[bt\_hfp\_hf\_turn\_off\_ecnr](group__bt__hfp.md#ga7f37a9c009b4e55b7060d635c5b0c67b)

int bt\_hfp\_hf\_turn\_off\_ecnr(struct bt\_hfp\_hf \*hf)

Handsfree HF turns off AG's EC and NR.

[hfp\_hf\_ag\_indicators](group__bt__hfp.md#ga862b201be555821e932f6df5599eaa57)

hfp\_hf\_ag\_indicators

**Definition** hfp\_hf.h:901

[bt\_hfp\_hf\_set\_codecs](group__bt__hfp.md#ga91fc2204f50df07567f87a2b7a18e69f)

int bt\_hfp\_hf\_set\_codecs(struct bt\_hfp\_hf \*hf, uint8\_t codec\_ids)

Handsfree HF set supported codec ids.

[bt\_hfp\_hf\_request\_phone\_number](group__bt__hfp.md#ga92d89b0b37186688e86091a7a8015245)

int bt\_hfp\_hf\_request\_phone\_number(struct bt\_hfp\_hf \*hf)

Handsfree HF attach a phone number for a voice tag.

[bt\_hfp\_hf\_redial](group__bt__hfp.md#ga9611012a35df66fac324b99b16e5d958)

int bt\_hfp\_hf\_redial(struct bt\_hfp\_hf \*hf)

Handsfree HF redial last number.

[bt\_hfp\_hf\_get\_operator](group__bt__hfp.md#gaaa9fbdceec140f274fc88c063a4cd4b8)

int bt\_hfp\_hf\_get\_operator(struct bt\_hfp\_hf \*hf)

Handsfree HF requests currently selected operator.

[bt\_hfp\_hf\_enhanced\_safety](group__bt__hfp.md#gab6710ce433812c3bf785b787008c36be)

int bt\_hfp\_hf\_enhanced\_safety(struct bt\_hfp\_hf \*hf, bool enable)

Handsfree HF enable/disable enhanced safety.

[bt\_hfp\_hf\_indicator\_status](group__bt__hfp.md#gab743d3e14fa13b71ddaf26d46cf41fb3)

int bt\_hfp\_hf\_indicator\_status(struct bt\_hfp\_hf \*hf, uint8\_t status)

Handsfree HF set AG indicator activated/deactivated status.

[bt\_hfp\_hf\_memory\_dial](group__bt__hfp.md#gabacb666eb0f43db8614413a4ae0ce60a)

int bt\_hfp\_hf\_memory\_dial(struct bt\_hfp\_hf \*hf, const char \*location)

Handsfree HF memory dialing call.

[bt\_hfp\_hf\_terminate](group__bt__hfp.md#gabbce5fbf0dec27e1c5a4da144fbfc9c1)

int bt\_hfp\_hf\_terminate(struct bt\_hfp\_hf\_call \*call)

Handsfree HF terminate the incoming call.

[bt\_hfp\_hf\_private\_consultation\_mode](group__bt__hfp.md#gac3c038818cda3645eaadc5374d18c3ee)

int bt\_hfp\_hf\_private\_consultation\_mode(struct bt\_hfp\_hf\_call \*call)

Handsfree HF request private consultation mode with specified call.

[bt\_hfp\_hf\_reject](group__bt__hfp.md#gac4e3d88b80b69840d52050dcd72c9ab3)

int bt\_hfp\_hf\_reject(struct bt\_hfp\_hf\_call \*call)

Handsfree HF reject the incoming call.

[bt\_hfp\_hf\_number\_call](group__bt__hfp.md#gac57d7188e3f8b6e1e28d2a55c2567dbf)

int bt\_hfp\_hf\_number\_call(struct bt\_hfp\_hf \*hf, const char \*number)

Handsfree HF phone number call.

[bt\_hfp\_hf\_audio\_connect](group__bt__hfp.md#gad29bf40953faf638cc08acf919eb8f4f)

int bt\_hfp\_hf\_audio\_connect(struct bt\_hfp\_hf \*hf)

Handsfree HF setup audio connection.

[bt\_hfp\_hf\_query\_subscriber](group__bt__hfp.md#gad5dab4dcb66d52a80e0689a86de5fec3)

int bt\_hfp\_hf\_query\_subscriber(struct bt\_hfp\_hf \*hf)

Handsfree HF Query Subscriber Number Information.

[bt\_hfp\_hf\_voice\_recognition](group__bt__hfp.md#gaeed952ce163ef2466ece04af24b76a28)

int bt\_hfp\_hf\_voice\_recognition(struct bt\_hfp\_hf \*hf, bool activate)

Handsfree HF enable/disable the voice recognition function.

[bt\_hfp\_hf\_disconnect](group__bt__hfp.md#gaf5e7ef119731c0dc35bec61fb7c34774)

int bt\_hfp\_hf\_disconnect(struct bt\_hfp\_hf \*hf)

Release the service level connection.

[HF\_BATTERY\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57a1444cacc3f0307e7b53a0375807668c5)

@ HF\_BATTERY\_IND

**Definition** hfp\_hf.h:908

[HF\_CALL\_SETUP\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57a24ceb35eba4e18dbde198b77a7db98de)

@ HF\_CALL\_SETUP\_IND

**Definition** hfp\_hf.h:904

[HF\_ROAM\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57a3f9c27a235db99073918a904d6902eae)

@ HF\_ROAM\_IND

**Definition** hfp\_hf.h:907

[HF\_SIGNAL\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57ac5055465440ffe897930cbfdabb7c3d0)

@ HF\_SIGNAL\_IND

**Definition** hfp\_hf.h:906

[HF\_CALL\_HELD\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57ad0cfee8ab087438502689d12cafa39cf)

@ HF\_CALL\_HELD\_IND

**Definition** hfp\_hf.h:905

[HF\_CALL\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57ad8620b141e11f48b46b9cd5ef1842fe6)

@ HF\_CALL\_IND

**Definition** hfp\_hf.h:903

[HF\_SERVICE\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57adb3fae0b3684e8d035e195a91d24deb8)

@ HF\_SERVICE\_IND

**Definition** hfp\_hf.h:902

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md)

HFP profile application callback.

**Definition** hfp\_hf.h:36

[bt\_hfp\_hf\_cb::voice\_recognition](structbt__hfp__hf__cb.md#a07da1a6c86031c42749972d5d9fb7677)

void(\* voice\_recognition)(struct bt\_hfp\_hf \*hf, bool activate)

Voice recognition activation/deactivation callback.

**Definition** hfp\_hf.h:321

[bt\_hfp\_hf\_cb::ecnr\_turn\_off](structbt__hfp__hf__cb.md#a0f2da8d9169658c03d2dabe2c8b1cf6f)

void(\* ecnr\_turn\_off)(struct bt\_hfp\_hf \*hf, int err)

HF ECNR turns off callback.

**Definition** hfp\_hf.h:292

[bt\_hfp\_hf\_cb::roam](structbt__hfp__hf__cb.md#a13b35eb32e4f579d853657a2ea89af42)

void(\* roam)(struct bt\_hfp\_hf \*hf, uint32\_t value)

HF indicator Callback.

**Definition** hfp\_hf.h:170

[bt\_hfp\_hf\_cb::battery](structbt__hfp__hf__cb.md#a17faaab9a9af5dc53018fc2f94855bea)

void(\* battery)(struct bt\_hfp\_hf \*hf, uint32\_t value)

HF indicator Callback.

**Definition** hfp\_hf.h:178

[bt\_hfp\_hf\_cb::textual\_representation](structbt__hfp__hf__cb.md#a1e7a4046b01ce4753352f86c209e171f)

void(\* textual\_representation)(struct bt\_hfp\_hf \*hf, char \*id, uint8\_t type, uint8\_t operation, char \*text)

Textual representation callback.

**Definition** hfp\_hf.h:374

[bt\_hfp\_hf\_cb::ring\_indication](structbt__hfp__hf__cb.md#a2712d3a5d68bdf2de6dc27f938590c0a)

void(\* ring\_indication)(struct bt\_hfp\_hf\_call \*call)

HF incoming call Ring indication callback to application.

**Definition** hfp\_hf.h:186

[bt\_hfp\_hf\_cb::call\_waiting](structbt__hfp__hf__cb.md#a283a791f330a49f402cde0233ad05f6e)

void(\* call\_waiting)(struct bt\_hfp\_hf\_call \*call, char \*number, uint8\_t type)

HF call waiting notification callback to application.

**Definition** hfp\_hf.h:307

[bt\_hfp\_hf\_cb::vre\_state](structbt__hfp__hf__cb.md#a298a6d3315535331ffb779899db9f973)

void(\* vre\_state)(struct bt\_hfp\_hf \*hf, uint8\_t state)

Voice recognition engine state callback.

**Definition** hfp\_hf.h:338

[bt\_hfp\_hf\_cb::vgs](structbt__hfp__hf__cb.md#a385cbe2c3a9c402a09b873a3ce753d8b)

void(\* vgs)(struct bt\_hfp\_hf \*hf, uint8\_t gain)

HF speaker gain notification callback to application.

**Definition** hfp\_hf.h:231

[bt\_hfp\_hf\_cb::accept](structbt__hfp__hf__cb.md#a44ae68eb055f23c30dd761fd6eb1c6cd)

void(\* accept)(struct bt\_hfp\_hf\_call \*call)

HF call accept Callback.

**Definition** hfp\_hf.h:124

[bt\_hfp\_hf\_cb::sco\_disconnected](structbt__hfp__hf__cb.md#a4586240506c876c9f58cf60a091b4044)

void(\* sco\_disconnected)(struct bt\_conn \*sco\_conn, uint8\_t reason)

HF SCO/eSCO disconnected Callback.

**Definition** hfp\_hf.h:74

[bt\_hfp\_hf\_cb::outgoing](structbt__hfp__hf__cb.md#a46677dbfe7e73dcdc3b6cacb0aa9fa58)

void(\* outgoing)(struct bt\_hfp\_hf \*hf, struct bt\_hfp\_hf\_call \*call)

HF call outgoing Callback.

**Definition** hfp\_hf.h:91

[bt\_hfp\_hf\_cb::retrieve](structbt__hfp__hf__cb.md#a4977076381a5c4daf620aa6c6ab558d3)

void(\* retrieve)(struct bt\_hfp\_hf\_call \*call)

HF call retrieve Callback.

**Definition** hfp\_hf.h:154

[bt\_hfp\_hf\_cb::vgm](structbt__hfp__hf__cb.md#a512de9839559def9c2110a310f21ca03)

void(\* vgm)(struct bt\_hfp\_hf \*hf, uint8\_t gain)

HF microphone gain notification callback to application.

**Definition** hfp\_hf.h:219

[bt\_hfp\_hf\_cb::incoming](structbt__hfp__hf__cb.md#a597d2e9b20ffc2dfedd53aea2969727e)

void(\* incoming)(struct bt\_hfp\_hf \*hf, struct bt\_hfp\_hf\_call \*call)

HF call incoming Callback.

**Definition** hfp\_hf.h:108

[bt\_hfp\_hf\_cb::connected](structbt__hfp__hf__cb.md#a68c09fe6aac4ff7f3b24e6a550e75d1e)

void(\* connected)(struct bt\_conn \*conn, struct bt\_hfp\_hf \*hf)

HF connected callback to application.

**Definition** hfp\_hf.h:45

[bt\_hfp\_hf\_cb::terminate](structbt__hfp__hf__cb.md#a691ec076d6fba14636b873cf75262e81)

void(\* terminate)(struct bt\_hfp\_hf\_call \*call)

HF call terminate Callback.

**Definition** hfp\_hf.h:140

[bt\_hfp\_hf\_cb::sco\_connected](structbt__hfp__hf__cb.md#a6ea6f5a866d7e4da5e3fe894d700f6b6)

void(\* sco\_connected)(struct bt\_hfp\_hf \*hf, struct bt\_conn \*sco\_conn)

HF SCO/eSCO connected Callback.

**Definition** hfp\_hf.h:65

[bt\_hfp\_hf\_cb::incoming\_held](structbt__hfp__hf__cb.md#a71f0f50a83defe014b3b364dcc16ad9d)

void(\* incoming\_held)(struct bt\_hfp\_hf\_call \*call)

HF incoming call on hold Callback.

**Definition** hfp\_hf.h:116

[bt\_hfp\_hf\_cb::dialing](structbt__hfp__hf__cb.md#a80e98b5dd212158c255215b8a304d67c)

void(\* dialing)(struct bt\_hfp\_hf \*hf, int err)

HF call dialing Callback.

**Definition** hfp\_hf.h:194

[bt\_hfp\_hf\_cb::service](structbt__hfp__hf__cb.md#a8483c3a3ba8b0e5131bec6fce5dbc36d)

void(\* service)(struct bt\_hfp\_hf \*hf, uint32\_t value)

HF indicator Callback.

**Definition** hfp\_hf.h:82

[bt\_hfp\_hf\_cb::reject](structbt__hfp__hf__cb.md#a9f248f9c7e3830c6941225bd4d2363d3)

void(\* reject)(struct bt\_hfp\_hf\_call \*call)

HF call reject Callback.

**Definition** hfp\_hf.h:132

[bt\_hfp\_hf\_cb::clip](structbt__hfp__hf__cb.md#abcbdaa8312f6efe3711da0aabba52bce)

void(\* clip)(struct bt\_hfp\_hf\_call \*call, char \*number, uint8\_t type)

HF calling line identification notification callback to application.

**Definition** hfp\_hf.h:207

[bt\_hfp\_hf\_cb::request\_phone\_number](structbt__hfp__hf__cb.md#ac1e9fb5d0446d498b6cf3705a05633e2)

void(\* request\_phone\_number)(struct bt\_hfp\_hf \*hf, const char \*number)

Request phone number callback.

**Definition** hfp\_hf.h:385

[bt\_hfp\_hf\_cb::inband\_ring](structbt__hfp__hf__cb.md#acc1ff77f98329986c2120b0c9c4f565a)

void(\* inband\_ring)(struct bt\_hfp\_hf \*hf, bool inband)

HF in-band ring tone notification callback to application.

**Definition** hfp\_hf.h:242

[bt\_hfp\_hf\_cb::remote\_ringing](structbt__hfp__hf__cb.md#ace8989f64fea9301d6f48e5252ceb2de)

void(\* remote\_ringing)(struct bt\_hfp\_hf\_call \*call)

HF call outgoing call is ringing Callback.

**Definition** hfp\_hf.h:99

[bt\_hfp\_hf\_cb::signal](structbt__hfp__hf__cb.md#add68ca4e00f7a5dbc28282ee29bea087)

void(\* signal)(struct bt\_hfp\_hf \*hf, uint32\_t value)

HF indicator Callback.

**Definition** hfp\_hf.h:162

[bt\_hfp\_hf\_cb::subscriber\_number](structbt__hfp__hf__cb.md#ae5682d96bdf18b148fac7ce1d9cbdb75)

void(\* subscriber\_number)(struct bt\_hfp\_hf \*hf, const char \*number, uint8\_t type, uint8\_t service)

Query subscriber number callback.

**Definition** hfp\_hf.h:417

[bt\_hfp\_hf\_cb::held](structbt__hfp__hf__cb.md#af6fe24140f5a5a1aea2eff7b1e534cfd)

void(\* held)(struct bt\_hfp\_hf\_call \*call)

HF call held Callback.

**Definition** hfp\_hf.h:147

[bt\_hfp\_hf\_cb::disconnected](structbt__hfp__hf__cb.md#afdf28b8d8f9598ee2f6fa826aba4fbba)

void(\* disconnected)(struct bt\_hfp\_hf \*hf)

HF disconnected callback to application.

**Definition** hfp\_hf.h:56

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [hfp\_hf.h](hfp__hf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
