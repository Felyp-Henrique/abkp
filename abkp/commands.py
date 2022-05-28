import click
import utils


@click.group()
def abkp(): ...


@abkp.command("backup:backup")
@click.argument("appname", type=str)
def abkp_backup_backup(appname: str):
    utils.adb.backup(appname)


@abkp.command("backup:restore")
@click.argument("filename", type=click.Path(exists=True))
def abkp_backup_restore(filename: str):
    utils.adb.restore(filename)
