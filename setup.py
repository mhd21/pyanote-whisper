import ospyanote-whisper

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="pyanote-whisper",
    py_modules=["pyanote-whisper"],
    version="1.0",
    description="Speech Recognition plus diarization",
    readme="README.md",
    python_requires=">=3.7",
    author="Ruiqing",
    url="https://github.com/yinruiqing/pyanote-whisper",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        'console_scripts': ['pyanote-whisper=pyannote_whisper.cli.transcribe:cli'],
    },
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
