from win32more import *
import win32more.Storage.EnhancedStorage
import win32more.Devices.PortableDevices
import win32more.Foundation
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Storage.EnhancedStorage, name, eval(f"_define_{name}()"))
    return getattr(win32more.Storage.EnhancedStorage, name)
GUID_DEVINTERFACE_ENHANCED_STORAGE_SILO = '3897f6a4-fd35-4bc8-a0b7-5dbba36adafa'
WPD_CATEGORY_ENHANCED_STORAGE = '91248166-b832-4ad4-baa4-7ca0b6b2798c'
ENHANCED_STORAGE_AUTHN_STATE_UNKNOWN = 0
ENHANCED_STORAGE_AUTHN_STATE_NO_AUTHENTICATION_REQUIRED = 1
ENHANCED_STORAGE_AUTHN_STATE_NOT_AUTHENTICATED = 2
ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATED = 3
ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATION_DENIED = 2147483649
ENHANCED_STORAGE_AUTHN_STATE_DEVICE_ERROR = 2147483650
CERT_TYPE_EMPTY = 0
CERT_TYPE_ASCm = 1
CERT_TYPE_PCp = 2
CERT_TYPE_ASCh = 3
CERT_TYPE_HCh = 4
CERT_TYPE_SIGNER = 6
CERT_VALIDATION_POLICY_RESERVED = 0
CERT_VALIDATION_POLICY_NONE = 1
CERT_VALIDATION_POLICY_BASIC = 2
CERT_VALIDATION_POLICY_EXTENDED = 3
CERT_CAPABILITY_HASH_ALG = 1
CERT_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY = 2
CERT_CAPABILITY_SIGNATURE_ALG = 3
CERT_CAPABILITY_CERTIFICATE_SUPPORT = 4
CERT_CAPABILITY_OPTIONAL_FEATURES = 5
CERT_MAX_CAPABILITY = 255
AUDIO_CHANNELCOUNT_MONO = 1
AUDIO_CHANNELCOUNT_STEREO = 2
CREATOROPENWITHUIOPTION_HIDDEN = 0
CREATOROPENWITHUIOPTION_VISIBLE = 1
ISDEFAULTSAVE_NONE = 0
ISDEFAULTSAVE_OWNER = 1
ISDEFAULTSAVE_NONOWNER = 2
ISDEFAULTSAVE_BOTH = 3
FILEOFFLINEAVAILABILITYSTATUS_NOTAVAILABLEOFFLINE = 0
FILEOFFLINEAVAILABILITYSTATUS_PARTIAL = 1
FILEOFFLINEAVAILABILITYSTATUS_COMPLETE = 2
FILEOFFLINEAVAILABILITYSTATUS_COMPLETE_PINNED = 3
FILEOFFLINEAVAILABILITYSTATUS_EXCLUDED = 4
FILEOFFLINEAVAILABILITYSTATUS_FOLDER_EMPTY = 5
FLAGSTATUS_NOTFLAGGED = 0
FLAGSTATUS_COMPLETED = 1
FLAGSTATUS_FOLLOWUP = 2
IMPORTANCE_LOW_MIN = 0
IMPORTANCE_LOW_SET = 1
IMPORTANCE_LOW_MAX = 1
IMPORTANCE_NORMAL_MIN = 2
IMPORTANCE_NORMAL_SET = 3
IMPORTANCE_NORMAL_MAX = 4
IMPORTANCE_HIGH_MIN = 5
IMPORTANCE_HIGH_SET = 5
IMPORTANCE_HIGH_MAX = 5
OFFLINEAVAILABILITY_NOT_AVAILABLE = 0
OFFLINEAVAILABILITY_AVAILABLE = 1
OFFLINEAVAILABILITY_ALWAYS_AVAILABLE = 2
OFFLINESTATUS_ONLINE = 0
OFFLINESTATUS_OFFLINE = 1
OFFLINESTATUS_OFFLINE_FORCED = 2
OFFLINESTATUS_OFFLINE_SLOW = 3
OFFLINESTATUS_OFFLINE_ERROR = 4
OFFLINESTATUS_OFFLINE_ITEM_VERSION_CONFLICT = 5
OFFLINESTATUS_OFFLINE_SUSPENDED = 6
RATING_ONE_STAR_MIN = 1
RATING_ONE_STAR_SET = 1
RATING_ONE_STAR_MAX = 12
RATING_TWO_STARS_MIN = 13
RATING_TWO_STARS_SET = 25
RATING_TWO_STARS_MAX = 37
RATING_THREE_STARS_MIN = 38
RATING_THREE_STARS_SET = 50
RATING_THREE_STARS_MAX = 62
RATING_FOUR_STARS_MIN = 63
RATING_FOUR_STARS_SET = 75
RATING_FOUR_STARS_MAX = 87
RATING_FIVE_STARS_MIN = 88
RATING_FIVE_STARS_SET = 99
RATING_FIVE_STARS_MAX = 99
SHARINGSTATUS_NOTSHARED = 0
SHARINGSTATUS_SHARED = 1
SHARINGSTATUS_PRIVATE = 2
STORAGE_PROVIDER_SHARINGSTATUS_NOTSHARED = 0
STORAGE_PROVIDER_SHARINGSTATUS_SHARED = 1
STORAGE_PROVIDER_SHARINGSTATUS_PRIVATE = 2
STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC = 3
STORAGE_PROVIDER_SHARINGSTATUS_SHARED_OWNED = 4
STORAGE_PROVIDER_SHARINGSTATUS_SHARED_COOWNED = 5
STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_OWNED = 6
STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_COOWNED = 7
BLUETOOTH_ADDRESS_TYPE_PUBLIC = 0
BLUETOOTH_ADDRESS_TYPE_RANDOM = 1
BLUETOOTH_CACHE_MODE_CACHED = 0
BLUETOOTH_CACHED_MODE_UNCACHED = 1
PLAYBACKSTATE_UNKNOWN = 0
PLAYBACKSTATE_STOPPED = 1
PLAYBACKSTATE_PLAYING = 2
PLAYBACKSTATE_TRANSITIONING = 3
PLAYBACKSTATE_PAUSED = 4
PLAYBACKSTATE_RECORDINGPAUSED = 5
PLAYBACKSTATE_RECORDING = 6
PLAYBACKSTATE_NOMEDIA = 7
LINK_STATUS_RESOLVED = 1
LINK_STATUS_BROKEN = 2
PHOTO_CONTRAST_NORMAL = 0
PHOTO_CONTRAST_SOFT = 1
PHOTO_CONTRAST_HARD = 2
PHOTO_EXPOSUREPROGRAM_UNKNOWN = 0
PHOTO_EXPOSUREPROGRAM_MANUAL = 1
PHOTO_EXPOSUREPROGRAM_NORMAL = 2
PHOTO_EXPOSUREPROGRAM_APERTURE = 3
PHOTO_EXPOSUREPROGRAM_SHUTTER = 4
PHOTO_EXPOSUREPROGRAM_CREATIVE = 5
PHOTO_EXPOSUREPROGRAM_ACTION = 6
PHOTO_EXPOSUREPROGRAM_PORTRAIT = 7
PHOTO_EXPOSUREPROGRAM_LANDSCAPE = 8
PHOTO_FLASH_NONE = 0
PHOTO_FLASH_FLASH = 1
PHOTO_FLASH_WITHOUTSTROBE = 5
PHOTO_FLASH_WITHSTROBE = 7
PHOTO_FLASH_FLASH_COMPULSORY = 9
PHOTO_FLASH_FLASH_COMPULSORY_NORETURNLIGHT = 13
PHOTO_FLASH_FLASH_COMPULSORY_RETURNLIGHT = 15
PHOTO_FLASH_NONE_COMPULSORY = 16
PHOTO_FLASH_NONE_AUTO = 24
PHOTO_FLASH_FLASH_AUTO = 25
PHOTO_FLASH_FLASH_AUTO_NORETURNLIGHT = 29
PHOTO_FLASH_FLASH_AUTO_RETURNLIGHT = 31
PHOTO_FLASH_NOFUNCTION = 32
PHOTO_FLASH_FLASH_REDEYE = 65
PHOTO_FLASH_FLASH_REDEYE_NORETURNLIGHT = 69
PHOTO_FLASH_FLASH_REDEYE_RETURNLIGHT = 71
PHOTO_FLASH_FLASH_COMPULSORY_REDEYE = 73
PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_NORETURNLIGHT = 77
PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_RETURNLIGHT = 79
PHOTO_FLASH_FLASH_AUTO_REDEYE = 89
PHOTO_FLASH_FLASH_AUTO_REDEYE_NORETURNLIGHT = 93
PHOTO_FLASH_FLASH_AUTO_REDEYE_RETURNLIGHT = 95
PHOTO_GAINCONTROL_NONE = 0
PHOTO_GAINCONTROL_LOWGAINUP = 1
PHOTO_GAINCONTROL_HIGHGAINUP = 2
PHOTO_GAINCONTROL_LOWGAINDOWN = 3
PHOTO_GAINCONTROL_HIGHGAINDOWN = 4
PHOTO_LIGHTSOURCE_UNKNOWN = 0
PHOTO_LIGHTSOURCE_DAYLIGHT = 1
PHOTO_LIGHTSOURCE_FLUORESCENT = 2
PHOTO_LIGHTSOURCE_TUNGSTEN = 3
PHOTO_LIGHTSOURCE_STANDARD_A = 17
PHOTO_LIGHTSOURCE_STANDARD_B = 18
PHOTO_LIGHTSOURCE_STANDARD_C = 19
PHOTO_LIGHTSOURCE_D55 = 20
PHOTO_LIGHTSOURCE_D65 = 21
PHOTO_LIGHTSOURCE_D75 = 22
PHOTO_PROGRAMMODE_NOTDEFINED = 0
PHOTO_PROGRAMMODE_MANUAL = 1
PHOTO_PROGRAMMODE_NORMAL = 2
PHOTO_PROGRAMMODE_APERTURE = 3
PHOTO_PROGRAMMODE_SHUTTER = 4
PHOTO_PROGRAMMODE_CREATIVE = 5
PHOTO_PROGRAMMODE_ACTION = 6
PHOTO_PROGRAMMODE_PORTRAIT = 7
PHOTO_PROGRAMMODE_LANDSCAPE = 8
PHOTO_SATURATION_NORMAL = 0
PHOTO_SATURATION_LOW = 1
PHOTO_SATURATION_HIGH = 2
PHOTO_SHARPNESS_NORMAL = 0
PHOTO_SHARPNESS_SOFT = 1
PHOTO_SHARPNESS_HARD = 2
PHOTO_WHITEBALANCE_AUTO = 0
PHOTO_WHITEBALANCE_MANUAL = 1
APPUSERMODEL_STARTPINOPTION_DEFAULT = 0
APPUSERMODEL_STARTPINOPTION_NOPINONINSTALL = 1
APPUSERMODEL_STARTPINOPTION_USERPINNED = 2
SYNC_HANDLERTYPE_OTHER = 0
SYNC_HANDLERTYPE_PROGRAMS = 1
SYNC_HANDLERTYPE_DEVICES = 2
SYNC_HANDLERTYPE_FOLDERS = 3
SYNC_HANDLERTYPE_WEBSERVICES = 4
SYNC_HANDLERTYPE_COMPUTERS = 5
SYNC_STATE_NOTSETUP = 0
SYNC_STATE_SYNCNOTRUN = 1
SYNC_STATE_IDLE = 2
SYNC_STATE_ERROR = 3
SYNC_STATE_PENDING = 4
SYNC_STATE_SYNCING = 5
ACT_AUTHORIZE_ON_RESUME = 1
ACT_AUTHORIZE_ON_SESSION_UNLOCK = 2
ACT_UNAUTHORIZE_ON_SUSPEND = 1
ACT_UNAUTHORIZE_ON_SESSION_LOCK = 2
ES_RESERVED_COM_ERROR_START = 0
ES_RESERVED_COM_ERROR_END = 511
ES_GENERAL_ERROR_START = 512
ES_GENERAL_ERROR_END = 1023
ES_AUTHN_ERROR_START = 1024
ES_AUTHN_ERROR_END = 1279
ES_RESERVED_SILO_ERROR_START = 1280
ES_RESERVED_SILO_ERROR_END = 4095
ES_PW_SILO_ERROR_START = 4352
ES_PW_SILO_ERROR_END = 4607
ES_RESERVED_SILO_SPECIFIC_ERROR_START = 4608
ES_RESERVED_SILO_SPECIFIC_ERROR_END = 49151
ES_VENDOR_ERROR_START = 49152
ES_VENDOR_ERROR_END = 65535
FACILITY_ENHANCED_STORAGE = 4
def _define_ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION_head():
    class ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION(Structure):
        pass
    return ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION
