import click
import syscalls
import compressors
import validators as vld


@click.group()
def abkp(): ...


@abkp.command("backup:backup")
@click.argument("appname", type=str)
@vld.required(vld.validate_adb_exists)
def abkp_backup_backup(appname: str):
    syscalls.adb.backup(appname)
    with compressors.abopen('backup.ab') as ab:
        ab.to_tar('backup.tar')


@abkp.command("backup:restore")
@click.argument("filename", type=click.Path(exists=True))
@vld.required(vld.validate_adb_exists)
def abkp_backup_restore(filename: str):
    syscalls.adb.restore(filename)
