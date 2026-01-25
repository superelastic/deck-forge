import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# Data
years = ['2020', '2021', '2022', '2023', '2024']
revenue = [10, 15, 25, 35, 50]

# Create figure
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(years, revenue, marker='o', linewidth=2.5, markersize=8, color='#1976d2')
ax.fill_between(years, revenue, alpha=0.1, color='#1976d2')

# Styling for slides
ax.set_ylabel('Revenue ($M)', fontsize=14)
ax.set_title('Revenue Growth 2020-2024', fontsize=16, fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(labelsize=12)

# Highlight 2024
ax.annotate('$50M', xy=('2024', 50), xytext=('2023', 55),
            arrowprops=dict(arrowstyle='->', color='#d32f2f'),
            fontsize=12, fontweight='bold', color='#d32f2f')

plt.tight_layout()
plt.savefig('revenue_growth.svg', format='svg', transparent=True)
plt.close()
