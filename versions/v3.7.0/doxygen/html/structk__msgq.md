---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structk__msgq.html
original_path: doxygen/html/structk__msgq.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_msgq Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Message Queue APIs](group__msgq__apis.md)

Message Queue Structure.
[More...](#details)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| \_wait\_q\_t | [wait\_q](#ae3b3d53d60b789d69c65494cfd090076) |
|  | Message queue wait queue. |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#aa2e00a7292502f0de88cff28c5e375f0) |
|  | Lock. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [msg\_size](#a512fe468da96540639a0d71f1707f79d) |
|  | Message size. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_msgs](#aebd3b6e91e97b2d4369feea1a3f7b7a0) |
|  | Maximal number of messages. |
| char \* | [buffer\_start](#aca77f1cf833d3aa27ae65004b446bdd2) |
|  | Start of message buffer. |
| char \* | [buffer\_end](#a9d47fd25d7a70e8518d45dd48c51f0e0) |
|  | End of message buffer. |
| char \* | [read\_ptr](#a594e8a4a638521f42f24f85fe0742d64) |
|  | Read pointer. |
| char \* | [write\_ptr](#aacf9b7b9f6e26e402f3752fc56834f23) |
|  | Write pointer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [used\_msgs](#a5c0cc83eaaf44d7fd7de8fffc7b2f857) |
|  | Number of used messages. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#ae03025420908f8342ce12a1395c7657b) |
|  | Message queue. |

## Detailed Description

Message Queue Structure.

## Field Documentation

## [◆ ](#a9d47fd25d7a70e8518d45dd48c51f0e0)buffer\_end

| char\* k\_msgq::buffer\_end |
| --- |

End of message buffer.

## [◆ ](#aca77f1cf833d3aa27ae65004b446bdd2)buffer\_start

| char\* k\_msgq::buffer\_start |
| --- |

Start of message buffer.

## [◆ ](#ae03025420908f8342ce12a1395c7657b)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) k\_msgq::flags |
| --- |

Message queue.

## [◆ ](#aa2e00a7292502f0de88cff28c5e375f0)lock

| struct [k\_spinlock](structk__spinlock.md) k\_msgq::lock |
| --- |

Lock.

## [◆ ](#aebd3b6e91e97b2d4369feea1a3f7b7a0)max\_msgs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_msgq::max\_msgs |
| --- |

Maximal number of messages.

## [◆ ](#a512fe468da96540639a0d71f1707f79d)msg\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_msgq::msg\_size |
| --- |

Message size.

## [◆ ](#a594e8a4a638521f42f24f85fe0742d64)read\_ptr

| char\* k\_msgq::read\_ptr |
| --- |

Read pointer.

## [◆ ](#a5c0cc83eaaf44d7fd7de8fffc7b2f857)used\_msgs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_msgq::used\_msgs |
| --- |

Number of used messages.

## [◆ ](#ae3b3d53d60b789d69c65494cfd090076)wait\_q

| \_wait\_q\_t k\_msgq::wait\_q |
| --- |

Message queue wait queue.

## [◆ ](#aacf9b7b9f6e26e402f3752fc56834f23)write\_ptr

| char\* k\_msgq::write\_ptr |
| --- |

Write pointer.

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_msgq](structk__msgq.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
