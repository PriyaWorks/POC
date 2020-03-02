# POC
conda create -n myflaskenv python=3.6

pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz --no-deps


step1: conda create -n lgApp python=3.6
step2: conda activate lgApp
step3: conda install -c conda-forge spacy
step4: python -m spacy download en_core_web_sm --> it gives error
step5: conda install -c anaconda flask
step6: code: 
step 7: python run app.py
conda remove --name myapp --all
