import requests
import csv

# URL de l'API à requêter
api_url = "https://exemple.com/api/data"

# Faire la requête à l'API
response = requests.get(api_url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()  # Convertir la réponse en JSON
    csv_file = "data.csv"

    # Écrire les données dans un fichier CSV
    with open(csv_file, "w", newline="") as file:
        csv_writer = csv.writer(file)
        
        # Écrire l'en-tête du CSV (si nécessaire)
        csv_writer.writerow(data[0].keys())
        
        # Écrire les données
        for row in data:
            csv_writer.writerow(row.values())
    
    print(f"Les données ont été enregistrées dans {csv_file}.")
else:
    print("La requête à l'API a échoué.")