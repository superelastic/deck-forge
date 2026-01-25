import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# Data
companies = ['Company D', 'Company C', 'Company B', 'Company A']
shares = [15, 22, 28, 35]
colors = ['#90a4ae', '#90a4ae', '#90a4ae', '#1976d2']  # Highlight A

# Create figure
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(companies, shares, color=colors)

# Styling for slides
ax.set_xlabel('Market Share (%)', fontsize=14)
ax.set_title('Market Share by Company', fontsize=16, fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(labelsize=12)
ax.set_xlim(0, 45)

# Add value labels
for bar, val in zip(bars, shares):
    ax.text(val + 1, bar.get_y() + bar.get_height()/2,
            f'{val}%', va='center', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('market_share.svg', format='svg', transparent=True)
plt.close()
