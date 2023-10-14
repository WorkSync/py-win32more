from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Contacts
CGD_DEFAULT: UInt32 = 0
CGD_UNKNOWN_PROPERTY: UInt32 = 0
CGD_STRING_PROPERTY: UInt32 = 1
CGD_DATE_PROPERTY: UInt32 = 2
CGD_BINARY_PROPERTY: UInt32 = 4
CGD_ARRAY_NODE: UInt32 = 8
CLSID_ContactAggregationManager: Guid = Guid('{96c8ad95-c199-44de-b34e-ac33c442df39}')
CONTACTPROP_PUB_NOTES: String = 'Notes'
CONTACTPROP_PUB_MAILER: String = 'Mailer'
CONTACTPROP_PUB_PROGID: String = 'ProgID'
CONTACTPROP_PUB_GENDER: String = 'Gender'
CONTACTPROP_PUB_GENDER_UNSPECIFIED: String = 'Unspecified'
CONTACTPROP_PUB_GENDER_MALE: String = 'Male'
CONTACTPROP_PUB_GENDER_FEMALE: String = 'Female'
CONTACTPROP_PUB_CREATIONDATE: String = 'CreationDate'
CONTACTPROP_PUB_L1_CONTACTIDCOLLECTION: String = 'ContactIDCollection'
CONTACTPROP_PUB_L2_CONTACTID: String = '/ContactID'
CONTACTPROP_PUB_L3_VALUE: String = '/Value'
CONTACTPROP_PUB_L1_NAMECOLLECTION: String = 'NameCollection'
CONTACTPROP_PUB_L2_NAME: String = '/Name'
CONTACTPROP_PUB_L3_FORMATTEDNAME: String = '/FormattedName'
CONTACTPROP_PUB_L3_PHONETIC: String = '/Phonetic'
CONTACTPROP_PUB_L3_PREFIX: String = '/Prefix'
CONTACTPROP_PUB_L3_TITLE: String = '/Title'
CONTACTPROP_PUB_L3_GIVENNAME: String = '/GivenName'
CONTACTPROP_PUB_L3_FAMILYNAME: String = '/FamilyName'
CONTACTPROP_PUB_L3_MIDDLENAME: String = '/MiddleName'
CONTACTPROP_PUB_L3_GENERATION: String = '/Generation'
CONTACTPROP_PUB_L3_SUFFIX: String = '/Suffix'
CONTACTPROP_PUB_L3_NICKNAME: String = '/NickName'
CONTACTPROP_PUB_L1_POSITIONCOLLECTION: String = 'PositionCollection'
CONTACTPROP_PUB_L2_POSITION: String = '/Position'
CONTACTPROP_PUB_L3_ORGANIZATION: String = '/Organization'
CONTACTPROP_PUB_L3_COMPANY: String = '/Company'
CONTACTPROP_PUB_L3_DEPARTMENT: String = '/Department'
CONTACTPROP_PUB_L3_OFFICE: String = '/Office'
CONTACTPROP_PUB_L3_JOB_TITLE: String = '/JobTitle'
CONTACTPROP_PUB_L3_PROFESSION: String = '/Profession'
CONTACTPROP_PUB_L3_ROLE: String = '/Role'
CONTACTPROP_PUB_L1_PERSONCOLLECTION: String = 'PersonCollection'
CONTACTPROP_PUB_L2_PERSON: String = '/Person'
CONTACTPROP_PUB_L3_PERSONID: String = '/PersonID'
CONTACTPROP_PUB_L1_DATECOLLECTION: String = 'DateCollection'
CONTACTPROP_PUB_L2_DATE: String = '/Date'
CONTACTPROP_PUB_L1_EMAILADDRESSCOLLECTION: String = 'EmailAddressCollection'
CONTACTPROP_PUB_L2_EMAILADDRESS: String = '/EmailAddress'
CONTACTPROP_PUB_L3_ADDRESS: String = '/Address'
CONTACTPROP_PUB_L3_TYPE: String = '/Type'
CONTACTPROP_PUB_L1_CERTIFICATECOLLECTION: String = 'CertificateCollection'
CONTACTPROP_PUB_L2_CERTIFICATE: String = '/Certificate'
CONTACTPROP_PUB_L3_THUMBPRINT: String = '/ThumbPrint'
CONTACTPROP_PUB_L1_PHONENUMBERCOLLECTION: String = 'PhoneNumberCollection'
CONTACTPROP_PUB_L2_PHONENUMBER: String = '/PhoneNumber'
CONTACTPROP_PUB_L3_NUMBER: String = '/Number'
CONTACTPROP_PUB_L3_ALTERNATE: String = '/Alternate'
CONTACTPROP_PUB_L1_PHYSICALADDRESSCOLLECTION: String = 'PhysicalAddressCollection'
CONTACTPROP_PUB_L2_PHYSICALADDRESS: String = '/PhysicalAddress'
CONTACTPROP_PUB_L3_ADDRESSLABEL: String = '/AddressLabel'
CONTACTPROP_PUB_L3_STREET: String = '/Street'
CONTACTPROP_PUB_L3_LOCALITY: String = '/Locality'
CONTACTPROP_PUB_L3_REGION: String = '/Region'
CONTACTPROP_PUB_L3_POSTALCODE: String = '/PostalCode'
CONTACTPROP_PUB_L3_COUNTRY: String = '/Country'
CONTACTPROP_PUB_L3_POBOX: String = '/POBox'
CONTACTPROP_PUB_L3_EXTENDEDADDRESS: String = '/ExtendedAddress'
CONTACTPROP_PUB_L1_IMADDRESSCOLLECTION: String = 'IMAddressCollection'
CONTACTPROP_PUB_L2_IMADDRESSENTRY: String = '/IMAddress'
CONTACTPROP_PUB_L3_PROTOCOL: String = '/Protocol'
CONTACTPROP_PUB_L1_URLCOLLECTION: String = 'UrlCollection'
CONTACTPROP_PUB_L2_URL: String = '/Url'
CONTACTPROP_PUB_L1_PHOTOCOLLECTION: String = 'PhotoCollection'
CONTACTPROP_PUB_L2_PHOTO: String = '/Photo'
CONTACTPROP_PUB_L3_URL: String = '/Url'
CONTACTLABEL_PUB_PREFERRED: String = 'Preferred'
CONTACTLABEL_PUB_PERSONAL: String = 'Personal'
CONTACTLABEL_PUB_BUSINESS: String = 'Business'
CONTACTLABEL_PUB_OTHER: String = 'Other'
CONTACTLABEL_PUB_VOICE: String = 'Voice'
CONTACTLABEL_PUB_MOBILE: String = 'Mobile'
CONTACTLABEL_PUB_PCS: String = 'PCS'
CONTACTLABEL_PUB_CELLULAR: String = 'Cellular'
CONTACTLABEL_PUB_CAR: String = 'Car'
CONTACTLABEL_PUB_PAGER: String = 'Pager'
CONTACTLABEL_PUB_TTY: String = 'TTY'
CONTACTLABEL_PUB_FAX: String = 'Fax'
CONTACTLABEL_PUB_VIDEO: String = 'Video'
CONTACTLABEL_PUB_MODEM: String = 'Modem'
CONTACTLABEL_PUB_BBS: String = 'BBS'
CONTACTLABEL_PUB_ISDN: String = 'ISDN'
CONTACTLABEL_PUB_AGENT: String = 'Agent'
CONTACTLABEL_PUB_DOMESTIC: String = 'Domestic'
CONTACTLABEL_PUB_INTERNATIONAL: String = 'International'
CONTACTLABEL_PUB_POSTAL: String = 'Postal'
CONTACTLABEL_PUB_PARCEL: String = 'Parcel'
CONTACTLABEL_PUB_USERTILE: String = 'UserTile'
CONTACTLABEL_PUB_LOGO: String = 'Logo'
CONTACTLABEL_WAB_SPOUSE: String = 'wab:Spouse'
CONTACTLABEL_WAB_CHILD: String = 'wab:Child'
CONTACTLABEL_WAB_MANAGER: String = 'wab:Manager'
CONTACTLABEL_WAB_ASSISTANT: String = 'wab:Assistant'
CONTACTLABEL_WAB_BIRTHDAY: String = 'wab:Birthday'
CONTACTLABEL_WAB_ANNIVERSARY: String = 'wab:Anniversary'
CONTACTLABEL_WAB_SOCIALNETWORK: String = 'wab:SocialNetwork'
CONTACTLABEL_WAB_SCHOOL: String = 'wab:School'
CONTACTLABEL_WAB_WISHLIST: String = 'wab:WishList'
class CONTACT_AGGREGATION_BLOB(EasyCastStructure):
    dwCount: UInt32
    lpb: POINTER(Byte)
