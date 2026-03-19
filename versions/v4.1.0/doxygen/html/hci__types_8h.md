---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hci__types_8h.html
original_path: doxygen/html/hci__types_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci\_types.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/bluetooth/addr.h](addr_8h_source.md)>`

[Go to the source code of this file.](hci__types_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_hci\_sco\_hdr](structbt__hci__sco__hdr.md) |
| struct | [bt\_hci\_evt\_hdr](structbt__hci__evt__hdr.md) |
| struct | [bt\_hci\_acl\_hdr](structbt__hci__acl__hdr.md) |
| struct | [bt\_hci\_iso\_sdu\_hdr](structbt__hci__iso__sdu__hdr.md) |
| struct | [bt\_hci\_iso\_sdu\_ts\_hdr](structbt__hci__iso__sdu__ts__hdr.md) |
| struct | [bt\_hci\_iso\_hdr](structbt__hci__iso__hdr.md) |
| struct | [bt\_hci\_cmd\_hdr](structbt__hci__cmd__hdr.md) |
| struct | [bt\_hci\_op\_inquiry](structbt__hci__op__inquiry.md) |
| struct | [bt\_hci\_cp\_connect](structbt__hci__cp__connect.md) |
| struct | [bt\_hci\_cp\_disconnect](structbt__hci__cp__disconnect.md) |
| struct | [bt\_hci\_cp\_connect\_cancel](structbt__hci__cp__connect__cancel.md) |
| struct | [bt\_hci\_rp\_connect\_cancel](structbt__hci__rp__connect__cancel.md) |
| struct | [bt\_hci\_cp\_accept\_conn\_req](structbt__hci__cp__accept__conn__req.md) |
| struct | [bt\_hci\_cp\_setup\_sync\_conn](structbt__hci__cp__setup__sync__conn.md) |
| struct | [bt\_hci\_cp\_accept\_sync\_conn\_req](structbt__hci__cp__accept__sync__conn__req.md) |
| struct | [bt\_hci\_cp\_reject\_conn\_req](structbt__hci__cp__reject__conn__req.md) |
| struct | [bt\_hci\_cp\_link\_key\_reply](structbt__hci__cp__link__key__reply.md) |
| struct | [bt\_hci\_cp\_link\_key\_neg\_reply](structbt__hci__cp__link__key__neg__reply.md) |
| struct | [bt\_hci\_cp\_pin\_code\_reply](structbt__hci__cp__pin__code__reply.md) |
| struct | [bt\_hci\_rp\_pin\_code\_reply](structbt__hci__rp__pin__code__reply.md) |
| struct | [bt\_hci\_cp\_pin\_code\_neg\_reply](structbt__hci__cp__pin__code__neg__reply.md) |
| struct | [bt\_hci\_rp\_pin\_code\_neg\_reply](structbt__hci__rp__pin__code__neg__reply.md) |
| struct | [bt\_hci\_cp\_auth\_requested](structbt__hci__cp__auth__requested.md) |
| struct | [bt\_hci\_cp\_set\_conn\_encrypt](structbt__hci__cp__set__conn__encrypt.md) |
| struct | [bt\_hci\_cp\_remote\_name\_request](structbt__hci__cp__remote__name__request.md) |
| struct | [bt\_hci\_cp\_remote\_name\_cancel](structbt__hci__cp__remote__name__cancel.md) |
| struct | [bt\_hci\_rp\_remote\_name\_cancel](structbt__hci__rp__remote__name__cancel.md) |
| struct | [bt\_hci\_cp\_read\_remote\_features](structbt__hci__cp__read__remote__features.md) |
| struct | [bt\_hci\_cp\_read\_remote\_ext\_features](structbt__hci__cp__read__remote__ext__features.md) |
| struct | [bt\_hci\_cp\_read\_remote\_version\_info](structbt__hci__cp__read__remote__version__info.md) |
| struct | [bt\_hci\_cp\_io\_capability\_reply](structbt__hci__cp__io__capability__reply.md) |
| struct | [bt\_hci\_cp\_user\_confirm\_reply](structbt__hci__cp__user__confirm__reply.md) |
| struct | [bt\_hci\_rp\_user\_confirm\_reply](structbt__hci__rp__user__confirm__reply.md) |
| struct | [bt\_hci\_cp\_user\_passkey\_reply](structbt__hci__cp__user__passkey__reply.md) |
| struct | [bt\_hci\_cp\_user\_passkey\_neg\_reply](structbt__hci__cp__user__passkey__neg__reply.md) |
| struct | [bt\_hci\_cp\_io\_capability\_neg\_reply](structbt__hci__cp__io__capability__neg__reply.md) |
| struct | [bt\_hci\_cp\_set\_event\_mask](structbt__hci__cp__set__event__mask.md) |
| struct | [bt\_hci\_write\_local\_name](structbt__hci__write__local__name.md) |
| struct | [bt\_hci\_rp\_read\_conn\_accept\_timeout](structbt__hci__rp__read__conn__accept__timeout.md) |
| struct | [bt\_hci\_cp\_write\_conn\_accept\_timeout](structbt__hci__cp__write__conn__accept__timeout.md) |
| struct | [bt\_hci\_rp\_write\_conn\_accept\_timeout](structbt__hci__rp__write__conn__accept__timeout.md) |
| struct | [bt\_hci\_cp\_write\_class\_of\_device](structbt__hci__cp__write__class__of__device.md) |
| struct | [bt\_hci\_cp\_read\_tx\_power\_level](structbt__hci__cp__read__tx__power__level.md) |
| struct | [bt\_hci\_rp\_read\_tx\_power\_level](structbt__hci__rp__read__tx__power__level.md) |
| struct | [bt\_hci\_cp\_le\_read\_tx\_power\_level](structbt__hci__cp__le__read__tx__power__level.md) |
| struct | [bt\_hci\_rp\_le\_read\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md) |
| struct | [bt\_hci\_cp\_le\_set\_tx\_power\_report\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md) |
| struct | [bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_parameters](structbt__hci__cp__le__set__path__loss__reporting__parameters.md) |
| struct | [bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_enable](structbt__hci__cp__le__set__path__loss__reporting__enable.md) |
| struct | [bt\_hci\_cp\_le\_set\_default\_subrate](structbt__hci__cp__le__set__default__subrate.md) |
| struct | [bt\_hci\_cp\_le\_subrate\_request](structbt__hci__cp__le__subrate__request.md) |
| struct | [bt\_hci\_cp\_set\_ctl\_to\_host\_flow](structbt__hci__cp__set__ctl__to__host__flow.md) |
| struct | [bt\_hci\_cp\_host\_buffer\_size](structbt__hci__cp__host__buffer__size.md) |
| struct | [bt\_hci\_handle\_count](structbt__hci__handle__count.md) |
| struct | [bt\_hci\_cp\_host\_num\_completed\_packets](structbt__hci__cp__host__num__completed__packets.md) |
| struct | [bt\_hci\_cp\_write\_inquiry\_mode](structbt__hci__cp__write__inquiry__mode.md) |
| struct | [bt\_hci\_cp\_write\_ssp\_mode](structbt__hci__cp__write__ssp__mode.md) |
| struct | [bt\_hci\_cp\_set\_event\_mask\_page\_2](structbt__hci__cp__set__event__mask__page__2.md) |
| struct | [bt\_hci\_cp\_write\_le\_host\_supp](structbt__hci__cp__write__le__host__supp.md) |
| struct | [bt\_hci\_cp\_write\_sc\_host\_supp](structbt__hci__cp__write__sc__host__supp.md) |
| struct | [bt\_hci\_cp\_read\_auth\_payload\_timeout](structbt__hci__cp__read__auth__payload__timeout.md) |
| struct | [bt\_hci\_rp\_read\_auth\_payload\_timeout](structbt__hci__rp__read__auth__payload__timeout.md) |
| struct | [bt\_hci\_cp\_write\_auth\_payload\_timeout](structbt__hci__cp__write__auth__payload__timeout.md) |
| struct | [bt\_hci\_rp\_write\_auth\_payload\_timeout](structbt__hci__rp__write__auth__payload__timeout.md) |
| struct | [bt\_hci\_cp\_configure\_data\_path](structbt__hci__cp__configure__data__path.md) |
| struct | [bt\_hci\_rp\_configure\_data\_path](structbt__hci__rp__configure__data__path.md) |
| struct | [bt\_hci\_rp\_read\_local\_version\_info](structbt__hci__rp__read__local__version__info.md) |
| struct | [bt\_hci\_rp\_read\_supported\_commands](structbt__hci__rp__read__supported__commands.md) |
| struct | [bt\_hci\_cp\_read\_local\_ext\_features](structbt__hci__cp__read__local__ext__features.md) |
| struct | [bt\_hci\_rp\_read\_local\_ext\_features](structbt__hci__rp__read__local__ext__features.md) |
| struct | [bt\_hci\_rp\_read\_local\_features](structbt__hci__rp__read__local__features.md) |
| struct | [bt\_hci\_rp\_read\_buffer\_size](structbt__hci__rp__read__buffer__size.md) |
| struct | [bt\_hci\_rp\_read\_bd\_addr](structbt__hci__rp__read__bd__addr.md) |
| struct | [bt\_hci\_std\_codec\_info](structbt__hci__std__codec__info.md) |
| struct | [bt\_hci\_std\_codecs](structbt__hci__std__codecs.md) |
| struct | [bt\_hci\_vs\_codec\_info](structbt__hci__vs__codec__info.md) |
| struct | [bt\_hci\_vs\_codecs](structbt__hci__vs__codecs.md) |
| struct | [bt\_hci\_rp\_read\_codecs](structbt__hci__rp__read__codecs.md) |
| struct | [bt\_hci\_std\_codec\_info\_v2](structbt__hci__std__codec__info__v2.md) |
| struct | [bt\_hci\_std\_codecs\_v2](structbt__hci__std__codecs__v2.md) |
| struct | [bt\_hci\_vs\_codec\_info\_v2](structbt__hci__vs__codec__info__v2.md) |
| struct | [bt\_hci\_vs\_codecs\_v2](structbt__hci__vs__codecs__v2.md) |
| struct | [bt\_hci\_rp\_read\_codecs\_v2](structbt__hci__rp__read__codecs__v2.md) |
| struct | [bt\_hci\_cp\_codec\_id](structbt__hci__cp__codec__id.md) |
| struct | [bt\_hci\_cp\_read\_codec\_capabilities](structbt__hci__cp__read__codec__capabilities.md) |
| struct | [bt\_hci\_codec\_capability\_info](structbt__hci__codec__capability__info.md) |
| struct | [bt\_hci\_rp\_read\_codec\_capabilities](structbt__hci__rp__read__codec__capabilities.md) |
| struct | [bt\_hci\_cp\_read\_ctlr\_delay](structbt__hci__cp__read__ctlr__delay.md) |
| struct | [bt\_hci\_rp\_read\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md) |
| struct | [bt\_hci\_cp\_read\_rssi](structbt__hci__cp__read__rssi.md) |
| struct | [bt\_hci\_rp\_read\_rssi](structbt__hci__rp__read__rssi.md) |
| struct | [bt\_hci\_cp\_read\_encryption\_key\_size](structbt__hci__cp__read__encryption__key__size.md) |
| struct | [bt\_hci\_rp\_read\_encryption\_key\_size](structbt__hci__rp__read__encryption__key__size.md) |
| struct | [bt\_hci\_cp\_le\_set\_event\_mask](structbt__hci__cp__le__set__event__mask.md) |
| struct | [bt\_hci\_rp\_le\_read\_buffer\_size](structbt__hci__rp__le__read__buffer__size.md) |
| struct | [bt\_hci\_rp\_le\_read\_local\_features](structbt__hci__rp__le__read__local__features.md) |
| struct | [bt\_hci\_cp\_le\_set\_random\_address](structbt__hci__cp__le__set__random__address.md) |
| struct | [bt\_hci\_cp\_le\_set\_adv\_param](structbt__hci__cp__le__set__adv__param.md) |
| struct | [bt\_hci\_rp\_le\_read\_chan\_tx\_power](structbt__hci__rp__le__read__chan__tx__power.md) |
| struct | [bt\_hci\_cp\_le\_set\_adv\_data](structbt__hci__cp__le__set__adv__data.md) |
| struct | [bt\_hci\_cp\_le\_set\_scan\_rsp\_data](structbt__hci__cp__le__set__scan__rsp__data.md) |
| struct | [bt\_hci\_cp\_le\_set\_adv\_enable](structbt__hci__cp__le__set__adv__enable.md) |
| struct | [bt\_hci\_cp\_le\_set\_scan\_param](structbt__hci__cp__le__set__scan__param.md) |
| struct | [bt\_hci\_cp\_le\_set\_scan\_enable](structbt__hci__cp__le__set__scan__enable.md) |
| struct | [bt\_hci\_cp\_le\_create\_conn](structbt__hci__cp__le__create__conn.md) |
| struct | [bt\_hci\_rp\_le\_read\_fal\_size](structbt__hci__rp__le__read__fal__size.md) |
| struct | [bt\_hci\_cp\_le\_add\_dev\_to\_fal](structbt__hci__cp__le__add__dev__to__fal.md) |
| struct | [bt\_hci\_cp\_le\_rem\_dev\_from\_fal](structbt__hci__cp__le__rem__dev__from__fal.md) |
| struct | [hci\_cp\_le\_conn\_update](structhci__cp__le__conn__update.md) |
| struct | [bt\_hci\_cp\_le\_set\_host\_chan\_classif](structbt__hci__cp__le__set__host__chan__classif.md) |
| struct | [bt\_hci\_cp\_le\_read\_chan\_map](structbt__hci__cp__le__read__chan__map.md) |
| struct | [bt\_hci\_rp\_le\_read\_chan\_map](structbt__hci__rp__le__read__chan__map.md) |
| struct | [bt\_hci\_cp\_le\_read\_remote\_features](structbt__hci__cp__le__read__remote__features.md) |
| struct | [bt\_hci\_cp\_le\_encrypt](structbt__hci__cp__le__encrypt.md) |
| struct | [bt\_hci\_rp\_le\_encrypt](structbt__hci__rp__le__encrypt.md) |
| struct | [bt\_hci\_rp\_le\_rand](structbt__hci__rp__le__rand.md) |
| struct | [bt\_hci\_cp\_le\_start\_encryption](structbt__hci__cp__le__start__encryption.md) |
| struct | [bt\_hci\_cp\_le\_ltk\_req\_reply](structbt__hci__cp__le__ltk__req__reply.md) |
| struct | [bt\_hci\_rp\_le\_ltk\_req\_reply](structbt__hci__rp__le__ltk__req__reply.md) |
| struct | [bt\_hci\_cp\_le\_ltk\_req\_neg\_reply](structbt__hci__cp__le__ltk__req__neg__reply.md) |
| struct | [bt\_hci\_rp\_le\_ltk\_req\_neg\_reply](structbt__hci__rp__le__ltk__req__neg__reply.md) |
| struct | [bt\_hci\_rp\_le\_read\_supp\_states](structbt__hci__rp__le__read__supp__states.md) |
| struct | [bt\_hci\_cp\_le\_rx\_test](structbt__hci__cp__le__rx__test.md) |
| struct | [bt\_hci\_cp\_le\_tx\_test](structbt__hci__cp__le__tx__test.md) |
| struct | [bt\_hci\_rp\_le\_test\_end](structbt__hci__rp__le__test__end.md) |
| struct | [bt\_hci\_cp\_le\_conn\_param\_req\_reply](structbt__hci__cp__le__conn__param__req__reply.md) |
| struct | [bt\_hci\_rp\_le\_conn\_param\_req\_reply](structbt__hci__rp__le__conn__param__req__reply.md) |
| struct | [bt\_hci\_cp\_le\_conn\_param\_req\_neg\_reply](structbt__hci__cp__le__conn__param__req__neg__reply.md) |
| struct | [bt\_hci\_rp\_le\_conn\_param\_req\_neg\_reply](structbt__hci__rp__le__conn__param__req__neg__reply.md) |
| struct | [bt\_hci\_cp\_le\_set\_data\_len](structbt__hci__cp__le__set__data__len.md) |
| struct | [bt\_hci\_rp\_le\_set\_data\_len](structbt__hci__rp__le__set__data__len.md) |
| struct | [bt\_hci\_rp\_le\_read\_default\_data\_len](structbt__hci__rp__le__read__default__data__len.md) |
| struct | [bt\_hci\_cp\_le\_write\_default\_data\_len](structbt__hci__cp__le__write__default__data__len.md) |
| struct | [bt\_hci\_cp\_le\_generate\_dhkey](structbt__hci__cp__le__generate__dhkey.md) |
| struct | [bt\_hci\_cp\_le\_generate\_dhkey\_v2](structbt__hci__cp__le__generate__dhkey__v2.md) |
| struct | [bt\_hci\_cp\_le\_add\_dev\_to\_rl](structbt__hci__cp__le__add__dev__to__rl.md) |
| struct | [bt\_hci\_cp\_le\_rem\_dev\_from\_rl](structbt__hci__cp__le__rem__dev__from__rl.md) |
| struct | [bt\_hci\_rp\_le\_read\_rl\_size](structbt__hci__rp__le__read__rl__size.md) |
| struct | [bt\_hci\_cp\_le\_read\_peer\_rpa](structbt__hci__cp__le__read__peer__rpa.md) |
| struct | [bt\_hci\_rp\_le\_read\_peer\_rpa](structbt__hci__rp__le__read__peer__rpa.md) |
| struct | [bt\_hci\_cp\_le\_read\_local\_rpa](structbt__hci__cp__le__read__local__rpa.md) |
| struct | [bt\_hci\_rp\_le\_read\_local\_rpa](structbt__hci__rp__le__read__local__rpa.md) |
| struct | [bt\_hci\_cp\_le\_set\_addr\_res\_enable](structbt__hci__cp__le__set__addr__res__enable.md) |
| struct | [bt\_hci\_cp\_le\_set\_rpa\_timeout](structbt__hci__cp__le__set__rpa__timeout.md) |
| struct | [bt\_hci\_rp\_le\_read\_max\_data\_len](structbt__hci__rp__le__read__max__data__len.md) |
| struct | [bt\_hci\_cp\_le\_read\_phy](structbt__hci__cp__le__read__phy.md) |
| struct | [bt\_hci\_rp\_le\_read\_phy](structbt__hci__rp__le__read__phy.md) |
| struct | [bt\_hci\_cp\_le\_set\_default\_phy](structbt__hci__cp__le__set__default__phy.md) |
| struct | [bt\_hci\_cp\_le\_set\_phy](structbt__hci__cp__le__set__phy.md) |
| struct | [bt\_hci\_cp\_le\_enh\_rx\_test](structbt__hci__cp__le__enh__rx__test.md) |
| struct | [bt\_hci\_cp\_le\_enh\_tx\_test](structbt__hci__cp__le__enh__tx__test.md) |
| struct | [bt\_hci\_cp\_le\_set\_adv\_set\_random\_addr](structbt__hci__cp__le__set__adv__set__random__addr.md) |
| struct | [bt\_hci\_cp\_le\_set\_ext\_adv\_param](structbt__hci__cp__le__set__ext__adv__param.md) |
| struct | [bt\_hci\_rp\_le\_set\_ext\_adv\_param](structbt__hci__rp__le__set__ext__adv__param.md) |
| struct | [bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2](structbt__hci__cp__le__set__ext__adv__param__v2.md) |
| struct | [bt\_hci\_cp\_le\_set\_ext\_adv\_data](structbt__hci__cp__le__set__ext__adv__data.md) |
| struct | [bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data](structbt__hci__cp__le__set__ext__scan__rsp__data.md) |
| struct | [bt\_hci\_ext\_adv\_set](structbt__hci__ext__adv__set.md) |
| struct | [bt\_hci\_cp\_le\_set\_ext\_adv\_enable](structbt__hci__cp__le__set__ext__adv__enable.md) |
| struct | [bt\_hci\_rp\_le\_read\_max\_adv\_data\_len](structbt__hci__rp__le__read__max__adv__data__len.md) |
| struct | [bt\_hci\_rp\_le\_read\_num\_adv\_sets](structbt__hci__rp__le__read__num__adv__sets.md) |
| struct | [bt\_hci\_cp\_le\_remove\_adv\_set](structbt__hci__cp__le__remove__adv__set.md) |
| struct | [bt\_hci\_cp\_le\_set\_per\_adv\_param](structbt__hci__cp__le__set__per__adv__param.md) |
| struct | [bt\_hci\_cp\_le\_set\_per\_adv\_data](structbt__hci__cp__le__set__per__adv__data.md) |
| struct | [bt\_hci\_cp\_le\_set\_per\_adv\_enable](structbt__hci__cp__le__set__per__adv__enable.md) |
| struct | [bt\_hci\_ext\_scan\_phy](structbt__hci__ext__scan__phy.md) |
| struct | [bt\_hci\_cp\_le\_set\_ext\_scan\_param](structbt__hci__cp__le__set__ext__scan__param.md) |
| struct | [bt\_hci\_cp\_le\_set\_ext\_scan\_enable](structbt__hci__cp__le__set__ext__scan__enable.md) |
| struct | [bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md) |
| struct | [bt\_hci\_cp\_le\_ext\_create\_conn](structbt__hci__cp__le__ext__create__conn.md) |
| struct | [bt\_hci\_cp\_le\_ext\_create\_conn\_v2](structbt__hci__cp__le__ext__create__conn__v2.md) |
| struct | [bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element](structbt__hci__cp__le__set__pawr__subevent__data__element.md) |
| struct | [bt\_hci\_cp\_le\_set\_pawr\_subevent\_data](structbt__hci__cp__le__set__pawr__subevent__data.md) |
| struct | [bt\_hci\_cp\_le\_set\_pawr\_response\_data](structbt__hci__cp__le__set__pawr__response__data.md) |
| struct | [bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent](structbt__hci__cp__le__set__pawr__sync__subevent.md) |
| struct | [bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2](structbt__hci__cp__le__set__per__adv__param__v2.md) |
| struct | [bt\_hci\_cp\_le\_per\_adv\_create\_sync](structbt__hci__cp__le__per__adv__create__sync.md) |
| struct | [bt\_hci\_cp\_le\_per\_adv\_terminate\_sync](structbt__hci__cp__le__per__adv__terminate__sync.md) |
| struct | [bt\_hci\_cp\_le\_add\_dev\_to\_per\_adv\_list](structbt__hci__cp__le__add__dev__to__per__adv__list.md) |
| struct | [bt\_hci\_cp\_le\_rem\_dev\_from\_per\_adv\_list](structbt__hci__cp__le__rem__dev__from__per__adv__list.md) |
| struct | [bt\_hci\_rp\_le\_read\_per\_adv\_list\_size](structbt__hci__rp__le__read__per__adv__list__size.md) |
| struct | [bt\_hci\_rp\_le\_read\_tx\_power](structbt__hci__rp__le__read__tx__power.md) |
| struct | [bt\_hci\_rp\_le\_read\_rf\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md) |
| struct | [bt\_hci\_cp\_le\_write\_rf\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md) |
| struct | [bt\_hci\_cp\_le\_set\_privacy\_mode](structbt__hci__cp__le__set__privacy__mode.md) |
| struct | [bt\_hci\_cp\_le\_rx\_test\_v3](structbt__hci__cp__le__rx__test__v3.md) |
| struct | [bt\_hci\_cp\_le\_tx\_test\_v3](structbt__hci__cp__le__tx__test__v3.md) |
| struct | [bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params](structbt__hci__cp__le__set__cl__cte__tx__params.md) |
| struct | [bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_enable](structbt__hci__cp__le__set__cl__cte__tx__enable.md) |
| struct | [bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable](structbt__hci__cp__le__set__cl__cte__sampling__enable.md) |
| struct | [bt\_hci\_rp\_le\_set\_cl\_cte\_sampling\_enable](structbt__hci__rp__le__set__cl__cte__sampling__enable.md) |
| struct | [bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params](structbt__hci__cp__le__set__conn__cte__rx__params.md) |
| struct | [bt\_hci\_rp\_le\_set\_conn\_cte\_rx\_params](structbt__hci__rp__le__set__conn__cte__rx__params.md) |
| struct | [bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params](structbt__hci__cp__le__set__conn__cte__tx__params.md) |
| struct | [bt\_hci\_rp\_le\_set\_conn\_cte\_tx\_params](structbt__hci__rp__le__set__conn__cte__tx__params.md) |
| struct | [bt\_hci\_cp\_le\_conn\_cte\_req\_enable](structbt__hci__cp__le__conn__cte__req__enable.md) |
| struct | [bt\_hci\_rp\_le\_conn\_cte\_req\_enable](structbt__hci__rp__le__conn__cte__req__enable.md) |
| struct | [bt\_hci\_cp\_le\_conn\_cte\_rsp\_enable](structbt__hci__cp__le__conn__cte__rsp__enable.md) |
| struct | [bt\_hci\_rp\_le\_conn\_cte\_rsp\_enable](structbt__hci__rp__le__conn__cte__rsp__enable.md) |
| struct | [bt\_hci\_rp\_le\_read\_ant\_info](structbt__hci__rp__le__read__ant__info.md) |
| struct | [bt\_hci\_cp\_le\_set\_per\_adv\_recv\_enable](structbt__hci__cp__le__set__per__adv__recv__enable.md) |
| struct | [bt\_hci\_cp\_le\_per\_adv\_sync\_transfer](structbt__hci__cp__le__per__adv__sync__transfer.md) |
| struct | [bt\_hci\_rp\_le\_per\_adv\_sync\_transfer](structbt__hci__rp__le__per__adv__sync__transfer.md) |
| struct | [bt\_hci\_cp\_le\_per\_adv\_set\_info\_transfer](structbt__hci__cp__le__per__adv__set__info__transfer.md) |
| struct | [bt\_hci\_rp\_le\_per\_adv\_set\_info\_transfer](structbt__hci__rp__le__per__adv__set__info__transfer.md) |
| struct | [bt\_hci\_cp\_le\_past\_param](structbt__hci__cp__le__past__param.md) |
| struct | [bt\_hci\_rp\_le\_past\_param](structbt__hci__rp__le__past__param.md) |
| struct | [bt\_hci\_cp\_le\_default\_past\_param](structbt__hci__cp__le__default__past__param.md) |
| struct | [bt\_hci\_rp\_le\_default\_past\_param](structbt__hci__rp__le__default__past__param.md) |
| struct | [bt\_hci\_rp\_le\_read\_buffer\_size\_v2](structbt__hci__rp__le__read__buffer__size__v2.md) |
| struct | [bt\_hci\_cp\_le\_read\_iso\_tx\_sync](structbt__hci__cp__le__read__iso__tx__sync.md) |
| struct | [bt\_hci\_rp\_le\_read\_iso\_tx\_sync](structbt__hci__rp__le__read__iso__tx__sync.md) |
| struct | [bt\_hci\_cis\_params](structbt__hci__cis__params.md) |
| struct | [bt\_hci\_cp\_le\_set\_cig\_params](structbt__hci__cp__le__set__cig__params.md) |
| struct | [bt\_hci\_rp\_le\_set\_cig\_params](structbt__hci__rp__le__set__cig__params.md) |
| struct | [bt\_hci\_cis\_params\_test](structbt__hci__cis__params__test.md) |
| struct | [bt\_hci\_cp\_le\_set\_cig\_params\_test](structbt__hci__cp__le__set__cig__params__test.md) |
| struct | [bt\_hci\_rp\_le\_set\_cig\_params\_test](structbt__hci__rp__le__set__cig__params__test.md) |
| struct | [bt\_hci\_cis](structbt__hci__cis.md) |
| struct | [bt\_hci\_cp\_le\_create\_cis](structbt__hci__cp__le__create__cis.md) |
| struct | [bt\_hci\_cp\_le\_remove\_cig](structbt__hci__cp__le__remove__cig.md) |
| struct | [bt\_hci\_rp\_le\_remove\_cig](structbt__hci__rp__le__remove__cig.md) |
| struct | [bt\_hci\_cp\_le\_accept\_cis](structbt__hci__cp__le__accept__cis.md) |
| struct | [bt\_hci\_cp\_le\_reject\_cis](structbt__hci__cp__le__reject__cis.md) |
| struct | [bt\_hci\_rp\_le\_reject\_cis](structbt__hci__rp__le__reject__cis.md) |
| struct | [bt\_hci\_cp\_le\_create\_big](structbt__hci__cp__le__create__big.md) |
| struct | [bt\_hci\_cp\_le\_create\_big\_test](structbt__hci__cp__le__create__big__test.md) |
| struct | [bt\_hci\_cp\_le\_terminate\_big](structbt__hci__cp__le__terminate__big.md) |
| struct | [bt\_hci\_cp\_le\_big\_create\_sync](structbt__hci__cp__le__big__create__sync.md) |
| struct | [bt\_hci\_cp\_le\_big\_terminate\_sync](structbt__hci__cp__le__big__terminate__sync.md) |
| struct | [bt\_hci\_rp\_le\_big\_terminate\_sync](structbt__hci__rp__le__big__terminate__sync.md) |
| struct | [bt\_hci\_cp\_le\_req\_peer\_sca](structbt__hci__cp__le__req__peer__sca.md) |
| struct | [bt\_hci\_cp\_le\_setup\_iso\_path](structbt__hci__cp__le__setup__iso__path.md) |
| struct | [bt\_hci\_rp\_le\_setup\_iso\_path](structbt__hci__rp__le__setup__iso__path.md) |
| struct | [bt\_hci\_cp\_le\_remove\_iso\_path](structbt__hci__cp__le__remove__iso__path.md) |
| struct | [bt\_hci\_rp\_le\_remove\_iso\_path](structbt__hci__rp__le__remove__iso__path.md) |
| struct | [bt\_hci\_cp\_le\_iso\_transmit\_test](structbt__hci__cp__le__iso__transmit__test.md) |
| struct | [bt\_hci\_rp\_le\_iso\_transmit\_test](structbt__hci__rp__le__iso__transmit__test.md) |
| struct | [bt\_hci\_cp\_le\_iso\_receive\_test](structbt__hci__cp__le__iso__receive__test.md) |
| struct | [bt\_hci\_rp\_le\_iso\_receive\_test](structbt__hci__rp__le__iso__receive__test.md) |
| struct | [bt\_hci\_cp\_le\_read\_test\_counters](structbt__hci__cp__le__read__test__counters.md) |
| struct | [bt\_hci\_rp\_le\_read\_test\_counters](structbt__hci__rp__le__read__test__counters.md) |
| struct | [bt\_hci\_cp\_le\_iso\_test\_end](structbt__hci__cp__le__iso__test__end.md) |
| struct | [bt\_hci\_rp\_le\_iso\_test\_end](structbt__hci__rp__le__iso__test__end.md) |
| struct | [bt\_hci\_cp\_le\_set\_host\_feature](structbt__hci__cp__le__set__host__feature.md) |
| struct | [bt\_hci\_rp\_le\_set\_host\_feature](structbt__hci__rp__le__set__host__feature.md) |
| struct | [bt\_hci\_cp\_le\_read\_iso\_link\_quality](structbt__hci__cp__le__read__iso__link__quality.md) |
| struct | [bt\_hci\_rp\_le\_read\_iso\_link\_quality](structbt__hci__rp__le__read__iso__link__quality.md) |
| struct | [bt\_hci\_cp\_le\_tx\_test\_v4](structbt__hci__cp__le__tx__test__v4.md) |
| struct | [bt\_hci\_cp\_le\_tx\_test\_v4\_tx\_power](structbt__hci__cp__le__tx__test__v4__tx__power.md) |
| struct | [bt\_hci\_rp\_le\_read\_local\_supported\_capabilities](structbt__hci__rp__le__read__local__supported__capabilities.md) |
| struct | [bt\_hci\_cp\_le\_read\_remote\_supported\_capabilities](structbt__hci__cp__le__read__remote__supported__capabilities.md) |
| struct | [bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md) |
| struct | [bt\_hci\_cp\_le\_security\_enable](structbt__hci__cp__le__security__enable.md) |
| struct | [bt\_hci\_cp\_le\_cs\_set\_default\_settings](structbt__hci__cp__le__cs__set__default__settings.md) |
| struct | [bt\_hci\_cp\_le\_read\_remote\_fae\_table](structbt__hci__cp__le__read__remote__fae__table.md) |
| struct | [bt\_hci\_cp\_le\_write\_cached\_remote\_fae\_table](structbt__hci__cp__le__write__cached__remote__fae__table.md) |
| struct | [bt\_hci\_cp\_le\_set\_procedure\_parameters](structbt__hci__cp__le__set__procedure__parameters.md) |
| struct | [bt\_hci\_cp\_le\_procedure\_enable](structbt__hci__cp__le__procedure__enable.md) |
| struct | [bt\_hci\_op\_le\_cs\_test](structbt__hci__op__le__cs__test.md) |
| struct | [bt\_hci\_cp\_le\_cs\_create\_config](structbt__hci__cp__le__cs__create__config.md) |
| struct | [bt\_hci\_cp\_le\_cs\_remove\_config](structbt__hci__cp__le__cs__remove__config.md) |
| struct | [bt\_hci\_evt\_inquiry\_complete](structbt__hci__evt__inquiry__complete.md) |
| struct | [bt\_hci\_evt\_conn\_complete](structbt__hci__evt__conn__complete.md) |
| struct | [bt\_hci\_evt\_conn\_request](structbt__hci__evt__conn__request.md) |
| struct | [bt\_hci\_evt\_disconn\_complete](structbt__hci__evt__disconn__complete.md) |
| struct | [bt\_hci\_evt\_auth\_complete](structbt__hci__evt__auth__complete.md) |
| struct | [bt\_hci\_evt\_remote\_name\_req\_complete](structbt__hci__evt__remote__name__req__complete.md) |
| struct | [bt\_hci\_evt\_encrypt\_change](structbt__hci__evt__encrypt__change.md) |
| struct | [bt\_hci\_evt\_remote\_features](structbt__hci__evt__remote__features.md) |
| struct | [bt\_hci\_evt\_remote\_version\_info](structbt__hci__evt__remote__version__info.md) |
| struct | [bt\_hci\_evt\_cmd\_complete](structbt__hci__evt__cmd__complete.md) |
| struct | [bt\_hci\_evt\_cc\_status](structbt__hci__evt__cc__status.md) |
| struct | [bt\_hci\_evt\_cmd\_status](structbt__hci__evt__cmd__status.md) |
| struct | [bt\_hci\_evt\_hardware\_error](structbt__hci__evt__hardware__error.md) |
| struct | [bt\_hci\_evt\_role\_change](structbt__hci__evt__role__change.md) |
| struct | [bt\_hci\_evt\_num\_completed\_packets](structbt__hci__evt__num__completed__packets.md) |
| struct | [bt\_hci\_evt\_pin\_code\_req](structbt__hci__evt__pin__code__req.md) |
| struct | [bt\_hci\_evt\_link\_key\_req](structbt__hci__evt__link__key__req.md) |
| struct | [bt\_hci\_evt\_link\_key\_notify](structbt__hci__evt__link__key__notify.md) |
| struct | [bt\_hci\_evt\_data\_buf\_overflow](structbt__hci__evt__data__buf__overflow.md) |
| struct | [bt\_hci\_evt\_inquiry\_result\_with\_rssi](structbt__hci__evt__inquiry__result__with__rssi.md) |
| struct | [bt\_hci\_evt\_remote\_ext\_features](structbt__hci__evt__remote__ext__features.md) |
| struct | [bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2](structbt__hci__evt__le__per__adv__sync__established__v2.md) |
| struct | [bt\_hci\_evt\_le\_per\_advertising\_report\_v2](structbt__hci__evt__le__per__advertising__report__v2.md) |
| struct | [bt\_hci\_evt\_le\_past\_received\_v2](structbt__hci__evt__le__past__received__v2.md) |
| struct | [bt\_hci\_evt\_le\_per\_adv\_subevent\_data\_request](structbt__hci__evt__le__per__adv__subevent__data__request.md) |
| struct | [bt\_hci\_evt\_le\_per\_adv\_response](structbt__hci__evt__le__per__adv__response.md) |
| struct | [bt\_hci\_evt\_le\_per\_adv\_response\_report](structbt__hci__evt__le__per__adv__response__report.md) |
| struct | [bt\_hci\_evt\_le\_enh\_conn\_complete\_v2](structbt__hci__evt__le__enh__conn__complete__v2.md) |
| struct | [bt\_hci\_evt\_sync\_conn\_complete](structbt__hci__evt__sync__conn__complete.md) |
| struct | [bt\_hci\_evt\_extended\_inquiry\_result](structbt__hci__evt__extended__inquiry__result.md) |
| struct | [bt\_hci\_evt\_encrypt\_key\_refresh\_complete](structbt__hci__evt__encrypt__key__refresh__complete.md) |
| struct | [bt\_hci\_evt\_io\_capa\_req](structbt__hci__evt__io__capa__req.md) |
| struct | [bt\_hci\_evt\_io\_capa\_resp](structbt__hci__evt__io__capa__resp.md) |
| struct | [bt\_hci\_evt\_user\_confirm\_req](structbt__hci__evt__user__confirm__req.md) |
| struct | [bt\_hci\_evt\_user\_passkey\_req](structbt__hci__evt__user__passkey__req.md) |
| struct | [bt\_hci\_evt\_ssp\_complete](structbt__hci__evt__ssp__complete.md) |
| struct | [bt\_hci\_evt\_user\_passkey\_notify](structbt__hci__evt__user__passkey__notify.md) |
| struct | [bt\_hci\_evt\_le\_meta\_event](structbt__hci__evt__le__meta__event.md) |
| struct | [bt\_hci\_evt\_auth\_payload\_timeout\_exp](structbt__hci__evt__auth__payload__timeout__exp.md) |
| struct | [bt\_hci\_evt\_le\_conn\_complete](structbt__hci__evt__le__conn__complete.md) |
| struct | [bt\_hci\_evt\_le\_advertising\_info](structbt__hci__evt__le__advertising__info.md) |
| struct | [bt\_hci\_evt\_le\_advertising\_report](structbt__hci__evt__le__advertising__report.md) |
| struct | [bt\_hci\_evt\_le\_conn\_update\_complete](structbt__hci__evt__le__conn__update__complete.md) |
| struct | [bt\_hci\_evt\_le\_remote\_feat\_complete](structbt__hci__evt__le__remote__feat__complete.md) |
| struct | [bt\_hci\_evt\_le\_ltk\_request](structbt__hci__evt__le__ltk__request.md) |
| struct | [bt\_hci\_evt\_le\_conn\_param\_req](structbt__hci__evt__le__conn__param__req.md) |
| struct | [bt\_hci\_evt\_le\_data\_len\_change](structbt__hci__evt__le__data__len__change.md) |
| struct | [bt\_hci\_evt\_le\_p256\_public\_key\_complete](structbt__hci__evt__le__p256__public__key__complete.md) |
| struct | [bt\_hci\_evt\_le\_generate\_dhkey\_complete](structbt__hci__evt__le__generate__dhkey__complete.md) |
| struct | [bt\_hci\_evt\_le\_enh\_conn\_complete](structbt__hci__evt__le__enh__conn__complete.md) |
| struct | [bt\_hci\_evt\_le\_direct\_adv\_info](structbt__hci__evt__le__direct__adv__info.md) |
| struct | [bt\_hci\_evt\_le\_direct\_adv\_report](structbt__hci__evt__le__direct__adv__report.md) |
| struct | [bt\_hci\_evt\_le\_phy\_update\_complete](structbt__hci__evt__le__phy__update__complete.md) |
| struct | [bt\_hci\_evt\_le\_ext\_advertising\_info](structbt__hci__evt__le__ext__advertising__info.md) |
| struct | [bt\_hci\_evt\_le\_ext\_advertising\_report](structbt__hci__evt__le__ext__advertising__report.md) |
| struct | [bt\_hci\_evt\_le\_per\_adv\_sync\_established](structbt__hci__evt__le__per__adv__sync__established.md) |
| struct | [bt\_hci\_evt\_le\_per\_advertising\_report](structbt__hci__evt__le__per__advertising__report.md) |
| struct | [bt\_hci\_evt\_le\_per\_adv\_sync\_lost](structbt__hci__evt__le__per__adv__sync__lost.md) |
| struct | [bt\_hci\_evt\_le\_adv\_set\_terminated](structbt__hci__evt__le__adv__set__terminated.md) |
| struct | [bt\_hci\_evt\_le\_scan\_req\_received](structbt__hci__evt__le__scan__req__received.md) |
| struct | [bt\_hci\_evt\_le\_chan\_sel\_algo](structbt__hci__evt__le__chan__sel__algo.md) |
| struct | [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) |
| struct | [bt\_hci\_evt\_le\_connectionless\_iq\_report](structbt__hci__evt__le__connectionless__iq__report.md) |
| struct | [bt\_hci\_evt\_le\_connection\_iq\_report](structbt__hci__evt__le__connection__iq__report.md) |
| struct | [bt\_hci\_evt\_le\_cte\_req\_failed](structbt__hci__evt__le__cte__req__failed.md) |
| struct | [bt\_hci\_evt\_le\_past\_received](structbt__hci__evt__le__past__received.md) |
| struct | [bt\_hci\_evt\_le\_cis\_established](structbt__hci__evt__le__cis__established.md) |
| struct | [bt\_hci\_evt\_le\_cis\_req](structbt__hci__evt__le__cis__req.md) |
| struct | [bt\_hci\_evt\_le\_big\_complete](structbt__hci__evt__le__big__complete.md) |
| struct | [bt\_hci\_evt\_le\_big\_terminate](structbt__hci__evt__le__big__terminate.md) |
| struct | [bt\_hci\_evt\_le\_big\_sync\_established](structbt__hci__evt__le__big__sync__established.md) |
| struct | [bt\_hci\_evt\_le\_big\_sync\_lost](structbt__hci__evt__le__big__sync__lost.md) |
| struct | [bt\_hci\_evt\_le\_req\_peer\_sca\_complete](structbt__hci__evt__le__req__peer__sca__complete.md) |
| struct | [bt\_hci\_evt\_le\_path\_loss\_threshold](structbt__hci__evt__le__path__loss__threshold.md) |
| struct | [bt\_hci\_evt\_le\_transmit\_power\_report](structbt__hci__evt__le__transmit__power__report.md) |
| struct | [bt\_hci\_evt\_le\_biginfo\_adv\_report](structbt__hci__evt__le__biginfo__adv__report.md) |
| struct | [bt\_hci\_evt\_le\_subrate\_change](structbt__hci__evt__le__subrate__change.md) |
| struct | [bt\_hci\_evt\_le\_cis\_established\_v2](structbt__hci__evt__le__cis__established__v2.md) |
| struct | [bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md) |
| struct | [bt\_hci\_evt\_le\_cs\_read\_remote\_fae\_table\_complete](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md) |
| struct | [bt\_hci\_evt\_le\_cs\_security\_enable\_complete](structbt__hci__evt__le__cs__security__enable__complete.md) |
| struct | [bt\_hci\_evt\_le\_cs\_config\_complete](structbt__hci__evt__le__cs__config__complete.md) |
| struct | [bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator](structbt__hci__le__cs__step__data__mode__0__initiator.md) |
|  | Subevent result step data format: Mode 0 Initiator. [More...](structbt__hci__le__cs__step__data__mode__0__initiator.md#details) |
| struct | [bt\_hci\_le\_cs\_step\_data\_mode\_0\_reflector](structbt__hci__le__cs__step__data__mode__0__reflector.md) |
|  | Subevent result step data format: Mode 0 Reflector. [More...](structbt__hci__le__cs__step__data__mode__0__reflector.md#details) |
| struct | [bt\_hci\_le\_cs\_step\_data\_mode\_1](structbt__hci__le__cs__step__data__mode__1.md) |
|  | Subevent result step data format: Mode 1. [More...](structbt__hci__le__cs__step__data__mode__1.md#details) |
| struct | [bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md) |
|  | Subevent result step data format: Mode 1 with sounding sequence RTT support. [More...](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#details) |
| struct | [bt\_hci\_le\_cs\_step\_data\_tone\_info](structbt__hci__le__cs__step__data__tone__info.md) |
|  | Format for per-antenna path step data in modes 2 and 3. [More...](structbt__hci__le__cs__step__data__tone__info.md#details) |
| struct | [bt\_hci\_le\_cs\_step\_data\_mode\_2](structbt__hci__le__cs__step__data__mode__2.md) |
|  | Subevent result step data format: Mode 2. [More...](structbt__hci__le__cs__step__data__mode__2.md#details) |
| struct | [bt\_hci\_le\_cs\_step\_data\_mode\_3](structbt__hci__le__cs__step__data__mode__3.md) |
|  | Subevent result step data format: Mode 3. [More...](structbt__hci__le__cs__step__data__mode__3.md#details) |
| struct | [bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md) |
|  | Subevent result step data format: Mode 3 with sounding sequence RTT support. [More...](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#details) |
| struct | [bt\_hci\_evt\_le\_cs\_subevent\_result\_step](structbt__hci__evt__le__cs__subevent__result__step.md) |
| struct | [bt\_hci\_evt\_le\_cs\_subevent\_result](structbt__hci__evt__le__cs__subevent__result.md) |
| struct | [bt\_hci\_evt\_le\_cs\_subevent\_result\_continue](structbt__hci__evt__le__cs__subevent__result__continue.md) |
| struct | [bt\_hci\_evt\_le\_cs\_test\_end\_complete](structbt__hci__evt__le__cs__test__end__complete.md) |
| struct | [bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete](structbt__hci__evt__le__cs__procedure__enable__complete.md) |

| Macros | |
| --- | --- |
| #define | [BT\_HCI\_H4\_NONE](#a2a578399cd3a1ed875ba2c8a49b8129b)   0x00 /\* None of the known packet types \*/ |
| #define | [BT\_HCI\_H4\_CMD](#a524788ee4d21fe9a4625c35e1756bfe9)   0x01 /\* HCI Command packet \*/ |
| #define | [BT\_HCI\_H4\_ACL](#a17386452bbd60c85959296b6539232bd)   0x02 /\* HCI ACL Data packet \*/ |
| #define | [BT\_HCI\_H4\_SCO](#a9e1c93f187ed5864cebefccea1b3faa2)   0x03 /\* HCI Synchronous Data packet \*/ |
| #define | [BT\_HCI\_H4\_EVT](#a783053bc2846063e50755f1590e81ba8)   0x04 /\* HCI Event packet \*/ |
| #define | [BT\_HCI\_H4\_ISO](#af5e6a53cc7d9619f4ac2ea5bd3256149)   0x05 /\* HCI ISO Data packet \*/ |
| #define | [BT\_HCI\_OWN\_ADDR\_PUBLIC](#a1109fda761e1ef8c6df935cf97fdc646)   0x00 |
| #define | [BT\_HCI\_OWN\_ADDR\_RANDOM](#a8693ea59b948960e627d62785515996e)   0x01 |
| #define | [BT\_HCI\_OWN\_ADDR\_RPA\_OR\_PUBLIC](#a92a5db1ce46bbf3ddeaab4da76bc6685)   0x02 |
| #define | [BT\_HCI\_OWN\_ADDR\_RPA\_OR\_RANDOM](#aec05e679e29fde812e9a066e672405b4)   0x03 |
| #define | [BT\_HCI\_OWN\_ADDR\_RPA\_MASK](#a115907057c92a59a407d261133946b59)   0x02 |
| #define | [BT\_HCI\_PEER\_ADDR\_RPA\_UNRESOLVED](#aebc5bd975899f765afe697ab322db114)   0xfe |
| #define | [BT\_HCI\_PEER\_ADDR\_ANONYMOUS](#a1e6d78149d0990511b2b6dffb617069e)   0xff |
| #define | [BT\_ENC\_KEY\_SIZE\_MIN](#a90a6c0c50f915c347b75ac3ca46996ac)   0x07 |
| #define | [BT\_ENC\_KEY\_SIZE\_MAX](#a4c274cd6947d37bf4f895ca0002c4f63)   0x10 |
| #define | [BT\_HCI\_ADV\_HANDLE\_INVALID](#aa85640ad3a1aa78cf862a5d8b2567fa1)   0xff |
| #define | [BT\_HCI\_SYNC\_HANDLE\_INVALID](#a4e4a6e6bb2dc713de8cb7c12139583ed)   0xffff |
| #define | [BT\_HCI\_PAWR\_SUBEVENT\_MAX](#a98554ced76600577254b4124b27ef8a8)   128 |
| #define | [BT\_HCI\_SCO\_HDR\_SIZE](#acb8daef29a7f5f2d11a169fd10ae0caa)   3 |
| #define | [BT\_HCI\_EVT\_HDR\_SIZE](#a0edb7e700cfa557e7fb8ec44f5eea961)   2 |
| #define | [BT\_ACL\_START\_NO\_FLUSH](#ae8c5ddd450d47b45a310bc979207ebff)   0x00 |
| #define | [BT\_ACL\_CONT](#a0bfb8a0bac96eb223eb8229c1dff9e7d)   0x01 |
| #define | [BT\_ACL\_START](#a49c9728293c37e718c009ad973f6d43e)   0x02 |
| #define | [BT\_ACL\_COMPLETE](#ad6f24425a0818730d2377e159698922b)   0x03 |
| #define | [BT\_ACL\_POINT\_TO\_POINT](#a343e6550f9a24a59c5a08efd2dab16bb)   0x00 |
| #define | [BT\_ACL\_BROADCAST](#a2f9e6232229ae1bed3d835b5f6531a76)   0x01 |
| #define | [BT\_ACL\_HANDLE\_MASK](#a28a9f26ba563e2687856aff39b044039)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(12) |
| #define | [bt\_acl\_handle](#a500341d3485843d85dc034ce6f8a908c)(h) |
| #define | [bt\_acl\_flags](#a499f8647747fd6b7b82d9b3280b4b048)(h) |
| #define | [bt\_acl\_flags\_pb](#ae358e74ce455f11bb134700ec80fe07b)(f) |
| #define | [bt\_acl\_flags\_bc](#a55cfcca3e0a6a7401e57e7430421093e)(f) |
| #define | [bt\_acl\_handle\_pack](#aa08e6239d84ce55153baa41f46814363)(h, f) |
| #define | [BT\_HCI\_ACL\_HDR\_SIZE](#a7418d845532d6b077a9695454fa65bc5)   4 |
| #define | [BT\_ISO\_START](#a9ef86241b4dfb462ec31c855bce4ee28)   0x00 |
| #define | [BT\_ISO\_CONT](#a06c43e91abee990343ece9c22f5a515e)   0x01 |
| #define | [BT\_ISO\_SINGLE](#a1db9801de1c97b2d15cf9d2f0ec2a5f0)   0x02 |
| #define | [BT\_ISO\_END](#ac2da3db69ba73112fff5bf16ef386cb3)   0x03 |
| #define | [bt\_iso\_handle](#adcdb9dd367b64a820a040724c1c42c15)(h) |
| #define | [bt\_iso\_flags](#a54e2f7efc0f22287d65bdd560dd7ec78)(h) |
| #define | [bt\_iso\_flags\_pb](#a7ea328491745f1bde6e2b376c19cc380)(f) |
| #define | [bt\_iso\_flags\_ts](#aed6d45daf19ce7fadc1c8fbcc79c9e8a)(f) |
| #define | [bt\_iso\_pack\_flags](#a9bdbdc6e181731a58ec91d53cdade532)(pb, ts) |
| #define | [bt\_iso\_handle\_pack](#ab96b2d1b49a86ee96b2254b624b2e93f)(h, pb, ts) |
| #define | [bt\_iso\_hdr\_len](#a128d269790ccf3f8dcdeb51f80697ba0)(h) |
| #define | [BT\_ISO\_DATA\_VALID](#a52091a307cca85d8d39fbfe5be6b6179)   0x00 |
| #define | [BT\_ISO\_DATA\_INVALID](#a7149213544fe2ac9e7d3d0fd64ecb271)   0x01 |
| #define | [BT\_ISO\_DATA\_NOP](#ae736b21ff7b99c4bb85df1a3f4bee9cd)   0x02 |
| #define | [bt\_iso\_pkt\_len](#a0d540918a423992f5f244febcc82248a)(h) |
| #define | [bt\_iso\_pkt\_flags](#a6dbade5730a92ea7f85017792939e941)(h) |
| #define | [bt\_iso\_pkt\_len\_pack](#a3683be1ceedbcb97f61483b6fa4344e6)(h, f) |
| #define | [BT\_HCI\_ISO\_SDU\_HDR\_SIZE](#a94b93cd856353f24afee5e4022cdbdb9)   4 |
| #define | [BT\_HCI\_ISO\_SDU\_TS\_HDR\_SIZE](#a22db454317bc89afe092ab9127888441)   8 |
| #define | [BT\_HCI\_ISO\_HDR\_SIZE](#a75c1f5e8a44b034004ecfebdb75ee4be)   4 |
| #define | [BT\_HCI\_CMD\_HDR\_SIZE](#acdf2b6de1459a7492415a8987ad9a896)   3 |
| #define | [BT\_CMD\_TEST](#a7d5bc35e597d03fbc65084b39771cf0b)([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), octet, bit) |
| #define | [BT\_CMD\_LE\_STATES](#ae3aaad5ae408cb8c72a29ff7a8817c21)([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
| #define | [BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, page, octet, bit) |
| #define | [BT\_FEAT\_BREDR](#a5508c481ff6b8fd46f2f2c077aaa90c9)(feat) |
| #define | [BT\_FEAT\_LE](#a8b1df8d6b9e0dfcaa13635588cc3bfe3)(feat) |
| #define | [BT\_FEAT\_EXT\_FEATURES](#ac26ebac4f1641d5ff4484f74579852d7)(feat) |
| #define | [BT\_FEAT\_HOST\_SSP](#af011519b6fb0477ac7f87e5dc98daed0)(feat) |
| #define | [BT\_FEAT\_SC](#a9ecf892ec94af8cbfd2e6c99310b1fa2)(feat) |
| #define | [BT\_FEAT\_LMP\_SCO\_CAPABLE](#a24f24640d9f52adb15336a1b17122346)(feat) |
| #define | [BT\_FEAT\_LMP\_ESCO\_CAPABLE](#a7622a2fc0a65f82a827ab3cc84e4e7c5)(feat) |
| #define | [BT\_FEAT\_HV2\_PKT](#ad59c138e945d7f27d3befc286b679e03)(feat) |
| #define | [BT\_FEAT\_HV3\_PKT](#aed6f11d60161c919b4d2b7eb13f46e47)(feat) |
| #define | [BT\_FEAT\_EV4\_PKT](#ad154d0649e8e90c1102b74cae8327fa7)(feat) |
| #define | [BT\_FEAT\_EV5\_PKT](#a0a6b9afb4673dc852e1a4d8e867003c9)(feat) |
| #define | [BT\_FEAT\_2EV3\_PKT](#a8dbbf37965a9d0ddab5a07f88d7cd7ca)(feat) |
| #define | [BT\_FEAT\_3EV3\_PKT](#a00aec89aa4d1504934e85ec79462b346)(feat) |
| #define | [BT\_FEAT\_3SLOT\_PKT](#a5219ff658b46cf28104a99f089854444)(feat) |
| #define | [BT\_LE\_FEAT\_BIT\_ENC](#abd616dd5af5ed3742be9bae400ded848)   0 |
| #define | [BT\_LE\_FEAT\_BIT\_CONN\_PARAM\_REQ](#ab816048bdd6c1e42b0e458abebb76572)   1 |
| #define | [BT\_LE\_FEAT\_BIT\_EXT\_REJ\_IND](#ae5644021aff31996c09f6edf3ede197c)   2 |
| #define | [BT\_LE\_FEAT\_BIT\_PER\_INIT\_FEAT\_XCHG](#aeaea6ea6595de9e3283fd6063bf7c579)   3 |
| #define | [BT\_LE\_FEAT\_BIT\_PING](#a9b4dc56ef4433b0c0dc74a3d95cf289e)   4 |
| #define | [BT\_LE\_FEAT\_BIT\_DLE](#ac09127210b281e5ee45fbc134df64aa6)   5 |
| #define | [BT\_LE\_FEAT\_BIT\_PRIVACY](#a3c4196c04a73aa537baa845e061e9654)   6 |
| #define | [BT\_LE\_FEAT\_BIT\_EXT\_SCAN](#a8f1fa8948f79bec50373e0342ab0969a)   7 |
| #define | [BT\_LE\_FEAT\_BIT\_PHY\_2M](#afcbc8d664c8e924b777c06ffb4c17315)   8 |
| #define | [BT\_LE\_FEAT\_BIT\_SMI\_TX](#aea19f3c3cdcec054c81c176d5aa5f319)   9 |
| #define | [BT\_LE\_FEAT\_BIT\_SMI\_RX](#a9430a65ea813861b6890252ed4748f19)   10 |
| #define | [BT\_LE\_FEAT\_BIT\_PHY\_CODED](#a800686aa45cf336fbd6efc76b3752959)   11 |
| #define | [BT\_LE\_FEAT\_BIT\_EXT\_ADV](#ae1a0751e7c380117c4e31741712096a4)   12 |
| #define | [BT\_LE\_FEAT\_BIT\_PER\_ADV](#a1ac5bab6d48775b4e63e249b5759a683)   13 |
| #define | [BT\_LE\_FEAT\_BIT\_CHAN\_SEL\_ALGO\_2](#a9120867d6f31465cb5f085b610d5ed70)   14 |
| #define | [BT\_LE\_FEAT\_BIT\_PWR\_CLASS\_1](#a938f823110f31a3a5d034cbe9b9d26eb)   15 |
| #define | [BT\_LE\_FEAT\_BIT\_MIN\_USED\_CHAN\_PROC](#ac8cf36c670ae359ec24e62efb4505758)   16 |
| #define | [BT\_LE\_FEAT\_BIT\_CONN\_CTE\_REQ](#aed34742e8554b830c3b6c4bf04f0e2db)   17 |
| #define | [BT\_LE\_FEAT\_BIT\_CONN\_CTE\_RESP](#aa5279a2ce26decb5856a6b709d0641c9)   18 |
| #define | [BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_TX](#a331e7697a3fdc073abba5dd0ff47346b)   19 |
| #define | [BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_RX](#a6abf01c846a5d637ca98997f6cfc263d)   20 |
| #define | [BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_TX\_AOD](#a41eae1585972ae6792eb1a639c2e3a8e)   21 |
| #define | [BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_RX\_AOA](#a480fc67a1c8a2f36410f285ef0ee36e7)   22 |
| #define | [BT\_LE\_FEAT\_BIT\_RX\_CTE](#a9d9449f1935d6522291eca581f3fa9b0)   23 |
| #define | [BT\_LE\_FEAT\_BIT\_PAST\_SEND](#aa05da01a6a9b9ac26423d6fc2661f3db)   24 |
| #define | [BT\_LE\_FEAT\_BIT\_PAST\_RECV](#a28a862eaf11f8b45237f3b87e4bb15c7)   25 |
| #define | [BT\_LE\_FEAT\_BIT\_SCA\_UPDATE](#a829e9d23a16912bad19448a6c4061e3b)   26 |
| #define | [BT\_LE\_FEAT\_BIT\_REMOTE\_PUB\_KEY\_VALIDATE](#a6d17dd4238ea471daca22f74e3cc3bcb)   27 |
| #define | [BT\_LE\_FEAT\_BIT\_CIS\_CENTRAL](#aa98eed376b6d5263621f14c55d776088)   28 |
| #define | [BT\_LE\_FEAT\_BIT\_CIS\_PERIPHERAL](#a298fde96c2d6376e3333a99f7e03409d)   29 |
| #define | [BT\_LE\_FEAT\_BIT\_ISO\_BROADCASTER](#af08a1ffd734d1c211f38d90b4fe72417)   30 |
| #define | [BT\_LE\_FEAT\_BIT\_SYNC\_RECEIVER](#a2fed771f5611212e48027025e11f7678)   31 |
| #define | [BT\_LE\_FEAT\_BIT\_ISO\_CHANNELS](#a0d80ccb33d263abd3b42de1b69cfeeeb)   32 |
| #define | [BT\_LE\_FEAT\_BIT\_PWR\_CTRL\_REQ](#ae58f5260530d1b94608874f5d03d766d)   33 |
| #define | [BT\_LE\_FEAT\_BIT\_PWR\_CHG\_IND](#a0138172a0ed78244d8d3ac9d6936cf85)   34 |
| #define | [BT\_LE\_FEAT\_BIT\_PATH\_LOSS\_MONITOR](#a434fb43b6b3176393f5d22d3932d69fa)   35 |
| #define | [BT\_LE\_FEAT\_BIT\_PER\_ADV\_ADI\_SUPP](#ad5a8221cb25d79b63f1a574699983038)   36 |
| #define | [BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING](#aa45b06a49232372891ceb5e4496d46da)   37 |
| #define | [BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING\_HOST\_SUPP](#adb884a30bc1a24e3dfb115cef7149c81)   38 |
| #define | [BT\_LE\_FEAT\_BIT\_CHANNEL\_CLASSIFICATION](#af2a4be520b4d8c3eb56231b865738e90)   39 |
| #define | [BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL](#a4d920d42e8042c9117f97e334f889f51)   40 |
| #define | [BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL\_HOST](#ad711e7491883e1f1e068fe167cca8a4e)   41 |
| #define | [BT\_LE\_FEAT\_BIT\_PAWR\_ADVERTISER](#af251cb9d905586fd53113f5920038dae)   43 |
| #define | [BT\_LE\_FEAT\_BIT\_PAWR\_SCANNER](#a00bb51972e0db07be84d4f3dfd007cea)   44 |
| #define | [BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING](#ab918084874aace22954aa748333baf6d)   46 |
| #define | [BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING\_HOST](#aa4572a11d78651ce775a010178c6dfa2)   47 |
| #define | [BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, n) |
| #define | [BT\_FEAT\_LE\_ENCR](#a51464aacf5bbcbfb873fa6c757bbcd79)(feat) |
| #define | [BT\_FEAT\_LE\_CONN\_PARAM\_REQ\_PROC](#a554c027fb3946de6f861ea267968ba17)(feat) |
| #define | [BT\_FEAT\_LE\_PER\_INIT\_FEAT\_XCHG](#a132b2561dcd4140458fb612b6e0d8b25)(feat) |
| #define | [BT\_FEAT\_LE\_DLE](#a62e7d152cd9dfabf5b1420945099ecb6)(feat) |
| #define | [BT\_FEAT\_LE\_PHY\_2M](#aaf11993f4938bb4894cdd317f9386fa3)(feat) |
| #define | [BT\_FEAT\_LE\_PHY\_CODED](#abb89a0bebe4046ae310b01dd27e02c99)(feat) |
| #define | [BT\_FEAT\_LE\_PRIVACY](#a0b2781f29085a5807d0b2235c32f5173)(feat) |
| #define | [BT\_FEAT\_LE\_EXT\_ADV](#a8bce94a732d28ce74ad2663e01da09b2)(feat) |
| #define | [BT\_FEAT\_LE\_EXT\_PER\_ADV](#a5d479d919db4920b7a53c054e4ae7a19)(feat) |
| #define | [BT\_FEAT\_LE\_CONNECTION\_CTE\_REQ](#a51316a5b67950e7644dfb71c4c6baa96)(feat) |
| #define | [BT\_FEAT\_LE\_CONNECTION\_CTE\_RESP](#a0cdc67a1345969d3504380fce94a4cda)(feat) |
| #define | [BT\_FEAT\_LE\_CONNECTIONLESS\_CTE\_TX](#a81e30f5630750ce4f805748fbe14b456)(feat) |
| #define | [BT\_FEAT\_LE\_CONNECTIONLESS\_CTE\_RX](#aeb0639a8e5cbc904d7f5c02d72375913)(feat) |
| #define | [BT\_FEAT\_LE\_ANT\_SWITCH\_TX\_AOD](#ae503f9186d39fbea2347036c891fc8bf)(feat) |
| #define | [BT\_FEAT\_LE\_ANT\_SWITCH\_RX\_AOA](#a1c3c0e6a213b71e680ca24738047f09a)(feat) |
| #define | [BT\_FEAT\_LE\_RX\_CTE](#adf4303d47abfab3bd23080c545b77ef7)(feat) |
| #define | [BT\_FEAT\_LE\_PAST\_SEND](#a9e68dcf290273a4a140645c187cd7aee)(feat) |
| #define | [BT\_FEAT\_LE\_PAST\_RECV](#a7a88046c26b3603a2bb8b0f2ee158b5f)(feat) |
| #define | [BT\_FEAT\_LE\_CIS\_CENTRAL](#adce7c3804a224e7b7317728fa27d4945)(feat) |
| #define | [BT\_FEAT\_LE\_CIS\_PERIPHERAL](#a8a6860b285b3b4401021ba16f59404ce)(feat) |
| #define | [BT\_FEAT\_LE\_ISO\_BROADCASTER](#a1c6fd06877a5606ae33aedc45a71f853)(feat) |
| #define | [BT\_FEAT\_LE\_SYNC\_RECEIVER](#af33c8331e204eeee2a7a02e2ad46c7a2)(feat) |
| #define | [BT\_FEAT\_LE\_ISO\_CHANNELS](#a0b24b74715fbf84c2da2dd2cbbb34605)(feat) |
| #define | [BT\_FEAT\_LE\_PWR\_CTRL\_REQ](#a8ab0d3ca572861bb1c40191766481799)(feat) |
| #define | [BT\_FEAT\_LE\_PWR\_CHG\_IND](#a342ce6074faa59b507cf179868e612ba)(feat) |
| #define | [BT\_FEAT\_LE\_PATH\_LOSS\_MONITOR](#a8d771bd34d22853f117dbbd41ef4afe5)(feat) |
| #define | [BT\_FEAT\_LE\_PER\_ADV\_ADI\_SUPP](#a6213deacc8582f14546b23331d41c3a3)(feat) |
| #define | [BT\_FEAT\_LE\_CONN\_SUBRATING](#a75bf595ba1e16deeeedb45a55f470620)(feat) |
| #define | [BT\_FEAT\_LE\_CONN\_SUBRATING\_HOST\_SUPP](#a37adeecbf4c200cf8b060344718e7949)(feat) |
| #define | [BT\_FEAT\_LE\_CHANNEL\_CLASSIFICATION](#abb7763cc16340d23bc7d687e60badcc0)(feat) |
| #define | [BT\_FEAT\_LE\_ADV\_CODING\_SEL](#af10735230c38d2b5a0baf5377212e827)(feat) |
| #define | [BT\_FEAT\_LE\_ADV\_CODING\_SEL\_HOST](#aecf06a32c61c783305ad3817f9e5a596)(feat) |
| #define | [BT\_FEAT\_LE\_PAWR\_ADVERTISER](#ac5d15de2be03bc837afdb33905ea40be)(feat) |
| #define | [BT\_FEAT\_LE\_PAWR\_SCANNER](#a3ee6277e0e4db5e925912e8cb89269fa)(feat) |
| #define | [BT\_FEAT\_LE\_CHANNEL\_SOUNDING](#a7b13b55fd2cfb4d756d3591215b47b7e)(feat) |
| #define | [BT\_FEAT\_LE\_CHANNEL\_SOUNDING\_HOST](#aff2b8ca285698906deecfeff7447a74a)(feat) |
| #define | [BT\_FEAT\_LE\_CIS](#abe5a1ddbede473f583106e3500dccdb1)(feat) |
| #define | [BT\_FEAT\_LE\_BIS](#a46b2f535c74178c8cc9359a7b1d2e140)(feat) |
| #define | [BT\_FEAT\_LE\_ISO](#a7b1b490bf00af8b0bf8ecbf4ef4aaba3)(feat) |
| #define | [BT\_LE\_STATES\_PER\_CONN\_ADV](#abff5a0c6d1f3ab8ecf297d4ef29f7940)(states) |
| #define | [BT\_LE\_STATES\_SCAN\_INIT](#a9871a7d021f9e0bcfda278c82c3731d7)(states) |
| #define | [BT\_HCI\_NO\_BONDING](#ac886a10eed1313f6114fcfc3810a34f0)   0x00 |
| #define | [BT\_HCI\_NO\_BONDING\_MITM](#a89c6d0d285c1c99c51c96d282fe593b9)   0x01 |
| #define | [BT\_HCI\_DEDICATED\_BONDING](#aae1149095ff44d1b749e8b4b4d4aa32f)   0x02 |
| #define | [BT\_HCI\_DEDICATED\_BONDING\_MITM](#aa1361f09852be86296cf91896d8f0853)   0x03 |
| #define | [BT\_HCI\_GENERAL\_BONDING](#ad777455cbcdfe02dd297dee5510e63b4)   0x04 |
| #define | [BT\_HCI\_GENERAL\_BONDING\_MITM](#a5b30ffdf3753d0a2a6c8ab025d32acef)   0x05 |
| #define | [BT\_MITM](#a47ba0b282416c3e8f4275a38b7780b59)   0x01 |
| #define | [BT\_IO\_DISPLAY\_ONLY](#ac656a702e4193044a59cac517099e2cf)   0x00 |
| #define | [BT\_IO\_DISPLAY\_YESNO](#a701d4fa8a4ebc07647f70264ad36153e)   0x01 |
| #define | [BT\_IO\_KEYBOARD\_ONLY](#a5a2a51ccedf3041c42ecdbd69e8c4a68)   0x02 |
| #define | [BT\_IO\_NO\_INPUT\_OUTPUT](#ad68c0057160d5dacae12fce949fdaa32)   0x03 |
| #define | [HCI\_PKT\_TYPE\_HV1](#aecb5b3886467c41baf979d01d8bde4a1)   0x0020 |
| #define | [HCI\_PKT\_TYPE\_HV2](#ae68633ce74639ec6f06d5ef4feee2d09)   0x0040 |
| #define | [HCI\_PKT\_TYPE\_HV3](#aecd04ca27f536a1cb15aacf9ee80aba8)   0x0080 |
| #define | [HCI\_PKT\_TYPE\_SCO\_HV1](#a4b048addd84409867177a97c785c4a73)   0x0001 |
| #define | [HCI\_PKT\_TYPE\_SCO\_HV2](#a98f8217b27c0b9b7817c86520da45018)   0x0002 |
| #define | [HCI\_PKT\_TYPE\_SCO\_HV3](#af67cdc23b6542e6d8323f14e17c7171d)   0x0004 |
| #define | [HCI\_PKT\_TYPE\_ESCO\_EV3](#a9530e916a0cf905e2185cd021320bfff)   0x0008 |
| #define | [HCI\_PKT\_TYPE\_ESCO\_EV4](#a3e0b6a1aa3818cb0c36f7883fd361c7e)   0x0010 |
| #define | [HCI\_PKT\_TYPE\_ESCO\_EV5](#a1f7474cb16a495bd81dc1f23d4103f70)   0x0020 |
| #define | [HCI\_PKT\_TYPE\_ESCO\_2EV3](#a1ccc4d6e5cfc560b7e2cb80c4c386607)   0x0040 |
| #define | [HCI\_PKT\_TYPE\_ESCO\_3EV3](#ac5f09e3db1bc4d697ff705802e9ec3a0)   0x0080 |
| #define | [HCI\_PKT\_TYPE\_ESCO\_2EV5](#a1252be2692bcfb7a1256c63c4deed15d)   0x0100 |
| #define | [HCI\_PKT\_TYPE\_ESCO\_3EV5](#aa45e51b1be89505fe599bc7983fcb950)   0x0200 |
| #define | [ESCO\_PKT\_MASK](#a8afe2c798b2d9657778f0815e3cb11c8) |
| #define | [SCO\_PKT\_MASK](#a1ef7929257a087f340f1f421cd8f51ce) |
| #define | [EDR\_ESCO\_PKT\_MASK](#aa3a50b43beddbd76ae67b71e79a80175) |
| #define | [BT\_HCI\_SCO](#a5e79467b20a9173726c6be86b091e596)   0x00 |
| #define | [BT\_HCI\_ACL](#afee2289cd70b50f888518fd0b6b3f559)   0x01 |
| #define | [BT\_HCI\_ESCO](#a4c57b051b336788e503a8521bb5ada80)   0x02 |
| #define | [BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381)   0x01 |
| #define | [BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)   0x03 |
| #define | [BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e)   0x04 |
| #define | [BT\_OGF\_STATUS](#a5ce14b9103bd538f3610afd80284157e)   0x05 |
| #define | [BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5)   0x08 |
| #define | [BT\_OGF\_VS](#a6b682cb6e4f489ffb67b05280b3dbd65)   0x3f |
| #define | [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)(ogf, ocf) |
| #define | [BT\_OP\_NOP](#a1bf4881fa3237f4a5b22e5fdb417762b)   0x0000 |
| #define | [BT\_OGF](#af3ae81176a4ace13a562262ad53aeae6)(opcode) |
| #define | [BT\_OCF](#ac267cc5384724efba92df0be57379a89)(opcode) |
| #define | [BT\_HCI\_OP\_INQUIRY](#adce48ff5cdde5f4f8ab5bc960717581a)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0001) /\* 0x0401 \*/ |
| #define | [BT\_HCI\_OP\_INQUIRY\_CANCEL](#ae2d4e5e9cbf056bff03a668e74523442)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0002) /\* 0x0402 \*/ |
| #define | [BT\_HCI\_OP\_CONNECT](#addfd3dec2a69e7e5e2634c4fe63769f2)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0005) /\* 0x0405 \*/ |
| #define | [BT\_HCI\_OP\_DISCONNECT](#ab3d8612855550e52a0887e231371fbc2)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0006) /\* 0x0406 \*/ |
| #define | [BT\_HCI\_OP\_CONNECT\_CANCEL](#ac50eb14115129bcc8c47016a6479149d)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0008) /\* 0x0408 \*/ |
| #define | [BT\_HCI\_OP\_ACCEPT\_CONN\_REQ](#af45bed44788b16be1b172c56c33eea34)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0009) /\* 0x0409 \*/ |
| #define | [BT\_HCI\_OP\_SETUP\_SYNC\_CONN](#ac4e12b8f7b89a658da7bbbaf371358e0)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0028) /\* 0x0428 \*/ |
| #define | [BT\_HCI\_OP\_ACCEPT\_SYNC\_CONN\_REQ](#a97976c13fe03d346313bc19489d45360)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0029) /\* 0x0429 \*/ |
| #define | [BT\_HCI\_OP\_REJECT\_CONN\_REQ](#aabb1f800ad4574e0350007af94cd786d)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x000a) /\* 0x040a \*/ |
| #define | [BT\_HCI\_OP\_LINK\_KEY\_REPLY](#a7da489e05d679c00f6cbbca0dfaaf136)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x000b) /\* 0x040b \*/ |
| #define | [BT\_HCI\_OP\_LINK\_KEY\_NEG\_REPLY](#a7db25bd8bdbd4351e0dcef1df8dc7077)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x000c) /\* 0x040c \*/ |
| #define | [BT\_HCI\_OP\_PIN\_CODE\_REPLY](#a7713e5641070ac7fca91e027fc9b8c40)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x000d) /\* 0x040d \*/ |
| #define | [BT\_HCI\_OP\_PIN\_CODE\_NEG\_REPLY](#a5833de4cefd59cee9c614163de7e927b)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x000e) /\* 0x040e \*/ |
| #define | [BT\_HCI\_OP\_AUTH\_REQUESTED](#a4c24e505f9c799275fc2f35619b7df97)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0011) /\* 0x0411 \*/ |
| #define | [BT\_HCI\_OP\_SET\_CONN\_ENCRYPT](#ac32c04cf6bc9de299f0a307dbeed63f3)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0013) /\* 0x0413 \*/ |
| #define | [BT\_HCI\_OP\_REMOTE\_NAME\_REQUEST](#a2e759212d10ecd3a2e975379bf18d374)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0019) /\* 0x0419 \*/ |
| #define | [BT\_HCI\_OP\_REMOTE\_NAME\_CANCEL](#a76f79f4e14396297cc5db4ca8dba0c4c)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x001a) /\* 0x041a \*/ |
| #define | [BT\_HCI\_OP\_READ\_REMOTE\_FEATURES](#ab6282249d4c14412674083007346b005)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x001b) /\* 0x041b \*/ |
| #define | [BT\_HCI\_OP\_READ\_REMOTE\_EXT\_FEATURES](#a87f6747b2b5d52a7886a1ec72100d9d0)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x001c) /\* 0x041c \*/ |
| #define | [BT\_HCI\_OP\_READ\_REMOTE\_VERSION\_INFO](#ae723b797305fe7a370b94d8c865e5708)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x001d) /\* 0x041d \*/ |
| #define | [BT\_HCI\_OP\_IO\_CAPABILITY\_REPLY](#a343a3c5c594dd25483fedf38c304a09a)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x002b) /\* 0x042b \*/ |
| #define | [BT\_HCI\_OP\_USER\_CONFIRM\_REPLY](#ab688441778a4239e1e8f2b2e0b74004f)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x002c) /\* 0x042c \*/ |
| #define | [BT\_HCI\_OP\_USER\_CONFIRM\_NEG\_REPLY](#aecc09326c190d2ab7b89f99375cd39bd)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x002d) /\* 0x042d \*/ |
| #define | [BT\_HCI\_OP\_USER\_PASSKEY\_REPLY](#ad1fce315b731f9978cd52a8c23994a10)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x002e) /\* 0x042e \*/ |
| #define | [BT\_HCI\_OP\_USER\_PASSKEY\_NEG\_REPLY](#a96f9c5c3439d829dfac94cca9ad1f015)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x002f) /\* 0x042f \*/ |
| #define | [BT\_HCI\_OP\_IO\_CAPABILITY\_NEG\_REPLY](#a75d9a0acb6522dd0ae290572c4255540)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0034) /\* 0x0434 \*/ |
| #define | [BT\_HCI\_OP\_SET\_EVENT\_MASK](#abb9bf6d936310a43c4a88244ad12640d)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0001) /\* 0x0c01 \*/ |
| #define | [BT\_HCI\_OP\_RESET](#abb515eb4ea9e66503bf1f375af01a6c0)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0003) /\* 0x0c03 \*/ |
| #define | [BT\_HCI\_OP\_WRITE\_LOCAL\_NAME](#a9b328487dbeeaa587e6f75011441f340)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0013) /\* 0x0c13 \*/ |
| #define | [BT\_HCI\_OP\_READ\_CONN\_ACCEPT\_TIMEOUT](#af302a5e40644307f522154f3803572d0)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0015) /\* 0x0c15 \*/ |
| #define | [BT\_HCI\_OP\_WRITE\_CONN\_ACCEPT\_TIMEOUT](#a6799bd267ef7c19b05ed2dd57baf0393)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0016) /\* 0x0c16 \*/ |
| #define | [BT\_HCI\_OP\_WRITE\_PAGE\_TIMEOUT](#a5ef44fe1cca74a2258ffab1edd04acdf)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0018) /\* 0x0c18 \*/ |
| #define | [BT\_HCI\_OP\_WRITE\_SCAN\_ENABLE](#a0c8b9dc68ec6cd91ec0e9e565701a887)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x001a) /\* 0x0c1a \*/ |
| #define | [BT\_BREDR\_SCAN\_DISABLED](#a19b4c20d243de28462b686088e2971a3)   0x00 |
| #define | [BT\_BREDR\_SCAN\_INQUIRY](#a2f75eaee67bbb6c0211f3146d881278f)   0x01 |
| #define | [BT\_BREDR\_SCAN\_PAGE](#a006d877a26f4e8dd0689b1324107a843)   0x02 |
| #define | [BT\_COD](#aa8793a9bc39bf833124c8c961e441a43)(major\_service, major\_device, minor\_device) |
| #define | [BT\_COD\_VALID](#af2c925e431eec42930101a72b00a7283)(cod) |
| #define | [BT\_COD\_MAJOR\_SERVICE\_CLASSES](#ab598bdad77874748f74187aa32049ea6)(cod) |
| #define | [BT\_COD\_MAJOR\_DEVICE\_CLASS](#a129895b48ad9071017a2e97335ec6d2b)(cod) |
| #define | [BT\_COD\_MINOR\_DEVICE\_CLASS](#adcf892b98d0924ea8a78d4b8b588bddb)(cod) |
| #define | [BT\_COD\_MAJOR\_MISC](#ad14acbda93a611913f675175a433c6e3)   0x00 |
| #define | [BT\_COD\_MAJOR\_COMPUTER](#acdd58e03fb46b783025cfd54d429263b)   0x01 |
| #define | [BT\_COD\_MAJOR\_PHONE](#a59dd55c19cb4d995175a49125529536f)   0x02 |
| #define | [BT\_COD\_MAJOR\_LAN\_NETWORK\_AP](#a81ce79e07c526ae4ef3be26cca65cb2d)   0x03 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO](#ae35a91503887ea73a32342888cc75239)   0x04 |
| #define | [BT\_COD\_MAJOR\_PERIPHERAL](#ad5cf6294b462dd8b1f49c23a93deb267)   0x05 |
| #define | [BT\_COD\_MAJOR\_IMAGING](#a1daeb8de054847bcd5fbee8c5797648c)   0x06 |
| #define | [BT\_COD\_MAJOR\_WEARABLE](#ac5d662f2a86144c1d9698cf0443c9ea7)   0x07 |
| #define | [BT\_COD\_MAJOR\_TOY](#a592ae9ac7a15862b8fa866a2f79d36e8)   0x08 |
| #define | [BT\_COD\_MAJOR\_HEALTH](#a9091627f66847298c6a1f9fa566d261d)   0x09 |
| #define | [BT\_COD\_MAJOR\_UNCATEGORIZED](#ac6cffb2a74393e469b587adc5dfb12b1)   0x1F |
| #define | [BT\_COD\_MAJOR\_COMPUTER\_MINOR\_UNCATEGORIZED](#aec73961628a8ba0ea835b08971d23ce3)   0x00 |
| #define | [BT\_COD\_MAJOR\_COMPUTER\_MINOR\_DESKTOP](#a54cd2fc8881fc63b3784d4267df0cc98)   0x01 |
| #define | [BT\_COD\_MAJOR\_COMPUTER\_MINOR\_SERVER\_CLASS\_COMPUTER](#af247d382b726b0599b706900fe189e4d)   0x02 |
| #define | [BT\_COD\_MAJOR\_COMPUTER\_MINOR\_LAPTOP](#a8655f31e07a18335fa7a3f42635c1352)   0x03 |
| #define | [BT\_COD\_MAJOR\_COMPUTER\_MINOR\_HANDHELD\_PC\_PDA](#ac6b246fe1bb6faf7c5a4d7d1004ad73e)   0x04 |
| #define | [BT\_COD\_MAJOR\_COMPUTER\_MINOR\_PALM\_SIZE\_PC\_PDA](#a0d44dc3f155861fa6e1ea8620d957e97)   0x05 |
| #define | [BT\_COD\_MAJOR\_COMPUTER\_MINOR\_WEARABLE\_COMPUTER](#a4a02b61073979297d275c16302d1452f)   0x06 |
| #define | [BT\_COD\_MAJOR\_COMPUTER\_MINOR\_TABLET](#ac4a3ced7c754169af6fe24f987f80e3a)   0x07 |
| #define | [BT\_COD\_MAJOR\_PHONE\_MINOR\_UNCATEGORIZED](#a70e534fba0ee653a1d8fffc4f57a399d)   0x00 |
| #define | [BT\_COD\_MAJOR\_PHONE\_MINOR\_CELLULAR](#a4954e6760da119f71d91624200b70344)   0x01 |
| #define | [BT\_COD\_MAJOR\_PHONE\_MINOR\_CORDLESS](#ab6dc621f45cd579242a58b523cf250bf)   0x02 |
| #define | [BT\_COD\_MAJOR\_PHONE\_MINOR\_SMARTPHONE](#a3c22870123a8c9015d2664e061bf095a)   0x03 |
| #define | [BT\_COD\_MAJOR\_PHONE\_MINOR\_WIRED\_MODEM\_VOICE\_GATEWAY](#a7f2801f76561e04801c8cd7bc0de3cc1)   0x04 |
| #define | [BT\_COD\_MAJOR\_PHONE\_MINOR\_ISDN](#a4eded4ed6985c8110e040c0a4e3b5341)   0x05 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_UNCATEGORIZED](#a0432846ee3f571d35feba5af70b1b0af)   0x00 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_WEARABLE\_HEADSET](#a56c2a8e3602b53fce244faafd4101af4)   0x01 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_HANDS\_FREE](#a7eff517cf71309181024f9eb7babb277)   0x02 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_RFU](#a50941bdf421209a7bd41b5e225c8a8ed)   0x03 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_MICROPHONE](#ac586986c21d07748bf92e4ade2cb857c)   0x04 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_LOUDSPEAKER](#a54790088ccbeca72e3a41cd559f1c994)   0x05 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_HEADPHONES](#ab93463c966352ee2b246003edad18924)   0x06 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_PORTABLE\_AUDIO](#a516cf67e162628fa7e8ab15c85aa50a1)   0x07 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_CAR\_AUDIO](#a9df23b6e094f75de44fdc6e072d07ed6)   0x08 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_SET\_TOP\_BOX](#a28db3d9daf698fcb382b417532a53652)   0x09 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_HIFI\_AUDIO](#a0ab46892a2ab50747d8fcec489b8a5c2)   0x0A |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VCR](#a0c0c540721712ba407ea08972420cad6)   0x0B |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_CAMERA](#a0b61e3de9a35c714fc1414f29a2a79c5)   0x0C |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_CAMCORDER](#a1c77c5966d3cb71e827a4e59234240f9)   0x0D |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_MONITOR](#a13af74023c32c24f7baa6249cc538e2c)   0x0E |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_DISPLAY\_LOUDSPEAKER](#a5569a391b209cdb551576392e228dcb0)   0x0F |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_CONFERENCING](#afa9446149a24189fd4192c8b32a5ae97)   0x10 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_RFU2](#a85de6aa2ca223da1ac43ffe57489ac24)   0x11 |
| #define | [BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_GAME\_TOY](#a2ed0612651757c12606bab74ea10d14a)   0x12 |
| #define | [BT\_HCI\_OP\_WRITE\_CLASS\_OF\_DEVICE](#ace988e19fa62bf61654a329acaf99018)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0024) /\* 0x0c24 \*/ |
| #define | [BT\_TX\_POWER\_LEVEL\_CURRENT](#ac1ebc6168b2823aea2af2e2f89ffb6cd)   0x00 |
| #define | [BT\_TX\_POWER\_LEVEL\_MAX](#ad835bc44abee2e174f86cd55ac0338e3)   0x01 |
| #define | [BT\_HCI\_OP\_READ\_TX\_POWER\_LEVEL](#aaac00b7d9f9f96d1438643ee054ab21a)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x002d) /\* 0x0c2d \*/ |
| #define | [BT\_HCI\_LE\_TX\_POWER\_PHY\_1M](#a740a01412d6fad277362634e1854f54b)   0x01 |
| #define | [BT\_HCI\_LE\_TX\_POWER\_PHY\_2M](#aa3eadebe7675de492b01ec117f72d808)   0x02 |
| #define | [BT\_HCI\_LE\_TX\_POWER\_PHY\_CODED\_S8](#a66f2c7c03e65392c3477faddc14d9787)   0x03 |
| #define | [BT\_HCI\_LE\_TX\_POWER\_PHY\_CODED\_S2](#ab2bed6683929c37a3d087dba88309e45)   0x04 |
| #define | [BT\_HCI\_OP\_LE\_ENH\_READ\_TX\_POWER\_LEVEL](#aebd5487b500c54a47a926bb1daa56f5e)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0076) /\* 0x2076 \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_REMOTE\_TX\_POWER\_LEVEL](#ac5bc187df83f28a48ba1f87f84aed54a)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0077) /\* 0x2077 \*/ |
| #define | [BT\_HCI\_LE\_TX\_POWER\_REPORT\_DISABLE](#a46bac5521c33da56df1d06ed7c472a06)   0x00 |
| #define | [BT\_HCI\_LE\_TX\_POWER\_REPORT\_ENABLE](#a31f7372543b6dec580fe464ec011d752)   0x01 |
| #define | [BT\_HCI\_OP\_LE\_SET\_TX\_POWER\_REPORT\_ENABLE](#aec22a58c052e856558b316b4f94f8561)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x007A) /\* 0x207A \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_PATH\_LOSS\_REPORTING\_PARAMETERS](#a48a3e41f8d6598e617d02ebc609911c6)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0078) /\* 0x2078 \*/ |
| #define | [BT\_HCI\_LE\_PATH\_LOSS\_REPORTING\_DISABLE](#a9faae90b3adfcbcdf7da19c631e68a69)   0x00 |
| #define | [BT\_HCI\_LE\_PATH\_LOSS\_REPORTING\_ENABLE](#ab2e698e4ebbb45d9e3db0663ae5e4657)   0x01 |
| #define | [BT\_HCI\_OP\_LE\_SET\_PATH\_LOSS\_REPORTING\_ENABLE](#a09c0d554937de38a7b74661a2820237b)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0079) /\* 0x2079 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_DEFAULT\_SUBRATE](#a05c5f2cb7028e3ae831047e53b767836)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x007D) /\* 0x207D \*/ |
| #define | [BT\_HCI\_OP\_LE\_SUBRATE\_REQUEST](#af6825cfdac02620af56b8c747d1ef308)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x007E) /\* 0x207E \*/ |
| #define | [BT\_HCI\_CTL\_TO\_HOST\_FLOW\_DISABLE](#a252ef06a33818e117fc7f8146413cbd0)   0x00 |
| #define | [BT\_HCI\_CTL\_TO\_HOST\_FLOW\_ENABLE](#a4231ce6514091008191d5843b2c0b452)   0x01 |
| #define | [BT\_HCI\_OP\_SET\_CTL\_TO\_HOST\_FLOW](#abe87fa64cb529d2cfe7ddf4fa045d3b5)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0031) /\* 0x0c31 \*/ |
| #define | [BT\_HCI\_OP\_HOST\_BUFFER\_SIZE](#a2e05f146890ad81be27dca91250bf69d)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0033) /\* 0x0c33 \*/ |
| #define | [BT\_HCI\_OP\_HOST\_NUM\_COMPLETED\_PACKETS](#a6c7afa8e3b324714bc5f8dce9702604d)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0035) /\* 0x0c35 \*/ |
| #define | [BT\_HCI\_OP\_WRITE\_INQUIRY\_MODE](#a04985a29d0f131c09aeb9769689b727b)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0045) /\* 0x0c45 \*/ |
| #define | [BT\_HCI\_OP\_WRITE\_SSP\_MODE](#ac7a73c5e38a2308d56f0dbaaf0a4795b)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0056) /\* 0x0c56 \*/ |
| #define | [BT\_HCI\_OP\_SET\_EVENT\_MASK\_PAGE\_2](#af5d2954950e00dfd5a69fc19db0fe530)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0063) /\* 0x0c63 \*/ |
| #define | [BT\_HCI\_OP\_LE\_WRITE\_LE\_HOST\_SUPP](#a2afc45fe32acff87265d36865c8d0b17)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x006d) /\* 0x0c6d \*/ |
| #define | [BT\_HCI\_OP\_WRITE\_SC\_HOST\_SUPP](#a0480dd89b0f851d0a791b97138b01a5b)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x007a) /\* 0x0c7a \*/ |
| #define | [BT\_HCI\_OP\_READ\_AUTH\_PAYLOAD\_TIMEOUT](#a0ea6134bcd33e24b068f35d080cdc4e0)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x007b) /\* 0x0c7b \*/ |
| #define | [BT\_HCI\_OP\_WRITE\_AUTH\_PAYLOAD\_TIMEOUT](#ae74450b7b643f947fa2e83a80e0e2fae)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x007c) /\* 0x0c7c \*/ |
| #define | [BT\_HCI\_OP\_CONFIGURE\_DATA\_PATH](#abc80a803d0e540541bcd889772e59940)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0083) /\* 0x0c83 \*/ |
| #define | [BT\_HCI\_VERSION\_1\_0B](#a4947ee8a84f7cd81e242ee812b5b8760)   0 |
| #define | [BT\_HCI\_VERSION\_1\_1](#a0fac5f104d8ab1539e84a900aafa9e43)   1 |
| #define | [BT\_HCI\_VERSION\_1\_2](#afe6fd8249a97d3762fe454bfb7eab021)   2 |
| #define | [BT\_HCI\_VERSION\_2\_0](#afc0d24e2ba5e6b992aec81104cbf035e)   3 |
| #define | [BT\_HCI\_VERSION\_2\_1](#a98d73e8f548d5ae7eddff91a3e647aae)   4 |
| #define | [BT\_HCI\_VERSION\_3\_0](#acaf91cc6895552243c5b85c2fc007db5)   5 |
| #define | [BT\_HCI\_VERSION\_4\_0](#aeb77e725323c3f31c90482e676dad08a)   6 |
| #define | [BT\_HCI\_VERSION\_4\_1](#a08cca779ede398a551359efccdaf3090)   7 |
| #define | [BT\_HCI\_VERSION\_4\_2](#aa398d6e6fcca0b427a2ccd3a0a343835)   8 |
| #define | [BT\_HCI\_VERSION\_5\_0](#a9a203a5a633d28c644b30125d437701a)   9 |
| #define | [BT\_HCI\_VERSION\_5\_1](#acfa0dbddfde8ee82b114dd34ff75c5bc)   10 |
| #define | [BT\_HCI\_VERSION\_5\_2](#aa4828a916c53d97de0541992d0359c09)   11 |
| #define | [BT\_HCI\_VERSION\_5\_3](#a37b04f40e68e821a1aac3b785903b379)   12 |
| #define | [BT\_HCI\_VERSION\_5\_4](#ae8eadab2b7be415160f145bd63bae367)   13 |
| #define | [BT\_HCI\_VERSION\_6\_0](#a66f6fbbc23991a16aa8bcfa2998f025f)   14 |
| #define | [BT\_HCI\_OP\_READ\_LOCAL\_VERSION\_INFO](#a195b8faf6d7d3e4f1b528185c73b4d67)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x0001) /\* 0x1001 \*/ |
| #define | [BT\_HCI\_OP\_READ\_SUPPORTED\_COMMANDS](#ac0d7533d221db0fa44cfb83135dfcc6a)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x0002) /\* 0x1002 \*/ |
| #define | [BT\_HCI\_OP\_READ\_LOCAL\_EXT\_FEATURES](#a882f120b35a9baa2f70bc33ef5ced6d3)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x0004) /\* 0x1004 \*/ |
| #define | [BT\_HCI\_OP\_READ\_LOCAL\_FEATURES](#a8524505dff48ceb41c008c8662da6408)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x0003) /\* 0x1003 \*/ |
| #define | [BT\_HCI\_OP\_READ\_BUFFER\_SIZE](#acd5d9ecda744969d4692e6ebface2e53)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x0005) /\* 0x1005 \*/ |
| #define | [BT\_HCI\_OP\_READ\_BD\_ADDR](#a4ba1bf2078ac12686e2a7727f637f70b)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x0009) /\* 0x1009 \*/ |
| #define | [BT\_HCI\_CODEC\_TRANSPORT\_MASK\_BREDR\_ACL](#a89eeffc2f46c776ecdb5eea81cb1f47a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_CODEC\_TRANSPORT\_MASK\_BREDR\_SCO](#ab50b70f27bd9beb4da6fe8d4b91398c1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_CODEC\_TRANSPORT\_MASK\_LE\_CIS](#a38dd1118554de13f3f6f2853900212c5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_CODEC\_TRANSPORT\_MASK\_LE\_BIS](#a7d90fc1df2260a4067c3eb4ab169c406)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_BREDR\_ACL](#a73dfca6788b272380e6920d2907bf43f)   0x00 |
| #define | [BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_BREDR\_SCO](#ad10d8c5ffd49cb183731a9ba97c0e058)   0x01 |
| #define | [BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_LE\_CIS](#a5e53f28cedf59f18ce8d494f16933b3c)   0x02 |
| #define | [BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_LE\_BIS](#a560cb22e5f39c144e3d477eea5c32beb)   0x03 |
| #define | [BT\_HCI\_DATAPATH\_DIR\_HOST\_TO\_CTLR](#a0f74c19fabbcb3088e1a819d33a05a1c)   0x00 |
| #define | [BT\_HCI\_DATAPATH\_DIR\_CTLR\_TO\_HOST](#af8d89c712a3d27f9b6f92a31bea2a8c3)   0x01 |
| #define | [BT\_HCI\_DATAPATH\_ID\_HCI](#a5f748cb264265b9fc12f146ba47fa14c)   0x00 |
| #define | [BT\_HCI\_DATAPATH\_ID\_VS](#a0382b1713c7b2a774a8f004b6d1bc33f)   0x01 |
| #define | [BT\_HCI\_DATAPATH\_ID\_VS\_END](#abf755f2839b36a3ac3431bff04193b2f)   0xfe |
| #define | [BT\_HCI\_CODING\_FORMAT\_ULAW\_LOG](#a4f4939e7fa43ab73861f64d25b6549d8)   0x00 |
| #define | [BT\_HCI\_CODING\_FORMAT\_ALAW\_LOG](#a36f18d10467a580e9864eb8629b8ce01)   0x01 |
| #define | [BT\_HCI\_CODING\_FORMAT\_CVSD](#a80dc369e54038df30f44ca4c13ee14d6)   0x02 |
| #define | [BT\_HCI\_CODING\_FORMAT\_TRANSPARENT](#ad93af498e2265c180a01055eca2a4de0)   0x03 |
| #define | [BT\_HCI\_CODING\_FORMAT\_LINEAR\_PCM](#a2630de3f8cc3ccc3d81f0f2fa4084587)   0x04 |
| #define | [BT\_HCI\_CODING\_FORMAT\_MSBC](#a9178f80b7783c9cffb4574667d3033af)   0x05 |
| #define | [BT\_HCI\_CODING\_FORMAT\_LC3](#a1fa62d6f28ef56ebe9c18d5ab86fbf8e)   0x06 |
| #define | [BT\_HCI\_CODING\_FORMAT\_G729A](#a405e22871772b5155f99774178e4093d)   0x07 |
| #define | [BT\_HCI\_CODING\_FORMAT\_VS](#a46839c453b81e80fb8e578f89dc31864)   0xFF |
| #define | [BT\_HCI\_OP\_READ\_CODECS](#a8755487f4672f196051cc513894e4603)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x000b) /\* 0x100b \*/ |
| #define | [BT\_HCI\_OP\_READ\_CODECS\_V2](#acb09b1a94453c1c341decabc029bbc04)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x000d) /\* 0x100d \*/ |
| #define | [BT\_HCI\_OP\_READ\_CODEC\_CAPABILITIES](#a4b9e24d16cd92ce6ee1d6444410cfb43)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x000e) /\* 0x100e \*/ |
| #define | [BT\_HCI\_OP\_READ\_CTLR\_DELAY](#a9a183b26d18453d5daa6de2dcbe4d9a1)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x000f) /\* 0x100f \*/ |
| #define | [BT\_HCI\_OP\_READ\_RSSI](#a528902591490d9d20a6966a042254b3a)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_STATUS](#a5ce14b9103bd538f3610afd80284157e), 0x0005) /\* 0x1405 \*/ |
| #define | [BT\_HCI\_ENCRYPTION\_KEY\_SIZE\_MIN](#ab4eedd90a583b3893c77f51aee16e3c0)   7 |
| #define | [BT\_HCI\_ENCRYPTION\_KEY\_SIZE\_MAX](#ae4271fbdb039750aceac7c0712d4f3db)   16 |
| #define | [BT\_HCI\_OP\_READ\_ENCRYPTION\_KEY\_SIZE](#adefeb2117010fa2d53937ce513e28a18)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_STATUS](#a5ce14b9103bd538f3610afd80284157e), 0x0008) /\* 0x1408 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_EVENT\_MASK](#aa9a3688473bf15c8845f52a3128362f7)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0001) /\* 0x2001 \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_BUFFER\_SIZE](#a965e30fec3f9b5956bd2ea38e57b8b00)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0002) /\* 0x2002 \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_LOCAL\_FEATURES](#ae4e1d6098793b91ee0e4974886b98336)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0003) /\* 0x2003 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_RANDOM\_ADDRESS](#af34eced252d01bbc27bd8e19ed4dc80e)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0005) /\* 0x2005 \*/ |
| #define | [BT\_HCI\_ADV\_IND](#a338499e51470b8910e9f663be8f55db5)   0x00 |
| #define | [BT\_HCI\_ADV\_DIRECT\_IND](#afaecb8d6be1b1c0ce98db7edd8bad343)   0x01 |
| #define | [BT\_HCI\_ADV\_SCAN\_IND](#ae94df1ac3bc14f42be1207531872104a)   0x02 |
| #define | [BT\_HCI\_ADV\_NONCONN\_IND](#a48e13ce185bf9612455c49484ff80bb9)   0x03 |
| #define | [BT\_HCI\_ADV\_DIRECT\_IND\_LOW\_DUTY](#a67c1c0c5349b2de661030138185d7b0d)   0x04 |
| #define | [BT\_HCI\_ADV\_SCAN\_RSP](#afb3e678c87b81f9348749f1c5721ce26)   0x04 |
| #define | [BT\_LE\_ADV\_INTERVAL\_MIN](#ac89392b0484164812b77360d15d9984b)   0x0020 |
| #define | [BT\_LE\_ADV\_INTERVAL\_MAX](#a6479fb2c964155cfcdd3cc48c3a45618)   0x4000 |
| #define | [BT\_LE\_ADV\_INTERVAL\_DEFAULT](#a607201e55561cdccf34e18ceac0f23b7)   0x0800 |
| #define | [BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_37](#af9652f7d96b61e7cc9f44f3d923bd962)   0x01 |
| #define | [BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_38](#a07c18344ec56b22c8a3e902bc53ba191)   0x02 |
| #define | [BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_39](#a14be9af8f16dcdf70aebf251bcfb52f3)   0x04 |
| #define | [BT\_LE\_ADV\_CHAN\_MAP\_ALL](#af96bfa8c912e66233f64b7cc1844b82e)   0x07 |
| #define | [BT\_LE\_ADV\_FP\_NO\_FILTER](#abc1615c8d22ab64844c3f3394023c1b4)   0x00 |
| #define | [BT\_LE\_ADV\_FP\_FILTER\_SCAN\_REQ](#aba027e2aeacea1040c3b45ccaeb23d3c)   0x01 |
| #define | [BT\_LE\_ADV\_FP\_FILTER\_CONN\_IND](#a5f3d27b78705afc3abff35e353eee9fa)   0x02 |
| #define | [BT\_LE\_ADV\_FP\_FILTER\_BOTH](#a980ff7f9bf7154c7866b5e302a1f2a55)   0x03 |
| #define | [BT\_HCI\_OP\_LE\_SET\_ADV\_PARAM](#a446b6e7a74800ee657f5ddcf1c198d02)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0006) /\* 0x2006 \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_ADV\_CHAN\_TX\_POWER](#afd47d6bbfd4688383aaa6b5014cf0019)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0007) /\* 0x2007 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_ADV\_DATA](#adb8f5236ac1b5eaa4c82d620c78c45aa)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0008) /\* 0x2008 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_SCAN\_RSP\_DATA](#a81718bfe6796648eb5831f3cd03049c8)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0009) /\* 0x2009 \*/ |
| #define | [BT\_HCI\_LE\_ADV\_DISABLE](#ae8361a3ca39019757304034c32391b47)   0x00 |
| #define | [BT\_HCI\_LE\_ADV\_ENABLE](#a6b8140956fbf85bd5aab2f1974b673f9)   0x01 |
| #define | [BT\_HCI\_OP\_LE\_SET\_ADV\_ENABLE](#a5f218883bda0698b5c52fd6a34d5e9f0)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x000a) /\* 0x200a \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_SCAN\_PARAM](#a56db98b00b57fd713f8cedbf34e2f8fa)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x000b) /\* 0x200b \*/ |
| #define | [BT\_HCI\_LE\_SCAN\_PASSIVE](#a2274aacde21083e9633fe59fbff0df87)   0x00 |
| #define | [BT\_HCI\_LE\_SCAN\_ACTIVE](#ac13c2e39ac1e13cf5cd2cfa248a6f316)   0x01 |
| #define | [BT\_HCI\_LE\_SCAN\_FP\_BASIC\_NO\_FILTER](#a278ccd7cfefd1a46f6de843b722f583a)   0x00 |
| #define | [BT\_HCI\_LE\_SCAN\_FP\_BASIC\_FILTER](#ac6f3763ab47d20efee1af16d8d019bf3)   0x01 |
| #define | [BT\_HCI\_LE\_SCAN\_FP\_EXT\_NO\_FILTER](#aed7fa63104bbc551bc0dbfa21e38744a)   0x02 |
| #define | [BT\_HCI\_LE\_SCAN\_FP\_EXT\_FILTER](#a45846e02e2630608b14f62f9b9020f9d)   0x03 |
| #define | [BT\_HCI\_OP\_LE\_SET\_SCAN\_ENABLE](#a894cf6904ec16b11f6d930d72d30fce6)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x000c) /\* 0x200c \*/ |
| #define | [BT\_HCI\_LE\_SCAN\_DISABLE](#a152712b517c9ee0452555408d14bbfa7)   0x00 |
| #define | [BT\_HCI\_LE\_SCAN\_ENABLE](#a6859aeda42fe72b75d5cc1896b7e6afd)   0x01 |
| #define | [BT\_HCI\_LE\_SCAN\_FILTER\_DUP\_DISABLE](#a6fb35a340e8eecd7bc2602ed010aa6c1)   0x00 |
| #define | [BT\_HCI\_LE\_SCAN\_FILTER\_DUP\_ENABLE](#a4c9503d4a13f78a1dc44e087af922793)   0x01 |
| #define | [BT\_HCI\_OP\_LE\_CREATE\_CONN](#aadde6f016c942c7907afddf7b6c94304)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x000d) /\* 0x200d \*/ |
| #define | [BT\_HCI\_LE\_CREATE\_CONN\_FP\_NO\_FILTER](#ae1bd495a90fd902614014e7e1e2f1239)   0x00 |
| #define | [BT\_HCI\_LE\_CREATE\_CONN\_FP\_FILTER](#ac04c2c0020d2972d6df169f39c421c08)   0x01 |
| #define | [BT\_HCI\_OP\_LE\_CREATE\_CONN\_CANCEL](#acacd0832cddc00702da74b4a36e5c825)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x000e) /\* 0x200e \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_FAL\_SIZE](#aeeba2e21bd5e33abbd48fa18f5e252f3)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x000f) /\* 0x200f \*/ |
| #define | [BT\_HCI\_OP\_LE\_CLEAR\_FAL](#a592ce45c74bdabf1b25954b8021a50bb)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0010) /\* 0x2010 \*/ |
| #define | [BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_FAL](#a103c6fada57c61fc3f994f8902f4123c)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0011) /\* 0x2011 \*/ |
| #define | [BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_FAL](#aedbb03b04ed567e54642e42ae758538a)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0012) /\* 0x2012 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CONN\_UPDATE](#ac0c308b64ed89c9b7326982ef04ba6d3)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0013) /\* 0x2013 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_HOST\_CHAN\_CLASSIF](#a6224aab014342d93bcb16c717cd52421)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0014) /\* 0x2014 \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_CHAN\_MAP](#a9040e4b5e719d53cc324faa280a670a4)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0015) /\* 0x2015 \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_REMOTE\_FEATURES](#ac8d5165a3a5d190b8e2d31feb79a17c9)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0016) /\* 0x2016 \*/ |
| #define | [BT\_HCI\_OP\_LE\_ENCRYPT](#a99fdd1dbff627a2f627e7d9eced68326)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0017) /\* 0x2017 \*/ |
| #define | [BT\_HCI\_OP\_LE\_RAND](#ac3af817deaf472dbb2a825fd57b67f42)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0018) /\* 0x2018 \*/ |
| #define | [BT\_HCI\_OP\_LE\_START\_ENCRYPTION](#afececfce5819f1b8555ce47fbde2aa0b)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0019) /\* 0x2019 \*/ |
| #define | [BT\_HCI\_OP\_LE\_LTK\_REQ\_REPLY](#a92050425248585bd1c3873e8593db362)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x001a) /\* 0x201a \*/ |
| #define | [BT\_HCI\_OP\_LE\_LTK\_REQ\_NEG\_REPLY](#ae04bd3c7ff17142f2b47e24accdf6a20)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x001b) /\* 0x201b \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_SUPP\_STATES](#a286869ebde03594d56ecd8bc1aa7c73c)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x001c) /\* 0x201c \*/ |
| #define | [BT\_HCI\_OP\_LE\_RX\_TEST](#abd18c6854a0dc97c451b498816f206e4)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x001d) /\* 0x201d \*/ |
| #define | [BT\_HCI\_TEST\_PKT\_PAYLOAD\_PRBS9](#aa9ce0f2db7b63303a9c61c37d052d7b7)   0x00 |
| #define | [BT\_HCI\_TEST\_PKT\_PAYLOAD\_11110000](#a51d26730c8f4c3c8491b33483bdb9494)   0x01 |
| #define | [BT\_HCI\_TEST\_PKT\_PAYLOAD\_10101010](#aab044752b89bb4493a509580ae8eaf9b)   0x02 |
| #define | [BT\_HCI\_TEST\_PKT\_PAYLOAD\_PRBS15](#a0eb4fcbb3ab6c7d4e2ed87d61c5b30f1)   0x03 |
| #define | [BT\_HCI\_TEST\_PKT\_PAYLOAD\_11111111](#a5008205909cecc994b74c8a1cb1f92af)   0x04 |
| #define | [BT\_HCI\_TEST\_PKT\_PAYLOAD\_00000000](#a1fe8c26f174833a4dccbe192df2c6f7d)   0x05 |
| #define | [BT\_HCI\_TEST\_PKT\_PAYLOAD\_00001111](#a13baca9e4517522c763c25882177a2a7)   0x06 |
| #define | [BT\_HCI\_TEST\_PKT\_PAYLOAD\_01010101](#a8f660f979b14d91abd9423e718921ebb)   0x07 |
| #define | [BT\_HCI\_OP\_LE\_TX\_TEST](#af5fe87cbe280dcf26ddc21952e84e93e)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x001e) /\* 0x201e \*/ |
| #define | [BT\_HCI\_OP\_LE\_TEST\_END](#a7ff8a81ae09ddb0d18f999fe454e41df)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x001f) /\* 0x201f \*/ |
| #define | [BT\_HCI\_OP\_LE\_CONN\_PARAM\_REQ\_REPLY](#a8b824639d31fa9f579e73cf1f1344c85)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0020) /\* 0x2020 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CONN\_PARAM\_REQ\_NEG\_REPLY](#a1fbca6b816791f1967278224f37782c1)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0021) /\* 0x2021 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_DATA\_LEN](#a5aeb49334449851866537ea8703f5ab0)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0022) /\* 0x2022 \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_DEFAULT\_DATA\_LEN](#aa58d9ce08e0f1d4a3e5a2f2b1733a6d2)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0023) /\* 0x2023 \*/ |
| #define | [BT\_HCI\_OP\_LE\_WRITE\_DEFAULT\_DATA\_LEN](#ae344c1ab9af250787b9ed8109ad3cde0)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0024) /\* 0x2024 \*/ |
| #define | [BT\_HCI\_OP\_LE\_P256\_PUBLIC\_KEY](#ab1ff230560c1f7712e23a22eb44f0e69)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0025) /\* 0x2025 \*/ |
| #define | [BT\_HCI\_OP\_LE\_GENERATE\_DHKEY](#af2625fcbc0f29199f1a95dc9fe0f929d)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0026) /\* 0x2026 \*/ |
| #define | [BT\_HCI\_OP\_LE\_GENERATE\_DHKEY\_V2](#aa7bf82632c6df22096210de18902a465)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x005e) /\* 0x205e \*/ |
| #define | [BT\_HCI\_LE\_KEY\_TYPE\_GENERATED](#ac85ab1283cd175fc575ebd98b52b3335)   0x00 |
| #define | [BT\_HCI\_LE\_KEY\_TYPE\_DEBUG](#a71f16c552b14042c00e98ea20c1e03c4)   0x01 |
| #define | [BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_RL](#a735c643e8afa27c4e7f7be9bfb09676a)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0027) /\* 0x2027 \*/ |
| #define | [BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_RL](#ac4c11605a4cd244ec3ffa972295396fa)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0028) /\* 0x2028 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CLEAR\_RL](#a5efab85a3beac1fe3fc5a5294a2b1079)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0029) /\* 0x2029 \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_RL\_SIZE](#a45b38708e807c784bd734ba1f69c7f86)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x002a) /\* 0x202a \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_PEER\_RPA](#a6c605e63bd1633f3423a915cf4db00e8)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x002b) /\* 0x202b \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_LOCAL\_RPA](#af8ec9d3b6889a8530bc5977b8594fea6)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x002c) /\* 0x202c \*/ |
| #define | [BT\_HCI\_ADDR\_RES\_DISABLE](#a017742ee92c9ed7b80b41f339394f1e4)   0x00 |
| #define | [BT\_HCI\_ADDR\_RES\_ENABLE](#a61e677658b5a730b13869ebc0dbbffbe)   0x01 |
| #define | [BT\_HCI\_OP\_LE\_SET\_ADDR\_RES\_ENABLE](#a183431c86b7eb32b7c00e6b3a000f29e)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x002d) /\* 0x202d \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_RPA\_TIMEOUT](#aeabb8438460e694867d855cf7f8e3b31)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x002e) /\* 0x202e \*/ |
| #define | [BT\_HCI\_LE\_MAX\_TX\_OCTETS\_MIN](#a6c731f3c0644818489c146eeca9e3ea8)   0x001B |
| #define | [BT\_HCI\_LE\_MAX\_TX\_OCTETS\_MAX](#aec6c2a321f9700572fe8cf84d8bed238)   0x00FB |
| #define | [BT\_HCI\_LE\_MAX\_RX\_OCTETS\_MIN](#a6c192a213459f5cc7898faa8aa0f5f42)   0x001B |
| #define | [BT\_HCI\_LE\_MAX\_RX\_OCTETS\_MAX](#a72d22456f1eb112a75b91faa40e3b776)   0x00FB |
| #define | [BT\_HCI\_LE\_MAX\_TX\_TIME\_MIN](#ac7c6251a5342a591ff4c413820125f94)   0x0148 |
| #define | [BT\_HCI\_LE\_MAX\_TX\_TIME\_MAX](#aae4ce04bdfd0ad339c87eb18616d8a8a)   0x4290 |
| #define | [BT\_HCI\_LE\_MAX\_RX\_TIME\_MIN](#a6666cbeff0cb43fa4c820ba92311fc11)   0x0148 |
| #define | [BT\_HCI\_LE\_MAX\_RX\_TIME\_MAX](#ad4c16d0e80cb6dc2b6fd65e72e331173)   0x4290 |
| #define | [BT\_HCI\_OP\_LE\_READ\_MAX\_DATA\_LEN](#aafb5872650d77d9f4c6ae43038ef2bf1)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x002f) /\* 0x202f \*/ |
| #define | [BT\_HCI\_LE\_PHY\_1M](#a833ae32a3a5ffefbe57c7aa9cdf2e5a9)   0x01 |
| #define | [BT\_HCI\_LE\_PHY\_2M](#a727a1780d5f3754a78dea0476c2b97bb)   0x02 |
| #define | [BT\_HCI\_LE\_PHY\_CODED](#ac5173dfe471fe4d1aad0f7d79904e46a)   0x03 |
| #define | [BT\_HCI\_OP\_LE\_READ\_PHY](#ad2e063f4522a64ceeb36c1d95835e74e)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0030) /\* 0x2030 \*/ |
| #define | [BT\_HCI\_LE\_PHY\_TX\_ANY](#a7656d3400ccb540e8bd066cf1232c38e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_PHY\_RX\_ANY](#a0fb6efaf47f2d676eb51b3fb99d0a691)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_PHY\_PREFER\_1M](#a8101f257838639b46dcd0d50a92bba0c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_PHY\_PREFER\_2M](#ae89ffa7723482ced707f8a57febce629)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_PHY\_PREFER\_CODED](#ab33fde130c9fdb99559b15455e827a7a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_OP\_LE\_SET\_DEFAULT\_PHY](#aaa4e3fd27b4157a617a5fb6817bc1881)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0031) /\* 0x2031 \*/ |
| #define | [BT\_HCI\_LE\_PHY\_CODED\_ANY](#a61909ce217268c8cc6274f16d3db8484)   0x00 |
| #define | [BT\_HCI\_LE\_PHY\_CODED\_S2](#a54bf26868903f0178b0f9f70111ea6b7)   0x01 |
| #define | [BT\_HCI\_LE\_PHY\_CODED\_S8](#abe28c39a93e86d9ad5e6f0c08b09ef9c)   0x02 |
| #define | [BT\_HCI\_OP\_LE\_SET\_PHY](#a1d21c4ffe4db8caafa374a9138e179fa)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0032) /\* 0x2032 \*/ |
| #define | [BT\_HCI\_LE\_MOD\_INDEX\_STANDARD](#a631e672ab64e36a983d4d3aae789b237)   0x00 |
| #define | [BT\_HCI\_LE\_MOD\_INDEX\_STABLE](#a423acd131760a1ab7b0671c45c9214ca)   0x01 |
| #define | [BT\_HCI\_LE\_RX\_PHY\_1M](#a27c179b4c8e85f840b41c4765613c99b)   0x01 |
| #define | [BT\_HCI\_LE\_RX\_PHY\_2M](#ac1db92b615a94b30e587a87d3637ad47)   0x02 |
| #define | [BT\_HCI\_LE\_RX\_PHY\_CODED](#a689bc0f95a315c18ee4efbc556d31d60)   0x03 |
| #define | [BT\_HCI\_OP\_LE\_ENH\_RX\_TEST](#a51c3637712a8701ae7fee16806f677df)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0033) /\* 0x2033 \*/ |
| #define | [BT\_HCI\_LE\_TX\_PHY\_1M](#a0cb0c8d33e23ff6e59241c88b9e5adee)   0x01 |
| #define | [BT\_HCI\_LE\_TX\_PHY\_2M](#a7de4598ca06439f89772f0e72306ac3c)   0x02 |
| #define | [BT\_HCI\_LE\_TX\_PHY\_CODED\_S8](#a01d96d9e7bb61db9b3cd31d161b0abf4)   0x03 |
| #define | [BT\_HCI\_LE\_TX\_PHY\_CODED\_S2](#a599195b97f069412e112df470bf2b536)   0x04 |
| #define | [BT\_HCI\_OP\_LE\_ENH\_TX\_TEST](#a903b1ce0bfe7df7de86bae5fb143e88f)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0034) /\* 0x2034 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_ADV\_SET\_RANDOM\_ADDR](#ac96cefff0857a4d19025a2d9dec8333e)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0035) /\* 0x2035 \*/ |
| #define | [BT\_HCI\_LE\_ADV\_PROP\_CONN](#ac9597c1c284e23578352a23bd66c9fad)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_ADV\_PROP\_SCAN](#ab886c4c7f33adf396ca3e09d0f38995d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_ADV\_PROP\_DIRECT](#acd154c93af2dc866cfe8bcf8e370dd3d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_ADV\_PROP\_HI\_DC\_CONN](#a0fb43dd85c3671420029027cbfbf8c11)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [BT\_HCI\_LE\_ADV\_PROP\_LEGACY](#a936310de47af573e0d1d5d9401097ba1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [BT\_HCI\_LE\_ADV\_PROP\_ANON](#a21c60f21a4de9136accc32b0a8a0325c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [BT\_HCI\_LE\_ADV\_PROP\_TX\_POWER](#abd14685442f2fe315a095516464fc92d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [BT\_HCI\_LE\_PRIM\_ADV\_INTERVAL\_MIN](#a1599475c6673d4fa0e00d16024df9a3b)   0x000020 |
| #define | [BT\_HCI\_LE\_PRIM\_ADV\_INTERVAL\_MAX](#a5b394658223fd700fa152c4deb2f956e)   0xFFFFFF |
| #define | [BT\_HCI\_LE\_ADV\_SCAN\_REQ\_ENABLE](#a39fa8033dcf14aa43dfad7cabc1cb429)   1 |
| #define | [BT\_HCI\_LE\_ADV\_SCAN\_REQ\_DISABLE](#aa1f4b7ba3b48ea6bd7b8a34a7b831a25)   0 |
| #define | [BT\_HCI\_LE\_ADV\_TX\_POWER\_NO\_PREF](#a7f4fcc517033a4743ded39503b35ce29)   0x7F |
| #define | [BT\_HCI\_LE\_ADV\_HANDLE\_MAX](#a12d97417fa11a07b0af5370b595e9a17)   0xEF |
| #define | [BT\_HCI\_LE\_EXT\_ADV\_SID\_INVALID](#a973c2e0fc4cb22d58c47865b9e76b940)   0xFF |
| #define | [BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_PARAM](#a098efdd7908adafd26b8e3f63508c476)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0036) /\* 0x2036 \*/ |
| #define | [BT\_HCI\_LE\_ADV\_PHY\_OPTION\_NO\_REQUIRED](#a2ba70856f1e7fe8c6e7990ac9cdf5aaa)   0x00 |
| #define | [BT\_HCI\_LE\_ADV\_PHY\_OPTION\_REQUIRE\_S2](#ac707220fea6b3fc077b8b85267ed0030)   0x03 |
| #define | [BT\_HCI\_LE\_ADV\_PHY\_OPTION\_REQUIRE\_S8](#aab845a49577d93974b468187c948beff)   0x04 |
| #define | [BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_PARAM\_V2](#a66ffb876e588d64ce2b2d9091de94806)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x007F) /\* 0x207F \*/ |
| #define | [BT\_HCI\_LE\_EXT\_ADV\_OP\_INTERM\_FRAG](#a68c62ac99c4198dbadf6563e40ce33cb)   0x00 |
| #define | [BT\_HCI\_LE\_EXT\_ADV\_OP\_FIRST\_FRAG](#a65b3ae46e1164815cda1325e55df4091)   0x01 |
| #define | [BT\_HCI\_LE\_EXT\_ADV\_OP\_LAST\_FRAG](#aade6b8cac66aee356c857fcfae17ce65)   0x02 |
| #define | [BT\_HCI\_LE\_EXT\_ADV\_OP\_COMPLETE\_DATA](#a5394a0dbcd3856ffb8c63440d352120b)   0x03 |
| #define | [BT\_HCI\_LE\_EXT\_ADV\_OP\_UNCHANGED\_DATA](#a2860ae578d2332a1c76c7bfaa0714e08)   0x04 |
| #define | [BT\_HCI\_LE\_EXT\_ADV\_FRAG\_ENABLED](#aa1dbb6b62c021501320865ac77b5d6da)   0x00 |
| #define | [BT\_HCI\_LE\_EXT\_ADV\_FRAG\_DISABLED](#a4d9626f1b9f0601708b3c38386b5f85c)   0x01 |
| #define | [BT\_HCI\_LE\_EXT\_ADV\_FRAG\_MAX\_LEN](#a3b3f91c046b0656d489c228d75c8b3ff)   251 |
| #define | [BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_DATA](#a563769ae57bb58be9d7ee8e92019cb99)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0037) /\* 0x2037 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_RSP\_DATA](#a586395798b3d827ab17634287862ef54)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0038) /\* 0x2038 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_ENABLE](#a99e9573f9bd290fb18f82a327ca55ecd)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0039) /\* 0x2039 \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_MAX\_ADV\_DATA\_LEN](#a0246ea11fada7570bf59e73250b49b95)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x003a) /\* 0x203a \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_NUM\_ADV\_SETS](#a8d2a855322d0aa454ed00e1458cf9a38)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x003b) /\* 0x203b \*/ |
| #define | [BT\_HCI\_OP\_LE\_REMOVE\_ADV\_SET](#ae802afd7081a39f062f65e5c0994a9e4)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x003c) /\* 0x203c \*/ |
| #define | [BT\_HCI\_OP\_CLEAR\_ADV\_SETS](#a2f95e881ffcda381d8d8ad7ba8705e7d)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x003d) /\* 0x203d \*/ |
| #define | [BT\_HCI\_LE\_PER\_ADV\_INTERVAL\_MIN](#a04f870ac03c1baca22ab5d984354f3bf)   0x0006 |
| #define | [BT\_HCI\_LE\_PER\_ADV\_INTERVAL\_MAX](#a2f2216a88cf77ccac1c9a2f6c5820746)   0xFFFF |
| #define | [BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_PARAM](#a3a111d29fd682fa825f4f9c8c358243f)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x003e) /\* 0x203e \*/ |
| #define | [BT\_HCI\_LE\_PER\_ADV\_OP\_INTERM\_FRAG](#aa18edf54edfb8d0fcaca5941e8e5e493)   0x00 |
| #define | [BT\_HCI\_LE\_PER\_ADV\_OP\_FIRST\_FRAG](#a8aeb4c76ec769879fc4796fc2919c459)   0x01 |
| #define | [BT\_HCI\_LE\_PER\_ADV\_OP\_LAST\_FRAG](#a7f2314472ccb051e87d1bb2f9b3fded8)   0x02 |
| #define | [BT\_HCI\_LE\_PER\_ADV\_OP\_COMPLETE\_DATA](#ada39c45c3c1c7576d4d9794dad115e61)   0x03 |
| #define | [BT\_HCI\_LE\_PER\_ADV\_FRAG\_MAX\_LEN](#a7b3cd7870ba4af2ff483a831d2700466)   252 |
| #define | [BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_DATA](#ae6611e7b72b057ac9d4004a1772fe435)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x003f) /\* 0x203f \*/ |
| #define | [BT\_HCI\_LE\_SET\_PER\_ADV\_ENABLE\_ENABLE](#a1c03932d8c1e2c5436eaf45be093b4d4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_SET\_PER\_ADV\_ENABLE\_ADI](#aaf9b76b276b5cf7e02bb5e3b0a12ecf6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_ENABLE](#a3ae23554c13b099b50b129462e08afe4)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0040) /\* 0x2040 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_PARAM](#a7b0687c9e1faae997b76ece821338fd7)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0041) /\* 0x2041 \*/ |
| #define | [BT\_HCI\_LE\_EXT\_SCAN\_PHY\_1M](#a0ef6a16a2b042b3e7623210fc5fcd1a0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_EXT\_SCAN\_PHY\_2M](#ad0f0fe21e4e9136e09e0a443a7253759)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_EXT\_SCAN\_PHY\_CODED](#ae15b1ae9e35d060b3a9619d293a7d9ac)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_EXT\_SCAN\_FILTER\_DUP\_ENABLE\_RESET](#ae9ba6da1a01dacc52c6a1a2c84d16948)   0x02 |
| #define | [BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_ENABLE](#af7a8256887657e482084d4ed3810195b)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0042) /\* 0x2042 \*/ |
| #define | [BT\_HCI\_OP\_LE\_EXT\_CREATE\_CONN](#ac498c9cd93b664b5bd2e58982d36d7ad)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0043) /\* 0x2043 \*/ |
| #define | [BT\_HCI\_OP\_LE\_EXT\_CREATE\_CONN\_V2](#a1b6bc4da843ed8d04e0b9571465ffd12)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0085) /\* 0x2085 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_SUBEVENT\_DATA](#a44e729aebc339ada5deb86ad9d350404)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0082) /\* 0x2082 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_RESPONSE\_DATA](#a2be1e66c896dca2022c04164fd94da49)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0083) /\* 0x2083 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_SYNC\_SUBEVENT](#aea7f44f563c109be1676454412757fab)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0084) /\* 0x2084 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_PARAM\_V2](#a1125bfc15404124bf4bd533520be0f77)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0086) /\* 0x2086 \*/ |
| #define | [BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_USE\_LIST](#a490bb7d8cf236e49c60771a95d258247)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_REPORTS\_DISABLED](#a44f11af392e3188e699d8f987cb2f6d6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_FILTER\_DUPLICATE](#a29c5cf397f94af42bdea484fa95a2a78)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_FILTERING](#abb3c8fcfc0b48cf6dbebff206a2a9a48)   0 |
| #define | [BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOA](#a64c7e74877c8ca638217a09d503e742b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOD\_1US](#ad349244f13388a7437651e5c3909bcb9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOD\_2US](#aae32740df5a3096a9b17b9c06e6cc3e9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_CTE](#a5532c8ee93198eb831c12b182e13a534)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ONLY\_CTE](#aa3b526ab2ed1aeaab0e26a5390b3dcea)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ALLOWED\_BITS](#a4c884821e7136f6f68bc4d92b394381a)   5 |
| #define | [BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_INVALID\_VALUE](#a6ad9e08bcef788c32481756f76df6a43)   (~[BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)([BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ALLOWED\_BITS](#a4c884821e7136f6f68bc4d92b394381a))) |
| #define | [BT\_HCI\_OP\_LE\_PER\_ADV\_CREATE\_SYNC](#a589c2da26ce325d5cb45726c772cf7ab)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0044) /\* 0x2044 \*/ |
| #define | [BT\_HCI\_OP\_LE\_PER\_ADV\_CREATE\_SYNC\_CANCEL](#a3803042099104029f5b49536cb769e6c)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0045) /\* 0x2045 \*/ |
| #define | [BT\_HCI\_OP\_LE\_PER\_ADV\_TERMINATE\_SYNC](#a57b7b3cab371b4dd230343dfbc5a5e98)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0046) /\* 0x2046 \*/ |
| #define | [BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_PER\_ADV\_LIST](#a393378ba85552bb5f41475a863ca649f)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0047) /\* 0x2047 \*/ |
| #define | [BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_PER\_ADV\_LIST](#a8545e1ede192257a4383eea6b2e932b7)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0048) /\* 0x2048 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CLEAR\_PER\_ADV\_LIST](#affcd4a54d0b26d7b07e39157f17167b4)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0049) /\* 0x2049 \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_PER\_ADV\_LIST\_SIZE](#a3e2fd45c015809e131ac6b3f6a9c72fc)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x004a) /\* 0x204a \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_TX\_POWER](#a77d132306109474465575369db342dbd)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x004b) /\* 0x204b \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_RF\_PATH\_COMP](#a6c454d3276f7eaae542b13becad6482c)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x004c) /\* 0x204c \*/ |
| #define | [BT\_HCI\_OP\_LE\_WRITE\_RF\_PATH\_COMP](#a766b66d1fc7df1d8924d060217de9b9b)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x004d) /\* 0x204d \*/ |
| #define | [BT\_HCI\_LE\_PRIVACY\_MODE\_NETWORK](#a423b143e474548458b8bcce59029f722)   0x00 |
| #define | [BT\_HCI\_LE\_PRIVACY\_MODE\_DEVICE](#ae61d38e84e0d58be45ffaf521abad2f6)   0x01 |
| #define | [BT\_HCI\_OP\_LE\_SET\_PRIVACY\_MODE](#a7e1fad2d353904bb345f3a1579c98576)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x004e) /\* 0x204e \*/ |
| #define | [BT\_HCI\_LE\_TEST\_CTE\_DISABLED](#a6764be57300c8dac30a058ebf8387159)   0x00 |
| #define | [BT\_HCI\_LE\_TEST\_CTE\_TYPE\_ANY](#a1f45696f06d7bc3f4cc8393bd6967286)   0x00 |
| #define | [BT\_HCI\_LE\_TEST\_SLOT\_DURATION\_ANY](#ac4ac180578ed3f662d91c43b5c6b6b53)   0x00 |
| #define | [BT\_HCI\_LE\_TEST\_SWITCH\_PATTERN\_LEN\_ANY](#aef669f8887a165b4948eb651c91968c1)   0x00 |
| #define | [BT\_HCI\_OP\_LE\_RX\_TEST\_V3](#abe1567f7cf83148b3f2214b6e0787da0)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x004f) /\* 0x204f \*/ |
| #define | [BT\_HCI\_OP\_LE\_TX\_TEST\_V3](#ad570a3edcefcf927e5253805e1d3d4e4)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0050) /\* 0x2050 \*/ |
| #define | [BT\_HCI\_LE\_CTE\_LEN\_MIN](#a80376d34b4d701d5f6092aa101ce0e6c)   0x2 |
| #define | [BT\_HCI\_LE\_CTE\_LEN\_MAX](#acdfe03ade99fa88779b68e435aea23e3)   0x14 |
| #define | [BT\_HCI\_LE\_AOA\_CTE](#a9b3306f29525c50cd8bd501f7391e518)   0x0 |
| #define | [BT\_HCI\_LE\_AOD\_CTE\_1US](#a8569e960c44660eb41cdccbe5aeb6ead)   0x1 |
| #define | [BT\_HCI\_LE\_AOD\_CTE\_2US](#a970732caa95f5742fc18c91efbc7095b)   0x2 |
| #define | [BT\_HCI\_LE\_NO\_CTE](#aeee9fd73771de54542f7ff24f95eceba)   0xFF |
| #define | [BT\_HCI\_LE\_CTE\_COUNT\_MIN](#aec2a77fadbb6bf24267d659a84b7c9a9)   0x1 |
| #define | [BT\_HCI\_LE\_CTE\_COUNT\_MAX](#a442df4f693ae5bb75d1d8f54fe204bda)   0x10 |
| #define | [BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_TX\_PARAMS](#a900509c6e7485b44de09a43555225ce8)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0051) /\* 0x2051 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_TX\_ENABLE](#a5527fd8badb977f2ef061ba76468ccf3)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0052) /\* 0x2052 \*/ |
| #define | [BT\_HCI\_LE\_ANTENNA\_SWITCHING\_SLOT\_1US](#a1410330e31701a140eb8c0c73c943972)   0x1 |
| #define | [BT\_HCI\_LE\_ANTENNA\_SWITCHING\_SLOT\_2US](#afa70fe0b1b9e277bfcb6bf7d6fc03564)   0x2 |
| #define | [BT\_HCI\_LE\_SAMPLE\_CTE\_ALL](#a85450acad700f8cef375d34235752650)   0x0 |
| #define | [BT\_HCI\_LE\_SAMPLE\_CTE\_COUNT\_MIN](#afd22fac7ff6d5006015159ffc978798a)   0x1 |
| #define | [BT\_HCI\_LE\_SAMPLE\_CTE\_COUNT\_MAX](#a0c8888c4dfed6ab4c0f07a37ca3b2278)   0x10 |
| #define | [BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_SAMPLING\_ENABLE](#a728b9a505c9a2f719424bd277f7e8765)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0053) /\* 0x2053 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_CONN\_CTE\_RX\_PARAMS](#a8a079c51fc7c37f29afeda663206c59e)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0054) /\* 0x2054 \*/ |
| #define | [BT\_HCI\_LE\_AOA\_CTE\_RSP](#ac80b68b1ca4f55a8a44b6bf0dfa7bfb3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_AOD\_CTE\_RSP\_1US](#a124137512b0f87a67fff694359d629d0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_AOD\_CTE\_RSP\_2US](#a5c1dd462d05e4a5615f80402f892ecbc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_SWITCH\_PATTERN\_LEN\_MIN](#ad74e54836996fc3d02fbb245f9c72b5a)   0x2 |
| #define | [BT\_HCI\_LE\_SWITCH\_PATTERN\_LEN\_MAX](#ad6bdc84c282a4e35ded32687cba94e9f)   0x4B |
| #define | [BT\_HCI\_OP\_LE\_SET\_CONN\_CTE\_TX\_PARAMS](#af4110be6e09c80cd7362d9b2580243e7)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0055) /\* 0x2055 \*/ |
| #define | [BT\_HCI\_REQUEST\_CTE\_ONCE](#ad9e1fa26a799b8730c17772482da7982)   0x0 |
| #define | [BT\_HCI\_REQUEST\_CTE\_INTERVAL\_MIN](#a13875ad8ac3a77759afdb4b6a76ad3e8)   0x1 |
| #define | [BT\_HCI\_REQUEST\_CTE\_INTERVAL\_MAX](#a0a41f911f5f4b50b571c7f091393c7d8)   0xFFFF |
| #define | [BT\_HCI\_OP\_LE\_CONN\_CTE\_REQ\_ENABLE](#ae488ce598705cf60b78da985015bb42b)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0056) /\* 0x2056 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CONN\_CTE\_RSP\_ENABLE](#a150b54d69fb6fe9175336fadb7d81bb8)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0057) /\* 0x2057 \*/ |
| #define | [BT\_HCI\_LE\_1US\_AOD\_TX](#a41aac54cd90cfc58990ce93124ce7077)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_1US\_AOD\_RX](#a70edcf0bd7e63454996ef5d925e91bbf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_1US\_AOA\_RX](#a04a69a823bac190d0ac16f3c21481bde)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_NUM\_ANT\_MIN](#a112d3fb3d3ec663278aa4463fedbd89b)   0x1 |
| #define | [BT\_HCI\_LE\_NUM\_ANT\_MAX](#ad9ff685b2854b877e0cdd1ae93272ddf)   0x4B |
| #define | [BT\_HCI\_LE\_MAX\_SWITCH\_PATTERN\_LEN\_MIN](#a327330c5b69e8ec56dd18fcc3fdf0622)   0x2 |
| #define | [BT\_HCI\_LE\_MAX\_SWITCH\_PATTERN\_LEN\_MAX](#a647de996dd2e75a8242e6459abd565f6)   0x4B |
| #define | [BT\_HCI\_LE\_MAX\_CTE\_LEN\_MIN](#adee7271e25e6d66ba434502ab56674c3)   0x2 |
| #define | [BT\_HCI\_LE\_MAX\_CTE\_LEN\_MAX](#af54ba281111d90f3edb77c0abf9c57b1)   0x14 |
| #define | [BT\_HCI\_OP\_LE\_READ\_ANT\_INFO](#aff3ea5f19135609d5553cacec0d700a6)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0058) /\* 0x2058 \*/ |
| #define | [BT\_HCI\_LE\_SET\_PER\_ADV\_RECV\_ENABLE\_ENABLE](#a1aaaffb3044bfd824aa6744867da0a97)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_SET\_PER\_ADV\_RECV\_ENABLE\_FILTER\_DUPLICATE](#a08fe0a16e8c1b3eb6b23869b37739f2d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_RECV\_ENABLE](#a047efb565b182e90178513dc3db6390f)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0059) /\* 0x2059 \*/ |
| #define | [BT\_HCI\_OP\_LE\_PER\_ADV\_SYNC\_TRANSFER](#aa1d0bc8ccc0e1e8835938f8e8d87b7f1)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x005a) /\* 0x205a \*/ |
| #define | [BT\_HCI\_OP\_LE\_PER\_ADV\_SET\_INFO\_TRANSFER](#ab7d661097af4cc612ac6631b18bbc7e3)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x005b) /\* 0x205b \*/ |
| #define | [BT\_HCI\_LE\_PAST\_MODE\_NO\_SYNC](#a65ff1c4a937422000f6f1eadea28ccba)   0x00 |
| #define | [BT\_HCI\_LE\_PAST\_MODE\_NO\_REPORTS](#ac7233f9c34f5e33d765b68b55ebc9b9e)   0x01 |
| #define | [BT\_HCI\_LE\_PAST\_MODE\_SYNC](#aaeac19606d3d5e7d0906b38e2c4b4c69)   0x02 |
| #define | [BT\_HCI\_LE\_PAST\_MODE\_SYNC\_FILTER\_DUPLICATES](#ab0232a2abc2b7c86b19ae89298ef8c4b)   0x03 |
| #define | [BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOA](#a3a3937965aeb187b6fb18da3b7731ed7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOD\_1US](#a440aca4bf97bc6b583284ae6c8037a53)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOD\_2US](#ae2d9be5e54595cb5a426ae8909cdee1c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_CTE](#af3d8cf0fb8af60c057ba8c24abaf3897)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [BT\_HCI\_LE\_PAST\_CTE\_TYPE\_ONLY\_CTE](#a6fca2634e0e5b0dd5d86b18666ed38e4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [BT\_HCI\_OP\_LE\_PAST\_PARAM](#a177ec628eac4a7d535cfe6c07123cb34)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x005c) /\* 0x205c \*/ |
| #define | [BT\_HCI\_OP\_LE\_DEFAULT\_PAST\_PARAM](#a650fe2941ffe238b16fd99ed5e78b25a)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x005d) /\* 0x205d \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_BUFFER\_SIZE\_V2](#aa7e78541d152c21e101fab5a094c972f)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0060) /\* 0x2060 \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_ISO\_TX\_SYNC](#acb7f49f17a60a4e29270c8719b7aeeed)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0061) /\* 0x2061 \*/ |
| #define | [BT\_HCI\_ISO\_CIG\_ID\_MAX](#a18b5fef3eb5b947ce328e17c1e7db02d)   0xFE |
| #define | [BT\_HCI\_ISO\_CIS\_COUNT\_MAX](#a26c78a4b760b97682269e66dfe6f99df)   0x1F |
| #define | [BT\_HCI\_ISO\_SDU\_INTERVAL\_MIN](#a12e9af0e72013649da8afc7aa70a4e9c)   0x0000FF |
| #define | [BT\_HCI\_ISO\_SDU\_INTERVAL\_MAX](#aa75800427e808756fc7c6d30da57de37)   0x0FFFFF |
| #define | [BT\_HCI\_ISO\_WORST\_CASE\_SCA\_VALID\_MASK](#a49f62e83dd51d17efd77c89337fdd537)   0x07 |
| #define | [BT\_HCI\_ISO\_PACKING\_VALID\_MASK](#aecaa88e04025e575c9bcda093f027400)   0x01 |
| #define | [BT\_HCI\_ISO\_FRAMING\_VALID\_MASK](#aaf4b4fc224c8b5cfdca663250eb29350)   0x01 |
| #define | [BT\_HCI\_ISO\_MAX\_TRANSPORT\_LATENCY\_MIN](#a8d044df1bfab8381b7e334597b303588)   0x0005 |
| #define | [BT\_HCI\_ISO\_MAX\_TRANSPORT\_LATENCY\_MAX](#a9794f59f8d28879753b39bd504cf55be)   0x0FA0 |
| #define | [BT\_HCI\_ISO\_CIS\_ID\_VALID\_MAX](#a11e614cc72adb58bda2a2bdd5f4b36ef)   0xEF |
| #define | [BT\_HCI\_ISO\_MAX\_SDU\_VALID\_MASK](#a9f3e990cadf1be179fcbac3f8ef74efe)   0x0FFF |
| #define | [BT\_HCI\_ISO\_PHY\_VALID\_MASK](#ae055ed9714ca23bebd48bb399af04d83)   0x07 |
| #define | [BT\_HCI\_ISO\_INTERVAL\_MIN](#a9d5e85ae1380fa85bae9d7e5e67aa0ae)   0x0004 |
| #define | [BT\_HCI\_ISO\_INTERVAL\_MAX](#aaadbec2cc6adc2bb14d7117396023d06)   0x0C80 |
| #define | [BT\_HCI\_OP\_LE\_SET\_CIG\_PARAMS](#a0a4b2732026a6300d4b354eb6d93905d)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0062) /\* 0x2062 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_CIG\_PARAMS\_TEST](#a54df2d12a0c07bab9fb3521dc69ff2f4)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0063) /\* 0x2063 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CREATE\_CIS](#a63c9af35a55d9b1ed1b253d057657608)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0064) /\* 0x2064 \*/ |
| #define | [BT\_HCI\_OP\_LE\_REMOVE\_CIG](#ab623f680f2031fc03bd73199ebbf4e4e)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0065) /\* 0x2065 \*/ |
| #define | [BT\_HCI\_OP\_LE\_ACCEPT\_CIS](#ade7635c85588941a2e628639be06ce7b)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0066) /\* 0x2066 \*/ |
| #define | [BT\_HCI\_OP\_LE\_REJECT\_CIS](#a6c58ebc2082de8c2c3aafd9ee77dfd11)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0067) /\* 0x2067 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CREATE\_BIG](#a2a57bb6089e3a064e62119188b555ba9)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0068) /\* 0x2068 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CREATE\_BIG\_TEST](#ad0f1ae4be3f5bb90ef967d88dcaaf353)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0069) /\* 0x2069 \*/ |
| #define | [BT\_HCI\_OP\_LE\_TERMINATE\_BIG](#acc5e6c17e33cf43f2a68cb93bb09ef20)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x006a) /\* 0x206a \*/ |
| #define | [BT\_HCI\_OP\_LE\_BIG\_CREATE\_SYNC](#a47af328ede7f14e3d78c81de609af1c9)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x006b) /\* 0x206b \*/ |
| #define | [BT\_HCI\_OP\_LE\_BIG\_TERMINATE\_SYNC](#aa7576f4ab30ec7985b4afd08a08800d2)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x006c) /\* 0x206c \*/ |
| #define | [BT\_HCI\_OP\_LE\_REQ\_PEER\_SC](#a0057468b1638b07f799b62a24cd096d9)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x006d) /\* 0x206d \*/ |
| #define | [BT\_HCI\_OP\_LE\_SETUP\_ISO\_PATH](#a97de1164704f5d3c517b9c2ff6b0584a)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x006e) /\* 0x206e \*/ |
| #define | [BT\_HCI\_OP\_LE\_REMOVE\_ISO\_PATH](#addec65d76f67f07c029216435cf117c6)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x006f) /\* 0x206f \*/ |
| #define | [BT\_HCI\_ISO\_TEST\_ZERO\_SIZE\_SDU](#aa857bdd2e81c923ab540761986074557)   0 |
| #define | [BT\_HCI\_ISO\_TEST\_VARIABLE\_SIZE\_SDU](#aed9e2581c74218e023100d63201721af)   1 |
| #define | [BT\_HCI\_ISO\_TEST\_MAX\_SIZE\_SDU](#af5c0bf9fd20df7b4a4cdb7ce18fdc7fc)   2 |
| #define | [BT\_HCI\_OP\_LE\_ISO\_TRANSMIT\_TEST](#a740f1964df5bdb675906c87ad8ee0cef)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0070) /\* 0x2070 \*/ |
| #define | [BT\_HCI\_OP\_LE\_ISO\_RECEIVE\_TEST](#a467736569f030fbb433000e712f1b08e)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0071) /\* 0x2071 \*/ |
| #define | [BT\_HCI\_OP\_LE\_ISO\_READ\_TEST\_COUNTERS](#a2b988ffc8ffd10ce1dfde377afa699e1)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0072) /\* 0x2072 \*/ |
| #define | [BT\_HCI\_OP\_LE\_ISO\_TEST\_END](#a86436e6b0cb17de95b438f192bbff1d2)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0073) /\* 0x2073 \*/ |
| #define | [BT\_HCI\_OP\_LE\_SET\_HOST\_FEATURE](#a29555bdcc7b439c2d0311fcb0721dc0b)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0074) /\* 0x2074 \*/ |
| #define | [BT\_HCI\_OP\_LE\_READ\_ISO\_LINK\_QUALITY](#acd6367a62d2c80d9f2e796d7b6ab1417)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0075) /\* 0x2075 \*/ |
| #define | [BT\_HCI\_OP\_LE\_TX\_TEST\_V4](#a13827b7d7b656ea02c0620ec7b525f65)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x007B) /\* 0x207B \*/ |
| #define | [BT\_HCI\_TX\_TEST\_POWER\_MIN](#a034d4a4fd8f7d6d324efa820d0b627d1)   -0x7F |
| #define | [BT\_HCI\_TX\_TEST\_POWER\_MAX](#a925dda1fdce843e0bbcdd4acff696440)   0x14 |
| #define | [BT\_HCI\_TX\_TEST\_POWER\_MIN\_SET](#a5d0fc1dbb127ba0a383e4e56bb503334)   0x7E |
| #define | [BT\_HCI\_TX\_TEST\_POWER\_MAX\_SET](#a2e9caac5d12f8df1ce69a54f603500ee)   0x7F |
| #define | [BT\_HCI\_OP\_LE\_CS\_READ\_LOCAL\_SUPPORTED\_CAPABILITIES](#a84e0338551dd8256a821d960bf745208)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0089) /\* 0x2089 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_READ\_REMOTE\_SUPPORTED\_CAPABILITIES](#a4f6dd157a555e06cd028a9097fd7b81a)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x008A) /\* 0x208A \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_WRITE\_CACHED\_REMOTE\_SUPPORTED\_CAPABILITIES](#acdbbe0da013fb3b6da5514498c3932dd)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x008B) /\* 0x208B \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_SECURITY\_ENABLE](#a574168efdaa5729aec9699d48f988d77)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x008C) /\* 0x208C \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_SET\_DEFAULT\_SETTINGS](#addb1ab37dc75ab5389d74c6c96629b02)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x008D) /\* 0x208D \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_INITIATOR\_ROLE\_MASK](#a74aaa5b6b799dad3af6778e23093b230)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_ROLE\_MASK](#a1beb2f602b3635fee272580f0f2f8719)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_OP\_LE\_CS\_MIN\_MAX\_TX\_POWER](#a040315a8ac4f80a2c497919a2fd4d7bc)   -127 |
| #define | [BT\_HCI\_OP\_LE\_CS\_MAX\_MAX\_TX\_POWER](#a29a240b2d3f209b1f5f3d96e380dde08)   20 |
| #define | [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_ONE](#a7fa26323384443ba9c5e635047b74f51)   0x01 |
| #define | [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_TWO](#aa6d146c85e3148a2afb66023d94c2eeb)   0x02 |
| #define | [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_THREE](#a8721a8f4670a8038d66d42adea061f57)   0x03 |
| #define | [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_FOUR](#af0d407f944831f8c85f91fb60f5bc618)   0x04 |
| #define | [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_REP](#afad5b26b2a6ce125b6198856d20bcdd8)   0xFE |
| #define | [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_NONE](#aed2444a40bc79ccf3f383dd961036f5e)   0xFF |
| #define | [BT\_HCI\_OP\_LE\_CS\_READ\_REMOTE\_FAE\_TABLE](#afa7a0214b145891562f1d2b7b16860ab)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x008E) /\* 0x208E \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_WRITE\_CACHED\_REMOTE\_FAE\_TABLE](#a44eb5d70628f6522a08b1327588df979)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x008F) /\* 0x208F \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_SET\_CHANNEL\_CLASSIFICATION](#a880439089735247c7011862d5b3e090f)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0092) /\* 0x2092 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_SET\_PROCEDURE\_PARAMETERS](#ad74850cecd8d8dd8a7878d944abdb411)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0093) /\* 0x2093 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_1M](#a3a8f1c94f40696f18e18810f736497e3)   0x01 |
| #define | [BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_2M](#a016f68a621de8d332f3073df4faf1702)   0x02 |
| #define | [BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S8](#a2543f9fa20db642fb8b47b949c50af6a)   0x03 |
| #define | [BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S2](#a776a14d8e7fdca584475f26b441c8bfb)   0x04 |
| #define | [BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_ENABLE](#a4eddce6558339caba6a3d16f8fe5d485)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0094) /\* 0x2094 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_DISABLED](#a3e01bbe3a72c946015a288ee49d3cbdd)   0x00 |
| #define | [BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_ENABLED](#a4a88120ae7e83fd791012c913315d14f)   0x01 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST](#af09601cffd1adf3f8b623868d8f8a3e9)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0095) /\* 0x2095 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_1](#af1b7924e50ba017e59d697fd8814d491)   0x1 |
| #define | [BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_2](#a714152a085bbc317b539d6e973ccffc6)   0x2 |
| #define | [BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_3](#a5d2af0ed5e0cc5cf7d9f0baae512ff68)   0x3 |
| #define | [BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_1](#a219243d501bbcb6d62668398cde79fca)   0x1 |
| #define | [BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_2](#ada09c787fca0a1d54bb754635489b51e)   0x2 |
| #define | [BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_3](#a4b48c199b6b75e9dd62ec36883b40aa4)   0x3 |
| #define | [BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_UNUSED](#ab3fce1eb448b0ade581e4e12b2d56039)   0xFF |
| #define | [BT\_HCI\_OP\_LE\_CS\_INITIATOR\_ROLE](#a4505bedc3b5aae63b80cf53fc516b342)   0x0 |
| #define | [BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_ROLE](#aeb3715dfcac55a46532f51279e29708c)   0x1 |
| #define | [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_AA\_ONLY](#a759eb7a8e43ee7cf1ea88ddd3e69feb5)   0x0 |
| #define | [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_SOUND](#aa2ae18252a20ef3481d2402f8924cdda)   0x1 |
| #define | [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_SOUND](#a73cbfe2a942b684ac0b5b50d900fb83f)   0x2 |
| #define | [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_RAND](#abe4efee7cf9371129f4b5bd650b0d64a)   0x3 |
| #define | [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_64BIT\_RAND](#a77e56fd5302673f6ef295c0cceabdc9f)   0x4 |
| #define | [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_RAND](#aa60f64ff7259fd79fb1da2c063530348)   0x5 |
| #define | [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_128BIT\_RAND](#a1fe5e94fbd1156c8196c8e1ab9816bac)   0x6 |
| #define | [BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_1M](#a7baf90f5bf691ce6b650677e6c2a9600)   0x1 |
| #define | [BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M](#ae49d35db87532e06ea685a63eb89177a)   0x2 |
| #define | [BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M\_2BT](#ac34716156b071e06eb454f091a63216c)   0x3 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_MINIMIZE\_TX\_POWER](#a500597c78a6ada65d1224960bf6a370f)   0x7E |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_MAXIMIZE\_TX\_POWER](#a50eb827977c0c596cb357ed62a6e80bd)   0x7F |
| #define | [BT\_HCI\_OP\_LE\_CS\_ACI\_0](#a92e1ec21014999f40172fa1812c36575)   0x0 |
| #define | [BT\_HCI\_OP\_LE\_CS\_ACI\_1](#a5b082fa5b8ba11a651468cc516d067fe)   0x1 |
| #define | [BT\_HCI\_OP\_LE\_CS\_ACI\_2](#ab30a4e55002080394c39fb885eba36e4)   0x2 |
| #define | [BT\_HCI\_OP\_LE\_CS\_ACI\_3](#a76d1452003c0bd3b688765aa2d25047f)   0x3 |
| #define | [BT\_HCI\_OP\_LE\_CS\_ACI\_4](#af16c4c79e602e6da833b8aa3e0c4bf64)   0x4 |
| #define | [BT\_HCI\_OP\_LE\_CS\_ACI\_5](#ad980d8f134d940b80dc9b0e3a570ac06)   0x5 |
| #define | [BT\_HCI\_OP\_LE\_CS\_ACI\_6](#a4c7ff3c949023f4544bf50353a0f082b)   0x6 |
| #define | [BT\_HCI\_OP\_LE\_CS\_ACI\_7](#acabccf9f5893324dcb6acc0769ab8417)   0x7 |
| #define | [BT\_HCI\_OP\_LE\_CS\_SNR\_18](#a96b13fb3b363a5436e1b9633f54bb248)   0x0 |
| #define | [BT\_HCI\_OP\_LE\_CS\_SNR\_21](#a4b93a8bceafd49d6ca65816924bb4230)   0x1 |
| #define | [BT\_HCI\_OP\_LE\_CS\_SNR\_24](#a135a4dc2f191d2a931b4270e00774cb2)   0x2 |
| #define | [BT\_HCI\_OP\_LE\_CS\_SNR\_27](#a52eb27d8f726a2ed6859149fcdf2355d)   0x3 |
| #define | [BT\_HCI\_OP\_LE\_CS\_SNR\_30](#a181c2d98b93bd18e9edc11a6f9535331)   0x4 |
| #define | [BT\_HCI\_OP\_LE\_CS\_SNR\_NOT\_USED](#a4aa2e02ce5110be3dc68a801bb583372)   0xFF |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_0\_MASK](#a0a73e0d46b5ca0e94b4bb00d2f79e89d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_2\_MASK](#a2a62cbc191abd177cbf5aea27112fb8b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_3\_MASK](#a560f6f1bddedc60b3a373778bc56b1a7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_4\_MASK](#a36c2c6debe6bf395853112c68a726d25)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_5\_MASK](#a4aca98e213ba81c999c8495310af9320)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_6\_MASK](#afd7b8b4ec0baf526cc4335d26c380b62)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_7\_MASK](#a695d2ba272dbdd2681ab9216d00ca43a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_8\_MASK](#ad92a29871be9aff39802fdea4446ef4b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_10\_MASK](#a90c77fe0022f016453a8eb174b8fcd63)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3B](#a77d27762b9faa7743a55d822a1839eac)   0x0 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3C](#af17f867204bc7cf99e5d530c39302be0)   0x1 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_HAT](#acd33fc2eb3f5ebe10cbe4c5060f8336b)   0x0 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_X](#ad09c735ab352d7a546cade296e915e85)   0x1 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_NONE](#a9ed8967faa3ee3824433422709148330)   0x0 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_INIT](#a0513bf5ca6eb9f43a7e8cecaf943c4d7)   0x1 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REFL](#aa24ae1cf1501de66660051a4a62246df)   0x2 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_BOTH](#ad7a89a9365e20e4cd1e44bdb74ae7ecb)   0x3 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REPEAT](#a50fba6ab75b37ccf39452211ba05e896)   0x4 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_00](#aa4ba4be270035da446389766b795c327)   0x0 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_01](#aa0e9e2081d3cbbb60de9b6dcffe77239)   0x1 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_02](#a762c5efa09e1fba989fdfb0bdcba9b9c)   0x2 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_03](#a2cc7a5d5d2105b1a428703e274cc5388)   0x3 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_04](#a03ffb0ffb8e98b26390575b153471bab)   0x4 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_05](#adbd3820e0ffa5f99e27778217d477010)   0x5 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_06](#a70607449d6bd6207783e319e77d63b16)   0x6 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_07](#acc79a879ea527c2901a8b91dae58d0ed)   0x7 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_08](#a9dfd88863d649182855edc8c268107d6)   0x8 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_09](#ae5a27304aa1cefdfb26ae2cbf42532e3)   0x9 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_10](#a0e9664c52808aa246218f92a4fb55516)   0xA |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_11](#a8fbc80d91e4a1ae04c76cda189cd5d83)   0xB |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_12](#a4c4a44bd33ebf97852e6640b0d510fdd)   0xC |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_13](#a08690b2f762d24c34966b839a6d5e696)   0xD |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_14](#ac2cd3ed1583f86af0480b8481cedca1e)   0xE |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_15](#ab2b0745d98053775e9bf073e36ce5d78)   0xF |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_16](#add2c42aa2583b93b0f98ac33ca61ca9d)   0x10 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_17](#a08db476ea6516691baeb9007b553281d)   0x11 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_18](#a9f0bf05cb0aac50e1df43397c3b913bc)   0x12 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_19](#a5df817bdfefc4de0a1309cf71908a105)   0x13 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_20](#ae64e5a409523b94ef1ce315ed49afed0)   0x14 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_21](#a46f70b5096593956795cc381e33c4aa2)   0x15 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_22](#abe9fa4621e9c004421170b0166ea14e1)   0x16 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_23](#afc41ca64d03a7ed8ea82a641a0217436)   0x17 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_LOOP](#ac9d7cb5a339759b7e0c4ed150a487ca3)   0xFF |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_2\_POSITION\_NOT\_PRESENT](#a1f2bfc1afab1928321c01beddb658f01)   0xFF |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_0011](#a45e1ff56f1a6dcc59b784905e4fc6726)   0x0 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_1100](#a5d3c206a5067ddc5a02a5d5e8c3eb7a3)   0x1 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_LOOP](#a24d2e56f620500905572e786f2523b0e)   0x2 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS9](#a4f922c5e0662adf8471686dfa9b719ec)   0x00 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11110000](#af20dfb1e245afc06a495179d700f126f)   0x01 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_10101010](#ae133ef2939518d660df5322551157d47)   0x02 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS15](#a92bc70a5ad7938a46ac9f2127f1bc2d9)   0x03 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11111111](#aa94eda86c6ffe85a65267f285dae5cb1)   0x04 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00000000](#a04a26b8600cac8c82247a7d51122f600)   0x05 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00001111](#abf19d511680005828add231d64e1e3f0)   0x06 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_01010101](#a53f0ca5604489a38a1367736a5297b45)   0x07 |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_USER](#a94007d8250c3524ad0b86745dbb74b3b)   0x80 |
| #define | [BT\_HCI\_OP\_LE\_CS\_CREATE\_CONFIG](#af26aad0e137782c8f12937b1736d6ada)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0090) /\* 0x2090 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_REMOVE\_CONFIG](#a54116ddaa8338d59b23fb879c185a399)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0091) /\* 0x2091 \*/ |
| #define | [BT\_HCI\_OP\_LE\_CS\_TEST\_END](#a4c45c8b2b33ae857c654cc100b5e5550)   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0096) /\* 0x2096 \*/ |
| #define | [BT\_HCI\_EVT\_UNKNOWN](#a0f44f6e5037d650b9dd0c5f34ba681b5)   0x00 |
| #define | [BT\_HCI\_EVT\_VENDOR](#a955fe06f3fcab82c3370cb621f0dbca0)   0xff |
| #define | [BT\_HCI\_EVT\_INQUIRY\_COMPLETE](#abd8f15d920c0bdb3c68556b4e873f413)   0x01 |
| #define | [BT\_HCI\_EVT\_CONN\_COMPLETE](#a0dd2162851b4a7afc3d96924f69cceca)   0x03 |
| #define | [BT\_HCI\_EVT\_CONN\_REQUEST](#afc473fec33612ffb044d54bad39e8d76)   0x04 |
| #define | [BT\_HCI\_EVT\_DISCONN\_COMPLETE](#a32e5051a114f8987b49c6957c84d60e2)   0x05 |
| #define | [BT\_HCI\_EVT\_AUTH\_COMPLETE](#acc9c74c8406b84baaf55d9452924aaf9)   0x06 |
| #define | [BT\_HCI\_EVT\_REMOTE\_NAME\_REQ\_COMPLETE](#a1a4be9cf628063db2fb821f67c54ea56)   0x07 |
| #define | [BT\_HCI\_EVT\_ENCRYPT\_CHANGE](#a8dee2fc366d0371b68b212ff40e6ea7d)   0x08 |
| #define | [BT\_HCI\_EVT\_REMOTE\_FEATURES](#acbad340a978d4fc118af826d2c1a81e3)   0x0b |
| #define | [BT\_HCI\_EVT\_REMOTE\_VERSION\_INFO](#a18f58c80d213d666ee8309cda8eb0a26)   0x0c |
| #define | [BT\_HCI\_EVT\_CMD\_COMPLETE](#a06f6cf60885ac051cdc9b463fc3b7de7)   0x0e |
| #define | [BT\_HCI\_EVT\_CMD\_STATUS](#a2b35e7484351228243bb3564273c5bff)   0x0f |
| #define | [BT\_HCI\_EVT\_HARDWARE\_ERROR](#a54c3bdd2687d142f925183a46ffc5f8b)   0x10 |
| #define | [BT\_HCI\_EVT\_ROLE\_CHANGE](#a9508e6faf71a345f7ff3d2cec9d85dde)   0x12 |
| #define | [BT\_HCI\_EVT\_NUM\_COMPLETED\_PACKETS](#a883433c60959629a013d34cea21ab88f)   0x13 |
| #define | [BT\_HCI\_EVT\_PIN\_CODE\_REQ](#a8c16e0bdecf9eae58bbd884fb48b0fc2)   0x16 |
| #define | [BT\_HCI\_EVT\_LINK\_KEY\_REQ](#aab60607637f0e1f8e3cbf9f7292ddc57)   0x17 |
| #define | [BT\_LK\_COMBINATION](#a7283a42b1220dd6d56c22cd9cb424e7c)   0x00 |
| #define | [BT\_LK\_LOCAL\_UNIT](#a12ffe67b9e4ec01bbe400a6a3cc5b859)   0x01 |
| #define | [BT\_LK\_REMOTE\_UNIT](#aeb53b797c4fc91a38a459ff5f29d35e1)   0x02 |
| #define | [BT\_LK\_DEBUG\_COMBINATION](#a916e6133d2dadb9aaf5fe42d0c0e1b96)   0x03 |
| #define | [BT\_LK\_UNAUTH\_COMBINATION\_P192](#adfea495d48088eae78491a14730bef31)   0x04 |
| #define | [BT\_LK\_AUTH\_COMBINATION\_P192](#a6630ceb874d343f721931f80ee5fa67e)   0x05 |
| #define | [BT\_LK\_CHANGED\_COMBINATION](#a5753841a02ba0c2fa627d9e96bad045d)   0x06 |
| #define | [BT\_LK\_UNAUTH\_COMBINATION\_P256](#ada18ab581a323eafe8754009ef27d05e)   0x07 |
| #define | [BT\_LK\_AUTH\_COMBINATION\_P256](#aa941cce486c497afa6d03fec326396b9)   0x08 |
| #define | [BT\_HCI\_EVT\_LINK\_KEY\_NOTIFY](#a15578dd8e9d2b16a28ea0b020ac9112b)   0x18 |
| #define | [BT\_OVERFLOW\_LINK\_SYNCH](#a44233b934e33c65af90d03ad301e6b9d)   0x00 |
| #define | [BT\_OVERFLOW\_LINK\_ACL](#a35831810e3a7e2c5446780b14ef7d9c1)   0x01 |
| #define | [BT\_OVERFLOW\_LINK\_ISO](#ad32010743baef10c635d8b08f21c8641)   0x02 |
| #define | [BT\_HCI\_EVT\_DATA\_BUF\_OVERFLOW](#ae747b016101bc9e9614163288c5c0d15)   0x1a |
| #define | [BT\_HCI\_EVT\_INQUIRY\_RESULT\_WITH\_RSSI](#a92243c99484922771d5aca8f98945d29)   0x22 |
| #define | [BT\_HCI\_EVT\_REMOTE\_EXT\_FEATURES](#a092a782ea069c98475a6617241321122)   0x23 |
| #define | [BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_ESTABLISHED\_V2](#a0decb07f1b4ae20b23cffc616dd442e4)   0x24 |
| #define | [BT\_HCI\_EVT\_LE\_PER\_ADVERTISING\_REPORT\_V2](#a8d067bf751953fd8a7bb5421bdc94970)   0x25 |
| #define | [BT\_HCI\_EVT\_LE\_PAST\_RECEIVED\_V2](#a5379a2a0016a2551ac79736924c7ea86)   0x26 |
| #define | [BT\_HCI\_EVT\_LE\_PER\_ADV\_SUBEVENT\_DATA\_REQUEST](#a4395b8b850e9fd3735c2369798f9c226)   0x27 |
| #define | [BT\_HCI\_EVT\_LE\_PER\_ADV\_RESPONSE\_REPORT](#a64e0f465068e72e98904fa6cdc33d3de)   0x28 |
| #define | [BT\_HCI\_EVT\_LE\_ENH\_CONN\_COMPLETE\_V2](#a60ea5e58028aa09c00d20cfff5c942d5)   0x29 |
| #define | [BT\_HCI\_EVT\_SYNC\_CONN\_COMPLETE](#ab77f3074a2236afc1ed773775d17befe)   0x2c |
| #define | [BT\_HCI\_EVT\_EXTENDED\_INQUIRY\_RESULT](#a9b5405de1e07fcefba54b286bd1fdfbe)   0x2f |
| #define | [BT\_HCI\_EVT\_ENCRYPT\_KEY\_REFRESH\_COMPLETE](#aad28cc20cc111ac39e39011932b9d22e)   0x30 |
| #define | [BT\_HCI\_EVT\_IO\_CAPA\_REQ](#a4d69a943660da9c1a6ffedb9b653ce3f)   0x31 |
| #define | [BT\_HCI\_EVT\_IO\_CAPA\_RESP](#a0f5cae40268568e25142eed9e3e5e639)   0x32 |
| #define | [BT\_HCI\_EVT\_USER\_CONFIRM\_REQ](#a78cdb5848d8a12a8cbea17767b3d02aa)   0x33 |
| #define | [BT\_HCI\_EVT\_USER\_PASSKEY\_REQ](#a38a1bce81af39bb28d40e149f9309b69)   0x34 |
| #define | [BT\_HCI\_EVT\_SSP\_COMPLETE](#a7d2ba655c6954f90de04cafafccd727f)   0x36 |
| #define | [BT\_HCI\_EVT\_USER\_PASSKEY\_NOTIFY](#a724d43899b16fcb89c235898a21c13b9)   0x3b |
| #define | [BT\_HCI\_EVT\_LE\_META\_EVENT](#ac1d7f9270323d7fa459e60b372cf998b)   0x3e |
| #define | [BT\_HCI\_EVT\_AUTH\_PAYLOAD\_TIMEOUT\_EXP](#a589975abd5d9532ba16d15ac21c5e81e)   0x57 |
| #define | [BT\_HCI\_ROLE\_CENTRAL](#a150ea8f2095d8510bde3ebd65d521c29)   0x00 |
| #define | [BT\_HCI\_ROLE\_PERIPHERAL](#a9ca37afd4638ef94cdd55302bd4c99b3)   0x01 |
| #define | [BT\_HCI\_EVT\_LE\_CONN\_COMPLETE](#a2c3c4f81903d1860f21880c7c3cfbaa7)   0x01 |
| #define | [BT\_HCI\_LE\_RSSI\_NOT\_AVAILABLE](#a56f7acd075e03694d966d949f637946c)   0x7F |
| #define | [BT\_HCI\_EVT\_LE\_ADVERTISING\_REPORT](#a1a93b78bdbb29982d989aea5eae5ec19)   0x02 |
| #define | [BT\_HCI\_LE\_INTERVAL\_MIN](#adcf6bcefe1d8a34f65597730910bab69)   0x0006 |
|  | All limits according to BT Core Spec v5.4 [Vol 4, Part E]. |
| #define | [BT\_HCI\_LE\_INTERVAL\_MAX](#a23ce5829beb61d9db40fedfce35c368e)   0x0c80 |
| #define | [BT\_HCI\_LE\_PERIPHERAL\_LATENCY\_MAX](#a9af7ce6ecbd978df6193c4e9c2d8b002)   0x01f3 |
| #define | [BT\_HCI\_LE\_SUPERVISON\_TIMEOUT\_MIN](#a03dc93eec388a17c286d50395c683fcb)   0x000a |
| #define | [BT\_HCI\_LE\_SUPERVISON\_TIMEOUT\_MAX](#a2564ee96b802cb887f67e3cc38f8f400)   0x0c80 |
| #define | [BT\_HCI\_EVT\_LE\_CONN\_UPDATE\_COMPLETE](#aeef912e71549d4b5a0d8b293074a909c)   0x03 |
| #define | [BT\_HCI\_EVT\_LE\_REMOTE\_FEAT\_COMPLETE](#a8b1653caabce8474fba132343aa62f56)   0x04 |
| #define | [BT\_HCI\_EVT\_LE\_LTK\_REQUEST](#a9efb73da285829cde0e4c1ac28a48f1a)   0x05 |
| #define | [BT\_HCI\_EVT\_LE\_CONN\_PARAM\_REQ](#a77072c10df87395e7e649307b975fb69)   0x06 |
| #define | [BT\_HCI\_EVT\_LE\_DATA\_LEN\_CHANGE](#a064cf9e32616c6f94041d138a5bf4819)   0x07 |
| #define | [BT\_HCI\_EVT\_LE\_P256\_PUBLIC\_KEY\_COMPLETE](#abe39909eb984dd6edd1220f9c6744546)   0x08 |
| #define | [BT\_HCI\_EVT\_LE\_GENERATE\_DHKEY\_COMPLETE](#a8ab77f497135e365fb9e895dc2d4d453)   0x09 |
| #define | [BT\_HCI\_EVT\_LE\_ENH\_CONN\_COMPLETE](#a292de9ec009a80e23308ead618656b4f)   0x0a |
| #define | [BT\_HCI\_EVT\_LE\_DIRECT\_ADV\_REPORT](#a417144400fd8d7f5c05e050950c75dab)   0x0b |
| #define | [BT\_HCI\_EVT\_LE\_PHY\_UPDATE\_COMPLETE](#a44f18d799280d47ec09376e7cffd4c40)   0x0c |
| #define | [BT\_HCI\_EVT\_LE\_EXT\_ADVERTISING\_REPORT](#ad63fc0c42f0253dfe06b81324a05f505)   0x0d |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_TYPE\_CONN](#ae448216e385d4e1175b92e112c941140)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_TYPE\_SCAN](#a54673fbd23e05fec88e1f6bca6aa70e9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DIRECT](#a1b5738583447011ee63350787236b3b8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_TYPE\_SCAN\_RSP](#a485843f24c09934b1f15d5274b4a56d5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_TYPE\_LEGACY](#a0879fbea8bf3acbe56e25f3693c81ad6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS](#a9557bf3ea41a526fb9d628d2fd3d5bea)(ev\_type) |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_COMPLETE](#a85720f3d88c7fa5da9dc9cdffb94ec87)   0 |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_PARTIAL](#ab7842a3081c9bf5288275b57337955f2)   1 |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_INCOMPLETE](#abf119f5606440c075e61abcbfaa683c6)   2 |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_RX\_FAILED](#ad9bcda2a43eed7e73112f2ef84cc6183)   0xFF |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_PHY\_1M](#a4e3752dfde6a1f6ce6c7561b6c19657c)   0x01 |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_PHY\_2M](#a0eae639d3066358da815743aa7ba2933)   0x02 |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_PHY\_CODED\_S8](#a51fd268794a726f7d9fa2fb4ce937507)   0x03 |
| #define | [BT\_HCI\_LE\_ADV\_EVT\_PHY\_CODED\_S2](#a865ad7eefd0051e7965bd5e391bf852c)   0x04 |
| #define | [BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_ESTABLISHED](#a8c721c9e5df496900f661755aff7cbd6)   0x0e |
| #define | [BT\_HCI\_EVT\_LE\_PER\_ADVERTISING\_REPORT](#a31fc096530a89e63d4967d7ddd85b753)   0x0f |
| #define | [BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_LOST](#ab303042eabbeb133e202bdcfbd38666c)   0x10 |
| #define | [BT\_HCI\_EVT\_LE\_SCAN\_TIMEOUT](#a7234c851946c6025aa850c9bf28faab0)   0x11 |
| #define | [BT\_HCI\_EVT\_LE\_ADV\_SET\_TERMINATED](#a398afcbdb732fe76ec01db1393721ab2)   0x12 |
| #define | [BT\_HCI\_EVT\_LE\_SCAN\_REQ\_RECEIVED](#a0ebf19a602a02c00793b3de64392e514)   0x13 |
| #define | [BT\_HCI\_LE\_CHAN\_SEL\_ALGO\_1](#ac8dcea08127aa5ce2a870d64fcc843f1)   0x00 |
| #define | [BT\_HCI\_LE\_CHAN\_SEL\_ALGO\_2](#a7a4b52643c764233427314732896d353)   0x01 |
| #define | [BT\_HCI\_EVT\_LE\_CHAN\_SEL\_ALGO](#a4f012a8357e5bb17b5dd04128bd39911)   0x14 |
| #define | [BT\_HCI\_LE\_CTE\_CRC\_OK](#ac1ce16d42df9eb71860e51a843dbc943)   0x0 |
| #define | [BT\_HCI\_LE\_CTE\_CRC\_ERR\_CTE\_BASED\_TIME](#a3f787f516c3cc233fc700c08552a4034)   0x1 |
| #define | [BT\_HCI\_LE\_CTE\_CRC\_ERR\_CTE\_BASED\_OTHER](#a478bc1be161e0b1eb05667bc8b6c9ae5)   0x2 |
| #define | [BT\_HCI\_LE\_CTE\_INSUFFICIENT\_RESOURCES](#a3bc1e15287e6173d45b7d1e981d6e90e)   0xFF |
| #define | [B\_HCI\_LE\_CTE\_REPORT\_SAMPLE\_COUNT\_MIN](#a87364c12ecac6b05681469c9450f887e)   0x9 |
| #define | [B\_HCI\_LE\_CTE\_REPORT\_SAMPLE\_COUNT\_MAX](#a9693358ac3b7d9da498ca557fa0d1410)   0x52 |
| #define | [BT\_HCI\_LE\_CTE\_REPORT\_NO\_VALID\_SAMPLE](#a40156c4680916b289b00b1546e0d5bb0)   0x80 |
| #define | [BT\_HCI\_EVT\_LE\_CONNECTIONLESS\_IQ\_REPORT](#a04c4a4567eaad7c592f2181e47768522)   0x15 |
| #define | [BT\_HCI\_EVT\_LE\_CONNECTION\_IQ\_REPORT](#ace41ae5ec2a8f036aabf83ac94937a8b)   0x16 |
| #define | [BT\_HCI\_CTE\_REQ\_STATUS\_RSP\_WITHOUT\_CTE](#a5e0814f9ca6e7fbc78b0778634ff075d)   0x0 |
| #define | [BT\_HCI\_EVT\_LE\_CTE\_REQUEST\_FAILED](#aacaa203f0c8e23c6ca551df0375410e8)   0x17 |
| #define | [BT\_HCI\_EVT\_LE\_PAST\_RECEIVED](#ad61867c0bef6797f7a3b5418c5a4ed5f)   0x18 |
| #define | [BT\_HCI\_EVT\_LE\_CIS\_ESTABLISHED](#a263d26617702ab43fa8b6717007e1df8)   0x19 |
| #define | [BT\_HCI\_EVT\_LE\_CIS\_REQ](#aaa4af1dcdb163a57b0473b43e8107fd7)   0x1a |
| #define | [BT\_HCI\_EVT\_LE\_BIG\_COMPLETE](#aade42399ac596746100849328c551259)   0x1b |
| #define | [BT\_HCI\_EVT\_LE\_BIG\_TERMINATE](#ac0a1310793a73afda4c2179749df9985)   0x1c |
| #define | [BT\_HCI\_EVT\_LE\_BIG\_SYNC\_ESTABLISHED](#a8d021615f0b1b2077bbec1f1482b85ef)   0x1d |
| #define | [BT\_HCI\_EVT\_LE\_BIG\_SYNC\_LOST](#a9c79430501848b9e75a21020920a8ca8)   0x1e |
| #define | [BT\_HCI\_EVT\_LE\_REQ\_PEER\_SCA\_COMPLETE](#aeb33301a950a9520d7ff706dddb07951)   0x1f |
| #define | [BT\_HCI\_LE\_ZONE\_ENTERED\_LOW](#aff1538e314a97aa4910d4f7066dc4d55)   0x0 |
| #define | [BT\_HCI\_LE\_ZONE\_ENTERED\_MIDDLE](#ab88f3d713f6862c08b73752436ca8b1b)   0x1 |
| #define | [BT\_HCI\_LE\_ZONE\_ENTERED\_HIGH](#af7cc15be8165315ee0358ebb517b5e33)   0x2 |
| #define | [BT\_HCI\_LE\_PATH\_LOSS\_UNAVAILABLE](#a0408b7ecb697bd573b2ea7d2c3c93b92)   0xFF |
| #define | [BT\_HCI\_EVT\_LE\_PATH\_LOSS\_THRESHOLD](#a3e646ec9a2e0baca5126e58368c97995)   0x20 |
| #define | [BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_LOCAL\_CHANGED](#a443a5a524ec41bf2ea86eab74dd022dc)   0x00 |
|  | Reason for Transmit power reporting. |
| #define | [BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_REMOTE\_CHANGED](#a1fbc1b017b13987a017af7cd90bdf708)   0x01 |
| #define | [BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_READ\_REMOTE\_COMPLETED](#a268761b9eae9c84f74394a6098f15ee8)   0x02 |
| #define | [BT\_HCI\_EVT\_LE\_TRANSMIT\_POWER\_REPORT](#a835280c0bf13ddebf451fef5f08c22d0)   0x21 |
| #define | [BT\_HCI\_EVT\_LE\_BIGINFO\_ADV\_REPORT](#a651e36b5529cb7f289721573434154cd)   0x22 |
| #define | [BT\_HCI\_LE\_SUBRATE\_FACTOR\_MIN](#a135059b92eba0676689abc78a2f560d3)   0x0001 |
|  | All limits according to BT Core Spec v5.4 [Vol 4, Part E]. |
| #define | [BT\_HCI\_LE\_SUBRATE\_FACTOR\_MAX](#a33ce951c9eddfcc5556b0168c14b9769)   0x01f4 |
| #define | [BT\_HCI\_LE\_CONTINUATION\_NUM\_MAX](#aa2b9a667e0b80a4cf4d8cef9cb022ad4)   0x01f3 |
| #define | [BT\_HCI\_EVT\_LE\_SUBRATE\_CHANGE](#a2098d628b6ad185cb29106ef69c3627d)   0x23 |
| #define | [BT\_HCI\_EVT\_LE\_CIS\_ESTABLISHED\_V2](#ae5a1301a0fea0ab6c205dab22e39c6c9)   0x2a |
| #define | [BT\_HCI\_LE\_CS\_INITIATOR\_ROLE\_MASK](#af457a20ddc90001f8a523a0e3df6a4bd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_CS\_REFLECTOR\_ROLE\_MASK](#a4c42a75a04962264257c690ba80f6126)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_CS\_MODES\_SUPPORTED\_MODE\_3\_MASK](#a62ab6fbe9acb92c4023f35ae8bb7b14b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_CS\_RTT\_AA\_ONLY\_N\_10NS\_MASK](#ab7843d7e6463e96bce693b82c3f8cc7d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_CS\_RTT\_SOUNDING\_N\_10NS\_MASK](#ad701c1822a44a639bf5a576bf291544f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_N\_10NS\_MASK](#a2135776cd2413e80b3ad653405f0ec67)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_CS\_NADM\_SOUNDING\_CAPABILITY\_PHASE\_BASED\_MASK](#a903505932b23ae60c59fc4f439f8f3ce)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_CS\_NADM\_RANDOM\_CAPABILITY\_PHASE\_BASED\_MASK](#a6b64cb407c353d7a143b7483cf16507f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_CS\_SYNC\_PHYS\_2M\_MASK](#ad8742ec8b365df1850b6e5f56c39e655)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_CS\_SYNC\_PHYS\_2M\_2BT\_MASK](#aeba1a6050a1ff6ad3864132015063026)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_CS\_SUBFEATURE\_NO\_TX\_FAE\_MASK](#a2241cba5ca0dbeb1ea19797654c97397)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_CS\_SUBFEATURE\_CHSEL\_ALG\_3C\_MASK](#a5a7e8927e6086b70177cc04915d16ff8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_CS\_SUBFEATURE\_PBR\_FROM\_RTT\_SOUNDING\_SEQ\_MASK](#a4bcdc621f0292fd182f47762a2cf16bb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_10US\_MASK](#a85f667356dd1e1d9de288776ec13e721)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_20US\_MASK](#a331eff3b3e89a073b30c9d334014b2da)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_30US\_MASK](#a62112179c80be4546b29bc39f632f619)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_40US\_MASK](#a57232d7cbd988c6d6d01d2462e90a7f5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_50US\_MASK](#a4aa0365eb6bc4f54bbbd3ebc2b717c41)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_60US\_MASK](#a647ea407f97ea754f3f729ac8a9bbb02)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_80US\_MASK](#a8bd6f366622ed48cea49fc67692349ce)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_10US\_MASK](#a46420b559fcc0e584bc604790ae066ae)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_20US\_MASK](#a5d279467b3b0b239748b23be57fee63b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_30US\_MASK](#a95d5e9901c50e579600db0ef160425eb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_40US\_MASK](#a66b0bca7c0b19f43b6871cdf05e57543)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_50US\_MASK](#a875fa244820e7aea6f1d6674e3d7d72a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_60US\_MASK](#ab73d093bcb50ebdd5630e85677af6223)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_80US\_MASK](#a6d6e20505ba9b86bc254bc3419e5bc04)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_15US\_MASK](#ac1138ac8f702b4b79bc03c9a7d60207b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_20US\_MASK](#a7023db07ddc8f9e9fbfc59283511bafb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_30US\_MASK](#a77aea9f93d8bcc5949abddcbda52d919)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_40US\_MASK](#a93fc4d9abc1964278748d7dacec7d15a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_50US\_MASK](#a9f45646b734d3d831d307485d2c8c076)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_60US\_MASK](#a27771be57984aac0b825b3ff033df070)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_80US\_MASK](#ab9c3168510c3e5161c393d7093c3527b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_100US\_MASK](#acc787bc6363f4c885816a677f7c47db7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_1200US\_MASK](#a40d5f49728ef8204e9b19be3da28a5ae)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [BT\_HCI\_LE\_CS\_T\_PM\_TIME\_10US\_MASK](#a46f2a35868d8422878e89f1ddde0e7dc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_CS\_T\_PM\_TIME\_20US\_MASK](#a68e13620f22327e8e132aeb19a7cdaf6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_18DB\_MASK](#a24c56f19fcf03aabb170925555209f33)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_21DB\_MASK](#a80fe1748abbd89e1700c239ff450ce07)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_24DB\_MASK](#acd8cc2c9de0edd52c954b0d70dfa44ac)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_27DB\_MASK](#a1f27b2456c323b90eebfa8e45932d92f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_30DB\_MASK](#a5045b5b06b3c79c77a4997066f332d13)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [BT\_HCI\_EVT\_LE\_CS\_READ\_REMOTE\_SUPPORTED\_CAPABILITIES\_COMPLETE](#abceb3da0b6d4c858ad35c631acf0516e)   0x2C |
| #define | [BT\_HCI\_EVT\_LE\_CS\_READ\_REMOTE\_FAE\_TABLE\_COMPLETE](#a319b523766bcc778ba6bfb3784ac49b7)   0x2D |
| #define | [BT\_HCI\_LE\_CS\_CONFIG\_ACTION\_REMOVED](#a9c815ae28e424256fc440b426ba69892)   0x00 |
| #define | [BT\_HCI\_LE\_CS\_CONFIG\_ACTION\_CREATED](#aa437d198f03b30ddbac6ada679e5e0c6)   0x01 |
| #define | [BT\_HCI\_EVT\_LE\_CS\_SECURITY\_ENABLE\_COMPLETE](#ae1e6afca81585dda0f08f85adc3c69a3)   0x2E |
| #define | [BT\_HCI\_EVT\_LE\_CS\_CONFIG\_COMPLETE](#ab0d5abde05c53bc194fe07b8726fb307)   0x2F |
| #define | [BT\_HCI\_LE\_CS\_TEST\_CONN\_HANDLE](#aa615aebe1d896ca1a06bf618619d96f7)   0x0FFF |
| #define | [BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_COMPLETE](#ace872d54fba6d94d62b59a2373c7d0d5)   0x0 |
| #define | [BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_PARTIAL](#af057e8492e52d0c8763d4a2e969d949d)   0x1 |
| #define | [BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_ABORTED](#a821a29dacea9867e4e576f916cf7be3d)   0xF |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_COMPLETE](#aee251ce3c46dc0404d880be7d4550fa6)   0x0 |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_PARTIAL](#a414d620018a946fcb6c209b21ad6fb00)   0x1 |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_ABORTED](#af1907f8ae481a08c674d86e689826f49)   0xF |
| #define | [BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_NO\_ABORT](#a056a67d663cfdc2189b480fc79946c74)   0x0 |
| #define | [BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST](#a21eb191c5d99f902c7a244cad685995f)   0x1 |
| #define | [BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_TOO\_FEW\_CHANNELS](#a6dc3f766ce40bbd0ddb7af3cf85677b1)   0x2 |
| #define | [BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_CHMAP\_INSTANT\_PASSED](#ae8446a2638bd4009b7dee725bb54c883)   0x3 |
| #define | [BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_UNSPECIFIED](#a1e92177f7be3c6a6be00f97fbfc17dcf)   0xF |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_ABORT](#a095b6061c31229b951b6b96e5d02381f)   0x0 |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST](#a41bbe08db99fb0a2ef77f4f3103f9b6c)   0x1 |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_CS\_SYNC\_RECEIVED](#ac4817c265c50019d8f74146f7477bf58)   0x2 |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_SCHED\_CONFLICT](#a31cb520a05fe31313bacf8b021da468c)   0x3 |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_UNSPECIFIED](#abfdca3ae615e19c8e24c098ba8349618)   0xF |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_IGNORED](#a6efdde19fbbf06a40d5dc8dee0515af8)   0x00 |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_1](#ae3e9f6d380a61278a8082f07694bdf43)   0x01 |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_2](#ad6951a0000c3b5cadfbaae94decb153f)   0x02 |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_3](#aaeb365c3f3ea16d760d4943587ea0bd7)   0x03 |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_4](#a4cf750ee707ca0b81d4945e4f66798e3)   0x04 |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_FREQ\_COMPENSATION\_NOT\_AVAILABLE](#a385a401b373522160b1832b66838e02d)   0xC000 |
| #define | [BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_PCT\_NOT\_AVAILABLE](#a22b108e24f198dfd41b2ad692d448c01)   0xFFFFFFFF |
| #define | [BT\_HCI\_LE\_CS\_REF\_POWER\_LEVEL\_UNAVAILABLE](#aa4345ca4225d3958968131ba7a5ff950)   0x7F |
| #define | [BT\_HCI\_LE\_CS\_PCT\_I\_MASK](#af69d92b7c92c8fbeeba8e14838a41f74)   0x000FFF |
| #define | [BT\_HCI\_LE\_CS\_PCT\_Q\_MASK](#a1720b6024f6156e98cb407d6e06e894e)   0xFFF000 |
| #define | [BT\_HCI\_LE\_CS\_TONE\_QUALITY\_HIGH](#adcc92fe105d853cc329bbf4340562835)   0x0 |
| #define | [BT\_HCI\_LE\_CS\_TONE\_QUALITY\_MED](#af42a419097a2e8ee37d46419cd5e20c3)   0x1 |
| #define | [BT\_HCI\_LE\_CS\_TONE\_QUALITY\_LOW](#accc9e73d5fd38c6ab3d108bc3fd039de)   0x2 |
| #define | [BT\_HCI\_LE\_CS\_TONE\_QUALITY\_UNAVAILABLE](#a2b14945754c982ead67ad3b7e615eba9)   0x3 |
| #define | [BT\_HCI\_LE\_CS\_NOT\_TONE\_EXT\_SLOT](#a014d9a06d3c571ce06c94a2ebfdbe4e5)   0x0 |
| #define | [BT\_HCI\_LE\_CS\_TONE\_EXT\_SLOT\_EXT\_NOT\_EXPECTED](#a72a59878b1445b037eb633a374de92e8)   0x1 |
| #define | [BT\_HCI\_LE\_CS\_TONE\_EXT\_SLOT\_EXT\_EXPECTED](#a932802d089c04b78dd6a541b3ddff1e1)   0x2 |
| #define | [BT\_HCI\_LE\_CS\_TIME\_DIFFERENCE\_NOT\_AVAILABLE](#ad0895b572ba1e3d763dbef69c1541b2c)   (([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf))0x8000) |
| #define | [BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_EXT\_UNLIKELY](#a54895cd6caacff2dc5aee25e301144a7)   0x00 |
| #define | [BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_VERY\_UNLIKELY](#af10362bcbd6b95f8404654d258acdbcb)   0x01 |
| #define | [BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_UNLIKELY](#acf2d6f7fd7873e12389a2d470241340f)   0x02 |
| #define | [BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_POSSIBLE](#a73bf7224e934c28a73d5e54a632e0e69)   0x03 |
| #define | [BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_LIKELY](#a93f1786e8177c89eb9db36a72e367122)   0x04 |
| #define | [BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_VERY\_LIKELY](#a0b10dcb24c429d594b17eec494954d74)   0x05 |
| #define | [BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_EXT\_LIKELY](#abfedf14c97b27f6cdbbb66f2598734e9)   0x06 |
| #define | [BT\_HCI\_LE\_CS\_PACKET\_NADM\_UNKNOWN](#a5f7d8e81a83a3b94e18a39b507232823)   0xFF |
| #define | [BT\_HCI\_LE\_CS\_PACKET\_QUALITY\_AA\_CHECK\_SUCCESSFUL](#ab05d15713fb0145b32a5977774b50533)   0x0 |
| #define | [BT\_HCI\_LE\_CS\_PACKET\_QUALITY\_AA\_CHECK\_BIT\_ERRORS\_FOUND](#a7c0e4053873d629e10567937adc033d3)   0x1 |
| #define | [BT\_HCI\_LE\_CS\_PACKET\_QUALITY\_AA\_CHECK\_AA\_NOT\_FOUND](#af357550f37226be5b2b6491ebad3fd57)   0x2 |
| #define | [BT\_HCI\_LE\_CS\_PACKET\_RSSI\_NOT\_AVAILABLE](#a8ce6b3556a9f5b83648b80d90652f00d)   0x7F |
| #define | [BT\_HCI\_EVT\_LE\_CS\_SUBEVENT\_RESULT](#a56079aad1e8efe328c0bfd4dbad9d953)   0x31 |
| #define | [BT\_HCI\_EVT\_LE\_CS\_SUBEVENT\_RESULT\_CONTINUE](#aad00fc66b8bbc4f3e474661cb4122e47)   0x32 |
| #define | [BT\_HCI\_EVT\_LE\_CS\_TEST\_END\_COMPLETE](#a7dae3e2125d30c3b344b51aba0df68bf)   0x33 |
| #define | [BT\_HCI\_EVT\_LE\_CS\_PROCEDURE\_ENABLE\_COMPLETE](#a276cf3951bb5c4ee0b1deeb78a7b5681)   0x30 |
| #define | [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(n) |
| #define | [BT\_EVT\_MASK\_INQUIRY\_COMPLETE](#a79851cd962916f9be81e29ce9797e901)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(0) |
| #define | [BT\_EVT\_MASK\_CONN\_COMPLETE](#a5a13adda8bf4f015550a043667e0b67d)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(2) |
| #define | [BT\_EVT\_MASK\_CONN\_REQUEST](#ad77bbcd4fb8b0e37700492e8a3cccd38)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(3) |
| #define | [BT\_EVT\_MASK\_DISCONN\_COMPLETE](#a5ea9d4fb977c660bc33be93c73817705)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(4) |
| #define | [BT\_EVT\_MASK\_AUTH\_COMPLETE](#ad4f80dd3fdf22b23d47785a507aa5a85)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(5) |
| #define | [BT\_EVT\_MASK\_REMOTE\_NAME\_REQ\_COMPLETE](#a4433027483d6d63911b59c4fe605ba69)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(6) |
| #define | [BT\_EVT\_MASK\_ENCRYPT\_CHANGE](#a334c571248a1aad285bb11bc39d2ade8)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(7) |
| #define | [BT\_EVT\_MASK\_REMOTE\_FEATURES](#a7ccade60a01e0f8a175b3b11b5e20f6d)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(10) |
| #define | [BT\_EVT\_MASK\_REMOTE\_VERSION\_INFO](#a87331cabdea78ace1577cbf2fa7e3523)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(11) |
| #define | [BT\_EVT\_MASK\_HARDWARE\_ERROR](#a079c00e59422034a9f977af7dd20234c)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(15) |
| #define | [BT\_EVT\_MASK\_ROLE\_CHANGE](#a4b4a80b51b2c20bf28fbfac57679a86e)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(17) |
| #define | [BT\_EVT\_MASK\_PIN\_CODE\_REQ](#a9f5612d89848aafb6e9063a55e5cd6b4)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(21) |
| #define | [BT\_EVT\_MASK\_LINK\_KEY\_REQ](#a1e16ab7caf239e804c0c2057e9b49e42)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(22) |
| #define | [BT\_EVT\_MASK\_LINK\_KEY\_NOTIFY](#aa20a3ce217a60070826d0b55ebd105be)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(23) |
| #define | [BT\_EVT\_MASK\_DATA\_BUFFER\_OVERFLOW](#a829ea33c603291d331faba58689b0198)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(25) |
| #define | [BT\_EVT\_MASK\_INQUIRY\_RESULT\_WITH\_RSSI](#aeb5b4cbc01a8cebea5ce8e0090d37261)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(33) |
| #define | [BT\_EVT\_MASK\_REMOTE\_EXT\_FEATURES](#a9d3bbaa1eb1dbe72714b922dcada3347)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(34) |
| #define | [BT\_EVT\_MASK\_SYNC\_CONN\_COMPLETE](#a4f1a905136cb713c09fb5197dd099ce2)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(43) |
| #define | [BT\_EVT\_MASK\_EXTENDED\_INQUIRY\_RESULT](#a9b361fe6314f56fcb016bacb064af815)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(46) |
| #define | [BT\_EVT\_MASK\_ENCRYPT\_KEY\_REFRESH\_COMPLETE](#af8d96cc1cf99a7130d4c181450998cb7)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(47) |
| #define | [BT\_EVT\_MASK\_IO\_CAPA\_REQ](#a845de3735dc3989d3a9d54cf5e55b408)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(48) |
| #define | [BT\_EVT\_MASK\_IO\_CAPA\_RESP](#a409e33dbe4fdb1dc90050e0b4eab1f86)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(49) |
| #define | [BT\_EVT\_MASK\_USER\_CONFIRM\_REQ](#a1c04cc7d04f056e5edfc4ddaa97c657f)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(50) |
| #define | [BT\_EVT\_MASK\_USER\_PASSKEY\_REQ](#af56d87ffc24c2e4c08db68ab019fd58e)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(51) |
| #define | [BT\_EVT\_MASK\_SSP\_COMPLETE](#a6a08ace148ea2728614a3bab02c21f65)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(53) |
| #define | [BT\_EVT\_MASK\_USER\_PASSKEY\_NOTIFY](#a2eb47347a5685a290087b236d696971e)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(58) |
| #define | [BT\_EVT\_MASK\_LE\_META\_EVENT](#a59f89d39350b396f8d0c986e2d477bba)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(61) |
| #define | [BT\_EVT\_MASK\_NUM\_COMPLETE\_DATA\_BLOCKS](#abe39e63cbdee9bfeac36a1b6a4d40aba)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(8) |
| #define | [BT\_EVT\_MASK\_TRIGG\_CLOCK\_CAPTURE](#aff43216feb0c29c6813d198473f34fdc)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(14) |
| #define | [BT\_EVT\_MASK\_SYNCH\_TRAIN\_COMPLETE](#ac078d5b46d7e227726cb7456e2163d3f)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(15) |
| #define | [BT\_EVT\_MASK\_SYNCH\_TRAIN\_RX](#a8901b477ec3584af207b3648b221bb92)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(16) |
| #define | [BT\_EVT\_MASK\_CL\_PER\_BC\_RX](#aa8842138b1146d3581c39062d11a6305)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(17) |
| #define | [BT\_EVT\_MASK\_CL\_PER\_BC\_TIMEOUT](#af513eaa35861cfcfefba97e0263e3f5b)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(18) |
| #define | [BT\_EVT\_MASK\_TRUNC\_PAGE\_COMPLETE](#a9b82f06f42651c32f4c0db9826002134)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(19) |
| #define | [BT\_EVT\_MASK\_PER\_PAGE\_RSP\_TIMEOUT](#ad078befa197baac20294dc0d46eff9dd)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(20) |
| #define | [BT\_EVT\_MASK\_CL\_PER\_BC\_CH\_MAP\_CHANGE](#a35f42f297b980a050deceb71237883ba)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(21) |
| #define | [BT\_EVT\_MASK\_INQUIRY\_RSP\_NOT](#ae8106016a80e123016c6d2fc406224d7)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(22) |
| #define | [BT\_EVT\_MASK\_AUTH\_PAYLOAD\_TIMEOUT\_EXP](#a33753df12afb5f7e19be01f9febc5d23)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(23) |
| #define | [BT\_EVT\_MASK\_SAM\_STATUS\_CHANGE](#a8bfac36e993c48d12bdeb7c130fdd6dc)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(24) |
| #define | [BT\_EVT\_MASK\_LE\_CONN\_COMPLETE](#a59cd7a15e5b562adb6397509463e375c)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(0) |
| #define | [BT\_EVT\_MASK\_LE\_ADVERTISING\_REPORT](#a39a55a4c3e71db708e39c8110a2349f7)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(1) |
| #define | [BT\_EVT\_MASK\_LE\_CONN\_UPDATE\_COMPLETE](#ab1988671f4017f6434dc0438b2e8b9f6)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(2) |
| #define | [BT\_EVT\_MASK\_LE\_REMOTE\_FEAT\_COMPLETE](#adba1a3a872ee26a41218c9104e9f957b)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(3) |
| #define | [BT\_EVT\_MASK\_LE\_LTK\_REQUEST](#ab495948af67d01208eff1adb9a33e489)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(4) |
| #define | [BT\_EVT\_MASK\_LE\_CONN\_PARAM\_REQ](#ac3eeaa0610a6ac6d3b57880042071f2a)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(5) |
| #define | [BT\_EVT\_MASK\_LE\_DATA\_LEN\_CHANGE](#a73489ce7067d812e8443e242ee53a5e6)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(6) |
| #define | [BT\_EVT\_MASK\_LE\_P256\_PUBLIC\_KEY\_COMPLETE](#a281d70b2b596b918972b59e684b6a476)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(7) |
| #define | [BT\_EVT\_MASK\_LE\_GENERATE\_DHKEY\_COMPLETE](#afbe64037a16680397614ba2db136b452)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(8) |
| #define | [BT\_EVT\_MASK\_LE\_ENH\_CONN\_COMPLETE](#afb3b477cb835e60c3e77237451ebae5b)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(9) |
| #define | [BT\_EVT\_MASK\_LE\_DIRECT\_ADV\_REPORT](#a3e84268b1e701ae37c77e95847490222)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(10) |
| #define | [BT\_EVT\_MASK\_LE\_PHY\_UPDATE\_COMPLETE](#ab5f6014468b107486aba04ba698453ed)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(11) |
| #define | [BT\_EVT\_MASK\_LE\_EXT\_ADVERTISING\_REPORT](#a1d7fc1a3ea229622560de8cf0bb63a81)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(12) |
| #define | [BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_ESTABLISHED](#a96142f5d79029a93a99152ade46fc005)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(13) |
| #define | [BT\_EVT\_MASK\_LE\_PER\_ADVERTISING\_REPORT](#ad7fc62afd0e1e3dc040567d91320e18e)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(14) |
| #define | [BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_LOST](#ae78587797f24987f36c348fe790438b2)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(15) |
| #define | [BT\_EVT\_MASK\_LE\_SCAN\_TIMEOUT](#a372f6b8e355972d63e5f9ff45a486e9d)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(16) |
| #define | [BT\_EVT\_MASK\_LE\_ADV\_SET\_TERMINATED](#a11330b1b6847d77d3ba88e1de0aaa36e)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(17) |
| #define | [BT\_EVT\_MASK\_LE\_SCAN\_REQ\_RECEIVED](#a3f13865e913a1c6afb6d8d05a6d84608)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(18) |
| #define | [BT\_EVT\_MASK\_LE\_CHAN\_SEL\_ALGO](#acee0428356c4853fe664709fc1675f02)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(19) |
| #define | [BT\_EVT\_MASK\_LE\_CONNECTIONLESS\_IQ\_REPORT](#a6ef13decc171530c00f12b0226fa9ed1)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(20) |
| #define | [BT\_EVT\_MASK\_LE\_CONNECTION\_IQ\_REPORT](#a3b2f133db5641414b95bfd953d715ff3)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(21) |
| #define | [BT\_EVT\_MASK\_LE\_CTE\_REQUEST\_FAILED](#afbd3991be814ec6462d62fbc4c898ac0)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(22) |
| #define | [BT\_EVT\_MASK\_LE\_PAST\_RECEIVED](#a5b2139ce8847bfcdbcd99c3241fb5ea2)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(23) |
| #define | [BT\_EVT\_MASK\_LE\_CIS\_ESTABLISHED](#a9e41b4cb965576490fb39f7dc396722f)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(24) |
| #define | [BT\_EVT\_MASK\_LE\_CIS\_REQ](#aa24e9569ace049098a6d822ad7433e26)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(25) |
| #define | [BT\_EVT\_MASK\_LE\_BIG\_COMPLETE](#a447ff4a3e4dfba390ce9729e45abb410)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(26) |
| #define | [BT\_EVT\_MASK\_LE\_BIG\_TERMINATED](#ad4b775d48bfa14c00c78ac1fbb8f2a2a)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(27) |
| #define | [BT\_EVT\_MASK\_LE\_BIG\_SYNC\_ESTABLISHED](#ab88b8bcde1d07b5f16c55c4cbf4fd20d)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(28) |
| #define | [BT\_EVT\_MASK\_LE\_BIG\_SYNC\_LOST](#a87abdedde8bd43f845fe604c80612ca0)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(29) |
| #define | [BT\_EVT\_MASK\_LE\_REQ\_PEER\_SCA\_COMPLETE](#a01e518d3bb3d4f99c335743362a84080)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(30) |
| #define | [BT\_EVT\_MASK\_LE\_PATH\_LOSS\_THRESHOLD](#a6aad398435aa48ba67f6917bca2a690e)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(31) |
| #define | [BT\_EVT\_MASK\_LE\_TRANSMIT\_POWER\_REPORTING](#a7f9d3cdf0de067ad408bec600b9a691f)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(32) |
| #define | [BT\_EVT\_MASK\_LE\_BIGINFO\_ADV\_REPORT](#aff9c37de1e55e6a7085b3a521f34d3e0)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(33) |
| #define | [BT\_EVT\_MASK\_LE\_SUBRATE\_CHANGE](#a8a52784fd872a8ee6f666c31e846411d)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(34) |
| #define | [BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_ESTABLISHED\_V2](#a92a360ad268c29e1616de1e16748eb44)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(35) |
| #define | [BT\_EVT\_MASK\_LE\_PER\_ADVERTISING\_REPORT\_V2](#ad78d5a027581dee52c54bb3f5a19b68d)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(36) |
| #define | [BT\_EVT\_MASK\_LE\_PAST\_RECEIVED\_V2](#a93aec31c1636fec90b609981736eb2de)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(37) |
| #define | [BT\_EVT\_MASK\_LE\_PER\_ADV\_SUBEVENT\_DATA\_REQ](#af0e2c2e66bdac52fbe5e9c91ca26fe49)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(38) |
| #define | [BT\_EVT\_MASK\_LE\_PER\_ADV\_RESPONSE\_REPORT](#ab8a9486fedec169e4d44b249f2445acf)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(39) |
| #define | [BT\_EVT\_MASK\_LE\_ENH\_CONN\_COMPLETE\_V2](#a8b40a701334d25741a6e17ffd86576ad)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(40) |
| #define | [BT\_EVT\_MASK\_LE\_CIS\_ESTABLISHED\_V2](#a1b02618f1fbfb3a710fd413f205da9a6)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(41) |
| #define | [BT\_EVT\_MASK\_LE\_CS\_READ\_REMOTE\_SUPPORTED\_CAPABILITIES\_COMPLETE](#a97d1b704b1638fb85fa4da6f6d31e209)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(43) |
| #define | [BT\_EVT\_MASK\_LE\_CS\_READ\_REMOTE\_FAE\_TABLE\_COMPLETE](#a406cdb92d8c6524aca8971425bab7baa)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(44) |
| #define | [BT\_EVT\_MASK\_LE\_CS\_SECURITY\_ENABLE\_COMPLETE](#a07b9cc5a2fcc73d56590a034977cf3a0)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(45) |
| #define | [BT\_EVT\_MASK\_LE\_CS\_CONFIG\_COMPLETE](#abe6f94ab4bae0d34f23e27c0948e3a21)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(46) |
| #define | [BT\_EVT\_MASK\_LE\_CS\_PROCEDURE\_ENABLE\_COMPLETE](#affbe9c98cf94e50673a2a59c8fb68256)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(47) |
| #define | [BT\_EVT\_MASK\_LE\_CS\_SUBEVENT\_RESULT](#a040ef537fe66f923dc3c344fee023002)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(48) |
| #define | [BT\_EVT\_MASK\_LE\_CS\_SUBEVENT\_RESULT\_CONTINUE](#a226c276713e3cf16108e4a66fad6db79)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(49) |
| #define | [BT\_EVT\_MASK\_LE\_CS\_TEST\_END\_COMPLETE](#a8a6ec9510323355aa003cb8be519be7d)   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(50) |
| #define | [BT\_HCI\_ERR\_SUCCESS](#a27c890210eded48f159073cccef8582a)   0x00 |
|  | HCI Error Codes, BT Core Spec v5.4 [Vol 1, Part F]. |
| #define | [BT\_HCI\_ERR\_UNKNOWN\_CMD](#a376012d3b8f7814870e3f03f6cbabb89)   0x01 |
| #define | [BT\_HCI\_ERR\_UNKNOWN\_CONN\_ID](#afd68afeb0296e3af363d7d60eaf4e9a1)   0x02 |
| #define | [BT\_HCI\_ERR\_HW\_FAILURE](#a5dfcb0d206b98be7eacdc67547bb8a2c)   0x03 |
| #define | [BT\_HCI\_ERR\_PAGE\_TIMEOUT](#a1e89c8eb63dee6bd720ef9354c867519)   0x04 |
| #define | [BT\_HCI\_ERR\_AUTH\_FAIL](#a070d51dd0de3288f9811f90a558c889b)   0x05 |
| #define | [BT\_HCI\_ERR\_PIN\_OR\_KEY\_MISSING](#a39f129aefe81c2d06f70552ace008a15)   0x06 |
| #define | [BT\_HCI\_ERR\_MEM\_CAPACITY\_EXCEEDED](#ac54f84b29901185822f6bad2edf86b61)   0x07 |
| #define | [BT\_HCI\_ERR\_CONN\_TIMEOUT](#ab702caf5cd73431cc9aede8891f74610)   0x08 |
| #define | [BT\_HCI\_ERR\_CONN\_LIMIT\_EXCEEDED](#a490798f4f1e226e66475f0fb84cfbcd5)   0x09 |
| #define | [BT\_HCI\_ERR\_SYNC\_CONN\_LIMIT\_EXCEEDED](#a56a3d3d9d7798334b29c02214a2e73bf)   0x0a |
| #define | [BT\_HCI\_ERR\_CONN\_ALREADY\_EXISTS](#abcf4cd921e304758cc969a83445d70ec)   0x0b |
| #define | [BT\_HCI\_ERR\_CMD\_DISALLOWED](#a5ee9f2e9625d732e84e5ef593bb2a3f9)   0x0c |
| #define | [BT\_HCI\_ERR\_INSUFFICIENT\_RESOURCES](#a0efddbffb31b93158b10a3f678f94f4e)   0x0d |
| #define | [BT\_HCI\_ERR\_INSUFFICIENT\_SECURITY](#a08d4bdfc189bccbdb97a51b0089e77a0)   0x0e |
| #define | [BT\_HCI\_ERR\_BD\_ADDR\_UNACCEPTABLE](#a366f85b3bcb3f578b2572149c69b7fc0)   0x0f |
| #define | [BT\_HCI\_ERR\_CONN\_ACCEPT\_TIMEOUT](#ae4682cbd7a9b9dedd25926efe029c0d7)   0x10 |
| #define | [BT\_HCI\_ERR\_UNSUPP\_FEATURE\_PARAM\_VAL](#af73db17855859676827bad84e2ccbabe)   0x11 |
| #define | [BT\_HCI\_ERR\_INVALID\_PARAM](#afc76c774f5e71423eb9fea910d1860e9)   0x12 |
| #define | [BT\_HCI\_ERR\_REMOTE\_USER\_TERM\_CONN](#ac0e3b44027180d7a2dedb59395c4b111)   0x13 |
| #define | [BT\_HCI\_ERR\_REMOTE\_LOW\_RESOURCES](#a5eeadfb220c24b2e7f5ce3fd21e5d46a)   0x14 |
| #define | [BT\_HCI\_ERR\_REMOTE\_POWER\_OFF](#a083f1fc52300f7e47c2f8d4e50551851)   0x15 |
| #define | [BT\_HCI\_ERR\_LOCALHOST\_TERM\_CONN](#a0f07b75be216456e9370485dca0da992)   0x16 |
| #define | [BT\_HCI\_ERR\_REPEATED\_ATTEMPTS](#a11d42e0347cc9d1d50ccd45c2e9a39f6)   0x17 |
| #define | [BT\_HCI\_ERR\_PAIRING\_NOT\_ALLOWED](#a60823c337c91aa95348dcae250a83977)   0x18 |
| #define | [BT\_HCI\_ERR\_UNKNOWN\_LMP\_PDU](#a0f81b5c19358982bd33c527239200b08)   0x19 |
| #define | [BT\_HCI\_ERR\_UNSUPP\_REMOTE\_FEATURE](#a516751f02bd497a020783f69bcf71453)   0x1a |
| #define | [BT\_HCI\_ERR\_SCO\_OFFSET\_REJECTED](#a5e28f04c454361508bc791c6ce292bc2)   0x1b |
| #define | [BT\_HCI\_ERR\_SCO\_INTERVAL\_REJECTED](#a5093c6357fcefd1ccdcbdf9a99f18e7c)   0x1c |
| #define | [BT\_HCI\_ERR\_SCO\_AIR\_MODE\_REJECTED](#ad8f77a43360e8ab2e6c71a103e14c951)   0x1d |
| #define | [BT\_HCI\_ERR\_INVALID\_LL\_PARAM](#a943fe81109d82983018b558b9274f9a3)   0x1e |
| #define | [BT\_HCI\_ERR\_UNSPECIFIED](#ab3833bbb70b6a2e57870d8243f528b90)   0x1f |
| #define | [BT\_HCI\_ERR\_UNSUPP\_LL\_PARAM\_VAL](#af1fa61561b6a91d08f81e9c19cbe89f7)   0x20 |
| #define | [BT\_HCI\_ERR\_ROLE\_CHANGE\_NOT\_ALLOWED](#a070d016f54e7f5f0a7ca6d8c8218505f)   0x21 |
| #define | [BT\_HCI\_ERR\_LL\_RESP\_TIMEOUT](#a6317763780d9c81e6752d5a2c8ce3172)   0x22 |
| #define | [BT\_HCI\_ERR\_LL\_PROC\_COLLISION](#a0e280074290680d62ad4721384bb603e)   0x23 |
| #define | [BT\_HCI\_ERR\_LMP\_PDU\_NOT\_ALLOWED](#a47c02d44d40d785db6fee28c88d3c5b4)   0x24 |
| #define | [BT\_HCI\_ERR\_ENC\_MODE\_NOT\_ACCEPTABLE](#aeb5499a707e1c41cbd9db882cfdf0677)   0x25 |
| #define | [BT\_HCI\_ERR\_LINK\_KEY\_CANNOT\_BE\_CHANGED](#aee97132db4398e2db0a6e115ca20b9b4)   0x26 |
| #define | [BT\_HCI\_ERR\_REQUESTED\_QOS\_NOT\_SUPPORTED](#a0e02fd84d7a355f42fe006c756936d78)   0x27 |
| #define | [BT\_HCI\_ERR\_INSTANT\_PASSED](#a2d336db995ab250f94de66da952c642c)   0x28 |
| #define | [BT\_HCI\_ERR\_PAIRING\_NOT\_SUPPORTED](#a059c7d5619823eddf2c541b40a6464cb)   0x29 |
| #define | [BT\_HCI\_ERR\_DIFF\_TRANS\_COLLISION](#a3b461d65baa95f8f984b212264dc5072)   0x2a |
| #define | [BT\_HCI\_ERR\_QOS\_UNACCEPTABLE\_PARAM](#a37c2fdc6b32b4a2cb70d5c17dfbe262b)   0x2c |
| #define | [BT\_HCI\_ERR\_QOS\_REJECTED](#a88363d1eb1c0d13dc8138af8edc76abc)   0x2d |
| #define | [BT\_HCI\_ERR\_CHAN\_ASSESS\_NOT\_SUPPORTED](#a3b9fc13a3e3ecc9f0f4431487c0301b5)   0x2e |
| #define | [BT\_HCI\_ERR\_INSUFF\_SECURITY](#a334efee11bd7086e0611c8f628d65abb)   0x2f |
| #define | [BT\_HCI\_ERR\_PARAM\_OUT\_OF\_MANDATORY\_RANGE](#a29c763a2e70820fae7e2e825d22f4991)   0x30 |
| #define | [BT\_HCI\_ERR\_ROLE\_SWITCH\_PENDING](#ac9c9a68e696e038d7b05af89e3a0c7b6)   0x32 |
| #define | [BT\_HCI\_ERR\_RESERVED\_SLOT\_VIOLATION](#ac6244ca7123879ef039c2c5486d50d41)   0x34 |
| #define | [BT\_HCI\_ERR\_ROLE\_SWITCH\_FAILED](#ab40a919a2d87376f2aca6d2ea3f55758)   0x35 |
| #define | [BT\_HCI\_ERR\_EXT\_INQ\_RESP\_TOO\_LARGE](#a1b7094ad185ed22542f370ab1101c1ae)   0x36 |
| #define | [BT\_HCI\_ERR\_SIMPLE\_PAIR\_NOT\_SUPP\_BY\_HOST](#afd8840ad198dfdb666bf24851a478c70)   0x37 |
| #define | [BT\_HCI\_ERR\_HOST\_BUSY\_PAIRING](#a107d85e39fec3146d6b017deb047571b)   0x38 |
| #define | [BT\_HCI\_ERR\_CONN\_REJECTED\_DUE\_TO\_NO\_CHAN](#a1adf558f8f606612ca96bdbbb55e0e78)   0x39 |
| #define | [BT\_HCI\_ERR\_CONTROLLER\_BUSY](#a33167856fe838b833fe42d92c3eac4eb)   0x3a |
| #define | [BT\_HCI\_ERR\_UNACCEPT\_CONN\_PARAM](#a712e214942c0d151597ce04e9d0df453)   0x3b |
| #define | [BT\_HCI\_ERR\_ADV\_TIMEOUT](#abfa408d8366ff3cae1cd35fffcda30c0)   0x3c |
| #define | [BT\_HCI\_ERR\_TERM\_DUE\_TO\_MIC\_FAIL](#a71dd49b1b5dc51ad7db8da9aecf9ff06)   0x3d |
| #define | [BT\_HCI\_ERR\_CONN\_FAIL\_TO\_ESTAB](#ac6c44be2e737d7a10b5c886c69d6b1a5)   0x3e |
| #define | [BT\_HCI\_ERR\_MAC\_CONN\_FAILED](#af0b9f71a874ca2c3587256c7f665e9fa)   0x3f |
| #define | [BT\_HCI\_ERR\_CLOCK\_ADJUST\_REJECTED](#a6e9a4db5962d79b5a7f43a4c2919c9e9)   0x40 |
| #define | [BT\_HCI\_ERR\_SUBMAP\_NOT\_DEFINED](#a9e7483e2d7f46981e9d1fcdbb8a7515c)   0x41 |
| #define | [BT\_HCI\_ERR\_UNKNOWN\_ADV\_IDENTIFIER](#a7646bc91f5dbb28c5eeda7e1828f2e30)   0x42 |
| #define | [BT\_HCI\_ERR\_LIMIT\_REACHED](#a86b092455cfd220d48af2bea04900b5b)   0x43 |
| #define | [BT\_HCI\_ERR\_OP\_CANCELLED\_BY\_HOST](#a85433a7b3bcac0a507d7f6376a084142)   0x44 |
| #define | [BT\_HCI\_ERR\_PACKET\_TOO\_LONG](#ab63f7d0c79aaa57abf59aa18e112345f)   0x45 |
| #define | [BT\_HCI\_ERR\_TOO\_LATE](#a9c62f8f73470a3157a60f8d6d56b22a4)   0x46 |
| #define | [BT\_HCI\_ERR\_TOO\_EARLY](#a8dcf345b1fea1364f490f40963992cd6)   0x47 |

## Macro Definition Documentation

## [◆ ](#a9693358ac3b7d9da498ca557fa0d1410)B\_HCI\_LE\_CTE\_REPORT\_SAMPLE\_COUNT\_MAX

| #define B\_HCI\_LE\_CTE\_REPORT\_SAMPLE\_COUNT\_MAX   0x52 |
| --- |

## [◆ ](#a87364c12ecac6b05681469c9450f887e)B\_HCI\_LE\_CTE\_REPORT\_SAMPLE\_COUNT\_MIN

| #define B\_HCI\_LE\_CTE\_REPORT\_SAMPLE\_COUNT\_MIN   0x9 |
| --- |

## [◆ ](#a2f9e6232229ae1bed3d835b5f6531a76)BT\_ACL\_BROADCAST

| #define BT\_ACL\_BROADCAST   0x01 |
| --- |

## [◆ ](#ad6f24425a0818730d2377e159698922b)BT\_ACL\_COMPLETE

| #define BT\_ACL\_COMPLETE   0x03 |
| --- |

## [◆ ](#a0bfb8a0bac96eb223eb8229c1dff9e7d)BT\_ACL\_CONT

| #define BT\_ACL\_CONT   0x01 |
| --- |

## [◆ ](#a499f8647747fd6b7b82d9b3280b4b048)bt\_acl\_flags

| #define bt\_acl\_flags | ( |  | *h* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((h) >> 12)

## [◆ ](#a55cfcca3e0a6a7401e57e7430421093e)bt\_acl\_flags\_bc

| #define bt\_acl\_flags\_bc | ( |  | *f* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((f) >> 2)

## [◆ ](#ae358e74ce455f11bb134700ec80fe07b)bt\_acl\_flags\_pb

| #define bt\_acl\_flags\_pb | ( |  | *f* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((f) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(2))

[BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)

#define BIT\_MASK(n)

Bit mask with bits 0 through n-1 (inclusive) set, or 0 if n is 0.

**Definition** util\_macro.h:68

## [◆ ](#a500341d3485843d85dc034ce6f8a908c)bt\_acl\_handle

| #define bt\_acl\_handle | ( |  | *h* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((h) & [BT\_ACL\_HANDLE\_MASK](#a28a9f26ba563e2687856aff39b044039))

[BT\_ACL\_HANDLE\_MASK](#a28a9f26ba563e2687856aff39b044039)

#define BT\_ACL\_HANDLE\_MASK

**Definition** hci\_types.h:74

## [◆ ](#a28a9f26ba563e2687856aff39b044039)BT\_ACL\_HANDLE\_MASK

| #define BT\_ACL\_HANDLE\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(12) |
| --- |

## [◆ ](#aa08e6239d84ce55153baa41f46814363)bt\_acl\_handle\_pack

| #define bt\_acl\_handle\_pack | ( |  | *h*, |
| --- | --- | --- | --- |
|  |  |  | *f* ) |

**Value:**

((h) | ((f) << 12))

## [◆ ](#a343e6550f9a24a59c5a08efd2dab16bb)BT\_ACL\_POINT\_TO\_POINT

| #define BT\_ACL\_POINT\_TO\_POINT   0x00 |
| --- |

## [◆ ](#a49c9728293c37e718c009ad973f6d43e)BT\_ACL\_START

| #define BT\_ACL\_START   0x02 |
| --- |

## [◆ ](#ae8c5ddd450d47b45a310bc979207ebff)BT\_ACL\_START\_NO\_FLUSH

| #define BT\_ACL\_START\_NO\_FLUSH   0x00 |
| --- |

## [◆ ](#a19b4c20d243de28462b686088e2971a3)BT\_BREDR\_SCAN\_DISABLED

| #define BT\_BREDR\_SCAN\_DISABLED   0x00 |
| --- |

## [◆ ](#a2f75eaee67bbb6c0211f3146d881278f)BT\_BREDR\_SCAN\_INQUIRY

| #define BT\_BREDR\_SCAN\_INQUIRY   0x01 |
| --- |

## [◆ ](#a006d877a26f4e8dd0689b1324107a843)BT\_BREDR\_SCAN\_PAGE

| #define BT\_BREDR\_SCAN\_PAGE   0x02 |
| --- |

## [◆ ](#ae3aaad5ae408cb8c72a29ff7a8817c21)BT\_CMD\_LE\_STATES

| #define BT\_CMD\_LE\_STATES | ( |  | *[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_CMD\_TEST](#a7d5bc35e597d03fbc65084b39771cf0b)([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), 28, 3)

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[BT\_CMD\_TEST](#a7d5bc35e597d03fbc65084b39771cf0b)

#define BT\_CMD\_TEST(cmd, octet, bit)

**Definition** hci\_types.h:139

## [◆ ](#a7d5bc35e597d03fbc65084b39771cf0b)BT\_CMD\_TEST

| #define BT\_CMD\_TEST | ( |  | *[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)*, |
| --- | --- | --- | --- |
|  |  |  | *octet*, |
|  |  |  | *bit* ) |

**Value:**

([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)[octet] & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(bit))

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

## [◆ ](#aa8793a9bc39bf833124c8c961e441a43)BT\_COD

| #define BT\_COD | ( |  | *major\_service*, |
| --- | --- | --- | --- |
|  |  |  | *major\_device*, |
|  |  |  | *minor\_device* ) |

**Value:**

((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))major\_service << 13) | (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))major\_device << 8) | \

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))minor\_device << 2))

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

## [◆ ](#ae35a91503887ea73a32342888cc75239)BT\_COD\_MAJOR\_AUDIO\_VIDEO

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO   0x04 |
| --- |

## [◆ ](#a1c77c5966d3cb71e827a4e59234240f9)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_CAMCORDER

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_CAMCORDER   0x0D |
| --- |

## [◆ ](#a9df23b6e094f75de44fdc6e072d07ed6)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_CAR\_AUDIO

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_CAR\_AUDIO   0x08 |
| --- |

## [◆ ](#a2ed0612651757c12606bab74ea10d14a)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_GAME\_TOY

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_GAME\_TOY   0x12 |
| --- |

## [◆ ](#a7eff517cf71309181024f9eb7babb277)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_HANDS\_FREE

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_HANDS\_FREE   0x02 |
| --- |

## [◆ ](#ab93463c966352ee2b246003edad18924)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_HEADPHONES

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_HEADPHONES   0x06 |
| --- |

## [◆ ](#a0ab46892a2ab50747d8fcec489b8a5c2)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_HIFI\_AUDIO

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_HIFI\_AUDIO   0x0A |
| --- |

## [◆ ](#a54790088ccbeca72e3a41cd559f1c994)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_LOUDSPEAKER

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_LOUDSPEAKER   0x05 |
| --- |

## [◆ ](#ac586986c21d07748bf92e4ade2cb857c)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_MICROPHONE

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_MICROPHONE   0x04 |
| --- |

## [◆ ](#a516cf67e162628fa7e8ab15c85aa50a1)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_PORTABLE\_AUDIO

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_PORTABLE\_AUDIO   0x07 |
| --- |

## [◆ ](#a50941bdf421209a7bd41b5e225c8a8ed)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_RFU

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_RFU   0x03 |
| --- |

## [◆ ](#a85de6aa2ca223da1ac43ffe57489ac24)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_RFU2

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_RFU2   0x11 |
| --- |

## [◆ ](#a28db3d9daf698fcb382b417532a53652)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_SET\_TOP\_BOX

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_SET\_TOP\_BOX   0x09 |
| --- |

## [◆ ](#a0432846ee3f571d35feba5af70b1b0af)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_UNCATEGORIZED

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_UNCATEGORIZED   0x00 |
| --- |

## [◆ ](#a0c0c540721712ba407ea08972420cad6)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VCR

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VCR   0x0B |
| --- |

## [◆ ](#a0b61e3de9a35c714fc1414f29a2a79c5)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_CAMERA

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_CAMERA   0x0C |
| --- |

## [◆ ](#afa9446149a24189fd4192c8b32a5ae97)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_CONFERENCING

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_CONFERENCING   0x10 |
| --- |

## [◆ ](#a5569a391b209cdb551576392e228dcb0)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_DISPLAY\_LOUDSPEAKER

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_DISPLAY\_LOUDSPEAKER   0x0F |
| --- |

## [◆ ](#a13af74023c32c24f7baa6249cc538e2c)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_MONITOR

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_MONITOR   0x0E |
| --- |

## [◆ ](#a56c2a8e3602b53fce244faafd4101af4)BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_WEARABLE\_HEADSET

| #define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_WEARABLE\_HEADSET   0x01 |
| --- |

## [◆ ](#acdd58e03fb46b783025cfd54d429263b)BT\_COD\_MAJOR\_COMPUTER

| #define BT\_COD\_MAJOR\_COMPUTER   0x01 |
| --- |

## [◆ ](#a54cd2fc8881fc63b3784d4267df0cc98)BT\_COD\_MAJOR\_COMPUTER\_MINOR\_DESKTOP

| #define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_DESKTOP   0x01 |
| --- |

## [◆ ](#ac6b246fe1bb6faf7c5a4d7d1004ad73e)BT\_COD\_MAJOR\_COMPUTER\_MINOR\_HANDHELD\_PC\_PDA

| #define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_HANDHELD\_PC\_PDA   0x04 |
| --- |

## [◆ ](#a8655f31e07a18335fa7a3f42635c1352)BT\_COD\_MAJOR\_COMPUTER\_MINOR\_LAPTOP

| #define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_LAPTOP   0x03 |
| --- |

## [◆ ](#a0d44dc3f155861fa6e1ea8620d957e97)BT\_COD\_MAJOR\_COMPUTER\_MINOR\_PALM\_SIZE\_PC\_PDA

| #define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_PALM\_SIZE\_PC\_PDA   0x05 |
| --- |

## [◆ ](#af247d382b726b0599b706900fe189e4d)BT\_COD\_MAJOR\_COMPUTER\_MINOR\_SERVER\_CLASS\_COMPUTER

| #define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_SERVER\_CLASS\_COMPUTER   0x02 |
| --- |

## [◆ ](#ac4a3ced7c754169af6fe24f987f80e3a)BT\_COD\_MAJOR\_COMPUTER\_MINOR\_TABLET

| #define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_TABLET   0x07 |
| --- |

## [◆ ](#aec73961628a8ba0ea835b08971d23ce3)BT\_COD\_MAJOR\_COMPUTER\_MINOR\_UNCATEGORIZED

| #define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_UNCATEGORIZED   0x00 |
| --- |

## [◆ ](#a4a02b61073979297d275c16302d1452f)BT\_COD\_MAJOR\_COMPUTER\_MINOR\_WEARABLE\_COMPUTER

| #define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_WEARABLE\_COMPUTER   0x06 |
| --- |

## [◆ ](#a129895b48ad9071017a2e97335ec6d2b)BT\_COD\_MAJOR\_DEVICE\_CLASS

| #define BT\_COD\_MAJOR\_DEVICE\_CLASS | ( |  | *cod* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))cod[1]) & 0x1FUL))

## [◆ ](#a9091627f66847298c6a1f9fa566d261d)BT\_COD\_MAJOR\_HEALTH

| #define BT\_COD\_MAJOR\_HEALTH   0x09 |
| --- |

## [◆ ](#a1daeb8de054847bcd5fbee8c5797648c)BT\_COD\_MAJOR\_IMAGING

| #define BT\_COD\_MAJOR\_IMAGING   0x06 |
| --- |

## [◆ ](#a81ce79e07c526ae4ef3be26cca65cb2d)BT\_COD\_MAJOR\_LAN\_NETWORK\_AP

| #define BT\_COD\_MAJOR\_LAN\_NETWORK\_AP   0x03 |
| --- |

## [◆ ](#ad14acbda93a611913f675175a433c6e3)BT\_COD\_MAJOR\_MISC

| #define BT\_COD\_MAJOR\_MISC   0x00 |
| --- |

## [◆ ](#ad5cf6294b462dd8b1f49c23a93deb267)BT\_COD\_MAJOR\_PERIPHERAL

| #define BT\_COD\_MAJOR\_PERIPHERAL   0x05 |
| --- |

## [◆ ](#a59dd55c19cb4d995175a49125529536f)BT\_COD\_MAJOR\_PHONE

| #define BT\_COD\_MAJOR\_PHONE   0x02 |
| --- |

## [◆ ](#a4954e6760da119f71d91624200b70344)BT\_COD\_MAJOR\_PHONE\_MINOR\_CELLULAR

| #define BT\_COD\_MAJOR\_PHONE\_MINOR\_CELLULAR   0x01 |
| --- |

## [◆ ](#ab6dc621f45cd579242a58b523cf250bf)BT\_COD\_MAJOR\_PHONE\_MINOR\_CORDLESS

| #define BT\_COD\_MAJOR\_PHONE\_MINOR\_CORDLESS   0x02 |
| --- |

## [◆ ](#a4eded4ed6985c8110e040c0a4e3b5341)BT\_COD\_MAJOR\_PHONE\_MINOR\_ISDN

| #define BT\_COD\_MAJOR\_PHONE\_MINOR\_ISDN   0x05 |
| --- |

## [◆ ](#a3c22870123a8c9015d2664e061bf095a)BT\_COD\_MAJOR\_PHONE\_MINOR\_SMARTPHONE

| #define BT\_COD\_MAJOR\_PHONE\_MINOR\_SMARTPHONE   0x03 |
| --- |

## [◆ ](#a70e534fba0ee653a1d8fffc4f57a399d)BT\_COD\_MAJOR\_PHONE\_MINOR\_UNCATEGORIZED

| #define BT\_COD\_MAJOR\_PHONE\_MINOR\_UNCATEGORIZED   0x00 |
| --- |

## [◆ ](#a7f2801f76561e04801c8cd7bc0de3cc1)BT\_COD\_MAJOR\_PHONE\_MINOR\_WIRED\_MODEM\_VOICE\_GATEWAY

| #define BT\_COD\_MAJOR\_PHONE\_MINOR\_WIRED\_MODEM\_VOICE\_GATEWAY   0x04 |
| --- |

## [◆ ](#ab598bdad77874748f74187aa32049ea6)BT\_COD\_MAJOR\_SERVICE\_CLASSES

| #define BT\_COD\_MAJOR\_SERVICE\_CLASSES | ( |  | *cod* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))cod[2] & 0xFF) >> 5) | ((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))cod[1] & 0xD0) >> 5))

## [◆ ](#a592ae9ac7a15862b8fa866a2f79d36e8)BT\_COD\_MAJOR\_TOY

| #define BT\_COD\_MAJOR\_TOY   0x08 |
| --- |

## [◆ ](#ac6cffb2a74393e469b587adc5dfb12b1)BT\_COD\_MAJOR\_UNCATEGORIZED

| #define BT\_COD\_MAJOR\_UNCATEGORIZED   0x1F |
| --- |

## [◆ ](#ac5d662f2a86144c1d9698cf0443c9ea7)BT\_COD\_MAJOR\_WEARABLE

| #define BT\_COD\_MAJOR\_WEARABLE   0x07 |
| --- |

## [◆ ](#adcf892b98d0924ea8a78d4b8b588bddb)BT\_COD\_MINOR\_DEVICE\_CLASS

| #define BT\_COD\_MINOR\_DEVICE\_CLASS | ( |  | *cod* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))cod[0]) & 0xFF) >> 2))

## [◆ ](#af2c925e431eec42930101a72b00a7283)BT\_COD\_VALID

| #define BT\_COD\_VALID | ( |  | *cod* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((0 == (cod[0] & ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1)))) ? [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) : false)

[true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)

#define true

**Definition** stdbool.h:14

## [◆ ](#a4c274cd6947d37bf4f895ca0002c4f63)BT\_ENC\_KEY\_SIZE\_MAX

| #define BT\_ENC\_KEY\_SIZE\_MAX   0x10 |
| --- |

## [◆ ](#a90a6c0c50f915c347b75ac3ca46996ac)BT\_ENC\_KEY\_SIZE\_MIN

| #define BT\_ENC\_KEY\_SIZE\_MIN   0x07 |
| --- |

## [◆ ](#a25201544478590f6ee87a829410c612b)BT\_EVT\_BIT

| #define BT\_EVT\_BIT | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(1ULL << (n))

## [◆ ](#ad4f80dd3fdf22b23d47785a507aa5a85)BT\_EVT\_MASK\_AUTH\_COMPLETE

| #define BT\_EVT\_MASK\_AUTH\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(5) |
| --- |

## [◆ ](#a33753df12afb5f7e19be01f9febc5d23)BT\_EVT\_MASK\_AUTH\_PAYLOAD\_TIMEOUT\_EXP

| #define BT\_EVT\_MASK\_AUTH\_PAYLOAD\_TIMEOUT\_EXP   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(23) |
| --- |

## [◆ ](#a35f42f297b980a050deceb71237883ba)BT\_EVT\_MASK\_CL\_PER\_BC\_CH\_MAP\_CHANGE

| #define BT\_EVT\_MASK\_CL\_PER\_BC\_CH\_MAP\_CHANGE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(21) |
| --- |

## [◆ ](#aa8842138b1146d3581c39062d11a6305)BT\_EVT\_MASK\_CL\_PER\_BC\_RX

| #define BT\_EVT\_MASK\_CL\_PER\_BC\_RX   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(17) |
| --- |

## [◆ ](#af513eaa35861cfcfefba97e0263e3f5b)BT\_EVT\_MASK\_CL\_PER\_BC\_TIMEOUT

| #define BT\_EVT\_MASK\_CL\_PER\_BC\_TIMEOUT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(18) |
| --- |

## [◆ ](#a5a13adda8bf4f015550a043667e0b67d)BT\_EVT\_MASK\_CONN\_COMPLETE

| #define BT\_EVT\_MASK\_CONN\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(2) |
| --- |

## [◆ ](#ad77bbcd4fb8b0e37700492e8a3cccd38)BT\_EVT\_MASK\_CONN\_REQUEST

| #define BT\_EVT\_MASK\_CONN\_REQUEST   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(3) |
| --- |

## [◆ ](#a829ea33c603291d331faba58689b0198)BT\_EVT\_MASK\_DATA\_BUFFER\_OVERFLOW

| #define BT\_EVT\_MASK\_DATA\_BUFFER\_OVERFLOW   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(25) |
| --- |

## [◆ ](#a5ea9d4fb977c660bc33be93c73817705)BT\_EVT\_MASK\_DISCONN\_COMPLETE

| #define BT\_EVT\_MASK\_DISCONN\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(4) |
| --- |

## [◆ ](#a334c571248a1aad285bb11bc39d2ade8)BT\_EVT\_MASK\_ENCRYPT\_CHANGE

| #define BT\_EVT\_MASK\_ENCRYPT\_CHANGE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(7) |
| --- |

## [◆ ](#af8d96cc1cf99a7130d4c181450998cb7)BT\_EVT\_MASK\_ENCRYPT\_KEY\_REFRESH\_COMPLETE

| #define BT\_EVT\_MASK\_ENCRYPT\_KEY\_REFRESH\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(47) |
| --- |

## [◆ ](#a9b361fe6314f56fcb016bacb064af815)BT\_EVT\_MASK\_EXTENDED\_INQUIRY\_RESULT

| #define BT\_EVT\_MASK\_EXTENDED\_INQUIRY\_RESULT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(46) |
| --- |

## [◆ ](#a079c00e59422034a9f977af7dd20234c)BT\_EVT\_MASK\_HARDWARE\_ERROR

| #define BT\_EVT\_MASK\_HARDWARE\_ERROR   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(15) |
| --- |

## [◆ ](#a79851cd962916f9be81e29ce9797e901)BT\_EVT\_MASK\_INQUIRY\_COMPLETE

| #define BT\_EVT\_MASK\_INQUIRY\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(0) |
| --- |

## [◆ ](#aeb5b4cbc01a8cebea5ce8e0090d37261)BT\_EVT\_MASK\_INQUIRY\_RESULT\_WITH\_RSSI

| #define BT\_EVT\_MASK\_INQUIRY\_RESULT\_WITH\_RSSI   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(33) |
| --- |

## [◆ ](#ae8106016a80e123016c6d2fc406224d7)BT\_EVT\_MASK\_INQUIRY\_RSP\_NOT

| #define BT\_EVT\_MASK\_INQUIRY\_RSP\_NOT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(22) |
| --- |

## [◆ ](#a845de3735dc3989d3a9d54cf5e55b408)BT\_EVT\_MASK\_IO\_CAPA\_REQ

| #define BT\_EVT\_MASK\_IO\_CAPA\_REQ   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(48) |
| --- |

## [◆ ](#a409e33dbe4fdb1dc90050e0b4eab1f86)BT\_EVT\_MASK\_IO\_CAPA\_RESP

| #define BT\_EVT\_MASK\_IO\_CAPA\_RESP   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(49) |
| --- |

## [◆ ](#a11330b1b6847d77d3ba88e1de0aaa36e)BT\_EVT\_MASK\_LE\_ADV\_SET\_TERMINATED

| #define BT\_EVT\_MASK\_LE\_ADV\_SET\_TERMINATED   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(17) |
| --- |

## [◆ ](#a39a55a4c3e71db708e39c8110a2349f7)BT\_EVT\_MASK\_LE\_ADVERTISING\_REPORT

| #define BT\_EVT\_MASK\_LE\_ADVERTISING\_REPORT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(1) |
| --- |

## [◆ ](#a447ff4a3e4dfba390ce9729e45abb410)BT\_EVT\_MASK\_LE\_BIG\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_BIG\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(26) |
| --- |

## [◆ ](#ab88b8bcde1d07b5f16c55c4cbf4fd20d)BT\_EVT\_MASK\_LE\_BIG\_SYNC\_ESTABLISHED

| #define BT\_EVT\_MASK\_LE\_BIG\_SYNC\_ESTABLISHED   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(28) |
| --- |

## [◆ ](#a87abdedde8bd43f845fe604c80612ca0)BT\_EVT\_MASK\_LE\_BIG\_SYNC\_LOST

| #define BT\_EVT\_MASK\_LE\_BIG\_SYNC\_LOST   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(29) |
| --- |

## [◆ ](#ad4b775d48bfa14c00c78ac1fbb8f2a2a)BT\_EVT\_MASK\_LE\_BIG\_TERMINATED

| #define BT\_EVT\_MASK\_LE\_BIG\_TERMINATED   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(27) |
| --- |

## [◆ ](#aff9c37de1e55e6a7085b3a521f34d3e0)BT\_EVT\_MASK\_LE\_BIGINFO\_ADV\_REPORT

| #define BT\_EVT\_MASK\_LE\_BIGINFO\_ADV\_REPORT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(33) |
| --- |

## [◆ ](#acee0428356c4853fe664709fc1675f02)BT\_EVT\_MASK\_LE\_CHAN\_SEL\_ALGO

| #define BT\_EVT\_MASK\_LE\_CHAN\_SEL\_ALGO   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(19) |
| --- |

## [◆ ](#a9e41b4cb965576490fb39f7dc396722f)BT\_EVT\_MASK\_LE\_CIS\_ESTABLISHED

| #define BT\_EVT\_MASK\_LE\_CIS\_ESTABLISHED   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(24) |
| --- |

## [◆ ](#a1b02618f1fbfb3a710fd413f205da9a6)BT\_EVT\_MASK\_LE\_CIS\_ESTABLISHED\_V2

| #define BT\_EVT\_MASK\_LE\_CIS\_ESTABLISHED\_V2   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(41) |
| --- |

## [◆ ](#aa24e9569ace049098a6d822ad7433e26)BT\_EVT\_MASK\_LE\_CIS\_REQ

| #define BT\_EVT\_MASK\_LE\_CIS\_REQ   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(25) |
| --- |

## [◆ ](#a59cd7a15e5b562adb6397509463e375c)BT\_EVT\_MASK\_LE\_CONN\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_CONN\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(0) |
| --- |

## [◆ ](#ac3eeaa0610a6ac6d3b57880042071f2a)BT\_EVT\_MASK\_LE\_CONN\_PARAM\_REQ

| #define BT\_EVT\_MASK\_LE\_CONN\_PARAM\_REQ   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(5) |
| --- |

## [◆ ](#ab1988671f4017f6434dc0438b2e8b9f6)BT\_EVT\_MASK\_LE\_CONN\_UPDATE\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_CONN\_UPDATE\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(2) |
| --- |

## [◆ ](#a3b2f133db5641414b95bfd953d715ff3)BT\_EVT\_MASK\_LE\_CONNECTION\_IQ\_REPORT

| #define BT\_EVT\_MASK\_LE\_CONNECTION\_IQ\_REPORT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(21) |
| --- |

## [◆ ](#a6ef13decc171530c00f12b0226fa9ed1)BT\_EVT\_MASK\_LE\_CONNECTIONLESS\_IQ\_REPORT

| #define BT\_EVT\_MASK\_LE\_CONNECTIONLESS\_IQ\_REPORT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(20) |
| --- |

## [◆ ](#abe6f94ab4bae0d34f23e27c0948e3a21)BT\_EVT\_MASK\_LE\_CS\_CONFIG\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_CS\_CONFIG\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(46) |
| --- |

## [◆ ](#affbe9c98cf94e50673a2a59c8fb68256)BT\_EVT\_MASK\_LE\_CS\_PROCEDURE\_ENABLE\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_CS\_PROCEDURE\_ENABLE\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(47) |
| --- |

## [◆ ](#a406cdb92d8c6524aca8971425bab7baa)BT\_EVT\_MASK\_LE\_CS\_READ\_REMOTE\_FAE\_TABLE\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_CS\_READ\_REMOTE\_FAE\_TABLE\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(44) |
| --- |

## [◆ ](#a97d1b704b1638fb85fa4da6f6d31e209)BT\_EVT\_MASK\_LE\_CS\_READ\_REMOTE\_SUPPORTED\_CAPABILITIES\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_CS\_READ\_REMOTE\_SUPPORTED\_CAPABILITIES\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(43) |
| --- |

## [◆ ](#a07b9cc5a2fcc73d56590a034977cf3a0)BT\_EVT\_MASK\_LE\_CS\_SECURITY\_ENABLE\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_CS\_SECURITY\_ENABLE\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(45) |
| --- |

## [◆ ](#a040ef537fe66f923dc3c344fee023002)BT\_EVT\_MASK\_LE\_CS\_SUBEVENT\_RESULT

| #define BT\_EVT\_MASK\_LE\_CS\_SUBEVENT\_RESULT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(48) |
| --- |

## [◆ ](#a226c276713e3cf16108e4a66fad6db79)BT\_EVT\_MASK\_LE\_CS\_SUBEVENT\_RESULT\_CONTINUE

| #define BT\_EVT\_MASK\_LE\_CS\_SUBEVENT\_RESULT\_CONTINUE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(49) |
| --- |

## [◆ ](#a8a6ec9510323355aa003cb8be519be7d)BT\_EVT\_MASK\_LE\_CS\_TEST\_END\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_CS\_TEST\_END\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(50) |
| --- |

## [◆ ](#afbd3991be814ec6462d62fbc4c898ac0)BT\_EVT\_MASK\_LE\_CTE\_REQUEST\_FAILED

| #define BT\_EVT\_MASK\_LE\_CTE\_REQUEST\_FAILED   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(22) |
| --- |

## [◆ ](#a73489ce7067d812e8443e242ee53a5e6)BT\_EVT\_MASK\_LE\_DATA\_LEN\_CHANGE

| #define BT\_EVT\_MASK\_LE\_DATA\_LEN\_CHANGE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(6) |
| --- |

## [◆ ](#a3e84268b1e701ae37c77e95847490222)BT\_EVT\_MASK\_LE\_DIRECT\_ADV\_REPORT

| #define BT\_EVT\_MASK\_LE\_DIRECT\_ADV\_REPORT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(10) |
| --- |

## [◆ ](#afb3b477cb835e60c3e77237451ebae5b)BT\_EVT\_MASK\_LE\_ENH\_CONN\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_ENH\_CONN\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(9) |
| --- |

## [◆ ](#a8b40a701334d25741a6e17ffd86576ad)BT\_EVT\_MASK\_LE\_ENH\_CONN\_COMPLETE\_V2

| #define BT\_EVT\_MASK\_LE\_ENH\_CONN\_COMPLETE\_V2   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(40) |
| --- |

## [◆ ](#a1d7fc1a3ea229622560de8cf0bb63a81)BT\_EVT\_MASK\_LE\_EXT\_ADVERTISING\_REPORT

| #define BT\_EVT\_MASK\_LE\_EXT\_ADVERTISING\_REPORT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(12) |
| --- |

## [◆ ](#afbe64037a16680397614ba2db136b452)BT\_EVT\_MASK\_LE\_GENERATE\_DHKEY\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_GENERATE\_DHKEY\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(8) |
| --- |

## [◆ ](#ab495948af67d01208eff1adb9a33e489)BT\_EVT\_MASK\_LE\_LTK\_REQUEST

| #define BT\_EVT\_MASK\_LE\_LTK\_REQUEST   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(4) |
| --- |

## [◆ ](#a59f89d39350b396f8d0c986e2d477bba)BT\_EVT\_MASK\_LE\_META\_EVENT

| #define BT\_EVT\_MASK\_LE\_META\_EVENT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(61) |
| --- |

## [◆ ](#a281d70b2b596b918972b59e684b6a476)BT\_EVT\_MASK\_LE\_P256\_PUBLIC\_KEY\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_P256\_PUBLIC\_KEY\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(7) |
| --- |

## [◆ ](#a5b2139ce8847bfcdbcd99c3241fb5ea2)BT\_EVT\_MASK\_LE\_PAST\_RECEIVED

| #define BT\_EVT\_MASK\_LE\_PAST\_RECEIVED   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(23) |
| --- |

## [◆ ](#a93aec31c1636fec90b609981736eb2de)BT\_EVT\_MASK\_LE\_PAST\_RECEIVED\_V2

| #define BT\_EVT\_MASK\_LE\_PAST\_RECEIVED\_V2   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(37) |
| --- |

## [◆ ](#a6aad398435aa48ba67f6917bca2a690e)BT\_EVT\_MASK\_LE\_PATH\_LOSS\_THRESHOLD

| #define BT\_EVT\_MASK\_LE\_PATH\_LOSS\_THRESHOLD   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(31) |
| --- |

## [◆ ](#ab8a9486fedec169e4d44b249f2445acf)BT\_EVT\_MASK\_LE\_PER\_ADV\_RESPONSE\_REPORT

| #define BT\_EVT\_MASK\_LE\_PER\_ADV\_RESPONSE\_REPORT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(39) |
| --- |

## [◆ ](#af0e2c2e66bdac52fbe5e9c91ca26fe49)BT\_EVT\_MASK\_LE\_PER\_ADV\_SUBEVENT\_DATA\_REQ

| #define BT\_EVT\_MASK\_LE\_PER\_ADV\_SUBEVENT\_DATA\_REQ   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(38) |
| --- |

## [◆ ](#a96142f5d79029a93a99152ade46fc005)BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_ESTABLISHED

| #define BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_ESTABLISHED   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(13) |
| --- |

## [◆ ](#a92a360ad268c29e1616de1e16748eb44)BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_ESTABLISHED\_V2

| #define BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_ESTABLISHED\_V2   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(35) |
| --- |

## [◆ ](#ae78587797f24987f36c348fe790438b2)BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_LOST

| #define BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_LOST   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(15) |
| --- |

## [◆ ](#ad7fc62afd0e1e3dc040567d91320e18e)BT\_EVT\_MASK\_LE\_PER\_ADVERTISING\_REPORT

| #define BT\_EVT\_MASK\_LE\_PER\_ADVERTISING\_REPORT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(14) |
| --- |

## [◆ ](#ad78d5a027581dee52c54bb3f5a19b68d)BT\_EVT\_MASK\_LE\_PER\_ADVERTISING\_REPORT\_V2

| #define BT\_EVT\_MASK\_LE\_PER\_ADVERTISING\_REPORT\_V2   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(36) |
| --- |

## [◆ ](#ab5f6014468b107486aba04ba698453ed)BT\_EVT\_MASK\_LE\_PHY\_UPDATE\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_PHY\_UPDATE\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(11) |
| --- |

## [◆ ](#adba1a3a872ee26a41218c9104e9f957b)BT\_EVT\_MASK\_LE\_REMOTE\_FEAT\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_REMOTE\_FEAT\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(3) |
| --- |

## [◆ ](#a01e518d3bb3d4f99c335743362a84080)BT\_EVT\_MASK\_LE\_REQ\_PEER\_SCA\_COMPLETE

| #define BT\_EVT\_MASK\_LE\_REQ\_PEER\_SCA\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(30) |
| --- |

## [◆ ](#a3f13865e913a1c6afb6d8d05a6d84608)BT\_EVT\_MASK\_LE\_SCAN\_REQ\_RECEIVED

| #define BT\_EVT\_MASK\_LE\_SCAN\_REQ\_RECEIVED   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(18) |
| --- |

## [◆ ](#a372f6b8e355972d63e5f9ff45a486e9d)BT\_EVT\_MASK\_LE\_SCAN\_TIMEOUT

| #define BT\_EVT\_MASK\_LE\_SCAN\_TIMEOUT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(16) |
| --- |

## [◆ ](#a8a52784fd872a8ee6f666c31e846411d)BT\_EVT\_MASK\_LE\_SUBRATE\_CHANGE

| #define BT\_EVT\_MASK\_LE\_SUBRATE\_CHANGE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(34) |
| --- |

## [◆ ](#a7f9d3cdf0de067ad408bec600b9a691f)BT\_EVT\_MASK\_LE\_TRANSMIT\_POWER\_REPORTING

| #define BT\_EVT\_MASK\_LE\_TRANSMIT\_POWER\_REPORTING   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(32) |
| --- |

## [◆ ](#aa20a3ce217a60070826d0b55ebd105be)BT\_EVT\_MASK\_LINK\_KEY\_NOTIFY

| #define BT\_EVT\_MASK\_LINK\_KEY\_NOTIFY   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(23) |
| --- |

## [◆ ](#a1e16ab7caf239e804c0c2057e9b49e42)BT\_EVT\_MASK\_LINK\_KEY\_REQ

| #define BT\_EVT\_MASK\_LINK\_KEY\_REQ   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(22) |
| --- |

## [◆ ](#abe39e63cbdee9bfeac36a1b6a4d40aba)BT\_EVT\_MASK\_NUM\_COMPLETE\_DATA\_BLOCKS

| #define BT\_EVT\_MASK\_NUM\_COMPLETE\_DATA\_BLOCKS   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(8) |
| --- |

## [◆ ](#ad078befa197baac20294dc0d46eff9dd)BT\_EVT\_MASK\_PER\_PAGE\_RSP\_TIMEOUT

| #define BT\_EVT\_MASK\_PER\_PAGE\_RSP\_TIMEOUT   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(20) |
| --- |

## [◆ ](#a9f5612d89848aafb6e9063a55e5cd6b4)BT\_EVT\_MASK\_PIN\_CODE\_REQ

| #define BT\_EVT\_MASK\_PIN\_CODE\_REQ   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(21) |
| --- |

## [◆ ](#a9d3bbaa1eb1dbe72714b922dcada3347)BT\_EVT\_MASK\_REMOTE\_EXT\_FEATURES

| #define BT\_EVT\_MASK\_REMOTE\_EXT\_FEATURES   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(34) |
| --- |

## [◆ ](#a7ccade60a01e0f8a175b3b11b5e20f6d)BT\_EVT\_MASK\_REMOTE\_FEATURES

| #define BT\_EVT\_MASK\_REMOTE\_FEATURES   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(10) |
| --- |

## [◆ ](#a4433027483d6d63911b59c4fe605ba69)BT\_EVT\_MASK\_REMOTE\_NAME\_REQ\_COMPLETE

| #define BT\_EVT\_MASK\_REMOTE\_NAME\_REQ\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(6) |
| --- |

## [◆ ](#a87331cabdea78ace1577cbf2fa7e3523)BT\_EVT\_MASK\_REMOTE\_VERSION\_INFO

| #define BT\_EVT\_MASK\_REMOTE\_VERSION\_INFO   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(11) |
| --- |

## [◆ ](#a4b4a80b51b2c20bf28fbfac57679a86e)BT\_EVT\_MASK\_ROLE\_CHANGE

| #define BT\_EVT\_MASK\_ROLE\_CHANGE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(17) |
| --- |

## [◆ ](#a8bfac36e993c48d12bdeb7c130fdd6dc)BT\_EVT\_MASK\_SAM\_STATUS\_CHANGE

| #define BT\_EVT\_MASK\_SAM\_STATUS\_CHANGE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(24) |
| --- |

## [◆ ](#a6a08ace148ea2728614a3bab02c21f65)BT\_EVT\_MASK\_SSP\_COMPLETE

| #define BT\_EVT\_MASK\_SSP\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(53) |
| --- |

## [◆ ](#a4f1a905136cb713c09fb5197dd099ce2)BT\_EVT\_MASK\_SYNC\_CONN\_COMPLETE

| #define BT\_EVT\_MASK\_SYNC\_CONN\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(43) |
| --- |

## [◆ ](#ac078d5b46d7e227726cb7456e2163d3f)BT\_EVT\_MASK\_SYNCH\_TRAIN\_COMPLETE

| #define BT\_EVT\_MASK\_SYNCH\_TRAIN\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(15) |
| --- |

## [◆ ](#a8901b477ec3584af207b3648b221bb92)BT\_EVT\_MASK\_SYNCH\_TRAIN\_RX

| #define BT\_EVT\_MASK\_SYNCH\_TRAIN\_RX   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(16) |
| --- |

## [◆ ](#aff43216feb0c29c6813d198473f34fdc)BT\_EVT\_MASK\_TRIGG\_CLOCK\_CAPTURE

| #define BT\_EVT\_MASK\_TRIGG\_CLOCK\_CAPTURE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(14) |
| --- |

## [◆ ](#a9b82f06f42651c32f4c0db9826002134)BT\_EVT\_MASK\_TRUNC\_PAGE\_COMPLETE

| #define BT\_EVT\_MASK\_TRUNC\_PAGE\_COMPLETE   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(19) |
| --- |

## [◆ ](#a1c04cc7d04f056e5edfc4ddaa97c657f)BT\_EVT\_MASK\_USER\_CONFIRM\_REQ

| #define BT\_EVT\_MASK\_USER\_CONFIRM\_REQ   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(50) |
| --- |

## [◆ ](#a2eb47347a5685a290087b236d696971e)BT\_EVT\_MASK\_USER\_PASSKEY\_NOTIFY

| #define BT\_EVT\_MASK\_USER\_PASSKEY\_NOTIFY   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(58) |
| --- |

## [◆ ](#af56d87ffc24c2e4c08db68ab019fd58e)BT\_EVT\_MASK\_USER\_PASSKEY\_REQ

| #define BT\_EVT\_MASK\_USER\_PASSKEY\_REQ   [BT\_EVT\_BIT](#a25201544478590f6ee87a829410c612b)(51) |
| --- |

## [◆ ](#a8dbbf37965a9d0ddab5a07f88d7cd7ca)BT\_FEAT\_2EV3\_PKT

| #define BT\_FEAT\_2EV3\_PKT | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 0, 5, 5)

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)

#define BT\_FEAT\_TEST(feat, page, octet, bit)

**Definition** hci\_types.h:142

## [◆ ](#a00aec89aa4d1504934e85ec79462b346)BT\_FEAT\_3EV3\_PKT

| #define BT\_FEAT\_3EV3\_PKT | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 0, 5, 6)

## [◆ ](#a5219ff658b46cf28104a99f089854444)BT\_FEAT\_3SLOT\_PKT

| #define BT\_FEAT\_3SLOT\_PKT | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 0, 5, 7)

## [◆ ](#a5508c481ff6b8fd46f2f2c077aaa90c9)BT\_FEAT\_BREDR

| #define BT\_FEAT\_BREDR | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

![BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 0, 4, 5)

## [◆ ](#ad154d0649e8e90c1102b74cae8327fa7)BT\_FEAT\_EV4\_PKT

| #define BT\_FEAT\_EV4\_PKT | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 0, 4, 0)

## [◆ ](#a0a6b9afb4673dc852e1a4d8e867003c9)BT\_FEAT\_EV5\_PKT

| #define BT\_FEAT\_EV5\_PKT | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 0, 4, 1)

## [◆ ](#ac26ebac4f1641d5ff4484f74579852d7)BT\_FEAT\_EXT\_FEATURES

| #define BT\_FEAT\_EXT\_FEATURES | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 0, 7, 7)

## [◆ ](#af011519b6fb0477ac7f87e5dc98daed0)BT\_FEAT\_HOST\_SSP

| #define BT\_FEAT\_HOST\_SSP | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 1, 0, 0)

## [◆ ](#ad59c138e945d7f27d3befc286b679e03)BT\_FEAT\_HV2\_PKT

| #define BT\_FEAT\_HV2\_PKT | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 0, 1, 4)

## [◆ ](#aed6f11d60161c919b4d2b7eb13f46e47)BT\_FEAT\_HV3\_PKT

| #define BT\_FEAT\_HV3\_PKT | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 0, 1, 5)

## [◆ ](#a8b1df8d6b9e0dfcaa13635588cc3bfe3)BT\_FEAT\_LE

| #define BT\_FEAT\_LE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 0, 4, 6)

## [◆ ](#af10735230c38d2b5a0baf5377212e827)BT\_FEAT\_LE\_ADV\_CODING\_SEL

| #define BT\_FEAT\_LE\_ADV\_CODING\_SEL | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL](#a4d920d42e8042c9117f97e334f889f51))

[BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL](#a4d920d42e8042c9117f97e334f889f51)

#define BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL

**Definition** hci\_types.h:201

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)

#define BT\_LE\_FEAT\_TEST(feat, n)

**Definition** hci\_types.h:210

## [◆ ](#aecf06a32c61c783305ad3817f9e5a596)BT\_FEAT\_LE\_ADV\_CODING\_SEL\_HOST

| #define BT\_FEAT\_LE\_ADV\_CODING\_SEL\_HOST | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL\_HOST](#ad711e7491883e1f1e068fe167cca8a4e))

[BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL\_HOST](#ad711e7491883e1f1e068fe167cca8a4e)

#define BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL\_HOST

**Definition** hci\_types.h:202

## [◆ ](#a1c3c0e6a213b71e680ca24738047f09a)BT\_FEAT\_LE\_ANT\_SWITCH\_RX\_AOA

| #define BT\_FEAT\_LE\_ANT\_SWITCH\_RX\_AOA | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_RX\_AOA](#a480fc67a1c8a2f36410f285ef0ee36e7))

[BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_RX\_AOA](#a480fc67a1c8a2f36410f285ef0ee36e7)

#define BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_RX\_AOA

**Definition** hci\_types.h:183

## [◆ ](#ae503f9186d39fbea2347036c891fc8bf)BT\_FEAT\_LE\_ANT\_SWITCH\_TX\_AOD

| #define BT\_FEAT\_LE\_ANT\_SWITCH\_TX\_AOD | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_TX\_AOD](#a41eae1585972ae6792eb1a639c2e3a8e))

[BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_TX\_AOD](#a41eae1585972ae6792eb1a639c2e3a8e)

#define BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_TX\_AOD

**Definition** hci\_types.h:182

## [◆ ](#a46b2f535c74178c8cc9359a7b1d2e140)BT\_FEAT\_LE\_BIS

| #define BT\_FEAT\_LE\_BIS | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([BT\_FEAT\_LE\_ISO\_BROADCASTER](#a1c6fd06877a5606ae33aedc45a71f853)(feat) | \

BT\_FEAT\_LE\_SYNC\_RECEIVER(feat))

[BT\_FEAT\_LE\_ISO\_BROADCASTER](#a1c6fd06877a5606ae33aedc45a71f853)

#define BT\_FEAT\_LE\_ISO\_BROADCASTER(feat)

**Definition** hci\_types.h:253

## [◆ ](#abb7763cc16340d23bc7d687e60badcc0)BT\_FEAT\_LE\_CHANNEL\_CLASSIFICATION

| #define BT\_FEAT\_LE\_CHANNEL\_CLASSIFICATION | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_CHANNEL\_CLASSIFICATION](#af2a4be520b4d8c3eb56231b865738e90))

[BT\_LE\_FEAT\_BIT\_CHANNEL\_CLASSIFICATION](#af2a4be520b4d8c3eb56231b865738e90)

#define BT\_LE\_FEAT\_BIT\_CHANNEL\_CLASSIFICATION

**Definition** hci\_types.h:200

## [◆ ](#a7b13b55fd2cfb4d756d3591215b47b7e)BT\_FEAT\_LE\_CHANNEL\_SOUNDING

| #define BT\_FEAT\_LE\_CHANNEL\_SOUNDING | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING](#ab918084874aace22954aa748333baf6d))

[BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING](#ab918084874aace22954aa748333baf6d)

#define BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING

**Definition** hci\_types.h:207

## [◆ ](#aff2b8ca285698906deecfeff7447a74a)BT\_FEAT\_LE\_CHANNEL\_SOUNDING\_HOST

| #define BT\_FEAT\_LE\_CHANNEL\_SOUNDING\_HOST | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING\_HOST](#aa4572a11d78651ce775a010178c6dfa2))

[BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING\_HOST](#aa4572a11d78651ce775a010178c6dfa2)

#define BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING\_HOST

**Definition** hci\_types.h:208

## [◆ ](#abe5a1ddbede473f583106e3500dccdb1)BT\_FEAT\_LE\_CIS

| #define BT\_FEAT\_LE\_CIS | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([BT\_FEAT\_LE\_CIS\_CENTRAL](#adce7c3804a224e7b7317728fa27d4945)(feat) | \

BT\_FEAT\_LE\_CIS\_PERIPHERAL(feat))

[BT\_FEAT\_LE\_CIS\_CENTRAL](#adce7c3804a224e7b7317728fa27d4945)

#define BT\_FEAT\_LE\_CIS\_CENTRAL(feat)

**Definition** hci\_types.h:249

## [◆ ](#adce7c3804a224e7b7317728fa27d4945)BT\_FEAT\_LE\_CIS\_CENTRAL

| #define BT\_FEAT\_LE\_CIS\_CENTRAL | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_CIS\_CENTRAL](#aa98eed376b6d5263621f14c55d776088))

[BT\_LE\_FEAT\_BIT\_CIS\_CENTRAL](#aa98eed376b6d5263621f14c55d776088)

#define BT\_LE\_FEAT\_BIT\_CIS\_CENTRAL

**Definition** hci\_types.h:189

## [◆ ](#a8a6860b285b3b4401021ba16f59404ce)BT\_FEAT\_LE\_CIS\_PERIPHERAL

| #define BT\_FEAT\_LE\_CIS\_PERIPHERAL | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_CIS\_PERIPHERAL](#a298fde96c2d6376e3333a99f7e03409d))

[BT\_LE\_FEAT\_BIT\_CIS\_PERIPHERAL](#a298fde96c2d6376e3333a99f7e03409d)

#define BT\_LE\_FEAT\_BIT\_CIS\_PERIPHERAL

**Definition** hci\_types.h:190

## [◆ ](#a554c027fb3946de6f861ea267968ba17)BT\_FEAT\_LE\_CONN\_PARAM\_REQ\_PROC

| #define BT\_FEAT\_LE\_CONN\_PARAM\_REQ\_PROC | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_CONN\_PARAM\_REQ](#ab816048bdd6c1e42b0e458abebb76572))

[BT\_LE\_FEAT\_BIT\_CONN\_PARAM\_REQ](#ab816048bdd6c1e42b0e458abebb76572)

#define BT\_LE\_FEAT\_BIT\_CONN\_PARAM\_REQ

**Definition** hci\_types.h:162

## [◆ ](#a75bf595ba1e16deeeedb45a55f470620)BT\_FEAT\_LE\_CONN\_SUBRATING

| #define BT\_FEAT\_LE\_CONN\_SUBRATING | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING](#aa45b06a49232372891ceb5e4496d46da))

[BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING](#aa45b06a49232372891ceb5e4496d46da)

#define BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING

**Definition** hci\_types.h:198

## [◆ ](#a37adeecbf4c200cf8b060344718e7949)BT\_FEAT\_LE\_CONN\_SUBRATING\_HOST\_SUPP

| #define BT\_FEAT\_LE\_CONN\_SUBRATING\_HOST\_SUPP | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING\_HOST\_SUPP](#adb884a30bc1a24e3dfb115cef7149c81))

[BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING\_HOST\_SUPP](#adb884a30bc1a24e3dfb115cef7149c81)

#define BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING\_HOST\_SUPP

**Definition** hci\_types.h:199

## [◆ ](#a51316a5b67950e7644dfb71c4c6baa96)BT\_FEAT\_LE\_CONNECTION\_CTE\_REQ

| #define BT\_FEAT\_LE\_CONNECTION\_CTE\_REQ | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_CONN\_CTE\_REQ](#aed34742e8554b830c3b6c4bf04f0e2db))

[BT\_LE\_FEAT\_BIT\_CONN\_CTE\_REQ](#aed34742e8554b830c3b6c4bf04f0e2db)

#define BT\_LE\_FEAT\_BIT\_CONN\_CTE\_REQ

**Definition** hci\_types.h:178

## [◆ ](#a0cdc67a1345969d3504380fce94a4cda)BT\_FEAT\_LE\_CONNECTION\_CTE\_RESP

| #define BT\_FEAT\_LE\_CONNECTION\_CTE\_RESP | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_CONN\_CTE\_RESP](#aa5279a2ce26decb5856a6b709d0641c9))

[BT\_LE\_FEAT\_BIT\_CONN\_CTE\_RESP](#aa5279a2ce26decb5856a6b709d0641c9)

#define BT\_LE\_FEAT\_BIT\_CONN\_CTE\_RESP

**Definition** hci\_types.h:179

## [◆ ](#aeb0639a8e5cbc904d7f5c02d72375913)BT\_FEAT\_LE\_CONNECTIONLESS\_CTE\_RX

| #define BT\_FEAT\_LE\_CONNECTIONLESS\_CTE\_RX | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_RX](#a6abf01c846a5d637ca98997f6cfc263d))

[BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_RX](#a6abf01c846a5d637ca98997f6cfc263d)

#define BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_RX

**Definition** hci\_types.h:181

## [◆ ](#a81e30f5630750ce4f805748fbe14b456)BT\_FEAT\_LE\_CONNECTIONLESS\_CTE\_TX

| #define BT\_FEAT\_LE\_CONNECTIONLESS\_CTE\_TX | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_TX](#a331e7697a3fdc073abba5dd0ff47346b))

[BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_TX](#a331e7697a3fdc073abba5dd0ff47346b)

#define BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_TX

**Definition** hci\_types.h:180

## [◆ ](#a62e7d152cd9dfabf5b1420945099ecb6)BT\_FEAT\_LE\_DLE

| #define BT\_FEAT\_LE\_DLE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_DLE](#ac09127210b281e5ee45fbc134df64aa6))

[BT\_LE\_FEAT\_BIT\_DLE](#ac09127210b281e5ee45fbc134df64aa6)

#define BT\_LE\_FEAT\_BIT\_DLE

**Definition** hci\_types.h:166

## [◆ ](#a51464aacf5bbcbfb873fa6c757bbcd79)BT\_FEAT\_LE\_ENCR

| #define BT\_FEAT\_LE\_ENCR | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_ENC](#abd616dd5af5ed3742be9bae400ded848))

[BT\_LE\_FEAT\_BIT\_ENC](#abd616dd5af5ed3742be9bae400ded848)

#define BT\_LE\_FEAT\_BIT\_ENC

**Definition** hci\_types.h:161

## [◆ ](#a8bce94a732d28ce74ad2663e01da09b2)BT\_FEAT\_LE\_EXT\_ADV

| #define BT\_FEAT\_LE\_EXT\_ADV | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_EXT\_ADV](#ae1a0751e7c380117c4e31741712096a4))

[BT\_LE\_FEAT\_BIT\_EXT\_ADV](#ae1a0751e7c380117c4e31741712096a4)

#define BT\_LE\_FEAT\_BIT\_EXT\_ADV

**Definition** hci\_types.h:173

## [◆ ](#a5d479d919db4920b7a53c054e4ae7a19)BT\_FEAT\_LE\_EXT\_PER\_ADV

| #define BT\_FEAT\_LE\_EXT\_PER\_ADV | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PER\_ADV](#a1ac5bab6d48775b4e63e249b5759a683))

[BT\_LE\_FEAT\_BIT\_PER\_ADV](#a1ac5bab6d48775b4e63e249b5759a683)

#define BT\_LE\_FEAT\_BIT\_PER\_ADV

**Definition** hci\_types.h:174

## [◆ ](#a7b1b490bf00af8b0bf8ecbf4ef4aaba3)BT\_FEAT\_LE\_ISO

| #define BT\_FEAT\_LE\_ISO | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([BT\_FEAT\_LE\_CIS](#abe5a1ddbede473f583106e3500dccdb1)(feat) | \

BT\_FEAT\_LE\_BIS(feat))

[BT\_FEAT\_LE\_CIS](#abe5a1ddbede473f583106e3500dccdb1)

#define BT\_FEAT\_LE\_CIS(feat)

**Definition** hci\_types.h:286

## [◆ ](#a1c6fd06877a5606ae33aedc45a71f853)BT\_FEAT\_LE\_ISO\_BROADCASTER

| #define BT\_FEAT\_LE\_ISO\_BROADCASTER | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_ISO\_BROADCASTER](#af08a1ffd734d1c211f38d90b4fe72417))

[BT\_LE\_FEAT\_BIT\_ISO\_BROADCASTER](#af08a1ffd734d1c211f38d90b4fe72417)

#define BT\_LE\_FEAT\_BIT\_ISO\_BROADCASTER

**Definition** hci\_types.h:191

## [◆ ](#a0b24b74715fbf84c2da2dd2cbbb34605)BT\_FEAT\_LE\_ISO\_CHANNELS

| #define BT\_FEAT\_LE\_ISO\_CHANNELS | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_ISO\_CHANNELS](#a0d80ccb33d263abd3b42de1b69cfeeeb))

[BT\_LE\_FEAT\_BIT\_ISO\_CHANNELS](#a0d80ccb33d263abd3b42de1b69cfeeeb)

#define BT\_LE\_FEAT\_BIT\_ISO\_CHANNELS

**Definition** hci\_types.h:193

## [◆ ](#a7a88046c26b3603a2bb8b0f2ee158b5f)BT\_FEAT\_LE\_PAST\_RECV

| #define BT\_FEAT\_LE\_PAST\_RECV | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PAST\_RECV](#a28a862eaf11f8b45237f3b87e4bb15c7))

[BT\_LE\_FEAT\_BIT\_PAST\_RECV](#a28a862eaf11f8b45237f3b87e4bb15c7)

#define BT\_LE\_FEAT\_BIT\_PAST\_RECV

**Definition** hci\_types.h:186

## [◆ ](#a9e68dcf290273a4a140645c187cd7aee)BT\_FEAT\_LE\_PAST\_SEND

| #define BT\_FEAT\_LE\_PAST\_SEND | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PAST\_SEND](#aa05da01a6a9b9ac26423d6fc2661f3db))

[BT\_LE\_FEAT\_BIT\_PAST\_SEND](#aa05da01a6a9b9ac26423d6fc2661f3db)

#define BT\_LE\_FEAT\_BIT\_PAST\_SEND

**Definition** hci\_types.h:185

## [◆ ](#a8d771bd34d22853f117dbbd41ef4afe5)BT\_FEAT\_LE\_PATH\_LOSS\_MONITOR

| #define BT\_FEAT\_LE\_PATH\_LOSS\_MONITOR | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PATH\_LOSS\_MONITOR](#a434fb43b6b3176393f5d22d3932d69fa))

[BT\_LE\_FEAT\_BIT\_PATH\_LOSS\_MONITOR](#a434fb43b6b3176393f5d22d3932d69fa)

#define BT\_LE\_FEAT\_BIT\_PATH\_LOSS\_MONITOR

**Definition** hci\_types.h:196

## [◆ ](#ac5d15de2be03bc837afdb33905ea40be)BT\_FEAT\_LE\_PAWR\_ADVERTISER

| #define BT\_FEAT\_LE\_PAWR\_ADVERTISER | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PAWR\_ADVERTISER](#af251cb9d905586fd53113f5920038dae))

[BT\_LE\_FEAT\_BIT\_PAWR\_ADVERTISER](#af251cb9d905586fd53113f5920038dae)

#define BT\_LE\_FEAT\_BIT\_PAWR\_ADVERTISER

**Definition** hci\_types.h:204

## [◆ ](#a3ee6277e0e4db5e925912e8cb89269fa)BT\_FEAT\_LE\_PAWR\_SCANNER

| #define BT\_FEAT\_LE\_PAWR\_SCANNER | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PAWR\_SCANNER](#a00bb51972e0db07be84d4f3dfd007cea))

[BT\_LE\_FEAT\_BIT\_PAWR\_SCANNER](#a00bb51972e0db07be84d4f3dfd007cea)

#define BT\_LE\_FEAT\_BIT\_PAWR\_SCANNER

**Definition** hci\_types.h:205

## [◆ ](#a6213deacc8582f14546b23331d41c3a3)BT\_FEAT\_LE\_PER\_ADV\_ADI\_SUPP

| #define BT\_FEAT\_LE\_PER\_ADV\_ADI\_SUPP | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PER\_ADV\_ADI\_SUPP](#ad5a8221cb25d79b63f1a574699983038))

[BT\_LE\_FEAT\_BIT\_PER\_ADV\_ADI\_SUPP](#ad5a8221cb25d79b63f1a574699983038)

#define BT\_LE\_FEAT\_BIT\_PER\_ADV\_ADI\_SUPP

**Definition** hci\_types.h:197

## [◆ ](#a132b2561dcd4140458fb612b6e0d8b25)BT\_FEAT\_LE\_PER\_INIT\_FEAT\_XCHG

| #define BT\_FEAT\_LE\_PER\_INIT\_FEAT\_XCHG | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PER\_INIT\_FEAT\_XCHG](#aeaea6ea6595de9e3283fd6063bf7c579))

[BT\_LE\_FEAT\_BIT\_PER\_INIT\_FEAT\_XCHG](#aeaea6ea6595de9e3283fd6063bf7c579)

#define BT\_LE\_FEAT\_BIT\_PER\_INIT\_FEAT\_XCHG

**Definition** hci\_types.h:164

## [◆ ](#aaf11993f4938bb4894cdd317f9386fa3)BT\_FEAT\_LE\_PHY\_2M

| #define BT\_FEAT\_LE\_PHY\_2M | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PHY\_2M](#afcbc8d664c8e924b777c06ffb4c17315))

[BT\_LE\_FEAT\_BIT\_PHY\_2M](#afcbc8d664c8e924b777c06ffb4c17315)

#define BT\_LE\_FEAT\_BIT\_PHY\_2M

**Definition** hci\_types.h:169

## [◆ ](#abb89a0bebe4046ae310b01dd27e02c99)BT\_FEAT\_LE\_PHY\_CODED

| #define BT\_FEAT\_LE\_PHY\_CODED | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PHY\_CODED](#a800686aa45cf336fbd6efc76b3752959))

[BT\_LE\_FEAT\_BIT\_PHY\_CODED](#a800686aa45cf336fbd6efc76b3752959)

#define BT\_LE\_FEAT\_BIT\_PHY\_CODED

**Definition** hci\_types.h:172

## [◆ ](#a0b2781f29085a5807d0b2235c32f5173)BT\_FEAT\_LE\_PRIVACY

| #define BT\_FEAT\_LE\_PRIVACY | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PRIVACY](#a3c4196c04a73aa537baa845e061e9654))

[BT\_LE\_FEAT\_BIT\_PRIVACY](#a3c4196c04a73aa537baa845e061e9654)

#define BT\_LE\_FEAT\_BIT\_PRIVACY

**Definition** hci\_types.h:167

## [◆ ](#a342ce6074faa59b507cf179868e612ba)BT\_FEAT\_LE\_PWR\_CHG\_IND

| #define BT\_FEAT\_LE\_PWR\_CHG\_IND | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PWR\_CHG\_IND](#a0138172a0ed78244d8d3ac9d6936cf85))

[BT\_LE\_FEAT\_BIT\_PWR\_CHG\_IND](#a0138172a0ed78244d8d3ac9d6936cf85)

#define BT\_LE\_FEAT\_BIT\_PWR\_CHG\_IND

**Definition** hci\_types.h:195

## [◆ ](#a8ab0d3ca572861bb1c40191766481799)BT\_FEAT\_LE\_PWR\_CTRL\_REQ

| #define BT\_FEAT\_LE\_PWR\_CTRL\_REQ | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_PWR\_CTRL\_REQ](#ae58f5260530d1b94608874f5d03d766d))

[BT\_LE\_FEAT\_BIT\_PWR\_CTRL\_REQ](#ae58f5260530d1b94608874f5d03d766d)

#define BT\_LE\_FEAT\_BIT\_PWR\_CTRL\_REQ

**Definition** hci\_types.h:194

## [◆ ](#adf4303d47abfab3bd23080c545b77ef7)BT\_FEAT\_LE\_RX\_CTE

| #define BT\_FEAT\_LE\_RX\_CTE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_RX\_CTE](#a9d9449f1935d6522291eca581f3fa9b0))

[BT\_LE\_FEAT\_BIT\_RX\_CTE](#a9d9449f1935d6522291eca581f3fa9b0)

#define BT\_LE\_FEAT\_BIT\_RX\_CTE

**Definition** hci\_types.h:184

## [◆ ](#af33c8331e204eeee2a7a02e2ad46c7a2)BT\_FEAT\_LE\_SYNC\_RECEIVER

| #define BT\_FEAT\_LE\_SYNC\_RECEIVER | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](#a6bf20989952fed3726bc45873beb896e)(feat, \

[BT\_LE\_FEAT\_BIT\_SYNC\_RECEIVER](#a2fed771f5611212e48027025e11f7678))

[BT\_LE\_FEAT\_BIT\_SYNC\_RECEIVER](#a2fed771f5611212e48027025e11f7678)

#define BT\_LE\_FEAT\_BIT\_SYNC\_RECEIVER

**Definition** hci\_types.h:192

## [◆ ](#a7622a2fc0a65f82a827ab3cc84e4e7c5)BT\_FEAT\_LMP\_ESCO\_CAPABLE

| #define BT\_FEAT\_LMP\_ESCO\_CAPABLE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 0, 3, 7)

## [◆ ](#a24f24640d9f52adb15336a1b17122346)BT\_FEAT\_LMP\_SCO\_CAPABLE

| #define BT\_FEAT\_LMP\_SCO\_CAPABLE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 0, 1, 3)

## [◆ ](#a9ecf892ec94af8cbfd2e6c99310b1fa2)BT\_FEAT\_SC

| #define BT\_FEAT\_SC | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_FEAT\_TEST](#a41e5b49e645ed511340a61f843f6b238)(feat, 2, 1, 0)

## [◆ ](#a41e5b49e645ed511340a61f843f6b238)BT\_FEAT\_TEST

| #define BT\_FEAT\_TEST | ( |  | *feat*, |
| --- | --- | --- | --- |
|  |  |  | *page*, |
|  |  |  | *octet*, |
|  |  |  | *bit* ) |

**Value:**

(feat[page][octet] & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(bit))

## [◆ ](#afee2289cd70b50f888518fd0b6b3f559)BT\_HCI\_ACL

| #define BT\_HCI\_ACL   0x01 |
| --- |

## [◆ ](#a7418d845532d6b077a9695454fa65bc5)BT\_HCI\_ACL\_HDR\_SIZE

| #define BT\_HCI\_ACL\_HDR\_SIZE   4 |
| --- |

## [◆ ](#a017742ee92c9ed7b80b41f339394f1e4)BT\_HCI\_ADDR\_RES\_DISABLE

| #define BT\_HCI\_ADDR\_RES\_DISABLE   0x00 |
| --- |

## [◆ ](#a61e677658b5a730b13869ebc0dbbffbe)BT\_HCI\_ADDR\_RES\_ENABLE

| #define BT\_HCI\_ADDR\_RES\_ENABLE   0x01 |
| --- |

## [◆ ](#afaecb8d6be1b1c0ce98db7edd8bad343)BT\_HCI\_ADV\_DIRECT\_IND

| #define BT\_HCI\_ADV\_DIRECT\_IND   0x01 |
| --- |

## [◆ ](#a67c1c0c5349b2de661030138185d7b0d)BT\_HCI\_ADV\_DIRECT\_IND\_LOW\_DUTY

| #define BT\_HCI\_ADV\_DIRECT\_IND\_LOW\_DUTY   0x04 |
| --- |

## [◆ ](#aa85640ad3a1aa78cf862a5d8b2567fa1)BT\_HCI\_ADV\_HANDLE\_INVALID

| #define BT\_HCI\_ADV\_HANDLE\_INVALID   0xff |
| --- |

## [◆ ](#a338499e51470b8910e9f663be8f55db5)BT\_HCI\_ADV\_IND

| #define BT\_HCI\_ADV\_IND   0x00 |
| --- |

## [◆ ](#a48e13ce185bf9612455c49484ff80bb9)BT\_HCI\_ADV\_NONCONN\_IND

| #define BT\_HCI\_ADV\_NONCONN\_IND   0x03 |
| --- |

## [◆ ](#ae94df1ac3bc14f42be1207531872104a)BT\_HCI\_ADV\_SCAN\_IND

| #define BT\_HCI\_ADV\_SCAN\_IND   0x02 |
| --- |

## [◆ ](#afb3e678c87b81f9348749f1c5721ce26)BT\_HCI\_ADV\_SCAN\_RSP

| #define BT\_HCI\_ADV\_SCAN\_RSP   0x04 |
| --- |

## [◆ ](#acdf2b6de1459a7492415a8987ad9a896)BT\_HCI\_CMD\_HDR\_SIZE

| #define BT\_HCI\_CMD\_HDR\_SIZE   3 |
| --- |

## [◆ ](#a89eeffc2f46c776ecdb5eea81cb1f47a)BT\_HCI\_CODEC\_TRANSPORT\_MASK\_BREDR\_ACL

| #define BT\_HCI\_CODEC\_TRANSPORT\_MASK\_BREDR\_ACL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#ab50b70f27bd9beb4da6fe8d4b91398c1)BT\_HCI\_CODEC\_TRANSPORT\_MASK\_BREDR\_SCO

| #define BT\_HCI\_CODEC\_TRANSPORT\_MASK\_BREDR\_SCO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a7d90fc1df2260a4067c3eb4ab169c406)BT\_HCI\_CODEC\_TRANSPORT\_MASK\_LE\_BIS

| #define BT\_HCI\_CODEC\_TRANSPORT\_MASK\_LE\_BIS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a38dd1118554de13f3f6f2853900212c5)BT\_HCI\_CODEC\_TRANSPORT\_MASK\_LE\_CIS

| #define BT\_HCI\_CODEC\_TRANSPORT\_MASK\_LE\_CIS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a36f18d10467a580e9864eb8629b8ce01)BT\_HCI\_CODING\_FORMAT\_ALAW\_LOG

| #define BT\_HCI\_CODING\_FORMAT\_ALAW\_LOG   0x01 |
| --- |

## [◆ ](#a80dc369e54038df30f44ca4c13ee14d6)BT\_HCI\_CODING\_FORMAT\_CVSD

| #define BT\_HCI\_CODING\_FORMAT\_CVSD   0x02 |
| --- |

## [◆ ](#a405e22871772b5155f99774178e4093d)BT\_HCI\_CODING\_FORMAT\_G729A

| #define BT\_HCI\_CODING\_FORMAT\_G729A   0x07 |
| --- |

## [◆ ](#a1fa62d6f28ef56ebe9c18d5ab86fbf8e)BT\_HCI\_CODING\_FORMAT\_LC3

| #define BT\_HCI\_CODING\_FORMAT\_LC3   0x06 |
| --- |

## [◆ ](#a2630de3f8cc3ccc3d81f0f2fa4084587)BT\_HCI\_CODING\_FORMAT\_LINEAR\_PCM

| #define BT\_HCI\_CODING\_FORMAT\_LINEAR\_PCM   0x04 |
| --- |

## [◆ ](#a9178f80b7783c9cffb4574667d3033af)BT\_HCI\_CODING\_FORMAT\_MSBC

| #define BT\_HCI\_CODING\_FORMAT\_MSBC   0x05 |
| --- |

## [◆ ](#ad93af498e2265c180a01055eca2a4de0)BT\_HCI\_CODING\_FORMAT\_TRANSPARENT

| #define BT\_HCI\_CODING\_FORMAT\_TRANSPARENT   0x03 |
| --- |

## [◆ ](#a4f4939e7fa43ab73861f64d25b6549d8)BT\_HCI\_CODING\_FORMAT\_ULAW\_LOG

| #define BT\_HCI\_CODING\_FORMAT\_ULAW\_LOG   0x00 |
| --- |

## [◆ ](#a46839c453b81e80fb8e578f89dc31864)BT\_HCI\_CODING\_FORMAT\_VS

| #define BT\_HCI\_CODING\_FORMAT\_VS   0xFF |
| --- |

## [◆ ](#a5e0814f9ca6e7fbc78b0778634ff075d)BT\_HCI\_CTE\_REQ\_STATUS\_RSP\_WITHOUT\_CTE

| #define BT\_HCI\_CTE\_REQ\_STATUS\_RSP\_WITHOUT\_CTE   0x0 |
| --- |

## [◆ ](#a252ef06a33818e117fc7f8146413cbd0)BT\_HCI\_CTL\_TO\_HOST\_FLOW\_DISABLE

| #define BT\_HCI\_CTL\_TO\_HOST\_FLOW\_DISABLE   0x00 |
| --- |

## [◆ ](#a4231ce6514091008191d5843b2c0b452)BT\_HCI\_CTL\_TO\_HOST\_FLOW\_ENABLE

| #define BT\_HCI\_CTL\_TO\_HOST\_FLOW\_ENABLE   0x01 |
| --- |

## [◆ ](#af8d89c712a3d27f9b6f92a31bea2a8c3)BT\_HCI\_DATAPATH\_DIR\_CTLR\_TO\_HOST

| #define BT\_HCI\_DATAPATH\_DIR\_CTLR\_TO\_HOST   0x01 |
| --- |

## [◆ ](#a0f74c19fabbcb3088e1a819d33a05a1c)BT\_HCI\_DATAPATH\_DIR\_HOST\_TO\_CTLR

| #define BT\_HCI\_DATAPATH\_DIR\_HOST\_TO\_CTLR   0x00 |
| --- |

## [◆ ](#a5f748cb264265b9fc12f146ba47fa14c)BT\_HCI\_DATAPATH\_ID\_HCI

| #define BT\_HCI\_DATAPATH\_ID\_HCI   0x00 |
| --- |

## [◆ ](#a0382b1713c7b2a774a8f004b6d1bc33f)BT\_HCI\_DATAPATH\_ID\_VS

| #define BT\_HCI\_DATAPATH\_ID\_VS   0x01 |
| --- |

## [◆ ](#abf755f2839b36a3ac3431bff04193b2f)BT\_HCI\_DATAPATH\_ID\_VS\_END

| #define BT\_HCI\_DATAPATH\_ID\_VS\_END   0xfe |
| --- |

## [◆ ](#aae1149095ff44d1b749e8b4b4d4aa32f)BT\_HCI\_DEDICATED\_BONDING

| #define BT\_HCI\_DEDICATED\_BONDING   0x02 |
| --- |

## [◆ ](#aa1361f09852be86296cf91896d8f0853)BT\_HCI\_DEDICATED\_BONDING\_MITM

| #define BT\_HCI\_DEDICATED\_BONDING\_MITM   0x03 |
| --- |

## [◆ ](#ae4271fbdb039750aceac7c0712d4f3db)BT\_HCI\_ENCRYPTION\_KEY\_SIZE\_MAX

| #define BT\_HCI\_ENCRYPTION\_KEY\_SIZE\_MAX   16 |
| --- |

## [◆ ](#ab4eedd90a583b3893c77f51aee16e3c0)BT\_HCI\_ENCRYPTION\_KEY\_SIZE\_MIN

| #define BT\_HCI\_ENCRYPTION\_KEY\_SIZE\_MIN   7 |
| --- |

## [◆ ](#abfa408d8366ff3cae1cd35fffcda30c0)BT\_HCI\_ERR\_ADV\_TIMEOUT

| #define BT\_HCI\_ERR\_ADV\_TIMEOUT   0x3c |
| --- |

## [◆ ](#a070d51dd0de3288f9811f90a558c889b)BT\_HCI\_ERR\_AUTH\_FAIL

| #define BT\_HCI\_ERR\_AUTH\_FAIL   0x05 |
| --- |

## [◆ ](#a366f85b3bcb3f578b2572149c69b7fc0)BT\_HCI\_ERR\_BD\_ADDR\_UNACCEPTABLE

| #define BT\_HCI\_ERR\_BD\_ADDR\_UNACCEPTABLE   0x0f |
| --- |

## [◆ ](#a3b9fc13a3e3ecc9f0f4431487c0301b5)BT\_HCI\_ERR\_CHAN\_ASSESS\_NOT\_SUPPORTED

| #define BT\_HCI\_ERR\_CHAN\_ASSESS\_NOT\_SUPPORTED   0x2e |
| --- |

## [◆ ](#a6e9a4db5962d79b5a7f43a4c2919c9e9)BT\_HCI\_ERR\_CLOCK\_ADJUST\_REJECTED

| #define BT\_HCI\_ERR\_CLOCK\_ADJUST\_REJECTED   0x40 |
| --- |

## [◆ ](#a5ee9f2e9625d732e84e5ef593bb2a3f9)BT\_HCI\_ERR\_CMD\_DISALLOWED

| #define BT\_HCI\_ERR\_CMD\_DISALLOWED   0x0c |
| --- |

## [◆ ](#ae4682cbd7a9b9dedd25926efe029c0d7)BT\_HCI\_ERR\_CONN\_ACCEPT\_TIMEOUT

| #define BT\_HCI\_ERR\_CONN\_ACCEPT\_TIMEOUT   0x10 |
| --- |

## [◆ ](#abcf4cd921e304758cc969a83445d70ec)BT\_HCI\_ERR\_CONN\_ALREADY\_EXISTS

| #define BT\_HCI\_ERR\_CONN\_ALREADY\_EXISTS   0x0b |
| --- |

## [◆ ](#ac6c44be2e737d7a10b5c886c69d6b1a5)BT\_HCI\_ERR\_CONN\_FAIL\_TO\_ESTAB

| #define BT\_HCI\_ERR\_CONN\_FAIL\_TO\_ESTAB   0x3e |
| --- |

## [◆ ](#a490798f4f1e226e66475f0fb84cfbcd5)BT\_HCI\_ERR\_CONN\_LIMIT\_EXCEEDED

| #define BT\_HCI\_ERR\_CONN\_LIMIT\_EXCEEDED   0x09 |
| --- |

## [◆ ](#a1adf558f8f606612ca96bdbbb55e0e78)BT\_HCI\_ERR\_CONN\_REJECTED\_DUE\_TO\_NO\_CHAN

| #define BT\_HCI\_ERR\_CONN\_REJECTED\_DUE\_TO\_NO\_CHAN   0x39 |
| --- |

## [◆ ](#ab702caf5cd73431cc9aede8891f74610)BT\_HCI\_ERR\_CONN\_TIMEOUT

| #define BT\_HCI\_ERR\_CONN\_TIMEOUT   0x08 |
| --- |

## [◆ ](#a33167856fe838b833fe42d92c3eac4eb)BT\_HCI\_ERR\_CONTROLLER\_BUSY

| #define BT\_HCI\_ERR\_CONTROLLER\_BUSY   0x3a |
| --- |

## [◆ ](#a3b461d65baa95f8f984b212264dc5072)BT\_HCI\_ERR\_DIFF\_TRANS\_COLLISION

| #define BT\_HCI\_ERR\_DIFF\_TRANS\_COLLISION   0x2a |
| --- |

## [◆ ](#aeb5499a707e1c41cbd9db882cfdf0677)BT\_HCI\_ERR\_ENC\_MODE\_NOT\_ACCEPTABLE

| #define BT\_HCI\_ERR\_ENC\_MODE\_NOT\_ACCEPTABLE   0x25 |
| --- |

## [◆ ](#a1b7094ad185ed22542f370ab1101c1ae)BT\_HCI\_ERR\_EXT\_INQ\_RESP\_TOO\_LARGE

| #define BT\_HCI\_ERR\_EXT\_INQ\_RESP\_TOO\_LARGE   0x36 |
| --- |

## [◆ ](#a107d85e39fec3146d6b017deb047571b)BT\_HCI\_ERR\_HOST\_BUSY\_PAIRING

| #define BT\_HCI\_ERR\_HOST\_BUSY\_PAIRING   0x38 |
| --- |

## [◆ ](#a5dfcb0d206b98be7eacdc67547bb8a2c)BT\_HCI\_ERR\_HW\_FAILURE

| #define BT\_HCI\_ERR\_HW\_FAILURE   0x03 |
| --- |

## [◆ ](#a2d336db995ab250f94de66da952c642c)BT\_HCI\_ERR\_INSTANT\_PASSED

| #define BT\_HCI\_ERR\_INSTANT\_PASSED   0x28 |
| --- |

## [◆ ](#a334efee11bd7086e0611c8f628d65abb)BT\_HCI\_ERR\_INSUFF\_SECURITY

| #define BT\_HCI\_ERR\_INSUFF\_SECURITY   0x2f |
| --- |

## [◆ ](#a0efddbffb31b93158b10a3f678f94f4e)BT\_HCI\_ERR\_INSUFFICIENT\_RESOURCES

| #define BT\_HCI\_ERR\_INSUFFICIENT\_RESOURCES   0x0d |
| --- |

## [◆ ](#a08d4bdfc189bccbdb97a51b0089e77a0)BT\_HCI\_ERR\_INSUFFICIENT\_SECURITY

| #define BT\_HCI\_ERR\_INSUFFICIENT\_SECURITY   0x0e |
| --- |

## [◆ ](#a943fe81109d82983018b558b9274f9a3)BT\_HCI\_ERR\_INVALID\_LL\_PARAM

| #define BT\_HCI\_ERR\_INVALID\_LL\_PARAM   0x1e |
| --- |

## [◆ ](#afc76c774f5e71423eb9fea910d1860e9)BT\_HCI\_ERR\_INVALID\_PARAM

| #define BT\_HCI\_ERR\_INVALID\_PARAM   0x12 |
| --- |

## [◆ ](#a86b092455cfd220d48af2bea04900b5b)BT\_HCI\_ERR\_LIMIT\_REACHED

| #define BT\_HCI\_ERR\_LIMIT\_REACHED   0x43 |
| --- |

## [◆ ](#aee97132db4398e2db0a6e115ca20b9b4)BT\_HCI\_ERR\_LINK\_KEY\_CANNOT\_BE\_CHANGED

| #define BT\_HCI\_ERR\_LINK\_KEY\_CANNOT\_BE\_CHANGED   0x26 |
| --- |

## [◆ ](#a0e280074290680d62ad4721384bb603e)BT\_HCI\_ERR\_LL\_PROC\_COLLISION

| #define BT\_HCI\_ERR\_LL\_PROC\_COLLISION   0x23 |
| --- |

## [◆ ](#a6317763780d9c81e6752d5a2c8ce3172)BT\_HCI\_ERR\_LL\_RESP\_TIMEOUT

| #define BT\_HCI\_ERR\_LL\_RESP\_TIMEOUT   0x22 |
| --- |

## [◆ ](#a47c02d44d40d785db6fee28c88d3c5b4)BT\_HCI\_ERR\_LMP\_PDU\_NOT\_ALLOWED

| #define BT\_HCI\_ERR\_LMP\_PDU\_NOT\_ALLOWED   0x24 |
| --- |

## [◆ ](#a0f07b75be216456e9370485dca0da992)BT\_HCI\_ERR\_LOCALHOST\_TERM\_CONN

| #define BT\_HCI\_ERR\_LOCALHOST\_TERM\_CONN   0x16 |
| --- |

## [◆ ](#af0b9f71a874ca2c3587256c7f665e9fa)BT\_HCI\_ERR\_MAC\_CONN\_FAILED

| #define BT\_HCI\_ERR\_MAC\_CONN\_FAILED   0x3f |
| --- |

## [◆ ](#ac54f84b29901185822f6bad2edf86b61)BT\_HCI\_ERR\_MEM\_CAPACITY\_EXCEEDED

| #define BT\_HCI\_ERR\_MEM\_CAPACITY\_EXCEEDED   0x07 |
| --- |

## [◆ ](#a85433a7b3bcac0a507d7f6376a084142)BT\_HCI\_ERR\_OP\_CANCELLED\_BY\_HOST

| #define BT\_HCI\_ERR\_OP\_CANCELLED\_BY\_HOST   0x44 |
| --- |

## [◆ ](#ab63f7d0c79aaa57abf59aa18e112345f)BT\_HCI\_ERR\_PACKET\_TOO\_LONG

| #define BT\_HCI\_ERR\_PACKET\_TOO\_LONG   0x45 |
| --- |

## [◆ ](#a1e89c8eb63dee6bd720ef9354c867519)BT\_HCI\_ERR\_PAGE\_TIMEOUT

| #define BT\_HCI\_ERR\_PAGE\_TIMEOUT   0x04 |
| --- |

## [◆ ](#a60823c337c91aa95348dcae250a83977)BT\_HCI\_ERR\_PAIRING\_NOT\_ALLOWED

| #define BT\_HCI\_ERR\_PAIRING\_NOT\_ALLOWED   0x18 |
| --- |

## [◆ ](#a059c7d5619823eddf2c541b40a6464cb)BT\_HCI\_ERR\_PAIRING\_NOT\_SUPPORTED

| #define BT\_HCI\_ERR\_PAIRING\_NOT\_SUPPORTED   0x29 |
| --- |

## [◆ ](#a29c763a2e70820fae7e2e825d22f4991)BT\_HCI\_ERR\_PARAM\_OUT\_OF\_MANDATORY\_RANGE

| #define BT\_HCI\_ERR\_PARAM\_OUT\_OF\_MANDATORY\_RANGE   0x30 |
| --- |

## [◆ ](#a39f129aefe81c2d06f70552ace008a15)BT\_HCI\_ERR\_PIN\_OR\_KEY\_MISSING

| #define BT\_HCI\_ERR\_PIN\_OR\_KEY\_MISSING   0x06 |
| --- |

## [◆ ](#a88363d1eb1c0d13dc8138af8edc76abc)BT\_HCI\_ERR\_QOS\_REJECTED

| #define BT\_HCI\_ERR\_QOS\_REJECTED   0x2d |
| --- |

## [◆ ](#a37c2fdc6b32b4a2cb70d5c17dfbe262b)BT\_HCI\_ERR\_QOS\_UNACCEPTABLE\_PARAM

| #define BT\_HCI\_ERR\_QOS\_UNACCEPTABLE\_PARAM   0x2c |
| --- |

## [◆ ](#a5eeadfb220c24b2e7f5ce3fd21e5d46a)BT\_HCI\_ERR\_REMOTE\_LOW\_RESOURCES

| #define BT\_HCI\_ERR\_REMOTE\_LOW\_RESOURCES   0x14 |
| --- |

## [◆ ](#a083f1fc52300f7e47c2f8d4e50551851)BT\_HCI\_ERR\_REMOTE\_POWER\_OFF

| #define BT\_HCI\_ERR\_REMOTE\_POWER\_OFF   0x15 |
| --- |

## [◆ ](#ac0e3b44027180d7a2dedb59395c4b111)BT\_HCI\_ERR\_REMOTE\_USER\_TERM\_CONN

| #define BT\_HCI\_ERR\_REMOTE\_USER\_TERM\_CONN   0x13 |
| --- |

## [◆ ](#a11d42e0347cc9d1d50ccd45c2e9a39f6)BT\_HCI\_ERR\_REPEATED\_ATTEMPTS

| #define BT\_HCI\_ERR\_REPEATED\_ATTEMPTS   0x17 |
| --- |

## [◆ ](#a0e02fd84d7a355f42fe006c756936d78)BT\_HCI\_ERR\_REQUESTED\_QOS\_NOT\_SUPPORTED

| #define BT\_HCI\_ERR\_REQUESTED\_QOS\_NOT\_SUPPORTED   0x27 |
| --- |

## [◆ ](#ac6244ca7123879ef039c2c5486d50d41)BT\_HCI\_ERR\_RESERVED\_SLOT\_VIOLATION

| #define BT\_HCI\_ERR\_RESERVED\_SLOT\_VIOLATION   0x34 |
| --- |

## [◆ ](#a070d016f54e7f5f0a7ca6d8c8218505f)BT\_HCI\_ERR\_ROLE\_CHANGE\_NOT\_ALLOWED

| #define BT\_HCI\_ERR\_ROLE\_CHANGE\_NOT\_ALLOWED   0x21 |
| --- |

## [◆ ](#ab40a919a2d87376f2aca6d2ea3f55758)BT\_HCI\_ERR\_ROLE\_SWITCH\_FAILED

| #define BT\_HCI\_ERR\_ROLE\_SWITCH\_FAILED   0x35 |
| --- |

## [◆ ](#ac9c9a68e696e038d7b05af89e3a0c7b6)BT\_HCI\_ERR\_ROLE\_SWITCH\_PENDING

| #define BT\_HCI\_ERR\_ROLE\_SWITCH\_PENDING   0x32 |
| --- |

## [◆ ](#ad8f77a43360e8ab2e6c71a103e14c951)BT\_HCI\_ERR\_SCO\_AIR\_MODE\_REJECTED

| #define BT\_HCI\_ERR\_SCO\_AIR\_MODE\_REJECTED   0x1d |
| --- |

## [◆ ](#a5093c6357fcefd1ccdcbdf9a99f18e7c)BT\_HCI\_ERR\_SCO\_INTERVAL\_REJECTED

| #define BT\_HCI\_ERR\_SCO\_INTERVAL\_REJECTED   0x1c |
| --- |

## [◆ ](#a5e28f04c454361508bc791c6ce292bc2)BT\_HCI\_ERR\_SCO\_OFFSET\_REJECTED

| #define BT\_HCI\_ERR\_SCO\_OFFSET\_REJECTED   0x1b |
| --- |

## [◆ ](#afd8840ad198dfdb666bf24851a478c70)BT\_HCI\_ERR\_SIMPLE\_PAIR\_NOT\_SUPP\_BY\_HOST

| #define BT\_HCI\_ERR\_SIMPLE\_PAIR\_NOT\_SUPP\_BY\_HOST   0x37 |
| --- |

## [◆ ](#a9e7483e2d7f46981e9d1fcdbb8a7515c)BT\_HCI\_ERR\_SUBMAP\_NOT\_DEFINED

| #define BT\_HCI\_ERR\_SUBMAP\_NOT\_DEFINED   0x41 |
| --- |

## [◆ ](#a27c890210eded48f159073cccef8582a)BT\_HCI\_ERR\_SUCCESS

| #define BT\_HCI\_ERR\_SUCCESS   0x00 |
| --- |

HCI Error Codes, BT Core Spec v5.4 [Vol 1, Part F].

## [◆ ](#a56a3d3d9d7798334b29c02214a2e73bf)BT\_HCI\_ERR\_SYNC\_CONN\_LIMIT\_EXCEEDED

| #define BT\_HCI\_ERR\_SYNC\_CONN\_LIMIT\_EXCEEDED   0x0a |
| --- |

## [◆ ](#a71dd49b1b5dc51ad7db8da9aecf9ff06)BT\_HCI\_ERR\_TERM\_DUE\_TO\_MIC\_FAIL

| #define BT\_HCI\_ERR\_TERM\_DUE\_TO\_MIC\_FAIL   0x3d |
| --- |

## [◆ ](#a8dcf345b1fea1364f490f40963992cd6)BT\_HCI\_ERR\_TOO\_EARLY

| #define BT\_HCI\_ERR\_TOO\_EARLY   0x47 |
| --- |

## [◆ ](#a9c62f8f73470a3157a60f8d6d56b22a4)BT\_HCI\_ERR\_TOO\_LATE

| #define BT\_HCI\_ERR\_TOO\_LATE   0x46 |
| --- |

## [◆ ](#a712e214942c0d151597ce04e9d0df453)BT\_HCI\_ERR\_UNACCEPT\_CONN\_PARAM

| #define BT\_HCI\_ERR\_UNACCEPT\_CONN\_PARAM   0x3b |
| --- |

## [◆ ](#a7646bc91f5dbb28c5eeda7e1828f2e30)BT\_HCI\_ERR\_UNKNOWN\_ADV\_IDENTIFIER

| #define BT\_HCI\_ERR\_UNKNOWN\_ADV\_IDENTIFIER   0x42 |
| --- |

## [◆ ](#a376012d3b8f7814870e3f03f6cbabb89)BT\_HCI\_ERR\_UNKNOWN\_CMD

| #define BT\_HCI\_ERR\_UNKNOWN\_CMD   0x01 |
| --- |

## [◆ ](#afd68afeb0296e3af363d7d60eaf4e9a1)BT\_HCI\_ERR\_UNKNOWN\_CONN\_ID

| #define BT\_HCI\_ERR\_UNKNOWN\_CONN\_ID   0x02 |
| --- |

## [◆ ](#a0f81b5c19358982bd33c527239200b08)BT\_HCI\_ERR\_UNKNOWN\_LMP\_PDU

| #define BT\_HCI\_ERR\_UNKNOWN\_LMP\_PDU   0x19 |
| --- |

## [◆ ](#ab3833bbb70b6a2e57870d8243f528b90)BT\_HCI\_ERR\_UNSPECIFIED

| #define BT\_HCI\_ERR\_UNSPECIFIED   0x1f |
| --- |

## [◆ ](#af73db17855859676827bad84e2ccbabe)BT\_HCI\_ERR\_UNSUPP\_FEATURE\_PARAM\_VAL

| #define BT\_HCI\_ERR\_UNSUPP\_FEATURE\_PARAM\_VAL   0x11 |
| --- |

## [◆ ](#af1fa61561b6a91d08f81e9c19cbe89f7)BT\_HCI\_ERR\_UNSUPP\_LL\_PARAM\_VAL

| #define BT\_HCI\_ERR\_UNSUPP\_LL\_PARAM\_VAL   0x20 |
| --- |

## [◆ ](#a516751f02bd497a020783f69bcf71453)BT\_HCI\_ERR\_UNSUPP\_REMOTE\_FEATURE

| #define BT\_HCI\_ERR\_UNSUPP\_REMOTE\_FEATURE   0x1a |
| --- |

## [◆ ](#a4c57b051b336788e503a8521bb5ada80)BT\_HCI\_ESCO

| #define BT\_HCI\_ESCO   0x02 |
| --- |

## [◆ ](#acc9c74c8406b84baaf55d9452924aaf9)BT\_HCI\_EVT\_AUTH\_COMPLETE

| #define BT\_HCI\_EVT\_AUTH\_COMPLETE   0x06 |
| --- |

## [◆ ](#a589975abd5d9532ba16d15ac21c5e81e)BT\_HCI\_EVT\_AUTH\_PAYLOAD\_TIMEOUT\_EXP

| #define BT\_HCI\_EVT\_AUTH\_PAYLOAD\_TIMEOUT\_EXP   0x57 |
| --- |

## [◆ ](#a06f6cf60885ac051cdc9b463fc3b7de7)BT\_HCI\_EVT\_CMD\_COMPLETE

| #define BT\_HCI\_EVT\_CMD\_COMPLETE   0x0e |
| --- |

## [◆ ](#a2b35e7484351228243bb3564273c5bff)BT\_HCI\_EVT\_CMD\_STATUS

| #define BT\_HCI\_EVT\_CMD\_STATUS   0x0f |
| --- |

## [◆ ](#a0dd2162851b4a7afc3d96924f69cceca)BT\_HCI\_EVT\_CONN\_COMPLETE

| #define BT\_HCI\_EVT\_CONN\_COMPLETE   0x03 |
| --- |

## [◆ ](#afc473fec33612ffb044d54bad39e8d76)BT\_HCI\_EVT\_CONN\_REQUEST

| #define BT\_HCI\_EVT\_CONN\_REQUEST   0x04 |
| --- |

## [◆ ](#ae747b016101bc9e9614163288c5c0d15)BT\_HCI\_EVT\_DATA\_BUF\_OVERFLOW

| #define BT\_HCI\_EVT\_DATA\_BUF\_OVERFLOW   0x1a |
| --- |

## [◆ ](#a32e5051a114f8987b49c6957c84d60e2)BT\_HCI\_EVT\_DISCONN\_COMPLETE

| #define BT\_HCI\_EVT\_DISCONN\_COMPLETE   0x05 |
| --- |

## [◆ ](#a8dee2fc366d0371b68b212ff40e6ea7d)BT\_HCI\_EVT\_ENCRYPT\_CHANGE

| #define BT\_HCI\_EVT\_ENCRYPT\_CHANGE   0x08 |
| --- |

## [◆ ](#aad28cc20cc111ac39e39011932b9d22e)BT\_HCI\_EVT\_ENCRYPT\_KEY\_REFRESH\_COMPLETE

| #define BT\_HCI\_EVT\_ENCRYPT\_KEY\_REFRESH\_COMPLETE   0x30 |
| --- |

## [◆ ](#a9b5405de1e07fcefba54b286bd1fdfbe)BT\_HCI\_EVT\_EXTENDED\_INQUIRY\_RESULT

| #define BT\_HCI\_EVT\_EXTENDED\_INQUIRY\_RESULT   0x2f |
| --- |

## [◆ ](#a54c3bdd2687d142f925183a46ffc5f8b)BT\_HCI\_EVT\_HARDWARE\_ERROR

| #define BT\_HCI\_EVT\_HARDWARE\_ERROR   0x10 |
| --- |

## [◆ ](#a0edb7e700cfa557e7fb8ec44f5eea961)BT\_HCI\_EVT\_HDR\_SIZE

| #define BT\_HCI\_EVT\_HDR\_SIZE   2 |
| --- |

## [◆ ](#abd8f15d920c0bdb3c68556b4e873f413)BT\_HCI\_EVT\_INQUIRY\_COMPLETE

| #define BT\_HCI\_EVT\_INQUIRY\_COMPLETE   0x01 |
| --- |

## [◆ ](#a92243c99484922771d5aca8f98945d29)BT\_HCI\_EVT\_INQUIRY\_RESULT\_WITH\_RSSI

| #define BT\_HCI\_EVT\_INQUIRY\_RESULT\_WITH\_RSSI   0x22 |
| --- |

## [◆ ](#a4d69a943660da9c1a6ffedb9b653ce3f)BT\_HCI\_EVT\_IO\_CAPA\_REQ

| #define BT\_HCI\_EVT\_IO\_CAPA\_REQ   0x31 |
| --- |

## [◆ ](#a0f5cae40268568e25142eed9e3e5e639)BT\_HCI\_EVT\_IO\_CAPA\_RESP

| #define BT\_HCI\_EVT\_IO\_CAPA\_RESP   0x32 |
| --- |

## [◆ ](#a398afcbdb732fe76ec01db1393721ab2)BT\_HCI\_EVT\_LE\_ADV\_SET\_TERMINATED

| #define BT\_HCI\_EVT\_LE\_ADV\_SET\_TERMINATED   0x12 |
| --- |

## [◆ ](#a1a93b78bdbb29982d989aea5eae5ec19)BT\_HCI\_EVT\_LE\_ADVERTISING\_REPORT

| #define BT\_HCI\_EVT\_LE\_ADVERTISING\_REPORT   0x02 |
| --- |

## [◆ ](#aade42399ac596746100849328c551259)BT\_HCI\_EVT\_LE\_BIG\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_BIG\_COMPLETE   0x1b |
| --- |

## [◆ ](#a8d021615f0b1b2077bbec1f1482b85ef)BT\_HCI\_EVT\_LE\_BIG\_SYNC\_ESTABLISHED

| #define BT\_HCI\_EVT\_LE\_BIG\_SYNC\_ESTABLISHED   0x1d |
| --- |

## [◆ ](#a9c79430501848b9e75a21020920a8ca8)BT\_HCI\_EVT\_LE\_BIG\_SYNC\_LOST

| #define BT\_HCI\_EVT\_LE\_BIG\_SYNC\_LOST   0x1e |
| --- |

## [◆ ](#ac0a1310793a73afda4c2179749df9985)BT\_HCI\_EVT\_LE\_BIG\_TERMINATE

| #define BT\_HCI\_EVT\_LE\_BIG\_TERMINATE   0x1c |
| --- |

## [◆ ](#a651e36b5529cb7f289721573434154cd)BT\_HCI\_EVT\_LE\_BIGINFO\_ADV\_REPORT

| #define BT\_HCI\_EVT\_LE\_BIGINFO\_ADV\_REPORT   0x22 |
| --- |

## [◆ ](#a4f012a8357e5bb17b5dd04128bd39911)BT\_HCI\_EVT\_LE\_CHAN\_SEL\_ALGO

| #define BT\_HCI\_EVT\_LE\_CHAN\_SEL\_ALGO   0x14 |
| --- |

## [◆ ](#a263d26617702ab43fa8b6717007e1df8)BT\_HCI\_EVT\_LE\_CIS\_ESTABLISHED

| #define BT\_HCI\_EVT\_LE\_CIS\_ESTABLISHED   0x19 |
| --- |

## [◆ ](#ae5a1301a0fea0ab6c205dab22e39c6c9)BT\_HCI\_EVT\_LE\_CIS\_ESTABLISHED\_V2

| #define BT\_HCI\_EVT\_LE\_CIS\_ESTABLISHED\_V2   0x2a |
| --- |

## [◆ ](#aaa4af1dcdb163a57b0473b43e8107fd7)BT\_HCI\_EVT\_LE\_CIS\_REQ

| #define BT\_HCI\_EVT\_LE\_CIS\_REQ   0x1a |
| --- |

## [◆ ](#a2c3c4f81903d1860f21880c7c3cfbaa7)BT\_HCI\_EVT\_LE\_CONN\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_CONN\_COMPLETE   0x01 |
| --- |

## [◆ ](#a77072c10df87395e7e649307b975fb69)BT\_HCI\_EVT\_LE\_CONN\_PARAM\_REQ

| #define BT\_HCI\_EVT\_LE\_CONN\_PARAM\_REQ   0x06 |
| --- |

## [◆ ](#aeef912e71549d4b5a0d8b293074a909c)BT\_HCI\_EVT\_LE\_CONN\_UPDATE\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_CONN\_UPDATE\_COMPLETE   0x03 |
| --- |

## [◆ ](#ace41ae5ec2a8f036aabf83ac94937a8b)BT\_HCI\_EVT\_LE\_CONNECTION\_IQ\_REPORT

| #define BT\_HCI\_EVT\_LE\_CONNECTION\_IQ\_REPORT   0x16 |
| --- |

## [◆ ](#a04c4a4567eaad7c592f2181e47768522)BT\_HCI\_EVT\_LE\_CONNECTIONLESS\_IQ\_REPORT

| #define BT\_HCI\_EVT\_LE\_CONNECTIONLESS\_IQ\_REPORT   0x15 |
| --- |

## [◆ ](#ab0d5abde05c53bc194fe07b8726fb307)BT\_HCI\_EVT\_LE\_CS\_CONFIG\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_CS\_CONFIG\_COMPLETE   0x2F |
| --- |

## [◆ ](#a276cf3951bb5c4ee0b1deeb78a7b5681)BT\_HCI\_EVT\_LE\_CS\_PROCEDURE\_ENABLE\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_CS\_PROCEDURE\_ENABLE\_COMPLETE   0x30 |
| --- |

## [◆ ](#a319b523766bcc778ba6bfb3784ac49b7)BT\_HCI\_EVT\_LE\_CS\_READ\_REMOTE\_FAE\_TABLE\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_CS\_READ\_REMOTE\_FAE\_TABLE\_COMPLETE   0x2D |
| --- |

## [◆ ](#abceb3da0b6d4c858ad35c631acf0516e)BT\_HCI\_EVT\_LE\_CS\_READ\_REMOTE\_SUPPORTED\_CAPABILITIES\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_CS\_READ\_REMOTE\_SUPPORTED\_CAPABILITIES\_COMPLETE   0x2C |
| --- |

## [◆ ](#ae1e6afca81585dda0f08f85adc3c69a3)BT\_HCI\_EVT\_LE\_CS\_SECURITY\_ENABLE\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_CS\_SECURITY\_ENABLE\_COMPLETE   0x2E |
| --- |

## [◆ ](#a56079aad1e8efe328c0bfd4dbad9d953)BT\_HCI\_EVT\_LE\_CS\_SUBEVENT\_RESULT

| #define BT\_HCI\_EVT\_LE\_CS\_SUBEVENT\_RESULT   0x31 |
| --- |

## [◆ ](#aad00fc66b8bbc4f3e474661cb4122e47)BT\_HCI\_EVT\_LE\_CS\_SUBEVENT\_RESULT\_CONTINUE

| #define BT\_HCI\_EVT\_LE\_CS\_SUBEVENT\_RESULT\_CONTINUE   0x32 |
| --- |

## [◆ ](#a7dae3e2125d30c3b344b51aba0df68bf)BT\_HCI\_EVT\_LE\_CS\_TEST\_END\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_CS\_TEST\_END\_COMPLETE   0x33 |
| --- |

## [◆ ](#aacaa203f0c8e23c6ca551df0375410e8)BT\_HCI\_EVT\_LE\_CTE\_REQUEST\_FAILED

| #define BT\_HCI\_EVT\_LE\_CTE\_REQUEST\_FAILED   0x17 |
| --- |

## [◆ ](#a064cf9e32616c6f94041d138a5bf4819)BT\_HCI\_EVT\_LE\_DATA\_LEN\_CHANGE

| #define BT\_HCI\_EVT\_LE\_DATA\_LEN\_CHANGE   0x07 |
| --- |

## [◆ ](#a417144400fd8d7f5c05e050950c75dab)BT\_HCI\_EVT\_LE\_DIRECT\_ADV\_REPORT

| #define BT\_HCI\_EVT\_LE\_DIRECT\_ADV\_REPORT   0x0b |
| --- |

## [◆ ](#a292de9ec009a80e23308ead618656b4f)BT\_HCI\_EVT\_LE\_ENH\_CONN\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_ENH\_CONN\_COMPLETE   0x0a |
| --- |

## [◆ ](#a60ea5e58028aa09c00d20cfff5c942d5)BT\_HCI\_EVT\_LE\_ENH\_CONN\_COMPLETE\_V2

| #define BT\_HCI\_EVT\_LE\_ENH\_CONN\_COMPLETE\_V2   0x29 |
| --- |

## [◆ ](#ad63fc0c42f0253dfe06b81324a05f505)BT\_HCI\_EVT\_LE\_EXT\_ADVERTISING\_REPORT

| #define BT\_HCI\_EVT\_LE\_EXT\_ADVERTISING\_REPORT   0x0d |
| --- |

## [◆ ](#a8ab77f497135e365fb9e895dc2d4d453)BT\_HCI\_EVT\_LE\_GENERATE\_DHKEY\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_GENERATE\_DHKEY\_COMPLETE   0x09 |
| --- |

## [◆ ](#a9efb73da285829cde0e4c1ac28a48f1a)BT\_HCI\_EVT\_LE\_LTK\_REQUEST

| #define BT\_HCI\_EVT\_LE\_LTK\_REQUEST   0x05 |
| --- |

## [◆ ](#ac1d7f9270323d7fa459e60b372cf998b)BT\_HCI\_EVT\_LE\_META\_EVENT

| #define BT\_HCI\_EVT\_LE\_META\_EVENT   0x3e |
| --- |

## [◆ ](#abe39909eb984dd6edd1220f9c6744546)BT\_HCI\_EVT\_LE\_P256\_PUBLIC\_KEY\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_P256\_PUBLIC\_KEY\_COMPLETE   0x08 |
| --- |

## [◆ ](#ad61867c0bef6797f7a3b5418c5a4ed5f)BT\_HCI\_EVT\_LE\_PAST\_RECEIVED

| #define BT\_HCI\_EVT\_LE\_PAST\_RECEIVED   0x18 |
| --- |

## [◆ ](#a5379a2a0016a2551ac79736924c7ea86)BT\_HCI\_EVT\_LE\_PAST\_RECEIVED\_V2

| #define BT\_HCI\_EVT\_LE\_PAST\_RECEIVED\_V2   0x26 |
| --- |

## [◆ ](#a3e646ec9a2e0baca5126e58368c97995)BT\_HCI\_EVT\_LE\_PATH\_LOSS\_THRESHOLD

| #define BT\_HCI\_EVT\_LE\_PATH\_LOSS\_THRESHOLD   0x20 |
| --- |

## [◆ ](#a64e0f465068e72e98904fa6cdc33d3de)BT\_HCI\_EVT\_LE\_PER\_ADV\_RESPONSE\_REPORT

| #define BT\_HCI\_EVT\_LE\_PER\_ADV\_RESPONSE\_REPORT   0x28 |
| --- |

## [◆ ](#a4395b8b850e9fd3735c2369798f9c226)BT\_HCI\_EVT\_LE\_PER\_ADV\_SUBEVENT\_DATA\_REQUEST

| #define BT\_HCI\_EVT\_LE\_PER\_ADV\_SUBEVENT\_DATA\_REQUEST   0x27 |
| --- |

## [◆ ](#a8c721c9e5df496900f661755aff7cbd6)BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_ESTABLISHED

| #define BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_ESTABLISHED   0x0e |
| --- |

## [◆ ](#a0decb07f1b4ae20b23cffc616dd442e4)BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_ESTABLISHED\_V2

| #define BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_ESTABLISHED\_V2   0x24 |
| --- |

## [◆ ](#ab303042eabbeb133e202bdcfbd38666c)BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_LOST

| #define BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_LOST   0x10 |
| --- |

## [◆ ](#a31fc096530a89e63d4967d7ddd85b753)BT\_HCI\_EVT\_LE\_PER\_ADVERTISING\_REPORT

| #define BT\_HCI\_EVT\_LE\_PER\_ADVERTISING\_REPORT   0x0f |
| --- |

## [◆ ](#a8d067bf751953fd8a7bb5421bdc94970)BT\_HCI\_EVT\_LE\_PER\_ADVERTISING\_REPORT\_V2

| #define BT\_HCI\_EVT\_LE\_PER\_ADVERTISING\_REPORT\_V2   0x25 |
| --- |

## [◆ ](#a44f18d799280d47ec09376e7cffd4c40)BT\_HCI\_EVT\_LE\_PHY\_UPDATE\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_PHY\_UPDATE\_COMPLETE   0x0c |
| --- |

## [◆ ](#a8b1653caabce8474fba132343aa62f56)BT\_HCI\_EVT\_LE\_REMOTE\_FEAT\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_REMOTE\_FEAT\_COMPLETE   0x04 |
| --- |

## [◆ ](#aeb33301a950a9520d7ff706dddb07951)BT\_HCI\_EVT\_LE\_REQ\_PEER\_SCA\_COMPLETE

| #define BT\_HCI\_EVT\_LE\_REQ\_PEER\_SCA\_COMPLETE   0x1f |
| --- |

## [◆ ](#a0ebf19a602a02c00793b3de64392e514)BT\_HCI\_EVT\_LE\_SCAN\_REQ\_RECEIVED

| #define BT\_HCI\_EVT\_LE\_SCAN\_REQ\_RECEIVED   0x13 |
| --- |

## [◆ ](#a7234c851946c6025aa850c9bf28faab0)BT\_HCI\_EVT\_LE\_SCAN\_TIMEOUT

| #define BT\_HCI\_EVT\_LE\_SCAN\_TIMEOUT   0x11 |
| --- |

## [◆ ](#a2098d628b6ad185cb29106ef69c3627d)BT\_HCI\_EVT\_LE\_SUBRATE\_CHANGE

| #define BT\_HCI\_EVT\_LE\_SUBRATE\_CHANGE   0x23 |
| --- |

## [◆ ](#a835280c0bf13ddebf451fef5f08c22d0)BT\_HCI\_EVT\_LE\_TRANSMIT\_POWER\_REPORT

| #define BT\_HCI\_EVT\_LE\_TRANSMIT\_POWER\_REPORT   0x21 |
| --- |

## [◆ ](#a15578dd8e9d2b16a28ea0b020ac9112b)BT\_HCI\_EVT\_LINK\_KEY\_NOTIFY

| #define BT\_HCI\_EVT\_LINK\_KEY\_NOTIFY   0x18 |
| --- |

## [◆ ](#aab60607637f0e1f8e3cbf9f7292ddc57)BT\_HCI\_EVT\_LINK\_KEY\_REQ

| #define BT\_HCI\_EVT\_LINK\_KEY\_REQ   0x17 |
| --- |

## [◆ ](#a883433c60959629a013d34cea21ab88f)BT\_HCI\_EVT\_NUM\_COMPLETED\_PACKETS

| #define BT\_HCI\_EVT\_NUM\_COMPLETED\_PACKETS   0x13 |
| --- |

## [◆ ](#a8c16e0bdecf9eae58bbd884fb48b0fc2)BT\_HCI\_EVT\_PIN\_CODE\_REQ

| #define BT\_HCI\_EVT\_PIN\_CODE\_REQ   0x16 |
| --- |

## [◆ ](#a092a782ea069c98475a6617241321122)BT\_HCI\_EVT\_REMOTE\_EXT\_FEATURES

| #define BT\_HCI\_EVT\_REMOTE\_EXT\_FEATURES   0x23 |
| --- |

## [◆ ](#acbad340a978d4fc118af826d2c1a81e3)BT\_HCI\_EVT\_REMOTE\_FEATURES

| #define BT\_HCI\_EVT\_REMOTE\_FEATURES   0x0b |
| --- |

## [◆ ](#a1a4be9cf628063db2fb821f67c54ea56)BT\_HCI\_EVT\_REMOTE\_NAME\_REQ\_COMPLETE

| #define BT\_HCI\_EVT\_REMOTE\_NAME\_REQ\_COMPLETE   0x07 |
| --- |

## [◆ ](#a18f58c80d213d666ee8309cda8eb0a26)BT\_HCI\_EVT\_REMOTE\_VERSION\_INFO

| #define BT\_HCI\_EVT\_REMOTE\_VERSION\_INFO   0x0c |
| --- |

## [◆ ](#a9508e6faf71a345f7ff3d2cec9d85dde)BT\_HCI\_EVT\_ROLE\_CHANGE

| #define BT\_HCI\_EVT\_ROLE\_CHANGE   0x12 |
| --- |

## [◆ ](#a7d2ba655c6954f90de04cafafccd727f)BT\_HCI\_EVT\_SSP\_COMPLETE

| #define BT\_HCI\_EVT\_SSP\_COMPLETE   0x36 |
| --- |

## [◆ ](#ab77f3074a2236afc1ed773775d17befe)BT\_HCI\_EVT\_SYNC\_CONN\_COMPLETE

| #define BT\_HCI\_EVT\_SYNC\_CONN\_COMPLETE   0x2c |
| --- |

## [◆ ](#a0f44f6e5037d650b9dd0c5f34ba681b5)BT\_HCI\_EVT\_UNKNOWN

| #define BT\_HCI\_EVT\_UNKNOWN   0x00 |
| --- |

## [◆ ](#a78cdb5848d8a12a8cbea17767b3d02aa)BT\_HCI\_EVT\_USER\_CONFIRM\_REQ

| #define BT\_HCI\_EVT\_USER\_CONFIRM\_REQ   0x33 |
| --- |

## [◆ ](#a724d43899b16fcb89c235898a21c13b9)BT\_HCI\_EVT\_USER\_PASSKEY\_NOTIFY

| #define BT\_HCI\_EVT\_USER\_PASSKEY\_NOTIFY   0x3b |
| --- |

## [◆ ](#a38a1bce81af39bb28d40e149f9309b69)BT\_HCI\_EVT\_USER\_PASSKEY\_REQ

| #define BT\_HCI\_EVT\_USER\_PASSKEY\_REQ   0x34 |
| --- |

## [◆ ](#a955fe06f3fcab82c3370cb621f0dbca0)BT\_HCI\_EVT\_VENDOR

| #define BT\_HCI\_EVT\_VENDOR   0xff |
| --- |

## [◆ ](#ad777455cbcdfe02dd297dee5510e63b4)BT\_HCI\_GENERAL\_BONDING

| #define BT\_HCI\_GENERAL\_BONDING   0x04 |
| --- |

## [◆ ](#a5b30ffdf3753d0a2a6c8ab025d32acef)BT\_HCI\_GENERAL\_BONDING\_MITM

| #define BT\_HCI\_GENERAL\_BONDING\_MITM   0x05 |
| --- |

## [◆ ](#a17386452bbd60c85959296b6539232bd)BT\_HCI\_H4\_ACL

| #define BT\_HCI\_H4\_ACL   0x02 /\* HCI ACL Data packet \*/ |
| --- |

## [◆ ](#a524788ee4d21fe9a4625c35e1756bfe9)BT\_HCI\_H4\_CMD

| #define BT\_HCI\_H4\_CMD   0x01 /\* HCI Command packet \*/ |
| --- |

## [◆ ](#a783053bc2846063e50755f1590e81ba8)BT\_HCI\_H4\_EVT

| #define BT\_HCI\_H4\_EVT   0x04 /\* HCI Event packet \*/ |
| --- |

## [◆ ](#af5e6a53cc7d9619f4ac2ea5bd3256149)BT\_HCI\_H4\_ISO

| #define BT\_HCI\_H4\_ISO   0x05 /\* HCI ISO Data packet \*/ |
| --- |

## [◆ ](#a2a578399cd3a1ed875ba2c8a49b8129b)BT\_HCI\_H4\_NONE

| #define BT\_HCI\_H4\_NONE   0x00 /\* None of the known packet types \*/ |
| --- |

## [◆ ](#a9e1c93f187ed5864cebefccea1b3faa2)BT\_HCI\_H4\_SCO

| #define BT\_HCI\_H4\_SCO   0x03 /\* HCI Synchronous Data packet \*/ |
| --- |

## [◆ ](#a18b5fef3eb5b947ce328e17c1e7db02d)BT\_HCI\_ISO\_CIG\_ID\_MAX

| #define BT\_HCI\_ISO\_CIG\_ID\_MAX   0xFE |
| --- |

## [◆ ](#a26c78a4b760b97682269e66dfe6f99df)BT\_HCI\_ISO\_CIS\_COUNT\_MAX

| #define BT\_HCI\_ISO\_CIS\_COUNT\_MAX   0x1F |
| --- |

## [◆ ](#a11e614cc72adb58bda2a2bdd5f4b36ef)BT\_HCI\_ISO\_CIS\_ID\_VALID\_MAX

| #define BT\_HCI\_ISO\_CIS\_ID\_VALID\_MAX   0xEF |
| --- |

## [◆ ](#aaf4b4fc224c8b5cfdca663250eb29350)BT\_HCI\_ISO\_FRAMING\_VALID\_MASK

| #define BT\_HCI\_ISO\_FRAMING\_VALID\_MASK   0x01 |
| --- |

## [◆ ](#a75c1f5e8a44b034004ecfebdb75ee4be)BT\_HCI\_ISO\_HDR\_SIZE

| #define BT\_HCI\_ISO\_HDR\_SIZE   4 |
| --- |

## [◆ ](#aaadbec2cc6adc2bb14d7117396023d06)BT\_HCI\_ISO\_INTERVAL\_MAX

| #define BT\_HCI\_ISO\_INTERVAL\_MAX   0x0C80 |
| --- |

## [◆ ](#a9d5e85ae1380fa85bae9d7e5e67aa0ae)BT\_HCI\_ISO\_INTERVAL\_MIN

| #define BT\_HCI\_ISO\_INTERVAL\_MIN   0x0004 |
| --- |

## [◆ ](#a9f3e990cadf1be179fcbac3f8ef74efe)BT\_HCI\_ISO\_MAX\_SDU\_VALID\_MASK

| #define BT\_HCI\_ISO\_MAX\_SDU\_VALID\_MASK   0x0FFF |
| --- |

## [◆ ](#a9794f59f8d28879753b39bd504cf55be)BT\_HCI\_ISO\_MAX\_TRANSPORT\_LATENCY\_MAX

| #define BT\_HCI\_ISO\_MAX\_TRANSPORT\_LATENCY\_MAX   0x0FA0 |
| --- |

## [◆ ](#a8d044df1bfab8381b7e334597b303588)BT\_HCI\_ISO\_MAX\_TRANSPORT\_LATENCY\_MIN

| #define BT\_HCI\_ISO\_MAX\_TRANSPORT\_LATENCY\_MIN   0x0005 |
| --- |

## [◆ ](#aecaa88e04025e575c9bcda093f027400)BT\_HCI\_ISO\_PACKING\_VALID\_MASK

| #define BT\_HCI\_ISO\_PACKING\_VALID\_MASK   0x01 |
| --- |

## [◆ ](#ae055ed9714ca23bebd48bb399af04d83)BT\_HCI\_ISO\_PHY\_VALID\_MASK

| #define BT\_HCI\_ISO\_PHY\_VALID\_MASK   0x07 |
| --- |

## [◆ ](#a94b93cd856353f24afee5e4022cdbdb9)BT\_HCI\_ISO\_SDU\_HDR\_SIZE

| #define BT\_HCI\_ISO\_SDU\_HDR\_SIZE   4 |
| --- |

## [◆ ](#aa75800427e808756fc7c6d30da57de37)BT\_HCI\_ISO\_SDU\_INTERVAL\_MAX

| #define BT\_HCI\_ISO\_SDU\_INTERVAL\_MAX   0x0FFFFF |
| --- |

## [◆ ](#a12e9af0e72013649da8afc7aa70a4e9c)BT\_HCI\_ISO\_SDU\_INTERVAL\_MIN

| #define BT\_HCI\_ISO\_SDU\_INTERVAL\_MIN   0x0000FF |
| --- |

## [◆ ](#a22db454317bc89afe092ab9127888441)BT\_HCI\_ISO\_SDU\_TS\_HDR\_SIZE

| #define BT\_HCI\_ISO\_SDU\_TS\_HDR\_SIZE   8 |
| --- |

## [◆ ](#af5c0bf9fd20df7b4a4cdb7ce18fdc7fc)BT\_HCI\_ISO\_TEST\_MAX\_SIZE\_SDU

| #define BT\_HCI\_ISO\_TEST\_MAX\_SIZE\_SDU   2 |
| --- |

## [◆ ](#aed9e2581c74218e023100d63201721af)BT\_HCI\_ISO\_TEST\_VARIABLE\_SIZE\_SDU

| #define BT\_HCI\_ISO\_TEST\_VARIABLE\_SIZE\_SDU   1 |
| --- |

## [◆ ](#aa857bdd2e81c923ab540761986074557)BT\_HCI\_ISO\_TEST\_ZERO\_SIZE\_SDU

| #define BT\_HCI\_ISO\_TEST\_ZERO\_SIZE\_SDU   0 |
| --- |

## [◆ ](#a49f62e83dd51d17efd77c89337fdd537)BT\_HCI\_ISO\_WORST\_CASE\_SCA\_VALID\_MASK

| #define BT\_HCI\_ISO\_WORST\_CASE\_SCA\_VALID\_MASK   0x07 |
| --- |

## [◆ ](#a04a69a823bac190d0ac16f3c21481bde)BT\_HCI\_LE\_1US\_AOA\_RX

| #define BT\_HCI\_LE\_1US\_AOA\_RX   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a70edcf0bd7e63454996ef5d925e91bbf)BT\_HCI\_LE\_1US\_AOD\_RX

| #define BT\_HCI\_LE\_1US\_AOD\_RX   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a41aac54cd90cfc58990ce93124ce7077)BT\_HCI\_LE\_1US\_AOD\_TX

| #define BT\_HCI\_LE\_1US\_AOD\_TX   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#ae8361a3ca39019757304034c32391b47)BT\_HCI\_LE\_ADV\_DISABLE

| #define BT\_HCI\_LE\_ADV\_DISABLE   0x00 |
| --- |

## [◆ ](#a6b8140956fbf85bd5aab2f1974b673f9)BT\_HCI\_LE\_ADV\_ENABLE

| #define BT\_HCI\_LE\_ADV\_ENABLE   0x01 |
| --- |

## [◆ ](#a4e3752dfde6a1f6ce6c7561b6c19657c)BT\_HCI\_LE\_ADV\_EVT\_PHY\_1M

| #define BT\_HCI\_LE\_ADV\_EVT\_PHY\_1M   0x01 |
| --- |

## [◆ ](#a0eae639d3066358da815743aa7ba2933)BT\_HCI\_LE\_ADV\_EVT\_PHY\_2M

| #define BT\_HCI\_LE\_ADV\_EVT\_PHY\_2M   0x02 |
| --- |

## [◆ ](#a865ad7eefd0051e7965bd5e391bf852c)BT\_HCI\_LE\_ADV\_EVT\_PHY\_CODED\_S2

| #define BT\_HCI\_LE\_ADV\_EVT\_PHY\_CODED\_S2   0x04 |
| --- |

## [◆ ](#a51fd268794a726f7d9fa2fb4ce937507)BT\_HCI\_LE\_ADV\_EVT\_PHY\_CODED\_S8

| #define BT\_HCI\_LE\_ADV\_EVT\_PHY\_CODED\_S8   0x03 |
| --- |

## [◆ ](#ae448216e385d4e1175b92e112c941140)BT\_HCI\_LE\_ADV\_EVT\_TYPE\_CONN

| #define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_CONN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a9557bf3ea41a526fb9d628d2fd3d5bea)BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS

| #define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS | ( |  | *ev\_type* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((ev\_type) >> 5) & 0x03)

## [◆ ](#a85720f3d88c7fa5da9dc9cdffb94ec87)BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_COMPLETE

| #define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_COMPLETE   0 |
| --- |

## [◆ ](#abf119f5606440c075e61abcbfaa683c6)BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_INCOMPLETE

| #define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_INCOMPLETE   2 |
| --- |

## [◆ ](#ab7842a3081c9bf5288275b57337955f2)BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_PARTIAL

| #define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_PARTIAL   1 |
| --- |

## [◆ ](#ad9bcda2a43eed7e73112f2ef84cc6183)BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_RX\_FAILED

| #define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_RX\_FAILED   0xFF |
| --- |

## [◆ ](#a1b5738583447011ee63350787236b3b8)BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DIRECT

| #define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DIRECT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a0879fbea8bf3acbe56e25f3693c81ad6)BT\_HCI\_LE\_ADV\_EVT\_TYPE\_LEGACY

| #define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_LEGACY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a54673fbd23e05fec88e1f6bca6aa70e9)BT\_HCI\_LE\_ADV\_EVT\_TYPE\_SCAN

| #define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_SCAN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a485843f24c09934b1f15d5274b4a56d5)BT\_HCI\_LE\_ADV\_EVT\_TYPE\_SCAN\_RSP

| #define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_SCAN\_RSP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a12d97417fa11a07b0af5370b595e9a17)BT\_HCI\_LE\_ADV\_HANDLE\_MAX

| #define BT\_HCI\_LE\_ADV\_HANDLE\_MAX   0xEF |
| --- |

## [◆ ](#a2ba70856f1e7fe8c6e7990ac9cdf5aaa)BT\_HCI\_LE\_ADV\_PHY\_OPTION\_NO\_REQUIRED

| #define BT\_HCI\_LE\_ADV\_PHY\_OPTION\_NO\_REQUIRED   0x00 |
| --- |

## [◆ ](#ac707220fea6b3fc077b8b85267ed0030)BT\_HCI\_LE\_ADV\_PHY\_OPTION\_REQUIRE\_S2

| #define BT\_HCI\_LE\_ADV\_PHY\_OPTION\_REQUIRE\_S2   0x03 |
| --- |

## [◆ ](#aab845a49577d93974b468187c948beff)BT\_HCI\_LE\_ADV\_PHY\_OPTION\_REQUIRE\_S8

| #define BT\_HCI\_LE\_ADV\_PHY\_OPTION\_REQUIRE\_S8   0x04 |
| --- |

## [◆ ](#a21c60f21a4de9136accc32b0a8a0325c)BT\_HCI\_LE\_ADV\_PROP\_ANON

| #define BT\_HCI\_LE\_ADV\_PROP\_ANON   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#ac9597c1c284e23578352a23bd66c9fad)BT\_HCI\_LE\_ADV\_PROP\_CONN

| #define BT\_HCI\_LE\_ADV\_PROP\_CONN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#acd154c93af2dc866cfe8bcf8e370dd3d)BT\_HCI\_LE\_ADV\_PROP\_DIRECT

| #define BT\_HCI\_LE\_ADV\_PROP\_DIRECT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a0fb43dd85c3671420029027cbfbf8c11)BT\_HCI\_LE\_ADV\_PROP\_HI\_DC\_CONN

| #define BT\_HCI\_LE\_ADV\_PROP\_HI\_DC\_CONN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a936310de47af573e0d1d5d9401097ba1)BT\_HCI\_LE\_ADV\_PROP\_LEGACY

| #define BT\_HCI\_LE\_ADV\_PROP\_LEGACY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#ab886c4c7f33adf396ca3e09d0f38995d)BT\_HCI\_LE\_ADV\_PROP\_SCAN

| #define BT\_HCI\_LE\_ADV\_PROP\_SCAN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#abd14685442f2fe315a095516464fc92d)BT\_HCI\_LE\_ADV\_PROP\_TX\_POWER

| #define BT\_HCI\_LE\_ADV\_PROP\_TX\_POWER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#aa1f4b7ba3b48ea6bd7b8a34a7b831a25)BT\_HCI\_LE\_ADV\_SCAN\_REQ\_DISABLE

| #define BT\_HCI\_LE\_ADV\_SCAN\_REQ\_DISABLE   0 |
| --- |

## [◆ ](#a39fa8033dcf14aa43dfad7cabc1cb429)BT\_HCI\_LE\_ADV\_SCAN\_REQ\_ENABLE

| #define BT\_HCI\_LE\_ADV\_SCAN\_REQ\_ENABLE   1 |
| --- |

## [◆ ](#a7f4fcc517033a4743ded39503b35ce29)BT\_HCI\_LE\_ADV\_TX\_POWER\_NO\_PREF

| #define BT\_HCI\_LE\_ADV\_TX\_POWER\_NO\_PREF   0x7F |
| --- |

## [◆ ](#a1410330e31701a140eb8c0c73c943972)BT\_HCI\_LE\_ANTENNA\_SWITCHING\_SLOT\_1US

| #define BT\_HCI\_LE\_ANTENNA\_SWITCHING\_SLOT\_1US   0x1 |
| --- |

## [◆ ](#afa70fe0b1b9e277bfcb6bf7d6fc03564)BT\_HCI\_LE\_ANTENNA\_SWITCHING\_SLOT\_2US

| #define BT\_HCI\_LE\_ANTENNA\_SWITCHING\_SLOT\_2US   0x2 |
| --- |

## [◆ ](#a9b3306f29525c50cd8bd501f7391e518)BT\_HCI\_LE\_AOA\_CTE

| #define BT\_HCI\_LE\_AOA\_CTE   0x0 |
| --- |

## [◆ ](#ac80b68b1ca4f55a8a44b6bf0dfa7bfb3)BT\_HCI\_LE\_AOA\_CTE\_RSP

| #define BT\_HCI\_LE\_AOA\_CTE\_RSP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a8569e960c44660eb41cdccbe5aeb6ead)BT\_HCI\_LE\_AOD\_CTE\_1US

| #define BT\_HCI\_LE\_AOD\_CTE\_1US   0x1 |
| --- |

## [◆ ](#a970732caa95f5742fc18c91efbc7095b)BT\_HCI\_LE\_AOD\_CTE\_2US

| #define BT\_HCI\_LE\_AOD\_CTE\_2US   0x2 |
| --- |

## [◆ ](#a124137512b0f87a67fff694359d629d0)BT\_HCI\_LE\_AOD\_CTE\_RSP\_1US

| #define BT\_HCI\_LE\_AOD\_CTE\_RSP\_1US   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a5c1dd462d05e4a5615f80402f892ecbc)BT\_HCI\_LE\_AOD\_CTE\_RSP\_2US

| #define BT\_HCI\_LE\_AOD\_CTE\_RSP\_2US   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#ac8dcea08127aa5ce2a870d64fcc843f1)BT\_HCI\_LE\_CHAN\_SEL\_ALGO\_1

| #define BT\_HCI\_LE\_CHAN\_SEL\_ALGO\_1   0x00 |
| --- |

## [◆ ](#a7a4b52643c764233427314732896d353)BT\_HCI\_LE\_CHAN\_SEL\_ALGO\_2

| #define BT\_HCI\_LE\_CHAN\_SEL\_ALGO\_2   0x01 |
| --- |

## [◆ ](#aa2b9a667e0b80a4cf4d8cef9cb022ad4)BT\_HCI\_LE\_CONTINUATION\_NUM\_MAX

| #define BT\_HCI\_LE\_CONTINUATION\_NUM\_MAX   0x01f3 |
| --- |

## [◆ ](#ac04c2c0020d2972d6df169f39c421c08)BT\_HCI\_LE\_CREATE\_CONN\_FP\_FILTER

| #define BT\_HCI\_LE\_CREATE\_CONN\_FP\_FILTER   0x01 |
| --- |

## [◆ ](#ae1bd495a90fd902614014e7e1e2f1239)BT\_HCI\_LE\_CREATE\_CONN\_FP\_NO\_FILTER

| #define BT\_HCI\_LE\_CREATE\_CONN\_FP\_NO\_FILTER   0x00 |
| --- |

## [◆ ](#aa437d198f03b30ddbac6ada679e5e0c6)BT\_HCI\_LE\_CS\_CONFIG\_ACTION\_CREATED

| #define BT\_HCI\_LE\_CS\_CONFIG\_ACTION\_CREATED   0x01 |
| --- |

## [◆ ](#a9c815ae28e424256fc440b426ba69892)BT\_HCI\_LE\_CS\_CONFIG\_ACTION\_REMOVED

| #define BT\_HCI\_LE\_CS\_CONFIG\_ACTION\_REMOVED   0x00 |
| --- |

## [◆ ](#af457a20ddc90001f8a523a0e3df6a4bd)BT\_HCI\_LE\_CS\_INITIATOR\_ROLE\_MASK

| #define BT\_HCI\_LE\_CS\_INITIATOR\_ROLE\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a62ab6fbe9acb92c4023f35ae8bb7b14b)BT\_HCI\_LE\_CS\_MODES\_SUPPORTED\_MODE\_3\_MASK

| #define BT\_HCI\_LE\_CS\_MODES\_SUPPORTED\_MODE\_3\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a6b64cb407c353d7a143b7483cf16507f)BT\_HCI\_LE\_CS\_NADM\_RANDOM\_CAPABILITY\_PHASE\_BASED\_MASK

| #define BT\_HCI\_LE\_CS\_NADM\_RANDOM\_CAPABILITY\_PHASE\_BASED\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a903505932b23ae60c59fc4f439f8f3ce)BT\_HCI\_LE\_CS\_NADM\_SOUNDING\_CAPABILITY\_PHASE\_BASED\_MASK

| #define BT\_HCI\_LE\_CS\_NADM\_SOUNDING\_CAPABILITY\_PHASE\_BASED\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a014d9a06d3c571ce06c94a2ebfdbe4e5)BT\_HCI\_LE\_CS\_NOT\_TONE\_EXT\_SLOT

| #define BT\_HCI\_LE\_CS\_NOT\_TONE\_EXT\_SLOT   0x0 |
| --- |

## [◆ ](#abfedf14c97b27f6cdbbb66f2598734e9)BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_EXT\_LIKELY

| #define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_EXT\_LIKELY   0x06 |
| --- |

## [◆ ](#a54895cd6caacff2dc5aee25e301144a7)BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_EXT\_UNLIKELY

| #define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_EXT\_UNLIKELY   0x00 |
| --- |

## [◆ ](#a93f1786e8177c89eb9db36a72e367122)BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_LIKELY

| #define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_LIKELY   0x04 |
| --- |

## [◆ ](#a73bf7224e934c28a73d5e54a632e0e69)BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_POSSIBLE

| #define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_POSSIBLE   0x03 |
| --- |

## [◆ ](#acf2d6f7fd7873e12389a2d470241340f)BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_UNLIKELY

| #define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_UNLIKELY   0x02 |
| --- |

## [◆ ](#a0b10dcb24c429d594b17eec494954d74)BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_VERY\_LIKELY

| #define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_VERY\_LIKELY   0x05 |
| --- |

## [◆ ](#af10362bcbd6b95f8404654d258acdbcb)BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_VERY\_UNLIKELY

| #define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_VERY\_UNLIKELY   0x01 |
| --- |

## [◆ ](#a5f7d8e81a83a3b94e18a39b507232823)BT\_HCI\_LE\_CS\_PACKET\_NADM\_UNKNOWN

| #define BT\_HCI\_LE\_CS\_PACKET\_NADM\_UNKNOWN   0xFF |
| --- |

## [◆ ](#af357550f37226be5b2b6491ebad3fd57)BT\_HCI\_LE\_CS\_PACKET\_QUALITY\_AA\_CHECK\_AA\_NOT\_FOUND

| #define BT\_HCI\_LE\_CS\_PACKET\_QUALITY\_AA\_CHECK\_AA\_NOT\_FOUND   0x2 |
| --- |

## [◆ ](#a7c0e4053873d629e10567937adc033d3)BT\_HCI\_LE\_CS\_PACKET\_QUALITY\_AA\_CHECK\_BIT\_ERRORS\_FOUND

| #define BT\_HCI\_LE\_CS\_PACKET\_QUALITY\_AA\_CHECK\_BIT\_ERRORS\_FOUND   0x1 |
| --- |

## [◆ ](#ab05d15713fb0145b32a5977774b50533)BT\_HCI\_LE\_CS\_PACKET\_QUALITY\_AA\_CHECK\_SUCCESSFUL

| #define BT\_HCI\_LE\_CS\_PACKET\_QUALITY\_AA\_CHECK\_SUCCESSFUL   0x0 |
| --- |

## [◆ ](#a8ce6b3556a9f5b83648b80d90652f00d)BT\_HCI\_LE\_CS\_PACKET\_RSSI\_NOT\_AVAILABLE

| #define BT\_HCI\_LE\_CS\_PACKET\_RSSI\_NOT\_AVAILABLE   0x7F |
| --- |

## [◆ ](#af69d92b7c92c8fbeeba8e14838a41f74)BT\_HCI\_LE\_CS\_PCT\_I\_MASK

| #define BT\_HCI\_LE\_CS\_PCT\_I\_MASK   0x000FFF |
| --- |

## [◆ ](#a1720b6024f6156e98cb407d6e06e894e)BT\_HCI\_LE\_CS\_PCT\_Q\_MASK

| #define BT\_HCI\_LE\_CS\_PCT\_Q\_MASK   0xFFF000 |
| --- |

## [◆ ](#ae8446a2638bd4009b7dee725bb54c883)BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_CHMAP\_INSTANT\_PASSED

| #define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_CHMAP\_INSTANT\_PASSED   0x3 |
| --- |

## [◆ ](#a21eb191c5d99f902c7a244cad685995f)BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST

| #define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST   0x1 |
| --- |

## [◆ ](#a056a67d663cfdc2189b480fc79946c74)BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_NO\_ABORT

| #define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_NO\_ABORT   0x0 |
| --- |

## [◆ ](#a6dc3f766ce40bbd0ddb7af3cf85677b1)BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_TOO\_FEW\_CHANNELS

| #define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_TOO\_FEW\_CHANNELS   0x2 |
| --- |

## [◆ ](#a1e92177f7be3c6a6be00f97fbfc17dcf)BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_UNSPECIFIED

| #define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_UNSPECIFIED   0xF |
| --- |

## [◆ ](#a821a29dacea9867e4e576f916cf7be3d)BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_ABORTED

| #define BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_ABORTED   0xF |
| --- |

## [◆ ](#ace872d54fba6d94d62b59a2373c7d0d5)BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_COMPLETE

| #define BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_COMPLETE   0x0 |
| --- |

## [◆ ](#af057e8492e52d0c8763d4a2e969d949d)BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_PARTIAL

| #define BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_PARTIAL   0x1 |
| --- |

## [◆ ](#aa4345ca4225d3958968131ba7a5ff950)BT\_HCI\_LE\_CS\_REF\_POWER\_LEVEL\_UNAVAILABLE

| #define BT\_HCI\_LE\_CS\_REF\_POWER\_LEVEL\_UNAVAILABLE   0x7F |
| --- |

## [◆ ](#a4c42a75a04962264257c690ba80f6126)BT\_HCI\_LE\_CS\_REFLECTOR\_ROLE\_MASK

| #define BT\_HCI\_LE\_CS\_REFLECTOR\_ROLE\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#ab7843d7e6463e96bce693b82c3f8cc7d)BT\_HCI\_LE\_CS\_RTT\_AA\_ONLY\_N\_10NS\_MASK

| #define BT\_HCI\_LE\_CS\_RTT\_AA\_ONLY\_N\_10NS\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a2135776cd2413e80b3ad653405f0ec67)BT\_HCI\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_N\_10NS\_MASK

| #define BT\_HCI\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_N\_10NS\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#ad701c1822a44a639bf5a576bf291544f)BT\_HCI\_LE\_CS\_RTT\_SOUNDING\_N\_10NS\_MASK

| #define BT\_HCI\_LE\_CS\_RTT\_SOUNDING\_N\_10NS\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a41bbe08db99fb0a2ef77f4f3103f9b6c)BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST   0x1 |
| --- |

## [◆ ](#a095b6061c31229b951b6b96e5d02381f)BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_ABORT

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_ABORT   0x0 |
| --- |

## [◆ ](#ac4817c265c50019d8f74146f7477bf58)BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_CS\_SYNC\_RECEIVED

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_CS\_SYNC\_RECEIVED   0x2 |
| --- |

## [◆ ](#a31cb520a05fe31313bacf8b021da468c)BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_SCHED\_CONFLICT

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_SCHED\_CONFLICT   0x3 |
| --- |

## [◆ ](#abfdca3ae615e19c8e24c098ba8349618)BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_UNSPECIFIED

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_UNSPECIFIED   0xF |
| --- |

## [◆ ](#af1907f8ae481a08c674d86e689826f49)BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_ABORTED

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_ABORTED   0xF |
| --- |

## [◆ ](#aee251ce3c46dc0404d880be7d4550fa6)BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_COMPLETE

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_COMPLETE   0x0 |
| --- |

## [◆ ](#a414d620018a946fcb6c209b21ad6fb00)BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_PARTIAL

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_PARTIAL   0x1 |
| --- |

## [◆ ](#a385a401b373522160b1832b66838e02d)BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_FREQ\_COMPENSATION\_NOT\_AVAILABLE

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_FREQ\_COMPENSATION\_NOT\_AVAILABLE   0xC000 |
| --- |

## [◆ ](#ae3e9f6d380a61278a8082f07694bdf43)BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_1

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_1   0x01 |
| --- |

## [◆ ](#ad6951a0000c3b5cadfbaae94decb153f)BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_2

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_2   0x02 |
| --- |

## [◆ ](#aaeb365c3f3ea16d760d4943587ea0bd7)BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_3

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_3   0x03 |
| --- |

## [◆ ](#a4cf750ee707ca0b81d4945e4f66798e3)BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_4

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_4   0x04 |
| --- |

## [◆ ](#a6efdde19fbbf06a40d5dc8dee0515af8)BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_IGNORED

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_IGNORED   0x00 |
| --- |

## [◆ ](#a22b108e24f198dfd41b2ad692d448c01)BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_PCT\_NOT\_AVAILABLE

| #define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_PCT\_NOT\_AVAILABLE   0xFFFFFFFF |
| --- |

## [◆ ](#a5a7e8927e6086b70177cc04915d16ff8)BT\_HCI\_LE\_CS\_SUBFEATURE\_CHSEL\_ALG\_3C\_MASK

| #define BT\_HCI\_LE\_CS\_SUBFEATURE\_CHSEL\_ALG\_3C\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a2241cba5ca0dbeb1ea19797654c97397)BT\_HCI\_LE\_CS\_SUBFEATURE\_NO\_TX\_FAE\_MASK

| #define BT\_HCI\_LE\_CS\_SUBFEATURE\_NO\_TX\_FAE\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a4bcdc621f0292fd182f47762a2cf16bb)BT\_HCI\_LE\_CS\_SUBFEATURE\_PBR\_FROM\_RTT\_SOUNDING\_SEQ\_MASK

| #define BT\_HCI\_LE\_CS\_SUBFEATURE\_PBR\_FROM\_RTT\_SOUNDING\_SEQ\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#aeba1a6050a1ff6ad3864132015063026)BT\_HCI\_LE\_CS\_SYNC\_PHYS\_2M\_2BT\_MASK

| #define BT\_HCI\_LE\_CS\_SYNC\_PHYS\_2M\_2BT\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#ad8742ec8b365df1850b6e5f56c39e655)BT\_HCI\_LE\_CS\_SYNC\_PHYS\_2M\_MASK

| #define BT\_HCI\_LE\_CS\_SYNC\_PHYS\_2M\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#acc787bc6363f4c885816a677f7c47db7)BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_100US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_100US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a40d5f49728ef8204e9b19be3da28a5ae)BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_1200US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_1200US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#ac1138ac8f702b4b79bc03c9a7d60207b)BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_15US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_15US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a7023db07ddc8f9e9fbfc59283511bafb)BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_20US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_20US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a77aea9f93d8bcc5949abddcbda52d919)BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_30US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_30US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a93fc4d9abc1964278748d7dacec7d15a)BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_40US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_40US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a9f45646b734d3d831d307485d2c8c076)BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_50US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_50US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a27771be57984aac0b825b3ff033df070)BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_60US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_60US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#ab9c3168510c3e5161c393d7093c3527b)BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_80US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_80US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a85f667356dd1e1d9de288776ec13e721)BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_10US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_10US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a331eff3b3e89a073b30c9d334014b2da)BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_20US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_20US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a62112179c80be4546b29bc39f632f619)BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_30US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_30US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a57232d7cbd988c6d6d01d2462e90a7f5)BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_40US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_40US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a4aa0365eb6bc4f54bbbd3ebc2b717c41)BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_50US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_50US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a647ea407f97ea754f3f729ac8a9bbb02)BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_60US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_60US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a8bd6f366622ed48cea49fc67692349ce)BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_80US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_80US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a46420b559fcc0e584bc604790ae066ae)BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_10US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_10US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a5d279467b3b0b239748b23be57fee63b)BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_20US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_20US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a95d5e9901c50e579600db0ef160425eb)BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_30US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_30US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a66b0bca7c0b19f43b6871cdf05e57543)BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_40US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_40US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a875fa244820e7aea6f1d6674e3d7d72a)BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_50US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_50US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#ab73d093bcb50ebdd5630e85677af6223)BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_60US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_60US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a6d6e20505ba9b86bc254bc3419e5bc04)BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_80US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_80US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a46f2a35868d8422878e89f1ddde0e7dc)BT\_HCI\_LE\_CS\_T\_PM\_TIME\_10US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_PM\_TIME\_10US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a68e13620f22327e8e132aeb19a7cdaf6)BT\_HCI\_LE\_CS\_T\_PM\_TIME\_20US\_MASK

| #define BT\_HCI\_LE\_CS\_T\_PM\_TIME\_20US\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#aa615aebe1d896ca1a06bf618619d96f7)BT\_HCI\_LE\_CS\_TEST\_CONN\_HANDLE

| #define BT\_HCI\_LE\_CS\_TEST\_CONN\_HANDLE   0x0FFF |
| --- |

## [◆ ](#ad0895b572ba1e3d763dbef69c1541b2c)BT\_HCI\_LE\_CS\_TIME\_DIFFERENCE\_NOT\_AVAILABLE

| #define BT\_HCI\_LE\_CS\_TIME\_DIFFERENCE\_NOT\_AVAILABLE   (([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf))0x8000) |
| --- |

## [◆ ](#a932802d089c04b78dd6a541b3ddff1e1)BT\_HCI\_LE\_CS\_TONE\_EXT\_SLOT\_EXT\_EXPECTED

| #define BT\_HCI\_LE\_CS\_TONE\_EXT\_SLOT\_EXT\_EXPECTED   0x2 |
| --- |

## [◆ ](#a72a59878b1445b037eb633a374de92e8)BT\_HCI\_LE\_CS\_TONE\_EXT\_SLOT\_EXT\_NOT\_EXPECTED

| #define BT\_HCI\_LE\_CS\_TONE\_EXT\_SLOT\_EXT\_NOT\_EXPECTED   0x1 |
| --- |

## [◆ ](#adcc92fe105d853cc329bbf4340562835)BT\_HCI\_LE\_CS\_TONE\_QUALITY\_HIGH

| #define BT\_HCI\_LE\_CS\_TONE\_QUALITY\_HIGH   0x0 |
| --- |

## [◆ ](#accc9e73d5fd38c6ab3d108bc3fd039de)BT\_HCI\_LE\_CS\_TONE\_QUALITY\_LOW

| #define BT\_HCI\_LE\_CS\_TONE\_QUALITY\_LOW   0x2 |
| --- |

## [◆ ](#af42a419097a2e8ee37d46419cd5e20c3)BT\_HCI\_LE\_CS\_TONE\_QUALITY\_MED

| #define BT\_HCI\_LE\_CS\_TONE\_QUALITY\_MED   0x1 |
| --- |

## [◆ ](#a2b14945754c982ead67ad3b7e615eba9)BT\_HCI\_LE\_CS\_TONE\_QUALITY\_UNAVAILABLE

| #define BT\_HCI\_LE\_CS\_TONE\_QUALITY\_UNAVAILABLE   0x3 |
| --- |

## [◆ ](#a24c56f19fcf03aabb170925555209f33)BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_18DB\_MASK

| #define BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_18DB\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a80fe1748abbd89e1700c239ff450ce07)BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_21DB\_MASK

| #define BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_21DB\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#acd8cc2c9de0edd52c954b0d70dfa44ac)BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_24DB\_MASK

| #define BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_24DB\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a1f27b2456c323b90eebfa8e45932d92f)BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_27DB\_MASK

| #define BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_27DB\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a5045b5b06b3c79c77a4997066f332d13)BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_30DB\_MASK

| #define BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_30DB\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a442df4f693ae5bb75d1d8f54fe204bda)BT\_HCI\_LE\_CTE\_COUNT\_MAX

| #define BT\_HCI\_LE\_CTE\_COUNT\_MAX   0x10 |
| --- |

## [◆ ](#aec2a77fadbb6bf24267d659a84b7c9a9)BT\_HCI\_LE\_CTE\_COUNT\_MIN

| #define BT\_HCI\_LE\_CTE\_COUNT\_MIN   0x1 |
| --- |

## [◆ ](#a478bc1be161e0b1eb05667bc8b6c9ae5)BT\_HCI\_LE\_CTE\_CRC\_ERR\_CTE\_BASED\_OTHER

| #define BT\_HCI\_LE\_CTE\_CRC\_ERR\_CTE\_BASED\_OTHER   0x2 |
| --- |

## [◆ ](#a3f787f516c3cc233fc700c08552a4034)BT\_HCI\_LE\_CTE\_CRC\_ERR\_CTE\_BASED\_TIME

| #define BT\_HCI\_LE\_CTE\_CRC\_ERR\_CTE\_BASED\_TIME   0x1 |
| --- |

## [◆ ](#ac1ce16d42df9eb71860e51a843dbc943)BT\_HCI\_LE\_CTE\_CRC\_OK

| #define BT\_HCI\_LE\_CTE\_CRC\_OK   0x0 |
| --- |

## [◆ ](#a3bc1e15287e6173d45b7d1e981d6e90e)BT\_HCI\_LE\_CTE\_INSUFFICIENT\_RESOURCES

| #define BT\_HCI\_LE\_CTE\_INSUFFICIENT\_RESOURCES   0xFF |
| --- |

## [◆ ](#acdfe03ade99fa88779b68e435aea23e3)BT\_HCI\_LE\_CTE\_LEN\_MAX

| #define BT\_HCI\_LE\_CTE\_LEN\_MAX   0x14 |
| --- |

## [◆ ](#a80376d34b4d701d5f6092aa101ce0e6c)BT\_HCI\_LE\_CTE\_LEN\_MIN

| #define BT\_HCI\_LE\_CTE\_LEN\_MIN   0x2 |
| --- |

## [◆ ](#a40156c4680916b289b00b1546e0d5bb0)BT\_HCI\_LE\_CTE\_REPORT\_NO\_VALID\_SAMPLE

| #define BT\_HCI\_LE\_CTE\_REPORT\_NO\_VALID\_SAMPLE   0x80 |
| --- |

## [◆ ](#a4d9626f1b9f0601708b3c38386b5f85c)BT\_HCI\_LE\_EXT\_ADV\_FRAG\_DISABLED

| #define BT\_HCI\_LE\_EXT\_ADV\_FRAG\_DISABLED   0x01 |
| --- |

## [◆ ](#aa1dbb6b62c021501320865ac77b5d6da)BT\_HCI\_LE\_EXT\_ADV\_FRAG\_ENABLED

| #define BT\_HCI\_LE\_EXT\_ADV\_FRAG\_ENABLED   0x00 |
| --- |

## [◆ ](#a3b3f91c046b0656d489c228d75c8b3ff)BT\_HCI\_LE\_EXT\_ADV\_FRAG\_MAX\_LEN

| #define BT\_HCI\_LE\_EXT\_ADV\_FRAG\_MAX\_LEN   251 |
| --- |

## [◆ ](#a5394a0dbcd3856ffb8c63440d352120b)BT\_HCI\_LE\_EXT\_ADV\_OP\_COMPLETE\_DATA

| #define BT\_HCI\_LE\_EXT\_ADV\_OP\_COMPLETE\_DATA   0x03 |
| --- |

## [◆ ](#a65b3ae46e1164815cda1325e55df4091)BT\_HCI\_LE\_EXT\_ADV\_OP\_FIRST\_FRAG

| #define BT\_HCI\_LE\_EXT\_ADV\_OP\_FIRST\_FRAG   0x01 |
| --- |

## [◆ ](#a68c62ac99c4198dbadf6563e40ce33cb)BT\_HCI\_LE\_EXT\_ADV\_OP\_INTERM\_FRAG

| #define BT\_HCI\_LE\_EXT\_ADV\_OP\_INTERM\_FRAG   0x00 |
| --- |

## [◆ ](#aade6b8cac66aee356c857fcfae17ce65)BT\_HCI\_LE\_EXT\_ADV\_OP\_LAST\_FRAG

| #define BT\_HCI\_LE\_EXT\_ADV\_OP\_LAST\_FRAG   0x02 |
| --- |

## [◆ ](#a2860ae578d2332a1c76c7bfaa0714e08)BT\_HCI\_LE\_EXT\_ADV\_OP\_UNCHANGED\_DATA

| #define BT\_HCI\_LE\_EXT\_ADV\_OP\_UNCHANGED\_DATA   0x04 |
| --- |

## [◆ ](#a973c2e0fc4cb22d58c47865b9e76b940)BT\_HCI\_LE\_EXT\_ADV\_SID\_INVALID

| #define BT\_HCI\_LE\_EXT\_ADV\_SID\_INVALID   0xFF |
| --- |

## [◆ ](#ae9ba6da1a01dacc52c6a1a2c84d16948)BT\_HCI\_LE\_EXT\_SCAN\_FILTER\_DUP\_ENABLE\_RESET

| #define BT\_HCI\_LE\_EXT\_SCAN\_FILTER\_DUP\_ENABLE\_RESET   0x02 |
| --- |

## [◆ ](#a0ef6a16a2b042b3e7623210fc5fcd1a0)BT\_HCI\_LE\_EXT\_SCAN\_PHY\_1M

| #define BT\_HCI\_LE\_EXT\_SCAN\_PHY\_1M   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#ad0f0fe21e4e9136e09e0a443a7253759)BT\_HCI\_LE\_EXT\_SCAN\_PHY\_2M

| #define BT\_HCI\_LE\_EXT\_SCAN\_PHY\_2M   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#ae15b1ae9e35d060b3a9619d293a7d9ac)BT\_HCI\_LE\_EXT\_SCAN\_PHY\_CODED

| #define BT\_HCI\_LE\_EXT\_SCAN\_PHY\_CODED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a23ce5829beb61d9db40fedfce35c368e)BT\_HCI\_LE\_INTERVAL\_MAX

| #define BT\_HCI\_LE\_INTERVAL\_MAX   0x0c80 |
| --- |

## [◆ ](#adcf6bcefe1d8a34f65597730910bab69)BT\_HCI\_LE\_INTERVAL\_MIN

| #define BT\_HCI\_LE\_INTERVAL\_MIN   0x0006 |
| --- |

All limits according to BT Core Spec v5.4 [Vol 4, Part E].

## [◆ ](#a71f16c552b14042c00e98ea20c1e03c4)BT\_HCI\_LE\_KEY\_TYPE\_DEBUG

| #define BT\_HCI\_LE\_KEY\_TYPE\_DEBUG   0x01 |
| --- |

## [◆ ](#ac85ab1283cd175fc575ebd98b52b3335)BT\_HCI\_LE\_KEY\_TYPE\_GENERATED

| #define BT\_HCI\_LE\_KEY\_TYPE\_GENERATED   0x00 |
| --- |

## [◆ ](#af54ba281111d90f3edb77c0abf9c57b1)BT\_HCI\_LE\_MAX\_CTE\_LEN\_MAX

| #define BT\_HCI\_LE\_MAX\_CTE\_LEN\_MAX   0x14 |
| --- |

## [◆ ](#adee7271e25e6d66ba434502ab56674c3)BT\_HCI\_LE\_MAX\_CTE\_LEN\_MIN

| #define BT\_HCI\_LE\_MAX\_CTE\_LEN\_MIN   0x2 |
| --- |

## [◆ ](#a72d22456f1eb112a75b91faa40e3b776)BT\_HCI\_LE\_MAX\_RX\_OCTETS\_MAX

| #define BT\_HCI\_LE\_MAX\_RX\_OCTETS\_MAX   0x00FB |
| --- |

## [◆ ](#a6c192a213459f5cc7898faa8aa0f5f42)BT\_HCI\_LE\_MAX\_RX\_OCTETS\_MIN

| #define BT\_HCI\_LE\_MAX\_RX\_OCTETS\_MIN   0x001B |
| --- |

## [◆ ](#ad4c16d0e80cb6dc2b6fd65e72e331173)BT\_HCI\_LE\_MAX\_RX\_TIME\_MAX

| #define BT\_HCI\_LE\_MAX\_RX\_TIME\_MAX   0x4290 |
| --- |

## [◆ ](#a6666cbeff0cb43fa4c820ba92311fc11)BT\_HCI\_LE\_MAX\_RX\_TIME\_MIN

| #define BT\_HCI\_LE\_MAX\_RX\_TIME\_MIN   0x0148 |
| --- |

## [◆ ](#a647de996dd2e75a8242e6459abd565f6)BT\_HCI\_LE\_MAX\_SWITCH\_PATTERN\_LEN\_MAX

| #define BT\_HCI\_LE\_MAX\_SWITCH\_PATTERN\_LEN\_MAX   0x4B |
| --- |

## [◆ ](#a327330c5b69e8ec56dd18fcc3fdf0622)BT\_HCI\_LE\_MAX\_SWITCH\_PATTERN\_LEN\_MIN

| #define BT\_HCI\_LE\_MAX\_SWITCH\_PATTERN\_LEN\_MIN   0x2 |
| --- |

## [◆ ](#aec6c2a321f9700572fe8cf84d8bed238)BT\_HCI\_LE\_MAX\_TX\_OCTETS\_MAX

| #define BT\_HCI\_LE\_MAX\_TX\_OCTETS\_MAX   0x00FB |
| --- |

## [◆ ](#a6c731f3c0644818489c146eeca9e3ea8)BT\_HCI\_LE\_MAX\_TX\_OCTETS\_MIN

| #define BT\_HCI\_LE\_MAX\_TX\_OCTETS\_MIN   0x001B |
| --- |

## [◆ ](#aae4ce04bdfd0ad339c87eb18616d8a8a)BT\_HCI\_LE\_MAX\_TX\_TIME\_MAX

| #define BT\_HCI\_LE\_MAX\_TX\_TIME\_MAX   0x4290 |
| --- |

## [◆ ](#ac7c6251a5342a591ff4c413820125f94)BT\_HCI\_LE\_MAX\_TX\_TIME\_MIN

| #define BT\_HCI\_LE\_MAX\_TX\_TIME\_MIN   0x0148 |
| --- |

## [◆ ](#a423acd131760a1ab7b0671c45c9214ca)BT\_HCI\_LE\_MOD\_INDEX\_STABLE

| #define BT\_HCI\_LE\_MOD\_INDEX\_STABLE   0x01 |
| --- |

## [◆ ](#a631e672ab64e36a983d4d3aae789b237)BT\_HCI\_LE\_MOD\_INDEX\_STANDARD

| #define BT\_HCI\_LE\_MOD\_INDEX\_STANDARD   0x00 |
| --- |

## [◆ ](#aeee9fd73771de54542f7ff24f95eceba)BT\_HCI\_LE\_NO\_CTE

| #define BT\_HCI\_LE\_NO\_CTE   0xFF |
| --- |

## [◆ ](#ad9ff685b2854b877e0cdd1ae93272ddf)BT\_HCI\_LE\_NUM\_ANT\_MAX

| #define BT\_HCI\_LE\_NUM\_ANT\_MAX   0x4B |
| --- |

## [◆ ](#a112d3fb3d3ec663278aa4463fedbd89b)BT\_HCI\_LE\_NUM\_ANT\_MIN

| #define BT\_HCI\_LE\_NUM\_ANT\_MIN   0x1 |
| --- |

## [◆ ](#a3a3937965aeb187b6fb18da3b7731ed7)BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOA

| #define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a440aca4bf97bc6b583284ae6c8037a53)BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOD\_1US

| #define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOD\_1US   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#ae2d9be5e54595cb5a426ae8909cdee1c)BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOD\_2US

| #define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOD\_2US   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#af3d8cf0fb8af60c057ba8c24abaf3897)BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_CTE

| #define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_CTE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a6fca2634e0e5b0dd5d86b18666ed38e4)BT\_HCI\_LE\_PAST\_CTE\_TYPE\_ONLY\_CTE

| #define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_ONLY\_CTE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#ac7233f9c34f5e33d765b68b55ebc9b9e)BT\_HCI\_LE\_PAST\_MODE\_NO\_REPORTS

| #define BT\_HCI\_LE\_PAST\_MODE\_NO\_REPORTS   0x01 |
| --- |

## [◆ ](#a65ff1c4a937422000f6f1eadea28ccba)BT\_HCI\_LE\_PAST\_MODE\_NO\_SYNC

| #define BT\_HCI\_LE\_PAST\_MODE\_NO\_SYNC   0x00 |
| --- |

## [◆ ](#aaeac19606d3d5e7d0906b38e2c4b4c69)BT\_HCI\_LE\_PAST\_MODE\_SYNC

| #define BT\_HCI\_LE\_PAST\_MODE\_SYNC   0x02 |
| --- |

## [◆ ](#ab0232a2abc2b7c86b19ae89298ef8c4b)BT\_HCI\_LE\_PAST\_MODE\_SYNC\_FILTER\_DUPLICATES

| #define BT\_HCI\_LE\_PAST\_MODE\_SYNC\_FILTER\_DUPLICATES   0x03 |
| --- |

## [◆ ](#a9faae90b3adfcbcdf7da19c631e68a69)BT\_HCI\_LE\_PATH\_LOSS\_REPORTING\_DISABLE

| #define BT\_HCI\_LE\_PATH\_LOSS\_REPORTING\_DISABLE   0x00 |
| --- |

## [◆ ](#ab2e698e4ebbb45d9e3db0663ae5e4657)BT\_HCI\_LE\_PATH\_LOSS\_REPORTING\_ENABLE

| #define BT\_HCI\_LE\_PATH\_LOSS\_REPORTING\_ENABLE   0x01 |
| --- |

## [◆ ](#a0408b7ecb697bd573b2ea7d2c3c93b92)BT\_HCI\_LE\_PATH\_LOSS\_UNAVAILABLE

| #define BT\_HCI\_LE\_PATH\_LOSS\_UNAVAILABLE   0xFF |
| --- |

## [◆ ](#a4c884821e7136f6f68bc4d92b394381a)BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ALLOWED\_BITS

| #define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ALLOWED\_BITS   5 |
| --- |

## [◆ ](#a6ad9e08bcef788c32481756f76df6a43)BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_INVALID\_VALUE

| #define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_INVALID\_VALUE   (~[BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)([BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ALLOWED\_BITS](#a4c884821e7136f6f68bc4d92b394381a))) |
| --- |

## [◆ ](#a64c7e74877c8ca638217a09d503e742b)BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOA

| #define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#ad349244f13388a7437651e5c3909bcb9)BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOD\_1US

| #define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOD\_1US   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#aae32740df5a3096a9b17b9c06e6cc3e9)BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOD\_2US

| #define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOD\_2US   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a5532c8ee93198eb831c12b182e13a534)BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_CTE

| #define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_CTE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#abb3c8fcfc0b48cf6dbebff206a2a9a48)BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_FILTERING

| #define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_FILTERING   0 |
| --- |

## [◆ ](#aa3b526ab2ed1aeaab0e26a5390b3dcea)BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ONLY\_CTE

| #define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ONLY\_CTE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a29c5cf397f94af42bdea484fa95a2a78)BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_FILTER\_DUPLICATE

| #define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_FILTER\_DUPLICATE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a44f11af392e3188e699d8f987cb2f6d6)BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_REPORTS\_DISABLED

| #define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_REPORTS\_DISABLED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a490bb7d8cf236e49c60771a95d258247)BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_USE\_LIST

| #define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_USE\_LIST   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a7b3cd7870ba4af2ff483a831d2700466)BT\_HCI\_LE\_PER\_ADV\_FRAG\_MAX\_LEN

| #define BT\_HCI\_LE\_PER\_ADV\_FRAG\_MAX\_LEN   252 |
| --- |

## [◆ ](#a2f2216a88cf77ccac1c9a2f6c5820746)BT\_HCI\_LE\_PER\_ADV\_INTERVAL\_MAX

| #define BT\_HCI\_LE\_PER\_ADV\_INTERVAL\_MAX   0xFFFF |
| --- |

## [◆ ](#a04f870ac03c1baca22ab5d984354f3bf)BT\_HCI\_LE\_PER\_ADV\_INTERVAL\_MIN

| #define BT\_HCI\_LE\_PER\_ADV\_INTERVAL\_MIN   0x0006 |
| --- |

## [◆ ](#ada39c45c3c1c7576d4d9794dad115e61)BT\_HCI\_LE\_PER\_ADV\_OP\_COMPLETE\_DATA

| #define BT\_HCI\_LE\_PER\_ADV\_OP\_COMPLETE\_DATA   0x03 |
| --- |

## [◆ ](#a8aeb4c76ec769879fc4796fc2919c459)BT\_HCI\_LE\_PER\_ADV\_OP\_FIRST\_FRAG

| #define BT\_HCI\_LE\_PER\_ADV\_OP\_FIRST\_FRAG   0x01 |
| --- |

## [◆ ](#aa18edf54edfb8d0fcaca5941e8e5e493)BT\_HCI\_LE\_PER\_ADV\_OP\_INTERM\_FRAG

| #define BT\_HCI\_LE\_PER\_ADV\_OP\_INTERM\_FRAG   0x00 |
| --- |

## [◆ ](#a7f2314472ccb051e87d1bb2f9b3fded8)BT\_HCI\_LE\_PER\_ADV\_OP\_LAST\_FRAG

| #define BT\_HCI\_LE\_PER\_ADV\_OP\_LAST\_FRAG   0x02 |
| --- |

## [◆ ](#a9af7ce6ecbd978df6193c4e9c2d8b002)BT\_HCI\_LE\_PERIPHERAL\_LATENCY\_MAX

| #define BT\_HCI\_LE\_PERIPHERAL\_LATENCY\_MAX   0x01f3 |
| --- |

## [◆ ](#a833ae32a3a5ffefbe57c7aa9cdf2e5a9)BT\_HCI\_LE\_PHY\_1M

| #define BT\_HCI\_LE\_PHY\_1M   0x01 |
| --- |

## [◆ ](#a727a1780d5f3754a78dea0476c2b97bb)BT\_HCI\_LE\_PHY\_2M

| #define BT\_HCI\_LE\_PHY\_2M   0x02 |
| --- |

## [◆ ](#ac5173dfe471fe4d1aad0f7d79904e46a)BT\_HCI\_LE\_PHY\_CODED

| #define BT\_HCI\_LE\_PHY\_CODED   0x03 |
| --- |

## [◆ ](#a61909ce217268c8cc6274f16d3db8484)BT\_HCI\_LE\_PHY\_CODED\_ANY

| #define BT\_HCI\_LE\_PHY\_CODED\_ANY   0x00 |
| --- |

## [◆ ](#a54bf26868903f0178b0f9f70111ea6b7)BT\_HCI\_LE\_PHY\_CODED\_S2

| #define BT\_HCI\_LE\_PHY\_CODED\_S2   0x01 |
| --- |

## [◆ ](#abe28c39a93e86d9ad5e6f0c08b09ef9c)BT\_HCI\_LE\_PHY\_CODED\_S8

| #define BT\_HCI\_LE\_PHY\_CODED\_S8   0x02 |
| --- |

## [◆ ](#a8101f257838639b46dcd0d50a92bba0c)BT\_HCI\_LE\_PHY\_PREFER\_1M

| #define BT\_HCI\_LE\_PHY\_PREFER\_1M   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#ae89ffa7723482ced707f8a57febce629)BT\_HCI\_LE\_PHY\_PREFER\_2M

| #define BT\_HCI\_LE\_PHY\_PREFER\_2M   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#ab33fde130c9fdb99559b15455e827a7a)BT\_HCI\_LE\_PHY\_PREFER\_CODED

| #define BT\_HCI\_LE\_PHY\_PREFER\_CODED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a0fb6efaf47f2d676eb51b3fb99d0a691)BT\_HCI\_LE\_PHY\_RX\_ANY

| #define BT\_HCI\_LE\_PHY\_RX\_ANY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a7656d3400ccb540e8bd066cf1232c38e)BT\_HCI\_LE\_PHY\_TX\_ANY

| #define BT\_HCI\_LE\_PHY\_TX\_ANY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a5b394658223fd700fa152c4deb2f956e)BT\_HCI\_LE\_PRIM\_ADV\_INTERVAL\_MAX

| #define BT\_HCI\_LE\_PRIM\_ADV\_INTERVAL\_MAX   0xFFFFFF |
| --- |

## [◆ ](#a1599475c6673d4fa0e00d16024df9a3b)BT\_HCI\_LE\_PRIM\_ADV\_INTERVAL\_MIN

| #define BT\_HCI\_LE\_PRIM\_ADV\_INTERVAL\_MIN   0x000020 |
| --- |

## [◆ ](#ae61d38e84e0d58be45ffaf521abad2f6)BT\_HCI\_LE\_PRIVACY\_MODE\_DEVICE

| #define BT\_HCI\_LE\_PRIVACY\_MODE\_DEVICE   0x01 |
| --- |

## [◆ ](#a423b143e474548458b8bcce59029f722)BT\_HCI\_LE\_PRIVACY\_MODE\_NETWORK

| #define BT\_HCI\_LE\_PRIVACY\_MODE\_NETWORK   0x00 |
| --- |

## [◆ ](#a56f7acd075e03694d966d949f637946c)BT\_HCI\_LE\_RSSI\_NOT\_AVAILABLE

| #define BT\_HCI\_LE\_RSSI\_NOT\_AVAILABLE   0x7F |
| --- |

## [◆ ](#a27c179b4c8e85f840b41c4765613c99b)BT\_HCI\_LE\_RX\_PHY\_1M

| #define BT\_HCI\_LE\_RX\_PHY\_1M   0x01 |
| --- |

## [◆ ](#ac1db92b615a94b30e587a87d3637ad47)BT\_HCI\_LE\_RX\_PHY\_2M

| #define BT\_HCI\_LE\_RX\_PHY\_2M   0x02 |
| --- |

## [◆ ](#a689bc0f95a315c18ee4efbc556d31d60)BT\_HCI\_LE\_RX\_PHY\_CODED

| #define BT\_HCI\_LE\_RX\_PHY\_CODED   0x03 |
| --- |

## [◆ ](#a85450acad700f8cef375d34235752650)BT\_HCI\_LE\_SAMPLE\_CTE\_ALL

| #define BT\_HCI\_LE\_SAMPLE\_CTE\_ALL   0x0 |
| --- |

## [◆ ](#a0c8888c4dfed6ab4c0f07a37ca3b2278)BT\_HCI\_LE\_SAMPLE\_CTE\_COUNT\_MAX

| #define BT\_HCI\_LE\_SAMPLE\_CTE\_COUNT\_MAX   0x10 |
| --- |

## [◆ ](#afd22fac7ff6d5006015159ffc978798a)BT\_HCI\_LE\_SAMPLE\_CTE\_COUNT\_MIN

| #define BT\_HCI\_LE\_SAMPLE\_CTE\_COUNT\_MIN   0x1 |
| --- |

## [◆ ](#ac13c2e39ac1e13cf5cd2cfa248a6f316)BT\_HCI\_LE\_SCAN\_ACTIVE

| #define BT\_HCI\_LE\_SCAN\_ACTIVE   0x01 |
| --- |

## [◆ ](#a152712b517c9ee0452555408d14bbfa7)BT\_HCI\_LE\_SCAN\_DISABLE

| #define BT\_HCI\_LE\_SCAN\_DISABLE   0x00 |
| --- |

## [◆ ](#a6859aeda42fe72b75d5cc1896b7e6afd)BT\_HCI\_LE\_SCAN\_ENABLE

| #define BT\_HCI\_LE\_SCAN\_ENABLE   0x01 |
| --- |

## [◆ ](#a6fb35a340e8eecd7bc2602ed010aa6c1)BT\_HCI\_LE\_SCAN\_FILTER\_DUP\_DISABLE

| #define BT\_HCI\_LE\_SCAN\_FILTER\_DUP\_DISABLE   0x00 |
| --- |

## [◆ ](#a4c9503d4a13f78a1dc44e087af922793)BT\_HCI\_LE\_SCAN\_FILTER\_DUP\_ENABLE

| #define BT\_HCI\_LE\_SCAN\_FILTER\_DUP\_ENABLE   0x01 |
| --- |

## [◆ ](#ac6f3763ab47d20efee1af16d8d019bf3)BT\_HCI\_LE\_SCAN\_FP\_BASIC\_FILTER

| #define BT\_HCI\_LE\_SCAN\_FP\_BASIC\_FILTER   0x01 |
| --- |

## [◆ ](#a278ccd7cfefd1a46f6de843b722f583a)BT\_HCI\_LE\_SCAN\_FP\_BASIC\_NO\_FILTER

| #define BT\_HCI\_LE\_SCAN\_FP\_BASIC\_NO\_FILTER   0x00 |
| --- |

## [◆ ](#a45846e02e2630608b14f62f9b9020f9d)BT\_HCI\_LE\_SCAN\_FP\_EXT\_FILTER

| #define BT\_HCI\_LE\_SCAN\_FP\_EXT\_FILTER   0x03 |
| --- |

## [◆ ](#aed7fa63104bbc551bc0dbfa21e38744a)BT\_HCI\_LE\_SCAN\_FP\_EXT\_NO\_FILTER

| #define BT\_HCI\_LE\_SCAN\_FP\_EXT\_NO\_FILTER   0x02 |
| --- |

## [◆ ](#a2274aacde21083e9633fe59fbff0df87)BT\_HCI\_LE\_SCAN\_PASSIVE

| #define BT\_HCI\_LE\_SCAN\_PASSIVE   0x00 |
| --- |

## [◆ ](#aaf9b76b276b5cf7e02bb5e3b0a12ecf6)BT\_HCI\_LE\_SET\_PER\_ADV\_ENABLE\_ADI

| #define BT\_HCI\_LE\_SET\_PER\_ADV\_ENABLE\_ADI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a1c03932d8c1e2c5436eaf45be093b4d4)BT\_HCI\_LE\_SET\_PER\_ADV\_ENABLE\_ENABLE

| #define BT\_HCI\_LE\_SET\_PER\_ADV\_ENABLE\_ENABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a1aaaffb3044bfd824aa6744867da0a97)BT\_HCI\_LE\_SET\_PER\_ADV\_RECV\_ENABLE\_ENABLE

| #define BT\_HCI\_LE\_SET\_PER\_ADV\_RECV\_ENABLE\_ENABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a08fe0a16e8c1b3eb6b23869b37739f2d)BT\_HCI\_LE\_SET\_PER\_ADV\_RECV\_ENABLE\_FILTER\_DUPLICATE

| #define BT\_HCI\_LE\_SET\_PER\_ADV\_RECV\_ENABLE\_FILTER\_DUPLICATE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a33ce951c9eddfcc5556b0168c14b9769)BT\_HCI\_LE\_SUBRATE\_FACTOR\_MAX

| #define BT\_HCI\_LE\_SUBRATE\_FACTOR\_MAX   0x01f4 |
| --- |

## [◆ ](#a135059b92eba0676689abc78a2f560d3)BT\_HCI\_LE\_SUBRATE\_FACTOR\_MIN

| #define BT\_HCI\_LE\_SUBRATE\_FACTOR\_MIN   0x0001 |
| --- |

All limits according to BT Core Spec v5.4 [Vol 4, Part E].

## [◆ ](#a2564ee96b802cb887f67e3cc38f8f400)BT\_HCI\_LE\_SUPERVISON\_TIMEOUT\_MAX

| #define BT\_HCI\_LE\_SUPERVISON\_TIMEOUT\_MAX   0x0c80 |
| --- |

## [◆ ](#a03dc93eec388a17c286d50395c683fcb)BT\_HCI\_LE\_SUPERVISON\_TIMEOUT\_MIN

| #define BT\_HCI\_LE\_SUPERVISON\_TIMEOUT\_MIN   0x000a |
| --- |

## [◆ ](#ad6bdc84c282a4e35ded32687cba94e9f)BT\_HCI\_LE\_SWITCH\_PATTERN\_LEN\_MAX

| #define BT\_HCI\_LE\_SWITCH\_PATTERN\_LEN\_MAX   0x4B |
| --- |

## [◆ ](#ad74e54836996fc3d02fbb245f9c72b5a)BT\_HCI\_LE\_SWITCH\_PATTERN\_LEN\_MIN

| #define BT\_HCI\_LE\_SWITCH\_PATTERN\_LEN\_MIN   0x2 |
| --- |

## [◆ ](#a6764be57300c8dac30a058ebf8387159)BT\_HCI\_LE\_TEST\_CTE\_DISABLED

| #define BT\_HCI\_LE\_TEST\_CTE\_DISABLED   0x00 |
| --- |

## [◆ ](#a1f45696f06d7bc3f4cc8393bd6967286)BT\_HCI\_LE\_TEST\_CTE\_TYPE\_ANY

| #define BT\_HCI\_LE\_TEST\_CTE\_TYPE\_ANY   0x00 |
| --- |

## [◆ ](#ac4ac180578ed3f662d91c43b5c6b6b53)BT\_HCI\_LE\_TEST\_SLOT\_DURATION\_ANY

| #define BT\_HCI\_LE\_TEST\_SLOT\_DURATION\_ANY   0x00 |
| --- |

## [◆ ](#aef669f8887a165b4948eb651c91968c1)BT\_HCI\_LE\_TEST\_SWITCH\_PATTERN\_LEN\_ANY

| #define BT\_HCI\_LE\_TEST\_SWITCH\_PATTERN\_LEN\_ANY   0x00 |
| --- |

## [◆ ](#a0cb0c8d33e23ff6e59241c88b9e5adee)BT\_HCI\_LE\_TX\_PHY\_1M

| #define BT\_HCI\_LE\_TX\_PHY\_1M   0x01 |
| --- |

## [◆ ](#a7de4598ca06439f89772f0e72306ac3c)BT\_HCI\_LE\_TX\_PHY\_2M

| #define BT\_HCI\_LE\_TX\_PHY\_2M   0x02 |
| --- |

## [◆ ](#a599195b97f069412e112df470bf2b536)BT\_HCI\_LE\_TX\_PHY\_CODED\_S2

| #define BT\_HCI\_LE\_TX\_PHY\_CODED\_S2   0x04 |
| --- |

## [◆ ](#a01d96d9e7bb61db9b3cd31d161b0abf4)BT\_HCI\_LE\_TX\_PHY\_CODED\_S8

| #define BT\_HCI\_LE\_TX\_PHY\_CODED\_S8   0x03 |
| --- |

## [◆ ](#a740a01412d6fad277362634e1854f54b)BT\_HCI\_LE\_TX\_POWER\_PHY\_1M

| #define BT\_HCI\_LE\_TX\_POWER\_PHY\_1M   0x01 |
| --- |

## [◆ ](#aa3eadebe7675de492b01ec117f72d808)BT\_HCI\_LE\_TX\_POWER\_PHY\_2M

| #define BT\_HCI\_LE\_TX\_POWER\_PHY\_2M   0x02 |
| --- |

## [◆ ](#ab2bed6683929c37a3d087dba88309e45)BT\_HCI\_LE\_TX\_POWER\_PHY\_CODED\_S2

| #define BT\_HCI\_LE\_TX\_POWER\_PHY\_CODED\_S2   0x04 |
| --- |

## [◆ ](#a66f2c7c03e65392c3477faddc14d9787)BT\_HCI\_LE\_TX\_POWER\_PHY\_CODED\_S8

| #define BT\_HCI\_LE\_TX\_POWER\_PHY\_CODED\_S8   0x03 |
| --- |

## [◆ ](#a46bac5521c33da56df1d06ed7c472a06)BT\_HCI\_LE\_TX\_POWER\_REPORT\_DISABLE

| #define BT\_HCI\_LE\_TX\_POWER\_REPORT\_DISABLE   0x00 |
| --- |

## [◆ ](#a31f7372543b6dec580fe464ec011d752)BT\_HCI\_LE\_TX\_POWER\_REPORT\_ENABLE

| #define BT\_HCI\_LE\_TX\_POWER\_REPORT\_ENABLE   0x01 |
| --- |

## [◆ ](#a443a5a524ec41bf2ea86eab74dd022dc)BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_LOCAL\_CHANGED

| #define BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_LOCAL\_CHANGED   0x00 |
| --- |

Reason for Transmit power reporting.

## [◆ ](#a268761b9eae9c84f74394a6098f15ee8)BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_READ\_REMOTE\_COMPLETED

| #define BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_READ\_REMOTE\_COMPLETED   0x02 |
| --- |

## [◆ ](#a1fbc1b017b13987a017af7cd90bdf708)BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_REMOTE\_CHANGED

| #define BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_REMOTE\_CHANGED   0x01 |
| --- |

## [◆ ](#af7cc15be8165315ee0358ebb517b5e33)BT\_HCI\_LE\_ZONE\_ENTERED\_HIGH

| #define BT\_HCI\_LE\_ZONE\_ENTERED\_HIGH   0x2 |
| --- |

## [◆ ](#aff1538e314a97aa4910d4f7066dc4d55)BT\_HCI\_LE\_ZONE\_ENTERED\_LOW

| #define BT\_HCI\_LE\_ZONE\_ENTERED\_LOW   0x0 |
| --- |

## [◆ ](#ab88f3d713f6862c08b73752436ca8b1b)BT\_HCI\_LE\_ZONE\_ENTERED\_MIDDLE

| #define BT\_HCI\_LE\_ZONE\_ENTERED\_MIDDLE   0x1 |
| --- |

## [◆ ](#a73dfca6788b272380e6920d2907bf43f)BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_BREDR\_ACL

| #define BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_BREDR\_ACL   0x00 |
| --- |

## [◆ ](#ad10d8c5ffd49cb183731a9ba97c0e058)BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_BREDR\_SCO

| #define BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_BREDR\_SCO   0x01 |
| --- |

## [◆ ](#a560cb22e5f39c144e3d477eea5c32beb)BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_LE\_BIS

| #define BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_LE\_BIS   0x03 |
| --- |

## [◆ ](#a5e53f28cedf59f18ce8d494f16933b3c)BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_LE\_CIS

| #define BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_LE\_CIS   0x02 |
| --- |

## [◆ ](#ac886a10eed1313f6114fcfc3810a34f0)BT\_HCI\_NO\_BONDING

| #define BT\_HCI\_NO\_BONDING   0x00 |
| --- |

## [◆ ](#a89c6d0d285c1c99c51c96d282fe593b9)BT\_HCI\_NO\_BONDING\_MITM

| #define BT\_HCI\_NO\_BONDING\_MITM   0x01 |
| --- |

## [◆ ](#af45bed44788b16be1b172c56c33eea34)BT\_HCI\_OP\_ACCEPT\_CONN\_REQ

| #define BT\_HCI\_OP\_ACCEPT\_CONN\_REQ   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0009) /\* 0x0409 \*/ |
| --- |

## [◆ ](#a97976c13fe03d346313bc19489d45360)BT\_HCI\_OP\_ACCEPT\_SYNC\_CONN\_REQ

| #define BT\_HCI\_OP\_ACCEPT\_SYNC\_CONN\_REQ   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0029) /\* 0x0429 \*/ |
| --- |

## [◆ ](#a4c24e505f9c799275fc2f35619b7df97)BT\_HCI\_OP\_AUTH\_REQUESTED

| #define BT\_HCI\_OP\_AUTH\_REQUESTED   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0011) /\* 0x0411 \*/ |
| --- |

## [◆ ](#a2f95e881ffcda381d8d8ad7ba8705e7d)BT\_HCI\_OP\_CLEAR\_ADV\_SETS

| #define BT\_HCI\_OP\_CLEAR\_ADV\_SETS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x003d) /\* 0x203d \*/ |
| --- |

## [◆ ](#abc80a803d0e540541bcd889772e59940)BT\_HCI\_OP\_CONFIGURE\_DATA\_PATH

| #define BT\_HCI\_OP\_CONFIGURE\_DATA\_PATH   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0083) /\* 0x0c83 \*/ |
| --- |

## [◆ ](#addfd3dec2a69e7e5e2634c4fe63769f2)BT\_HCI\_OP\_CONNECT

| #define BT\_HCI\_OP\_CONNECT   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0005) /\* 0x0405 \*/ |
| --- |

## [◆ ](#ac50eb14115129bcc8c47016a6479149d)BT\_HCI\_OP\_CONNECT\_CANCEL

| #define BT\_HCI\_OP\_CONNECT\_CANCEL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0008) /\* 0x0408 \*/ |
| --- |

## [◆ ](#ab3d8612855550e52a0887e231371fbc2)BT\_HCI\_OP\_DISCONNECT

| #define BT\_HCI\_OP\_DISCONNECT   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0006) /\* 0x0406 \*/ |
| --- |

## [◆ ](#a2e05f146890ad81be27dca91250bf69d)BT\_HCI\_OP\_HOST\_BUFFER\_SIZE

| #define BT\_HCI\_OP\_HOST\_BUFFER\_SIZE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0033) /\* 0x0c33 \*/ |
| --- |

## [◆ ](#a6c7afa8e3b324714bc5f8dce9702604d)BT\_HCI\_OP\_HOST\_NUM\_COMPLETED\_PACKETS

| #define BT\_HCI\_OP\_HOST\_NUM\_COMPLETED\_PACKETS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0035) /\* 0x0c35 \*/ |
| --- |

## [◆ ](#adce48ff5cdde5f4f8ab5bc960717581a)BT\_HCI\_OP\_INQUIRY

| #define BT\_HCI\_OP\_INQUIRY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0001) /\* 0x0401 \*/ |
| --- |

## [◆ ](#ae2d4e5e9cbf056bff03a668e74523442)BT\_HCI\_OP\_INQUIRY\_CANCEL

| #define BT\_HCI\_OP\_INQUIRY\_CANCEL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0002) /\* 0x0402 \*/ |
| --- |

## [◆ ](#a75d9a0acb6522dd0ae290572c4255540)BT\_HCI\_OP\_IO\_CAPABILITY\_NEG\_REPLY

| #define BT\_HCI\_OP\_IO\_CAPABILITY\_NEG\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0034) /\* 0x0434 \*/ |
| --- |

## [◆ ](#a343a3c5c594dd25483fedf38c304a09a)BT\_HCI\_OP\_IO\_CAPABILITY\_REPLY

| #define BT\_HCI\_OP\_IO\_CAPABILITY\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x002b) /\* 0x042b \*/ |
| --- |

## [◆ ](#ade7635c85588941a2e628639be06ce7b)BT\_HCI\_OP\_LE\_ACCEPT\_CIS

| #define BT\_HCI\_OP\_LE\_ACCEPT\_CIS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0066) /\* 0x2066 \*/ |
| --- |

## [◆ ](#a103c6fada57c61fc3f994f8902f4123c)BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_FAL

| #define BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_FAL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0011) /\* 0x2011 \*/ |
| --- |

## [◆ ](#a393378ba85552bb5f41475a863ca649f)BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_PER\_ADV\_LIST

| #define BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_PER\_ADV\_LIST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0047) /\* 0x2047 \*/ |
| --- |

## [◆ ](#a735c643e8afa27c4e7f7be9bfb09676a)BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_RL

| #define BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_RL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0027) /\* 0x2027 \*/ |
| --- |

## [◆ ](#a47af328ede7f14e3d78c81de609af1c9)BT\_HCI\_OP\_LE\_BIG\_CREATE\_SYNC

| #define BT\_HCI\_OP\_LE\_BIG\_CREATE\_SYNC   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x006b) /\* 0x206b \*/ |
| --- |

## [◆ ](#aa7576f4ab30ec7985b4afd08a08800d2)BT\_HCI\_OP\_LE\_BIG\_TERMINATE\_SYNC

| #define BT\_HCI\_OP\_LE\_BIG\_TERMINATE\_SYNC   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x006c) /\* 0x206c \*/ |
| --- |

## [◆ ](#a592ce45c74bdabf1b25954b8021a50bb)BT\_HCI\_OP\_LE\_CLEAR\_FAL

| #define BT\_HCI\_OP\_LE\_CLEAR\_FAL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0010) /\* 0x2010 \*/ |
| --- |

## [◆ ](#affcd4a54d0b26d7b07e39157f17167b4)BT\_HCI\_OP\_LE\_CLEAR\_PER\_ADV\_LIST

| #define BT\_HCI\_OP\_LE\_CLEAR\_PER\_ADV\_LIST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0049) /\* 0x2049 \*/ |
| --- |

## [◆ ](#a5efab85a3beac1fe3fc5a5294a2b1079)BT\_HCI\_OP\_LE\_CLEAR\_RL

| #define BT\_HCI\_OP\_LE\_CLEAR\_RL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0029) /\* 0x2029 \*/ |
| --- |

## [◆ ](#ae488ce598705cf60b78da985015bb42b)BT\_HCI\_OP\_LE\_CONN\_CTE\_REQ\_ENABLE

| #define BT\_HCI\_OP\_LE\_CONN\_CTE\_REQ\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0056) /\* 0x2056 \*/ |
| --- |

## [◆ ](#a150b54d69fb6fe9175336fadb7d81bb8)BT\_HCI\_OP\_LE\_CONN\_CTE\_RSP\_ENABLE

| #define BT\_HCI\_OP\_LE\_CONN\_CTE\_RSP\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0057) /\* 0x2057 \*/ |
| --- |

## [◆ ](#a1fbca6b816791f1967278224f37782c1)BT\_HCI\_OP\_LE\_CONN\_PARAM\_REQ\_NEG\_REPLY

| #define BT\_HCI\_OP\_LE\_CONN\_PARAM\_REQ\_NEG\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0021) /\* 0x2021 \*/ |
| --- |

## [◆ ](#a8b824639d31fa9f579e73cf1f1344c85)BT\_HCI\_OP\_LE\_CONN\_PARAM\_REQ\_REPLY

| #define BT\_HCI\_OP\_LE\_CONN\_PARAM\_REQ\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0020) /\* 0x2020 \*/ |
| --- |

## [◆ ](#ac0c308b64ed89c9b7326982ef04ba6d3)BT\_HCI\_OP\_LE\_CONN\_UPDATE

| #define BT\_HCI\_OP\_LE\_CONN\_UPDATE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0013) /\* 0x2013 \*/ |
| --- |

## [◆ ](#a2a57bb6089e3a064e62119188b555ba9)BT\_HCI\_OP\_LE\_CREATE\_BIG

| #define BT\_HCI\_OP\_LE\_CREATE\_BIG   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0068) /\* 0x2068 \*/ |
| --- |

## [◆ ](#ad0f1ae4be3f5bb90ef967d88dcaaf353)BT\_HCI\_OP\_LE\_CREATE\_BIG\_TEST

| #define BT\_HCI\_OP\_LE\_CREATE\_BIG\_TEST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0069) /\* 0x2069 \*/ |
| --- |

## [◆ ](#a63c9af35a55d9b1ed1b253d057657608)BT\_HCI\_OP\_LE\_CREATE\_CIS

| #define BT\_HCI\_OP\_LE\_CREATE\_CIS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0064) /\* 0x2064 \*/ |
| --- |

## [◆ ](#aadde6f016c942c7907afddf7b6c94304)BT\_HCI\_OP\_LE\_CREATE\_CONN

| #define BT\_HCI\_OP\_LE\_CREATE\_CONN   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x000d) /\* 0x200d \*/ |
| --- |

## [◆ ](#acacd0832cddc00702da74b4a36e5c825)BT\_HCI\_OP\_LE\_CREATE\_CONN\_CANCEL

| #define BT\_HCI\_OP\_LE\_CREATE\_CONN\_CANCEL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x000e) /\* 0x200e \*/ |
| --- |

## [◆ ](#a92e1ec21014999f40172fa1812c36575)BT\_HCI\_OP\_LE\_CS\_ACI\_0

| #define BT\_HCI\_OP\_LE\_CS\_ACI\_0   0x0 |
| --- |

## [◆ ](#a5b082fa5b8ba11a651468cc516d067fe)BT\_HCI\_OP\_LE\_CS\_ACI\_1

| #define BT\_HCI\_OP\_LE\_CS\_ACI\_1   0x1 |
| --- |

## [◆ ](#ab30a4e55002080394c39fb885eba36e4)BT\_HCI\_OP\_LE\_CS\_ACI\_2

| #define BT\_HCI\_OP\_LE\_CS\_ACI\_2   0x2 |
| --- |

## [◆ ](#a76d1452003c0bd3b688765aa2d25047f)BT\_HCI\_OP\_LE\_CS\_ACI\_3

| #define BT\_HCI\_OP\_LE\_CS\_ACI\_3   0x3 |
| --- |

## [◆ ](#af16c4c79e602e6da833b8aa3e0c4bf64)BT\_HCI\_OP\_LE\_CS\_ACI\_4

| #define BT\_HCI\_OP\_LE\_CS\_ACI\_4   0x4 |
| --- |

## [◆ ](#ad980d8f134d940b80dc9b0e3a570ac06)BT\_HCI\_OP\_LE\_CS\_ACI\_5

| #define BT\_HCI\_OP\_LE\_CS\_ACI\_5   0x5 |
| --- |

## [◆ ](#a4c7ff3c949023f4544bf50353a0f082b)BT\_HCI\_OP\_LE\_CS\_ACI\_6

| #define BT\_HCI\_OP\_LE\_CS\_ACI\_6   0x6 |
| --- |

## [◆ ](#acabccf9f5893324dcb6acc0769ab8417)BT\_HCI\_OP\_LE\_CS\_ACI\_7

| #define BT\_HCI\_OP\_LE\_CS\_ACI\_7   0x7 |
| --- |

## [◆ ](#af0d407f944831f8c85f91fb60f5bc618)BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_FOUR

| #define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_FOUR   0x04 |
| --- |

## [◆ ](#aed2444a40bc79ccf3f383dd961036f5e)BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_NONE

| #define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_NONE   0xFF |
| --- |

## [◆ ](#a7fa26323384443ba9c5e635047b74f51)BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_ONE

| #define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_ONE   0x01 |
| --- |

## [◆ ](#afad5b26b2a6ce125b6198856d20bcdd8)BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_REP

| #define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_REP   0xFE |
| --- |

## [◆ ](#a8721a8f4670a8038d66d42adea061f57)BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_THREE

| #define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_THREE   0x03 |
| --- |

## [◆ ](#aa6d146c85e3148a2afb66023d94c2eeb)BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_TWO

| #define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_TWO   0x02 |
| --- |

## [◆ ](#af26aad0e137782c8f12937b1736d6ada)BT\_HCI\_OP\_LE\_CS\_CREATE\_CONFIG

| #define BT\_HCI\_OP\_LE\_CS\_CREATE\_CONFIG   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0090) /\* 0x2090 \*/ |
| --- |

## [◆ ](#a7baf90f5bf691ce6b650677e6c2a9600)BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_1M

| #define BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_1M   0x1 |
| --- |

## [◆ ](#ae49d35db87532e06ea685a63eb89177a)BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M

| #define BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M   0x2 |
| --- |

## [◆ ](#ac34716156b071e06eb454f091a63216c)BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M\_2BT

| #define BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M\_2BT   0x3 |
| --- |

## [◆ ](#a4505bedc3b5aae63b80cf53fc516b342)BT\_HCI\_OP\_LE\_CS\_INITIATOR\_ROLE

| #define BT\_HCI\_OP\_LE\_CS\_INITIATOR\_ROLE   0x0 |
| --- |

## [◆ ](#a74aaa5b6b799dad3af6778e23093b230)BT\_HCI\_OP\_LE\_CS\_INITIATOR\_ROLE\_MASK

| #define BT\_HCI\_OP\_LE\_CS\_INITIATOR\_ROLE\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#af1b7924e50ba017e59d697fd8814d491)BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_1

| #define BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_1   0x1 |
| --- |

## [◆ ](#a714152a085bbc317b539d6e973ccffc6)BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_2

| #define BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_2   0x2 |
| --- |

## [◆ ](#a5d2af0ed5e0cc5cf7d9f0baae512ff68)BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_3

| #define BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_3   0x3 |
| --- |

## [◆ ](#a29a240b2d3f209b1f5f3d96e380dde08)BT\_HCI\_OP\_LE\_CS\_MAX\_MAX\_TX\_POWER

| #define BT\_HCI\_OP\_LE\_CS\_MAX\_MAX\_TX\_POWER   20 |
| --- |

## [◆ ](#a040315a8ac4f80a2c497919a2fd4d7bc)BT\_HCI\_OP\_LE\_CS\_MIN\_MAX\_TX\_POWER

| #define BT\_HCI\_OP\_LE\_CS\_MIN\_MAX\_TX\_POWER   -127 |
| --- |

## [◆ ](#a4eddce6558339caba6a3d16f8fe5d485)BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_ENABLE

| #define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0094) /\* 0x2094 \*/ |
| --- |

## [◆ ](#a3a8f1c94f40696f18e18810f736497e3)BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_1M

| #define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_1M   0x01 |
| --- |

## [◆ ](#a016f68a621de8d332f3073df4faf1702)BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_2M

| #define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_2M   0x02 |
| --- |

## [◆ ](#a776a14d8e7fdca584475f26b441c8bfb)BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S2

| #define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S2   0x04 |
| --- |

## [◆ ](#a2543f9fa20db642fb8b47b949c50af6a)BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S8

| #define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S8   0x03 |
| --- |

## [◆ ](#a3e01bbe3a72c946015a288ee49d3cbdd)BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_DISABLED

| #define BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_DISABLED   0x00 |
| --- |

## [◆ ](#a4a88120ae7e83fd791012c913315d14f)BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_ENABLED

| #define BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_ENABLED   0x01 |
| --- |

## [◆ ](#a84e0338551dd8256a821d960bf745208)BT\_HCI\_OP\_LE\_CS\_READ\_LOCAL\_SUPPORTED\_CAPABILITIES

| #define BT\_HCI\_OP\_LE\_CS\_READ\_LOCAL\_SUPPORTED\_CAPABILITIES   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0089) /\* 0x2089 \*/ |
| --- |

## [◆ ](#afa7a0214b145891562f1d2b7b16860ab)BT\_HCI\_OP\_LE\_CS\_READ\_REMOTE\_FAE\_TABLE

| #define BT\_HCI\_OP\_LE\_CS\_READ\_REMOTE\_FAE\_TABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x008E) /\* 0x208E \*/ |
| --- |

## [◆ ](#a4f6dd157a555e06cd028a9097fd7b81a)BT\_HCI\_OP\_LE\_CS\_READ\_REMOTE\_SUPPORTED\_CAPABILITIES

| #define BT\_HCI\_OP\_LE\_CS\_READ\_REMOTE\_SUPPORTED\_CAPABILITIES   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x008A) /\* 0x208A \*/ |
| --- |

## [◆ ](#aeb3715dfcac55a46532f51279e29708c)BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_ROLE

| #define BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_ROLE   0x1 |
| --- |

## [◆ ](#a1beb2f602b3635fee272580f0f2f8719)BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_ROLE\_MASK

| #define BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_ROLE\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a54116ddaa8338d59b23fb879c185a399)BT\_HCI\_OP\_LE\_CS\_REMOVE\_CONFIG

| #define BT\_HCI\_OP\_LE\_CS\_REMOVE\_CONFIG   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0091) /\* 0x2091 \*/ |
| --- |

## [◆ ](#a1fe5e94fbd1156c8196c8e1ab9816bac)BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_128BIT\_RAND

| #define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_128BIT\_RAND   0x6 |
| --- |

## [◆ ](#abe4efee7cf9371129f4b5bd650b0d64a)BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_RAND

| #define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_RAND   0x3 |
| --- |

## [◆ ](#aa2ae18252a20ef3481d2402f8924cdda)BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_SOUND

| #define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_SOUND   0x1 |
| --- |

## [◆ ](#a77e56fd5302673f6ef295c0cceabdc9f)BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_64BIT\_RAND

| #define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_64BIT\_RAND   0x4 |
| --- |

## [◆ ](#aa60f64ff7259fd79fb1da2c063530348)BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_RAND

| #define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_RAND   0x5 |
| --- |

## [◆ ](#a73cbfe2a942b684ac0b5b50d900fb83f)BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_SOUND

| #define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_SOUND   0x2 |
| --- |

## [◆ ](#a759eb7a8e43ee7cf1ea88ddd3e69feb5)BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_AA\_ONLY

| #define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_AA\_ONLY   0x0 |
| --- |

## [◆ ](#a574168efdaa5729aec9699d48f988d77)BT\_HCI\_OP\_LE\_CS\_SECURITY\_ENABLE

| #define BT\_HCI\_OP\_LE\_CS\_SECURITY\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x008C) /\* 0x208C \*/ |
| --- |

## [◆ ](#a880439089735247c7011862d5b3e090f)BT\_HCI\_OP\_LE\_CS\_SET\_CHANNEL\_CLASSIFICATION

| #define BT\_HCI\_OP\_LE\_CS\_SET\_CHANNEL\_CLASSIFICATION   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0092) /\* 0x2092 \*/ |
| --- |

## [◆ ](#addb1ab37dc75ab5389d74c6c96629b02)BT\_HCI\_OP\_LE\_CS\_SET\_DEFAULT\_SETTINGS

| #define BT\_HCI\_OP\_LE\_CS\_SET\_DEFAULT\_SETTINGS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x008D) /\* 0x208D \*/ |
| --- |

## [◆ ](#ad74850cecd8d8dd8a7878d944abdb411)BT\_HCI\_OP\_LE\_CS\_SET\_PROCEDURE\_PARAMETERS

| #define BT\_HCI\_OP\_LE\_CS\_SET\_PROCEDURE\_PARAMETERS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0093) /\* 0x2093 \*/ |
| --- |

## [◆ ](#a96b13fb3b363a5436e1b9633f54bb248)BT\_HCI\_OP\_LE\_CS\_SNR\_18

| #define BT\_HCI\_OP\_LE\_CS\_SNR\_18   0x0 |
| --- |

## [◆ ](#a4b93a8bceafd49d6ca65816924bb4230)BT\_HCI\_OP\_LE\_CS\_SNR\_21

| #define BT\_HCI\_OP\_LE\_CS\_SNR\_21   0x1 |
| --- |

## [◆ ](#a135a4dc2f191d2a931b4270e00774cb2)BT\_HCI\_OP\_LE\_CS\_SNR\_24

| #define BT\_HCI\_OP\_LE\_CS\_SNR\_24   0x2 |
| --- |

## [◆ ](#a52eb27d8f726a2ed6859149fcdf2355d)BT\_HCI\_OP\_LE\_CS\_SNR\_27

| #define BT\_HCI\_OP\_LE\_CS\_SNR\_27   0x3 |
| --- |

## [◆ ](#a181c2d98b93bd18e9edc11a6f9535331)BT\_HCI\_OP\_LE\_CS\_SNR\_30

| #define BT\_HCI\_OP\_LE\_CS\_SNR\_30   0x4 |
| --- |

## [◆ ](#a4aa2e02ce5110be3dc68a801bb583372)BT\_HCI\_OP\_LE\_CS\_SNR\_NOT\_USED

| #define BT\_HCI\_OP\_LE\_CS\_SNR\_NOT\_USED   0xFF |
| --- |

## [◆ ](#a219243d501bbcb6d62668398cde79fca)BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_1

| #define BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_1   0x1 |
| --- |

## [◆ ](#ada09c787fca0a1d54bb754635489b51e)BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_2

| #define BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_2   0x2 |
| --- |

## [◆ ](#a4b48c199b6b75e9dd62ec36883b40aa4)BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_3

| #define BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_3   0x3 |
| --- |

## [◆ ](#ab3fce1eb448b0ade581e4e12b2d56039)BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_UNUSED

| #define BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_UNUSED   0xFF |
| --- |

## [◆ ](#af09601cffd1adf3f8b623868d8f8a3e9)BT\_HCI\_OP\_LE\_CS\_TEST

| #define BT\_HCI\_OP\_LE\_CS\_TEST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0095) /\* 0x2095 \*/ |
| --- |

## [◆ ](#aa4ba4be270035da446389766b795c327)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_00

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_00   0x0 |
| --- |

## [◆ ](#aa0e9e2081d3cbbb60de9b6dcffe77239)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_01

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_01   0x1 |
| --- |

## [◆ ](#a762c5efa09e1fba989fdfb0bdcba9b9c)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_02

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_02   0x2 |
| --- |

## [◆ ](#a2cc7a5d5d2105b1a428703e274cc5388)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_03

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_03   0x3 |
| --- |

## [◆ ](#a03ffb0ffb8e98b26390575b153471bab)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_04

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_04   0x4 |
| --- |

## [◆ ](#adbd3820e0ffa5f99e27778217d477010)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_05

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_05   0x5 |
| --- |

## [◆ ](#a70607449d6bd6207783e319e77d63b16)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_06

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_06   0x6 |
| --- |

## [◆ ](#acc79a879ea527c2901a8b91dae58d0ed)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_07

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_07   0x7 |
| --- |

## [◆ ](#a9dfd88863d649182855edc8c268107d6)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_08

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_08   0x8 |
| --- |

## [◆ ](#ae5a27304aa1cefdfb26ae2cbf42532e3)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_09

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_09   0x9 |
| --- |

## [◆ ](#a0e9664c52808aa246218f92a4fb55516)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_10

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_10   0xA |
| --- |

## [◆ ](#a8fbc80d91e4a1ae04c76cda189cd5d83)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_11

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_11   0xB |
| --- |

## [◆ ](#a4c4a44bd33ebf97852e6640b0d510fdd)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_12

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_12   0xC |
| --- |

## [◆ ](#a08690b2f762d24c34966b839a6d5e696)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_13

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_13   0xD |
| --- |

## [◆ ](#ac2cd3ed1583f86af0480b8481cedca1e)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_14

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_14   0xE |
| --- |

## [◆ ](#ab2b0745d98053775e9bf073e36ce5d78)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_15

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_15   0xF |
| --- |

## [◆ ](#add2c42aa2583b93b0f98ac33ca61ca9d)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_16

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_16   0x10 |
| --- |

## [◆ ](#a08db476ea6516691baeb9007b553281d)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_17

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_17   0x11 |
| --- |

## [◆ ](#a9f0bf05cb0aac50e1df43397c3b913bc)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_18

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_18   0x12 |
| --- |

## [◆ ](#a5df817bdfefc4de0a1309cf71908a105)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_19

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_19   0x13 |
| --- |

## [◆ ](#ae64e5a409523b94ef1ce315ed49afed0)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_20

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_20   0x14 |
| --- |

## [◆ ](#a46f70b5096593956795cc381e33c4aa2)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_21

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_21   0x15 |
| --- |

## [◆ ](#abe9fa4621e9c004421170b0166ea14e1)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_22

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_22   0x16 |
| --- |

## [◆ ](#afc41ca64d03a7ed8ea82a641a0217436)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_23

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_23   0x17 |
| --- |

## [◆ ](#ac9d7cb5a339759b7e0c4ed150a487ca3)BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_LOOP

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_LOOP   0xFF |
| --- |

## [◆ ](#acd33fc2eb3f5ebe10cbe4c5060f8336b)BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_HAT

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_HAT   0x0 |
| --- |

## [◆ ](#ad09c735ab352d7a546cade296e915e85)BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_X

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_X   0x1 |
| --- |

## [◆ ](#a77d27762b9faa7743a55d822a1839eac)BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3B

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3B   0x0 |
| --- |

## [◆ ](#af17f867204bc7cf99e5d530c39302be0)BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3C

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3C   0x1 |
| --- |

## [◆ ](#a4c45c8b2b33ae857c654cc100b5e5550)BT\_HCI\_OP\_LE\_CS\_TEST\_END

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_END   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0096) /\* 0x2096 \*/ |
| --- |

## [◆ ](#a50eb827977c0c596cb357ed62a6e80bd)BT\_HCI\_OP\_LE\_CS\_TEST\_MAXIMIZE\_TX\_POWER

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_MAXIMIZE\_TX\_POWER   0x7F |
| --- |

## [◆ ](#a500597c78a6ada65d1224960bf6a370f)BT\_HCI\_OP\_LE\_CS\_TEST\_MINIMIZE\_TX\_POWER

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_MINIMIZE\_TX\_POWER   0x7E |
| --- |

## [◆ ](#a0a73e0d46b5ca0e94b4bb00d2f79e89d)BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_0\_MASK

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_0\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a90c77fe0022f016453a8eb174b8fcd63)BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_10\_MASK

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_10\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#a2a62cbc191abd177cbf5aea27112fb8b)BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_2\_MASK

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_2\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a560f6f1bddedc60b3a373778bc56b1a7)BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_3\_MASK

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_3\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a36c2c6debe6bf395853112c68a726d25)BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_4\_MASK

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_4\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a4aca98e213ba81c999c8495310af9320)BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_5\_MASK

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_5\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#afd7b8b4ec0baf526cc4335d26c380b62)BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_6\_MASK

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_6\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a695d2ba272dbdd2681ab9216d00ca43a)BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_7\_MASK

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_7\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#ad92a29871be9aff39802fdea4446ef4b)BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_8\_MASK

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_8\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#a04a26b8600cac8c82247a7d51122f600)BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00000000

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00000000   0x05 |
| --- |

## [◆ ](#abf19d511680005828add231d64e1e3f0)BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00001111

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00001111   0x06 |
| --- |

## [◆ ](#a53f0ca5604489a38a1367736a5297b45)BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_01010101

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_01010101   0x07 |
| --- |

## [◆ ](#ae133ef2939518d660df5322551157d47)BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_10101010

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_10101010   0x02 |
| --- |

## [◆ ](#af20dfb1e245afc06a495179d700f126f)BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11110000

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11110000   0x01 |
| --- |

## [◆ ](#aa94eda86c6ffe85a65267f285dae5cb1)BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11111111

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11111111   0x04 |
| --- |

## [◆ ](#a92bc70a5ad7938a46ac9f2127f1bc2d9)BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS15

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS15   0x03 |
| --- |

## [◆ ](#a4f922c5e0662adf8471686dfa9b719ec)BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS9

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS9   0x00 |
| --- |

## [◆ ](#a94007d8250c3524ad0b86745dbb74b3b)BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_USER

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_USER   0x80 |
| --- |

## [◆ ](#a1f2bfc1afab1928321c01beddb658f01)BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_2\_POSITION\_NOT\_PRESENT

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_2\_POSITION\_NOT\_PRESENT   0xFF |
| --- |

## [◆ ](#a45e1ff56f1a6dcc59b784905e4fc6726)BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_0011

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_0011   0x0 |
| --- |

## [◆ ](#a5d3c206a5067ddc5a02a5d5e8c3eb7a3)BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_1100

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_1100   0x1 |
| --- |

## [◆ ](#a24d2e56f620500905572e786f2523b0e)BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_LOOP

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_LOOP   0x2 |
| --- |

## [◆ ](#ad7a89a9365e20e4cd1e44bdb74ae7ecb)BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_BOTH

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_BOTH   0x3 |
| --- |

## [◆ ](#a0513bf5ca6eb9f43a7e8cecaf943c4d7)BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_INIT

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_INIT   0x1 |
| --- |

## [◆ ](#a9ed8967faa3ee3824433422709148330)BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_NONE

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_NONE   0x0 |
| --- |

## [◆ ](#aa24ae1cf1501de66660051a4a62246df)BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REFL

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REFL   0x2 |
| --- |

## [◆ ](#a50fba6ab75b37ccf39452211ba05e896)BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REPEAT

| #define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REPEAT   0x4 |
| --- |

## [◆ ](#a44eb5d70628f6522a08b1327588df979)BT\_HCI\_OP\_LE\_CS\_WRITE\_CACHED\_REMOTE\_FAE\_TABLE

| #define BT\_HCI\_OP\_LE\_CS\_WRITE\_CACHED\_REMOTE\_FAE\_TABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x008F) /\* 0x208F \*/ |
| --- |

## [◆ ](#acdbbe0da013fb3b6da5514498c3932dd)BT\_HCI\_OP\_LE\_CS\_WRITE\_CACHED\_REMOTE\_SUPPORTED\_CAPABILITIES

| #define BT\_HCI\_OP\_LE\_CS\_WRITE\_CACHED\_REMOTE\_SUPPORTED\_CAPABILITIES   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x008B) /\* 0x208B \*/ |
| --- |

## [◆ ](#a650fe2941ffe238b16fd99ed5e78b25a)BT\_HCI\_OP\_LE\_DEFAULT\_PAST\_PARAM

| #define BT\_HCI\_OP\_LE\_DEFAULT\_PAST\_PARAM   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x005d) /\* 0x205d \*/ |
| --- |

## [◆ ](#a99fdd1dbff627a2f627e7d9eced68326)BT\_HCI\_OP\_LE\_ENCRYPT

| #define BT\_HCI\_OP\_LE\_ENCRYPT   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0017) /\* 0x2017 \*/ |
| --- |

## [◆ ](#aebd5487b500c54a47a926bb1daa56f5e)BT\_HCI\_OP\_LE\_ENH\_READ\_TX\_POWER\_LEVEL

| #define BT\_HCI\_OP\_LE\_ENH\_READ\_TX\_POWER\_LEVEL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0076) /\* 0x2076 \*/ |
| --- |

## [◆ ](#a51c3637712a8701ae7fee16806f677df)BT\_HCI\_OP\_LE\_ENH\_RX\_TEST

| #define BT\_HCI\_OP\_LE\_ENH\_RX\_TEST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0033) /\* 0x2033 \*/ |
| --- |

## [◆ ](#a903b1ce0bfe7df7de86bae5fb143e88f)BT\_HCI\_OP\_LE\_ENH\_TX\_TEST

| #define BT\_HCI\_OP\_LE\_ENH\_TX\_TEST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0034) /\* 0x2034 \*/ |
| --- |

## [◆ ](#ac498c9cd93b664b5bd2e58982d36d7ad)BT\_HCI\_OP\_LE\_EXT\_CREATE\_CONN

| #define BT\_HCI\_OP\_LE\_EXT\_CREATE\_CONN   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0043) /\* 0x2043 \*/ |
| --- |

## [◆ ](#a1b6bc4da843ed8d04e0b9571465ffd12)BT\_HCI\_OP\_LE\_EXT\_CREATE\_CONN\_V2

| #define BT\_HCI\_OP\_LE\_EXT\_CREATE\_CONN\_V2   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0085) /\* 0x2085 \*/ |
| --- |

## [◆ ](#af2625fcbc0f29199f1a95dc9fe0f929d)BT\_HCI\_OP\_LE\_GENERATE\_DHKEY

| #define BT\_HCI\_OP\_LE\_GENERATE\_DHKEY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0026) /\* 0x2026 \*/ |
| --- |

## [◆ ](#aa7bf82632c6df22096210de18902a465)BT\_HCI\_OP\_LE\_GENERATE\_DHKEY\_V2

| #define BT\_HCI\_OP\_LE\_GENERATE\_DHKEY\_V2   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x005e) /\* 0x205e \*/ |
| --- |

## [◆ ](#a2b988ffc8ffd10ce1dfde377afa699e1)BT\_HCI\_OP\_LE\_ISO\_READ\_TEST\_COUNTERS

| #define BT\_HCI\_OP\_LE\_ISO\_READ\_TEST\_COUNTERS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0072) /\* 0x2072 \*/ |
| --- |

## [◆ ](#a467736569f030fbb433000e712f1b08e)BT\_HCI\_OP\_LE\_ISO\_RECEIVE\_TEST

| #define BT\_HCI\_OP\_LE\_ISO\_RECEIVE\_TEST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0071) /\* 0x2071 \*/ |
| --- |

## [◆ ](#a86436e6b0cb17de95b438f192bbff1d2)BT\_HCI\_OP\_LE\_ISO\_TEST\_END

| #define BT\_HCI\_OP\_LE\_ISO\_TEST\_END   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0073) /\* 0x2073 \*/ |
| --- |

## [◆ ](#a740f1964df5bdb675906c87ad8ee0cef)BT\_HCI\_OP\_LE\_ISO\_TRANSMIT\_TEST

| #define BT\_HCI\_OP\_LE\_ISO\_TRANSMIT\_TEST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0070) /\* 0x2070 \*/ |
| --- |

## [◆ ](#ae04bd3c7ff17142f2b47e24accdf6a20)BT\_HCI\_OP\_LE\_LTK\_REQ\_NEG\_REPLY

| #define BT\_HCI\_OP\_LE\_LTK\_REQ\_NEG\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x001b) /\* 0x201b \*/ |
| --- |

## [◆ ](#a92050425248585bd1c3873e8593db362)BT\_HCI\_OP\_LE\_LTK\_REQ\_REPLY

| #define BT\_HCI\_OP\_LE\_LTK\_REQ\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x001a) /\* 0x201a \*/ |
| --- |

## [◆ ](#ab1ff230560c1f7712e23a22eb44f0e69)BT\_HCI\_OP\_LE\_P256\_PUBLIC\_KEY

| #define BT\_HCI\_OP\_LE\_P256\_PUBLIC\_KEY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0025) /\* 0x2025 \*/ |
| --- |

## [◆ ](#a177ec628eac4a7d535cfe6c07123cb34)BT\_HCI\_OP\_LE\_PAST\_PARAM

| #define BT\_HCI\_OP\_LE\_PAST\_PARAM   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x005c) /\* 0x205c \*/ |
| --- |

## [◆ ](#a589c2da26ce325d5cb45726c772cf7ab)BT\_HCI\_OP\_LE\_PER\_ADV\_CREATE\_SYNC

| #define BT\_HCI\_OP\_LE\_PER\_ADV\_CREATE\_SYNC   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0044) /\* 0x2044 \*/ |
| --- |

## [◆ ](#a3803042099104029f5b49536cb769e6c)BT\_HCI\_OP\_LE\_PER\_ADV\_CREATE\_SYNC\_CANCEL

| #define BT\_HCI\_OP\_LE\_PER\_ADV\_CREATE\_SYNC\_CANCEL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0045) /\* 0x2045 \*/ |
| --- |

## [◆ ](#ab7d661097af4cc612ac6631b18bbc7e3)BT\_HCI\_OP\_LE\_PER\_ADV\_SET\_INFO\_TRANSFER

| #define BT\_HCI\_OP\_LE\_PER\_ADV\_SET\_INFO\_TRANSFER   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x005b) /\* 0x205b \*/ |
| --- |

## [◆ ](#aa1d0bc8ccc0e1e8835938f8e8d87b7f1)BT\_HCI\_OP\_LE\_PER\_ADV\_SYNC\_TRANSFER

| #define BT\_HCI\_OP\_LE\_PER\_ADV\_SYNC\_TRANSFER   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x005a) /\* 0x205a \*/ |
| --- |

## [◆ ](#a57b7b3cab371b4dd230343dfbc5a5e98)BT\_HCI\_OP\_LE\_PER\_ADV\_TERMINATE\_SYNC

| #define BT\_HCI\_OP\_LE\_PER\_ADV\_TERMINATE\_SYNC   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0046) /\* 0x2046 \*/ |
| --- |

## [◆ ](#ac3af817deaf472dbb2a825fd57b67f42)BT\_HCI\_OP\_LE\_RAND

| #define BT\_HCI\_OP\_LE\_RAND   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0018) /\* 0x2018 \*/ |
| --- |

## [◆ ](#afd47d6bbfd4688383aaa6b5014cf0019)BT\_HCI\_OP\_LE\_READ\_ADV\_CHAN\_TX\_POWER

| #define BT\_HCI\_OP\_LE\_READ\_ADV\_CHAN\_TX\_POWER   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0007) /\* 0x2007 \*/ |
| --- |

## [◆ ](#aff3ea5f19135609d5553cacec0d700a6)BT\_HCI\_OP\_LE\_READ\_ANT\_INFO

| #define BT\_HCI\_OP\_LE\_READ\_ANT\_INFO   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0058) /\* 0x2058 \*/ |
| --- |

## [◆ ](#a965e30fec3f9b5956bd2ea38e57b8b00)BT\_HCI\_OP\_LE\_READ\_BUFFER\_SIZE

| #define BT\_HCI\_OP\_LE\_READ\_BUFFER\_SIZE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0002) /\* 0x2002 \*/ |
| --- |

## [◆ ](#aa7e78541d152c21e101fab5a094c972f)BT\_HCI\_OP\_LE\_READ\_BUFFER\_SIZE\_V2

| #define BT\_HCI\_OP\_LE\_READ\_BUFFER\_SIZE\_V2   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0060) /\* 0x2060 \*/ |
| --- |

## [◆ ](#a9040e4b5e719d53cc324faa280a670a4)BT\_HCI\_OP\_LE\_READ\_CHAN\_MAP

| #define BT\_HCI\_OP\_LE\_READ\_CHAN\_MAP   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0015) /\* 0x2015 \*/ |
| --- |

## [◆ ](#aa58d9ce08e0f1d4a3e5a2f2b1733a6d2)BT\_HCI\_OP\_LE\_READ\_DEFAULT\_DATA\_LEN

| #define BT\_HCI\_OP\_LE\_READ\_DEFAULT\_DATA\_LEN   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0023) /\* 0x2023 \*/ |
| --- |

## [◆ ](#aeeba2e21bd5e33abbd48fa18f5e252f3)BT\_HCI\_OP\_LE\_READ\_FAL\_SIZE

| #define BT\_HCI\_OP\_LE\_READ\_FAL\_SIZE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x000f) /\* 0x200f \*/ |
| --- |

## [◆ ](#acd6367a62d2c80d9f2e796d7b6ab1417)BT\_HCI\_OP\_LE\_READ\_ISO\_LINK\_QUALITY

| #define BT\_HCI\_OP\_LE\_READ\_ISO\_LINK\_QUALITY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0075) /\* 0x2075 \*/ |
| --- |

## [◆ ](#acb7f49f17a60a4e29270c8719b7aeeed)BT\_HCI\_OP\_LE\_READ\_ISO\_TX\_SYNC

| #define BT\_HCI\_OP\_LE\_READ\_ISO\_TX\_SYNC   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0061) /\* 0x2061 \*/ |
| --- |

## [◆ ](#ae4e1d6098793b91ee0e4974886b98336)BT\_HCI\_OP\_LE\_READ\_LOCAL\_FEATURES

| #define BT\_HCI\_OP\_LE\_READ\_LOCAL\_FEATURES   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0003) /\* 0x2003 \*/ |
| --- |

## [◆ ](#af8ec9d3b6889a8530bc5977b8594fea6)BT\_HCI\_OP\_LE\_READ\_LOCAL\_RPA

| #define BT\_HCI\_OP\_LE\_READ\_LOCAL\_RPA   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x002c) /\* 0x202c \*/ |
| --- |

## [◆ ](#a0246ea11fada7570bf59e73250b49b95)BT\_HCI\_OP\_LE\_READ\_MAX\_ADV\_DATA\_LEN

| #define BT\_HCI\_OP\_LE\_READ\_MAX\_ADV\_DATA\_LEN   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x003a) /\* 0x203a \*/ |
| --- |

## [◆ ](#aafb5872650d77d9f4c6ae43038ef2bf1)BT\_HCI\_OP\_LE\_READ\_MAX\_DATA\_LEN

| #define BT\_HCI\_OP\_LE\_READ\_MAX\_DATA\_LEN   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x002f) /\* 0x202f \*/ |
| --- |

## [◆ ](#a8d2a855322d0aa454ed00e1458cf9a38)BT\_HCI\_OP\_LE\_READ\_NUM\_ADV\_SETS

| #define BT\_HCI\_OP\_LE\_READ\_NUM\_ADV\_SETS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x003b) /\* 0x203b \*/ |
| --- |

## [◆ ](#a6c605e63bd1633f3423a915cf4db00e8)BT\_HCI\_OP\_LE\_READ\_PEER\_RPA

| #define BT\_HCI\_OP\_LE\_READ\_PEER\_RPA   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x002b) /\* 0x202b \*/ |
| --- |

## [◆ ](#a3e2fd45c015809e131ac6b3f6a9c72fc)BT\_HCI\_OP\_LE\_READ\_PER\_ADV\_LIST\_SIZE

| #define BT\_HCI\_OP\_LE\_READ\_PER\_ADV\_LIST\_SIZE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x004a) /\* 0x204a \*/ |
| --- |

## [◆ ](#ad2e063f4522a64ceeb36c1d95835e74e)BT\_HCI\_OP\_LE\_READ\_PHY

| #define BT\_HCI\_OP\_LE\_READ\_PHY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0030) /\* 0x2030 \*/ |
| --- |

## [◆ ](#ac8d5165a3a5d190b8e2d31feb79a17c9)BT\_HCI\_OP\_LE\_READ\_REMOTE\_FEATURES

| #define BT\_HCI\_OP\_LE\_READ\_REMOTE\_FEATURES   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0016) /\* 0x2016 \*/ |
| --- |

## [◆ ](#ac5bc187df83f28a48ba1f87f84aed54a)BT\_HCI\_OP\_LE\_READ\_REMOTE\_TX\_POWER\_LEVEL

| #define BT\_HCI\_OP\_LE\_READ\_REMOTE\_TX\_POWER\_LEVEL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0077) /\* 0x2077 \*/ |
| --- |

## [◆ ](#a6c454d3276f7eaae542b13becad6482c)BT\_HCI\_OP\_LE\_READ\_RF\_PATH\_COMP

| #define BT\_HCI\_OP\_LE\_READ\_RF\_PATH\_COMP   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x004c) /\* 0x204c \*/ |
| --- |

## [◆ ](#a45b38708e807c784bd734ba1f69c7f86)BT\_HCI\_OP\_LE\_READ\_RL\_SIZE

| #define BT\_HCI\_OP\_LE\_READ\_RL\_SIZE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x002a) /\* 0x202a \*/ |
| --- |

## [◆ ](#a286869ebde03594d56ecd8bc1aa7c73c)BT\_HCI\_OP\_LE\_READ\_SUPP\_STATES

| #define BT\_HCI\_OP\_LE\_READ\_SUPP\_STATES   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x001c) /\* 0x201c \*/ |
| --- |

## [◆ ](#a77d132306109474465575369db342dbd)BT\_HCI\_OP\_LE\_READ\_TX\_POWER

| #define BT\_HCI\_OP\_LE\_READ\_TX\_POWER   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x004b) /\* 0x204b \*/ |
| --- |

## [◆ ](#a6c58ebc2082de8c2c3aafd9ee77dfd11)BT\_HCI\_OP\_LE\_REJECT\_CIS

| #define BT\_HCI\_OP\_LE\_REJECT\_CIS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0067) /\* 0x2067 \*/ |
| --- |

## [◆ ](#aedbb03b04ed567e54642e42ae758538a)BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_FAL

| #define BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_FAL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0012) /\* 0x2012 \*/ |
| --- |

## [◆ ](#a8545e1ede192257a4383eea6b2e932b7)BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_PER\_ADV\_LIST

| #define BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_PER\_ADV\_LIST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0048) /\* 0x2048 \*/ |
| --- |

## [◆ ](#ac4c11605a4cd244ec3ffa972295396fa)BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_RL

| #define BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_RL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0028) /\* 0x2028 \*/ |
| --- |

## [◆ ](#ae802afd7081a39f062f65e5c0994a9e4)BT\_HCI\_OP\_LE\_REMOVE\_ADV\_SET

| #define BT\_HCI\_OP\_LE\_REMOVE\_ADV\_SET   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x003c) /\* 0x203c \*/ |
| --- |

## [◆ ](#ab623f680f2031fc03bd73199ebbf4e4e)BT\_HCI\_OP\_LE\_REMOVE\_CIG

| #define BT\_HCI\_OP\_LE\_REMOVE\_CIG   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0065) /\* 0x2065 \*/ |
| --- |

## [◆ ](#addec65d76f67f07c029216435cf117c6)BT\_HCI\_OP\_LE\_REMOVE\_ISO\_PATH

| #define BT\_HCI\_OP\_LE\_REMOVE\_ISO\_PATH   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x006f) /\* 0x206f \*/ |
| --- |

## [◆ ](#a0057468b1638b07f799b62a24cd096d9)BT\_HCI\_OP\_LE\_REQ\_PEER\_SC

| #define BT\_HCI\_OP\_LE\_REQ\_PEER\_SC   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x006d) /\* 0x206d \*/ |
| --- |

## [◆ ](#abd18c6854a0dc97c451b498816f206e4)BT\_HCI\_OP\_LE\_RX\_TEST

| #define BT\_HCI\_OP\_LE\_RX\_TEST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x001d) /\* 0x201d \*/ |
| --- |

## [◆ ](#abe1567f7cf83148b3f2214b6e0787da0)BT\_HCI\_OP\_LE\_RX\_TEST\_V3

| #define BT\_HCI\_OP\_LE\_RX\_TEST\_V3   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x004f) /\* 0x204f \*/ |
| --- |

## [◆ ](#a183431c86b7eb32b7c00e6b3a000f29e)BT\_HCI\_OP\_LE\_SET\_ADDR\_RES\_ENABLE

| #define BT\_HCI\_OP\_LE\_SET\_ADDR\_RES\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x002d) /\* 0x202d \*/ |
| --- |

## [◆ ](#adb8f5236ac1b5eaa4c82d620c78c45aa)BT\_HCI\_OP\_LE\_SET\_ADV\_DATA

| #define BT\_HCI\_OP\_LE\_SET\_ADV\_DATA   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0008) /\* 0x2008 \*/ |
| --- |

## [◆ ](#a5f218883bda0698b5c52fd6a34d5e9f0)BT\_HCI\_OP\_LE\_SET\_ADV\_ENABLE

| #define BT\_HCI\_OP\_LE\_SET\_ADV\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x000a) /\* 0x200a \*/ |
| --- |

## [◆ ](#a446b6e7a74800ee657f5ddcf1c198d02)BT\_HCI\_OP\_LE\_SET\_ADV\_PARAM

| #define BT\_HCI\_OP\_LE\_SET\_ADV\_PARAM   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0006) /\* 0x2006 \*/ |
| --- |

## [◆ ](#ac96cefff0857a4d19025a2d9dec8333e)BT\_HCI\_OP\_LE\_SET\_ADV\_SET\_RANDOM\_ADDR

| #define BT\_HCI\_OP\_LE\_SET\_ADV\_SET\_RANDOM\_ADDR   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0035) /\* 0x2035 \*/ |
| --- |

## [◆ ](#a0a4b2732026a6300d4b354eb6d93905d)BT\_HCI\_OP\_LE\_SET\_CIG\_PARAMS

| #define BT\_HCI\_OP\_LE\_SET\_CIG\_PARAMS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0062) /\* 0x2062 \*/ |
| --- |

## [◆ ](#a54df2d12a0c07bab9fb3521dc69ff2f4)BT\_HCI\_OP\_LE\_SET\_CIG\_PARAMS\_TEST

| #define BT\_HCI\_OP\_LE\_SET\_CIG\_PARAMS\_TEST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0063) /\* 0x2063 \*/ |
| --- |

## [◆ ](#a728b9a505c9a2f719424bd277f7e8765)BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_SAMPLING\_ENABLE

| #define BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_SAMPLING\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0053) /\* 0x2053 \*/ |
| --- |

## [◆ ](#a5527fd8badb977f2ef061ba76468ccf3)BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_TX\_ENABLE

| #define BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_TX\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0052) /\* 0x2052 \*/ |
| --- |

## [◆ ](#a900509c6e7485b44de09a43555225ce8)BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_TX\_PARAMS

| #define BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_TX\_PARAMS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0051) /\* 0x2051 \*/ |
| --- |

## [◆ ](#a8a079c51fc7c37f29afeda663206c59e)BT\_HCI\_OP\_LE\_SET\_CONN\_CTE\_RX\_PARAMS

| #define BT\_HCI\_OP\_LE\_SET\_CONN\_CTE\_RX\_PARAMS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0054) /\* 0x2054 \*/ |
| --- |

## [◆ ](#af4110be6e09c80cd7362d9b2580243e7)BT\_HCI\_OP\_LE\_SET\_CONN\_CTE\_TX\_PARAMS

| #define BT\_HCI\_OP\_LE\_SET\_CONN\_CTE\_TX\_PARAMS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0055) /\* 0x2055 \*/ |
| --- |

## [◆ ](#a5aeb49334449851866537ea8703f5ab0)BT\_HCI\_OP\_LE\_SET\_DATA\_LEN

| #define BT\_HCI\_OP\_LE\_SET\_DATA\_LEN   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0022) /\* 0x2022 \*/ |
| --- |

## [◆ ](#aaa4e3fd27b4157a617a5fb6817bc1881)BT\_HCI\_OP\_LE\_SET\_DEFAULT\_PHY

| #define BT\_HCI\_OP\_LE\_SET\_DEFAULT\_PHY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0031) /\* 0x2031 \*/ |
| --- |

## [◆ ](#a05c5f2cb7028e3ae831047e53b767836)BT\_HCI\_OP\_LE\_SET\_DEFAULT\_SUBRATE

| #define BT\_HCI\_OP\_LE\_SET\_DEFAULT\_SUBRATE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x007D) /\* 0x207D \*/ |
| --- |

## [◆ ](#aa9a3688473bf15c8845f52a3128362f7)BT\_HCI\_OP\_LE\_SET\_EVENT\_MASK

| #define BT\_HCI\_OP\_LE\_SET\_EVENT\_MASK   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0001) /\* 0x2001 \*/ |
| --- |

## [◆ ](#a563769ae57bb58be9d7ee8e92019cb99)BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_DATA

| #define BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_DATA   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0037) /\* 0x2037 \*/ |
| --- |

## [◆ ](#a99e9573f9bd290fb18f82a327ca55ecd)BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_ENABLE

| #define BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0039) /\* 0x2039 \*/ |
| --- |

## [◆ ](#a098efdd7908adafd26b8e3f63508c476)BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_PARAM

| #define BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_PARAM   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0036) /\* 0x2036 \*/ |
| --- |

## [◆ ](#a66ffb876e588d64ce2b2d9091de94806)BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_PARAM\_V2

| #define BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_PARAM\_V2   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x007F) /\* 0x207F \*/ |
| --- |

## [◆ ](#af7a8256887657e482084d4ed3810195b)BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_ENABLE

| #define BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0042) /\* 0x2042 \*/ |
| --- |

## [◆ ](#a7b0687c9e1faae997b76ece821338fd7)BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_PARAM

| #define BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_PARAM   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0041) /\* 0x2041 \*/ |
| --- |

## [◆ ](#a586395798b3d827ab17634287862ef54)BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_RSP\_DATA

| #define BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_RSP\_DATA   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0038) /\* 0x2038 \*/ |
| --- |

## [◆ ](#a6224aab014342d93bcb16c717cd52421)BT\_HCI\_OP\_LE\_SET\_HOST\_CHAN\_CLASSIF

| #define BT\_HCI\_OP\_LE\_SET\_HOST\_CHAN\_CLASSIF   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0014) /\* 0x2014 \*/ |
| --- |

## [◆ ](#a29555bdcc7b439c2d0311fcb0721dc0b)BT\_HCI\_OP\_LE\_SET\_HOST\_FEATURE

| #define BT\_HCI\_OP\_LE\_SET\_HOST\_FEATURE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0074) /\* 0x2074 \*/ |
| --- |

## [◆ ](#a09c0d554937de38a7b74661a2820237b)BT\_HCI\_OP\_LE\_SET\_PATH\_LOSS\_REPORTING\_ENABLE

| #define BT\_HCI\_OP\_LE\_SET\_PATH\_LOSS\_REPORTING\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0079) /\* 0x2079 \*/ |
| --- |

## [◆ ](#a48a3e41f8d6598e617d02ebc609911c6)BT\_HCI\_OP\_LE\_SET\_PATH\_LOSS\_REPORTING\_PARAMETERS

| #define BT\_HCI\_OP\_LE\_SET\_PATH\_LOSS\_REPORTING\_PARAMETERS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0078) /\* 0x2078 \*/ |
| --- |

## [◆ ](#ae6611e7b72b057ac9d4004a1772fe435)BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_DATA

| #define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_DATA   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x003f) /\* 0x203f \*/ |
| --- |

## [◆ ](#a3ae23554c13b099b50b129462e08afe4)BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_ENABLE

| #define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0040) /\* 0x2040 \*/ |
| --- |

## [◆ ](#a3a111d29fd682fa825f4f9c8c358243f)BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_PARAM

| #define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_PARAM   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x003e) /\* 0x203e \*/ |
| --- |

## [◆ ](#a1125bfc15404124bf4bd533520be0f77)BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_PARAM\_V2

| #define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_PARAM\_V2   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0086) /\* 0x2086 \*/ |
| --- |

## [◆ ](#a047efb565b182e90178513dc3db6390f)BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_RECV\_ENABLE

| #define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_RECV\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0059) /\* 0x2059 \*/ |
| --- |

## [◆ ](#a2be1e66c896dca2022c04164fd94da49)BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_RESPONSE\_DATA

| #define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_RESPONSE\_DATA   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0083) /\* 0x2083 \*/ |
| --- |

## [◆ ](#a44e729aebc339ada5deb86ad9d350404)BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_SUBEVENT\_DATA

| #define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_SUBEVENT\_DATA   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0082) /\* 0x2082 \*/ |
| --- |

## [◆ ](#aea7f44f563c109be1676454412757fab)BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_SYNC\_SUBEVENT

| #define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_SYNC\_SUBEVENT   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0084) /\* 0x2084 \*/ |
| --- |

## [◆ ](#a1d21c4ffe4db8caafa374a9138e179fa)BT\_HCI\_OP\_LE\_SET\_PHY

| #define BT\_HCI\_OP\_LE\_SET\_PHY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0032) /\* 0x2032 \*/ |
| --- |

## [◆ ](#a7e1fad2d353904bb345f3a1579c98576)BT\_HCI\_OP\_LE\_SET\_PRIVACY\_MODE

| #define BT\_HCI\_OP\_LE\_SET\_PRIVACY\_MODE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x004e) /\* 0x204e \*/ |
| --- |

## [◆ ](#af34eced252d01bbc27bd8e19ed4dc80e)BT\_HCI\_OP\_LE\_SET\_RANDOM\_ADDRESS

| #define BT\_HCI\_OP\_LE\_SET\_RANDOM\_ADDRESS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0005) /\* 0x2005 \*/ |
| --- |

## [◆ ](#aeabb8438460e694867d855cf7f8e3b31)BT\_HCI\_OP\_LE\_SET\_RPA\_TIMEOUT

| #define BT\_HCI\_OP\_LE\_SET\_RPA\_TIMEOUT   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x002e) /\* 0x202e \*/ |
| --- |

## [◆ ](#a894cf6904ec16b11f6d930d72d30fce6)BT\_HCI\_OP\_LE\_SET\_SCAN\_ENABLE

| #define BT\_HCI\_OP\_LE\_SET\_SCAN\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x000c) /\* 0x200c \*/ |
| --- |

## [◆ ](#a56db98b00b57fd713f8cedbf34e2f8fa)BT\_HCI\_OP\_LE\_SET\_SCAN\_PARAM

| #define BT\_HCI\_OP\_LE\_SET\_SCAN\_PARAM   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x000b) /\* 0x200b \*/ |
| --- |

## [◆ ](#a81718bfe6796648eb5831f3cd03049c8)BT\_HCI\_OP\_LE\_SET\_SCAN\_RSP\_DATA

| #define BT\_HCI\_OP\_LE\_SET\_SCAN\_RSP\_DATA   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0009) /\* 0x2009 \*/ |
| --- |

## [◆ ](#aec22a58c052e856558b316b4f94f8561)BT\_HCI\_OP\_LE\_SET\_TX\_POWER\_REPORT\_ENABLE

| #define BT\_HCI\_OP\_LE\_SET\_TX\_POWER\_REPORT\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x007A) /\* 0x207A \*/ |
| --- |

## [◆ ](#a97de1164704f5d3c517b9c2ff6b0584a)BT\_HCI\_OP\_LE\_SETUP\_ISO\_PATH

| #define BT\_HCI\_OP\_LE\_SETUP\_ISO\_PATH   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x006e) /\* 0x206e \*/ |
| --- |

## [◆ ](#afececfce5819f1b8555ce47fbde2aa0b)BT\_HCI\_OP\_LE\_START\_ENCRYPTION

| #define BT\_HCI\_OP\_LE\_START\_ENCRYPTION   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0019) /\* 0x2019 \*/ |
| --- |

## [◆ ](#af6825cfdac02620af56b8c747d1ef308)BT\_HCI\_OP\_LE\_SUBRATE\_REQUEST

| #define BT\_HCI\_OP\_LE\_SUBRATE\_REQUEST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x007E) /\* 0x207E \*/ |
| --- |

## [◆ ](#acc5e6c17e33cf43f2a68cb93bb09ef20)BT\_HCI\_OP\_LE\_TERMINATE\_BIG

| #define BT\_HCI\_OP\_LE\_TERMINATE\_BIG   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x006a) /\* 0x206a \*/ |
| --- |

## [◆ ](#a7ff8a81ae09ddb0d18f999fe454e41df)BT\_HCI\_OP\_LE\_TEST\_END

| #define BT\_HCI\_OP\_LE\_TEST\_END   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x001f) /\* 0x201f \*/ |
| --- |

## [◆ ](#af5fe87cbe280dcf26ddc21952e84e93e)BT\_HCI\_OP\_LE\_TX\_TEST

| #define BT\_HCI\_OP\_LE\_TX\_TEST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x001e) /\* 0x201e \*/ |
| --- |

## [◆ ](#ad570a3edcefcf927e5253805e1d3d4e4)BT\_HCI\_OP\_LE\_TX\_TEST\_V3

| #define BT\_HCI\_OP\_LE\_TX\_TEST\_V3   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0050) /\* 0x2050 \*/ |
| --- |

## [◆ ](#a13827b7d7b656ea02c0620ec7b525f65)BT\_HCI\_OP\_LE\_TX\_TEST\_V4

| #define BT\_HCI\_OP\_LE\_TX\_TEST\_V4   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x007B) /\* 0x207B \*/ |
| --- |

## [◆ ](#ae344c1ab9af250787b9ed8109ad3cde0)BT\_HCI\_OP\_LE\_WRITE\_DEFAULT\_DATA\_LEN

| #define BT\_HCI\_OP\_LE\_WRITE\_DEFAULT\_DATA\_LEN   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x0024) /\* 0x2024 \*/ |
| --- |

## [◆ ](#a2afc45fe32acff87265d36865c8d0b17)BT\_HCI\_OP\_LE\_WRITE\_LE\_HOST\_SUPP

| #define BT\_HCI\_OP\_LE\_WRITE\_LE\_HOST\_SUPP   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x006d) /\* 0x0c6d \*/ |
| --- |

## [◆ ](#a766b66d1fc7df1d8924d060217de9b9b)BT\_HCI\_OP\_LE\_WRITE\_RF\_PATH\_COMP

| #define BT\_HCI\_OP\_LE\_WRITE\_RF\_PATH\_COMP   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LE](#abb09db6a211185842f039eddb9fadca5), 0x004d) /\* 0x204d \*/ |
| --- |

## [◆ ](#a7db25bd8bdbd4351e0dcef1df8dc7077)BT\_HCI\_OP\_LINK\_KEY\_NEG\_REPLY

| #define BT\_HCI\_OP\_LINK\_KEY\_NEG\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x000c) /\* 0x040c \*/ |
| --- |

## [◆ ](#a7da489e05d679c00f6cbbca0dfaaf136)BT\_HCI\_OP\_LINK\_KEY\_REPLY

| #define BT\_HCI\_OP\_LINK\_KEY\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x000b) /\* 0x040b \*/ |
| --- |

## [◆ ](#a5833de4cefd59cee9c614163de7e927b)BT\_HCI\_OP\_PIN\_CODE\_NEG\_REPLY

| #define BT\_HCI\_OP\_PIN\_CODE\_NEG\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x000e) /\* 0x040e \*/ |
| --- |

## [◆ ](#a7713e5641070ac7fca91e027fc9b8c40)BT\_HCI\_OP\_PIN\_CODE\_REPLY

| #define BT\_HCI\_OP\_PIN\_CODE\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x000d) /\* 0x040d \*/ |
| --- |

## [◆ ](#a0ea6134bcd33e24b068f35d080cdc4e0)BT\_HCI\_OP\_READ\_AUTH\_PAYLOAD\_TIMEOUT

| #define BT\_HCI\_OP\_READ\_AUTH\_PAYLOAD\_TIMEOUT   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x007b) /\* 0x0c7b \*/ |
| --- |

## [◆ ](#a4ba1bf2078ac12686e2a7727f637f70b)BT\_HCI\_OP\_READ\_BD\_ADDR

| #define BT\_HCI\_OP\_READ\_BD\_ADDR   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x0009) /\* 0x1009 \*/ |
| --- |

## [◆ ](#acd5d9ecda744969d4692e6ebface2e53)BT\_HCI\_OP\_READ\_BUFFER\_SIZE

| #define BT\_HCI\_OP\_READ\_BUFFER\_SIZE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x0005) /\* 0x1005 \*/ |
| --- |

## [◆ ](#a4b9e24d16cd92ce6ee1d6444410cfb43)BT\_HCI\_OP\_READ\_CODEC\_CAPABILITIES

| #define BT\_HCI\_OP\_READ\_CODEC\_CAPABILITIES   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x000e) /\* 0x100e \*/ |
| --- |

## [◆ ](#a8755487f4672f196051cc513894e4603)BT\_HCI\_OP\_READ\_CODECS

| #define BT\_HCI\_OP\_READ\_CODECS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x000b) /\* 0x100b \*/ |
| --- |

## [◆ ](#acb09b1a94453c1c341decabc029bbc04)BT\_HCI\_OP\_READ\_CODECS\_V2

| #define BT\_HCI\_OP\_READ\_CODECS\_V2   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x000d) /\* 0x100d \*/ |
| --- |

## [◆ ](#af302a5e40644307f522154f3803572d0)BT\_HCI\_OP\_READ\_CONN\_ACCEPT\_TIMEOUT

| #define BT\_HCI\_OP\_READ\_CONN\_ACCEPT\_TIMEOUT   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0015) /\* 0x0c15 \*/ |
| --- |

## [◆ ](#a9a183b26d18453d5daa6de2dcbe4d9a1)BT\_HCI\_OP\_READ\_CTLR\_DELAY

| #define BT\_HCI\_OP\_READ\_CTLR\_DELAY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x000f) /\* 0x100f \*/ |
| --- |

## [◆ ](#adefeb2117010fa2d53937ce513e28a18)BT\_HCI\_OP\_READ\_ENCRYPTION\_KEY\_SIZE

| #define BT\_HCI\_OP\_READ\_ENCRYPTION\_KEY\_SIZE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_STATUS](#a5ce14b9103bd538f3610afd80284157e), 0x0008) /\* 0x1408 \*/ |
| --- |

## [◆ ](#a882f120b35a9baa2f70bc33ef5ced6d3)BT\_HCI\_OP\_READ\_LOCAL\_EXT\_FEATURES

| #define BT\_HCI\_OP\_READ\_LOCAL\_EXT\_FEATURES   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x0004) /\* 0x1004 \*/ |
| --- |

## [◆ ](#a8524505dff48ceb41c008c8662da6408)BT\_HCI\_OP\_READ\_LOCAL\_FEATURES

| #define BT\_HCI\_OP\_READ\_LOCAL\_FEATURES   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x0003) /\* 0x1003 \*/ |
| --- |

## [◆ ](#a195b8faf6d7d3e4f1b528185c73b4d67)BT\_HCI\_OP\_READ\_LOCAL\_VERSION\_INFO

| #define BT\_HCI\_OP\_READ\_LOCAL\_VERSION\_INFO   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x0001) /\* 0x1001 \*/ |
| --- |

## [◆ ](#a87f6747b2b5d52a7886a1ec72100d9d0)BT\_HCI\_OP\_READ\_REMOTE\_EXT\_FEATURES

| #define BT\_HCI\_OP\_READ\_REMOTE\_EXT\_FEATURES   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x001c) /\* 0x041c \*/ |
| --- |

## [◆ ](#ab6282249d4c14412674083007346b005)BT\_HCI\_OP\_READ\_REMOTE\_FEATURES

| #define BT\_HCI\_OP\_READ\_REMOTE\_FEATURES   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x001b) /\* 0x041b \*/ |
| --- |

## [◆ ](#ae723b797305fe7a370b94d8c865e5708)BT\_HCI\_OP\_READ\_REMOTE\_VERSION\_INFO

| #define BT\_HCI\_OP\_READ\_REMOTE\_VERSION\_INFO   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x001d) /\* 0x041d \*/ |
| --- |

## [◆ ](#a528902591490d9d20a6966a042254b3a)BT\_HCI\_OP\_READ\_RSSI

| #define BT\_HCI\_OP\_READ\_RSSI   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_STATUS](#a5ce14b9103bd538f3610afd80284157e), 0x0005) /\* 0x1405 \*/ |
| --- |

## [◆ ](#ac0d7533d221db0fa44cfb83135dfcc6a)BT\_HCI\_OP\_READ\_SUPPORTED\_COMMANDS

| #define BT\_HCI\_OP\_READ\_SUPPORTED\_COMMANDS   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e), 0x0002) /\* 0x1002 \*/ |
| --- |

## [◆ ](#aaac00b7d9f9f96d1438643ee054ab21a)BT\_HCI\_OP\_READ\_TX\_POWER\_LEVEL

| #define BT\_HCI\_OP\_READ\_TX\_POWER\_LEVEL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x002d) /\* 0x0c2d \*/ |
| --- |

## [◆ ](#aabb1f800ad4574e0350007af94cd786d)BT\_HCI\_OP\_REJECT\_CONN\_REQ

| #define BT\_HCI\_OP\_REJECT\_CONN\_REQ   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x000a) /\* 0x040a \*/ |
| --- |

## [◆ ](#a76f79f4e14396297cc5db4ca8dba0c4c)BT\_HCI\_OP\_REMOTE\_NAME\_CANCEL

| #define BT\_HCI\_OP\_REMOTE\_NAME\_CANCEL   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x001a) /\* 0x041a \*/ |
| --- |

## [◆ ](#a2e759212d10ecd3a2e975379bf18d374)BT\_HCI\_OP\_REMOTE\_NAME\_REQUEST

| #define BT\_HCI\_OP\_REMOTE\_NAME\_REQUEST   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0019) /\* 0x0419 \*/ |
| --- |

## [◆ ](#abb515eb4ea9e66503bf1f375af01a6c0)BT\_HCI\_OP\_RESET

| #define BT\_HCI\_OP\_RESET   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0003) /\* 0x0c03 \*/ |
| --- |

## [◆ ](#ac32c04cf6bc9de299f0a307dbeed63f3)BT\_HCI\_OP\_SET\_CONN\_ENCRYPT

| #define BT\_HCI\_OP\_SET\_CONN\_ENCRYPT   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0013) /\* 0x0413 \*/ |
| --- |

## [◆ ](#abe87fa64cb529d2cfe7ddf4fa045d3b5)BT\_HCI\_OP\_SET\_CTL\_TO\_HOST\_FLOW

| #define BT\_HCI\_OP\_SET\_CTL\_TO\_HOST\_FLOW   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0031) /\* 0x0c31 \*/ |
| --- |

## [◆ ](#abb9bf6d936310a43c4a88244ad12640d)BT\_HCI\_OP\_SET\_EVENT\_MASK

| #define BT\_HCI\_OP\_SET\_EVENT\_MASK   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0001) /\* 0x0c01 \*/ |
| --- |

## [◆ ](#af5d2954950e00dfd5a69fc19db0fe530)BT\_HCI\_OP\_SET\_EVENT\_MASK\_PAGE\_2

| #define BT\_HCI\_OP\_SET\_EVENT\_MASK\_PAGE\_2   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0063) /\* 0x0c63 \*/ |
| --- |

## [◆ ](#ac4e12b8f7b89a658da7bbbaf371358e0)BT\_HCI\_OP\_SETUP\_SYNC\_CONN

| #define BT\_HCI\_OP\_SETUP\_SYNC\_CONN   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x0028) /\* 0x0428 \*/ |
| --- |

## [◆ ](#aecc09326c190d2ab7b89f99375cd39bd)BT\_HCI\_OP\_USER\_CONFIRM\_NEG\_REPLY

| #define BT\_HCI\_OP\_USER\_CONFIRM\_NEG\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x002d) /\* 0x042d \*/ |
| --- |

## [◆ ](#ab688441778a4239e1e8f2b2e0b74004f)BT\_HCI\_OP\_USER\_CONFIRM\_REPLY

| #define BT\_HCI\_OP\_USER\_CONFIRM\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x002c) /\* 0x042c \*/ |
| --- |

## [◆ ](#a96f9c5c3439d829dfac94cca9ad1f015)BT\_HCI\_OP\_USER\_PASSKEY\_NEG\_REPLY

| #define BT\_HCI\_OP\_USER\_PASSKEY\_NEG\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x002f) /\* 0x042f \*/ |
| --- |

## [◆ ](#ad1fce315b731f9978cd52a8c23994a10)BT\_HCI\_OP\_USER\_PASSKEY\_REPLY

| #define BT\_HCI\_OP\_USER\_PASSKEY\_REPLY   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_LINK\_CTRL](#abb6c50fe170ffaaaf4a0827058331381), 0x002e) /\* 0x042e \*/ |
| --- |

## [◆ ](#ae74450b7b643f947fa2e83a80e0e2fae)BT\_HCI\_OP\_WRITE\_AUTH\_PAYLOAD\_TIMEOUT

| #define BT\_HCI\_OP\_WRITE\_AUTH\_PAYLOAD\_TIMEOUT   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x007c) /\* 0x0c7c \*/ |
| --- |

## [◆ ](#ace988e19fa62bf61654a329acaf99018)BT\_HCI\_OP\_WRITE\_CLASS\_OF\_DEVICE

| #define BT\_HCI\_OP\_WRITE\_CLASS\_OF\_DEVICE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0024) /\* 0x0c24 \*/ |
| --- |

## [◆ ](#a6799bd267ef7c19b05ed2dd57baf0393)BT\_HCI\_OP\_WRITE\_CONN\_ACCEPT\_TIMEOUT

| #define BT\_HCI\_OP\_WRITE\_CONN\_ACCEPT\_TIMEOUT   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0016) /\* 0x0c16 \*/ |
| --- |

## [◆ ](#a04985a29d0f131c09aeb9769689b727b)BT\_HCI\_OP\_WRITE\_INQUIRY\_MODE

| #define BT\_HCI\_OP\_WRITE\_INQUIRY\_MODE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0045) /\* 0x0c45 \*/ |
| --- |

## [◆ ](#a9b328487dbeeaa587e6f75011441f340)BT\_HCI\_OP\_WRITE\_LOCAL\_NAME

| #define BT\_HCI\_OP\_WRITE\_LOCAL\_NAME   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0013) /\* 0x0c13 \*/ |
| --- |

## [◆ ](#a5ef44fe1cca74a2258ffab1edd04acdf)BT\_HCI\_OP\_WRITE\_PAGE\_TIMEOUT

| #define BT\_HCI\_OP\_WRITE\_PAGE\_TIMEOUT   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0018) /\* 0x0c18 \*/ |
| --- |

## [◆ ](#a0480dd89b0f851d0a791b97138b01a5b)BT\_HCI\_OP\_WRITE\_SC\_HOST\_SUPP

| #define BT\_HCI\_OP\_WRITE\_SC\_HOST\_SUPP   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x007a) /\* 0x0c7a \*/ |
| --- |

## [◆ ](#a0c8b9dc68ec6cd91ec0e9e565701a887)BT\_HCI\_OP\_WRITE\_SCAN\_ENABLE

| #define BT\_HCI\_OP\_WRITE\_SCAN\_ENABLE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x001a) /\* 0x0c1a \*/ |
| --- |

## [◆ ](#ac7a73c5e38a2308d56f0dbaaf0a4795b)BT\_HCI\_OP\_WRITE\_SSP\_MODE

| #define BT\_HCI\_OP\_WRITE\_SSP\_MODE   [BT\_OP](#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4), 0x0056) /\* 0x0c56 \*/ |
| --- |

## [◆ ](#a1109fda761e1ef8c6df935cf97fdc646)BT\_HCI\_OWN\_ADDR\_PUBLIC

| #define BT\_HCI\_OWN\_ADDR\_PUBLIC   0x00 |
| --- |

## [◆ ](#a8693ea59b948960e627d62785515996e)BT\_HCI\_OWN\_ADDR\_RANDOM

| #define BT\_HCI\_OWN\_ADDR\_RANDOM   0x01 |
| --- |

## [◆ ](#a115907057c92a59a407d261133946b59)BT\_HCI\_OWN\_ADDR\_RPA\_MASK

| #define BT\_HCI\_OWN\_ADDR\_RPA\_MASK   0x02 |
| --- |

## [◆ ](#a92a5db1ce46bbf3ddeaab4da76bc6685)BT\_HCI\_OWN\_ADDR\_RPA\_OR\_PUBLIC

| #define BT\_HCI\_OWN\_ADDR\_RPA\_OR\_PUBLIC   0x02 |
| --- |

## [◆ ](#aec05e679e29fde812e9a066e672405b4)BT\_HCI\_OWN\_ADDR\_RPA\_OR\_RANDOM

| #define BT\_HCI\_OWN\_ADDR\_RPA\_OR\_RANDOM   0x03 |
| --- |

## [◆ ](#a98554ced76600577254b4124b27ef8a8)BT\_HCI\_PAWR\_SUBEVENT\_MAX

| #define BT\_HCI\_PAWR\_SUBEVENT\_MAX   128 |
| --- |

## [◆ ](#a1e6d78149d0990511b2b6dffb617069e)BT\_HCI\_PEER\_ADDR\_ANONYMOUS

| #define BT\_HCI\_PEER\_ADDR\_ANONYMOUS   0xff |
| --- |

## [◆ ](#aebc5bd975899f765afe697ab322db114)BT\_HCI\_PEER\_ADDR\_RPA\_UNRESOLVED

| #define BT\_HCI\_PEER\_ADDR\_RPA\_UNRESOLVED   0xfe |
| --- |

## [◆ ](#a0a41f911f5f4b50b571c7f091393c7d8)BT\_HCI\_REQUEST\_CTE\_INTERVAL\_MAX

| #define BT\_HCI\_REQUEST\_CTE\_INTERVAL\_MAX   0xFFFF |
| --- |

## [◆ ](#a13875ad8ac3a77759afdb4b6a76ad3e8)BT\_HCI\_REQUEST\_CTE\_INTERVAL\_MIN

| #define BT\_HCI\_REQUEST\_CTE\_INTERVAL\_MIN   0x1 |
| --- |

## [◆ ](#ad9e1fa26a799b8730c17772482da7982)BT\_HCI\_REQUEST\_CTE\_ONCE

| #define BT\_HCI\_REQUEST\_CTE\_ONCE   0x0 |
| --- |

## [◆ ](#a150ea8f2095d8510bde3ebd65d521c29)BT\_HCI\_ROLE\_CENTRAL

| #define BT\_HCI\_ROLE\_CENTRAL   0x00 |
| --- |

## [◆ ](#a9ca37afd4638ef94cdd55302bd4c99b3)BT\_HCI\_ROLE\_PERIPHERAL

| #define BT\_HCI\_ROLE\_PERIPHERAL   0x01 |
| --- |

## [◆ ](#a5e79467b20a9173726c6be86b091e596)BT\_HCI\_SCO

| #define BT\_HCI\_SCO   0x00 |
| --- |

## [◆ ](#acb8daef29a7f5f2d11a169fd10ae0caa)BT\_HCI\_SCO\_HDR\_SIZE

| #define BT\_HCI\_SCO\_HDR\_SIZE   3 |
| --- |

## [◆ ](#a4e4a6e6bb2dc713de8cb7c12139583ed)BT\_HCI\_SYNC\_HANDLE\_INVALID

| #define BT\_HCI\_SYNC\_HANDLE\_INVALID   0xffff |
| --- |

## [◆ ](#a1fe8c26f174833a4dccbe192df2c6f7d)BT\_HCI\_TEST\_PKT\_PAYLOAD\_00000000

| #define BT\_HCI\_TEST\_PKT\_PAYLOAD\_00000000   0x05 |
| --- |

## [◆ ](#a13baca9e4517522c763c25882177a2a7)BT\_HCI\_TEST\_PKT\_PAYLOAD\_00001111

| #define BT\_HCI\_TEST\_PKT\_PAYLOAD\_00001111   0x06 |
| --- |

## [◆ ](#a8f660f979b14d91abd9423e718921ebb)BT\_HCI\_TEST\_PKT\_PAYLOAD\_01010101

| #define BT\_HCI\_TEST\_PKT\_PAYLOAD\_01010101   0x07 |
| --- |

## [◆ ](#aab044752b89bb4493a509580ae8eaf9b)BT\_HCI\_TEST\_PKT\_PAYLOAD\_10101010

| #define BT\_HCI\_TEST\_PKT\_PAYLOAD\_10101010   0x02 |
| --- |

## [◆ ](#a51d26730c8f4c3c8491b33483bdb9494)BT\_HCI\_TEST\_PKT\_PAYLOAD\_11110000

| #define BT\_HCI\_TEST\_PKT\_PAYLOAD\_11110000   0x01 |
| --- |

## [◆ ](#a5008205909cecc994b74c8a1cb1f92af)BT\_HCI\_TEST\_PKT\_PAYLOAD\_11111111

| #define BT\_HCI\_TEST\_PKT\_PAYLOAD\_11111111   0x04 |
| --- |

## [◆ ](#a0eb4fcbb3ab6c7d4e2ed87d61c5b30f1)BT\_HCI\_TEST\_PKT\_PAYLOAD\_PRBS15

| #define BT\_HCI\_TEST\_PKT\_PAYLOAD\_PRBS15   0x03 |
| --- |

## [◆ ](#aa9ce0f2db7b63303a9c61c37d052d7b7)BT\_HCI\_TEST\_PKT\_PAYLOAD\_PRBS9

| #define BT\_HCI\_TEST\_PKT\_PAYLOAD\_PRBS9   0x00 |
| --- |

## [◆ ](#a925dda1fdce843e0bbcdd4acff696440)BT\_HCI\_TX\_TEST\_POWER\_MAX

| #define BT\_HCI\_TX\_TEST\_POWER\_MAX   0x14 |
| --- |

## [◆ ](#a2e9caac5d12f8df1ce69a54f603500ee)BT\_HCI\_TX\_TEST\_POWER\_MAX\_SET

| #define BT\_HCI\_TX\_TEST\_POWER\_MAX\_SET   0x7F |
| --- |

## [◆ ](#a034d4a4fd8f7d6d324efa820d0b627d1)BT\_HCI\_TX\_TEST\_POWER\_MIN

| #define BT\_HCI\_TX\_TEST\_POWER\_MIN   -0x7F |
| --- |

## [◆ ](#a5d0fc1dbb127ba0a383e4e56bb503334)BT\_HCI\_TX\_TEST\_POWER\_MIN\_SET

| #define BT\_HCI\_TX\_TEST\_POWER\_MIN\_SET   0x7E |
| --- |

## [◆ ](#a4947ee8a84f7cd81e242ee812b5b8760)BT\_HCI\_VERSION\_1\_0B

| #define BT\_HCI\_VERSION\_1\_0B   0 |
| --- |

## [◆ ](#a0fac5f104d8ab1539e84a900aafa9e43)BT\_HCI\_VERSION\_1\_1

| #define BT\_HCI\_VERSION\_1\_1   1 |
| --- |

## [◆ ](#afe6fd8249a97d3762fe454bfb7eab021)BT\_HCI\_VERSION\_1\_2

| #define BT\_HCI\_VERSION\_1\_2   2 |
| --- |

## [◆ ](#afc0d24e2ba5e6b992aec81104cbf035e)BT\_HCI\_VERSION\_2\_0

| #define BT\_HCI\_VERSION\_2\_0   3 |
| --- |

## [◆ ](#a98d73e8f548d5ae7eddff91a3e647aae)BT\_HCI\_VERSION\_2\_1

| #define BT\_HCI\_VERSION\_2\_1   4 |
| --- |

## [◆ ](#acaf91cc6895552243c5b85c2fc007db5)BT\_HCI\_VERSION\_3\_0

| #define BT\_HCI\_VERSION\_3\_0   5 |
| --- |

## [◆ ](#aeb77e725323c3f31c90482e676dad08a)BT\_HCI\_VERSION\_4\_0

| #define BT\_HCI\_VERSION\_4\_0   6 |
| --- |

## [◆ ](#a08cca779ede398a551359efccdaf3090)BT\_HCI\_VERSION\_4\_1

| #define BT\_HCI\_VERSION\_4\_1   7 |
| --- |

## [◆ ](#aa398d6e6fcca0b427a2ccd3a0a343835)BT\_HCI\_VERSION\_4\_2

| #define BT\_HCI\_VERSION\_4\_2   8 |
| --- |

## [◆ ](#a9a203a5a633d28c644b30125d437701a)BT\_HCI\_VERSION\_5\_0

| #define BT\_HCI\_VERSION\_5\_0   9 |
| --- |

## [◆ ](#acfa0dbddfde8ee82b114dd34ff75c5bc)BT\_HCI\_VERSION\_5\_1

| #define BT\_HCI\_VERSION\_5\_1   10 |
| --- |

## [◆ ](#aa4828a916c53d97de0541992d0359c09)BT\_HCI\_VERSION\_5\_2

| #define BT\_HCI\_VERSION\_5\_2   11 |
| --- |

## [◆ ](#a37b04f40e68e821a1aac3b785903b379)BT\_HCI\_VERSION\_5\_3

| #define BT\_HCI\_VERSION\_5\_3   12 |
| --- |

## [◆ ](#ae8eadab2b7be415160f145bd63bae367)BT\_HCI\_VERSION\_5\_4

| #define BT\_HCI\_VERSION\_5\_4   13 |
| --- |

## [◆ ](#a66f6fbbc23991a16aa8bcfa2998f025f)BT\_HCI\_VERSION\_6\_0

| #define BT\_HCI\_VERSION\_6\_0   14 |
| --- |

## [◆ ](#ac656a702e4193044a59cac517099e2cf)BT\_IO\_DISPLAY\_ONLY

| #define BT\_IO\_DISPLAY\_ONLY   0x00 |
| --- |

## [◆ ](#a701d4fa8a4ebc07647f70264ad36153e)BT\_IO\_DISPLAY\_YESNO

| #define BT\_IO\_DISPLAY\_YESNO   0x01 |
| --- |

## [◆ ](#a5a2a51ccedf3041c42ecdbd69e8c4a68)BT\_IO\_KEYBOARD\_ONLY

| #define BT\_IO\_KEYBOARD\_ONLY   0x02 |
| --- |

## [◆ ](#ad68c0057160d5dacae12fce949fdaa32)BT\_IO\_NO\_INPUT\_OUTPUT

| #define BT\_IO\_NO\_INPUT\_OUTPUT   0x03 |
| --- |

## [◆ ](#a06c43e91abee990343ece9c22f5a515e)BT\_ISO\_CONT

| #define BT\_ISO\_CONT   0x01 |
| --- |

## [◆ ](#a7149213544fe2ac9e7d3d0fd64ecb271)BT\_ISO\_DATA\_INVALID

| #define BT\_ISO\_DATA\_INVALID   0x01 |
| --- |

## [◆ ](#ae736b21ff7b99c4bb85df1a3f4bee9cd)BT\_ISO\_DATA\_NOP

| #define BT\_ISO\_DATA\_NOP   0x02 |
| --- |

## [◆ ](#a52091a307cca85d8d39fbfe5be6b6179)BT\_ISO\_DATA\_VALID

| #define BT\_ISO\_DATA\_VALID   0x00 |
| --- |

## [◆ ](#ac2da3db69ba73112fff5bf16ef386cb3)BT\_ISO\_END

| #define BT\_ISO\_END   0x03 |
| --- |

## [◆ ](#a54e2f7efc0f22287d65bdd560dd7ec78)bt\_iso\_flags

| #define bt\_iso\_flags | ( |  | *h* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((h) >> 12)

## [◆ ](#a7ea328491745f1bde6e2b376c19cc380)bt\_iso\_flags\_pb

| #define bt\_iso\_flags\_pb | ( |  | *f* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((f) & 0x0003)

## [◆ ](#aed6d45daf19ce7fadc1c8fbcc79c9e8a)bt\_iso\_flags\_ts

| #define bt\_iso\_flags\_ts | ( |  | *f* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((f) >> 2) & 0x0001)

## [◆ ](#adcdb9dd367b64a820a040724c1c42c15)bt\_iso\_handle

| #define bt\_iso\_handle | ( |  | *h* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((h) & 0x0fff)

## [◆ ](#ab96b2d1b49a86ee96b2254b624b2e93f)bt\_iso\_handle\_pack

| #define bt\_iso\_handle\_pack | ( |  | *h*, |
| --- | --- | --- | --- |
|  |  |  | *pb*, |
|  |  |  | *ts* ) |

**Value:**

((h) | ([bt\_iso\_pack\_flags](#a9bdbdc6e181731a58ec91d53cdade532)(pb, ts) << 12))

[bt\_iso\_pack\_flags](#a9bdbdc6e181731a58ec91d53cdade532)

#define bt\_iso\_pack\_flags(pb, ts)

**Definition** hci\_types.h:98

## [◆ ](#a128d269790ccf3f8dcdeb51f80697ba0)bt\_iso\_hdr\_len

| #define bt\_iso\_hdr\_len | ( |  | *h* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((h) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(14))

## [◆ ](#a9bdbdc6e181731a58ec91d53cdade532)bt\_iso\_pack\_flags

| #define bt\_iso\_pack\_flags | ( |  | *pb*, |
| --- | --- | --- | --- |
|  |  |  | *ts* ) |

**Value:**

(((pb) & 0x0003) | (((ts) & 0x0001) << 2))

## [◆ ](#a6dbade5730a92ea7f85017792939e941)bt\_iso\_pkt\_flags

| #define bt\_iso\_pkt\_flags | ( |  | *h* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((h) >> 14)

## [◆ ](#a0d540918a423992f5f244febcc82248a)bt\_iso\_pkt\_len

| #define bt\_iso\_pkt\_len | ( |  | *h* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((h) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(12))

## [◆ ](#a3683be1ceedbcb97f61483b6fa4344e6)bt\_iso\_pkt\_len\_pack

| #define bt\_iso\_pkt\_len\_pack | ( |  | *h*, |
| --- | --- | --- | --- |
|  |  |  | *f* ) |

**Value:**

(((h) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(12)) | ((f) << 14))

## [◆ ](#a1db9801de1c97b2d15cf9d2f0ec2a5f0)BT\_ISO\_SINGLE

| #define BT\_ISO\_SINGLE   0x02 |
| --- |

## [◆ ](#a9ef86241b4dfb462ec31c855bce4ee28)BT\_ISO\_START

| #define BT\_ISO\_START   0x00 |
| --- |

## [◆ ](#af96bfa8c912e66233f64b7cc1844b82e)BT\_LE\_ADV\_CHAN\_MAP\_ALL

| #define BT\_LE\_ADV\_CHAN\_MAP\_ALL   0x07 |
| --- |

## [◆ ](#af9652f7d96b61e7cc9f44f3d923bd962)BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_37

| #define BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_37   0x01 |
| --- |

## [◆ ](#a07c18344ec56b22c8a3e902bc53ba191)BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_38

| #define BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_38   0x02 |
| --- |

## [◆ ](#a14be9af8f16dcdf70aebf251bcfb52f3)BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_39

| #define BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_39   0x04 |
| --- |

## [◆ ](#a980ff7f9bf7154c7866b5e302a1f2a55)BT\_LE\_ADV\_FP\_FILTER\_BOTH

| #define BT\_LE\_ADV\_FP\_FILTER\_BOTH   0x03 |
| --- |

## [◆ ](#a5f3d27b78705afc3abff35e353eee9fa)BT\_LE\_ADV\_FP\_FILTER\_CONN\_IND

| #define BT\_LE\_ADV\_FP\_FILTER\_CONN\_IND   0x02 |
| --- |

## [◆ ](#aba027e2aeacea1040c3b45ccaeb23d3c)BT\_LE\_ADV\_FP\_FILTER\_SCAN\_REQ

| #define BT\_LE\_ADV\_FP\_FILTER\_SCAN\_REQ   0x01 |
| --- |

## [◆ ](#abc1615c8d22ab64844c3f3394023c1b4)BT\_LE\_ADV\_FP\_NO\_FILTER

| #define BT\_LE\_ADV\_FP\_NO\_FILTER   0x00 |
| --- |

## [◆ ](#a607201e55561cdccf34e18ceac0f23b7)BT\_LE\_ADV\_INTERVAL\_DEFAULT

| #define BT\_LE\_ADV\_INTERVAL\_DEFAULT   0x0800 |
| --- |

## [◆ ](#a6479fb2c964155cfcdd3cc48c3a45618)BT\_LE\_ADV\_INTERVAL\_MAX

| #define BT\_LE\_ADV\_INTERVAL\_MAX   0x4000 |
| --- |

## [◆ ](#ac89392b0484164812b77360d15d9984b)BT\_LE\_ADV\_INTERVAL\_MIN

| #define BT\_LE\_ADV\_INTERVAL\_MIN   0x0020 |
| --- |

## [◆ ](#a4d920d42e8042c9117f97e334f889f51)BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL

| #define BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL   40 |
| --- |

## [◆ ](#ad711e7491883e1f1e068fe167cca8a4e)BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL\_HOST

| #define BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL\_HOST   41 |
| --- |

## [◆ ](#a480fc67a1c8a2f36410f285ef0ee36e7)BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_RX\_AOA

| #define BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_RX\_AOA   22 |
| --- |

## [◆ ](#a41eae1585972ae6792eb1a639c2e3a8e)BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_TX\_AOD

| #define BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_TX\_AOD   21 |
| --- |

## [◆ ](#a9120867d6f31465cb5f085b610d5ed70)BT\_LE\_FEAT\_BIT\_CHAN\_SEL\_ALGO\_2

| #define BT\_LE\_FEAT\_BIT\_CHAN\_SEL\_ALGO\_2   14 |
| --- |

## [◆ ](#af2a4be520b4d8c3eb56231b865738e90)BT\_LE\_FEAT\_BIT\_CHANNEL\_CLASSIFICATION

| #define BT\_LE\_FEAT\_BIT\_CHANNEL\_CLASSIFICATION   39 |
| --- |

## [◆ ](#ab918084874aace22954aa748333baf6d)BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING

| #define BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING   46 |
| --- |

## [◆ ](#aa4572a11d78651ce775a010178c6dfa2)BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING\_HOST

| #define BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING\_HOST   47 |
| --- |

## [◆ ](#aa98eed376b6d5263621f14c55d776088)BT\_LE\_FEAT\_BIT\_CIS\_CENTRAL

| #define BT\_LE\_FEAT\_BIT\_CIS\_CENTRAL   28 |
| --- |

## [◆ ](#a298fde96c2d6376e3333a99f7e03409d)BT\_LE\_FEAT\_BIT\_CIS\_PERIPHERAL

| #define BT\_LE\_FEAT\_BIT\_CIS\_PERIPHERAL   29 |
| --- |

## [◆ ](#aed34742e8554b830c3b6c4bf04f0e2db)BT\_LE\_FEAT\_BIT\_CONN\_CTE\_REQ

| #define BT\_LE\_FEAT\_BIT\_CONN\_CTE\_REQ   17 |
| --- |

## [◆ ](#aa5279a2ce26decb5856a6b709d0641c9)BT\_LE\_FEAT\_BIT\_CONN\_CTE\_RESP

| #define BT\_LE\_FEAT\_BIT\_CONN\_CTE\_RESP   18 |
| --- |

## [◆ ](#ab816048bdd6c1e42b0e458abebb76572)BT\_LE\_FEAT\_BIT\_CONN\_PARAM\_REQ

| #define BT\_LE\_FEAT\_BIT\_CONN\_PARAM\_REQ   1 |
| --- |

## [◆ ](#aa45b06a49232372891ceb5e4496d46da)BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING

| #define BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING   37 |
| --- |

## [◆ ](#adb884a30bc1a24e3dfb115cef7149c81)BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING\_HOST\_SUPP

| #define BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING\_HOST\_SUPP   38 |
| --- |

## [◆ ](#a6abf01c846a5d637ca98997f6cfc263d)BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_RX

| #define BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_RX   20 |
| --- |

## [◆ ](#a331e7697a3fdc073abba5dd0ff47346b)BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_TX

| #define BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_TX   19 |
| --- |

## [◆ ](#ac09127210b281e5ee45fbc134df64aa6)BT\_LE\_FEAT\_BIT\_DLE

| #define BT\_LE\_FEAT\_BIT\_DLE   5 |
| --- |

## [◆ ](#abd616dd5af5ed3742be9bae400ded848)BT\_LE\_FEAT\_BIT\_ENC

| #define BT\_LE\_FEAT\_BIT\_ENC   0 |
| --- |

## [◆ ](#ae1a0751e7c380117c4e31741712096a4)BT\_LE\_FEAT\_BIT\_EXT\_ADV

| #define BT\_LE\_FEAT\_BIT\_EXT\_ADV   12 |
| --- |

## [◆ ](#ae5644021aff31996c09f6edf3ede197c)BT\_LE\_FEAT\_BIT\_EXT\_REJ\_IND

| #define BT\_LE\_FEAT\_BIT\_EXT\_REJ\_IND   2 |
| --- |

## [◆ ](#a8f1fa8948f79bec50373e0342ab0969a)BT\_LE\_FEAT\_BIT\_EXT\_SCAN

| #define BT\_LE\_FEAT\_BIT\_EXT\_SCAN   7 |
| --- |

## [◆ ](#af08a1ffd734d1c211f38d90b4fe72417)BT\_LE\_FEAT\_BIT\_ISO\_BROADCASTER

| #define BT\_LE\_FEAT\_BIT\_ISO\_BROADCASTER   30 |
| --- |

## [◆ ](#a0d80ccb33d263abd3b42de1b69cfeeeb)BT\_LE\_FEAT\_BIT\_ISO\_CHANNELS

| #define BT\_LE\_FEAT\_BIT\_ISO\_CHANNELS   32 |
| --- |

## [◆ ](#ac8cf36c670ae359ec24e62efb4505758)BT\_LE\_FEAT\_BIT\_MIN\_USED\_CHAN\_PROC

| #define BT\_LE\_FEAT\_BIT\_MIN\_USED\_CHAN\_PROC   16 |
| --- |

## [◆ ](#a28a862eaf11f8b45237f3b87e4bb15c7)BT\_LE\_FEAT\_BIT\_PAST\_RECV

| #define BT\_LE\_FEAT\_BIT\_PAST\_RECV   25 |
| --- |

## [◆ ](#aa05da01a6a9b9ac26423d6fc2661f3db)BT\_LE\_FEAT\_BIT\_PAST\_SEND

| #define BT\_LE\_FEAT\_BIT\_PAST\_SEND   24 |
| --- |

## [◆ ](#a434fb43b6b3176393f5d22d3932d69fa)BT\_LE\_FEAT\_BIT\_PATH\_LOSS\_MONITOR

| #define BT\_LE\_FEAT\_BIT\_PATH\_LOSS\_MONITOR   35 |
| --- |

## [◆ ](#af251cb9d905586fd53113f5920038dae)BT\_LE\_FEAT\_BIT\_PAWR\_ADVERTISER

| #define BT\_LE\_FEAT\_BIT\_PAWR\_ADVERTISER   43 |
| --- |

## [◆ ](#a00bb51972e0db07be84d4f3dfd007cea)BT\_LE\_FEAT\_BIT\_PAWR\_SCANNER

| #define BT\_LE\_FEAT\_BIT\_PAWR\_SCANNER   44 |
| --- |

## [◆ ](#a1ac5bab6d48775b4e63e249b5759a683)BT\_LE\_FEAT\_BIT\_PER\_ADV

| #define BT\_LE\_FEAT\_BIT\_PER\_ADV   13 |
| --- |

## [◆ ](#ad5a8221cb25d79b63f1a574699983038)BT\_LE\_FEAT\_BIT\_PER\_ADV\_ADI\_SUPP

| #define BT\_LE\_FEAT\_BIT\_PER\_ADV\_ADI\_SUPP   36 |
| --- |

## [◆ ](#aeaea6ea6595de9e3283fd6063bf7c579)BT\_LE\_FEAT\_BIT\_PER\_INIT\_FEAT\_XCHG

| #define BT\_LE\_FEAT\_BIT\_PER\_INIT\_FEAT\_XCHG   3 |
| --- |

## [◆ ](#afcbc8d664c8e924b777c06ffb4c17315)BT\_LE\_FEAT\_BIT\_PHY\_2M

| #define BT\_LE\_FEAT\_BIT\_PHY\_2M   8 |
| --- |

## [◆ ](#a800686aa45cf336fbd6efc76b3752959)BT\_LE\_FEAT\_BIT\_PHY\_CODED

| #define BT\_LE\_FEAT\_BIT\_PHY\_CODED   11 |
| --- |

## [◆ ](#a9b4dc56ef4433b0c0dc74a3d95cf289e)BT\_LE\_FEAT\_BIT\_PING

| #define BT\_LE\_FEAT\_BIT\_PING   4 |
| --- |

## [◆ ](#a3c4196c04a73aa537baa845e061e9654)BT\_LE\_FEAT\_BIT\_PRIVACY

| #define BT\_LE\_FEAT\_BIT\_PRIVACY   6 |
| --- |

## [◆ ](#a0138172a0ed78244d8d3ac9d6936cf85)BT\_LE\_FEAT\_BIT\_PWR\_CHG\_IND

| #define BT\_LE\_FEAT\_BIT\_PWR\_CHG\_IND   34 |
| --- |

## [◆ ](#a938f823110f31a3a5d034cbe9b9d26eb)BT\_LE\_FEAT\_BIT\_PWR\_CLASS\_1

| #define BT\_LE\_FEAT\_BIT\_PWR\_CLASS\_1   15 |
| --- |

## [◆ ](#ae58f5260530d1b94608874f5d03d766d)BT\_LE\_FEAT\_BIT\_PWR\_CTRL\_REQ

| #define BT\_LE\_FEAT\_BIT\_PWR\_CTRL\_REQ   33 |
| --- |

## [◆ ](#a6d17dd4238ea471daca22f74e3cc3bcb)BT\_LE\_FEAT\_BIT\_REMOTE\_PUB\_KEY\_VALIDATE

| #define BT\_LE\_FEAT\_BIT\_REMOTE\_PUB\_KEY\_VALIDATE   27 |
| --- |

## [◆ ](#a9d9449f1935d6522291eca581f3fa9b0)BT\_LE\_FEAT\_BIT\_RX\_CTE

| #define BT\_LE\_FEAT\_BIT\_RX\_CTE   23 |
| --- |

## [◆ ](#a829e9d23a16912bad19448a6c4061e3b)BT\_LE\_FEAT\_BIT\_SCA\_UPDATE

| #define BT\_LE\_FEAT\_BIT\_SCA\_UPDATE   26 |
| --- |

## [◆ ](#a9430a65ea813861b6890252ed4748f19)BT\_LE\_FEAT\_BIT\_SMI\_RX

| #define BT\_LE\_FEAT\_BIT\_SMI\_RX   10 |
| --- |

## [◆ ](#aea19f3c3cdcec054c81c176d5aa5f319)BT\_LE\_FEAT\_BIT\_SMI\_TX

| #define BT\_LE\_FEAT\_BIT\_SMI\_TX   9 |
| --- |

## [◆ ](#a2fed771f5611212e48027025e11f7678)BT\_LE\_FEAT\_BIT\_SYNC\_RECEIVER

| #define BT\_LE\_FEAT\_BIT\_SYNC\_RECEIVER   31 |
| --- |

## [◆ ](#a6bf20989952fed3726bc45873beb896e)BT\_LE\_FEAT\_TEST

| #define BT\_LE\_FEAT\_TEST | ( |  | *feat*, |
| --- | --- | --- | --- |
|  |  |  | *n* ) |

**Value:**

(feat[(n) >> 3] & \

BIT((n) & 7))

## [◆ ](#abff5a0c6d1f3ab8ecf297d4ef29f7940)BT\_LE\_STATES\_PER\_CONN\_ADV

| #define BT\_LE\_STATES\_PER\_CONN\_ADV | ( |  | *states* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(states & [BIT64\_MASK](group__sys-util.md#ga1a138896caafcb2429a6483ea7412d12)(38))

[BIT64\_MASK](group__sys-util.md#ga1a138896caafcb2429a6483ea7412d12)

#define BIT64\_MASK(n)

64-bit bit mask with bits 0 through n-1 (inclusive) set, or 0 if n is 0.

**Definition** util\_macro.h:74

## [◆ ](#a9871a7d021f9e0bcfda278c82c3731d7)BT\_LE\_STATES\_SCAN\_INIT

| #define BT\_LE\_STATES\_SCAN\_INIT | ( |  | *states* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

0

## [◆ ](#a6630ceb874d343f721931f80ee5fa67e)BT\_LK\_AUTH\_COMBINATION\_P192

| #define BT\_LK\_AUTH\_COMBINATION\_P192   0x05 |
| --- |

## [◆ ](#aa941cce486c497afa6d03fec326396b9)BT\_LK\_AUTH\_COMBINATION\_P256

| #define BT\_LK\_AUTH\_COMBINATION\_P256   0x08 |
| --- |

## [◆ ](#a5753841a02ba0c2fa627d9e96bad045d)BT\_LK\_CHANGED\_COMBINATION

| #define BT\_LK\_CHANGED\_COMBINATION   0x06 |
| --- |

## [◆ ](#a7283a42b1220dd6d56c22cd9cb424e7c)BT\_LK\_COMBINATION

| #define BT\_LK\_COMBINATION   0x00 |
| --- |

## [◆ ](#a916e6133d2dadb9aaf5fe42d0c0e1b96)BT\_LK\_DEBUG\_COMBINATION

| #define BT\_LK\_DEBUG\_COMBINATION   0x03 |
| --- |

## [◆ ](#a12ffe67b9e4ec01bbe400a6a3cc5b859)BT\_LK\_LOCAL\_UNIT

| #define BT\_LK\_LOCAL\_UNIT   0x01 |
| --- |

## [◆ ](#aeb53b797c4fc91a38a459ff5f29d35e1)BT\_LK\_REMOTE\_UNIT

| #define BT\_LK\_REMOTE\_UNIT   0x02 |
| --- |

## [◆ ](#adfea495d48088eae78491a14730bef31)BT\_LK\_UNAUTH\_COMBINATION\_P192

| #define BT\_LK\_UNAUTH\_COMBINATION\_P192   0x04 |
| --- |

## [◆ ](#ada18ab581a323eafe8754009ef27d05e)BT\_LK\_UNAUTH\_COMBINATION\_P256

| #define BT\_LK\_UNAUTH\_COMBINATION\_P256   0x07 |
| --- |

## [◆ ](#a47ba0b282416c3e8f4275a38b7780b59)BT\_MITM

| #define BT\_MITM   0x01 |
| --- |

## [◆ ](#ac267cc5384724efba92df0be57379a89)BT\_OCF

| #define BT\_OCF | ( |  | *opcode* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((opcode) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10))

## [◆ ](#af3ae81176a4ace13a562262ad53aeae6)BT\_OGF

| #define BT\_OGF | ( |  | *opcode* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((opcode) >> 10) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(6))

## [◆ ](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)BT\_OGF\_BASEBAND

| #define BT\_OGF\_BASEBAND   0x03 |
| --- |

## [◆ ](#ac7c7348e291360169bf0ca5bb57b3d7e)BT\_OGF\_INFO

| #define BT\_OGF\_INFO   0x04 |
| --- |

## [◆ ](#abb09db6a211185842f039eddb9fadca5)BT\_OGF\_LE

| #define BT\_OGF\_LE   0x08 |
| --- |

## [◆ ](#abb6c50fe170ffaaaf4a0827058331381)BT\_OGF\_LINK\_CTRL

| #define BT\_OGF\_LINK\_CTRL   0x01 |
| --- |

## [◆ ](#a5ce14b9103bd538f3610afd80284157e)BT\_OGF\_STATUS

| #define BT\_OGF\_STATUS   0x05 |
| --- |

## [◆ ](#a6b682cb6e4f489ffb67b05280b3dbd65)BT\_OGF\_VS

| #define BT\_OGF\_VS   0x3f |
| --- |

## [◆ ](#a7e006e0f69c498601f2c64a4ce3d8101)BT\_OP

| #define BT\_OP | ( |  | *ogf*, |
| --- | --- | --- | --- |
|  |  |  | *ocf* ) |

**Value:**

((ocf) | ((ogf) << 10))

## [◆ ](#a1bf4881fa3237f4a5b22e5fdb417762b)BT\_OP\_NOP

| #define BT\_OP\_NOP   0x0000 |
| --- |

## [◆ ](#a35831810e3a7e2c5446780b14ef7d9c1)BT\_OVERFLOW\_LINK\_ACL

| #define BT\_OVERFLOW\_LINK\_ACL   0x01 |
| --- |

## [◆ ](#ad32010743baef10c635d8b08f21c8641)BT\_OVERFLOW\_LINK\_ISO

| #define BT\_OVERFLOW\_LINK\_ISO   0x02 |
| --- |

## [◆ ](#a44233b934e33c65af90d03ad301e6b9d)BT\_OVERFLOW\_LINK\_SYNCH

| #define BT\_OVERFLOW\_LINK\_SYNCH   0x00 |
| --- |

## [◆ ](#ac1ebc6168b2823aea2af2e2f89ffb6cd)BT\_TX\_POWER\_LEVEL\_CURRENT

| #define BT\_TX\_POWER\_LEVEL\_CURRENT   0x00 |
| --- |

## [◆ ](#ad835bc44abee2e174f86cd55ac0338e3)BT\_TX\_POWER\_LEVEL\_MAX

| #define BT\_TX\_POWER\_LEVEL\_MAX   0x01 |
| --- |

## [◆ ](#aa3a50b43beddbd76ae67b71e79a80175)EDR\_ESCO\_PKT\_MASK

| #define EDR\_ESCO\_PKT\_MASK |
| --- |

**Value:**

([HCI\_PKT\_TYPE\_ESCO\_2EV3](#a1ccc4d6e5cfc560b7e2cb80c4c386607) | \

[HCI\_PKT\_TYPE\_ESCO\_3EV3](#ac5f09e3db1bc4d697ff705802e9ec3a0) | \

[HCI\_PKT\_TYPE\_ESCO\_2EV5](#a1252be2692bcfb7a1256c63c4deed15d) | \

[HCI\_PKT\_TYPE\_ESCO\_3EV5](#aa45e51b1be89505fe599bc7983fcb950))

[HCI\_PKT\_TYPE\_ESCO\_2EV5](#a1252be2692bcfb7a1256c63c4deed15d)

#define HCI\_PKT\_TYPE\_ESCO\_2EV5

**Definition** hci\_types.h:339

[HCI\_PKT\_TYPE\_ESCO\_2EV3](#a1ccc4d6e5cfc560b7e2cb80c4c386607)

#define HCI\_PKT\_TYPE\_ESCO\_2EV3

**Definition** hci\_types.h:337

[HCI\_PKT\_TYPE\_ESCO\_3EV5](#aa45e51b1be89505fe599bc7983fcb950)

#define HCI\_PKT\_TYPE\_ESCO\_3EV5

**Definition** hci\_types.h:340

[HCI\_PKT\_TYPE\_ESCO\_3EV3](#ac5f09e3db1bc4d697ff705802e9ec3a0)

#define HCI\_PKT\_TYPE\_ESCO\_3EV3

**Definition** hci\_types.h:338

## [◆ ](#a8afe2c798b2d9657778f0815e3cb11c8)ESCO\_PKT\_MASK

| #define ESCO\_PKT\_MASK |
| --- |

**Value:**

([HCI\_PKT\_TYPE\_SCO\_HV1](#a4b048addd84409867177a97c785c4a73) | \

[HCI\_PKT\_TYPE\_SCO\_HV2](#a98f8217b27c0b9b7817c86520da45018) | \

[HCI\_PKT\_TYPE\_SCO\_HV3](#af67cdc23b6542e6d8323f14e17c7171d) | \

[HCI\_PKT\_TYPE\_ESCO\_EV3](#a9530e916a0cf905e2185cd021320bfff) | \

[HCI\_PKT\_TYPE\_ESCO\_EV4](#a3e0b6a1aa3818cb0c36f7883fd361c7e) | \

[HCI\_PKT\_TYPE\_ESCO\_EV5](#a1f7474cb16a495bd81dc1f23d4103f70))

[HCI\_PKT\_TYPE\_ESCO\_EV5](#a1f7474cb16a495bd81dc1f23d4103f70)

#define HCI\_PKT\_TYPE\_ESCO\_EV5

**Definition** hci\_types.h:336

[HCI\_PKT\_TYPE\_ESCO\_EV4](#a3e0b6a1aa3818cb0c36f7883fd361c7e)

#define HCI\_PKT\_TYPE\_ESCO\_EV4

**Definition** hci\_types.h:335

[HCI\_PKT\_TYPE\_SCO\_HV1](#a4b048addd84409867177a97c785c4a73)

#define HCI\_PKT\_TYPE\_SCO\_HV1

**Definition** hci\_types.h:331

[HCI\_PKT\_TYPE\_ESCO\_EV3](#a9530e916a0cf905e2185cd021320bfff)

#define HCI\_PKT\_TYPE\_ESCO\_EV3

**Definition** hci\_types.h:334

[HCI\_PKT\_TYPE\_SCO\_HV2](#a98f8217b27c0b9b7817c86520da45018)

#define HCI\_PKT\_TYPE\_SCO\_HV2

**Definition** hci\_types.h:332

[HCI\_PKT\_TYPE\_SCO\_HV3](#af67cdc23b6542e6d8323f14e17c7171d)

#define HCI\_PKT\_TYPE\_SCO\_HV3

**Definition** hci\_types.h:333

## [◆ ](#a1ccc4d6e5cfc560b7e2cb80c4c386607)HCI\_PKT\_TYPE\_ESCO\_2EV3

| #define HCI\_PKT\_TYPE\_ESCO\_2EV3   0x0040 |
| --- |

## [◆ ](#a1252be2692bcfb7a1256c63c4deed15d)HCI\_PKT\_TYPE\_ESCO\_2EV5

| #define HCI\_PKT\_TYPE\_ESCO\_2EV5   0x0100 |
| --- |

## [◆ ](#ac5f09e3db1bc4d697ff705802e9ec3a0)HCI\_PKT\_TYPE\_ESCO\_3EV3

| #define HCI\_PKT\_TYPE\_ESCO\_3EV3   0x0080 |
| --- |

## [◆ ](#aa45e51b1be89505fe599bc7983fcb950)HCI\_PKT\_TYPE\_ESCO\_3EV5

| #define HCI\_PKT\_TYPE\_ESCO\_3EV5   0x0200 |
| --- |

## [◆ ](#a9530e916a0cf905e2185cd021320bfff)HCI\_PKT\_TYPE\_ESCO\_EV3

| #define HCI\_PKT\_TYPE\_ESCO\_EV3   0x0008 |
| --- |

## [◆ ](#a3e0b6a1aa3818cb0c36f7883fd361c7e)HCI\_PKT\_TYPE\_ESCO\_EV4

| #define HCI\_PKT\_TYPE\_ESCO\_EV4   0x0010 |
| --- |

## [◆ ](#a1f7474cb16a495bd81dc1f23d4103f70)HCI\_PKT\_TYPE\_ESCO\_EV5

| #define HCI\_PKT\_TYPE\_ESCO\_EV5   0x0020 |
| --- |

## [◆ ](#aecb5b3886467c41baf979d01d8bde4a1)HCI\_PKT\_TYPE\_HV1

| #define HCI\_PKT\_TYPE\_HV1   0x0020 |
| --- |

## [◆ ](#ae68633ce74639ec6f06d5ef4feee2d09)HCI\_PKT\_TYPE\_HV2

| #define HCI\_PKT\_TYPE\_HV2   0x0040 |
| --- |

## [◆ ](#aecd04ca27f536a1cb15aacf9ee80aba8)HCI\_PKT\_TYPE\_HV3

| #define HCI\_PKT\_TYPE\_HV3   0x0080 |
| --- |

## [◆ ](#a4b048addd84409867177a97c785c4a73)HCI\_PKT\_TYPE\_SCO\_HV1

| #define HCI\_PKT\_TYPE\_SCO\_HV1   0x0001 |
| --- |

## [◆ ](#a98f8217b27c0b9b7817c86520da45018)HCI\_PKT\_TYPE\_SCO\_HV2

| #define HCI\_PKT\_TYPE\_SCO\_HV2   0x0002 |
| --- |

## [◆ ](#af67cdc23b6542e6d8323f14e17c7171d)HCI\_PKT\_TYPE\_SCO\_HV3

| #define HCI\_PKT\_TYPE\_SCO\_HV3   0x0004 |
| --- |

## [◆ ](#a1ef7929257a087f340f1f421cd8f51ce)SCO\_PKT\_MASK

| #define SCO\_PKT\_MASK |
| --- |

**Value:**

([HCI\_PKT\_TYPE\_SCO\_HV1](#a4b048addd84409867177a97c785c4a73) | \

[HCI\_PKT\_TYPE\_SCO\_HV2](#a98f8217b27c0b9b7817c86520da45018) | \

[HCI\_PKT\_TYPE\_SCO\_HV3](#af67cdc23b6542e6d8323f14e17c7171d))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [hci\_types.h](hci__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
