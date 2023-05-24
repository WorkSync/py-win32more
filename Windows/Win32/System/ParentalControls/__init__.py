from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.ParentalControls
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ARRAY_SEP_CHAR: UInt32 = 9
WPCCHANNEL: UInt32 = 16
WPC_SETTINGS_LOCATE: UInt32 = 20
WPC_SETTINGS_MODIFY: UInt32 = 21
WPC_APP_LAUNCH: UInt32 = 22
WPC_SYSTEM: UInt32 = 23
WPC_WEB: UInt32 = 24
WPCPROV_TASK_SettingChange: UInt32 = 1
WPCPROV_TASK_GameStart: UInt32 = 2
WPCPROV_TASK_UrlVisit: UInt32 = 3
WPCPROV_TASK_EmailReceived: UInt32 = 4
WPCPROV_TASK_EmailSent: UInt32 = 5
WPCPROV_TASK_MediaPlayback: UInt32 = 6
WPCPROV_TASK_IMInvitation: UInt32 = 7
WPCPROV_TASK_IMJoin: UInt32 = 8
WPCPROV_TASK_IMLeave: UInt32 = 9
WPCPROV_TASK_FileDownload: UInt32 = 10
WPCPROV_TASK_IMFeature: UInt32 = 11
WPCPROV_TASK_Custom: UInt32 = 13
WPCPROV_TASK_EmailContact: UInt32 = 14
WPCPROV_TASK_IMContact: UInt32 = 15
WPCPROV_TASK_AppBlocked: UInt32 = 16
WPCPROV_TASK_AppOverride: UInt32 = 17
WPCPROV_TASK_WebOverride: UInt32 = 18
WPCPROV_TASK_WebsiteVisit: UInt32 = 19
WPCPROV_TASK_Application: UInt32 = 20
WPCPROV_TASK_ComputerUsage: UInt32 = 21
WPCPROV_TASK_ContentUsage: UInt32 = 22
WPCPROV_KEYWORD_WPC: UInt32 = 16
WPCPROV_KEYWORD_ThirdParty: UInt32 = 32
WPCEVENT_SYS_SETTINGCHANGE_value: UInt32 = 1
WPCEVENT_GAME_START_value: UInt32 = 2
WPCEVENT_WEB_URLVISIT_value: UInt32 = 3
WPCEVENT_EMAIL_RECEIVED_value: UInt32 = 4
WPCEVENT_EMAIL_SENT_value: UInt32 = 5
WPCEVENT_MEDIA_PLAYBACK_value: UInt32 = 6
WPCEVENT_IM_INVITATION_value: UInt32 = 7
WPCEVENT_IM_JOIN_value: UInt32 = 8
WPCEVENT_IM_LEAVE_value: UInt32 = 9
WPCEVENT_WEB_FILEDOWNLOAD_value: UInt32 = 10
WPCEVENT_IM_FEATURE_value: UInt32 = 11
WPCEVENT_CUSTOM_value: UInt32 = 13
WPCEVENT_EMAIL_CONTACT_value: UInt32 = 14
WPCEVENT_IM_CONTACT_value: UInt32 = 15
WPCEVENT_SYSTEM_APPBLOCKED_value: UInt32 = 16
WPCEVENT_APPOVERRIDE_value: UInt32 = 17
WPCEVENT_WEBOVERRIDE_value: UInt32 = 18
WPCEVENT_WEB_WEBSITEVISIT_value: UInt32 = 19
WPCEVENT_APPLICATION_value: UInt32 = 20
WPCEVENT_COMPUTERUSAGE_value: UInt32 = 21
WPCEVENT_CONTENTUSAGE_value: UInt32 = 22
MSG_Keyword_WPC: Int32 = 268435461
MSG_Keyword_ThirdParty: Int32 = 268435462
MSG_Opcode_Locate: Int32 = 805306388
MSG_Opcode_Modify: Int32 = 805306389
MSG_Opcode_Launch: Int32 = 805306390
MSG_Opcode_System: Int32 = 805306391
MSG_Opcode_Web: Int32 = 805306392
MSG_Task_SettingChange: Int32 = 1879048193
MSG_Task_GameStart: Int32 = 1879048194
MSG_Task_UrlVisit: Int32 = 1879048195
MSG_Task_EmailReceived: Int32 = 1879048196
MSG_Task_EmailSent: Int32 = 1879048197
MSG_Task_MediaPlayback: Int32 = 1879048198
MSG_Task_IMInvitation: Int32 = 1879048199
MSG_Task_IMJoin: Int32 = 1879048200
MSG_Task_IMLeave: Int32 = 1879048201
MSG_Task_FileDownload: Int32 = 1879048202
MSG_Task_IMFeature: Int32 = 1879048203
MSG_Task_Custom: Int32 = 1879048205
MSG_Task_EmailContact: Int32 = 1879048206
MSG_Task_IMContact: Int32 = 1879048207
MSG_Task_AppBlocked: Int32 = 1879048208
MSG_Task_AppOverride: Int32 = 1879048209
MSG_Task_WebOverride: Int32 = 1879048210
MSG_Task_WebsiteVisit: Int32 = 1879048211
MSG_Task_Application: Int32 = 1879048212
MSG_Task_ComputerUsage: Int32 = 1879048213
MSG_Task_ContentUsage: Int32 = 1879048214
MSG_Publisher_Name: Int32 = -1879048191
MSG_Event_SettingChange: Int32 = -1342177279
MSG_Event_GameStart: Int32 = -1342177278
MSG_Event_UrlVisit: Int32 = -1342177277
MSG_Event_EmailReceived: Int32 = -1342177276
MSG_Event_EmailSent: Int32 = -1342177275
MSG_Event_MediaPlayback: Int32 = -1342177274
MSG_Event_IMInvitation: Int32 = -1342177273
MSG_Event_IMJoin: Int32 = -1342177272
MSG_Event_IMLeave: Int32 = -1342177271
MSG_Event_FileDownload: Int32 = -1342177270
MSG_Event_IMFeature: Int32 = -1342177269
MSG_Event_Custom: Int32 = -1342177267
MSG_Event_EmailContact: Int32 = -1342177266
MSG_Event_IMContact: Int32 = -1342177265
MSG_Event_AppBlocked: Int32 = -1342177264
MSG_Event_AppOverride: Int32 = -1342177263
MSG_Event_WebOverride: Int32 = -1342177262
MSG_Event_WebsiteVisit: Int32 = -1342177261
MSG_Event_Application: Int32 = -1342177260
MSG_Event_ComputerUsage: Int32 = -1342177259
MSG_Event_ContentUsage: Int32 = -1342177258
FACILITY_WPC: UInt32 = 2457
WPCPROV: Guid = Guid('{01090065-b467-4503-9b28-533766761087}')
class IWPCGamesSettings(ComPtr):
    extends: Windows.Win32.System.ParentalControls.IWPCSettings
    _iid_ = Guid('{95e87780-e158-489e-b452-bbb850790715}')
    @commethod(6)
    def IsBlocked(self, guidAppID: Guid, pdwReasons: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWPCProviderConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bef54196-2d02-4a26-b6e5-d65af295d0f1}')
    @commethod(3)
    def GetUserSummary(self, bstrSID: Windows.Win32.Foundation.BSTR, pbstrUserSummary: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Configure(self, hWnd: Windows.Win32.Foundation.HWND, bstrSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RequestOverride(self, hWnd: Windows.Win32.Foundation.HWND, bstrPath: Windows.Win32.Foundation.BSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWPCProviderState(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{50b6a267-c4bd-450b-adb5-759073837c9e}')
    @commethod(3)
    def Enable(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disable(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWPCProviderSupport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{41eba572-23ed-4779-bec1-8df96206c44c}')
    @commethod(3)
    def GetCurrent(self, pguidProvider: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IWPCSettings(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8fdf6ca1-0189-47e4-b670-1a8a4636e340}')
    @commethod(3)
    def IsLoggingRequired(self, pfRequired: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLastSettingsChangeTime(self, pTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRestrictions(self, pdwRestrictions: POINTER(Windows.Win32.System.ParentalControls.WPCFLAG_RESTRICTION)) -> Windows.Win32.Foundation.HRESULT: ...
class IWPCWebSettings(ComPtr):
    extends: Windows.Win32.System.ParentalControls.IWPCSettings
    _iid_ = Guid('{ffccbdb8-0992-4c30-b0f1-1cbb09c240aa}')
    @commethod(6)
    def GetSettings(self, pdwSettings: POINTER(Windows.Win32.System.ParentalControls.WPCFLAG_WEB_SETTING)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RequestURLOverride(self, hWnd: Windows.Win32.Foundation.HWND, pcszURL: Windows.Win32.Foundation.PWSTR, cURLs: UInt32, ppcszSubURLs: POINTER(Windows.Win32.Foundation.PWSTR), pfChanged: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWindowsParentalControls(ComPtr):
    extends: Windows.Win32.System.ParentalControls.IWindowsParentalControlsCore
    _iid_ = Guid('{28b4d88b-e072-49e6-804d-26edbe21a7b9}')
    @commethod(7)
    def GetGamesSettings(self, pcszSID: Windows.Win32.Foundation.PWSTR, ppSettings: POINTER(Windows.Win32.System.ParentalControls.IWPCGamesSettings_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWindowsParentalControlsCore(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ff40a0f-3f3b-4d7c-a41b-4f39d7b44d05}')
    @commethod(3)
    def GetVisibility(self, peVisibility: POINTER(Windows.Win32.System.ParentalControls.WPCFLAG_VISIBILITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUserSettings(self, pcszSID: Windows.Win32.Foundation.PWSTR, ppSettings: POINTER(Windows.Win32.System.ParentalControls.IWPCSettings_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetWebSettings(self, pcszSID: Windows.Win32.Foundation.PWSTR, ppSettings: POINTER(Windows.Win32.System.ParentalControls.IWPCWebSettings_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetWebFilterInfo(self, pguidID: POINTER(Guid), ppszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
WPCFLAG_IM_FEATURE = Int32
WPCFLAG_IM_FEATURE_NONE: WPCFLAG_IM_FEATURE = 0
WPCFLAG_IM_FEATURE_VIDEO: WPCFLAG_IM_FEATURE = 1
WPCFLAG_IM_FEATURE_AUDIO: WPCFLAG_IM_FEATURE = 2
WPCFLAG_IM_FEATURE_GAME: WPCFLAG_IM_FEATURE = 4
WPCFLAG_IM_FEATURE_SMS: WPCFLAG_IM_FEATURE = 8
WPCFLAG_IM_FEATURE_FILESWAP: WPCFLAG_IM_FEATURE = 16
WPCFLAG_IM_FEATURE_URLSWAP: WPCFLAG_IM_FEATURE = 32
WPCFLAG_IM_FEATURE_SENDING: WPCFLAG_IM_FEATURE = -2147483648
WPCFLAG_IM_FEATURE_ALL: WPCFLAG_IM_FEATURE = -1
WPCFLAG_IM_LEAVE = Int32
WPCFLAG_IM_LEAVE_NORMAL: WPCFLAG_IM_LEAVE = 0
WPCFLAG_IM_LEAVE_FORCED: WPCFLAG_IM_LEAVE = 1
WPCFLAG_IM_LEAVE_CONVERSATION_END: WPCFLAG_IM_LEAVE = 2
WPCFLAG_ISBLOCKED = Int32
WPCFLAG_ISBLOCKED_NOTBLOCKED: WPCFLAG_ISBLOCKED = 0
WPCFLAG_ISBLOCKED_IMBLOCKED: WPCFLAG_ISBLOCKED = 1
WPCFLAG_ISBLOCKED_EMAILBLOCKED: WPCFLAG_ISBLOCKED = 2
WPCFLAG_ISBLOCKED_MEDIAPLAYBACKBLOCKED: WPCFLAG_ISBLOCKED = 4
WPCFLAG_ISBLOCKED_WEBBLOCKED: WPCFLAG_ISBLOCKED = 8
WPCFLAG_ISBLOCKED_GAMESBLOCKED: WPCFLAG_ISBLOCKED = 16
WPCFLAG_ISBLOCKED_CONTACTBLOCKED: WPCFLAG_ISBLOCKED = 32
WPCFLAG_ISBLOCKED_FEATUREBLOCKED: WPCFLAG_ISBLOCKED = 64
WPCFLAG_ISBLOCKED_DOWNLOADBLOCKED: WPCFLAG_ISBLOCKED = 128
WPCFLAG_ISBLOCKED_RATINGBLOCKED: WPCFLAG_ISBLOCKED = 256
WPCFLAG_ISBLOCKED_DESCRIPTORBLOCKED: WPCFLAG_ISBLOCKED = 512
WPCFLAG_ISBLOCKED_EXPLICITBLOCK: WPCFLAG_ISBLOCKED = 1024
WPCFLAG_ISBLOCKED_BADPASS: WPCFLAG_ISBLOCKED = 2048
WPCFLAG_ISBLOCKED_MAXHOURS: WPCFLAG_ISBLOCKED = 4096
WPCFLAG_ISBLOCKED_SPECHOURS: WPCFLAG_ISBLOCKED = 8192
WPCFLAG_ISBLOCKED_SETTINGSCHANGEBLOCKED: WPCFLAG_ISBLOCKED = 16384
WPCFLAG_ISBLOCKED_ATTACHMENTBLOCKED: WPCFLAG_ISBLOCKED = 32768
WPCFLAG_ISBLOCKED_SENDERBLOCKED: WPCFLAG_ISBLOCKED = 65536
WPCFLAG_ISBLOCKED_RECEIVERBLOCKED: WPCFLAG_ISBLOCKED = 131072
WPCFLAG_ISBLOCKED_NOTEXPLICITLYALLOWED: WPCFLAG_ISBLOCKED = 262144
WPCFLAG_ISBLOCKED_NOTINLIST: WPCFLAG_ISBLOCKED = 524288
WPCFLAG_ISBLOCKED_CATEGORYBLOCKED: WPCFLAG_ISBLOCKED = 1048576
WPCFLAG_ISBLOCKED_CATEGORYNOTINLIST: WPCFLAG_ISBLOCKED = 2097152
WPCFLAG_ISBLOCKED_NOTKIDS: WPCFLAG_ISBLOCKED = 4194304
WPCFLAG_ISBLOCKED_UNRATED: WPCFLAG_ISBLOCKED = 8388608
WPCFLAG_ISBLOCKED_NOACCESS: WPCFLAG_ISBLOCKED = 16777216
WPCFLAG_ISBLOCKED_INTERNALERROR: WPCFLAG_ISBLOCKED = -1
WPCFLAG_LOGOFF_TYPE = Int32
WPCFLAG_LOGOFF_TYPE_LOGOUT: WPCFLAG_LOGOFF_TYPE = 0
WPCFLAG_LOGOFF_TYPE_RESTART: WPCFLAG_LOGOFF_TYPE = 1
WPCFLAG_LOGOFF_TYPE_SHUTDOWN: WPCFLAG_LOGOFF_TYPE = 2
WPCFLAG_LOGOFF_TYPE_FUS: WPCFLAG_LOGOFF_TYPE = 4
WPCFLAG_LOGOFF_TYPE_FORCEDFUS: WPCFLAG_LOGOFF_TYPE = 8
WPCFLAG_OVERRIDE = Int32
WPCFLAG_APPLICATION: WPCFLAG_OVERRIDE = 1
WPCFLAG_RESTRICTION = Int32
WPCFLAG_NO_RESTRICTION: WPCFLAG_RESTRICTION = 0
WPCFLAG_LOGGING_REQUIRED: WPCFLAG_RESTRICTION = 1
WPCFLAG_WEB_FILTERED: WPCFLAG_RESTRICTION = 2
WPCFLAG_HOURS_RESTRICTED: WPCFLAG_RESTRICTION = 4
WPCFLAG_GAMES_BLOCKED: WPCFLAG_RESTRICTION = 8
WPCFLAG_APPS_RESTRICTED: WPCFLAG_RESTRICTION = 16
WPCFLAG_TIME_ALLOWANCE_RESTRICTED: WPCFLAG_RESTRICTION = 32
WPCFLAG_GAMES_RESTRICTED: WPCFLAG_RESTRICTION = 64
WPCFLAG_VISIBILITY = Int32
WPCFLAG_WPC_VISIBLE: WPCFLAG_VISIBILITY = 0
WPCFLAG_WPC_HIDDEN: WPCFLAG_VISIBILITY = 1
WPCFLAG_WEB_SETTING = Int32
WPCFLAG_WEB_SETTING_NOTBLOCKED: WPCFLAG_WEB_SETTING = 0
WPCFLAG_WEB_SETTING_DOWNLOADSBLOCKED: WPCFLAG_WEB_SETTING = 1
WPC_ARGS_APPLICATIONEVENT = Int32
WPC_ARGS_APPLICATIONEVENT_SERIALIZEDAPPLICATION: WPC_ARGS_APPLICATIONEVENT = 0
WPC_ARGS_APPLICATIONEVENT_DECISION: WPC_ARGS_APPLICATIONEVENT = 1
WPC_ARGS_APPLICATIONEVENT_PROCESSID: WPC_ARGS_APPLICATIONEVENT = 2
WPC_ARGS_APPLICATIONEVENT_CREATIONTIME: WPC_ARGS_APPLICATIONEVENT = 3
WPC_ARGS_APPLICATIONEVENT_TIMEUSED: WPC_ARGS_APPLICATIONEVENT = 4
WPC_ARGS_APPLICATIONEVENT_CARGS: WPC_ARGS_APPLICATIONEVENT = 5
WPC_ARGS_APPOVERRIDEEVENT = Int32
WPC_ARGS_APPOVERRIDEEVENT_USERID: WPC_ARGS_APPOVERRIDEEVENT = 0
WPC_ARGS_APPOVERRIDEEVENT_PATH: WPC_ARGS_APPOVERRIDEEVENT = 1
WPC_ARGS_APPOVERRIDEEVENT_REASON: WPC_ARGS_APPOVERRIDEEVENT = 2
WPC_ARGS_APPOVERRIDEEVENT_CARGS: WPC_ARGS_APPOVERRIDEEVENT = 3
WPC_ARGS_COMPUTERUSAGEEVENT = Int32
WPC_ARGS_COMPUTERUSAGEEVENT_ID: WPC_ARGS_COMPUTERUSAGEEVENT = 0
WPC_ARGS_COMPUTERUSAGEEVENT_TIMEUSED: WPC_ARGS_COMPUTERUSAGEEVENT = 1
WPC_ARGS_COMPUTERUSAGEEVENT_CARGS: WPC_ARGS_COMPUTERUSAGEEVENT = 2
WPC_ARGS_CONTENTUSAGEEVENT = Int32
WPC_ARGS_CONTENTUSAGEEVENT_CONTENTPROVIDERID: WPC_ARGS_CONTENTUSAGEEVENT = 0
WPC_ARGS_CONTENTUSAGEEVENT_CONTENTPROVIDERTITLE: WPC_ARGS_CONTENTUSAGEEVENT = 1
WPC_ARGS_CONTENTUSAGEEVENT_ID: WPC_ARGS_CONTENTUSAGEEVENT = 2
WPC_ARGS_CONTENTUSAGEEVENT_TITLE: WPC_ARGS_CONTENTUSAGEEVENT = 3
WPC_ARGS_CONTENTUSAGEEVENT_CATEGORY: WPC_ARGS_CONTENTUSAGEEVENT = 4
WPC_ARGS_CONTENTUSAGEEVENT_RATINGS: WPC_ARGS_CONTENTUSAGEEVENT = 5
WPC_ARGS_CONTENTUSAGEEVENT_DECISION: WPC_ARGS_CONTENTUSAGEEVENT = 6
WPC_ARGS_CONTENTUSAGEEVENT_CARGS: WPC_ARGS_CONTENTUSAGEEVENT = 7
WPC_ARGS_CONVERSATIONINITEVENT = Int32
WPC_ARGS_CONVERSATIONINITEVENT_APPNAME: WPC_ARGS_CONVERSATIONINITEVENT = 0
WPC_ARGS_CONVERSATIONINITEVENT_APPVERSION: WPC_ARGS_CONVERSATIONINITEVENT = 1
WPC_ARGS_CONVERSATIONINITEVENT_ACCOUNTNAME: WPC_ARGS_CONVERSATIONINITEVENT = 2
WPC_ARGS_CONVERSATIONINITEVENT_CONVID: WPC_ARGS_CONVERSATIONINITEVENT = 3
WPC_ARGS_CONVERSATIONINITEVENT_REQUESTINGIP: WPC_ARGS_CONVERSATIONINITEVENT = 4
WPC_ARGS_CONVERSATIONINITEVENT_SENDER: WPC_ARGS_CONVERSATIONINITEVENT = 5
WPC_ARGS_CONVERSATIONINITEVENT_REASON: WPC_ARGS_CONVERSATIONINITEVENT = 6
WPC_ARGS_CONVERSATIONINITEVENT_RECIPCOUNT: WPC_ARGS_CONVERSATIONINITEVENT = 7
WPC_ARGS_CONVERSATIONINITEVENT_RECIPIENT: WPC_ARGS_CONVERSATIONINITEVENT = 8
WPC_ARGS_CONVERSATIONINITEVENT_CARGS: WPC_ARGS_CONVERSATIONINITEVENT = 9
WPC_ARGS_CONVERSATIONJOINEVENT = Int32
WPC_ARGS_CONVERSATIONJOINEVENT_APPNAME: WPC_ARGS_CONVERSATIONJOINEVENT = 0
WPC_ARGS_CONVERSATIONJOINEVENT_APPVERSION: WPC_ARGS_CONVERSATIONJOINEVENT = 1
WPC_ARGS_CONVERSATIONJOINEVENT_ACCOUNTNAME: WPC_ARGS_CONVERSATIONJOINEVENT = 2
WPC_ARGS_CONVERSATIONJOINEVENT_CONVID: WPC_ARGS_CONVERSATIONJOINEVENT = 3
WPC_ARGS_CONVERSATIONJOINEVENT_JOININGIP: WPC_ARGS_CONVERSATIONJOINEVENT = 4
WPC_ARGS_CONVERSATIONJOINEVENT_JOININGUSER: WPC_ARGS_CONVERSATIONJOINEVENT = 5
WPC_ARGS_CONVERSATIONJOINEVENT_REASON: WPC_ARGS_CONVERSATIONJOINEVENT = 6
WPC_ARGS_CONVERSATIONJOINEVENT_MEMBERCOUNT: WPC_ARGS_CONVERSATIONJOINEVENT = 7
WPC_ARGS_CONVERSATIONJOINEVENT_MEMBER: WPC_ARGS_CONVERSATIONJOINEVENT = 8
WPC_ARGS_CONVERSATIONJOINEVENT_SENDER: WPC_ARGS_CONVERSATIONJOINEVENT = 9
WPC_ARGS_CONVERSATIONJOINEVENT_CARGS: WPC_ARGS_CONVERSATIONJOINEVENT = 10
WPC_ARGS_CONVERSATIONLEAVEEVENT = Int32
WPC_ARGS_CONVERSATIONLEAVEEVENT_APPNAME: WPC_ARGS_CONVERSATIONLEAVEEVENT = 0
WPC_ARGS_CONVERSATIONLEAVEEVENT_APPVERSION: WPC_ARGS_CONVERSATIONLEAVEEVENT = 1
WPC_ARGS_CONVERSATIONLEAVEEVENT_ACCOUNTNAME: WPC_ARGS_CONVERSATIONLEAVEEVENT = 2
WPC_ARGS_CONVERSATIONLEAVEEVENT_CONVID: WPC_ARGS_CONVERSATIONLEAVEEVENT = 3
WPC_ARGS_CONVERSATIONLEAVEEVENT_LEAVINGIP: WPC_ARGS_CONVERSATIONLEAVEEVENT = 4
WPC_ARGS_CONVERSATIONLEAVEEVENT_LEAVINGUSER: WPC_ARGS_CONVERSATIONLEAVEEVENT = 5
WPC_ARGS_CONVERSATIONLEAVEEVENT_REASON: WPC_ARGS_CONVERSATIONLEAVEEVENT = 6
WPC_ARGS_CONVERSATIONLEAVEEVENT_MEMBERCOUNT: WPC_ARGS_CONVERSATIONLEAVEEVENT = 7
WPC_ARGS_CONVERSATIONLEAVEEVENT_MEMBER: WPC_ARGS_CONVERSATIONLEAVEEVENT = 8
WPC_ARGS_CONVERSATIONLEAVEEVENT_FLAGS: WPC_ARGS_CONVERSATIONLEAVEEVENT = 9
WPC_ARGS_CONVERSATIONLEAVEEVENT_CARGS: WPC_ARGS_CONVERSATIONLEAVEEVENT = 10
WPC_ARGS_CUSTOMEVENT = Int32
WPC_ARGS_CUSTOMEVENT_PUBLISHER: WPC_ARGS_CUSTOMEVENT = 0
WPC_ARGS_CUSTOMEVENT_APPNAME: WPC_ARGS_CUSTOMEVENT = 1
WPC_ARGS_CUSTOMEVENT_APPVERSION: WPC_ARGS_CUSTOMEVENT = 2
WPC_ARGS_CUSTOMEVENT_EVENT: WPC_ARGS_CUSTOMEVENT = 3
WPC_ARGS_CUSTOMEVENT_VALUE1: WPC_ARGS_CUSTOMEVENT = 4
WPC_ARGS_CUSTOMEVENT_VALUE2: WPC_ARGS_CUSTOMEVENT = 5
WPC_ARGS_CUSTOMEVENT_VALUE3: WPC_ARGS_CUSTOMEVENT = 6
WPC_ARGS_CUSTOMEVENT_BLOCKED: WPC_ARGS_CUSTOMEVENT = 7
WPC_ARGS_CUSTOMEVENT_REASON: WPC_ARGS_CUSTOMEVENT = 8
WPC_ARGS_CUSTOMEVENT_CARGS: WPC_ARGS_CUSTOMEVENT = 9
WPC_ARGS_EMAILCONTACTEVENT = Int32
WPC_ARGS_EMAILCONTACTEVENT_APPNAME: WPC_ARGS_EMAILCONTACTEVENT = 0
WPC_ARGS_EMAILCONTACTEVENT_APPVERSION: WPC_ARGS_EMAILCONTACTEVENT = 1
WPC_ARGS_EMAILCONTACTEVENT_OLDNAME: WPC_ARGS_EMAILCONTACTEVENT = 2
WPC_ARGS_EMAILCONTACTEVENT_OLDID: WPC_ARGS_EMAILCONTACTEVENT = 3
WPC_ARGS_EMAILCONTACTEVENT_NEWNAME: WPC_ARGS_EMAILCONTACTEVENT = 4
WPC_ARGS_EMAILCONTACTEVENT_NEWID: WPC_ARGS_EMAILCONTACTEVENT = 5
WPC_ARGS_EMAILCONTACTEVENT_REASON: WPC_ARGS_EMAILCONTACTEVENT = 6
WPC_ARGS_EMAILCONTACTEVENT_EMAILACCOUNT: WPC_ARGS_EMAILCONTACTEVENT = 7
WPC_ARGS_EMAILCONTACTEVENT_CARGS: WPC_ARGS_EMAILCONTACTEVENT = 8
WPC_ARGS_EMAILRECEIEVEDEVENT = Int32
WPC_ARGS_EMAILRECEIEVEDEVENT_SENDER: WPC_ARGS_EMAILRECEIEVEDEVENT = 0
WPC_ARGS_EMAILRECEIEVEDEVENT_APPNAME: WPC_ARGS_EMAILRECEIEVEDEVENT = 1
WPC_ARGS_EMAILRECEIEVEDEVENT_APPVERSION: WPC_ARGS_EMAILRECEIEVEDEVENT = 2
WPC_ARGS_EMAILRECEIEVEDEVENT_SUBJECT: WPC_ARGS_EMAILRECEIEVEDEVENT = 3
WPC_ARGS_EMAILRECEIEVEDEVENT_REASON: WPC_ARGS_EMAILRECEIEVEDEVENT = 4
WPC_ARGS_EMAILRECEIEVEDEVENT_RECIPCOUNT: WPC_ARGS_EMAILRECEIEVEDEVENT = 5
WPC_ARGS_EMAILRECEIEVEDEVENT_RECIPIENT: WPC_ARGS_EMAILRECEIEVEDEVENT = 6
WPC_ARGS_EMAILRECEIEVEDEVENT_ATTACHCOUNT: WPC_ARGS_EMAILRECEIEVEDEVENT = 7
WPC_ARGS_EMAILRECEIEVEDEVENT_ATTACHMENTNAME: WPC_ARGS_EMAILRECEIEVEDEVENT = 8
WPC_ARGS_EMAILRECEIEVEDEVENT_RECEIVEDTIME: WPC_ARGS_EMAILRECEIEVEDEVENT = 9
WPC_ARGS_EMAILRECEIEVEDEVENT_EMAILACCOUNT: WPC_ARGS_EMAILRECEIEVEDEVENT = 10
WPC_ARGS_EMAILRECEIEVEDEVENT_CARGS: WPC_ARGS_EMAILRECEIEVEDEVENT = 11
WPC_ARGS_EMAILSENTEVENT = Int32
WPC_ARGS_EMAILSENTEVENT_SENDER: WPC_ARGS_EMAILSENTEVENT = 0
WPC_ARGS_EMAILSENTEVENT_APPNAME: WPC_ARGS_EMAILSENTEVENT = 1
WPC_ARGS_EMAILSENTEVENT_APPVERSION: WPC_ARGS_EMAILSENTEVENT = 2
WPC_ARGS_EMAILSENTEVENT_SUBJECT: WPC_ARGS_EMAILSENTEVENT = 3
WPC_ARGS_EMAILSENTEVENT_REASON: WPC_ARGS_EMAILSENTEVENT = 4
WPC_ARGS_EMAILSENTEVENT_RECIPCOUNT: WPC_ARGS_EMAILSENTEVENT = 5
WPC_ARGS_EMAILSENTEVENT_RECIPIENT: WPC_ARGS_EMAILSENTEVENT = 6
WPC_ARGS_EMAILSENTEVENT_ATTACHCOUNT: WPC_ARGS_EMAILSENTEVENT = 7
WPC_ARGS_EMAILSENTEVENT_ATTACHMENTNAME: WPC_ARGS_EMAILSENTEVENT = 8
WPC_ARGS_EMAILSENTEVENT_EMAILACCOUNT: WPC_ARGS_EMAILSENTEVENT = 9
WPC_ARGS_EMAILSENTEVENT_CARGS: WPC_ARGS_EMAILSENTEVENT = 10
WPC_ARGS_FILEDOWNLOADEVENT = Int32
WPC_ARGS_FILEDOWNLOADEVENT_URL: WPC_ARGS_FILEDOWNLOADEVENT = 0
WPC_ARGS_FILEDOWNLOADEVENT_APPNAME: WPC_ARGS_FILEDOWNLOADEVENT = 1
WPC_ARGS_FILEDOWNLOADEVENT_VERSION: WPC_ARGS_FILEDOWNLOADEVENT = 2
WPC_ARGS_FILEDOWNLOADEVENT_BLOCKED: WPC_ARGS_FILEDOWNLOADEVENT = 3
WPC_ARGS_FILEDOWNLOADEVENT_PATH: WPC_ARGS_FILEDOWNLOADEVENT = 4
WPC_ARGS_FILEDOWNLOADEVENT_CARGS: WPC_ARGS_FILEDOWNLOADEVENT = 5
WPC_ARGS_GAMESTARTEVENT = Int32
WPC_ARGS_GAMESTARTEVENT_APPID: WPC_ARGS_GAMESTARTEVENT = 0
WPC_ARGS_GAMESTARTEVENT_INSTANCEID: WPC_ARGS_GAMESTARTEVENT = 1
WPC_ARGS_GAMESTARTEVENT_APPVERSION: WPC_ARGS_GAMESTARTEVENT = 2
WPC_ARGS_GAMESTARTEVENT_PATH: WPC_ARGS_GAMESTARTEVENT = 3
WPC_ARGS_GAMESTARTEVENT_RATING: WPC_ARGS_GAMESTARTEVENT = 4
WPC_ARGS_GAMESTARTEVENT_RATINGSYSTEM: WPC_ARGS_GAMESTARTEVENT = 5
WPC_ARGS_GAMESTARTEVENT_REASON: WPC_ARGS_GAMESTARTEVENT = 6
WPC_ARGS_GAMESTARTEVENT_DESCCOUNT: WPC_ARGS_GAMESTARTEVENT = 7
WPC_ARGS_GAMESTARTEVENT_DESCRIPTOR: WPC_ARGS_GAMESTARTEVENT = 8
WPC_ARGS_GAMESTARTEVENT_PID: WPC_ARGS_GAMESTARTEVENT = 9
WPC_ARGS_GAMESTARTEVENT_CARGS: WPC_ARGS_GAMESTARTEVENT = 10
WPC_ARGS_IMCONTACTEVENT = Int32
WPC_ARGS_IMCONTACTEVENT_APPNAME: WPC_ARGS_IMCONTACTEVENT = 0
WPC_ARGS_IMCONTACTEVENT_APPVERSION: WPC_ARGS_IMCONTACTEVENT = 1
WPC_ARGS_IMCONTACTEVENT_ACCOUNTNAME: WPC_ARGS_IMCONTACTEVENT = 2
WPC_ARGS_IMCONTACTEVENT_OLDNAME: WPC_ARGS_IMCONTACTEVENT = 3
WPC_ARGS_IMCONTACTEVENT_OLDID: WPC_ARGS_IMCONTACTEVENT = 4
WPC_ARGS_IMCONTACTEVENT_NEWNAME: WPC_ARGS_IMCONTACTEVENT = 5
WPC_ARGS_IMCONTACTEVENT_NEWID: WPC_ARGS_IMCONTACTEVENT = 6
WPC_ARGS_IMCONTACTEVENT_REASON: WPC_ARGS_IMCONTACTEVENT = 7
WPC_ARGS_IMCONTACTEVENT_CARGS: WPC_ARGS_IMCONTACTEVENT = 8
WPC_ARGS_IMFEATUREEVENT = Int32
WPC_ARGS_IMFEATUREEVENT_APPNAME: WPC_ARGS_IMFEATUREEVENT = 0
WPC_ARGS_IMFEATUREEVENT_APPVERSION: WPC_ARGS_IMFEATUREEVENT = 1
WPC_ARGS_IMFEATUREEVENT_ACCOUNTNAME: WPC_ARGS_IMFEATUREEVENT = 2
WPC_ARGS_IMFEATUREEVENT_CONVID: WPC_ARGS_IMFEATUREEVENT = 3
WPC_ARGS_IMFEATUREEVENT_MEDIATYPE: WPC_ARGS_IMFEATUREEVENT = 4
WPC_ARGS_IMFEATUREEVENT_REASON: WPC_ARGS_IMFEATUREEVENT = 5
WPC_ARGS_IMFEATUREEVENT_RECIPCOUNT: WPC_ARGS_IMFEATUREEVENT = 6
WPC_ARGS_IMFEATUREEVENT_RECIPIENT: WPC_ARGS_IMFEATUREEVENT = 7
WPC_ARGS_IMFEATUREEVENT_SENDER: WPC_ARGS_IMFEATUREEVENT = 8
WPC_ARGS_IMFEATUREEVENT_SENDERIP: WPC_ARGS_IMFEATUREEVENT = 9
WPC_ARGS_IMFEATUREEVENT_DATA: WPC_ARGS_IMFEATUREEVENT = 10
WPC_ARGS_IMFEATUREEVENT_CARGS: WPC_ARGS_IMFEATUREEVENT = 11
WPC_ARGS_MEDIADOWNLOADEVENT = Int32
WPC_ARGS_MEDIADOWNLOADEVENT_APPNAME: WPC_ARGS_MEDIADOWNLOADEVENT = 0
WPC_ARGS_MEDIADOWNLOADEVENT_APPVERSION: WPC_ARGS_MEDIADOWNLOADEVENT = 1
WPC_ARGS_MEDIADOWNLOADEVENT_MEDIATYPE: WPC_ARGS_MEDIADOWNLOADEVENT = 2
WPC_ARGS_MEDIADOWNLOADEVENT_PATH: WPC_ARGS_MEDIADOWNLOADEVENT = 3
WPC_ARGS_MEDIADOWNLOADEVENT_TITLE: WPC_ARGS_MEDIADOWNLOADEVENT = 4
WPC_ARGS_MEDIADOWNLOADEVENT_PML: WPC_ARGS_MEDIADOWNLOADEVENT = 5
WPC_ARGS_MEDIADOWNLOADEVENT_ALBUM: WPC_ARGS_MEDIADOWNLOADEVENT = 6
WPC_ARGS_MEDIADOWNLOADEVENT_EXPLICIT: WPC_ARGS_MEDIADOWNLOADEVENT = 7
WPC_ARGS_MEDIADOWNLOADEVENT_REASON: WPC_ARGS_MEDIADOWNLOADEVENT = 8
WPC_ARGS_MEDIADOWNLOADEVENT_CARGS: WPC_ARGS_MEDIADOWNLOADEVENT = 9
WPC_ARGS_MEDIAPLAYBACKEVENT = Int32
WPC_ARGS_MEDIAPLAYBACKEVENT_APPNAME: WPC_ARGS_MEDIAPLAYBACKEVENT = 0
WPC_ARGS_MEDIAPLAYBACKEVENT_APPVERSION: WPC_ARGS_MEDIAPLAYBACKEVENT = 1
WPC_ARGS_MEDIAPLAYBACKEVENT_MEDIATYPE: WPC_ARGS_MEDIAPLAYBACKEVENT = 2
WPC_ARGS_MEDIAPLAYBACKEVENT_PATH: WPC_ARGS_MEDIAPLAYBACKEVENT = 3
WPC_ARGS_MEDIAPLAYBACKEVENT_TITLE: WPC_ARGS_MEDIAPLAYBACKEVENT = 4
WPC_ARGS_MEDIAPLAYBACKEVENT_PML: WPC_ARGS_MEDIAPLAYBACKEVENT = 5
WPC_ARGS_MEDIAPLAYBACKEVENT_ALBUM: WPC_ARGS_MEDIAPLAYBACKEVENT = 6
WPC_ARGS_MEDIAPLAYBACKEVENT_EXPLICIT: WPC_ARGS_MEDIAPLAYBACKEVENT = 7
WPC_ARGS_MEDIAPLAYBACKEVENT_REASON: WPC_ARGS_MEDIAPLAYBACKEVENT = 8
WPC_ARGS_MEDIAPLAYBACKEVENT_CARGS: WPC_ARGS_MEDIAPLAYBACKEVENT = 9
WPC_ARGS_SAFERAPPBLOCKED = Int32
WPC_ARGS_SAFERAPPBLOCKED_TIMESTAMP: WPC_ARGS_SAFERAPPBLOCKED = 0
WPC_ARGS_SAFERAPPBLOCKED_USERID: WPC_ARGS_SAFERAPPBLOCKED = 1
WPC_ARGS_SAFERAPPBLOCKED_PATH: WPC_ARGS_SAFERAPPBLOCKED = 2
WPC_ARGS_SAFERAPPBLOCKED_RULEID: WPC_ARGS_SAFERAPPBLOCKED = 3
WPC_ARGS_SAFERAPPBLOCKED_CARGS: WPC_ARGS_SAFERAPPBLOCKED = 4
WPC_ARGS_SETTINGSCHANGEEVENT = Int32
WPC_ARGS_SETTINGSCHANGEEVENT_CLASS: WPC_ARGS_SETTINGSCHANGEEVENT = 0
WPC_ARGS_SETTINGSCHANGEEVENT_SETTING: WPC_ARGS_SETTINGSCHANGEEVENT = 1
WPC_ARGS_SETTINGSCHANGEEVENT_OWNER: WPC_ARGS_SETTINGSCHANGEEVENT = 2
WPC_ARGS_SETTINGSCHANGEEVENT_OLDVAL: WPC_ARGS_SETTINGSCHANGEEVENT = 3
WPC_ARGS_SETTINGSCHANGEEVENT_NEWVAL: WPC_ARGS_SETTINGSCHANGEEVENT = 4
WPC_ARGS_SETTINGSCHANGEEVENT_REASON: WPC_ARGS_SETTINGSCHANGEEVENT = 5
WPC_ARGS_SETTINGSCHANGEEVENT_OPTIONAL: WPC_ARGS_SETTINGSCHANGEEVENT = 6
WPC_ARGS_SETTINGSCHANGEEVENT_CARGS: WPC_ARGS_SETTINGSCHANGEEVENT = 7
WPC_ARGS_URLVISITEVENT = Int32
WPC_ARGS_URLVISITEVENT_URL: WPC_ARGS_URLVISITEVENT = 0
WPC_ARGS_URLVISITEVENT_APPNAME: WPC_ARGS_URLVISITEVENT = 1
WPC_ARGS_URLVISITEVENT_VERSION: WPC_ARGS_URLVISITEVENT = 2
WPC_ARGS_URLVISITEVENT_REASON: WPC_ARGS_URLVISITEVENT = 3
WPC_ARGS_URLVISITEVENT_RATINGSYSTEMID: WPC_ARGS_URLVISITEVENT = 4
WPC_ARGS_URLVISITEVENT_CATCOUNT: WPC_ARGS_URLVISITEVENT = 5
WPC_ARGS_URLVISITEVENT_CATEGORY: WPC_ARGS_URLVISITEVENT = 6
WPC_ARGS_URLVISITEVENT_CARGS: WPC_ARGS_URLVISITEVENT = 7
WPC_ARGS_WEBOVERRIDEEVENT = Int32
WPC_ARGS_WEBOVERRIDEEVENT_USERID: WPC_ARGS_WEBOVERRIDEEVENT = 0
WPC_ARGS_WEBOVERRIDEEVENT_URL: WPC_ARGS_WEBOVERRIDEEVENT = 1
WPC_ARGS_WEBOVERRIDEEVENT_REASON: WPC_ARGS_WEBOVERRIDEEVENT = 2
WPC_ARGS_WEBOVERRIDEEVENT_CARGS: WPC_ARGS_WEBOVERRIDEEVENT = 3
WPC_ARGS_WEBSITEVISITEVENT = Int32
WPC_ARGS_WEBSITEVISITEVENT_URL: WPC_ARGS_WEBSITEVISITEVENT = 0
WPC_ARGS_WEBSITEVISITEVENT_DECISION: WPC_ARGS_WEBSITEVISITEVENT = 1
WPC_ARGS_WEBSITEVISITEVENT_CATEGORIES: WPC_ARGS_WEBSITEVISITEVENT = 2
WPC_ARGS_WEBSITEVISITEVENT_BLOCKEDCATEGORIES: WPC_ARGS_WEBSITEVISITEVENT = 3
WPC_ARGS_WEBSITEVISITEVENT_SERIALIZEDAPPLICATION: WPC_ARGS_WEBSITEVISITEVENT = 4
WPC_ARGS_WEBSITEVISITEVENT_TITLE: WPC_ARGS_WEBSITEVISITEVENT = 5
WPC_ARGS_WEBSITEVISITEVENT_CONTENTTYPE: WPC_ARGS_WEBSITEVISITEVENT = 6
WPC_ARGS_WEBSITEVISITEVENT_REFERRER: WPC_ARGS_WEBSITEVISITEVENT = 7
WPC_ARGS_WEBSITEVISITEVENT_TELEMETRY: WPC_ARGS_WEBSITEVISITEVENT = 8
WPC_ARGS_WEBSITEVISITEVENT_CARGS: WPC_ARGS_WEBSITEVISITEVENT = 9
WPC_MEDIA_EXPLICIT = Int32
WPC_MEDIA_EXPLICIT_FALSE: WPC_MEDIA_EXPLICIT = 0
WPC_MEDIA_EXPLICIT_TRUE: WPC_MEDIA_EXPLICIT = 1
WPC_MEDIA_EXPLICIT_UNKNOWN: WPC_MEDIA_EXPLICIT = 2
WPC_MEDIA_TYPE = Int32
WPC_MEDIA_TYPE_OTHER: WPC_MEDIA_TYPE = 0
WPC_MEDIA_TYPE_DVD: WPC_MEDIA_TYPE = 1
WPC_MEDIA_TYPE_RECORDED_TV: WPC_MEDIA_TYPE = 2
WPC_MEDIA_TYPE_AUDIO_FILE: WPC_MEDIA_TYPE = 3
WPC_MEDIA_TYPE_CD_AUDIO: WPC_MEDIA_TYPE = 4
WPC_MEDIA_TYPE_VIDEO_FILE: WPC_MEDIA_TYPE = 5
WPC_MEDIA_TYPE_PICTURE_FILE: WPC_MEDIA_TYPE = 6
WPC_MEDIA_TYPE_MAX: WPC_MEDIA_TYPE = 7
WPC_SETTINGS = Int32
WPC_SETTINGS_WPC_EXTENSION_PATH: WPC_SETTINGS = 0
WPC_SETTINGS_WPC_EXTENSION_SILO: WPC_SETTINGS = 1
WPC_SETTINGS_WPC_EXTENSION_IMAGE_PATH: WPC_SETTINGS = 2
WPC_SETTINGS_WPC_EXTENSION_DISABLEDIMAGE_PATH: WPC_SETTINGS = 3
WPC_SETTINGS_WPC_EXTENSION_NAME: WPC_SETTINGS = 4
WPC_SETTINGS_WPC_EXTENSION_SUB_TITLE: WPC_SETTINGS = 5
WPC_SETTINGS_SYSTEM_CURRENT_RATING_SYSTEM: WPC_SETTINGS = 6
WPC_SETTINGS_SYSTEM_LAST_LOG_VIEW: WPC_SETTINGS = 7
WPC_SETTINGS_SYSTEM_LOG_VIEW_REMINDER_INTERVAL: WPC_SETTINGS = 8
WPC_SETTINGS_SYSTEM_HTTP_EXEMPTION_LIST: WPC_SETTINGS = 9
WPC_SETTINGS_SYSTEM_URL_EXEMPTION_LIST: WPC_SETTINGS = 10
WPC_SETTINGS_SYSTEM_FILTER_ID: WPC_SETTINGS = 11
WPC_SETTINGS_SYSTEM_FILTER_NAME: WPC_SETTINGS = 12
WPC_SETTINGS_SYSTEM_LOCALE: WPC_SETTINGS = 13
WPC_SETTINGS_ALLOW_BLOCK: WPC_SETTINGS = 14
WPC_SETTINGS_GAME_BLOCKED: WPC_SETTINGS = 15
WPC_SETTINGS_GAME_ALLOW_UNRATED: WPC_SETTINGS = 16
WPC_SETTINGS_GAME_MAX_ALLOWED: WPC_SETTINGS = 17
WPC_SETTINGS_GAME_DENIED_DESCRIPTORS: WPC_SETTINGS = 18
WPC_SETTINGS_USER_WPC_ENABLED: WPC_SETTINGS = 19
WPC_SETTINGS_USER_LOGGING_REQUIRED: WPC_SETTINGS = 20
WPC_SETTINGS_USER_HOURLY_RESTRICTIONS: WPC_SETTINGS = 21
WPC_SETTINGS_USER_OVERRRIDE_REQUESTS: WPC_SETTINGS = 22
WPC_SETTINGS_USER_LOGON_HOURS: WPC_SETTINGS = 23
WPC_SETTINGS_USER_APP_RESTRICTIONS: WPC_SETTINGS = 24
WPC_SETTINGS_WEB_FILTER_ON: WPC_SETTINGS = 25
WPC_SETTINGS_WEB_DOWNLOAD_BLOCKED: WPC_SETTINGS = 26
WPC_SETTINGS_WEB_FILTER_LEVEL: WPC_SETTINGS = 27
WPC_SETTINGS_WEB_BLOCKED_CATEGORY_LIST: WPC_SETTINGS = 28
WPC_SETTINGS_WEB_BLOCK_UNRATED: WPC_SETTINGS = 29
WPC_SETTINGS_WPC_ENABLED: WPC_SETTINGS = 30
WPC_SETTINGS_WPC_LOGGING_REQUIRED: WPC_SETTINGS = 31
WPC_SETTINGS_RATING_SYSTEM_PATH: WPC_SETTINGS = 32
WPC_SETTINGS_WPC_PROVIDER_CURRENT: WPC_SETTINGS = 33
WPC_SETTINGS_USER_TIME_ALLOWANCE: WPC_SETTINGS = 34
WPC_SETTINGS_USER_TIME_ALLOWANCE_RESTRICTIONS: WPC_SETTINGS = 35
WPC_SETTINGS_GAME_RESTRICTED: WPC_SETTINGS = 36
WPC_SETTING_COUNT: WPC_SETTINGS = 37
WindowsParentalControls = Guid('{e77cc89b-7401-4c04-8ced-149db35add04}')
WpcProviderSupport = Guid('{bb18c7a0-2186-4be0-97d8-04847b628e02}')
WpcSettingsProvider = Guid('{355dffaa-3b9f-435c-b428-5d44290bc5f2}')
make_head(_module, 'IWPCGamesSettings')
make_head(_module, 'IWPCProviderConfig')
make_head(_module, 'IWPCProviderState')
make_head(_module, 'IWPCProviderSupport')
make_head(_module, 'IWPCSettings')
make_head(_module, 'IWPCWebSettings')
make_head(_module, 'IWindowsParentalControls')
make_head(_module, 'IWindowsParentalControlsCore')