CONTACT_AGGREGATION_COLLECTION_OPTIONS = Int32
CACO_DEFAULT: CONTACT_AGGREGATION_COLLECTION_OPTIONS = 0
CACO_INCLUDE_EXTERNAL: CONTACT_AGGREGATION_COLLECTION_OPTIONS = 1
CACO_EXTERNAL_ONLY: CONTACT_AGGREGATION_COLLECTION_OPTIONS = 2
CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS = Int32
CA_CREATE_LOCAL: CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS = 0
CA_CREATE_EXTERNAL: CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS = 1
Contact = Guid('{61b68808-8eee-4fd1-acb8-3d804c8db056}')
ContactManager = Guid('{7165c8ab-af88-42bd-86fd-5310b4285a02}')
class IContact(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f941b671-bda7-4f77-884a-f46462f226a7}')
    @commethod(3)
    def GetContactID(self, pszContactID: win32more.Windows.Win32.Foundation.PWSTR, cchContactID: UInt32, pdwcchContactIDRequired: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPath(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UInt32, pdwcchPathRequired: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CommitChanges(self, dwCommitFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationAggregate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7ed1c814-cd30-43c8-9b8d-2e489e53d54b}')
    @commethod(3)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetComponentItems(self, pComponentItems: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationContactCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Link(self, pAggregateId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Groups(self, options: win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS, ppGroups: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationGroupCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_AntiLink(self, ppAntiLink: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AntiLink(self, pAntiLink: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FavoriteOrder(self, pFavoriteOrder: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_FavoriteOrder(self, favoriteOrder: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Id(self, ppItemId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationAggregateCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2359f3a6-3a68-40af-98db-0f9eb143c3bb}')
    @commethod(3)
    def FindFirst(self, ppAggregate: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationAggregate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindFirstByAntiLinkId(self, pAntiLinkId: win32more.Windows.Win32.Foundation.PWSTR, ppAggregate: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationAggregate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindNext(self, ppAggregate: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationAggregate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationContact(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1eb22e86-4c86-41f0-9f9f-c251e9fda6c3}')
    @commethod(3)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveToAggregate(self, pAggregateId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unlink(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_AccountId(self, ppAccountId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AccountId(self, pAccountId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AggregateId(self, ppAggregateId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Id(self, ppItemId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsMe(self, pIsMe: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsExternal(self, pIsExternal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_NetworkSourceId(self, pNetworkSourceId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_NetworkSourceId(self, networkSourceId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_NetworkSourceIdString(self, ppNetworkSourceId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_NetworkSourceIdString(self, pNetworkSourceId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RemoteObjectId(self, ppRemoteObjectId: POINTER(POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_RemoteObjectId(self, pRemoteObjectId: POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SyncIdentityHash(self, ppSyncIdentityHash: POINTER(POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_SyncIdentityHash(self, pSyncIdentityHash: POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationContactCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{826e66fa-81de-43ca-a6fb-8c785cd996c6}')
    @commethod(3)
    def FindFirst(self, ppItem: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationContact)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindNext(self, ppItem: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationContact)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindFirstByIdentityHash(self, pSourceType: win32more.Windows.Win32.Foundation.PWSTR, pAccountId: win32more.Windows.Win32.Foundation.PWSTR, pIdentityHash: POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB), ppItem: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationContact)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindFirstByRemoteId(self, pSourceType: win32more.Windows.Win32.Foundation.PWSTR, pAccountId: win32more.Windows.Win32.Foundation.PWSTR, pRemoteObjectId: POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB), ppItem: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationContact)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationGroup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c93c545f-1284-499b-96af-07372af473e0}')
    @commethod(3)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, pAggregateId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Remove(self, pAggregateId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Members(self, ppAggregateContactCollection: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationAggregateCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_GlobalObjectId(self, pGlobalObjectId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_GlobalObjectId(self, pGlobalObjectId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Id(self, ppItemId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Name(self, ppName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Name(self, pName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationGroupCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{20a19a9c-d2f3-4b83-9143-beffd2cc226d}')
    @commethod(3)
    def FindFirst(self, ppGroup: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindFirstByGlobalObjectId(self, pGlobalObjectId: POINTER(Guid), ppGroup: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindNext(self, ppGroup: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationLink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b6813323-a183-4654-8627-79b30de3a0ec}')
    @commethod(3)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_AccountId(self, ppAccountId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_AccountId(self, pAccountId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Id(self, ppItemId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IsLinkResolved(self, pIsLinkResolved: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_IsLinkResolved(self, isLinkResolved: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NetworkSourceIdString(self, ppNetworkSourceId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_NetworkSourceIdString(self, pNetworkSourceId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_RemoteObjectId(self, ppRemoteObjectId: POINTER(POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_RemoteObjectId(self, pRemoteObjectId: POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ServerPerson(self, ppServerPersonId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_ServerPerson(self, pServerPersonId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ServerPersonBaseline(self, ppServerPersonId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_ServerPersonBaseline(self, pServerPersonId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_SyncIdentityHash(self, ppSyncIdentityHash: POINTER(POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_SyncIdentityHash(self, pSyncIdentityHash: POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationLinkCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f8bc0e93-fb55-4f28-b9fa-b1c274153292}')
    @commethod(3)
    def FindFirst(self, ppServerContactLink: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationLink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindFirstByRemoteId(self, pSourceType: win32more.Windows.Win32.Foundation.PWSTR, pAccountId: win32more.Windows.Win32.Foundation.PWSTR, pRemoteId: POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB), ppServerContactLink: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationLink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindNext(self, ppServerContactLink: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationLink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1d865989-4b1f-4b60-8f34-c2ad468b2b50}')
    @commethod(3)
    def GetVersionInfo(self, plMajorVersion: POINTER(Int32), plMinorVersion: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateOrOpenGroup(self, pGroupName: win32more.Windows.Win32.Foundation.PWSTR, options: win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS, pCreatedGroup: POINTER(win32more.Windows.Win32.Foundation.BOOL), ppGroup: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateExternalContact(self, ppItem: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationContact)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateServerPerson(self, ppServerPerson: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationServerPerson)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateServerContactLink(self, ppServerContactLink: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationLink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Flush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OpenAggregateContact(self, pItemId: win32more.Windows.Win32.Foundation.PWSTR, ppItem: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationAggregate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OpenContact(self, pItemId: win32more.Windows.Win32.Foundation.PWSTR, ppItem: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationContact)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OpenServerContactLink(self, pItemId: win32more.Windows.Win32.Foundation.PWSTR, ppItem: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationLink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OpenServerPerson(self, pItemId: win32more.Windows.Win32.Foundation.PWSTR, ppItem: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationServerPerson)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Contacts(self, options: win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS, ppItems: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationContactCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AggregateContacts(self, options: win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS, ppAggregates: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationAggregateCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Groups(self, options: win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS, ppGroups: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationGroupCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ServerPersons(self, ppServerPersonCollection: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationServerPersonCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ServerContactLinks(self, pPersonItemId: win32more.Windows.Win32.Foundation.PWSTR, ppServerContactLinkCollection: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationLinkCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationServerPerson(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7fdc3d4b-1b82-4334-85c5-25184ee5a5f2}')
    @commethod(3)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_AggregateId(self, ppAggregateId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_AggregateId(self, pAggregateId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_AntiLink(self, ppAntiLink: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AntiLink(self, pAntiLink: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AntiLinkBaseline(self, ppAntiLink: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_AntiLinkBaseline(self, pAntiLink: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_FavoriteOrder(self, pFavoriteOrder: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_FavoriteOrder(self, favoriteOrder: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_FavoriteOrderBaseline(self, pFavoriteOrder: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_FavoriteOrderBaseline(self, favoriteOrder: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Groups(self, pGroups: POINTER(POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Groups(self, pGroups: POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_GroupsBaseline(self, ppGroups: POINTER(POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_GroupsBaseline(self, pGroups: POINTER(win32more.Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Id(self, ppId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_IsTombstone(self, pIsTombstone: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_IsTombstone(self, isTombstone: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_LinkedAggregateId(self, ppLinkedAggregateId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_LinkedAggregateId(self, pLinkedAggregateId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_ObjectId(self, ppObjectId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_ObjectId(self, pObjectId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationServerPersonCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4f730a4a-6604-47b6-a987-669ecf1e5751}')
    @commethod(3)
    def FindFirst(self, ppServerPerson: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationServerPerson)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindFirstByServerId(self, pServerId: win32more.Windows.Win32.Foundation.PWSTR, ppServerPerson: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationServerPerson)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindFirstByAggregateId(self, pAggregateId: win32more.Windows.Win32.Foundation.PWSTR, ppServerPerson: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationServerPerson)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindFirstByLinkedAggregateId(self, pAggregateId: win32more.Windows.Win32.Foundation.PWSTR, ppServerPerson: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationServerPerson)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindNext(self, ppServerPerson: POINTER(win32more.Windows.Win32.System.Contacts.IContactAggregationServerPerson)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b6afa338-d779-11d9-8bde-f66bad1e3f3a}')
    @commethod(3)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(self, ppContact: POINTER(win32more.Windows.Win32.System.Contacts.IContact)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ad553d98-deb1-474a-8e17-fc0c2075b738}')
    @commethod(3)
    def Initialize(self, pszAppName: win32more.Windows.Win32.Foundation.PWSTR, pszAppVersion: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Load(self, pszContactID: win32more.Windows.Win32.Foundation.PWSTR, ppContact: POINTER(win32more.Windows.Win32.System.Contacts.IContact)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MergeContactIDs(self, pszNewContactID: win32more.Windows.Win32.Foundation.PWSTR, pszOldContactID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMeContact(self, ppMeContact: POINTER(win32more.Windows.Win32.System.Contacts.IContact)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetMeContact(self, pMeContact: win32more.Windows.Win32.System.Contacts.IContact) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetContactCollection(self, ppContactCollection: POINTER(win32more.Windows.Win32.System.Contacts.IContactCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{70dd27dd-5cbd-46e8-bef0-23b6b346288f}')
    @commethod(3)
    def GetString(self, pszPropertyName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pszValue: win32more.Windows.Win32.Foundation.PWSTR, cchValue: UInt32, pdwcchPropertyValueRequired: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDate(self, pszPropertyName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pftDateTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBinary(self, pszPropertyName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pszContentType: win32more.Windows.Win32.Foundation.PWSTR, cchContentType: UInt32, pdwcchContentTypeRequired: POINTER(UInt32), ppStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLabels(self, pszArrayElementName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pszLabels: win32more.Windows.Win32.Foundation.PWSTR, cchLabels: UInt32, pdwcchLabelsRequired: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetString(self, pszPropertyName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pszValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDate(self, pszPropertyName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ftDateTime: win32more.Windows.Win32.Foundation.FILETIME) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetBinary(self, pszPropertyName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pszContentType: win32more.Windows.Win32.Foundation.PWSTR, pStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetLabels(self, pszArrayElementName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwLabelCount: UInt32, ppszLabels: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateArrayNode(self, pszArrayName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, fAppend: win32more.Windows.Win32.Foundation.BOOL, pszNewArrayElementName: win32more.Windows.Win32.Foundation.PWSTR, cchNewArrayElementName: UInt32, pdwcchNewArrayElementNameRequired: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeleteProperty(self, pszPropertyName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteArrayNode(self, pszArrayElementName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def DeleteLabels(self, pszArrayElementName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetPropertyCollection(self, ppPropertyCollection: POINTER(win32more.Windows.Win32.System.Contacts.IContactPropertyCollection), dwFlags: UInt32, pszMultiValueName: win32more.Windows.Win32.Foundation.PWSTR, dwLabelCount: UInt32, ppszLabels: POINTER(win32more.Windows.Win32.Foundation.PWSTR), fAnyLabelMatches: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactPropertyCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ffd3adf8-fa64-4328-b1b6-2e0db509cb3c}')
    @commethod(3)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyName(self, pszPropertyName: win32more.Windows.Win32.Foundation.PWSTR, cchPropertyName: UInt32, pdwcchPropertyNameRequired: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyType(self, pdwType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPropertyVersion(self, pdwVersion: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPropertyModificationDate(self, pftModificationDate: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPropertyArrayElementID(self, pszArrayElementID: win32more.Windows.Win32.Foundation.PWSTR, cchArrayElementID: UInt32, pdwcchArrayElementIDRequired: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_ready(__name__)
