# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

a = Analysis(['main.py'],
             pathex=['C:\\Users\\Administrator\\Desktop\\VScode\\Python\\Python_work\\3.RSA_work'],
             binaries=[],
             datas=[("resources", "resources")], # 资源文件路径
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='RSA_Liu',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False, # 黑框
          icon = './resources/RSA.ico' )    # .exe图标文件
