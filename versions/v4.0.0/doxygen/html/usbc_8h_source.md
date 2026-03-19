---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/usbc_8h_source.html
original_path: doxygen/html/usbc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc.h

[Go to the documentation of this file.](usbc_8h.md)

1/\*

2 \* Copyright 2022 The Chromium OS Authors

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

12

13#ifndef ZEPHYR\_INCLUDE\_USBC\_H\_

14#define ZEPHYR\_INCLUDE\_USBC\_H\_

15

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17#include <[zephyr/device.h](device_8h.md)>

18#include <[zephyr/drivers/usb\_c/usbc\_tcpc.h](usbc__tcpc_8h.md)>

19#include <[zephyr/drivers/usb\_c/usbc\_vbus.h](usbc__vbus_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

32

[ 48](group____usbc__device__api.md#gaaa5c1f6278a7ca6d589c9c80695ca746)#define FIXED\_5V\_100MA\_RDO 0x1100280a

49

[ 53](group____usbc__device__api.md#ga38a301a97a5e1a85e9836bbf083859f3)enum [usbc\_policy\_request\_t](group____usbc__device__api.md#ga38a301a97a5e1a85e9836bbf083859f3) {

[ 55](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a2274197ac367b3da6358cac8dd781134) [REQUEST\_NOP](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a2274197ac367b3da6358cac8dd781134),

[ 57](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a899633a1b63b1c3a826b5556f0f23d8b) [REQUEST\_TC\_DISABLED](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a899633a1b63b1c3a826b5556f0f23d8b),

[ 59](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a8a7b77d81428f0c4784af3204f33b290) [REQUEST\_TC\_ERROR\_RECOVERY](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a8a7b77d81428f0c4784af3204f33b290),

[ 61](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a0c5ff3bc4c0d6f636663fd3911ed85d5) [REQUEST\_TC\_END](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a0c5ff3bc4c0d6f636663fd3911ed85d5),

62

[ 64](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a1fe9f57fac7f5149fe5f0f7c42523536) [REQUEST\_PE\_DR\_SWAP](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a1fe9f57fac7f5149fe5f0f7c42523536),

[ 66](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a7c3c9c959439ee73539cff13e561c403) [REQUEST\_PE\_HARD\_RESET\_SEND](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a7c3c9c959439ee73539cff13e561c403),

[ 68](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3ad45120b1ceabeb054c2c2273b8431894) [REQUEST\_PE\_SOFT\_RESET\_SEND](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3ad45120b1ceabeb054c2c2273b8431894),

[ 73](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a8c6083028ee8655cd0bebb6d9aab2e1e) [REQUEST\_PE\_GET\_SRC\_CAPS](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a8c6083028ee8655cd0bebb6d9aab2e1e),

[ 78](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3ade1edc3aef0e4d563934edbc9ce784bc) [REQUEST\_GET\_SNK\_CAPS](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3ade1edc3aef0e4d563934edbc9ce784bc),

[ 83](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3ae5b4eb0db00e81a98cfe2436b64a7018) [REQUEST\_PE\_GOTO\_MIN](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3ae5b4eb0db00e81a98cfe2436b64a7018),

84};

85

[ 89](group____usbc__device__api.md#ga66f934a5c5cd88b574c71d1f18fbda23)enum [usbc\_policy\_notify\_t](group____usbc__device__api.md#ga66f934a5c5cd88b574c71d1f18fbda23) {

[ 91](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a43bc56906b5dc4767d3297400053d286) [MSG\_ACCEPT\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a43bc56906b5dc4767d3297400053d286),

[ 93](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a4ad0620e76c694004d3a1b43458a14b2) [MSG\_REJECTED\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a4ad0620e76c694004d3a1b43458a14b2),

[ 95](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23aa316636e8353dad1a9d5dec8b85a67e4) [MSG\_DISCARDED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23aa316636e8353dad1a9d5dec8b85a67e4),

[ 97](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ab2f97ffaa13c84e656f7ac0004ec86ae) [MSG\_NOT\_SUPPORTED\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ab2f97ffaa13c84e656f7ac0004ec86ae),

[ 99](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a4020203569dcb95ab1b3d2946efced19) [DATA\_ROLE\_IS\_UFP](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a4020203569dcb95ab1b3d2946efced19),

[ 101](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a791604f4f0b2a2c3ccea4e98d1659a61) [DATA\_ROLE\_IS\_DFP](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a791604f4f0b2a2c3ccea4e98d1659a61),

[ 103](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23adbefad204068244fdf75ba1ff211fbfc) [PD\_CONNECTED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23adbefad204068244fdf75ba1ff211fbfc),

[ 105](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23adebcbf5155b43ce562127d4077d46d7d) [NOT\_PD\_CONNECTED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23adebcbf5155b43ce562127d4077d46d7d),

[ 107](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a3a27b8e70ffe5788aa3ffea1bf61cae9) [TRANSITION\_PS](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a3a27b8e70ffe5788aa3ffea1bf61cae9),

[ 109](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ad52e1c4f949bb64fef1d996ac2f4e0de) [PORT\_PARTNER\_NOT\_RESPONSIVE](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ad52e1c4f949bb64fef1d996ac2f4e0de),

[ 111](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a8cb937247ec21f791706f4f426496a8c) [PROTOCOL\_ERROR](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a8cb937247ec21f791706f4f426496a8c),

[ 113](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23aa02158d0afdd60c755453977200dfb28) [SNK\_TRANSITION\_TO\_DEFAULT](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23aa02158d0afdd60c755453977200dfb28),

[ 115](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ab74f5bcaa94a5fb1e46cdd7c6a5d822f) [HARD\_RESET\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ab74f5bcaa94a5fb1e46cdd7c6a5d822f),

[ 117](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a0fb0676a11ad8bad2d5249031ba5fd19) [POWER\_CHANGE\_0A0](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a0fb0676a11ad8bad2d5249031ba5fd19),

[ 119](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a3a50be6f70c1a7abd724ab447491c46a) [POWER\_CHANGE\_DEF](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a3a50be6f70c1a7abd724ab447491c46a),

[ 121](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a336bfb983c4d07684d67d4d9ef6c1489) [POWER\_CHANGE\_1A5](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a336bfb983c4d07684d67d4d9ef6c1489),

[ 123](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a3477c1c6ad8885c3ab7a9c58b7399dcf) [POWER\_CHANGE\_3A0](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a3477c1c6ad8885c3ab7a9c58b7399dcf),

[ 125](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ac22b0026881f65c574d0bf7454321745) [SENDER\_RESPONSE\_TIMEOUT](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ac22b0026881f65c574d0bf7454321745),

[ 127](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a0266a21d8c836cf281c30542eb6badd4) [SOURCE\_CAPABILITIES\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a0266a21d8c836cf281c30542eb6badd4),

128};

129

[ 133](group____usbc__device__api.md#gafea882f4f3cc96c502d53a24a3e5aec5)enum [usbc\_policy\_check\_t](group____usbc__device__api.md#gafea882f4f3cc96c502d53a24a3e5aec5) {

[ 135](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a1181a470497b797136cf0eb204394106) [CHECK\_POWER\_ROLE\_SWAP](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a1181a470497b797136cf0eb204394106),

[ 137](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5afa602e00bf418656e365baa4d9ff6cef) [CHECK\_DATA\_ROLE\_SWAP\_TO\_DFP](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5afa602e00bf418656e365baa4d9ff6cef),

[ 139](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a7c97208a8a12f70e7ffa43bb406b9ebd) [CHECK\_DATA\_ROLE\_SWAP\_TO\_UFP](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a7c97208a8a12f70e7ffa43bb406b9ebd),

[ 141](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a17f7f4fc9aa4178f0358769dedd29ade) [CHECK\_SNK\_AT\_DEFAULT\_LEVEL](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a17f7f4fc9aa4178f0358769dedd29ade),

[ 143](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a655e913c86db5caa961083dad9f6b7a1) [CHECK\_VCONN\_CONTROL](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a655e913c86db5caa961083dad9f6b7a1),

[ 145](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a42b660bb630edcca5ae8b031033d0718) [CHECK\_SRC\_PS\_AT\_DEFAULT\_LEVEL](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a42b660bb630edcca5ae8b031033d0718),

146};

147

[ 151](group____usbc__device__api.md#gadf5d2934b5dc8e2b01d20bb904988784)enum [usbc\_policy\_wait\_t](group____usbc__device__api.md#gadf5d2934b5dc8e2b01d20bb904988784) {

[ 153](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784a009ce2ceacd92db88d9a6beb01f84a28) [WAIT\_SINK\_REQUEST](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784a009ce2ceacd92db88d9a6beb01f84a28),

[ 155](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784a91f1f41bf9318e06c02c1957a39a762a) [WAIT\_POWER\_ROLE\_SWAP](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784a91f1f41bf9318e06c02c1957a39a762a),

[ 157](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784ae5ef03f78d78a7014404c581bad77c18) [WAIT\_DATA\_ROLE\_SWAP](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784ae5ef03f78d78a7014404c581bad77c18),

[ 159](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784aa982aed81f39e35cde74399c6d74e601) [WAIT\_VCONN\_SWAP](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784aa982aed81f39e35cde74399c6d74e601),

160};

161

[ 165](group____usbc__device__api.md#ga4c4f0592a034b4e49eee85e95af33f94)enum [usbc\_snk\_req\_reply\_t](group____usbc__device__api.md#ga4c4f0592a034b4e49eee85e95af33f94) {

[ 167](group____usbc__device__api.md#gga4c4f0592a034b4e49eee85e95af33f94a7922edb67afe83596819994a71de76dd) [SNK\_REQUEST\_VALID](group____usbc__device__api.md#gga4c4f0592a034b4e49eee85e95af33f94a7922edb67afe83596819994a71de76dd),

[ 169](group____usbc__device__api.md#gga4c4f0592a034b4e49eee85e95af33f94a714f82e830f9528a8200c2c14795b282) [SNK\_REQUEST\_REJECT](group____usbc__device__api.md#gga4c4f0592a034b4e49eee85e95af33f94a714f82e830f9528a8200c2c14795b282),

[ 171](group____usbc__device__api.md#gga4c4f0592a034b4e49eee85e95af33f94a7ae46f6deb593eedd0564d30cb4c75fb) [SNK\_REQUEST\_WAIT](group____usbc__device__api.md#gga4c4f0592a034b4e49eee85e95af33f94a7ae46f6deb593eedd0564d30cb4c75fb),

172};

173

[ 185](group__sink__callbacks.md#gaaed0161142c3481ce9180015b6968357)typedef int (\*[policy\_cb\_get\_snk\_cap\_t](group__sink__callbacks.md#gaaed0161142c3481ce9180015b6968357))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*\*pdos, int \*num\_pdos);

[ 194](group__sink__callbacks.md#ga6096d6909698f1b86a1a9cbd1f8d4097)typedef void (\*[policy\_cb\_set\_src\_cap\_t](group__sink__callbacks.md#ga6096d6909698f1b86a1a9cbd1f8d4097))(const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*pdos,

195 const int num\_pdos);

196

[ 204](group__sink__callbacks.md#ga2aacd704d08a8cecbf818150e8ec51b6)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[policy\_cb\_check\_t](group__sink__callbacks.md#ga2aacd704d08a8cecbf818150e8ec51b6))(const struct [device](structdevice.md) \*dev,

205 const enum [usbc\_policy\_check\_t](group____usbc__device__api.md#gafea882f4f3cc96c502d53a24a3e5aec5) policy\_check);

206

[ 215](group__sink__callbacks.md#gaea62016b263dfaf5f869dd6ea036fdad)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[policy\_cb\_wait\_notify\_t](group__sink__callbacks.md#gaea62016b263dfaf5f869dd6ea036fdad))(const struct [device](structdevice.md) \*dev,

216 const enum [usbc\_policy\_wait\_t](group____usbc__device__api.md#gadf5d2934b5dc8e2b01d20bb904988784) wait\_notify);

217

[ 225](group__sink__callbacks.md#ga44af668d9c22e757983c803d7b8ff82e)typedef void (\*[policy\_cb\_notify\_t](group__sink__callbacks.md#ga44af668d9c22e757983c803d7b8ff82e))(const struct [device](structdevice.md) \*dev,

226 const enum [usbc\_policy\_notify\_t](group____usbc__device__api.md#ga66f934a5c5cd88b574c71d1f18fbda23) policy\_notify);

227

[ 234](group__sink__callbacks.md#gae0448c6b271273c5db59775c3a6260dc)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[policy\_cb\_get\_rdo\_t](group__sink__callbacks.md#gae0448c6b271273c5db59775c3a6260dc))(const struct [device](structdevice.md) \*dev);

235

[ 243](group__sink__callbacks.md#ga1a3da6faad509213f607893fef16b673)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[policy\_cb\_is\_snk\_at\_default\_t](group__sink__callbacks.md#ga1a3da6faad509213f607893fef16b673))(const struct [device](structdevice.md) \*dev);

244

[ 258](group__source__callbacks.md#gaeeda677224456f685137e4b345c0e173)typedef int (\*[policy\_cb\_get\_src\_caps\_t](group__source__callbacks.md#ga4bbf78bd752d38d915412dd942d3aab8))(const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*\*pdos,

259 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*num\_pdos);

260

268typedef enum [usbc\_snk\_req\_reply\_t](group____usbc__device__api.md#ga4c4f0592a034b4e49eee85e95af33f94) (\*[policy\_cb\_check\_sink\_request\_t](group__source__callbacks.md#gaeeda677224456f685137e4b345c0e173))(const struct [device](structdevice.md) \*dev,

269 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) request\_msg);

270

[ 277](group__source__callbacks.md#gae7391e858485e44a74e5fcdbb7931ca7)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[policy\_cb\_is\_ps\_ready\_t](group__source__callbacks.md#gae7391e858485e44a74e5fcdbb7931ca7))(const struct [device](structdevice.md) \*dev);

278

[ 286](group__source__callbacks.md#ga2925e462140a700920251d92ae5a3aa4)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[policy\_cb\_present\_contract\_is\_valid\_t](group__source__callbacks.md#ga2925e462140a700920251d92ae5a3aa4))(const struct [device](structdevice.md) \*dev,

287 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) present\_contract);

288

[ 296](group__source__callbacks.md#ga699811c862990b31ec0126dd3a4c3e4d)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[policy\_cb\_change\_src\_caps\_t](group__source__callbacks.md#ga699811c862990b31ec0126dd3a4c3e4d))(const struct [device](structdevice.md) \*dev);

297

[ 306](group__source__callbacks.md#gae903c8108e8d1563cb0b1ccdd901c925)typedef void (\*[policy\_cb\_set\_port\_partner\_snk\_cap\_t](group__source__callbacks.md#gae903c8108e8d1563cb0b1ccdd901c925))(const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*pdos,

307 const int num\_pdos);

[ 316](group__source__callbacks.md#ga7c75f8192001179f20bf1fe48316f3c6)typedef int (\*[policy\_cb\_get\_src\_rp\_t](group__source__callbacks.md#ga7c75f8192001179f20bf1fe48316f3c6))(const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \*rp);

[ 324](group__source__callbacks.md#gaaecac7683d7092c0a477e8d9ca0e5a33)typedef int (\*[policy\_cb\_src\_en\_t](group__source__callbacks.md#gaaecac7683d7092c0a477e8d9ca0e5a33))(const struct [device](structdevice.md) \*dev, bool en);

326

[ 334](group____usbc__device__api.md#ga1535f7f53b3cc859ff536883fd631830)int [usbc\_start](group____usbc__device__api.md#ga1535f7f53b3cc859ff536883fd631830)(const struct [device](structdevice.md) \*dev);

335

[ 343](group____usbc__device__api.md#ga68b73c03a5098a21260b5c3638edc973)int [usbc\_suspend](group____usbc__device__api.md#ga68b73c03a5098a21260b5c3638edc973)(const struct [device](structdevice.md) \*dev);

344

[ 353](group____usbc__device__api.md#ga42691b0bb2b4be50147ac655e2cd9761)int [usbc\_request](group____usbc__device__api.md#ga42691b0bb2b4be50147ac655e2cd9761)(const struct [device](structdevice.md) \*dev, const enum [usbc\_policy\_request\_t](group____usbc__device__api.md#ga38a301a97a5e1a85e9836bbf083859f3) req);

354

[ 362](group____usbc__device__api.md#ga0ffb467dc02585187e9543b17abd6c6a)void [usbc\_bypass\_next\_sleep](group____usbc__device__api.md#ga0ffb467dc02585187e9543b17abd6c6a)(const struct [device](structdevice.md) \*dev);

363

[ 370](group____usbc__device__api.md#ga997007cab2e54ad53b774b4215d0f593)void [usbc\_set\_dpm\_data](group____usbc__device__api.md#ga997007cab2e54ad53b774b4215d0f593)(const struct [device](structdevice.md) \*dev, void \*dpm\_data);

371

[ 380](group____usbc__device__api.md#gabd99b6926baf67212d65c4a4d147ce5b)void \*[usbc\_get\_dpm\_data](group____usbc__device__api.md#gabd99b6926baf67212d65c4a4d147ce5b)(const struct [device](structdevice.md) \*dev);

381

[ 388](group____usbc__device__api.md#ga9846b36061453023e16c160f5f120159)void [usbc\_set\_vconn\_control\_cb](group____usbc__device__api.md#ga9846b36061453023e16c160f5f120159)(const struct [device](structdevice.md) \*dev, const [tcpc\_vconn\_control\_cb\_t](group__usb__type__c__port__controller__api.md#ga7a989ffd6bdc83696188de59acbd49c7) cb);

389

[ 396](group____usbc__device__api.md#ga8741df33b5432d9c7d5902af9bd67084)void [usbc\_set\_vconn\_discharge\_cb](group____usbc__device__api.md#ga8741df33b5432d9c7d5902af9bd67084)(const struct [device](structdevice.md) \*dev, const [tcpc\_vconn\_discharge\_cb\_t](group__usb__type__c__port__controller__api.md#ga4437e66605f988be1e16c52b9912e9c2) cb);

397

[ 404](group____usbc__device__api.md#ga67a046b411134d7c631942ae6ba73fc5)void [usbc\_set\_policy\_cb\_check](group____usbc__device__api.md#ga67a046b411134d7c631942ae6ba73fc5)(const struct [device](structdevice.md) \*dev, const [policy\_cb\_check\_t](group__sink__callbacks.md#ga2aacd704d08a8cecbf818150e8ec51b6) cb);

405

[ 413](group____usbc__device__api.md#gaedec1b4ad7b028ad18e1bcbe5396f1ee)void [usbc\_set\_policy\_cb\_notify](group____usbc__device__api.md#gaedec1b4ad7b028ad18e1bcbe5396f1ee)(const struct [device](structdevice.md) \*dev, const [policy\_cb\_notify\_t](group__sink__callbacks.md#ga44af668d9c22e757983c803d7b8ff82e) cb);

414

[ 422](group____usbc__device__api.md#gaa295593c7d5ede31328efaaab38b5880)void [usbc\_set\_policy\_cb\_wait\_notify](group____usbc__device__api.md#gaa295593c7d5ede31328efaaab38b5880)(const struct [device](structdevice.md) \*dev, const [policy\_cb\_wait\_notify\_t](group__sink__callbacks.md#gaea62016b263dfaf5f869dd6ea036fdad) cb);

423

[ 430](group____usbc__device__api.md#gafbd2885d758aa869635041fa89750596)void [usbc\_set\_policy\_cb\_get\_snk\_cap](group____usbc__device__api.md#gafbd2885d758aa869635041fa89750596)(const struct [device](structdevice.md) \*dev, const [policy\_cb\_get\_snk\_cap\_t](group__sink__callbacks.md#gaaed0161142c3481ce9180015b6968357) cb);

431

[ 439](group____usbc__device__api.md#ga4536f47082f58f49d492de6f2b00dd17)void [usbc\_set\_policy\_cb\_set\_src\_cap](group____usbc__device__api.md#ga4536f47082f58f49d492de6f2b00dd17)(const struct [device](structdevice.md) \*dev, const [policy\_cb\_set\_src\_cap\_t](group__sink__callbacks.md#ga6096d6909698f1b86a1a9cbd1f8d4097) cb);

440

[ 447](group____usbc__device__api.md#ga7c1ffea81f71416ab2942fc5a5b67d41)void [usbc\_set\_policy\_cb\_get\_rdo](group____usbc__device__api.md#ga7c1ffea81f71416ab2942fc5a5b67d41)(const struct [device](structdevice.md) \*dev, const [policy\_cb\_get\_rdo\_t](group__sink__callbacks.md#gae0448c6b271273c5db59775c3a6260dc) cb);

448

[ 456](group____usbc__device__api.md#gaffa045ee6e2fbc07fde7e84e44d3853f)void [usbc\_set\_policy\_cb\_is\_snk\_at\_default](group____usbc__device__api.md#gaffa045ee6e2fbc07fde7e84e44d3853f)(const struct [device](structdevice.md) \*dev,

457 const [policy\_cb\_is\_snk\_at\_default\_t](group__sink__callbacks.md#ga1a3da6faad509213f607893fef16b673) cb);

458

[ 466](group____usbc__device__api.md#ga8974f9661dfebf8f686d677f999d5957)void [usbc\_set\_policy\_cb\_get\_src\_rp](group____usbc__device__api.md#ga8974f9661dfebf8f686d677f999d5957)(const struct [device](structdevice.md) \*dev, const [policy\_cb\_get\_src\_rp\_t](group__source__callbacks.md#ga7c75f8192001179f20bf1fe48316f3c6) cb);

467

[ 474](group____usbc__device__api.md#gaf5332ba0c87ff737e1c476d7be071fec)void [usbc\_set\_policy\_cb\_src\_en](group____usbc__device__api.md#gaf5332ba0c87ff737e1c476d7be071fec)(const struct [device](structdevice.md) \*dev, const [policy\_cb\_src\_en\_t](group__source__callbacks.md#gaaecac7683d7092c0a477e8d9ca0e5a33) cb);

475

[ 483](group____usbc__device__api.md#ga7800c065ae5cfb7a95b58865d47c7f04)void [usbc\_set\_policy\_cb\_get\_src\_caps](group____usbc__device__api.md#ga7800c065ae5cfb7a95b58865d47c7f04)(const struct [device](structdevice.md) \*dev, const [policy\_cb\_get\_src\_caps\_t](group__source__callbacks.md#ga4bbf78bd752d38d915412dd942d3aab8) cb);

484

[ 491](group____usbc__device__api.md#ga7f85188cc4f1a95350195abd0d736ada)void [usbc\_set\_policy\_cb\_check\_sink\_request](group____usbc__device__api.md#ga7f85188cc4f1a95350195abd0d736ada)(const struct [device](structdevice.md) \*dev,

492 const [policy\_cb\_check\_sink\_request\_t](group__source__callbacks.md#gaeeda677224456f685137e4b345c0e173) cb);

493

[ 500](group____usbc__device__api.md#gaf25c9cc2b6c514b9dcddc8129a76ccee)void [usbc\_set\_policy\_cb\_is\_ps\_ready](group____usbc__device__api.md#gaf25c9cc2b6c514b9dcddc8129a76ccee)(const struct [device](structdevice.md) \*dev,

501 const [policy\_cb\_is\_ps\_ready\_t](group__source__callbacks.md#gae7391e858485e44a74e5fcdbb7931ca7) cb);

502

[ 509](group____usbc__device__api.md#ga5b4adb4330dfadf127d0a01253d722bb)void [usbc\_set\_policy\_cb\_present\_contract\_is\_valid](group____usbc__device__api.md#ga5b4adb4330dfadf127d0a01253d722bb)(const struct [device](structdevice.md) \*dev,

510 const [policy\_cb\_present\_contract\_is\_valid\_t](group__source__callbacks.md#ga2925e462140a700920251d92ae5a3aa4) cb);

511

[ 519](group____usbc__device__api.md#gaa8f89bfb1e9a1840b2d61ebaa13aeb2f)void [usbc\_set\_policy\_cb\_change\_src\_caps](group____usbc__device__api.md#gaa8f89bfb1e9a1840b2d61ebaa13aeb2f)(const struct [device](structdevice.md) \*dev,

520 const [policy\_cb\_change\_src\_caps\_t](group__source__callbacks.md#ga699811c862990b31ec0126dd3a4c3e4d) cb);

521

[ 528](group____usbc__device__api.md#gafd0a407558bb92dc8b7007d9d717b940)void [usbc\_set\_policy\_cb\_set\_port\_partner\_snk\_cap](group____usbc__device__api.md#gafd0a407558bb92dc8b7007d9d717b940)(const struct [device](structdevice.md) \*dev,

529 const [policy\_cb\_set\_port\_partner\_snk\_cap\_t](group__source__callbacks.md#gae903c8108e8d1563cb0b1ccdd901c925) cb);

530

534

535#ifdef \_\_cplusplus

536}

537#endif

538

539#endif /\* ZEPHYR\_INCLUDE\_USBC\_H\_ \*/

[device.h](device_8h.md)

[usbc\_bypass\_next\_sleep](group____usbc__device__api.md#ga0ffb467dc02585187e9543b17abd6c6a)

void usbc\_bypass\_next\_sleep(const struct device \*dev)

[usbc\_start](group____usbc__device__api.md#ga1535f7f53b3cc859ff536883fd631830)

int usbc\_start(const struct device \*dev)

Start the USB-C Subsystem.

[usbc\_policy\_request\_t](group____usbc__device__api.md#ga38a301a97a5e1a85e9836bbf083859f3)

usbc\_policy\_request\_t

Device Policy Manager requests.

**Definition** usbc.h:53

[usbc\_request](group____usbc__device__api.md#ga42691b0bb2b4be50147ac655e2cd9761)

int usbc\_request(const struct device \*dev, const enum usbc\_policy\_request\_t req)

Make a request of the USB-C Subsystem.

[usbc\_set\_policy\_cb\_set\_src\_cap](group____usbc__device__api.md#ga4536f47082f58f49d492de6f2b00dd17)

void usbc\_set\_policy\_cb\_set\_src\_cap(const struct device \*dev, const policy\_cb\_set\_src\_cap\_t cb)

Set the callback used to store the received Port Partner's Source Capabilities.

[usbc\_snk\_req\_reply\_t](group____usbc__device__api.md#ga4c4f0592a034b4e49eee85e95af33f94)

usbc\_snk\_req\_reply\_t

Device Policy Manager's response to a Sink Request.

**Definition** usbc.h:165

[usbc\_set\_policy\_cb\_present\_contract\_is\_valid](group____usbc__device__api.md#ga5b4adb4330dfadf127d0a01253d722bb)

void usbc\_set\_policy\_cb\_present\_contract\_is\_valid(const struct device \*dev, const policy\_cb\_present\_contract\_is\_valid\_t cb)

Set the callback to check if present Contract is still valid.

[usbc\_policy\_notify\_t](group____usbc__device__api.md#ga66f934a5c5cd88b574c71d1f18fbda23)

usbc\_policy\_notify\_t

Device Policy Manager notifications.

**Definition** usbc.h:89

[usbc\_set\_policy\_cb\_check](group____usbc__device__api.md#ga67a046b411134d7c631942ae6ba73fc5)

void usbc\_set\_policy\_cb\_check(const struct device \*dev, const policy\_cb\_check\_t cb)

Set the callback used to check a policy.

[usbc\_suspend](group____usbc__device__api.md#ga68b73c03a5098a21260b5c3638edc973)

int usbc\_suspend(const struct device \*dev)

Suspend the USB-C Subsystem.

[usbc\_set\_policy\_cb\_get\_src\_caps](group____usbc__device__api.md#ga7800c065ae5cfb7a95b58865d47c7f04)

void usbc\_set\_policy\_cb\_get\_src\_caps(const struct device \*dev, const policy\_cb\_get\_src\_caps\_t cb)

Set the callback used to get the Source Capabilities from the Device Policy Manager.

[usbc\_set\_policy\_cb\_get\_rdo](group____usbc__device__api.md#ga7c1ffea81f71416ab2942fc5a5b67d41)

void usbc\_set\_policy\_cb\_get\_rdo(const struct device \*dev, const policy\_cb\_get\_rdo\_t cb)

Set the callback used to get the Request Data Object (RDO).

[usbc\_set\_policy\_cb\_check\_sink\_request](group____usbc__device__api.md#ga7f85188cc4f1a95350195abd0d736ada)

void usbc\_set\_policy\_cb\_check\_sink\_request(const struct device \*dev, const policy\_cb\_check\_sink\_request\_t cb)

Set the callback used to check if Sink request is valid.

[usbc\_set\_vconn\_discharge\_cb](group____usbc__device__api.md#ga8741df33b5432d9c7d5902af9bd67084)

void usbc\_set\_vconn\_discharge\_cb(const struct device \*dev, const tcpc\_vconn\_discharge\_cb\_t cb)

Set the callback used to discharge VCONN.

[usbc\_set\_policy\_cb\_get\_src\_rp](group____usbc__device__api.md#ga8974f9661dfebf8f686d677f999d5957)

void usbc\_set\_policy\_cb\_get\_src\_rp(const struct device \*dev, const policy\_cb\_get\_src\_rp\_t cb)

Set the callback used to get the Rp value that should be placed on the CC lines.

[usbc\_set\_vconn\_control\_cb](group____usbc__device__api.md#ga9846b36061453023e16c160f5f120159)

void usbc\_set\_vconn\_control\_cb(const struct device \*dev, const tcpc\_vconn\_control\_cb\_t cb)

Set the callback used to set VCONN control.

[usbc\_set\_dpm\_data](group____usbc__device__api.md#ga997007cab2e54ad53b774b4215d0f593)

void usbc\_set\_dpm\_data(const struct device \*dev, void \*dpm\_data)

Set pointer to Device Policy Manager (DPM) data.

[usbc\_set\_policy\_cb\_wait\_notify](group____usbc__device__api.md#gaa295593c7d5ede31328efaaab38b5880)

void usbc\_set\_policy\_cb\_wait\_notify(const struct device \*dev, const policy\_cb\_wait\_notify\_t cb)

Set the callback used to notify Device Policy Manager of WAIT message reception.

[usbc\_set\_policy\_cb\_change\_src\_caps](group____usbc__device__api.md#gaa8f89bfb1e9a1840b2d61ebaa13aeb2f)

void usbc\_set\_policy\_cb\_change\_src\_caps(const struct device \*dev, const policy\_cb\_change\_src\_caps\_t cb)

Set the callback used to request that a different set of Source Caps be sent to the Sink.

[usbc\_get\_dpm\_data](group____usbc__device__api.md#gabd99b6926baf67212d65c4a4d147ce5b)

void \* usbc\_get\_dpm\_data(const struct device \*dev)

Get pointer to Device Policy Manager (DPM) data.

[usbc\_policy\_wait\_t](group____usbc__device__api.md#gadf5d2934b5dc8e2b01d20bb904988784)

usbc\_policy\_wait\_t

Device Policy Manager Wait message notifications.

**Definition** usbc.h:151

[usbc\_set\_policy\_cb\_notify](group____usbc__device__api.md#gaedec1b4ad7b028ad18e1bcbe5396f1ee)

void usbc\_set\_policy\_cb\_notify(const struct device \*dev, const policy\_cb\_notify\_t cb)

Set the callback used to notify Device Policy Manager of a policy change.

[usbc\_set\_policy\_cb\_is\_ps\_ready](group____usbc__device__api.md#gaf25c9cc2b6c514b9dcddc8129a76ccee)

void usbc\_set\_policy\_cb\_is\_ps\_ready(const struct device \*dev, const policy\_cb\_is\_ps\_ready\_t cb)

Set the callback used to check if Source Power Supply is ready.

[usbc\_set\_policy\_cb\_src\_en](group____usbc__device__api.md#gaf5332ba0c87ff737e1c476d7be071fec)

void usbc\_set\_policy\_cb\_src\_en(const struct device \*dev, const policy\_cb\_src\_en\_t cb)

Set the callback used to enable VBUS.

[usbc\_set\_policy\_cb\_get\_snk\_cap](group____usbc__device__api.md#gafbd2885d758aa869635041fa89750596)

void usbc\_set\_policy\_cb\_get\_snk\_cap(const struct device \*dev, const policy\_cb\_get\_snk\_cap\_t cb)

Set the callback used to get the Sink Capabilities.

[usbc\_set\_policy\_cb\_set\_port\_partner\_snk\_cap](group____usbc__device__api.md#gafd0a407558bb92dc8b7007d9d717b940)

void usbc\_set\_policy\_cb\_set\_port\_partner\_snk\_cap(const struct device \*dev, const policy\_cb\_set\_port\_partner\_snk\_cap\_t cb)

Set the callback used to store the Capabilities received from a Sink Port Partner.

[usbc\_policy\_check\_t](group____usbc__device__api.md#gafea882f4f3cc96c502d53a24a3e5aec5)

usbc\_policy\_check\_t

Device Policy Manager checks.

**Definition** usbc.h:133

[usbc\_set\_policy\_cb\_is\_snk\_at\_default](group____usbc__device__api.md#gaffa045ee6e2fbc07fde7e84e44d3853f)

void usbc\_set\_policy\_cb\_is\_snk\_at\_default(const struct device \*dev, const policy\_cb\_is\_snk\_at\_default\_t cb)

Set the callback used to check if the sink power supply is at the default level.

[REQUEST\_TC\_END](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a0c5ff3bc4c0d6f636663fd3911ed85d5)

@ REQUEST\_TC\_END

End of Type-C requests.

**Definition** usbc.h:61

[REQUEST\_PE\_DR\_SWAP](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a1fe9f57fac7f5149fe5f0f7c42523536)

@ REQUEST\_PE\_DR\_SWAP

Request Policy Engine layer to perform a Data Role Swap.

**Definition** usbc.h:64

[REQUEST\_NOP](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a2274197ac367b3da6358cac8dd781134)

@ REQUEST\_NOP

No request.

**Definition** usbc.h:55

[REQUEST\_PE\_HARD\_RESET\_SEND](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a7c3c9c959439ee73539cff13e561c403)

@ REQUEST\_PE\_HARD\_RESET\_SEND

Request Policy Engine layer to send a hard reset.

**Definition** usbc.h:66

[REQUEST\_TC\_DISABLED](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a899633a1b63b1c3a826b5556f0f23d8b)

@ REQUEST\_TC\_DISABLED

Request Type-C layer to transition to Disabled State.

**Definition** usbc.h:57

[REQUEST\_TC\_ERROR\_RECOVERY](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a8a7b77d81428f0c4784af3204f33b290)

@ REQUEST\_TC\_ERROR\_RECOVERY

Request Type-C layer to transition to Error Recovery State.

**Definition** usbc.h:59

[REQUEST\_PE\_GET\_SRC\_CAPS](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a8c6083028ee8655cd0bebb6d9aab2e1e)

@ REQUEST\_PE\_GET\_SRC\_CAPS

Request Policy Engine layer to get Source Capabilities from port partner.

**Definition** usbc.h:73

[REQUEST\_PE\_SOFT\_RESET\_SEND](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3ad45120b1ceabeb054c2c2273b8431894)

@ REQUEST\_PE\_SOFT\_RESET\_SEND

Request Policy Engine layer to send a soft reset.

**Definition** usbc.h:68

[REQUEST\_GET\_SNK\_CAPS](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3ade1edc3aef0e4d563934edbc9ce784bc)

@ REQUEST\_GET\_SNK\_CAPS

Request Policy Engine to get Sink Capabilities from port partner.

**Definition** usbc.h:78

[REQUEST\_PE\_GOTO\_MIN](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3ae5b4eb0db00e81a98cfe2436b64a7018)

@ REQUEST\_PE\_GOTO\_MIN

Request Policy Engine to request the port partner to source minimum power.

**Definition** usbc.h:83

[SNK\_REQUEST\_REJECT](group____usbc__device__api.md#gga4c4f0592a034b4e49eee85e95af33f94a714f82e830f9528a8200c2c14795b282)

@ SNK\_REQUEST\_REJECT

The sink port partner's request can not be met.

**Definition** usbc.h:169

[SNK\_REQUEST\_VALID](group____usbc__device__api.md#gga4c4f0592a034b4e49eee85e95af33f94a7922edb67afe83596819994a71de76dd)

@ SNK\_REQUEST\_VALID

The sink port partner's request can be met.

**Definition** usbc.h:167

[SNK\_REQUEST\_WAIT](group____usbc__device__api.md#gga4c4f0592a034b4e49eee85e95af33f94a7ae46f6deb593eedd0564d30cb4c75fb)

@ SNK\_REQUEST\_WAIT

The sink port partner's request can be met at a later time.

**Definition** usbc.h:171

[SOURCE\_CAPABILITIES\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a0266a21d8c836cf281c30542eb6badd4)

@ SOURCE\_CAPABILITIES\_RECEIVED

Source Capabilities Received.

**Definition** usbc.h:127

[POWER\_CHANGE\_0A0](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a0fb0676a11ad8bad2d5249031ba5fd19)

@ POWER\_CHANGE\_0A0

Sink SubPower state at 0V.

**Definition** usbc.h:117

[POWER\_CHANGE\_1A5](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a336bfb983c4d07684d67d4d9ef6c1489)

@ POWER\_CHANGE\_1A5

Sink SubPower state a 5V / 1.5A.

**Definition** usbc.h:121

[POWER\_CHANGE\_3A0](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a3477c1c6ad8885c3ab7a9c58b7399dcf)

@ POWER\_CHANGE\_3A0

Sink SubPower state a 5V / 3A.

**Definition** usbc.h:123

[TRANSITION\_PS](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a3a27b8e70ffe5788aa3ffea1bf61cae9)

@ TRANSITION\_PS

Transition the Power Supply.

**Definition** usbc.h:107

[POWER\_CHANGE\_DEF](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a3a50be6f70c1a7abd724ab447491c46a)

@ POWER\_CHANGE\_DEF

Sink SubPower state a 5V / 500mA.

**Definition** usbc.h:119

[DATA\_ROLE\_IS\_UFP](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a4020203569dcb95ab1b3d2946efced19)

@ DATA\_ROLE\_IS\_UFP

Data Role has been set to Upstream Facing Port (UFP).

**Definition** usbc.h:99

[MSG\_ACCEPT\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a43bc56906b5dc4767d3297400053d286)

@ MSG\_ACCEPT\_RECEIVED

Power Delivery Accept message was received.

**Definition** usbc.h:91

[MSG\_REJECTED\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a4ad0620e76c694004d3a1b43458a14b2)

@ MSG\_REJECTED\_RECEIVED

Power Delivery Reject message was received.

**Definition** usbc.h:93

[DATA\_ROLE\_IS\_DFP](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a791604f4f0b2a2c3ccea4e98d1659a61)

@ DATA\_ROLE\_IS\_DFP

Data Role has been set to Downstream Facing Port (DFP).

**Definition** usbc.h:101

[PROTOCOL\_ERROR](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a8cb937247ec21f791706f4f426496a8c)

@ PROTOCOL\_ERROR

Protocol Error occurred.

**Definition** usbc.h:111

[SNK\_TRANSITION\_TO\_DEFAULT](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23aa02158d0afdd60c755453977200dfb28)

@ SNK\_TRANSITION\_TO\_DEFAULT

Transition the Sink to default.

**Definition** usbc.h:113

[MSG\_DISCARDED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23aa316636e8353dad1a9d5dec8b85a67e4)

@ MSG\_DISCARDED

Power Delivery discarded the message being transmitted.

**Definition** usbc.h:95

[MSG\_NOT\_SUPPORTED\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ab2f97ffaa13c84e656f7ac0004ec86ae)

@ MSG\_NOT\_SUPPORTED\_RECEIVED

Power Delivery Not Supported message was received.

**Definition** usbc.h:97

[HARD\_RESET\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ab74f5bcaa94a5fb1e46cdd7c6a5d822f)

@ HARD\_RESET\_RECEIVED

Hard Reset Received.

**Definition** usbc.h:115

[SENDER\_RESPONSE\_TIMEOUT](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ac22b0026881f65c574d0bf7454321745)

@ SENDER\_RESPONSE\_TIMEOUT

Sender Response Timeout.

**Definition** usbc.h:125

[PORT\_PARTNER\_NOT\_RESPONSIVE](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ad52e1c4f949bb64fef1d996ac2f4e0de)

@ PORT\_PARTNER\_NOT\_RESPONSIVE

Port partner is not responsive.

**Definition** usbc.h:109

[PD\_CONNECTED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23adbefad204068244fdf75ba1ff211fbfc)

@ PD\_CONNECTED

A PD Explicit Contract is in place.

**Definition** usbc.h:103

[NOT\_PD\_CONNECTED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23adebcbf5155b43ce562127d4077d46d7d)

@ NOT\_PD\_CONNECTED

No PD Explicit Contract is in place.

**Definition** usbc.h:105

[WAIT\_SINK\_REQUEST](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784a009ce2ceacd92db88d9a6beb01f84a28)

@ WAIT\_SINK\_REQUEST

The port partner is unable to meet the sink request at this time.

**Definition** usbc.h:153

[WAIT\_POWER\_ROLE\_SWAP](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784a91f1f41bf9318e06c02c1957a39a762a)

@ WAIT\_POWER\_ROLE\_SWAP

The port partner is unable to do a Power Role Swap at this time.

**Definition** usbc.h:155

[WAIT\_VCONN\_SWAP](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784aa982aed81f39e35cde74399c6d74e601)

@ WAIT\_VCONN\_SWAP

The port partner is unable to do a VCONN Swap at this time.

**Definition** usbc.h:159

[WAIT\_DATA\_ROLE\_SWAP](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784ae5ef03f78d78a7014404c581bad77c18)

@ WAIT\_DATA\_ROLE\_SWAP

The port partner is unable to do a Data Role Swap at this time.

**Definition** usbc.h:157

[CHECK\_POWER\_ROLE\_SWAP](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a1181a470497b797136cf0eb204394106)

@ CHECK\_POWER\_ROLE\_SWAP

Check if Power Role Swap is allowed.

**Definition** usbc.h:135

[CHECK\_SNK\_AT\_DEFAULT\_LEVEL](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a17f7f4fc9aa4178f0358769dedd29ade)

@ CHECK\_SNK\_AT\_DEFAULT\_LEVEL

Check if Sink is at default level.

**Definition** usbc.h:141

[CHECK\_SRC\_PS\_AT\_DEFAULT\_LEVEL](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a42b660bb630edcca5ae8b031033d0718)

@ CHECK\_SRC\_PS\_AT\_DEFAULT\_LEVEL

Check if Source Power Supply is at default level.

**Definition** usbc.h:145

[CHECK\_VCONN\_CONTROL](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a655e913c86db5caa961083dad9f6b7a1)

@ CHECK\_VCONN\_CONTROL

Check if should control VCONN.

**Definition** usbc.h:143

[CHECK\_DATA\_ROLE\_SWAP\_TO\_UFP](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a7c97208a8a12f70e7ffa43bb406b9ebd)

@ CHECK\_DATA\_ROLE\_SWAP\_TO\_UFP

Check if Data Role Swap to UFP is allowed.

**Definition** usbc.h:139

[CHECK\_DATA\_ROLE\_SWAP\_TO\_DFP](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5afa602e00bf418656e365baa4d9ff6cef)

@ CHECK\_DATA\_ROLE\_SWAP\_TO\_DFP

Check if Data Role Swap to DFP is allowed.

**Definition** usbc.h:137

[policy\_cb\_is\_snk\_at\_default\_t](group__sink__callbacks.md#ga1a3da6faad509213f607893fef16b673)

bool(\* policy\_cb\_is\_snk\_at\_default\_t)(const struct device \*dev)

Callback type used to check if the sink power supply is at the default level.

**Definition** usbc.h:243

[policy\_cb\_check\_t](group__sink__callbacks.md#ga2aacd704d08a8cecbf818150e8ec51b6)

bool(\* policy\_cb\_check\_t)(const struct device \*dev, const enum usbc\_policy\_check\_t policy\_check)

Callback type used to check a policy.

**Definition** usbc.h:204

[policy\_cb\_notify\_t](group__sink__callbacks.md#ga44af668d9c22e757983c803d7b8ff82e)

void(\* policy\_cb\_notify\_t)(const struct device \*dev, const enum usbc\_policy\_notify\_t policy\_notify)

Callback type used to notify Device Policy Manager of a policy change.

**Definition** usbc.h:225

[policy\_cb\_set\_src\_cap\_t](group__sink__callbacks.md#ga6096d6909698f1b86a1a9cbd1f8d4097)

void(\* policy\_cb\_set\_src\_cap\_t)(const struct device \*dev, const uint32\_t \*pdos, const int num\_pdos)

Callback type used to report the received Port Partner's Source Capabilities.

**Definition** usbc.h:194

[policy\_cb\_get\_snk\_cap\_t](group__sink__callbacks.md#gaaed0161142c3481ce9180015b6968357)

int(\* policy\_cb\_get\_snk\_cap\_t)(const struct device \*dev, uint32\_t \*\*pdos, int \*num\_pdos)

Callback type used to get the Sink Capabilities.

**Definition** usbc.h:185

[policy\_cb\_get\_rdo\_t](group__sink__callbacks.md#gae0448c6b271273c5db59775c3a6260dc)

uint32\_t(\* policy\_cb\_get\_rdo\_t)(const struct device \*dev)

Callback type used to get the Request Data Object (RDO).

**Definition** usbc.h:234

[policy\_cb\_wait\_notify\_t](group__sink__callbacks.md#gaea62016b263dfaf5f869dd6ea036fdad)

bool(\* policy\_cb\_wait\_notify\_t)(const struct device \*dev, const enum usbc\_policy\_wait\_t wait\_notify)

Callback type used to notify Device Policy Manager of WAIT message reception.

**Definition** usbc.h:215

[policy\_cb\_present\_contract\_is\_valid\_t](group__source__callbacks.md#ga2925e462140a700920251d92ae5a3aa4)

bool(\* policy\_cb\_present\_contract\_is\_valid\_t)(const struct device \*dev, const uint32\_t present\_contract)

Callback type used to check if present Contract is still valid.

**Definition** usbc.h:286

[policy\_cb\_get\_src\_caps\_t](group__source__callbacks.md#ga4bbf78bd752d38d915412dd942d3aab8)

int(\* policy\_cb\_get\_src\_caps\_t)(const struct device \*dev, const uint32\_t \*\*pdos, uint32\_t \*num\_pdos)

Callback type used to get the Source Capabilities from the Device Policy Manager.

**Definition** usbc.h:258

[policy\_cb\_change\_src\_caps\_t](group__source__callbacks.md#ga699811c862990b31ec0126dd3a4c3e4d)

bool(\* policy\_cb\_change\_src\_caps\_t)(const struct device \*dev)

Callback type used to request that a different set of Source Caps be sent to the Sink.

**Definition** usbc.h:296

[policy\_cb\_get\_src\_rp\_t](group__source__callbacks.md#ga7c75f8192001179f20bf1fe48316f3c6)

int(\* policy\_cb\_get\_src\_rp\_t)(const struct device \*dev, enum tc\_rp\_value \*rp)

Callback type used to get the Rp value that should be placed on the CC lines.

**Definition** usbc.h:316

[policy\_cb\_src\_en\_t](group__source__callbacks.md#gaaecac7683d7092c0a477e8d9ca0e5a33)

int(\* policy\_cb\_src\_en\_t)(const struct device \*dev, bool en)

Callback type used to enable VBUS.

**Definition** usbc.h:324

[policy\_cb\_is\_ps\_ready\_t](group__source__callbacks.md#gae7391e858485e44a74e5fcdbb7931ca7)

bool(\* policy\_cb\_is\_ps\_ready\_t)(const struct device \*dev)

Callback type used to check if Source Power Supply is ready.

**Definition** usbc.h:277

[policy\_cb\_set\_port\_partner\_snk\_cap\_t](group__source__callbacks.md#gae903c8108e8d1563cb0b1ccdd901c925)

void(\* policy\_cb\_set\_port\_partner\_snk\_cap\_t)(const struct device \*dev, const uint32\_t \*pdos, const int num\_pdos)

Callback type used to report the Capabilities received from a Sink Port Partner.

**Definition** usbc.h:306

[policy\_cb\_check\_sink\_request\_t](group__source__callbacks.md#gaeeda677224456f685137e4b345c0e173)

enum usbc\_snk\_req\_reply\_t(\* policy\_cb\_check\_sink\_request\_t)(const struct device \*dev, const uint32\_t request\_msg)

Callback type used to check if Sink request is valid.

**Definition** usbc.h:268

[tcpc\_vconn\_discharge\_cb\_t](group__usb__type__c__port__controller__api.md#ga4437e66605f988be1e16c52b9912e9c2)

int(\* tcpc\_vconn\_discharge\_cb\_t)(const struct device \*dev, enum tc\_cc\_polarity pol, bool enable)

**Definition** usbc\_tcpc.h:123

[tcpc\_vconn\_control\_cb\_t](group__usb__type__c__port__controller__api.md#ga7a989ffd6bdc83696188de59acbd49c7)

int(\* tcpc\_vconn\_control\_cb\_t)(const struct device \*dev, enum tc\_cc\_polarity pol, bool enable)

**Definition** usbc\_tcpc.h:121

[tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5)

tc\_rp\_value

Pull-Up resistor values.

**Definition** usbc\_tc.h:338

[types.h](include_2zephyr_2types_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[usbc\_tcpc.h](usbc__tcpc_8h.md)

USBC Type-C Port Controller device APIs.

[usbc\_vbus.h](usbc__vbus_8h.md)

USB-C VBUS device APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb\_c](dir_29299904d896cedab2c4945a0291e19f.md)
- [usbc.h](usbc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
