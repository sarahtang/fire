import pandas as pd
import numpy as np
from google.colab import files
uploaded = files.upload()

import io
terra = pd.read_csv(io.BytesIO(uploaded["fire_nrt_V1_83401.csv"]))

# considered spread if there is a fire within the next day of +- .5 lat and long
# put out if fire within day is +- .5 lat and long