def _define_ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION():
    ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION = win32more.Storage.EnhancedStorage.ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION_head
    ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION._fields_ = [
        ("CurrentAdminFailures", Byte),
        ("CurrentUserFailures", Byte),
        ("TotalUserAuthenticationCount", UInt32),
        ("TotalAdminAuthenticationCount", UInt32),
        ("FipsCompliant", win32more.Foundation.BOOL),
        ("SecurityIDAvailable", win32more.Foundation.BOOL),
        ("InitializeInProgress", win32more.Foundation.BOOL),
        ("ITMSArmed", win32more.Foundation.BOOL),
        ("ITMSArmable", win32more.Foundation.BOOL),
        ("UserCreated", win32more.Foundation.BOOL),
        ("ResetOnPORDefault", win32more.Foundation.BOOL),
        ("ResetOnPORCurrent", win32more.Foundation.BOOL),
        ("MaxAdminFailures", Byte),
        ("MaxUserFailures", Byte),
        ("TimeToCompleteInitialization", UInt32),
        ("TimeRemainingToCompleteInitialization", UInt32),
        ("MinTimeToAuthenticate", UInt32),
        ("MaxAdminPasswordSize", Byte),
        ("MinAdminPasswordSize", Byte),
        ("MaxAdminHintSize", Byte),
        ("MaxUserPasswordSize", Byte),
        ("MinUserPasswordSize", Byte),
        ("MaxUserHintSize", Byte),
        ("MaxUserNameSize", Byte),
        ("MaxSiloNameSize", Byte),
        ("MaxChallengeSize", UInt16),
    ]
    return ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION
