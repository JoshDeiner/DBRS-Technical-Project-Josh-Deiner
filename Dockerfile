FROM jupyter/base-notebook

WORKDIR work

COPY running_coding running_coding
COPY requirements.txt .

# ENTRYPOINT ["bash"]

RUN conda install --yes --file requirements.txt

# CMD ["jupyter", "notebook"]
