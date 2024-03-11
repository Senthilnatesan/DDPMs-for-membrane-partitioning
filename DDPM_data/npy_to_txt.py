import numpy as np

def npy_to_txt(npy_filename, txt_filename):
    # Load the npy file
    data = np.load(npy_filename)
    
    # Check if the data is 3D
    if data.ndim == 3:
        with open(txt_filename, 'w') as f:
            for i in range(data.shape[0]):
                np.savetxt(f, data[i], fmt='%.4f', delimiter='\t')
                if i != data.shape[0] - 1:  # Avoid adding an extra newline at the end of the file
                    f.write("\n")
    elif data.ndim in [1, 2]:
        # Save the array to a txt file as usual
        np.savetxt(txt_filename, data, fmt='%.4f', delimiter='\s+')
    else:
        raise ValueError(f"Unsupported array dimension: {data.ndim}")

# Example usage:
npy_filename = "salm_10_final.npy"
txt_filename = "salm_10_final.txt"
npy_to_txt(npy_filename, txt_filename)

