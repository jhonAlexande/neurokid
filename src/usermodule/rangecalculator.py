def get_range(meses):
  if meses<=1:
    return 1
  if meses>1 and meses<=3:
    return 2
  if meses>3 and meses<=6:
    return 3
  if meses>6 and meses<=9:
    return 4
  if meses>9 and meses<=12:
    return 5
  if meses>12 and meses<=18:
    return 6
  if meses>18 and meses<=24:
    return 7
  if meses>24 and meses<=36:
    return 8
  if meses>36 and meses<=48:
    return 9
  if meses>48 and meses<=60:
    return 10
  if meses>60 and meses<=72:
    return 11
  if meses>72 and meses<=84:
    return 12