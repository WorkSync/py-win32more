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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Data.Json
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IJsonArray(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonArray'
    _iid_ = Guid('{08c1ddb6-0cbd-4a9a-b5d3-2f852dc37e81}')
    @winrt_commethod(6)
    def GetObjectAt(self, index: UInt32) -> win32more.Windows.Data.Json.JsonObject: ...
    @winrt_commethod(7)
    def GetArrayAt(self, index: UInt32) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_commethod(8)
    def GetStringAt(self, index: UInt32) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetNumberAt(self, index: UInt32) -> Double: ...
    @winrt_commethod(10)
    def GetBooleanAt(self, index: UInt32) -> Boolean: ...
class IJsonArrayStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonArrayStatics'
    _iid_ = Guid('{db1434a9-e164-499f-93e2-8a8f49bb90ba}')
    @winrt_commethod(6)
    def Parse(self, input: WinRT_String) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_commethod(7)
    def TryParse(self, input: WinRT_String, result: POINTER(win32more.Windows.Data.Json.JsonArray)) -> Boolean: ...
class IJsonErrorStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonErrorStatics2'
    _iid_ = Guid('{404030da-87d0-436c-83ab-fc7b12c0cc26}')
    @winrt_commethod(6)
    def GetJsonStatus(self, hresult: Int32) -> win32more.Windows.Data.Json.JsonErrorStatus: ...
class IJsonObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonObject'
    _iid_ = Guid('{064e24dd-29c2-4f83-9ac1-9ee11578beb3}')
    @winrt_commethod(6)
    def GetNamedValue(self, name: WinRT_String) -> win32more.Windows.Data.Json.JsonValue: ...
    @winrt_commethod(7)
    def SetNamedValue(self, name: WinRT_String, value: win32more.Windows.Data.Json.IJsonValue) -> Void: ...
    @winrt_commethod(8)
    def GetNamedObject(self, name: WinRT_String) -> win32more.Windows.Data.Json.JsonObject: ...
    @winrt_commethod(9)
    def GetNamedArray(self, name: WinRT_String) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_commethod(10)
    def GetNamedString(self, name: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetNamedNumber(self, name: WinRT_String) -> Double: ...
    @winrt_commethod(12)
    def GetNamedBoolean(self, name: WinRT_String) -> Boolean: ...
class IJsonObjectStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonObjectStatics'
    _iid_ = Guid('{2289f159-54de-45d8-abcc-22603fa066a0}')
    @winrt_commethod(6)
    def Parse(self, input: WinRT_String) -> win32more.Windows.Data.Json.JsonObject: ...
    @winrt_commethod(7)
    def TryParse(self, input: WinRT_String, result: POINTER(win32more.Windows.Data.Json.JsonObject)) -> Boolean: ...
class IJsonObjectWithDefaultValues(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonObjectWithDefaultValues'
    _iid_ = Guid('{d960d2a2-b7f0-4f00-8e44-d82cf415ea13}')
    @winrt_commethod(6)
    def GetNamedValueOrDefault(self, name: WinRT_String, defaultValue: win32more.Windows.Data.Json.JsonValue) -> win32more.Windows.Data.Json.JsonValue: ...
    @winrt_commethod(7)
    def GetNamedObjectOrDefault(self, name: WinRT_String, defaultValue: win32more.Windows.Data.Json.JsonObject) -> win32more.Windows.Data.Json.JsonObject: ...
    @winrt_commethod(8)
    def GetNamedStringOrDefault(self, name: WinRT_String, defaultValue: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetNamedArrayOrDefault(self, name: WinRT_String, defaultValue: win32more.Windows.Data.Json.JsonArray) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_commethod(10)
    def GetNamedNumberOrDefault(self, name: WinRT_String, defaultValue: Double) -> Double: ...
    @winrt_commethod(11)
    def GetNamedBooleanOrDefault(self, name: WinRT_String, defaultValue: Boolean) -> Boolean: ...
class IJsonValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonValue'
    _iid_ = Guid('{a3219ecb-f0b3-4dcd-beee-19d48cd3ed1e}')
    @winrt_commethod(6)
    def get_ValueType(self) -> win32more.Windows.Data.Json.JsonValueType: ...
    @winrt_commethod(7)
    def Stringify(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetString(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetNumber(self) -> Double: ...
    @winrt_commethod(10)
    def GetBoolean(self) -> Boolean: ...
    @winrt_commethod(11)
    def GetArray(self) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_commethod(12)
    def GetObject(self) -> win32more.Windows.Data.Json.JsonObject: ...
    ValueType = property(get_ValueType, None)
class IJsonValueStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonValueStatics'
    _iid_ = Guid('{5f6b544a-2f53-48e1-91a3-f78b50a6345c}')
    @winrt_commethod(6)
    def Parse(self, input: WinRT_String) -> win32more.Windows.Data.Json.JsonValue: ...
    @winrt_commethod(7)
    def TryParse(self, input: WinRT_String, result: POINTER(win32more.Windows.Data.Json.JsonValue)) -> Boolean: ...
    @winrt_commethod(8)
    def CreateBooleanValue(self, input: Boolean) -> win32more.Windows.Data.Json.JsonValue: ...
    @winrt_commethod(9)
    def CreateNumberValue(self, input: Double) -> win32more.Windows.Data.Json.JsonValue: ...
    @winrt_commethod(10)
    def CreateStringValue(self, input: WinRT_String) -> win32more.Windows.Data.Json.JsonValue: ...
class IJsonValueStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonValueStatics2'
    _iid_ = Guid('{1d9ecbe4-3fe8-4335-8392-93d8e36865f0}')
    @winrt_commethod(6)
    def CreateNullValue(self) -> win32more.Windows.Data.Json.JsonValue: ...
class JsonArray(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Json.IJsonArray
    _classid_ = 'Windows.Data.Json.JsonArray'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetObjectAt(self: win32more.Windows.Data.Json.IJsonArray, index: UInt32) -> win32more.Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def GetArrayAt(self: win32more.Windows.Data.Json.IJsonArray, index: UInt32) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetStringAt(self: win32more.Windows.Data.Json.IJsonArray, index: UInt32) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNumberAt(self: win32more.Windows.Data.Json.IJsonArray, index: UInt32) -> Double: ...
    @winrt_mixinmethod
    def GetBooleanAt(self: win32more.Windows.Data.Json.IJsonArray, index: UInt32) -> Boolean: ...
    @winrt_mixinmethod
    def get_ValueType(self: win32more.Windows.Data.Json.IJsonValue) -> win32more.Windows.Data.Json.JsonValueType: ...
    @winrt_mixinmethod
    def Stringify(self: win32more.Windows.Data.Json.IJsonValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetString(self: win32more.Windows.Data.Json.IJsonValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNumber(self: win32more.Windows.Data.Json.IJsonValue) -> Double: ...
    @winrt_mixinmethod
    def GetBoolean(self: win32more.Windows.Data.Json.IJsonValue) -> Boolean: ...
    @winrt_mixinmethod
    def GetArray(self: win32more.Windows.Data.Json.IJsonValue) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetObject(self: win32more.Windows.Data.Json.IJsonValue) -> win32more.Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Data.Json.IJsonValue], index: UInt32) -> win32more.Windows.Data.Json.IJsonValue: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Data.Json.IJsonValue]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Data.Json.IJsonValue]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Json.IJsonValue]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Data.Json.IJsonValue], value: win32more.Windows.Data.Json.IJsonValue, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Data.Json.IJsonValue], index: UInt32, value: win32more.Windows.Data.Json.IJsonValue) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Data.Json.IJsonValue], index: UInt32, value: win32more.Windows.Data.Json.IJsonValue) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Data.Json.IJsonValue], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Data.Json.IJsonValue], value: win32more.Windows.Data.Json.IJsonValue) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Data.Json.IJsonValue]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Data.Json.IJsonValue]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Data.Json.IJsonValue], startIndex: UInt32, items: Annotated[SZArray[win32more.Windows.Data.Json.IJsonValue], 'Out']) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Data.Json.IJsonValue], items: Annotated[SZArray[win32more.Windows.Data.Json.IJsonValue], 'In']) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Data.Json.IJsonValue]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Data.Json.IJsonValue]: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def Parse(cls: win32more.Windows.Data.Json.IJsonArrayStatics, input: WinRT_String) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_classmethod
    def TryParse(cls: win32more.Windows.Data.Json.IJsonArrayStatics, input: WinRT_String, result: POINTER(win32more.Windows.Data.Json.JsonArray)) -> Boolean: ...
    ValueType = property(get_ValueType, None)
    Size = property(get_Size, None)
