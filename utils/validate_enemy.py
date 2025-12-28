def ValidateEnemy ():
    chosenEnemy = input("Enemy (soldier / knight / demigod / dragon):  ").lower()
    exists = False

    for key, _ in enemies.items():
        if key == chosenEnemy:
            exists = True
    
    if exists is False:
        print('Enemy does not exist, choose again!')
        ValidateEnemy()
    else: 
        return chosenEnemy 