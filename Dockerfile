FROM jupyter/base-notebook

WORKDIR work

# Files for jupyter
COPY notebooks notebooks
COPY requirements.txt .

# For testing purposes
COPY resources resources
COPY src src

# Install modules using conda
RUN conda install --yes --file requirements.txt

# Install module using pip
RUN pip install import-ipynb

# Expose port from the container
EXPOSE 8881

# Run the notebook on exposed port
CMD ["jupyter", "notebook", "--port=8881"]
