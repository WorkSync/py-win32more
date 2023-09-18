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
import win32more.Windows.ApplicationModel.Contacts
import win32more.Windows.Data.Text
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.UI
import win32more.Windows.UI.Popups
import win32more.Windows.UI.ViewManagement
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AggregateContactManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IAggregateContactManager
    _classid_ = 'Windows.ApplicationModel.Contacts.AggregateContactManager'
    @winrt_mixinmethod
    def FindRawContactsAsync(self: win32more.Windows.ApplicationModel.Contacts.IAggregateContactManager, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.Contact]]: ...
    @winrt_mixinmethod
    def TryLinkContactsAsync(self: win32more.Windows.ApplicationModel.Contacts.IAggregateContactManager, primaryContact: win32more.Windows.ApplicationModel.Contacts.Contact, secondaryContact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_mixinmethod
    def UnlinkRawContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IAggregateContactManager, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def TrySetPreferredSourceForPictureAsync(self: win32more.Windows.ApplicationModel.Contacts.IAggregateContactManager, aggregateContact: win32more.Windows.ApplicationModel.Contacts.Contact, rawContact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SetRemoteIdentificationInformationAsync(self: win32more.Windows.ApplicationModel.Contacts.IAggregateContactManager2, contactListId: WinRT_String, remoteSourceId: WinRT_String, accountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class Contact(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContact
    _classid_ = 'Windows.ApplicationModel.Contacts.Contact'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Contacts.IContact) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.ApplicationModel.Contacts.IContact, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.ApplicationModel.Contacts.IContact) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: win32more.Windows.ApplicationModel.Contacts.IContact, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Fields(self: win32more.Windows.ApplicationModel.Contacts.IContact) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.IContactField]: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Contacts.IContact2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.ApplicationModel.Contacts.IContact2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Notes(self: win32more.Windows.ApplicationModel.Contacts.IContact2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Notes(self: win32more.Windows.ApplicationModel.Contacts.IContact2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Phones(self: win32more.Windows.ApplicationModel.Contacts.IContact2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactPhone]: ...
    @winrt_mixinmethod
    def get_Emails(self: win32more.Windows.ApplicationModel.Contacts.IContact2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactEmail]: ...
    @winrt_mixinmethod
    def get_Addresses(self: win32more.Windows.ApplicationModel.Contacts.IContact2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactAddress]: ...
    @winrt_mixinmethod
    def get_ConnectedServiceAccounts(self: win32more.Windows.ApplicationModel.Contacts.IContact2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactConnectedServiceAccount]: ...
    @winrt_mixinmethod
    def get_ImportantDates(self: win32more.Windows.ApplicationModel.Contacts.IContact2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactDate]: ...
    @winrt_mixinmethod
    def get_DataSuppliers(self: win32more.Windows.ApplicationModel.Contacts.IContact2) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_JobInfo(self: win32more.Windows.ApplicationModel.Contacts.IContact2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactJobInfo]: ...
    @winrt_mixinmethod
    def get_SignificantOthers(self: win32more.Windows.ApplicationModel.Contacts.IContact2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactSignificantOther]: ...
    @winrt_mixinmethod
    def get_Websites(self: win32more.Windows.ApplicationModel.Contacts.IContact2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactWebsite]: ...
    @winrt_mixinmethod
    def get_ProviderProperties(self: win32more.Windows.ApplicationModel.Contacts.IContact2) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def get_FirstName(self: win32more.Windows.ApplicationModel.Contacts.IContactName) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FirstName(self: win32more.Windows.ApplicationModel.Contacts.IContactName, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_LastName(self: win32more.Windows.ApplicationModel.Contacts.IContactName) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LastName(self: win32more.Windows.ApplicationModel.Contacts.IContactName, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_MiddleName(self: win32more.Windows.ApplicationModel.Contacts.IContactName) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_MiddleName(self: win32more.Windows.ApplicationModel.Contacts.IContactName, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_YomiGivenName(self: win32more.Windows.ApplicationModel.Contacts.IContactName) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_YomiGivenName(self: win32more.Windows.ApplicationModel.Contacts.IContactName, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_YomiFamilyName(self: win32more.Windows.ApplicationModel.Contacts.IContactName) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_YomiFamilyName(self: win32more.Windows.ApplicationModel.Contacts.IContactName, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HonorificNameSuffix(self: win32more.Windows.ApplicationModel.Contacts.IContactName) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HonorificNameSuffix(self: win32more.Windows.ApplicationModel.Contacts.IContactName, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HonorificNamePrefix(self: win32more.Windows.ApplicationModel.Contacts.IContactName) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HonorificNamePrefix(self: win32more.Windows.ApplicationModel.Contacts.IContactName, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.Contacts.IContactName) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_YomiDisplayName(self: win32more.Windows.ApplicationModel.Contacts.IContactName) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContactListId(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayPictureUserUpdateTime(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_DisplayPictureUserUpdateTime(self: win32more.Windows.ApplicationModel.Contacts.IContact3, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_IsMe(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> Boolean: ...
    @winrt_mixinmethod
    def get_AggregateId(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: win32more.Windows.ApplicationModel.Contacts.IContact3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RingToneToken(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RingToneToken(self: win32more.Windows.ApplicationModel.Contacts.IContact3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsDisplayPictureManuallySet(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> Boolean: ...
    @winrt_mixinmethod
    def get_LargeDisplayPicture(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_SmallDisplayPicture(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_SourceDisplayPicture(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_SourceDisplayPicture(self: win32more.Windows.ApplicationModel.Contacts.IContact3, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_TextToneToken(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TextToneToken(self: win32more.Windows.ApplicationModel.Contacts.IContact3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsAggregate(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> Boolean: ...
    @winrt_mixinmethod
    def get_FullName(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayNameOverride(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayNameOverride(self: win32more.Windows.ApplicationModel.Contacts.IContact3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Nickname(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Nickname(self: win32more.Windows.ApplicationModel.Contacts.IContact3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SortName(self: win32more.Windows.ApplicationModel.Contacts.IContact3) -> WinRT_String: ...
    Name = property(get_Name, put_Name)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    Fields = property(get_Fields, None)
    Id = property(get_Id, put_Id)
    Notes = property(get_Notes, put_Notes)
    Phones = property(get_Phones, None)
    Emails = property(get_Emails, None)
    Addresses = property(get_Addresses, None)
    ConnectedServiceAccounts = property(get_ConnectedServiceAccounts, None)
    ImportantDates = property(get_ImportantDates, None)
    DataSuppliers = property(get_DataSuppliers, None)
    JobInfo = property(get_JobInfo, None)
    SignificantOthers = property(get_SignificantOthers, None)
    Websites = property(get_Websites, None)
    ProviderProperties = property(get_ProviderProperties, None)
    FirstName = property(get_FirstName, put_FirstName)
    LastName = property(get_LastName, put_LastName)
    MiddleName = property(get_MiddleName, put_MiddleName)
    YomiGivenName = property(get_YomiGivenName, put_YomiGivenName)
    YomiFamilyName = property(get_YomiFamilyName, put_YomiFamilyName)
    HonorificNameSuffix = property(get_HonorificNameSuffix, put_HonorificNameSuffix)
    HonorificNamePrefix = property(get_HonorificNamePrefix, put_HonorificNamePrefix)
    DisplayName = property(get_DisplayName, None)
    YomiDisplayName = property(get_YomiDisplayName, None)
    ContactListId = property(get_ContactListId, None)
    DisplayPictureUserUpdateTime = property(get_DisplayPictureUserUpdateTime, put_DisplayPictureUserUpdateTime)
    IsMe = property(get_IsMe, None)
    AggregateId = property(get_AggregateId, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
    RingToneToken = property(get_RingToneToken, put_RingToneToken)
    IsDisplayPictureManuallySet = property(get_IsDisplayPictureManuallySet, None)
    LargeDisplayPicture = property(get_LargeDisplayPicture, None)
    SmallDisplayPicture = property(get_SmallDisplayPicture, None)
    SourceDisplayPicture = property(get_SourceDisplayPicture, put_SourceDisplayPicture)
    TextToneToken = property(get_TextToneToken, put_TextToneToken)
    IsAggregate = property(get_IsAggregate, None)
    FullName = property(get_FullName, None)
    DisplayNameOverride = property(get_DisplayNameOverride, put_DisplayNameOverride)
    Nickname = property(get_Nickname, put_Nickname)
    SortName = property(get_SortName, None)
class ContactAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactAddress
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactAddress'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactAddress: ...
    @winrt_mixinmethod
    def get_StreetAddress(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_StreetAddress(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Locality(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Locality(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Region(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Region(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Country(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Country(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PostalCode(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PostalCode(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress) -> win32more.Windows.ApplicationModel.Contacts.ContactAddressKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress, value: win32more.Windows.ApplicationModel.Contacts.ContactAddressKind) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactAddress, value: WinRT_String) -> Void: ...
    StreetAddress = property(get_StreetAddress, put_StreetAddress)
    Locality = property(get_Locality, put_Locality)
    Region = property(get_Region, put_Region)
    Country = property(get_Country, put_Country)
    PostalCode = property(get_PostalCode, put_PostalCode)
    Kind = property(get_Kind, put_Kind)
    Description = property(get_Description, put_Description)
ContactAddressKind = Int32
ContactAddressKind_Home: ContactAddressKind = 0
ContactAddressKind_Work: ContactAddressKind = 1
ContactAddressKind_Other: ContactAddressKind = 2
class ContactAnnotation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactAnnotation'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactAnnotation: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AnnotationListId(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContactId(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContactId(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedOperations(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation) -> win32more.Windows.ApplicationModel.Contacts.ContactAnnotationOperations: ...
    @winrt_mixinmethod
    def put_SupportedOperations(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation, value: win32more.Windows.ApplicationModel.Contacts.ContactAnnotationOperations) -> Void: ...
    @winrt_mixinmethod
    def get_IsDisabled(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation) -> Boolean: ...
    @winrt_mixinmethod
    def get_ProviderProperties(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_ContactListId(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContactListId(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotation2, value: WinRT_String) -> Void: ...
    Id = property(get_Id, None)
    AnnotationListId = property(get_AnnotationListId, None)
    ContactId = property(get_ContactId, put_ContactId)
    RemoteId = property(get_RemoteId, put_RemoteId)
    SupportedOperations = property(get_SupportedOperations, put_SupportedOperations)
    IsDisabled = property(get_IsDisabled, None)
    ProviderProperties = property(get_ProviderProperties, None)
    ContactListId = property(get_ContactListId, put_ContactListId)
class ContactAnnotationList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationList
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactAnnotationList'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationList) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProviderPackageFamilyName(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationList) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserDataAccountId(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationList) -> WinRT_String: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationList) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def TrySaveAnnotationAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationList, annotation: win32more.Windows.ApplicationModel.Contacts.ContactAnnotation) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def GetAnnotationAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationList, annotationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactAnnotation]: ...
    @winrt_mixinmethod
    def FindAnnotationsByRemoteIdAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationList, remoteId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactAnnotation]]: ...
    @winrt_mixinmethod
    def FindAnnotationsAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationList) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactAnnotation]]: ...
    @winrt_mixinmethod
    def DeleteAnnotationAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationList, annotation: win32more.Windows.ApplicationModel.Contacts.ContactAnnotation) -> win32more.Windows.Foundation.IAsyncAction: ...
    Id = property(get_Id, None)
    ProviderPackageFamilyName = property(get_ProviderPackageFamilyName, None)
    UserDataAccountId = property(get_UserDataAccountId, None)
ContactAnnotationOperations = UInt32
ContactAnnotationOperations_None: ContactAnnotationOperations = 0
ContactAnnotationOperations_ContactProfile: ContactAnnotationOperations = 1
ContactAnnotationOperations_Message: ContactAnnotationOperations = 2
ContactAnnotationOperations_AudioCall: ContactAnnotationOperations = 4
ContactAnnotationOperations_VideoCall: ContactAnnotationOperations = 8
ContactAnnotationOperations_SocialFeeds: ContactAnnotationOperations = 16
ContactAnnotationOperations_Share: ContactAnnotationOperations = 32
class ContactAnnotationStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationStore
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactAnnotationStore'
    @winrt_mixinmethod
    def FindContactIdsByEmailAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationStore, emailAddress: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def FindContactIdsByPhoneNumberAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationStore, phoneNumber: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def FindAnnotationsForContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationStore, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactAnnotation]]: ...
    @winrt_mixinmethod
    def DisableAnnotationAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationStore, annotation: win32more.Windows.ApplicationModel.Contacts.ContactAnnotation) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CreateAnnotationListAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationStore) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationList]: ...
    @winrt_mixinmethod
    def CreateAnnotationListInAccountAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationStore, userDataAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationList]: ...
    @winrt_mixinmethod
    def GetAnnotationListAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationStore, annotationListId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationList]: ...
    @winrt_mixinmethod
    def FindAnnotationListsAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationStore) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationList]]: ...
    @winrt_mixinmethod
    def FindAnnotationsForContactListAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactAnnotationStore2, contactListId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactAnnotation]]: ...
ContactAnnotationStoreAccessType = Int32
ContactAnnotationStoreAccessType_AppAnnotationsReadWrite: ContactAnnotationStoreAccessType = 0
ContactAnnotationStoreAccessType_AllAnnotationsReadWrite: ContactAnnotationStoreAccessType = 1
class ContactBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactBatch
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactBatch'
    @winrt_mixinmethod
    def get_Contacts(self: win32more.Windows.ApplicationModel.Contacts.IContactBatch) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Contacts.IContactBatch) -> win32more.Windows.ApplicationModel.Contacts.ContactBatchStatus: ...
    Contacts = property(get_Contacts, None)
    Status = property(get_Status, None)
ContactBatchStatus = Int32
ContactBatchStatus_Success: ContactBatchStatus = 0
ContactBatchStatus_ServerSearchSyncManagerError: ContactBatchStatus = 1
ContactBatchStatus_ServerSearchUnknownError: ContactBatchStatus = 2
class ContactCardDelayedDataLoader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactCardDelayedDataLoader
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactCardDelayedDataLoader'
    @winrt_mixinmethod
    def SetData(self: win32more.Windows.ApplicationModel.Contacts.IContactCardDelayedDataLoader, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
ContactCardHeaderKind = Int32
ContactCardHeaderKind_Default: ContactCardHeaderKind = 0
ContactCardHeaderKind_Basic: ContactCardHeaderKind = 1
ContactCardHeaderKind_Enterprise: ContactCardHeaderKind = 2
class ContactCardOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactCardOptions
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactCardOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactCardOptions: ...
    @winrt_mixinmethod
    def get_HeaderKind(self: win32more.Windows.ApplicationModel.Contacts.IContactCardOptions) -> win32more.Windows.ApplicationModel.Contacts.ContactCardHeaderKind: ...
    @winrt_mixinmethod
    def put_HeaderKind(self: win32more.Windows.ApplicationModel.Contacts.IContactCardOptions, value: win32more.Windows.ApplicationModel.Contacts.ContactCardHeaderKind) -> Void: ...
    @winrt_mixinmethod
    def get_InitialTabKind(self: win32more.Windows.ApplicationModel.Contacts.IContactCardOptions) -> win32more.Windows.ApplicationModel.Contacts.ContactCardTabKind: ...
    @winrt_mixinmethod
    def put_InitialTabKind(self: win32more.Windows.ApplicationModel.Contacts.IContactCardOptions, value: win32more.Windows.ApplicationModel.Contacts.ContactCardTabKind) -> Void: ...
    @winrt_mixinmethod
    def get_ServerSearchContactListIds(self: win32more.Windows.ApplicationModel.Contacts.IContactCardOptions2) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    HeaderKind = property(get_HeaderKind, put_HeaderKind)
    InitialTabKind = property(get_InitialTabKind, put_InitialTabKind)
    ServerSearchContactListIds = property(get_ServerSearchContactListIds, None)
ContactCardTabKind = Int32
ContactCardTabKind_Default: ContactCardTabKind = 0
ContactCardTabKind_Email: ContactCardTabKind = 1
ContactCardTabKind_Messaging: ContactCardTabKind = 2
ContactCardTabKind_Phone: ContactCardTabKind = 3
ContactCardTabKind_Video: ContactCardTabKind = 4
ContactCardTabKind_OrganizationalHierarchy: ContactCardTabKind = 5
class ContactChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactChange
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactChange'
    @winrt_mixinmethod
    def get_ChangeType(self: win32more.Windows.ApplicationModel.Contacts.IContactChange) -> win32more.Windows.ApplicationModel.Contacts.ContactChangeType: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Contacts.IContactChange) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    ChangeType = property(get_ChangeType, None)
    Contact = property(get_Contact, None)
class ContactChangeReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactChangeReader
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactChangeReader'
    @winrt_mixinmethod
    def AcceptChanges(self: win32more.Windows.ApplicationModel.Contacts.IContactChangeReader) -> Void: ...
    @winrt_mixinmethod
    def AcceptChangesThrough(self: win32more.Windows.ApplicationModel.Contacts.IContactChangeReader, lastChangeToAccept: win32more.Windows.ApplicationModel.Contacts.ContactChange) -> Void: ...
    @winrt_mixinmethod
    def ReadBatchAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactChangeReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactChange]]: ...
class ContactChangeTracker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactChangeTracker
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactChangeTracker'
    @winrt_mixinmethod
    def Enable(self: win32more.Windows.ApplicationModel.Contacts.IContactChangeTracker) -> Void: ...
    @winrt_mixinmethod
    def GetChangeReader(self: win32more.Windows.ApplicationModel.Contacts.IContactChangeTracker) -> win32more.Windows.ApplicationModel.Contacts.ContactChangeReader: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.ApplicationModel.Contacts.IContactChangeTracker) -> Void: ...
    @winrt_mixinmethod
    def get_IsTracking(self: win32more.Windows.ApplicationModel.Contacts.IContactChangeTracker2) -> Boolean: ...
    IsTracking = property(get_IsTracking, None)
ContactChangeType = Int32
ContactChangeType_Created: ContactChangeType = 0
ContactChangeType_Modified: ContactChangeType = 1
ContactChangeType_Deleted: ContactChangeType = 2
ContactChangeType_ChangeTrackingLost: ContactChangeType = 3
class ContactChangedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactChangedDeferral
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactChangedDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.Contacts.IContactChangedDeferral) -> Void: ...
class ContactChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Contacts.IContactChangedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.ContactChangedDeferral: ...
class ContactConnectedServiceAccount(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactConnectedServiceAccount
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactConnectedServiceAccount'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactConnectedServiceAccount: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Contacts.IContactConnectedServiceAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.ApplicationModel.Contacts.IContactConnectedServiceAccount, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ServiceName(self: win32more.Windows.ApplicationModel.Contacts.IContactConnectedServiceAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ServiceName(self: win32more.Windows.ApplicationModel.Contacts.IContactConnectedServiceAccount, value: WinRT_String) -> Void: ...
    Id = property(get_Id, put_Id)
    ServiceName = property(get_ServiceName, put_ServiceName)
class ContactDate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactDate
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactDate'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactDate: ...
    @winrt_mixinmethod
    def get_Day(self: win32more.Windows.ApplicationModel.Contacts.IContactDate) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_Day(self: win32more.Windows.ApplicationModel.Contacts.IContactDate, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_Month(self: win32more.Windows.ApplicationModel.Contacts.IContactDate) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_Month(self: win32more.Windows.ApplicationModel.Contacts.IContactDate, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_Year(self: win32more.Windows.ApplicationModel.Contacts.IContactDate) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_Year(self: win32more.Windows.ApplicationModel.Contacts.IContactDate, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Contacts.IContactDate) -> win32more.Windows.ApplicationModel.Contacts.ContactDateKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Windows.ApplicationModel.Contacts.IContactDate, value: win32more.Windows.ApplicationModel.Contacts.ContactDateKind) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactDate) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactDate, value: WinRT_String) -> Void: ...
    Day = property(get_Day, put_Day)
    Month = property(get_Month, put_Month)
    Year = property(get_Year, put_Year)
    Kind = property(get_Kind, put_Kind)
    Description = property(get_Description, put_Description)
ContactDateKind = Int32
ContactDateKind_Birthday: ContactDateKind = 0
ContactDateKind_Anniversary: ContactDateKind = 1
ContactDateKind_Other: ContactDateKind = 2
class ContactEmail(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactEmail
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactEmail'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactEmail: ...
    @winrt_mixinmethod
    def get_Address(self: win32more.Windows.ApplicationModel.Contacts.IContactEmail) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Address(self: win32more.Windows.ApplicationModel.Contacts.IContactEmail, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Contacts.IContactEmail) -> win32more.Windows.ApplicationModel.Contacts.ContactEmailKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Windows.ApplicationModel.Contacts.IContactEmail, value: win32more.Windows.ApplicationModel.Contacts.ContactEmailKind) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactEmail) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactEmail, value: WinRT_String) -> Void: ...
    Address = property(get_Address, put_Address)
    Kind = property(get_Kind, put_Kind)
    Description = property(get_Description, put_Description)
ContactEmailKind = Int32
ContactEmailKind_Personal: ContactEmailKind = 0
ContactEmailKind_Work: ContactEmailKind = 1
ContactEmailKind_Other: ContactEmailKind = 2
class ContactField(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactField
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactField'
    @winrt_factorymethod
    def CreateField(cls: win32more.Windows.ApplicationModel.Contacts.IContactFieldFactory, value: WinRT_String, type: win32more.Windows.ApplicationModel.Contacts.ContactFieldType) -> win32more.Windows.ApplicationModel.Contacts.ContactField: ...
    @winrt_factorymethod
    def CreateField(cls: win32more.Windows.ApplicationModel.Contacts.IContactFieldFactory, value: WinRT_String, type: win32more.Windows.ApplicationModel.Contacts.ContactFieldType, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory) -> win32more.Windows.ApplicationModel.Contacts.ContactField: ...
    @winrt_factorymethod
    def CreateField(cls: win32more.Windows.ApplicationModel.Contacts.IContactFieldFactory, name: WinRT_String, value: WinRT_String, type: win32more.Windows.ApplicationModel.Contacts.ContactFieldType, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory) -> win32more.Windows.ApplicationModel.Contacts.ContactField: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.ApplicationModel.Contacts.IContactField) -> win32more.Windows.ApplicationModel.Contacts.ContactFieldType: ...
    @winrt_mixinmethod
    def get_Category(self: win32more.Windows.ApplicationModel.Contacts.IContactField) -> win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Contacts.IContactField) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.ApplicationModel.Contacts.IContactField) -> WinRT_String: ...
    Type = property(get_Type, None)
    Category = property(get_Category, None)
    Name = property(get_Name, None)
    Value = property(get_Value, None)
ContactFieldCategory = Int32
ContactFieldCategory_None: ContactFieldCategory = 0
ContactFieldCategory_Home: ContactFieldCategory = 1
ContactFieldCategory_Work: ContactFieldCategory = 2
ContactFieldCategory_Mobile: ContactFieldCategory = 3
ContactFieldCategory_Other: ContactFieldCategory = 4
class ContactFieldFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactFieldFactory
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactFieldFactory'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactFieldFactory: ...
    @winrt_mixinmethod
    def CreateField_Default(self: win32more.Windows.ApplicationModel.Contacts.IContactFieldFactory, value: WinRT_String, type: win32more.Windows.ApplicationModel.Contacts.ContactFieldType) -> win32more.Windows.ApplicationModel.Contacts.ContactField: ...
    @winrt_mixinmethod
    def CreateField_Category(self: win32more.Windows.ApplicationModel.Contacts.IContactFieldFactory, value: WinRT_String, type: win32more.Windows.ApplicationModel.Contacts.ContactFieldType, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory) -> win32more.Windows.ApplicationModel.Contacts.ContactField: ...
    @winrt_mixinmethod
    def CreateField_Custom(self: win32more.Windows.ApplicationModel.Contacts.IContactFieldFactory, name: WinRT_String, value: WinRT_String, type: win32more.Windows.ApplicationModel.Contacts.ContactFieldType, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory) -> win32more.Windows.ApplicationModel.Contacts.ContactField: ...
    @winrt_mixinmethod
    def CreateLocation_Default(self: win32more.Windows.ApplicationModel.Contacts.IContactLocationFieldFactory, unstructuredAddress: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactLocationField: ...
    @winrt_mixinmethod
    def CreateLocation_Category(self: win32more.Windows.ApplicationModel.Contacts.IContactLocationFieldFactory, unstructuredAddress: WinRT_String, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory) -> win32more.Windows.ApplicationModel.Contacts.ContactLocationField: ...
    @winrt_mixinmethod
    def CreateLocation_All(self: win32more.Windows.ApplicationModel.Contacts.IContactLocationFieldFactory, unstructuredAddress: WinRT_String, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory, street: WinRT_String, city: WinRT_String, region: WinRT_String, country: WinRT_String, postalCode: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactLocationField: ...
    @winrt_mixinmethod
    def CreateInstantMessage_Default(self: win32more.Windows.ApplicationModel.Contacts.IContactInstantMessageFieldFactory, userName: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactInstantMessageField: ...
    @winrt_mixinmethod
    def CreateInstantMessage_Category(self: win32more.Windows.ApplicationModel.Contacts.IContactInstantMessageFieldFactory, userName: WinRT_String, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory) -> win32more.Windows.ApplicationModel.Contacts.ContactInstantMessageField: ...
    @winrt_mixinmethod
    def CreateInstantMessage_All(self: win32more.Windows.ApplicationModel.Contacts.IContactInstantMessageFieldFactory, userName: WinRT_String, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory, service: WinRT_String, displayText: WinRT_String, verb: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Contacts.ContactInstantMessageField: ...
ContactFieldType = Int32
ContactFieldType_Email: ContactFieldType = 0
ContactFieldType_PhoneNumber: ContactFieldType = 1
ContactFieldType_Location: ContactFieldType = 2
ContactFieldType_InstantMessage: ContactFieldType = 3
ContactFieldType_Custom: ContactFieldType = 4
ContactFieldType_ConnectedServiceAccount: ContactFieldType = 5
ContactFieldType_ImportantDate: ContactFieldType = 6
ContactFieldType_Address: ContactFieldType = 7
ContactFieldType_SignificantOther: ContactFieldType = 8
ContactFieldType_Notes: ContactFieldType = 9
ContactFieldType_Website: ContactFieldType = 10
ContactFieldType_JobInfo: ContactFieldType = 11
class ContactGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactGroup
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactGroup'
class ContactInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactInformation
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactInformation'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Contacts.IContactInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetThumbnailAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
    @winrt_mixinmethod
    def get_Emails(self: win32more.Windows.ApplicationModel.Contacts.IContactInformation) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactField]: ...
    @winrt_mixinmethod
    def get_PhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactInformation) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactField]: ...
    @winrt_mixinmethod
    def get_Locations(self: win32more.Windows.ApplicationModel.Contacts.IContactInformation) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactLocationField]: ...
    @winrt_mixinmethod
    def get_InstantMessages(self: win32more.Windows.ApplicationModel.Contacts.IContactInformation) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactInstantMessageField]: ...
    @winrt_mixinmethod
    def get_CustomFields(self: win32more.Windows.ApplicationModel.Contacts.IContactInformation) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactField]: ...
    @winrt_mixinmethod
    def QueryCustomFields(self: win32more.Windows.ApplicationModel.Contacts.IContactInformation, customName: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactField]: ...
    Name = property(get_Name, None)
    Emails = property(get_Emails, None)
    PhoneNumbers = property(get_PhoneNumbers, None)
    Locations = property(get_Locations, None)
    InstantMessages = property(get_InstantMessages, None)
    CustomFields = property(get_CustomFields, None)
class ContactInstantMessageField(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactInstantMessageField
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactInstantMessageField'
    @winrt_factorymethod
    def CreateInstantMessage(cls: win32more.Windows.ApplicationModel.Contacts.IContactInstantMessageFieldFactory, userName: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactInstantMessageField: ...
    @winrt_factorymethod
    def CreateInstantMessage(cls: win32more.Windows.ApplicationModel.Contacts.IContactInstantMessageFieldFactory, userName: WinRT_String, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory) -> win32more.Windows.ApplicationModel.Contacts.ContactInstantMessageField: ...
    @winrt_factorymethod
    def CreateInstantMessage(cls: win32more.Windows.ApplicationModel.Contacts.IContactInstantMessageFieldFactory, userName: WinRT_String, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory, service: WinRT_String, displayText: WinRT_String, verb: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Contacts.ContactInstantMessageField: ...
    @winrt_mixinmethod
    def get_UserName(self: win32more.Windows.ApplicationModel.Contacts.IContactInstantMessageField) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Service(self: win32more.Windows.ApplicationModel.Contacts.IContactInstantMessageField) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayText(self: win32more.Windows.ApplicationModel.Contacts.IContactInstantMessageField) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LaunchUri(self: win32more.Windows.ApplicationModel.Contacts.IContactInstantMessageField) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.ApplicationModel.Contacts.IContactField) -> win32more.Windows.ApplicationModel.Contacts.ContactFieldType: ...
    @winrt_mixinmethod
    def get_Category(self: win32more.Windows.ApplicationModel.Contacts.IContactField) -> win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Contacts.IContactField) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.ApplicationModel.Contacts.IContactField) -> WinRT_String: ...
    UserName = property(get_UserName, None)
    Service = property(get_Service, None)
    DisplayText = property(get_DisplayText, None)
    LaunchUri = property(get_LaunchUri, None)
    Type = property(get_Type, None)
    Category = property(get_Category, None)
    Name = property(get_Name, None)
    Value = property(get_Value, None)
class ContactJobInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactJobInfo'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactJobInfo: ...
    @winrt_mixinmethod
    def get_CompanyName(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CompanyName(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CompanyYomiName(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CompanyYomiName(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Department(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Department(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Manager(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Manager(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Office(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Office(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CompanyAddress(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CompanyAddress(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactJobInfo, value: WinRT_String) -> Void: ...
    CompanyName = property(get_CompanyName, put_CompanyName)
    CompanyYomiName = property(get_CompanyYomiName, put_CompanyYomiName)
    Department = property(get_Department, put_Department)
    Title = property(get_Title, put_Title)
    Manager = property(get_Manager, put_Manager)
    Office = property(get_Office, put_Office)
    CompanyAddress = property(get_CompanyAddress, put_CompanyAddress)
    Description = property(get_Description, put_Description)
class _ContactLaunchActionVerbs_Meta_(ComPtr.__class__):
    pass
class ContactLaunchActionVerbs(ComPtr, metaclass=_ContactLaunchActionVerbs_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactLaunchActionVerbs'
    @winrt_classmethod
    def get_Call(cls: win32more.Windows.ApplicationModel.Contacts.IContactLaunchActionVerbsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Message(cls: win32more.Windows.ApplicationModel.Contacts.IContactLaunchActionVerbsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Map(cls: win32more.Windows.ApplicationModel.Contacts.IContactLaunchActionVerbsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Post(cls: win32more.Windows.ApplicationModel.Contacts.IContactLaunchActionVerbsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoCall(cls: win32more.Windows.ApplicationModel.Contacts.IContactLaunchActionVerbsStatics) -> WinRT_String: ...
    _ContactLaunchActionVerbs_Meta_.Call = property(get_Call.__wrapped__, None)
    _ContactLaunchActionVerbs_Meta_.Message = property(get_Message.__wrapped__, None)
    _ContactLaunchActionVerbs_Meta_.Map = property(get_Map.__wrapped__, None)
    _ContactLaunchActionVerbs_Meta_.Post = property(get_Post.__wrapped__, None)
    _ContactLaunchActionVerbs_Meta_.VideoCall = property(get_VideoCall.__wrapped__, None)
class ContactList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactList
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactList'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.ApplicationModel.Contacts.IContactList, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SourceDisplayName(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsHidden(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsHidden(self: win32more.Windows.ApplicationModel.Contacts.IContactList, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OtherAppReadAccess(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> win32more.Windows.ApplicationModel.Contacts.ContactListOtherAppReadAccess: ...
    @winrt_mixinmethod
    def put_OtherAppReadAccess(self: win32more.Windows.ApplicationModel.Contacts.IContactList, value: win32more.Windows.ApplicationModel.Contacts.ContactListOtherAppReadAccess) -> Void: ...
    @winrt_mixinmethod
    def get_OtherAppWriteAccess(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> win32more.Windows.ApplicationModel.Contacts.ContactListOtherAppWriteAccess: ...
    @winrt_mixinmethod
    def put_OtherAppWriteAccess(self: win32more.Windows.ApplicationModel.Contacts.IContactList, value: win32more.Windows.ApplicationModel.Contacts.ContactListOtherAppWriteAccess) -> Void: ...
    @winrt_mixinmethod
    def get_ChangeTracker(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> win32more.Windows.ApplicationModel.Contacts.ContactChangeTracker: ...
    @winrt_mixinmethod
    def get_SyncManager(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> win32more.Windows.ApplicationModel.Contacts.ContactListSyncManager: ...
    @winrt_mixinmethod
    def get_SupportsServerSearch(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> Boolean: ...
    @winrt_mixinmethod
    def get_UserDataAccountId(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_ContactChanged(self: win32more.Windows.ApplicationModel.Contacts.IContactList, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.ContactList, win32more.Windows.ApplicationModel.Contacts.ContactChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContactChanged(self: win32more.Windows.ApplicationModel.Contacts.IContactList, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetContactFromRemoteIdAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactList, remoteId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_mixinmethod
    def GetMeContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_mixinmethod
    def GetContactReader(self: win32more.Windows.ApplicationModel.Contacts.IContactList) -> win32more.Windows.ApplicationModel.Contacts.ContactReader: ...
    @winrt_mixinmethod
    def GetContactReaderWithOptions(self: win32more.Windows.ApplicationModel.Contacts.IContactList, options: win32more.Windows.ApplicationModel.Contacts.ContactQueryOptions) -> win32more.Windows.ApplicationModel.Contacts.ContactReader: ...
    @winrt_mixinmethod
    def SaveContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactList, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactList, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactList, contactId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_mixinmethod
    def RegisterSyncManagerAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactList2) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def put_SupportsServerSearch(self: win32more.Windows.ApplicationModel.Contacts.IContactList2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SyncConstraints(self: win32more.Windows.ApplicationModel.Contacts.IContactList2) -> win32more.Windows.ApplicationModel.Contacts.ContactListSyncConstraints: ...
    @winrt_mixinmethod
    def get_LimitedWriteOperations(self: win32more.Windows.ApplicationModel.Contacts.IContactList3) -> win32more.Windows.ApplicationModel.Contacts.ContactListLimitedWriteOperations: ...
    @winrt_mixinmethod
    def GetChangeTracker(self: win32more.Windows.ApplicationModel.Contacts.IContactList3, identity: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactChangeTracker: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    SourceDisplayName = property(get_SourceDisplayName, None)
    IsHidden = property(get_IsHidden, put_IsHidden)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    OtherAppWriteAccess = property(get_OtherAppWriteAccess, put_OtherAppWriteAccess)
    ChangeTracker = property(get_ChangeTracker, None)
    SyncManager = property(get_SyncManager, None)
    SupportsServerSearch = property(get_SupportsServerSearch, put_SupportsServerSearch)
    UserDataAccountId = property(get_UserDataAccountId, None)
    SyncConstraints = property(get_SyncConstraints, None)
    LimitedWriteOperations = property(get_LimitedWriteOperations, None)
class ContactListLimitedWriteOperations(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactListLimitedWriteOperations
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactListLimitedWriteOperations'
    @winrt_mixinmethod
    def TryCreateOrUpdateContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactListLimitedWriteOperations, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryDeleteContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactListLimitedWriteOperations, contactId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
ContactListOtherAppReadAccess = Int32
ContactListOtherAppReadAccess_SystemOnly: ContactListOtherAppReadAccess = 0
ContactListOtherAppReadAccess_Limited: ContactListOtherAppReadAccess = 1
ContactListOtherAppReadAccess_Full: ContactListOtherAppReadAccess = 2
ContactListOtherAppReadAccess_None: ContactListOtherAppReadAccess = 3
ContactListOtherAppWriteAccess = Int32
ContactListOtherAppWriteAccess_None: ContactListOtherAppWriteAccess = 0
ContactListOtherAppWriteAccess_SystemOnly: ContactListOtherAppWriteAccess = 1
ContactListOtherAppWriteAccess_Limited: ContactListOtherAppWriteAccess = 2
class ContactListSyncConstraints(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactListSyncConstraints'
    @winrt_mixinmethod
    def get_CanSyncDescriptions(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanSyncDescriptions(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaxHomePhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxHomePhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxMobilePhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxMobilePhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxWorkPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxWorkPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxOtherPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxOtherPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxPagerPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxPagerPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxBusinessFaxPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxBusinessFaxPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxHomeFaxPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxHomeFaxPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxCompanyPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxCompanyPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxAssistantPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxAssistantPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxRadioPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxRadioPhoneNumbers(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxPersonalEmailAddresses(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxPersonalEmailAddresses(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxWorkEmailAddresses(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxWorkEmailAddresses(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxOtherEmailAddresses(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxOtherEmailAddresses(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxHomeAddresses(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxHomeAddresses(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxWorkAddresses(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxWorkAddresses(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxOtherAddresses(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxOtherAddresses(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxBirthdayDates(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxBirthdayDates(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxAnniversaryDates(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxAnniversaryDates(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxOtherDates(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxOtherDates(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxOtherRelationships(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxOtherRelationships(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxSpouseRelationships(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxSpouseRelationships(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxPartnerRelationships(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxPartnerRelationships(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxSiblingRelationships(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxSiblingRelationships(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxParentRelationships(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxParentRelationships(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxChildRelationships(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxChildRelationships(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxJobInfo(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxJobInfo(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxWebsites(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxWebsites(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncConstraints, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    CanSyncDescriptions = property(get_CanSyncDescriptions, put_CanSyncDescriptions)
    MaxHomePhoneNumbers = property(get_MaxHomePhoneNumbers, put_MaxHomePhoneNumbers)
    MaxMobilePhoneNumbers = property(get_MaxMobilePhoneNumbers, put_MaxMobilePhoneNumbers)
    MaxWorkPhoneNumbers = property(get_MaxWorkPhoneNumbers, put_MaxWorkPhoneNumbers)
    MaxOtherPhoneNumbers = property(get_MaxOtherPhoneNumbers, put_MaxOtherPhoneNumbers)
    MaxPagerPhoneNumbers = property(get_MaxPagerPhoneNumbers, put_MaxPagerPhoneNumbers)
    MaxBusinessFaxPhoneNumbers = property(get_MaxBusinessFaxPhoneNumbers, put_MaxBusinessFaxPhoneNumbers)
    MaxHomeFaxPhoneNumbers = property(get_MaxHomeFaxPhoneNumbers, put_MaxHomeFaxPhoneNumbers)
    MaxCompanyPhoneNumbers = property(get_MaxCompanyPhoneNumbers, put_MaxCompanyPhoneNumbers)
    MaxAssistantPhoneNumbers = property(get_MaxAssistantPhoneNumbers, put_MaxAssistantPhoneNumbers)
    MaxRadioPhoneNumbers = property(get_MaxRadioPhoneNumbers, put_MaxRadioPhoneNumbers)
    MaxPersonalEmailAddresses = property(get_MaxPersonalEmailAddresses, put_MaxPersonalEmailAddresses)
    MaxWorkEmailAddresses = property(get_MaxWorkEmailAddresses, put_MaxWorkEmailAddresses)
    MaxOtherEmailAddresses = property(get_MaxOtherEmailAddresses, put_MaxOtherEmailAddresses)
    MaxHomeAddresses = property(get_MaxHomeAddresses, put_MaxHomeAddresses)
    MaxWorkAddresses = property(get_MaxWorkAddresses, put_MaxWorkAddresses)
    MaxOtherAddresses = property(get_MaxOtherAddresses, put_MaxOtherAddresses)
    MaxBirthdayDates = property(get_MaxBirthdayDates, put_MaxBirthdayDates)
    MaxAnniversaryDates = property(get_MaxAnniversaryDates, put_MaxAnniversaryDates)
    MaxOtherDates = property(get_MaxOtherDates, put_MaxOtherDates)
    MaxOtherRelationships = property(get_MaxOtherRelationships, put_MaxOtherRelationships)
    MaxSpouseRelationships = property(get_MaxSpouseRelationships, put_MaxSpouseRelationships)
    MaxPartnerRelationships = property(get_MaxPartnerRelationships, put_MaxPartnerRelationships)
    MaxSiblingRelationships = property(get_MaxSiblingRelationships, put_MaxSiblingRelationships)
    MaxParentRelationships = property(get_MaxParentRelationships, put_MaxParentRelationships)
    MaxChildRelationships = property(get_MaxChildRelationships, put_MaxChildRelationships)
    MaxJobInfo = property(get_MaxJobInfo, put_MaxJobInfo)
    MaxWebsites = property(get_MaxWebsites, put_MaxWebsites)
class ContactListSyncManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactListSyncManager
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactListSyncManager'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncManager) -> win32more.Windows.ApplicationModel.Contacts.ContactListSyncStatus: ...
    @winrt_mixinmethod
    def get_LastSuccessfulSyncTime(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncManager) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_LastAttemptedSyncTime(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncManager) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def SyncAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncManager) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_SyncStatusChanged(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.ContactListSyncManager, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SyncStatusChanged(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncManager2, value: win32more.Windows.ApplicationModel.Contacts.ContactListSyncStatus) -> Void: ...
    @winrt_mixinmethod
    def put_LastSuccessfulSyncTime(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncManager2, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def put_LastAttemptedSyncTime(self: win32more.Windows.ApplicationModel.Contacts.IContactListSyncManager2, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    Status = property(get_Status, put_Status)
    LastSuccessfulSyncTime = property(get_LastSuccessfulSyncTime, put_LastSuccessfulSyncTime)
    LastAttemptedSyncTime = property(get_LastAttemptedSyncTime, put_LastAttemptedSyncTime)
ContactListSyncStatus = Int32
ContactListSyncStatus_Idle: ContactListSyncStatus = 0
ContactListSyncStatus_Syncing: ContactListSyncStatus = 1
ContactListSyncStatus_UpToDate: ContactListSyncStatus = 2
ContactListSyncStatus_AuthenticationError: ContactListSyncStatus = 3
ContactListSyncStatus_PolicyError: ContactListSyncStatus = 4
ContactListSyncStatus_UnknownError: ContactListSyncStatus = 5
ContactListSyncStatus_ManualAccountRemovalRequired: ContactListSyncStatus = 6
class ContactLocationField(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactLocationField
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactLocationField'
    @winrt_factorymethod
    def CreateLocation(cls: win32more.Windows.ApplicationModel.Contacts.IContactLocationFieldFactory, unstructuredAddress: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactLocationField: ...
    @winrt_factorymethod
    def CreateLocation(cls: win32more.Windows.ApplicationModel.Contacts.IContactLocationFieldFactory, unstructuredAddress: WinRT_String, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory) -> win32more.Windows.ApplicationModel.Contacts.ContactLocationField: ...
    @winrt_factorymethod
    def CreateLocation(cls: win32more.Windows.ApplicationModel.Contacts.IContactLocationFieldFactory, unstructuredAddress: WinRT_String, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory, street: WinRT_String, city: WinRT_String, region: WinRT_String, country: WinRT_String, postalCode: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactLocationField: ...
    @winrt_mixinmethod
    def get_UnstructuredAddress(self: win32more.Windows.ApplicationModel.Contacts.IContactLocationField) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Street(self: win32more.Windows.ApplicationModel.Contacts.IContactLocationField) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_City(self: win32more.Windows.ApplicationModel.Contacts.IContactLocationField) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Region(self: win32more.Windows.ApplicationModel.Contacts.IContactLocationField) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Country(self: win32more.Windows.ApplicationModel.Contacts.IContactLocationField) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PostalCode(self: win32more.Windows.ApplicationModel.Contacts.IContactLocationField) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.ApplicationModel.Contacts.IContactField) -> win32more.Windows.ApplicationModel.Contacts.ContactFieldType: ...
    @winrt_mixinmethod
    def get_Category(self: win32more.Windows.ApplicationModel.Contacts.IContactField) -> win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Contacts.IContactField) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.ApplicationModel.Contacts.IContactField) -> WinRT_String: ...
    UnstructuredAddress = property(get_UnstructuredAddress, None)
    Street = property(get_Street, None)
    City = property(get_City, None)
    Region = property(get_Region, None)
    Country = property(get_Country, None)
    PostalCode = property(get_PostalCode, None)
    Type = property(get_Type, None)
    Category = property(get_Category, None)
    Name = property(get_Name, None)
    Value = property(get_Value, None)
class _ContactManager_Meta_(ComPtr.__class__):
    pass
class ContactManager(ComPtr, metaclass=_ContactManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactManager'
    @winrt_classmethod
    def IsShowFullContactCardSupportedAsync(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics5) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_IncludeMiddleNameInSystemDisplayAndSort(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics5) -> Boolean: ...
    @winrt_classmethod
    def put_IncludeMiddleNameInSystemDisplayAndSort(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics5, value: Boolean) -> Void: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics4, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.Contacts.ContactManagerForUser: ...
    @winrt_classmethod
    def ConvertContactToVCardAsync(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_classmethod
    def ConvertContactToVCardAsyncWithMaxBytes(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3, contact: win32more.Windows.ApplicationModel.Contacts.Contact, maxBytes: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_classmethod
    def ConvertVCardToContactAsync(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3, vCard: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_classmethod
    def RequestStoreAsyncWithAccessType(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3, accessType: win32more.Windows.ApplicationModel.Contacts.ContactStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactStore]: ...
    @winrt_classmethod
    def RequestAnnotationStoreAsync(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3, accessType: win32more.Windows.ApplicationModel.Contacts.ContactAnnotationStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationStore]: ...
    @winrt_classmethod
    def IsShowContactCardSupported(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3) -> Boolean: ...
    @winrt_classmethod
    def ShowContactCardWithOptions(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3, contact: win32more.Windows.ApplicationModel.Contacts.Contact, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement, contactCardOptions: win32more.Windows.ApplicationModel.Contacts.ContactCardOptions) -> Void: ...
    @winrt_classmethod
    def IsShowDelayLoadedContactCardSupported(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3) -> Boolean: ...
    @winrt_classmethod
    def ShowDelayLoadedContactCardWithOptions(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3, contact: win32more.Windows.ApplicationModel.Contacts.Contact, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement, contactCardOptions: win32more.Windows.ApplicationModel.Contacts.ContactCardOptions) -> win32more.Windows.ApplicationModel.Contacts.ContactCardDelayedDataLoader: ...
    @winrt_classmethod
    def ShowFullContactCard(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3, contact: win32more.Windows.ApplicationModel.Contacts.Contact, fullContactCardOptions: win32more.Windows.ApplicationModel.Contacts.FullContactCardOptions) -> Void: ...
    @winrt_classmethod
    def get_SystemDisplayNameOrder(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3) -> win32more.Windows.ApplicationModel.Contacts.ContactNameOrder: ...
    @winrt_classmethod
    def put_SystemDisplayNameOrder(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3, value: win32more.Windows.ApplicationModel.Contacts.ContactNameOrder) -> Void: ...
    @winrt_classmethod
    def get_SystemSortOrder(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3) -> win32more.Windows.ApplicationModel.Contacts.ContactNameOrder: ...
    @winrt_classmethod
    def put_SystemSortOrder(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics3, value: win32more.Windows.ApplicationModel.Contacts.ContactNameOrder) -> Void: ...
    @winrt_classmethod
    def RequestStoreAsync(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactStore]: ...
    @winrt_classmethod
    def ShowContactCard(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics, contact: win32more.Windows.ApplicationModel.Contacts.Contact, selection: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_classmethod
    def ShowContactCardWithPlacement(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics, contact: win32more.Windows.ApplicationModel.Contacts.Contact, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> Void: ...
    @winrt_classmethod
    def ShowDelayLoadedContactCard(cls: win32more.Windows.ApplicationModel.Contacts.IContactManagerStatics, contact: win32more.Windows.ApplicationModel.Contacts.Contact, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.ApplicationModel.Contacts.ContactCardDelayedDataLoader: ...
    _ContactManager_Meta_.IncludeMiddleNameInSystemDisplayAndSort = property(get_IncludeMiddleNameInSystemDisplayAndSort.__wrapped__, put_IncludeMiddleNameInSystemDisplayAndSort.__wrapped__)
    _ContactManager_Meta_.SystemDisplayNameOrder = property(get_SystemDisplayNameOrder.__wrapped__, put_SystemDisplayNameOrder.__wrapped__)
    _ContactManager_Meta_.SystemSortOrder = property(get_SystemSortOrder.__wrapped__, put_SystemSortOrder.__wrapped__)
class ContactManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactManagerForUser
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactManagerForUser'
    @winrt_mixinmethod
    def ConvertContactToVCardAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactManagerForUser, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_mixinmethod
    def ConvertContactToVCardAsyncWithMaxBytes(self: win32more.Windows.ApplicationModel.Contacts.IContactManagerForUser, contact: win32more.Windows.ApplicationModel.Contacts.Contact, maxBytes: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_mixinmethod
    def ConvertVCardToContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactManagerForUser, vCard: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_mixinmethod
    def RequestStoreAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactManagerForUser, accessType: win32more.Windows.ApplicationModel.Contacts.ContactStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactStore]: ...
    @winrt_mixinmethod
    def RequestAnnotationStoreAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactManagerForUser, accessType: win32more.Windows.ApplicationModel.Contacts.ContactAnnotationStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationStore]: ...
    @winrt_mixinmethod
    def get_SystemDisplayNameOrder(self: win32more.Windows.ApplicationModel.Contacts.IContactManagerForUser) -> win32more.Windows.ApplicationModel.Contacts.ContactNameOrder: ...
    @winrt_mixinmethod
    def put_SystemDisplayNameOrder(self: win32more.Windows.ApplicationModel.Contacts.IContactManagerForUser, value: win32more.Windows.ApplicationModel.Contacts.ContactNameOrder) -> Void: ...
    @winrt_mixinmethod
    def get_SystemSortOrder(self: win32more.Windows.ApplicationModel.Contacts.IContactManagerForUser) -> win32more.Windows.ApplicationModel.Contacts.ContactNameOrder: ...
    @winrt_mixinmethod
    def put_SystemSortOrder(self: win32more.Windows.ApplicationModel.Contacts.IContactManagerForUser, value: win32more.Windows.ApplicationModel.Contacts.ContactNameOrder) -> Void: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Contacts.IContactManagerForUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def ShowFullContactCard(self: win32more.Windows.ApplicationModel.Contacts.IContactManagerForUser2, contact: win32more.Windows.ApplicationModel.Contacts.Contact, fullContactCardOptions: win32more.Windows.ApplicationModel.Contacts.FullContactCardOptions) -> Void: ...
    SystemDisplayNameOrder = property(get_SystemDisplayNameOrder, put_SystemDisplayNameOrder)
    SystemSortOrder = property(get_SystemSortOrder, put_SystemSortOrder)
    User = property(get_User, None)
class ContactMatchReason(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactMatchReason
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactMatchReason'
    @winrt_mixinmethod
    def get_Field(self: win32more.Windows.ApplicationModel.Contacts.IContactMatchReason) -> win32more.Windows.ApplicationModel.Contacts.ContactMatchReasonKind: ...
    @winrt_mixinmethod
    def get_Segments(self: win32more.Windows.ApplicationModel.Contacts.IContactMatchReason) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.TextSegment]: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.ApplicationModel.Contacts.IContactMatchReason) -> WinRT_String: ...
    Field = property(get_Field, None)
    Segments = property(get_Segments, None)
    Text = property(get_Text, None)
ContactMatchReasonKind = Int32
ContactMatchReasonKind_Name: ContactMatchReasonKind = 0
ContactMatchReasonKind_EmailAddress: ContactMatchReasonKind = 1
ContactMatchReasonKind_PhoneNumber: ContactMatchReasonKind = 2
ContactMatchReasonKind_JobInfo: ContactMatchReasonKind = 3
ContactMatchReasonKind_YomiName: ContactMatchReasonKind = 4
ContactMatchReasonKind_Other: ContactMatchReasonKind = 5
ContactNameOrder = Int32
ContactNameOrder_FirstNameLastName: ContactNameOrder = 0
ContactNameOrder_LastNameFirstName: ContactNameOrder = 1
class ContactPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactPanel
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactPanel'
    @winrt_mixinmethod
    def ClosePanel(self: win32more.Windows.ApplicationModel.Contacts.IContactPanel) -> Void: ...
    @winrt_mixinmethod
    def get_HeaderColor(self: win32more.Windows.ApplicationModel.Contacts.IContactPanel) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_HeaderColor(self: win32more.Windows.ApplicationModel.Contacts.IContactPanel, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def add_LaunchFullAppRequested(self: win32more.Windows.ApplicationModel.Contacts.IContactPanel, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.ContactPanel, win32more.Windows.ApplicationModel.Contacts.ContactPanelLaunchFullAppRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LaunchFullAppRequested(self: win32more.Windows.ApplicationModel.Contacts.IContactPanel, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closing(self: win32more.Windows.ApplicationModel.Contacts.IContactPanel, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.ContactPanel, win32more.Windows.ApplicationModel.Contacts.ContactPanelClosingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closing(self: win32more.Windows.ApplicationModel.Contacts.IContactPanel, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    HeaderColor = property(get_HeaderColor, put_HeaderColor)
class ContactPanelClosingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactPanelClosingEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactPanelClosingEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Contacts.IContactPanelClosingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class ContactPanelLaunchFullAppRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactPanelLaunchFullAppRequestedEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactPanelLaunchFullAppRequestedEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.ApplicationModel.Contacts.IContactPanelLaunchFullAppRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.ApplicationModel.Contacts.IContactPanelLaunchFullAppRequestedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class ContactPhone(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactPhone
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactPhone'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactPhone: ...
    @winrt_mixinmethod
    def get_Number(self: win32more.Windows.ApplicationModel.Contacts.IContactPhone) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Number(self: win32more.Windows.ApplicationModel.Contacts.IContactPhone, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Contacts.IContactPhone) -> win32more.Windows.ApplicationModel.Contacts.ContactPhoneKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Windows.ApplicationModel.Contacts.IContactPhone, value: win32more.Windows.ApplicationModel.Contacts.ContactPhoneKind) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactPhone) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactPhone, value: WinRT_String) -> Void: ...
    Number = property(get_Number, put_Number)
    Kind = property(get_Kind, put_Kind)
    Description = property(get_Description, put_Description)
ContactPhoneKind = Int32
ContactPhoneKind_Home: ContactPhoneKind = 0
ContactPhoneKind_Mobile: ContactPhoneKind = 1
ContactPhoneKind_Work: ContactPhoneKind = 2
ContactPhoneKind_Other: ContactPhoneKind = 3
ContactPhoneKind_Pager: ContactPhoneKind = 4
ContactPhoneKind_BusinessFax: ContactPhoneKind = 5
ContactPhoneKind_HomeFax: ContactPhoneKind = 6
ContactPhoneKind_Company: ContactPhoneKind = 7
ContactPhoneKind_Assistant: ContactPhoneKind = 8
ContactPhoneKind_Radio: ContactPhoneKind = 9
class ContactPicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactPicker
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactPicker'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactPicker: ...
    @winrt_mixinmethod
    def get_CommitButtonText(self: win32more.Windows.ApplicationModel.Contacts.IContactPicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CommitButtonText(self: win32more.Windows.ApplicationModel.Contacts.IContactPicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionMode(self: win32more.Windows.ApplicationModel.Contacts.IContactPicker) -> win32more.Windows.ApplicationModel.Contacts.ContactSelectionMode: ...
    @winrt_mixinmethod
    def put_SelectionMode(self: win32more.Windows.ApplicationModel.Contacts.IContactPicker, value: win32more.Windows.ApplicationModel.Contacts.ContactSelectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredFields(self: win32more.Windows.ApplicationModel.Contacts.IContactPicker) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def PickSingleContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactPicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactInformation]: ...
    @winrt_mixinmethod
    def PickMultipleContactsAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactPicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactInformation]]: ...
    @winrt_mixinmethod
    def get_DesiredFieldsWithContactFieldType(self: win32more.Windows.ApplicationModel.Contacts.IContactPicker2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactFieldType]: ...
    @winrt_mixinmethod
    def PickContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactPicker2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_mixinmethod
    def PickContactsAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactPicker2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.Contact]]: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Contacts.IContactPicker3) -> win32more.Windows.System.User: ...
    @winrt_classmethod
    def CreateForUser(cls: win32more.Windows.ApplicationModel.Contacts.IContactPickerStatics, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.Contacts.ContactPicker: ...
    @winrt_classmethod
    def IsSupportedAsync(cls: win32more.Windows.ApplicationModel.Contacts.IContactPickerStatics) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    SelectionMode = property(get_SelectionMode, put_SelectionMode)
    DesiredFields = property(get_DesiredFields, None)
    DesiredFieldsWithContactFieldType = property(get_DesiredFieldsWithContactFieldType, None)
    User = property(get_User, None)
ContactQueryDesiredFields = UInt32
ContactQueryDesiredFields_None: ContactQueryDesiredFields = 0
ContactQueryDesiredFields_PhoneNumber: ContactQueryDesiredFields = 1
ContactQueryDesiredFields_EmailAddress: ContactQueryDesiredFields = 2
ContactQueryDesiredFields_PostalAddress: ContactQueryDesiredFields = 4
class ContactQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactQueryOptions
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactQueryOptions'
    @winrt_factorymethod
    def CreateWithText(cls: win32more.Windows.ApplicationModel.Contacts.IContactQueryOptionsFactory, text: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactQueryOptions: ...
    @winrt_factorymethod
    def CreateWithTextAndFields(cls: win32more.Windows.ApplicationModel.Contacts.IContactQueryOptionsFactory, text: WinRT_String, fields: win32more.Windows.ApplicationModel.Contacts.ContactQuerySearchFields) -> win32more.Windows.ApplicationModel.Contacts.ContactQueryOptions: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactQueryOptions: ...
    @winrt_mixinmethod
    def get_TextSearch(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryOptions) -> win32more.Windows.ApplicationModel.Contacts.ContactQueryTextSearch: ...
    @winrt_mixinmethod
    def get_ContactListIds(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryOptions) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IncludeContactsFromHiddenLists(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeContactsFromHiddenLists(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredFields(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryOptions) -> win32more.Windows.ApplicationModel.Contacts.ContactQueryDesiredFields: ...
    @winrt_mixinmethod
    def put_DesiredFields(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryOptions, value: win32more.Windows.ApplicationModel.Contacts.ContactQueryDesiredFields) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredOperations(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryOptions) -> win32more.Windows.ApplicationModel.Contacts.ContactAnnotationOperations: ...
    @winrt_mixinmethod
    def put_DesiredOperations(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryOptions, value: win32more.Windows.ApplicationModel.Contacts.ContactAnnotationOperations) -> Void: ...
    @winrt_mixinmethod
    def get_AnnotationListIds(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryOptions) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    TextSearch = property(get_TextSearch, None)
    ContactListIds = property(get_ContactListIds, None)
    IncludeContactsFromHiddenLists = property(get_IncludeContactsFromHiddenLists, put_IncludeContactsFromHiddenLists)
    DesiredFields = property(get_DesiredFields, put_DesiredFields)
    DesiredOperations = property(get_DesiredOperations, put_DesiredOperations)
    AnnotationListIds = property(get_AnnotationListIds, None)
ContactQuerySearchFields = UInt32
ContactQuerySearchFields_None: ContactQuerySearchFields = 0
ContactQuerySearchFields_Name: ContactQuerySearchFields = 1
ContactQuerySearchFields_Email: ContactQuerySearchFields = 2
ContactQuerySearchFields_Phone: ContactQuerySearchFields = 4
ContactQuerySearchFields_All: ContactQuerySearchFields = 4294967295
ContactQuerySearchScope = Int32
ContactQuerySearchScope_Local: ContactQuerySearchScope = 0
ContactQuerySearchScope_Server: ContactQuerySearchScope = 1
class ContactQueryTextSearch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactQueryTextSearch
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactQueryTextSearch'
    @winrt_mixinmethod
    def get_Fields(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryTextSearch) -> win32more.Windows.ApplicationModel.Contacts.ContactQuerySearchFields: ...
    @winrt_mixinmethod
    def put_Fields(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryTextSearch, value: win32more.Windows.ApplicationModel.Contacts.ContactQuerySearchFields) -> Void: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryTextSearch) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryTextSearch, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SearchScope(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryTextSearch) -> win32more.Windows.ApplicationModel.Contacts.ContactQuerySearchScope: ...
    @winrt_mixinmethod
    def put_SearchScope(self: win32more.Windows.ApplicationModel.Contacts.IContactQueryTextSearch, value: win32more.Windows.ApplicationModel.Contacts.ContactQuerySearchScope) -> Void: ...
    Fields = property(get_Fields, put_Fields)
    Text = property(get_Text, put_Text)
    SearchScope = property(get_SearchScope, put_SearchScope)
class ContactReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactReader
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactBatch]: ...
    @winrt_mixinmethod
    def GetMatchingPropertiesWithMatchReason(self: win32more.Windows.ApplicationModel.Contacts.IContactReader, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactMatchReason]: ...
ContactRelationship = Int32
ContactRelationship_Other: ContactRelationship = 0
ContactRelationship_Spouse: ContactRelationship = 1
ContactRelationship_Partner: ContactRelationship = 2
ContactRelationship_Sibling: ContactRelationship = 3
ContactRelationship_Parent: ContactRelationship = 4
ContactRelationship_Child: ContactRelationship = 5
ContactSelectionMode = Int32
ContactSelectionMode_Contacts: ContactSelectionMode = 0
ContactSelectionMode_Fields: ContactSelectionMode = 1
class ContactSignificantOther(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactSignificantOther
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactSignificantOther'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactSignificantOther: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Contacts.IContactSignificantOther) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.ApplicationModel.Contacts.IContactSignificantOther, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactSignificantOther) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactSignificantOther, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Relationship(self: win32more.Windows.ApplicationModel.Contacts.IContactSignificantOther2) -> win32more.Windows.ApplicationModel.Contacts.ContactRelationship: ...
    @winrt_mixinmethod
    def put_Relationship(self: win32more.Windows.ApplicationModel.Contacts.IContactSignificantOther2, value: win32more.Windows.ApplicationModel.Contacts.ContactRelationship) -> Void: ...
    Name = property(get_Name, put_Name)
    Description = property(get_Description, put_Description)
    Relationship = property(get_Relationship, put_Relationship)
class ContactStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactStore
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactStore'
    @winrt_mixinmethod
    def FindContactsAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactStore) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.Contact]]: ...
    @winrt_mixinmethod
    def FindContactsWithSearchTextAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactStore, searchText: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.Contact]]: ...
    @winrt_mixinmethod
    def GetContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactStore, contactId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_mixinmethod
    def get_ChangeTracker(self: win32more.Windows.ApplicationModel.Contacts.IContactStore2) -> win32more.Windows.ApplicationModel.Contacts.ContactChangeTracker: ...
    @winrt_mixinmethod
    def add_ContactChanged(self: win32more.Windows.ApplicationModel.Contacts.IContactStore2, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.ContactStore, win32more.Windows.ApplicationModel.Contacts.ContactChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContactChanged(self: win32more.Windows.ApplicationModel.Contacts.IContactStore2, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AggregateContactManager(self: win32more.Windows.ApplicationModel.Contacts.IContactStore2) -> win32more.Windows.ApplicationModel.Contacts.AggregateContactManager: ...
    @winrt_mixinmethod
    def FindContactListsAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactStore2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactList]]: ...
    @winrt_mixinmethod
    def GetContactListAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactStore2, contactListId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactList]: ...
    @winrt_mixinmethod
    def CreateContactListAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactStore2, displayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactList]: ...
    @winrt_mixinmethod
    def GetMeContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactStore2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_mixinmethod
    def GetContactReader(self: win32more.Windows.ApplicationModel.Contacts.IContactStore2) -> win32more.Windows.ApplicationModel.Contacts.ContactReader: ...
    @winrt_mixinmethod
    def GetContactReaderWithOptions(self: win32more.Windows.ApplicationModel.Contacts.IContactStore2, options: win32more.Windows.ApplicationModel.Contacts.ContactQueryOptions) -> win32more.Windows.ApplicationModel.Contacts.ContactReader: ...
    @winrt_mixinmethod
    def CreateContactListInAccountAsync(self: win32more.Windows.ApplicationModel.Contacts.IContactStore2, displayName: WinRT_String, userDataAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactList]: ...
    @winrt_mixinmethod
    def GetChangeTracker(self: win32more.Windows.ApplicationModel.Contacts.IContactStore3, identity: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactChangeTracker: ...
    ChangeTracker = property(get_ChangeTracker, None)
    AggregateContactManager = property(get_AggregateContactManager, None)
ContactStoreAccessType = Int32
ContactStoreAccessType_AppContactsReadWrite: ContactStoreAccessType = 0
ContactStoreAccessType_AllContactsReadOnly: ContactStoreAccessType = 1
ContactStoreAccessType_AllContactsReadWrite: ContactStoreAccessType = 2
class ContactStoreNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactStoreNotificationTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactStoreNotificationTriggerDetails'
class ContactWebsite(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IContactWebsite
    _classid_ = 'Windows.ApplicationModel.Contacts.ContactWebsite'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.ContactWebsite: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.Contacts.IContactWebsite) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.ApplicationModel.Contacts.IContactWebsite, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactWebsite) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.Contacts.IContactWebsite, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RawValue(self: win32more.Windows.ApplicationModel.Contacts.IContactWebsite2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RawValue(self: win32more.Windows.ApplicationModel.Contacts.IContactWebsite2, value: WinRT_String) -> Void: ...
    Uri = property(get_Uri, put_Uri)
    Description = property(get_Description, put_Description)
    RawValue = property(get_RawValue, put_RawValue)
class FullContactCardOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IFullContactCardOptions
    _classid_ = 'Windows.ApplicationModel.Contacts.FullContactCardOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Contacts.FullContactCardOptions: ...
    @winrt_mixinmethod
    def get_DesiredRemainingView(self: win32more.Windows.ApplicationModel.Contacts.IFullContactCardOptions) -> win32more.Windows.UI.ViewManagement.ViewSizePreference: ...
    @winrt_mixinmethod
    def put_DesiredRemainingView(self: win32more.Windows.ApplicationModel.Contacts.IFullContactCardOptions, value: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> Void: ...
    DesiredRemainingView = property(get_DesiredRemainingView, put_DesiredRemainingView)
class IAggregateContactManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IAggregateContactManager'
    _iid_ = Guid('{0379d5dd-db5a-4fd3-b54e-4df17917a212}')
    @winrt_commethod(6)
    def FindRawContactsAsync(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.Contact]]: ...
    @winrt_commethod(7)
    def TryLinkContactsAsync(self, primaryContact: win32more.Windows.ApplicationModel.Contacts.Contact, secondaryContact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_commethod(8)
    def UnlinkRawContactAsync(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def TrySetPreferredSourceForPictureAsync(self, aggregateContact: win32more.Windows.ApplicationModel.Contacts.Contact, rawContact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IAggregateContactManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IAggregateContactManager2'
    _iid_ = Guid('{5e8cc2d8-a9cd-4430-9c4b-01348db2ca50}')
    @winrt_commethod(6)
    def SetRemoteIdentificationInformationAsync(self, contactListId: WinRT_String, remoteSourceId: WinRT_String, accountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IContact(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContact'
    _iid_ = Guid('{ec0072f3-2118-4049-9ebc-17f0ab692b64}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(9)
    def put_Thumbnail(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(10)
    def get_Fields(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.IContactField]: ...
    Name = property(get_Name, put_Name)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    Fields = property(get_Fields, None)
class IContact2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContact2'
    _iid_ = Guid('{f312f365-bb77-4c94-802d-8328cee40c08}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Notes(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Notes(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Phones(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactPhone]: ...
    @winrt_commethod(11)
    def get_Emails(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactEmail]: ...
    @winrt_commethod(12)
    def get_Addresses(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactAddress]: ...
    @winrt_commethod(13)
    def get_ConnectedServiceAccounts(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactConnectedServiceAccount]: ...
    @winrt_commethod(14)
    def get_ImportantDates(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactDate]: ...
    @winrt_commethod(15)
    def get_DataSuppliers(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(16)
    def get_JobInfo(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactJobInfo]: ...
    @winrt_commethod(17)
    def get_SignificantOthers(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactSignificantOther]: ...
    @winrt_commethod(18)
    def get_Websites(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactWebsite]: ...
    @winrt_commethod(19)
    def get_ProviderProperties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    Id = property(get_Id, put_Id)
    Notes = property(get_Notes, put_Notes)
    Phones = property(get_Phones, None)
    Emails = property(get_Emails, None)
    Addresses = property(get_Addresses, None)
    ConnectedServiceAccounts = property(get_ConnectedServiceAccounts, None)
    ImportantDates = property(get_ImportantDates, None)
    DataSuppliers = property(get_DataSuppliers, None)
    JobInfo = property(get_JobInfo, None)
    SignificantOthers = property(get_SignificantOthers, None)
    Websites = property(get_Websites, None)
    ProviderProperties = property(get_ProviderProperties, None)
class IContact3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContact3'
    _iid_ = Guid('{48201e67-e08e-42a4-b561-41d08ca9575d}')
    @winrt_commethod(6)
    def get_ContactListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayPictureUserUpdateTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def put_DisplayPictureUserUpdateTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(9)
    def get_IsMe(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_AggregateId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_RingToneToken(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_RingToneToken(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_IsDisplayPictureManuallySet(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_LargeDisplayPicture(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(17)
    def get_SmallDisplayPicture(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(18)
    def get_SourceDisplayPicture(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(19)
    def put_SourceDisplayPicture(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(20)
    def get_TextToneToken(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def put_TextToneToken(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(22)
    def get_IsAggregate(self) -> Boolean: ...
    @winrt_commethod(23)
    def get_FullName(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def get_DisplayNameOverride(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def put_DisplayNameOverride(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(26)
    def get_Nickname(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def put_Nickname(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(28)
    def get_SortName(self) -> WinRT_String: ...
    ContactListId = property(get_ContactListId, None)
    DisplayPictureUserUpdateTime = property(get_DisplayPictureUserUpdateTime, put_DisplayPictureUserUpdateTime)
    IsMe = property(get_IsMe, None)
    AggregateId = property(get_AggregateId, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
    RingToneToken = property(get_RingToneToken, put_RingToneToken)
    IsDisplayPictureManuallySet = property(get_IsDisplayPictureManuallySet, None)
    LargeDisplayPicture = property(get_LargeDisplayPicture, None)
    SmallDisplayPicture = property(get_SmallDisplayPicture, None)
    SourceDisplayPicture = property(get_SourceDisplayPicture, put_SourceDisplayPicture)
    TextToneToken = property(get_TextToneToken, put_TextToneToken)
    IsAggregate = property(get_IsAggregate, None)
    FullName = property(get_FullName, None)
    DisplayNameOverride = property(get_DisplayNameOverride, put_DisplayNameOverride)
    Nickname = property(get_Nickname, put_Nickname)
    SortName = property(get_SortName, None)
class IContactAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactAddress'
    _iid_ = Guid('{9739d39a-42ce-4872-8d70-3063aa584b70}')
    @winrt_commethod(6)
    def get_StreetAddress(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_StreetAddress(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Locality(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Locality(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Region(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Region(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Country(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_Country(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_PostalCode(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_PostalCode(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Contacts.ContactAddressKind: ...
    @winrt_commethod(17)
    def put_Kind(self, value: win32more.Windows.ApplicationModel.Contacts.ContactAddressKind) -> Void: ...
    @winrt_commethod(18)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def put_Description(self, value: WinRT_String) -> Void: ...
    StreetAddress = property(get_StreetAddress, put_StreetAddress)
    Locality = property(get_Locality, put_Locality)
    Region = property(get_Region, put_Region)
    Country = property(get_Country, put_Country)
    PostalCode = property(get_PostalCode, put_PostalCode)
    Kind = property(get_Kind, put_Kind)
    Description = property(get_Description, put_Description)
class IContactAnnotation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactAnnotation'
    _iid_ = Guid('{821fc2ef-7d41-44a2-84c3-60a281dd7b86}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AnnotationListId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ContactId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_ContactId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_SupportedOperations(self) -> win32more.Windows.ApplicationModel.Contacts.ContactAnnotationOperations: ...
    @winrt_commethod(13)
    def put_SupportedOperations(self, value: win32more.Windows.ApplicationModel.Contacts.ContactAnnotationOperations) -> Void: ...
    @winrt_commethod(14)
    def get_IsDisabled(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_ProviderProperties(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Id = property(get_Id, None)
    AnnotationListId = property(get_AnnotationListId, None)
    ContactId = property(get_ContactId, put_ContactId)
    RemoteId = property(get_RemoteId, put_RemoteId)
    SupportedOperations = property(get_SupportedOperations, put_SupportedOperations)
    IsDisabled = property(get_IsDisabled, None)
    ProviderProperties = property(get_ProviderProperties, None)
class IContactAnnotation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactAnnotation2'
    _iid_ = Guid('{b691ecf3-4ab7-4a1f-9941-0c9cf3171b75}')
    @winrt_commethod(6)
    def get_ContactListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ContactListId(self, value: WinRT_String) -> Void: ...
    ContactListId = property(get_ContactListId, put_ContactListId)
class IContactAnnotationList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactAnnotationList'
    _iid_ = Guid('{92a486aa-5c88-45b9-aad0-461888e68d8a}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ProviderPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_UserDataAccountId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def DeleteAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def TrySaveAnnotationAsync(self, annotation: win32more.Windows.ApplicationModel.Contacts.ContactAnnotation) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def GetAnnotationAsync(self, annotationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactAnnotation]: ...
    @winrt_commethod(12)
    def FindAnnotationsByRemoteIdAsync(self, remoteId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactAnnotation]]: ...
    @winrt_commethod(13)
    def FindAnnotationsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactAnnotation]]: ...
    @winrt_commethod(14)
    def DeleteAnnotationAsync(self, annotation: win32more.Windows.ApplicationModel.Contacts.ContactAnnotation) -> win32more.Windows.Foundation.IAsyncAction: ...
    Id = property(get_Id, None)
    ProviderPackageFamilyName = property(get_ProviderPackageFamilyName, None)
    UserDataAccountId = property(get_UserDataAccountId, None)
class IContactAnnotationStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactAnnotationStore'
    _iid_ = Guid('{23acf4aa-7a77-457d-8203-987f4b31af09}')
    @winrt_commethod(6)
    def FindContactIdsByEmailAsync(self, emailAddress: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(7)
    def FindContactIdsByPhoneNumberAsync(self, phoneNumber: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(8)
    def FindAnnotationsForContactAsync(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactAnnotation]]: ...
    @winrt_commethod(9)
    def DisableAnnotationAsync(self, annotation: win32more.Windows.ApplicationModel.Contacts.ContactAnnotation) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def CreateAnnotationListAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationList]: ...
    @winrt_commethod(11)
    def CreateAnnotationListInAccountAsync(self, userDataAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationList]: ...
    @winrt_commethod(12)
    def GetAnnotationListAsync(self, annotationListId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationList]: ...
    @winrt_commethod(13)
    def FindAnnotationListsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationList]]: ...
class IContactAnnotationStore2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactAnnotationStore2'
    _iid_ = Guid('{7ede23fd-61e7-4967-8ec5-bdf280a24063}')
    @winrt_commethod(6)
    def FindAnnotationsForContactListAsync(self, contactListId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactAnnotation]]: ...
class IContactBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactBatch'
    _iid_ = Guid('{35d1972d-bfce-46bb-93f8-a5b06ec5e201}')
    @winrt_commethod(6)
    def get_Contacts(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Contacts.ContactBatchStatus: ...
    Contacts = property(get_Contacts, None)
    Status = property(get_Status, None)
class IContactCardDelayedDataLoader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactCardDelayedDataLoader'
    _iid_ = Guid('{b60af902-1546-434d-869c-6e3520760ef3}')
    @winrt_commethod(6)
    def SetData(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> Void: ...
class IContactCardOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactCardOptions'
    _iid_ = Guid('{8c0a4f7e-6ab6-4f3f-be72-817236eeea5b}')
    @winrt_commethod(6)
    def get_HeaderKind(self) -> win32more.Windows.ApplicationModel.Contacts.ContactCardHeaderKind: ...
    @winrt_commethod(7)
    def put_HeaderKind(self, value: win32more.Windows.ApplicationModel.Contacts.ContactCardHeaderKind) -> Void: ...
    @winrt_commethod(8)
    def get_InitialTabKind(self) -> win32more.Windows.ApplicationModel.Contacts.ContactCardTabKind: ...
    @winrt_commethod(9)
    def put_InitialTabKind(self, value: win32more.Windows.ApplicationModel.Contacts.ContactCardTabKind) -> Void: ...
    HeaderKind = property(get_HeaderKind, put_HeaderKind)
    InitialTabKind = property(get_InitialTabKind, put_InitialTabKind)
class IContactCardOptions2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactCardOptions2'
    _iid_ = Guid('{8f271ba0-d74b-4cc6-9f53-1b0eb5d1273c}')
    @winrt_commethod(6)
    def get_ServerSearchContactListIds(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    ServerSearchContactListIds = property(get_ServerSearchContactListIds, None)
class IContactChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactChange'
    _iid_ = Guid('{951d4b10-6a59-4720-a4e1-363d98c135d5}')
    @winrt_commethod(6)
    def get_ChangeType(self) -> win32more.Windows.ApplicationModel.Contacts.ContactChangeType: ...
    @winrt_commethod(7)
    def get_Contact(self) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    ChangeType = property(get_ChangeType, None)
    Contact = property(get_Contact, None)
class IContactChangeReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactChangeReader'
    _iid_ = Guid('{217319fa-2d0c-42e0-a9da-3ecd56a78a47}')
    @winrt_commethod(6)
    def AcceptChanges(self) -> Void: ...
    @winrt_commethod(7)
    def AcceptChangesThrough(self, lastChangeToAccept: win32more.Windows.ApplicationModel.Contacts.ContactChange) -> Void: ...
    @winrt_commethod(8)
    def ReadBatchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactChange]]: ...
class IContactChangeTracker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactChangeTracker'
    _iid_ = Guid('{6e992952-309b-404d-9712-b37bd30278aa}')
    @winrt_commethod(6)
    def Enable(self) -> Void: ...
    @winrt_commethod(7)
    def GetChangeReader(self) -> win32more.Windows.ApplicationModel.Contacts.ContactChangeReader: ...
    @winrt_commethod(8)
    def Reset(self) -> Void: ...
class IContactChangeTracker2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactChangeTracker2'
    _iid_ = Guid('{7f8ad0fc-9321-4d18-9c09-d708c63fcd31}')
    @winrt_commethod(6)
    def get_IsTracking(self) -> Boolean: ...
    IsTracking = property(get_IsTracking, None)
class IContactChangedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactChangedDeferral'
    _iid_ = Guid('{c5143ae8-1b03-46f8-b694-a523e83cfcb6}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IContactChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactChangedEventArgs'
    _iid_ = Guid('{525e7fd1-73f3-4b7d-a918-580be4366121}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.Contacts.ContactChangedDeferral: ...
class IContactConnectedServiceAccount(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactConnectedServiceAccount'
    _iid_ = Guid('{f6f83553-aa27-4731-8e4a-3dec5ce9eec9}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ServiceName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_ServiceName(self, value: WinRT_String) -> Void: ...
    Id = property(get_Id, put_Id)
    ServiceName = property(get_ServiceName, put_ServiceName)
class IContactDate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactDate'
    _iid_ = Guid('{fe98ae66-b205-4934-9174-0ff2b0565707}')
    @winrt_commethod(6)
    def get_Day(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(7)
    def put_Day(self, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(8)
    def get_Month(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def put_Month(self, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(10)
    def get_Year(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(11)
    def put_Year(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(12)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Contacts.ContactDateKind: ...
    @winrt_commethod(13)
    def put_Kind(self, value: win32more.Windows.ApplicationModel.Contacts.ContactDateKind) -> Void: ...
    @winrt_commethod(14)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_Description(self, value: WinRT_String) -> Void: ...
    Day = property(get_Day, put_Day)
    Month = property(get_Month, put_Month)
    Year = property(get_Year, put_Year)
    Kind = property(get_Kind, put_Kind)
    Description = property(get_Description, put_Description)
class IContactEmail(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactEmail'
    _iid_ = Guid('{90a219a9-e3d3-4d63-993b-05b9a5393abf}')
    @winrt_commethod(6)
    def get_Address(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Address(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Contacts.ContactEmailKind: ...
    @winrt_commethod(9)
    def put_Kind(self, value: win32more.Windows.ApplicationModel.Contacts.ContactEmailKind) -> Void: ...
    @winrt_commethod(10)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Description(self, value: WinRT_String) -> Void: ...
    Address = property(get_Address, put_Address)
    Kind = property(get_Kind, put_Kind)
    Description = property(get_Description, put_Description)
class IContactField(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactField'
    _iid_ = Guid('{b176486a-d293-492c-a058-db575b3e3c0f}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.ApplicationModel.Contacts.ContactFieldType: ...
    @winrt_commethod(7)
    def get_Category(self) -> win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory: ...
    @winrt_commethod(8)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Value(self) -> WinRT_String: ...
    Type = property(get_Type, None)
    Category = property(get_Category, None)
    Name = property(get_Name, None)
    Value = property(get_Value, None)
class IContactFieldFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactFieldFactory'
    _iid_ = Guid('{85e2913f-0e4a-4a3e-8994-406ae7ed646e}')
    @winrt_commethod(6)
    def CreateField_Default(self, value: WinRT_String, type: win32more.Windows.ApplicationModel.Contacts.ContactFieldType) -> win32more.Windows.ApplicationModel.Contacts.ContactField: ...
    @winrt_commethod(7)
    def CreateField_Category(self, value: WinRT_String, type: win32more.Windows.ApplicationModel.Contacts.ContactFieldType, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory) -> win32more.Windows.ApplicationModel.Contacts.ContactField: ...
    @winrt_commethod(8)
    def CreateField_Custom(self, name: WinRT_String, value: WinRT_String, type: win32more.Windows.ApplicationModel.Contacts.ContactFieldType, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory) -> win32more.Windows.ApplicationModel.Contacts.ContactField: ...
class IContactGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactGroup'
    _iid_ = Guid('{59bdeb01-9e9a-475d-bfe5-a37b806d852c}')
class IContactInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactInformation'
    _iid_ = Guid('{275eb6d4-6a2e-4278-a914-e460d5f088f6}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetThumbnailAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
    @winrt_commethod(8)
    def get_Emails(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactField]: ...
    @winrt_commethod(9)
    def get_PhoneNumbers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactField]: ...
    @winrt_commethod(10)
    def get_Locations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactLocationField]: ...
    @winrt_commethod(11)
    def get_InstantMessages(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactInstantMessageField]: ...
    @winrt_commethod(12)
    def get_CustomFields(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactField]: ...
    @winrt_commethod(13)
    def QueryCustomFields(self, customName: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactField]: ...
    Name = property(get_Name, None)
    Emails = property(get_Emails, None)
    PhoneNumbers = property(get_PhoneNumbers, None)
    Locations = property(get_Locations, None)
    InstantMessages = property(get_InstantMessages, None)
    CustomFields = property(get_CustomFields, None)
class IContactInstantMessageField(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactInstantMessageField'
    _iid_ = Guid('{cce33b37-0d85-41fa-b43d-da599c3eb009}')
    @winrt_commethod(6)
    def get_UserName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Service(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DisplayText(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_LaunchUri(self) -> win32more.Windows.Foundation.Uri: ...
    UserName = property(get_UserName, None)
    Service = property(get_Service, None)
    DisplayText = property(get_DisplayText, None)
    LaunchUri = property(get_LaunchUri, None)
class IContactInstantMessageFieldFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactInstantMessageFieldFactory'
    _iid_ = Guid('{ba0b6794-91a3-4bb2-b1b9-69a5dff0ba09}')
    @winrt_commethod(6)
    def CreateInstantMessage_Default(self, userName: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactInstantMessageField: ...
    @winrt_commethod(7)
    def CreateInstantMessage_Category(self, userName: WinRT_String, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory) -> win32more.Windows.ApplicationModel.Contacts.ContactInstantMessageField: ...
    @winrt_commethod(8)
    def CreateInstantMessage_All(self, userName: WinRT_String, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory, service: WinRT_String, displayText: WinRT_String, verb: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Contacts.ContactInstantMessageField: ...
class IContactJobInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactJobInfo'
    _iid_ = Guid('{6d117b4c-ce50-4b43-9e69-b18258ea5315}')
    @winrt_commethod(6)
    def get_CompanyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_CompanyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_CompanyYomiName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_CompanyYomiName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Department(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Department(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Manager(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_Manager(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_Office(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_Office(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_CompanyAddress(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def put_CompanyAddress(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(20)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def put_Description(self, value: WinRT_String) -> Void: ...
    CompanyName = property(get_CompanyName, put_CompanyName)
    CompanyYomiName = property(get_CompanyYomiName, put_CompanyYomiName)
    Department = property(get_Department, put_Department)
    Title = property(get_Title, put_Title)
    Manager = property(get_Manager, put_Manager)
    Office = property(get_Office, put_Office)
    CompanyAddress = property(get_CompanyAddress, put_CompanyAddress)
    Description = property(get_Description, put_Description)
class IContactLaunchActionVerbsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactLaunchActionVerbsStatics'
    _iid_ = Guid('{fb1232d6-ee73-46e7-8761-11cd0157728f}')
    @winrt_commethod(6)
    def get_Call(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Map(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Post(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_VideoCall(self) -> WinRT_String: ...
    Call = property(get_Call, None)
    Message = property(get_Message, None)
    Map = property(get_Map, None)
    Post = property(get_Post, None)
    VideoCall = property(get_VideoCall, None)
class IContactList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactList'
    _iid_ = Guid('{16ddec75-392c-4845-9dfb-51a3e7ef3e42}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_SourceDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_IsHidden(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsHidden(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_OtherAppReadAccess(self) -> win32more.Windows.ApplicationModel.Contacts.ContactListOtherAppReadAccess: ...
    @winrt_commethod(13)
    def put_OtherAppReadAccess(self, value: win32more.Windows.ApplicationModel.Contacts.ContactListOtherAppReadAccess) -> Void: ...
    @winrt_commethod(14)
    def get_OtherAppWriteAccess(self) -> win32more.Windows.ApplicationModel.Contacts.ContactListOtherAppWriteAccess: ...
    @winrt_commethod(15)
    def put_OtherAppWriteAccess(self, value: win32more.Windows.ApplicationModel.Contacts.ContactListOtherAppWriteAccess) -> Void: ...
    @winrt_commethod(16)
    def get_ChangeTracker(self) -> win32more.Windows.ApplicationModel.Contacts.ContactChangeTracker: ...
    @winrt_commethod(17)
    def get_SyncManager(self) -> win32more.Windows.ApplicationModel.Contacts.ContactListSyncManager: ...
    @winrt_commethod(18)
    def get_SupportsServerSearch(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_UserDataAccountId(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def add_ContactChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.ContactList, win32more.Windows.ApplicationModel.Contacts.ContactChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_ContactChanged(self, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(23)
    def DeleteAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(24)
    def GetContactFromRemoteIdAsync(self, remoteId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_commethod(25)
    def GetMeContactAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_commethod(26)
    def GetContactReader(self) -> win32more.Windows.ApplicationModel.Contacts.ContactReader: ...
    @winrt_commethod(27)
    def GetContactReaderWithOptions(self, options: win32more.Windows.ApplicationModel.Contacts.ContactQueryOptions) -> win32more.Windows.ApplicationModel.Contacts.ContactReader: ...
    @winrt_commethod(28)
    def SaveContactAsync(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(29)
    def DeleteContactAsync(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(30)
    def GetContactAsync(self, contactId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    SourceDisplayName = property(get_SourceDisplayName, None)
    IsHidden = property(get_IsHidden, put_IsHidden)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    OtherAppWriteAccess = property(get_OtherAppWriteAccess, put_OtherAppWriteAccess)
    ChangeTracker = property(get_ChangeTracker, None)
    SyncManager = property(get_SyncManager, None)
    SupportsServerSearch = property(get_SupportsServerSearch, None)
    UserDataAccountId = property(get_UserDataAccountId, None)
class IContactList2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactList2'
    _iid_ = Guid('{cb3943b4-4550-4dcb-9229-40ff91fb0203}')
    @winrt_commethod(6)
    def RegisterSyncManagerAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def put_SupportsServerSearch(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_SyncConstraints(self) -> win32more.Windows.ApplicationModel.Contacts.ContactListSyncConstraints: ...
    SupportsServerSearch = property(None, put_SupportsServerSearch)
    SyncConstraints = property(get_SyncConstraints, None)
class IContactList3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactList3'
    _iid_ = Guid('{1578ee57-26fc-41e8-a850-5aa32514aca9}')
    @winrt_commethod(6)
    def get_LimitedWriteOperations(self) -> win32more.Windows.ApplicationModel.Contacts.ContactListLimitedWriteOperations: ...
    @winrt_commethod(7)
    def GetChangeTracker(self, identity: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactChangeTracker: ...
    LimitedWriteOperations = property(get_LimitedWriteOperations, None)
class IContactListLimitedWriteOperations(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactListLimitedWriteOperations'
    _iid_ = Guid('{e19813da-4a0b-44b8-9a1f-a0f3d218175f}')
    @winrt_commethod(6)
    def TryCreateOrUpdateContactAsync(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def TryDeleteContactAsync(self, contactId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IContactListSyncConstraints(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactListSyncConstraints'
    _iid_ = Guid('{b2b0bf01-3062-4e2e-969d-018d1987f314}')
    @winrt_commethod(6)
    def get_CanSyncDescriptions(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CanSyncDescriptions(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_MaxHomePhoneNumbers(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def put_MaxHomePhoneNumbers(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(10)
    def get_MaxMobilePhoneNumbers(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(11)
    def put_MaxMobilePhoneNumbers(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(12)
    def get_MaxWorkPhoneNumbers(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(13)
    def put_MaxWorkPhoneNumbers(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(14)
    def get_MaxOtherPhoneNumbers(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(15)
    def put_MaxOtherPhoneNumbers(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(16)
    def get_MaxPagerPhoneNumbers(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(17)
    def put_MaxPagerPhoneNumbers(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(18)
    def get_MaxBusinessFaxPhoneNumbers(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(19)
    def put_MaxBusinessFaxPhoneNumbers(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(20)
    def get_MaxHomeFaxPhoneNumbers(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(21)
    def put_MaxHomeFaxPhoneNumbers(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(22)
    def get_MaxCompanyPhoneNumbers(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(23)
    def put_MaxCompanyPhoneNumbers(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(24)
    def get_MaxAssistantPhoneNumbers(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(25)
    def put_MaxAssistantPhoneNumbers(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(26)
    def get_MaxRadioPhoneNumbers(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(27)
    def put_MaxRadioPhoneNumbers(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(28)
    def get_MaxPersonalEmailAddresses(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(29)
    def put_MaxPersonalEmailAddresses(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(30)
    def get_MaxWorkEmailAddresses(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(31)
    def put_MaxWorkEmailAddresses(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(32)
    def get_MaxOtherEmailAddresses(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(33)
    def put_MaxOtherEmailAddresses(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(34)
    def get_MaxHomeAddresses(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(35)
    def put_MaxHomeAddresses(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(36)
    def get_MaxWorkAddresses(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(37)
    def put_MaxWorkAddresses(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(38)
    def get_MaxOtherAddresses(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(39)
    def put_MaxOtherAddresses(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(40)
    def get_MaxBirthdayDates(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(41)
    def put_MaxBirthdayDates(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(42)
    def get_MaxAnniversaryDates(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(43)
    def put_MaxAnniversaryDates(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(44)
    def get_MaxOtherDates(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(45)
    def put_MaxOtherDates(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(46)
    def get_MaxOtherRelationships(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(47)
    def put_MaxOtherRelationships(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(48)
    def get_MaxSpouseRelationships(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(49)
    def put_MaxSpouseRelationships(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(50)
    def get_MaxPartnerRelationships(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(51)
    def put_MaxPartnerRelationships(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(52)
    def get_MaxSiblingRelationships(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(53)
    def put_MaxSiblingRelationships(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(54)
    def get_MaxParentRelationships(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(55)
    def put_MaxParentRelationships(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(56)
    def get_MaxChildRelationships(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(57)
    def put_MaxChildRelationships(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(58)
    def get_MaxJobInfo(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(59)
    def put_MaxJobInfo(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(60)
    def get_MaxWebsites(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(61)
    def put_MaxWebsites(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    CanSyncDescriptions = property(get_CanSyncDescriptions, put_CanSyncDescriptions)
    MaxHomePhoneNumbers = property(get_MaxHomePhoneNumbers, put_MaxHomePhoneNumbers)
    MaxMobilePhoneNumbers = property(get_MaxMobilePhoneNumbers, put_MaxMobilePhoneNumbers)
    MaxWorkPhoneNumbers = property(get_MaxWorkPhoneNumbers, put_MaxWorkPhoneNumbers)
    MaxOtherPhoneNumbers = property(get_MaxOtherPhoneNumbers, put_MaxOtherPhoneNumbers)
    MaxPagerPhoneNumbers = property(get_MaxPagerPhoneNumbers, put_MaxPagerPhoneNumbers)
    MaxBusinessFaxPhoneNumbers = property(get_MaxBusinessFaxPhoneNumbers, put_MaxBusinessFaxPhoneNumbers)
    MaxHomeFaxPhoneNumbers = property(get_MaxHomeFaxPhoneNumbers, put_MaxHomeFaxPhoneNumbers)
    MaxCompanyPhoneNumbers = property(get_MaxCompanyPhoneNumbers, put_MaxCompanyPhoneNumbers)
    MaxAssistantPhoneNumbers = property(get_MaxAssistantPhoneNumbers, put_MaxAssistantPhoneNumbers)
    MaxRadioPhoneNumbers = property(get_MaxRadioPhoneNumbers, put_MaxRadioPhoneNumbers)
    MaxPersonalEmailAddresses = property(get_MaxPersonalEmailAddresses, put_MaxPersonalEmailAddresses)
    MaxWorkEmailAddresses = property(get_MaxWorkEmailAddresses, put_MaxWorkEmailAddresses)
    MaxOtherEmailAddresses = property(get_MaxOtherEmailAddresses, put_MaxOtherEmailAddresses)
    MaxHomeAddresses = property(get_MaxHomeAddresses, put_MaxHomeAddresses)
    MaxWorkAddresses = property(get_MaxWorkAddresses, put_MaxWorkAddresses)
    MaxOtherAddresses = property(get_MaxOtherAddresses, put_MaxOtherAddresses)
    MaxBirthdayDates = property(get_MaxBirthdayDates, put_MaxBirthdayDates)
    MaxAnniversaryDates = property(get_MaxAnniversaryDates, put_MaxAnniversaryDates)
    MaxOtherDates = property(get_MaxOtherDates, put_MaxOtherDates)
    MaxOtherRelationships = property(get_MaxOtherRelationships, put_MaxOtherRelationships)
    MaxSpouseRelationships = property(get_MaxSpouseRelationships, put_MaxSpouseRelationships)
    MaxPartnerRelationships = property(get_MaxPartnerRelationships, put_MaxPartnerRelationships)
    MaxSiblingRelationships = property(get_MaxSiblingRelationships, put_MaxSiblingRelationships)
    MaxParentRelationships = property(get_MaxParentRelationships, put_MaxParentRelationships)
    MaxChildRelationships = property(get_MaxChildRelationships, put_MaxChildRelationships)
    MaxJobInfo = property(get_MaxJobInfo, put_MaxJobInfo)
    MaxWebsites = property(get_MaxWebsites, put_MaxWebsites)
class IContactListSyncManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactListSyncManager'
    _iid_ = Guid('{146e83be-7925-4acc-9de5-21ddd06f8674}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Contacts.ContactListSyncStatus: ...
    @winrt_commethod(7)
    def get_LastSuccessfulSyncTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_LastAttemptedSyncTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def SyncAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def add_SyncStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.ContactListSyncManager, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SyncStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
    LastSuccessfulSyncTime = property(get_LastSuccessfulSyncTime, None)
    LastAttemptedSyncTime = property(get_LastAttemptedSyncTime, None)
class IContactListSyncManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactListSyncManager2'
    _iid_ = Guid('{a9591247-bb55-4e23-8128-370134a85d0d}')
    @winrt_commethod(6)
    def put_Status(self, value: win32more.Windows.ApplicationModel.Contacts.ContactListSyncStatus) -> Void: ...
    @winrt_commethod(7)
    def put_LastSuccessfulSyncTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(8)
    def put_LastAttemptedSyncTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    Status = property(None, put_Status)
    LastSuccessfulSyncTime = property(None, put_LastSuccessfulSyncTime)
    LastAttemptedSyncTime = property(None, put_LastAttemptedSyncTime)
class IContactLocationField(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactLocationField'
    _iid_ = Guid('{9ec00f82-ab6e-4b36-89e3-b23bc0a1dacc}')
    @winrt_commethod(6)
    def get_UnstructuredAddress(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Street(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_City(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Region(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Country(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_PostalCode(self) -> WinRT_String: ...
    UnstructuredAddress = property(get_UnstructuredAddress, None)
    Street = property(get_Street, None)
    City = property(get_City, None)
    Region = property(get_Region, None)
    Country = property(get_Country, None)
    PostalCode = property(get_PostalCode, None)
class IContactLocationFieldFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactLocationFieldFactory'
    _iid_ = Guid('{f79932d7-2fdf-43fe-8f18-41897390bcfe}')
    @winrt_commethod(6)
    def CreateLocation_Default(self, unstructuredAddress: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactLocationField: ...
    @winrt_commethod(7)
    def CreateLocation_Category(self, unstructuredAddress: WinRT_String, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory) -> win32more.Windows.ApplicationModel.Contacts.ContactLocationField: ...
    @winrt_commethod(8)
    def CreateLocation_All(self, unstructuredAddress: WinRT_String, category: win32more.Windows.ApplicationModel.Contacts.ContactFieldCategory, street: WinRT_String, city: WinRT_String, region: WinRT_String, country: WinRT_String, postalCode: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactLocationField: ...
class IContactManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactManagerForUser'
    _iid_ = Guid('{b74bba57-1076-4bef-aef3-54686d18387d}')
    @winrt_commethod(6)
    def ConvertContactToVCardAsync(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_commethod(7)
    def ConvertContactToVCardAsyncWithMaxBytes(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact, maxBytes: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_commethod(8)
    def ConvertVCardToContactAsync(self, vCard: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_commethod(9)
    def RequestStoreAsync(self, accessType: win32more.Windows.ApplicationModel.Contacts.ContactStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactStore]: ...
    @winrt_commethod(10)
    def RequestAnnotationStoreAsync(self, accessType: win32more.Windows.ApplicationModel.Contacts.ContactAnnotationStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationStore]: ...
    @winrt_commethod(11)
    def get_SystemDisplayNameOrder(self) -> win32more.Windows.ApplicationModel.Contacts.ContactNameOrder: ...
    @winrt_commethod(12)
    def put_SystemDisplayNameOrder(self, value: win32more.Windows.ApplicationModel.Contacts.ContactNameOrder) -> Void: ...
    @winrt_commethod(13)
    def get_SystemSortOrder(self) -> win32more.Windows.ApplicationModel.Contacts.ContactNameOrder: ...
    @winrt_commethod(14)
    def put_SystemSortOrder(self, value: win32more.Windows.ApplicationModel.Contacts.ContactNameOrder) -> Void: ...
    @winrt_commethod(15)
    def get_User(self) -> win32more.Windows.System.User: ...
    SystemDisplayNameOrder = property(get_SystemDisplayNameOrder, put_SystemDisplayNameOrder)
    SystemSortOrder = property(get_SystemSortOrder, put_SystemSortOrder)
    User = property(get_User, None)
class IContactManagerForUser2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactManagerForUser2'
    _iid_ = Guid('{4d469c2e-3b75-4a73-bb30-736645472256}')
    @winrt_commethod(6)
    def ShowFullContactCard(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact, fullContactCardOptions: win32more.Windows.ApplicationModel.Contacts.FullContactCardOptions) -> Void: ...
class IContactManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactManagerStatics'
    _iid_ = Guid('{81f21ac0-f661-4708-ba4f-d386bd0d622e}')
    @winrt_commethod(6)
    def ShowContactCard(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact, selection: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(7)
    def ShowContactCardWithPlacement(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> Void: ...
    @winrt_commethod(8)
    def ShowDelayLoadedContactCard(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.ApplicationModel.Contacts.ContactCardDelayedDataLoader: ...
class IContactManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactManagerStatics2'
    _iid_ = Guid('{a178e620-47d8-48cc-963c-9592b6e510c6}')
    @winrt_commethod(6)
    def RequestStoreAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactStore]: ...
class IContactManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactManagerStatics3'
    _iid_ = Guid('{c4cc3d42-7586-492a-930b-7bc138fc2139}')
    @winrt_commethod(6)
    def ConvertContactToVCardAsync(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_commethod(7)
    def ConvertContactToVCardAsyncWithMaxBytes(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact, maxBytes: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_commethod(8)
    def ConvertVCardToContactAsync(self, vCard: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_commethod(9)
    def RequestStoreAsyncWithAccessType(self, accessType: win32more.Windows.ApplicationModel.Contacts.ContactStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactStore]: ...
    @winrt_commethod(10)
    def RequestAnnotationStoreAsync(self, accessType: win32more.Windows.ApplicationModel.Contacts.ContactAnnotationStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationStore]: ...
    @winrt_commethod(11)
    def IsShowContactCardSupported(self) -> Boolean: ...
    @winrt_commethod(12)
    def ShowContactCardWithOptions(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement, contactCardOptions: win32more.Windows.ApplicationModel.Contacts.ContactCardOptions) -> Void: ...
    @winrt_commethod(13)
    def IsShowDelayLoadedContactCardSupported(self) -> Boolean: ...
    @winrt_commethod(14)
    def ShowDelayLoadedContactCardWithOptions(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement, contactCardOptions: win32more.Windows.ApplicationModel.Contacts.ContactCardOptions) -> win32more.Windows.ApplicationModel.Contacts.ContactCardDelayedDataLoader: ...
    @winrt_commethod(15)
    def ShowFullContactCard(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact, fullContactCardOptions: win32more.Windows.ApplicationModel.Contacts.FullContactCardOptions) -> Void: ...
    @winrt_commethod(16)
    def get_SystemDisplayNameOrder(self) -> win32more.Windows.ApplicationModel.Contacts.ContactNameOrder: ...
    @winrt_commethod(17)
    def put_SystemDisplayNameOrder(self, value: win32more.Windows.ApplicationModel.Contacts.ContactNameOrder) -> Void: ...
    @winrt_commethod(18)
    def get_SystemSortOrder(self) -> win32more.Windows.ApplicationModel.Contacts.ContactNameOrder: ...
    @winrt_commethod(19)
    def put_SystemSortOrder(self, value: win32more.Windows.ApplicationModel.Contacts.ContactNameOrder) -> Void: ...
    SystemDisplayNameOrder = property(get_SystemDisplayNameOrder, put_SystemDisplayNameOrder)
    SystemSortOrder = property(get_SystemSortOrder, put_SystemSortOrder)
class IContactManagerStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactManagerStatics4'
    _iid_ = Guid('{24982272-347b-46dc-8d95-51bd41e15aaf}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.Contacts.ContactManagerForUser: ...
class IContactManagerStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactManagerStatics5'
    _iid_ = Guid('{f7591a87-acb7-4fad-90f2-a8ab64cdbba4}')
    @winrt_commethod(6)
    def IsShowFullContactCardSupportedAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def get_IncludeMiddleNameInSystemDisplayAndSort(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IncludeMiddleNameInSystemDisplayAndSort(self, value: Boolean) -> Void: ...
    IncludeMiddleNameInSystemDisplayAndSort = property(get_IncludeMiddleNameInSystemDisplayAndSort, put_IncludeMiddleNameInSystemDisplayAndSort)
class IContactMatchReason(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactMatchReason'
    _iid_ = Guid('{bc922504-e7d8-413e-95f4-b75c54c74077}')
    @winrt_commethod(6)
    def get_Field(self) -> win32more.Windows.ApplicationModel.Contacts.ContactMatchReasonKind: ...
    @winrt_commethod(7)
    def get_Segments(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.TextSegment]: ...
    @winrt_commethod(8)
    def get_Text(self) -> WinRT_String: ...
    Field = property(get_Field, None)
    Segments = property(get_Segments, None)
    Text = property(get_Text, None)
class IContactName(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactName'
    _iid_ = Guid('{f404e97b-9034-453c-8ebf-140a38c86f1d}')
    @winrt_commethod(6)
    def get_FirstName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_FirstName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_LastName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_LastName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_MiddleName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_MiddleName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_YomiGivenName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_YomiGivenName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_YomiFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_YomiFamilyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_HonorificNameSuffix(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_HonorificNameSuffix(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_HonorificNamePrefix(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def put_HonorificNamePrefix(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(20)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_YomiDisplayName(self) -> WinRT_String: ...
    FirstName = property(get_FirstName, put_FirstName)
    LastName = property(get_LastName, put_LastName)
    MiddleName = property(get_MiddleName, put_MiddleName)
    YomiGivenName = property(get_YomiGivenName, put_YomiGivenName)
    YomiFamilyName = property(get_YomiFamilyName, put_YomiFamilyName)
    HonorificNameSuffix = property(get_HonorificNameSuffix, put_HonorificNameSuffix)
    HonorificNamePrefix = property(get_HonorificNamePrefix, put_HonorificNamePrefix)
    DisplayName = property(get_DisplayName, None)
    YomiDisplayName = property(get_YomiDisplayName, None)
class IContactPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactPanel'
    _iid_ = Guid('{41bf1265-d2ee-4b97-a80a-7d8d64cca6f5}')
    @winrt_commethod(6)
    def ClosePanel(self) -> Void: ...
    @winrt_commethod(7)
    def get_HeaderColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(8)
    def put_HeaderColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(9)
    def add_LaunchFullAppRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.ContactPanel, win32more.Windows.ApplicationModel.Contacts.ContactPanelLaunchFullAppRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_LaunchFullAppRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Closing(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.ContactPanel, win32more.Windows.ApplicationModel.Contacts.ContactPanelClosingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Closing(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    HeaderColor = property(get_HeaderColor, put_HeaderColor)
class IContactPanelClosingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactPanelClosingEventArgs'
    _iid_ = Guid('{222174d3-cf4b-46d7-b739-6edc16110bfb}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class IContactPanelLaunchFullAppRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactPanelLaunchFullAppRequestedEventArgs'
    _iid_ = Guid('{88d61c0e-23b4-4be8-8afc-072c25a4190d}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class IContactPhone(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactPhone'
    _iid_ = Guid('{467dab65-2712-4f52-b783-9ea8111c63cd}')
    @winrt_commethod(6)
    def get_Number(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Number(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Contacts.ContactPhoneKind: ...
    @winrt_commethod(9)
    def put_Kind(self, value: win32more.Windows.ApplicationModel.Contacts.ContactPhoneKind) -> Void: ...
    @winrt_commethod(10)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Description(self, value: WinRT_String) -> Void: ...
    Number = property(get_Number, put_Number)
    Kind = property(get_Kind, put_Kind)
    Description = property(get_Description, put_Description)
class IContactPicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactPicker'
    _iid_ = Guid('{0e09fd91-42f8-4055-90a0-896f96738936}')
    @winrt_commethod(6)
    def get_CommitButtonText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_CommitButtonText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_SelectionMode(self) -> win32more.Windows.ApplicationModel.Contacts.ContactSelectionMode: ...
    @winrt_commethod(9)
    def put_SelectionMode(self, value: win32more.Windows.ApplicationModel.Contacts.ContactSelectionMode) -> Void: ...
    @winrt_commethod(10)
    def get_DesiredFields(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(11)
    def PickSingleContactAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactInformation]: ...
    @winrt_commethod(12)
    def PickMultipleContactsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactInformation]]: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    SelectionMode = property(get_SelectionMode, put_SelectionMode)
    DesiredFields = property(get_DesiredFields, None)
class IContactPicker2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactPicker2'
    _iid_ = Guid('{b35011cf-5cef-4d24-aa0c-340c5208725d}')
    @winrt_commethod(6)
    def get_DesiredFieldsWithContactFieldType(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactFieldType]: ...
    @winrt_commethod(7)
    def PickContactAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_commethod(8)
    def PickContactsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.Contact]]: ...
    DesiredFieldsWithContactFieldType = property(get_DesiredFieldsWithContactFieldType, None)
class IContactPicker3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactPicker3'
    _iid_ = Guid('{0e723315-b243-4bed-8516-22b1a7ac0ace}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IContactPickerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactPickerStatics'
    _iid_ = Guid('{7488c029-6a53-4258-a3e9-62dff6784b6c}')
    @winrt_commethod(6)
    def CreateForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.Contacts.ContactPicker: ...
    @winrt_commethod(7)
    def IsSupportedAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IContactQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactQueryOptions'
    _iid_ = Guid('{4408cc9e-7d7c-42f0-8ac7-f50733ecdbc1}')
    @winrt_commethod(6)
    def get_TextSearch(self) -> win32more.Windows.ApplicationModel.Contacts.ContactQueryTextSearch: ...
    @winrt_commethod(7)
    def get_ContactListIds(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(8)
    def get_IncludeContactsFromHiddenLists(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IncludeContactsFromHiddenLists(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_DesiredFields(self) -> win32more.Windows.ApplicationModel.Contacts.ContactQueryDesiredFields: ...
    @winrt_commethod(11)
    def put_DesiredFields(self, value: win32more.Windows.ApplicationModel.Contacts.ContactQueryDesiredFields) -> Void: ...
    @winrt_commethod(12)
    def get_DesiredOperations(self) -> win32more.Windows.ApplicationModel.Contacts.ContactAnnotationOperations: ...
    @winrt_commethod(13)
    def put_DesiredOperations(self, value: win32more.Windows.ApplicationModel.Contacts.ContactAnnotationOperations) -> Void: ...
    @winrt_commethod(14)
    def get_AnnotationListIds(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    TextSearch = property(get_TextSearch, None)
    ContactListIds = property(get_ContactListIds, None)
    IncludeContactsFromHiddenLists = property(get_IncludeContactsFromHiddenLists, put_IncludeContactsFromHiddenLists)
    DesiredFields = property(get_DesiredFields, put_DesiredFields)
    DesiredOperations = property(get_DesiredOperations, put_DesiredOperations)
    AnnotationListIds = property(get_AnnotationListIds, None)
class IContactQueryOptionsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactQueryOptionsFactory'
    _iid_ = Guid('{543fba47-8ce7-46cb-9dac-9aa42a1bc8e2}')
    @winrt_commethod(6)
    def CreateWithText(self, text: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactQueryOptions: ...
    @winrt_commethod(7)
    def CreateWithTextAndFields(self, text: WinRT_String, fields: win32more.Windows.ApplicationModel.Contacts.ContactQuerySearchFields) -> win32more.Windows.ApplicationModel.Contacts.ContactQueryOptions: ...
class IContactQueryTextSearch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactQueryTextSearch'
    _iid_ = Guid('{f7e3f9cb-a957-439b-a0b7-1c02a1963ff0}')
    @winrt_commethod(6)
    def get_Fields(self) -> win32more.Windows.ApplicationModel.Contacts.ContactQuerySearchFields: ...
    @winrt_commethod(7)
    def put_Fields(self, value: win32more.Windows.ApplicationModel.Contacts.ContactQuerySearchFields) -> Void: ...
    @winrt_commethod(8)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_SearchScope(self) -> win32more.Windows.ApplicationModel.Contacts.ContactQuerySearchScope: ...
    @winrt_commethod(11)
    def put_SearchScope(self, value: win32more.Windows.ApplicationModel.Contacts.ContactQuerySearchScope) -> Void: ...
    Fields = property(get_Fields, put_Fields)
    Text = property(get_Text, put_Text)
    SearchScope = property(get_SearchScope, put_SearchScope)
class IContactReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactReader'
    _iid_ = Guid('{d397e42e-1488-42f2-bf64-253f4884bfed}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactBatch]: ...
    @winrt_commethod(7)
    def GetMatchingPropertiesWithMatchReason(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactMatchReason]: ...
class IContactSignificantOther(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactSignificantOther'
    _iid_ = Guid('{8873b5ab-c5fb-46d8-93fe-da3ff1934054}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)
    Description = property(get_Description, put_Description)
class IContactSignificantOther2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactSignificantOther2'
    _iid_ = Guid('{8d7bd474-3f03-45f8-ba0f-c4ed37d64219}')
    @winrt_commethod(6)
    def get_Relationship(self) -> win32more.Windows.ApplicationModel.Contacts.ContactRelationship: ...
    @winrt_commethod(7)
    def put_Relationship(self, value: win32more.Windows.ApplicationModel.Contacts.ContactRelationship) -> Void: ...
    Relationship = property(get_Relationship, put_Relationship)
class IContactStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactStore'
    _iid_ = Guid('{2c220b10-3a6c-4293-b9bc-fe987f6e0d52}')
    @winrt_commethod(6)
    def FindContactsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.Contact]]: ...
    @winrt_commethod(7)
    def FindContactsWithSearchTextAsync(self, searchText: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.Contact]]: ...
    @winrt_commethod(8)
    def GetContactAsync(self, contactId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
class IContactStore2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactStore2'
    _iid_ = Guid('{18ce1c22-ebd5-4bfb-b690-5f4f27c4f0e8}')
    @winrt_commethod(6)
    def get_ChangeTracker(self) -> win32more.Windows.ApplicationModel.Contacts.ContactChangeTracker: ...
    @winrt_commethod(7)
    def add_ContactChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.ContactStore, win32more.Windows.ApplicationModel.Contacts.ContactChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_ContactChanged(self, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def get_AggregateContactManager(self) -> win32more.Windows.ApplicationModel.Contacts.AggregateContactManager: ...
    @winrt_commethod(10)
    def FindContactListsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactList]]: ...
    @winrt_commethod(11)
    def GetContactListAsync(self, contactListId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactList]: ...
    @winrt_commethod(12)
    def CreateContactListAsync(self, displayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactList]: ...
    @winrt_commethod(13)
    def GetMeContactAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    @winrt_commethod(14)
    def GetContactReader(self) -> win32more.Windows.ApplicationModel.Contacts.ContactReader: ...
    @winrt_commethod(15)
    def GetContactReaderWithOptions(self, options: win32more.Windows.ApplicationModel.Contacts.ContactQueryOptions) -> win32more.Windows.ApplicationModel.Contacts.ContactReader: ...
    @winrt_commethod(16)
    def CreateContactListInAccountAsync(self, displayName: WinRT_String, userDataAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.ContactList]: ...
    ChangeTracker = property(get_ChangeTracker, None)
    AggregateContactManager = property(get_AggregateContactManager, None)
class IContactStore3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactStore3'
    _iid_ = Guid('{cb882c6c-004e-4050-87f0-840407ee6818}')
    @winrt_commethod(6)
    def GetChangeTracker(self, identity: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactChangeTracker: ...
class IContactStoreNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactStoreNotificationTriggerDetails'
    _iid_ = Guid('{abb298d6-878a-4f8b-a9ce-46bb7d1c84ce}')
class IContactWebsite(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactWebsite'
    _iid_ = Guid('{9f130176-dc1b-4055-ad66-652f39d990e8}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_Uri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
    Uri = property(get_Uri, put_Uri)
    Description = property(get_Description, put_Description)
class IContactWebsite2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IContactWebsite2'
    _iid_ = Guid('{f87ee91e-5647-4068-bb5e-4b6f437ce308}')
    @winrt_commethod(6)
    def get_RawValue(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_RawValue(self, value: WinRT_String) -> Void: ...
    RawValue = property(get_RawValue, put_RawValue)
class IFullContactCardOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IFullContactCardOptions'
    _iid_ = Guid('{8744436c-5cf9-4683-bdca-a1fdebf8dbce}')
    @winrt_commethod(6)
    def get_DesiredRemainingView(self) -> win32more.Windows.UI.ViewManagement.ViewSizePreference: ...
    @winrt_commethod(7)
    def put_DesiredRemainingView(self, value: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> Void: ...
    DesiredRemainingView = property(get_DesiredRemainingView, put_DesiredRemainingView)
class IKnownContactFieldStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IKnownContactFieldStatics'
    _iid_ = Guid('{2e0e1b12-d627-4fca-bad4-1faf168c7d14}')
    @winrt_commethod(6)
    def get_Email(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_PhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Location(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_InstantMessage(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def ConvertNameToType(self, name: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactFieldType: ...
    @winrt_commethod(11)
    def ConvertTypeToName(self, type: win32more.Windows.ApplicationModel.Contacts.ContactFieldType) -> WinRT_String: ...
    Email = property(get_Email, None)
    PhoneNumber = property(get_PhoneNumber, None)
    Location = property(get_Location, None)
    InstantMessage = property(get_InstantMessage, None)
class IPinnedContactIdsQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IPinnedContactIdsQueryResult'
    _iid_ = Guid('{7d9b2552-1579-4ddc-871f-a30a3aea9ba1}')
    @winrt_commethod(6)
    def get_ContactIds(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    ContactIds = property(get_ContactIds, None)
class IPinnedContactManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IPinnedContactManager'
    _iid_ = Guid('{fcbc740c-e1d6-45c3-b8b6-a35604e167a0}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(7)
    def IsPinSurfaceSupported(self, surface: win32more.Windows.ApplicationModel.Contacts.PinnedContactSurface) -> Boolean: ...
    @winrt_commethod(8)
    def IsContactPinned(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact, surface: win32more.Windows.ApplicationModel.Contacts.PinnedContactSurface) -> Boolean: ...
    @winrt_commethod(9)
    def RequestPinContactAsync(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact, surface: win32more.Windows.ApplicationModel.Contacts.PinnedContactSurface) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def RequestPinContactsAsync(self, contacts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Contacts.Contact], surface: win32more.Windows.ApplicationModel.Contacts.PinnedContactSurface) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def RequestUnpinContactAsync(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact, surface: win32more.Windows.ApplicationModel.Contacts.PinnedContactSurface) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(12)
    def SignalContactActivity(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> Void: ...
    @winrt_commethod(13)
    def GetPinnedContactIdsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.PinnedContactIdsQueryResult]: ...
    User = property(get_User, None)
class IPinnedContactManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.IPinnedContactManagerStatics'
    _iid_ = Guid('{f65ccc7e-fdf9-486a-ace9-bc311d0ae7f0}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.ApplicationModel.Contacts.PinnedContactManager: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.Contacts.PinnedContactManager: ...
    @winrt_commethod(8)
    def IsSupported(self) -> Boolean: ...
class _KnownContactField_Meta_(ComPtr.__class__):
    pass
class KnownContactField(ComPtr, metaclass=_KnownContactField_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.KnownContactField'
    @winrt_classmethod
    def get_Email(cls: win32more.Windows.ApplicationModel.Contacts.IKnownContactFieldStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PhoneNumber(cls: win32more.Windows.ApplicationModel.Contacts.IKnownContactFieldStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Location(cls: win32more.Windows.ApplicationModel.Contacts.IKnownContactFieldStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_InstantMessage(cls: win32more.Windows.ApplicationModel.Contacts.IKnownContactFieldStatics) -> WinRT_String: ...
    @winrt_classmethod
    def ConvertNameToType(cls: win32more.Windows.ApplicationModel.Contacts.IKnownContactFieldStatics, name: WinRT_String) -> win32more.Windows.ApplicationModel.Contacts.ContactFieldType: ...
    @winrt_classmethod
    def ConvertTypeToName(cls: win32more.Windows.ApplicationModel.Contacts.IKnownContactFieldStatics, type: win32more.Windows.ApplicationModel.Contacts.ContactFieldType) -> WinRT_String: ...
    _KnownContactField_Meta_.Email = property(get_Email.__wrapped__, None)
    _KnownContactField_Meta_.PhoneNumber = property(get_PhoneNumber.__wrapped__, None)
    _KnownContactField_Meta_.Location = property(get_Location.__wrapped__, None)
    _KnownContactField_Meta_.InstantMessage = property(get_InstantMessage.__wrapped__, None)
class PinnedContactIdsQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IPinnedContactIdsQueryResult
    _classid_ = 'Windows.ApplicationModel.Contacts.PinnedContactIdsQueryResult'
    @winrt_mixinmethod
    def get_ContactIds(self: win32more.Windows.ApplicationModel.Contacts.IPinnedContactIdsQueryResult) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    ContactIds = property(get_ContactIds, None)
class PinnedContactManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.IPinnedContactManager
    _classid_ = 'Windows.ApplicationModel.Contacts.PinnedContactManager'
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Contacts.IPinnedContactManager) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def IsPinSurfaceSupported(self: win32more.Windows.ApplicationModel.Contacts.IPinnedContactManager, surface: win32more.Windows.ApplicationModel.Contacts.PinnedContactSurface) -> Boolean: ...
    @winrt_mixinmethod
    def IsContactPinned(self: win32more.Windows.ApplicationModel.Contacts.IPinnedContactManager, contact: win32more.Windows.ApplicationModel.Contacts.Contact, surface: win32more.Windows.ApplicationModel.Contacts.PinnedContactSurface) -> Boolean: ...
    @winrt_mixinmethod
    def RequestPinContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IPinnedContactManager, contact: win32more.Windows.ApplicationModel.Contacts.Contact, surface: win32more.Windows.ApplicationModel.Contacts.PinnedContactSurface) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPinContactsAsync(self: win32more.Windows.ApplicationModel.Contacts.IPinnedContactManager, contacts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Contacts.Contact], surface: win32more.Windows.ApplicationModel.Contacts.PinnedContactSurface) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestUnpinContactAsync(self: win32more.Windows.ApplicationModel.Contacts.IPinnedContactManager, contact: win32more.Windows.ApplicationModel.Contacts.Contact, surface: win32more.Windows.ApplicationModel.Contacts.PinnedContactSurface) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SignalContactActivity(self: win32more.Windows.ApplicationModel.Contacts.IPinnedContactManager, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> Void: ...
    @winrt_mixinmethod
    def GetPinnedContactIdsAsync(self: win32more.Windows.ApplicationModel.Contacts.IPinnedContactManager) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Contacts.PinnedContactIdsQueryResult]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.ApplicationModel.Contacts.IPinnedContactManagerStatics) -> win32more.Windows.ApplicationModel.Contacts.PinnedContactManager: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.ApplicationModel.Contacts.IPinnedContactManagerStatics, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.Contacts.PinnedContactManager: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.ApplicationModel.Contacts.IPinnedContactManagerStatics) -> Boolean: ...
    User = property(get_User, None)
PinnedContactSurface = Int32
PinnedContactSurface_StartMenu: PinnedContactSurface = 0
PinnedContactSurface_Taskbar: PinnedContactSurface = 1
make_head(_module, 'AggregateContactManager')
make_head(_module, 'Contact')
make_head(_module, 'ContactAddress')
make_head(_module, 'ContactAnnotation')
make_head(_module, 'ContactAnnotationList')
make_head(_module, 'ContactAnnotationStore')
make_head(_module, 'ContactBatch')
make_head(_module, 'ContactCardDelayedDataLoader')
make_head(_module, 'ContactCardOptions')
make_head(_module, 'ContactChange')
make_head(_module, 'ContactChangeReader')
make_head(_module, 'ContactChangeTracker')
make_head(_module, 'ContactChangedDeferral')
make_head(_module, 'ContactChangedEventArgs')
make_head(_module, 'ContactConnectedServiceAccount')
make_head(_module, 'ContactDate')
make_head(_module, 'ContactEmail')
make_head(_module, 'ContactField')
make_head(_module, 'ContactFieldFactory')
make_head(_module, 'ContactGroup')
make_head(_module, 'ContactInformation')
make_head(_module, 'ContactInstantMessageField')
make_head(_module, 'ContactJobInfo')
make_head(_module, 'ContactLaunchActionVerbs')
make_head(_module, 'ContactList')
make_head(_module, 'ContactListLimitedWriteOperations')
make_head(_module, 'ContactListSyncConstraints')
make_head(_module, 'ContactListSyncManager')
make_head(_module, 'ContactLocationField')
make_head(_module, 'ContactManager')
make_head(_module, 'ContactManagerForUser')
make_head(_module, 'ContactMatchReason')
make_head(_module, 'ContactPanel')
make_head(_module, 'ContactPanelClosingEventArgs')
make_head(_module, 'ContactPanelLaunchFullAppRequestedEventArgs')
make_head(_module, 'ContactPhone')
make_head(_module, 'ContactPicker')
make_head(_module, 'ContactQueryOptions')
make_head(_module, 'ContactQueryTextSearch')
make_head(_module, 'ContactReader')
make_head(_module, 'ContactSignificantOther')
make_head(_module, 'ContactStore')
make_head(_module, 'ContactStoreNotificationTriggerDetails')
make_head(_module, 'ContactWebsite')
make_head(_module, 'FullContactCardOptions')
make_head(_module, 'IAggregateContactManager')
make_head(_module, 'IAggregateContactManager2')
make_head(_module, 'IContact')
make_head(_module, 'IContact2')
make_head(_module, 'IContact3')
make_head(_module, 'IContactAddress')
make_head(_module, 'IContactAnnotation')
make_head(_module, 'IContactAnnotation2')
make_head(_module, 'IContactAnnotationList')
make_head(_module, 'IContactAnnotationStore')
make_head(_module, 'IContactAnnotationStore2')
make_head(_module, 'IContactBatch')
make_head(_module, 'IContactCardDelayedDataLoader')
make_head(_module, 'IContactCardOptions')
make_head(_module, 'IContactCardOptions2')
make_head(_module, 'IContactChange')
make_head(_module, 'IContactChangeReader')
make_head(_module, 'IContactChangeTracker')
make_head(_module, 'IContactChangeTracker2')
make_head(_module, 'IContactChangedDeferral')
make_head(_module, 'IContactChangedEventArgs')
make_head(_module, 'IContactConnectedServiceAccount')
make_head(_module, 'IContactDate')
make_head(_module, 'IContactEmail')
make_head(_module, 'IContactField')
make_head(_module, 'IContactFieldFactory')
make_head(_module, 'IContactGroup')
make_head(_module, 'IContactInformation')
make_head(_module, 'IContactInstantMessageField')
make_head(_module, 'IContactInstantMessageFieldFactory')
make_head(_module, 'IContactJobInfo')
make_head(_module, 'IContactLaunchActionVerbsStatics')
make_head(_module, 'IContactList')
make_head(_module, 'IContactList2')
make_head(_module, 'IContactList3')
make_head(_module, 'IContactListLimitedWriteOperations')
make_head(_module, 'IContactListSyncConstraints')
make_head(_module, 'IContactListSyncManager')
make_head(_module, 'IContactListSyncManager2')
make_head(_module, 'IContactLocationField')
make_head(_module, 'IContactLocationFieldFactory')
make_head(_module, 'IContactManagerForUser')
make_head(_module, 'IContactManagerForUser2')
make_head(_module, 'IContactManagerStatics')
make_head(_module, 'IContactManagerStatics2')
make_head(_module, 'IContactManagerStatics3')
make_head(_module, 'IContactManagerStatics4')
make_head(_module, 'IContactManagerStatics5')
make_head(_module, 'IContactMatchReason')
make_head(_module, 'IContactName')
make_head(_module, 'IContactPanel')
make_head(_module, 'IContactPanelClosingEventArgs')
make_head(_module, 'IContactPanelLaunchFullAppRequestedEventArgs')
make_head(_module, 'IContactPhone')
make_head(_module, 'IContactPicker')
make_head(_module, 'IContactPicker2')
make_head(_module, 'IContactPicker3')
make_head(_module, 'IContactPickerStatics')
make_head(_module, 'IContactQueryOptions')
make_head(_module, 'IContactQueryOptionsFactory')
make_head(_module, 'IContactQueryTextSearch')
make_head(_module, 'IContactReader')
make_head(_module, 'IContactSignificantOther')
make_head(_module, 'IContactSignificantOther2')
make_head(_module, 'IContactStore')
make_head(_module, 'IContactStore2')
make_head(_module, 'IContactStore3')
make_head(_module, 'IContactStoreNotificationTriggerDetails')
make_head(_module, 'IContactWebsite')
make_head(_module, 'IContactWebsite2')
make_head(_module, 'IFullContactCardOptions')
make_head(_module, 'IKnownContactFieldStatics')
make_head(_module, 'IPinnedContactIdsQueryResult')
make_head(_module, 'IPinnedContactManager')
make_head(_module, 'IPinnedContactManagerStatics')
make_head(_module, 'KnownContactField')
make_head(_module, 'PinnedContactIdsQueryResult')
make_head(_module, 'PinnedContactManager')
