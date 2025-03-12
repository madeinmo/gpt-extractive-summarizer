from setuptools import setup
from setuptools import find_packages

setup(name='gpt-extractive-summarizer',
      version='0.10.1',
      description='Extractive Text Summarization with OpenAI',
      keywords=['openai', 'pytorch', 'machine learning',
                'deep learning', 'extractive summarization', 'summary'],
      long_description=open("README.md", "r", encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      url='https://github.com/madeinmo/gpt-extractive-summarizer',
      download_url='https://github.com/madeinmo/gpt-extractive-summarizer/archive/0.10.1.tar.gz',
      author='Timur Zhilyaev',
      author_email='timurgan.gi2@gmail.com',
      install_requires=['openai', 'scikit-learn', 'spacy'],
      license='MIT',
      packages=find_packages(),
      zip_safe=False
)
