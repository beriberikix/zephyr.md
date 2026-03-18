---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/object_cores/index.html
original_path: kernel/object_cores/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Object Cores

Object cores are a kernel debugging tool that can be used to both identify and
perform operations on registered objects.

## [Object Core Concepts](#id1)

Each instance of an object embeds an object core field named obj\_core.
Objects of the same type are linked together via their respective object
cores to form a singly linked list. Each object core also links to the their
respective object type. Each object type contains a singly linked list
linking together all the object cores of that type. Object types are also
linked together via a singly linked list. Together, this can allow debugging
tools to traverse all the objects in the system.

Object cores have been integrated into following kernel objects:
:   - [Condition Variables](../services/synchronization/condvar.md#condvar)
    - [Events](../services/synchronization/events.md#events)
    - [FIFOs](../services/data_passing/fifos.md#fifos-v2) and [LIFOs](../services/data_passing/lifos.md#lifos-v2)
    - [Mailboxes](../services/data_passing/mailboxes.md#mailboxes-v2)
    - [Memory Slabs](../memory_management/slabs.md#memory-slabs-v2)
    - [Message Queues](../services/data_passing/message_queues.md#message-queues-v2)
    - [Mutexes](../services/synchronization/mutexes.md#mutexes-v2)
    - [Pipes](../services/data_passing/pipes.md#pipes-v2)
    - [Semaphores](../services/synchronization/semaphores.md#semaphores-v2)
    - [Threads](../services/threads/index.md#threads-v2)
    - [Timers](../services/timing/timers.md#timers-v2)
    - [System Memory Blocks](../memory_management/sys_mem_blocks.md#sys-mem-blocks)

Developers are free to integrate them if desired into other objects within
their projects.

## [Object Core Statistics Concepts](#id2)

A variety of kernel objects allow for the gathering and reporting of statistics.
Object cores provide a uniform means to retrieve that information via object
core statistics. When enabled, the object type contains a pointer to a
statistics descriptor that defines the various operations that have been
enabled for interfacing with the object’s statistics. Additionally, the object
core contains a pointer to the “raw” statistical information associated with
that object. Raw data is the raw, unmanipulated data associated with the
statistics. Queried data may be “raw”, but it may also have been manipulated in
some way by calculation (such as determining an average).

The following table indicates both what objects have been integrated into the
object core statistics as well as the structures used for both “raw” and
“queried” data.

| Object | Raw Data Type | Query Data Type |
| --- | --- | --- |
| struct mem\_slab | struct mem\_slab\_info | struct sys\_memory\_stats |
| struct sys\_mem\_blocks | struct sys\_mem\_blocks\_info | struct sys\_memory\_stats |
| struct k\_thread | struct k\_cycle\_stats | struct k\_thread\_runtime\_stats |
| struct \_cpu | struct k\_cycle\_stats | struct k\_thread\_runtime\_stats |
| struct z\_kernel | struct k\_cycle\_stats[num CPUs] | struct k\_thread\_runtime\_stats |

## [Implementation](#id3)

### [Defining a New Object Type](#id4)

An object type is defined using a global variable of type
[`k_obj_type`](#c.k_obj_type). It must be initialized before any objects of that type
are initialized. The following code shows how a new object type can be
initialized for use with object cores and object core statistics.

```c
/* Unique object type ID */

#define K_OBJ_TYPE_MY_NEW_TYPE  K_OBJ_TYPE_ID_GEN("UNIQ")
struct k_obj_type  my_obj_type;

struct my_obj_type_raw_info {
    ...
};

struct my_obj_type_query_stats {
    ...
};

struct my_new_obj {
    ...
    struct k_obj_core obj_core;
    struct my_obj_type_raw_info  info;
};

struct k_obj_core_stats_desc my_obj_type_stats_desc = {
    .raw_size = sizeof(struct my_obj_type_raw_stats),
    .query_size = sizeof(struct my_obj_type_query_stats),
    .raw = my_obj_type_stats_raw,
    .query = my_obj_type_stats_query,
    .reset = my_obj_type_stats_reset,
    .disable = NULL,    /* Stats gathering is always on */
    .enable = NULL,     /* Stats gathering is always on */
};

void my_obj_type_init(void)
{
    z_obj_type_init(&my_obj_type, K_OBJ_TYPE_MY_NEW_TYPE,
                    offsetof(struct my_new_obj, obj_core);
    k_obj_type_stats_init(&my_obj_type, &my_obj_type_stats_desc);
}
```

### [Initializing a New Object Core](#id5)

Kernel objects that have already been integrated into the object core framework
automatically have their object cores initialized when the object is
initialized. However, developers that wish to add their own objects into the
framework need to both initialize the object core and link it. The following
code builds on the example above and initializes the object core.

```c
void my_new_obj_init(struct my_new_obj *new_obj)
{
    ...
    k_obj_core_init(K_OBJ_CORE(new_obj), &my_obj_type);
    k_obj_core_link(K_OBJ_CORE(new_obj));
    k_obj_core_stats_register(K_OBJ_CORE(new_obj), &new_obj->raw_stats,
                              sizeof(struct my_obj_type_raw_info));
}
```

### [Walking a List of Object Cores](#id6)

Two routines exist for walking the list of object cores linked to an object
type. These are [`k_obj_type_walk_locked()`](#c.k_obj_type_walk_locked) and
[`k_obj_type_walk_unlocked()`](#c.k_obj_type_walk_unlocked). The following code builds upon the example
above and prints the addresses of all the objects of that new object type.

```c
int walk_op(struct k_obj_core *obj_core, void *data)
{
    uint8_t *ptr;

    ptr = obj_core;
    ptr -= obj_core->type->obj_core_offset;

    printk("%p\n", ptr);

    return 0;
}

void print_object_addresses(void)
{
    struct k_obj_type *obj_type;

    /* Find the object type */

    obj_type = k_obj_type_find(K_OBJ_TYPE_MY_NEW_TYPE);

    /* Walk the list of objects */

    k_obj_type_walk_unlocked(obj_type, walk_op, NULL);
}
```

### [Object Core Statistics Querying](#id7)

The following code builds on the examples above and shows how an object
integrated into the object core statistics framework can both retrieve queried
data and reset the stats associated with the object.

```c
struct my_new_obj my_obj;

...

void my_func(void)
{
    struct my_obj_type_query_stats  my_stats;
    int  status;

    my_obj_type_init(&my_obj);

    ...

    status = k_obj_core_stats_query(K_OBJ_CORE(&my_obj),
                                    &my_stats, sizeof(my_stats));
    if (status != 0) {
        /* Failed to get stats */
        ...
    } else {
        k_obj_core_stats_reset(K_OBJ_CORE(&my_obj));
    }

    ...
}
```

## [Configuration Options](#id8)

Related configuration options:

- [`CONFIG_OBJ_CORE`](../../kconfig.md#CONFIG_OBJ_CORE "CONFIG_OBJ_CORE")
- [`CONFIG_OBJ_CORE_CONDVAR`](../../kconfig.md#CONFIG_OBJ_CORE_CONDVAR "CONFIG_OBJ_CORE_CONDVAR")
- [`CONFIG_OBJ_CORE_EVENT`](../../kconfig.md#CONFIG_OBJ_CORE_EVENT "CONFIG_OBJ_CORE_EVENT")
- [`CONFIG_OBJ_CORE_FIFO`](../../kconfig.md#CONFIG_OBJ_CORE_FIFO "CONFIG_OBJ_CORE_FIFO")
- [`CONFIG_OBJ_CORE_LIFO`](../../kconfig.md#CONFIG_OBJ_CORE_LIFO "CONFIG_OBJ_CORE_LIFO")
- [`CONFIG_OBJ_CORE_MAILBOX`](../../kconfig.md#CONFIG_OBJ_CORE_MAILBOX "CONFIG_OBJ_CORE_MAILBOX")
- [`CONFIG_OBJ_CORE_MEM_SLAB`](../../kconfig.md#CONFIG_OBJ_CORE_MEM_SLAB "CONFIG_OBJ_CORE_MEM_SLAB")
- [`CONFIG_OBJ_CORE_MSGQ`](../../kconfig.md#CONFIG_OBJ_CORE_MSGQ "CONFIG_OBJ_CORE_MSGQ")
- [`CONFIG_OBJ_CORE_MUTEX`](../../kconfig.md#CONFIG_OBJ_CORE_MUTEX "CONFIG_OBJ_CORE_MUTEX")
- [`CONFIG_OBJ_CORE_PIPE`](../../kconfig.md#CONFIG_OBJ_CORE_PIPE "CONFIG_OBJ_CORE_PIPE")
- [`CONFIG_OBJ_CORE_SEM`](../../kconfig.md#CONFIG_OBJ_CORE_SEM "CONFIG_OBJ_CORE_SEM")
- [`CONFIG_OBJ_CORE_STACK`](../../kconfig.md#CONFIG_OBJ_CORE_STACK "CONFIG_OBJ_CORE_STACK")
- [`CONFIG_OBJ_CORE_THREAD`](../../kconfig.md#CONFIG_OBJ_CORE_THREAD "CONFIG_OBJ_CORE_THREAD")
- [`CONFIG_OBJ_CORE_TIMER`](../../kconfig.md#CONFIG_OBJ_CORE_TIMER "CONFIG_OBJ_CORE_TIMER")
- [`CONFIG_OBJ_CORE_SYS_MEM_BLOCKS`](../../kconfig.md#CONFIG_OBJ_CORE_SYS_MEM_BLOCKS "CONFIG_OBJ_CORE_SYS_MEM_BLOCKS")
- [`CONFIG_OBJ_CORE_STATS`](../../kconfig.md#CONFIG_OBJ_CORE_STATS "CONFIG_OBJ_CORE_STATS")
- [`CONFIG_OBJ_CORE_STATS_MEM_SLAB`](../../kconfig.md#CONFIG_OBJ_CORE_STATS_MEM_SLAB "CONFIG_OBJ_CORE_STATS_MEM_SLAB")
- [`CONFIG_OBJ_CORE_STATS_THREAD`](../../kconfig.md#CONFIG_OBJ_CORE_STATS_THREAD "CONFIG_OBJ_CORE_STATS_THREAD")
- [`CONFIG_OBJ_CORE_STATS_SYSTEM`](../../kconfig.md#CONFIG_OBJ_CORE_STATS_SYSTEM "CONFIG_OBJ_CORE_STATS_SYSTEM")
- [`CONFIG_OBJ_CORE_STATS_SYS_MEM_BLOCKS`](../../kconfig.md#CONFIG_OBJ_CORE_STATS_SYS_MEM_BLOCKS "CONFIG_OBJ_CORE_STATS_SYS_MEM_BLOCKS")

## [API Reference](#id9)

*group* obj\_core\_apis
:   Defines

    K\_OBJ\_CORE(kobj)
    :   Convert kernel object pointer into its object core pointer.

    K\_OBJ\_TYPE\_ID\_GEN(s)
    :   Generate new object type IDs based on a 4 letter string.

    K\_OBJ\_TYPE\_CONDVAR\_ID
    :   Condition variable object type.

    K\_OBJ\_TYPE\_CPU\_ID
    :   CPU object type.

    K\_OBJ\_TYPE\_EVENT\_ID
    :   Event object type.

    K\_OBJ\_TYPE\_FIFO\_ID
    :   FIFO object type.

    K\_OBJ\_TYPE\_KERNEL\_ID
    :   Kernel object type.

    K\_OBJ\_TYPE\_LIFO\_ID
    :   LIFO object type.

    K\_OBJ\_TYPE\_MEM\_BLOCK\_ID
    :   Memory block object type.

    K\_OBJ\_TYPE\_MBOX\_ID
    :   Mailbox object type.

    K\_OBJ\_TYPE\_MEM\_SLAB\_ID
    :   Memory slab object type.

    K\_OBJ\_TYPE\_MSGQ\_ID
    :   Message queue object type.

    K\_OBJ\_TYPE\_MUTEX\_ID
    :   Mutex object type.

    K\_OBJ\_TYPE\_PIPE\_ID
    :   Pipe object type.

    K\_OBJ\_TYPE\_SEM\_ID
    :   Semaphore object type.

    K\_OBJ\_TYPE\_STACK\_ID
    :   Stack object type.

    K\_OBJ\_TYPE\_THREAD\_ID
    :   Thread object type.

    K\_OBJ\_TYPE\_TIMER\_ID
    :   Timer object type.

    Functions

    struct [k\_obj\_type](#c.k_obj_type) \*k\_obj\_type\_find(uint32\_t type\_id)
    :   Find a specific object type by ID.

        Given an object type ID, this function searches for the object type that is associated with the specified type ID *type\_id*.

        Parameters:
        :   - **type\_id** – Type ID associated with object type

        Return values:
        :   - **NULL** – if object type not found
            - **Pointer** – to object type if found

    int k\_obj\_type\_walk\_locked(struct [k\_obj\_type](#c.k_obj_type) \*type, int (\*func)(struct [k\_obj\_core](#c.k_obj_core)\*, void\*), void \*data)
    :   Walk the object type’s list of object cores.

        This function takes a global spinlock and walks the object type’s list of object cores and invokes the callback function on each element while holding that lock. Although this will ensure that the list is not modified, one can expect a significant penalty in terms of performance and latency.

        The callback function shall either return non-zero to stop further walking, or it shall return 0 to continue walking.

        Parameters:
        :   - **type** – Pointer to the object type
            - **func** – Callback to invoke on each object core of the object type
            - **data** – Custom data passed to the callback

        Return values:
        :   **non-zero** – if walk is terminated by the callback; otherwise 0

    int k\_obj\_type\_walk\_unlocked(struct [k\_obj\_type](#c.k_obj_type) \*type, int (\*func)(struct [k\_obj\_core](#c.k_obj_core)\*, void\*), void \*data)
    :   Walk the object type’s list of object cores.

        This function is similar to [k\_obj\_type\_walk\_locked()](#group__obj__core__apis_1ga1e9a331ca6f3f7bf1f0e3b144b964b9b) except that it walks the list without obtaining the global spinlock. No synchronization is provided here. Mutation of the list of objects while this function is in progress must be prevented at the application layer, otherwise undefined/unreliable behavior, corruption and/or crashes may result.

        The callback function shall either return non-zero to stop further walking, or it shall return 0 to continue walking.

        Parameters:
        :   - **type** – Pointer to the object type
            - **func** – Callback to invoke on each object core of the object type
            - **data** – Custom data passed to the callback

        Return values:
        :   **non-zero** – if walk is terminated by the callback; otherwise 0

    void k\_obj\_core\_init(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core, struct [k\_obj\_type](#c.k_obj_type) \*type)
    :   Initialize the core of the kernel object.

        Initializing the kernel object core associates it with the specified kernel object type.

        Parameters:
        :   - **obj\_core** – Pointer to the kernel object to initialize
            - **type** – Pointer to the kernel object type

    void k\_obj\_core\_link(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core)
    :   Link the kernel object to the kernel object type list.

        A kernel object can be optionally linked into the kernel object type’s list of objects. A kernel object must have been initialized before it can be linked. Linked kernel objects can be traversed and have information extracted from them by system tools.

        Parameters:
        :   - **obj\_core** – Pointer to the kernel object

    void k\_obj\_core\_init\_and\_link(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core, struct [k\_obj\_type](#c.k_obj_type) \*type)
    :   Automatically link the kernel object after initializing it.

        A useful wrapper to both initialize the core of the kernel object and automatically link it into the kernel object type’s list of objects.

        Parameters:
        :   - **obj\_core** – Pointer to the kernel object to initialize
            - **type** – Pointer to the kernel object type

    void k\_obj\_core\_unlink(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core)
    :   Unlink the kernel object from the kernel object type list.

        Kernel objects can be unlinked from their respective kernel object type lists. If on a list, it must be done at the end of the kernel object’s life cycle.

        Parameters:
        :   - **obj\_core** – Pointer to the kernel object

    struct k\_obj\_core\_stats\_desc
    :   *#include <obj\_core.h>*

        Object core statistics descriptor.

        Public Members

        size\_t raw\_size
        :   Internal representation stats buffer size.

        size\_t query\_size
        :   Stats buffer size used for reporting.

        int (\*raw)(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core, void \*stats)
        :   Function pointer to retrieve internal representation of stats.

        int (\*query)(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core, void \*stats)
        :   Function pointer to retrieve reported statistics.

        int (\*reset)(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core)
        :   Function pointer to reset object’s statistics.

        int (\*disable)(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core)
        :   Function pointer to disable object’s statistics gathering.

        int (\*enable)(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core)
        :   Function pointer to enable object’s statistics gathering.

    struct k\_obj\_type
    :   *#include <obj\_core.h>*

        Object type structure.

        Public Members

        [sys\_snode\_t](../data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Node within list of object types.

        [sys\_slist\_t](../data_structures/slist.md#c.sys_slist_t "sys_slist_t") list
        :   List of objects of this object type.

        uint32\_t id
        :   Unique type ID.

        size\_t obj\_core\_offset
        :   Offset to obj\_core field.

    struct k\_obj\_core
    :   *#include <obj\_core.h>*

        Object core structure.

        Public Members

        [sys\_snode\_t](../data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Object node within object type’s list.

        struct [k\_obj\_type](#c.k_obj_type) \*type
        :   Object type to which object belongs.

*group* obj\_core\_stats\_apis
:   Functions

    int k\_obj\_core\_stats\_register(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core, void \*stats, size\_t stats\_len)
    :   Register kernel object for gathering statistics.

        Before a kernel object can gather statistics, it must be registered to do so. Registering will also automatically enable the kernel object to gather its statistics.

        Parameters:
        :   - **obj\_core** – Pointer to kernel object core
            - **stats** – Pointer to raw kernel statistics
            - **stats\_len** – Size of raw kernel statistics buffer

        Return values:
        :   - **0** – on success
            - **-errno** – on failure

    int k\_obj\_core\_stats\_deregister(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core)
    :   Deregister kernel object from gathering statistics.

        Deregistering a kernel object core from gathering statistics prevents it from gathering any more statistics. It is expected to be invoked at the end of a kernel object’s life cycle.

        Parameters:
        :   - **obj\_core** – Pointer to kernel object core

        Return values:
        :   - **0** – on success
            - **-errno** – on failure

    int k\_obj\_core\_stats\_raw(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core, void \*stats, size\_t stats\_len)
    :   Retrieve the raw statistics associated with the kernel object.

        This function copies the raw statistics associated with the kernel object core specified by *obj\_core* into the buffer *stats*. Note that the size of the buffer (*stats\_len*) must match the size specified by the kernel object type’s statistics descriptor.

        Parameters:
        :   - **obj\_core** – Pointer to kernel object core
            - **stats** – Pointer to memory buffer into which to copy raw stats
            - **stats\_len** – Length of the memory buffer

        Return values:
        :   - **0** – on success
            - **-errno** – on failure

    int k\_obj\_core\_stats\_query(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core, void \*stats, size\_t stats\_len)
    :   Retrieve the statistics associated with the kernel object.

        This function copies the statistics associated with the kernel object core specified by *obj\_core* into the buffer *stats*. Unlike the raw statistics this may report calculated values such as averages. Note that the size of the buffer (*stats\_len*) must match the size specified by the kernel object type’s statistics descriptor.

        Parameters:
        :   - **obj\_core** – Pointer to kernel object core
            - **stats** – Pointer to memory buffer into which to copy the queried stats
            - **stats\_len** – Length of the memory buffer

        Return values:
        :   - **0** – on success
            - **-errno** – on failure

    int k\_obj\_core\_stats\_reset(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core)
    :   Reset the stats associated with the kernel object.

        This function resets the statistics associated with the kernel object core specified by *obj\_core*.

        Parameters:
        :   - **obj\_core** – Pointer to kernel object core

        Return values:
        :   - **0** – on success
            - **-errno** – on failure

    int k\_obj\_core\_stats\_disable(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core)
    :   Stop gathering the stats associated with the kernel object.

        This function temporarily stops the gathering of statistics associated with the kernel object core specified by *obj\_core*. The gathering of statistics can be resumed by invoking :c:func :`[k_obj_core_stats_enable](#group__obj__core__stats__apis_1ga079df60c5ba6dd08a2270362490553fa)`.

        Parameters:
        :   - **obj\_core** – Pointer to kernel object core

        Return values:
        :   - **0** – on success
            - **-errno** – on failure

    int k\_obj\_core\_stats\_enable(struct [k\_obj\_core](#c.k_obj_core) \*obj\_core)
    :   Reset the stats associated with the kernel object.

        This function resumes the gathering of statistics associated with the kernel object core specified by *obj\_core*.

        Parameters:
        :   - **obj\_core** – Pointer to kernel object core

        Return values:
        :   - **0** – on success
            - **-errno** – on failure
