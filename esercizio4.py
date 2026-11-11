import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Fix del seed per rendere il rumore riproducibile ad ogni esecuzione
np.random.seed(42)

# --- 1. PREPARAZIONE DATI CATEGORICI (VENDITE E PROFITTI) ---
df = pd.DataFrame({
    "Mese": ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu"] * 2,
    "Tipo": ["Vendite"] * 6 + ["Profitti"] * 6,
    "Valore": [
        1200, 1350, 1280, 1500, 1620, 1700,
        240, 280, 260, 320, 350, 390
    ]
})

# --- 2. GRAFICO 1: ANALISI SEGNALE SCIENTIFICO ---
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)

# Individuazione del punto di massimo
indice_picco = np.argmax(y)
x_picco, y_picco = x[indice_picco], y[indice_picco]

# Creazione della figura
plt.figure(figsize=(9, 5))
plt.plot(x, y, label="Segnale", color="#1f77b4", linewidth=2)
plt.axhline(y=0, color="red", linestyle="--", label="Linea di riferimento")

# Annotazione del picco con freccia
plt.annotate(
    "Picco massimo",
    xy=(x_picco, y_picco),
    xytext=(x_picco + 0.6, y_picco + 0.15),
    arrowprops=dict(facecolor="black", arrowstyle="->", connectionstyle="arc3,rad=.2"),
    fontsize=10,
    fontweight="bold"
)

# Rifiniture grafiche
plt.title("Analisi di un segnale scientifico", fontsize=14, pad=12)
plt.xlabel("Tempo (s)", fontsize=11)
plt.ylabel("Ampiezza", fontsize=11)
plt.legend(loc="upper right")
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()

# Salvataggio e chiusura figura
plt.savefig("esercizio4.png", dpi=300)
plt.show()
plt.close()

# --- 3. GRAFICO 2: CONFRONTO VENDITE VS PROFITTI ---
g = sns.catplot(
    data=df,
    x="Mese",
    y="Valore",
    hue="Tipo",
    kind="bar",
    palette="muted",
    height=5,
    aspect=1.5
)

# Personalizzazione dei titoli ed etichette del catplot
g.fig.suptitle("Andamento Mensile: Vendite vs Profitti", y=1.02, fontsize=14)
g.set_axis_labels("Mese", "Valore (€)")

plt.tight_layout()
plt.savefig("esercizio4catplot.png", dpi=300)
plt.show()
plt.close()