EnumEnhancedStorageACT = Guid('fe841493-835c-4fa3-b6cc-b4b2d4719848')
EnhancedStorageACT = Guid('af076a15-2ece-4ad4-bb21-29f040e176d8')
EnhancedStorageSilo = Guid('cb25220c-76c7-4fee-842b-f3383cd022bc')
EnhancedStorageSiloAction = Guid('886d29dd-b506-466b-9fbf-b44ff383fb3f')
def _define_ACT_AUTHORIZATION_STATE_head():
    class ACT_AUTHORIZATION_STATE(Structure):
        pass
    return ACT_AUTHORIZATION_STATE
def _define_ACT_AUTHORIZATION_STATE():
    ACT_AUTHORIZATION_STATE = win32more.Storage.EnhancedStorage.ACT_AUTHORIZATION_STATE_head
    ACT_AUTHORIZATION_STATE._fields_ = [
        ("ulState", UInt32),
    ]
    return ACT_AUTHORIZATION_STATE
def _define_SILO_INFO_head():
    class SILO_INFO(Structure):
        pass
    return SILO_INFO
def _define_SILO_INFO():
    SILO_INFO = win32more.Storage.EnhancedStorage.SILO_INFO_head
    SILO_INFO._fields_ = [
        ("ulSTID", UInt32),
        ("SpecificationMajor", Byte),
        ("SpecificationMinor", Byte),
        ("ImplementationMajor", Byte),
        ("ImplementationMinor", Byte),
        ("type", Byte),
        ("capabilities", Byte),
    ]
    return SILO_INFO
