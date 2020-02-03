import setuptools

setuptools.setup(
    name='musical-spoon',
    version='0.1',
    packages=[
        'musical_spoon',
    ],
    install_requires=[
        'mendeleev>=0.5',
        'networkx>=2.4',
        'numpy>=1.18',
        'matplotlib>=3.1',
    ]
)
