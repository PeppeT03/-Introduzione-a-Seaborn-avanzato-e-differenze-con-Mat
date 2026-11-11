# Importazione delle librerie
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Impostiamo il seme per ottenere sempre gli stessi numeri casuali
np.random.seed(42)

# Creiamo i dati
Categoria = np.repeat(["A", "B", "C"], 10)
Valore = np.random.randint(10, 100, size=30)
Gruppo = np.tile(["X", "Y"], 15)

# Creiamo il DataFrame
df = pd.DataFrame({
    "Categoria": Categoria,
    "Valore": Valore,
    "Gruppo": Gruppo
})

# CALCOLO DELLA MEDIA CON PANDAS
# Raggruppiamo i dati per categoria e calcoliamo
# la media dei valori di ogni categoria
media_categoria = df.groupby("Categoria")["Valore"].mean()


# GRAFICO CON MATPLOTLIB

plt.figure(figsize=(6, 4))

# Disegniamo le barre utilizzando le medie già calcolate
plt.bar(
    media_categoria.index,
    media_categoria.values,
    color="skyblue",
    edgecolor="black"
)

# Personalizzazione del grafico
plt.title("Valore medio per categoria (Matplotlib)")
plt.xlabel("Categoria")
plt.ylabel("Valore medio")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Sistemiamo gli spazi e salviamo il grafico
plt.tight_layout()
plt.savefig("esercizio1matplot.png")
plt.show()


# GRAFICO CON SEABORN

# Seaborn calcola automaticamente le medie
# e distingue i gruppi X e Y attraverso hue
sns.barplot(
    data=df,
    x="Categoria",
    y="Valore",
    hue="Gruppo",
    palette="viridis"
)

plt.tight_layout()
plt.savefig("esercizio1sns.png")
plt.show()