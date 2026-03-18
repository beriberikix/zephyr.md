---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/util/index.html
original_path: kernel/util/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Utilities

This page contains reference documentation for `<sys/util.h>`, which provides
miscellaneous utility functions and macros.

*group* Utility Functions
:   **Since**
    :   2.4

    **Version**
    :   0.1.0

    Defines

    POINTER\_TO\_UINT(x)
    :   Cast `x`, a pointer, to an unsigned integer.

    UINT\_TO\_POINTER(x)
    :   Cast `x`, an unsigned integer, to a `void*`.

    POINTER\_TO\_INT(x)
    :   Cast `x`, a pointer, to a signed integer.

    INT\_TO\_POINTER(x)
    :   Cast `x`, a signed integer, to a `void*`.

    BITS\_PER\_LONG
    :   Number of bits in a long int.

    BITS\_PER\_LONG\_LONG
    :   Number of bits in a long long int.

    GENMASK(h, l)
    :   Create a contiguous bitmask starting at bit position `l` and ending at position `h`.

    GENMASK64(h, l)
    :   Create a contiguous 64-bit bitmask starting at bit position `l` and ending at position `h`.

    LSB\_GET(value)
    :   Extract the Least Significant Bit from `value`.

    FIELD\_GET(mask, value)
    :   Extract a bitfield element from `value` corresponding to the field mask `mask`.

    FIELD\_PREP(mask, value)
    :   Prepare a bitfield element using `value` with `mask` representing its field position and width.

        The result should be combined with other fields using a logical OR.

    ZERO\_OR\_COMPILE\_ERROR(cond)
    :   0 if `cond` is true-ish; causes a compile error otherwise.

    IS\_ARRAY(array)
    :   Zero if `array` has an array type, a compile error otherwise.

        This macro is available only from C, not C++.

    ARRAY\_SIZE(array)
    :   Number of elements in the given `array`.

        In C++, due to language limitations, this will accept as `array` any type that implements `operator[]`. The results may not be particularly meaningful in this case.

        In C, passing a pointer as `array` causes a compile error.

    IS\_ARRAY\_ELEMENT(array, ptr)
    :   Whether `ptr` is an element of `array`.

        This macro can be seen as a slightly stricter version of [PART\_OF\_ARRAY](#group__sys-util_1ga4fbecf59c021cb60fa1267b7818f90ef) in that it also ensures that `ptr` is aligned to an array-element boundary of `array`.

        In C, passing a pointer as `array` causes a compile error.

        Parameters:
        :   - **array** – the array in question
            - **ptr** – the pointer to check

        Returns:
        :   1 if `ptr` is part of `array`, 0 otherwise

    ARRAY\_INDEX(array, ptr)
    :   Index of `ptr` within `array`.

        With `CONFIG_ASSERT=y`, this macro will trigger a runtime assertion when `ptr` does not fall into the range of `array` or when `ptr` is not aligned to an array-element boundary of `array`.

        In C, passing a pointer as `array` causes a compile error.

        Parameters:
        :   - **array** – the array in question
            - **ptr** – pointer to an element of `array`

        Returns:
        :   the array index of `ptr` within `array`, on success

    PART\_OF\_ARRAY(array, ptr)
    :   Check if a pointer `ptr` lies within `array`.

        In C but not C++, this causes a compile error if `array` is not an array (e.g. if `ptr` and `array` are mixed up).

        Parameters:
        :   - **array** – an array
            - **ptr** – a pointer

        Returns:
        :   1 if `ptr` is part of `array`, 0 otherwise

    ARRAY\_INDEX\_FLOOR(array, ptr)
    :   Array-index of `ptr` within `array`, rounded down.

        This macro behaves much like [ARRAY\_INDEX](#group__sys-util_1ga27c31909224761e41d77118b41212d6b) with the notable difference that it accepts any `ptr` in the range of `array` rather than exclusively a `ptr` aligned to an array-element boundary of `array`.

        With `CONFIG_ASSERT=y`, this macro will trigger a runtime assertion when `ptr` does not fall into the range of `array`.

        In C, passing a pointer as `array` causes a compile error.

        Parameters:
        :   - **array** – the array in question
            - **ptr** – pointer to an element of `array`

        Returns:
        :   the array index of `ptr` within `array`, on success

    ARRAY\_FOR\_EACH(array, idx)
    :   Iterate over members of an array using an index variable.

        Parameters:
        :   - **array** – the array in question
            - **idx** – name of array index variable

    ARRAY\_FOR\_EACH\_PTR(array, ptr)
    :   Iterate over members of an array using a pointer.

        Parameters:
        :   - **array** – the array in question
            - **ptr** – pointer to an element of `array`

    SAME\_TYPE(a, b)
    :   Validate if two entities have a compatible type.

        Parameters:
        :   - **a** – the first entity to be compared
            - **b** – the second entity to be compared

        Returns:
        :   1 if the two elements are compatible, 0 if they are not

    CONTAINER\_OF\_VALIDATE(ptr, type, field)
    :   Validate CONTAINER\_OF parameters, only applies to C mode.

    CONTAINER\_OF(ptr, type, field)
    :   Get a pointer to a structure containing the element.

        Example:

        ```text
         struct foo {
            int bar;
         };

         struct foo my_foo;
         int *ptr = &my_foo.bar;

         struct foo *container = CONTAINER_OF(ptr, struct foo, bar);
        ```

        Above, `container` points at `my_foo`.

        Parameters:
        :   - **ptr** – pointer to a structure element
            - **type** – name of the type that `ptr` is an element of
            - **field** – the name of the field within the struct `ptr` points to

        Returns:
        :   a pointer to the structure that contains `ptr`

    SIZEOF\_FIELD(type, member)
    :   Report the size of a struct field in bytes.

        Parameters:
        :   - **type** – The structure containing the field of interest.
            - **member** – The field to return the size of.

        Returns:
        :   The field size.

    CONCAT(...)
    :   Concatenate input arguments.

        Concatenate provided tokens into a combined token during the preprocessor pass. This can be used to, for ex., build an identifier out of multiple parts, where one of those parts may be, for ex, a number, another macro, or a macro argument.

        Parameters:
        :   - **...** – Tokens to concatencate

        Returns:
        :   Concatenated token.

    IS\_ALIGNED(ptr, align)
    :   Check if `ptr` is aligned to `align` alignment.

    ROUND\_UP(x, align)
    :   Value of `x` rounded up to the next multiple of `align`.

    ROUND\_DOWN(x, align)
    :   Value of `x` rounded down to the previous multiple of `align`.

    WB\_UP(x)
    :   Value of `x` rounded up to the next word boundary.

    WB\_DN(x)
    :   Value of `x` rounded down to the previous word boundary.

    DIV\_ROUND\_UP(n, d)
    :   Divide and round up.

        Example:

        ```c
        DIV_ROUND_UP(1, 2); // 1
        DIV_ROUND_UP(3, 2); // 2
        ```

        Parameters:
        :   - **n** – Numerator.
            - **d** – Denominator.

        Returns:
        :   The result of `n` / `d`, rounded up.

    DIV\_ROUND\_CLOSEST(n, d)
    :   Divide and round to the nearest integer.

        Example:

        ```c
        DIV_ROUND_CLOSEST(5, 2); // 3
        DIV_ROUND_CLOSEST(5, -2); // -3
        DIV_ROUND_CLOSEST(5, 3); // 2
        ```

        Parameters:
        :   - **n** – Numerator.
            - **d** – Denominator.

        Returns:
        :   The result of `n` / `d`, rounded to the nearest integer.

    ceiling\_fraction(numerator, divider)
    :   Ceiling function applied to `numerator` / `divider` as a fraction.

        *Deprecated:*
        :   Use [DIV\_ROUND\_UP()](#group__sys-util_1gae664e7492e37d324831caf2321ddda37) instead.

    MAX(a, b)
    :   Obtain the maximum of two values.

        Note

        Arguments are evaluated twice. Use Z\_MAX for a GCC-only, single evaluation version

        Parameters:
        :   - **a** – First value.
            - **b** – Second value.

        Returns:
        :   Maximum value of `a` and `b`.

    MIN(a, b)
    :   Obtain the minimum of two values.

        Note

        Arguments are evaluated twice. Use Z\_MIN for a GCC-only, single evaluation version

        Parameters:
        :   - **a** – First value.
            - **b** – Second value.

        Returns:
        :   Minimum value of `a` and `b`.

    CLAMP(val, low, high)
    :   Clamp a value to a given range.

        Note

        Arguments are evaluated multiple times. Use Z\_CLAMP for a GCC-only, single evaluation version.

        Parameters:
        :   - **val** – Value to be clamped.
            - **low** – Lowest allowed value (inclusive).
            - **high** – Highest allowed value (inclusive).

        Returns:
        :   Clamped value.

    IN\_RANGE(val, min, max)
    :   Checks if a value is within range.

        Note

        `val` is evaluated twice.

        Parameters:
        :   - **val** – Value to be checked.
            - **min** – Lower bound (inclusive).
            - **max** – Upper bound (inclusive).

        Return values:
        :   - **true** – If value is within range
            - **false** – If the value is not within range

    LOG2(x)
    :   Compute log2(x).

        Note

        This macro expands its argument multiple times (to permit use in constant expressions), which must not have side effects.

        Parameters:
        :   - **x** – An unsigned integral value to compute logarithm of (positive only)

        Returns:
        :   log2(x) when 1 <= x <= max(x), -1 when x < 1

    LOG2CEIL(x)
    :   Compute ceil(log2(x)).

        Note

        This macro expands its argument multiple times (to permit use in constant expressions), which must not have side effects.

        Parameters:
        :   - **x** – An unsigned integral value

        Returns:
        :   ceil(log2(x)) when 1 <= x <= max(type(x)), 0 when x < 1

    NHPOT(x)
    :   Compute next highest power of two.

        Equivalent to 2^ceil(log2(x))

        Note

        This macro expands its argument multiple times (to permit use in constant expressions), which must not have side effects.

        Parameters:
        :   - **x** – An unsigned integral value

        Returns:
        :   2^ceil(log2(x)) or 0 if 2^ceil(log2(x)) would saturate 64-bits

    KB(x)
    :   Number of bytes in `x` kibibytes.

    MB(x)
    :   Number of bytes in `x` mebibytes.

    GB(x)
    :   Number of bytes in `x` gibibytes.

    KHZ(x)
    :   Number of Hz in `x` kHz.

    MHZ(x)
    :   Number of Hz in `x` MHz.

    WAIT\_FOR(expr, timeout, delay\_stmt)
    :   Wait for an expression to return true with a timeout.

        Spin on an expression with a timeout and optional delay between iterations

        Commonly needed when waiting on hardware to complete an asynchronous request to read/write/initialize/reset, but useful for any expression.

        Parameters:
        :   - **expr** – Truth expression upon which to poll, e.g.: XYZREG & XYZREG\_EN
            - **timeout** – Timeout to wait for in microseconds, e.g.: 1000 (1ms)
            - **delay\_stmt** – Delay statement to perform each poll iteration e.g.: NULL, [k\_yield()](../services/threads/index.md#group__thread__apis_1ga08a3484c33444ecedc2d71d78495a295), k\_msleep(1) or k\_busy\_wait(1)

        Return values:
        :   **expr** – As a boolean return, if false then it has timed out.

    BIT(n)
    :   Unsigned integer with bit position `n` set (signed in assembly language).

    BIT64(\_n)
    :   64-bit unsigned integer with bit position `_n` set.

    WRITE\_BIT(var, bit, set)
    :   Set or clear a bit depending on a boolean value.

        The argument `var` is a variable whose value is written to as a side effect.

        Parameters:
        :   - **var** – Variable to be altered
            - **bit** – Bit number
            - **set** – if 0, clears `bit` in `var`; any other value sets `bit`

    BIT\_MASK(n)
    :   Bit mask with bits 0 through `n-1` (inclusive) set, or 0 if `n` is 0.

    BIT64\_MASK(n)
    :   64-bit bit mask with bits 0 through `n-1` (inclusive) set, or 0 if `n` is 0.

    IS\_POWER\_OF\_TWO(x)
    :   Check if a `x` is a power of two.

    IS\_SHIFTED\_BIT\_MASK(m, s)
    :   Check if bits are set continuously from the specified bit.

        The macro is not dependent on the bit-width.

        Parameters:
        :   - **m** – Check whether the bits are set continuously or not.
            - **s** – Specify the lowest bit for that is continuously set bits.

    IS\_BIT\_MASK(m)
    :   Check if bits are set continuously from the LSB.

        Parameters:
        :   - **m** – Check whether the bits are set continuously from LSB.

    IS\_ENABLED(config\_macro)
    :   Check for macro definition in compiler-visible expressions.

        This trick was pioneered in Linux as the config\_enabled() macro. It has the effect of taking a macro value that may be defined to “1” or may not be defined at all and turning it into a literal expression that can be handled by the C compiler instead of just the preprocessor. It is often used with a `CONFIG_FOO` macro which may be defined to 1 via Kconfig, or left undefined.

        That is, it works similarly to `#if defined(CONFIG_FOO)` except that its expansion is a C expression. Thus, much `#ifdef` usage can be replaced with equivalents like:

        ```text
        if (IS_ENABLED(CONFIG_FOO)) {
                do_something_with_foo
        }
        ```

        This is cleaner since the compiler can generate errors and warnings for `do_something_with_foo` even when `CONFIG_FOO` is undefined.

        Note: Use of IS\_ENABLED in a `#if` statement is discouraged as it doesn’t provide any benefit vs plain `#if defined()`

        Parameters:
        :   - **config\_macro** – Macro to check

        Returns:
        :   1 if `config_macro` is defined to 1, 0 otherwise (including if `config_macro` is not defined)

    COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)
    :   Insert code depending on whether `_flag` expands to 1 or not.

        This relies on similar tricks as [IS\_ENABLED()](#group__sys-util_1ga111fe4e9d63758262fc6810a782cb32a), but as the result of `_flag` expansion, results in either `_if_1_code` or `_else_code` is expanded.

        To prevent the preprocessor from treating commas as argument separators, the `_if_1_code` and `_else_code` expressions must be inside brackets/parentheses: `()`. These are stripped away during macro expansion.

        Example:

        ```text
        COND_CODE_1(CONFIG_FLAG, (uint32_t x;), (there_is_no_flag();))
        ```

        If `CONFIG_FLAG` is defined to 1, this expands to:

        ```text
        uint32_t x;
        ```

        It expands to `there_is_no_flag();` otherwise.

        This could be used as an alternative to:

        ```text
        #if defined(CONFIG_FLAG) && (CONFIG_FLAG == 1)
        #define MAYBE_DECLARE(x) uint32_t x
        #else
        #define MAYBE_DECLARE(x) there_is_no_flag()
        #endif

        MAYBE_DECLARE(x);
        ```

        However, the advantage of [COND\_CODE\_1()](#group__sys-util_1ga358bc3e7669c860a98839a51cd526b20) is that code is resolved in place where it is used, while the `#if` method defines `MAYBE_DECLARE` on two lines and requires it to be invoked again on a separate line. This makes [COND\_CODE\_1()](#group__sys-util_1ga358bc3e7669c860a98839a51cd526b20) more concise and also sometimes more useful when used within another macro’s expansion.

        Note

        `_flag` can be the result of preprocessor expansion, e.g. an expression involving `[NUM_VA_ARGS_LESS_1(...)](#group__sys-util_1ga8a0e9835e0a8f864ffc2359b9c419cc2)`. However, `_if_1_code` is only expanded if `_flag` expands to the integer literal 1. Integer expressions that evaluate to 1, e.g. after doing some arithmetic, will not work.

        Parameters:
        :   - **\_flag** – evaluated flag
            - **\_if\_1\_code** – result if `_flag` expands to 1; must be in parentheses
            - **\_else\_code** – result otherwise; must be in parentheses

    COND\_CODE\_0(\_flag, \_if\_0\_code, \_else\_code)
    :   Like [COND\_CODE\_1()](#group__sys-util_1ga358bc3e7669c860a98839a51cd526b20) except tests if `_flag` is 0.

        This is like [COND\_CODE\_1()](#group__sys-util_1ga358bc3e7669c860a98839a51cd526b20), except that it tests whether `_flag` expands to the integer literal 0. It expands to `_if_0_code` if so, and `_else_code` otherwise; both of these must be enclosed in parentheses.

        See also

        [COND\_CODE\_1()](#group__sys-util_1ga358bc3e7669c860a98839a51cd526b20)

        Parameters:
        :   - **\_flag** – evaluated flag
            - **\_if\_0\_code** – result if `_flag` expands to 0; must be in parentheses
            - **\_else\_code** – result otherwise; must be in parentheses

    IF\_ENABLED(\_flag, \_code)
    :   Insert code if `_flag` is defined and equals 1.

        Like [COND\_CODE\_1()](#group__sys-util_1ga358bc3e7669c860a98839a51cd526b20), this expands to `_code` if `_flag` is defined to 1; it expands to nothing otherwise.

        Example:

        ```text
        IF_ENABLED(CONFIG_FLAG, (uint32_t foo;))
        ```

        If `CONFIG_FLAG` is defined to 1, this expands to:

        ```text
        uint32_t foo;
        ```

        and to nothing otherwise.

        It can be considered as a more compact alternative to:

        ```text
        #if defined(CONFIG_FLAG) && (CONFIG_FLAG == 1)
        uint32_t foo;
        #endif
        ```

        Parameters:
        :   - **\_flag** – evaluated flag
            - **\_code** – result if `_flag` expands to 1; must be in parentheses

    IF\_DISABLED(\_flag, \_code)
    :   Insert code if `_flag` is not defined as 1.

        This expands to nothing if `_flag` is defined and equal to 1; it expands to `_code` otherwise.

        Example:

        ```text
        IF_DISABLED(CONFIG_FLAG, (uint32_t foo;))
        ```

        If `CONFIG_FLAG` isn’t defined or different than 1, this expands to:

        ```text
        uint32_t foo;
        ```

        and to nothing otherwise.

        IF\_DISABLED does the opposite of IF\_ENABLED.

        Parameters:
        :   - **\_flag** – evaluated flag
            - **\_code** – result if `_flag` does not expand to 1; must be in parentheses

    IS\_EMPTY(...)
    :   Check if a macro has a replacement expression.

        If `a` is a macro defined to a nonempty value, this will return true, otherwise it will return false. It only works with defined macros, so an additional `#ifdef` test may be needed in some cases.

        This macro may be used with [COND\_CODE\_1()](#group__sys-util_1ga358bc3e7669c860a98839a51cd526b20) and [COND\_CODE\_0()](#group__sys-util_1ga5483ea38af79bc6c4509936288705377) while processing `__VA_ARGS__` to avoid processing empty arguments.

        Example:

        ```text
         #define EMPTY
         #define NON_EMPTY  1
         #undef  UNDEFINED
         IS_EMPTY(EMPTY)
         IS_EMPTY(NON_EMPTY)
         IS_EMPTY(UNDEFINED)
         #if defined(EMPTY) && IS_EMPTY(EMPTY) == true
         some_conditional_code
         #endif
        ```

        In above examples, the invocations of [IS\_EMPTY(…)](#group__sys-util_1gab9487eea703d51cb1f235432dab4a1c7) return `true`, `false`, and `true`; `some_conditional_code` is included.

        Parameters:
        :   - **...** – macro to check for emptiness (may be `__VA_ARGS__`)

    IS\_EQ(a, b)
    :   Like `a == b`, but does evaluation and short-circuiting at C preprocessor time.

        This however only works for integer literal from 0 to 4095.

    LIST\_DROP\_EMPTY(...)
    :   Remove empty arguments from list.

        During macro expansion, `__VA_ARGS__` and other preprocessor generated lists may contain empty elements, e.g.:

        ```text
         #define LIST ,a,b,,d,
        ```

        Using EMPTY to show each empty element, LIST contains:

        ```text
         EMPTY, a, b, EMPTY, d
        ```

        When processing such lists, e.g. using [FOR\_EACH()](#group__sys-util_1ga278c8b7cbbea2f585e371d3568f3cb12), all empty elements will be processed, and may require filtering out. To make that process easier, it is enough to invoke LIST\_DROP\_EMPTY which will remove all empty elements.

        Example:

        ```text
         LIST_DROP_EMPTY(LIST)
        ```

        expands to:

        ```text
         a, b, d
        ```

        Parameters:
        :   - **...** – list to be processed

    EMPTY
    :   Macro with an empty expansion.

        This trivial definition is provided for readability when a macro should expand to an empty result, which e.g. is sometimes needed to silence checkpatch.

        Example:

        ```text
         #define LIST_ITEM(n) , item##n
        ```

        The above would cause checkpatch to complain, but:

        ```text
         #define LIST_ITEM(n) EMPTY, item##n
        ```

        would not.

    IDENTITY(V)
    :   Macro that expands to its argument.

        This is useful in macros like `[FOR_EACH()](#group__sys-util_1ga278c8b7cbbea2f585e371d3568f3cb12)` when there is no transformation required on the list elements.

        Parameters:
        :   - **V** – any value

    GET\_ARG\_N(N, ...)
    :   Get nth argument from argument list.

        Parameters:
        :   - **N** – Argument index to fetch. Counter from 1.
            - **...** – Variable list of arguments from which one argument is returned.

        Returns:
        :   Nth argument.

    GET\_ARGS\_LESS\_N(N, ...)
    :   Strips n first arguments from the argument list.

        Parameters:
        :   - **N** – Number of arguments to discard.
            - **...** – Variable list of arguments.

        Returns:
        :   argument list without N first arguments.

    UTIL\_OR(a, b)
    :   Like `a || b`, but does evaluation and short-circuiting at C preprocessor time.

        This is not the same as the binary `||` operator; in particular, `a` should expand to an integer literal 0 or 1. However, `b` can be any value.

        This can be useful when `b` is an expression that would cause a build error when `a` is 1.

    UTIL\_AND(a, b)
    :   Like `a && b`, but does evaluation and short-circuiting at C preprocessor time.

        This is not the same as the binary `&&`, however; in particular, `a` should expand to an integer literal 0 or 1. However, `b` can be any value.

        This can be useful when `b` is an expression that would cause a build error when `a` is 0.

    UTIL\_INC(x)
    :   [UTIL\_INC(x)](#group__sys-util_1ga90a54212306c3e210ac87fd0bd7b32da) for an integer literal x from 0 to 4095 expands to an integer literal whose value is x+1.

        See also

        [UTIL\_DEC(x)](#group__sys-util_1gaa7623e1e33316024217094698e4d8258)

    UTIL\_DEC(x)
    :   [UTIL\_DEC(x)](#group__sys-util_1gaa7623e1e33316024217094698e4d8258) for an integer literal x from 0 to 4095 expands to an integer literal whose value is x-1.

        See also

        [UTIL\_INC(x)](#group__sys-util_1ga90a54212306c3e210ac87fd0bd7b32da)

    UTIL\_X2(y)
    :   [UTIL\_X2(y)](#group__sys-util_1gab23deac75762adfb6bdde2c15d51f158) for an integer literal y from 0 to 4095 expands to an integer literal whose value is 2y.

    LISTIFY(LEN, F, sep, ...)
    :   Generates a sequence of code with configurable separator.

        Example:

        ```text
        #define FOO(i, _) MY_PWM ## i
        { LISTIFY(PWM_COUNT, FOO, (,)) }
        ```

        The above two lines expand to:

        { MY\_PWM0 , MY\_PWM1 }

        Note

        Calling LISTIFY with undefined arguments has undefined behavior.

        Parameters:
        :   - **LEN** – The length of the sequence. Must be an integer literal less than 4095.
            - **F** – A macro function that accepts at least two arguments: `F(i, ...)`. `F` is called repeatedly in the expansion. Its first argument `i` is the index in the sequence, and the variable list of arguments passed to LISTIFY are passed through to `F`.
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.

    FOR\_EACH(F, sep, ...)
    :   Call a macro `F` on each provided argument with a given separator between each call.

        Example:

        ```text
        #define F(x) int a##x
        FOR_EACH(F, (;), 4, 5, 6);
        ```

        This expands to:

        ```text
        int a4;
        int a5;
        int a6;
        ```

        Parameters:
        :   - **F** – Macro to invoke
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.
            - **...** – Variable argument list. The macro `F` is invoked as `F(element)` for each element in the list.

    FOR\_EACH\_NONEMPTY\_TERM(F, term, ...)
    :   Like [FOR\_EACH()](#group__sys-util_1ga278c8b7cbbea2f585e371d3568f3cb12), but with a terminator instead of a separator, and drops empty elements from the argument list.

        The `sep` argument to `[FOR_EACH(F, (sep), a, b)](#group__sys-util_1ga278c8b7cbbea2f585e371d3568f3cb12)` is a separator which is placed between calls to `F`, like this:

        ```text
        FOR_EACH(F, (sep), a, b) // F(a) sep F(b)
                                 //               ^^^ no sep here!
        ```

        By contrast, the `term` argument to `[FOR_EACH_NONEMPTY_TERM(F, (term),a, b)](#group__sys-util_1ga24b3862161d725f5503b1bb08f4e339f)` is added after each time `F` appears in the expansion:

        ```text
        FOR_EACH_NONEMPTY_TERM(F, (term), a, b) // F(a) term F(b) term
                                                //                ^^^^
        ```

        Further, any empty elements are dropped:

        ```text
        FOR_EACH_NONEMPTY_TERM(F, (term), a, EMPTY, b) // F(a) term F(b) term
        ```

        This is more convenient in some cases, because [FOR\_EACH\_NONEMPTY\_TERM()](#group__sys-util_1ga24b3862161d725f5503b1bb08f4e339f) expands to nothing when given an empty argument list, and it’s often cumbersome to write a macro `F` that does the right thing even when given an empty argument.

        One example is when `__VA_ARGS__` may or may not be empty, and the results are embedded in a larger initializer:

        ```text
        #define SQUARE(x) ((x)*(x))

        int my_array[] = {
                FOR_EACH_NONEMPTY_TERM(SQUARE, (,), FOO(...))
                FOR_EACH_NONEMPTY_TERM(SQUARE, (,), BAR(...))
                FOR_EACH_NONEMPTY_TERM(SQUARE, (,), BAZ(...))
        };
        ```

        This is more convenient than:

        1. figuring out whether the `FOO`, `BAR`, and `BAZ` expansions are empty and adding a comma manually (or not) between [FOR\_EACH()](#group__sys-util_1ga278c8b7cbbea2f585e371d3568f3cb12) calls
        2. rewriting SQUARE so it reacts appropriately when “x” is empty (which would be necessary if e.g. `FOO` expands to nothing)

        Parameters:
        :   - **F** – Macro to invoke on each nonempty element of the variable arguments
            - **term** – Terminator (e.g. comma or semicolon) placed after each invocation of F. Must be in parentheses; this is required to enable providing a comma as separator.
            - **...** – Variable argument list. The macro `F` is invoked as `F(element)` for each nonempty element in the list.

    FOR\_EACH\_IDX(F, sep, ...)
    :   Call macro `F` on each provided argument, with the argument’s index as an additional parameter.

        This is like [FOR\_EACH()](#group__sys-util_1ga278c8b7cbbea2f585e371d3568f3cb12), except `F` should be a macro which takes two arguments: `F(index, variable_arg)`.

        Example:

        ```text
        #define F(idx, x) int a##idx = x
        FOR_EACH_IDX(F, (;), 4, 5, 6);
        ```

        This expands to:

        ```text
        int a0 = 4;
        int a1 = 5;
        int a2 = 6;
        ```

        Parameters:
        :   - **F** – Macro to invoke
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.
            - **...** – Variable argument list. The macro `F` is invoked as `F(index, element)` for each element in the list.

    FOR\_EACH\_FIXED\_ARG(F, sep, fixed\_arg, ...)
    :   Call macro `F` on each provided argument, with an additional fixed argument as a parameter.

        This is like [FOR\_EACH()](#group__sys-util_1ga278c8b7cbbea2f585e371d3568f3cb12), except `F` should be a macro which takes two arguments: `F(variable_arg, fixed_arg)`.

        Example:

        ```text
        static void func(int val, void *dev);
        FOR_EACH_FIXED_ARG(func, (;), dev, 4, 5, 6);
        ```

        This expands to:

        ```text
        func(4, dev);
        func(5, dev);
        func(6, dev);
        ```

        Parameters:
        :   - **F** – Macro to invoke
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.
            - **fixed\_arg** – Fixed argument passed to `F` as the second macro parameter.
            - **...** – Variable argument list. The macro `F` is invoked as `F(element, fixed_arg)` for each element in the list.

    FOR\_EACH\_IDX\_FIXED\_ARG(F, sep, fixed\_arg, ...)
    :   Calls macro `F` for each variable argument with an index and fixed argument.

        This is like the combination of [FOR\_EACH\_IDX()](#group__sys-util_1ga069f709e18eeafb8d276b5ff4fc09d31) with [FOR\_EACH\_FIXED\_ARG()](#group__sys-util_1ga1a2b2aa21d7cc37f33e6a62abd2ae340).

        Example:

        ```text
        #define F(idx, x, fixed_arg) int fixed_arg##idx = x
        FOR_EACH_IDX_FIXED_ARG(F, (;), a, 4, 5, 6);
        ```

        This expands to:

        ```text
        int a0 = 4;
        int a1 = 5;
        int a2 = 6;
        ```

        Parameters:
        :   - **F** – Macro to invoke
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; This is required to enable providing a comma as separator.
            - **fixed\_arg** – Fixed argument passed to `F` as the third macro parameter.
            - **...** – Variable list of arguments. The macro `F` is invoked as `F(index, element, fixed_arg)` for each element in the list.

    REVERSE\_ARGS(...)
    :   Reverse arguments order.

        Parameters:
        :   - **...** – Variable argument list.

    NUM\_VA\_ARGS\_LESS\_1(...)
    :   Number of arguments in the variable arguments list minus one.

        Note

        Supports up to 64 arguments.

        Parameters:
        :   - **...** – List of arguments

        Returns:
        :   Number of variadic arguments in the argument list, minus one

    NUM\_VA\_ARGS(...)
    :   Number of arguments in the variable arguments list.

        Note

        Supports up to 63 arguments.

        Parameters:
        :   - **...** – List of arguments

        Returns:
        :   Number of variadic arguments in the argument list

    MACRO\_MAP\_CAT(...)
    :   Mapping macro that pastes results together.

        This is similar to [FOR\_EACH()](#group__sys-util_1ga278c8b7cbbea2f585e371d3568f3cb12) in that it invokes a macro repeatedly on each element of `__VA_ARGS__`. However, unlike [FOR\_EACH()](#group__sys-util_1ga278c8b7cbbea2f585e371d3568f3cb12), [MACRO\_MAP\_CAT()](#group__sys-util_1gaf82371bd6bf317add5276fc6cbd66662) pastes the results together into a single token.

        For example, with this macro FOO:

        ```text
        #define FOO(x) item_##x##_
        ```

        `[MACRO_MAP_CAT(FOO, a, b, c)](#group__sys-util_1gaf82371bd6bf317add5276fc6cbd66662),` expands to the token:

        ```text
        item_a_item_b_item_c_
        ```

        Parameters:
        :   - **...** – Macro to expand on each argument, followed by its arguments. (The macro should take exactly one argument.)

        Returns:
        :   The results of expanding the macro on each argument, all pasted together

    MACRO\_MAP\_CAT\_N(N, ...)
    :   Mapping macro that pastes a fixed number of results together.

        Similar to [MACRO\_MAP\_CAT()](#group__sys-util_1gaf82371bd6bf317add5276fc6cbd66662), but expects a fixed number of arguments. If more arguments are given than are expected, the rest are ignored.

        Parameters:
        :   - **N** – Number of arguments to map
            - **...** – Macro to expand on each argument, followed by its arguments. (The macro should take exactly one argument.)

        Returns:
        :   The results of expanding the macro on each argument, all pasted together

    Functions

    static inline bool is\_power\_of\_two(unsigned int x)
    :   Is `x` a power of two?

        Parameters:
        :   - **x** – value to check

        Returns:
        :   true if `x` is a power of two, false otherwise

    ALWAYS\_INLINE static bool is\_null\_no\_warn(void \*p)
    :   Is `p` equal to `NULL`?

        Some macros may need to check their arguments against NULL to support multiple use-cases, but NULL checks can generate warnings if such a macro is used in contexts where that particular argument can never be NULL.

        The warnings can be triggered if: a) all macros are expanded (e.g. when using CONFIG\_COMPILER\_SAVE\_TEMPS=y) or b) tracking of macro expansions are turned off (-ftrack-macro-expansion=0)

        The warnings can be circumvented by using this inline function for doing the NULL check within the macro. The compiler is still able to optimize the NULL check out at a later stage.

        Parameters:
        :   - **p** – Pointer to check

        Returns:
        :   true if `p` is equal to `NULL`, false otherwise

    static inline int64\_t arithmetic\_shift\_right(int64\_t value, uint8\_t shift)
    :   Arithmetic shift right.

        Parameters:
        :   - **value** – value to shift
            - **shift** – number of bits to shift

        Returns:
        :   `value` shifted right by `shift`; opened bit positions are filled with the sign bit

    static inline void bytecpy(void \*dst, const void \*src, size\_t size)
    :   byte by byte memcpy.

        Copy `size` bytes of `src` into `dest`. This is guaranteed to be done byte by byte.

        Parameters:
        :   - **dst** – Pointer to the destination memory.
            - **src** – Pointer to the source of the data.
            - **size** – The number of bytes to copy.

    static inline void byteswp(void \*a, void \*b, size\_t size)
    :   byte by byte swap.

        Swap *size* bytes between memory regions *a* and *b*. This is guaranteed to be done byte by byte.

        Parameters:
        :   - **a** – Pointer to the first memory region.
            - **b** – Pointer to the second memory region.
            - **size** – The number of bytes to swap.

    int char2hex(char c, uint8\_t \*x)
    :   Convert a single character into a hexadecimal nibble.

        Parameters:
        :   - **c** – The character to convert
            - **x** – The address of storage for the converted number.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int hex2char(uint8\_t x, char \*c)
    :   Convert a single hexadecimal nibble into a character.

        Parameters:
        :   - **c** – The number to convert
            - **x** – The address of storage for the converted character.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    size\_t bin2hex(const uint8\_t \*buf, size\_t buflen, char \*hex, size\_t hexlen)
    :   Convert a binary array into string representation.

        Parameters:
        :   - **buf** – The binary array to convert
            - **buflen** – The length of the binary array to convert
            - **hex** – Address of where to store the string representation.
            - **hexlen** – Size of the storage area for string representation.

        Returns:
        :   The length of the converted string, or 0 if an error occurred.

    size\_t hex2bin(const char \*hex, size\_t hexlen, uint8\_t \*buf, size\_t buflen)
    :   Convert a hexadecimal string into a binary array.

        Parameters:
        :   - **hex** – The hexadecimal string to convert
            - **hexlen** – The length of the hexadecimal string to convert.
            - **buf** – Address of where to store the binary data
            - **buflen** – Size of the storage area for binary data

        Returns:
        :   The length of the binary array, or 0 if an error occurred.

    static inline uint8\_t bcd2bin(uint8\_t bcd)
    :   Convert a binary coded decimal (BCD 8421) value to binary.

        Parameters:
        :   - **bcd** – BCD 8421 value to convert.

        Returns:
        :   Binary representation of input value.

    static inline uint8\_t bin2bcd(uint8\_t bin)
    :   Convert a binary value to binary coded decimal (BCD 8421).

        Parameters:
        :   - **bin** – Binary value to convert.

        Returns:
        :   BCD 8421 representation of input value.

    uint8\_t u8\_to\_dec(char \*buf, uint8\_t buflen, uint8\_t value)
    :   Convert a uint8\_t into a decimal string representation.

        Convert a uint8\_t value into its ASCII decimal string representation. The string is terminated if there is enough space in buf.

        Parameters:
        :   - **buf** – Address of where to store the string representation.
            - **buflen** – Size of the storage area for string representation.
            - **value** – The value to convert to decimal string

        Returns:
        :   The length of the converted string (excluding terminator if any), or 0 if an error occurred.

    static inline int32\_t sign\_extend(uint32\_t value, uint8\_t index)
    :   Sign extend an 8, 16 or 32 bit value using the index bit as sign bit.

        Parameters:
        :   - **value** – The value to sign expand.
            - **index** – 0 based bit index to sign bit (0 to 31)

    static inline int64\_t sign\_extend\_64(uint64\_t value, uint8\_t index)
    :   Sign extend a 64 bit value using the index bit as sign bit.

        Parameters:
        :   - **value** – The value to sign expand.
            - **index** – 0 based bit index to sign bit (0 to 63)

    char \*utf8\_trunc(char \*utf8\_str)
    :   Properly truncate a NULL-terminated UTF-8 string.

        Take a NULL-terminated UTF-8 string and ensure that if the string has been truncated (by setting the NULL terminator) earlier by other means, that the string ends with a properly formatted UTF-8 character (1-4 bytes).

        Parameters:
        :   - **utf8\_str** – NULL-terminated string

        Returns:
        :   Pointer to the `utf8_str`

    char \*utf8\_lcpy(char \*dst, const char \*src, size\_t n)
    :   Copies a UTF-8 encoded string from `src` to `dst`.

        The resulting `dst` will always be NULL terminated if `n` is larger than 0, and the `dst` string will always be properly UTF-8 truncated.

        Parameters:
        :   - **dst** – The destination of the UTF-8 string.
            - **src** – The source string
            - **n** – The size of the `dst` buffer. Maximum number of characters copied is `n` - 1. If 0 nothing will be done, and the `dst` will not be NULL terminated.

        Returns:
        :   Pointer to the `dst`

    static inline void mem\_xor\_n(uint8\_t \*dst, const uint8\_t \*src1, const uint8\_t \*src2, size\_t len)
    :   XOR n bytes.

        Parameters:
        :   - **dst** – Destination of where to store result. Shall be `len` bytes.
            - **src1** – First source. Shall be `len` bytes.
            - **src2** – Second source. Shall be `len` bytes.
            - **len** – Number of bytes to XOR.

    static inline void mem\_xor\_32(uint8\_t dst[4], const uint8\_t src1[4], const uint8\_t src2[4])
    :   XOR 32 bits.

        Parameters:
        :   - **dst** – Destination of where to store result. Shall be 32 bits.
            - **src1** – First source. Shall be 32 bits.
            - **src2** – Second source. Shall be 32 bits.

    static inline void mem\_xor\_128(uint8\_t dst[16], const uint8\_t src1[16], const uint8\_t src2[16])
    :   XOR 128 bits.

        Parameters:
        :   - **dst** – Destination of where to store result. Shall be 128 bits.
            - **src1** – First source. Shall be 128 bits.
            - **src2** – Second source. Shall be 128 bits.
