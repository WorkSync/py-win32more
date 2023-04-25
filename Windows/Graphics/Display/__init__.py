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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics
import Windows.Graphics.Display
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AdvancedColorInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Display.AdvancedColorInfo'
    @winrt_mixinmethod
    def get_CurrentAdvancedColorKind(self: Windows.Graphics.Display.IAdvancedColorInfo) -> Windows.Graphics.Display.AdvancedColorKind: ...
    @winrt_mixinmethod
    def get_RedPrimary(self: Windows.Graphics.Display.IAdvancedColorInfo) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_GreenPrimary(self: Windows.Graphics.Display.IAdvancedColorInfo) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_BluePrimary(self: Windows.Graphics.Display.IAdvancedColorInfo) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_WhitePoint(self: Windows.Graphics.Display.IAdvancedColorInfo) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_MaxLuminanceInNits(self: Windows.Graphics.Display.IAdvancedColorInfo) -> Single: ...
    @winrt_mixinmethod
    def get_MinLuminanceInNits(self: Windows.Graphics.Display.IAdvancedColorInfo) -> Single: ...
    @winrt_mixinmethod
    def get_MaxAverageFullFrameLuminanceInNits(self: Windows.Graphics.Display.IAdvancedColorInfo) -> Single: ...
    @winrt_mixinmethod
    def get_SdrWhiteLevelInNits(self: Windows.Graphics.Display.IAdvancedColorInfo) -> Single: ...
    @winrt_mixinmethod
    def IsHdrMetadataFormatCurrentlySupported(self: Windows.Graphics.Display.IAdvancedColorInfo, format: Windows.Graphics.Display.HdrMetadataFormat) -> Boolean: ...
    @winrt_mixinmethod
    def IsAdvancedColorKindAvailable(self: Windows.Graphics.Display.IAdvancedColorInfo, kind: Windows.Graphics.Display.AdvancedColorKind) -> Boolean: ...
    CurrentAdvancedColorKind = property(get_CurrentAdvancedColorKind, None)
    RedPrimary = property(get_RedPrimary, None)
    GreenPrimary = property(get_GreenPrimary, None)
    BluePrimary = property(get_BluePrimary, None)
    WhitePoint = property(get_WhitePoint, None)
    MaxLuminanceInNits = property(get_MaxLuminanceInNits, None)
    MinLuminanceInNits = property(get_MinLuminanceInNits, None)
    MaxAverageFullFrameLuminanceInNits = property(get_MaxAverageFullFrameLuminanceInNits, None)
    SdrWhiteLevelInNits = property(get_SdrWhiteLevelInNits, None)
