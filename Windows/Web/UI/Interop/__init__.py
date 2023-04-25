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
import Windows.ApplicationModel.DataTransfer
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage.Streams
import Windows.System
import Windows.UI
import Windows.UI.Core
import Windows.Web
import Windows.Web.Http
import Windows.Web.UI
import Windows.Web.UI.Interop
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWebViewControlAcceleratorKeyPressedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('77a2a53e-7c74-437d-a2-90-3a-c0-d8-cd-56-55')
    @winrt_commethod(6)
    def get_EventType(self) -> Windows.UI.Core.CoreAcceleratorKeyEventType: ...
    @winrt_commethod(7)
    def get_VirtualKey(self) -> Windows.System.VirtualKey: ...
    @winrt_commethod(8)
    def get_KeyStatus(self) -> Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_commethod(9)
    def get_RoutingStage(self) -> Windows.Web.UI.Interop.WebViewControlAcceleratorKeyRoutingStage: ...
    @winrt_commethod(10)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_Handled(self, value: Boolean) -> Void: ...
    EventType = property(get_EventType, None)
    VirtualKey = property(get_VirtualKey, None)
    KeyStatus = property(get_KeyStatus, None)
    RoutingStage = property(get_RoutingStage, None)
    Handled = property(get_Handled, put_Handled)
class IWebViewControlMoveFocusRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6b2a340d-4bd0-405e-b7-c1-1e-72-a4-92-f4-46')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.Web.UI.Interop.WebViewControlMoveFocusReason: ...
    Reason = property(get_Reason, None)
