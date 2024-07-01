from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, FillArray, Generic, K, MulticastDelegate, PassArray, ReceiveArray, T, TProgress, TResult, TSender, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.AccessCache
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
class AccessCacheOptions(Enum, UInt32):
    None_ = 0
    DisallowUserInput = 1
    FastLocationsOnly = 2
    UseReadOnlyCachedCopy = 4
    SuppressAccessTimeUpdate = 8
class AccessListEntry(Structure):
    Token: WinRT_String
    Metadata: WinRT_String
class AccessListEntryView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.AccessCache.AccessListEntry]
    _classid_ = 'Windows.Storage.AccessCache.AccessListEntryView'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.AccessCache.AccessListEntry], index: UInt32) -> win32more.Windows.Storage.AccessCache.AccessListEntry: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.AccessCache.AccessListEntry]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.AccessCache.AccessListEntry], value: win32more.Windows.Storage.AccessCache.AccessListEntry, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.AccessCache.AccessListEntry], startIndex: UInt32, items: FillArray[win32more.Windows.Storage.AccessCache.AccessListEntry]) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.AccessCache.AccessListEntry]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Storage.AccessCache.AccessListEntry]: ...
    Size = property(get_Size, None)
class IItemRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.IItemRemovedEventArgs'
    _iid_ = Guid('{59677e5c-55be-4c66-ba66-5eaea79d2631}')
    @winrt_commethod(6)
    def get_RemovedEntry(self) -> win32more.Windows.Storage.AccessCache.AccessListEntry: ...
    RemovedEntry = property(get_RemovedEntry, None)
class IStorageApplicationPermissionsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.IStorageApplicationPermissionsStatics'
    _iid_ = Guid('{4391dfaa-d033-48f9-8060-3ec847d2e3f1}')
    @winrt_commethod(6)
    def get_FutureAccessList(self) -> win32more.Windows.Storage.AccessCache.StorageItemAccessList: ...
    @winrt_commethod(7)
    def get_MostRecentlyUsedList(self) -> win32more.Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList: ...
    FutureAccessList = property(get_FutureAccessList, None)
    MostRecentlyUsedList = property(get_MostRecentlyUsedList, None)
class IStorageApplicationPermissionsStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.IStorageApplicationPermissionsStatics2'
    _iid_ = Guid('{072716ec-aa05-4294-9a11-1a3d04519ad0}')
    @winrt_commethod(6)
    def GetFutureAccessListForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Storage.AccessCache.StorageItemAccessList: ...
    @winrt_commethod(7)
    def GetMostRecentlyUsedListForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList: ...
