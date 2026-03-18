---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/llext/index.html
original_path: services/llext/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Linkable Loadable Extensions (LLEXT)

The llext subsystem provides a toolbox for extending the functionality of an
application at runtime with linkable loadable code.

Extensions can be loaded from precompiled ELF formatted data which is
verified, loaded, and linked with other extensions. Extensions can be
manipulated and introspected to some degree, as well as unloaded when no longer
needed.

An extension may be loaded using any implementation of a [`llext_loader`](#c.llext_loader)
which has a set of function pointers that provide the necessary functionality
to read the ELF data. A loader also provides some minimal context (memory)
needed by the [`llext_load()`](#c.llext_load) function. An implementation over a buffer
containing an ELF in addressable memory in memory is available as
[`llext_buf_loader`](#c.llext_buf_loader).

## API Reference

Related code samples

[Linkable loadable extensions shell module](../../samples/subsys/llext/shell_loader/README.md#llext-shell-loader "Manage loadable extensions using shell commands.")
:   Manage loadable extensions using shell commands.

*group* llext
:   Linkable loadable extensions.

    Defines

    LLEXT\_MEM\_PARTITIONS

    LLEXT\_LOAD\_PARAM\_DEFAULT

    Enums

    enum llext\_mem
    :   List of ELF regions that are stored or referenced in the llext.

        *Values:*

        enumerator LLEXT\_MEM\_TEXT

        enumerator LLEXT\_MEM\_DATA

        enumerator LLEXT\_MEM\_RODATA

        enumerator LLEXT\_MEM\_BSS

        enumerator LLEXT\_MEM\_EXPORT

        enumerator LLEXT\_MEM\_SYMTAB

        enumerator LLEXT\_MEM\_STRTAB

        enumerator LLEXT\_MEM\_SHSTRTAB

        enumerator LLEXT\_MEM\_COUNT

    Functions

    struct [llext](#c.llext) \*llext\_by\_name(const char \*name)
    :   Find an llext by name.

        Parameters:
        :   - **name** – **[in]** String name of the llext

        Return values:
        :   - **NULL** – if no llext not found
            - **llext** – if llext found

    int llext\_iterate(int (\*fn)(struct [llext](#c.llext) \*ext, void \*arg), void \*arg)
    :   Iterate overall registered llext instances.

        Calls a provided callback function for each registered extension or until the callback function returns a non-0 value.

        Parameters:
        :   - **fn** – **[in]** callback function
            - **arg** – **[in]** a private argument to be provided to the callback function

        Return values:
        :   - **0** – if no extensions are registered
            - **value** – returned by the most recent callback invocation

    int llext\_load(struct [llext\_loader](#c.llext_loader) \*loader, const char \*name, struct [llext](#c.llext) \*\*ext, struct [llext\_load\_param](#c.llext_load_param) \*ldr\_parm)
    :   Load and link an extension.

        Loads relevant ELF data into memory and provides a structure to work with it.

        Only relocatable ELF files are currently supported (partially linked).

        Parameters:
        :   - **loader** – **[in]** An extension loader that provides input data and context
            - **name** – **[in]** A string identifier for the extension
            - **ext** – **[out]** This will hold the pointer to the llext struct
            - **ldr\_parm** – **[in]** Loader parameters

        Return values:
        :   - **0** – Success
            - **-ENOMEM** – Not enough memory
            - **-EINVAL** – Invalid ELF stream

    int llext\_unload(struct [llext](#c.llext) \*\*ext)
    :   Unload an extension.

        Parameters:
        :   - **ext** – **[in]** Extension to unload

    const void \*const llext\_find\_sym(const struct [llext\_symtable](#c.llext_symtable) \*sym\_table, const char \*sym\_name)
    :   Find the address for an arbitrary symbol name.

        Parameters:
        :   - **sym\_table** – **[in]** Symbol table to lookup symbol in, if NULL uses base table
            - **sym\_name** – **[in]** Symbol name to find

        Return values:
        :   - **NULL** – if no symbol found
            - **addr** – Address of symbol in memory if found

    int llext\_call\_fn(struct [llext](#c.llext) \*ext, const char \*sym\_name)
    :   Call a function by name.

        Expects a symbol representing a void fn(void) style function exists and may be called.

        Parameters:
        :   - **ext** – **[in]** Extension to call function in
            - **sym\_name** – **[in]** Function name (exported symbol) in the extension

        Return values:
        :   - **0** – success
            - **-EINVAL** – invalid symbol name

    int llext\_add\_domain(struct [llext](#c.llext) \*ext, struct [k\_mem\_domain](../../kernel/usermode/memory_domain.md#c.k_mem_domain "k_mem_domain") \*domain)
    :   Add the known memory partitions of the extension to a memory domain.

        Allows an extension to be executed in supervisor or user mode threads when memory protection hardware is enabled.

        Parameters:
        :   - **ext** – **[in]** Extension to add to a domain
            - **domain** – **[in]** Memory domain to add partitions to

        Return values:
        :   - **0** – success
            - **-errno** – error

    void arch\_elf\_relocate(elf\_rela\_t \*rel, uintptr\_t opaddr, uintptr\_t opval)
    :   Architecture specific function for updating op codes given a relocation.

        Elf files contain a series of relocations described in a section. These relocation instructions are architecture specific and each architecture supporting extensions must implement this. They are instructions on how to rewrite opcodes given the actual placement of some symbolic data such as a section, function, or object.

        Parameters:
        :   - **rel** – **[in]** Relocation data provided by elf
            - **opaddr** – **[in]** Address of operation to rewrite with relocation
            - **opval** – **[in]** Value of looked up symbol to relocate

    ssize\_t llext\_find\_section(struct [llext\_loader](#c.llext_loader) \*loader, const char \*search\_name)
    :   Find an ELF section.

        Parameters:
        :   - **loader** – Extension loader data and context
            - **search\_name** – Section name to search for

        Return values:
        :   **Section** – offset or a negative error code

    void arch\_elf\_relocate\_local(struct [llext\_loader](#c.llext_loader) \*loader, struct [llext](#c.llext) \*ext, elf\_rela\_t \*rel, size\_t got\_offset)
    :   Architecture specific function for updating addresses via relocation table.

        Parameters:
        :   - **loader** – **[in]** Extension loader data and context
            - **ext** – **[in]** Extension to call function in
            - **rel** – **[in]** Relocation data provided by elf
            - **got\_offset** – **[in]** Offset within a relocation table

    struct llext
    :   *#include <llext.h>*

        Linkable loadable extension.

        Public Members

        char name[16]
        :   Name of the llext.

        void \*mem[[LLEXT\_MEM\_COUNT](#c.llext_mem.LLEXT_MEM_COUNT)]
        :   Lookup table of llext memory regions.

        bool mem\_on\_heap[[LLEXT\_MEM\_COUNT](#c.llext_mem.LLEXT_MEM_COUNT)]
        :   Is the memory for this section allocated on heap?

        size\_t mem\_size[[LLEXT\_MEM\_COUNT](#c.llext_mem.LLEXT_MEM_COUNT)]
        :   Size of each stored section.

        size\_t alloc\_size
        :   Total llext allocation size.

        struct [llext\_symtable](#c.llext_symtable) exp\_tab
        :   Exported symbols from the llext, may be linked against by other llext.

        unsigned int use\_count
        :   Extension use counter, prevents unloading while in use.

    struct llext\_load\_param
    :   *#include <llext.h>*

        llext loader parameters

        These are parameters, not saved in the permanent llext context, needed only for the loader

        Public Members

        bool relocate\_local
        :   Should local relocation be performed.

*group* llext\_symbols
:   Linkable loadable extension symbol.

    Defines

    EXPORT\_SYMBOL(x)
    :   Export a constant symbol to a table of symbols.

        Takes a symbol (function or object) by symbolic name and adds the name and address of the symbol to a table of symbols that may be used for linking.

        Parameters:
        :   - **x** – Symbol to export

    LL\_EXTENSION\_SYMBOL(x)

    EXPORT\_SYSCALL(x)
    :   Export a system call to a table of symbols.

        Takes a system call name and uses *[EXPORT\_SYMBOL()](#group__llext__symbols_1ga0188531646d69e784eccf85bd4fb34aa)* to export the respective function.

        Parameters:
        :   - **x** – System call to export

    struct llext\_const\_symbol
    :   *#include <symbol.h>*

        Constant symbols are unchangeable named memory addresses.

        Symbols may be named function or global objects that have been exported for linking. These constant symbols are useful in the base image as they may be placed in ROM.

        Public Members

        const char \*const name
        :   Name of symbol.

        const void \*const addr
        :   Address of symbol.

    struct llext\_symbol
    :   *#include <symbol.h>*

        Symbols are named memory addresses.

        Symbols may be named function or global objects that have been exported for linking. These are mutable and should come from extensions where the location may need updating depending on where memory is placed.

        Public Members

        const char \*name
        :   Name of symbol.

        void \*addr
        :   Address of symbol.

    struct llext\_symtable
    :   *#include <symbol.h>*

        A symbol table.

        An array of symbols

        Public Members

        size\_t sym\_cnt
        :   Number of symbols in the table.

        struct [llext\_symbol](#c.llext_symbol) \*syms
        :   Array of symbols.

*group* llext\_loader
:   Loader context for llext.

    Functions

    static inline int llext\_read(struct [llext\_loader](#c.llext_loader) \*l, void \*buf, size\_t len)

    static inline int llext\_seek(struct [llext\_loader](#c.llext_loader) \*l, size\_t pos)

    static inline void \*llext\_peek(struct [llext\_loader](#c.llext_loader) \*l, size\_t pos)

    struct llext\_loader
    :   *#include <loader.h>*

        Linkable loadable extension loader context.

        Public Members

        int (\*read)(struct [llext\_loader](#c.llext_loader) \*ldr, void \*out, size\_t len)
        :   Read (copy) from the loader.

            Copies len bytes into buf from the current position of the loader.

            Param ldr:
            :   **[in]** Loader

            Param out:
            :   **[in]** Output location

            Param len:
            :   **[in]** Length to copy into the output location

            Retval 0:
            :   Success

            Retval -errno:
            :   Error reading (any errno)

        int (\*seek)(struct [llext\_loader](#c.llext_loader) \*ldr, size\_t pos)
        :   Seek to a new absolute location.

            Changes the location of the loader position to a new absolute given position.

            Param ldr:
            :   **[in]** Loader

            Param pos:
            :   **[in]** Position in stream to move loader

            Retval 0:
            :   Success

            Retval -errno:
            :   Error reading (any errno)

        void \*(\*peek)(struct [llext\_loader](#c.llext_loader) \*ldr, size\_t pos)
        :   Peek at an absolute location.

            Return a pointer to the buffer at specified offset.

            Param ldr:
            :   **[in]** Loader

            Param pos:
            :   **[in]** Position to obtain a pointer to

            Retval pointer:
            :   into the buffer

*group* llext\_buf\_loader
:   LLEXT buffer loader.

    Defines

    LLEXT\_BUF\_LOADER(\_buf, \_buf\_len)
    :   Initialize an extension buf loader.

        Parameters:
        :   - **\_buf** – Buffer containing an ELF binary
            - **\_buf\_len** – Buffer length in bytes

    struct llext\_buf\_loader
    :   *#include <buf\_loader.h>*

        An extension loader from a provided buffer containing an ELF.

        Public Members

        struct [llext\_loader](#c.llext_loader) loader
        :   Extension loader.
