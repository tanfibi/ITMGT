'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    isFollowing = False
    isFollowed = False
    ret = "" 
    if (social_graph.get(from_member)!= None): 
        
        if (to_member in social_graph.get(from_member).get("following")): 
            isFollowing = True
        if (from_member in social_graph.get(to_member).get("following")): 
            isFollowed = True
        
        if (isFollowing == True and isFollowed == False):
            ret = "follower"
        elif (isFollowing == False and isFollowed == True):
            ret = "followed by"
        elif (isFollowing == True and isFollowed == True):
            ret = "friends"
        else:
            ret = "no relationship"
        
    else:        
        print(social_graph.get(from_member))
    
    return ret


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    import numpy as np
    def Rows(board):
        for row in board:
            if len(set(row)) == 1:
                return row[0]
        return 0

    def Columns(board):
        for col in board:
            if len(set(col)) == 1:
                return col[0]
        return 0
        
    def Diagonals(board):
        if len(set([board[i][i] for i in range(len(board))])) == 1:
            return board[0][0]
        if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
            return board[0][len(board)-1]
        return "NO WINNER"

    rowBoard = board 
    colBoard = np.transpose(board)

    result = Rows(board)

    if (result):
        return result
    else:
        result = Columns(colBoard)
        if (result):
            return result

    return Diagonals(board)



def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    travel_time = 0
    middle_flag = 0
    keyList = list(route_map.keys())
    for key in keyList:
        if(key[0] == first_stop and key[1] == second_stop):
            travel_time += route_map[(key)]["travel_time_mins"]
            break
        if (key[0]==first_stop):
            travel_time += route_map[key]["travel_time_mins"]
            middle_flag = 1
        elif(key[1] == second_stop):
            travel_time += route_map[key]["travel_time_mins"]
            middle_flag = 0
        elif(middle_flag == 1 and key[0] != first_stop and key[1] != second_stop):
            travel_time += route_map[key]["travel_time_mins"]
        print(travel_time)
    return travel_time