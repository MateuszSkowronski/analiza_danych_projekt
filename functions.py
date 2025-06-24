import pandas as pd

def hours(dt):
    minute=dt.minute
    if minute<45:
        return dt.replace(minute=0)
    else:
        return (dt+pd.Timedelta(hours=1)).replace(minute=0)
    