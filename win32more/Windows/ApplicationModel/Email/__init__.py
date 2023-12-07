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
import win32more.Windows.ApplicationModel.Appointments
import win32more.Windows.ApplicationModel.Email
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Cryptography.Certificates
import win32more.Windows.Storage.Streams
import win32more.Windows.System
class EmailAttachment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailAttachment
    _classid_ = 'Windows.ApplicationModel.Email.EmailAttachment'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Email.EmailAttachment.CreateInstance(*args)
        elif len(args) == 2:
            instance = win32more.Windows.ApplicationModel.Email.EmailAttachment.Create(*args)
        elif len(args) == 3:
            instance = win32more.Windows.ApplicationModel.Email.EmailAttachment.Create(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Email.EmailAttachment: ...
    @winrt_overload
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Email.IEmailAttachmentFactory, fileName: WinRT_String, data: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.ApplicationModel.Email.EmailAttachment: ...
    @Create.register
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Email.IEmailAttachmentFactory2, fileName: WinRT_String, data: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, mimeType: WinRT_String) -> win32more.Windows.ApplicationModel.Email.EmailAttachment: ...
    @winrt_mixinmethod
    def get_FileName(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FileName(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentId(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentId(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentLocation(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentLocation(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DownloadState(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2) -> win32more.Windows.ApplicationModel.Email.EmailAttachmentDownloadState: ...
    @winrt_mixinmethod
    def put_DownloadState(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2, value: win32more.Windows.ApplicationModel.Email.EmailAttachmentDownloadState) -> Void: ...
    @winrt_mixinmethod
    def get_EstimatedDownloadSizeInBytes(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2) -> UInt64: ...
    @winrt_mixinmethod
    def put_EstimatedDownloadSizeInBytes(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def get_IsFromBaseMessage(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsInline(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInline(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MimeType(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_MimeType(self: win32more.Windows.ApplicationModel.Email.IEmailAttachment2, value: WinRT_String) -> Void: ...
    FileName = property(get_FileName, put_FileName)
    Data = property(get_Data, put_Data)
    Id = property(get_Id, None)
    ContentId = property(get_ContentId, put_ContentId)
    ContentLocation = property(get_ContentLocation, put_ContentLocation)
    DownloadState = property(get_DownloadState, put_DownloadState)
    EstimatedDownloadSizeInBytes = property(get_EstimatedDownloadSizeInBytes, put_EstimatedDownloadSizeInBytes)
    IsFromBaseMessage = property(get_IsFromBaseMessage, None)
    IsInline = property(get_IsInline, put_IsInline)
    MimeType = property(get_MimeType, put_MimeType)
EmailAttachmentDownloadState = Int32
EmailAttachmentDownloadState_NotDownloaded: EmailAttachmentDownloadState = 0
EmailAttachmentDownloadState_Downloading: EmailAttachmentDownloadState = 1
EmailAttachmentDownloadState_Downloaded: EmailAttachmentDownloadState = 2
EmailAttachmentDownloadState_Failed: EmailAttachmentDownloadState = 3
EmailBatchStatus = Int32
EmailBatchStatus_Success: EmailBatchStatus = 0
EmailBatchStatus_ServerSearchSyncManagerError: EmailBatchStatus = 1
EmailBatchStatus_ServerSearchUnknownError: EmailBatchStatus = 2
EmailCertificateValidationStatus = Int32
EmailCertificateValidationStatus_Success: EmailCertificateValidationStatus = 0
EmailCertificateValidationStatus_NoMatch: EmailCertificateValidationStatus = 1
EmailCertificateValidationStatus_InvalidUsage: EmailCertificateValidationStatus = 2
EmailCertificateValidationStatus_InvalidCertificate: EmailCertificateValidationStatus = 3
EmailCertificateValidationStatus_Revoked: EmailCertificateValidationStatus = 4
EmailCertificateValidationStatus_ChainRevoked: EmailCertificateValidationStatus = 5
EmailCertificateValidationStatus_RevocationServerFailure: EmailCertificateValidationStatus = 6
EmailCertificateValidationStatus_Expired: EmailCertificateValidationStatus = 7
EmailCertificateValidationStatus_Untrusted: EmailCertificateValidationStatus = 8
EmailCertificateValidationStatus_ServerError: EmailCertificateValidationStatus = 9
EmailCertificateValidationStatus_UnknownFailure: EmailCertificateValidationStatus = 10
class EmailConversation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailConversation
    _classid_ = 'Windows.ApplicationModel.Email.EmailConversation'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MailboxId(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FlagState(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> win32more.Windows.ApplicationModel.Email.EmailFlagState: ...
    @winrt_mixinmethod
    def get_HasAttachment(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> Boolean: ...
    @winrt_mixinmethod
    def get_Importance(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> win32more.Windows.ApplicationModel.Email.EmailImportance: ...
    @winrt_mixinmethod
    def get_LastEmailResponseKind(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> win32more.Windows.ApplicationModel.Email.EmailMessageResponseKind: ...
    @winrt_mixinmethod
    def get_MessageCount(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> UInt32: ...
    @winrt_mixinmethod
    def get_MostRecentMessageId(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MostRecentMessageTime(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Preview(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LatestSender(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> win32more.Windows.ApplicationModel.Email.EmailRecipient: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UnreadMessageCount(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> UInt32: ...
    @winrt_mixinmethod
    def FindMessagesAsync(self: win32more.Windows.ApplicationModel.Email.IEmailConversation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailMessage]]: ...
    @winrt_mixinmethod
    def FindMessagesWithCountAsync(self: win32more.Windows.ApplicationModel.Email.IEmailConversation, count: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailMessage]]: ...
    Id = property(get_Id, None)
    MailboxId = property(get_MailboxId, None)
    FlagState = property(get_FlagState, None)
    HasAttachment = property(get_HasAttachment, None)
    Importance = property(get_Importance, None)
    LastEmailResponseKind = property(get_LastEmailResponseKind, None)
    MessageCount = property(get_MessageCount, None)
    MostRecentMessageId = property(get_MostRecentMessageId, None)
    MostRecentMessageTime = property(get_MostRecentMessageTime, None)
    Preview = property(get_Preview, None)
    LatestSender = property(get_LatestSender, None)
    Subject = property(get_Subject, None)
    UnreadMessageCount = property(get_UnreadMessageCount, None)
class EmailConversationBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailConversationBatch
    _classid_ = 'Windows.ApplicationModel.Email.EmailConversationBatch'
    @winrt_mixinmethod
    def get_Conversations(self: win32more.Windows.ApplicationModel.Email.IEmailConversationBatch) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailConversation]: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Email.IEmailConversationBatch) -> win32more.Windows.ApplicationModel.Email.EmailBatchStatus: ...
    Conversations = property(get_Conversations, None)
    Status = property(get_Status, None)
class EmailConversationReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailConversationReader
    _classid_ = 'Windows.ApplicationModel.Email.EmailConversationReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: win32more.Windows.ApplicationModel.Email.IEmailConversationReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailConversationBatch]: ...
EmailFlagState = Int32
EmailFlagState_Unflagged: EmailFlagState = 0
EmailFlagState_Flagged: EmailFlagState = 1
EmailFlagState_Completed: EmailFlagState = 2
EmailFlagState_Cleared: EmailFlagState = 3
class EmailFolder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailFolder
    _classid_ = 'Windows.ApplicationModel.Email.EmailFolder'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: win32more.Windows.ApplicationModel.Email.IEmailFolder, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_MailboxId(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ParentFolderId(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.ApplicationModel.Email.IEmailFolder, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsSyncEnabled(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSyncEnabled(self: win32more.Windows.ApplicationModel.Email.IEmailFolder, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LastSuccessfulSyncTime(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_LastSuccessfulSyncTime(self: win32more.Windows.ApplicationModel.Email.IEmailFolder, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> win32more.Windows.ApplicationModel.Email.EmailSpecialFolderKind: ...
    @winrt_mixinmethod
    def CreateFolderAsync(self: win32more.Windows.ApplicationModel.Email.IEmailFolder, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailFolder]: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FindChildFoldersAsync(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailFolder]]: ...
    @winrt_mixinmethod
    def GetConversationReader(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> win32more.Windows.ApplicationModel.Email.EmailConversationReader: ...
    @winrt_mixinmethod
    def GetConversationReaderWithOptions(self: win32more.Windows.ApplicationModel.Email.IEmailFolder, options: win32more.Windows.ApplicationModel.Email.EmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailConversationReader: ...
    @winrt_mixinmethod
    def GetMessageAsync(self: win32more.Windows.ApplicationModel.Email.IEmailFolder, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMessage]: ...
    @winrt_mixinmethod
    def GetMessageReader(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> win32more.Windows.ApplicationModel.Email.EmailMessageReader: ...
    @winrt_mixinmethod
    def GetMessageReaderWithOptions(self: win32more.Windows.ApplicationModel.Email.IEmailFolder, options: win32more.Windows.ApplicationModel.Email.EmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailMessageReader: ...
    @winrt_mixinmethod
    def GetMessageCountsAsync(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailItemCounts]: ...
    @winrt_mixinmethod
    def TryMoveAsync(self: win32more.Windows.ApplicationModel.Email.IEmailFolder, newParentFolder: win32more.Windows.ApplicationModel.Email.EmailFolder) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryMoveWithNewNameAsync(self: win32more.Windows.ApplicationModel.Email.IEmailFolder, newParentFolder: win32more.Windows.ApplicationModel.Email.EmailFolder, newFolderName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySaveAsync(self: win32more.Windows.ApplicationModel.Email.IEmailFolder) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SaveMessageAsync(self: win32more.Windows.ApplicationModel.Email.IEmailFolder, message: win32more.Windows.ApplicationModel.Email.EmailMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    Id = property(get_Id, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
    MailboxId = property(get_MailboxId, None)
    ParentFolderId = property(get_ParentFolderId, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    IsSyncEnabled = property(get_IsSyncEnabled, put_IsSyncEnabled)
    LastSuccessfulSyncTime = property(get_LastSuccessfulSyncTime, put_LastSuccessfulSyncTime)
    Kind = property(get_Kind, None)
EmailImportance = Int32
EmailImportance_Normal: EmailImportance = 0
EmailImportance_High: EmailImportance = 1
EmailImportance_Low: EmailImportance = 2
class EmailIrmInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo
    _classid_ = 'Windows.ApplicationModel.Email.EmailIrmInfo'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Email.EmailIrmInfo.CreateInstance(*args)
        elif len(args) == 2:
            instance = win32more.Windows.ApplicationModel.Email.EmailIrmInfo.Create(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Email.EmailIrmInfo: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Email.IEmailIrmInfoFactory, expiration: win32more.Windows.Foundation.DateTime, irmTemplate: win32more.Windows.ApplicationModel.Email.EmailIrmTemplate) -> win32more.Windows.ApplicationModel.Email.EmailIrmInfo: ...
    @winrt_mixinmethod
    def get_CanEdit(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanEdit(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanExtractData(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanExtractData(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanForward(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanForward(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanModifyRecipientsOnResponse(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanModifyRecipientsOnResponse(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanPrintData(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanPrintData(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanRemoveIrmOnResponse(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanRemoveIrmOnResponse(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanReply(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanReply(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanReplyAll(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanReplyAll(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_ExpirationDate(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_IsIrmOriginator(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsIrmOriginator(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsProgramaticAccessAllowed(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsProgramaticAccessAllowed(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Template(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo) -> win32more.Windows.ApplicationModel.Email.EmailIrmTemplate: ...
    @winrt_mixinmethod
    def put_Template(self: win32more.Windows.ApplicationModel.Email.IEmailIrmInfo, value: win32more.Windows.ApplicationModel.Email.EmailIrmTemplate) -> Void: ...
    CanEdit = property(get_CanEdit, put_CanEdit)
    CanExtractData = property(get_CanExtractData, put_CanExtractData)
    CanForward = property(get_CanForward, put_CanForward)
    CanModifyRecipientsOnResponse = property(get_CanModifyRecipientsOnResponse, put_CanModifyRecipientsOnResponse)
    CanPrintData = property(get_CanPrintData, put_CanPrintData)
    CanRemoveIrmOnResponse = property(get_CanRemoveIrmOnResponse, put_CanRemoveIrmOnResponse)
    CanReply = property(get_CanReply, put_CanReply)
    CanReplyAll = property(get_CanReplyAll, put_CanReplyAll)
    ExpirationDate = property(get_ExpirationDate, put_ExpirationDate)
    IsIrmOriginator = property(get_IsIrmOriginator, put_IsIrmOriginator)
    IsProgramaticAccessAllowed = property(get_IsProgramaticAccessAllowed, put_IsProgramaticAccessAllowed)
    Template = property(get_Template, put_Template)
class EmailIrmTemplate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailIrmTemplate
    _classid_ = 'Windows.ApplicationModel.Email.EmailIrmTemplate'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Email.EmailIrmTemplate.CreateInstance(*args)
        elif len(args) == 3:
            instance = win32more.Windows.ApplicationModel.Email.EmailIrmTemplate.Create(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Email.EmailIrmTemplate: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Email.IEmailIrmTemplateFactory, id: WinRT_String, name: WinRT_String, description: WinRT_String) -> win32more.Windows.ApplicationModel.Email.EmailIrmTemplate: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Email.IEmailIrmTemplate) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.ApplicationModel.Email.IEmailIrmTemplate, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Email.IEmailIrmTemplate) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.Email.IEmailIrmTemplate, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Email.IEmailIrmTemplate) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.ApplicationModel.Email.IEmailIrmTemplate, value: WinRT_String) -> Void: ...
    Id = property(get_Id, put_Id)
    Description = property(get_Description, put_Description)
    Name = property(get_Name, put_Name)
class EmailItemCounts(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailItemCounts
    _classid_ = 'Windows.ApplicationModel.Email.EmailItemCounts'
    @winrt_mixinmethod
    def get_Flagged(self: win32more.Windows.ApplicationModel.Email.IEmailItemCounts) -> UInt32: ...
    @winrt_mixinmethod
    def get_Important(self: win32more.Windows.ApplicationModel.Email.IEmailItemCounts) -> UInt32: ...
    @winrt_mixinmethod
    def get_Total(self: win32more.Windows.ApplicationModel.Email.IEmailItemCounts) -> UInt32: ...
    @winrt_mixinmethod
    def get_Unread(self: win32more.Windows.ApplicationModel.Email.IEmailItemCounts) -> UInt32: ...
    Flagged = property(get_Flagged, None)
    Important = property(get_Important, None)
    Total = property(get_Total, None)
    Unread = property(get_Unread, None)
class EmailMailbox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailbox
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailbox'
    @winrt_mixinmethod
    def get_Capabilities(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> win32more.Windows.ApplicationModel.Email.EmailMailboxCapabilities: ...
    @winrt_mixinmethod
    def get_ChangeTracker(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> win32more.Windows.ApplicationModel.Email.EmailMailboxChangeTracker: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsOwnedByCurrentApp(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDataEncryptedUnderLock(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> Boolean: ...
    @winrt_mixinmethod
    def get_MailAddress(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_MailAddress(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_MailAddressAliases(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_OtherAppReadAccess(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> win32more.Windows.ApplicationModel.Email.EmailMailboxOtherAppReadAccess: ...
    @winrt_mixinmethod
    def put_OtherAppReadAccess(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, value: win32more.Windows.ApplicationModel.Email.EmailMailboxOtherAppReadAccess) -> Void: ...
    @winrt_mixinmethod
    def get_OtherAppWriteAccess(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> win32more.Windows.ApplicationModel.Email.EmailMailboxOtherAppWriteAccess: ...
    @winrt_mixinmethod
    def put_OtherAppWriteAccess(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, value: win32more.Windows.ApplicationModel.Email.EmailMailboxOtherAppWriteAccess) -> Void: ...
    @winrt_mixinmethod
    def get_Policies(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> win32more.Windows.ApplicationModel.Email.EmailMailboxPolicies: ...
    @winrt_mixinmethod
    def get_SourceDisplayName(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SyncManager(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> win32more.Windows.ApplicationModel.Email.EmailMailboxSyncManager: ...
    @winrt_mixinmethod
    def get_UserDataAccountId(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetConversationReader(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> win32more.Windows.ApplicationModel.Email.EmailConversationReader: ...
    @winrt_mixinmethod
    def GetConversationReaderWithOptions(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, options: win32more.Windows.ApplicationModel.Email.EmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailConversationReader: ...
    @winrt_mixinmethod
    def GetMessageReader(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> win32more.Windows.ApplicationModel.Email.EmailMessageReader: ...
    @winrt_mixinmethod
    def GetMessageReaderWithOptions(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, options: win32more.Windows.ApplicationModel.Email.EmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailMessageReader: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetConversationAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailConversation]: ...
    @winrt_mixinmethod
    def GetFolderAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailFolder]: ...
    @winrt_mixinmethod
    def GetMessageAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMessage]: ...
    @winrt_mixinmethod
    def GetSpecialFolderAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, folderType: win32more.Windows.ApplicationModel.Email.EmailSpecialFolderKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailFolder]: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MarkMessageAsSeenAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, messageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MarkFolderAsSeenAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, folderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MarkMessageReadAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, messageId: WinRT_String, isRead: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ChangeMessageFlagStateAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, messageId: WinRT_String, flagState: win32more.Windows.ApplicationModel.Email.EmailFlagState) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def TryMoveMessageAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, messageId: WinRT_String, newParentFolderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryMoveFolderAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, folderId: WinRT_String, newParentFolderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryMoveFolderWithNewNameAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, folderId: WinRT_String, newParentFolderId: WinRT_String, newFolderName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def DeleteMessageAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, messageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MarkFolderSyncEnabledAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, folderId: WinRT_String, isSyncEnabled: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SendMessageAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, message: win32more.Windows.ApplicationModel.Email.EmailMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SaveDraftAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, message: win32more.Windows.ApplicationModel.Email.EmailMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DownloadMessageAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, messageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DownloadAttachmentAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, attachmentId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CreateResponseMessageAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, messageId: WinRT_String, responseType: win32more.Windows.ApplicationModel.Email.EmailMessageResponseKind, subject: WinRT_String, responseHeaderType: win32more.Windows.ApplicationModel.Email.EmailMessageBodyKind, responseHeader: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMessage]: ...
    @winrt_mixinmethod
    def TryUpdateMeetingResponseAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, meeting: win32more.Windows.ApplicationModel.Email.EmailMessage, response: win32more.Windows.ApplicationModel.Email.EmailMeetingResponseType, subject: WinRT_String, comment: WinRT_String, sendUpdate: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryForwardMeetingAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, meeting: win32more.Windows.ApplicationModel.Email.EmailMessage, recipients: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Email.EmailRecipient], subject: WinRT_String, forwardHeaderType: win32more.Windows.ApplicationModel.Email.EmailMessageBodyKind, forwardHeader: WinRT_String, comment: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryProposeNewTimeForMeetingAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, meeting: win32more.Windows.ApplicationModel.Email.EmailMessage, newStartTime: win32more.Windows.Foundation.DateTime, newDuration: win32more.Windows.Foundation.TimeSpan, subject: WinRT_String, comment: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_MailboxChanged(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, pHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.EmailMailbox, win32more.Windows.ApplicationModel.Email.EmailMailboxChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MailboxChanged(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SmartSendMessageAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, message: win32more.Windows.ApplicationModel.Email.EmailMessage, smartSend: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def TrySetAutoReplySettingsAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, autoReplySettings: win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryGetAutoReplySettingsAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox, requestedFormat: win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings]: ...
    @winrt_mixinmethod
    def get_LinkedMailboxId(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NetworkAccountId(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NetworkId(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox2) -> WinRT_String: ...
    @winrt_mixinmethod
    def ResolveRecipientsAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox3, recipients: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailRecipientResolutionResult]]: ...
    @winrt_mixinmethod
    def ValidateCertificatesAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox3, certificates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.Certificate]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailCertificateValidationStatus]]: ...
    @winrt_mixinmethod
    def TryEmptyFolderAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox3, folderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailboxEmptyFolderStatus]: ...
    @winrt_mixinmethod
    def TryCreateFolderAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox3, parentFolderId: WinRT_String, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailboxCreateFolderResult]: ...
    @winrt_mixinmethod
    def TryDeleteFolderAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox3, folderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailboxDeleteFolderStatus]: ...
    @winrt_mixinmethod
    def RegisterSyncManagerAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox4) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetChangeTracker(self: win32more.Windows.ApplicationModel.Email.IEmailMailbox5, identity: WinRT_String) -> win32more.Windows.ApplicationModel.Email.EmailMailboxChangeTracker: ...
    Capabilities = property(get_Capabilities, None)
    ChangeTracker = property(get_ChangeTracker, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Id = property(get_Id, None)
    IsOwnedByCurrentApp = property(get_IsOwnedByCurrentApp, None)
    IsDataEncryptedUnderLock = property(get_IsDataEncryptedUnderLock, None)
    MailAddress = property(get_MailAddress, put_MailAddress)
    MailAddressAliases = property(get_MailAddressAliases, None)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    OtherAppWriteAccess = property(get_OtherAppWriteAccess, put_OtherAppWriteAccess)
    Policies = property(get_Policies, None)
    SourceDisplayName = property(get_SourceDisplayName, None)
    SyncManager = property(get_SyncManager, None)
    UserDataAccountId = property(get_UserDataAccountId, None)
    LinkedMailboxId = property(get_LinkedMailboxId, None)
    NetworkAccountId = property(get_NetworkAccountId, None)
    NetworkId = property(get_NetworkId, None)
class EmailMailboxAction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailboxAction
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailboxAction'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAction) -> win32more.Windows.ApplicationModel.Email.EmailMailboxActionKind: ...
    @winrt_mixinmethod
    def get_ChangeNumber(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAction) -> UInt64: ...
    Kind = property(get_Kind, None)
    ChangeNumber = property(get_ChangeNumber, None)
EmailMailboxActionKind = Int32
EmailMailboxActionKind_MarkMessageAsSeen: EmailMailboxActionKind = 0
EmailMailboxActionKind_MarkMessageRead: EmailMailboxActionKind = 1
EmailMailboxActionKind_ChangeMessageFlagState: EmailMailboxActionKind = 2
EmailMailboxActionKind_MoveMessage: EmailMailboxActionKind = 3
EmailMailboxActionKind_SaveDraft: EmailMailboxActionKind = 4
EmailMailboxActionKind_SendMessage: EmailMailboxActionKind = 5
EmailMailboxActionKind_CreateResponseReplyMessage: EmailMailboxActionKind = 6
EmailMailboxActionKind_CreateResponseReplyAllMessage: EmailMailboxActionKind = 7
EmailMailboxActionKind_CreateResponseForwardMessage: EmailMailboxActionKind = 8
EmailMailboxActionKind_MoveFolder: EmailMailboxActionKind = 9
EmailMailboxActionKind_MarkFolderForSyncEnabled: EmailMailboxActionKind = 10
EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation = Int32
EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation_None: EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation = 0
EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation_StrongAlgorithm: EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation = 1
EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation_AnyAlgorithm: EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation = 2
class EmailMailboxAutoReply(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReply
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailboxAutoReply'
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReply) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReply, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Response(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReply) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Response(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReply, value: WinRT_String) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Response = property(get_Response, put_Response)
EmailMailboxAutoReplyMessageResponseKind = Int32
EmailMailboxAutoReplyMessageResponseKind_Html: EmailMailboxAutoReplyMessageResponseKind = 0
EmailMailboxAutoReplyMessageResponseKind_PlainText: EmailMailboxAutoReplyMessageResponseKind = 1
class EmailMailboxAutoReplySettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseKind(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind: ...
    @winrt_mixinmethod
    def put_ResponseKind(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings, value: win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_StartTime(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_EndTime(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_EndTime(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_InternalReply(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReply: ...
    @winrt_mixinmethod
    def get_KnownExternalReply(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReply: ...
    @winrt_mixinmethod
    def get_UnknownExternalReply(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReply: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    ResponseKind = property(get_ResponseKind, put_ResponseKind)
    StartTime = property(get_StartTime, put_StartTime)
    EndTime = property(get_EndTime, put_EndTime)
    InternalReply = property(get_InternalReply, None)
    KnownExternalReply = property(get_KnownExternalReply, None)
    UnknownExternalReply = property(get_UnknownExternalReply, None)
class EmailMailboxCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailboxCapabilities'
    @winrt_mixinmethod
    def get_CanForwardMeetings(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanGetAndSetExternalAutoReplies(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanGetAndSetInternalAutoReplies(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanUpdateMeetingResponses(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanServerSearchFolders(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanServerSearchMailbox(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanProposeNewTimeForMeetings(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanSmartSend(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanResolveRecipients(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanValidateCertificates(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanEmptyFolder(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanCreateFolder(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanDeleteFolder(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanMoveFolder(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanForwardMeetings(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanGetAndSetExternalAutoReplies(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanGetAndSetInternalAutoReplies(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanUpdateMeetingResponses(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanServerSearchFolders(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanServerSearchMailbox(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanProposeNewTimeForMeetings(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanSmartSend(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanResolveRecipients(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanValidateCertificates(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanEmptyFolder(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanCreateFolder(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanDeleteFolder(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_CanMoveFolder(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCapabilities3, value: Boolean) -> Void: ...
    CanForwardMeetings = property(get_CanForwardMeetings, put_CanForwardMeetings)
    CanGetAndSetExternalAutoReplies = property(get_CanGetAndSetExternalAutoReplies, put_CanGetAndSetExternalAutoReplies)
    CanGetAndSetInternalAutoReplies = property(get_CanGetAndSetInternalAutoReplies, put_CanGetAndSetInternalAutoReplies)
    CanUpdateMeetingResponses = property(get_CanUpdateMeetingResponses, put_CanUpdateMeetingResponses)
    CanServerSearchFolders = property(get_CanServerSearchFolders, put_CanServerSearchFolders)
    CanServerSearchMailbox = property(get_CanServerSearchMailbox, put_CanServerSearchMailbox)
    CanProposeNewTimeForMeetings = property(get_CanProposeNewTimeForMeetings, put_CanProposeNewTimeForMeetings)
    CanSmartSend = property(get_CanSmartSend, put_CanSmartSend)
    CanResolveRecipients = property(get_CanResolveRecipients, put_CanResolveRecipients)
    CanValidateCertificates = property(get_CanValidateCertificates, put_CanValidateCertificates)
    CanEmptyFolder = property(get_CanEmptyFolder, put_CanEmptyFolder)
    CanCreateFolder = property(get_CanCreateFolder, put_CanCreateFolder)
    CanDeleteFolder = property(get_CanDeleteFolder, put_CanDeleteFolder)
    CanMoveFolder = property(get_CanMoveFolder, put_CanMoveFolder)
class EmailMailboxChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailboxChange
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailboxChange'
    @winrt_mixinmethod
    def get_ChangeType(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChange) -> win32more.Windows.ApplicationModel.Email.EmailMailboxChangeType: ...
    @winrt_mixinmethod
    def get_MailboxActions(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChange) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Email.EmailMailboxAction]: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChange) -> win32more.Windows.ApplicationModel.Email.EmailMessage: ...
    @winrt_mixinmethod
    def get_Folder(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChange) -> win32more.Windows.ApplicationModel.Email.EmailFolder: ...
    ChangeType = property(get_ChangeType, None)
    MailboxActions = property(get_MailboxActions, None)
    Message = property(get_Message, None)
    Folder = property(get_Folder, None)
class EmailMailboxChangeReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangeReader
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailboxChangeReader'
    @winrt_mixinmethod
    def AcceptChanges(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangeReader) -> Void: ...
    @winrt_mixinmethod
    def AcceptChangesThrough(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangeReader, lastChangeToAcknowledge: win32more.Windows.ApplicationModel.Email.EmailMailboxChange) -> Void: ...
    @winrt_mixinmethod
    def ReadBatchAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangeReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailMailboxChange]]: ...
class EmailMailboxChangeTracker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangeTracker
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailboxChangeTracker'
    @winrt_mixinmethod
    def get_IsTracking(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangeTracker) -> Boolean: ...
    @winrt_mixinmethod
    def Enable(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangeTracker) -> Void: ...
    @winrt_mixinmethod
    def GetChangeReader(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangeTracker) -> win32more.Windows.ApplicationModel.Email.EmailMailboxChangeReader: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangeTracker) -> Void: ...
    IsTracking = property(get_IsTracking, None)
EmailMailboxChangeType = Int32
EmailMailboxChangeType_MessageCreated: EmailMailboxChangeType = 0
EmailMailboxChangeType_MessageModified: EmailMailboxChangeType = 1
EmailMailboxChangeType_MessageDeleted: EmailMailboxChangeType = 2
EmailMailboxChangeType_FolderCreated: EmailMailboxChangeType = 3
EmailMailboxChangeType_FolderModified: EmailMailboxChangeType = 4
EmailMailboxChangeType_FolderDeleted: EmailMailboxChangeType = 5
EmailMailboxChangeType_ChangeTrackingLost: EmailMailboxChangeType = 6
class EmailMailboxChangedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangedDeferral
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailboxChangedDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangedDeferral) -> Void: ...
class EmailMailboxChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailboxChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxChangedEventArgs) -> win32more.Windows.ApplicationModel.Email.EmailMailboxChangedDeferral: ...
class EmailMailboxCreateFolderResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailboxCreateFolderResult
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailboxCreateFolderResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCreateFolderResult) -> win32more.Windows.ApplicationModel.Email.EmailMailboxCreateFolderStatus: ...
    @winrt_mixinmethod
    def get_Folder(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxCreateFolderResult) -> win32more.Windows.ApplicationModel.Email.EmailFolder: ...
    Status = property(get_Status, None)
    Folder = property(get_Folder, None)
EmailMailboxCreateFolderStatus = Int32
EmailMailboxCreateFolderStatus_Success: EmailMailboxCreateFolderStatus = 0
EmailMailboxCreateFolderStatus_NetworkError: EmailMailboxCreateFolderStatus = 1
EmailMailboxCreateFolderStatus_PermissionsError: EmailMailboxCreateFolderStatus = 2
EmailMailboxCreateFolderStatus_ServerError: EmailMailboxCreateFolderStatus = 3
EmailMailboxCreateFolderStatus_UnknownFailure: EmailMailboxCreateFolderStatus = 4
EmailMailboxCreateFolderStatus_NameCollision: EmailMailboxCreateFolderStatus = 5
EmailMailboxCreateFolderStatus_ServerRejected: EmailMailboxCreateFolderStatus = 6
EmailMailboxDeleteFolderStatus = Int32
EmailMailboxDeleteFolderStatus_Success: EmailMailboxDeleteFolderStatus = 0
EmailMailboxDeleteFolderStatus_NetworkError: EmailMailboxDeleteFolderStatus = 1
EmailMailboxDeleteFolderStatus_PermissionsError: EmailMailboxDeleteFolderStatus = 2
EmailMailboxDeleteFolderStatus_ServerError: EmailMailboxDeleteFolderStatus = 3
EmailMailboxDeleteFolderStatus_UnknownFailure: EmailMailboxDeleteFolderStatus = 4
EmailMailboxDeleteFolderStatus_CouldNotDeleteEverything: EmailMailboxDeleteFolderStatus = 5
EmailMailboxEmptyFolderStatus = Int32
EmailMailboxEmptyFolderStatus_Success: EmailMailboxEmptyFolderStatus = 0
EmailMailboxEmptyFolderStatus_NetworkError: EmailMailboxEmptyFolderStatus = 1
EmailMailboxEmptyFolderStatus_PermissionsError: EmailMailboxEmptyFolderStatus = 2
EmailMailboxEmptyFolderStatus_ServerError: EmailMailboxEmptyFolderStatus = 3
EmailMailboxEmptyFolderStatus_UnknownFailure: EmailMailboxEmptyFolderStatus = 4
EmailMailboxEmptyFolderStatus_CouldNotDeleteEverything: EmailMailboxEmptyFolderStatus = 5
EmailMailboxOtherAppReadAccess = Int32
EmailMailboxOtherAppReadAccess_SystemOnly: EmailMailboxOtherAppReadAccess = 0
EmailMailboxOtherAppReadAccess_Full: EmailMailboxOtherAppReadAccess = 1
EmailMailboxOtherAppReadAccess_None: EmailMailboxOtherAppReadAccess = 2
EmailMailboxOtherAppWriteAccess = Int32
EmailMailboxOtherAppWriteAccess_None: EmailMailboxOtherAppWriteAccess = 0
EmailMailboxOtherAppWriteAccess_Limited: EmailMailboxOtherAppWriteAccess = 1
class EmailMailboxPolicies(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailboxPolicies'
    @winrt_mixinmethod
    def get_AllowedSmimeEncryptionAlgorithmNegotiation(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation: ...
    @winrt_mixinmethod
    def get_AllowSmimeSoftCertificates(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies) -> Boolean: ...
    @winrt_mixinmethod
    def get_RequiredSmimeEncryptionAlgorithm(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies) -> win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.Email.EmailMailboxSmimeEncryptionAlgorithm]: ...
    @winrt_mixinmethod
    def get_RequiredSmimeSigningAlgorithm(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies) -> win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.Email.EmailMailboxSmimeSigningAlgorithm]: ...
    @winrt_mixinmethod
    def get_MustEncryptSmimeMessages(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies2) -> Boolean: ...
    @winrt_mixinmethod
    def get_MustSignSmimeMessages(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowedSmimeEncryptionAlgorithmNegotiation(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies3, value: win32more.Windows.ApplicationModel.Email.EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation) -> Void: ...
    @winrt_mixinmethod
    def put_AllowSmimeSoftCertificates(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_RequiredSmimeEncryptionAlgorithm(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies3, value: win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.Email.EmailMailboxSmimeEncryptionAlgorithm]) -> Void: ...
    @winrt_mixinmethod
    def put_RequiredSmimeSigningAlgorithm(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies3, value: win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.Email.EmailMailboxSmimeSigningAlgorithm]) -> Void: ...
    @winrt_mixinmethod
    def put_MustEncryptSmimeMessages(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_MustSignSmimeMessages(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxPolicies3, value: Boolean) -> Void: ...
    AllowedSmimeEncryptionAlgorithmNegotiation = property(get_AllowedSmimeEncryptionAlgorithmNegotiation, put_AllowedSmimeEncryptionAlgorithmNegotiation)
    AllowSmimeSoftCertificates = property(get_AllowSmimeSoftCertificates, put_AllowSmimeSoftCertificates)
    RequiredSmimeEncryptionAlgorithm = property(get_RequiredSmimeEncryptionAlgorithm, put_RequiredSmimeEncryptionAlgorithm)
    RequiredSmimeSigningAlgorithm = property(get_RequiredSmimeSigningAlgorithm, put_RequiredSmimeSigningAlgorithm)
    MustEncryptSmimeMessages = property(get_MustEncryptSmimeMessages, put_MustEncryptSmimeMessages)
    MustSignSmimeMessages = property(get_MustSignSmimeMessages, put_MustSignSmimeMessages)
EmailMailboxSmimeEncryptionAlgorithm = Int32
EmailMailboxSmimeEncryptionAlgorithm_Any: EmailMailboxSmimeEncryptionAlgorithm = 0
EmailMailboxSmimeEncryptionAlgorithm_TripleDes: EmailMailboxSmimeEncryptionAlgorithm = 1
EmailMailboxSmimeEncryptionAlgorithm_Des: EmailMailboxSmimeEncryptionAlgorithm = 2
EmailMailboxSmimeEncryptionAlgorithm_RC2128Bit: EmailMailboxSmimeEncryptionAlgorithm = 3
EmailMailboxSmimeEncryptionAlgorithm_RC264Bit: EmailMailboxSmimeEncryptionAlgorithm = 4
EmailMailboxSmimeEncryptionAlgorithm_RC240Bit: EmailMailboxSmimeEncryptionAlgorithm = 5
EmailMailboxSmimeSigningAlgorithm = Int32
EmailMailboxSmimeSigningAlgorithm_Any: EmailMailboxSmimeSigningAlgorithm = 0
EmailMailboxSmimeSigningAlgorithm_Sha1: EmailMailboxSmimeSigningAlgorithm = 1
EmailMailboxSmimeSigningAlgorithm_MD5: EmailMailboxSmimeSigningAlgorithm = 2
class EmailMailboxSyncManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMailboxSyncManager
    _classid_ = 'Windows.ApplicationModel.Email.EmailMailboxSyncManager'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxSyncManager) -> win32more.Windows.ApplicationModel.Email.EmailMailboxSyncStatus: ...
    @winrt_mixinmethod
    def get_LastSuccessfulSyncTime(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxSyncManager) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_LastAttemptedSyncTime(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxSyncManager) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def SyncAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxSyncManager) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_SyncStatusChanged(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxSyncManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.EmailMailboxSyncManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SyncStatusChanged(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxSyncManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxSyncManager2, value: win32more.Windows.ApplicationModel.Email.EmailMailboxSyncStatus) -> Void: ...
    @winrt_mixinmethod
    def put_LastSuccessfulSyncTime(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxSyncManager2, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def put_LastAttemptedSyncTime(self: win32more.Windows.ApplicationModel.Email.IEmailMailboxSyncManager2, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    Status = property(get_Status, put_Status)
    LastSuccessfulSyncTime = property(get_LastSuccessfulSyncTime, put_LastSuccessfulSyncTime)
    LastAttemptedSyncTime = property(get_LastAttemptedSyncTime, put_LastAttemptedSyncTime)
EmailMailboxSyncStatus = Int32
EmailMailboxSyncStatus_Idle: EmailMailboxSyncStatus = 0
EmailMailboxSyncStatus_Syncing: EmailMailboxSyncStatus = 1
EmailMailboxSyncStatus_UpToDate: EmailMailboxSyncStatus = 2
EmailMailboxSyncStatus_AuthenticationError: EmailMailboxSyncStatus = 3
EmailMailboxSyncStatus_PolicyError: EmailMailboxSyncStatus = 4
EmailMailboxSyncStatus_UnknownError: EmailMailboxSyncStatus = 5
EmailMailboxSyncStatus_ManualAccountRemovalRequired: EmailMailboxSyncStatus = 6
class EmailManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.EmailManager'
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.ApplicationModel.Email.IEmailManagerStatics3, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.Email.EmailManagerForUser: ...
    @winrt_classmethod
    def RequestStoreAsync(cls: win32more.Windows.ApplicationModel.Email.IEmailManagerStatics2, accessType: win32more.Windows.ApplicationModel.Email.EmailStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailStore]: ...
    @winrt_classmethod
    def ShowComposeNewEmailAsync(cls: win32more.Windows.ApplicationModel.Email.IEmailManagerStatics, message: win32more.Windows.ApplicationModel.Email.EmailMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
class EmailManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailManagerForUser
    _classid_ = 'Windows.ApplicationModel.Email.EmailManagerForUser'
    @winrt_mixinmethod
    def ShowComposeNewEmailAsync(self: win32more.Windows.ApplicationModel.Email.IEmailManagerForUser, message: win32more.Windows.ApplicationModel.Email.EmailMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RequestStoreAsync(self: win32more.Windows.ApplicationModel.Email.IEmailManagerForUser, accessType: win32more.Windows.ApplicationModel.Email.EmailStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailStore]: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Email.IEmailManagerForUser) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class EmailMeetingInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo
    _classid_ = 'Windows.ApplicationModel.Email.EmailMeetingInfo'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Email.EmailMeetingInfo.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Email.EmailMeetingInfo: ...
    @winrt_mixinmethod
    def get_AllowNewTimeProposal(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowNewTimeProposal(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AppointmentRoamingId(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AppointmentRoamingId(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AppointmentOriginalStartTime(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_AppointmentOriginalStartTime(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_IsAllDay(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAllDay(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsResponseRequested(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsResponseRequested(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Location(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ProposedStartTime(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_ProposedStartTime(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, proposedStartTime: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ProposedDuration(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_ProposedDuration(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, duration: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_RecurrenceStartTime(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_RecurrenceStartTime(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Recurrence(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> win32more.Windows.ApplicationModel.Appointments.AppointmentRecurrence: ...
    @winrt_mixinmethod
    def put_Recurrence(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, value: win32more.Windows.ApplicationModel.Appointments.AppointmentRecurrence) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteChangeNumber(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> UInt64: ...
    @winrt_mixinmethod
    def put_RemoteChangeNumber(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_StartTime(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_IsReportedOutOfDateByServer(self: win32more.Windows.ApplicationModel.Email.IEmailMeetingInfo2) -> Boolean: ...
    AllowNewTimeProposal = property(get_AllowNewTimeProposal, put_AllowNewTimeProposal)
    AppointmentRoamingId = property(get_AppointmentRoamingId, put_AppointmentRoamingId)
    AppointmentOriginalStartTime = property(get_AppointmentOriginalStartTime, put_AppointmentOriginalStartTime)
    Duration = property(get_Duration, put_Duration)
    IsAllDay = property(get_IsAllDay, put_IsAllDay)
    IsResponseRequested = property(get_IsResponseRequested, put_IsResponseRequested)
    Location = property(get_Location, put_Location)
    ProposedStartTime = property(get_ProposedStartTime, put_ProposedStartTime)
    ProposedDuration = property(get_ProposedDuration, put_ProposedDuration)
    RecurrenceStartTime = property(get_RecurrenceStartTime, put_RecurrenceStartTime)
    Recurrence = property(get_Recurrence, put_Recurrence)
    RemoteChangeNumber = property(get_RemoteChangeNumber, put_RemoteChangeNumber)
    StartTime = property(get_StartTime, put_StartTime)
    IsReportedOutOfDateByServer = property(get_IsReportedOutOfDateByServer, None)
EmailMeetingResponseType = Int32
EmailMeetingResponseType_Accept: EmailMeetingResponseType = 0
EmailMeetingResponseType_Decline: EmailMeetingResponseType = 1
EmailMeetingResponseType_Tentative: EmailMeetingResponseType = 2
class EmailMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMessage
    _classid_ = 'Windows.ApplicationModel.Email.EmailMessage'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Email.EmailMessage.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Email.EmailMessage: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.ApplicationModel.Email.IEmailMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subject(self: win32more.Windows.ApplicationModel.Email.IEmailMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Body(self: win32more.Windows.ApplicationModel.Email.IEmailMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Body(self: win32more.Windows.ApplicationModel.Email.IEmailMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Windows.ApplicationModel.Email.IEmailMessage) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Email.EmailRecipient]: ...
    @winrt_mixinmethod
    def get_CC(self: win32more.Windows.ApplicationModel.Email.IEmailMessage) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Email.EmailRecipient]: ...
    @winrt_mixinmethod
    def get_Bcc(self: win32more.Windows.ApplicationModel.Email.IEmailMessage) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Email.EmailRecipient]: ...
    @winrt_mixinmethod
    def get_Attachments(self: win32more.Windows.ApplicationModel.Email.IEmailMessage) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Email.EmailAttachment]: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_MailboxId(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConversationId(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FolderId(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AllowInternetImages(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowInternetImages(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ChangeNumber(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> UInt64: ...
    @winrt_mixinmethod
    def get_DownloadState(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> win32more.Windows.ApplicationModel.Email.EmailMessageDownloadState: ...
    @winrt_mixinmethod
    def put_DownloadState(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: win32more.Windows.ApplicationModel.Email.EmailMessageDownloadState) -> Void: ...
    @winrt_mixinmethod
    def get_EstimatedDownloadSizeInBytes(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> UInt32: ...
    @winrt_mixinmethod
    def put_EstimatedDownloadSizeInBytes(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_FlagState(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> win32more.Windows.ApplicationModel.Email.EmailFlagState: ...
    @winrt_mixinmethod
    def put_FlagState(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: win32more.Windows.ApplicationModel.Email.EmailFlagState) -> Void: ...
    @winrt_mixinmethod
    def get_HasPartialBodies(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Importance(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> win32more.Windows.ApplicationModel.Email.EmailImportance: ...
    @winrt_mixinmethod
    def put_Importance(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: win32more.Windows.ApplicationModel.Email.EmailImportance) -> Void: ...
    @winrt_mixinmethod
    def get_InResponseToMessageId(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IrmInfo(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> win32more.Windows.ApplicationModel.Email.EmailIrmInfo: ...
    @winrt_mixinmethod
    def put_IrmInfo(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: win32more.Windows.ApplicationModel.Email.EmailIrmInfo) -> Void: ...
    @winrt_mixinmethod
    def get_IsDraftMessage(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRead(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRead(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsSeen(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSeen(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsServerSearchMessage(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSmartSendable(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def get_MessageClass(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_MessageClass(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NormalizedSubject(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OriginalCodePage(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> Int32: ...
    @winrt_mixinmethod
    def put_OriginalCodePage(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Preview(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Preview(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_LastResponseKind(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> win32more.Windows.ApplicationModel.Email.EmailMessageResponseKind: ...
    @winrt_mixinmethod
    def put_LastResponseKind(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: win32more.Windows.ApplicationModel.Email.EmailMessageResponseKind) -> Void: ...
    @winrt_mixinmethod
    def get_Sender(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> win32more.Windows.ApplicationModel.Email.EmailRecipient: ...
    @winrt_mixinmethod
    def put_Sender(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: win32more.Windows.ApplicationModel.Email.EmailRecipient) -> Void: ...
    @winrt_mixinmethod
    def get_SentTime(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_SentTime(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_MeetingInfo(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2) -> win32more.Windows.ApplicationModel.Email.EmailMeetingInfo: ...
    @winrt_mixinmethod
    def put_MeetingInfo(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, value: win32more.Windows.ApplicationModel.Email.EmailMeetingInfo) -> Void: ...
    @winrt_mixinmethod
    def GetBodyStream(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, type: win32more.Windows.ApplicationModel.Email.EmailMessageBodyKind) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def SetBodyStream(self: win32more.Windows.ApplicationModel.Email.IEmailMessage2, type: win32more.Windows.ApplicationModel.Email.EmailMessageBodyKind, stream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_SmimeData(self: win32more.Windows.ApplicationModel.Email.IEmailMessage3) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_SmimeData(self: win32more.Windows.ApplicationModel.Email.IEmailMessage3, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_SmimeKind(self: win32more.Windows.ApplicationModel.Email.IEmailMessage3) -> win32more.Windows.ApplicationModel.Email.EmailMessageSmimeKind: ...
    @winrt_mixinmethod
    def put_SmimeKind(self: win32more.Windows.ApplicationModel.Email.IEmailMessage3, value: win32more.Windows.ApplicationModel.Email.EmailMessageSmimeKind) -> Void: ...
    @winrt_mixinmethod
    def get_ReplyTo(self: win32more.Windows.ApplicationModel.Email.IEmailMessage4) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Email.EmailRecipient]: ...
    @winrt_mixinmethod
    def get_SentRepresenting(self: win32more.Windows.ApplicationModel.Email.IEmailMessage4) -> win32more.Windows.ApplicationModel.Email.EmailRecipient: ...
    @winrt_mixinmethod
    def put_SentRepresenting(self: win32more.Windows.ApplicationModel.Email.IEmailMessage4, value: win32more.Windows.ApplicationModel.Email.EmailRecipient) -> Void: ...
    Subject = property(get_Subject, put_Subject)
    Body = property(get_Body, put_Body)
    To = property(get_To, None)
    CC = property(get_CC, None)
    Bcc = property(get_Bcc, None)
    Attachments = property(get_Attachments, None)
    Id = property(get_Id, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
    MailboxId = property(get_MailboxId, None)
    ConversationId = property(get_ConversationId, None)
    FolderId = property(get_FolderId, None)
    AllowInternetImages = property(get_AllowInternetImages, put_AllowInternetImages)
    ChangeNumber = property(get_ChangeNumber, None)
    DownloadState = property(get_DownloadState, put_DownloadState)
    EstimatedDownloadSizeInBytes = property(get_EstimatedDownloadSizeInBytes, put_EstimatedDownloadSizeInBytes)
    FlagState = property(get_FlagState, put_FlagState)
    HasPartialBodies = property(get_HasPartialBodies, None)
    Importance = property(get_Importance, put_Importance)
    InResponseToMessageId = property(get_InResponseToMessageId, None)
    IrmInfo = property(get_IrmInfo, put_IrmInfo)
    IsDraftMessage = property(get_IsDraftMessage, None)
    IsRead = property(get_IsRead, put_IsRead)
    IsSeen = property(get_IsSeen, put_IsSeen)
    IsServerSearchMessage = property(get_IsServerSearchMessage, None)
    IsSmartSendable = property(get_IsSmartSendable, None)
    MessageClass = property(get_MessageClass, put_MessageClass)
    NormalizedSubject = property(get_NormalizedSubject, None)
    OriginalCodePage = property(get_OriginalCodePage, put_OriginalCodePage)
    Preview = property(get_Preview, put_Preview)
    LastResponseKind = property(get_LastResponseKind, put_LastResponseKind)
    Sender = property(get_Sender, put_Sender)
    SentTime = property(get_SentTime, put_SentTime)
    MeetingInfo = property(get_MeetingInfo, put_MeetingInfo)
    SmimeData = property(get_SmimeData, put_SmimeData)
    SmimeKind = property(get_SmimeKind, put_SmimeKind)
    ReplyTo = property(get_ReplyTo, None)
    SentRepresenting = property(get_SentRepresenting, put_SentRepresenting)
class EmailMessageBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMessageBatch
    _classid_ = 'Windows.ApplicationModel.Email.EmailMessageBatch'
    @winrt_mixinmethod
    def get_Messages(self: win32more.Windows.ApplicationModel.Email.IEmailMessageBatch) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailMessage]: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Email.IEmailMessageBatch) -> win32more.Windows.ApplicationModel.Email.EmailBatchStatus: ...
    Messages = property(get_Messages, None)
    Status = property(get_Status, None)
EmailMessageBodyKind = Int32
EmailMessageBodyKind_Html: EmailMessageBodyKind = 0
EmailMessageBodyKind_PlainText: EmailMessageBodyKind = 1
EmailMessageDownloadState = Int32
EmailMessageDownloadState_PartiallyDownloaded: EmailMessageDownloadState = 0
EmailMessageDownloadState_Downloading: EmailMessageDownloadState = 1
EmailMessageDownloadState_Downloaded: EmailMessageDownloadState = 2
EmailMessageDownloadState_Failed: EmailMessageDownloadState = 3
class EmailMessageReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailMessageReader
    _classid_ = 'Windows.ApplicationModel.Email.EmailMessageReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: win32more.Windows.ApplicationModel.Email.IEmailMessageReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMessageBatch]: ...
EmailMessageResponseKind = Int32
EmailMessageResponseKind_None: EmailMessageResponseKind = 0
EmailMessageResponseKind_Reply: EmailMessageResponseKind = 1
EmailMessageResponseKind_ReplyAll: EmailMessageResponseKind = 2
EmailMessageResponseKind_Forward: EmailMessageResponseKind = 3
EmailMessageSmimeKind = Int32
EmailMessageSmimeKind_None: EmailMessageSmimeKind = 0
EmailMessageSmimeKind_ClearSigned: EmailMessageSmimeKind = 1
EmailMessageSmimeKind_OpaqueSigned: EmailMessageSmimeKind = 2
EmailMessageSmimeKind_Encrypted: EmailMessageSmimeKind = 3
EmailQueryKind = Int32
EmailQueryKind_All: EmailQueryKind = 0
EmailQueryKind_Important: EmailQueryKind = 1
EmailQueryKind_Flagged: EmailQueryKind = 2
EmailQueryKind_Unread: EmailQueryKind = 3
EmailQueryKind_Read: EmailQueryKind = 4
EmailQueryKind_Unseen: EmailQueryKind = 5
class EmailQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailQueryOptions
    _classid_ = 'Windows.ApplicationModel.Email.EmailQueryOptions'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Email.EmailQueryOptions.CreateInstance(*args)
        elif len(args) == 1:
            instance = win32more.Windows.ApplicationModel.Email.EmailQueryOptions.CreateWithText(*args)
        elif len(args) == 2:
            instance = win32more.Windows.ApplicationModel.Email.EmailQueryOptions.CreateWithTextAndFields(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Email.EmailQueryOptions: ...
    @winrt_factorymethod
    def CreateWithText(cls: win32more.Windows.ApplicationModel.Email.IEmailQueryOptionsFactory, text: WinRT_String) -> win32more.Windows.ApplicationModel.Email.EmailQueryOptions: ...
    @winrt_factorymethod
    def CreateWithTextAndFields(cls: win32more.Windows.ApplicationModel.Email.IEmailQueryOptionsFactory, text: WinRT_String, fields: win32more.Windows.ApplicationModel.Email.EmailQuerySearchFields) -> win32more.Windows.ApplicationModel.Email.EmailQueryOptions: ...
    @winrt_mixinmethod
    def get_TextSearch(self: win32more.Windows.ApplicationModel.Email.IEmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailQueryTextSearch: ...
    @winrt_mixinmethod
    def get_SortDirection(self: win32more.Windows.ApplicationModel.Email.IEmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailQuerySortDirection: ...
    @winrt_mixinmethod
    def put_SortDirection(self: win32more.Windows.ApplicationModel.Email.IEmailQueryOptions, value: win32more.Windows.ApplicationModel.Email.EmailQuerySortDirection) -> Void: ...
    @winrt_mixinmethod
    def get_SortProperty(self: win32more.Windows.ApplicationModel.Email.IEmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailQuerySortProperty: ...
    @winrt_mixinmethod
    def put_SortProperty(self: win32more.Windows.ApplicationModel.Email.IEmailQueryOptions, value: win32more.Windows.ApplicationModel.Email.EmailQuerySortProperty) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Email.IEmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailQueryKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Windows.ApplicationModel.Email.IEmailQueryOptions, value: win32more.Windows.ApplicationModel.Email.EmailQueryKind) -> Void: ...
    @winrt_mixinmethod
    def get_FolderIds(self: win32more.Windows.ApplicationModel.Email.IEmailQueryOptions) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    TextSearch = property(get_TextSearch, None)
    SortDirection = property(get_SortDirection, put_SortDirection)
    SortProperty = property(get_SortProperty, put_SortProperty)
    Kind = property(get_Kind, put_Kind)
    FolderIds = property(get_FolderIds, None)
EmailQuerySearchFields = UInt32
EmailQuerySearchFields_None: EmailQuerySearchFields = 0
EmailQuerySearchFields_Subject: EmailQuerySearchFields = 1
EmailQuerySearchFields_Sender: EmailQuerySearchFields = 2
EmailQuerySearchFields_Preview: EmailQuerySearchFields = 4
EmailQuerySearchFields_Recipients: EmailQuerySearchFields = 8
EmailQuerySearchFields_All: EmailQuerySearchFields = 4294967295
EmailQuerySearchScope = Int32
EmailQuerySearchScope_Local: EmailQuerySearchScope = 0
EmailQuerySearchScope_Server: EmailQuerySearchScope = 1
EmailQuerySortDirection = Int32
EmailQuerySortDirection_Descending: EmailQuerySortDirection = 0
EmailQuerySortDirection_Ascending: EmailQuerySortDirection = 1
EmailQuerySortProperty = Int32
EmailQuerySortProperty_Date: EmailQuerySortProperty = 0
class EmailQueryTextSearch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailQueryTextSearch
    _classid_ = 'Windows.ApplicationModel.Email.EmailQueryTextSearch'
    @winrt_mixinmethod
    def get_Fields(self: win32more.Windows.ApplicationModel.Email.IEmailQueryTextSearch) -> win32more.Windows.ApplicationModel.Email.EmailQuerySearchFields: ...
    @winrt_mixinmethod
    def put_Fields(self: win32more.Windows.ApplicationModel.Email.IEmailQueryTextSearch, value: win32more.Windows.ApplicationModel.Email.EmailQuerySearchFields) -> Void: ...
    @winrt_mixinmethod
    def get_SearchScope(self: win32more.Windows.ApplicationModel.Email.IEmailQueryTextSearch) -> win32more.Windows.ApplicationModel.Email.EmailQuerySearchScope: ...
    @winrt_mixinmethod
    def put_SearchScope(self: win32more.Windows.ApplicationModel.Email.IEmailQueryTextSearch, value: win32more.Windows.ApplicationModel.Email.EmailQuerySearchScope) -> Void: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.ApplicationModel.Email.IEmailQueryTextSearch) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.ApplicationModel.Email.IEmailQueryTextSearch, value: WinRT_String) -> Void: ...
    Fields = property(get_Fields, put_Fields)
    SearchScope = property(get_SearchScope, put_SearchScope)
    Text = property(get_Text, put_Text)
class EmailRecipient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailRecipient
    _classid_ = 'Windows.ApplicationModel.Email.EmailRecipient'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Email.EmailRecipient.CreateInstance(*args)
        elif len(args) == 1:
            instance = win32more.Windows.ApplicationModel.Email.EmailRecipient.Create(*args)
        elif len(args) == 2:
            instance = win32more.Windows.ApplicationModel.Email.EmailRecipient.CreateWithName(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Email.EmailRecipient: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Email.IEmailRecipientFactory, address: WinRT_String) -> win32more.Windows.ApplicationModel.Email.EmailRecipient: ...
    @winrt_factorymethod
    def CreateWithName(cls: win32more.Windows.ApplicationModel.Email.IEmailRecipientFactory, address: WinRT_String, name: WinRT_String) -> win32more.Windows.ApplicationModel.Email.EmailRecipient: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Email.IEmailRecipient) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.ApplicationModel.Email.IEmailRecipient, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Address(self: win32more.Windows.ApplicationModel.Email.IEmailRecipient) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Address(self: win32more.Windows.ApplicationModel.Email.IEmailRecipient, value: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)
    Address = property(get_Address, put_Address)
class EmailRecipientResolutionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailRecipientResolutionResult
    _classid_ = 'Windows.ApplicationModel.Email.EmailRecipientResolutionResult'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Email.EmailRecipientResolutionResult.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Email.EmailRecipientResolutionResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Email.IEmailRecipientResolutionResult) -> win32more.Windows.ApplicationModel.Email.EmailRecipientResolutionStatus: ...
    @winrt_mixinmethod
    def get_PublicKeys(self: win32more.Windows.ApplicationModel.Email.IEmailRecipientResolutionResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Windows.ApplicationModel.Email.IEmailRecipientResolutionResult2, value: win32more.Windows.ApplicationModel.Email.EmailRecipientResolutionStatus) -> Void: ...
    @winrt_mixinmethod
    def SetPublicKeys(self: win32more.Windows.ApplicationModel.Email.IEmailRecipientResolutionResult2, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.Certificate]) -> Void: ...
    Status = property(get_Status, put_Status)
    PublicKeys = property(get_PublicKeys, None)
EmailRecipientResolutionStatus = Int32
EmailRecipientResolutionStatus_Success: EmailRecipientResolutionStatus = 0
EmailRecipientResolutionStatus_RecipientNotFound: EmailRecipientResolutionStatus = 1
EmailRecipientResolutionStatus_AmbiguousRecipient: EmailRecipientResolutionStatus = 2
EmailRecipientResolutionStatus_NoCertificate: EmailRecipientResolutionStatus = 3
EmailRecipientResolutionStatus_CertificateRequestLimitReached: EmailRecipientResolutionStatus = 4
EmailRecipientResolutionStatus_CannotResolveDistributionList: EmailRecipientResolutionStatus = 5
EmailRecipientResolutionStatus_ServerError: EmailRecipientResolutionStatus = 6
EmailRecipientResolutionStatus_UnknownFailure: EmailRecipientResolutionStatus = 7
EmailSpecialFolderKind = Int32
EmailSpecialFolderKind_None: EmailSpecialFolderKind = 0
EmailSpecialFolderKind_Root: EmailSpecialFolderKind = 1
EmailSpecialFolderKind_Inbox: EmailSpecialFolderKind = 2
EmailSpecialFolderKind_Outbox: EmailSpecialFolderKind = 3
EmailSpecialFolderKind_Drafts: EmailSpecialFolderKind = 4
EmailSpecialFolderKind_DeletedItems: EmailSpecialFolderKind = 5
EmailSpecialFolderKind_Sent: EmailSpecialFolderKind = 6
class EmailStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailStore
    _classid_ = 'Windows.ApplicationModel.Email.EmailStore'
    @winrt_mixinmethod
    def FindMailboxesAsync(self: win32more.Windows.ApplicationModel.Email.IEmailStore) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailMailbox]]: ...
    @winrt_mixinmethod
    def GetConversationReader(self: win32more.Windows.ApplicationModel.Email.IEmailStore) -> win32more.Windows.ApplicationModel.Email.EmailConversationReader: ...
    @winrt_mixinmethod
    def GetConversationReaderWithOptions(self: win32more.Windows.ApplicationModel.Email.IEmailStore, options: win32more.Windows.ApplicationModel.Email.EmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailConversationReader: ...
    @winrt_mixinmethod
    def GetMessageReader(self: win32more.Windows.ApplicationModel.Email.IEmailStore) -> win32more.Windows.ApplicationModel.Email.EmailMessageReader: ...
    @winrt_mixinmethod
    def GetMessageReaderWithOptions(self: win32more.Windows.ApplicationModel.Email.IEmailStore, options: win32more.Windows.ApplicationModel.Email.EmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailMessageReader: ...
    @winrt_mixinmethod
    def GetMailboxAsync(self: win32more.Windows.ApplicationModel.Email.IEmailStore, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailbox]: ...
    @winrt_mixinmethod
    def GetConversationAsync(self: win32more.Windows.ApplicationModel.Email.IEmailStore, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailConversation]: ...
    @winrt_mixinmethod
    def GetFolderAsync(self: win32more.Windows.ApplicationModel.Email.IEmailStore, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailFolder]: ...
    @winrt_mixinmethod
    def GetMessageAsync(self: win32more.Windows.ApplicationModel.Email.IEmailStore, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMessage]: ...
    @winrt_mixinmethod
    def CreateMailboxAsync(self: win32more.Windows.ApplicationModel.Email.IEmailStore, accountName: WinRT_String, accountAddress: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailbox]: ...
    @winrt_mixinmethod
    def CreateMailboxInAccountAsync(self: win32more.Windows.ApplicationModel.Email.IEmailStore, accountName: WinRT_String, accountAddress: WinRT_String, userDataAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailbox]: ...
EmailStoreAccessType = Int32
EmailStoreAccessType_AppMailboxesReadWrite: EmailStoreAccessType = 0
EmailStoreAccessType_AllMailboxesLimitedReadWrite: EmailStoreAccessType = 1
class EmailStoreNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.IEmailStoreNotificationTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Email.EmailStoreNotificationTriggerDetails'
class IEmailAttachment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailAttachment'
    _iid_ = Guid('{f353caf9-57c8-4adb-b992-60fceb584f54}')
    @winrt_commethod(6)
    def get_FileName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_FileName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Data(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(9)
    def put_Data(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    FileName = property(get_FileName, put_FileName)
    Data = property(get_Data, put_Data)
class IEmailAttachment2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailAttachment2'
    _iid_ = Guid('{225f1070-b0ff-4571-9d54-a706c48d55c6}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ContentId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_ContentId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_ContentLocation(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_ContentLocation(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_DownloadState(self) -> win32more.Windows.ApplicationModel.Email.EmailAttachmentDownloadState: ...
    @winrt_commethod(12)
    def put_DownloadState(self, value: win32more.Windows.ApplicationModel.Email.EmailAttachmentDownloadState) -> Void: ...
    @winrt_commethod(13)
    def get_EstimatedDownloadSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(14)
    def put_EstimatedDownloadSizeInBytes(self, value: UInt64) -> Void: ...
    @winrt_commethod(15)
    def get_IsFromBaseMessage(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_IsInline(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsInline(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_MimeType(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def put_MimeType(self, value: WinRT_String) -> Void: ...
    Id = property(get_Id, None)
    ContentId = property(get_ContentId, put_ContentId)
    ContentLocation = property(get_ContentLocation, put_ContentLocation)
    DownloadState = property(get_DownloadState, put_DownloadState)
    EstimatedDownloadSizeInBytes = property(get_EstimatedDownloadSizeInBytes, put_EstimatedDownloadSizeInBytes)
    IsFromBaseMessage = property(get_IsFromBaseMessage, None)
    IsInline = property(get_IsInline, put_IsInline)
    MimeType = property(get_MimeType, put_MimeType)
class IEmailAttachmentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailAttachmentFactory'
    _iid_ = Guid('{796eac46-ed56-4979-8708-abb8bc854b7d}')
    @winrt_commethod(6)
    def Create(self, fileName: WinRT_String, data: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.ApplicationModel.Email.EmailAttachment: ...
class IEmailAttachmentFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailAttachmentFactory2'
    _iid_ = Guid('{23259435-51f9-427d-adcd-241023c8cfb7}')
    @winrt_commethod(6)
    def Create(self, fileName: WinRT_String, data: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, mimeType: WinRT_String) -> win32more.Windows.ApplicationModel.Email.EmailAttachment: ...
class IEmailConversation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailConversation'
    _iid_ = Guid('{da18c248-a0bc-4349-902d-90f66389f51b}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MailboxId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_FlagState(self) -> win32more.Windows.ApplicationModel.Email.EmailFlagState: ...
    @winrt_commethod(9)
    def get_HasAttachment(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Importance(self) -> win32more.Windows.ApplicationModel.Email.EmailImportance: ...
    @winrt_commethod(11)
    def get_LastEmailResponseKind(self) -> win32more.Windows.ApplicationModel.Email.EmailMessageResponseKind: ...
    @winrt_commethod(12)
    def get_MessageCount(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_MostRecentMessageId(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_MostRecentMessageTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(15)
    def get_Preview(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_LatestSender(self) -> win32more.Windows.ApplicationModel.Email.EmailRecipient: ...
    @winrt_commethod(17)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_UnreadMessageCount(self) -> UInt32: ...
    @winrt_commethod(19)
    def FindMessagesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailMessage]]: ...
    @winrt_commethod(20)
    def FindMessagesWithCountAsync(self, count: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailMessage]]: ...
    Id = property(get_Id, None)
    MailboxId = property(get_MailboxId, None)
    FlagState = property(get_FlagState, None)
    HasAttachment = property(get_HasAttachment, None)
    Importance = property(get_Importance, None)
    LastEmailResponseKind = property(get_LastEmailResponseKind, None)
    MessageCount = property(get_MessageCount, None)
    MostRecentMessageId = property(get_MostRecentMessageId, None)
    MostRecentMessageTime = property(get_MostRecentMessageTime, None)
    Preview = property(get_Preview, None)
    LatestSender = property(get_LatestSender, None)
    Subject = property(get_Subject, None)
    UnreadMessageCount = property(get_UnreadMessageCount, None)
class IEmailConversationBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailConversationBatch'
    _iid_ = Guid('{b8c1ab81-01c5-432a-9df1-fe85d98a279a}')
    @winrt_commethod(6)
    def get_Conversations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailConversation]: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Email.EmailBatchStatus: ...
    Conversations = property(get_Conversations, None)
    Status = property(get_Status, None)
class IEmailConversationReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailConversationReader'
    _iid_ = Guid('{b4630f82-2875-44c8-9b8c-85beb3a3c653}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailConversationBatch]: ...
class IEmailFolder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailFolder'
    _iid_ = Guid('{a24f7771-996c-4864-b1ba-ed1240e57d11}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_MailboxId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ParentFolderId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_IsSyncEnabled(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_IsSyncEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_LastSuccessfulSyncTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(16)
    def put_LastSuccessfulSyncTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(17)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Email.EmailSpecialFolderKind: ...
    @winrt_commethod(18)
    def CreateFolderAsync(self, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailFolder]: ...
    @winrt_commethod(19)
    def DeleteAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def FindChildFoldersAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailFolder]]: ...
    @winrt_commethod(21)
    def GetConversationReader(self) -> win32more.Windows.ApplicationModel.Email.EmailConversationReader: ...
    @winrt_commethod(22)
    def GetConversationReaderWithOptions(self, options: win32more.Windows.ApplicationModel.Email.EmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailConversationReader: ...
    @winrt_commethod(23)
    def GetMessageAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMessage]: ...
    @winrt_commethod(24)
    def GetMessageReader(self) -> win32more.Windows.ApplicationModel.Email.EmailMessageReader: ...
    @winrt_commethod(25)
    def GetMessageReaderWithOptions(self, options: win32more.Windows.ApplicationModel.Email.EmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailMessageReader: ...
    @winrt_commethod(26)
    def GetMessageCountsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailItemCounts]: ...
    @winrt_commethod(27)
    def TryMoveAsync(self, newParentFolder: win32more.Windows.ApplicationModel.Email.EmailFolder) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(28)
    def TryMoveWithNewNameAsync(self, newParentFolder: win32more.Windows.ApplicationModel.Email.EmailFolder, newFolderName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(29)
    def TrySaveAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(30)
    def SaveMessageAsync(self, message: win32more.Windows.ApplicationModel.Email.EmailMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    Id = property(get_Id, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
    MailboxId = property(get_MailboxId, None)
    ParentFolderId = property(get_ParentFolderId, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    IsSyncEnabled = property(get_IsSyncEnabled, put_IsSyncEnabled)
    LastSuccessfulSyncTime = property(get_LastSuccessfulSyncTime, put_LastSuccessfulSyncTime)
    Kind = property(get_Kind, None)
class IEmailIrmInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailIrmInfo'
    _iid_ = Guid('{90f52193-b1a0-4ebd-a6b6-ddca55606e0e}')
    @winrt_commethod(6)
    def get_CanEdit(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CanEdit(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CanExtractData(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_CanExtractData(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_CanForward(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_CanForward(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_CanModifyRecipientsOnResponse(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_CanModifyRecipientsOnResponse(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_CanPrintData(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_CanPrintData(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_CanRemoveIrmOnResponse(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_CanRemoveIrmOnResponse(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_CanReply(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_CanReply(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_CanReplyAll(self) -> Boolean: ...
    @winrt_commethod(21)
    def put_CanReplyAll(self, value: Boolean) -> Void: ...
    @winrt_commethod(22)
    def get_ExpirationDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(23)
    def put_ExpirationDate(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(24)
    def get_IsIrmOriginator(self) -> Boolean: ...
    @winrt_commethod(25)
    def put_IsIrmOriginator(self, value: Boolean) -> Void: ...
    @winrt_commethod(26)
    def get_IsProgramaticAccessAllowed(self) -> Boolean: ...
    @winrt_commethod(27)
    def put_IsProgramaticAccessAllowed(self, value: Boolean) -> Void: ...
    @winrt_commethod(28)
    def get_Template(self) -> win32more.Windows.ApplicationModel.Email.EmailIrmTemplate: ...
    @winrt_commethod(29)
    def put_Template(self, value: win32more.Windows.ApplicationModel.Email.EmailIrmTemplate) -> Void: ...
    CanEdit = property(get_CanEdit, put_CanEdit)
    CanExtractData = property(get_CanExtractData, put_CanExtractData)
    CanForward = property(get_CanForward, put_CanForward)
    CanModifyRecipientsOnResponse = property(get_CanModifyRecipientsOnResponse, put_CanModifyRecipientsOnResponse)
    CanPrintData = property(get_CanPrintData, put_CanPrintData)
    CanRemoveIrmOnResponse = property(get_CanRemoveIrmOnResponse, put_CanRemoveIrmOnResponse)
    CanReply = property(get_CanReply, put_CanReply)
    CanReplyAll = property(get_CanReplyAll, put_CanReplyAll)
    ExpirationDate = property(get_ExpirationDate, put_ExpirationDate)
    IsIrmOriginator = property(get_IsIrmOriginator, put_IsIrmOriginator)
    IsProgramaticAccessAllowed = property(get_IsProgramaticAccessAllowed, put_IsProgramaticAccessAllowed)
    Template = property(get_Template, put_Template)
class IEmailIrmInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailIrmInfoFactory'
    _iid_ = Guid('{314bb18c-e3e6-4d7b-be8d-91a96311b01b}')
    @winrt_commethod(6)
    def Create(self, expiration: win32more.Windows.Foundation.DateTime, irmTemplate: win32more.Windows.ApplicationModel.Email.EmailIrmTemplate) -> win32more.Windows.ApplicationModel.Email.EmailIrmInfo: ...
class IEmailIrmTemplate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailIrmTemplate'
    _iid_ = Guid('{f327758d-546d-4bea-a963-54a38b2cc016}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Name(self, value: WinRT_String) -> Void: ...
    Id = property(get_Id, put_Id)
    Description = property(get_Description, put_Description)
    Name = property(get_Name, put_Name)
class IEmailIrmTemplateFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailIrmTemplateFactory'
    _iid_ = Guid('{3da31876-8738-4418-b9cb-471b936fe71e}')
    @winrt_commethod(6)
    def Create(self, id: WinRT_String, name: WinRT_String, description: WinRT_String) -> win32more.Windows.ApplicationModel.Email.EmailIrmTemplate: ...
class IEmailItemCounts(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailItemCounts'
    _iid_ = Guid('{5bd13321-fec8-4bab-83ba-0baf3c1f6cbd}')
    @winrt_commethod(6)
    def get_Flagged(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Important(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Total(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Unread(self) -> UInt32: ...
    Flagged = property(get_Flagged, None)
    Important = property(get_Important, None)
    Total = property(get_Total, None)
    Unread = property(get_Unread, None)
class IEmailMailbox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailbox'
    _iid_ = Guid('{a8790649-cf5b-411b-80b1-4a6a1484ce25}')
    @winrt_commethod(6)
    def get_Capabilities(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxCapabilities: ...
    @winrt_commethod(7)
    def get_ChangeTracker(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxChangeTracker: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_IsOwnedByCurrentApp(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsDataEncryptedUnderLock(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_MailAddress(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_MailAddress(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_MailAddressAliases(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(16)
    def get_OtherAppReadAccess(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxOtherAppReadAccess: ...
    @winrt_commethod(17)
    def put_OtherAppReadAccess(self, value: win32more.Windows.ApplicationModel.Email.EmailMailboxOtherAppReadAccess) -> Void: ...
    @winrt_commethod(18)
    def get_OtherAppWriteAccess(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxOtherAppWriteAccess: ...
    @winrt_commethod(19)
    def put_OtherAppWriteAccess(self, value: win32more.Windows.ApplicationModel.Email.EmailMailboxOtherAppWriteAccess) -> Void: ...
    @winrt_commethod(20)
    def get_Policies(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxPolicies: ...
    @winrt_commethod(21)
    def get_SourceDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_SyncManager(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxSyncManager: ...
    @winrt_commethod(23)
    def get_UserDataAccountId(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def GetConversationReader(self) -> win32more.Windows.ApplicationModel.Email.EmailConversationReader: ...
    @winrt_commethod(25)
    def GetConversationReaderWithOptions(self, options: win32more.Windows.ApplicationModel.Email.EmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailConversationReader: ...
    @winrt_commethod(26)
    def GetMessageReader(self) -> win32more.Windows.ApplicationModel.Email.EmailMessageReader: ...
    @winrt_commethod(27)
    def GetMessageReaderWithOptions(self, options: win32more.Windows.ApplicationModel.Email.EmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailMessageReader: ...
    @winrt_commethod(28)
    def DeleteAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(29)
    def GetConversationAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailConversation]: ...
    @winrt_commethod(30)
    def GetFolderAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailFolder]: ...
    @winrt_commethod(31)
    def GetMessageAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMessage]: ...
    @winrt_commethod(32)
    def GetSpecialFolderAsync(self, folderType: win32more.Windows.ApplicationModel.Email.EmailSpecialFolderKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailFolder]: ...
    @winrt_commethod(33)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(34)
    def MarkMessageAsSeenAsync(self, messageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(35)
    def MarkFolderAsSeenAsync(self, folderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(36)
    def MarkMessageReadAsync(self, messageId: WinRT_String, isRead: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(37)
    def ChangeMessageFlagStateAsync(self, messageId: WinRT_String, flagState: win32more.Windows.ApplicationModel.Email.EmailFlagState) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(38)
    def TryMoveMessageAsync(self, messageId: WinRT_String, newParentFolderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(39)
    def TryMoveFolderAsync(self, folderId: WinRT_String, newParentFolderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(40)
    def TryMoveFolderWithNewNameAsync(self, folderId: WinRT_String, newParentFolderId: WinRT_String, newFolderName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(41)
    def DeleteMessageAsync(self, messageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(42)
    def MarkFolderSyncEnabledAsync(self, folderId: WinRT_String, isSyncEnabled: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(43)
    def SendMessageAsync(self, message: win32more.Windows.ApplicationModel.Email.EmailMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(44)
    def SaveDraftAsync(self, message: win32more.Windows.ApplicationModel.Email.EmailMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(45)
    def DownloadMessageAsync(self, messageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(46)
    def DownloadAttachmentAsync(self, attachmentId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(47)
    def CreateResponseMessageAsync(self, messageId: WinRT_String, responseType: win32more.Windows.ApplicationModel.Email.EmailMessageResponseKind, subject: WinRT_String, responseHeaderType: win32more.Windows.ApplicationModel.Email.EmailMessageBodyKind, responseHeader: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMessage]: ...
    @winrt_commethod(48)
    def TryUpdateMeetingResponseAsync(self, meeting: win32more.Windows.ApplicationModel.Email.EmailMessage, response: win32more.Windows.ApplicationModel.Email.EmailMeetingResponseType, subject: WinRT_String, comment: WinRT_String, sendUpdate: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(49)
    def TryForwardMeetingAsync(self, meeting: win32more.Windows.ApplicationModel.Email.EmailMessage, recipients: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Email.EmailRecipient], subject: WinRT_String, forwardHeaderType: win32more.Windows.ApplicationModel.Email.EmailMessageBodyKind, forwardHeader: WinRT_String, comment: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(50)
    def TryProposeNewTimeForMeetingAsync(self, meeting: win32more.Windows.ApplicationModel.Email.EmailMessage, newStartTime: win32more.Windows.Foundation.DateTime, newDuration: win32more.Windows.Foundation.TimeSpan, subject: WinRT_String, comment: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(51)
    def add_MailboxChanged(self, pHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.EmailMailbox, win32more.Windows.ApplicationModel.Email.EmailMailboxChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(52)
    def remove_MailboxChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(53)
    def SmartSendMessageAsync(self, message: win32more.Windows.ApplicationModel.Email.EmailMessage, smartSend: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(54)
    def TrySetAutoReplySettingsAsync(self, autoReplySettings: win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(55)
    def TryGetAutoReplySettingsAsync(self, requestedFormat: win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings]: ...
    Capabilities = property(get_Capabilities, None)
    ChangeTracker = property(get_ChangeTracker, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Id = property(get_Id, None)
    IsOwnedByCurrentApp = property(get_IsOwnedByCurrentApp, None)
    IsDataEncryptedUnderLock = property(get_IsDataEncryptedUnderLock, None)
    MailAddress = property(get_MailAddress, put_MailAddress)
    MailAddressAliases = property(get_MailAddressAliases, None)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    OtherAppWriteAccess = property(get_OtherAppWriteAccess, put_OtherAppWriteAccess)
    Policies = property(get_Policies, None)
    SourceDisplayName = property(get_SourceDisplayName, None)
    SyncManager = property(get_SyncManager, None)
    UserDataAccountId = property(get_UserDataAccountId, None)
class IEmailMailbox2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailbox2'
    _iid_ = Guid('{14f8e404-6ca2-4ab2-9241-79cd7bf46346}')
    @winrt_commethod(6)
    def get_LinkedMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_NetworkId(self) -> WinRT_String: ...
    LinkedMailboxId = property(get_LinkedMailboxId, None)
    NetworkAccountId = property(get_NetworkAccountId, None)
    NetworkId = property(get_NetworkId, None)
class IEmailMailbox3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailbox3'
    _iid_ = Guid('{3da5897b-458b-408a-8e37-ac8b05d8af56}')
    @winrt_commethod(6)
    def ResolveRecipientsAsync(self, recipients: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailRecipientResolutionResult]]: ...
    @winrt_commethod(7)
    def ValidateCertificatesAsync(self, certificates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.Certificate]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailCertificateValidationStatus]]: ...
    @winrt_commethod(8)
    def TryEmptyFolderAsync(self, folderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailboxEmptyFolderStatus]: ...
    @winrt_commethod(9)
    def TryCreateFolderAsync(self, parentFolderId: WinRT_String, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailboxCreateFolderResult]: ...
    @winrt_commethod(10)
    def TryDeleteFolderAsync(self, folderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailboxDeleteFolderStatus]: ...
class IEmailMailbox4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailbox4'
    _iid_ = Guid('{5d1f301b-f222-48a7-b7b6-716356cd26a1}')
    @winrt_commethod(6)
    def RegisterSyncManagerAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IEmailMailbox5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailbox5'
    _iid_ = Guid('{39967087-0092-49be-bd0e-5d4dc9d96d90}')
    @winrt_commethod(6)
    def GetChangeTracker(self, identity: WinRT_String) -> win32more.Windows.ApplicationModel.Email.EmailMailboxChangeTracker: ...
class IEmailMailboxAction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxAction'
    _iid_ = Guid('{ac9889fa-21fa-4927-9210-d410582fdf3e}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxActionKind: ...
    @winrt_commethod(7)
    def get_ChangeNumber(self) -> UInt64: ...
    Kind = property(get_Kind, None)
    ChangeNumber = property(get_ChangeNumber, None)
class IEmailMailboxAutoReply(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxAutoReply'
    _iid_ = Guid('{e223254c-8ab4-485b-b31f-04d15476bd59}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Response(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Response(self, value: WinRT_String) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Response = property(get_Response, put_Response)
class IEmailMailboxAutoReplySettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxAutoReplySettings'
    _iid_ = Guid('{a87a9fa8-0ac6-4b77-ba77-a6b99e9a27b8}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_ResponseKind(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind: ...
    @winrt_commethod(9)
    def put_ResponseKind(self, value: win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind) -> Void: ...
    @winrt_commethod(10)
    def get_StartTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def put_StartTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(12)
    def get_EndTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(13)
    def put_EndTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(14)
    def get_InternalReply(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReply: ...
    @winrt_commethod(15)
    def get_KnownExternalReply(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReply: ...
    @winrt_commethod(16)
    def get_UnknownExternalReply(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReply: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    ResponseKind = property(get_ResponseKind, put_ResponseKind)
    StartTime = property(get_StartTime, put_StartTime)
    EndTime = property(get_EndTime, put_EndTime)
    InternalReply = property(get_InternalReply, None)
    KnownExternalReply = property(get_KnownExternalReply, None)
    UnknownExternalReply = property(get_UnknownExternalReply, None)
class IEmailMailboxCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxCapabilities'
    _iid_ = Guid('{eedec3a6-89db-4305-82c4-439e0a33da11}')
    @winrt_commethod(6)
    def get_CanForwardMeetings(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CanGetAndSetExternalAutoReplies(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_CanGetAndSetInternalAutoReplies(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_CanUpdateMeetingResponses(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_CanServerSearchFolders(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_CanServerSearchMailbox(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_CanProposeNewTimeForMeetings(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_CanSmartSend(self) -> Boolean: ...
    CanForwardMeetings = property(get_CanForwardMeetings, None)
    CanGetAndSetExternalAutoReplies = property(get_CanGetAndSetExternalAutoReplies, None)
    CanGetAndSetInternalAutoReplies = property(get_CanGetAndSetInternalAutoReplies, None)
    CanUpdateMeetingResponses = property(get_CanUpdateMeetingResponses, None)
    CanServerSearchFolders = property(get_CanServerSearchFolders, None)
    CanServerSearchMailbox = property(get_CanServerSearchMailbox, None)
    CanProposeNewTimeForMeetings = property(get_CanProposeNewTimeForMeetings, None)
    CanSmartSend = property(get_CanSmartSend, None)
class IEmailMailboxCapabilities2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxCapabilities2'
    _iid_ = Guid('{69723ee4-2f21-4cbc-88ab-2e7602a4806b}')
    @winrt_commethod(6)
    def get_CanResolveRecipients(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CanValidateCertificates(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_CanEmptyFolder(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_CanCreateFolder(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_CanDeleteFolder(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_CanMoveFolder(self) -> Boolean: ...
    CanResolveRecipients = property(get_CanResolveRecipients, None)
    CanValidateCertificates = property(get_CanValidateCertificates, None)
    CanEmptyFolder = property(get_CanEmptyFolder, None)
    CanCreateFolder = property(get_CanCreateFolder, None)
    CanDeleteFolder = property(get_CanDeleteFolder, None)
    CanMoveFolder = property(get_CanMoveFolder, None)
class IEmailMailboxCapabilities3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxCapabilities3'
    _iid_ = Guid('{f690e944-56f2-45aa-872c-0ce9f3db0b5c}')
    @winrt_commethod(6)
    def put_CanForwardMeetings(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def put_CanGetAndSetExternalAutoReplies(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def put_CanGetAndSetInternalAutoReplies(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def put_CanUpdateMeetingResponses(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def put_CanServerSearchFolders(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def put_CanServerSearchMailbox(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def put_CanProposeNewTimeForMeetings(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def put_CanSmartSend(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def put_CanResolveRecipients(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def put_CanValidateCertificates(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def put_CanEmptyFolder(self, value: Boolean) -> Void: ...
    @winrt_commethod(17)
    def put_CanCreateFolder(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def put_CanDeleteFolder(self, value: Boolean) -> Void: ...
    @winrt_commethod(19)
    def put_CanMoveFolder(self, value: Boolean) -> Void: ...
    CanForwardMeetings = property(None, put_CanForwardMeetings)
    CanGetAndSetExternalAutoReplies = property(None, put_CanGetAndSetExternalAutoReplies)
    CanGetAndSetInternalAutoReplies = property(None, put_CanGetAndSetInternalAutoReplies)
    CanUpdateMeetingResponses = property(None, put_CanUpdateMeetingResponses)
    CanServerSearchFolders = property(None, put_CanServerSearchFolders)
    CanServerSearchMailbox = property(None, put_CanServerSearchMailbox)
    CanProposeNewTimeForMeetings = property(None, put_CanProposeNewTimeForMeetings)
    CanSmartSend = property(None, put_CanSmartSend)
    CanResolveRecipients = property(None, put_CanResolveRecipients)
    CanValidateCertificates = property(None, put_CanValidateCertificates)
    CanEmptyFolder = property(None, put_CanEmptyFolder)
    CanCreateFolder = property(None, put_CanCreateFolder)
    CanDeleteFolder = property(None, put_CanDeleteFolder)
    CanMoveFolder = property(None, put_CanMoveFolder)
class IEmailMailboxChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxChange'
    _iid_ = Guid('{61edf54b-11ef-400c-adde-8cde65c85e66}')
    @winrt_commethod(6)
    def get_ChangeType(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxChangeType: ...
    @winrt_commethod(7)
    def get_MailboxActions(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Email.EmailMailboxAction]: ...
    @winrt_commethod(8)
    def get_Message(self) -> win32more.Windows.ApplicationModel.Email.EmailMessage: ...
    @winrt_commethod(9)
    def get_Folder(self) -> win32more.Windows.ApplicationModel.Email.EmailFolder: ...
    ChangeType = property(get_ChangeType, None)
    MailboxActions = property(get_MailboxActions, None)
    Message = property(get_Message, None)
    Folder = property(get_Folder, None)
class IEmailMailboxChangeReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxChangeReader'
    _iid_ = Guid('{bdbd0ebb-c53d-4331-97be-be75a2146a75}')
    @winrt_commethod(6)
    def AcceptChanges(self) -> Void: ...
    @winrt_commethod(7)
    def AcceptChangesThrough(self, lastChangeToAcknowledge: win32more.Windows.ApplicationModel.Email.EmailMailboxChange) -> Void: ...
    @winrt_commethod(8)
    def ReadBatchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailMailboxChange]]: ...
class IEmailMailboxChangeTracker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxChangeTracker'
    _iid_ = Guid('{7ae48638-5166-42b7-8882-fd21c92bdd4b}')
    @winrt_commethod(6)
    def get_IsTracking(self) -> Boolean: ...
    @winrt_commethod(7)
    def Enable(self) -> Void: ...
    @winrt_commethod(8)
    def GetChangeReader(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxChangeReader: ...
    @winrt_commethod(9)
    def Reset(self) -> Void: ...
    IsTracking = property(get_IsTracking, None)
class IEmailMailboxChangedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxChangedDeferral'
    _iid_ = Guid('{779a74c1-97c5-4b54-b30d-306232623e6d}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IEmailMailboxChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxChangedEventArgs'
    _iid_ = Guid('{3cfd5f6e-01d4-4e4a-a44c-b22dd42ec207}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxChangedDeferral: ...
class IEmailMailboxCreateFolderResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxCreateFolderResult'
    _iid_ = Guid('{b228557f-2885-4998-b595-8a2d374ce950}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxCreateFolderStatus: ...
    @winrt_commethod(7)
    def get_Folder(self) -> win32more.Windows.ApplicationModel.Email.EmailFolder: ...
    Status = property(get_Status, None)
    Folder = property(get_Folder, None)
class IEmailMailboxPolicies(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxPolicies'
    _iid_ = Guid('{1f3345c5-1c3b-4dc7-b410-6373783e545d}')
    @winrt_commethod(6)
    def get_AllowedSmimeEncryptionAlgorithmNegotiation(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation: ...
    @winrt_commethod(7)
    def get_AllowSmimeSoftCertificates(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_RequiredSmimeEncryptionAlgorithm(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.Email.EmailMailboxSmimeEncryptionAlgorithm]: ...
    @winrt_commethod(9)
    def get_RequiredSmimeSigningAlgorithm(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.Email.EmailMailboxSmimeSigningAlgorithm]: ...
    AllowedSmimeEncryptionAlgorithmNegotiation = property(get_AllowedSmimeEncryptionAlgorithmNegotiation, None)
    AllowSmimeSoftCertificates = property(get_AllowSmimeSoftCertificates, None)
    RequiredSmimeEncryptionAlgorithm = property(get_RequiredSmimeEncryptionAlgorithm, None)
    RequiredSmimeSigningAlgorithm = property(get_RequiredSmimeSigningAlgorithm, None)
class IEmailMailboxPolicies2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxPolicies2'
    _iid_ = Guid('{bab58afb-a14b-497c-a8e2-55eac29cc4b5}')
    @winrt_commethod(6)
    def get_MustEncryptSmimeMessages(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_MustSignSmimeMessages(self) -> Boolean: ...
    MustEncryptSmimeMessages = property(get_MustEncryptSmimeMessages, None)
    MustSignSmimeMessages = property(get_MustSignSmimeMessages, None)
class IEmailMailboxPolicies3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxPolicies3'
    _iid_ = Guid('{bdd4a01f-4867-414a-81a2-803919c44191}')
    @winrt_commethod(6)
    def put_AllowedSmimeEncryptionAlgorithmNegotiation(self, value: win32more.Windows.ApplicationModel.Email.EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation) -> Void: ...
    @winrt_commethod(7)
    def put_AllowSmimeSoftCertificates(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def put_RequiredSmimeEncryptionAlgorithm(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.Email.EmailMailboxSmimeEncryptionAlgorithm]) -> Void: ...
    @winrt_commethod(9)
    def put_RequiredSmimeSigningAlgorithm(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.Email.EmailMailboxSmimeSigningAlgorithm]) -> Void: ...
    @winrt_commethod(10)
    def put_MustEncryptSmimeMessages(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def put_MustSignSmimeMessages(self, value: Boolean) -> Void: ...
    AllowedSmimeEncryptionAlgorithmNegotiation = property(None, put_AllowedSmimeEncryptionAlgorithmNegotiation)
    AllowSmimeSoftCertificates = property(None, put_AllowSmimeSoftCertificates)
    RequiredSmimeEncryptionAlgorithm = property(None, put_RequiredSmimeEncryptionAlgorithm)
    RequiredSmimeSigningAlgorithm = property(None, put_RequiredSmimeSigningAlgorithm)
    MustEncryptSmimeMessages = property(None, put_MustEncryptSmimeMessages)
    MustSignSmimeMessages = property(None, put_MustSignSmimeMessages)
class IEmailMailboxSyncManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxSyncManager'
    _iid_ = Guid('{517ac55a-3591-4b5d-85bc-c71dde862263}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxSyncStatus: ...
    @winrt_commethod(7)
    def get_LastSuccessfulSyncTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_LastAttemptedSyncTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def SyncAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def add_SyncStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.EmailMailboxSyncManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SyncStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
    LastSuccessfulSyncTime = property(get_LastSuccessfulSyncTime, None)
    LastAttemptedSyncTime = property(get_LastAttemptedSyncTime, None)
class IEmailMailboxSyncManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMailboxSyncManager2'
    _iid_ = Guid('{cd8dc97e-95c1-4f89-81b7-e6aecb6695fc}')
    @winrt_commethod(6)
    def put_Status(self, value: win32more.Windows.ApplicationModel.Email.EmailMailboxSyncStatus) -> Void: ...
    @winrt_commethod(7)
    def put_LastSuccessfulSyncTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(8)
    def put_LastAttemptedSyncTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    Status = property(None, put_Status)
    LastSuccessfulSyncTime = property(None, put_LastSuccessfulSyncTime)
    LastAttemptedSyncTime = property(None, put_LastAttemptedSyncTime)
class IEmailManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailManagerForUser'
    _iid_ = Guid('{f773de9f-3ca5-4b0f-90c1-156e40174ce5}')
    @winrt_commethod(6)
    def ShowComposeNewEmailAsync(self, message: win32more.Windows.ApplicationModel.Email.EmailMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def RequestStoreAsync(self, accessType: win32more.Windows.ApplicationModel.Email.EmailStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailStore]: ...
    @winrt_commethod(8)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IEmailManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailManagerStatics'
    _iid_ = Guid('{f5128654-55c5-4890-a824-216c2618ce7f}')
    @winrt_commethod(6)
    def ShowComposeNewEmailAsync(self, message: win32more.Windows.ApplicationModel.Email.EmailMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
class IEmailManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailManagerStatics2'
    _iid_ = Guid('{ac052da3-b194-425d-b6d9-d0f04135eda2}')
    @winrt_commethod(6)
    def RequestStoreAsync(self, accessType: win32more.Windows.ApplicationModel.Email.EmailStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailStore]: ...
class IEmailManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailManagerStatics3'
    _iid_ = Guid('{4a722395-843e-4945-b3aa-349e07a362c5}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.Email.EmailManagerForUser: ...
class IEmailMeetingInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMeetingInfo'
    _iid_ = Guid('{31c03fa9-7933-415f-a275-d165ba07026b}')
    @winrt_commethod(6)
    def get_AllowNewTimeProposal(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowNewTimeProposal(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_AppointmentRoamingId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_AppointmentRoamingId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_AppointmentOriginalStartTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def put_AppointmentOriginalStartTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(12)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def put_Duration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(14)
    def get_IsAllDay(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsAllDay(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_IsResponseRequested(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsResponseRequested(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_Location(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def put_Location(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(20)
    def get_ProposedStartTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(21)
    def put_ProposedStartTime(self, proposedStartTime: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(22)
    def get_ProposedDuration(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(23)
    def put_ProposedDuration(self, duration: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(24)
    def get_RecurrenceStartTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(25)
    def put_RecurrenceStartTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(26)
    def get_Recurrence(self) -> win32more.Windows.ApplicationModel.Appointments.AppointmentRecurrence: ...
    @winrt_commethod(27)
    def put_Recurrence(self, value: win32more.Windows.ApplicationModel.Appointments.AppointmentRecurrence) -> Void: ...
    @winrt_commethod(28)
    def get_RemoteChangeNumber(self) -> UInt64: ...
    @winrt_commethod(29)
    def put_RemoteChangeNumber(self, value: UInt64) -> Void: ...
    @winrt_commethod(30)
    def get_StartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(31)
    def put_StartTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    AllowNewTimeProposal = property(get_AllowNewTimeProposal, put_AllowNewTimeProposal)
    AppointmentRoamingId = property(get_AppointmentRoamingId, put_AppointmentRoamingId)
    AppointmentOriginalStartTime = property(get_AppointmentOriginalStartTime, put_AppointmentOriginalStartTime)
    Duration = property(get_Duration, put_Duration)
    IsAllDay = property(get_IsAllDay, put_IsAllDay)
    IsResponseRequested = property(get_IsResponseRequested, put_IsResponseRequested)
    Location = property(get_Location, put_Location)
    ProposedStartTime = property(get_ProposedStartTime, put_ProposedStartTime)
    ProposedDuration = property(get_ProposedDuration, put_ProposedDuration)
    RecurrenceStartTime = property(get_RecurrenceStartTime, put_RecurrenceStartTime)
    Recurrence = property(get_Recurrence, put_Recurrence)
    RemoteChangeNumber = property(get_RemoteChangeNumber, put_RemoteChangeNumber)
    StartTime = property(get_StartTime, put_StartTime)
class IEmailMeetingInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMeetingInfo2'
    _iid_ = Guid('{7e59386d-b0d9-4fe5-867c-e31ed2b588b8}')
    @winrt_commethod(6)
    def get_IsReportedOutOfDateByServer(self) -> Boolean: ...
    IsReportedOutOfDateByServer = property(get_IsReportedOutOfDateByServer, None)
class IEmailMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMessage'
    _iid_ = Guid('{6c6d948d-80b5-48f8-b0b1-e04e430f44e5}')
    @winrt_commethod(6)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Subject(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Body(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_To(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Email.EmailRecipient]: ...
    @winrt_commethod(11)
    def get_CC(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Email.EmailRecipient]: ...
    @winrt_commethod(12)
    def get_Bcc(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Email.EmailRecipient]: ...
    @winrt_commethod(13)
    def get_Attachments(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Email.EmailAttachment]: ...
    Subject = property(get_Subject, put_Subject)
    Body = property(get_Body, put_Body)
    To = property(get_To, None)
    CC = property(get_CC, None)
    Bcc = property(get_Bcc, None)
    Attachments = property(get_Attachments, None)
class IEmailMessage2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMessage2'
    _iid_ = Guid('{fdc8248b-9f1a-44db-bd3c-65c384770f86}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_MailboxId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ConversationId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_FolderId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_AllowInternetImages(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_AllowInternetImages(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_ChangeNumber(self) -> UInt64: ...
    @winrt_commethod(15)
    def get_DownloadState(self) -> win32more.Windows.ApplicationModel.Email.EmailMessageDownloadState: ...
    @winrt_commethod(16)
    def put_DownloadState(self, value: win32more.Windows.ApplicationModel.Email.EmailMessageDownloadState) -> Void: ...
    @winrt_commethod(17)
    def get_EstimatedDownloadSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(18)
    def put_EstimatedDownloadSizeInBytes(self, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def get_FlagState(self) -> win32more.Windows.ApplicationModel.Email.EmailFlagState: ...
    @winrt_commethod(20)
    def put_FlagState(self, value: win32more.Windows.ApplicationModel.Email.EmailFlagState) -> Void: ...
    @winrt_commethod(21)
    def get_HasPartialBodies(self) -> Boolean: ...
    @winrt_commethod(22)
    def get_Importance(self) -> win32more.Windows.ApplicationModel.Email.EmailImportance: ...
    @winrt_commethod(23)
    def put_Importance(self, value: win32more.Windows.ApplicationModel.Email.EmailImportance) -> Void: ...
    @winrt_commethod(24)
    def get_InResponseToMessageId(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def get_IrmInfo(self) -> win32more.Windows.ApplicationModel.Email.EmailIrmInfo: ...
    @winrt_commethod(26)
    def put_IrmInfo(self, value: win32more.Windows.ApplicationModel.Email.EmailIrmInfo) -> Void: ...
    @winrt_commethod(27)
    def get_IsDraftMessage(self) -> Boolean: ...
    @winrt_commethod(28)
    def get_IsRead(self) -> Boolean: ...
    @winrt_commethod(29)
    def put_IsRead(self, value: Boolean) -> Void: ...
    @winrt_commethod(30)
    def get_IsSeen(self) -> Boolean: ...
    @winrt_commethod(31)
    def put_IsSeen(self, value: Boolean) -> Void: ...
    @winrt_commethod(32)
    def get_IsServerSearchMessage(self) -> Boolean: ...
    @winrt_commethod(33)
    def get_IsSmartSendable(self) -> Boolean: ...
    @winrt_commethod(34)
    def get_MessageClass(self) -> WinRT_String: ...
    @winrt_commethod(35)
    def put_MessageClass(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(36)
    def get_NormalizedSubject(self) -> WinRT_String: ...
    @winrt_commethod(37)
    def get_OriginalCodePage(self) -> Int32: ...
    @winrt_commethod(38)
    def put_OriginalCodePage(self, value: Int32) -> Void: ...
    @winrt_commethod(39)
    def get_Preview(self) -> WinRT_String: ...
    @winrt_commethod(40)
    def put_Preview(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(41)
    def get_LastResponseKind(self) -> win32more.Windows.ApplicationModel.Email.EmailMessageResponseKind: ...
    @winrt_commethod(42)
    def put_LastResponseKind(self, value: win32more.Windows.ApplicationModel.Email.EmailMessageResponseKind) -> Void: ...
    @winrt_commethod(43)
    def get_Sender(self) -> win32more.Windows.ApplicationModel.Email.EmailRecipient: ...
    @winrt_commethod(44)
    def put_Sender(self, value: win32more.Windows.ApplicationModel.Email.EmailRecipient) -> Void: ...
    @winrt_commethod(45)
    def get_SentTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(46)
    def put_SentTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(47)
    def get_MeetingInfo(self) -> win32more.Windows.ApplicationModel.Email.EmailMeetingInfo: ...
    @winrt_commethod(48)
    def put_MeetingInfo(self, value: win32more.Windows.ApplicationModel.Email.EmailMeetingInfo) -> Void: ...
    @winrt_commethod(49)
    def GetBodyStream(self, type: win32more.Windows.ApplicationModel.Email.EmailMessageBodyKind) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(50)
    def SetBodyStream(self, type: win32more.Windows.ApplicationModel.Email.EmailMessageBodyKind, stream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    Id = property(get_Id, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
    MailboxId = property(get_MailboxId, None)
    ConversationId = property(get_ConversationId, None)
    FolderId = property(get_FolderId, None)
    AllowInternetImages = property(get_AllowInternetImages, put_AllowInternetImages)
    ChangeNumber = property(get_ChangeNumber, None)
    DownloadState = property(get_DownloadState, put_DownloadState)
    EstimatedDownloadSizeInBytes = property(get_EstimatedDownloadSizeInBytes, put_EstimatedDownloadSizeInBytes)
    FlagState = property(get_FlagState, put_FlagState)
    HasPartialBodies = property(get_HasPartialBodies, None)
    Importance = property(get_Importance, put_Importance)
    InResponseToMessageId = property(get_InResponseToMessageId, None)
    IrmInfo = property(get_IrmInfo, put_IrmInfo)
    IsDraftMessage = property(get_IsDraftMessage, None)
    IsRead = property(get_IsRead, put_IsRead)
    IsSeen = property(get_IsSeen, put_IsSeen)
    IsServerSearchMessage = property(get_IsServerSearchMessage, None)
    IsSmartSendable = property(get_IsSmartSendable, None)
    MessageClass = property(get_MessageClass, put_MessageClass)
    NormalizedSubject = property(get_NormalizedSubject, None)
    OriginalCodePage = property(get_OriginalCodePage, put_OriginalCodePage)
    Preview = property(get_Preview, put_Preview)
    LastResponseKind = property(get_LastResponseKind, put_LastResponseKind)
    Sender = property(get_Sender, put_Sender)
    SentTime = property(get_SentTime, put_SentTime)
    MeetingInfo = property(get_MeetingInfo, put_MeetingInfo)
class IEmailMessage3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMessage3'
    _iid_ = Guid('{a1ea675c-e598-4d29-a018-fc7b7eece0a1}')
    @winrt_commethod(6)
    def get_SmimeData(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(7)
    def put_SmimeData(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(8)
    def get_SmimeKind(self) -> win32more.Windows.ApplicationModel.Email.EmailMessageSmimeKind: ...
    @winrt_commethod(9)
    def put_SmimeKind(self, value: win32more.Windows.ApplicationModel.Email.EmailMessageSmimeKind) -> Void: ...
    SmimeData = property(get_SmimeData, put_SmimeData)
    SmimeKind = property(get_SmimeKind, put_SmimeKind)
class IEmailMessage4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMessage4'
    _iid_ = Guid('{317cf181-3e7f-4a05-8394-3e10336dd435}')
    @winrt_commethod(6)
    def get_ReplyTo(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Email.EmailRecipient]: ...
    @winrt_commethod(7)
    def get_SentRepresenting(self) -> win32more.Windows.ApplicationModel.Email.EmailRecipient: ...
    @winrt_commethod(8)
    def put_SentRepresenting(self, value: win32more.Windows.ApplicationModel.Email.EmailRecipient) -> Void: ...
    ReplyTo = property(get_ReplyTo, None)
    SentRepresenting = property(get_SentRepresenting, put_SentRepresenting)
class IEmailMessageBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMessageBatch'
    _iid_ = Guid('{605cd08f-25d9-4f1b-9e51-0514c0149653}')
    @winrt_commethod(6)
    def get_Messages(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailMessage]: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Email.EmailBatchStatus: ...
    Messages = property(get_Messages, None)
    Status = property(get_Status, None)
class IEmailMessageReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailMessageReader'
    _iid_ = Guid('{2f4abe9f-6213-4a85-a3b0-f92d1a839d19}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMessageBatch]: ...
class IEmailQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailQueryOptions'
    _iid_ = Guid('{45504b9b-3e7f-4d52-b6dd-d6fd4e1fbd9a}')
    @winrt_commethod(6)
    def get_TextSearch(self) -> win32more.Windows.ApplicationModel.Email.EmailQueryTextSearch: ...
    @winrt_commethod(7)
    def get_SortDirection(self) -> win32more.Windows.ApplicationModel.Email.EmailQuerySortDirection: ...
    @winrt_commethod(8)
    def put_SortDirection(self, value: win32more.Windows.ApplicationModel.Email.EmailQuerySortDirection) -> Void: ...
    @winrt_commethod(9)
    def get_SortProperty(self) -> win32more.Windows.ApplicationModel.Email.EmailQuerySortProperty: ...
    @winrt_commethod(10)
    def put_SortProperty(self, value: win32more.Windows.ApplicationModel.Email.EmailQuerySortProperty) -> Void: ...
    @winrt_commethod(11)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Email.EmailQueryKind: ...
    @winrt_commethod(12)
    def put_Kind(self, value: win32more.Windows.ApplicationModel.Email.EmailQueryKind) -> Void: ...
    @winrt_commethod(13)
    def get_FolderIds(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    TextSearch = property(get_TextSearch, None)
    SortDirection = property(get_SortDirection, put_SortDirection)
    SortProperty = property(get_SortProperty, put_SortProperty)
    Kind = property(get_Kind, put_Kind)
    FolderIds = property(get_FolderIds, None)
class IEmailQueryOptionsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailQueryOptionsFactory'
    _iid_ = Guid('{88f1a1b8-78ab-4ee8-b4e3-046d6e2fe5e2}')
    @winrt_commethod(6)
    def CreateWithText(self, text: WinRT_String) -> win32more.Windows.ApplicationModel.Email.EmailQueryOptions: ...
    @winrt_commethod(7)
    def CreateWithTextAndFields(self, text: WinRT_String, fields: win32more.Windows.ApplicationModel.Email.EmailQuerySearchFields) -> win32more.Windows.ApplicationModel.Email.EmailQueryOptions: ...
class IEmailQueryTextSearch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailQueryTextSearch'
    _iid_ = Guid('{9fa0a288-3c5d-46a5-a6e2-31d6fd17e540}')
    @winrt_commethod(6)
    def get_Fields(self) -> win32more.Windows.ApplicationModel.Email.EmailQuerySearchFields: ...
    @winrt_commethod(7)
    def put_Fields(self, value: win32more.Windows.ApplicationModel.Email.EmailQuerySearchFields) -> Void: ...
    @winrt_commethod(8)
    def get_SearchScope(self) -> win32more.Windows.ApplicationModel.Email.EmailQuerySearchScope: ...
    @winrt_commethod(9)
    def put_SearchScope(self, value: win32more.Windows.ApplicationModel.Email.EmailQuerySearchScope) -> Void: ...
    @winrt_commethod(10)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Text(self, value: WinRT_String) -> Void: ...
    Fields = property(get_Fields, put_Fields)
    SearchScope = property(get_SearchScope, put_SearchScope)
    Text = property(get_Text, put_Text)
class IEmailRecipient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailRecipient'
    _iid_ = Guid('{cae825b3-4478-4814-b900-c902b5e19b53}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Address(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Address(self, value: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)
    Address = property(get_Address, put_Address)
class IEmailRecipientFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailRecipientFactory'
    _iid_ = Guid('{5500b84d-c79a-4ef8-b909-722e18e3935d}')
    @winrt_commethod(6)
    def Create(self, address: WinRT_String) -> win32more.Windows.ApplicationModel.Email.EmailRecipient: ...
    @winrt_commethod(7)
    def CreateWithName(self, address: WinRT_String, name: WinRT_String) -> win32more.Windows.ApplicationModel.Email.EmailRecipient: ...
class IEmailRecipientResolutionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailRecipientResolutionResult'
    _iid_ = Guid('{918338fa-8d8d-4573-80d1-07172a34b98d}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Email.EmailRecipientResolutionStatus: ...
    @winrt_commethod(7)
    def get_PublicKeys(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    Status = property(get_Status, None)
    PublicKeys = property(get_PublicKeys, None)
class IEmailRecipientResolutionResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailRecipientResolutionResult2'
    _iid_ = Guid('{5e420bb6-ce5b-4bde-b9d4-e16da0b09fca}')
    @winrt_commethod(6)
    def put_Status(self, value: win32more.Windows.ApplicationModel.Email.EmailRecipientResolutionStatus) -> Void: ...
    @winrt_commethod(7)
    def SetPublicKeys(self, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.Certificate]) -> Void: ...
    Status = property(None, put_Status)
class IEmailStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailStore'
    _iid_ = Guid('{f803226e-9137-4f8b-a470-279ac3058eb6}')
    @winrt_commethod(6)
    def FindMailboxesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailMailbox]]: ...
    @winrt_commethod(7)
    def GetConversationReader(self) -> win32more.Windows.ApplicationModel.Email.EmailConversationReader: ...
    @winrt_commethod(8)
    def GetConversationReaderWithOptions(self, options: win32more.Windows.ApplicationModel.Email.EmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailConversationReader: ...
    @winrt_commethod(9)
    def GetMessageReader(self) -> win32more.Windows.ApplicationModel.Email.EmailMessageReader: ...
    @winrt_commethod(10)
    def GetMessageReaderWithOptions(self, options: win32more.Windows.ApplicationModel.Email.EmailQueryOptions) -> win32more.Windows.ApplicationModel.Email.EmailMessageReader: ...
    @winrt_commethod(11)
    def GetMailboxAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailbox]: ...
    @winrt_commethod(12)
    def GetConversationAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailConversation]: ...
    @winrt_commethod(13)
    def GetFolderAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailFolder]: ...
    @winrt_commethod(14)
    def GetMessageAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMessage]: ...
    @winrt_commethod(15)
    def CreateMailboxAsync(self, accountName: WinRT_String, accountAddress: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailbox]: ...
    @winrt_commethod(16)
    def CreateMailboxInAccountAsync(self, accountName: WinRT_String, accountAddress: WinRT_String, userDataAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Email.EmailMailbox]: ...
class IEmailStoreNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.IEmailStoreNotificationTriggerDetails'
    _iid_ = Guid('{ce17563c-46e6-43c9-96f7-facf7dd710cb}')
make_ready(__name__)