AdvancedColorKind = Int32
AdvancedColorKind_StandardDynamicRange: AdvancedColorKind = 0
AdvancedColorKind_WideColorGamut: AdvancedColorKind = 1
AdvancedColorKind_HighDynamicRange: AdvancedColorKind = 2
class BrightnessOverride(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Display.BrightnessOverride'
    @winrt_mixinmethod
    def get_IsSupported(self: Windows.Graphics.Display.IBrightnessOverride) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsOverrideActive(self: Windows.Graphics.Display.IBrightnessOverride) -> Boolean: ...
    @winrt_mixinmethod
    def get_BrightnessLevel(self: Windows.Graphics.Display.IBrightnessOverride) -> Double: ...
    @winrt_mixinmethod
    def SetBrightnessLevel(self: Windows.Graphics.Display.IBrightnessOverride, brightnessLevel: Double, options: Windows.Graphics.Display.DisplayBrightnessOverrideOptions) -> Void: ...
    @winrt_mixinmethod
    def SetBrightnessScenario(self: Windows.Graphics.Display.IBrightnessOverride, scenario: Windows.Graphics.Display.DisplayBrightnessScenario, options: Windows.Graphics.Display.DisplayBrightnessOverrideOptions) -> Void: ...
    @winrt_mixinmethod
    def GetLevelForScenario(self: Windows.Graphics.Display.IBrightnessOverride, scenario: Windows.Graphics.Display.DisplayBrightnessScenario) -> Double: ...
    @winrt_mixinmethod
    def StartOverride(self: Windows.Graphics.Display.IBrightnessOverride) -> Void: ...
    @winrt_mixinmethod
    def StopOverride(self: Windows.Graphics.Display.IBrightnessOverride) -> Void: ...
    @winrt_mixinmethod
    def add_IsSupportedChanged(self: Windows.Graphics.Display.IBrightnessOverride, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.BrightnessOverride, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsSupportedChanged(self: Windows.Graphics.Display.IBrightnessOverride, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_IsOverrideActiveChanged(self: Windows.Graphics.Display.IBrightnessOverride, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.BrightnessOverride, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsOverrideActiveChanged(self: Windows.Graphics.Display.IBrightnessOverride, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BrightnessLevelChanged(self: Windows.Graphics.Display.IBrightnessOverride, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.BrightnessOverride, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BrightnessLevelChanged(self: Windows.Graphics.Display.IBrightnessOverride, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefaultForSystem(cls: Windows.Graphics.Display.IBrightnessOverrideStatics) -> Windows.Graphics.Display.BrightnessOverride: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.Graphics.Display.IBrightnessOverrideStatics) -> Windows.Graphics.Display.BrightnessOverride: ...
    @winrt_classmethod
    def SaveForSystemAsync(cls: Windows.Graphics.Display.IBrightnessOverrideStatics, value: Windows.Graphics.Display.BrightnessOverride) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    IsSupported = property(get_IsSupported, None)
    IsOverrideActive = property(get_IsOverrideActive, None)
    BrightnessLevel = property(get_BrightnessLevel, None)
class BrightnessOverrideSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Display.BrightnessOverrideSettings'
    @winrt_mixinmethod
    def get_DesiredLevel(self: Windows.Graphics.Display.IBrightnessOverrideSettings) -> Double: ...
    @winrt_mixinmethod
    def get_DesiredNits(self: Windows.Graphics.Display.IBrightnessOverrideSettings) -> Single: ...
    @winrt_classmethod
    def CreateFromLevel(cls: Windows.Graphics.Display.IBrightnessOverrideSettingsStatics, level: Double) -> Windows.Graphics.Display.BrightnessOverrideSettings: ...
    @winrt_classmethod
    def CreateFromNits(cls: Windows.Graphics.Display.IBrightnessOverrideSettingsStatics, nits: Single) -> Windows.Graphics.Display.BrightnessOverrideSettings: ...
    @winrt_classmethod
    def CreateFromDisplayBrightnessOverrideScenario(cls: Windows.Graphics.Display.IBrightnessOverrideSettingsStatics, overrideScenario: Windows.Graphics.Display.DisplayBrightnessOverrideScenario) -> Windows.Graphics.Display.BrightnessOverrideSettings: ...
    DesiredLevel = property(get_DesiredLevel, None)
    DesiredNits = property(get_DesiredNits, None)
class ColorOverrideSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Display.ColorOverrideSettings'
    @winrt_mixinmethod
    def get_DesiredDisplayColorOverrideScenario(self: Windows.Graphics.Display.IColorOverrideSettings) -> Windows.Graphics.Display.DisplayColorOverrideScenario: ...
    @winrt_classmethod
    def CreateFromDisplayColorOverrideScenario(cls: Windows.Graphics.Display.IColorOverrideSettingsStatics, overrideScenario: Windows.Graphics.Display.DisplayColorOverrideScenario) -> Windows.Graphics.Display.ColorOverrideSettings: ...
    DesiredDisplayColorOverrideScenario = property(get_DesiredDisplayColorOverrideScenario, None)
DisplayBrightnessOverrideOptions = UInt32
DisplayBrightnessOverrideOptions_None: DisplayBrightnessOverrideOptions = 0
DisplayBrightnessOverrideOptions_UseDimmedPolicyWhenBatteryIsLow: DisplayBrightnessOverrideOptions = 1
DisplayBrightnessOverrideScenario = Int32
DisplayBrightnessOverrideScenario_IdleBrightness: DisplayBrightnessOverrideScenario = 0
DisplayBrightnessOverrideScenario_BarcodeReadingBrightness: DisplayBrightnessOverrideScenario = 1
DisplayBrightnessOverrideScenario_FullBrightness: DisplayBrightnessOverrideScenario = 2
DisplayBrightnessScenario = Int32
DisplayBrightnessScenario_DefaultBrightness: DisplayBrightnessScenario = 0
DisplayBrightnessScenario_IdleBrightness: DisplayBrightnessScenario = 1
DisplayBrightnessScenario_BarcodeReadingBrightness: DisplayBrightnessScenario = 2
DisplayBrightnessScenario_FullBrightness: DisplayBrightnessScenario = 3
DisplayColorOverrideScenario = Int32
DisplayColorOverrideScenario_Accurate: DisplayColorOverrideScenario = 0
class DisplayEnhancementOverride(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Display.DisplayEnhancementOverride'
    @winrt_mixinmethod
    def get_ColorOverrideSettings(self: Windows.Graphics.Display.IDisplayEnhancementOverride) -> Windows.Graphics.Display.ColorOverrideSettings: ...
    @winrt_mixinmethod
    def put_ColorOverrideSettings(self: Windows.Graphics.Display.IDisplayEnhancementOverride, value: Windows.Graphics.Display.ColorOverrideSettings) -> Void: ...
    @winrt_mixinmethod
    def get_BrightnessOverrideSettings(self: Windows.Graphics.Display.IDisplayEnhancementOverride) -> Windows.Graphics.Display.BrightnessOverrideSettings: ...
    @winrt_mixinmethod
    def put_BrightnessOverrideSettings(self: Windows.Graphics.Display.IDisplayEnhancementOverride, value: Windows.Graphics.Display.BrightnessOverrideSettings) -> Void: ...
    @winrt_mixinmethod
    def get_CanOverride(self: Windows.Graphics.Display.IDisplayEnhancementOverride) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsOverrideActive(self: Windows.Graphics.Display.IDisplayEnhancementOverride) -> Boolean: ...
    @winrt_mixinmethod
    def GetCurrentDisplayEnhancementOverrideCapabilities(self: Windows.Graphics.Display.IDisplayEnhancementOverride) -> Windows.Graphics.Display.DisplayEnhancementOverrideCapabilities: ...
    @winrt_mixinmethod
    def RequestOverride(self: Windows.Graphics.Display.IDisplayEnhancementOverride) -> Void: ...
    @winrt_mixinmethod
    def StopOverride(self: Windows.Graphics.Display.IDisplayEnhancementOverride) -> Void: ...
    @winrt_mixinmethod
    def add_CanOverrideChanged(self: Windows.Graphics.Display.IDisplayEnhancementOverride, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayEnhancementOverride, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CanOverrideChanged(self: Windows.Graphics.Display.IDisplayEnhancementOverride, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_IsOverrideActiveChanged(self: Windows.Graphics.Display.IDisplayEnhancementOverride, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayEnhancementOverride, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsOverrideActiveChanged(self: Windows.Graphics.Display.IDisplayEnhancementOverride, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DisplayEnhancementOverrideCapabilitiesChanged(self: Windows.Graphics.Display.IDisplayEnhancementOverride, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayEnhancementOverride, Windows.Graphics.Display.DisplayEnhancementOverrideCapabilitiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DisplayEnhancementOverrideCapabilitiesChanged(self: Windows.Graphics.Display.IDisplayEnhancementOverride, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.Graphics.Display.IDisplayEnhancementOverrideStatics) -> Windows.Graphics.Display.DisplayEnhancementOverride: ...
    ColorOverrideSettings = property(get_ColorOverrideSettings, put_ColorOverrideSettings)
    BrightnessOverrideSettings = property(get_BrightnessOverrideSettings, put_BrightnessOverrideSettings)
    CanOverride = property(get_CanOverride, None)
    IsOverrideActive = property(get_IsOverrideActive, None)
class DisplayEnhancementOverrideCapabilities(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Display.DisplayEnhancementOverrideCapabilities'
    @winrt_mixinmethod
    def get_IsBrightnessControlSupported(self: Windows.Graphics.Display.IDisplayEnhancementOverrideCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBrightnessNitsControlSupported(self: Windows.Graphics.Display.IDisplayEnhancementOverrideCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def GetSupportedNitRanges(self: Windows.Graphics.Display.IDisplayEnhancementOverrideCapabilities) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Display.NitRange]: ...
    IsBrightnessControlSupported = property(get_IsBrightnessControlSupported, None)
    IsBrightnessNitsControlSupported = property(get_IsBrightnessNitsControlSupported, None)
class DisplayEnhancementOverrideCapabilitiesChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Display.DisplayEnhancementOverrideCapabilitiesChangedEventArgs'
    @winrt_mixinmethod
    def get_Capabilities(self: Windows.Graphics.Display.IDisplayEnhancementOverrideCapabilitiesChangedEventArgs) -> Windows.Graphics.Display.DisplayEnhancementOverrideCapabilities: ...
    Capabilities = property(get_Capabilities, None)
class DisplayInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Display.DisplayInformation'
    @winrt_mixinmethod
    def get_CurrentOrientation(self: Windows.Graphics.Display.IDisplayInformation) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_mixinmethod
    def get_NativeOrientation(self: Windows.Graphics.Display.IDisplayInformation) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_mixinmethod
    def add_OrientationChanged(self: Windows.Graphics.Display.IDisplayInformation, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OrientationChanged(self: Windows.Graphics.Display.IDisplayInformation, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_ResolutionScale(self: Windows.Graphics.Display.IDisplayInformation) -> Windows.Graphics.Display.ResolutionScale: ...
    @winrt_mixinmethod
    def get_LogicalDpi(self: Windows.Graphics.Display.IDisplayInformation) -> Single: ...
    @winrt_mixinmethod
    def get_RawDpiX(self: Windows.Graphics.Display.IDisplayInformation) -> Single: ...
    @winrt_mixinmethod
    def get_RawDpiY(self: Windows.Graphics.Display.IDisplayInformation) -> Single: ...
    @winrt_mixinmethod
    def add_DpiChanged(self: Windows.Graphics.Display.IDisplayInformation, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DpiChanged(self: Windows.Graphics.Display.IDisplayInformation, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_StereoEnabled(self: Windows.Graphics.Display.IDisplayInformation) -> Boolean: ...
    @winrt_mixinmethod
    def add_StereoEnabledChanged(self: Windows.Graphics.Display.IDisplayInformation, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StereoEnabledChanged(self: Windows.Graphics.Display.IDisplayInformation, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetColorProfileAsync(self: Windows.Graphics.Display.IDisplayInformation) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def add_ColorProfileChanged(self: Windows.Graphics.Display.IDisplayInformation, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ColorProfileChanged(self: Windows.Graphics.Display.IDisplayInformation, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_RawPixelsPerViewPixel(self: Windows.Graphics.Display.IDisplayInformation2) -> Double: ...
    @winrt_mixinmethod
    def get_DiagonalSizeInInches(self: Windows.Graphics.Display.IDisplayInformation3) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_ScreenWidthInRawPixels(self: Windows.Graphics.Display.IDisplayInformation4) -> UInt32: ...
    @winrt_mixinmethod
    def get_ScreenHeightInRawPixels(self: Windows.Graphics.Display.IDisplayInformation4) -> UInt32: ...
    @winrt_mixinmethod
    def GetAdvancedColorInfo(self: Windows.Graphics.Display.IDisplayInformation5) -> Windows.Graphics.Display.AdvancedColorInfo: ...
    @winrt_mixinmethod
    def add_AdvancedColorInfoChanged(self: Windows.Graphics.Display.IDisplayInformation5, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AdvancedColorInfoChanged(self: Windows.Graphics.Display.IDisplayInformation5, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.Graphics.Display.IDisplayInformationStatics) -> Windows.Graphics.Display.DisplayInformation: ...
    @winrt_classmethod
    def get_AutoRotationPreferences(cls: Windows.Graphics.Display.IDisplayInformationStatics) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_classmethod
    def put_AutoRotationPreferences(cls: Windows.Graphics.Display.IDisplayInformationStatics, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_classmethod
    def add_DisplayContentsInvalidated(cls: Windows.Graphics.Display.IDisplayInformationStatics, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_DisplayContentsInvalidated(cls: Windows.Graphics.Display.IDisplayInformationStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentOrientation = property(get_CurrentOrientation, None)
    NativeOrientation = property(get_NativeOrientation, None)
    ResolutionScale = property(get_ResolutionScale, None)
    LogicalDpi = property(get_LogicalDpi, None)
    RawDpiX = property(get_RawDpiX, None)
    RawDpiY = property(get_RawDpiY, None)
    StereoEnabled = property(get_StereoEnabled, None)
    RawPixelsPerViewPixel = property(get_RawPixelsPerViewPixel, None)
    DiagonalSizeInInches = property(get_DiagonalSizeInInches, None)
    ScreenWidthInRawPixels = property(get_ScreenWidthInRawPixels, None)
    ScreenHeightInRawPixels = property(get_ScreenHeightInRawPixels, None)
    AutoRotationPreferences = property(get_AutoRotationPreferences, put_AutoRotationPreferences)
DisplayOrientations = UInt32
DisplayOrientations_None: DisplayOrientations = 0
DisplayOrientations_Landscape: DisplayOrientations = 1
DisplayOrientations_Portrait: DisplayOrientations = 2
DisplayOrientations_LandscapeFlipped: DisplayOrientations = 4
DisplayOrientations_PortraitFlipped: DisplayOrientations = 8
class DisplayProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Display.DisplayProperties'
    @winrt_classmethod
    def get_CurrentOrientation(cls: Windows.Graphics.Display.IDisplayPropertiesStatics) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_classmethod
    def get_NativeOrientation(cls: Windows.Graphics.Display.IDisplayPropertiesStatics) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_classmethod
    def get_AutoRotationPreferences(cls: Windows.Graphics.Display.IDisplayPropertiesStatics) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_classmethod
    def put_AutoRotationPreferences(cls: Windows.Graphics.Display.IDisplayPropertiesStatics, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_classmethod
    def add_OrientationChanged(cls: Windows.Graphics.Display.IDisplayPropertiesStatics, handler: Windows.Graphics.Display.DisplayPropertiesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_OrientationChanged(cls: Windows.Graphics.Display.IDisplayPropertiesStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ResolutionScale(cls: Windows.Graphics.Display.IDisplayPropertiesStatics) -> Windows.Graphics.Display.ResolutionScale: ...
    @winrt_classmethod
    def get_LogicalDpi(cls: Windows.Graphics.Display.IDisplayPropertiesStatics) -> Single: ...
    @winrt_classmethod
    def add_LogicalDpiChanged(cls: Windows.Graphics.Display.IDisplayPropertiesStatics, handler: Windows.Graphics.Display.DisplayPropertiesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LogicalDpiChanged(cls: Windows.Graphics.Display.IDisplayPropertiesStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_StereoEnabled(cls: Windows.Graphics.Display.IDisplayPropertiesStatics) -> Boolean: ...
    @winrt_classmethod
    def add_StereoEnabledChanged(cls: Windows.Graphics.Display.IDisplayPropertiesStatics, handler: Windows.Graphics.Display.DisplayPropertiesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_StereoEnabledChanged(cls: Windows.Graphics.Display.IDisplayPropertiesStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetColorProfileAsync(cls: Windows.Graphics.Display.IDisplayPropertiesStatics) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_classmethod
    def add_ColorProfileChanged(cls: Windows.Graphics.Display.IDisplayPropertiesStatics, handler: Windows.Graphics.Display.DisplayPropertiesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ColorProfileChanged(cls: Windows.Graphics.Display.IDisplayPropertiesStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_DisplayContentsInvalidated(cls: Windows.Graphics.Display.IDisplayPropertiesStatics, handler: Windows.Graphics.Display.DisplayPropertiesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_DisplayContentsInvalidated(cls: Windows.Graphics.Display.IDisplayPropertiesStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentOrientation = property(get_CurrentOrientation, None)
    NativeOrientation = property(get_NativeOrientation, None)
    AutoRotationPreferences = property(get_AutoRotationPreferences, put_AutoRotationPreferences)
    ResolutionScale = property(get_ResolutionScale, None)
    LogicalDpi = property(get_LogicalDpi, None)
    StereoEnabled = property(get_StereoEnabled, None)
class DisplayPropertiesEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dbdd8b01-f1a1-46d1-9e-e3-54-3b-cc-99-59-80')
    ClassId = 'Windows.Graphics.Display.DisplayPropertiesEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
class DisplayServices(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Display.DisplayServices'
    @winrt_classmethod
    def FindAll(cls: Windows.Graphics.Display.IDisplayServicesStatics) -> POINTER(Windows.Graphics.DisplayId_head): ...
HdrMetadataFormat = Int32
HdrMetadataFormat_Hdr10: HdrMetadataFormat = 0
HdrMetadataFormat_Hdr10Plus: HdrMetadataFormat = 1
class IAdvancedColorInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8797dcfb-b229-4081-ae-9a-2c-c8-5e-34-ad-6a')
    @winrt_commethod(6)
    def get_CurrentAdvancedColorKind(self) -> Windows.Graphics.Display.AdvancedColorKind: ...
    @winrt_commethod(7)
    def get_RedPrimary(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_GreenPrimary(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def get_BluePrimary(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(10)
    def get_WhitePoint(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(11)
    def get_MaxLuminanceInNits(self) -> Single: ...
    @winrt_commethod(12)
    def get_MinLuminanceInNits(self) -> Single: ...
    @winrt_commethod(13)
    def get_MaxAverageFullFrameLuminanceInNits(self) -> Single: ...
    @winrt_commethod(14)
    def get_SdrWhiteLevelInNits(self) -> Single: ...
    @winrt_commethod(15)
    def IsHdrMetadataFormatCurrentlySupported(self, format: Windows.Graphics.Display.HdrMetadataFormat) -> Boolean: ...
    @winrt_commethod(16)
    def IsAdvancedColorKindAvailable(self, kind: Windows.Graphics.Display.AdvancedColorKind) -> Boolean: ...
    CurrentAdvancedColorKind = property(get_CurrentAdvancedColorKind, None)
    RedPrimary = property(get_RedPrimary, None)
    GreenPrimary = property(get_GreenPrimary, None)
    BluePrimary = property(get_BluePrimary, None)
    WhitePoint = property(get_WhitePoint, None)
    MaxLuminanceInNits = property(get_MaxLuminanceInNits, None)
    MinLuminanceInNits = property(get_MinLuminanceInNits, None)
    MaxAverageFullFrameLuminanceInNits = property(get_MaxAverageFullFrameLuminanceInNits, None)
    SdrWhiteLevelInNits = property(get_SdrWhiteLevelInNits, None)
class IBrightnessOverride(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('96c9621a-c143-4392-be-dd-4a-7e-95-74-c8-fd')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsOverrideActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_BrightnessLevel(self) -> Double: ...
    @winrt_commethod(9)
    def SetBrightnessLevel(self, brightnessLevel: Double, options: Windows.Graphics.Display.DisplayBrightnessOverrideOptions) -> Void: ...
    @winrt_commethod(10)
    def SetBrightnessScenario(self, scenario: Windows.Graphics.Display.DisplayBrightnessScenario, options: Windows.Graphics.Display.DisplayBrightnessOverrideOptions) -> Void: ...
    @winrt_commethod(11)
    def GetLevelForScenario(self, scenario: Windows.Graphics.Display.DisplayBrightnessScenario) -> Double: ...
    @winrt_commethod(12)
    def StartOverride(self) -> Void: ...
    @winrt_commethod(13)
    def StopOverride(self) -> Void: ...
    @winrt_commethod(14)
    def add_IsSupportedChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.BrightnessOverride, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_IsSupportedChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_IsOverrideActiveChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.BrightnessOverride, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_IsOverrideActiveChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_BrightnessLevelChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.BrightnessOverride, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_BrightnessLevelChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsSupported = property(get_IsSupported, None)
    IsOverrideActive = property(get_IsOverrideActive, None)
    BrightnessLevel = property(get_BrightnessLevel, None)
class IBrightnessOverrideSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d112ab2a-7604-4dba-bc-f8-4b-6f-49-50-2c-b0')
    @winrt_commethod(6)
    def get_DesiredLevel(self) -> Double: ...
    @winrt_commethod(7)
    def get_DesiredNits(self) -> Single: ...
    DesiredLevel = property(get_DesiredLevel, None)
    DesiredNits = property(get_DesiredNits, None)
class IBrightnessOverrideSettingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d487dc90-6f74-440b-b3-83-5f-e9-6c-f0-0b-0f')
    @winrt_commethod(6)
    def CreateFromLevel(self, level: Double) -> Windows.Graphics.Display.BrightnessOverrideSettings: ...
    @winrt_commethod(7)
    def CreateFromNits(self, nits: Single) -> Windows.Graphics.Display.BrightnessOverrideSettings: ...
    @winrt_commethod(8)
    def CreateFromDisplayBrightnessOverrideScenario(self, overrideScenario: Windows.Graphics.Display.DisplayBrightnessOverrideScenario) -> Windows.Graphics.Display.BrightnessOverrideSettings: ...
class IBrightnessOverrideStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('03a7b9ed-e1f1-4a68-a1-1f-94-6a-d8-ce-53-93')
    @winrt_commethod(6)
    def GetDefaultForSystem(self) -> Windows.Graphics.Display.BrightnessOverride: ...
    @winrt_commethod(7)
    def GetForCurrentView(self) -> Windows.Graphics.Display.BrightnessOverride: ...
    @winrt_commethod(8)
    def SaveForSystemAsync(self, value: Windows.Graphics.Display.BrightnessOverride) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IColorOverrideSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fbefa134-4a81-4c4d-a5-b6-7d-1b-5c-4b-d0-0b')
    @winrt_commethod(6)
    def get_DesiredDisplayColorOverrideScenario(self) -> Windows.Graphics.Display.DisplayColorOverrideScenario: ...
    DesiredDisplayColorOverrideScenario = property(get_DesiredDisplayColorOverrideScenario, None)
class IColorOverrideSettingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b068e05f-c41f-4ac9-af-ab-82-7a-b6-24-8f-9a')
    @winrt_commethod(6)
    def CreateFromDisplayColorOverrideScenario(self, overrideScenario: Windows.Graphics.Display.DisplayColorOverrideScenario) -> Windows.Graphics.Display.ColorOverrideSettings: ...
class IDisplayEnhancementOverride(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('429594cf-d97a-4b02-a4-28-5c-42-92-f7-f5-22')
    @winrt_commethod(6)
    def get_ColorOverrideSettings(self) -> Windows.Graphics.Display.ColorOverrideSettings: ...
    @winrt_commethod(7)
    def put_ColorOverrideSettings(self, value: Windows.Graphics.Display.ColorOverrideSettings) -> Void: ...
    @winrt_commethod(8)
    def get_BrightnessOverrideSettings(self) -> Windows.Graphics.Display.BrightnessOverrideSettings: ...
    @winrt_commethod(9)
    def put_BrightnessOverrideSettings(self, value: Windows.Graphics.Display.BrightnessOverrideSettings) -> Void: ...
    @winrt_commethod(10)
    def get_CanOverride(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsOverrideActive(self) -> Boolean: ...
    @winrt_commethod(12)
    def GetCurrentDisplayEnhancementOverrideCapabilities(self) -> Windows.Graphics.Display.DisplayEnhancementOverrideCapabilities: ...
    @winrt_commethod(13)
    def RequestOverride(self) -> Void: ...
    @winrt_commethod(14)
    def StopOverride(self) -> Void: ...
    @winrt_commethod(15)
    def add_CanOverrideChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayEnhancementOverride, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_CanOverrideChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_IsOverrideActiveChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayEnhancementOverride, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_IsOverrideActiveChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_DisplayEnhancementOverrideCapabilitiesChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayEnhancementOverride, Windows.Graphics.Display.DisplayEnhancementOverrideCapabilitiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_DisplayEnhancementOverrideCapabilitiesChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ColorOverrideSettings = property(get_ColorOverrideSettings, put_ColorOverrideSettings)
    BrightnessOverrideSettings = property(get_BrightnessOverrideSettings, put_BrightnessOverrideSettings)
    CanOverride = property(get_CanOverride, None)
    IsOverrideActive = property(get_IsOverrideActive, None)
class IDisplayEnhancementOverrideCapabilities(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('457060de-ee5a-47b7-99-18-1e-51-e8-12-cc-c8')
    @winrt_commethod(6)
    def get_IsBrightnessControlSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsBrightnessNitsControlSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetSupportedNitRanges(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Display.NitRange]: ...
    IsBrightnessControlSupported = property(get_IsBrightnessControlSupported, None)
    IsBrightnessNitsControlSupported = property(get_IsBrightnessNitsControlSupported, None)
class IDisplayEnhancementOverrideCapabilitiesChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('db61e664-15fa-49da-8b-77-07-db-d2-af-58-5d')
    @winrt_commethod(6)
    def get_Capabilities(self) -> Windows.Graphics.Display.DisplayEnhancementOverrideCapabilities: ...
    Capabilities = property(get_Capabilities, None)
class IDisplayEnhancementOverrideStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cf5b7ec1-9791-4453-b0-13-29-b6-f7-78-e5-19')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.Graphics.Display.DisplayEnhancementOverride: ...
class IDisplayInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bed112ae-adc3-4dc9-ae-65-85-1f-4d-7d-47-99')
    @winrt_commethod(6)
    def get_CurrentOrientation(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(7)
    def get_NativeOrientation(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(8)
    def add_OrientationChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_OrientationChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_ResolutionScale(self) -> Windows.Graphics.Display.ResolutionScale: ...
    @winrt_commethod(11)
    def get_LogicalDpi(self) -> Single: ...
    @winrt_commethod(12)
    def get_RawDpiX(self) -> Single: ...
    @winrt_commethod(13)
    def get_RawDpiY(self) -> Single: ...
    @winrt_commethod(14)
    def add_DpiChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_DpiChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_StereoEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def add_StereoEnabledChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_StereoEnabledChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def GetColorProfileAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(20)
    def add_ColorProfileChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_ColorProfileChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentOrientation = property(get_CurrentOrientation, None)
    NativeOrientation = property(get_NativeOrientation, None)
    ResolutionScale = property(get_ResolutionScale, None)
    LogicalDpi = property(get_LogicalDpi, None)
    RawDpiX = property(get_RawDpiX, None)
    RawDpiY = property(get_RawDpiY, None)
    StereoEnabled = property(get_StereoEnabled, None)
class IDisplayInformation2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4dcd0021-fad1-4b8e-8e-df-77-58-87-b8-bf-19')
    @winrt_commethod(6)
    def get_RawPixelsPerViewPixel(self) -> Double: ...
    RawPixelsPerViewPixel = property(get_RawPixelsPerViewPixel, None)
class IDisplayInformation3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('db15011d-0f09-4466-8f-f3-11-de-9a-3c-92-9a')
    @winrt_commethod(6)
    def get_DiagonalSizeInInches(self) -> Windows.Foundation.IReference[Double]: ...
    DiagonalSizeInInches = property(get_DiagonalSizeInInches, None)
class IDisplayInformation4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c972ce2f-1242-46be-b5-36-e1-aa-fe-9e-7a-cf')
    @winrt_commethod(6)
    def get_ScreenWidthInRawPixels(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ScreenHeightInRawPixels(self) -> UInt32: ...
    ScreenWidthInRawPixels = property(get_ScreenWidthInRawPixels, None)
    ScreenHeightInRawPixels = property(get_ScreenHeightInRawPixels, None)
class IDisplayInformation5(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3a5442dc-2cde-4a8d-80-d1-21-dc-5a-dc-c1-aa')
    @winrt_commethod(6)
    def GetAdvancedColorInfo(self) -> Windows.Graphics.Display.AdvancedColorInfo: ...
    @winrt_commethod(7)
    def add_AdvancedColorInfoChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_AdvancedColorInfoChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDisplayInformationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c6a02a6c-d452-44dc-ba-07-96-f3-c6-ad-f9-d1')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.Graphics.Display.DisplayInformation: ...
    @winrt_commethod(7)
    def get_AutoRotationPreferences(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(8)
    def put_AutoRotationPreferences(self, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_commethod(9)
    def add_DisplayContentsInvalidated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.DisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_DisplayContentsInvalidated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoRotationPreferences = property(get_AutoRotationPreferences, put_AutoRotationPreferences)
class IDisplayPropertiesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6937ed8d-30ea-4ded-82-71-45-53-ff-02-f6-8a')
    @winrt_commethod(6)
    def get_CurrentOrientation(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(7)
    def get_NativeOrientation(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(8)
    def get_AutoRotationPreferences(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(9)
    def put_AutoRotationPreferences(self, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_commethod(10)
    def add_OrientationChanged(self, handler: Windows.Graphics.Display.DisplayPropertiesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_OrientationChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_ResolutionScale(self) -> Windows.Graphics.Display.ResolutionScale: ...
    @winrt_commethod(13)
    def get_LogicalDpi(self) -> Single: ...
    @winrt_commethod(14)
    def add_LogicalDpiChanged(self, handler: Windows.Graphics.Display.DisplayPropertiesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_LogicalDpiChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_StereoEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def add_StereoEnabledChanged(self, handler: Windows.Graphics.Display.DisplayPropertiesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_StereoEnabledChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def GetColorProfileAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(20)
    def add_ColorProfileChanged(self, handler: Windows.Graphics.Display.DisplayPropertiesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_ColorProfileChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_DisplayContentsInvalidated(self, handler: Windows.Graphics.Display.DisplayPropertiesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_DisplayContentsInvalidated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentOrientation = property(get_CurrentOrientation, None)
    NativeOrientation = property(get_NativeOrientation, None)
    AutoRotationPreferences = property(get_AutoRotationPreferences, put_AutoRotationPreferences)
    ResolutionScale = property(get_ResolutionScale, None)
    LogicalDpi = property(get_LogicalDpi, None)
    StereoEnabled = property(get_StereoEnabled, None)
class IDisplayServices(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1b54f32b-890d-5747-bd-26-fd-bd-eb-0c-8a-71')
class IDisplayServicesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dc2096bf-730a-5560-b4-61-91-c1-3d-69-2e-0c')
    @winrt_commethod(6)
    def FindAll(self) -> POINTER(Windows.Graphics.DisplayId_head): ...
class NitRange(EasyCastStructure):
    MinNits: Single
    MaxNits: Single
    StepSizeNits: Single
ResolutionScale = Int32
ResolutionScale_Invalid: ResolutionScale = 0
ResolutionScale_Scale100Percent: ResolutionScale = 100
ResolutionScale_Scale120Percent: ResolutionScale = 120
ResolutionScale_Scale125Percent: ResolutionScale = 125
ResolutionScale_Scale140Percent: ResolutionScale = 140
ResolutionScale_Scale150Percent: ResolutionScale = 150
ResolutionScale_Scale160Percent: ResolutionScale = 160
ResolutionScale_Scale175Percent: ResolutionScale = 175
ResolutionScale_Scale180Percent: ResolutionScale = 180
ResolutionScale_Scale200Percent: ResolutionScale = 200
ResolutionScale_Scale225Percent: ResolutionScale = 225
ResolutionScale_Scale250Percent: ResolutionScale = 250
ResolutionScale_Scale300Percent: ResolutionScale = 300
ResolutionScale_Scale350Percent: ResolutionScale = 350
ResolutionScale_Scale400Percent: ResolutionScale = 400
ResolutionScale_Scale450Percent: ResolutionScale = 450
ResolutionScale_Scale500Percent: ResolutionScale = 500
make_head(_module, 'AdvancedColorInfo')
make_head(_module, 'BrightnessOverride')
make_head(_module, 'BrightnessOverrideSettings')
make_head(_module, 'ColorOverrideSettings')
make_head(_module, 'DisplayEnhancementOverride')
make_head(_module, 'DisplayEnhancementOverrideCapabilities')
make_head(_module, 'DisplayEnhancementOverrideCapabilitiesChangedEventArgs')
make_head(_module, 'DisplayInformation')
make_head(_module, 'DisplayProperties')
make_head(_module, 'DisplayPropertiesEventHandler')
make_head(_module, 'DisplayServices')
make_head(_module, 'IAdvancedColorInfo')
make_head(_module, 'IBrightnessOverride')
make_head(_module, 'IBrightnessOverrideSettings')
make_head(_module, 'IBrightnessOverrideSettingsStatics')
make_head(_module, 'IBrightnessOverrideStatics')
make_head(_module, 'IColorOverrideSettings')
make_head(_module, 'IColorOverrideSettingsStatics')
make_head(_module, 'IDisplayEnhancementOverride')
make_head(_module, 'IDisplayEnhancementOverrideCapabilities')
make_head(_module, 'IDisplayEnhancementOverrideCapabilitiesChangedEventArgs')
make_head(_module, 'IDisplayEnhancementOverrideStatics')
make_head(_module, 'IDisplayInformation')
make_head(_module, 'IDisplayInformation2')
make_head(_module, 'IDisplayInformation3')
make_head(_module, 'IDisplayInformation4')
make_head(_module, 'IDisplayInformation5')
make_head(_module, 'IDisplayInformationStatics')
make_head(_module, 'IDisplayPropertiesStatics')
make_head(_module, 'IDisplayServices')
make_head(_module, 'IDisplayServicesStatics')
make_head(_module, 'NitRange')
