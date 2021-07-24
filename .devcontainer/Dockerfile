#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

FROM jdvelasq/python:3.6.9-ml

# Avoid warnings by switching to noninteractive
# ENV DEBIAN_FRONTEND=noninteractive

# This Dockerfile adds a non-root user with sudo access. Use the "remoteUser"
# property in devcontainer.json to use it. On Linux, the container user's GID/UIDs
# will be updated to match your local UID/GID (when using the dockerFile property).
# See https://aka.ms/vscode-remote/containers/non-root-user for details.
# ARG USERNAME=vscode
# ARG USER_UID=1000
# ARG USER_GID=$USER_UID

# Uncomment the following COPY line and the corresponding lines in the `RUN` command if you wish to
# include your requirements in the image itself. It is suggested that you only do this if your
# requirements rarely (if ever) change.
# COPY requirements.txt /tmp/pip-tmp/

# Configure apt and install packages



# RUN apt-get update \
#     && apt-get -yq --no-install-recommends install  pandoc  make \
#     && apt-get clean \
#     && apt-get autoremove -yq \
#     && rm -rf /var/lib/apt/lists/* 

# RUN python3 -m pip install \
#     altair \
#     flask  \
#     gensim \
#     graphviz \
#     h5py \
#     ipykernel \
#     ipywidgets \
#     isort \
#     Jinja2 \
#     keras-tuner \
#     matplotlib \
#     nbsphinx \
#     networkx \
#     nltk \
#     numpy \
#     pandas \
#     pandas-datareader \
#     pandas-gbq \
#     pandas-profiling \
#     progressbar2 \
#     pydotplus  \
#     pygments \
#     pytest \
#     pyyaml \
#     scikit-learn \
#     scipy \
#     seaborn \
#     sklearn-pandas \
#     snowballstemmer \
#     spacy \
#     sphinx_copybutton \
#     sphinx-rtd-theme \ 
#     sphinx==4.0.3 \
#     SQLAlchemy \
#     statsmodels \
#     tensorboard \
#     tensorflow \
#     tensorflow_io \
#     tensorflow-addons \
#     tensorflow-datasets \
#     tensorflow-estimator \
#     tensorflow-hub \
#     tensorflow-text \
#     textblob \
#     widgetsnbextension \
#     wordcloud

# RUN pip install -q git+https://github.com/tensorflow/docs

# RUN pip install -q git+https://github.com/tensorflow/examples.git

# RUN apt update \
#     && apt -yq --no-install-recommends install  graphviz \
#     && apt clean \
#     && apt autoremove -yq \
#     && rm -rf /var/lib/apt/lists/* 
