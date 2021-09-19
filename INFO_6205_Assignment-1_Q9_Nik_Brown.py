'''
    Authour : Rishabh Modi
    Date : 09/19/2021

    The World Cup is changing its playoff format using the Gale-Shapley matching algorithm. 
    The eight best teams from groups A,B & C, 
    called Super Group 1, will be matched against the eight best teams from groups D, E & F, 
    called Super Group 2, using the Gale-Shapley matching algorithm. 
    Further social media will be used to ask fans, media, players and coaches 
    to create a ranking of which teams they would most like to see play their favorite team.
'''

# The list of teams in both the super groups
Super_Group_1 = [ 't1' , 't2' , 't3' , 't4' , 't5' , 't6' , 't7' , 't8' ]
Super_Group_2 = [ 's1' , 's2' , 's3' , 's4' , 's5' , 's6' , 's7' , 's8' ]

# Preferences 
preference_dict_super_grp_1 = {
    't1': ['s2', 's3', 's4', 's5', 's6', 's7', 's8', 's1'],
    't2': ['s3', 's4', 's5', 's6', 's7', 's8', 's1', 's2'],
    't3': ['s4', 's5', 's6', 's7', 's8', 's1', 's2', 's3'],
    't4': ['s5', 's6', 's7', 's8', 's1', 's2', 's3', 's4'],
    't5': ['s6', 's7', 's8', 's1', 's2', 's3', 's4', 's5'],
    't6': ['s7', 's8', 's1', 's2', 's3', 's4', 's5', 's6'],
    't7': ['s8', 's1', 's2', 's3', 's4', 's5', 's6', 's7'],
    't8': ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8']
}

preference_dict_super_grp_2 = { 
    's1': ['t2', 't3', 't4', 't5', 't6', 't7', 't8', 't1'],
    's2': ['t3', 't4', 't5', 't6', 't7', 't8', 't1', 't2'],
    's3': ['t4', 't5', 't6', 't7', 't8', 't1', 't2', 't3'],
    's4': ['t5', 't6', 't7', 't8', 't1', 't2', 't3', 't4'],
    's5': ['t6', 't7', 't8', 't1', 't2', 't3', 't4', 't5'],
    's6': ['t7', 't8', 't1', 't2', 't3', 't4', 't5', 't6'],
    's7': ['t8', 't1', 't2', 't3', 't4', 't5', 't6', 't7'],
    's8': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8']
}

'''
    Find a Gale-Shapley implementation in python on Github and modify it so that the eight Super Group 1 teams will be matched against the eight Super Group 2 teams. You can make up the preference lists for each team. Make sure you cite any code you use or state that you wrote it from scratch if you did. 
'''
