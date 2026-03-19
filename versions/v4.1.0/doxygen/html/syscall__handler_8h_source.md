---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/syscall__handler_8h_source.html
original_path: doxygen/html/syscall__handler_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall\_handler.h

[Go to the documentation of this file.](syscall__handler_8h.md)

1/\*

2 \* Copyright (c) 2017, Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_SYSCALL\_HANDLER\_H\_

7#define ZEPHYR\_INCLUDE\_SYSCALL\_HANDLER\_H\_

8

15

16#if defined(CONFIG\_USERSPACE) || defined(\_\_DOXYGEN\_\_)

17

18#ifndef \_ASMLANGUAGE

19#include <[zephyr/kernel.h](kernel_8h.md)>

20#include <[zephyr/arch/arch\_interface.h](arch__interface_8h.md)>

21#include <[zephyr/sys/math\_extras.h](math__extras_8h.md)>

22#include <[stdbool.h](stdbool_8h.md)>

23#include <[zephyr/logging/log.h](log_8h.md)>

24

25extern const \_k\_syscall\_handler\_t \_k\_syscall\_table[K\_SYSCALL\_LIMIT];

26

27enum \_obj\_init\_check {

28 \_OBJ\_INIT\_TRUE = 0,

29 \_OBJ\_INIT\_FALSE = -1,

30 \_OBJ\_INIT\_ANY = 1

31};

32

