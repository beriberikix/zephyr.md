---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/syscall__handler_8h.html
original_path: doxygen/html/syscall__handler_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall\_handler.h File Reference

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/sys/arch_interface.h](arch__interface_8h_source.md)>`  
`#include <[zephyr/sys/math_extras.h](math__extras_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/logging/log.h](log_8h_source.md)>`  
`#include <driver-validation.h>`

[Go to the source code of this file.](syscall__handler_8h_source.md)

| Macros | |
| --- | --- |
| #define | [K\_OOPS](group__syscall__apis.md#gadffbde0c37a4c192d8ce860943ef6181)(expr) |
|  | Induce a kernel oops. |
| #define | [K\_SYSCALL\_VERIFY\_MSG](group__syscall__apis.md#gac1a9c494aa091d9e67e2bf4fb1113f53)(expr, fmt, ...) |
|  | Runtime expression check for system call arguments. |
| #define | [K\_SYSCALL\_VERIFY](group__syscall__apis.md#ga2b79503cd448a698e8a4ccb46a012b48)(expr) |
|  | Runtime expression check for system call arguments. |
| #define | [K\_SYSCALL\_MEMORY\_SIZE\_CHECK](group__syscall__apis.md#gaf7aacc0b779ad1b0aa739d7698b36963)(ptr, size) |
|  | Macro to check if size is negative. |
| #define | [K\_SYSCALL\_MEMORY](group__syscall__apis.md#gacd20e09824dc9124f339f06b49ca6f39)(ptr, size, write) |
|  | Runtime check that a user thread has read and/or write permission to a memory area. |
| #define | [K\_SYSCALL\_MEMORY\_READ](group__syscall__apis.md#ga964d979b84494266ffc360318732b537)(ptr, size) |
|  | Runtime check that a user thread has read permission to a memory area. |
| #define | [K\_SYSCALL\_MEMORY\_WRITE](group__syscall__apis.md#ga5f6dfb5b3b2b6e75e164f42e127cea1a)(ptr, size) |
|  | Runtime check that a user thread has write permission to a memory area. |
| #define | [K\_SYSCALL\_MEMORY\_ARRAY](group__syscall__apis.md#gaac0e4ded775b724a809cdb9bf17803a8)(ptr, nmemb, size, write) |
| #define | [K\_SYSCALL\_MEMORY\_ARRAY\_READ](group__syscall__apis.md#ga48a8ccdd4ff43b6fb3caa77956466dd1)(ptr, nmemb, size) |
|  | Validate user thread has read permission for sized array. |
| #define | [K\_SYSCALL\_MEMORY\_ARRAY\_WRITE](group__syscall__apis.md#ga6a1465208770d52a5c06de72ffda4421)(ptr, nmemb, size) |
|  | Validate user thread has read/write permission for sized array. |
| #define | [K\_SYSCALL\_IS\_OBJ](group__syscall__apis.md#ga4292eb5dd4b4d54780eb1a93ce9f6a7b)(ptr, type, init) |
| #define | [K\_SYSCALL\_DRIVER\_OP](group__syscall__apis.md#ga5113d697b1ec8615afa66771aeb91a4e)(ptr, api\_name, op) |
|  | Runtime check driver object pointer for presence of operation. |
| #define | [K\_SYSCALL\_SPECIFIC\_DRIVER](group__syscall__apis.md#ga1f5b938fc90bb11e2f8a200fe3b59730)(\_device, \_dtype, \_api) |
|  | Runtime check that device object is of a specific driver type. |
| #define | [K\_SYSCALL\_OBJ](group__syscall__apis.md#gaf1139c2c6044c5bb6da2bf901b5804c4)(ptr, type) |
|  | Runtime check kernel object pointer for non-init functions. |
| #define | [K\_SYSCALL\_OBJ\_INIT](group__syscall__apis.md#ga54db53f239955f325e8b7e18f06589ca)(ptr, type) |
|  | Runtime check kernel object pointer for non-init functions. |
| #define | [K\_SYSCALL\_OBJ\_NEVER\_INIT](group__syscall__apis.md#ga652457773cc6d45c2058183d374affe6)(ptr, type) |
|  | Runtime check kernel object pointer for non-init functions. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_is\_in\_user\_syscall](group__syscall__apis.md#ga7a9fa19673bf4dfc27c741cc5c6f041c) (void) |
|  | Return true if we are currently handling a system call from user mode. |
| int | [k\_object\_validate](group__syscall__apis.md#ga63f436a6ce6ea661f336b5e9e37b9a49) (struct [k\_object](structk__object.md) \*ko, enum [k\_objects](include_2zephyr_2sys_2kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype, enum \_obj\_init\_check init) |
|  | Ensure a system object is a valid object of the expected type. |
| void | [k\_object\_dump\_error](group__syscall__apis.md#gab480a9da8e883b1877266a32f03d9d46) (int retval, const void \*obj, struct [k\_object](structk__object.md) \*ko, enum [k\_objects](include_2zephyr_2sys_2kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype) |
|  | Dump out error information on failed [k\_object\_validate()](group__syscall__apis.md#ga63f436a6ce6ea661f336b5e9e37b9a49 "Ensure a system object is a valid object of the expected type.") call. |
| struct [k\_object](structk__object.md) \* | [k\_object\_find](group__syscall__apis.md#ga0d5a4ed3856e0e57c7953f2082ee6fca) (const void \*obj) |
|  | Kernel object validation function. |
| void | [k\_object\_wordlist\_foreach](group__syscall__apis.md#ga433a7f942497aa50e1258b3175074a35) (\_wordlist\_cb\_func\_t func, void \*context) |
|  | Iterate over all the kernel object metadata in the system. |
| void | [k\_thread\_perms\_inherit](group__syscall__apis.md#ga4ef1222d947e366df2071b0d39f4397f) (struct [k\_thread](structk__thread.md) \*parent, struct [k\_thread](structk__thread.md) \*child) |
|  | Copy all kernel object permissions from the parent to the child. |
| void | [k\_thread\_perms\_set](group__syscall__apis.md#ga14c6dccdc556cf4845c87bf0de53c594) (struct [k\_object](structk__object.md) \*ko, struct [k\_thread](structk__thread.md) \*thread) |
|  | Grant a thread permission to a kernel object. |
| void | [k\_thread\_perms\_clear](group__syscall__apis.md#ga10ac3b729614c50c96174eea35e4d48a) (struct [k\_object](structk__object.md) \*ko, struct [k\_thread](structk__thread.md) \*thread) |
|  | Revoke a thread's permission to a kernel object. |
| void | [k\_thread\_perms\_all\_clear](group__syscall__apis.md#ga9cf6dc74c8220cb5a4f0844c0de4c0a5) (struct [k\_thread](structk__thread.md) \*thread) |
|  | Revoke access to all objects for the provided thread. |
| void | [k\_object\_uninit](group__syscall__apis.md#gac3f856ffbb8b780c5435106580690d04) (const void \*obj) |
|  | Clear initialization state of a kernel object. |
| void | [k\_object\_recycle](group__syscall__apis.md#gac14f20707378454823500d5e0697d16e) (const void \*obj) |
|  | Initialize and reset permissions to only access by the caller. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [k\_usermode\_string\_nlen](group__syscall__apis.md#ga31d4ba17f1f77d5030110ff7f593c769) (const char \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) maxlen, int \*err) |
|  | Obtain the size of a C string passed from user mode. |
| void \* | [k\_usermode\_alloc\_from\_copy](group__syscall__apis.md#ga203a8c900fed91585df7147e25e072eb) (const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Copy data from userspace into a resource pool allocation. |
| int | [k\_usermode\_from\_copy](group__syscall__apis.md#ga931b212610371c3a288a16c158318501) (void \*dst, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Copy data from user mode. |
| int | [k\_usermode\_to\_copy](group__syscall__apis.md#gaf454b8b7e076a9b9acd698b1ec2a6b79) (void \*dst, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Copy data to user mode. |
| char \* | [k\_usermode\_string\_alloc\_copy](group__syscall__apis.md#ga32fef6a47062bf30a7ef8c6d58220887) (const char \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) maxlen) |
|  | Copy a C string from userspace into a resource pool allocation. |
| int | [k\_usermode\_string\_copy](group__syscall__apis.md#ga61cfc14e57e88b8d03dd7b2053f37dc4) (char \*dst, const char \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) maxlen) |
|  | Copy a C string from userspace into a provided buffer. |
| static int | [k\_object\_validation\_check](group__syscall__apis.md#gaaf711b2a214a341c0f2c1efaca78da5b) (struct [k\_object](structk__object.md) \*ko, const void \*obj, enum [k\_objects](include_2zephyr_2sys_2kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype, enum \_obj\_init\_check init) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [internal](dir_72eb1b59a003155cd0b9b947ac16180e.md)
- [syscall\_handler.h](syscall__handler_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
