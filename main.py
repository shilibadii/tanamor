import os
import pandas as pd
import tensorflow as tf
import numpy as np
df = pd.read_csv(os.path.join('jigsaw-toxic-comment-classification-challenge','train.csv', 'train.csv'))
df.head()