---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/kernel/services/data_passing/stacks.html
original_path: kernel/services/data_passing/stacks.html
---

# Stacks

A *stack* is a kernel object that implements a traditional
last in, first out (LIFO) queue, allowing threads and ISRs
to add and remove a limited number of integer data values.

## [Concepts](#id1)

Any number of stacks can be defined (limited only by available RAM). Each stack
is referenced by its memory address.

A stack has the following key properties:

- A **queue** of integer data values that have been added but not yet removed.
  The queue is implemented using an array of stack\_data\_t values
  and must be aligned on a native word boundary.
  The stack\_data\_t type corresponds to the native word size i.e. 32 bits or
  64 bits depending on the CPU architecture and compilation mode.
- A **maximum quantity** of data values that can be queued in the array.

A stack must be initialized before it can be used. This sets its queue to empty.

A data value can be **added** to a stack by a thread or an ISR.
The value is given directly to a waiting thread, if one exists;
otherwise the value is added to the LIFO’s queue.

Note

If [`CONFIG_NO_RUNTIME_CHECKS`](../../../kconfig.md#CONFIG_NO_RUNTIME_CHECKS "CONFIG_NO_RUNTIME_CHECKS") is enabled, the kernel will *not* detect
and prevent attempts to add a data value to a stack that has already reached
its maximum quantity of queued values. Adding a data value to a stack that is
already full will result in array overflow, and lead to unpredictable behavior.

A data value may be **removed** from a stack by a thread.
If the stack’s queue is empty a thread may choose to wait for it to be given.
Any number of threads may wait on an empty stack simultaneously.
When a data item is added, it is given to the highest priority thread
that has waited longest.

Note

The kernel does allow an ISR to remove an item from a stack, however
the ISR must not attempt to wait if the stack is empty.

## [Implementation](#id2)

### [Defining a Stack](#id3)

A stack is defined using a variable of type `k_stack`.
It must then be initialized by calling [`k_stack_init()`](../../../doxygen/html/group__stack__apis.md#ga4400a39ef48289305cf66a092d5c6c7d) or
[`k_stack_alloc_init()`](../../../doxygen/html/group__stack__apis.md#gab97d924db1aef3f6adade156a107d45c). In the latter case, a buffer is not
provided and it is instead allocated from the calling thread’s resource
pool.

The following code defines and initializes an empty stack capable of holding
up to ten word-sized data values.

```c
#define MAX_ITEMS 10

stack_data_t my_stack_array[MAX_ITEMS];
struct k_stack my_stack;

k_stack_init(&my_stack, my_stack_array, MAX_ITEMS);
```

Alternatively, a stack can be defined and initialized at compile time
by calling [`K_STACK_DEFINE`](../../../doxygen/html/group__stack__apis.md#ga8c9ca77e5de3c9757dcd4ecb55797835).

The following code has the same effect as the code segment above. Observe
that the macro defines both the stack and its array of data values.

```c
K_STACK_DEFINE(my_stack, MAX_ITEMS);
```

### [Pushing to a Stack](#id4)

A data item is added to a stack by calling [`k_stack_push()`](../../../doxygen/html/group__stack__apis.md#gaa6180f4db6ec93ee84149cba054d3e53).

The following code builds on the example above, and shows how a thread
can create a pool of data structures by saving their memory addresses
in a stack.

```c
/* define array of data structures */
struct my_buffer_type {
    int field1;
    ...
    };
struct my_buffer_type my_buffers[MAX_ITEMS];

/* save address of each data structure in a stack */
for (int i = 0; i < MAX_ITEMS; i++) {
    k_stack_push(&my_stack, (stack_data_t)&my_buffers[i]);
}
```

### [Popping from a Stack](#id5)

A data item is taken from a stack by calling [`k_stack_pop()`](../../../doxygen/html/group__stack__apis.md#ga36ce6ceb9ea3d5c36d22b10430789480).

The following code builds on the example above, and shows how a thread
can dynamically allocate an unused data structure.
When the data structure is no longer required, the thread must push
its address back on the stack to allow the data structure to be reused.

```c
struct my_buffer_type *new_buffer;

k_stack_pop(&buffer_stack, (stack_data_t *)&new_buffer, K_FOREVER);
new_buffer->field1 = ...
```

## [Suggested Uses](#id6)

Use a stack to store and retrieve integer data values in a “last in,
first out” manner, when the maximum number of stored items is known.

## [Configuration Options](#id7)

Related configuration options:

- None.

## [API Reference](#id8)

[Stack APIs](../../../doxygen/html/group__stack__apis.md)

Related code samples

- [Dining Philosophers](../../../samples/philosophers/README.md#dining-philosophers "Implement a solution to the Dining Philosophers problem using Zephyr kernel services.")Implement a solution to the Dining Philosophers problem using Zephyr kernel services.