ACT_AUTHORIZATION_STATE_VALUE = Int32
ACT_UNAUTHORIZED = 0
ACT_AUTHORIZED = 1
def _define_IEnumEnhancedStorageACT_head():
    class IEnumEnhancedStorageACT(win32more.System.Com.IUnknown_head):
        Guid = Guid('09b224bd-1335-4631-a7ff-cfd3a92646d7')
    return IEnumEnhancedStorageACT
def _define_IEnumEnhancedStorageACT():
    IEnumEnhancedStorageACT = win32more.Storage.EnhancedStorage.IEnumEnhancedStorageACT_head
    IEnumEnhancedStorageACT.GetACTs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Storage.EnhancedStorage.IEnhancedStorageACT_head)),POINTER(UInt32), use_last_error=False)(3, 'GetACTs', ((1, 'pppIEnhancedStorageACTs'),(1, 'pcEnhancedStorageACTs'),)))
    IEnumEnhancedStorageACT.GetMatchingACT = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.EnhancedStorage.IEnhancedStorageACT_head), use_last_error=False)(4, 'GetMatchingACT', ((1, 'szVolume'),(1, 'ppIEnhancedStorageACT'),)))
    return IEnumEnhancedStorageACT
def _define_IEnhancedStorageACT_head():
    class IEnhancedStorageACT(win32more.System.Com.IUnknown_head):
        Guid = Guid('6e7781f4-e0f2-4239-b976-a01abab52930')
    return IEnhancedStorageACT
