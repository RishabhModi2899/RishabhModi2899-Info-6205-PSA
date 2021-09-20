'''
    @Authour : Rishabh Modi
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

# List to keep track of all free teams from super group 1 
free_teams_super_group_1 = []
free_teams_super_group_2 = []

def init_free_teams(): 
    # Function to initialize the lists
    for i in preference_dict_super_grp_1.keys():
        free_teams_super_group_1.append(i)
    for j in preference_dict_super_grp_2.keys():
        free_teams_super_group_2.append(j)

# Loop through the free teams 1 
matching_results_dict = {} #Empty dictionary to keep track of the matching 

def handle_Matching(team_from_super_group_1 , team_from_super_group_2 , highest_preference_match):
    # Function to handle the matching event and update the list of free teams
    
    # Removing the instances from the free teams lists
    free_teams_super_group_1.remove(team_from_super_group_1)
    free_teams_super_group_2.remove(team_from_super_group_2)
    
    # Adding the entry in the result dictionary
    matching_results_dict[team_from_super_group_2] = team_from_super_group_1

def parse_free_teams_super_group_1():
    # To parse thrugh the free teams of super group 1

    match_index = None
    current_index = None

    for team_var in free_teams_super_group_1:
        temp_list = preference_dict_super_grp_1[team_var]
        for team in temp_list:
            if team in free_teams_super_group_2:
                highest_preference_match = team
                break # Now we have the highest preference match

        for team_sg2_var in free_teams_super_group_2:
            if team_sg2_var in free_teams_super_group_2:
                handle_Matching(team_var , team_sg2_var , highest_preference_match)
            elif team_sg2_var not in free_teams_super_group_2:
                for keys in matching_results_dict.keys():
                    if keys == team_sg2_var:
                        check_preference_var = matching_results_dict[keys] # This variable stores the team form group number 1
                        preference_list_for_team_grp_2 = preference_dict_super_grp_2[keys] # This stores the list of preferences for the team from group number 2
                        for preference_rank in preference_list_for_team_grp_2:
                            if check_preference_var == preference_rank:
                                match_index = preference_list_for_team_grp_2.index(preference_rank)
                            if preference_rank == team_var:
                                current_index = preference_list_for_team_grp_2.index(preference_rank)
                        if match_index > current_index :
                            # Then replace in the matching dictionary and free up the rejected value by adding in the free list 
                            
                                
                    



