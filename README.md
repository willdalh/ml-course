## Building and running the docker image locally

```bash
docker build -t ai-crash-course .
```
This will install PyTorch and other necessary libraries in a Python environment.

To run the container:
```
docker run -p 8888:8888 --gpus all ai-crash-course
```
Then do the following:
- Follow the instructions in the terminal output.
- Select `concepts.ipynb` when seen in the browser.

## Running through Google Colab
If your computer does not have a dedicated graphics card installed, but you want to test the code with a GPU, you can run it through Google Colab. You need a Google account for this. 

- Open https://colab.research.google.com/github/willdalh/deep-learning-concepts/blob/main/concepts.ipynb.
- Select `Runtime` in the navigation bar.
- Click `Change Runtime type`.
- Select `T4 GPU` in the popup and click save.