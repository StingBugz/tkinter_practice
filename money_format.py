a = 52123562.00

def formatrupiah(value):
    y = str(value)
    if len(y) <= 3:
         value = y
         return value
    else:
        #tidak di kasih index setelah atau sebelum : maka dihitung sampai akhir(sesudah :) atau dari awal(sebelum :)
        p = y[-3:]
        q = y[:-3] 
        value = formatrupiah(q) + "." + p
        # print(p)
        # print(q)
        # print()
        return value
formated = formatrupiah(int(a))
print(formated)