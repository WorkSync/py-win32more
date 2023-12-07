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
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.Casting
import win32more.Windows.Storage.Streams
import win32more.Windows.UI.Popups
class CastingConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Casting.ICastingConnection
    _classid_ = 'Windows.Media.Casting.CastingConnection'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.Casting.ICastingConnection) -> win32more.Windows.Media.Casting.CastingConnectionState: ...
    @winrt_mixinmethod
    def get_Device(self: win32more.Windows.Media.Casting.ICastingConnection) -> win32more.Windows.Media.Casting.CastingDevice: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Media.Casting.ICastingConnection) -> win32more.Windows.Media.Casting.CastingSource: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Windows.Media.Casting.ICastingConnection, value: win32more.Windows.Media.Casting.CastingSource) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Media.Casting.ICastingConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Casting.CastingConnection, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Media.Casting.ICastingConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ErrorOccurred(self: win32more.Windows.Media.Casting.ICastingConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Casting.CastingConnection, win32more.Windows.Media.Casting.CastingConnectionErrorOccurredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ErrorOccurred(self: win32more.Windows.Media.Casting.ICastingConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RequestStartCastingAsync(self: win32more.Windows.Media.Casting.ICastingConnection, value: win32more.Windows.Media.Casting.CastingSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Casting.CastingConnectionErrorStatus]: ...
    @winrt_mixinmethod
    def DisconnectAsync(self: win32more.Windows.Media.Casting.ICastingConnection) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Casting.CastingConnectionErrorStatus]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    State = property(get_State, None)
    Device = property(get_Device, None)
    Source = property(get_Source, put_Source)
class CastingConnectionErrorOccurredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Casting.ICastingConnectionErrorOccurredEventArgs
    _classid_ = 'Windows.Media.Casting.CastingConnectionErrorOccurredEventArgs'
    @winrt_mixinmethod
    def get_ErrorStatus(self: win32more.Windows.Media.Casting.ICastingConnectionErrorOccurredEventArgs) -> win32more.Windows.Media.Casting.CastingConnectionErrorStatus: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.Media.Casting.ICastingConnectionErrorOccurredEventArgs) -> WinRT_String: ...
    ErrorStatus = property(get_ErrorStatus, None)
    Message = property(get_Message, None)