def _define_IEnhancedStorageACT():
    IEnhancedStorageACT = win32more.Storage.EnhancedStorage.IEnhancedStorageACT_head
    IEnhancedStorageACT.Authorize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(3, 'Authorize', ((1, 'hwndParent'),(1, 'dwFlags'),)))
    IEnhancedStorageACT.Unauthorize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Unauthorize', ()))
    IEnhancedStorageACT.GetAuthorizationState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.EnhancedStorage.ACT_AUTHORIZATION_STATE_head), use_last_error=False)(5, 'GetAuthorizationState', ((1, 'pState'),)))
    IEnhancedStorageACT.GetMatchingVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetMatchingVolume', ((1, 'ppwszVolume'),)))
    IEnhancedStorageACT.GetUniqueIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetUniqueIdentity', ((1, 'ppwszIdentity'),)))
    IEnhancedStorageACT.GetSilos = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Storage.EnhancedStorage.IEnhancedStorageSilo_head)),POINTER(UInt32), use_last_error=False)(8, 'GetSilos', ((1, 'pppIEnhancedStorageSilos'),(1, 'pcEnhancedStorageSilos'),)))
    return IEnhancedStorageACT
def _define_IEnhancedStorageACT2_head():
    class IEnhancedStorageACT2(win32more.Storage.EnhancedStorage.IEnhancedStorageACT_head):
        Guid = Guid('4da57d2e-8eb3-41f6-a07e-98b52b88242b')
    return IEnhancedStorageACT2
def _define_IEnhancedStorageACT2():
    IEnhancedStorageACT2 = win32more.Storage.EnhancedStorage.IEnhancedStorageACT2_head
    IEnhancedStorageACT2.GetDeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(9, 'GetDeviceName', ((1, 'ppwszDeviceName'),)))
    IEnhancedStorageACT2.IsDeviceRemovable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'IsDeviceRemovable', ((1, 'pIsDeviceRemovable'),)))
    return IEnhancedStorageACT2
def _define_IEnhancedStorageACT3_head():
    class IEnhancedStorageACT3(win32more.Storage.EnhancedStorage.IEnhancedStorageACT2_head):
        Guid = Guid('022150a1-113d-11df-bb61-001aa01bbc58')
    return IEnhancedStorageACT3
def _define_IEnhancedStorageACT3():
    IEnhancedStorageACT3 = win32more.Storage.EnhancedStorage.IEnhancedStorageACT3_head
    IEnhancedStorageACT3.UnauthorizeEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(11, 'UnauthorizeEx', ((1, 'dwFlags'),)))
    IEnhancedStorageACT3.IsQueueFrozen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'IsQueueFrozen', ((1, 'pIsQueueFrozen'),)))
    IEnhancedStorageACT3.GetShellExtSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'GetShellExtSupport', ((1, 'pShellExtSupport'),)))
    return IEnhancedStorageACT3
def _define_IEnhancedStorageSilo_head():
    class IEnhancedStorageSilo(win32more.System.Com.IUnknown_head):
        Guid = Guid('5aef78c6-2242-4703-bf49-44b29357a359')
    return IEnhancedStorageSilo
def _define_IEnhancedStorageSilo():
    IEnhancedStorageSilo = win32more.Storage.EnhancedStorage.IEnhancedStorageSilo_head
    IEnhancedStorageSilo.GetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.EnhancedStorage.SILO_INFO_head), use_last_error=False)(3, 'GetInfo', ((1, 'pSiloInfo'),)))
    IEnhancedStorageSilo.GetActions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Storage.EnhancedStorage.IEnhancedStorageSiloAction_head)),POINTER(UInt32), use_last_error=False)(4, 'GetActions', ((1, 'pppIEnhancedStorageSiloActions'),(1, 'pcEnhancedStorageSiloActions'),)))
    IEnhancedStorageSilo.SendCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(Byte),UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(5, 'SendCommand', ((1, 'Command'),(1, 'pbCommandBuffer'),(1, 'cbCommandBuffer'),(1, 'pbResponseBuffer'),(1, 'pcbResponseBuffer'),)))
    IEnhancedStorageSilo.GetPortableDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDevice_head), use_last_error=False)(6, 'GetPortableDevice', ((1, 'ppIPortableDevice'),)))
    IEnhancedStorageSilo.GetDevicePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetDevicePath', ((1, 'ppwszSiloDevicePath'),)))
    return IEnhancedStorageSilo
def _define_IEnhancedStorageSiloAction_head():
    class IEnhancedStorageSiloAction(win32more.System.Com.IUnknown_head):
        Guid = Guid('b6f7f311-206f-4ff8-9c4b-27efee77a86f')
    return IEnhancedStorageSiloAction
