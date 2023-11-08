
## Building and running
The course can be run both locally and through Google Colab.

### Building and running the docker image locally

```bash
docker build -t ml-course .
```
This will install PyTorch and other necessary libraries in a Python environment.

To run the container:
```
docker run -p 8888:8888 --gpus all ml-course
```
Then do the following:
- Follow the instructions in the terminal output.
- Select `concepts.ipynb` when seen in the browser.

### Running through Google Colab
If your computer does not have a dedicated graphics card installed, but you want to test the code with a GPU, you can run it through Google Colab. You need a Google account for this. 

- Open https://colab.research.google.com/github/willdalh/deep-learning-concepts/blob/main/concepts.ipynb.
- Select `Runtime` in the navigation bar.
- Click `Change Runtime type`.
- Select `T4 GPU` in the popup and click save.


## Instructions for running code cells:
- VSCode and Google Colab
    - Select a cell and click the ▶️ button located to the left of the cell.
- Jupyter Notebook in the browser
    - Select a cell and click the ▶️ button in the navigation menu at the top of the window.
- Shortcut for all mentioned above
    - Select a cell and press `CTRL-Enter`.