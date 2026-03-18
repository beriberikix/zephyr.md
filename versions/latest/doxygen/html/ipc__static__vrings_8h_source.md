---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ipc__static__vrings_8h_source.html
original_path: doxygen/html/ipc__static__vrings_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_static\_vrings.h

[Go to the documentation of this file.](ipc__static__vrings_8h.md)

1/\*

2 \* Copyright (c) 2021 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_IPC\_SERVICE\_IPC\_STATIC\_VRINGS\_H\_

8#define ZEPHYR\_INCLUDE\_IPC\_SERVICE\_IPC\_STATIC\_VRINGS\_H\_

9

10#include <[zephyr/ipc/ipc\_service.h](ipc__service_8h.md)>

11#include <openamp/open\_amp.h>

12#include <metal/device.h>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

24

[ 26](group__ipc__service__static__vrings__api.md#ga2b05772c325881ba650dc01f3e6e2834)#define VRING\_COUNT (2)

27

[ 34](group__ipc__service__static__vrings__api.md#ga97343214666ee6dcb18c0bd77b441ea7)#define MEM\_ALIGNMENT CONFIG\_IPC\_SERVICE\_STATIC\_VRINGS\_MEM\_ALIGNMENT

35

[ 45](group__ipc__service__static__vrings__api.md#ga70026ad72cd08d42461e1489c4ddfc9b)typedef void (\*[ipc\_notify\_cb](group__ipc__service__static__vrings__api.md#ga70026ad72cd08d42461e1489c4ddfc9b))(struct virtqueue \*vq, void \*priv);

46

[ 51](structipc__static__vrings.md)struct [ipc\_static\_vrings](structipc__static__vrings.md) {

[ 53](structipc__static__vrings.md#a1676900beba6921f55933dc174adad4d) struct virtio\_device [vdev](structipc__static__vrings.md#a1676900beba6921f55933dc174adad4d);

54

[ 56](structipc__static__vrings.md#ac8c8f9ec4dc0ef630f0b270208ec2674) metal\_phys\_addr\_t [shm\_physmap](structipc__static__vrings.md#ac8c8f9ec4dc0ef630f0b270208ec2674)[1];

57

[ 59](structipc__static__vrings.md#a25621a534fd37590758f13f96242dc37) struct metal\_device [shm\_device](structipc__static__vrings.md#a25621a534fd37590758f13f96242dc37);

60

[ 62](structipc__static__vrings.md#ae4871539972adc756ec57c8c20a7e2eb) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [status\_reg\_addr](structipc__static__vrings.md#ae4871539972adc756ec57c8c20a7e2eb);

63

[ 65](structipc__static__vrings.md#a59f39be99885182298f57af36fc874fb) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [tx\_addr](structipc__static__vrings.md#a59f39be99885182298f57af36fc874fb);

66

[ 68](structipc__static__vrings.md#a4eaf0eb4095a58fc6256d74911baa671) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [rx\_addr](structipc__static__vrings.md#a4eaf0eb4095a58fc6256d74911baa671);

69

[ 71](structipc__static__vrings.md#a893bc5387c5b29ecdcfc1abfd57c9caf) size\_t [vring\_size](structipc__static__vrings.md#a893bc5387c5b29ecdcfc1abfd57c9caf);

72

[ 74](structipc__static__vrings.md#ac68695b382dfe7c282eba3e97ea96022) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [shm\_addr](structipc__static__vrings.md#ac68695b382dfe7c282eba3e97ea96022);

75

[ 77](structipc__static__vrings.md#a6c31f7450f051c1ac4cd3cc56b133a3f) size\_t [shm\_size](structipc__static__vrings.md#a6c31f7450f051c1ac4cd3cc56b133a3f);

78

[ 80](structipc__static__vrings.md#a29071801929abab9da38c9d806faa89e) struct metal\_io\_region \*[shm\_io](structipc__static__vrings.md#a29071801929abab9da38c9d806faa89e);

81

[ 83](structipc__static__vrings.md#a9614b2239b4720fcc5ae58cf45816318) struct virtio\_vring\_info [rvrings](structipc__static__vrings.md#a9614b2239b4720fcc5ae58cf45816318)[[VRING\_COUNT](group__ipc__service__static__vrings__api.md#ga2b05772c325881ba650dc01f3e6e2834)];

84

[ 86](structipc__static__vrings.md#a787e801d8d836026a01e8b6bd4478c13) struct virtqueue \*[vq](structipc__static__vrings.md#a787e801d8d836026a01e8b6bd4478c13)[[VRING\_COUNT](group__ipc__service__static__vrings__api.md#ga2b05772c325881ba650dc01f3e6e2834)];

87

[ 89](structipc__static__vrings.md#a30d2cdf9ee8fb400dac490effc49cce2) void \*[priv](structipc__static__vrings.md#a30d2cdf9ee8fb400dac490effc49cce2);

90

[ 92](structipc__static__vrings.md#a16261f77762e5d226ed934d0ad2a51a6) [ipc\_notify\_cb](group__ipc__service__static__vrings__api.md#ga70026ad72cd08d42461e1489c4ddfc9b) [notify\_cb](structipc__static__vrings.md#a16261f77762e5d226ed934d0ad2a51a6);

93};

94

[ 107](group__ipc__service__static__vrings__api.md#ga5cab9a9a9ade1e61eb02592aa23dc0bc)int [ipc\_static\_vrings\_init](group__ipc__service__static__vrings__api.md#ga5cab9a9a9ade1e61eb02592aa23dc0bc)(struct [ipc\_static\_vrings](structipc__static__vrings.md) \*vr, unsigned int role);

108

[ 119](group__ipc__service__static__vrings__api.md#ga90680ce6a8cc4dae9cabba8fad6e939a)int [ipc\_static\_vrings\_deinit](group__ipc__service__static__vrings__api.md#ga90680ce6a8cc4dae9cabba8fad6e939a)(struct [ipc\_static\_vrings](structipc__static__vrings.md) \*vr, unsigned int role);

120

124

125#ifdef \_\_cplusplus

126}

127#endif

128

129#endif /\* ZEPHYR\_INCLUDE\_IPC\_SERVICE\_IPC\_STATIC\_VRINGS\_H\_ \*/

[VRING\_COUNT](group__ipc__service__static__vrings__api.md#ga2b05772c325881ba650dc01f3e6e2834)

#define VRING\_COUNT

Number of used VRING buffers.

**Definition** ipc\_static\_vrings.h:26

[ipc\_static\_vrings\_init](group__ipc__service__static__vrings__api.md#ga5cab9a9a9ade1e61eb02592aa23dc0bc)

int ipc\_static\_vrings\_init(struct ipc\_static\_vrings \*vr, unsigned int role)

Init the static VRINGs.

[ipc\_notify\_cb](group__ipc__service__static__vrings__api.md#ga70026ad72cd08d42461e1489c4ddfc9b)

void(\* ipc\_notify\_cb)(struct virtqueue \*vq, void \*priv)

Define the notify callback.

**Definition** ipc\_static\_vrings.h:45

[ipc\_static\_vrings\_deinit](group__ipc__service__static__vrings__api.md#ga90680ce6a8cc4dae9cabba8fad6e939a)

int ipc\_static\_vrings\_deinit(struct ipc\_static\_vrings \*vr, unsigned int role)

Deinitialise the static VRINGs.

[ipc\_service.h](ipc__service_8h.md)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[ipc\_static\_vrings](structipc__static__vrings.md)

Static VRINGs structure.

**Definition** ipc\_static\_vrings.h:51

[ipc\_static\_vrings::notify\_cb](structipc__static__vrings.md#a16261f77762e5d226ed934d0ad2a51a6)

ipc\_notify\_cb notify\_cb

Notify callback.

**Definition** ipc\_static\_vrings.h:92

[ipc\_static\_vrings::vdev](structipc__static__vrings.md#a1676900beba6921f55933dc174adad4d)

struct virtio\_device vdev

virtIO device.

**Definition** ipc\_static\_vrings.h:53

[ipc\_static\_vrings::shm\_device](structipc__static__vrings.md#a25621a534fd37590758f13f96242dc37)

struct metal\_device shm\_device

SHM device.

**Definition** ipc\_static\_vrings.h:59

[ipc\_static\_vrings::shm\_io](structipc__static__vrings.md#a29071801929abab9da38c9d806faa89e)

struct metal\_io\_region \* shm\_io

SHM IO region.

**Definition** ipc\_static\_vrings.h:80

[ipc\_static\_vrings::priv](structipc__static__vrings.md#a30d2cdf9ee8fb400dac490effc49cce2)

void \* priv

Private data to be passed to the notify callback.

**Definition** ipc\_static\_vrings.h:89

[ipc\_static\_vrings::rx\_addr](structipc__static__vrings.md#a4eaf0eb4095a58fc6256d74911baa671)

uintptr\_t rx\_addr

RX VRING address.

**Definition** ipc\_static\_vrings.h:68

[ipc\_static\_vrings::tx\_addr](structipc__static__vrings.md#a59f39be99885182298f57af36fc874fb)

uintptr\_t tx\_addr

TX VRING address.

**Definition** ipc\_static\_vrings.h:65

[ipc\_static\_vrings::shm\_size](structipc__static__vrings.md#a6c31f7450f051c1ac4cd3cc56b133a3f)

size\_t shm\_size

Share memory region size.

**Definition** ipc\_static\_vrings.h:77

[ipc\_static\_vrings::vq](structipc__static__vrings.md#a787e801d8d836026a01e8b6bd4478c13)

struct virtqueue \* vq[(2)]

Virtqueues.

**Definition** ipc\_static\_vrings.h:86

[ipc\_static\_vrings::vring\_size](structipc__static__vrings.md#a893bc5387c5b29ecdcfc1abfd57c9caf)

size\_t vring\_size

VRING size.

**Definition** ipc\_static\_vrings.h:71

[ipc\_static\_vrings::rvrings](structipc__static__vrings.md#a9614b2239b4720fcc5ae58cf45816318)

struct virtio\_vring\_info rvrings[(2)]

VRINGs.

**Definition** ipc\_static\_vrings.h:83

[ipc\_static\_vrings::shm\_addr](structipc__static__vrings.md#ac68695b382dfe7c282eba3e97ea96022)

uintptr\_t shm\_addr

Shared memory region address.

**Definition** ipc\_static\_vrings.h:74

[ipc\_static\_vrings::shm\_physmap](structipc__static__vrings.md#ac8c8f9ec4dc0ef630f0b270208ec2674)

metal\_phys\_addr\_t shm\_physmap[1]

SHM physmap.

**Definition** ipc\_static\_vrings.h:56

[ipc\_static\_vrings::status\_reg\_addr](structipc__static__vrings.md#ae4871539972adc756ec57c8c20a7e2eb)

uintptr\_t status\_reg\_addr

SHM and addresses.

**Definition** ipc\_static\_vrings.h:62

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [ipc\_static\_vrings.h](ipc__static__vrings_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
