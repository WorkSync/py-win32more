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
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Media
import win32more.Windows.Media.Audio
import win32more.Windows.Media.Capture
import win32more.Windows.Media.Core
import win32more.Windows.Media.Devices
import win32more.Windows.Media.Effects
import win32more.Windows.Media.MediaProperties
import win32more.Windows.Media.Render
import win32more.Windows.Media.Transcoding
import win32more.Windows.Storage
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AudioDeviceInputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioDeviceInputNode
    _classid_ = 'Windows.Media.Audio.AudioDeviceInputNode'
    @winrt_mixinmethod
    def get_Device(self: win32more.Windows.Media.Audio.IAudioDeviceInputNode) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_OutgoingConnections(self: win32more.Windows.Media.Audio.IAudioInputNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Audio.AudioGraphConnection]: ...
    @winrt_mixinmethod
    def AddOutgoingConnection(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def AddOutgoingConnectionWithGain(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode, gain: Double) -> Void: ...
    @winrt_mixinmethod
    def RemoveOutgoingConnection(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def get_EffectDefinitions(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    @winrt_mixinmethod
    def put_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode) -> Double: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode) -> Boolean: ...
    @winrt_mixinmethod
    def put_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def DisableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def EnableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_Emitter(self: win32more.Windows.Media.Audio.IAudioInputNode2) -> win32more.Windows.Media.Audio.AudioNodeEmitter: ...
    Device = property(get_Device, None)
    OutgoingConnections = property(get_OutgoingConnections, None)
    EffectDefinitions = property(get_EffectDefinitions, None)
    OutgoingGain = property(get_OutgoingGain, put_OutgoingGain)
    EncodingProperties = property(get_EncodingProperties, None)
    ConsumeInput = property(get_ConsumeInput, put_ConsumeInput)
    Emitter = property(get_Emitter, None)
AudioDeviceNodeCreationStatus = Int32
AudioDeviceNodeCreationStatus_Success: AudioDeviceNodeCreationStatus = 0
AudioDeviceNodeCreationStatus_DeviceNotAvailable: AudioDeviceNodeCreationStatus = 1
AudioDeviceNodeCreationStatus_FormatNotSupported: AudioDeviceNodeCreationStatus = 2
AudioDeviceNodeCreationStatus_UnknownFailure: AudioDeviceNodeCreationStatus = 3
AudioDeviceNodeCreationStatus_AccessDenied: AudioDeviceNodeCreationStatus = 4
class AudioDeviceOutputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioDeviceOutputNode
    _classid_ = 'Windows.Media.Audio.AudioDeviceOutputNode'
    @winrt_mixinmethod
    def get_Device(self: win32more.Windows.Media.Audio.IAudioDeviceOutputNode) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_EffectDefinitions(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    @winrt_mixinmethod
    def put_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode) -> Double: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode) -> Boolean: ...
    @winrt_mixinmethod
    def put_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def DisableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def EnableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def put_Listener(self: win32more.Windows.Media.Audio.IAudioNodeWithListener, value: win32more.Windows.Media.Audio.AudioNodeListener) -> Void: ...
    @winrt_mixinmethod
    def get_Listener(self: win32more.Windows.Media.Audio.IAudioNodeWithListener) -> win32more.Windows.Media.Audio.AudioNodeListener: ...
    Device = property(get_Device, None)
    EffectDefinitions = property(get_EffectDefinitions, None)
    OutgoingGain = property(get_OutgoingGain, put_OutgoingGain)
    EncodingProperties = property(get_EncodingProperties, None)
    ConsumeInput = property(get_ConsumeInput, put_ConsumeInput)
    Listener = property(get_Listener, put_Listener)
class AudioFileInputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioFileInputNode
    _classid_ = 'Windows.Media.Audio.AudioFileInputNode'
    @winrt_mixinmethod
    def put_PlaybackSpeedFactor(self: win32more.Windows.Media.Audio.IAudioFileInputNode, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_PlaybackSpeedFactor(self: win32more.Windows.Media.Audio.IAudioFileInputNode) -> Double: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Media.Audio.IAudioFileInputNode) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def Seek(self: win32more.Windows.Media.Audio.IAudioFileInputNode, position: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Media.Audio.IAudioFileInputNode) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_StartTime(self: win32more.Windows.Media.Audio.IAudioFileInputNode, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_EndTime(self: win32more.Windows.Media.Audio.IAudioFileInputNode) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_EndTime(self: win32more.Windows.Media.Audio.IAudioFileInputNode, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_LoopCount(self: win32more.Windows.Media.Audio.IAudioFileInputNode) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_LoopCount(self: win32more.Windows.Media.Audio.IAudioFileInputNode, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Audio.IAudioFileInputNode) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SourceFile(self: win32more.Windows.Media.Audio.IAudioFileInputNode) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def add_FileCompleted(self: win32more.Windows.Media.Audio.IAudioFileInputNode, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioFileInputNode, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FileCompleted(self: win32more.Windows.Media.Audio.IAudioFileInputNode, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_OutgoingConnections(self: win32more.Windows.Media.Audio.IAudioInputNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Audio.AudioGraphConnection]: ...
    @winrt_mixinmethod
    def AddOutgoingConnection(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def AddOutgoingConnectionWithGain(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode, gain: Double) -> Void: ...
    @winrt_mixinmethod
    def RemoveOutgoingConnection(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def get_EffectDefinitions(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    @winrt_mixinmethod
    def put_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode) -> Double: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode) -> Boolean: ...
    @winrt_mixinmethod
    def put_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def DisableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def EnableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_Emitter(self: win32more.Windows.Media.Audio.IAudioInputNode2) -> win32more.Windows.Media.Audio.AudioNodeEmitter: ...
    PlaybackSpeedFactor = property(get_PlaybackSpeedFactor, put_PlaybackSpeedFactor)
    Position = property(get_Position, None)
    StartTime = property(get_StartTime, put_StartTime)
    EndTime = property(get_EndTime, put_EndTime)
    LoopCount = property(get_LoopCount, put_LoopCount)
    Duration = property(get_Duration, None)
    SourceFile = property(get_SourceFile, None)
    OutgoingConnections = property(get_OutgoingConnections, None)
    EffectDefinitions = property(get_EffectDefinitions, None)
    OutgoingGain = property(get_OutgoingGain, put_OutgoingGain)
    EncodingProperties = property(get_EncodingProperties, None)
    ConsumeInput = property(get_ConsumeInput, put_ConsumeInput)
    Emitter = property(get_Emitter, None)
AudioFileNodeCreationStatus = Int32
AudioFileNodeCreationStatus_Success: AudioFileNodeCreationStatus = 0
AudioFileNodeCreationStatus_FileNotFound: AudioFileNodeCreationStatus = 1
AudioFileNodeCreationStatus_InvalidFileType: AudioFileNodeCreationStatus = 2
AudioFileNodeCreationStatus_FormatNotSupported: AudioFileNodeCreationStatus = 3
AudioFileNodeCreationStatus_UnknownFailure: AudioFileNodeCreationStatus = 4
class AudioFileOutputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioFileOutputNode
    _classid_ = 'Windows.Media.Audio.AudioFileOutputNode'
    @winrt_mixinmethod
    def get_File(self: win32more.Windows.Media.Audio.IAudioFileOutputNode) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_mixinmethod
    def get_FileEncodingProfile(self: win32more.Windows.Media.Audio.IAudioFileOutputNode) -> win32more.Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_mixinmethod
    def FinalizeAsync(self: win32more.Windows.Media.Audio.IAudioFileOutputNode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Transcoding.TranscodeFailureReason]: ...
    @winrt_mixinmethod
    def get_EffectDefinitions(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    @winrt_mixinmethod
    def put_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode) -> Double: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode) -> Boolean: ...
    @winrt_mixinmethod
    def put_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def DisableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def EnableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    File = property(get_File, None)
    FileEncodingProfile = property(get_FileEncodingProfile, None)
    EffectDefinitions = property(get_EffectDefinitions, None)
    OutgoingGain = property(get_OutgoingGain, put_OutgoingGain)
    EncodingProperties = property(get_EncodingProperties, None)
    ConsumeInput = property(get_ConsumeInput, put_ConsumeInput)
class AudioFrameCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioFrameCompletedEventArgs
    _classid_ = 'Windows.Media.Audio.AudioFrameCompletedEventArgs'
    @winrt_mixinmethod
    def get_Frame(self: win32more.Windows.Media.Audio.IAudioFrameCompletedEventArgs) -> win32more.Windows.Media.AudioFrame: ...
    Frame = property(get_Frame, None)
class AudioFrameInputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioFrameInputNode
    _classid_ = 'Windows.Media.Audio.AudioFrameInputNode'
    @winrt_mixinmethod
    def put_PlaybackSpeedFactor(self: win32more.Windows.Media.Audio.IAudioFrameInputNode, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_PlaybackSpeedFactor(self: win32more.Windows.Media.Audio.IAudioFrameInputNode) -> Double: ...
    @winrt_mixinmethod
    def AddFrame(self: win32more.Windows.Media.Audio.IAudioFrameInputNode, frame: win32more.Windows.Media.AudioFrame) -> Void: ...
    @winrt_mixinmethod
    def DiscardQueuedFrames(self: win32more.Windows.Media.Audio.IAudioFrameInputNode) -> Void: ...
    @winrt_mixinmethod
    def get_QueuedSampleCount(self: win32more.Windows.Media.Audio.IAudioFrameInputNode) -> UInt64: ...
    @winrt_mixinmethod
    def add_AudioFrameCompleted(self: win32more.Windows.Media.Audio.IAudioFrameInputNode, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioFrameInputNode, win32more.Windows.Media.Audio.AudioFrameCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AudioFrameCompleted(self: win32more.Windows.Media.Audio.IAudioFrameInputNode, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_QuantumStarted(self: win32more.Windows.Media.Audio.IAudioFrameInputNode, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioFrameInputNode, win32more.Windows.Media.Audio.FrameInputNodeQuantumStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_QuantumStarted(self: win32more.Windows.Media.Audio.IAudioFrameInputNode, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_OutgoingConnections(self: win32more.Windows.Media.Audio.IAudioInputNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Audio.AudioGraphConnection]: ...
    @winrt_mixinmethod
    def AddOutgoingConnection(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def AddOutgoingConnectionWithGain(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode, gain: Double) -> Void: ...
    @winrt_mixinmethod
    def RemoveOutgoingConnection(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def get_EffectDefinitions(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    @winrt_mixinmethod
    def put_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode) -> Double: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode) -> Boolean: ...
    @winrt_mixinmethod
    def put_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def DisableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def EnableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_Emitter(self: win32more.Windows.Media.Audio.IAudioInputNode2) -> win32more.Windows.Media.Audio.AudioNodeEmitter: ...
    PlaybackSpeedFactor = property(get_PlaybackSpeedFactor, put_PlaybackSpeedFactor)
    QueuedSampleCount = property(get_QueuedSampleCount, None)
    OutgoingConnections = property(get_OutgoingConnections, None)
    EffectDefinitions = property(get_EffectDefinitions, None)
    OutgoingGain = property(get_OutgoingGain, put_OutgoingGain)
    EncodingProperties = property(get_EncodingProperties, None)
    ConsumeInput = property(get_ConsumeInput, put_ConsumeInput)
    Emitter = property(get_Emitter, None)
class AudioFrameOutputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioFrameOutputNode
    _classid_ = 'Windows.Media.Audio.AudioFrameOutputNode'
    @winrt_mixinmethod
    def GetFrame(self: win32more.Windows.Media.Audio.IAudioFrameOutputNode) -> win32more.Windows.Media.AudioFrame: ...
    @winrt_mixinmethod
    def get_EffectDefinitions(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    @winrt_mixinmethod
    def put_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode) -> Double: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode) -> Boolean: ...
    @winrt_mixinmethod
    def put_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def DisableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def EnableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    EffectDefinitions = property(get_EffectDefinitions, None)
    OutgoingGain = property(get_OutgoingGain, put_OutgoingGain)
    EncodingProperties = property(get_EncodingProperties, None)
    ConsumeInput = property(get_ConsumeInput, put_ConsumeInput)
class AudioGraph(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioGraph
    _classid_ = 'Windows.Media.Audio.AudioGraph'
    @winrt_mixinmethod
    def CreateFrameInputNode(self: win32more.Windows.Media.Audio.IAudioGraph) -> win32more.Windows.Media.Audio.AudioFrameInputNode: ...
    @winrt_mixinmethod
    def CreateFrameInputNodeWithFormat(self: win32more.Windows.Media.Audio.IAudioGraph, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> win32more.Windows.Media.Audio.AudioFrameInputNode: ...
    @winrt_mixinmethod
    def CreateDeviceInputNodeAsync(self: win32more.Windows.Media.Audio.IAudioGraph, category: win32more.Windows.Media.Capture.MediaCategory) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioDeviceInputNodeResult]: ...
    @winrt_mixinmethod
    def CreateDeviceInputNodeWithFormatAsync(self: win32more.Windows.Media.Audio.IAudioGraph, category: win32more.Windows.Media.Capture.MediaCategory, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioDeviceInputNodeResult]: ...
    @winrt_mixinmethod
    def CreateDeviceInputNodeWithFormatOnDeviceAsync(self: win32more.Windows.Media.Audio.IAudioGraph, category: win32more.Windows.Media.Capture.MediaCategory, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties, device: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioDeviceInputNodeResult]: ...
    @winrt_mixinmethod
    def CreateFrameOutputNode(self: win32more.Windows.Media.Audio.IAudioGraph) -> win32more.Windows.Media.Audio.AudioFrameOutputNode: ...
    @winrt_mixinmethod
    def CreateFrameOutputNodeWithFormat(self: win32more.Windows.Media.Audio.IAudioGraph, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> win32more.Windows.Media.Audio.AudioFrameOutputNode: ...
    @winrt_mixinmethod
    def CreateDeviceOutputNodeAsync(self: win32more.Windows.Media.Audio.IAudioGraph) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioDeviceOutputNodeResult]: ...
    @winrt_mixinmethod
    def CreateFileInputNodeAsync(self: win32more.Windows.Media.Audio.IAudioGraph, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioFileInputNodeResult]: ...
    @winrt_mixinmethod
    def CreateFileOutputNodeAsync(self: win32more.Windows.Media.Audio.IAudioGraph, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioFileOutputNodeResult]: ...
    @winrt_mixinmethod
    def CreateFileOutputNodeWithFileProfileAsync(self: win32more.Windows.Media.Audio.IAudioGraph, file: win32more.Windows.Storage.IStorageFile, fileEncodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioFileOutputNodeResult]: ...
    @winrt_mixinmethod
    def CreateSubmixNode(self: win32more.Windows.Media.Audio.IAudioGraph) -> win32more.Windows.Media.Audio.AudioSubmixNode: ...
    @winrt_mixinmethod
    def CreateSubmixNodeWithFormat(self: win32more.Windows.Media.Audio.IAudioGraph, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> win32more.Windows.Media.Audio.AudioSubmixNode: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Audio.IAudioGraph) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Media.Audio.IAudioGraph) -> Void: ...
    @winrt_mixinmethod
    def ResetAllNodes(self: win32more.Windows.Media.Audio.IAudioGraph) -> Void: ...
    @winrt_mixinmethod
    def add_QuantumStarted(self: win32more.Windows.Media.Audio.IAudioGraph, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioGraph, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_QuantumStarted(self: win32more.Windows.Media.Audio.IAudioGraph, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_QuantumProcessed(self: win32more.Windows.Media.Audio.IAudioGraph, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioGraph, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_QuantumProcessed(self: win32more.Windows.Media.Audio.IAudioGraph, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnrecoverableErrorOccurred(self: win32more.Windows.Media.Audio.IAudioGraph, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioGraph, win32more.Windows.Media.Audio.AudioGraphUnrecoverableErrorOccurredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnrecoverableErrorOccurred(self: win32more.Windows.Media.Audio.IAudioGraph, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CompletedQuantumCount(self: win32more.Windows.Media.Audio.IAudioGraph) -> UInt64: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Audio.IAudioGraph) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_LatencyInSamples(self: win32more.Windows.Media.Audio.IAudioGraph) -> Int32: ...
    @winrt_mixinmethod
    def get_PrimaryRenderDevice(self: win32more.Windows.Media.Audio.IAudioGraph) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_RenderDeviceAudioProcessing(self: win32more.Windows.Media.Audio.IAudioGraph) -> win32more.Windows.Media.AudioProcessing: ...
    @winrt_mixinmethod
    def get_SamplesPerQuantum(self: win32more.Windows.Media.Audio.IAudioGraph) -> Int32: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def CreateFrameInputNodeWithFormatAndEmitter(self: win32more.Windows.Media.Audio.IAudioGraph2, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties, emitter: win32more.Windows.Media.Audio.AudioNodeEmitter) -> win32more.Windows.Media.Audio.AudioFrameInputNode: ...
    @winrt_mixinmethod
    def CreateDeviceInputNodeWithFormatAndEmitterOnDeviceAsync(self: win32more.Windows.Media.Audio.IAudioGraph2, category: win32more.Windows.Media.Capture.MediaCategory, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties, device: win32more.Windows.Devices.Enumeration.DeviceInformation, emitter: win32more.Windows.Media.Audio.AudioNodeEmitter) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioDeviceInputNodeResult]: ...
    @winrt_mixinmethod
    def CreateFileInputNodeWithEmitterAsync(self: win32more.Windows.Media.Audio.IAudioGraph2, file: win32more.Windows.Storage.IStorageFile, emitter: win32more.Windows.Media.Audio.AudioNodeEmitter) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioFileInputNodeResult]: ...
    @winrt_mixinmethod
    def CreateSubmixNodeWithFormatAndEmitter(self: win32more.Windows.Media.Audio.IAudioGraph2, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties, emitter: win32more.Windows.Media.Audio.AudioNodeEmitter) -> win32more.Windows.Media.Audio.AudioSubmixNode: ...
    @winrt_mixinmethod
    def CreateBatchUpdater(self: win32more.Windows.Media.Audio.IAudioGraph2) -> win32more.Windows.Media.Audio.AudioGraphBatchUpdater: ...
    @winrt_mixinmethod
    def CreateMediaSourceAudioInputNodeAsync(self: win32more.Windows.Media.Audio.IAudioGraph3, mediaSource: win32more.Windows.Media.Core.MediaSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateMediaSourceAudioInputNodeResult]: ...
    @winrt_mixinmethod
    def CreateMediaSourceAudioInputNodeWithEmitterAsync(self: win32more.Windows.Media.Audio.IAudioGraph3, mediaSource: win32more.Windows.Media.Core.MediaSource, emitter: win32more.Windows.Media.Audio.AudioNodeEmitter) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateMediaSourceAudioInputNodeResult]: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Windows.Media.Audio.IAudioGraphStatics, settings: win32more.Windows.Media.Audio.AudioGraphSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioGraphResult]: ...
    CompletedQuantumCount = property(get_CompletedQuantumCount, None)
    EncodingProperties = property(get_EncodingProperties, None)
    LatencyInSamples = property(get_LatencyInSamples, None)
    PrimaryRenderDevice = property(get_PrimaryRenderDevice, None)
    RenderDeviceAudioProcessing = property(get_RenderDeviceAudioProcessing, None)
    SamplesPerQuantum = property(get_SamplesPerQuantum, None)
class AudioGraphBatchUpdater(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.IClosable
    _classid_ = 'Windows.Media.Audio.AudioGraphBatchUpdater'
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class AudioGraphConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioGraphConnection
    _classid_ = 'Windows.Media.Audio.AudioGraphConnection'
    @winrt_mixinmethod
    def get_Destination(self: win32more.Windows.Media.Audio.IAudioGraphConnection) -> win32more.Windows.Media.Audio.IAudioNode: ...
    @winrt_mixinmethod
    def put_Gain(self: win32more.Windows.Media.Audio.IAudioGraphConnection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Gain(self: win32more.Windows.Media.Audio.IAudioGraphConnection) -> Double: ...
    Destination = property(get_Destination, None)
    Gain = property(get_Gain, put_Gain)
AudioGraphCreationStatus = Int32
AudioGraphCreationStatus_Success: AudioGraphCreationStatus = 0
AudioGraphCreationStatus_DeviceNotAvailable: AudioGraphCreationStatus = 1
AudioGraphCreationStatus_FormatNotSupported: AudioGraphCreationStatus = 2
AudioGraphCreationStatus_UnknownFailure: AudioGraphCreationStatus = 3
class AudioGraphSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioGraphSettings
    _classid_ = 'Windows.Media.Audio.AudioGraphSettings'
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Audio.IAudioGraphSettingsFactory, audioRenderCategory: win32more.Windows.Media.Render.AudioRenderCategory) -> win32more.Windows.Media.Audio.AudioGraphSettings: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Audio.IAudioGraphSettings) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def put_EncodingProperties(self: win32more.Windows.Media.Audio.IAudioGraphSettings, value: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> Void: ...
    @winrt_mixinmethod
    def get_PrimaryRenderDevice(self: win32more.Windows.Media.Audio.IAudioGraphSettings) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def put_PrimaryRenderDevice(self: win32more.Windows.Media.Audio.IAudioGraphSettings, value: win32more.Windows.Devices.Enumeration.DeviceInformation) -> Void: ...
    @winrt_mixinmethod
    def get_QuantumSizeSelectionMode(self: win32more.Windows.Media.Audio.IAudioGraphSettings) -> win32more.Windows.Media.Audio.QuantumSizeSelectionMode: ...
    @winrt_mixinmethod
    def put_QuantumSizeSelectionMode(self: win32more.Windows.Media.Audio.IAudioGraphSettings, value: win32more.Windows.Media.Audio.QuantumSizeSelectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredSamplesPerQuantum(self: win32more.Windows.Media.Audio.IAudioGraphSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_DesiredSamplesPerQuantum(self: win32more.Windows.Media.Audio.IAudioGraphSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_AudioRenderCategory(self: win32more.Windows.Media.Audio.IAudioGraphSettings) -> win32more.Windows.Media.Render.AudioRenderCategory: ...
    @winrt_mixinmethod
    def put_AudioRenderCategory(self: win32more.Windows.Media.Audio.IAudioGraphSettings, value: win32more.Windows.Media.Render.AudioRenderCategory) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredRenderDeviceAudioProcessing(self: win32more.Windows.Media.Audio.IAudioGraphSettings) -> win32more.Windows.Media.AudioProcessing: ...
    @winrt_mixinmethod
    def put_DesiredRenderDeviceAudioProcessing(self: win32more.Windows.Media.Audio.IAudioGraphSettings, value: win32more.Windows.Media.AudioProcessing) -> Void: ...
    @winrt_mixinmethod
    def put_MaxPlaybackSpeedFactor(self: win32more.Windows.Media.Audio.IAudioGraphSettings2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MaxPlaybackSpeedFactor(self: win32more.Windows.Media.Audio.IAudioGraphSettings2) -> Double: ...
    EncodingProperties = property(get_EncodingProperties, put_EncodingProperties)
    PrimaryRenderDevice = property(get_PrimaryRenderDevice, put_PrimaryRenderDevice)
    QuantumSizeSelectionMode = property(get_QuantumSizeSelectionMode, put_QuantumSizeSelectionMode)
    DesiredSamplesPerQuantum = property(get_DesiredSamplesPerQuantum, put_DesiredSamplesPerQuantum)
    AudioRenderCategory = property(get_AudioRenderCategory, put_AudioRenderCategory)
    DesiredRenderDeviceAudioProcessing = property(get_DesiredRenderDeviceAudioProcessing, put_DesiredRenderDeviceAudioProcessing)
    MaxPlaybackSpeedFactor = property(get_MaxPlaybackSpeedFactor, put_MaxPlaybackSpeedFactor)
AudioGraphUnrecoverableError = Int32
AudioGraphUnrecoverableError_None: AudioGraphUnrecoverableError = 0
AudioGraphUnrecoverableError_AudioDeviceLost: AudioGraphUnrecoverableError = 1
AudioGraphUnrecoverableError_AudioSessionDisconnected: AudioGraphUnrecoverableError = 2
AudioGraphUnrecoverableError_UnknownFailure: AudioGraphUnrecoverableError = 3
class AudioGraphUnrecoverableErrorOccurredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioGraphUnrecoverableErrorOccurredEventArgs
    _classid_ = 'Windows.Media.Audio.AudioGraphUnrecoverableErrorOccurredEventArgs'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Media.Audio.IAudioGraphUnrecoverableErrorOccurredEventArgs) -> win32more.Windows.Media.Audio.AudioGraphUnrecoverableError: ...
    Error = property(get_Error, None)
class AudioNodeEmitter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioNodeEmitter
    _classid_ = 'Windows.Media.Audio.AudioNodeEmitter'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Audio.AudioNodeEmitter: ...
    @winrt_factorymethod
    def CreateAudioNodeEmitter(cls: win32more.Windows.Media.Audio.IAudioNodeEmitterFactory, shape: win32more.Windows.Media.Audio.AudioNodeEmitterShape, decayModel: win32more.Windows.Media.Audio.AudioNodeEmitterDecayModel, settings: win32more.Windows.Media.Audio.AudioNodeEmitterSettings) -> win32more.Windows.Media.Audio.AudioNodeEmitter: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Media.Audio.IAudioNodeEmitter) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Position(self: win32more.Windows.Media.Audio.IAudioNodeEmitter, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Windows.Media.Audio.IAudioNodeEmitter) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Direction(self: win32more.Windows.Media.Audio.IAudioNodeEmitter, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.Media.Audio.IAudioNodeEmitter) -> win32more.Windows.Media.Audio.AudioNodeEmitterShape: ...
    @winrt_mixinmethod
    def get_DecayModel(self: win32more.Windows.Media.Audio.IAudioNodeEmitter) -> win32more.Windows.Media.Audio.AudioNodeEmitterDecayModel: ...
    @winrt_mixinmethod
    def get_Gain(self: win32more.Windows.Media.Audio.IAudioNodeEmitter) -> Double: ...
    @winrt_mixinmethod
    def put_Gain(self: win32more.Windows.Media.Audio.IAudioNodeEmitter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DistanceScale(self: win32more.Windows.Media.Audio.IAudioNodeEmitter) -> Double: ...
    @winrt_mixinmethod
    def put_DistanceScale(self: win32more.Windows.Media.Audio.IAudioNodeEmitter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DopplerScale(self: win32more.Windows.Media.Audio.IAudioNodeEmitter) -> Double: ...
    @winrt_mixinmethod
    def put_DopplerScale(self: win32more.Windows.Media.Audio.IAudioNodeEmitter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DopplerVelocity(self: win32more.Windows.Media.Audio.IAudioNodeEmitter) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_DopplerVelocity(self: win32more.Windows.Media.Audio.IAudioNodeEmitter, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_IsDopplerDisabled(self: win32more.Windows.Media.Audio.IAudioNodeEmitter) -> Boolean: ...
    @winrt_mixinmethod
    def get_SpatialAudioModel(self: win32more.Windows.Media.Audio.IAudioNodeEmitter2) -> win32more.Windows.Media.Audio.SpatialAudioModel: ...
    @winrt_mixinmethod
    def put_SpatialAudioModel(self: win32more.Windows.Media.Audio.IAudioNodeEmitter2, value: win32more.Windows.Media.Audio.SpatialAudioModel) -> Void: ...
    Position = property(get_Position, put_Position)
    Direction = property(get_Direction, put_Direction)
    Shape = property(get_Shape, None)
    DecayModel = property(get_DecayModel, None)
    Gain = property(get_Gain, put_Gain)
    DistanceScale = property(get_DistanceScale, put_DistanceScale)
    DopplerScale = property(get_DopplerScale, put_DopplerScale)
    DopplerVelocity = property(get_DopplerVelocity, put_DopplerVelocity)
    IsDopplerDisabled = property(get_IsDopplerDisabled, None)
    SpatialAudioModel = property(get_SpatialAudioModel, put_SpatialAudioModel)
class AudioNodeEmitterConeProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioNodeEmitterConeProperties
    _classid_ = 'Windows.Media.Audio.AudioNodeEmitterConeProperties'
    @winrt_mixinmethod
    def get_InnerAngle(self: win32more.Windows.Media.Audio.IAudioNodeEmitterConeProperties) -> Double: ...
    @winrt_mixinmethod
    def get_OuterAngle(self: win32more.Windows.Media.Audio.IAudioNodeEmitterConeProperties) -> Double: ...
    @winrt_mixinmethod
    def get_OuterAngleGain(self: win32more.Windows.Media.Audio.IAudioNodeEmitterConeProperties) -> Double: ...
    InnerAngle = property(get_InnerAngle, None)
    OuterAngle = property(get_OuterAngle, None)
    OuterAngleGain = property(get_OuterAngleGain, None)
AudioNodeEmitterDecayKind = Int32
AudioNodeEmitterDecayKind_Natural: AudioNodeEmitterDecayKind = 0
AudioNodeEmitterDecayKind_Custom: AudioNodeEmitterDecayKind = 1
class AudioNodeEmitterDecayModel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioNodeEmitterDecayModel
    _classid_ = 'Windows.Media.Audio.AudioNodeEmitterDecayModel'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Media.Audio.IAudioNodeEmitterDecayModel) -> win32more.Windows.Media.Audio.AudioNodeEmitterDecayKind: ...
    @winrt_mixinmethod
    def get_MinGain(self: win32more.Windows.Media.Audio.IAudioNodeEmitterDecayModel) -> Double: ...
    @winrt_mixinmethod
    def get_MaxGain(self: win32more.Windows.Media.Audio.IAudioNodeEmitterDecayModel) -> Double: ...
    @winrt_mixinmethod
    def get_NaturalProperties(self: win32more.Windows.Media.Audio.IAudioNodeEmitterDecayModel) -> win32more.Windows.Media.Audio.AudioNodeEmitterNaturalDecayModelProperties: ...
    @winrt_classmethod
    def CreateNatural(cls: win32more.Windows.Media.Audio.IAudioNodeEmitterDecayModelStatics, minGain: Double, maxGain: Double, unityGainDistance: Double, cutoffDistance: Double) -> win32more.Windows.Media.Audio.AudioNodeEmitterDecayModel: ...
    @winrt_classmethod
    def CreateCustom(cls: win32more.Windows.Media.Audio.IAudioNodeEmitterDecayModelStatics, minGain: Double, maxGain: Double) -> win32more.Windows.Media.Audio.AudioNodeEmitterDecayModel: ...
    Kind = property(get_Kind, None)
    MinGain = property(get_MinGain, None)
    MaxGain = property(get_MaxGain, None)
    NaturalProperties = property(get_NaturalProperties, None)
class AudioNodeEmitterNaturalDecayModelProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioNodeEmitterNaturalDecayModelProperties
    _classid_ = 'Windows.Media.Audio.AudioNodeEmitterNaturalDecayModelProperties'
    @winrt_mixinmethod
    def get_UnityGainDistance(self: win32more.Windows.Media.Audio.IAudioNodeEmitterNaturalDecayModelProperties) -> Double: ...
    @winrt_mixinmethod
    def get_CutoffDistance(self: win32more.Windows.Media.Audio.IAudioNodeEmitterNaturalDecayModelProperties) -> Double: ...
    UnityGainDistance = property(get_UnityGainDistance, None)
    CutoffDistance = property(get_CutoffDistance, None)
AudioNodeEmitterSettings = UInt32
AudioNodeEmitterSettings_None: AudioNodeEmitterSettings = 0
AudioNodeEmitterSettings_DisableDoppler: AudioNodeEmitterSettings = 1
class AudioNodeEmitterShape(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioNodeEmitterShape
    _classid_ = 'Windows.Media.Audio.AudioNodeEmitterShape'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Media.Audio.IAudioNodeEmitterShape) -> win32more.Windows.Media.Audio.AudioNodeEmitterShapeKind: ...
    @winrt_mixinmethod
    def get_ConeProperties(self: win32more.Windows.Media.Audio.IAudioNodeEmitterShape) -> win32more.Windows.Media.Audio.AudioNodeEmitterConeProperties: ...
    @winrt_classmethod
    def CreateCone(cls: win32more.Windows.Media.Audio.IAudioNodeEmitterShapeStatics, innerAngle: Double, outerAngle: Double, outerAngleGain: Double) -> win32more.Windows.Media.Audio.AudioNodeEmitterShape: ...
    @winrt_classmethod
    def CreateOmnidirectional(cls: win32more.Windows.Media.Audio.IAudioNodeEmitterShapeStatics) -> win32more.Windows.Media.Audio.AudioNodeEmitterShape: ...
    Kind = property(get_Kind, None)
    ConeProperties = property(get_ConeProperties, None)
AudioNodeEmitterShapeKind = Int32
AudioNodeEmitterShapeKind_Omnidirectional: AudioNodeEmitterShapeKind = 0
AudioNodeEmitterShapeKind_Cone: AudioNodeEmitterShapeKind = 1
class AudioNodeListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioNodeListener
    _classid_ = 'Windows.Media.Audio.AudioNodeListener'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Audio.AudioNodeListener: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Media.Audio.IAudioNodeListener) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Position(self: win32more.Windows.Media.Audio.IAudioNodeListener, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.Media.Audio.IAudioNodeListener) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def put_Orientation(self: win32more.Windows.Media.Audio.IAudioNodeListener, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def get_SpeedOfSound(self: win32more.Windows.Media.Audio.IAudioNodeListener) -> Double: ...
    @winrt_mixinmethod
    def put_SpeedOfSound(self: win32more.Windows.Media.Audio.IAudioNodeListener, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DopplerVelocity(self: win32more.Windows.Media.Audio.IAudioNodeListener) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_DopplerVelocity(self: win32more.Windows.Media.Audio.IAudioNodeListener, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    Position = property(get_Position, put_Position)
    Orientation = property(get_Orientation, put_Orientation)
    SpeedOfSound = property(get_SpeedOfSound, put_SpeedOfSound)
    DopplerVelocity = property(get_DopplerVelocity, put_DopplerVelocity)
class AudioPlaybackConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioPlaybackConnection
    _classid_ = 'Windows.Media.Audio.AudioPlaybackConnection'
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Audio.IAudioPlaybackConnection) -> Void: ...
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Media.Audio.IAudioPlaybackConnection) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Media.Audio.IAudioPlaybackConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.Audio.IAudioPlaybackConnection) -> win32more.Windows.Media.Audio.AudioPlaybackConnectionState: ...
    @winrt_mixinmethod
    def Open(self: win32more.Windows.Media.Audio.IAudioPlaybackConnection) -> win32more.Windows.Media.Audio.AudioPlaybackConnectionOpenResult: ...
    @winrt_mixinmethod
    def OpenAsync(self: win32more.Windows.Media.Audio.IAudioPlaybackConnection) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.AudioPlaybackConnectionOpenResult]: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Media.Audio.IAudioPlaybackConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioPlaybackConnection, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Media.Audio.IAudioPlaybackConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Media.Audio.IAudioPlaybackConnectionStatics) -> WinRT_String: ...
    @winrt_classmethod
    def TryCreateFromId(cls: win32more.Windows.Media.Audio.IAudioPlaybackConnectionStatics, id: WinRT_String) -> win32more.Windows.Media.Audio.AudioPlaybackConnection: ...
    DeviceId = property(get_DeviceId, None)
    State = property(get_State, None)
class AudioPlaybackConnectionOpenResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioPlaybackConnectionOpenResult
    _classid_ = 'Windows.Media.Audio.AudioPlaybackConnectionOpenResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Audio.IAudioPlaybackConnectionOpenResult) -> win32more.Windows.Media.Audio.AudioPlaybackConnectionOpenResultStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Audio.IAudioPlaybackConnectionOpenResult) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
AudioPlaybackConnectionOpenResultStatus = Int32
AudioPlaybackConnectionOpenResultStatus_Success: AudioPlaybackConnectionOpenResultStatus = 0
AudioPlaybackConnectionOpenResultStatus_RequestTimedOut: AudioPlaybackConnectionOpenResultStatus = 1
AudioPlaybackConnectionOpenResultStatus_DeniedBySystem: AudioPlaybackConnectionOpenResultStatus = 2
AudioPlaybackConnectionOpenResultStatus_UnknownFailure: AudioPlaybackConnectionOpenResultStatus = 3
AudioPlaybackConnectionState = Int32
AudioPlaybackConnectionState_Closed: AudioPlaybackConnectionState = 0
AudioPlaybackConnectionState_Opened: AudioPlaybackConnectionState = 1
class AudioStateMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioStateMonitor
    _classid_ = 'Windows.Media.Audio.AudioStateMonitor'
    @winrt_mixinmethod
    def add_SoundLevelChanged(self: win32more.Windows.Media.Audio.IAudioStateMonitor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioStateMonitor, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SoundLevelChanged(self: win32more.Windows.Media.Audio.IAudioStateMonitor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_SoundLevel(self: win32more.Windows.Media.Audio.IAudioStateMonitor) -> win32more.Windows.Media.SoundLevel: ...
    @winrt_classmethod
    def CreateForRenderMonitoring(cls: win32more.Windows.Media.Audio.IAudioStateMonitorStatics) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_classmethod
    def CreateForRenderMonitoringWithCategory(cls: win32more.Windows.Media.Audio.IAudioStateMonitorStatics, category: win32more.Windows.Media.Render.AudioRenderCategory) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_classmethod
    def CreateForRenderMonitoringWithCategoryAndDeviceRole(cls: win32more.Windows.Media.Audio.IAudioStateMonitorStatics, category: win32more.Windows.Media.Render.AudioRenderCategory, role: win32more.Windows.Media.Devices.AudioDeviceRole) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_classmethod
    def CreateForRenderMonitoringWithCategoryAndDeviceId(cls: win32more.Windows.Media.Audio.IAudioStateMonitorStatics, category: win32more.Windows.Media.Render.AudioRenderCategory, deviceId: WinRT_String) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_classmethod
    def CreateForCaptureMonitoring(cls: win32more.Windows.Media.Audio.IAudioStateMonitorStatics) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_classmethod
    def CreateForCaptureMonitoringWithCategory(cls: win32more.Windows.Media.Audio.IAudioStateMonitorStatics, category: win32more.Windows.Media.Capture.MediaCategory) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_classmethod
    def CreateForCaptureMonitoringWithCategoryAndDeviceRole(cls: win32more.Windows.Media.Audio.IAudioStateMonitorStatics, category: win32more.Windows.Media.Capture.MediaCategory, role: win32more.Windows.Media.Devices.AudioDeviceRole) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_classmethod
    def CreateForCaptureMonitoringWithCategoryAndDeviceId(cls: win32more.Windows.Media.Audio.IAudioStateMonitorStatics, category: win32more.Windows.Media.Capture.MediaCategory, deviceId: WinRT_String) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    SoundLevel = property(get_SoundLevel, None)
class AudioSubmixNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IAudioInputNode
    _classid_ = 'Windows.Media.Audio.AudioSubmixNode'
    @winrt_mixinmethod
    def get_OutgoingConnections(self: win32more.Windows.Media.Audio.IAudioInputNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Audio.AudioGraphConnection]: ...
    @winrt_mixinmethod
    def AddOutgoingConnection(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def AddOutgoingConnectionWithGain(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode, gain: Double) -> Void: ...
    @winrt_mixinmethod
    def RemoveOutgoingConnection(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def get_EffectDefinitions(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    @winrt_mixinmethod
    def put_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode) -> Double: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode) -> Boolean: ...
    @winrt_mixinmethod
    def put_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def DisableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def EnableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_Emitter(self: win32more.Windows.Media.Audio.IAudioInputNode2) -> win32more.Windows.Media.Audio.AudioNodeEmitter: ...
    OutgoingConnections = property(get_OutgoingConnections, None)
    EffectDefinitions = property(get_EffectDefinitions, None)
    OutgoingGain = property(get_OutgoingGain, put_OutgoingGain)
    EncodingProperties = property(get_EncodingProperties, None)
    ConsumeInput = property(get_ConsumeInput, put_ConsumeInput)
    Emitter = property(get_Emitter, None)
class CreateAudioDeviceInputNodeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.ICreateAudioDeviceInputNodeResult
    _classid_ = 'Windows.Media.Audio.CreateAudioDeviceInputNodeResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Audio.ICreateAudioDeviceInputNodeResult) -> win32more.Windows.Media.Audio.AudioDeviceNodeCreationStatus: ...
    @winrt_mixinmethod
    def get_DeviceInputNode(self: win32more.Windows.Media.Audio.ICreateAudioDeviceInputNodeResult) -> win32more.Windows.Media.Audio.AudioDeviceInputNode: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Audio.ICreateAudioDeviceInputNodeResult2) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    DeviceInputNode = property(get_DeviceInputNode, None)
    ExtendedError = property(get_ExtendedError, None)
class CreateAudioDeviceOutputNodeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.ICreateAudioDeviceOutputNodeResult
    _classid_ = 'Windows.Media.Audio.CreateAudioDeviceOutputNodeResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Audio.ICreateAudioDeviceOutputNodeResult) -> win32more.Windows.Media.Audio.AudioDeviceNodeCreationStatus: ...
    @winrt_mixinmethod
    def get_DeviceOutputNode(self: win32more.Windows.Media.Audio.ICreateAudioDeviceOutputNodeResult) -> win32more.Windows.Media.Audio.AudioDeviceOutputNode: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Audio.ICreateAudioDeviceOutputNodeResult2) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    DeviceOutputNode = property(get_DeviceOutputNode, None)
    ExtendedError = property(get_ExtendedError, None)
class CreateAudioFileInputNodeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.ICreateAudioFileInputNodeResult
    _classid_ = 'Windows.Media.Audio.CreateAudioFileInputNodeResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Audio.ICreateAudioFileInputNodeResult) -> win32more.Windows.Media.Audio.AudioFileNodeCreationStatus: ...
    @winrt_mixinmethod
    def get_FileInputNode(self: win32more.Windows.Media.Audio.ICreateAudioFileInputNodeResult) -> win32more.Windows.Media.Audio.AudioFileInputNode: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Audio.ICreateAudioFileInputNodeResult2) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    FileInputNode = property(get_FileInputNode, None)
    ExtendedError = property(get_ExtendedError, None)
class CreateAudioFileOutputNodeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.ICreateAudioFileOutputNodeResult
    _classid_ = 'Windows.Media.Audio.CreateAudioFileOutputNodeResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Audio.ICreateAudioFileOutputNodeResult) -> win32more.Windows.Media.Audio.AudioFileNodeCreationStatus: ...
    @winrt_mixinmethod
    def get_FileOutputNode(self: win32more.Windows.Media.Audio.ICreateAudioFileOutputNodeResult) -> win32more.Windows.Media.Audio.AudioFileOutputNode: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Audio.ICreateAudioFileOutputNodeResult2) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    FileOutputNode = property(get_FileOutputNode, None)
    ExtendedError = property(get_ExtendedError, None)
class CreateAudioGraphResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.ICreateAudioGraphResult
    _classid_ = 'Windows.Media.Audio.CreateAudioGraphResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Audio.ICreateAudioGraphResult) -> win32more.Windows.Media.Audio.AudioGraphCreationStatus: ...
    @winrt_mixinmethod
    def get_Graph(self: win32more.Windows.Media.Audio.ICreateAudioGraphResult) -> win32more.Windows.Media.Audio.AudioGraph: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Audio.ICreateAudioGraphResult2) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    Graph = property(get_Graph, None)
    ExtendedError = property(get_ExtendedError, None)
class CreateMediaSourceAudioInputNodeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.ICreateMediaSourceAudioInputNodeResult
    _classid_ = 'Windows.Media.Audio.CreateMediaSourceAudioInputNodeResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Audio.ICreateMediaSourceAudioInputNodeResult) -> win32more.Windows.Media.Audio.MediaSourceAudioInputNodeCreationStatus: ...
    @winrt_mixinmethod
    def get_Node(self: win32more.Windows.Media.Audio.ICreateMediaSourceAudioInputNodeResult) -> win32more.Windows.Media.Audio.MediaSourceAudioInputNode: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Audio.ICreateMediaSourceAudioInputNodeResult2) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    Node = property(get_Node, None)
    ExtendedError = property(get_ExtendedError, None)
class EchoEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IEchoEffectDefinition
    _classid_ = 'Windows.Media.Audio.EchoEffectDefinition'
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Audio.IEchoEffectDefinitionFactory, audioGraph: win32more.Windows.Media.Audio.AudioGraph) -> win32more.Windows.Media.Audio.EchoEffectDefinition: ...
    @winrt_mixinmethod
    def put_WetDryMix(self: win32more.Windows.Media.Audio.IEchoEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_WetDryMix(self: win32more.Windows.Media.Audio.IEchoEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def put_Feedback(self: win32more.Windows.Media.Audio.IEchoEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Feedback(self: win32more.Windows.Media.Audio.IEchoEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def put_Delay(self: win32more.Windows.Media.Audio.IEchoEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Delay(self: win32more.Windows.Media.Audio.IEchoEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    WetDryMix = property(get_WetDryMix, put_WetDryMix)
    Feedback = property(get_Feedback, put_Feedback)
    Delay = property(get_Delay, put_Delay)
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class EqualizerBand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IEqualizerBand
    _classid_ = 'Windows.Media.Audio.EqualizerBand'
    @winrt_mixinmethod
    def get_Bandwidth(self: win32more.Windows.Media.Audio.IEqualizerBand) -> Double: ...
    @winrt_mixinmethod
    def put_Bandwidth(self: win32more.Windows.Media.Audio.IEqualizerBand, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FrequencyCenter(self: win32more.Windows.Media.Audio.IEqualizerBand) -> Double: ...
    @winrt_mixinmethod
    def put_FrequencyCenter(self: win32more.Windows.Media.Audio.IEqualizerBand, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Gain(self: win32more.Windows.Media.Audio.IEqualizerBand) -> Double: ...
    @winrt_mixinmethod
    def put_Gain(self: win32more.Windows.Media.Audio.IEqualizerBand, value: Double) -> Void: ...
    Bandwidth = property(get_Bandwidth, put_Bandwidth)
    FrequencyCenter = property(get_FrequencyCenter, put_FrequencyCenter)
    Gain = property(get_Gain, put_Gain)
class EqualizerEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IEqualizerEffectDefinition
    _classid_ = 'Windows.Media.Audio.EqualizerEffectDefinition'
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Audio.IEqualizerEffectDefinitionFactory, audioGraph: win32more.Windows.Media.Audio.AudioGraph) -> win32more.Windows.Media.Audio.EqualizerEffectDefinition: ...
    @winrt_mixinmethod
    def get_Bands(self: win32more.Windows.Media.Audio.IEqualizerEffectDefinition) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Audio.EqualizerBand]: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    Bands = property(get_Bands, None)
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class FrameInputNodeQuantumStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IFrameInputNodeQuantumStartedEventArgs
    _classid_ = 'Windows.Media.Audio.FrameInputNodeQuantumStartedEventArgs'
    @winrt_mixinmethod
    def get_RequiredSamples(self: win32more.Windows.Media.Audio.IFrameInputNodeQuantumStartedEventArgs) -> Int32: ...
    RequiredSamples = property(get_RequiredSamples, None)
class IAudioDeviceInputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioDeviceInputNode'
    _iid_ = Guid('{b01b6be1-6f4e-49e2-ac01-559d62beb3a9}')
    @winrt_commethod(6)
    def get_Device(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    Device = property(get_Device, None)
class IAudioDeviceOutputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioDeviceOutputNode'
    _iid_ = Guid('{362edbff-ff1c-4434-9e0f-bd2ef522ac82}')
    @winrt_commethod(6)
    def get_Device(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    Device = property(get_Device, None)
class IAudioFileInputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioFileInputNode'
    _iid_ = Guid('{905b67c8-6f65-4cd4-8890-4694843c276d}')
    @winrt_commethod(6)
    def put_PlaybackSpeedFactor(self, value: Double) -> Void: ...
    @winrt_commethod(7)
    def get_PlaybackSpeedFactor(self) -> Double: ...
    @winrt_commethod(8)
    def get_Position(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def Seek(self, position: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_StartTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(11)
    def put_StartTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(12)
    def get_EndTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(13)
    def put_EndTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(14)
    def get_LoopCount(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(15)
    def put_LoopCount(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(16)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(17)
    def get_SourceFile(self) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_commethod(18)
    def add_FileCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioFileInputNode, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_FileCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PlaybackSpeedFactor = property(get_PlaybackSpeedFactor, put_PlaybackSpeedFactor)
    Position = property(get_Position, None)
    StartTime = property(get_StartTime, put_StartTime)
    EndTime = property(get_EndTime, put_EndTime)
    LoopCount = property(get_LoopCount, put_LoopCount)
    Duration = property(get_Duration, None)
    SourceFile = property(get_SourceFile, None)
class IAudioFileOutputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioFileOutputNode'
    _iid_ = Guid('{50e01980-5166-4093-80f8-ada00089e9cf}')
    @winrt_commethod(6)
    def get_File(self) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_commethod(7)
    def get_FileEncodingProfile(self) -> win32more.Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_commethod(8)
    def FinalizeAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Transcoding.TranscodeFailureReason]: ...
    File = property(get_File, None)
    FileEncodingProfile = property(get_FileEncodingProfile, None)
class IAudioFrameCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioFrameCompletedEventArgs'
    _iid_ = Guid('{dc7c829e-0208-4504-a5a8-f0f268920a65}')
    @winrt_commethod(6)
    def get_Frame(self) -> win32more.Windows.Media.AudioFrame: ...
    Frame = property(get_Frame, None)
class IAudioFrameInputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioFrameInputNode'
    _iid_ = Guid('{01b266c7-fd96-4ff5-a3c5-d27a9bf44237}')
    @winrt_commethod(6)
    def put_PlaybackSpeedFactor(self, value: Double) -> Void: ...
    @winrt_commethod(7)
    def get_PlaybackSpeedFactor(self) -> Double: ...
    @winrt_commethod(8)
    def AddFrame(self, frame: win32more.Windows.Media.AudioFrame) -> Void: ...
    @winrt_commethod(9)
    def DiscardQueuedFrames(self) -> Void: ...
    @winrt_commethod(10)
    def get_QueuedSampleCount(self) -> UInt64: ...
    @winrt_commethod(11)
    def add_AudioFrameCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioFrameInputNode, win32more.Windows.Media.Audio.AudioFrameCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_AudioFrameCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_QuantumStarted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioFrameInputNode, win32more.Windows.Media.Audio.FrameInputNodeQuantumStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_QuantumStarted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PlaybackSpeedFactor = property(get_PlaybackSpeedFactor, put_PlaybackSpeedFactor)
    QueuedSampleCount = property(get_QueuedSampleCount, None)
class IAudioFrameOutputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioFrameOutputNode'
    _iid_ = Guid('{b847371b-3299-45f5-88b3-c9d12a3f1cc8}')
    @winrt_commethod(6)
    def GetFrame(self) -> win32more.Windows.Media.AudioFrame: ...
class IAudioGraph(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioGraph'
    _iid_ = Guid('{1ad46eed-e48c-4e14-9660-2c4f83e9cdd8}')
    @winrt_commethod(6)
    def CreateFrameInputNode(self) -> win32more.Windows.Media.Audio.AudioFrameInputNode: ...
    @winrt_commethod(7)
    def CreateFrameInputNodeWithFormat(self, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> win32more.Windows.Media.Audio.AudioFrameInputNode: ...
    @winrt_commethod(8)
    def CreateDeviceInputNodeAsync(self, category: win32more.Windows.Media.Capture.MediaCategory) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioDeviceInputNodeResult]: ...
    @winrt_commethod(9)
    def CreateDeviceInputNodeWithFormatAsync(self, category: win32more.Windows.Media.Capture.MediaCategory, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioDeviceInputNodeResult]: ...
    @winrt_commethod(10)
    def CreateDeviceInputNodeWithFormatOnDeviceAsync(self, category: win32more.Windows.Media.Capture.MediaCategory, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties, device: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioDeviceInputNodeResult]: ...
    @winrt_commethod(11)
    def CreateFrameOutputNode(self) -> win32more.Windows.Media.Audio.AudioFrameOutputNode: ...
    @winrt_commethod(12)
    def CreateFrameOutputNodeWithFormat(self, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> win32more.Windows.Media.Audio.AudioFrameOutputNode: ...
    @winrt_commethod(13)
    def CreateDeviceOutputNodeAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioDeviceOutputNodeResult]: ...
    @winrt_commethod(14)
    def CreateFileInputNodeAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioFileInputNodeResult]: ...
    @winrt_commethod(15)
    def CreateFileOutputNodeAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioFileOutputNodeResult]: ...
    @winrt_commethod(16)
    def CreateFileOutputNodeWithFileProfileAsync(self, file: win32more.Windows.Storage.IStorageFile, fileEncodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioFileOutputNodeResult]: ...
    @winrt_commethod(17)
    def CreateSubmixNode(self) -> win32more.Windows.Media.Audio.AudioSubmixNode: ...
    @winrt_commethod(18)
    def CreateSubmixNodeWithFormat(self, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> win32more.Windows.Media.Audio.AudioSubmixNode: ...
    @winrt_commethod(19)
    def Start(self) -> Void: ...
    @winrt_commethod(20)
    def Stop(self) -> Void: ...
    @winrt_commethod(21)
    def ResetAllNodes(self) -> Void: ...
    @winrt_commethod(22)
    def add_QuantumStarted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioGraph, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_QuantumStarted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_QuantumProcessed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioGraph, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_QuantumProcessed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def add_UnrecoverableErrorOccurred(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioGraph, win32more.Windows.Media.Audio.AudioGraphUnrecoverableErrorOccurredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_UnrecoverableErrorOccurred(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def get_CompletedQuantumCount(self) -> UInt64: ...
    @winrt_commethod(29)
    def get_EncodingProperties(self) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(30)
    def get_LatencyInSamples(self) -> Int32: ...
    @winrt_commethod(31)
    def get_PrimaryRenderDevice(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(32)
    def get_RenderDeviceAudioProcessing(self) -> win32more.Windows.Media.AudioProcessing: ...
    @winrt_commethod(33)
    def get_SamplesPerQuantum(self) -> Int32: ...
    CompletedQuantumCount = property(get_CompletedQuantumCount, None)
    EncodingProperties = property(get_EncodingProperties, None)
    LatencyInSamples = property(get_LatencyInSamples, None)
    PrimaryRenderDevice = property(get_PrimaryRenderDevice, None)
    RenderDeviceAudioProcessing = property(get_RenderDeviceAudioProcessing, None)
    SamplesPerQuantum = property(get_SamplesPerQuantum, None)
class IAudioGraph2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioGraph2'
    _iid_ = Guid('{4e4c3bd5-4fc1-45f6-a947-3cd38f4fd839}')
    @winrt_commethod(6)
    def CreateFrameInputNodeWithFormatAndEmitter(self, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties, emitter: win32more.Windows.Media.Audio.AudioNodeEmitter) -> win32more.Windows.Media.Audio.AudioFrameInputNode: ...
    @winrt_commethod(7)
    def CreateDeviceInputNodeWithFormatAndEmitterOnDeviceAsync(self, category: win32more.Windows.Media.Capture.MediaCategory, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties, device: win32more.Windows.Devices.Enumeration.DeviceInformation, emitter: win32more.Windows.Media.Audio.AudioNodeEmitter) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioDeviceInputNodeResult]: ...
    @winrt_commethod(8)
    def CreateFileInputNodeWithEmitterAsync(self, file: win32more.Windows.Storage.IStorageFile, emitter: win32more.Windows.Media.Audio.AudioNodeEmitter) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioFileInputNodeResult]: ...
    @winrt_commethod(9)
    def CreateSubmixNodeWithFormatAndEmitter(self, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties, emitter: win32more.Windows.Media.Audio.AudioNodeEmitter) -> win32more.Windows.Media.Audio.AudioSubmixNode: ...
    @winrt_commethod(10)
    def CreateBatchUpdater(self) -> win32more.Windows.Media.Audio.AudioGraphBatchUpdater: ...
class IAudioGraph3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioGraph3'
    _iid_ = Guid('{ddcd25ae-1185-42a7-831d-6a9b0fc86820}')
    @winrt_commethod(6)
    def CreateMediaSourceAudioInputNodeAsync(self, mediaSource: win32more.Windows.Media.Core.MediaSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateMediaSourceAudioInputNodeResult]: ...
    @winrt_commethod(7)
    def CreateMediaSourceAudioInputNodeWithEmitterAsync(self, mediaSource: win32more.Windows.Media.Core.MediaSource, emitter: win32more.Windows.Media.Audio.AudioNodeEmitter) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateMediaSourceAudioInputNodeResult]: ...
class IAudioGraphConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioGraphConnection'
    _iid_ = Guid('{763070ed-d04e-4fac-b233-600b42edd469}')
    @winrt_commethod(6)
    def get_Destination(self) -> win32more.Windows.Media.Audio.IAudioNode: ...
    @winrt_commethod(7)
    def put_Gain(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_Gain(self) -> Double: ...
    Destination = property(get_Destination, None)
    Gain = property(get_Gain, put_Gain)
class IAudioGraphSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioGraphSettings'
    _iid_ = Guid('{1d59647f-e6fe-4628-84f8-9d8bdba25785}')
    @winrt_commethod(6)
    def get_EncodingProperties(self) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(7)
    def put_EncodingProperties(self, value: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> Void: ...
    @winrt_commethod(8)
    def get_PrimaryRenderDevice(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(9)
    def put_PrimaryRenderDevice(self, value: win32more.Windows.Devices.Enumeration.DeviceInformation) -> Void: ...
    @winrt_commethod(10)
    def get_QuantumSizeSelectionMode(self) -> win32more.Windows.Media.Audio.QuantumSizeSelectionMode: ...
    @winrt_commethod(11)
    def put_QuantumSizeSelectionMode(self, value: win32more.Windows.Media.Audio.QuantumSizeSelectionMode) -> Void: ...
    @winrt_commethod(12)
    def get_DesiredSamplesPerQuantum(self) -> Int32: ...
    @winrt_commethod(13)
    def put_DesiredSamplesPerQuantum(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_AudioRenderCategory(self) -> win32more.Windows.Media.Render.AudioRenderCategory: ...
    @winrt_commethod(15)
    def put_AudioRenderCategory(self, value: win32more.Windows.Media.Render.AudioRenderCategory) -> Void: ...
    @winrt_commethod(16)
    def get_DesiredRenderDeviceAudioProcessing(self) -> win32more.Windows.Media.AudioProcessing: ...
    @winrt_commethod(17)
    def put_DesiredRenderDeviceAudioProcessing(self, value: win32more.Windows.Media.AudioProcessing) -> Void: ...
    EncodingProperties = property(get_EncodingProperties, put_EncodingProperties)
    PrimaryRenderDevice = property(get_PrimaryRenderDevice, put_PrimaryRenderDevice)
    QuantumSizeSelectionMode = property(get_QuantumSizeSelectionMode, put_QuantumSizeSelectionMode)
    DesiredSamplesPerQuantum = property(get_DesiredSamplesPerQuantum, put_DesiredSamplesPerQuantum)
    AudioRenderCategory = property(get_AudioRenderCategory, put_AudioRenderCategory)
    DesiredRenderDeviceAudioProcessing = property(get_DesiredRenderDeviceAudioProcessing, put_DesiredRenderDeviceAudioProcessing)
class IAudioGraphSettings2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioGraphSettings2'
    _iid_ = Guid('{72919787-4dab-46e3-b4c9-d8e1a2636062}')
    @winrt_commethod(6)
    def put_MaxPlaybackSpeedFactor(self, value: Double) -> Void: ...
    @winrt_commethod(7)
    def get_MaxPlaybackSpeedFactor(self) -> Double: ...
    MaxPlaybackSpeedFactor = property(get_MaxPlaybackSpeedFactor, put_MaxPlaybackSpeedFactor)
class IAudioGraphSettingsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioGraphSettingsFactory'
    _iid_ = Guid('{a5d91cc6-c2eb-4a61-a214-1d66d75f83da}')
    @winrt_commethod(6)
    def Create(self, audioRenderCategory: win32more.Windows.Media.Render.AudioRenderCategory) -> win32more.Windows.Media.Audio.AudioGraphSettings: ...
class IAudioGraphStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioGraphStatics'
    _iid_ = Guid('{76ec3132-e159-4ab7-a82a-17beb4b31e94}')
    @winrt_commethod(6)
    def CreateAsync(self, settings: win32more.Windows.Media.Audio.AudioGraphSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.CreateAudioGraphResult]: ...
class IAudioGraphUnrecoverableErrorOccurredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioGraphUnrecoverableErrorOccurredEventArgs'
    _iid_ = Guid('{c3d9cbe0-3ff6-4fb3-b262-50d435c55423}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Media.Audio.AudioGraphUnrecoverableError: ...
    Error = property(get_Error, None)
class IAudioInputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioInputNode'
    _iid_ = Guid('{d148005c-8428-4784-b7fd-a99d468c5d20}')
    @winrt_commethod(6)
    def get_OutgoingConnections(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Audio.AudioGraphConnection]: ...
    @winrt_commethod(7)
    def AddOutgoingConnection(self, destination: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_commethod(8)
    def AddOutgoingConnectionWithGain(self, destination: win32more.Windows.Media.Audio.IAudioNode, gain: Double) -> Void: ...
    @winrt_commethod(9)
    def RemoveOutgoingConnection(self, destination: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    OutgoingConnections = property(get_OutgoingConnections, None)
class IAudioInputNode2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioInputNode2'
    _iid_ = Guid('{905156b7-ca68-4c6d-a8bc-e3ee17fe3fd2}')
    @winrt_commethod(6)
    def get_Emitter(self) -> win32more.Windows.Media.Audio.AudioNodeEmitter: ...
    Emitter = property(get_Emitter, None)
class IAudioNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioNode'
    _iid_ = Guid('{15389d7f-dbd8-4819-bf03-668e9357cd6d}')
    @winrt_commethod(6)
    def get_EffectDefinitions(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    @winrt_commethod(7)
    def put_OutgoingGain(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_OutgoingGain(self) -> Double: ...
    @winrt_commethod(9)
    def get_EncodingProperties(self) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(10)
    def get_ConsumeInput(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_ConsumeInput(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def Start(self) -> Void: ...
    @winrt_commethod(13)
    def Stop(self) -> Void: ...
    @winrt_commethod(14)
    def Reset(self) -> Void: ...
    @winrt_commethod(15)
    def DisableEffectsByDefinition(self, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_commethod(16)
    def EnableEffectsByDefinition(self, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    EffectDefinitions = property(get_EffectDefinitions, None)
    OutgoingGain = property(get_OutgoingGain, put_OutgoingGain)
    EncodingProperties = property(get_EncodingProperties, None)
    ConsumeInput = property(get_ConsumeInput, put_ConsumeInput)
class IAudioNodeEmitter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioNodeEmitter'
    _iid_ = Guid('{3676971d-880a-47b8-adf7-1323a9d965be}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def put_Position(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(8)
    def get_Direction(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def put_Direction(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(10)
    def get_Shape(self) -> win32more.Windows.Media.Audio.AudioNodeEmitterShape: ...
    @winrt_commethod(11)
    def get_DecayModel(self) -> win32more.Windows.Media.Audio.AudioNodeEmitterDecayModel: ...
    @winrt_commethod(12)
    def get_Gain(self) -> Double: ...
    @winrt_commethod(13)
    def put_Gain(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_DistanceScale(self) -> Double: ...
    @winrt_commethod(15)
    def put_DistanceScale(self, value: Double) -> Void: ...
    @winrt_commethod(16)
    def get_DopplerScale(self) -> Double: ...
    @winrt_commethod(17)
    def put_DopplerScale(self, value: Double) -> Void: ...
    @winrt_commethod(18)
    def get_DopplerVelocity(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(19)
    def put_DopplerVelocity(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(20)
    def get_IsDopplerDisabled(self) -> Boolean: ...
    Position = property(get_Position, put_Position)
    Direction = property(get_Direction, put_Direction)
    Shape = property(get_Shape, None)
    DecayModel = property(get_DecayModel, None)
    Gain = property(get_Gain, put_Gain)
    DistanceScale = property(get_DistanceScale, put_DistanceScale)
    DopplerScale = property(get_DopplerScale, put_DopplerScale)
    DopplerVelocity = property(get_DopplerVelocity, put_DopplerVelocity)
    IsDopplerDisabled = property(get_IsDopplerDisabled, None)
class IAudioNodeEmitter2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioNodeEmitter2'
    _iid_ = Guid('{4ab6eecb-ec29-47f8-818c-b6b660a5aeb1}')
    @winrt_commethod(6)
    def get_SpatialAudioModel(self) -> win32more.Windows.Media.Audio.SpatialAudioModel: ...
    @winrt_commethod(7)
    def put_SpatialAudioModel(self, value: win32more.Windows.Media.Audio.SpatialAudioModel) -> Void: ...
    SpatialAudioModel = property(get_SpatialAudioModel, put_SpatialAudioModel)
class IAudioNodeEmitterConeProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioNodeEmitterConeProperties'
    _iid_ = Guid('{e99b2cee-02ca-4375-9326-0c6ae4bcdfb5}')
    @winrt_commethod(6)
    def get_InnerAngle(self) -> Double: ...
    @winrt_commethod(7)
    def get_OuterAngle(self) -> Double: ...
    @winrt_commethod(8)
    def get_OuterAngleGain(self) -> Double: ...
    InnerAngle = property(get_InnerAngle, None)
    OuterAngle = property(get_OuterAngle, None)
    OuterAngleGain = property(get_OuterAngleGain, None)
class IAudioNodeEmitterDecayModel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioNodeEmitterDecayModel'
    _iid_ = Guid('{1d1d5af7-0d53-4fa9-bd84-d5816a86f3ff}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.Media.Audio.AudioNodeEmitterDecayKind: ...
    @winrt_commethod(7)
    def get_MinGain(self) -> Double: ...
    @winrt_commethod(8)
    def get_MaxGain(self) -> Double: ...
    @winrt_commethod(9)
    def get_NaturalProperties(self) -> win32more.Windows.Media.Audio.AudioNodeEmitterNaturalDecayModelProperties: ...
    Kind = property(get_Kind, None)
    MinGain = property(get_MinGain, None)
    MaxGain = property(get_MaxGain, None)
    NaturalProperties = property(get_NaturalProperties, None)
class IAudioNodeEmitterDecayModelStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioNodeEmitterDecayModelStatics'
    _iid_ = Guid('{c7787ca8-f178-462f-bc81-8dd5cbe5dae8}')
    @winrt_commethod(6)
    def CreateNatural(self, minGain: Double, maxGain: Double, unityGainDistance: Double, cutoffDistance: Double) -> win32more.Windows.Media.Audio.AudioNodeEmitterDecayModel: ...
    @winrt_commethod(7)
    def CreateCustom(self, minGain: Double, maxGain: Double) -> win32more.Windows.Media.Audio.AudioNodeEmitterDecayModel: ...
class IAudioNodeEmitterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioNodeEmitterFactory'
    _iid_ = Guid('{fdc8489a-6ad6-4ce4-b7f7-a99370df7ee9}')
    @winrt_commethod(6)
    def CreateAudioNodeEmitter(self, shape: win32more.Windows.Media.Audio.AudioNodeEmitterShape, decayModel: win32more.Windows.Media.Audio.AudioNodeEmitterDecayModel, settings: win32more.Windows.Media.Audio.AudioNodeEmitterSettings) -> win32more.Windows.Media.Audio.AudioNodeEmitter: ...
class IAudioNodeEmitterNaturalDecayModelProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioNodeEmitterNaturalDecayModelProperties'
    _iid_ = Guid('{48934bcf-cf2c-4efc-9331-75bd22df1f0c}')
    @winrt_commethod(6)
    def get_UnityGainDistance(self) -> Double: ...
    @winrt_commethod(7)
    def get_CutoffDistance(self) -> Double: ...
    UnityGainDistance = property(get_UnityGainDistance, None)
    CutoffDistance = property(get_CutoffDistance, None)
class IAudioNodeEmitterShape(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioNodeEmitterShape'
    _iid_ = Guid('{ea0311c5-e73d-44bc-859c-45553bbc4828}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.Media.Audio.AudioNodeEmitterShapeKind: ...
    @winrt_commethod(7)
    def get_ConeProperties(self) -> win32more.Windows.Media.Audio.AudioNodeEmitterConeProperties: ...
    Kind = property(get_Kind, None)
    ConeProperties = property(get_ConeProperties, None)
class IAudioNodeEmitterShapeStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioNodeEmitterShapeStatics'
    _iid_ = Guid('{57bb2771-ffa5-4b86-a779-e264aeb9145f}')
    @winrt_commethod(6)
    def CreateCone(self, innerAngle: Double, outerAngle: Double, outerAngleGain: Double) -> win32more.Windows.Media.Audio.AudioNodeEmitterShape: ...
    @winrt_commethod(7)
    def CreateOmnidirectional(self) -> win32more.Windows.Media.Audio.AudioNodeEmitterShape: ...
class IAudioNodeListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioNodeListener'
    _iid_ = Guid('{d9722e16-0c0a-41da-b755-6c77835fb1eb}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def put_Position(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(8)
    def get_Orientation(self) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(9)
    def put_Orientation(self, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(10)
    def get_SpeedOfSound(self) -> Double: ...
    @winrt_commethod(11)
    def put_SpeedOfSound(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_DopplerVelocity(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(13)
    def put_DopplerVelocity(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    Position = property(get_Position, put_Position)
    Orientation = property(get_Orientation, put_Orientation)
    SpeedOfSound = property(get_SpeedOfSound, put_SpeedOfSound)
    DopplerVelocity = property(get_DopplerVelocity, put_DopplerVelocity)
class IAudioNodeWithListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioNodeWithListener'
    _iid_ = Guid('{0e0f907c-79ff-4544-9eeb-01257b15105a}')
    @winrt_commethod(6)
    def put_Listener(self, value: win32more.Windows.Media.Audio.AudioNodeListener) -> Void: ...
    @winrt_commethod(7)
    def get_Listener(self) -> win32more.Windows.Media.Audio.AudioNodeListener: ...
    Listener = property(get_Listener, put_Listener)
class IAudioPlaybackConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioPlaybackConnection'
    _iid_ = Guid('{1a4c1dea-cafc-50e7-8718-ea3f81cbfa51}')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_State(self) -> win32more.Windows.Media.Audio.AudioPlaybackConnectionState: ...
    @winrt_commethod(10)
    def Open(self) -> win32more.Windows.Media.Audio.AudioPlaybackConnectionOpenResult: ...
    @winrt_commethod(11)
    def OpenAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.AudioPlaybackConnectionOpenResult]: ...
    @winrt_commethod(12)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioPlaybackConnection, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    State = property(get_State, None)
class IAudioPlaybackConnectionOpenResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioPlaybackConnectionOpenResult'
    _iid_ = Guid('{4e656aef-39f9-5fc9-a519-a5bbfd9fe921}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Audio.AudioPlaybackConnectionOpenResultStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
class IAudioPlaybackConnectionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioPlaybackConnectionStatics'
    _iid_ = Guid('{e60963a2-69e6-5ffc-9e13-824a85213daf}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def TryCreateFromId(self, id: WinRT_String) -> win32more.Windows.Media.Audio.AudioPlaybackConnection: ...
class IAudioStateMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioStateMonitor'
    _iid_ = Guid('{1d13d136-0199-4cdc-b84e-e72c2b581ece}')
    @winrt_commethod(6)
    def add_SoundLevelChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.AudioStateMonitor, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SoundLevelChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_SoundLevel(self) -> win32more.Windows.Media.SoundLevel: ...
    SoundLevel = property(get_SoundLevel, None)
class IAudioStateMonitorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IAudioStateMonitorStatics'
    _iid_ = Guid('{6374ea4c-1b3b-4001-94d9-dd225330fa40}')
    @winrt_commethod(6)
    def CreateForRenderMonitoring(self) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_commethod(7)
    def CreateForRenderMonitoringWithCategory(self, category: win32more.Windows.Media.Render.AudioRenderCategory) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_commethod(8)
    def CreateForRenderMonitoringWithCategoryAndDeviceRole(self, category: win32more.Windows.Media.Render.AudioRenderCategory, role: win32more.Windows.Media.Devices.AudioDeviceRole) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_commethod(9)
    def CreateForRenderMonitoringWithCategoryAndDeviceId(self, category: win32more.Windows.Media.Render.AudioRenderCategory, deviceId: WinRT_String) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_commethod(10)
    def CreateForCaptureMonitoring(self) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_commethod(11)
    def CreateForCaptureMonitoringWithCategory(self, category: win32more.Windows.Media.Capture.MediaCategory) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_commethod(12)
    def CreateForCaptureMonitoringWithCategoryAndDeviceRole(self, category: win32more.Windows.Media.Capture.MediaCategory, role: win32more.Windows.Media.Devices.AudioDeviceRole) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
    @winrt_commethod(13)
    def CreateForCaptureMonitoringWithCategoryAndDeviceId(self, category: win32more.Windows.Media.Capture.MediaCategory, deviceId: WinRT_String) -> win32more.Windows.Media.Audio.AudioStateMonitor: ...
class ICreateAudioDeviceInputNodeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ICreateAudioDeviceInputNodeResult'
    _iid_ = Guid('{16eec7a8-1ca7-40ef-91a4-d346e0aa1bba}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Audio.AudioDeviceNodeCreationStatus: ...
    @winrt_commethod(7)
    def get_DeviceInputNode(self) -> win32more.Windows.Media.Audio.AudioDeviceInputNode: ...
    Status = property(get_Status, None)
    DeviceInputNode = property(get_DeviceInputNode, None)
class ICreateAudioDeviceInputNodeResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ICreateAudioDeviceInputNodeResult2'
    _iid_ = Guid('{921c69ce-3f35-41c7-9622-79f608baedc2}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class ICreateAudioDeviceOutputNodeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ICreateAudioDeviceOutputNodeResult'
    _iid_ = Guid('{f7776d27-1d9a-47f7-9cd4-2859cc1b7bff}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Audio.AudioDeviceNodeCreationStatus: ...
    @winrt_commethod(7)
    def get_DeviceOutputNode(self) -> win32more.Windows.Media.Audio.AudioDeviceOutputNode: ...
    Status = property(get_Status, None)
    DeviceOutputNode = property(get_DeviceOutputNode, None)
class ICreateAudioDeviceOutputNodeResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ICreateAudioDeviceOutputNodeResult2'
    _iid_ = Guid('{4864269f-bdce-4ab1-bd38-fbae93aedaca}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class ICreateAudioFileInputNodeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ICreateAudioFileInputNodeResult'
    _iid_ = Guid('{ce83d61c-e297-4c50-9ce7-1c7a69d6bd09}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Audio.AudioFileNodeCreationStatus: ...
    @winrt_commethod(7)
    def get_FileInputNode(self) -> win32more.Windows.Media.Audio.AudioFileInputNode: ...
    Status = property(get_Status, None)
    FileInputNode = property(get_FileInputNode, None)
class ICreateAudioFileInputNodeResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ICreateAudioFileInputNodeResult2'
    _iid_ = Guid('{f9082020-3d80-4fe0-81c1-768fea7ca7e0}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class ICreateAudioFileOutputNodeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ICreateAudioFileOutputNodeResult'
    _iid_ = Guid('{47d6ba7b-e909-453f-866e-5540cda734ff}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Audio.AudioFileNodeCreationStatus: ...
    @winrt_commethod(7)
    def get_FileOutputNode(self) -> win32more.Windows.Media.Audio.AudioFileOutputNode: ...
    Status = property(get_Status, None)
    FileOutputNode = property(get_FileOutputNode, None)
class ICreateAudioFileOutputNodeResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ICreateAudioFileOutputNodeResult2'
    _iid_ = Guid('{9f01b50d-3318-47b3-a60a-1b492be7fc0d}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class ICreateAudioGraphResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ICreateAudioGraphResult'
    _iid_ = Guid('{5453ef7e-7bde-4b76-bb5d-48f79cfc8c0b}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Audio.AudioGraphCreationStatus: ...
    @winrt_commethod(7)
    def get_Graph(self) -> win32more.Windows.Media.Audio.AudioGraph: ...
    Status = property(get_Status, None)
    Graph = property(get_Graph, None)
class ICreateAudioGraphResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ICreateAudioGraphResult2'
    _iid_ = Guid('{6d738dfc-88c6-4fcb-a534-85cedd4050a1}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class ICreateMediaSourceAudioInputNodeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ICreateMediaSourceAudioInputNodeResult'
    _iid_ = Guid('{46a658a3-53c0-4d59-9e51-cc1d1044a4c4}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Audio.MediaSourceAudioInputNodeCreationStatus: ...
    @winrt_commethod(7)
    def get_Node(self) -> win32more.Windows.Media.Audio.MediaSourceAudioInputNode: ...
    Status = property(get_Status, None)
    Node = property(get_Node, None)
class ICreateMediaSourceAudioInputNodeResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ICreateMediaSourceAudioInputNodeResult2'
    _iid_ = Guid('{63514ce8-6a1a-49e3-97ec-28fd5be114e5}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IEchoEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IEchoEffectDefinition'
    _iid_ = Guid('{0e4d3faa-36b8-4c91-b9da-11f44a8a6610}')
    @winrt_commethod(6)
    def put_WetDryMix(self, value: Double) -> Void: ...
    @winrt_commethod(7)
    def get_WetDryMix(self) -> Double: ...
    @winrt_commethod(8)
    def put_Feedback(self, value: Double) -> Void: ...
    @winrt_commethod(9)
    def get_Feedback(self) -> Double: ...
    @winrt_commethod(10)
    def put_Delay(self, value: Double) -> Void: ...
    @winrt_commethod(11)
    def get_Delay(self) -> Double: ...
    WetDryMix = property(get_WetDryMix, put_WetDryMix)
    Feedback = property(get_Feedback, put_Feedback)
    Delay = property(get_Delay, put_Delay)
class IEchoEffectDefinitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IEchoEffectDefinitionFactory'
    _iid_ = Guid('{0d4e2257-aaf2-4e86-a54c-fb79db8f6c12}')
    @winrt_commethod(6)
    def Create(self, audioGraph: win32more.Windows.Media.Audio.AudioGraph) -> win32more.Windows.Media.Audio.EchoEffectDefinition: ...
class IEqualizerBand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IEqualizerBand'
    _iid_ = Guid('{c00a5a6a-262d-4b85-9bb7-43280b62ed0c}')
    @winrt_commethod(6)
    def get_Bandwidth(self) -> Double: ...
    @winrt_commethod(7)
    def put_Bandwidth(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_FrequencyCenter(self) -> Double: ...
    @winrt_commethod(9)
    def put_FrequencyCenter(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_Gain(self) -> Double: ...
    @winrt_commethod(11)
    def put_Gain(self, value: Double) -> Void: ...
    Bandwidth = property(get_Bandwidth, put_Bandwidth)
    FrequencyCenter = property(get_FrequencyCenter, put_FrequencyCenter)
    Gain = property(get_Gain, put_Gain)
class IEqualizerEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IEqualizerEffectDefinition'
    _iid_ = Guid('{023f6f1f-83fe-449a-a822-c696442d16b0}')
    @winrt_commethod(6)
    def get_Bands(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Audio.EqualizerBand]: ...
    Bands = property(get_Bands, None)
class IEqualizerEffectDefinitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IEqualizerEffectDefinitionFactory'
    _iid_ = Guid('{d2876fc4-d410-4eb5-9e69-c9aa1277eaf0}')
    @winrt_commethod(6)
    def Create(self, audioGraph: win32more.Windows.Media.Audio.AudioGraph) -> win32more.Windows.Media.Audio.EqualizerEffectDefinition: ...
class IFrameInputNodeQuantumStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IFrameInputNodeQuantumStartedEventArgs'
    _iid_ = Guid('{3d9bd498-a306-4f06-bd9f-e9efc8226304}')
    @winrt_commethod(6)
    def get_RequiredSamples(self) -> Int32: ...
    RequiredSamples = property(get_RequiredSamples, None)
class ILimiterEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ILimiterEffectDefinition'
    _iid_ = Guid('{6b755d19-2603-47ba-bdeb-39055e3486dc}')
    @winrt_commethod(6)
    def put_Release(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_Release(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_Loudness(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_Loudness(self) -> UInt32: ...
    Release = property(get_Release, put_Release)
    Loudness = property(get_Loudness, put_Loudness)
class ILimiterEffectDefinitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ILimiterEffectDefinitionFactory'
    _iid_ = Guid('{ecbae6f1-61ff-45ef-b8f5-48659a57c72d}')
    @winrt_commethod(6)
    def Create(self, audioGraph: win32more.Windows.Media.Audio.AudioGraph) -> win32more.Windows.Media.Audio.LimiterEffectDefinition: ...
class IMediaSourceAudioInputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IMediaSourceAudioInputNode'
    _iid_ = Guid('{99d8983b-a88a-4041-8e4f-ddbac0c91fd3}')
    @winrt_commethod(6)
    def put_PlaybackSpeedFactor(self, value: Double) -> Void: ...
    @winrt_commethod(7)
    def get_PlaybackSpeedFactor(self) -> Double: ...
    @winrt_commethod(8)
    def get_Position(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def Seek(self, position: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_StartTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(11)
    def put_StartTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(12)
    def get_EndTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(13)
    def put_EndTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(14)
    def get_LoopCount(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(15)
    def put_LoopCount(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(16)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(17)
    def get_MediaSource(self) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_commethod(18)
    def add_MediaSourceCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.MediaSourceAudioInputNode, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_MediaSourceCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PlaybackSpeedFactor = property(get_PlaybackSpeedFactor, put_PlaybackSpeedFactor)
    Position = property(get_Position, None)
    StartTime = property(get_StartTime, put_StartTime)
    EndTime = property(get_EndTime, put_EndTime)
    LoopCount = property(get_LoopCount, put_LoopCount)
    Duration = property(get_Duration, None)
    MediaSource = property(get_MediaSource, None)
class IReverbEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IReverbEffectDefinition'
    _iid_ = Guid('{4606aa89-f563-4d0a-8f6e-f0cddff35d84}')
    @winrt_commethod(6)
    def put_WetDryMix(self, value: Double) -> Void: ...
    @winrt_commethod(7)
    def get_WetDryMix(self) -> Double: ...
    @winrt_commethod(8)
    def put_ReflectionsDelay(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_ReflectionsDelay(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_ReverbDelay(self, value: Byte) -> Void: ...
    @winrt_commethod(11)
    def get_ReverbDelay(self) -> Byte: ...
    @winrt_commethod(12)
    def put_RearDelay(self, value: Byte) -> Void: ...
    @winrt_commethod(13)
    def get_RearDelay(self) -> Byte: ...
    @winrt_commethod(14)
    def put_PositionLeft(self, value: Byte) -> Void: ...
    @winrt_commethod(15)
    def get_PositionLeft(self) -> Byte: ...
    @winrt_commethod(16)
    def put_PositionRight(self, value: Byte) -> Void: ...
    @winrt_commethod(17)
    def get_PositionRight(self) -> Byte: ...
    @winrt_commethod(18)
    def put_PositionMatrixLeft(self, value: Byte) -> Void: ...
    @winrt_commethod(19)
    def get_PositionMatrixLeft(self) -> Byte: ...
    @winrt_commethod(20)
    def put_PositionMatrixRight(self, value: Byte) -> Void: ...
    @winrt_commethod(21)
    def get_PositionMatrixRight(self) -> Byte: ...
    @winrt_commethod(22)
    def put_EarlyDiffusion(self, value: Byte) -> Void: ...
    @winrt_commethod(23)
    def get_EarlyDiffusion(self) -> Byte: ...
    @winrt_commethod(24)
    def put_LateDiffusion(self, value: Byte) -> Void: ...
    @winrt_commethod(25)
    def get_LateDiffusion(self) -> Byte: ...
    @winrt_commethod(26)
    def put_LowEQGain(self, value: Byte) -> Void: ...
    @winrt_commethod(27)
    def get_LowEQGain(self) -> Byte: ...
    @winrt_commethod(28)
    def put_LowEQCutoff(self, value: Byte) -> Void: ...
    @winrt_commethod(29)
    def get_LowEQCutoff(self) -> Byte: ...
    @winrt_commethod(30)
    def put_HighEQGain(self, value: Byte) -> Void: ...
    @winrt_commethod(31)
    def get_HighEQGain(self) -> Byte: ...
    @winrt_commethod(32)
    def put_HighEQCutoff(self, value: Byte) -> Void: ...
    @winrt_commethod(33)
    def get_HighEQCutoff(self) -> Byte: ...
    @winrt_commethod(34)
    def put_RoomFilterFreq(self, value: Double) -> Void: ...
    @winrt_commethod(35)
    def get_RoomFilterFreq(self) -> Double: ...
    @winrt_commethod(36)
    def put_RoomFilterMain(self, value: Double) -> Void: ...
    @winrt_commethod(37)
    def get_RoomFilterMain(self) -> Double: ...
    @winrt_commethod(38)
    def put_RoomFilterHF(self, value: Double) -> Void: ...
    @winrt_commethod(39)
    def get_RoomFilterHF(self) -> Double: ...
    @winrt_commethod(40)
    def put_ReflectionsGain(self, value: Double) -> Void: ...
    @winrt_commethod(41)
    def get_ReflectionsGain(self) -> Double: ...
    @winrt_commethod(42)
    def put_ReverbGain(self, value: Double) -> Void: ...
    @winrt_commethod(43)
    def get_ReverbGain(self) -> Double: ...
    @winrt_commethod(44)
    def put_DecayTime(self, value: Double) -> Void: ...
    @winrt_commethod(45)
    def get_DecayTime(self) -> Double: ...
    @winrt_commethod(46)
    def put_Density(self, value: Double) -> Void: ...
    @winrt_commethod(47)
    def get_Density(self) -> Double: ...
    @winrt_commethod(48)
    def put_RoomSize(self, value: Double) -> Void: ...
    @winrt_commethod(49)
    def get_RoomSize(self) -> Double: ...
    @winrt_commethod(50)
    def put_DisableLateField(self, value: Boolean) -> Void: ...
    @winrt_commethod(51)
    def get_DisableLateField(self) -> Boolean: ...
    WetDryMix = property(get_WetDryMix, put_WetDryMix)
    ReflectionsDelay = property(get_ReflectionsDelay, put_ReflectionsDelay)
    ReverbDelay = property(get_ReverbDelay, put_ReverbDelay)
    RearDelay = property(get_RearDelay, put_RearDelay)
    PositionLeft = property(get_PositionLeft, put_PositionLeft)
    PositionRight = property(get_PositionRight, put_PositionRight)
    PositionMatrixLeft = property(get_PositionMatrixLeft, put_PositionMatrixLeft)
    PositionMatrixRight = property(get_PositionMatrixRight, put_PositionMatrixRight)
    EarlyDiffusion = property(get_EarlyDiffusion, put_EarlyDiffusion)
    LateDiffusion = property(get_LateDiffusion, put_LateDiffusion)
    LowEQGain = property(get_LowEQGain, put_LowEQGain)
    LowEQCutoff = property(get_LowEQCutoff, put_LowEQCutoff)
    HighEQGain = property(get_HighEQGain, put_HighEQGain)
    HighEQCutoff = property(get_HighEQCutoff, put_HighEQCutoff)
    RoomFilterFreq = property(get_RoomFilterFreq, put_RoomFilterFreq)
    RoomFilterMain = property(get_RoomFilterMain, put_RoomFilterMain)
    RoomFilterHF = property(get_RoomFilterHF, put_RoomFilterHF)
    ReflectionsGain = property(get_ReflectionsGain, put_ReflectionsGain)
    ReverbGain = property(get_ReverbGain, put_ReverbGain)
    DecayTime = property(get_DecayTime, put_DecayTime)
    Density = property(get_Density, put_Density)
    RoomSize = property(get_RoomSize, put_RoomSize)
    DisableLateField = property(get_DisableLateField, put_DisableLateField)
class IReverbEffectDefinitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.IReverbEffectDefinitionFactory'
    _iid_ = Guid('{a7d5cbfe-100b-4ff0-9da6-dc4e05a759f0}')
    @winrt_commethod(6)
    def Create(self, audioGraph: win32more.Windows.Media.Audio.AudioGraph) -> win32more.Windows.Media.Audio.ReverbEffectDefinition: ...
class ISetDefaultSpatialAudioFormatResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ISetDefaultSpatialAudioFormatResult'
    _iid_ = Guid('{1c2aa511-1400-5e70-9ea9-ae151241e8ea}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Audio.SetDefaultSpatialAudioFormatStatus: ...
    Status = property(get_Status, None)
class ISpatialAudioDeviceConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ISpatialAudioDeviceConfiguration'
    _iid_ = Guid('{ee830034-61cf-5749-9da4-10f0fe028199}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsSpatialAudioSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def IsSpatialAudioFormatSupported(self, subtype: WinRT_String) -> Boolean: ...
    @winrt_commethod(9)
    def get_ActiveSpatialAudioFormat(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_DefaultSpatialAudioFormat(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def SetDefaultSpatialAudioFormatAsync(self, subtype: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.SetDefaultSpatialAudioFormatResult]: ...
    @winrt_commethod(12)
    def add_ConfigurationChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.SpatialAudioDeviceConfiguration, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ConfigurationChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    IsSpatialAudioSupported = property(get_IsSpatialAudioSupported, None)
    ActiveSpatialAudioFormat = property(get_ActiveSpatialAudioFormat, None)
    DefaultSpatialAudioFormat = property(get_DefaultSpatialAudioFormat, None)
class ISpatialAudioDeviceConfigurationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ISpatialAudioDeviceConfigurationStatics'
    _iid_ = Guid('{3ec37f7b-936d-4e04-9728-2827d9f758c4}')
    @winrt_commethod(6)
    def GetForDeviceId(self, deviceId: WinRT_String) -> win32more.Windows.Media.Audio.SpatialAudioDeviceConfiguration: ...
class ISpatialAudioFormatConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ISpatialAudioFormatConfiguration'
    _iid_ = Guid('{32df09a8-50f0-5395-9923-7d44ca71ed6d}')
    @winrt_commethod(6)
    def ReportLicenseChangedAsync(self, subtype: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportConfigurationChangedAsync(self, subtype: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_MixedRealityExclusiveModePolicy(self) -> win32more.Windows.Media.Audio.MixedRealitySpatialAudioFormatPolicy: ...
    @winrt_commethod(9)
    def put_MixedRealityExclusiveModePolicy(self, value: win32more.Windows.Media.Audio.MixedRealitySpatialAudioFormatPolicy) -> Void: ...
    MixedRealityExclusiveModePolicy = property(get_MixedRealityExclusiveModePolicy, put_MixedRealityExclusiveModePolicy)
class ISpatialAudioFormatConfigurationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ISpatialAudioFormatConfigurationStatics'
    _iid_ = Guid('{2b5fef71-67c9-4e5f-a35b-41680711f8c7}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Media.Audio.SpatialAudioFormatConfiguration: ...
class ISpatialAudioFormatSubtypeStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ISpatialAudioFormatSubtypeStatics'
    _iid_ = Guid('{b3de8a47-83ee-4266-a945-bedf507afeed}')
    @winrt_commethod(6)
    def get_WindowsSonic(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DolbyAtmosForHeadphones(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DolbyAtmosForHomeTheater(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DolbyAtmosForSpeakers(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_DTSHeadphoneX(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_DTSXUltra(self) -> WinRT_String: ...
    WindowsSonic = property(get_WindowsSonic, None)
    DolbyAtmosForHeadphones = property(get_DolbyAtmosForHeadphones, None)
    DolbyAtmosForHomeTheater = property(get_DolbyAtmosForHomeTheater, None)
    DolbyAtmosForSpeakers = property(get_DolbyAtmosForSpeakers, None)
    DTSHeadphoneX = property(get_DTSHeadphoneX, None)
    DTSXUltra = property(get_DTSXUltra, None)
class ISpatialAudioFormatSubtypeStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.ISpatialAudioFormatSubtypeStatics2'
    _iid_ = Guid('{4565e6cb-d95b-5621-b6af-0e8849c57c80}')
    @winrt_commethod(6)
    def get_DTSXForHomeTheater(self) -> WinRT_String: ...
    DTSXForHomeTheater = property(get_DTSXForHomeTheater, None)
class LimiterEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.ILimiterEffectDefinition
    _classid_ = 'Windows.Media.Audio.LimiterEffectDefinition'
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Audio.ILimiterEffectDefinitionFactory, audioGraph: win32more.Windows.Media.Audio.AudioGraph) -> win32more.Windows.Media.Audio.LimiterEffectDefinition: ...
    @winrt_mixinmethod
    def put_Release(self: win32more.Windows.Media.Audio.ILimiterEffectDefinition, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Release(self: win32more.Windows.Media.Audio.ILimiterEffectDefinition) -> UInt32: ...
    @winrt_mixinmethod
    def put_Loudness(self: win32more.Windows.Media.Audio.ILimiterEffectDefinition, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Loudness(self: win32more.Windows.Media.Audio.ILimiterEffectDefinition) -> UInt32: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    Release = property(get_Release, put_Release)
    Loudness = property(get_Loudness, put_Loudness)
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class MediaSourceAudioInputNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode
    _classid_ = 'Windows.Media.Audio.MediaSourceAudioInputNode'
    @winrt_mixinmethod
    def put_PlaybackSpeedFactor(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_PlaybackSpeedFactor(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode) -> Double: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def Seek(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode, position: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_StartTime(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_EndTime(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_EndTime(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_LoopCount(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_LoopCount(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MediaSource(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_mixinmethod
    def add_MediaSourceCompleted(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.MediaSourceAudioInputNode, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MediaSourceCompleted(self: win32more.Windows.Media.Audio.IMediaSourceAudioInputNode, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_OutgoingConnections(self: win32more.Windows.Media.Audio.IAudioInputNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Audio.AudioGraphConnection]: ...
    @winrt_mixinmethod
    def AddOutgoingConnection(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def AddOutgoingConnectionWithGain(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode, gain: Double) -> Void: ...
    @winrt_mixinmethod
    def RemoveOutgoingConnection(self: win32more.Windows.Media.Audio.IAudioInputNode, destination: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def get_EffectDefinitions(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    @winrt_mixinmethod
    def put_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OutgoingGain(self: win32more.Windows.Media.Audio.IAudioNode) -> Double: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Audio.IAudioNode) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode) -> Boolean: ...
    @winrt_mixinmethod
    def put_ConsumeInput(self: win32more.Windows.Media.Audio.IAudioNode, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.Media.Audio.IAudioNode) -> Void: ...
    @winrt_mixinmethod
    def DisableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def EnableEffectsByDefinition(self: win32more.Windows.Media.Audio.IAudioNode, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_Emitter(self: win32more.Windows.Media.Audio.IAudioInputNode2) -> win32more.Windows.Media.Audio.AudioNodeEmitter: ...
    PlaybackSpeedFactor = property(get_PlaybackSpeedFactor, put_PlaybackSpeedFactor)
    Position = property(get_Position, None)
    StartTime = property(get_StartTime, put_StartTime)
    EndTime = property(get_EndTime, put_EndTime)
    LoopCount = property(get_LoopCount, put_LoopCount)
    Duration = property(get_Duration, None)
    MediaSource = property(get_MediaSource, None)
    OutgoingConnections = property(get_OutgoingConnections, None)
    EffectDefinitions = property(get_EffectDefinitions, None)
    OutgoingGain = property(get_OutgoingGain, put_OutgoingGain)
    EncodingProperties = property(get_EncodingProperties, None)
    ConsumeInput = property(get_ConsumeInput, put_ConsumeInput)
    Emitter = property(get_Emitter, None)
MediaSourceAudioInputNodeCreationStatus = Int32
MediaSourceAudioInputNodeCreationStatus_Success: MediaSourceAudioInputNodeCreationStatus = 0
MediaSourceAudioInputNodeCreationStatus_FormatNotSupported: MediaSourceAudioInputNodeCreationStatus = 1
MediaSourceAudioInputNodeCreationStatus_NetworkError: MediaSourceAudioInputNodeCreationStatus = 2
MediaSourceAudioInputNodeCreationStatus_UnknownFailure: MediaSourceAudioInputNodeCreationStatus = 3
MixedRealitySpatialAudioFormatPolicy = Int32
MixedRealitySpatialAudioFormatPolicy_UseMixedRealityDefaultSpatialAudioFormat: MixedRealitySpatialAudioFormatPolicy = 0
MixedRealitySpatialAudioFormatPolicy_UseDeviceConfigurationDefaultSpatialAudioFormat: MixedRealitySpatialAudioFormatPolicy = 1
QuantumSizeSelectionMode = Int32
QuantumSizeSelectionMode_SystemDefault: QuantumSizeSelectionMode = 0
QuantumSizeSelectionMode_LowestLatency: QuantumSizeSelectionMode = 1
QuantumSizeSelectionMode_ClosestToDesired: QuantumSizeSelectionMode = 2
class ReverbEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.IReverbEffectDefinition
    _classid_ = 'Windows.Media.Audio.ReverbEffectDefinition'
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Audio.IReverbEffectDefinitionFactory, audioGraph: win32more.Windows.Media.Audio.AudioGraph) -> win32more.Windows.Media.Audio.ReverbEffectDefinition: ...
    @winrt_mixinmethod
    def put_WetDryMix(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_WetDryMix(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def put_ReflectionsDelay(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReflectionsDelay(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReverbDelay(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_ReverbDelay(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Byte: ...
    @winrt_mixinmethod
    def put_RearDelay(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_RearDelay(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Byte: ...
    @winrt_mixinmethod
    def put_PositionLeft(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_PositionLeft(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Byte: ...
    @winrt_mixinmethod
    def put_PositionRight(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_PositionRight(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Byte: ...
    @winrt_mixinmethod
    def put_PositionMatrixLeft(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_PositionMatrixLeft(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Byte: ...
    @winrt_mixinmethod
    def put_PositionMatrixRight(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_PositionMatrixRight(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Byte: ...
    @winrt_mixinmethod
    def put_EarlyDiffusion(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_EarlyDiffusion(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Byte: ...
    @winrt_mixinmethod
    def put_LateDiffusion(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_LateDiffusion(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Byte: ...
    @winrt_mixinmethod
    def put_LowEQGain(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_LowEQGain(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Byte: ...
    @winrt_mixinmethod
    def put_LowEQCutoff(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_LowEQCutoff(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Byte: ...
    @winrt_mixinmethod
    def put_HighEQGain(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_HighEQGain(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Byte: ...
    @winrt_mixinmethod
    def put_HighEQCutoff(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_HighEQCutoff(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Byte: ...
    @winrt_mixinmethod
    def put_RoomFilterFreq(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RoomFilterFreq(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def put_RoomFilterMain(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RoomFilterMain(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def put_RoomFilterHF(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RoomFilterHF(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def put_ReflectionsGain(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ReflectionsGain(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def put_ReverbGain(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ReverbGain(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def put_DecayTime(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DecayTime(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def put_Density(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Density(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def put_RoomSize(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RoomSize(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def put_DisableLateField(self: win32more.Windows.Media.Audio.IReverbEffectDefinition, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DisableLateField(self: win32more.Windows.Media.Audio.IReverbEffectDefinition) -> Boolean: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    WetDryMix = property(get_WetDryMix, put_WetDryMix)
    ReflectionsDelay = property(get_ReflectionsDelay, put_ReflectionsDelay)
    ReverbDelay = property(get_ReverbDelay, put_ReverbDelay)
    RearDelay = property(get_RearDelay, put_RearDelay)
    PositionLeft = property(get_PositionLeft, put_PositionLeft)
    PositionRight = property(get_PositionRight, put_PositionRight)
    PositionMatrixLeft = property(get_PositionMatrixLeft, put_PositionMatrixLeft)
    PositionMatrixRight = property(get_PositionMatrixRight, put_PositionMatrixRight)
    EarlyDiffusion = property(get_EarlyDiffusion, put_EarlyDiffusion)
    LateDiffusion = property(get_LateDiffusion, put_LateDiffusion)
    LowEQGain = property(get_LowEQGain, put_LowEQGain)
    LowEQCutoff = property(get_LowEQCutoff, put_LowEQCutoff)
    HighEQGain = property(get_HighEQGain, put_HighEQGain)
    HighEQCutoff = property(get_HighEQCutoff, put_HighEQCutoff)
    RoomFilterFreq = property(get_RoomFilterFreq, put_RoomFilterFreq)
    RoomFilterMain = property(get_RoomFilterMain, put_RoomFilterMain)
    RoomFilterHF = property(get_RoomFilterHF, put_RoomFilterHF)
    ReflectionsGain = property(get_ReflectionsGain, put_ReflectionsGain)
    ReverbGain = property(get_ReverbGain, put_ReverbGain)
    DecayTime = property(get_DecayTime, put_DecayTime)
    Density = property(get_Density, put_Density)
    RoomSize = property(get_RoomSize, put_RoomSize)
    DisableLateField = property(get_DisableLateField, put_DisableLateField)
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class SetDefaultSpatialAudioFormatResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.ISetDefaultSpatialAudioFormatResult
    _classid_ = 'Windows.Media.Audio.SetDefaultSpatialAudioFormatResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Audio.ISetDefaultSpatialAudioFormatResult) -> win32more.Windows.Media.Audio.SetDefaultSpatialAudioFormatStatus: ...
    Status = property(get_Status, None)
SetDefaultSpatialAudioFormatStatus = Int32
SetDefaultSpatialAudioFormatStatus_Succeeded: SetDefaultSpatialAudioFormatStatus = 0
SetDefaultSpatialAudioFormatStatus_AccessDenied: SetDefaultSpatialAudioFormatStatus = 1
SetDefaultSpatialAudioFormatStatus_LicenseExpired: SetDefaultSpatialAudioFormatStatus = 2
SetDefaultSpatialAudioFormatStatus_LicenseNotValidForAudioEndpoint: SetDefaultSpatialAudioFormatStatus = 3
SetDefaultSpatialAudioFormatStatus_NotSupportedOnAudioEndpoint: SetDefaultSpatialAudioFormatStatus = 4
SetDefaultSpatialAudioFormatStatus_UnknownError: SetDefaultSpatialAudioFormatStatus = 5
class SpatialAudioDeviceConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.ISpatialAudioDeviceConfiguration
    _classid_ = 'Windows.Media.Audio.SpatialAudioDeviceConfiguration'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Media.Audio.ISpatialAudioDeviceConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsSpatialAudioSupported(self: win32more.Windows.Media.Audio.ISpatialAudioDeviceConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def IsSpatialAudioFormatSupported(self: win32more.Windows.Media.Audio.ISpatialAudioDeviceConfiguration, subtype: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def get_ActiveSpatialAudioFormat(self: win32more.Windows.Media.Audio.ISpatialAudioDeviceConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DefaultSpatialAudioFormat(self: win32more.Windows.Media.Audio.ISpatialAudioDeviceConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetDefaultSpatialAudioFormatAsync(self: win32more.Windows.Media.Audio.ISpatialAudioDeviceConfiguration, subtype: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.SetDefaultSpatialAudioFormatResult]: ...
    @winrt_mixinmethod
    def add_ConfigurationChanged(self: win32more.Windows.Media.Audio.ISpatialAudioDeviceConfiguration, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Audio.SpatialAudioDeviceConfiguration, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConfigurationChanged(self: win32more.Windows.Media.Audio.ISpatialAudioDeviceConfiguration, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForDeviceId(cls: win32more.Windows.Media.Audio.ISpatialAudioDeviceConfigurationStatics, deviceId: WinRT_String) -> win32more.Windows.Media.Audio.SpatialAudioDeviceConfiguration: ...
    DeviceId = property(get_DeviceId, None)
    IsSpatialAudioSupported = property(get_IsSpatialAudioSupported, None)
    ActiveSpatialAudioFormat = property(get_ActiveSpatialAudioFormat, None)
    DefaultSpatialAudioFormat = property(get_DefaultSpatialAudioFormat, None)
class SpatialAudioFormatConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Audio.ISpatialAudioFormatConfiguration
    _classid_ = 'Windows.Media.Audio.SpatialAudioFormatConfiguration'
    @winrt_mixinmethod
    def ReportLicenseChangedAsync(self: win32more.Windows.Media.Audio.ISpatialAudioFormatConfiguration, subtype: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportConfigurationChangedAsync(self: win32more.Windows.Media.Audio.ISpatialAudioFormatConfiguration, subtype: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_MixedRealityExclusiveModePolicy(self: win32more.Windows.Media.Audio.ISpatialAudioFormatConfiguration) -> win32more.Windows.Media.Audio.MixedRealitySpatialAudioFormatPolicy: ...
    @winrt_mixinmethod
    def put_MixedRealityExclusiveModePolicy(self: win32more.Windows.Media.Audio.ISpatialAudioFormatConfiguration, value: win32more.Windows.Media.Audio.MixedRealitySpatialAudioFormatPolicy) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Media.Audio.ISpatialAudioFormatConfigurationStatics) -> win32more.Windows.Media.Audio.SpatialAudioFormatConfiguration: ...
    MixedRealityExclusiveModePolicy = property(get_MixedRealityExclusiveModePolicy, put_MixedRealityExclusiveModePolicy)
class _SpatialAudioFormatSubtype_Meta_(ComPtr.__class__):
    pass
class SpatialAudioFormatSubtype(ComPtr, metaclass=_SpatialAudioFormatSubtype_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Audio.SpatialAudioFormatSubtype'
    @winrt_classmethod
    def get_DTSXForHomeTheater(cls: win32more.Windows.Media.Audio.ISpatialAudioFormatSubtypeStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_WindowsSonic(cls: win32more.Windows.Media.Audio.ISpatialAudioFormatSubtypeStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DolbyAtmosForHeadphones(cls: win32more.Windows.Media.Audio.ISpatialAudioFormatSubtypeStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DolbyAtmosForHomeTheater(cls: win32more.Windows.Media.Audio.ISpatialAudioFormatSubtypeStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DolbyAtmosForSpeakers(cls: win32more.Windows.Media.Audio.ISpatialAudioFormatSubtypeStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DTSHeadphoneX(cls: win32more.Windows.Media.Audio.ISpatialAudioFormatSubtypeStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DTSXUltra(cls: win32more.Windows.Media.Audio.ISpatialAudioFormatSubtypeStatics) -> WinRT_String: ...
    _SpatialAudioFormatSubtype_Meta_.DTSXForHomeTheater = property(get_DTSXForHomeTheater.__wrapped__, None)
    _SpatialAudioFormatSubtype_Meta_.WindowsSonic = property(get_WindowsSonic.__wrapped__, None)
    _SpatialAudioFormatSubtype_Meta_.DolbyAtmosForHeadphones = property(get_DolbyAtmosForHeadphones.__wrapped__, None)
    _SpatialAudioFormatSubtype_Meta_.DolbyAtmosForHomeTheater = property(get_DolbyAtmosForHomeTheater.__wrapped__, None)
    _SpatialAudioFormatSubtype_Meta_.DolbyAtmosForSpeakers = property(get_DolbyAtmosForSpeakers.__wrapped__, None)
    _SpatialAudioFormatSubtype_Meta_.DTSHeadphoneX = property(get_DTSHeadphoneX.__wrapped__, None)
    _SpatialAudioFormatSubtype_Meta_.DTSXUltra = property(get_DTSXUltra.__wrapped__, None)
SpatialAudioModel = Int32
SpatialAudioModel_ObjectBased: SpatialAudioModel = 0
SpatialAudioModel_FoldDown: SpatialAudioModel = 1
make_head(_module, 'AudioDeviceInputNode')
make_head(_module, 'AudioDeviceOutputNode')
make_head(_module, 'AudioFileInputNode')
make_head(_module, 'AudioFileOutputNode')
make_head(_module, 'AudioFrameCompletedEventArgs')
make_head(_module, 'AudioFrameInputNode')
make_head(_module, 'AudioFrameOutputNode')
make_head(_module, 'AudioGraph')
make_head(_module, 'AudioGraphBatchUpdater')
make_head(_module, 'AudioGraphConnection')
make_head(_module, 'AudioGraphSettings')
make_head(_module, 'AudioGraphUnrecoverableErrorOccurredEventArgs')
make_head(_module, 'AudioNodeEmitter')
make_head(_module, 'AudioNodeEmitterConeProperties')
make_head(_module, 'AudioNodeEmitterDecayModel')
make_head(_module, 'AudioNodeEmitterNaturalDecayModelProperties')
make_head(_module, 'AudioNodeEmitterShape')
make_head(_module, 'AudioNodeListener')
make_head(_module, 'AudioPlaybackConnection')
make_head(_module, 'AudioPlaybackConnectionOpenResult')
make_head(_module, 'AudioStateMonitor')
make_head(_module, 'AudioSubmixNode')
make_head(_module, 'CreateAudioDeviceInputNodeResult')
make_head(_module, 'CreateAudioDeviceOutputNodeResult')
make_head(_module, 'CreateAudioFileInputNodeResult')
make_head(_module, 'CreateAudioFileOutputNodeResult')
make_head(_module, 'CreateAudioGraphResult')
make_head(_module, 'CreateMediaSourceAudioInputNodeResult')
make_head(_module, 'EchoEffectDefinition')
make_head(_module, 'EqualizerBand')
make_head(_module, 'EqualizerEffectDefinition')
make_head(_module, 'FrameInputNodeQuantumStartedEventArgs')
make_head(_module, 'IAudioDeviceInputNode')
make_head(_module, 'IAudioDeviceOutputNode')
make_head(_module, 'IAudioFileInputNode')
make_head(_module, 'IAudioFileOutputNode')
make_head(_module, 'IAudioFrameCompletedEventArgs')
make_head(_module, 'IAudioFrameInputNode')
make_head(_module, 'IAudioFrameOutputNode')
make_head(_module, 'IAudioGraph')
make_head(_module, 'IAudioGraph2')
make_head(_module, 'IAudioGraph3')
make_head(_module, 'IAudioGraphConnection')
make_head(_module, 'IAudioGraphSettings')
make_head(_module, 'IAudioGraphSettings2')
make_head(_module, 'IAudioGraphSettingsFactory')
make_head(_module, 'IAudioGraphStatics')
make_head(_module, 'IAudioGraphUnrecoverableErrorOccurredEventArgs')
make_head(_module, 'IAudioInputNode')
make_head(_module, 'IAudioInputNode2')
make_head(_module, 'IAudioNode')
make_head(_module, 'IAudioNodeEmitter')
make_head(_module, 'IAudioNodeEmitter2')
make_head(_module, 'IAudioNodeEmitterConeProperties')
make_head(_module, 'IAudioNodeEmitterDecayModel')
make_head(_module, 'IAudioNodeEmitterDecayModelStatics')
make_head(_module, 'IAudioNodeEmitterFactory')
make_head(_module, 'IAudioNodeEmitterNaturalDecayModelProperties')
make_head(_module, 'IAudioNodeEmitterShape')
make_head(_module, 'IAudioNodeEmitterShapeStatics')
make_head(_module, 'IAudioNodeListener')
make_head(_module, 'IAudioNodeWithListener')
make_head(_module, 'IAudioPlaybackConnection')
make_head(_module, 'IAudioPlaybackConnectionOpenResult')
make_head(_module, 'IAudioPlaybackConnectionStatics')
make_head(_module, 'IAudioStateMonitor')
make_head(_module, 'IAudioStateMonitorStatics')
make_head(_module, 'ICreateAudioDeviceInputNodeResult')
make_head(_module, 'ICreateAudioDeviceInputNodeResult2')
make_head(_module, 'ICreateAudioDeviceOutputNodeResult')
make_head(_module, 'ICreateAudioDeviceOutputNodeResult2')
make_head(_module, 'ICreateAudioFileInputNodeResult')
make_head(_module, 'ICreateAudioFileInputNodeResult2')
make_head(_module, 'ICreateAudioFileOutputNodeResult')
make_head(_module, 'ICreateAudioFileOutputNodeResult2')
make_head(_module, 'ICreateAudioGraphResult')
make_head(_module, 'ICreateAudioGraphResult2')
make_head(_module, 'ICreateMediaSourceAudioInputNodeResult')
make_head(_module, 'ICreateMediaSourceAudioInputNodeResult2')
make_head(_module, 'IEchoEffectDefinition')
make_head(_module, 'IEchoEffectDefinitionFactory')
make_head(_module, 'IEqualizerBand')
make_head(_module, 'IEqualizerEffectDefinition')
make_head(_module, 'IEqualizerEffectDefinitionFactory')
make_head(_module, 'IFrameInputNodeQuantumStartedEventArgs')
make_head(_module, 'ILimiterEffectDefinition')
make_head(_module, 'ILimiterEffectDefinitionFactory')
make_head(_module, 'IMediaSourceAudioInputNode')
make_head(_module, 'IReverbEffectDefinition')
make_head(_module, 'IReverbEffectDefinitionFactory')
make_head(_module, 'ISetDefaultSpatialAudioFormatResult')
make_head(_module, 'ISpatialAudioDeviceConfiguration')
make_head(_module, 'ISpatialAudioDeviceConfigurationStatics')
make_head(_module, 'ISpatialAudioFormatConfiguration')
make_head(_module, 'ISpatialAudioFormatConfigurationStatics')
make_head(_module, 'ISpatialAudioFormatSubtypeStatics')
make_head(_module, 'ISpatialAudioFormatSubtypeStatics2')
make_head(_module, 'LimiterEffectDefinition')
make_head(_module, 'MediaSourceAudioInputNode')
make_head(_module, 'ReverbEffectDefinition')
make_head(_module, 'SetDefaultSpatialAudioFormatResult')
make_head(_module, 'SpatialAudioDeviceConfiguration')
make_head(_module, 'SpatialAudioFormatConfiguration')
make_head(_module, 'SpatialAudioFormatSubtype')
