---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/llext/api.html
original_path: services/llext/api.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# API Reference

*group* Linkable loadable extensions
:   **Since**
    :   3.5

    **Version**
    :   0.1.0

    Defines

    LLEXT\_LOAD\_PARAM\_DEFAULT
    :   Default initializer for [llext\_load\_param](#structllext__load__param).

    Enums

    enum llext\_mem
    :   List of memory regions stored or referenced in the LLEXT subsystem.

        This enum lists the different types of memory regions that are used by the LLEXT subsystem. The names match common ELF file section names; but note that at load time multiple ELF sections with similar flags may be merged together into a single memory region.

        *Values:*

        enumerator LLEXT\_MEM\_TEXT
        :   Executable code.

        enumerator LLEXT\_MEM\_DATA
        :   Initialized data.

        enumerator LLEXT\_MEM\_RODATA
        :   Read-only data.

        enumerator LLEXT\_MEM\_BSS
        :   Uninitialized data.

        enumerator LLEXT\_MEM\_EXPORT
        :   Exported symbol table.

        enumerator LLEXT\_MEM\_SYMTAB
        :   Symbol table.

        enumerator LLEXT\_MEM\_STRTAB
        :   Symbol name strings.

        enumerator LLEXT\_MEM\_SHSTRTAB
        :   Section name strings.

        enumerator LLEXT\_MEM\_COUNT
        :   Number of regions managed by LLEXT.

    Functions

    struct [llext](#c.llext) \*llext\_by\_name(const char \*name)
    :   Find an llext by name.

        Parameters:
        :   - **name** – **[in]** String name of the llext

        Returns:
        :   a pointer to the [llext](#structllext), or `NULL` if not found

    int llext\_iterate(int (\*fn)(struct [llext](#c.llext) \*ext, void \*arg), void \*arg)
    :   Iterate over all loaded extensions.

        Calls a provided callback function for each registered extension or until the callback function returns a non-0 value.

        Parameters:
        :   - **fn** – **[in]** callback function
            - **arg** – **[in]** a private argument to be provided to the callback function

        Return values:
        :   **0** – if no extensions are registered

        Returns:
        :   the value returned by the last callback invocation

    int llext\_load(struct [llext\_loader](#c.llext_loader) \*loader, const char \*name, struct [llext](#c.llext) \*\*ext, struct [llext\_load\_param](#c.llext_load_param) \*ldr\_parm)
    :   Load and link an extension.

        Loads relevant ELF data into memory and provides a structure to work with it.

        Parameters:
        :   - **loader** – **[in]** An extension loader that provides input data and context
            - **name** – **[in]** A string identifier for the extension
            - **ext** – **[out]** Pointer to the newly allocated [llext](#structllext) structure
            - **ldr\_parm** – **[in]** Optional advanced load parameters (may be `NULL`)

        Return values:
        :   - **-ENOMEM** – Not enough memory
            - **-ENOEXEC** – Invalid ELF stream
            - **-ENOTSUP** – Unsupported ELF features

        Returns:
        :   the previous extension use count on success, or a negative error code.

    int llext\_unload(struct [llext](#c.llext) \*\*ext)
    :   Unload an extension.

        Parameters:
        :   - **ext** – **[in]** Extension to unload

    const void \*llext\_find\_sym(const struct [llext\_symtable](#c.llext_symtable) \*sym\_table, const char \*sym\_name)
    :   Find the address for an arbitrary symbol.

        Searches for a symbol address, either in the list of symbols exported by the main Zephyr binary or in an extension’s symbol table.

        Parameters:
        :   - **sym\_table** – **[in]** Symbol table to lookup symbol in, or `NULL` to search in the main Zephyr symbol table
            - **sym\_name** – **[in]** Symbol name to find

        Returns:
        :   the address of symbol in memory, or `NULL` if not found

    int llext\_call\_fn(struct [llext](#c.llext) \*ext, const char \*sym\_name)
    :   Call a function by name.

        Expects a symbol representing a `void fn(void)` style function exists and may be called.

        Parameters:
        :   - **ext** – **[in]** Extension to call function in
            - **sym\_name** – **[in]** Function name (exported symbol) in the extension

        Return values:
        :   - **0** – Success
            - **-ENOENT** – Symbol name not found

    int llext\_add\_domain(struct [llext](#c.llext) \*ext, struct [k\_mem\_domain](../../kernel/usermode/memory_domain.md#c.k_mem_domain "k_mem_domain") \*domain)
    :   Add an extension to a memory domain.

        Allows an extension to be executed in user mode threads when memory protection hardware is enabled by adding memory partitions covering the extension’s memory regions to a memory domain.

        Parameters:
        :   - **ext** – **[in]** Extension to add to a domain
            - **domain** – **[in]** Memory domain to add partitions to

        Return values:
        :   **-ENOSYS** –  [`CONFIG_USERSPACE`](../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") is not enabled or supported

        Returns:
        :   0 on success, or a negative error code.

    int arch\_elf\_relocate(elf\_rela\_t \*rel, uintptr\_t loc, uintptr\_t sym\_base\_addr, const char \*sym\_name, uintptr\_t load\_bias)
    :   Architecture specific opcode update function.

        ELF files include sections describing a series of *relocations*, which are instructions on how to rewrite opcodes given the actual placement of some symbolic data such as a section, function, or object. These relocations are architecture specific and each architecture supporting LLEXT must implement this.

        Parameters:
        :   - **rel** – **[in]** Relocation data provided by ELF
            - **loc** – **[in]** Address of opcode to rewrite
            - **sym\_base\_addr** – **[in]** Address of symbol referenced by relocation
            - **sym\_name** – **[in]** Name of symbol referenced by relocation
            - **load\_bias** – **[in]** `.text` load address

        Return values:
        :   - **0** – Success
            - **-ENOTSUP** – Unsupported relocation
            - **-ENOEXEC** – Invalid relocation

    ssize\_t llext\_find\_section(struct [llext\_loader](#c.llext_loader) \*loader, const char \*search\_name)
    :   Locates an ELF section in the file.

        Searches for a section by name in the ELF file and returns its offset.

        Parameters:
        :   - **loader** – Extension loader data and context
            - **search\_name** – Section name to search for

        Returns:
        :   the section offset or a negative error code

    void arch\_elf\_relocate\_local(struct [llext\_loader](#c.llext_loader) \*loader, struct [llext](#c.llext) \*ext, const elf\_rela\_t \*rel, const elf\_sym\_t \*sym, size\_t got\_offset)
    :   Architecture specific function for updating addresses via relocation table.

        Parameters:
        :   - **loader** – **[in]** Extension loader data and context
            - **ext** – **[in]** Extension to call function in
            - **rel** – **[in]** Relocation data provided by elf
            - **sym** – **[in]** Corresponding symbol table entry
            - **got\_offset** – **[in]** Offset within a relocation table

    struct llext
    :   *#include <llext.h>*

        Structure describing a linkable loadable extension.

        This structure holds the data for a loaded extension. It is created by the [llext\_load](#group__llext__apis_1ga93c7d7f8987bd25e3dc486943785c8a1) function and destroyed by the [llext\_unload](#group__llext__apis_1gad3df7ed4d436846504c0047166eb929e) function.

        Public Members

        char name[16]
        :   Name of the llext.

        void \*mem[[LLEXT\_MEM\_COUNT](#c.llext_mem.LLEXT_MEM_COUNT)]
        :   Lookup table of memory regions.

        bool mem\_on\_heap[[LLEXT\_MEM\_COUNT](#c.llext_mem.LLEXT_MEM_COUNT)]
        :   Is the memory for this region allocated on heap?

        size\_t mem\_size[[LLEXT\_MEM\_COUNT](#c.llext_mem.LLEXT_MEM_COUNT)]
        :   Size of each stored region.

        size\_t alloc\_size
        :   Total llext allocation size.

        struct [llext\_symtable](#c.llext_symtable) sym\_tab
        :   Table of all global symbols in the extension; used internally as part of the linking process.

            E.g. if the extension is built out of several files, if any symbols are referenced between files, this table will be used to link them.

        struct [llext\_symtable](#c.llext_symtable) exp\_tab
        :   Table of symbols exported by the llext via [LL\_EXTENSION\_SYMBOL](#group__llext__symbols_1ga2e05a6082a3ee50fbc74e14a48056626).

            This can be used in the main Zephyr binary to find symbols in the extension.

        unsigned int use\_count
        :   Extension use counter, prevents unloading while in use.

    struct llext\_load\_param
    :   *#include <llext.h>*

        Advanced llext\_load parameters.

        This structure contains advanced parameters for [llext\_load](#group__llext__apis_1ga93c7d7f8987bd25e3dc486943785c8a1).

        Public Members

        bool relocate\_local
        :   Perform local relocation.

        bool pre\_located
        :   Use the virtual symbol addresses from the ELF, not addresses within the memory buffer, when calculating relocation targets.

*group* Exported symbol definitions
:   Defines

    EXPORT\_SYMBOL(x)
    :   Export a constant symbol to extensions.

        Takes a symbol (function or object) by symbolic name and adds the name and address of the symbol to a table of symbols that may be referenced by extensions.

        Parameters:
        :   - **x** – Symbol to export to extensions

    LL\_EXTENSION\_SYMBOL(x)
    :   Exports a symbol from an extension to the base image.

        This macro can be used in extensions to add a symbol (function or object) to the extension’s exported symbol table, so that it may be referenced by the base image.

        Parameters:
        :   - **x** – Extension symbol to export to the base image

    struct llext\_const\_symbol
    :   *#include <symbol.h>*

        Constant symbols are unchangeable named memory addresses.

        Symbols may be named function or global objects that have been exported for linking. These constant symbols are useful in the base image as they may be placed in ROM.

        Note

        When updating this structure, make sure to also update the ‘scripts/build/llext\_prepare\_exptab.py’ build script.

        Public Members

        const char \*const name
        :   Name of symbol.

        const uintptr\_t slid
        :   Symbol Link Identifier.

        union [llext\_const\_symbol](#c.llext_const_symbol).[anonymous] [anonymous]
        :   At build time, we always write to ‘name’.

            At runtime, which field is used depends on CONFIG\_LLEXT\_EXPORT\_BUILTINS\_BY\_SLID.

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

*group* ELF loader context
:   Defines

    LLEXT\_BUF\_LOADER(\_buf, \_buf\_len)
    :   Initializer for an [llext\_buf\_loader](#structllext__buf__loader) structure.

        Parameters:
        :   - **\_buf** – Buffer containing the ELF binary
            - **\_buf\_len** – Buffer length in bytes

    struct llext\_buf\_loader
    :   *#include <buf\_loader.h>*

        Implementation of [llext\_loader](#structllext__loader) that reads from a memory buffer.

        Public Members

        struct [llext\_loader](#c.llext_loader) loader
        :   Extension loader.

    struct llext\_loader
    :   *#include <loader.h>*

        Linkable loadable extension loader context.

        This object is used to access the ELF file data and cache its contents while an extension is being loaded by the LLEXT subsystem. Once the extension is loaded, this object is no longer needed.

        Public Members

        int (\*read)(struct [llext\_loader](#c.llext_loader) \*ldr, void \*out, size\_t len)
        :   Function to read (copy) from the loader.

            Copies len bytes into buf from the current position of the loader.

            Param ldr:
            :   **[in]** Loader

            Param out:
            :   **[in]** Output location

            Param len:
            :   **[in]** Length to copy into the output location

            Return:
            :   0 on success, or a negative error code.

        int (\*seek)(struct [llext\_loader](#c.llext_loader) \*ldr, size\_t pos)
        :   Function to seek to a new absolute location in the stream.

            Changes the location of the loader position to a new absolute given position.

            Param ldr:
            :   **[in]** Loader

            Param pos:
            :   **[in]** Position in stream to move loader

            Return:
            :   0 on success, or a negative error code.

        void \*(\*peek)(struct [llext\_loader](#c.llext_loader) \*ldr, size\_t pos)
        :   Optional function to peek at an absolute location in the ELF.

            Return a pointer to the buffer at specified offset.

            Param ldr:
            :   **[in]** Loader

            Param pos:
            :   **[in]** Position to obtain a pointer to

            Return:
            :   a pointer into the buffer or `NULL` if not supported
