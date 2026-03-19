---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/obj__core_8h.html
original_path: doxygen/html/obj__core_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

obj\_core.h File Reference

`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](obj__core_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [k\_obj\_core\_stats\_desc](structk__obj__core__stats__desc.md) |
|  | Object core statistics descriptor. [More...](structk__obj__core__stats__desc.md#details) |
| struct | [k\_obj\_type](structk__obj__type.md) |
|  | Object type structure. [More...](structk__obj__type.md#details) |
| struct | [k\_obj\_core](structk__obj__core.md) |
|  | Object core structure. [More...](structk__obj__core.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_OBJ\_CORE](group__obj__core__apis.md#ga2bd0c2c121afc09448926a3648c7d814)(kobj) |
|  | Convert kernel object pointer into its object core pointer. |
| #define | [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Generate new object type IDs based on a 4 letter string. |
| #define | [K\_OBJ\_TYPE\_CONDVAR\_ID](group__obj__core__apis.md#gab8d2838ae8064facda465bb9db88e948)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("COND") |
|  | Condition variable object type. |
| #define | [K\_OBJ\_TYPE\_CPU\_ID](group__obj__core__apis.md#ga59c569e93e1301903618fa0c53f642ec)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("CPU\_") |
|  | CPU object type. |
| #define | [K\_OBJ\_TYPE\_EVENT\_ID](group__obj__core__apis.md#gac6fdf29f93b81f4a868ce39f3ae50c8c)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("EVNT") |
|  | Event object type. |
| #define | [K\_OBJ\_TYPE\_FIFO\_ID](group__obj__core__apis.md#ga4eadc00416f1da919c5f49fea028b79f)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("FIFO") |
|  | FIFO object type. |
| #define | [K\_OBJ\_TYPE\_KERNEL\_ID](group__obj__core__apis.md#gad2b7452f304d6e27c612941a578cc651)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("KRNL") |
|  | Kernel object type. |
| #define | [K\_OBJ\_TYPE\_LIFO\_ID](group__obj__core__apis.md#ga956d61f2af839077adeb67ccd2e15d28)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("LIFO") |
|  | LIFO object type. |
| #define | [K\_OBJ\_TYPE\_MEM\_BLOCK\_ID](group__obj__core__apis.md#ga83a03cfe8485b3e005ea2dc20a291115)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("MBLK") |
|  | Memory block object type. |
| #define | [K\_OBJ\_TYPE\_MBOX\_ID](group__obj__core__apis.md#ga6ee0890bc9e22a381440a3e156c54f2e)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("MBOX") |
|  | Mailbox object type. |
| #define | [K\_OBJ\_TYPE\_MEM\_SLAB\_ID](group__obj__core__apis.md#ga0d84b7ac3f48e2e2d0fcd3bfbeed2519)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("SLAB") |
|  | Memory slab object type. |
| #define | [K\_OBJ\_TYPE\_MSGQ\_ID](group__obj__core__apis.md#ga8bf245e4f25c61bb4ec8267b15384feb)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("MSGQ") |
|  | Message queue object type. |
| #define | [K\_OBJ\_TYPE\_MUTEX\_ID](group__obj__core__apis.md#gab109845d59689ce64523786ccce9b8c6)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("MUTX") |
|  | Mutex object type. |
| #define | [K\_OBJ\_TYPE\_PIPE\_ID](group__obj__core__apis.md#ga36eb538a1bd7f8454a9da42de170d2a9)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("PIPE") |
|  | Pipe object type. |
| #define | [K\_OBJ\_TYPE\_SEM\_ID](group__obj__core__apis.md#gad08de0f2f76ad2fe368ed82524bd8335)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("SEM4") |
|  | Semaphore object type. |
| #define | [K\_OBJ\_TYPE\_STACK\_ID](group__obj__core__apis.md#gacb41863cbd89368e1204080e6f7f14c2)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("STCK") |
|  | Stack object type. |
| #define | [K\_OBJ\_TYPE\_THREAD\_ID](group__obj__core__apis.md#gaf7adb45984ccfb2bbe64b1f8e559f24b)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("THRD") |
|  | Thread object type. |
| #define | [K\_OBJ\_TYPE\_TIMER\_ID](group__obj__core__apis.md#ga583ff6ce85756d9aa1b2baf7ac19574f)   [K\_OBJ\_TYPE\_ID\_GEN](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)("TIMR") |
|  | Timer object type. |

| Functions | |
| --- | --- |
| struct [k\_obj\_type](structk__obj__type.md) \* | [k\_obj\_type\_find](group__obj__core__apis.md#ga325c21774af7d3f092dcab17d8f260fd) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type\_id) |
|  | Find a specific object type by ID. |
| int | [k\_obj\_type\_walk\_locked](group__obj__core__apis.md#ga1e9a331ca6f3f7bf1f0e3b144b964b9b) (struct [k\_obj\_type](structk__obj__type.md) \*type, int(\*func)(struct [k\_obj\_core](structk__obj__core.md) \*, void \*), void \*data) |
|  | Walk the object type's list of object cores. |
| int | [k\_obj\_type\_walk\_unlocked](group__obj__core__apis.md#ga4d3da7db72063699b66a54e56cf75e2e) (struct [k\_obj\_type](structk__obj__type.md) \*type, int(\*func)(struct [k\_obj\_core](structk__obj__core.md) \*, void \*), void \*data) |
|  | Walk the object type's list of object cores. |
| void | [k\_obj\_core\_init](group__obj__core__apis.md#gaf00bc2c3bfa0420f00fe5bf49796b3a0) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, struct [k\_obj\_type](structk__obj__type.md) \*type) |
|  | Initialize the core of the kernel object. |
| void | [k\_obj\_core\_link](group__obj__core__apis.md#ga6b4a21304216582d7cc16088b00e69bf) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Link the kernel object to the kernel object type list. |
| void | [k\_obj\_core\_init\_and\_link](group__obj__core__apis.md#gab1563101ae5f163fcbc06dc17660f9bc) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, struct [k\_obj\_type](structk__obj__type.md) \*type) |
|  | Automatically link the kernel object after initializing it. |
| void | [k\_obj\_core\_unlink](group__obj__core__apis.md#ga7cb5b22d776880313c91a14583bb5d62) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Unlink the kernel object from the kernel object type list. |
| int | [k\_obj\_core\_stats\_register](group__obj__core__stats__apis.md#gae3fda75cf0b9e3c91bfb5ba57239621d) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stats\_len) |
|  | Register kernel object for gathering statistics. |
| int | [k\_obj\_core\_stats\_deregister](group__obj__core__stats__apis.md#gab2b23cf62d89e0bc21d89a0b77b01a21) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Deregister kernel object from gathering statistics. |
| int | [k\_obj\_core\_stats\_raw](group__obj__core__stats__apis.md#ga9c5f91bd221b9086ccaea7347ac357ab) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stats\_len) |
|  | Retrieve the raw statistics associated with the kernel object. |
| int | [k\_obj\_core\_stats\_query](group__obj__core__stats__apis.md#ga52afc700fb116acfaa4dd5e1ca49a782) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stats\_len) |
|  | Retrieve the statistics associated with the kernel object. |
| int | [k\_obj\_core\_stats\_reset](group__obj__core__stats__apis.md#ga0b4d2270e968e2c694290c0f90f208c4) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Reset the stats associated with the kernel object. |
| int | [k\_obj\_core\_stats\_disable](group__obj__core__stats__apis.md#ga547b121e75aeafc2f54dba2d58ca62db) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Stop gathering the stats associated with the kernel object. |
| int | [k\_obj\_core\_stats\_enable](group__obj__core__stats__apis.md#ga079df60c5ba6dd08a2270362490553fa) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Reset the stats associated with the kernel object. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [obj\_core.h](obj__core_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
