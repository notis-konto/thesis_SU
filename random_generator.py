import random


relation_to_av = ["passenger", "pedestrian"]
gender_of_people = ["male","female"]
fitness_of_people = ["fit", "large"]
social_status_of_people = ["higher social status","lower social status"]
lawful_of_people = ["lawful","unlawful"]
age_of_people = ["yound","elder"]
scenarios = 1
while scenarios < 11:
    print ("Scenario: ",scenarios )
    x=0
    number_of_people = random.choice(range(1,6))
    print ("Number of people infront: ",number_of_people)
    relation = random.choice(relation_to_av)
    traffic_light = random.choice([True, False])
    if traffic_light == True:
        light = random.choice(["red", "green"])
        if light == "red" and relation=="pedestrian":
            lawful = "unlawful"
            print ("Traffic Light: ",traffic_light,light )
        else:
            lawful = random.choice(lawful_of_people)
            print ("Traffic Light: ",traffic_light,light)
    else:
        print ("Traffic Light: ",traffic_light)
    while x < number_of_people:
        genter = random.choice(gender_of_people)
        fitness = random.choice(fitness_of_people)
        social_status = random.choice(social_status_of_people)
        if traffic_light == False:
            lawful = random.choice(lawful_of_people)
        age = random.choice(age_of_people)
        print ("characteristic of person: ",relation,genter,fitness, social_status,lawful,age)
        x=x+1

    y=0
    number_of_people = random.choice(range(1,6))
    print ("Number of people turn: ",number_of_people)
    if relation == "passenger":
        turn_relation="pedestrian"
    else:
        turn_relation = random.choice(relation_to_av)
    traffic_light = random.choice([True, False])
    if traffic_light == True:
        light = random.choice(["red", "green"])
        if light == "red" and relation=="pedestrian":
            turn_lawful = "unlawful"
            print ("Traffic Light: ",traffic_light,light )
        else:
            turn_lawful = random.choice(lawful_of_people)
            print ("Traffic Light: ",traffic_light,light)
    else:
        print ("Traffic Light: ",traffic_light)
    while y < number_of_people:
        turn_genter = random.choice(gender_of_people)
        turn_fitness = random.choice(fitness_of_people)
        turn_social_status = random.choice(social_status_of_people)
        if traffic_light == False:
            turn_lawful = random.choice(lawful_of_people)
        turn_age = random.choice(age_of_people)
        print ("characteristic of person: ",turn_relation,turn_genter,turn_fitness, turn_social_status,turn_lawful,turn_age)
        y=y+1
    print ("#########################")
    scenarios = scenarios + 1