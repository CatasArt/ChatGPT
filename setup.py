from setuptools import find_packages, setup

setup(
    name="revChatGPT",
<<<<<<< HEAD
    version="2.3.5",
    license="GNU General Public License v2.0",
=======
    version="3.1.1",
    description="ChatGPT is a reverse engineering of OpenAI's ChatGPT API",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/acheong08/ChatGPT",
>>>>>>> 925bef9abdce6232a3ec028c128c81018aad2a10
    author="Antonio Cheong",
    author_email="acheong@student.dalat.org",
    license="GNU General Public License v2.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["Unofficial", "V2", "V1", "V0", "V3"],
    install_requires=[
        "OpenAIAuth==0.3.2",
<<<<<<< HEAD
        "requests",
=======
        "requests[socks]",
        "httpx[socks]",
        "prompt-toolkit",
        "tiktoken",
>>>>>>> 925bef9abdce6232a3ec028c128c81018aad2a10
    ],
    extras_require={
        "unofficial": [
            "requests",
            "undetected_chromedriver",
            "selenium",
            "tls_client",
        ],
        "official": [
            "openai",
            "tiktoken",
        ],
    },
)
