---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/kconfig/preprocessor-functions.html
original_path: build/kconfig/preprocessor-functions.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Custom Kconfig Preprocessor Functions

Kconfiglib supports custom Kconfig preprocessor functions written in Python.
These functions are defined in
[scripts/kconfig/kconfigfunctions.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/kconfig/kconfigfunctions.py).

Note

The official Kconfig preprocessor documentation can be found [here](https://www.kernel.org/doc/html/latest/kbuild/kconfig-macro-language.html).

Most of the custom preprocessor functions are used to get devicetree
information into Kconfig. For example, the default value of a Kconfig symbol
can be fetched from a devicetree `reg` property.

## Devicetree-related Functions

The functions listed below are used to get devicetree information into Kconfig.
See the Python docstrings in [scripts/kconfig/kconfigfunctions.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/kconfig/kconfigfunctions.py)
for detailed documentation.

The `*_int` version of each function returns the value as a decimal integer,
while the `*_hex` version returns a hexadecimal value starting with `0x`.

```text
$(dt_alias_enabled,<node alias>)
$(dt_chosen_bool_prop, <property in /chosen>, <prop>)
$(dt_chosen_enabled,<property in /chosen>)
$(dt_chosen_has_compat,<property in /chosen>)
$(dt_chosen_label,<property in /chosen>)
$(dt_chosen_path,<property in /chosen>)
$(dt_chosen_reg_addr_hex,<property in /chosen>[,<index>,<unit>])
$(dt_chosen_reg_addr_int,<property in /chosen>[,<index>,<unit>])
$(dt_chosen_reg_size_hex,<property in /chosen>[,<index>,<unit>])
$(dt_chosen_reg_size_int,<property in /chosen>[,<index>,<unit>])
$(dt_compat_enabled,<compatible string>)
$(dt_compat_on_bus,<compatible string>,<bus>)
$(dt_gpio_hogs_enabled)
$(dt_has_compat,<compatible string>)
$(dt_node_bool_prop,<node path>,<prop>)
$(dt_node_has_compat,<node path>,<compatible string>)
$(dt_node_has_prop,<node path>,<prop>)
$(dt_node_int_prop_hex,<node path>,<prop>[,<unit>])
$(dt_node_int_prop_int,<node path>,<prop>[,<unit>])
$(dt_node_parent,<node path>)
$(dt_node_reg_addr_hex,<node path>[,<index>,<unit>])
$(dt_node_reg_addr_int,<node path>[,<index>,<unit>])
$(dt_node_reg_size_hex,<node path>[,<index>,<unit>])
$(dt_node_reg_size_int,<node path>[,<index>,<unit>])
$(dt_node_str_prop_equals,<node path>,<prop>,<value>)
$(dt_nodelabel_array_prop_has_val, <node label>, <prop>, <value>)
$(dt_nodelabel_bool_prop,<node label>,<prop>)
$(dt_nodelabel_enabled,<node label>)
$(dt_nodelabel_enabled_with_compat,<node label>,<compatible string>)
$(dt_nodelabel_has_compat,<node label>,<compatible string>)
$(dt_nodelabel_has_prop,<node label>,<prop>)
$(dt_nodelabel_path,<node label>)
$(dt_nodelabel_reg_addr_hex,<node label>[,<index>,<unit>])
$(dt_nodelabel_reg_addr_int,<node label>[,<index>,<unit>])
$(dt_nodelabel_reg_size_hex,<node label>[,<index>,<unit>])
$(dt_nodelabel_reg_size_int,<node label>[,<index>,<unit>])
$(dt_path_enabled,<node path>)
$(shields_list_contains,<shield name>)
```

### Example Usage

Assume that the devicetree for some board looks like this:

```devicetree
{
     soc {
             #address-cells = <1>;
             #size-cells = <1>;

             spi0: spi@10014000 {
                     compatible = "sifive,spi0";
                     reg = <0x10014000 0x1000 0x20010000 0x3c0900>;
                     reg-names = "control", "mem";
                     ...
             };
};
```

The second entry in `reg` in `spi@1001400` (`<0x20010000 0x3c0900>`)
corresponds to `mem`, and has the address `0x20010000`. This address can be
inserted into Kconfig as follows:

```kconfig
config FLASH_BASE_ADDRESS
     default $(dt_node_reg_addr_hex,/soc/spi@1001400,1)
```

After preprocessor expansion, this turns into the definition below:

```kconfig
config FLASH_BASE_ADDRESS
     default 0x20010000
```
