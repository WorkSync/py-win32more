from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.BulkAccess
import win32more.Windows.Storage.FileProperties
import win32more.Windows.Storage.Search
import win32more.Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class FileInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.BulkAccess.IStorageItemInformation
    _classid_ = 'Windows.Storage.BulkAccess.FileInformation'
    @winrt_mixinmethod
    def get_MusicProperties(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation) -> win32more.Windows.Storage.FileProperties.MusicProperties: ...
    @winrt_mixinmethod
    def get_VideoProperties(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation) -> win32more.Windows.Storage.FileProperties.VideoProperties: ...
    @winrt_mixinmethod
    def get_ImageProperties(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation) -> win32more.Windows.Storage.FileProperties.ImageProperties: ...
    @winrt_mixinmethod
    def get_DocumentProperties(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation) -> win32more.Windows.Storage.FileProperties.DocumentProperties: ...
    @winrt_mixinmethod
    def get_BasicProperties(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation) -> win32more.Windows.Storage.FileProperties.BasicProperties: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation) -> win32more.Windows.Storage.FileProperties.StorageItemThumbnail: ...
    @winrt_mixinmethod
    def add_ThumbnailUpdated(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation, changedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.BulkAccess.IStorageItemInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ThumbnailUpdated(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PropertiesUpdated(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation, changedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.BulkAccess.IStorageItemInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PropertiesUpdated(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_FileType(self: win32more.Windows.Storage.IStorageFile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.Storage.IStorageFile) -> WinRT_String: ...
    @winrt_mixinmethod
    def OpenAsync(self: win32more.Windows.Storage.IStorageFile, accessMode: win32more.Windows.Storage.FileAccessMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def OpenTransactedWriteAsync(self: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageStreamTransaction]: ...
    @winrt_mixinmethod
    def CopyOverloadDefaultNameAndOptions(self: win32more.Windows.Storage.IStorageFile, destinationFolder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CopyOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageFile, destinationFolder: win32more.Windows.Storage.IStorageFolder, desiredNewName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CopyOverload(self: win32more.Windows.Storage.IStorageFile, destinationFolder: win32more.Windows.Storage.IStorageFolder, desiredNewName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CopyAndReplaceAsync(self: win32more.Windows.Storage.IStorageFile, fileToReplace: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MoveOverloadDefaultNameAndOptions(self: win32more.Windows.Storage.IStorageFile, destinationFolder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MoveOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageFile, destinationFolder: win32more.Windows.Storage.IStorageFolder, desiredNewName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MoveOverload(self: win32more.Windows.Storage.IStorageFile, destinationFolder: win32more.Windows.Storage.IStorageFolder, desiredNewName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MoveAndReplaceAsync(self: win32more.Windows.Storage.IStorageFile, fileToReplace: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenameAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItem, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenameAsync(self: win32more.Windows.Storage.IStorageItem, desiredName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.Storage.IStorageItem, option: win32more.Windows.Storage.StorageDeleteOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetBasicPropertiesAsync(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.BasicProperties]: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Attributes(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Storage.FileAttributes: ...
    @winrt_mixinmethod
    def get_DateCreated(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def IsOfType(self: win32more.Windows.Storage.IStorageItem, type: win32more.Windows.Storage.StorageItemTypes) -> Boolean: ...
    @winrt_mixinmethod
    def OpenReadAsync(self: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
    @winrt_mixinmethod
    def OpenSequentialReadAsync(self: win32more.Windows.Storage.Streams.IInputStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IInputStream]: ...
    @winrt_mixinmethod
    def GetThumbnailAsyncOverloadDefaultSizeDefaultOptions(self: win32more.Windows.Storage.IStorageItemProperties, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetThumbnailAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItemProperties, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetThumbnailAsync(self: win32more.Windows.Storage.IStorageItemProperties, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: win32more.Windows.Storage.FileProperties.ThumbnailOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayType(self: win32more.Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FolderRelativeId(self: win32more.Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Storage.IStorageItemProperties) -> win32more.Windows.Storage.FileProperties.StorageItemContentProperties: ...
    @winrt_mixinmethod
    def GetParentAsync(self: win32more.Windows.Storage.IStorageItem2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def IsEqual(self: win32more.Windows.Storage.IStorageItem2, item: win32more.Windows.Storage.IStorageItem) -> Boolean: ...
    @winrt_mixinmethod
    def get_Provider(self: win32more.Windows.Storage.IStorageItemPropertiesWithProvider) -> win32more.Windows.Storage.StorageProvider: ...
    @winrt_mixinmethod
    def get_IsAvailable(self: win32more.Windows.Storage.IStorageFilePropertiesWithAvailability) -> Boolean: ...
    @winrt_mixinmethod
    def OpenWithOptionsAsync(self: win32more.Windows.Storage.IStorageFile2, accessMode: win32more.Windows.Storage.FileAccessMode, options: win32more.Windows.Storage.StorageOpenOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def OpenTransactedWriteWithOptionsAsync(self: win32more.Windows.Storage.IStorageFile2, options: win32more.Windows.Storage.StorageOpenOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageStreamTransaction]: ...
    MusicProperties = property(get_MusicProperties, None)
    VideoProperties = property(get_VideoProperties, None)
    ImageProperties = property(get_ImageProperties, None)
    DocumentProperties = property(get_DocumentProperties, None)
    BasicProperties = property(get_BasicProperties, None)
    Thumbnail = property(get_Thumbnail, None)
    FileType = property(get_FileType, None)
    ContentType = property(get_ContentType, None)
    Name = property(get_Name, None)
    Path = property(get_Path, None)
    Attributes = property(get_Attributes, None)
    DateCreated = property(get_DateCreated, None)
    DisplayName = property(get_DisplayName, None)
    DisplayType = property(get_DisplayType, None)
    FolderRelativeId = property(get_FolderRelativeId, None)
    Properties = property(get_Properties, None)
    Provider = property(get_Provider, None)
    IsAvailable = property(get_IsAvailable, None)
class FileInformationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.BulkAccess.IFileInformationFactory
    _classid_ = 'Windows.Storage.BulkAccess.FileInformationFactory'
    @winrt_factorymethod
    def CreateWithMode(cls: win32more.Windows.Storage.BulkAccess.IFileInformationFactoryFactory, queryResult: win32more.Windows.Storage.Search.IStorageQueryResultBase, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode) -> win32more.Windows.Storage.BulkAccess.FileInformationFactory: ...
    @winrt_factorymethod
    def CreateWithModeAndSize(cls: win32more.Windows.Storage.BulkAccess.IFileInformationFactoryFactory, queryResult: win32more.Windows.Storage.Search.IStorageQueryResultBase, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedThumbnailSize: UInt32) -> win32more.Windows.Storage.BulkAccess.FileInformationFactory: ...
    @winrt_factorymethod
    def CreateWithModeAndSizeAndOptions(cls: win32more.Windows.Storage.BulkAccess.IFileInformationFactoryFactory, queryResult: win32more.Windows.Storage.Search.IStorageQueryResultBase, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedThumbnailSize: UInt32, thumbnailOptions: win32more.Windows.Storage.FileProperties.ThumbnailOptions) -> win32more.Windows.Storage.BulkAccess.FileInformationFactory: ...
    @winrt_factorymethod
    def CreateWithModeAndSizeAndOptionsAndFlags(cls: win32more.Windows.Storage.BulkAccess.IFileInformationFactoryFactory, queryResult: win32more.Windows.Storage.Search.IStorageQueryResultBase, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedThumbnailSize: UInt32, thumbnailOptions: win32more.Windows.Storage.FileProperties.ThumbnailOptions, delayLoad: Boolean) -> win32more.Windows.Storage.BulkAccess.FileInformationFactory: ...
    @winrt_mixinmethod
    def GetItemsAsync(self: win32more.Windows.Storage.BulkAccess.IFileInformationFactory, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.BulkAccess.IStorageItemInformation]]: ...
    @winrt_mixinmethod
    def GetItemsAsyncDefaultStartAndCount(self: win32more.Windows.Storage.BulkAccess.IFileInformationFactory) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.BulkAccess.IStorageItemInformation]]: ...
    @winrt_mixinmethod
    def GetFilesAsync(self: win32more.Windows.Storage.BulkAccess.IFileInformationFactory, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.BulkAccess.FileInformation]]: ...
    @winrt_mixinmethod
    def GetFilesAsyncDefaultStartAndCount(self: win32more.Windows.Storage.BulkAccess.IFileInformationFactory) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.BulkAccess.FileInformation]]: ...
    @winrt_mixinmethod
    def GetFoldersAsync(self: win32more.Windows.Storage.BulkAccess.IFileInformationFactory, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.BulkAccess.FolderInformation]]: ...
    @winrt_mixinmethod
    def GetFoldersAsyncDefaultStartAndCount(self: win32more.Windows.Storage.BulkAccess.IFileInformationFactory) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.BulkAccess.FolderInformation]]: ...
    @winrt_mixinmethod
    def GetVirtualizedItemsVector(self: win32more.Windows.Storage.BulkAccess.IFileInformationFactory) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def GetVirtualizedFilesVector(self: win32more.Windows.Storage.BulkAccess.IFileInformationFactory) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def GetVirtualizedFoldersVector(self: win32more.Windows.Storage.BulkAccess.IFileInformationFactory) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
class FolderInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.BulkAccess.IStorageItemInformation
    _classid_ = 'Windows.Storage.BulkAccess.FolderInformation'
    @winrt_mixinmethod
    def get_MusicProperties(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation) -> win32more.Windows.Storage.FileProperties.MusicProperties: ...
    @winrt_mixinmethod
    def get_VideoProperties(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation) -> win32more.Windows.Storage.FileProperties.VideoProperties: ...
    @winrt_mixinmethod
    def get_ImageProperties(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation) -> win32more.Windows.Storage.FileProperties.ImageProperties: ...
    @winrt_mixinmethod
    def get_DocumentProperties(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation) -> win32more.Windows.Storage.FileProperties.DocumentProperties: ...
    @winrt_mixinmethod
    def get_BasicProperties(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation) -> win32more.Windows.Storage.FileProperties.BasicProperties: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation) -> win32more.Windows.Storage.FileProperties.StorageItemThumbnail: ...
    @winrt_mixinmethod
    def add_ThumbnailUpdated(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation, changedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.BulkAccess.IStorageItemInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ThumbnailUpdated(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PropertiesUpdated(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation, changedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.BulkAccess.IStorageItemInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PropertiesUpdated(self: win32more.Windows.Storage.BulkAccess.IStorageItemInformation, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateFileAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CreateFileAsync(self: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String, options: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CreateFolderAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def CreateFolderAsync(self: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String, options: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def GetFileAsync(self: win32more.Windows.Storage.IStorageFolder, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetFolderAsync(self: win32more.Windows.Storage.IStorageFolder, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def GetItemAsync(self: win32more.Windows.Storage.IStorageFolder, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def GetFilesAsyncOverloadDefaultOptionsStartAndCount(self: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetFoldersAsyncOverloadDefaultOptionsStartAndCount(self: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetItemsAsyncOverloadDefaultStartAndCount(self: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]]: ...
    @winrt_mixinmethod
    def RenameAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItem, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenameAsync(self: win32more.Windows.Storage.IStorageItem, desiredName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.Storage.IStorageItem, option: win32more.Windows.Storage.StorageDeleteOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetBasicPropertiesAsync(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.BasicProperties]: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Attributes(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Storage.FileAttributes: ...
    @winrt_mixinmethod
    def get_DateCreated(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def IsOfType(self: win32more.Windows.Storage.IStorageItem, type: win32more.Windows.Storage.StorageItemTypes) -> Boolean: ...
    @winrt_mixinmethod
    def GetThumbnailAsyncOverloadDefaultSizeDefaultOptions(self: win32more.Windows.Storage.IStorageItemProperties, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetThumbnailAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItemProperties, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetThumbnailAsync(self: win32more.Windows.Storage.IStorageItemProperties, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: win32more.Windows.Storage.FileProperties.ThumbnailOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayType(self: win32more.Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FolderRelativeId(self: win32more.Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Storage.IStorageItemProperties) -> win32more.Windows.Storage.FileProperties.StorageItemContentProperties: ...
    @winrt_mixinmethod
    def GetIndexedStateAsync(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Search.IndexedState]: ...
    @winrt_mixinmethod
    def CreateFileQueryOverloadDefault(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def CreateFileQuery(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFileQuery) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def CreateFileQueryWithOptions(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, queryOptions: win32more.Windows.Storage.Search.QueryOptions) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def CreateFolderQueryOverloadDefault(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations) -> win32more.Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_mixinmethod
    def CreateFolderQuery(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFolderQuery) -> win32more.Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_mixinmethod
    def CreateFolderQueryWithOptions(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, queryOptions: win32more.Windows.Storage.Search.QueryOptions) -> win32more.Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_mixinmethod
    def CreateItemQuery(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations) -> win32more.Windows.Storage.Search.StorageItemQueryResult: ...
    @winrt_mixinmethod
    def CreateItemQueryWithOptions(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, queryOptions: win32more.Windows.Storage.Search.QueryOptions) -> win32more.Windows.Storage.Search.StorageItemQueryResult: ...
    @winrt_mixinmethod
    def GetFilesAsync(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFileQuery, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetFilesAsyncOverloadDefaultStartAndCount(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFileQuery) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetFoldersAsync(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFolderQuery, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetFoldersAsyncOverloadDefaultStartAndCount(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFolderQuery) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetItemsAsync(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]]: ...
    @winrt_mixinmethod
    def AreQueryOptionsSupported(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, queryOptions: win32more.Windows.Storage.Search.QueryOptions) -> Boolean: ...
    @winrt_mixinmethod
    def IsCommonFolderQuerySupported(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFolderQuery) -> Boolean: ...
    @winrt_mixinmethod
    def IsCommonFileQuerySupported(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFileQuery) -> Boolean: ...
    @winrt_mixinmethod
    def GetParentAsync(self: win32more.Windows.Storage.IStorageItem2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def IsEqual(self: win32more.Windows.Storage.IStorageItem2, item: win32more.Windows.Storage.IStorageItem) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetItemAsync(self: win32more.Windows.Storage.IStorageFolder2, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def get_Provider(self: win32more.Windows.Storage.IStorageItemPropertiesWithProvider) -> win32more.Windows.Storage.StorageProvider: ...
    MusicProperties = property(get_MusicProperties, None)
    VideoProperties = property(get_VideoProperties, None)
    ImageProperties = property(get_ImageProperties, None)
    DocumentProperties = property(get_DocumentProperties, None)
    BasicProperties = property(get_BasicProperties, None)
    Thumbnail = property(get_Thumbnail, None)
    Name = property(get_Name, None)
    Path = property(get_Path, None)
    Attributes = property(get_Attributes, None)
    DateCreated = property(get_DateCreated, None)
    DisplayName = property(get_DisplayName, None)
    DisplayType = property(get_DisplayType, None)
    FolderRelativeId = property(get_FolderRelativeId, None)
    Properties = property(get_Properties, None)
    Provider = property(get_Provider, None)
class IFileInformationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.BulkAccess.IFileInformationFactory'
    _iid_ = Guid('{401d88be-960f-4d6d-a7d0-1a3861e76c83}')
    @winrt_commethod(6)
    def GetItemsAsync(self, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.BulkAccess.IStorageItemInformation]]: ...
    @winrt_commethod(7)
    def GetItemsAsyncDefaultStartAndCount(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.BulkAccess.IStorageItemInformation]]: ...
    @winrt_commethod(8)
    def GetFilesAsync(self, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.BulkAccess.FileInformation]]: ...
    @winrt_commethod(9)
    def GetFilesAsyncDefaultStartAndCount(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.BulkAccess.FileInformation]]: ...
    @winrt_commethod(10)
    def GetFoldersAsync(self, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.BulkAccess.FolderInformation]]: ...
    @winrt_commethod(11)
    def GetFoldersAsyncDefaultStartAndCount(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.BulkAccess.FolderInformation]]: ...
    @winrt_commethod(12)
    def GetVirtualizedItemsVector(self) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(13)
    def GetVirtualizedFilesVector(self) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(14)
    def GetVirtualizedFoldersVector(self) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
class IFileInformationFactoryFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.BulkAccess.IFileInformationFactoryFactory'
    _iid_ = Guid('{84ea0e7d-e4a2-4f00-8afa-af5e0f826bd5}')
    @winrt_commethod(6)
    def CreateWithMode(self, queryResult: win32more.Windows.Storage.Search.IStorageQueryResultBase, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode) -> win32more.Windows.Storage.BulkAccess.FileInformationFactory: ...
    @winrt_commethod(7)
    def CreateWithModeAndSize(self, queryResult: win32more.Windows.Storage.Search.IStorageQueryResultBase, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedThumbnailSize: UInt32) -> win32more.Windows.Storage.BulkAccess.FileInformationFactory: ...
    @winrt_commethod(8)
    def CreateWithModeAndSizeAndOptions(self, queryResult: win32more.Windows.Storage.Search.IStorageQueryResultBase, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedThumbnailSize: UInt32, thumbnailOptions: win32more.Windows.Storage.FileProperties.ThumbnailOptions) -> win32more.Windows.Storage.BulkAccess.FileInformationFactory: ...
    @winrt_commethod(9)
    def CreateWithModeAndSizeAndOptionsAndFlags(self, queryResult: win32more.Windows.Storage.Search.IStorageQueryResultBase, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedThumbnailSize: UInt32, thumbnailOptions: win32more.Windows.Storage.FileProperties.ThumbnailOptions, delayLoad: Boolean) -> win32more.Windows.Storage.BulkAccess.FileInformationFactory: ...
class IStorageItemInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.BulkAccess.IStorageItemInformation'
    _iid_ = Guid('{87a5cb8b-8972-4f40-8de0-d86fb179d8fa}')
    @winrt_commethod(6)
    def get_MusicProperties(self) -> win32more.Windows.Storage.FileProperties.MusicProperties: ...
    @winrt_commethod(7)
    def get_VideoProperties(self) -> win32more.Windows.Storage.FileProperties.VideoProperties: ...
    @winrt_commethod(8)
    def get_ImageProperties(self) -> win32more.Windows.Storage.FileProperties.ImageProperties: ...
    @winrt_commethod(9)
    def get_DocumentProperties(self) -> win32more.Windows.Storage.FileProperties.DocumentProperties: ...
    @winrt_commethod(10)
    def get_BasicProperties(self) -> win32more.Windows.Storage.FileProperties.BasicProperties: ...
    @winrt_commethod(11)
    def get_Thumbnail(self) -> win32more.Windows.Storage.FileProperties.StorageItemThumbnail: ...
    @winrt_commethod(12)
    def add_ThumbnailUpdated(self, changedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.BulkAccess.IStorageItemInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ThumbnailUpdated(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_PropertiesUpdated(self, changedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.BulkAccess.IStorageItemInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_PropertiesUpdated(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    MusicProperties = property(get_MusicProperties, None)
    VideoProperties = property(get_VideoProperties, None)
    ImageProperties = property(get_ImageProperties, None)
    DocumentProperties = property(get_DocumentProperties, None)
    BasicProperties = property(get_BasicProperties, None)
    Thumbnail = property(get_Thumbnail, None)
make_head(_module, 'FileInformation')
make_head(_module, 'FileInformationFactory')
make_head(_module, 'FolderInformation')
make_head(_module, 'IFileInformationFactory')
make_head(_module, 'IFileInformationFactoryFactory')
make_head(_module, 'IStorageItemInformation')
