import pandas as pd

df = pd.read_csv("C:\\Users\\ROHITH\\Downloads\\Employee.csv")

grouped = df.groupby('Department')['Hours_Worked'].sum().reset_index()
grouped = grouped.sort_values(by='Hours_Worked', ascending=False)
print("Total hours by department:\n", grouped)

pivot = pd.pivot_table(df, values='Hours_Worked', index='Department',
                       aggfunc={'Hours_Worked': ['sum', 'mean', 'max', 'min']})
pivot.columns = ['Total_Hours', 'Average_Hours', 'Max_Hours', 'Min_Hours']
print("\nPivot Table Summary:\n", pivot)

def highlight_max(s):
    is_max = s == s.max()
    return ['background-color: yellow' if v else '' for v in is_max]

styled = grouped.style.apply(highlight_max, subset=['Hours_Worked'])
styled_pivot = pivot.style.apply(highlight_max, subset=['Total_Hours'])

# Save to Excel instead of using display()
styled.to_excel("grouped_report.xlsx", index=False)
styled_pivot.to_excel("pivot_summary.xlsx")
