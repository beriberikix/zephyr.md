---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/posix__types_8h.html
original_path: doxygen/html/posix__types_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

posix\_types.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](posix__types_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pthread\_attr](structpthread__attr.md) |
| struct | [pthread\_mutexattr](structpthread__mutexattr.md) |
| struct | [pthread\_condattr](structpthread__condattr.md) |
| struct | [pthread\_barrierattr](structpthread__barrierattr.md) |
| struct | [pthread\_once](structpthread__once.md) |

| Typedefs | |
| --- | --- |
| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [clock\_t](#a3b55f88f25d2c571de53a365ad658426) |
| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [clockid\_t](#a6bb3206700910111f26e946bfbf0f2af) |
| typedef int | [dev\_t](#a0f89a9a6420c24efc5254e10170009e9) |
| typedef int | [ino\_t](#a779f87527fcb00a46d12056b753cf22c) |
| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [nlink\_t](#a952c84a825bb4f319cf55c9afb99ee0e) |
| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [uid\_t](#a75bb141dc55bc89a8ddc565fd374e3d9) |
| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [gid\_t](#a3a7834be1a79bb0c5a65d3546c2e3bd8) |
| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [blksize\_t](#a50c0d048e63387089a42aaf054a6d05b) |
| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [blkcnt\_t](#aa9a628992e7bcdc59d4fb606baada347) |
| typedef int | [pid\_t](#a288e13e815d43b06e75819f8939524df) |
| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [useconds\_t](#a1cf3c794977f92f3ccf2e041a68f3342) |
| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [timer\_t](#aa37fa84abebf94371f0c8426c2fc614d) |
| typedef struct [pthread\_attr](structpthread__attr.md) | [pthread\_attr\_t](#a1d96fa5809832849f591deef6cc7af7a) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pthread\_t](#a405938c67e9c568fde9993c7e14d58ec) = [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [pthread\_attr](structpthread__attr.md))) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pthread\_spinlock\_t](#a1d9c308dd59bf38ff0a7a45020d0aefa) |
| typedef struct k\_sem | [sem\_t](#afb4edc6a51d66a7a352424942b631a1e) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pthread\_mutex\_t](#a465eb2b962de164efdc8ce957025de7e) |
| typedef struct [pthread\_mutexattr](structpthread__mutexattr.md) | [pthread\_mutexattr\_t](#a2489174ff5737a33443b0959f4278765) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pthread\_cond\_t](#a1b893f49dfdf497be09c04a0e40f425e) = [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [pthread\_mutexattr](structpthread__mutexattr.md))) |
| typedef struct [pthread\_condattr](structpthread__condattr.md) | [pthread\_condattr\_t](#a9f62774a7a4e1634e60fb611765251f1) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pthread\_barrier\_t](#aeb637552f63e4c249e7aaeb2905f3db2) = [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [pthread\_condattr](structpthread__condattr.md))) |
| typedef struct [pthread\_barrierattr](structpthread__barrierattr.md) | [pthread\_barrierattr\_t](#a24d58850626c8022bf4bbd5d2628615b) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pthread\_rwlockattr\_t](#a4e92e3fbb4be682babbb6796af90b50f) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pthread\_rwlock\_t](#acd12f65541fede33b6226f646e900ea6) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pthread\_key\_t](#a8fd226393057ab7a8b17ac1c8b061911) |
| typedef struct [pthread\_once](structpthread__once.md) | [pthread\_once\_t](#a2603a6fda916554839174bc7d8849297) |

## Typedef Documentation

## [◆ ](#aa9a628992e7bcdc59d4fb606baada347)blkcnt\_t

| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long [blkcnt\_t](#aa9a628992e7bcdc59d4fb606baada347) |
| --- |

## [◆ ](#a50c0d048e63387089a42aaf054a6d05b)blksize\_t

| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long [blksize\_t](#a50c0d048e63387089a42aaf054a6d05b) |
| --- |

## [◆ ](#a3b55f88f25d2c571de53a365ad658426)clock\_t

| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long [clock\_t](#a3b55f88f25d2c571de53a365ad658426) |
| --- |

## [◆ ](#a6bb3206700910111f26e946bfbf0f2af)clockid\_t

| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long [clockid\_t](#a6bb3206700910111f26e946bfbf0f2af) |
| --- |

## [◆ ](#a0f89a9a6420c24efc5254e10170009e9)dev\_t

| typedef int [dev\_t](#a0f89a9a6420c24efc5254e10170009e9) |
| --- |

## [◆ ](#a3a7834be1a79bb0c5a65d3546c2e3bd8)gid\_t

| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short [gid\_t](#a3a7834be1a79bb0c5a65d3546c2e3bd8) |
| --- |

## [◆ ](#a779f87527fcb00a46d12056b753cf22c)ino\_t

| typedef int [ino\_t](#a779f87527fcb00a46d12056b753cf22c) |
| --- |

## [◆ ](#a952c84a825bb4f319cf55c9afb99ee0e)nlink\_t

| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short [nlink\_t](#a952c84a825bb4f319cf55c9afb99ee0e) |
| --- |

## [◆ ](#a288e13e815d43b06e75819f8939524df)pid\_t

| typedef int [pid\_t](#a288e13e815d43b06e75819f8939524df) |
| --- |

## [◆ ](#a1d96fa5809832849f591deef6cc7af7a)pthread\_attr\_t

| typedef struct [pthread\_attr](structpthread__attr.md) [pthread\_attr\_t](#a1d96fa5809832849f591deef6cc7af7a) |
| --- |

## [◆ ](#aeb637552f63e4c249e7aaeb2905f3db2)pthread\_barrier\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_barrier\_t](#aeb637552f63e4c249e7aaeb2905f3db2) = [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [pthread\_condattr](structpthread__condattr.md))) |
| --- |

## [◆ ](#a24d58850626c8022bf4bbd5d2628615b)pthread\_barrierattr\_t

| typedef struct [pthread\_barrierattr](structpthread__barrierattr.md) [pthread\_barrierattr\_t](#a24d58850626c8022bf4bbd5d2628615b) |
| --- |

## [◆ ](#a1b893f49dfdf497be09c04a0e40f425e)pthread\_cond\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_cond\_t](#a1b893f49dfdf497be09c04a0e40f425e) = [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [pthread\_mutexattr](structpthread__mutexattr.md))) |
| --- |

## [◆ ](#a9f62774a7a4e1634e60fb611765251f1)pthread\_condattr\_t

| typedef struct [pthread\_condattr](structpthread__condattr.md) [pthread\_condattr\_t](#a9f62774a7a4e1634e60fb611765251f1) |
| --- |

## [◆ ](#a8fd226393057ab7a8b17ac1c8b061911)pthread\_key\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_key\_t](#a8fd226393057ab7a8b17ac1c8b061911) |
| --- |

## [◆ ](#a465eb2b962de164efdc8ce957025de7e)pthread\_mutex\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_mutex\_t](#a465eb2b962de164efdc8ce957025de7e) |
| --- |

## [◆ ](#a2489174ff5737a33443b0959f4278765)pthread\_mutexattr\_t

| typedef struct [pthread\_mutexattr](structpthread__mutexattr.md) [pthread\_mutexattr\_t](#a2489174ff5737a33443b0959f4278765) |
| --- |

## [◆ ](#a2603a6fda916554839174bc7d8849297)pthread\_once\_t

| typedef struct [pthread\_once](structpthread__once.md) [pthread\_once\_t](#a2603a6fda916554839174bc7d8849297) |
| --- |

## [◆ ](#acd12f65541fede33b6226f646e900ea6)pthread\_rwlock\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_rwlock\_t](#acd12f65541fede33b6226f646e900ea6) |
| --- |

## [◆ ](#a4e92e3fbb4be682babbb6796af90b50f)pthread\_rwlockattr\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_rwlockattr\_t](#a4e92e3fbb4be682babbb6796af90b50f) |
| --- |

## [◆ ](#a1d9c308dd59bf38ff0a7a45020d0aefa)pthread\_spinlock\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_spinlock\_t](#a1d9c308dd59bf38ff0a7a45020d0aefa) |
| --- |

## [◆ ](#a405938c67e9c568fde9993c7e14d58ec)pthread\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_t](#a405938c67e9c568fde9993c7e14d58ec) = [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [pthread\_attr](structpthread__attr.md))) |
| --- |

## [◆ ](#afb4edc6a51d66a7a352424942b631a1e)sem\_t

| typedef struct k\_sem [sem\_t](#afb4edc6a51d66a7a352424942b631a1e) |
| --- |

## [◆ ](#aa37fa84abebf94371f0c8426c2fc614d)timer\_t

| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long [timer\_t](#aa37fa84abebf94371f0c8426c2fc614d) |
| --- |

## [◆ ](#a75bb141dc55bc89a8ddc565fd374e3d9)uid\_t

| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short [uid\_t](#a75bb141dc55bc89a8ddc565fd374e3d9) |
| --- |

## [◆ ](#a1cf3c794977f92f3ccf2e041a68f3342)useconds\_t

| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long [useconds\_t](#a1cf3c794977f92f3ccf2e041a68f3342) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [posix\_types.h](posix__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
