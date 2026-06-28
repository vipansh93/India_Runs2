# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for Aura Recruit - AI Candidate Ranker
# Bundles the Flask backend + index.html into a single Windows EXE.
# The candidates.jsonl dataset is NOT bundled (too large) - the EXE looks
# for it next to itself, or you can pass --candidates path\to\candidates.jsonl

import os
from PyInstaller.utils.hooks import collect_all

# Collect all sub-packages for bundled libraries
flask_datas, flask_binaries, flask_hiddenimports = collect_all('flask')
cors_datas, cors_binaries, cors_hiddenimports = collect_all('flask_cors')
openpyxl_datas, openpyxl_binaries, openpyxl_hiddenimports = collect_all('openpyxl')

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=['.'],
    binaries=flask_binaries + cors_binaries + openpyxl_binaries,
    datas=[
        # Bundle the HTML frontend alongside the executable
        ('index.html', '.'),
    ] + flask_datas + cors_datas + openpyxl_datas,
    hiddenimports=[
        'flask', 'flask_cors', 'werkzeug', 'werkzeug.serving',
        'werkzeug.routing', 'werkzeug.exceptions', 'werkzeug.middleware',
        'werkzeug.utils', 'click', 'jinja2', 'itsdangerous',
        'openpyxl', 'openpyxl.styles', 'openpyxl.utils',
        'openpyxl.workbook', 'openpyxl.worksheet',
        'et_xmlfile',
    ] + flask_hiddenimports + cors_hiddenimports + openpyxl_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AuraRecruit',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,   # keep console so users can see startup logs & progress
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    onefile=True,
)
