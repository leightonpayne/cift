import gemmi
import sys

input_cif = sys.argv[1]
output_cif = sys.argv[2]
target_model = sys.argv[3]
target_chain = sys.argv[4]

st = gemmi.read_structure(input_cif)

for mo in st:
    if mo.name == target_model:
        for ch in mo:
            if ch.name != target_chain:
                del ch[:]
    else:
        del mo [:]

st.make_mmcif_document().write_file(output_cif)

