---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/usermode/kernelobjects.html
original_path: kernel/usermode/kernelobjects.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Kernel Objects

A kernel object can be one of three classes of data:

- A core kernel object, such as a semaphore, thread, pipe, etc.
- A thread stack, which is an array of `z_thread_stack_element`
  and declared with [`K_THREAD_STACK_DEFINE()`](../services/threads/index.md#c.K_THREAD_STACK_DEFINE "K_THREAD_STACK_DEFINE")
- A device driver instance (const struct device) that belongs to one of a defined
  set of subsystems

The set of known kernel objects and driver subsystems is defined in
include/kernel.h as `k_objects`.

Kernel objects are completely opaque to user threads. User threads work
with addresses to kernel objects when making API calls, but may never
dereference these addresses, doing so will cause a memory protection fault.
All kernel objects must be placed in memory that is not accessible by
user threads.

Since user threads may not directly manipulate kernel objects, all use of
them must go through system calls. In order to perform a system call on
a kernel object, checks are performed by system call handler functions
that the kernel object address is valid and that the calling thread
has sufficient permissions to work with it.

Permission on an object also has the semantics of a reference to an object.
This is significant for certain object APIs which do temporary allocations,
or objects which themselves have been allocated from a runtime memory pool.

If an object loses all references, two events may happen:

- If the object has an associated cleanup function, the cleanup function
  may be called to release any runtime-allocated buffers the object was using.
- If the object itself was dynamically allocated, the memory for the object
  will be freed.

## Object Placement

Kernel objects that are only used by supervisor threads have no restrictions
and can be located anywhere in the binary, or even declared on stacks. However,
to prevent accidental or intentional corruption by user threads, they must
not be located in any memory that user threads have direct access to.

In order for a static kernel object to be usable by a user thread via system
call APIs, several conditions must be met on how the kernel object is declared:

- The object must be declared as a top-level global at build time, such that it
  appears in the ELF symbol table. It is permitted to declare kernel objects
  with static scope. The post-build script [scripts/build/gen\_kobject\_list.py](../../build/cmake/index.md#gen-kobject-list-py) scans the
  generated ELF file to find kernel objects and places their memory addresses
  in a special table of kernel object metadata. Kernel objects may be members
  of arrays or embedded within other data structures.
- Kernel objects must be located in memory reserved for the kernel. They
  must not be located in any memory partitions that are user-accessible.
- Any memory reserved for a kernel object must be used exclusively for that
  object. Kernel objects may not be members of a union data type.

Kernel objects that are found but do not meet the above conditions will not be
included in the generated table that is used to validate kernel object pointers
passed in from user mode.

The debug output of the [scripts/build/gen\_kobject\_list.py](../../build/cmake/index.md#gen-kobject-list-py) script may be useful when
debugging why some object was unexpectedly not being tracked. This
information will be printed if the script is run with the `--verbose` flag,
or if the build system is invoked with verbose output.

## Dynamic Objects

Kernel objects may also be allocated at runtime if
[`CONFIG_DYNAMIC_OBJECTS`](../../kconfig.md#CONFIG_DYNAMIC_OBJECTS "CONFIG_DYNAMIC_OBJECTS") is enabled. In this case, the
[`k_object_alloc()`](#c.k_object_alloc) API may be used to instantiate an object from
the calling thread’s resource pool. Such allocations may be freed in two
ways:

- Supervisor threads may call [`k_object_free()`](#c.k_object_free) to force a dynamic
  object to be released.
- If an object’s references drop to zero (which happens when no threads have
  permissions on it) the object will be automatically freed. User threads
  may drop their own permission on an object with
  [`k_object_release()`](#c.k_object_release), and their permissions are automatically
  cleared when a thread terminates. Supervisor threads may additionally
  revoke references for another thread using
  [`k_object_access_revoke()`](#c.k_object_access_revoke).

Because permissions are also used for reference counting, it is important for
supervisor threads to acquire permissions on objects they are using even though
the access control aspects of the permission system are not enforced.

### Implementation Details

The [scripts/build/gen\_kobject\_list.py](../../build/cmake/index.md#gen-kobject-list-py) script is a post-build step which finds all the
valid kernel object instances in the binary. It accomplishes this by parsing
the DWARF debug information present in the generated ELF file for the kernel.

Any instances of structs or arrays corresponding to kernel objects that meet
the object placement criteria will have their memory addresses placed in a
special perfect hash table of kernel objects generated by the ‘gperf’ tool.
When a system call is made and the kernel is presented with a memory address
of what may or may not be a valid kernel object, the address can be validated
with a constant-time lookup in this table.

Drivers are a special case. All drivers are instances of [`device`](../drivers/index.md#c.device "device"), but
it is important to know what subsystem a driver belongs to so that
incorrect operations, such as calling a UART API on a sensor driver object, can
be prevented. When a device struct is found, its API pointer is examined to
determine what subsystem the driver belongs to.

The table itself maps kernel object memory addresses to instances of
`z_object`, which has all the metadata for that object. This
includes:

- A bitfield indicating permissions on that object. All threads have a
  numerical ID assigned to them at build time, used to index the permission
  bitfield for an object to see if that thread has permission on it. The size
  of this bitfield is controlled by the [`CONFIG_MAX_THREAD_BYTES`](../../kconfig.md#CONFIG_MAX_THREAD_BYTES "CONFIG_MAX_THREAD_BYTES")
  option and the build system will generate an error if this value is too low.
- A type field indicating what kind of object this is, which is some
  instance of `k_objects`.
- A set of flags for that object. This is currently used to track
  initialization state and whether an object is public or not.
- An extra data field. The semantics of this field vary by object type, see
  the definition of `z_object_data`.

Dynamic objects allocated at runtime are tracked in a runtime red/black tree
which is used in parallel to the gperf table when validating object pointers.

## Supervisor Thread Access Permission

Supervisor threads can access any kernel object. However, permissions for
supervisor threads are still tracked for two reasons:

- If a supervisor thread calls [`k_thread_user_mode_enter()`](../services/threads/index.md#c.k_thread_user_mode_enter "k_thread_user_mode_enter"), the
  thread will then run in user mode with any permissions it had been granted
  (in many cases, by itself) when it was a supervisor thread.
- If a supervisor thread creates a user thread with the
  [`K_INHERIT_PERMS`](../services/threads/index.md#c.K_INHERIT_PERMS "K_INHERIT_PERMS") option, the child thread will be granted the
  same permissions as the parent thread, except the parent thread object.

## User Thread Access Permission

By default, when a user thread is created, it will only have access permissions
on its own thread object. Other kernel objects by default are not usable.
Access to them needs to be explicitly or implicitly granted. There are several
ways to do this.

- If a thread is created with the [`K_INHERIT_PERMS`](../services/threads/index.md#c.K_INHERIT_PERMS "K_INHERIT_PERMS"), that thread
  will inherit all the permissions of the parent thread, except the parent
  thread object.
- A thread that has permission on an object, or is running in supervisor mode,
  may grant permission on that object to another thread via the
  [`k_object_access_grant()`](#c.k_object_access_grant) API. The convenience pseudo-function
  [`k_thread_access_grant()`](../services/threads/index.md#c.k_thread_access_grant "k_thread_access_grant") may also be used, which accepts an arbitrary
  number of pointers to kernel objects and calls
  [`k_object_access_grant()`](#c.k_object_access_grant) on each of them. The thread being granted
  permission, or the object whose access is being granted, do not need to be
  in an initialized state. If the caller is from user mode, the caller must
  have permissions on both the kernel object and the target thread object.
- Supervisor threads may declare a particular kernel object to be a public
  object, usable by all current and future threads with the
  [`k_object_access_all_grant()`](#c.k_object_access_all_grant) API. You must assume that any
  untrusted or exploited code will then be able to access the object. Use
  this API with caution!
- If a thread was declared statically with [`K_THREAD_DEFINE()`](../services/threads/index.md#c.K_THREAD_DEFINE "K_THREAD_DEFINE"),
  then the [`K_THREAD_ACCESS_GRANT()`](#c.K_THREAD_ACCESS_GRANT) may be used to grant that thread
  access to a set of kernel objects at boot time.

Once a thread has been granted access to an object, such access may be
removed with the [`k_object_access_revoke()`](#c.k_object_access_revoke) API. This API is not
available to user threads, however user threads may use
[`k_object_release()`](#c.k_object_release) to relinquish their own permissions on an
object.

API calls from supervisor mode to set permissions on kernel objects that are
not being tracked by the kernel will be no-ops. Doing the same from user mode
will result in a fatal error for the calling thread.

Objects allocated with [`k_object_alloc()`](#c.k_object_alloc) implicitly grant
permission on the allocated object to the calling thread.

## Initialization State

Most operations on kernel objects will fail if the object is considered to be
in an uninitialized state. The appropriate init function for the object must
be performed first.

Some objects will be implicitly initialized at boot:

- Kernel objects that were declared with static initialization macros
  (such as [`K_SEM_DEFINE`](../services/synchronization/semaphores.md#c.K_SEM_DEFINE "K_SEM_DEFINE") for semaphores) will be in an initialized
  state at build time.
- Device driver objects are considered initialized after their init function
  is run by the kernel early in the boot process.

If a kernel object is initialized with a private static initializer, the object
must have `k_object_init()` called on it at some point by a supervisor
thread, otherwise the kernel will consider the object uninitialized if accessed
by a user thread. This is very uncommon, typically only for kernel objects that
are embedded within some larger struct and initialized statically.

```c
struct foo {
    struct k_sem sem;
    ...
};

struct foo my_foo = {
    .sem = Z_SEM_INITIALIZER(my_foo.sem, 0, 1),
    ...
};

...
k_object_init(&my_foo.sem);
...
```

## Creating New Kernel Object Types

When implementing new kernel features or driver subsystems, it may be necessary
to define some new kernel object types. There are different steps needed
for creating core kernel objects and new driver subsystems.

### Creating New Core Kernel Objects

- In `scripts/build/gen_kobject_list.py`, add the name of the struct to the
  `kobjects` list.

Instances of the new struct should now be tracked.

### Creating New Driver Subsystem Kernel Objects

All driver instances are [`device`](../drivers/index.md#c.device "device"). They are differentiated by
what API struct they are set to.

- In `scripts/build/gen_kobject_list.py`, add the name of the API struct for the
  new subsystem to the `subsystems` list.

Driver instances of the new subsystem should now be tracked.

## Configuration Options

Related configuration options:

- [`CONFIG_USERSPACE`](../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE")
- [`CONFIG_MAX_THREAD_BYTES`](../../kconfig.md#CONFIG_MAX_THREAD_BYTES "CONFIG_MAX_THREAD_BYTES")

## API Reference

*group* User Mode APIs
:   Defines

    K\_THREAD\_ACCESS\_GRANT(name\_, ...)
    :   Grant a static thread access to a list of kernel objects.

        For threads declared with [K\_THREAD\_DEFINE()](../services/threads/index.md#group__thread__apis_1gab3ced58648ca35788a40676e8478ecd2), grant the thread access to a set of kernel objects. These objects do not need to be in an initialized state. The permissions will be granted when the threads are initialized in the early boot sequence.

        All arguments beyond the first must be pointers to kernel objects.

        Parameters:
        :   - **name\_** – Name of the thread, as passed to [K\_THREAD\_DEFINE()](../services/threads/index.md#group__thread__apis_1gab3ced58648ca35788a40676e8478ecd2)

    K\_OBJ\_FLAG\_INITIALIZED
    :   Object initialized.

    K\_OBJ\_FLAG\_PUBLIC
    :   Object is Public.

    K\_OBJ\_FLAG\_ALLOC
    :   Object allocated.

    K\_OBJ\_FLAG\_DRIVER
    :   Driver Object.

    Functions

    void k\_object\_access\_grant(const void \*object, struct [k\_thread](../services/threads/index.md#c.k_thread "k_thread") \*thread)
    :   Grant a thread access to a kernel object.

        The thread will be granted access to the object if the caller is from supervisor mode, or the caller is from user mode AND has permissions on both the object and the thread whose access is being granted.

        Parameters:
        :   - **object** – Address of kernel object
            - **thread** – Thread to grant access to the object

    void k\_object\_access\_revoke(const void \*object, struct [k\_thread](../services/threads/index.md#c.k_thread "k_thread") \*thread)
    :   Revoke a thread’s access to a kernel object.

        The thread will lose access to the object if the caller is from supervisor mode, or the caller is from user mode AND has permissions on both the object and the thread whose access is being revoked.

        Parameters:
        :   - **object** – Address of kernel object
            - **thread** – Thread to remove access to the object

    void k\_object\_release(const void \*object)
    :   Release an object.

        Allows user threads to drop their own permission on an object Their permissions are automatically cleared when a thread terminates.

        Parameters:
        :   - **object** – The object to be released

    void k\_object\_access\_all\_grant(const void \*object)
    :   Grant all present and future threads access to an object.

        If the caller is from supervisor mode, or the caller is from user mode and have sufficient permissions on the object, then that object will have permissions granted to it for *all* current and future threads running in the system, effectively becoming a public kernel object.

        Use of this API should be avoided on systems that are running untrusted code as it is possible for such code to derive the addresses of kernel objects and perform unwanted operations on them.

        It is not possible to revoke permissions on public objects; once public, any thread may use it.

        Parameters:
        :   - **object** – Address of kernel object

    bool k\_object\_is\_valid(const void \*obj, enum k\_objects otype)
    :   Check if a kernel object is of certain type and is valid.

        This checks if the kernel object exists, of certain type, and has been initialized.

        Parameters:
        :   - **obj** – Address of the kernel object
            - **otype** – Object type (use K\_OBJ\_ANY for ignoring type checking)

        Returns:
        :   True if kernel object (*obj*) exists, of certain type, and has been initialized. False otherwise.

    void \*k\_object\_alloc(enum k\_objects otype)
    :   Allocate a kernel object of a designated type.

        This will instantiate at runtime a kernel object of the specified type, returning a pointer to it. The object will be returned in an uninitialized state, with the calling thread being granted permission on it. The memory for the object will be allocated out of the calling thread’s resource pool.

        Note

        This function is available only if  [`CONFIG_DYNAMIC_OBJECTS`](../../kconfig.md#CONFIG_DYNAMIC_OBJECTS "CONFIG_DYNAMIC_OBJECTS") is selected.

        Note

        Thread stack object has to use [k\_object\_alloc\_size()](#group__usermode__apis_1gab99a640325f14a6505a85218dcba5446) since stacks may have different sizes.

        Parameters:
        :   - **otype** – Requested kernel object type

        Returns:
        :   A pointer to the allocated kernel object, or NULL if memory wasn’t available

    void \*k\_object\_alloc\_size(enum k\_objects otype, size\_t size)
    :   Allocate a kernel object of a designated type and a given size.

        This will instantiate at runtime a kernel object of the specified type, returning a pointer to it. The object will be returned in an uninitialized state, with the calling thread being granted permission on it. The memory for the object will be allocated out of the calling thread’s resource pool.

        This function is specially helpful for thread stack objects because their sizes can vary. Other objects should probably look [k\_object\_alloc()](#group__usermode__apis_1ga5bba3a354fbc63673c76c9815db40812).

        Note

        This function is available only if  [`CONFIG_DYNAMIC_OBJECTS`](../../kconfig.md#CONFIG_DYNAMIC_OBJECTS "CONFIG_DYNAMIC_OBJECTS") is selected.

        Parameters:
        :   - **otype** – Requested kernel object type
            - **size** – Requested kernel object size

        Returns:
        :   A pointer to the allocated kernel object, or NULL if memory wasn’t available

    void k\_object\_free(void \*obj)
    :   Free a kernel object previously allocated with [k\_object\_alloc()](#group__usermode__apis_1ga5bba3a354fbc63673c76c9815db40812).

        This will return memory for a kernel object back to resource pool it was allocated from. Care must be exercised that the object will not be used during or after when this call is made.

        Note

        This function is available only if  [`CONFIG_DYNAMIC_OBJECTS`](../../kconfig.md#CONFIG_DYNAMIC_OBJECTS "CONFIG_DYNAMIC_OBJECTS") is selected.

        Parameters:
        :   - **obj** – Pointer to the kernel object memory address.
