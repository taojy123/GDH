# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'App1.py'],
             pathex=['E:\\Workspace\\GitHub\\GDH'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'GDH_test.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='c:\\QQProtect.ico')
app = BUNDLE(exe,
             name=os.path.join('dist', 'GDH_test.exe.app'))
