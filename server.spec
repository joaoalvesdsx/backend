# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['server.py'],
    pathex=['C:\\Users\\Pc\\Desktop\\Projeto final\\my-react-app\\backend'],  # Ajuste para o diretório correto
    binaries=[],
    datas=[
        ('.env', '.'), 
        ('uploads/', 'uploads'),  # Inclui todos os arquivos em uploads
    ],
    hiddenimports=[
        'models',
        'database',
        'utils.py',
        'config',  # Assuma que config.py também precisa ser incluído
        # Adicione outros módulos aqui que possam não estar sendo automaticamente detectados
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='server',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Se o UPX estiver causando problemas, considere definir como False
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Adicione o caminho para um ícone se necessário
)

# Garanta que 'upx' esteja disponível se upx=True ou remova essa opção se não estiver usando UPX