class IStorageItemAccessList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.IStorageItemAccessList'
    _iid_ = Guid('{2caff6ad-de90-47f5-b2c3-dd36c9fdd453}')
    @winrt_commethod(6)
    def AddOverloadDefaultMetadata(self, file: win32more.Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_commethod(7)
    def Add(self, file: win32more.Windows.Storage.IStorageItem, metadata: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(8)
    def AddOrReplaceOverloadDefaultMetadata(self, token: WinRT_String, file: win32more.Windows.Storage.IStorageItem) -> Void: ...
    @winrt_commethod(9)
    def AddOrReplace(self, token: WinRT_String, file: win32more.Windows.Storage.IStorageItem, metadata: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def GetItemAsync(self, token: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_commethod(11)
    def GetFileAsync(self, token: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(12)
    def GetFolderAsync(self, token: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_commethod(13)
    def GetItemWithOptionsAsync(self, token: WinRT_String, options: win32more.Windows.Storage.AccessCache.AccessCacheOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_commethod(14)
    def GetFileWithOptionsAsync(self, token: WinRT_String, options: win32more.Windows.Storage.AccessCache.AccessCacheOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(15)
    def GetFolderWithOptionsAsync(self, token: WinRT_String, options: win32more.Windows.Storage.AccessCache.AccessCacheOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_commethod(16)
    def Remove(self, token: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def ContainsItem(self, token: WinRT_String) -> Boolean: ...
    @winrt_commethod(18)
    def Clear(self) -> Void: ...
    @winrt_commethod(19)
    def CheckAccess(self, file: win32more.Windows.Storage.IStorageItem) -> Boolean: ...
    @winrt_commethod(20)
    def get_Entries(self) -> win32more.Windows.Storage.AccessCache.AccessListEntryView: ...
    @winrt_commethod(21)
    def get_MaximumItemsAllowed(self) -> UInt32: ...
    Entries = property(get_Entries, None)
    MaximumItemsAllowed = property(get_MaximumItemsAllowed, None)
class IStorageItemMostRecentlyUsedList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList'
    _iid_ = Guid('{016239d5-510d-411e-8cf1-c3d1effa4c33}')
    @winrt_commethod(6)
    def add_ItemRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList, win32more.Windows.Storage.AccessCache.ItemRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ItemRemoved(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ItemRemoved = event()
class IStorageItemMostRecentlyUsedList2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList2'
    _iid_ = Guid('{da481ea0-ed8d-4731-a1db-e44ee2204093}')
    @winrt_commethod(6)
    def AddWithMetadataAndVisibility(self, file: win32more.Windows.Storage.IStorageItem, metadata: WinRT_String, visibility: win32more.Windows.Storage.AccessCache.RecentStorageItemVisibility) -> WinRT_String: ...
    @winrt_commethod(7)
    def AddOrReplaceWithMetadataAndVisibility(self, token: WinRT_String, file: win32more.Windows.Storage.IStorageItem, metadata: WinRT_String, visibility: win32more.Windows.Storage.AccessCache.RecentStorageItemVisibility) -> Void: ...
class ItemRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.AccessCache.IItemRemovedEventArgs
    _classid_ = 'Windows.Storage.AccessCache.ItemRemovedEventArgs'
    @winrt_mixinmethod
    def get_RemovedEntry(self: win32more.Windows.Storage.AccessCache.IItemRemovedEventArgs) -> win32more.Windows.Storage.AccessCache.AccessListEntry: ...
    RemovedEntry = property(get_RemovedEntry, None)
class RecentStorageItemVisibility(Enum, Int32):
    AppOnly = 0
    AppAndSystem = 1
class _StorageApplicationPermissions_Meta_(ComPtr.__class__):
    pass
class StorageApplicationPermissions(ComPtr, metaclass=_StorageApplicationPermissions_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.StorageApplicationPermissions'
    @winrt_classmethod
    def GetFutureAccessListForUser(cls: win32more.Windows.Storage.AccessCache.IStorageApplicationPermissionsStatics2, user: win32more.Windows.System.User) -> win32more.Windows.Storage.AccessCache.StorageItemAccessList: ...
    @winrt_classmethod
    def GetMostRecentlyUsedListForUser(cls: win32more.Windows.Storage.AccessCache.IStorageApplicationPermissionsStatics2, user: win32more.Windows.System.User) -> win32more.Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList: ...
    @winrt_classmethod
    def get_FutureAccessList(cls: win32more.Windows.Storage.AccessCache.IStorageApplicationPermissionsStatics) -> win32more.Windows.Storage.AccessCache.StorageItemAccessList: ...
    @winrt_classmethod
    def get_MostRecentlyUsedList(cls: win32more.Windows.Storage.AccessCache.IStorageApplicationPermissionsStatics) -> win32more.Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList: ...
    _StorageApplicationPermissions_Meta_.FutureAccessList = property(get_FutureAccessList, None)
    _StorageApplicationPermissions_Meta_.MostRecentlyUsedList = property(get_MostRecentlyUsedList, None)
class StorageItemAccessList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.AccessCache.IStorageItemAccessList
    _classid_ = 'Windows.Storage.AccessCache.StorageItemAccessList'
    @winrt_mixinmethod
    def AddOverloadDefaultMetadata(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, file: win32more.Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def Add(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, file: win32more.Windows.Storage.IStorageItem, metadata: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def AddOrReplaceOverloadDefaultMetadata(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, file: win32more.Windows.Storage.IStorageItem) -> Void: ...
    @winrt_mixinmethod
    def AddOrReplace(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, file: win32more.Windows.Storage.IStorageItem, metadata: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetItemAsync(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def GetFileAsync(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetFolderAsync(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def GetItemWithOptionsAsync(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, options: win32more.Windows.Storage.AccessCache.AccessCacheOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def GetFileWithOptionsAsync(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, options: win32more.Windows.Storage.AccessCache.AccessCacheOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetFolderWithOptionsAsync(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, options: win32more.Windows.Storage.AccessCache.AccessCacheOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ContainsItem(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList) -> Void: ...
    @winrt_mixinmethod
    def CheckAccess(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, file: win32more.Windows.Storage.IStorageItem) -> Boolean: ...
    @winrt_mixinmethod
    def get_Entries(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList) -> win32more.Windows.Storage.AccessCache.AccessListEntryView: ...
    @winrt_mixinmethod
    def get_MaximumItemsAllowed(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList) -> UInt32: ...
    Entries = property(get_Entries, None)
    MaximumItemsAllowed = property(get_MaximumItemsAllowed, None)
class StorageItemMostRecentlyUsedList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList
    _classid_ = 'Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList'
    @winrt_mixinmethod
    def add_ItemRemoved(self: win32more.Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList, win32more.Windows.Storage.AccessCache.ItemRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ItemRemoved(self: win32more.Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddOverloadDefaultMetadata(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, file: win32more.Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def Add(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, file: win32more.Windows.Storage.IStorageItem, metadata: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def AddOrReplaceOverloadDefaultMetadata(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, file: win32more.Windows.Storage.IStorageItem) -> Void: ...
    @winrt_mixinmethod
    def AddOrReplace(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, file: win32more.Windows.Storage.IStorageItem, metadata: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetItemAsync(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def GetFileAsync(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetFolderAsync(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def GetItemWithOptionsAsync(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, options: win32more.Windows.Storage.AccessCache.AccessCacheOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def GetFileWithOptionsAsync(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, options: win32more.Windows.Storage.AccessCache.AccessCacheOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetFolderWithOptionsAsync(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, options: win32more.Windows.Storage.AccessCache.AccessCacheOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ContainsItem(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList) -> Void: ...
    @winrt_mixinmethod
    def CheckAccess(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList, file: win32more.Windows.Storage.IStorageItem) -> Boolean: ...
    @winrt_mixinmethod
    def get_Entries(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList) -> win32more.Windows.Storage.AccessCache.AccessListEntryView: ...
    @winrt_mixinmethod
    def get_MaximumItemsAllowed(self: win32more.Windows.Storage.AccessCache.IStorageItemAccessList) -> UInt32: ...
    @winrt_mixinmethod
    def AddWithMetadataAndVisibility(self: win32more.Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList2, file: win32more.Windows.Storage.IStorageItem, metadata: WinRT_String, visibility: win32more.Windows.Storage.AccessCache.RecentStorageItemVisibility) -> WinRT_String: ...
    @winrt_mixinmethod
    def AddOrReplaceWithMetadataAndVisibility(self: win32more.Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList2, token: WinRT_String, file: win32more.Windows.Storage.IStorageItem, metadata: WinRT_String, visibility: win32more.Windows.Storage.AccessCache.RecentStorageItemVisibility) -> Void: ...
    Entries = property(get_Entries, None)
    MaximumItemsAllowed = property(get_MaximumItemsAllowed, None)
    ItemRemoved = event()


make_ready(__name__)