CastingConnectionErrorStatus = Int32
CastingConnectionErrorStatus_Succeeded: CastingConnectionErrorStatus = 0
CastingConnectionErrorStatus_DeviceDidNotRespond: CastingConnectionErrorStatus = 1
CastingConnectionErrorStatus_DeviceError: CastingConnectionErrorStatus = 2
CastingConnectionErrorStatus_DeviceLocked: CastingConnectionErrorStatus = 3
CastingConnectionErrorStatus_ProtectedPlaybackFailed: CastingConnectionErrorStatus = 4
CastingConnectionErrorStatus_InvalidCastingSource: CastingConnectionErrorStatus = 5
CastingConnectionErrorStatus_Unknown: CastingConnectionErrorStatus = 6
CastingConnectionState = Int32
CastingConnectionState_Disconnected: CastingConnectionState = 0
CastingConnectionState_Connected: CastingConnectionState = 1
CastingConnectionState_Rendering: CastingConnectionState = 2
CastingConnectionState_Disconnecting: CastingConnectionState = 3
CastingConnectionState_Connecting: CastingConnectionState = 4
class CastingDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Casting.ICastingDevice
    _classid_ = 'Windows.Media.Casting.CastingDevice'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Casting.ICastingDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.Media.Casting.ICastingDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Icon(self: win32more.Windows.Media.Casting.ICastingDevice) -> win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_mixinmethod
    def GetSupportedCastingPlaybackTypesAsync(self: win32more.Windows.Media.Casting.ICastingDevice) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Casting.CastingPlaybackTypes]: ...
    @winrt_mixinmethod
    def CreateCastingConnection(self: win32more.Windows.Media.Casting.ICastingDevice) -> win32more.Windows.Media.Casting.CastingConnection: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Media.Casting.ICastingDeviceStatics, type: win32more.Windows.Media.Casting.CastingPlaybackTypes) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromCastingSourceAsync(cls: win32more.Windows.Media.Casting.ICastingDeviceStatics, castingSource: win32more.Windows.Media.Casting.CastingSource) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Media.Casting.ICastingDeviceStatics, value: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Casting.CastingDevice]: ...
    @winrt_classmethod
    def DeviceInfoSupportsCastingAsync(cls: win32more.Windows.Media.Casting.ICastingDeviceStatics, device: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    Id = property(get_Id, None)
    FriendlyName = property(get_FriendlyName, None)
    Icon = property(get_Icon, None)
class CastingDevicePicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Casting.ICastingDevicePicker
    _classid_ = 'Windows.Media.Casting.CastingDevicePicker'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Media.Casting.CastingDevicePicker.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Casting.CastingDevicePicker: ...
    @winrt_mixinmethod
    def get_Filter(self: win32more.Windows.Media.Casting.ICastingDevicePicker) -> win32more.Windows.Media.Casting.CastingDevicePickerFilter: ...
    @winrt_mixinmethod
    def get_Appearance(self: win32more.Windows.Media.Casting.ICastingDevicePicker) -> win32more.Windows.Devices.Enumeration.DevicePickerAppearance: ...
    @winrt_mixinmethod
    def add_CastingDeviceSelected(self: win32more.Windows.Media.Casting.ICastingDevicePicker, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Casting.CastingDevicePicker, win32more.Windows.Media.Casting.CastingDeviceSelectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CastingDeviceSelected(self: win32more.Windows.Media.Casting.ICastingDevicePicker, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CastingDevicePickerDismissed(self: win32more.Windows.Media.Casting.ICastingDevicePicker, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Casting.CastingDevicePicker, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CastingDevicePickerDismissed(self: win32more.Windows.Media.Casting.ICastingDevicePicker, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Show(self: win32more.Windows.Media.Casting.ICastingDevicePicker, selection: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def ShowWithPlacement(self: win32more.Windows.Media.Casting.ICastingDevicePicker, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> Void: ...
    @winrt_mixinmethod
    def Hide(self: win32more.Windows.Media.Casting.ICastingDevicePicker) -> Void: ...
    Filter = property(get_Filter, None)
    Appearance = property(get_Appearance, None)
class CastingDevicePickerFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Casting.ICastingDevicePickerFilter
    _classid_ = 'Windows.Media.Casting.CastingDevicePickerFilter'
    @winrt_mixinmethod
    def get_SupportsAudio(self: win32more.Windows.Media.Casting.ICastingDevicePickerFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_SupportsAudio(self: win32more.Windows.Media.Casting.ICastingDevicePickerFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportsVideo(self: win32more.Windows.Media.Casting.ICastingDevicePickerFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_SupportsVideo(self: win32more.Windows.Media.Casting.ICastingDevicePickerFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportsPictures(self: win32more.Windows.Media.Casting.ICastingDevicePickerFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_SupportsPictures(self: win32more.Windows.Media.Casting.ICastingDevicePickerFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedCastingSources(self: win32more.Windows.Media.Casting.ICastingDevicePickerFilter) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Casting.CastingSource]: ...
    SupportsAudio = property(get_SupportsAudio, put_SupportsAudio)
    SupportsVideo = property(get_SupportsVideo, put_SupportsVideo)
    SupportsPictures = property(get_SupportsPictures, put_SupportsPictures)
    SupportedCastingSources = property(get_SupportedCastingSources, None)
class CastingDeviceSelectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Casting.ICastingDeviceSelectedEventArgs
    _classid_ = 'Windows.Media.Casting.CastingDeviceSelectedEventArgs'
    @winrt_mixinmethod
    def get_SelectedCastingDevice(self: win32more.Windows.Media.Casting.ICastingDeviceSelectedEventArgs) -> win32more.Windows.Media.Casting.CastingDevice: ...
    SelectedCastingDevice = property(get_SelectedCastingDevice, None)
CastingPlaybackTypes = UInt32
CastingPlaybackTypes_None: CastingPlaybackTypes = 0
CastingPlaybackTypes_Audio: CastingPlaybackTypes = 1
CastingPlaybackTypes_Video: CastingPlaybackTypes = 2
CastingPlaybackTypes_Picture: CastingPlaybackTypes = 4
class CastingSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Casting.ICastingSource
    _classid_ = 'Windows.Media.Casting.CastingSource'
    @winrt_mixinmethod
    def get_PreferredSourceUri(self: win32more.Windows.Media.Casting.ICastingSource) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_PreferredSourceUri(self: win32more.Windows.Media.Casting.ICastingSource, value: win32more.Windows.Foundation.Uri) -> Void: ...
    PreferredSourceUri = property(get_PreferredSourceUri, put_PreferredSourceUri)
class ICastingConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingConnection'
    _iid_ = Guid('{cd951653-c2f1-4498-8b78-5fb4cd3640dd}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.Media.Casting.CastingConnectionState: ...
    @winrt_commethod(7)
    def get_Device(self) -> win32more.Windows.Media.Casting.CastingDevice: ...
    @winrt_commethod(8)
    def get_Source(self) -> win32more.Windows.Media.Casting.CastingSource: ...
    @winrt_commethod(9)
    def put_Source(self, value: win32more.Windows.Media.Casting.CastingSource) -> Void: ...
    @winrt_commethod(10)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Casting.CastingConnection, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_ErrorOccurred(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Casting.CastingConnection, win32more.Windows.Media.Casting.CastingConnectionErrorOccurredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ErrorOccurred(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def RequestStartCastingAsync(self, value: win32more.Windows.Media.Casting.CastingSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Casting.CastingConnectionErrorStatus]: ...
    @winrt_commethod(15)
    def DisconnectAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Casting.CastingConnectionErrorStatus]: ...
    State = property(get_State, None)
    Device = property(get_Device, None)
    Source = property(get_Source, put_Source)
class ICastingConnectionErrorOccurredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingConnectionErrorOccurredEventArgs'
    _iid_ = Guid('{a7fb3c69-8719-4f00-81fb-961863c79a32}')
    @winrt_commethod(6)
    def get_ErrorStatus(self) -> win32more.Windows.Media.Casting.CastingConnectionErrorStatus: ...
    @winrt_commethod(7)
    def get_Message(self) -> WinRT_String: ...
    ErrorStatus = property(get_ErrorStatus, None)
    Message = property(get_Message, None)
class ICastingDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingDevice'
    _iid_ = Guid('{de721c83-4a43-4ad1-a6d2-2492a796c3f2}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Icon(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_commethod(9)
    def GetSupportedCastingPlaybackTypesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Casting.CastingPlaybackTypes]: ...
    @winrt_commethod(10)
    def CreateCastingConnection(self) -> win32more.Windows.Media.Casting.CastingConnection: ...
    Id = property(get_Id, None)
    FriendlyName = property(get_FriendlyName, None)
    Icon = property(get_Icon, None)
class ICastingDevicePicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingDevicePicker'
    _iid_ = Guid('{dcd39924-0591-49be-aacb-4b82ee756a95}')
    @winrt_commethod(6)
    def get_Filter(self) -> win32more.Windows.Media.Casting.CastingDevicePickerFilter: ...
    @winrt_commethod(7)
    def get_Appearance(self) -> win32more.Windows.Devices.Enumeration.DevicePickerAppearance: ...
    @winrt_commethod(8)
    def add_CastingDeviceSelected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Casting.CastingDevicePicker, win32more.Windows.Media.Casting.CastingDeviceSelectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CastingDeviceSelected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_CastingDevicePickerDismissed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Casting.CastingDevicePicker, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_CastingDevicePickerDismissed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def Show(self, selection: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(13)
    def ShowWithPlacement(self, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> Void: ...
    @winrt_commethod(14)
    def Hide(self) -> Void: ...
    Filter = property(get_Filter, None)
    Appearance = property(get_Appearance, None)
class ICastingDevicePickerFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingDevicePickerFilter'
    _iid_ = Guid('{be8c619c-b563-4354-ae33-9fdaad8c6291}')
    @winrt_commethod(6)
    def get_SupportsAudio(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SupportsAudio(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_SupportsVideo(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_SupportsVideo(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_SupportsPictures(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_SupportsPictures(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_SupportedCastingSources(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Casting.CastingSource]: ...
    SupportsAudio = property(get_SupportsAudio, put_SupportsAudio)
    SupportsVideo = property(get_SupportsVideo, put_SupportsVideo)
    SupportsPictures = property(get_SupportsPictures, put_SupportsPictures)
    SupportedCastingSources = property(get_SupportedCastingSources, None)
class ICastingDeviceSelectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingDeviceSelectedEventArgs'
    _iid_ = Guid('{dc439e86-dd57-4d0d-9400-af45e4fb3663}')
    @winrt_commethod(6)
    def get_SelectedCastingDevice(self) -> win32more.Windows.Media.Casting.CastingDevice: ...
    SelectedCastingDevice = property(get_SelectedCastingDevice, None)
class ICastingDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingDeviceStatics'
    _iid_ = Guid('{e7d958d7-4d13-4237-a365-4c4f6a4cfd2f}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, type: win32more.Windows.Media.Casting.CastingPlaybackTypes) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromCastingSourceAsync(self, castingSource: win32more.Windows.Media.Casting.CastingSource) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(8)
    def FromIdAsync(self, value: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Casting.CastingDevice]: ...
    @winrt_commethod(9)
    def DeviceInfoSupportsCastingAsync(self, device: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class ICastingSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingSource'
    _iid_ = Guid('{f429ea72-3467-47e6-a027-522923e9d727}')
    @winrt_commethod(6)
    def get_PreferredSourceUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_PreferredSourceUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    PreferredSourceUri = property(get_PreferredSourceUri, put_PreferredSourceUri)
make_ready(__name__)
