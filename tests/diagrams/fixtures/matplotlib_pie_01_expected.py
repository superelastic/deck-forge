import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# Data
categories = ['Salaries', 'Operations', 'Marketing', 'R&D']
values = [55, 20, 15, 10]
colors = ['#1976d2', '#42a5f5', '#90caf9', '#bbdefb']
explode = (0.05, 0, 0, 0)  # Explode Salaries

# Create figure
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    values,
    labels=categories,
    autopct='%1.0f%%',
    explode=explode,
    colors=colors,
    startangle=90,
    textprops={'fontsize': 12}
)

# Style the percentage labels
for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_color('white')

ax.set_title('Annual Budget Allocation', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('budget_allocation.svg', format='svg', transparent=True)
plt.close()
