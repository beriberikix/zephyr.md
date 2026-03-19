---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ipc__static__vrings_8h_source.html
original_path: doxygen/html/ipc__static__vrings_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

[ 25](group__ipc__service__static__vrings__api.md#ga2b05772c325881ba650dc01f3e6e2834)#define VRING\_COUNT (2)

26

[ 33](group__ipc__service__static__vrings__api.md#ga97343214666ee6dcb18c0bd77b441ea7)#define MEM\_ALIGNMENT CONFIG\_IPC\_SERVICE\_STATIC\_VRINGS\_MEM\_ALIGNMENT

34

[ 44](group__ipc__service__static__vrings__api.md#ga70026ad72cd08d42461e1489c4ddfc9b)typedef void (\*[ipc\_notify\_cb](group__ipc__service__static__vrings__api.md#ga70026ad72cd08d42461e1489c4ddfc9b))(struct virtqueue \*vq, void \*priv);

45

[ 50](structipc__static__vrings.md)struct [ipc\_static\_vrings](structipc__static__vrings.md) {

[ 52](structipc__static__vrings.md#a1676900beba6921f55933dc174adad4d) struct virtio\_device [vdev](structipc__static__vrings.md#a1676900beba6921f55933dc174adad4d);

53

[ 55](structipc__static__vrings.md#ac8c8f9ec4dc0ef630f0b270208ec2674) metal\_phys\_addr\_t [shm\_physmap](structipc__static__vrings.md#ac8c8f9ec4dc0ef630f0b270208ec2674)[1];

56

[ 58](structipc__static__vrings.md#ae4871539972adc756ec57c8c20a7e2eb) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [status\_reg\_addr](structipc__static__vrings.md#ae4871539972adc756ec57c8c20a7e2eb);

59

[ 61](structipc__static__vrings.md#a59f39be99885182298f57af36fc874fb) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [tx\_addr](structipc__static__vrings.md#a59f39be99885182298f57af36fc874fb);

62

[ 64](structipc__static__vrings.md#a4eaf0eb4095a58fc6256d74911baa671) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [rx\_addr](structipc__static__vrings.md#a4eaf0eb4095a58fc6256d74911baa671);

65

[ 67](structipc__static__vrings.md#a893bc5387c5b29ecdcfc1abfd57c9caf) size\_t [vring\_size](structipc__static__vrings.md#a893bc5387c5b29ecdcfc1abfd57c9caf);

68

[ 70](structipc__static__vrings.md#ac68695b382dfe7c282eba3e97ea96022) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [shm\_addr](structipc__static__vrings.md#ac68695b382dfe7c282eba3e97ea96022);

71

[ 73](structipc__static__vrings.md#a6c31f7450f051c1ac4cd3cc56b133a3f) size\_t [shm\_size](structipc__static__vrings.md#a6c31f7450f051c1ac4cd3cc56b133a3f);

74

[ 76](structipc__static__vrings.md#a9421025bb9c06fc7b0e5fa300f2be403) struct metal\_io\_region [shm\_io](structipc__static__vrings.md#a9421025bb9c06fc7b0e5fa300f2be403);

77

[ 79](structipc__static__vrings.md#a9614b2239b4720fcc5ae58cf45816318) struct virtio\_vring\_info [rvrings](structipc__static__vrings.md#a9614b2239b4720fcc5ae58cf45816318)[[VRING\_COUNT](group__ipc__service__static__vrings__api.md#ga2b05772c325881ba650dc01f3e6e2834)];

80

[ 82](structipc__static__vrings.md#a787e801d8d836026a01e8b6bd4478c13) struct virtqueue \*[vq](structipc__static__vrings.md#a787e801d8d836026a01e8b6bd4478c13)[[VRING\_COUNT](group__ipc__service__static__vrings__api.md#ga2b05772c325881ba650dc01f3e6e2834)];

83

[ 85](structipc__static__vrings.md#a30d2cdf9ee8fb400dac490effc49cce2) void \*[priv](structipc__static__vrings.md#a30d2cdf9ee8fb400dac490effc49cce2);

86

[ 88](structipc__static__vrings.md#a16261f77762e5d226ed934d0ad2a51a6) [ipc\_notify\_cb](group__ipc__service__static__vrings__api.md#ga70026ad72cd08d42461e1489c4ddfc9b) [notify\_cb](structipc__static__vrings.md#a16261f77762e5d226ed934d0ad2a51a6);

89};

90

[ 103](group__ipc__service__static__vrings__api.md#ga5cab9a9a9ade1e61eb02592aa23dc0bc)int [ipc\_static\_vrings\_init](group__ipc__service__static__vrings__api.md#ga5cab9a9a9ade1e61eb02592aa23dc0bc)(struct [ipc\_static\_vrings](structipc__static__vrings.md) \*vr, unsigned int role);

104

[ 115](group__ipc__service__static__vrings__api.md#ga90680ce6a8cc4dae9cabba8fad6e939a)int [ipc\_static\_vrings\_deinit](group__ipc__service__static__vrings__api.md#ga90680ce6a8cc4dae9cabba8fad6e939a)(struct [ipc\_static\_vrings](structipc__static__vrings.md) \*vr, unsigned int role);

116

120

121#ifdef \_\_cplusplus

122}

123#endif

124

125#endif /\* ZEPHYR\_INCLUDE\_IPC\_SERVICE\_IPC\_STATIC\_VRINGS\_H\_ \*/

[VRING\_COUNT](group__ipc__service__static__vrings__api.md#ga2b05772c325881ba650dc01f3e6e2834)

#define VRING\_COUNT

Number of used VRING buffers.

**Definition** ipc\_static\_vrings.h:25

[ipc\_static\_vrings\_init](group__ipc__service__static__vrings__api.md#ga5cab9a9a9ade1e61eb02592aa23dc0bc)

int ipc\_static\_vrings\_init(struct ipc\_static\_vrings \*vr, unsigned int role)

Init the static VRINGs.

[ipc\_notify\_cb](group__ipc__service__static__vrings__api.md#ga70026ad72cd08d42461e1489c4ddfc9b)

void(\* ipc\_notify\_cb)(struct virtqueue \*vq, void \*priv)

Define the notify callback.

**Definition** ipc\_static\_vrings.h:44

[ipc\_static\_vrings\_deinit](group__ipc__service__static__vrings__api.md#ga90680ce6a8cc4dae9cabba8fad6e939a)

int ipc\_static\_vrings\_deinit(struct ipc\_static\_vrings \*vr, unsigned int role)

Deinitialise the static VRINGs.

[ipc\_service.h](ipc__service_8h.md)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[ipc\_static\_vrings](structipc__static__vrings.md)

Static VRINGs structure.

**Definition** ipc\_static\_vrings.h:50

[ipc\_static\_vrings::notify\_cb](structipc__static__vrings.md#a16261f77762e5d226ed934d0ad2a51a6)

ipc\_notify\_cb notify\_cb

Notify callback.

**Definition** ipc\_static\_vrings.h:88

[ipc\_static\_vrings::vdev](structipc__static__vrings.md#a1676900beba6921f55933dc174adad4d)

struct virtio\_device vdev

virtIO device.

**Definition** ipc\_static\_vrings.h:52

[ipc\_static\_vrings::priv](structipc__static__vrings.md#a30d2cdf9ee8fb400dac490effc49cce2)

void \* priv

Private data to be passed to the notify callback.

**Definition** ipc\_static\_vrings.h:85

[ipc\_static\_vrings::rx\_addr](structipc__static__vrings.md#a4eaf0eb4095a58fc6256d74911baa671)

uintptr\_t rx\_addr

RX VRING address.

**Definition** ipc\_static\_vrings.h:64

[ipc\_static\_vrings::tx\_addr](structipc__static__vrings.md#a59f39be99885182298f57af36fc874fb)

uintptr\_t tx\_addr

TX VRING address.

**Definition** ipc\_static\_vrings.h:61

[ipc\_static\_vrings::shm\_size](structipc__static__vrings.md#a6c31f7450f051c1ac4cd3cc56b133a3f)

size\_t shm\_size

Share memory region size.

**Definition** ipc\_static\_vrings.h:73

[ipc\_static\_vrings::vq](structipc__static__vrings.md#a787e801d8d836026a01e8b6bd4478c13)

struct virtqueue \* vq[(2)]

Virtqueues.

**Definition** ipc\_static\_vrings.h:82

[ipc\_static\_vrings::vring\_size](structipc__static__vrings.md#a893bc5387c5b29ecdcfc1abfd57c9caf)

size\_t vring\_size

VRING size.

**Definition** ipc\_static\_vrings.h:67

[ipc\_static\_vrings::shm\_io](structipc__static__vrings.md#a9421025bb9c06fc7b0e5fa300f2be403)

struct metal\_io\_region shm\_io

SHM IO region.

**Definition** ipc\_static\_vrings.h:76

[ipc\_static\_vrings::rvrings](structipc__static__vrings.md#a9614b2239b4720fcc5ae58cf45816318)

struct virtio\_vring\_info rvrings[(2)]

VRINGs.

**Definition** ipc\_static\_vrings.h:79

[ipc\_static\_vrings::shm\_addr](structipc__static__vrings.md#ac68695b382dfe7c282eba3e97ea96022)

uintptr\_t shm\_addr

Shared memory region address.

**Definition** ipc\_static\_vrings.h:70

[ipc\_static\_vrings::shm\_physmap](structipc__static__vrings.md#ac8c8f9ec4dc0ef630f0b270208ec2674)

metal\_phys\_addr\_t shm\_physmap[1]

SHM physmap.

**Definition** ipc\_static\_vrings.h:55

[ipc\_static\_vrings::status\_reg\_addr](structipc__static__vrings.md#ae4871539972adc756ec57c8c20a7e2eb)

uintptr\_t status\_reg\_addr

SHM and addresses.

**Definition** ipc\_static\_vrings.h:58

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [ipc\_static\_vrings.h](ipc__static__vrings_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
