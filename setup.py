from setuptools import setup

setup(
    name='AutoTyper',
    version='1.0',
    py_modules=['rumapp'],
    install_requires=[
        'rumps',
        'pyautogui'
    ],
    app=['rumapp.py'],
    data_files=[('icons', ['icons/logo.icns'])],
    options={
        'py2app': {
            'argv_emulation': False,
            'iconfile': 'icons/logo.icns',
            'plist': {
                'LSUIElement': True,
            },
            'packages': ['rumps', 'pyautogui'],
            'excludes': ['rubicon'],
        }
    },
    setup_requires=['py2app']
)
