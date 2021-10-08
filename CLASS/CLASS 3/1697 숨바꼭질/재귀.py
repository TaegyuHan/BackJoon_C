def find_count(current_location):
    
    if current_location == brother:
        return
    
    global result
    result += 1
    print(current_location)
    tmp_distance = abs(me - brother)
    
    for next_location in next_time(current_location, brother):
        me = next_location[0]
        for next_me in [me*2, me + 1, me - 1]:
            if (tmp := abs(next_me - brother)) <= tmp_distance:
                tmp_distance = tmp
                current_location = next_location[0]
                
    find_count(current_location)