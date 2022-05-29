import shutil
import subprocess
import abc


class Syscall(abc.ABC):

    @abc.abstractmethod
    def get_bin(self) -> str:
        ...

    def get_args(self) -> list:
        return self.__args

    def set_args(self, *args) -> None:
        self.__args = list(args)

    def call(self) -> None:
        args = " ".join(self.get_args() or [])
        bin = self.get_bin()
        cmd = f"{ bin } { args }".split()
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        self.print_stdout(proc)

    def print_stdout(self, proc: subprocess.Popen) -> None:
        while True:
            output = proc.stdout.readline()
            if not output: break
            print(f"[ABKP] { output.rstrip().decode('utf-8') }")


class ADBSyscall(Syscall):

    def __init__(self, *args) -> None:
        self.__args = list(args)

    def get_bin(self) -> str:
        return shutil.which('adb')

    @staticmethod
    def backup(appname: str) -> None:
        adb = ADBSyscall()
        adb.set_args('backup', appname)
        adb.call()

    @staticmethod
    def restore(filename: str) -> None:
        adb = ADBSyscall()
        adb.set_args('restore', filename)
        adb.call()


adb = ADBSyscall
