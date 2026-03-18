---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/llext/index.html
original_path: services/llext/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Linkable Loadable Extensions (LLEXT)

The LLEXT subsystem provides a toolbox for extending the functionality of an
application at runtime with linkable loadable code.

Extensions are precompiled executables in ELF format that can be verified,
loaded, and linked with the main Zephyr binary. Extensions can be manipulated
and introspected to some degree, as well as unloaded when no longer needed.

Note

The LLEXT subsystem requires architecture-specific support. It is currently
available only on ARM and Xtensa cores.
