import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.set_theme(style="whitegrid")



plt.figure(figsize=(6, 4))
sns.heatmap(tips.corr(), annot=True, cmap="coolwarm")
plt.title("Heatmap: Correlation Matrix")
plt.show()
