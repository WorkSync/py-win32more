from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
CollectionChange = Int32
CollectionChange_Reset: CollectionChange = 0
CollectionChange_ItemInserted: CollectionChange = 1
CollectionChange_ItemRemoved: CollectionChange = 2
CollectionChange_ItemChanged: CollectionChange = 3
class IIterable(Generic[T], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Collections.IIterable'
    _iid_ = Guid('{faa585ea-6214-4217-afda-7f46de5869b3}')
    @winrt_commethod(6)
    def First(self) -> win32more.Windows.Foundation.Collections.IIterator[T]: ...
class IIterator(Generic[T], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Collections.IIterator'
    _iid_ = Guid('{6a79e863-4300-459a-9966-cbb660963ee1}')
    @winrt_commethod(6)
    def get_Current(self) -> T: ...
    @winrt_commethod(7)
    def get_HasCurrent(self) -> Boolean: ...
    @winrt_commethod(8)
    def MoveNext(self) -> Boolean: ...
    @winrt_commethod(9)
    def GetMany(self, items: Annotated[SZArray[T], 'Out']) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class IKeyValuePair(Generic[K, V], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Collections.IKeyValuePair'
    _iid_ = Guid('{02b51929-c1c4-4a7e-8940-0312b5c18500}')
    @winrt_commethod(6)
    def get_Key(self) -> K: ...
    @winrt_commethod(7)
    def get_Value(self) -> V: ...
    Key = property(get_Key, None)
    Value = property(get_Value, None)
class IMapChangedEventArgs(Generic[K], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Collections.IMapChangedEventArgs'
    _iid_ = Guid('{9939f4df-050a-4c0f-aa60-77075f9c4777}')
    @winrt_commethod(6)
    def get_CollectionChange(self) -> win32more.Windows.Foundation.Collections.CollectionChange: ...
    @winrt_commethod(7)
    def get_Key(self) -> K: ...
    CollectionChange = property(get_CollectionChange, None)
    Key = property(get_Key, None)
class IMapView(Generic[K, V], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Collections.IMapView'
    _iid_ = Guid('{e480ce40-a338-4ada-adcf-272272e48cb9}')
    @winrt_commethod(6)
    def Lookup(self, key: K) -> V: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def HasKey(self, key: K) -> Boolean: ...
    @winrt_commethod(9)
    def Split(self, first: POINTER(win32more.Windows.Foundation.Collections.IMapView[K, V]), second: POINTER(win32more.Windows.Foundation.Collections.IMapView[K, V])) -> Void: ...
    Size = property(get_Size, None)
class IMap(Generic[K, V], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Collections.IMap'
    _iid_ = Guid('{3c2925fe-8519-45c1-aa79-197b6718c1c1}')
    @winrt_commethod(6)
    def Lookup(self, key: K) -> V: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def HasKey(self, key: K) -> Boolean: ...
    @winrt_commethod(9)
    def GetView(self) -> win32more.Windows.Foundation.Collections.IMapView[K, V]: ...
    @winrt_commethod(10)
    def Insert(self, key: K, value: V) -> Boolean: ...
    @winrt_commethod(11)
    def Remove(self, key: K) -> Void: ...
    @winrt_commethod(12)
    def Clear(self) -> Void: ...
    Size = property(get_Size, None)
class IObservableMap(Generic[K, V], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Collections.IObservableMap'
    _iid_ = Guid('{65df2bf5-bf39-41b5-aebc-5a9d865e472b}')
    @winrt_commethod(6)
    def add_MapChanged(self, vhnd: win32more.Windows.Foundation.Collections.MapChangedEventHandler[K, V]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MapChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IObservableVector(Generic[T], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Collections.IObservableVector'
    _iid_ = Guid('{5917eb53-50b4-4a0d-b309-65862b3f1dbc}')
    @winrt_commethod(6)
    def add_VectorChanged(self, vhnd: win32more.Windows.Foundation.Collections.VectorChangedEventHandler[T]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_VectorChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Collections.IPropertySet'
    _iid_ = Guid('{8a43ed9f-f4e6-4421-acf9-1dab2986820c}')
class IVectorChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Collections.IVectorChangedEventArgs'
    _iid_ = Guid('{575933df-34fe-4480-af15-07691f3d5d9b}')
    @winrt_commethod(6)
    def get_CollectionChange(self) -> win32more.Windows.Foundation.Collections.CollectionChange: ...
    @winrt_commethod(7)
    def get_Index(self) -> UInt32: ...
    CollectionChange = property(get_CollectionChange, None)
    Index = property(get_Index, None)
class IVectorView(Generic[T], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Collections.IVectorView'
    _iid_ = Guid('{bbe1fa4c-b0e3-4583-baef-1f1b2e483e56}')
    @winrt_commethod(6)
    def GetAt(self, index: UInt32) -> T: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def IndexOf(self, value: T, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_commethod(9)
    def GetMany(self, startIndex: UInt32, items: Annotated[SZArray[T], 'Out']) -> UInt32: ...
    Size = property(get_Size, None)
class IVector(Generic[T], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Collections.IVector'
    _iid_ = Guid('{913337e9-11a1-4345-a3a2-4e7f956e222d}')
    @winrt_commethod(6)
    def GetAt(self, index: UInt32) -> T: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def GetView(self) -> win32more.Windows.Foundation.Collections.IVectorView[T]: ...
    @winrt_commethod(9)
    def IndexOf(self, value: T, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_commethod(10)
    def SetAt(self, index: UInt32, value: T) -> Void: ...
    @winrt_commethod(11)
    def InsertAt(self, index: UInt32, value: T) -> Void: ...
    @winrt_commethod(12)
    def RemoveAt(self, index: UInt32) -> Void: ...
    @winrt_commethod(13)
    def Append(self, value: T) -> Void: ...
    @winrt_commethod(14)
    def RemoveAtEnd(self) -> Void: ...
    @winrt_commethod(15)
    def Clear(self) -> Void: ...
    @winrt_commethod(16)
    def GetMany(self, startIndex: UInt32, items: Annotated[SZArray[T], 'Out']) -> UInt32: ...
    @winrt_commethod(17)
    def ReplaceAll(self, items: Annotated[SZArray[T], 'In']) -> Void: ...
    Size = property(get_Size, None)
class MapChangedEventHandler(Generic[K, V], MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{179517f3-94ee-41f8-bddc-768a895544f3}')
    def Invoke(self, sender: win32more.Windows.Foundation.Collections.IObservableMap[K, V], event: win32more.Windows.Foundation.Collections.IMapChangedEventArgs[K]) -> Void: ...
class PropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IPropertySet
    _classid_ = 'Windows.Foundation.Collections.PropertySet'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Foundation.Collections.PropertySet.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Foundation.Collections.PropertySet: ...
    @winrt_mixinmethod
    def add_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], vhnd: win32more.Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    Size = property(get_Size, None)
class StringMap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]
    _classid_ = 'Windows.Foundation.Collections.StringMap'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Foundation.Collections.StringMap.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Foundation.Collections.StringMap: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String, value: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]: ...
    @winrt_mixinmethod
    def add_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String], vhnd: win32more.Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, WinRT_String]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String], token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Size = property(get_Size, None)
class ValueSet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IPropertySet
    _classid_ = 'Windows.Foundation.Collections.ValueSet'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Foundation.Collections.ValueSet.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def add_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], vhnd: win32more.Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    Size = property(get_Size, None)
class VectorChangedEventHandler(Generic[T], MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0c051752-9fbf-4c70-aa0c-0e4c82d9a761}')
    def Invoke(self, sender: win32more.Windows.Foundation.Collections.IObservableVector[T], event: win32more.Windows.Foundation.Collections.IVectorChangedEventArgs) -> Void: ...
make_ready(__name__)
