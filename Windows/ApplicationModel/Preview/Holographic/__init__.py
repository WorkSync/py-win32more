from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.Activation
import Windows.ApplicationModel.Preview.Holographic
import Windows.Foundation.Numerics
import Windows.Perception.Spatial
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class HolographicApplicationPreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Preview.Holographic.HolographicApplicationPreview'
    @winrt_classmethod
    def IsCurrentViewPresentedOnHolographicDisplay(cls: Windows.ApplicationModel.Preview.Holographic.IHolographicApplicationPreviewStatics) -> Boolean: ...
    @winrt_classmethod
    def IsHolographicActivation(cls: Windows.ApplicationModel.Preview.Holographic.IHolographicApplicationPreviewStatics, activatedEventArgs: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Boolean: ...
class HolographicKeyboardPlacementOverridePreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Preview.Holographic.HolographicKeyboardPlacementOverridePreview'
    @winrt_mixinmethod
    def SetPlacementOverride(self: Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreview, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: Windows.Foundation.Numerics.Vector3, normal: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def SetPlacementOverrideWithMaxSize(self: Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreview, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: Windows.Foundation.Numerics.Vector3, normal: Windows.Foundation.Numerics.Vector3, maxSize: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def ResetPlacementOverride(self: Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreview) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreviewStatics) -> Windows.ApplicationModel.Preview.Holographic.HolographicKeyboardPlacementOverridePreview: ...
class IHolographicApplicationPreviewStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fe038691-2a3a-45a9-a2-08-7b-ed-69-19-19-f3')
    @winrt_commethod(6)
    def IsCurrentViewPresentedOnHolographicDisplay(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsHolographicActivation(self, activatedEventArgs: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Boolean: ...
class IHolographicKeyboardPlacementOverridePreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c8a8ce3a-dfde-5a14-8d-5f-18-2c-52-6d-d9-c4')
    @winrt_commethod(6)
    def SetPlacementOverride(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: Windows.Foundation.Numerics.Vector3, normal: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(7)
    def SetPlacementOverrideWithMaxSize(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: Windows.Foundation.Numerics.Vector3, normal: Windows.Foundation.Numerics.Vector3, maxSize: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def ResetPlacementOverride(self) -> Void: ...
class IHolographicKeyboardPlacementOverridePreviewStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('202e6039-1ff6-5a06-aa-c4-a5-e2-4f-a3-ec-4b')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.ApplicationModel.Preview.Holographic.HolographicKeyboardPlacementOverridePreview: ...
make_head(_module, 'HolographicApplicationPreview')
make_head(_module, 'HolographicKeyboardPlacementOverridePreview')
make_head(_module, 'IHolographicApplicationPreviewStatics')
make_head(_module, 'IHolographicKeyboardPlacementOverridePreview')
make_head(_module, 'IHolographicKeyboardPlacementOverridePreviewStatics')
