---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/kernel/object_cores/index.html
original_path: kernel/object_cores/index.html
---

# Object Cores

Object cores are a kernel debugging tool that can be used to both identify and
perform operations on registered objects.

## [Object Core Concepts](#id1)

Each instance of an object embeds an object core field named `obj_core`.
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
[`k_obj_type`](../../doxygen/html/structk__obj__type.md). It must be initialized before any objects of that type
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
type. These are [`k_obj_type_walk_locked()`](../../doxygen/html/group__obj__core__apis.md#ga1e9a331ca6f3f7bf1f0e3b144b964b9b) and
[`k_obj_type_walk_unlocked()`](../../doxygen/html/group__obj__core__apis.md#ga4d3da7db72063699b66a54e56cf75e2e). The following code builds upon the example
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

[Object Core APIs](../../doxygen/html/group__obj__core__apis.md)

[Object Core Statistics APIs](../../doxygen/html/group__obj__core__stats__apis.md)
