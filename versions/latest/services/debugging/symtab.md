---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/debugging/symtab.html
original_path: services/debugging/symtab.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Symbol Table (Symtab)

The Symtab module, when enabled, will generate full symbol table during the Zephyr linking
stage that keep tracks of the information about the functions’ name and address, for advanced application
with a lot of functions, this is expected to consume a sizable amount of ROM.

Currently, this is being used to look up the function names during a stack trace in supported architectures.

## Usage

Application can gain access to the symbol table data structure by including the `symtab.h` header
file and call [`symtab_get()`](#c.symtab_get). For now, we only provide [`symtab_find_symbol_name()`](#c.symtab_find_symbol_name)
function to look-up the symbol name and offset of an address. More advanced functionalities and be
achieved by directly accessing the members of the data structure.

## Configuration

Configure this module using the following options.

- [`CONFIG_SYMTAB`](../../kconfig.md#CONFIG_SYMTAB "CONFIG_SYMTAB"): enable the generation of the symbol table.

## API documentation

*group* Symbol Table API
:   Functions

    const struct [symtab\_info](#c.symtab_info) \*const symtab\_get(void)
    :   Get the pointer to the symbol table.

        Returns:
        :   Pointer to the symbol table.

    const char \*const symtab\_find\_symbol\_name(uintptr\_t addr, uint32\_t \*offset)
    :   Find the symbol name with a binary search.

        Parameters:
        :   - **addr** – **[in]** Address of the symbol to find
            - **offset** – **[out]** Offset of the symbol from the nearest symbol. If the symbol can’t be found, this will be 0.

        Returns:
        :   Name of the nearest symbol if found, otherwise “?” is returned.

    struct symtab\_info
    :   *#include <symtab.h>*
