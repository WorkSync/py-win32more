from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Phone.Devices.Notification
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IVibrationDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1b4a6595-cfcd-4e08-92-fb-c1-90-6d-04-49-8c')
    @winrt_commethod(6)
    def Vibrate(self, duration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def Cancel(self) -> Void: ...
class IVibrationDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('332fd2f1-1c69-4c91-94-9e-4b-b6-7a-85-bd-c7')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Phone.Devices.Notification.VibrationDevice: ...
class VibrationDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Devices.Notification.VibrationDevice'
    @winrt_mixinmethod
    def Vibrate(self: Windows.Phone.Devices.Notification.IVibrationDevice, duration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def Cancel(self: Windows.Phone.Devices.Notification.IVibrationDevice) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Phone.Devices.Notification.IVibrationDeviceStatics) -> Windows.Phone.Devices.Notification.VibrationDevice: ...
make_head(_module, 'IVibrationDevice')
make_head(_module, 'IVibrationDeviceStatics')
make_head(_module, 'VibrationDevice')
