# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 10:06:51 2020

@author: xXJaneXx
"""


from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app_toy import HDapp

layout = [dcc.Markdown("""
### References
1. 	Hervatis V. Project management and tools for HI [Internet]. Stockholm; 2020 Sep [cited 2020 Sep 22]. Available from: https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1365-2934.2006.00624.x
2. 	Hollmén J. PROHI 2020: Assignment for Data Mining [Internet]. Stockholm; 2020 Sep [cited 2020 Sep 22]. Available from: http://archive.ics.uci.edu/ml/datasets/Heart+Disease
3. 	WHO. Cardiovascular diseases (CVDs) [Internet]. 2017 [cited 2020 Sep 18]. Available from: https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)
4. 	Chaurasia V, Pal S. Data Mining Approach to Detect Heart Diseases. Int J Adv Comput Sci Inf Technol. 2013 Nov;2(4):56–66
5.  How to refer - Rapid access chest pain clinic [Internet]. [cited 2020 Oct 27]. Available from: https://www.uclh.nhs.uk/OURSERVICES/SERVICEA-Z/CARDIACS/RACPC/Pages/refer.aspx
 
""")]
