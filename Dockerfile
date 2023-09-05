FROM pytorch/pytorch

# Install Jupyter and other necessary dependencies
RUN pip install jupyter
RUN pip install matplotlib
RUN pip install transformers

WORKDIR /app
COPY . /app

# Expose the Jupyter port
EXPOSE 8888

# Start Jupyter notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
