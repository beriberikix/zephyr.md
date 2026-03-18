---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/tee_8h_source.html
original_path: doxygen/html/tee_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tee.h

[Go to the documentation of this file.](tee_8h.md)

1/\*

2 \* Copyright (c) 2023 EPAM Systems

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13/\*

14 \* Copyright (c) 2015-2016, Linaro Limited

15 \* All rights reserved.

16 \*

17 \* Redistribution and use in source and binary forms, with or without

18 \* modification, are permitted provided that the following conditions are met:

19 \*

20 \* 1. Redistributions of source code must retain the above copyright notice,

21 \* this list of conditions and the following disclaimer.

22 \*

23 \* 2. Redistributions in binary form must reproduce the above copyright notice,

24 \* this list of conditions and the following disclaimer in the documentation

25 \* and/or other materials provided with the distribution.

26 \*

27 \* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"

28 \* AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE

29 \* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE

30 \* ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE

31 \* LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR

32 \* CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF

33 \* SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS

34 \* INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN

35 \* CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)

36 \* ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE

37 \* POSSIBILITY OF SUCH DAMAGE.

38 \*/

39#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_TEE\_H\_

40#define ZEPHYR\_INCLUDE\_DRIVERS\_TEE\_H\_

41

42#include <[zephyr/device.h](device_8h.md)>

43#include <[zephyr/kernel.h](kernel_8h.md)>

44#include <[zephyr/sys/util.h](util_8h.md)>

45

68

69#ifdef \_\_cplusplus

