---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/debugging/symtab.html
original_path: services/debugging/symtab.html
---

# Symbol Table (Symtab)

The Symtab module, when enabled, will generate full symbol table during the Zephyr linking
stage that keep tracks of the information about the functions’ name and address, for advanced application
with a lot of functions, this is expected to consume a sizable amount of ROM.

Currently, this is being used to look up the function names during a stack trace in supported architectures.

## Usage

Application can gain access to the symbol table data structure by including the `symtab.h` header
file and call [`symtab_get()`](../../doxygen/html/group__symtab__apis.md#ga2f1c4fa3cc113c2e5f47c5bbcd337e32). For now, we only provide [`symtab_find_symbol_name()`](../../doxygen/html/group__symtab__apis.md#gac5927cf3f4e0bf3e1b27b397290e44c5)
function to look-up the symbol name and offset of an address. More advanced functionalities and be
achieved by directly accessing the members of the data structure.

## Configuration

Configure this module using the following options.

- [`CONFIG_SYMTAB`](../../kconfig.md#CONFIG_SYMTAB "CONFIG_SYMTAB"): enable the generation of the symbol table.

## API documentation

[Symbol Table API](../../doxygen/html/group__symtab__apis.md)
