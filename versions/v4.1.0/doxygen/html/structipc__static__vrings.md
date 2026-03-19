---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structipc__static__vrings.html
original_path: doxygen/html/structipc__static__vrings.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_static\_vrings Struct Reference

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md) » [IPC service static VRINGs API](group__ipc__service__static__vrings__api.md)

Static VRINGs structure.
[More...](#details)

`#include <[ipc_static_vrings.h](ipc__static__vrings_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct virtio\_device | [vdev](#a1676900beba6921f55933dc174adad4d) |
|  | virtIO device. |
| metal\_phys\_addr\_t | [shm\_physmap](#ac8c8f9ec4dc0ef630f0b270208ec2674) [1] |
|  | SHM physmap. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [status\_reg\_addr](#ae4871539972adc756ec57c8c20a7e2eb) |
|  | SHM and addresses. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [tx\_addr](#a59f39be99885182298f57af36fc874fb) |
|  | TX VRING address. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [rx\_addr](#a4eaf0eb4095a58fc6256d74911baa671) |
|  | RX VRING address. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [vring\_size](#a893bc5387c5b29ecdcfc1abfd57c9caf) |
|  | VRING size. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [shm\_addr](#ac68695b382dfe7c282eba3e97ea96022) |
|  | Shared memory region address. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [shm\_size](#a6c31f7450f051c1ac4cd3cc56b133a3f) |
|  | Share memory region size. |
| struct metal\_io\_region | [shm\_io](#a9421025bb9c06fc7b0e5fa300f2be403) |
|  | SHM IO region. |
| struct virtio\_vring\_info | [rvrings](#a9614b2239b4720fcc5ae58cf45816318) [(2)] |
|  | VRINGs. |
| struct virtqueue \* | [vq](#a787e801d8d836026a01e8b6bd4478c13) [(2)] |
|  | Virtqueues. |
| void \* | [priv](#a30d2cdf9ee8fb400dac490effc49cce2) |
|  | Private data to be passed to the notify callback. |
| [ipc\_notify\_cb](group__ipc__service__static__vrings__api.md#ga70026ad72cd08d42461e1489c4ddfc9b) | [notify\_cb](#a16261f77762e5d226ed934d0ad2a51a6) |
|  | Notify callback. |

## Detailed Description

Static VRINGs structure.

Struct used to represent and carry information about static allocation of VRINGs.

## Field Documentation

## [◆ ](#a16261f77762e5d226ed934d0ad2a51a6)notify\_cb

| [ipc\_notify\_cb](group__ipc__service__static__vrings__api.md#ga70026ad72cd08d42461e1489c4ddfc9b) ipc\_static\_vrings::notify\_cb |
| --- |

Notify callback.

## [◆ ](#a30d2cdf9ee8fb400dac490effc49cce2)priv

| void\* ipc\_static\_vrings::priv |
| --- |

Private data to be passed to the notify callback.

## [◆ ](#a9614b2239b4720fcc5ae58cf45816318)rvrings

| struct virtio\_vring\_info ipc\_static\_vrings::rvrings[(2)] |
| --- |

VRINGs.

## [◆ ](#a4eaf0eb4095a58fc6256d74911baa671)rx\_addr

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) ipc\_static\_vrings::rx\_addr |
| --- |

RX VRING address.

## [◆ ](#ac68695b382dfe7c282eba3e97ea96022)shm\_addr

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) ipc\_static\_vrings::shm\_addr |
| --- |

Shared memory region address.

## [◆ ](#a9421025bb9c06fc7b0e5fa300f2be403)shm\_io

| struct metal\_io\_region ipc\_static\_vrings::shm\_io |
| --- |

SHM IO region.

## [◆ ](#ac8c8f9ec4dc0ef630f0b270208ec2674)shm\_physmap

| metal\_phys\_addr\_t ipc\_static\_vrings::shm\_physmap[1] |
| --- |

SHM physmap.

## [◆ ](#a6c31f7450f051c1ac4cd3cc56b133a3f)shm\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ipc\_static\_vrings::shm\_size |
| --- |

Share memory region size.

## [◆ ](#ae4871539972adc756ec57c8c20a7e2eb)status\_reg\_addr

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) ipc\_static\_vrings::status\_reg\_addr |
| --- |

SHM and addresses.

## [◆ ](#a59f39be99885182298f57af36fc874fb)tx\_addr

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) ipc\_static\_vrings::tx\_addr |
| --- |

TX VRING address.

## [◆ ](#a1676900beba6921f55933dc174adad4d)vdev

| struct virtio\_device ipc\_static\_vrings::vdev |
| --- |

virtIO device.

## [◆ ](#a787e801d8d836026a01e8b6bd4478c13)vq

| struct virtqueue\* ipc\_static\_vrings::vq[(2)] |
| --- |

Virtqueues.

## [◆ ](#a893bc5387c5b29ecdcfc1abfd57c9caf)vring\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ipc\_static\_vrings::vring\_size |
| --- |

VRING size.

---

The documentation for this struct was generated from the following file:

- zephyr/ipc/[ipc\_static\_vrings.h](ipc__static__vrings_8h_source.md)

- [ipc\_static\_vrings](structipc__static__vrings.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
