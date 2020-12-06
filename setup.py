import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yt_playlist_dl",
    version="0.0.1",
    author="Tushar Sadhwani",
    author_email="tushar.sadhwani000@gmail.com",
    description="A tool to download (and keep up-to-date) a playlist from youtube.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tusharsadhwani/yt_playlist_dl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
