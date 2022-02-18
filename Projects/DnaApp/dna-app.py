######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

######################
# Page Title
######################

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# Compteur de nucléotides: 
Cette application compte le nombre de nucléotides présents dans une sequence ADN.
***
""")


######################
# Input Text Box
######################

st.header("Entrer une séquence d'ADN")

sequence_input = ">Séquence d'ADN\nGCACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence d'ADN: ", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")


st.header('INPUT (Séquence ADN)')
sequence


st.header('OUTPUT (Nombre de nucléotides)')

# Sous forme de dictionnaire
st.subheader('1. Dictionnaire')


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d


X = DNA_nucleotide_count(sequence)

X

# 2. Sous forme de text
st.subheader('2. Texte')
st.write('Il y a ' + str(X['A']) + ' adenine (A)')
st.write('Il y a ' + str(X['T']) + ' thymine (T)')
st.write('Il y a ' + str(X['G']) + ' guanine (G)')
st.write('Il y a ' + str(X['C']) + ' cytosine (C)')

# 3. Sous forme de df
st.subheader('3. DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'nombres'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

# 4. Histogramme à partir d'altair
st.subheader('4. Histogramme')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='nombres'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)
