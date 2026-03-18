---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__syscall__apis.html
original_path: doxygen/html/group__syscall__apis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

User mode and Syscall APIs

[Internal and System API](group__internal__api.md)

User mode and Syscall APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [K\_OOPS](#gadffbde0c37a4c192d8ce860943ef6181)(expr) |
|  | Induce a kernel oops. |
| #define | [K\_SYSCALL\_VERIFY\_MSG](#gac1a9c494aa091d9e67e2bf4fb1113f53)(expr, fmt, ...) |
|  | Runtime expression check for system call arguments. |
| #define | [K\_SYSCALL\_VERIFY](#ga2b79503cd448a698e8a4ccb46a012b48)(expr) |
|  | Runtime expression check for system call arguments. |
| #define | [K\_SYSCALL\_MEMORY\_SIZE\_CHECK](#gaf7aacc0b779ad1b0aa739d7698b36963)(ptr, size) |
|  | Macro to check if size is negative. |
| #define | [K\_SYSCALL\_MEMORY](#gacd20e09824dc9124f339f06b49ca6f39)(ptr, size, write) |
|  | Runtime check that a user thread has read and/or write permission to a memory area. |
| #define | [K\_SYSCALL\_MEMORY\_READ](#ga964d979b84494266ffc360318732b537)(ptr, size) |
|  | Runtime check that a user thread has read permission to a memory area. |
| #define | [K\_SYSCALL\_MEMORY\_WRITE](#ga5f6dfb5b3b2b6e75e164f42e127cea1a)(ptr, size) |
|  | Runtime check that a user thread has write permission to a memory area. |
| #define | [K\_SYSCALL\_MEMORY\_ARRAY](#gaac0e4ded775b724a809cdb9bf17803a8)(ptr, nmemb, size, write) |
| #define | [K\_SYSCALL\_MEMORY\_ARRAY\_READ](#ga48a8ccdd4ff43b6fb3caa77956466dd1)(ptr, nmemb, size) |
|  | Validate user thread has read permission for sized array. |
| #define | [K\_SYSCALL\_MEMORY\_ARRAY\_WRITE](#ga6a1465208770d52a5c06de72ffda4421)(ptr, nmemb, size) |
|  | Validate user thread has read/write permission for sized array. |
| #define | [K\_SYSCALL\_IS\_OBJ](#ga4292eb5dd4b4d54780eb1a93ce9f6a7b)(ptr, type, init) |
| #define | [K\_SYSCALL\_DRIVER\_OP](#ga5113d697b1ec8615afa66771aeb91a4e)(ptr, api\_name, op) |
|  | Runtime check driver object pointer for presence of operation. |
| #define | [K\_SYSCALL\_SPECIFIC\_DRIVER](#ga1f5b938fc90bb11e2f8a200fe3b59730)(\_device, \_dtype, \_api) |
|  | Runtime check that device object is of a specific driver type. |
| #define | [K\_SYSCALL\_OBJ](#gaf1139c2c6044c5bb6da2bf901b5804c4)(ptr, type) |
|  | Runtime check kernel object pointer for non-init functions. |
| #define | [K\_SYSCALL\_OBJ\_INIT](#ga54db53f239955f325e8b7e18f06589ca)(ptr, type) |
|  | Runtime check kernel object pointer for non-init functions. |
| #define | [K\_SYSCALL\_OBJ\_NEVER\_INIT](#ga652457773cc6d45c2058183d374affe6)(ptr, type) |
|  | Runtime check kernel object pointer for non-init functions. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_is\_in\_user\_syscall](#ga7a9fa19673bf4dfc27c741cc5c6f041c) (void) |
|  | Return true if we are currently handling a system call from user mode. |
| int | [k\_object\_validate](#ga63f436a6ce6ea661f336b5e9e37b9a49) (struct [k\_object](structk__object.md) \*ko, enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype, enum \_obj\_init\_check init) |
|  | Ensure a system object is a valid object of the expected type. |
| void | [k\_object\_dump\_error](#gab480a9da8e883b1877266a32f03d9d46) (int retval, const void \*obj, struct [k\_object](structk__object.md) \*ko, enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype) |
|  | Dump out error information on failed [k\_object\_validate()](#ga63f436a6ce6ea661f336b5e9e37b9a49) call. |
| struct [k\_object](structk__object.md) \* | [k\_object\_find](#ga0d5a4ed3856e0e57c7953f2082ee6fca) (const void \*obj) |
|  | Kernel object validation function. |
| void | [k\_object\_wordlist\_foreach](#ga433a7f942497aa50e1258b3175074a35) (\_wordlist\_cb\_func\_t func, void \*context) |
|  | Iterate over all the kernel object metadata in the system. |
| void | [k\_thread\_perms\_inherit](#ga4ef1222d947e366df2071b0d39f4397f) (struct [k\_thread](structk__thread.md) \*parent, struct [k\_thread](structk__thread.md) \*child) |
|  | Copy all kernel object permissions from the parent to the child. |
| void | [k\_thread\_perms\_set](#ga14c6dccdc556cf4845c87bf0de53c594) (struct [k\_object](structk__object.md) \*ko, struct [k\_thread](structk__thread.md) \*thread) |
|  | Grant a thread permission to a kernel object. |
| void | [k\_thread\_perms\_clear](#ga10ac3b729614c50c96174eea35e4d48a) (struct [k\_object](structk__object.md) \*ko, struct [k\_thread](structk__thread.md) \*thread) |
|  | Revoke a thread's permission to a kernel object. |
| void | [k\_thread\_perms\_all\_clear](#ga9cf6dc74c8220cb5a4f0844c0de4c0a5) (struct [k\_thread](structk__thread.md) \*thread) |
|  | Revoke access to all objects for the provided thread. |
| void | [k\_object\_uninit](#gac3f856ffbb8b780c5435106580690d04) (const void \*obj) |
|  | Clear initialization state of a kernel object. |
| void | [k\_object\_recycle](#gac14f20707378454823500d5e0697d16e) (const void \*obj) |
|  | Initialize and reset permissions to only access by the caller. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [k\_usermode\_string\_nlen](#ga31d4ba17f1f77d5030110ff7f593c769) (const char \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) maxlen, int \*err) |
|  | Obtain the size of a C string passed from user mode. |
| void \* | [k\_usermode\_alloc\_from\_copy](#ga203a8c900fed91585df7147e25e072eb) (const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Copy data from userspace into a resource pool allocation. |
| int | [k\_usermode\_from\_copy](#ga931b212610371c3a288a16c158318501) (void \*dst, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Copy data from user mode. |
| int | [k\_usermode\_to\_copy](#gaf454b8b7e076a9b9acd698b1ec2a6b79) (void \*dst, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Copy data to user mode. |
| char \* | [k\_usermode\_string\_alloc\_copy](#ga32fef6a47062bf30a7ef8c6d58220887) (const char \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) maxlen) |
|  | Copy a C string from userspace into a resource pool allocation. |
| int | [k\_usermode\_string\_copy](#ga61cfc14e57e88b8d03dd7b2053f37dc4) (char \*dst, const char \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) maxlen) |
|  | Copy a C string from userspace into a provided buffer. |
| static int | [k\_object\_validation\_check](#gaaf711b2a214a341c0f2c1efaca78da5b) (struct [k\_object](structk__object.md) \*ko, const void \*obj, enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype, enum \_obj\_init\_check init) |

## Detailed Description

User mode and Syscall APIs.

## Macro Definition Documentation

## [◆ ](#gadffbde0c37a4c192d8ce860943ef6181)K\_OOPS

| #define K\_OOPS | ( |  | *expr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

do { \

if (expr) { \

arch\_syscall\_oops(\_current->syscall\_frame); \

} \

} while (false)

Induce a kernel oops.

This macro can be used to induce a kernel oops which will kill the calling thread.

Parameters
:   | expr | Expression to be evaluated |
    | --- | --- |

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga5113d697b1ec8615afa66771aeb91a4e)K\_SYSCALL\_DRIVER\_OP

| #define K\_SYSCALL\_DRIVER\_OP | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *api\_name*, |
|  |  |  | *op* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

({ \

struct api\_name \*\_\_device\_\_ = (struct api\_name \*) \

((const struct [device](structdevice.md) \*)(ptr))->api; \

K\_SYSCALL\_VERIFY\_MSG(\_\_device\_\_->op != NULL, \

"Operation %s not defined for driver " \

"instance %p", \

# op, \_\_device\_\_); \

})

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

Runtime check driver object pointer for presence of operation.

Validates if the driver object is capable of performing a certain operation.

Parameters
:   | ptr | Untrusted device instance object pointer |
    | --- | --- |
    | api\_name | Name of the driver API struct (e.g. gpio\_driver\_api) |
    | op | Driver operation (e.g. manage\_callback) |

Returns
:   0 on success, nonzero on failure

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga4292eb5dd4b4d54780eb1a93ce9f6a7b)K\_SYSCALL\_IS\_OBJ

| #define K\_SYSCALL\_IS\_OBJ | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *type*, |
|  |  |  | *init* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

[K\_SYSCALL\_VERIFY\_MSG](#gac1a9c494aa091d9e67e2bf4fb1113f53)([k\_object\_validation\_check](#gaaf711b2a214a341c0f2c1efaca78da5b)( \

[k\_object\_find](#ga0d5a4ed3856e0e57c7953f2082ee6fca)((const void \*)(ptr)), \

(const void \*)(ptr), \

(type), (init)) == 0, "access denied")

[k\_object\_find](#ga0d5a4ed3856e0e57c7953f2082ee6fca)

struct k\_object \* k\_object\_find(const void \*obj)

Kernel object validation function.

[k\_object\_validation\_check](#gaaf711b2a214a341c0f2c1efaca78da5b)

static int k\_object\_validation\_check(struct k\_object \*ko, const void \*obj, enum k\_objects otype, enum \_obj\_init\_check init)

**Definition** syscall\_handler.h:522

[K\_SYSCALL\_VERIFY\_MSG](#gac1a9c494aa091d9e67e2bf4fb1113f53)

#define K\_SYSCALL\_VERIFY\_MSG(expr, fmt,...)

Runtime expression check for system call arguments.

**Definition** syscall\_handler.h:372

## [◆ ](#gacd20e09824dc9124f339f06b49ca6f39)K\_SYSCALL\_MEMORY

| #define K\_SYSCALL\_MEMORY | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *size*, |
|  |  |  | *write* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

[K\_SYSCALL\_VERIFY\_MSG](#gac1a9c494aa091d9e67e2bf4fb1113f53)([K\_SYSCALL\_MEMORY\_SIZE\_CHECK](#gaf7aacc0b779ad1b0aa739d7698b36963)(ptr, size) \

&& !Z\_DETECT\_POINTER\_OVERFLOW(ptr, size) \

&& ([arch\_buffer\_validate](group__arch-userspace.md#ga13053a9233b86d5cd19dc3cea5804a16)((void \*)(ptr), (size), (write)) \

== 0), \

"Memory region %p (size %zu) %s access denied", \

(void \*)(ptr), (size\_t)(size), \

(write) ? "write" : "read")

[arch\_buffer\_validate](group__arch-userspace.md#ga13053a9233b86d5cd19dc3cea5804a16)

int arch\_buffer\_validate(const void \*addr, size\_t size, int write)

Check memory region permissions.

[K\_SYSCALL\_MEMORY\_SIZE\_CHECK](#gaf7aacc0b779ad1b0aa739d7698b36963)

#define K\_SYSCALL\_MEMORY\_SIZE\_CHECK(ptr, size)

Macro to check if size is negative.

**Definition** syscall\_handler.h:410

Runtime check that a user thread has read and/or write permission to a memory area.

Checks that the particular memory area is readable and/or writeable by the currently running thread if the CPU was in user mode, and generates a kernel oops if it wasn't. Prevents userspace from getting the kernel to read and/or modify memory the thread does not have access to, or passing in garbage pointers that would crash/pagefault the kernel if dereferenced.

Parameters
:   | ptr | Memory area to examine |
    | --- | --- |
    | size | Size of the memory area |
    | write | If the thread should be able to write to this memory, not just read it |

Returns
:   0 on success, nonzero on failure

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#gaac0e4ded775b724a809cdb9bf17803a8)K\_SYSCALL\_MEMORY\_ARRAY

| #define K\_SYSCALL\_MEMORY\_ARRAY | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *nmemb*, |
|  |  |  | *size*, |
|  |  |  | *write* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

({ \

size\_t product; \

K\_SYSCALL\_VERIFY\_MSG(![size\_mul\_overflow](group__math__extras.md#ga790b24a5d239afcc08d9e4f66c25ea56)((size\_t)(nmemb), \

(size\_t)(size), \

&product), \

"%zux%zu array is too large", \

(size\_t)(nmemb), (size\_t)(size)) || \

K\_SYSCALL\_MEMORY(ptr, product, write); \

})

[size\_mul\_overflow](group__math__extras.md#ga790b24a5d239afcc08d9e4f66c25ea56)

static bool size\_mul\_overflow(size\_t a, size\_t b, size\_t \*result)

Multiply two size\_t integers.

## [◆ ](#ga48a8ccdd4ff43b6fb3caa77956466dd1)K\_SYSCALL\_MEMORY\_ARRAY\_READ

| #define K\_SYSCALL\_MEMORY\_ARRAY\_READ | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *nmemb*, |
|  |  |  | *size* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

[K\_SYSCALL\_MEMORY\_ARRAY](#gaac0e4ded775b724a809cdb9bf17803a8)(ptr, nmemb, size, 0)

[K\_SYSCALL\_MEMORY\_ARRAY](#gaac0e4ded775b724a809cdb9bf17803a8)

#define K\_SYSCALL\_MEMORY\_ARRAY(ptr, nmemb, size, write)

**Definition** syscall\_handler.h:477

Validate user thread has read permission for sized array.

Used when the memory region is expressed in terms of number of elements and each element size, handles any overflow issues with computing the total array bounds. Otherwise see \_SYSCALL\_MEMORY\_READ.

Parameters
:   | ptr | Memory area to examine |
    | --- | --- |
    | nmemb | Number of elements in the array |
    | size | Size of each array element |

Returns
:   0 on success, nonzero on failure

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga6a1465208770d52a5c06de72ffda4421)K\_SYSCALL\_MEMORY\_ARRAY\_WRITE

| #define K\_SYSCALL\_MEMORY\_ARRAY\_WRITE | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *nmemb*, |
|  |  |  | *size* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

[K\_SYSCALL\_MEMORY\_ARRAY](#gaac0e4ded775b724a809cdb9bf17803a8)(ptr, nmemb, size, 1)

Validate user thread has read/write permission for sized array.

Used when the memory region is expressed in terms of number of elements and each element size, handles any overflow issues with computing the total array bounds. Otherwise see \_SYSCALL\_MEMORY\_WRITE.

Parameters
:   | ptr | Memory area to examine |
    | --- | --- |
    | nmemb | Number of elements in the array |
    | size | Size of each array element |

Returns
:   0 on success, nonzero on failure

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga964d979b84494266ffc360318732b537)K\_SYSCALL\_MEMORY\_READ

| #define K\_SYSCALL\_MEMORY\_READ | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

[K\_SYSCALL\_MEMORY](#gacd20e09824dc9124f339f06b49ca6f39)(ptr, size, 0)

[K\_SYSCALL\_MEMORY](#gacd20e09824dc9124f339f06b49ca6f39)

#define K\_SYSCALL\_MEMORY(ptr, size, write)

Runtime check that a user thread has read and/or write permission to a memory area.

**Definition** syscall\_handler.h:431

Runtime check that a user thread has read permission to a memory area.

Checks that the particular memory area is readable by the currently running thread if the CPU was in user mode, and generates a kernel oops if it wasn't. Prevents userspace from getting the kernel to read memory the thread does not have access to, or passing in garbage pointers that would crash/pagefault the kernel if dereferenced.

Parameters
:   | ptr | Memory area to examine |
    | --- | --- |
    | size | Size of the memory area |

Returns
:   0 on success, nonzero on failure

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#gaf7aacc0b779ad1b0aa739d7698b36963)K\_SYSCALL\_MEMORY\_SIZE\_CHECK

| #define K\_SYSCALL\_MEMORY\_SIZE\_CHECK | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

((([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))(ptr) + (size)) >= ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))(ptr))

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

Macro to check if size is negative.

K\_SYSCALL\_MEMORY can be called with signed/unsigned types and because of that if we check if size is greater or equal to zero, many static analyzers complain about no effect expression.

Parameters
:   | ptr | Memory area to examine |
    | --- | --- |
    | size | Size of the memory area |

Returns
:   true if size is valid, false otherwise

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga5f6dfb5b3b2b6e75e164f42e127cea1a)K\_SYSCALL\_MEMORY\_WRITE

| #define K\_SYSCALL\_MEMORY\_WRITE | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

[K\_SYSCALL\_MEMORY](#gacd20e09824dc9124f339f06b49ca6f39)(ptr, size, 1)

Runtime check that a user thread has write permission to a memory area.

Checks that the particular memory area is readable and writable by the currently running thread if the CPU was in user mode, and generates a kernel oops if it wasn't. Prevents userspace from getting the kernel to read or modify memory the thread does not have access to, or passing in garbage pointers that would crash/pagefault the kernel if dereferenced.

Parameters
:   | ptr | Memory area to examine |
    | --- | --- |
    | size | Size of the memory area |

Returns
:   0 on success, nonzero on failure

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#gaf1139c2c6044c5bb6da2bf901b5804c4)K\_SYSCALL\_OBJ

| #define K\_SYSCALL\_OBJ | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *type* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

[K\_SYSCALL\_IS\_OBJ](#ga4292eb5dd4b4d54780eb1a93ce9f6a7b)(ptr, type, \_OBJ\_INIT\_TRUE)

[K\_SYSCALL\_IS\_OBJ](#ga4292eb5dd4b4d54780eb1a93ce9f6a7b)

#define K\_SYSCALL\_IS\_OBJ(ptr, type, init)

**Definition** syscall\_handler.h:542

Runtime check kernel object pointer for non-init functions.

Calls k\_object\_validate and triggers a kernel oops if the check fails. For use in system call handlers which are not init functions; a fatal error will occur if the object is not initialized.

Parameters
:   | ptr | Untrusted kernel object pointer |
    | --- | --- |
    | type | Expected kernel object type |

Returns
:   0 on success, nonzero on failure

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga54db53f239955f325e8b7e18f06589ca)K\_SYSCALL\_OBJ\_INIT

| #define K\_SYSCALL\_OBJ\_INIT | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *type* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

[K\_SYSCALL\_IS\_OBJ](#ga4292eb5dd4b4d54780eb1a93ce9f6a7b)(ptr, type, \_OBJ\_INIT\_ANY)

Runtime check kernel object pointer for non-init functions.

See description of \_SYSCALL\_IS\_OBJ. No initialization checks are done. Intended for init functions where objects may be re-initialized at will.

Parameters
:   | ptr | Untrusted kernel object pointer |
    | --- | --- |
    | type | Expected kernel object type |

Returns
:   0 on success, nonzero on failure

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga652457773cc6d45c2058183d374affe6)K\_SYSCALL\_OBJ\_NEVER\_INIT

| #define K\_SYSCALL\_OBJ\_NEVER\_INIT | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *type* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

[K\_SYSCALL\_IS\_OBJ](#ga4292eb5dd4b4d54780eb1a93ce9f6a7b)(ptr, type, \_OBJ\_INIT\_FALSE)

Runtime check kernel object pointer for non-init functions.

See description of \_SYSCALL\_IS\_OBJ. Triggers a fatal error if the object is initialized. Intended for init functions where objects, once initialized, can only be re-used when their initialization state expires due to some other mechanism.

Parameters
:   | ptr | Untrusted kernel object pointer |
    | --- | --- |
    | type | Expected kernel object type |

Returns
:   0 on success, nonzero on failure

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga1f5b938fc90bb11e2f8a200fe3b59730)K\_SYSCALL\_SPECIFIC\_DRIVER

| #define K\_SYSCALL\_SPECIFIC\_DRIVER | ( |  | *\_device*, |
| --- | --- | --- | --- |
|  |  |  | *\_dtype*, |
|  |  |  | *\_api* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

({ \

const struct [device](structdevice.md) \*\_dev = (const struct [device](structdevice.md) \*)\_device; \

K\_SYSCALL\_OBJ(\_dev, \_dtype) || \

K\_SYSCALL\_VERIFY\_MSG(\_dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d) == \_api, \

"API structure mismatch"); \

})

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

Runtime check that device object is of a specific driver type.

Checks that the driver object passed in is initialized, the caller has correct permissions, and that it belongs to the specified driver subsystems. Additionally, all devices store a structure pointer of the driver's API. If this doesn't match the value provided, the check will fail.

This provides an easy way to determine if a device object not only belongs to a particular subsystem, but is of a specific device driver implementation. Useful for defining out-of-subsystem system calls which are implemented for only one driver.

Parameters
:   | \_device | Untrusted device pointer |
    | --- | --- |
    | \_dtype | Expected kernel object type for the provided device pointer |
    | \_api | Expected driver API structure memory address |

Returns
:   0 on success, nonzero on failure

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga2b79503cd448a698e8a4ccb46a012b48)K\_SYSCALL\_VERIFY

| #define K\_SYSCALL\_VERIFY | ( |  | *expr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

[K\_SYSCALL\_VERIFY\_MSG](#gac1a9c494aa091d9e67e2bf4fb1113f53)(expr, #expr)

Runtime expression check for system call arguments.

Used in handler functions to perform various runtime checks on arguments, and generate a kernel oops if anything is not expected.

Parameters
:   | expr | Boolean expression to verify, a false result will trigger an oops. A stringified version of this expression will be printed. |
    | --- | --- |

Returns
:   0 on success, nonzero on failure

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#gac1a9c494aa091d9e67e2bf4fb1113f53)K\_SYSCALL\_VERIFY\_MSG

| #define K\_SYSCALL\_VERIFY\_MSG | ( |  | *expr*, |
| --- | --- | --- | --- |
|  |  |  | *fmt*, |
|  |  |  | ... ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

**Value:**

({ \

bool expr\_copy = !(expr); \

if (expr\_copy) { \

TOOLCHAIN\_IGNORE\_WSHADOW\_BEGIN \

LOG\_MODULE\_DECLARE(os, CONFIG\_KERNEL\_LOG\_LEVEL); \

TOOLCHAIN\_IGNORE\_WSHADOW\_END \

LOG\_ERR("syscall %s failed check: " fmt, \

\_\_func\_\_, ##\_\_VA\_ARGS\_\_); \

} \

expr\_copy; })

Runtime expression check for system call arguments.

Used in handler functions to perform various runtime checks on arguments, and generate a kernel oops if anything is not expected, printing a custom message.

Parameters
:   | expr | Boolean expression to verify, a false result will trigger an oops |
    | --- | --- |
    | fmt | Printf-style format string (followed by appropriate variadic arguments) to print on verification failure |

Returns
:   False on success, True on failure

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## Function Documentation

## [◆ ](#ga7a9fa19673bf4dfc27c741cc5c6f041c)k\_is\_in\_user\_syscall()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_is\_in\_user\_syscall | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Return true if we are currently handling a system call from user mode.

Inside z\_vrfy functions, we always know that we are handling a system call invoked from user context.

However, some checks that are only relevant to user mode must instead be placed deeper within the implementation. This API is useful to conditionally make these checks.

For performance reasons, whenever possible, checks should be placed in the relevant z\_vrfy function since these are completely skipped when a syscall is invoked.

This will return true only if we are handling a syscall for a user thread. If the system call was invoked from supervisor mode, or we are not handling a system call, this will return false.

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

Returns
:   whether the current context is handling a syscall for a user mode thread

## [◆ ](#gab480a9da8e883b1877266a32f03d9d46)k\_object\_dump\_error()

| void k\_object\_dump\_error | ( | int | *retval*, |
| --- | --- | --- | --- |
|  |  | const void \* | *obj*, |
|  |  | struct [k\_object](structk__object.md) \* | *ko*, |
|  |  | enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) | *otype* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Dump out error information on failed [k\_object\_validate()](#ga63f436a6ce6ea661f336b5e9e37b9a49) call.

Parameters
:   | retval | Return value from [k\_object\_validate()](#ga63f436a6ce6ea661f336b5e9e37b9a49) |
    | --- | --- |
    | obj | Kernel object we were trying to verify |
    | ko | If retval=-EPERM, struct [k\_object](structk__object.md "Table generated by gperf, these objects are retrieved via k_object_find().") \* that was looked up, or NULL |
    | otype | Expected type of the kernel object |

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga0d5a4ed3856e0e57c7953f2082ee6fca)k\_object\_find()

| struct [k\_object](structk__object.md) \* k\_object\_find | ( | const void \* | *obj* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Kernel object validation function.

Retrieve metadata for a kernel object. This function is implemented in the gperf script footer, see gen\_kobject\_list.py

Parameters
:   | obj | Address of kernel object to get metadata |
    | --- | --- |

Returns
:   Kernel object's metadata, or NULL if the parameter wasn't the memory address of a kernel object

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#gac14f20707378454823500d5e0697d16e)k\_object\_recycle()

| void k\_object\_recycle | ( | const void \* | *obj* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Initialize and reset permissions to only access by the caller.

Intended for scenarios where objects are fetched from slab pools and may have had different permissions set during prior usage.

This is only intended for pools of objects, where such objects are acquired and released to the pool. If an object has already been used, we do not want stale permission information hanging around, the object should only have permissions on the caller. Objects which are not managed by a pool-like mechanism should not use this API.

The object will be marked as initialized and the calling thread granted access to it.

Parameters
:   | obj | Address of the kernel object |
    | --- | --- |

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#gac3f856ffbb8b780c5435106580690d04)k\_object\_uninit()

| void k\_object\_uninit | ( | const void \* | *obj* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Clear initialization state of a kernel object.

Intended for thread objects upon thread exit, or for other kernel objects that were released back to an object pool.

Parameters
:   | obj | Address of the kernel object |
    | --- | --- |

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga63f436a6ce6ea661f336b5e9e37b9a49)k\_object\_validate()

| int k\_object\_validate | ( | struct [k\_object](structk__object.md) \* | *ko*, |
| --- | --- | --- | --- |
|  |  | enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) | *otype*, |
|  |  | enum \_obj\_init\_check | *init* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Ensure a system object is a valid object of the expected type.

Searches for the object and ensures that it is indeed an object of the expected type, that the caller has the right permissions on it, and that the object has been initialized.

This function is intended to be called on the kernel-side system call handlers to validate kernel object pointers passed in from userspace.

Parameters
:   | ko | Kernel object metadata pointer, or NULL |
    | --- | --- |
    | otype | Expected type of the kernel object, or K\_OBJ\_ANY if type doesn't matter |
    | init | Indicate whether the object needs to already be in initialized or uninitialized state, or that we don't care |

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

Returns
:   0 If the object is valid -EBADF if not a valid object of the specified type -EPERM If the caller does not have permissions -EINVAL Object is not initialized

## [◆ ](#gaaf711b2a214a341c0f2c1efaca78da5b)k\_object\_validation\_check()

| | int k\_object\_validation\_check | ( | struct [k\_object](structk__object.md) \* | *ko*, | | --- | --- | --- | --- | |  |  | const void \* | *obj*, | |  |  | enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) | *otype*, | |  |  | enum \_obj\_init\_check | *init* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

## [◆ ](#ga433a7f942497aa50e1258b3175074a35)k\_object\_wordlist\_foreach()

| void k\_object\_wordlist\_foreach | ( | \_wordlist\_cb\_func\_t | *func*, |
| --- | --- | --- | --- |
|  |  | void \* | *context* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Iterate over all the kernel object metadata in the system.

Parameters
:   | func | function to run on each struct [k\_object](structk__object.md "Table generated by gperf, these objects are retrieved via k_object_find().") |
    | --- | --- |
    | context | Context pointer to pass to each invocation |

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga9cf6dc74c8220cb5a4f0844c0de4c0a5)k\_thread\_perms\_all\_clear()

| void k\_thread\_perms\_all\_clear | ( | struct [k\_thread](structk__thread.md) \* | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Revoke access to all objects for the provided thread.

Note
:   Unlike [k\_thread\_perms\_clear()](#ga10ac3b729614c50c96174eea35e4d48a), this function will not clear permissions on public objects.
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

Parameters
:   | thread | Thread object to revoke access |
    | --- | --- |

## [◆ ](#ga10ac3b729614c50c96174eea35e4d48a)k\_thread\_perms\_clear()

| void k\_thread\_perms\_clear | ( | struct [k\_object](structk__object.md) \* | *ko*, |
| --- | --- | --- | --- |
|  |  | struct [k\_thread](structk__thread.md) \* | *thread* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Revoke a thread's permission to a kernel object.

Parameters
:   | ko | Kernel object metadata to update |
    | --- | --- |
    | thread | The thread to grant permission |

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga4ef1222d947e366df2071b0d39f4397f)k\_thread\_perms\_inherit()

| void k\_thread\_perms\_inherit | ( | struct [k\_thread](structk__thread.md) \* | *parent*, |
| --- | --- | --- | --- |
|  |  | struct [k\_thread](structk__thread.md) \* | *child* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Copy all kernel object permissions from the parent to the child.

Parameters
:   | parent | Parent thread, to get permissions from |
    | --- | --- |
    | child | Child thread, to copy permissions to |

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga14c6dccdc556cf4845c87bf0de53c594)k\_thread\_perms\_set()

| void k\_thread\_perms\_set | ( | struct [k\_object](structk__object.md) \* | *ko*, |
| --- | --- | --- | --- |
|  |  | struct [k\_thread](structk__thread.md) \* | *thread* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Grant a thread permission to a kernel object.

Parameters
:   | ko | Kernel object metadata to update |
    | --- | --- |
    | thread | The thread to grant permission |

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga203a8c900fed91585df7147e25e072eb)k\_usermode\_alloc\_from\_copy()

| void \* k\_usermode\_alloc\_from\_copy | ( | const void \* | *src*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Copy data from userspace into a resource pool allocation.

Given a pointer and a size, allocate a similarly sized buffer in the caller's resource pool and copy all the data within it to the newly allocated buffer. This will need to be freed later with [k\_free()](group__heap__apis.md#ga79b63cc93b3358cf82d74f40e73b69d5 "Free memory allocated from heap.").

Checks are done to ensure that the current thread would have read access to the provided buffer.

Parameters
:   | src | Source memory address |
    | --- | --- |
    | size | Size of the memory buffer |

Returns
:   An allocated buffer with the data copied within it, or NULL if some error condition occurred

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga931b212610371c3a288a16c158318501)k\_usermode\_from\_copy()

| int k\_usermode\_from\_copy | ( | void \* | *dst*, |
| --- | --- | --- | --- |
|  |  | const void \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Copy data from user mode.

Given a userspace pointer and a size, copies data from it into a provided destination buffer, performing checks to ensure that the caller would have appropriate access when in user mode.

Parameters
:   | dst | Destination memory buffer |
    | --- | --- |
    | src | Source memory buffer, in userspace |
    | size | Number of bytes to copy |

Return values
:   | 0 | On success |
    | --- | --- |
    | [EFAULT](group__system__errno.md#ga3f317946e043623f9d6b93dbf60e6316 "Bad address.") | On memory access error |

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga32fef6a47062bf30a7ef8c6d58220887)k\_usermode\_string\_alloc\_copy()

| char \* k\_usermode\_string\_alloc\_copy | ( | const char \* | *src*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *maxlen* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Copy a C string from userspace into a resource pool allocation.

Given a C string and maximum length, duplicate the string using an allocation from the calling thread's resource pool. This will need to be freed later with [k\_free()](group__heap__apis.md#ga79b63cc93b3358cf82d74f40e73b69d5 "Free memory allocated from heap.").

Checks are performed to ensure that the string is valid memory and that the caller has access to it in user mode.

Parameters
:   | src | Source string pointer, in userspace |
    | --- | --- |
    | maxlen | Maximum size of the string including trailing NULL |

Returns
:   The duplicated string, or NULL if an error occurred.

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga61cfc14e57e88b8d03dd7b2053f37dc4)k\_usermode\_string\_copy()

| int k\_usermode\_string\_copy | ( | char \* | *dst*, |
| --- | --- | --- | --- |
|  |  | const char \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *maxlen* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Copy a C string from userspace into a provided buffer.

Given a C string and maximum length, copy the string into a buffer.

Checks are performed to ensure that the string is valid memory and that the caller has access to it in user mode.

Parameters
:   | dst | Destination buffer |
    | --- | --- |
    | src | Source string pointer, in userspace |
    | maxlen | Maximum size of the string including trailing NULL |

Return values
:   | 0 | on success |
    | --- | --- |
    | [EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4 "Invalid argument.") | if the source string is too long with respect to maxlen |
    | [EFAULT](group__system__errno.md#ga3f317946e043623f9d6b93dbf60e6316 "Bad address.") | On memory access error |

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#ga31d4ba17f1f77d5030110ff7f593c769)k\_usermode\_string\_nlen()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_usermode\_string\_nlen | ( | const char \* | *src*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *maxlen*, | |  |  | int \* | *err* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Obtain the size of a C string passed from user mode.

Given a C string pointer and a maximum size, obtain the true size of the string (not including the trailing NULL byte) just as if calling [strnlen()](string_8h.md#afc92d2231e45d19988c7894aa2a07f0c) on it, with the same semantics of [strnlen()](string_8h.md#afc92d2231e45d19988c7894aa2a07f0c) with respect to the return value and the maxlen parameter.

Any memory protection faults triggered by the examination of the string will be safely handled and an error code returned.

NOTE: Doesn't guarantee that user mode has actual access to this string, you will need to still do a [K\_SYSCALL\_MEMORY\_READ()](#ga964d979b84494266ffc360318732b537) with the obtained size value to guarantee this.

Parameters
:   | src | String to measure size of |
    | --- | --- |
    | maxlen | Maximum number of characters to examine |
    | err | Pointer to int, filled in with -1 on memory error, 0 on success |

Returns
:   undefined on error, or strlen(src) if that is less than maxlen, or maxlen if there were no NULL terminating characters within the first maxlen bytes.

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

## [◆ ](#gaf454b8b7e076a9b9acd698b1ec2a6b79)k\_usermode\_to\_copy()

| int k\_usermode\_to\_copy | ( | void \* | *dst*, |
| --- | --- | --- | --- |
|  |  | const void \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[syscall_handler.h](syscall__handler_8h.md)>`

Copy data to user mode.

Given a userspace pointer and a size, copies data to it from a provided source buffer, performing checks to ensure that the caller would have appropriate access when in user mode.

Parameters
:   | dst | Destination memory buffer, in userspace |
    | --- | --- |
    | src | Source memory buffer |
    | size | Number of bytes to copy |

Return values
:   | 0 | On success |
    | --- | --- |
    | [EFAULT](group__system__errno.md#ga3f317946e043623f9d6b93dbf60e6316 "Bad address.") | On memory access error |

Note
:   This is an internal API. Do not use unless you are extending functionality in the Zephyr tree.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
