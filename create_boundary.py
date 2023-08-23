import helpers as hp
import pandas as pd
import numpy as np 


def boundary():
    # df = pd.read_csv ('/content/Input/Node - Time Series.csv')
    user_file = hp.file_upload("Upload fill model time series data")
    df = pd.read_csv(user_file)
    boundary_stage_point = df.reindex(df.columns.tolist() + ['Year', 'Month', 'Day'], axis=1)
    boundary_stage_point = boundary_stage_point.rename(columns={'Sim': 'Set', 
                                                                'Node Name': 'Parent', 
                                                                'Relative Time [hrs]': 'Hour', 
                                                                'Stage [ft]': 'Stage'})
    boundary_stage_point = boundary_stage_point[['Set', 'Parent', 'Year', 'Month', 'Day', 'Hour', 'Stage']]

    nodes = df['Node Name'].unique()
    simulations = df['Sim'].unique()

    boundary_stage_set = pd.DataFrame(simulations, columns =['Name']) 
    boundary_stage_set['Comment'] = np.nan
   
    combined_list = []
    for sim in simulations:
        for node in nodes:
            row = [sim, node, '']
            combined_list.append(row)
    boundary_stage = pd.DataFrame(combined_list, columns =['Parent', 'Name', 'Comment']) 

    boundary_stage_point.to_csv('/content/Output/Boundary_Files/Collection-BoundaryStage_Point.csv',
                    encoding='utf-8', index=False)
    boundary_stage_set.to_csv('/content/Output/Boundary_Files/Collection-BoundaryStageSet.csv',
                    encoding='utf-8', index=False)
    boundary_stage.to_csv('/content/Output/Boundary_Files/Collection-BoundaryStage.csv',
                    encoding='utf-8', index=False)