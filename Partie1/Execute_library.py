#%%
## Intallation et exécution de la bibliothèque surf_scrap
import os
from surf_scrap import scrape_surf_report
#%%
# Exemple d'utilisation de la fonction scrape_surf
url = "https://www.surf-report.com/meteo-surf/carcans-plage-s1013.html"
df = scrape_surf_report(url, output_csv_path=None)

# %%
