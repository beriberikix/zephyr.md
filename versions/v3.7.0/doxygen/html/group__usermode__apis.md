---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__usermode__apis.html
original_path: doxygen/html/group__usermode__apis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

User Mode APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [K\_THREAD\_ACCESS\_GRANT](#ga6a2dae4c6dc6959d8785ff1924b1b424)(name\_, ...) |
|  | Grant a static thread access to a list of kernel objects. |
| #define | [K\_OBJ\_FLAG\_INITIALIZED](#ga1418482d67c7964855570fd0ac79628d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Object initialized. |
| #define | [K\_OBJ\_FLAG\_PUBLIC](#ga8892f9343266ec24abf25e29f3f6bc9b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Object is Public. |
| #define | [K\_OBJ\_FLAG\_ALLOC](#ga1bf7c8c1d5fe0a7358dd70c4663a5a7a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Object allocated. |
| #define | [K\_OBJ\_FLAG\_DRIVER](#ga82d3a7242074db70130415201d3d0fd6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Driver Object. |

| Functions | |
| --- | --- |
| void | [k\_object\_access\_grant](#ga94087bedf96fe2a2bea437d3d585ca22) (const void \*object, struct [k\_thread](structk__thread.md) \*thread) |
|  | Grant a thread access to a kernel object. |
| void | [k\_object\_access\_revoke](#gab70fe65497da1347cc4b7bf7ca2daf22) (const void \*object, struct [k\_thread](structk__thread.md) \*thread) |
|  | Revoke a thread's access to a kernel object. |
| void | [k\_object\_release](#ga3cb1a024c0178918def2dd0186e565b3) (const void \*object) |
|  | Release an object. |
| void | [k\_object\_access\_all\_grant](#gababc731e98a6378323c0d633b2abaa6a) (const void \*object) |
|  | Grant all present and future threads access to an object. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_object\_is\_valid](#gaacd9b4b517db99b3b027dd717e6746b4) (const void \*obj, enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype) |
|  | Check if a kernel object is of certain type and is valid. |
| void \* | [k\_object\_alloc](#ga5bba3a354fbc63673c76c9815db40812) (enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype) |
|  | Allocate a kernel object of a designated type. |
| void \* | [k\_object\_alloc\_size](#gab99a640325f14a6505a85218dcba5446) (enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate a kernel object of a designated type and a given size. |
| void | [k\_object\_free](#ga9cc15e8fd7df9cb81c3d7b6c79917aab) (void \*obj) |
|  | Free a kernel object previously allocated with [k\_object\_alloc()](#ga5bba3a354fbc63673c76c9815db40812). |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga1bf7c8c1d5fe0a7358dd70c4663a5a7a)K\_OBJ\_FLAG\_ALLOC

| #define K\_OBJ\_FLAG\_ALLOC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[kobject.h](kobject_8h.md)>`

Object allocated.

## [◆ ](#ga82d3a7242074db70130415201d3d0fd6)K\_OBJ\_FLAG\_DRIVER

| #define K\_OBJ\_FLAG\_DRIVER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[kobject.h](kobject_8h.md)>`

Driver Object.

## [◆ ](#ga1418482d67c7964855570fd0ac79628d)K\_OBJ\_FLAG\_INITIALIZED

| #define K\_OBJ\_FLAG\_INITIALIZED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[kobject.h](kobject_8h.md)>`

Object initialized.

## [◆ ](#ga8892f9343266ec24abf25e29f3f6bc9b)K\_OBJ\_FLAG\_PUBLIC

| #define K\_OBJ\_FLAG\_PUBLIC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[kobject.h](kobject_8h.md)>`

Object is Public.

## [◆ ](#ga6a2dae4c6dc6959d8785ff1924b1b424)K\_THREAD\_ACCESS\_GRANT

| #define K\_THREAD\_ACCESS\_GRANT | ( |  | *name\_*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[kobject.h](kobject_8h.md)>`

**Value:**

static void \* const \_CONCAT(\_object\_list\_, name\_)[] = \

{ \_\_VA\_ARGS\_\_, NULL }; \

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([k\_object\_assignment](structk__object__assignment.md), \

\_CONCAT(\_object\_access\_, name\_)) = \

{ (&\_k\_thread\_obj\_ ## name\_), \

(\_CONCAT(\_object\_list\_, name\_)) }

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[k\_object\_assignment](structk__object__assignment.md)

**Definition** kobject\_internal.h:69

Grant a static thread access to a list of kernel objects.

For threads declared with [K\_THREAD\_DEFINE()](group__thread__apis.md#gab3ced58648ca35788a40676e8478ecd2 "Statically define and initialize a thread."), grant the thread access to a set of kernel objects. These objects do not need to be in an initialized state. The permissions will be granted when the threads are initialized in the early boot sequence.

All arguments beyond the first must be pointers to kernel objects.

Parameters
:   | name\_ | Name of the thread, as passed to [K\_THREAD\_DEFINE()](group__thread__apis.md#gab3ced58648ca35788a40676e8478ecd2 "Statically define and initialize a thread.") |
    | --- | --- |

## Function Documentation

## [◆ ](#gababc731e98a6378323c0d633b2abaa6a)k\_object\_access\_all\_grant()

| void k\_object\_access\_all\_grant | ( | const void \* | *object* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kobject.h](kobject_8h.md)>`

Grant all present and future threads access to an object.

If the caller is from supervisor mode, or the caller is from user mode and have sufficient permissions on the object, then that object will have permissions granted to it for *all* current and future threads running in the system, effectively becoming a public kernel object.

Use of this API should be avoided on systems that are running untrusted code as it is possible for such code to derive the addresses of kernel objects and perform unwanted operations on them.

It is not possible to revoke permissions on public objects; once public, any thread may use it.

Parameters
:   | object | Address of kernel object |
    | --- | --- |

## [◆ ](#ga94087bedf96fe2a2bea437d3d585ca22)k\_object\_access\_grant()

| void k\_object\_access\_grant | ( | const void \* | *object*, |
| --- | --- | --- | --- |
|  |  | struct [k\_thread](structk__thread.md) \* | *thread* ) |

`#include <[kobject.h](kobject_8h.md)>`

Grant a thread access to a kernel object.

The thread will be granted access to the object if the caller is from supervisor mode, or the caller is from user mode AND has permissions on both the object and the thread whose access is being granted.

Parameters
:   | object | Address of kernel object |
    | --- | --- |
    | thread | Thread to grant access to the object |

## [◆ ](#gab70fe65497da1347cc4b7bf7ca2daf22)k\_object\_access\_revoke()

| void k\_object\_access\_revoke | ( | const void \* | *object*, |
| --- | --- | --- | --- |
|  |  | struct [k\_thread](structk__thread.md) \* | *thread* ) |

`#include <[kobject.h](kobject_8h.md)>`

Revoke a thread's access to a kernel object.

The thread will lose access to the object if the caller is from supervisor mode, or the caller is from user mode AND has permissions on both the object and the thread whose access is being revoked.

Parameters
:   | object | Address of kernel object |
    | --- | --- |
    | thread | Thread to remove access to the object |

## [◆ ](#ga5bba3a354fbc63673c76c9815db40812)k\_object\_alloc()

| void \* k\_object\_alloc | ( | enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) | *otype* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kobject.h](kobject_8h.md)>`

Allocate a kernel object of a designated type.

This will instantiate at runtime a kernel object of the specified type, returning a pointer to it. The object will be returned in an uninitialized state, with the calling thread being granted permission on it. The memory for the object will be allocated out of the calling thread's resource pool.

Note
:   This function is available only if `CONFIG_DYNAMIC_OBJECTS` is selected.
:   Thread stack object has to use [k\_object\_alloc\_size()](#gab99a640325f14a6505a85218dcba5446) since stacks may have different sizes.

Parameters
:   | otype | Requested kernel object type |
    | --- | --- |

Returns
:   A pointer to the allocated kernel object, or NULL if memory wasn't available

## [◆ ](#gab99a640325f14a6505a85218dcba5446)k\_object\_alloc\_size()

| void \* k\_object\_alloc\_size | ( | enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) | *otype*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[kobject.h](kobject_8h.md)>`

Allocate a kernel object of a designated type and a given size.

This will instantiate at runtime a kernel object of the specified type, returning a pointer to it. The object will be returned in an uninitialized state, with the calling thread being granted permission on it. The memory for the object will be allocated out of the calling thread's resource pool.

This function is specially helpful for thread stack objects because their sizes can vary. Other objects should probably look [k\_object\_alloc()](#ga5bba3a354fbc63673c76c9815db40812).

Note
:   This function is available only if `CONFIG_DYNAMIC_OBJECTS` is selected.

Parameters
:   | otype | Requested kernel object type |
    | --- | --- |
    | size | Requested kernel object size |

Returns
:   A pointer to the allocated kernel object, or NULL if memory wasn't available

## [◆ ](#ga9cc15e8fd7df9cb81c3d7b6c79917aab)k\_object\_free()

| void k\_object\_free | ( | void \* | *obj* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kobject.h](kobject_8h.md)>`

Free a kernel object previously allocated with [k\_object\_alloc()](#ga5bba3a354fbc63673c76c9815db40812).

This will return memory for a kernel object back to resource pool it was allocated from. Care must be exercised that the object will not be used during or after when this call is made.

Note
:   This function is available only if `CONFIG_DYNAMIC_OBJECTS` is selected.

Parameters
:   | obj | Pointer to the kernel object memory address. |
    | --- | --- |

## [◆ ](#gaacd9b4b517db99b3b027dd717e6746b4)k\_object\_is\_valid()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_object\_is\_valid | ( | const void \* | *obj*, |
| --- | --- | --- | --- |
|  |  | enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) | *otype* ) |

`#include <[kobject.h](kobject_8h.md)>`

Check if a kernel object is of certain type and is valid.

This checks if the kernel object exists, of certain type, and has been initialized.

Parameters
:   | obj | Address of the kernel object |
    | --- | --- |
    | otype | Object type (use K\_OBJ\_ANY for ignoring type checking) |

Returns
:   True if kernel object (*obj*) exists, of certain type, and has been initialized. False otherwise.

## [◆ ](#ga3cb1a024c0178918def2dd0186e565b3)k\_object\_release()

| void k\_object\_release | ( | const void \* | *object* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kobject.h](kobject_8h.md)>`

Release an object.

Allows user threads to drop their own permission on an object Their permissions are automatically cleared when a thread terminates.

Parameters
:   | object | The object to be released |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
