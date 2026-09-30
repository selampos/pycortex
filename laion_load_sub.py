from laion_fmri import load_subject

sub = load_subject("sub-01")

betas = sub.get_betas(
    session="ses-01",
    streaming=True
)

print(betas)