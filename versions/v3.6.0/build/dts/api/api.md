---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/api.html
original_path: build/dts/api/api.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Devicetree API

This is a reference page for the `<zephyr/devicetree.h>` API. The API is macro
based. Use of these macros has no impact on scheduling. They can be used from
any calling context and at file scope.

Some of these – the ones beginning with `DT_INST_` – require a special
macro named `DT_DRV_COMPAT` to be defined before they can be used; these are
discussed individually below. These macros are generally meant for use within
[device drivers](../../../kernel/drivers/index.md#device-model-api), though they can be used outside of
drivers with appropriate care.

## [Generic APIs](#id3)

The APIs in this section can be used anywhere and do not require
`DT_DRV_COMPAT` to be defined.

### [Node identifiers and helpers](#id4)

A *node identifier* is a way to refer to a devicetree node at C preprocessor
time. While node identifiers are not C values, you can use them to access
devicetree data in C rvalue form using, for example, the
[Property access](#devicetree-property-access) API.

The root node `/` has node identifier `DT_ROOT`. You can create node
identifiers for other devicetree nodes using [`DT_PATH()`](#c.DT_PATH),
[`DT_NODELABEL()`](#c.DT_NODELABEL), [`DT_ALIAS()`](#c.DT_ALIAS), and [`DT_INST()`](#c.DT_INST).

There are also [`DT_PARENT()`](#c.DT_PARENT) and [`DT_CHILD()`](#c.DT_CHILD) macros which can be
used to create node identifiers for a given node’s parent node or a particular
child node, respectively.

The following macros create or operate on node identifiers.

Related code samples

[GPIO with custom Devicetree binding](../../../samples/basic/custom_dts_binding/README.md#gpio-custom-dts-binding "Use custom Devicetree binding to control a GPIO.")
:   Use custom Devicetree binding to control a GPIO.

*group* devicetree-generic-id
:   Defines

    DT\_INVALID\_NODE
    :   Name for an invalid node identifier.

        This supports cases where factored macros can be invoked from paths where devicetree data may or may not be available. It is a preprocessor identifier that does not match any valid devicetree node identifier.

    DT\_ROOT
    :   Node identifier for the root node in the devicetree.

    DT\_PATH(...)
    :   Get a node identifier for a devicetree path.

        The arguments to this macro are the names of non-root nodes in the tree required to reach the desired node, starting from the root. Non-alphanumeric characters in each name must be converted to underscores to form valid C tokens, and letters must be lowercased.

        Example devicetree fragment:

        ```devicetree
        / {
                soc {
                        serial1: serial@40001000 {
                                status = "okay";
                                current-speed = <115200>;
                                ...
                        };
                };
        };
        ```

        You can use `[DT_PATH(soc, serial_40001000)](#group__devicetree-generic-id_1ga015b4819473797982e83cae497697086)` to get a node identifier for the `serial@40001000` node. Node labels like `serial1` cannot be used as [DT\_PATH()](#group__devicetree-generic-id_1ga015b4819473797982e83cae497697086) arguments; use [DT\_NODELABEL()](#group__devicetree-generic-id_1gab7d23294a6bf7fd44a98b48ec47d8a79) for those instead.

        Example usage with [DT\_PROP()](#group__devicetree-generic-prop_1ga8e1fd9ebacd85d2013df027d041d506b) to get the `current-speed` property:

        ```c
        DT_PROP(DT_PATH(soc, serial_40001000), current_speed) // 115200
        ```

        (The `current-speed` property is also in `lowercase-and-underscores` form when used with this API.)

        When determining arguments to [DT\_PATH()](#group__devicetree-generic-id_1ga015b4819473797982e83cae497697086):

        - the first argument corresponds to a child node of the root (`soc` above)
        - a second argument corresponds to a child of the first argument (`serial_40001000` above, from the node name `serial@40001000` after lowercasing and changing `@` to `_`)
        - and so on for deeper nodes in the desired node’s path

        Note

        This macro returns a node identifier from path components. To get a path string from a node identifier, use [DT\_NODE\_PATH()](#group__devicetree-generic-id_1gacd79818b99724d834e3bb7ae74ee02cf) instead.

        Parameters:
        :   - **...** – lowercase-and-underscores node names along the node’s path, with each name given as a separate argument

        Returns:
        :   node identifier for the node with that path

    DT\_NODELABEL(label)
    :   Get a node identifier for a node label.

        Convert non-alphanumeric characters in the node label to underscores to form valid C tokens, and lowercase all letters. Note that node labels are not the same thing as label properties.

        Example devicetree fragment:

        ```devicetree
        serial1: serial@40001000 {
                label = "UART_0";
                status = "okay";
                current-speed = <115200>;
                ...
        };
        ```

        The only node label in this example is `serial1`.

        The string `UART_0` is *not* a node label; it’s the value of a property named label.

        You can use `[DT_NODELABEL(serial1)](#group__devicetree-generic-id_1gab7d23294a6bf7fd44a98b48ec47d8a79)` to get a node identifier for the `serial@40001000` node. Example usage with [DT\_PROP()](#group__devicetree-generic-prop_1ga8e1fd9ebacd85d2013df027d041d506b) to get the current-speed property:

        ```c
        DT_PROP(DT_NODELABEL(serial1), current_speed) // 115200
        ```

        Another example devicetree fragment:

        ```devicetree
        cpu@0 {
               L2_0: l2-cache {
                       cache-level = <2>;
                       ...
               };
        };
        ```

        Example usage to get the cache-level property:

        ```c
        DT_PROP(DT_NODELABEL(l2_0), cache_level) // 2
        ```

        Notice how `L2_0` in the devicetree is lowercased to `l2_0` in the [DT\_NODELABEL()](#group__devicetree-generic-id_1gab7d23294a6bf7fd44a98b48ec47d8a79) argument.

        Parameters:
        :   - **label** – lowercase-and-underscores node label name

        Returns:
        :   node identifier for the node with that label

    DT\_ALIAS(alias)
    :   Get a node identifier from /aliases.

        This macro’s argument is a property of the `/aliases` node. It returns a node identifier for the node which is aliased. Convert non-alphanumeric characters in the alias property to underscores to form valid C tokens, and lowercase all letters.

        Example devicetree fragment:

        ```devicetree
        / {
                aliases {
                        my-serial = &serial1;
                };

                soc {
                        serial1: serial@40001000 {
                                status = "okay";
                                current-speed = <115200>;
                                ...
                        };
                };
        };
        ```

        You can use [DT\_ALIAS(my\_serial)](#group__devicetree-generic-id_1gaa49e19bbc39dc0d6f16b78a5d02482c9) to get a node identifier for the `serial@40001000` node. Notice how `my-serial` in the devicetree becomes `my_serial` in the [DT\_ALIAS()](#group__devicetree-generic-id_1gaa49e19bbc39dc0d6f16b78a5d02482c9) argument. Example usage with [DT\_PROP()](#group__devicetree-generic-prop_1ga8e1fd9ebacd85d2013df027d041d506b) to get the current-speed property:

        ```c
        DT_PROP(DT_ALIAS(my_serial), current_speed) // 115200
        ```

        Parameters:
        :   - **alias** – lowercase-and-underscores alias name.

        Returns:
        :   node identifier for the node with that alias

    DT\_INST(inst, compat)
    :   Get a node identifier for an instance of a compatible.

        All nodes with a particular compatible property value are assigned instance numbers, which are zero-based indexes specific to that compatible. You can get a node identifier for these nodes by passing [DT\_INST()](#group__devicetree-generic-id_1gae199b930cb21ff38dab284a696093ead) an instance number, `inst`, along with the lowercase-and-underscores version of the compatible, `compat`.

        Instance numbers have the following properties:

        - for each compatible, instance numbers start at 0 and are contiguous
        - exactly one instance number is assigned for each node with a compatible, **including disabled nodes**
        - enabled nodes (status property is `okay` or missing) are assigned the instance numbers starting from 0, and disabled nodes have instance numbers which are greater than those of any enabled node

        No other guarantees are made. In particular:

        - instance numbers **in no way reflect** any numbering scheme that might exist in SoC documentation, node labels or unit addresses, or properties of the /aliases node (use [DT\_NODELABEL()](#group__devicetree-generic-id_1gab7d23294a6bf7fd44a98b48ec47d8a79) or [DT\_ALIAS()](#group__devicetree-generic-id_1gaa49e19bbc39dc0d6f16b78a5d02482c9) for those)
        - there **is no general guarantee** that the same node will have the same instance number between builds, even if you are building the same application again in the same build directory

        Example devicetree fragment:

        ```devicetree
        serial1: serial@40001000 {
                compatible = "vnd,soc-serial";
                status = "disabled";
                current-speed = <9600>;
                ...
        };

        serial2: serial@40002000 {
                compatible = "vnd,soc-serial";
                status = "okay";
                current-speed = <57600>;
                ...
        };

        serial3: serial@40003000 {
                compatible = "vnd,soc-serial";
                current-speed = <115200>;
                ...
        };
        ```

        Assuming no other nodes in the devicetree have compatible `"vnd,soc-serial"`, that compatible has nodes with instance numbers 0, 1, and 2.

        The nodes `serial@40002000` and `serial@40003000` are both enabled, so their instance numbers are 0 and 1, but no guarantees are made regarding which node has which instance number.

        Since `serial@40001000` is the only disabled node, it has instance number 2, since disabled nodes are assigned the largest instance numbers. Therefore:

        ```c
        // Could be 57600 or 115200. There is no way to be sure:
        // either serial@40002000 or serial@40003000 could
        // have instance number 0, so this could be the current-speed
        // property of either of those nodes.
        DT_PROP(DT_INST(0, vnd_soc_serial), current_speed)

        // Could be 57600 or 115200, for the same reason.
        // If the above expression expands to 57600, then
        // this expands to 115200, and vice-versa.
        DT_PROP(DT_INST(1, vnd_soc_serial), current_speed)

        // 9600, because there is only one disabled node, and
        // disabled nodes are "at the the end" of the instance
        // number "list".
        DT_PROP(DT_INST(2, vnd_soc_serial), current_speed)
        ```

        Notice how `"vnd,soc-serial"` in the devicetree becomes `vnd_soc_serial` (without quotes) in the [DT\_INST()](#group__devicetree-generic-id_1gae199b930cb21ff38dab284a696093ead) arguments. (As usual, `current-speed` in the devicetree becomes `current_speed` as well.)

        Nodes whose `compatible` property has multiple values are assigned independent instance numbers for each compatible.

        Parameters:
        :   - **inst** – instance number for compatible `compat`
            - **compat** – lowercase-and-underscores compatible, without quotes

        Returns:
        :   node identifier for the node with that instance number and compatible

    DT\_PARENT(node\_id)
    :   Get a node identifier for a parent node.

        Example devicetree fragment:

        ```devicetree
        parent: parent-node {
                child: child-node {
                        ...
                };
        };
        ```

        The following are equivalent ways to get the same node identifier:

        ```c
        DT_NODELABEL(parent)
        DT_PARENT(DT_NODELABEL(child))
        ```

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   a node identifier for the node’s parent

    DT\_GPARENT(node\_id)
    :   Get a node identifier for a grandparent node.

        Example devicetree fragment:

        ```devicetree
        gparent: grandparent-node {
                parent: parent-node {
                        child: child-node { ... }
                };
        };
        ```

        The following are equivalent ways to get the same node identifier:

        ```c
        DT_GPARENT(DT_NODELABEL(child))
        DT_PARENT(DT_PARENT(DT_NODELABEL(child))
        ```

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   a node identifier for the node’s parent’s parent

    DT\_CHILD(node\_id, child)
    :   Get a node identifier for a child node.

        Example devicetree fragment:

        ```devicetree
        / {
                soc-label: soc {
                        serial1: serial@40001000 {
                                status = "okay";
                                current-speed = <115200>;
                                ...
                        };
                };
        };
        ```

        Example usage with [DT\_PROP()](#group__devicetree-generic-prop_1ga8e1fd9ebacd85d2013df027d041d506b) to get the status of the `serial@40001000` node:

        ```c
        #define SOC_NODE DT_NODELABEL(soc_label)
        DT_PROP(DT_CHILD(SOC_NODE, serial_40001000), status) // "okay"
        ```

        Node labels like `serial1` cannot be used as the `child` argument to this macro. Use [DT\_NODELABEL()](#group__devicetree-generic-id_1gab7d23294a6bf7fd44a98b48ec47d8a79) for that instead.

        You can also use [DT\_FOREACH\_CHILD()](#group__devicetree-generic-foreach_1ga2f4eead8e8190110f5c0eb353e6a408f) to iterate over node identifiers for all of a node’s children.

        Parameters:
        :   - **node\_id** – node identifier
            - **child** – lowercase-and-underscores child node name

        Returns:
        :   node identifier for the node with the name referred to by ‘child’

    DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat)
    :   Get a node identifier for a status `okay` node with a compatible.

        Use this if you want to get an arbitrary enabled node with a given compatible, and you do not care which one you get. If any enabled nodes with the given compatible exist, a node identifier for one of them is returned. Otherwise, [DT\_INVALID\_NODE](#group__devicetree-generic-id_1ga710cc4455dd7e738f43f750153163855) is returned.

        Example devicetree fragment:

        ```devicetree
        node-a {
           compatible = "vnd,device";
           status = "okay";
        };

        node-b {
           compatible = "vnd,device";
           status = "okay";
        };

        node-c {
           compatible = "vnd,device";
           status = "disabled";
        };
        ```

        Example usage:

        ```c
        DT_COMPAT_GET_ANY_STATUS_OKAY(vnd_device)
        ```

        This expands to a node identifier for either `node-a` or `node-b`. It will not expand to a node identifier for `node-c`, because that node does not have status `okay`.

        Parameters:
        :   - **compat** – lowercase-and-underscores compatible, without quotes

        Returns:
        :   node identifier for a node with that compatible, or [DT\_INVALID\_NODE](#group__devicetree-generic-id_1ga710cc4455dd7e738f43f750153163855)

    DT\_NODE\_PATH(node\_id)
    :   Get a devicetree node’s full path as a string literal.

        This returns the path to a node from a node identifier. To get a node identifier from path components instead, use [DT\_PATH()](#group__devicetree-generic-id_1ga015b4819473797982e83cae497697086).

        Example devicetree fragment:

        ```devicetree
        / {
                soc {
                        node: my-node@12345678 { ... };
                };
        };
        ```

        Example usage:

        ```c
        DT_NODE_PATH(DT_NODELABEL(node)) // "/soc/my-node@12345678"
        DT_NODE_PATH(DT_PATH(soc))       // "/soc"
        DT_NODE_PATH(DT_ROOT)            // "/"
        ```

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   the node’s full path in the devicetree

    DT\_NODE\_FULL\_NAME(node\_id)
    :   Get a devicetree node’s name with unit-address as a string literal.

        This returns the node name and unit-address from a node identifier.

        Example devicetree fragment:

        ```devicetree
        / {
                soc {
                        node: my-node@12345678 { ... };
                };
        };
        ```

        Example usage:

        ```c
        DT_NODE_FULL_NAME(DT_NODELABEL(node)) // "my-node@12345678"
        ```

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   the node’s name with unit-address as a string in the devicetree

    DT\_NODE\_CHILD\_IDX(node\_id)
    :   Get a devicetree node’s index into its parent’s list of children.

        Indexes are zero-based.

        It is an error to use this macro with the root node.

        Example devicetree fragment:

        ```devicetree
        parent {
                c1: child-1 {};
                c2: child-2 {};
        };
        ```

        Example usage:

        ```c
        DT_NODE_CHILD_IDX(DT_NODELABEL(c1)) // 0
        DT_NODE_CHILD_IDX(DT_NODELABEL(c2)) // 1
        ```

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   the node’s index in its parent node’s list of children

    DT\_SAME\_NODE(node\_id1, node\_id2)
    :   Do `node_id1` and `node_id2` refer to the same node?

        Both `node_id1` and `node_id2` must be node identifiers for nodes that exist in the devicetree (if unsure, you can check with [DT\_NODE\_EXISTS()](#group__devicetree-generic-exist_1ga9d5cf40051d042b853f6b0088fd4500a)).

        The expansion evaluates to 0 or 1, but may not be a literal integer 0 or 1.

        Parameters:
        :   - **node\_id1** – first node identifier
            - **node\_id2** – second node identifier

        Returns:
        :   an expression that evaluates to 1 if the node identifiers refer to the same node, and evaluates to 0 otherwise

### [Property access](#id5)

The following general-purpose macros can be used to access node properties.
There are special-purpose APIs for accessing the [ranges property](#devicetree-ranges-property),
[reg property](#devicetree-reg-property) and [interrupts property](#devicetree-interrupts-property).

Property values can be read using these macros even if the node is disabled,
as long as it has a matching binding.

*group* devicetree-generic-prop
:   Defines

    DT\_PROP(node\_id, prop)
    :   Get a devicetree property value.

        For properties whose bindings have the following types, this macro expands to:

        - string: a string literal
        - boolean: `0` if the property is false, or `1` if it is true
        - int: the property’s value as an integer literal
        - array, uint8-array, string-array: an initializer expression in braces, whose elements are integer or string literals (like `{0, 1, 2}`, `{"hello", "world"}`, etc.)
        - phandle: a node identifier for the node with that phandle

        A property’s type is usually defined by its binding. In some special cases, it has an assumed type defined by the devicetree specification even when no binding is available: `compatible` has type string-array, `status` has type string, and `interrupt-controller` has type boolean.

        For other properties or properties with unknown type due to a missing binding, behavior is undefined.

        For usage examples, see [DT\_PATH()](#group__devicetree-generic-id_1ga015b4819473797982e83cae497697086), [DT\_ALIAS()](#group__devicetree-generic-id_1gaa49e19bbc39dc0d6f16b78a5d02482c9), [DT\_NODELABEL()](#group__devicetree-generic-id_1gab7d23294a6bf7fd44a98b48ec47d8a79), and [DT\_INST()](#group__devicetree-generic-id_1gae199b930cb21ff38dab284a696093ead) above.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   a representation of the property’s value

    DT\_PROP\_LEN(node\_id, prop)
    :   Get a property’s logical length.

        Here, “length” is a number of elements, which may differ from the property’s size in bytes.

        The return value depends on the property’s type:

        - for types array, string-array, and uint8-array, this expands to the number of elements in the array
        - for type phandles, this expands to the number of phandles
        - for type phandle-array, this expands to the number of phandle and specifier blocks in the property
        - for type phandle, this expands to 1 (so that a phandle can be treated as a degenerate case of phandles with length 1)
        - for type string, this expands to 1 (so that a string can be treated as a degenerate case of string-array with length 1)

        These properties are handled as special cases:

        - reg property: use `[DT_NUM_REGS(node_id)](#group__devicetree-reg-prop_1ga6cdd22b6a2881b09ed63d9d262566a0a)` instead
        - interrupts property: use `[DT_NUM_IRQS(node_id)](#group__devicetree-interrupts-prop_1ga2985e5d55d2d9dbbbe93ba855d5db320)` instead

        It is an error to use this macro with the `ranges`, `dma-ranges`, `reg` or `interrupts` properties.

        For other properties, behavior is undefined.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – a lowercase-and-underscores property with a logical length

        Returns:
        :   the property’s length

    DT\_PROP\_LEN\_OR(node\_id, prop, default\_value)
    :   Like [DT\_PROP\_LEN()](#group__devicetree-generic-prop_1gaa7f5afcedd1f54be79a5337e8e28a5b6), but with a fallback to `default_value`.

        If the property is defined (as determined by [DT\_NODE\_HAS\_PROP()](#group__devicetree-generic-exist_1gacce67bf20541cd2d07d8540058964692)), this expands to [DT\_PROP\_LEN(node\_id, prop)](#group__devicetree-generic-prop_1gaa7f5afcedd1f54be79a5337e8e28a5b6). The `default_value` parameter is not expanded in this case.

        Otherwise, this expands to `default_value`.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – a lowercase-and-underscores property with a logical length
            - **default\_value** – a fallback value to expand to

        Returns:
        :   the property’s length or the given default value

    DT\_PROP\_HAS\_IDX(node\_id, prop, idx)
    :   Is index `idx` valid for an array type property?

        If this returns 1, then [DT\_PROP\_BY\_IDX(node\_id, prop, idx)](#group__devicetree-generic-prop_1ga52ad691ea4cae633ca702020e939d461) or [DT\_PHA\_BY\_IDX(node\_id, prop, idx, …)](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed) are valid at index `idx`. If it returns 0, it is an error to use those macros with that index.

        These properties are handled as special cases:

        - `reg` property: use [DT\_REG\_HAS\_IDX(node\_id, idx)](#group__devicetree-reg-prop_1ga59aa43231678d08eeac6e5b344048f02) instead
        - `interrupts` property: use [DT\_IRQ\_HAS\_IDX(node\_id, idx)](#group__devicetree-interrupts-prop_1ga238a290dc6cea9479104ff8f95de1c4c) instead

        It is an error to use this macro with the `reg` or `interrupts` properties.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – a lowercase-and-underscores property with a logical length
            - **idx** – index to check

        Returns:
        :   An expression which evaluates to 1 if `idx` is a valid index into the given property, and 0 otherwise.

    DT\_PROP\_HAS\_NAME(node\_id, prop, name)
    :   Is name `name` available in a `foo-names` property?

        This property is handled as special case:

        - `interrupts` property: use [DT\_IRQ\_HAS\_NAME(node\_id, idx)](#group__devicetree-interrupts-prop_1ga1c757ff5e4d15f1b3020b30f72c0dd5d) instead

        It is an error to use this macro with the `interrupts` property.

        Example devicetree fragment:

        ```devicetree
        nx: node-x {
           foos = <&bar xx yy>, <&baz xx zz>;
           foo-names = "event", "error";
           status = "okay";
        };
        ```

        Example usage:

        ```c
        DT_PROP_HAS_NAME(DT_NODELABEL(nx), foos, event)    // 1
        DT_PROP_HAS_NAME(DT_NODELABEL(nx), foos, failure)  // 0
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – a lowercase-and-underscores `prop-names` type property
            - **name** – a lowercase-and-underscores name to check

        Returns:
        :   An expression which evaluates to 1 if “name” is an available name into the given property, and 0 otherwise.

    DT\_PROP\_BY\_IDX(node\_id, prop, idx)
    :   Get the value at index `idx` in an array type property.

        It might help to read the argument order as being similar to `node->property[index]`.

        The return value depends on the property’s type:

        - for types array, string-array, uint8-array, and phandles, this expands to the idx-th array element as an integer, string literal, integer, and node identifier respectively
        - for type phandle, idx must be 0 and the expansion is a node identifier (this treats phandle like a phandles of length 1)
        - for type string, idx must be 0 and the expansion is the the entire string (this treats string like string-array of length 1)

        These properties are handled as special cases:

        - `reg`: use [DT\_REG\_ADDR\_BY\_IDX()](#group__devicetree-reg-prop_1gac540b00bb12d0662f6aefe6ac0cff243) or [DT\_REG\_SIZE\_BY\_IDX()](#group__devicetree-reg-prop_1ga9a703d688e4b983689b8579e0e7d9f48) instead
        - `interrupts`: use [DT\_IRQ\_BY\_IDX()](#group__devicetree-interrupts-prop_1ga3779b2115eac60ab32adfc8d212e973f)
        - `ranges`: use [DT\_NUM\_RANGES()](#group__devicetree-ranges-prop_1ga784cff5ee4c0439c429cc3c26c4410fc)
        - `dma-ranges`: it is an error to use this property with [DT\_PROP\_BY\_IDX()](#group__devicetree-generic-prop_1ga52ad691ea4cae633ca702020e939d461)

        For properties of other types, behavior is undefined.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **idx** – the index to get

        Returns:
        :   a representation of the idx-th element of the property

    DT\_PROP\_OR(node\_id, prop, default\_value)
    :   Like [DT\_PROP()](#group__devicetree-generic-prop_1ga8e1fd9ebacd85d2013df027d041d506b), but with a fallback to `default_value`.

        If the value exists, this expands to [DT\_PROP(node\_id, prop)](#group__devicetree-generic-prop_1ga8e1fd9ebacd85d2013df027d041d506b). The `default_value` parameter is not expanded in this case.

        Otherwise, this expands to `default_value`.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **default\_value** – a fallback value to expand to

        Returns:
        :   the property’s value or `default_value`

    DT\_ENUM\_IDX(node\_id, prop)
    :   Get a property value’s index into its enumeration values.

        The return values start at zero.

        Example devicetree fragment:

        ```devicetree
        usb1: usb@12340000 {
                maximum-speed = "full-speed";
        };
        usb2: usb@12341000 {
                maximum-speed = "super-speed";
        };
        ```

        Example bindings fragment:

        ```yaml
        properties:
          maximum-speed:
            type: string
            enum:
               - "low-speed"
               - "full-speed"
               - "high-speed"
               - "super-speed"
        ```

        Example usage:

        ```c
        DT_ENUM_IDX(DT_NODELABEL(usb1), maximum_speed) // 1
        DT_ENUM_IDX(DT_NODELABEL(usb2), maximum_speed) // 3
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   zero-based index of the property’s value in its enum: list

    DT\_ENUM\_IDX\_OR(node\_id, prop, default\_idx\_value)
    :   Like [DT\_ENUM\_IDX()](#group__devicetree-generic-prop_1ga6c1a3b93e30429c1c69a7e2d8fe2d840), but with a fallback to a default enum index.

        If the value exists, this expands to its zero based index value thanks to [DT\_ENUM\_IDX(node\_id, prop)](#group__devicetree-generic-prop_1ga6c1a3b93e30429c1c69a7e2d8fe2d840).

        Otherwise, this expands to provided default index enum value.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **default\_idx\_value** – a fallback index value to expand to

        Returns:
        :   zero-based index of the property’s value in its enum if present, default\_idx\_value otherwise

    DT\_ENUM\_HAS\_VALUE(node\_id, prop, value)
    :   Does a node enumeration property have a given value?

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **value** – lowercase-and-underscores enumeration value

        Returns:
        :   1 if the node property has the value *value*, 0 otherwise.

    DT\_STRING\_TOKEN(node\_id, prop)
    :   Get a string property’s value as a token.

        This removes “the quotes” from a string property’s value, converting any non-alphanumeric characters to underscores. This can be useful, for example, when programmatically using the value to form a C variable or code.

        [DT\_STRING\_TOKEN()](#group__devicetree-generic-prop_1ga5995350cc7fd2d12ef7daa2487d1db54) can only be used for properties with string type.

        It is an error to use [DT\_STRING\_TOKEN()](#group__devicetree-generic-prop_1ga5995350cc7fd2d12ef7daa2487d1db54) in other circumstances.

        Example devicetree fragment:

        ```devicetree
        n1: node-1 {
                prop = "foo";
        };
        n2: node-2 {
                prop = "FOO";
        }
        n3: node-3 {
                prop = "123 foo";
        };
        ```

        Example bindings fragment:

        ```yaml
        properties:
          prop:
            type: string
        ```

        Example usage:

        ```c
        DT_STRING_TOKEN(DT_NODELABEL(n1), prop) // foo
        DT_STRING_TOKEN(DT_NODELABEL(n2), prop) // FOO
        DT_STRING_TOKEN(DT_NODELABEL(n3), prop) // 123_foo
        ```

        Notice how:

        - Unlike C identifiers, the property values may begin with a number. It’s the user’s responsibility not to use such values as the name of a C identifier.
        - The uppercased `"FOO"` in the DTS remains `FOO` as a token. It is *not* converted to `foo`.
        - The whitespace in the DTS `"123 foo"` string is converted to `123_foo` as a token.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   the value of `prop` as a token, i.e. without any quotes and with special characters converted to underscores

    DT\_STRING\_TOKEN\_OR(node\_id, prop, default\_value)
    :   Like [DT\_STRING\_TOKEN()](#group__devicetree-generic-prop_1ga5995350cc7fd2d12ef7daa2487d1db54), but with a fallback to `default_value`.

        If the value exists, this expands to [DT\_STRING\_TOKEN(node\_id, prop)](#group__devicetree-generic-prop_1ga5995350cc7fd2d12ef7daa2487d1db54). The `default_value` parameter is not expanded in this case.

        Otherwise, this expands to `default_value`.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **default\_value** – a fallback value to expand to

        Returns:
        :   the property’s value as a token, or `default_value`

    DT\_STRING\_UPPER\_TOKEN(node\_id, prop)
    :   Like [DT\_STRING\_TOKEN()](#group__devicetree-generic-prop_1ga5995350cc7fd2d12ef7daa2487d1db54), but uppercased.

        This removes “the quotes” from a string property’s value, converting any non-alphanumeric characters to underscores, and capitalizing the result. This can be useful, for example, when programmatically using the value to form a C variable or code.

        [DT\_STRING\_UPPER\_TOKEN()](#group__devicetree-generic-prop_1gae0b5e2b6633a98ead17ec20d3494658f) can only be used for properties with string type.

        It is an error to use [DT\_STRING\_UPPER\_TOKEN()](#group__devicetree-generic-prop_1gae0b5e2b6633a98ead17ec20d3494658f) in other circumstances.

        Example devicetree fragment:

        ```devicetree
        n1: node-1 {
                prop = "foo";
        };
        n2: node-2 {
                prop = "123 foo";
        };
        ```

        Example bindings fragment:

        ```yaml
        properties:
          prop:
            type: string
        ```

        Example usage:

        ```c
        DT_STRING_UPPER_TOKEN(DT_NODELABEL(n1), prop) // FOO
        DT_STRING_UPPER_TOKEN(DT_NODELABEL(n2), prop) // 123_FOO
        ```

        Notice how:

        - Unlike C identifiers, the property values may begin with a number. It’s the user’s responsibility not to use such values as the name of a C identifier.
        - The lowercased `"foo"` in the DTS becomes `FOO` as a token, i.e. it is uppercased.
        - The whitespace in the DTS `"123 foo"` string is converted to `123_FOO` as a token, i.e. it is uppercased and whitespace becomes an underscore.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   the value of `prop` as an uppercased token, i.e. without any quotes and with special characters converted to underscores

    DT\_STRING\_UPPER\_TOKEN\_OR(node\_id, prop, default\_value)
    :   Like [DT\_STRING\_UPPER\_TOKEN()](#group__devicetree-generic-prop_1gae0b5e2b6633a98ead17ec20d3494658f), but with a fallback to `default_value`.

        If the value exists, this expands to [DT\_STRING\_UPPER\_TOKEN(node\_id, prop)](#group__devicetree-generic-prop_1gae0b5e2b6633a98ead17ec20d3494658f). The `default_value` parameter is not expanded in this case.

        Otherwise, this expands to `default_value`.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **default\_value** – a fallback value to expand to

        Returns:
        :   the property’s value as an uppercased token, or `default_value`

    DT\_STRING\_UNQUOTED(node\_id, prop)
    :   Get a string property’s value as an unquoted sequence of tokens.

        This removes “the quotes” from string-valued properties. That can be useful, for example, when defining floating point values as a string in devicetree that you would like to use to initialize a float or double variable in C.

        [DT\_STRING\_UNQUOTED()](#group__devicetree-generic-prop_1gad71ae303ce20e116a75c23ca552c2225) can only be used for properties with string type.

        It is an error to use [DT\_STRING\_UNQUOTED()](#group__devicetree-generic-prop_1gad71ae303ce20e116a75c23ca552c2225) in other circumstances.

        Example devicetree fragment:

        ```text
        n1: node-1 {
                prop = "12.7";
        };
        n2: node-2 {
                prop = "0.5";
        }
        n3: node-3 {
                prop = "A B C";
        };
        ```

        Example bindings fragment:

        ```text
        properties:
          prop:
            type: string
        ```

        Example usage:

        ```text
        DT_STRING_UNQUOTED(DT_NODELABEL(n1), prop) // 12.7
        DT_STRING_UNQUOTED(DT_NODELABEL(n2), prop) // 0.5
        DT_STRING_UNQUOTED(DT_NODELABEL(n3), prop) // A B C
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   the property’s value as a sequence of tokens, with no quotes

    DT\_STRING\_UNQUOTED\_OR(node\_id, prop, default\_value)
    :   Like [DT\_STRING\_UNQUOTED()](#group__devicetree-generic-prop_1gad71ae303ce20e116a75c23ca552c2225), but with a fallback to `default_value`.

        If the value exists, this expands to [DT\_STRING\_UNQUOTED(node\_id, prop)](#group__devicetree-generic-prop_1gad71ae303ce20e116a75c23ca552c2225). The `default_value` parameter is not expanded in this case.

        Otherwise, this expands to `default_value`.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **default\_value** – a fallback value to expand to

        Returns:
        :   the property’s value as a sequence of tokens, with no quotes, or `default_value`

    DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx)
    :   Get an element out of a string-array property as a token.

        This removes “the quotes” from an element in the array, and converts non-alphanumeric characters to underscores. That can be useful, for example, when programmatically using the value to form a C variable or code.

        [DT\_STRING\_TOKEN\_BY\_IDX()](#group__devicetree-generic-prop_1ga583e5e2e3c897f1095073e6192061d3a) can only be used for properties with string-array type.

        It is an error to use [DT\_STRING\_TOKEN\_BY\_IDX()](#group__devicetree-generic-prop_1ga583e5e2e3c897f1095073e6192061d3a) in other circumstances.

        Example devicetree fragment:

        ```devicetree
        n1: node-1 {
                prop = "f1", "F2";
        };
        n2: node-2 {
                prop = "123 foo", "456 FOO";
        };
        ```

        Example bindings fragment:

        ```yaml
        properties:
          prop:
            type: string-array
        ```

        Example usage:

        ```c
        DT_STRING_TOKEN_BY_IDX(DT_NODELABEL(n1), prop, 0) // f1
        DT_STRING_TOKEN_BY_IDX(DT_NODELABEL(n1), prop, 1) // F2
        DT_STRING_TOKEN_BY_IDX(DT_NODELABEL(n2), prop, 0) // 123_foo
        DT_STRING_TOKEN_BY_IDX(DT_NODELABEL(n2), prop, 1) // 456_FOO
        ```

        For more information, see [DT\_STRING\_TOKEN](#group__devicetree-generic-prop_1ga5995350cc7fd2d12ef7daa2487d1db54).

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **idx** – the index to get

        Returns:
        :   the element in `prop` at index `idx` as a token

    DT\_STRING\_UPPER\_TOKEN\_BY\_IDX(node\_id, prop, idx)
    :   Like [DT\_STRING\_TOKEN\_BY\_IDX()](#group__devicetree-generic-prop_1ga583e5e2e3c897f1095073e6192061d3a), but uppercased.

        This removes “the quotes” and capitalizes an element in the array, and converts non-alphanumeric characters to underscores. That can be useful, for example, when programmatically using the value to form a C variable or code.

        [DT\_STRING\_UPPER\_TOKEN\_BY\_IDX()](#group__devicetree-generic-prop_1ga73105b3402fbd6f82274a8b4a2ca6b35) can only be used for properties with string-array type.

        It is an error to use [DT\_STRING\_UPPER\_TOKEN\_BY\_IDX()](#group__devicetree-generic-prop_1ga73105b3402fbd6f82274a8b4a2ca6b35) in other circumstances.

        Example devicetree fragment:

        ```devicetree
        n1: node-1 {
                prop = "f1", "F2";
        };
        n2: node-2 {
                prop = "123 foo", "456 FOO";
        };
        ```

        Example bindings fragment:

        ```yaml
        properties:
          prop:
            type: string-array
        ```

        Example usage:

        ```c
        DT_STRING_UPPER_TOKEN_BY_IDX(DT_NODELABEL(n1), prop, 0) // F1
        DT_STRING_UPPER_TOKEN_BY_IDX(DT_NODELABEL(n1), prop, 1) // F2
        DT_STRING_UPPER_TOKEN_BY_IDX(DT_NODELABEL(n2), prop, 0) // 123_FOO
        DT_STRING_UPPER_TOKEN_BY_IDX(DT_NODELABEL(n2), prop, 1) // 456_FOO
        ```

        For more information, see [DT\_STRING\_UPPER\_TOKEN](#group__devicetree-generic-prop_1gae0b5e2b6633a98ead17ec20d3494658f).

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **idx** – the index to get

        Returns:
        :   the element in `prop` at index `idx` as an uppercased token

    DT\_STRING\_UNQUOTED\_BY\_IDX(node\_id, prop, idx)
    :   Get a string array item value as an unquoted sequence of tokens.

        This removes “the quotes” from string-valued item. That can be useful, for example, when defining floating point values as a string in devicetree that you would like to use to initialize a float or double variable in C.

        [DT\_STRING\_UNQUOTED\_BY\_IDX()](#group__devicetree-generic-prop_1ga3736709d70fdcb00bf305fd500f9ab64) can only be used for properties with string-array type.

        It is an error to use [DT\_STRING\_UNQUOTED\_BY\_IDX()](#group__devicetree-generic-prop_1ga3736709d70fdcb00bf305fd500f9ab64) in other circumstances.

        Example devicetree fragment:

        ```text
        n1: node-1 {
                prop = "12.7", "34.1";
        };
        n2: node-2 {
                prop = "A B", "C D";
        }
        ```

        Example bindings fragment:

        ```text
        properties:
          prop:
            type: string-array
        ```

        Example usage:

        ```text
        DT_STRING_UNQUOTED_BY_IDX(DT_NODELABEL(n1), prop, 0) // 12.7
        DT_STRING_UNQUOTED_BY_IDX(DT_NODELABEL(n1), prop, 1) // 34.1
        DT_STRING_UNQUOTED_BY_IDX(DT_NODELABEL(n2), prop, 0) // A B
        DT_STRING_UNQUOTED_BY_IDX(DT_NODELABEL(n2), prop, 1) // C D
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **idx** – the index to get

        Returns:
        :   the property’s value as a sequence of tokens, with no quotes

    DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, phs, idx, prop)
    :   Get a property value from a phandle in a property.

        This is a shorthand for:

        ```c
        DT_PROP(DT_PHANDLE_BY_IDX(node_id, phs, idx), prop)
        ```

        That is, `prop` is a property of the phandle’s node, not a property of `node_id`.

        Example devicetree fragment:

        ```devicetree
        n1: node-1 {
                foo = <&n2 &n3>;
        };

        n2: node-2 {
                bar = <42>;
        };

        n3: node-3 {
                baz = <43>;
        };
        ```

        Example usage:

        ```c
        #define N1 DT_NODELABEL(n1)

        DT_PROP_BY_PHANDLE_IDX(N1, foo, 0, bar) // 42
        DT_PROP_BY_PHANDLE_IDX(N1, foo, 1, baz) // 43
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **phs** – lowercase-and-underscores property with type `phandle`, `phandles`, or `phandle-array`
            - **idx** – logical index into `phs`, which must be zero if `phs` has type `phandle`
            - **prop** – lowercase-and-underscores property of the phandle’s node

        Returns:
        :   the property’s value

    DT\_PROP\_BY\_PHANDLE\_IDX\_OR(node\_id, phs, idx, prop, default\_value)
    :   Like [DT\_PROP\_BY\_PHANDLE\_IDX()](#group__devicetree-generic-prop_1gaeba973992914d493cff5506ecf86a00d), but with a fallback to `default_value`.

        If the value exists, this expands to [DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, phs,idx, prop)](#group__devicetree-generic-prop_1gaeba973992914d493cff5506ecf86a00d). The `default_value` parameter is not expanded in this case.

        Otherwise, this expands to `default_value`.

        Parameters:
        :   - **node\_id** – node identifier
            - **phs** – lowercase-and-underscores property with type `phandle`, `phandles`, or `phandle-array`
            - **idx** – logical index into `phs`, which must be zero if `phs` has type `phandle`
            - **prop** – lowercase-and-underscores property of the phandle’s node
            - **default\_value** – a fallback value to expand to

        Returns:
        :   the property’s value

    DT\_PROP\_BY\_PHANDLE(node\_id, ph, prop)
    :   Get a property value from a phandle’s node.

        This is equivalent to [DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, ph, 0, prop)](#group__devicetree-generic-prop_1gaeba973992914d493cff5506ecf86a00d).

        Parameters:
        :   - **node\_id** – node identifier
            - **ph** – lowercase-and-underscores property of `node_id` with type `phandle`
            - **prop** – lowercase-and-underscores property of the phandle’s node

        Returns:
        :   the property’s value

    DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell)
    :   Get a phandle-array specifier cell value at an index.

        It might help to read the argument order as being similar to `node->phandle_array[index].cell`. That is, the cell value is in the `pha` property of `node_id`, inside the specifier at index `idx`.

        Example devicetree fragment:

        ```devicetree
        gpio0: gpio@abcd1234 {
                #gpio-cells = <2>;
        };

        gpio1: gpio@1234abcd {
                #gpio-cells = <2>;
        };

        led: led_0 {
                gpios = <&gpio0 17 0x1>, <&gpio1 5 0x3>;
        };
        ```

        Bindings fragment for the `gpio0` and `gpio1` nodes:

        ```yaml
        gpio-cells:
          - pin
          - flags
        ```

        Above, `gpios` has two elements:

        - index 0 has specifier <17 0x1>, so its `pin` cell is 17, and its `flags` cell is 0x1
        - index 1 has specifier <5 0x3>, so `pin` is 5 and `flags` is 0x3

        Example usage:

        ```c
        #define LED DT_NODELABEL(led)

        DT_PHA_BY_IDX(LED, gpios, 0, pin)   // 17
        DT_PHA_BY_IDX(LED, gpios, 1, flags) // 0x3
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **idx** – logical index into `pha`
            - **cell** – lowercase-and-underscores cell name within the specifier at `pha` index `idx`

        Returns:
        :   the cell’s value

    DT\_PHA\_BY\_IDX\_OR(node\_id, pha, idx, cell, default\_value)
    :   Like [DT\_PHA\_BY\_IDX()](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed), but with a fallback to `default_value`.

        If the value exists, this expands to [DT\_PHA\_BY\_IDX(node\_id, pha,idx, cell)](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed). The `default_value` parameter is not expanded in this case.

        Otherwise, this expands to `default_value`.

        Parameters:
        :   - **node\_id** – node identifier
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **idx** – logical index into `pha`
            - **cell** – lowercase-and-underscores cell name within the specifier at `pha` index `idx`
            - **default\_value** – a fallback value to expand to

        Returns:
        :   the cell’s value or `default_value`

    DT\_PHA(node\_id, pha, cell)
    :   Equivalent to [DT\_PHA\_BY\_IDX(node\_id, pha, 0, cell)](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed).

        Parameters:
        :   - **node\_id** – node identifier
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell’s value

    DT\_PHA\_OR(node\_id, pha, cell, default\_value)
    :   Like [DT\_PHA()](#group__devicetree-generic-prop_1gacef5921973a55433161fe0be3f8f628d), but with a fallback to `default_value`.

        If the value exists, this expands to [DT\_PHA(node\_id, pha, cell)](#group__devicetree-generic-prop_1gacef5921973a55433161fe0be3f8f628d). The `default_value` parameter is not expanded in this case.

        Otherwise, this expands to `default_value`.

        Parameters:
        :   - **node\_id** – node identifier
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **cell** – lowercase-and-underscores cell name
            - **default\_value** – a fallback value to expand to

        Returns:
        :   the cell’s value or `default_value`

    DT\_PHA\_BY\_NAME(node\_id, pha, name, cell)
    :   Get a value within a phandle-array specifier by name.

        This is like [DT\_PHA\_BY\_IDX()](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed), except it treats `pha` as a structure where each array element has a name.

        It might help to read the argument order as being similar to `node->phandle_struct.name.cell`. That is, the cell value is in the `pha` property of `node_id`, treated as a data structure where each array element has a name.

        Example devicetree fragment:

        ```devicetree
        n: node {
                io-channels = <&adc1 10>, <&adc2 20>;
                io-channel-names = "SENSOR", "BANDGAP";
        };
        ```

        Bindings fragment for the “adc1” and “adc2” nodes:

        ```yaml
        io-channel-cells:
          - input
        ```

        Example usage:

        ```c
        DT_PHA_BY_NAME(DT_NODELABEL(n), io_channels, sensor, input)  // 10
        DT_PHA_BY_NAME(DT_NODELABEL(n), io_channels, bandgap, input) // 20
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **name** – lowercase-and-underscores name of a specifier in `pha`
            - **cell** – lowercase-and-underscores cell name in the named specifier

        Returns:
        :   the cell’s value

    DT\_PHA\_BY\_NAME\_OR(node\_id, pha, name, cell, default\_value)
    :   Like [DT\_PHA\_BY\_NAME()](#group__devicetree-generic-prop_1gae469615356a867c49416da15bdc44a26), but with a fallback to `default_value`.

        If the value exists, this expands to [DT\_PHA\_BY\_NAME(node\_id, pha,name, cell)](#group__devicetree-generic-prop_1gae469615356a867c49416da15bdc44a26). The `default_value` parameter is not expanded in this case.

        Otherwise, this expands to `default_value`.

        Parameters:
        :   - **node\_id** – node identifier
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **name** – lowercase-and-underscores name of a specifier in `pha`
            - **cell** – lowercase-and-underscores cell name in the named specifier
            - **default\_value** – a fallback value to expand to

        Returns:
        :   the cell’s value or `default_value`

    DT\_PHANDLE\_BY\_NAME(node\_id, pha, name)
    :   Get a phandle’s node identifier from a phandle array by `name`.

        It might help to read the argument order as being similar to `node->phandle_struct.name.phandle`. That is, the phandle array is treated as a structure with named elements. The return value is the node identifier for a phandle inside the structure.

        Example devicetree fragment:

        ```devicetree
        adc1: adc@abcd1234 {
                foobar = "ADC_1";
        };

        adc2: adc@1234abcd {
                foobar = "ADC_2";
        };

        n: node {
                io-channels = <&adc1 10>, <&adc2 20>;
                io-channel-names = "SENSOR", "BANDGAP";
        };
        ```

        Above, “io-channels” has two elements:

        - the element named `"SENSOR"` has phandle `&adc1`
        - the element named `"BANDGAP"` has phandle `&adc2`

        Example usage:

        ```c
        #define NODE DT_NODELABEL(n)

        DT_PROP(DT_PHANDLE_BY_NAME(NODE, io_channels, sensor), foobar)  // "ADC_1"
        DT_PROP(DT_PHANDLE_BY_NAME(NODE, io_channels, bandgap), foobar) // "ADC_2"
        ```

        Notice how devicetree properties and names are lowercased, and non-alphanumeric characters are converted to underscores.

        Parameters:
        :   - **node\_id** – node identifier
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **name** – lowercase-and-underscores name of an element in `pha`

        Returns:
        :   a node identifier for the node with that phandle

    DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)
    :   Get a node identifier for a phandle in a property.

        When a node’s value at a logical index contains a phandle, this macro returns a node identifier for the node with that phandle.

        Therefore, if `prop` has type `phandle`, `idx` must be zero. (A `phandle` type is treated as a `phandles` with a fixed length of 1).

        Example devicetree fragment:

        ```devicetree
        n1: node-1 {
                foo = <&n2 &n3>;
        };

        n2: node-2 { ... };
        n3: node-3 { ... };
        ```

        Above, `foo` has type phandles and has two elements:

        - index 0 has phandle `&n2`, which is `node-2`’s phandle
        - index 1 has phandle `&n3`, which is `node-3`’s phandle

        Example usage:

        ```c
        #define N1 DT_NODELABEL(n1)

        DT_PHANDLE_BY_IDX(N1, foo, 0) // node identifier for node-2
        DT_PHANDLE_BY_IDX(N1, foo, 1) // node identifier for node-3
        ```

        Behavior is analogous for phandle-arrays.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name in `node_id` with type `phandle`, `phandles` or `phandle-array`
            - **idx** – index into `prop`

        Returns:
        :   node identifier for the node with the phandle at that index

    DT\_PHANDLE(node\_id, prop)
    :   Get a node identifier for a phandle property’s value.

        This is equivalent to [DT\_PHANDLE\_BY\_IDX(node\_id, prop, 0)](#group__devicetree-generic-prop_1ga8ff163c240878a988d29d727671671de). Its primary benefit is readability when `prop` has type `phandle`.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property of `node_id` with type `phandle`

        Returns:
        :   a node identifier for the node pointed to by “ph”

### [`ranges` property](#id6)

Use these APIs instead of [Property access](#devicetree-property-access) to access the
`ranges` property. Because this property’s semantics are defined by the
devicetree specification, these macros can be used even for nodes without
matching bindings. However, they take on special semantics when the node’s
binding indicates it is a PCIe bus node, as defined in the
[PCI Bus Binding to: IEEE Std 1275-1994 Standard for Boot (Initialization Configuration) Firmware](https://www.openfirmware.info/data/docs/bus.pci.pdf)

*group* devicetree-ranges-prop
:   Defines

    DT\_NUM\_RANGES(node\_id)
    :   Get the number of range blocks in the ranges property.

        Use this instead of [DT\_PROP\_LEN(node\_id, ranges)](#group__devicetree-generic-prop_1gaa7f5afcedd1f54be79a5337e8e28a5b6).

        Example devicetree fragment:

        ```devicetree
        pcie0: pcie@0 {
                compatible = "pcie-controller";
                reg = <0 1>;
                #address-cells = <3>;
                #size-cells = <2>;

                ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,
                         <0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,
                         <0x3000000 0x80 0 0x80 0 0x80 0>;
        };

        other: other@1 {
                reg = <1 1>;

                ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,
                         <0x0 0x10000000 0x0 0x10000000 0x2eff0000>;
        };
        ```

        Example usage:

        ```c
        DT_NUM_RANGES(DT_NODELABEL(pcie0)) // 3
        DT_NUM_RANGES(DT_NODELABEL(other)) // 2
        ```

        Parameters:
        :   - **node\_id** – node identifier

    DT\_RANGES\_HAS\_IDX(node\_id, idx)
    :   Is `idx` a valid range block index?

        If this returns 1, then [DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx)](#group__devicetree-ranges-prop_1ga449940559213086b15151ec00e46607d), [DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx)](#group__devicetree-ranges-prop_1ga48d493ad616438ace2396c0312a242ba) or [DT\_RANGES\_LENGTH\_BY\_IDX(node\_id, idx)](#group__devicetree-ranges-prop_1ga52677a5bc86f9132a09b6bc37153afb2) are valid. For [DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx)](#group__devicetree-ranges-prop_1ga32a9c873d3ec1f5d7922c38eaafd1af8) the return value of [DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX(node\_id, idx)](#group__devicetree-ranges-prop_1ga3730c9176911bd8cc762f447eb020ecd) will indicate validity. If it returns 0, it is an error to use those macros with index `idx`, including [DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx)](#group__devicetree-ranges-prop_1ga32a9c873d3ec1f5d7922c38eaafd1af8).

        Example devicetree fragment:

        ```devicetree
        pcie0: pcie@0 {
                compatible = "pcie-controller";
                reg = <0 1>;
                #address-cells = <3>;
                #size-cells = <2>;

                ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,
                         <0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,
                         <0x3000000 0x80 0 0x80 0 0x80 0>;
        };

        other: other@1 {
                reg = <1 1>;

                ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,
                         <0x0 0x10000000 0x0 0x10000000 0x2eff0000>;
        };
        ```

        Example usage:

        ```c
        DT_RANGES_HAS_IDX(DT_NODELABEL(pcie0), 0) // 1
        DT_RANGES_HAS_IDX(DT_NODELABEL(pcie0), 1) // 1
        DT_RANGES_HAS_IDX(DT_NODELABEL(pcie0), 2) // 1
        DT_RANGES_HAS_IDX(DT_NODELABEL(pcie0), 3) // 0
        DT_RANGES_HAS_IDX(DT_NODELABEL(other), 0) // 1
        DT_RANGES_HAS_IDX(DT_NODELABEL(other), 1) // 1
        DT_RANGES_HAS_IDX(DT_NODELABEL(other), 2) // 0
        DT_RANGES_HAS_IDX(DT_NODELABEL(other), 3) // 0
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – index to check

        Returns:
        :   1 if `idx` is a valid register block index, 0 otherwise.

    DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX(node\_id, idx)
    :   Does a ranges property have child bus flags at index?

        If this returns 1, then [DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx)](#group__devicetree-ranges-prop_1ga32a9c873d3ec1f5d7922c38eaafd1af8) is valid. If it returns 0, it is an error to use this macro with index `idx`. This macro only returns 1 for PCIe buses (i.e. nodes whose bindings specify they are “pcie” bus nodes.)

        Example devicetree fragment:

        ```devicetree
        parent {
                #address-cells = <2>;

                pcie0: pcie@0 {
                        compatible = "pcie-controller";
                        reg = <0 0 1>;
                        #address-cells = <3>;
                        #size-cells = <2>;

                        ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,
                                 <0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,
                                 <0x3000000 0x80 0 0x80 0 0x80 0>;
                };

                other: other@1 {
                        reg = <0 1 1>;

                        ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,
                                 <0x0 0x10000000 0x0 0x10000000 0x2eff0000>;
                };
        };
        ```

        Example usage:

        ```c
        DT_RANGES_HAS_CHILD_BUS_FLAGS_AT_IDX(DT_NODELABEL(pcie0), 0) // 1
        DT_RANGES_HAS_CHILD_BUS_FLAGS_AT_IDX(DT_NODELABEL(pcie0), 1) // 1
        DT_RANGES_HAS_CHILD_BUS_FLAGS_AT_IDX(DT_NODELABEL(pcie0), 2) // 1
        DT_RANGES_HAS_CHILD_BUS_FLAGS_AT_IDX(DT_NODELABEL(pcie0), 3) // 0
        DT_RANGES_HAS_CHILD_BUS_FLAGS_AT_IDX(DT_NODELABEL(other), 0) // 0
        DT_RANGES_HAS_CHILD_BUS_FLAGS_AT_IDX(DT_NODELABEL(other), 1) // 0
        DT_RANGES_HAS_CHILD_BUS_FLAGS_AT_IDX(DT_NODELABEL(other), 2) // 0
        DT_RANGES_HAS_CHILD_BUS_FLAGS_AT_IDX(DT_NODELABEL(other), 3) // 0
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – logical index into the ranges array

        Returns:
        :   1 if `idx` is a valid child bus flags index, 0 otherwise.

    DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx)
    :   Get the ranges property child bus flags at index.

        When the node is a PCIe bus, the Child Bus Address has an extra cell used to store some flags, thus this cell is extracted from the Child Bus Address as Child Bus Flags field.

        Example devicetree fragments:

        ```devicetree
        parent {
                #address-cells = <2>;

                pcie0: pcie@0 {
                        compatible = "pcie-controller";
                        reg = <0 0 1>;
                        #address-cells = <3>;
                        #size-cells = <2>;

                        ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,
                                 <0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,
                                 <0x3000000 0x80 0 0x80 0 0x80 0>;
                };
        };
        ```

        Example usage:

        ```c
        DT_RANGES_CHILD_BUS_FLAGS_BY_IDX(DT_NODELABEL(pcie0), 0) // 0x1000000
        DT_RANGES_CHILD_BUS_FLAGS_BY_IDX(DT_NODELABEL(pcie0), 1) // 0x2000000
        DT_RANGES_CHILD_BUS_FLAGS_BY_IDX(DT_NODELABEL(pcie0), 2) // 0x3000000
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – logical index into the ranges array

        Returns:
        :   range child bus flags field at idx

    DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx)
    :   Get the ranges property child bus address at index.

        When the node is a PCIe bus, the Child Bus Address has an extra cell used to store some flags, thus this cell is removed from the Child Bus Address.

        Example devicetree fragments:

        ```devicetree
        parent {
                #address-cells = <2>;

                pcie0: pcie@0 {
                        compatible = "pcie-controller";
                        reg = <0 0 1>;
                        #address-cells = <3>;
                        #size-cells = <2>;

                        ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,
                                 <0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,
                                 <0x3000000 0x80 0 0x80 0 0x80 0>;
                };

                other: other@1 {
                        reg = <0 1 1>;

                        ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,
                                 <0x0 0x10000000 0x0 0x10000000 0x2eff0000>;
                };
        };
        ```

        Example usage:

        ```c
        DT_RANGES_CHILD_BUS_ADDRESS_BY_IDX(DT_NODELABEL(pcie0), 0) // 0
        DT_RANGES_CHILD_BUS_ADDRESS_BY_IDX(DT_NODELABEL(pcie0), 1) // 0x10000000
        DT_RANGES_CHILD_BUS_ADDRESS_BY_IDX(DT_NODELABEL(pcie0), 2) // 0x8000000000
        DT_RANGES_CHILD_BUS_ADDRESS_BY_IDX(DT_NODELABEL(other), 0) // 0
        DT_RANGES_CHILD_BUS_ADDRESS_BY_IDX(DT_NODELABEL(other), 1) // 0x10000000
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – logical index into the ranges array

        Returns:
        :   range child bus address field at idx

    DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx)
    :   Get the ranges property parent bus address at index.

        Similarly to [DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX()](#group__devicetree-ranges-prop_1ga449940559213086b15151ec00e46607d), this properly accounts for child bus flags cells when the node is a PCIe bus.

        Example devicetree fragment:

        ```devicetree
        parent {
                #address-cells = <2>;

                pcie0: pcie@0 {
                        compatible = "pcie-controller";
                        reg = <0 0 1>;
                        #address-cells = <3>;
                        #size-cells = <2>;

                        ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,
                                 <0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,
                                 <0x3000000 0x80 0 0x80 0 0x80 0>;
                };

                other: other@1 {
                        reg = <0 1 1>;

                        ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,
                                 <0x0 0x10000000 0x0 0x10000000 0x2eff0000>;
                };
        };
        ```

        Example usage:

        ```c
        DT_RANGES_PARENT_BUS_ADDRESS_BY_IDX(DT_NODELABEL(pcie0), 0) // 0x3eff0000
        DT_RANGES_PARENT_BUS_ADDRESS_BY_IDX(DT_NODELABEL(pcie0), 1) // 0x10000000
        DT_RANGES_PARENT_BUS_ADDRESS_BY_IDX(DT_NODELABEL(pcie0), 2) // 0x8000000000
        DT_RANGES_PARENT_BUS_ADDRESS_BY_IDX(DT_NODELABEL(other), 0) // 0x3eff0000
        DT_RANGES_PARENT_BUS_ADDRESS_BY_IDX(DT_NODELABEL(other), 1) // 0x10000000
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – logical index into the ranges array

        Returns:
        :   range parent bus address field at idx

    DT\_RANGES\_LENGTH\_BY\_IDX(node\_id, idx)
    :   Get the ranges property length at index.

        Similarly to [DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX()](#group__devicetree-ranges-prop_1ga449940559213086b15151ec00e46607d), this properly accounts for child bus flags cells when the node is a PCIe bus.

        Example devicetree fragment:

        ```devicetree
        parent {
                #address-cells = <2>;

                pcie0: pcie@0 {
                        compatible = "pcie-controller";
                        reg = <0 0 1>;
                        #address-cells = <3>;
                        #size-cells = <2>;

                        ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,
                                 <0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,
                                 <0x3000000 0x80 0 0x80 0 0x80 0>;
                };

                other: other@1 {
                        reg = <0 1 1>;

                        ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,
                                 <0x0 0x10000000 0x0 0x10000000 0x2eff0000>;
                };
        };
        ```

        Example usage:

        ```c
        DT_RANGES_LENGTH_BY_IDX(DT_NODELABEL(pcie0), 0) // 0x10000
        DT_RANGES_LENGTH_BY_IDX(DT_NODELABEL(pcie0), 1) // 0x2eff0000
        DT_RANGES_LENGTH_BY_IDX(DT_NODELABEL(pcie0), 2) // 0x8000000000
        DT_RANGES_LENGTH_BY_IDX(DT_NODELABEL(other), 0) // 0x10000
        DT_RANGES_LENGTH_BY_IDX(DT_NODELABEL(other), 1) // 0x2eff0000
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – logical index into the ranges array

        Returns:
        :   range length field at idx

    DT\_FOREACH\_RANGE(node\_id, fn)
    :   Invokes `fn` for each entry of `node_id` ranges property.

        The macro `fn` must take two parameters, `node_id` which will be the node identifier of the node with the ranges property and `idx` the index of the ranges block.

        Example devicetree fragment:

        ```devicetree
        n: node@0 {
                reg = <0 0 1>;

                ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,
                         <0x0 0x10000000 0x0 0x10000000 0x2eff0000>;
        };
        ```

        Example usage:

        ```c
        #define RANGE_LENGTH(node_id, idx) DT_RANGES_LENGTH_BY_IDX(node_id, idx),

        const uint64_t *ranges_length[] = {
                DT_FOREACH_RANGE(DT_NODELABEL(n), RANGE_LENGTH)
        };
        ```

        This expands to:

        ```c
        const char *ranges_length[] = {
            0x10000, 0x2eff0000,
        };
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **fn** – macro to invoke

### [`reg` property](#id7)

Use these APIs instead of [Property access](#devicetree-property-access) to access the
`reg` property. Because this property’s semantics are defined by the
devicetree specification, these macros can be used even for nodes without
matching bindings.

*group* devicetree-reg-prop
:   Defines

    DT\_NUM\_REGS(node\_id)
    :   Get the number of register blocks in the reg property.

        Use this instead of [DT\_PROP\_LEN(node\_id, reg)](#group__devicetree-generic-prop_1gaa7f5afcedd1f54be79a5337e8e28a5b6).

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   Number of register blocks in the node’s “reg” property.

    DT\_REG\_HAS\_IDX(node\_id, idx)
    :   Is `idx` a valid register block index?

        If this returns 1, then [DT\_REG\_ADDR\_BY\_IDX(node\_id, idx)](#group__devicetree-reg-prop_1gac540b00bb12d0662f6aefe6ac0cff243) or [DT\_REG\_SIZE\_BY\_IDX(node\_id, idx)](#group__devicetree-reg-prop_1ga9a703d688e4b983689b8579e0e7d9f48) are valid. If it returns 0, it is an error to use those macros with index `idx`.

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – index to check

        Returns:
        :   1 if `idx` is a valid register block index, 0 otherwise.

    DT\_REG\_ADDR\_BY\_IDX(node\_id, idx)
    :   Get the base address of the register block at index `idx`.

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – index of the register whose address to return

        Returns:
        :   address of the idx-th register block

    DT\_REG\_SIZE\_BY\_IDX(node\_id, idx)
    :   Get the size of the register block at index `idx`.

        This is the size of an individual register block, not the total number of register blocks in the property; use [DT\_NUM\_REGS()](#group__devicetree-reg-prop_1ga6cdd22b6a2881b09ed63d9d262566a0a) for that.

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – index of the register whose size to return

        Returns:
        :   size of the idx-th register block

    DT\_REG\_ADDR(node\_id)
    :   Get a node’s (only) register block address.

        Equivalent to [DT\_REG\_ADDR\_BY\_IDX(node\_id, 0)](#group__devicetree-reg-prop_1gac540b00bb12d0662f6aefe6ac0cff243).

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   node’s register block address

    DT\_REG\_ADDR\_U64(node\_id)
    :   64-bit version of [DT\_REG\_ADDR()](#group__devicetree-reg-prop_1gac6d8279c32351ced4c0ac7f32270974e)

        This macro version adds the appropriate suffix for 64-bit unsigned integer literals. Note that this macro is equivalent to [DT\_REG\_ADDR()](#group__devicetree-reg-prop_1gac6d8279c32351ced4c0ac7f32270974e) in linker/ASM context.

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   node’s register block address

    DT\_REG\_SIZE(node\_id)
    :   Get a node’s (only) register block size.

        Equivalent to [DT\_REG\_SIZE\_BY\_IDX(node\_id, 0)](#group__devicetree-reg-prop_1ga9a703d688e4b983689b8579e0e7d9f48).

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   node’s only register block’s size

    DT\_REG\_ADDR\_BY\_NAME(node\_id, name)
    :   Get a register block’s base address by name.

        Parameters:
        :   - **node\_id** – node identifier
            - **name** – lowercase-and-underscores register specifier name

        Returns:
        :   address of the register block specified by name

    DT\_REG\_ADDR\_BY\_NAME\_U64(node\_id, name)
    :   64-bit version of [DT\_REG\_ADDR\_BY\_NAME()](#group__devicetree-reg-prop_1gaeb5863e878bbd3a362e17616403da692)

        This macro version adds the appropriate suffix for 64-bit unsigned integer literals. Note that this macro is equivalent to [DT\_REG\_ADDR\_BY\_NAME()](#group__devicetree-reg-prop_1gaeb5863e878bbd3a362e17616403da692) in linker/ASM context.

        Parameters:
        :   - **node\_id** – node identifier
            - **name** – lowercase-and-underscores register specifier name

        Returns:
        :   address of the register block specified by name

    DT\_REG\_SIZE\_BY\_NAME(node\_id, name)
    :   Get a register block’s size by name.

        Parameters:
        :   - **node\_id** – node identifier
            - **name** – lowercase-and-underscores register specifier name

        Returns:
        :   size of the register block specified by name

### [`interrupts` property](#id8)

Use these APIs instead of [Property access](#devicetree-property-access) to access the
`interrupts` property.

Because this property’s semantics are defined by the devicetree specification,
some of these macros can be used even for nodes without matching bindings. This
does not apply to macros which take cell names as arguments.

*group* devicetree-interrupts-prop
:   Defines

    DT\_NUM\_IRQS(node\_id)
    :   Get the number of interrupt sources for the node.

        Use this instead of [DT\_PROP\_LEN(node\_id, interrupts)](#group__devicetree-generic-prop_1gaa7f5afcedd1f54be79a5337e8e28a5b6).

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   Number of interrupt specifiers in the node’s “interrupts” property.

    DT\_IRQ\_LEVEL(node\_id)
    :   Get the interrupt level for the node.

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   interrupt level

    DT\_IRQ\_HAS\_IDX(node\_id, idx)
    :   Is `idx` a valid interrupt index?

        If this returns 1, then [DT\_IRQ\_BY\_IDX(node\_id, idx)](#group__devicetree-interrupts-prop_1ga3779b2115eac60ab32adfc8d212e973f) is valid. If it returns 0, it is an error to use that macro with this index.

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – index to check

        Returns:
        :   1 if the idx is valid for the interrupt property 0 otherwise.

    DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, idx, cell)
    :   Does an interrupts property have a named cell specifier at an index?

        If this returns 1, then [DT\_IRQ\_BY\_IDX(node\_id, idx, cell)](#group__devicetree-interrupts-prop_1ga3779b2115eac60ab32adfc8d212e973f) is valid. If it returns 0, it is an error to use that macro.

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – index to check
            - **cell** – named cell value whose existence to check

        Returns:
        :   1 if the named cell exists in the interrupt specifier at index idx 0 otherwise.

    DT\_IRQ\_HAS\_CELL(node\_id, cell)
    :   Equivalent to [DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, 0, cell)](#group__devicetree-interrupts-prop_1ga739ebdd4bd01d6b7beb75d915174206f).

        Parameters:
        :   - **node\_id** – node identifier
            - **cell** – named cell value whose existence to check

        Returns:
        :   1 if the named cell exists in the interrupt specifier at index 0 0 otherwise.

    DT\_IRQ\_HAS\_NAME(node\_id, name)
    :   Does an interrupts property have a named specifier value at an index?

        If this returns 1, then [DT\_IRQ\_BY\_NAME(node\_id, name, cell)](#group__devicetree-interrupts-prop_1ga904917c0a407343ef0185e9e6fe96812) is valid. If it returns 0, it is an error to use that macro.

        Parameters:
        :   - **node\_id** – node identifier
            - **name** – lowercase-and-underscores interrupt specifier name

        Returns:
        :   1 if “name” is a valid named specifier 0 otherwise.

    DT\_IRQ\_BY\_IDX(node\_id, idx, cell)
    :   Get a value within an interrupt specifier at an index.

        It might help to read the argument order as being similar to “node->interrupts[index].cell”.

        This can be used to get information about an individual interrupt when a device generates more than one.

        Example devicetree fragment:

        ```devicetree
        my-serial: serial@abcd1234 {
                interrupts = < 33 0 >, < 34 1 >;
        };
        ```

        Assuming the node’s interrupt domain has “#interrupt-cells = <2>;” and the individual cells in each interrupt specifier are named “irq” and “priority” by the node’s binding, here are some examples:

        ```text
        #define SERIAL DT_NODELABEL(my_serial)

        Example usage                       Value
        -------------                       -----
        DT_IRQ_BY_IDX(SERIAL, 0, irq)          33
        DT_IRQ_BY_IDX(SERIAL, 0, priority)      0
        DT_IRQ_BY_IDX(SERIAL, 1, irq,          34
        DT_IRQ_BY_IDX(SERIAL, 1, priority)      1
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – logical index into the interrupt specifier array
            - **cell** – cell name specifier

        Returns:
        :   the named value at the specifier given by the index

    DT\_IRQ\_BY\_NAME(node\_id, name, cell)
    :   Get a value within an interrupt specifier by name.

        It might help to read the argument order as being similar to `node->interrupts.name.cell`.

        This can be used to get information about an individual interrupt when a device generates more than one, if the bindings give each interrupt specifier a name.

        Parameters:
        :   - **node\_id** – node identifier
            - **name** – lowercase-and-underscores interrupt specifier name
            - **cell** – cell name specifier

        Returns:
        :   the named value at the specifier given by the index

    DT\_IRQ(node\_id, cell)
    :   Get an interrupt specifier’s value Equivalent to [DT\_IRQ\_BY\_IDX(node\_id, 0, cell)](#group__devicetree-interrupts-prop_1ga3779b2115eac60ab32adfc8d212e973f).

        Parameters:
        :   - **node\_id** – node identifier
            - **cell** – cell name specifier

        Returns:
        :   the named value at that index

    DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx)
    :   Get an interrupt specifier’s interrupt controller by index.

        ```devicetree
        gpio0: gpio0 {
                interrupt-controller;
                #interrupt-cells = <2>;
        };

        foo: foo {
                interrupt-parent = <&gpio0>;
                interrupts = <1 1>, <2 2>;
        };

        bar: bar {
                interrupts-extended = <&gpio0 3 3>, <&pic0 4>;
        };

        pic0: pic0 {
                interrupt-controller;
                #interrupt-cells = <1>;

                qux: qux {
                        interrupts = <5>, <6>;
                        interrupt-names = "int1", "int2";
                };
        };
        ```

        Example usage:

        ```text
        DT_IRQ_INTC_BY_IDX(DT_NODELABEL(foo), 0) // &gpio0
        DT_IRQ_INTC_BY_IDX(DT_NODELABEL(foo), 1) // &gpio0
        DT_IRQ_INTC_BY_IDX(DT_NODELABEL(bar), 0) // &gpio0
        DT_IRQ_INTC_BY_IDX(DT_NODELABEL(bar), 1) // &pic0
        DT_IRQ_INTC_BY_IDX(DT_NODELABEL(qux), 0) // &pic0
        DT_IRQ_INTC_BY_IDX(DT_NODELABEL(qux), 1) // &pic0
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – interrupt specifier’s index

        Returns:
        :   node\_id of interrupt specifier’s interrupt controller

    DT\_IRQ\_INTC\_BY\_NAME(node\_id, name)
    :   Get an interrupt specifier’s interrupt controller by name.

        ```devicetree
        gpio0: gpio0 {
                interrupt-controller;
                #interrupt-cells = <2>;
        };

        foo: foo {
                interrupt-parent = <&gpio0>;
                interrupts = <1 1>, <2 2>;
                interrupt-names = "int1", "int2";
        };

        bar: bar {
                interrupts-extended = <&gpio0 3 3>, <&pic0 4>;
                interrupt-names = "int1", "int2";
        };

        pic0: pic0 {
                interrupt-controller;
                #interrupt-cells = <1>;

                qux: qux {
                        interrupts = <5>, <6>;
                        interrupt-names = "int1", "int2";
                };
        };
        ```

        Example usage:

        ```text
        DT_IRQ_INTC_BY_NAME(DT_NODELABEL(foo), int1) // &gpio0
        DT_IRQ_INTC_BY_NAME(DT_NODELABEL(foo), int2) // &gpio0
        DT_IRQ_INTC_BY_NAME(DT_NODELABEL(bar), int1) // &gpio0
        DT_IRQ_INTC_BY_NAME(DT_NODELABEL(bar), int2) // &pic0
        DT_IRQ_INTC_BY_NAME(DT_NODELABEL(qux), int1) // &pic0
        DT_IRQ_INTC_BY_NAME(DT_NODELABEL(qux), int2) // &pic0
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **name** – interrupt specifier’s name

        Returns:
        :   node\_id of interrupt specifier’s interrupt controller

    DT\_IRQ\_INTC(node\_id)
    :   Get an interrupt specifier’s interrupt controller.

        ```devicetree
        gpio0: gpio0 {
                interrupt-controller;
                #interrupt-cells = <2>;
        };

        foo: foo {
                interrupt-parent = <&gpio0>;
                interrupts = <1 1>;
        };

        bar: bar {
                interrupts-extended = <&gpio0 3 3>;
        };

        pic0: pic0 {
                interrupt-controller;
                #interrupt-cells = <1>;

                qux: qux {
                        interrupts = <5>;
                };
        };
        ```

        Example usage:

        ```text
        DT_IRQ_INTC(DT_NODELABEL(foo)) // &gpio0
        DT_IRQ_INTC(DT_NODELABEL(bar)) // &gpio0
        DT_IRQ_INTC(DT_NODELABEL(qux)) // &pic0
        ```

        See also

        [DT\_IRQ\_INTC\_BY\_IDX()](#group__devicetree-interrupts-prop_1ga061a34529fb2bbac9fe8615056d71ea4)

        Note

        Equivalent to [DT\_IRQ\_INTC\_BY\_IDX(node\_id, 0)](#group__devicetree-interrupts-prop_1ga061a34529fb2bbac9fe8615056d71ea4)

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   node\_id of interrupt specifier’s interrupt controller

    DT\_IRQN\_BY\_IDX(node\_id, idx)
    :   Get the node’s Zephyr interrupt number at index If  [`CONFIG_MULTI_LEVEL_INTERRUPTS`](../../../kconfig.md#CONFIG_MULTI_LEVEL_INTERRUPTS "CONFIG_MULTI_LEVEL_INTERRUPTS") is enabled, the interrupt number at index will be multi-level encoded.

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – logical index into the interrupt specifier array

        Returns:
        :   the Zephyr interrupt number

    DT\_IRQN(node\_id)
    :   Get a node’s (only) irq number.

        Equivalent to [DT\_IRQ(node\_id, irq)](#group__devicetree-interrupts-prop_1gabf60fbd528d300a26c0b4e66fe80a53f). This is provided as a convenience for the common case where a node generates exactly one interrupt, and the IRQ number is in a cell named `irq`.

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   the interrupt number for the node’s only interrupt

### [For-each macros](#id9)

There is currently only one “generic” for-each macro,
[`DT_FOREACH_CHILD()`](#c.DT_FOREACH_CHILD), which allows iterating over the children of a
devicetree node.

There are special-purpose for-each macros, like
[`DT_INST_FOREACH_STATUS_OKAY()`](#c.DT_INST_FOREACH_STATUS_OKAY), but these require `DT_DRV_COMPAT` to
be defined before use.

*group* devicetree-generic-foreach
:   Defines

    DT\_FOREACH\_NODE(fn)
    :   Invokes `fn` for every node in the tree.

        The macro `fn` must take one parameter, which will be a node identifier. The macro is expanded once for each node in the tree. The order that nodes are visited in is not specified.

        Parameters:
        :   - **fn** – macro to invoke

    DT\_FOREACH\_NODE\_VARGS(fn, ...)
    :   Invokes `fn` for every node in the tree with multiple arguments.

        The macro `fn` takes multiple arguments. The first should be the node identifier for the node. The remaining are passed-in by the caller.

        The macro is expanded once for each node in the tree. The order that nodes are visited in is not specified.

        Parameters:
        :   - **fn** – macro to invoke
            - **...** – variable number of arguments to pass to `fn`

    DT\_FOREACH\_STATUS\_OKAY\_NODE(fn)
    :   Invokes `fn` for every status `okay` node in the tree.

        The macro `fn` must take one parameter, which will be a node identifier. The macro is expanded once for each node in the tree with status `okay` (as usual, a missing status property is treated as status `okay`). The order that nodes are visited in is not specified.

        Parameters:
        :   - **fn** – macro to invoke

    DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS(fn, ...)
    :   Invokes `fn` for every status `okay` node in the tree with multiple arguments.

        The macro `fn` takes multiple arguments. The first should be the node identifier for the node. The remaining are passed-in by the caller.

        The macro is expanded once for each node in the tree with status `okay` (as usual, a missing status property is treated as status `okay`). The order that nodes are visited in is not specified.

        Parameters:
        :   - **fn** – macro to invoke
            - **...** – variable number of arguments to pass to `fn`

    DT\_FOREACH\_CHILD(node\_id, fn)
    :   Invokes `fn` for each child of `node_id`.

        The macro `fn` must take one parameter, which will be the node identifier of a child node of `node_id`.

        The children will be iterated over in the same order as they appear in the final devicetree.

        Example devicetree fragment:

        ```devicetree
        n: node {
                child-1 {
                        foobar = "foo";
                };
                child-2 {
                        foobar = "bar";
                };
        };
        ```

        Example usage:

        ```c
        #define FOOBAR_AND_COMMA(node_id) DT_PROP(node_id, foobar),

        const char *child_foobars[] = {
            DT_FOREACH_CHILD(DT_NODELABEL(n), FOOBAR_AND_COMMA)
        };
        ```

        This expands to:

        ```c
        const char *child_foobars[] = {
            "foo", "bar",
        };
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **fn** – macro to invoke

    DT\_FOREACH\_CHILD\_SEP(node\_id, fn, sep)
    :   Invokes `fn` for each child of `node_id` with a separator.

        The macro `fn` must take one parameter, which will be the node identifier of a child node of `node_id`.

        Example devicetree fragment:

        ```devicetree
        n: node {
                child-1 {
                        ...
                };
                child-2 {
                        ...
                };
        };
        ```

        Example usage:

        ```c
        const char *child_names[] = {
            DT_FOREACH_CHILD_SEP(DT_NODELABEL(n), DT_NODE_FULL_NAME, (,))
        };
        ```

        This expands to:

        ```c
        const char *child_names[] = {
            "child-1", "child-2"
        };
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **fn** – macro to invoke
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.

    DT\_FOREACH\_CHILD\_VARGS(node\_id, fn, ...)
    :   Invokes `fn` for each child of `node_id` with multiple arguments.

        The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

        The children will be iterated over in the same order as they appear in the final devicetree.

        See also

        [DT\_FOREACH\_CHILD](#group__devicetree-generic-foreach_1ga2f4eead8e8190110f5c0eb353e6a408f)

        Parameters:
        :   - **node\_id** – node identifier
            - **fn** – macro to invoke
            - **...** – variable number of arguments to pass to `fn`

    DT\_FOREACH\_CHILD\_SEP\_VARGS(node\_id, fn, sep, ...)
    :   Invokes `fn` for each child of `node_id` with separator and multiple arguments.

        The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

        See also

        [DT\_FOREACH\_CHILD\_VARGS](#group__devicetree-generic-foreach_1gae7461e9fa4687bf88cdd7c76f30986de)

        Parameters:
        :   - **node\_id** – node identifier
            - **fn** – macro to invoke
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.
            - **...** – variable number of arguments to pass to `fn`

    DT\_FOREACH\_CHILD\_STATUS\_OKAY(node\_id, fn)
    :   Call `fn` on the child nodes with status `okay`.

        The macro `fn` should take one argument, which is the node identifier for the child node.

        As usual, both a missing status and an `ok` status are treated as `okay`.

        The children will be iterated over in the same order as they appear in the final devicetree.

        Parameters:
        :   - **node\_id** – node identifier
            - **fn** – macro to invoke

    DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(node\_id, fn, sep)
    :   Call `fn` on the child nodes with status `okay` with separator.

        The macro `fn` should take one argument, which is the node identifier for the child node.

        As usual, both a missing status and an `ok` status are treated as `okay`.

        See also

        [DT\_FOREACH\_CHILD\_STATUS\_OKAY](#group__devicetree-generic-foreach_1gae907df926b94f1da52b1ab701392f3bd)

        Parameters:
        :   - **node\_id** – node identifier
            - **fn** – macro to invoke
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.

    DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(node\_id, fn, ...)
    :   Call `fn` on the child nodes with status `okay` with multiple arguments.

        The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

        As usual, both a missing status and an `ok` status are treated as `okay`.

        The children will be iterated over in the same order as they appear in the final devicetree.

        See also

        [DT\_FOREACH\_CHILD\_STATUS\_OKAY](#group__devicetree-generic-foreach_1gae907df926b94f1da52b1ab701392f3bd)

        Parameters:
        :   - **node\_id** – node identifier
            - **fn** – macro to invoke
            - **...** – variable number of arguments to pass to `fn`

    DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(node\_id, fn, sep, ...)
    :   Call `fn` on the child nodes with status `okay` with separator and multiple arguments.

        The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

        As usual, both a missing status and an `ok` status are treated as `okay`.

        See also

        DT\_FOREACH\_CHILD\_SEP\_STATUS\_OKAY

        Parameters:
        :   - **node\_id** – node identifier
            - **fn** – macro to invoke
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.
            - **...** – variable number of arguments to pass to `fn`

    DT\_FOREACH\_PROP\_ELEM(node\_id, prop, fn)
    :   Invokes `fn` for each element in the value of property `prop`.

        The macro `fn` must take three parameters: fn(node\_id, prop, idx). `node_id` and `prop` are the same as what is passed to [DT\_FOREACH\_PROP\_ELEM()](#group__devicetree-generic-foreach_1ga118a0477ab297a1bda9e16acf556babc), and `idx` is the current index into the array. The `idx` values are integer literals starting from 0.

        The `prop` argument must refer to a property that can be passed to [DT\_PROP\_LEN()](#group__devicetree-generic-prop_1gaa7f5afcedd1f54be79a5337e8e28a5b6).

        Example devicetree fragment:

        ```devicetree
        n: node {
                my-ints = <1 2 3>;
        };
        ```

        Example usage:

        ```c
        #define TIMES_TWO(node_id, prop, idx) \
                (2 * DT_PROP_BY_IDX(node_id, prop, idx)),

        int array[] = {
                DT_FOREACH_PROP_ELEM(DT_NODELABEL(n), my_ints, TIMES_TWO)
        };
        ```

        This expands to:

        ```c
        int array[] = {
                (2 * 1), (2 * 2), (2 * 3),
        };
        ```

        In general, this macro expands to:

        ```text
        fn(node_id, prop, 0) fn(node_id, prop, 1) [...] fn(node_id, prop, n-1)
        ```

        where `n` is the number of elements in `prop`, as it would be returned by `[DT_PROP_LEN(node_id, prop)](#group__devicetree-generic-prop_1gaa7f5afcedd1f54be79a5337e8e28a5b6)`.

        See also

        [DT\_PROP\_LEN](#group__devicetree-generic-prop_1gaa7f5afcedd1f54be79a5337e8e28a5b6)

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **fn** – macro to invoke

    DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, prop, fn, sep)
    :   Invokes `fn` for each element in the value of property `prop` with separator.

        Example devicetree fragment:

        ```devicetree
        n: node {
                my-gpios = <&gpioa 0 GPIO_ACTICE_HIGH>,
                           <&gpiob 1 GPIO_ACTIVE_HIGH>;
        };
        ```

        Example usage:

        ```c
        struct gpio_dt_spec specs[] = {
                DT_FOREACH_PROP_ELEM_SEP(DT_NODELABEL(n), my_gpios,
                                         GPIO_DT_SPEC_GET_BY_IDX, (,))
        };
        ```

        This expands as a first step to:

        ```c
        struct gpio_dt_spec specs[] = {
                GPIO_DT_SPEC_GET_BY_IDX(DT_NODELABEL(n), my_gpios, 0),
                GPIO_DT_SPEC_GET_BY_IDX(DT_NODELABEL(n), my_gpios, 1)
        };
        ```

        The `prop` parameter has the same restrictions as the same parameter given to [DT\_FOREACH\_PROP\_ELEM()](#group__devicetree-generic-foreach_1ga118a0477ab297a1bda9e16acf556babc).

        See also

        [DT\_FOREACH\_PROP\_ELEM](#group__devicetree-generic-foreach_1ga118a0477ab297a1bda9e16acf556babc)

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **fn** – macro to invoke
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.

    DT\_FOREACH\_PROP\_ELEM\_VARGS(node\_id, prop, fn, ...)
    :   Invokes `fn` for each element in the value of property `prop` with multiple arguments.

        The macro `fn` must take multiple parameters: `fn(node_id, prop, idx, ...)`. `node_id` and `prop` are the same as what is passed to [DT\_FOREACH\_PROP\_ELEM()](#group__devicetree-generic-foreach_1ga118a0477ab297a1bda9e16acf556babc), and `idx` is the current index into the array. The `idx` values are integer literals starting from 0. The remaining arguments are passed-in by the caller.

        The `prop` parameter has the same restrictions as the same parameter given to [DT\_FOREACH\_PROP\_ELEM()](#group__devicetree-generic-foreach_1ga118a0477ab297a1bda9e16acf556babc).

        See also

        [DT\_FOREACH\_PROP\_ELEM](#group__devicetree-generic-foreach_1ga118a0477ab297a1bda9e16acf556babc)

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **fn** – macro to invoke
            - **...** – variable number of arguments to pass to `fn`

    DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(node\_id, prop, fn, sep, ...)
    :   Invokes `fn` for each element in the value of property `prop` with multiple arguments and a separator.

        The `prop` parameter has the same restrictions as the same parameter given to [DT\_FOREACH\_PROP\_ELEM()](#group__devicetree-generic-foreach_1ga118a0477ab297a1bda9e16acf556babc).

        See also

        [DT\_FOREACH\_PROP\_ELEM\_VARGS](#group__devicetree-generic-foreach_1gaae36970d49c860414374c76e136a9607)

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name
            - **fn** – macro to invoke
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.
            - **...** – variable number of arguments to pass to fn

    DT\_FOREACH\_STATUS\_OKAY(compat, fn)
    :   Invokes `fn` for each status `okay` node of a compatible.

        This macro expands to:

        ```text
        fn(node_id_1) fn(node_id_2) ... fn(node_id_n)
        ```

        where each `node_id_<i>` is a node identifier for some node with compatible `compat` and status `okay`. Whitespace is added between expansions as shown above.

        Example devicetree fragment:

        ```devicetree
        / {
                a {
                        compatible = "foo";
                        status = "okay";
                };
                b {
                        compatible = "foo";
                        status = "disabled";
                };
                c {
                        compatible = "foo";
                };
        };
        ```

        Example usage:

        ```c
        DT_FOREACH_STATUS_OKAY(foo, DT_NODE_PATH)
        ```

        This expands to one of the following:

        ```text
        "/a" "/c"
        "/c" "/a"
        ```

        “One of the following” is because no guarantees are made about the order that node identifiers are passed to `fn` in the expansion.

        (The `/c` string literal is present because a missing status property is always treated as if the status were set to `okay`.)

        Note also that `fn` is responsible for adding commas, semicolons, or other terminators as needed.

        Parameters:
        :   - **compat** – lowercase-and-underscores devicetree compatible
            - **fn** – Macro to call for each enabled node. Must accept a node\_id as its only parameter.

    DT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, fn, ...)
    :   Invokes `fn` for each status `okay` node of a compatible with multiple arguments.

        This is like [DT\_FOREACH\_STATUS\_OKAY()](#group__devicetree-generic-foreach_1ga52b34316d269cc8d8ef2244d3ca460b8) except you can also pass additional arguments to `fn`.

        Example devicetree fragment:

        ```devicetree
        / {
                a {
                        compatible = "foo";
                        val = <3>;
                };
                b {
                        compatible = "foo";
                        val = <4>;
                };
        };
        ```

        Example usage:

        ```c
        #define MY_FN(node_id, operator) DT_PROP(node_id, val) operator
        x = DT_FOREACH_STATUS_OKAY_VARGS(foo, MY_FN, +) 0;
        ```

        This expands to one of the following:

        ```c
        x = 3 + 4 + 0;
        x = 4 + 3 + 0;
        ```

        i.e. it sets `x` to 7. As with [DT\_FOREACH\_STATUS\_OKAY()](#group__devicetree-generic-foreach_1ga52b34316d269cc8d8ef2244d3ca460b8), there are no guarantees about the order nodes appear in the expansion.

        Parameters:
        :   - **compat** – lowercase-and-underscores devicetree compatible
            - **fn** – Macro to call for each enabled node. Must accept a node\_id as its only parameter.
            - **...** – Additional arguments to pass to `fn`

### [Existence checks](#id10)

This section documents miscellaneous macros that can be used to test if a node
exists, how many nodes of a certain type exist, whether a node has certain
properties, etc. Some macros used for special purposes (such as
[`DT_IRQ_HAS_IDX()`](#c.DT_IRQ_HAS_IDX) and all macros which require `DT_DRV_COMPAT`) are
documented elsewhere on this page.

Related code samples

[GPIO with custom Devicetree binding](../../../samples/basic/custom_dts_binding/README.md#gpio-custom-dts-binding "Use custom Devicetree binding to control a GPIO.")
:   Use custom Devicetree binding to control a GPIO.

*group* devicetree-generic-exist
:   Defines

    DT\_NODE\_EXISTS(node\_id)
    :   Does a node identifier refer to a node?

        Tests whether a node identifier refers to a node which exists, i.e. is defined in the devicetree.

        It doesn’t matter whether or not the node has a matching binding, or what the node’s status value is. This is purely a check of whether the node exists at all.

        Parameters:
        :   - **node\_id** – a node identifier

        Returns:
        :   1 if the node identifier refers to a node, 0 otherwise.

    DT\_NODE\_HAS\_STATUS(node\_id, status)
    :   Does a node identifier refer to a node with a status?

        Example uses:

        ```c
        DT_NODE_HAS_STATUS(DT_PATH(soc, i2c_12340000), okay)
        DT_NODE_HAS_STATUS(DT_PATH(soc, i2c_12340000), disabled)
        ```

        Tests whether a node identifier refers to a node which:

        - exists in the devicetree, and
        - has a status property matching the second argument (except that either a missing status or an `ok` status in the devicetree is treated as if it were `okay` instead)

        Parameters:
        :   - **node\_id** – a node identifier
            - **status** – a status as one of the tokens okay or disabled, not a string

        Returns:
        :   1 if the node has the given status, 0 otherwise.

    DT\_HAS\_COMPAT\_STATUS\_OKAY(compat)
    :   Does the devicetree have a status `okay` node with a compatible?

        Test for whether the devicetree has any nodes with status `okay` and the given compatible. That is, this returns 1 if and only if there is at least one `node_id` for which both of these expressions return 1:

        ```c
        DT_NODE_HAS_STATUS(node_id, okay)
        DT_NODE_HAS_COMPAT(node_id, compat)
        ```

        As usual, both a missing status and an `ok` status are treated as `okay`.

        Parameters:
        :   - **compat** – lowercase-and-underscores compatible, without quotes

        Returns:
        :   1 if both of the above conditions are met, 0 otherwise

    DT\_NUM\_INST\_STATUS\_OKAY(compat)
    :   Get the number of instances of a given compatible with status `okay`.

        Parameters:
        :   - **compat** – lowercase-and-underscores compatible, without quotes

        Returns:
        :   Number of instances with status `okay`

    DT\_NODE\_HAS\_COMPAT(node\_id, compat)
    :   Does a devicetree node match a compatible?

        Example devicetree fragment:

        ```devicetree
        n: node {
                compatible = "vnd,specific-device", "generic-device";
        }
        ```

        Example usages which evaluate to 1:

        ```c
        DT_NODE_HAS_COMPAT(DT_NODELABEL(n), vnd_specific_device)
        DT_NODE_HAS_COMPAT(DT_NODELABEL(n), generic_device)
        ```

        This macro only uses the value of the compatible property. Whether or not a particular compatible has a matching binding has no effect on its value, nor does the node’s status.

        Parameters:
        :   - **node\_id** – node identifier
            - **compat** – lowercase-and-underscores compatible, without quotes

        Returns:
        :   1 if the node’s compatible property contains `compat`, 0 otherwise.

    DT\_NODE\_HAS\_COMPAT\_STATUS(node\_id, compat, status)
    :   Does a devicetree node have a compatible and status?

        This is equivalent to:

        ```c
        (DT_NODE_HAS_COMPAT(node_id, compat) &&
         DT_NODE_HAS_STATUS(node_id, status))
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **compat** – lowercase-and-underscores compatible, without quotes
            - **status** – okay or disabled as a token, not a string

    DT\_NODE\_HAS\_PROP(node\_id, prop)
    :   Does a devicetree node have a property?

        Tests whether a devicetree node has a property defined.

        This tests whether the property is defined at all, not whether a boolean property is true or false. To get a boolean property’s truth value, use [DT\_PROP(node\_id, prop)](#group__devicetree-generic-prop_1ga8e1fd9ebacd85d2013df027d041d506b) instead.

        Parameters:
        :   - **node\_id** – node identifier
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   1 if the node has the property, 0 otherwise.

    DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, idx, cell)
    :   Does a phandle array have a named cell specifier at an index?

        If this returns 1, then the phandle-array property `pha` has a cell named `cell` at index `idx`, and therefore [DT\_PHA\_BY\_IDX(node\_id,pha, idx, cell)](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed) is valid. If it returns 0, it’s an error to use [DT\_PHA\_BY\_IDX()](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed) with the same arguments.

        Parameters:
        :   - **node\_id** – node identifier
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **idx** – index to check within `pha`
            - **cell** – lowercase-and-underscores cell name whose existence to check at index `idx`

        Returns:
        :   1 if the named cell exists in the specifier at index idx, 0 otherwise.

    DT\_PHA\_HAS\_CELL(node\_id, pha, cell)
    :   Equivalent to [DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, 0, cell)](#group__devicetree-generic-exist_1gacfbd6a2cb3038e5aba1e2216d65ebc78).

        Parameters:
        :   - **node\_id** – node identifier
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **cell** – lowercase-and-underscores cell name whose existence to check at index `idx`

        Returns:
        :   1 if the named cell exists in the specifier at index 0, 0 otherwise.

### [Inter-node dependencies](#id11)

The `devicetree.h` API has some support for tracking dependencies between
nodes. Dependency tracking relies on a binary “depends on” relation between
devicetree nodes, which is defined as the [transitive closure](https://en.wikipedia.org/wiki/Transitive_closure) of the following “directly
depends on” relation:

- every non-root node directly depends on its parent node
- a node directly depends on any nodes its properties refer to by phandle
- a node directly depends on its `interrupt-parent` if it has an
  `interrupts` property
- a parent node inherits all dependencies from its child nodes

A *dependency ordering* of a devicetree is a list of its nodes, where each node
`n` appears earlier in the list than any nodes that depend on `n`. A node’s
*dependency ordinal* is then its zero-based index in that list. Thus, for two
distinct devicetree nodes `n1` and `n2` with dependency ordinals `d1` and
`d2`, we have:

- `d1 != d2`
- if `n1` depends on `n2`, then `d1 > d2`
- `d1 > d2` does **not** necessarily imply that `n1` depends on `n2`

The Zephyr build system chooses a dependency ordering of the final devicetree
and assigns a dependency ordinal to each node. Dependency related information
can be accessed using the following macros. The exact dependency ordering
chosen is an implementation detail, but cyclic dependencies are detected and
cause errors, so it’s safe to assume there are none when using these macros.

There are instance number-based conveniences as well; see
[`DT_INST_DEP_ORD()`](#c.DT_INST_DEP_ORD) and subsequent documentation.

*group* devicetree-dep-ord
:   Defines

    DT\_DEP\_ORD(node\_id)
    :   Get a node’s dependency ordinal.

        Parameters:
        :   - **node\_id** – Node identifier

        Returns:
        :   the node’s dependency ordinal as an integer literal

    DT\_DEP\_ORD\_STR\_SORTABLE(node\_id)
    :   Get a node’s dependency ordinal in string sortable form.

        Parameters:
        :   - **node\_id** – Node identifier

        Returns:
        :   the node’s dependency ordinal as a zero-padded integer literal

    DT\_REQUIRES\_DEP\_ORDS(node\_id)
    :   Get a list of dependency ordinals of a node’s direct dependencies.

        There is a comma after each ordinal in the expansion, **including** the last one:

        ```text
        DT_REQUIRES_DEP_ORDS(my_node) // required_ord_1, ..., required_ord_n,
        ```

        The one case [DT\_REQUIRES\_DEP\_ORDS()](#group__devicetree-dep-ord_1ga22dd1b0c89eb5ddfbfdd1e723d44f509) expands to nothing is when given the root node identifier `DT_ROOT` as argument. The root has no direct dependencies; every other node at least depends on its parent.

        Parameters:
        :   - **node\_id** – Node identifier

        Returns:
        :   a list of dependency ordinals, with each ordinal followed by a comma (`,`), or an empty expansion

    DT\_SUPPORTS\_DEP\_ORDS(node\_id)
    :   Get a list of dependency ordinals of what depends directly on a node.

        There is a comma after each ordinal in the expansion, **including** the last one:

        ```text
        DT_SUPPORTS_DEP_ORDS(my_node) // supported_ord_1, ..., supported_ord_n,
        ```

        [DT\_SUPPORTS\_DEP\_ORDS()](#group__devicetree-dep-ord_1ga3f559e9a787792685ed08be124b374ae) may expand to nothing. This happens when `node_id` refers to a leaf node that nothing else depends on.

        Parameters:
        :   - **node\_id** – Node identifier

        Returns:
        :   a list of dependency ordinals, with each ordinal followed by a comma (`,`), or an empty expansion

    DT\_INST\_DEP\_ORD(inst)
    :   Get a DT\_DRV\_COMPAT instance’s dependency ordinal.

        Equivalent to [DT\_DEP\_ORD(DT\_DRV\_INST(inst))](#group__devicetree-dep-ord_1ga5b96dccfd349dd0ddba1812aa942c1bd).

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   The instance’s dependency ordinal

    DT\_INST\_REQUIRES\_DEP\_ORDS(inst)
    :   Get a list of dependency ordinals of a DT\_DRV\_COMPAT instance’s direct dependencies.

        Equivalent to [DT\_REQUIRES\_DEP\_ORDS(DT\_DRV\_INST(inst))](#group__devicetree-dep-ord_1ga22dd1b0c89eb5ddfbfdd1e723d44f509).

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   a list of dependency ordinals for the nodes the instance depends on directly

    DT\_INST\_SUPPORTS\_DEP\_ORDS(inst)
    :   Get a list of dependency ordinals of what depends directly on a DT\_DRV\_COMPAT instance.

        Equivalent to [DT\_SUPPORTS\_DEP\_ORDS(DT\_DRV\_INST(inst))](#group__devicetree-dep-ord_1ga3f559e9a787792685ed08be124b374ae).

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   a list of node identifiers for the nodes that depend directly on the instance

### [Bus helpers](#id12)

Zephyr’s devicetree bindings language supports a `bus:` key which allows
bindings to declare that nodes with a given compatible describe system buses.
In this case, child nodes are considered to be on a bus of the given type, and
the following APIs may be used.

*group* devicetree-generic-bus
:   Defines

    DT\_BUS(node\_id)
    :   Node’s bus controller.

        Get the node identifier of the node’s bus controller. This can be used with [DT\_PROP()](#group__devicetree-generic-prop_1ga8e1fd9ebacd85d2013df027d041d506b) to get properties of the bus controller.

        It is an error to use this with nodes which do not have bus controllers.

        Example devicetree fragment:

        ```devicetree
        i2c@deadbeef {
                status = "okay";
                clock-frequency = < 100000 >;

                i2c_device: accelerometer@12 {
                        ...
                };
        };
        ```

        Example usage:

        ```c
        DT_PROP(DT_BUS(DT_NODELABEL(i2c_device)), clock_frequency) // 100000
        ```

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   a node identifier for the node’s bus controller

    DT\_ON\_BUS(node\_id, bus)
    :   Is a node on a bus of a given type?

        Example devicetree overlay:

        ```devicetree
        &i2c0 {
               temp: temperature-sensor@76 {
                        compatible = "vnd,some-sensor";
                        reg = <0x76>;
               };
        };
        ```

        Example usage, assuming `i2c0` is an I2C bus controller node, and therefore `temp` is on an I2C bus:

        ```c
        DT_ON_BUS(DT_NODELABEL(temp), i2c) // 1
        DT_ON_BUS(DT_NODELABEL(temp), spi) // 0
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **bus** – lowercase-and-underscores bus type as a C token (i.e. without quotes)

        Returns:
        :   1 if the node is on a bus of the given type, 0 otherwise

## [Instance-based APIs](#id13)

These are recommended for use within device drivers. To use them, define
`DT_DRV_COMPAT` to the lowercase-and-underscores compatible the device driver
implements support for. Here is an example devicetree fragment:

```devicetree
serial@40001000 {
        compatible = "vnd,serial";
        status = "okay";
        current-speed = <115200>;
};
```

Example usage, assuming `serial@40001000` is the only enabled node
with compatible `vnd,serial`:

```c
#define DT_DRV_COMPAT vnd_serial
DT_DRV_INST(0)                  // node identifier for serial@40001000
DT_INST_PROP(0, current_speed)  // 115200
```

Warning

Be careful making assumptions about instance numbers. See [`DT_INST()`](#c.DT_INST)
for the API guarantees.

As shown above, the `DT_INST_*` APIs are conveniences for addressing nodes by
instance number. They are almost all defined in terms of one of the
[Generic APIs](#devicetree-generic-apis). The equivalent generic API can be found by
removing `INST_` from the macro name. For example, `DT_INST_PROP(inst,
prop)` is equivalent to `DT_PROP(DT_DRV_INST(inst), prop)`. Similarly,
`DT_INST_REG_ADDR(inst)` is equivalent to `DT_REG_ADDR(DT_DRV_INST(inst))`,
and so on. There are some exceptions: [`DT_ANY_INST_ON_BUS_STATUS_OKAY()`](#c.DT_ANY_INST_ON_BUS_STATUS_OKAY)
and [`DT_INST_FOREACH_STATUS_OKAY()`](#c.DT_INST_FOREACH_STATUS_OKAY) are special-purpose helpers without
straightforward generic equivalents.

Since `DT_DRV_INST()` requires `DT_DRV_COMPAT` to be defined, it’s an error
to use any of these without that macro defined.

Note that there are also helpers available for
specific hardware; these are documented in [Hardware specific APIs](#devicetree-hw-api).

*group* devicetree-inst
:   Defines

    DT\_DRV\_INST(inst)
    :   Node identifier for an instance of a `DT_DRV_COMPAT` compatible.

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   a node identifier for the node with `DT_DRV_COMPAT` compatible and instance number `inst`

    DT\_INST\_PARENT(inst)
    :   Get a `DT_DRV_COMPAT` parent’s node identifier.

        See also

        [DT\_PARENT](#group__devicetree-generic-id_1ga3ac56d491510275ee1321446796ab63b)

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   a node identifier for the instance’s parent

    DT\_INST\_GPARENT(inst)
    :   Get a `DT_DRV_COMPAT` grandparent’s node identifier.

        See also

        [DT\_GPARENT](#group__devicetree-generic-id_1gaa4eccf276a426cbbc6e440d72b692753)

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   a node identifier for the instance’s grandparent

    DT\_INST\_CHILD(inst, child)
    :   Get a node identifier for a child node of [DT\_DRV\_INST(inst)](#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1).

        See also

        [DT\_CHILD](#group__devicetree-generic-id_1ga88259608f4e9083ccc2e9ca5ec2c212e)

        Parameters:
        :   - **inst** – instance number
            - **child** – lowercase-and-underscores child node name

        Returns:
        :   node identifier for the node with the name referred to by ‘child’

    DT\_INST\_FOREACH\_CHILD(inst, fn)
    :   Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1).

        The macro `fn` should take one argument, which is the node identifier for the child node.

        The children will be iterated over in the same order as they appear in the final devicetree.

        See also

        [DT\_FOREACH\_CHILD](#group__devicetree-generic-foreach_1ga2f4eead8e8190110f5c0eb353e6a408f)

        Parameters:
        :   - **inst** – instance number
            - **fn** – macro to invoke on each child node identifier

    DT\_INST\_FOREACH\_CHILD\_SEP(inst, fn, sep)
    :   Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1) with a separator.

        The macro `fn` should take one argument, which is the node identifier for the child node.

        See also

        [DT\_FOREACH\_CHILD\_SEP](#group__devicetree-generic-foreach_1ga1fbeb335d66745803dbf7a185bf10afc)

        Parameters:
        :   - **inst** – instance number
            - **fn** – macro to invoke on each child node identifier
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.

    DT\_INST\_FOREACH\_CHILD\_VARGS(inst, fn, ...)
    :   Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1).

        The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

        The children will be iterated over in the same order as they appear in the final devicetree.

        See also

        [DT\_FOREACH\_CHILD](#group__devicetree-generic-foreach_1ga2f4eead8e8190110f5c0eb353e6a408f)

        Parameters:
        :   - **inst** – instance number
            - **fn** – macro to invoke on each child node identifier
            - **...** – variable number of arguments to pass to `fn`

    DT\_INST\_FOREACH\_CHILD\_SEP\_VARGS(inst, fn, sep, ...)
    :   Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1) with separator.

        The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

        See also

        [DT\_FOREACH\_CHILD\_SEP\_VARGS](#group__devicetree-generic-foreach_1ga0042485aef7caaa48fa252b76a6629aa)

        Parameters:
        :   - **inst** – instance number
            - **fn** – macro to invoke on each child node identifier
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.
            - **...** – variable number of arguments to pass to `fn`

    DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY(inst, fn)
    :   Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1) with status `okay`.

        The macro `fn` should take one argument, which is the node identifier for the child node.

        See also

        [DT\_FOREACH\_CHILD\_STATUS\_OKAY](#group__devicetree-generic-foreach_1gae907df926b94f1da52b1ab701392f3bd)

        Parameters:
        :   - **inst** – instance number
            - **fn** – macro to invoke on each child node identifier

    DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(inst, fn, sep)
    :   Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1) with status `okay` and with separator.

        The macro `fn` should take one argument, which is the node identifier for the child node.

        See also

        [DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP](#group__devicetree-generic-foreach_1ga97414c01ebbb6df5ee2862c0ee9d44ce)

        Parameters:
        :   - **inst** – instance number
            - **fn** – macro to invoke on each child node identifier
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.

    DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(inst, fn, ...)
    :   Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1) with status `okay` and multiple arguments.

        The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

        See also

        [DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS](#group__devicetree-generic-foreach_1ga8bbf6992e5f90d8a28035ea6211dd2a3)

        Parameters:
        :   - **inst** – instance number
            - **fn** – macro to invoke on each child node identifier
            - **...** – variable number of arguments to pass to `fn`

    DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(inst, fn, sep, ...)
    :   Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1) with status `okay` and with separator and multiple arguments.

        The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

        See also

        [DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS](#group__devicetree-generic-foreach_1gaf46c1ac296f0d6c9388c3ca6fb4ca5cd)

        Parameters:
        :   - **inst** – instance number
            - **fn** – macro to invoke on each child node identifier
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.
            - **...** – variable number of arguments to pass to `fn`

    DT\_INST\_ENUM\_IDX(inst, prop)
    :   Get a `DT_DRV_COMPAT` value’s index into its enumeration values.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   zero-based index of the property’s value in its enum: list

    DT\_INST\_ENUM\_IDX\_OR(inst, prop, default\_idx\_value)
    :   Like [DT\_INST\_ENUM\_IDX()](#group__devicetree-inst_1ga866d6c28eb7a72ba9831c7ee1ecb98d2), but with a fallback to a default enum index.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **default\_idx\_value** – a fallback index value to expand to

        Returns:
        :   zero-based index of the property’s value in its enum if present, default\_idx\_value otherwise

    DT\_INST\_ENUM\_HAS\_VALUE(inst, prop, value)
    :   Does a `DT_DRV_COMPAT` enumeration property have a given value?

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **value** – lowercase-and-underscores enumeration value

        Returns:
        :   1 if the node property has the value *value*, 0 otherwise.

    DT\_INST\_PROP(inst, prop)
    :   Get a `DT_DRV_COMPAT` instance property.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   a representation of the property’s value

    DT\_INST\_PROP\_LEN(inst, prop)
    :   Get a `DT_DRV_COMPAT` property length.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   logical length of the property

    DT\_INST\_PROP\_HAS\_IDX(inst, prop, idx)
    :   Is index `idx` valid for an array type property on a `DT_DRV_COMPAT` instance?

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **idx** – index to check

        Returns:
        :   1 if `idx` is a valid index into the given property, 0 otherwise.

    DT\_INST\_PROP\_HAS\_NAME(inst, prop, name)
    :   Is name `name` available in a `foo-names` property?

        Parameters:
        :   - **inst** – instance number
            - **prop** – a lowercase-and-underscores `prop-names` type property
            - **name** – a lowercase-and-underscores name to check

        Returns:
        :   An expression which evaluates to 1 if `name` is an available name into the given property, and 0 otherwise.

    DT\_INST\_PROP\_BY\_IDX(inst, prop, idx)
    :   Get a `DT_DRV_COMPAT` element value in an array property.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **idx** – the index to get

        Returns:
        :   a representation of the idx-th element of the property

    DT\_INST\_PROP\_OR(inst, prop, default\_value)
    :   Like [DT\_INST\_PROP()](#group__devicetree-inst_1ga9dce2e631b2a94804e8f2bcc76c6eff8), but with a fallback to `default_value`.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **default\_value** – a fallback value to expand to

        Returns:
        :   [DT\_INST\_PROP(inst, prop)](#group__devicetree-inst_1ga9dce2e631b2a94804e8f2bcc76c6eff8) or `default_value`

    DT\_INST\_PROP\_LEN\_OR(inst, prop, default\_value)
    :   Like [DT\_INST\_PROP\_LEN()](#group__devicetree-inst_1ga9471df75ff3c4f8d2298bb69c581b365), but with a fallback to `default_value`.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **default\_value** – a fallback value to expand to

        Returns:
        :   [DT\_INST\_PROP\_LEN(inst, prop)](#group__devicetree-inst_1ga9471df75ff3c4f8d2298bb69c581b365) or `default_value`

    DT\_INST\_STRING\_TOKEN(inst, prop)
    :   Get a `DT_DRV_COMPAT` instance’s string property’s value as a token.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   the value of `prop` as a token, i.e. without any quotes and with special characters converted to underscores

    DT\_INST\_STRING\_UPPER\_TOKEN(inst, prop)
    :   Like [DT\_INST\_STRING\_TOKEN()](#group__devicetree-inst_1ga8e8c72187ce0d47fd24e4585f3d48484), but uppercased.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   the value of `prop` as an uppercased token, i.e. without any quotes and with special characters converted to underscores

    DT\_INST\_STRING\_UNQUOTED(inst, prop)
    :   Get a `DT_DRV_COMPAT` instance’s string property’s value as an unquoted sequence of tokens.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   the value of `prop` as a sequence of tokens, with no quotes

    DT\_INST\_STRING\_TOKEN\_BY\_IDX(inst, prop, idx)
    :   Get an element out of string-array property as a token.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **idx** – the index to get

        Returns:
        :   the element in `prop` at index `idx` as a token

    DT\_INST\_STRING\_UPPER\_TOKEN\_BY\_IDX(inst, prop, idx)
    :   Like [DT\_INST\_STRING\_TOKEN\_BY\_IDX()](#group__devicetree-inst_1gae1c28cbd9c1869112d2ae5c7ddf00b97), but uppercased.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **idx** – the index to get

        Returns:
        :   the element in `prop` at index `idx` as an uppercased token

    DT\_INST\_STRING\_UNQUOTED\_BY\_IDX(inst, prop, idx)
    :   Get an element out of string-array property as an unquoted sequence of tokens.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **idx** – the index to get

        Returns:
        :   the value of `prop` at index `idx` as a sequence of tokens, with no quotes

    DT\_INST\_PROP\_BY\_PHANDLE(inst, ph, prop)
    :   Get a `DT_DRV_COMPAT` instance’s property value from a phandle’s node.

        Parameters:
        :   - **inst** – instance number
            - **ph** – lowercase-and-underscores property of `inst` with type `phandle`
            - **prop** – lowercase-and-underscores property of the phandle’s node

        Returns:
        :   the value of `prop` as described in the [DT\_PROP()](#group__devicetree-generic-prop_1ga8e1fd9ebacd85d2013df027d041d506b) documentation

    DT\_INST\_PROP\_BY\_PHANDLE\_IDX(inst, phs, idx, prop)
    :   Get a `DT_DRV_COMPAT` instance’s property value from a phandle in a property.

        Parameters:
        :   - **inst** – instance number
            - **phs** – lowercase-and-underscores property with type `phandle`, `phandles`, or `phandle-array`
            - **idx** – logical index into “phs”, which must be zero if “phs” has type `phandle`
            - **prop** – lowercase-and-underscores property of the phandle’s node

        Returns:
        :   the value of `prop` as described in the [DT\_PROP()](#group__devicetree-generic-prop_1ga8e1fd9ebacd85d2013df027d041d506b) documentation

    DT\_INST\_PHA\_BY\_IDX(inst, pha, idx, cell)
    :   Get a `DT_DRV_COMPAT` instance’s phandle-array specifier value at an index.

        Parameters:
        :   - **inst** – instance number
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **idx** – logical index into the property `pha`
            - **cell** – binding’s cell name within the specifier at index `idx`

        Returns:
        :   the value of the cell inside the specifier at index `idx`

    DT\_INST\_PHA\_BY\_IDX\_OR(inst, pha, idx, cell, default\_value)
    :   Like [DT\_INST\_PHA\_BY\_IDX()](#group__devicetree-inst_1gaac886e11906d628acad1d73ed3a64018), but with a fallback to default\_value.

        Parameters:
        :   - **inst** – instance number
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **idx** – logical index into the property `pha`
            - **cell** – binding’s cell name within the specifier at index `idx`
            - **default\_value** – a fallback value to expand to

        Returns:
        :   [DT\_INST\_PHA\_BY\_IDX(inst, pha, idx, cell)](#group__devicetree-inst_1gaac886e11906d628acad1d73ed3a64018) or default\_value

    DT\_INST\_PHA(inst, pha, cell)
    :   Get a `DT_DRV_COMPAT` instance’s phandle-array specifier value Equivalent to [DT\_INST\_PHA\_BY\_IDX(inst, pha, 0, cell)](#group__devicetree-inst_1gaac886e11906d628acad1d73ed3a64018).

        Parameters:
        :   - **inst** – instance number
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **cell** – binding’s cell name for the specifier at `pha` index 0

        Returns:
        :   the cell value

    DT\_INST\_PHA\_OR(inst, pha, cell, default\_value)
    :   Like [DT\_INST\_PHA()](#group__devicetree-inst_1ga0de189f14fa7dd38a99382b7f2adbff8), but with a fallback to default\_value.

        Parameters:
        :   - **inst** – instance number
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **cell** – binding’s cell name for the specifier at `pha` index 0
            - **default\_value** – a fallback value to expand to

        Returns:
        :   [DT\_INST\_PHA(inst, pha, cell)](#group__devicetree-inst_1ga0de189f14fa7dd38a99382b7f2adbff8) or default\_value

    DT\_INST\_PHA\_BY\_NAME(inst, pha, name, cell)
    :   Get a `DT_DRV_COMPAT` instance’s value within a phandle-array specifier by name.

        Parameters:
        :   - **inst** – instance number
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **name** – lowercase-and-underscores name of a specifier in `pha`
            - **cell** – binding’s cell name for the named specifier

        Returns:
        :   the cell value

    DT\_INST\_PHA\_BY\_NAME\_OR(inst, pha, name, cell, default\_value)
    :   Like [DT\_INST\_PHA\_BY\_NAME()](#group__devicetree-inst_1ga25418914c5190df10c842744aa967dc8), but with a fallback to default\_value.

        Parameters:
        :   - **inst** – instance number
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **name** – lowercase-and-underscores name of a specifier in `pha`
            - **cell** – binding’s cell name for the named specifier
            - **default\_value** – a fallback value to expand to

        Returns:
        :   [DT\_INST\_PHA\_BY\_NAME(inst, pha, name, cell)](#group__devicetree-inst_1ga25418914c5190df10c842744aa967dc8) or default\_value

    DT\_INST\_PHANDLE\_BY\_NAME(inst, pha, name)
    :   Get a `DT_DRV_COMPAT` instance’s phandle node identifier from a phandle array by name.

        Parameters:
        :   - **inst** – instance number
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **name** – lowercase-and-underscores name of an element in `pha`

        Returns:
        :   node identifier for the phandle at the element named “name”

    DT\_INST\_PHANDLE\_BY\_IDX(inst, prop, idx)
    :   Get a `DT_DRV_COMPAT` instance’s node identifier for a phandle in a property.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name in `inst` with type `phandle`, `phandles` or `phandle-array`
            - **idx** – index into `prop`

        Returns:
        :   a node identifier for the phandle at index `idx` in `prop`

    DT\_INST\_PHANDLE(inst, prop)
    :   Get a `DT_DRV_COMPAT` instance’s node identifier for a phandle property’s value.

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property of `inst` with type `phandle`

        Returns:
        :   a node identifier for the node pointed to by “ph”

    DT\_INST\_REG\_HAS\_IDX(inst, idx)
    :   is `idx` a valid register block index on a `DT_DRV_COMPAT` instance?

        Parameters:
        :   - **inst** – instance number
            - **idx** – index to check

        Returns:
        :   1 if `idx` is a valid register block index, 0 otherwise.

    DT\_INST\_REG\_ADDR\_BY\_IDX(inst, idx)
    :   Get a `DT_DRV_COMPAT` instance’s idx-th register block’s address.

        Parameters:
        :   - **inst** – instance number
            - **idx** – index of the register whose address to return

        Returns:
        :   address of the instance’s idx-th register block

    DT\_INST\_REG\_SIZE\_BY\_IDX(inst, idx)
    :   Get a `DT_DRV_COMPAT` instance’s idx-th register block’s size.

        Parameters:
        :   - **inst** – instance number
            - **idx** – index of the register whose size to return

        Returns:
        :   size of the instance’s idx-th register block

    DT\_INST\_REG\_ADDR\_BY\_NAME(inst, name)
    :   Get a `DT_DRV_COMPAT`’s register block address by name.

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores register specifier name

        Returns:
        :   address of the register block with the given `name`

    DT\_INST\_REG\_ADDR\_BY\_NAME\_U64(inst, name)
    :   64-bit version of [DT\_INST\_REG\_ADDR\_BY\_NAME()](#group__devicetree-inst_1ga722d6f7b97136aa9229242e4ba7dd25c)

        This macro version adds the appropriate suffix for 64-bit unsigned integer literals. Note that this macro is equivalent to [DT\_INST\_REG\_ADDR\_BY\_NAME()](#group__devicetree-inst_1ga722d6f7b97136aa9229242e4ba7dd25c) in linker/ASM context.

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores register specifier name

        Returns:
        :   address of the register block with the given `name`

    DT\_INST\_REG\_SIZE\_BY\_NAME(inst, name)
    :   Get a `DT_DRV_COMPAT`’s register block size by name.

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores register specifier name

        Returns:
        :   size of the register block with the given `name`

    DT\_INST\_REG\_ADDR(inst)
    :   Get a `DT_DRV_COMPAT`’s (only) register block address.

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   instance’s register block address

    DT\_INST\_REG\_ADDR\_U64(inst)
    :   64-bit version of [DT\_INST\_REG\_ADDR()](#group__devicetree-inst_1gafde8fa67b94ac959ba2e24b44b3386a7)

        This macro version adds the appropriate suffix for 64-bit unsigned integer literals. Note that this macro is equivalent to [DT\_INST\_REG\_ADDR()](#group__devicetree-inst_1gafde8fa67b94ac959ba2e24b44b3386a7) in linker/ASM context.

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   instance’s register block address

    DT\_INST\_REG\_SIZE(inst)
    :   Get a `DT_DRV_COMPAT`’s (only) register block size.

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   instance’s register block size

    DT\_INST\_IRQ\_LEVEL(inst)
    :   Get a `DT_DRV_COMPAT` interrupt level.

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   interrupt level

    DT\_INST\_IRQ\_BY\_IDX(inst, idx, cell)
    :   Get a `DT_DRV_COMPAT` interrupt specifier value at an index.

        Parameters:
        :   - **inst** – instance number
            - **idx** – logical index into the interrupt specifier array
            - **cell** – cell name specifier

        Returns:
        :   the named value at the specifier given by the index

    DT\_INST\_IRQ\_INTC\_BY\_IDX(inst, idx)
    :   Get a `DT_DRV_COMPAT` interrupt specifier’s interrupt controller by index.

        Parameters:
        :   - **inst** – instance number
            - **idx** – interrupt specifier’s index

        Returns:
        :   node\_id of interrupt specifier’s interrupt controller

    DT\_INST\_IRQ\_INTC\_BY\_NAME(inst, name)
    :   Get a `DT_DRV_COMPAT` interrupt specifier’s interrupt controller by name.

        Parameters:
        :   - **inst** – instance number
            - **name** – interrupt specifier’s name

        Returns:
        :   node\_id of interrupt specifier’s interrupt controller

    DT\_INST\_IRQ\_INTC(inst)
    :   Get a `DT_DRV_COMPAT` interrupt specifier’s interrupt controller.

        See also

        [DT\_INST\_IRQ\_INTC\_BY\_IDX()](#group__devicetree-inst_1gab29f18e52d7475245c9fbeb4cd8e7769)

        Note

        Equivalent to [DT\_INST\_IRQ\_INTC\_BY\_IDX(node\_id, 0)](#group__devicetree-inst_1gab29f18e52d7475245c9fbeb4cd8e7769)

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   node\_id of interrupt specifier’s interrupt controller

    DT\_INST\_IRQ\_BY\_NAME(inst, name, cell)
    :   Get a `DT_DRV_COMPAT` interrupt specifier value by name.

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores interrupt specifier name
            - **cell** – cell name specifier

        Returns:
        :   the named value at the specifier given by the index

    DT\_INST\_IRQ(inst, cell)
    :   Get a `DT_DRV_COMPAT` interrupt specifier’s value.

        Parameters:
        :   - **inst** – instance number
            - **cell** – cell name specifier

        Returns:
        :   the named value at that index

    DT\_INST\_IRQN(inst)
    :   Get a `DT_DRV_COMPAT`’s (only) irq number.

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   the interrupt number for the node’s only interrupt

    DT\_INST\_IRQN\_BY\_IDX(inst, idx)
    :   Get a `DT_DRV_COMPAT`’s irq number at index.

        Parameters:
        :   - **inst** – instance number
            - **idx** – logical index into the interrupt specifier array

        Returns:
        :   the interrupt number for the node’s idx-th interrupt

    DT\_INST\_BUS(inst)
    :   Get a `DT_DRV_COMPAT`’s bus node identifier.

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   node identifier for the instance’s bus node

    DT\_INST\_ON\_BUS(inst, bus)
    :   Test if a `DT_DRV_COMPAT`’s bus type is a given type.

        Parameters:
        :   - **inst** – instance number
            - **bus** – a binding’s bus type as a C token, lowercased and without quotes

        Returns:
        :   1 if the given instance is on a bus of the given type, 0 otherwise

    DT\_INST\_STRING\_TOKEN\_OR(inst, name, default\_value)
    :   Like [DT\_INST\_STRING\_TOKEN()](#group__devicetree-inst_1ga8e8c72187ce0d47fd24e4585f3d48484), but with a fallback to `default_value`.

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores property name
            - **default\_value** – a fallback value to expand to

        Returns:
        :   if `prop` exists, its value as a token, i.e. without any quotes and with special characters converted to underscores. Othewise `default_value`

    DT\_INST\_STRING\_UPPER\_TOKEN\_OR(inst, name, default\_value)
    :   Like [DT\_INST\_STRING\_UPPER\_TOKEN()](#group__devicetree-inst_1ga0487d19ae023acb9b0eb613317f31aa5), but with a fallback to `default_value`.

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores property name
            - **default\_value** – a fallback value to expand to

        Returns:
        :   the property’s value as an uppercased token, or `default_value`

    DT\_INST\_STRING\_UNQUOTED\_OR(inst, name, default\_value)
    :   Like [DT\_INST\_STRING\_UNQUOTED()](#group__devicetree-inst_1ga1c4fc4c808113cb6e0d7b54af9869228), but with a fallback to `default_value`.

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores property name
            - **default\_value** – a fallback value to expand to

        Returns:
        :   the property’s value as a sequence of tokens, with no quotes, or `default_value`

    DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(compat, bus)

    DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY(bus)
    :   Test if any `DT_DRV_COMPAT` node is on a bus of a given type and has status okay.

        This is a special-purpose macro which can be useful when writing drivers for devices which can appear on multiple buses. One example is a sensor device which may be wired on an I2C or SPI bus.

        Example devicetree overlay:

        ```devicetree
        &i2c0 {
               temp: temperature-sensor@76 {
                        compatible = "vnd,some-sensor";
                        reg = <0x76>;
               };
        };
        ```

        Example usage, assuming `i2c0` is an I2C bus controller node, and therefore `temp` is on an I2C bus:

        ```c
        #define DT_DRV_COMPAT vnd_some_sensor

        DT_ANY_INST_ON_BUS_STATUS_OKAY(i2c) // 1
        ```

        Parameters:
        :   - **bus** – a binding’s bus type as a C token, lowercased and without quotes

        Returns:
        :   1 if any enabled node with that compatible is on that bus type, 0 otherwise

    DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY(prop)
    :   Check if any `DT_DRV_COMPAT` node with status `okay` has a given property.

        Example devicetree overlay:

        ```devicetree
        &i2c0 {
            sensor0: sensor@0 {
                compatible = "vnd,some-sensor";
                status = "okay";
                reg = <0>;
                foo = <1>;
                bar = <2>;
            };

            sensor1: sensor@1 {
                compatible = "vnd,some-sensor";
                status = "okay";
                reg = <1>;
                foo = <2>;
            };

            sensor2: sensor@2 {
                compatible = "vnd,some-sensor";
                status = "disabled";
                reg = <2>;
                baz = <1>;
            };
        };
        ```

        Example usage:

        ```c
        #define DT_DRV_COMPAT vnd_some_sensor

        DT_ANY_INST_HAS_PROP_STATUS_OKAY(foo) // 1
        DT_ANY_INST_HAS_PROP_STATUS_OKAY(bar) // 1
        DT_ANY_INST_HAS_PROP_STATUS_OKAY(baz) // 0
        ```

        Parameters:
        :   - **prop** – lowercase-and-underscores property name

    DT\_INST\_FOREACH\_STATUS\_OKAY(fn)
    :   Call `fn` on all nodes with compatible `DT_DRV_COMPAT` and status `okay`.

        This macro calls `fn(inst)` on each `inst` number that refers to a node with status `okay`. Whitespace is added between invocations.

        Example devicetree fragment:

        ```devicetree
        a {
                compatible = "vnd,device";
                status = "okay";
                foobar = "DEV_A";
        };

        b {
                compatible = "vnd,device";
                status = "okay";
                foobar = "DEV_B";
        };

        c {
                compatible = "vnd,device";
                status = "disabled";
                foobar = "DEV_C";
        };
        ```

        Example usage:

        ```c
        #define DT_DRV_COMPAT vnd_device
        #define MY_FN(inst) DT_INST_PROP(inst, foobar),

        DT_INST_FOREACH_STATUS_OKAY(MY_FN)
        ```

        This expands to:

        ```c
        MY_FN(0) MY_FN(1)
        ```

        and from there, to either this:

        ```text
        "DEV_A", "DEV_B",
        ```

        or this:

        ```text
        "DEV_B", "DEV_A",
        ```

        No guarantees are made about the order that a and b appear in the expansion.

        Note that `fn` is responsible for adding commas, semicolons, or other separators or terminators.

        Device drivers should use this macro whenever possible to instantiate a struct device for each enabled node in the devicetree of the driver’s compatible `DT_DRV_COMPAT`.

        Parameters:
        :   - **fn** – Macro to call for each enabled node. Must accept an instance number as its only parameter.

    DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS(fn, ...)
    :   Call `fn` on all nodes with compatible `DT_DRV_COMPAT` and status `okay` with multiple arguments.

        See also

        [DT\_INST\_FOREACH\_STATUS\_OKAY](#group__devicetree-inst_1gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)

        Parameters:
        :   - **fn** – Macro to call for each enabled node. Must accept an instance number as its only parameter.
            - **...** – variable number of arguments to pass to `fn`

    DT\_INST\_FOREACH\_PROP\_ELEM(inst, prop, fn)
    :   Invokes `fn` for each element of property `prop` for a `DT_DRV_COMPAT` instance.

        Equivalent to [DT\_FOREACH\_PROP\_ELEM(DT\_DRV\_INST(inst), prop, fn)](#group__devicetree-generic-foreach_1ga118a0477ab297a1bda9e16acf556babc).

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **fn** – macro to invoke

    DT\_INST\_FOREACH\_PROP\_ELEM\_SEP(inst, prop, fn, sep)
    :   Invokes `fn` for each element of property `prop` for a `DT_DRV_COMPAT` instance with a separator.

        Equivalent to [DT\_FOREACH\_PROP\_ELEM\_SEP(DT\_DRV\_INST(inst), prop, fn, sep)](#group__devicetree-generic-foreach_1ga72d0b6859b4fc61cde518aee118d9ed8).

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **fn** – macro to invoke
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.

    DT\_INST\_FOREACH\_PROP\_ELEM\_VARGS(inst, prop, fn, ...)
    :   Invokes `fn` for each element of property `prop` for a `DT_DRV_COMPAT` instance with multiple arguments.

        Equivalent to DT\_FOREACH\_PROP\_ELEM\_VARGS([DT\_DRV\_INST(inst)](#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1), prop, fn, **VA\_ARGS**)

        See also

        [DT\_INST\_FOREACH\_PROP\_ELEM](#group__devicetree-inst_1gaf163f2f85b3893ca46c87f0fcbe65255)

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **fn** – macro to invoke
            - **...** – variable number of arguments to pass to `fn`

    DT\_INST\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(inst, prop, fn, sep, ...)
    :   Invokes `fn` for each element of property `prop` for a `DT_DRV_COMPAT` instance with multiple arguments and a sepatator.

        Equivalent to DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS([DT\_DRV\_INST(inst)](#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1), prop, fn, sep, **VA\_ARGS**)

        See also

        [DT\_INST\_FOREACH\_PROP\_ELEM](#group__devicetree-inst_1gaf163f2f85b3893ca46c87f0fcbe65255)

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name
            - **fn** – macro to invoke
            - **sep** – Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator.
            - **...** – variable number of arguments to pass to fn

    DT\_INST\_NODE\_HAS\_PROP(inst, prop)
    :   Does a DT\_DRV\_COMPAT instance have a property?

        Parameters:
        :   - **inst** – instance number
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   1 if the instance has the property, 0 otherwise.

    DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX(inst, pha, idx, cell)
    :   Does a phandle array have a named cell specifier at an index for a `DT_DRV_COMPAT` instance?

        Parameters:
        :   - **inst** – instance number
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **idx** – index to check
            - **cell** – named cell value whose existence to check

        Returns:
        :   1 if the named `cell` exists in the specifier at index `idx`, 0 otherwise.

    DT\_INST\_PHA\_HAS\_CELL(inst, pha, cell)
    :   Does a phandle array have a named cell specifier at index 0 for a `DT_DRV_COMPAT` instance?

        Parameters:
        :   - **inst** – instance number
            - **pha** – lowercase-and-underscores property with type `phandle-array`
            - **cell** – named cell value whose existence to check

        Returns:
        :   1 if the named `cell` exists in the specifier at index 0, 0 otherwise.

    DT\_INST\_IRQ\_HAS\_IDX(inst, idx)
    :   is index valid for interrupt property on a `DT_DRV_COMPAT` instance?

        Parameters:
        :   - **inst** – instance number
            - **idx** – logical index into the interrupt specifier array

        Returns:
        :   1 if the `idx` is valid for the interrupt property 0 otherwise.

    DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX(inst, idx, cell)
    :   Does a `DT_DRV_COMPAT` instance have an interrupt named cell specifier?

        Parameters:
        :   - **inst** – instance number
            - **idx** – index to check
            - **cell** – named cell value whose existence to check

        Returns:
        :   1 if the named `cell` exists in the interrupt specifier at index `idx` 0 otherwise.

    DT\_INST\_IRQ\_HAS\_CELL(inst, cell)
    :   Does a `DT_DRV_COMPAT` instance have an interrupt value?

        Parameters:
        :   - **inst** – instance number
            - **cell** – named cell value whose existence to check

        Returns:
        :   1 if the named `cell` exists in the interrupt specifier at index 0 0 otherwise.

    DT\_INST\_IRQ\_HAS\_NAME(inst, name)
    :   Does a `DT_DRV_COMPAT` instance have an interrupt value?

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores interrupt specifier name

        Returns:
        :   1 if `name` is a valid named specifier

## [Hardware specific APIs](#id14)

The following APIs can also be used by including `<devicetree.h>`;
no additional include is needed.

### [CAN](#id15)

These conveniences may be used for nodes which describe CAN
controllers/transceivers, and properties related to them.

*group* devicetree-can
:   Defines

    DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE(node\_id, max)
    :   Get the maximum transceiver bitrate for a CAN controller.

        The bitrate will be limited to the maximum bitrate supported by the CAN controller. If no CAN transceiver is present in the devicetree, the maximum bitrate will be that of the CAN controller.

        Example devicetree fragment:

        ```text
        transceiver0: can-phy0 {
                compatible = "vnd,can-transceiver";
                max-bitrate = <1000000>;
                #phy-cells = <0>;
        };

        can0: can@... {
                compatible = "vnd,can-controller";
                phys = <&transceiver0>;
        };

        can1: can@... {
                compatible = "vnd,can-controller";

                can-transceiver {
                        max-bitrate = <2000000>;
                };
        };
        ```

        Example usage:

        ```text
        DT_CAN_TRANSCEIVER_MAX_BITRATE(DT_NODELABEL(can0), 5000000) // 1000000
        DT_CAN_TRANSCEIVER_MAX_BITRATE(DT_NODELABEL(can1), 5000000) // 2000000
        DT_CAN_TRANSCEIVER_MAX_BITRATE(DT_NODELABEL(can1), 1000000) // 1000000
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **max** – maximum bitrate supported by the CAN controller

        Returns:
        :   the maximum bitrate supported by the CAN controller/transceiver combination

    DT\_INST\_CAN\_TRANSCEIVER\_MAX\_BITRATE(inst, max)
    :   Get the maximum transceiver bitrate for a DT\_DRV\_COMPAT CAN controller.

        See also

        [DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE()](#group__devicetree-can_1ga9c56ded2142fbd8a4a7facffd3dd549d)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **max** – maximum bitrate supported by the CAN controller

        Returns:
        :   the maximum bitrate supported by the CAN controller/transceiver combination

### [Clocks](#id16)

These conveniences may be used for nodes which describe clock sources, and
properties related to them.

*group* devicetree-clocks
:   Defines

    DT\_CLOCKS\_HAS\_IDX(node\_id, idx)
    :   Test if a node has a clocks phandle-array property at a given index.

        This expands to 1 if the given index is valid clocks property phandle-array index. Otherwise, it expands to 0.

        Example devicetree fragment:

        ```text
        n1: node-1 {
                clocks = <...>, <...>;
        };

        n2: node-2 {
                clocks = <...>;
        };
        ```

        Example usage:

        ```text
        DT_CLOCKS_HAS_IDX(DT_NODELABEL(n1), 0) // 1
        DT_CLOCKS_HAS_IDX(DT_NODELABEL(n1), 1) // 1
        DT_CLOCKS_HAS_IDX(DT_NODELABEL(n1), 2) // 0
        DT_CLOCKS_HAS_IDX(DT_NODELABEL(n2), 1) // 0
        ```

        Parameters:
        :   - **node\_id** – node identifier; may or may not have any clocks property
            - **idx** – index of a clocks property phandle-array whose existence to check

        Returns:
        :   1 if the index exists, 0 otherwise

    DT\_CLOCKS\_HAS\_NAME(node\_id, name)
    :   Test if a node has a clock-names array property holds a given name.

        This expands to 1 if the name is available as clocks-name array property cell. Otherwise, it expands to 0.

        Example devicetree fragment:

        ```text
        n1: node-1 {
                clocks = <...>, <...>;
                clock-names = "alpha", "beta";
        };

        n2: node-2 {
                clocks = <...>;
                clock-names = "alpha";
        };
        ```

        Example usage:

        ```text
        DT_CLOCKS_HAS_NAME(DT_NODELABEL(n1), alpha) // 1
        DT_CLOCKS_HAS_NAME(DT_NODELABEL(n1), beta)  // 1
        DT_CLOCKS_HAS_NAME(DT_NODELABEL(n2), beta)  // 0
        ```

        Parameters:
        :   - **node\_id** – node identifier; may or may not have any clock-names property.
            - **name** – lowercase-and-underscores clock-names cell value name to check

        Returns:
        :   1 if the clock name exists, 0 otherwise

    DT\_NUM\_CLOCKS(node\_id)
    :   Get the number of elements in a clocks property.

        Example devicetree fragment:

        ```text
        n1: node-1 {
                clocks = <&foo>, <&bar>;
        };

        n2: node-2 {
                clocks = <&foo>;
        };
        ```

        Example usage:

        ```text
        DT_NUM_CLOCKS(DT_NODELABEL(n1)) // 2
        DT_NUM_CLOCKS(DT_NODELABEL(n2)) // 1
        ```

        Parameters:
        :   - **node\_id** – node identifier with a clocks property

        Returns:
        :   number of elements in the property

    DT\_CLOCKS\_CTLR\_BY\_IDX(node\_id, idx)
    :   Get the node identifier for the controller phandle from a “clocks” phandle-array property at an index.

        Example devicetree fragment:

        ```text
        clk1: clock-controller@... { ... };

        clk2: clock-controller@... { ... };

        n: node {
                clocks = <&clk1 10 20>, <&clk2 30 40>;
        };
        ```

        Example usage:

        ```text
        DT_CLOCKS_CTLR_BY_IDX(DT_NODELABEL(n), 0)) // DT_NODELABEL(clk1)
        DT_CLOCKS_CTLR_BY_IDX(DT_NODELABEL(n), 1)) // DT_NODELABEL(clk2)
        ```

        See also

        [DT\_PHANDLE\_BY\_IDX()](#group__devicetree-generic-prop_1ga8ff163c240878a988d29d727671671de)

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – logical index into “clocks”

        Returns:
        :   the node identifier for the clock controller referenced at index “idx”

    DT\_CLOCKS\_CTLR(node\_id)
    :   Equivalent to [DT\_CLOCKS\_CTLR\_BY\_IDX(node\_id, 0)](#group__devicetree-clocks_1gab36c92fc26c3517031bce342148308c3).

        See also

        [DT\_CLOCKS\_CTLR\_BY\_IDX()](#group__devicetree-clocks_1gab36c92fc26c3517031bce342148308c3)

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   a node identifier for the clocks controller at index 0 in “clocks”

    DT\_CLOCKS\_CTLR\_BY\_NAME(node\_id, name)
    :   Get the node identifier for the controller phandle from a clocks phandle-array property by name.

        Example devicetree fragment:

        ```text
        clk1: clock-controller@... { ... };

        clk2: clock-controller@... { ... };

        n: node {
                clocks = <&clk1 10 20>, <&clk2 30 40>;
                clock-names = "alpha", "beta";
        };
        ```

        Example usage:

        ```text
        DT_CLOCKS_CTLR_BY_NAME(DT_NODELABEL(n), beta) // DT_NODELABEL(clk2)
        ```

        See also

        [DT\_PHANDLE\_BY\_NAME()](#group__devicetree-generic-prop_1ga65c90d2d96255b8569c5b869b637c2fd)

        Parameters:
        :   - **node\_id** – node identifier
            - **name** – lowercase-and-underscores name of a clocks element as defined by the node’s clock-names property

        Returns:
        :   the node identifier for the clock controller referenced by name

    DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, idx, cell)
    :   Get a clock specifier’s cell value at an index.

        Example devicetree fragment:

        ```text
        clk1: clock-controller@... {
                compatible = "vnd,clock";
                #clock-cells = < 2 >;
        };

        n: node {
                clocks = < &clk1 10 20 >, < &clk1 30 40 >;
        };
        ```

        Bindings fragment for the vnd,clock compatible:

        ```text
        clock-cells:
          - bus
          - bits
        ```

        Example usage:

        ```text
        DT_CLOCKS_CELL_BY_IDX(DT_NODELABEL(n), 0, bus) // 10
        DT_CLOCKS_CELL_BY_IDX(DT_NODELABEL(n), 1, bits) // 40
        ```

        See also

        [DT\_PHA\_BY\_IDX()](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed)

        Parameters:
        :   - **node\_id** – node identifier for a node with a clocks property
            - **idx** – logical index into clocks property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value at index “idx”

    DT\_CLOCKS\_CELL\_BY\_NAME(node\_id, name, cell)
    :   Get a clock specifier’s cell value by name.

        Example devicetree fragment:

        ```text
        clk1: clock-controller@... {
                compatible = "vnd,clock";
                #clock-cells = < 2 >;
        };

        n: node {
                clocks = < &clk1 10 20 >, < &clk1 30 40 >;
                clock-names = "alpha", "beta";
        };
        ```

        Bindings fragment for the vnd,clock compatible:

        ```text
        clock-cells:
          - bus
          - bits
        ```

        Example usage:

        ```text
        DT_CLOCKS_CELL_BY_NAME(DT_NODELABEL(n), alpha, bus) // 10
        DT_CLOCKS_CELL_BY_NAME(DT_NODELABEL(n), beta, bits) // 40
        ```

        See also

        [DT\_PHA\_BY\_NAME()](#group__devicetree-generic-prop_1gae469615356a867c49416da15bdc44a26)

        Parameters:
        :   - **node\_id** – node identifier for a node with a clocks property
            - **name** – lowercase-and-underscores name of a clocks element as defined by the node’s clock-names property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value in the specifier at the named element

    DT\_CLOCKS\_CELL(node\_id, cell)
    :   Equivalent to [DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, 0, cell)](#group__devicetree-clocks_1ga7db765e869b8455a6c56a8f22a7cc5c8).

        See also

        [DT\_CLOCKS\_CELL\_BY\_IDX()](#group__devicetree-clocks_1ga7db765e869b8455a6c56a8f22a7cc5c8)

        Parameters:
        :   - **node\_id** – node identifier for a node with a clocks property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value at index 0

    DT\_INST\_CLOCKS\_HAS\_IDX(inst, idx)
    :   Equivalent to [DT\_CLOCKS\_HAS\_IDX(DT\_DRV\_INST(inst), idx)](#group__devicetree-clocks_1gabfdf51e2b14c05e84366cff1bb056da0).

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number; may or may not have any clocks property
            - **idx** – index of a clocks property phandle-array whose existence to check

        Returns:
        :   1 if the index exists, 0 otherwise

    DT\_INST\_CLOCKS\_HAS\_NAME(inst, name)
    :   Equivalent to DT\_CLOCK\_HAS\_NAME(DT\_DRV\_INST(inst), name).

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number; may or may not have any clock-names property.
            - **name** – lowercase-and-underscores clock-names cell value name to check

        Returns:
        :   1 if the clock name exists, 0 otherwise

    DT\_INST\_NUM\_CLOCKS(inst)
    :   Equivalent to [DT\_NUM\_CLOCKS(DT\_DRV\_INST(inst))](#group__devicetree-clocks_1ga22d4e8621b5bf56ed0ac8295dd11d7e3).

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   number of elements in the clocks property

    DT\_INST\_CLOCKS\_CTLR\_BY\_IDX(inst, idx)
    :   Get the node identifier for the controller phandle from a “clocks” phandle-array property at an index.

        See also

        [DT\_CLOCKS\_CTLR\_BY\_IDX()](#group__devicetree-clocks_1gab36c92fc26c3517031bce342148308c3)

        Parameters:
        :   - **inst** – instance number
            - **idx** – logical index into “clocks”

        Returns:
        :   the node identifier for the clock controller referenced at index “idx”

    DT\_INST\_CLOCKS\_CTLR(inst)
    :   Equivalent to [DT\_INST\_CLOCKS\_CTLR\_BY\_IDX(inst, 0)](#group__devicetree-clocks_1gac4a7a89937eae57960a2091d7edc5fd3).

        See also

        [DT\_CLOCKS\_CTLR()](#group__devicetree-clocks_1ga69795ece1f4a46e2c26a8e2dbb452f23)

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   a node identifier for the clocks controller at index 0 in “clocks”

    DT\_INST\_CLOCKS\_CTLR\_BY\_NAME(inst, name)
    :   Get the node identifier for the controller phandle from a clocks phandle-array property by name.

        See also

        [DT\_CLOCKS\_CTLR\_BY\_NAME()](#group__devicetree-clocks_1gaf4c92378a2599ee7024f914ea3584404)

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores name of a clocks element as defined by the node’s clock-names property

        Returns:
        :   the node identifier for the clock controller referenced by the named element

    DT\_INST\_CLOCKS\_CELL\_BY\_IDX(inst, idx, cell)
    :   Get a DT\_DRV\_COMPAT instance’s clock specifier’s cell value at an index.

        See also

        [DT\_CLOCKS\_CELL\_BY\_IDX()](#group__devicetree-clocks_1ga7db765e869b8455a6c56a8f22a7cc5c8)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into clocks property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value at index “idx”

    DT\_INST\_CLOCKS\_CELL\_BY\_NAME(inst, name, cell)
    :   Get a DT\_DRV\_COMPAT instance’s clock specifier’s cell value by name.

        See also

        [DT\_CLOCKS\_CELL\_BY\_NAME()](#group__devicetree-clocks_1gaca32bfb478ac92e6a760ad0761328d5a)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of a clocks element as defined by the node’s clock-names property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value in the specifier at the named element

    DT\_INST\_CLOCKS\_CELL(inst, cell)
    :   Equivalent to [DT\_INST\_CLOCKS\_CELL\_BY\_IDX(inst, 0, cell)](#group__devicetree-clocks_1ga5bee2e489f0818f0f2d1ec6d195bd3a8).

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the value of the cell inside the specifier at index 0

### [DMA](#id17)

These conveniences may be used for nodes which describe direct memory access
controllers or channels, and properties related to them.

*group* devicetree-dmas
:   Defines

    DT\_DMAS\_CTLR\_BY\_IDX(node\_id, idx)
    :   Get the node identifier for the DMA controller from a dmas property at an index.

        Example devicetree fragment:

        ```text
        dma1: dma@... { ... };

        dma2: dma@... { ... };

        n: node {
            dmas = <&dma1 1 2 0x400 0x3>,
                    <&dma2 6 3 0x404 0x5>;
        };
        ```

        Example usage:

        ```text
        DT_DMAS_CTLR_BY_IDX(DT_NODELABEL(n), 0) // DT_NODELABEL(dma1)
        DT_DMAS_CTLR_BY_IDX(DT_NODELABEL(n), 1) // DT_NODELABEL(dma2)
        ```

        See also

        [DT\_PROP\_BY\_PHANDLE\_IDX()](#group__devicetree-generic-prop_1gaeba973992914d493cff5506ecf86a00d)

        Parameters:
        :   - **node\_id** – node identifier for a node with a dmas property
            - **idx** – logical index into dmas property

        Returns:
        :   the node identifier for the DMA controller referenced at index “idx”

    DT\_DMAS\_CTLR\_BY\_NAME(node\_id, name)
    :   Get the node identifier for the DMA controller from a dmas property by name.

        Example devicetree fragment:

        ```text
        dma1: dma@... { ... };

        dma2: dma@... { ... };

        n: node {
            dmas = <&dma1 1 2 0x400 0x3>,
                    <&dma2 6 3 0x404 0x5>;
            dma-names = "tx", "rx";
        };
        ```

        Example usage:

        ```text
        DT_DMAS_CTLR_BY_NAME(DT_NODELABEL(n), tx) // DT_NODELABEL(dma1)
        DT_DMAS_CTLR_BY_NAME(DT_NODELABEL(n), rx) // DT_NODELABEL(dma2)
        ```

        See also

        [DT\_PHANDLE\_BY\_NAME()](#group__devicetree-generic-prop_1ga65c90d2d96255b8569c5b869b637c2fd)

        Parameters:
        :   - **node\_id** – node identifier for a node with a dmas property
            - **name** – lowercase-and-underscores name of a dmas element as defined by the node’s dma-names property

        Returns:
        :   the node identifier for the DMA controller in the named element

    DT\_DMAS\_CTLR(node\_id)
    :   Equivalent to [DT\_DMAS\_CTLR\_BY\_IDX(node\_id, 0)](#group__devicetree-dmas_1gac74e56d90f8abe4bb0b53acddb618a3a).

        See also

        [DT\_DMAS\_CTLR\_BY\_IDX()](#group__devicetree-dmas_1gac74e56d90f8abe4bb0b53acddb618a3a)

        Parameters:
        :   - **node\_id** – node identifier for a node with a dmas property

        Returns:
        :   the node identifier for the DMA controller at index 0 in the node’s “dmas” property

    DT\_INST\_DMAS\_CTLR\_BY\_IDX(inst, idx)
    :   Get the node identifier for the DMA controller from a DT\_DRV\_COMPAT instance’s dmas property at an index.

        See also

        [DT\_DMAS\_CTLR\_BY\_IDX()](#group__devicetree-dmas_1gac74e56d90f8abe4bb0b53acddb618a3a)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into dmas property

        Returns:
        :   the node identifier for the DMA controller referenced at index “idx”

    DT\_INST\_DMAS\_CTLR\_BY\_NAME(inst, name)
    :   Get the node identifier for the DMA controller from a DT\_DRV\_COMPAT instance’s dmas property by name.

        See also

        [DT\_DMAS\_CTLR\_BY\_NAME()](#group__devicetree-dmas_1ga8c148fc826dee34f5e4601f4a7aa9f55)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of a dmas element as defined by the node’s dma-names property

        Returns:
        :   the node identifier for the DMA controller in the named element

    DT\_INST\_DMAS\_CTLR(inst)
    :   Equivalent to [DT\_INST\_DMAS\_CTLR\_BY\_IDX(inst, 0)](#group__devicetree-dmas_1ga5dbb1f22a0098a3493fd6f4cef9985a9).

        See also

        [DT\_DMAS\_CTLR\_BY\_IDX()](#group__devicetree-dmas_1gac74e56d90f8abe4bb0b53acddb618a3a)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   the node identifier for the DMA controller at index 0 in the instance’s “dmas” property

    DT\_DMAS\_CELL\_BY\_IDX(node\_id, idx, cell)
    :   Get a DMA specifier’s cell value at an index.

        Example devicetree fragment:

        ```text
        dma1: dma@... {
                compatible = "vnd,dma";
                #dma-cells = <2>;
        };

        dma2: dma@... {
                compatible = "vnd,dma";
                #dma-cells = <2>;
        };

        n: node {
            dmas = <&dma1 1 0x400>,
                   <&dma2 6 0x404>;
        };
        ```

        Bindings fragment for the vnd,dma compatible:

        ```text
        dma-cells:
          - channel
          - config
        ```

        Example usage:

        ```text
        DT_DMAS_CELL_BY_IDX(DT_NODELABEL(n), 0, channel) // 1
        DT_DMAS_CELL_BY_IDX(DT_NODELABEL(n), 1, channel) // 6
        DT_DMAS_CELL_BY_IDX(DT_NODELABEL(n), 0, config) // 0x400
        DT_DMAS_CELL_BY_IDX(DT_NODELABEL(n), 1, config) // 0x404
        ```

        See also

        [DT\_PHA\_BY\_IDX()](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed)

        Parameters:
        :   - **node\_id** – node identifier for a node with a dmas property
            - **idx** – logical index into dmas property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value at index “idx”

    DT\_INST\_DMAS\_CELL\_BY\_IDX(inst, idx, cell)
    :   Get a DT\_DRV\_COMPAT instance’s DMA specifier’s cell value at an index.

        See also

        [DT\_DMAS\_CELL\_BY\_IDX()](#group__devicetree-dmas_1ga8aff7a91d19482964b8b56cb558c1b59)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into dmas property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value at index “idx”

    DT\_DMAS\_CELL\_BY\_NAME(node\_id, name, cell)
    :   Get a DMA specifier’s cell value by name.

        Example devicetree fragment:

        ```text
        dma1: dma@... {
                compatible = "vnd,dma";
                #dma-cells = <2>;
        };

        dma2: dma@... {
                compatible = "vnd,dma";
                #dma-cells = <2>;
        };

        n: node {
            dmas = <&dma1 1 0x400>,
                   <&dma2 6 0x404>;
            dma-names = "tx", "rx";
        };
        ```

        Bindings fragment for the vnd,dma compatible:

        ```text
        dma-cells:
          - channel
          - config
        ```

        Example usage:

        ```text
        DT_DMAS_CELL_BY_NAME(DT_NODELABEL(n), tx, channel) // 1
        DT_DMAS_CELL_BY_NAME(DT_NODELABEL(n), rx, channel) // 6
        DT_DMAS_CELL_BY_NAME(DT_NODELABEL(n), tx, config) // 0x400
        DT_DMAS_CELL_BY_NAME(DT_NODELABEL(n), rx, config) // 0x404
        ```

        See also

        [DT\_PHA\_BY\_NAME()](#group__devicetree-generic-prop_1gae469615356a867c49416da15bdc44a26)

        Parameters:
        :   - **node\_id** – node identifier for a node with a dmas property
            - **name** – lowercase-and-underscores name of a dmas element as defined by the node’s dma-names property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value in the specifier at the named element

    DT\_INST\_DMAS\_CELL\_BY\_NAME(inst, name, cell)
    :   Get a DT\_DRV\_COMPAT instance’s DMA specifier’s cell value by name.

        See also

        [DT\_DMAS\_CELL\_BY\_NAME()](#group__devicetree-dmas_1ga1b80ae7fee6bcc9aa2ad03435e70dd14)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of a dmas element as defined by the node’s dma-names property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value in the specifier at the named element

    DT\_DMAS\_HAS\_IDX(node\_id, idx)
    :   Is index “idx” valid for a dmas property?

        Parameters:
        :   - **node\_id** – node identifier for a node with a dmas property
            - **idx** – logical index into dmas property

        Returns:
        :   1 if the “dmas” property has index “idx”, 0 otherwise

    DT\_INST\_DMAS\_HAS\_IDX(inst, idx)
    :   Is index “idx” valid for a DT\_DRV\_COMPAT instance’s dmas property?

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into dmas property

        Returns:
        :   1 if the “dmas” property has a specifier at index “idx”, 0 otherwise

    DT\_DMAS\_HAS\_NAME(node\_id, name)
    :   Does a dmas property have a named element?

        Parameters:
        :   - **node\_id** – node identifier for a node with a dmas property
            - **name** – lowercase-and-underscores name of a dmas element as defined by the node’s dma-names property

        Returns:
        :   1 if the dmas property has the named element, 0 otherwise

    DT\_INST\_DMAS\_HAS\_NAME(inst, name)
    :   Does a DT\_DRV\_COMPAT instance’s dmas property have a named element?

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of a dmas element as defined by the node’s dma-names property

        Returns:
        :   1 if the dmas property has the named element, 0 otherwise

### [Fixed flash partitions](#id18)

These conveniences may be used for the special-purpose `fixed-partitions`
compatible used to encode information about flash memory partitions in the
device tree. See See `fixed-partition` for more details.

*group* devicetree-fixed-partition
:   Defines

    DT\_NODE\_BY\_FIXED\_PARTITION\_LABEL(label)
    :   Get a node identifier for a fixed partition with a given label property.

        Example devicetree fragment:

        ```text
        flash@... {
                 partitions {
                         compatible = "fixed-partitions";
                         boot_partition: partition@0 {
                                 label = "mcuboot";
                         };
                         slot0_partition: partition@c000 {
                                 label = "image-0";
                         };
                         ...
                 };
        };
        ```

        Example usage:

        ```text
        DT_NODE_BY_FIXED_PARTITION_LABEL(mcuboot) // node identifier for boot_partition
        DT_NODE_BY_FIXED_PARTITION_LABEL(image_0) // node identifier for slot0_partition
        ```

        Parameters:
        :   - **label** – lowercase-and-underscores label property value

        Returns:
        :   a node identifier for the partition with that label property

    DT\_HAS\_FIXED\_PARTITION\_LABEL(label)
    :   Test if a fixed partition with a given label property exists.

        Parameters:
        :   - **label** – lowercase-and-underscores label property value

        Returns:
        :   1 if any “fixed-partitions” child node has the given label, 0 otherwise.

    DT\_FIXED\_PARTITION\_EXISTS(node\_id)
    :   Test if fixed-partition compatible node exists.

        Parameters:
        :   - **node\_id** – DTS node to test

        Returns:
        :   1 if node exists and is fixed-partition compatible, 0 otherwise.

    DT\_FIXED\_PARTITION\_ID(node\_id)
    :   Get a numeric identifier for a fixed partition.

        Parameters:
        :   - **node\_id** – node identifier for a fixed-partitions child node

        Returns:
        :   the partition’s ID, a unique zero-based index number

    DT\_MEM\_FROM\_FIXED\_PARTITION(node\_id)
    :   Get the node identifier of the flash memory for a partition.

        Parameters:
        :   - **node\_id** – node identifier for a fixed-partitions child node

        Returns:
        :   the node identifier of the internal memory that contains the fixed-partitions node, or [DT\_INVALID\_NODE](#group__devicetree-generic-id_1ga710cc4455dd7e738f43f750153163855) if it doesn’t exist.

    DT\_MTD\_FROM\_FIXED\_PARTITION(node\_id)
    :   Get the node identifier of the flash controller for a partition.

        Parameters:
        :   - **node\_id** – node identifier for a fixed-partitions child node

        Returns:
        :   the node identifier of the memory technology device that contains the fixed-partitions node.

    DT\_FIXED\_PARTITION\_ADDR(node\_id)
    :   Get the absolute address of a fixed partition.

        Example devicetree fragment:

        ```text
        &flash_controller {
                flash@1000000 {
                        compatible = "soc-nv-flash";
                        partitions {
                                compatible = "fixed-partitions";
                                storage_partition: partition@3a000 {
                                        label = "storage";
                                };
                        };
                };
        };
        ```

        Here, the “storage” partition is seen to belong to flash memory starting at address 0x1000000. The partition’s unit address of 0x3a000 represents an offset inside that flash memory.

        Example usage:

        ```text
        DT_FIXED_PARTITION_ADDR(DT_NODELABEL(storage_partition)) // 0x103a000
        ```

        This macro can only be used with partitions of internal memory addressable by the CPU. Otherwise, it may produce a compile-time error, such as: `'__REG_IDX_0_VAL_ADDRESS' undeclared`.

        Parameters:
        :   - **node\_id** – node identifier for a fixed-partitions child node

        Returns:
        :   the partition’s offset plus the base address of the flash node containing it.

### [GPIO](#id19)

These conveniences may be used for nodes which describe GPIO controllers/pins,
and properties related to them.

*group* devicetree-gpio
:   Defines

    DT\_GPIO\_CTLR\_BY\_IDX(node\_id, gpio\_pha, idx)
    :   Get the node identifier for the controller phandle from a gpio phandle-array property at an index.

        Example devicetree fragment:

        ```text
        gpio1: gpio@... { };

        gpio2: gpio@... { };

        n: node {
                gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                        <&gpio2 30 GPIO_ACTIVE_HIGH>;
        };
        ```

        Example usage:

        ```text
        DT_GPIO_CTLR_BY_IDX(DT_NODELABEL(n), gpios, 1) // DT_NODELABEL(gpio2)
        ```

        See also

        [DT\_PHANDLE\_BY\_IDX()](#group__devicetree-generic-prop_1ga8ff163c240878a988d29d727671671de)

        Parameters:
        :   - **node\_id** – node identifier
            - **gpio\_pha** – lowercase-and-underscores GPIO property with type “phandle-array”
            - **idx** – logical index into “gpio\_pha”

        Returns:
        :   the node identifier for the gpio controller referenced at index “idx”

    DT\_GPIO\_CTLR(node\_id, gpio\_pha)
    :   Equivalent to [DT\_GPIO\_CTLR\_BY\_IDX(node\_id, gpio\_pha, 0)](#group__devicetree-gpio_1ga97bd46d2ab88d392a3f336f4d23184eb).

        See also

        [DT\_GPIO\_CTLR\_BY\_IDX()](#group__devicetree-gpio_1ga97bd46d2ab88d392a3f336f4d23184eb)

        Parameters:
        :   - **node\_id** – node identifier
            - **gpio\_pha** – lowercase-and-underscores GPIO property with type “phandle-array”

        Returns:
        :   a node identifier for the gpio controller at index 0 in “gpio\_pha”

    DT\_GPIO\_PIN\_BY\_IDX(node\_id, gpio\_pha, idx)
    :   Get a GPIO specifier’s pin cell at an index.

        This macro only works for GPIO specifiers with cells named “pin”. Refer to the node’s binding to check if necessary.

        Example devicetree fragment:

        ```text
        gpio1: gpio@... {
                compatible = "vnd,gpio";
                #gpio-cells = <2>;
        };

        gpio2: gpio@... {
                compatible = "vnd,gpio";
                #gpio-cells = <2>;
        };

        n: node {
                gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                        <&gpio2 30 GPIO_ACTIVE_HIGH>;
        };
        ```

        Bindings fragment for the vnd,gpio compatible:

        ```text
        gpio-cells:
          - pin
          - flags
        ```

        Example usage:

        ```text
        DT_GPIO_PIN_BY_IDX(DT_NODELABEL(n), gpios, 0) // 10
        DT_GPIO_PIN_BY_IDX(DT_NODELABEL(n), gpios, 1) // 30
        ```

        See also

        [DT\_PHA\_BY\_IDX()](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed)

        Parameters:
        :   - **node\_id** – node identifier
            - **gpio\_pha** – lowercase-and-underscores GPIO property with type “phandle-array”
            - **idx** – logical index into “gpio\_pha”

        Returns:
        :   the pin cell value at index “idx”

    DT\_GPIO\_PIN(node\_id, gpio\_pha)
    :   Equivalent to [DT\_GPIO\_PIN\_BY\_IDX(node\_id, gpio\_pha, 0)](#group__devicetree-gpio_1ga8f7d82567056266bab1603865f8b27af).

        See also

        [DT\_GPIO\_PIN\_BY\_IDX()](#group__devicetree-gpio_1ga8f7d82567056266bab1603865f8b27af)

        Parameters:
        :   - **node\_id** – node identifier
            - **gpio\_pha** – lowercase-and-underscores GPIO property with type “phandle-array”

        Returns:
        :   the pin cell value at index 0

    DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, gpio\_pha, idx)
    :   Get a GPIO specifier’s flags cell at an index.

        This macro expects GPIO specifiers with cells named “flags”. If there is no “flags” cell in the GPIO specifier, zero is returned. Refer to the node’s binding to check specifier cell names if necessary.

        Example devicetree fragment:

        ```text
        gpio1: gpio@... {
                compatible = "vnd,gpio";
                #gpio-cells = <2>;
        };

        gpio2: gpio@... {
                compatible = "vnd,gpio";
                #gpio-cells = <2>;
        };

        n: node {
                gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                        <&gpio2 30 GPIO_ACTIVE_HIGH>;
        };
        ```

        Bindings fragment for the vnd,gpio compatible:

        ```text
        gpio-cells:
          - pin
          - flags
        ```

        Example usage:

        ```text
        DT_GPIO_FLAGS_BY_IDX(DT_NODELABEL(n), gpios, 0) // GPIO_ACTIVE_LOW
        DT_GPIO_FLAGS_BY_IDX(DT_NODELABEL(n), gpios, 1) // GPIO_ACTIVE_HIGH
        ```

        See also

        [DT\_PHA\_BY\_IDX()](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed)

        Parameters:
        :   - **node\_id** – node identifier
            - **gpio\_pha** – lowercase-and-underscores GPIO property with type “phandle-array”
            - **idx** – logical index into “gpio\_pha”

        Returns:
        :   the flags cell value at index “idx”, or zero if there is none

    DT\_GPIO\_FLAGS(node\_id, gpio\_pha)
    :   Equivalent to [DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, gpio\_pha, 0)](#group__devicetree-gpio_1ga672b2597b99194b8cbd42b3f3401d2b5).

        See also

        [DT\_GPIO\_FLAGS\_BY\_IDX()](#group__devicetree-gpio_1ga672b2597b99194b8cbd42b3f3401d2b5)

        Parameters:
        :   - **node\_id** – node identifier
            - **gpio\_pha** – lowercase-and-underscores GPIO property with type “phandle-array”

        Returns:
        :   the flags cell value at index 0, or zero if there is none

    DT\_NUM\_GPIO\_HOGS(node\_id)
    :   Get the number of GPIO hogs in a node.

        This expands to the number of hogged GPIOs, or zero if there are none.

        Example devicetree fragment:

        ```text
        gpio1: gpio@... {
          compatible = "vnd,gpio";
          #gpio-cells = <2>;

          n1: node-1 {
                  gpio-hog;
                  gpios = <0 GPIO_ACTIVE_HIGH>, <1 GPIO_ACTIVE_LOW>;
                  output-high;
          };

          n2: node-2 {
                  gpio-hog;
                  gpios = <3 GPIO_ACTIVE_HIGH>;
                  output-low;
          };
        };
        ```

        Bindings fragment for the vnd,gpio compatible:

        ```text
        gpio-cells:
          - pin
          - flags
        ```

        Example usage:

        ```text
        DT_NUM_GPIO_HOGS(DT_NODELABEL(n1)) // 2
        DT_NUM_GPIO_HOGS(DT_NODELABEL(n2)) // 1
        ```

        Parameters:
        :   - **node\_id** – node identifier; may or may not be a GPIO hog node.

        Returns:
        :   number of hogged GPIOs in the node

    DT\_GPIO\_HOG\_PIN\_BY\_IDX(node\_id, idx)
    :   Get a GPIO hog specifier’s pin cell at an index.

        This macro only works for GPIO specifiers with cells named “pin”. Refer to the node’s binding to check if necessary.

        Example devicetree fragment:

        ```text
        gpio1: gpio@... {
          compatible = "vnd,gpio";
          #gpio-cells = <2>;

          n1: node-1 {
                  gpio-hog;
                  gpios = <0 GPIO_ACTIVE_HIGH>, <1 GPIO_ACTIVE_LOW>;
                  output-high;
          };

          n2: node-2 {
                  gpio-hog;
                  gpios = <3 GPIO_ACTIVE_HIGH>;
                  output-low;
          };
        };
        ```

        Bindings fragment for the vnd,gpio compatible:

        ```text
        gpio-cells:
          - pin
          - flags
        ```

        Example usage:

        ```text
        DT_GPIO_HOG_PIN_BY_IDX(DT_NODELABEL(n1), 0) // 0
        DT_GPIO_HOG_PIN_BY_IDX(DT_NODELABEL(n1), 1) // 1
        DT_GPIO_HOG_PIN_BY_IDX(DT_NODELABEL(n2), 0) // 3
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – logical index into “gpios”

        Returns:
        :   the pin cell value at index “idx”

    DT\_GPIO\_HOG\_FLAGS\_BY\_IDX(node\_id, idx)
    :   Get a GPIO hog specifier’s flags cell at an index.

        This macro expects GPIO specifiers with cells named “flags”. If there is no “flags” cell in the GPIO specifier, zero is returned. Refer to the node’s binding to check specifier cell names if necessary.

        Example devicetree fragment:

        ```text
        gpio1: gpio@... {
          compatible = "vnd,gpio";
          #gpio-cells = <2>;

          n1: node-1 {
                  gpio-hog;
                  gpios = <0 GPIO_ACTIVE_HIGH>, <1 GPIO_ACTIVE_LOW>;
                  output-high;
          };

          n2: node-2 {
                  gpio-hog;
                  gpios = <3 GPIO_ACTIVE_HIGH>;
                  output-low;
          };
        };
        ```

        Bindings fragment for the vnd,gpio compatible:

        ```text
        gpio-cells:
          - pin
          - flags
        ```

        Example usage:

        ```text
        DT_GPIO_HOG_FLAGS_BY_IDX(DT_NODELABEL(n1), 0) // GPIO_ACTIVE_HIGH
        DT_GPIO_HOG_FLAGS_BY_IDX(DT_NODELABEL(n1), 1) // GPIO_ACTIVE_LOW
        DT_GPIO_HOG_FLAGS_BY_IDX(DT_NODELABEL(n2), 0) // GPIO_ACTIVE_HIGH
        ```

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – logical index into “gpios”

        Returns:
        :   the flags cell value at index “idx”, or zero if there is none

    DT\_INST\_GPIO\_PIN\_BY\_IDX(inst, gpio\_pha, idx)
    :   Get a DT\_DRV\_COMPAT instance’s GPIO specifier’s pin cell value at an index.

        See also

        [DT\_GPIO\_PIN\_BY\_IDX()](#group__devicetree-gpio_1ga8f7d82567056266bab1603865f8b27af)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **gpio\_pha** – lowercase-and-underscores GPIO property with type “phandle-array”
            - **idx** – logical index into “gpio\_pha”

        Returns:
        :   the pin cell value at index “idx”

    DT\_INST\_GPIO\_PIN(inst, gpio\_pha)
    :   Equivalent to [DT\_INST\_GPIO\_PIN\_BY\_IDX(inst, gpio\_pha, 0)](#group__devicetree-gpio_1ga162bca126f7015816286358f09bde6ff).

        See also

        [DT\_INST\_GPIO\_PIN\_BY\_IDX()](#group__devicetree-gpio_1ga162bca126f7015816286358f09bde6ff)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **gpio\_pha** – lowercase-and-underscores GPIO property with type “phandle-array”

        Returns:
        :   the pin cell value at index 0

    DT\_INST\_GPIO\_FLAGS\_BY\_IDX(inst, gpio\_pha, idx)
    :   Get a DT\_DRV\_COMPAT instance’s GPIO specifier’s flags cell at an index.

        See also

        [DT\_GPIO\_FLAGS\_BY\_IDX()](#group__devicetree-gpio_1ga672b2597b99194b8cbd42b3f3401d2b5)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **gpio\_pha** – lowercase-and-underscores GPIO property with type “phandle-array”
            - **idx** – logical index into “gpio\_pha”

        Returns:
        :   the flags cell value at index “idx”, or zero if there is none

    DT\_INST\_GPIO\_FLAGS(inst, gpio\_pha)
    :   Equivalent to [DT\_INST\_GPIO\_FLAGS\_BY\_IDX(inst, gpio\_pha, 0)](#group__devicetree-gpio_1gafd40d1eec5c1672b7675ae47388c1cef).

        See also

        [DT\_INST\_GPIO\_FLAGS\_BY\_IDX()](#group__devicetree-gpio_1gafd40d1eec5c1672b7675ae47388c1cef)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **gpio\_pha** – lowercase-and-underscores GPIO property with type “phandle-array”

        Returns:
        :   the flags cell value at index 0, or zero if there is none

### [IO channels](#id20)

These are commonly used by device drivers which need to use IO
channels (e.g. ADC or DAC channels) for conversion.

*group* devicetree-io-channels
:   Defines

    DT\_IO\_CHANNELS\_CTLR\_BY\_IDX(node\_id, idx)
    :   Get the node identifier for the node referenced by an io-channels property at an index.

        Example devicetree fragment:

        ```text
        adc1: adc@... { ... };

        adc2: adc@... { ... };

        n: node {
                io-channels = <&adc1 10>, <&adc2 20>;
        };
        ```

        Example usage:

        ```text
        DT_IO_CHANNELS_CTLR_BY_IDX(DT_NODELABEL(n), 0) // DT_NODELABEL(adc1)
        DT_IO_CHANNELS_CTLR_BY_IDX(DT_NODELABEL(n), 1) // DT_NODELABEL(adc2)
        ```

        See also

        [DT\_PROP\_BY\_PHANDLE\_IDX()](#group__devicetree-generic-prop_1gaeba973992914d493cff5506ecf86a00d)

        Parameters:
        :   - **node\_id** – node identifier for a node with an io-channels property
            - **idx** – logical index into io-channels property

        Returns:
        :   the node identifier for the node referenced at index “idx”

    DT\_IO\_CHANNELS\_CTLR\_BY\_NAME(node\_id, name)
    :   Get the node identifier for the node referenced by an io-channels property by name.

        Example devicetree fragment:

        ```text
        adc1: adc@... { ... };

        adc2: adc@... { ... };

        n: node {
                io-channels = <&adc1 10>, <&adc2 20>;
                io-channel-names = "SENSOR", "BANDGAP";
        };
        ```

        Example usage:

        [DT\_IO\_CHANNELS\_CTLR\_BY\_NAME(DT\_NODELABEL(n), sensor)](#group__devicetree-io-channels_1ga1d6422230eb139beec9ac0f25ca2eab3) // [DT\_NODELABEL(adc1)](#group__devicetree-generic-id_1gab7d23294a6bf7fd44a98b48ec47d8a79) [DT\_IO\_CHANNELS\_CTLR\_BY\_NAME(DT\_NODELABEL(n), bandgap)](#group__devicetree-io-channels_1ga1d6422230eb139beec9ac0f25ca2eab3) // [DT\_NODELABEL(adc2)](#group__devicetree-generic-id_1gab7d23294a6bf7fd44a98b48ec47d8a79)

        See also

        [DT\_PHANDLE\_BY\_NAME()](#group__devicetree-generic-prop_1ga65c90d2d96255b8569c5b869b637c2fd)

        Parameters:
        :   - **node\_id** – node identifier for a node with an io-channels property
            - **name** – lowercase-and-underscores name of an io-channels element as defined by the node’s io-channel-names property

        Returns:
        :   the node identifier for the node referenced at the named element

    DT\_IO\_CHANNELS\_CTLR(node\_id)
    :   Equivalent to [DT\_IO\_CHANNELS\_CTLR\_BY\_IDX(node\_id, 0)](#group__devicetree-io-channels_1gaf5bbae59dca995d827ff3ec8b9ce187c).

        See also

        [DT\_IO\_CHANNELS\_CTLR\_BY\_IDX()](#group__devicetree-io-channels_1gaf5bbae59dca995d827ff3ec8b9ce187c)

        Parameters:
        :   - **node\_id** – node identifier for a node with an io-channels property

        Returns:
        :   the node identifier for the node referenced at index 0 in the node’s “io-channels” property

    DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX(inst, idx)
    :   Get the node identifier from a DT\_DRV\_COMPAT instance’s io-channels property at an index.

        See also

        [DT\_IO\_CHANNELS\_CTLR\_BY\_IDX()](#group__devicetree-io-channels_1gaf5bbae59dca995d827ff3ec8b9ce187c)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into io-channels property

        Returns:
        :   the node identifier for the node referenced at index “idx”

    DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_NAME(inst, name)
    :   Get the node identifier from a DT\_DRV\_COMPAT instance’s io-channels property by name.

        See also

        [DT\_IO\_CHANNELS\_CTLR\_BY\_NAME()](#group__devicetree-io-channels_1ga1d6422230eb139beec9ac0f25ca2eab3)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of an io-channels element as defined by the node’s io-channel-names property

        Returns:
        :   the node identifier for the node referenced at the named element

    DT\_INST\_IO\_CHANNELS\_CTLR(inst)
    :   Equivalent to [DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX(inst, 0)](#group__devicetree-io-channels_1gacf417be0bda7b8ddfb20503f8d846822).

        See also

        [DT\_IO\_CHANNELS\_CTLR\_BY\_IDX()](#group__devicetree-io-channels_1gaf5bbae59dca995d827ff3ec8b9ce187c)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   the node identifier for the node referenced at index 0 in the node’s “io-channels” property

    DT\_IO\_CHANNELS\_INPUT\_BY\_IDX(node\_id, idx)
    :   Get an io-channels specifier input cell at an index.

        This macro only works for io-channels specifiers with cells named “input”. Refer to the node’s binding to check if necessary.

        Example devicetree fragment:

        ```text
        adc1: adc@... {
                compatible = "vnd,adc";
                #io-channel-cells = <1>;
        };

        adc2: adc@... {
                compatible = "vnd,adc";
                #io-channel-cells = <1>;
        };

        n: node {
                io-channels = <&adc1 10>, <&adc2 20>;
        };
        ```

        Bindings fragment for the vnd,adc compatible:

        io-channel-cells:

        - input

        Example usage:

        ```text
        DT_IO_CHANNELS_INPUT_BY_IDX(DT_NODELABEL(n), 0) // 10
        DT_IO_CHANNELS_INPUT_BY_IDX(DT_NODELABEL(n), 1) // 20
        ```

        See also

        [DT\_PHA\_BY\_IDX()](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed)

        Parameters:
        :   - **node\_id** – node identifier for a node with an io-channels property
            - **idx** – logical index into io-channels property

        Returns:
        :   the input cell in the specifier at index “idx”

    DT\_IO\_CHANNELS\_INPUT\_BY\_NAME(node\_id, name)
    :   Get an io-channels specifier input cell by name.

        This macro only works for io-channels specifiers with cells named “input”. Refer to the node’s binding to check if necessary.

        Example devicetree fragment:

        ```text
        adc1: adc@... {
                compatible = "vnd,adc";
                #io-channel-cells = <1>;
        };

        adc2: adc@... {
                compatible = "vnd,adc";
                #io-channel-cells = <1>;
        };

        n: node {
                io-channels = <&adc1 10>, <&adc2 20>;
                io-channel-names = "SENSOR", "BANDGAP";
        };
        ```

        Bindings fragment for the vnd,adc compatible:

        io-channel-cells:

        - input

        Example usage:

        ```text
        DT_IO_CHANNELS_INPUT_BY_NAME(DT_NODELABEL(n), sensor) // 10
        DT_IO_CHANNELS_INPUT_BY_NAME(DT_NODELABEL(n), bandgap) // 20
        ```

        See also

        [DT\_PHA\_BY\_NAME()](#group__devicetree-generic-prop_1gae469615356a867c49416da15bdc44a26)

        Parameters:
        :   - **node\_id** – node identifier for a node with an io-channels property
            - **name** – lowercase-and-underscores name of an io-channels element as defined by the node’s io-channel-names property

        Returns:
        :   the input cell in the specifier at the named element

    DT\_IO\_CHANNELS\_INPUT(node\_id)
    :   Equivalent to [DT\_IO\_CHANNELS\_INPUT\_BY\_IDX(node\_id, 0)](#group__devicetree-io-channels_1ga290c912d0a96ba65bb44341a783fac19).

        See also

        [DT\_IO\_CHANNELS\_INPUT\_BY\_IDX()](#group__devicetree-io-channels_1ga290c912d0a96ba65bb44341a783fac19)

        Parameters:
        :   - **node\_id** – node identifier for a node with an io-channels property

        Returns:
        :   the input cell in the specifier at index 0

    DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX(inst, idx)
    :   Get an input cell from the “DT\_DRV\_INST(inst)” io-channels property at an index.

        See also

        [DT\_IO\_CHANNELS\_INPUT\_BY\_IDX()](#group__devicetree-io-channels_1ga290c912d0a96ba65bb44341a783fac19)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into io-channels property

        Returns:
        :   the input cell in the specifier at index “idx”

    DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_NAME(inst, name)
    :   Get an input cell from the “DT\_DRV\_INST(inst)” io-channels property by name.

        See also

        [DT\_IO\_CHANNELS\_INPUT\_BY\_NAME()](#group__devicetree-io-channels_1ga6870a8215f61f87c3cb8f137a7bbbcc3)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of an io-channels element as defined by the instance’s io-channel-names property

        Returns:
        :   the input cell in the specifier at the named element

    DT\_INST\_IO\_CHANNELS\_INPUT(inst)
    :   Equivalent to [DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX(inst, 0)](#group__devicetree-io-channels_1gac396f180ab5b24bdca01c021447a0211).

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   the input cell in the specifier at index 0

### [MBOX](#id21)

These conveniences may be used for nodes which describe MBOX controllers/users,
and properties related to them.

*group* devicetree-mbox
:   Defines

    DT\_MBOX\_CTLR\_BY\_NAME(node\_id, name)
    :   Get the node identifier for the MBOX controller from a mboxes property by name.

        Example devicetree fragment:

        ```text
        mbox1: mbox-controller@... { ... };

        n: node {
                mboxes = <&mbox1 8>,
                         <&mbox1 9>;
                mbox-names = "tx", "rx";
        };
        ```

        Example usage:

        ```text
        DT_MBOX_CTLR_BY_NAME(DT_NODELABEL(n), tx) // DT_NODELABEL(mbox1)
        DT_MBOX_CTLR_BY_NAME(DT_NODELABEL(n), rx) // DT_NODELABEL(mbox1)
        ```

        See also

        [DT\_PHANDLE\_BY\_NAME()](#group__devicetree-generic-prop_1ga65c90d2d96255b8569c5b869b637c2fd)

        Parameters:
        :   - **node\_id** – node identifier for a node with a mboxes property
            - **name** – lowercase-and-underscores name of a mboxes element as defined by the node’s mbox-names property

        Returns:
        :   the node identifier for the MBOX controller in the named element

    DT\_MBOX\_CHANNEL\_BY\_NAME(node\_id, name)
    :   Get a MBOX channel value by name.

        Example devicetree fragment:

        ```text
        mbox1: mbox@... {
                #mbox-cells = <1>;
        };

        n: node {
            mboxes = <&mbox1 1>,
                     <&mbox1 6>;
            mbox-names = "tx", "rx";
        };
        ```

        Bindings fragment for the mbox compatible:

        ```text
        mbox-cells:
          - channel
        ```

        Example usage:

        ```text
        DT_MBOX_CHANNEL_BY_NAME(DT_NODELABEL(n), tx) // 1
        DT_MBOX_CHANNEL_BY_NAME(DT_NODELABEL(n), rx) // 6
        ```

        See also

        [DT\_PHA\_BY\_NAME\_OR()](#group__devicetree-generic-prop_1ga79cda6ca70cc1e27b034ad096d4f4401)

        Parameters:
        :   - **node\_id** – node identifier for a node with a mboxes property
            - **name** – lowercase-and-underscores name of a mboxes element as defined by the node’s mbox-names property

        Returns:
        :   the channel value in the specifier at the named element or 0 if no channels are supported

### [Pinctrl (pin control)](#id22)

These are used to access pin control properties by name or index.

Devicetree nodes may have properties which specify pin control (sometimes known
as pin mux) settings. These are expressed using `pinctrl-<index>` properties
within the node, where the `<index>` values are contiguous integers starting
from 0. These may also be named using the `pinctrl-names` property.

Here is an example:

```dts
node {
    ...
    pinctrl-0 = <&foo &bar ...>;
    pinctrl-1 = <&baz ...>;
    pinctrl-names = "default", "sleep";
};
```

Above, `pinctrl-0` has name `"default"`, and `pinctrl-1` has name
`"sleep"`. The `pinctrl-<index>` property values contain phandles. The
`&foo`, `&bar`, etc. phandles within the properties point to nodes whose
contents vary by platform, and which describe a pin configuration for the node.

*group* devicetree-pinctrl
:   Defines

    DT\_PINCTRL\_BY\_IDX(node\_id, pc\_idx, idx)
    :   Get a node identifier for a phandle in a pinctrl property by index.

        Example devicetree fragment:

        ```text
        n: node {
                pinctrl-0 = <&foo &bar>;
                pinctrl-1 = <&baz &blub>;
        }
        ```

        Example usage:

        ```text
        DT_PINCTRL_BY_IDX(DT_NODELABEL(n), 0, 1) // DT_NODELABEL(bar)
        DT_PINCTRL_BY_IDX(DT_NODELABEL(n), 1, 0) // DT_NODELABEL(baz)
        ```

        Parameters:
        :   - **node\_id** – node with a pinctrl-‘pc\_idx’ property
            - **pc\_idx** – index of the pinctrl property itself
            - **idx** – index into the value of the pinctrl property

        Returns:
        :   node identifier for the phandle at index ‘idx’ in ‘pinctrl-‘pc\_idx’’

    DT\_PINCTRL\_0(node\_id, idx)
    :   Get a node identifier from a pinctrl-0 property.

        This is equivalent to:

        ```text
        DT_PINCTRL_BY_IDX(node_id, 0, idx)
        ```

        It is provided for convenience since pinctrl-0 is commonly used.

        Parameters:
        :   - **node\_id** – node with a pinctrl-0 property
            - **idx** – index into the pinctrl-0 property

        Returns:
        :   node identifier for the phandle at index idx in the pinctrl-0 property of that node

    DT\_PINCTRL\_BY\_NAME(node\_id, name, idx)
    :   Get a node identifier for a phandle inside a pinctrl node by name.

        Example devicetree fragment:

        ```text
        n: node {
                pinctrl-0 = <&foo &bar>;
                pinctrl-1 = <&baz &blub>;
                pinctrl-names = "default", "sleep";
        };
        ```

        Example usage:

        ```text
        DT_PINCTRL_BY_NAME(DT_NODELABEL(n), default, 1) // DT_NODELABEL(bar)
        DT_PINCTRL_BY_NAME(DT_NODELABEL(n), sleep, 0) // DT_NODELABEL(baz)
        ```

        Parameters:
        :   - **node\_id** – node with a named pinctrl property
            - **name** – lowercase-and-underscores pinctrl property name
            - **idx** – index into the value of the named pinctrl property

        Returns:
        :   node identifier for the phandle at that index in the pinctrl property

    DT\_PINCTRL\_NAME\_TO\_IDX(node\_id, name)
    :   Convert a pinctrl name to its corresponding index.

        Example devicetree fragment:

        ```text
        n: node {
                pinctrl-0 = <&foo &bar>;
                pinctrl-1 = <&baz &blub>;
                pinctrl-names = "default", "sleep";
        };
        ```

        Example usage:

        ```text
        DT_PINCTRL_NAME_TO_IDX(DT_NODELABEL(n), default) // 0
        DT_PINCTRL_NAME_TO_IDX(DT_NODELABEL(n), sleep)   // 1
        ```

        Parameters:
        :   - **node\_id** – node identifier with a named pinctrl property
            - **name** – lowercase-and-underscores name name of the pinctrl whose index to get

        Returns:
        :   integer literal for the index of the pinctrl property with that name

    DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN(node\_id, pc\_idx)
    :   Convert a pinctrl property index to its name as a token.

        This allows you to get a pinctrl property’s name, and “remove the

        quotes” from it.

        [DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN()](#group__devicetree-pinctrl_1ga47b0e5a18919f9f4829209cccbdeb430) can only be used if the node has a pinctrl-‘pc\_idx’ property and a pinctrl-names property element for that index. It is an error to use it in other circumstances.

        Example devicetree fragment:

        ```text
        n: node {
                pinctrl-0 = <...>;
                pinctrl-1 = <...>;
                pinctrl-names = "default", "f.o.o2";
        };
        ```

        Example usage:

        ```text
        DT_PINCTRL_IDX_TO_NAME_TOKEN(DT_NODELABEL(n), 0) // default
        DT_PINCTRL_IDX_TO_NAME_TOKEN(DT_NODELABEL(n), 1) // f_o_o2
        ```

        The same caveats and restrictions that apply to [DT\_STRING\_TOKEN()](#group__devicetree-generic-prop_1ga5995350cc7fd2d12ef7daa2487d1db54)’s return value also apply here.

        Parameters:
        :   - **node\_id** – node identifier
            - **pc\_idx** – index of a pinctrl property in that node

        Returns:
        :   name of the pinctrl property, as a token, without any quotes and with non-alphanumeric characters converted to underscores

    DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN(node\_id, pc\_idx)
    :   Like [DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN()](#group__devicetree-pinctrl_1ga47b0e5a18919f9f4829209cccbdeb430), but with an uppercased result.

        This does the a similar conversion as [DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN(node\_id, pc\_idx)](#group__devicetree-pinctrl_1ga47b0e5a18919f9f4829209cccbdeb430). The only difference is that alphabetical characters in the result are uppercased.

        Example devicetree fragment:

        ```text
        n: node {
                pinctrl-0 = <...>;
                pinctrl-1 = <...>;
                pinctrl-names = "default", "f.o.o2";
        };
        ```

        Example usage:

        ```text
        DT_PINCTRL_IDX_TO_NAME_TOKEN(DT_NODELABEL(n), 0) // DEFAULT
        DT_PINCTRL_IDX_TO_NAME_TOKEN(DT_NODELABEL(n), 1) // F_O_O2
        ```

        The same caveats and restrictions that apply to [DT\_STRING\_UPPER\_TOKEN()](#group__devicetree-generic-prop_1gae0b5e2b6633a98ead17ec20d3494658f)’s return value also apply here.

    DT\_NUM\_PINCTRLS\_BY\_IDX(node\_id, pc\_idx)
    :   Get the number of phandles in a pinctrl property.

        Example devicetree fragment:

        ```text
        n1: node-1 {
                pinctrl-0 = <&foo &bar>;
        };

        n2: node-2 {
                pinctrl-0 = <&baz>;
        };
        ```

        Example usage:

        ```text
        DT_NUM_PINCTRLS_BY_IDX(DT_NODELABEL(n1), 0) // 2
        DT_NUM_PINCTRLS_BY_IDX(DT_NODELABEL(n2), 0) // 1
        ```

        Parameters:
        :   - **node\_id** – node identifier with a pinctrl property
            - **pc\_idx** – index of the pinctrl property itself

        Returns:
        :   number of phandles in the property with that index

    DT\_NUM\_PINCTRLS\_BY\_NAME(node\_id, name)
    :   Like [DT\_NUM\_PINCTRLS\_BY\_IDX()](#group__devicetree-pinctrl_1ga6ae1bab2a71cb628405ec43d38705606), but by name instead.

        Example devicetree fragment:

        ```text
        n: node {
                pinctrl-0 = <&foo &bar>;
                pinctrl-1 = <&baz>
                pinctrl-names = "default", "sleep";
        };
        ```

        Example usage:

        ```text
        DT_NUM_PINCTRLS_BY_NAME(DT_NODELABEL(n), default) // 2
        DT_NUM_PINCTRLS_BY_NAME(DT_NODELABEL(n), sleep)   // 1
        ```

        Parameters:
        :   - **node\_id** – node identifier with a pinctrl property
            - **name** – lowercase-and-underscores name name of the pinctrl property

        Returns:
        :   number of phandles in the property with that name

    DT\_NUM\_PINCTRL\_STATES(node\_id)
    :   Get the number of pinctrl properties in a node.

        This expands to 0 if there are no pinctrl-i properties. Otherwise, it expands to the number of such properties.

        Example devicetree fragment:

        ```text
        n1: node-1 {
                pinctrl-0 = <...>;
                pinctrl-1 = <...>;
        };

        n2: node-2 {
        };
        ```

        Example usage:

        ```text
        DT_NUM_PINCTRL_STATES(DT_NODELABEL(n1)) // 2
        DT_NUM_PINCTRL_STATES(DT_NODELABEL(n2)) // 0
        ```

        Parameters:
        :   - **node\_id** – node identifier; may or may not have any pinctrl properties

        Returns:
        :   number of pinctrl properties in the node

    DT\_PINCTRL\_HAS\_IDX(node\_id, pc\_idx)
    :   Test if a node has a pinctrl property with an index.

        This expands to 1 if the pinctrl-‘idx’ property exists. Otherwise, it expands to 0.

        Example devicetree fragment:

        ```text
        n1: node-1 {
                pinctrl-0 = <...>;
                pinctrl-1 = <...>;
        };

        n2: node-2 {
        };
        ```

        Example usage:

        ```text
        DT_PINCTRL_HAS_IDX(DT_NODELABEL(n1), 0) // 1
        DT_PINCTRL_HAS_IDX(DT_NODELABEL(n1), 1) // 1
        DT_PINCTRL_HAS_IDX(DT_NODELABEL(n1), 2) // 0
        DT_PINCTRL_HAS_IDX(DT_NODELABEL(n2), 0) // 0
        ```

        Parameters:
        :   - **node\_id** – node identifier; may or may not have any pinctrl properties
            - **pc\_idx** – index of a pinctrl property whose existence to check

        Returns:
        :   1 if the property exists, 0 otherwise

    DT\_PINCTRL\_HAS\_NAME(node\_id, name)
    :   Test if a node has a pinctrl property with a name.

        This expands to 1 if the named pinctrl property exists. Otherwise, it expands to 0.

        Example devicetree fragment:

        ```text
        n1: node-1 {
                pinctrl-0 = <...>;
                pinctrl-names = "default";
        };

        n2: node-2 {
        };
        ```

        Example usage:

        ```text
        DT_PINCTRL_HAS_NAME(DT_NODELABEL(n1), default) // 1
        DT_PINCTRL_HAS_NAME(DT_NODELABEL(n1), sleep)   // 0
        DT_PINCTRL_HAS_NAME(DT_NODELABEL(n2), default) // 0
        ```

        Parameters:
        :   - **node\_id** – node identifier; may or may not have any pinctrl properties
            - **name** – lowercase-and-underscores pinctrl property name to check

        Returns:
        :   1 if the property exists, 0 otherwise

    DT\_INST\_PINCTRL\_BY\_IDX(inst, pc\_idx, idx)
    :   Get a node identifier for a phandle in a pinctrl property by index for a DT\_DRV\_COMPAT instance.

        This is equivalent to [DT\_PINCTRL\_BY\_IDX(DT\_DRV\_INST(inst), pc\_idx, idx)](#group__devicetree-pinctrl_1ga24089220a93bc955700fba2c6170090e).

        Parameters:
        :   - **inst** – instance number
            - **pc\_idx** – index of the pinctrl property itself
            - **idx** – index into the value of the pinctrl property

        Returns:
        :   node identifier for the phandle at index ‘idx’ in ‘pinctrl-‘pc\_idx’’

    DT\_INST\_PINCTRL\_0(inst, idx)
    :   Get a node identifier from a pinctrl-0 property for a DT\_DRV\_COMPAT instance.

        This is equivalent to:

        ```text
        DT_PINCTRL_BY_IDX(DT_DRV_INST(inst), 0, idx)
        ```

        It is provided for convenience since pinctrl-0 is commonly used.

        Parameters:
        :   - **inst** – instance number
            - **idx** – index into the pinctrl-0 property

        Returns:
        :   node identifier for the phandle at index idx in the pinctrl-0 property of that instance

    DT\_INST\_PINCTRL\_BY\_NAME(inst, name, idx)
    :   Get a node identifier for a phandle inside a pinctrl node for a DT\_DRV\_COMPAT instance.

        This is equivalent to [DT\_PINCTRL\_BY\_NAME(DT\_DRV\_INST(inst), name, idx)](#group__devicetree-pinctrl_1ga1cd336f902738fd684f3d81b3fb6caae).

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores pinctrl property name
            - **idx** – index into the value of the named pinctrl property

        Returns:
        :   node identifier for the phandle at that index in the pinctrl property

    DT\_INST\_PINCTRL\_NAME\_TO\_IDX(inst, name)
    :   Convert a pinctrl name to its corresponding index for a DT\_DRV\_COMPAT instance.

        This is equivalent to [DT\_PINCTRL\_NAME\_TO\_IDX(DT\_DRV\_INST(inst),name)](#group__devicetree-pinctrl_1ga36eb691efc2a4854ccb62555aeade785).

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores name of the pinctrl whose index to get

        Returns:
        :   integer literal for the index of the pinctrl property with that name

    DT\_INST\_PINCTRL\_IDX\_TO\_NAME\_TOKEN(inst, pc\_idx)
    :   Convert a pinctrl index to its name as an uppercased token.

        This is equivalent to [DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN(DT\_DRV\_INST(inst), pc\_idx)](#group__devicetree-pinctrl_1ga47b0e5a18919f9f4829209cccbdeb430).

        Parameters:
        :   - **inst** – instance number
            - **pc\_idx** – index of the pinctrl property itself

        Returns:
        :   name of the pin control property as a token

    DT\_INST\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN(inst, pc\_idx)
    :   Convert a pinctrl index to its name as an uppercased token.

        This is equivalent to [DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN(DT\_DRV\_INST(inst), idx)](#group__devicetree-pinctrl_1gaa6eec236ccde612e88017b027f4ba711).

        Parameters:
        :   - **inst** – instance number
            - **pc\_idx** – index of the pinctrl property itself

        Returns:
        :   name of the pin control property as an uppercase token

    DT\_INST\_NUM\_PINCTRLS\_BY\_IDX(inst, pc\_idx)
    :   Get the number of phandles in a pinctrl property for a DT\_DRV\_COMPAT instance.

        This is equivalent to [DT\_NUM\_PINCTRLS\_BY\_IDX(DT\_DRV\_INST(inst),pc\_idx)](#group__devicetree-pinctrl_1ga6ae1bab2a71cb628405ec43d38705606).

        Parameters:
        :   - **inst** – instance number
            - **pc\_idx** – index of the pinctrl property itself

        Returns:
        :   number of phandles in the property with that index

    DT\_INST\_NUM\_PINCTRLS\_BY\_NAME(inst, name)
    :   Like [DT\_INST\_NUM\_PINCTRLS\_BY\_IDX()](#group__devicetree-pinctrl_1ga1de8198573428ec717733204d91f0391), but by name instead.

        This is equivalent to [DT\_NUM\_PINCTRLS\_BY\_NAME(DT\_DRV\_INST(inst),name)](#group__devicetree-pinctrl_1gaf96f1c82cc08008882f52e719ecd348c).

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores name of the pinctrl property

        Returns:
        :   number of phandles in the property with that name

    DT\_INST\_NUM\_PINCTRL\_STATES(inst)
    :   Get the number of pinctrl properties in a DT\_DRV\_COMPAT instance.

        This is equivalent to [DT\_NUM\_PINCTRL\_STATES(DT\_DRV\_INST(inst))](#group__devicetree-pinctrl_1gaa2a012ce1d9ba026ee90001ae7f80381).

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   number of pinctrl properties in the instance

    DT\_INST\_PINCTRL\_HAS\_IDX(inst, pc\_idx)
    :   Test if a DT\_DRV\_COMPAT instance has a pinctrl property with an index.

        This is equivalent to [DT\_PINCTRL\_HAS\_IDX(DT\_DRV\_INST(inst), pc\_idx)](#group__devicetree-pinctrl_1ga5f1493cbfb7578b8fe3e37953aa9feaa).

        Parameters:
        :   - **inst** – instance number
            - **pc\_idx** – index of a pinctrl property whose existence to check

        Returns:
        :   1 if the property exists, 0 otherwise

    DT\_INST\_PINCTRL\_HAS\_NAME(inst, name)
    :   Test if a DT\_DRV\_COMPAT instance has a pinctrl property with a name.

        This is equivalent to [DT\_PINCTRL\_HAS\_NAME(DT\_DRV\_INST(inst), name)](#group__devicetree-pinctrl_1gac9cd8112ad745f34eb6f6e4a13d7fd7e).

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores pinctrl property name to check

        Returns:
        :   1 if the property exists, 0 otherwise

### [PWM](#id23)

These conveniences may be used for nodes which describe PWM controllers and
properties related to them.

*group* devicetree-pwms
:   Defines

    DT\_PWMS\_CTLR\_BY\_IDX(node\_id, idx)
    :   Get the node identifier for the PWM controller from a pwms property at an index.

        Example devicetree fragment:

        ```text
        pwm1: pwm-controller@... { ... };

        pwm2: pwm-controller@... { ... };

        n: node {
                pwms = <&pwm1 1 PWM_POLARITY_NORMAL>,
                       <&pwm2 3 PWM_POLARITY_INVERTED>;
        };
        ```

        Example usage:

        ```text
        DT_PWMS_CTLR_BY_IDX(DT_NODELABEL(n), 0) // DT_NODELABEL(pwm1)
        DT_PWMS_CTLR_BY_IDX(DT_NODELABEL(n), 1) // DT_NODELABEL(pwm2)
        ```

        See also

        [DT\_PROP\_BY\_PHANDLE\_IDX()](#group__devicetree-generic-prop_1gaeba973992914d493cff5506ecf86a00d)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property
            - **idx** – logical index into pwms property

        Returns:
        :   the node identifier for the PWM controller referenced at index “idx”

    DT\_PWMS\_CTLR\_BY\_NAME(node\_id, name)
    :   Get the node identifier for the PWM controller from a pwms property by name.

        Example devicetree fragment:

        ```text
        pwm1: pwm-controller@... { ... };
        ```

        pwm2: pwm-controller… { … };

        n: node { pwms = <&pwm1 1 PWM\_POLARITY\_NORMAL>, <&pwm2 3 PWM\_POLARITY\_INVERTED>; pwm-names = “alpha”, “beta”; };

        Example usage:

        ```text
        DT_PWMS_CTLR_BY_NAME(DT_NODELABEL(n), alpha) // DT_NODELABEL(pwm1)
        DT_PWMS_CTLR_BY_NAME(DT_NODELABEL(n), beta)  // DT_NODELABEL(pwm2)
        ```

        See also

        [DT\_PHANDLE\_BY\_NAME()](#group__devicetree-generic-prop_1ga65c90d2d96255b8569c5b869b637c2fd)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property
            - **name** – lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property

        Returns:
        :   the node identifier for the PWM controller in the named element

    DT\_PWMS\_CTLR(node\_id)
    :   Equivalent to [DT\_PWMS\_CTLR\_BY\_IDX(node\_id, 0)](#group__devicetree-pwms_1ga2f16d00a53717a66668fb8bc967acce5).

        See also

        [DT\_PWMS\_CTLR\_BY\_IDX()](#group__devicetree-pwms_1ga2f16d00a53717a66668fb8bc967acce5)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property

        Returns:
        :   the node identifier for the PWM controller at index 0 in the node’s “pwms” property

    DT\_PWMS\_CELL\_BY\_IDX(node\_id, idx, cell)
    :   Get PWM specifier’s cell value at an index.

        Example devicetree fragment:

        ```text
        pwm1: pwm-controller@... {
                compatible = "vnd,pwm";
                #pwm-cells = <2>;
        };

        pwm2: pwm-controller@... {
                compatible = "vnd,pwm";
                #pwm-cells = <2>;
        };

        n: node {
                pwms = <&pwm1 1 200000 PWM_POLARITY_NORMAL>,
                       <&pwm2 3 100000 PWM_POLARITY_INVERTED>;
        };
        ```

        Bindings fragment for the “vnd,pwm” compatible:

        ```text
        pwm-cells:
          - channel
          - period
          - flags
        ```

        Example usage:

        ```text
        DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 0, channel) // 1
        DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 1, channel) // 3
        DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 0, period)  // 200000
        DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 1, period)  // 100000
        DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 0, flags)   // PWM_POLARITY_NORMAL
        DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 1, flags)   // PWM_POLARITY_INVERTED
        ```

        See also

        [DT\_PHA\_BY\_IDX()](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property
            - **idx** – logical index into pwms property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value at index “idx”

    DT\_PWMS\_CELL\_BY\_NAME(node\_id, name, cell)
    :   Get a PWM specifier’s cell value by name.

        Example devicetree fragment:

        ```text
        pwm1: pwm-controller@... {
                compatible = "vnd,pwm";
                #pwm-cells = <2>;
        };

        pwm2: pwm-controller@... {
                compatible = "vnd,pwm";
                #pwm-cells = <2>;
        };

        n: node {
                pwms = <&pwm1 1 200000 PWM_POLARITY_NORMAL>,
                       <&pwm2 3 100000 PWM_POLARITY_INVERTED>;
                pwm-names = "alpha", "beta";
        };
        ```

        Bindings fragment for the “vnd,pwm” compatible:

        ```text
        pwm-cells:
          - channel
          - period
          - flags
        ```

        Example usage:

        ```text
        DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), alpha, channel) // 1
        DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), beta, channel)  // 3
        DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), alpha, period)  // 200000
        DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), beta, period)   // 100000
        DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), alpha, flags)   // PWM_POLARITY_NORMAL
        DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), beta, flags)    // PWM_POLARITY_INVERTED
        ```

        See also

        [DT\_PHA\_BY\_NAME()](#group__devicetree-generic-prop_1gae469615356a867c49416da15bdc44a26)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property
            - **name** – lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value in the specifier at the named element

    DT\_PWMS\_CELL(node\_id, cell)
    :   Equivalent to [DT\_PWMS\_CELL\_BY\_IDX(node\_id, 0, cell)](#group__devicetree-pwms_1ga0c1ab3329448f92936d57a83b5b3594e).

        See also

        [DT\_PWMS\_CELL\_BY\_IDX()](#group__devicetree-pwms_1ga0c1ab3329448f92936d57a83b5b3594e)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value at index 0

    DT\_PWMS\_CHANNEL\_BY\_IDX(node\_id, idx)
    :   Get a PWM specifier’s channel cell value at an index.

        This macro only works for PWM specifiers with cells named “channel”. Refer to the node’s binding to check if necessary.

        This is equivalent to [DT\_PWMS\_CELL\_BY\_IDX(node\_id, idx, channel)](#group__devicetree-pwms_1ga0c1ab3329448f92936d57a83b5b3594e).

        See also

        [DT\_PWMS\_CELL\_BY\_IDX()](#group__devicetree-pwms_1ga0c1ab3329448f92936d57a83b5b3594e)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property
            - **idx** – logical index into pwms property

        Returns:
        :   the channel cell value at index “idx”

    DT\_PWMS\_CHANNEL\_BY\_NAME(node\_id, name)
    :   Get a PWM specifier’s channel cell value by name.

        This macro only works for PWM specifiers with cells named “channel”. Refer to the node’s binding to check if necessary.

        This is equivalent to [DT\_PWMS\_CELL\_BY\_NAME(node\_id, name, channel)](#group__devicetree-pwms_1ga69233198a489283068bc1ded5072ca26).

        See also

        [DT\_PWMS\_CELL\_BY\_NAME()](#group__devicetree-pwms_1ga69233198a489283068bc1ded5072ca26)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property
            - **name** – lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property

        Returns:
        :   the channel cell value in the specifier at the named element

    DT\_PWMS\_CHANNEL(node\_id)
    :   Equivalent to [DT\_PWMS\_CHANNEL\_BY\_IDX(node\_id, 0)](#group__devicetree-pwms_1ga10a372e44c7e3feb551ca996c6ca5a8f).

        See also

        [DT\_PWMS\_CHANNEL\_BY\_IDX()](#group__devicetree-pwms_1ga10a372e44c7e3feb551ca996c6ca5a8f)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property

        Returns:
        :   the channel cell value at index 0

    DT\_PWMS\_PERIOD\_BY\_IDX(node\_id, idx)
    :   Get PWM specifier’s period cell value at an index.

        This macro only works for PWM specifiers with cells named “period”. Refer to the node’s binding to check if necessary.

        This is equivalent to [DT\_PWMS\_CELL\_BY\_IDX(node\_id, idx, period)](#group__devicetree-pwms_1ga0c1ab3329448f92936d57a83b5b3594e).

        See also

        [DT\_PWMS\_CELL\_BY\_IDX()](#group__devicetree-pwms_1ga0c1ab3329448f92936d57a83b5b3594e)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property
            - **idx** – logical index into pwms property

        Returns:
        :   the period cell value at index “idx”

    DT\_PWMS\_PERIOD\_BY\_NAME(node\_id, name)
    :   Get a PWM specifier’s period cell value by name.

        This macro only works for PWM specifiers with cells named “period”. Refer to the node’s binding to check if necessary.

        This is equivalent to [DT\_PWMS\_CELL\_BY\_NAME(node\_id, name, period)](#group__devicetree-pwms_1ga69233198a489283068bc1ded5072ca26).

        See also

        [DT\_PWMS\_CELL\_BY\_NAME()](#group__devicetree-pwms_1ga69233198a489283068bc1ded5072ca26)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property
            - **name** – lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property

        Returns:
        :   the period cell value in the specifier at the named element

    DT\_PWMS\_PERIOD(node\_id)
    :   Equivalent to [DT\_PWMS\_PERIOD\_BY\_IDX(node\_id, 0)](#group__devicetree-pwms_1ga9456f65777e6fc7c057c6e0709c9245f).

        See also

        [DT\_PWMS\_PERIOD\_BY\_IDX()](#group__devicetree-pwms_1ga9456f65777e6fc7c057c6e0709c9245f)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property

        Returns:
        :   the period cell value at index 0

    DT\_PWMS\_FLAGS\_BY\_IDX(node\_id, idx)
    :   Get a PWM specifier’s flags cell value at an index.

        This macro expects PWM specifiers with cells named “flags”. If there is no “flags” cell in the PWM specifier, zero is returned. Refer to the node’s binding to check specifier cell names if necessary.

        This is equivalent to [DT\_PWMS\_CELL\_BY\_IDX(node\_id, idx, flags)](#group__devicetree-pwms_1ga0c1ab3329448f92936d57a83b5b3594e).

        See also

        [DT\_PWMS\_CELL\_BY\_IDX()](#group__devicetree-pwms_1ga0c1ab3329448f92936d57a83b5b3594e)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property
            - **idx** – logical index into pwms property

        Returns:
        :   the flags cell value at index “idx”, or zero if there is none

    DT\_PWMS\_FLAGS\_BY\_NAME(node\_id, name)
    :   Get a PWM specifier’s flags cell value by name.

        This macro expects PWM specifiers with cells named “flags”. If there is no “flags” cell in the PWM specifier, zero is returned. Refer to the node’s binding to check specifier cell names if necessary.

        This is equivalent to [DT\_PWMS\_CELL\_BY\_NAME(node\_id, name, flags)](#group__devicetree-pwms_1ga69233198a489283068bc1ded5072ca26) if there is a flags cell, but expands to zero if there is none.

        See also

        [DT\_PWMS\_CELL\_BY\_NAME()](#group__devicetree-pwms_1ga69233198a489283068bc1ded5072ca26)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property
            - **name** – lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property

        Returns:
        :   the flags cell value in the specifier at the named element, or zero if there is none

    DT\_PWMS\_FLAGS(node\_id)
    :   Equivalent to [DT\_PWMS\_FLAGS\_BY\_IDX(node\_id, 0)](#group__devicetree-pwms_1gaf9c1ac7f3a39f4022f3ec31ef8de98e6).

        See also

        [DT\_PWMS\_FLAGS\_BY\_IDX()](#group__devicetree-pwms_1gaf9c1ac7f3a39f4022f3ec31ef8de98e6)

        Parameters:
        :   - **node\_id** – node identifier for a node with a pwms property

        Returns:
        :   the flags cell value at index 0, or zero if there is none

    DT\_INST\_PWMS\_CTLR\_BY\_IDX(inst, idx)
    :   Get the node identifier for the PWM controller from a DT\_DRV\_COMPAT instance’s pwms property at an index.

        See also

        [DT\_PWMS\_CTLR\_BY\_IDX()](#group__devicetree-pwms_1ga2f16d00a53717a66668fb8bc967acce5)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into pwms property

        Returns:
        :   the node identifier for the PWM controller referenced at index “idx”

    DT\_INST\_PWMS\_CTLR\_BY\_NAME(inst, name)
    :   Get the node identifier for the PWM controller from a DT\_DRV\_COMPAT instance’s pwms property by name.

        See also

        [DT\_PWMS\_CTLR\_BY\_NAME()](#group__devicetree-pwms_1ga6922e69c707219cd766fe317484dac8a)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property

        Returns:
        :   the node identifier for the PWM controller in the named element

    DT\_INST\_PWMS\_CTLR(inst)
    :   Equivalent to [DT\_INST\_PWMS\_CTLR\_BY\_IDX(inst, 0)](#group__devicetree-pwms_1ga4f751ba5f3c1aad5d62178b166f36c24).

        See also

        [DT\_PWMS\_CTLR\_BY\_IDX()](#group__devicetree-pwms_1ga2f16d00a53717a66668fb8bc967acce5)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   the node identifier for the PWM controller at index 0 in the instance’s “pwms” property

    DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, cell)
    :   Get a DT\_DRV\_COMPAT instance’s PWM specifier’s cell value at an index.

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into pwms property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value at index “idx”

    DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, cell)
    :   Get a DT\_DRV\_COMPAT instance’s PWM specifier’s cell value by name.

        See also

        [DT\_PWMS\_CELL\_BY\_NAME()](#group__devicetree-pwms_1ga69233198a489283068bc1ded5072ca26)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value in the specifier at the named element

    DT\_INST\_PWMS\_CELL(inst, cell)
    :   Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, 0, cell)](#group__devicetree-pwms_1gad106bf22d9dc90384519cd6ccc8fd1c6).

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value at index 0

    DT\_INST\_PWMS\_CHANNEL\_BY\_IDX(inst, idx)
    :   Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, channel)](#group__devicetree-pwms_1gad106bf22d9dc90384519cd6ccc8fd1c6).

        See also

        [DT\_INST\_PWMS\_CELL\_BY\_IDX()](#group__devicetree-pwms_1gad106bf22d9dc90384519cd6ccc8fd1c6)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into pwms property

        Returns:
        :   the channel cell value at index “idx”

    DT\_INST\_PWMS\_CHANNEL\_BY\_NAME(inst, name)
    :   Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, channel)](#group__devicetree-pwms_1ga5731d949be09461f5da040e451cc509c).

        See also

        [DT\_INST\_PWMS\_CELL\_BY\_NAME()](#group__devicetree-pwms_1ga5731d949be09461f5da040e451cc509c)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property

        Returns:
        :   the channel cell value in the specifier at the named element

    DT\_INST\_PWMS\_CHANNEL(inst)
    :   Equivalent to [DT\_INST\_PWMS\_CHANNEL\_BY\_IDX(inst, 0)](#group__devicetree-pwms_1ga154ece84d782a7df2ce31b2a34f43870).

        See also

        [DT\_INST\_PWMS\_CHANNEL\_BY\_IDX()](#group__devicetree-pwms_1ga154ece84d782a7df2ce31b2a34f43870)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   the channel cell value at index 0

    DT\_INST\_PWMS\_PERIOD\_BY\_IDX(inst, idx)
    :   Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, period)](#group__devicetree-pwms_1gad106bf22d9dc90384519cd6ccc8fd1c6).

        See also

        [DT\_INST\_PWMS\_CELL\_BY\_IDX()](#group__devicetree-pwms_1gad106bf22d9dc90384519cd6ccc8fd1c6)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into pwms property

        Returns:
        :   the period cell value at index “idx”

    DT\_INST\_PWMS\_PERIOD\_BY\_NAME(inst, name)
    :   Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, period)](#group__devicetree-pwms_1ga5731d949be09461f5da040e451cc509c).

        See also

        [DT\_INST\_PWMS\_CELL\_BY\_NAME()](#group__devicetree-pwms_1ga5731d949be09461f5da040e451cc509c)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property

        Returns:
        :   the period cell value in the specifier at the named element

    DT\_INST\_PWMS\_PERIOD(inst)
    :   Equivalent to [DT\_INST\_PWMS\_PERIOD\_BY\_IDX(inst, 0)](#group__devicetree-pwms_1ga7e7408507ecdac75cb7c9ba2b9176ec8).

        See also

        [DT\_INST\_PWMS\_PERIOD\_BY\_IDX()](#group__devicetree-pwms_1ga7e7408507ecdac75cb7c9ba2b9176ec8)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   the period cell value at index 0

    DT\_INST\_PWMS\_FLAGS\_BY\_IDX(inst, idx)
    :   Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, flags)](#group__devicetree-pwms_1gad106bf22d9dc90384519cd6ccc8fd1c6).

        See also

        [DT\_INST\_PWMS\_CELL\_BY\_IDX()](#group__devicetree-pwms_1gad106bf22d9dc90384519cd6ccc8fd1c6)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into pwms property

        Returns:
        :   the flags cell value at index “idx”, or zero if there is none

    DT\_INST\_PWMS\_FLAGS\_BY\_NAME(inst, name)
    :   Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, flags)](#group__devicetree-pwms_1ga5731d949be09461f5da040e451cc509c).

        See also

        [DT\_INST\_PWMS\_CELL\_BY\_NAME()](#group__devicetree-pwms_1ga5731d949be09461f5da040e451cc509c)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property

        Returns:
        :   the flags cell value in the specifier at the named element, or zero if there is none

    DT\_INST\_PWMS\_FLAGS(inst)
    :   Equivalent to [DT\_INST\_PWMS\_FLAGS\_BY\_IDX(inst, 0)](#group__devicetree-pwms_1ga9cfbc4e3c0ab9d419cfb7700a5b42ced).

        See also

        [DT\_INST\_PWMS\_FLAGS\_BY\_IDX()](#group__devicetree-pwms_1ga9cfbc4e3c0ab9d419cfb7700a5b42ced)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   the flags cell value at index 0, or zero if there is none

### [Reset Controller](#id24)

These conveniences may be used for nodes which describe reset controllers and
properties related to them.

*group* devicetree-reset-controller
:   Defines

    DT\_RESET\_CTLR\_BY\_IDX(node\_id, idx)
    :   Get the node identifier for the controller phandle from a “resets” phandle-array property at an index.

        Example devicetree fragment:

        ```text
        reset1: reset-controller@... { ... };

        reset2: reset-controller@... { ... };

        n: node {
                resets = <&reset1 10>, <&reset2 20>;
        };
        ```

        Example usage:

        ```text
        DT_RESET_CTLR_BY_IDX(DT_NODELABEL(n), 0)) // DT_NODELABEL(reset1)
        DT_RESET_CTLR_BY_IDX(DT_NODELABEL(n), 1)) // DT_NODELABEL(reset2)
        ```

        See also

        [DT\_PHANDLE\_BY\_IDX()](#group__devicetree-generic-prop_1ga8ff163c240878a988d29d727671671de)

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – logical index into “resets”

        Returns:
        :   the node identifier for the reset controller referenced at index “idx”

    DT\_RESET\_CTLR(node\_id)
    :   Equivalent to [DT\_RESET\_CTLR\_BY\_IDX(node\_id, 0)](#group__devicetree-reset-controller_1gaa730fe6a58ee0a2d9daf7e125048f9e6).

        See also

        [DT\_RESET\_CTLR\_BY\_IDX()](#group__devicetree-reset-controller_1gaa730fe6a58ee0a2d9daf7e125048f9e6)

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   a node identifier for the reset controller at index 0 in “resets”

    DT\_RESET\_CTLR\_BY\_NAME(node\_id, name)
    :   Get the node identifier for the controller phandle from a resets phandle-array property by name.

        Example devicetree fragment:

        ```text
        reset1: reset-controller@... { ... };

        reset2: reset-controller@... { ... };

        n: node {
                resets = <&reset1 10>, <&reset2 20>;
                reset-names = "alpha", "beta";
        };
        ```

        Example usage:

        ```text
        DT_RESET_CTLR_BY_NAME(DT_NODELABEL(n), alpha) // DT_NODELABEL(reset1)
        DT_RESET_CTLR_BY_NAME(DT_NODELABEL(n), beta) // DT_NODELABEL(reset2)
        ```

        See also

        [DT\_PHANDLE\_BY\_NAME()](#group__devicetree-generic-prop_1ga65c90d2d96255b8569c5b869b637c2fd)

        Parameters:
        :   - **node\_id** – node identifier
            - **name** – lowercase-and-underscores name of a resets element as defined by the node’s reset-names property

        Returns:
        :   the node identifier for the reset controller referenced by name

    DT\_RESET\_CELL\_BY\_IDX(node\_id, idx, cell)
    :   Get a reset specifier’s cell value at an index.

        Example devicetree fragment:

        ```text
        reset: reset-controller@... {
                compatible = "vnd,reset";
                #reset-cells = <1>;
        };

        n: node {
                resets = <&reset 10>;
        };
        ```

        Bindings fragment for the vnd,reset compatible:

        ```text
        reset-cells:
          - id
        ```

        Example usage:

        ```text
        DT_RESET_CELL_BY_IDX(DT_NODELABEL(n), 0, id) // 10
        ```

        See also

        [DT\_PHA\_BY\_IDX()](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed)

        Parameters:
        :   - **node\_id** – node identifier for a node with a resets property
            - **idx** – logical index into resets property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value at index “idx”

    DT\_RESET\_CELL\_BY\_NAME(node\_id, name, cell)
    :   Get a reset specifier’s cell value by name.

        Example devicetree fragment:

        ```text
        reset: reset-controller@... {
                compatible = "vnd,reset";
                #reset-cells = <1>;
        };

        n: node {
                resets = <&reset 10>;
                reset-names = "alpha";
        };
        ```

        Bindings fragment for the vnd,reset compatible:

        ```text
        reset-cells:
          - id
        ```

        Example usage:

        ```text
        DT_RESET_CELL_BY_NAME(DT_NODELABEL(n), alpha, id) // 10
        ```

        See also

        [DT\_PHA\_BY\_NAME()](#group__devicetree-generic-prop_1gae469615356a867c49416da15bdc44a26)

        Parameters:
        :   - **node\_id** – node identifier for a node with a resets property
            - **name** – lowercase-and-underscores name of a resets element as defined by the node’s reset-names property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value in the specifier at the named element

    DT\_RESET\_CELL(node\_id, cell)
    :   Equivalent to [DT\_RESET\_CELL\_BY\_IDX(node\_id, 0, cell)](#group__devicetree-reset-controller_1ga17918c75ef82acea60d7e65b6f1cee0a).

        See also

        [DT\_RESET\_CELL\_BY\_IDX()](#group__devicetree-reset-controller_1ga17918c75ef82acea60d7e65b6f1cee0a)

        Parameters:
        :   - **node\_id** – node identifier for a node with a resets property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value at index 0

    DT\_INST\_RESET\_CTLR\_BY\_IDX(inst, idx)
    :   Get the node identifier for the controller phandle from a “resets” phandle-array property at an index.

        See also

        [DT\_RESET\_CTLR\_BY\_IDX()](#group__devicetree-reset-controller_1gaa730fe6a58ee0a2d9daf7e125048f9e6)

        Parameters:
        :   - **inst** – instance number
            - **idx** – logical index into “resets”

        Returns:
        :   the node identifier for the reset controller referenced at index “idx”

    DT\_INST\_RESET\_CTLR(inst)
    :   Equivalent to [DT\_INST\_RESET\_CTLR\_BY\_IDX(inst, 0)](#group__devicetree-reset-controller_1ga44cc59dc014eb69aacd4b6fedb5b2a54).

        See also

        [DT\_RESET\_CTLR()](#group__devicetree-reset-controller_1ga55afbfa565375eb4b233051f7065e504)

        Parameters:
        :   - **inst** – instance number

        Returns:
        :   a node identifier for the reset controller at index 0 in “resets”

    DT\_INST\_RESET\_CTLR\_BY\_NAME(inst, name)
    :   Get the node identifier for the controller phandle from a resets phandle-array property by name.

        See also

        [DT\_RESET\_CTLR\_BY\_NAME()](#group__devicetree-reset-controller_1ga5bc0702036df3a38ceb2d2741ee0717d)

        Parameters:
        :   - **inst** – instance number
            - **name** – lowercase-and-underscores name of a resets element as defined by the node’s reset-names property

        Returns:
        :   the node identifier for the reset controller referenced by the named element

    DT\_INST\_RESET\_CELL\_BY\_IDX(inst, idx, cell)
    :   Get a DT\_DRV\_COMPAT instance’s reset specifier’s cell value at an index.

        See also

        [DT\_RESET\_CELL\_BY\_IDX()](#group__devicetree-reset-controller_1ga17918c75ef82acea60d7e65b6f1cee0a)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into resets property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value at index “idx”

    DT\_INST\_RESET\_CELL\_BY\_NAME(inst, name, cell)
    :   Get a DT\_DRV\_COMPAT instance’s reset specifier’s cell value by name.

        See also

        [DT\_RESET\_CELL\_BY\_NAME()](#group__devicetree-reset-controller_1ga102229a7a1a30a29c5a5bf2bb0d42ada)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of a resets element as defined by the node’s reset-names property
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the cell value in the specifier at the named element

    DT\_INST\_RESET\_CELL(inst, cell)
    :   Equivalent to [DT\_INST\_RESET\_CELL\_BY\_IDX(inst, 0, cell)](#group__devicetree-reset-controller_1ga9727e93185d96b84ec2d53ef07597a02).

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **cell** – lowercase-and-underscores cell name

        Returns:
        :   the value of the cell inside the specifier at index 0

    DT\_RESET\_ID\_BY\_IDX(node\_id, idx)
    :   Get a Reset Controller specifier’s id cell at an index.

        This macro only works for Reset Controller specifiers with cells named “id”. Refer to the node’s binding to check if necessary.

        Example devicetree fragment:

        ```text
        reset: reset-controller@... {
                compatible = "vnd,reset";
                #reset-cells = <1>;
        };

        n: node {
                resets = <&reset 10>;
        };
        ```

        Bindings fragment for the vnd,reset compatible:

        ```text
        reset-cells:
          - id
        ```

        Example usage:

        ```text
        DT_RESET_ID_BY_IDX(DT_NODELABEL(n), 0) // 10
        ```

        See also

        [DT\_PHA\_BY\_IDX()](#group__devicetree-generic-prop_1ga118b63fd22c20ef940ac2fa073c126ed)

        Parameters:
        :   - **node\_id** – node identifier
            - **idx** – logical index into “resets”

        Returns:
        :   the id cell value at index “idx”

    DT\_RESET\_ID(node\_id)
    :   Equivalent to [DT\_RESET\_ID\_BY\_IDX(node\_id, 0)](#group__devicetree-reset-controller_1ga4259b4aa8bfe6f4ccb268c180541237d).

        See also

        [DT\_RESET\_ID\_BY\_IDX()](#group__devicetree-reset-controller_1ga4259b4aa8bfe6f4ccb268c180541237d)

        Parameters:
        :   - **node\_id** – node identifier

        Returns:
        :   the id cell value at index 0

    DT\_INST\_RESET\_ID\_BY\_IDX(inst, idx)
    :   Get a DT\_DRV\_COMPAT instance’s Reset Controller specifier’s id cell value at an index.

        See also

        [DT\_RESET\_ID\_BY\_IDX()](#group__devicetree-reset-controller_1ga4259b4aa8bfe6f4ccb268c180541237d)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into “resets”

        Returns:
        :   the id cell value at index “idx”

    DT\_INST\_RESET\_ID(inst)
    :   Equivalent to [DT\_INST\_RESET\_ID\_BY\_IDX(inst, 0)](#group__devicetree-reset-controller_1gac42ce32f6e5fd1ae2b449bcf60d70afc).

        See also

        [DT\_INST\_RESET\_ID\_BY\_IDX()](#group__devicetree-reset-controller_1gac42ce32f6e5fd1ae2b449bcf60d70afc)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   the id cell value at index 0

### [SPI](#id25)

These conveniences may be used for nodes which describe either SPI controllers
or devices, depending on the case.

*group* devicetree-spi
:   Defines

    DT\_SPI\_HAS\_CS\_GPIOS(spi)
    :   Does a SPI controller node have chip select GPIOs configured?

        SPI bus controllers use the “cs-gpios” property for configuring chip select GPIOs. Its value is a phandle-array which specifies the chip select lines.

        Example devicetree fragment:

        ```text
        spi1: spi@... {
                compatible = "vnd,spi";
                cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                           <&gpio2 20 GPIO_ACTIVE_LOW>;
        };

        spi2: spi@... {
                compatible = "vnd,spi";
        };
        ```

        Example usage:

        ```text
        DT_SPI_HAS_CS_GPIOS(DT_NODELABEL(spi1)) // 1
        DT_SPI_HAS_CS_GPIOS(DT_NODELABEL(spi2)) // 0
        ```

        Parameters:
        :   - **spi** – a SPI bus controller node identifier

        Returns:
        :   1 if “spi” has a cs-gpios property, 0 otherwise

    DT\_SPI\_NUM\_CS\_GPIOS(spi)
    :   Number of chip select GPIOs in a SPI controller’s cs-gpios property.

        Example devicetree fragment:

        ```text
        spi1: spi@... {
                compatible = "vnd,spi";
                cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                           <&gpio2 20 GPIO_ACTIVE_LOW>;
        };

        spi2: spi@... {
                compatible = "vnd,spi";
        };
        ```

        Example usage:

        ```text
        DT_SPI_NUM_CS_GPIOS(DT_NODELABEL(spi1)) // 2
        DT_SPI_NUM_CS_GPIOS(DT_NODELABEL(spi2)) // 0
        ```

        Parameters:
        :   - **spi** – a SPI bus controller node identifier

        Returns:
        :   Logical length of spi’s cs-gpios property, or 0 if “spi” doesn’t have a cs-gpios property

    DT\_SPI\_DEV\_HAS\_CS\_GPIOS(spi\_dev)
    :   Does a SPI device have a chip select line configured?

        Example devicetree fragment:

        ```text
        spi1: spi@... {
                compatible = "vnd,spi";
                cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                           <&gpio2 20 GPIO_ACTIVE_LOW>;

                a: spi-dev-a@0 {
                        reg = <0>;
                };

                b: spi-dev-b@1 {
                        reg = <1>;
                };
        };

        spi2: spi@... {
                compatible = "vnd,spi";
                c: spi-dev-c@0 {
                        reg = <0>;
                };
        };
        ```

        Example usage:

        ```text
        DT_SPI_DEV_HAS_CS_GPIOS(DT_NODELABEL(a)) // 1
        DT_SPI_DEV_HAS_CS_GPIOS(DT_NODELABEL(b)) // 1
        DT_SPI_DEV_HAS_CS_GPIOS(DT_NODELABEL(c)) // 0
        ```

        Parameters:
        :   - **spi\_dev** – a SPI device node identifier

        Returns:
        :   1 if spi\_dev’s bus node [DT\_BUS(spi\_dev)](#group__devicetree-generic-bus_1ga1082d31ac2dafdf9e085d4c23f2169dc) has a chip select pin at index [DT\_REG\_ADDR(spi\_dev)](#group__devicetree-reg-prop_1gac6d8279c32351ced4c0ac7f32270974e), 0 otherwise

    DT\_SPI\_DEV\_CS\_GPIOS\_CTLR(spi\_dev)
    :   Get a SPI device’s chip select GPIO controller’s node identifier.

        Example devicetree fragment:

        ```text
        gpio1: gpio@... { ... };

        gpio2: gpio@... { ... };

        spi@... {
                compatible = "vnd,spi";
                cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                           <&gpio2 20 GPIO_ACTIVE_LOW>;

                a: spi-dev-a@0 {
                        reg = <0>;
                };

                b: spi-dev-b@1 {
                        reg = <1>;
                };
        };
        ```

        Example usage:

        ```text
        DT_SPI_DEV_CS_GPIOS_CTLR(DT_NODELABEL(a)) // DT_NODELABEL(gpio1)
        DT_SPI_DEV_CS_GPIOS_CTLR(DT_NODELABEL(b)) // DT_NODELABEL(gpio2)
        ```

        Parameters:
        :   - **spi\_dev** – a SPI device node identifier

        Returns:
        :   node identifier for spi\_dev’s chip select GPIO controller

    DT\_SPI\_DEV\_CS\_GPIOS\_PIN(spi\_dev)
    :   Get a SPI device’s chip select GPIO pin number.

        It’s an error if the GPIO specifier for spi\_dev’s entry in its bus node’s cs-gpios property has no pin cell.

        Example devicetree fragment:

        ```text
        spi1: spi@... {
                compatible = "vnd,spi";
                cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                           <&gpio2 20 GPIO_ACTIVE_LOW>;

                a: spi-dev-a@0 {
                        reg = <0>;
                };

                b: spi-dev-b@1 {
                        reg = <1>;
                };
        };
        ```

        Example usage:

        ```text
        DT_SPI_DEV_CS_GPIOS_PIN(DT_NODELABEL(a)) // 10
        DT_SPI_DEV_CS_GPIOS_PIN(DT_NODELABEL(b)) // 20
        ```

        Parameters:
        :   - **spi\_dev** – a SPI device node identifier

        Returns:
        :   pin number of spi\_dev’s chip select GPIO

    DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS(spi\_dev)
    :   Get a SPI device’s chip select GPIO flags.

        Example devicetree fragment:

        ```text
        spi1: spi@... {
                compatible = "vnd,spi";
                cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>;

                a: spi-dev-a@0 {
                        reg = <0>;
                };
        };
        ```

        Example usage:

        ```text
        DT_SPI_DEV_CS_GPIOS_FLAGS(DT_NODELABEL(a)) // GPIO_ACTIVE_LOW
        ```

        If the GPIO specifier for spi\_dev’s entry in its bus node’s cs-gpios property has no flags cell, this expands to zero.

        Parameters:
        :   - **spi\_dev** – a SPI device node identifier

        Returns:
        :   flags value of spi\_dev’s chip select GPIO specifier, or zero if there is none

    DT\_INST\_SPI\_DEV\_HAS\_CS\_GPIOS(inst)
    :   Equivalent to [DT\_SPI\_DEV\_HAS\_CS\_GPIOS(DT\_DRV\_INST(inst))](#group__devicetree-spi_1gad66b759d6aa4826f2c68a94e8708ad4f).

        See also

        [DT\_SPI\_DEV\_HAS\_CS\_GPIOS()](#group__devicetree-spi_1gad66b759d6aa4826f2c68a94e8708ad4f)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   1 if the instance’s bus has a CS pin at index [DT\_INST\_REG\_ADDR(inst)](#group__devicetree-inst_1gafde8fa67b94ac959ba2e24b44b3386a7), 0 otherwise

    DT\_INST\_SPI\_DEV\_CS\_GPIOS\_CTLR(inst)
    :   Get GPIO controller node identifier for a SPI device instance This is equivalent to [DT\_SPI\_DEV\_CS\_GPIOS\_CTLR(DT\_DRV\_INST(inst))](#group__devicetree-spi_1ga0eaad9de680b5ac7cd8950957560c199).

        See also

        [DT\_SPI\_DEV\_CS\_GPIOS\_CTLR()](#group__devicetree-spi_1ga0eaad9de680b5ac7cd8950957560c199)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   node identifier for instance’s chip select GPIO controller

    DT\_INST\_SPI\_DEV\_CS\_GPIOS\_PIN(inst)
    :   Equivalent to [DT\_SPI\_DEV\_CS\_GPIOS\_PIN(DT\_DRV\_INST(inst))](#group__devicetree-spi_1ga8c1dd6a65c6f7fdf67291be1ed47fc9f).

        See also

        [DT\_SPI\_DEV\_CS\_GPIOS\_PIN()](#group__devicetree-spi_1ga8c1dd6a65c6f7fdf67291be1ed47fc9f)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   pin number of the instance’s chip select GPIO

    DT\_INST\_SPI\_DEV\_CS\_GPIOS\_FLAGS(inst)
    :   [DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS(DT\_DRV\_INST(inst))](#group__devicetree-spi_1ga49fd9c174931b44584a7dbbc18f7c644).

        See also

        [DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS()](#group__devicetree-spi_1ga49fd9c174931b44584a7dbbc18f7c644)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   flags value of the instance’s chip select GPIO specifier, or zero if there is none

## [Chosen nodes](#id26)

The special `/chosen` node contains properties whose values describe
system-wide settings. The [`DT_CHOSEN()`](#c.DT_CHOSEN) macro can be used to get a node
identifier for a chosen node.

*group* devicetree-generic-chosen
:   Defines

    DT\_CHOSEN(prop)
    :   Get a node identifier for a `/chosen` node property.

        This is only valid to call if `[DT_HAS_CHOSEN(prop)](#group__devicetree-generic-chosen_1ga9df6bacab5f579284f5f3c1e4856cd15)` is 1.

        Parameters:
        :   - **prop** – lowercase-and-underscores property name for the /chosen node

        Returns:
        :   a node identifier for the chosen node property

    DT\_HAS\_CHOSEN(prop)
    :   Test if the devicetree has a `/chosen` node.

        Parameters:
        :   - **prop** – lowercase-and-underscores devicetree property

        Returns:
        :   1 if the chosen property exists and refers to a node, 0 otherwise

## [Zephyr-specific chosen nodes](#id27)

The following table documents some commonly used Zephyr-specific chosen nodes.

Sometimes, a chosen node’s label property will be used to set the default value
of a Kconfig option which in turn configures a hardware-specific device. This
is usually for backwards compatibility in cases when the Kconfig option
predates devicetree support in Zephyr. In other cases, there is no Kconfig
option, and the devicetree node is used directly in the source code to select a
device.

Zephyr-specific chosen properties

| Property | Purpose |
| --- | --- |
| zephyr,bt-c2h-uart | Selects the UART used for host communication in the [Bluetooth: HCI UART](../../../samples/bluetooth/hci_uart/README.md#bluetooth-hci-uart-sample) |
| zephyr,bt-mon-uart | Sets UART device used for the Bluetooth monitor logging |
| zephyr,bt-uart | Sets UART device used by Bluetooth |
| zephyr,canbus | Sets the default CAN controller |
| zephyr,ccm | Core-Coupled Memory node on some STM32 SoCs |
| zephyr,code-partition | Flash partition that the Zephyr image’s text section should be linked into |
| zephyr,console | Sets UART device used by console driver |
| zephyr,display | Sets the default display controller |
| zephyr,keyboard-scan | Sets the default keyboard scan controller |
| zephyr,dtcm | Data Tightly Coupled Memory node on some Arm SoCs |
| zephyr,entropy | A device which can be used as a system-wide entropy source |
| zephyr,flash | A node whose `reg` is sometimes used to set the defaults for [`CONFIG_FLASH_BASE_ADDRESS`](../../../kconfig.md#CONFIG_FLASH_BASE_ADDRESS "CONFIG_FLASH_BASE_ADDRESS") and [`CONFIG_FLASH_SIZE`](../../../kconfig.md#CONFIG_FLASH_SIZE "CONFIG_FLASH_SIZE") |
| zephyr,flash-controller | The node corresponding to the flash controller device for the `zephyr,flash` node |
| zephyr,gdbstub-uart | Sets UART device used by the [GDB stub](../../../services/debugging/gdbstub.md#gdbstub) subsystem |
| zephyr,ieee802154 | Used by the networking subsystem to set the IEEE 802.15.4 device |
| zephyr,ipc | Used by the OpenAMP subsystem to specify the inter-process communication (IPC) device |
| zephyr,ipc\_shm | A node whose `reg` is used by the OpenAMP subsystem to determine the base address and size of the shared memory (SHM) usable for interprocess-communication (IPC) |
| zephyr,itcm | Instruction Tightly Coupled Memory node on some Arm SoCs |
| zephyr,log-uart | Sets the UART device(s) used by the logging subsystem’s UART backend. If defined, the UART log backend would output to the devices listed in this node. |
| zephyr,ocm | On-chip memory node on Xilinx Zynq-7000 and ZynqMP SoCs |
| zephyr,osdp-uart | Sets UART device used by OSDP subsystem |
| zephyr,ot-uart | Used by the OpenThread to specify UART device for Spinel protocol |
| zephyr,pcie-controller | The node corresponding to the PCIe Controller |
| zephyr,ppp-uart | Sets UART device used by PPP |
| zephyr,settings-partition | Fixed partition node. If defined this selects the partition used by the NVS and FCB settings backends. |
| zephyr,shell-uart | Sets UART device used by serial shell backend |
| zephyr,sram | A node whose `reg` sets the base address and size of SRAM memory available to the Zephyr image, used during linking |
| zephyr,tracing-uart | Sets UART device used by tracing subsystem |
| zephyr,uart-mcumgr | UART used for [Device Management](../../../services/device_mgmt/index.md#device-mgmt) |
| zephyr,uart-pipe | Sets UART device used by serial pipe driver |
| zephyr,usb-device | USB device node. If defined and has a `vbus-gpios` property, these will be used by the USB subsystem to enable/disable VBUS |
