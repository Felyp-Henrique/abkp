import shutil
import click
import subprocess


ADB_BIN = shutil.which("adb")


@click.group()
def abkp():
    pass


@abkp.command("backup:backup")
@click.argument("appname", type=str)
def abkp_backup_backup(appname: str):
    cmd =  f"{ ADB_BIN } backup { appname }"
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    _read_stdout(proc)


@abkp.command("backup:restore")
@click.argument("filename", type=click.Path(exists=True))
def abkp_backup_restore(filename: str):
    cmd =  f"{ ADB_BIN } restore { filename }"
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    _read_stdout(proc)


def _read_stdout(proc: subprocess.Popen):
    while True:
        output = proc.stdout.readline()
        if not output:
            break
        print(f"[ABKP] { output.rstrip().decode('utf-8') }")