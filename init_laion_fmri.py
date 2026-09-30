from laion_fmri.config import dataset_initialize, get_data_dir
from laion_fmri.download import download

dataset_initialize("/mnt/c/Users/rendo/Documents/BA/laion_fmri_data")

print(get_data_dir())       # → "./laion_fmri_data"

download(
    subject="sub-01",
    ses="ses-01",
    include_anatomical=True,
    include_freesurfer=True,
    n_jobs=4,
)