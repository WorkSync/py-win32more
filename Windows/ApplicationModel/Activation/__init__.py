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
import Windows.ApplicationModel.Appointments.AppointmentsProvider
import Windows.ApplicationModel.Background
import Windows.ApplicationModel.Contacts
import Windows.ApplicationModel.DataTransfer.ShareTarget
import Windows.ApplicationModel.Search
import Windows.ApplicationModel.UserDataAccounts.Provider
import Windows.Devices.Enumeration
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Media.SpeechRecognition
import Windows.Security.Authentication.Web
import Windows.Security.Authentication.Web.Provider
import Windows.Storage
import Windows.Storage.Pickers.Provider
import Windows.Storage.Provider
import Windows.Storage.Search
import Windows.System
import Windows.UI.Notifications
import Windows.UI.ViewManagement
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ActivationKind = Int32
ActivationKind_Launch: ActivationKind = 0
ActivationKind_Search: ActivationKind = 1
ActivationKind_ShareTarget: ActivationKind = 2
ActivationKind_File: ActivationKind = 3
ActivationKind_Protocol: ActivationKind = 4
ActivationKind_FileOpenPicker: ActivationKind = 5
ActivationKind_FileSavePicker: ActivationKind = 6
ActivationKind_CachedFileUpdater: ActivationKind = 7
ActivationKind_ContactPicker: ActivationKind = 8
ActivationKind_Device: ActivationKind = 9
ActivationKind_PrintTaskSettings: ActivationKind = 10
ActivationKind_CameraSettings: ActivationKind = 11
ActivationKind_RestrictedLaunch: ActivationKind = 12
ActivationKind_AppointmentsProvider: ActivationKind = 13
ActivationKind_Contact: ActivationKind = 14
ActivationKind_LockScreenCall: ActivationKind = 15
ActivationKind_VoiceCommand: ActivationKind = 16
ActivationKind_LockScreen: ActivationKind = 17
ActivationKind_PickerReturned: ActivationKind = 1000
ActivationKind_WalletAction: ActivationKind = 1001
ActivationKind_PickFileContinuation: ActivationKind = 1002
ActivationKind_PickSaveFileContinuation: ActivationKind = 1003
ActivationKind_PickFolderContinuation: ActivationKind = 1004
ActivationKind_WebAuthenticationBrokerContinuation: ActivationKind = 1005
ActivationKind_WebAccountProvider: ActivationKind = 1006
ActivationKind_ComponentUI: ActivationKind = 1007
ActivationKind_ProtocolForResults: ActivationKind = 1009
ActivationKind_ToastNotification: ActivationKind = 1010
ActivationKind_Print3DWorkflow: ActivationKind = 1011
ActivationKind_DialReceiver: ActivationKind = 1012
ActivationKind_DevicePairing: ActivationKind = 1013
ActivationKind_UserDataAccountsProvider: ActivationKind = 1014
ActivationKind_FilePickerExperience: ActivationKind = 1015
ActivationKind_LockScreenComponent: ActivationKind = 1016
ActivationKind_ContactPanel: ActivationKind = 1017
ActivationKind_PrintWorkflowForegroundTask: ActivationKind = 1018
ActivationKind_GameUIProvider: ActivationKind = 1019
ActivationKind_StartupTask: ActivationKind = 1020
ActivationKind_CommandLineLaunch: ActivationKind = 1021
ActivationKind_BarcodeScannerProvider: ActivationKind = 1022
ActivationKind_PrintSupportJobUI: ActivationKind = 1023
ActivationKind_PrintSupportSettingsUI: ActivationKind = 1024
ActivationKind_PhoneCallActivation: ActivationKind = 1025
ActivationKind_VpnForeground: ActivationKind = 1026
ApplicationExecutionState = Int32
ApplicationExecutionState_NotRunning: ApplicationExecutionState = 0
ApplicationExecutionState_Running: ApplicationExecutionState = 1
ApplicationExecutionState_Suspended: ApplicationExecutionState = 2
ApplicationExecutionState_Terminated: ApplicationExecutionState = 3
ApplicationExecutionState_ClosedByUser: ApplicationExecutionState = 4
class AppointmentsProviderAddAppointmentActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.AppointmentsProviderAddAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_AddAppointmentOperation(self: Windows.ApplicationModel.Activation.IAppointmentsProviderAddAppointmentActivatedEventArgs) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.AddAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    AddAppointmentOperation = property(get_AddAppointmentOperation, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class AppointmentsProviderRemoveAppointmentActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.AppointmentsProviderRemoveAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_RemoveAppointmentOperation(self: Windows.ApplicationModel.Activation.IAppointmentsProviderRemoveAppointmentActivatedEventArgs) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.RemoveAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    RemoveAppointmentOperation = property(get_RemoveAppointmentOperation, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class AppointmentsProviderReplaceAppointmentActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.AppointmentsProviderReplaceAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_ReplaceAppointmentOperation(self: Windows.ApplicationModel.Activation.IAppointmentsProviderReplaceAppointmentActivatedEventArgs) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.ReplaceAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ReplaceAppointmentOperation = property(get_ReplaceAppointmentOperation, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class AppointmentsProviderShowAppointmentDetailsActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.AppointmentsProviderShowAppointmentDetailsActivatedEventArgs'
    @winrt_mixinmethod
    def get_InstanceStartDate(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_LocalId(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoamingId(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    InstanceStartDate = property(get_InstanceStartDate, None)
    LocalId = property(get_LocalId, None)
    RoamingId = property(get_RoamingId, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class AppointmentsProviderShowTimeFrameActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.AppointmentsProviderShowTimeFrameActivatedEventArgs'
    @winrt_mixinmethod
    def get_TimeToShow(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    TimeToShow = property(get_TimeToShow, None)
    Duration = property(get_Duration, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class BackgroundActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs'
    @winrt_mixinmethod
    def get_TaskInstance(self: Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs) -> Windows.ApplicationModel.Background.IBackgroundTaskInstance: ...
    TaskInstance = property(get_TaskInstance, None)
class BarcodeScannerPreviewActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.BarcodeScannerPreviewActivatedEventArgs'
    @winrt_mixinmethod
    def get_ConnectionId(self: Windows.ApplicationModel.Activation.IBarcodeScannerPreviewActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ConnectionId = property(get_ConnectionId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class CachedFileUpdaterActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.CachedFileUpdaterActivatedEventArgs'
    @winrt_mixinmethod
    def get_CachedFileUpdaterUI(self: Windows.ApplicationModel.Activation.ICachedFileUpdaterActivatedEventArgs) -> Windows.Storage.Provider.CachedFileUpdaterUI: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    CachedFileUpdaterUI = property(get_CachedFileUpdaterUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class CommandLineActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.CommandLineActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: Windows.ApplicationModel.Activation.ICommandLineActivatedEventArgs) -> Windows.ApplicationModel.Activation.CommandLineActivationOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Operation = property(get_Operation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class CommandLineActivationOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.CommandLineActivationOperation'
    @winrt_mixinmethod
    def get_Arguments(self: Windows.ApplicationModel.Activation.ICommandLineActivationOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CurrentDirectoryPath(self: Windows.ApplicationModel.Activation.ICommandLineActivationOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExitCode(self: Windows.ApplicationModel.Activation.ICommandLineActivationOperation, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ExitCode(self: Windows.ApplicationModel.Activation.ICommandLineActivationOperation) -> Int32: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Activation.ICommandLineActivationOperation) -> Windows.Foundation.Deferral: ...
    Arguments = property(get_Arguments, None)
    CurrentDirectoryPath = property(get_CurrentDirectoryPath, None)
    ExitCode = property(get_ExitCode, put_ExitCode)
class ContactPanelActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.ContactPanelActivatedEventArgs'
    @winrt_mixinmethod
    def get_ContactPanel(self: Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs) -> Windows.ApplicationModel.Contacts.ContactPanel: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ContactPanel = property(get_ContactPanel, None)
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class DeviceActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.DeviceActivatedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformationId(self: Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    DeviceInformationId = property(get_DeviceInformationId, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    User = property(get_User, None)
class DevicePairingActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.DevicePairingActivatedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformation(self: Windows.ApplicationModel.Activation.IDevicePairingActivatedEventArgs) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    DeviceInformation = property(get_DeviceInformation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class DialReceiverActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.DialReceiverActivatedEventArgs'
    @winrt_mixinmethod
    def get_AppName(self: Windows.ApplicationModel.Activation.IDialReceiverActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Arguments(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    AppName = property(get_AppName, None)
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    User = property(get_User, None)
class FileActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.FileActivatedEventArgs'
    @winrt_mixinmethod
    def get_Files(self: Windows.ApplicationModel.Activation.IFileActivatedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IFileActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_NeighboringFilesQuery(self: Windows.ApplicationModel.Activation.IFileActivatedEventArgsWithNeighboringFiles) -> Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IFileActivatedEventArgsWithCallerPackageFamilyName) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Files = property(get_Files, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    User = property(get_User, None)
class FileOpenPickerActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.FileOpenPickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_FileOpenPickerUI(self: Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs) -> Windows.Storage.Pickers.Provider.FileOpenPickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    FileOpenPickerUI = property(get_FileOpenPickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    User = property(get_User, None)
class FileOpenPickerContinuationEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.FileOpenPickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_Files(self: Windows.ApplicationModel.Activation.IFileOpenPickerContinuationEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Files = property(get_Files, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class FileSavePickerActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.FileSavePickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_FileSavePickerUI(self: Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs) -> Windows.Storage.Pickers.Provider.FileSavePickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    FileSavePickerUI = property(get_FileSavePickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    EnterpriseId = property(get_EnterpriseId, None)
    User = property(get_User, None)
class FileSavePickerContinuationEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.FileSavePickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_File(self: Windows.ApplicationModel.Activation.IFileSavePickerContinuationEventArgs) -> Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    File = property(get_File, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class FolderPickerContinuationEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.FolderPickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_Folder(self: Windows.ApplicationModel.Activation.IFolderPickerContinuationEventArgs) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Folder = property(get_Folder, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class IActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cf651713-cd08-4fd8-b6-97-a2-81-b6-54-4e-2e')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_commethod(7)
    def get_PreviousExecutionState(self) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_commethod(8)
    def get_SplashScreen(self) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class IActivatedEventArgsWithUser(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1cf09b9e-9962-4936-80-ff-af-c8-e8-ae-5c-8c')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    User = property(get_User, None)
class IApplicationViewActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('930cef4b-b829-40fc-88-f4-85-13-e8-a6-47-38')
    @winrt_commethod(6)
    def get_CurrentlyShownApplicationViewId(self) -> Int32: ...
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
class IAppointmentsProviderActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3364c405-933c-4e7d-a0-34-50-0f-b8-dc-d9-f3')
    @winrt_commethod(6)
    def get_Verb(self) -> WinRT_String: ...
    Verb = property(get_Verb, None)
class IAppointmentsProviderAddAppointmentActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a2861367-cee5-4e4d-9e-d7-41-c3-4e-c1-8b-02')
    @winrt_commethod(6)
    def get_AddAppointmentOperation(self) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.AddAppointmentOperation: ...
    AddAppointmentOperation = property(get_AddAppointmentOperation, None)
class IAppointmentsProviderRemoveAppointmentActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('751f3ab8-0b8e-451c-9f-15-96-6e-69-9b-ac-25')
    @winrt_commethod(6)
    def get_RemoveAppointmentOperation(self) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.RemoveAppointmentOperation: ...
    RemoveAppointmentOperation = property(get_RemoveAppointmentOperation, None)
class IAppointmentsProviderReplaceAppointmentActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1551b7d4-a981-4067-8a-62-05-24-e4-ad-e1-21')
    @winrt_commethod(6)
    def get_ReplaceAppointmentOperation(self) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.ReplaceAppointmentOperation: ...
    ReplaceAppointmentOperation = property(get_ReplaceAppointmentOperation, None)
class IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3958f065-9841-4ca5-99-9b-88-51-98-b9-ef-2a')
    @winrt_commethod(6)
    def get_InstanceStartDate(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(7)
    def get_LocalId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RoamingId(self) -> WinRT_String: ...
    InstanceStartDate = property(get_InstanceStartDate, None)
    LocalId = property(get_LocalId, None)
    RoamingId = property(get_RoamingId, None)
class IAppointmentsProviderShowTimeFrameActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9baeaba6-0e0b-49aa-ba-bc-12-b1-dc-77-49-86')
    @winrt_commethod(6)
    def get_TimeToShow(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    TimeToShow = property(get_TimeToShow, None)
    Duration = property(get_Duration, None)
class IBackgroundActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ab14bee0-e760-440e-a9-1c-44-79-6d-e3-a9-2d')
    @winrt_commethod(6)
    def get_TaskInstance(self) -> Windows.ApplicationModel.Background.IBackgroundTaskInstance: ...
    TaskInstance = property(get_TaskInstance, None)
class IBarcodeScannerPreviewActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6772797c-99bf-4349-af-22-e4-12-35-60-37-1c')
    @winrt_commethod(6)
    def get_ConnectionId(self) -> WinRT_String: ...
    ConnectionId = property(get_ConnectionId, None)
class ICachedFileUpdaterActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d06eb1c7-3805-4ecb-b7-57-6c-f1-5e-26-fe-f3')
    @winrt_commethod(6)
    def get_CachedFileUpdaterUI(self) -> Windows.Storage.Provider.CachedFileUpdaterUI: ...
    CachedFileUpdaterUI = property(get_CachedFileUpdaterUI, None)
class ICommandLineActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4506472c-006a-48eb-8a-fb-d0-7a-b2-5e-33-66')
    @winrt_commethod(6)
    def get_Operation(self) -> Windows.ApplicationModel.Activation.CommandLineActivationOperation: ...
    Operation = property(get_Operation, None)
class ICommandLineActivationOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('994b2841-c59e-4f69-bc-fd-b6-1e-d4-e6-22-eb')
    @winrt_commethod(6)
    def get_Arguments(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_CurrentDirectoryPath(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_ExitCode(self, value: Int32) -> Void: ...
    @winrt_commethod(9)
    def get_ExitCode(self) -> Int32: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Arguments = property(get_Arguments, None)
    CurrentDirectoryPath = property(get_CurrentDirectoryPath, None)
    ExitCode = property(get_ExitCode, put_ExitCode)
class IContactPanelActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('52bb63e4-d3d4-4b63-80-51-4a-f2-08-2c-ab-80')
    @winrt_commethod(6)
    def get_ContactPanel(self) -> Windows.ApplicationModel.Contacts.ContactPanel: ...
    @winrt_commethod(7)
    def get_Contact(self) -> Windows.ApplicationModel.Contacts.Contact: ...
    ContactPanel = property(get_ContactPanel, None)
    Contact = property(get_Contact, None)
class IContinuationActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e58106b5-155f-4a94-a7-42-c7-e0-8f-4e-18-8c')
    @winrt_commethod(6)
    def get_ContinuationData(self) -> Windows.Foundation.Collections.ValueSet: ...
    ContinuationData = property(get_ContinuationData, None)
class IDeviceActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cd50b9a9-ce10-44d2-82-34-c3-55-a0-73-ef-33')
    @winrt_commethod(6)
    def get_DeviceInformationId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Verb(self) -> WinRT_String: ...
    DeviceInformationId = property(get_DeviceInformationId, None)
    Verb = property(get_Verb, None)
class IDevicePairingActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eba0d1e4-ecc6-4148-94-ed-f4-b3-7e-c0-5b-3e')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> Windows.Devices.Enumeration.DeviceInformation: ...
    DeviceInformation = property(get_DeviceInformation, None)
class IDialReceiverActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fb777ed7-85ee-456e-a4-4d-85-d7-30-e7-0a-ed')
    @winrt_commethod(6)
    def get_AppName(self) -> WinRT_String: ...
    AppName = property(get_AppName, None)
class IFileActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bb2afc33-93b1-42ed-8b-26-23-6d-d9-c7-84-96')
    @winrt_commethod(6)
    def get_Files(self) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]: ...
    @winrt_commethod(7)
    def get_Verb(self) -> WinRT_String: ...
    Files = property(get_Files, None)
    Verb = property(get_Verb, None)
class IFileActivatedEventArgsWithCallerPackageFamilyName(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2d60f06b-d25f-4d25-86-53-e1-c5-e1-10-83-09')
    @winrt_commethod(6)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
class IFileActivatedEventArgsWithNeighboringFiles(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('433ba1a4-e1e2-48fd-b7-fc-b5-d6-ee-e6-50-33')
    @winrt_commethod(6)
    def get_NeighboringFilesQuery(self) -> Windows.Storage.Search.StorageFileQueryResult: ...
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, None)
class IFileOpenPickerActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('72827082-5525-4bf2-bc-09-1f-50-95-d4-96-4d')
    @winrt_commethod(6)
    def get_FileOpenPickerUI(self) -> Windows.Storage.Pickers.Provider.FileOpenPickerUI: ...
    FileOpenPickerUI = property(get_FileOpenPickerUI, None)
class IFileOpenPickerActivatedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5e731f66-8d1f-45fb-af-1d-73-20-5c-8f-c7-a1')
    @winrt_commethod(6)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
class IFileOpenPickerContinuationEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f0fa3f3a-d4e8-4ad3-9c-34-23-08-f3-2f-ce-c9')
    @winrt_commethod(6)
    def get_Files(self) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]: ...
    Files = property(get_Files, None)
class IFileSavePickerActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('81c19cf1-74e6-4387-82-eb-bb-8f-d6-4b-43-46')
    @winrt_commethod(6)
    def get_FileSavePickerUI(self) -> Windows.Storage.Pickers.Provider.FileSavePickerUI: ...
    FileSavePickerUI = property(get_FileSavePickerUI, None)
class IFileSavePickerActivatedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6b73fe13-2cf2-4d48-8c-bc-af-67-d2-3f-1c-e7')
    @winrt_commethod(6)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EnterpriseId(self) -> WinRT_String: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    EnterpriseId = property(get_EnterpriseId, None)
class IFileSavePickerContinuationEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2c846fe1-3bad-4f33-8c-8b-e4-6f-ae-82-4b-4b')
    @winrt_commethod(6)
    def get_File(self) -> Windows.Storage.StorageFile: ...
    File = property(get_File, None)
class IFolderPickerContinuationEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('51882366-9f4b-498f-be-b0-42-68-4f-6e-1c-29')
    @winrt_commethod(6)
    def get_Folder(self) -> Windows.Storage.StorageFolder: ...
    Folder = property(get_Folder, None)
class ILaunchActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fbc93e26-a14a-4b4f-82-b0-33-be-d9-20-af-52')
    @winrt_commethod(6)
    def get_Arguments(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TileId(self) -> WinRT_String: ...
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
class ILaunchActivatedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0fd37ebc-9dc9-46b5-9a-ce-bd-95-d4-56-53-45')
    @winrt_commethod(6)
    def get_TileActivatedInfo(self) -> Windows.ApplicationModel.Activation.TileActivatedInfo: ...
    TileActivatedInfo = property(get_TileActivatedInfo, None)
class ILockScreenActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3ca77966-6108-4a41-82-20-ee-7d-13-3c-85-32')
    @winrt_commethod(6)
    def get_Info(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Info = property(get_Info, None)
class IPhoneCallActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('54615221-a3c1-4ced-b6-2f-8c-60-52-36-19-ad')
    @winrt_commethod(6)
    def get_LineId(self) -> Guid: ...
    LineId = property(get_LineId, None)
class IPickerReturnedActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('360defb9-a9d3-4984-a4-ed-9e-c7-34-60-49-21')
    @winrt_commethod(6)
    def get_PickerOperationId(self) -> WinRT_String: ...
    PickerOperationId = property(get_PickerOperationId, None)
class IPrelaunchActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0c44717b-19f7-48d6-b0-46-cf-22-82-6e-aa-74')
    @winrt_commethod(6)
    def get_PrelaunchActivated(self) -> Boolean: ...
    PrelaunchActivated = property(get_PrelaunchActivated, None)
class IProtocolActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6095f4dd-b7c0-46ab-81-fe-d9-0f-36-d0-0d-24')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d84a0c12-5c8f-438c-83-cb-c2-8f-cc-0b-2f-db')
    @winrt_commethod(6)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Data(self) -> Windows.Foundation.Collections.ValueSet: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    Data = property(get_Data, None)
class IProtocolForResultsActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e75132c2-7ae7-4517-80-ac-db-e8-d7-cc-5b-9c')
    @winrt_commethod(6)
    def get_ProtocolForResultsOperation(self) -> Windows.System.ProtocolForResultsOperation: ...
    ProtocolForResultsOperation = property(get_ProtocolForResultsOperation, None)
class IRestrictedLaunchActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e0b7ac81-bfc3-4344-a5-da-19-fd-5a-27-ba-ae')
    @winrt_commethod(6)
    def get_SharedContext(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    SharedContext = property(get_SharedContext, None)
class ISearchActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8cb36951-58c8-43e3-94-bc-41-d3-3f-8b-63-0e')
    @winrt_commethod(6)
    def get_QueryText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Language(self) -> WinRT_String: ...
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
class ISearchActivatedEventArgsWithLinguisticDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c09f33da-08ab-4931-9b-7c-45-10-25-f2-1f-81')
    @winrt_commethod(6)
    def get_LinguisticDetails(self) -> Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    LinguisticDetails = property(get_LinguisticDetails, None)
class IShareTargetActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4bdaf9c8-cdb2-4acb-bf-c3-66-48-56-33-78-ec')
    @winrt_commethod(6)
    def get_ShareOperation(self) -> Windows.ApplicationModel.DataTransfer.ShareTarget.ShareOperation: ...
    ShareOperation = property(get_ShareOperation, None)
class ISplashScreen(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ca4d975c-d4d6-43f0-97-c0-08-33-c6-39-1c-24')
    @winrt_commethod(6)
    def get_ImageLocation(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def add_Dismissed(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Activation.SplashScreen, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Dismissed(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ImageLocation = property(get_ImageLocation, None)
class IStartupTaskActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('03b11a58-5276-4d91-86-21-54-61-18-64-d5-fa')
    @winrt_commethod(6)
    def get_TaskId(self) -> WinRT_String: ...
    TaskId = property(get_TaskId, None)
class ITileActivatedInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('80e4a3b1-3980-4f17-b7-38-89-19-4e-0b-8f-65')
    @winrt_commethod(6)
    def get_RecentlyShownNotifications(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ShownTileNotification]: ...
    RecentlyShownNotifications = property(get_RecentlyShownNotifications, None)
class IToastNotificationActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('92a86f82-5290-431d-be-85-c4-aa-ee-b8-68-5f')
    @winrt_commethod(6)
    def get_Argument(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UserInput(self) -> Windows.Foundation.Collections.ValueSet: ...
    Argument = property(get_Argument, None)
    UserInput = property(get_UserInput, None)
class IUserDataAccountProviderActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1bc9f723-8ef1-4a51-a6-3a-fe-71-1e-ea-b6-07')
    @winrt_commethod(6)
    def get_Operation(self) -> Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation: ...
    Operation = property(get_Operation, None)
class IViewSwitcherProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('33f288a6-5c2c-4d27-ba-c7-75-36-08-8f-12-19')
    @winrt_commethod(6)
    def get_ViewSwitcher(self) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    ViewSwitcher = property(get_ViewSwitcher, None)
class IVoiceCommandActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ab92dcfd-8d43-4de6-97-75-20-70-4b-58-1b-00')
    @winrt_commethod(6)
    def get_Result(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    Result = property(get_Result, None)
class IWebAccountProviderActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('72b71774-98ea-4ccf-97-52-46-d9-05-10-04-f1')
    @winrt_commethod(6)
    def get_Operation(self) -> Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation: ...
    Operation = property(get_Operation, None)
class IWebAuthenticationBrokerContinuationEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('75dda3d4-7714-453d-b7-ff-b9-5e-3a-17-09-da')
    @winrt_commethod(6)
    def get_WebAuthenticationResult(self) -> Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    WebAuthenticationResult = property(get_WebAuthenticationResult, None)
class LaunchActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.LaunchActivatedEventArgs'
    @winrt_mixinmethod
    def get_Arguments(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_PrelaunchActivated(self: Windows.ApplicationModel.Activation.IPrelaunchActivatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_TileActivatedInfo(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs2) -> Windows.ApplicationModel.Activation.TileActivatedInfo: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    PrelaunchActivated = property(get_PrelaunchActivated, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    TileActivatedInfo = property(get_TileActivatedInfo, None)
    User = property(get_User, None)
class LockScreenActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.LockScreenActivatedEventArgs'
    @winrt_mixinmethod
    def get_Info(self: Windows.ApplicationModel.Activation.ILockScreenActivatedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Info = property(get_Info, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class LockScreenComponentActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.LockScreenComponentActivatedEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class PhoneCallActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.PhoneCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_LineId(self: Windows.ApplicationModel.Activation.IPhoneCallActivatedEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    LineId = property(get_LineId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class PickerReturnedActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.PickerReturnedActivatedEventArgs'
    @winrt_mixinmethod
    def get_PickerOperationId(self: Windows.ApplicationModel.Activation.IPickerReturnedActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    PickerOperationId = property(get_PickerOperationId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class ProtocolActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.ProtocolActivatedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Uri = property(get_Uri, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    Data = property(get_Data, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    User = property(get_User, None)
class ProtocolForResultsActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.ProtocolForResultsActivatedEventArgs'
    @winrt_mixinmethod
    def get_ProtocolForResultsOperation(self: Windows.ApplicationModel.Activation.IProtocolForResultsActivatedEventArgs) -> Windows.System.ProtocolForResultsOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ProtocolForResultsOperation = property(get_ProtocolForResultsOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    Uri = property(get_Uri, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    Data = property(get_Data, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    User = property(get_User, None)
class RestrictedLaunchActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.RestrictedLaunchActivatedEventArgs'
    @winrt_mixinmethod
    def get_SharedContext(self: Windows.ApplicationModel.Activation.IRestrictedLaunchActivatedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    SharedContext = property(get_SharedContext, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class SearchActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.SearchActivatedEventArgs'
    @winrt_mixinmethod
    def get_QueryText(self: Windows.ApplicationModel.Activation.ISearchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.ApplicationModel.Activation.ISearchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: Windows.ApplicationModel.Activation.ISearchActivatedEventArgsWithLinguisticDetails) -> Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    User = property(get_User, None)
class ShareTargetActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.ShareTargetActivatedEventArgs'
    @winrt_mixinmethod
    def get_ShareOperation(self: Windows.ApplicationModel.Activation.IShareTargetActivatedEventArgs) -> Windows.ApplicationModel.DataTransfer.ShareTarget.ShareOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ShareOperation = property(get_ShareOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class SplashScreen(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.SplashScreen'
    @winrt_mixinmethod
    def get_ImageLocation(self: Windows.ApplicationModel.Activation.ISplashScreen) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def add_Dismissed(self: Windows.ApplicationModel.Activation.ISplashScreen, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Activation.SplashScreen, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Dismissed(self: Windows.ApplicationModel.Activation.ISplashScreen, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ImageLocation = property(get_ImageLocation, None)
class StartupTaskActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.StartupTaskActivatedEventArgs'
    @winrt_mixinmethod
    def get_TaskId(self: Windows.ApplicationModel.Activation.IStartupTaskActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    TaskId = property(get_TaskId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class TileActivatedInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.TileActivatedInfo'
    @winrt_mixinmethod
    def get_RecentlyShownNotifications(self: Windows.ApplicationModel.Activation.ITileActivatedInfo) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ShownTileNotification]: ...
    RecentlyShownNotifications = property(get_RecentlyShownNotifications, None)
class ToastNotificationActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.ToastNotificationActivatedEventArgs'
    @winrt_mixinmethod
    def get_Argument(self: Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserInput(self: Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    Argument = property(get_Argument, None)
    UserInput = property(get_UserInput, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
class UserDataAccountProviderActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.UserDataAccountProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: Windows.ApplicationModel.Activation.IUserDataAccountProviderActivatedEventArgs) -> Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    Operation = property(get_Operation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class VoiceCommandActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.VoiceCommandActivatedEventArgs'
    @winrt_mixinmethod
    def get_Result(self: Windows.ApplicationModel.Activation.IVoiceCommandActivatedEventArgs) -> Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Result = property(get_Result, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebAccountProviderActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.WebAccountProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: Windows.ApplicationModel.Activation.IWebAccountProviderActivatedEventArgs) -> Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Operation = property(get_Operation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebAuthenticationBrokerContinuationEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Activation.WebAuthenticationBrokerContinuationEventArgs'
    @winrt_mixinmethod
    def get_WebAuthenticationResult(self: Windows.ApplicationModel.Activation.IWebAuthenticationBrokerContinuationEventArgs) -> Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    WebAuthenticationResult = property(get_WebAuthenticationResult, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
make_head(_module, 'AppointmentsProviderAddAppointmentActivatedEventArgs')
make_head(_module, 'AppointmentsProviderRemoveAppointmentActivatedEventArgs')
make_head(_module, 'AppointmentsProviderReplaceAppointmentActivatedEventArgs')
make_head(_module, 'AppointmentsProviderShowAppointmentDetailsActivatedEventArgs')
make_head(_module, 'AppointmentsProviderShowTimeFrameActivatedEventArgs')
make_head(_module, 'BackgroundActivatedEventArgs')
make_head(_module, 'BarcodeScannerPreviewActivatedEventArgs')
make_head(_module, 'CachedFileUpdaterActivatedEventArgs')
make_head(_module, 'CommandLineActivatedEventArgs')
make_head(_module, 'CommandLineActivationOperation')
make_head(_module, 'ContactPanelActivatedEventArgs')
make_head(_module, 'DeviceActivatedEventArgs')
make_head(_module, 'DevicePairingActivatedEventArgs')
make_head(_module, 'DialReceiverActivatedEventArgs')
make_head(_module, 'FileActivatedEventArgs')
make_head(_module, 'FileOpenPickerActivatedEventArgs')
make_head(_module, 'FileOpenPickerContinuationEventArgs')
make_head(_module, 'FileSavePickerActivatedEventArgs')
make_head(_module, 'FileSavePickerContinuationEventArgs')
make_head(_module, 'FolderPickerContinuationEventArgs')
make_head(_module, 'IActivatedEventArgs')
make_head(_module, 'IActivatedEventArgsWithUser')
make_head(_module, 'IApplicationViewActivatedEventArgs')
make_head(_module, 'IAppointmentsProviderActivatedEventArgs')
make_head(_module, 'IAppointmentsProviderAddAppointmentActivatedEventArgs')
make_head(_module, 'IAppointmentsProviderRemoveAppointmentActivatedEventArgs')
make_head(_module, 'IAppointmentsProviderReplaceAppointmentActivatedEventArgs')
make_head(_module, 'IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs')
make_head(_module, 'IAppointmentsProviderShowTimeFrameActivatedEventArgs')
make_head(_module, 'IBackgroundActivatedEventArgs')
make_head(_module, 'IBarcodeScannerPreviewActivatedEventArgs')
make_head(_module, 'ICachedFileUpdaterActivatedEventArgs')
make_head(_module, 'ICommandLineActivatedEventArgs')
make_head(_module, 'ICommandLineActivationOperation')
make_head(_module, 'IContactPanelActivatedEventArgs')
make_head(_module, 'IContinuationActivatedEventArgs')
make_head(_module, 'IDeviceActivatedEventArgs')
make_head(_module, 'IDevicePairingActivatedEventArgs')
make_head(_module, 'IDialReceiverActivatedEventArgs')
make_head(_module, 'IFileActivatedEventArgs')
make_head(_module, 'IFileActivatedEventArgsWithCallerPackageFamilyName')
make_head(_module, 'IFileActivatedEventArgsWithNeighboringFiles')
make_head(_module, 'IFileOpenPickerActivatedEventArgs')
make_head(_module, 'IFileOpenPickerActivatedEventArgs2')
make_head(_module, 'IFileOpenPickerContinuationEventArgs')
make_head(_module, 'IFileSavePickerActivatedEventArgs')
make_head(_module, 'IFileSavePickerActivatedEventArgs2')
make_head(_module, 'IFileSavePickerContinuationEventArgs')
make_head(_module, 'IFolderPickerContinuationEventArgs')
make_head(_module, 'ILaunchActivatedEventArgs')
make_head(_module, 'ILaunchActivatedEventArgs2')
make_head(_module, 'ILockScreenActivatedEventArgs')
make_head(_module, 'IPhoneCallActivatedEventArgs')
make_head(_module, 'IPickerReturnedActivatedEventArgs')
make_head(_module, 'IPrelaunchActivatedEventArgs')
make_head(_module, 'IProtocolActivatedEventArgs')
make_head(_module, 'IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData')
make_head(_module, 'IProtocolForResultsActivatedEventArgs')
make_head(_module, 'IRestrictedLaunchActivatedEventArgs')
make_head(_module, 'ISearchActivatedEventArgs')
make_head(_module, 'ISearchActivatedEventArgsWithLinguisticDetails')
make_head(_module, 'IShareTargetActivatedEventArgs')
make_head(_module, 'ISplashScreen')
make_head(_module, 'IStartupTaskActivatedEventArgs')
make_head(_module, 'ITileActivatedInfo')
make_head(_module, 'IToastNotificationActivatedEventArgs')
make_head(_module, 'IUserDataAccountProviderActivatedEventArgs')
make_head(_module, 'IViewSwitcherProvider')
make_head(_module, 'IVoiceCommandActivatedEventArgs')
make_head(_module, 'IWebAccountProviderActivatedEventArgs')
make_head(_module, 'IWebAuthenticationBrokerContinuationEventArgs')
make_head(_module, 'LaunchActivatedEventArgs')
make_head(_module, 'LockScreenActivatedEventArgs')
make_head(_module, 'LockScreenComponentActivatedEventArgs')
make_head(_module, 'PhoneCallActivatedEventArgs')
make_head(_module, 'PickerReturnedActivatedEventArgs')
make_head(_module, 'ProtocolActivatedEventArgs')
make_head(_module, 'ProtocolForResultsActivatedEventArgs')
make_head(_module, 'RestrictedLaunchActivatedEventArgs')
make_head(_module, 'SearchActivatedEventArgs')
make_head(_module, 'ShareTargetActivatedEventArgs')
make_head(_module, 'SplashScreen')
make_head(_module, 'StartupTaskActivatedEventArgs')
make_head(_module, 'TileActivatedInfo')
make_head(_module, 'ToastNotificationActivatedEventArgs')
make_head(_module, 'UserDataAccountProviderActivatedEventArgs')
make_head(_module, 'VoiceCommandActivatedEventArgs')
make_head(_module, 'WebAccountProviderActivatedEventArgs')
make_head(_module, 'WebAuthenticationBrokerContinuationEventArgs')
