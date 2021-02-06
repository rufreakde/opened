#!/usr/local/bin/python3
from __future__ import annotations
from pathlib import Path


class opened():
    def __init__(self, folderpath: str, filename: str, mode='w', extended=False, dot_root="."):
        self.filehandle = {}
        self.folderpath: str = folderpath
        self.filename: str = filename
        self.mode: str = mode
        self.filepath: str = ''
        self.extended: bool = extended
        self.dot_root = dot_root

    def handle_relative_Path_beginning(self, folderpath: str) -> str:
        if self.dot_root is ".":
            return folderpath

        if folderpath[:1] is '..':
            return f"{self.dot_root}/../{folderpath}"

        if folderpath[0] is '.':
            return f"{self.dot_root}/{folderpath}"

        raise Exception("Unkown String Beginning format found! - opened")

    def handle_paths(self, folderpath: str, filename: str) -> str:
        folderpath = self.handle_relative_Path_beginning(folderpath)
        folderpath = folderpath.replace('\\', '/')
        Path(folderpath).mkdir(parents=True, exist_ok=True)
        path = Path(folderpath).resolve()
        return f"{path}/{filename}"

    def __enter__(self) -> opened | dict:

        self.filepath = self.handle_paths(
            self.folderpath, self.filename)
        self.filehandle = open(self.filepath, self.mode)

        if self.extended is True:
            return self
        else:
            return self.filehandle

    def __exit__(self, type, value, traceback):
        self.filehandle.close()
