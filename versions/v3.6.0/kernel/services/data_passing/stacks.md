---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/data_passing/stacks.html
original_path: kernel/services/data_passing/stacks.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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
It must then be initialized by calling [`k_stack_init()`](#c.k_stack_init) or
[`k_stack_alloc_init()`](#c.k_stack_alloc_init). In the latter case, a buffer is not
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
by calling [`K_STACK_DEFINE`](#c.K_STACK_DEFINE).

The following code has the same effect as the code segment above. Observe
that the macro defines both the stack and its array of data values.

```c
K_STACK_DEFINE(my_stack, MAX_ITEMS);
```

### [Pushing to a Stack](#id4)

A data item is added to a stack by calling [`k_stack_push()`](#c.k_stack_push).

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

A data item is taken from a stack by calling [`k_stack_pop()`](#c.k_stack_pop).

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

*group* stack\_apis
:   Defines

    K\_STACK\_DEFINE(name, stack\_num\_entries)
    :   Statically define and initialize a stack.

        The stack can be accessed outside the module where it is defined using:

        ```text
        extern struct k_stack <name>;
        ```

        Parameters:
        :   - **name** – Name of the stack.
            - **stack\_num\_entries** – Maximum number of values that can be stacked.

    Functions

    void k\_stack\_init(struct k\_stack \*stack, stack\_data\_t \*buffer, uint32\_t num\_entries)
    :   Initialize a stack.

        This routine initializes a stack object, prior to its first use.

        Parameters:
        :   - **stack** – Address of the stack.
            - **buffer** – Address of array used to hold stacked values.
            - **num\_entries** – Maximum number of values that can be stacked.

    int32\_t k\_stack\_alloc\_init(struct k\_stack \*stack, uint32\_t num\_entries)
    :   Initialize a stack.

        This routine initializes a stack object, prior to its first use. Internal buffers will be allocated from the calling thread’s resource pool. This memory will be released if [k\_stack\_cleanup()](#group__stack__apis_1ga819f4e7b2cf11cf2e1b80933fdcb67ea) is called, or userspace is enabled and the stack object loses all references to it.

        Parameters:
        :   - **stack** – Address of the stack.
            - **num\_entries** – Maximum number of values that can be stacked.

        Returns:
        :   -ENOMEM if memory couldn’t be allocated

    int k\_stack\_cleanup(struct k\_stack \*stack)
    :   Release a stack’s allocated buffer.

        If a stack object was given a dynamically allocated buffer via [k\_stack\_alloc\_init()](#group__stack__apis_1gab97d924db1aef3f6adade156a107d45c), this will free it. This function does nothing if the buffer wasn’t dynamically allocated.

        Parameters:
        :   - **stack** – Address of the stack.

        Return values:
        :   - **0** – on success
            - **-EAGAIN** – when object is still in use

    int k\_stack\_push(struct k\_stack \*stack, stack\_data\_t data)
    :   Push an element onto a stack.

        This routine adds a stack\_data\_t value *data* to *stack*.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **stack** – Address of the stack.
            - **data** – Value to push onto the stack.

        Return values:
        :   - **0** – on success
            - **-ENOMEM** – if stack is full

    int k\_stack\_pop(struct k\_stack \*stack, stack\_data\_t \*data, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Pop an element from a stack.

        This routine removes a stack\_data\_t value from *stack*

        in a “last in,

        first out” manner and stores the value in

        *data*.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        *timeout* must be set to K\_NO\_WAIT if called from ISR.

        Parameters:
        :   - **stack** – Address of the stack.
            - **data** – Address of area to hold the value popped from the stack.
            - **timeout** – Waiting period to obtain a value, or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Return values:
        :   - **0** – Element popped from stack.
            - **-EBUSY** – Returned without waiting.
            - **-EAGAIN** – Waiting period timed out.