class IWebViewControlProcess(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('02c723ec-98d6-424a-b6-3e-c6-13-6c-36-a0-f2')
    @winrt_commethod(6)
    def get_ProcessId(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_EnterpriseId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsPrivateNetworkClientServerCapabilityEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def CreateWebViewControlAsync(self, hostWindowHandle: Int64, bounds: Windows.Foundation.Rect) -> Windows.Foundation.IAsyncOperation[Windows.Web.UI.Interop.WebViewControl]: ...
    @winrt_commethod(10)
    def GetWebViewControls(self) -> Windows.Foundation.Collections.IVectorView[Windows.Web.UI.Interop.WebViewControl]: ...
    @winrt_commethod(11)
    def Terminate(self) -> Void: ...
    @winrt_commethod(12)
    def add_ProcessExited(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.Interop.WebViewControlProcess, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ProcessExited(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ProcessId = property(get_ProcessId, None)
    EnterpriseId = property(get_EnterpriseId, None)
    IsPrivateNetworkClientServerCapabilityEnabled = property(get_IsPrivateNetworkClientServerCapabilityEnabled, None)
class IWebViewControlProcessFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('47b65cf9-a2d2-453c-b0-97-f6-77-9d-4b-8e-02')
    @winrt_commethod(6)
    def CreateWithOptions(self, processOptions: Windows.Web.UI.Interop.WebViewControlProcessOptions) -> Windows.Web.UI.Interop.WebViewControlProcess: ...
class IWebViewControlProcessOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1cca72a7-3bd6-4826-82-61-6c-81-89-50-5d-89')
    @winrt_commethod(6)
    def put_EnterpriseId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_EnterpriseId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_PrivateNetworkClientServerCapability(self, value: Windows.Web.UI.Interop.WebViewControlProcessCapabilityState) -> Void: ...
    @winrt_commethod(9)
    def get_PrivateNetworkClientServerCapability(self) -> Windows.Web.UI.Interop.WebViewControlProcessCapabilityState: ...
    EnterpriseId = property(get_EnterpriseId, put_EnterpriseId)
    PrivateNetworkClientServerCapability = property(get_PrivateNetworkClientServerCapability, put_PrivateNetworkClientServerCapability)
class IWebViewControlSite(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('133f47c6-12dc-4898-bd-47-04-96-7d-e6-48-ba')
    @winrt_commethod(6)
    def get_Process(self) -> Windows.Web.UI.Interop.WebViewControlProcess: ...
    @winrt_commethod(7)
    def put_Scale(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_Scale(self) -> Double: ...
    @winrt_commethod(9)
    def put_Bounds(self, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(10)
    def get_Bounds(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def put_IsVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsVisible(self) -> Boolean: ...
    @winrt_commethod(13)
    def Close(self) -> Void: ...
    @winrt_commethod(14)
    def MoveFocus(self, reason: Windows.Web.UI.Interop.WebViewControlMoveFocusReason) -> Void: ...
    @winrt_commethod(15)
    def add_MoveFocusRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.Interop.WebViewControl, Windows.Web.UI.Interop.WebViewControlMoveFocusRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_MoveFocusRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_AcceleratorKeyPressed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.Interop.WebViewControl, Windows.Web.UI.Interop.WebViewControlAcceleratorKeyPressedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_AcceleratorKeyPressed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Process = property(get_Process, None)
    Scale = property(get_Scale, put_Scale)
    Bounds = property(get_Bounds, put_Bounds)
    IsVisible = property(get_IsVisible, put_IsVisible)
class IWebViewControlSite2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d13b2e3f-48ee-4730-82-43-d2-ed-0c-05-60-6a')
    @winrt_commethod(6)
    def add_GotFocus(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.Interop.WebViewControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_GotFocus(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_LostFocus(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.Interop.WebViewControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_LostFocus(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class WebViewControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Web.UI.Interop.WebViewControl'
    @winrt_mixinmethod
    def get_Source(self: Windows.Web.UI.IWebViewControl) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Source(self: Windows.Web.UI.IWebViewControl, source: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_DocumentTitle(self: Windows.Web.UI.IWebViewControl) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CanGoBack(self: Windows.Web.UI.IWebViewControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanGoForward(self: Windows.Web.UI.IWebViewControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_DefaultBackgroundColor(self: Windows.Web.UI.IWebViewControl, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultBackgroundColor(self: Windows.Web.UI.IWebViewControl) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_ContainsFullScreenElement(self: Windows.Web.UI.IWebViewControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Settings(self: Windows.Web.UI.IWebViewControl) -> Windows.Web.UI.WebViewControlSettings: ...
    @winrt_mixinmethod
    def get_DeferredPermissionRequests(self: Windows.Web.UI.IWebViewControl) -> Windows.Foundation.Collections.IVectorView[Windows.Web.UI.WebViewControlDeferredPermissionRequest]: ...
    @winrt_mixinmethod
    def GoForward(self: Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def GoBack(self: Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def Refresh(self: Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def Navigate(self: Windows.Web.UI.IWebViewControl, source: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def NavigateToString(self: Windows.Web.UI.IWebViewControl, text: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def NavigateToLocalStreamUri(self: Windows.Web.UI.IWebViewControl, source: Windows.Foundation.Uri, streamResolver: Windows.Web.IUriToStreamResolver) -> Void: ...
    @winrt_mixinmethod
    def NavigateWithHttpRequestMessage(self: Windows.Web.UI.IWebViewControl, requestMessage: Windows.Web.Http.HttpRequestMessage) -> Void: ...
    @winrt_mixinmethod
    def InvokeScriptAsync(self: Windows.Web.UI.IWebViewControl, scriptName: WinRT_String, arguments: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def CapturePreviewToStreamAsync(self: Windows.Web.UI.IWebViewControl, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CaptureSelectedContentToDataPackageAsync(self: Windows.Web.UI.IWebViewControl) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.DataTransfer.DataPackage]: ...
    @winrt_mixinmethod
    def BuildLocalStreamUri(self: Windows.Web.UI.IWebViewControl, contentIdentifier: WinRT_String, relativePath: WinRT_String) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def GetDeferredPermissionRequestById(self: Windows.Web.UI.IWebViewControl, id: UInt32, result: POINTER(Windows.Web.UI.WebViewControlDeferredPermissionRequest)) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationStarting(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNavigationStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationStarting(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContentLoading(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlContentLoadingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentLoading(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DOMContentLoaded(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DOMContentLoaded(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationCompleted(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNavigationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationCompleted(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameNavigationStarting(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNavigationStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameNavigationStarting(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameContentLoading(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlContentLoadingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameContentLoading(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameDOMContentLoaded(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameDOMContentLoaded(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameNavigationCompleted(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNavigationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameNavigationCompleted(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScriptNotify(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlScriptNotifyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScriptNotify(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LongRunningScriptDetected(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlLongRunningScriptDetectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LongRunningScriptDetected(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnsafeContentWarningDisplaying(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnsafeContentWarningDisplaying(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnviewableContentIdentified(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlUnviewableContentIdentifiedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnviewableContentIdentified(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PermissionRequested(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlPermissionRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PermissionRequested(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnsupportedUriSchemeIdentified(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlUnsupportedUriSchemeIdentifiedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnsupportedUriSchemeIdentified(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NewWindowRequested(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNewWindowRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NewWindowRequested(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContainsFullScreenElementChanged(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContainsFullScreenElementChanged(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WebResourceRequested(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlWebResourceRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WebResourceRequested(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Process(self: Windows.Web.UI.Interop.IWebViewControlSite) -> Windows.Web.UI.Interop.WebViewControlProcess: ...
    @winrt_mixinmethod
    def put_Scale(self: Windows.Web.UI.Interop.IWebViewControlSite, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: Windows.Web.UI.Interop.IWebViewControlSite) -> Double: ...
    @winrt_mixinmethod
    def put_Bounds(self: Windows.Web.UI.Interop.IWebViewControlSite, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_Bounds(self: Windows.Web.UI.Interop.IWebViewControlSite) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_IsVisible(self: Windows.Web.UI.Interop.IWebViewControlSite, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsVisible(self: Windows.Web.UI.Interop.IWebViewControlSite) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: Windows.Web.UI.Interop.IWebViewControlSite) -> Void: ...
    @winrt_mixinmethod
    def MoveFocus(self: Windows.Web.UI.Interop.IWebViewControlSite, reason: Windows.Web.UI.Interop.WebViewControlMoveFocusReason) -> Void: ...
    @winrt_mixinmethod
    def add_MoveFocusRequested(self: Windows.Web.UI.Interop.IWebViewControlSite, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.Interop.WebViewControl, Windows.Web.UI.Interop.WebViewControlMoveFocusRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MoveFocusRequested(self: Windows.Web.UI.Interop.IWebViewControlSite, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AcceleratorKeyPressed(self: Windows.Web.UI.Interop.IWebViewControlSite, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.Interop.WebViewControl, Windows.Web.UI.Interop.WebViewControlAcceleratorKeyPressedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AcceleratorKeyPressed(self: Windows.Web.UI.Interop.IWebViewControlSite, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddInitializeScript(self: Windows.Web.UI.IWebViewControl2, script: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_GotFocus(self: Windows.Web.UI.Interop.IWebViewControlSite2, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.Interop.WebViewControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GotFocus(self: Windows.Web.UI.Interop.IWebViewControlSite2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LostFocus(self: Windows.Web.UI.Interop.IWebViewControlSite2, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.Interop.WebViewControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LostFocus(self: Windows.Web.UI.Interop.IWebViewControlSite2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Source = property(get_Source, put_Source)
    DocumentTitle = property(get_DocumentTitle, None)
    CanGoBack = property(get_CanGoBack, None)
    CanGoForward = property(get_CanGoForward, None)
    DefaultBackgroundColor = property(get_DefaultBackgroundColor, put_DefaultBackgroundColor)
    ContainsFullScreenElement = property(get_ContainsFullScreenElement, None)
    Settings = property(get_Settings, None)
    DeferredPermissionRequests = property(get_DeferredPermissionRequests, None)
    Process = property(get_Process, None)
    Scale = property(get_Scale, put_Scale)
    Bounds = property(get_Bounds, put_Bounds)
    IsVisible = property(get_IsVisible, put_IsVisible)
class WebViewControlAcceleratorKeyPressedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Web.UI.Interop.WebViewControlAcceleratorKeyPressedEventArgs'
    @winrt_mixinmethod
    def get_EventType(self: Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs) -> Windows.UI.Core.CoreAcceleratorKeyEventType: ...
    @winrt_mixinmethod
    def get_VirtualKey(self: Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs) -> Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs) -> Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_RoutingStage(self: Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs) -> Windows.Web.UI.Interop.WebViewControlAcceleratorKeyRoutingStage: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs, value: Boolean) -> Void: ...
    EventType = property(get_EventType, None)
    VirtualKey = property(get_VirtualKey, None)
    KeyStatus = property(get_KeyStatus, None)
    RoutingStage = property(get_RoutingStage, None)
    Handled = property(get_Handled, put_Handled)
WebViewControlAcceleratorKeyRoutingStage = Int32
WebViewControlAcceleratorKeyRoutingStage_Tunneling: WebViewControlAcceleratorKeyRoutingStage = 0
WebViewControlAcceleratorKeyRoutingStage_Bubbling: WebViewControlAcceleratorKeyRoutingStage = 1
WebViewControlMoveFocusReason = Int32
WebViewControlMoveFocusReason_Programmatic: WebViewControlMoveFocusReason = 0
WebViewControlMoveFocusReason_Next: WebViewControlMoveFocusReason = 1
WebViewControlMoveFocusReason_Previous: WebViewControlMoveFocusReason = 2
class WebViewControlMoveFocusRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Web.UI.Interop.WebViewControlMoveFocusRequestedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: Windows.Web.UI.Interop.IWebViewControlMoveFocusRequestedEventArgs) -> Windows.Web.UI.Interop.WebViewControlMoveFocusReason: ...
    Reason = property(get_Reason, None)
class WebViewControlProcess(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Web.UI.Interop.WebViewControlProcess'
    @winrt_factorymethod
    def CreateWithOptions(cls: Windows.Web.UI.Interop.IWebViewControlProcessFactory, processOptions: Windows.Web.UI.Interop.WebViewControlProcessOptions) -> Windows.Web.UI.Interop.WebViewControlProcess: ...
    @winrt_activatemethod
    def New(cls) -> Windows.Web.UI.Interop.WebViewControlProcess: ...
    @winrt_mixinmethod
    def get_ProcessId(self: Windows.Web.UI.Interop.IWebViewControlProcess) -> UInt32: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: Windows.Web.UI.Interop.IWebViewControlProcess) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsPrivateNetworkClientServerCapabilityEnabled(self: Windows.Web.UI.Interop.IWebViewControlProcess) -> Boolean: ...
    @winrt_mixinmethod
    def CreateWebViewControlAsync(self: Windows.Web.UI.Interop.IWebViewControlProcess, hostWindowHandle: Int64, bounds: Windows.Foundation.Rect) -> Windows.Foundation.IAsyncOperation[Windows.Web.UI.Interop.WebViewControl]: ...
    @winrt_mixinmethod
    def GetWebViewControls(self: Windows.Web.UI.Interop.IWebViewControlProcess) -> Windows.Foundation.Collections.IVectorView[Windows.Web.UI.Interop.WebViewControl]: ...
    @winrt_mixinmethod
    def Terminate(self: Windows.Web.UI.Interop.IWebViewControlProcess) -> Void: ...
    @winrt_mixinmethod
    def add_ProcessExited(self: Windows.Web.UI.Interop.IWebViewControlProcess, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.Interop.WebViewControlProcess, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProcessExited(self: Windows.Web.UI.Interop.IWebViewControlProcess, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ProcessId = property(get_ProcessId, None)
    EnterpriseId = property(get_EnterpriseId, None)
    IsPrivateNetworkClientServerCapabilityEnabled = property(get_IsPrivateNetworkClientServerCapabilityEnabled, None)
WebViewControlProcessCapabilityState = Int32
WebViewControlProcessCapabilityState_Default: WebViewControlProcessCapabilityState = 0
WebViewControlProcessCapabilityState_Disabled: WebViewControlProcessCapabilityState = 1
WebViewControlProcessCapabilityState_Enabled: WebViewControlProcessCapabilityState = 2
class WebViewControlProcessOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Web.UI.Interop.WebViewControlProcessOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.Web.UI.Interop.WebViewControlProcessOptions: ...
    @winrt_mixinmethod
    def put_EnterpriseId(self: Windows.Web.UI.Interop.IWebViewControlProcessOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: Windows.Web.UI.Interop.IWebViewControlProcessOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PrivateNetworkClientServerCapability(self: Windows.Web.UI.Interop.IWebViewControlProcessOptions, value: Windows.Web.UI.Interop.WebViewControlProcessCapabilityState) -> Void: ...
    @winrt_mixinmethod
    def get_PrivateNetworkClientServerCapability(self: Windows.Web.UI.Interop.IWebViewControlProcessOptions) -> Windows.Web.UI.Interop.WebViewControlProcessCapabilityState: ...
    EnterpriseId = property(get_EnterpriseId, put_EnterpriseId)
    PrivateNetworkClientServerCapability = property(get_PrivateNetworkClientServerCapability, put_PrivateNetworkClientServerCapability)
make_head(_module, 'IWebViewControlAcceleratorKeyPressedEventArgs')
make_head(_module, 'IWebViewControlMoveFocusRequestedEventArgs')
make_head(_module, 'IWebViewControlProcess')
make_head(_module, 'IWebViewControlProcessFactory')
make_head(_module, 'IWebViewControlProcessOptions')
make_head(_module, 'IWebViewControlSite')
make_head(_module, 'IWebViewControlSite2')
make_head(_module, 'WebViewControl')
make_head(_module, 'WebViewControlAcceleratorKeyPressedEventArgs')
make_head(_module, 'WebViewControlMoveFocusRequestedEventArgs')
make_head(_module, 'WebViewControlProcess')
make_head(_module, 'WebViewControlProcessOptions')
