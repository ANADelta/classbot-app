# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="alphaclassbot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "openai",
        "python-dotenv"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    description="A bot for AlphaClass using Streamlit and OpenAI.",
    long_description="A longer description of AlphaClassBot.",
    long_description_content_type="text/markdown"
)

