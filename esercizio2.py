# Importazione delle librerie
import matplotlib.pyplot as plt
import seaborn as sns

# Carichiamo il dataset già disponibile in Seaborn
tips = sns.load_dataset("tips")

# Impostiamo lo stile generale dei grafici
sns.set_theme(style="whitegrid")


# PRIMO GRAFICO: LMPlot

grafico = sns.lmplot(
    data=tips,                 # Dataset utilizzato
    x="total_bill",            # Variabile sull'asse X
    y="tip",                   # Variabile sull'asse Y
    hue="sex",                 # Distingue maschi e femmine
    height=5,                  # Altezza del grafico
    aspect=1.2,                # Rapporto larghezza/altezza
    palette="Set1",            # Palette dei colori
    legend=False,              # Disattiva la legenda automatica
    scatter_kws={"alpha": 0.65},  # Rende i punti trasparenti
    line_kws={"linewidth": 2}    # Aumenta lo spessore delle linee
)

# Personalizziamo titoli ed etichette
grafico.set_axis_labels("Conto totale (€)", "Mancia (€)")
grafico.fig.suptitle("Relazione tra conto e mancia", y=1.03)

# Aggiungiamo una legenda esterna al grafico
grafico.add_legend(
    title="Sesso",
    loc="center left",
    bbox_to_anchor=(1.02, 0.5)
)

# Lasciamo spazio alla legenda sulla destra
grafico.fig.subplots_adjust(right=0.82)

# Salviamo il grafico
grafico.savefig("esercizio2.png")
plt.show()


# SECONDO GRAFICO: VIOLINPLOT

plt.figure(figsize=(7, 5))

# Rappresentiamo la distribuzione delle mance per giorno
sns.violinplot(
    data=tips,
    x="day",
    y="tip",
    palette="coolwarm"
)

# Personalizziamo il grafico
plt.title("Distribuzione delle mance per giorno")
plt.xlabel("Giorno della settimana")
plt.ylabel("Importo della mancia (€)")

# Sistemiamo gli spazi e salviamo
plt.tight_layout()
plt.savefig("esercizio2violin.png")
plt.show()