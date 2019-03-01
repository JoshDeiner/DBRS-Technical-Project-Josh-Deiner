FROM jupyter/base-notebook


COPY . /running_coding


# Run python when the container launches
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]

RUN conda install --quiet --yes -c \
    conda-forge osmnx dask
RUN fc-cache
RUN fc-list

EXPOSE 8888

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]
