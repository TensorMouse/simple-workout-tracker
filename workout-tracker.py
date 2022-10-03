import pandas as pd
import numpy as np

def load_workout_history(path='workout_history.csv'):
    try:
        workout=pd.read_csv('workout_history.csv').T
    except FileNotFoundError as e:
        workout=pd.DataFrame()
    return(workout)

def enter_stats():
    weight=input('input weight, s for stop, enter for 6: ') or "6"
    if weight == 's':
        return([np.nan,np.nan,np.nan])
    
    reps=input('input reps, s for stop, enter for 10: ') or "10"
    if weight == 's':
        return([weight,np.nan,np.nan])
    
    rest=input('input rest, s for stop, enter for 60 ') or "60"
    if weight == 's':
        return([weight,reps,np.nan])
    
    return([weight,reps,rest])




if __name__ == "__main__":
    workout = pd.DataFrame()
    while True:
        workout = load_workout_history()
        workout_part=pd.Series()
        workout_part['exercise'] = input('input exercise: ')
        if workout_part['exercise']=='stop':
            break
        workout_part['date'] = input('input date: ')
        set_number=0
        while True:
            set_number+=1
            workout_stats=enter_stats()
            if workout_stats[0]==np.nan:
                break
            workout_part['set '+str(set_number)+': weight']=workout_stats[0]
            workout_part['set '+str(set_number)+': reps']=workout_stats[1]
            workout_part['set '+str(set_number)+': rest']=workout_stats[2]
            workout=pd.concat([workout,workout_part],axis=1)
            print(workout_stats)
            if np.nan in workout_stats:
                break
        workout.T.to_csv('workout_history.csv',index=False)
        print(workout)

