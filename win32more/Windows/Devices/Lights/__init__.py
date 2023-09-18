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
import win32more.Windows.Devices.Lights
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ILamp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.ILamp'
    _iid_ = Guid('{047d5b9a-ea45-4b2b-b1a2-14dff00bde7b}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_BrightnessLevel(self) -> Single: ...
    @winrt_commethod(10)
    def put_BrightnessLevel(self, value: Single) -> Void: ...
    @winrt_commethod(11)
    def get_IsColorSettable(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(13)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(14)
    def add_AvailabilityChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Lights.Lamp, win32more.Windows.Devices.Lights.LampAvailabilityChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_AvailabilityChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    BrightnessLevel = property(get_BrightnessLevel, put_BrightnessLevel)
    IsColorSettable = property(get_IsColorSettable, None)
    Color = property(get_Color, put_Color)
class ILampArray(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.ILampArray'
    _iid_ = Guid('{7ace9787-c8a0-4e95-a1e0-d58676538649}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_HardwareVendorId(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_HardwareProductId(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_HardwareVersion(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_LampArrayKind(self) -> win32more.Windows.Devices.Lights.LampArrayKind: ...
    @winrt_commethod(11)
    def get_LampCount(self) -> Int32: ...
    @winrt_commethod(12)
    def get_MinUpdateInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def get_BoundingBox(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(14)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_BrightnessLevel(self) -> Double: ...
    @winrt_commethod(17)
    def put_BrightnessLevel(self, value: Double) -> Void: ...
    @winrt_commethod(18)
    def get_IsConnected(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_SupportsVirtualKeys(self) -> Boolean: ...
    @winrt_commethod(20)
    def GetLampInfo(self, lampIndex: Int32) -> win32more.Windows.Devices.Lights.LampInfo: ...
    @winrt_commethod(21)
    def GetIndicesForKey(self, key: win32more.Windows.System.VirtualKey) -> SZArray[Int32]: ...
    @winrt_commethod(22)
    def GetIndicesForPurposes(self, purposes: win32more.Windows.Devices.Lights.LampPurposes) -> SZArray[Int32]: ...
    @winrt_commethod(23)
    def SetColor(self, desiredColor: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(24)
    def SetColorForIndex(self, lampIndex: Int32, desiredColor: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(25)
    def SetSingleColorForIndices(self, desiredColor: win32more.Windows.UI.Color, lampIndexes: Annotated[SZArray[Int32], 'In']) -> Void: ...
    @winrt_commethod(26)
    def SetColorsForIndices(self, desiredColors: Annotated[SZArray[win32more.Windows.UI.Color], 'In'], lampIndexes: Annotated[SZArray[Int32], 'In']) -> Void: ...
    @winrt_commethod(27)
    def SetColorsForKey(self, desiredColor: win32more.Windows.UI.Color, key: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(28)
    def SetColorsForKeys(self, desiredColors: Annotated[SZArray[win32more.Windows.UI.Color], 'In'], keys: Annotated[SZArray[win32more.Windows.System.VirtualKey], 'In']) -> Void: ...
    @winrt_commethod(29)
    def SetColorsForPurposes(self, desiredColor: win32more.Windows.UI.Color, purposes: win32more.Windows.Devices.Lights.LampPurposes) -> Void: ...
    @winrt_commethod(30)
    def SendMessageAsync(self, messageId: Int32, message: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(31)
    def RequestMessageAsync(self, messageId: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    DeviceId = property(get_DeviceId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVersion = property(get_HardwareVersion, None)
    LampArrayKind = property(get_LampArrayKind, None)
    LampCount = property(get_LampCount, None)
    MinUpdateInterval = property(get_MinUpdateInterval, None)
    BoundingBox = property(get_BoundingBox, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    BrightnessLevel = property(get_BrightnessLevel, put_BrightnessLevel)
    IsConnected = property(get_IsConnected, None)
    SupportsVirtualKeys = property(get_SupportsVirtualKeys, None)
class ILampArrayStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.ILampArrayStatics'
    _iid_ = Guid('{7bb8c98d-5fc1-452d-bb1f-4ad410d398ff}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Lights.LampArray]: ...
class ILampAvailabilityChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.ILampAvailabilityChangedEventArgs'
    _iid_ = Guid('{4f6e3ded-07a2-499d-9260-67e304532ba4}')
    @winrt_commethod(6)
    def get_IsAvailable(self) -> Boolean: ...
    IsAvailable = property(get_IsAvailable, None)
class ILampInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.ILampInfo'
    _iid_ = Guid('{30bb521c-0acf-49da-8c10-150b9cf62713}')
    @winrt_commethod(6)
    def get_Index(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Purposes(self) -> win32more.Windows.Devices.Lights.LampPurposes: ...
    @winrt_commethod(8)
    def get_Position(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def get_RedLevelCount(self) -> Int32: ...
    @winrt_commethod(10)
    def get_GreenLevelCount(self) -> Int32: ...
    @winrt_commethod(11)
    def get_BlueLevelCount(self) -> Int32: ...
    @winrt_commethod(12)
    def get_GainLevelCount(self) -> Int32: ...
    @winrt_commethod(13)
    def get_FixedColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(14)
    def GetNearestSupportedColor(self, desiredColor: win32more.Windows.UI.Color) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(15)
    def get_UpdateLatency(self) -> win32more.Windows.Foundation.TimeSpan: ...
    Index = property(get_Index, None)
    Purposes = property(get_Purposes, None)
    Position = property(get_Position, None)
    RedLevelCount = property(get_RedLevelCount, None)
    GreenLevelCount = property(get_GreenLevelCount, None)
    BlueLevelCount = property(get_BlueLevelCount, None)
    GainLevelCount = property(get_GainLevelCount, None)
    FixedColor = property(get_FixedColor, None)
    UpdateLatency = property(get_UpdateLatency, None)
class ILampStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.ILampStatics'
    _iid_ = Guid('{a822416c-8885-401e-b821-8e8b38a8e8ec}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Lights.Lamp]: ...
    @winrt_commethod(8)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Lights.Lamp]: ...
class Lamp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Lights.ILamp
    _classid_ = 'Windows.Devices.Lights.Lamp'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Lights.ILamp) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Devices.Lights.ILamp) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.Devices.Lights.ILamp, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BrightnessLevel(self: win32more.Windows.Devices.Lights.ILamp) -> Single: ...
    @winrt_mixinmethod
    def put_BrightnessLevel(self: win32more.Windows.Devices.Lights.ILamp, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_IsColorSettable(self: win32more.Windows.Devices.Lights.ILamp) -> Boolean: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.Devices.Lights.ILamp) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.Devices.Lights.ILamp, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def add_AvailabilityChanged(self: win32more.Windows.Devices.Lights.ILamp, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Lights.Lamp, win32more.Windows.Devices.Lights.LampAvailabilityChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailabilityChanged(self: win32more.Windows.Devices.Lights.ILamp, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Lights.ILampStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Lights.ILampStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Lights.Lamp]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.Devices.Lights.ILampStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Lights.Lamp]: ...
    DeviceId = property(get_DeviceId, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    BrightnessLevel = property(get_BrightnessLevel, put_BrightnessLevel)
    IsColorSettable = property(get_IsColorSettable, None)
    Color = property(get_Color, put_Color)
class LampArray(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Lights.ILampArray
    _classid_ = 'Windows.Devices.Lights.LampArray'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Lights.ILampArray) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HardwareVendorId(self: win32more.Windows.Devices.Lights.ILampArray) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareProductId(self: win32more.Windows.Devices.Lights.ILampArray) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVersion(self: win32more.Windows.Devices.Lights.ILampArray) -> UInt16: ...
    @winrt_mixinmethod
    def get_LampArrayKind(self: win32more.Windows.Devices.Lights.ILampArray) -> win32more.Windows.Devices.Lights.LampArrayKind: ...
    @winrt_mixinmethod
    def get_LampCount(self: win32more.Windows.Devices.Lights.ILampArray) -> Int32: ...
    @winrt_mixinmethod
    def get_MinUpdateInterval(self: win32more.Windows.Devices.Lights.ILampArray) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_BoundingBox(self: win32more.Windows.Devices.Lights.ILampArray) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Devices.Lights.ILampArray) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.Devices.Lights.ILampArray, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BrightnessLevel(self: win32more.Windows.Devices.Lights.ILampArray) -> Double: ...
    @winrt_mixinmethod
    def put_BrightnessLevel(self: win32more.Windows.Devices.Lights.ILampArray, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsConnected(self: win32more.Windows.Devices.Lights.ILampArray) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportsVirtualKeys(self: win32more.Windows.Devices.Lights.ILampArray) -> Boolean: ...
    @winrt_mixinmethod
    def GetLampInfo(self: win32more.Windows.Devices.Lights.ILampArray, lampIndex: Int32) -> win32more.Windows.Devices.Lights.LampInfo: ...
    @winrt_mixinmethod
    def GetIndicesForKey(self: win32more.Windows.Devices.Lights.ILampArray, key: win32more.Windows.System.VirtualKey) -> SZArray[Int32]: ...
    @winrt_mixinmethod
    def GetIndicesForPurposes(self: win32more.Windows.Devices.Lights.ILampArray, purposes: win32more.Windows.Devices.Lights.LampPurposes) -> SZArray[Int32]: ...
    @winrt_mixinmethod
    def SetColor(self: win32more.Windows.Devices.Lights.ILampArray, desiredColor: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def SetColorForIndex(self: win32more.Windows.Devices.Lights.ILampArray, lampIndex: Int32, desiredColor: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def SetSingleColorForIndices(self: win32more.Windows.Devices.Lights.ILampArray, desiredColor: win32more.Windows.UI.Color, lampIndexes: Annotated[SZArray[Int32], 'In']) -> Void: ...
    @winrt_mixinmethod
    def SetColorsForIndices(self: win32more.Windows.Devices.Lights.ILampArray, desiredColors: Annotated[SZArray[win32more.Windows.UI.Color], 'In'], lampIndexes: Annotated[SZArray[Int32], 'In']) -> Void: ...
    @winrt_mixinmethod
    def SetColorsForKey(self: win32more.Windows.Devices.Lights.ILampArray, desiredColor: win32more.Windows.UI.Color, key: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_mixinmethod
    def SetColorsForKeys(self: win32more.Windows.Devices.Lights.ILampArray, desiredColors: Annotated[SZArray[win32more.Windows.UI.Color], 'In'], keys: Annotated[SZArray[win32more.Windows.System.VirtualKey], 'In']) -> Void: ...
    @winrt_mixinmethod
    def SetColorsForPurposes(self: win32more.Windows.Devices.Lights.ILampArray, desiredColor: win32more.Windows.UI.Color, purposes: win32more.Windows.Devices.Lights.LampPurposes) -> Void: ...
    @winrt_mixinmethod
    def SendMessageAsync(self: win32more.Windows.Devices.Lights.ILampArray, messageId: Int32, message: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RequestMessageAsync(self: win32more.Windows.Devices.Lights.ILampArray, messageId: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Lights.ILampArrayStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Lights.ILampArrayStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Lights.LampArray]: ...
    DeviceId = property(get_DeviceId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVersion = property(get_HardwareVersion, None)
    LampArrayKind = property(get_LampArrayKind, None)
    LampCount = property(get_LampCount, None)
    MinUpdateInterval = property(get_MinUpdateInterval, None)
    BoundingBox = property(get_BoundingBox, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    BrightnessLevel = property(get_BrightnessLevel, put_BrightnessLevel)
    IsConnected = property(get_IsConnected, None)
    SupportsVirtualKeys = property(get_SupportsVirtualKeys, None)
LampArrayKind = Int32
LampArrayKind_Undefined: LampArrayKind = 0
LampArrayKind_Keyboard: LampArrayKind = 1
LampArrayKind_Mouse: LampArrayKind = 2
LampArrayKind_GameController: LampArrayKind = 3
LampArrayKind_Peripheral: LampArrayKind = 4
LampArrayKind_Scene: LampArrayKind = 5
LampArrayKind_Notification: LampArrayKind = 6
LampArrayKind_Chassis: LampArrayKind = 7
LampArrayKind_Wearable: LampArrayKind = 8
LampArrayKind_Furniture: LampArrayKind = 9
LampArrayKind_Art: LampArrayKind = 10
class LampAvailabilityChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Lights.ILampAvailabilityChangedEventArgs
    _classid_ = 'Windows.Devices.Lights.LampAvailabilityChangedEventArgs'
    @winrt_mixinmethod
    def get_IsAvailable(self: win32more.Windows.Devices.Lights.ILampAvailabilityChangedEventArgs) -> Boolean: ...
    IsAvailable = property(get_IsAvailable, None)
class LampInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Lights.ILampInfo
    _classid_ = 'Windows.Devices.Lights.LampInfo'
    @winrt_mixinmethod
    def get_Index(self: win32more.Windows.Devices.Lights.ILampInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_Purposes(self: win32more.Windows.Devices.Lights.ILampInfo) -> win32more.Windows.Devices.Lights.LampPurposes: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Devices.Lights.ILampInfo) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_RedLevelCount(self: win32more.Windows.Devices.Lights.ILampInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_GreenLevelCount(self: win32more.Windows.Devices.Lights.ILampInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_BlueLevelCount(self: win32more.Windows.Devices.Lights.ILampInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_GainLevelCount(self: win32more.Windows.Devices.Lights.ILampInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_FixedColor(self: win32more.Windows.Devices.Lights.ILampInfo) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def GetNearestSupportedColor(self: win32more.Windows.Devices.Lights.ILampInfo, desiredColor: win32more.Windows.UI.Color) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_UpdateLatency(self: win32more.Windows.Devices.Lights.ILampInfo) -> win32more.Windows.Foundation.TimeSpan: ...
    Index = property(get_Index, None)
    Purposes = property(get_Purposes, None)
    Position = property(get_Position, None)
    RedLevelCount = property(get_RedLevelCount, None)
    GreenLevelCount = property(get_GreenLevelCount, None)
    BlueLevelCount = property(get_BlueLevelCount, None)
    GainLevelCount = property(get_GainLevelCount, None)
    FixedColor = property(get_FixedColor, None)
    UpdateLatency = property(get_UpdateLatency, None)
LampPurposes = UInt32
LampPurposes_Undefined: LampPurposes = 0
LampPurposes_Control: LampPurposes = 1
LampPurposes_Accent: LampPurposes = 2
LampPurposes_Branding: LampPurposes = 4
LampPurposes_Status: LampPurposes = 8
LampPurposes_Illumination: LampPurposes = 16
LampPurposes_Presentation: LampPurposes = 32
make_head(_module, 'ILamp')
make_head(_module, 'ILampArray')
make_head(_module, 'ILampArrayStatics')
make_head(_module, 'ILampAvailabilityChangedEventArgs')
make_head(_module, 'ILampInfo')
make_head(_module, 'ILampStatics')
make_head(_module, 'Lamp')
make_head(_module, 'LampArray')
make_head(_module, 'LampAvailabilityChangedEventArgs')
make_head(_module, 'LampInfo')
