mdp = input('Entrez votre mdp : ')
counter = 0

if len(mdp) > 8:
    counter += 1
    
if any(c.islower() for c in mdp):
    counter += 1
    
if any(c.isupper() for c in mdp):
    counter += 1

if any(c.isdigit() for c in mdp):
    counter += 1

if any(c in '@#$%^,;:!?./§ù¨£*µ=+' for c in mdp):
    counter += 1

if counter == 0:
    print('Votre mdp est claqué au sol !')
elif counter == 1:
    print('Votre mdp est faible !')
elif 2 <= counter < 4:
    print('Votre mdp est moyen !')
elif counter == 4:
    print('Votre mdp est fort !')

print('Il a une note de ', counter, '/ 5.')