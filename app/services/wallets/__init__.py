#!/usr/bin/python
# app/services/wallets/__init__.py


def extract_zip(path: str) -> str:
    """Extract the MetaMask ZIP content."""
    from zipfile import ZipFile
    from os.path import exists
    folder: str = path.replace('.crx', '')
    if not exists(folder):
        with ZipFile(path, 'r') as zip_content:
            zip_content.extractall(folder)
    return folder
