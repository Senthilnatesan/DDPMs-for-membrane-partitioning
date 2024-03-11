# DDPMs-for-membrane-partitioning
This repository contains, input and output files for implementing denoising diffusion probabilistic models (DDPMs) for membrane partitioning. The code for running the model is an adaption of DDPM_REMD at https://github.com/tiwarylab/DDPM_REMD with slight modifications.

#### DDPM_MP 

This folder contains the jupyter notebook for running the DDPM model and the denoising_diffusion_pytorch.py

#### DDPM_data

This folder contains the input numpy files, output files from DDPMs and model checkpoints. Post-processing scripts include npy_to_txt.py for converting the final numpy file from the DDPM to a text file and extract_centers_z.sh to split into sepearate files based on the restraint center.

#### US_data

Contains output files from initial umbrella sampling simulations.

#### Citations
```
@article{
doi:10.1073/pnas.2203656119,
author = {Yihang Wang  and Lukas Herron  and Pratyush Tiwary },
title = {From data to noise to data for mixing physics across temperatures with generative artificial intelligence},
journal = {Proceedings of the National Academy of Sciences},
volume = {119},
number = {32},
pages = {e2203656119},
year = {2022}
} 
```
```
@misc{ho2020denoising,
    title={Denoising Diffusion Probabilistic Models},
    author={Jonathan Ho and Ajay Jain and Pieter Abbeel},
    year={2020},
    eprint={2006.11239},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```
