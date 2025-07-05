import pandas as pd

def hours(dt):
    minute=dt.minute
    if minute<45:
        return dt.replace(minute=0)
    else:
        return (dt+pd.Timedelta(hours=1)).replace(minute=0)
    
def custom_round_hour(t):
    if pd.isna(t):
        return None
    hour = t.hour
    minute = t.minute
    return hour if minute <= 30 else hour + 1