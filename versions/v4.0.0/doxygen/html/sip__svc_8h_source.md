---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sip__svc_8h_source.html
original_path: doxygen/html/sip__svc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc.h

[Go to the documentation of this file.](sip__svc_8h.md)

1/\*

2 \* Copyright (c) 2022-2023, Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SIP\_SVC\_H\_

8#define ZEPHYR\_INCLUDE\_SIP\_SVC\_H\_

9

42

43#include <[zephyr/kernel.h](kernel_8h.md)>

44#include <[zephyr/arch/arm64/arm-smccc.h](arm-smccc_8h.md)>

45#include <[zephyr/drivers/sip\_svc/sip\_svc\_proto.h](sip__svc__proto_8h.md)>

46

[ 47](sip__svc_8h.md#ab90395e8383b1665ef5d6d88114432d8)#define SIP\_SVC\_CLIENT\_ST\_INVALID 0

[ 48](sip__svc_8h.md#a65723ac5b896f336035fc28e42ba973b)#define SIP\_SVC\_CLIENT\_ST\_IDLE 1

[ 49](sip__svc_8h.md#a2d2ad62c149785afe1d60bd4c36e0008)#define SIP\_SVC\_CLIENT\_ST\_OPEN 2

[ 50](sip__svc_8h.md#ae200454b4fde621b96b2a17b8f1885a2)#define SIP\_SVC\_CLIENT\_ST\_ABORT 3

51

[ 59](sip__svc_8h.md#a73d836f58dd466241f5ba50955468b4c)typedef void (\*[sip\_svc\_cb\_fn](sip__svc_8h.md#a73d836f58dd466241f5ba50955468b4c))([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token, struct [sip\_svc\_response](structsip__svc__response.md) \*res);

60

[ 77](sip__svc_8h.md#a7f5a7116667f4904d128935e3a0fcc58)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sip\_svc\_register](sip__svc_8h.md#a7f5a7116667f4904d128935e3a0fcc58)(void \*ctrl, void \*[priv\_data](structsip__svc__response.md#a992b3f936866852633569f9c8d37d6a0));

78

[ 95](sip__svc_8h.md#aaafe385fe1dd0b13fe6dbffd2f01bd16)int [sip\_svc\_unregister](sip__svc_8h.md#aaafe385fe1dd0b13fe6dbffd2f01bd16)(void \*ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token);

96

[ 119](sip__svc_8h.md#ac1991768d256e5260542c544859c5bca)int [sip\_svc\_open](sip__svc_8h.md#ac1991768d256e5260542c544859c5bca)(void \*ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token, [k\_timeout\_t](structk__timeout__t.md) k\_timeout);

120

[ 135](sip__svc_8h.md#ab3774b372ddba3d3c4dd6e0a80082b9e)int [sip\_svc\_close](sip__svc_8h.md#ab3774b372ddba3d3c4dd6e0a80082b9e)(void \*ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token, struct [sip\_svc\_request](structsip__svc__request.md) \*pre\_close\_req);

136

[ 163](sip__svc_8h.md#afd71f6da58b4e8df3fbcf3b985226e74)int [sip\_svc\_send](sip__svc_8h.md#afd71f6da58b4e8df3fbcf3b985226e74)(void \*ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token, struct [sip\_svc\_request](structsip__svc__request.md) \*req, [sip\_svc\_cb\_fn](sip__svc_8h.md#a73d836f58dd466241f5ba50955468b4c) cb);

164

[ 176](sip__svc_8h.md#a754649a7ad55281bc0059036b0e5c7e9)void \*[sip\_svc\_get\_priv\_data](sip__svc_8h.md#a754649a7ad55281bc0059036b0e5c7e9)(void \*ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token);

177

[ 186](sip__svc_8h.md#a217c518c046cd1d716d803175b4cd99e)void \*[sip\_svc\_get\_controller](sip__svc_8h.md#a217c518c046cd1d716d803175b4cd99e)(char \*method);

187

188#endif /\* ZEPHYR\_INCLUDE\_SIP\_SVC\_H\_ \*/

[arm-smccc.h](arm-smccc_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[sip\_svc\_get\_controller](sip__svc_8h.md#a217c518c046cd1d716d803175b4cd99e)

void \* sip\_svc\_get\_controller(char \*method)

get the ARM SiP service handle

[sip\_svc\_cb\_fn](sip__svc_8h.md#a73d836f58dd466241f5ba50955468b4c)

void(\* sip\_svc\_cb\_fn)(uint32\_t c\_token, struct sip\_svc\_response \*res)

ARM sip service callback function prototype for response after completion.

**Definition** sip\_svc.h:59

[sip\_svc\_get\_priv\_data](sip__svc_8h.md#a754649a7ad55281bc0059036b0e5c7e9)

void \* sip\_svc\_get\_priv\_data(void \*ctrl, uint32\_t c\_token)

Get the address pointer to the client private data.

[sip\_svc\_register](sip__svc_8h.md#a7f5a7116667f4904d128935e3a0fcc58)

uint32\_t sip\_svc\_register(void \*ctrl, void \*priv\_data)

Register a client on ARM SiP service.

[sip\_svc\_unregister](sip__svc_8h.md#aaafe385fe1dd0b13fe6dbffd2f01bd16)

int sip\_svc\_unregister(void \*ctrl, uint32\_t c\_token)

Unregister a client on ARM SiP service.

[sip\_svc\_close](sip__svc_8h.md#ab3774b372ddba3d3c4dd6e0a80082b9e)

int sip\_svc\_close(void \*ctrl, uint32\_t c\_token, struct sip\_svc\_request \*pre\_close\_req)

Client requests to close the channel on ARM SiP services.

[sip\_svc\_open](sip__svc_8h.md#ac1991768d256e5260542c544859c5bca)

int sip\_svc\_open(void \*ctrl, uint32\_t c\_token, k\_timeout\_t k\_timeout)

Client requests to open a channel on ARM SiP service.

[sip\_svc\_send](sip__svc_8h.md#afd71f6da58b4e8df3fbcf3b985226e74)

int sip\_svc\_send(void \*ctrl, uint32\_t c\_token, struct sip\_svc\_request \*req, sip\_svc\_cb\_fn cb)

Client requests to send a SMC/HVC call to EL3/EL2.

[sip\_svc\_proto.h](sip__svc__proto_8h.md)

Arm SiP services communication protocol between service provider and client.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[sip\_svc\_request](structsip__svc__request.md)

SiP Service communication protocol request format.

**Definition** sip\_svc\_proto.h:133

[sip\_svc\_response](structsip__svc__response.md)

SiP Services service communication protocol response format.

**Definition** sip\_svc\_proto.h:177

[sip\_svc\_response::priv\_data](structsip__svc__response.md#a992b3f936866852633569f9c8d37d6a0)

void \* priv\_data

**Definition** sip\_svc\_proto.h:185

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sip\_svc](dir_8cbf67ac7d7b628e7429e25a66b76887.md)
- [sip\_svc.h](sip__svc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
