from setuptools import setup

setup(name='ner_crf',
      version='0.1',
      description='ner crf',
      url='#',
      author='jassim',
      author_email='mohammedjassim.jasmir@gmail.com',
      license='MIT',
      packages=[],
      zip_safe=False,
      # Dependent packages (distributions)
      install_requires=[
          "spacy",
          "joblib",
          "textblob",
          "scikit-learn",
          "sklearn-crfsuite",
          "pandas",
          'en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz',

      ],
      )