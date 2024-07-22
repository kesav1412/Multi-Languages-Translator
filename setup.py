from setuptools import setup, find_packages 

setup(
    name="Multi Language Translate",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
      "mariadb",
        "transformers",
        "torch",
        "torchvision",
        "torchaudio",
        "sentencepiece",
        "protobuf",  
    ],
)