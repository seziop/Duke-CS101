def howMany(meals, restaurant):
    meals = list(set(meals))
    counter = 0
    for i in meals:
        mealsSeperated = i.split(':')
        if mealsSeperated[1] == restaurant:
            counter += 1
    return counter