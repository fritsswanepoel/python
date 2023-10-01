
Reference:
https://thepythoncode.com/article/generate-images-from-text-stable-diffusion-python#stable-diffusion-pipeline

Detours:
Had to enable long file paths in Windows
Had to Install Microsoft Visual C++ 14.0 or greater
Had to install Visual Studio
Had to install CUDA
Had to install the cuDNN library
- https://saturncloud.io/blog/what-is-assertionerror-torch-not-compiled-with-cuda-enabled/
- https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html

Packages:
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

pip install diffusers transformers accelerate

pip install -q xformers==0.0.16rc425
