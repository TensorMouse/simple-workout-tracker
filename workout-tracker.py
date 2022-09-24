import pandas as pd
import numpy as np

if __name__ == "__main__":
    workout = pd.DataFrame()
    while True:
        try:
            workout=pd.read_csv('workout_history.csv').T
        except FileNotFoundError as e:
            workout=pd.DataFrame()
        workout_part=pd.Series()
        workout_part['exercise'] = input('input exercise: ')
        if workout_part['exercise']=='stop':
            break

        workout_part['date'] = input('input date: ')
        set_number=0
        while True:
            set_number+=1
            workout_part['set '+str(set_number)+' weight']=input('input weight: ')
            if workout_part['set '+str(set_number)+' weight'] == 'stop':
                workout_part['set '+str(set_number)+' weight'] = np.nan
                break
            workout_part['set '+str(set_number)+' reps']=input('input reps: ')
            if workout_part['set '+str(set_number)+' reps'] == 'stop':
                workout_part['set '+str(set_number)+' reps'] == np.nan
                break
            workout_part['set '+str(set_number)+' rest']=input('input rest: ')
            if workout_part['set '+str(set_number)+' rest'] == 'stop':
               workout_part['set '+str(set_number)+' rest'] = np.nan
               break
        workout=pd.concat([workout,workout_part],axis=1)
        workout.T.to_csv('workout_history.csv',index=False)
        print(workout)