def _define_IEnhancedStorageSiloAction():
    IEnhancedStorageSiloAction = win32more.Storage.EnhancedStorage.IEnhancedStorageSiloAction_head
    IEnhancedStorageSiloAction.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetName', ((1, 'ppwszActionName'),)))
    IEnhancedStorageSiloAction.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetDescription', ((1, 'ppwszActionDescription'),)))
    IEnhancedStorageSiloAction.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Invoke', ()))
    return IEnhancedStorageSiloAction
__all__ = [
    "GUID_DEVINTERFACE_ENHANCED_STORAGE_SILO",
    "WPD_CATEGORY_ENHANCED_STORAGE",
    "ENHANCED_STORAGE_AUTHN_STATE_UNKNOWN",
    "ENHANCED_STORAGE_AUTHN_STATE_NO_AUTHENTICATION_REQUIRED",
    "ENHANCED_STORAGE_AUTHN_STATE_NOT_AUTHENTICATED",
    "ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATED",
    "ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATION_DENIED",
    "ENHANCED_STORAGE_AUTHN_STATE_DEVICE_ERROR",
    "CERT_TYPE_EMPTY",
    "CERT_TYPE_ASCm",
    "CERT_TYPE_PCp",
    "CERT_TYPE_ASCh",
    "CERT_TYPE_HCh",
    "CERT_TYPE_SIGNER",
    "CERT_VALIDATION_POLICY_RESERVED",
    "CERT_VALIDATION_POLICY_NONE",
    "CERT_VALIDATION_POLICY_BASIC",
    "CERT_VALIDATION_POLICY_EXTENDED",
    "CERT_CAPABILITY_HASH_ALG",
    "CERT_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY",
    "CERT_CAPABILITY_SIGNATURE_ALG",
    "CERT_CAPABILITY_CERTIFICATE_SUPPORT",
    "CERT_CAPABILITY_OPTIONAL_FEATURES",
    "CERT_MAX_CAPABILITY",
    "AUDIO_CHANNELCOUNT_MONO",
    "AUDIO_CHANNELCOUNT_STEREO",
    "CREATOROPENWITHUIOPTION_HIDDEN",
    "CREATOROPENWITHUIOPTION_VISIBLE",
    "ISDEFAULTSAVE_NONE",
    "ISDEFAULTSAVE_OWNER",
    "ISDEFAULTSAVE_NONOWNER",
    "ISDEFAULTSAVE_BOTH",
    "FILEOFFLINEAVAILABILITYSTATUS_NOTAVAILABLEOFFLINE",
    "FILEOFFLINEAVAILABILITYSTATUS_PARTIAL",
    "FILEOFFLINEAVAILABILITYSTATUS_COMPLETE",
    "FILEOFFLINEAVAILABILITYSTATUS_COMPLETE_PINNED",
    "FILEOFFLINEAVAILABILITYSTATUS_EXCLUDED",
    "FILEOFFLINEAVAILABILITYSTATUS_FOLDER_EMPTY",
    "FLAGSTATUS_NOTFLAGGED",
    "FLAGSTATUS_COMPLETED",
    "FLAGSTATUS_FOLLOWUP",
    "IMPORTANCE_LOW_MIN",
    "IMPORTANCE_LOW_SET",
    "IMPORTANCE_LOW_MAX",
    "IMPORTANCE_NORMAL_MIN",
    "IMPORTANCE_NORMAL_SET",
    "IMPORTANCE_NORMAL_MAX",
    "IMPORTANCE_HIGH_MIN",
    "IMPORTANCE_HIGH_SET",
    "IMPORTANCE_HIGH_MAX",
    "OFFLINEAVAILABILITY_NOT_AVAILABLE",
    "OFFLINEAVAILABILITY_AVAILABLE",
    "OFFLINEAVAILABILITY_ALWAYS_AVAILABLE",
    "OFFLINESTATUS_ONLINE",
    "OFFLINESTATUS_OFFLINE",
    "OFFLINESTATUS_OFFLINE_FORCED",
    "OFFLINESTATUS_OFFLINE_SLOW",
    "OFFLINESTATUS_OFFLINE_ERROR",
    "OFFLINESTATUS_OFFLINE_ITEM_VERSION_CONFLICT",
    "OFFLINESTATUS_OFFLINE_SUSPENDED",
    "RATING_ONE_STAR_MIN",
    "RATING_ONE_STAR_SET",
    "RATING_ONE_STAR_MAX",
    "RATING_TWO_STARS_MIN",
    "RATING_TWO_STARS_SET",
    "RATING_TWO_STARS_MAX",
    "RATING_THREE_STARS_MIN",
    "RATING_THREE_STARS_SET",
    "RATING_THREE_STARS_MAX",
    "RATING_FOUR_STARS_MIN",
    "RATING_FOUR_STARS_SET",
    "RATING_FOUR_STARS_MAX",
    "RATING_FIVE_STARS_MIN",
    "RATING_FIVE_STARS_SET",
    "RATING_FIVE_STARS_MAX",
    "SHARINGSTATUS_NOTSHARED",
    "SHARINGSTATUS_SHARED",
    "SHARINGSTATUS_PRIVATE",
    "STORAGE_PROVIDER_SHARINGSTATUS_NOTSHARED",
    "STORAGE_PROVIDER_SHARINGSTATUS_SHARED",
    "STORAGE_PROVIDER_SHARINGSTATUS_PRIVATE",
    "STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC",
    "STORAGE_PROVIDER_SHARINGSTATUS_SHARED_OWNED",
    "STORAGE_PROVIDER_SHARINGSTATUS_SHARED_COOWNED",
    "STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_OWNED",
    "STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_COOWNED",
    "BLUETOOTH_ADDRESS_TYPE_PUBLIC",
    "BLUETOOTH_ADDRESS_TYPE_RANDOM",
    "BLUETOOTH_CACHE_MODE_CACHED",
    "BLUETOOTH_CACHED_MODE_UNCACHED",
    "PLAYBACKSTATE_UNKNOWN",
    "PLAYBACKSTATE_STOPPED",
    "PLAYBACKSTATE_PLAYING",
    "PLAYBACKSTATE_TRANSITIONING",
    "PLAYBACKSTATE_PAUSED",
    "PLAYBACKSTATE_RECORDINGPAUSED",
    "PLAYBACKSTATE_RECORDING",
    "PLAYBACKSTATE_NOMEDIA",
    "LINK_STATUS_RESOLVED",
    "LINK_STATUS_BROKEN",
    "PHOTO_CONTRAST_NORMAL",
    "PHOTO_CONTRAST_SOFT",
    "PHOTO_CONTRAST_HARD",
    "PHOTO_EXPOSUREPROGRAM_UNKNOWN",
    "PHOTO_EXPOSUREPROGRAM_MANUAL",
    "PHOTO_EXPOSUREPROGRAM_NORMAL",
    "PHOTO_EXPOSUREPROGRAM_APERTURE",
    "PHOTO_EXPOSUREPROGRAM_SHUTTER",
    "PHOTO_EXPOSUREPROGRAM_CREATIVE",
    "PHOTO_EXPOSUREPROGRAM_ACTION",
    "PHOTO_EXPOSUREPROGRAM_PORTRAIT",
    "PHOTO_EXPOSUREPROGRAM_LANDSCAPE",
    "PHOTO_FLASH_NONE",
    "PHOTO_FLASH_FLASH",
    "PHOTO_FLASH_WITHOUTSTROBE",
    "PHOTO_FLASH_WITHSTROBE",
    "PHOTO_FLASH_FLASH_COMPULSORY",
    "PHOTO_FLASH_FLASH_COMPULSORY_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_COMPULSORY_RETURNLIGHT",
    "PHOTO_FLASH_NONE_COMPULSORY",
    "PHOTO_FLASH_NONE_AUTO",
    "PHOTO_FLASH_FLASH_AUTO",
    "PHOTO_FLASH_FLASH_AUTO_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_AUTO_RETURNLIGHT",
    "PHOTO_FLASH_NOFUNCTION",
    "PHOTO_FLASH_FLASH_REDEYE",
    "PHOTO_FLASH_FLASH_REDEYE_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_REDEYE_RETURNLIGHT",
    "PHOTO_FLASH_FLASH_COMPULSORY_REDEYE",
    "PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_RETURNLIGHT",
    "PHOTO_FLASH_FLASH_AUTO_REDEYE",
    "PHOTO_FLASH_FLASH_AUTO_REDEYE_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_AUTO_REDEYE_RETURNLIGHT",
    "PHOTO_GAINCONTROL_NONE",
    "PHOTO_GAINCONTROL_LOWGAINUP",
    "PHOTO_GAINCONTROL_HIGHGAINUP",
    "PHOTO_GAINCONTROL_LOWGAINDOWN",
    "PHOTO_GAINCONTROL_HIGHGAINDOWN",
    "PHOTO_LIGHTSOURCE_UNKNOWN",
    "PHOTO_LIGHTSOURCE_DAYLIGHT",
    "PHOTO_LIGHTSOURCE_FLUORESCENT",
    "PHOTO_LIGHTSOURCE_TUNGSTEN",
    "PHOTO_LIGHTSOURCE_STANDARD_A",
    "PHOTO_LIGHTSOURCE_STANDARD_B",
    "PHOTO_LIGHTSOURCE_STANDARD_C",
    "PHOTO_LIGHTSOURCE_D55",
    "PHOTO_LIGHTSOURCE_D65",
    "PHOTO_LIGHTSOURCE_D75",
    "PHOTO_PROGRAMMODE_NOTDEFINED",
    "PHOTO_PROGRAMMODE_MANUAL",
    "PHOTO_PROGRAMMODE_NORMAL",
    "PHOTO_PROGRAMMODE_APERTURE",
    "PHOTO_PROGRAMMODE_SHUTTER",
    "PHOTO_PROGRAMMODE_CREATIVE",
    "PHOTO_PROGRAMMODE_ACTION",
    "PHOTO_PROGRAMMODE_PORTRAIT",
    "PHOTO_PROGRAMMODE_LANDSCAPE",
    "PHOTO_SATURATION_NORMAL",
    "PHOTO_SATURATION_LOW",
    "PHOTO_SATURATION_HIGH",
    "PHOTO_SHARPNESS_NORMAL",
    "PHOTO_SHARPNESS_SOFT",
    "PHOTO_SHARPNESS_HARD",
    "PHOTO_WHITEBALANCE_AUTO",
    "PHOTO_WHITEBALANCE_MANUAL",
    "APPUSERMODEL_STARTPINOPTION_DEFAULT",
    "APPUSERMODEL_STARTPINOPTION_NOPINONINSTALL",
    "APPUSERMODEL_STARTPINOPTION_USERPINNED",
    "SYNC_HANDLERTYPE_OTHER",
    "SYNC_HANDLERTYPE_PROGRAMS",
    "SYNC_HANDLERTYPE_DEVICES",
    "SYNC_HANDLERTYPE_FOLDERS",
    "SYNC_HANDLERTYPE_WEBSERVICES",
    "SYNC_HANDLERTYPE_COMPUTERS",
    "SYNC_STATE_NOTSETUP",
    "SYNC_STATE_SYNCNOTRUN",
    "SYNC_STATE_IDLE",
    "SYNC_STATE_ERROR",
    "SYNC_STATE_PENDING",
    "SYNC_STATE_SYNCING",
    "ACT_AUTHORIZE_ON_RESUME",
    "ACT_AUTHORIZE_ON_SESSION_UNLOCK",
    "ACT_UNAUTHORIZE_ON_SUSPEND",
    "ACT_UNAUTHORIZE_ON_SESSION_LOCK",
    "ES_RESERVED_COM_ERROR_START",
    "ES_RESERVED_COM_ERROR_END",
    "ES_GENERAL_ERROR_START",
    "ES_GENERAL_ERROR_END",
    "ES_AUTHN_ERROR_START",
    "ES_AUTHN_ERROR_END",
    "ES_RESERVED_SILO_ERROR_START",
    "ES_RESERVED_SILO_ERROR_END",
    "ES_PW_SILO_ERROR_START",
    "ES_PW_SILO_ERROR_END",
    "ES_RESERVED_SILO_SPECIFIC_ERROR_START",
    "ES_RESERVED_SILO_SPECIFIC_ERROR_END",
    "ES_VENDOR_ERROR_START",
    "ES_VENDOR_ERROR_END",
    "FACILITY_ENHANCED_STORAGE",
    "ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION",
    "EnumEnhancedStorageACT",
    "EnhancedStorageACT",
    "EnhancedStorageSilo",
    "EnhancedStorageSiloAction",
    "ACT_AUTHORIZATION_STATE",
    "SILO_INFO",
    "ACT_AUTHORIZATION_STATE_VALUE",
    "ACT_UNAUTHORIZED",
    "ACT_AUTHORIZED",
    "IEnumEnhancedStorageACT",
    "IEnhancedStorageACT",
    "IEnhancedStorageACT2",
    "IEnhancedStorageACT3",
    "IEnhancedStorageSilo",
    "IEnhancedStorageSiloAction",
]
