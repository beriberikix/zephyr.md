---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/other/atomic.html
original_path: kernel/services/other/atomic.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Atomic Services

An *atomic variable* is one that can be read and modified
by threads and ISRs in an uninterruptible manner. It is a 32-bit variable on
32-bit machines and a 64-bit variable on 64-bit machines.

## [Concepts](#id1)

Any number of atomic variables can be defined (limited only by available RAM).

Using the kernel’s atomic APIs to manipulate an atomic variable
guarantees that the desired operation occurs correctly,
even if higher priority contexts also manipulate the same variable.

The kernel also supports the atomic manipulation of a single bit
in an array of atomic variables.

## [Implementation](#id2)

### [Defining an Atomic Variable](#id3)

An atomic variable is defined using a variable of type `atomic_t`.

By default an atomic variable is initialized to zero. However, it can be given
a different value using [`ATOMIC_INIT`](#c.ATOMIC_INIT):

```c
atomic_t flags = ATOMIC_INIT(0xFF);
```

### [Manipulating an Atomic Variable](#id4)

An atomic variable is manipulated using the APIs listed at the end of
this section.

The following code shows how an atomic variable can be used to keep track
of the number of times a function has been invoked. Since the count is
incremented atomically, there is no risk that it will become corrupted
in mid-increment if a thread calling the function is interrupted if
by a higher priority context that also calls the routine.

```c
atomic_t call_count;

int call_counting_routine(void)
{
    /* increment invocation counter */
    atomic_inc(&call_count);

    /* do rest of routine's processing */
    ...
}
```

### [Manipulating an Array of Atomic Variables](#id5)

An array of 32-bit atomic variables can be defined in the conventional manner.
However, you can also define an N-bit array of atomic variables using
[`ATOMIC_DEFINE`](#c.ATOMIC_DEFINE).

A single bit in array of atomic variables can be manipulated using
the APIs listed at the end of this section that end with `_bit()`.

The following code shows how a set of 200 flag bits can be implemented
using an array of atomic variables.

```c
#define NUM_FLAG_BITS 200

ATOMIC_DEFINE(flag_bits, NUM_FLAG_BITS);

/* set specified flag bit & return its previous value */
int set_flag_bit(int bit_position)
{
    return (int)atomic_set_bit(flag_bits, bit_position);
}
```

### [Memory Ordering](#id6)

For consistency and correctness, all Zephyr atomic APIs are expected
to include a full memory barrier (in the sense of e.g. “serializing”
instructions on x86, “DMB” on ARM, or a “sequentially consistent”
operation as defined by the C++ memory model) where needed by hardware
to guarantee a reliable picture across contexts. Any
architecture-specific implementations are responsible for ensuring
this behavior.

## [Suggested Uses](#id7)

Use an atomic variable to implement critical section processing that only
requires the manipulation of a single 32-bit value.

Use multiple atomic variables to implement critical section processing
on a set of flag bits in a bit array longer than 32 bits.

Note

Using atomic variables is typically far more efficient than using
other techniques to implement critical sections such as using a mutex
or locking interrupts.

## [Configuration Options](#id8)

Related configuration options:

- [`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](../../../kconfig.md#CONFIG_ATOMIC_OPERATIONS_BUILTIN "CONFIG_ATOMIC_OPERATIONS_BUILTIN")
- [`CONFIG_ATOMIC_OPERATIONS_ARCH`](../../../kconfig.md#CONFIG_ATOMIC_OPERATIONS_ARCH "CONFIG_ATOMIC_OPERATIONS_ARCH")
- [`CONFIG_ATOMIC_OPERATIONS_C`](../../../kconfig.md#CONFIG_ATOMIC_OPERATIONS_C "CONFIG_ATOMIC_OPERATIONS_C")

## [API Reference](#id9)

Important

All atomic services APIs can be used by both threads and ISRs.

*group* atomic\_apis
:   Defines

    ATOMIC\_INIT(i)
    :   Initialize an atomic variable.

        This macro can be used to initialize an atomic variable. For example,

        ```text
        atomic_t my_var = ATOMIC_INIT(75);
        ```

        Parameters:
        :   - **i** – Value to assign to atomic variable.

    ATOMIC\_PTR\_INIT(p)
    :   Initialize an atomic pointer variable.

        This macro can be used to initialize an atomic pointer variable. For example,

        ```text
        atomic_ptr_t my_ptr = ATOMIC_PTR_INIT(&data);
        ```

        Parameters:
        :   - **p** – Pointer value to assign to atomic pointer variable.

    ATOMIC\_BITMAP\_SIZE(num\_bits)
    :   This macro computes the number of atomic variables necessary to represent a bitmap with *num\_bits*.

        Parameters:
        :   - **num\_bits** – Number of bits.

    ATOMIC\_DEFINE(name, num\_bits)
    :   Define an array of atomic variables.

        This macro defines an array of atomic variables containing at least *num\_bits* bits.

        Note

        If used from file scope, the bits of the array are initialized to zero; if used from within a function, the bits are left uninitialized.

        Parameters:
        :   - **name** – Name of array of atomic variables.
            - **num\_bits** – Number of bits needed.

    Functions

    static inline bool atomic\_test\_bit(const atomic\_t \*target, int bit)
    :   Atomically test a bit.

        This routine tests whether bit number *bit* of *target* is set or not. The target may be a single atomic variable or an array of them.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable or array.
            - **bit** – Bit number (starting from 0).

        Returns:
        :   true if the bit was set, false if it wasn’t.

    static inline bool atomic\_test\_and\_clear\_bit(atomic\_t \*target, int bit)
    :   Atomically test and clear a bit.

        Atomically clear bit number *bit* of *target* and return its old value. The target may be a single atomic variable or an array of them.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable or array.
            - **bit** – Bit number (starting from 0).

        Returns:
        :   false if the bit was already cleared, true if it wasn’t.

    static inline bool atomic\_test\_and\_set\_bit(atomic\_t \*target, int bit)
    :   Atomically set a bit.

        Atomically set bit number *bit* of *target* and return its old value. The target may be a single atomic variable or an array of them.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable or array.
            - **bit** – Bit number (starting from 0).

        Returns:
        :   true if the bit was already set, false if it wasn’t.

    static inline void atomic\_clear\_bit(atomic\_t \*target, int bit)
    :   Atomically clear a bit.

        Atomically clear bit number *bit* of *target*. The target may be a single atomic variable or an array of them.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable or array.
            - **bit** – Bit number (starting from 0).

    static inline void atomic\_set\_bit(atomic\_t \*target, int bit)
    :   Atomically set a bit.

        Atomically set bit number *bit* of *target*. The target may be a single atomic variable or an array of them.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable or array.
            - **bit** – Bit number (starting from 0).

    static inline void atomic\_set\_bit\_to(atomic\_t \*target, int bit, bool val)
    :   Atomically set a bit to a given value.

        Atomically set bit number *bit* of *target* to value *val*. The target may be a single atomic variable or an array of them.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable or array.
            - **bit** – Bit number (starting from 0).
            - **val** – true for 1, false for 0.

    bool atomic\_cas(atomic\_t \*target, atomic\_val\_t old\_value, atomic\_val\_t new\_value)
    :   Atomic compare-and-set.

        This routine performs an atomic compare-and-set on *target*. If the current value of *target* equals *old\_value*, *target* is set to *new\_value*. If the current value of *target* does not equal *old\_value*, *target* is left unchanged.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.
            - **old\_value** – Original value to compare against.
            - **new\_value** – New value to store.

        Returns:
        :   true if *new\_value* is written, false otherwise.

    bool atomic\_ptr\_cas(atomic\_ptr\_t \*target, atomic\_ptr\_val\_t old\_value, atomic\_ptr\_val\_t new\_value)
    :   Atomic compare-and-set with pointer values.

        This routine performs an atomic compare-and-set on *target*. If the current value of *target* equals *old\_value*, *target* is set to *new\_value*. If the current value of *target* does not equal *old\_value*, *target* is left unchanged.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.
            - **old\_value** – Original value to compare against.
            - **new\_value** – New value to store.

        Returns:
        :   true if *new\_value* is written, false otherwise.

    atomic\_val\_t atomic\_add(atomic\_t \*target, atomic\_val\_t value)
    :   Atomic addition.

        This routine performs an atomic addition on *target*.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.
            - **value** – Value to add.

        Returns:
        :   Previous value of *target*.

    atomic\_val\_t atomic\_sub(atomic\_t \*target, atomic\_val\_t value)
    :   Atomic subtraction.

        This routine performs an atomic subtraction on *target*.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.
            - **value** – Value to subtract.

        Returns:
        :   Previous value of *target*.

    atomic\_val\_t atomic\_inc(atomic\_t \*target)
    :   Atomic increment.

        This routine performs an atomic increment by 1 on *target*.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.

        Returns:
        :   Previous value of *target*.

    atomic\_val\_t atomic\_dec(atomic\_t \*target)
    :   Atomic decrement.

        This routine performs an atomic decrement by 1 on *target*.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.

        Returns:
        :   Previous value of *target*.

    atomic\_val\_t atomic\_get(const atomic\_t \*target)
    :   Atomic get.

        This routine performs an atomic read on *target*.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.

        Returns:
        :   Value of *target*.

    atomic\_ptr\_val\_t atomic\_ptr\_get(const atomic\_ptr\_t \*target)
    :   Atomic get a pointer value.

        This routine performs an atomic read on *target*.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of pointer variable.

        Returns:
        :   Value of *target*.

    atomic\_val\_t atomic\_set(atomic\_t \*target, atomic\_val\_t value)
    :   Atomic get-and-set.

        This routine atomically sets *target* to *value* and returns the previous value of *target*.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.
            - **value** – Value to write to *target*.

        Returns:
        :   Previous value of *target*.

    atomic\_ptr\_val\_t atomic\_ptr\_set(atomic\_ptr\_t \*target, atomic\_ptr\_val\_t value)
    :   Atomic get-and-set for pointer values.

        This routine atomically sets *target* to *value* and returns the previous value of *target*.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.
            - **value** – Value to write to *target*.

        Returns:
        :   Previous value of *target*.

    atomic\_val\_t atomic\_clear(atomic\_t \*target)
    :   Atomic clear.

        This routine atomically sets *target* to zero and returns its previous value. (Hence, it is equivalent to atomic\_set(target, 0).)

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.

        Returns:
        :   Previous value of *target*.

    atomic\_ptr\_val\_t atomic\_ptr\_clear(atomic\_ptr\_t \*target)
    :   Atomic clear of a pointer value.

        This routine atomically sets *target* to zero and returns its previous value. (Hence, it is equivalent to atomic\_set(target, 0).)

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.

        Returns:
        :   Previous value of *target*.

    atomic\_val\_t atomic\_or(atomic\_t \*target, atomic\_val\_t value)
    :   Atomic bitwise inclusive OR.

        This routine atomically sets *target* to the bitwise inclusive OR of *target* and *value*.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.
            - **value** – Value to OR.

        Returns:
        :   Previous value of *target*.

    atomic\_val\_t atomic\_xor(atomic\_t \*target, atomic\_val\_t value)
    :   Atomic bitwise exclusive OR (XOR).

        This routine atomically sets *target* to the bitwise exclusive OR (XOR) of *target* and *value*.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.
            - **value** – Value to XOR

        Returns:
        :   Previous value of *target*.

    atomic\_val\_t atomic\_and(atomic\_t \*target, atomic\_val\_t value)
    :   Atomic bitwise AND.

        This routine atomically sets *target* to the bitwise AND of *target* and *value*.

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.
            - **value** – Value to AND.

        Returns:
        :   Previous value of *target*.

    atomic\_val\_t atomic\_nand(atomic\_t \*target, atomic\_val\_t value)
    :   Atomic bitwise NAND.

        This routine atomically sets *target* to the bitwise NAND of *target* and *value*. (This operation is equivalent to target = ~(target & value).)

        Note

        As for all atomic APIs, includes a full/sequentially-consistent memory barrier (where applicable).

        Parameters:
        :   - **target** – Address of atomic variable.
            - **value** – Value to NAND.

        Returns:
        :   Previous value of *target*.
