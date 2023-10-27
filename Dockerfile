FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime

WORKDIR /app
COPY . /app

# Install Jupyter and other necessary dependencies
RUN pip install -r requirements.txt

# Expose the Jupyter port
EXPOSE 8888

# Start Jupyter notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