class JsonError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.JsonError'
    @winrt_classmethod
    def GetJsonStatus(cls: win32more.Windows.Data.Json.IJsonErrorStatics2, hresult: Int32) -> win32more.Windows.Data.Json.JsonErrorStatus: ...
JsonErrorStatus = Int32
JsonErrorStatus_Unknown: JsonErrorStatus = 0
JsonErrorStatus_InvalidJsonString: JsonErrorStatus = 1
JsonErrorStatus_InvalidJsonNumber: JsonErrorStatus = 2
JsonErrorStatus_JsonValueNotFound: JsonErrorStatus = 3
JsonErrorStatus_ImplementationLimit: JsonErrorStatus = 4
class JsonObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Json.IJsonObject
    _classid_ = 'Windows.Data.Json.JsonObject'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def GetNamedValue(self: win32more.Windows.Data.Json.IJsonObject, name: WinRT_String) -> win32more.Windows.Data.Json.JsonValue: ...
    @winrt_mixinmethod
    def SetNamedValue(self: win32more.Windows.Data.Json.IJsonObject, name: WinRT_String, value: win32more.Windows.Data.Json.IJsonValue) -> Void: ...
    @winrt_mixinmethod
    def GetNamedObject(self: win32more.Windows.Data.Json.IJsonObject, name: WinRT_String) -> win32more.Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def GetNamedArray(self: win32more.Windows.Data.Json.IJsonObject, name: WinRT_String) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetNamedString(self: win32more.Windows.Data.Json.IJsonObject, name: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNamedNumber(self: win32more.Windows.Data.Json.IJsonObject, name: WinRT_String) -> Double: ...
    @winrt_mixinmethod
    def GetNamedBoolean(self: win32more.Windows.Data.Json.IJsonObject, name: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def get_ValueType(self: win32more.Windows.Data.Json.IJsonValue) -> win32more.Windows.Data.Json.JsonValueType: ...
    @winrt_mixinmethod
    def Stringify(self: win32more.Windows.Data.Json.IJsonValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetString(self: win32more.Windows.Data.Json.IJsonValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNumber(self: win32more.Windows.Data.Json.IJsonValue) -> Double: ...
    @winrt_mixinmethod
    def GetBoolean(self: win32more.Windows.Data.Json.IJsonValue) -> Boolean: ...
    @winrt_mixinmethod
    def GetArray(self: win32more.Windows.Data.Json.IJsonValue) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetObject(self: win32more.Windows.Data.Json.IJsonValue) -> win32more.Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Data.Json.IJsonValue], key: WinRT_String) -> win32more.Windows.Data.Json.IJsonValue: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Data.Json.IJsonValue]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Data.Json.IJsonValue], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Data.Json.IJsonValue]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Data.Json.IJsonValue]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Data.Json.IJsonValue], key: WinRT_String, value: win32more.Windows.Data.Json.IJsonValue) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Data.Json.IJsonValue], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Data.Json.IJsonValue]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Data.Json.IJsonValue]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Data.Json.IJsonValue]]: ...
    @winrt_mixinmethod
    def GetNamedValueOrDefault(self: win32more.Windows.Data.Json.IJsonObjectWithDefaultValues, name: WinRT_String, defaultValue: win32more.Windows.Data.Json.JsonValue) -> win32more.Windows.Data.Json.JsonValue: ...
    @winrt_mixinmethod
    def GetNamedObjectOrDefault(self: win32more.Windows.Data.Json.IJsonObjectWithDefaultValues, name: WinRT_String, defaultValue: win32more.Windows.Data.Json.JsonObject) -> win32more.Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def GetNamedStringOrDefault(self: win32more.Windows.Data.Json.IJsonObjectWithDefaultValues, name: WinRT_String, defaultValue: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNamedArrayOrDefault(self: win32more.Windows.Data.Json.IJsonObjectWithDefaultValues, name: WinRT_String, defaultValue: win32more.Windows.Data.Json.JsonArray) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetNamedNumberOrDefault(self: win32more.Windows.Data.Json.IJsonObjectWithDefaultValues, name: WinRT_String, defaultValue: Double) -> Double: ...
    @winrt_mixinmethod
    def GetNamedBooleanOrDefault(self: win32more.Windows.Data.Json.IJsonObjectWithDefaultValues, name: WinRT_String, defaultValue: Boolean) -> Boolean: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def Parse(cls: win32more.Windows.Data.Json.IJsonObjectStatics, input: WinRT_String) -> win32more.Windows.Data.Json.JsonObject: ...
    @winrt_classmethod
    def TryParse(cls: win32more.Windows.Data.Json.IJsonObjectStatics, input: WinRT_String, result: POINTER(win32more.Windows.Data.Json.JsonObject)) -> Boolean: ...
    ValueType = property(get_ValueType, None)
    Size = property(get_Size, None)
class JsonValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Json.IJsonValue
    _classid_ = 'Windows.Data.Json.JsonValue'
    @winrt_mixinmethod
    def get_ValueType(self: win32more.Windows.Data.Json.IJsonValue) -> win32more.Windows.Data.Json.JsonValueType: ...
    @winrt_mixinmethod
    def Stringify(self: win32more.Windows.Data.Json.IJsonValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetString(self: win32more.Windows.Data.Json.IJsonValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNumber(self: win32more.Windows.Data.Json.IJsonValue) -> Double: ...
    @winrt_mixinmethod
    def GetBoolean(self: win32more.Windows.Data.Json.IJsonValue) -> Boolean: ...
    @winrt_mixinmethod
    def GetArray(self: win32more.Windows.Data.Json.IJsonValue) -> win32more.Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetObject(self: win32more.Windows.Data.Json.IJsonValue) -> win32more.Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def CreateNullValue(cls: win32more.Windows.Data.Json.IJsonValueStatics2) -> win32more.Windows.Data.Json.JsonValue: ...
    @winrt_classmethod
    def Parse(cls: win32more.Windows.Data.Json.IJsonValueStatics, input: WinRT_String) -> win32more.Windows.Data.Json.JsonValue: ...
    @winrt_classmethod
    def TryParse(cls: win32more.Windows.Data.Json.IJsonValueStatics, input: WinRT_String, result: POINTER(win32more.Windows.Data.Json.JsonValue)) -> Boolean: ...
    @winrt_classmethod
    def CreateBooleanValue(cls: win32more.Windows.Data.Json.IJsonValueStatics, input: Boolean) -> win32more.Windows.Data.Json.JsonValue: ...
    @winrt_classmethod
    def CreateNumberValue(cls: win32more.Windows.Data.Json.IJsonValueStatics, input: Double) -> win32more.Windows.Data.Json.JsonValue: ...
    @winrt_classmethod
    def CreateStringValue(cls: win32more.Windows.Data.Json.IJsonValueStatics, input: WinRT_String) -> win32more.Windows.Data.Json.JsonValue: ...
    ValueType = property(get_ValueType, None)
JsonValueType = Int32
JsonValueType_Null: JsonValueType = 0
JsonValueType_Boolean: JsonValueType = 1
JsonValueType_Number: JsonValueType = 2
JsonValueType_String: JsonValueType = 3
JsonValueType_Array: JsonValueType = 4
JsonValueType_Object: JsonValueType = 5
make_head(_module, 'IJsonArray')
make_head(_module, 'IJsonArrayStatics')
make_head(_module, 'IJsonErrorStatics2')
make_head(_module, 'IJsonObject')
make_head(_module, 'IJsonObjectStatics')
make_head(_module, 'IJsonObjectWithDefaultValues')
make_head(_module, 'IJsonValue')
make_head(_module, 'IJsonValueStatics')
make_head(_module, 'IJsonValueStatics2')
make_head(_module, 'JsonArray')
make_head(_module, 'JsonError')
make_head(_module, 'JsonObject')
make_head(_module, 'JsonValue')