70extern "C" {

71#endif

[ 72](group__tee__interface.md#ga79ff2ca70757daf8e677b42002f4aeac)#define TEE\_UUID\_LEN 16

73

[ 74](group__tee__interface.md#ga2eb5a95c2f50e08bbb6235fa47253f10)#define TEE\_GEN\_CAP\_GP BIT(0) /\* GlobalPlatform compliant TEE \*/

[ 75](group__tee__interface.md#ga15e96022b209b84d29c29f213aab0331)#define TEE\_GEN\_CAP\_PRIVILEGED BIT(1) /\* Privileged device (for supplicant) \*/

[ 76](group__tee__interface.md#gae661041c8b0f0638891a5a82b74aa928)#define TEE\_GEN\_CAP\_REG\_MEM BIT(2) /\* Supports registering shared memory \*/

[ 77](group__tee__interface.md#ga4cd66a4425e312338823061e561638de)#define TEE\_GEN\_CAP\_MEMREF\_NULL BIT(3) /\* Support NULL MemRef \*/

78

[ 79](group__tee__interface.md#ga2fac25b74105b1ddfb15db51598b89c8)#define TEE\_SHM\_REGISTER BIT(0)

[ 80](group__tee__interface.md#ga85fd3e6e6b596da02c97661a35c9814c)#define TEE\_SHM\_ALLOC BIT(1)

81

[ 82](group__tee__interface.md#gad3f8bf86812e0e5befa873389235ddd9)#define TEE\_PARAM\_ATTR\_TYPE\_NONE 0 /\* parameter not used \*/

[ 83](group__tee__interface.md#ga5304d0bdbfb80563bdf3bd801cc72613)#define TEE\_PARAM\_ATTR\_TYPE\_VALUE\_INPUT 1

[ 84](group__tee__interface.md#gaf66e35aefb70c34cba93eeb5f3cb0f8a)#define TEE\_PARAM\_ATTR\_TYPE\_VALUE\_OUTPUT 2

[ 85](group__tee__interface.md#ga925026258aed48470a015a655f25b270)#define TEE\_PARAM\_ATTR\_TYPE\_VALUE\_INOUT 3 /\* input and output \*/

[ 86](group__tee__interface.md#ga0c7f0c79fd599a2d5ec2759230bff6e7)#define TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_INPUT 5

[ 87](group__tee__interface.md#ga5305a53edb649a22c774731bf2f53987)#define TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_OUTPUT 6

[ 88](group__tee__interface.md#ga43fcdc052991d21fc7fde3720256ef2c)#define TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_INOUT 7 /\* input and output \*/

[ 89](group__tee__interface.md#ga8e2dca32129d730d9394f0798d578ce7)#define TEE\_PARAM\_ATTR\_TYPE\_MASK 0xff

[ 90](group__tee__interface.md#ga42e96de713673837d60ac3b938373206)#define TEE\_PARAM\_ATTR\_META 0x100

[ 91](group__tee__interface.md#ga15358e8f86ca9a2b6aca9899ee982542)#define TEE\_PARAM\_ATTR\_MASK (TEE\_PARAM\_ATTR\_TYPE\_MASK | TEE\_PARAM\_ATTR\_META)

92

[ 106](group__tee__interface.md#ga6040bf64a72a13c675681c99112f7f69)#define TEEC\_ORIGIN\_API 0x00000001

[ 107](group__tee__interface.md#ga668c5799e8360e3e885a908784805578)#define TEEC\_ORIGIN\_COMMS 0x00000002

[ 108](group__tee__interface.md#gabebf4008dbbf440ac352d510675c9433)#define TEEC\_ORIGIN\_TEE 0x00000003

[ 109](group__tee__interface.md#gaebb73e90a25eeecc5ac274c2c396f32f)#define TEEC\_ORIGIN\_TRUSTED\_APP 0x00000004

110

139

[ 143](group__tee__interface.md#gae000299e1a48b8e9c807c8e1b7e62aed)#define TEEC\_SUCCESS 0x00000000

[ 144](group__tee__interface.md#gad9e7d08ba6637d86cf611952b9842568)#define TEEC\_ERROR\_STORAGE\_NOT\_AVAILABLE 0xF0100003

[ 145](group__tee__interface.md#ga13c7ed6f37eba36870e4b138b661b61f)#define TEEC\_ERROR\_GENERIC 0xFFFF0000

[ 146](group__tee__interface.md#gad7c7cd2ed537347d60276bd08375ca30)#define TEEC\_ERROR\_ACCESS\_DENIED 0xFFFF0001

[ 147](group__tee__interface.md#ga8cbe25a679add519a048c85c03be1ede)#define TEEC\_ERROR\_CANCEL 0xFFFF0002

[ 148](group__tee__interface.md#ga65a8bd0582ef42f84e85704bab5a85fe)#define TEEC\_ERROR\_ACCESS\_CONFLICT 0xFFFF0003

[ 149](group__tee__interface.md#gad8825a36962871ac2006386d18a821e7)#define TEEC\_ERROR\_EXCESS\_DATA 0xFFFF0004

[ 150](group__tee__interface.md#ga0e08a22cf7abe05ae2d0cfd7fe92b0e7)#define TEEC\_ERROR\_BAD\_FORMAT 0xFFFF0005

[ 151](group__tee__interface.md#ga79b607eb603bef58b3065a3014ee7117)#define TEEC\_ERROR\_BAD\_PARAMETERS 0xFFFF0006

[ 152](group__tee__interface.md#ga19c6e3eb278dd58fa49b7de3dff8b7ac)#define TEEC\_ERROR\_BAD\_STATE 0xFFFF0007

[ 153](group__tee__interface.md#ga805299b26fda6bb38a97cf6a0825431d)#define TEEC\_ERROR\_ITEM\_NOT\_FOUND 0xFFFF0008

[ 154](group__tee__interface.md#gaa7ef60306699f14fa7f3bcd6ed744633)#define TEEC\_ERROR\_NOT\_IMPLEMENTED 0xFFFF0009

[ 155](group__tee__interface.md#ga17041726bc43fb2a1aa3ddc927ac6cef)#define TEEC\_ERROR\_NOT\_SUPPORTED 0xFFFF000A

[ 156](group__tee__interface.md#gaf515dfd970be2caf575be186dd32afd7)#define TEEC\_ERROR\_NO\_DATA 0xFFFF000B

[ 157](group__tee__interface.md#gac7aaf1249147ecd63d6fba179e26ad33)#define TEEC\_ERROR\_OUT\_OF\_MEMORY 0xFFFF000C

[ 158](group__tee__interface.md#ga28d244820db7caa7cb829ed3469f5961)#define TEEC\_ERROR\_BUSY 0xFFFF000D

[ 159](group__tee__interface.md#ga0a3047b67556c437e80c308853705de2)#define TEEC\_ERROR\_COMMUNICATION 0xFFFF000E

[ 160](group__tee__interface.md#gaae2b6bb8d476d422f782e7ac226de21b)#define TEEC\_ERROR\_SECURITY 0xFFFF000F

[ 161](group__tee__interface.md#ga511a0747fab1c307a5263a07ce396962)#define TEEC\_ERROR\_SHORT\_BUFFER 0xFFFF0010

[ 162](group__tee__interface.md#ga10e9a718e8ce09e6fe117bc0b002a3d6)#define TEEC\_ERROR\_EXTERNAL\_CANCEL 0xFFFF0011

[ 163](group__tee__interface.md#ga6aa8da2d81b77fb8d2ec16f4e3a27528)#define TEEC\_ERROR\_TARGET\_DEAD 0xFFFF3024

[ 164](group__tee__interface.md#ga6229f84eb575bf10c14b40f02495b46e)#define TEEC\_ERROR\_STORAGE\_NO\_SPACE 0xFFFF3041

165

[ 182](group__tee__interface.md#ga16baa8eb95393514c6035c957ad55a6b)#define TEEC\_LOGIN\_PUBLIC 0x00000000

[ 183](group__tee__interface.md#gab6940dd1f636aa67e74a8615e8544f85)#define TEEC\_LOGIN\_USER 0x00000001

[ 184](group__tee__interface.md#ga8cdd4a2102e18a60d0624d610ef3619e)#define TEEC\_LOGIN\_GROUP 0x00000002

[ 185](group__tee__interface.md#gae803496f14c6cc84b7f56174006c16a6)#define TEEC\_LOGIN\_APPLICATION 0x00000004

[ 186](group__tee__interface.md#ga37fbb624e8c289d400cd69948bf8b505)#define TEEC\_LOGIN\_USER\_APPLICATION 0x00000005

[ 187](group__tee__interface.md#gad1da184306fe0283fc1e618f829119e3)#define TEEC\_LOGIN\_GROUP\_APPLICATION 0x00000006

188

[ 196](structtee__version__info.md)struct [tee\_version\_info](structtee__version__info.md) {

[ 197](structtee__version__info.md#aaf74a1ff5fb899a0675724669a7d7e36) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [impl\_id](structtee__version__info.md#aaf74a1ff5fb899a0675724669a7d7e36);

[ 198](structtee__version__info.md#a6cbf12676e5cfc1bdf4221a8188bf055) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [impl\_caps](structtee__version__info.md#a6cbf12676e5cfc1bdf4221a8188bf055);

[ 199](structtee__version__info.md#a56a3c50a69f125428dfbf7a867cb7177) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gen\_caps](structtee__version__info.md#a56a3c50a69f125428dfbf7a867cb7177);

200};

201

[ 205](structtee__open__session__arg.md)struct [tee\_open\_session\_arg](structtee__open__session__arg.md) {

[ 206](structtee__open__session__arg.md#a9f4c56fe45f5ad9313bdc1f457d31f9a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](structtee__open__session__arg.md#a9f4c56fe45f5ad9313bdc1f457d31f9a)[[TEE\_UUID\_LEN](group__tee__interface.md#ga79ff2ca70757daf8e677b42002f4aeac)];

[ 207](structtee__open__session__arg.md#aff38cc02e83936e23965ee2e4e44ff26) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clnt\_uuid](structtee__open__session__arg.md#aff38cc02e83936e23965ee2e4e44ff26)[[TEE\_UUID\_LEN](group__tee__interface.md#ga79ff2ca70757daf8e677b42002f4aeac)];

[ 208](structtee__open__session__arg.md#a226c617eae1b959025a0232eed48aa41) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clnt\_login](structtee__open__session__arg.md#a226c617eae1b959025a0232eed48aa41);

[ 209](structtee__open__session__arg.md#adf8bfaaf5059de617a7139b5f06a0ac6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cancel\_id](structtee__open__session__arg.md#adf8bfaaf5059de617a7139b5f06a0ac6);

[ 210](structtee__open__session__arg.md#a5e28bb77990ce6d050a57daa419760e1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [session](structtee__open__session__arg.md#a5e28bb77990ce6d050a57daa419760e1);

[ 211](structtee__open__session__arg.md#a3be6d6ea6aeff1a8f27051fe30f21347) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ret](structtee__open__session__arg.md#a3be6d6ea6aeff1a8f27051fe30f21347);

[ 212](structtee__open__session__arg.md#a73a7e82fb0b589eed327ab8f4217e6fc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ret\_origin](structtee__open__session__arg.md#a73a7e82fb0b589eed327ab8f4217e6fc);

213};

214

[ 229](structtee__param.md)struct [tee\_param](structtee__param.md) {

[ 230](structtee__param.md#ac8ced719ce993735e22d68ca50f54e5b) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [attr](structtee__param.md#ac8ced719ce993735e22d68ca50f54e5b);

[ 231](structtee__param.md#aea8916d1bc24ab5a56f59fa4608f1a38) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [a](structtee__param.md#aea8916d1bc24ab5a56f59fa4608f1a38);

[ 232](structtee__param.md#a22785fe00950c3a7d6353c39b12d72a8) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [b](structtee__param.md#a22785fe00950c3a7d6353c39b12d72a8);

[ 233](structtee__param.md#a79b39571785949e32629216742e34d72) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [c](structtee__param.md#a79b39571785949e32629216742e34d72);

234};

235

[ 239](structtee__invoke__func__arg.md)struct [tee\_invoke\_func\_arg](structtee__invoke__func__arg.md) {

[ 240](structtee__invoke__func__arg.md#a17aa094ca0a6c6d9a72d2fae9c0c66ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [func](structtee__invoke__func__arg.md#a17aa094ca0a6c6d9a72d2fae9c0c66ef);

[ 241](structtee__invoke__func__arg.md#af110327354b1ca48dedf22855c3a7afc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [session](structtee__invoke__func__arg.md#af110327354b1ca48dedf22855c3a7afc);

[ 242](structtee__invoke__func__arg.md#a457daf2221f9520aecb42667acc4ccd1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cancel\_id](structtee__invoke__func__arg.md#a457daf2221f9520aecb42667acc4ccd1);

[ 243](structtee__invoke__func__arg.md#af63bd284a7397d4086ac17f83d6b1e93) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ret](structtee__invoke__func__arg.md#af63bd284a7397d4086ac17f83d6b1e93);

[ 244](structtee__invoke__func__arg.md#ae806e940e463321b3de31bad2e05bf60) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ret\_origin](structtee__invoke__func__arg.md#ae806e940e463321b3de31bad2e05bf60);

245};

246

[ 250](structtee__shm.md)struct [tee\_shm](structtee__shm.md) {

[ 251](structtee__shm.md#ab761c1d3d5e64c21725eff97521b4b86) const struct [device](structdevice.md) \*[dev](structtee__shm.md#ab761c1d3d5e64c21725eff97521b4b86);

[ 252](structtee__shm.md#a65446310f73319aa5f8e100e4d83198e) void \*[addr](structtee__shm.md#a65446310f73319aa5f8e100e4d83198e);

[ 253](structtee__shm.md#a02fe0fd69f1e8d5650cfa116136ea9ca) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [size](structtee__shm.md#a02fe0fd69f1e8d5650cfa116136ea9ca);

[ 254](structtee__shm.md#ac2738d87cbe439f093cad67a375c2807) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structtee__shm.md#ac2738d87cbe439f093cad67a375c2807);

255};

256

[ 264](group__tee__interface.md#gac533d9e85d65857c0d984506024a55b4)typedef int (\*[tee\_get\_version\_t](group__tee__interface.md#gac533d9e85d65857c0d984506024a55b4))(const struct [device](structdevice.md) \*dev, struct [tee\_version\_info](structtee__version__info.md) \*info);

265

[ 273](group__tee__interface.md#gaf972199fcdbd892688dc141ddba6e6aa)typedef int (\*[tee\_open\_session\_t](group__tee__interface.md#gaf972199fcdbd892688dc141ddba6e6aa))(const struct [device](structdevice.md) \*dev, struct [tee\_open\_session\_arg](structtee__open__session__arg.md) \*arg,

274 unsigned int num\_param, struct [tee\_param](structtee__param.md) \*param,

275 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*session\_id);

[ 283](group__tee__interface.md#gac412f57a3da187e6e272857d5bdaaaeb)typedef int (\*[tee\_close\_session\_t](group__tee__interface.md#gac412f57a3da187e6e272857d5bdaaaeb))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id);

284

[ 292](group__tee__interface.md#gad4cd5b65cac3eb7b4338fd99eeb13a93)typedef int (\*[tee\_cancel\_t](group__tee__interface.md#gad4cd5b65cac3eb7b4338fd99eeb13a93))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cancel\_id);

293

[ 301](group__tee__interface.md#gac3695e51dc8b08bb5e5c5d984c402b0e)typedef int (\*[tee\_invoke\_func\_t](group__tee__interface.md#gac3695e51dc8b08bb5e5c5d984c402b0e))(const struct [device](structdevice.md) \*dev, struct [tee\_invoke\_func\_arg](structtee__invoke__func__arg.md) \*arg,

302 unsigned int num\_param, struct [tee\_param](structtee__param.md) \*param);

[ 310](group__tee__interface.md#ga9e2807d34d580c012129a2fc1f5a425a)typedef int (\*[tee\_shm\_register\_t](group__tee__interface.md#ga9e2807d34d580c012129a2fc1f5a425a))(const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm);

311

[ 319](group__tee__interface.md#ga2ea18e713a101a6ca715baa04c2f4185)typedef int (\*[tee\_shm\_unregister\_t](group__tee__interface.md#ga2ea18e713a101a6ca715baa04c2f4185))(const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm);

320

[ 328](group__tee__interface.md#gaae68677cbff1e831fadc3d188c8588ff)typedef int (\*[tee\_suppl\_recv\_t](group__tee__interface.md#gaae68677cbff1e831fadc3d188c8588ff))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*func, unsigned int \*num\_params,

329 struct [tee\_param](structtee__param.md) \*param);

330

[ 338](group__tee__interface.md#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20)typedef int (\*[tee\_suppl\_send\_t](group__tee__interface.md#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20))(const struct [device](structdevice.md) \*dev, unsigned int ret, unsigned int num\_params,

339 struct [tee\_param](structtee__param.md) \*param);

340

[ 341](structtee__driver__api.md)\_\_subsystem struct [tee\_driver\_api](structtee__driver__api.md) {

[ 342](structtee__driver__api.md#ac99f066bd644741df90d418ab9fe4198) [tee\_get\_version\_t](group__tee__interface.md#gac533d9e85d65857c0d984506024a55b4) [get\_version](structtee__driver__api.md#ac99f066bd644741df90d418ab9fe4198);

[ 343](structtee__driver__api.md#acf8076d0cf2bb496d9c6143d6e5d2253) [tee\_open\_session\_t](group__tee__interface.md#gaf972199fcdbd892688dc141ddba6e6aa) [open\_session](structtee__driver__api.md#acf8076d0cf2bb496d9c6143d6e5d2253);

[ 344](structtee__driver__api.md#a380a12c033c1c659d7169d0d16593f94) [tee\_close\_session\_t](group__tee__interface.md#gac412f57a3da187e6e272857d5bdaaaeb) [close\_session](structtee__driver__api.md#a380a12c033c1c659d7169d0d16593f94);

[ 345](structtee__driver__api.md#a04db5713f645416fa9cc015433941a94) [tee\_cancel\_t](group__tee__interface.md#gad4cd5b65cac3eb7b4338fd99eeb13a93) [cancel](structtee__driver__api.md#a04db5713f645416fa9cc015433941a94);

[ 346](structtee__driver__api.md#a5d2a33d8156fd56176f69e903da9204e) [tee\_invoke\_func\_t](group__tee__interface.md#gac3695e51dc8b08bb5e5c5d984c402b0e) [invoke\_func](structtee__driver__api.md#a5d2a33d8156fd56176f69e903da9204e);

[ 347](structtee__driver__api.md#a1db852ebd953c0c4ba5f88fcab9fdce9) [tee\_shm\_register\_t](group__tee__interface.md#ga9e2807d34d580c012129a2fc1f5a425a) [shm\_register](structtee__driver__api.md#a1db852ebd953c0c4ba5f88fcab9fdce9);

[ 348](structtee__driver__api.md#ac24f7f4d3f63145e8f687a37cad780ca) [tee\_shm\_unregister\_t](group__tee__interface.md#ga2ea18e713a101a6ca715baa04c2f4185) [shm\_unregister](structtee__driver__api.md#ac24f7f4d3f63145e8f687a37cad780ca);

[ 349](structtee__driver__api.md#a35c770c1dfb807bb461640a519fdabe5) [tee\_suppl\_recv\_t](group__tee__interface.md#gaae68677cbff1e831fadc3d188c8588ff) [suppl\_recv](structtee__driver__api.md#a35c770c1dfb807bb461640a519fdabe5);

[ 350](structtee__driver__api.md#abd28ba23f09ce245a6346f7a241eb9cc) [tee\_suppl\_send\_t](group__tee__interface.md#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20) [suppl\_send](structtee__driver__api.md#abd28ba23f09ce245a6346f7a241eb9cc);

351};

352

[ 365](group__tee__interface.md#gadaaec6b6ea29d81f36943bbe5bcb305e)\_\_syscall int [tee\_get\_version](group__tee__interface.md#gadaaec6b6ea29d81f36943bbe5bcb305e)(const struct [device](structdevice.md) \*dev, struct [tee\_version\_info](structtee__version__info.md) \*info);

366

367static inline int z\_impl\_tee\_get\_version(const struct [device](structdevice.md) \*dev, struct [tee\_version\_info](structtee__version__info.md) \*info)

368{

369 const struct [tee\_driver\_api](structtee__driver__api.md) \*api = (const struct [tee\_driver\_api](structtee__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

370

371 if (!api->get\_version) {

372 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

373 }

374

375 return api->get\_version(dev, info);

376}

377

[ 393](group__tee__interface.md#gad7c66e32d5b02c42c698bd422cf43523)\_\_syscall int [tee\_open\_session](group__tee__interface.md#gad7c66e32d5b02c42c698bd422cf43523)(const struct [device](structdevice.md) \*dev, struct [tee\_open\_session\_arg](structtee__open__session__arg.md) \*arg,

394 unsigned int num\_param, struct [tee\_param](structtee__param.md) \*param,

395 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*session\_id);

396

397static inline int z\_impl\_tee\_open\_session(const struct [device](structdevice.md) \*dev,

398 struct [tee\_open\_session\_arg](structtee__open__session__arg.md) \*arg,

399 unsigned int num\_param, struct [tee\_param](structtee__param.md) \*param,

400 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*session\_id)

401{

402 const struct [tee\_driver\_api](structtee__driver__api.md) \*api = (const struct [tee\_driver\_api](structtee__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

403

404 if (!api->open\_session) {

405 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

406 }

407

408 return api->open\_session(dev, arg, num\_param, param, session\_id);

409}

410

[ 423](group__tee__interface.md#gacb1d58002378a11d92361a149d451241)\_\_syscall int [tee\_close\_session](group__tee__interface.md#gacb1d58002378a11d92361a149d451241)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id);

424

425static inline int z\_impl\_tee\_close\_session(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id)

426{

427 const struct [tee\_driver\_api](structtee__driver__api.md) \*api = (const struct [tee\_driver\_api](structtee__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

428

429 if (!api->close\_session) {

430 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

431 }

432

433 return api->close\_session(dev, session\_id);

434}

435

[ 449](group__tee__interface.md#ga34fbbfe48a07541041ffddb9e318332a)\_\_syscall int [tee\_cancel](group__tee__interface.md#ga34fbbfe48a07541041ffddb9e318332a)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cancel\_id);

450

451static inline int z\_impl\_tee\_cancel(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id,

452 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cancel\_id)

453{

454 const struct [tee\_driver\_api](structtee__driver__api.md) \*api = (const struct [tee\_driver\_api](structtee__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

455

456 if (!api->cancel) {

457 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

458 }

459

460 return api->cancel(dev, session\_id, cancel\_id);

461}

462

[ 477](group__tee__interface.md#gae1337f293febcecc7dbc79ac064e7824)\_\_syscall int [tee\_invoke\_func](group__tee__interface.md#gae1337f293febcecc7dbc79ac064e7824)(const struct [device](structdevice.md) \*dev, struct [tee\_invoke\_func\_arg](structtee__invoke__func__arg.md) \*arg,

478 unsigned int num\_param, struct [tee\_param](structtee__param.md) \*param);

479

480static inline int z\_impl\_tee\_invoke\_func(const struct [device](structdevice.md) \*dev, struct [tee\_invoke\_func\_arg](structtee__invoke__func__arg.md) \*arg,

481 unsigned int num\_param, struct [tee\_param](structtee__param.md) \*param)

482{

483 const struct [tee\_driver\_api](structtee__driver__api.md) \*api = (const struct [tee\_driver\_api](structtee__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

484

485 if (!api->invoke\_func) {

486 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

487 }

488

489 return api->invoke\_func(dev, arg, num\_param, param);

490}

491

[ 506](group__tee__interface.md#gade7fdbece8b0bd47f5d148572016c4ef)int [tee\_add\_shm](group__tee__interface.md#gade7fdbece8b0bd47f5d148572016c4ef)(const struct [device](structdevice.md) \*dev, void \*addr, size\_t align, size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

507 struct [tee\_shm](structtee__shm.md) \*\*shmp);

508

[ 519](group__tee__interface.md#gaf53521a3e3a36a9827753716bef1434f)int [tee\_rm\_shm](group__tee__interface.md#gaf53521a3e3a36a9827753716bef1434f)(const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm);

520

[ 536](group__tee__interface.md#ga1565c23104792203ede9d9cb388ff782)\_\_syscall int [tee\_shm\_register](group__tee__interface.md#ga1565c23104792203ede9d9cb388ff782)(const struct [device](structdevice.md) \*dev, void \*addr, size\_t size,

537 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [tee\_shm](structtee__shm.md) \*\*shm);

538

539static inline int z\_impl\_tee\_shm\_register(const struct [device](structdevice.md) \*dev, void \*addr, size\_t size,

540 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [tee\_shm](structtee__shm.md) \*\*shm)

541{

542 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) &= [~TEE\_SHM\_ALLOC](group__tee__interface.md#ga85fd3e6e6b596da02c97661a35c9814c);

543 return [tee\_add\_shm](group__tee__interface.md#gade7fdbece8b0bd47f5d148572016c4ef)(dev, addr, 0, size, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | [TEE\_SHM\_REGISTER](group__tee__interface.md#ga2fac25b74105b1ddfb15db51598b89c8), shm);

544}

545

[ 558](group__tee__interface.md#gade2c0e7d89e3594707637b62a1901bac)\_\_syscall int [tee\_shm\_unregister](group__tee__interface.md#gade2c0e7d89e3594707637b62a1901bac)(const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm);

559

560static inline int z\_impl\_tee\_shm\_unregister(const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm)

561{

562 return [tee\_rm\_shm](group__tee__interface.md#gaf53521a3e3a36a9827753716bef1434f)(dev, shm);

563}

564

[ 579](group__tee__interface.md#ga47f7403e2b136f755432159c7bd679a5)\_\_syscall int [tee\_shm\_alloc](group__tee__interface.md#ga47f7403e2b136f755432159c7bd679a5)(const struct [device](structdevice.md) \*dev, size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

580 struct [tee\_shm](structtee__shm.md) \*\*shm);

581

582static inline int z\_impl\_tee\_shm\_alloc(const struct [device](structdevice.md) \*dev, size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

583 struct [tee\_shm](structtee__shm.md) \*\*shm)

584{

585 return [tee\_add\_shm](group__tee__interface.md#gade7fdbece8b0bd47f5d148572016c4ef)(dev, NULL, 0, size, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | [TEE\_SHM\_ALLOC](group__tee__interface.md#ga85fd3e6e6b596da02c97661a35c9814c) | [TEE\_SHM\_REGISTER](group__tee__interface.md#ga2fac25b74105b1ddfb15db51598b89c8), shm);

586}

587

[ 600](group__tee__interface.md#ga346d8d67a18542c097f1254c0ace8726)\_\_syscall int [tee\_shm\_free](group__tee__interface.md#ga346d8d67a18542c097f1254c0ace8726)(const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm);

601

602static inline int z\_impl\_tee\_shm\_free(const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm)

603{

604 return [tee\_rm\_shm](group__tee__interface.md#gaf53521a3e3a36a9827753716bef1434f)(dev, shm);

605}

606

[ 619](group__tee__interface.md#ga2213f63da1f080beaedc169e13531a37)\_\_syscall int [tee\_suppl\_recv](group__tee__interface.md#ga2213f63da1f080beaedc169e13531a37)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*func, unsigned int \*num\_params,

620 struct [tee\_param](structtee__param.md) \*param);

621

622static inline int z\_impl\_tee\_suppl\_recv(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*func,

623 unsigned int \*num\_params, struct [tee\_param](structtee__param.md) \*param)

624{

625 const struct [tee\_driver\_api](structtee__driver__api.md) \*api = (const struct [tee\_driver\_api](structtee__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

626

627 if (!api->suppl\_recv) {

628 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

629 }

630

631 return api->suppl\_recv(dev, func, num\_params, param);

632}

633

[ 647](group__tee__interface.md#ga93cccfa446983be704f364760bf7567b)\_\_syscall int [tee\_suppl\_send](group__tee__interface.md#ga93cccfa446983be704f364760bf7567b)(const struct [device](structdevice.md) \*dev, unsigned int ret, unsigned int num\_params,

648 struct [tee\_param](structtee__param.md) \*param);

649

650static inline int z\_impl\_tee\_suppl\_send(const struct [device](structdevice.md) \*dev, unsigned int ret,

651 unsigned int num\_params, struct [tee\_param](structtee__param.md) \*param)

652{

653 const struct [tee\_driver\_api](structtee__driver__api.md) \*api = (const struct [tee\_driver\_api](structtee__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

654

655 if (!api->suppl\_send) {

656 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

657 }

658

659 return api->suppl\_send(dev, ret, num\_params, param);

660}

661

662#ifdef \_\_cplusplus

663}

664#endif

665

669

670#include <zephyr/syscalls/tee.h>

671

672#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_TEE\_H\_ \*/

[device.h](device_8h.md)

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[tee\_shm\_register](group__tee__interface.md#ga1565c23104792203ede9d9cb388ff782)

int tee\_shm\_register(const struct device \*dev, void \*addr, size\_t size, uint32\_t flags, struct tee\_shm \*\*shm)

Register shared memory for Trusted Environment.

[tee\_suppl\_recv](group__tee__interface.md#ga2213f63da1f080beaedc169e13531a37)

int tee\_suppl\_recv(const struct device \*dev, uint32\_t \*func, unsigned int \*num\_params, struct tee\_param \*param)

Receive a request for TEE Supplicant.

[tee\_shm\_unregister\_t](group__tee__interface.md#ga2ea18e713a101a6ca715baa04c2f4185)

int(\* tee\_shm\_unregister\_t)(const struct device \*dev, struct tee\_shm \*shm)

Callback API to unregister shared memory.

**Definition** tee.h:319

[TEE\_SHM\_REGISTER](group__tee__interface.md#ga2fac25b74105b1ddfb15db51598b89c8)

#define TEE\_SHM\_REGISTER

**Definition** tee.h:79

[tee\_shm\_free](group__tee__interface.md#ga346d8d67a18542c097f1254c0ace8726)

int tee\_shm\_free(const struct device \*dev, struct tee\_shm \*shm)

Free shared memory region for Trusted Environment.

[tee\_cancel](group__tee__interface.md#ga34fbbfe48a07541041ffddb9e318332a)

int tee\_cancel(const struct device \*dev, uint32\_t session\_id, uint32\_t cancel\_id)

Cancel session or invoke function for Trusted Environment.

[tee\_suppl\_send\_t](group__tee__interface.md#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20)

int(\* tee\_suppl\_send\_t)(const struct device \*dev, unsigned int ret, unsigned int num\_params, struct tee\_param \*param)

Callback API to send a request for TEE supplicant.

**Definition** tee.h:338

[tee\_shm\_alloc](group__tee__interface.md#ga47f7403e2b136f755432159c7bd679a5)

int tee\_shm\_alloc(const struct device \*dev, size\_t size, uint32\_t flags, struct tee\_shm \*\*shm)

Allocate shared memory region for Trusted Environment.

[TEE\_UUID\_LEN](group__tee__interface.md#ga79ff2ca70757daf8e677b42002f4aeac)

#define TEE\_UUID\_LEN

**Definition** tee.h:72

[TEE\_SHM\_ALLOC](group__tee__interface.md#ga85fd3e6e6b596da02c97661a35c9814c)

#define TEE\_SHM\_ALLOC

**Definition** tee.h:80

[tee\_suppl\_send](group__tee__interface.md#ga93cccfa446983be704f364760bf7567b)

int tee\_suppl\_send(const struct device \*dev, unsigned int ret, unsigned int num\_params, struct tee\_param \*param)

Send a request for TEE Supplicant function.

[tee\_shm\_register\_t](group__tee__interface.md#ga9e2807d34d580c012129a2fc1f5a425a)

int(\* tee\_shm\_register\_t)(const struct device \*dev, struct tee\_shm \*shm)

Callback API to register shared memory.

**Definition** tee.h:310

[tee\_suppl\_recv\_t](group__tee__interface.md#gaae68677cbff1e831fadc3d188c8588ff)

int(\* tee\_suppl\_recv\_t)(const struct device \*dev, uint32\_t \*func, unsigned int \*num\_params, struct tee\_param \*param)

Callback API to receive a request for TEE supplicant.

**Definition** tee.h:328

[tee\_invoke\_func\_t](group__tee__interface.md#gac3695e51dc8b08bb5e5c5d984c402b0e)

int(\* tee\_invoke\_func\_t)(const struct device \*dev, struct tee\_invoke\_func\_arg \*arg, unsigned int num\_param, struct tee\_param \*param)

Callback API to invoke function to TA.

**Definition** tee.h:301

[tee\_close\_session\_t](group__tee__interface.md#gac412f57a3da187e6e272857d5bdaaaeb)

int(\* tee\_close\_session\_t)(const struct device \*dev, uint32\_t session\_id)

Callback API to close session to TA.

**Definition** tee.h:283

[tee\_get\_version\_t](group__tee__interface.md#gac533d9e85d65857c0d984506024a55b4)

int(\* tee\_get\_version\_t)(const struct device \*dev, struct tee\_version\_info \*info)

Callback API to get current tee version.

**Definition** tee.h:264

[tee\_close\_session](group__tee__interface.md#gacb1d58002378a11d92361a149d451241)

int tee\_close\_session(const struct device \*dev, uint32\_t session\_id)

Close session for Trusted Environment.

[tee\_cancel\_t](group__tee__interface.md#gad4cd5b65cac3eb7b4338fd99eeb13a93)

int(\* tee\_cancel\_t)(const struct device \*dev, uint32\_t session\_id, uint32\_t cancel\_id)

Callback API to cancel open session of invoke function to TA.

**Definition** tee.h:292

[tee\_open\_session](group__tee__interface.md#gad7c66e32d5b02c42c698bd422cf43523)

int tee\_open\_session(const struct device \*dev, struct tee\_open\_session\_arg \*arg, unsigned int num\_param, struct tee\_param \*param, uint32\_t \*session\_id)

Open session for Trusted Environment.

[tee\_get\_version](group__tee__interface.md#gadaaec6b6ea29d81f36943bbe5bcb305e)

int tee\_get\_version(const struct device \*dev, struct tee\_version\_info \*info)

Get the current TEE version info.

[tee\_shm\_unregister](group__tee__interface.md#gade2c0e7d89e3594707637b62a1901bac)

int tee\_shm\_unregister(const struct device \*dev, struct tee\_shm \*shm)

Unregister shared memory for Trusted Environment.

[tee\_add\_shm](group__tee__interface.md#gade7fdbece8b0bd47f5d148572016c4ef)

int tee\_add\_shm(const struct device \*dev, void \*addr, size\_t align, size\_t size, uint32\_t flags, struct tee\_shm \*\*shmp)

Helper function to allocate and register shared memory.

[tee\_invoke\_func](group__tee__interface.md#gae1337f293febcecc7dbc79ac064e7824)

int tee\_invoke\_func(const struct device \*dev, struct tee\_invoke\_func\_arg \*arg, unsigned int num\_param, struct tee\_param \*param)

Invoke function for Trusted Environment Application.

[tee\_rm\_shm](group__tee__interface.md#gaf53521a3e3a36a9827753716bef1434f)

int tee\_rm\_shm(const struct device \*dev, struct tee\_shm \*shm)

Helper function to remove and unregister shared memory.

[tee\_open\_session\_t](group__tee__interface.md#gaf972199fcdbd892688dc141ddba6e6aa)

int(\* tee\_open\_session\_t)(const struct device \*dev, struct tee\_open\_session\_arg \*arg, unsigned int num\_param, struct tee\_param \*param, uint32\_t \*session\_id)

Callback API to open session to Trusted Application.

**Definition** tee.h:273

[kernel.h](kernel_8h.md)

Public kernel APIs.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[tee\_driver\_api](structtee__driver__api.md)

**Definition** tee.h:341

[tee\_driver\_api::cancel](structtee__driver__api.md#a04db5713f645416fa9cc015433941a94)

tee\_cancel\_t cancel

**Definition** tee.h:345

[tee\_driver\_api::shm\_register](structtee__driver__api.md#a1db852ebd953c0c4ba5f88fcab9fdce9)

tee\_shm\_register\_t shm\_register

**Definition** tee.h:347

[tee\_driver\_api::suppl\_recv](structtee__driver__api.md#a35c770c1dfb807bb461640a519fdabe5)

tee\_suppl\_recv\_t suppl\_recv

**Definition** tee.h:349

[tee\_driver\_api::close\_session](structtee__driver__api.md#a380a12c033c1c659d7169d0d16593f94)

tee\_close\_session\_t close\_session

**Definition** tee.h:344

[tee\_driver\_api::invoke\_func](structtee__driver__api.md#a5d2a33d8156fd56176f69e903da9204e)

tee\_invoke\_func\_t invoke\_func

**Definition** tee.h:346

[tee\_driver\_api::suppl\_send](structtee__driver__api.md#abd28ba23f09ce245a6346f7a241eb9cc)

tee\_suppl\_send\_t suppl\_send

**Definition** tee.h:350

[tee\_driver\_api::shm\_unregister](structtee__driver__api.md#ac24f7f4d3f63145e8f687a37cad780ca)

tee\_shm\_unregister\_t shm\_unregister

**Definition** tee.h:348

[tee\_driver\_api::get\_version](structtee__driver__api.md#ac99f066bd644741df90d418ab9fe4198)

tee\_get\_version\_t get\_version

**Definition** tee.h:342

[tee\_driver\_api::open\_session](structtee__driver__api.md#acf8076d0cf2bb496d9c6143d6e5d2253)

tee\_open\_session\_t open\_session

**Definition** tee.h:343

[tee\_invoke\_func\_arg](structtee__invoke__func__arg.md)

Invokes a function in a Trusted Application.

**Definition** tee.h:239

[tee\_invoke\_func\_arg::func](structtee__invoke__func__arg.md#a17aa094ca0a6c6d9a72d2fae9c0c66ef)

uint32\_t func

[in] Trusted Application function, specific to the TA

**Definition** tee.h:240

[tee\_invoke\_func\_arg::cancel\_id](structtee__invoke__func__arg.md#a457daf2221f9520aecb42667acc4ccd1)

uint32\_t cancel\_id

[in] cancellation id, a unique value to identify this request

**Definition** tee.h:242

[tee\_invoke\_func\_arg::ret\_origin](structtee__invoke__func__arg.md#ae806e940e463321b3de31bad2e05bf60)

uint32\_t ret\_origin

[out] origin of the return value

**Definition** tee.h:244

[tee\_invoke\_func\_arg::session](structtee__invoke__func__arg.md#af110327354b1ca48dedf22855c3a7afc)

uint32\_t session

[in] session id

**Definition** tee.h:241

[tee\_invoke\_func\_arg::ret](structtee__invoke__func__arg.md#af63bd284a7397d4086ac17f83d6b1e93)

uint32\_t ret

[out] return value

**Definition** tee.h:243

[tee\_open\_session\_arg](structtee__open__session__arg.md)

Open session argument

**Definition** tee.h:205

[tee\_open\_session\_arg::clnt\_login](structtee__open__session__arg.md#a226c617eae1b959025a0232eed48aa41)

uint32\_t clnt\_login

login class of client, TEE\_IOCTL\_LOGIN\_\* above

**Definition** tee.h:208

[tee\_open\_session\_arg::ret](structtee__open__session__arg.md#a3be6d6ea6aeff1a8f27051fe30f21347)

uint32\_t ret

[out] return value

**Definition** tee.h:211

[tee\_open\_session\_arg::session](structtee__open__session__arg.md#a5e28bb77990ce6d050a57daa419760e1)

uint32\_t session

[out] session id

**Definition** tee.h:210

[tee\_open\_session\_arg::ret\_origin](structtee__open__session__arg.md#a73a7e82fb0b589eed327ab8f4217e6fc)

uint32\_t ret\_origin

[out] origin of the return value

**Definition** tee.h:212

[tee\_open\_session\_arg::uuid](structtee__open__session__arg.md#a9f4c56fe45f5ad9313bdc1f457d31f9a)

uint8\_t uuid[16]

[in] UUID of the Trusted Application

**Definition** tee.h:206

[tee\_open\_session\_arg::cancel\_id](structtee__open__session__arg.md#adf8bfaaf5059de617a7139b5f06a0ac6)

uint32\_t cancel\_id

[in] cancellation id, a unique value to identify this request

**Definition** tee.h:209

[tee\_open\_session\_arg::clnt\_uuid](structtee__open__session__arg.md#aff38cc02e83936e23965ee2e4e44ff26)

uint8\_t clnt\_uuid[16]

[in] UUID of client

**Definition** tee.h:207

[tee\_param](structtee__param.md)

Tee parameter.

**Definition** tee.h:229

[tee\_param::b](structtee__param.md#a22785fe00950c3a7d6353c39b12d72a8)

uint64\_t b

if a memref, size of the buffer, else a value parameter

**Definition** tee.h:232

[tee\_param::c](structtee__param.md#a79b39571785949e32629216742e34d72)

uint64\_t c

if a memref, shared memory identifier, else a value parameter

**Definition** tee.h:233

[tee\_param::attr](structtee__param.md#ac8ced719ce993735e22d68ca50f54e5b)

uint64\_t attr

attributes

**Definition** tee.h:230

[tee\_param::a](structtee__param.md#aea8916d1bc24ab5a56f59fa4608f1a38)

uint64\_t a

if a memref, offset into the shared memory object, else a value

**Definition** tee.h:231

[tee\_shm](structtee__shm.md)

Tee shared memory structure.

**Definition** tee.h:250

[tee\_shm::size](structtee__shm.md#a02fe0fd69f1e8d5650cfa116136ea9ca)

uint64\_t size

[out] shared buffer size

**Definition** tee.h:253

[tee\_shm::addr](structtee__shm.md#a65446310f73319aa5f8e100e4d83198e)

void \* addr

[out] shared buffer pointer

**Definition** tee.h:252

[tee\_shm::dev](structtee__shm.md#ab761c1d3d5e64c21725eff97521b4b86)

const struct device \* dev

[out] pointer to the device driver structure

**Definition** tee.h:251

[tee\_shm::flags](structtee__shm.md#ac2738d87cbe439f093cad67a375c2807)

uint32\_t flags

[out] shared buffer flags

**Definition** tee.h:254

[tee\_version\_info](structtee__version__info.md)

TEE version.

**Definition** tee.h:196

[tee\_version\_info::gen\_caps](structtee__version__info.md#a56a3c50a69f125428dfbf7a867cb7177)

uint32\_t gen\_caps

Generic capabilities, defined by TEE\_GEN\_CAPS\_\* above.

**Definition** tee.h:199

[tee\_version\_info::impl\_caps](structtee__version__info.md#a6cbf12676e5cfc1bdf4221a8188bf055)

uint32\_t impl\_caps

[out] implementation specific capabilities

**Definition** tee.h:198

[tee\_version\_info::impl\_id](structtee__version__info.md#aaf74a1ff5fb899a0675724669a7d7e36)

uint32\_t impl\_id

[out] TEE implementation id

**Definition** tee.h:197

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [tee.h](tee_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
