schools = {'NLCS': 'North London Collegiate School',
            'BHA': 'Branksome Hall Asia',
            'KIS': 'Korea International School',
            'SJA': 'St. Johnsbury Academy'}

school = input()

if school in schools:
    print(schools[school])