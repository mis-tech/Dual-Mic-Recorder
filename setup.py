from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'system32':
    base = None


executables = [Executable("Dua_Mic_Recorder.py", base=base)]

packages = ["idna", "os","sys","scipy.io.wavfile","tkinter","tkinter.ttk","pyaudio","time","csv","timeit","cv2","wave"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Dua_Mic_Recorder",
    options = options,
    version = "0.11",
    description = 'Descriptionn',
    executables = executables
)