class ABFile:
    def __init__(self, path: str) -> None:
        self.path = path

    def __enter__(self) -> object:
        return self

    def __exit__(self, type, value, traceback) -> None:
        pass

    def to_tar(self, path: str) -> None:
        with open(self.path, 'rb') as ab:
            buffer = ab.read(1)
        with open(path, 'wb') as tar:
            tar.write("\x1f\x8b\x08\x00\x00\x00\x00\x00")
            tar.write(buffer)


abopen = ABFile