[ 57](group__syscall__apis.md#ga7a9fa19673bf4dfc27c741cc5c6f041c)static inline bool [k\_is\_in\_user\_syscall](group__syscall__apis.md#ga7a9fa19673bf4dfc27c741cc5c6f041c)(void)

58{

59 /\* This gets set on entry to the syscall's generated z\_mrsh

60 \* function and then cleared on exit. This code path is only

61 \* encountered when a syscall is made from user mode, system

62 \* calls from supervisor mode bypass everything directly to

63 \* the implementation function.

64 \*/

65 return ![k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)() && (\_current->syscall\_frame != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

66}

67

[ 92](group__syscall__apis.md#ga63f436a6ce6ea661f336b5e9e37b9a49)int [k\_object\_validate](group__syscall__apis.md#ga63f436a6ce6ea661f336b5e9e37b9a49)(struct [k\_object](structk__object.md) \*ko, enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype,

93 enum \_obj\_init\_check init);

94

[ 106](group__syscall__apis.md#gab480a9da8e883b1877266a32f03d9d46)void [k\_object\_dump\_error](group__syscall__apis.md#gab480a9da8e883b1877266a32f03d9d46)(int retval, const void \*obj,

107 struct [k\_object](structk__object.md) \*ko, enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype);

108

[ 122](group__syscall__apis.md#ga0d5a4ed3856e0e57c7953f2082ee6fca)struct [k\_object](structk__object.md) \*[k\_object\_find](group__syscall__apis.md#ga0d5a4ed3856e0e57c7953f2082ee6fca)(const void \*obj);

123

124typedef void (\*\_wordlist\_cb\_func\_t)(struct [k\_object](structk__object.md) \*ko, void \*context);

125

[ 135](group__syscall__apis.md#ga433a7f942497aa50e1258b3175074a35)void [k\_object\_wordlist\_foreach](group__syscall__apis.md#ga433a7f942497aa50e1258b3175074a35)(\_wordlist\_cb\_func\_t func, void \*context);

136

[ 146](group__syscall__apis.md#ga4ef1222d947e366df2071b0d39f4397f)void [k\_thread\_perms\_inherit](group__syscall__apis.md#ga4ef1222d947e366df2071b0d39f4397f)(struct [k\_thread](structk__thread.md) \*parent, struct [k\_thread](structk__thread.md) \*child);

147

[ 157](group__syscall__apis.md#ga14c6dccdc556cf4845c87bf0de53c594)void [k\_thread\_perms\_set](group__syscall__apis.md#ga14c6dccdc556cf4845c87bf0de53c594)(struct [k\_object](structk__object.md) \*ko, struct [k\_thread](structk__thread.md) \*thread);

158

[ 168](group__syscall__apis.md#ga10ac3b729614c50c96174eea35e4d48a)void [k\_thread\_perms\_clear](group__syscall__apis.md#ga10ac3b729614c50c96174eea35e4d48a)(struct [k\_object](structk__object.md) \*ko, struct [k\_thread](structk__thread.md) \*thread);

169

[ 181](group__syscall__apis.md#ga9cf6dc74c8220cb5a4f0844c0de4c0a5)void [k\_thread\_perms\_all\_clear](group__syscall__apis.md#ga9cf6dc74c8220cb5a4f0844c0de4c0a5)(struct [k\_thread](structk__thread.md) \*thread);

182

[ 194](group__syscall__apis.md#gac3f856ffbb8b780c5435106580690d04)void [k\_object\_uninit](group__syscall__apis.md#gac3f856ffbb8b780c5435106580690d04)(const void \*obj);

195

[ 215](group__syscall__apis.md#gac14f20707378454823500d5e0697d16e)void [k\_object\_recycle](group__syscall__apis.md#gac14f20707378454823500d5e0697d16e)(const void \*obj);

216

[ 242](group__syscall__apis.md#ga31d4ba17f1f77d5030110ff7f593c769)static inline size\_t [k\_usermode\_string\_nlen](group__syscall__apis.md#ga31d4ba17f1f77d5030110ff7f593c769)(const char \*src, size\_t maxlen,

243 int \*err)

244{

245 return [arch\_user\_string\_nlen](group__arch-userspace.md#ga174c4f356fe315c523cefbf513858c9c)(src, maxlen, err);

246}

247

[ 265](group__syscall__apis.md#ga203a8c900fed91585df7147e25e072eb)void \*[k\_usermode\_alloc\_from\_copy](group__syscall__apis.md#ga203a8c900fed91585df7147e25e072eb)(const void \*src, size\_t size);

266

[ 282](group__syscall__apis.md#ga931b212610371c3a288a16c158318501)int [k\_usermode\_from\_copy](group__syscall__apis.md#ga931b212610371c3a288a16c158318501)(void \*dst, const void \*src, size\_t size);

283

[ 299](group__syscall__apis.md#gaf454b8b7e076a9b9acd698b1ec2a6b79)int [k\_usermode\_to\_copy](group__syscall__apis.md#gaf454b8b7e076a9b9acd698b1ec2a6b79)(void \*dst, const void \*src, size\_t size);

300

[ 317](group__syscall__apis.md#ga32fef6a47062bf30a7ef8c6d58220887)char \*[k\_usermode\_string\_alloc\_copy](group__syscall__apis.md#ga32fef6a47062bf30a7ef8c6d58220887)(const char \*src, size\_t maxlen);

318

[ 337](group__syscall__apis.md#ga61cfc14e57e88b8d03dd7b2053f37dc4)int [k\_usermode\_string\_copy](group__syscall__apis.md#ga61cfc14e57e88b8d03dd7b2053f37dc4)(char \*dst, const char \*src, size\_t maxlen);

338

[ 350](group__syscall__apis.md#gadffbde0c37a4c192d8ce860943ef6181)#define K\_OOPS(expr) \

351 do { \

352 if (expr) { \

353 arch\_syscall\_oops(\_current->syscall\_frame); \

354 } \

355 } while (false)

356

[ 372](group__syscall__apis.md#gac1a9c494aa091d9e67e2bf4fb1113f53)#define K\_SYSCALL\_VERIFY\_MSG(expr, fmt, ...) ({ \

373 bool expr\_copy = !(expr); \

374 if (expr\_copy) { \

375 TOOLCHAIN\_IGNORE\_WSHADOW\_BEGIN \

376 LOG\_MODULE\_DECLARE(os, CONFIG\_KERNEL\_LOG\_LEVEL); \

377 TOOLCHAIN\_IGNORE\_WSHADOW\_END \

378 LOG\_ERR("syscall %s failed check: " fmt, \

379 \_\_func\_\_, ##\_\_VA\_ARGS\_\_); \

380 } \

381 expr\_copy; })

382

[ 395](group__syscall__apis.md#ga2b79503cd448a698e8a4ccb46a012b48)#define K\_SYSCALL\_VERIFY(expr) K\_SYSCALL\_VERIFY\_MSG(expr, #expr)

396

[ 410](group__syscall__apis.md#gaf7aacc0b779ad1b0aa739d7698b36963)#define K\_SYSCALL\_MEMORY\_SIZE\_CHECK(ptr, size) \

411 (((uintptr\_t)(ptr) + (size)) >= (uintptr\_t)(ptr))

412

[ 431](group__syscall__apis.md#gacd20e09824dc9124f339f06b49ca6f39)#define K\_SYSCALL\_MEMORY(ptr, size, write) \

432 K\_SYSCALL\_VERIFY\_MSG(K\_SYSCALL\_MEMORY\_SIZE\_CHECK(ptr, size) \

433 && !Z\_DETECT\_POINTER\_OVERFLOW(ptr, size) \

434 && (arch\_buffer\_validate((void \*)(ptr), (size), (write)) \

435 == 0), \

436 "Memory region %p (size %zu) %s access denied", \

437 (void \*)(ptr), (size\_t)(size), \

438 (write) ? "write" : "read")

439

[ 455](group__syscall__apis.md#ga964d979b84494266ffc360318732b537)#define K\_SYSCALL\_MEMORY\_READ(ptr, size) \

456 K\_SYSCALL\_MEMORY(ptr, size, 0)

457

[ 474](group__syscall__apis.md#ga5f6dfb5b3b2b6e75e164f42e127cea1a)#define K\_SYSCALL\_MEMORY\_WRITE(ptr, size) \

475 K\_SYSCALL\_MEMORY(ptr, size, 1)

476

[ 477](group__syscall__apis.md#gaac0e4ded775b724a809cdb9bf17803a8)#define K\_SYSCALL\_MEMORY\_ARRAY(ptr, nmemb, size, write) \

478 ({ \

479 size\_t product; \

480 K\_SYSCALL\_VERIFY\_MSG(!size\_mul\_overflow((size\_t)(nmemb), \

481 (size\_t)(size), \

482 &product), \

483 "%zux%zu array is too large", \

484 (size\_t)(nmemb), (size\_t)(size)) || \

485 K\_SYSCALL\_MEMORY(ptr, product, write); \

486 })

487

[ 502](group__syscall__apis.md#ga48a8ccdd4ff43b6fb3caa77956466dd1)#define K\_SYSCALL\_MEMORY\_ARRAY\_READ(ptr, nmemb, size) \

503 K\_SYSCALL\_MEMORY\_ARRAY(ptr, nmemb, size, 0)

504

[ 519](group__syscall__apis.md#ga6a1465208770d52a5c06de72ffda4421)#define K\_SYSCALL\_MEMORY\_ARRAY\_WRITE(ptr, nmemb, size) \

520 K\_SYSCALL\_MEMORY\_ARRAY(ptr, nmemb, size, 1)

521

[ 522](group__syscall__apis.md#gaaf711b2a214a341c0f2c1efaca78da5b)static inline int [k\_object\_validation\_check](group__syscall__apis.md#gaaf711b2a214a341c0f2c1efaca78da5b)(struct [k\_object](structk__object.md) \*ko,

523 const void \*obj,

524 enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype,

525 enum \_obj\_init\_check init)

526{

527 int ret;

528

529 ret = [k\_object\_validate](group__syscall__apis.md#ga63f436a6ce6ea661f336b5e9e37b9a49)(ko, otype, init);

530

531#ifdef CONFIG\_LOG

532 if (ret != 0) {

533 [k\_object\_dump\_error](group__syscall__apis.md#gab480a9da8e883b1877266a32f03d9d46)(ret, obj, ko, otype);

534 }

535#else

536 ARG\_UNUSED(obj);

537#endif

538

539 return ret;

540}

541

[ 542](group__syscall__apis.md#ga4292eb5dd4b4d54780eb1a93ce9f6a7b)#define K\_SYSCALL\_IS\_OBJ(ptr, type, init) \

543 K\_SYSCALL\_VERIFY\_MSG(k\_object\_validation\_check( \

544 k\_object\_find((const void \*)(ptr)), \

545 (const void \*)(ptr), \

546 (type), (init)) == 0, "access denied")

547

[ 562](group__syscall__apis.md#ga5113d697b1ec8615afa66771aeb91a4e)#define K\_SYSCALL\_DRIVER\_OP(ptr, api\_name, op) \

563 ({ \

564 struct api\_name \*\_\_device\_\_ = (struct api\_name \*) \

565 ((const struct device \*)(ptr))->api; \

566 K\_SYSCALL\_VERIFY\_MSG(\_\_device\_\_->op != NULL, \

567 "Operation %s not defined for driver " \

568 "instance %p", \

569 # op, \_\_device\_\_); \

570 })

571

[ 592](group__syscall__apis.md#ga1f5b938fc90bb11e2f8a200fe3b59730)#define K\_SYSCALL\_SPECIFIC\_DRIVER(\_device, \_dtype, \_api) \

593 ({ \

594 const struct device \*\_dev = (const struct device \*)\_device; \

595 K\_SYSCALL\_OBJ(\_dev, \_dtype) || \

596 K\_SYSCALL\_VERIFY\_MSG(\_dev->api == \_api, \

597 "API structure mismatch"); \

598 })

599

[ 613](group__syscall__apis.md#gaf1139c2c6044c5bb6da2bf901b5804c4)#define K\_SYSCALL\_OBJ(ptr, type) \

614 K\_SYSCALL\_IS\_OBJ(ptr, type, \_OBJ\_INIT\_TRUE)

615

628

[ 629](group__syscall__apis.md#ga54db53f239955f325e8b7e18f06589ca)#define K\_SYSCALL\_OBJ\_INIT(ptr, type) \

630 K\_SYSCALL\_IS\_OBJ(ptr, type, \_OBJ\_INIT\_ANY)

631

646

[ 647](group__syscall__apis.md#ga652457773cc6d45c2058183d374affe6)#define K\_SYSCALL\_OBJ\_NEVER\_INIT(ptr, type) \

648 K\_SYSCALL\_IS\_OBJ(ptr, type, \_OBJ\_INIT\_FALSE)

649

650#include <zephyr/driver-validation.h>

651

652#endif /\* \_ASMLANGUAGE \*/

653

654#endif /\* CONFIG\_USERSPACE \*/

658

659#endif /\* ZEPHYR\_INCLUDE\_SYSCALL\_HANDLER\_H\_ \*/

[arch\_interface.h](arch__interface_8h.md)

[arch\_user\_string\_nlen](group__arch-userspace.md#ga174c4f356fe315c523cefbf513858c9c)

size\_t arch\_user\_string\_nlen(const char \*s, size\_t maxsize, int \*err)

Safely take the length of a potentially bad string.

[k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)

bool k\_is\_in\_isr(void)

Determine if code is running at interrupt level.

[k\_object\_find](group__syscall__apis.md#ga0d5a4ed3856e0e57c7953f2082ee6fca)

struct k\_object \* k\_object\_find(const void \*obj)

Kernel object validation function.

[k\_thread\_perms\_clear](group__syscall__apis.md#ga10ac3b729614c50c96174eea35e4d48a)

void k\_thread\_perms\_clear(struct k\_object \*ko, struct k\_thread \*thread)

Revoke a thread's permission to a kernel object.

[k\_thread\_perms\_set](group__syscall__apis.md#ga14c6dccdc556cf4845c87bf0de53c594)

void k\_thread\_perms\_set(struct k\_object \*ko, struct k\_thread \*thread)

Grant a thread permission to a kernel object.

[k\_usermode\_alloc\_from\_copy](group__syscall__apis.md#ga203a8c900fed91585df7147e25e072eb)

void \* k\_usermode\_alloc\_from\_copy(const void \*src, size\_t size)

Copy data from userspace into a resource pool allocation.

[k\_usermode\_string\_nlen](group__syscall__apis.md#ga31d4ba17f1f77d5030110ff7f593c769)

static size\_t k\_usermode\_string\_nlen(const char \*src, size\_t maxlen, int \*err)

Obtain the size of a C string passed from user mode.

**Definition** syscall\_handler.h:242

[k\_usermode\_string\_alloc\_copy](group__syscall__apis.md#ga32fef6a47062bf30a7ef8c6d58220887)

char \* k\_usermode\_string\_alloc\_copy(const char \*src, size\_t maxlen)

Copy a C string from userspace into a resource pool allocation.

[k\_object\_wordlist\_foreach](group__syscall__apis.md#ga433a7f942497aa50e1258b3175074a35)

void k\_object\_wordlist\_foreach(\_wordlist\_cb\_func\_t func, void \*context)

Iterate over all the kernel object metadata in the system.

[k\_thread\_perms\_inherit](group__syscall__apis.md#ga4ef1222d947e366df2071b0d39f4397f)

void k\_thread\_perms\_inherit(struct k\_thread \*parent, struct k\_thread \*child)

Copy all kernel object permissions from the parent to the child.

[k\_usermode\_string\_copy](group__syscall__apis.md#ga61cfc14e57e88b8d03dd7b2053f37dc4)

int k\_usermode\_string\_copy(char \*dst, const char \*src, size\_t maxlen)

Copy a C string from userspace into a provided buffer.

[k\_object\_validate](group__syscall__apis.md#ga63f436a6ce6ea661f336b5e9e37b9a49)

int k\_object\_validate(struct k\_object \*ko, enum k\_objects otype, enum \_obj\_init\_check init)

Ensure a system object is a valid object of the expected type.

[k\_is\_in\_user\_syscall](group__syscall__apis.md#ga7a9fa19673bf4dfc27c741cc5c6f041c)

static bool k\_is\_in\_user\_syscall(void)

Return true if we are currently handling a system call from user mode.

**Definition** syscall\_handler.h:57

[k\_usermode\_from\_copy](group__syscall__apis.md#ga931b212610371c3a288a16c158318501)

int k\_usermode\_from\_copy(void \*dst, const void \*src, size\_t size)

Copy data from user mode.

[k\_thread\_perms\_all\_clear](group__syscall__apis.md#ga9cf6dc74c8220cb5a4f0844c0de4c0a5)

void k\_thread\_perms\_all\_clear(struct k\_thread \*thread)

Revoke access to all objects for the provided thread.

[k\_object\_validation\_check](group__syscall__apis.md#gaaf711b2a214a341c0f2c1efaca78da5b)

static int k\_object\_validation\_check(struct k\_object \*ko, const void \*obj, enum k\_objects otype, enum \_obj\_init\_check init)

**Definition** syscall\_handler.h:522

[k\_object\_dump\_error](group__syscall__apis.md#gab480a9da8e883b1877266a32f03d9d46)

void k\_object\_dump\_error(int retval, const void \*obj, struct k\_object \*ko, enum k\_objects otype)

Dump out error information on failed k\_object\_validate() call.

[k\_object\_recycle](group__syscall__apis.md#gac14f20707378454823500d5e0697d16e)

void k\_object\_recycle(const void \*obj)

Initialize and reset permissions to only access by the caller.

[k\_object\_uninit](group__syscall__apis.md#gac3f856ffbb8b780c5435106580690d04)

void k\_object\_uninit(const void \*obj)

Clear initialization state of a kernel object.

[k\_usermode\_to\_copy](group__syscall__apis.md#gaf454b8b7e076a9b9acd698b1ec2a6b79)

int k\_usermode\_to\_copy(void \*dst, const void \*src, size\_t size)

Copy data to user mode.

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[kernel.h](kernel_8h.md)

Public kernel APIs.

[k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1)

k\_objects

Kernel Object Types.

**Definition** kobject.h:30

[log.h](log_8h.md)

[math\_extras.h](math__extras_8h.md)

[stdbool.h](stdbool_8h.md)

[k\_object](structk__object.md)

Table generated by gperf, these objects are retrieved via k\_object\_find().

**Definition** kobject\_internal.h:61

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [internal](dir_72eb1b59a003155cd0b9b947ac16180e.md)
- [syscall\_handler.h](syscall__handler_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
