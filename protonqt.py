import subprocess

def run_proton_qt(path_to_exe:str):
    proton_path = '/usr/bin/proton'
    subprocess.run([proton_path, path_to_exe])