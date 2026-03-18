---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/iterable_sections/index.html
original_path: kernel/iterable_sections/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Iterable Sections

This page contains the reference documentation for the iterable sections APIs,
which can be used for defining iterable areas of equally-sized data structures,
that can be iterated on using [`STRUCT_SECTION_FOREACH`](#c.STRUCT_SECTION_FOREACH).

## Usage

Iterable section elements are typically used by defining the data structure and
associated initializer in a common header file, so that they can be
instantiated anywhere in the code base.

```c
struct my_data {
         int a, b;
};

#define DEFINE_DATA(name, _a, _b) \
         STRUCT_SECTION_ITERABLE(my_data, name) = { \
                 .a = _a, \
                 .b = _b, \
         }

...

DEFINE_DATA(d1, 1, 2);
DEFINE_DATA(d2, 3, 4);
DEFINE_DATA(d3, 5, 6);
```

Then the linker has to be setup to place the place the structure in a
contiguous segment using one of the linker macros such as
[`ITERABLE_SECTION_RAM`](#c.ITERABLE_SECTION_RAM) or [`ITERABLE_SECTION_ROM`](#c.ITERABLE_SECTION_ROM). Custom
linker snippets are normally declared using one of the
`zephyr_linker_sources()` CMake functions, using the appropriate section
identifier, `DATA_SECTIONS` for RAM structures and `SECTIONS` for ROM ones.

```cmake
# CMakeLists.txt
zephyr_linker_sources(DATA_SECTIONS iterables.ld)
```

```c
# iterables.ld
ITERABLE_SECTION_RAM(my_data, 4)
```

The data can then be accessed using [`STRUCT_SECTION_FOREACH`](#c.STRUCT_SECTION_FOREACH).

```c
STRUCT_SECTION_FOREACH(my_data, data) {
        printk("%p: a: %d, b: %d\n", data, data->a, data->b);
}
```

Note

The linker is going to place the entries sorted by name, so the example
above would visit `d1`, `d2` and `d3` in that order, regardless of how
they were defined in the code.

## API Reference

*group* Iterable Sections APIs
:   Iterable Sections APIs.

    Defines

    ITERABLE\_SECTION\_ROM(struct\_type, subalign)
    :   Define a read-only iterable section output.

        Define an output section which will set up an iterable area of equally-sized data structures. For use with [STRUCT\_SECTION\_ITERABLE()](#group__iterable__section__apis_1ga9104f42cbe4a67a931bed7f7cc8f600f). Input sections will be sorted by name, per ld’s SORT\_BY\_NAME.

        This macro should be used for read-only data.

        Note that this keeps the symbols in the image even though they are not being directly referenced. Use this when symbols are indirectly referenced by iterating through the section.

    ITERABLE\_SECTION\_ROM\_NUMERIC(struct\_type, subalign)
    :   Define a read-only iterable section output, sorted numerically.

        This version of [ITERABLE\_SECTION\_ROM()](#group__iterable__section__apis_1gaa83030f309052399a7d1f61c56a0c901) sorts the entries numerically, that is, `SECNAME_10` will come after `SECNAME_2`. `_` separator is required, and up to 2 numeric digits are handled (0-99).

        See also

        [ITERABLE\_SECTION\_ROM()](#group__iterable__section__apis_1gaa83030f309052399a7d1f61c56a0c901)

    ITERABLE\_SECTION\_ROM\_GC\_ALLOWED(struct\_type, subalign)
    :   Define a garbage collectable read-only iterable section output.

        Define an output section which will set up an iterable area of equally-sized data structures. For use with [STRUCT\_SECTION\_ITERABLE()](#group__iterable__section__apis_1ga9104f42cbe4a67a931bed7f7cc8f600f). Input sections will be sorted by name, per ld’s SORT\_BY\_NAME.

        This macro should be used for read-only data.

        Note that the symbols within the section can be garbage collected.

    ITERABLE\_SECTION\_RAM(struct\_type, subalign)
    :   Define a read-write iterable section output.

        Define an output section which will set up an iterable area of equally-sized data structures. For use with [STRUCT\_SECTION\_ITERABLE()](#group__iterable__section__apis_1ga9104f42cbe4a67a931bed7f7cc8f600f). Input sections will be sorted by name, per ld’s SORT\_BY\_NAME.

        This macro should be used for read-write data that is modified at runtime.

        Note that this keeps the symbols in the image even though they are not being directly referenced. Use this when symbols are indirectly referenced by iterating through the section.

    ITERABLE\_SECTION\_RAM\_NUMERIC(struct\_type, subalign)
    :   Define a read-write iterable section output, sorted numerically.

        This version of [ITERABLE\_SECTION\_RAM()](#group__iterable__section__apis_1ga50d995ef13e80eb36cfc8556e39056d0) sorts the entries numerically, that is, `SECNAME10` will come after `SECNAME2`. Up to 2 numeric digits are handled (0-99).

        See also

        [ITERABLE\_SECTION\_RAM()](#group__iterable__section__apis_1ga50d995ef13e80eb36cfc8556e39056d0)

    ITERABLE\_SECTION\_RAM\_GC\_ALLOWED(struct\_type, subalign)
    :   Define a garbage collectable read-write iterable section output.

        Define an output section which will set up an iterable area of equally-sized data structures. For use with [STRUCT\_SECTION\_ITERABLE()](#group__iterable__section__apis_1ga9104f42cbe4a67a931bed7f7cc8f600f). Input sections will be sorted by name, per ld’s SORT\_BY\_NAME.

        This macro should be used for read-write data that is modified at runtime.

        Note that the symbols within the section can be garbage collected.

    TYPE\_SECTION\_ITERABLE(type, varname, secname, section\_postfix)
    :   Defines a new element for an iterable section for a generic type.

        Convenience helper combining \_\_in\_section() and Z\_DECL\_ALIGN(). The section name will be ‘.[SECNAME].static.[SECTION\_POSTFIX]’

        In the linker script, create output sections for these using [ITERABLE\_SECTION\_ROM()](#group__iterable__section__apis_1gaa83030f309052399a7d1f61c56a0c901) or [ITERABLE\_SECTION\_RAM()](#group__iterable__section__apis_1ga50d995ef13e80eb36cfc8556e39056d0).

        Note

        In order to store the element in ROM, a const specifier has to be added to the declaration: const [TYPE\_SECTION\_ITERABLE(…)](#group__iterable__section__apis_1gac5177fefd615bdd3025fac742d414808);

        Parameters:
        :   - **type** – **[in]** data type of variable
            - **varname** – **[in]** name of variable to place in section
            - **secname** – **[in]** type name of iterable section.
            - **section\_postfix** – **[in]** postfix to use in section name

    TYPE\_SECTION\_START(secname)
    :   iterable section start symbol for a generic type

        will return ‘\_[OUT\_TYPE]\_list\_start’.

        Parameters:
        :   - **secname** – **[in]** type name of iterable section. For ‘struct foobar’ this would be [TYPE\_SECTION\_START(foobar)](#group__iterable__section__apis_1gac97b7f4fd42a2d9e11b6a585bc716a05)

    TYPE\_SECTION\_END(secname)
    :   iterable section end symbol for a generic type

        will return ‘\_<SECNAME>\_list\_end’.

        Parameters:
        :   - **secname** – **[in]** type name of iterable section. For ‘struct foobar’ this would be [TYPE\_SECTION\_START(foobar)](#group__iterable__section__apis_1gac97b7f4fd42a2d9e11b6a585bc716a05)

    TYPE\_SECTION\_START\_EXTERN(type, secname)
    :   iterable section extern for start symbol for a generic type

        Helper macro to give extern for start of iterable section. The macro typically will be called [TYPE\_SECTION\_START\_EXTERN(struct foobar, foobar)](#group__iterable__section__apis_1ga40c6ba05d5bcb848a530bdc17bbff5be). This allows the macro to hand different types as well as cases where the type and section name may differ.

        Parameters:
        :   - **type** – **[in]** data type of section
            - **secname** – **[in]** name of output section

    TYPE\_SECTION\_END\_EXTERN(type, secname)
    :   iterable section extern for end symbol for a generic type

        Helper macro to give extern for end of iterable section. The macro typically will be called [TYPE\_SECTION\_END\_EXTERN(struct foobar, foobar)](#group__iterable__section__apis_1gaf009fe4b90f7b338c3bf85bb4cd682e5). This allows the macro to hand different types as well as cases where the type and section name may differ.

        Parameters:
        :   - **type** – **[in]** data type of section
            - **secname** – **[in]** name of output section

    TYPE\_SECTION\_FOREACH(type, secname, iterator)
    :   Iterate over a specified iterable section for a generic type.

        Iterator for structure instances gathered by [TYPE\_SECTION\_ITERABLE()](#group__iterable__section__apis_1gac5177fefd615bdd3025fac742d414808). The linker must provide a \_<SECNAME>\_list\_start symbol and a \_<SECNAME>\_list\_end symbol to mark the start and the end of the list of struct objects to iterate over. This is normally done using [ITERABLE\_SECTION\_ROM()](#group__iterable__section__apis_1gaa83030f309052399a7d1f61c56a0c901) or [ITERABLE\_SECTION\_RAM()](#group__iterable__section__apis_1ga50d995ef13e80eb36cfc8556e39056d0) in the linker script.

    TYPE\_SECTION\_GET(type, secname, i, dst)
    :   Get element from section for a generic type.

        Note

        There is no protection against reading beyond the section.

        Parameters:
        :   - **type** – **[in]** type of element
            - **secname** – **[in]** name of output section
            - **i** – **[in]** Index.
            - **dst** – **[out]** Pointer to location where pointer to element is written.

    TYPE\_SECTION\_COUNT(type, secname, dst)
    :   Count elements in a section for a generic type.

        Parameters:
        :   - **type** – **[in]** type of element
            - **secname** – **[in]** name of output section
            - **dst** – **[out]** Pointer to location where result is written.

    STRUCT\_SECTION\_START(struct\_type)
    :   iterable section start symbol for a struct type

        Parameters:
        :   - **struct\_type** – **[in]** data type of section

    STRUCT\_SECTION\_START\_EXTERN(struct\_type)
    :   iterable section extern for start symbol for a struct

        Helper macro to give extern for start of iterable section.

        Parameters:
        :   - **struct\_type** – **[in]** data type of section

    STRUCT\_SECTION\_END(struct\_type)
    :   iterable section end symbol for a struct type

        Parameters:
        :   - **struct\_type** – **[in]** data type of section

    STRUCT\_SECTION\_END\_EXTERN(struct\_type)
    :   iterable section extern for end symbol for a struct

        Helper macro to give extern for end of iterable section.

        Parameters:
        :   - **struct\_type** – **[in]** data type of section

    STRUCT\_SECTION\_ITERABLE\_ALTERNATE(secname, struct\_type, varname)
    :   Defines a new element of alternate data type for an iterable section.

        Special variant of [STRUCT\_SECTION\_ITERABLE()](#group__iterable__section__apis_1ga9104f42cbe4a67a931bed7f7cc8f600f), for placing alternate data types within the iterable section of a specific data type. The data type sizes and semantics must be equivalent!

    STRUCT\_SECTION\_ITERABLE\_ARRAY\_ALTERNATE(secname, struct\_type, varname, size)
    :   Defines an array of elements of alternate data type for an iterable section.

        See also

        [STRUCT\_SECTION\_ITERABLE\_ALTERNATE](#group__iterable__section__apis_1gae08ef16db3e04967fdca69a19ca4c70b)

    STRUCT\_SECTION\_ITERABLE(struct\_type, varname)
    :   Defines a new element for an iterable section.

        Convenience helper combining \_\_in\_section() and Z\_DECL\_ALIGN(). The section name is the struct type prepended with an underscore. The subsection is “static” and the subsubsection is the variable name.

        In the linker script, create output sections for these using [ITERABLE\_SECTION\_ROM()](#group__iterable__section__apis_1gaa83030f309052399a7d1f61c56a0c901) or [ITERABLE\_SECTION\_RAM()](#group__iterable__section__apis_1ga50d995ef13e80eb36cfc8556e39056d0).

        Note

        In order to store the element in ROM, a const specifier has to be added to the declaration: const [STRUCT\_SECTION\_ITERABLE(…)](#group__iterable__section__apis_1ga9104f42cbe4a67a931bed7f7cc8f600f);

    STRUCT\_SECTION\_ITERABLE\_ARRAY(struct\_type, varname, size)
    :   Defines an array of elements for an iterable section.

        See also

        [STRUCT\_SECTION\_ITERABLE](#group__iterable__section__apis_1ga9104f42cbe4a67a931bed7f7cc8f600f)

    STRUCT\_SECTION\_ITERABLE\_NAMED(struct\_type, name, varname)
    :   Defines a new element for an iterable section with a custom name.

        The name can be used to customize how iterable section entries are sorted.

        See also

        [STRUCT\_SECTION\_ITERABLE()](#group__iterable__section__apis_1ga9104f42cbe4a67a931bed7f7cc8f600f)

    STRUCT\_SECTION\_ITERABLE\_NAMED\_ALTERNATE(struct\_type, secname, name, varname)
    :   Defines a new element for an iterable section with a custom name, placed in a custom section.

        The name can be used to customize how iterable section entries are sorted.

        See also

        [STRUCT\_SECTION\_ITERABLE\_NAMED()](#group__iterable__section__apis_1gada3ff915b4ed4881a61b79d8877131e2)

    STRUCT\_SECTION\_FOREACH\_ALTERNATE(secname, struct\_type, iterator)
    :   Iterate over a specified iterable section (alternate).

        Iterator for structure instances gathered by [STRUCT\_SECTION\_ITERABLE()](#group__iterable__section__apis_1ga9104f42cbe4a67a931bed7f7cc8f600f). The linker must provide a \_<SECNAME>\_list\_start symbol and a \_<SECNAME>\_list\_end symbol to mark the start and the end of the list of struct objects to iterate over. This is normally done using [ITERABLE\_SECTION\_ROM()](#group__iterable__section__apis_1gaa83030f309052399a7d1f61c56a0c901) or [ITERABLE\_SECTION\_RAM()](#group__iterable__section__apis_1ga50d995ef13e80eb36cfc8556e39056d0) in the linker script.

    STRUCT\_SECTION\_FOREACH(struct\_type, iterator)
    :   Iterate over a specified iterable section.

        Iterator for structure instances gathered by [STRUCT\_SECTION\_ITERABLE()](#group__iterable__section__apis_1ga9104f42cbe4a67a931bed7f7cc8f600f). The linker must provide a \_<struct\_type>\_list\_start symbol and a \_<struct\_type>\_list\_end symbol to mark the start and the end of the list of struct objects to iterate over. This is normally done using [ITERABLE\_SECTION\_ROM()](#group__iterable__section__apis_1gaa83030f309052399a7d1f61c56a0c901) or [ITERABLE\_SECTION\_RAM()](#group__iterable__section__apis_1ga50d995ef13e80eb36cfc8556e39056d0) in the linker script.

    STRUCT\_SECTION\_GET(struct\_type, i, dst)
    :   Get element from section.

        Note

        There is no protection against reading beyond the section.

        Parameters:
        :   - **struct\_type** – **[in]** Struct type.
            - **i** – **[in]** Index.
            - **dst** – **[out]** Pointer to location where pointer to element is written.

    STRUCT\_SECTION\_COUNT(struct\_type, dst)
    :   Count elements in a section.

        Parameters:
        :   - **struct\_type** – **[in]** Struct type
            - **dst** – **[out]** Pointer to location where result is written.
