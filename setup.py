from cx_Freeze import setup, Executable

#must include all file names
includefiles = ['button.py, camera.py, editor.py, game.py, img_n_sound.py, map.py, menu.py, mode.py, freesansbold.ttf']

setup(  
      name = "Parkour",
        version = "0.1",
        description = "My GUI application!",
        executables = [Executable("Main.py")])