# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r9FdoausTIfK6HXiu4HoSl0gQSA-LCvx
"""

import pandas as pd
baza={
    "F.I.SH": ['Karimov Abdulaziz', 'Ibroximov Ramzbek', 'Akmalova Mahliyo', 'Rustamova Oygul', 'Ahmadaliyeva Sarvinoz', 'Olimjonov Otabek', 'Nomonjonov Asilbek', 'Razzoqova Asila', 'Yunusov Muhammadin', 'Sobirov Anvar'   ],
    "Yoshi": ['18', '17', '15', '19', '11', '20', '13', '17', '23', '15'   ],
    "Jinsi": ['erkak', 'erkak', 'ayol', 'ayol', 'ayol', 'erkak', 'erkak', 'ayol', 'erkak', 'erkak'   ],
    "O'qish joyi": ['T.D.T.U', '26-maktab', '37-maktab', 'TATU', 'Prezident Maktabi', 'FarDU', '41-maktab', '3-IDUM', 'ToshMI', '33-maktab'   ]


}
fb = pd.DataFrame(baza)
print(fb)

filtr = fb[(fb['Jinsi']=="erkak")&(fb['Yoshi']>"17")]
print(filtr)