# Importazione delle librerie
import matplotlib.pyplot as plt
import seaborn as sns

# Carichiamo il dataset ed eliminiamo le righe incomplete
penguins = sns.load_dataset("penguins").dropna()

# Calcoliamo la matrice di correlazione
# numeric_only=True considera soltanto le colonne numeriche
corr = penguins.corr(numeric_only=True)
print(corr)


# PRIMO GRAFICO: PAIRPLOT

grafico = sns.pairplot(
    data=penguins,
    hue="species",            # Distingue le tre specie
    diag_kind="kde",          # Distribuzione KDE sulla diagonale
    palette="Set2",           # Palette dei colori
    height=2.6,               # Altezza dei singoli grafici
    aspect=1.05,              # Rapporto larghezza/altezza
    plot_kws={"alpha": 0.7, "s": 35}  # Trasparenza e dimensione dei punti
)

# Aggiungiamo il titolo generale
grafico.fig.suptitle(
    "Confronto delle caratteristiche dei pinguini",
    y=1.02
)

# Creiamo una sola legenda e la posizioniamo all'esterno
grafico.add_legend(
    title="Specie",
    loc="center left",
    bbox_to_anchor=(1.02, 0.5)
)

# Lasciamo spazio alla legenda e al titolo
grafico.fig.subplots_adjust(right=0.88, top=0.92)

# Salviamo e mostriamo il grafico
grafico.fig.savefig("esercizio3.png", bbox_inches="tight")
plt.show()


# SECONDO GRAFICO: HEATMAP

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr,
    annot=True,         # Mostra i valori numerici nelle celle
    cmap="coolwarm",    # Colori per correlazioni positive e negative
    center=0,           # Lo zero è il centro della scala cromatica
    linewidths=0.5      # Separazione tra le celle
)

plt.title("Matrice di correlazione dei pinguini")
plt.tight_layout()

# Salviamo e mostriamo il grafico
plt.savefig("esercizio3heatmap.png", bbox_inches="tight")
plt.show()