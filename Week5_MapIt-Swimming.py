#!/usr/bin/env python
# coding: utf-8

# In[53]:


#Map It! - Butterfly Stroke in Swimming

import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

# d in meters

day = ['Day 1','Day 2','Day 3','Day 4','Day 5', 'Day 6']
meters = [25, 25.5, 25.5, 50, 50.5, 75]

#establishing features
plt.bar(day, meters, label = 'Distance per Day', color = 'Turquoise')
plt.xticks(day)
plt.legend()
plt.show()


# In[ ]:




